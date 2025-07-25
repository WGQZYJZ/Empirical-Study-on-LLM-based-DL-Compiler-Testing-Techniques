import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_195 = relay.var("var_195", dtype = "float32", shape = (8, 1, 6))#candidate|195|(8, 1, 6)|var|float32
uop_196 = relay.tan(var_195.astype('float32')) # shape=(8, 1, 6)
bop_203 = relay.mod(uop_196.astype('float64'), relay.reshape(var_195.astype('float64'), relay.shape_of(uop_196))) # shape=(8, 1, 6)
output = bop_203
output2 = bop_203
func_212 = relay.Function([var_195,], output)
mod['func_212'] = func_212
mod = relay.transform.InferType()(mod)
mutated_mod['func_212'] = func_212
mutated_mod = relay.transform.InferType()(mutated_mod)
var_213 = relay.var("var_213", dtype = "float32", shape = (8, 1, 6))#candidate|213|(8, 1, 6)|var|float32
func_212_call = mutated_mod.get_global_var('func_212')
call_214 = func_212_call(var_213)
output = call_214
func_215 = relay.Function([var_213], output)
mutated_mod['func_215'] = func_215
mutated_mod = relay.transform.InferType()(mutated_mod)
var_461 = relay.var("var_461", dtype = "int32", shape = (14, 1, 1))#candidate|461|(14, 1, 1)|var|int32
var_462 = relay.var("var_462", dtype = "int32", shape = (14, 8, 5))#candidate|462|(14, 8, 5)|var|int32
bop_463 = relay.maximum(var_461.astype('int32'), var_462.astype('int32')) # shape=(14, 8, 5)
uop_468 = relay.rsqrt(bop_463.astype('float32')) # shape=(14, 8, 5)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
const_476 = relay.const([[0.786557],[6.019047],[4.217862],[-8.351557],[-6.215527],[6.545883],[9.456935],[-1.205687],[9.363961],[-0.431115],[3.450678],[2.097752],[-3.660468],[-3.534699],[-2.320405],[4.247182],[-0.077669],[4.636077],[7.961181],[2.905322],[-0.453903],[-2.846023],[2.523216],[1.319543],[-3.192035],[1.578206],[8.052755],[-4.611318],[8.105990],[-1.600733],[1.206672],[8.978238],[-6.004171],[8.939567],[-8.524933],[4.702814],[-6.754650],[4.763946],[-2.555639],[-9.255221],[-2.655973],[-3.792074],[-2.783082],[2.205950],[4.326982],[-6.048935],[0.878390],[4.577842]], dtype = "float32")#candidate|476|(48, 1)|const|float32
call_475 = func_212_call(relay.reshape(const_476.astype('float32'), [8, 1, 6]))
call_477 = func_212_call(relay.reshape(const_476.astype('float32'), [8, 1, 6]))
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
call_480 = func_212_call(relay.reshape(call_475.astype('float32'), [8, 1, 6]))
call_481 = func_212_call(relay.reshape(call_475.astype('float32'), [8, 1, 6]))
output = relay.Tuple([uop_468,call_475,const_476,call_480,])
output2 = relay.Tuple([uop_468,call_477,const_476,call_481,])
func_483 = relay.Function([var_461,var_462,], output)
mod['func_483'] = func_483
mod = relay.transform.InferType()(mod)
var_484 = relay.var("var_484", dtype = "int32", shape = (14, 1, 1))#candidate|484|(14, 1, 1)|var|int32
var_485 = relay.var("var_485", dtype = "int32", shape = (14, 8, 5))#candidate|485|(14, 8, 5)|var|int32
output = func_483(var_484,var_485,)
func_486 = relay.Function([var_484,var_485,], output)
mutated_mod['func_486'] = func_486
mutated_mod = relay.transform.InferType()(mutated_mod)
var_519 = relay.var("var_519", dtype = "int16", shape = (13, 15, 11))#candidate|519|(13, 15, 11)|var|int16
var_520 = relay.var("var_520", dtype = "int16", shape = (13, 15, 11))#candidate|520|(13, 15, 11)|var|int16
bop_521 = relay.add(var_519.astype('int16'), relay.reshape(var_520.astype('int16'), relay.shape_of(var_519))) # shape=(13, 15, 11)
func_483_call = mod.get_global_var('func_483')
func_486_call = mutated_mod.get_global_var('func_486')
const_528 = relay.const([[9],[10],[-3],[4],[-2],[-8],[4],[8],[-9],[-7],[8],[-5],[-6],[-1]], dtype = "int32")#candidate|528|(14, 1)|const|int32
var_529 = relay.var("var_529", dtype = "int32", shape = (560,))#candidate|529|(560,)|var|int32
call_527 = relay.TupleGetItem(func_483_call(relay.reshape(const_528.astype('int32'), [14, 1, 1]), relay.reshape(var_529.astype('int32'), [14, 8, 5]), ), 1)
call_530 = relay.TupleGetItem(func_486_call(relay.reshape(const_528.astype('int32'), [14, 1, 1]), relay.reshape(var_529.astype('int32'), [14, 8, 5]), ), 1)
output = relay.Tuple([bop_521,call_527,const_528,var_529,])
output2 = relay.Tuple([bop_521,call_530,const_528,var_529,])
func_533 = relay.Function([var_519,var_520,var_529,], output)
mod['func_533'] = func_533
mod = relay.transform.InferType()(mod)
var_534 = relay.var("var_534", dtype = "int16", shape = (13, 15, 11))#candidate|534|(13, 15, 11)|var|int16
var_535 = relay.var("var_535", dtype = "int16", shape = (13, 15, 11))#candidate|535|(13, 15, 11)|var|int16
var_536 = relay.var("var_536", dtype = "int32", shape = (560,))#candidate|536|(560,)|var|int32
output = func_533(var_534,var_535,var_536,)
func_537 = relay.Function([var_534,var_535,var_536,], output)
mutated_mod['func_537'] = func_537
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1050 = relay.var("var_1050", dtype = "float64", shape = (14, 13, 9))#candidate|1050|(14, 13, 9)|var|float64
uop_1051 = relay.sqrt(var_1050.astype('float64')) # shape=(14, 13, 9)
output = relay.Tuple([uop_1051,])
output2 = relay.Tuple([uop_1051,])
func_1070 = relay.Function([var_1050,], output)
mod['func_1070'] = func_1070
mod = relay.transform.InferType()(mod)
mutated_mod['func_1070'] = func_1070
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1071 = relay.var("var_1071", dtype = "float64", shape = (14, 13, 9))#candidate|1071|(14, 13, 9)|var|float64
func_1070_call = mutated_mod.get_global_var('func_1070')
call_1072 = func_1070_call(var_1071)
output = call_1072
func_1073 = relay.Function([var_1071], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1216 = relay.var("var_1216", dtype = "bool", shape = (4, 8, 14))#candidate|1216|(4, 8, 14)|var|bool
var_1217 = relay.var("var_1217", dtype = "bool", shape = (4, 8, 14))#candidate|1217|(4, 8, 14)|var|bool
bop_1218 = relay.logical_or(var_1216.astype('bool'), relay.reshape(var_1217.astype('bool'), relay.shape_of(var_1216))) # shape=(4, 8, 14)
output = bop_1218
output2 = bop_1218
func_1229 = relay.Function([var_1216,var_1217,], output)
mod['func_1229'] = func_1229
mod = relay.transform.InferType()(mod)
var_1230 = relay.var("var_1230", dtype = "bool", shape = (4, 8, 14))#candidate|1230|(4, 8, 14)|var|bool
var_1231 = relay.var("var_1231", dtype = "bool", shape = (4, 8, 14))#candidate|1231|(4, 8, 14)|var|bool
output = func_1229(var_1230,var_1231,)
func_1232 = relay.Function([var_1230,var_1231,], output)
mutated_mod['func_1232'] = func_1232
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1389 = relay.const([[[3.029052,-2.846199,4.408754,-1.578563],[7.777149,-5.741461,8.155286,-3.537471]],[[-4.171629,-4.437221,6.850652,0.610398],[7.117590,7.893643,-6.700468,-8.505426]],[[9.233318,-4.276620,7.800275,-9.141844],[7.231933,5.311622,-5.907279,4.557543]],[[1.578563,-0.476279,-6.260021,3.301356],[9.565129,-7.871553,1.687598,-6.286700]]], dtype = "float64")#candidate|1389|(4, 2, 4)|const|float64
uop_1390 = relay.sinh(const_1389.astype('float64')) # shape=(4, 2, 4)
output = relay.Tuple([uop_1390,])
output2 = relay.Tuple([uop_1390,])
func_1396 = relay.Function([], output)
mod['func_1396'] = func_1396
mod = relay.transform.InferType()(mod)
output = func_1396()
func_1397 = relay.Function([], output)
mutated_mod['func_1397'] = func_1397
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1398 = relay.var("var_1398", dtype = "int64", shape = (3, 13, 4))#candidate|1398|(3, 13, 4)|var|int64
var_1399 = relay.var("var_1399", dtype = "int64", shape = (3, 13, 4))#candidate|1399|(3, 13, 4)|var|int64
bop_1400 = relay.not_equal(var_1398.astype('bool'), relay.reshape(var_1399.astype('bool'), relay.shape_of(var_1398))) # shape=(3, 13, 4)
output = relay.Tuple([bop_1400,])
output2 = relay.Tuple([bop_1400,])
func_1411 = relay.Function([var_1398,var_1399,], output)
mod['func_1411'] = func_1411
mod = relay.transform.InferType()(mod)
mutated_mod['func_1411'] = func_1411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1411_call = mutated_mod.get_global_var('func_1411')
var_1413 = relay.var("var_1413", dtype = "int64", shape = (3, 13, 4))#candidate|1413|(3, 13, 4)|var|int64
var_1414 = relay.var("var_1414", dtype = "int64", shape = (3, 13, 4))#candidate|1414|(3, 13, 4)|var|int64
call_1412 = func_1411_call(var_1413,var_1414,)
output = call_1412
func_1415 = relay.Function([var_1413,var_1414,], output)
mutated_mod['func_1415'] = func_1415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_1471 = relay.TupleGetItem(func_1396_call(), 0)
call_1472 = relay.TupleGetItem(func_1397_call(), 0)
output = call_1471
output2 = call_1472
func_1487 = relay.Function([], output)
mod['func_1487'] = func_1487
mod = relay.transform.InferType()(mod)
mutated_mod['func_1487'] = func_1487
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mutated_mod.get_global_var('func_1487')
call_1488 = func_1487_call()
output = call_1488
func_1489 = relay.Function([], output)
mutated_mod['func_1489'] = func_1489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1589 = func_1487_call()
call_1590 = func_1487_call()
func_1229_call = mod.get_global_var('func_1229')
func_1232_call = mutated_mod.get_global_var('func_1232')
const_1597 = relay.const([True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,True], dtype = "bool")#candidate|1597|(448,)|const|bool
call_1596 = func_1229_call(relay.reshape(const_1597.astype('bool'), [4, 8, 14]), relay.reshape(const_1597.astype('bool'), [4, 8, 14]), )
call_1598 = func_1229_call(relay.reshape(const_1597.astype('bool'), [4, 8, 14]), relay.reshape(const_1597.astype('bool'), [4, 8, 14]), )
output = relay.Tuple([call_1589,call_1596,const_1597,])
output2 = relay.Tuple([call_1590,call_1598,const_1597,])
func_1608 = relay.Function([], output)
mod['func_1608'] = func_1608
mod = relay.transform.InferType()(mod)
mutated_mod['func_1608'] = func_1608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mutated_mod.get_global_var('func_1608')
call_1609 = func_1608_call()
output = call_1609
func_1610 = relay.Function([], output)
mutated_mod['func_1610'] = func_1610
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1631 = relay.var("var_1631", dtype = "uint16", shape = (7, 10, 14))#candidate|1631|(7, 10, 14)|var|uint16
const_1632 = relay.const([[[-3,10,4,8,-4,9,4,10,6,8,-10,3,-5,-1],[9,-2,7,-6,10,8,9,-7,9,2,9,-9,4,-10],[-3,2,7,6,-6,8,-6,-9,-4,-7,-4,-8,10,2],[1,3,-5,8,8,7,-6,-9,-1,-7,-5,-8,7,1],[-3,-1,7,10,10,-5,2,4,8,10,2,-4,6,-5],[6,-8,3,5,3,1,3,-2,9,-5,-9,-4,-4,9],[10,3,-2,-9,8,4,-9,-5,-2,-9,2,5,1,-4],[10,7,7,-8,-10,-3,-10,2,-1,-4,-3,-1,-9,10],[-6,8,-8,-7,-4,-6,-1,3,-4,-1,-1,8,-1,2],[-5,-1,9,-8,4,-1,-10,3,4,5,2,-2,2,-10]],[[9,3,6,-5,-3,9,-8,-6,-9,-10,-6,2,-2,2],[6,-6,-3,9,3,2,6,-3,-6,-3,-7,-8,9,-10],[8,-4,1,-9,9,4,1,7,-9,-2,-9,-10,9,1],[9,6,1,-2,-9,9,-9,9,-10,7,-7,6,1,6],[5,-7,-9,2,4,4,-6,-9,-9,5,5,1,-9,1],[5,2,-5,4,2,3,1,7,-2,2,-7,3,7,5],[2,-7,-3,7,-6,1,-7,3,-2,7,9,7,6,-7],[3,10,7,-2,-6,8,8,-1,-2,4,5,9,-1,-9],[4,2,7,3,-1,4,-2,9,-2,8,5,9,5,5],[4,-5,-9,6,-2,1,3,-1,6,8,2,-1,8,-6]],[[-7,9,6,-2,2,2,8,-7,7,-6,10,2,-10,9],[-2,-10,-8,4,4,9,-3,-10,-4,-2,5,-7,-3,-6],[-1,-10,-10,6,9,1,6,-9,-1,-10,6,-10,-9,7],[-6,-5,-6,2,3,-3,7,-6,-4,-10,6,1,-3,4],[-8,5,3,-10,5,4,-9,-2,1,-9,-5,-9,10,-4],[1,-4,8,-2,7,10,6,-10,1,1,-2,-4,-9,9],[-2,-2,-10,3,-6,-10,9,-7,-6,-1,-10,8,5,10],[-6,5,3,-1,6,2,-9,4,-4,2,-9,6,7,3],[7,-6,-4,9,8,10,-5,5,7,-1,-2,3,-8,-9],[5,5,-5,3,1,7,-3,5,-1,2,-2,1,8,3]],[[4,-10,-6,-9,7,-2,-5,10,-8,-7,-7,-7,2,3],[1,-7,-10,4,-2,-8,-6,-9,-1,-10,-8,-6,-6,4],[-10,-9,2,7,-2,7,5,-5,8,-1,-7,-8,8,9],[-6,3,7,8,-9,-1,-6,-7,4,2,-7,10,4,8],[1,-7,10,4,3,9,7,-2,-8,5,-2,3,2,5],[1,-9,3,-9,7,2,-5,3,-3,-8,6,3,4,7],[-9,-3,8,-3,9,5,7,-7,10,-6,-7,-4,-10,10],[4,10,-2,4,-7,4,-10,4,-6,-10,5,9,-2,4],[1,6,3,-9,-10,-6,1,-5,-9,-8,3,1,-6,7],[-5,-2,5,2,-3,-3,-7,2,-1,8,-5,4,8,6]],[[-10,-2,6,-3,-1,8,-9,8,4,-3,6,-6,2,1],[-9,-2,1,-6,-9,7,8,-5,-8,3,5,-6,7,-6],[-4,-7,-5,10,6,-1,6,6,-3,9,5,3,7,-5],[-3,-3,7,8,10,5,5,-2,4,-3,8,6,5,5],[1,6,10,-9,-9,6,4,-7,7,-7,9,8,3,3],[5,10,8,8,-5,-5,-3,-6,-4,5,6,4,4,-3],[8,-7,-3,-9,-2,1,5,2,8,-4,-4,-4,2,6],[-2,5,2,-2,-8,8,-9,7,-6,3,-10,-4,7,7],[-10,9,1,-1,-7,-9,-8,-5,5,-3,3,-5,-3,9],[1,-3,-8,-2,-6,3,-7,-8,-9,-4,-7,7,2,-4]],[[1,9,1,2,4,-10,8,-4,4,-2,7,9,-2,5],[-8,-3,6,2,3,9,-9,-8,10,2,7,7,1,-9],[10,-8,-7,-7,2,10,-3,-5,-6,9,-6,-10,-6,-9],[2,-9,4,-3,10,-1,1,-2,-2,9,9,-4,1,-9],[2,4,-6,8,-4,-8,-3,9,-4,-10,-7,2,7,4],[-1,-4,1,-7,-3,-6,8,-1,6,-4,-2,-5,-3,6],[5,7,5,9,1,4,2,1,3,-10,-6,9,9,7],[-1,4,-5,3,4,5,-9,9,8,-1,4,1,-6,-7],[2,-10,1,2,7,-7,9,-8,10,2,-7,-10,-4,2],[1,8,-3,10,-10,-9,8,-10,7,-7,-5,-8,2,5]],[[9,10,5,5,4,-4,-8,3,-9,4,1,7,-8,8],[3,10,1,5,-5,5,-8,6,-4,-3,-4,-2,-6,-10],[-4,-6,2,-2,-5,-2,-7,-2,8,10,-6,4,10,4],[-5,-2,-3,-7,-4,1,-5,-2,9,-7,1,-8,2,9],[-8,-8,9,5,8,-10,-2,-4,1,-9,-1,7,6,10],[-7,-8,6,-1,3,7,-7,-6,6,-6,-5,1,-3,-7],[-4,-7,-10,8,-10,-8,-5,6,2,1,-1,8,3,-1],[8,5,9,-4,6,2,3,1,-7,-9,1,10,6,6],[-7,-8,-7,6,-5,-4,4,-9,7,4,8,-6,3,9],[-4,-1,-5,8,1,9,-6,-5,8,7,3,-1,3,10]]], dtype = "uint16")#candidate|1632|(7, 10, 14)|const|uint16
bop_1633 = relay.right_shift(var_1631.astype('uint16'), relay.reshape(const_1632.astype('uint16'), relay.shape_of(var_1631))) # shape=(7, 10, 14)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
var_1639 = relay.var("var_1639", dtype = "float64", shape = (1638,))#candidate|1639|(1638,)|var|float64
call_1638 = relay.TupleGetItem(func_1070_call(relay.reshape(var_1639.astype('float64'), [14, 13, 9])), 0)
call_1640 = relay.TupleGetItem(func_1073_call(relay.reshape(var_1639.astype('float64'), [14, 13, 9])), 0)
uop_1647 = relay.log2(const_1632.astype('float64')) # shape=(7, 10, 14)
uop_1659 = relay.erf(uop_1647.astype('float64')) # shape=(7, 10, 14)
bop_1663 = relay.logical_or(uop_1647.astype('bool'), relay.reshape(uop_1659.astype('bool'), relay.shape_of(uop_1647))) # shape=(7, 10, 14)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1666 = func_1487_call()
call_1667 = func_1487_call()
var_1670 = relay.var("var_1670", dtype = "float64", shape = (7, 10, 14))#candidate|1670|(7, 10, 14)|var|float64
bop_1671 = relay.left_shift(uop_1659.astype('int16'), relay.reshape(var_1670.astype('int16'), relay.shape_of(uop_1659))) # shape=(7, 10, 14)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
const_1677 = relay.const([-5,4,5,-7,6,3,-2,-1,3,2,-8,8,-6,-4,3,2,2,-5,8,6,-7,-9,9,-6,9,4,2,1,3,8,7,-2,-10,7,-1,3,-4,-5,-10,7,10,9,7,9,-5,4,8,4,6,-5,-6,3,1,-7,10,2,-9,-3,1,6,8,8,9,4,-3,10,-7,1,4,1,-4,-5,4,-9,7,-8,5,-1,-10,-8,3,-4,5,-8,-5,-3,2,10,-4,-10,4,8,-6,4,3,6,-1,6,-6,-5,3,-10,3,-8,10,-2,6,4,10,-7,-9,8,-5,-8,-9,2,8,-5,-3,-2,3,-7,-5,-2,-8,-7,-3,-7,-1,7,-5,-2,-4,-5,-3,10,-10,-8,8,9,8,3,3,8,-4,-4,8,3,6,-9,-7,-7,-7,-4,-5,-3,9,6,7,-7,-3,-1,8,2,-3,3,1,-1,-2,-5,9,10,3,1,-2,-10,-9,5,-4,1,8,-1,1,9,-6,10,10,3,-8,3,1,2,-4,-7,-3,-10,-10,4,-3,-7,-5,4,9,-1,4,-6,1,4,6,-6,10,2,6,-3,8,8,7,1,1,-2,7,-1,7,-4,9,-1,-7,-10,10,-10,3,2,-1,-7,-4,-9,-6,-1,-6,-5,-8,-5,-1,6,8,2,7,5,-6,2,9,4,2,10,2,-4,-2,-5,-3,8,8,-7,1,-3,-4,8,-8,1,-8,9,-6,10,3,-5,-8,-2,-1,3,2,-1,-3,-10,-3,-1,3,1,-3,9,8,-4,7,3,4,-9,4,-3,-1,5,5,5,6,-9,-8,-6,-4,-5,6,-8,3,-9,9,3,-6,-4,-6,10,4,2,-8,2,-9,-1,-4,7,6,6,7,-7,-10,3,9,-8,3,-7,-8,-10,-6,4,-2,1,9,5,-7,-1,3,-2,9,5,10,10,-3,-7,-5,-2,3,7,1,10,-6,6,4,2,-6,5,3,5,8,-6,10,2,-1,5,-2,-1,-3,10,3,-3,10,-8,-3,-8,3,-8,4,-6,10,7,6,2,5,9,5,10,9,-8,-8,-7,-10,4,4,9,1,8,5,7,2,-1,-9,2,-6,-4,7,-5,-8,-3,1,8,1,1,6,8,-5,4,-10,4,7,2,1,2,-8,-2,10,-3,4,7,-2,-7,-5,-3,-7,3,-6,9,2,-5,-10,-9,4,1,6,7,6,6,-3,6,-5,6,-4,7,10,-6,8,1,9,-10,-2,2,-9,9,5,-5,-6,2,-8,4,2,10,-7,-9,-5,-1,6,-2,2,-8,-9,-9,-4,3,-1,-3,8,10,4,-10,-10,5,4,10,1,5,1,-4,-7,10,-3,9,-6,-7,-10,-1,-9,6,-4,-9,6,-4,8,-5,-3,2,-10,9,2,8,4,6,-4,7,9,-2,2,4,-1,4,4,4,-9,-9,9,-6,-7,-6,-5,10,9,-10,9,10,3,-6,1,2,-2,-2,-10,-6,3,1,-3,1,-4,-2,7,3,-9,8,10,2,10,-5,-4,-7,-10,-4,-1,6,6,-8,-1,4,1,-10,9,-3,5,9,-8,8,-9,3,-7,-3,7,7,-2,8,10,-4,-9,10,-6,5,9,2,-6,-6,-3,8,-2,-8,4,10,3,5,-3,-5,-5,-1,-4,2,9,4,9,-2,5,-5,-5,4,-9,9,5,-8,-4,7,-5,1,9,6,7,8,7,2,-8,-3,9,-10,-5,7,1,-1,-2,-8,8,-8,-3,9,-2,3,1,-9,-7,-5,9,-6,-3,-5,-1,-6,9,6,-2,2,-7,-4,-3,9,3,-6,3,1,1,10,10,-1,-4,3,-3,10,1,10,-8,-6,10,-1,4,-8,-9,6,-6,2,-5,6,1,-10,7,-8,7,-5,-8,10,10,6,6,-1,-9,4,8,-4,3,3,5,6,7,-1,-10,6,8,-9,4,-9,-3,-8,3,1,-7,-10,6,-6,-9,-8,7,9,4,2,-8,-2,3,3,2,-6,8,3,3,-9,-6,1,8,9,-8,1,-9,6,-3,-2,2,-5,-3,6,-6,8,1,5,1,-3,-2,-2,9,7,-4,-8,6,-9,-2,4,-10,-1,-4,-10,8,-2,2,-5,2,7,-10,4,-8,4,-6,7,-3,-6,-3,-9,-4,5,-7,-8,-2,-6,-10,10,-3,-6,-5,6,-1,2,-3,-9,6,-2,4,-3,-5,-3,-9,-10,9,3,3,1,-4,-10,-6,1,-4,-6,-4,-9,7,-3,4,1,3,7,-5,-10,1,-5,10,10,10,-6,-4,5,-6,-2,-2,-4,-8,1,-7,-2,10,7,5,5,3,4,-6,-3,-5,-3,-7,-4,-7,-8,-5,-5,10,-4,-7,-4,2,-10,-5,3,7,9,-4,-8,-9,7,7,-8,2,-3,2,-1,-5,5,3,2,-5,-3,5,9,-6,-7,-6,1,6,7,1,-6,-1,6,10,-6,-8,-3,-10,8,-7,-10,-9,-1,5,5,-9,10,-4,4,2,-9,8,-5,4,-4,-6,6,-5,2,-8,-4,8,5,-10,-5,10,5,6,4,-3,1,-3,7,-5,-8,6,7,5,5,2,2,-2,10,6,7,4,-1,6,-7,-8,1,-6,-7,2,-8,2,8,6,-3,2,6,-10,3,6,7,4,8,-8,-2,-7,-9,-2,-4,-5,-3,-6,2,-5,-2,-6,4,6,-1,7,7,6,2,2,-4,-10,3,7,4,2,-2,-6,2,6,-8,-7,-6,10,-8,-3,-9,-3,-1,-8,10,-2,10,-9,-9,6,-10,2,-5,-4,-5,7,-2,-6,1,-9,-4,3,6,-8,9,-2,-6,-4,7,6,-7,-7,5,1,7,-7,10,7,-4,-10,-9,-1,-9,8,7,7,8,2,-7,-9,2,7,8,9,-1,4,-3,6,3,7,7,3,-10,-1,9,-1,-6,4,-2,-5,-2,-2,-3,7,2,6,-8,7,4,-4,7,-4,6,8,-1,-3,-1,7,3,2,8,5,6,5,-9,3,-6,1,-6,-2,-2,-9,-7,-7,-10,8,-6,5,6,-2,-1,-2,-3,-1,-10,4,-5,4,-7,6,1,-7,-8,1,-4,-8,-9,6,-3,-8,9,4,-5,9,9,-1,-9,7,3,-1,2,-4,2,-10,-6,-8,10,-2,-10,9,6,10,-8,-5,7,-10,7,-10,5,-4,10,-7,-3,7,9,3,-6,3,9,7,-3,-5,-2,-1,-4,-7,10,7,2,-7,10,6,-2,-9,6,9,4,2,-10,2,-2,10,-2,5,1,-7,-3,-6,-2,10,-3,-7,-4,5,-4,7,8,5,-6,-6,-4,7,-3,-2,8,-3,10,1,1,-7,-5,-8,-4,2,5,5,10,7,-5,-10,-3,-7,5,7,4,-8,10,3,-2,2,-5,-7,10,-8,-4,-1,1,10,-6,1,-2,-10,-6,-4,9,8,-6,-9,-10,3,-7,-1,-10,4,7,-7,-6,-1,9,-3,-3,4,-5,-6,-10,-8,-3,5,9,1,-9,-5,3,-9,3,-5,-4,-4,2,5,8,8,10,5,7,5,2,10,8,-2,-1,7,-3,-6,10,-8,-3,-10,-2,-4,2,-6,3,-2,5,-4,-10,-4,2,2,1,10,6,9,-6,-8,2,5,-10,-6,2,1,-1,-8,7,4,-8,10,-8,-4,1,5,6,1,-6,8,9,3,-8,-2,1,-1,-2,-4,1,7,10,7,1,-9,-7,8,-10,-5,-9,3,4,-10,-4,-9,10,7,7,5,4,-8,5,-6,-4,-3,-9,-5,-8,-1,7,9,5,9,-2,3,-10,-8,4,8,-6,-3,7,9,-2,2,-10,1,7,-9,-4,-6,3,9,-9,-7,10,-3,9,4,4,-5,7,2,-5,4,5,-6,-5,6,-2,10,-5,8,-4,-5,10,-5,-5,-10,9,-4,5,3,-4,3,-3,7,5,10,-10,10,-7,7,-1,6,3,4,-7,6,-7,-7,-2,-8,2,8,7,3,2,-7,9,1,-1,-7,-4,-2,-4,3,5,-6,-1,10,2,-1,-3,5,4,-3,-5,-5,-5,-1,-8,-8,-6,-2,9,-5,5,-5,-6,10,10,-7,4,-3,-1,-2,9,-3,-4,-3,7,6,-6,8,-3,4,-2,10,2,-6,8,-9,-8,5,7,7,-6,4,3,-5,-2,2,7,9,5,-2,3,-3,4,-3,6,7,-10,-5,2,-3,-7,8,9,5,3,9,9,-5,2,7,7,-9,2,-1,-1,1,-1,6,-8,-4,-8,-7,6,1,-1,5,2,-4,-5,-1,9,-8,2,-8,5,-1,6,-4,-1,10,5,7,-9,-2,-6,-3,-6,5,5,8,7,6,9,-6,7,10,1,-7,-8,5,3,-9,10,-7,-9,-8,-6,10,6,-6,3,-3,5,7,1,9,1,-3,6,-8,8,-1,-2,-10,10,9,3,-10,-6,-4,-8,-2,-5,-9,-6,-5,-5,-9,-1,5,-6,-5,-8,9,-1,-10,-10,-9,9,5,7,2,-10,10,1,-3,2,7,-4,-6,3,-7,10,7,5,5,-6,5,7,7,3,-6,-9,-4,1,-1,8,7,-3,-7,10,10,8,-2,-3,4,1,8,3,7,4,10,6,-1,-4,7,10,-10,5,5,10,-1,-9,3,2,8,7,-9,-5,-2,-7,-1,-8,-9,-2,8,-4,-5,7,7,-9,7,-2,9,-5,6,-1,10,9,-10,-6,5,7,-4,-9,6,-5,3,7,3,-4,5,8,-3,-5,-8,-1,-10,2,-5,-5,10,-3,-7,5,-2,1,-4,-3,3,-2,-10,1,-3,5,5,-10,10,-10,-4,9,3,5,6,-6,7,-10,-1,8,6,-2,3,-8,5,-2,-4,-7,8,6,-10,-2,8,-4,5,-3,-5,-3,-8,1,-10,2,-3,-1,-9,-6,-7,5,-2,-6,-1,5,-5,4,1,7,-10,3,8,-4,-9,5,1,-5,9,8,-4,5,1,-5,7,-4,-10,10,-9,4,-7,7,-9,8,6,9,9,9,5,4,5,9,-5,3,5,3,8,-9,2,6,-3,8,-1,4,3,8,-8,-5,-5,-6,-8,2,8,-3,-9,10,4,-6,9,2,9,-1,-6,9,-7,-6,3,10,-9,6,4,2,6,-4,7,6,-6,3,3,7,-7,4,-9,3,-1,-8,5,-4,7,5,-4,9,7,-1,-6,-10,-9,4,3,10,8,-9,-7,5,9,-7,2,2,-8,8,1,-8,4,-10,1,9,9,4,8,-9,9,1,-2,1,-6,-5,-8,-7,4,7,9,-5,-5,4,6,2,1,-9,6,2,-8,9,9,8,5,-9,5,-3,-2,-4,4,6,-1,6,-6,1,7,-1,6,-2,-7,5,4,2,9,-6,4,-6,-8,6,1,9,-7,-6,10,-4,-8,10,-9,10,8,8,-8,9,-7,2,-2,7,1,-2,1,1,5,1,-4,9,-7,-4,-1,4,9,5,-7,1,-6,-1,9,6,3,-7,10,-9,-4,5,7,3,-5,7,3,-2,-3,7,4,7,1,-4,-1,-10,-7,10,4,10,-2,-3,-7,3,7,3,3,1,-5,7,-10,-10,-3,1,-2,9,9,8,-5,7,2,5,1,1,1,-1,6,7,2,7,10,9,-7,7,-1,-4,-6,8,5,3,-9,8,-8,5,5,-5,9,4,4,-6,4,5,10,-9,-5,10,9,-9,5,10,-7,2,-10,2,6], dtype = "int16")#candidate|1677|(2145,)|const|int16
const_1678 = relay.const([2,-8,-2,4,5,-3,-9,-8,-1,-2,9,-7,10,-1,6,8,6,9,-10,1,10,10,6,-6,4,-3,7,-8,-9,-5,-3,-4,-9,-4,-6,4,10,7,-1,-2,-1,8,6,-7,4,-1,-7,3,-8,4,-3,-1,-4,8,1,10,6,2,-1,8,-10,-2,2,2,-4,5,7,-2,-4,4,-2,-7,-2,2,-7,9,-7,-4,-6,-2,-3,10,3,-10,-2,-2,1,-3,-8,4,-5,-3,-4,5,1,2,4,-5,2,2,2,-8,-5,3,8,-9,2,7,-8,8,10,5,-2,9,-8,7,8,2,-6,7,4,-9,7,-4,10,6,4,4,-4,1,5,-1,-5,6,-7,7,6,-8,4,10,8,4,7,-1,10,-2,-9,-9,3,-8,-6,-2,3,-7,-5,-10,3,6,-1,-1,-8,7,-6,-4,10,9,-8,-8,4,9,2,-2,-3,-5,7,7,-8,7,-3,-3,4,8,-7,-5,4,8,-3,-1,3,5,3,-9,8,-7,6,3,3,4,-10,1,-4,9,3,6,-7,8,-4,-3,3,-3,-9,9,-10,4,-5,-3,3,-8,2,-2,4,-1,9,1,1,10,-2,3,-5,1,1,-9,-6,1,-1,-8,-7,5,2,-7,-4,4,10,-10,-6,5,7,-4,-2,-2,1,10,-9,-3,5,-4,1,-4,9,5,5,5,-5,4,5,10,5,2,-7,7,-7,10,10,8,-8,-5,3,4,8,-5,5,8,5,6,-7,5,-5,-3,-9,-4,-3,9,-8,4,-2,-10,-2,8,10,-3,-8,-2,-3,6,5,-8,-1,-4,9,-7,-7,-9,7,8,3,6,-10,-2,3,-5,-10,-9,-10,-9,1,4,-7,8,-10,1,8,3,-6,-2,-5,-9,10,7,3,2,4,-1,-9,-4,5,-2,-1,-2,-4,-5,-3,-5,4,-4,-7,-10,-2,-3,10,-10,3,10,7,-10,-8,9,3,4,-7,4,-5,-7,5,-8,7,2,7,3,-3,6,-10,-5,-2,-10,-9,3,1,3,-9,-1,-8,-6,4,-1,-4,2,-6,9,-6,-7,5,1,9,10,-4,6,-5,-6,-6,7,8,4,-6,1,1,-9,5,2,3,-4,4,-8,4,1,-3,-10,8,4,-8,-6,-3,7,4,-2,1,5,-7,6,8,-3,-6,3,-8,7,-2,-5,7,-2,1,-9,1,-8,6,-4,-3,-7,-2,4,7,-8,-4,3,4,6,1,-8,9,5,-1,-2,-7,-5,9,-1,-1,-5,-1,-10,-4,-2,10,-9,5,-6,2,3,9,8,-5,4,5,3,-8,3,-7,-8,5,8,9,6,-4,-9,-7,10,-6,-8,-4,9,3,-5,-6,-9,-8,1,-3,-1,8,-9,-6,6,3,-5,6,10,-5,-2,-6,2,-8,-3,1,-5,3,3,2,3,3,4,-9,1,-7,-5,-1,-9,9,9,8,-1,9,2,3,-9,-3,-8,-7,-6,-9,9,9,9], dtype = "int32")#candidate|1678|(560,)|const|int32
call_1676 = relay.TupleGetItem(func_533_call(relay.reshape(const_1677.astype('int16'), [13, 15, 11]), relay.reshape(const_1677.astype('int16'), [13, 15, 11]), relay.reshape(const_1678.astype('int32'), [560,]), ), 1)
call_1679 = relay.TupleGetItem(func_537_call(relay.reshape(const_1677.astype('int16'), [13, 15, 11]), relay.reshape(const_1677.astype('int16'), [13, 15, 11]), relay.reshape(const_1678.astype('int32'), [560,]), ), 1)
uop_1686 = relay.asin(bop_1663.astype('float32')) # shape=(7, 10, 14)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_1697 = relay.TupleGetItem(func_1608_call(), 2)
call_1698 = relay.TupleGetItem(func_1610_call(), 2)
uop_1714 = relay.tan(bop_1671.astype('float32')) # shape=(7, 10, 14)
output = relay.Tuple([bop_1633,call_1638,var_1639,call_1666,call_1676,const_1677,const_1678,uop_1686,call_1697,uop_1714,])
output2 = relay.Tuple([bop_1633,call_1640,var_1639,call_1667,call_1679,const_1677,const_1678,uop_1686,call_1698,uop_1714,])
func_1717 = relay.Function([var_1631,var_1639,var_1670,], output)
mod['func_1717'] = func_1717
mod = relay.transform.InferType()(mod)
var_1718 = relay.var("var_1718", dtype = "uint16", shape = (7, 10, 14))#candidate|1718|(7, 10, 14)|var|uint16
var_1719 = relay.var("var_1719", dtype = "float64", shape = (1638,))#candidate|1719|(1638,)|var|float64
var_1720 = relay.var("var_1720", dtype = "float64", shape = (7, 10, 14))#candidate|1720|(7, 10, 14)|var|float64
output = func_1717(var_1718,var_1719,var_1720,)
func_1721 = relay.Function([var_1718,var_1719,var_1720,], output)
mutated_mod['func_1721'] = func_1721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_1747 = relay.TupleGetItem(func_1396_call(), 0)
call_1748 = relay.TupleGetItem(func_1397_call(), 0)
output = relay.Tuple([call_1747,])
output2 = relay.Tuple([call_1748,])
func_1788 = relay.Function([], output)
mod['func_1788'] = func_1788
mod = relay.transform.InferType()(mod)
mutated_mod['func_1788'] = func_1788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1788_call = mutated_mod.get_global_var('func_1788')
call_1789 = func_1788_call()
output = call_1789
func_1790 = relay.Function([], output)
mutated_mod['func_1790'] = func_1790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1864 = func_1487_call()
call_1865 = func_1487_call()
output = call_1864
output2 = call_1865
func_1870 = relay.Function([], output)
mod['func_1870'] = func_1870
mod = relay.transform.InferType()(mod)
mutated_mod['func_1870'] = func_1870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1870_call = mutated_mod.get_global_var('func_1870')
call_1871 = func_1870_call()
output = call_1871
func_1872 = relay.Function([], output)
mutated_mod['func_1872'] = func_1872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1882 = func_1487_call()
call_1883 = func_1487_call()
output = call_1882
output2 = call_1883
func_1884 = relay.Function([], output)
mod['func_1884'] = func_1884
mod = relay.transform.InferType()(mod)
output = func_1884()
func_1885 = relay.Function([], output)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1884_call = mod.get_global_var('func_1884')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_1936 = func_1884_call()
call_1937 = func_1884_call()
const_1950 = relay.const([[[-4.605742,-8.042355,9.839536,4.427190],[-5.689566,-3.773366,2.521636,9.164722]],[[5.322402,-9.701377,5.600141,-4.599910],[-5.969772,-8.021650,1.613668,7.437178]],[[-7.492235,6.124034,-7.862530,-9.549185],[1.427635,8.505729,6.226024,-5.611734]],[[-1.829247,-2.185545,9.043500,-7.013093],[1.256228,8.939100,4.723070,9.480729]]], dtype = "float64")#candidate|1950|(4, 2, 4)|const|float64
bop_1951 = relay.equal(call_1936.astype('bool'), relay.reshape(const_1950.astype('bool'), relay.shape_of(call_1936))) # shape=(4, 2, 4)
bop_1954 = relay.equal(call_1937.astype('bool'), relay.reshape(const_1950.astype('bool'), relay.shape_of(call_1937))) # shape=(4, 2, 4)
const_1960 = relay.const([[[-0.249966,6.446147,-9.532289,-1.888238],[-8.207380,-4.781513,-6.890549,-2.348507]],[[-9.195565,-3.554332,-1.415811,-1.487337],[-8.025416,-9.080563,0.974644,-5.097185]],[[8.880992,3.434178,0.756913,6.336154],[-9.960877,-1.729284,-1.374564,-0.167206]],[[4.437549,-3.371535,3.308293,9.736260],[-2.517348,-8.983820,4.492775,-2.481387]]], dtype = "float64")#candidate|1960|(4, 2, 4)|const|float64
bop_1961 = relay.less_equal(call_1936.astype('bool'), relay.reshape(const_1960.astype('bool'), relay.shape_of(call_1936))) # shape=(4, 2, 4)
bop_1964 = relay.less_equal(call_1937.astype('bool'), relay.reshape(const_1960.astype('bool'), relay.shape_of(call_1937))) # shape=(4, 2, 4)
uop_1978 = relay.cosh(call_1936.astype('float32')) # shape=(4, 2, 4)
uop_1980 = relay.cosh(call_1937.astype('float32')) # shape=(4, 2, 4)
uop_2004 = relay.erf(uop_1978.astype('float32')) # shape=(4, 2, 4)
uop_2006 = relay.erf(uop_1980.astype('float32')) # shape=(4, 2, 4)
output = relay.Tuple([bop_1951,bop_1961,uop_2004,])
output2 = relay.Tuple([bop_1954,bop_1964,uop_2006,])
func_2030 = relay.Function([], output)
mod['func_2030'] = func_2030
mod = relay.transform.InferType()(mod)
mutated_mod['func_2030'] = func_2030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mutated_mod.get_global_var('func_2030')
call_2031 = func_2030_call()
output = call_2031
func_2032 = relay.Function([], output)
mutated_mod['func_2032'] = func_2032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1884_call = mod.get_global_var('func_1884')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_2035 = func_1884_call()
call_2036 = func_1884_call()
func_483_call = mod.get_global_var('func_483')
func_486_call = mutated_mod.get_global_var('func_486')
var_2045 = relay.var("var_2045", dtype = "int32", shape = (1, 14))#candidate|2045|(1, 14)|var|int32
const_2046 = relay.const([-10,-5,2,6,-7,3,-4,-4,-5,2,-2,-1,-1,3,8,3,2,-5,-8,-6,-7,-3,-6,-7,-7,-8,2,-7,-8,2,8,-6,-5,-7,-1,8,-2,8,9,-2,-4,5,-8,9,-5,-4,8,3,10,-6,5,-8,4,8,9,10,-8,7,9,4,9,-7,7,-8,-4,-9,-8,-7,-2,8,4,-5,2,10,10,-5,1,5,4,8,-10,6,-7,4,7,-1,9,3,9,-5,9,-1,-6,10,-4,9,-9,-3,9,6,-9,-6,4,-4,-5,6,-2,4,-3,-7,7,10,2,-2,3,6,-6,4,4,-5,-8,-2,-7,-6,3,7,1,7,5,2,-1,1,1,-7,3,3,-10,10,1,8,-3,-7,-4,-8,8,-8,8,-4,3,5,1,7,-3,9,-7,10,-3,4,3,-8,-2,8,4,-3,3,-4,4,-8,-8,-10,3,5,-9,5,1,-3,-10,4,-2,2,3,-2,7,5,-6,-2,-5,6,6,-5,5,-1,-8,-6,2,-8,3,-3,9,-6,2,-5,-5,-10,2,-7,5,9,-2,6,4,10,-3,8,10,-8,-1,9,5,6,-9,4,10,-7,-2,-6,-6,-4,9,2,7,4,-4,2,6,-7,-1,-9,6,-5,7,-3,-8,-2,2,-10,4,4,9,-7,6,-8,-7,-9,-2,-9,8,2,2,4,-9,-10,-8,-3,4,10,6,-10,6,3,-6,7,-6,-9,-6,-2,-7,8,-9,-10,10,5,-9,-8,6,3,4,3,10,8,-5,10,3,7,8,-8,-7,-4,-8,3,2,6,-5,-7,3,10,-6,-9,-8,-4,4,-5,-5,-9,-9,-8,8,10,5,8,-3,-3,1,-1,-8,5,6,-5,9,5,8,-1,-9,10,8,-9,6,-3,6,6,-8,-8,-1,9,-10,-7,10,-5,-1,-1,2,-2,-2,7,-9,-3,-6,-3,-5,6,-7,-4,-5,5,3,-4,6,3,-1,7,5,-6,1,7,-4,-3,-10,-9,7,10,10,5,10,-7,10,10,3,6,7,-4,-8,3,4,-4,6,1,8,3,5,10,5,1,-7,-6,2,-7,-6,10,-2,3,6,3,1,3,-9,3,2,2,3,-8,-7,-5,5,5,8,5,-3,10,-8,9,-6,9,-6,-9,-10,-4,-2,-2,-4,6,6,-8,2,2,-10,7,-3,6,-9,10,4,6,3,-4,-4,1,-4,6,8,7,-9,6,3,5,6,1,1,5,5,5,4,9,6,5,5,3,-8,-8,-2,-5,2,10,5,-9,7,-2,-9,-8,-8,8,8,-7,-2,-9,10,3,-2,-5,-8,-1,-8,7,-6,2,-9,5,-2,6,-9,-6,-1,-1,2,1,-4,-7,7,-2,9,5,4,7,-2,8,8,-10,-7,-3,9,-10,-8,5,-3,8,-1,-1,-3,-1,-1,-6,-4,-9,9,9,8,3,8,-1,7,2,2,-2,-4,-2,1,8,-6,8,9,-5], dtype = "int32")#candidate|2046|(560,)|const|int32
call_2044 = relay.TupleGetItem(func_483_call(relay.reshape(var_2045.astype('int32'), [14, 1, 1]), relay.reshape(const_2046.astype('int32'), [14, 8, 5]), ), 1)
call_2047 = relay.TupleGetItem(func_486_call(relay.reshape(var_2045.astype('int32'), [14, 1, 1]), relay.reshape(const_2046.astype('int32'), [14, 8, 5]), ), 1)
output = relay.Tuple([call_2035,call_2044,var_2045,const_2046,])
output2 = relay.Tuple([call_2036,call_2047,var_2045,const_2046,])
func_2061 = relay.Function([var_2045,], output)
mod['func_2061'] = func_2061
mod = relay.transform.InferType()(mod)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2062 = relay.var("var_2062", dtype = "int32", shape = (1, 14))#candidate|2062|(1, 14)|var|int32
func_2061_call = mutated_mod.get_global_var('func_2061')
call_2063 = func_2061_call(var_2062)
output = call_2063
func_2064 = relay.Function([var_2062], output)
mutated_mod['func_2064'] = func_2064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2093 = func_1487_call()
call_2094 = func_1487_call()
output = relay.Tuple([call_2093,])
output2 = relay.Tuple([call_2094,])
func_2096 = relay.Function([], output)
mod['func_2096'] = func_2096
mod = relay.transform.InferType()(mod)
mutated_mod['func_2096'] = func_2096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mutated_mod.get_global_var('func_2096')
call_2097 = func_2096_call()
output = call_2097
func_2098 = relay.Function([], output)
mutated_mod['func_2098'] = func_2098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_2131 = relay.TupleGetItem(func_1608_call(), 1)
call_2132 = relay.TupleGetItem(func_1610_call(), 1)
func_1229_call = mod.get_global_var('func_1229')
func_1232_call = mutated_mod.get_global_var('func_1232')
call_2143 = func_1229_call(relay.reshape(call_2131.astype('bool'), [4, 8, 14]), relay.reshape(call_2131.astype('bool'), [4, 8, 14]), )
call_2144 = func_1229_call(relay.reshape(call_2131.astype('bool'), [4, 8, 14]), relay.reshape(call_2131.astype('bool'), [4, 8, 14]), )
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_2149 = relay.TupleGetItem(func_1396_call(), 0)
call_2150 = relay.TupleGetItem(func_1397_call(), 0)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2165 = relay.TupleGetItem(func_2030_call(), 0)
call_2166 = relay.TupleGetItem(func_2032_call(), 0)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_2172 = relay.TupleGetItem(func_2096_call(), 0)
call_2173 = relay.TupleGetItem(func_2098_call(), 0)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
var_2181 = relay.var("var_2181", dtype = "float32", shape = (1, 48))#candidate|2181|(1, 48)|var|float32
call_2180 = func_212_call(relay.reshape(var_2181.astype('float32'), [8, 1, 6]))
call_2182 = func_212_call(relay.reshape(var_2181.astype('float32'), [8, 1, 6]))
output = relay.Tuple([call_2131,call_2143,call_2149,call_2165,call_2172,call_2180,var_2181,])
output2 = relay.Tuple([call_2132,call_2144,call_2150,call_2166,call_2173,call_2182,var_2181,])
func_2187 = relay.Function([var_2181,], output)
mod['func_2187'] = func_2187
mod = relay.transform.InferType()(mod)
mutated_mod['func_2187'] = func_2187
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2188 = relay.var("var_2188", dtype = "float32", shape = (1, 48))#candidate|2188|(1, 48)|var|float32
func_2187_call = mutated_mod.get_global_var('func_2187')
call_2189 = func_2187_call(var_2188)
output = call_2189
func_2190 = relay.Function([var_2188], output)
mutated_mod['func_2190'] = func_2190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2216 = relay.TupleGetItem(func_2030_call(), 1)
call_2217 = relay.TupleGetItem(func_2032_call(), 1)
func_483_call = mod.get_global_var('func_483')
func_486_call = mutated_mod.get_global_var('func_486')
const_2241 = relay.const([[-10,-10,-3,-8,-5,9,3,4,-9,3,-1,-1,10,3]], dtype = "int32")#candidate|2241|(1, 14)|const|int32
const_2242 = relay.const([[2,10,-4,10,2,-1,2,-6,4,-10,6,9,3,6,1,-10,2,7,-8,9,7,-9,-4,7,-8,6,-1,6,4,-3,-3,-2,-5,-10,-5,1,9,-10,-6,2,6,-6,5,-10,-5,6,6,-5,-6,-3,4,-5,-7,-5,-4,7,-6,-6,8,-10,8,10,-5,-6,10,3,7,-6,-3,-7],[7,-8,8,4,9,-8,-3,3,-3,-10,-2,8,1,4,-4,-2,5,-6,1,9,-7,8,-5,-7,-2,3,9,3,-5,5,-8,-10,6,-5,7,8,-1,1,7,-4,6,5,1,5,-7,-5,7,9,3,-2,-8,-4,7,4,-5,7,10,-7,1,6,2,6,-1,5,-9,-4,-9,7,-6,-2],[-1,-2,-10,-1,1,-3,-3,6,-4,-7,10,-9,4,5,-8,10,-5,-2,3,7,5,1,-9,-1,8,3,3,-6,-9,-4,-7,10,-1,6,8,-8,-3,8,-5,-4,-8,10,-10,-8,-7,-10,9,8,-2,3,-2,-10,9,-9,-8,-7,10,10,6,-3,-10,-1,2,-10,6,4,-6,2,-4,-2],[-4,1,-8,5,6,-7,2,-7,7,-1,-3,-2,-1,4,5,-10,-5,-4,9,-7,9,3,-1,-6,-10,-3,1,-1,2,-8,3,8,8,-3,1,-1,-3,2,7,-6,2,-1,7,-5,-9,-5,-10,10,-5,4,10,-8,2,-1,-5,-7,8,-10,-9,-1,-8,1,-1,6,2,6,5,-9,4,-7],[6,-8,3,-9,-4,3,9,2,4,8,7,-8,-7,-1,-8,10,4,10,7,-2,-2,-3,-10,2,2,-8,5,-1,-4,3,-3,-7,10,-6,7,-8,-6,9,-5,-8,5,5,-3,-10,9,10,-8,-10,-4,-7,-8,-1,5,10,3,6,5,7,8,-6,3,-2,5,-9,-10,-2,-9,-3,-3,6],[-1,5,6,4,9,2,10,-1,5,5,-6,6,-2,-2,3,4,-2,10,8,3,-7,-9,8,1,-4,1,-7,-5,-5,5,-7,-2,7,9,7,5,7,-1,6,8,-10,9,-5,8,3,8,4,1,1,7,3,3,5,-5,-6,2,4,-5,6,-9,-7,-1,6,-2,-3,6,-8,4,-3,-6],[-5,-4,10,10,-3,8,-5,-2,-10,-9,-3,9,-5,7,-5,6,-1,-9,-10,-10,-7,6,7,4,-4,2,-9,9,5,2,8,8,-8,2,-7,4,1,5,-10,7,3,9,10,7,-3,5,-9,-1,-1,7,-5,9,3,-6,-6,-6,4,-2,5,-2,-10,-10,-10,-8,-3,-9,9,6,4,6],[-9,-9,-10,-9,-2,-3,-8,3,-3,-8,-7,-5,-5,-8,-7,10,-7,-8,2,3,-8,8,1,-3,4,9,8,-8,6,-3,10,-10,-4,7,-6,10,7,2,-1,2,-6,-7,-6,-9,-10,-7,8,1,-8,8,7,9,-7,-3,4,2,-6,-6,3,-5,8,5,-1,-7,-3,2,4,5,2,8]], dtype = "int32")#candidate|2242|(8, 70)|const|int32
call_2240 = relay.TupleGetItem(func_483_call(relay.reshape(const_2241.astype('int32'), [14, 1, 1]), relay.reshape(const_2242.astype('int32'), [14, 8, 5]), ), 3)
call_2243 = relay.TupleGetItem(func_486_call(relay.reshape(const_2241.astype('int32'), [14, 1, 1]), relay.reshape(const_2242.astype('int32'), [14, 8, 5]), ), 3)
uop_2246 = relay.sqrt(const_2242.astype('float32')) # shape=(8, 70)
var_2254 = relay.var("var_2254", dtype = "float32", shape = (8, 70))#candidate|2254|(8, 70)|var|float32
bop_2255 = relay.multiply(uop_2246.astype('int16'), relay.reshape(var_2254.astype('int16'), relay.shape_of(uop_2246))) # shape=(8, 70)
func_2061_call = mod.get_global_var('func_2061')
func_2064_call = mutated_mod.get_global_var('func_2064')
call_2265 = relay.TupleGetItem(func_2061_call(relay.reshape(const_2241.astype('int32'), [1, 14])), 1)
call_2266 = relay.TupleGetItem(func_2064_call(relay.reshape(const_2241.astype('int32'), [1, 14])), 1)
bop_2270 = relay.power(const_2242.astype('float32'), relay.reshape(uop_2246.astype('float32'), relay.shape_of(const_2242))) # shape=(8, 70)
uop_2296 = relay.log(uop_2246.astype('float32')) # shape=(8, 70)
uop_2312 = relay.exp(uop_2296.astype('float64')) # shape=(8, 70)
var_2315 = relay.var("var_2315", dtype = "float64", shape = (8, 70))#candidate|2315|(8, 70)|var|float64
bop_2316 = relay.equal(uop_2312.astype('bool'), relay.reshape(var_2315.astype('bool'), relay.shape_of(uop_2312))) # shape=(8, 70)
bop_2319 = relay.add(uop_2246.astype('int16'), relay.reshape(uop_2296.astype('int16'), relay.shape_of(uop_2246))) # shape=(8, 70)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
const_2324 = relay.const([-9,2,-3,10,10,1,6,10,8,5,-3,-3,2,6,8,-10,-2,8,5,-9,-10,6,-2,1,2,-4,-4,-10,7,-6,-7,3,-7,7,8,8,6,-7,10,10,6,7,-1,10,-2,6,-1,9,9,-1,-3,7,4,-8,4,6,-2,-9,1,4,6,-3,6,-6,-9,3,7,-3,-6,5,9,-7,8,7,-7,-3,10,9,-9,2,-3,1,-7,-1,5,10,-9,8,-6,7,7,-6,5,4,4,3,1,7,8,10,6,-9,8,4,-4,7,10,-6,-1,-10,-6,-2,7,-4,9,-10,3,-2,9,-5,9,-2,-5,6,1,-1,-1,4,2,4,-4,-6,8,-2,-4,-9,8,3,-4,-1,5,1,-5,-3,-5,-8,-5,-9,-10,9,-7,8,2,3,10,-10,-8,-2,-4,-1,4,-1,4,2,-1,2,9,-7,1,6,6,8,-5,-8,-5,-9,10,8,9,10,8,10,-3,-10,-7,-8,2,-6,4,7,2,-8,7,-6,7,8,9,-5,-7,7,-1,6,10,-2,5,-6,7,-9,2,-3,-3,-4,-1,7,4,-1,-10,8,-10,-4,10,-1,-6,3,6,-6,-1,3,1,-9,5,-10,8,5,-10,2,-9,-9,1,-2,2,-10,-10,4,-5,6,6,5,6,3,-10,-8,-5,-5,-10,7,-7,-4,10,-8,-2,6,-2,1,2,-6,8,3,-10,4,-5,4,8,9,-8,4,5,6,-3,-7,-3,-7,-6,4,9,10,9,-4,-1,-6,1,-9,-9,6,-3,9,6,7,-8,-10,9,9,-3,4,9,5,9,8,10,-2,-7,-1,8,-6,8,-1,7,2,6,-6,-3,5,-6,10,7,8,-4,6,4,-6,8,-9,1,5,-7,-2,-1,-2,10,-10,5,-10,7,-1,-5,-7,-6,8,-8,-7,-1,5,6,8,3,-6,9,9,1,1,7,-1,-2,4,-9,5,10,3,-9,-3,-2,-3,4,-7,4,-2,-3,5,1,5,10,1,10,-5,8,3,8,9,10,8,-3,4,-1,-1,-10,-2,6,10,9,9,3,7,10,5,1,3,-4,-2,-9,7,1,2,5,5,5,-3,-6,4,-6,7,2,3,-8,-1,8,-8,9,6,2,-2,-5,-7,-3,8,-10,9,4,6,-5,-3,-4,9,3,-9,-7,3,-4,-5,-3,-10,-10,5,-9,8,-7,-6,-3,6,2,-10,6,3,6,-1,-2,10,-8,-6,5,2,6,-4,-4,-7,-6,9,2,2,-1,5,-1,-7,-9,5,-8,7,-4,-5,1,-9,10,-7,-10,-8,-1,6,9,1,8,-3,5,-4,-1,9,2,-7,4,5,-2,-6,-8,-6,-10,5,5,6,-6,-8,1,8,-5,-8,-8,4,-7,-2,-7,-2,-5,4,-2,9,3,6,-7,9,-9,3,-9,-5,9,1,-8,-2,-9,3,9,3,3,7,-4,-10,-5,-10,9,-3,5,-6,-7,5,7,1,-4,-9,4,5,-6,10,-9,6,-6,-10,-2,-3,5,9,10,9,2,10,-5,3,3,3,-4,2,7,-2,-6,-2,-6,4,-8,-9,2,8,6,1,7,-1,-2,-2,3,-1,-10,4,3,2,-3,-4,10,-4,-3,6,-10,8,10,-2,5,-3,-6,9,-7,1,-1,6,-4,8,7,7,2,9,7,-6,7,-5,6,-2,-4,2,-9,7,-9,3,2,3,-5,-8,4,-3,3,3,4,2,-10,5,5,5,10,1,-7,-8,5,-5,7,-7,7,-10,5,1,8,-7,10,8,9,2,4,-8,-3,7,2,10,3,-10,-2,6,-9,-5,-6,-8,4,2,-9,8,-5,4,8,7,-4,2,10,-9,4,7,-9,-6,5,3,-10,8,4,3,7,-5,-8,10,6,6,-3,9,-6,-7,5,-4,10,2,-5,-8,-6,-5,2,10,-3,8,-7,-10,-6,-3,6,7,1,-10,4,-1,2,5,-1,2,3,-2,8,5,-6,6,8,-7,-3,-7,6,-9,4,-10,1,9,-3,4,2,7,10,1,7,8,7,-6,3,-3,9,2,-7,-4,1,-2,-9,-2,-10,-8,-10,-6,-4,-2,-8,-6,8,9,-8,-4,8,3,-2,-6,-7,-1,3,-6,10,3,-2,-6,-6,6,5,4,-5,-3,-1,3,-5,5,-2,4,6,1,-6,-8,2,-8,-5,4,-9,-1,10,-6,-8,5,-1,-3,6,-7,-1,-9,-1,3,9,-8,-6,7,-10,-3,6,-8,6,-4,-5,9,5,10,4,2,1,-2,-6,7,3,-6,-9,-4,8,-9,8,-9,-7,9,-2,-5,-2,4,-5,7,10,-7,-8,5,-10,8,-4,10,-6,3,3,-3,-2,-4,7,-4,-3,-9,3,-6,10,-8,-1,-6,-9,-6,-6,7,5,8,1,2,-5,6,5,-9,-5,9,-7,-6,-5,-9,1,-2,5,2,-2,-1,-3,2,-8,3,10,-1,7,5,10,-5,-10,-9,5,-3,6,-3,-1,-9,6,2,1,4,3,-2,-1,-5,-1,8,-6,4,-4,-2,-2,4,10,5,-1,1,-6,8,9,-8,8,10,-6,-5,-1,-7,-8,10,-7,1,-2,2,7,-5,3,-9,-1,6,-3,-2,-10,7,10,-5,-2,4,1,4,-8,-6,-6,4,6,-7,-1,-5,-7,-6,-2,3,7,10,5,-8,4,-6,9,-8,-9,5,-3,8,5,-9,7,10,1,-4,7,1,-5,2,6,10,6,-5,8,-10,-9,7,-1,2,1,8,7,9,-6,-8,10,8,-5,-6,-8,5,5,5,-1,8,2,-9,-5,3,-9,4,10,9,6,-8,10,-6,-5,3,-8,9,-6,9,7,1,-2,9,-8,7,2,2,9,10,-9,-2,-1,6,-9,7,8,4,-6,2,-1,-9,6,-8,-9,1,-9,-4,-3,-8,-5,8,6,3,-7,5,6,3,-5,-7,9,-4,-10,-1,-9,5,7,-9,-5,4,-9,-10,-2,7,5,-4,1,-5,6,-3,-8,-9,2,-7,-10,7,-9,-6,-1,10,8,-2,-4,1,-6,3,3,-6,-9,1,3,3,-6,-3,-4,5,-9,-3,6,2,-10,-6,8,9,-5,9,8,-10,-10,1,9,8,-5,-2,-8,-4,1,3,-2,-7,1,-6,9,-3,-10,5,-4,-9,5,-9,6,-1,-3,-6,-5,1,10,-6,3,8,-6,5,5,9,5,-4,1,-8,8,-7,-9,-10,6,-10,5,-4,-10,-3,5,8,9,-1,-5,-5,4,-7,-2,4,3,9,-1,-1,4,-9,-5,8,-8,4,-7,10,1,-6,6,-1,3,7,2,8,-1,6,-3,9,3,-9,-10,-2,6,-4,-8,-9,2,7,-5,4,2,-1,-4,8,-4,8,6,7,-9,-2,3,-10,-9,-10,3,-10,4,2,4,5,-9,-1,4,4,-6,-2,10,-5,10,5,1,-10,9,-5,2,-10,-5,-5,-9,-4,-7,-6,-10,-8,-8,6,8,-6,-8,1,-3,2,-2,-6,-5,-9,-5,-9,-8,7,-10,9,9,-7,8,-6,9,-6,-2,-5,3,9,-1,-4,5,-8,2,-3,3,-5,-7,2,8,8,-10,-9,9,2,-6,10,6,4,-7,9,6,1,-9,-9,10,-9,4,-3,5,4,2,5,-4,-7,6,1,4,-5,-4,9,6,6,5,-3,-7,-6,-3,-6,-9,-9,1,-7,3,-5,8,3,-2,-4,-10,-1,-5,7,-7,-8,8,-1,7,-3,10,9,3,-4,1,-4,-6,-10,-2,-1,-10,5,-6,6,-4,4,-6,-4,5,4,5,-8,2,1,5,-5,3,-4,4,-2,8,2,9,2,3,1,-3,8,9,1,5,10,4,7,-3,-8,-5,2,8,9,10,-1,10,-8,3,2,5,-4,-5,9,-9,6,7,9,4,9,9,4,-1,6,-4,-2,10,8,-8,-1,5,-3,7,-10,-2,-2,-10,8,-3,-7,-3,-5,-8,6,1,-5,7,1,-9,-3,-9,-2,5,2,6,-4,8,-2,4,2,-7,2,-4,8,-3,6,9,-2,-10,2,-2,5,-8,8,-6,7,-9,9,-3,9,-9,-7,7,-3,-4,2,-3,-9,5,3,10,-9,9,2,-5,8,-8,-2,-6,1,-10,-7,-4,-6,-2,2,-8,-10,-9,1,-5,-9,5,9,4,1,-5,-9,-3,-7,3,-8,10,-10,-2,6,9,10,5,-3,-9,7,3,10,2,-2,7,-7,-7,10,7,7,-9,8,-6,7,5,9,9,-5,-7,5,4,2,9,1,6,-2,4,-3,10,6,-1,5,-6,-2,-5,6,-10,-3,10,7,-1,-3,6,5,-5,5,-8,7,-1,7,-7,-7,1,6,-3,9,9,-1,7,4,9,-9,10,-2,-6,-6,2,-10,5,-4,8,-4,-5,-5,-1,8,8,8,5,8,-7,-4,2,-1,9,-5,1,3,6,-10,-9,-6,6,-5,-2,-2,-1,-9,8,8,-7,4,6,-4,7,9,4,3,1,-1,-4,3,9,6,4,-5,-9,-9,-8,9,-6,-1,6,-2,-5,10,-8,-3,-5,-4,-3,9,10,8,10,-3,-6,9,-10,6,4,3,9,8,-4,-4,-1,-2,-1,-9,10,7,8,-7,-7,-4,-1,2,4,5,-2,9,-3,6,-1,-5,9,-6,-6,-5,-6,-5,-7,-8,-6,-3,3,4,10,10,-5,2,-6,10,9,-6,-4,3,-7,4,-5,4,8,-4,7,10,10,7,8,8,1,-6,5,8,-10,5,-1,3,-6,6,4,9,-7,10,2,-7,-3,9,2,-2,-2,-8,-8,10,10,9,-3,-8,5,-8,-7,1,7,10,9,-2,10,4,2,2,-2,-6,1,5,-3,2,-9,-1,-3,8,4,-3,-1,-2,10,5,-9,5,6,-6,7,8,-1,4,2,7,1,10,-8,-5,8,-10,-10,7,-7,4,10,-1,2,8,7,-10,7,10,-2,-4,4,7,9,9,-6,-1,6,-1,7,-4,7,3,-6,9,-10,10,9,6,-1,5,10,4,-9,-8,-4,-1,8,5,10,6,1,2,3,-7,4,2,9,4,10,-4,-4,-7,2,-10,10,-10,10,-8,-1,9,-8,-3,-6,-4,-9,-3,5,7,4,10,3,-4,2,-8,-10,10,8,4,10,-10,-6,2,-5,-9,-8,4,8,4,3,-5,-1,-10,10,-10,-9,9,-5,9,2,10,8,9,3,8,-9,8,9,6,-9,-10,-7,6,-2,2,4,3,-6,-9,-8,-5,-9,-7,-9,10,9,6,10,10,8,5,-3,-5,-1,-8,-9,-7,5,9,-5,2,8,2,2,10,-3,4,-3,7,-1,-4,7,1,5,6,8,6,5,-5,-1,7,-2,-1,9,-1,-2,-3,8,3,-5,-5,-6,-10,-10,-8,-2,6,7,6,-5,6,-2,8,-6,-5,-1,-5,-3,6,2,6,-10,-5,-10,-4,-8,4,-1,1,-5,-8,9,1,-8,7,4,1,6,2,-7,-10,-9,6,-7,7,5,8,9,-6,-8,-9,6,8,-6,-7,9,9,-2,-5,-5,-2,-10,-4,2,7,3,-4,-6,9,3,8,-5,-7,3,9,8,8,-2,6,2,-5,1,-4,-2,-10,10,8,-4,-4,8,-5,-7,-4,-7,4,-8,-6,6,8,4,-4,8,2,6,-1,1,1,-10,6,9,-1,-9], dtype = "int16")#candidate|2324|(2145,)|const|int16
call_2323 = relay.TupleGetItem(func_533_call(relay.reshape(const_2324.astype('int16'), [13, 15, 11]), relay.reshape(const_2324.astype('int16'), [13, 15, 11]), relay.reshape(uop_2296.astype('int32'), [560,]), ), 2)
call_2325 = relay.TupleGetItem(func_537_call(relay.reshape(const_2324.astype('int16'), [13, 15, 11]), relay.reshape(const_2324.astype('int16'), [13, 15, 11]), relay.reshape(uop_2296.astype('int32'), [560,]), ), 2)
func_1870_call = mod.get_global_var('func_1870')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_2326 = func_1870_call()
call_2327 = func_1870_call()
output = relay.Tuple([call_2216,call_2240,const_2241,bop_2255,call_2265,bop_2270,bop_2316,bop_2319,call_2323,const_2324,call_2326,])
output2 = relay.Tuple([call_2217,call_2243,const_2241,bop_2255,call_2266,bop_2270,bop_2316,bop_2319,call_2325,const_2324,call_2327,])
func_2335 = relay.Function([var_2254,var_2315,], output)
mod['func_2335'] = func_2335
mod = relay.transform.InferType()(mod)
mutated_mod['func_2335'] = func_2335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2335_call = mutated_mod.get_global_var('func_2335')
var_2337 = relay.var("var_2337", dtype = "float32", shape = (8, 70))#candidate|2337|(8, 70)|var|float32
var_2338 = relay.var("var_2338", dtype = "float64", shape = (8, 70))#candidate|2338|(8, 70)|var|float64
call_2336 = func_2335_call(var_2337,var_2338,)
output = call_2336
func_2339 = relay.Function([var_2337,var_2338,], output)
mutated_mod['func_2339'] = func_2339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2384 = relay.TupleGetItem(func_2030_call(), 2)
call_2385 = relay.TupleGetItem(func_2032_call(), 2)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
var_2387 = relay.var("var_2387", dtype = "float32", shape = (2, 24))#candidate|2387|(2, 24)|var|float32
call_2386 = func_212_call(relay.reshape(var_2387.astype('float32'), [8, 1, 6]))
call_2388 = func_212_call(relay.reshape(var_2387.astype('float32'), [8, 1, 6]))
bop_2401 = relay.floor_divide(call_2386.astype('float64'), relay.reshape(var_2387.astype('float64'), relay.shape_of(call_2386))) # shape=(8, 1, 6)
bop_2404 = relay.floor_divide(call_2388.astype('float64'), relay.reshape(var_2387.astype('float64'), relay.shape_of(call_2388))) # shape=(8, 1, 6)
output = relay.Tuple([call_2384,bop_2401,])
output2 = relay.Tuple([call_2385,bop_2404,])
func_2408 = relay.Function([var_2387,], output)
mod['func_2408'] = func_2408
mod = relay.transform.InferType()(mod)
mutated_mod['func_2408'] = func_2408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2409 = relay.var("var_2409", dtype = "float32", shape = (2, 24))#candidate|2409|(2, 24)|var|float32
func_2408_call = mutated_mod.get_global_var('func_2408')
call_2410 = func_2408_call(var_2409)
output = call_2410
func_2411 = relay.Function([var_2409], output)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1870_call = mod.get_global_var('func_1870')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_2514 = func_1870_call()
call_2515 = func_1870_call()
uop_2517 = relay.atan(call_2514.astype('float64')) # shape=(4, 2, 4)
uop_2519 = relay.atan(call_2515.astype('float64')) # shape=(4, 2, 4)
output = relay.Tuple([uop_2517,])
output2 = relay.Tuple([uop_2519,])
func_2521 = relay.Function([], output)
mod['func_2521'] = func_2521
mod = relay.transform.InferType()(mod)
mutated_mod['func_2521'] = func_2521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2521_call = mutated_mod.get_global_var('func_2521')
call_2522 = func_2521_call()
output = call_2522
func_2523 = relay.Function([], output)
mutated_mod['func_2523'] = func_2523
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2530 = relay.var("var_2530", dtype = "uint64", shape = (13, 4, 16))#candidate|2530|(13, 4, 16)|var|uint64
var_2531 = relay.var("var_2531", dtype = "uint64", shape = (13, 4, 16))#candidate|2531|(13, 4, 16)|var|uint64
bop_2532 = relay.less_equal(var_2530.astype('bool'), relay.reshape(var_2531.astype('bool'), relay.shape_of(var_2530))) # shape=(13, 4, 16)
uop_2536 = relay.log(var_2531.astype('float32')) # shape=(13, 4, 16)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
var_2541 = relay.var("var_2541", dtype = "float64", shape = (1638,))#candidate|2541|(1638,)|var|float64
call_2540 = relay.TupleGetItem(func_1070_call(relay.reshape(var_2541.astype('float64'), [14, 13, 9])), 0)
call_2542 = relay.TupleGetItem(func_1073_call(relay.reshape(var_2541.astype('float64'), [14, 13, 9])), 0)
bop_2546 = relay.floor_divide(bop_2532.astype('float64'), relay.reshape(uop_2536.astype('float64'), relay.shape_of(bop_2532))) # shape=(13, 4, 16)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2568 = func_1487_call()
call_2569 = func_1487_call()
output = relay.Tuple([call_2540,var_2541,bop_2546,call_2568,])
output2 = relay.Tuple([call_2542,var_2541,bop_2546,call_2569,])
func_2577 = relay.Function([var_2530,var_2531,var_2541,], output)
mod['func_2577'] = func_2577
mod = relay.transform.InferType()(mod)
mutated_mod['func_2577'] = func_2577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2577_call = mutated_mod.get_global_var('func_2577')
var_2579 = relay.var("var_2579", dtype = "uint64", shape = (13, 4, 16))#candidate|2579|(13, 4, 16)|var|uint64
var_2580 = relay.var("var_2580", dtype = "uint64", shape = (13, 4, 16))#candidate|2580|(13, 4, 16)|var|uint64
var_2581 = relay.var("var_2581", dtype = "float64", shape = (1638,))#candidate|2581|(1638,)|var|float64
call_2578 = func_2577_call(var_2579,var_2580,var_2581,)
output = call_2578
func_2582 = relay.Function([var_2579,var_2580,var_2581,], output)
mutated_mod['func_2582'] = func_2582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2584 = func_1487_call()
call_2585 = func_1487_call()
output = relay.Tuple([call_2584,])
output2 = relay.Tuple([call_2585,])
func_2589 = relay.Function([], output)
mod['func_2589'] = func_2589
mod = relay.transform.InferType()(mod)
output = func_2589()
func_2590 = relay.Function([], output)
mutated_mod['func_2590'] = func_2590
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2602 = relay.const([[[-2,6,6,4,-3,4,-3,-1,-9,6],[-2,10,2,-6,4,-8,2,8,-6,-9],[-7,4,-2,-6,9,4,1,-7,-2,6],[8,4,-8,8,-5,6,-10,2,5,-4]],[[2,-4,-2,5,-3,-1,3,-8,8,-8],[5,-4,4,8,4,2,9,-8,-8,-6],[4,-9,-5,-9,-5,7,-2,-4,5,-6],[3,6,5,-5,-6,1,2,-6,-8,-1]],[[5,4,7,4,9,4,7,8,-3,-2],[-5,1,-4,4,4,-7,-1,6,9,3],[-7,2,8,-3,-2,-2,-7,-2,-9,-3],[2,-2,8,-3,6,-5,-5,-7,8,4]],[[7,6,-8,-7,7,-10,9,-3,7,-6],[-4,-6,-9,-1,-4,-8,2,7,4,-7],[-3,9,-6,-8,8,6,4,-2,4,1],[-10,-1,3,-2,-9,8,-5,-3,-1,2]],[[5,-3,9,-6,-1,-2,-8,-3,10,-7],[-6,10,-6,-10,4,-6,9,1,-7,2],[-4,8,9,2,-9,-8,-6,4,-3,-8],[-8,7,-6,-7,5,-10,6,-10,1,2]],[[-3,-5,-1,2,5,1,8,1,6,8],[9,-10,-8,-10,6,-1,4,-9,-6,9],[5,-5,7,9,-7,-5,-7,-3,-9,5],[7,-4,3,6,-8,-3,2,-6,-7,4]],[[-1,2,8,-2,8,-2,-3,-6,2,6],[-6,5,-8,-10,-5,8,-3,-2,4,10],[1,-9,-10,3,-8,4,-9,-3,-9,1],[-7,-7,-7,-3,-7,5,5,-4,-10,9]],[[-7,3,1,2,-8,1,10,-8,-1,10],[-4,-5,10,5,6,9,6,-9,9,-6],[-4,4,9,5,-3,-7,9,-7,3,2],[-4,5,2,-9,-7,7,2,-7,3,10]],[[-6,-2,-10,7,-1,-5,7,-6,-3,-1],[-10,4,-2,-4,3,-1,-2,6,-4,-9],[2,-9,-3,-10,-10,9,-1,-1,-5,6],[-8,9,-1,-5,-9,-7,6,10,1,-8]],[[-2,8,-1,4,3,-4,-8,2,-9,4],[1,9,-9,9,-10,10,5,3,8,-3],[-9,3,-1,7,-2,-8,-4,2,-7,-3],[7,6,1,9,-7,10,9,-3,8,10]],[[3,-5,-6,-10,8,-7,7,9,3,7],[10,5,-3,-10,8,-3,8,8,6,5],[3,9,5,10,-5,9,-6,-5,-3,-2],[-2,4,4,4,-3,-4,-4,8,2,-9]],[[-7,-10,-3,6,9,10,2,3,-7,-5],[-7,9,-3,-1,7,2,8,-10,9,10],[-1,-9,-6,6,9,-6,-2,10,-1,2],[4,-1,8,-5,5,-4,10,9,8,-1]],[[-9,-7,-1,-8,-9,8,6,8,-1,10],[-10,4,2,6,-7,6,4,-6,-2,7],[7,-5,-7,5,-5,5,3,-7,-1,4],[-10,5,-6,8,7,9,3,5,8,7]],[[8,1,1,8,-3,-1,5,-8,7,8],[3,6,-1,5,2,5,4,-3,5,7],[4,-10,2,-9,-4,-2,2,3,2,5],[10,6,-5,8,-10,8,5,-2,-6,7]],[[-8,8,-9,-7,9,-5,-1,4,9,6],[9,1,3,-10,-6,10,-7,8,-9,7],[7,8,4,-6,6,-10,7,8,9,-1],[-6,-1,-7,-9,5,6,-9,-2,8,5]]], dtype = "uint32")#candidate|2602|(15, 4, 10)|const|uint32
const_2603 = relay.const([[[-5,7,7,7,-7,4,-4,5,-6,-10],[-2,2,3,6,9,9,10,3,2,-7],[5,-8,8,3,-8,6,3,-7,1,6],[5,-4,-1,-6,9,6,3,-2,-7,2]],[[9,-5,-5,1,-8,-5,-4,1,10,-10],[9,2,10,-2,1,2,3,2,-10,3],[10,4,-1,-9,10,-9,-7,-10,6,-2],[5,9,-1,-5,6,2,10,-1,-1,-9]],[[2,-2,8,6,4,-5,1,-9,6,5],[6,7,-1,4,-1,-5,-10,3,-8,5],[8,3,1,4,-7,-9,-6,6,7,1],[4,2,-10,-3,-6,10,-6,3,-4,7]],[[6,6,-2,-9,-4,-8,4,-2,7,-5],[-4,6,8,9,6,5,10,4,-4,3],[-5,6,-1,6,-2,10,5,-5,-5,5],[10,7,-3,-4,-6,-7,-9,10,9,-5]],[[-6,8,1,2,-8,1,-9,10,9,-1],[2,-4,8,1,10,8,-3,5,10,1],[-6,-7,-9,9,10,1,-5,-5,8,10],[-3,4,-7,-9,-10,-4,-3,3,8,1]],[[1,4,-8,-9,-4,-6,9,3,1,-2],[4,-7,-9,-10,2,6,5,9,6,2],[7,7,10,-2,3,3,-10,-4,-3,-5],[-6,-8,1,-6,5,9,6,10,7,10]],[[-5,-5,5,3,6,3,-9,4,-8,6],[-8,7,-2,-3,-10,9,6,-2,3,-9],[5,10,-2,-5,5,-6,-8,-9,10,9],[3,-5,2,-9,3,6,9,4,-2,-4]],[[2,-4,-2,1,4,-2,-10,7,-2,-8],[6,5,-4,9,-9,5,-4,2,-1,-8],[4,2,-4,-7,7,5,3,-1,10,3],[4,9,-6,-5,-5,-1,-2,-7,2,-5]],[[1,-4,-10,9,4,9,9,-7,-10,-1],[-5,8,-5,-6,-8,8,2,4,-5,-2],[-5,9,9,-9,8,8,4,3,-8,8],[9,-7,-8,-3,-4,-3,5,4,-8,7]],[[-5,-9,8,8,-8,-3,-2,8,-1,-4],[7,5,9,-8,-4,-3,9,-8,4,4],[-2,-1,-7,-4,-1,3,-6,-9,-8,4],[-3,1,-8,10,6,-6,-3,5,-9,10]],[[9,-9,4,2,7,1,2,4,2,-2],[8,-9,6,-2,-2,6,-8,6,2,-1],[3,-1,-8,5,-8,8,-4,8,-10,-6],[5,-4,4,4,-8,-5,10,4,-10,8]],[[5,-8,3,-10,8,-5,-9,-7,-9,-8],[-7,5,-10,3,-9,2,7,4,5,4],[1,8,10,-2,-6,3,-7,1,1,-9],[-5,4,-8,3,-2,9,-8,-3,2,-7]],[[-8,-4,-3,2,8,-2,-2,-4,-5,-6],[-8,10,1,6,9,-4,6,-1,2,2],[-3,-3,-1,5,-6,10,-5,-1,4,-10],[3,-1,3,-7,-3,4,-3,3,4,9]],[[1,7,4,2,5,2,-9,6,-2,6],[-4,-3,7,-3,6,-4,-5,-4,-7,6],[10,10,10,-3,9,-2,-2,-1,3,-2],[8,-9,-9,4,9,9,-10,3,5,4]],[[3,-6,-3,6,3,-4,-5,5,-5,-9],[-1,-8,-7,10,-4,5,-2,-4,10,-10],[7,-3,8,6,7,10,6,-8,8,5],[6,-1,1,-5,7,-1,1,9,-3,5]]], dtype = "uint32")#candidate|2603|(15, 4, 10)|const|uint32
bop_2604 = relay.bitwise_and(const_2602.astype('uint32'), relay.reshape(const_2603.astype('uint32'), relay.shape_of(const_2602))) # shape=(15, 4, 10)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_2626 = relay.TupleGetItem(func_1396_call(), 0)
call_2627 = relay.TupleGetItem(func_1397_call(), 0)
func_1717_call = mod.get_global_var('func_1717')
func_1721_call = mutated_mod.get_global_var('func_1721')
var_2642 = relay.var("var_2642", dtype = "uint16", shape = (980,))#candidate|2642|(980,)|var|uint16
var_2643 = relay.var("var_2643", dtype = "float64", shape = (1638,))#candidate|2643|(1638,)|var|float64
call_2641 = relay.TupleGetItem(func_1717_call(relay.reshape(var_2642.astype('uint16'), [7, 10, 14]), relay.reshape(var_2643.astype('float64'), [1638,]), relay.reshape(var_2642.astype('float64'), [7, 10, 14]), ), 9)
call_2644 = relay.TupleGetItem(func_1721_call(relay.reshape(var_2642.astype('uint16'), [7, 10, 14]), relay.reshape(var_2643.astype('float64'), [1638,]), relay.reshape(var_2642.astype('float64'), [7, 10, 14]), ), 9)
output = relay.Tuple([bop_2604,call_2626,call_2641,var_2642,var_2643,])
output2 = relay.Tuple([bop_2604,call_2627,call_2644,var_2642,var_2643,])
func_2646 = relay.Function([var_2642,var_2643,], output)
mod['func_2646'] = func_2646
mod = relay.transform.InferType()(mod)
var_2647 = relay.var("var_2647", dtype = "uint16", shape = (980,))#candidate|2647|(980,)|var|uint16
var_2648 = relay.var("var_2648", dtype = "float64", shape = (1638,))#candidate|2648|(1638,)|var|float64
output = func_2646(var_2647,var_2648,)
func_2649 = relay.Function([var_2647,var_2648,], output)
mutated_mod['func_2649'] = func_2649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1788_call = mod.get_global_var('func_1788')
func_1790_call = mutated_mod.get_global_var('func_1790')
call_2654 = relay.TupleGetItem(func_1788_call(), 0)
call_2655 = relay.TupleGetItem(func_1790_call(), 0)
uop_2667 = relay.atanh(call_2654.astype('float32')) # shape=(4, 2, 4)
uop_2669 = relay.atanh(call_2655.astype('float32')) # shape=(4, 2, 4)
func_1229_call = mod.get_global_var('func_1229')
func_1232_call = mutated_mod.get_global_var('func_1232')
const_2680 = relay.const([False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,True,False,False], dtype = "bool")#candidate|2680|(448,)|const|bool
call_2679 = func_1229_call(relay.reshape(const_2680.astype('bool'), [4, 8, 14]), relay.reshape(const_2680.astype('bool'), [4, 8, 14]), )
call_2681 = func_1229_call(relay.reshape(const_2680.astype('bool'), [4, 8, 14]), relay.reshape(const_2680.astype('bool'), [4, 8, 14]), )
func_2521_call = mod.get_global_var('func_2521')
func_2523_call = mutated_mod.get_global_var('func_2523')
call_2682 = relay.TupleGetItem(func_2521_call(), 0)
call_2683 = relay.TupleGetItem(func_2523_call(), 0)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_2727 = relay.TupleGetItem(func_2030_call(), 2)
call_2728 = relay.TupleGetItem(func_2032_call(), 2)
output = relay.Tuple([uop_2667,call_2679,const_2680,call_2682,call_2727,])
output2 = relay.Tuple([uop_2669,call_2681,const_2680,call_2683,call_2728,])
func_2741 = relay.Function([], output)
mod['func_2741'] = func_2741
mod = relay.transform.InferType()(mod)
output = func_2741()
func_2742 = relay.Function([], output)
mutated_mod['func_2742'] = func_2742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_2753 = relay.TupleGetItem(func_2096_call(), 0)
call_2754 = relay.TupleGetItem(func_2098_call(), 0)
uop_2757 = relay.sin(call_2753.astype('float64')) # shape=(4, 2, 4)
uop_2759 = relay.sin(call_2754.astype('float64')) # shape=(4, 2, 4)
output = uop_2757
output2 = uop_2759
func_2760 = relay.Function([], output)
mod['func_2760'] = func_2760
mod = relay.transform.InferType()(mod)
mutated_mod['func_2760'] = func_2760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2760_call = mutated_mod.get_global_var('func_2760')
call_2761 = func_2760_call()
output = call_2761
func_2762 = relay.Function([], output)
mutated_mod['func_2762'] = func_2762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_2768 = relay.TupleGetItem(func_1396_call(), 0)
call_2769 = relay.TupleGetItem(func_1397_call(), 0)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_2775 = relay.TupleGetItem(func_1608_call(), 2)
call_2776 = relay.TupleGetItem(func_1610_call(), 2)
func_1870_call = mod.get_global_var('func_1870')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_2783 = func_1870_call()
call_2784 = func_1870_call()
output = relay.Tuple([call_2768,call_2775,call_2783,])
output2 = relay.Tuple([call_2769,call_2776,call_2784,])
func_2793 = relay.Function([], output)
mod['func_2793'] = func_2793
mod = relay.transform.InferType()(mod)
output = func_2793()
func_2794 = relay.Function([], output)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_2806 = relay.TupleGetItem(func_1608_call(), 0)
call_2807 = relay.TupleGetItem(func_1610_call(), 0)
output = relay.Tuple([call_2806,])
output2 = relay.Tuple([call_2807,])
func_2810 = relay.Function([], output)
mod['func_2810'] = func_2810
mod = relay.transform.InferType()(mod)
mutated_mod['func_2810'] = func_2810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2810_call = mutated_mod.get_global_var('func_2810')
call_2811 = func_2810_call()
output = call_2811
func_2812 = relay.Function([], output)
mutated_mod['func_2812'] = func_2812
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2822 = relay.var("var_2822", dtype = "float64", shape = (7, 9, 12))#candidate|2822|(7, 9, 12)|var|float64
uop_2823 = relay.sigmoid(var_2822.astype('float64')) # shape=(7, 9, 12)
func_2577_call = mod.get_global_var('func_2577')
func_2582_call = mutated_mod.get_global_var('func_2582')
const_2826 = relay.const([-7,1,-3,9,9,-6,-3,-2,8,-9,-10,3,3,-1,4,-9,4,2,-8,-7,-9,3,-5,-4,2,4,-10,-3,6,3,-10,2,2,-1,7,9,-4,-9,1,2,9,-5,-2,1,-4,2,7,-8,-10,-1,-1,-2,-7,4,4,-1,-1,-3,-7,-4,1,3,-10,8,1,4,4,-7,-6,-8,6,-5,-8,-3,-5,3,3,-7,-8,2,6,3,3,-2,-10,1,-2,4,-7,4,-4,-1,5,-1,-2,-2,2,-10,-5,5,-3,-1,5,6,2,7,6,-6,-5,-4,1,-5,3,-7,-6,-4,-1,3,-10,-7,8,2,-1,5,-5,-10,6,1,-1,-8,3,5,8,-9,8,3,-1,9,3,-9,-2,-9,6,-8,10,-3,1,-8,-7,-7,6,-10,7,10,-1,2,-10,2,1,-3,7,6,4,-6,3,-6,5,8,3,-4,9,-10,7,4,-1,10,3,-5,-10,-9,-4,1,-3,1,-7,2,3,4,3,1,-3,1,7,-4,-5,-1,8,-8,3,8,-6,-7,-4,2,-6,-9,-4,-4,6,-1,1,-10,7,1,-9,9,3,8,-6,-3,3,-1,4,-1,5,1,-5,-6,-9,2,10,-5,7,10,-6,-6,-7,-8,-4,9,-1,7,1,8,-4,10,-2,-7,-10,2,10,-5,-5,-5,-1,10,7,10,3,-8,8,1,6,-9,-4,4,-7,8,3,-2,-2,-8,8,-6,8,7,5,6,-3,8,3,1,3,3,5,-2,-8,7,-10,6,-9,4,9,3,-4,-9,-5,9,2,-5,9,-5,10,2,4,-10,1,7,5,-3,-3,5,5,-7,8,-3,1,-6,1,-3,-6,-8,-10,-8,-4,-3,3,6,-4,4,-9,10,6,-3,4,2,10,8,4,4,-4,7,-4,7,10,-1,2,-8,-7,-7,-6,2,10,7,-3,2,-7,7,5,-9,-9,3,2,-2,-4,-2,10,8,2,-4,4,4,-6,-5,7,8,-6,9,-4,-7,-2,9,-2,1,-2,-9,-2,10,-6,-1,-8,-10,9,2,-2,2,-9,7,-9,5,3,10,9,-5,4,7,-4,8,-6,-7,-1,-4,9,4,-10,-1,-5,10,10,10,-1,10,5,7,10,2,2,-4,5,-8,6,-8,10,-8,3,-8,6,10,-6,3,-10,7,-8,10,8,-8,9,5,6,-4,1,5,-10,7,9,-1,-4,8,1,5,10,-2,-1,-10,2,6,-4,1,4,-9,9,-2,2,4,10,3,-5,8,-3,1,-10,1,7,-7,1,6,10,2,9,-5,7,10,-2,6,-7,-5,5,3,7,5,-10,9,-2,-1,-8,2,2,-7,-2,-4,-3,8,-2,-2,-4,8,-9,-5,-7,-3,-1,-10,9,-1,-4,2,3,-5,-2,5,-3,4,-9,4,5,3,-2,-1,2,-2,7,4,-3,-7,4,-4,5,1,-5,4,-10,-6,-9,3,-10,-8,8,-9,10,7,7,1,7,8,6,-4,6,-1,8,8,1,-7,9,10,-1,3,8,10,7,9,-9,-2,-2,1,10,-10,-7,-10,2,-4,-8,-8,3,2,-5,5,-4,10,1,8,3,2,4,4,3,8,7,8,6,-9,-10,5,-3,-10,8,-8,5,-1,-2,-4,3,8,9,-9,9,8,-4,3,-9,4,2,-8,-1,-5,-4,-10,10,8,-8,-6,6,-6,8,2,6,-5,-7,5,-4,1,-7,6,2,1,-2,7,-3,-2,6,-8,-9,1,8,4,-4,3,-7,-3,4,9,4,-5,10,-8,1,-9,1,-6,5,2,-4,-5,3,-2,-5,-4,-10,4,6,8,-9,8,8,8,4,7,4,-3,-1,5,-7,-2,6,8,-1,-9,-5,8,-1,-9,6,-4,-9,9,-3,5,-3,-8,-7,3,5,8,-1,3,3,-8,9,1,-1,7,7,4,1,1,8,-5,7,3,10,-1,-10,-3,-3,7,9,7,-6,-5,5,-4,-3,-8,-2,10,8,4,10,-7,4,-6,5,-8,-6,-7,-3,4,2,8,-2,4,10,8,-7,-5,-8,-5,-6,-6,-8,-3,-8,8,-10,1,-3,-4,3,4,-8,3,10,10,1,-10,3,-1,-2,-8,-3,8,4,-10,-5,-8,-3,-8,-1,9,-6,-2,-4,-9,-1,-1,-8,2,-1,10,9,7,-1,5,5,3,-4,-2,7,5,10,4,-4,-1], dtype = "uint64")#candidate|2826|(832,)|const|uint64
var_2827 = relay.var("var_2827", dtype = "float64", shape = (1638,))#candidate|2827|(1638,)|var|float64
call_2825 = relay.TupleGetItem(func_2577_call(relay.reshape(const_2826.astype('uint64'), [13, 4, 16]), relay.reshape(const_2826.astype('uint64'), [13, 4, 16]), relay.reshape(var_2827.astype('float64'), [1638,]), ), 2)
call_2828 = relay.TupleGetItem(func_2582_call(relay.reshape(const_2826.astype('uint64'), [13, 4, 16]), relay.reshape(const_2826.astype('uint64'), [13, 4, 16]), relay.reshape(var_2827.astype('float64'), [1638,]), ), 2)
bop_2831 = relay.less_equal(uop_2823.astype('bool'), relay.reshape(var_2822.astype('bool'), relay.shape_of(uop_2823))) # shape=(7, 9, 12)
output = relay.Tuple([call_2825,const_2826,var_2827,bop_2831,])
output2 = relay.Tuple([call_2828,const_2826,var_2827,bop_2831,])
func_2836 = relay.Function([var_2822,var_2827,], output)
mod['func_2836'] = func_2836
mod = relay.transform.InferType()(mod)
mutated_mod['func_2836'] = func_2836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mutated_mod.get_global_var('func_2836')
var_2838 = relay.var("var_2838", dtype = "float64", shape = (7, 9, 12))#candidate|2838|(7, 9, 12)|var|float64
var_2839 = relay.var("var_2839", dtype = "float64", shape = (1638,))#candidate|2839|(1638,)|var|float64
call_2837 = func_2836_call(var_2838,var_2839,)
output = call_2837
func_2840 = relay.Function([var_2838,var_2839,], output)
mutated_mod['func_2840'] = func_2840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1788_call = mod.get_global_var('func_1788')
func_1790_call = mutated_mod.get_global_var('func_1790')
call_2852 = relay.TupleGetItem(func_1788_call(), 0)
call_2853 = relay.TupleGetItem(func_1790_call(), 0)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_2864 = relay.TupleGetItem(func_1396_call(), 0)
call_2865 = relay.TupleGetItem(func_1397_call(), 0)
output = relay.Tuple([call_2852,call_2864,])
output2 = relay.Tuple([call_2853,call_2865,])
func_2869 = relay.Function([], output)
mod['func_2869'] = func_2869
mod = relay.transform.InferType()(mod)
mutated_mod['func_2869'] = func_2869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2869_call = mutated_mod.get_global_var('func_2869')
call_2870 = func_2869_call()
output = call_2870
func_2871 = relay.Function([], output)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_2875 = relay.TupleGetItem(func_2589_call(), 0)
call_2876 = relay.TupleGetItem(func_2590_call(), 0)
output = relay.Tuple([call_2875,])
output2 = relay.Tuple([call_2876,])
func_2879 = relay.Function([], output)
mod['func_2879'] = func_2879
mod = relay.transform.InferType()(mod)
mutated_mod['func_2879'] = func_2879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2879_call = mutated_mod.get_global_var('func_2879')
call_2880 = func_2879_call()
output = call_2880
func_2881 = relay.Function([], output)
mutated_mod['func_2881'] = func_2881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1788_call = mod.get_global_var('func_1788')
func_1790_call = mutated_mod.get_global_var('func_1790')
call_2927 = relay.TupleGetItem(func_1788_call(), 0)
call_2928 = relay.TupleGetItem(func_1790_call(), 0)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_2929 = relay.TupleGetItem(func_1608_call(), 2)
call_2930 = relay.TupleGetItem(func_1610_call(), 2)
uop_2935 = relay.cos(call_2927.astype('float32')) # shape=(4, 2, 4)
uop_2937 = relay.cos(call_2928.astype('float32')) # shape=(4, 2, 4)
output = relay.Tuple([call_2929,uop_2935,])
output2 = relay.Tuple([call_2930,uop_2937,])
func_2960 = relay.Function([], output)
mod['func_2960'] = func_2960
mod = relay.transform.InferType()(mod)
output = func_2960()
func_2961 = relay.Function([], output)
mutated_mod['func_2961'] = func_2961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_2965 = relay.TupleGetItem(func_2741_call(), 0)
call_2966 = relay.TupleGetItem(func_2742_call(), 0)
func_1229_call = mod.get_global_var('func_1229')
func_1232_call = mutated_mod.get_global_var('func_1232')
var_2969 = relay.var("var_2969", dtype = "bool", shape = (1, 448))#candidate|2969|(1, 448)|var|bool
call_2968 = func_1229_call(relay.reshape(var_2969.astype('bool'), [4, 8, 14]), relay.reshape(var_2969.astype('bool'), [4, 8, 14]), )
call_2970 = func_1229_call(relay.reshape(var_2969.astype('bool'), [4, 8, 14]), relay.reshape(var_2969.astype('bool'), [4, 8, 14]), )
bop_2971 = relay.equal(call_2968.astype('bool'), relay.reshape(var_2969.astype('bool'), relay.shape_of(call_2968))) # shape=(4, 8, 14)
bop_2974 = relay.equal(call_2970.astype('bool'), relay.reshape(var_2969.astype('bool'), relay.shape_of(call_2970))) # shape=(4, 8, 14)
output = relay.Tuple([call_2965,bop_2971,])
output2 = relay.Tuple([call_2966,bop_2974,])
func_2976 = relay.Function([var_2969,], output)
mod['func_2976'] = func_2976
mod = relay.transform.InferType()(mod)
mutated_mod['func_2976'] = func_2976
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2977 = relay.var("var_2977", dtype = "bool", shape = (1, 448))#candidate|2977|(1, 448)|var|bool
func_2976_call = mutated_mod.get_global_var('func_2976')
call_2978 = func_2976_call(var_2977)
output = call_2978
func_2979 = relay.Function([var_2977], output)
mutated_mod['func_2979'] = func_2979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2521_call = mod.get_global_var('func_2521')
func_2523_call = mutated_mod.get_global_var('func_2523')
call_2983 = relay.TupleGetItem(func_2521_call(), 0)
call_2984 = relay.TupleGetItem(func_2523_call(), 0)
output = relay.Tuple([call_2983,])
output2 = relay.Tuple([call_2984,])
func_2995 = relay.Function([], output)
mod['func_2995'] = func_2995
mod = relay.transform.InferType()(mod)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mutated_mod.get_global_var('func_2995')
call_2996 = func_2995_call()
output = call_2996
func_2997 = relay.Function([], output)
mutated_mod['func_2997'] = func_2997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_3025 = relay.TupleGetItem(func_2793_call(), 1)
call_3026 = relay.TupleGetItem(func_2794_call(), 1)
output = call_3025
output2 = call_3026
func_3040 = relay.Function([], output)
mod['func_3040'] = func_3040
mod = relay.transform.InferType()(mod)
output = func_3040()
func_3041 = relay.Function([], output)
mutated_mod['func_3041'] = func_3041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_3089 = relay.TupleGetItem(func_2030_call(), 1)
call_3090 = relay.TupleGetItem(func_2032_call(), 1)
output = call_3089
output2 = call_3090
func_3104 = relay.Function([], output)
mod['func_3104'] = func_3104
mod = relay.transform.InferType()(mod)
output = func_3104()
func_3105 = relay.Function([], output)
mutated_mod['func_3105'] = func_3105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2961_call = mutated_mod.get_global_var('func_2961')
call_3139 = relay.TupleGetItem(func_2960_call(), 0)
call_3140 = relay.TupleGetItem(func_2961_call(), 0)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_3145 = relay.TupleGetItem(func_2030_call(), 0)
call_3146 = relay.TupleGetItem(func_2032_call(), 0)
func_1788_call = mod.get_global_var('func_1788')
func_1790_call = mutated_mod.get_global_var('func_1790')
call_3172 = relay.TupleGetItem(func_1788_call(), 0)
call_3173 = relay.TupleGetItem(func_1790_call(), 0)
func_2976_call = mod.get_global_var('func_2976')
func_2979_call = mutated_mod.get_global_var('func_2979')
call_3178 = relay.TupleGetItem(func_2976_call(relay.reshape(call_3139.astype('bool'), [1, 448])), 0)
call_3179 = relay.TupleGetItem(func_2979_call(relay.reshape(call_3139.astype('bool'), [1, 448])), 0)
output = relay.Tuple([call_3139,call_3145,call_3172,call_3178,])
output2 = relay.Tuple([call_3140,call_3146,call_3173,call_3179,])
func_3180 = relay.Function([], output)
mod['func_3180'] = func_3180
mod = relay.transform.InferType()(mod)
output = func_3180()
func_3181 = relay.Function([], output)
mutated_mod['func_3181'] = func_3181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3180_call = mod.get_global_var('func_3180')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_3214 = relay.TupleGetItem(func_3180_call(), 0)
call_3215 = relay.TupleGetItem(func_3181_call(), 0)
output = call_3214
output2 = call_3215
func_3216 = relay.Function([], output)
mod['func_3216'] = func_3216
mod = relay.transform.InferType()(mod)
output = func_3216()
func_3217 = relay.Function([], output)
mutated_mod['func_3217'] = func_3217
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3262 = relay.var("var_3262", dtype = "float32", shape = (4, 15, 1))#candidate|3262|(4, 15, 1)|var|float32
uop_3263 = relay.exp(var_3262.astype('float32')) # shape=(4, 15, 1)
output = relay.Tuple([uop_3263,])
output2 = relay.Tuple([uop_3263,])
func_3267 = relay.Function([var_3262,], output)
mod['func_3267'] = func_3267
mod = relay.transform.InferType()(mod)
var_3268 = relay.var("var_3268", dtype = "float32", shape = (4, 15, 1))#candidate|3268|(4, 15, 1)|var|float32
output = func_3267(var_3268)
func_3269 = relay.Function([var_3268], output)
mutated_mod['func_3269'] = func_3269
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3287 = relay.const([[[-5,-4,-2,-2,-8,-3],[9,1,5,8,10,4],[-8,2,10,-1,-10,-4],[1,-1,5,9,10,-1],[-10,10,-5,-3,-1,-2]],[[-6,3,-1,8,-5,10],[-5,-1,-9,-1,-1,10],[-5,9,-5,-6,6,-6],[-10,-9,-5,2,10,-4],[-8,-9,-8,-7,1,1]],[[-6,8,8,-9,10,1],[8,5,9,-6,-6,7],[5,7,9,3,-4,-7],[5,-1,5,10,7,1],[3,-2,4,3,5,-5]],[[-5,-10,-9,1,3,1],[-6,-3,-4,-7,-6,8],[-2,9,-8,-10,7,3],[-6,-2,-8,9,1,7],[8,2,4,-4,-10,4]],[[9,2,3,-4,2,10],[-6,-6,-10,-4,-6,2],[8,-6,9,6,-5,6],[6,9,-3,-9,-7,-9],[5,-5,2,3,-3,8]],[[-1,2,7,-4,-7,10],[-1,2,-4,-6,4,2],[-9,8,5,4,2,-2],[3,1,-2,-9,-8,2],[1,2,9,3,-8,2]],[[7,-9,-3,10,-10,5],[2,4,6,-3,-2,-2],[7,-1,-6,-8,8,-4],[10,-6,-4,10,-6,7],[10,8,-5,5,6,8]],[[-8,7,-6,6,4,6],[-2,6,-3,-9,-5,9],[7,-1,-1,-7,5,-6],[2,9,-3,-5,-3,4],[-6,-3,9,-10,-7,9]],[[9,-8,7,-7,5,8],[1,4,6,4,-10,-4],[8,-3,-4,4,8,10],[-9,8,-3,3,-10,1],[-4,10,9,-2,8,3]],[[-8,5,-2,-5,2,-4],[-8,10,-5,-7,-4,-4],[-3,-4,-2,2,6,7],[-2,9,-4,8,2,-3],[1,-6,7,9,-4,10]],[[10,5,-9,5,5,-3],[9,-2,-1,5,-4,-8],[1,-10,2,1,2,-9],[-10,-10,10,-3,-9,1],[-1,4,9,8,-9,7]]], dtype = "uint16")#candidate|3287|(11, 5, 6)|const|uint16
var_3288 = relay.var("var_3288", dtype = "uint16", shape = (11, 5, 6))#candidate|3288|(11, 5, 6)|var|uint16
bop_3289 = relay.bitwise_or(const_3287.astype('uint16'), relay.reshape(var_3288.astype('uint16'), relay.shape_of(const_3287))) # shape=(11, 5, 6)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3294 = func_1487_call()
call_3295 = func_1487_call()
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_3304 = relay.TupleGetItem(func_2589_call(), 0)
call_3305 = relay.TupleGetItem(func_2590_call(), 0)
output = relay.Tuple([bop_3289,call_3294,call_3304,])
output2 = relay.Tuple([bop_3289,call_3295,call_3305,])
func_3311 = relay.Function([var_3288,], output)
mod['func_3311'] = func_3311
mod = relay.transform.InferType()(mod)
mutated_mod['func_3311'] = func_3311
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3312 = relay.var("var_3312", dtype = "uint16", shape = (11, 5, 6))#candidate|3312|(11, 5, 6)|var|uint16
func_3311_call = mutated_mod.get_global_var('func_3311')
call_3313 = func_3311_call(var_3312)
output = call_3313
func_3314 = relay.Function([var_3312], output)
mutated_mod['func_3314'] = func_3314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_3468 = relay.TupleGetItem(func_2741_call(), 1)
call_3469 = relay.TupleGetItem(func_2742_call(), 1)
uop_3482 = relay.asin(call_3468.astype('float64')) # shape=(4, 8, 14)
uop_3484 = relay.asin(call_3469.astype('float64')) # shape=(4, 8, 14)
func_2760_call = mod.get_global_var('func_2760')
func_2762_call = mutated_mod.get_global_var('func_2762')
call_3505 = func_2760_call()
call_3506 = func_2760_call()
uop_3525 = relay.cos(uop_3482.astype('float32')) # shape=(4, 8, 14)
uop_3527 = relay.cos(uop_3484.astype('float32')) # shape=(4, 8, 14)
output = relay.Tuple([call_3505,uop_3525,])
output2 = relay.Tuple([call_3506,uop_3527,])
func_3534 = relay.Function([], output)
mod['func_3534'] = func_3534
mod = relay.transform.InferType()(mod)
mutated_mod['func_3534'] = func_3534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mutated_mod.get_global_var('func_3534')
call_3535 = func_3534_call()
output = call_3535
func_3536 = relay.Function([], output)
mutated_mod['func_3536'] = func_3536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3558 = func_1487_call()
call_3559 = func_1487_call()
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_3561 = relay.TupleGetItem(func_1396_call(), 0)
call_3562 = relay.TupleGetItem(func_1397_call(), 0)
func_2061_call = mod.get_global_var('func_2061')
func_2064_call = mutated_mod.get_global_var('func_2064')
var_3566 = relay.var("var_3566", dtype = "int32", shape = (14,))#candidate|3566|(14,)|var|int32
call_3565 = relay.TupleGetItem(func_2061_call(relay.reshape(var_3566.astype('int32'), [1, 14])), 0)
call_3567 = relay.TupleGetItem(func_2064_call(relay.reshape(var_3566.astype('int32'), [1, 14])), 0)
bop_3574 = relay.bitwise_and(call_3561.astype('int64'), relay.reshape(call_3565.astype('int64'), relay.shape_of(call_3561))) # shape=(4, 2, 4)
bop_3577 = relay.bitwise_and(call_3562.astype('int64'), relay.reshape(call_3567.astype('int64'), relay.shape_of(call_3562))) # shape=(4, 2, 4)
output = relay.Tuple([call_3558,var_3566,bop_3574,])
output2 = relay.Tuple([call_3559,var_3566,bop_3577,])
func_3579 = relay.Function([var_3566,], output)
mod['func_3579'] = func_3579
mod = relay.transform.InferType()(mod)
mutated_mod['func_3579'] = func_3579
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3580 = relay.var("var_3580", dtype = "int32", shape = (14,))#candidate|3580|(14,)|var|int32
func_3579_call = mutated_mod.get_global_var('func_3579')
call_3581 = func_3579_call(var_3580)
output = call_3581
func_3582 = relay.Function([var_3580], output)
mutated_mod['func_3582'] = func_3582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_3594 = relay.TupleGetItem(func_3534_call(), 1)
call_3595 = relay.TupleGetItem(func_3536_call(), 1)
output = relay.Tuple([call_3594,])
output2 = relay.Tuple([call_3595,])
func_3617 = relay.Function([], output)
mod['func_3617'] = func_3617
mod = relay.transform.InferType()(mod)
output = func_3617()
func_3618 = relay.Function([], output)
mutated_mod['func_3618'] = func_3618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3676 = func_1487_call()
call_3677 = func_1487_call()
output = relay.Tuple([call_3676,])
output2 = relay.Tuple([call_3677,])
func_3680 = relay.Function([], output)
mod['func_3680'] = func_3680
mod = relay.transform.InferType()(mod)
mutated_mod['func_3680'] = func_3680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3680_call = mutated_mod.get_global_var('func_3680')
call_3681 = func_3680_call()
output = call_3681
func_3682 = relay.Function([], output)
mutated_mod['func_3682'] = func_3682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_3711 = relay.TupleGetItem(func_2589_call(), 0)
call_3712 = relay.TupleGetItem(func_2590_call(), 0)
output = relay.Tuple([call_3711,])
output2 = relay.Tuple([call_3712,])
func_3713 = relay.Function([], output)
mod['func_3713'] = func_3713
mod = relay.transform.InferType()(mod)
mutated_mod['func_3713'] = func_3713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3713_call = mutated_mod.get_global_var('func_3713')
call_3714 = func_3713_call()
output = call_3714
func_3715 = relay.Function([], output)
mutated_mod['func_3715'] = func_3715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3716 = func_1487_call()
call_3717 = func_1487_call()
output = call_3716
output2 = call_3717
func_3729 = relay.Function([], output)
mod['func_3729'] = func_3729
mod = relay.transform.InferType()(mod)
mutated_mod['func_3729'] = func_3729
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3729_call = mutated_mod.get_global_var('func_3729')
call_3730 = func_3729_call()
output = call_3730
func_3731 = relay.Function([], output)
mutated_mod['func_3731'] = func_3731
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3800 = relay.const([[[-4.284182],[-4.980266],[-8.714262],[4.928232],[0.680158]],[[0.597525],[-2.760953],[8.986473],[9.495641],[8.153276]],[[-2.717076],[-6.607318],[-1.650732],[8.787325],[-6.033957]],[[3.562399],[-7.448957],[-9.631111],[9.987602],[3.738453]],[[-2.817845],[1.617797],[4.373070],[4.066702],[0.140967]],[[-2.419394],[-9.406438],[-9.179002],[5.555939],[-6.757548]],[[8.488121],[-9.142922],[8.942471],[-7.533303],[-5.157758]],[[3.902504],[7.007563],[3.433117],[3.766003],[1.357480]],[[5.662221],[5.351139],[-6.829758],[-8.137151],[5.636107]],[[0.998250],[2.813911],[-5.541894],[-0.926303],[0.295200]],[[-5.936918],[1.767443],[-3.738961],[-7.445455],[6.882185]],[[-4.769949],[-9.446385],[-3.027305],[-4.170621],[-1.707724]]], dtype = "float32")#candidate|3800|(12, 5, 1)|const|float32
var_3801 = relay.var("var_3801", dtype = "float32", shape = (12, 5, 1))#candidate|3801|(12, 5, 1)|var|float32
bop_3802 = relay.minimum(const_3800.astype('float32'), relay.reshape(var_3801.astype('float32'), relay.shape_of(const_3800))) # shape=(12, 5, 1)
output = bop_3802
output2 = bop_3802
func_3808 = relay.Function([var_3801,], output)
mod['func_3808'] = func_3808
mod = relay.transform.InferType()(mod)
mutated_mod['func_3808'] = func_3808
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3809 = relay.var("var_3809", dtype = "float32", shape = (12, 5, 1))#candidate|3809|(12, 5, 1)|var|float32
func_3808_call = mutated_mod.get_global_var('func_3808')
call_3810 = func_3808_call(var_3809)
output = call_3810
func_3811 = relay.Function([var_3809], output)
mutated_mod['func_3811'] = func_3811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3852 = relay.var("var_3852", dtype = "int8", shape = (16, 11, 15))#candidate|3852|(16, 11, 15)|var|int8
var_3853 = relay.var("var_3853", dtype = "int8", shape = (16, 11, 15))#candidate|3853|(16, 11, 15)|var|int8
bop_3854 = relay.bitwise_xor(var_3852.astype('int8'), relay.reshape(var_3853.astype('int8'), relay.shape_of(var_3852))) # shape=(16, 11, 15)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_3859 = relay.TupleGetItem(func_2793_call(), 2)
call_3860 = relay.TupleGetItem(func_2794_call(), 2)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_3864 = relay.TupleGetItem(func_1396_call(), 0)
call_3865 = relay.TupleGetItem(func_1397_call(), 0)
bop_3870 = relay.greater_equal(var_3852.astype('bool'), relay.reshape(bop_3854.astype('bool'), relay.shape_of(var_3852))) # shape=(16, 11, 15)
output = relay.Tuple([call_3859,call_3864,bop_3870,])
output2 = relay.Tuple([call_3860,call_3865,bop_3870,])
func_3873 = relay.Function([var_3852,var_3853,], output)
mod['func_3873'] = func_3873
mod = relay.transform.InferType()(mod)
var_3874 = relay.var("var_3874", dtype = "int8", shape = (16, 11, 15))#candidate|3874|(16, 11, 15)|var|int8
var_3875 = relay.var("var_3875", dtype = "int8", shape = (16, 11, 15))#candidate|3875|(16, 11, 15)|var|int8
output = func_3873(var_3874,var_3875,)
func_3876 = relay.Function([var_3874,var_3875,], output)
mutated_mod['func_3876'] = func_3876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3887 = func_1487_call()
call_3888 = func_1487_call()
output = relay.Tuple([call_3887,])
output2 = relay.Tuple([call_3888,])
func_3921 = relay.Function([], output)
mod['func_3921'] = func_3921
mod = relay.transform.InferType()(mod)
output = func_3921()
func_3922 = relay.Function([], output)
mutated_mod['func_3922'] = func_3922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3680_call = mod.get_global_var('func_3680')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_3959 = relay.TupleGetItem(func_3680_call(), 0)
call_3960 = relay.TupleGetItem(func_3682_call(), 0)
output = relay.Tuple([call_3959,])
output2 = relay.Tuple([call_3960,])
func_3976 = relay.Function([], output)
mod['func_3976'] = func_3976
mod = relay.transform.InferType()(mod)
mutated_mod['func_3976'] = func_3976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3976_call = mutated_mod.get_global_var('func_3976')
call_3977 = func_3976_call()
output = call_3977
func_3978 = relay.Function([], output)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3729_call = mod.get_global_var('func_3729')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_3994 = func_3729_call()
call_3995 = func_3729_call()
output = relay.Tuple([call_3994,])
output2 = relay.Tuple([call_3995,])
func_4014 = relay.Function([], output)
mod['func_4014'] = func_4014
mod = relay.transform.InferType()(mod)
mutated_mod['func_4014'] = func_4014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4014_call = mutated_mod.get_global_var('func_4014')
call_4015 = func_4014_call()
output = call_4015
func_4016 = relay.Function([], output)
mutated_mod['func_4016'] = func_4016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3040_call = mod.get_global_var('func_3040')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_4031 = func_3040_call()
call_4032 = func_3040_call()
func_2879_call = mod.get_global_var('func_2879')
func_2881_call = mutated_mod.get_global_var('func_2881')
call_4040 = relay.TupleGetItem(func_2879_call(), 0)
call_4041 = relay.TupleGetItem(func_2881_call(), 0)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
const_4043 = relay.const([9.534947,6.366987,-0.382595,-1.193421,-0.395010,7.542329,0.638899,9.674763,1.350846,8.373649,8.508730,-7.668454,5.362873,-1.336014,4.047853,-6.864842,-8.713994,8.436852,-5.585141,-9.878868,9.879962,6.386244,8.415080,8.417470,-2.534282,-2.105967,0.593075,0.726001,7.929306,5.251511,-3.965262,6.823416,3.656521,-8.263276,2.823287,-1.036405,-9.453030,2.273962,-5.143931,-4.154864,-3.217554,-1.191484,9.349861,-8.529064,0.165928,5.076319,-9.191681,-2.693250], dtype = "float32")#candidate|4043|(48,)|const|float32
call_4042 = func_212_call(relay.reshape(const_4043.astype('float32'), [8, 1, 6]))
call_4044 = func_212_call(relay.reshape(const_4043.astype('float32'), [8, 1, 6]))
output = relay.Tuple([call_4031,call_4040,call_4042,const_4043,])
output2 = relay.Tuple([call_4032,call_4041,call_4044,const_4043,])
func_4046 = relay.Function([], output)
mod['func_4046'] = func_4046
mod = relay.transform.InferType()(mod)
output = func_4046()
func_4047 = relay.Function([], output)
mutated_mod['func_4047'] = func_4047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3180_call = mod.get_global_var('func_3180')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_4056 = relay.TupleGetItem(func_3180_call(), 1)
call_4057 = relay.TupleGetItem(func_3181_call(), 1)
var_4063 = relay.var("var_4063", dtype = "bool", shape = (4, 2, 4))#candidate|4063|(4, 2, 4)|var|bool
bop_4064 = relay.greater(call_4056.astype('bool'), relay.reshape(var_4063.astype('bool'), relay.shape_of(call_4056))) # shape=(4, 2, 4)
bop_4067 = relay.greater(call_4057.astype('bool'), relay.reshape(var_4063.astype('bool'), relay.shape_of(call_4057))) # shape=(4, 2, 4)
func_2960_call = mod.get_global_var('func_2960')
func_2961_call = mutated_mod.get_global_var('func_2961')
call_4069 = relay.TupleGetItem(func_2960_call(), 0)
call_4070 = relay.TupleGetItem(func_2961_call(), 0)
output = relay.Tuple([bop_4064,call_4069,])
output2 = relay.Tuple([bop_4067,call_4070,])
func_4083 = relay.Function([var_4063,], output)
mod['func_4083'] = func_4083
mod = relay.transform.InferType()(mod)
mutated_mod['func_4083'] = func_4083
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4084 = relay.var("var_4084", dtype = "bool", shape = (4, 2, 4))#candidate|4084|(4, 2, 4)|var|bool
func_4083_call = mutated_mod.get_global_var('func_4083')
call_4085 = func_4083_call(var_4084)
output = call_4085
func_4086 = relay.Function([var_4084], output)
mutated_mod['func_4086'] = func_4086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3921_call = mod.get_global_var('func_3921')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_4095 = relay.TupleGetItem(func_3921_call(), 0)
call_4096 = relay.TupleGetItem(func_3922_call(), 0)
func_483_call = mod.get_global_var('func_483')
func_486_call = mutated_mod.get_global_var('func_486')
var_4098 = relay.var("var_4098", dtype = "int32", shape = (14,))#candidate|4098|(14,)|var|int32
var_4099 = relay.var("var_4099", dtype = "int32", shape = (1, 560))#candidate|4099|(1, 560)|var|int32
call_4097 = relay.TupleGetItem(func_483_call(relay.reshape(var_4098.astype('int32'), [14, 1, 1]), relay.reshape(var_4099.astype('int32'), [14, 8, 5]), ), 2)
call_4100 = relay.TupleGetItem(func_486_call(relay.reshape(var_4098.astype('int32'), [14, 1, 1]), relay.reshape(var_4099.astype('int32'), [14, 8, 5]), ), 2)
output = relay.Tuple([call_4095,call_4097,var_4098,var_4099,])
output2 = relay.Tuple([call_4096,call_4100,var_4098,var_4099,])
func_4105 = relay.Function([var_4098,var_4099,], output)
mod['func_4105'] = func_4105
mod = relay.transform.InferType()(mod)
var_4106 = relay.var("var_4106", dtype = "int32", shape = (14,))#candidate|4106|(14,)|var|int32
var_4107 = relay.var("var_4107", dtype = "int32", shape = (1, 560))#candidate|4107|(1, 560)|var|int32
output = func_4105(var_4106,var_4107,)
func_4108 = relay.Function([var_4106,var_4107,], output)
mutated_mod['func_4108'] = func_4108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3713_call = mod.get_global_var('func_3713')
func_3715_call = mutated_mod.get_global_var('func_3715')
call_4146 = relay.TupleGetItem(func_3713_call(), 0)
call_4147 = relay.TupleGetItem(func_3715_call(), 0)
output = relay.Tuple([call_4146,])
output2 = relay.Tuple([call_4147,])
func_4174 = relay.Function([], output)
mod['func_4174'] = func_4174
mod = relay.transform.InferType()(mod)
output = func_4174()
func_4175 = relay.Function([], output)
mutated_mod['func_4175'] = func_4175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2961_call = mutated_mod.get_global_var('func_2961')
call_4178 = relay.TupleGetItem(func_2960_call(), 1)
call_4179 = relay.TupleGetItem(func_2961_call(), 1)
func_2335_call = mod.get_global_var('func_2335')
func_2339_call = mutated_mod.get_global_var('func_2339')
const_4182 = relay.const([0.911468,5.916730,-6.575702,7.750099,8.770561,5.897979,6.242968,2.980775,-1.386419,-0.883238,4.954426,8.963347,-7.448931,0.007844,-3.449800,-8.109056,1.680523,1.119425,-3.341712,3.887535,1.322238,8.625737,5.073920,0.378617,3.544560,9.378736,-8.847850,-1.973260,0.741257,-9.115433,-4.211024,6.832201,-8.769654,1.157091,1.347831,-1.780985,-6.209625,-6.858994,-2.725890,4.745003,9.459856,5.423214,-8.538489,-0.891798,5.575026,6.622858,-9.147127,-1.911532,4.987023,0.489546,-1.851729,4.694923,7.538033,-1.134347,6.734664,0.988311,-1.755261,-7.504219,3.883281,-1.986563,0.726543,-4.285837,-5.099873,5.796387,2.612274,1.315127,-3.389825,-4.494674,-2.286960,-1.102698,-7.422691,-0.052722,-5.814217,2.360362,-8.917565,-4.430103,-3.192117,2.718202,1.943070,-8.539984,2.509568,-8.378538,9.655266,3.653818,4.987510,9.854511,5.487481,1.897964,1.068001,6.217942,-5.096123,3.502395,6.411368,-0.410056,7.009830,1.616014,-6.968086,3.096482,-3.555739,1.073935,-9.237118,6.297299,-8.101942,7.526762,-0.829478,0.647608,-6.626875,1.417032,7.271800,3.946803,-4.292880,6.010941,-6.124762,-9.660824,6.373139,7.801673,9.976306,-3.851594,9.194236,2.363328,-3.918482,-0.891970,6.448984,-6.759001,4.724365,-7.664193,-1.121895,-9.814710,-1.876692,5.621471,-4.015896,0.117234,-8.884689,-5.396196,8.723566,4.657354,-4.127590,-5.182808,2.954088,1.882331,-0.596804,-5.899894,1.504737,-4.549482,-9.343474,-5.366881,-5.329173,-8.991476,7.624172,-8.303538,-4.321284,-6.465680,4.927226,-1.195061,-1.500476,-5.477766,9.712615,9.194951,6.123944,-2.567968,-4.035247,8.235599,-4.610733,1.947277,-7.527071,-8.601475,2.494865,1.088104,-9.554188,7.957616,0.520430,1.830265,-8.385292,-9.938181,-7.974589,2.819971,0.592333,7.797181,-8.979465,3.858401,-4.295522,8.953452,-6.268228,1.966805,3.908195,9.083678,-3.663899,7.691914,-7.086709,-9.684305,8.944981,3.443033,-5.580516,-6.044131,0.679678,9.023183,-9.208963,4.760132,-0.191027,5.560851,6.851081,-1.542350,9.870256,-4.536418,0.117186,8.191926,4.620581,7.460699,5.630940,-8.671588,1.745961,5.740810,3.315959,3.279396,9.682699,6.990849,9.940186,-0.636144,5.357845,-2.555129,0.179117,1.536338,-6.044566,8.036900,2.347528,-0.693365,7.943701,-4.789455,-3.581364,-2.306133,-5.522838,-2.036220,-1.216212,-9.669372,-0.056842,-4.723745,-1.858550,-3.302532,4.306994,4.170721,9.212316,2.730687,8.145663,3.441626,4.753257,5.000070,2.124855,-9.733428,-7.670821,-6.029594,3.696243,-7.238138,-2.579180,3.722192,-8.415300,-5.798461,-8.996415,6.636822,9.277888,-8.736466,-8.825292,-4.390695,3.187139,8.716737,-5.900368,-4.181114,0.323821,4.910320,0.777328,4.848594,4.032776,-9.077538,4.124223,5.720704,-1.997421,-9.974771,3.054448,3.456468,9.388242,-3.161528,-0.528742,3.303405,-7.250379,6.769390,7.625133,2.620313,3.020023,2.151656,7.575191,2.787856,-9.575283,8.674082,3.238240,-6.166739,5.006007,-9.783355,-8.413234,5.278911,-7.697501,-7.386079,4.304995,3.825293,2.673288,-1.125135,8.877845,3.417971,6.833825,-7.199385,2.260336,3.551459,0.207423,-1.901433,4.373425,-0.139787,-0.711008,-6.729559,8.775018,-6.554703,-8.387875,6.796329,5.219379,3.938108,0.186481,1.947672,-0.209832,-7.075419,-8.005695,0.744072,-0.122624,1.291920,0.384264,6.594815,7.906628,6.029621,-4.812206,-9.616646,2.401309,-0.460140,9.930531,6.059865,-5.035709,3.851668,-2.306828,-7.426065,2.934445,-5.801448,9.554161,9.488899,5.034678,-6.880957,6.717990,4.675301,-5.323005,-8.647093,1.293126,-3.164672,5.725850,-1.911485,-9.862310,-0.717702,5.063998,-9.376968,-3.694577,1.511658,5.964753,0.201876,-3.192885,6.369853,-9.369498,-0.074773,-5.692298,3.356076,7.596211,7.615842,3.526652,8.076911,-9.164000,2.444180,0.463453,5.162037,3.977451,2.675302,3.574347,-1.815299,-9.229128,-0.272020,6.702381,-8.754229,6.540728,9.523307,-0.614134,7.685311,-5.098046,5.756960,-3.841400,-8.496789,-9.284871,5.484721,6.646831,1.544379,9.189185,-0.427460,-9.493361,7.335986,-1.608389,-4.887265,0.684644,-9.288354,-6.745117,2.687173,-1.202114,-1.525602,4.840321,-5.733861,-4.589996,0.690990,2.039274,-0.554662,-9.551079,-8.652096,-1.989130,0.259690,-1.515037,-8.514214,-6.757345,7.897298,2.837175,5.761357,-0.098580,9.955386,5.428291,-2.682513,-9.484425,-3.385905,-8.171702,-2.312434,7.114318,-0.417438,1.812131,4.814173,-6.401798,-5.441824,-4.487392,-3.522599,4.749623,6.284307,-2.693952,-5.025002,9.486493,-1.591740,8.083148,-9.661353,-6.673382,-4.337308,7.855184,1.389679,8.570622,-7.896194,5.424553,-6.508069,-8.854716,-1.738800,6.965639,-6.467697,0.983920,-3.847922,3.163282,-2.692421,9.220659,4.837844,-0.257775,-0.968735,-3.184625,1.526107,6.464848,-4.349125,-1.636402,8.859203,0.368341,-4.713150,-3.359252,4.397785,8.580652,3.823136,8.002261,-8.393960,-4.383917,0.374496,5.756717,-1.404718,-7.222097,-3.557841,6.913311,-9.271969,4.678937,-5.394717,6.145609,8.751653,9.038379,6.637596,5.990800,-6.140271,-6.937034,-0.225217,-1.849902,-6.209864,-4.600146,1.666190,-6.995546,-8.319550,-3.292734,7.316487,4.312186,6.323954,-0.766177,2.129307,-1.905067,7.244727,7.267171,-3.721904,-2.826940,-0.213805,4.080371,0.701298,0.300473,-4.260231,-2.863138,4.993633,-6.631095,-0.014597,0.073932,3.702246,1.973457,-2.715251,-1.970205,-4.916752,6.056273,4.293168,9.042570,7.653020,2.181852,-8.352200,0.947929,2.251263,-9.847036,-4.806704,2.645680,8.973746,-0.864472,8.295013,-9.264111,-5.232775,-5.176815,5.208717,-8.906576,-0.503599,-1.550955,0.473819,-3.898523,0.473510], dtype = "float32")#candidate|4182|(560,)|const|float32
call_4181 = relay.TupleGetItem(func_2335_call(relay.reshape(const_4182.astype('float32'), [8, 70]), relay.reshape(const_4182.astype('float64'), [8, 70]), ), 7)
call_4183 = relay.TupleGetItem(func_2339_call(relay.reshape(const_4182.astype('float32'), [8, 70]), relay.reshape(const_4182.astype('float64'), [8, 70]), ), 7)
func_3729_call = mod.get_global_var('func_3729')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_4188 = func_3729_call()
call_4189 = func_3729_call()
output = relay.Tuple([call_4178,call_4181,const_4182,call_4188,])
output2 = relay.Tuple([call_4179,call_4183,const_4182,call_4189,])
func_4190 = relay.Function([], output)
mod['func_4190'] = func_4190
mod = relay.transform.InferType()(mod)
output = func_4190()
func_4191 = relay.Function([], output)
mutated_mod['func_4191'] = func_4191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3680_call = mod.get_global_var('func_3680')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_4216 = relay.TupleGetItem(func_3680_call(), 0)
call_4217 = relay.TupleGetItem(func_3682_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
const_4232 = relay.const([3.865502,3.009241,-9.997732,-2.425782,-6.091758,6.068082,-5.806496,-0.431559,-6.545067,2.741987,-8.730139,-0.854673,8.896065,0.938685,3.170721,2.633946,1.666117,-6.871876,8.798654,6.564116,1.612939,5.990892,-4.042080,-4.562048,-4.934892,-0.073546,2.364058,-6.194907,-8.934825,-9.293508,6.465114,-3.140311,-8.008967,-0.023107,-7.948093,-5.906470,-4.028425,4.541390,8.525459,3.367906,3.627910,-5.105768,-0.510479,-3.412927,-2.929875,3.099586,-5.328276,-7.820944,-3.575208,3.993836,-8.554003,-4.830739,9.901469,9.611976,1.407362,-0.445446,3.403664,-1.281299,0.183413,-5.368683,3.486886,3.463337,4.892688,-9.497240,-4.813690,-7.645085,2.423413,6.024156,-9.617314,-9.405572,-9.992575,6.863986,3.770707,0.554739,-9.500024,1.054155,5.456359,5.543004,-9.839178,-1.611393,2.207653,-3.434825,5.902172,7.124370,-3.750351,-0.627606,6.065659,-7.855052,3.042948,8.784298,2.340462,2.852217,-3.935977,-7.334355,-4.629315,3.475979,1.525303,6.866571,-9.006925,9.515362,-2.865279,9.111808,5.379008,-7.892445,0.492248,-1.814057,-4.927583,-4.329308,-4.136507,-4.242992,1.143851,1.754824,1.717567,-9.094446,4.426254,-5.497928,6.413827,1.549256,-6.529160,5.691903,-9.397850,-9.612485,0.812251,8.351026,5.151307,-6.324324,9.869232,-3.232524,-0.614406,-8.321802,-9.906377,6.755587,-1.067591,-8.857500,7.414107,9.028484,4.934980,-5.430812,-2.059140,-9.283822,1.529228,-7.736878,-5.708528,5.441451,6.435725,1.714909,3.868805,2.618609,8.903575,-1.093945,6.918496,-4.191344,7.734241,6.334025,-4.370843,-5.068095,3.352358,0.146928,6.313598,-4.187380,-1.746624,-6.232744,5.344346,-9.364247,5.295928,9.804580,-0.308920,0.821468,-3.570301,9.346205,-8.568014,0.574150,-5.587507,-1.076069,5.979124,2.198332,-1.510433,7.714517,1.109880,-0.861059,-6.126388,-9.518808,-4.909369,4.555805,-6.213630,9.668045,-3.377107,-0.234828,9.189539,-8.203389,-0.979392,0.218333,5.017439,-8.602907,-5.821243,0.264586,-2.537795,5.173293,8.224137,9.769235,4.149279,-2.205220,1.328488,-7.843221,7.998275,-2.037600,-3.736658,-6.076247,-4.929044,8.113030,-5.227830,-6.359891,-4.392479,5.852039,-7.195000,0.174857,1.273341,4.524638,0.610862,-5.030951,-3.227854,-2.910736,-5.485156,-8.297556,2.556564,3.739037,-5.681036,-5.215393,5.733987,-9.483208,-3.125437,5.237853,6.376454,1.025503,-4.711829,-0.898839,-4.876383,-7.095340,7.932783,0.544424,-4.743267,-3.148145,-9.290935,9.767473,-6.360131,1.124610,2.250600,1.162346,2.356144,5.813737,-5.112227,-6.864854,-6.717320,5.483099,6.254835,-5.290268,6.934100,-0.456950,9.332855,0.012998,3.705856,5.188961,6.992078,-9.597053,9.614867,-1.336680,2.019093,-5.272135,9.589721,8.473221,-3.264931,-5.257576,2.793878,-3.620381,-6.026024,-0.751851,-6.604333,6.006289,-6.988888,4.668945,6.327365,6.260126,-9.845300,4.017879,1.424620,5.663292,-7.709216,2.907277,-2.131817,4.536470,3.041343,8.199707,4.768714,3.263343,-2.567286,4.102579,3.216086,-8.690392,-0.968535,3.640517,-5.394958,3.593208,4.909328,-2.368244,-6.931199,-0.732992,-5.413452,-5.377984,-3.808150,0.439231,-3.169956,1.282632,-8.209797,5.246296,4.884620,-9.916480,6.131562,-2.657908,9.486097,7.985766,-1.223599,7.367061,7.781804,-2.133172,-1.948470,-4.148113,-7.765853,-3.420492,9.634064,9.779430,-2.486440,-7.127990,-6.278322,-5.141318,-5.856044,5.857299,-0.193166,9.358272,-4.302120,9.903450,5.467338,1.936190,1.511438,-6.558078,-3.370919,9.978404,-3.835882,-2.692235,1.152884,-1.796594,-5.153156,-5.247225,-3.440425,-9.895932,-7.269134,5.195472,5.915182,6.269784,-0.741783,2.082649,-0.787442,-4.365211,6.577888,8.709588,8.999697,-1.207682,7.825865,-9.708994,-2.752894,0.013450,8.302804,-4.713184,7.047311,6.196179,-2.025413,-1.529698,-3.567651,9.222495,-4.010488,-5.646640,-7.579791,8.939859,9.850392,3.813298,3.703630,-3.370049,-9.241140,5.357378,2.412228,2.493055,-1.945441,-7.798644,-1.595499,-7.511504,-5.794809,4.118057,3.071072,-1.592527,-1.964431,-1.789823,-6.424811,-4.185264,7.883532,4.047280,8.294034,-0.701815,-8.750495,-6.127654,-6.524919,2.099402,7.997294,7.902567,-2.397870,9.774096,-9.089073,-5.020982,3.157795,6.418587,-6.796536,7.827178,5.455285,0.473123,-4.835483,7.570071,-6.076913,7.981536,1.736151,-7.233011,-7.497123,-7.077318,1.823502,-2.440454,-8.748721,-8.201758,-7.135152,-1.006315,6.359567,1.358855,9.577410,1.399212,-1.157753,1.998855,8.480116,9.293198,4.905833,-3.650747,-3.757806,7.128711,-5.500418,2.355437,4.046778,1.127600,-9.880726,-4.526694,1.406724,9.848316,-9.535590,5.313701,3.311357,-0.640483,-8.294262,9.967546,3.932327,6.548917,-0.075450,-5.075993,-6.001073,1.469745,-7.477982,-5.205702,8.832324,5.580799,-4.133518,4.115456,4.209115,2.898280,4.885318,-8.011025,6.123575,-7.487215,2.426107,-2.655549,-0.020606,-0.310960,1.426920,-0.801119,-8.081839,9.822092,-7.974908,-6.111869,-6.678350,-4.682012,5.562214,-4.960856,-0.428738,-4.168987,4.955392,-7.576665,-4.107915,-9.614267,6.778870,-5.650704,8.533584,3.169713,0.264800,6.906464,6.618139,7.407489,2.344757,0.517931,-8.665919,7.879576,-9.157393,-4.195607,-7.778429,8.743708,9.144612,0.380966,0.197981,2.346861,4.239285,-7.361431,-1.376145,1.520659,8.868372,9.323712,-0.024241,6.942383,-1.306396,-1.026731,-4.572307,6.799061,9.609803,-9.121418,3.338446,6.119233,0.927963,2.131924,2.703572,6.167242,1.079596,2.464541,2.056909,0.226069,-7.633898,-3.762365,2.055132,-2.481832,-4.686406,1.151949,-6.283764,-1.092011,-6.609567,5.990688,-7.075971,-7.884752,-3.122817,-0.092139,-6.614827,8.276089,4.363353,4.976191,7.084817,9.265413,8.621086,1.658677,-9.470970,1.440896,8.926125,-6.896517,0.412285,-2.006140,-9.560923,9.349698,-3.369519,4.519811,-6.549799,-0.239946,0.190234,0.112732,-3.431943,-9.525844,1.005834,4.263002,0.390365,-0.979521,-3.504336,-3.647468,4.901452,7.505020,-8.989964,6.580852,2.823644,1.260204,-1.025552,7.662597,5.805114,6.982142,6.744433,-2.668875,-2.444132,2.518597,6.774427,-4.945045,8.966615,-1.361737,-3.447373,-1.361325,6.658122,-0.455719,9.381429,-6.952881,-0.640336,9.248968,-4.210452,-2.619891,-4.945239,9.587896,9.894337,3.288320,7.648775,-5.257172,3.505765,0.500462,-2.708511,-0.831944,-8.822548,9.467250,-5.107204,-2.126933,-7.988903,-8.078474,0.850512,-0.091197,2.419360,9.926205,9.037233,-9.967546,7.568906,9.674626,-5.702040,9.693814,-6.190721,2.500055,4.360657,9.824397,-4.689584,-7.995753,3.238218,-0.171305,-4.781011,0.840461,5.924886,2.885240,7.589220,6.342443,-1.389653,-5.132038,5.595850,-1.533418,-1.034300,-0.644724,6.123283,-8.628764,5.561650,4.781028,-4.536046,1.553936,-2.964863,-7.079372,9.268852,0.853016,-5.786691,-4.617405,4.020503,-5.988239,-6.209190,-9.682249,-4.055961,-2.633806,6.417918,0.769702,-3.907278,-6.053302,1.957884,-4.026870,-0.872975,8.507207,-7.212289,-5.207619,-0.626624,0.855501,7.599160,-1.266499,-7.127461,0.979622,-2.687817,9.161539,5.533990,8.374070,2.241435,6.264412,-8.091428,-8.313523,-0.715099,-4.116557,-2.958230,9.404374,-5.070510,5.401059,-4.034701,-1.267463,8.515403,4.364268,8.358762,-2.230369,-7.928756,-1.623662,-9.806644,0.220129,7.926444,8.460955,2.083320,7.279605,-2.254204,-4.690590,3.326817,5.684422,8.303884,9.779922,6.544939,4.865003,1.602223,-4.965425,-1.767545,-5.633838,-1.923668,5.206811,-4.356589,4.286308,9.356089,8.454720,-9.954849,-5.524321,8.838065,0.478948,4.631634,1.397507,-7.534969,-5.957074,6.367321,3.797128,-4.537113,-1.441165,5.731478,9.079457,5.791299,-7.945203,5.563896,6.834010,-0.643856,3.676352,8.943666,7.849182,3.118354,7.292463,-0.665934,-5.036728,2.800336,-3.042785,-0.822148,-9.262076,-4.287757,5.407999,2.735597,1.953666,0.108271,6.912928,8.095017,9.014351,-9.278538,3.938892,0.572763,6.271123,-4.609726,4.238326,1.042179,2.816331,-9.612838,2.089963,1.338381,-5.133968,5.574306,-3.110342,-4.309017,1.481053,-3.211308,8.224055,-8.933313,-8.546234,-2.435681,4.566563,2.226679,-2.093673,-8.952386,0.317727,-5.201387,-2.644206,5.966776,-6.383014,-0.015068,-4.779164,-4.493556,-6.669142,-0.444979,-5.693045,4.834835,-8.913051,-0.641317,-1.243809,-6.191561,-8.022189,0.862686,5.390242,4.022989,-0.138361,3.077369,-6.509813,0.378166,4.859821,-7.845853,-2.472070,0.820161,-3.796110,6.803992,-5.690788,8.457039,-4.117736,-3.204570,8.402131,0.035125,9.390297,4.150753,6.985843,5.983083,-0.047308,-9.386751,9.211134,-2.203891,7.355334,-7.165824,9.165322,-1.634961,2.848891,5.669736,4.813705,-1.235647,-8.914875,-7.196810,-1.446876,-3.881060,3.167267,-8.339544,-2.383758,6.349801,-3.536160,-8.020958,3.072508,-7.627092,5.344540,4.645215,-1.140597,2.669860,6.667406,-4.818873,2.123935,2.318572,2.992582,8.297745,-2.536831,5.237925,5.516283,-5.746484,8.538557,8.422115,0.772044,0.082925,-6.381306,-1.966920,-9.002046,-5.865530,5.975711,2.948691,2.256175,-0.617340,2.701788,-3.360123,0.548179,3.166537,3.442534,6.120391,6.067886,3.903040,-2.019477,-2.017867,-6.658595,-6.982357,-6.918249,3.515363,3.251898,8.912849,4.892192,2.619646,-3.727401,1.512839,4.128413,-1.578974,2.330925,-6.723691,8.528236,3.215075,9.265218,6.416225,7.561155,8.644033,8.205443,2.526878,3.711654,2.622303,0.578506,8.267951,-5.417134,7.863172,4.167004,8.894651,-6.993602,8.978780,-6.582471,4.850317,4.947834,-2.061956,9.153914,1.790187,-1.530095,7.325632,-7.140114,-3.165131,-7.571890,-6.567751,-7.326042,6.788811,-3.886247,-2.757535,5.520654,-2.528276,6.575567,8.607112,-6.751419,1.572564,-2.899987,-4.674046,5.643839,3.035866,0.884399,-8.197591,4.312674,-5.758511,-4.358242,-6.437125,6.319189,-7.236865,-1.688338,2.281647,-3.541343,8.760151,1.988248,3.628697,2.737555,2.671162,5.609003,-7.255052,8.122362,-9.405216,9.141439,7.937158,-7.601676,7.486904,-0.300233,7.218384,4.332212,6.950864,3.301485,-8.167257,8.895530,8.891479,7.726081,0.882146,-1.438432,-1.064485,-5.810629,-6.875664,6.179862,5.526961,9.988126,-7.208646,-2.881957,0.440964,8.359803,-8.744830,0.255271,1.829345,8.000839,9.082293,-2.458630,1.304784,-1.062823,7.699107,-8.012658,9.853817,-7.220287,-0.285000,0.825504,-0.952221,9.834514,0.822949,-2.916515,1.870784,2.314135,2.932027,-7.358736,-1.142176,5.694329,-1.178916,8.179427,1.059669,-4.822635,-3.430085,5.423980,-1.517907,3.283472,-5.433111,-7.110364,5.498950,-4.961058,7.734407,5.155734,4.956523,-5.907701,-7.422148,1.125939,9.539251,-9.536457,0.224435,-3.796207,-5.708925,2.057822,3.336931,6.318592,6.002973,1.128195,-8.797305,3.896296,1.893121,-4.817632,0.807420,2.276328,1.798954,-9.829177,-4.232690,-3.641910,-4.108174,3.511737,7.998058,-1.031397,-0.737653,4.244891,-5.487249,3.311528,-3.168903,-5.349519,4.112893,-8.700674,4.979546,-8.156518,8.199526,-6.654633,-0.845617,2.844002,-3.159479,2.380842,-9.083277,-8.323508,0.763091,-5.930891,9.513032,9.946613,8.237551,1.043737,-7.803490,-6.871376,-3.025940,7.654068,-7.577064,-9.564207,-2.157454,2.480233,-0.645673,3.205394,7.647955,-1.986958,-9.204286,-2.665268,5.395937,-2.219528,1.061779,-1.701203,-3.776756,-9.958575,-0.805749,5.961711,-4.290403,4.895211,-7.567915,-0.638588,4.783064,-9.919461,-4.378127,1.026521,-2.469839,4.999478,-4.223550,6.813739,6.501776,5.529218,-7.962820,-2.647054,9.711446,-0.906340,7.877610,-7.916510,9.245066,-0.199834,4.590014,8.827267,-7.704515,9.415261,-9.683158,8.121175,-5.592897,-7.939282,0.188856,-0.457516,-5.616042,6.274404,9.696149,-3.451597,-3.059411,7.795261,-7.563684,-5.170973,9.058205,9.323403,-6.224094,-6.060106,3.602025,-9.252568,4.250949,-9.093766,6.566960,2.144893,3.823134,4.141159,6.869675,1.111732,1.752229,-5.254814,3.133298,7.105420,-5.913089,-8.930937,-4.924870,-5.853015,6.950304,6.884194,-8.542294,-0.936419,8.441947,-0.240714,-4.168154,-2.015328,4.285446,-8.826843,9.127449,-4.246385,4.119214,1.866892,2.859718,-4.691923,-4.237428,4.205132,-4.506427,-2.032984,7.229784,-7.706178,-8.292508,-0.938257,1.351719,-4.544550,-1.706815,-9.961791,-1.479307,3.172318,-5.666885,-0.979122,5.003287,3.321337,3.899693,3.894151,-8.340650,-6.205707,1.876061,-0.205233,-8.669222,9.238053,-9.474396,-8.650644,7.501603,-8.803616,1.433603,6.127015,4.344783,7.258993,-9.199034,1.739345,-7.542424,-7.780355,-6.549134,4.164585,5.735845,8.182527,-9.850063,-5.396780,5.209187,2.759788,-9.013864,-5.088104,-2.729102,-9.185542,-3.114761,8.043272,-2.381712,-5.430186,4.939841,9.148572,-1.812856,-6.434177,-8.561382,0.208622,1.493746,4.628344,5.976856,8.475472,2.006480,-4.692564,-7.418905,-9.366601,4.806118,6.872297,-1.534024,-1.772108,-3.136531,-2.017365,1.478924,-0.873740,-0.628650,-7.122761,8.746821,5.923217,-1.489553,0.243137,-4.960064,8.312295,-7.094534,-6.410293,1.525832,-5.414389,0.941086,-9.767140,-1.904594,2.337948,-3.768098,-7.292825,-4.564323,-9.323459,0.254658,9.095418,-5.797381,-5.507946,5.301717,4.884109,1.045120,-9.681758,-6.841112,0.631559,-9.502604,-9.415091,9.022465,-2.572897,-9.923007,-0.258554,-4.194159,7.471902,-8.251619,-0.449855,-5.374141,-3.993609,2.123227,-7.981387,1.022361,-5.407325,9.802644,6.032691,0.855654,-8.734435,-1.733533,3.334334,-7.614282,7.731411,-2.588776,-7.364521,-9.634209,-2.189600,-3.694988,1.058234,3.858947,9.597524,-4.786317,5.182317,-1.528916,-7.925071,-6.283109,-1.341108,-1.521920,0.937868,6.432891,-0.864514,-4.596387,0.031548,2.739157,-3.404295,-1.169582,4.242770,-7.765751,-6.812990,-6.370488,-3.033526,-3.994530,4.669187,-0.981001,-8.390715,7.248822,6.617883,3.155994,-4.272581,-6.468507,5.682917,-0.865887,0.246539,3.586713,2.993634,-6.911095,-9.227346,-3.343695,-3.895488,-9.611869,-1.357358,8.472523,6.385837,-5.789376,0.657819,6.811859,5.036645,-0.577696,-4.024058,-1.627791,7.371507,2.470090,-1.206274,-6.974901,4.129111,2.924656,-1.574573,8.008282,8.759844,0.584780,-7.625866,-0.014611,-7.761735,2.841397,-4.914504,-9.739179,-1.522712,-0.765109,-7.189436,5.282765,6.169952,8.601237,3.063324,-2.187496,8.950787,-9.815386,-0.796080,1.746975,2.777969,1.356145,2.546875,8.274048,-8.894730,-6.014211,-0.035094,-0.695232,-0.695131,1.637057,-8.940671,-8.418105,9.805893,-8.269321,6.495047,-4.397816,-4.172192,5.307984,-2.116415,2.348441,-3.106349,9.400060,-6.897003,-4.626539,7.869136,-9.083312,0.537104,5.089772,1.206705,-5.838323,-3.592815,4.566599,9.113813,-5.310462,-8.804032,-0.239424,6.354413,7.701417,9.771610,-0.418407,-9.460241,-4.455772,8.071672,-0.849373,1.109552,-7.259163,-0.985521,-8.377266,-4.364411,6.352056,4.519421,1.339442,1.555479,-3.633976,-1.753501,2.851698,3.701258,8.005872,-0.348875,-7.501210,-5.777832,3.847453,-6.449551,-3.297501,-3.971511,2.217388,8.918093,-5.465224,-3.126335,3.803355,6.824623,3.656795,9.216740,5.204539,-4.361075,6.165833,-6.137773,8.711662,3.537712,0.085795,7.403721,0.608404,4.422731,4.400233,-4.905133,5.790144,-6.565743,-8.106067,8.506327,2.744499,9.086478,-3.751681,2.012401,8.386203,-7.903295,-8.107721,2.832866,-8.761846,8.359914,-8.971977,1.896959,3.070087,-7.159329,6.260969,2.584298,-8.193430,1.313583,9.175489,-8.175321,8.852053,6.582010,7.380925,7.792274,-8.979636,9.149865,-5.483977,-8.210368,-9.998496,-4.226694,-9.855053,-1.344512,-6.615492,2.509674,-9.478201,-3.149212,-4.158130,2.827610,8.952704,-4.349343,2.482829,-0.488182,-6.055805,5.464941,-2.582773,-3.325458,-5.843461,7.960150,-6.708561,-5.167591,-2.313991,8.379584,-9.949050,-0.453156,1.554544,1.409011,9.640310,0.720191,-2.407534,-8.864021,-8.020492,2.758306,-7.255016,6.462634,-7.744498,0.931965,0.170595,1.100341,-5.040162,3.032651,-4.771531,-1.688266,-2.914489,9.912212,8.978723,6.259689,-8.831759,-7.905134,6.946769,-8.256723,2.900701,1.511079,-9.064228,-2.145694,-1.797924,-8.145505,9.164851,-7.285503,-8.203392,-2.750636,-7.015176,7.760277,7.592830,1.817954,-4.412584,-9.856825,4.263741,-9.884257,-7.768569,-0.494534,-3.412789,-9.679647,-9.567540,1.947987,-6.724648,-9.449788,-1.627506,-9.160339,5.429560,-4.859846,3.935582,8.271665,-4.558554,-1.311228,-7.621097,-1.114947,8.017277,-0.313201,4.901976,5.832718,-5.421544,-0.856325,5.512951,-1.795895,-3.616055,-6.368026,1.875736,9.156543,7.820940,-7.154995,-8.989828,-0.932202,2.701443,1.491147,2.794005,0.818177], dtype = "float64")#candidate|4232|(1638,)|const|float64
call_4231 = relay.TupleGetItem(func_1070_call(relay.reshape(const_4232.astype('float64'), [14, 13, 9])), 0)
call_4233 = relay.TupleGetItem(func_1073_call(relay.reshape(const_4232.astype('float64'), [14, 13, 9])), 0)
func_4190_call = mod.get_global_var('func_4190')
func_4191_call = mutated_mod.get_global_var('func_4191')
call_4265 = relay.TupleGetItem(func_4190_call(), 3)
call_4266 = relay.TupleGetItem(func_4191_call(), 3)
output = relay.Tuple([call_4216,call_4231,const_4232,call_4265,])
output2 = relay.Tuple([call_4217,call_4233,const_4232,call_4266,])
func_4267 = relay.Function([], output)
mod['func_4267'] = func_4267
mod = relay.transform.InferType()(mod)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4267_call = mutated_mod.get_global_var('func_4267')
call_4268 = func_4267_call()
output = call_4268
func_4269 = relay.Function([], output)
mutated_mod['func_4269'] = func_4269
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4305 = relay.var("var_4305", dtype = "float64", shape = (8, 1, 9))#candidate|4305|(8, 1, 9)|var|float64
uop_4306 = relay.erf(var_4305.astype('float64')) # shape=(8, 1, 9)
func_2869_call = mod.get_global_var('func_2869')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_4314 = relay.TupleGetItem(func_2869_call(), 0)
call_4315 = relay.TupleGetItem(func_2871_call(), 0)
func_3267_call = mod.get_global_var('func_3267')
func_3269_call = mutated_mod.get_global_var('func_3269')
var_4330 = relay.var("var_4330", dtype = "float32", shape = (60,))#candidate|4330|(60,)|var|float32
call_4329 = relay.TupleGetItem(func_3267_call(relay.reshape(var_4330.astype('float32'), [4, 15, 1])), 0)
call_4331 = relay.TupleGetItem(func_3269_call(relay.reshape(var_4330.astype('float32'), [4, 15, 1])), 0)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
var_4351 = relay.var("var_4351", dtype = "float32", shape = (1, 48))#candidate|4351|(1, 48)|var|float32
call_4350 = func_212_call(relay.reshape(var_4351.astype('float32'), [8, 1, 6]))
call_4352 = func_212_call(relay.reshape(var_4351.astype('float32'), [8, 1, 6]))
func_3808_call = mod.get_global_var('func_3808')
func_3811_call = mutated_mod.get_global_var('func_3811')
call_4356 = func_3808_call(relay.reshape(var_4330.astype('float32'), [12, 5, 1]))
call_4357 = func_3808_call(relay.reshape(var_4330.astype('float32'), [12, 5, 1]))
output = relay.Tuple([uop_4306,call_4314,call_4329,var_4330,call_4350,var_4351,call_4356,])
output2 = relay.Tuple([uop_4306,call_4315,call_4331,var_4330,call_4352,var_4351,call_4357,])
func_4365 = relay.Function([var_4305,var_4330,var_4351,], output)
mod['func_4365'] = func_4365
mod = relay.transform.InferType()(mod)
var_4366 = relay.var("var_4366", dtype = "float64", shape = (8, 1, 9))#candidate|4366|(8, 1, 9)|var|float64
var_4367 = relay.var("var_4367", dtype = "float32", shape = (60,))#candidate|4367|(60,)|var|float32
var_4368 = relay.var("var_4368", dtype = "float32", shape = (1, 48))#candidate|4368|(1, 48)|var|float32
output = func_4365(var_4366,var_4367,var_4368,)
func_4369 = relay.Function([var_4366,var_4367,var_4368,], output)
mutated_mod['func_4369'] = func_4369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2760_call = mod.get_global_var('func_2760')
func_2762_call = mutated_mod.get_global_var('func_2762')
call_4380 = func_2760_call()
call_4381 = func_2760_call()
func_3311_call = mod.get_global_var('func_3311')
func_3314_call = mutated_mod.get_global_var('func_3314')
var_4383 = relay.var("var_4383", dtype = "uint16", shape = (330,))#candidate|4383|(330,)|var|uint16
call_4382 = relay.TupleGetItem(func_3311_call(relay.reshape(var_4383.astype('uint16'), [11, 5, 6])), 0)
call_4384 = relay.TupleGetItem(func_3314_call(relay.reshape(var_4383.astype('uint16'), [11, 5, 6])), 0)
output = relay.Tuple([call_4380,call_4382,var_4383,])
output2 = relay.Tuple([call_4381,call_4384,var_4383,])
func_4387 = relay.Function([var_4383,], output)
mod['func_4387'] = func_4387
mod = relay.transform.InferType()(mod)
var_4388 = relay.var("var_4388", dtype = "uint16", shape = (330,))#candidate|4388|(330,)|var|uint16
output = func_4387(var_4388)
func_4389 = relay.Function([var_4388], output)
mutated_mod['func_4389'] = func_4389
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4414 = relay.var("var_4414", dtype = "int8", shape = ())#candidate|4414|()|var|int8
var_4415 = relay.var("var_4415", dtype = "int8", shape = (9, 11, 13))#candidate|4415|(9, 11, 13)|var|int8
bop_4416 = relay.bitwise_or(var_4414.astype('int8'), var_4415.astype('int8')) # shape=(9, 11, 13)
output = bop_4416
output2 = bop_4416
func_4423 = relay.Function([var_4414,var_4415,], output)
mod['func_4423'] = func_4423
mod = relay.transform.InferType()(mod)
var_4424 = relay.var("var_4424", dtype = "int8", shape = ())#candidate|4424|()|var|int8
var_4425 = relay.var("var_4425", dtype = "int8", shape = (9, 11, 13))#candidate|4425|(9, 11, 13)|var|int8
output = func_4423(var_4424,var_4425,)
func_4426 = relay.Function([var_4424,var_4425,], output)
mutated_mod['func_4426'] = func_4426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_4436 = relay.TupleGetItem(func_3534_call(), 1)
call_4437 = relay.TupleGetItem(func_3536_call(), 1)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_4438 = func_1487_call()
call_4439 = func_1487_call()
output = relay.Tuple([call_4436,call_4438,])
output2 = relay.Tuple([call_4437,call_4439,])
func_4458 = relay.Function([], output)
mod['func_4458'] = func_4458
mod = relay.transform.InferType()(mod)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4458_call = mutated_mod.get_global_var('func_4458')
call_4459 = func_4458_call()
output = call_4459
func_4460 = relay.Function([], output)
mutated_mod['func_4460'] = func_4460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3617_call = mod.get_global_var('func_3617')
func_3618_call = mutated_mod.get_global_var('func_3618')
call_4489 = relay.TupleGetItem(func_3617_call(), 0)
call_4490 = relay.TupleGetItem(func_3618_call(), 0)
output = relay.Tuple([call_4489,])
output2 = relay.Tuple([call_4490,])
func_4491 = relay.Function([], output)
mod['func_4491'] = func_4491
mod = relay.transform.InferType()(mod)
output = func_4491()
func_4492 = relay.Function([], output)
mutated_mod['func_4492'] = func_4492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_4566 = relay.TupleGetItem(func_2030_call(), 0)
call_4567 = relay.TupleGetItem(func_2032_call(), 0)
output = call_4566
output2 = call_4567
func_4574 = relay.Function([], output)
mod['func_4574'] = func_4574
mod = relay.transform.InferType()(mod)
mutated_mod['func_4574'] = func_4574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mutated_mod.get_global_var('func_4574')
call_4575 = func_4574_call()
output = call_4575
func_4576 = relay.Function([], output)
mutated_mod['func_4576'] = func_4576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_4582 = relay.TupleGetItem(func_2741_call(), 2)
call_4583 = relay.TupleGetItem(func_2742_call(), 2)
output = call_4582
output2 = call_4583
func_4594 = relay.Function([], output)
mod['func_4594'] = func_4594
mod = relay.transform.InferType()(mod)
mutated_mod['func_4594'] = func_4594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4594_call = mutated_mod.get_global_var('func_4594')
call_4595 = func_4594_call()
output = call_4595
func_4596 = relay.Function([], output)
mutated_mod['func_4596'] = func_4596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3976_call = mod.get_global_var('func_3976')
func_3978_call = mutated_mod.get_global_var('func_3978')
call_4614 = relay.TupleGetItem(func_3976_call(), 0)
call_4615 = relay.TupleGetItem(func_3978_call(), 0)
func_2869_call = mod.get_global_var('func_2869')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_4632 = relay.TupleGetItem(func_2869_call(), 0)
call_4633 = relay.TupleGetItem(func_2871_call(), 0)
output = relay.Tuple([call_4614,call_4632,])
output2 = relay.Tuple([call_4615,call_4633,])
func_4643 = relay.Function([], output)
mod['func_4643'] = func_4643
mod = relay.transform.InferType()(mod)
mutated_mod['func_4643'] = func_4643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4643_call = mutated_mod.get_global_var('func_4643')
call_4644 = func_4643_call()
output = call_4644
func_4645 = relay.Function([], output)
mutated_mod['func_4645'] = func_4645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mod.get_global_var('func_4574')
func_4576_call = mutated_mod.get_global_var('func_4576')
call_4649 = func_4574_call()
call_4650 = func_4574_call()
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
const_4652 = relay.const([[0.012333,3.059284,2.043427,-1.767930,9.323010,-4.039846,-3.373369,5.678848,-9.971260,9.679896,6.587879,0.043314,6.321498,9.677390,8.364485,1.539002,3.189829,-8.254528,-3.677373,-9.524257,-2.504262,1.538497,-0.985325,-1.019736,-0.702446,8.830901,0.944294,-3.389238,8.507738,4.443909,-6.903315,0.649079,7.764687,-7.571283,-6.676174,4.848729,-0.354191,-4.528578,2.013955,0.281738,-0.607173,6.525656,-7.196902,-8.793611,3.243365,-8.030714,8.296824,9.284489,4.972704,-3.893891,-8.763765,-2.840148,-3.537495,7.737387,2.367947,6.569972,7.466680,-4.008272,-8.788699,4.176623,-9.776144,-5.056217,-0.585834,-4.423177,0.580590,6.077669,3.285650,-7.538268,-2.805764,8.604895,0.141682,0.201517,-3.001149,-6.452501,0.003422,-8.181226,7.261630,5.806894,2.756403,0.439642,-4.413676,-8.990238,-3.569643,4.446823,1.316607,-0.281581,9.594600,0.496210,5.089493,3.266476,-4.527629,-7.038536,-0.659819,5.067135,-7.084070,-4.487338,3.743533,-7.868528,-6.836070,2.947643,-8.411184,-5.565841,7.130844,6.290569,0.619004,9.902303,6.170694,3.760115,3.386971,6.014230,8.476828,-4.976027,-0.370264,-9.063434,-8.544378,-5.371396,6.408963,5.195134,6.294073,-0.814303,5.285150,-3.452417,4.318035,-0.464050,-5.265697,-6.543085,9.631825,-6.842012,8.942003,-5.997297,-6.124663,6.192357,3.188843,1.406317,2.394283,3.802829,0.974402,5.551538,9.333393,-9.210414,0.318547,3.794053,9.204583,4.336212,-4.757514,9.865674,-7.813224,2.326789,1.435731,-6.008367,-3.251332,5.643993,0.545809,-7.577669,-5.293560,-4.768782,-6.586236,-4.462043,-1.068526,-8.476812,-8.606686,6.489906,-4.609823,-7.163571,8.092269,5.515346,6.693799,-1.682868,1.912917,3.833126,1.085033,-2.698785,-9.402535,8.199364,-8.280201,8.468176,4.680139,9.532324,1.221431,3.933640,1.162757,-1.295913,0.356528,4.732326,-5.978251,-5.735533,0.772622,6.805167,-7.799259,-6.589554,-8.879551,4.101396,-4.747500,-0.580782,-1.100746,4.036864,-3.016407,-7.956683,-7.828073,-8.478954,8.857819,-5.519906,3.735163,-2.836527,-7.082238,-8.110645,-4.459912,4.874262,0.781920,1.680742,9.442525,4.629106,-7.813793,-2.732156,0.975954,2.376456,3.500082,9.185690,6.133612,-5.748121,-7.479161,8.559368,-1.113314,-6.275112,-9.336378,-7.209097,-7.591003,7.154338,3.819662,4.237009,-4.764248,7.506325,-8.855455,5.618769,-0.891807,4.483961,-0.461598,-1.493442,4.929009,-9.146401,-5.832195,-9.003439,-9.250434,7.461529,8.629359,4.151480,-7.086587,1.228222,6.445738,-8.396649,9.347972,4.588568,-5.404800,-2.906030,-8.257379,8.231253,2.205838,5.381705,6.378870,-6.206429,9.280806,2.516397,-8.984590,-1.528705,9.148635,-1.583264,-7.364517,-6.212099,1.734468,6.728101,-7.869892,-5.248934,-6.504709,0.663864,-9.385129,-6.548704,3.438427,1.630261,-7.265721,-4.335349,0.657169,-7.530526,-6.404068,-1.044404,-0.618838,6.881846,7.292048,-0.971264,8.796449,9.707500,0.878345,0.812461,7.344954,2.754799,-1.309727,7.113441,-6.299989,2.005129,3.291058,-5.528263,5.032228,-7.271571,9.800894,-2.424943,-0.383990,-7.770263,2.234768,9.140052,8.518852,5.909706,-1.175557,3.136306,-0.095830,4.187141,-2.180405,9.055245,3.291012,-7.441784,3.767523,6.271819,8.976252,8.999057,0.808091,3.016995,7.279812,-1.408011,-6.719478,-2.877779,-1.778403,-2.746010,6.713453,9.462849,5.290247,4.619012,-7.150047,-7.162021,1.930212,8.706796,-2.990301,7.381811,2.929570,0.120015,9.317002,-1.711175,6.715196,-7.627481,6.376036,0.443689,-1.313197,1.251759,4.377116,-3.348081,1.935748,5.395922,-5.323171,-6.824364,-4.488195,4.092365,0.289437,-2.741360,-7.700351,-5.701927,-4.247243,-6.610948,-7.265286,1.388002,-5.120728,-2.838921,1.961800,2.080366,-3.780179,9.303390,-5.201878,-3.229330,3.011240,-6.420564,-2.601779,1.540758,2.350386,7.878950,2.342606,3.248227,-2.348477,4.529815,-9.314413,0.730623,-2.952344,1.964324,-6.646493,7.553103,-3.954993,6.439695,-1.847721,4.892642,2.233472,3.763292,-6.989333,-8.732005,0.039932,-3.419361,-2.943338,-2.372274,5.979980,5.679537,-2.382723,6.801353,0.709217,5.160647,7.848145,5.093009,4.741639,5.049653,0.718498,-4.330981,6.006862,-2.061677,-6.574760,7.869267,3.713915,6.670927,3.613154,-4.194972,-4.081152,-1.605351,5.598661,-0.995042,-6.679205,-6.990531,1.617002,-3.505089,9.367318,-8.572496,-1.116363,3.106491,9.863155,5.406883,5.666045,2.462119,6.048599,4.651626,0.671727,7.876454,5.855813,0.764269,-1.085701,-2.063203,5.348563,5.094392,-3.800573,4.105174,-7.617900,-9.106322,-4.760077,7.198897,1.587076,-8.069729,-4.903371,-8.058950,5.623406,-0.704240,-7.369325,-9.100300,7.879518,9.435560,-7.499313,9.138329,9.464834,8.873434,8.872615,7.251416,0.210678,6.508938,7.381529,-6.706932,-9.095622,-2.767612,6.199955,-9.045342,-5.074286,-3.074242,-8.034132,5.392903,4.306839,8.030418,1.978397,4.824448,2.460038,-9.243996,-2.888980,5.917246,5.429212,2.676409,-8.921988,-2.990018,9.768726,-4.013222,-7.450581,1.154320,-6.888139,7.971721,2.070335,-3.257233,9.929773,2.541726,0.700059,-8.084803,-0.573746,5.072527,9.281220,-6.371773,-3.660133,-7.980432,-2.143334,-2.004891,8.877617,1.358927,-7.942759,0.865669,-8.061739,-5.862975,4.339417,2.363064,-8.100951,7.076173,-8.682412,5.664104,-5.170360,0.366660,8.668131,5.348592,1.184285,-1.293662,-0.730380,-5.414121,-3.158543,4.885930,6.205813,-4.910834,1.431608,-7.289079,6.353037,9.641243,4.117575,-6.298209,-2.750371,7.895097,-1.477710,-3.723525,2.910895,-5.631164,7.497875,-5.749483,-8.761072,-3.042206,-9.951445,0.880597,-7.398604,5.606318,6.224878,9.157273,6.440072,-8.390678,-1.953717,-3.623980,4.450303,6.252253,-6.033993,5.990592,-1.217757,3.322731,-5.669100,-8.667134,5.834756,0.932116,-0.250194,-1.977141,1.372641,5.184818,2.765698,-6.855927,-8.358823,6.224385,5.319163,5.979082,0.765536,-0.420461,4.471726,-2.833471,-8.430435,-1.830359,-3.394405,-7.426710,1.946700,2.263451,2.641494,5.703412,-6.948214,8.386811,3.655915,3.829028,3.750547,8.136749,9.138756,5.206556,5.810941,-1.866139,-7.034650,6.472699,-2.363551,0.200456,-4.851016,-4.051120,3.629096,-3.665079,-8.677367,9.832128,4.199726,2.173780,4.351327,-1.398648,-0.216043,-0.849313,3.063458,-7.675682,3.641964,-1.143875,-6.411233,-8.276748,-8.102958,-6.532474,-3.019027,-1.522379,-1.279225,-0.263431,-8.741274,-0.576528,9.978630,5.852246,1.518367,8.693429,7.743223,-8.509044,-5.512171,-3.020227,-0.816847,2.688699,-1.777501,-2.713143,2.356429,-9.423034,-9.140883,-2.073857,-7.741286,-0.688007,9.464544,-3.605422,6.378032,-4.094218,5.408348,-6.198326,-7.452798,-7.698717,9.514451,6.127053,-2.599945,-6.945278,6.107583,-7.238730,3.893309,0.819478,-1.477915,1.373935,-8.298467,9.126008,-7.343949,5.463614,-8.268871,-2.691267,9.940372,-1.638838,1.728607,-9.870163,-1.911441,-1.952441,6.800361,-4.131169,0.921036,-7.308290,-7.886930,7.909277,4.094064,3.850855,8.261098,-3.712836,1.898008,-2.804112,5.181017,1.703276,6.430456,8.831843,7.046856,1.054046,-3.823867,2.651856,2.832907,2.838522,1.911743,-4.217260,-8.505787,5.477106,-8.968464,5.201273,-5.192006,8.816850,-0.738648,9.575276,-6.303495,2.520505,-0.665858,8.394748,3.391693,-9.247258,2.159288,7.035685,2.997344,-0.575346,-4.456464,-3.705577,-1.609959,2.096013,-2.281521,7.348638,3.701365,6.959837,2.649156,9.810450,-5.561249,3.435720,5.385870,1.712348,-9.026465,-2.509926,3.560456,0.030465,-2.056865,3.512202,8.178669,6.285112,1.790064,-5.059497,-7.346206,2.291925,-6.342672,-7.874139,-6.759704,-9.868373,3.095323,3.598788,2.326756,9.400921,7.730190,9.394515,2.407711,3.648468,5.375522,0.461802,-8.779459,-7.282013,7.077221,-1.150252,2.553424,-6.348498,6.016959,0.563633,6.960696,-2.363892,9.905749,8.827035,-5.174843,4.117974,6.492979,0.716119,-7.706133,-7.759519,3.491633,8.902008,5.173135,9.630683,1.710047,-8.989909,7.909602,-7.146940,-0.176461,8.630369,-3.957354,-5.359894,5.607341,8.272529,-6.126867,-4.957773,-8.158512,-1.571735,2.423482,-2.996961,-4.537658,5.546661,6.095245,5.995579,-8.697853,7.788330,4.768912,-1.069271,5.056425,-0.233566,4.525356,6.136618,-5.824709,1.784062,-9.337394,5.821724,-3.497205,-4.467136,-8.098181,9.374145,2.153149,6.883656,9.463965,6.655000,-2.569086,-7.668816,-0.883978,6.158719,8.259272,3.240996,2.272701,-2.581713,6.592321,1.123274,-6.520136,-9.595545,4.326075,4.739623,4.488122,-0.710064,-9.589918,2.440550,-1.549444,-7.274665,-9.501663,3.291584,-2.656646,1.655475,7.088932,0.200126,-7.603915,8.435417,5.473726,-2.112881,9.385515,-3.674668,1.184897,1.017258,4.254021,4.682452,2.471238,5.057070,-7.990048,7.134599,3.304679,-9.624731,5.059023,-2.345444,-4.996119,6.700791,5.809390,7.937632,-7.003571,-9.111669,-7.433246,5.060581,1.931206,9.144247,3.341563,0.093476,6.052722,-7.383926,6.882413,-5.106473,9.834879,5.864811,0.237718,3.843769,9.831692,3.411276,7.744474,0.228396,9.940154,2.132537,-8.499277,-8.797699,-8.880587,-0.466544,0.488314,6.371873,-1.667339,1.818429,1.137907,7.163200,-3.480309,8.170761,8.981690,-0.342815,2.572308,-5.076209,-2.945259,-6.392751,6.357351,-8.617469,9.963183,-3.064319,4.620013,1.849921,-0.078961,6.951274,-4.178481,3.819354,-5.644695,-9.114430,0.097459,5.526319,8.985115,-5.711648,-0.679517,3.767586,-7.785665,2.961935,7.489160,-4.268711,-1.000202,6.837257,-2.518520,-0.590349,-3.281123,6.588599,7.800333,-2.678036,-0.898801,-1.238137,3.795619,-7.260996,7.930509,4.781391,-2.094175,-4.497202,-9.448080,0.245094,-7.118992,0.118761,4.930715,-6.776808,4.312676,5.785228,4.795476,-5.482642,-6.831555,-9.233674,-4.822665,-3.963889,-1.466749,2.958617,-0.345462,3.440958,6.272996,-4.954772,2.571477,8.632082,2.576920,-3.975281,-1.845772,4.175853,2.445335,-0.805390,-6.722112,2.853466,-7.680481,5.334750,7.519397,3.503644,3.618954,2.640300,0.420008,6.123766,-5.037216,3.484781,-7.731718,3.443925,5.900550,5.198362,-6.644553,-9.749692,-2.733431,-3.152525,-2.901021,-8.059927,6.076086,0.502052,-9.495505,4.491233,-0.009582,-2.045645,4.778190,0.542249,8.834651,-2.584016,6.208669,-1.648017,-9.136671,9.778124,3.590327,-4.180889,-6.870398,7.839721,-5.777688,0.471289,9.314982,3.842931,2.358372,3.946370,-9.590875,-7.251130,-1.075571,6.660328,7.652951,-7.350260,-1.019874,5.748634,-6.492408,8.937050,5.717761,7.351302,-7.801085,-8.877276,1.740808,4.164993,3.437460,6.474668,-9.323891,1.122405,-0.487827,-9.401579,-2.175242,8.176430,-5.768185,-1.772473,7.749048,7.023909,-4.694761,1.803815,0.961763,3.600271,-9.744965,2.320411,7.332666,1.775958,-5.494475,-5.133142,5.139772,3.743768,4.911454,-5.687322,1.747787,-3.408218,0.629100,-8.966607,-2.910478,9.631498,-6.670134,-6.635152,9.336819,0.605010,0.071895,6.361755,3.613177,8.152423,-1.705610,9.911408,2.311689,4.285194,3.721741,8.129328,-7.752272,4.608545,6.232402,-8.639911,5.974633,-6.796181,-9.168959,2.821739,-0.864649,-4.167972,-0.828584,2.611970,5.978258,-7.578812,-4.639630,3.565715,3.383488,8.042573,-3.262871,9.189087,-6.649916,-8.076132,2.834229,-9.635483,-6.474264,-6.484301,3.222771,-0.833574,9.673079,0.782401,5.572014,-1.406081,3.306642,1.835667,1.680905,9.999218,5.852717,-0.894427,-1.440246,-1.800055,0.005640,7.267346,-1.733464,-8.687071,0.498184,8.585292,-6.157521,1.774467,-3.471475,9.882291,3.207134,8.895212,-7.041852,-7.541289,-9.298308,-5.912880,5.476382,-4.262319,1.981163,8.506898,8.173978,0.646386,-3.592612,3.391430,-7.175796,3.812377,-6.245250,-1.777684,-1.137909,6.412206,1.821524,0.063676,0.079640,9.328932,-8.390755,0.595168,4.726966,7.904020,7.335939,-5.063944,7.618009,-0.421725,-8.095190,-1.939774,7.758113,-5.323332,6.698551,1.611250,5.998412,-2.726221,-5.164017,1.304229,-3.744469,9.743143,-4.628954,6.006391,2.653877,3.135170,-7.490916,0.333832,9.757941,9.315126,3.397603,8.255324,6.337674,-5.104025,-4.349081,9.504439,-3.555661,-8.162107,6.268334,-7.519693,8.866805,-9.086481,2.340446,6.600165,3.218012,-7.077763,-4.993093,-5.306031,4.019160,9.647090,-0.362251,-9.334195,3.302938,1.167594,4.703082,-1.180850,1.912716,-4.615359,-0.308199,2.781075,-8.174015,-9.024200,-5.193078,-7.337168,2.516321,7.900538,8.589379,-0.169939,-4.992360,7.972678,4.972944,4.071478,-0.961910,8.096462,2.754818,2.821058,-8.743374,-6.964475,-8.855177,-5.393272,-6.623102,6.704857,-7.168925,1.774491,-4.919424,-3.323564,-2.690449,-5.850760,1.705313,2.952210,4.897854,4.272025,-0.045882,-7.885753,-1.873209,-5.179817,-0.980097,-1.859955,7.739045,9.980658,-5.335887,6.099545,2.643206,-9.917025,5.205977,-1.206797,-8.414183,1.515947,9.825095,7.554739,-9.029499,6.146906,2.330088,1.838536,3.227900,-3.851972,-8.261816,-2.810122,-0.508359,6.805847,-3.523713,-2.519941,4.221143,0.190940,6.795201,-9.336363,-5.686696,-2.528487,-9.194512,-9.739048,-0.013183,1.513943,-2.783082,0.256236,-1.286286,-2.576131,-3.919075,8.071034,-8.308644,-5.429363,9.371277,-5.503062,-3.992459,-3.031750,-4.615600,-1.242592,1.120210,-7.771564,6.032986,-1.092226,-5.141049,-2.297082,6.203164,-3.763768,-6.556900,3.956727,7.220363,3.467952,-0.635004,-5.437437,-5.735571,-8.121560,1.896384,6.335185,-0.344194,-7.052199,8.729186,2.107587,7.575434,-5.063427,-0.689716,6.865668,3.696738,-3.564166,-5.328837,9.270382,3.282497,1.755039,-8.614714,-7.593738,-4.366778,4.857800,7.519650,3.839209,-4.840799,8.466253,2.676018,-2.685115,5.582923,6.870265,-1.345783,5.620906,-4.468473,-3.271226,1.015642,2.140664,1.579696,3.948490,6.725768,7.680545,4.995648,-4.015102,-8.408934,3.052570,2.044115,5.053417,1.734973,-5.206437,3.207677,-4.222316,4.555929,5.258465,-8.079159,4.573051,7.334361,9.078119,6.562651,0.159957,5.275605,-4.871213,0.576546,-9.521772,-6.761998,-7.312689,5.054141,-1.254917,-0.313770,9.870036,5.686059,-2.092277,-8.236216,3.647774,-9.703487,0.515282,7.869112,-1.689946,6.587523,-7.059403,3.697904,-9.505511,6.379274,7.777426,-2.546663,8.468919,-2.615778,-4.059158,3.709121,-9.773509,-4.586344,5.127732,3.246614,5.074129,-7.701667,-1.888040,-1.985411,-8.919638,-4.723357,-3.815840,2.371301,-0.515468,5.079301,-7.578825,-9.594039,-0.268986,-6.613220,-9.158801,-2.714496,-4.611859,8.530454,-9.542837,5.157161,-3.916251,5.535167,-4.336240,-5.276006,-8.090914,9.402881,-0.634007,2.666328,1.659146,5.962187,-7.942474,4.551807,-9.954977,6.729684,-0.450256,-0.986019,-9.729501,5.174453,-2.021376,0.294956,-2.067798,5.581181,-2.575413,5.062889,-9.894626,-2.262107,-9.766827,7.420805,-7.955941,-5.952786,-7.261332,7.798489,-9.413591,5.412318,-8.260853,4.633334,-1.257833,-1.715450,2.797301,-5.952063,-5.054186,-7.017565,-2.489770,4.434495,0.683750,4.311927,-0.331672,-9.291537,-2.983064,9.319423,4.298135,7.789267,5.895182,-2.481079,5.149896,-2.077447,0.207884,1.078382,9.996668,3.111100,-1.173875,-7.738545,4.410400,4.573843,-0.900031,9.596866,0.183870,7.293481,-5.244957,4.326277,-6.279119,6.136447,7.202087,4.267754,3.761815,1.166163,-4.007381,4.428632,-4.560868,8.610928,7.769626,-2.023407,2.413526,-9.568410,-6.010235,5.714776,8.423953,-7.441914,4.799828,8.198223,-5.007325,-1.265452,-1.927459,6.722835,-6.803033,-5.013417,7.651601,-5.852860,-2.098997,-2.979373,0.374182,-5.577120,-7.523519,7.836361,-3.554721,-6.825562,1.679472,6.521562,-0.491761,-9.729570,0.695298,9.591993,-1.973401,4.709675,-0.425557,6.456083,-6.289928,-0.439629,-5.599238,-6.732079,8.279250,-3.925835,-6.353648,-4.863538,-2.339899,3.972269,4.560873,-4.233170,1.910841,3.620016,0.417261,4.979769,-6.721539,-0.453730,0.130208,7.026395,7.467811,9.862576,-1.907618,5.925922,-9.232392,-9.357655,2.053050,7.200732,6.804967,-7.233948,1.360046,-9.074016,5.088103,9.002144,6.150947,9.377884,-1.463335,-6.542647,1.756166,6.712576,1.502332,6.841985,-5.088035,8.067605,9.699731,-7.571467,0.618637,-9.118597,0.975513,5.037600,5.181856,9.678663,3.640341,-1.598353,5.617886,-1.519389,7.573178,3.355355,5.352527,1.983185,-6.880069,5.206582,-8.743213,8.558738,5.210845,2.953982,6.118620,-7.439680,-1.973256,7.336504,-5.105872,-9.315036,-3.086857,5.140286,-9.967253,-5.652348,-0.057532,-1.251124,-3.705860,-5.690487,-5.960062,-6.024433,9.236621,-8.965774,7.439541,9.014343,-4.846001,7.115171,-4.811920]], dtype = "float64")#candidate|4652|(1, 1638)|const|float64
call_4651 = relay.TupleGetItem(func_1070_call(relay.reshape(const_4652.astype('float64'), [14, 13, 9])), 0)
call_4653 = relay.TupleGetItem(func_1073_call(relay.reshape(const_4652.astype('float64'), [14, 13, 9])), 0)
func_2793_call = mod.get_global_var('func_2793')
func_2794_call = mutated_mod.get_global_var('func_2794')
call_4656 = relay.TupleGetItem(func_2793_call(), 2)
call_4657 = relay.TupleGetItem(func_2794_call(), 2)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_4667 = relay.TupleGetItem(func_1396_call(), 0)
call_4668 = relay.TupleGetItem(func_1397_call(), 0)
bop_4671 = relay.floor_divide(call_4649.astype('float32'), relay.reshape(call_4656.astype('float32'), relay.shape_of(call_4649))) # shape=(4, 2, 4)
bop_4674 = relay.floor_divide(call_4650.astype('float32'), relay.reshape(call_4657.astype('float32'), relay.shape_of(call_4650))) # shape=(4, 2, 4)
func_4594_call = mod.get_global_var('func_4594')
func_4596_call = mutated_mod.get_global_var('func_4596')
call_4687 = func_4594_call()
call_4688 = func_4594_call()
func_2646_call = mod.get_global_var('func_2646')
func_2649_call = mutated_mod.get_global_var('func_2649')
var_4692 = relay.var("var_4692", dtype = "uint16", shape = (1, 980))#candidate|4692|(1, 980)|var|uint16
call_4691 = relay.TupleGetItem(func_2646_call(relay.reshape(var_4692.astype('uint16'), [980,]), relay.reshape(call_4651.astype('float64'), [1638,]), ), 4)
call_4693 = relay.TupleGetItem(func_2649_call(relay.reshape(var_4692.astype('uint16'), [980,]), relay.reshape(call_4651.astype('float64'), [1638,]), ), 4)
func_4174_call = mod.get_global_var('func_4174')
func_4175_call = mutated_mod.get_global_var('func_4175')
call_4709 = relay.TupleGetItem(func_4174_call(), 0)
call_4710 = relay.TupleGetItem(func_4175_call(), 0)
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_4715 = func_1487_call()
call_4716 = func_1487_call()
output = relay.Tuple([call_4651,const_4652,call_4667,bop_4671,call_4687,call_4691,var_4692,call_4709,call_4715,])
output2 = relay.Tuple([call_4653,const_4652,call_4668,bop_4674,call_4688,call_4693,var_4692,call_4710,call_4716,])
func_4721 = relay.Function([var_4692,], output)
mod['func_4721'] = func_4721
mod = relay.transform.InferType()(mod)
mutated_mod['func_4721'] = func_4721
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4722 = relay.var("var_4722", dtype = "uint16", shape = (1, 980))#candidate|4722|(1, 980)|var|uint16
func_4721_call = mutated_mod.get_global_var('func_4721')
call_4723 = func_4721_call(var_4722)
output = call_4723
func_4724 = relay.Function([var_4722], output)
mutated_mod['func_4724'] = func_4724
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4742 = relay.var("var_4742", dtype = "float64", shape = (8, 2, 6))#candidate|4742|(8, 2, 6)|var|float64
uop_4743 = relay.log(var_4742.astype('float64')) # shape=(8, 2, 6)
bop_4748 = relay.less_equal(var_4742.astype('bool'), relay.reshape(uop_4743.astype('bool'), relay.shape_of(var_4742))) # shape=(8, 2, 6)
output = bop_4748
output2 = bop_4748
func_4754 = relay.Function([var_4742,], output)
mod['func_4754'] = func_4754
mod = relay.transform.InferType()(mod)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4755 = relay.var("var_4755", dtype = "float64", shape = (8, 2, 6))#candidate|4755|(8, 2, 6)|var|float64
func_4754_call = mutated_mod.get_global_var('func_4754')
call_4756 = func_4754_call(var_4755)
output = call_4756
func_4757 = relay.Function([var_4755], output)
mutated_mod['func_4757'] = func_4757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_4769 = relay.TupleGetItem(func_2096_call(), 0)
call_4770 = relay.TupleGetItem(func_2098_call(), 0)
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
var_4794 = relay.var("var_4794", dtype = "int16", shape = (2145,))#candidate|4794|(2145,)|var|int16
const_4795 = relay.const([-10,8,-7,7,10,7,-6,1,3,10,10,-7,-9,4,-2,9,-9,-5,7,6,-1,5,7,3,9,-3,7,2,6,7,10,-9,-6,5,-6,1,3,7,1,1,-3,8,4,-7,5,-8,3,4,-4,3,2,-9,7,7,4,-7,-2,-1,5,7,-4,-5,-2,6,-9,-6,-2,-10,-1,-8,-4,-3,2,-5,2,6,-6,-2,-1,-4,7,5,-5,2,-1,10,-7,-4,-7,-3,8,4,2,2,-2,8,-8,-1,-8,-8,3,-4,1,9,-4,6,4,6,3,3,-6,-7,4,7,2,8,-1,8,-8,-9,-1,-4,6,3,10,7,7,-10,3,-2,1,10,2,-6,-5,5,-2,1,3,-7,9,10,-7,6,8,-5,-8,2,5,4,-5,-3,2,-6,7,-9,-9,-2,-7,-8,-6,5,10,-8,7,4,-3,-10,-3,1,10,-6,-6,5,7,-10,8,9,-5,4,6,-2,7,5,8,9,5,9,4,-7,-9,3,4,-7,6,-9,-1,5,-2,-5,-6,10,-10,3,5,2,-6,-1,-7,-9,2,-7,-8,-9,3,-1,-10,2,-2,-1,-6,-10,10,-5,2,1,-10,8,-1,8,-3,-6,-4,1,5,10,5,-6,-1,-3,4,8,-2,-4,3,8,-5,-9,3,2,1,9,-1,-2,-5,7,9,-7,-4,-4,5,5,6,-6,5,7,9,6,1,4,3,9,-1,-2,7,3,10,1,-3,7,6,-6,9,5,-9,10,-2,-7,7,-7,-7,-8,10,7,8,-5,-7,9,2,8,5,-7,-8,2,-4,-10,1,2,-9,9,10,-2,-5,-4,5,2,3,10,4,7,-3,2,6,7,2,3,-10,-10,-5,3,8,1,5,-3,1,10,8,10,-6,9,3,-10,6,7,6,-1,-5,8,-4,-8,4,1,-10,7,-7,3,-10,-4,-5,-8,-3,7,-3,-8,7,-4,-6,2,5,1,6,4,7,4,1,2,5,1,-4,7,-5,-10,-5,4,-4,3,-8,-7,7,6,-5,9,6,8,-9,1,5,4,6,1,4,9,3,7,-7,-7,1,-10,5,9,2,-7,-3,-6,-8,8,-5,4,-3,9,7,-10,-9,7,10,-10,-8,-9,6,10,4,-8,3,8,-6,-5,10,-1,-10,5,-4,2,1,-3,-9,-3,-10,-2,4,8,5,-10,1,-6,-10,10,-5,8,-6,-3,5,-7,-6,8,9,9,-1,10,2,2,-8,-8,7,-1,8,-5,1,-9,-1,8,-5,7,-5,10,5,-9,-6,-8,-4,3,4,-6,2,-1,-4,-4,-5,7,-9,9,-10,-7,-5,7,-3,-3,10,1,5,-4,2,-8,-10,10,1,-3,8,-5,-4,-4,5,-5,7,7,-9,-10,1,-9,2,-2,9,-4,-7,1,5,10,3,7,3,-1,-6,-3,-1,-2,4,-6,1,-1,2,10,9,9,7,-3,9,3,7,4,10,10], dtype = "int32")#candidate|4795|(560,)|const|int32
call_4793 = relay.TupleGetItem(func_533_call(relay.reshape(var_4794.astype('int16'), [13, 15, 11]), relay.reshape(var_4794.astype('int16'), [13, 15, 11]), relay.reshape(const_4795.astype('int32'), [560,]), ), 1)
call_4796 = relay.TupleGetItem(func_537_call(relay.reshape(var_4794.astype('int16'), [13, 15, 11]), relay.reshape(var_4794.astype('int16'), [13, 15, 11]), relay.reshape(const_4795.astype('int32'), [560,]), ), 1)
func_3873_call = mod.get_global_var('func_3873')
func_3876_call = mutated_mod.get_global_var('func_3876')
var_4802 = relay.var("var_4802", dtype = "int8", shape = (2640,))#candidate|4802|(2640,)|var|int8
call_4801 = relay.TupleGetItem(func_3873_call(relay.reshape(var_4802.astype('int8'), [16, 11, 15]), relay.reshape(var_4802.astype('int8'), [16, 11, 15]), ), 2)
call_4803 = relay.TupleGetItem(func_3876_call(relay.reshape(var_4802.astype('int8'), [16, 11, 15]), relay.reshape(var_4802.astype('int8'), [16, 11, 15]), ), 2)
output = relay.Tuple([call_4769,call_4793,var_4794,const_4795,call_4801,var_4802,])
output2 = relay.Tuple([call_4770,call_4796,var_4794,const_4795,call_4803,var_4802,])
func_4807 = relay.Function([var_4794,var_4802,], output)
mod['func_4807'] = func_4807
mod = relay.transform.InferType()(mod)
mutated_mod['func_4807'] = func_4807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4807_call = mutated_mod.get_global_var('func_4807')
var_4809 = relay.var("var_4809", dtype = "int16", shape = (2145,))#candidate|4809|(2145,)|var|int16
var_4810 = relay.var("var_4810", dtype = "int8", shape = (2640,))#candidate|4810|(2640,)|var|int8
call_4808 = func_4807_call(var_4809,var_4810,)
output = call_4808
func_4811 = relay.Function([var_4809,var_4810,], output)
mutated_mod['func_4811'] = func_4811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2760_call = mod.get_global_var('func_2760')
func_2762_call = mutated_mod.get_global_var('func_2762')
call_4983 = func_2760_call()
call_4984 = func_2760_call()
func_483_call = mod.get_global_var('func_483')
func_486_call = mutated_mod.get_global_var('func_486')
var_4988 = relay.var("var_4988", dtype = "int32", shape = (1, 14))#candidate|4988|(1, 14)|var|int32
const_4989 = relay.const([10,-3,2,7,4,-9,-2,-10,-7,-2,7,6,9,8,-9,-1,2,-5,-1,-10,-6,1,10,-8,-2,7,-10,-9,-2,-10,-10,9,2,-8,-8,-1,-7,-2,-6,3,3,-7,2,3,5,-6,-4,-6,-1,-3,-3,5,9,-9,10,-2,6,5,7,4,1,4,-7,4,-5,6,3,1,1,-6,-4,3,2,-7,-5,-1,-1,2,5,5,-4,1,-4,-9,2,5,8,7,-5,-8,-7,7,-4,-7,6,3,3,-7,-4,-2,-4,4,5,1,-8,-10,-8,5,7,-10,-2,-5,7,-5,-10,9,6,-7,7,-2,-9,-1,1,-8,8,3,3,6,-2,10,10,10,-5,6,9,10,-10,4,7,-2,-1,4,7,-3,2,4,5,5,-3,3,-9,-9,-3,2,4,-4,3,9,9,8,5,3,-6,-9,9,8,-6,9,-9,-1,7,9,5,-7,-10,-8,-6,5,9,-10,8,8,-6,-3,-10,-7,-10,-6,-4,3,-9,-9,2,-9,-7,-3,7,-7,10,8,-4,6,3,1,4,-3,5,-10,-5,-9,-7,7,4,9,-6,4,3,-6,-4,8,-2,-3,-3,3,-3,4,5,-6,-7,-2,3,5,-8,6,9,-9,5,8,-6,-9,5,9,-5,6,-3,7,6,3,4,-5,-5,5,-6,-9,-4,-1,4,-9,-6,-2,-5,6,4,5,-1,2,5,-6,-10,5,-7,-5,8,-9,10,5,2,-7,1,4,-4,-7,-6,2,-2,-2,-5,2,-2,2,-4,-7,10,-5,-8,4,7,-3,-8,9,-3,-1,-9,-6,3,2,4,-6,-3,-5,9,-3,3,-7,10,-1,8,-3,-4,-9,4,-4,1,3,8,5,9,4,-1,-3,9,-5,-5,-6,-7,7,6,-2,-1,1,6,9,-3,9,3,6,-5,9,-1,-10,9,2,9,4,-10,1,2,-3,-10,10,2,5,9,9,6,8,9,1,-3,-7,-10,1,8,-7,-4,-2,-3,6,-9,-1,6,-10,-9,-4,8,7,10,1,2,6,5,4,5,9,7,-8,-9,-10,3,-5,5,-8,2,3,-7,1,7,7,7,5,-6,-9,-5,-7,4,9,4,6,-7,1,10,-4,-9,-8,-9,-2,-7,-3,-3,1,10,9,-7,1,6,8,6,-2,4,-3,2,-9,-8,3,3,-9,6,-9,2,7,-2,3,-8,4,4,5,3,-9,8,-2,-8,4,-10,-8,-2,2,1,-3,10,-9,5,2,-9,10,-3,-8,5,6,4,-10,9,2,9,9,3,6,5,5,-1,3,7,-8,3,10,7,6,1,-8,-5,2,6,-5,7,4,7,3,-9,8,4,3,-9,-7,-9,3,-3,-2,-2,-7,1,7,9,3,1,-1,-1,-6,3,3,2,8,10,4,8,-10,-5,4,9,3,9,6,-10,2,-10,7,-10,7,4,-1,3,1,2,-1,5,4,-9,5,5,-5,2,-8], dtype = "int32")#candidate|4989|(560,)|const|int32
call_4987 = relay.TupleGetItem(func_483_call(relay.reshape(var_4988.astype('int32'), [14, 1, 1]), relay.reshape(const_4989.astype('int32'), [14, 8, 5]), ), 3)
call_4990 = relay.TupleGetItem(func_486_call(relay.reshape(var_4988.astype('int32'), [14, 1, 1]), relay.reshape(const_4989.astype('int32'), [14, 8, 5]), ), 3)
output = relay.Tuple([call_4983,call_4987,var_4988,const_4989,])
output2 = relay.Tuple([call_4984,call_4990,var_4988,const_4989,])
func_4993 = relay.Function([var_4988,], output)
mod['func_4993'] = func_4993
mod = relay.transform.InferType()(mod)
mutated_mod['func_4993'] = func_4993
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4994 = relay.var("var_4994", dtype = "int32", shape = (1, 14))#candidate|4994|(1, 14)|var|int32
func_4993_call = mutated_mod.get_global_var('func_4993')
call_4995 = func_4993_call(var_4994)
output = call_4995
func_4996 = relay.Function([var_4994], output)
mutated_mod['func_4996'] = func_4996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3040_call = mod.get_global_var('func_3040')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_5118 = func_3040_call()
call_5119 = func_3040_call()
output = relay.Tuple([call_5118,])
output2 = relay.Tuple([call_5119,])
func_5141 = relay.Function([], output)
mod['func_5141'] = func_5141
mod = relay.transform.InferType()(mod)
mutated_mod['func_5141'] = func_5141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5141_call = mutated_mod.get_global_var('func_5141')
call_5142 = func_5141_call()
output = call_5142
func_5143 = relay.Function([], output)
mutated_mod['func_5143'] = func_5143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4594_call = mod.get_global_var('func_4594')
func_4596_call = mutated_mod.get_global_var('func_4596')
call_5165 = func_4594_call()
call_5166 = func_4594_call()
output = relay.Tuple([call_5165,])
output2 = relay.Tuple([call_5166,])
func_5177 = relay.Function([], output)
mod['func_5177'] = func_5177
mod = relay.transform.InferType()(mod)
output = func_5177()
func_5178 = relay.Function([], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_5244 = relay.TupleGetItem(func_2030_call(), 0)
call_5245 = relay.TupleGetItem(func_2032_call(), 0)
output = call_5244
output2 = call_5245
func_5246 = relay.Function([], output)
mod['func_5246'] = func_5246
mod = relay.transform.InferType()(mod)
output = func_5246()
func_5247 = relay.Function([], output)
mutated_mod['func_5247'] = func_5247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4491_call = mod.get_global_var('func_4491')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_5250 = relay.TupleGetItem(func_4491_call(), 0)
call_5251 = relay.TupleGetItem(func_4492_call(), 0)
output = relay.Tuple([call_5250,])
output2 = relay.Tuple([call_5251,])
func_5252 = relay.Function([], output)
mod['func_5252'] = func_5252
mod = relay.transform.InferType()(mod)
mutated_mod['func_5252'] = func_5252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5252_call = mutated_mod.get_global_var('func_5252')
call_5253 = func_5252_call()
output = call_5253
func_5254 = relay.Function([], output)
mutated_mod['func_5254'] = func_5254
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5258 = relay.var("var_5258", dtype = "float32", shape = (7, 2, 2))#candidate|5258|(7, 2, 2)|var|float32
uop_5259 = relay.asin(var_5258.astype('float32')) # shape=(7, 2, 2)
uop_5267 = relay.atanh(var_5258.astype('float64')) # shape=(7, 2, 2)
bop_5273 = relay.power(uop_5267.astype('float32'), relay.reshape(uop_5259.astype('float32'), relay.shape_of(uop_5267))) # shape=(7, 2, 2)
func_4174_call = mod.get_global_var('func_4174')
func_4175_call = mutated_mod.get_global_var('func_4175')
call_5278 = relay.TupleGetItem(func_4174_call(), 0)
call_5279 = relay.TupleGetItem(func_4175_call(), 0)
output = relay.Tuple([bop_5273,call_5278,])
output2 = relay.Tuple([bop_5273,call_5279,])
func_5289 = relay.Function([var_5258,], output)
mod['func_5289'] = func_5289
mod = relay.transform.InferType()(mod)
var_5290 = relay.var("var_5290", dtype = "float32", shape = (7, 2, 2))#candidate|5290|(7, 2, 2)|var|float32
output = func_5289(var_5290)
func_5291 = relay.Function([var_5290], output)
mutated_mod['func_5291'] = func_5291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mod.get_global_var('func_4574')
func_4576_call = mutated_mod.get_global_var('func_4576')
call_5313 = func_4574_call()
call_5314 = func_4574_call()
uop_5315 = relay.asin(call_5313.astype('float32')) # shape=(4, 2, 4)
uop_5317 = relay.asin(call_5314.astype('float32')) # shape=(4, 2, 4)
func_2869_call = mod.get_global_var('func_2869')
func_2871_call = mutated_mod.get_global_var('func_2871')
call_5331 = relay.TupleGetItem(func_2869_call(), 0)
call_5332 = relay.TupleGetItem(func_2871_call(), 0)
bop_5352 = relay.subtract(uop_5315.astype('int16'), relay.reshape(call_5331.astype('int16'), relay.shape_of(uop_5315))) # shape=(4, 2, 4)
bop_5355 = relay.subtract(uop_5317.astype('int16'), relay.reshape(call_5332.astype('int16'), relay.shape_of(uop_5317))) # shape=(4, 2, 4)
func_3808_call = mod.get_global_var('func_3808')
func_3811_call = mutated_mod.get_global_var('func_3811')
var_5358 = relay.var("var_5358", dtype = "float32", shape = (60, 1))#candidate|5358|(60, 1)|var|float32
call_5357 = func_3808_call(relay.reshape(var_5358.astype('float32'), [12, 5, 1]))
call_5359 = func_3808_call(relay.reshape(var_5358.astype('float32'), [12, 5, 1]))
func_2960_call = mod.get_global_var('func_2960')
func_2961_call = mutated_mod.get_global_var('func_2961')
call_5365 = relay.TupleGetItem(func_2960_call(), 1)
call_5366 = relay.TupleGetItem(func_2961_call(), 1)
output = relay.Tuple([bop_5352,call_5357,var_5358,call_5365,])
output2 = relay.Tuple([bop_5355,call_5359,var_5358,call_5366,])
func_5368 = relay.Function([var_5358,], output)
mod['func_5368'] = func_5368
mod = relay.transform.InferType()(mod)
var_5369 = relay.var("var_5369", dtype = "float32", shape = (60, 1))#candidate|5369|(60, 1)|var|float32
output = func_5368(var_5369)
func_5370 = relay.Function([var_5369], output)
mutated_mod['func_5370'] = func_5370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4174_call = mod.get_global_var('func_4174')
func_4175_call = mutated_mod.get_global_var('func_4175')
call_5378 = relay.TupleGetItem(func_4174_call(), 0)
call_5379 = relay.TupleGetItem(func_4175_call(), 0)
output = call_5378
output2 = call_5379
func_5395 = relay.Function([], output)
mod['func_5395'] = func_5395
mod = relay.transform.InferType()(mod)
output = func_5395()
func_5396 = relay.Function([], output)
mutated_mod['func_5396'] = func_5396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_5397 = func_3216_call()
call_5398 = func_3216_call()
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_5402 = func_3216_call()
call_5403 = func_3216_call()
func_5177_call = mod.get_global_var('func_5177')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_5407 = relay.TupleGetItem(func_5177_call(), 0)
call_5408 = relay.TupleGetItem(func_5178_call(), 0)
output = relay.Tuple([call_5397,call_5402,call_5407,])
output2 = relay.Tuple([call_5398,call_5403,call_5408,])
func_5410 = relay.Function([], output)
mod['func_5410'] = func_5410
mod = relay.transform.InferType()(mod)
output = func_5410()
func_5411 = relay.Function([], output)
mutated_mod['func_5411'] = func_5411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2960_call = mod.get_global_var('func_2960')
func_2961_call = mutated_mod.get_global_var('func_2961')
call_5412 = relay.TupleGetItem(func_2960_call(), 0)
call_5413 = relay.TupleGetItem(func_2961_call(), 0)
func_1229_call = mod.get_global_var('func_1229')
func_1232_call = mutated_mod.get_global_var('func_1232')
call_5419 = func_1229_call(relay.reshape(call_5412.astype('bool'), [4, 8, 14]), relay.reshape(call_5412.astype('bool'), [4, 8, 14]), )
call_5420 = func_1229_call(relay.reshape(call_5412.astype('bool'), [4, 8, 14]), relay.reshape(call_5412.astype('bool'), [4, 8, 14]), )
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
var_5422 = relay.var("var_5422", dtype = "float64", shape = (1638,))#candidate|5422|(1638,)|var|float64
call_5421 = relay.TupleGetItem(func_1070_call(relay.reshape(var_5422.astype('float64'), [14, 13, 9])), 0)
call_5423 = relay.TupleGetItem(func_1073_call(relay.reshape(var_5422.astype('float64'), [14, 13, 9])), 0)
output = relay.Tuple([call_5412,call_5419,call_5421,var_5422,])
output2 = relay.Tuple([call_5413,call_5420,call_5423,var_5422,])
func_5429 = relay.Function([var_5422,], output)
mod['func_5429'] = func_5429
mod = relay.transform.InferType()(mod)
mutated_mod['func_5429'] = func_5429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5430 = relay.var("var_5430", dtype = "float64", shape = (1638,))#candidate|5430|(1638,)|var|float64
func_5429_call = mutated_mod.get_global_var('func_5429')
call_5431 = func_5429_call(var_5430)
output = call_5431
func_5432 = relay.Function([var_5430], output)
mutated_mod['func_5432'] = func_5432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4046_call = mod.get_global_var('func_4046')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_5453 = relay.TupleGetItem(func_4046_call(), 3)
call_5454 = relay.TupleGetItem(func_4047_call(), 3)
output = call_5453
output2 = call_5454
func_5469 = relay.Function([], output)
mod['func_5469'] = func_5469
mod = relay.transform.InferType()(mod)
mutated_mod['func_5469'] = func_5469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5469_call = mutated_mod.get_global_var('func_5469')
call_5470 = func_5469_call()
output = call_5470
func_5471 = relay.Function([], output)
mutated_mod['func_5471'] = func_5471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4267_call = mod.get_global_var('func_4267')
func_4269_call = mutated_mod.get_global_var('func_4269')
call_5492 = relay.TupleGetItem(func_4267_call(), 1)
call_5493 = relay.TupleGetItem(func_4269_call(), 1)
var_5505 = relay.var("var_5505", dtype = "float64", shape = (14, 13, 9))#candidate|5505|(14, 13, 9)|var|float64
bop_5506 = relay.mod(call_5492.astype('float64'), relay.reshape(var_5505.astype('float64'), relay.shape_of(call_5492))) # shape=(14, 13, 9)
bop_5509 = relay.mod(call_5493.astype('float64'), relay.reshape(var_5505.astype('float64'), relay.shape_of(call_5493))) # shape=(14, 13, 9)
func_4594_call = mod.get_global_var('func_4594')
func_4596_call = mutated_mod.get_global_var('func_4596')
call_5523 = func_4594_call()
call_5524 = func_4594_call()
output = relay.Tuple([bop_5506,call_5523,])
output2 = relay.Tuple([bop_5509,call_5524,])
func_5529 = relay.Function([var_5505,], output)
mod['func_5529'] = func_5529
mod = relay.transform.InferType()(mod)
var_5530 = relay.var("var_5530", dtype = "float64", shape = (14, 13, 9))#candidate|5530|(14, 13, 9)|var|float64
output = func_5529(var_5530)
func_5531 = relay.Function([var_5530], output)
mutated_mod['func_5531'] = func_5531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4046_call = mod.get_global_var('func_4046')
func_4047_call = mutated_mod.get_global_var('func_4047')
call_5560 = relay.TupleGetItem(func_4046_call(), 1)
call_5561 = relay.TupleGetItem(func_4047_call(), 1)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
const_5565 = relay.const([9.707525,9.059155,5.328355,-1.031448,-4.246304,-9.947511,8.686661,-1.184888,-8.570178,8.220065,-7.448669,3.952838,6.876693,2.674350,9.056626,-0.855780,2.984192,-5.339320,-4.787297,-5.489979,1.369682,-9.204854,4.731125,4.283954,1.714694,3.104659,0.430316,8.772026,-7.386192,6.246938,7.280334,-2.050013,4.132719,-2.382714,-3.452915,-1.695064,7.328286,-8.361539,8.466803,-1.735682,-2.835833,-8.030768,7.074478,0.067710,-5.434341,2.043772,-5.598018,6.362467,-8.797780,-9.097676,-5.017605,-5.089516,5.270792,-6.080148,-0.433873,9.694562,-1.539558,-5.091551,0.793370,9.975595,-6.689683,-5.228065,3.560753,4.349045,1.710170,-0.187049,-4.326047,8.320004,5.645999,3.306640,-1.646014,-8.554817,-7.085612,-4.935968,-0.409225,-8.105729,-6.339879,-7.193425,-5.218001,0.012344,7.480629,9.612567,-5.885177,7.792512,-1.626125,-0.741806,-2.405215,-0.946518,5.620133,-7.585902,-7.742820,1.701439,9.770317,-6.814314,5.472307,4.347665,5.562299,-4.573529,7.325021,8.847751,-4.499964,9.121100,0.794418,-8.773306,-8.568575,-9.585049,8.746809,-4.654323,7.394847,-8.214393,-7.483062,2.713270,-1.462384,-9.117414,-9.654156,2.566560,0.261582,0.895408,-1.209398,3.682628,-3.033914,-2.770587,2.559958,1.517640,1.697446,1.795388,6.112848,-7.348066,6.193585,-6.971765,-9.179367,-2.072216,-6.855020,-6.796818,9.533060,5.297974,-7.721046,4.151146,-3.273757,-6.707278,-6.188302,-9.893847,6.302653,3.519425,5.122254,-3.798452,-1.951738,6.314187,-3.798601,7.725571,7.486453,7.409549,-9.778497,-1.529251,9.249924,0.335764,-3.737250,-7.727522,-8.467933,-3.900944,0.667660,8.977074,-5.078300,-9.708236,6.272540,-7.985805,-9.582430,-6.040708,1.791137,-1.087119,8.884598,-7.953568,4.889418,7.439813,9.813972,4.971727,-7.842756,-6.216746,9.951824,2.130136,-5.165902,1.399012,-1.896303,-2.303093,-4.085554,-1.705201,-5.392226,-6.616567,1.598313,6.140462,1.070797,9.231799,2.982386,-1.727318,-6.233176,6.116884,-8.157345,-3.200319,-4.808676,-5.532835,5.168184,9.561343,9.983767,4.483140,2.197368,1.707795,2.834517,6.306971,-2.849399,1.643918,0.626884,-4.932218,0.236931,-5.142174,4.811347,5.771877,-1.774267,-0.953215,-3.862161,-2.682586,-8.170821,-6.183488,4.226605,-9.619678,-5.485658,-8.332847,8.739976,8.463440,3.042712,-5.671777,-8.874052,8.623514,-4.259015,-4.040663,6.673675,8.802191,2.537475,9.744411,7.747123,-4.656694,6.837440,1.955415,4.310513,-3.716339,8.116293,8.695964,-0.740309,-1.891722,-8.280672,2.929551,4.428949,6.451996,-0.970260,0.768364,2.831411,2.243768,7.784664,8.731827,9.871354,4.486826,-0.567726,-4.777973,-1.961423,-3.848599,-1.840839,-7.513000,-9.947668,-6.640749,4.603533,-6.818578,7.046308,4.300525,-0.679646,-2.052627,-5.889960,-2.858887,-0.614454,8.234876,4.396119,-5.613324,2.122196,-6.203717,-1.895122,5.421459,-7.152562,-2.058696,8.436647,-2.970196,-2.470169,-7.355081,2.883968,-4.431049,0.762195,-0.736934,3.404153,-5.164788,8.256302,-7.649741,5.362977,3.725189,3.244672,-7.165692,-6.216128,-3.730769,5.366818,5.277079,-0.104801,-2.567616,-2.030234,-5.081125,6.368850,-8.107821,7.244011,4.979679,-1.066649,3.149205,-7.684525,3.524587,-3.535878,-7.221316,-9.358639,-4.666061,2.245139,-1.105182,3.094721,2.566067,-5.222603,-8.716108,-7.693281,-6.284765,-6.875054,-4.361039,6.431201,1.570583,3.244314,1.550276,-2.991690,-6.586489,4.940668,6.396632,-4.705515,4.759912,-2.297636,-1.762636,5.423073,-0.322508,-8.031097,0.825192,-1.926373,-4.750947,-7.556258,1.916761,6.259149,-6.453377,-2.880054,-9.114234,-6.224626,0.387440,8.562092,9.353707,7.652163,-3.106968,-7.394670,7.899020,3.078726,-6.267802,-1.276684,-3.571153,-1.584435,-7.632468,-0.259885,2.520382,-9.122290,6.665949,-2.110351,7.711968,-9.145917,-2.289550,2.413582,9.355163,9.164287,-4.254247,7.398025,4.194274,7.993452,5.178862,-7.530271,-1.263869,2.048988,-0.579501,-4.186408,0.854592,-1.195021,2.067246,-0.963518,-0.657439,-1.986011,7.351083,4.865712,2.216996,-6.728186,-0.853910,2.210263,3.540949,-4.035545,8.083644,8.200549,-6.285064,-4.507918,7.467926,-5.627375,-0.596129,-6.950979,1.189757,-2.673454,-5.869874,6.045475,-4.921865,5.236532,9.429022,1.452669,-3.421673,-2.211503,-0.452717,-3.326694,2.890059,8.977585,-4.489761,3.449061,1.215610,-3.652817,-2.970874,-4.607103,6.153977,-6.379402,-7.978431,4.064087,4.453280,7.033605,-9.098800,6.763677,-6.177100,3.009025,0.860716,-7.345829,-8.624490,-7.902070,-7.462471,9.782105,9.901367,0.870139,-0.496361,-6.633364,-2.557527,5.043621,-7.050387,-6.555108,-8.166270,2.929889,-3.335097,-6.013616,-9.529450,4.832758,-2.659891,-5.085045,-9.728963,1.067304,-3.431513,-6.831712,8.620961,0.028414,8.107430,-7.991283,0.104451,4.787867,-0.043879,5.195844,-9.955346,0.477821,7.368553,-4.975556,7.028094,-7.911358,-5.176671,-8.677707,0.007968,8.281653,0.632445,-9.827721,6.215892,-7.248460,0.788184,-0.139271,-3.444087,-3.945151,-5.520101,-8.898028,-9.745370,2.644283,4.712039,-0.297501,-3.196345,5.885403,-1.448309,-8.714994,5.111725,7.902933,-4.656575,6.013552,1.372963,1.855837,-5.715733,-2.732583,-1.163327,8.028566,4.246656,-0.324500,8.229455,-9.148451,8.167403,9.100666,3.501384,-1.546182,6.062105,5.783015,2.709745,-0.141990,-5.323174,1.347351,-4.521994,-9.313589,-2.189011,1.578639,3.132724,3.804304,6.149880,7.689955,2.185997,-8.508326,6.369176,-8.452999,-9.747023,9.781846,2.276102,-4.294940,9.213694,5.056561,2.896565,-6.413003,-0.397273,-2.924390,-4.633408,5.283146,5.135126,-2.778092,9.413031,0.899657,2.943869,-1.478184,2.932130,9.349419,9.472146,7.308121,2.329185,8.893905,3.299948,4.865014,-2.321637,-7.575352,9.689022,-6.867919,8.801915,-9.561387,-1.436965,1.489004,3.431563,5.950079,9.236447,-5.704670,-8.313786,0.088162,3.719346,4.977418,2.513600,7.553451,7.093119,2.490527,6.073279,1.125307,-2.591742,-2.029287,9.429873,-3.896243,-7.957692,-2.576063,7.703001,-5.289240,-4.075382,-9.715813,1.869769,-3.894728,9.930224,4.920246,-6.518352,0.121059,4.599708,-7.230638,8.353532,-8.215343,5.337734,-7.311858,-8.828862,6.331911,-4.293039,-3.206774,2.934397,-8.626501,-7.616428,-1.252376,2.972269,3.361407,6.106039,2.689252,-0.468212,-1.011172,-8.617052,-5.976487,6.854949,-2.938832,3.222003,-7.916670,0.458598,-4.260058,-8.966607,-4.805156,-6.579315,9.405421,-1.557802,-2.737201,-7.806374,-3.789554,1.536473,8.727731,5.102859,-1.790032,-9.492736,6.342285,-4.102361,5.536256,-6.979287,-9.986067,2.785171,-0.234001,-4.265936,-0.928457,2.412234,-2.512918,-9.414062,-5.449254,2.077734,-7.145931,8.351000,4.161445,3.116771,-2.559281,8.980398,-6.234550,-6.846479,-5.862163,9.393467,8.950342,2.653040,3.831194,6.969723,9.919557,2.374094,-2.936135,-4.517994,-6.743085,-5.110019,2.705420,4.006763,-0.708652,2.791762,-7.820702,-0.269934,1.469263,9.899268,3.208558,-8.954333,2.050455,-5.279547,-9.668385,-6.586062,1.994012,-3.416437,-6.207457,-2.456285,5.984455,9.124606,8.714128,-3.275371,1.215614,1.566916,-6.867756,-3.490165,7.264626,-5.258352,9.162229,-9.212144,8.638528,7.018211,-3.500363,1.686176,1.060407,-2.531238,-1.885706,-5.031057,-9.861947,-8.784860,0.357191,6.377884,7.306451,0.620383,-8.748181,4.120168,-5.547686,1.467557,8.967319,-0.513911,6.618290,5.657437,0.957192,6.286530,7.631682,5.416933,-6.975364,-9.906879,-0.932197,-3.086871,4.509098,-7.254219,5.928113,1.769580,-0.742991,0.351482,-3.122292,8.977065,-2.306511,7.477536,-6.875324,7.894191,7.964619,5.535245,9.677963,-2.339271,5.123576,-9.327446,-3.276491,2.593424,8.486050,-9.398745,0.594821,-1.922278,3.968603,-7.855684,-5.127104,-8.285039,8.775523,0.881649,-4.537715,5.652269,-7.388924,-9.496885,6.627816,-8.061707,-5.193173,-9.024721,-6.537571,-9.045768,1.725007,-1.672523,-6.525287,5.792064,-6.740798,-7.341691,4.578212,-0.231607,9.386531,-8.354167,6.889259,7.280613,-3.214086,2.370149,-8.724733,-5.658753,-6.453623,7.845994,0.453998,-6.794445,8.792124,-3.328882,5.346531,9.153398,2.204214,7.980003,-3.241393,3.253151,0.059563,5.060166,-1.733880,9.968644,-2.517956,2.508597,0.650156,3.435597,-9.852908,5.108710,5.521337,-1.163301,3.147392,8.117750,-2.003762,-9.137604,2.871034,-8.282820,5.899104,7.268603,-1.079402,3.876469,-7.554741,4.200583,6.752208,-4.467657,0.763499,4.854976,8.288791,-6.002207,9.438700,9.434113,-6.137852,-2.810788,7.594764,-2.329702,-8.688045,4.441485,-3.049324,2.071083,-4.651445,-1.924540,-2.831453,-5.249762,-2.819440,-1.867164,3.194598,8.379235,4.750146,7.704397,6.489686,-3.947665,9.415789,-4.216312,-2.652496,6.680760,-2.807510,-6.307595,-2.988524,-2.996808,5.261844,-8.695866,-9.243525,8.737475,-7.693809,-3.000065,-6.028707,1.408884,-5.907907,3.543330,-9.547983,8.035813,1.726519,1.245219,-0.392783,-7.071561,-3.734768,-2.820012,-4.756148,-3.399790,-5.927084,-7.789225,-9.141106,0.549986,-0.992468,6.206616,0.812304,6.249123,4.059167,-8.266556,-5.770516,0.839234,-9.541178,7.892986,9.632575,0.453955,-3.091215,-3.590986,4.988793,9.453023,0.963864,-3.907217,-8.956804,1.426554,9.169612,4.960978,-7.932869,-6.567618,8.484405,-3.537407,-9.733672,-9.361382,7.884517,3.652008,-1.611386,-9.375600,8.942272,2.421992,-3.192361,8.648112,-2.838132,4.116479,-5.523272,9.999511,6.935965,-2.308906,2.285939,-0.989269,-3.940228,-2.161692,7.397016,-7.027427,3.373387,-4.768225,-8.203573,2.424069,-4.603278,1.510146,8.385852,-2.437509,-1.464062,-4.109586,-6.610295,7.508749,-4.048262,9.749175,-2.761724,-8.213398,2.540613,-6.847083,3.011556,0.992767,-4.025524,-3.267819,3.134129,7.724327,5.375780,-4.332147,-0.660345,-9.060689,8.704128,-6.075790,5.761820,8.838066,8.940501,-9.015738,-5.222478,1.911938,2.180244,-2.641017,-3.206796,-8.947560,5.030503,9.798900,-7.926474,-9.856950,-6.700838,-6.794989,4.847146,-8.596569,4.751871,0.441711,-9.440441,-5.902986,-3.467284,7.026038,-5.687666,3.103722,-0.115547,-4.730423,-5.566437,-7.379644,5.245642,1.586752,-2.238222,-5.603314,-4.323558,0.212387,-4.224023,-4.316644,-8.731128,4.760277,-7.830788,-2.933651,-1.087352,9.645842,8.741725,2.152255,-5.933615,-7.855875,-8.175290,-6.083989,-4.800336,-9.416292,-5.489441,-0.247272,-0.275666,6.430661,-6.325914,7.293392,-1.610654,5.517915,-2.677406,2.764069,2.526909,0.971029,-0.619159,8.371140,-8.504747,1.235412,-6.709762,2.193274,5.456013,3.924021,7.883078,-0.511702,-3.621772,6.593565,-9.200010,0.776789,-7.861455,-9.533921,8.165744,-5.642958,4.749322,-2.648111,8.897295,-8.284905,-8.713487,-9.351591,-9.011459,-2.057537,-9.408127,6.867579,-3.369061,0.145871,9.147351,0.319236,5.478768,-3.102498,1.029753,-5.957296,0.586409,1.535968,9.182371,7.540060,5.781218,-1.697361,9.239314,-2.914055,-2.205277,8.254769,3.878098,-4.901113,-9.183312,5.410561,0.689998,-1.596437,-1.116709,8.556942,0.933953,2.136794,-3.775296,-9.650185,9.158323,5.831995,-9.088871,-5.212806,5.563675,-9.961697,2.698906,9.302578,-4.255848,6.243893,4.235287,-5.840319,9.663595,4.343821,6.524737,-7.247567,1.073949,-7.398314,-6.585080,2.597049,-9.633943,2.537117,-7.796358,-0.709207,-3.714971,0.487171,-2.062776,-0.443701,-3.313365,1.794341,1.950262,-8.005574,3.875039,8.855396,2.747900,7.803999,-2.458064,-9.224874,5.833641,3.739034,-0.081046,-5.391640,-7.250141,9.745673,-3.882142,-3.392955,-6.415422,-9.916942,-3.509231,1.979644,0.628759,6.666705,8.115046,-7.872683,-9.866057,-7.057263,-5.681507,-6.479588,2.494744,5.685719,-5.634335,3.394165,8.007589,5.047150,6.068037,5.494505,5.440596,0.253270,-1.092330,-4.599536,1.376113,-7.074258,8.920968,7.921702,-8.734344,-4.047962,-7.153059,4.506133,-6.759230,5.726804,0.460669,-9.917892,8.906011,6.200618,4.381338,8.062734,-2.023128,-6.030055,-7.490754,-6.349895,3.011204,5.784494,-4.576181,8.462075,2.201395,9.394384,9.173387,-7.485654,5.195027,8.069095,2.318450,3.359848,-7.070867,3.982807,8.068328,6.367795,-2.833875,3.013866,0.258765,4.317830,0.062428,9.258158,-3.394983,-9.954787,6.953387,-9.597565,-6.343860,-8.074395,-6.688578,5.217664,3.605103,-7.783501,9.423895,-8.913129,-8.882210,-1.967509,-6.892161,-6.304318,3.899810,-0.409340,-5.057058,2.725183,0.123564,1.428915,7.147671,0.220474,0.227709,-4.643478,3.351653,1.657034,6.211362,-4.158155,5.649945,-0.142715,6.550622,2.516198,-3.853172,-0.162289,-5.591567,8.387553,-1.775884,-8.854208,-6.893430,-9.695516,-5.162027,8.934926,2.466761,6.085731,-4.268679,8.615785,1.635006,-0.058044,4.102631,5.978091,-6.203862,4.696976,1.092415,1.792495,8.941346,-3.646604,0.527660,9.004638,5.125039,-9.006962,-5.843914,3.966603,-1.750135,0.685972,-9.141081,-8.109760,6.420758,1.285186,3.563314,-5.613603,-7.306834,-0.858465,-4.280185,4.556105,0.527181,-4.564491,0.538456,8.496436,6.641555,-7.906094,3.036513,-4.245346,-1.511449,1.767735,-4.957293,-2.274614,-7.542307,6.239740,-3.401335,-2.075740,-5.462506,-1.794321,-1.498900,5.690124,-2.288039,6.684497,-6.943730,6.352163,5.552882,5.280359,-9.684758,6.812003,-7.747763,-3.848873,1.858432,-3.660304,6.511656,4.858451,-6.454274,3.284722,-2.363130,-1.822478,-4.374587,-1.333706,9.375012,-7.493778,4.338385,-1.361288,-5.963653,8.180458,-1.370250,6.524559,-7.106403,8.671789,6.062149,1.571346,-5.164968,5.672065,4.534442,-5.132758,5.394196,7.895754,-7.814115,-9.044195,-1.674489,-7.279200,-8.652795,-3.496426,1.949859,6.596416,-3.258978,-9.652463,0.543253,5.921545,8.007813,5.238695,-7.299017,-6.347366,-2.428678,0.792767,-2.854748,6.914701,6.299716,3.593053,-5.281372,-6.055627,1.439764,9.099248,-9.211502,-6.344714,-2.162082,-9.161349,-8.513840,-7.363381,6.767302,9.892289,2.568153,-3.579092,-2.376915,7.138071,0.595774,4.691989,3.768340,3.133694,3.283447,1.426431,8.141117,0.022136,-3.403314,-8.881493,5.495563,0.446902,9.749730,-0.779426,9.359736,-9.504527,1.395529,-5.808827,-6.738831,-7.296977,4.402105,1.546455,3.602979,-5.693907,-6.397085,3.776186,-1.666064,9.033157,0.479697,3.472921,7.609706,5.774614,4.694850,8.501111,7.480978,6.441572,-5.600644,7.482300,2.363440,3.806632,-0.150806,-0.607764,-4.745020,-8.923662,2.084901,-1.403393,0.729921,1.304050,8.112265,-5.611764,-8.299060,9.893724,1.933270,-6.968880,-9.539333,-5.020042,-9.029679,3.466916,-1.764348,-0.452203,7.347745,5.097147,-6.921095,8.147126,0.361959,-7.784031,-1.223748,-5.669313,-0.324693,-8.804014,3.980044,-1.022140,0.261753,-5.152780,4.284038,3.540761,1.556896,-7.787020,5.840536,-1.134346,7.780595,-1.594106,-0.981223,2.384921,0.904664,-1.273144,8.255864,4.613527,-4.356234,-8.716990,-6.122053,0.574145,-6.050166,-8.886847,4.595022,2.328828,5.069618,-4.133139,-1.881516,7.796738,-6.963392,-1.894429,-9.322949,-1.165310,1.833099,-6.473469,4.872196,-3.715156,4.230932,8.329533,9.039945,-5.035052,8.949731,-9.135593,-7.796306,5.719911,7.426086,-7.832391,1.151422,6.820862,-0.700287,0.047180,0.320800,1.562313,-0.674638,6.623236,0.287237,-4.843240,9.469858,0.944407,-7.321948,-5.667955,-9.645841,4.082189,4.023882,1.530444,6.535425,7.265576,-0.148211,1.297239,-8.890005,-2.382480,-1.427253,-2.515753,5.619369,-0.060920,-3.344326,-2.125528,9.319437,2.429849,-5.673928,-3.274387,1.749734,-0.158053,1.885775,-9.082367,-7.455872,8.322421,9.296091,-2.279531,7.957908,8.766135,9.961469,1.331087,4.398918,-2.492960,6.307479,5.315047,-1.035441,-5.575915,-5.008486,6.727467,3.003126,9.738885,-1.203856,2.549779,-5.388450,-7.150375,-5.763327,4.192220,-3.209336,0.596879,-7.697317,-5.034180,-8.954645,-5.554984,8.339482,-3.734156,5.543130,7.894297,1.136126,2.247828,3.054697,-0.615738,1.591654,-9.848985,1.573826,3.478250,-4.037937,-9.368913,-7.083488,5.845411,8.151547,-2.859747,-4.711171,-9.949866,9.281124,0.711310,1.618204,-9.314144,2.838305,-4.350527,6.984660,3.616029,2.559033,-6.465967,-6.167316,7.378620,3.924851,-3.344618,-1.501816,-0.406137,9.604178,-7.975431,1.676289,2.916714,7.579082,7.567560,-0.488679,1.140435,-0.008859,5.535385,9.295241,-7.107672,7.391182,-6.149551,-5.305363,6.102180,2.868258,-4.510109,-8.153788,0.875245,-2.834653,-9.043202,7.117809,-9.934703,-1.395635,4.751594,1.282317,-8.115574,-1.978720,-1.518653,8.501452,-3.667514,7.197760,1.375838,5.581748,-8.422867,9.790988,-8.153743,-6.414445,4.281842], dtype = "float64")#candidate|5565|(1638,)|const|float64
call_5564 = relay.TupleGetItem(func_1070_call(relay.reshape(const_5565.astype('float64'), [14, 13, 9])), 0)
call_5566 = relay.TupleGetItem(func_1073_call(relay.reshape(const_5565.astype('float64'), [14, 13, 9])), 0)
func_4993_call = mod.get_global_var('func_4993')
func_4996_call = mutated_mod.get_global_var('func_4996')
var_5568 = relay.var("var_5568", dtype = "int32", shape = (1, 14))#candidate|5568|(1, 14)|var|int32
call_5567 = relay.TupleGetItem(func_4993_call(relay.reshape(var_5568.astype('int32'), [1, 14])), 3)
call_5569 = relay.TupleGetItem(func_4996_call(relay.reshape(var_5568.astype('int32'), [1, 14])), 3)
func_3040_call = mod.get_global_var('func_3040')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_5573 = func_3040_call()
call_5574 = func_3040_call()
func_2879_call = mod.get_global_var('func_2879')
func_2881_call = mutated_mod.get_global_var('func_2881')
call_5578 = relay.TupleGetItem(func_2879_call(), 0)
call_5579 = relay.TupleGetItem(func_2881_call(), 0)
func_2879_call = mod.get_global_var('func_2879')
func_2881_call = mutated_mod.get_global_var('func_2881')
call_5582 = relay.TupleGetItem(func_2879_call(), 0)
call_5583 = relay.TupleGetItem(func_2881_call(), 0)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_5586 = relay.TupleGetItem(func_2741_call(), 3)
call_5587 = relay.TupleGetItem(func_2742_call(), 3)
func_4458_call = mod.get_global_var('func_4458')
func_4460_call = mutated_mod.get_global_var('func_4460')
call_5589 = relay.TupleGetItem(func_4458_call(), 1)
call_5590 = relay.TupleGetItem(func_4460_call(), 1)
func_5141_call = mod.get_global_var('func_5141')
func_5143_call = mutated_mod.get_global_var('func_5143')
call_5596 = relay.TupleGetItem(func_5141_call(), 0)
call_5597 = relay.TupleGetItem(func_5143_call(), 0)
output = relay.Tuple([call_5560,call_5564,const_5565,call_5567,var_5568,call_5573,call_5578,call_5582,call_5586,call_5589,call_5596,])
output2 = relay.Tuple([call_5561,call_5566,const_5565,call_5569,var_5568,call_5574,call_5579,call_5583,call_5587,call_5590,call_5597,])
func_5618 = relay.Function([var_5568,], output)
mod['func_5618'] = func_5618
mod = relay.transform.InferType()(mod)
var_5619 = relay.var("var_5619", dtype = "int32", shape = (1, 14))#candidate|5619|(1, 14)|var|int32
output = func_5618(var_5619)
func_5620 = relay.Function([var_5619], output)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4594_call = mod.get_global_var('func_4594')
func_4596_call = mutated_mod.get_global_var('func_4596')
call_5624 = func_4594_call()
call_5625 = func_4594_call()
func_4594_call = mod.get_global_var('func_4594')
func_4596_call = mutated_mod.get_global_var('func_4596')
call_5630 = func_4594_call()
call_5631 = func_4594_call()
output = relay.Tuple([call_5624,call_5630,])
output2 = relay.Tuple([call_5625,call_5631,])
func_5656 = relay.Function([], output)
mod['func_5656'] = func_5656
mod = relay.transform.InferType()(mod)
output = func_5656()
func_5657 = relay.Function([], output)
mutated_mod['func_5657'] = func_5657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5246_call = mod.get_global_var('func_5246')
func_5247_call = mutated_mod.get_global_var('func_5247')
call_5691 = func_5246_call()
call_5692 = func_5246_call()
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_5714 = relay.TupleGetItem(func_2589_call(), 0)
call_5715 = relay.TupleGetItem(func_2590_call(), 0)
func_5252_call = mod.get_global_var('func_5252')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_5721 = relay.TupleGetItem(func_5252_call(), 0)
call_5722 = relay.TupleGetItem(func_5254_call(), 0)
output = relay.Tuple([call_5691,call_5714,call_5721,])
output2 = relay.Tuple([call_5692,call_5715,call_5722,])
func_5727 = relay.Function([], output)
mod['func_5727'] = func_5727
mod = relay.transform.InferType()(mod)
mutated_mod['func_5727'] = func_5727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mutated_mod.get_global_var('func_5727')
call_5728 = func_5727_call()
output = call_5728
func_5729 = relay.Function([], output)
mutated_mod['func_5729'] = func_5729
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5813 = relay.var("var_5813", dtype = "int32", shape = ())#candidate|5813|()|var|int32
var_5814 = relay.var("var_5814", dtype = "int32", shape = (7, 13, 11))#candidate|5814|(7, 13, 11)|var|int32
bop_5815 = relay.bitwise_and(var_5813.astype('int32'), var_5814.astype('int32')) # shape=(7, 13, 11)
func_3808_call = mod.get_global_var('func_3808')
func_3811_call = mutated_mod.get_global_var('func_3811')
var_5829 = relay.var("var_5829", dtype = "float32", shape = (15, 4))#candidate|5829|(15, 4)|var|float32
call_5828 = func_3808_call(relay.reshape(var_5829.astype('float32'), [12, 5, 1]))
call_5830 = func_3808_call(relay.reshape(var_5829.astype('float32'), [12, 5, 1]))
func_483_call = mod.get_global_var('func_483')
func_486_call = mutated_mod.get_global_var('func_486')
var_5835 = relay.var("var_5835", dtype = "int32", shape = (1, 14))#candidate|5835|(1, 14)|var|int32
const_5836 = relay.const([[9,-3,-1,4,-9,-7,3,9,8,2,-7,-8,8,-2],[2,-5,8,-9,8,-8,2,-9,-9,4,-10,3,-1,-8],[3,-1,8,7,3,-6,9,10,-1,-6,-9,10,-9,7],[-6,-1,7,-7,10,-2,1,-8,1,-2,6,5,-10,-5],[9,-1,6,-5,5,-7,-7,-2,8,9,-7,-4,-10,-8],[-3,1,2,-9,5,-3,-8,-7,-1,3,10,-1,-10,-10],[3,1,1,-9,4,-3,-4,9,-7,8,9,7,1,4],[2,-4,-4,-2,8,7,-3,-1,7,10,-10,3,-10,-7],[-8,-4,7,-7,4,-5,5,4,-4,-5,-7,-6,5,-4],[-10,6,4,-10,8,3,1,4,-9,3,5,4,-7,1],[-10,7,-8,9,2,6,-1,6,6,-7,10,10,-10,-1],[7,-8,-7,-6,-7,10,6,-3,-6,8,-9,-8,-5,-6],[3,1,-9,8,4,-2,10,-10,9,-3,2,-4,-8,-2],[1,9,5,-5,-1,-2,-6,5,6,4,1,-8,-1,-4],[7,2,-5,-5,5,7,-4,10,-1,7,2,-5,-9,6],[9,8,9,5,5,4,-1,-5,-8,-4,9,10,-3,6],[10,-3,-5,5,3,6,2,-7,9,-6,6,-7,3,10],[-2,7,10,9,1,7,-5,-3,5,8,3,-10,-7,-5],[4,-6,2,8,-5,5,-2,1,7,4,5,5,-7,-6],[4,5,-7,-6,-6,10,3,9,-8,-3,-6,9,9,1],[9,-2,-1,4,-10,8,7,9,-3,-5,9,-8,-3,8],[10,-9,9,3,8,9,-10,-6,-6,6,5,10,9,1],[-4,-5,-8,-3,-4,6,-6,2,5,2,4,9,-9,-3],[9,-2,3,-7,-2,10,9,-9,-3,8,10,-9,7,-2],[-9,5,-9,2,6,4,2,-5,-2,-3,-7,4,2,-2],[1,5,10,-9,7,-2,-3,-3,2,5,4,8,-10,9],[-4,-10,6,9,5,5,-1,7,3,6,-7,9,8,3],[10,1,4,10,-7,5,7,8,-7,2,4,-7,-1,-4],[-4,9,10,9,-1,3,-8,-4,8,-4,6,5,4,-2],[-8,3,3,7,2,-9,-7,-5,-1,-1,-10,2,-9,-5],[-10,-7,5,-4,10,4,-7,6,-5,8,-9,-3,-4,-2],[-5,-7,6,-3,1,-9,-9,4,-6,-2,9,-7,1,-7],[8,-9,8,5,-7,5,8,-9,-9,-4,3,-7,6,-3],[5,-1,9,5,-3,9,1,-9,2,-5,-1,7,5,-8],[-10,-5,9,10,-5,5,-5,9,10,4,-6,-2,-8,-2],[-5,-1,1,1,-5,10,-4,-9,1,5,-7,-5,10,3],[8,-8,-8,-9,-8,-1,-1,-2,-5,-6,-2,-10,-1,-4],[-2,-8,2,5,-8,9,7,8,10,-5,-4,3,-5,5],[-8,7,-5,2,3,-7,6,-7,-7,-10,-9,-2,-7,7],[10,8,-2,-7,1,4,9,-7,9,-5,-10,-1,-2,-2]], dtype = "int32")#candidate|5836|(40, 14)|const|int32
call_5834 = relay.TupleGetItem(func_483_call(relay.reshape(var_5835.astype('int32'), [14, 1, 1]), relay.reshape(const_5836.astype('int32'), [14, 8, 5]), ), 1)
call_5837 = relay.TupleGetItem(func_486_call(relay.reshape(var_5835.astype('int32'), [14, 1, 1]), relay.reshape(const_5836.astype('int32'), [14, 8, 5]), ), 1)
func_2408_call = mod.get_global_var('func_2408')
func_2411_call = mutated_mod.get_global_var('func_2411')
call_5843 = relay.TupleGetItem(func_2408_call(relay.reshape(call_5834.astype('float32'), [2, 24])), 1)
call_5844 = relay.TupleGetItem(func_2411_call(relay.reshape(call_5834.astype('float32'), [2, 24])), 1)
output = relay.Tuple([bop_5815,call_5828,var_5829,call_5834,var_5835,const_5836,call_5843,])
output2 = relay.Tuple([bop_5815,call_5830,var_5829,call_5837,var_5835,const_5836,call_5844,])
func_5848 = relay.Function([var_5813,var_5814,var_5829,var_5835,], output)
mod['func_5848'] = func_5848
mod = relay.transform.InferType()(mod)
mutated_mod['func_5848'] = func_5848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5848_call = mutated_mod.get_global_var('func_5848')
var_5850 = relay.var("var_5850", dtype = "int32", shape = ())#candidate|5850|()|var|int32
var_5851 = relay.var("var_5851", dtype = "int32", shape = (7, 13, 11))#candidate|5851|(7, 13, 11)|var|int32
var_5852 = relay.var("var_5852", dtype = "float32", shape = (15, 4))#candidate|5852|(15, 4)|var|float32
var_5853 = relay.var("var_5853", dtype = "int32", shape = (1, 14))#candidate|5853|(1, 14)|var|int32
call_5849 = func_5848_call(var_5850,var_5851,var_5852,var_5853,)
output = call_5849
func_5854 = relay.Function([var_5850,var_5851,var_5852,var_5853,], output)
mutated_mod['func_5854'] = func_5854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3180_call = mod.get_global_var('func_3180')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_5859 = relay.TupleGetItem(func_3180_call(), 1)
call_5860 = relay.TupleGetItem(func_3181_call(), 1)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_5861 = relay.TupleGetItem(func_2741_call(), 2)
call_5862 = relay.TupleGetItem(func_2742_call(), 2)
output = relay.Tuple([call_5859,call_5861,])
output2 = relay.Tuple([call_5860,call_5862,])
func_5871 = relay.Function([], output)
mod['func_5871'] = func_5871
mod = relay.transform.InferType()(mod)
mutated_mod['func_5871'] = func_5871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5871_call = mutated_mod.get_global_var('func_5871')
call_5872 = func_5871_call()
output = call_5872
func_5873 = relay.Function([], output)
mutated_mod['func_5873'] = func_5873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_5877 = relay.TupleGetItem(func_3534_call(), 0)
call_5878 = relay.TupleGetItem(func_3536_call(), 0)
output = relay.Tuple([call_5877,])
output2 = relay.Tuple([call_5878,])
func_5884 = relay.Function([], output)
mod['func_5884'] = func_5884
mod = relay.transform.InferType()(mod)
mutated_mod['func_5884'] = func_5884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5884_call = mutated_mod.get_global_var('func_5884')
call_5885 = func_5884_call()
output = call_5885
func_5886 = relay.Function([], output)
mutated_mod['func_5886'] = func_5886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3729_call = mod.get_global_var('func_3729')
func_3731_call = mutated_mod.get_global_var('func_3731')
call_5887 = func_3729_call()
call_5888 = func_3729_call()
func_2810_call = mod.get_global_var('func_2810')
func_2812_call = mutated_mod.get_global_var('func_2812')
call_5889 = relay.TupleGetItem(func_2810_call(), 0)
call_5890 = relay.TupleGetItem(func_2812_call(), 0)
output = relay.Tuple([call_5887,call_5889,])
output2 = relay.Tuple([call_5888,call_5890,])
func_5893 = relay.Function([], output)
mod['func_5893'] = func_5893
mod = relay.transform.InferType()(mod)
output = func_5893()
func_5894 = relay.Function([], output)
mutated_mod['func_5894'] = func_5894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4643_call = mod.get_global_var('func_4643')
func_4645_call = mutated_mod.get_global_var('func_4645')
call_5939 = relay.TupleGetItem(func_4643_call(), 0)
call_5940 = relay.TupleGetItem(func_4645_call(), 0)
output = call_5939
output2 = call_5940
func_5957 = relay.Function([], output)
mod['func_5957'] = func_5957
mod = relay.transform.InferType()(mod)
output = func_5957()
func_5958 = relay.Function([], output)
mutated_mod['func_5958'] = func_5958
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5981 = relay.var("var_5981", dtype = "bool", shape = ())#candidate|5981|()|var|bool
var_5982 = relay.var("var_5982", dtype = "bool", shape = (15, 2, 16))#candidate|5982|(15, 2, 16)|var|bool
bop_5983 = relay.logical_and(var_5981.astype('bool'), var_5982.astype('bool')) # shape=(15, 2, 16)
output = bop_5983
output2 = bop_5983
func_5988 = relay.Function([var_5981,var_5982,], output)
mod['func_5988'] = func_5988
mod = relay.transform.InferType()(mod)
mutated_mod['func_5988'] = func_5988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5988_call = mutated_mod.get_global_var('func_5988')
var_5990 = relay.var("var_5990", dtype = "bool", shape = ())#candidate|5990|()|var|bool
var_5991 = relay.var("var_5991", dtype = "bool", shape = (15, 2, 16))#candidate|5991|(15, 2, 16)|var|bool
call_5989 = func_5988_call(var_5990,var_5991,)
output = call_5989
func_5992 = relay.Function([var_5990,var_5991,], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3617_call = mod.get_global_var('func_3617')
func_3618_call = mutated_mod.get_global_var('func_3618')
call_6002 = relay.TupleGetItem(func_3617_call(), 0)
call_6003 = relay.TupleGetItem(func_3618_call(), 0)
func_212_call = mod.get_global_var('func_212')
func_215_call = mutated_mod.get_global_var('func_215')
const_6007 = relay.const([4.171485,7.579777,9.228127,9.708680,-2.268541,9.277496,4.583657,7.929333,8.046895,-8.345822,5.018854,-6.999460,-9.406564,-6.696795,-1.280601,-4.696176,3.545516,5.017940,-5.738182,9.783825,7.447995,8.329912,-2.746764,6.063401,6.294306,-5.776270,4.653034,-4.544625,-9.053331,0.870947,-4.690509,-2.747421,5.873057,-6.367828,-0.260768,-4.283203,-7.947661,-8.508578,0.818861,3.134049,3.287015,0.899058,-5.672506,-4.116194,4.339047,-4.840752,-7.014320,8.830227], dtype = "float32")#candidate|6007|(48,)|const|float32
call_6006 = func_212_call(relay.reshape(const_6007.astype('float32'), [8, 1, 6]))
call_6008 = func_212_call(relay.reshape(const_6007.astype('float32'), [8, 1, 6]))
func_5429_call = mod.get_global_var('func_5429')
func_5432_call = mutated_mod.get_global_var('func_5432')
var_6010 = relay.var("var_6010", dtype = "float64", shape = (1638,))#candidate|6010|(1638,)|var|float64
call_6009 = relay.TupleGetItem(func_5429_call(relay.reshape(var_6010.astype('float64'), [1638,])), 0)
call_6011 = relay.TupleGetItem(func_5432_call(relay.reshape(var_6010.astype('float64'), [1638,])), 0)
func_5957_call = mod.get_global_var('func_5957')
func_5958_call = mutated_mod.get_global_var('func_5958')
call_6029 = func_5957_call()
call_6030 = func_5957_call()
output = relay.Tuple([call_6002,call_6006,const_6007,call_6009,var_6010,call_6029,])
output2 = relay.Tuple([call_6003,call_6008,const_6007,call_6011,var_6010,call_6030,])
func_6036 = relay.Function([var_6010,], output)
mod['func_6036'] = func_6036
mod = relay.transform.InferType()(mod)
mutated_mod['func_6036'] = func_6036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6037 = relay.var("var_6037", dtype = "float64", shape = (1638,))#candidate|6037|(1638,)|var|float64
func_6036_call = mutated_mod.get_global_var('func_6036')
call_6038 = func_6036_call(var_6037)
output = call_6038
func_6039 = relay.Function([var_6037], output)
mutated_mod['func_6039'] = func_6039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3680_call = mod.get_global_var('func_3680')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_6083 = relay.TupleGetItem(func_3680_call(), 0)
call_6084 = relay.TupleGetItem(func_3682_call(), 0)
func_4491_call = mod.get_global_var('func_4491')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_6150 = relay.TupleGetItem(func_4491_call(), 0)
call_6151 = relay.TupleGetItem(func_4492_call(), 0)
uop_6156 = relay.acos(call_6083.astype('float64')) # shape=(4, 2, 4)
uop_6158 = relay.acos(call_6084.astype('float64')) # shape=(4, 2, 4)
func_1870_call = mod.get_global_var('func_1870')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_6186 = func_1870_call()
call_6187 = func_1870_call()
func_3873_call = mod.get_global_var('func_3873')
func_3876_call = mutated_mod.get_global_var('func_3876')
var_6190 = relay.var("var_6190", dtype = "int8", shape = (2640,))#candidate|6190|(2640,)|var|int8
call_6189 = relay.TupleGetItem(func_3873_call(relay.reshape(var_6190.astype('int8'), [16, 11, 15]), relay.reshape(var_6190.astype('int8'), [16, 11, 15]), ), 0)
call_6191 = relay.TupleGetItem(func_3876_call(relay.reshape(var_6190.astype('int8'), [16, 11, 15]), relay.reshape(var_6190.astype('int8'), [16, 11, 15]), ), 0)
output = relay.Tuple([call_6150,uop_6156,call_6186,call_6189,var_6190,])
output2 = relay.Tuple([call_6151,uop_6158,call_6187,call_6191,var_6190,])
func_6200 = relay.Function([var_6190,], output)
mod['func_6200'] = func_6200
mod = relay.transform.InferType()(mod)
var_6201 = relay.var("var_6201", dtype = "int8", shape = (2640,))#candidate|6201|(2640,)|var|int8
output = func_6200(var_6201)
func_6202 = relay.Function([var_6201], output)
mutated_mod['func_6202'] = func_6202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_6254 = relay.TupleGetItem(func_2589_call(), 0)
call_6255 = relay.TupleGetItem(func_2590_call(), 0)
func_3873_call = mod.get_global_var('func_3873')
func_3876_call = mutated_mod.get_global_var('func_3876')
const_6273 = relay.const([-5,-2,-10,5,8,4,-1,3,8,2,2,-3,1,8,-4,-9,-1,10,-7,-9,10,6,10,7,-9,3,2,-6,5,-10,-4,9,-9,7,8,3,-9,-7,10,6,-6,-1,-6,-1,1,-1,-10,2,-3,-7,5,7,1,-3,-2,10,-8,6,10,-5,9,-7,10,10,8,-2,-7,9,5,-1,-10,4,-4,4,-8,-6,-6,-5,4,-10,3,5,1,10,-5,4,1,-7,-8,10,1,10,3,-4,1,9,-5,3,-8,3,-3,-3,5,-1,1,7,-1,9,-2,-1,6,4,4,-9,-2,8,-1,10,-8,-9,6,1,2,-1,3,-7,2,10,1,-10,6,-8,8,-3,3,-7,9,-4,8,-9,-7,-7,10,-7,-9,-5,7,-1,3,3,-9,3,-8,1,4,4,6,2,-3,8,8,-6,-7,9,-5,6,-3,-2,-7,7,-4,-5,-6,-8,-8,10,10,-2,-7,8,5,5,-4,1,3,5,2,-10,6,7,6,1,-3,4,-8,-1,-8,-3,5,-8,-3,-6,4,1,-5,6,-6,-9,2,1,8,2,-8,10,8,-2,2,4,-3,6,5,-1,-8,2,-8,1,4,-3,10,-8,3,9,-7,9,-10,-9,-6,-8,5,-6,2,8,-3,-10,6,1,-7,5,3,-5,-9,-10,9,1,7,-6,5,4,-8,-2,4,4,-4,-7,-4,-10,1,10,-7,3,-8,-4,6,2,-4,-8,8,2,-10,-8,3,9,-9,5,10,1,-8,1,-5,-8,7,-9,-8,6,-2,-4,2,1,2,9,-4,10,-7,6,3,-1,7,-7,1,-3,-8,9,10,-3,-6,6,5,1,-6,2,-10,4,-4,-4,-4,7,-6,6,-6,10,-3,1,-2,-10,9,10,6,7,-4,-7,8,2,2,-9,7,10,6,8,4,-6,9,-10,-1,6,-8,4,7,-7,4,-7,5,-2,9,-9,-7,3,3,2,-2,9,-1,3,1,-9,8,-7,-3,6,-9,6,9,10,5,-6,-2,5,8,-3,10,5,6,-4,10,-3,-4,3,-10,-5,-6,-2,-6,2,-6,2,-5,-5,6,1,9,5,3,-7,2,8,3,-8,6,10,5,10,-8,2,-6,9,9,9,3,-6,7,5,-3,-8,3,5,-1,-7,-1,2,3,3,7,-3,5,7,3,-2,3,9,10,-1,6,8,10,-5,3,-5,7,1,7,-5,-10,-9,7,-6,-10,7,-8,7,7,10,-9,10,-1,9,-1,-10,-1,3,-7,-6,9,-6,10,-4,5,-9,-7,10,4,-7,6,-5,8,-7,-8,-3,6,-3,-3,7,10,-2,-7,-6,4,5,3,-6,-7,-6,-8,1,8,-2,10,1,-5,7,-5,-2,-8,-10,-6,-4,1,-9,8,-3,-5,-9,6,5,3,5,4,-9,-4,-5,-7,-3,-8,-7,4,5,9,-2,-6,-10,8,-8,-3,-7,8,-5,-3,-3,-3,-7,4,-6,-10,10,7,4,5,10,-1,-3,10,-1,-10,-2,-7,-2,5,-6,8,10,5,-1,-5,10,-7,-4,3,-10,2,-6,2,-1,-5,1,-2,9,4,2,2,-7,5,7,-7,-10,8,-7,5,-9,-5,-4,-1,8,2,9,10,-4,-7,2,6,4,-2,-6,9,5,-8,-2,-1,-6,-10,6,3,6,1,-6,4,2,-1,10,6,5,-4,4,-9,10,-9,1,6,-4,9,-3,1,6,-8,3,4,9,-7,5,5,-5,-2,6,6,-5,9,-8,7,-2,2,8,-5,6,-2,-8,-8,1,1,-10,-7,-4,4,9,-7,6,-8,7,-1,-5,-6,10,-6,-4,10,6,8,8,-3,5,7,9,-6,-1,9,-2,7,-9,-4,-1,-4,4,8,-3,-8,-1,10,2,-6,4,9,10,-9,8,-1,-8,8,6,5,-7,10,9,7,7,-6,-1,-9,10,10,-9,-9,-6,2,-2,-3,-9,-4,2,-2,7,10,-3,-8,6,1,1,-6,-8,10,3,-7,-4,-3,-4,-5,-4,-8,-5,10,-4,-9,-2,1,3,-9,3,-1,9,-5,-8,6,9,-1,-8,-8,-3,-5,-3,-6,-8,-3,1,9,-5,-4,7,6,-4,10,7,4,6,4,8,6,-5,6,-10,-7,-9,1,-3,-2,4,-8,-10,3,-4,7,-9,5,-1,-9,3,-7,8,-8,7,-7,2,3,8,9,-3,3,9,-5,8,-3,-1,-5,8,-10,-5,-5,-2,10,4,-3,8,-10,-3,-9,-10,-4,-3,-2,4,6,-8,-6,-1,10,8,4,-9,-2,9,3,-4,-2,6,7,-5,9,6,-4,2,2,-9,-5,-9,1,10,9,1,-10,5,-6,2,6,9,-3,-5,-10,-1,3,1,10,-5,5,10,2,-7,-8,2,-5,3,3,-4,2,-9,5,-6,1,-4,9,6,-3,-10,9,4,-4,-5,5,-3,5,10,1,-5,-1,-3,-6,2,1,10,-3,-8,-1,7,2,-3,-1,5,2,8,-10,2,1,3,5,4,8,-6,-2,-7,4,-1,6,10,-5,-1,-1,-1,8,-6,9,-2,9,10,-2,8,-8,2,-5,1,-1,7,7,4,-3,-8,-10,1,-10,-3,-7,-10,-7,2,5,4,-8,-7,8,-10,-2,3,-1,-1,5,-7,4,1,10,-5,-7,-10,-9,-9,8,6,-10,-4,-5,-3,-3,-7,8,10,1,2,4,4,10,-10,3,-10,7,3,3,6,-6,2,-3,3,-10,4,8,-7,3,7,-5,8,-5,6,9,-3,-7,1,9,-5,-9,-3,9,7,9,-8,5,6,9,7,8,-2,-6,4,-7,4,-10,-4,7,2,7,10,-8,-1,2,4,9,4,1,3,-9,-5,-4,-9,-2,8,-3,-1,-9,-7,-2,1,-8,-1,3,8,-2,10,-2,8,-1,5,-7,4,-1,-8,-3,6,-2,-2,-2,-6,3,-8,-6,-1,5,1,-4,-9,-8,-8,4,4,-3,-2,7,7,3,-5,4,-3,1,10,-1,-10,5,-1,4,-8,4,-1,-5,10,-6,4,10,8,5,7,-10,-4,7,-6,3,-9,4,-5,-10,7,-10,5,-10,3,2,1,9,7,-3,10,-8,10,-10,-9,1,-4,8,-3,4,-6,-8,-8,-4,-4,9,10,4,9,8,4,-5,2,-10,4,3,-10,-6,-9,-5,-5,8,2,-9,5,9,7,-10,7,-6,-3,10,-1,2,-7,2,1,-9,-3,4,-4,-7,-8,9,-6,8,-5,5,-5,5,-5,-1,-10,-9,-9,-1,7,5,7,-3,-1,4,-9,4,-5,-3,-10,7,7,1,1,10,-1,5,8,-1,-9,5,-4,-2,-9,-1,3,7,6,-7,-1,2,3,10,-5,10,-5,-6,5,-2,-4,3,1,-9,-7,1,-5,-2,2,10,2,-5,-9,8,8,-8,2,-10,-1,-1,7,-8,7,-1,-1,-8,2,-2,2,-5,-9,-3,-6,4,-3,-6,7,3,6,-4,-6,10,8,9,1,2,-8,-8,1,-4,7,7,5,-9,-3,-8,7,-6,-1,5,-10,-1,-2,-5,-3,7,8,-3,3,4,4,6,-3,6,-7,5,8,6,-4,-2,9,-6,-5,-7,-10,-6,-4,-8,5,10,-5,-1,-10,-4,7,1,7,-10,6,-3,-2,-3,-3,3,6,-2,-8,-3,-10,-3,3,5,-1,4,-4,-6,-10,-3,1,-3,-1,8,-1,-8,-10,-10,-6,4,-9,7,-9,-2,-3,4,-4,2,3,5,-3,-5,-5,-7,-9,10,-1,-5,-9,9,-5,5,9,5,7,8,-4,-6,-9,1,4,-7,-8,3,-1,-7,-3,-6,-2,-6,10,1,-6,-10,-10,2,2,-6,6,-6,-4,-3,-9,-9,9,-10,-9,10,9,-8,-3,-10,-2,5,-8,4,8,-8,8,8,5,6,-8,-7,10,-4,8,8,-2,9,-8,3,4,-2,1,2,7,-9,-6,-2,4,9,-1,5,4,7,-8,-7,-4,-5,-1,2,-6,-5,-9,-1,4,-6,-9,-2,2,-4,-2,3,3,10,8,4,-4,8,-7,-4,-9,7,9,10,9,-4,-6,-6,8,5,-9,-9,9,4,-6,-6,-1,2,2,-5,-7,-5,-7,-4,-8,-10,7,10,7,-9,-6,-6,9,1,4,-6,5,6,2,-9,-6,-7,-10,-8,-5,-8,3,10,-5,-5,4,-10,3,-5,5,-3,-4,-5,-9,9,-9,5,-2,3,-5,-6,10,-10,-1,5,-8,6,-1,6,3,6,-4,-3,-7,6,7,-2,8,-1,6,5,-6,-8,2,-9,-9,7,5,2,8,-5,-9,-1,9,-6,-10,1,-1,-5,10,8,-8,-5,-2,-8,-6,-5,-7,2,10,1,8,-8,-8,10,6,9,2,10,2,4,8,-3,-10,3,4,10,5,-8,10,2,7,-3,-7,3,-8,1,8,2,-10,8,8,-3,7,-5,3,-4,-9,7,9,-9,-7,-4,4,-5,-3,-8,10,-2,-5,5,-4,-8,7,3,7,2,10,-1,3,1,-6,7,-10,-4,-7,5,-9,6,-10,1,-1,-1,10,-7,7,-1,7,-2,6,-4,-6,-6,-1,10,-3,9,3,-7,2,-8,-4,-6,6,7,-4,6,-9,-5,-9,4,-6,-8,-4,4,10,7,-10,6,10,7,-4,2,-7,6,1,-8,4,6,10,4,-3,-8,3,-10,-7,7,-1,-7,-7,4,4,5,-9,-5,-2,-3,-9,9,-2,5,5,3,10,-4,-2,4,-4,1,9,-4,-5,7,7,6,-2,-1,2,3,-1,-8,7,6,-1,7,-4,-1,8,-3,-2,4,-9,-3,8,-4,2,1,-3,5,5,4,-2,10,-2,7,-3,2,-8,4,10,5,9,-5,3,6,1,9,4,-5,6,2,3,-3,8,6,-7,-10,-5,1,-5,7,-9,-9,-8,1,6,-3,-9,1,6,-5,-8,-9,2,-2,9,2,6,2,8,7,-9,3,9,-5,-1,7,-9,-2,-8,-9,4,4,-5,-3,10,-6,-2,-6,1,5,-6,-1,1,-8,-8,6,10,-1,8,9,5,6,-2,-8,8,7,8,-10,3,-5,-7,-2,-3,-4,-6,1,-6,-9,-1,-3,2,4,-8,-8,2,-2,6,-6,9,-2,-10,-8,-9,-5,6,1,8,10,10,6,3,1,-2,-10,6,5,4,4,-10,6,-7,-6,4,8,3,-6,-2,8,5,-6,-2,8,-6,-1,-9,2,4,10,3,-2,4,7,-6,-1,-4,1,-9,2,-1,-10,10,6,-2,-1,-6,3,2,7,4,-8,-4,6,10,-9,-3,-1,2,6,-6,1,2,2,-6,4,7,-10,-3,-4,-6,-3,-3,9,-4,1,6,9,-8,3,-10,-5,1,7,4,8,-6,7,5,-7,5,-8,10,8,-8,3,8,-4,5,-2,5,-7,2,2,-3,6,-5,-8,2,4,-9,-10,6,7,-7,8,-10,5,-2,9,4,-5,2,5,-1,5,-9,-8,-1,4,-7,-2,-9,9,3,-9,5,-5,7,-2,2,-10,-4,-6,5,-3,-2,1,1,5,10,-1,7,-4,10,5,-3,5,-5,-2,-8,-5,1,4,-6,8,-2,-10,6,3,2,-10,-1,2,-5,-6,-1,-7,-7,-8,9,-8,6,-10,-4,2,9,2,-8,-5,1,8,-4,-8,-6,-5,-2,-6,1,-3,-8,-2,9,-6,8,-10,7,-3,-2,6,-5,5,-2,-8,-8,7,-7,3,-2,-1,-4,-9,10,6,1,10,-10,7,-7,-4,-7,-10,-1,10,-4,2,-3,-1,-3,5,-8,3,-1,10,5,-2,7,5,-7,-1,-6,-10,-4,-2,-7,-4,-1,3,-5,-9,-6,-3,4,-1,2,1,5,-9,-2,7,-5,4,-7,-7,9,3,8,10,-3,-3,5,5,3,10,-4,-5,-9,6,-4,-8,-2,8,-8,-1,9,8,-8,-3,-8,6,-1,2,10,6,2,8,-5,-3,5,4,8,10,-6,6,-6,-5,-3,-7,-6,8,-6,-1,3,6,9,-3,-3,-4,-6,10,-3,10,-3,-1,-9,8,-7,6,4,-7,-1,10,5,-2,4,-4,-10,-7,1,-3,-10,6,9,-5,-6,-4,7,3,-9,3,-9,-2,-1,-2,-10,-3,-6,-6,-4,6,5,1,5,2,-10,-7,3,-8,2,-7,4,1,-10,5,-9,-6,-10,-6,10,8,4,9,-9,-10,-6,3,6,2,-2,1,-7,-6,3,-3,-10,5,8,-1,-2,10,-9,-1,-9,-2,9,4,2,2,-2,10,-6,7,-10,3,-1,-1,-7,7,5,-9,-5,-10,-3,-4,-9,-6,-1,1,1,-5,-8,-5,1,1,1,2,-2,-5,-7,1,-3,-3,10,-8,-9,-5,3,9,4,-10,9,3,6,-8,6,1,6,8,9,9,10,2,-6,7,-1,4,-1,-3,6,-2,-9,-4,8,-1,9,-4,5,-4,6,-10,-10,-9,3,10,1,2,6,5,9,2,7,8,-1,-1,-6,6,-7,-7,-4,8,8,7,7,7,-9,3,-4,-6,-5,-3,-1,-7,1,7,-10,3,6,-1,4,-6,-6,1,-1,-6,-7,9,8,-4,-9,-6,-7,-6,-1,-3,-4,9,1,-3,-8,-1,8,3,-6,-4,-10,-4,9,2,-7,-6,6,-3,7,9,5,-2,-2,6,4,2,10,2,6,-9,9,-5,1,1,-4,-5,2,9,-2,1,4,-1,1,-4,-7,1,-6,-2,2,5,6,2,-7,4,-7,7,-10,6,2,-8,2,-9,-4,5,6,2,10,-4,7,6,4,-7,-2,4,4,-6,-9,-5,6,9,-2,6,8,-8,-9,-1,10,5,-3,-7,-1,3,8,5,10,7,-8,5,-4,-1,9,-6,-1,2,-10,-1,2,2,-4,5,2,7,9,-6,-6,8,10,-6,-4,5,7,-6,-9,-2,-7,6,-1,9,-6,-4,1,-10,5,2,-6,3,10,-4,-8,-2,3,4,3,-5,8,1,-1,-10,7,-6,-6,6,-8,7,-9,3,-6,-8,-2], dtype = "int8")#candidate|6273|(2640,)|const|int8
call_6272 = relay.TupleGetItem(func_3873_call(relay.reshape(const_6273.astype('int8'), [16, 11, 15]), relay.reshape(const_6273.astype('int8'), [16, 11, 15]), ), 0)
call_6274 = relay.TupleGetItem(func_3876_call(relay.reshape(const_6273.astype('int8'), [16, 11, 15]), relay.reshape(const_6273.astype('int8'), [16, 11, 15]), ), 0)
uop_6275 = relay.sqrt(call_6272.astype('float32')) # shape=(4, 2, 4)
uop_6277 = relay.sqrt(call_6274.astype('float32')) # shape=(4, 2, 4)
output = relay.Tuple([call_6254,const_6273,uop_6275,])
output2 = relay.Tuple([call_6255,const_6273,uop_6277,])
func_6296 = relay.Function([], output)
mod['func_6296'] = func_6296
mod = relay.transform.InferType()(mod)
mutated_mod['func_6296'] = func_6296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6296_call = mutated_mod.get_global_var('func_6296')
call_6297 = func_6296_call()
output = call_6297
func_6298 = relay.Function([], output)
mutated_mod['func_6298'] = func_6298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3216_call = mod.get_global_var('func_3216')
func_3217_call = mutated_mod.get_global_var('func_3217')
call_6343 = func_3216_call()
call_6344 = func_3216_call()
func_2810_call = mod.get_global_var('func_2810')
func_2812_call = mutated_mod.get_global_var('func_2812')
call_6348 = relay.TupleGetItem(func_2810_call(), 0)
call_6349 = relay.TupleGetItem(func_2812_call(), 0)
output = relay.Tuple([call_6343,call_6348,])
output2 = relay.Tuple([call_6344,call_6349,])
func_6356 = relay.Function([], output)
mod['func_6356'] = func_6356
mod = relay.transform.InferType()(mod)
output = func_6356()
func_6357 = relay.Function([], output)
mutated_mod['func_6357'] = func_6357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4643_call = mod.get_global_var('func_4643')
func_4645_call = mutated_mod.get_global_var('func_4645')
call_6383 = relay.TupleGetItem(func_4643_call(), 0)
call_6384 = relay.TupleGetItem(func_4645_call(), 0)
func_1717_call = mod.get_global_var('func_1717')
func_1721_call = mutated_mod.get_global_var('func_1721')
const_6393 = relay.const([-2,-1,-6,-7,7,7,-9,-10,-6,-4,-4,-3,-9,-10,3,-7,8,2,-9,4,-8,-5,-8,3,-5,-6,2,-8,4,-10,-5,-2,4,-8,-2,-3,5,-1,-7,8,-3,-1,-6,6,8,7,-2,8,-4,3,1,10,5,9,-6,-4,-3,-4,7,-9,5,-10,-4,6,-7,3,6,3,5,-3,-1,7,-3,5,2,-5,-7,-7,5,8,-2,-9,-6,-10,-4,-1,-2,-1,1,7,9,2,6,6,3,-1,-6,-5,-3,-3,-10,6,-5,8,-4,-9,4,-8,3,2,-1,-2,5,1,-2,9,-1,5,1,-9,-8,-9,-2,-5,-2,-10,1,-9,-7,8,-7,3,-9,3,2,8,-2,2,-1,-6,3,-7,-8,-3,-9,6,8,-5,6,9,-9,5,4,-3,4,10,-7,-4,-5,10,9,-9,3,-4,-1,-8,1,-2,-3,-10,6,4,6,8,6,5,-2,-2,10,6,10,4,7,6,10,-7,-5,10,3,-5,4,6,-8,-2,6,-2,10,-8,9,-9,2,-5,-10,-2,-1,-4,9,-2,8,-7,-10,1,-4,-10,-4,2,-8,-5,-2,-1,-4,-1,-5,-1,-6,7,7,9,8,-4,10,-2,-5,-7,4,1,5,2,-2,2,1,-6,-9,10,4,-4,10,-5,3,-1,1,6,3,-3,10,2,7,10,3,-5,-3,-3,3,9,9,-2,1,4,5,-8,-5,8,10,-9,-9,-2,-1,7,-1,1,-6,10,-2,-1,4,-4,4,2,-2,-9,-5,-3,-5,2,7,-8,10,-10,2,9,-5,-4,7,-2,-9,9,-9,-10,-5,2,8,4,-8,10,10,-4,4,-3,-8,-9,-4,-8,-5,9,1,-3,-1,-6,-3,-7,-6,9,2,1,7,-6,-10,-5,-1,4,-6,-2,4,-6,-2,4,-5,-8,-7,9,-10,-6,-7,5,5,-3,-8,10,1,-1,-10,-3,-9,3,1,-1,-5,1,-8,-4,-8,8,10,-8,-5,-3,5,9,8,-2,-4,-2,-10,2,1,-2,1,-5,-7,1,3,4,-4,5,-5,-3,-10,9,-9,-9,-7,1,1,10,-10,-10,6,4,9,4,-6,4,-1,7,1,2,5,7,-3,3,-7,8,-9,5,-2,1,-5,4,-5,10,5,6,-7,-7,10,-4,5,2,6,1,8,6,6,-1,-10,-8,3,8,-9,-10,7,5,8,3,7,-2,5,-8,7,-3,-10,-6,7,3,-9,6,-7,-5,10,-8,3,4,7,10,-1,3,-3,4,-10,-7,-8,-2,-4,1,-6,-3,-7,8,6,8,-8,1,-9,-1,-10,8,3,-6,-7,-1,5,4,8,8,10,5,6,-9,-1,-1,-1,2,9,1,4,-2,5,-1,-8,10,4,5,-1,4,-7,4,6,-1,3,-2,5,6,-2,4,-5,-9,2,-6,8,-7,-6,4,7,6,9,-7,-4,4,-9,7,7,-10,1,3,7,-6,-1,5,-6,-9,1,-7,8,-2,-4,-10,6,-9,5,6,-2,-5,3,-2,-10,-1,-7,-5,-4,4,5,-8,-4,-6,8,3,6,-4,9,-7,-5,8,-1,-8,10,-4,6,6,10,8,-7,10,10,-4,8,-8,4,-8,10,1,-10,5,-6,5,-4,-3,-6,4,-7,-5,-10,9,-10,8,-2,10,-3,-7,5,-2,-9,-9,10,-2,-10,1,1,-5,-6,9,-1,2,-3,10,3,8,-8,6,10,4,-7,1,6,9,8,-2,8,-2,2,-10,5,6,4,-1,10,-4,10,-6,-1,8,4,8,-3,2,10,2,-7,9,10,6,5,10,-5,-2,1,6,2,-7,2,-2,-9,-10,-3,-10,10,5,-3,-3,-1,-5,-6,10,-4,-3,-6,1,-9,4,1,-5,9,8,-4,2,-9,10,7,5,6,-8,-3,10,1,4,-9,6,-8,1,7,-1,-2,4,-10,-1,-7,1,-1,1,-6,-5,-3,-4,-5,-5,10,-1,-7,-2,-3,5,5,9,-8,9,7,-10,6,3,1,-6,-6,-5,-1,1,-3,4,-4,-3,5,-8,-5,3,4,-3,-4,10,-7,2,-4,-3,-1,3,2,-10,8,-7,8,-4,-6,9,-7,1,-4,3,-7,-4,-3,-8,3,-2,-7,5,9,-10,-6,8,-8,9,-1,1,-7,10,2,-7,-5,-7,7,8,1,2,6,1,8,-5,2,-1,-1,-1,9,7,4,-6,7,-7,-3,6,-1,-5,-8,-8,-6,-9,9,9,7,-2,1,-4,-6,-7,-3,10,9,-3,-6,7,-1,1,8,10,6,-10,3,-7,6,10,6,-3,5,-4,-6,-5,9,9,-5,-5,-10,-10,-9,-2,3,-4,1,-6,1,7,2,6,-7,-1,3,-3,-10,-8,2,-4,1,1,-5,-8,6,-6,7,-10,-7,9,6,5,-5,-5,-2,-9,6,2,-9,-10,6,-3,-9,1,5,-8,-2,-7,5,-3,10,9,-3,9,-1,-7,6,2,-7,1,-3,-1,3,1,9,-4,-5,8,4,-10,-6,-4,10,-8,-8,-7,10,-5,7,1,-9,8,10,2,1,8,2,2,9,7,8,10,3,1,1,-7,-6,4,8,9,9,-1,-3,-3], dtype = "uint16")#candidate|6393|(980,)|const|uint16
var_6394 = relay.var("var_6394", dtype = "float64", shape = (1638,))#candidate|6394|(1638,)|var|float64
call_6392 = relay.TupleGetItem(func_1717_call(relay.reshape(const_6393.astype('uint16'), [7, 10, 14]), relay.reshape(var_6394.astype('float64'), [1638,]), relay.reshape(const_6393.astype('float64'), [7, 10, 14]), ), 8)
call_6395 = relay.TupleGetItem(func_1721_call(relay.reshape(const_6393.astype('uint16'), [7, 10, 14]), relay.reshape(var_6394.astype('float64'), [1638,]), relay.reshape(const_6393.astype('float64'), [7, 10, 14]), ), 8)
func_6296_call = mod.get_global_var('func_6296')
func_6298_call = mutated_mod.get_global_var('func_6298')
call_6401 = relay.TupleGetItem(func_6296_call(), 0)
call_6402 = relay.TupleGetItem(func_6298_call(), 0)
func_2335_call = mod.get_global_var('func_2335')
func_2339_call = mutated_mod.get_global_var('func_2339')
const_6426 = relay.const([8.300780,6.165375,7.896130,3.841673,5.397995,4.078457,2.010707,4.585911,-9.205284,0.754364,-7.238904,-5.503786,2.209111,-0.209963,1.692350,5.263263,-1.130599,-2.215690,2.551166,4.797910,-9.547983,4.584786,-9.293785,-7.479393,-1.552824,7.376111,-9.457141,5.161520,0.728772,5.256446,-7.404354,-4.089804,7.487326,-8.544165,-0.026671,1.868968,7.472294,4.670358,-5.632571,-1.008454,7.691098,3.503182,-1.466385,4.295679,-5.408004,-9.584238,3.247520,1.040379,7.366209,-4.512379,3.982547,-1.750480,-9.267435,6.816217,8.793537,-6.636154,4.168782,4.949225,-8.537416,-9.554636,8.507309,-3.263630,0.880271,3.994084,9.280763,-0.796465,-9.693865,0.581500,-6.852521,5.157641,7.104000,6.915737,7.319763,-1.063368,9.366670,-2.279279,9.367197,-0.028337,-8.286466,7.059072,7.154494,-3.533655,2.674508,-5.424637,-4.479883,1.654283,4.643312,4.159313,0.168229,9.587442,-1.967902,7.527660,-5.678302,-7.370539,-1.780707,-5.288168,7.294479,6.059665,4.463733,3.720421,4.759802,4.086743,2.274457,2.267978,-4.771369,3.917034,-2.783479,-2.346404,-0.604095,4.200117,-0.750990,-3.628995,-7.585047,-1.850449,-0.960766,-0.139548,7.849977,-8.156650,-7.389250,7.508939,-7.586543,8.358212,-0.876349,2.590083,-7.041089,3.625589,8.489205,-0.111589,4.381958,7.684479,-9.360051,4.886411,3.567997,-8.875875,0.654105,-1.553479,4.126728,-9.565254,1.591297,-5.416502,-1.599006,-0.419915,-3.309036,3.714936,-2.330270,2.828530,-8.014242,-4.914666,-8.462925,1.514444,-1.266172,-1.038917,5.137228,7.204024,-0.428206,-8.634224,3.933031,-3.834991,-9.747168,5.557160,-4.192180,5.123987,2.651210,-0.594867,7.512720,7.706883,2.518860,2.676173,-9.561168,1.880551,-0.979662,4.993903,2.853085,2.422718,-5.663057,-5.002277,4.750001,3.418365,1.351908,9.262045,-6.127873,-0.806966,-5.215425,-9.495743,7.461457,3.152319,-0.041976,2.688475,2.566606,1.885514,-8.497750,-9.877076,4.340091,-4.277981,-0.342187,3.823261,7.440349,-0.630532,3.307421,-2.345490,8.761508,7.724107,7.817005,2.326912,9.553414,-7.588302,-0.362381,-3.719650,-4.707744,-8.065855,-3.674554,0.992945,1.932426,7.832753,3.052846,9.162930,0.493632,-9.869250,-6.325349,4.816213,-1.879839,6.795337,0.605230,-2.727513,-9.364879,-9.275282,2.653132,-2.819708,4.697479,1.155387,-2.492633,5.624592,3.166693,-3.589633,0.539280,-1.954541,6.374850,-4.493035,4.629257,-2.226553,4.274051,-1.841506,6.938135,-9.252245,-3.982027,8.556378,-3.071928,-7.124590,-0.613695,0.533546,8.462365,2.002165,5.013921,5.541629,-4.501434,1.234646,-6.099475,-4.746352,-6.048348,-4.989585,2.747033,7.902480,4.153758,5.351899,-8.347274,0.434587,-2.955388,-4.394202,8.567053,-3.896633,-2.972641,3.989248,7.425589,-3.128701,-5.826182,-4.642718,-6.486671,-1.331369,-0.682945,0.215336,-0.158344,-0.048043,5.672038,0.922785,-0.851266,-4.968564,1.325033,8.267164,-4.205258,-3.885920,-1.333966,-9.465715,6.483982,-9.582419,-2.224469,-9.665684,7.872656,-1.411004,-6.810748,5.259483,5.151127,4.843028,7.574952,-5.875174,-5.103025,5.870524,7.502037,1.863435,-6.925362,-8.188414,5.305990,8.043257,0.750556,6.798117,3.045110,-2.233083,-0.242139,5.739684,-1.144646,9.935461,2.271691,-3.000458,-8.623612,5.569162,7.989845,-3.025169,-7.968676,2.602147,6.757914,6.762584,3.543990,1.392414,2.021111,-1.055052,-9.360984,-6.237107,-4.672219,7.898291,-8.490635,1.161750,-2.396248,-4.871027,7.554927,6.337867,-7.083880,-3.672121,-2.934892,-0.322118,-8.204826,-0.496113,-2.818571,-8.960452,1.617764,-6.745751,-7.308595,9.977537,1.983290,-1.647657,-8.534859,5.967572,-3.013342,-6.720267,6.529969,0.381579,7.500482,2.427947,-0.761510,-2.281012,4.732231,-3.321613,-7.040303,-2.605672,4.992020,4.654080,-9.907757,8.578460,-7.925423,-0.008384,-6.742228,9.621722,3.419730,6.705576,6.041042,0.911761,-5.598762,-9.766760,5.824385,-4.473949,4.101410,-9.387050,-1.968870,8.276405,-6.693572,7.221582,7.457719,-1.746597,9.848028,-4.752723,-6.777729,0.481250,3.780513,5.018317,-3.157643,-9.691977,3.859004,-8.134302,-1.923693,-0.356604,2.374548,1.219891,3.025739,5.041920,4.315891,2.071380,8.533739,9.951177,-0.252198,9.271404,-2.922781,5.098724,1.283448,-4.673162,6.130628,-2.501255,-6.844955,9.249141,4.679750,-8.499230,-2.524661,-8.391821,-6.302022,6.313226,8.885578,0.557083,-2.923052,1.709010,-1.541672,6.537092,4.759327,-8.375397,0.915603,4.900482,-1.099047,0.056875,0.833836,-9.296595,0.334874,-6.394293,7.342172,3.773723,-4.718925,3.895359,-1.434779,-3.085833,-8.839914,4.779613,-9.097970,-7.436208,-7.897961,-2.930413,-2.050061,8.149704,-3.343530,-2.587345,4.863542,0.558737,-7.249779,8.964251,1.246150,-5.241015,-3.306232,0.303241,-0.771747,-9.367794,5.324625,-1.248659,6.409006,-8.382127,-3.457036,5.734014,-6.125428,0.728170,0.952694,0.583567,4.174731,-4.097241,4.708919,-0.933575,-2.268250,-2.762566,6.412093,1.668899,-9.890608,-0.821504,-4.080002,-1.699306,-3.241457,1.035475,-4.366206,-7.179734,3.732070,-7.263615,-7.324552,-4.445312,6.812760,8.161922,-5.916374,3.485166,-1.753084,9.177376,-7.570611,3.718309,1.019294,-8.266042,2.844447,6.818479,-4.584089,8.043229,8.160800,3.800613,-5.132603,3.618906,4.380191,7.660432,1.770854,-1.139464,-5.926528,-5.844159,-0.312759,-9.959033,-6.307057,-9.407651,3.197163,7.718991,-4.901114,2.589149,7.544749,1.759993,0.550090,-2.302682,0.116885,-3.312778,-3.812465,4.603435,-9.425014,-1.813724,-0.748654,0.689438,-6.248709,-9.174321,2.604493,4.489269,-6.173716,8.767558,5.345325,-8.923039,-8.477258,0.738527,-5.169744,8.731427], dtype = "float32")#candidate|6426|(560,)|const|float32
call_6425 = relay.TupleGetItem(func_2335_call(relay.reshape(const_6426.astype('float32'), [8, 70]), relay.reshape(const_6426.astype('float64'), [8, 70]), ), 0)
call_6427 = relay.TupleGetItem(func_2339_call(relay.reshape(const_6426.astype('float32'), [8, 70]), relay.reshape(const_6426.astype('float64'), [8, 70]), ), 0)
func_3680_call = mod.get_global_var('func_3680')
func_3682_call = mutated_mod.get_global_var('func_3682')
call_6428 = relay.TupleGetItem(func_3680_call(), 0)
call_6429 = relay.TupleGetItem(func_3682_call(), 0)
var_6430 = relay.var("var_6430", dtype = "uint16", shape = (980,))#candidate|6430|(980,)|var|uint16
bop_6431 = relay.bitwise_xor(const_6393.astype('uint64'), relay.reshape(var_6430.astype('uint64'), relay.shape_of(const_6393))) # shape=(980,)
output = relay.Tuple([call_6383,call_6392,var_6394,call_6401,call_6425,const_6426,call_6428,bop_6431,])
output2 = relay.Tuple([call_6384,call_6395,var_6394,call_6402,call_6427,const_6426,call_6429,bop_6431,])
func_6436 = relay.Function([var_6394,var_6430,], output)
mod['func_6436'] = func_6436
mod = relay.transform.InferType()(mod)
mutated_mod['func_6436'] = func_6436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6436_call = mutated_mod.get_global_var('func_6436')
var_6438 = relay.var("var_6438", dtype = "float64", shape = (1638,))#candidate|6438|(1638,)|var|float64
var_6439 = relay.var("var_6439", dtype = "uint16", shape = (980,))#candidate|6439|(980,)|var|uint16
call_6437 = func_6436_call(var_6438,var_6439,)
output = call_6437
func_6440 = relay.Function([var_6438,var_6439,], output)
mutated_mod['func_6440'] = func_6440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2030_call = mod.get_global_var('func_2030')
func_2032_call = mutated_mod.get_global_var('func_2032')
call_6508 = relay.TupleGetItem(func_2030_call(), 2)
call_6509 = relay.TupleGetItem(func_2032_call(), 2)
func_4754_call = mod.get_global_var('func_4754')
func_4757_call = mutated_mod.get_global_var('func_4757')
var_6512 = relay.var("var_6512", dtype = "float64", shape = (96,))#candidate|6512|(96,)|var|float64
call_6511 = func_4754_call(relay.reshape(var_6512.astype('float64'), [8, 2, 6]))
call_6513 = func_4754_call(relay.reshape(var_6512.astype('float64'), [8, 2, 6]))
func_2335_call = mod.get_global_var('func_2335')
func_2339_call = mutated_mod.get_global_var('func_2339')
var_6518 = relay.var("var_6518", dtype = "float32", shape = (560,))#candidate|6518|(560,)|var|float32
call_6517 = relay.TupleGetItem(func_2335_call(relay.reshape(var_6518.astype('float32'), [8, 70]), relay.reshape(var_6518.astype('float64'), [8, 70]), ), 0)
call_6519 = relay.TupleGetItem(func_2339_call(relay.reshape(var_6518.astype('float32'), [8, 70]), relay.reshape(var_6518.astype('float64'), [8, 70]), ), 0)
func_3040_call = mod.get_global_var('func_3040')
func_3041_call = mutated_mod.get_global_var('func_3041')
call_6524 = func_3040_call()
call_6525 = func_3040_call()
output = relay.Tuple([call_6508,call_6511,var_6512,call_6517,var_6518,call_6524,])
output2 = relay.Tuple([call_6509,call_6513,var_6512,call_6519,var_6518,call_6525,])
func_6534 = relay.Function([var_6512,var_6518,], output)
mod['func_6534'] = func_6534
mod = relay.transform.InferType()(mod)
mutated_mod['func_6534'] = func_6534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6534_call = mutated_mod.get_global_var('func_6534')
var_6536 = relay.var("var_6536", dtype = "float64", shape = (96,))#candidate|6536|(96,)|var|float64
var_6537 = relay.var("var_6537", dtype = "float32", shape = (560,))#candidate|6537|(560,)|var|float32
call_6535 = func_6534_call(var_6536,var_6537,)
output = call_6535
func_6538 = relay.Function([var_6536,var_6537,], output)
mutated_mod['func_6538'] = func_6538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3534_call = mod.get_global_var('func_3534')
func_3536_call = mutated_mod.get_global_var('func_3536')
call_6608 = relay.TupleGetItem(func_3534_call(), 1)
call_6609 = relay.TupleGetItem(func_3536_call(), 1)
uop_6621 = relay.sqrt(call_6608.astype('float64')) # shape=(4, 8, 14)
uop_6623 = relay.sqrt(call_6609.astype('float64')) # shape=(4, 8, 14)
output = uop_6621
output2 = uop_6623
func_6625 = relay.Function([], output)
mod['func_6625'] = func_6625
mod = relay.transform.InferType()(mod)
output = func_6625()
func_6626 = relay.Function([], output)
mutated_mod['func_6626'] = func_6626
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5469_call = mod.get_global_var('func_5469')
func_5471_call = mutated_mod.get_global_var('func_5471')
call_6665 = func_5469_call()
call_6666 = func_5469_call()
func_1487_call = mod.get_global_var('func_1487')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_6673 = func_1487_call()
call_6674 = func_1487_call()
output = relay.Tuple([call_6665,call_6673,])
output2 = relay.Tuple([call_6666,call_6674,])
func_6687 = relay.Function([], output)
mod['func_6687'] = func_6687
mod = relay.transform.InferType()(mod)
output = func_6687()
func_6688 = relay.Function([], output)
mutated_mod['func_6688'] = func_6688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5729_call = mutated_mod.get_global_var('func_5729')
call_6712 = relay.TupleGetItem(func_5727_call(), 2)
call_6713 = relay.TupleGetItem(func_5729_call(), 2)
output = relay.Tuple([call_6712,])
output2 = relay.Tuple([call_6713,])
func_6729 = relay.Function([], output)
mod['func_6729'] = func_6729
mod = relay.transform.InferType()(mod)
output = func_6729()
func_6730 = relay.Function([], output)
mutated_mod['func_6730'] = func_6730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1870_call = mod.get_global_var('func_1870')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_6857 = func_1870_call()
call_6858 = func_1870_call()
func_2836_call = mod.get_global_var('func_2836')
func_2840_call = mutated_mod.get_global_var('func_2840')
var_6862 = relay.var("var_6862", dtype = "float64", shape = (756,))#candidate|6862|(756,)|var|float64
const_6863 = relay.const([8.030351,4.516814,-1.556935,7.389795,-9.164853,-7.686485,0.924493,-2.582330,3.822727,-9.596257,6.052715,5.757609,2.853109,0.875795,3.777185,9.156948,6.676318,-1.296624,-2.256255,4.707829,-1.989861,-1.850602,9.936013,-0.270881,4.477826,5.445012,5.060173,-0.609411,1.328986,7.334422,1.987569,6.230682,-7.067226,-3.854728,3.647015,5.707041,-8.806629,6.667690,-2.493518,-6.154694,-2.210102,0.017077,-2.003980,1.373864,6.260462,-3.654043,3.045168,2.594353,7.472949,-2.209287,-4.106092,7.803940,4.004768,-0.964965,-9.525519,-1.133300,-4.956076,-4.399333,2.265666,1.082252,7.767434,6.651368,9.209802,-7.217126,6.713930,-4.668967,-6.391240,-5.917732,-5.644211,6.334635,5.731069,-7.057061,6.137159,-7.021411,-5.443100,0.135104,7.000953,-2.217313,-2.363870,-8.680988,8.362545,7.728767,-6.417473,-6.443396,-9.621651,1.015965,3.987493,-3.615848,0.586553,6.063446,-0.873795,8.545200,-3.068479,-6.097899,-3.026219,-8.065241,7.868848,3.968498,5.806591,9.350305,7.046266,5.482770,-3.035899,-3.229894,-7.951374,5.973106,-4.659748,-0.827647,-6.404516,4.201188,4.344064,-8.209814,4.646328,-2.803959,6.601055,7.908833,0.640137,9.966423,-7.163665,5.087635,-5.607294,5.174523,5.364399,5.445091,-8.905736,-6.542269,-4.982578,4.637534,-3.325471,-0.665541,6.440490,-6.863665,-9.786798,-4.197958,3.263156,9.843375,-7.839176,0.180469,-8.891108,7.361888,3.857593,2.023841,-8.912780,-0.668533,-2.995419,7.436445,-5.891376,-9.972081,4.228782,9.508578,-3.058717,-2.080298,6.958896,-8.612377,-8.004673,-9.787111,5.091055,1.908051,-8.765370,-4.013353,-4.660466,-1.930284,-2.225521,8.761406,7.514996,-5.282053,1.906011,-6.022830,-5.689577,8.026604,-8.645133,1.058899,6.899658,-3.378308,-4.364096,-0.681446,-3.133259,6.191774,-6.795649,-3.215073,5.848939,3.340747,-1.788370,3.500677,1.690949,7.912077,-1.760647,5.476120,-4.424064,-4.782226,1.136387,8.887599,2.226856,-8.482370,-0.408169,-5.286863,2.388006,-1.993470,6.269037,5.921126,-1.113979,9.412500,4.648100,-3.257324,-4.035052,-8.446775,-9.223052,5.370686,-9.704479,8.094726,-9.171488,-5.624495,4.880908,3.873711,-7.494276,9.024155,-2.545098,8.982682,-2.475672,4.674261,-6.881307,-5.906918,9.714976,1.800895,2.953508,-4.583380,-7.992176,9.207744,-4.098019,-0.055645,6.331612,9.059297,-6.872795,1.165006,4.028816,0.700827,-4.950319,-0.984377,3.605194,6.911506,-7.719032,5.985613,-7.463628,-3.769790,9.025430,8.450389,3.960465,-8.286098,-7.739872,-8.030510,-2.543174,6.269516,4.937387,6.623461,0.820257,2.792261,-5.780501,-9.318221,1.122280,6.078925,-8.119318,-8.340837,-2.419782,5.493532,-8.936278,-9.284752,-0.022222,-9.257722,0.140838,-3.933261,-4.605919,-0.101866,-1.669439,-8.691595,0.846976,1.161577,-1.043244,9.966285,-2.609020,8.193276,-8.472081,-2.898827,-5.175397,-6.538325,-1.267555,-6.823393,-9.340140,7.055085,-2.442788,4.165084,-2.630682,3.537582,-3.905128,8.237080,1.503967,7.711571,-2.119549,-8.645666,-7.580332,-1.141552,-4.663168,-2.411668,6.604422,4.534322,7.043049,7.497695,2.185873,-5.325940,-1.052888,0.843937,4.089865,8.621449,-9.362217,-6.890148,8.302982,1.234214,7.312609,-0.420517,1.473984,-7.228503,-9.354746,-3.897907,-6.926971,0.226713,-0.080779,5.701780,-1.125276,5.809583,-6.789203,0.869902,-5.545911,4.926721,-4.846143,-0.282963,-3.097395,-9.084995,5.102638,-7.123565,-7.360773,-4.994325,-1.345800,-0.781927,-3.045938,7.029043,5.983416,-4.493632,0.067940,1.738019,-3.954866,-6.384055,5.304426,6.920716,2.539310,-6.811362,-8.911375,8.081850,-2.657393,8.889435,6.240780,-5.483202,0.440815,3.699539,-1.749419,4.294144,-3.497526,3.043446,-3.603663,-9.540398,8.345959,8.274052,4.915501,-6.107154,-5.096784,7.195685,2.505478,-9.641331,-2.465804,9.595131,8.675173,3.026530,-7.344542,5.855904,-7.186323,5.358580,-8.221921,3.743874,1.943487,-3.621776,8.327808,3.862696,0.364139,9.903426,8.482446,-2.483009,5.097432,2.350755,6.470991,2.948920,-2.046599,6.720342,0.329636,0.537294,-3.239117,9.186562,9.840869,-2.661920,-2.968013,-0.522020,5.688941,-5.094857,2.569554,-4.108144,-9.975095,-5.792227,-3.905106,-2.869285,-7.380181,-4.975649,9.150858,-2.853618,6.263310,7.272427,-0.507413,2.545451,-7.853498,8.739559,9.496911,-5.952212,7.198823,3.503369,-0.050445,4.215860,9.129458,-8.058757,8.377047,5.844121,8.361938,9.811539,-0.791063,4.658399,-4.843379,-1.125599,9.495894,-1.917071,1.087478,-2.465138,7.551095,-2.827056,-2.479588,1.765073,9.337276,-9.118160,7.933319,2.098199,-2.086630,-8.594690,7.760025,1.930061,-1.406736,9.398687,7.138741,7.985336,5.802324,1.313020,-7.993539,-0.822955,2.876754,4.235846,-2.401901,-0.327528,1.724740,6.331387,-8.899494,2.676561,-0.177992,-1.169405,4.293974,-7.324176,-6.373863,-9.779452,-5.791233,-1.235803,0.780390,-0.500126,-2.089808,-4.115003,-0.542867,-9.836006,-1.715261,4.256661,-8.078495,-3.823259,4.594927,5.664406,-3.818088,7.542402,-0.579448,-5.540914,4.235357,8.111954,-7.644860,7.127652,8.270519,1.963267,-9.926853,7.199393,-1.767852,-3.792036,-5.097046,6.377434,3.452225,-5.462927,8.636277,5.838451,9.183733,-6.523807,-1.584640,-6.611290,-7.835476,-3.697681,-8.734291,5.461938,0.749038,6.678754,6.268898,1.192853,7.667736,-9.064763,-4.358335,4.639257,-6.010901,4.959497,8.690875,7.514138,7.270918,-3.404424,0.890454,5.046300,6.297406,-4.692212,4.108525,7.670649,9.009147,3.164599,4.490804,-4.748813,2.664071,5.314148,5.377696,-1.591320,-4.637244,4.978256,-9.418101,-4.370571,9.186105,5.742813,-2.427888,0.740704,-2.963534,-3.244337,7.004751,-7.701179,-6.926182,3.829858,-9.436999,2.328529,3.856711,-4.162388,2.720219,4.631009,5.934447,3.545626,-5.629926,-0.626845,-6.030861,-2.851912,9.747393,-2.479297,-1.164698,9.545060,4.029258,2.584624,6.733620,-5.394366,6.431764,1.631363,-8.812052,-2.375756,4.936104,-2.106055,3.506325,5.361336,6.341732,1.135698,-0.235323,-9.128220,3.413906,-1.874914,8.216468,5.069368,-4.615641,6.728046,0.367935,3.658250,-8.737487,-2.423437,6.373477,-8.399988,7.275809,-2.281819,7.793439,8.390936,5.183525,3.245541,9.960277,0.894647,-1.472981,-0.744992,-4.058632,-5.095210,6.506344,7.506654,3.342215,2.290739,5.702788,-3.647904,-2.437005,4.835810,7.820329,-2.996661,8.593476,-2.147751,2.215389,0.691847,3.821645,-6.442707,4.461140,9.980745,-9.914009,0.736511,-7.762769,-0.782397,-9.449440,-8.153881,-9.241035,-8.955482,-8.437138,6.453393,6.783021,-5.903333,6.950340,-4.769806,-2.965699,7.270881,-5.539477,-1.253522,-3.821313,-9.668708,-3.205932,-0.159340,7.132601,-6.199916,8.889673,9.335859,-4.379133,4.932165,8.801454,-4.012329,4.310389,-6.010919,4.749466,7.012763,8.480605,-5.566864,-7.447533,-1.847419,3.878892,-2.577096,0.268176,9.917781,2.841634,5.034805,-7.714170,-5.886476,6.900375,-9.499190,3.301550,-1.771839,1.300935,-7.310662,3.114247,0.033394,5.463755,1.127920,-2.240050,-5.244035,-2.527167,-2.866329,-5.615925,-5.934214,2.807951,-9.309284,-2.082525,3.785764,3.015927,-3.261821,-4.622752,1.536883,7.388955,-8.537887,8.701880,0.638173,-4.826276,5.526223,-5.457894,-5.095270,-5.996043,-2.632762,7.004009,-8.180876,9.347256,5.198555,-2.748476,3.152676,-1.736029,0.922610,-3.043495,4.812577,-4.110713,4.472132,-2.223050,-9.639000,-8.597609,-4.794048,-6.691630,-7.510710,0.532834,-3.188388,-3.395614,3.981005,7.163352,5.751165,3.944506,3.865755,9.270577,-0.708849,-1.936380,-4.163333,5.993231,6.958623,4.527515,0.779058,8.472825,-2.888970,7.829761,-6.522194,8.509371,-7.104888,-1.550202,-8.646160,4.415394,-9.337032,-5.495522,-4.950029,1.601886,8.040071,-2.184345,8.325132,-0.190728,6.407921,6.594529,1.143252,5.185429,4.421610,8.306562,9.106803,-8.092833,-9.118281,-7.895382,-8.511127,-5.294937,-2.356882,-4.097829,8.004680,-3.426696,-8.199747,-4.452363,-4.597932,5.802987,-6.612332,7.900278,8.052858,2.116160,-0.388380,3.237243,4.840948,8.858166,-4.054992,1.346710,-2.657708,-4.294835,4.319142,-2.120312,8.121770,8.180235,-3.443452,9.436091,-9.242562,-8.004602,7.689744,2.124833,2.365939,-8.856903,-0.565538,2.793424,2.353491,6.608340,8.512176,-6.015973,5.358606,-9.838005,1.824404,-1.879623,-6.778085,-6.508635,-7.168198,-3.944217,-9.727724,9.425648,-8.951088,-0.749121,-5.576533,-9.122922,0.406386,-2.783589,-7.159932,4.626528,3.995323,6.100695,-8.464297,5.239867,7.193674,-9.991326,-4.525021,-3.174421,0.755843,3.950393,-3.575884,8.358821,-6.517381,-5.202446,-6.806345,-6.046724,0.267165,2.130888,-8.688620,-1.190803,-0.628190,2.299610,-0.078485,0.881987,-0.092867,-0.348015,-7.284001,5.682833,7.416411,2.182801,2.433885,2.734063,4.929260,-1.334907,5.548908,6.774131,9.806450,9.319985,-2.548543,9.384919,2.296780,3.633740,7.383063,-1.186833,-9.913420,-4.544263,-6.196440,5.639913,-4.995226,4.161237,-2.787135,3.882988,0.550933,-0.531525,6.477246,1.262291,5.550083,-7.976036,9.276213,1.141383,-3.718733,2.012117,-4.276375,-1.158453,-7.428727,-1.738402,-6.633885,-2.685163,-7.511162,6.383872,6.528228,-6.652659,0.127799,5.765828,-6.847266,3.379859,5.428855,8.809996,8.109576,-1.681665,3.199351,-4.088606,7.951035,6.181336,6.789350,1.690839,6.235701,7.657737,3.863630,1.071980,-0.003738,-1.723607,4.270503,0.862226,-4.148493,-4.513012,-7.191874,2.103645,-8.851305,-5.506508,-2.365340,-2.395398,2.737727,-9.914780,-4.639840,-8.796738,-7.897602,-5.975155,-7.878390,-2.340861,-5.725843,-2.600886,-8.549604,-7.383916,2.867220,-7.425223,-0.141684,5.828241,8.281169,-2.060863,-8.938040,-1.503137,-1.375639,-0.851586,-5.199974,5.827704,-9.324243,4.320415,1.326381,5.274084,-1.335485,-3.337352,-1.046476,6.701421,-8.242168,8.177129,-4.117819,3.280827,4.592744,-2.722088,7.862053,-9.620335,5.721016,-9.806027,6.754431,1.327029,8.249592,-2.810085,-8.504202,4.473111,-2.796809,0.214655,-0.024091,9.047722,-7.957229,4.739861,9.990337,4.257125,-8.706964,6.870037,5.028476,8.606714,1.144649,-7.279932,1.534066,-7.648146,0.454948,8.468899,-1.271725,5.300163,-7.146801,-3.579020,-5.004086,-8.925741,5.065829,-6.360899,5.120654,-9.446095,6.111457,-6.652782,-9.871335,-8.688737,-6.518326,-0.828122,-8.299448,8.223018,-8.824351,-0.766255,-0.779354,6.277961,3.775584,-3.540605,-9.746435,4.039319,-5.991678,-7.185183,-2.511242,-3.548527,-1.403778,6.018770,-4.627832,7.496267,4.391377,1.041409,3.085328,2.560996,-8.583344,0.487872,-4.672002,-3.612679,-8.286342,-1.552453,-4.144103,5.885032,2.799569,8.273761,3.341878,-2.871701,7.424199,-6.660100,0.350233,5.339210,-5.949200,-4.915031,5.178563,6.646564,9.941959,-2.858797,-6.626868,5.947529,-6.002100,8.366649,1.473620,-1.476300,4.081793,5.789907,6.360002,-0.444201,0.250343,-1.389430,6.541745,-7.392530,1.418464,-4.056290,-3.600051,8.870883,6.646061,5.003302,8.552078,9.759779,-8.449760,6.968724,6.895937,1.958563,-2.707140,7.639251,8.590330,-4.542643,-2.139246,-8.469188,-4.050454,8.414683,-3.705290,1.920283,4.214339,-5.254209,5.050458,6.828448,2.015441,-7.364709,-1.296848,-5.926489,2.441559,2.514060,8.836501,5.429353,0.939692,5.654301,5.532737,6.917998,4.666208,-9.835885,4.292731,5.710283,2.521112,-1.715362,9.639050,4.724352,-3.036573,-9.409320,0.798283,1.244584,1.341187,-0.497208,7.078138,3.870135,-0.386828,-7.868363,1.117373,-6.432114,5.385905,-9.196129,1.175040,8.658984,-3.422827,-4.176806,3.053770,7.509372,-2.677840,0.388604,0.632923,7.046680,6.276595,-6.927670,4.586415,4.940198,2.977810,-0.325940,7.531125,-9.894663,7.174173,9.365000,3.074437,5.688127,9.713976,6.700888,2.482539,-4.524657,-3.949350,7.331182,9.082830,-2.700100,0.473304,-3.500275,1.041318,-5.886566,6.005537,4.269185,-6.670292,-3.895560,-0.345506,1.853648,-8.246255,-6.482246,-5.627099,0.290909,-9.382193,-7.825167,-1.152979,-7.841991,-6.382950,-5.526727,7.246004,-5.296440,7.558748,8.710552,-3.226013,9.161296,-2.336097,-0.511087,-7.451938,-9.578775,5.196464,-3.474926,7.814191,2.603917,3.110688,1.467692,-7.073792,2.422484,2.722972,3.711702,4.559204,-9.899271,-0.892924,-0.136097,-9.869359,0.699945,3.918193,3.057244,-4.466226,-4.065513,0.530226,-9.934918,7.427492,3.966210,-4.600866,7.723009,2.441107,7.936226,-1.182235,-5.653166,5.414916,-9.573187,7.217700,6.485281,4.583102,-7.148213,-7.232184,-0.273265,-2.388791,-1.075803,-6.798540,-6.013515,8.886979,1.456417,9.477403,7.613618,8.916845,9.391158,8.292971,-5.299442,6.138964,2.704032,-8.160139,5.061107,8.956868,6.650648,6.502299,-2.069212,-3.269290,-7.212753,7.941994,-7.842526,-3.763658,-4.221934,-0.310055,-5.257059,6.015311,0.934809,3.162773,-9.830034,-1.964289,-1.301739,8.840701,7.482140,-4.221568,6.031198,2.038705,-6.626866,9.120603,9.251034,3.127518,0.204471,-5.044634,-4.222254,-4.736763,-7.016544,7.338259,-7.798958,7.117860,-7.099451,-8.481118,-4.245725,1.384048,4.580455,9.678676,-4.429079,-9.634310,0.564560,4.707528,-4.390689,-6.681578,-2.558015,2.220991,-8.163260,-1.817483,-9.731600,-6.209236,-4.238551,3.317504,-8.187113,4.244366,0.084971,5.669935,-3.360801,4.194811,-6.702426,6.228928,3.256707,4.579898,-7.425953,-3.442415,-4.591692,7.807249,-7.846639,-1.454359,0.035311,9.979850,1.416005,9.360907,8.660924,-9.842289,-1.783337,4.838010,-5.967333,3.182775,-8.982793,1.790008,-5.529548,-7.744031,3.787052,9.291217,-7.854585,-9.175848,8.892016,1.606516,-9.403607,-2.885849,7.860280,-3.071899,2.126726,-7.944339,0.240888,-8.576143,-5.492445,-2.743267,-4.150454,-3.631128,-7.428576,-3.705768,-3.525548,4.471111,-1.227297,1.399873,7.919768,3.762797,2.839326,-6.836501,-4.014041,-3.940282,0.356654,-4.035732,7.052078,-7.392820,7.532417,4.486798,-2.388937,-8.219572,5.068368,8.978825,9.443394,9.250832,-8.216896,0.993363,-1.575845,-8.590393,-8.981155,1.860293,9.596755,-1.715648,0.938464,7.716139,-0.446351,-8.310594,2.507999,-8.574593,-6.632508,-2.020368,6.112497,9.302594,7.072637,-0.162993,5.664500,2.874203,2.438771,8.470838,-0.398325,4.332759,5.575238,-0.934368,5.267971,4.078951,-1.449778,-5.607947,-1.428670,5.447630,7.139860,4.985563,-7.779292,-2.548692,-2.396881,-4.124867,-2.857666,3.640220,5.287208,-6.465233,-2.344242,-1.769639,6.839229,2.488129,2.179263,-7.965444,-5.190828,7.436514,-5.270362,-9.587554,5.200912,1.189695,-6.492630,2.200976,-3.134215,-8.889412,-9.099624,4.748944,-9.335052,8.331347,-5.308209,-7.077437,1.221877,0.647731,9.490954,0.876849,-7.283738,-6.307404,1.102125,-3.174291,-5.607261,7.577136,5.421090,-9.735617,1.965943,3.691548,6.202208,-6.447144,6.920060,6.738546,2.239750,-0.225071,6.528433,0.002651,-7.881033,9.252452,-7.309105,8.959088,3.354201,1.587052,2.026983,-5.423532,2.561149,-1.573631,-1.336257,7.982939,-8.742218,4.179983,7.444786,-4.195046,-9.337424,-1.143517,-2.924770,3.746982,5.300724,-6.421704,0.062769,-3.860374,8.134816,-5.610668,-9.583385,-9.944141,4.470868,-2.048509,-4.600372,-5.769429,-0.673601,3.228910,5.258863,0.950186,-9.265023,4.657416,-1.117140,-4.908874,-7.554283,-7.049020,-3.125528,6.628796,-5.879517,-9.668683,9.228876,-8.382758,3.487017,-3.575653,-5.523188,-6.745747,-2.688534,-6.380900,4.607736,-5.367742,2.850614,-4.856785,3.327448,8.090618,0.584497,-0.994776,5.726003,7.923405,5.095899,0.519629,3.226000,-3.534304,6.878724,-9.977577,6.803062,9.671435,4.073077,-3.950374,3.774831,8.623808,-9.995296,3.582386,-6.567884,-6.344792,2.434818,6.997046,2.153704,-8.630435,-0.672114,4.340319,3.677842,7.972623,-0.679533,-1.769674,4.626853,4.985943,4.026638,3.918541,0.165901,9.409820,1.951554,1.738133,-3.634985,-0.498298,-8.640678,-1.665616,-6.733643,8.070362,-2.010537,-8.585695,3.730336,0.980211,9.599979,-4.843833,-5.183158,4.338776,-9.050623,6.907507,-2.491576,5.676423,5.087292,-2.278234,5.547530,9.964519,2.988344,-8.748361,7.400074,-0.641354,-5.113942,4.559743,-8.990985,7.904072,2.168364,-2.657599,-5.751933,-0.932935,2.487790,4.935719,-1.424770,-5.125958,-5.134301,-7.376330,-6.985550,-6.706235,9.817085,-3.793390,-4.902876,-4.759441,-8.726376,9.979596,1.662847,-8.061526,8.912784,1.456692,-7.665940,6.717705,-9.956555,-3.972978,-2.856186,-8.439601,-0.987060,-1.653216,-0.875023,-4.033564,9.450982,2.489266,-9.473923,5.907554,4.860950,2.049351,2.856255,-9.635252,4.645111,-5.574224], dtype = "float64")#candidate|6863|(1638,)|const|float64
call_6861 = relay.TupleGetItem(func_2836_call(relay.reshape(var_6862.astype('float64'), [7, 9, 12]), relay.reshape(const_6863.astype('float64'), [1638,]), ), 2)
call_6864 = relay.TupleGetItem(func_2840_call(relay.reshape(var_6862.astype('float64'), [7, 9, 12]), relay.reshape(const_6863.astype('float64'), [1638,]), ), 2)
uop_6870 = relay.tan(call_6861.astype('float64')) # shape=(1638,)
uop_6872 = relay.tan(call_6864.astype('float64')) # shape=(1638,)
func_2995_call = mod.get_global_var('func_2995')
func_2997_call = mutated_mod.get_global_var('func_2997')
call_6873 = relay.TupleGetItem(func_2995_call(), 0)
call_6874 = relay.TupleGetItem(func_2997_call(), 0)
output = relay.Tuple([call_6857,var_6862,const_6863,uop_6870,call_6873,])
output2 = relay.Tuple([call_6858,var_6862,const_6863,uop_6872,call_6874,])
func_6883 = relay.Function([var_6862,], output)
mod['func_6883'] = func_6883
mod = relay.transform.InferType()(mod)
mutated_mod['func_6883'] = func_6883
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6884 = relay.var("var_6884", dtype = "float64", shape = (756,))#candidate|6884|(756,)|var|float64
func_6883_call = mutated_mod.get_global_var('func_6883')
call_6885 = func_6883_call(var_6884)
output = call_6885
func_6886 = relay.Function([var_6884], output)
mutated_mod['func_6886'] = func_6886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6926 = relay.var("var_6926", dtype = "float32", shape = (12, 6, 16))#candidate|6926|(12, 6, 16)|var|float32
uop_6927 = relay.erf(var_6926.astype('float32')) # shape=(12, 6, 16)
bop_6929 = relay.power(uop_6927.astype('float64'), relay.reshape(var_6926.astype('float64'), relay.shape_of(uop_6927))) # shape=(12, 6, 16)
output = relay.Tuple([bop_6929,])
output2 = relay.Tuple([bop_6929,])
func_6932 = relay.Function([var_6926,], output)
mod['func_6932'] = func_6932
mod = relay.transform.InferType()(mod)
mutated_mod['func_6932'] = func_6932
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6933 = relay.var("var_6933", dtype = "float32", shape = (12, 6, 16))#candidate|6933|(12, 6, 16)|var|float32
func_6932_call = mutated_mod.get_global_var('func_6932')
call_6934 = func_6932_call(var_6933)
output = call_6934
func_6935 = relay.Function([var_6933], output)
mutated_mod['func_6935'] = func_6935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5871_call = mod.get_global_var('func_5871')
func_5873_call = mutated_mod.get_global_var('func_5873')
call_6942 = relay.TupleGetItem(func_5871_call(), 1)
call_6943 = relay.TupleGetItem(func_5873_call(), 1)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_6956 = relay.TupleGetItem(func_1608_call(), 1)
call_6957 = relay.TupleGetItem(func_1610_call(), 1)
func_6356_call = mod.get_global_var('func_6356')
func_6357_call = mutated_mod.get_global_var('func_6357')
call_6972 = relay.TupleGetItem(func_6356_call(), 1)
call_6973 = relay.TupleGetItem(func_6357_call(), 1)
func_5368_call = mod.get_global_var('func_5368')
func_5370_call = mutated_mod.get_global_var('func_5370')
const_6976 = relay.const([-5.906043,-3.340165,-8.577155,6.216270,-8.135796,-6.691606,7.820721,0.510278,8.925114,7.093012,9.543070,-7.639731,1.552406,4.507916,2.600553,8.631168,-1.741288,-3.672460,-6.156757,-3.092431,4.190199,8.954011,-4.780948,-9.364927,-3.022323,-1.666321,-2.818025,8.158714,3.955644,9.190725,6.678968,-4.830902,-4.919195,-2.997083,-6.453317,0.641326,4.063902,7.691742,-2.634941,6.448117,1.708808,-0.846888,3.267074,-0.945186,-1.799633,8.260154,-3.952798,-4.176160,7.714794,2.907460,6.713944,4.071358,-4.611768,-5.267239,-0.573466,6.791026,-6.487474,-5.530514,3.718482,-1.707170], dtype = "float32")#candidate|6976|(60,)|const|float32
call_6975 = relay.TupleGetItem(func_5368_call(relay.reshape(const_6976.astype('float32'), [60, 1])), 3)
call_6977 = relay.TupleGetItem(func_5370_call(relay.reshape(const_6976.astype('float32'), [60, 1])), 3)
func_5988_call = mod.get_global_var('func_5988')
func_5992_call = mutated_mod.get_global_var('func_5992')
var_6983 = relay.var("var_6983", dtype = "bool", shape = ())#candidate|6983|()|var|bool
var_6984 = relay.var("var_6984", dtype = "bool", shape = (4, 120))#candidate|6984|(4, 120)|var|bool
call_6982 = func_5988_call(relay.reshape(var_6983.astype('bool'), []), relay.reshape(var_6984.astype('bool'), [15, 2, 16]), )
call_6985 = func_5988_call(relay.reshape(var_6983.astype('bool'), []), relay.reshape(var_6984.astype('bool'), [15, 2, 16]), )
func_6200_call = mod.get_global_var('func_6200')
func_6202_call = mutated_mod.get_global_var('func_6202')
var_6995 = relay.var("var_6995", dtype = "int8", shape = (2640,))#candidate|6995|(2640,)|var|int8
call_6994 = relay.TupleGetItem(func_6200_call(relay.reshape(var_6995.astype('int8'), [2640,])), 2)
call_6996 = relay.TupleGetItem(func_6202_call(relay.reshape(var_6995.astype('int8'), [2640,])), 2)
func_6534_call = mod.get_global_var('func_6534')
func_6538_call = mutated_mod.get_global_var('func_6538')
var_7000 = relay.var("var_7000", dtype = "float64", shape = (96,))#candidate|7000|(96,)|var|float64
const_7001 = relay.const([-3.568350,3.539058,-5.087164,4.531326,3.363918,3.157903,6.287173,7.895893,8.442019,-2.820799,2.097406,3.578998,7.505588,8.186241,7.290307,3.962614,-7.973474,-4.259319,-5.283246,-4.157813,9.786703,8.416908,-1.312067,9.994108,-4.076815,3.063202,1.094975,-7.045588,6.726449,5.159867,4.179804,-9.296961,8.028231,-1.277247,5.711619,-2.293577,-7.288045,0.313540,-8.340247,-1.435030,-4.987020,0.179296,7.404875,-5.230420,2.131293,0.309279,-4.549076,-4.632507,-2.185425,8.004961,1.447392,-3.347940,1.683375,4.751036,3.829115,-8.688696,9.930199,3.119447,2.931488,5.476367,9.953254,4.369127,-9.102171,-1.212036,1.624648,-4.396641,3.179451,-7.070417,-4.525468,-4.191825,-3.436641,0.357033,-4.601887,-1.912643,-4.487448,7.504974,-4.824066,6.739443,-2.862426,5.729486,3.479201,6.993977,-2.301942,8.276633,9.796443,-4.530015,0.067873,8.073465,-5.622153,0.460022,8.748248,9.155725,-8.565972,-5.815027,-1.865759,-2.616444,-1.773204,-6.663720,8.600545,9.339554,0.189850,-4.522583,-7.571653,1.679269,0.550651,7.967829,5.144960,-1.405360,-4.675923,-7.911216,-8.478352,-1.740224,-4.749357,-9.679451,5.709026,-3.570328,1.799578,9.109652,-2.620821,3.234497,5.782880,-7.157149,9.710674,-9.361138,-8.261312,-8.860515,0.876958,4.543475,0.905026,-4.049341,5.775905,8.742166,9.613027,-5.771391,2.091245,-1.235676,1.338713,3.902037,2.782665,-1.129944,7.935443,5.253750,3.927081,-7.881765,-7.604834,7.554965,-4.664828,-5.799910,5.579605,0.208757,-7.382615,-9.815848,5.759303,-2.932174,8.497643,-1.553557,8.415341,-9.078741,-6.006953,9.704550,9.718562,-8.401497,-4.856341,5.557145,-4.519805,-8.699779,-5.804144,-2.873827,7.730327,0.417284,9.713194,3.658895,5.647875,9.627733,-1.256963,-5.221255,-5.416935,7.528274,2.952122,-7.846969,-4.210274,0.417795,9.529833,-6.497747,-9.341189,-6.201553,3.177539,2.623072,4.072180,-1.638985,8.968409,4.675898,9.526443,-0.920526,1.989932,-4.260099,-4.002749,3.650841,6.641704,-6.172863,0.457702,0.919750,-1.334223,9.024636,-2.066249,5.380893,-4.438079,9.645716,-6.219085,-3.724889,-9.131408,3.186754,-7.889649,8.195820,-0.762905,-4.707524,-5.809059,-0.699494,-8.916834,-0.148109,0.140368,-1.209059,-5.992303,3.714282,-7.271826,-7.468217,3.294966,0.168741,-5.254928,9.748458,-2.676791,-3.366618,-4.133478,4.641730,-5.309819,7.382543,9.143990,0.259638,7.756626,-5.453800,7.806483,-2.124396,-1.979255,-8.846394,-6.894285,8.470796,1.656411,0.649976,-8.785748,-0.438289,-1.188040,-6.256451,-3.335896,5.977056,3.769844,2.467087,3.536427,4.014579,8.107956,-3.477485,0.920033,-1.097782,-4.094604,-5.573636,-1.973478,9.220820,-5.028229,-9.885297,-1.656801,-8.640672,-1.705028,-9.557167,-5.118471,9.702654,7.685681,7.124999,-8.983087,-2.927094,-2.271345,0.058109,8.953197,4.733233,6.638055,-2.910786,-3.203407,5.659698,-2.932993,-0.465102,1.933079,-0.672274,8.066345,6.431582,6.884386,-4.919759,9.418950,-1.551935,0.344570,-7.908488,-2.124098,-1.281209,-4.410635,6.553880,2.047758,9.884259,0.891142,1.072511,9.673305,-5.388558,-0.911115,-1.115509,1.920505,4.218037,9.158830,2.486424,-9.254723,-3.371195,8.159956,-0.771494,3.877072,5.049555,3.873647,1.087559,5.548608,-5.100230,5.271484,9.996853,9.045760,0.659899,8.970050,-3.856962,-9.167497,-6.897275,-7.905816,-0.894375,-0.070121,6.804126,-8.295225,-0.207065,-6.900421,-4.931329,-1.657574,-6.997336,-7.428776,-7.319412,-6.032694,8.645139,2.586383,-9.856555,-4.387604,0.379305,-5.247489,6.984869,4.864161,6.723037,-2.314323,6.209153,0.897931,-1.963424,7.190184,4.590993,-7.271000,-2.001178,-7.702864,3.401365,4.137051,5.633179,3.878982,5.588950,5.825744,9.994770,-7.643432,-3.264731,-8.140316,8.941414,6.081840,-6.202607,8.048422,6.708606,5.277761,5.010514,3.116106,8.350854,0.985842,9.072849,5.187486,-5.674978,-5.598481,3.833040,9.369371,-9.379484,-1.200647,-0.802195,-0.886414,8.616664,8.677358,-2.612057,-2.663764,3.728489,-5.077108,-1.030244,2.111146,4.432394,1.363887,3.726790,4.798729,3.926627,-8.457328,-0.444399,1.304198,-1.721917,-2.371786,6.655989,-0.017027,-8.725502,3.402558,-1.668176,5.823243,-6.360852,3.339914,6.720998,-7.131050,-9.619154,5.675663,9.103514,-8.213180,5.577735,-4.928725,5.958607,8.320859,-0.131403,-2.690707,-4.008451,-3.065881,-6.428808,-4.572454,4.115713,-2.766712,4.843461,-9.252870,-7.420079,-1.009329,5.409905,-6.035383,-7.589026,-2.080487,2.877861,8.119245,-5.291402,-7.320431,1.403856,-7.606507,4.679730,-4.353491,-9.259677,3.112630,-1.688385,-8.057311,8.813688,-6.628625,0.688104,-0.671405,-1.911140,-9.979996,8.721310,2.710287,5.589710,5.762422,8.499726,2.793362,-7.418003,-5.778817,-6.680095,-8.268015,-2.269246,6.858663,0.799505,-5.255551,-6.899955,-1.124707,4.656796,-5.994842,-7.853974,-5.909718,-9.446219,3.643661,-6.713722,6.496043,4.961330,-1.965148,-0.477185,3.966902,2.550923,7.530242,-2.745400,-1.470751,-5.466333,-6.263767,-0.661453,-7.427051,-3.675298,-2.973575,6.689927,6.489157,2.994801,-6.736516,-6.365041,-9.554181,8.034442,9.898980,4.410389,-9.306805,-9.291182,-9.157961,0.394339,0.776045,8.056664,-0.925499,3.310928,2.315720,-4.132684,9.996180,8.433694,-6.624702,4.279549,-8.668648,3.813115,-8.645646,6.527489,0.174953,9.755539,-3.548163,-1.970428,-0.677114,-5.558860,-2.575646,7.423184,3.299678,1.974225,-6.326366,1.279661,-1.453988,2.647798,9.013760,2.154205,1.990969,7.457593,6.751552,-4.393248,-7.244801,5.697413,3.145982,-9.180012,7.941167,1.866743,-2.729939,-9.995991,4.557031,-7.858534,-1.580985,1.821642], dtype = "float32")#candidate|7001|(560,)|const|float32
call_6999 = relay.TupleGetItem(func_6534_call(relay.reshape(var_7000.astype('float64'), [96,]), relay.reshape(const_7001.astype('float32'), [560,]), ), 1)
call_7002 = relay.TupleGetItem(func_6538_call(relay.reshape(var_7000.astype('float64'), [96,]), relay.reshape(const_7001.astype('float32'), [560,]), ), 1)
output = relay.Tuple([call_6942,call_6956,call_6972,call_6975,const_6976,call_6982,var_6983,var_6984,call_6994,var_6995,call_6999,var_7000,const_7001,])
output2 = relay.Tuple([call_6943,call_6957,call_6973,call_6977,const_6976,call_6985,var_6983,var_6984,call_6996,var_6995,call_7002,var_7000,const_7001,])
func_7011 = relay.Function([var_6983,var_6984,var_6995,var_7000,], output)
mod['func_7011'] = func_7011
mod = relay.transform.InferType()(mod)
var_7012 = relay.var("var_7012", dtype = "bool", shape = ())#candidate|7012|()|var|bool
var_7013 = relay.var("var_7013", dtype = "bool", shape = (4, 120))#candidate|7013|(4, 120)|var|bool
var_7014 = relay.var("var_7014", dtype = "int8", shape = (2640,))#candidate|7014|(2640,)|var|int8
var_7015 = relay.var("var_7015", dtype = "float64", shape = (96,))#candidate|7015|(96,)|var|float64
output = func_7011(var_7012,var_7013,var_7014,var_7015,)
func_7016 = relay.Function([var_7012,var_7013,var_7014,var_7015,], output)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1396_call = mod.get_global_var('func_1396')
func_1397_call = mutated_mod.get_global_var('func_1397')
call_7051 = relay.TupleGetItem(func_1396_call(), 0)
call_7052 = relay.TupleGetItem(func_1397_call(), 0)
output = relay.Tuple([call_7051,])
output2 = relay.Tuple([call_7052,])
func_7072 = relay.Function([], output)
mod['func_7072'] = func_7072
mod = relay.transform.InferType()(mod)
mutated_mod['func_7072'] = func_7072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7072_call = mutated_mod.get_global_var('func_7072')
call_7073 = func_7072_call()
output = call_7073
func_7074 = relay.Function([], output)
mutated_mod['func_7074'] = func_7074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4190_call = mod.get_global_var('func_4190')
func_4191_call = mutated_mod.get_global_var('func_4191')
call_7135 = relay.TupleGetItem(func_4190_call(), 0)
call_7136 = relay.TupleGetItem(func_4191_call(), 0)
output = relay.Tuple([call_7135,])
output2 = relay.Tuple([call_7136,])
func_7148 = relay.Function([], output)
mod['func_7148'] = func_7148
mod = relay.transform.InferType()(mod)
output = func_7148()
func_7149 = relay.Function([], output)
mutated_mod['func_7149'] = func_7149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4174_call = mod.get_global_var('func_4174')
func_4175_call = mutated_mod.get_global_var('func_4175')
call_7225 = relay.TupleGetItem(func_4174_call(), 0)
call_7226 = relay.TupleGetItem(func_4175_call(), 0)
output = call_7225
output2 = call_7226
func_7239 = relay.Function([], output)
mod['func_7239'] = func_7239
mod = relay.transform.InferType()(mod)
output = func_7239()
func_7240 = relay.Function([], output)
mutated_mod['func_7240'] = func_7240
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7249 = relay.var("var_7249", dtype = "float32", shape = (8, 5, 3))#candidate|7249|(8, 5, 3)|var|float32
uop_7250 = relay.sin(var_7249.astype('float32')) # shape=(8, 5, 3)
bop_7254 = relay.mod(uop_7250.astype('float32'), relay.reshape(var_7249.astype('float32'), relay.shape_of(uop_7250))) # shape=(8, 5, 3)
uop_7260 = relay.acos(uop_7250.astype('float32')) # shape=(8, 5, 3)
output = relay.Tuple([bop_7254,uop_7260,])
output2 = relay.Tuple([bop_7254,uop_7260,])
func_7275 = relay.Function([var_7249,], output)
mod['func_7275'] = func_7275
mod = relay.transform.InferType()(mod)
mutated_mod['func_7275'] = func_7275
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7276 = relay.var("var_7276", dtype = "float32", shape = (8, 5, 3))#candidate|7276|(8, 5, 3)|var|float32
func_7275_call = mutated_mod.get_global_var('func_7275')
call_7277 = func_7275_call(var_7276)
output = call_7277
func_7278 = relay.Function([var_7276], output)
mutated_mod['func_7278'] = func_7278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3617_call = mod.get_global_var('func_3617')
func_3618_call = mutated_mod.get_global_var('func_3618')
call_7311 = relay.TupleGetItem(func_3617_call(), 0)
call_7312 = relay.TupleGetItem(func_3618_call(), 0)
output = relay.Tuple([call_7311,])
output2 = relay.Tuple([call_7312,])
func_7330 = relay.Function([], output)
mod['func_7330'] = func_7330
mod = relay.transform.InferType()(mod)
mutated_mod['func_7330'] = func_7330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7330_call = mutated_mod.get_global_var('func_7330')
call_7331 = func_7330_call()
output = call_7331
func_7332 = relay.Function([], output)
mutated_mod['func_7332'] = func_7332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5957_call = mod.get_global_var('func_5957')
func_5958_call = mutated_mod.get_global_var('func_5958')
call_7358 = func_5957_call()
call_7359 = func_5957_call()
func_2879_call = mod.get_global_var('func_2879')
func_2881_call = mutated_mod.get_global_var('func_2881')
call_7374 = relay.TupleGetItem(func_2879_call(), 0)
call_7375 = relay.TupleGetItem(func_2881_call(), 0)
output = relay.Tuple([call_7358,call_7374,])
output2 = relay.Tuple([call_7359,call_7375,])
func_7383 = relay.Function([], output)
mod['func_7383'] = func_7383
mod = relay.transform.InferType()(mod)
output = func_7383()
func_7384 = relay.Function([], output)
mutated_mod['func_7384'] = func_7384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6729_call = mod.get_global_var('func_6729')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_7391 = relay.TupleGetItem(func_6729_call(), 0)
call_7392 = relay.TupleGetItem(func_6730_call(), 0)
func_5893_call = mod.get_global_var('func_5893')
func_5894_call = mutated_mod.get_global_var('func_5894')
call_7404 = relay.TupleGetItem(func_5893_call(), 1)
call_7405 = relay.TupleGetItem(func_5894_call(), 1)
output = relay.Tuple([call_7391,call_7404,])
output2 = relay.Tuple([call_7392,call_7405,])
func_7414 = relay.Function([], output)
mod['func_7414'] = func_7414
mod = relay.transform.InferType()(mod)
mutated_mod['func_7414'] = func_7414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7414_call = mutated_mod.get_global_var('func_7414')
call_7415 = func_7414_call()
output = call_7415
func_7416 = relay.Function([], output)
mutated_mod['func_7416'] = func_7416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5656_call = mod.get_global_var('func_5656')
func_5657_call = mutated_mod.get_global_var('func_5657')
call_7420 = relay.TupleGetItem(func_5656_call(), 0)
call_7421 = relay.TupleGetItem(func_5657_call(), 0)
output = call_7420
output2 = call_7421
func_7428 = relay.Function([], output)
mod['func_7428'] = func_7428
mod = relay.transform.InferType()(mod)
mutated_mod['func_7428'] = func_7428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7428_call = mutated_mod.get_global_var('func_7428')
call_7429 = func_7428_call()
output = call_7429
func_7430 = relay.Function([], output)
mutated_mod['func_7430'] = func_7430
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7484 = relay.const([[[True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False],[False,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True],[False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True],[False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,True],[False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False],[True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,True],[False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True]],[[True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False],[False,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True],[False,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True],[False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True],[False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,False],[True,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True],[True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,True]],[[True,True,False,False,False,True,True,False,True,True,False,True,True,False,False,True],[True,False,True,True,False,False,False,False,False,True,True,False,True,True,True,False],[False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True],[True,False,False,False,True,False,False,True,True,True,True,False,True,False,False,True],[True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True],[True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,True],[False,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False]]], dtype = "bool")#candidate|7484|(3, 7, 16)|const|bool
var_7485 = relay.var("var_7485", dtype = "bool", shape = (3, 7, 16))#candidate|7485|(3, 7, 16)|var|bool
bop_7486 = relay.logical_and(const_7484.astype('bool'), relay.reshape(var_7485.astype('bool'), relay.shape_of(const_7484))) # shape=(3, 7, 16)
func_5252_call = mod.get_global_var('func_5252')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_7491 = relay.TupleGetItem(func_5252_call(), 0)
call_7492 = relay.TupleGetItem(func_5254_call(), 0)
uop_7501 = relay.acosh(bop_7486.astype('float32')) # shape=(3, 7, 16)
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_7510 = relay.TupleGetItem(func_2589_call(), 0)
call_7511 = relay.TupleGetItem(func_2590_call(), 0)
output = relay.Tuple([call_7491,uop_7501,call_7510,])
output2 = relay.Tuple([call_7492,uop_7501,call_7511,])
func_7515 = relay.Function([var_7485,], output)
mod['func_7515'] = func_7515
mod = relay.transform.InferType()(mod)
mutated_mod['func_7515'] = func_7515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7516 = relay.var("var_7516", dtype = "bool", shape = (3, 7, 16))#candidate|7516|(3, 7, 16)|var|bool
func_7515_call = mutated_mod.get_global_var('func_7515')
call_7517 = func_7515_call(var_7516)
output = call_7517
func_7518 = relay.Function([var_7516], output)
mutated_mod['func_7518'] = func_7518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5727_call = mod.get_global_var('func_5727')
func_5729_call = mutated_mod.get_global_var('func_5729')
call_7522 = relay.TupleGetItem(func_5727_call(), 2)
call_7523 = relay.TupleGetItem(func_5729_call(), 2)
uop_7539 = relay.tan(call_7522.astype('float32')) # shape=(4, 8, 14)
uop_7541 = relay.tan(call_7523.astype('float32')) # shape=(4, 8, 14)
output = uop_7539
output2 = uop_7541
func_7546 = relay.Function([], output)
mod['func_7546'] = func_7546
mod = relay.transform.InferType()(mod)
mutated_mod['func_7546'] = func_7546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7546_call = mutated_mod.get_global_var('func_7546')
call_7547 = func_7546_call()
output = call_7547
func_7548 = relay.Function([], output)
mutated_mod['func_7548'] = func_7548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4174_call = mod.get_global_var('func_4174')
func_4175_call = mutated_mod.get_global_var('func_4175')
call_7571 = relay.TupleGetItem(func_4174_call(), 0)
call_7572 = relay.TupleGetItem(func_4175_call(), 0)
func_2810_call = mod.get_global_var('func_2810')
func_2812_call = mutated_mod.get_global_var('func_2812')
call_7581 = relay.TupleGetItem(func_2810_call(), 0)
call_7582 = relay.TupleGetItem(func_2812_call(), 0)
func_3617_call = mod.get_global_var('func_3617')
func_3618_call = mutated_mod.get_global_var('func_3618')
call_7598 = relay.TupleGetItem(func_3617_call(), 0)
call_7599 = relay.TupleGetItem(func_3618_call(), 0)
uop_7607 = relay.log2(call_7598.astype('float32')) # shape=(4, 8, 14)
uop_7609 = relay.log2(call_7599.astype('float32')) # shape=(4, 8, 14)
func_5469_call = mod.get_global_var('func_5469')
func_5471_call = mutated_mod.get_global_var('func_5471')
call_7610 = func_5469_call()
call_7611 = func_5469_call()
func_2960_call = mod.get_global_var('func_2960')
func_2961_call = mutated_mod.get_global_var('func_2961')
call_7612 = relay.TupleGetItem(func_2960_call(), 1)
call_7613 = relay.TupleGetItem(func_2961_call(), 1)
output = relay.Tuple([call_7571,call_7581,uop_7607,call_7610,call_7612,])
output2 = relay.Tuple([call_7572,call_7582,uop_7609,call_7611,call_7613,])
func_7615 = relay.Function([], output)
mod['func_7615'] = func_7615
mod = relay.transform.InferType()(mod)
output = func_7615()
func_7616 = relay.Function([], output)
mutated_mod['func_7616'] = func_7616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5871_call = mod.get_global_var('func_5871')
func_5873_call = mutated_mod.get_global_var('func_5873')
call_7672 = relay.TupleGetItem(func_5871_call(), 0)
call_7673 = relay.TupleGetItem(func_5873_call(), 0)
output = call_7672
output2 = call_7673
func_7681 = relay.Function([], output)
mod['func_7681'] = func_7681
mod = relay.transform.InferType()(mod)
mutated_mod['func_7681'] = func_7681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7681_call = mutated_mod.get_global_var('func_7681')
call_7682 = func_7681_call()
output = call_7682
func_7683 = relay.Function([], output)
mutated_mod['func_7683'] = func_7683
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7699 = relay.var("var_7699", dtype = "float64", shape = (16, 3, 8))#candidate|7699|(16, 3, 8)|var|float64
uop_7700 = relay.cos(var_7699.astype('float64')) # shape=(16, 3, 8)
bop_7713 = relay.logical_and(uop_7700.astype('bool'), relay.reshape(var_7699.astype('bool'), relay.shape_of(uop_7700))) # shape=(16, 3, 8)
func_1608_call = mod.get_global_var('func_1608')
func_1610_call = mutated_mod.get_global_var('func_1610')
call_7716 = relay.TupleGetItem(func_1608_call(), 1)
call_7717 = relay.TupleGetItem(func_1610_call(), 1)
bop_7720 = relay.add(bop_7713.astype('int32'), relay.reshape(uop_7700.astype('int32'), relay.shape_of(bop_7713))) # shape=(16, 3, 8)
uop_7727 = relay.sinh(bop_7720.astype('float64')) # shape=(16, 3, 8)
bop_7730 = relay.subtract(uop_7700.astype('int16'), relay.reshape(var_7699.astype('int16'), relay.shape_of(uop_7700))) # shape=(16, 3, 8)
uop_7743 = relay.log2(uop_7727.astype('float32')) # shape=(16, 3, 8)
bop_7745 = relay.left_shift(uop_7743.astype('uint64'), relay.reshape(bop_7730.astype('uint64'), relay.shape_of(uop_7743))) # shape=(16, 3, 8)
uop_7748 = relay.cosh(uop_7727.astype('float32')) # shape=(16, 3, 8)
uop_7759 = relay.asin(uop_7743.astype('float32')) # shape=(16, 3, 8)
output = relay.Tuple([call_7716,bop_7745,uop_7748,uop_7759,])
output2 = relay.Tuple([call_7717,bop_7745,uop_7748,uop_7759,])
func_7767 = relay.Function([var_7699,], output)
mod['func_7767'] = func_7767
mod = relay.transform.InferType()(mod)
var_7768 = relay.var("var_7768", dtype = "float64", shape = (16, 3, 8))#candidate|7768|(16, 3, 8)|var|float64
output = func_7767(var_7768)
func_7769 = relay.Function([var_7768], output)
mutated_mod['func_7769'] = func_7769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4643_call = mod.get_global_var('func_4643')
func_4645_call = mutated_mod.get_global_var('func_4645')
call_7771 = relay.TupleGetItem(func_4643_call(), 0)
call_7772 = relay.TupleGetItem(func_4645_call(), 0)
output = relay.Tuple([call_7771,])
output2 = relay.Tuple([call_7772,])
func_7777 = relay.Function([], output)
mod['func_7777'] = func_7777
mod = relay.transform.InferType()(mod)
output = func_7777()
func_7778 = relay.Function([], output)
mutated_mod['func_7778'] = func_7778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2589_call = mod.get_global_var('func_2589')
func_2590_call = mutated_mod.get_global_var('func_2590')
call_7787 = relay.TupleGetItem(func_2589_call(), 0)
call_7788 = relay.TupleGetItem(func_2590_call(), 0)
output = relay.Tuple([call_7787,])
output2 = relay.Tuple([call_7788,])
func_7795 = relay.Function([], output)
mod['func_7795'] = func_7795
mod = relay.transform.InferType()(mod)
mutated_mod['func_7795'] = func_7795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7795_call = mutated_mod.get_global_var('func_7795')
call_7796 = func_7795_call()
output = call_7796
func_7797 = relay.Function([], output)
mutated_mod['func_7797'] = func_7797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4267_call = mod.get_global_var('func_4267')
func_4269_call = mutated_mod.get_global_var('func_4269')
call_7803 = relay.TupleGetItem(func_4267_call(), 3)
call_7804 = relay.TupleGetItem(func_4269_call(), 3)
func_5727_call = mod.get_global_var('func_5727')
func_5729_call = mutated_mod.get_global_var('func_5729')
call_7807 = relay.TupleGetItem(func_5727_call(), 2)
call_7808 = relay.TupleGetItem(func_5729_call(), 2)
const_7824 = relay.const([[[0.569735,-1.981678,-8.629001,9.280136,1.616075,6.200935,9.720897,-5.517845,9.070523,-0.663012,-9.654258,-8.266650,-3.380960,8.138762],[-5.078029,4.615097,1.329785,8.630119,-6.593910,4.483543,-1.277755,0.047928,-8.926639,-1.483991,-4.218280,5.679572,-0.677196,-8.292010],[-8.449093,-3.358939,2.616884,1.255013,8.301974,-9.935688,7.140907,-5.503336,0.618163,6.713172,0.172832,8.350127,-7.730050,-6.259981],[3.981607,-2.907119,-3.733414,-1.452727,-7.406904,2.457671,1.155152,2.473432,2.407843,-3.450867,-2.800129,-1.516766,7.165537,8.565503],[-3.901743,-5.214584,1.842445,-5.363095,-1.487873,1.159565,-9.894275,-0.476862,-7.374701,-4.813456,7.007978,-4.124786,8.396594,4.193781],[0.966855,-4.700223,-5.079648,0.045597,0.829932,-4.220826,-6.716134,4.518096,-4.658709,-6.711222,3.531941,-2.726607,0.434087,-6.732665],[7.043993,-2.047415,8.980639,-1.645968,1.206197,1.030514,4.042010,-9.756493,8.699597,-7.707121,-0.065373,-7.936705,-6.343410,-8.941711],[-2.103514,-2.940497,4.837678,-3.646704,5.052974,-8.154060,-7.195586,-3.103776,4.469596,9.750465,-5.298188,-8.278272,9.859866,-6.155503]],[[5.175530,8.112019,-3.319770,5.650291,-8.474905,-8.526018,4.975165,6.625442,-1.937733,8.103081,-4.462791,-9.442850,4.769572,8.766879],[5.691270,-7.376329,0.124184,-0.294512,7.549906,5.158913,7.483466,9.293305,-6.089720,-6.894021,-5.089500,0.093635,2.437343,1.823049],[-5.731020,2.285952,8.224837,8.960389,4.282679,-6.242034,9.474450,6.254159,4.756241,5.719997,1.182943,-6.301519,-5.562764,-9.298813],[4.113428,-8.689015,8.092002,6.500306,4.055403,3.269915,6.940374,0.668192,7.997881,1.232710,2.116395,-7.567950,0.031524,9.916647],[-5.832307,0.397004,0.639228,-7.744043,1.341464,3.707936,-5.649200,4.461866,-4.049115,-7.468321,6.528888,-5.964938,9.153795,4.023093],[9.617240,-5.188168,3.739401,8.112474,4.457281,7.071120,-0.566317,2.557916,6.958869,-4.505580,4.233363,4.938139,-4.072194,4.521473],[-8.691006,-8.251812,5.982192,-3.700466,-4.149610,-4.916115,6.356816,-8.549969,-3.504429,-6.896422,2.533698,-1.593089,4.785410,5.944153],[8.303164,9.108046,-0.930208,-5.580226,-0.847958,-7.038145,-1.741490,-1.830105,-9.451726,6.924179,-7.506284,-1.311323,-7.020474,-1.234622]],[[-5.673484,-5.409812,1.788392,2.409731,3.903506,0.354276,-3.790700,5.504179,-7.274028,-7.240054,-7.612459,-8.225459,0.694385,-2.905230],[9.792778,-2.759892,4.904954,1.589440,-3.628106,-1.681408,-3.942954,-7.937672,5.108507,-7.511258,2.696361,-3.814980,-7.381390,1.443618],[6.317860,-2.320894,-3.906671,-0.250442,1.992298,-6.194540,-2.671114,3.567591,1.194395,-1.675961,7.342392,-8.950150,0.505369,7.702310],[6.089271,-8.516308,-2.072197,6.701592,3.279220,-1.355272,-2.493252,-4.883101,1.754703,8.922562,9.615232,2.049000,-7.039865,-4.063622],[-1.827113,-6.532395,-3.724287,-2.333204,9.089543,6.818909,9.911759,7.988240,3.591178,1.721795,0.724281,2.759067,-9.259980,-8.725785],[-4.159428,-6.057083,-4.588554,2.601643,6.839744,2.298312,0.164129,2.679530,8.949192,-8.819812,7.286322,0.594932,4.804315,0.902773],[-5.220299,-7.821380,-7.843376,3.819609,2.437648,4.192717,3.887771,6.130987,-4.571231,8.958450,8.307292,-4.914455,4.787135,-9.869518],[-7.166129,-0.607391,7.458205,0.355278,-8.241901,-1.951027,0.622846,-1.391784,-2.361676,-8.177357,0.804053,-9.293658,7.461026,4.778498]],[[5.619553,3.992758,4.463705,-3.624419,8.487157,0.373474,-8.766332,7.615212,9.029692,-3.014927,-0.337357,-1.995879,6.536000,-3.195270],[9.796850,9.399701,0.468391,-2.809219,7.786200,8.411126,0.503273,-6.116218,-9.548008,3.619804,6.064557,-5.028637,-5.024317,7.179515],[6.554649,2.449169,1.538882,8.690373,1.352069,-2.147510,-5.471963,0.832765,-4.347229,-9.396835,-2.741485,-0.702979,1.113722,2.455513],[-2.990683,2.220931,-9.107370,-9.047085,-4.701524,9.481516,-2.694398,-3.991333,8.944569,-2.283858,1.784749,4.114465,-8.724263,2.784836],[-6.978812,-9.513374,-5.325012,-1.909689,-2.407789,-5.890948,0.682400,-2.777620,6.859738,-6.715151,4.903630,-0.694660,0.302093,-3.035068],[-1.942675,-4.257312,-5.800629,8.821400,-2.913428,2.231998,-8.293417,3.162841,7.363572,9.646316,-1.910381,-2.508025,-5.401694,-1.933138],[-2.077483,-9.697595,1.333009,7.077268,5.503648,-1.389986,-3.292469,-5.036076,3.955928,-5.050914,0.821340,-3.492591,-5.815504,5.393256],[8.402245,-5.611032,-2.309474,-0.089732,2.199025,5.714154,-2.790844,4.848352,-3.533440,-9.507857,7.580999,-0.718925,-9.540019,8.356602]]], dtype = "float32")#candidate|7824|(4, 8, 14)|const|float32
bop_7825 = relay.logical_xor(call_7807.astype('uint8'), relay.reshape(const_7824.astype('uint8'), relay.shape_of(call_7807))) # shape=(4, 8, 14)
bop_7828 = relay.logical_xor(call_7808.astype('uint8'), relay.reshape(const_7824.astype('uint8'), relay.shape_of(call_7808))) # shape=(4, 8, 14)
bop_7832 = relay.maximum(const_7824.astype('int64'), relay.reshape(call_7807.astype('int64'), relay.shape_of(const_7824))) # shape=(4, 8, 14)
bop_7835 = relay.maximum(const_7824.astype('int64'), relay.reshape(call_7808.astype('int64'), relay.shape_of(const_7824))) # shape=(4, 8, 14)
func_4014_call = mod.get_global_var('func_4014')
func_4016_call = mutated_mod.get_global_var('func_4016')
call_7839 = relay.TupleGetItem(func_4014_call(), 0)
call_7840 = relay.TupleGetItem(func_4016_call(), 0)
bop_7848 = relay.bitwise_xor(call_7807.astype('uint16'), relay.reshape(const_7824.astype('uint16'), relay.shape_of(call_7807))) # shape=(4, 8, 14)
bop_7851 = relay.bitwise_xor(call_7808.astype('uint16'), relay.reshape(const_7824.astype('uint16'), relay.shape_of(call_7808))) # shape=(4, 8, 14)
func_4491_call = mod.get_global_var('func_4491')
func_4492_call = mutated_mod.get_global_var('func_4492')
call_7864 = relay.TupleGetItem(func_4491_call(), 0)
call_7865 = relay.TupleGetItem(func_4492_call(), 0)
output = relay.Tuple([call_7803,bop_7825,bop_7832,call_7839,bop_7848,call_7864,])
output2 = relay.Tuple([call_7804,bop_7828,bop_7835,call_7840,bop_7851,call_7865,])
func_7867 = relay.Function([], output)
mod['func_7867'] = func_7867
mod = relay.transform.InferType()(mod)
output = func_7867()
func_7868 = relay.Function([], output)
mutated_mod['func_7868'] = func_7868
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7879 = relay.var("var_7879", dtype = "float32", shape = (14, 8, 7))#candidate|7879|(14, 8, 7)|var|float32
uop_7880 = relay.sinh(var_7879.astype('float32')) # shape=(14, 8, 7)
uop_7888 = relay.acos(uop_7880.astype('float32')) # shape=(14, 8, 7)
func_7330_call = mod.get_global_var('func_7330')
func_7332_call = mutated_mod.get_global_var('func_7332')
call_7890 = relay.TupleGetItem(func_7330_call(), 0)
call_7891 = relay.TupleGetItem(func_7332_call(), 0)
uop_7895 = relay.sigmoid(uop_7888.astype('float64')) # shape=(14, 8, 7)
bop_7913 = relay.right_shift(uop_7895.astype('int32'), relay.reshape(var_7879.astype('int32'), relay.shape_of(uop_7895))) # shape=(14, 8, 7)
bop_7916 = relay.bitwise_or(uop_7888.astype('int16'), relay.reshape(bop_7913.astype('int16'), relay.shape_of(uop_7888))) # shape=(14, 8, 7)
func_5469_call = mod.get_global_var('func_5469')
func_5471_call = mutated_mod.get_global_var('func_5471')
call_7924 = func_5469_call()
call_7925 = func_5469_call()
func_2096_call = mod.get_global_var('func_2096')
func_2098_call = mutated_mod.get_global_var('func_2098')
call_7929 = relay.TupleGetItem(func_2096_call(), 0)
call_7930 = relay.TupleGetItem(func_2098_call(), 0)
uop_7931 = relay.rsqrt(uop_7888.astype('float64')) # shape=(14, 8, 7)
func_6932_call = mod.get_global_var('func_6932')
func_6935_call = mutated_mod.get_global_var('func_6935')
const_7936 = relay.const([-5.198345,-7.039271,9.210629,-8.382512,2.622529,9.485875,4.295290,-1.346095,9.355532,-7.076053,3.654506,7.544650,0.744305,5.238721,-2.431624,2.233975,3.261596,8.463921,-3.317833,7.616648,8.614696,9.265197,-6.313072,-6.230277,-3.461970,-5.018987,2.619233,-9.595087,1.414056,3.101662,-3.351373,-9.554534,-9.332775,-2.864597,6.119414,-7.240208,5.468037,9.744977,-0.066942,4.506676,0.691619,-4.110139,7.143321,2.248806,1.937916,-8.532696,0.581693,3.350983,-3.045257,-9.322801,1.620452,0.677167,-1.844313,-6.138198,-7.910342,7.461262,4.160784,-8.744910,9.201197,8.430579,-3.567655,-7.493977,-4.092997,2.524035,9.806911,-6.878863,2.232570,2.371152,8.846381,-5.760954,7.123156,9.973118,2.325449,-0.368518,3.418915,5.737944,1.644200,4.764891,7.973563,1.236427,0.004250,8.517227,1.437331,-9.651100,-0.022154,-7.084012,6.768659,9.295204,-5.248939,6.195981,1.149695,2.807524,-0.103138,7.142053,-7.282984,-9.248661,-2.444030,-2.608135,8.109917,-5.602769,4.109808,3.154782,-1.637683,1.185192,-5.625263,-0.622306,-1.565934,0.458828,0.309242,-7.965190,1.170428,7.095126,1.379995,9.933089,-2.134834,-4.931990,-7.713754,-4.867126,-6.167749,7.584376,-9.038527,8.137056,-0.814608,7.219041,0.846205,8.145031,4.958356,-7.646562,-4.572735,8.813336,-5.296267,-3.320765,7.401081,2.393024,-0.695410,0.475563,3.944444,8.351359,6.419832,5.517875,3.511171,6.773266,0.536721,3.082262,1.737846,-5.381532,-6.958005,-0.952166,-5.316835,-4.763493,8.444511,7.632875,-9.258807,-7.467528,-9.836065,-5.283061,-0.836233,-6.365837,1.769946,2.529531,-8.003829,-6.346588,-7.614400,-9.410399,4.436610,1.486265,-1.759134,4.560722,-3.339210,-0.170234,6.514282,-2.618294,-3.554512,6.219016,-0.085204,-5.781459,-7.344253,7.572459,-4.212668,4.119127,-2.466826,-3.722929,-6.326558,9.612113,8.401072,0.210329,-9.939795,-2.539230,-7.778863,4.355357,-4.438395,4.978147,-9.726816,1.035187,-9.535082,-6.846501,7.820679,-0.698300,-7.956467,-1.095614,5.380134,-6.970106,5.883437,4.854465,-8.046641,-1.377791,-5.592126,-1.442684,4.889717,9.798364,-4.074367,-6.983487,-2.427427,2.846414,5.929648,-5.305372,4.228940,-2.190462,2.671477,-1.196508,-3.426861,-8.322405,-4.026261,-0.845960,-8.825671,-4.582295,2.103824,5.413758,9.738431,0.760671,-1.215547,0.305648,-2.791125,7.239458,4.173245,-6.033164,-6.915429,7.374750,0.218409,-1.491686,1.355448,-7.038070,-2.701355,8.623478,4.338378,-4.139546,-0.780140,3.285414,8.784668,8.731016,9.837942,0.220437,-5.215372,-5.041668,-7.163938,-9.136681,2.167037,-8.442108,-5.846773,5.567307,-2.269407,8.037308,-2.794531,-0.862874,6.669703,-4.491120,0.732689,3.732915,-5.825951,3.308622,-0.426946,7.040559,-6.633201,4.741454,1.124025,-1.294795,-1.438430,-0.298622,1.538974,6.120947,-6.343492,4.772310,6.364591,-6.005541,-3.365608,-7.577479,1.867279,4.985291,6.462345,-4.349298,6.813145,6.546900,-6.705080,-5.558027,-6.295868,4.064472,-9.372927,-6.558973,7.857223,8.551410,-4.264751,-2.991550,4.319418,5.889352,5.849329,8.711738,3.821390,-4.137012,0.267054,4.171385,-1.641466,-6.099823,1.112363,-8.887595,5.645883,-1.059948,2.943856,1.504787,-4.272110,-0.838106,-2.176462,0.486326,-2.517022,-3.136012,-0.058218,2.045519,-4.695472,8.263770,-4.341185,-5.443565,-4.421113,5.211199,4.987127,-5.718930,3.630417,0.622906,3.497126,6.634645,9.520120,8.012330,6.552171,-3.718508,-1.696724,3.130931,-7.951726,7.832532,4.383164,-4.975333,7.367919,-2.322473,6.748874,9.404918,-3.554592,-1.563832,-0.862654,-9.474299,-8.714998,8.166234,-6.832300,3.527746,-1.409879,7.456382,2.133978,-4.431237,4.559690,-8.571012,6.337236,3.999563,-4.227118,5.522414,1.021580,8.217549,-8.975457,-7.033556,7.819971,4.917235,-0.703598,6.078036,7.539182,3.934898,0.099228,1.758636,9.609772,-5.335659,9.825198,-9.111857,1.285148,-9.674955,-7.366840,4.557156,5.917281,6.459597,4.368166,7.747170,-8.890649,4.961019,-7.803665,-9.690076,3.391754,-0.474803,-5.508119,5.103163,-8.774488,-6.978986,5.978176,-3.589834,-1.528136,-3.937829,7.094151,-7.003414,-9.840852,2.448072,1.506568,-2.472508,-0.069808,9.003311,2.938456,8.330897,-4.913400,-8.543273,1.760907,-0.212106,-6.020810,6.525119,4.205748,-0.907926,-5.344391,-6.125461,7.021273,-9.104524,5.142803,2.847269,5.700386,-1.129176,-7.800467,7.266553,-5.085299,0.161732,-8.804450,-8.043507,9.280278,-3.292566,-4.386745,5.130814,5.993864,1.333610,5.189442,-2.077280,0.433520,-3.143617,3.860241,3.566633,-4.937513,0.977450,-6.043993,-9.201370,-9.390415,2.337193,0.908703,-0.781764,-9.764505,-1.064280,-8.011444,-4.786320,8.340917,1.820306,-1.205079,-3.771326,-2.147868,-2.868555,7.572986,-8.151336,6.400728,-9.556724,-8.579818,2.598636,0.234098,-7.687044,-6.575595,0.996495,7.233733,4.195542,-4.839409,-1.957028,3.407904,9.383440,6.828224,-5.791506,0.686318,-2.825788,6.955209,-3.377539,0.585911,0.337066,-7.490790,7.248518,1.265613,4.517667,2.019245,-1.298699,-4.241319,7.364921,4.157808,-7.564573,3.696525,-3.681888,0.302676,5.252211,4.470836,-5.900016,5.033104,-0.878128,-4.348687,-9.629955,6.029842,-7.299100,-6.865314,-1.368495,1.260170,-1.979896,7.915420,-6.316589,-5.113885,8.374236,-8.338734,2.105120,1.948776,-4.673822,7.966016,1.219363,-9.971829,9.419593,-6.951643,-6.308678,-7.486582,-5.597778,-6.165481,-0.223042,-1.970788,-5.950937,-0.410686,-6.059821,1.873831,9.383666,-6.599508,-1.222010,5.295425,6.910940,2.648620,8.825488,5.888461,2.421092,-6.234569,-3.627099,8.414425,7.540083,-7.413161,5.545544,2.048962,-6.900314,-4.772859,-7.772053,-5.064501,1.488705,9.797631,-7.608120,-0.461043,-1.010467,5.847504,2.416065,-8.059182,-1.876441,-2.331437,-9.176536,2.799479,8.905672,9.310484,7.167929,-5.894945,7.896414,9.086037,-7.998627,4.676631,7.496605,1.040021,6.513498,7.536891,-5.261996,-1.675039,7.855987,8.449311,5.763779,-2.875652,5.086781,1.791539,1.101026,-6.383205,-3.109746,-8.846927,-0.942753,-9.386520,5.750598,-2.829713,2.488866,6.705951,-9.016867,-6.502570,3.149480,-1.130506,6.760184,-8.066787,-8.650282,-8.610986,-8.857423,-0.563861,-0.298945,2.703633,5.344902,6.690906,-2.853267,6.568323,7.868038,-4.830571,7.960265,3.731489,-6.957611,2.766763,-1.367163,8.974753,-7.327612,-9.688527,-9.236634,9.971357,4.240041,-9.147856,1.291703,-6.315485,6.146416,1.079155,0.120550,9.577608,-8.618596,-9.327314,-3.303589,-8.883921,-8.860533,3.540624,-5.051144,-7.387925,2.223943,2.399419,-6.005232,-2.083889,-5.063703,-0.531324,-6.328289,2.052553,-9.259169,-9.493468,2.123400,-5.261559,6.973877,-7.781875,-5.900535,7.928092,4.819490,-8.932752,-6.330778,-0.477840,-1.321955,-4.253194,-6.030272,-3.109312,4.378152,-6.866721,7.962039,-3.072808,-0.916580,-7.043600,2.302261,9.680672,-9.845124,8.351114,-6.970909,3.529713,-1.997487,6.308190,2.966109,-1.342202,-3.936074,8.981847,9.082605,-9.715387,-7.254835,-9.618167,-4.916444,-1.535639,9.447271,0.733006,1.053995,-3.276233,-0.626074,8.566454,8.587234,0.570523,-3.286500,5.972828,-4.819944,2.485973,-3.399263,6.270224,5.144578,4.749006,7.172179,-7.466670,1.356874,-3.362080,2.939595,2.755223,7.146784,-6.456852,2.325244,5.171994,-0.783607,-0.522287,-1.917224,5.073270,-6.032956,-2.940070,-8.488786,-2.126517,-1.465916,0.881525,-9.878546,-0.260558,4.153636,2.439261,6.545713,5.391828,-6.935865,-6.782024,3.957801,-1.463142,9.726611,9.911466,-4.252007,7.354242,-6.429193,-2.933195,-6.739363,9.399335,7.334485,-9.754603,8.495218,-5.836576,-2.877755,6.865248,8.288622,9.545975,-0.313901,-9.857507,-0.179531,4.300988,-1.333719,-9.295983,1.565220,9.454234,-3.705546,3.467808,7.079630,1.522823,-3.261186,7.595758,7.552985,-7.615882,9.121158,-0.244333,8.867307,-3.346396,9.739104,-2.094099,-6.408033,8.867460,8.094637,3.121135,3.078960,-6.241666,5.454058,3.073886,-7.733805,-6.085995,-8.125907,-8.398588,8.691122,7.919450,2.963453,9.610681,7.969443,-8.399790,3.432505,5.063244,0.778855,-3.227471,9.600533,2.759020,-5.604990,6.410870,-2.092143,-1.044347,4.507986,-7.185950,6.577346,-6.109124,-8.667333,9.250828,-6.422991,-3.596954,7.336330,-0.148477,-6.587531,-7.778384,-0.791731,9.196407,8.640526,-7.412460,-2.798316,6.050922,-5.426093,-9.027967,8.993882,-9.256443,6.545563,9.686229,2.573050,6.392964,6.225313,-1.295928,-4.431968,-9.087696,1.442657,-1.775637,7.971728,4.423919,7.845330,-5.518366,-2.410143,4.978373,-1.922197,-9.116284,-4.255467,9.216291,5.504917,7.369257,-0.401033,-2.526025,-6.627748,9.946487,-4.665189,0.927208,-1.999771,-1.722740,-8.410167,-7.789123,-4.413871,1.292874,6.924179,-2.478585,-5.367205,-1.163969,7.806869,2.891387,8.961484,4.787372,9.686125,8.251527,5.388015,-5.945798,3.053961,-6.556102,0.369938,9.544407,-9.137709,-9.437883,5.637382,0.403581,6.244804,6.101029,8.387742,-1.964220,6.943415,1.443662,-0.004602,1.714248,-9.990146,3.575084,8.416575,-6.843199,4.445283,-5.554941,1.588564,6.415718,-2.470563,2.715579,-2.469876,5.461443,-5.501612,-8.616913,-7.394149,-9.546998,9.645557,0.657589,-1.062511,-3.729699,-9.750111,2.300496,9.238082,-6.811933,5.530306,8.916428,9.737313,3.543829,6.175687,-7.789685,0.231557,2.079578,5.417298,7.830294,-0.228267,0.508078,9.772943,7.511562,0.986802,-7.244368,9.426001,-0.516607,-5.264122,-3.751349,1.059887,-4.868403,-0.351740,0.846619,-9.061319,1.767951,9.418871,9.459839,0.876637,6.735730,-7.289879,8.603529,3.381359,-8.137959,-3.859037,-5.971630,-3.857799,-1.581368,-4.731014,-5.426910,6.271080,3.062358,-4.769518,9.035109,6.998966,-9.962414,-9.802874,-1.502430,-1.916107,-7.791841,9.996982,-2.782968,0.125090,-9.650258,5.401424,-1.779425,1.731881,2.078870,-1.540851,7.414263,8.608280,4.783810,-7.765926,8.300958,-9.946332,3.692792,-9.876519,6.829076,-7.806960,9.875285,-8.229856,-1.377843,-6.672119,5.372912,-7.623000,-3.097506,7.505445,-6.704264,7.431280,-2.323520,6.214383,-6.733013,8.346030,3.274229,2.392935,2.369801,-8.571162,1.267976,3.781675,7.747978,-9.529348,9.090520,6.075440,4.562021,-0.441172,-0.031602,6.424067,8.091919,5.210385,-5.057059,-8.110757,-3.977213,-3.046107,4.292040,7.002666,3.767864,-5.097181,3.052277,-7.371197,9.257847,-3.727523,-3.402465,-4.249947,-4.404710,-6.218113,-7.435547,1.820856,8.641267,5.064770,2.458843,7.331391,-1.529389,-4.979678,8.185367,-0.422455,0.162555,1.837797,-1.721132,2.213439,6.838355,1.229379,-5.523233,-0.579458,-1.136351,-2.071950,-4.626707,5.260761,-9.344890,-8.212806,-5.061342,-0.336810,1.760068,-0.136414,9.040881,0.155223,9.835630,-6.877943,8.784513,-3.096857,-5.792619,3.481237,-2.187656,4.925077,-9.883965,7.453921,-5.463684,-0.343944,1.172052,6.885184,5.735030,7.439047,-2.198197,-5.590128,-9.150768,2.913260,-7.600720,-0.613026,8.681657,5.477696,8.828695,8.129690,-4.471262,-4.486244,-5.948215,-7.731825,-9.640967,-9.740296,0.083574,-1.312835,0.208839,9.502472,-8.380368,3.271077,8.346871,-4.898929,1.176878,4.783790,3.074033,2.543585,6.405216,9.509001,7.047859,-4.918514,9.758114,-6.147572,3.747383,-8.569218,3.253511,4.183236,-9.887289,-0.213918,2.820162,2.514117,1.400972,-1.182859,-3.541733,-9.259034,-2.629807,-5.704157,2.498758,-0.529960,-5.145211,-3.282849,-6.923251,1.334816,9.076030,-4.553962,7.392778,-7.791984,-6.742181,2.323441,-7.345315,-5.566819,2.276875,-1.220693,-0.047302,5.398541,2.339974,-8.236382,0.990785,-5.793048,4.448446,-5.925038,-6.496810,0.757303], dtype = "float32")#candidate|7936|(1152,)|const|float32
call_7935 = relay.TupleGetItem(func_6932_call(relay.reshape(const_7936.astype('float32'), [12, 6, 16])), 0)
call_7937 = relay.TupleGetItem(func_6935_call(relay.reshape(const_7936.astype('float32'), [12, 6, 16])), 0)
func_3180_call = mod.get_global_var('func_3180')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_7940 = relay.TupleGetItem(func_3180_call(), 1)
call_7941 = relay.TupleGetItem(func_3181_call(), 1)
func_5289_call = mod.get_global_var('func_5289')
func_5291_call = mutated_mod.get_global_var('func_5291')
const_7949 = relay.const([-2.541583,7.843936,1.275575,0.094862,5.097090,9.785557,-0.970616,8.053459,8.271523,-8.006370,8.657464,9.259887,-1.150445,6.837247,-4.062577,-3.650292,7.345176,3.262046,-1.233187,3.345321,3.695096,-5.880419,-9.469852,-9.341127,-2.273642,6.085353,5.049887,-4.668770], dtype = "float32")#candidate|7949|(28,)|const|float32
call_7948 = relay.TupleGetItem(func_5289_call(relay.reshape(const_7949.astype('float32'), [7, 2, 2])), 1)
call_7950 = relay.TupleGetItem(func_5291_call(relay.reshape(const_7949.astype('float32'), [7, 2, 2])), 1)
func_6036_call = mod.get_global_var('func_6036')
func_6039_call = mutated_mod.get_global_var('func_6039')
var_7955 = relay.var("var_7955", dtype = "float64", shape = (1638,))#candidate|7955|(1638,)|var|float64
call_7954 = relay.TupleGetItem(func_6036_call(relay.reshape(var_7955.astype('float64'), [1638,])), 3)
call_7956 = relay.TupleGetItem(func_6039_call(relay.reshape(var_7955.astype('float64'), [1638,])), 3)
func_7681_call = mod.get_global_var('func_7681')
func_7683_call = mutated_mod.get_global_var('func_7683')
call_7967 = func_7681_call()
call_7968 = func_7681_call()
func_1870_call = mod.get_global_var('func_1870')
func_1872_call = mutated_mod.get_global_var('func_1872')
call_7972 = func_1870_call()
call_7973 = func_1870_call()
bop_7978 = relay.less(uop_7888.astype('bool'), relay.reshape(bop_7913.astype('bool'), relay.shape_of(uop_7888))) # shape=(14, 8, 7)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_7987 = func_7239_call()
call_7988 = func_7239_call()
output = relay.Tuple([call_7890,bop_7916,call_7924,call_7929,uop_7931,call_7935,const_7936,call_7940,call_7948,const_7949,call_7954,var_7955,call_7967,call_7972,bop_7978,call_7987,])
output2 = relay.Tuple([call_7891,bop_7916,call_7925,call_7930,uop_7931,call_7937,const_7936,call_7941,call_7950,const_7949,call_7956,var_7955,call_7968,call_7973,bop_7978,call_7988,])
func_7994 = relay.Function([var_7879,var_7955,], output)
mod['func_7994'] = func_7994
mod = relay.transform.InferType()(mod)
var_7995 = relay.var("var_7995", dtype = "float32", shape = (14, 8, 7))#candidate|7995|(14, 8, 7)|var|float32
var_7996 = relay.var("var_7996", dtype = "float64", shape = (1638,))#candidate|7996|(1638,)|var|float64
output = func_7994(var_7995,var_7996,)
func_7997 = relay.Function([var_7995,var_7996,], output)
mutated_mod['func_7997'] = func_7997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2521_call = mod.get_global_var('func_2521')
func_2523_call = mutated_mod.get_global_var('func_2523')
call_8020 = relay.TupleGetItem(func_2521_call(), 0)
call_8021 = relay.TupleGetItem(func_2523_call(), 0)
output = call_8020
output2 = call_8021
func_8026 = relay.Function([], output)
mod['func_8026'] = func_8026
mod = relay.transform.InferType()(mod)
mutated_mod['func_8026'] = func_8026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8026_call = mutated_mod.get_global_var('func_8026')
call_8027 = func_8026_call()
output = call_8027
func_8028 = relay.Function([], output)
mutated_mod['func_8028'] = func_8028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4594_call = mod.get_global_var('func_4594')
func_4596_call = mutated_mod.get_global_var('func_4596')
call_8029 = func_4594_call()
call_8030 = func_4594_call()
func_533_call = mod.get_global_var('func_533')
func_537_call = mutated_mod.get_global_var('func_537')
const_8036 = relay.const([-4,3,8,-8,4,-6,9,-6,-8,-1,-4,2,-5,-7,10,-5,6,6,6,9,-5,4,-2,-10,-3,-9,-3,-3,9,3,5,-6,3,-5,5,10,-8,3,-5,4,-2,-5,5,-3,9,6,1,-4,-5,5,2,1,2,-2,6,6,-9,3,2,-10,2,-4,-9,7,-7,5,2,1,-1,4,9,5,3,-3,6,6,9,-8,10,4,2,7,9,-9,-1,8,-4,-9,5,-4,7,-6,1,7,-1,-9,2,8,-3,4,3,5,6,-6,8,-9,-3,-1,1,4,-1,-7,-8,-6,6,-7,1,6,-6,8,6,8,4,-2,9,9,10,5,-2,10,-1,7,-7,-9,7,8,5,-3,-7,-6,-2,10,-2,9,-6,-4,-6,-8,5,-7,-3,8,-10,10,5,-8,10,6,-3,-10,5,-5,-6,-5,8,-5,-6,-2,-3,8,6,-2,1,2,6,2,-5,-4,10,4,-1,1,-4,-6,3,5,-9,10,9,-4,2,-8,-5,-8,2,-4,-10,2,10,-3,1,4,6,-2,6,2,3,4,10,2,-3,7,-3,-9,7,6,9,10,6,2,7,9,-4,8,5,8,-6,3,-1,2,6,8,2,3,-9,1,1,-5,-2,-8,3,-7,8,10,-4,-1,-2,8,-6,-3,7,10,5,10,-8,-6,-4,-10,5,-6,-2,-1,-6,10,1,-9,-9,-6,-6,-2,7,-5,-1,5,-3,-6,8,1,6,7,5,6,7,-8,10,-9,-6,-10,-9,4,6,9,5,9,9,9,-4,-10,8,-5,-8,7,-9,2,2,2,-3,-5,10,2,-9,-7,-7,-3,-5,-5,-3,8,9,-3,-7,2,-7,10,8,9,4,-10,5,6,-4,-4,3,-2,-5,7,10,-1,6,-6,-5,4,3,8,9,-7,-7,1,-4,-4,6,8,-1,-2,-2,3,-5,7,-3,5,1,7,2,7,9,-4,3,10,3,-2,2,4,-2,-5,-8,-9,10,-8,-3,10,-8,-6,6,-6,-8,6,4,7,-3,-3,3,-1,-7,7,7,2,2,8,-4,9,-5,-3,-6,-4,-5,1,8,-10,2,5,-7,-7,-4,10,-3,1,-5,4,-7,2,5,9,-5,8,-10,-9,1,7,4,5,-6,3,3,5,-8,-3,10,6,-2,-5,7,-1,-1,-4,-8,10,5,7,5,-7,9,-5,1,4,-6,-8,-2,-9,-9,-6,10,-1,3,3,10,-10,10,-7,9,-4,8,-5,-3,3,-7,-7,9,2,-7,-8,4,7,-5,5,-6,6,5,6,8,-7,10,-2,3,-1,-10,9,-6,10,-1,-5,5,2,-3,-7,-8,5,-10,7,2,4,-6,10,9,5,-4,-6,-2,-1,5,-7,2,-10,-1,-6,4,7,-4,2,-6,1,7,-2,-6,-5,3,-3,-4,-7,-2,9,4,-4,4,2,-4,3,10,10,10,-6,-7,-8,-6,5,-10,3,-10,-2,4,-6,7,-2,5,-5,-7,-6,4,5,-8,7,7,-4,7,-1,2,-1,-7,9,5,6,7,-6,5,10,-6,-5,-6,-7,-7,-4,-8,-9,8,-8,10,-2,-6,-7,-4,8,5,-10,-2,-2,9,-7,2,3,-2,10,-5,-10,-5,-3,5,8,7,-10,6,8,-9,4,9,-1,8,-4,6,-3,-2,-7,-10,-6,4,5,-10,-5,6,-10,7,-7,-1,-8,-2,7,9,-10,10,7,-3,-3,-5,-2,8,-7,3,7,-2,10,-6,-9,-2,6,-8,5,-5,-6,7,-3,-10,-7,4,-7,-9,-2,6,1,-4,-2,-2,-4,3,9,-10,4,-5,-2,-5,5,6,2,-1,-1,-2,7,-10,-2,3,-5,-6,-2,10,-9,-1,-2,4,-10,-8,1,-6,5,1,8,-1,-6,2,7,10,-6,2,9,-1,-4,3,-1,6,-2,-3,1,-5,-10,-7,-6,7,-9,9,7,-8,-1,4,10,7,-7,6,4,-8,-6,-5,1,6,1,9,-7,6,-10,9,-2,-5,7,-8,-1,-9,-1,-9,6,-2,1,2,-10,8,-1,-1,-3,4,6,-3,10,3,-6,-4,10,-7,9,10,10,-9,-5,5,-7,-10,-1,-9,4,-4,6,3,6,-6,-3,-6,4,-3,-8,-7,-7,7,1,-3,-7,7,5,-9,2,-7,2,8,-1,-5,1,-3,10,-10,-5,5,-8,-7,-4,3,2,3,-3,1,5,-4,-1,-7,-8,-1,-8,7,1,-8,-8,3,2,5,-10,-9,4,1,10,-6,5,-1,6,-10,2,3,10,10,-3,-7,-3,8,-10,5,-7,8,10,4,9,-4,1,-1,-3,-4,7,-3,-8,2,-8,-9,9,4,9,7,1,9,7,4,10,-10,9,-9,-4,6,9,-6,3,10,-9,1,6,-5,-7,-7,-7,6,-2,-5,-8,-8,-4,-5,-6,10,2,9,-1,-3,3,7,-8,-8,-8,7,-3,4,1,8,-6,5,10,-8,-8,9,-2,3,-9,-2,-5,-6,-6,-8,10,4,-4,6,5,-7,4,4,2,7,8,2,-8,4,7,-1,-9,4,4,-9,3,-9,4,4,3,-9,1,-6,10,-5,3,-5,-10,8,-3,10,5,-5,-7,6,10,-2,-9,-2,-8,7,4,6,4,-6,2,-1,9,7,4,-5,1,7,-4,8,-7,-7,-6,3,-6,-5,6,5,-5,-1,-6,-3,-2,6,1,-1,-8,7,1,5,10,-8,-9,4,-7,-3,1,-1,-8,2,10,6,-4,-3,-5,-4,8,5,-9,1,4,-1,10,10,9,-7,-7,-7,8,-6,8,-1,-6,-4,-3,-2,-1,-4,5,8,5,-2,-10,3,-9,-10,3,-3,-8,-5,-4,-8,10,-5,-5,8,10,-6,9,8,-10,-4,2,3,4,10,3,-4,-1,7,-4,8,6,-6,-3,2,-5,-8,4,6,1,8,4,-8,-9,-3,-1,8,-6,10,-9,5,-1,-10,8,2,1,-3,10,-2,-6,5,-7,-5,-7,2,-9,9,-2,4,-4,9,-8,2,6,10,-10,-1,8,-10,1,9,9,-2,7,-10,6,-8,-2,2,-6,-9,-7,-5,-6,-10,-5,9,-8,-6,8,-8,5,-7,-8,-6,3,-3,8,7,-3,3,5,3,-2,8,4,2,-4,8,-2,-8,-2,7,-1,5,1,-1,9,-8,2,1,-6,5,4,1,10,10,4,-3,2,-8,-6,-9,-4,4,-5,-4,-7,-10,-4,6,-2,-7,6,1,8,10,10,-6,6,-2,6,3,-7,-6,-6,5,1,-6,2,6,7,-1,-5,3,9,-6,3,10,-2,1,3,6,7,-2,9,6,-3,-5,6,-2,7,-1,5,10,-2,-5,-8,8,3,4,-5,10,-1,-6,4,3,-4,-4,10,8,7,-4,4,-10,-1,9,-7,3,3,-5,7,-10,4,2,10,-5,-3,9,2,-2,-4,-10,9,10,-3,3,-5,-3,-9,-5,2,3,9,-3,-3,-6,8,-9,9,3,6,-4,-8,-2,-9,-5,6,-8,-2,-8,6,2,-9,-4,-10,-10,10,-9,-8,-5,-9,10,8,2,1,-5,-3,-2,7,9,-1,-4,-3,-1,-6,-10,7,-2,-9,5,4,6,4,-10,-6,-8,7,9,-7,-3,-7,9,4,-8,-6,3,-2,7,-9,-9,-5,-1,1,4,-2,-2,-9,-4,-4,6,-7,8,-9,7,2,-2,-3,9,5,-1,-10,8,5,2,6,9,-6,3,4,3,6,-2,10,-10,-5,-6,5,6,-5,1,-4,-5,7,-4,-9,-6,-4,-1,-10,-1,-3,1,10,10,-4,7,9,-8,1,9,9,-5,4,7,-1,8,-7,4,4,3,4,6,3,2,-6,-5,8,9,-8,-7,-9,2,4,1,9,8,3,9,-7,-1,-3,1,-6,5,-1,10,-7,-3,-10,1,-10,5,2,-1,-4,-6,-9,-8,7,7,-4,-7,-1,2,-9,-3,1,-4,1,-3,-8,-9,4,-1,1,-1,9,7,-2,-3,1,10,3,6,9,-8,6,7,-5,5,8,-2,-5,7,8,-8,6,-3,-4,-5,-8,-2,-10,-4,-7,2,4,2,-3,-9,-1,-1,7,-7,3,-3,-5,-5,6,-2,10,-10,-10,-6,-5,5,3,2,10,-10,1,5,-10,3,-2,9,-10,8,5,-2,-10,4,-3,-5,6,-9,9,-3,6,5,10,4,4,8,6,8,9,1,-10,6,-2,-3,2,-9,1,-8,9,10,4,5,-10,-7,-6,-2,7,-2,-6,9,10,-6,-4,-1,6,8,-1,-1,-7,1,-1,2,4,4,-7,-6,10,8,-8,-9,-10,6,10,-2,8,-2,8,-6,6,-2,2,9,-10,8,-8,2,-3,-1,8,10,9,-6,4,9,9,-4,-9,-6,10,9,-10,7,-1,-4,2,-8,8,9,-3,3,-10,-6,-9,-10,-4,-8,1,-8,4,3,8,8,-5,-9,5,-2,-6,-8,1,-4,8,-1,-7,-3,-1,-8,8,-6,-1,3,6,3,-6,-6,8,1,-4,-4,1,4,4,2,8,-6,2,6,-5,-9,9,-7,9,-4,-10,6,8,5,3,-5,-5,1,10,-7,-6,7,4,-6,-2,6,1,-5,-3,10,-8,-9,5,4,7,2,8,1,-3,-4,7,7,1,6,4,2,-8,7,-10,1,-2,1,2,3,8,10,-5,-3,3,-2,3,9,4,-9,6,-2,-2,-8,4,2,9,7,-1,2,-10,-8,-8,-8,-2,-7,-6,-7,-3,-5,-8,-8,8,-1,-8,4,-7,4,-9,8,-9,10,-5,4,-3,4,5,-8,-9,-4,2,-8,-10,4,5,3,-6,-1,-1,8,5,7,4,-3,-4,4,4,-7,-2,-4,-3,-3,9,2,9,5,-2,4,-8,2,3,-8,-6,9,-5,7,9,1,-1,7,-2,4,5,-1,4,-4,7,-3,-6,3,5,-3,7,2,6,-10,4,-4,1,-1,-1,9,7,-3,6,8,5,6,5,1,-9,-4,2,-3,5,7,1,6,-10,2,-8,-7,-2,-4,-3,2,6,7,4,-3,6,-9,-6,6,5,-1,-8,5,-9,9,-5,-6,-5,-1,4,9,3,-8,2,-4,2,1,2,-10,-6,5,-7,4,-3,-2,8,9,-1,10,-1,-2,2,2,1,6,-8,1,-3,9,10,3,3,1,8,-7,8,1,7,3,-5,5,2,-9,1,-1,1,10,5,-8,-5,-4,-8,-2,-8,3,5,-7,6,-2,-5,-1,-8,-10,4,-7,-7,-1,-4,10,-9,-5,4,1,-9,-8,-5,-1,-10,5,-1,1,3,-4,7,1,10,-8,10,-2,-4,3,9,-2,5,3,10,-7,-9,10,-7,-10,8,9,1,7,4,-5,-4,-4,-4,8,-2,-9,-5,7,-3,-7,6,9,9,-3,5,-8,2,-1,-10,4,-3,-4,-3,10,-7,7,5,3,1,7,-1,-9,4,3,1,7,-10,2,-10,-1,9,2,-3,8,-10,-4,-7,-8,-2,-6,-8,-7,-1,-4,-3,-10,3,6,7,-2,8,-2,6,7,-10,-3,5,-9,-10,9,-9,6,1,10,6,6,5,-9,7,10,-1,6,-4,-4,1,6,4,-2,3,-4,-3,5,10,8,1,5,-3,-10,7,9,-1,7,-6,2,-2,-10,-9,-10,10,4,-6,-5,-1,5,-3,5,-1,9,3,9,-8,-10,-4,3], dtype = "int16")#candidate|8036|(2145,)|const|int16
const_8037 = relay.const([-5,-4,7,9,-1,-2,4,-4,-9,10,-3,-7,-5,3,5,-8,8,-5,1,-3,-8,-9,-2,-5,10,-9,8,-2,-2,-2,8,1,-3,-3,2,-7,10,5,8,4,-7,-1,-6,7,1,-9,1,-4,-6,-9,2,3,3,-5,9,-9,2,-3,-6,-8,-2,-5,-9,-9,6,5,5,2,-5,-9,8,-1,9,-9,-4,9,8,-9,2,9,-8,-8,2,1,10,-2,-7,9,6,-10,-6,6,-4,8,5,-6,4,7,7,-5,-5,3,9,9,-9,8,1,-9,1,3,-7,-10,-4,-10,5,7,-2,4,-2,9,-4,-9,10,-2,-7,8,3,-8,-7,9,2,1,-6,-7,10,2,-2,-10,8,5,4,-1,3,7,6,1,-10,3,-7,-6,6,-2,-6,-3,4,-10,-3,-7,-10,6,10,5,-10,-8,1,-4,10,7,8,-10,8,-3,3,-7,4,-1,1,-4,6,-7,-6,4,-7,-1,1,-9,3,1,-10,1,4,-10,-9,5,6,10,5,7,-7,8,10,-10,-7,-1,9,-3,-7,9,7,9,8,-7,-5,4,5,-3,-7,-9,2,-3,3,6,-9,6,-9,-3,-6,9,-9,5,-4,6,-1,-8,-7,6,9,2,6,-5,-2,-3,3,10,-4,-3,-3,-4,5,9,-4,-4,8,-10,1,-1,-6,-9,-8,-10,-4,-3,-3,3,-10,10,7,7,-9,2,-2,2,9,8,4,2,-2,-7,3,-3,-4,6,-6,-7,-10,6,3,-4,3,10,2,5,6,-7,4,1,-2,9,2,4,6,5,-7,-2,1,-8,-5,-6,-5,-9,4,6,10,7,-3,3,-10,1,-7,10,8,-2,-10,-3,5,3,3,-7,-9,5,5,3,8,3,-8,5,10,8,-8,-5,4,-4,1,2,-6,-2,-6,-4,-1,-8,-3,-5,-10,5,6,5,-9,-7,-10,2,5,-5,-9,3,-10,-8,-4,6,-8,6,-10,-1,7,3,4,-3,7,10,-9,-5,4,9,-8,5,-5,-1,-1,-8,-10,-8,-4,5,-9,1,-8,6,-2,1,2,-10,-9,6,1,10,4,-8,-9,4,-10,5,-1,-9,5,-5,-7,6,3,-6,5,-10,4,-9,-2,2,-6,-7,7,2,-7,-1,-1,2,8,-2,6,3,-9,4,5,-3,-2,-8,8,10,-8,-4,9,-4,-4,1,-8,1,-7,1,2,3,-4,-4,4,10,5,10,9,-3,2,-4,-8,-10,-3,-9,2,-8,4,1,-6,-9,-4,-6,-4,-8,3,-9,-7,8,-7,-5,-10,5,7,-3,8,7,-2,5,-2,-2,-4,-7,-7,3,3,-5,2,-8,-8,3,2,8,-5,-10,5,-3,5,2,-7,8,-2,3,-4,5,2,6,10,-10,6,-1,3,9,-5,2,5,-2,-2,5,7,-8,9,-5,-7,-3,4,-5,9,-7,-7,8,6,1,6,5,-5,4,-6,-3,3,-7,2,-6,-6,-7], dtype = "int32")#candidate|8037|(560,)|const|int32
call_8035 = relay.TupleGetItem(func_533_call(relay.reshape(const_8036.astype('int16'), [13, 15, 11]), relay.reshape(const_8036.astype('int16'), [13, 15, 11]), relay.reshape(const_8037.astype('int32'), [560,]), ), 2)
call_8038 = relay.TupleGetItem(func_537_call(relay.reshape(const_8036.astype('int16'), [13, 15, 11]), relay.reshape(const_8036.astype('int16'), [13, 15, 11]), relay.reshape(const_8037.astype('int32'), [560,]), ), 2)
bop_8043 = relay.greater(call_8035.astype('bool'), call_8029.astype('bool')) # shape=(14, 448)
bop_8046 = relay.greater(call_8038.astype('bool'), call_8030.astype('bool')) # shape=(14, 448)
output = relay.Tuple([const_8036,const_8037,bop_8043,])
output2 = relay.Tuple([const_8036,const_8037,bop_8046,])
func_8049 = relay.Function([], output)
mod['func_8049'] = func_8049
mod = relay.transform.InferType()(mod)
output = func_8049()
func_8050 = relay.Function([], output)
mutated_mod['func_8050'] = func_8050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mod.get_global_var('func_2741')
func_2742_call = mutated_mod.get_global_var('func_2742')
call_8098 = relay.TupleGetItem(func_2741_call(), 3)
call_8099 = relay.TupleGetItem(func_2742_call(), 3)
func_5246_call = mod.get_global_var('func_5246')
func_5247_call = mutated_mod.get_global_var('func_5247')
call_8100 = func_5246_call()
call_8101 = func_5246_call()
output = relay.Tuple([call_8098,call_8100,])
output2 = relay.Tuple([call_8099,call_8101,])
func_8114 = relay.Function([], output)
mod['func_8114'] = func_8114
mod = relay.transform.InferType()(mod)
output = func_8114()
func_8115 = relay.Function([], output)
mutated_mod['func_8115'] = func_8115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4190_call = mod.get_global_var('func_4190')
func_4191_call = mutated_mod.get_global_var('func_4191')
call_8122 = relay.TupleGetItem(func_4190_call(), 1)
call_8123 = relay.TupleGetItem(func_4191_call(), 1)
func_5871_call = mod.get_global_var('func_5871')
func_5873_call = mutated_mod.get_global_var('func_5873')
call_8146 = relay.TupleGetItem(func_5871_call(), 0)
call_8147 = relay.TupleGetItem(func_5873_call(), 0)
var_8161 = relay.var("var_8161", dtype = "int16", shape = (8, 70))#candidate|8161|(8, 70)|var|int16
bop_8162 = relay.maximum(call_8122.astype('uint64'), relay.reshape(var_8161.astype('uint64'), relay.shape_of(call_8122))) # shape=(8, 70)
bop_8165 = relay.maximum(call_8123.astype('uint64'), relay.reshape(var_8161.astype('uint64'), relay.shape_of(call_8123))) # shape=(8, 70)
output = relay.Tuple([call_8146,bop_8162,])
output2 = relay.Tuple([call_8147,bop_8165,])
func_8166 = relay.Function([var_8161,], output)
mod['func_8166'] = func_8166
mod = relay.transform.InferType()(mod)
mutated_mod['func_8166'] = func_8166
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8167 = relay.var("var_8167", dtype = "int16", shape = (8, 70))#candidate|8167|(8, 70)|var|int16
func_8166_call = mutated_mod.get_global_var('func_8166')
call_8168 = func_8166_call(var_8167)
output = call_8168
func_8169 = relay.Function([var_8167], output)
mutated_mod['func_8169'] = func_8169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5252_call = mod.get_global_var('func_5252')
func_5254_call = mutated_mod.get_global_var('func_5254')
call_8175 = relay.TupleGetItem(func_5252_call(), 0)
call_8176 = relay.TupleGetItem(func_5254_call(), 0)
func_5988_call = mod.get_global_var('func_5988')
func_5992_call = mutated_mod.get_global_var('func_5992')
const_8186 = relay.const(True, dtype = "bool")#candidate|8186|()|const|bool
const_8187 = relay.const([[True,True,False,True,False,True,True,False,False,True,False,False],[False,True,True,False,False,True,True,True,True,False,True,False],[True,False,True,False,False,False,False,True,False,True,False,False],[False,False,False,False,True,False,False,True,False,False,False,False],[True,True,True,False,True,False,True,False,True,False,False,True],[False,True,True,False,False,True,False,False,True,False,False,False],[True,False,False,True,False,False,True,False,True,True,False,False],[True,True,True,False,True,True,False,False,False,True,False,False],[False,True,False,False,True,False,False,False,True,False,True,True],[False,True,True,True,False,False,False,True,True,True,False,True],[False,False,True,True,True,True,True,True,False,False,True,False],[False,False,False,True,False,False,True,True,True,False,False,True],[False,False,False,False,True,False,True,False,False,False,True,True],[True,False,True,False,False,False,False,True,False,False,False,True],[False,True,False,True,False,False,False,False,True,True,False,False],[True,True,False,False,True,True,True,True,False,False,True,False],[True,True,True,True,True,False,False,False,True,False,True,True],[True,False,False,False,True,False,False,False,False,True,False,True],[False,False,False,False,False,True,True,True,False,False,True,False],[False,True,False,False,False,True,True,True,True,True,True,False],[False,True,True,False,False,True,True,True,True,False,True,False],[True,False,True,False,True,False,False,True,False,False,True,False],[True,True,True,True,False,False,True,False,True,False,False,False],[False,False,True,True,False,False,True,True,True,True,True,False],[True,True,True,True,True,True,True,True,False,False,False,False],[False,True,True,False,False,True,False,False,True,True,True,True],[True,True,True,False,False,False,False,True,False,False,True,True],[True,False,False,True,True,False,True,True,False,False,True,False],[False,True,False,True,False,True,True,False,False,False,False,False],[False,True,False,False,True,True,False,False,True,False,True,False],[True,False,False,True,True,True,True,True,True,True,False,True],[False,True,True,True,True,False,True,False,True,True,False,False],[False,False,False,False,True,True,False,False,True,False,True,False],[False,False,True,True,True,False,False,True,True,False,False,True],[False,False,True,True,True,True,True,False,False,True,False,True],[False,False,True,True,True,False,False,True,False,True,False,True],[True,False,False,True,False,True,False,False,True,True,True,False],[False,False,False,False,True,False,True,True,True,False,True,False],[False,True,True,False,False,True,True,False,True,False,True,False],[True,True,False,False,False,False,False,False,False,True,True,False]], dtype = "bool")#candidate|8187|(40, 12)|const|bool
call_8185 = func_5988_call(relay.reshape(const_8186.astype('bool'), []), relay.reshape(const_8187.astype('bool'), [15, 2, 16]), )
call_8188 = func_5988_call(relay.reshape(const_8186.astype('bool'), []), relay.reshape(const_8187.astype('bool'), [15, 2, 16]), )
func_7428_call = mod.get_global_var('func_7428')
func_7430_call = mutated_mod.get_global_var('func_7430')
call_8209 = func_7428_call()
call_8210 = func_7428_call()
func_4754_call = mod.get_global_var('func_4754')
func_4757_call = mutated_mod.get_global_var('func_4757')
var_8221 = relay.var("var_8221", dtype = "float64", shape = (96,))#candidate|8221|(96,)|var|float64
call_8220 = func_4754_call(relay.reshape(var_8221.astype('float64'), [8, 2, 6]))
call_8222 = func_4754_call(relay.reshape(var_8221.astype('float64'), [8, 2, 6]))
func_7515_call = mod.get_global_var('func_7515')
func_7518_call = mutated_mod.get_global_var('func_7518')
var_8227 = relay.var("var_8227", dtype = "bool", shape = (336,))#candidate|8227|(336,)|var|bool
call_8226 = relay.TupleGetItem(func_7515_call(relay.reshape(var_8227.astype('bool'), [3, 7, 16])), 2)
call_8228 = relay.TupleGetItem(func_7518_call(relay.reshape(var_8227.astype('bool'), [3, 7, 16])), 2)
func_4267_call = mod.get_global_var('func_4267')
func_4269_call = mutated_mod.get_global_var('func_4269')
call_8240 = relay.TupleGetItem(func_4267_call(), 3)
call_8241 = relay.TupleGetItem(func_4269_call(), 3)
uop_8254 = relay.sigmoid(call_8185.astype('float32')) # shape=(15, 2, 16)
uop_8256 = relay.sigmoid(call_8188.astype('float32')) # shape=(15, 2, 16)
func_1884_call = mod.get_global_var('func_1884')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_8267 = func_1884_call()
call_8268 = func_1884_call()
output = relay.Tuple([call_8175,const_8186,const_8187,call_8209,call_8220,var_8221,call_8226,var_8227,call_8240,uop_8254,call_8267,])
output2 = relay.Tuple([call_8176,const_8186,const_8187,call_8210,call_8222,var_8221,call_8228,var_8227,call_8241,uop_8256,call_8268,])
func_8288 = relay.Function([var_8221,var_8227,], output)
mod['func_8288'] = func_8288
mod = relay.transform.InferType()(mod)
var_8289 = relay.var("var_8289", dtype = "float64", shape = (96,))#candidate|8289|(96,)|var|float64
var_8290 = relay.var("var_8290", dtype = "bool", shape = (336,))#candidate|8290|(336,)|var|bool
output = func_8288(var_8289,var_8290,)
func_8291 = relay.Function([var_8289,var_8290,], output)
mutated_mod['func_8291'] = func_8291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8310 = relay.var("var_8310", dtype = "int64", shape = (5, 9, 16))#candidate|8310|(5, 9, 16)|var|int64
var_8311 = relay.var("var_8311", dtype = "int64", shape = (5, 9, 16))#candidate|8311|(5, 9, 16)|var|int64
bop_8312 = relay.bitwise_or(var_8310.astype('int64'), relay.reshape(var_8311.astype('int64'), relay.shape_of(var_8310))) # shape=(5, 9, 16)
func_7239_call = mod.get_global_var('func_7239')
func_7240_call = mutated_mod.get_global_var('func_7240')
call_8321 = func_7239_call()
call_8322 = func_7239_call()
func_3311_call = mod.get_global_var('func_3311')
func_3314_call = mutated_mod.get_global_var('func_3314')
const_8331 = relay.const([-9,-3,4,-6,-6,-8,1,2,-1,7,-3,5,-4,-6,-7,-6,-5,7,-8,4,5,6,3,-8,-8,-2,-7,-10,-10,-9,-1,-3,2,6,2,6,4,-7,-10,1,7,1,-10,6,-1,-7,8,1,-2,1,-8,3,-9,-9,3,-6,-5,6,-2,-7,9,-7,6,8,4,-3,-8,-4,-7,5,7,4,-10,9,-5,7,10,1,-2,3,-2,-10,-3,9,-9,3,6,10,-8,-2,-5,4,-2,1,-6,2,3,10,6,7,4,3,-5,-9,-10,-3,9,10,4,7,-8,-2,1,-6,-1,-4,10,4,8,8,4,3,-3,-7,6,9,-5,4,2,4,-4,-8,-6,2,8,4,-3,7,1,3,10,-1,4,2,7,1,6,6,4,8,9,-5,-10,-10,-8,6,6,4,3,8,-4,1,-8,6,6,5,-7,-10,3,-7,3,-9,-1,9,-1,-5,-5,6,5,5,-5,9,-1,10,8,-6,-1,10,-10,-7,7,5,-10,3,-3,7,9,2,6,3,-9,5,-6,1,5,4,-10,3,-1,5,5,4,1,-5,9,-1,8,6,2,-7,-5,-10,-1,-7,9,6,8,-9,7,-4,-1,3,-2,1,-8,2,1,-2,-4,5,-5,-5,-3,1,-8,6,-1,-9,10,6,2,5,7,8,-10,-5,5,7,-6,-8,3,-4,-5,-7,6,-4,1,-2,1,-2,-2,-4,-6,-7,-7,-7,-10,-7,5,-9,9,-7,-7,1,-8,8,9,-9,3,7,2,4,-4,-7,7,10,-3,10,-8,9,5,8,-9,1,2,4,4,5,9,9,-10,-5,7,-5,6,1,-1,-7,5,-2,8,10,-4,-9,7,-10,-6,9,10,-8], dtype = "uint16")#candidate|8331|(330,)|const|uint16
call_8330 = relay.TupleGetItem(func_3311_call(relay.reshape(const_8331.astype('uint16'), [11, 5, 6])), 0)
call_8332 = relay.TupleGetItem(func_3314_call(relay.reshape(const_8331.astype('uint16'), [11, 5, 6])), 0)
bop_8347 = relay.power(bop_8312.astype('float32'), relay.reshape(var_8311.astype('float32'), relay.shape_of(bop_8312))) # shape=(5, 9, 16)
bop_8356 = relay.left_shift(var_8311.astype('uint8'), relay.reshape(bop_8347.astype('uint8'), relay.shape_of(var_8311))) # shape=(5, 9, 16)
output = relay.Tuple([call_8321,call_8330,const_8331,bop_8356,])
output2 = relay.Tuple([call_8322,call_8332,const_8331,bop_8356,])
F = relay.Function([var_8310,var_8311,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8310,var_8311,], output2)
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
