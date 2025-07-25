import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_36 = relay.const(5, dtype = "int16")#candidate|36|()|const|int16
var_37 = relay.var("var_37", dtype = "int16", shape = (15, 6, 5))#candidate|37|(15, 6, 5)|var|int16
bop_38 = relay.left_shift(const_36.astype('int16'), var_37.astype('int16')) # shape=(15, 6, 5)
var_44 = relay.var("var_44", dtype = "int16", shape = (15, 6, 5))#candidate|44|(15, 6, 5)|var|int16
bop_45 = relay.mod(var_37.astype('float32'), relay.reshape(var_44.astype('float32'), relay.shape_of(var_37))) # shape=(15, 6, 5)
output = relay.Tuple([bop_38,bop_45,])
output2 = relay.Tuple([bop_38,bop_45,])
func_54 = relay.Function([var_37,var_44,], output)
mod['func_54'] = func_54
mod = relay.transform.InferType()(mod)
var_55 = relay.var("var_55", dtype = "int16", shape = (15, 6, 5))#candidate|55|(15, 6, 5)|var|int16
var_56 = relay.var("var_56", dtype = "int16", shape = (15, 6, 5))#candidate|56|(15, 6, 5)|var|int16
output = func_54(var_55,var_56,)
func_57 = relay.Function([var_55,var_56,], output)
mutated_mod['func_57'] = func_57
mutated_mod = relay.transform.InferType()(mutated_mod)
var_356 = relay.var("var_356", dtype = "float32", shape = ())#candidate|356|()|var|float32
var_357 = relay.var("var_357", dtype = "float32", shape = (4, 1, 4))#candidate|357|(4, 1, 4)|var|float32
bop_358 = relay.floor_divide(var_356.astype('float32'), var_357.astype('float32')) # shape=(4, 1, 4)
output = bop_358
output2 = bop_358
func_361 = relay.Function([var_356,var_357,], output)
mod['func_361'] = func_361
mod = relay.transform.InferType()(mod)
var_362 = relay.var("var_362", dtype = "float32", shape = ())#candidate|362|()|var|float32
var_363 = relay.var("var_363", dtype = "float32", shape = (4, 1, 4))#candidate|363|(4, 1, 4)|var|float32
output = func_361(var_362,var_363,)
func_364 = relay.Function([var_362,var_363,], output)
mutated_mod['func_364'] = func_364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_428 = relay.var("var_428", dtype = "float32", shape = (12, 4, 1))#candidate|428|(12, 4, 1)|var|float32
uop_429 = relay.acos(var_428.astype('float32')) # shape=(12, 4, 1)
bop_433 = relay.subtract(uop_429.astype('uint8'), relay.reshape(var_428.astype('uint8'), relay.shape_of(uop_429))) # shape=(12, 4, 1)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
var_438 = relay.var("var_438", dtype = "int16", shape = (450,))#candidate|438|(450,)|var|int16
call_437 = relay.TupleGetItem(func_54_call(relay.reshape(var_438.astype('int16'), [15, 6, 5]), relay.reshape(var_438.astype('int16'), [15, 6, 5]), ), 1)
call_439 = relay.TupleGetItem(func_57_call(relay.reshape(var_438.astype('int16'), [15, 6, 5]), relay.reshape(var_438.astype('int16'), [15, 6, 5]), ), 1)
func_361_call = mod.get_global_var('func_361')
func_364_call = mutated_mod.get_global_var('func_364')
var_456 = relay.var("var_456", dtype = "float32", shape = ())#candidate|456|()|var|float32
const_457 = relay.const([-7.292972,-1.172498,8.301297,9.825039,8.764988,-5.084243,-6.774315,-3.871046,9.259592,0.886178,1.265501,-6.945771,6.216138,-6.025340,4.334736,5.257063], dtype = "float32")#candidate|457|(16,)|const|float32
call_455 = func_361_call(relay.reshape(var_456.astype('float32'), []), relay.reshape(const_457.astype('float32'), [4, 1, 4]), )
call_458 = func_361_call(relay.reshape(var_456.astype('float32'), []), relay.reshape(const_457.astype('float32'), [4, 1, 4]), )
bop_462 = relay.logical_and(uop_429.astype('bool'), var_438.astype('bool')) # shape=(12, 4, 450)
func_361_call = mod.get_global_var('func_361')
func_364_call = mutated_mod.get_global_var('func_364')
call_477 = func_361_call(relay.reshape(var_456.astype('float32'), []), relay.reshape(const_457.astype('float32'), [4, 1, 4]), )
call_478 = func_361_call(relay.reshape(var_456.astype('float32'), []), relay.reshape(const_457.astype('float32'), [4, 1, 4]), )
bop_479 = relay.power(bop_433.astype('float32'), const_457.astype('float32')) # shape=(12, 4, 16)
uop_492 = relay.sin(bop_462.astype('float64')) # shape=(12, 4, 450)
uop_494 = relay.atanh(uop_492.astype('float64')) # shape=(12, 4, 450)
bop_498 = relay.add(uop_494.astype('uint8'), relay.reshape(bop_462.astype('uint8'), relay.shape_of(uop_494))) # shape=(12, 4, 450)
uop_505 = relay.acosh(bop_462.astype('float32')) # shape=(12, 4, 450)
output = relay.Tuple([call_437,call_455,var_456,call_477,bop_479,bop_498,uop_505,])
output2 = relay.Tuple([call_439,call_458,var_456,call_478,bop_479,bop_498,uop_505,])
func_507 = relay.Function([var_428,var_438,var_456,], output)
mod['func_507'] = func_507
mod = relay.transform.InferType()(mod)
var_508 = relay.var("var_508", dtype = "float32", shape = (12, 4, 1))#candidate|508|(12, 4, 1)|var|float32
var_509 = relay.var("var_509", dtype = "int16", shape = (450,))#candidate|509|(450,)|var|int16
var_510 = relay.var("var_510", dtype = "float32", shape = ())#candidate|510|()|var|float32
output = func_507(var_508,var_509,var_510,)
func_511 = relay.Function([var_508,var_509,var_510,], output)
mutated_mod['func_511'] = func_511
mutated_mod = relay.transform.InferType()(mutated_mod)
var_513 = relay.var("var_513", dtype = "float64", shape = (13, 15, 3))#candidate|513|(13, 15, 3)|var|float64
uop_514 = relay.rsqrt(var_513.astype('float64')) # shape=(13, 15, 3)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
var_523 = relay.var("var_523", dtype = "int16", shape = (450,))#candidate|523|(450,)|var|int16
call_522 = relay.TupleGetItem(func_54_call(relay.reshape(var_523.astype('int16'), [15, 6, 5]), relay.reshape(var_523.astype('int16'), [15, 6, 5]), ), 1)
call_524 = relay.TupleGetItem(func_57_call(relay.reshape(var_523.astype('int16'), [15, 6, 5]), relay.reshape(var_523.astype('int16'), [15, 6, 5]), ), 1)
output = relay.Tuple([uop_514,call_522,var_523,])
output2 = relay.Tuple([uop_514,call_524,var_523,])
func_538 = relay.Function([var_513,var_523,], output)
mod['func_538'] = func_538
mod = relay.transform.InferType()(mod)
var_539 = relay.var("var_539", dtype = "float64", shape = (13, 15, 3))#candidate|539|(13, 15, 3)|var|float64
var_540 = relay.var("var_540", dtype = "int16", shape = (450,))#candidate|540|(450,)|var|int16
output = func_538(var_539,var_540,)
func_541 = relay.Function([var_539,var_540,], output)
mutated_mod['func_541'] = func_541
mutated_mod = relay.transform.InferType()(mutated_mod)
var_819 = relay.var("var_819", dtype = "float32", shape = (10, 16, 4))#candidate|819|(10, 16, 4)|var|float32
uop_820 = relay.cos(var_819.astype('float32')) # shape=(10, 16, 4)
bop_823 = relay.floor_mod(var_819.astype('float64'), relay.reshape(uop_820.astype('float64'), relay.shape_of(var_819))) # shape=(10, 16, 4)
uop_842 = relay.rsqrt(var_819.astype('float32')) # shape=(10, 16, 4)
output = relay.Tuple([bop_823,uop_842,])
output2 = relay.Tuple([bop_823,uop_842,])
func_846 = relay.Function([var_819,], output)
mod['func_846'] = func_846
mod = relay.transform.InferType()(mod)
var_847 = relay.var("var_847", dtype = "float32", shape = (10, 16, 4))#candidate|847|(10, 16, 4)|var|float32
output = func_846(var_847)
func_848 = relay.Function([var_847], output)
mutated_mod['func_848'] = func_848
mutated_mod = relay.transform.InferType()(mutated_mod)
const_862 = relay.const([[[True,False,False,True,True,True,False,False,True,False],[False,True,True,True,True,False,False,False,True,False],[False,False,False,True,False,True,True,True,False,False],[True,True,False,True,True,True,False,True,True,True],[True,False,True,False,True,False,False,False,False,False],[False,False,False,False,False,True,True,True,False,False]],[[True,True,True,True,False,False,False,False,True,False],[False,False,False,True,True,True,True,True,True,True],[True,True,True,False,False,True,True,True,False,True],[True,True,False,True,False,False,True,True,False,True],[True,False,True,True,True,False,False,False,False,False],[True,True,True,True,True,True,False,False,True,True]],[[True,False,False,True,True,True,True,True,False,False],[False,True,False,True,False,False,False,False,False,False],[False,False,True,False,True,True,True,True,True,False],[False,True,True,True,False,False,False,False,True,False],[False,True,True,False,True,True,False,True,True,True],[True,False,True,False,False,False,True,True,True,True]],[[False,False,False,True,True,False,True,True,False,True],[True,False,False,False,True,True,True,True,False,False],[False,True,False,True,False,False,True,True,False,True],[False,False,True,False,True,False,True,False,True,True],[True,False,False,False,False,True,True,True,False,False],[True,True,True,False,False,True,False,False,True,False]],[[True,True,False,False,False,True,False,True,False,True],[False,True,True,False,True,True,True,True,False,False],[True,True,True,False,True,True,False,False,True,True],[False,False,False,True,False,False,False,False,True,False],[True,False,False,False,False,True,True,False,False,True],[False,True,True,True,False,False,False,False,False,False]],[[True,True,False,True,False,True,False,False,True,True],[True,True,True,True,True,False,False,True,False,True],[False,False,False,True,True,False,False,True,False,False],[True,True,True,False,True,True,True,True,False,False],[False,True,True,False,False,True,False,False,False,False],[True,False,False,False,False,True,False,False,False,True]],[[False,False,False,False,False,True,True,True,False,True],[True,True,False,True,True,False,False,True,True,False],[True,False,False,True,False,False,False,True,False,False],[False,True,False,False,True,False,False,False,True,False],[False,True,True,False,False,False,True,False,True,False],[False,False,False,False,True,True,True,True,False,True]],[[False,False,False,False,False,True,True,False,False,False],[True,False,True,False,False,True,True,True,True,False],[True,True,True,False,False,False,True,True,False,True],[False,False,True,True,False,True,False,True,False,False],[False,True,False,True,True,True,True,False,False,False],[True,False,False,False,False,False,False,True,True,False]],[[False,True,False,True,False,True,False,True,False,False],[True,False,True,False,False,True,True,True,True,True],[True,False,True,True,False,True,True,True,False,False],[True,False,False,False,True,False,True,False,True,True],[False,True,False,False,True,False,True,False,True,False],[True,False,True,True,False,True,False,True,False,True]],[[False,False,True,False,False,True,False,True,True,False],[False,True,True,False,True,False,False,False,False,True],[True,True,False,False,False,False,True,True,True,False],[False,True,False,True,True,False,False,False,True,True],[False,True,True,True,False,False,True,False,True,True],[False,False,False,False,False,True,False,True,False,True]],[[True,False,True,True,True,False,True,False,False,False],[True,False,False,False,True,False,True,False,False,False],[True,False,False,False,False,False,True,False,True,True],[False,True,True,True,False,False,True,False,False,False],[False,False,False,False,False,False,False,True,False,True],[True,False,True,True,False,False,True,True,False,True]],[[False,False,False,True,True,False,True,True,False,False],[True,True,False,True,True,False,True,False,False,False],[True,True,False,False,True,False,False,False,True,True],[True,True,True,True,False,True,False,True,False,False],[True,True,True,True,False,True,False,False,True,False],[False,False,True,False,False,False,False,True,True,True]],[[False,False,False,True,False,False,False,False,True,False],[False,True,True,False,False,False,True,False,False,False],[False,False,False,False,False,False,False,False,True,True],[True,True,False,True,True,False,True,True,False,False],[False,False,True,True,False,False,True,True,False,True],[True,True,True,True,True,True,False,True,True,True]]], dtype = "bool")#candidate|862|(13, 6, 10)|const|bool
var_863 = relay.var("var_863", dtype = "bool", shape = (13, 6, 10))#candidate|863|(13, 6, 10)|var|bool
bop_864 = relay.logical_and(const_862.astype('bool'), relay.reshape(var_863.astype('bool'), relay.shape_of(const_862))) # shape=(13, 6, 10)
var_869 = relay.var("var_869", dtype = "bool", shape = (13, 6, 10))#candidate|869|(13, 6, 10)|var|bool
bop_870 = relay.greater_equal(bop_864.astype('bool'), relay.reshape(var_869.astype('bool'), relay.shape_of(bop_864))) # shape=(13, 6, 10)
output = relay.Tuple([bop_870,])
output2 = relay.Tuple([bop_870,])
func_874 = relay.Function([var_863,var_869,], output)
mod['func_874'] = func_874
mod = relay.transform.InferType()(mod)
mutated_mod['func_874'] = func_874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_874_call = mutated_mod.get_global_var('func_874')
var_876 = relay.var("var_876", dtype = "bool", shape = (13, 6, 10))#candidate|876|(13, 6, 10)|var|bool
var_877 = relay.var("var_877", dtype = "bool", shape = (13, 6, 10))#candidate|877|(13, 6, 10)|var|bool
call_875 = func_874_call(var_876,var_877,)
output = call_875
func_878 = relay.Function([var_876,var_877,], output)
mutated_mod['func_878'] = func_878
mutated_mod = relay.transform.InferType()(mutated_mod)
var_891 = relay.var("var_891", dtype = "int8", shape = (14, 4, 13))#candidate|891|(14, 4, 13)|var|int8
var_892 = relay.var("var_892", dtype = "int8", shape = (14, 4, 13))#candidate|892|(14, 4, 13)|var|int8
bop_893 = relay.logical_xor(var_891.astype('int8'), relay.reshape(var_892.astype('int8'), relay.shape_of(var_891))) # shape=(14, 4, 13)
output = bop_893
output2 = bop_893
func_899 = relay.Function([var_891,var_892,], output)
mod['func_899'] = func_899
mod = relay.transform.InferType()(mod)
var_900 = relay.var("var_900", dtype = "int8", shape = (14, 4, 13))#candidate|900|(14, 4, 13)|var|int8
var_901 = relay.var("var_901", dtype = "int8", shape = (14, 4, 13))#candidate|901|(14, 4, 13)|var|int8
output = func_899(var_900,var_901,)
func_902 = relay.Function([var_900,var_901,], output)
mutated_mod['func_902'] = func_902
mutated_mod = relay.transform.InferType()(mutated_mod)
var_962 = relay.var("var_962", dtype = "uint64", shape = (7, 14, 10))#candidate|962|(7, 14, 10)|var|uint64
var_963 = relay.var("var_963", dtype = "uint64", shape = (7, 14, 10))#candidate|963|(7, 14, 10)|var|uint64
bop_964 = relay.not_equal(var_962.astype('bool'), relay.reshape(var_963.astype('bool'), relay.shape_of(var_962))) # shape=(7, 14, 10)
bop_968 = relay.bitwise_or(bop_964.astype('int8'), relay.reshape(var_963.astype('int8'), relay.shape_of(bop_964))) # shape=(7, 14, 10)
output = bop_968
output2 = bop_968
func_972 = relay.Function([var_962,var_963,], output)
mod['func_972'] = func_972
mod = relay.transform.InferType()(mod)
var_973 = relay.var("var_973", dtype = "uint64", shape = (7, 14, 10))#candidate|973|(7, 14, 10)|var|uint64
var_974 = relay.var("var_974", dtype = "uint64", shape = (7, 14, 10))#candidate|974|(7, 14, 10)|var|uint64
output = func_972(var_973,var_974,)
func_975 = relay.Function([var_973,var_974,], output)
mutated_mod['func_975'] = func_975
mutated_mod = relay.transform.InferType()(mutated_mod)
var_980 = relay.var("var_980", dtype = "float32", shape = (1, 4, 7))#candidate|980|(1, 4, 7)|var|float32
uop_981 = relay.sinh(var_980.astype('float32')) # shape=(1, 4, 7)
output = relay.Tuple([uop_981,])
output2 = relay.Tuple([uop_981,])
func_986 = relay.Function([var_980,], output)
mod['func_986'] = func_986
mod = relay.transform.InferType()(mod)
var_987 = relay.var("var_987", dtype = "float32", shape = (1, 4, 7))#candidate|987|(1, 4, 7)|var|float32
output = func_986(var_987)
func_988 = relay.Function([var_987], output)
mutated_mod['func_988'] = func_988
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1076 = relay.var("var_1076", dtype = "int32", shape = (14, 16, 12))#candidate|1076|(14, 16, 12)|var|int32
var_1077 = relay.var("var_1077", dtype = "int32", shape = (14, 16, 12))#candidate|1077|(14, 16, 12)|var|int32
bop_1078 = relay.less_equal(var_1076.astype('bool'), relay.reshape(var_1077.astype('bool'), relay.shape_of(var_1076))) # shape=(14, 16, 12)
output = relay.Tuple([bop_1078,])
output2 = relay.Tuple([bop_1078,])
func_1095 = relay.Function([var_1076,var_1077,], output)
mod['func_1095'] = func_1095
mod = relay.transform.InferType()(mod)
mutated_mod['func_1095'] = func_1095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mutated_mod.get_global_var('func_1095')
var_1097 = relay.var("var_1097", dtype = "int32", shape = (14, 16, 12))#candidate|1097|(14, 16, 12)|var|int32
var_1098 = relay.var("var_1098", dtype = "int32", shape = (14, 16, 12))#candidate|1098|(14, 16, 12)|var|int32
call_1096 = func_1095_call(var_1097,var_1098,)
output = call_1096
func_1099 = relay.Function([var_1097,var_1098,], output)
mutated_mod['func_1099'] = func_1099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1489 = relay.var("var_1489", dtype = "float64", shape = (6, 3, 7))#candidate|1489|(6, 3, 7)|var|float64
uop_1490 = relay.rsqrt(var_1489.astype('float64')) # shape=(6, 3, 7)
output = uop_1490
output2 = uop_1490
func_1492 = relay.Function([var_1489,], output)
mod['func_1492'] = func_1492
mod = relay.transform.InferType()(mod)
var_1493 = relay.var("var_1493", dtype = "float64", shape = (6, 3, 7))#candidate|1493|(6, 3, 7)|var|float64
output = func_1492(var_1493)
func_1494 = relay.Function([var_1493], output)
mutated_mod['func_1494'] = func_1494
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1806 = relay.var("var_1806", dtype = "float64", shape = (9, 9, 6))#candidate|1806|(9, 9, 6)|var|float64
uop_1807 = relay.sinh(var_1806.astype('float64')) # shape=(9, 9, 6)
uop_1809 = relay.acos(uop_1807.astype('float32')) # shape=(9, 9, 6)
func_846_call = mod.get_global_var('func_846')
func_848_call = mutated_mod.get_global_var('func_848')
var_1837 = relay.var("var_1837", dtype = "float32", shape = (640,))#candidate|1837|(640,)|var|float32
call_1836 = relay.TupleGetItem(func_846_call(relay.reshape(var_1837.astype('float32'), [10, 16, 4])), 0)
call_1838 = relay.TupleGetItem(func_848_call(relay.reshape(var_1837.astype('float32'), [10, 16, 4])), 0)
bop_1840 = relay.add(uop_1807.astype('float64'), relay.reshape(var_1806.astype('float64'), relay.shape_of(uop_1807))) # shape=(9, 9, 6)
var_1846 = relay.var("var_1846", dtype = "float32", shape = (9, 9, 6))#candidate|1846|(9, 9, 6)|var|float32
bop_1847 = relay.bitwise_xor(uop_1809.astype('uint16'), relay.reshape(var_1846.astype('uint16'), relay.shape_of(uop_1809))) # shape=(9, 9, 6)
output = relay.Tuple([call_1836,var_1837,bop_1840,bop_1847,])
output2 = relay.Tuple([call_1838,var_1837,bop_1840,bop_1847,])
func_1862 = relay.Function([var_1806,var_1837,var_1846,], output)
mod['func_1862'] = func_1862
mod = relay.transform.InferType()(mod)
mutated_mod['func_1862'] = func_1862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1862_call = mutated_mod.get_global_var('func_1862')
var_1864 = relay.var("var_1864", dtype = "float64", shape = (9, 9, 6))#candidate|1864|(9, 9, 6)|var|float64
var_1865 = relay.var("var_1865", dtype = "float32", shape = (640,))#candidate|1865|(640,)|var|float32
var_1866 = relay.var("var_1866", dtype = "float32", shape = (9, 9, 6))#candidate|1866|(9, 9, 6)|var|float32
call_1863 = func_1862_call(var_1864,var_1865,var_1866,)
output = call_1863
func_1867 = relay.Function([var_1864,var_1865,var_1866,], output)
mutated_mod['func_1867'] = func_1867
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1966 = relay.var("var_1966", dtype = "float32", shape = (6, 3, 6))#candidate|1966|(6, 3, 6)|var|float32
uop_1967 = relay.cos(var_1966.astype('float32')) # shape=(6, 3, 6)
func_507_call = mod.get_global_var('func_507')
func_511_call = mutated_mod.get_global_var('func_511')
var_1972 = relay.var("var_1972", dtype = "float32", shape = (12, 4))#candidate|1972|(12, 4)|var|float32
const_1973 = relay.const([-4,-7,3,-9,6,-1,7,3,1,-6,9,-4,-7,-7,1,7,3,8,-7,-10,-6,-3,-6,-4,2,1,-7,4,-2,-8,-5,10,2,3,-8,6,3,8,6,6,3,1,-4,1,-6,-9,-7,10,-1,-1,-7,3,-8,9,3,4,-3,-6,-10,5,8,-8,4,-8,-2,-2,-8,6,5,2,1,4,10,2,-6,7,-2,-3,-4,1,-10,2,-9,-3,-4,-2,2,-8,3,4,7,-5,6,-5,-9,-6,-1,-8,-7,-5,-8,5,-1,2,-2,-5,-8,8,-8,-6,-1,-7,-1,1,8,10,-2,-5,9,-7,4,2,2,-7,4,1,-8,-8,-3,-6,6,6,2,-1,9,-3,-9,6,-8,-6,-8,10,5,-2,8,1,7,-1,1,1,-7,-4,1,2,2,-4,4,6,-1,-10,-8,10,-10,-4,1,2,2,-8,5,4,7,10,9,3,-4,-8,3,10,9,6,-1,-1,6,8,9,-1,-8,-8,-6,-9,-3,7,-5,3,10,7,10,6,9,-7,6,5,-10,-2,-5,1,10,-5,-4,2,-10,7,8,5,-9,-6,-2,-10,-7,3,7,-1,1,-1,-6,8,3,5,-3,7,-3,-9,-5,9,3,-3,5,5,-1,8,-1,-3,-4,-6,-9,10,-7,6,8,-3,7,-1,-3,6,-5,3,-3,-2,7,5,-10,-5,-2,10,-8,10,10,-8,8,-9,10,-2,-8,-9,2,-10,-9,-3,8,2,6,-1,-3,-1,3,-5,10,4,-4,5,-9,2,2,10,7,-7,-3,-1,-7,9,-10,1,-4,10,-9,5,3,-9,-1,6,2,2,2,-4,-4,7,9,-4,4,-2,2,-3,3,2,3,-3,-1,-10,8,10,-9,6,6,5,-7,-4,-2,-3,-1,10,-3,8,-10,7,-4,-10,5,-5,9,10,4,-4,-1,3,4,-5,-8,2,-1,6,5,10,-5,10,2,-9,-4,-5,1,-8,-3,5,7,-1,-4,4,4,-9,1,-10,-9,-1,1,-1,-6,-1,-3,-4,2,9,-2,-5,-8,-3,4,-4,-4,10,-1,-10,-2,-9,7,-7,7,-7,10,-5,-6,9,-4,5,-6,-3,-7,-7,6,-6,-9,4,-7,-5,4,-5,-10,2,-7,-10,-3,-1,8,9,-6,-8,6,-1,6,-1,-7,1,-3,9,-10,-3,6,1,-4,9,-5,-4], dtype = "int16")#candidate|1973|(450,)|const|int16
const_1974 = relay.const(-7.477730, dtype = "float32")#candidate|1974|()|const|float32
call_1971 = relay.TupleGetItem(func_507_call(relay.reshape(var_1972.astype('float32'), [12, 4, 1]), relay.reshape(const_1973.astype('int16'), [450,]), relay.reshape(const_1974.astype('float32'), []), ), 3)
call_1975 = relay.TupleGetItem(func_511_call(relay.reshape(var_1972.astype('float32'), [12, 4, 1]), relay.reshape(const_1973.astype('int16'), [450,]), relay.reshape(const_1974.astype('float32'), []), ), 3)
output = relay.Tuple([uop_1967,call_1971,var_1972,const_1973,const_1974,])
output2 = relay.Tuple([uop_1967,call_1975,var_1972,const_1973,const_1974,])
func_1982 = relay.Function([var_1966,var_1972,], output)
mod['func_1982'] = func_1982
mod = relay.transform.InferType()(mod)
mutated_mod['func_1982'] = func_1982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1982_call = mutated_mod.get_global_var('func_1982')
var_1984 = relay.var("var_1984", dtype = "float32", shape = (6, 3, 6))#candidate|1984|(6, 3, 6)|var|float32
var_1985 = relay.var("var_1985", dtype = "float32", shape = (12, 4))#candidate|1985|(12, 4)|var|float32
call_1983 = func_1982_call(var_1984,var_1985,)
output = call_1983
func_1986 = relay.Function([var_1984,var_1985,], output)
mutated_mod['func_1986'] = func_1986
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2027 = relay.var("var_2027", dtype = "float32", shape = (4, 4, 4))#candidate|2027|(4, 4, 4)|var|float32
uop_2028 = relay.asin(var_2027.astype('float32')) # shape=(4, 4, 4)
output = relay.Tuple([uop_2028,])
output2 = relay.Tuple([uop_2028,])
func_2038 = relay.Function([var_2027,], output)
mod['func_2038'] = func_2038
mod = relay.transform.InferType()(mod)
var_2039 = relay.var("var_2039", dtype = "float32", shape = (4, 4, 4))#candidate|2039|(4, 4, 4)|var|float32
output = func_2038(var_2039)
func_2040 = relay.Function([var_2039], output)
mutated_mod['func_2040'] = func_2040
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2046 = relay.const([[[-2,1,2,-7,6,-8,-7,-10,-1]],[[-4,-10,-5,-10,-1,6,-10,-7,-8]],[[-8,5,-10,6,-1,2,9,-5,6]],[[-5,-6,-9,-4,-1,-7,-1,3,1]],[[-9,9,-3,2,-8,-3,8,-3,6]],[[-7,8,-3,-8,-1,10,-4,-9,1]]], dtype = "int8")#candidate|2046|(6, 1, 9)|const|int8
var_2047 = relay.var("var_2047", dtype = "int8", shape = (6, 1, 9))#candidate|2047|(6, 1, 9)|var|int8
bop_2048 = relay.subtract(const_2046.astype('int8'), relay.reshape(var_2047.astype('int8'), relay.shape_of(const_2046))) # shape=(6, 1, 9)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
var_2052 = relay.var("var_2052", dtype = "int16", shape = (450, 1))#candidate|2052|(450, 1)|var|int16
call_2051 = relay.TupleGetItem(func_54_call(relay.reshape(var_2052.astype('int16'), [15, 6, 5]), relay.reshape(var_2052.astype('int16'), [15, 6, 5]), ), 1)
call_2053 = relay.TupleGetItem(func_57_call(relay.reshape(var_2052.astype('int16'), [15, 6, 5]), relay.reshape(var_2052.astype('int16'), [15, 6, 5]), ), 1)
output = relay.Tuple([bop_2048,call_2051,var_2052,])
output2 = relay.Tuple([bop_2048,call_2053,var_2052,])
func_2054 = relay.Function([var_2047,var_2052,], output)
mod['func_2054'] = func_2054
mod = relay.transform.InferType()(mod)
var_2055 = relay.var("var_2055", dtype = "int8", shape = (6, 1, 9))#candidate|2055|(6, 1, 9)|var|int8
var_2056 = relay.var("var_2056", dtype = "int16", shape = (450, 1))#candidate|2056|(450, 1)|var|int16
output = func_2054(var_2055,var_2056,)
func_2057 = relay.Function([var_2055,var_2056,], output)
mutated_mod['func_2057'] = func_2057
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2356 = relay.var("var_2356", dtype = "int16", shape = (2, 9, 11))#candidate|2356|(2, 9, 11)|var|int16
var_2357 = relay.var("var_2357", dtype = "int16", shape = (2, 9, 11))#candidate|2357|(2, 9, 11)|var|int16
bop_2358 = relay.not_equal(var_2356.astype('bool'), relay.reshape(var_2357.astype('bool'), relay.shape_of(var_2356))) # shape=(2, 9, 11)
output = bop_2358
output2 = bop_2358
func_2361 = relay.Function([var_2356,var_2357,], output)
mod['func_2361'] = func_2361
mod = relay.transform.InferType()(mod)
var_2362 = relay.var("var_2362", dtype = "int16", shape = (2, 9, 11))#candidate|2362|(2, 9, 11)|var|int16
var_2363 = relay.var("var_2363", dtype = "int16", shape = (2, 9, 11))#candidate|2363|(2, 9, 11)|var|int16
output = func_2361(var_2362,var_2363,)
func_2364 = relay.Function([var_2362,var_2363,], output)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2496 = relay.var("var_2496", dtype = "uint64", shape = ())#candidate|2496|()|var|uint64
var_2497 = relay.var("var_2497", dtype = "uint64", shape = (1, 14, 16))#candidate|2497|(1, 14, 16)|var|uint64
bop_2498 = relay.logical_xor(var_2496.astype('uint64'), var_2497.astype('uint64')) # shape=(1, 14, 16)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_2518 = relay.const([2,-1,10,2,-9,-1,4,-3,-9,4,3,-7,-6,5,2,3,5,-8,8,-8,10,5,1,-10,6,-10,2,3,2,7,-9,-9,-6,9,8,2,-5,1,-8,-8,-5,-5,-8,6,8,8,-4,2,-6,6,8,-2,-7,-1,-4,-1,-9,-7,-7,-9,-6,4,5,-2,7,-5,-5,10,-7,-9,9,-9,8,-5,9,-2,4,7,-2,-10,-6,-5,-9,-7,5,-7,-7,3,4,-2,6,8,-2,9,3,-6,-2,3,6,-8,-5,-5,3,10,10,10,8,5,-2,-7,-2,7,-1,-5,-8,10,-10,-8,5,-10,-1,-2,-10,-10,-3,-1,-9,-9,7,-9,-9,-10,4,-9,7,-5,-2,9,5,-6,8,3,4,-10,-8,-7,8,3,9,-2,-5,-7,5,9,-7,8,2,7,-3,-8,5,-9,7,6,8,-2,-4,-10,-7,9,-5,1,6,5,4,4,1,4,-7,-3,6,-6,6,-9,4,-7,3,-6,6,2,-5,1,10,-5,4,10,5,2,9,-2,-1,1,7,-5,-9,4,3,-1,1,-8,5,-6,-3,10,4,-6,-1,1,6,-10,4,2,-9,10,10,4,-7,6,1,-3,-9,9,10,7,-5,5,-3,7,-10,4,5,7,-10,-4,-10,7,-10,9,-4,7,5,1,9,-4,2,-2,7,3,-2,-2,3,-10,-6,2,7,-1,3,2,7,2,-5,-10,-2,4,9,-4,3,-5,5,1,9,4,-4,-4,4,2,-8,6,5,-4,3,-7,4,-7,3,10,-10,6,5,-4,-5,10,1,5,-5,-2,-1,-9,5,5,-6,2,3,9,-5,7,-3,5,-5,2,1,10,-7,6,-5,-1,-8,-6,-8,-7,9,-5,2,-6,10,9,-6,-1,6,-6,-8,3,-8,7,3,3,7,-4,-7,8,-10,9,5,-10,9,3,3,-5,4,-8,-3,9,-8,1,-5,5,7,3,5,-5,9,4,-6,2,-9,7,1,4,-10,7,7,3,5,7,1,-6,2,4,-9,9,9,1,-3,1,3,9,1,5,-9,-8,4,3,-4,-5,-5,2,-10,6,-8,-7,9,1,9,6,8,-10,-7,-10,2,-5,-2,3,-10,7,9,10,-1,6,7,-8,5,7,1,-5,3,-1,7,-8,4,4,9,-9,-5,10,6,-6,8,-5,3,5], dtype = "int16")#candidate|2518|(450,)|const|int16
call_2517 = relay.TupleGetItem(func_54_call(relay.reshape(const_2518.astype('int16'), [15, 6, 5]), relay.reshape(const_2518.astype('int16'), [15, 6, 5]), ), 1)
call_2519 = relay.TupleGetItem(func_57_call(relay.reshape(const_2518.astype('int16'), [15, 6, 5]), relay.reshape(const_2518.astype('int16'), [15, 6, 5]), ), 1)
output = relay.Tuple([bop_2498,call_2517,const_2518,])
output2 = relay.Tuple([bop_2498,call_2519,const_2518,])
func_2525 = relay.Function([var_2496,var_2497,], output)
mod['func_2525'] = func_2525
mod = relay.transform.InferType()(mod)
mutated_mod['func_2525'] = func_2525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2525_call = mutated_mod.get_global_var('func_2525')
var_2527 = relay.var("var_2527", dtype = "uint64", shape = ())#candidate|2527|()|var|uint64
var_2528 = relay.var("var_2528", dtype = "uint64", shape = (1, 14, 16))#candidate|2528|(1, 14, 16)|var|uint64
call_2526 = func_2525_call(var_2527,var_2528,)
output = call_2526
func_2529 = relay.Function([var_2527,var_2528,], output)
mutated_mod['func_2529'] = func_2529
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2557 = relay.const([[[5.787875,-1.734659,9.300026,2.515201,8.594198,-5.601512,5.776280,0.169018],[5.923059,9.055643,3.754877,-4.276262,3.949484,-9.088423,-3.551420,1.445399],[6.656156,-8.795588,-0.529791,-0.245534,6.457219,-4.520677,3.676967,9.715481],[1.044192,-8.786688,-7.801825,-6.261972,1.287642,7.393742,4.030611,-9.627466],[-9.616113,7.683155,-1.398951,-5.591998,9.012061,5.458068,6.433111,9.845791],[4.920612,4.619680,-2.834679,-8.938558,6.005923,-7.859613,-2.593161,2.456917],[1.652366,4.242542,-3.890750,8.981307,-0.556495,-0.929382,3.618183,-5.676019],[9.138592,-3.566376,-3.168876,-0.544042,-6.302593,-1.642293,0.127709,6.295029],[-2.013265,-8.437020,5.404764,-6.384434,-7.848450,3.009315,4.806438,7.352253],[0.262687,-6.695842,-2.519399,7.826921,1.815611,9.539017,7.808805,2.720203],[3.716792,-8.942022,2.306924,-3.021976,7.308198,2.947008,-8.072926,-6.740967],[-5.092066,1.359432,5.975273,5.838662,-8.996648,9.604806,-4.183241,4.413965]],[[-9.302377,-0.815922,8.385529,-2.411800,-6.061090,0.426925,-4.415284,-9.416526],[-5.042933,0.870984,4.746313,8.239833,6.680837,9.501898,0.294471,4.818765],[6.961690,-8.123104,-0.449991,7.329674,-7.248185,7.104562,-8.456455,-1.458057],[8.991156,-8.025902,-4.494201,-4.826362,-8.272536,8.465203,0.005950,-8.148944],[-1.885700,6.417348,3.404715,5.773568,5.132663,-0.702758,1.698984,-5.691655],[-1.049755,3.418447,-9.688177,-4.531499,3.661166,9.907262,-5.508059,4.680273],[-7.151922,2.804852,-7.072132,7.132196,-8.915625,7.065613,-9.518074,-3.173734],[3.447481,-8.825767,-8.304906,-2.141560,-5.971472,-0.191278,4.322287,-2.181757],[-9.172453,5.286005,-0.359032,-0.626544,-5.786925,-2.086044,5.676408,7.570853],[-1.849266,3.112825,-1.840218,8.845581,2.840740,6.182710,9.732392,-7.514957],[-6.969787,-7.367774,-6.809849,5.739999,3.901741,-8.769719,-4.186235,2.504879],[5.988737,9.251292,-3.186938,-9.471963,-1.476362,3.326203,7.080714,2.915621]],[[3.195677,5.766800,-7.982452,1.000582,-8.347274,2.840410,9.727037,-7.945964],[3.737337,5.782103,-8.736812,1.220670,9.565753,-2.466370,-5.960525,-2.349321],[-3.463599,1.824199,-4.718596,-2.522302,-0.266175,-5.336539,-7.342096,-2.043044],[-8.617707,3.976524,-5.891196,-5.645411,2.677614,-7.162987,-1.218824,-5.647449],[-2.459624,-8.342083,-4.854968,-8.874407,-2.319103,-7.551673,3.128534,-1.032530],[-5.944445,-6.969013,-7.609778,9.336866,5.514292,2.399069,-9.512393,-4.363224],[3.176719,-3.238553,3.239168,6.900404,8.670871,-6.904844,-2.119027,-2.354520],[0.501732,8.558317,0.306008,9.379099,4.412913,5.560129,-5.344684,-1.463195],[-6.235139,0.857583,6.336050,9.337416,4.514911,6.302726,-5.882626,-1.221188],[-8.036344,1.671017,-1.816426,3.340631,1.583698,-1.193270,-1.733813,5.021214],[4.577679,2.669561,3.704517,8.898786,-9.659757,5.595177,-7.017237,-9.390397],[5.599640,4.599046,8.382148,1.515400,2.991430,-7.587123,9.045635,-6.374980]],[[2.739883,2.323404,-0.506726,0.198242,-6.808143,4.393784,-9.333884,6.817597],[0.655968,-8.386370,8.448721,5.655944,7.102667,0.304582,8.693001,4.672642],[5.741578,-2.689377,8.721171,-1.019575,-2.020492,-2.867164,-8.848822,-5.545391],[-6.430740,-6.592553,0.534644,-8.328674,0.935867,3.745902,2.549950,9.201504],[3.027847,-6.606807,0.453587,-2.891811,-1.960437,8.023646,0.689378,-1.773639],[-7.385268,8.617456,-9.040816,-1.734624,3.088917,0.470746,-8.037477,9.842334],[-0.439661,-9.025058,3.695312,8.500184,7.142217,-4.576754,-2.010219,4.869813],[1.547006,-0.179096,-3.459014,4.165969,-5.250666,0.383487,-4.981187,0.280919],[-9.991356,-5.930701,-8.772507,-7.354552,-8.746418,-7.950358,6.239001,8.682799],[0.015889,8.460985,-0.552389,8.918180,8.334809,3.465720,-5.253408,-8.980852],[-0.765988,-3.518734,-9.590245,5.766527,0.463150,5.447328,5.899231,2.122198],[4.688280,-4.533300,5.757029,-1.773862,-1.889782,-0.700562,-0.957559,-9.898292]],[[-0.900388,-6.660222,4.159378,4.322821,5.135190,5.453428,-5.001484,1.684420],[5.141875,2.527151,-4.889629,6.425936,-8.866682,8.555764,-6.224776,5.878273],[-1.580290,5.898942,8.036873,-1.055181,-9.495924,2.275340,-7.265603,-2.127640],[8.740190,-1.752575,0.153783,-4.966679,-4.246894,9.391520,1.736620,5.359586],[-4.557552,6.006674,6.605926,-5.447828,-0.114709,-6.185395,2.510547,-0.832624],[0.109271,-6.735220,8.878155,-2.881847,-8.194513,-0.905017,-3.894639,2.365942],[1.383367,5.139859,-0.193429,-9.128415,6.825655,8.743422,1.404544,1.008902],[-8.936791,5.831573,7.555805,1.653550,8.289836,7.642048,4.520389,-5.635582],[-3.111405,-2.703079,-4.189173,0.724259,4.073630,-2.659571,-0.269820,3.431680],[4.632175,-6.669243,-7.179598,-9.444699,-5.228307,-9.334902,-7.167570,-7.143800],[-4.500154,5.201330,7.255240,-7.427919,1.830172,1.851556,8.417898,-9.717372],[0.643904,7.281225,7.438448,-7.202922,8.645352,0.360924,7.196399,-0.937736]],[[-9.351415,-2.922444,-9.370736,2.705308,8.083499,-5.887847,5.268175,8.578039],[2.601900,6.848392,-3.051850,-2.593496,-6.567946,4.199359,1.983681,0.196008],[9.198609,5.276598,-5.593561,1.153488,1.061996,-1.912287,3.504182,-3.777237],[-4.660276,4.265349,2.094092,2.929480,3.304484,2.044749,-0.804552,3.824318],[5.086184,-2.070906,3.102865,9.052613,1.001300,1.325969,-8.402726,6.020428],[0.605396,5.266470,2.289455,-6.805895,-8.580310,2.342511,-7.898178,-9.021364],[-8.746839,-3.117965,3.305849,-4.677997,5.144733,3.253893,2.706147,8.692081],[2.361826,0.409161,0.888454,1.508583,-9.598912,-8.562655,2.273036,-6.403778],[4.463204,1.545761,-3.159763,6.055052,-6.837979,1.873750,-2.327703,-8.848176],[-6.291432,-3.625583,-3.722623,0.834948,-4.860001,6.244267,-4.277551,2.643118],[-8.724708,-4.998771,0.179441,4.533920,-6.949370,6.385469,2.278391,-6.511564],[-5.286380,7.712771,2.829697,0.543896,-0.829283,4.578139,-5.220498,6.444770]],[[-6.160916,1.497349,2.984551,8.014128,-0.793248,-7.422051,-2.983570,6.553163],[4.915982,8.978876,1.912109,0.361119,-2.430327,-1.230437,1.706904,4.636970],[-8.197873,6.074958,6.340938,9.997556,-7.415933,5.411755,3.236645,7.234358],[0.776247,7.172403,8.489634,6.743508,4.465150,-3.558210,7.691163,-4.183239],[-9.982066,0.412048,-4.077408,6.300941,1.114106,-9.811671,0.280453,0.169086],[-8.819111,1.720966,2.858897,4.353275,1.895017,-0.516139,-2.930527,-7.168435],[-6.684100,-2.220713,-6.745052,5.244301,6.741173,-7.152262,0.039535,4.335314],[-3.264880,1.237512,9.377821,9.868968,-2.042014,1.463755,-6.532340,-4.599855],[-4.662437,-3.333908,-6.588699,-7.665641,7.772234,8.432205,-8.662388,-1.387466],[2.066139,6.561601,9.065818,0.630315,-1.200983,-9.979248,-0.200418,8.751313],[4.625624,-9.240861,-9.692629,9.616157,0.559754,-9.825451,-5.646071,4.001232],[4.408964,-4.083934,7.439795,-5.421124,9.390279,-3.179337,4.151309,-5.243850]],[[3.551552,0.205547,3.313397,2.174812,7.178119,-8.353860,8.887656,1.780255],[-0.136786,3.177916,-2.631754,8.945364,-1.382596,1.641488,-9.783680,-7.892531],[-4.717362,6.278613,2.006778,1.467492,-5.183472,-7.302608,4.464634,-0.244049],[4.309160,3.117902,-6.019296,2.590801,-8.689648,-0.570825,-5.307369,5.649729],[-7.354167,-3.105962,2.263224,-9.624420,-4.414724,1.525324,5.962878,9.643440],[7.141613,-6.971152,-9.071092,-6.433402,-6.654955,6.904604,-6.432163,-9.652751],[0.002290,-4.660883,-8.525674,-3.830133,7.022959,-5.123498,-3.314079,5.030918],[-4.132766,2.075998,-2.685710,5.124345,-5.341716,0.015079,8.142606,-3.710003],[4.434292,-6.343037,7.415898,-7.936690,-5.637378,3.774869,-7.564349,6.960414],[-3.823258,7.593801,-8.757107,-3.768636,2.090956,2.704928,1.691134,7.685741],[-9.797043,-9.712473,6.833478,-5.308412,4.574904,-6.349102,1.920100,-4.014507],[-1.211042,-9.520869,-5.181470,6.333668,-0.031486,9.300420,-6.246186,-0.699724]],[[-3.249550,1.221527,0.393387,4.333030,3.653003,0.740023,4.386082,8.426723],[1.098115,6.818429,-9.730277,-0.407051,2.251447,-1.524127,-9.282621,0.024798],[3.876778,-6.203020,-5.113920,0.815217,4.590226,-5.235079,-7.974669,-3.196918],[4.184359,5.282746,2.686694,3.258653,6.586884,-0.633580,-0.943109,-6.217028],[-9.483534,2.718224,1.170858,5.294578,3.694356,0.176190,1.363922,4.024573],[9.706781,-5.539177,-4.002681,-8.445940,1.392460,-4.608785,-3.190294,9.655080],[5.237930,6.157555,5.187439,-8.842180,8.382280,-5.395467,9.630434,2.265531],[-8.253978,7.520905,8.679039,6.802165,7.235368,4.605518,-2.168270,-2.281290],[7.453939,-5.630095,-3.965562,5.816693,5.711641,-7.593755,8.097542,5.509518],[6.997283,0.577224,-7.284681,3.236584,-8.251027,2.547040,8.198034,-1.063232],[-5.690196,6.277375,3.410588,-5.998752,-8.342494,-3.842025,-1.194527,-1.047395],[-3.883562,4.587721,-1.810694,-8.568258,8.346088,6.545548,-6.221455,5.026767]],[[6.237192,2.561795,9.177051,1.629646,2.684581,1.554578,7.171528,9.865824],[6.154440,1.888224,-9.840368,-3.923922,4.261623,-6.741267,-9.793246,-3.730659],[1.576973,-7.419991,6.384748,-3.872438,7.818594,5.769442,9.483818,0.291531],[4.553230,-3.337142,-5.120586,9.581615,7.676444,8.871273,2.736842,6.175025],[-9.004443,9.986053,9.946257,-8.814673,0.904541,9.082513,-3.752990,-7.817164],[1.477595,1.745314,2.588217,-0.380918,0.476556,-2.238146,5.147829,1.011264],[-3.407239,-6.665161,-9.551993,-6.738193,-8.971758,3.616190,-7.806891,-9.804645],[-6.040105,-7.751601,-5.931992,-7.859326,-3.339849,-8.722433,-9.974937,3.364996],[-8.759446,-3.231078,-8.858914,-4.671183,3.045295,-5.640991,6.582170,3.086350],[-7.252138,-6.251383,-0.906717,-3.412542,7.007960,4.052943,-9.494741,-9.008856],[-6.757162,-4.195722,-8.900037,6.490192,-5.131941,8.909222,-7.246525,5.547083],[-4.437064,1.013294,6.608857,-6.247108,-6.986664,-5.278586,-8.471738,1.986602]]], dtype = "float32")#candidate|2557|(10, 12, 8)|const|float32
uop_2558 = relay.acosh(const_2557.astype('float32')) # shape=(10, 12, 8)
func_507_call = mod.get_global_var('func_507')
func_511_call = mutated_mod.get_global_var('func_511')
const_2585 = relay.const([1.316208,9.029774,2.401510,3.957939,9.408894,-8.801500,7.396178,0.414520,-3.616084,-1.688415,7.105476,-2.300958,3.491913,-0.614470,-9.564500,-9.635195,-3.176309,-7.589672,8.433939,5.198987,-9.416003,8.557359,-7.474625,-2.688079,-6.823427,-9.930654,9.481563,-2.490371,-1.921757,2.774251,-1.228953,-1.828451,6.582865,-0.347709,8.984173,7.664832,9.307601,5.277897,-0.838276,4.761931,-4.168630,-7.572131,-4.723058,-5.053177,2.655690,2.018306,0.627359,-3.170638], dtype = "float32")#candidate|2585|(48,)|const|float32
const_2586 = relay.const([-3,-1,5,4,10,10,-8,-5,7,-2,9,-1,7,3,6,-10,-2,-2,10,-5,-3,-10,-7,8,5,6,-8,-5,6,-10,7,-9,-3,-5,10,-5,6,4,10,-5,3,-1,8,-7,5,7,9,10,-7,-7,7,-10,7,4,7,4,-3,-1,10,-5,7,-8,8,-8,-5,1,-5,6,-4,-9,2,-1,8,-5,-9,-5,2,3,-1,2,6,-9,6,-4,6,1,7,-2,-3,-3,-7,9,2,-7,10,1,5,-6,-5,-1,-4,-10,6,7,-9,10,-9,-3,-10,5,2,-6,8,-9,-4,6,5,-10,10,-8,8,-4,8,9,10,8,2,8,-7,4,7,3,6,3,-3,-4,1,-9,7,-5,-3,-8,8,-6,-3,10,10,4,-7,5,-7,10,-9,7,6,-3,-6,6,9,10,-4,-1,-2,-4,1,-8,8,-10,-4,3,10,10,8,-1,10,8,10,10,-6,2,2,10,7,-7,7,-4,7,-3,10,2,5,-3,1,8,6,7,-1,9,6,-2,7,10,-10,7,-6,9,8,6,-7,-7,8,2,10,1,1,-9,-9,-10,-1,-10,-7,8,-5,7,3,-5,-9,-2,10,6,-7,10,3,7,-9,3,-8,-5,7,4,-5,3,-6,4,-6,-9,-5,-9,1,4,-4,7,-8,-4,-4,7,7,-3,4,-3,8,-3,3,3,9,3,4,5,2,-7,10,-6,-5,-2,-8,9,-8,-9,6,4,-9,9,9,-3,7,-7,-5,6,6,9,4,10,-2,-3,-10,4,-6,-1,10,5,-6,-6,9,-5,1,-9,-3,9,7,-2,10,6,-10,10,3,-9,10,-1,7,-4,-9,-3,9,8,3,4,-7,-1,7,8,9,-10,1,7,-7,-6,1,1,-1,-7,8,-10,-2,-1,-2,-9,-6,-9,-10,7,-5,-8,-2,8,7,-10,5,-9,10,-5,10,-3,-5,-5,9,6,7,-10,-2,-2,4,-3,1,7,3,4,-8,-2,-1,9,1,4,9,6,-2,2,10,6,-7,-3,-5,-4,5,-7,4,-4,3,-2,-2,8,7,-2,5,-10,-9,3,-1,-8,-4,3,-2,3,-7,-10,3,4,5,-9,-4,-3,4,-8,6,3,8,7,5,7,-7,2,4,10,-2,10,-7,-8,2,6,-9,-7,7,8,6,-3,-2,-10,10,6,6,7], dtype = "int16")#candidate|2586|(450,)|const|int16
var_2587 = relay.var("var_2587", dtype = "float32", shape = ())#candidate|2587|()|var|float32
call_2584 = relay.TupleGetItem(func_507_call(relay.reshape(const_2585.astype('float32'), [12, 4, 1]), relay.reshape(const_2586.astype('int16'), [450,]), relay.reshape(var_2587.astype('float32'), []), ), 3)
call_2588 = relay.TupleGetItem(func_511_call(relay.reshape(const_2585.astype('float32'), [12, 4, 1]), relay.reshape(const_2586.astype('int16'), [450,]), relay.reshape(var_2587.astype('float32'), []), ), 3)
func_986_call = mod.get_global_var('func_986')
func_988_call = mutated_mod.get_global_var('func_988')
var_2590 = relay.var("var_2590", dtype = "float32", shape = (28,))#candidate|2590|(28,)|var|float32
call_2589 = relay.TupleGetItem(func_986_call(relay.reshape(var_2590.astype('float32'), [1, 4, 7])), 0)
call_2591 = relay.TupleGetItem(func_988_call(relay.reshape(var_2590.astype('float32'), [1, 4, 7])), 0)
output = relay.Tuple([uop_2558,call_2584,const_2585,const_2586,var_2587,call_2589,var_2590,])
output2 = relay.Tuple([uop_2558,call_2588,const_2585,const_2586,var_2587,call_2591,var_2590,])
func_2604 = relay.Function([var_2587,var_2590,], output)
mod['func_2604'] = func_2604
mod = relay.transform.InferType()(mod)
var_2605 = relay.var("var_2605", dtype = "float32", shape = ())#candidate|2605|()|var|float32
var_2606 = relay.var("var_2606", dtype = "float32", shape = (28,))#candidate|2606|(28,)|var|float32
output = func_2604(var_2605,var_2606,)
func_2607 = relay.Function([var_2605,var_2606,], output)
mutated_mod['func_2607'] = func_2607
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2693 = relay.var("var_2693", dtype = "float64", shape = (9, 4, 1))#candidate|2693|(9, 4, 1)|var|float64
uop_2694 = relay.atanh(var_2693.astype('float64')) # shape=(9, 4, 1)
output = relay.Tuple([uop_2694,])
output2 = relay.Tuple([uop_2694,])
func_2702 = relay.Function([var_2693,], output)
mod['func_2702'] = func_2702
mod = relay.transform.InferType()(mod)
var_2703 = relay.var("var_2703", dtype = "float64", shape = (9, 4, 1))#candidate|2703|(9, 4, 1)|var|float64
output = func_2702(var_2703)
func_2704 = relay.Function([var_2703], output)
mutated_mod['func_2704'] = func_2704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2880 = relay.var("var_2880", dtype = "float32", shape = (16, 10, 10))#candidate|2880|(16, 10, 10)|var|float32
uop_2881 = relay.log(var_2880.astype('float32')) # shape=(16, 10, 10)
uop_2883 = relay.log2(var_2880.astype('float32')) # shape=(16, 10, 10)
output = relay.Tuple([uop_2881,uop_2883,])
output2 = relay.Tuple([uop_2881,uop_2883,])
func_2886 = relay.Function([var_2880,], output)
mod['func_2886'] = func_2886
mod = relay.transform.InferType()(mod)
var_2887 = relay.var("var_2887", dtype = "float32", shape = (16, 10, 10))#candidate|2887|(16, 10, 10)|var|float32
output = func_2886(var_2887)
func_2888 = relay.Function([var_2887], output)
mutated_mod['func_2888'] = func_2888
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3026 = relay.var("var_3026", dtype = "float32", shape = (1, 1, 15))#candidate|3026|(1, 1, 15)|var|float32
uop_3027 = relay.exp(var_3026.astype('float32')) # shape=(1, 1, 15)
var_3030 = relay.var("var_3030", dtype = "float32", shape = (11, 1, 15))#candidate|3030|(11, 1, 15)|var|float32
bop_3031 = relay.add(uop_3027.astype('int32'), var_3030.astype('int32')) # shape=(11, 1, 15)
bop_3035 = relay.maximum(bop_3031.astype('float32'), uop_3027.astype('float32')) # shape=(11, 1, 15)
uop_3047 = relay.acos(bop_3035.astype('float32')) # shape=(11, 1, 15)
output = relay.Tuple([uop_3047,])
output2 = relay.Tuple([uop_3047,])
func_3052 = relay.Function([var_3026,var_3030,], output)
mod['func_3052'] = func_3052
mod = relay.transform.InferType()(mod)
mutated_mod['func_3052'] = func_3052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3052_call = mutated_mod.get_global_var('func_3052')
var_3054 = relay.var("var_3054", dtype = "float32", shape = (1, 1, 15))#candidate|3054|(1, 1, 15)|var|float32
var_3055 = relay.var("var_3055", dtype = "float32", shape = (11, 1, 15))#candidate|3055|(11, 1, 15)|var|float32
call_3053 = func_3052_call(var_3054,var_3055,)
output = call_3053
func_3056 = relay.Function([var_3054,var_3055,], output)
mutated_mod['func_3056'] = func_3056
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3239 = relay.const([[[6,3,6,-7,-10,-5],[9,9,-8,4,2,5],[9,8,2,1,7,-1],[-4,3,-7,-2,-8,2],[2,5,-5,3,-10,7],[-6,2,-2,8,1,-9],[10,5,-2,3,-2,-9],[1,-10,-10,-4,7,2],[1,5,-3,-10,-8,8],[1,-6,-2,-1,-7,-5],[-10,-5,-9,6,9,3],[8,3,-8,7,-4,4],[8,-8,-10,1,-4,-7],[-3,2,-6,4,-8,-1]],[[-1,8,1,-1,1,1],[-4,9,9,10,9,-6],[9,-1,8,-5,-8,4],[7,8,7,-9,-4,-9],[-4,-6,5,8,-3,-2],[10,-2,2,-10,3,7],[9,-9,4,-5,8,-1],[-5,-6,-1,9,-8,2],[9,9,1,-2,-1,5],[-10,4,-4,-3,-8,-7],[-9,-10,9,5,5,-10],[9,1,2,7,-6,1],[8,9,3,6,-2,9],[10,9,-9,6,-8,9]],[[-10,-5,-7,-6,-10,-2],[-3,-7,5,-6,3,2],[4,-9,2,-4,4,1],[-6,6,-4,-1,7,1],[7,8,-3,-1,8,-1],[7,5,7,-3,-2,8],[-7,10,10,-5,1,6],[-2,10,6,10,-9,7],[10,-8,8,8,-9,-7],[-2,-6,6,4,7,-7],[9,8,-4,-3,-2,-7],[-9,6,-3,-6,5,-7],[-4,-8,7,5,7,-4],[-6,-7,10,-1,-9,8]]], dtype = "uint8")#candidate|3239|(3, 14, 6)|const|uint8
var_3240 = relay.var("var_3240", dtype = "uint8", shape = (3, 14, 6))#candidate|3240|(3, 14, 6)|var|uint8
bop_3241 = relay.subtract(const_3239.astype('uint8'), relay.reshape(var_3240.astype('uint8'), relay.shape_of(const_3239))) # shape=(3, 14, 6)
uop_3247 = relay.acos(var_3240.astype('float32')) # shape=(3, 14, 6)
uop_3249 = relay.sigmoid(uop_3247.astype('float64')) # shape=(3, 14, 6)
func_972_call = mod.get_global_var('func_972')
func_975_call = mutated_mod.get_global_var('func_975')
const_3264 = relay.const([-5,1,6,-2,-8,4,2,6,9,8,-2,1,7,-9,-7,2,3,-1,5,-6,2,10,3,3,8,10,-2,-5,-6,-1,1,5,9,5,-1,8,4,-7,-6,8,6,1,3,-6,-4,-10,-2,-1,10,6,8,5,4,8,4,3,8,-5,-1,9,-2,2,-5,7,-10,7,9,-1,-3,2,-9,-7,-8,-9,5,-6,-9,1,1,9,2,-1,-9,-3,-5,10,-9,-10,-9,-8,9,1,2,3,-1,9,10,4,4,10,2,3,6,10,4,-2,-4,2,7,3,10,3,2,7,-7,-5,-10,-10,-4,4,10,3,-10,-2,-2,9,7,-10,-1,4,8,9,-2,4,1,5,5,7,-5,-4,-6,-9,-5,9,-7,-6,-6,3,-3,-3,-5,8,-4,-5,6,6,-2,-2,-3,7,-7,5,9,9,-6,-8,9,-3,3,-4,9,8,2,-10,-4,-4,-1,2,10,-4,6,-7,8,-9,-8,-9,-2,8,-8,10,-7,-2,-5,8,6,2,-4,6,-9,-4,-8,3,1,-4,2,-2,8,7,8,3,-9,-7,-3,4,10,10,2,-7,-7,-3,-7,-9,-1,-2,-4,-5,7,-6,5,-4,-10,2,-10,-5,4,-7,5,5,4,4,-2,3,-1,2,10,10,10,2,-4,6,-6,-8,1,-8,-3,-7,1,6,10,9,-6,10,2,-8,8,4,-9,7,-8,-6,-9,-5,4,4,1,-4,4,-5,-5,-5,-6,-10,-3,-8,-4,-1,-9,5,10,-7,-5,-10,-4,-7,7,-3,3,2,10,9,4,9,10,7,3,3,-5,-9,7,10,-6,-8,8,-6,-8,4,-7,-3,7,7,4,-10,-2,-7,-2,2,10,10,-8,6,-3,7,-3,7,10,2,3,-2,10,5,-6,2,8,4,8,3,-4,1,1,-9,-1,7,-2,2,-8,-4,5,8,9,9,-6,1,5,7,-2,-8,-5,1,-6,9,-10,-6,-10,8,8,9,4,-4,-5,-4,5,-2,-9,-8,-5,-8,-2,2,9,-3,9,-3,-3,-9,-5,-5,-9,3,-1,-4,9,-3,-6,-3,5,4,-8,-9,1,9,-3,8,-3,-1,-3,-1,4,-3,1,5,-2,1,3,10,10,-2,6,-4,-3,3,9,-6,10,-3,-5,-8,-7,-4,-9,-6,6,1,-10,-10,1,8,-9,-2,6,-1,-4,-8,8,-3,8,7,9,-5,4,-3,1,4,8,1,9,-4,3,-6,-4,1,8,8,-7,-8,8,-7,-5,-1,4,8,5,8,6,8,-5,-3,-6,-2,-4,5,6,-3,10,-7,-5,10,8,6,4,-5,-5,-3,1,-6,-10,9,1,-6,-5,5,-7,-9,-5,-1,3,7,6,10,7,-2,-5,2,4,-6,2,-10,6,-6,-6,-9,4,-6,-8,-8,10,-4,1,-10,-6,4,10,9,-3,7,3,-8,-6,7,-3,-10,3,10,10,2,6,3,10,-2,-6,-4,-8,6,-1,7,6,-4,1,-6,4,6,4,8,1,10,-2,8,9,2,-7,-3,-6,5,-3,-10,-10,8,8,-1,7,-8,-8,-9,-2,-8,-1,5,7,9,-2,-6,-7,-10,10,4,3,-8,-2,-7,-1,-5,-5,2,-10,-10,1,-9,-10,-1,-8,-10,1,-3,7,7,-4,-10,1,-1,-6,7,6,-4,-3,-7,-4,-4,-6,-7,-7,-3,-7,2,-9,-2,3,-10,3,7,1,-9,-2,-9,1,5,2,-3,-3,8,-7,4,-10,-10,8,-1,1,3,6,-6,-10,9,9,1,-6,-1,-1,-4,9,6,-1,-8,8,8,3,-2,-4,-5,2,4,-8,10,10,-2,8,-6,-4,3,-6,-5,6,-4,-8,-3,8,6,-2,5,2,9,-5,1,1,-3,-7,-8,8,3,-4,6,-6,9,-1,-8,-4,-5,5,-10,9,3,-2,1,6,5,2,3,-4,-6,9,-7,4,-9,7,-5,-3,-4,-3,6,-9,-1,-2,1,-9,10,2,10,-1,-6,10,-7,-2,-9,-4,-6,6,3,6,-4,10,4,5,-1,2,-5,9,-5,-2,7,9,-6,1,-5,-3,3,-4,7,-8,8,-6,-2,6,7,2,-2,7,8,-9,-4,-1,-10,-3,-6,5,-1,-6,7,8,10,8,-1,-1,-3,-1,5,-6,-8,-1,-10,-10,-9,-3,10,2,3,1,-5,4,-3,6,8,-4,-1,-3,-3,-3,9,3,-1,-9,-5,10,-3,7,-1,7,-3,8,-5,-6,-3,-3,6,4,-10,-2,5,2,-8,7,10,-1,-2,10,1,8,-6,8,8,1,-9,3,-9,-4,-4,8,-3,-10,9,6,7,-4,6,6,8,-4,-2,-2,1,-8,7,2,7,8,-1,6,8,-2,-5,-2,8,1,2,3,-9,2,-8,-7,6,3,-8,7,10,-4,-8,10,-10,-7,6,10,10,-1,-6,-3,4,2,-4,9,8,3,-8,3,-5,4,10,-7,6,9,6,4,8,3,-5,-8,-4,1,3,3,4,-7,1,-5,2,7,-5,-10,-7,5,-3,-4,-3,2,1,-1,-3,1,4,9,1,-6,8,-9,8,4,-8,-2,-5,6,10,-1,8,6,-8], dtype = "uint64")#candidate|3264|(980,)|const|uint64
call_3263 = func_972_call(relay.reshape(const_3264.astype('uint64'), [7, 14, 10]), relay.reshape(const_3264.astype('uint64'), [7, 14, 10]), )
call_3265 = func_972_call(relay.reshape(const_3264.astype('uint64'), [7, 14, 10]), relay.reshape(const_3264.astype('uint64'), [7, 14, 10]), )
func_2038_call = mod.get_global_var('func_2038')
func_2040_call = mutated_mod.get_global_var('func_2040')
const_3276 = relay.const([[-8.513451,-3.199764,0.763644,2.074398,3.113382,7.247456,-3.275057,0.043512,-3.367387,-4.568846,7.833008,-6.405275,-1.678318,0.062801,-4.969463,-5.597299,9.876995,-7.620929,3.689934,-6.662987,-6.705813,6.360167,-0.142455,5.417442,-7.885162,4.361959,-0.582495,-8.725273,5.121308,-0.533452,-4.132450,-4.361835,3.524206,-9.835879,4.057256,2.761334,0.311354,-2.102683,3.735301,-9.937136,2.079489,2.680102,3.261213,3.109046,0.133941,5.420601,-9.845943,5.491172,-9.124627,7.115332,-4.906880,5.292788,4.006067,-1.246690,5.468675,-3.301508,-3.185389,9.854478,6.831469,-6.070498,-2.028012,0.963728,-6.805785,-2.510352]], dtype = "float32")#candidate|3276|(1, 64)|const|float32
call_3275 = relay.TupleGetItem(func_2038_call(relay.reshape(const_3276.astype('float32'), [4, 4, 4])), 0)
call_3277 = relay.TupleGetItem(func_2040_call(relay.reshape(const_3276.astype('float32'), [4, 4, 4])), 0)
uop_3289 = relay.acosh(uop_3247.astype('float64')) # shape=(3, 14, 6)
bop_3292 = relay.maximum(uop_3289.astype('uint64'), relay.reshape(bop_3241.astype('uint64'), relay.shape_of(uop_3289))) # shape=(3, 14, 6)
func_1095_call = mod.get_global_var('func_1095')
func_1099_call = mutated_mod.get_global_var('func_1099')
var_3296 = relay.var("var_3296", dtype = "int32", shape = (2688,))#candidate|3296|(2688,)|var|int32
call_3295 = relay.TupleGetItem(func_1095_call(relay.reshape(var_3296.astype('int32'), [14, 16, 12]), relay.reshape(var_3296.astype('int32'), [14, 16, 12]), ), 0)
call_3297 = relay.TupleGetItem(func_1099_call(relay.reshape(var_3296.astype('int32'), [14, 16, 12]), relay.reshape(var_3296.astype('int32'), [14, 16, 12]), ), 0)
output = relay.Tuple([uop_3249,call_3263,const_3264,call_3275,const_3276,bop_3292,call_3295,var_3296,])
output2 = relay.Tuple([uop_3249,call_3265,const_3264,call_3277,const_3276,bop_3292,call_3297,var_3296,])
func_3298 = relay.Function([var_3240,var_3296,], output)
mod['func_3298'] = func_3298
mod = relay.transform.InferType()(mod)
var_3299 = relay.var("var_3299", dtype = "uint8", shape = (3, 14, 6))#candidate|3299|(3, 14, 6)|var|uint8
var_3300 = relay.var("var_3300", dtype = "int32", shape = (2688,))#candidate|3300|(2688,)|var|int32
output = func_3298(var_3299,var_3300,)
func_3301 = relay.Function([var_3299,var_3300,], output)
mutated_mod['func_3301'] = func_3301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3322 = relay.var("var_3322", dtype = "float32", shape = ())#candidate|3322|()|var|float32
const_3323 = relay.const([[[-2.183017,-2.001897,-6.137216,-2.997021,2.689771,0.745056,-0.443096,8.265493,1.256579,3.532784,-6.003253],[6.408639,-8.799974,-2.280347,-7.016219,1.777937,2.157672,-8.676159,-0.672507,-4.525804,7.110826,-8.580106],[-7.908078,1.261787,-0.353829,-8.441859,-2.804623,-1.098395,-1.420610,-9.243497,9.597707,4.923856,3.391514],[-9.250082,-8.563315,-1.635834,4.958023,-1.983420,-5.308988,5.274913,-9.378435,-9.724982,8.592283,8.826467],[2.385752,1.288234,9.812794,3.437739,-5.778177,2.049177,-5.405518,5.995894,-5.420785,-5.808972,4.223775],[-8.184710,6.167304,-4.885336,4.593086,-9.041691,9.890939,5.650168,-0.532712,0.459142,4.856577,-2.677631],[-7.523247,9.182396,0.287798,-8.918776,7.341648,-1.433250,2.945549,-6.101754,8.120238,3.095574,-1.712463],[6.632823,-4.089340,9.983097,0.302315,9.230884,0.344777,9.938896,-0.317585,8.055646,-7.099799,7.635725]],[[-0.307991,-3.033930,-1.911131,-3.890208,4.641619,-1.698451,6.833245,7.754149,5.224689,-1.697359,0.693993],[6.471885,0.433565,9.183789,-1.344246,7.586532,-7.481123,-9.763749,-8.773413,1.448044,1.783001,1.724312],[-7.357713,2.406649,8.443820,-8.146977,4.269758,5.311936,5.216488,-1.265309,6.823217,-3.024922,-6.291495],[-9.254505,-4.218287,-9.053174,7.125192,-9.686536,-0.934190,6.226002,8.225945,-8.864444,8.146765,-4.800398],[-6.684868,6.787794,-3.269956,-9.206031,-5.425004,6.395647,-0.196495,-3.067624,3.628535,1.329127,0.218143],[-0.888225,3.813253,0.569463,-1.173596,4.697255,0.751573,-4.662427,-0.894755,-0.302318,1.462670,8.979710],[0.214533,-5.262810,-0.273486,-1.014749,-9.356071,4.784125,1.805523,8.792283,-6.172368,-3.600566,5.806961],[3.687527,7.918446,-8.880510,-0.942495,9.527031,-1.174107,-5.060588,5.752192,-7.127022,2.189588,2.211894]],[[-5.747697,-5.362674,0.038395,-1.390612,7.193851,3.618047,2.409829,-2.029466,0.626375,6.729710,3.436471],[2.506001,-7.805595,-0.370378,8.746159,-5.786715,-5.268619,-6.908767,-9.491344,-5.946800,-6.993546,-8.396525],[-0.286879,4.486169,-5.633188,5.128975,9.039122,6.856543,-7.352355,6.785385,8.491077,1.441938,5.013757],[-7.401480,1.042428,0.416642,-8.310641,4.702592,-1.122796,-3.320190,-2.800930,-9.763677,-0.341742,1.134009],[-0.271661,-7.375228,3.589138,5.513757,1.071378,-9.656707,9.008197,1.891907,3.331995,-6.803398,9.785160],[9.320673,-9.743797,6.651711,5.142406,7.540808,-7.151966,2.327408,2.865107,-5.119726,-4.755478,1.555082],[-7.859377,1.618733,-8.276812,-8.529296,4.568169,1.815724,7.082356,-4.340144,1.317223,-6.664864,-7.625987],[8.261597,0.111664,-9.716807,-2.020286,3.178722,-3.081012,9.650976,-3.410873,9.415424,2.848427,3.577089]],[[0.384922,3.933428,4.317665,-7.901781,8.899055,1.746263,8.841431,6.439569,-1.213474,2.253140,5.216395],[3.540922,-0.927167,3.980032,3.637311,-1.393035,2.905454,0.946091,-4.040147,-5.191102,-8.800439,-0.424392],[9.385275,0.841756,-0.444399,6.232996,1.482575,4.400298,9.212230,2.035812,6.442176,4.522719,1.730469],[9.372637,4.476997,-2.818148,5.696654,9.989914,-2.666197,-3.881290,5.185083,-9.496968,-6.857730,-1.141636],[3.055665,-4.929842,-7.889852,3.386251,5.757211,6.214473,-6.144330,-2.607964,-1.346821,-8.340796,-5.601518],[4.190678,-7.027495,3.081015,9.664929,-0.590799,8.475735,7.999926,6.540647,-8.080976,6.211873,4.768161],[8.846282,0.238135,3.994128,-1.105940,9.559336,-6.403961,6.748934,-4.836987,8.620459,9.260600,-0.744732],[-0.334718,0.918236,-7.145874,-6.565577,-2.605218,0.765203,8.652036,-8.280208,-3.294350,0.772004,0.193395]],[[-8.393157,1.262313,2.014403,5.846139,7.905153,2.744765,-5.614697,1.752495,9.887769,-4.653432,-4.181982],[3.050912,6.514245,-5.948158,-9.723121,9.752578,5.827643,0.195572,-4.294652,-4.293418,-4.831441,-8.329253],[3.973714,-2.340927,-6.651704,3.237797,-8.371313,3.344109,0.669493,6.312944,1.638620,-4.232596,7.044260],[4.053624,-3.683428,-7.167397,5.029589,0.343520,-3.696027,8.377415,-6.063719,8.101907,-9.893106,-0.775263],[-1.053183,0.262017,4.072306,0.940718,7.966199,-4.220298,-3.174282,2.463691,4.219085,1.491697,-9.335503],[-2.498332,1.711434,3.087371,-1.193929,3.303313,9.283684,1.563868,7.301384,-8.413030,4.108468,-4.294229],[1.421777,-5.587825,3.124051,-1.832621,-8.452787,-5.162658,6.983328,3.225941,-7.581138,-8.585567,-3.337592],[-8.630920,-7.463980,-0.448383,3.711790,-0.612663,-5.890829,3.827613,-3.007651,5.336828,0.372527,-0.908963]],[[-1.314902,-7.388605,5.520666,-8.659077,-5.993713,6.218902,0.435771,1.826203,-6.991082,5.329662,-2.833711],[-8.073548,3.847506,6.940022,-3.228966,5.540471,-0.386085,8.610422,-0.115887,0.204323,-6.041087,-6.548118],[-4.969006,-5.619224,3.635543,-2.783291,-5.717681,-8.583722,-2.866234,-0.182716,1.587946,3.685580,-8.689047],[1.700056,4.664055,8.559366,7.594646,9.519349,8.973010,4.249717,-1.344553,-4.230755,-6.621560,-0.513204],[1.036013,2.582217,-1.621984,-5.255481,5.725977,7.656660,-6.203447,-7.117855,-7.228471,0.443286,4.647977],[-2.558572,-9.905995,5.718764,4.376950,-2.946064,-0.973204,-0.033875,-0.504353,9.706055,-2.758751,-3.044451],[-2.471466,1.030412,0.814615,-7.867194,8.255741,-1.678015,-3.587928,-0.174854,5.893382,-0.146349,7.781613],[-1.068985,5.719599,5.756534,-3.078442,-3.261597,4.898853,-2.882815,-1.646126,4.796031,9.075372,-3.582988]],[[2.582921,-4.385088,4.011585,0.083989,8.933506,-7.625778,7.193359,-2.204932,-5.568227,-3.527972,-4.274360],[-3.382327,-6.507824,-4.691825,9.251666,1.133009,-8.560864,8.119366,-6.176532,-7.692548,-1.718647,-3.597296],[-4.278708,5.269339,7.619641,-2.208616,-2.228951,-6.045899,1.929467,7.093180,4.817126,6.189795,-9.821597],[5.390664,2.061150,-0.034694,7.064409,-5.310687,6.475600,-2.914254,2.298866,3.411883,2.862652,-8.773373],[-2.183185,0.382405,-0.797101,8.427256,9.077690,3.022628,-3.365013,-7.276554,-3.891685,-8.246536,-8.553490],[-5.176802,6.661843,-1.252026,-5.874658,0.180283,-6.097195,-8.431906,-0.293705,8.855115,9.970107,-7.978717],[-3.514743,1.663525,4.379132,-4.581865,-2.944452,-4.241718,-2.277117,-1.062093,6.852822,-7.876396,-4.681243],[2.960705,-7.878020,-7.461063,8.785087,-1.738969,3.069908,0.232557,8.946891,-8.020343,-5.865718,2.093779]],[[4.253963,4.401030,-6.642302,-9.011225,7.394230,0.430469,-0.122213,1.201527,-0.618506,8.615886,4.214454],[5.300614,4.957824,-5.373632,-7.781850,-6.032352,7.208519,-1.947364,7.654361,-7.434827,-5.291304,8.012556],[9.871744,3.953950,-8.393870,2.913626,6.189542,-8.810961,-6.670018,-5.561949,-5.841183,1.666044,7.266686],[4.647099,-8.574066,6.745376,5.183414,-2.759349,4.197652,6.429050,-1.390561,2.784634,5.247626,-9.298460],[-5.606511,-4.215982,-5.991089,-3.234227,1.279578,-1.312263,7.637221,5.837505,-5.103106,2.460062,4.338037],[5.499335,3.744608,6.833782,-4.480370,-4.940910,-7.894570,-1.901232,-5.882374,-0.291902,-5.554050,-0.982681],[-1.677097,4.703616,0.216084,-1.296981,8.047926,-5.818038,-1.879708,7.815084,-9.454254,8.141718,-2.871864],[4.359703,-5.821571,-2.992232,-8.491907,-2.850151,-0.994911,-9.430331,-0.337217,-7.275519,-9.137366,-1.606835]],[[-4.793776,-4.430968,-2.290513,-0.349051,4.766054,5.804173,4.216558,-0.761694,-0.232322,4.683836,-4.176962],[-7.709722,-1.196425,-1.998429,-5.978548,-0.929528,-3.188341,1.728974,-7.598622,9.270210,5.041948,-9.407635],[3.276209,-4.285362,1.670505,-9.624624,2.796169,3.873386,-0.700006,0.915698,-4.849614,8.830203,-4.372932],[0.550712,-0.491470,-8.340310,-7.395202,0.569936,2.938135,5.576537,0.516541,6.657756,1.793741,-8.162528],[-3.180938,-6.002588,2.973342,-7.124463,-0.516034,4.213702,-1.915475,-9.492769,-4.753168,-7.457384,8.762461],[-1.108765,-4.805894,-0.504833,-6.970542,4.063098,-5.597018,-9.406256,3.789456,4.542283,-8.766183,3.277199],[-5.015618,5.599775,0.734557,-5.808993,-8.329497,1.686988,-1.553685,-8.780776,-0.108194,-4.152754,9.360922],[4.649513,6.637161,-2.894421,2.574823,-5.220710,8.545389,-1.364177,-9.701418,4.274806,8.571829,0.377166]]], dtype = "float32")#candidate|3323|(9, 8, 11)|const|float32
bop_3324 = relay.mod(var_3322.astype('float32'), const_3323.astype('float32')) # shape=(9, 8, 11)
bop_3340 = relay.greater_equal(bop_3324.astype('bool'), var_3322.astype('bool')) # shape=(9, 8, 11)
func_1095_call = mod.get_global_var('func_1095')
func_1099_call = mutated_mod.get_global_var('func_1099')
const_3349 = relay.const([4,7,-9,4,-1,-2,1,8,1,-1,-1,-8,-3,-10,-6,-8,-8,-6,1,6,9,5,-3,5,8,3,-7,8,3,6,-8,2,1,-4,5,6,-7,7,-3,4,-8,-3,-7,-6,-6,2,1,1,-9,6,-4,-10,-3,-10,9,8,-10,4,-1,-8,5,2,-3,7,9,-7,-6,-3,-4,-5,-9,-2,-5,6,9,2,5,1,8,-1,-3,-9,7,-8,-7,4,8,-2,-2,-7,-4,6,-3,-9,-7,8,-1,9,-1,9,-9,-3,-8,-10,-5,5,7,1,8,-3,-4,-5,9,3,10,-7,6,8,5,8,4,-1,3,-1,6,6,-6,-5,6,5,1,-6,10,-2,-1,-6,4,-8,-9,-9,-4,3,7,-4,-9,8,-9,-8,10,5,-10,8,6,10,6,10,-4,9,4,-4,-2,-2,9,-1,10,2,-7,-4,6,-2,-3,2,7,1,-5,-2,-9,8,-2,9,-5,2,9,8,-9,-10,3,2,-5,1,7,-7,-8,6,-5,4,6,-3,3,2,2,-6,4,-4,2,9,9,-8,2,-8,1,-9,9,1,3,-4,5,-1,10,8,-9,1,-6,6,5,6,-6,-2,-7,5,-6,7,10,10,3,2,-6,1,-4,-1,9,-6,10,-1,10,-9,6,-8,5,-6,6,10,1,-4,-6,-3,-2,-1,-6,1,10,-4,7,-3,-10,1,-5,9,-10,-10,-10,1,-1,-6,7,-6,-9,-3,4,9,3,1,-10,-5,-5,-7,7,9,-2,-6,2,6,-4,-8,-3,2,8,5,4,-8,-6,-4,-1,-10,7,2,9,1,-6,-10,7,-4,-5,-2,-2,8,5,8,6,-1,-5,-2,-2,6,1,7,-7,-4,-4,1,-7,2,2,10,-10,-1,-3,-7,-6,-2,-10,7,-2,10,-7,1,-10,8,5,-10,-8,-9,-3,-7,-1,8,-10,9,-5,-7,9,-8,3,3,-3,-2,-3,3,7,-5,-9,-8,-7,2,-5,6,-8,-5,10,6,10,-6,9,8,-7,2,7,6,6,-8,8,-7,8,-7,9,-4,3,1,-9,-6,2,-6,-8,3,-2,-5,4,-7,3,1,-9,-2,-6,2,3,-4,8,6,-2,-1,1,-5,9,7,7,-7,-2,-9,-3,-4,1,-3,-7,6,-7,4,-5,3,2,-8,-8,5,4,-10,7,3,-1,-8,5,-8,10,-2,-2,9,-7,-2,1,-8,-3,10,-2,5,-9,-4,6,-9,-5,-3,8,-2,10,1,-3,-4,5,4,7,5,-4,-2,-2,-9,4,3,-6,6,-8,5,5,-8,3,10,-1,10,3,-8,-5,-1,8,2,10,8,-6,-9,-4,1,-9,9,-3,7,-3,10,-9,8,4,3,-9,-2,-6,5,-10,-7,-5,-10,5,6,-2,5,-7,1,4,-5,-5,-7,-10,10,7,10,6,-2,-7,1,5,3,1,-5,-7,8,-9,-4,-5,10,6,4,10,-4,-6,-8,-5,5,4,10,10,7,3,10,-8,10,8,7,-1,7,-10,-8,-6,10,3,-3,-8,-4,-2,8,5,-5,3,-3,4,4,4,6,5,10,-6,4,-1,-6,3,4,-6,-2,-10,-5,-6,-8,-1,10,2,5,-5,5,-7,1,-9,-9,4,3,-8,-10,-9,5,-5,-7,7,7,1,9,5,8,-5,-8,-10,-2,-1,-1,1,10,2,-4,-9,2,5,8,1,3,-4,-2,-3,-3,5,5,-1,-3,-4,4,10,-5,-7,-8,-8,-2,-3,7,9,10,-3,1,2,8,2,3,-8,-10,9,1,8,-10,-10,-5,-6,-2,-10,4,8,1,-2,4,3,4,2,1,-1,-3,7,-9,-2,1,-5,-7,-5,-4,5,8,6,1,-9,9,3,-2,-9,3,-3,7,-9,2,-5,4,8,9,6,-1,-10,5,-2,6,-8,-5,5,-9,-8,-10,-9,4,-6,9,-3,-7,3,-8,8,8,-3,9,7,-2,-8,8,7,-5,7,7,6,-2,-7,-4,4,-3,7,5,-9,-8,1,6,-2,-3,5,-6,5,8,10,-6,-7,3,2,-7,5,2,5,-4,-7,5,-10,-2,1,-6,5,-5,-5,-6,6,-10,3,7,-9,5,9,-9,1,3,-3,-2,2,-1,-8,4,10,-5,7,1,2,-4,-7,9,4,1,10,8,-3,-9,-3,4,-8,-8,-10,10,6,4,-9,-1,-6,2,8,-10,-6,3,-3,-7,-8,7,-6,2,3,5,-1,-4,-9,-5,-6,-1,3,4,-2,8,-5,-8,1,3,3,5,4,-3,8,1,2,-6,5,2,10,5,-6,-6,-2,3,7,-1,9,-4,-9,-9,-7,5,-5,-9,-8,2,-7,1,7,7,1,-5,-10,-5,3,2,-1,2,-6,2,-5,-6,-3,4,-10,-6,-8,1,-9,9,-2,-10,7,-6,-10,7,-3,10,3,-7,-4,3,-5,10,-3,-4,9,6,5,-1,2,-2,4,-2,5,-9,4,1,-8,-1,-9,6,8,-5,7,10,5,-6,-4,-5,8,10,-6,9,-1,5,-5,9,4,-6,2,-10,-8,8,-5,-2,7,-4,2,-6,-6,-4,-3,-4,-7,-10,8,7,-8,-9,10,-9,3,1,-9,-10,-10,-5,5,4,4,2,5,10,-6,8,10,4,-1,1,-4,4,-3,-8,2,2,-5,-8,4,4,6,-8,9,2,-7,-9,-3,-4,4,9,-6,-2,5,-3,-9,-3,-9,3,-2,-8,-9,-9,-10,3,9,-9,-2,7,-2,-10,-9,6,-1,8,6,-2,2,9,6,-5,-3,1,-5,3,-1,8,4,-2,3,-10,-7,-3,-6,9,4,9,8,1,8,-3,-8,3,-5,9,-4,-6,-3,-9,1,1,2,3,7,5,9,-8,-9,1,5,-9,-10,1,-3,-10,-8,10,-10,2,-6,-5,-5,3,4,-5,5,10,-10,-9,-9,7,-10,7,-7,-9,6,-9,-9,-2,-8,3,-2,9,2,-4,6,8,8,10,-6,10,5,2,6,8,-4,7,4,9,5,6,-5,-1,-4,8,-10,-4,10,8,4,9,-6,6,-4,3,8,-3,8,6,3,-3,-4,5,-5,-7,-8,8,3,-2,-7,-6,-8,10,1,7,-1,6,-7,9,-5,-2,-3,6,4,-4,-5,-8,9,9,5,5,-6,1,-3,9,7,2,-2,9,-6,-9,-3,-4,-6,-4,8,-8,2,10,-10,-7,10,8,-8,10,-9,-5,-7,-9,-1,-3,-4,-3,-10,4,-2,6,10,8,2,2,-8,-6,-5,5,7,4,10,-10,2,10,-4,-8,2,-2,5,-8,10,-5,8,-2,-1,-10,6,9,3,4,8,4,9,4,2,6,-5,-9,-4,-2,1,-5,-10,-7,-6,2,2,-3,2,6,1,-7,4,3,-9,2,-5,-9,1,-9,6,10,7,-2,5,4,9,-4,9,2,10,-10,-2,3,-4,2,-6,-9,-8,-4,8,-8,-1,-3,-10,8,10,7,6,7,4,1,4,5,-2,4,8,8,-6,10,5,-8,-6,9,6,-4,-5,-2,-9,-10,5,1,-10,5,-2,-4,2,2,-8,2,8,6,-4,-2,-5,-4,-8,8,-7,-4,7,-4,9,-9,-10,2,-8,1,9,5,-6,8,7,2,8,-1,-3,4,-4,10,3,-9,-2,-2,-2,5,-9,3,-9,-8,-2,-10,3,-8,6,-10,-2,9,-7,-5,10,-10,4,-3,-10,-10,9,9,5,-10,7,-7,6,5,6,4,-1,-5,10,10,8,-2,9,10,1,4,-9,-1,8,10,-7,2,-1,-4,4,10,-1,10,6,-5,-1,8,-9,-4,-4,-1,-1,10,-9,-2,8,6,4,1,-7,10,-3,-7,-7,9,7,4,-2,-7,-9,-3,-1,-6,4,-7,-6,-10,-5,-3,-10,-4,4,-5,2,-7,-1,6,9,8,-3,-8,-4,-8,-5,-1,-5,4,-3,-4,-10,-4,3,-4,-5,-8,9,-7,-4,2,-6,-8,8,-10,8,-5,-7,9,10,4,8,-4,-8,10,6,5,6,4,-3,6,8,-2,-10,-5,-6,6,1,-3,-10,4,6,9,1,8,6,9,-5,1,2,6,6,-4,-1,-7,9,-7,1,10,9,-7,-4,-1,7,-6,7,-9,-3,10,-9,7,10,-4,9,-4,2,3,10,-4,-3,6,-2,3,-7,1,9,5,-1,-10,-2,9,8,1,6,-4,8,1,4,-7,-6,-8,-6,6,-9,8,-3,-7,-10,8,6,7,10,3,-3,-7,-9,-5,6,-4,8,-8,8,-1,-6,6,-8,7,4,-4,-2,-5,-3,-8,2,6,4,2,-1,-2,-1,-10,-5,1,-7,-4,5,10,10,9,-9,-1,-8,7,-5,8,-9,-6,-5,2,1,1,-7,-6,-10,-8,-9,-4,-1,8,-1,-1,5,5,-6,2,-6,5,-7,-10,-5,7,-9,-3,-5,-4,5,7,5,-10,2,10,6,-1,6,1,2,-5,3,9,7,4,-1,4,4,10,-7,-4,-4,7,6,1,-5,7,4,-6,1,7,-1,-1,4,-1,-10,3,9,3,-7,1,3,-10,6,-2,-5,3,7,-3,5,-1,8,-10,3,2,10,-1,-3,-1,-6,10,-9,9,6,6,-7,-8,-10,-4,4,2,9,-8,-4,-3,-2,-4,-5,9,-7,5,-4,9,-1,-7,-8,10,2,-10,-9,-9,-8,-1,9,6,-7,-10,-4,-4,-1,-2,4,6,2,-4,-3,-1,9,-3,4,-2,10,1,-10,-1,-10,2,8,9,6,-2,-8,9,7,-6,3,3,10,9,2,5,-6,-5,-6,6,-2,2,-5,9,-5,4,-3,-3,-10,-4,-6,-4,5,9,-6,3,7,-7,-4,-4,-1,9,5,4,-6,-10,7,-5,5,-2,-8,8,8,-8,4,-5,10,9,-4,1,-3,-2,-4,3,-10,-10,-9,6,6,2,-5,6,-9,-9,8,-4,-2,1,5,5,6,4,4,5,-3,3,-3,3,4,8,-3,-4,1,1,7,9,-1,-3,4,-6,-2,-7,10,9,-4,-5,-9,10,-4,6,-6,9,2,2,-7,-5,9,-5,3,-2,-1,4,8,4,4,5,6,5,3,6,-8,-10,4,-8,1,6,9,-4,1,-8,9,-4,5,-3,-1,-10,-1,-7,-8,-3,-5,1,-6,-8,4,-1,9,-7,9,7,-8,-8,-9,-3,-10,-6,-3,6,3,-6,1,-7,7,7,4,5,-2,3,9,-10,2,1,-4,-7,-2,1,2,-6,-2,6,-8,7,5,-3,8,1,-9,7,1,10,9,-9,-9,-2,9,-6,7,8,5,-6,5,3,10,-9,8,-6,-1,7,-9,1,-7,4,-2,7,4,-8,-1,-4,5,-3,3,7,2,3,5,7,3,-5,4,10,-5,6,1,6,1,8,-7,-7,-1,2,6,-7,3,-2,3,-4,10,4,-7,-9,10,-2,2,-7,10,10,-1,3,-8,8,6,-2,9,10,-8,4,-6,-6,6,3,5,1,8,-7,-10,-10,6,-3,-9,2,-3,7,3,-8,-9,4,-4,-9,3,-1,-10,9,4,-4,6,2,10,-9,-3,1,-9,3,2,-6,-7,-7,-7,-6,10,-7,5,8,-9,10,5,3,6,7,-9,2,9,6,6,10,1,6,7,3,10,-9,3,-1,7,9,-1,3,-10,8,10,-4,5,8,4,7,5,3,5,8,-1,1,8,4,2,6,9,-6,-1,-6,6,-3,7,-10,9,8,5,-2,3,2,7,9,9,-10,-2,7,10,-10,5,1,7,2,7,4,-1,5,-4,3,2,6,-2,1,-5,8,10,-4,7,7,-1,3,-9,9,5,-9,-5,-2,-1,8,-5,-8,6,-9,7,8,-1,1,1,3,9,-6,8,5,2,-5,-10,1,-2,-10,8,-8,-10,9,8,9,2,4,-3,9,-2,10,7,9,-4,10,-8,-3,9,10,-1,-5,-4,5,7,1,-10,1,-4,7,-3,2,-7,-10,6,-4,-10,-4,-7,10,-4,-3,-3,2,-9,7,-7,-3,-3,-5,-6,-8,7,1,-2,9,-3,2,1,5,-4,1,-1,-10,-9,5,-3,2,-6,5,5,6,10,-5,-4,10,3,3,-6,-10,5,2,10,-9,8,-6,10,2,2,1,-6,-7,-2,4,-1,-7,-10,6,5,-8,-1,-8,8,3,5,-9,-4,-3,5,6,-10,4,-2,-1,8,-1,-6,2,-9,6,-10,7,9,2,-7,-10,3,-8,6,3,-1,-3,-3,10,1,-6,-9,6,-4,2,7,10,-7,5,10,-9,2,9,-8,-5,-3,9,7,1,-4,-3,-8,2,-3,-1,7,-7,2,2,3,9,2,1,5,-1,9,-1,8,4,-2,-8,5,-8,9,6,-9,1,7,1,6,-5,7,-1,1,8,-10,-2,2,-3,2,-7,6,-4,-10,9,6,-10,-9,-8,6,-6,4,3,-10,9,6,2,-3,-7,1,10,9,2,3,-8,8,7,-4,8,-7,-5,-4,-6,-5,-4,10,-6,4,-7,-8,5,-1,-5,-5,8,-3,-8,1,-6,9,-3,-1,-10,-4,3,-3,7,-3,8,7,-3,-8,7,-2,-6,-10,2,7,-10,8,-3,4,-5,-2,8,-9,-2,-9,-8,2,4,2,-5,9,-10,-1,-7,4,-3,-5,8,1,4,-8,10,8,-2,-1,9,-2,-8,3,7,7,4,2,-7,3,-10,-4,9,-6,2,9,1,2,6,3,3,-5,4,-2,-10,-2,3,5,-6,6,10,9,7,-1,7,8,5,-10,3,-10,6,-5,6,5,-1,-9,-6,-6,-10,-8,10,10,1,4,3,-7,6,9,4,-3,5,-7,2,4,10,-2,7,-8,3,2,-8,4,3,-5,5,1,1,1,-3,9,8,-4,5,-5,3,-2,-8,-2,-10,-5,6,7,6,-3,2,2,5,-6,5,-9,-1,-9,9,-8,-10,-4,-3,-4,-8,7,10,1,-5,-6,-10,-1,7,-10,3,5,-2,-10,1,-3,-2,10,-10,-7,-10,5,9,-3,-8,-3,10,6,9,7,1,-9,-10,5,10,5,7,1,8,4,-6,8,-7,10,-4,5,8,-10,-1,-10,-9,10,-7,-3,7,-4,4,-1,-8,-4,9,-8,3], dtype = "int32")#candidate|3349|(2688,)|const|int32
call_3348 = relay.TupleGetItem(func_1095_call(relay.reshape(const_3349.astype('int32'), [14, 16, 12]), relay.reshape(const_3349.astype('int32'), [14, 16, 12]), ), 0)
call_3350 = relay.TupleGetItem(func_1099_call(relay.reshape(const_3349.astype('int32'), [14, 16, 12]), relay.reshape(const_3349.astype('int32'), [14, 16, 12]), ), 0)
output = relay.Tuple([bop_3340,call_3348,const_3349,])
output2 = relay.Tuple([bop_3340,call_3350,const_3349,])
func_3359 = relay.Function([var_3322,], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
mutated_mod['func_3359'] = func_3359
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3360 = relay.var("var_3360", dtype = "float32", shape = ())#candidate|3360|()|var|float32
func_3359_call = mutated_mod.get_global_var('func_3359')
call_3361 = func_3359_call(var_3360)
output = call_3361
func_3362 = relay.Function([var_3360], output)
mutated_mod['func_3362'] = func_3362
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3427 = relay.const([[[9.610804,-3.171019,9.477125,3.732946,6.049286,-2.639172,9.188411,9.207260,-4.866077,4.280147,0.769416],[0.831430,-8.022934,-4.546113,4.567159,-9.903919,3.629871,9.996231,1.073355,-5.556237,-4.155634,1.954107],[4.981972,5.816102,-5.028045,-5.992684,7.609587,5.407879,9.165746,3.179817,4.082588,4.506670,-1.278339],[0.255393,7.477986,5.335585,-2.451408,-1.943278,9.575579,4.860985,-1.295737,2.962330,-9.511142,9.649400],[4.476602,-9.172836,2.305887,5.263193,-9.313595,3.776696,-0.638877,7.973900,7.997594,-1.244436,-9.552104],[3.348866,-3.486228,-4.731432,0.718086,-0.768968,-1.326378,7.344234,-3.733030,3.564666,4.052434,-3.616965],[5.959128,1.399622,8.005832,-1.482466,3.011765,5.455240,-5.688561,-8.998075,5.012045,-5.226950,1.400571]],[[6.156380,-4.406720,-3.714627,-9.511904,-5.843007,1.825271,-5.167118,5.513849,-6.515980,-9.151931,-3.276480],[5.528752,-5.945934,1.599702,-2.553910,-8.376116,-2.098190,-9.795494,5.652877,-5.860285,2.124759,5.977821],[-5.377061,-0.919173,6.818385,-5.014516,9.404982,9.660675,0.691785,6.513556,7.214548,5.183675,-7.550233],[5.753035,-0.682720,2.623363,1.636768,-1.364014,-1.059369,-0.290268,9.482421,2.751506,-2.266467,0.390147],[-8.041691,1.097599,-0.415530,8.646356,-8.329538,-8.379127,-4.614094,-3.290019,-5.095102,-4.465917,4.303882],[1.667201,1.200394,-4.356636,7.315309,7.377227,-3.743238,9.248551,-5.207359,2.707665,3.883692,5.000989],[-6.956126,7.652739,-5.085333,7.698153,-7.270552,2.086177,3.673783,1.047232,3.258512,-5.901507,4.016868]],[[-0.945035,0.743124,0.137825,-8.837462,-9.200815,-8.246105,4.805831,2.294896,3.358278,1.415549,-9.398932],[-5.406248,1.146384,-3.464790,1.752543,-5.083935,5.807453,5.852790,-2.992923,-4.639845,-0.448341,2.429081],[4.414553,-1.244907,-6.478677,8.360248,4.405438,5.019464,3.715113,-8.736161,2.272938,7.348047,-8.357942],[3.617304,-1.512321,-0.358066,9.337587,-0.139919,-8.602980,3.840764,3.551713,9.311179,-6.457544,7.939114],[5.885660,-9.289849,-4.289466,6.253974,-5.951076,-5.943964,-0.483733,-4.448766,-3.578451,3.231815,2.086239],[7.322398,6.733144,3.432675,3.770352,-0.341517,1.966834,-0.975666,-8.838039,-0.477410,-4.261691,9.321028],[7.497090,-3.612533,-3.076983,1.173882,-3.590282,-1.923222,4.664945,7.691641,7.429447,8.908411,-4.459992]],[[-8.809464,-0.506639,-3.864570,0.129674,5.917443,6.916256,-9.467181,9.298754,5.719417,8.127533,-2.937251],[-6.273416,1.468997,5.568708,-7.748436,-4.375871,-8.343972,9.652344,-0.411909,-3.042743,-4.315613,0.955097],[9.159997,-6.777787,8.814109,4.864852,-1.361172,9.476983,0.021505,7.435739,1.471006,-0.237005,-9.109806],[-3.307485,6.751285,-1.619089,-2.981060,-3.386538,5.175409,-8.756757,-2.509795,-4.640140,7.040189,1.391504],[-6.472483,-3.969111,-3.753929,7.982742,1.557794,8.326081,-5.928045,-2.308092,-6.876890,-6.555072,8.828032],[-1.396301,-9.277899,-1.232175,-7.187521,-6.213514,-7.236264,-7.645779,-8.306722,1.029179,9.265422,-0.539793],[1.692904,-7.716919,6.551017,9.795845,-3.797226,3.536600,-3.919043,-1.485004,6.344178,1.709684,-1.353837]],[[-3.113046,6.066086,-8.308956,9.293625,-8.681530,6.328892,-2.126596,1.347472,7.713121,9.937178,5.429015],[-1.841792,-0.444232,-6.790020,-1.467363,-7.648218,2.413509,-0.718924,-2.969530,-8.270630,-6.544447,-8.680290],[4.788912,-7.694851,0.025970,2.429679,1.491540,-3.786482,4.114668,1.889270,4.710674,-2.670331,7.011422],[-3.928565,-0.929742,-8.133482,-6.208580,8.452763,0.906482,-8.676679,1.048836,1.974303,-5.927914,9.784300],[-1.600673,7.504142,-2.719817,3.281940,-6.244839,4.543348,-6.452498,-3.166393,-4.478730,-6.878244,6.715303],[-1.481729,-8.843385,-8.506885,-6.003211,-3.601832,-9.642784,-7.213197,-2.075068,1.549012,-1.447106,8.931257],[-9.652441,9.934566,-8.438460,-9.888166,4.948023,-3.513452,-0.449779,-1.143502,-0.268576,-8.881049,-3.403897]]], dtype = "float32")#candidate|3427|(5, 7, 11)|const|float32
uop_3428 = relay.sin(const_3427.astype('float32')) # shape=(5, 7, 11)
bop_3432 = relay.less(uop_3428.astype('bool'), relay.reshape(const_3427.astype('bool'), relay.shape_of(uop_3428))) # shape=(5, 7, 11)
func_1982_call = mod.get_global_var('func_1982')
func_1986_call = mutated_mod.get_global_var('func_1986')
const_3441 = relay.const([-2.641981,-4.480213,-7.429094,8.159429,-8.195434,2.457521,7.821012,4.567262,-6.988374,9.856664,7.428548,-3.675453,0.225845,-1.630338,-7.792454,-8.412377,6.995671,5.539736,-1.778622,8.049864,2.786903,8.229759,-1.691744,-3.522888,9.580184,-9.583929,-4.326908,-8.803649,0.062341,-7.216334,-5.951298,-9.376207,5.752149,-6.740758,-7.242590,-4.954874,-5.697184,-1.958405,-4.769120,5.405955,6.284003,-6.671804,4.601166,2.116699,-8.657346,-8.795566,-6.544489,-1.913080,3.337648,1.684462,3.942934,8.284103,-5.896725,-5.234359,-9.801345,-2.433417,4.729053,0.392867,6.975909,-3.621481,-7.949703,4.377051,5.881091,-4.809488,-0.291971,9.570312,-8.503403,6.713049,-2.893716,7.432637,0.849038,-8.241347,4.815026,7.140770,-0.040653,-2.617856,8.210857,3.381757,4.336692,3.409304,-3.551853,3.831018,1.147984,7.611516,8.455292,0.229116,-3.733662,4.766730,9.217718,0.785983,-7.366236,4.519160,7.217828,9.670460,-1.603926,-6.858206,3.420789,7.904089,-3.112729,-8.954831,-9.378918,-6.643108,-6.879794,-6.696296,9.578632,7.938755,5.716667,1.536842], dtype = "float32")#candidate|3441|(108,)|const|float32
var_3442 = relay.var("var_3442", dtype = "float32", shape = (48,))#candidate|3442|(48,)|var|float32
call_3440 = relay.TupleGetItem(func_1982_call(relay.reshape(const_3441.astype('float32'), [6, 3, 6]), relay.reshape(var_3442.astype('float32'), [12, 4]), ), 4)
call_3443 = relay.TupleGetItem(func_1986_call(relay.reshape(const_3441.astype('float32'), [6, 3, 6]), relay.reshape(var_3442.astype('float32'), [12, 4]), ), 4)
output = relay.Tuple([bop_3432,call_3440,const_3441,var_3442,])
output2 = relay.Tuple([bop_3432,call_3443,const_3441,var_3442,])
func_3451 = relay.Function([var_3442,], output)
mod['func_3451'] = func_3451
mod = relay.transform.InferType()(mod)
var_3452 = relay.var("var_3452", dtype = "float32", shape = (48,))#candidate|3452|(48,)|var|float32
output = func_3451(var_3452)
func_3453 = relay.Function([var_3452], output)
mutated_mod['func_3453'] = func_3453
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3626 = relay.var("var_3626", dtype = "int8", shape = ())#candidate|3626|()|var|int8
const_3627 = relay.const([[[6],[6],[-8],[10],[-7],[-3]],[[2],[-8],[-7],[-1],[-2],[-4]],[[-4],[2],[-9],[-1],[-7],[-10]],[[9],[8],[-1],[-10],[4],[5]],[[2],[-8],[4],[-7],[-3],[10]],[[-6],[-9],[-9],[9],[-1],[3]],[[-7],[-6],[-1],[-2],[6],[-1]],[[-10],[-1],[-7],[-6],[-1],[5]],[[4],[-9],[10],[-6],[4],[-8]],[[10],[2],[-10],[6],[-1],[-4]],[[9],[9],[-5],[-1],[2],[-1]],[[-9],[1],[-10],[2],[1],[-7]],[[5],[2],[2],[4],[5],[1]]], dtype = "int8")#candidate|3627|(13, 6, 1)|const|int8
bop_3628 = relay.bitwise_and(var_3626.astype('int8'), const_3627.astype('int8')) # shape=(13, 6, 1)
bop_3633 = relay.equal(const_3627.astype('bool'), var_3626.astype('bool')) # shape=(13, 6, 1)
output = relay.Tuple([bop_3628,bop_3633,])
output2 = relay.Tuple([bop_3628,bop_3633,])
func_3651 = relay.Function([var_3626,], output)
mod['func_3651'] = func_3651
mod = relay.transform.InferType()(mod)
var_3652 = relay.var("var_3652", dtype = "int8", shape = ())#candidate|3652|()|var|int8
output = func_3651(var_3652)
func_3653 = relay.Function([var_3652], output)
mutated_mod['func_3653'] = func_3653
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3743 = relay.var("var_3743", dtype = "int64", shape = (8, 2, 6))#candidate|3743|(8, 2, 6)|var|int64
var_3744 = relay.var("var_3744", dtype = "int64", shape = (8, 2, 6))#candidate|3744|(8, 2, 6)|var|int64
bop_3745 = relay.maximum(var_3743.astype('int64'), relay.reshape(var_3744.astype('int64'), relay.shape_of(var_3743))) # shape=(8, 2, 6)
uop_3751 = relay.rsqrt(var_3743.astype('float32')) # shape=(8, 2, 6)
func_846_call = mod.get_global_var('func_846')
func_848_call = mutated_mod.get_global_var('func_848')
var_3754 = relay.var("var_3754", dtype = "float32", shape = (640,))#candidate|3754|(640,)|var|float32
call_3753 = relay.TupleGetItem(func_846_call(relay.reshape(var_3754.astype('float32'), [10, 16, 4])), 0)
call_3755 = relay.TupleGetItem(func_848_call(relay.reshape(var_3754.astype('float32'), [10, 16, 4])), 0)
output = relay.Tuple([bop_3745,uop_3751,call_3753,var_3754,])
output2 = relay.Tuple([bop_3745,uop_3751,call_3755,var_3754,])
func_3756 = relay.Function([var_3743,var_3744,var_3754,], output)
mod['func_3756'] = func_3756
mod = relay.transform.InferType()(mod)
mutated_mod['func_3756'] = func_3756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3756_call = mutated_mod.get_global_var('func_3756')
var_3758 = relay.var("var_3758", dtype = "int64", shape = (8, 2, 6))#candidate|3758|(8, 2, 6)|var|int64
var_3759 = relay.var("var_3759", dtype = "int64", shape = (8, 2, 6))#candidate|3759|(8, 2, 6)|var|int64
var_3760 = relay.var("var_3760", dtype = "float32", shape = (640,))#candidate|3760|(640,)|var|float32
call_3757 = func_3756_call(var_3758,var_3759,var_3760,)
output = call_3757
func_3761 = relay.Function([var_3758,var_3759,var_3760,], output)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4262 = relay.var("var_4262", dtype = "float32", shape = (16, 5, 16))#candidate|4262|(16, 5, 16)|var|float32
const_4263 = relay.const([[[-4.938317,9.359975,-7.600912,1.571372,1.302826,-6.379286,5.482643,5.211267,-9.220732,-4.604373,5.958793,9.717649,1.173920,-8.506868,-1.386634,1.608555],[-0.122374,-7.310102,8.041484,-7.006981,3.938947,2.801366,-9.643166,4.424311,-4.385709,4.844922,-2.762480,-6.353057,-5.649032,6.136522,2.129551,-6.704315],[-7.117557,-3.585231,-2.426550,-1.240384,2.220993,8.587626,0.936098,1.625718,-6.264619,8.232798,2.434137,-1.351839,-9.665762,-4.091311,-8.858073,-1.899901],[7.802433,9.890277,2.584411,1.991540,9.847376,-9.758735,6.477227,-5.839647,-6.601304,-2.073345,-3.561719,-5.792478,1.567976,-8.674764,0.847447,-5.107663],[0.697122,-5.236177,3.725146,2.316383,-4.072297,4.230373,3.950769,5.086088,4.725572,-5.936406,-3.006697,8.784264,3.769734,-0.119142,-0.727827,-9.758661]],[[-8.279504,-3.519851,-2.766594,-0.658207,5.221439,5.363912,7.305893,-1.817959,-1.736378,-7.213839,6.782708,-2.990189,9.983128,4.929290,6.548890,4.383780],[3.293089,-2.097779,-4.668523,-9.533242,-6.617970,-9.852065,6.591417,9.839964,3.600095,-9.277992,8.106209,-0.271639,7.278467,-2.840304,7.088392,-5.535118],[1.515422,-4.155623,8.025873,8.559028,-5.222117,-2.150063,-8.286585,-4.330252,3.011368,3.033170,6.481426,-1.573618,2.723262,-3.131326,-8.806853,9.258227],[4.878286,2.655787,3.562098,-7.192534,6.003930,8.405176,-4.499511,1.003399,-0.847580,-1.689720,-4.187126,0.563886,5.668603,-7.324369,-2.287169,8.109031],[-7.668958,2.727482,7.690135,0.035630,-4.532382,9.188544,-1.126716,-7.426466,3.736209,6.253549,5.164820,6.693446,-3.276231,2.399018,-7.163331,-3.721006]],[[8.839474,-4.694529,4.767576,9.136569,-1.248141,4.086978,-0.390738,6.368076,-1.046090,3.536603,7.857711,3.893079,8.015018,4.140236,4.472183,-3.182024],[6.009266,-2.266520,-5.104236,-7.390009,-1.658207,-6.845469,0.766615,-7.462207,-5.952963,-2.360855,-5.662598,3.974195,-0.198529,0.984190,-2.774687,-9.495569],[-3.387074,-5.996895,8.076559,1.097520,-7.722023,-8.509135,-9.414675,-1.566901,-5.459358,-6.982253,-0.382917,-2.523013,-4.258491,-8.063354,3.052115,-7.077579],[0.761365,2.057743,4.160068,-6.118748,-5.880257,-7.816525,0.489966,8.781368,4.210123,8.571952,8.205217,-9.040508,2.001435,-5.848521,1.015593,2.901089],[0.464566,1.686100,4.438557,7.084850,-4.736033,-5.251709,-8.126379,-5.868043,-1.475383,9.677794,6.195647,1.521351,-2.531328,-6.143485,1.443090,2.537612]],[[-1.321911,2.253935,-6.855614,5.222495,-5.905076,9.910713,8.699355,-6.104264,4.503694,7.753890,6.580390,1.784406,-4.474061,-6.283859,5.742054,-3.068838],[-8.909645,-5.193391,-2.436829,-6.220479,8.468448,0.515974,1.449471,-0.064649,7.027032,5.340504,7.081510,2.169433,-9.702695,3.736561,6.568652,8.098346],[6.320733,-4.139101,5.520026,4.074334,-9.298981,4.873009,-9.648301,-9.011440,8.423057,5.784415,3.723226,-4.060628,-5.402278,9.103366,-9.266579,3.416374],[-4.263069,9.302800,-5.275025,8.460339,-5.096767,-5.534295,-4.137849,-9.330208,6.941906,-1.682885,-1.390129,-4.707683,-9.582168,-8.086256,4.705715,6.066485],[-9.162342,4.291841,3.407557,4.699083,-7.129587,-5.114656,3.999581,-6.681717,-6.002533,5.320663,-9.650812,3.684694,8.506359,9.120377,-5.607549,0.287744]],[[2.483219,7.172289,8.554641,-8.600083,5.154266,-4.906563,-9.370631,3.802537,-5.246003,4.602762,-0.528628,8.554331,9.388144,-3.589331,6.844488,-8.180397],[8.233311,0.548870,-7.388832,-0.269755,5.976034,-4.684081,3.623886,-7.262907,-7.458590,-9.545153,9.371091,2.504433,-8.281841,-3.465073,2.002441,8.368030],[-8.956084,0.147032,-4.587848,-5.094703,-2.480293,0.090063,-4.983039,3.615268,-1.679470,-7.916122,-7.816225,-4.237551,7.582205,-5.315472,2.036646,4.022347],[9.182853,-2.874729,-6.396497,4.228355,-6.644983,3.567450,-6.661281,5.165522,-1.146820,-6.314475,7.990802,-3.132192,4.572329,0.223030,-8.446449,1.629491],[6.892160,9.816570,-9.768633,0.858999,-3.037366,-1.929074,6.846527,5.104243,5.941961,-1.282477,-4.009534,4.750516,-4.859896,-5.947883,-3.333932,-9.472618]],[[9.288433,7.734369,-8.731596,-2.030309,2.053491,7.348638,8.866897,9.731427,1.160962,1.331900,-2.172620,3.175797,-2.055433,7.845965,8.038097,-4.653190],[4.807215,2.810037,-2.945378,-1.842561,-8.951653,8.127175,-9.131374,-9.060741,-2.416160,8.274078,-4.939486,6.976676,-2.817142,5.437603,-3.383035,5.744438],[-0.593385,4.617636,-9.864832,-5.862718,-3.370944,-1.308701,-2.762508,-0.266015,9.869265,5.930937,-2.868987,-1.176223,5.774764,0.341094,9.728052,-3.639941],[4.511579,4.184265,2.306290,-1.510118,7.448901,2.713713,9.091964,-0.738148,0.051366,-3.414727,2.928253,9.013489,1.674898,-1.951062,4.307088,-2.409006],[7.482738,-2.434973,7.906353,-5.139201,-6.060391,9.798519,3.221607,-7.310561,0.005498,-6.119345,9.441305,-0.417682,-9.973264,4.253824,4.248048,-4.985452]],[[6.457645,6.917729,4.947493,7.656451,8.501609,4.580285,7.302949,-8.606116,4.040794,2.804379,-5.940456,5.707961,-9.699241,-8.814721,-3.845402,-5.007831],[1.611389,-1.777339,8.720971,-5.008123,-0.548950,6.576495,6.378564,1.939327,8.272131,0.454291,-8.831350,-9.689124,-9.973908,-9.828988,-9.348262,-9.898560],[-6.203315,-5.580597,0.563750,4.369630,1.144291,9.187249,-5.105603,0.305856,8.955927,1.086898,0.007140,-2.626606,-1.262621,-5.410409,-3.429408,-2.827765],[0.361634,-8.776906,-3.742371,4.935767,9.290413,-7.501920,0.962850,8.362567,9.364275,-8.409317,-8.869986,-8.087945,1.030272,8.749694,2.740951,-7.796826],[6.145152,0.924047,-6.037647,2.965552,5.201699,6.070380,2.524321,4.003403,5.818063,3.725515,7.319340,-5.541203,-1.384161,-0.119259,-5.518607,-4.824664]],[[7.248555,3.256356,-4.238437,2.040082,-9.065156,-8.895594,0.118338,-5.710833,6.189262,8.258984,2.379213,1.602476,0.053187,-5.917388,3.196979,8.190270],[-9.529133,-9.397874,8.058737,9.106499,9.689310,3.590486,2.288008,9.313801,3.986603,5.976121,8.138292,-1.779269,-5.145790,-1.795079,-2.932301,8.998319],[-0.832526,6.815122,4.843973,2.224194,7.812823,-9.025910,5.797352,3.029586,-2.435479,4.283330,-8.382346,-3.434266,-9.002958,-0.612411,9.589075,-0.559871],[4.152280,5.016889,-0.321014,1.995430,-9.586458,-0.283486,-0.812128,-6.720923,2.835525,-4.569370,-2.676637,-1.200067,1.197408,7.436029,-8.854730,-5.045531],[2.885055,0.607477,-8.617787,3.755314,-1.719163,-5.660319,-1.468362,3.139443,8.538731,7.699889,-8.416356,-4.584322,-9.921000,-2.558035,2.788236,-6.956052]],[[7.694978,-7.537478,3.122463,-1.027680,-2.357559,-9.055952,7.624380,-0.657160,3.109485,-2.936928,1.760758,4.466201,-2.004460,4.447676,-8.092303,6.854398],[0.476511,2.953825,4.344709,-5.451944,8.019375,-5.785536,-7.883774,5.430592,-0.952049,9.521112,-0.983793,9.213665,9.385786,4.981240,4.572934,0.192773],[-1.964334,2.577081,-0.907522,2.320906,-6.041605,-9.040315,-6.594469,-7.865064,-5.292308,5.636534,-9.420389,0.695116,6.563842,1.132216,0.886988,5.135495],[5.858038,-2.679371,-9.825953,9.498119,8.518353,5.586586,7.812803,2.704938,5.920221,7.126170,4.146815,0.493261,1.588857,7.563923,6.431147,-8.968731],[0.900480,-8.127081,2.163370,-2.000450,-4.734674,-9.534916,6.450035,6.300275,-5.963419,-8.387205,2.201803,-2.477880,-1.695302,-7.686712,-9.687430,9.001378]],[[6.692479,8.342072,2.377694,7.099313,6.515052,-8.802623,9.838354,-6.036964,-1.884412,-0.174020,-6.248385,-1.405177,-0.887130,3.920244,9.302835,3.948679],[-5.731028,1.812803,-4.159249,8.505154,5.408029,4.864453,2.150862,-3.665734,-4.046623,-5.398230,-1.246768,-1.111987,6.976419,1.872947,-8.523650,3.515684],[-0.644567,-5.394712,4.186214,-7.742802,2.887126,-7.825344,8.271555,-9.165728,4.160404,8.231966,8.324524,-8.531766,3.454732,-8.450264,-2.356223,-8.764927],[-2.382993,-4.183482,6.706926,-6.618437,-9.509850,5.579274,-3.062263,0.583786,-4.310656,7.000467,-5.162075,-9.809821,1.453213,2.657048,-7.301909,-2.329377],[8.082611,3.342388,-5.352757,7.877993,-0.349927,-2.583946,2.973541,-5.830466,-6.771310,1.027066,4.011767,-6.898354,-7.757803,1.979931,-9.067005,-3.292277]],[[-6.075098,-8.053828,1.844359,1.634203,-1.307548,-9.461714,7.441278,-5.280537,-9.926866,1.432529,0.085845,3.644568,9.021927,2.333076,-6.278442,0.573420],[2.763248,5.439329,-8.604911,-7.230015,0.186630,-4.024872,0.271021,-6.189246,-1.519451,0.598183,-6.724032,-1.691917,2.438123,7.418855,4.304106,-8.091453],[-7.792191,4.485865,-3.402529,7.447282,7.955597,2.155292,-7.902975,-2.741128,0.287898,6.053231,-5.079185,9.228056,7.950015,-2.309968,-9.887833,7.194357],[-5.714672,2.754301,-3.018166,-0.425777,-8.968270,-2.670390,-4.608348,6.841203,-6.642215,4.738948,-8.225666,1.711927,2.376170,-5.817393,-7.773198,-7.101822],[8.176318,-4.261660,-4.475399,2.248318,-8.987961,-6.493103,-2.777945,-4.616906,-2.284205,-4.634501,-5.873743,-6.167419,0.563710,8.726786,-2.476020,-6.782930]],[[8.316046,2.342603,-3.763249,-0.294105,-3.556838,1.169576,9.842482,2.894732,7.019120,-3.458719,8.905075,2.293243,-0.123075,2.305753,-2.142015,-2.385350],[-3.517361,1.588881,-9.753912,3.352383,-0.933431,2.828257,-9.337751,5.636993,-5.734941,3.619721,-2.414875,-6.062693,-3.998463,9.919615,-7.383857,-9.404075],[8.599378,8.919578,-9.175630,-9.699169,0.726352,-4.956271,0.944531,0.934731,5.814983,8.397750,9.386790,-2.255795,0.076773,-6.456314,8.724921,-9.127758],[-1.695000,-8.754854,-4.890051,-6.306664,3.641792,6.830149,-6.417530,-8.293095,-5.266163,-0.821649,-6.073991,1.777248,-0.613298,7.445263,-9.788868,8.084577],[3.955751,6.798468,-1.926625,8.243273,-3.742142,-6.239899,6.548168,7.182529,9.660830,2.815195,-2.203406,7.784232,-3.929285,3.251578,3.432969,1.942682]],[[-6.216373,-5.049341,-9.184458,-2.031786,6.599544,-1.796919,-9.596866,-6.123922,9.269694,4.061620,-2.685405,-8.222282,3.829409,1.371126,-5.342751,0.941842],[-6.439903,-1.516327,6.085286,2.085022,5.350074,1.001821,9.572465,4.523341,6.341523,2.498233,-6.928178,-8.495617,3.248203,-5.774499,-2.880414,-8.532909],[4.370033,-2.084823,-3.934503,6.364532,7.260701,3.674640,-2.228750,8.644330,7.033303,7.828399,-4.234760,8.274013,-3.529417,-4.475250,9.612854,5.383414],[2.098634,8.488117,8.719357,3.360403,8.424353,-4.690014,-5.359882,1.597100,-7.395061,0.015006,-6.721443,-8.049590,-6.270678,4.863354,7.253388,-2.739660],[-8.461856,-0.308143,5.501087,-5.867954,-6.056810,-7.966746,-1.987482,-8.348805,3.914809,-4.793872,-1.105117,-0.785413,4.455817,-2.366701,-9.932374,7.750515]],[[-6.804417,-2.997814,1.862181,-8.782616,2.275906,-3.528997,-0.193073,-8.562901,-0.111612,3.281291,7.373266,4.965873,-5.538390,-1.271374,1.558597,9.847292],[3.050815,6.088531,3.920693,3.627677,-7.577597,-4.634819,-1.324931,-0.524214,5.795681,-3.896771,0.314104,8.901260,5.609355,-8.919382,0.615740,2.375772],[-1.130147,-4.190770,-6.309604,-2.541552,6.824644,-6.009667,-9.293128,7.053543,-3.369733,-0.889939,1.326969,3.295285,9.627144,7.446544,-4.469857,-2.107890],[4.957968,-7.489463,-4.099968,5.781833,4.862224,9.017892,-7.751632,-7.603647,-5.087590,8.608267,-8.720649,3.660003,-9.699381,4.266713,9.217760,4.599336],[-6.227516,-7.642306,4.346454,-4.628683,2.423465,-1.103281,-4.957291,5.138280,8.850221,5.637415,3.580501,-5.645716,3.649391,-1.833304,4.226410,-0.103391]],[[8.979301,-8.220791,-8.494120,-5.295084,-8.671577,0.896977,5.471623,-8.967061,8.305695,-3.794841,-8.578272,2.163262,-0.343223,-5.879245,7.902239,1.231015],[3.837801,0.964297,5.069157,-5.298971,-2.907912,-5.689495,-6.032335,8.224891,-7.195493,-2.136862,-8.946823,8.927395,-9.166356,-4.881660,-6.351098,-8.935345],[9.844516,4.743467,6.497640,-1.803804,0.465172,7.767862,6.539785,-6.924368,0.164255,-1.183619,-8.274219,-6.149570,2.598475,-1.106911,0.919769,-4.945926],[7.674898,7.030669,8.034645,-6.475532,-8.265632,-5.356892,-0.836016,-3.501878,3.406522,3.582816,-1.176306,-8.696420,-6.270129,4.695538,-6.850828,-4.530626],[7.317820,-4.524007,-0.372682,4.982089,9.819284,-6.149317,-1.004870,6.968115,-6.269396,8.332586,-5.417204,-0.186051,6.281087,-0.136355,8.893280,3.830272]],[[-0.631752,3.366645,-2.801315,-2.931222,-4.043767,-3.819362,3.050415,1.421965,-4.934104,-5.377780,-4.048307,-8.965138,-5.590232,3.420551,9.418498,-9.490512],[3.778930,-2.774602,-7.974770,5.042890,-3.610310,-4.840440,3.746376,6.524476,-0.705132,-6.803656,-0.388577,-3.692299,-7.976728,2.840259,-6.319905,4.003492],[6.554560,-6.436119,-2.771357,9.861910,6.106282,-1.080141,5.183677,-1.262938,8.990603,-2.135850,0.806816,-2.848831,5.336156,-1.813563,3.065994,0.732623],[2.539986,9.415228,4.698241,-6.632131,-6.540361,4.810168,-8.990498,3.338582,-8.309464,-1.676446,3.104281,2.860999,-4.742272,-4.167551,-8.013169,-5.016567],[0.838604,3.866966,-8.335372,3.563440,4.511834,-0.448011,3.725401,3.877077,-1.234094,6.344466,8.632608,-5.802391,-7.413738,9.422814,-0.662608,3.234543]]], dtype = "float32")#candidate|4263|(16, 5, 16)|const|float32
bop_4264 = relay.floor_divide(var_4262.astype('float32'), relay.reshape(const_4263.astype('float32'), relay.shape_of(var_4262))) # shape=(16, 5, 16)
func_2038_call = mod.get_global_var('func_2038')
func_2040_call = mutated_mod.get_global_var('func_2040')
var_4268 = relay.var("var_4268", dtype = "float32", shape = (2, 32))#candidate|4268|(2, 32)|var|float32
call_4267 = relay.TupleGetItem(func_2038_call(relay.reshape(var_4268.astype('float32'), [4, 4, 4])), 0)
call_4269 = relay.TupleGetItem(func_2040_call(relay.reshape(var_4268.astype('float32'), [4, 4, 4])), 0)
uop_4286 = relay.cos(call_4267.astype('float64')) # shape=(4, 4, 4)
uop_4288 = relay.cos(call_4269.astype('float64')) # shape=(4, 4, 4)
output = relay.Tuple([bop_4264,var_4268,uop_4286,])
output2 = relay.Tuple([bop_4264,var_4268,uop_4288,])
func_4298 = relay.Function([var_4262,var_4268,], output)
mod['func_4298'] = func_4298
mod = relay.transform.InferType()(mod)
var_4299 = relay.var("var_4299", dtype = "float32", shape = (16, 5, 16))#candidate|4299|(16, 5, 16)|var|float32
var_4300 = relay.var("var_4300", dtype = "float32", shape = (2, 32))#candidate|4300|(2, 32)|var|float32
output = func_4298(var_4299,var_4300,)
func_4301 = relay.Function([var_4299,var_4300,], output)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4455 = relay.const([[[-5,-9],[-6,-3],[1,-1],[3,-2],[-7,10],[-2,-6],[-8,1],[-8,-7],[7,10]],[[-10,-2],[-2,-9],[2,2],[8,-9],[-10,7],[7,3],[2,6],[7,-5],[-1,-7]],[[-9,10],[6,3],[7,-6],[-8,-4],[10,-8],[-7,-4],[-4,-1],[-5,10],[3,-7]]], dtype = "int16")#candidate|4455|(3, 9, 2)|const|int16
var_4456 = relay.var("var_4456", dtype = "int16", shape = (3, 9, 2))#candidate|4456|(3, 9, 2)|var|int16
bop_4457 = relay.bitwise_xor(const_4455.astype('int16'), relay.reshape(var_4456.astype('int16'), relay.shape_of(const_4455))) # shape=(3, 9, 2)
func_538_call = mod.get_global_var('func_538')
func_541_call = mutated_mod.get_global_var('func_541')
var_4461 = relay.var("var_4461", dtype = "float64", shape = (585,))#candidate|4461|(585,)|var|float64
var_4462 = relay.var("var_4462", dtype = "int16", shape = (450,))#candidate|4462|(450,)|var|int16
call_4460 = relay.TupleGetItem(func_538_call(relay.reshape(var_4461.astype('float64'), [13, 15, 3]), relay.reshape(var_4462.astype('int16'), [450,]), ), 2)
call_4463 = relay.TupleGetItem(func_541_call(relay.reshape(var_4461.astype('float64'), [13, 15, 3]), relay.reshape(var_4462.astype('int16'), [450,]), ), 2)
func_3298_call = mod.get_global_var('func_3298')
func_3301_call = mutated_mod.get_global_var('func_3301')
const_4465 = relay.const([-8,10,-1,10,-3,-10,-8,4,-5,5,-6,4,-9,-2,-2,9,-5,1,-5,-10,3,1,5,7,2,-3,-10,10,4,2,-5,8,-2,-8,10,-5,-7,4,-4,4,-5,-6,-4,4,-10,-7,-9,-7,-4,10,-2,-6,-3,-3,-3,5,-5,-3,-7,8,5,-4,-10,7,-5,-5,2,-8,-2,-4,-1,3,9,-7,-2,8,10,-4,-5,4,8,9,-1,-8,1,9,2,7,5,10,1,-7,-9,1,1,-4,-3,10,-1,10,-2,-1,1,6,4,-5,3,5,-2,6,10,-2,-2,-10,3,-2,-8,-7,-4,5,10,-4,2,3,-6,7,8,10,6,-2,7,-3,-8,4,-5,2,6,6,-5,-4,-9,-6,2,6,5,6,3,-9,-2,-5,-9,-4,-2,7,-1,-10,-1,9,4,3,5,-3,1,-9,4,-1,10,-2,-6,-4,7,9,-2,-3,-6,-6,-6,-9,-1,-9,2,-8,3,-9,-8,-6,-6,-4,3,-5,-4,10,-1,6,-7,7,-4,4,-6,6,5,-8,7,9,1,-9,-8,6,7,-9,8,-4,2,8,2,-9,-6,-5,-1,2,-2,-9,-1,-8,-9,-3,-5,-7,-6,3,1,-2,-1,1,-5,5,6,-6,1,5,2,-4,4,4,-8,-7,-8,-7,10,-2,1,-2], dtype = "uint8")#candidate|4465|(252,)|const|uint8
const_4466 = relay.const([3,-3,1,4,-2,9,-10,2,-8,-10,1,5,5,-1,2,-7,4,-3,7,2,-8,7,10,7,10,-4,-7,4,-6,1,7,-3,7,-7,3,-6,-2,1,10,9,5,-1,-4,-6,-10,-8,-6,7,9,10,5,5,6,-7,-1,-8,-2,1,-4,6,-6,10,-5,5,-2,8,-8,-3,6,-1,-8,7,8,6,7,-9,-6,4,7,-5,-4,-4,-5,-9,1,-10,-10,1,-5,1,10,-4,8,-8,-7,4,8,-4,-9,6,4,8,-4,-2,-5,10,5,-2,4,-10,4,2,1,7,-10,9,8,6,8,1,-10,-9,-7,-8,10,1,1,8,-9,4,-7,-1,-2,-4,-2,-4,-8,-5,-3,-5,10,-8,9,-5,-4,-8,-1,3,6,4,4,10,8,-8,-10,-5,-1,5,3,-8,6,6,-7,-3,-10,-10,-2,8,-8,10,-1,2,9,4,5,7,-10,-3,5,7,-10,10,9,-1,-6,7,-7,1,-6,6,-7,-7,7,3,3,-7,-8,4,-7,-4,-5,4,10,7,-10,-9,7,3,3,8,-7,8,2,-3,-6,-5,8,4,5,-5,-6,4,-10,9,-5,1,10,5,3,2,-5,-2,-6,-10,-10,8,9,1,-8,-3,7,-3,5,-10,8,-8,1,-3,-8,10,7,-6,-1,-6,-7,-2,-4,1,4,8,3,4,-5,3,-9,-1,-2,-5,-4,-1,-1,-3,-9,6,6,-5,9,-3,6,10,-10,4,-8,2,-9,10,6,-6,-8,8,6,2,-3,-4,4,4,2,3,-6,-1,8,6,-7,-8,-7,-10,8,-2,1,-1,7,7,5,1,-5,-10,-6,-6,1,7,-8,10,-8,-8,6,2,-7,5,8,-5,8,3,-2,-4,-3,-8,7,7,-2,-6,6,-4,-6,-7,4,-5,-9,-6,-9,3,-5,-1,1,-10,4,-3,-6,7,7,6,8,-6,2,-6,-4,3,10,-4,3,-5,-1,-9,-5,-9,-10,4,8,3,-1,3,9,-7,-9,1,-4,-8,5,2,-4,4,5,2,-7,-3,7,6,-9,7,3,-9,4,-3,-5,-1,-3,-4,3,2,-4,-10,9,9,8,-6,-5,9,-2,-10,-7,-7,8,-1,-9,2,-5,6,-8,-4,10,9,-6,-5,-3,5,-8,2,-6,-6,5,-10,-10,-8,1,7,1,9,6,-6,-8,9,-7,-1,-6,-8,5,-5,4,3,3,-7,6,4,9,-1,2,5,2,2,3,1,8,10,7,-7,3,-7,-1,1,2,9,1,-3,1,1,5,-1,5,-7,7,5,10,-9,4,3,1,1,-7,4,-2,-2,-8,4,-6,-8,-4,5,6,9,3,7,3,5,-4,7,-6,5,-4,9,-9,-5,1,-1,3,8,-9,9,5,-1,2,7,7,-4,-2,-4,-10,-3,10,-8,1,8,-3,3,10,-10,-2,-2,10,1,-9,-2,4,9,-9,-7,-5,4,4,7,-9,-8,-4,1,8,-8,7,-5,-5,-6,-1,9,-10,5,10,9,7,-10,2,6,5,5,4,-4,-6,7,5,-5,-9,-10,10,-8,-1,-1,2,-10,-3,-9,-9,-8,-5,-2,1,7,6,8,-9,7,7,-2,5,-5,1,5,-1,2,-6,-8,2,6,5,5,2,-7,-10,-7,-10,-1,-10,-10,-9,-7,-7,-3,-2,-8,-5,-4,-7,-8,-7,1,-9,10,-9,8,-3,5,2,10,7,1,-2,-10,4,-3,-5,2,-7,3,5,7,8,9,-10,-4,-6,10,1,-7,2,-8,6,-10,2,-2,9,-4,-1,-9,-1,-9,-9,5,1,-5,-3,9,-4,-2,-4,-3,4,-2,-10,6,-3,10,-4,-3,8,7,2,-9,-6,-3,5,-5,-5,4,7,1,-2,5,-6,10,-6,-5,6,-5,5,3,5,-3,-5,10,-6,4,-9,-6,7,1,7,-2,-10,-3,8,-8,-6,-5,-5,-4,5,-1,-9,1,4,-9,-8,2,-1,-4,3,-2,-3,1,-4,-1,5,5,-10,9,-8,5,-9,-7,-3,9,-3,8,-10,3,4,-2,7,-2,-4,1,7,-2,-4,-9,10,-7,-9,-8,-4,2,9,6,3,-3,8,1,-3,-4,-1,-5,10,-3,-7,-7,-4,-6,3,8,-1,-5,8,-2,10,-7,-8,-4,-4,-7,-10,9,-3,8,8,-4,-1,-6,4,10,-6,6,9,4,7,-2,8,-2,8,-7,-7,5,-9,-7,-1,-8,5,-4,-4,-8,4,1,-3,10,-2,-8,-7,9,6,-10,2,-5,-2,1,-9,-10,-1,4,-3,-5,-1,-5,8,6,-9,-10,-6,8,-3,-5,-10,-7,5,6,4,-4,6,7,3,-5,-2,3,-9,-6,-2,7,8,-4,5,-3,-3,6,-8,3,-6,4,-5,-6,8,9,2,3,-1,-5,6,5,-6,-1,6,6,4,2,8,6,-7,-7,2,-1,6,-9,-7,-4,-9,-9,-8,-9,-6,-2,8,-10,4,7,5,8,5,6,6,-5,4,2,-9,-4,3,-1,5,-9,9,4,-2,-7,-2,9,2,2,5,10,6,-3,2,-1,5,6,4,10,-4,4,-10,5,6,2,3,9,5,-8,6,-4,9,-5,-1,2,-1,-5,-1,5,-10,-9,6,-4,-10,10,4,-8,-5,8,7,-5,-8,1,1,-7,2,5,3,-1,-4,10,-6,-10,1,-8,10,9,4,-7,4,9,9,-6,-5,-7,9,-6,-4,-5,-6,3,8,6,-10,10,-7,1,-3,10,5,7,-3,-6,-9,1,-6,3,-6,8,4,-1,-7,8,-1,-7,4,-8,-7,5,7,-3,-2,-7,-7,-4,4,-1,8,-10,6,5,1,8,-10,-4,-10,-10,-3,-1,-3,-9,-10,10,8,7,7,-5,-7,-6,7,-2,7,9,10,-8,5,-9,-8,3,9,1,3,-6,-10,-7,-4,-5,-10,9,-6,-2,6,4,-2,-1,8,-1,-9,-1,-1,7,-7,4,-9,-9,2,6,5,-4,-6,2,-9,4,9,-9,6,-6,2,-2,5,-6,3,8,1,-6,7,2,8,3,3,-10,2,4,5,5,-7,10,-2,-7,8,-9,-1,2,8,9,-9,-2,4,-5,10,-3,-2,7,1,6,-1,-6,-7,-4,-4,-6,-3,-6,-4,9,2,3,5,7,-5,-7,1,9,-4,2,-7,2,9,-8,-2,7,9,7,9,9,-10,-2,-2,8,-5,5,-9,3,-7,-8,-8,-3,4,-10,-8,9,-9,-9,-2,-8,-5,9,2,-3,3,-7,8,-9,-4,5,1,-9,5,-1,3,1,4,4,-2,-4,8,-7,3,-1,6,-6,2,-9,-3,3,2,4,4,10,4,-10,-5,-1,4,5,7,-8,7,5,10,6,2,7,-9,-1,-3,9,1,-6,3,-6,3,1,-3,-1,-4,4,8,-1,8,-2,-4,-1,-3,9,-8,-6,1,4,4,7,-4,-4,-2,-1,-9,-3,4,-10,-1,-10,-6,-2,4,2,-3,5,-10,2,-6,-4,4,7,-3,4,8,3,-2,10,4,5,-1,-5,-3,-4,-9,-3,-8,-2,9,-5,2,10,6,4,-4,-5,1,-7,-8,3,-1,-10,-7,10,-8,3,-4,8,3,-7,-10,1,6,-8,-8,2,5,8,4,-10,-4,4,5,7,-1,4,-1,-5,-4,-1,-3,-2,3,-2,10,9,4,4,-3,-5,9,8,-8,-7,7,5,-9,8,-8,8,4,-4,1,6,-2,10,2,-1,4,-3,6,-1,-4,8,1,2,5,2,3,-2,10,-6,2,3,7,-7,5,-9,-8,10,5,5,-7,6,6,7,-9,-8,-2,9,8,-4,3,-1,10,-10,-5,-5,-1,-4,-6,-3,-8,8,-4,1,2,-5,9,-7,9,-6,-2,7,-1,-2,-6,3,-8,3,-7,-3,10,-5,-6,-9,-10,9,7,9,9,-6,8,8,-2,7,-3,-8,8,3,-6,9,9,-1,-4,-6,-2,9,-4,8,-7,-3,5,3,-7,-9,1,10,-6,6,-9,-6,-5,-5,-1,4,7,-8,1,10,-10,-10,9,-10,-8,6,1,2,-8,-6,1,-8,-9,3,-10,7,-3,2,4,-6,10,-2,3,-10,3,1,8,-2,-6,7,9,-7,-1,-2,-10,-9,-10,5,7,6,1,-5,5,-4,-2,6,-4,-2,1,-2,-2,-3,-4,-8,2,-2,-9,2,4,-6,6,8,4,-5,-3,6,-7,-10,7,-1,-9,-2,10,6,-9,-10,6,-4,-7,-5,-7,-10,2,-7,-7,6,3,-6,-1,9,-5,-4,7,1,-1,8,1,-4,7,10,10,-10,5,6,-8,-7,-5,4,-2,-8,5,-3,-6,-7,-8,7,-6,-1,-2,-8,-3,5,-9,2,8,-6,-7,-7,-6,8,-5,4,-1,-2,-3,5,-9,-5,-1,-2,6,10,-7,-10,5,-10,2,-10,8,-8,-6,10,3,-6,2,-1,-7,6,8,-8,-2,3,-2,-7,-7,-3,7,-8,9,-5,1,-1,-5,-2,-1,-7,-1,-8,-5,1,-1,-7,-8,-1,1,7,-9,2,-5,10,7,2,-10,-8,7,-9,6,9,2,-2,-5,7,-1,-10,3,4,-7,-7,9,4,-7,-8,-2,10,8,-9,4,7,-4,2,6,7,-4,-2,2,-1,-2,3,-8,8,-6,9,10,3,-2,1,-3,-3,5,-10,-5,7,3,-1,-4,5,3,-1,-1,-9,9,2,10,-9,-3,3,3,7,-3,-5,5,-8,7,3,4,-10,2,7,7,9,4,-10,-6,-2,-3,-6,10,-9,5,-2,4,4,-4,-9,4,1,-2,8,7,-6,9,-1,8,-4,1,-4,8,2,8,2,-9,-1,-5,-6,-8,-3,4,6,5,7,-7,-3,-8,6,-6,7,3,-6,-8,1,7,-3,-9,5,10,-9,4,10,9,-5,6,10,-1,-8,-1,4,-2,-10,-7,-4,-8,2,7,3,1,2,-1,7,-1,10,-1,-3,-1,-3,-8,5,-3,10,-10,7,1,9,2,-2,10,-6,-6,3,1,-8,-6,-9,-2,9,9,3,3,-10,5,-9,-5,5,5,-1,-7,-9,1,-2,-4,5,6,3,-8,-8,8,10,-6,7,7,10,-4,-9,-7,-10,-1,-4,10,8,-4,-3,-4,8,-9,1,-10,2,-2,-2,1,7,4,-10,-3,-6,-7,-1,-3,-2,3,-10,6,8,-2,-6,2,-6,-7,3,-9,8,8,-8,8,5,3,4,-7,9,3,-4,-9,1,9,7,-5,-5,-6,-5,-10,6,6,-7,4,-2,-1,2,-7,7,1,5,1,-10,-2,9,-7,-7,7,-6,2,-8,4,-5,2,-8,-6,-8,2,1,-5,6,-7,3,-9,-5,-6,-3,2,1,10,7,-10,-2,-5,6,5,-1,7,8,-4,-6,-5,-1,9,-1,9,4,4,-6,10,10,6,-8,9,10,9,6,-6,-1,8,3,-9,-1,-4,-6,8,10,9,-8,3,2,3,4,-2,4,6,-9,8,-1,-6,-7,-1,10,-2,-8,6,5,-7,-9,-7,-1,2,-9,2,3,5,4,-4,7,3,-10,-5,-6,-7,1,10,6,-4,2,-5,3,2,7,10,-3,9,-3,2,7,6,3,4,6,4,-1,3,-8,-1,-3,9,5,-1,2,-8,1,1,-8,5,10,-3,10,-6,3,3,8,1,-10,2,4,-3,3,-2,8,8,9,-10,7,9,-3,5,-6,7,-9,-10,-10,-9,-8,8,8,-3,-7,-6,-10,6,7,9,8,-9,-6,9,1,-10,8,-4,-4,-3,-1,5,6,-9,3,-6,3,-7,4,6,7,-2,-6,3,-3,-8,7,-8,-5,6,4,-8,-7,9,-4,-5,-2,5,-5,-5,5,5,-9,5,-1,-1,-2,5,5,-9,8,7,2,8,-10,-8,-10,-9,7,2,-6,4,-3,7,10,4,-3,9,-5,-5,-2,2,-5,9,-6,1,-6,-9,-1,-7,-6,2,-4,-5,8,3,-2,-9,7,-10,-3,-4,3,9,4,8,9,-9,10,1,1,-7,-1,1,-6,-1,-9,9,-2,7,-4,-6,-4,-3,9,10,8,-5,4,6,-5,1,2,6,-8,-10,8,5,-2,-4,-4,1,4,10,-9,9,3,-8,2,1,-8,4,8,8,8,9,8,4,5,9,-2,10,10,2,-3,-4,5,-5,-7,-5,4,-5,-5,4,2,-3,-4,2,10,-10,7,2,-1,-7,1,-3,5,7,6,-7,7,-5,-3,-6,10,-6,1,-1,6,-1,7,1,-2,1,2,-8,-9,1,-9,7,-5,6,-10,8,-4,-2,-3,-4,-1,-2,-4,3,3,-9,1,2,8,1,7,-3,-10,-6,8,-7,7,-4,-2,-8,1,7,-1,9,1,7,-1,10,5,-2,6,-4,1,-7,4,-7,-1,6,-7,3,-5,5,1,5,3,-3,-9,3,-4,4,-6,-5,-9,-10,6,-4,4,-6,9,2,-1,1,1,-3,-4,7,9,-8,-4,7,-2,2,-4,-2,2,-3,9,6,-9,9,5,5,7,-4,-10,1,-4,9,-3,-9,4,-9,-7,5,3,9,-1,4,6,10,-1,-1,6,-4,-8,4,-6,-5,6,-9,5,9,-2,5,-2,-7,6,9,7,-10,6,-7,5,-5,5,3,4,7,2,-6,-6,9,-1,5,2,3,1,2,3,8,3,-7,3,3,-5,-2,-3,7,9,-4,-9,-1,-8,-6,-10,6,-8,-10,-8,-6,5,-5,9,4,4,-9,4,3,2,-2,6,6,2,4,-3,2,10,-6,-9,-9,8,-8,-7,-6,-10,1,-6,-1,5,10,-8,3,2,-7,10,6,3,2,-4,-10,7,-2,10,-5,9,-2,8,4,-7,-2,6,-6,-9,10,-9,8,2,10,3,7,-9,-8,-6,-8,5,9,6,-10,-6,-10,1,-10,10,-6,-5,7,-2,2,9,-9,8,6,7,-10,-8,-7,-10,3,7,7,10,8,10,10,-8,6,10,1,-9,10,3,6,4,-7,9,-5,-7,3,-10,9,-1,-5,8,-8,-1,4,-4,9,-2,-1,10,1,10,7,6,-10,-10,10,3,4,-6,7,-1,-10,-7,-5,10,6,-2,9,-6,5,-6,-3,4,-4,-6,-10,1,3,4,5,-5,-1,-2], dtype = "int32")#candidate|4466|(2688,)|const|int32
call_4464 = relay.TupleGetItem(func_3298_call(relay.reshape(const_4465.astype('uint8'), [3, 14, 6]), relay.reshape(const_4466.astype('int32'), [2688,]), ), 2)
call_4467 = relay.TupleGetItem(func_3301_call(relay.reshape(const_4465.astype('uint8'), [3, 14, 6]), relay.reshape(const_4466.astype('int32'), [2688,]), ), 2)
output = relay.Tuple([bop_4457,call_4460,var_4461,var_4462,call_4464,const_4465,const_4466,])
output2 = relay.Tuple([bop_4457,call_4463,var_4461,var_4462,call_4467,const_4465,const_4466,])
func_4472 = relay.Function([var_4456,var_4461,var_4462,], output)
mod['func_4472'] = func_4472
mod = relay.transform.InferType()(mod)
var_4473 = relay.var("var_4473", dtype = "int16", shape = (3, 9, 2))#candidate|4473|(3, 9, 2)|var|int16
var_4474 = relay.var("var_4474", dtype = "float64", shape = (585,))#candidate|4474|(585,)|var|float64
var_4475 = relay.var("var_4475", dtype = "int16", shape = (450,))#candidate|4475|(450,)|var|int16
output = func_4472(var_4473,var_4474,var_4475,)
func_4476 = relay.Function([var_4473,var_4474,var_4475,], output)
mutated_mod['func_4476'] = func_4476
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4491 = relay.const([[[8.290914,2.332883,-0.455990],[4.050294,5.886093,-4.174757],[-5.960559,-3.376780,-6.038214],[9.952366,-0.321162,-7.261954]],[[3.756034,4.193190,-1.497060],[0.254816,-1.717778,9.508957],[-0.307495,6.967824,9.506968],[-1.868121,6.929770,-4.006817]],[[-2.707188,0.662420,7.170716],[1.506854,-9.781533,-6.102086],[7.654372,9.238565,-8.417539],[6.577244,7.439546,-1.438851]],[[-7.072739,-0.768362,3.294556],[-0.383204,-9.710424,-6.785256],[3.057974,6.967483,4.903611],[-1.336386,4.576382,-1.389523]],[[-8.728492,-3.902388,5.276732],[8.719256,-3.013748,3.135441],[-1.720743,9.780639,4.591813],[3.402242,1.890462,7.615180]],[[-0.775867,-6.353327,9.993053],[6.519407,-2.446262,8.830138],[-8.533641,3.154374,-0.569323],[-3.224237,-6.899440,5.820556]]], dtype = "float32")#candidate|4491|(6, 4, 3)|const|float32
uop_4492 = relay.cos(const_4491.astype('float32')) # shape=(6, 4, 3)
func_986_call = mod.get_global_var('func_986')
func_988_call = mutated_mod.get_global_var('func_988')
const_4505 = relay.const([[0.856915,7.958061,-5.852545,-8.810867,4.598551,6.967981,-7.259502,1.441396,-2.024677,8.502867,-6.154032,7.966039,9.238800,-2.694597,2.105665,8.079395,8.372096,-3.635368,2.027250,0.959462,-8.502166,4.773642,-6.849783,7.397675,-7.869219,-7.498675,1.039274,9.207012]], dtype = "float32")#candidate|4505|(1, 28)|const|float32
call_4504 = relay.TupleGetItem(func_986_call(relay.reshape(const_4505.astype('float32'), [1, 4, 7])), 0)
call_4506 = relay.TupleGetItem(func_988_call(relay.reshape(const_4505.astype('float32'), [1, 4, 7])), 0)
bop_4507 = relay.less(const_4505.astype('bool'), relay.reshape(call_4504.astype('bool'), relay.shape_of(const_4505))) # shape=(1, 28)
bop_4510 = relay.less(const_4505.astype('bool'), relay.reshape(call_4506.astype('bool'), relay.shape_of(const_4505))) # shape=(1, 28)
output = relay.Tuple([uop_4492,bop_4507,])
output2 = relay.Tuple([uop_4492,bop_4510,])
func_4527 = relay.Function([], output)
mod['func_4527'] = func_4527
mod = relay.transform.InferType()(mod)
output = func_4527()
func_4528 = relay.Function([], output)
mutated_mod['func_4528'] = func_4528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_4555 = relay.TupleGetItem(func_4527_call(), 0)
call_4556 = relay.TupleGetItem(func_4528_call(), 0)
output = relay.Tuple([call_4555,])
output2 = relay.Tuple([call_4556,])
func_4562 = relay.Function([], output)
mod['func_4562'] = func_4562
mod = relay.transform.InferType()(mod)
output = func_4562()
func_4563 = relay.Function([], output)
mutated_mod['func_4563'] = func_4563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4562_call = mod.get_global_var('func_4562')
func_4563_call = mutated_mod.get_global_var('func_4563')
call_4577 = relay.TupleGetItem(func_4562_call(), 0)
call_4578 = relay.TupleGetItem(func_4563_call(), 0)
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_4596 = relay.const([-10,4,4,4,6,10,-4,-3,-10,-1,1,-9,-8,-10,-1,-3,-7,-2,10,7,-7,-1,1,8,-6,10,-4,10,4,-2,-2,-5,-5,-2,-4,-2,-7,3,-6,-9,-9,-2,8,6,-1,-8,-5,-3,-1,-5,5,7,10,-10,-1,9,-8,3,-4,-1,-7,-1,5,5,1,2,-7,8,8,-6,-8,9,9,-5,2,1,6,-4,-7,6,8,4,8,-7,-1,-7,1,5,1,2,-6,3,-4,-3,-5,-9,-1,-10,-4,-7,-1,1,2,1,-8,7,7,-7,6,-2,-3,5,3,-2,6,9,4,9,-8,1,5,-3,7,-3,-2,-5,-5,8,10,4,-7,-3,-3,-9,5,8,-6,-2,2,8,-10,10,5,-5,8,-1,10,-6,-10,-5,-4,5,-5,5,-4,-3,5,-2,-1,-7,4,-2,4,9,-4,9,9,-10,-4,-4,-7,3,-8,4,9,8,9,-10,-9,-7,3,-3,-3,-7,-7,3,7,9,10,7,-5,5,-7,9,3,-1,5,1,6,-2,10,-10,-3,4,-2,-5,6,-3,4,-8,-1,7,4,1,-5,-2,2,2,1,-9,9,-2,-1,-9,-10,-5,-8,4,-8,2,1,10,8,-7,10,-1,-7,5,9,-6,-10,9,-3,2,9,-7,-7,-4,-9,-3,-6,-7,9,-4,5,-9,-10,7,-1,-7,10,-3,-10,-4,-7,-1,3,-7,-1,3,10,1,10,3,6,4,-3,4,3,6,5,4,-5,-10,-1,-2,-5,-8,2,8,1,-3,10,-2,5,4,5,-6,6,-9,-9,5,4,8,-7,4,-8,-6,4,1,6,-9,-1,3,1,6,1,-3,-7,2,7,3,5,-6,-7,-10,2,6,-4,-5,-1,6,-4,-10,2,-4,10,-6,9,5,9,-3,-5,-8,-7,4,6,3,-9,-9,-5,-9,4,-9,7,1,9,1,-2,-3,-4,9,6,-7,5,7,-1,-4,-2,-8,-8,9,4,1,10,6,-10,-1,-9,3,-6,-1,-5,-2,9,-9,2,4,7,1,-7,9,-4,-4,-1,-4,-7,6,1,10,1,-6,-7,-8,-4,-10,-7,-10,1,3,-3,1,-3,2,4,-5,3,-7,-10,3,-5,6,-3,-5,2,-8,-7,3,-5,-6,-10,5,2,4,-8,-9,1,5,2,10,-9,9,9,-6,10,7,-4,-3,-6,-2], dtype = "int16")#candidate|4596|(450,)|const|int16
call_4595 = relay.TupleGetItem(func_54_call(relay.reshape(const_4596.astype('int16'), [15, 6, 5]), relay.reshape(const_4596.astype('int16'), [15, 6, 5]), ), 0)
call_4597 = relay.TupleGetItem(func_57_call(relay.reshape(const_4596.astype('int16'), [15, 6, 5]), relay.reshape(const_4596.astype('int16'), [15, 6, 5]), ), 0)
output = relay.Tuple([call_4577,call_4595,const_4596,])
output2 = relay.Tuple([call_4578,call_4597,const_4596,])
func_4606 = relay.Function([], output)
mod['func_4606'] = func_4606
mod = relay.transform.InferType()(mod)
mutated_mod['func_4606'] = func_4606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4606_call = mutated_mod.get_global_var('func_4606')
call_4607 = func_4606_call()
output = call_4607
func_4608 = relay.Function([], output)
mutated_mod['func_4608'] = func_4608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_4688 = relay.TupleGetItem(func_4527_call(), 1)
call_4689 = relay.TupleGetItem(func_4528_call(), 1)
output = relay.Tuple([call_4688,])
output2 = relay.Tuple([call_4689,])
func_4699 = relay.Function([], output)
mod['func_4699'] = func_4699
mod = relay.transform.InferType()(mod)
mutated_mod['func_4699'] = func_4699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mutated_mod.get_global_var('func_4699')
call_4700 = func_4699_call()
output = call_4700
func_4701 = relay.Function([], output)
mutated_mod['func_4701'] = func_4701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_4873 = relay.TupleGetItem(func_4527_call(), 0)
call_4874 = relay.TupleGetItem(func_4528_call(), 0)
output = relay.Tuple([call_4873,])
output2 = relay.Tuple([call_4874,])
func_4882 = relay.Function([], output)
mod['func_4882'] = func_4882
mod = relay.transform.InferType()(mod)
mutated_mod['func_4882'] = func_4882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mutated_mod.get_global_var('func_4882')
call_4883 = func_4882_call()
output = call_4883
func_4884 = relay.Function([], output)
mutated_mod['func_4884'] = func_4884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_4975 = relay.TupleGetItem(func_4527_call(), 0)
call_4976 = relay.TupleGetItem(func_4528_call(), 0)
output = relay.Tuple([call_4975,])
output2 = relay.Tuple([call_4976,])
func_4983 = relay.Function([], output)
mod['func_4983'] = func_4983
mod = relay.transform.InferType()(mod)
mutated_mod['func_4983'] = func_4983
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4983_call = mutated_mod.get_global_var('func_4983')
call_4984 = func_4983_call()
output = call_4984
func_4985 = relay.Function([], output)
mutated_mod['func_4985'] = func_4985
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4992 = relay.var("var_4992", dtype = "float64", shape = (1, 14, 6))#candidate|4992|(1, 14, 6)|var|float64
uop_4993 = relay.tan(var_4992.astype('float64')) # shape=(1, 14, 6)
output = relay.Tuple([uop_4993,])
output2 = relay.Tuple([uop_4993,])
func_5008 = relay.Function([var_4992,], output)
mod['func_5008'] = func_5008
mod = relay.transform.InferType()(mod)
mutated_mod['func_5008'] = func_5008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5009 = relay.var("var_5009", dtype = "float64", shape = (1, 14, 6))#candidate|5009|(1, 14, 6)|var|float64
func_5008_call = mutated_mod.get_global_var('func_5008')
call_5010 = func_5008_call(var_5009)
output = call_5010
func_5011 = relay.Function([var_5009], output)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4983_call = mod.get_global_var('func_4983')
func_4985_call = mutated_mod.get_global_var('func_4985')
call_5035 = relay.TupleGetItem(func_4983_call(), 0)
call_5036 = relay.TupleGetItem(func_4985_call(), 0)
func_361_call = mod.get_global_var('func_361')
func_364_call = mutated_mod.get_global_var('func_364')
const_5053 = relay.const(-0.610560, dtype = "float32")#candidate|5053|()|const|float32
var_5054 = relay.var("var_5054", dtype = "float32", shape = (16,))#candidate|5054|(16,)|var|float32
call_5052 = func_361_call(relay.reshape(const_5053.astype('float32'), []), relay.reshape(var_5054.astype('float32'), [4, 1, 4]), )
call_5055 = func_361_call(relay.reshape(const_5053.astype('float32'), []), relay.reshape(var_5054.astype('float32'), [4, 1, 4]), )
output = relay.Tuple([call_5035,call_5052,const_5053,var_5054,])
output2 = relay.Tuple([call_5036,call_5055,const_5053,var_5054,])
func_5060 = relay.Function([var_5054,], output)
mod['func_5060'] = func_5060
mod = relay.transform.InferType()(mod)
var_5061 = relay.var("var_5061", dtype = "float32", shape = (16,))#candidate|5061|(16,)|var|float32
output = func_5060(var_5061)
func_5062 = relay.Function([var_5061], output)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5080 = relay.var("var_5080", dtype = "float32", shape = ())#candidate|5080|()|var|float32
var_5081 = relay.var("var_5081", dtype = "float32", shape = (9, 1, 3))#candidate|5081|(9, 1, 3)|var|float32
bop_5082 = relay.divide(var_5080.astype('float32'), var_5081.astype('float32')) # shape=(9, 1, 3)
var_5086 = relay.var("var_5086", dtype = "float32", shape = (9, 5, 3))#candidate|5086|(9, 5, 3)|var|float32
bop_5087 = relay.mod(bop_5082.astype('float32'), var_5086.astype('float32')) # shape=(9, 5, 3)
output = bop_5087
output2 = bop_5087
func_5096 = relay.Function([var_5080,var_5081,var_5086,], output)
mod['func_5096'] = func_5096
mod = relay.transform.InferType()(mod)
var_5097 = relay.var("var_5097", dtype = "float32", shape = ())#candidate|5097|()|var|float32
var_5098 = relay.var("var_5098", dtype = "float32", shape = (9, 1, 3))#candidate|5098|(9, 1, 3)|var|float32
var_5099 = relay.var("var_5099", dtype = "float32", shape = (9, 5, 3))#candidate|5099|(9, 5, 3)|var|float32
output = func_5096(var_5097,var_5098,var_5099,)
func_5100 = relay.Function([var_5097,var_5098,var_5099,], output)
mutated_mod['func_5100'] = func_5100
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5154 = relay.const([[[-9.307138,-9.524551,3.027570,-1.276351,-7.016439,-1.304648,-8.203301,8.668231,2.184033,-2.208636,0.692275,2.780696,-4.471989,1.383997,3.546409,-1.864280],[8.709804,-6.624396,3.979375,2.243679,-2.284224,-7.368736,6.832317,5.816467,1.618210,-6.177419,-4.638531,-7.557659,-5.408568,9.815587,-0.835526,2.030196],[8.730810,3.998434,3.610559,-8.438018,-1.648063,-8.991311,-9.089816,-5.764343,2.731994,-4.679180,-3.183821,-8.326064,-8.523644,4.918217,-7.905870,7.464829],[-5.410060,-1.196850,4.979107,-4.003993,5.076042,-6.939545,-8.706982,-3.877604,1.237680,-1.873691,2.820088,6.179068,-5.976371,1.780479,4.473070,-9.714643],[6.774670,7.577925,-1.526021,-3.487229,8.874785,8.782129,7.265611,1.643840,6.867260,6.309587,2.266447,-1.417246,4.175210,-1.311196,-0.007230,-9.889773],[3.164730,3.399461,9.507106,2.423917,-4.210247,1.798010,-6.951552,-4.667339,-2.662500,1.210407,-9.832651,5.997644,0.646210,6.990354,8.225609,4.366442],[5.959932,-7.554995,-8.527872,6.190947,-1.408762,-4.956693,-1.158064,-8.041115,-6.631086,-7.121036,-4.027016,-5.059535,7.961516,8.525305,-6.436227,2.874496],[8.000342,-3.799258,3.964094,-4.622742,-7.546753,5.910116,-3.477573,4.754251,7.798483,8.929907,-2.441092,4.054428,0.689249,-3.285807,5.688005,-0.570875],[8.531721,-9.319111,-6.952395,-2.838537,7.504296,5.656758,-5.057264,5.446971,-1.064787,6.321528,-1.527475,-9.626718,2.464171,9.866293,-9.486938,-7.449033]],[[4.480088,2.246388,3.610867,-8.229382,2.992220,-2.581641,3.624586,7.356908,1.818722,-5.605069,6.724450,7.829956,4.389502,2.828648,-4.927590,4.839822],[-9.954904,-7.297227,-3.394661,-6.572063,-8.987298,7.274116,-7.622670,-1.090439,1.870745,-6.009848,7.590255,-0.612805,-0.085058,0.333909,6.525012,-5.747359],[5.668216,1.476459,-3.054005,6.330041,8.935172,-1.374842,6.791129,1.964223,8.328099,5.608496,8.256483,2.294118,9.211725,2.247335,7.542264,-9.642645],[-0.205169,-0.403559,4.460337,9.977148,4.082264,7.001805,-0.304644,4.515525,-1.602804,1.419579,-3.768193,8.744735,3.192624,-2.961905,1.777687,5.890203],[5.944167,-9.928290,5.669052,5.944697,7.232021,8.784974,9.732212,5.833393,5.199654,6.177348,8.050449,8.106564,7.613318,3.732654,-3.855638,-5.665003],[-1.012969,-4.822295,4.619281,-2.454873,-8.357054,-5.316644,4.934314,5.652600,-0.231843,-8.264340,-6.250728,-9.350501,-1.344529,-9.482335,-2.310764,-3.002712],[8.851062,-5.883316,-0.540735,6.266665,-9.989240,-8.738543,8.903930,-7.965860,-1.707812,3.527266,-0.935620,1.337504,2.871666,7.615524,-2.601852,-6.763117],[6.759624,-2.252107,-2.406453,-9.383138,-3.279912,-6.278511,3.066533,7.060943,0.610502,-5.306397,8.916449,-5.999452,1.264082,-8.900037,2.908288,6.704913],[-7.586140,-7.506479,0.169662,2.202929,9.665635,4.299395,6.704301,7.845963,9.435988,-1.390198,1.778161,3.852751,9.068845,-2.938396,-0.854134,5.079740]],[[-4.478110,8.985440,-4.602880,1.203568,-5.347968,-1.518134,0.416955,7.004305,1.091718,9.468083,-4.953677,5.925118,4.905745,1.791174,0.013653,-9.490640],[-1.187877,7.484591,-9.390498,2.950411,9.387220,-3.774965,0.850221,2.118308,-9.057730,2.165815,2.745032,-8.366895,-0.530507,5.307958,-0.217358,3.955962],[2.476473,0.313660,5.169675,4.232109,8.069715,-4.135754,4.475997,3.518663,-1.374221,-6.272613,-6.316192,-8.221445,-0.169157,-5.091755,7.587871,-2.633728],[1.705612,2.925830,-0.325597,3.734675,-1.114694,-2.704164,-1.189436,2.078183,-7.734380,-7.865257,-8.431195,6.446329,-2.611457,6.985198,-5.007594,8.140423],[-1.458643,-6.141883,7.188348,-2.813941,8.955581,8.820818,-9.507384,6.942609,-0.254885,8.485979,-2.848633,-6.297358,2.408215,1.638804,2.797781,2.641704],[2.721104,-7.773134,1.089119,-1.718999,0.303634,-3.964087,9.418870,-1.644158,-4.703906,-6.695183,-1.176521,8.651509,0.367311,1.243824,5.506595,-6.329661],[2.401229,3.366786,1.540759,9.178977,6.863768,-3.716859,4.534098,2.548545,7.598132,0.730869,-0.909069,4.229933,1.080535,-9.587528,9.965553,4.124200],[1.947745,3.062825,-2.127687,3.616978,2.782997,-7.794927,-2.274152,-7.450098,-6.343680,0.533273,-7.903427,-8.026055,-7.282699,3.825632,6.013119,-8.788285],[3.774567,6.023130,-1.827718,-1.447915,-1.285627,6.060432,-9.123139,-2.238538,1.783289,2.881515,-9.106650,5.133517,-5.105759,-8.233665,8.163041,-5.461190]],[[0.647546,-7.050044,-8.988983,1.473994,-6.430627,0.235184,-0.409110,9.080883,1.060693,1.773191,-0.974038,-5.157962,7.600238,-4.970016,4.116880,-4.898904],[-8.659106,7.916916,4.935505,6.313379,9.194950,-4.923167,5.809677,0.065171,-7.655613,-7.563903,4.237198,5.417064,-6.389972,9.182843,-3.895171,-8.492742],[-8.850853,8.682713,-7.072012,5.913674,2.225225,0.149967,3.392468,8.111634,4.115495,-8.190097,7.888325,-5.653617,6.261830,6.287654,1.612885,-0.536382],[1.500823,9.355921,8.211712,7.669740,-5.300947,3.284652,0.776205,0.141125,-4.629052,0.198903,1.266602,4.739021,1.438319,-0.066546,-8.593190,0.696480],[-7.100242,0.709037,9.976089,-3.134168,2.875403,-6.462168,-0.241633,-1.129329,9.233194,-6.947695,3.937047,-1.560113,1.567077,6.709802,0.571805,7.974977],[9.751827,4.870220,-9.052420,-2.123390,6.270956,-8.885425,-1.062465,2.104145,0.167658,-1.926234,6.831443,3.323252,9.236733,6.200047,6.381460,-0.726722],[4.662954,-0.474792,1.808551,-5.274183,1.129878,-9.825266,5.772470,9.578558,-6.182679,9.409090,-6.349798,-9.453289,4.777136,3.820735,-2.044339,7.963938],[8.736374,1.665693,-8.973877,-7.411216,1.837603,0.007677,-6.278401,8.512375,-0.869476,-1.520810,6.526350,-1.964093,-9.667792,-1.246516,4.844432,8.481139],[1.203388,3.105286,-1.126862,1.610238,-4.211767,-2.706777,7.656144,9.504852,-8.620706,3.093082,-4.135618,-8.503985,6.115251,-1.889797,-4.735749,3.508224]],[[-9.241898,3.115008,-7.294493,-9.581506,1.381204,3.988164,-3.011117,-7.827988,6.287479,2.787627,9.799116,-7.660974,-6.062780,8.584476,-2.085424,-8.785363],[9.192211,7.607893,-2.530562,-6.851512,-8.497456,-4.074116,9.257247,0.685990,-2.381419,-2.441360,-1.014259,-0.266041,0.678437,0.052262,2.659204,3.139034],[9.760440,-0.970479,-4.100773,0.340919,0.630201,-8.308595,-4.792365,6.963186,-5.819673,-7.530076,-2.110521,1.934957,-8.156575,-4.445771,-1.190768,-2.072713],[-6.629748,1.166176,-1.794869,-5.259572,-6.640505,-5.509016,-6.784114,-0.888229,6.608160,-7.726553,7.717468,-6.683609,-6.602742,6.655434,-9.369506,9.425572],[6.573147,4.417505,9.908667,5.692693,-8.253415,0.001015,4.179047,4.011983,-7.340885,-8.458508,8.314760,-9.357519,4.103357,-2.369959,6.723183,3.016190],[-9.974337,-3.082649,-0.728652,-8.319307,6.724938,1.129313,5.926808,-4.798804,-6.138515,4.605858,9.700176,-2.196155,-4.178733,-7.760038,-9.910669,-3.105759],[-3.013937,-6.151715,-5.704128,-0.944693,-2.373620,-1.919863,-0.774001,-2.552174,1.807738,7.702015,8.674166,-5.879397,-4.152827,9.275724,-2.999734,-9.074454],[9.707505,3.365326,0.921986,1.973617,6.059882,3.107440,-7.618957,1.459365,5.537434,-8.389234,-7.876398,-6.274105,2.393776,2.568303,8.521945,7.325505],[-1.978887,-9.260686,-4.552690,-1.440642,5.795357,1.801792,1.657791,-8.914242,3.640269,9.362093,0.626355,5.823667,5.578201,-0.364865,-1.153206,9.409000]],[[-5.942927,-4.503278,-8.931689,-6.017558,-7.162506,9.226428,-5.437432,-4.419497,0.247360,0.271686,-7.361211,0.481664,6.502487,-8.774755,4.541788,0.181372],[-7.185742,-3.748024,-6.541378,-3.047632,2.183241,-2.736440,0.352347,0.676978,-3.537042,1.182395,3.363060,-8.913033,-6.834304,-2.104345,5.887808,0.207304],[7.351540,-0.127142,9.472366,-0.516429,-2.269101,-5.846437,-8.618750,-7.520146,1.131509,1.105987,2.312626,8.243377,-5.651527,7.041071,6.592731,8.239824],[1.432079,-3.819164,9.919498,1.583915,2.860091,5.805735,2.110661,-7.389118,-4.442581,-2.088004,-6.937260,9.578747,1.566199,-9.023911,-5.129400,-6.797217],[0.309489,-0.715557,5.679369,-3.251691,6.741737,-4.836993,-5.138044,9.232912,-4.205081,-6.584587,-4.778957,-2.315148,-1.597528,-3.483756,-4.021407,-0.623269],[-7.255869,-1.941299,-6.653169,-3.148592,6.215280,7.930309,-1.322658,-9.306325,-3.003230,0.119750,-1.459650,-5.034048,-4.724202,7.831688,0.013729,-6.441768],[-7.325859,-7.642318,1.714032,1.525374,2.252025,-8.593754,1.116237,5.442078,7.134664,-3.857355,-9.805564,0.587833,-8.113117,5.725669,-0.289984,4.521990],[2.081424,-1.826387,-9.563484,4.054200,-1.651747,9.874568,-4.722388,1.300910,8.645264,6.275822,-7.872170,-0.686581,-7.671781,9.596665,8.072650,9.260385],[-7.381310,-0.622797,2.735486,-4.279931,2.692673,-5.331419,-3.390869,-9.190711,0.609547,1.842978,-7.920373,-1.279632,-7.439339,0.916514,-3.176299,-3.252964]],[[-0.847297,-5.559045,-4.975787,7.755598,-7.378233,6.589686,6.149359,4.073069,3.178360,1.469632,-3.667894,-6.309923,0.368959,6.809742,9.948406,-0.212114],[-7.039257,6.560598,6.807936,-3.749451,-0.890590,6.762762,9.796286,9.211095,0.626432,-2.645235,-5.810904,-9.047626,3.760233,-0.588766,0.600919,-7.444901],[8.886947,-5.193844,7.435472,-5.400776,-5.765202,8.469599,-2.780818,2.096340,3.009057,-4.033017,-1.204684,3.406772,-6.948059,-2.649887,-3.980072,3.462488],[2.179198,4.901645,-0.438587,-5.909434,2.007490,5.008260,-5.804069,1.306949,-3.245363,-3.277049,5.360089,-2.426958,2.408308,2.017194,-1.524381,9.881055],[4.723473,-4.709406,-5.939611,-7.582460,-2.256880,-7.554240,-6.709068,7.494103,4.867665,-8.644062,5.549415,-7.437830,3.282361,7.789309,-1.062645,5.783143],[9.487968,0.772892,4.406330,6.287973,6.997470,-1.274223,1.116360,6.502574,2.347201,7.351545,-2.362622,8.121687,-8.823372,9.618280,7.863127,-5.239330],[-0.836771,9.124202,6.968458,-8.699850,-1.610386,8.685048,-8.801367,-9.249055,-3.791780,-7.795560,9.484240,-3.546906,-6.886513,-9.133369,8.093640,-7.727867],[-4.111681,2.769916,-5.910907,6.352600,-3.038908,2.666085,4.435423,8.943370,2.561009,-0.429685,6.840694,-2.409528,2.676801,-4.841131,6.916147,-4.075448],[-4.415770,-1.794040,3.766672,8.482746,-0.496532,-7.108266,-8.959747,5.679748,-6.942375,-9.240994,-9.608988,7.814300,9.291928,-4.344006,3.184029,-2.013595]],[[-2.576843,-6.545398,-5.882605,-6.263341,-6.654735,-3.794238,-1.936314,1.705852,-6.654414,-8.211054,-7.099305,-6.705117,8.701414,0.868583,3.203895,-1.946927],[-6.870920,-2.799134,-8.432188,0.707305,5.658801,1.514184,7.055761,-0.788099,-0.536651,-1.818634,9.933411,-0.635053,-6.919004,3.638930,-7.778657,0.580123],[-9.527583,7.821327,-9.247969,-5.781290,4.933938,7.074785,-6.491489,-0.754034,1.514799,5.710610,0.066841,2.182983,6.294173,1.031773,0.594924,-9.650328],[-7.477087,-9.152038,-6.227927,4.644525,8.786379,-1.457669,-7.240210,-5.066695,-6.733247,-7.433687,-1.542866,6.919340,-4.715974,7.167900,7.185520,-0.471121],[3.826019,6.886420,1.199854,8.228614,8.574413,-1.955680,-0.878850,0.539989,-3.384593,-4.766414,-5.624966,4.940806,0.486911,-5.238530,-3.852649,-1.426693],[4.380747,-2.274259,-3.288507,8.745968,3.945603,-4.120394,1.091031,-6.728946,4.329364,-8.066478,-6.982973,3.819157,-2.719034,0.325329,-4.725395,-1.970042],[6.972300,-9.183399,2.147892,2.451690,9.005443,-6.330550,-1.274871,-9.109582,-9.857196,2.844397,-5.490662,-7.676552,-5.377210,-9.978599,9.141327,-1.376349],[0.302601,5.124224,3.643921,0.135004,-6.036520,1.060604,5.647411,-1.109993,-4.388581,-3.603869,-8.916259,6.711994,-2.900104,7.051935,-7.366590,-2.668302],[-8.355083,-8.239230,1.538636,-9.799337,-2.154866,-5.423674,-1.654643,1.598739,-5.929806,2.845811,-4.339236,7.545492,-9.352070,-8.940601,-8.673232,-2.564831]],[[-1.705384,-7.330606,1.619999,3.825895,-2.718075,3.828108,5.150267,9.200580,-6.768953,-7.058351,3.727397,-0.252492,0.161793,8.572270,8.356009,-7.959202],[-3.202704,0.348141,-9.347006,5.661329,-7.053416,6.514962,7.915258,5.300549,5.243957,-0.016704,6.036466,2.005634,-4.638135,1.064469,-9.705410,6.748648],[-0.849718,-9.872881,-2.946167,-5.224019,-6.875842,-6.108607,-2.594025,-6.763570,0.210066,7.894088,8.907825,9.578328,5.311363,7.774001,6.945415,-0.452206],[-7.197479,-7.183739,3.668507,1.260494,-7.469893,1.127570,-1.708330,-5.845119,1.550479,-3.803208,-7.921146,-9.273383,-2.536864,-6.989822,-1.804671,-7.011521],[8.869502,3.530098,8.764510,7.002003,-8.518792,-1.025806,-3.444748,6.197028,-2.466667,-5.979444,0.838547,-3.627771,-8.490307,1.675438,-1.178759,0.510508],[-7.651587,-0.674346,-7.788552,7.854274,-6.960259,0.962138,8.280128,-2.273924,-1.666864,-2.257659,4.705852,-5.333618,9.124327,9.413488,4.208322,-4.398802],[2.535443,1.330696,-8.643504,9.483391,-5.386692,9.241604,1.939092,-2.139827,-3.091256,1.946423,5.010538,6.817800,-8.346733,-6.366332,-4.607127,2.408380],[1.642158,2.248809,-6.029134,4.960558,0.261551,-3.335980,-2.103755,-7.433515,3.166891,0.884334,2.517770,-7.019727,5.349691,3.965929,1.316348,6.432268],[0.127019,-4.095340,6.270514,2.175147,-8.151906,0.487290,-8.899634,3.738588,-1.679633,-7.030696,1.980657,4.909056,-3.779495,-8.920528,2.792731,-7.024510]],[[-5.376209,-6.375749,-6.663226,-3.545721,3.996872,-0.624934,-7.084218,-7.592155,-8.122359,-8.977082,1.044857,-7.436600,2.549548,4.103128,-4.856528,9.866704],[-2.742630,3.964150,2.249694,9.928164,4.885017,-8.755071,4.622356,-7.592629,-7.063734,7.581775,-9.189444,2.523813,2.593940,6.624562,-5.518720,-8.155880],[-0.861176,-0.196700,-1.176562,7.224114,5.311575,9.798371,-7.866000,-2.253738,-6.890380,-9.920192,8.412856,-9.271511,-8.059143,-1.340843,5.165153,8.048638],[-5.279512,0.373607,4.746620,4.579057,2.485469,4.778750,-0.891641,-8.855306,4.797480,-2.587406,-3.840707,2.545086,-8.387219,7.276746,2.252987,1.370789],[-7.283845,-0.266502,0.879686,-9.986156,-1.760587,-5.933932,6.332594,1.728139,9.719906,2.610461,0.228628,-4.844480,4.406154,8.774325,-0.728408,-9.264661],[8.950072,-8.131777,-7.538944,0.700872,-2.293812,-2.451551,-0.401763,3.729329,5.432691,3.173976,2.162082,-7.150177,-0.130845,1.991609,-3.941301,6.715383],[-6.745016,0.160862,6.451289,4.438115,-8.502019,6.591751,-9.581583,7.292739,-5.324963,-9.229387,-8.151158,-9.896167,-3.272616,-1.509824,1.291771,-3.878630],[4.341196,2.905898,9.988835,7.321220,-9.924972,-8.717489,1.286998,-8.252963,8.564956,2.049057,3.360136,-6.418159,-5.827328,-3.001697,-7.678523,4.239521],[-0.727416,-2.006175,-5.325441,-2.408969,2.251599,8.240417,-0.912217,-2.095095,-1.585722,9.364676,4.802985,6.383062,-2.248180,4.607728,-8.140681,3.890582]]], dtype = "float32")#candidate|5154|(10, 9, 16)|const|float32
uop_5155 = relay.acosh(const_5154.astype('float32')) # shape=(10, 9, 16)
uop_5161 = relay.sinh(uop_5155.astype('float32')) # shape=(10, 9, 16)
output = relay.Tuple([uop_5161,])
output2 = relay.Tuple([uop_5161,])
func_5176 = relay.Function([], output)
mod['func_5176'] = func_5176
mod = relay.transform.InferType()(mod)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5176_call = mutated_mod.get_global_var('func_5176')
call_5177 = func_5176_call()
output = call_5177
func_5178 = relay.Function([], output)
mutated_mod['func_5178'] = func_5178
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5213 = relay.var("var_5213", dtype = "float64", shape = (10, 13, 7))#candidate|5213|(10, 13, 7)|var|float64
uop_5214 = relay.log2(var_5213.astype('float64')) # shape=(10, 13, 7)
func_2361_call = mod.get_global_var('func_2361')
func_2364_call = mutated_mod.get_global_var('func_2364')
var_5222 = relay.var("var_5222", dtype = "int16", shape = (33, 6))#candidate|5222|(33, 6)|var|int16
call_5221 = func_2361_call(relay.reshape(var_5222.astype('int16'), [2, 9, 11]), relay.reshape(var_5222.astype('int16'), [2, 9, 11]), )
call_5223 = func_2361_call(relay.reshape(var_5222.astype('int16'), [2, 9, 11]), relay.reshape(var_5222.astype('int16'), [2, 9, 11]), )
var_5227 = relay.var("var_5227", dtype = "float64", shape = (10, 13, 7))#candidate|5227|(10, 13, 7)|var|float64
bop_5228 = relay.less(uop_5214.astype('bool'), relay.reshape(var_5227.astype('bool'), relay.shape_of(uop_5214))) # shape=(10, 13, 7)
func_4298_call = mod.get_global_var('func_4298')
func_4301_call = mutated_mod.get_global_var('func_4301')
const_5253 = relay.const([[-6.640754,-2.957535,3.010389,-8.695338,8.347297,1.817941,-7.825496,4.188240,8.678936,9.214335,6.922648,-1.953432,-3.172080,-8.884594,-2.115525,9.931246,2.059361,-8.594857,-8.298297,1.235497,7.290466,-9.872686,7.059293,5.086862,1.857323,3.773063,2.287424,0.699666,9.484282,0.368795,7.169252,-9.398818,-7.842787,-6.331642,3.616948,-2.214868,-2.395817,-8.392258,-5.435745,1.550083,-5.848316,-0.954054,-6.095393,0.789871,-1.570896,3.269243,5.365129,-0.371745,9.142695,-2.874065,0.516823,8.839048,-1.645258,9.276106,-6.089802,-5.357863,1.706474,-2.786634,-6.621776,4.008223,-8.613708,8.812155,-0.700511,7.714545,-5.549455,-0.305805,-0.983749,7.117660,2.251905,-3.586689,7.124698,1.667999,0.721864,-8.870900,3.578925,-8.821602,5.715761,-0.520619,-5.871077,0.257274],[3.043056,-6.566261,9.244702,-3.916442,-8.508267,-5.100458,-5.304375,4.862218,-0.316594,5.346645,9.590449,5.386724,7.171047,6.369851,-8.413034,-6.801345,-6.835345,9.222924,3.082378,8.991146,-1.205999,0.005988,1.733173,2.424103,1.819398,4.982881,-3.503656,9.562498,-6.236484,3.170338,4.080803,9.650750,-2.649988,0.282103,-5.284742,-9.359883,0.195092,9.320464,-9.161425,-9.419021,-5.072166,-0.239296,-9.177850,-4.643105,-4.725663,4.510882,-6.646611,-5.366765,-0.253829,-4.101796,-6.044934,8.899469,-8.434177,-8.976892,2.775664,-4.431234,-4.539848,3.551725,-8.256370,-4.688920,5.956036,-0.615796,-9.019878,5.094764,7.458580,6.542218,-1.522004,0.313200,-1.350341,0.060398,-8.038270,5.956301,-1.442487,7.325518,-3.218205,-1.869336,-7.483742,6.495630,3.707306,5.164782],[-0.644624,-2.349979,5.080021,-4.094592,3.927977,-6.848979,6.350954,-5.443717,-7.303027,0.968528,4.736408,-0.874289,-6.303870,-6.477751,-7.788076,-3.487036,1.608527,4.669857,-8.785616,-4.843119,7.046150,2.390914,-4.592661,2.958789,-9.921633,5.362265,-3.605047,2.041235,-2.865446,-6.409254,7.042891,6.754004,1.685811,0.557927,-7.847705,4.767188,-5.097442,5.632814,-9.814387,2.160822,6.717465,0.053796,5.824258,-3.631236,-6.690179,-2.630063,-6.030820,-3.047210,0.703609,2.920223,4.328280,4.822980,-8.915449,-3.611773,8.444264,9.656804,6.346551,-4.310766,2.999449,-2.722216,7.669643,7.223855,-0.491977,0.241819,9.883830,-5.273990,7.574152,9.289376,-2.382261,9.478759,5.020788,-7.581158,1.778161,1.093971,6.534100,-6.381552,9.837131,-1.163028,-4.615786,8.410199],[5.720750,-8.145184,8.054598,-7.716898,-8.895313,-2.147773,-6.738949,-3.430926,0.803419,-3.569102,9.752614,-0.743282,-8.414321,-7.906962,-0.871499,-4.668736,9.607271,6.136715,-7.661122,-7.062288,7.721394,1.633009,6.123804,2.483857,7.542548,-0.380426,-3.797274,8.392493,1.062319,9.616772,2.422810,4.776636,3.962117,-3.961757,-4.007317,-7.593682,4.995790,6.677643,1.329063,9.016178,-4.768971,4.768703,-8.493916,5.224064,-3.812636,-5.906929,3.858022,0.406498,-8.660805,-1.167289,-4.664354,-0.759555,-0.552276,2.532755,-9.630494,0.721296,-9.997738,8.377856,8.982562,-2.183374,-8.433308,-3.584754,7.107488,-4.522517,4.332673,-7.650657,7.597629,6.870250,5.890336,1.678698,7.718482,-1.122409,9.069460,0.967699,6.580329,-0.165446,-8.297122,1.475250,-2.375798,0.723513],[-0.304078,-8.970675,-9.996485,-1.787694,-7.281194,4.385583,-2.875381,6.246215,9.718026,-0.670017,-5.039616,-8.012371,4.847985,-4.486523,8.994153,6.823885,-1.286675,2.240435,6.837032,-2.625247,4.687168,-5.173065,7.866785,5.869810,-8.177071,9.648653,7.198062,7.397460,0.177484,-9.208963,4.486064,2.977896,2.744134,-1.441571,-8.649636,-9.283467,-4.852629,4.126535,-4.996810,-5.339813,-8.536229,-2.922299,-5.856462,1.858457,5.074808,-8.596578,4.155254,-3.684589,2.114553,-3.750242,0.292750,1.924389,5.819465,-4.922594,-4.096257,-1.742305,-7.176023,-0.088463,-6.048266,5.929150,6.722567,-1.552014,2.047455,-6.287030,7.120739,-9.051106,2.801317,-2.012288,-2.412056,4.806663,6.461075,5.741038,-6.028369,-0.491351,7.743646,-3.994910,-2.598476,-0.602746,-1.761212,-4.347944],[0.947333,-7.991502,-1.586877,1.861283,2.304724,6.706992,-2.360887,2.332813,-0.610586,8.145343,6.040946,7.216287,-5.366188,0.191923,-3.860445,-9.285961,-8.146848,-4.037464,2.969513,1.057375,-4.801645,6.447834,9.753084,2.919481,3.749258,-8.837529,4.755715,-8.806546,7.392662,-2.509873,3.524346,7.828431,4.311281,-6.350656,4.425892,-0.066342,8.605812,-1.448424,-2.212591,-9.795072,-6.462338,-1.957008,-3.305972,4.020878,-0.650115,1.539515,-1.913596,0.267180,6.489244,-7.579353,8.750961,-3.413819,-4.253266,3.026269,8.864032,-0.256280,-7.392777,6.534187,7.937251,-3.477098,-4.003784,6.970620,-2.885141,-3.271905,0.216745,-8.225876,0.142164,2.791572,8.857133,-5.277095,-6.288268,-8.598708,2.938349,-6.400606,-0.399343,-4.765012,-8.145619,3.470834,-1.536367,-4.765378],[-8.170156,-1.768418,-9.608541,-8.098917,2.821043,-3.998405,6.064342,-7.771115,-1.221191,-6.922553,-4.381969,1.441796,-7.966822,4.738865,-6.678278,-5.268191,5.936363,6.049617,-8.870575,9.585214,-3.005003,-1.115770,6.782273,3.073400,5.432373,-8.342101,-0.653215,-1.078283,8.826724,-1.502360,-3.707384,-5.876940,0.919446,7.976132,9.910145,6.832383,-8.659244,-3.367248,1.272447,8.350564,9.244056,-0.451536,6.834197,-1.347194,-2.936525,-3.278893,-8.021309,-5.556382,-9.660975,3.671757,7.049009,-2.438298,-1.641609,9.516166,-7.580374,-2.107360,-5.035741,1.439423,-6.040998,-9.666290,-0.979700,4.436133,-1.152046,7.915085,3.468404,-1.202389,9.926026,-3.535444,6.309124,6.929442,-3.470117,7.337528,-2.428139,-6.707546,8.435457,-2.809008,3.335709,-6.145327,2.016436,1.187471],[-8.222254,0.749922,-3.302336,-7.028206,1.965566,4.260637,7.125216,7.149555,4.563383,-5.441446,-7.118970,5.467515,-8.853791,9.081921,8.714580,-8.430055,1.532239,5.157947,2.802915,4.112864,-0.884687,-5.323741,-6.910491,6.427399,9.151389,-9.821521,-6.982428,-1.838766,1.600262,0.203577,-8.576373,-1.796679,9.819922,0.924919,9.032944,-7.570755,1.172398,-6.160833,-1.484120,6.807517,6.503442,9.522345,5.433796,1.826324,-2.094878,1.211871,-3.215592,-9.673730,-4.623956,2.937842,-6.051954,4.313556,-5.827843,7.381285,0.926791,7.232140,-3.359536,1.335794,-4.024852,-6.898870,1.568214,9.923531,-6.149462,9.875062,4.910906,-2.360135,-2.301682,3.898754,5.283740,2.355689,5.946708,-8.375993,-7.072756,-2.254922,-8.110139,1.938779,-3.264085,4.500255,-8.061879,9.753509],[4.601101,6.619347,6.981262,0.051810,-9.074744,-0.840008,8.939923,9.319502,-9.729711,-4.243928,1.954022,-5.054769,-0.951452,-8.102183,-6.241803,-1.172414,5.822202,-1.881828,-9.261432,-3.116585,-4.226582,-8.470495,0.217709,7.709881,0.164355,-4.246411,3.532196,2.351093,-3.472769,-8.579000,4.378381,0.185148,1.810756,-8.309119,4.936855,-2.804950,6.044695,4.092903,-3.173603,-0.453495,-7.080550,-0.153154,3.016279,3.500515,0.512320,-8.215749,-7.205812,-6.240780,9.276123,1.217908,4.996745,5.599907,-9.561345,5.676406,2.836820,7.398430,-1.417999,-1.801187,2.325006,6.563621,3.058596,5.313482,3.302261,8.856286,-3.286854,8.542672,-5.487839,-3.242987,2.858496,-2.983066,5.093865,-5.398677,2.124469,8.787527,-3.757493,-4.789432,6.901160,3.158694,0.682044,3.171466],[6.982310,0.002822,3.196337,5.766270,0.140209,-7.792658,2.512495,-9.946435,5.264206,1.483326,-2.615719,4.186141,2.022759,9.511789,-7.148908,9.085251,9.717920,0.386774,-3.718806,-1.906445,-6.345291,7.491843,6.662080,2.180891,8.112442,2.649745,-4.436551,1.156428,5.992836,-5.602405,-7.736937,-5.961437,-0.005615,-9.387354,-5.107931,-7.344543,4.161694,-5.829192,4.506643,4.703776,-6.158760,-9.765291,-0.394094,-9.477959,-6.866112,8.945337,-9.777949,5.347921,0.113336,-0.062292,-0.372817,0.502001,-5.410079,-9.223092,6.604019,-6.059436,-0.707503,-7.958191,9.740133,5.644133,5.375162,-6.929866,-0.841546,-9.038029,3.996713,4.566037,0.045544,-1.845697,-2.773860,0.540831,-7.813882,8.712802,-9.536739,9.940689,-6.822470,-5.262675,0.436374,-1.399411,-2.260065,-1.823633],[6.693584,5.211222,-2.759486,-1.022581,-7.766555,-7.739077,8.153275,-9.948828,7.418065,6.171854,-7.552387,5.054802,-0.653217,2.579440,-4.357683,5.998624,4.634585,-1.075464,-8.585900,-8.630281,-9.802401,2.810257,-4.583693,0.785501,-6.731035,3.335903,-4.493748,-1.659285,-6.434521,3.044050,2.412485,-8.473622,8.449747,-4.170519,3.465645,8.817505,6.855302,-7.902441,-5.077428,2.194169,-3.690024,1.037225,1.205839,-2.219445,5.332800,-6.324322,-5.744784,1.101955,6.281084,8.504284,-6.274507,-6.259489,2.104751,2.277669,7.235380,-7.411009,0.560939,-4.234780,-9.567843,8.175712,8.655074,-7.533907,-7.765854,7.567360,-9.072607,0.690257,1.538712,-3.402569,-2.952206,-8.228274,8.599533,9.818315,-2.399168,1.267522,-6.966303,-6.484360,9.791981,0.181229,-3.190422,1.454081],[7.555853,8.111362,3.775055,-2.446181,7.516267,6.154827,8.045345,-4.645979,-8.990090,-6.477532,-5.721919,-0.470456,-7.467327,7.639981,9.112146,3.942096,5.520315,6.784979,-6.256667,-9.893793,1.152842,-2.402829,4.103320,-0.251137,0.683863,-3.648813,-2.005109,8.881314,5.459821,8.406569,1.096075,2.459564,-2.427933,1.106867,-4.005913,-1.862148,3.069982,4.588406,4.365148,9.977812,-0.285432,-5.420325,-4.988505,8.657996,5.707826,-2.202318,2.640478,5.045982,8.129906,4.430996,1.790535,5.485135,-6.101824,8.017175,-8.262776,-4.028503,-4.864625,2.320143,-0.475940,-0.155950,-9.084146,5.320928,3.557855,8.422274,5.913916,-2.014820,-1.457181,-1.482669,-2.422575,1.245714,-6.920811,-6.086632,-4.133273,3.356107,-0.309295,-5.436361,8.833022,0.038711,8.657059,9.015819],[3.004497,4.801164,1.810878,-4.923989,5.700747,-0.550603,-0.115842,-4.564748,2.016890,1.288099,-5.886723,-3.295987,1.864150,-3.252706,-7.871634,-0.379417,0.824439,4.061864,2.179793,2.476504,2.176677,-8.652853,-2.512271,6.497246,-7.921406,0.906876,-3.199022,-3.448365,2.189371,-9.376447,-4.804722,8.686728,-8.674540,-1.748628,2.901721,-3.950731,-1.424260,-4.351813,-2.400791,-8.209115,-0.001743,6.395409,7.537195,5.512467,-9.631096,-7.598068,-2.864280,-8.496905,-2.160617,-3.059718,-2.101751,1.429958,7.926245,2.047305,8.531603,-0.571489,-6.529419,-8.646041,-4.262266,-3.173709,-5.972081,4.369662,7.190533,7.390358,2.997906,2.408706,6.281436,-8.435713,-9.203788,-4.218374,0.155315,6.560336,-8.051994,2.307644,0.226135,0.885554,-7.781763,-9.773116,-0.784531,5.043752],[9.958512,-6.549507,6.205831,3.308058,-6.991642,8.475433,9.344371,7.272493,1.226166,-2.066494,7.613594,-5.219559,-7.071259,2.821351,-5.763989,-7.260368,1.761097,-1.119341,0.325256,-3.973944,8.834425,5.008906,-8.171823,-6.301956,0.035830,1.164902,-7.580703,-1.720361,-4.392716,-8.362250,8.765036,4.387898,2.869542,9.656989,4.360662,-7.386362,-6.314221,8.127472,3.369093,-8.228762,-2.221937,8.757657,2.080761,-5.183307,8.339947,-7.317940,0.005843,7.366510,-6.536008,-5.417417,-5.408480,-0.228216,-5.727737,4.792881,-7.561085,9.089524,5.848019,4.342057,-1.372621,9.597660,-1.134635,-8.297801,4.028778,-4.189299,3.344073,8.124928,-5.911867,-5.784403,-2.154427,-2.364740,0.807105,3.113652,-2.592565,0.884572,-9.690126,-0.538040,-4.080915,3.838530,-4.573851,5.205287],[-5.015425,7.368473,4.281136,2.601762,6.357423,-6.260594,6.980314,-8.789607,-9.733830,6.926085,-7.474791,-6.521659,-5.914795,-2.567466,3.831631,-8.954170,-9.795210,-1.314973,1.152077,3.235984,2.734321,4.488292,-2.450803,-2.252493,6.792103,2.178531,4.377621,8.383693,4.303496,-3.550059,6.146264,-0.548531,-9.649092,9.852757,3.631043,9.816250,-0.861264,2.474570,-8.959638,-2.596453,7.931281,6.620131,3.378817,0.940136,-4.857621,7.864071,-6.738179,4.702971,1.271564,4.189262,-9.412332,2.785480,7.956412,1.827745,7.236293,-4.700344,5.050074,5.837296,-4.922147,-8.406370,5.536574,-7.546092,1.183275,-4.831092,8.568449,4.177801,-1.541474,-4.673880,-5.785224,5.974411,3.242232,-7.740043,3.655321,6.782090,-7.049743,-8.850240,-1.878283,-6.281238,3.220309,-7.278012],[-9.619862,-0.545468,-5.902558,-5.204085,-4.423371,-5.575602,9.583044,-6.873614,1.891800,-5.155958,6.717688,9.120601,-0.431633,-9.941579,-2.808867,-5.011087,-9.075897,-7.252197,5.890138,1.547682,-5.484471,-5.967170,7.106711,8.659707,-0.516124,-0.249253,-0.691188,7.162005,4.319475,-9.716419,-3.850505,-6.524926,7.357483,-6.577903,-3.202251,-3.804218,8.282210,-4.195130,-4.276522,7.254066,-7.830870,-5.819193,3.712362,7.179289,3.986255,6.014511,-5.041281,3.498856,-6.660316,-3.049780,6.024351,9.357541,4.294781,3.492034,1.455152,3.696588,1.182318,1.864119,7.314291,1.731009,-8.135146,3.067759,6.389042,5.931896,-3.157149,-6.944597,-4.992181,-6.261125,6.302476,3.831469,3.809846,-7.951003,2.340460,8.428811,-3.168752,1.881017,0.328381,3.302360,9.801781,-8.456663]], dtype = "float32")#candidate|5253|(16, 80)|const|float32
const_5254 = relay.const([1.395857,8.162249,-6.279640,7.234414,2.892310,-6.354952,4.562788,-4.376450,8.871714,4.028569,-6.953076,6.014439,2.756110,3.814256,-1.009961,-8.373708,-8.922855,-5.499127,2.208778,-7.163569,-9.826002,4.955351,2.325250,8.271399,1.836334,8.280362,-0.158306,-4.121559,9.766870,-2.891430,6.313257,5.356730,-2.701622,-1.534602,7.289007,2.029885,-7.234676,-4.434948,-9.957321,-2.655674,-3.074627,5.417344,-4.132443,-9.588657,0.562326,5.004089,5.338015,-6.602398,-6.028205,7.162898,-9.973871,7.301232,1.932762,-3.252606,-7.808863,-7.650403,-1.068691,2.305963,6.304755,-1.506819,-8.058854,7.555212,-7.162030,4.305376], dtype = "float32")#candidate|5254|(64,)|const|float32
call_5252 = relay.TupleGetItem(func_4298_call(relay.reshape(const_5253.astype('float32'), [16, 5, 16]), relay.reshape(const_5254.astype('float32'), [2, 32]), ), 2)
call_5255 = relay.TupleGetItem(func_4301_call(relay.reshape(const_5253.astype('float32'), [16, 5, 16]), relay.reshape(const_5254.astype('float32'), [2, 32]), ), 2)
func_899_call = mod.get_global_var('func_899')
func_902_call = mutated_mod.get_global_var('func_902')
var_5259 = relay.var("var_5259", dtype = "int8", shape = (728,))#candidate|5259|(728,)|var|int8
call_5258 = func_899_call(relay.reshape(var_5259.astype('int8'), [14, 4, 13]), relay.reshape(var_5259.astype('int8'), [14, 4, 13]), )
call_5260 = func_899_call(relay.reshape(var_5259.astype('int8'), [14, 4, 13]), relay.reshape(var_5259.astype('int8'), [14, 4, 13]), )
output = relay.Tuple([call_5221,var_5222,bop_5228,call_5252,const_5253,const_5254,call_5258,var_5259,])
output2 = relay.Tuple([call_5223,var_5222,bop_5228,call_5255,const_5253,const_5254,call_5260,var_5259,])
func_5272 = relay.Function([var_5213,var_5222,var_5227,var_5259,], output)
mod['func_5272'] = func_5272
mod = relay.transform.InferType()(mod)
var_5273 = relay.var("var_5273", dtype = "float64", shape = (10, 13, 7))#candidate|5273|(10, 13, 7)|var|float64
var_5274 = relay.var("var_5274", dtype = "int16", shape = (33, 6))#candidate|5274|(33, 6)|var|int16
var_5275 = relay.var("var_5275", dtype = "float64", shape = (10, 13, 7))#candidate|5275|(10, 13, 7)|var|float64
var_5276 = relay.var("var_5276", dtype = "int8", shape = (728,))#candidate|5276|(728,)|var|int8
output = func_5272(var_5273,var_5274,var_5275,var_5276,)
func_5277 = relay.Function([var_5273,var_5274,var_5275,var_5276,], output)
mutated_mod['func_5277'] = func_5277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4983_call = mod.get_global_var('func_4983')
func_4985_call = mutated_mod.get_global_var('func_4985')
call_5287 = relay.TupleGetItem(func_4983_call(), 0)
call_5288 = relay.TupleGetItem(func_4985_call(), 0)
output = call_5287
output2 = call_5288
func_5293 = relay.Function([], output)
mod['func_5293'] = func_5293
mod = relay.transform.InferType()(mod)
output = func_5293()
func_5294 = relay.Function([], output)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_5330 = relay.TupleGetItem(func_4699_call(), 0)
call_5331 = relay.TupleGetItem(func_4701_call(), 0)
uop_5339 = relay.asinh(call_5330.astype('float32')) # shape=(1, 28)
uop_5341 = relay.asinh(call_5331.astype('float32')) # shape=(1, 28)
output = uop_5339
output2 = uop_5341
func_5342 = relay.Function([], output)
mod['func_5342'] = func_5342
mod = relay.transform.InferType()(mod)
mutated_mod['func_5342'] = func_5342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5342_call = mutated_mod.get_global_var('func_5342')
call_5343 = func_5342_call()
output = call_5343
func_5344 = relay.Function([], output)
mutated_mod['func_5344'] = func_5344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4606_call = mod.get_global_var('func_4606')
func_4608_call = mutated_mod.get_global_var('func_4608')
call_5376 = relay.TupleGetItem(func_4606_call(), 1)
call_5377 = relay.TupleGetItem(func_4608_call(), 1)
output = call_5376
output2 = call_5377
func_5381 = relay.Function([], output)
mod['func_5381'] = func_5381
mod = relay.transform.InferType()(mod)
output = func_5381()
func_5382 = relay.Function([], output)
mutated_mod['func_5382'] = func_5382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4606_call = mod.get_global_var('func_4606')
func_4608_call = mutated_mod.get_global_var('func_4608')
call_5388 = relay.TupleGetItem(func_4606_call(), 2)
call_5389 = relay.TupleGetItem(func_4608_call(), 2)
func_874_call = mod.get_global_var('func_874')
func_878_call = mutated_mod.get_global_var('func_878')
const_5397 = relay.const([True,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,True,False,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,False,False,False,True,False,False,False,True,False,True,False,True,False,False,False,False,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,True,False,True], dtype = "bool")#candidate|5397|(780,)|const|bool
call_5396 = relay.TupleGetItem(func_874_call(relay.reshape(const_5397.astype('bool'), [13, 6, 10]), relay.reshape(const_5397.astype('bool'), [13, 6, 10]), ), 0)
call_5398 = relay.TupleGetItem(func_878_call(relay.reshape(const_5397.astype('bool'), [13, 6, 10]), relay.reshape(const_5397.astype('bool'), [13, 6, 10]), ), 0)
func_2604_call = mod.get_global_var('func_2604')
func_2607_call = mutated_mod.get_global_var('func_2607')
const_5400 = relay.const(8.126920, dtype = "float32")#candidate|5400|()|const|float32
const_5401 = relay.const([[2.781230],[-9.336350],[-9.505588],[-1.320358],[4.161789],[5.342491],[7.724332],[-7.639127],[-0.682058],[-0.323758],[-1.909774],[2.869655],[-9.429215],[-4.869314],[7.810027],[2.917766],[5.889285],[5.253745],[-3.755021],[-0.955949],[8.451859],[2.155052],[4.400131],[-2.915892],[-2.654329],[-4.796558],[-6.551769],[-4.516985]], dtype = "float32")#candidate|5401|(28, 1)|const|float32
call_5399 = relay.TupleGetItem(func_2604_call(relay.reshape(const_5400.astype('float32'), []), relay.reshape(const_5401.astype('float32'), [28,]), ), 3)
call_5402 = relay.TupleGetItem(func_2607_call(relay.reshape(const_5400.astype('float32'), []), relay.reshape(const_5401.astype('float32'), [28,]), ), 3)
output = relay.Tuple([call_5388,call_5396,const_5397,call_5399,const_5400,const_5401,])
output2 = relay.Tuple([call_5389,call_5398,const_5397,call_5402,const_5400,const_5401,])
func_5409 = relay.Function([], output)
mod['func_5409'] = func_5409
mod = relay.transform.InferType()(mod)
output = func_5409()
func_5410 = relay.Function([], output)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_5443 = relay.TupleGetItem(func_4882_call(), 0)
call_5444 = relay.TupleGetItem(func_4884_call(), 0)
func_3651_call = mod.get_global_var('func_3651')
func_3653_call = mutated_mod.get_global_var('func_3653')
var_5451 = relay.var("var_5451", dtype = "int8", shape = ())#candidate|5451|()|var|int8
call_5450 = relay.TupleGetItem(func_3651_call(relay.reshape(var_5451.astype('int8'), [])), 1)
call_5452 = relay.TupleGetItem(func_3653_call(relay.reshape(var_5451.astype('int8'), [])), 1)
func_4472_call = mod.get_global_var('func_4472')
func_4476_call = mutated_mod.get_global_var('func_4476')
const_5467 = relay.const([5,-8,10,-10,-2,-9,6,-2,-9,2,3,9,-6,7,9,1,-3,-6,-8,-1,-3,-1,-10,-9,-2,-3,8,9,8,2,-9,1,4,4,-6,-2,5,-7,6,4,-7,-5,8,9,-9,5,-5,-1,-4,1,-9,-10,-8,-1], dtype = "int16")#candidate|5467|(54,)|const|int16
var_5468 = relay.var("var_5468", dtype = "float64", shape = (195, 3))#candidate|5468|(195, 3)|var|float64
var_5469 = relay.var("var_5469", dtype = "int16", shape = (450,))#candidate|5469|(450,)|var|int16
call_5466 = relay.TupleGetItem(func_4472_call(relay.reshape(const_5467.astype('int16'), [3, 9, 2]), relay.reshape(var_5468.astype('float64'), [585,]), relay.reshape(var_5469.astype('int16'), [450,]), ), 3)
call_5470 = relay.TupleGetItem(func_4476_call(relay.reshape(const_5467.astype('int16'), [3, 9, 2]), relay.reshape(var_5468.astype('float64'), [585,]), relay.reshape(var_5469.astype('int16'), [450,]), ), 3)
output = relay.Tuple([call_5443,call_5450,var_5451,call_5466,const_5467,var_5468,var_5469,])
output2 = relay.Tuple([call_5444,call_5452,var_5451,call_5470,const_5467,var_5468,var_5469,])
func_5471 = relay.Function([var_5451,var_5468,var_5469,], output)
mod['func_5471'] = func_5471
mod = relay.transform.InferType()(mod)
var_5472 = relay.var("var_5472", dtype = "int8", shape = ())#candidate|5472|()|var|int8
var_5473 = relay.var("var_5473", dtype = "float64", shape = (195, 3))#candidate|5473|(195, 3)|var|float64
var_5474 = relay.var("var_5474", dtype = "int16", shape = (450,))#candidate|5474|(450,)|var|int16
output = func_5471(var_5472,var_5473,var_5474,)
func_5475 = relay.Function([var_5472,var_5473,var_5474,], output)
mutated_mod['func_5475'] = func_5475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5495 = relay.var("var_5495", dtype = "float64", shape = (9, 8))#candidate|5495|(9, 8)|var|float64
var_5496 = relay.var("var_5496", dtype = "float64", shape = (9, 8))#candidate|5496|(9, 8)|var|float64
bop_5497 = relay.floor_mod(var_5495.astype('float64'), relay.reshape(var_5496.astype('float64'), relay.shape_of(var_5495))) # shape=(9, 8)
output = relay.Tuple([bop_5497,])
output2 = relay.Tuple([bop_5497,])
func_5503 = relay.Function([var_5495,var_5496,], output)
mod['func_5503'] = func_5503
mod = relay.transform.InferType()(mod)
var_5504 = relay.var("var_5504", dtype = "float64", shape = (9, 8))#candidate|5504|(9, 8)|var|float64
var_5505 = relay.var("var_5505", dtype = "float64", shape = (9, 8))#candidate|5505|(9, 8)|var|float64
output = func_5503(var_5504,var_5505,)
func_5506 = relay.Function([var_5504,var_5505,], output)
mutated_mod['func_5506'] = func_5506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_5564 = relay.TupleGetItem(func_4699_call(), 0)
call_5565 = relay.TupleGetItem(func_4701_call(), 0)
output = call_5564
output2 = call_5565
func_5594 = relay.Function([], output)
mod['func_5594'] = func_5594
mod = relay.transform.InferType()(mod)
output = func_5594()
func_5595 = relay.Function([], output)
mutated_mod['func_5595'] = func_5595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4606_call = mod.get_global_var('func_4606')
func_4608_call = mutated_mod.get_global_var('func_4608')
call_5598 = relay.TupleGetItem(func_4606_call(), 1)
call_5599 = relay.TupleGetItem(func_4608_call(), 1)
func_3651_call = mod.get_global_var('func_3651')
func_3653_call = mutated_mod.get_global_var('func_3653')
const_5609 = relay.const(-10, dtype = "int8")#candidate|5609|()|const|int8
call_5608 = relay.TupleGetItem(func_3651_call(relay.reshape(const_5609.astype('int8'), [])), 1)
call_5610 = relay.TupleGetItem(func_3653_call(relay.reshape(const_5609.astype('int8'), [])), 1)
bop_5611 = relay.logical_xor(call_5608.astype('int16'), const_5609.astype('int16')) # shape=(13, 6, 1)
bop_5614 = relay.logical_xor(call_5610.astype('int16'), const_5609.astype('int16')) # shape=(13, 6, 1)
bop_5632 = relay.add(bop_5611.astype('int64'), const_5609.astype('int64')) # shape=(13, 6, 1)
bop_5635 = relay.add(bop_5614.astype('int64'), const_5609.astype('int64')) # shape=(13, 6, 1)
output = relay.Tuple([call_5598,bop_5632,])
output2 = relay.Tuple([call_5599,bop_5635,])
func_5636 = relay.Function([], output)
mod['func_5636'] = func_5636
mod = relay.transform.InferType()(mod)
mutated_mod['func_5636'] = func_5636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5636_call = mutated_mod.get_global_var('func_5636')
call_5637 = func_5636_call()
output = call_5637
func_5638 = relay.Function([], output)
mutated_mod['func_5638'] = func_5638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_5661 = relay.TupleGetItem(func_4882_call(), 0)
call_5662 = relay.TupleGetItem(func_4884_call(), 0)
func_1492_call = mod.get_global_var('func_1492')
func_1494_call = mutated_mod.get_global_var('func_1494')
var_5674 = relay.var("var_5674", dtype = "float64", shape = (126,))#candidate|5674|(126,)|var|float64
call_5673 = func_1492_call(relay.reshape(var_5674.astype('float64'), [6, 3, 7]))
call_5675 = func_1492_call(relay.reshape(var_5674.astype('float64'), [6, 3, 7]))
func_2054_call = mod.get_global_var('func_2054')
func_2057_call = mutated_mod.get_global_var('func_2057')
const_5685 = relay.const([[2,2,-2,6,-3,-6,10,5,2,9,-6,-1,-8,2,6,10,8,2,9,5,-2,-10,8,-2,-3,-8,-9,-9,-3,4,5,-7,-6,-2,-5,-8,-7,9,-6,-4,1,7,4,8,-5,7,6,4,1,8,-2,-2,5,-6]], dtype = "int8")#candidate|5685|(1, 54)|const|int8
var_5686 = relay.var("var_5686", dtype = "int16", shape = (450,))#candidate|5686|(450,)|var|int16
call_5684 = relay.TupleGetItem(func_2054_call(relay.reshape(const_5685.astype('int8'), [6, 1, 9]), relay.reshape(var_5686.astype('int16'), [450, 1]), ), 1)
call_5687 = relay.TupleGetItem(func_2057_call(relay.reshape(const_5685.astype('int8'), [6, 1, 9]), relay.reshape(var_5686.astype('int16'), [450, 1]), ), 1)
uop_5699 = relay.asin(var_5674.astype('float32')) # shape=(126,)
uop_5704 = relay.atan(const_5685.astype('float64')) # shape=(1, 54)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_5712 = relay.TupleGetItem(func_4882_call(), 0)
call_5713 = relay.TupleGetItem(func_4884_call(), 0)
output = relay.Tuple([call_5661,call_5673,call_5684,var_5686,uop_5699,uop_5704,call_5712,])
output2 = relay.Tuple([call_5662,call_5675,call_5687,var_5686,uop_5699,uop_5704,call_5713,])
func_5714 = relay.Function([var_5674,var_5686,], output)
mod['func_5714'] = func_5714
mod = relay.transform.InferType()(mod)
mutated_mod['func_5714'] = func_5714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5714_call = mutated_mod.get_global_var('func_5714')
var_5716 = relay.var("var_5716", dtype = "float64", shape = (126,))#candidate|5716|(126,)|var|float64
var_5717 = relay.var("var_5717", dtype = "int16", shape = (450,))#candidate|5717|(450,)|var|int16
call_5715 = func_5714_call(var_5716,var_5717,)
output = call_5715
func_5718 = relay.Function([var_5716,var_5717,], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4606_call = mod.get_global_var('func_4606')
func_4608_call = mutated_mod.get_global_var('func_4608')
call_5744 = relay.TupleGetItem(func_4606_call(), 1)
call_5745 = relay.TupleGetItem(func_4608_call(), 1)
output = call_5744
output2 = call_5745
func_5759 = relay.Function([], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
mutated_mod['func_5759'] = func_5759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5759_call = mutated_mod.get_global_var('func_5759')
call_5760 = func_5759_call()
output = call_5760
func_5761 = relay.Function([], output)
mutated_mod['func_5761'] = func_5761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5759_call = mod.get_global_var('func_5759')
func_5761_call = mutated_mod.get_global_var('func_5761')
call_5775 = func_5759_call()
call_5776 = func_5759_call()
output = call_5775
output2 = call_5776
func_5783 = relay.Function([], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
output = func_5783()
func_5784 = relay.Function([], output)
mutated_mod['func_5784'] = func_5784
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mod.get_global_var('func_5783')
func_5784_call = mutated_mod.get_global_var('func_5784')
call_5793 = func_5783_call()
call_5794 = func_5783_call()
output = call_5793
output2 = call_5794
func_5801 = relay.Function([], output)
mod['func_5801'] = func_5801
mod = relay.transform.InferType()(mod)
output = func_5801()
func_5802 = relay.Function([], output)
mutated_mod['func_5802'] = func_5802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_5821 = relay.TupleGetItem(func_4882_call(), 0)
call_5822 = relay.TupleGetItem(func_4884_call(), 0)
func_5342_call = mod.get_global_var('func_5342')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_5825 = func_5342_call()
call_5826 = func_5342_call()
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_5836 = relay.TupleGetItem(func_4527_call(), 1)
call_5837 = relay.TupleGetItem(func_4528_call(), 1)
func_5060_call = mod.get_global_var('func_5060')
func_5062_call = mutated_mod.get_global_var('func_5062')
const_5853 = relay.const([-1.661952,-8.999584,9.446196,8.284782,-7.363257,1.348290,-1.954769,-0.636452,6.201996,3.512126,-1.683841,-0.560897,-7.021682,7.028817,0.198678,-6.474910], dtype = "float32")#candidate|5853|(16,)|const|float32
call_5852 = relay.TupleGetItem(func_5060_call(relay.reshape(const_5853.astype('float32'), [16,])), 2)
call_5854 = relay.TupleGetItem(func_5062_call(relay.reshape(const_5853.astype('float32'), [16,])), 2)
func_899_call = mod.get_global_var('func_899')
func_902_call = mutated_mod.get_global_var('func_902')
var_5871 = relay.var("var_5871", dtype = "int8", shape = (728,))#candidate|5871|(728,)|var|int8
call_5870 = func_899_call(relay.reshape(var_5871.astype('int8'), [14, 4, 13]), relay.reshape(var_5871.astype('int8'), [14, 4, 13]), )
call_5872 = func_899_call(relay.reshape(var_5871.astype('int8'), [14, 4, 13]), relay.reshape(var_5871.astype('int8'), [14, 4, 13]), )
func_4983_call = mod.get_global_var('func_4983')
func_4985_call = mutated_mod.get_global_var('func_4985')
call_5884 = relay.TupleGetItem(func_4983_call(), 0)
call_5885 = relay.TupleGetItem(func_4985_call(), 0)
var_5887 = relay.var("var_5887", dtype = "bool", shape = (11, 28))#candidate|5887|(11, 28)|var|bool
bop_5888 = relay.multiply(call_5836.astype('float64'), var_5887.astype('float64')) # shape=(11, 28)
bop_5891 = relay.multiply(call_5837.astype('float64'), var_5887.astype('float64')) # shape=(11, 28)
bop_5893 = relay.floor_mod(var_5887.astype('float32'), call_5852.astype('float32')) # shape=(11, 28)
bop_5896 = relay.floor_mod(var_5887.astype('float32'), call_5854.astype('float32')) # shape=(11, 28)
func_1862_call = mod.get_global_var('func_1862')
func_1867_call = mutated_mod.get_global_var('func_1867')
var_5904 = relay.var("var_5904", dtype = "float64", shape = (9, 54))#candidate|5904|(9, 54)|var|float64
var_5905 = relay.var("var_5905", dtype = "float32", shape = (640,))#candidate|5905|(640,)|var|float32
call_5903 = relay.TupleGetItem(func_1862_call(relay.reshape(var_5904.astype('float64'), [9, 9, 6]), relay.reshape(var_5905.astype('float32'), [640,]), relay.reshape(var_5904.astype('float32'), [9, 9, 6]), ), 0)
call_5906 = relay.TupleGetItem(func_1867_call(relay.reshape(var_5904.astype('float64'), [9, 9, 6]), relay.reshape(var_5905.astype('float32'), [640,]), relay.reshape(var_5904.astype('float32'), [9, 9, 6]), ), 0)
uop_5918 = relay.sigmoid(var_5887.astype('float32')) # shape=(11, 28)
bop_5929 = relay.floor_divide(uop_5918.astype('float64'), relay.reshape(bop_5888.astype('float64'), relay.shape_of(uop_5918))) # shape=(11, 28)
bop_5932 = relay.floor_divide(uop_5918.astype('float64'), relay.reshape(bop_5891.astype('float64'), relay.shape_of(uop_5918))) # shape=(11, 28)
func_5008_call = mod.get_global_var('func_5008')
func_5011_call = mutated_mod.get_global_var('func_5011')
var_5934 = relay.var("var_5934", dtype = "float64", shape = (84,))#candidate|5934|(84,)|var|float64
call_5933 = relay.TupleGetItem(func_5008_call(relay.reshape(var_5934.astype('float64'), [1, 14, 6])), 0)
call_5935 = relay.TupleGetItem(func_5011_call(relay.reshape(var_5934.astype('float64'), [1, 14, 6])), 0)
output = relay.Tuple([call_5821,call_5825,const_5853,call_5870,var_5871,call_5884,bop_5893,call_5903,var_5904,var_5905,bop_5929,call_5933,var_5934,])
output2 = relay.Tuple([call_5822,call_5826,const_5853,call_5872,var_5871,call_5885,bop_5896,call_5906,var_5904,var_5905,bop_5932,call_5935,var_5934,])
func_5939 = relay.Function([var_5871,var_5887,var_5904,var_5905,var_5934,], output)
mod['func_5939'] = func_5939
mod = relay.transform.InferType()(mod)
var_5940 = relay.var("var_5940", dtype = "int8", shape = (728,))#candidate|5940|(728,)|var|int8
var_5941 = relay.var("var_5941", dtype = "bool", shape = (11, 28))#candidate|5941|(11, 28)|var|bool
var_5942 = relay.var("var_5942", dtype = "float64", shape = (9, 54))#candidate|5942|(9, 54)|var|float64
var_5943 = relay.var("var_5943", dtype = "float32", shape = (640,))#candidate|5943|(640,)|var|float32
var_5944 = relay.var("var_5944", dtype = "float64", shape = (84,))#candidate|5944|(84,)|var|float64
output = func_5939(var_5940,var_5941,var_5942,var_5943,var_5944,)
func_5945 = relay.Function([var_5940,var_5941,var_5942,var_5943,var_5944,], output)
mutated_mod['func_5945'] = func_5945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5801_call = mod.get_global_var('func_5801')
func_5802_call = mutated_mod.get_global_var('func_5802')
call_5985 = func_5801_call()
call_5986 = func_5801_call()
func_2361_call = mod.get_global_var('func_2361')
func_2364_call = mutated_mod.get_global_var('func_2364')
var_5993 = relay.var("var_5993", dtype = "int16", shape = (198,))#candidate|5993|(198,)|var|int16
call_5992 = func_2361_call(relay.reshape(var_5993.astype('int16'), [2, 9, 11]), relay.reshape(var_5993.astype('int16'), [2, 9, 11]), )
call_5994 = func_2361_call(relay.reshape(var_5993.astype('int16'), [2, 9, 11]), relay.reshape(var_5993.astype('int16'), [2, 9, 11]), )
const_5995 = relay.const([-6,9,7,1,-7,7,6,2,-7,-10,2,-1,2,4,-7,-7,-7,9,8,7,-8,3,-2,-1,6,6,-7,-4,2,-3,4,-4,-6,-5,6,2,-8,7,1,-9,-9,-6,9,5,8,2,8,3,2,10,1,9,6,1,2,-4,-2,7,-10,5,-10,2,-5,-4,6,-5,4,6,10,7,7,2,2,3,2,2,6,-2,2,10,-9,-4,-8,5,10,-9,3,-6,-1,-7,-6,-6,4,3,-3,-3,-7,5,7,-3,-2,-4,4,-8,-7,-9,-3,-5,-1,4,-1,-6,3,-6,-1,-7,-1,-8,9,1,10,-8,5,1,-2,-1,1,5,-9,4,10,-5,-2,-6,-8,8,-7,2,-2,7,7,8,5,1,4,8,-5,-5,-7,-10,7,2,4,3,6,-9,10,-10,-1,-1,-6,-9,3,10,4,-2,5,3,7,-7,-10,7,-4,-4,-7,3,5,6,7,-7,-3,-2,-4,-2,-4,5,5,-3,8,7,-4,1,-2,7,-3,10,5,6], dtype = "int16")#candidate|5995|(198,)|const|int16
bop_5996 = relay.logical_xor(var_5993.astype('int32'), relay.reshape(const_5995.astype('int32'), relay.shape_of(var_5993))) # shape=(198,)
output = relay.Tuple([call_5985,call_5992,bop_5996,])
output2 = relay.Tuple([call_5986,call_5994,bop_5996,])
func_6014 = relay.Function([var_5993,], output)
mod['func_6014'] = func_6014
mod = relay.transform.InferType()(mod)
var_6015 = relay.var("var_6015", dtype = "int16", shape = (198,))#candidate|6015|(198,)|var|int16
output = func_6014(var_6015)
func_6016 = relay.Function([var_6015], output)
mutated_mod['func_6016'] = func_6016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4606_call = mod.get_global_var('func_4606')
func_4608_call = mutated_mod.get_global_var('func_4608')
call_6031 = relay.TupleGetItem(func_4606_call(), 2)
call_6032 = relay.TupleGetItem(func_4608_call(), 2)
output = relay.Tuple([call_6031,])
output2 = relay.Tuple([call_6032,])
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
func_4562_call = mod.get_global_var('func_4562')
func_4563_call = mutated_mod.get_global_var('func_4563')
call_6047 = relay.TupleGetItem(func_4562_call(), 0)
call_6048 = relay.TupleGetItem(func_4563_call(), 0)
func_5503_call = mod.get_global_var('func_5503')
func_5506_call = mutated_mod.get_global_var('func_5506')
call_6069 = relay.TupleGetItem(func_5503_call(relay.reshape(call_6047.astype('float64'), [9, 8]), relay.reshape(call_6047.astype('float64'), [9, 8]), ), 0)
call_6070 = relay.TupleGetItem(func_5506_call(relay.reshape(call_6047.astype('float64'), [9, 8]), relay.reshape(call_6047.astype('float64'), [9, 8]), ), 0)
func_5293_call = mod.get_global_var('func_5293')
func_5294_call = mutated_mod.get_global_var('func_5294')
call_6072 = func_5293_call()
call_6073 = func_5293_call()
uop_6078 = relay.asinh(call_6047.astype('float32')) # shape=(6, 4, 3)
uop_6080 = relay.asinh(call_6048.astype('float32')) # shape=(6, 4, 3)
output = relay.Tuple([call_6069,call_6072,uop_6078,])
output2 = relay.Tuple([call_6070,call_6073,uop_6080,])
func_6086 = relay.Function([], output)
mod['func_6086'] = func_6086
mod = relay.transform.InferType()(mod)
mutated_mod['func_6086'] = func_6086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6086_call = mutated_mod.get_global_var('func_6086')
call_6087 = func_6086_call()
output = call_6087
func_6088 = relay.Function([], output)
mutated_mod['func_6088'] = func_6088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5293_call = mod.get_global_var('func_5293')
func_5294_call = mutated_mod.get_global_var('func_5294')
call_6162 = func_5293_call()
call_6163 = func_5293_call()
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_6171 = relay.TupleGetItem(func_5409_call(), 4)
call_6172 = relay.TupleGetItem(func_5410_call(), 4)
output = relay.Tuple([call_6162,call_6171,])
output2 = relay.Tuple([call_6163,call_6172,])
func_6182 = relay.Function([], output)
mod['func_6182'] = func_6182
mod = relay.transform.InferType()(mod)
mutated_mod['func_6182'] = func_6182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6182_call = mutated_mod.get_global_var('func_6182')
call_6183 = func_6182_call()
output = call_6183
func_6184 = relay.Function([], output)
mutated_mod['func_6184'] = func_6184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_6211 = func_5381_call()
call_6212 = func_5381_call()
output = call_6211
output2 = call_6212
func_6226 = relay.Function([], output)
mod['func_6226'] = func_6226
mod = relay.transform.InferType()(mod)
output = func_6226()
func_6227 = relay.Function([], output)
mutated_mod['func_6227'] = func_6227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5594_call = mod.get_global_var('func_5594')
func_5595_call = mutated_mod.get_global_var('func_5595')
call_6280 = func_5594_call()
call_6281 = func_5594_call()
func_5759_call = mod.get_global_var('func_5759')
func_5761_call = mutated_mod.get_global_var('func_5761')
call_6282 = func_5759_call()
call_6283 = func_5759_call()
func_5503_call = mod.get_global_var('func_5503')
func_5506_call = mutated_mod.get_global_var('func_5506')
const_6285 = relay.const([-4.654554,-6.526473,6.608192,0.220851,-3.547498,6.758914,-2.044238,6.660368,-2.817241,-9.616831,-7.817271,-9.208443,6.768128,-7.883260,-0.539623,2.302741,9.281420,3.837071,8.802365,4.129542,5.757017,3.926774,-4.374858,-2.269487,8.503687,-0.901803,1.904092,7.071372,3.026091,3.122099,4.633135,-3.770822,-0.939525,5.275183,-4.727785,6.045441,6.694171,1.961029,-7.694660,-4.172931,-2.259129,4.539155,5.235980,-0.282405,-0.250559,0.672923,-6.847521,-9.692070,2.018537,9.115299,7.261756,4.561899,9.685867,-3.617073,-0.342702,8.846800,-1.469559,6.149602,-1.294761,-8.320416,0.638842,-4.753391,-1.630801,8.887897,5.843515,8.147778,4.311658,2.814045,-4.556222,-8.179992,9.707143,3.494528], dtype = "float64")#candidate|6285|(72,)|const|float64
call_6284 = relay.TupleGetItem(func_5503_call(relay.reshape(const_6285.astype('float64'), [9, 8]), relay.reshape(const_6285.astype('float64'), [9, 8]), ), 0)
call_6286 = relay.TupleGetItem(func_5506_call(relay.reshape(const_6285.astype('float64'), [9, 8]), relay.reshape(const_6285.astype('float64'), [9, 8]), ), 0)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_6287 = relay.TupleGetItem(func_4699_call(), 0)
call_6288 = relay.TupleGetItem(func_4701_call(), 0)
output = relay.Tuple([call_6280,call_6282,call_6284,const_6285,call_6287,])
output2 = relay.Tuple([call_6281,call_6283,call_6286,const_6285,call_6288,])
func_6289 = relay.Function([], output)
mod['func_6289'] = func_6289
mod = relay.transform.InferType()(mod)
output = func_6289()
func_6290 = relay.Function([], output)
mutated_mod['func_6290'] = func_6290
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6324 = relay.var("var_6324", dtype = "int16", shape = (3, 14, 13))#candidate|6324|(3, 14, 13)|var|int16
var_6325 = relay.var("var_6325", dtype = "int16", shape = (3, 14, 13))#candidate|6325|(3, 14, 13)|var|int16
bop_6326 = relay.less(var_6324.astype('bool'), relay.reshape(var_6325.astype('bool'), relay.shape_of(var_6324))) # shape=(3, 14, 13)
func_874_call = mod.get_global_var('func_874')
func_878_call = mutated_mod.get_global_var('func_878')
var_6336 = relay.var("var_6336", dtype = "bool", shape = (780,))#candidate|6336|(780,)|var|bool
call_6335 = relay.TupleGetItem(func_874_call(relay.reshape(var_6336.astype('bool'), [13, 6, 10]), relay.reshape(var_6336.astype('bool'), [13, 6, 10]), ), 0)
call_6337 = relay.TupleGetItem(func_878_call(relay.reshape(var_6336.astype('bool'), [13, 6, 10]), relay.reshape(var_6336.astype('bool'), [13, 6, 10]), ), 0)
output = relay.Tuple([bop_6326,call_6335,var_6336,])
output2 = relay.Tuple([bop_6326,call_6337,var_6336,])
func_6338 = relay.Function([var_6324,var_6325,var_6336,], output)
mod['func_6338'] = func_6338
mod = relay.transform.InferType()(mod)
mutated_mod['func_6338'] = func_6338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6338_call = mutated_mod.get_global_var('func_6338')
var_6340 = relay.var("var_6340", dtype = "int16", shape = (3, 14, 13))#candidate|6340|(3, 14, 13)|var|int16
var_6341 = relay.var("var_6341", dtype = "int16", shape = (3, 14, 13))#candidate|6341|(3, 14, 13)|var|int16
var_6342 = relay.var("var_6342", dtype = "bool", shape = (780,))#candidate|6342|(780,)|var|bool
call_6339 = func_6338_call(var_6340,var_6341,var_6342,)
output = call_6339
func_6343 = relay.Function([var_6340,var_6341,var_6342,], output)
mutated_mod['func_6343'] = func_6343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_6369 = relay.TupleGetItem(func_4699_call(), 0)
call_6370 = relay.TupleGetItem(func_4701_call(), 0)
func_3359_call = mod.get_global_var('func_3359')
func_3362_call = mutated_mod.get_global_var('func_3362')
const_6374 = relay.const(3.269925, dtype = "float32")#candidate|6374|()|const|float32
call_6373 = relay.TupleGetItem(func_3359_call(relay.reshape(const_6374.astype('float32'), [])), 0)
call_6375 = relay.TupleGetItem(func_3362_call(relay.reshape(const_6374.astype('float32'), [])), 0)
output = relay.Tuple([call_6369,call_6373,const_6374,])
output2 = relay.Tuple([call_6370,call_6375,const_6374,])
func_6378 = relay.Function([], output)
mod['func_6378'] = func_6378
mod = relay.transform.InferType()(mod)
output = func_6378()
func_6379 = relay.Function([], output)
mutated_mod['func_6379'] = func_6379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6440 = relay.var("var_6440", dtype = "float64", shape = ())#candidate|6440|()|var|float64
var_6441 = relay.var("var_6441", dtype = "float64", shape = (10, 9, 8))#candidate|6441|(10, 9, 8)|var|float64
bop_6442 = relay.power(var_6440.astype('float64'), var_6441.astype('float64')) # shape=(10, 9, 8)
func_1095_call = mod.get_global_var('func_1095')
func_1099_call = mutated_mod.get_global_var('func_1099')
const_6451 = relay.const([-4,1,-9,1,3,8,1,-10,3,-6,10,-8,5,-4,5,-9,2,9,4,-7,-6,-2,4,-1,3,-5,-9,2,9,9,1,5,9,7,5,-10,-10,8,-6,2,8,2,10,-1,2,-5,9,-6,-3,2,8,9,-4,-3,5,8,3,-1,6,4,-4,-10,-6,-1,-9,6,-3,-7,-3,-9,-8,-2,-9,-3,-4,10,5,-9,6,9,3,5,4,4,4,4,10,-2,10,1,-4,2,-1,-10,2,-4,-9,-10,-3,-10,6,1,-1,-5,10,-3,-7,6,5,-6,-9,2,9,1,-6,1,5,10,-8,-5,10,-5,-4,-6,-6,7,-1,3,1,-4,-3,9,-10,3,3,-6,-9,-10,1,3,-6,-3,9,1,-10,-7,3,-10,-6,-10,-3,9,-7,-5,3,-6,-8,10,-4,9,5,6,3,-10,1,7,-8,7,5,6,2,9,-10,9,-9,8,4,1,-2,-8,4,-8,-2,-8,9,-5,5,-10,4,-2,8,6,-6,1,9,-10,7,-5,-2,-5,8,-3,5,-9,3,-1,-1,-4,1,4,7,5,1,2,-3,-6,9,4,-3,3,6,8,1,6,-7,4,-4,7,-6,-9,-8,-8,6,-10,-6,-8,9,10,8,-1,-6,-9,3,4,-7,-8,1,1,-9,10,-6,-10,4,2,-5,5,10,-2,1,2,-2,-2,-8,2,-4,5,-1,-2,4,-5,10,2,5,1,-3,-8,5,10,3,-1,4,-6,10,2,-5,-4,-8,-5,4,2,10,2,10,-7,4,1,-5,-5,-8,-10,3,-7,4,-5,-9,6,5,-3,10,9,9,3,8,8,4,-8,-3,7,9,6,9,7,9,-8,-9,4,6,1,-7,9,-6,10,3,7,-9,2,-2,-1,-1,4,5,-8,-7,-2,-10,6,7,-5,5,-6,4,2,9,1,-4,9,-2,8,-8,2,3,-3,-5,-3,-2,-5,-7,6,-2,-5,9,6,3,-1,-6,8,-2,-10,-1,9,1,2,3,-5,3,3,-4,-5,5,-9,-8,2,9,-9,4,4,4,-5,-5,3,-8,2,-7,10,-1,-5,-5,-9,9,-5,-7,-8,6,-9,-4,9,-9,6,7,8,-7,7,7,6,-7,9,-1,-7,2,8,-8,-8,9,3,-9,4,-3,8,10,-8,-7,2,-5,5,-5,-1,-1,2,-2,3,-5,9,-9,-9,-3,5,5,-5,8,-6,-2,-8,8,10,4,-3,-2,10,-1,2,8,-1,-7,-1,-6,-8,8,1,5,-7,-9,-9,-5,6,-9,-8,-6,-10,-7,7,-10,2,-10,-3,8,-5,2,-10,6,1,-2,10,9,-2,3,-2,2,-10,-8,-1,-4,-5,-2,-3,1,-4,6,5,-6,-4,4,-1,-9,-3,5,-5,-10,-9,-7,3,-8,-3,2,10,4,-4,-7,7,7,4,3,5,10,-8,-6,-7,7,-7,-7,-7,-10,-9,8,-4,7,-7,7,-4,5,6,-2,-4,-10,-9,7,-9,-7,-5,-6,7,4,4,7,-8,9,-2,4,3,8,-2,6,-1,10,7,4,9,-10,-9,2,-7,-1,3,6,3,8,8,-7,-8,-6,4,8,8,-6,-3,6,9,-3,-7,10,3,-5,3,-4,10,-5,2,8,9,8,-2,4,-4,-8,5,10,10,-3,-9,4,-8,2,10,9,3,3,-4,1,-5,-10,10,10,-7,-3,-1,4,7,1,-5,9,10,7,9,1,-8,-6,-2,8,-1,-4,9,-6,-5,4,-5,-9,-6,-8,-6,-1,-1,5,-3,-3,-6,-9,-8,-3,-9,-4,-1,1,1,2,-10,4,-10,-7,3,-7,10,8,-2,2,10,-10,-8,8,-2,-9,-5,-6,-3,8,-6,9,-3,-5,-7,-8,10,8,9,-7,10,3,-8,-10,5,-9,5,6,-4,-4,-7,-8,8,-5,3,8,-10,9,-2,-1,9,8,9,-1,-5,3,-7,9,4,2,9,-1,3,-9,8,-3,-1,8,-5,2,-4,-1,4,6,-7,-5,10,-5,5,9,-3,8,-1,3,-7,-7,-8,4,10,9,-10,-4,-2,3,-5,1,-5,4,-9,-4,-2,7,-9,3,1,-9,-10,-1,-3,2,-7,6,5,-1,-6,1,6,-1,9,6,-8,10,7,-2,6,-8,10,8,-3,10,-2,1,-8,-4,-8,6,-5,-6,10,3,-4,10,5,9,-4,1,-9,7,7,-4,-10,-1,-1,-7,6,6,1,6,-3,-7,-6,-7,1,4,-5,-2,-3,2,-1,4,9,9,-7,9,2,8,-4,-4,-9,4,-9,9,-9,-5,-9,10,-10,-9,4,6,4,5,-1,5,-9,3,7,-1,4,9,-6,3,-7,-2,10,8,-4,-4,-2,-4,-9,-1,1,-3,10,8,10,-4,4,8,8,8,7,-6,2,-1,6,-7,4,2,1,-1,-3,-8,3,-1,-1,10,2,8,5,-6,3,-8,5,-10,1,-7,-6,-1,2,9,-2,1,6,-1,3,2,1,3,-9,2,4,-6,6,-9,-9,10,-9,9,-4,-4,8,-3,5,6,-6,-6,8,3,9,-2,2,2,-7,-5,-1,-10,-7,9,6,8,4,4,-5,-7,1,-3,-3,4,-7,-1,-10,-9,-3,-8,2,10,-9,-7,3,7,3,-9,-6,-6,-4,1,-9,10,7,-10,-4,-6,-7,7,8,8,-3,-10,9,-2,-5,6,3,6,6,10,6,-4,2,-7,-5,-2,9,9,-7,3,-4,-6,9,-7,-7,6,7,-8,-1,-9,-7,5,2,8,-5,-1,-1,5,8,4,3,1,-10,-6,4,-5,8,-1,-6,-10,-1,9,10,2,8,-5,8,10,5,-6,3,1,5,-2,10,-1,4,3,-6,4,-4,4,7,9,1,-2,-9,4,7,-7,7,-10,-10,7,-1,-1,-1,7,10,-1,-1,3,-10,-6,-4,-5,-10,4,-7,5,3,1,10,2,-3,-1,8,4,3,-4,-4,-10,2,-4,6,-7,7,2,7,9,9,-4,-6,-4,10,-7,-4,1,-2,7,6,8,-3,5,6,-1,4,1,-6,10,-2,-2,-6,4,-8,8,4,-1,6,-8,10,7,-5,-5,-5,8,-1,-4,3,-5,-1,-9,8,-4,4,7,3,7,6,2,-6,-9,-1,4,-2,-7,1,-8,3,-3,7,-10,-8,2,-8,3,3,1,-4,-9,3,1,-1,-2,4,1,7,-2,10,-7,8,-2,-2,6,7,6,1,-3,6,-7,3,2,1,5,9,8,1,-10,-5,3,-4,-4,-6,-7,4,-3,-4,-7,10,-4,3,6,-6,-9,3,-4,10,-3,-5,-1,6,6,-10,5,-4,-8,-3,-10,-3,9,-2,-4,-9,1,7,4,5,-5,4,4,9,6,-10,-10,-7,10,9,6,-3,3,8,-5,-1,9,-8,-5,8,-8,8,-1,4,8,7,3,-2,2,-8,-4,-7,6,5,4,-3,-2,-10,-9,6,2,-1,5,-3,-3,4,-2,10,8,-9,9,-7,-2,5,5,-9,7,2,-5,-9,-8,8,5,9,-3,8,-8,-4,3,-4,-1,5,-4,9,4,2,2,3,7,-1,-10,-4,-5,1,-8,-8,9,-8,-10,4,7,-5,3,-6,-2,3,-9,10,-5,-4,5,1,-3,7,-8,-9,-7,3,4,2,-10,8,10,-3,-1,8,-7,2,-10,5,-1,2,-9,-10,8,-1,-7,-8,-8,-3,-6,-7,-2,4,7,1,-4,-4,1,9,5,8,10,-8,6,7,2,6,-10,-7,10,5,-10,8,-4,-1,-7,-1,-6,5,-10,-4,8,-8,10,7,3,5,-2,7,2,-3,8,7,-2,-5,-7,-9,-1,-5,-4,3,6,-3,3,-2,-7,-5,8,-8,-6,-7,2,-10,-2,-3,9,4,-4,-2,6,-3,1,-9,-9,1,1,-8,3,7,-5,2,6,9,-2,8,-7,2,-6,6,9,1,-9,-3,9,8,10,-7,-7,-8,-9,8,5,1,10,-1,9,8,-2,-10,1,-4,9,9,10,-4,4,-3,1,-4,-5,1,6,-2,2,-9,10,-6,-9,-7,-2,7,3,7,-6,-7,4,7,-7,8,10,2,3,1,1,-10,-6,-1,7,-5,8,5,9,-2,10,-4,7,10,-2,-3,-6,-9,10,-5,9,3,3,-9,-2,7,-1,2,-6,10,-5,4,6,8,-5,-6,-5,10,-6,10,-2,-10,9,10,6,7,3,-7,-5,8,9,2,10,2,5,-4,9,9,-5,3,-1,7,2,-4,8,-8,-5,-1,-4,-2,2,-5,9,-9,3,8,-4,7,-8,4,-4,-2,-3,-5,-5,6,-3,8,-3,6,9,-9,10,9,-8,3,3,10,-10,3,-1,3,-9,8,8,-9,2,1,5,-10,-3,2,10,-4,-8,6,-7,7,-1,-2,-1,-9,-1,4,10,-9,-5,-3,-5,-7,-5,2,3,-9,-4,-5,-4,-9,5,-10,-5,2,-10,-7,1,7,7,9,9,-6,1,-2,-8,-9,-2,9,-8,9,5,2,-2,-1,10,-10,-10,-4,8,5,6,-8,-2,8,-10,-9,-7,-1,2,7,-4,1,-3,-4,-2,8,2,8,5,-6,-7,1,10,4,-8,5,9,-7,-2,5,9,-4,9,6,2,-2,9,-4,7,-2,-10,-8,-3,-1,-7,1,-10,-6,-10,7,-4,-2,4,3,-5,-8,-2,-4,-1,-1,3,-4,-8,-6,-3,-10,-3,2,-10,9,-2,10,5,-10,-1,7,-5,-9,-1,1,9,5,-4,9,3,-9,7,10,5,8,-3,10,-6,-2,5,5,5,-3,-6,-2,2,-6,1,1,-10,-2,6,2,2,-10,-7,10,-6,10,-7,3,-4,-10,-8,2,2,10,7,-9,-6,-7,-6,5,-2,-4,-7,-10,-9,-5,1,-5,-1,-10,-9,-7,-10,9,9,-9,-9,2,1,5,4,7,7,-10,-6,-5,1,-9,-6,8,2,-8,10,5,4,3,1,-5,1,7,8,-10,5,10,8,7,-7,9,7,-1,5,8,6,-4,-1,-2,-4,7,-4,1,9,1,4,-3,5,1,2,6,5,4,-3,-6,-1,-6,-2,-6,-6,-6,7,1,-5,-2,2,-4,-9,4,5,9,-2,10,2,4,-2,-10,10,-1,-2,4,10,-2,8,-1,5,-8,4,1,-5,4,5,-6,-5,-2,9,-2,7,10,-1,6,-10,5,6,10,10,1,-9,-10,6,-1,1,-6,1,-2,8,2,-6,-9,-10,-4,-4,4,1,-8,-10,-2,6,7,-5,-2,1,-8,-9,-7,-8,9,-5,-5,-1,-3,-4,9,-2,-7,-9,9,-3,5,8,2,5,9,-6,-6,9,-5,-4,-1,3,5,-7,2,-3,-1,-10,-6,4,-5,-10,-5,-2,-2,-7,5,2,-3,-4,10,-1,6,-4,6,-8,8,6,8,6,-4,-6,-4,-9,-9,10,-10,-8,2,-1,-2,3,-10,3,-7,-10,3,-10,-4,2,1,1,-4,-8,-5,-9,7,-4,1,4,8,10,2,8,8,9,3,9,-1,4,-5,10,4,-8,5,4,-10,5,-4,-5,-5,2,-4,-3,-9,2,1,5,-8,-10,-6,6,-9,-7,-6,-7,-9,-6,1,10,8,3,4,5,-10,-4,-9,4,3,-1,6,-7,9,7,-5,-10,-9,-4,-1,-4,4,-1,10,1,9,-10,1,7,5,2,1,6,-6,-10,9,-10,-3,6,-6,-7,-10,-7,6,-3,-8,-2,-6,8,7,9,-3,9,-7,1,1,-6,5,-1,9,-4,8,5,-4,-6,-2,-9,3,5,4,-3,4,-5,7,1,-2,3,3,-6,3,-10,-8,-4,-8,2,4,8,-9,8,10,9,6,-4,10,-10,5,-9,-10,5,-1,1,-4,-3,1,-6,3,-3,-7,-10,8,-9,-9,-5,1,-8,-6,-8,-9,3,2,-10,-3,4,1,-7,5,3,6,4,9,10,2,-8,-8,-10,8,-5,-3,3,6,-5,5,4,8,-9,-1,-4,6,3,-1,-6,1,2,-2,-9,2,-9,2,10,-3,-6,-7,-5,-10,-9,-1,2,6,-7,-8,7,8,8,-1,-9,7,-7,8,9,2,1,-3,-7,-6,7,9,-3,-4,-9,1,-9,5,-5,2,1,4,-9,-6,5,-1,5,8,6,-10,7,5,10,-6,3,10,1,-7,-8,7,4,-6,7,-6,8,-10,-5,-4,4,-1,7,-2,-5,1,9,-9,-7,1,-2,8,1,6,-2,-3,8,3,7,-4,-2,8,-4,-6,3,-4,4,-7,-10,1,1,8,1,-7,-7,-1,-7,-2,-9,1,-8,8,-6,5,6,-8,3,10,-7,10,-9,3,-3,4,-5,-3,9,5,6,3,-7,3,-7,3,10,-10,-6,3,-9,-1,-4,-9,8,10,5,8,-4,-3,-1,-7,-2,10,-1,9,-1,-6,7,-8,1,-8,1,2,6,8,-4,8,3,3,-2,4,5,8,7,-8,6,-9,-4,2,-6,7,7,-5,-3,4,3,9,-10,-9,-3,-7,2,5,7,-6,-10,-5,6,7,10,-7,1,-8,-4,-8,-1,7,-3,1,-2,2,-8,8,7,-7,9,10,1,1,-3,4,5,9,-6,7,7,-9,-6,-9,6,-2,2,-3,7,8,-4,-8,-4,7,9,-7,1,1,6,-2,6,5,5,-10,-3,-6,3,-6,-3,8,-6,8,2,7,-9,-8,5,2,-3,-4,-3,3,-6,-4,3,1,-6,7,6,5,2,-2,-7,9,-9,8,5,9,-2,10,-6,3,10,1,3,-3,9,4,-2,-8,5,-4,-7,4,7,-5,7,-4,-7,4,10,4,5,-7,-10,7,-1,6,3,9,3,2,1,8,-10,9,2,-9,-1,3,3,7,-10,-4,-4,-4,7,7,-3,-8,-7,-2,2,5,10,-7,9,-5,-8,3,-1,8,-4,-8,2,-9,4,-8,-3,-10,-3,5,10,3,10,7,-7,-1,-2,8,-8,-2,8,-9,-5,5,-7,-1,10,-4,-2,-4,-7,-9,-6,10,-6,6,-2,-7,3,6,2,-6,3,-5,-2,5,-3,-8,-5,-3,-1,-5,4,-2,5,9,-7,-10,-9,-7,-5,10,-1,9,7,5,2,2,3,5,2,-5,-2,-1,-1,2,3,4], dtype = "int32")#candidate|6451|(2688,)|const|int32
call_6450 = relay.TupleGetItem(func_1095_call(relay.reshape(const_6451.astype('int32'), [14, 16, 12]), relay.reshape(const_6451.astype('int32'), [14, 16, 12]), ), 0)
call_6452 = relay.TupleGetItem(func_1099_call(relay.reshape(const_6451.astype('int32'), [14, 16, 12]), relay.reshape(const_6451.astype('int32'), [14, 16, 12]), ), 0)
uop_6459 = relay.tan(var_6441.astype('float32')) # shape=(10, 9, 8)
output = relay.Tuple([bop_6442,call_6450,const_6451,uop_6459,])
output2 = relay.Tuple([bop_6442,call_6452,const_6451,uop_6459,])
func_6465 = relay.Function([var_6440,var_6441,], output)
mod['func_6465'] = func_6465
mod = relay.transform.InferType()(mod)
mutated_mod['func_6465'] = func_6465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6465_call = mutated_mod.get_global_var('func_6465')
var_6467 = relay.var("var_6467", dtype = "float64", shape = ())#candidate|6467|()|var|float64
var_6468 = relay.var("var_6468", dtype = "float64", shape = (10, 9, 8))#candidate|6468|(10, 9, 8)|var|float64
call_6466 = func_6465_call(var_6467,var_6468,)
output = call_6466
func_6469 = relay.Function([var_6467,var_6468,], output)
mutated_mod['func_6469'] = func_6469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6038_call = mod.get_global_var('func_6038')
func_6040_call = mutated_mod.get_global_var('func_6040')
call_6500 = relay.TupleGetItem(func_6038_call(), 0)
call_6501 = relay.TupleGetItem(func_6040_call(), 0)
var_6507 = relay.var("var_6507", dtype = "int16", shape = (450,))#candidate|6507|(450,)|var|int16
bop_6508 = relay.bitwise_and(call_6500.astype('int32'), relay.reshape(var_6507.astype('int32'), relay.shape_of(call_6500))) # shape=(450,)
bop_6511 = relay.bitwise_and(call_6501.astype('int32'), relay.reshape(var_6507.astype('int32'), relay.shape_of(call_6501))) # shape=(450,)
output = relay.Tuple([bop_6508,])
output2 = relay.Tuple([bop_6511,])
func_6515 = relay.Function([var_6507,], output)
mod['func_6515'] = func_6515
mod = relay.transform.InferType()(mod)
mutated_mod['func_6515'] = func_6515
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6516 = relay.var("var_6516", dtype = "int16", shape = (450,))#candidate|6516|(450,)|var|int16
func_6515_call = mutated_mod.get_global_var('func_6515')
call_6517 = func_6515_call(var_6516)
output = call_6517
func_6518 = relay.Function([var_6516], output)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_6539 = relay.TupleGetItem(func_5409_call(), 1)
call_6540 = relay.TupleGetItem(func_5410_call(), 1)
uop_6545 = relay.log2(call_6539.astype('float32')) # shape=(13, 6, 10)
uop_6547 = relay.log2(call_6540.astype('float32')) # shape=(13, 6, 10)
uop_6548 = relay.sin(uop_6545.astype('float32')) # shape=(13, 6, 10)
uop_6550 = relay.sin(uop_6547.astype('float32')) # shape=(13, 6, 10)
var_6554 = relay.var("var_6554", dtype = "bool", shape = (13, 6, 10))#candidate|6554|(13, 6, 10)|var|bool
bop_6555 = relay.less(call_6539.astype('bool'), relay.reshape(var_6554.astype('bool'), relay.shape_of(call_6539))) # shape=(13, 6, 10)
bop_6558 = relay.less(call_6540.astype('bool'), relay.reshape(var_6554.astype('bool'), relay.shape_of(call_6540))) # shape=(13, 6, 10)
func_6038_call = mod.get_global_var('func_6038')
func_6040_call = mutated_mod.get_global_var('func_6040')
call_6560 = relay.TupleGetItem(func_6038_call(), 0)
call_6561 = relay.TupleGetItem(func_6040_call(), 0)
output = relay.Tuple([uop_6548,bop_6555,call_6560,])
output2 = relay.Tuple([uop_6550,bop_6558,call_6561,])
func_6573 = relay.Function([var_6554,], output)
mod['func_6573'] = func_6573
mod = relay.transform.InferType()(mod)
mutated_mod['func_6573'] = func_6573
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6574 = relay.var("var_6574", dtype = "bool", shape = (13, 6, 10))#candidate|6574|(13, 6, 10)|var|bool
func_6573_call = mutated_mod.get_global_var('func_6573')
call_6575 = func_6573_call(var_6574)
output = call_6575
func_6576 = relay.Function([var_6574], output)
mutated_mod['func_6576'] = func_6576
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6653 = relay.const([[[2.034181,3.572155,-6.633612,3.762911,7.848785,5.942520,4.428178,4.297180,8.411252,6.836344,-3.538666],[9.765308,-3.329190,-4.503676,-1.296233,1.020785,5.463549,-1.626758,0.866343,3.848361,1.268420,4.137556],[7.605135,-0.535111,5.756211,-5.093706,1.266317,-1.611215,8.202737,1.185659,-6.433356,4.525714,-8.339985],[5.198270,1.392295,-8.414394,-2.110390,-0.330901,-2.858410,-6.007039,-0.277259,4.624624,5.152910,5.677945],[-9.740367,-0.791065,3.436795,3.891780,4.222413,1.613146,5.710676,3.212294,3.310911,1.667744,-7.495970]],[[-9.356027,-5.128246,2.743977,1.253956,-9.478353,3.473481,4.370281,-7.201960,-4.273988,9.387126,5.165623],[-6.807866,-2.054979,-2.302255,1.779188,-2.367872,3.950302,-1.429013,-0.456068,5.676386,9.165289,8.695552],[0.665913,8.114021,6.142540,0.665599,5.786383,-3.807278,-1.426123,6.741570,5.347282,7.608790,8.621383],[5.291453,1.304896,-1.152862,-0.472175,4.261686,-7.588196,2.162493,-0.567263,-3.847809,-9.072218,2.178884],[4.904893,1.473110,-8.793197,5.181605,-6.729183,1.984162,7.771895,-7.187940,8.443979,2.987668,9.065419]],[[-1.253254,4.126916,0.225669,5.363523,-4.151887,-0.693457,1.241029,-9.880093,-4.704920,-2.134233,0.048388],[9.792410,8.486919,7.157178,-3.281255,8.085886,-8.227143,2.689607,9.421906,8.881011,0.993902,3.861370],[-0.139496,8.381174,-0.897878,4.910889,2.957776,5.406897,2.979876,0.599526,1.564049,-3.799835,-4.915044],[-5.087519,-8.152706,5.935996,2.217460,9.728520,7.144617,-4.669877,-3.727591,1.546509,-9.779150,-7.361162],[9.362665,-2.414658,-5.123018,6.049935,-4.801712,-9.519857,4.099686,8.070550,-0.568172,-9.083006,9.760355]],[[1.374623,-0.551901,-9.901208,-2.769276,4.687769,-3.507449,-1.034163,-4.241151,0.376652,9.597813,-2.541364],[-7.924768,8.273131,-7.716361,-1.995094,-4.228008,3.730726,-8.295111,-2.066387,-2.310830,-2.666731,6.957636],[2.976009,-6.824544,-5.383418,9.144454,-7.307095,-9.525980,-5.330238,-4.024551,6.960732,2.657095,8.305177],[-4.769716,-8.403533,4.520520,8.568585,9.159730,5.906179,-6.818028,-2.350958,-1.352746,7.964501,-6.777519],[8.612215,-3.981169,-6.157637,4.905870,8.989780,1.089014,-1.931353,-7.674719,5.299601,-9.214877,-4.215078]],[[-3.526532,-1.700842,3.960113,-2.674897,-5.497189,-0.003641,-4.397979,-7.410100,5.395624,1.136040,7.826811],[6.828164,9.407127,0.444190,9.827143,-6.722904,-8.420841,-4.803804,-7.641122,-1.377798,-3.731698,5.218295],[9.978000,-0.143526,1.050538,5.442576,1.803141,8.586263,3.682436,2.567349,-8.331823,-5.456597,-8.468861],[-7.195051,1.022989,6.800287,-0.937635,-8.868780,-6.159634,-3.278595,-3.803140,-2.640391,-0.706679,8.540875],[7.706552,8.100258,-5.577815,-4.706786,-7.402881,-2.344948,8.388887,-3.672883,-2.662238,0.828844,0.378971]],[[6.754190,4.260130,-5.770433,7.002789,0.654731,-5.468061,-5.779013,2.001703,6.997168,3.188568,7.793609],[-6.444675,-4.343336,1.383067,2.585938,9.254882,-3.634479,8.349126,5.857658,-8.890951,9.649161,3.885605],[-8.841151,-9.673830,-6.223153,1.004196,4.657768,7.350069,-7.869133,3.877865,-2.238281,-9.426604,-1.114245],[7.617061,-7.943689,-6.789797,-0.840182,2.623183,-0.994498,-5.664195,-0.267353,0.201169,3.678259,3.339679],[4.922798,-9.105699,-0.531879,-2.169036,-5.034517,-8.511870,-5.031063,-0.056530,-6.738968,6.155746,9.307086]]], dtype = "float32")#candidate|6653|(6, 5, 11)|const|float32
uop_6654 = relay.acosh(const_6653.astype('float32')) # shape=(6, 5, 11)
func_3756_call = mod.get_global_var('func_3756')
func_3761_call = mutated_mod.get_global_var('func_3761')
var_6657 = relay.var("var_6657", dtype = "int64", shape = (48, 2))#candidate|6657|(48, 2)|var|int64
const_6658 = relay.const([1.008137,-5.215566,-6.538836,-6.960883,-8.404682,2.817395,6.427014,-4.455106,-8.602969,4.957915,-5.322583,3.885919,-2.800772,8.192675,-8.442253,8.115574,-6.179533,2.924987,-9.292494,-3.027726,2.397698,7.160439,-0.947089,-7.360031,-0.238574,-0.665493,1.390794,-0.624625,1.458343,0.493177,-1.260360,9.687338,-7.742037,1.670719,-9.772423,8.982173,5.477801,-4.069942,-4.827882,-9.654918,4.723260,0.236855,-8.163697,-5.929600,-2.832005,3.989984,4.951106,9.963382,7.732457,-8.222652,4.881273,-1.269153,-4.102400,-1.367638,7.939520,5.156962,0.546864,9.479064,-6.960398,6.861465,3.701911,8.139298,-5.027925,-9.941529,1.408917,9.896538,1.352410,-9.657584,6.650147,-7.803242,5.792532,7.210562,3.532961,9.324936,-5.369778,-4.397547,6.096624,-0.058154,-1.880284,-5.824231,-7.018219,-2.771794,3.738019,5.053612,-1.773649,0.364633,-6.723875,-2.799216,3.015226,7.493185,5.488196,9.394085,-9.753071,-1.718053,-7.278538,-4.268771,-5.078104,-6.679571,0.157353,-7.528354,-0.049053,-0.158636,-7.713284,-1.343170,-5.791623,-7.692069,2.227341,-4.407470,4.860361,-9.590243,5.250770,-9.186887,-4.107848,0.136102,9.883106,4.535606,2.216820,-6.600137,-9.329136,9.429453,-7.296392,-2.558866,7.548103,6.441391,8.183079,4.375493,5.990765,1.046081,-6.578459,6.297504,-7.703252,1.894901,-5.664917,-2.210931,-4.712285,6.861269,1.252321,-5.821874,3.741312,9.245610,-0.562594,6.314875,2.468894,0.051221,-9.389795,7.041989,2.376337,-1.256514,-8.137945,-0.552309,7.246785,4.368597,-4.467257,9.657555,-8.499658,-7.611270,2.403551,-1.757443,-5.505811,2.224968,-6.077201,-3.574930,6.188336,-8.197630,8.040922,3.113333,-8.390114,2.891054,-9.773590,-3.424544,6.389611,8.045297,6.430291,3.119998,9.961353,-4.287160,0.553777,5.631853,7.615960,-4.350407,2.807748,7.943956,1.695853,-5.729473,-0.942522,-0.344824,5.667722,-8.438916,5.307816,7.743989,-1.733872,-1.329213,-5.502062,5.509917,4.678656,-7.568484,4.196928,7.409647,-1.821992,-3.272869,-4.874174,-1.528141,5.971898,-5.431944,0.412646,2.385219,8.494031,5.492490,-7.190878,-8.855688,8.724745,-2.072491,-9.608983,9.170599,3.010405,1.636613,-1.412345,7.994288,1.161688,-4.124261,7.358130,-6.079233,0.381383,-4.539110,-6.256950,-4.848780,3.641817,-5.234098,-3.646941,-7.544499,-9.005570,7.414656,-5.865281,-2.629676,1.540499,-0.482381,-8.295625,8.176711,-1.662998,4.452019,-2.646512,-4.281792,-5.091627,-9.707239,-1.931108,-1.719452,-5.459152,9.988799,0.182147,-8.668304,-5.015029,6.989588,-5.095475,4.451146,1.853691,9.132104,-8.109086,8.029115,4.975043,7.475908,3.491758,-5.972525,3.979168,-0.689565,5.894303,8.523082,8.195487,-8.893569,-9.554670,-7.114567,3.964850,2.604657,-9.052189,-0.827584,-7.166611,7.537213,-9.561712,-5.412617,-7.388505,-8.588296,8.250385,3.260141,-0.339532,-4.352448,7.153377,-4.247564,7.736321,-0.888341,5.477034,6.395963,-1.324637,9.704701,-8.162276,1.614245,-7.757202,-5.800764,3.268534,-5.686777,6.216137,-0.605288,0.420133,7.267770,3.860883,-3.600856,3.631902,-2.502970,0.522310,-1.687049,0.049740,-8.035279,0.331842,-7.970135,-8.799461,-2.147862,0.806370,3.941005,-0.587024,5.714031,-4.566619,-9.152728,6.855569,-1.874507,-7.457048,-3.577645,-1.693307,8.777771,6.979851,-4.905067,-7.941755,-2.414800,-4.508656,-8.486721,-5.744858,-3.421298,-3.877338,-2.298607,2.472900,-7.404546,6.050096,-6.641857,8.237335,1.045825,5.824208,-0.782208,5.410004,8.173117,-8.569012,-0.276360,-4.672905,-8.501505,2.335509,-8.979225,9.389800,-7.688528,-6.942798,-8.244657,-9.813124,-0.262563,0.509699,0.117356,7.421848,-2.894845,-4.128670,6.062434,4.218558,8.095804,-3.001342,-5.475109,-4.662100,9.385120,7.997670,-5.577258,3.290184,1.539762,-0.630631,2.166610,4.031508,1.895490,-6.941704,-0.919726,-5.224812,-3.475844,-3.913287,-5.357700,9.643779,3.974576,5.512699,-9.805588,-5.881623,-7.885730,-8.528646,8.767902,5.410176,-6.436315,1.970400,-2.159942,-0.740872,-7.671436,4.874866,-6.971453,-9.345235,3.175544,8.402749,7.580121,4.185442,-9.077671,2.696183,5.909807,8.814628,7.164104,9.150817,-7.228474,-9.451905,-1.411761,-8.805061,2.227680,-2.175512,-6.981555,-9.508274,0.538429,8.698052,-8.924521,1.367849,-3.602968,4.304209,6.794645,9.904536,-0.869198,0.855957,6.790326,4.377386,-9.045589,2.724124,-8.690826,-1.098172,2.687763,5.614309,1.973583,0.756458,9.656344,8.919549,9.448340,7.969152,-8.928602,-2.025584,-7.220002,-3.865025,2.181824,7.083224,-5.510116,-1.774565,-9.039831,0.523894,-2.982178,0.512107,5.560479,5.898346,2.202975,-4.928352,5.456573,0.649879,1.100086,-7.602874,4.722305,-7.727213,-2.033143,8.953470,-4.883342,-6.006648,6.949786,7.725830,-2.965467,-5.408892,1.260719,0.857633,4.504864,-1.948460,0.166543,-3.473403,-1.684156,-7.788449,4.596590,1.916184,-6.869248,-1.411224,4.227133,-8.767089,-7.937695,5.119904,1.285061,-3.227927,3.944358,6.933295,-6.498193,7.058638,-5.467751,5.746204,4.549250,-3.938775,-2.941267,-3.160387,-7.670053,1.718502,8.964493,-5.844867,9.284308,6.497052,3.575523,6.956704,-3.509932,-0.678826,-6.624904,-8.025703,3.524292,6.968913,-2.530230,3.587578,-4.864637,4.788973,-8.897045,7.474977,3.169633,-0.282797,6.461070,-3.264183,6.894904,8.560924,-3.061353,5.012185,-6.471737,4.874999,-9.044518,5.317230,4.378612,-3.887614,-8.138154,9.530609,4.544285,-8.606073,-0.476210,-6.069390,5.110178,2.780242,-7.811062,1.624062,-1.658667,2.193087,-7.507789,4.206102,4.473069,6.094583,2.405158,3.967579,-1.320482,-9.563980,-6.675943,-8.012796,-7.202649,7.696337,4.128154,6.440925,9.883569,-7.621680,5.991189,8.134786,-1.179793,-2.717926,-7.099061,-3.775285,3.371791,7.396404,4.667903,3.492842,5.673638,-5.377209,-0.021853,-2.349173,-3.459873,7.899811,6.298508,2.622027,0.253742,2.151302,4.684997,-3.034239,-5.313599,7.986931,-6.854749,0.228139,8.718963,-0.462166,0.703260,-8.623013,0.602933,7.608161,-2.184932,-9.077673,-8.692090,1.801966,1.312249,-9.936963,7.812374,-5.898078,1.950042,-6.710599,9.383867,-7.923925,6.442517,6.568361,-7.956339,4.684458,0.120165,-3.396993,-0.972826,3.193635,4.950231,3.916252,3.128342,-9.837543,-2.900146,-5.346374,8.222747,-9.798459,2.402795,-0.099295,6.777577,-9.882494,2.734144,-3.506308,3.955722,-4.742022,-5.353423,2.662556,7.819060,-0.053658,-6.437181,0.054329,9.957338,7.360771,0.378852], dtype = "float32")#candidate|6658|(640,)|const|float32
call_6656 = relay.TupleGetItem(func_3756_call(relay.reshape(var_6657.astype('int64'), [8, 2, 6]), relay.reshape(var_6657.astype('int64'), [8, 2, 6]), relay.reshape(const_6658.astype('float32'), [640,]), ), 3)
call_6659 = relay.TupleGetItem(func_3761_call(relay.reshape(var_6657.astype('int64'), [8, 2, 6]), relay.reshape(var_6657.astype('int64'), [8, 2, 6]), relay.reshape(const_6658.astype('float32'), [640,]), ), 3)
func_6086_call = mod.get_global_var('func_6086')
func_6088_call = mutated_mod.get_global_var('func_6088')
call_6672 = relay.TupleGetItem(func_6086_call(), 0)
call_6673 = relay.TupleGetItem(func_6088_call(), 0)
func_2525_call = mod.get_global_var('func_2525')
func_2529_call = mutated_mod.get_global_var('func_2529')
var_6703 = relay.var("var_6703", dtype = "uint64", shape = ())#candidate|6703|()|var|uint64
var_6704 = relay.var("var_6704", dtype = "uint64", shape = (224,))#candidate|6704|(224,)|var|uint64
call_6702 = relay.TupleGetItem(func_2525_call(relay.reshape(var_6703.astype('uint64'), []), relay.reshape(var_6704.astype('uint64'), [1, 14, 16]), ), 0)
call_6705 = relay.TupleGetItem(func_2529_call(relay.reshape(var_6703.astype('uint64'), []), relay.reshape(var_6704.astype('uint64'), [1, 14, 16]), ), 0)
output = relay.Tuple([uop_6654,call_6656,var_6657,const_6658,call_6672,call_6702,var_6703,var_6704,])
output2 = relay.Tuple([uop_6654,call_6659,var_6657,const_6658,call_6673,call_6705,var_6703,var_6704,])
func_6714 = relay.Function([var_6657,var_6703,var_6704,], output)
mod['func_6714'] = func_6714
mod = relay.transform.InferType()(mod)
var_6715 = relay.var("var_6715", dtype = "int64", shape = (48, 2))#candidate|6715|(48, 2)|var|int64
var_6716 = relay.var("var_6716", dtype = "uint64", shape = ())#candidate|6716|()|var|uint64
var_6717 = relay.var("var_6717", dtype = "uint64", shape = (224,))#candidate|6717|(224,)|var|uint64
output = func_6714(var_6715,var_6716,var_6717,)
func_6718 = relay.Function([var_6715,var_6716,var_6717,], output)
mutated_mod['func_6718'] = func_6718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6741 = relay.var("var_6741", dtype = "int8", shape = (4, 14, 8))#candidate|6741|(4, 14, 8)|var|int8
const_6742 = relay.const([[[3,8,5,8,-1,-10,-1,-10],[6,-3,9,-4,-8,3,-3,5],[9,7,-7,-3,-5,3,-8,7],[2,8,8,6,-8,-9,-6,-6],[-10,-8,-7,-7,-4,6,-5,7],[-3,-9,-6,-8,-7,-5,3,-7],[-6,10,-6,6,9,-3,7,2],[-4,2,9,4,6,7,3,-2],[9,-2,1,4,-2,-4,6,8],[10,-9,7,-3,3,2,-5,6],[-6,-6,6,7,-4,6,1,-9],[-3,10,-2,-5,-4,-2,1,1],[-6,-6,-7,-10,-8,-1,10,1],[-10,5,5,-8,7,8,-10,7]],[[7,10,-6,7,7,-2,9,2],[4,3,7,8,3,-2,-6,1],[-2,-9,1,4,-3,-9,-2,4],[-8,7,10,7,-1,10,-8,3],[2,-10,-8,-5,1,-7,-4,-8],[8,8,-1,3,6,3,4,5],[10,3,10,-10,3,-3,-8,1],[-6,-8,-8,1,4,-9,10,6],[-1,-9,-10,-1,8,-2,-5,-6],[4,8,-5,-7,4,9,1,-5],[6,-1,-3,-9,-6,-9,6,10],[7,1,10,1,3,8,-5,6],[5,10,-2,10,2,7,-5,7],[8,6,-7,9,-6,3,8,-7]],[[-7,-2,7,-4,-3,4,-9,-2],[10,-4,4,6,10,3,9,2],[8,4,8,-4,-1,1,-1,7],[-8,6,-4,-3,-2,-4,-8,-4],[2,2,7,3,4,8,-6,7],[-7,7,5,-6,6,-5,-8,-1],[-8,2,-8,-1,-8,10,-5,-9],[9,-4,4,9,-1,4,-5,10],[7,9,7,-10,3,9,4,-10],[4,7,-7,-7,5,10,6,5],[1,9,-8,-5,8,8,-3,-6],[4,4,2,-10,3,-8,1,10],[-7,-10,-9,-3,10,-8,-10,10],[10,5,-3,8,6,-3,-9,-9]],[[-6,-1,-5,-10,8,7,-4,3],[-9,5,-5,8,-1,6,-7,-6],[5,8,4,4,7,1,8,-5],[-2,1,-3,7,-3,4,10,-3],[-9,-7,-8,-8,-4,-4,1,-1],[10,-10,-4,-9,-2,5,6,10],[-6,10,-8,8,-7,4,4,3],[-1,8,-10,10,-1,7,-2,3],[-2,3,1,-1,4,6,-3,1],[-10,9,6,-5,4,-2,-8,6],[8,-1,-1,-5,10,-2,-10,6],[1,-3,5,-2,9,7,9,-9],[-5,5,-3,-10,6,5,-4,-8],[-8,-10,7,4,-7,3,-8,-4]]], dtype = "int8")#candidate|6742|(4, 14, 8)|const|int8
bop_6743 = relay.less_equal(var_6741.astype('bool'), relay.reshape(const_6742.astype('bool'), relay.shape_of(var_6741))) # shape=(4, 14, 8)
output = relay.Tuple([bop_6743,])
output2 = relay.Tuple([bop_6743,])
func_6746 = relay.Function([var_6741,], output)
mod['func_6746'] = func_6746
mod = relay.transform.InferType()(mod)
mutated_mod['func_6746'] = func_6746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6747 = relay.var("var_6747", dtype = "int8", shape = (4, 14, 8))#candidate|6747|(4, 14, 8)|var|int8
func_6746_call = mutated_mod.get_global_var('func_6746')
call_6748 = func_6746_call(var_6747)
output = call_6748
func_6749 = relay.Function([var_6747], output)
mutated_mod['func_6749'] = func_6749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_6777 = func_5381_call()
call_6778 = func_5381_call()
uop_6795 = relay.log2(call_6777.astype('float32')) # shape=(15, 6, 5)
uop_6797 = relay.log2(call_6778.astype('float32')) # shape=(15, 6, 5)
output = uop_6795
output2 = uop_6797
func_6799 = relay.Function([], output)
mod['func_6799'] = func_6799
mod = relay.transform.InferType()(mod)
output = func_6799()
func_6800 = relay.Function([], output)
mutated_mod['func_6800'] = func_6800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4983_call = mod.get_global_var('func_4983')
func_4985_call = mutated_mod.get_global_var('func_4985')
call_6869 = relay.TupleGetItem(func_4983_call(), 0)
call_6870 = relay.TupleGetItem(func_4985_call(), 0)
output = call_6869
output2 = call_6870
func_6876 = relay.Function([], output)
mod['func_6876'] = func_6876
mod = relay.transform.InferType()(mod)
mutated_mod['func_6876'] = func_6876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6876_call = mutated_mod.get_global_var('func_6876')
call_6877 = func_6876_call()
output = call_6877
func_6878 = relay.Function([], output)
mutated_mod['func_6878'] = func_6878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_6884 = relay.TupleGetItem(func_5176_call(), 0)
call_6885 = relay.TupleGetItem(func_5178_call(), 0)
output = relay.Tuple([call_6884,])
output2 = relay.Tuple([call_6885,])
func_6886 = relay.Function([], output)
mod['func_6886'] = func_6886
mod = relay.transform.InferType()(mod)
output = func_6886()
func_6887 = relay.Function([], output)
mutated_mod['func_6887'] = func_6887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6950 = relay.var("var_6950", dtype = "float64", shape = (9, 13, 10))#candidate|6950|(9, 13, 10)|var|float64
uop_6951 = relay.acosh(var_6950.astype('float64')) # shape=(9, 13, 10)
func_6338_call = mod.get_global_var('func_6338')
func_6343_call = mutated_mod.get_global_var('func_6343')
const_6955 = relay.const([-5,6,4,-6,9,-6,-3,-9,5,4,-8,-2,-7,8,-6,2,-3,-9,-10,-7,-6,5,3,-6,10,2,9,2,10,9,4,-9,-2,7,-5,3,9,-1,-4,1,-8,-3,-6,10,7,-3,-3,-10,-5,8,-1,-1,1,-5,10,-8,-8,3,5,3,5,3,-2,-4,9,-7,5,3,2,10,3,-8,8,-8,-7,5,8,-1,-10,-5,8,-3,2,8,3,5,5,-8,7,6,-6,-7,8,3,2,10,10,1,-7,-5,7,6,-5,5,-10,-7,1,-1,3,-10,1,-3,1,-4,-4,-1,-1,3,3,10,-6,-10,-3,9,-4,-9,6,8,7,-8,-1,10,-5,-7,-10,4,4,-4,-6,2,-9,-6,4,-4,6,-10,8,10,-4,4,2,9,-3,-4,5,10,7,-10,-2,10,4,-4,1,-8,10,8,-1,9,-9,4,9,9,-1,-6,3,10,7,2,9,2,1,3,-6,-7,-5,8,-8,-9,6,-4,3,-6,2,-8,-5,10,2,-1,8,-1,2,9,6,1,-5,-1,-10,9,-3,3,-9,8,-8,8,-7,-9,10,-9,5,-10,-6,9,8,-10,-6,10,7,5,-5,1,5,2,-7,-4,4,3,7,-8,3,-3,-8,-4,-1,10,3,-1,-9,-4,6,9,3,10,7,4,-3,-8,-2,-7,1,-8,-7,3,-1,-4,-6,-7,-8,-1,-2,-6,-2,5,7,4,9,2,-2,-4,3,-10,-5,-10,-3,-10,3,-9,10,-6,7,-5,-3,-2,2,-10,8,-4,8,-7,-2,-5,5,-10,1,4,-10,-4,-5,-10,6,2,9,-6,9,-9,2,-5,-9,4,5,-7,6,-7,-2,8,6,-2,5,3,3,4,-7,2,8,-7,-3,-7,8,10,1,-7,-9,2,-9,7,-9,7,1,-2,-7,-1,3,-9,-2,-2,10,-9,-10,-4,-10,-1,3,-2,1,-5,-3,9,6,1,-1,-4,6,-10,6,7,5,4,-8,-6,2,-5,10,5,4,-8,2,-5,-5,5,9,9,10,5,2,6,1,-1,7,-8,5,-7,-8,-5,7,4,2,1,-7,-1,-8,-4,-10,1,-4,-2,5,-6,-2,-5,1,-7,5,6,-6,2,5,2,-3,-7,-2,-6,8,1,2,-9,7,7,-3,5,-1,-1,5,4,-6,6,9,4,-5,7,3,10,1,-4,-10,4,-8,-8,10,-4,4,-4,-4,-2,5,6,-7,-8,6,5,-2,5,-7,4,6,6,8,7,-10,2,-10,3,-7,-8,-4,-6,3,6,-8,-7,-6,6,-5,-7,4,8,8,-3,-4,-7,-3,3,-8,-6,-9,3,-8,-9,-4,5,6,1,-9,-8,-5,-9,9,4,3,4,-3,-7,-7,-3,5,-6,5,4,2,-5,6,-5,10,-2,7,6,2,2,-4,-10,-5,9,-6,2,-4,6,2,4], dtype = "int16")#candidate|6955|(546,)|const|int16
var_6956 = relay.var("var_6956", dtype = "bool", shape = (780,))#candidate|6956|(780,)|var|bool
call_6954 = relay.TupleGetItem(func_6338_call(relay.reshape(const_6955.astype('int16'), [3, 14, 13]), relay.reshape(const_6955.astype('int16'), [3, 14, 13]), relay.reshape(var_6956.astype('bool'), [780,]), ), 2)
call_6957 = relay.TupleGetItem(func_6343_call(relay.reshape(const_6955.astype('int16'), [3, 14, 13]), relay.reshape(const_6955.astype('int16'), [3, 14, 13]), relay.reshape(var_6956.astype('bool'), [780,]), ), 2)
func_6014_call = mod.get_global_var('func_6014')
func_6016_call = mutated_mod.get_global_var('func_6016')
const_6960 = relay.const([[-4,1,-3,-1,1,6],[1,5,8,-1,-6,9],[-5,9,-4,-7,1,10],[1,2,1,5,-9,3],[6,10,-7,9,5,-5],[6,-9,1,10,3,6],[-9,5,3,-7,-3,2],[-5,1,8,1,9,-10],[9,2,3,5,9,2],[-9,-3,-6,-2,6,5],[9,-8,5,-7,-10,-6],[7,5,-5,-9,5,-9],[-7,-4,-2,8,4,-10],[-4,3,7,6,-5,1],[-7,-4,-2,-5,-4,3],[7,-9,-7,-10,-7,-6],[-4,-10,3,-7,-4,5],[6,7,7,5,-3,-5],[-3,-3,9,7,-2,-2],[-8,7,2,8,-10,-5],[6,4,-4,10,-5,-8],[-2,8,1,1,1,-3],[-10,10,-7,10,6,-1],[-3,8,5,2,2,-3],[10,-4,4,3,-8,5],[-9,-9,6,-7,-2,-5],[-2,6,7,-7,-5,-7],[8,-4,-4,-4,-1,9],[-4,4,-1,4,-8,-5],[2,-3,5,-8,1,-1],[-9,9,7,-7,6,8],[-4,1,5,-8,-2,-5],[-10,-7,-5,7,3,-5]], dtype = "int16")#candidate|6960|(33, 6)|const|int16
call_6959 = relay.TupleGetItem(func_6014_call(relay.reshape(const_6960.astype('int16'), [198,])), 1)
call_6961 = relay.TupleGetItem(func_6016_call(relay.reshape(const_6960.astype('int16'), [198,])), 1)
func_2886_call = mod.get_global_var('func_2886')
func_2888_call = mutated_mod.get_global_var('func_2888')
var_6969 = relay.var("var_6969", dtype = "float32", shape = (1600,))#candidate|6969|(1600,)|var|float32
call_6968 = relay.TupleGetItem(func_2886_call(relay.reshape(var_6969.astype('float32'), [16, 10, 10])), 1)
call_6970 = relay.TupleGetItem(func_2888_call(relay.reshape(var_6969.astype('float32'), [16, 10, 10])), 1)
output = relay.Tuple([uop_6951,call_6954,const_6955,var_6956,call_6959,const_6960,call_6968,var_6969,])
output2 = relay.Tuple([uop_6951,call_6957,const_6955,var_6956,call_6961,const_6960,call_6970,var_6969,])
func_6977 = relay.Function([var_6950,var_6956,var_6969,], output)
mod['func_6977'] = func_6977
mod = relay.transform.InferType()(mod)
var_6978 = relay.var("var_6978", dtype = "float64", shape = (9, 13, 10))#candidate|6978|(9, 13, 10)|var|float64
var_6979 = relay.var("var_6979", dtype = "bool", shape = (780,))#candidate|6979|(780,)|var|bool
var_6980 = relay.var("var_6980", dtype = "float32", shape = (1600,))#candidate|6980|(1600,)|var|float32
output = func_6977(var_6978,var_6979,var_6980,)
func_6981 = relay.Function([var_6978,var_6979,var_6980,], output)
mutated_mod['func_6981'] = func_6981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_6987 = relay.TupleGetItem(func_5409_call(), 4)
call_6988 = relay.TupleGetItem(func_5410_call(), 4)
func_1862_call = mod.get_global_var('func_1862')
func_1867_call = mutated_mod.get_global_var('func_1867')
var_7002 = relay.var("var_7002", dtype = "float64", shape = (486,))#candidate|7002|(486,)|var|float64
const_7003 = relay.const([-8.969262,9.343982,-0.354217,8.003494,-3.259749,1.370221,8.091652,-0.603141,-4.375966,1.657567,8.801098,0.993067,3.378043,-8.880556,-9.649443,5.724056,4.985237,-4.088724,3.122632,-1.029964,2.024524,6.011062,7.865385,-6.484448,3.286899,7.530447,-1.505608,-7.450892,5.573639,0.844872,7.475102,2.610935,5.550950,-5.841961,0.048090,-7.012574,-8.373257,-1.538470,3.743698,-7.326233,-5.528349,-9.483508,-2.730330,-3.086132,3.552781,4.306566,6.164744,7.587069,7.409625,7.715487,4.784006,5.713762,2.687516,1.259186,-0.836362,6.980790,0.547097,-1.710309,-2.419314,1.560931,-8.881645,-6.436661,9.191793,-9.332915,8.132477,-4.330574,6.417722,-2.432199,2.024594,-8.973662,9.407891,-8.869907,9.067489,8.196425,-1.164931,0.585860,7.485384,-5.853907,-5.375694,2.080057,-5.928153,-0.612643,8.388326,-2.850493,-1.215753,6.217208,-3.914004,-8.956496,-1.844755,9.752975,-4.047087,3.521241,-1.974300,0.905823,-4.449739,-7.121820,-1.941047,-7.809706,6.057086,-2.581900,1.879840,-2.221896,2.153051,8.228931,-5.983443,-6.252813,-8.696272,-4.936032,6.426151,6.688700,2.977664,-8.698940,-7.390962,8.530377,8.384301,1.947662,8.762725,-5.325488,-2.698169,-5.840427,-8.638638,0.032551,-3.352022,4.189573,7.861525,7.039897,-4.535675,-8.915832,9.295266,2.905128,0.427171,7.844443,-5.654052,-4.909788,-9.343655,2.486863,1.339692,9.375516,-1.814632,-6.013168,9.203135,-8.940430,5.420160,-1.455527,5.214413,-7.885166,-6.238502,4.622334,8.076490,6.053726,2.158275,9.957555,3.554352,-9.268787,3.216355,-8.809114,7.223117,0.226241,8.210946,8.948569,8.170778,-1.831095,8.489164,-4.817175,8.324238,-9.827830,-2.752627,2.503131,-3.997509,8.680709,-7.526386,-1.035724,3.631061,7.167947,5.210461,9.226217,-8.380816,-3.206201,3.232911,-3.419077,-9.643350,8.248976,-7.354107,3.869048,1.756946,1.633515,-3.974188,2.441056,2.660051,-0.938165,3.942842,7.192779,8.547674,8.473555,-5.663511,7.989946,0.376871,9.337792,-4.323962,-0.127835,0.984475,6.967056,-2.634629,8.708558,9.787579,-9.954446,8.335841,-6.400311,-9.571924,-8.796807,-5.834640,5.963451,-1.049302,3.064577,1.700828,-9.710343,9.786591,-6.916864,-7.827554,3.567414,-0.770358,-6.177673,8.133526,-3.872927,0.119330,-3.339065,2.353509,2.354464,-2.865315,-7.577120,-1.404337,5.585090,-2.891044,2.028490,1.407323,3.348812,1.662585,-4.775229,-6.651488,-7.640219,8.569391,7.590623,-3.736975,-9.566199,-7.304069,0.126727,-1.763159,-1.697180,-5.894614,2.465522,2.374968,2.331257,3.192519,4.642906,3.144908,4.002600,5.803066,7.824761,5.806234,-4.329438,-3.007375,-3.334340,-5.234211,8.539727,8.545263,5.198123,1.088751,9.249232,-4.258889,9.321711,-6.726656,-2.198677,8.637475,7.160547,6.363351,-2.098740,2.449023,-0.372744,-7.514760,3.038416,5.557811,-0.713281,7.382197,1.509627,-8.863172,1.455900,5.308121,-5.734327,7.528021,4.100236,-9.754090,-8.353114,-9.797285,4.596717,0.228733,-9.926072,1.154126,1.249045,-4.855980,-1.030083,1.350711,4.860867,3.026492,-9.101405,-7.681971,-1.873478,5.161491,-0.438664,2.822309,-5.274401,-1.266459,6.201659,0.695286,1.486384,8.400971,2.767237,6.033237,8.150411,-7.458233,-7.643723,9.726468,8.336512,2.130814,3.198248,-4.124851,5.605063,-6.797204,-4.492644,-4.834556,-7.969795,-9.150231,-6.250013,-5.263344,-4.268182,4.092229,1.771283,0.792104,-4.289348,6.705311,-7.794829,2.258961,-3.393475,-3.890746,-1.858775,-3.507043,9.010831,-4.438373,2.658020,4.436760,4.452858,-8.507395,-9.937879,-0.893837,-9.148446,-1.712613,5.077696,7.376183,4.593709,-1.318101,-8.755897,-1.448729,4.901872,4.336177,-1.450712,0.148263,-0.985545,-2.986929,4.778292,1.340194,-8.003728,-8.006154,3.995953,-8.012640,-0.209770,-6.146006,4.537755,-8.355023,4.378885,6.396678,-5.151500,-2.759270,-9.031887,2.781931,6.898056,-0.975625,-0.249507,3.581704,-8.041402,1.541188,-1.049289,6.597107,-6.767531,0.220260,5.943444,7.769492,3.958419,-3.130193,3.417202,8.413667,-6.013875,-2.333744,8.178614,8.522230,6.258361,-2.757073,-3.583318,-3.201937,1.575754,1.812090,-7.817868,-3.839536,-7.697293,-1.980911,1.592082,-0.300844,0.377651,-0.981191,-7.552369,-1.233742,-5.377820,9.865359,-7.243571,-3.683905,7.231103,-7.679647,-9.765211,4.454162,-8.564632,-9.431383,-0.916783,3.202904,-4.106305,-4.264455,8.178044,-4.364139,6.078603,5.876641,9.723786,5.984446,1.579145,2.191588,-0.259787,-2.084403,-1.425490,-1.765446,5.049045,-3.049169,-9.576316,-1.896257,9.716379,5.190813,-4.759675,-6.015209,-6.977649,7.606894,5.815362,-4.960151,0.552489,-7.034183,7.432109,-3.479169,6.856513,-4.197042,6.496939,0.149375,-8.706592,8.636945,9.566797,-2.033391,6.638499,1.114114,-9.466809,9.255539,-1.042925,0.874704,-0.620640,-4.171887,-0.645564,0.433668,3.512150,-9.402275,-5.985266,1.570825,2.056117,6.106256,0.822178,-6.192010,-6.092293,0.903187,8.731342,2.792675,5.358613,4.897371,-5.248901,0.289765,-4.148156,2.428610,-0.309516,-0.498801,6.455719,-0.147516,1.383809,-3.522563,-3.154276,-2.395864,1.612026,-0.433405,-8.947219,-1.290399,-8.807681,-2.858328,-1.923452,7.512069,-4.199524,-5.182971,-9.985898,-3.217079,7.116610,4.282659,9.299971,-1.758184,6.289260,5.508684,-2.050200,4.397767,2.064809,4.124262,6.814003,-7.399733,8.076384,1.402060,-2.083348,8.773204,5.228266,5.468641,-0.134381,0.896758,-8.912348,9.548020,-5.171329,-7.826419,3.682358,4.783270,-8.145661,-4.922962,2.644211,4.616662,-1.606647,0.456195,-8.072804,-2.355244,-7.412160,-3.486788,-8.020572,-1.910457,-0.796331,-3.379784,-6.745275,1.646687,-2.818040,-0.893350,2.320834,0.815899,-4.048861,8.962710,3.897137,-4.956420,0.746963,7.948006,-8.746488,4.372624,-9.796646,-9.543172,2.126731,1.949721,-9.822479,3.520033,-7.548534,6.352567,-2.289873,5.126563,-9.443171,6.853483,-9.188118,7.016104,-9.040063,-2.616315,-2.229856,-2.662708,-8.924584,4.607457,6.907470,-1.940514,8.335727,3.730544,1.335138,-1.689192,-4.149038,4.888491,-3.277901,0.410859,1.377936,2.412511,6.730072,-0.509230,0.127609,-8.247481,-2.908693,-2.238401,-6.402667,3.605579,-4.010102,3.531280,-7.867106,-9.144908,1.700410,8.961252,2.273873,-2.216834,-4.445947,-1.690079,7.498676,7.157347,2.507760,9.839444,7.615121,3.695164,-1.146981,-8.010855,-8.153695,6.460807,-0.180832,-4.868442,6.279280,-7.119787,3.273792,-8.735370,2.223064,3.560266,2.968723], dtype = "float32")#candidate|7003|(640,)|const|float32
call_7001 = relay.TupleGetItem(func_1862_call(relay.reshape(var_7002.astype('float64'), [9, 9, 6]), relay.reshape(const_7003.astype('float32'), [640,]), relay.reshape(var_7002.astype('float32'), [9, 9, 6]), ), 0)
call_7004 = relay.TupleGetItem(func_1867_call(relay.reshape(var_7002.astype('float64'), [9, 9, 6]), relay.reshape(const_7003.astype('float32'), [640,]), relay.reshape(var_7002.astype('float32'), [9, 9, 6]), ), 0)
bop_7010 = relay.less_equal(var_7002.astype('bool'), call_6987.astype('bool')) # shape=(486,)
bop_7013 = relay.less_equal(var_7002.astype('bool'), call_6988.astype('bool')) # shape=(486,)
output = relay.Tuple([call_7001,const_7003,bop_7010,])
output2 = relay.Tuple([call_7004,const_7003,bop_7013,])
func_7046 = relay.Function([var_7002,], output)
mod['func_7046'] = func_7046
mod = relay.transform.InferType()(mod)
var_7047 = relay.var("var_7047", dtype = "float64", shape = (486,))#candidate|7047|(486,)|var|float64
output = func_7046(var_7047)
func_7048 = relay.Function([var_7047], output)
mutated_mod['func_7048'] = func_7048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5783_call = mod.get_global_var('func_5783')
func_5784_call = mutated_mod.get_global_var('func_5784')
call_7062 = func_5783_call()
call_7063 = func_5783_call()
func_5096_call = mod.get_global_var('func_5096')
func_5100_call = mutated_mod.get_global_var('func_5100')
var_7067 = relay.var("var_7067", dtype = "float32", shape = ())#candidate|7067|()|var|float32
const_7068 = relay.const([-5.837898,-7.970532,-9.341741,-8.969802,4.020218,8.677780,8.698177,-9.988893,7.171206,-1.494061,-4.295512,1.027990,2.363400,-5.506427,6.036011,-2.889532,9.445950,5.809089,6.727797,0.422459,3.878767,3.730903,7.619493,-9.269998,-3.602068,5.115422,-9.732811], dtype = "float32")#candidate|7068|(27,)|const|float32
var_7069 = relay.var("var_7069", dtype = "float32", shape = (135,))#candidate|7069|(135,)|var|float32
call_7066 = func_5096_call(relay.reshape(var_7067.astype('float32'), []), relay.reshape(const_7068.astype('float32'), [9, 1, 3]), relay.reshape(var_7069.astype('float32'), [9, 5, 3]), )
call_7070 = func_5096_call(relay.reshape(var_7067.astype('float32'), []), relay.reshape(const_7068.astype('float32'), [9, 1, 3]), relay.reshape(var_7069.astype('float32'), [9, 5, 3]), )
const_7078 = relay.const([[[-5,-3,-5,2,-9],[4,-6,-10,-9,-6],[10,-2,6,-1,8],[-8,-10,-5,-3,9],[-9,-2,5,-3,4],[-5,-7,-3,2,5]],[[5,-2,-8,1,4],[-5,-4,2,-9,-4],[-4,-5,7,-6,-5],[9,-8,-4,8,10],[-5,6,2,-9,-5],[-1,-3,4,8,8]],[[-4,-3,8,1,-1],[9,-5,-5,5,5],[-8,-2,7,-2,-5],[8,7,-2,-7,2],[-3,5,-6,-5,8],[-2,8,-9,10,-10]],[[10,-4,7,6,8],[-1,-9,-9,1,-7],[-5,3,-4,8,4],[9,-4,-2,1,-5],[6,-2,-6,-1,4],[-4,-8,2,-1,-6]],[[-8,8,-9,5,8],[3,-7,10,-5,-10],[8,9,3,6,2],[9,-8,-4,-7,9],[8,-1,6,-8,-10],[-1,2,-4,1,-9]],[[1,-5,-2,6,-5],[-7,8,7,7,6],[-4,8,6,9,2],[-2,-3,-4,3,6],[-6,2,1,7,-5],[-9,-7,-2,-9,-2]],[[-8,-5,-1,-10,8],[4,-1,7,8,-3],[-6,-1,-9,8,6],[10,4,9,-6,-2],[6,-10,4,10,1],[4,-6,-10,10,5]],[[-10,3,2,-1,-2],[-5,-9,-7,2,5],[-1,-1,-6,3,1],[-3,5,-6,8,7],[10,-10,9,-4,-5],[6,-1,-4,-10,-2]],[[-7,3,-1,-10,6],[-10,-1,7,-6,-1],[-3,-6,4,9,8],[-6,-6,-6,-7,7],[4,-10,-6,5,8],[-4,4,5,-1,-3]],[[-8,4,9,-3,4],[8,7,-5,4,6],[7,-5,1,3,6],[1,-7,10,-4,-2],[2,8,-7,2,-4],[-5,10,4,-2,3]],[[4,-2,2,-7,-2],[7,-9,3,8,9],[-4,5,-6,5,-7],[-4,6,-2,-5,-5],[5,2,4,10,-1],[-6,-3,8,1,5]],[[-6,8,4,-10,-8],[9,4,-7,-7,4],[8,-2,2,-10,7],[-2,-6,-3,-10,-3],[-8,2,-2,-2,-8],[8,8,-6,-1,-5]],[[6,9,8,4,7],[-10,10,6,-3,-2],[7,-8,9,3,-4],[8,6,2,9,5],[5,-2,-7,6,9],[2,9,8,6,8]],[[2,10,3,-5,9],[-10,-7,-1,1,6],[-7,-5,-10,4,6],[8,10,-9,1,5],[4,-8,8,-5,7],[10,-10,2,-7,8]],[[2,5,-5,3,6],[7,3,-1,3,9],[-9,-5,3,-1,-6],[8,-6,-8,-5,6],[-10,5,8,-4,4],[-2,4,4,-5,-10]]], dtype = "int16")#candidate|7078|(15, 6, 5)|const|int16
bop_7079 = relay.floor_divide(call_7062.astype('float32'), relay.reshape(const_7078.astype('float32'), relay.shape_of(call_7062))) # shape=(15, 6, 5)
bop_7082 = relay.floor_divide(call_7063.astype('float32'), relay.reshape(const_7078.astype('float32'), relay.shape_of(call_7063))) # shape=(15, 6, 5)
output = relay.Tuple([call_7066,var_7067,const_7068,var_7069,bop_7079,])
output2 = relay.Tuple([call_7070,var_7067,const_7068,var_7069,bop_7082,])
func_7086 = relay.Function([var_7067,var_7069,], output)
mod['func_7086'] = func_7086
mod = relay.transform.InferType()(mod)
mutated_mod['func_7086'] = func_7086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7086_call = mutated_mod.get_global_var('func_7086')
var_7088 = relay.var("var_7088", dtype = "float32", shape = ())#candidate|7088|()|var|float32
var_7089 = relay.var("var_7089", dtype = "float32", shape = (135,))#candidate|7089|(135,)|var|float32
call_7087 = func_7086_call(var_7088,var_7089,)
output = call_7087
func_7090 = relay.Function([var_7088,var_7089,], output)
mutated_mod['func_7090'] = func_7090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5176_call = mod.get_global_var('func_5176')
func_5178_call = mutated_mod.get_global_var('func_5178')
call_7141 = relay.TupleGetItem(func_5176_call(), 0)
call_7142 = relay.TupleGetItem(func_5178_call(), 0)
uop_7157 = relay.log10(call_7141.astype('float32')) # shape=(10, 9, 16)
uop_7159 = relay.log10(call_7142.astype('float32')) # shape=(10, 9, 16)
func_5471_call = mod.get_global_var('func_5471')
func_5475_call = mutated_mod.get_global_var('func_5475')
var_7170 = relay.var("var_7170", dtype = "int8", shape = ())#candidate|7170|()|var|int8
var_7171 = relay.var("var_7171", dtype = "float64", shape = (585, 1))#candidate|7171|(585, 1)|var|float64
var_7172 = relay.var("var_7172", dtype = "int16", shape = (450,))#candidate|7172|(450,)|var|int16
call_7169 = relay.TupleGetItem(func_5471_call(relay.reshape(var_7170.astype('int8'), []), relay.reshape(var_7171.astype('float64'), [195, 3]), relay.reshape(var_7172.astype('int16'), [450,]), ), 2)
call_7173 = relay.TupleGetItem(func_5475_call(relay.reshape(var_7170.astype('int8'), []), relay.reshape(var_7171.astype('float64'), [195, 3]), relay.reshape(var_7172.astype('int16'), [450,]), ), 2)
output = relay.Tuple([uop_7157,call_7169,var_7170,var_7171,var_7172,])
output2 = relay.Tuple([uop_7159,call_7173,var_7170,var_7171,var_7172,])
func_7178 = relay.Function([var_7170,var_7171,var_7172,], output)
mod['func_7178'] = func_7178
mod = relay.transform.InferType()(mod)
var_7179 = relay.var("var_7179", dtype = "int8", shape = ())#candidate|7179|()|var|int8
var_7180 = relay.var("var_7180", dtype = "float64", shape = (585, 1))#candidate|7180|(585, 1)|var|float64
var_7181 = relay.var("var_7181", dtype = "int16", shape = (450,))#candidate|7181|(450,)|var|int16
output = func_7178(var_7179,var_7180,var_7181,)
func_7182 = relay.Function([var_7179,var_7180,var_7181,], output)
mutated_mod['func_7182'] = func_7182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4527_call = mod.get_global_var('func_4527')
func_4528_call = mutated_mod.get_global_var('func_4528')
call_7203 = relay.TupleGetItem(func_4527_call(), 1)
call_7204 = relay.TupleGetItem(func_4528_call(), 1)
output = call_7203
output2 = call_7204
func_7237 = relay.Function([], output)
mod['func_7237'] = func_7237
mod = relay.transform.InferType()(mod)
mutated_mod['func_7237'] = func_7237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7237_call = mutated_mod.get_global_var('func_7237')
call_7238 = func_7237_call()
output = call_7238
func_7239 = relay.Function([], output)
mutated_mod['func_7239'] = func_7239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5594_call = mod.get_global_var('func_5594')
func_5595_call = mutated_mod.get_global_var('func_5595')
call_7252 = func_5594_call()
call_7253 = func_5594_call()
var_7254 = relay.var("var_7254", dtype = "bool", shape = (11, 28))#candidate|7254|(11, 28)|var|bool
bop_7255 = relay.less_equal(call_7252.astype('bool'), var_7254.astype('bool')) # shape=(11, 28)
bop_7258 = relay.less_equal(call_7253.astype('bool'), var_7254.astype('bool')) # shape=(11, 28)
output = relay.Tuple([bop_7255,])
output2 = relay.Tuple([bop_7258,])
func_7261 = relay.Function([var_7254,], output)
mod['func_7261'] = func_7261
mod = relay.transform.InferType()(mod)
var_7262 = relay.var("var_7262", dtype = "bool", shape = (11, 28))#candidate|7262|(11, 28)|var|bool
output = func_7261(var_7262)
func_7263 = relay.Function([var_7262], output)
mutated_mod['func_7263'] = func_7263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_7269 = relay.TupleGetItem(func_5409_call(), 0)
call_7270 = relay.TupleGetItem(func_5410_call(), 0)
func_2886_call = mod.get_global_var('func_2886')
func_2888_call = mutated_mod.get_global_var('func_2888')
var_7283 = relay.var("var_7283", dtype = "float32", shape = (1600,))#candidate|7283|(1600,)|var|float32
call_7282 = relay.TupleGetItem(func_2886_call(relay.reshape(var_7283.astype('float32'), [16, 10, 10])), 0)
call_7284 = relay.TupleGetItem(func_2888_call(relay.reshape(var_7283.astype('float32'), [16, 10, 10])), 0)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_7287 = func_5381_call()
call_7288 = func_5381_call()
output = relay.Tuple([call_7269,call_7282,var_7283,call_7287,])
output2 = relay.Tuple([call_7270,call_7284,var_7283,call_7288,])
func_7294 = relay.Function([var_7283,], output)
mod['func_7294'] = func_7294
mod = relay.transform.InferType()(mod)
var_7295 = relay.var("var_7295", dtype = "float32", shape = (1600,))#candidate|7295|(1600,)|var|float32
output = func_7294(var_7295)
func_7296 = relay.Function([var_7295], output)
mutated_mod['func_7296'] = func_7296
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7311 = relay.const([[[-9,8,2,-5,-9],[9,4,-10,-6,8],[-9,-1,-8,-9,-2]],[[-6,1,10,-8,-6],[-3,8,8,6,1],[3,-1,-8,3,-3]],[[-8,-7,2,4,2],[8,6,3,-4,-5],[-10,-4,1,9,1]],[[-10,-10,-10,4,-4],[-4,4,-10,4,-3],[-8,7,6,-4,-3]],[[-7,-4,2,9,7],[-4,10,3,-4,-2],[5,-2,2,2,2]],[[-10,10,6,-9,-8],[2,9,10,10,8],[1,-3,-8,2,2]],[[-5,5,-8,7,-7],[6,-7,-1,-9,-8],[-6,2,3,-6,-8]]], dtype = "int16")#candidate|7311|(7, 3, 5)|const|int16
const_7312 = relay.const([[[4,-3,-2,-9,-10],[-7,2,3,-1,-9],[-10,-10,-1,-5,-9]],[[2,-8,-4,-7,1],[-8,10,-10,-10,-8],[1,-7,8,-2,-3]],[[-8,4,-2,-6,1],[-8,-6,1,-9,-8],[-1,4,10,8,-7]],[[-2,-7,-2,-7,8],[6,9,4,7,-4],[-10,-5,-2,8,-6]],[[-10,9,7,4,10],[1,8,7,1,-5],[2,-7,4,10,9]],[[7,6,-7,-5,-4],[5,-10,-5,-4,2],[9,-9,-9,-8,-4]],[[-6,-8,-7,5,8],[-9,-5,5,-8,4],[10,-4,-2,3,5]]], dtype = "int16")#candidate|7312|(7, 3, 5)|const|int16
bop_7313 = relay.left_shift(const_7311.astype('int16'), relay.reshape(const_7312.astype('int16'), relay.shape_of(const_7311))) # shape=(7, 3, 5)
output = bop_7313
output2 = bop_7313
func_7319 = relay.Function([], output)
mod['func_7319'] = func_7319
mod = relay.transform.InferType()(mod)
output = func_7319()
func_7320 = relay.Function([], output)
mutated_mod['func_7320'] = func_7320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6182_call = mod.get_global_var('func_6182')
func_6184_call = mutated_mod.get_global_var('func_6184')
call_7337 = relay.TupleGetItem(func_6182_call(), 1)
call_7338 = relay.TupleGetItem(func_6184_call(), 1)
func_4699_call = mod.get_global_var('func_4699')
func_4701_call = mutated_mod.get_global_var('func_4701')
call_7340 = relay.TupleGetItem(func_4699_call(), 0)
call_7341 = relay.TupleGetItem(func_4701_call(), 0)
bop_7348 = relay.greater(call_7340.astype('bool'), call_7337.astype('bool')) # shape=(1, 28)
bop_7351 = relay.greater(call_7341.astype('bool'), call_7338.astype('bool')) # shape=(1, 28)
output = relay.Tuple([bop_7348,])
output2 = relay.Tuple([bop_7351,])
func_7376 = relay.Function([], output)
mod['func_7376'] = func_7376
mod = relay.transform.InferType()(mod)
output = func_7376()
func_7377 = relay.Function([], output)
mutated_mod['func_7377'] = func_7377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6378_call = mod.get_global_var('func_6378')
func_6379_call = mutated_mod.get_global_var('func_6379')
call_7445 = relay.TupleGetItem(func_6378_call(), 1)
call_7446 = relay.TupleGetItem(func_6379_call(), 1)
uop_7447 = relay.atan(call_7445.astype('float64')) # shape=(9, 8, 11)
uop_7449 = relay.atan(call_7446.astype('float64')) # shape=(9, 8, 11)
func_538_call = mod.get_global_var('func_538')
func_541_call = mutated_mod.get_global_var('func_541')
const_7453 = relay.const([5.828256,-4.267374,-6.093469,-9.201008,-3.669444,-6.887286,4.838300,3.733871,5.478789,-5.911413,0.988351,-9.987348,6.251086,-9.210075,1.937373,5.498043,0.908072,5.216132,-5.743923,4.688503,5.353248,2.645099,7.592038,4.052422,-7.017441,8.207272,8.129492,-8.819822,8.414910,4.796551,4.414307,-7.179054,8.986368,-4.361579,7.885756,-1.343425,1.369579,9.935817,-5.161787,3.709379,-0.154122,9.071748,2.931730,3.377358,-2.314731,6.880816,7.975892,-2.209657,7.173913,-0.142980,-1.286831,5.526411,7.963723,-6.343617,-4.965979,-4.851537,2.494653,-7.671792,2.431974,7.550384,-3.433704,3.991885,-5.489089,-5.228721,-8.672309,-4.740913,0.869080,0.112748,-8.041006,3.959942,1.057163,-8.837018,7.139161,6.242555,-4.342215,-6.153188,-1.284917,-8.125965,-9.359297,-4.505777,4.600515,5.495951,8.919823,8.500369,1.639702,-2.177644,-1.133803,4.008233,2.704662,-5.033348,2.523265,-5.543429,-3.645828,9.769823,-6.236078,-0.072623,-3.466644,-4.693811,-1.404642,-7.288948,-3.350775,-9.243291,8.603643,-9.958372,4.170453,-3.267704,-8.799167,-2.137808,8.036160,8.185589,1.051317,5.769100,3.251547,0.334670,-3.606819,3.924300,-2.278216,5.927521,7.637196,-8.287116,0.562170,-7.242972,-4.932647,-3.538359,-5.577061,9.309636,6.306025,8.075300,-8.740508,-9.690887,-7.946958,-2.881410,-6.331016,-7.044763,0.860911,-1.317161,1.425223,-6.409518,7.636641,9.861970,-1.779455,7.460506,-6.666659,3.826744,-7.880259,8.502163,2.648883,2.066838,2.564039,-3.310364,2.782895,2.278922,3.033390,-0.381549,9.107034,-4.283857,-2.271233,9.076492,-7.396392,1.497988,9.816936,-1.792747,-7.021071,-0.622655,9.088302,0.670101,4.006536,-9.653290,-5.133853,9.577098,-6.728491,-7.181728,8.899643,2.824444,-3.109138,-0.004878,1.870680,-2.417518,5.584648,-5.878396,5.341912,5.694750,-6.357474,5.904976,-1.489170,-6.665095,-3.446038,4.666437,9.512657,-5.643875,3.911831,8.182026,5.578236,6.868636,-6.693791,3.595751,3.561555,-4.792196,-9.326286,-1.293832,-7.610362,-0.512178,0.102479,-3.353407,-5.244996,-0.293631,-4.444516,6.251726,-9.621908,-2.374885,-9.981326,-3.557227,-0.493274,8.109203,6.212479,1.316080,9.003493,-9.841940,1.848761,7.831929,9.327726,4.863535,2.271968,7.067992,9.684895,-5.451632,-5.733663,1.278416,3.742088,9.121021,7.480120,-6.066558,-9.396536,8.410638,5.664375,-7.004340,4.103084,-6.319457,-6.339832,-4.336254,2.463437,6.267070,4.046546,-3.258375,6.902445,9.098489,-2.576489,7.104256,9.623633,-6.801034,9.516502,0.159213,4.376949,9.306187,-4.593186,5.673152,-1.499520,8.972289,-6.617038,-6.662768,5.937674,-9.271656,7.166066,0.005244,-3.582814,-0.131507,-0.565569,-9.766439,3.738767,7.133299,0.362644,-0.684726,9.264826,-0.983639,0.784886,2.251687,-8.599190,8.424849,-1.601366,-0.817331,-7.791255,-4.696282,2.779405,-7.369024,0.716494,-9.893903,6.510329,-2.691653,-4.838916,-0.652553,-5.348482,-0.957721,0.370502,-1.252980,-5.452610,-3.786508,1.154271,0.059667,-6.214981,-4.724671,2.881060,-3.402240,7.502681,4.792691,3.117478,6.273458,-8.523001,3.906702,1.364059,7.574053,-2.240353,0.051590,-8.481016,-9.044055,-9.077650,-9.913657,3.590230,-4.046202,-2.215327,-5.679825,3.500216,4.740946,-8.194840,4.576911,-0.287863,6.693103,6.304250,7.189990,-6.160415,-2.695952,-9.524036,-7.354899,8.180732,-7.416989,6.915300,-5.887199,-2.359408,-9.413398,-2.013161,3.689753,-8.716619,0.986875,6.787177,8.338787,8.973544,-3.697282,2.133406,4.459958,-0.626435,-6.602978,6.084909,-6.159777,-2.595814,-2.426365,9.014476,0.778458,-3.336812,4.554552,7.036921,2.983326,-9.147408,-0.586272,9.764684,-6.741524,1.216078,5.818053,2.764057,9.938347,-8.722603,-4.309497,5.678925,7.159630,9.744979,8.308076,4.292265,7.228159,-9.430445,0.972329,1.542254,4.332029,-1.600310,8.863638,9.620617,6.551144,-4.021276,1.324394,-8.774894,-8.689447,2.880485,-2.703858,-0.575965,-9.968267,-5.695710,-8.742990,6.999029,-1.555286,-6.487032,-0.520993,-9.665744,1.204747,6.868928,-6.843271,4.953897,3.964000,-5.955941,-3.268496,0.831716,-5.993623,-1.016031,-1.669249,-5.692466,-2.683903,-1.050959,-4.239705,-2.888742,-4.105153,-9.140831,5.859704,7.783737,-9.143201,0.445715,-7.353388,3.987410,-6.713716,-0.240120,-3.916968,4.787536,9.533157,8.147101,4.747912,-8.505412,9.242775,-8.046871,-2.674339,-2.937629,-7.931264,6.508694,-8.046440,6.079467,3.138280,5.571314,-7.667464,-8.538894,4.995528,-9.819064,9.042315,-2.250847,8.531325,-1.303142,-2.749207,3.453995,-3.823132,0.650300,2.072268,6.396018,-1.161363,-4.715402,8.451387,6.509282,-4.321545,7.028123,-8.817019,5.598517,4.677303,1.514946,-1.595634,-9.317455,-4.651580,7.895620,-7.032371,-6.610431,-4.777998,9.322189,7.088492,-3.009704,-6.236846,1.749145,9.728671,8.277937,-0.339208,-9.364056,9.145077,2.499702,-4.653481,0.496362,6.525871,-8.138687,0.268191,-7.365794,-6.533485,-8.132170,-5.578088,0.602590,-9.437412,-3.881668,1.936698,5.066335,4.770919,-9.076015,-2.689830,-8.738505,3.785722,6.352975,9.889381,9.734227,-0.781874,-5.687063,-8.313514,-6.712068,-5.921422,7.671884,7.433905,-8.902029,-1.952979,-6.749323,5.930741,-1.802211,1.318850,9.738683,3.244513,-5.619903,-9.623614,2.985390,-1.902220,-7.481373,-1.566859,6.958756,-1.324446,3.693219,-6.447107,9.034277,-2.209387,1.200565,7.043398,-3.717015,0.612084,-9.231058,-0.155287,-0.762148,1.386368,1.608791,9.541139,1.764674,5.716021,-7.752778,8.665990,7.226403,9.447191,1.230115,2.179847,-6.519308,0.128947,-6.216507,-0.043052,-9.848953,0.475108,9.462319,-2.740624,5.212058,8.534612,-2.139943,3.271541,5.105485,-5.591804,-5.362071,-7.995636,-0.122001,3.324453,6.530196,-3.415380,-3.433876,-9.729263,-0.251515,-7.998760,-6.588115,8.058303,-9.356593,-9.596835,2.489923,9.051640,-2.694049,-0.394550,6.137446,0.696412,9.130209], dtype = "float64")#candidate|7453|(585,)|const|float64
var_7454 = relay.var("var_7454", dtype = "int16", shape = (450,))#candidate|7454|(450,)|var|int16
call_7452 = relay.TupleGetItem(func_538_call(relay.reshape(const_7453.astype('float64'), [13, 15, 3]), relay.reshape(var_7454.astype('int16'), [450,]), ), 2)
call_7455 = relay.TupleGetItem(func_541_call(relay.reshape(const_7453.astype('float64'), [13, 15, 3]), relay.reshape(var_7454.astype('int16'), [450,]), ), 2)
output = relay.Tuple([uop_7447,call_7452,const_7453,var_7454,])
output2 = relay.Tuple([uop_7449,call_7455,const_7453,var_7454,])
func_7463 = relay.Function([var_7454,], output)
mod['func_7463'] = func_7463
mod = relay.transform.InferType()(mod)
mutated_mod['func_7463'] = func_7463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7464 = relay.var("var_7464", dtype = "int16", shape = (450,))#candidate|7464|(450,)|var|int16
func_7463_call = mutated_mod.get_global_var('func_7463')
call_7465 = func_7463_call(var_7464)
output = call_7465
func_7466 = relay.Function([var_7464], output)
mutated_mod['func_7466'] = func_7466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4882_call = mod.get_global_var('func_4882')
func_4884_call = mutated_mod.get_global_var('func_4884')
call_7486 = relay.TupleGetItem(func_4882_call(), 0)
call_7487 = relay.TupleGetItem(func_4884_call(), 0)
func_5342_call = mod.get_global_var('func_5342')
func_5344_call = mutated_mod.get_global_var('func_5344')
call_7503 = func_5342_call()
call_7504 = func_5342_call()
func_54_call = mod.get_global_var('func_54')
func_57_call = mutated_mod.get_global_var('func_57')
const_7524 = relay.const([[-10,-5,1,-6,-5,-9,5,7,-9,10,-8,2,-1,7,-8,3,-4,-5,-8,-9,-2,-3,10,6,5,-9,3,2,6,9,-8,1,3,-9,9,-4,-6,-1,1,6,-1,8,8,9,-9,1,-3,1,10,-6,8,3,-1,8,10,-7,-1,-7,4,7,6,-3,10,-4,-4,1,-2,-5,9,-4,-9,1,7,3,6,7,7,1,-3,-10,-5,10,7,10,-9,4,5,-10,-5,-4,-4,-5,10,-10,10,10,3,5,-5,6,7,-2,3,-5,-8,1,1,-2,-1,1,-6,-9,3,1,-8,2,4,10,-9,-8,-5,8,5,4,-6,-7,10,-1,1,2,6,-5,-9,10,1,6,6,-9,-6,7,1,-2,2,-3,5,10,-9,-2,1,10,-1,-7,10,10,-2,6,10,2,1,-5,-3,8,2,-2,-5,7,9,-2,4,3,-8,-9,6,2,-9,4,2,3,5,10,-10,-3,-3,-5,9,-4,8,-7,5,4,6,5,1,3,5,-5,10,-1,-4,-3,6,-10,-9,9,-8,-7,10,-4,9,-8,-1,-9,-2,6,-7,-9,-6,-7,7,10,-8,2,10,10,3,6,-10,7,-3,8,-3,5,7,6,-10,3,-5,8,1,7,-8,10,-7,-2,1,2,-6,-5,3,-8,8,-10,6,-8,-8,3,-7,-5,-3,5,-6,9,-8,-6,-6,3,-8,8,-3,-3,3,-8,-2,-7,10,10,-2,10,3,-8,-4,6,-4,-10,-3,9,-10,8,-9,-8,6,-7,-6,8,-6,-10,-7,-4,1,9,6,1,4,9,-2,-4,-4,-9,-9,10,3,-8,8,-3,-8,4,2,-2,-3,-10,10,5,5,6,9,1,-8,2,1,-5,-10,2,2,-6,9,-2,-2,-4,-3,2,6,5,2,-8,-3,-3,1,4,-1,2,8,8,-3,8,-3,-9,6,3,-1,1,5,8,-9,-3,5,-10,-9,3,-3,1,3,-6,-4,-7,3,3,-1,-6,-5,3,-4,3,3,7,-10,1,8,4,-8,1,8,9,-6,2,-6,3,7,-5,-5,6,3,-9,-7,-5,4,6,1,-1,-2,10,9,-8,-9,-9,-5,10,-4,-1,3,-6,3,7,7,10,-3,7,-4,-10,-8,-9,-6,3,7,-3,-1,7,10,9,-4,-9,1,-10,-1,-8,-1,-1,6,-7,9,3]], dtype = "int16")#candidate|7524|(1, 450)|const|int16
call_7523 = relay.TupleGetItem(func_54_call(relay.reshape(const_7524.astype('int16'), [15, 6, 5]), relay.reshape(const_7524.astype('int16'), [15, 6, 5]), ), 0)
call_7525 = relay.TupleGetItem(func_57_call(relay.reshape(const_7524.astype('int16'), [15, 6, 5]), relay.reshape(const_7524.astype('int16'), [15, 6, 5]), ), 0)
output = relay.Tuple([call_7486,call_7503,call_7523,const_7524,])
output2 = relay.Tuple([call_7487,call_7504,call_7525,const_7524,])
func_7535 = relay.Function([], output)
mod['func_7535'] = func_7535
mod = relay.transform.InferType()(mod)
mutated_mod['func_7535'] = func_7535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7535_call = mutated_mod.get_global_var('func_7535')
call_7536 = func_7535_call()
output = call_7536
func_7537 = relay.Function([], output)
mutated_mod['func_7537'] = func_7537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5381_call = mod.get_global_var('func_5381')
func_5382_call = mutated_mod.get_global_var('func_5382')
call_7538 = func_5381_call()
call_7539 = func_5381_call()
output = call_7538
output2 = call_7539
func_7549 = relay.Function([], output)
mod['func_7549'] = func_7549
mod = relay.transform.InferType()(mod)
output = func_7549()
func_7550 = relay.Function([], output)
mutated_mod['func_7550'] = func_7550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6086_call = mod.get_global_var('func_6086')
func_6088_call = mutated_mod.get_global_var('func_6088')
call_7739 = relay.TupleGetItem(func_6086_call(), 2)
call_7740 = relay.TupleGetItem(func_6088_call(), 2)
output = relay.Tuple([call_7739,])
output2 = relay.Tuple([call_7740,])
func_7763 = relay.Function([], output)
mod['func_7763'] = func_7763
mod = relay.transform.InferType()(mod)
output = func_7763()
func_7764 = relay.Function([], output)
mutated_mod['func_7764'] = func_7764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7802 = relay.var("var_7802", dtype = "float32", shape = (12, 7, 12))#candidate|7802|(12, 7, 12)|var|float32
uop_7803 = relay.log10(var_7802.astype('float32')) # shape=(12, 7, 12)
bop_7805 = relay.multiply(uop_7803.astype('uint32'), relay.reshape(var_7802.astype('uint32'), relay.shape_of(uop_7803))) # shape=(12, 7, 12)
uop_7810 = relay.sigmoid(bop_7805.astype('float64')) # shape=(12, 7, 12)
func_2886_call = mod.get_global_var('func_2886')
func_2888_call = mutated_mod.get_global_var('func_2888')
var_7821 = relay.var("var_7821", dtype = "float32", shape = (1600,))#candidate|7821|(1600,)|var|float32
call_7820 = relay.TupleGetItem(func_2886_call(relay.reshape(var_7821.astype('float32'), [16, 10, 10])), 1)
call_7822 = relay.TupleGetItem(func_2888_call(relay.reshape(var_7821.astype('float32'), [16, 10, 10])), 1)
func_6378_call = mod.get_global_var('func_6378')
func_6379_call = mutated_mod.get_global_var('func_6379')
call_7827 = relay.TupleGetItem(func_6378_call(), 1)
call_7828 = relay.TupleGetItem(func_6379_call(), 1)
bop_7838 = relay.right_shift(uop_7810.astype('uint64'), relay.reshape(uop_7803.astype('uint64'), relay.shape_of(uop_7810))) # shape=(12, 7, 12)
func_5714_call = mod.get_global_var('func_5714')
func_5718_call = mutated_mod.get_global_var('func_5718')
const_7844 = relay.const([6.713368,3.209652,2.043416,2.047228,-4.979792,5.480166,4.329236,4.619575,-9.474456,9.353868,-2.537063,-0.736318,5.096640,-7.238553,-3.922280,8.946595,-6.520048,-7.036851,-9.903429,-9.020628,0.165531,0.388166,9.775234,3.382699,-0.174769,-0.240927,-8.651223,-2.614412,-4.991095,-4.990266,-2.517707,-6.407088,-6.372291,-9.430684,4.691071,-1.706142,-3.253798,6.341159,-9.980691,9.393809,8.226562,6.298976,1.352687,-1.700994,9.857668,-8.425827,-2.564241,-1.733173,0.596689,4.286669,8.293040,5.453931,3.243486,2.084361,3.385612,-8.656246,-9.296943,1.469965,-1.491283,5.201913,-0.145877,5.028442,-6.392263,-7.285159,-5.329293,-6.773371,8.826954,3.614857,3.908316,-5.612908,4.929330,1.924023,-9.340652,8.450134,-9.223221,-0.091893,8.250524,-7.757049,9.133304,5.486256,-9.622372,8.663881,-6.548732,7.079353,4.123314,-7.065353,-8.367012,-5.753000,-7.215319,2.951715,-1.901961,-9.989191,7.051244,-5.446537,6.090079,-0.291524,2.072791,7.594494,-1.586228,5.916100,-0.130420,7.544001,-1.895425,1.188004,8.842591,6.402320,6.020989,7.649118,-0.042891,6.550601,-7.896680,-9.668139,-8.843616,4.010042,-1.011204,-5.938407,-6.271672,4.208322,-6.053380,-8.463187,-2.239953,2.367429,4.737967,-2.970266,-6.434807,7.385555], dtype = "float64")#candidate|7844|(126,)|const|float64
var_7845 = relay.var("var_7845", dtype = "int16", shape = (450,))#candidate|7845|(450,)|var|int16
call_7843 = relay.TupleGetItem(func_5714_call(relay.reshape(const_7844.astype('float64'), [126,]), relay.reshape(var_7845.astype('int16'), [450,]), ), 6)
call_7846 = relay.TupleGetItem(func_5718_call(relay.reshape(const_7844.astype('float64'), [126,]), relay.reshape(var_7845.astype('int16'), [450,]), ), 6)
output = relay.Tuple([call_7820,var_7821,call_7827,bop_7838,call_7843,const_7844,var_7845,])
output2 = relay.Tuple([call_7822,var_7821,call_7828,bop_7838,call_7846,const_7844,var_7845,])
func_7847 = relay.Function([var_7802,var_7821,var_7845,], output)
mod['func_7847'] = func_7847
mod = relay.transform.InferType()(mod)
mutated_mod['func_7847'] = func_7847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7847_call = mutated_mod.get_global_var('func_7847')
var_7849 = relay.var("var_7849", dtype = "float32", shape = (12, 7, 12))#candidate|7849|(12, 7, 12)|var|float32
var_7850 = relay.var("var_7850", dtype = "float32", shape = (1600,))#candidate|7850|(1600,)|var|float32
var_7851 = relay.var("var_7851", dtype = "int16", shape = (450,))#candidate|7851|(450,)|var|int16
call_7848 = func_7847_call(var_7849,var_7850,var_7851,)
output = call_7848
func_7852 = relay.Function([var_7849,var_7850,var_7851,], output)
mutated_mod['func_7852'] = func_7852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5594_call = mod.get_global_var('func_5594')
func_5595_call = mutated_mod.get_global_var('func_5595')
call_7861 = func_5594_call()
call_7862 = func_5594_call()
var_7866 = relay.var("var_7866", dtype = "bool", shape = (12, 28))#candidate|7866|(12, 28)|var|bool
bop_7867 = relay.multiply(call_7861.astype('uint32'), var_7866.astype('uint32')) # shape=(12, 28)
bop_7870 = relay.multiply(call_7862.astype('uint32'), var_7866.astype('uint32')) # shape=(12, 28)
output = relay.Tuple([bop_7867,])
output2 = relay.Tuple([bop_7870,])
F = relay.Function([var_7866,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7866,], output2)
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
