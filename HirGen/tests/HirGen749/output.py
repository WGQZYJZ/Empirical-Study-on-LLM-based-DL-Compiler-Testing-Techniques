import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_518 = relay.var("var_518", dtype = "uint64", shape = (2, 5, 6))#candidate|518|(2, 5, 6)|var|uint64
var_519 = relay.var("var_519", dtype = "uint64", shape = (2, 5, 6))#candidate|519|(2, 5, 6)|var|uint64
bop_520 = relay.right_shift(var_518.astype('uint64'), relay.reshape(var_519.astype('uint64'), relay.shape_of(var_518))) # shape=(2, 5, 6)
output = bop_520
output2 = bop_520
func_531 = relay.Function([var_518,var_519,], output)
mod['func_531'] = func_531
mod = relay.transform.InferType()(mod)
mutated_mod['func_531'] = func_531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_531_call = mutated_mod.get_global_var('func_531')
var_533 = relay.var("var_533", dtype = "uint64", shape = (2, 5, 6))#candidate|533|(2, 5, 6)|var|uint64
var_534 = relay.var("var_534", dtype = "uint64", shape = (2, 5, 6))#candidate|534|(2, 5, 6)|var|uint64
call_532 = func_531_call(var_533,var_534,)
output = call_532
func_535 = relay.Function([var_533,var_534,], output)
mutated_mod['func_535'] = func_535
mutated_mod = relay.transform.InferType()(mutated_mod)
var_930 = relay.var("var_930", dtype = "float64", shape = (2, 3, 10))#candidate|930|(2, 3, 10)|var|float64
uop_931 = relay.sqrt(var_930.astype('float64')) # shape=(2, 3, 10)
output = uop_931
output2 = uop_931
func_938 = relay.Function([var_930,], output)
mod['func_938'] = func_938
mod = relay.transform.InferType()(mod)
var_939 = relay.var("var_939", dtype = "float64", shape = (2, 3, 10))#candidate|939|(2, 3, 10)|var|float64
output = func_938(var_939)
func_940 = relay.Function([var_939], output)
mutated_mod['func_940'] = func_940
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1043 = relay.var("var_1043", dtype = "int16", shape = ())#candidate|1043|()|var|int16
var_1044 = relay.var("var_1044", dtype = "int16", shape = (15, 12, 11))#candidate|1044|(15, 12, 11)|var|int16
bop_1045 = relay.maximum(var_1043.astype('int16'), var_1044.astype('int16')) # shape=(15, 12, 11)
func_531_call = mod.get_global_var('func_531')
func_535_call = mutated_mod.get_global_var('func_535')
var_1050 = relay.var("var_1050", dtype = "uint64", shape = (60,))#candidate|1050|(60,)|var|uint64
call_1049 = func_531_call(relay.reshape(var_1050.astype('uint64'), [2, 5, 6]), relay.reshape(var_1050.astype('uint64'), [2, 5, 6]), )
call_1051 = func_531_call(relay.reshape(var_1050.astype('uint64'), [2, 5, 6]), relay.reshape(var_1050.astype('uint64'), [2, 5, 6]), )
func_938_call = mod.get_global_var('func_938')
func_940_call = mutated_mod.get_global_var('func_940')
call_1055 = func_938_call(relay.reshape(var_1050.astype('float64'), [2, 3, 10]))
call_1056 = func_938_call(relay.reshape(var_1050.astype('float64'), [2, 3, 10]))
func_938_call = mod.get_global_var('func_938')
func_940_call = mutated_mod.get_global_var('func_940')
call_1061 = func_938_call(relay.reshape(call_1055.astype('float64'), [2, 3, 10]))
call_1062 = func_938_call(relay.reshape(call_1055.astype('float64'), [2, 3, 10]))
output = relay.Tuple([bop_1045,call_1049,var_1050,call_1055,call_1061,])
output2 = relay.Tuple([bop_1045,call_1051,var_1050,call_1056,call_1062,])
func_1094 = relay.Function([var_1043,var_1044,var_1050,], output)
mod['func_1094'] = func_1094
mod = relay.transform.InferType()(mod)
mutated_mod['func_1094'] = func_1094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1094_call = mutated_mod.get_global_var('func_1094')
var_1096 = relay.var("var_1096", dtype = "int16", shape = ())#candidate|1096|()|var|int16
var_1097 = relay.var("var_1097", dtype = "int16", shape = (15, 12, 11))#candidate|1097|(15, 12, 11)|var|int16
var_1098 = relay.var("var_1098", dtype = "uint64", shape = (60,))#candidate|1098|(60,)|var|uint64
call_1095 = func_1094_call(var_1096,var_1097,var_1098,)
output = call_1095
func_1099 = relay.Function([var_1096,var_1097,var_1098,], output)
mutated_mod['func_1099'] = func_1099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1119 = relay.var("var_1119", dtype = "float64", shape = (16, 16, 5))#candidate|1119|(16, 16, 5)|var|float64
uop_1120 = relay.sin(var_1119.astype('float64')) # shape=(16, 16, 5)
func_531_call = mod.get_global_var('func_531')
func_535_call = mutated_mod.get_global_var('func_535')
var_1124 = relay.var("var_1124", dtype = "uint64", shape = (60,))#candidate|1124|(60,)|var|uint64
call_1123 = func_531_call(relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), )
call_1125 = func_531_call(relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), )
func_531_call = mod.get_global_var('func_531')
func_535_call = mutated_mod.get_global_var('func_535')
call_1132 = func_531_call(relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), )
call_1133 = func_531_call(relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), relay.reshape(var_1124.astype('uint64'), [2, 5, 6]), )
output = relay.Tuple([uop_1120,call_1123,var_1124,call_1132,])
output2 = relay.Tuple([uop_1120,call_1125,var_1124,call_1133,])
func_1145 = relay.Function([var_1119,var_1124,], output)
mod['func_1145'] = func_1145
mod = relay.transform.InferType()(mod)
mutated_mod['func_1145'] = func_1145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1145_call = mutated_mod.get_global_var('func_1145')
var_1147 = relay.var("var_1147", dtype = "float64", shape = (16, 16, 5))#candidate|1147|(16, 16, 5)|var|float64
var_1148 = relay.var("var_1148", dtype = "uint64", shape = (60,))#candidate|1148|(60,)|var|uint64
call_1146 = func_1145_call(var_1147,var_1148,)
output = call_1146
func_1149 = relay.Function([var_1147,var_1148,], output)
mutated_mod['func_1149'] = func_1149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1184 = relay.var("var_1184", dtype = "float64", shape = (12, 1, 16))#candidate|1184|(12, 1, 16)|var|float64
uop_1185 = relay.tan(var_1184.astype('float64')) # shape=(12, 1, 16)
func_531_call = mod.get_global_var('func_531')
func_535_call = mutated_mod.get_global_var('func_535')
var_1191 = relay.var("var_1191", dtype = "uint64", shape = (60,))#candidate|1191|(60,)|var|uint64
call_1190 = func_531_call(relay.reshape(var_1191.astype('uint64'), [2, 5, 6]), relay.reshape(var_1191.astype('uint64'), [2, 5, 6]), )
call_1192 = func_531_call(relay.reshape(var_1191.astype('uint64'), [2, 5, 6]), relay.reshape(var_1191.astype('uint64'), [2, 5, 6]), )
output = relay.Tuple([uop_1185,call_1190,var_1191,])
output2 = relay.Tuple([uop_1185,call_1192,var_1191,])
func_1202 = relay.Function([var_1184,var_1191,], output)
mod['func_1202'] = func_1202
mod = relay.transform.InferType()(mod)
var_1203 = relay.var("var_1203", dtype = "float64", shape = (12, 1, 16))#candidate|1203|(12, 1, 16)|var|float64
var_1204 = relay.var("var_1204", dtype = "uint64", shape = (60,))#candidate|1204|(60,)|var|uint64
output = func_1202(var_1203,var_1204,)
func_1205 = relay.Function([var_1203,var_1204,], output)
mutated_mod['func_1205'] = func_1205
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1492 = relay.var("var_1492", dtype = "float32", shape = (2, 14, 10))#candidate|1492|(2, 14, 10)|var|float32
uop_1493 = relay.acosh(var_1492.astype('float32')) # shape=(2, 14, 10)
output = relay.Tuple([uop_1493,])
output2 = relay.Tuple([uop_1493,])
func_1505 = relay.Function([var_1492,], output)
mod['func_1505'] = func_1505
mod = relay.transform.InferType()(mod)
var_1506 = relay.var("var_1506", dtype = "float32", shape = (2, 14, 10))#candidate|1506|(2, 14, 10)|var|float32
output = func_1505(var_1506)
func_1507 = relay.Function([var_1506], output)
mutated_mod['func_1507'] = func_1507
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1612 = relay.var("var_1612", dtype = "bool", shape = (14, 6, 12))#candidate|1612|(14, 6, 12)|var|bool
var_1613 = relay.var("var_1613", dtype = "bool", shape = (14, 6, 12))#candidate|1613|(14, 6, 12)|var|bool
bop_1614 = relay.logical_and(var_1612.astype('bool'), relay.reshape(var_1613.astype('bool'), relay.shape_of(var_1612))) # shape=(14, 6, 12)
output = bop_1614
output2 = bop_1614
func_1619 = relay.Function([var_1612,var_1613,], output)
mod['func_1619'] = func_1619
mod = relay.transform.InferType()(mod)
var_1620 = relay.var("var_1620", dtype = "bool", shape = (14, 6, 12))#candidate|1620|(14, 6, 12)|var|bool
var_1621 = relay.var("var_1621", dtype = "bool", shape = (14, 6, 12))#candidate|1621|(14, 6, 12)|var|bool
output = func_1619(var_1620,var_1621,)
func_1622 = relay.Function([var_1620,var_1621,], output)
mutated_mod['func_1622'] = func_1622
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1751 = relay.var("var_1751", dtype = "int64", shape = ())#candidate|1751|()|var|int64
var_1752 = relay.var("var_1752", dtype = "int64", shape = (6, 10, 13))#candidate|1752|(6, 10, 13)|var|int64
bop_1753 = relay.add(var_1751.astype('int64'), var_1752.astype('int64')) # shape=(6, 10, 13)
output = relay.Tuple([bop_1753,])
output2 = relay.Tuple([bop_1753,])
func_1756 = relay.Function([var_1751,var_1752,], output)
mod['func_1756'] = func_1756
mod = relay.transform.InferType()(mod)
var_1757 = relay.var("var_1757", dtype = "int64", shape = ())#candidate|1757|()|var|int64
var_1758 = relay.var("var_1758", dtype = "int64", shape = (6, 10, 13))#candidate|1758|(6, 10, 13)|var|int64
output = func_1756(var_1757,var_1758,)
func_1759 = relay.Function([var_1757,var_1758,], output)
mutated_mod['func_1759'] = func_1759
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1981 = relay.const([[[9,-1,-2,-1,9,-6,-2,7,-2,7],[-7,-4,-6,9,-10,-5,-6,7,-3,6],[-4,9,3,6,-6,3,-7,-6,-7,-4],[3,-8,-6,-9,-5,9,9,-5,-7,-8],[-5,8,9,6,-10,-4,10,4,-9,6],[-7,-3,-4,-9,-9,-4,7,6,-10,3],[-3,-3,-9,10,9,1,-1,-2,-3,6],[7,8,-5,-9,7,5,9,4,4,-5],[7,8,-10,-5,-1,-5,-2,-2,7,2]],[[-5,5,-4,1,2,10,2,7,8,3],[4,8,2,3,-1,-5,-3,-10,1,2],[9,-5,9,1,6,7,-5,-6,-2,6],[5,10,6,-4,3,-4,-9,5,3,-5],[1,8,8,-3,-4,-6,4,8,5,-9],[-7,3,10,-4,-6,-1,-5,-3,3,-3],[-6,-8,4,10,-8,-2,-10,1,-4,4],[-7,5,3,5,5,-3,-9,-1,6,4],[8,9,10,-9,-8,-2,-7,-7,6,-6]],[[-9,2,-1,1,-4,-3,9,-2,3,-3],[6,6,-4,-4,4,-3,-1,3,10,1],[-8,-6,-8,8,-2,4,6,-1,-4,3],[7,3,1,-9,-9,-2,-7,-4,9,-8],[-2,-10,4,-1,8,-6,-9,10,2,-10],[-4,-8,3,5,5,-6,8,9,9,8],[-3,-10,-3,2,-4,6,5,8,-9,1],[-8,3,2,8,2,-9,-10,9,3,-9],[-6,-2,1,10,-3,-4,-9,-9,-8,2]],[[-10,-9,2,-4,-3,-10,9,1,-4,-10],[1,9,10,1,-4,-2,-6,7,-10,2],[5,2,6,2,4,8,-7,-7,7,-6],[3,-5,8,-6,4,-2,2,1,-7,9],[-6,-9,5,9,-4,-5,3,-5,-4,1],[-10,5,9,1,10,9,6,10,-2,5],[5,2,-10,1,9,-9,7,1,3,-1],[-2,10,6,1,-10,3,-4,3,1,7],[-6,-9,4,8,-3,-2,-1,5,4,-7]],[[-10,-8,-5,-10,5,-6,-6,5,-6,7],[3,-6,-2,2,-7,-10,9,-5,1,3],[-3,-8,-6,8,5,3,5,-2,2,-2],[-1,8,-2,-6,-8,-10,8,9,10,-5],[-5,3,-8,8,7,9,-4,-9,9,1],[2,8,9,1,-9,4,-5,-5,-10,-6],[-2,-6,-3,-7,10,-10,1,-2,5,10],[10,-7,1,-1,-4,-9,-2,-5,9,7],[-1,-2,5,3,-7,-4,-8,-5,5,-1]],[[3,-5,6,1,-3,-7,-5,7,2,10],[4,8,8,-3,9,2,-4,8,9,7],[8,-6,-2,-3,-2,4,10,6,-5,-1],[-2,8,-9,8,-6,2,1,-6,-1,-7],[-3,-7,-3,1,3,-4,-2,-3,-7,-3],[-7,6,2,-1,1,4,-9,7,5,1],[7,-2,-6,-3,7,-7,-8,-2,-4,-1],[-3,9,7,3,1,9,7,-8,-6,7],[5,-8,4,-3,-5,3,3,-9,7,2]]], dtype = "int64")#candidate|1981|(6, 9, 10)|const|int64
var_1982 = relay.var("var_1982", dtype = "int64", shape = (6, 9, 10))#candidate|1982|(6, 9, 10)|var|int64
bop_1983 = relay.bitwise_xor(const_1981.astype('int64'), relay.reshape(var_1982.astype('int64'), relay.shape_of(const_1981))) # shape=(6, 9, 10)
func_1145_call = mod.get_global_var('func_1145')
func_1149_call = mutated_mod.get_global_var('func_1149')
var_1992 = relay.var("var_1992", dtype = "float64", shape = (1280,))#candidate|1992|(1280,)|var|float64
var_1993 = relay.var("var_1993", dtype = "uint64", shape = (60,))#candidate|1993|(60,)|var|uint64
call_1991 = relay.TupleGetItem(func_1145_call(relay.reshape(var_1992.astype('float64'), [16, 16, 5]), relay.reshape(var_1993.astype('uint64'), [60,]), ), 1)
call_1994 = relay.TupleGetItem(func_1149_call(relay.reshape(var_1992.astype('float64'), [16, 16, 5]), relay.reshape(var_1993.astype('uint64'), [60,]), ), 1)
output = relay.Tuple([bop_1983,call_1991,var_1992,var_1993,])
output2 = relay.Tuple([bop_1983,call_1994,var_1992,var_1993,])
func_1996 = relay.Function([var_1982,var_1992,var_1993,], output)
mod['func_1996'] = func_1996
mod = relay.transform.InferType()(mod)
var_1997 = relay.var("var_1997", dtype = "int64", shape = (6, 9, 10))#candidate|1997|(6, 9, 10)|var|int64
var_1998 = relay.var("var_1998", dtype = "float64", shape = (1280,))#candidate|1998|(1280,)|var|float64
var_1999 = relay.var("var_1999", dtype = "uint64", shape = (60,))#candidate|1999|(60,)|var|uint64
output = func_1996(var_1997,var_1998,var_1999,)
func_2000 = relay.Function([var_1997,var_1998,var_1999,], output)
mutated_mod['func_2000'] = func_2000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2486 = relay.var("var_2486", dtype = "float64", shape = (2, 12, 10))#candidate|2486|(2, 12, 10)|var|float64
uop_2487 = relay.sqrt(var_2486.astype('float64')) # shape=(2, 12, 10)
output = uop_2487
output2 = uop_2487
func_2495 = relay.Function([var_2486,], output)
mod['func_2495'] = func_2495
mod = relay.transform.InferType()(mod)
var_2496 = relay.var("var_2496", dtype = "float64", shape = (2, 12, 10))#candidate|2496|(2, 12, 10)|var|float64
output = func_2495(var_2496)
func_2497 = relay.Function([var_2496], output)
mutated_mod['func_2497'] = func_2497
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2804 = relay.var("var_2804", dtype = "uint16", shape = (12, 6, 16))#candidate|2804|(12, 6, 16)|var|uint16
var_2805 = relay.var("var_2805", dtype = "uint16", shape = (12, 6, 16))#candidate|2805|(12, 6, 16)|var|uint16
bop_2806 = relay.minimum(var_2804.astype('uint16'), relay.reshape(var_2805.astype('uint16'), relay.shape_of(var_2804))) # shape=(12, 6, 16)
output = bop_2806
output2 = bop_2806
func_2821 = relay.Function([var_2804,var_2805,], output)
mod['func_2821'] = func_2821
mod = relay.transform.InferType()(mod)
var_2822 = relay.var("var_2822", dtype = "uint16", shape = (12, 6, 16))#candidate|2822|(12, 6, 16)|var|uint16
var_2823 = relay.var("var_2823", dtype = "uint16", shape = (12, 6, 16))#candidate|2823|(12, 6, 16)|var|uint16
output = func_2821(var_2822,var_2823,)
func_2824 = relay.Function([var_2822,var_2823,], output)
mutated_mod['func_2824'] = func_2824
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3456 = relay.const([[[-1,7,-10,7,-8,4,10,3],[-6,5,-9,-7,8,-1,1,8],[-2,2,-10,5,10,7,5,-1],[2,2,-9,-4,8,-5,9,-1],[-8,3,5,-5,-7,7,4,-2],[4,-2,1,-9,-9,8,-8,3],[1,4,-3,-1,3,2,-5,-8]],[[6,-1,-3,-6,5,-4,-2,-10],[2,10,-3,6,10,5,-2,-6],[2,5,-8,-10,6,7,-1,-2],[-1,8,3,3,-4,9,-1,4],[4,9,-2,-6,-2,-6,-2,-6],[9,8,-10,5,9,-9,1,-6],[-3,-7,-5,-3,10,10,6,-4]],[[9,-8,4,2,1,6,5,9],[8,-2,10,1,-3,-1,-4,7],[-8,-2,-10,6,6,-5,7,-8],[1,9,3,3,-9,-8,-9,8],[-10,10,7,-5,-1,3,-6,4],[-10,1,2,-3,6,6,6,5],[-6,-8,-4,-5,5,2,8,-9]],[[8,4,-1,1,-8,-7,2,-10],[10,3,-3,8,6,-9,7,-3],[-7,-4,-3,8,-1,6,8,4],[-6,-1,-5,6,10,-4,-1,-1],[-5,7,-10,-9,-3,-6,1,-8],[-9,5,-9,-3,-4,7,5,6],[-4,10,-9,7,-6,-2,7,3]],[[10,-7,-8,-9,9,-2,5,-8],[2,-5,7,-4,6,-1,7,-8],[3,-7,8,-7,-1,3,6,4],[-9,8,2,-10,-7,3,6,-2],[-7,-2,-2,-9,-6,10,-6,-10],[3,1,-10,-6,-2,3,-8,-7],[-2,9,-7,-1,-3,-9,-5,-3]],[[8,6,5,-7,10,-6,-4,5],[-3,-4,-3,7,5,-4,-4,-3],[-1,10,-2,6,6,-4,7,10],[4,-4,10,4,7,8,-6,-2],[9,-6,1,-4,-4,-9,8,4],[-5,2,10,-1,-5,-6,9,2],[4,-10,8,1,-10,4,2,-1]],[[-6,10,-10,-3,-9,8,9,-7],[-7,-7,9,-8,8,1,2,5],[-7,-4,-6,-2,5,5,9,6],[-9,3,-1,-10,-5,-7,3,4],[8,6,4,3,7,3,1,4],[-4,-1,9,4,-2,-10,-4,6],[-4,-8,-8,8,-8,-3,-4,-1]],[[5,-3,-3,6,-9,-10,-3,-7],[-9,-7,-7,-4,6,3,6,8],[6,-6,10,4,-10,-4,-3,4],[-7,8,-4,8,2,1,7,-9],[-3,-2,9,-2,-2,-4,9,-6],[-8,10,-9,-3,-2,-8,4,-2],[4,-9,1,4,10,-8,-7,-5]],[[1,5,4,2,2,4,1,4],[3,-8,7,-10,1,7,-4,-1],[8,6,5,9,-10,-5,1,6],[-3,8,8,6,-8,7,5,-7],[-3,-8,-3,-6,-10,-3,8,-4],[-6,10,10,3,-1,10,-6,1],[-3,10,8,8,6,-8,3,-7]],[[6,-2,5,6,6,4,-4,3],[-5,-3,8,-10,7,1,2,8],[5,-4,-7,-8,6,-7,6,10],[-5,-2,-6,-9,2,2,8,-10],[4,-5,6,-6,-3,5,-6,-1],[-9,6,-7,8,-5,-3,-2,5],[-9,-7,-4,-7,7,-8,-8,4]]], dtype = "uint64")#candidate|3456|(10, 7, 8)|const|uint64
var_3457 = relay.var("var_3457", dtype = "uint64", shape = (10, 7, 8))#candidate|3457|(10, 7, 8)|var|uint64
bop_3458 = relay.less_equal(const_3456.astype('bool'), relay.reshape(var_3457.astype('bool'), relay.shape_of(const_3456))) # shape=(10, 7, 8)
uop_3467 = relay.log(const_3456.astype('float32')) # shape=(10, 7, 8)
output = relay.Tuple([bop_3458,uop_3467,])
output2 = relay.Tuple([bop_3458,uop_3467,])
func_3471 = relay.Function([var_3457,], output)
mod['func_3471'] = func_3471
mod = relay.transform.InferType()(mod)
var_3472 = relay.var("var_3472", dtype = "uint64", shape = (10, 7, 8))#candidate|3472|(10, 7, 8)|var|uint64
output = func_3471(var_3472)
func_3473 = relay.Function([var_3472], output)
mutated_mod['func_3473'] = func_3473
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3683 = relay.const([[[4,-5,6,3,-8,-4,-3,-2],[10,-2,-7,7,-7,6,7,-7],[-5,-4,-8,4,1,6,-6,-3],[-4,-5,-3,9,-3,-7,-5,1],[-9,-9,-1,2,-3,-6,-5,-9],[-3,-2,-7,8,3,10,2,-8],[-6,5,-1,9,-5,7,3,-1],[-10,-7,-3,7,-2,4,10,-4]]], dtype = "uint64")#candidate|3683|(1, 8, 8)|const|uint64
var_3684 = relay.var("var_3684", dtype = "uint64", shape = (4, 8, 8))#candidate|3684|(4, 8, 8)|var|uint64
bop_3685 = relay.equal(const_3683.astype('bool'), var_3684.astype('bool')) # shape=(4, 8, 8)
output = relay.Tuple([bop_3685,])
output2 = relay.Tuple([bop_3685,])
func_3692 = relay.Function([var_3684,], output)
mod['func_3692'] = func_3692
mod = relay.transform.InferType()(mod)
var_3693 = relay.var("var_3693", dtype = "uint64", shape = (4, 8, 8))#candidate|3693|(4, 8, 8)|var|uint64
output = func_3692(var_3693)
func_3694 = relay.Function([var_3693], output)
mutated_mod['func_3694'] = func_3694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3805 = relay.var("var_3805", dtype = "uint32", shape = ())#candidate|3805|()|var|uint32
var_3806 = relay.var("var_3806", dtype = "uint32", shape = (12, 16, 6))#candidate|3806|(12, 16, 6)|var|uint32
bop_3807 = relay.add(var_3805.astype('uint32'), var_3806.astype('uint32')) # shape=(12, 16, 6)
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
var_3819 = relay.var("var_3819", dtype = "bool", shape = (1008,))#candidate|3819|(1008,)|var|bool
call_3818 = func_1619_call(relay.reshape(var_3819.astype('bool'), [14, 6, 12]), relay.reshape(var_3819.astype('bool'), [14, 6, 12]), )
call_3820 = func_1619_call(relay.reshape(var_3819.astype('bool'), [14, 6, 12]), relay.reshape(var_3819.astype('bool'), [14, 6, 12]), )
output = relay.Tuple([bop_3807,call_3818,var_3819,])
output2 = relay.Tuple([bop_3807,call_3820,var_3819,])
func_3822 = relay.Function([var_3805,var_3806,var_3819,], output)
mod['func_3822'] = func_3822
mod = relay.transform.InferType()(mod)
mutated_mod['func_3822'] = func_3822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3822_call = mutated_mod.get_global_var('func_3822')
var_3824 = relay.var("var_3824", dtype = "uint32", shape = ())#candidate|3824|()|var|uint32
var_3825 = relay.var("var_3825", dtype = "uint32", shape = (12, 16, 6))#candidate|3825|(12, 16, 6)|var|uint32
var_3826 = relay.var("var_3826", dtype = "bool", shape = (1008,))#candidate|3826|(1008,)|var|bool
call_3823 = func_3822_call(var_3824,var_3825,var_3826,)
output = call_3823
func_3827 = relay.Function([var_3824,var_3825,var_3826,], output)
mutated_mod['func_3827'] = func_3827
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4514 = relay.var("var_4514", dtype = "int32", shape = ())#candidate|4514|()|var|int32
var_4515 = relay.var("var_4515", dtype = "int32", shape = (7, 3, 1))#candidate|4515|(7, 3, 1)|var|int32
bop_4516 = relay.logical_xor(var_4514.astype('int32'), var_4515.astype('int32')) # shape=(7, 3, 1)
func_1094_call = mod.get_global_var('func_1094')
func_1099_call = mutated_mod.get_global_var('func_1099')
const_4526 = relay.const([-3,5,-7,-1,-5,3,-9,10,-10,2,3,3,-6,9,2,8,-6,-3,7,2,-2,-10,3,-1,-4,7,2,3,6,6,3,7,-8,10,4,-7,-8,-5,9,-6,-8,-10,-4,6,6,1,-7,9,-9,-1,3,-9,-7,4,2,-8,-4,1,-1,7,1,9,6,-3,6,-8,-4,-10,1,6,3,-6,-2,4,-3,3,8,-2,-7,-9,-1,-2,2,-3,-5,8,4,-4,10,10,-10,7,-4,-2,6,-3,-6,1,6,-5,-4,8,9,-4,1,-2,6,9,-10,2,4,-4,-10,-10,-8,7,10,-10,7,-7,8,1,9,-6,5,-5,-3,9,4,10,-6,4,2,4,9,-2,-9,3,-5,6,-4,6,10,1,-7,-5,-1,9,-6,5,-4,-2,-9,10,-3,3,9,-7,5,2,2,-6,-8,-6,-8,10,9,-5,-9,2,3,-1,5,1,7,-3,-3,-10,4,5,-9,3,7,6,-5,7,-4,-10,6,8,-7,2,9,-10,10,-6,10,-4,-9,4,9,-4,2,1,-7,3,1,3,7,-5,-1,-3,2,10,8,-7,-9,-1,5,1,2,-6,-7,-4,-4,-9,-10,6,2,5,-1,-8,-3,1,2,2,4,-6,8,-5,-9,-5,-9,-4,6,10,2,-6,-6,7,-9,-1,-8,3,-8,-6,5,7,4,-4,1,-10,1,-1,4,-4,-6,5,-1,-8,9,6,-9,7,-8,-6,4,-3,-1,-3,-10,-8,-1,10,1,2,4,-5,5,-6,4,2,-7,4,-9,3,-3,6,3,-9,4,6,1,10,-5,9,-8,9,5,-3,2,4,6,1,-5,-4,2,-6,-1,-9,3,-6,-8,-6,2,-5,-5,10,-8,1,-1,-4,-4,8,-7,2,4,2,-6,-2,8,-1,-6,-6,-3,-8,1,9,-2,-1,-3,-10,-2,8,-3,-4,-8,3,5,-8,6,5,8,3,1,1,-6,1,-5,5,9,-6,4,3,-1,-10,-9,-6,-6,-6,-2,1,8,-5,-10,1,-8,10,-8,-3,-6,-10,7,1,-5,-4,-6,5,6,-8,-8,10,4,10,-3,-5,-10,-5,8,-2,-4,10,-1,5,2,-8,10,8,7,10,-5,-10,-7,-1,2,-8,2,-8,10,2,5,-4,-7,-1,-10,-6,-5,9,-3,6,4,2,1,-8,-3,5,-2,7,1,6,8,-8,10,4,8,9,-4,-9,-2,8,-9,5,1,-1,-9,-6,10,-1,-9,-4,-5,-10,-5,-5,-6,-10,7,-8,-7,-3,-7,5,-10,8,1,8,-4,-8,7,-3,6,10,3,4,-7,8,5,-1,-10,-6,-10,1,-5,4,2,-7,-5,4,6,-7,4,-7,1,-3,9,-3,6,-5,-3,-2,-8,-3,-7,10,6,8,-5,10,3,6,-5,-10,-3,1,-4,2,4,-5,-4,-6,-4,-2,-9,2,6,-5,7,1,2,7,-4,10,-6,-1,-1,1,-3,-2,-5,-6,2,-3,7,-10,-5,5,-8,9,9,4,-9,5,2,-4,-2,10,-10,-5,-7,3,2,1,-2,-5,10,-1,6,9,-3,-5,-3,-1,7,9,-2,4,-2,-5,-5,5,10,2,-2,-6,-6,-10,-7,2,-10,8,5,6,-8,10,-1,-7,-1,-1,-2,7,-9,8,9,-9,-3,1,-10,-5,-7,-2,-2,-1,9,-5,10,-10,-1,4,10,-9,2,-1,6,-1,-1,-3,-3,7,8,-5,-5,7,3,6,-7,-6,-6,1,1,6,6,-6,-8,1,4,-6,10,5,-5,7,-7,-8,10,-4,3,2,1,-8,-10,5,-4,-4,-2,-8,-1,8,-9,-10,10,-9,-6,-4,-10,4,-1,7,9,2,2,2,-8,-3,9,-6,-9,-1,10,2,8,-2,-6,-6,2,-10,-9,-10,-3,4,6,10,-6,10,8,6,7,-7,-8,-10,3,7,-2,-7,-7,6,2,9,-9,-6,1,3,1,-3,-4,-3,2,-7,4,7,6,7,9,5,-4,-5,4,-5,9,-6,-10,10,-9,-6,2,4,-9,5,6,-6,-3,-7,2,-2,9,-5,-8,-3,-1,-8,2,-8,-3,-9,-5,9,-9,-2,10,1,1,10,-1,6,2,5,-6,-7,8,-7,-2,-8,5,-1,4,-4,-9,6,-7,-4,-6,3,1,-2,7,-3,-6,-9,3,-3,3,3,2,-4,4,6,-4,-4,10,-8,-3,-3,2,-9,-3,1,10,9,-5,-10,8,7,-4,1,-6,8,-7,-8,6,-3,10,8,8,-3,-10,-10,-9,-4,-9,-9,-3,-4,-10,1,-2,7,-10,5,2,-1,-10,-3,-1,2,-2,-6,-9,-7,-5,-7,5,-10,-10,-1,2,7,4,-1,-8,6,5,7,2,-3,2,-5,-7,-10,-1,-9,6,5,7,6,10,-7,3,8,-8,4,2,-7,-6,6,-1,-8,-3,8,10,7,-5,2,-6,3,3,6,-7,-6,1,8,-9,8,3,3,-9,1,5,-3,-6,-5,-4,-6,-3,5,6,-5,-2,-8,2,-8,4,-6,-3,-9,5,-7,6,-1,-6,2,-10,9,-3,-8,-10,5,-4,-10,2,-7,3,8,-9,-8,-5,-9,1,-8,-4,-9,-3,-6,-7,-7,6,-6,9,-10,-2,3,9,4,-9,4,1,6,10,-2,-10,8,2,-9,-9,-7,-5,10,-4,4,7,7,-1,-1,-6,-10,1,-4,-1,1,-10,-10,-1,-1,-5,8,-2,9,9,4,4,-2,1,5,1,-3,4,-9,6,-2,2,-2,-5,10,4,9,-8,-10,-1,3,2,-4,-1,-1,-3,-7,-3,1,-1,-3,-5,-10,7,3,8,-9,-4,-5,8,-2,-1,5,-8,-5,7,4,2,6,8,7,-7,-4,-1,-8,9,9,-10,5,1,9,-7,10,8,1,7,-2,6,5,-7,8,4,-5,2,-2,-9,10,3,7,8,-5,-6,9,-3,1,7,7,5,-6,1,9,-9,5,-1,-3,-10,3,-7,10,-7,1,8,-5,-9,9,1,1,-7,1,-1,-6,-5,9,-1,2,-9,2,-3,2,10,-6,-9,10,-5,3,-7,1,10,-4,10,-9,-2,-10,-7,-1,-6,-9,-3,-3,4,-8,-7,-5,-8,7,6,9,-4,5,1,-2,10,-4,-10,3,4,-7,10,-7,-8,8,-8,-1,6,-8,9,-8,1,4,-8,7,10,-3,3,-9,-4,-6,4,7,-5,-10,4,5,-9,-7,8,9,8,-8,-1,2,6,8,-7,-1,-1,-9,9,10,-5,-5,3,-2,-5,1,-1,-9,-3,6,-3,4,-8,-7,-7,4,-6,-4,2,-9,8,1,5,4,-9,9,7,-6,-6,-1,1,-4,4,-3,4,1,4,-3,4,-8,-8,-6,2,-2,-4,3,8,-10,5,-1,7,-3,6,1,-3,-4,8,10,2,10,4,-9,1,7,7,5,9,-7,5,-4,9,-1,-10,8,-2,-5,-4,-9,8,-10,-1,8,-2,5,-5,6,-9,-10,10,10,-6,8,-1,-4,-4,-1,9,5,6,-1,-10,-2,5,-9,-10,9,-4,-8,8,2,-8,7,4,-1,3,-1,10,-4,-7,-4,-10,5,-1,-8,8,-1,5,-6,-1,1,-10,8,10,-6,5,-6,-2,10,5,-2,-8,-1,-2,-5,-3,-4,-1,-4,-4,-7,-2,-5,-5,10,3,-5,7,-7,3,10,8,-3,-8,-9,-9,3,-9,-8,5,6,-9,10,-7,5,-7,-7,10,-4,-7,3,9,-9,-6,5,-6,7,2,-3,4,-8,-4,-8,5,7,4,9,-5,4,-7,1,9,-9,9,9,-2,6,4,-2,-7,2,-8,7,-9,-5,9,10,-7,-9,2,2,5,-10,4,-9,-1,-4,-9,-2,-1,7,-6,8,-9,-10,2,-3,-9,-7,6,-6,6,8,1,8,-9,-2,3,8,4,2,-9,-5,9,3,-10,2,9,1,-10,-3,-3,3,4,9,1,-6,-6,1,4,1,-5,10,-5,-5,10,-5,3,-3,1,-5,-3,3,1,-5,9,9,-10,-9,9,-1,2,-6,-6,-1,2,1,8,-5,9,-4,-7,-2,1,4,-5,-1,-1,-3,-7,-5,-4,-4,-2,9,-10,-2,7,4,7,-8,-2,-1,-7,1,-3,-4,-5,-7,-7,10,1,-4,8,-6,7,9,-4,-4,7,8,-4,-4,9,7,8,-3,1,-7,7,-6,-9,6,5,8,-7,-1,7,9,-7,-3,-6,-7,-6,-6,10,-9,-4,4,-7,3,-7,3,10,-1,10,5,10,3,-8,9,10,7,-5,5,-1,5,3,-3,4,3,6,10,-1,2,-3,-7,10,-8,5,6,4,-6,-1,-1,1,-9,-3,2,3,1,-2,-10,2,-7,1,-3,-9,3,5,7,9,2,-6,-6,-8,-6,7,5,1,-6,-7,9,-9,-6,-8,2,-8,9,-9,-4,4,-9,3,8,-4,-10,5,-7,-4,9,-5,-1,-5,8,7,-3,1,10,4,9,4,10,-9,-4,-1,6,5,-10,10,-6,-9,8,1,-3,-7,4,2,-3,-3,3,-3,2,6,6,-2,-1,-1,3,6,-6,8,6,-4,-10,-9,10,2,10,4,4,-8,10,-3,-3,9,-3,9,-9,-2,9,4,5,-1,-5,-1,-4,-3,10,5,6,3,5,1,-5,4,6,5,-5,-4,-3,7,-4,10,-6,-7,1,2,-2,-9,-7,2,3,5,-4,-8,6,2,8,5,-9,6,4,5,10,4,-8,-1,4,1,-6,4,-8,1,-10,-10,1,-8,-4,1,-8,-3,1,-9,3,4,-1,-1,-9,-5,-1,10,10,6,-3,-10,-4,-7,-9,2,6,-1,-8,-6,-7,10,5,-1,-9,9,-6,1,1,4,4,-2,-6,7,-7,3,-3,1,2,-3,9,-3,8,-6,1,1,-8,6,-7,-7,6,-8,2,7,1,5,1,-6,1,1,4,9,-6,5,8,10,4,2,-7,-10,-10,-2,-10,-3,-2,2,6,-7,6,6,6,7,5,-5,-10,-3,-7,-3,-3,7,9,-1,-3,-7,-10,3,10,5,-1,8,-5,-2,-5,-1,-1,4,-2,-7,3,5,7,-1,-10,-2,7,10,2,6,9,6,8,10,-6,4,-10,-5,7,-6,2,-7,10,3,-1,9,-6,8,8,-3,-6,6,-6,-7,-8,-9,2,1,3,-6,-5,-2,4,7,1,-6,9,-5,2,-7,4,3,3,-2,10,-1,-6,7,7,10,6,-5,8,9,3,-2,-5,4,1,-4,-5,7,2,-9,-8], dtype = "int16")#candidate|4526|(1980,)|const|int16
var_4527 = relay.var("var_4527", dtype = "uint64", shape = (60,))#candidate|4527|(60,)|var|uint64
call_4525 = relay.TupleGetItem(func_1094_call(relay.reshape(var_4514.astype('int16'), []), relay.reshape(const_4526.astype('int16'), [15, 12, 11]), relay.reshape(var_4527.astype('uint64'), [60,]), ), 1)
call_4528 = relay.TupleGetItem(func_1099_call(relay.reshape(var_4514.astype('int16'), []), relay.reshape(const_4526.astype('int16'), [15, 12, 11]), relay.reshape(var_4527.astype('uint64'), [60,]), ), 1)
func_1996_call = mod.get_global_var('func_1996')
func_2000_call = mutated_mod.get_global_var('func_2000')
var_4546 = relay.var("var_4546", dtype = "int64", shape = (540,))#candidate|4546|(540,)|var|int64
var_4547 = relay.var("var_4547", dtype = "float64", shape = (1280,))#candidate|4547|(1280,)|var|float64
call_4545 = relay.TupleGetItem(func_1996_call(relay.reshape(var_4546.astype('int64'), [6, 9, 10]), relay.reshape(var_4547.astype('float64'), [1280,]), relay.reshape(var_4527.astype('uint64'), [60,]), ), 2)
call_4548 = relay.TupleGetItem(func_2000_call(relay.reshape(var_4546.astype('int64'), [6, 9, 10]), relay.reshape(var_4547.astype('float64'), [1280,]), relay.reshape(var_4527.astype('uint64'), [60,]), ), 2)
func_1202_call = mod.get_global_var('func_1202')
func_1205_call = mutated_mod.get_global_var('func_1205')
var_4560 = relay.var("var_4560", dtype = "float64", shape = (4, 48))#candidate|4560|(4, 48)|var|float64
call_4559 = relay.TupleGetItem(func_1202_call(relay.reshape(var_4560.astype('float64'), [12, 1, 16]), relay.reshape(call_4525.astype('uint64'), [60,]), ), 2)
call_4561 = relay.TupleGetItem(func_1205_call(relay.reshape(var_4560.astype('float64'), [12, 1, 16]), relay.reshape(call_4525.astype('uint64'), [60,]), ), 2)
output = relay.Tuple([bop_4516,call_4525,const_4526,var_4527,call_4545,var_4546,var_4547,call_4559,var_4560,])
output2 = relay.Tuple([bop_4516,call_4528,const_4526,var_4527,call_4548,var_4546,var_4547,call_4561,var_4560,])
func_4568 = relay.Function([var_4514,var_4515,var_4527,var_4546,var_4547,var_4560,], output)
mod['func_4568'] = func_4568
mod = relay.transform.InferType()(mod)
var_4569 = relay.var("var_4569", dtype = "int32", shape = ())#candidate|4569|()|var|int32
var_4570 = relay.var("var_4570", dtype = "int32", shape = (7, 3, 1))#candidate|4570|(7, 3, 1)|var|int32
var_4571 = relay.var("var_4571", dtype = "uint64", shape = (60,))#candidate|4571|(60,)|var|uint64
var_4572 = relay.var("var_4572", dtype = "int64", shape = (540,))#candidate|4572|(540,)|var|int64
var_4573 = relay.var("var_4573", dtype = "float64", shape = (1280,))#candidate|4573|(1280,)|var|float64
var_4574 = relay.var("var_4574", dtype = "float64", shape = (4, 48))#candidate|4574|(4, 48)|var|float64
output = func_4568(var_4569,var_4570,var_4571,var_4572,var_4573,var_4574,)
func_4575 = relay.Function([var_4569,var_4570,var_4571,var_4572,var_4573,var_4574,], output)
mutated_mod['func_4575'] = func_4575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5106 = relay.var("var_5106", dtype = "int64", shape = (5, 2, 7))#candidate|5106|(5, 2, 7)|var|int64
var_5107 = relay.var("var_5107", dtype = "int64", shape = (5, 2, 7))#candidate|5107|(5, 2, 7)|var|int64
bop_5108 = relay.bitwise_xor(var_5106.astype('int64'), relay.reshape(var_5107.astype('int64'), relay.shape_of(var_5106))) # shape=(5, 2, 7)
var_5111 = relay.var("var_5111", dtype = "int64", shape = (5, 2, 7))#candidate|5111|(5, 2, 7)|var|int64
bop_5112 = relay.bitwise_and(var_5107.astype('uint32'), relay.reshape(var_5111.astype('uint32'), relay.shape_of(var_5107))) # shape=(5, 2, 7)
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
var_5116 = relay.var("var_5116", dtype = "bool", shape = (1, 1008))#candidate|5116|(1, 1008)|var|bool
call_5115 = func_1619_call(relay.reshape(var_5116.astype('bool'), [14, 6, 12]), relay.reshape(var_5116.astype('bool'), [14, 6, 12]), )
call_5117 = func_1619_call(relay.reshape(var_5116.astype('bool'), [14, 6, 12]), relay.reshape(var_5116.astype('bool'), [14, 6, 12]), )
uop_5119 = relay.rsqrt(bop_5108.astype('float64')) # shape=(5, 2, 7)
func_1094_call = mod.get_global_var('func_1094')
func_1099_call = mutated_mod.get_global_var('func_1099')
var_5125 = relay.var("var_5125", dtype = "int16", shape = ())#candidate|5125|()|var|int16
var_5126 = relay.var("var_5126", dtype = "int16", shape = (1980,))#candidate|5126|(1980,)|var|int16
var_5127 = relay.var("var_5127", dtype = "uint64", shape = (60,))#candidate|5127|(60,)|var|uint64
call_5124 = relay.TupleGetItem(func_1094_call(relay.reshape(var_5125.astype('int16'), []), relay.reshape(var_5126.astype('int16'), [15, 12, 11]), relay.reshape(var_5127.astype('uint64'), [60,]), ), 2)
call_5128 = relay.TupleGetItem(func_1099_call(relay.reshape(var_5125.astype('int16'), []), relay.reshape(var_5126.astype('int16'), [15, 12, 11]), relay.reshape(var_5127.astype('uint64'), [60,]), ), 2)
output = relay.Tuple([bop_5112,call_5115,var_5116,uop_5119,call_5124,var_5125,var_5126,var_5127,])
output2 = relay.Tuple([bop_5112,call_5117,var_5116,uop_5119,call_5128,var_5125,var_5126,var_5127,])
func_5142 = relay.Function([var_5106,var_5107,var_5111,var_5116,var_5125,var_5126,var_5127,], output)
mod['func_5142'] = func_5142
mod = relay.transform.InferType()(mod)
var_5143 = relay.var("var_5143", dtype = "int64", shape = (5, 2, 7))#candidate|5143|(5, 2, 7)|var|int64
var_5144 = relay.var("var_5144", dtype = "int64", shape = (5, 2, 7))#candidate|5144|(5, 2, 7)|var|int64
var_5145 = relay.var("var_5145", dtype = "int64", shape = (5, 2, 7))#candidate|5145|(5, 2, 7)|var|int64
var_5146 = relay.var("var_5146", dtype = "bool", shape = (1, 1008))#candidate|5146|(1, 1008)|var|bool
var_5147 = relay.var("var_5147", dtype = "int16", shape = ())#candidate|5147|()|var|int16
var_5148 = relay.var("var_5148", dtype = "int16", shape = (1980,))#candidate|5148|(1980,)|var|int16
var_5149 = relay.var("var_5149", dtype = "uint64", shape = (60,))#candidate|5149|(60,)|var|uint64
output = func_5142(var_5143,var_5144,var_5145,var_5146,var_5147,var_5148,var_5149,)
func_5150 = relay.Function([var_5143,var_5144,var_5145,var_5146,var_5147,var_5148,var_5149,], output)
mutated_mod['func_5150'] = func_5150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5641 = relay.var("var_5641", dtype = "float64", shape = (5, 2, 16))#candidate|5641|(5, 2, 16)|var|float64
uop_5642 = relay.sinh(var_5641.astype('float64')) # shape=(5, 2, 16)
func_1756_call = mod.get_global_var('func_1756')
func_1759_call = mutated_mod.get_global_var('func_1759')
var_5660 = relay.var("var_5660", dtype = "int64", shape = ())#candidate|5660|()|var|int64
const_5661 = relay.const([-2,9,-3,-2,8,2,-2,5,-9,-9,-4,-8,-1,8,-1,8,-7,5,-3,-2,6,5,10,-2,-8,8,1,-9,-6,2,1,1,6,7,4,2,-5,8,6,-6,10,-4,-4,5,1,7,7,1,-5,-3,-10,-9,-4,2,-4,2,-4,6,1,-8,-9,6,3,9,6,7,9,-2,-10,10,-3,-9,-9,7,-8,-4,-9,5,6,10,-6,-1,-10,5,-7,5,9,1,10,-10,2,-5,4,5,-4,5,1,-4,-9,4,-7,-8,-4,4,6,2,8,8,-9,-4,-7,4,3,2,8,9,-4,10,5,-2,10,8,-3,-9,-1,-7,2,-8,-7,6,-6,-1,-4,-6,6,2,4,-3,-8,9,-5,-8,6,-1,-6,-10,-4,3,-3,6,9,-3,-8,9,-9,5,-5,-1,9,-5,1,-9,10,2,3,3,8,6,-4,-1,-5,9,1,10,3,7,5,-8,2,-8,-10,10,9,-3,2,6,-2,5,4,-3,3,1,-10,2,-1,-6,3,8,-1,-3,-6,-8,1,-2,-1,1,7,-3,-1,8,9,-2,1,2,-10,6,-3,4,2,-8,1,8,-1,6,9,-5,-9,9,-6,5,-6,-2,7,-3,-10,-1,-2,10,1,-7,-9,7,9,9,8,1,-6,5,1,-10,2,-3,-10,10,-8,-2,-1,-4,-6,8,-8,10,-4,-7,2,5,1,-8,10,2,9,4,2,2,2,2,9,-3,-6,7,8,-3,1,-9,1,10,7,10,1,-7,-10,-4,-2,3,7,-5,-3,5,-10,-6,8,-1,-9,4,2,4,2,-4,-4,2,8,-10,6,6,10,8,-7,4,-1,7,-2,9,6,-10,-10,-4,10,9,9,-5,-7,-8,-4,-2,1,-10,8,-8,-1,-7,-1,-7,-6,10,-2,-4,-7,-3,5,6,3,-10,3,9,4,-7,8,-7,-10,2,9,-1,10,-7,-9,2,7,5,8,6,-2,9,8,-6,3,10,-4,10,5,1,-8,-8,-3,-7,-6,4,-7,-10,7,3,4,3,6,-3,9,-7,-5,4,-7,-8,7,5,-5,10,8,3,1,-1,-7,10,-8,-5,-3,10,9,6,-2,-1,-3,10,-4,-7,-6,2,3,-1,2,-4,2,-6,6,8,-3,6,10,1,-8,1,-7,9,-6,10,6,-4,2,3,1,7,-2,2,-10,8,-1,1,-1,-7,3,-6,3,-9,-9,4,-6,6,5,-10,2,4,6,-1,-8,-5,-8,-1,-10,-6,7,-8,3,10,1,5,-7,-7,4,1,8,4,6,7,-10,-4,-4,-9,-4,7,1,7,10,-3,3,8,-10,7,2,2,8,-10,-8,-9,7,8,-5,6,-10,-2,4,6,4,10,9,9,-9,8,-7,-10,3,4,4,5,-10,-8,-9,-8,10,-1,1,-6,9,10,3,2,-9,-3,-6,-8,7,1,-2,1,9,3,-1,10,5,8,9,3,6,-10,8,1,6,3,2,-2,-5,-9,-3,8,9,5,8,8,6,6,-8,1,-8,-1,-8,1,5,-4,1,6,10,9,-1,-1,5,-3,4,-4,-8,-5,8,-4,8,-3,9,-10,-1,6,6,-1,7,-3,-9,5,5,-6,8,6,-7,6,8,-5,-6,1,8,-4,-7,6,-7,-3,-5,-3,-10,-10,8,3,3,-5,10,-3,-9,5,-4,-1,-4,-1,-7,1,-5,-6,-10,-9,8,-1,1,7,1,-7,3,-5,-4,7,3,1,-10,1,4,2,-3,10,-9,3,9,6,-9,10,-9,7,4,10,-2,5,-10,-10,3,6,-7,3,-10,-9,-10,-2,-5,-1,-6,-4,-1,-4,9,3,-4,-6,-9,-8,-8,7,3,8,-10,-6,9,5,-2,-10,-5,-10,1,1,-5,-6,5,2,5,-5,-1,1,4,10,5,4,3,10,-2,-4,1,1,-3,3,6,-3,2,7,-10,-9,-8,-6,8,7,-10,-10,-10,6,-5,3,8,8,-2,5,1,10,8,2,-3,-8,9,3,-9,5,9,-7,6,6,-8,3,-4,1,-8,-9,-2,-5,5,2,-10,-9], dtype = "int64")#candidate|5661|(780,)|const|int64
call_5659 = relay.TupleGetItem(func_1756_call(relay.reshape(var_5660.astype('int64'), []), relay.reshape(const_5661.astype('int64'), [6, 10, 13]), ), 0)
call_5662 = relay.TupleGetItem(func_1759_call(relay.reshape(var_5660.astype('int64'), []), relay.reshape(const_5661.astype('int64'), [6, 10, 13]), ), 0)
func_1145_call = mod.get_global_var('func_1145')
func_1149_call = mutated_mod.get_global_var('func_1149')
var_5664 = relay.var("var_5664", dtype = "float64", shape = (1280,))#candidate|5664|(1280,)|var|float64
var_5665 = relay.var("var_5665", dtype = "uint64", shape = (30, 2))#candidate|5665|(30, 2)|var|uint64
call_5663 = relay.TupleGetItem(func_1145_call(relay.reshape(var_5664.astype('float64'), [16, 16, 5]), relay.reshape(var_5665.astype('uint64'), [60,]), ), 0)
call_5666 = relay.TupleGetItem(func_1149_call(relay.reshape(var_5664.astype('float64'), [16, 16, 5]), relay.reshape(var_5665.astype('uint64'), [60,]), ), 0)
uop_5668 = relay.acosh(var_5664.astype('float32')) # shape=(1280,)
output = relay.Tuple([uop_5642,call_5659,var_5660,const_5661,call_5663,var_5665,uop_5668,])
output2 = relay.Tuple([uop_5642,call_5662,var_5660,const_5661,call_5666,var_5665,uop_5668,])
func_5673 = relay.Function([var_5641,var_5660,var_5664,var_5665,], output)
mod['func_5673'] = func_5673
mod = relay.transform.InferType()(mod)
var_5674 = relay.var("var_5674", dtype = "float64", shape = (5, 2, 16))#candidate|5674|(5, 2, 16)|var|float64
var_5675 = relay.var("var_5675", dtype = "int64", shape = ())#candidate|5675|()|var|int64
var_5676 = relay.var("var_5676", dtype = "float64", shape = (1280,))#candidate|5676|(1280,)|var|float64
var_5677 = relay.var("var_5677", dtype = "uint64", shape = (30, 2))#candidate|5677|(30, 2)|var|uint64
output = func_5673(var_5674,var_5675,var_5676,var_5677,)
func_5678 = relay.Function([var_5674,var_5675,var_5676,var_5677,], output)
mutated_mod['func_5678'] = func_5678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6286 = relay.var("var_6286", dtype = "uint32", shape = (12, 11, 16))#candidate|6286|(12, 11, 16)|var|uint32
var_6287 = relay.var("var_6287", dtype = "uint32", shape = (12, 11, 16))#candidate|6287|(12, 11, 16)|var|uint32
bop_6288 = relay.bitwise_and(var_6286.astype('uint32'), relay.reshape(var_6287.astype('uint32'), relay.shape_of(var_6286))) # shape=(12, 11, 16)
func_4568_call = mod.get_global_var('func_4568')
func_4575_call = mutated_mod.get_global_var('func_4575')
const_6296 = relay.const(4, dtype = "int32")#candidate|6296|()|const|int32
var_6297 = relay.var("var_6297", dtype = "int32", shape = (21,))#candidate|6297|(21,)|var|int32
var_6298 = relay.var("var_6298", dtype = "uint64", shape = (60,))#candidate|6298|(60,)|var|uint64
var_6299 = relay.var("var_6299", dtype = "int64", shape = (540, 1))#candidate|6299|(540, 1)|var|int64
var_6300 = relay.var("var_6300", dtype = "float64", shape = (320, 4))#candidate|6300|(320, 4)|var|float64
var_6301 = relay.var("var_6301", dtype = "float64", shape = (192,))#candidate|6301|(192,)|var|float64
call_6295 = relay.TupleGetItem(func_4568_call(relay.reshape(const_6296.astype('int32'), []), relay.reshape(var_6297.astype('int32'), [7, 3, 1]), relay.reshape(var_6298.astype('uint64'), [60,]), relay.reshape(var_6299.astype('int64'), [540,]), relay.reshape(var_6300.astype('float64'), [1280,]), relay.reshape(var_6301.astype('float64'), [4, 48]), ), 8)
call_6302 = relay.TupleGetItem(func_4575_call(relay.reshape(const_6296.astype('int32'), []), relay.reshape(var_6297.astype('int32'), [7, 3, 1]), relay.reshape(var_6298.astype('uint64'), [60,]), relay.reshape(var_6299.astype('int64'), [540,]), relay.reshape(var_6300.astype('float64'), [1280,]), relay.reshape(var_6301.astype('float64'), [4, 48]), ), 8)
output = relay.Tuple([bop_6288,call_6295,const_6296,var_6297,var_6298,var_6299,var_6300,var_6301,])
output2 = relay.Tuple([bop_6288,call_6302,const_6296,var_6297,var_6298,var_6299,var_6300,var_6301,])
func_6309 = relay.Function([var_6286,var_6287,var_6297,var_6298,var_6299,var_6300,var_6301,], output)
mod['func_6309'] = func_6309
mod = relay.transform.InferType()(mod)
mutated_mod['func_6309'] = func_6309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6309_call = mutated_mod.get_global_var('func_6309')
var_6311 = relay.var("var_6311", dtype = "uint32", shape = (12, 11, 16))#candidate|6311|(12, 11, 16)|var|uint32
var_6312 = relay.var("var_6312", dtype = "uint32", shape = (12, 11, 16))#candidate|6312|(12, 11, 16)|var|uint32
var_6313 = relay.var("var_6313", dtype = "int32", shape = (21,))#candidate|6313|(21,)|var|int32
var_6314 = relay.var("var_6314", dtype = "uint64", shape = (60,))#candidate|6314|(60,)|var|uint64
var_6315 = relay.var("var_6315", dtype = "int64", shape = (540, 1))#candidate|6315|(540, 1)|var|int64
var_6316 = relay.var("var_6316", dtype = "float64", shape = (320, 4))#candidate|6316|(320, 4)|var|float64
var_6317 = relay.var("var_6317", dtype = "float64", shape = (192,))#candidate|6317|(192,)|var|float64
call_6310 = func_6309_call(var_6311,var_6312,var_6313,var_6314,var_6315,var_6316,var_6317,)
output = call_6310
func_6318 = relay.Function([var_6311,var_6312,var_6313,var_6314,var_6315,var_6316,var_6317,], output)
mutated_mod['func_6318'] = func_6318
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6747 = relay.const([[[8.085686,4.935326,-9.468211,5.924269,5.044459,7.220363,-2.943699],[-8.053763,-7.135516,6.050652,1.730745,-6.299675,-3.997654,1.684509],[3.392405,-2.440350,2.807605,5.130000,-6.150176,-6.056916,7.279982],[-2.960367,9.000752,9.316146,2.807345,-0.822659,-2.859375,-4.206356],[-3.644316,-4.102557,-1.906241,-6.746657,-2.343136,6.319702,-0.691640],[-2.924489,-4.051834,-0.866742,2.942088,3.818623,-6.000662,-3.253190],[-5.710708,3.392601,-0.080492,-7.346599,7.649717,-8.995726,-6.769576]],[[-1.129517,0.453732,3.114290,4.443507,-2.663424,1.932789,-8.313141],[6.806729,-2.069675,6.768124,-3.963526,0.065932,-6.661383,8.845583],[-4.788945,2.111891,-1.441000,0.429781,-0.056404,6.411166,2.377815],[-7.195953,-7.031472,-1.240434,2.638716,2.966355,7.708096,-2.681351],[9.227150,-0.782991,3.219117,-8.246861,9.511452,5.831107,2.925495],[-5.385329,1.503938,-2.227716,-4.148329,-2.213038,-5.474691,7.454852],[-9.235840,9.823237,5.469331,6.199334,9.848879,-5.108448,0.189038]],[[-6.012990,6.735311,-5.009010,4.309754,-0.226872,9.533572,1.248638],[-2.756819,-1.665783,-7.909256,-0.613045,8.793193,1.516560,-4.223258],[6.342557,3.448123,-7.259006,-4.680588,-1.317602,4.586635,9.973672],[8.520578,-3.050000,6.671729,3.046520,-6.197075,2.705207,4.166364],[2.551968,8.328900,-8.168696,-7.513499,1.895083,7.786038,6.879289],[-6.035802,2.868512,0.833683,-8.047010,-2.575649,6.640945,8.639082],[9.070903,3.186309,-0.775720,5.431210,1.415486,0.309601,5.538011]]], dtype = "float64")#candidate|6747|(3, 7, 7)|const|float64
uop_6748 = relay.log(const_6747.astype('float64')) # shape=(3, 7, 7)
output = relay.Tuple([uop_6748,])
output2 = relay.Tuple([uop_6748,])
func_6751 = relay.Function([], output)
mod['func_6751'] = func_6751
mod = relay.transform.InferType()(mod)
mutated_mod['func_6751'] = func_6751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mutated_mod.get_global_var('func_6751')
call_6752 = func_6751_call()
output = call_6752
func_6753 = relay.Function([], output)
mutated_mod['func_6753'] = func_6753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_6767 = relay.TupleGetItem(func_6751_call(), 0)
call_6768 = relay.TupleGetItem(func_6753_call(), 0)
func_5673_call = mod.get_global_var('func_5673')
func_5678_call = mutated_mod.get_global_var('func_5678')
const_6777 = relay.const([-2.611568,-7.604625,9.976948,2.859856,-9.076864,-0.967367,-7.026418,-1.500138,-0.983531,9.630647,-7.213534,9.207315,-1.095075,5.232764,9.442233,-5.574224,-2.270199,0.248196,-7.614465,-6.526764,-0.739075,-9.082105,-9.418045,-8.538234,-2.275653,7.696184,9.857060,9.969232,4.735939,7.762491,-0.979846,-0.448695,-0.526438,-0.918884,3.378502,7.083610,0.347436,-2.184337,7.539456,-6.418405,6.203694,-5.283911,-7.737790,-0.121545,-4.754083,-2.496644,-5.202915,0.064628,-8.772007,6.438115,-9.085414,1.055359,-4.422371,2.780508,6.827693,0.685755,4.592986,5.633159,-9.824863,2.390255,-7.631195,6.951477,8.096306,5.773863,-9.108706,7.067511,-1.903844,-8.108819,-4.658299,-3.072324,1.734310,-3.846171,5.163191,-4.749285,-0.115700,8.381211,5.125868,1.714213,0.304590,-1.062552,8.378088,8.133888,6.668114,5.107951,6.300415,1.004657,7.305434,-0.201635,7.867947,-6.194170,-1.330079,-7.065664,-0.316821,-4.723621,0.477477,5.299895,-1.731287,-3.742292,-5.008656,-9.188524,6.052736,-5.350503,2.503670,8.018855,8.388633,-5.422687,8.059452,8.857826,-2.189402,-1.091306,7.813610,0.728078,-5.550246,8.698449,7.347079,-4.338691,3.361242,5.709900,9.803641,0.953409,6.477050,7.361663,8.196665,-3.431725,-3.547497,7.151473,1.882761,-1.320240,-2.927690,-6.734404,8.063943,-5.278469,-9.811804,1.787196,-6.304576,-7.205605,7.404099,4.632684,3.399450,-7.210397,-0.533736,1.415098,-7.691153,5.486842,2.622650,-2.680898,-8.594373,4.793451,7.297267,7.208073,1.282991,4.023423,9.534921,4.180414,-5.788134,-6.627202,4.539488,-0.423268,8.684643,-6.001360], dtype = "float64")#candidate|6777|(160,)|const|float64
var_6778 = relay.var("var_6778", dtype = "int64", shape = ())#candidate|6778|()|var|int64
const_6779 = relay.const([2.127903,-2.252461,3.547151,-2.701029,-9.332430,4.472683,-0.695492,7.140578,-4.583901,-8.824193,5.143363,-6.662591,-5.367052,-6.151630,8.940221,-1.440544,-6.422809,1.987753,3.200850,-7.735501,7.727055,4.577217,-6.495385,7.158593,-3.410929,4.503627,4.079360,3.622965,-6.335640,-4.123248,-9.261506,-3.363212,8.436861,-9.096039,-8.092757,-5.093985,-9.040337,4.529008,-9.076197,4.685521,9.610753,-0.954197,-4.071257,-2.278412,-9.200370,-1.396641,-6.523958,7.981941,9.617997,-2.324227,0.494230,0.538589,-2.568345,-3.024628,7.079866,7.055558,-5.201915,-8.953765,-3.996871,-8.193130,1.161593,9.385437,6.159575,2.008596,-2.250638,-9.768519,-7.143156,2.038347,5.497016,7.167009,4.235249,3.287116,8.796759,-1.199957,-7.986629,-0.157780,7.996336,1.978563,-6.605316,5.888782,-4.696385,-2.015970,-1.337318,-3.238290,2.892025,-9.821583,-6.988717,3.255463,1.462937,3.436321,-3.440019,4.570037,4.634519,-9.766855,4.067012,-9.154140,-1.959661,-2.778493,-2.074530,-1.197551,8.025155,-7.589812,-6.955001,4.684509,0.136653,3.356730,-3.694170,-1.674867,-1.970897,6.298706,-1.210010,6.238017,1.324401,6.959145,-6.966528,2.718148,8.007318,-8.769969,8.732194,5.787209,-0.609063,-2.205767,-7.382801,0.356764,-2.998305,-7.255415,-4.561134,6.682118,-8.865443,-9.964783,-5.009625,-1.853199,8.570614,2.352573,-6.217030,-0.450700,4.924507,3.838548,7.095673,-9.212618,0.016847,-0.031815,2.090469,8.672425,5.028065,-3.564271,-4.048511,1.272380,7.373317,-7.865471,5.100836,2.471614,-9.193791,-2.969367,5.982050,5.576012,-4.101576,-6.971733,4.341162,9.879851,8.473598,-2.444518,-3.062646,-4.578500,-1.650770,7.766542,8.029262,-1.193692,7.654054,7.950783,-3.794996,2.258013,-4.336748,-1.990066,-5.760699,-1.040340,3.039636,0.872884,-0.433312,-2.630441,-3.459029,4.785998,-9.769414,2.428742,-7.881117,-3.651809,5.916170,6.498508,2.343685,1.335303,2.233412,-6.653203,-6.607910,-1.217182,6.546483,9.388792,-7.104952,0.832599,9.244145,-7.327890,8.955668,-9.706379,0.466501,-0.237842,1.605908,-2.176041,-7.694279,8.867280,-7.596862,1.172965,-9.455083,3.480326,6.867760,5.872402,-5.864288,5.487145,-4.048755,-9.779191,1.999981,8.371242,8.089894,-0.609383,-3.779567,-3.668839,8.001496,-9.040027,0.011145,8.668664,-2.756909,6.394800,-7.130855,-0.876583,-6.512792,-6.652758,6.685262,-7.384686,8.251254,-6.757337,-5.650179,-2.365418,8.880267,-0.826295,0.575551,4.409391,-0.582178,-0.086426,3.416539,-8.555002,9.164925,-8.746953,-1.081049,7.698572,2.489965,8.031909,8.351988,6.339803,-1.745677,0.416456,2.911941,6.945510,2.024110,1.799653,-4.625679,-3.749632,-6.576124,-1.138267,2.990397,1.500418,-0.494140,-1.693598,-7.159615,-6.064104,8.515633,-4.949100,-8.225645,5.876329,9.600388,8.528895,-0.509745,-1.978000,-1.131833,8.759453,-5.476505,-6.112900,1.319441,-0.471406,-4.144923,-1.786786,-9.326246,2.874550,-7.820301,-1.042311,3.953119,6.538138,4.192930,-5.067366,-9.925605,1.833897,-2.122001,1.827868,6.981900,-2.477305,-8.883349,2.585106,2.235999,-3.552358,4.525230,-9.437338,-1.975461,-2.024957,7.940349,3.594146,-2.305541,-0.460213,-8.033197,-7.775920,-1.999121,1.839951,8.580442,4.905945,3.039933,-4.486456,6.505899,8.344173,-1.623706,6.731519,1.321738,-6.672152,-2.427382,-6.552060,-2.010588,-8.273166,6.501796,-0.476018,-1.774651,-9.278121,5.993061,9.545715,0.588271,-8.326895,-0.439049,6.356173,-9.877625,-0.749188,-3.863124,4.742634,0.553580,1.982848,4.997768,-8.290837,-2.343141,-7.571664,0.599173,-9.783042,-0.176380,6.608613,-9.885805,-8.783482,-2.759242,8.429447,-4.317806,2.076554,-1.397637,-2.437340,-1.548045,-5.097991,5.390568,-0.363143,-8.760255,4.677021,2.900001,1.585278,9.317893,-0.299021,-6.976028,2.542036,-0.976169,1.287257,9.821119,5.364183,-8.968391,-0.187734,-0.163854,-6.226360,1.890104,5.427999,-6.300521,6.337024,1.026873,7.433745,6.500660,-6.409098,-6.765729,4.092247,9.829174,9.846866,-7.407625,-9.809259,8.440255,3.706768,-5.678222,1.290596,9.866737,8.253425,4.960604,5.667668,6.588307,-4.496377,7.432002,1.454306,-9.621632,-1.901011,1.689810,8.722522,1.235148,5.727543,-1.063845,6.117822,8.451705,-8.737591,7.723243,-3.528042,3.651928,-5.282198,-8.586140,8.251738,1.632140,7.789909,-1.621180,2.302737,6.043626,-6.238595,3.412546,1.314032,-8.387625,0.415415,1.776964,-7.663199,9.961640,1.799247,-2.763068,-1.555175,-0.826847,-6.087029,2.441586,3.900813,1.397581,-0.152099,5.279326,7.788019,6.885620,4.888864,-8.810975,2.954519,5.439432,0.455600,3.459317,0.714216,5.746409,8.540700,0.523762,6.981801,-6.284367,1.522399,-6.333425,2.498751,-0.255931,-2.524535,-5.115387,-2.587544,2.632544,8.987615,8.493256,-9.254489,5.801635,0.003234,-9.912833,5.890577,-9.615715,-3.871038,8.261471,-2.955382,1.145930,1.976183,-0.673363,7.442836,1.284833,2.727856,0.979861,-3.431422,8.508206,5.945738,-2.493321,-3.941877,5.284179,1.780303,-3.482731,-5.032073,4.704255,9.271198,8.946513,6.514684,6.751446,-9.509867,-7.735660,2.782929,-0.003937,-6.651940,9.855880,-8.895012,2.330846,-7.863071,3.787098,0.850092,-9.412129,6.456099,2.191466,-8.353454,9.892172,2.038733,2.084964,1.393036,2.408965,6.224920,-7.849810,-2.314046,5.324303,7.831349,4.368824,3.346649,2.993431,-8.816482,4.227168,6.094047,4.371932,8.623053,-5.430660,-4.430409,-0.921987,-1.461075,1.771924,-8.314573,2.787852,-6.565456,7.843250,-3.035658,-1.563526,0.779901,-8.148651,-6.255024,-1.108744,-0.756044,-2.442021,-4.248996,-8.264619,3.828919,2.458122,3.900241,9.081492,-4.809755,6.756515,3.099954,5.621450,-7.953877,6.090937,8.327606,-2.535451,-8.941018,-1.370355,5.128171,-2.324586,4.020478,-7.738092,-2.318284,-9.168986,-4.700129,-2.839588,9.463720,7.069825,9.373903,-0.308917,-8.189677,-5.122559,5.543336,1.917029,-1.641449,7.309391,-6.650874,-9.684790,1.572695,0.936330,-4.707811,8.394393,6.355379,2.227606,3.224650,5.412394,-7.258841,3.885519,-3.283075,-4.281004,-3.295307,-7.032518,-5.573910,5.545764,4.598139,7.323255,-7.474648,1.289531,1.530690,-5.477649,-6.300311,-2.449178,-6.335526,-2.392448,4.312694,0.209284,-9.033685,-0.048861,-0.566163,-3.344005,-7.955212,8.303975,-4.552690,-3.536212,-0.437169,2.458242,-2.588157,7.368393,3.725511,7.793481,4.058366,-2.228693,1.474891,-4.094439,-7.973536,3.628083,-6.051967,-5.157528,-4.471762,1.747613,9.002147,2.570413,-7.575276,-5.242130,5.872403,-2.954080,-4.767993,-7.430530,7.022393,7.815019,-4.601038,-0.992479,-3.623855,0.175045,3.229594,5.363207,0.474455,-3.966039,0.477143,9.231367,0.468327,8.794247,-7.638713,8.687921,-1.331816,-8.344986,0.131975,-8.079331,5.570190,-6.120489,-4.867076,7.451764,0.835466,7.574748,1.583340,9.318881,8.543376,-3.210490,-2.432757,5.544149,5.037817,0.221672,3.957475,-3.384547,-8.409718,9.209329,-1.256174,-8.164377,0.933491,-8.845001,3.699348,2.345266,3.928857,-9.717936,9.691194,-9.497535,7.944492,0.695572,3.041551,3.255747,3.356921,-4.046323,-4.528596,9.751884,2.384179,-1.006892,2.551860,9.352755,6.139781,-0.723617,1.456210,5.384956,5.844775,4.982755,-8.593662,-3.833935,-4.772098,2.432945,6.222362,-1.165694,0.814740,1.314586,-5.128544,3.433892,0.294027,-6.781393,-9.657011,3.304996,-1.635449,6.207925,-6.801216,-0.394080,-4.729873,7.488221,-2.207862,-4.256678,-2.510375,-8.043743,-5.334903,-3.935224,-8.607971,1.691323,8.536363,-0.151294,1.910341,-7.134819,1.945226,-7.250580,0.219892,7.090773,2.878328,3.709243,-4.682634,-8.060112,0.395575,-4.381303,6.621565,-2.565279,-9.452441,7.497348,-5.341767,7.050208,-5.497361,-0.350297,7.021442,-1.687008,9.956627,-4.991313,2.906365,4.501390,-2.203213,-1.431280,5.030747,-5.506896,9.797417,9.393430,6.232968,6.439110,9.766399,1.386260,-0.950725,6.098382,5.865776,1.247708,8.458261,6.492956,-0.390191,5.729171,2.867517,6.521719,3.283627,-0.408454,-1.944364,2.969272,2.845534,-3.308542,-2.362879,-0.959187,-5.231022,-2.177254,-4.411643,3.003275,-4.288492,-2.670664,-2.045504,-9.355411,-2.193754,-1.981889,7.088387,-6.562153,7.733225,-5.021016,4.453595,4.691233,-2.914848,0.238206,-8.891347,3.259367,1.253273,-2.574209,8.047994,-1.427130,2.702505,-7.021345,-0.400369,-4.391874,-9.425193,2.225724,4.033126,9.117257,-5.391900,-7.480431,8.202024,7.372126,5.312566,-1.178616,4.896662,-4.789764,5.719415,2.191885,-9.362386,3.600068,-7.891197,-2.839697,-8.423685,1.202378,-3.378077,6.043467,9.215098,-6.280715,-0.318923,4.909341,6.252519,-4.024338,0.286333,-7.649394,3.243256,-3.173221,-1.806967,0.575560,-3.456659,-3.659394,-2.749857,-5.330426,-3.375966,-4.595157,8.064873,-0.785304,-8.758804,9.763631,-5.967682,9.989122,-1.896185,3.734887,-2.510133,3.232200,9.268936,9.540456,9.544158,0.674747,-9.916475,-4.136546,-6.854126,6.532887,7.655163,-5.302546,-5.870960,-2.769677,6.257753,-9.570490,-7.959807,-8.788477,7.922481,-6.718895,3.593973,-6.352609,1.413325,4.672968,-6.863900,-2.389652,6.630322,4.027532,-8.708470,-1.967085,-0.551688,1.782705,-9.700617,-7.561880,6.378400,-9.370393,2.531149,9.288701,7.668484,-8.335299,5.876880,-1.640849,3.439306,-1.307082,9.931868,2.896428,1.132321,-4.608083,-5.622394,9.754875,0.652620,-2.831549,3.712645,-7.991440,-4.785598,-2.990390,3.548008,-1.612784,-0.728522,0.552897,-0.008021,5.243652,3.009364,2.816306,8.914592,-1.973099,2.159456,0.144724,-0.907292,5.499904,-7.829372,-1.689252,-0.368002,-0.808273,7.619536,-7.809466,-6.553627,-2.262369,-9.327627,6.755681,-7.581991,-1.529642,-3.183557,-5.498202,1.270544,5.382927,5.484477,-3.813395,-0.706756,6.397440,-4.399349,4.736134,1.251283,-4.946083,-5.197150,3.248522,0.505281,-6.124101,9.050854,-7.701211,-4.144537,-0.625267,2.585426,-3.215344,0.948828,-6.573871,2.214226,-3.681742,1.597864,-1.770645,-7.862144,-8.537288,-7.151313,0.704417,-1.241576,-0.017032,7.034681,-4.341030,3.166068,1.147593,-0.782841,-0.074876,8.404306,5.861051,-2.374685,-4.859411,6.584554,-7.058186,9.010454,-9.449804,-0.537195,9.481472,2.013638,-3.300386,-4.321316,-4.912785,5.850806,-6.761368,0.264307,4.861181,-0.503748,3.971997,5.780520,4.384305,3.312574,-6.457396,-3.070318,-5.335328,1.931443,0.587775,-6.646107,6.779264,-9.871715,-1.905003,2.961568,6.139057,-2.334500,7.425107,4.987636,-7.102578,-2.944221,-4.797425,-9.391251,8.306500,3.888264,0.291305,-2.472521,-5.412656,5.419848,-4.167102,-6.784306,-0.741378,-9.684560,-4.184549,-2.525488,1.511420,6.209553,0.738337,-3.801939,-7.956140,6.946987,6.237854,-7.351749,1.887727,-4.201160,-0.792367,5.435970,0.286337,-0.813779,5.030467,7.650319,-3.049441,-1.784193,-4.687272,-9.043907,3.779755,4.229170,5.173739,-1.751859,4.661815,-3.919905,3.140478,-1.150595,-9.356269,1.980989,7.612044,-6.970860,1.421153,8.818201,9.210054,-2.794518,-1.662122,9.144348,2.206958,-4.405808,-7.072104,-1.651318,-2.817650,2.691695,-0.603061,4.906507,4.157875,0.639184,-8.495859,-9.466917,-9.389217,-7.653460,-7.180663,-2.350014,2.933470,-3.057193,8.176965,-9.968887,7.545848,-9.737386,-1.810709,0.589960,4.743767,-5.596089,-6.124706,8.743309,-6.285940,7.391655,9.565896,-9.273740,-9.890418,9.644144,-8.450852,0.990448,7.886724,4.714275,2.959726,0.433799,6.425800,2.246158,-1.153386,-0.545101,-9.663458,-9.277312,6.488834,1.226171,6.477811,4.821829,-7.997781,-8.870232,2.794392,5.745060,-1.749137,8.275551,-3.700980,1.149737,-5.987080,7.424505,8.511967,-3.679484,5.548785,-9.017227,-5.717540,-9.476122,7.053891,-8.415495,-2.159169,9.911148,-0.387304,-9.677686,5.388633,-9.405259,5.769811,2.831621,8.099045,5.216231,1.658341,5.427885,9.999611,-1.653973,-1.524152,5.766247,-1.505751,-9.615194,-3.407985,1.828342,-0.475461,7.687313,-2.988904,6.463396,-5.751000,-4.564219,-7.630051,-6.043518,3.029372,-8.386458,6.375609,-8.299873,6.817280,6.227173,3.785351,6.731030,-8.503998,6.669200,8.728085,-3.323741,7.846809,9.947973,-1.653706,0.640156,-6.115516,-3.938748,-4.109430,5.435117,5.677683,4.308296,-0.801476,-6.196729,7.501156,1.903248,-9.578339,-6.255975,-7.772384,-8.270787,2.406283,-1.214648,8.764881,-3.693188,8.563072,0.873252,-4.423683,9.183467,-9.902414,2.944530,6.375939,-6.751187,-3.025629,6.053327,5.325746,4.147043,7.729985,-5.674676,-9.337706,-6.888784,5.429321,-4.731261,-0.525639,-5.104341,-0.139107,-2.422709,-8.728243,7.456935,-9.465703,6.524166,-8.898809,-7.983814,-7.486600,8.792429,0.693461,-9.576548,8.187321,-0.270256,-4.868894,-3.915883,-1.827811,-3.873453,-4.632798,9.105212,-3.560143,-0.383456,-5.594311,-9.437944,6.098975,6.866457,-4.841229,0.126667,5.157035,8.607848,-6.716731,-1.111508,0.931457,9.269474,-3.505810,-6.920771,1.583306,-5.658434,8.689193,-2.187852,-0.715236,-0.419498], dtype = "float64")#candidate|6779|(1280,)|const|float64
const_6780 = relay.const([[-6,1,5,-8,-8,8,7,9,-2,5,-9,-5,9,-5,1,10,-2,-7,1,-7],[-4,-10,-10,-2,3,-10,-6,-1,-4,7,6,3,6,-6,-9,-10,9,3,9,4],[5,-6,8,-6,-4,8,-10,-9,-2,5,-9,4,5,9,-7,7,6,-4,1,-9]], dtype = "uint64")#candidate|6780|(3, 20)|const|uint64
call_6776 = relay.TupleGetItem(func_5673_call(relay.reshape(const_6777.astype('float64'), [5, 2, 16]), relay.reshape(var_6778.astype('int64'), []), relay.reshape(const_6779.astype('float64'), [1280,]), relay.reshape(const_6780.astype('uint64'), [30, 2]), ), 1)
call_6781 = relay.TupleGetItem(func_5678_call(relay.reshape(const_6777.astype('float64'), [5, 2, 16]), relay.reshape(var_6778.astype('int64'), []), relay.reshape(const_6779.astype('float64'), [1280,]), relay.reshape(const_6780.astype('uint64'), [30, 2]), ), 1)
func_1145_call = mod.get_global_var('func_1145')
func_1149_call = mutated_mod.get_global_var('func_1149')
call_6800 = relay.TupleGetItem(func_1145_call(relay.reshape(const_6779.astype('float64'), [16, 16, 5]), relay.reshape(const_6780.astype('uint64'), [60,]), ), 2)
call_6801 = relay.TupleGetItem(func_1149_call(relay.reshape(const_6779.astype('float64'), [16, 16, 5]), relay.reshape(const_6780.astype('uint64'), [60,]), ), 2)
output = relay.Tuple([call_6767,call_6776,const_6777,var_6778,const_6779,const_6780,call_6800,])
output2 = relay.Tuple([call_6768,call_6781,const_6777,var_6778,const_6779,const_6780,call_6801,])
func_6804 = relay.Function([var_6778,], output)
mod['func_6804'] = func_6804
mod = relay.transform.InferType()(mod)
var_6805 = relay.var("var_6805", dtype = "int64", shape = ())#candidate|6805|()|var|int64
output = func_6804(var_6805)
func_6806 = relay.Function([var_6805], output)
mutated_mod['func_6806'] = func_6806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_6836 = relay.TupleGetItem(func_6751_call(), 0)
call_6837 = relay.TupleGetItem(func_6753_call(), 0)
func_3822_call = mod.get_global_var('func_3822')
func_3827_call = mutated_mod.get_global_var('func_3827')
var_6841 = relay.var("var_6841", dtype = "uint32", shape = ())#candidate|6841|()|var|uint32
const_6842 = relay.const([-4,-10,-7,-1,-9,1,-9,4,-3,-1,-5,-10,3,4,-3,-3,-3,8,-2,-2,3,-8,8,-8,1,1,8,-6,3,3,8,5,-10,3,9,-2,1,-5,-2,-1,4,-8,3,-3,6,4,-5,7,-9,-9,8,-3,1,-7,10,-7,-9,-9,9,-9,-10,-8,2,-2,6,3,5,2,-3,1,6,-10,-1,5,10,4,7,-9,-9,-1,-2,-10,8,3,10,9,-1,9,7,-3,-8,-1,1,5,10,-5,-8,-1,9,-2,-7,-3,9,10,7,-6,-10,-1,4,-1,2,9,2,-10,4,-8,-2,-9,4,-10,-3,-6,-3,4,-3,-4,-2,6,-10,5,-8,-5,5,-3,3,9,-10,-1,-4,-10,9,-3,-6,-4,-7,2,-3,8,-1,8,6,4,-4,9,-9,4,-3,-10,8,-5,5,10,4,-8,1,-3,-5,1,1,9,8,-1,-2,10,-6,-5,-2,-9,-5,3,4,10,-4,-1,2,-6,-5,1,-7,9,4,4,-1,4,9,1,-5,5,2,6,-5,-4,1,-2,-6,2,7,8,9,5,1,-3,6,8,3,-2,8,3,-3,8,5,9,-5,3,1,4,-3,10,7,7,-4,10,-7,3,-5,-9,-2,6,7,5,-7,-10,8,-8,-8,4,-6,-5,-5,-2,1,5,-10,-3,8,5,-7,-4,2,9,-8,3,-5,-6,-5,3,10,1,8,-8,-2,-10,7,5,9,-1,-6,3,-1,4,-9,-3,-6,10,-10,8,1,-2,-5,8,-2,-3,3,2,6,3,-2,4,-3,-1,3,5,-9,-10,6,8,-9,6,6,-8,-3,-8,9,4,6,-5,7,1,-8,10,-1,2,1,3,-8,-10,2,-8,9,5,1,2,-9,-4,6,-1,-4,6,-2,5,-10,1,-2,-4,-4,6,-8,-3,-3,-4,-3,-7,-7,-6,-2,7,3,-5,-10,8,8,1,-4,5,-3,8,3,7,-8,6,-2,-3,4,4,9,-10,-7,4,-7,-1,-7,10,-6,-7,8,6,8,-6,9,6,1,-4,-9,2,-7,-8,-3,4,5,-4,5,-4,-9,-3,10,4,-5,2,9,2,4,-2,-10,6,6,-8,-10,-3,-3,-5,8,-6,2,-9,-9,-6,-2,-2,5,-6,8,3,6,-6,4,4,3,-5,8,-5,-4,4,1,8,5,-8,-10,10,-9,-7,-8,-5,2,7,5,-1,-4,6,-10,-1,10,8,10,-8,-4,2,-9,-6,-6,-3,6,-1,-8,6,-1,2,8,-1,-8,7,-5,6,7,-3,7,-5,9,-3,-1,6,8,3,-10,6,3,-1,-4,10,-1,6,10,-10,7,7,-6,10,-1,-2,7,-8,-1,7,-8,-7,-2,8,4,3,3,9,-5,5,-4,-8,3,1,6,1,7,-4,3,-10,-2,-10,5,6,10,5,-8,-5,8,7,6,-10,8,-9,-8,7,4,-8,-7,-6,-8,1,3,-9,3,-6,5,-9,2,3,-9,-1,-10,-1,-7,-3,9,3,1,-4,1,1,-6,1,10,-7,8,3,8,2,4,-2,-1,-4,8,-7,8,7,8,-9,5,9,-3,-9,8,-8,-1,5,7,4,-9,-6,-7,-10,-2,5,-6,-1,9,-4,5,9,-2,8,6,-5,-1,2,6,6,5,-7,6,-2,10,-3,-7,1,-7,-9,8,-9,-6,10,-5,10,-8,10,5,-10,-9,-9,3,6,-8,-4,10,7,4,-8,2,10,-4,-3,-4,3,-5,-10,6,-10,-10,1,10,7,-7,-5,-2,-10,-7,5,-7,-5,-3,-1,-10,3,7,-1,6,-3,3,-2,4,9,-5,3,5,4,-2,8,6,-1,7,-2,-7,6,4,5,9,9,10,-8,9,-4,-7,-2,-4,-7,-2,4,5,-1,7,9,2,2,10,-9,-1,10,5,-10,5,-2,8,10,7,2,-9,-1,-7,-5,2,7,-6,3,1,2,3,-2,-1,2,-6,-1,-5,6,-5,10,4,5,6,-5,3,10,-1,-7,-7,-10,5,-5,-6,-4,-3,-2,-2,9,5,5,-1,-2,-9,7,-7,-6,2,3,-4,1,-1,-4,-10,-3,9,10,2,4,-2,5,2,4,-5,-10,-5,-6,-3,-1,7,7,1,8,1,3,7,-3,-9,10,5,3,-2,8,1,-8,3,-4,3,6,-6,-5,6,9,-6,-9,1,-3,-3,8,-8,10,-2,-6,6,8,2,4,-3,5,-2,-2,-8,-5,6,3,-10,7,-7,6,8,7,7,-8,-4,2,7,8,9,-6,-7,-2,2,-8,4,-6,7,-2,5,-5,-3,7,-10,-5,8,-5,10,1,-9,-3,-2,5,2,-4,-7,6,-3,-10,-7,4,-6,-2,8,-8,-2,-10,-10,4,4,9,-4,-1,-7,1,-6,1,6,8,-7,-3,-1,-3,-9,5,4,3,10,-6,5,-2,4,2,-9,8,-1,4,3,3,6,-5,3,-8,-4,-9,-4,9,-6,-2,3,10,-8,-4,-4,4,6,-2,-7,-1,7,-9,2,-10,9,1,9,-4,6,9,6,1,1,2,-4,-1,2,1,-8,-2,1,6,5,-7,7,-2,-9,8,6,2,-2,8,-2,10,8,-4,-5,10,-10,10,5,4,-5,-6,2,-1,-10,10,8,10,2,-6,6,-7,-3,6,9,3,-10,-6,-8,9,-4,8,1,-9,-5,9,2,-6,3,2,1,7,-6,-6,-8,10,7,5,9,-10,10,4,7,7,-5,3,6,-7,-5,-7,-9,-6,-7,4,-8,10,8,-9,7,7,7,-8,-4,-5,10,-3,-1,7,3,-5,10,8,-1,-2,-3,2,3,-4,5,-5,3,3,-6,-1,-4,9,-2,-9,-1,5,4,-5,5,3,1,4,5,-6,-10,1,5,-5,4,-2,-8,1,4,10,-7,1,10,-2,5,-7,6,8,-7,-8,10,8,-7,-2,6,2,3,-1,-1,8,-2,-10,3,8,2,1,-8,-9,-9,-7,3,10,7,10,6,-5,-5,7,-4,9,2,9,2,-6,1,6,7,1,-1,1,1,8,-2,5,9,-3], dtype = "uint32")#candidate|6842|(1152,)|const|uint32
var_6843 = relay.var("var_6843", dtype = "bool", shape = (1008,))#candidate|6843|(1008,)|var|bool
call_6840 = relay.TupleGetItem(func_3822_call(relay.reshape(var_6841.astype('uint32'), []), relay.reshape(const_6842.astype('uint32'), [12, 16, 6]), relay.reshape(var_6843.astype('bool'), [1008,]), ), 1)
call_6844 = relay.TupleGetItem(func_3827_call(relay.reshape(var_6841.astype('uint32'), []), relay.reshape(const_6842.astype('uint32'), [12, 16, 6]), relay.reshape(var_6843.astype('bool'), [1008,]), ), 1)
func_1996_call = mod.get_global_var('func_1996')
func_2000_call = mutated_mod.get_global_var('func_2000')
const_6851 = relay.const([-8,-5,-3,2,6,8,7,-7,9,8,1,8,-4,-5,-10,-7,3,9,-8,-7,-7,6,-1,6,7,6,2,2,-7,-10,-7,-5,-1,-6,7,3,-10,-9,2,-1,-7,-6,10,-6,-5,4,-5,4,-5,-5,4,8,7,-5,1,7,-2,9,-3,9,-5,-1,3,-8,-6,3,-3,3,6,-10,-3,-9,1,7,6,1,-8,-2,8,9,7,1,3,-9,-2,-8,-7,10,-6,2,-2,1,-5,-10,7,4,-3,3,1,-5,-2,-7,-1,-6,5,-8,3,6,-4,-1,-8,-4,-2,-7,8,5,6,-8,-1,5,-4,-5,-10,-5,9,-5,10,10,-6,-4,-8,2,-3,10,-7,-1,7,10,-9,4,-10,9,-8,-4,3,-9,-9,6,5,7,2,-3,-6,-4,7,-4,-7,-8,9,3,2,-6,5,2,-7,-2,-6,6,9,6,-10,-2,3,-5,-4,8,-10,-8,4,7,-10,10,5,10,8,1,-8,6,-4,8,7,5,-10,-4,-4,8,1,10,4,3,7,9,-6,-9,-5,-10,2,-2,8,-9,-9,8,6,10,-7,-1,7,-2,-6,3,7,-4,9,-3,3,1,10,-4,7,-4,6,-1,-9,6,-3,7,-10,-8,8,-6,-3,3,-6,8,10,10,-1,-1,-5,6,-5,5,-3,-4,2,9,9,-9,-8,10,10,6,-2,-10,3,2,-8,-3,2,1,9,1,4,5,-6,-10,5,-6,4,-4,1,-4,7,-9,9,2,1,-6,-3,5,-5,6,4,1,-9,4,4,-10,-9,9,8,-4,5,4,-4,-9,-7,-1,8,-6,8,8,9,-1,6,6,1,5,-3,-6,-9,6,-2,4,10,9,-3,9,3,-2,-10,-3,8,9,-6,-8,3,-8,2,7,3,9,-10,-7,8,2,-8,3,2,7,8,-2,9,8,-3,3,-8,3,1,-1,-1,-9,9,-5,3,-8,9,-3,-1,2,-5,-1,7,3,5,-9,8,-3,9,7,-2,-6,-8,-1,-2,-2,-8,-10,-6,-3,8,5,-1,2,-10,5,-7,-5,9,-1,-9,-8,5,-9,2,1,-5,5,-9,-7,7,1,2,8,-1,4,3,6,1,-10,-9,-10,-9,2,3,7,3,3,-3,9,-9,6,5,1,-7,-9,-2,-3,-6,-1,8,9,5,9,3,3,-2,-6,-1,5,8,6,-4,2,-6,9,10,-5,1,4,3,8,8,-4,-2,9,-2,-1,4,6,-8,-3,-4,3,6,1,-5,-5,-4,-2,-8,4,5,-6,-1,-10,7,5,-6,1,6,-1,1,-1,-7,-1,3,-6,-3,9,3,10,5,-5,4,2,8,-10,-1,3,-6,-4,-10,-9,-1,6,10,-7,-1,-7,-10,6,4,6,7,-5,4,3,-8,-8,3,-6,-9,-9,7,7,6,-3,1,6], dtype = "int64")#candidate|6851|(540,)|const|int64
const_6852 = relay.const([[-8.419775,-4.161728,9.368532,-7.456731,8.686435,-9.049604,2.422416,-4.680948,-6.904309,0.721532,6.351780,4.152490,1.167550,5.911976,1.349353,-0.813167,1.793135,6.471065,1.412405,0.684373,-5.254280,8.697704,-0.233953,7.381503,2.543440,-1.148322,-5.449521,-8.601831,-7.615282,-4.951187,3.372873,7.050157,8.407352,0.215185,-6.651327,-7.908263,-8.633446,-2.335493,8.032145,4.804167,-8.354266,-3.139908,2.183606,-2.792226,-2.499582,2.636906,-5.549010,-2.208698,9.975288,-1.029123,3.093196,8.411655,-5.236011,-6.573774,0.703474,-3.213295,1.668466,4.648789,0.425861,-5.744272,-8.001360,-8.506902,-2.657238,-7.517410,-2.296989,9.250648,7.264085,-4.750763,-9.604001,-9.247466,-4.816041,8.722086,8.903832,7.410095,-9.175819,-3.868143,2.103059,2.970402,6.095783,-4.382460,-7.793319,6.397927,-3.219052,1.324874,-8.502088,-8.954777,7.363116,-1.343993,-2.587548,8.269888,9.684228,6.612727,-3.286949,-4.770530,7.904439,-6.120473,-9.176832,1.509765,9.307914,8.552634,-5.231154,-2.073870,4.007717,-9.363924,-8.023241,4.733263,1.154804,8.833916,0.570516,-2.990391,-8.096327,8.010755,-9.515898,6.000848,4.170830,-8.929597,-9.317671,0.741053,3.638388,-2.465703,-4.052143,-8.311244,-1.884466,0.503828,0.307507,-5.904889,-1.375946,0.024890,4.107919,-9.858308,8.570515,-5.129234,-3.662234,-3.827212,-2.769473,4.702221,-9.823676,-6.069725,5.092231,-4.111395,4.983477,-6.336801,-9.167991,0.530656,-8.084520,7.939994,-4.789484,-0.401144,9.097913,-3.508643,5.162323,-7.820396,0.154642,-4.551789,4.930485,-0.399081,-4.492305,-4.273314,-9.167034,-6.489351,-3.087018,-4.689749,2.690872,8.271716,1.047064,-5.562106,9.410672,-0.791746,-7.451545,-7.078679,-7.989369,-9.312625,7.328597,9.227620,-6.589590,6.698664,5.459782,6.137463,-7.359402,-6.268724,7.449191,-2.872624,5.051961,0.536618,4.036604,7.037430,-4.640896,-9.241647,9.849024,8.870221,8.458818,-7.762115,5.573082,-8.563951,-9.889415,0.223810,4.324637,-8.351028,2.232361,-7.562773,3.664193,-2.315942,-8.860521,-4.073397,-6.015552,8.018636,-4.270025,6.721560,-6.386569,8.991396,-8.146890,-0.557497,-4.353197,-9.281804,-1.882229,-2.683903,4.397748,-4.029911,-2.336751,9.290993,-0.434637,-8.097446,-9.595033,-1.353355,8.963892,4.810669,5.270475,-5.616892,-0.559259,5.338222,9.879858,2.628023,-3.525561,-6.771328,-4.953798,1.202966,7.126421,7.915741,1.870217,-8.739259,9.520642,-2.368399,4.159129,-5.520932,-9.617604,-3.530652,4.453447,-9.881215,6.831336,-9.852778,-2.209918,6.464080,-9.291179,5.465141,-2.362301,-6.187826,7.908025,-8.076936,1.896324,-7.312349,-6.474638,-6.633286,-4.694936,5.618404,3.034769,5.334887,-2.698221,2.063245,7.859503,-0.226594,-1.441851,3.018270,-2.967417,-5.171815,-9.072083,3.668092,-3.883617,0.485399,-7.114988,-8.086592,-4.732727,8.089047,-1.800191,0.874717,1.843216,-8.119599,6.408671,7.492364,8.559921,8.679310,-4.105176,9.112883,-6.989824,-1.539117,5.293738,0.530324,-2.283435,-5.270234,6.249241,7.463666,-5.689271,1.981068,5.395140,0.740541,-8.865021,9.849103,0.057751,9.070070,3.715495,-4.967201,1.489955,-5.794771,-9.286909,-8.722393,3.903022,-7.543898,2.883779,2.048141,-5.940388,-8.723801,6.674013,7.229648,-7.709660,8.478408,-6.999696,-6.564745,0.946409,-6.054760,-0.740608,2.641781,-6.859661,1.010984,3.829932,-9.516281,2.947804,2.482516,-4.681196,4.689378,0.277557,-3.424896,-3.801386,8.555932,-7.568685,9.535734,0.204993,-2.832902,-5.496790,4.333018,-9.576412,7.051670,-6.804382,-0.133727,5.336265,3.558434,-4.101619,1.064330,5.500463,-7.800684,-0.911427,-8.524531,2.767267,2.310368,-5.861099,7.361635,-3.787389,-4.858496,1.462880,-5.238260,-6.208581,-5.393839,3.987269,2.771875,-2.421311,-1.452835,7.534863,-3.878919,4.562358,-4.910774,6.940653,-9.319328,-0.069526,-6.978288,-1.069239,-9.243669,2.977487,7.331811,-1.068356,8.954407,2.073932,4.411560,-2.902874,9.343099,5.532306,6.139184,6.427272,3.570564,-4.628517,-7.162807,-9.790673,0.988985,8.915417,-7.282335,8.855382,-2.495093,-7.796743,3.410286,-1.430150,-9.489376,-4.319876,-0.846028,-3.239156,0.790988,5.767605,3.768302,-5.489127,1.458865,8.476186,-1.302750,6.094964,8.474777,-6.493605,-9.186139,0.489845,6.117419,-8.426809,-6.929056,5.712494,9.337641,9.370877,-7.283291,6.819415,5.124692,4.640663,9.220129,-1.633012,-4.393493,6.203965,7.310296,-6.085934,-4.256064,-5.769960,5.559226,-4.588695,3.547767,7.425738,-7.570459,6.046254,8.478312,7.797930,-8.637350,-3.140994,-6.995245,6.369723,-9.456711,-9.787029,4.651928,4.483616,-3.012747,2.905031,2.578986,7.820002,-0.683217,6.749623,-0.780168,-7.225378,9.566535,4.629131,4.384543,7.215137,-3.953646,-9.840590,2.137138,-3.973244,-9.580605,4.901760,-2.668460,0.253908,9.829744,0.944394,5.676401,-2.770938,-3.112363,-5.515690,5.411651,1.107500,-2.513957,7.564743,-6.956721,2.557617,2.550225,-1.985037,-8.389058,-2.973215,2.491575,0.138237,-5.534389,8.435820,6.266278,-5.841482,2.532765,7.152906,7.870310,7.440081,-8.366911,-4.964191,7.771638,-4.054677,-0.886136,-2.541119,-0.583447,-7.731951,9.183833,4.297906,-7.854712,4.360018,1.732641,2.574558,1.605218,-5.952946,4.071641,-5.603061,-1.115620,-5.730418,4.844672,-0.293521,-9.926471,-7.890442,-0.246500,3.597062,8.251530,-9.826736,4.468036,-9.389261,6.514094,-8.659526,9.841340,9.591042,1.296207,3.336314,-5.086548,-9.152845,-7.039475,8.512120,-5.668822,5.261804,8.689558,3.353001,5.696362,-7.461453,-5.764806,-0.888705,6.018922,4.889759,2.077330,5.374482,-4.288669,3.067632,1.194135,6.118101,0.999643,0.115759,1.265653,9.635331,-9.660221,1.087543,-9.534226,2.501458,0.848118,5.495458,9.395707,1.616991,-8.120225,-8.248327,7.734982,-0.453147,9.349318,7.090505,-3.661969,0.387609,-6.329182,6.558493,-2.018524,-1.453485,-3.895418,8.840153,8.621214,7.720498,1.755564,6.559946,-3.958507,4.138619,5.764903,-5.621441,0.196386,7.184957,-4.952025,-1.558187,2.772693,-1.209087,-0.198235,8.427396,-4.244074,-9.567246,-4.301745,-6.949108,8.254190,-5.885731,8.394436,-9.211784,9.600700,-7.241313,-2.909741,-8.171579,-4.308293,0.236638,-0.885651,-2.637784,-8.123639,-0.875440,-2.269934,5.728094,-1.942858,-6.696983,-2.299832,-7.740365,-8.537475,0.548145,-4.850176,-0.741974,-6.362273,9.045130,-8.591604,-9.412433,-2.376080,-7.544537,0.829016,-0.845487,8.850430,7.968005,7.078046],[2.267682,1.987703,1.717219,2.446445,-3.012091,6.783602,-1.994690,7.597565,-1.783052,-5.784165,-8.864528,-4.414911,7.500088,3.271326,1.388600,4.280582,2.465409,7.027014,-8.052197,-3.599447,4.430295,-5.825378,-3.215711,-0.203627,-2.863639,3.593925,-2.920622,8.529038,0.937448,1.973786,-9.037253,-6.670565,1.873303,-8.758430,-2.857575,-3.052411,-4.654414,0.288423,-8.368693,-9.362176,-0.640177,6.798656,7.575948,1.323417,3.442944,-9.370397,3.188397,2.300258,-7.876130,-0.052844,8.187667,-7.751061,4.487473,-5.069338,3.473988,-7.628707,-8.805377,6.224158,2.402405,-8.678543,8.005254,-8.581738,4.350630,9.075552,6.514860,-8.754327,-8.311728,-3.878256,5.573575,5.278309,4.022356,-2.648647,9.976303,-6.390382,-9.597721,8.316862,1.105631,-4.655742,-8.400623,-4.073067,0.216134,-6.345690,-3.970010,-2.234539,8.836630,-6.799730,0.373087,-7.410443,-6.286072,7.796071,8.723742,-4.706106,-8.960965,-0.950635,-6.145394,-9.260340,7.134912,9.675046,-6.757660,6.090946,1.925260,-4.757033,5.215127,7.942324,0.259911,-5.180106,-0.915076,4.611831,-8.453902,9.783536,3.807929,-5.782772,-9.641436,-1.417019,0.354251,-9.444747,7.129599,-2.211228,0.951767,7.902455,-2.495542,1.164918,-5.162810,-1.079599,-9.709849,-3.490180,5.689329,3.873937,-6.988523,-3.799962,4.956114,4.541172,-0.782158,0.501011,5.638859,-5.860635,3.939946,-2.804781,3.272412,-7.034942,-7.547248,9.291107,2.150948,4.719973,-3.243475,-4.732536,-0.864111,-3.563586,0.913411,-0.994162,-1.818119,-9.541480,1.822025,-7.156429,4.220657,-6.763646,1.070862,-1.954921,-5.472379,-8.836098,5.838930,2.399473,-0.749401,-2.644099,1.202234,0.806939,-4.434878,7.357052,-1.871844,-0.893230,-1.347049,-3.453840,-9.039633,3.193653,-3.654043,9.664564,-6.020506,-6.493534,-0.604618,-2.741710,4.079921,-4.551417,8.993486,9.586732,6.391051,-9.268203,4.619063,5.941465,2.158803,-9.598789,-4.616790,9.459526,-4.926644,-3.417928,2.077809,1.693817,-4.601347,-8.865274,0.003911,8.900523,0.523222,1.390714,-9.144105,-6.393006,5.048363,-8.246517,-2.743774,-1.502279,5.135535,5.042822,9.447470,0.482593,-5.702705,3.366360,-2.674952,-0.839002,-1.184766,-4.263553,-6.522287,-8.820403,5.569823,-6.756104,8.770261,9.105914,0.091329,8.638671,1.026646,-7.604104,-3.420268,7.065123,-2.769425,-8.075239,8.018499,-8.164554,6.634472,6.546797,4.336208,-4.059995,-6.292345,3.750963,-9.656339,-0.862804,5.135799,-6.335650,7.822946,-2.616100,3.208376,-5.092166,3.408956,8.711993,-4.922379,-7.603280,-5.475168,-4.140164,-9.211651,-1.260224,-8.461044,-9.818725,2.891140,2.978978,-9.296968,-1.917676,-1.929340,4.399320,5.726918,-1.886896,1.078851,7.486576,2.621859,9.541547,9.039122,-2.761634,-2.309997,-0.429901,0.423049,-8.113387,0.473472,-7.064765,-8.574337,-2.295670,-9.014013,9.130015,1.325251,9.161785,-9.313387,-9.311481,-0.160637,4.792920,4.922331,-2.296632,7.257713,-6.272270,3.061938,-7.218810,-8.526820,-0.051085,6.546957,5.717664,-6.432610,9.883213,7.580970,8.545206,-7.415177,-3.809230,-2.836161,2.456802,-8.153107,-5.760235,-2.397058,9.110316,6.716771,2.409243,9.637622,7.109025,9.442267,-4.366845,-2.089841,-8.254685,-3.565090,-6.808862,0.949180,-1.215380,-5.848464,2.454435,4.069252,4.419261,-4.920893,2.032494,4.514604,-1.385246,8.404309,1.086289,-6.468340,-7.734718,0.617275,7.709298,-6.532739,-6.166294,-3.588570,2.264024,-1.871560,1.017690,8.510215,-5.794114,0.600808,2.652785,6.811005,3.740431,-8.870897,-9.233590,-0.427511,-5.727232,8.830621,4.616213,4.104521,1.007389,-4.865072,-1.670858,0.511812,-5.075710,9.306797,7.513077,6.781884,-5.796185,-1.372472,4.355801,-1.406373,-0.575517,-1.439368,-6.263601,-8.871547,6.908287,-4.516324,6.704437,-5.416244,-3.308170,4.522295,-7.879686,-0.287991,1.849314,0.149789,-0.836538,-9.198733,4.210011,-0.847846,-4.100627,2.090975,2.264751,-8.357653,3.984954,0.124366,-4.378114,7.158515,4.014554,-0.461079,-3.621956,6.937283,6.769787,1.779375,-8.449179,-9.722373,4.789975,-3.352727,0.639299,5.404861,9.688561,9.213089,3.084917,-5.508202,-2.546057,7.225759,-5.218804,8.670038,0.728584,-8.724687,0.671532,-9.776706,-4.479613,0.295815,6.517538,-3.713812,4.116964,2.289202,-4.945528,2.117620,-6.954099,5.934312,6.683984,-0.418037,-6.160768,-2.094852,-8.508030,-5.959022,7.301659,-0.273673,-9.064707,6.790072,-2.916106,-4.916479,-3.525914,-2.787912,9.238746,0.222568,-5.451180,9.406331,-2.429621,-8.154028,-5.498003,6.379498,0.729517,3.547318,-1.132222,6.473388,1.909100,5.113762,-4.322069,-4.784519,-6.946283,-1.943546,9.832823,6.574362,-4.433899,-2.173678,-8.038452,-6.965132,-6.256286,6.156348,4.657258,2.180023,-6.994744,-3.498777,-9.219525,-4.307191,2.020586,-7.380247,-6.045922,-6.234843,2.225080,-6.746644,9.872196,1.803792,-4.908380,-4.960872,-0.830572,-6.444217,3.532730,9.463062,0.988994,-6.427012,-6.014382,8.383921,-3.668152,9.223091,8.065980,8.034963,4.451687,-5.584729,9.213786,5.320135,-3.270471,-4.362867,-8.505989,-4.753449,-9.712792,-2.336233,7.984633,5.728697,-4.651081,8.349035,-2.616244,-3.378310,-6.852599,8.323141,6.699084,9.742357,-5.264148,2.742597,4.382210,-7.017776,-7.759857,-4.410986,3.333962,0.236303,5.137924,5.914411,9.550634,4.322434,-7.103756,3.520779,5.493362,0.538151,0.549776,-4.704878,-7.074501,-3.319823,-9.564723,-5.164019,-7.275104,2.725628,9.843402,-6.694947,-0.151090,-8.823620,-4.498383,-9.862506,-5.732558,-0.714579,2.292705,-5.717264,4.280088,-1.177252,1.556306,5.071735,8.082722,4.891270,0.933929,4.482781,9.534081,-7.216485,-1.328504,6.427963,1.235771,-6.712709,2.532011,-5.468574,4.747526,-2.848704,-8.259495,-0.821389,-7.054802,-6.144850,6.254708,4.864913,6.685415,5.622706,-2.766611,-8.925072,-1.533889,-2.429344,3.785746,-5.530584,-0.422609,9.879901,2.035248,-4.742753,-3.739375,9.546711,-5.339277,-5.202669,2.703558,8.668766,6.284196,4.554431,-3.682868,7.857517,-4.453972,-7.909083,-1.528978,7.472292,-3.844674,5.489882,-8.945614,-2.455152,1.457430,-0.024824,-9.601614,-6.115535,0.544597,1.559163,-7.407451,1.705825,8.199958,6.796356,-6.091418,0.140546,-0.929041,3.362025,3.451344,5.786802,-2.830765,4.192393,-3.208183,-5.090575,5.458146,4.960131,-1.527707,3.241264,2.285786,4.862752,6.446716,-2.713104,2.534621,7.562484,2.508003,9.954357,-1.585066,1.660083,5.411165,6.046294,8.545494]], dtype = "float64")#candidate|6852|(2, 640)|const|float64
var_6853 = relay.var("var_6853", dtype = "uint64", shape = (60,))#candidate|6853|(60,)|var|uint64
call_6850 = relay.TupleGetItem(func_1996_call(relay.reshape(const_6851.astype('int64'), [6, 9, 10]), relay.reshape(const_6852.astype('float64'), [1280,]), relay.reshape(var_6853.astype('uint64'), [60,]), ), 2)
call_6854 = relay.TupleGetItem(func_2000_call(relay.reshape(const_6851.astype('int64'), [6, 9, 10]), relay.reshape(const_6852.astype('float64'), [1280,]), relay.reshape(var_6853.astype('uint64'), [60,]), ), 2)
func_6804_call = mod.get_global_var('func_6804')
func_6806_call = mutated_mod.get_global_var('func_6806')
call_6855 = relay.TupleGetItem(func_6804_call(relay.reshape(var_6841.astype('int64'), [])), 5)
call_6856 = relay.TupleGetItem(func_6806_call(relay.reshape(var_6841.astype('int64'), [])), 5)
bop_6863 = relay.mod(const_6852.astype('float64'), relay.reshape(call_6850.astype('float64'), relay.shape_of(const_6852))) # shape=(2, 640)
bop_6866 = relay.mod(const_6852.astype('float64'), relay.reshape(call_6854.astype('float64'), relay.shape_of(const_6852))) # shape=(2, 640)
output = relay.Tuple([call_6836,call_6840,var_6841,const_6842,var_6843,const_6851,var_6853,call_6855,bop_6863,])
output2 = relay.Tuple([call_6837,call_6844,var_6841,const_6842,var_6843,const_6851,var_6853,call_6856,bop_6866,])
func_6867 = relay.Function([var_6841,var_6843,var_6853,], output)
mod['func_6867'] = func_6867
mod = relay.transform.InferType()(mod)
mutated_mod['func_6867'] = func_6867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6867_call = mutated_mod.get_global_var('func_6867')
var_6869 = relay.var("var_6869", dtype = "uint32", shape = ())#candidate|6869|()|var|uint32
var_6870 = relay.var("var_6870", dtype = "bool", shape = (1008,))#candidate|6870|(1008,)|var|bool
var_6871 = relay.var("var_6871", dtype = "uint64", shape = (60,))#candidate|6871|(60,)|var|uint64
call_6868 = func_6867_call(var_6869,var_6870,var_6871,)
output = call_6868
func_6872 = relay.Function([var_6869,var_6870,var_6871,], output)
mutated_mod['func_6872'] = func_6872
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6955 = relay.var("var_6955", dtype = "float32", shape = (10, 5, 11))#candidate|6955|(10, 5, 11)|var|float32
uop_6956 = relay.log(var_6955.astype('float32')) # shape=(10, 5, 11)
output = relay.Tuple([uop_6956,])
output2 = relay.Tuple([uop_6956,])
func_6961 = relay.Function([var_6955,], output)
mod['func_6961'] = func_6961
mod = relay.transform.InferType()(mod)
mutated_mod['func_6961'] = func_6961
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6962 = relay.var("var_6962", dtype = "float32", shape = (10, 5, 11))#candidate|6962|(10, 5, 11)|var|float32
func_6961_call = mutated_mod.get_global_var('func_6961')
call_6963 = func_6961_call(var_6962)
output = call_6963
func_6964 = relay.Function([var_6962], output)
mutated_mod['func_6964'] = func_6964
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_7029 = relay.TupleGetItem(func_6751_call(), 0)
call_7030 = relay.TupleGetItem(func_6753_call(), 0)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
const_7038 = relay.const([8.346250,4.007023,1.825418,6.564755,-9.559573,-6.230714,-1.354693,-9.014948,0.645566,-7.713178,-4.439875,-0.813539,-3.363609,-3.858263,2.226606,0.937101,8.557597,-3.705713,4.161542,9.192007,1.557782,-4.701065,1.500179,-6.499071,-8.446213,-5.555240,-7.481063,5.558829,-6.919671,-3.380143,2.866768,-5.029902,2.310538,-8.749240,-3.980865,-6.053265,3.011960,2.073525,4.472318,5.788801,-9.417196,-3.386237,-9.865715,3.233304,-5.319586,4.921153,6.032978,-3.143532,-7.599984,-3.504439,-3.518498,-7.040944,6.764688,8.669417,4.800970,-8.700338,-2.386810,-9.331720,3.336366,8.324206,8.564821,6.608951,-4.257496,7.226927,-6.395923,4.247893,-2.906987,-6.053457,-5.521366,-4.708661,0.724497,9.128042,-1.224213,-4.593592,-9.426140,0.590953,-5.448363,-7.786711,-7.994040,6.505008,5.913690,-0.361200,-4.208854,9.112249,-7.250014,-9.014591,4.084922,0.003812,6.254891,2.411958,-8.350567,-0.419716,8.597259,9.366138,-5.304825,7.239914,-5.252243,-5.926917,-8.535826,4.550249,5.494941,-8.657216,0.935383,-1.758478,-6.692216,-4.217088,-5.525806,6.277842,-3.927718,-2.645377,-9.187049,-5.163558,5.154242,3.620760,6.081455,-1.515518,5.906065,9.307435,-3.354210,2.246670,9.801875,9.400377,-9.872955,3.885612,-6.553723,-5.830381,8.731083,6.934965,7.725341,3.748142,3.438376,0.133067,-3.278618,6.183907,5.506119,1.239759,1.576228,-1.555754,-0.746308,-8.336841,4.942399,7.946276,6.895681,1.946574,9.233280,5.600922,-3.561949,0.639557,6.252591,-9.472336,-1.440381,4.728177,-8.981274,5.839630,-7.191061,4.755955,-2.231351,-2.881537,1.726196,-6.437631,-0.911100,5.854700,7.097677,-1.769920,-2.710770,6.647081,-8.842035,-2.260966,-7.536380,8.775678,8.716416,6.185931,4.307334,9.984246,4.494161,-3.904931,-9.301531,7.243024,-7.910763,-2.187361,-0.632030,6.398053,5.064105,1.678671,-9.586486,-8.631415,-4.550297,8.917741,3.307469,-2.539981,1.416275,4.147712,5.617049,5.907021,-0.668771,-5.150644,9.728677,3.194867,4.584727,-9.965900,-6.301774,6.310820,-2.794929,-1.768011,8.090920,1.077188,1.020293,-9.011676,6.000642,0.111921,-1.120409,-3.934272,7.450851,-9.970928,-8.331090,-1.307170,7.110142,4.319167,3.115645,6.866991,2.157374,3.987186,7.985995,3.834141,0.132129,-3.368692,-8.930702,5.082546,1.702664,-6.878872,-8.929219,-8.562034,-7.137060,-8.380129,8.948774,-4.518199,-1.021074,-4.462827,-5.503826,-5.601843], dtype = "float64")#candidate|7038|(240,)|const|float64
call_7037 = func_2495_call(relay.reshape(const_7038.astype('float64'), [2, 12, 10]))
call_7039 = func_2495_call(relay.reshape(const_7038.astype('float64'), [2, 12, 10]))
var_7044 = relay.var("var_7044", dtype = "float64", shape = (3, 7, 7))#candidate|7044|(3, 7, 7)|var|float64
bop_7045 = relay.equal(call_7029.astype('bool'), relay.reshape(var_7044.astype('bool'), relay.shape_of(call_7029))) # shape=(3, 7, 7)
bop_7048 = relay.equal(call_7030.astype('bool'), relay.reshape(var_7044.astype('bool'), relay.shape_of(call_7030))) # shape=(3, 7, 7)
output = relay.Tuple([call_7037,const_7038,bop_7045,])
output2 = relay.Tuple([call_7039,const_7038,bop_7048,])
func_7056 = relay.Function([var_7044,], output)
mod['func_7056'] = func_7056
mod = relay.transform.InferType()(mod)
var_7057 = relay.var("var_7057", dtype = "float64", shape = (3, 7, 7))#candidate|7057|(3, 7, 7)|var|float64
output = func_7056(var_7057)
func_7058 = relay.Function([var_7057], output)
mutated_mod['func_7058'] = func_7058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_7099 = relay.TupleGetItem(func_6751_call(), 0)
call_7100 = relay.TupleGetItem(func_6753_call(), 0)
output = call_7099
output2 = call_7100
func_7106 = relay.Function([], output)
mod['func_7106'] = func_7106
mod = relay.transform.InferType()(mod)
output = func_7106()
func_7107 = relay.Function([], output)
mutated_mod['func_7107'] = func_7107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_7108 = relay.TupleGetItem(func_6751_call(), 0)
call_7109 = relay.TupleGetItem(func_6753_call(), 0)
output = call_7108
output2 = call_7109
func_7115 = relay.Function([], output)
mod['func_7115'] = func_7115
mod = relay.transform.InferType()(mod)
mutated_mod['func_7115'] = func_7115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7115_call = mutated_mod.get_global_var('func_7115')
call_7116 = func_7115_call()
output = call_7116
func_7117 = relay.Function([], output)
mutated_mod['func_7117'] = func_7117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_7118 = relay.TupleGetItem(func_6751_call(), 0)
call_7119 = relay.TupleGetItem(func_6753_call(), 0)
output = call_7118
output2 = call_7119
func_7205 = relay.Function([], output)
mod['func_7205'] = func_7205
mod = relay.transform.InferType()(mod)
mutated_mod['func_7205'] = func_7205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mutated_mod.get_global_var('func_7205')
call_7206 = func_7205_call()
output = call_7206
func_7207 = relay.Function([], output)
mutated_mod['func_7207'] = func_7207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7208 = func_7106_call()
call_7209 = func_7106_call()
uop_7210 = relay.sigmoid(call_7208.astype('float64')) # shape=(3, 7, 7)
uop_7212 = relay.sigmoid(call_7209.astype('float64')) # shape=(3, 7, 7)
output = uop_7210
output2 = uop_7212
func_7216 = relay.Function([], output)
mod['func_7216'] = func_7216
mod = relay.transform.InferType()(mod)
mutated_mod['func_7216'] = func_7216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7216_call = mutated_mod.get_global_var('func_7216')
call_7217 = func_7216_call()
output = call_7217
func_7218 = relay.Function([], output)
mutated_mod['func_7218'] = func_7218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_7245 = relay.TupleGetItem(func_6751_call(), 0)
call_7246 = relay.TupleGetItem(func_6753_call(), 0)
var_7254 = relay.var("var_7254", dtype = "float64", shape = (3, 7, 7))#candidate|7254|(3, 7, 7)|var|float64
bop_7255 = relay.minimum(call_7245.astype('int16'), relay.reshape(var_7254.astype('int16'), relay.shape_of(call_7245))) # shape=(3, 7, 7)
bop_7258 = relay.minimum(call_7246.astype('int16'), relay.reshape(var_7254.astype('int16'), relay.shape_of(call_7246))) # shape=(3, 7, 7)
output = relay.Tuple([bop_7255,])
output2 = relay.Tuple([bop_7258,])
func_7260 = relay.Function([var_7254,], output)
mod['func_7260'] = func_7260
mod = relay.transform.InferType()(mod)
var_7261 = relay.var("var_7261", dtype = "float64", shape = (3, 7, 7))#candidate|7261|(3, 7, 7)|var|float64
output = func_7260(var_7261)
func_7262 = relay.Function([var_7261], output)
mutated_mod['func_7262'] = func_7262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7281 = func_7106_call()
call_7282 = func_7106_call()
func_6867_call = mod.get_global_var('func_6867')
func_6872_call = mutated_mod.get_global_var('func_6872')
var_7294 = relay.var("var_7294", dtype = "uint32", shape = ())#candidate|7294|()|var|uint32
const_7295 = relay.const([True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,True,True,True,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False], dtype = "bool")#candidate|7295|(1008,)|const|bool
const_7296 = relay.const([3,-7,-7,-4,7,-6,10,5,10,-8,9,-3,10,1,3,7,9,10,2,4,10,8,-4,10,9,3,7,-4,-9,3,3,5,8,8,9,-7,-4,1,-10,-5,2,6,5,6,-5,3,-1,-1,-4,-6,1,-4,-8,6,-7,-8,9,10,-4,-8], dtype = "uint64")#candidate|7296|(60,)|const|uint64
call_7293 = relay.TupleGetItem(func_6867_call(relay.reshape(var_7294.astype('uint32'), []), relay.reshape(const_7295.astype('bool'), [1008,]), relay.reshape(const_7296.astype('uint64'), [60,]), ), 7)
call_7297 = relay.TupleGetItem(func_6872_call(relay.reshape(var_7294.astype('uint32'), []), relay.reshape(const_7295.astype('bool'), [1008,]), relay.reshape(const_7296.astype('uint64'), [60,]), ), 7)
output = relay.Tuple([call_7281,call_7293,var_7294,const_7295,const_7296,])
output2 = relay.Tuple([call_7282,call_7297,var_7294,const_7295,const_7296,])
func_7316 = relay.Function([var_7294,], output)
mod['func_7316'] = func_7316
mod = relay.transform.InferType()(mod)
mutated_mod['func_7316'] = func_7316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7317 = relay.var("var_7317", dtype = "uint32", shape = ())#candidate|7317|()|var|uint32
func_7316_call = mutated_mod.get_global_var('func_7316')
call_7318 = func_7316_call(var_7317)
output = call_7318
func_7319 = relay.Function([var_7317], output)
mutated_mod['func_7319'] = func_7319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7335 = func_7205_call()
call_7336 = func_7205_call()
output = call_7335
output2 = call_7336
func_7344 = relay.Function([], output)
mod['func_7344'] = func_7344
mod = relay.transform.InferType()(mod)
output = func_7344()
func_7345 = relay.Function([], output)
mutated_mod['func_7345'] = func_7345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7348 = func_7205_call()
call_7349 = func_7205_call()
output = call_7348
output2 = call_7349
func_7355 = relay.Function([], output)
mod['func_7355'] = func_7355
mod = relay.transform.InferType()(mod)
output = func_7355()
func_7356 = relay.Function([], output)
mutated_mod['func_7356'] = func_7356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_7381 = func_7344_call()
call_7382 = func_7344_call()
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_7397 = func_7344_call()
call_7398 = func_7344_call()
func_7355_call = mod.get_global_var('func_7355')
func_7356_call = mutated_mod.get_global_var('func_7356')
call_7399 = func_7355_call()
call_7400 = func_7355_call()
func_6961_call = mod.get_global_var('func_6961')
func_6964_call = mutated_mod.get_global_var('func_6964')
var_7403 = relay.var("var_7403", dtype = "float32", shape = (550,))#candidate|7403|(550,)|var|float32
call_7402 = relay.TupleGetItem(func_6961_call(relay.reshape(var_7403.astype('float32'), [10, 5, 11])), 0)
call_7404 = relay.TupleGetItem(func_6964_call(relay.reshape(var_7403.astype('float32'), [10, 5, 11])), 0)
output = relay.Tuple([call_7381,call_7397,call_7399,call_7402,var_7403,])
output2 = relay.Tuple([call_7382,call_7398,call_7400,call_7404,var_7403,])
func_7405 = relay.Function([var_7403,], output)
mod['func_7405'] = func_7405
mod = relay.transform.InferType()(mod)
mutated_mod['func_7405'] = func_7405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7406 = relay.var("var_7406", dtype = "float32", shape = (550,))#candidate|7406|(550,)|var|float32
func_7405_call = mutated_mod.get_global_var('func_7405')
call_7407 = func_7405_call(var_7406)
output = call_7407
func_7408 = relay.Function([var_7406], output)
mutated_mod['func_7408'] = func_7408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7475 = relay.var("var_7475", dtype = "float64", shape = (5, 2, 7))#candidate|7475|(5, 2, 7)|var|float64
uop_7476 = relay.acos(var_7475.astype('float64')) # shape=(5, 2, 7)
output = relay.Tuple([uop_7476,])
output2 = relay.Tuple([uop_7476,])
func_7482 = relay.Function([var_7475,], output)
mod['func_7482'] = func_7482
mod = relay.transform.InferType()(mod)
mutated_mod['func_7482'] = func_7482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7483 = relay.var("var_7483", dtype = "float64", shape = (5, 2, 7))#candidate|7483|(5, 2, 7)|var|float64
func_7482_call = mutated_mod.get_global_var('func_7482')
call_7484 = func_7482_call(var_7483)
output = call_7484
func_7485 = relay.Function([var_7483], output)
mutated_mod['func_7485'] = func_7485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7511 = func_7205_call()
call_7512 = func_7205_call()
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
const_7514 = relay.const([-9,6,-1,3,-5,-1,6,2,-3,-2,2,-7,8,-1,7,3,-10,-4,-7,2,-1,-10,-10,-3,-3,6,-1,-8,8,-1,9,3,-5,2,-3,6,9,1,6,2,8,-7,-10,9,-6,3,8,-5,-2,-7,-1,-6,-6,-10,10,-4,-10,9,-5,8,-3,-7,6,4,-6,2,3,-8,5,-3,-9,-5,-7,-1,-5,6,-1,-8,2,4,2,-5,-3,4,-10,5,6,-8,-4,-7,-7,8,-5,-4,8,-5,5,-7,-5,-8,-10,6,-3,-10,3,-10,10,10,-4,-4,-4,5,1,8,3,-4,-9,10,5,10,7,2,-8,5,-5,-2,-8,-8,9,8,2,-6,2,-4,5,-7,-6,2,-1,3,5,-7,-4,-3,-1,-6,3,-5,-9,-2,-4,9,-9,-1,-5,6,-2,3,10,-1,-9,5,1,6,10,6,-8,6,-3,8,3,-10,-9,-3,10,-9,10,-2,-5,-1,-8,-10,2,-4,5,5,-7,3,9,-6,-9,-10,8,-10,-2,-7,9,-7,-3,8,-4,-6,-1,1,-6,-10,2,5,-4,5,7,-6,-1,-9,-5,-4,3,4,-10,3,1,-10,5,-5,10,5,-3,-4,-6,-9,-2,-2,5,-9,2,-1,-5,-6,-8,-9,2,-6,7,-7,4,5,-1,1,4,10,-3,-9,-2,9,7,-8,6,-1,-5,7,6,-7,1,-4,-9,-1,5,-1,6,-7,-1,-3,1,9,4,-7,-8,-9,2,3,8,-2,-5,-10,-4,-7,3,2,-4,10,-7,-10,9,3,5,-3,-2,-5,-9,-10,-3,-9,-7,-8,10,-8,-5,1,10,-9,9,-7,8,-8,9,3,-6,-6,-1,-3,4,-7,2,7,3,-6,-8,5,-4,-5,2,-5,-10,3,-7,2,10,2,-1,-5,-5,-7,3,-10,-5,-2,-5,-7,-7,-6,-7,-6,10,-10,-7,3,7,4,4,-8,1,7,-6,8,-7,8,3,-10,1,3,-8,-9,-8,6,7,2,6,3,-6,-9,-7,6,10,2,9,-9,-4,3,-1,6,4,7,7,-6,-1,7,-2,8,10,-5,-5,-5,5,3,-6,-6,-4,10,1,6,9,-9,-4,-2,7,3,-4,-3,6,-4,2,1,-1,7,7,5,5,-8,1,5,-9,-9,7,-9,5,-5,5,1,7,9,1,3,-8,-9,10,4,-4,-10,5,6,-7,5,5,8,-5,-9,3,-6,-10,1,-1,-9,9,6,3,2,-2,-1,-4,-10,-8,-7,10,3,6,-2,-8,-2,2,-1,-1,-4,1,-2,6,3,-1,-6,-2,1,-2,7,-3,9,6,-10,-4,-1,-2,7,5,2,8,6,-7,-10,-1,-1,3,-2,1,-9,8,9,1,8,7,3,-9,7,-8,-5,1,7,-9,6,-1,-6,-3,1,-2,-1,10,-6,4,5,8,5,9,5,9,9,-4,-10,-1,-4,-1,-3,10,-2,-1,-6,-10,-10,3,6,-7,-1,-1,2], dtype = "uint64")#candidate|7514|(560,)|const|uint64
call_7513 = relay.TupleGetItem(func_3471_call(relay.reshape(const_7514.astype('uint64'), [10, 7, 8])), 0)
call_7515 = relay.TupleGetItem(func_3473_call(relay.reshape(const_7514.astype('uint64'), [10, 7, 8])), 0)
output = relay.Tuple([call_7511,call_7513,const_7514,])
output2 = relay.Tuple([call_7512,call_7515,const_7514,])
func_7517 = relay.Function([], output)
mod['func_7517'] = func_7517
mod = relay.transform.InferType()(mod)
output = func_7517()
func_7518 = relay.Function([], output)
mutated_mod['func_7518'] = func_7518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7521 = func_7106_call()
call_7522 = func_7106_call()
output = relay.Tuple([call_7521,])
output2 = relay.Tuple([call_7522,])
func_7523 = relay.Function([], output)
mod['func_7523'] = func_7523
mod = relay.transform.InferType()(mod)
mutated_mod['func_7523'] = func_7523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mutated_mod.get_global_var('func_7523')
call_7524 = func_7523_call()
output = call_7524
func_7525 = relay.Function([], output)
mutated_mod['func_7525'] = func_7525
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7545 = relay.const(-10, dtype = "uint32")#candidate|7545|()|const|uint32
var_7546 = relay.var("var_7546", dtype = "uint32", shape = (1, 12))#candidate|7546|(1, 12)|var|uint32
bop_7547 = relay.equal(const_7545.astype('bool'), var_7546.astype('bool')) # shape=(1, 12)
output = bop_7547
output2 = bop_7547
func_7550 = relay.Function([var_7546,], output)
mod['func_7550'] = func_7550
mod = relay.transform.InferType()(mod)
mutated_mod['func_7550'] = func_7550
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7551 = relay.var("var_7551", dtype = "uint32", shape = (1, 12))#candidate|7551|(1, 12)|var|uint32
func_7550_call = mutated_mod.get_global_var('func_7550')
call_7552 = func_7550_call(var_7551)
output = call_7552
func_7553 = relay.Function([var_7551], output)
mutated_mod['func_7553'] = func_7553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_7580 = relay.TupleGetItem(func_7523_call(), 0)
call_7581 = relay.TupleGetItem(func_7525_call(), 0)
uop_7590 = relay.sinh(call_7580.astype('float32')) # shape=(3, 7, 7)
uop_7592 = relay.sinh(call_7581.astype('float32')) # shape=(3, 7, 7)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
var_7597 = relay.var("var_7597", dtype = "uint64", shape = (560,))#candidate|7597|(560,)|var|uint64
call_7596 = relay.TupleGetItem(func_3471_call(relay.reshape(var_7597.astype('uint64'), [10, 7, 8])), 0)
call_7598 = relay.TupleGetItem(func_3473_call(relay.reshape(var_7597.astype('uint64'), [10, 7, 8])), 0)
uop_7599 = relay.log2(call_7580.astype('float64')) # shape=(3, 7, 7)
uop_7601 = relay.log2(call_7581.astype('float64')) # shape=(3, 7, 7)
output = relay.Tuple([uop_7590,call_7596,var_7597,uop_7599,])
output2 = relay.Tuple([uop_7592,call_7598,var_7597,uop_7601,])
func_7602 = relay.Function([var_7597,], output)
mod['func_7602'] = func_7602
mod = relay.transform.InferType()(mod)
var_7603 = relay.var("var_7603", dtype = "uint64", shape = (560,))#candidate|7603|(560,)|var|uint64
output = func_7602(var_7603)
func_7604 = relay.Function([var_7603], output)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7355_call = mod.get_global_var('func_7355')
func_7356_call = mutated_mod.get_global_var('func_7356')
call_7647 = func_7355_call()
call_7648 = func_7355_call()
output = relay.Tuple([call_7647,])
output2 = relay.Tuple([call_7648,])
func_7653 = relay.Function([], output)
mod['func_7653'] = func_7653
mod = relay.transform.InferType()(mod)
output = func_7653()
func_7654 = relay.Function([], output)
mutated_mod['func_7654'] = func_7654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_7729 = relay.TupleGetItem(func_6751_call(), 0)
call_7730 = relay.TupleGetItem(func_6753_call(), 0)
output = call_7729
output2 = call_7730
func_7731 = relay.Function([], output)
mod['func_7731'] = func_7731
mod = relay.transform.InferType()(mod)
mutated_mod['func_7731'] = func_7731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mutated_mod.get_global_var('func_7731')
call_7732 = func_7731_call()
output = call_7732
func_7733 = relay.Function([], output)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7753 = func_7106_call()
call_7754 = func_7106_call()
func_3822_call = mod.get_global_var('func_3822')
func_3827_call = mutated_mod.get_global_var('func_3827')
const_7759 = relay.const(10, dtype = "uint32")#candidate|7759|()|const|uint32
const_7760 = relay.const([[-3,-5,1,1,4,-3,-4,2,9,7,-7,9,-7,9,-6,-2,8,-7,9,6,2,6,8,1],[1,9,-6,-6,-3,-8,-3,-9,-6,-9,6,10,5,-3,4,-2,5,5,-10,-4,-7,3,3,-1],[2,-5,3,6,9,-3,-7,-8,-8,4,5,2,-2,-1,1,-5,-10,-1,4,-3,9,8,2,-10],[10,-8,-4,4,-7,3,5,-9,6,9,9,5,-9,6,10,2,10,2,2,3,10,-5,4,1],[-8,-2,-4,5,-9,-7,-6,8,10,-1,-5,-2,-10,2,-5,-6,5,7,4,-5,4,-3,-2,6],[10,-8,4,1,-9,10,8,-4,-3,-2,-5,-1,10,9,2,8,7,-6,-6,-6,2,6,3,10],[-2,-4,-1,8,-8,7,-4,-3,-1,-3,8,1,-7,-7,-8,8,-1,-9,-9,6,-5,7,-10,-10],[1,-7,3,8,-4,2,-2,-1,5,7,-8,9,-8,3,-9,8,-6,-9,-10,9,-10,5,1,6],[8,8,-10,9,5,7,-5,-4,-7,-10,-7,-10,-9,-10,-1,-6,4,6,3,2,-9,2,4,-7],[-8,-8,7,4,3,6,-2,4,6,-10,7,-7,-2,2,-6,7,-7,8,2,-2,6,8,10,-6],[2,-3,1,-5,10,9,8,9,2,1,-9,-1,-1,-5,-3,-7,-8,-3,-2,-1,6,6,7,-1],[-5,5,5,1,8,-9,8,5,-6,-4,-9,-1,-7,8,4,-5,2,-3,9,-5,1,-8,-9,4],[3,4,-4,-6,-3,7,6,6,-3,4,-4,-8,4,3,-9,9,-8,-4,9,3,4,1,1,7],[8,-7,2,-7,-1,10,-1,4,1,2,-5,3,-5,9,-2,2,-10,2,6,10,2,-9,-6,-2],[8,10,1,5,8,3,-2,9,4,6,1,-9,-4,7,9,1,-5,3,4,3,-1,3,-9,-7],[-4,-5,7,-9,2,10,-7,-1,2,10,3,10,-8,-9,-7,-4,-7,7,2,-2,-4,-8,-5,-5],[6,-5,-7,-2,9,-3,-6,-7,-5,7,-4,4,5,-1,2,9,9,6,8,10,9,-4,-8,2],[-7,3,-9,-9,10,7,4,-1,-10,9,-4,5,-2,-2,8,-6,-2,8,7,-8,-7,-8,-10,6],[-5,-6,-5,4,-8,10,10,-4,-6,-4,10,-9,-4,2,5,4,4,-10,-10,8,3,-7,5,-3],[-2,5,8,8,10,-8,9,-8,-1,-4,5,1,2,-10,9,-10,-2,-2,-1,-4,2,8,5,4],[6,-9,10,8,-7,-10,6,7,7,10,-10,8,8,3,4,9,5,-1,-7,-6,-1,-3,6,-5],[-9,-8,-9,1,4,1,1,-8,-8,-1,1,-9,4,9,2,-3,-7,10,-7,3,6,9,-4,4],[-7,-6,2,1,9,-6,-4,-10,9,-6,10,8,-5,-3,-6,-2,-2,1,6,-10,4,6,4,-8],[7,-9,-5,-2,4,1,4,2,2,2,9,-4,9,-10,7,3,-4,-2,-9,-9,-4,4,-2,4],[2,-5,-7,6,1,8,-6,4,3,-8,4,7,6,4,10,5,5,4,8,-7,-8,9,-7,-3],[-10,-5,8,10,5,-5,3,8,-9,9,4,6,-2,5,7,10,-1,-2,6,5,6,-8,-2,-7],[1,-8,-2,7,9,-1,-2,-6,5,1,9,-7,-8,6,-1,10,-8,5,3,4,-3,-10,8,-7],[-3,-8,-4,9,-8,-1,7,1,10,-5,-9,6,-8,9,4,10,-4,-2,-1,-2,6,-8,-7,-8],[4,-9,-6,6,-3,9,9,-7,-8,-1,1,-8,9,2,6,2,-5,4,5,-5,-3,8,-4,4],[5,10,3,5,-3,-7,-8,10,9,7,2,-4,6,8,6,-3,1,1,1,-5,4,3,10,-7],[7,-5,-6,3,-9,-6,-5,8,-10,10,-6,6,-7,-3,-4,8,-4,10,1,6,6,-5,-8,-7],[-3,-2,1,10,-8,-7,-3,6,9,1,-1,10,-8,-10,-9,7,-1,-4,6,10,-6,8,3,9],[8,-2,7,-8,-6,-1,3,-10,8,9,-7,-8,8,-4,-8,5,-3,6,-8,4,3,10,5,2],[-3,7,-4,4,-3,-4,-1,8,3,-1,10,-6,3,9,-5,3,-4,1,7,9,-4,-10,10,-9],[4,6,7,7,8,-8,-6,5,1,-9,3,-8,-1,-4,-10,5,-2,10,-7,-7,-10,9,6,-8],[-4,-7,5,6,6,8,-2,2,6,-3,-6,7,7,-5,-4,2,-10,-6,6,2,1,-10,2,9],[3,-2,-4,6,-9,-6,4,2,9,-2,10,-9,-3,-6,-10,-5,-4,-3,-8,-2,9,-9,-8,-10],[8,3,5,1,-8,3,1,-2,-6,5,-3,-10,-5,-7,1,1,9,-9,6,10,-8,-4,2,-4],[-1,2,-6,-8,9,-5,3,10,-1,-4,-1,-5,-9,6,6,-10,8,1,-2,6,-4,-4,8,9],[-4,-10,-9,-4,3,10,1,-6,-1,5,-6,7,-4,7,6,3,8,5,-6,6,10,-9,-5,9],[2,1,7,-7,10,2,7,6,-9,-3,-1,-6,-4,-1,2,6,8,-3,5,5,-4,-9,-2,-8],[-7,8,9,-10,-1,-1,3,-8,-5,5,10,5,-6,-7,-1,-1,-8,-8,-3,2,-9,6,10,-10],[-2,5,4,-8,-6,9,1,-8,9,8,4,5,-2,-3,4,7,10,-9,-4,5,1,-1,-3,3],[-7,-3,10,-4,8,5,5,-9,-6,1,3,-3,-1,-9,3,8,3,-3,-9,3,6,-1,-10,8],[-7,7,5,8,-4,2,-9,9,2,-4,1,-2,5,-8,4,-4,-4,-4,-3,-7,-9,4,1,-1],[7,8,3,5,-3,-7,-8,9,2,-3,4,-9,10,3,1,6,1,6,-4,-4,-3,-6,-9,-4],[-6,3,-8,-7,10,-4,5,-10,4,10,8,-6,2,3,5,-2,6,-5,2,7,-3,4,10,4],[-10,3,8,-1,1,4,3,9,3,-8,-7,8,3,-7,6,7,8,5,9,-10,2,-6,-10,-6]], dtype = "uint32")#candidate|7760|(48, 24)|const|uint32
var_7761 = relay.var("var_7761", dtype = "bool", shape = (1008,))#candidate|7761|(1008,)|var|bool
call_7758 = relay.TupleGetItem(func_3822_call(relay.reshape(const_7759.astype('uint32'), []), relay.reshape(const_7760.astype('uint32'), [12, 16, 6]), relay.reshape(var_7761.astype('bool'), [1008,]), ), 0)
call_7762 = relay.TupleGetItem(func_3827_call(relay.reshape(const_7759.astype('uint32'), []), relay.reshape(const_7760.astype('uint32'), [12, 16, 6]), relay.reshape(var_7761.astype('bool'), [1008,]), ), 0)
func_1756_call = mod.get_global_var('func_1756')
func_1759_call = mutated_mod.get_global_var('func_1759')
var_7767 = relay.var("var_7767", dtype = "int64", shape = (780,))#candidate|7767|(780,)|var|int64
call_7766 = relay.TupleGetItem(func_1756_call(relay.reshape(const_7759.astype('int64'), []), relay.reshape(var_7767.astype('int64'), [6, 10, 13]), ), 0)
call_7768 = relay.TupleGetItem(func_1759_call(relay.reshape(const_7759.astype('int64'), []), relay.reshape(var_7767.astype('int64'), [6, 10, 13]), ), 0)
output = relay.Tuple([call_7753,call_7758,const_7759,const_7760,var_7761,call_7766,var_7767,])
output2 = relay.Tuple([call_7754,call_7762,const_7759,const_7760,var_7761,call_7768,var_7767,])
func_7783 = relay.Function([var_7761,var_7767,], output)
mod['func_7783'] = func_7783
mod = relay.transform.InferType()(mod)
mutated_mod['func_7783'] = func_7783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7783_call = mutated_mod.get_global_var('func_7783')
var_7785 = relay.var("var_7785", dtype = "bool", shape = (1008,))#candidate|7785|(1008,)|var|bool
var_7786 = relay.var("var_7786", dtype = "int64", shape = (780,))#candidate|7786|(780,)|var|int64
call_7784 = func_7783_call(var_7785,var_7786,)
output = call_7784
func_7787 = relay.Function([var_7785,var_7786,], output)
mutated_mod['func_7787'] = func_7787
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7807 = func_7106_call()
call_7808 = func_7106_call()
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7825 = func_7205_call()
call_7826 = func_7205_call()
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_7833 = func_7106_call()
call_7834 = func_7106_call()
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
var_7840 = relay.var("var_7840", dtype = "bool", shape = (1008, 1))#candidate|7840|(1008, 1)|var|bool
call_7839 = func_1619_call(relay.reshape(var_7840.astype('bool'), [14, 6, 12]), relay.reshape(var_7840.astype('bool'), [14, 6, 12]), )
call_7841 = func_1619_call(relay.reshape(var_7840.astype('bool'), [14, 6, 12]), relay.reshape(var_7840.astype('bool'), [14, 6, 12]), )
func_7216_call = mod.get_global_var('func_7216')
func_7218_call = mutated_mod.get_global_var('func_7218')
call_7843 = func_7216_call()
call_7844 = func_7216_call()
bop_7879 = relay.equal(var_7840.astype('bool'), relay.reshape(call_7839.astype('bool'), relay.shape_of(var_7840))) # shape=(1008, 1)
bop_7882 = relay.equal(var_7840.astype('bool'), relay.reshape(call_7841.astype('bool'), relay.shape_of(var_7840))) # shape=(1008, 1)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7890 = func_7205_call()
call_7891 = func_7205_call()
output = relay.Tuple([call_7807,call_7825,call_7833,call_7843,bop_7879,call_7890,])
output2 = relay.Tuple([call_7808,call_7826,call_7834,call_7844,bop_7882,call_7891,])
func_7925 = relay.Function([var_7840,], output)
mod['func_7925'] = func_7925
mod = relay.transform.InferType()(mod)
mutated_mod['func_7925'] = func_7925
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7926 = relay.var("var_7926", dtype = "bool", shape = (1008, 1))#candidate|7926|(1008, 1)|var|bool
func_7925_call = mutated_mod.get_global_var('func_7925')
call_7927 = func_7925_call(var_7926)
output = call_7927
func_7928 = relay.Function([var_7926], output)
mutated_mod['func_7928'] = func_7928
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7517_call = mod.get_global_var('func_7517')
func_7518_call = mutated_mod.get_global_var('func_7518')
call_7938 = relay.TupleGetItem(func_7517_call(), 1)
call_7939 = relay.TupleGetItem(func_7518_call(), 1)
func_7482_call = mod.get_global_var('func_7482')
func_7485_call = mutated_mod.get_global_var('func_7485')
const_7948 = relay.const([[4.102119,7.198297,5.119119,-3.134716,-9.147147],[6.184082,-2.189074,-2.730695,1.412872,8.774825],[1.966678,-5.389002,1.248393,1.194048,-5.004701],[-9.497563,-9.177712,-4.091190,1.569167,-8.255799],[-0.994886,7.502952,3.580348,-3.123851,0.227750],[-2.925760,2.519137,3.048540,6.831172,-6.652219],[5.414199,0.427067,-5.281669,1.039418,4.630538],[9.824557,3.668689,-6.455929,-9.257497,-7.847725],[7.664105,3.261991,9.400318,7.816753,8.046042],[6.395890,-5.627120,-9.274914,-3.723444,3.406104],[-7.709844,8.567440,2.215466,-9.815581,-9.883328],[2.850516,0.289985,-5.411558,9.899194,3.925517],[6.597603,8.660493,-8.060337,-9.479851,-9.690588],[-2.481257,1.324048,-8.236055,5.652805,-8.779086]], dtype = "float64")#candidate|7948|(14, 5)|const|float64
call_7947 = relay.TupleGetItem(func_7482_call(relay.reshape(const_7948.astype('float64'), [5, 2, 7])), 0)
call_7949 = relay.TupleGetItem(func_7485_call(relay.reshape(const_7948.astype('float64'), [5, 2, 7])), 0)
output = relay.Tuple([call_7938,call_7947,const_7948,])
output2 = relay.Tuple([call_7939,call_7949,const_7948,])
func_7952 = relay.Function([], output)
mod['func_7952'] = func_7952
mod = relay.transform.InferType()(mod)
mutated_mod['func_7952'] = func_7952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mutated_mod.get_global_var('func_7952')
call_7953 = func_7952_call()
output = call_7953
func_7954 = relay.Function([], output)
mutated_mod['func_7954'] = func_7954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_7955 = relay.TupleGetItem(func_7653_call(), 0)
call_7956 = relay.TupleGetItem(func_7654_call(), 0)
func_3822_call = mod.get_global_var('func_3822')
func_3827_call = mutated_mod.get_global_var('func_3827')
const_7974 = relay.const(-2, dtype = "uint32")#candidate|7974|()|const|uint32
var_7975 = relay.var("var_7975", dtype = "uint32", shape = (1152,))#candidate|7975|(1152,)|var|uint32
var_7976 = relay.var("var_7976", dtype = "bool", shape = (1008,))#candidate|7976|(1008,)|var|bool
call_7973 = relay.TupleGetItem(func_3822_call(relay.reshape(const_7974.astype('uint32'), []), relay.reshape(var_7975.astype('uint32'), [12, 16, 6]), relay.reshape(var_7976.astype('bool'), [1008,]), ), 2)
call_7977 = relay.TupleGetItem(func_3827_call(relay.reshape(const_7974.astype('uint32'), []), relay.reshape(var_7975.astype('uint32'), [12, 16, 6]), relay.reshape(var_7976.astype('bool'), [1008,]), ), 2)
func_3692_call = mod.get_global_var('func_3692')
func_3694_call = mutated_mod.get_global_var('func_3694')
var_7979 = relay.var("var_7979", dtype = "uint64", shape = (256,))#candidate|7979|(256,)|var|uint64
call_7978 = relay.TupleGetItem(func_3692_call(relay.reshape(var_7979.astype('uint64'), [4, 8, 8])), 0)
call_7980 = relay.TupleGetItem(func_3694_call(relay.reshape(var_7979.astype('uint64'), [4, 8, 8])), 0)
func_3822_call = mod.get_global_var('func_3822')
func_3827_call = mutated_mod.get_global_var('func_3827')
call_7987 = relay.TupleGetItem(func_3822_call(relay.reshape(const_7974.astype('uint32'), []), relay.reshape(var_7975.astype('uint32'), [12, 16, 6]), relay.reshape(call_7973.astype('bool'), [1008,]), ), 0)
call_7988 = relay.TupleGetItem(func_3827_call(relay.reshape(const_7974.astype('uint32'), []), relay.reshape(var_7975.astype('uint32'), [12, 16, 6]), relay.reshape(call_7973.astype('bool'), [1008,]), ), 0)
output = relay.Tuple([call_7955,call_7973,const_7974,var_7975,var_7976,call_7978,var_7979,call_7987,])
output2 = relay.Tuple([call_7956,call_7977,const_7974,var_7975,var_7976,call_7980,var_7979,call_7988,])
func_7999 = relay.Function([var_7975,var_7976,var_7979,], output)
mod['func_7999'] = func_7999
mod = relay.transform.InferType()(mod)
mutated_mod['func_7999'] = func_7999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7999_call = mutated_mod.get_global_var('func_7999')
var_8001 = relay.var("var_8001", dtype = "uint32", shape = (1152,))#candidate|8001|(1152,)|var|uint32
var_8002 = relay.var("var_8002", dtype = "bool", shape = (1008,))#candidate|8002|(1008,)|var|bool
var_8003 = relay.var("var_8003", dtype = "uint64", shape = (256,))#candidate|8003|(256,)|var|uint64
call_8000 = func_7999_call(var_8001,var_8002,var_8003,)
output = call_8000
func_8004 = relay.Function([var_8001,var_8002,var_8003,], output)
mutated_mod['func_8004'] = func_8004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_8014 = relay.TupleGetItem(func_6751_call(), 0)
call_8015 = relay.TupleGetItem(func_6753_call(), 0)
output = relay.Tuple([call_8014,])
output2 = relay.Tuple([call_8015,])
func_8021 = relay.Function([], output)
mod['func_8021'] = func_8021
mod = relay.transform.InferType()(mod)
output = func_8021()
func_8022 = relay.Function([], output)
mutated_mod['func_8022'] = func_8022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_8079 = relay.TupleGetItem(func_8021_call(), 0)
call_8080 = relay.TupleGetItem(func_8022_call(), 0)
output = relay.Tuple([call_8079,])
output2 = relay.Tuple([call_8080,])
func_8090 = relay.Function([], output)
mod['func_8090'] = func_8090
mod = relay.transform.InferType()(mod)
output = func_8090()
func_8091 = relay.Function([], output)
mutated_mod['func_8091'] = func_8091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_8124 = func_7106_call()
call_8125 = func_7106_call()
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_8158 = func_7106_call()
call_8159 = func_7106_call()
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_8165 = func_7731_call()
call_8166 = func_7731_call()
output = relay.Tuple([call_8124,call_8158,call_8165,])
output2 = relay.Tuple([call_8125,call_8159,call_8166,])
func_8192 = relay.Function([], output)
mod['func_8192'] = func_8192
mod = relay.transform.InferType()(mod)
mutated_mod['func_8192'] = func_8192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8192_call = mutated_mod.get_global_var('func_8192')
call_8193 = func_8192_call()
output = call_8193
func_8194 = relay.Function([], output)
mutated_mod['func_8194'] = func_8194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_8195 = relay.TupleGetItem(func_7653_call(), 0)
call_8196 = relay.TupleGetItem(func_7654_call(), 0)
func_7405_call = mod.get_global_var('func_7405')
func_7408_call = mutated_mod.get_global_var('func_7408')
const_8200 = relay.const([7.980968,-2.898812,-3.987954,8.248968,2.948445,-8.049430,2.385173,-9.810150,-8.438754,-6.095432,7.328505,-3.814103,-4.841497,9.823661,-1.585683,-4.764569,3.834525,0.470809,-5.514076,3.085055,-5.343269,8.240688,0.971430,-3.724060,-2.285998,-0.391971,-8.643292,1.048328,-2.693426,-1.211444,-8.067658,-3.563908,-4.182729,1.233875,-9.769596,-6.660128,-2.731161,-2.524167,-2.897078,6.189111,3.261266,-6.220510,8.567440,-5.761240,8.350599,-4.404138,-8.404064,5.045383,-9.064297,0.698087,6.599789,7.735198,4.594147,2.592480,-1.698126,-2.767255,-6.820701,7.230199,-8.915008,8.680304,9.189417,-7.990897,-0.221631,-3.645194,-9.910143,7.588909,9.921073,-8.690664,-4.444856,-2.198101,-1.426086,-5.840200,-4.853282,-3.985461,-8.169504,-8.557515,-1.895501,9.298774,-3.323469,9.121306,6.254683,-8.359398,-4.938322,0.417917,5.910884,8.214050,7.132153,-9.662601,-2.021665,-7.265474,6.796437,-0.289055,8.783981,-4.008804,7.919293,8.234945,3.001100,9.370071,-9.455697,-5.107129,4.978342,3.153288,-9.987740,-2.517751,2.132130,2.114507,0.564206,-8.600687,3.554473,-7.101396,-0.662588,3.067196,5.017985,8.850248,6.934286,7.689999,-2.580274,2.858573,1.787636,2.585927,5.936363,7.607482,-4.065036,5.431126,-7.378477,-5.872522,6.386608,-6.383066,-0.429844,-0.224548,-4.584073,-5.537126,0.756360,3.899360,4.257054,6.288716,9.921979,4.657726,-5.063715,7.525507,-5.150452,7.835921,5.961301,2.347452,-3.630614,8.183042,8.608207,5.383778,-9.089984,1.398386,5.485738,-7.009242,6.050884,-8.111627,-9.457360,7.659068,0.262088,7.610625,-3.887367,-5.838819,-7.984579,9.719442,-1.591446,-1.017089,9.972921,-3.628571,-1.638833,5.308229,0.645088,6.058506,0.720946,-8.848831,-5.194862,8.655546,-2.901248,6.450463,-9.370585,8.732330,8.008582,2.210646,8.658755,2.138962,-8.806190,-9.067373,-6.716411,9.882178,-5.447136,-3.720665,4.337105,9.180624,8.050017,0.874085,-3.299502,-1.735360,-0.419750,-1.208310,-7.259028,-2.412343,4.274529,-7.612860,-3.986926,6.728317,5.384905,1.938423,-9.760372,7.234612,3.720782,8.948915,1.738333,0.096244,1.477020,1.269710,3.452707,-8.975494,-9.242982,-8.148567,-8.810531,0.814714,1.995656,9.468677,-9.644227,-3.927075,0.737211,0.316565,1.018918,-3.599055,-1.218684,-8.193455,7.526140,-3.677801,6.300700,0.327873,7.738427,-0.083697,9.194166,-7.205282,-4.344155,-6.778960,-2.067219,-7.241731,-0.830334,-6.473977,-9.968302,1.819551,5.480509,-8.118593,-4.849006,-0.523355,-4.425893,0.623920,-5.645443,2.978677,-4.039356,-3.662407,9.707310,-0.994223,-6.153427,2.247753,-8.867869,-7.176107,-9.627237,-5.655804,-7.992670,-2.578737,0.749926,4.045706,5.482952,-7.238617,-8.636272,-5.929125,2.159319,4.605164,1.970773,0.384623,3.727054,2.128584,-4.005880,7.568698,6.994000,1.930448,1.630122,-2.250887,-8.958565,-7.381601,-8.353245,-7.335727,3.060154,3.716397,-7.403812,-4.293291,-1.978879,-8.101836,-0.790722,-2.891308,5.260627,-5.685385,-5.449354,-5.637218,-3.435569,1.347615,5.564052,-7.512859,3.577004,-3.580171,-1.115655,-7.270055,-6.479351,1.321771,-9.293770,-4.601256,-9.337150,-4.921842,-6.141246,0.076982,8.978116,2.724386,-0.942148,0.106446,2.743876,-5.676022,7.244121,-8.871867,9.237193,-1.953579,7.806234,5.389818,1.144874,-7.511196,-3.633023,-7.408860,-7.509614,7.452770,-1.009560,6.191017,-6.598590,1.912178,-8.854366,8.256991,-0.698322,7.577965,9.366929,2.966786,-9.562162,-6.306312,7.616989,-2.490433,-6.684233,-7.625842,-6.831689,-6.667722,1.666068,-4.497809,7.697264,1.885044,9.111486,-1.009426,-9.564353,-6.518280,0.338192,9.600780,9.198131,7.381575,9.367315,-0.467034,8.053980,-3.050504,5.844629,-9.454525,5.758810,-5.098028,-7.833216,6.572799,-2.152573,8.919693,-0.746704,-6.556553,-3.819080,4.341162,3.005229,4.269979,-0.117430,-2.060408,6.739932,-1.218422,-0.707509,6.511124,0.301399,7.447886,-5.343063,-8.492555,-2.441091,7.915478,-6.495881,-1.776509,-1.705152,-4.865700,-7.393700,-9.481187,9.612149,-8.752046,2.058952,-9.997718,-6.643196,-8.585652,-2.553435,2.529000,0.466766,5.890287,9.892158,-9.195379,1.963948,-9.706728,9.055323,9.480684,0.979495,-1.683158,-6.728077,-4.766748,5.522889,3.984062,4.677930,-9.058374,3.367327,-2.828450,0.764183,1.264850,2.969953,-0.629255,-1.640063,6.403880,2.018755,9.424114,-5.366708,-3.160253,-7.547626,0.375525,-9.104765,2.880653,8.822583,-6.729011,-0.027215,5.672098,0.583613,-3.714688,-8.064760,-3.169293,3.002762,2.960599,5.161963,8.731113,1.176733,3.153741,-4.560380,-3.126138,-3.665969,0.774280,-7.581631,-2.010984,-2.493196,9.629896,-5.366975,9.716158,7.889938,3.495680,-5.038428,0.465438,2.789094,-3.865892,9.374614,2.822457,9.488456,-8.490765,1.410637,-7.744480,8.902470,-0.821507,8.555609,3.833111,-9.016334,7.251492,-2.194624,1.736672,4.936837,5.816879,-4.112866,-0.066432,1.044039,2.127965,4.949696,3.147373,4.813760,-8.136862,8.225646,-2.416081,-5.962598,-2.842613,-6.811052,-2.845968,1.183144,-1.228408,-6.833743,-1.980126,3.613182,-5.750494,6.366803,3.441983,-0.626930,5.837622,2.432346,4.100119,2.414242,-9.882865,2.931441,0.539139,7.700100,-5.183368,-7.425972,2.288480,-1.899339,-6.450617,2.429469,2.046316,8.602514,1.088760,-1.388869,-9.793400,4.267424,1.082326,6.926363,5.015542,-9.875957,-8.995779,-6.326743,-6.134297,7.134247,-4.478439,-1.203010,-8.769388,-9.577752,-8.263715,8.517328,-4.274403,-9.439919,8.971121,-5.405795,-5.158502,9.847818,5.760596,-0.550190,-8.262099], dtype = "float32")#candidate|8200|(550,)|const|float32
call_8199 = relay.TupleGetItem(func_7405_call(relay.reshape(const_8200.astype('float32'), [550,])), 3)
call_8201 = relay.TupleGetItem(func_7408_call(relay.reshape(const_8200.astype('float32'), [550,])), 3)
output = relay.Tuple([call_8195,call_8199,const_8200,])
output2 = relay.Tuple([call_8196,call_8201,const_8200,])
func_8212 = relay.Function([], output)
mod['func_8212'] = func_8212
mod = relay.transform.InferType()(mod)
mutated_mod['func_8212'] = func_8212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8212_call = mutated_mod.get_global_var('func_8212')
call_8213 = func_8212_call()
output = call_8213
func_8214 = relay.Function([], output)
mutated_mod['func_8214'] = func_8214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_8221 = relay.TupleGetItem(func_7952_call(), 2)
call_8222 = relay.TupleGetItem(func_7954_call(), 2)
func_5142_call = mod.get_global_var('func_5142')
func_5150_call = mutated_mod.get_global_var('func_5150')
const_8227 = relay.const([[True,True],[False,False],[False,False],[True,True],[True,True],[False,False],[True,False],[True,True],[False,False],[True,True],[False,False],[True,False],[False,False],[False,True],[False,True],[False,True],[False,False],[False,False],[True,True],[True,False],[False,False],[False,True],[False,True],[True,False],[True,False],[True,False],[False,False],[False,False],[False,False],[True,False],[True,True],[False,False],[False,False],[False,True],[True,False],[True,True],[False,True],[True,False],[False,False],[True,True],[False,False],[True,False],[True,True],[False,True],[True,True],[False,True],[True,False],[True,True],[False,True],[False,True],[True,True],[False,True],[False,True],[False,False],[True,True],[True,True],[True,True],[True,False],[False,True],[False,False],[True,False],[True,False],[False,False],[True,False],[True,True],[True,True],[False,True],[False,False],[True,False],[False,False],[True,True],[False,True],[False,True],[True,True],[True,True],[True,False],[True,False],[False,True],[False,True],[True,True],[False,False],[False,False],[False,True],[False,True],[True,False],[True,True],[True,True],[False,False],[True,True],[True,False],[True,False],[False,False],[False,False],[False,False],[True,True],[True,True],[False,False],[True,False],[True,True],[True,False],[True,False],[True,False],[False,True],[False,True],[True,True],[True,False],[True,True],[False,True],[True,False],[True,False],[False,True],[True,False],[True,False],[False,False],[True,True],[False,False],[True,False],[False,True],[True,True],[False,False],[False,True],[False,False],[False,True],[True,True],[True,True],[True,True],[False,False],[True,True],[False,True],[True,True],[False,True],[True,False],[True,False],[True,True],[True,False],[True,True],[True,False],[True,False],[True,True],[True,False],[False,True],[False,False],[True,True],[True,False],[True,False],[True,True],[True,True],[True,True],[True,True],[False,False],[True,True],[True,False],[True,True],[False,False],[False,False],[True,False],[True,True],[False,False],[False,True],[False,True],[True,False],[True,False],[True,False],[True,False],[True,True],[False,False],[True,True],[True,False],[False,True],[True,False],[True,False],[False,False],[True,False],[True,True],[True,True],[True,False],[True,False],[True,False],[False,False],[False,False],[False,False],[False,True],[False,True],[True,False],[True,False],[True,False],[False,True],[True,True],[False,False],[True,True],[True,False],[False,True],[False,True],[True,False],[True,False],[False,True],[False,True],[False,False],[False,False],[True,True],[False,False],[False,True],[True,True],[False,True],[True,True],[True,False],[True,True],[True,True],[False,True],[False,True],[True,False],[True,True],[True,True],[False,False],[True,True],[True,False],[True,True],[True,False],[False,True],[False,True],[True,True],[False,False],[False,True],[False,False],[False,False],[True,True],[False,False],[True,False],[False,True],[False,True],[False,True],[True,True],[True,False],[True,True],[False,True],[True,True],[False,True],[True,False],[False,True],[False,True],[True,False],[False,False],[False,True],[False,False],[False,False],[False,False],[True,True],[True,False],[False,True],[False,False],[False,True],[True,True],[False,False],[True,False],[False,False],[True,True],[False,False],[True,False],[True,True],[True,False],[True,True],[False,True],[False,False],[True,False],[True,True],[False,True],[False,True],[False,False],[False,False],[True,False],[False,False],[True,False],[False,True],[False,False],[False,True],[False,False],[False,False],[True,True],[False,False],[True,True],[False,False],[True,False],[True,True],[True,True],[True,False],[True,True],[False,True],[True,True],[False,False],[True,False],[True,True],[False,False],[True,True],[True,False],[False,False],[True,False],[False,False],[False,False],[False,True],[True,True],[True,True],[True,False],[False,False],[True,False],[False,False],[False,False],[True,True],[False,False],[False,True],[False,False],[True,False],[False,False],[False,True],[False,False],[False,True],[False,False],[False,True],[False,False],[True,True],[False,False],[True,True],[False,False],[False,False],[False,False],[True,True],[True,False],[True,True],[False,True],[False,False],[False,True],[False,False],[True,False],[True,True],[True,False],[False,True],[False,True],[False,False],[True,False],[False,True],[True,True],[False,False],[False,True],[True,False],[True,False],[True,True],[True,True],[True,False],[True,False],[True,False],[False,True],[False,True],[False,False],[True,True],[True,False],[False,False],[True,True],[False,True],[False,True],[False,True],[True,True],[False,False],[False,True],[False,True],[True,True],[False,False],[False,False],[True,False],[False,False],[True,True],[False,False],[True,False],[True,True],[True,True],[True,True],[True,False],[False,True],[True,False],[True,True],[False,False],[True,False],[False,True],[False,True],[False,False],[False,True],[False,False],[True,True],[False,False],[True,False],[False,False],[True,True],[False,False],[False,True],[False,True],[True,False],[False,False],[False,False],[True,False],[False,True],[True,False],[True,True],[False,False],[False,True],[True,True],[True,True],[True,False],[False,False],[False,False],[True,True],[False,False],[True,False],[False,False],[False,False],[False,False],[True,True],[False,False],[False,True],[True,True],[False,False],[False,True],[True,False],[True,True],[False,False],[True,True],[True,True],[False,False],[True,False],[False,False],[False,True],[False,False],[False,True],[False,True],[False,True],[False,False],[True,False],[True,False],[False,False],[True,False],[False,True],[False,True],[False,False],[False,False],[False,False],[False,True],[True,False],[True,False],[True,True],[True,True],[True,True],[True,False],[True,False],[True,False],[True,False],[False,True],[True,False],[True,False],[False,True],[False,True],[True,False],[False,True],[False,True],[True,False],[False,False],[True,True],[True,True],[False,False],[True,True],[False,False],[True,True],[False,True],[True,True],[True,False],[False,True],[True,True],[True,True],[False,True],[False,True],[True,False],[True,True],[False,False],[False,False],[True,True],[True,True],[False,False],[False,False],[True,False],[True,False],[False,True],[True,True],[False,False],[False,True],[False,False],[False,True],[False,False],[False,False],[False,False],[False,True],[False,True],[True,False],[False,True],[False,True],[True,True],[False,True],[False,True],[False,False]], dtype = "bool")#candidate|8227|(504, 2)|const|bool
const_8228 = relay.const(-3, dtype = "int16")#candidate|8228|()|const|int16
const_8229 = relay.const([-1,4,-5,9,3,-3,10,8,-7,-1,-10,2,7,5,4,-8,3,10,8,-3,-7,-2,4,2,-2,4,-10,-6,-8,6,9,1,-7,9,10,-10,10,-3,10,6,6,6,6,2,-4,-10,-4,6,-3,1,-7,-10,3,-3,-9,-6,1,-1,-5,5,-3,4,-7,1,5,3,4,-1,9,9,3,2,-9,-2,-8,-6,1,8,-10,8,-2,-9,6,-3,-4,-2,-10,-2,7,-5,-9,6,3,-8,5,-10,4,-5,-9,-5,3,-1,-2,-5,-7,6,3,5,-7,1,-6,-1,2,3,6,-6,5,-3,-10,-8,9,4,7,10,-4,-6,-1,5,2,-7,-7,-9,-10,-9,-1,9,2,-1,-5,-1,-1,-1,5,-8,-5,-7,-5,5,7,8,-3,-7,10,-4,-1,8,-3,4,7,4,8,2,-8,-9,-1,4,-3,8,10,-2,6,-3,-1,6,-1,-7,4,2,-6,-8,9,-2,-6,8,4,-9,2,-3,10,-8,-2,2,6,-9,-7,3,2,10,8,3,10,6,3,4,9,-6,6,-8,-10,-7,5,-4,-5,-4,-4,9,-1,7,-4,-7,2,-3,-9,-3,9,9,9,-2,10,9,5,10,-3,-1,-10,10,-2,-2,-4,-4,-6,7,-6,10,-5,2,7,7,10,6,6,4,7,-3,-3,-3,9,4,9,3,-5,7,6,-3,-1,8,5,9,10,-6,-6,1,9,3,1,5,1,-1,5,5,5,7,-7,-3,-6,-1,-7,10,-10,-5,8,-9,1,6,-6,-6,-6,10,-9,2,1,2,6,6,-6,8,-3,3,-9,-4,1,3,-2,3,-7,1,-10,7,-4,3,4,-3,8,-10,4,9,3,5,8,-9,2,-2,2,8,2,7,3,-10,-6,8,-6,7,1,-5,9,4,5,-4,7,6,-3,5,10,7,-8,8,-1,1,9,3,-1,7,-4,6,5,3,2,-6,-3,-10,9,3,7,4,-2,-1,-5,-3,-1,4,-1,-6,3,5,4,-7,7,2,5,-7,-4,-2,-1,10,3,10,1,7,5,-9,9,-1,-5,-10,1,-9,-8,-4,5,-2,1,2,-7,5,-1,2,-2,8,-6,-10,-6,1,-10,-2,2,3,6,-5,-6,-7,-7,-9,-10,10,5,-4,-9,-4,4,3,-2,9,-6,2,-7,9,6,4,-4,3,-4,-10,-5,-1,-10,5,3,-9,10,-10,-8,10,-6,-1,9,-2,2,6,-6,-6,-1,6,7,-2,-9,-6,1,3,2,-10,10,4,3,9,6,6,10,-3,9,6,10,-7,7,8,5,-10,1,-7,5,4,3,9,3,-10,9,-10,-9,-10,8,6,10,-6,-2,-5,-1,8,-10,9,1,6,7,-1,-5,-3,-2,6,-6,3,7,7,-9,-4,-4,-4,2,6,-8,-6,-1,9,7,-5,2,-3,8,-9,-4,9,5,2,-3,-7,-7,-7,-1,2,-4,10,-7,-4,-2,-3,5,-4,-5,-8,-5,3,-7,10,7,-5,-1,6,10,4,-3,10,-8,8,1,4,-8,-7,5,4,-1,6,4,1,-4,-5,3,4,-10,-5,-6,-6,-3,-1,10,4,-4,5,-2,1,-3,-2,-4,10,-9,-4,5,9,-2,-8,-8,6,-5,-2,-9,-5,-1,-3,-5,10,7,7,5,9,10,10,4,-4,8,7,8,4,-1,8,-9,8,-2,7,4,-5,-7,-4,2,9,-3,9,-10,-3,-9,7,-9,3,1,-1,8,-9,2,8,-1,-5,-5,6,-9,-8,-1,-6,1,6,-1,-7,4,6,1,-1,10,7,-10,1,-3,10,6,-6,5,-9,10,5,-5,-9,2,-9,6,8,-2,-7,-9,-10,-3,4,-10,-4,2,-4,2,-3,5,-9,-9,-9,5,5,1,3,-4,3,9,-6,-9,-7,-8,-5,2,4,-10,-4,8,-3,7,-4,10,-4,-5,9,3,-4,4,-3,-3,10,9,10,-5,6,-8,10,-6,-6,-7,4,3,-10,-7,-5,-10,-6,1,6,-1,-6,3,-7,-4,-1,-10,-2,10,9,-7,-10,1,7,1,8,6,-9,1,7,10,8,-10,2,4,-1,-6,-9,-4,1,-10,7,4,-4,-3,10,-8,3,9,-1,-7,-4,-1,1,9,-3,2,6,10,-9,-10,8,7,7,-7,9,-1,6,-5,-9,1,-7,4,7,3,8,-6,3,-8,-1,3,8,4,5,-10,-6,-8,4,-6,7,8,5,4,9,-2,-6,2,-6,7,-8,10,10,6,-2,-4,4,-6,3,-8,-1,-3,-3,10,-1,-5,-4,2,-4,5,-3,-7,-10,-7,-3,7,3,-1,-7,10,-6,7,-9,-1,1,9,6,2,-10,-8,2,-7,5,3,-10,10,-7,5,7,-1,3,-4,-5,-4,-3,-8,-8,-2,-4,5,-8,-10,-3,3,3,10,-1,7,-1,2,5,-9,-6,6,-5,-4,7,8,-2,-1,2,-5,8,-10,4,10,-2,2,9,-10,8,-7,-9,-4,5,-8,-9,-3,-4,3,-7,-7,4,-8,5,9,-1,8,-3,-3,-8,-7,-1,-1,3,2,6,10,-9,3,6,9,10,9,10,2,-2,-4,-1,-7,8,6,-1,6,-5,-3,-2,-10,8,6,1,5,-8,6,3,-4,5,8,8,-3,2,-6,8,9,-5,-5,2,8,10,-7,-9,5,3,-7,7,4,8,8,-3,-4,-9,-5,-1,-8,8,6,-8,-9,-6,10,8,5,-3,4,9,6,-8,-8,5,2,5,3,10,-4,10,-10,-7,6,7,8,9,3,-7,8,10,7,9,7,-4,6,5,4,-10,-6,2,4,-9,9,-9,-10,-7,2,-9,-5,-10,-6,-4,10,3,-4,9,-6,-4,-4,2,-2,3,4,5,-6,8,-1,-4,-10,-7,2,2,-4,-3,-1,-6,-3,-9,2,6,-8,-10,1,-1,3,-5,6,4,-4,-2,-1,8,-7,9,-10,7,-1,8,-5,3,9,-4,5,-4,-7,4,5,10,-10,1,-5,-7,-7,10,-3,1,-1,4,-5,7,-7,7,-4,3,-7,-3,5,3,-2,-6,-6,-7,-4,-4,-1,10,-3,-9,-6,-2,-1,9,2,9,-5,-1,4,9,-8,6,4,-9,-6,6,5,7,1,-9,8,-9,5,-3,9,-8,4,8,3,-7,-8,-1,10,-6,-3,-6,-4,-5,6,-1,-1,1,4,-5,7,-4,-6,-7,-2,-7,-1,-10,-9,-6,-5,9,-8,1,-2,-9,-2,-5,9,-7,8,-7,-9,3,-2,-3,6,2,4,5,4,6,-8,-4,-4,7,-7,8,1,-3,10,1,2,9,-9,-4,10,-8,-1,-3,-5,7,-5,7,-6,-1,10,2,7,10,8,10,-3,4,5,9,8,-4,-10,-8,-3,3,-3,5,-6,8,8,2,10,-5,5,-7,-1,7,1,-8,-6,-10,-5,1,-2,7,-10,-3,-7,5,4,9,10,7,-1,8,5,8,-4,1,-9,8,-7,8,-9,8,-5,-9,2,8,10,-3,-5,4,2,-9,-4,-8,8,-5,-3,2,-9,-4,-6,4,-2,10,-10,9,10,10,-5,-4,-8,-1,1,8,-4,-3,-7,-6,-6,6,-3,-7,-3,8,9,2,-1,8,-6,-6,-1,1,-7,-6,-5,10,-9,2,6,-1,-4,-2,-8,10,9,4,-4,9,-10,-8,-1,-3,-9,-4,7,-10,10,5,-6,-2,1,-6,-9,-8,-4,-5,9,5,5,3,-7,-2,-6,-5,-1,9,10,-9,-4,9,-5,3,4,-10,-9,4,5,-3,4,5,-4,7,2,7,5,4,-2,-4,6,9,6,-1,7,3,-1,-7,5,-3,2,-2,5,6,4,-4,-3,-8,-4,1,-5,5,3,3,9,-6,5,9,6,5,-7,-2,2,9,-1,1,5,1,9,-7,-1,9,-10,6,-6,-6,10,1,-10,-9,-3,6,-6,7,5,4,-6,4,1,-2,8,10,-9,-1,-3,1,-3,-3,6,-6,3,-8,3,5,-9,3,-6,-9,-3,-6,-3,2,4,6,-7,-2,2,-9,2,-9,2,2,4,-5,-2,-3,5,-2,3,8,2,-2,2,7,5,8,-9,-7,4,10,-2,2,10,-6,-3,5,-8,10,-6,5,5,1,4,9,-10,3,-1,9,10,-4,-4,10,6,10,-7,7,8,9,6,9,6,9,-8,9,-8,3,-4,3,-1,3,-10,3,8,10,-8,3,-3,-3,3,-9,9,-2,-4,-4,-8,4,-9,5,-9,-5,-4,-2,1,7,9,4,9,2,10,8,-5,7,-1,5,-5,-6,-9,5,-6,-5,-10,3,-6,5,-3,6,-7,-3,-3,-8,-9,9,-5,-7,9,-7,10,10,-7,3,-10,-7,2,-5,6,-5,-2,-2,-9,7,2,8,-4,-9,-5,-10,-3,-2,-4,-2,-2,7,3,10,-8,-1,3,-2,10,-7,-6,-8,1,-4,8,-7,-6,4,-4,3,-3,2,-6,2,-10,10,7,4,7,5,7,6,6,3,6,2,2,5,10,5,8,5,3,-3,9,-6,10,10,-3,4,10,-1,1,2,5,3,-3,9,10,-6,10,5,-5,-5,-7,10,-4,10,6,7,9,5,10,8,5,-9,8,-6,9,3,-10,-1,-1,10,-5,9,10,-8,7,10,-1,-9,-3,2,-4,-7,-6,-1,-1,6,-9,-10,10,-9,3,1,8,-3,-2,-4,7,-3,2,-2,4,-9,-5,-3,-8,-4,-4,4,-4,5,-1,-6,-2,5,-2,7,7,2,6,8,10,4,8,7,7,8,3,-8,3,-1,2,-3,-5,-10,-2,2,4,-7,-5,2,8,-10,6,-8,-3,5,6,-4,-5,-1,-7,-1,10,-1,2,-7,-7,-3,-6,3,-9,-7,-8,-9,7,2,-4,3,8,-9,9,-5,4,9,-9,1,1,-5,1,4,4,2,-6,4,-10,8,-10,6,-1,3,-7,7,4,-7,-8,1,-6,1,-7,-7,9,-6,8,-2,7,6,2,10,-7,-1,9,-8,6,-8,-4,9,10,-2,-9,7,4,8,1,3,8,-5,-7,-3,-10,-5,-5,8,4,-6,-6,7,-8,-5,-4,7,2,8,-4,-10,1,9,-2,1,-8,-6,-10,2,9,-7,6,6,5,-7,4,-1,3,-9,10,-2,9,-1,-3,6,-2,7,-6,-8,-7,-8,-2,-6,-3,-1,-6,-9,3,3,5,-9,2,-9,-9,9,-9,8,8,-6,8,-3,-2,-9,-4,-10,2,8], dtype = "int16")#candidate|8229|(1980,)|const|int16
const_8230 = relay.const([2,3,3,6,3,3,6,1,-6,-10,8,7,-5,-9,-1,-9,4,4,-5,-9,6,-2,-5,-10,5,-6,-5,3,10,-2,-8,-5,4,10,-10,10,10,8,4,-6,9,-4,-5,-4,-8,-7,9,1,-1,-5,-9,-7,-8,4,-3,2,2,-6,-4,-3], dtype = "uint64")#candidate|8230|(60,)|const|uint64
call_8226 = relay.TupleGetItem(func_5142_call(relay.reshape(call_8221.astype('int64'), [5, 2, 7]), relay.reshape(call_8221.astype('int64'), [5, 2, 7]), relay.reshape(call_8221.astype('int64'), [5, 2, 7]), relay.reshape(const_8227.astype('bool'), [1, 1008]), relay.reshape(const_8228.astype('int16'), []), relay.reshape(const_8229.astype('int16'), [1980,]), relay.reshape(const_8230.astype('uint64'), [60,]), ), 6)
call_8231 = relay.TupleGetItem(func_5150_call(relay.reshape(call_8221.astype('int64'), [5, 2, 7]), relay.reshape(call_8221.astype('int64'), [5, 2, 7]), relay.reshape(call_8221.astype('int64'), [5, 2, 7]), relay.reshape(const_8227.astype('bool'), [1, 1008]), relay.reshape(const_8228.astype('int16'), []), relay.reshape(const_8229.astype('int16'), [1980,]), relay.reshape(const_8230.astype('uint64'), [60,]), ), 6)
output = relay.Tuple([call_8221,call_8226,const_8227,const_8228,const_8229,const_8230,])
output2 = relay.Tuple([call_8222,call_8231,const_8227,const_8228,const_8229,const_8230,])
func_8244 = relay.Function([], output)
mod['func_8244'] = func_8244
mod = relay.transform.InferType()(mod)
mutated_mod['func_8244'] = func_8244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8244_call = mutated_mod.get_global_var('func_8244')
call_8245 = func_8244_call()
output = call_8245
func_8246 = relay.Function([], output)
mutated_mod['func_8246'] = func_8246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_8276 = relay.TupleGetItem(func_8021_call(), 0)
call_8277 = relay.TupleGetItem(func_8022_call(), 0)
const_8287 = relay.const([[[-9.108938,3.565910,2.251391,-5.352079,1.333674,2.063169,3.926391],[-8.839254,4.244971,-5.205924,8.271346,-3.208056,2.757763,4.448905],[9.808781,6.556239,-2.600449,4.969974,6.729957,3.166199,-6.076413],[-2.608244,7.937622,2.266832,7.637903,3.087323,9.241639,6.050066],[-7.750733,-4.926495,6.480343,1.593815,-2.566482,4.282376,-3.662385],[-8.784311,2.981436,-2.715419,-6.261444,2.184254,8.072211,-7.608983],[-7.323527,-6.720554,7.615447,9.887011,-7.960422,-9.014077,2.322476]],[[6.081468,8.616984,-7.719839,-8.557111,8.856287,-0.749195,-7.400350],[3.887422,-1.617078,-3.738697,-4.172019,7.408888,-0.516283,-8.192188],[-4.470137,-0.625658,3.951883,-5.984283,-0.617135,-5.796966,6.695338],[-9.240134,3.034680,-6.904686,5.504538,-5.405172,-6.032704,2.347252],[1.177107,-0.585664,3.572200,9.432732,-4.270301,-6.652231,-7.962722],[-9.160107,6.494548,5.310558,-6.792708,-0.503636,-4.651363,-4.796367],[-7.084761,5.175545,8.685466,-2.716775,-8.557366,-7.123494,2.137895]],[[5.193618,8.303616,1.192825,-6.176874,8.280199,-6.763478,6.575349],[-2.648069,-2.405219,5.549390,7.040293,0.388135,-1.089855,0.391825],[-9.512420,0.057855,8.382553,1.840636,-9.519647,8.244652,-2.741704],[9.941084,7.022245,0.309422,1.713975,6.031427,-8.685096,-2.160115],[0.777688,4.395121,-8.093108,9.273028,2.062472,-6.072982,9.903972],[-0.753003,8.559410,1.575420,1.958668,-8.376504,5.024052,9.083640],[-0.623606,-4.728385,-7.959860,0.664373,7.738909,-8.198431,8.833340]]], dtype = "float64")#candidate|8287|(3, 7, 7)|const|float64
bop_8288 = relay.bitwise_xor(call_8276.astype('int8'), relay.reshape(const_8287.astype('int8'), relay.shape_of(call_8276))) # shape=(3, 7, 7)
bop_8291 = relay.bitwise_xor(call_8277.astype('int8'), relay.reshape(const_8287.astype('int8'), relay.shape_of(call_8277))) # shape=(3, 7, 7)
output = bop_8288
output2 = bop_8291
func_8296 = relay.Function([], output)
mod['func_8296'] = func_8296
mod = relay.transform.InferType()(mod)
mutated_mod['func_8296'] = func_8296
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8296_call = mutated_mod.get_global_var('func_8296')
call_8297 = func_8296_call()
output = call_8297
func_8298 = relay.Function([], output)
mutated_mod['func_8298'] = func_8298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8090_call = mod.get_global_var('func_8090')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_8339 = relay.TupleGetItem(func_8090_call(), 0)
call_8340 = relay.TupleGetItem(func_8091_call(), 0)
output = call_8339
output2 = call_8340
func_8349 = relay.Function([], output)
mod['func_8349'] = func_8349
mod = relay.transform.InferType()(mod)
output = func_8349()
func_8350 = relay.Function([], output)
mutated_mod['func_8350'] = func_8350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_8387 = relay.TupleGetItem(func_7653_call(), 0)
call_8388 = relay.TupleGetItem(func_7654_call(), 0)
func_4568_call = mod.get_global_var('func_4568')
func_4575_call = mutated_mod.get_global_var('func_4575')
const_8393 = relay.const(-10, dtype = "int32")#candidate|8393|()|const|int32
const_8394 = relay.const([[7],[-2],[-9],[5],[9],[-6],[-3],[-9],[6],[-10],[-4],[-9],[6],[-9],[-3],[-5],[-5],[3],[7],[5],[-7]], dtype = "int32")#candidate|8394|(21, 1)|const|int32
const_8395 = relay.const([1,6,3,-10,-5,-7,1,7,1,6,-8,-9,4,3,6,5,5,7,-9,7,5,7,2,-10,6,8,-5,-9,2,4,9,5,3,1,8,6,-2,1,-6,8,9,6,-4,4,-10,-5,-10,-2,-2,-4,1,-8,-2,-8,10,-2,3,-4,6,6], dtype = "uint64")#candidate|8395|(60,)|const|uint64
var_8396 = relay.var("var_8396", dtype = "int64", shape = (540,))#candidate|8396|(540,)|var|int64
var_8397 = relay.var("var_8397", dtype = "float64", shape = (1280,))#candidate|8397|(1280,)|var|float64
const_8398 = relay.const([-6.301985,9.205229,5.582293,-5.017897,-6.715287,5.889078,-3.139716,1.606925,-4.842565,-4.193463,-4.115415,3.046495,1.987471,3.017364,3.116682,-8.762824,-8.855453,7.675046,6.318697,5.714737,-6.231965,-2.047028,-2.083231,2.356353,5.580738,3.221858,-6.403870,-2.686180,-9.054306,0.081216,3.032601,8.938924,1.423114,0.448289,-6.754747,-9.625049,1.991538,-7.178196,-2.472564,-0.839083,0.550898,2.005913,-2.183814,2.485362,-9.610653,-1.838587,-0.434661,0.937213,-0.639410,-6.287092,-6.310356,4.398856,-8.906738,4.719071,2.283451,-4.282510,9.870243,-8.323746,3.910740,-9.925045,-7.016795,7.972427,0.275224,-1.136744,8.485956,-8.964068,7.110483,2.977420,8.884191,-6.387853,-8.527672,8.306054,3.950065,6.655592,5.545685,-0.482623,-1.529615,4.644473,-7.701452,4.793054,-2.989917,5.279502,2.757162,5.275086,8.193248,0.316082,-3.996544,-4.838118,4.089638,9.986749,2.022505,-8.252668,6.113789,8.639877,-9.790829,-1.716163,5.680469,-7.739371,-0.118170,9.903742,-1.813751,-2.589119,-2.013165,-1.590965,-6.089194,-7.287064,3.097224,-5.991430,-6.071421,-3.643747,-3.182696,-5.164768,7.297773,5.709224,-7.463429,0.479772,2.284104,-9.736788,-1.499684,8.644659,-5.790592,7.787042,7.685767,-5.398244,3.550208,-2.801250,8.163423,9.241200,5.133482,1.918337,-6.186107,-6.652783,-9.185038,2.293376,2.577970,0.425950,-8.019019,3.099451,-4.319297,-0.145928,6.876845,-7.129315,3.464960,0.392989,-5.955721,-7.238829,3.609456,-2.822419,4.462674,4.584492,4.134451,-0.307540,1.596607,8.018214,-5.675217,7.348827,-9.420080,-7.365067,-2.672226,-5.736237,-3.141270,7.918172,-5.244486,3.978167,8.151785,-5.290803,-8.021695,-3.271726,0.004722,4.467323,9.553891,0.231612,-6.815801,6.910514,6.301513,1.793823,0.927406,8.713244,1.996342,4.726020,5.154291,8.708167,4.623589,4.715618,9.152817,-0.650248,-5.925045,-3.543045,6.571489,6.490707,1.584880,5.677761], dtype = "float64")#candidate|8398|(192,)|const|float64
call_8392 = relay.TupleGetItem(func_4568_call(relay.reshape(const_8393.astype('int32'), []), relay.reshape(const_8394.astype('int32'), [7, 3, 1]), relay.reshape(const_8395.astype('uint64'), [60,]), relay.reshape(var_8396.astype('int64'), [540,]), relay.reshape(var_8397.astype('float64'), [1280,]), relay.reshape(const_8398.astype('float64'), [4, 48]), ), 1)
call_8399 = relay.TupleGetItem(func_4575_call(relay.reshape(const_8393.astype('int32'), []), relay.reshape(const_8394.astype('int32'), [7, 3, 1]), relay.reshape(const_8395.astype('uint64'), [60,]), relay.reshape(var_8396.astype('int64'), [540,]), relay.reshape(var_8397.astype('float64'), [1280,]), relay.reshape(const_8398.astype('float64'), [4, 48]), ), 1)
func_5673_call = mod.get_global_var('func_5673')
func_5678_call = mutated_mod.get_global_var('func_5678')
const_8404 = relay.const([-2.472478,3.111610,-2.244669,1.385239,0.429257,-1.565700,7.772904,9.117874,5.990203,-1.091814,-2.059816,3.056561,-8.016137,-0.697281,5.917744,-6.528644,-9.640303,-7.146740,-7.285868,6.645002,6.006642,-5.074825,-0.090737,8.177883,-1.440669,3.413477,3.584884,-4.973157,-2.816938,3.046896,7.365890,6.785605,1.808916,-7.146198,8.899348,8.799385,2.056813,-2.561231,2.327752,8.778643,9.431898,-7.258320,1.258632,4.825828,5.973359,-7.564500,-6.676398,-6.116843,2.932126,-8.813905,-4.806300,5.144719,7.272621,9.485751,-0.353210,-3.567237,6.880301,-0.695060,4.730732,-7.802120,-5.786122,4.201528,7.969256,-1.333275,-9.117704,0.850375,-7.976714,-9.861891,-1.701577,-9.777688,-9.825104,0.647415,1.895930,0.528900,3.446345,6.948878,-9.961049,-8.659330,3.564070,-0.631959,2.977782,-2.657665,-5.683155,4.127986,2.456668,4.727189,-2.101297,5.746977,-3.687719,8.403241,5.963070,8.159431,3.829376,1.976584,-6.420580,3.956404,2.212906,4.882334,-0.437325,8.807972,-4.661644,-3.195509,3.043768,-0.917970,-9.967076,1.504637,5.046088,7.765926,-4.100417,2.297523,-6.293979,1.634279,-2.872304,4.338901,7.669761,-9.308933,-5.540261,0.409044,1.381394,7.017470,9.390417,0.604917,-0.552702,7.596757,2.854466,7.857275,7.647587,5.285641,-6.979585,1.250599,1.702888,1.061230,-6.525301,3.757618,7.420193,2.557416,6.126458,5.895983,0.045083,7.165599,9.115865,-1.842888,1.062844,-9.064579,-6.657129,4.172716,-2.160521,5.457311,2.938759,-5.329440,-4.411583,5.109887,-8.800346,0.122380,-7.792013,-5.090881,1.480247,-2.997856,-1.365674,-9.758255], dtype = "float64")#candidate|8404|(160,)|const|float64
call_8403 = relay.TupleGetItem(func_5673_call(relay.reshape(const_8404.astype('float64'), [5, 2, 16]), relay.reshape(const_8393.astype('int64'), []), relay.reshape(var_8397.astype('float64'), [1280,]), relay.reshape(const_8395.astype('uint64'), [30, 2]), ), 6)
call_8405 = relay.TupleGetItem(func_5678_call(relay.reshape(const_8404.astype('float64'), [5, 2, 16]), relay.reshape(const_8393.astype('int64'), []), relay.reshape(var_8397.astype('float64'), [1280,]), relay.reshape(const_8395.astype('uint64'), [30, 2]), ), 6)
output = relay.Tuple([call_8387,call_8392,const_8393,const_8394,const_8395,var_8396,var_8397,const_8398,call_8403,const_8404,])
output2 = relay.Tuple([call_8388,call_8399,const_8393,const_8394,const_8395,var_8396,var_8397,const_8398,call_8405,const_8404,])
func_8419 = relay.Function([var_8396,var_8397,], output)
mod['func_8419'] = func_8419
mod = relay.transform.InferType()(mod)
var_8420 = relay.var("var_8420", dtype = "int64", shape = (540,))#candidate|8420|(540,)|var|int64
var_8421 = relay.var("var_8421", dtype = "float64", shape = (1280,))#candidate|8421|(1280,)|var|float64
output = func_8419(var_8420,var_8421,)
func_8422 = relay.Function([var_8420,var_8421,], output)
mutated_mod['func_8422'] = func_8422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_8426 = relay.TupleGetItem(func_8021_call(), 0)
call_8427 = relay.TupleGetItem(func_8022_call(), 0)
func_7517_call = mod.get_global_var('func_7517')
func_7518_call = mutated_mod.get_global_var('func_7518')
call_8438 = relay.TupleGetItem(func_7517_call(), 1)
call_8439 = relay.TupleGetItem(func_7518_call(), 1)
func_1145_call = mod.get_global_var('func_1145')
func_1149_call = mutated_mod.get_global_var('func_1149')
const_8446 = relay.const([1.239812,-9.738115,-2.461201,-5.729837,1.026055,-3.246973,-1.193731,6.306210,4.040222,-4.396931,5.531474,6.614665,8.358064,5.903071,-2.329859,-8.736471,-8.317394,-7.757637,3.278217,6.099520,-1.219403,7.811987,4.705662,9.234127,6.649179,-7.410042,-7.284642,5.174862,-2.307250,-9.314987,6.377233,-2.847630,-2.842038,-4.138695,-0.344894,-2.199146,-8.869801,4.004834,-6.894334,-9.638326,-5.984970,-3.354669,-3.290668,-5.269517,-2.870166,-9.374948,-6.376447,-7.868533,0.645070,-1.546307,-5.791037,5.118577,-3.798315,-6.082727,1.220792,-0.788571,-8.022000,-5.436615,-3.510541,0.757242,8.508239,-6.940296,8.695665,-6.277835,-7.367806,-9.222106,9.570179,6.077540,-5.254748,-7.439045,-4.347500,-2.243323,8.718491,-5.126571,3.122764,2.014167,1.294789,-9.220694,-0.537326,9.816219,5.884706,5.936363,1.312797,-6.972321,-9.752287,4.370098,-4.255653,0.278930,-6.813003,9.284526,-0.879549,9.983713,1.990639,-3.976013,-0.743241,-7.760106,3.123988,0.673968,-4.285780,-2.387333,-2.805193,4.871900,0.372280,6.524672,-7.311296,-9.575747,8.744699,-9.262972,2.218393,-9.242033,5.231479,-1.948754,-7.307539,4.641727,1.768569,4.057511,-8.246069,-7.293279,-6.563285,2.031332,1.676989,6.350012,5.755316,8.810301,-2.710206,4.466601,-3.007094,-3.052592,2.835075,1.625222,7.026835,-1.971296,1.188492,-6.670202,-2.548977,0.355631,9.425614,-5.329119,-0.321278,2.927539,0.270947,-1.964616,-3.255029,-3.143880,3.383399,3.501824,5.576337,-4.987079,-9.634683,-9.593530,-3.446949,-0.337386,-0.886965,4.028968,-6.375457,6.817205,1.575656,8.799003,-6.337572,9.878566,8.799071,-6.283518,-0.659157,-3.333415,8.789792,-4.041476,-8.665540,4.619293,2.441174,5.726900,-2.255901,-0.620595,6.575480,3.940524,4.666335,6.890102,0.760106,3.059056,-5.837177,4.385508,-2.843171,9.300286,-1.160040,3.381595,4.285120,-1.667253,9.553511,5.904813,-6.103096,-0.293719,0.140860,3.275636,-0.995756,7.160781,-1.641830,-1.378306,-5.363719,0.386884,9.468643,-1.682174,8.232599,-3.324915,4.786964,6.820085,-8.992332,-9.183579,1.312019,3.514601,-1.335571,-0.909505,7.997313,-2.514289,3.759099,-3.627397,-1.668982,4.104271,9.230454,6.524407,-1.152959,2.099211,-0.147669,-4.045011,0.852455,0.949569,-5.697789,-5.970695,2.681810,5.986157,-9.441710,8.486190,5.732590,-5.710382,-4.406456,7.841552,7.006631,7.257311,-4.869260,2.031224,6.965023,-9.791166,1.810968,9.143999,5.948239,3.679973,6.416446,-5.877343,6.061592,2.133687,-4.260156,-3.926315,0.182762,-0.059567,-3.725113,7.052439,-1.912721,6.762071,-6.051293,-9.407017,-4.209512,5.420120,-5.466533,-5.129060,0.437267,0.531649,-5.248712,2.593413,-8.840617,-7.879177,2.974555,-9.670029,9.511507,3.069970,1.166897,2.912472,9.736101,6.857131,-3.312558,-2.308799,5.048949,-2.963194,3.049904,-5.630108,3.291542,-7.380758,-1.485548,-8.010259,9.352079,-2.124382,-6.993340,-6.356714,-5.460246,5.368499,1.250686,-2.618196,-2.964878,-7.470794,-0.060183,8.354520,2.692228,0.392485,-0.218736,6.620659,1.702426,-0.388671,1.958900,-9.152221,-3.136071,6.609036,8.055147,2.063635,-7.019018,5.113053,-5.849433,-6.372456,3.655370,7.970794,7.578915,4.109079,-0.214535,-0.076881,-5.142978,-1.476937,3.702797,-0.088374,1.371819,-4.583647,0.243052,3.074323,-5.956840,-5.963037,7.213725,0.364994,-5.540723,7.270253,6.594858,4.249458,-3.762439,-0.756163,4.874257,-0.533639,-2.854350,-0.535965,0.463003,1.371367,5.164679,6.263438,-1.807225,4.747246,1.990570,0.389121,2.021226,-1.126959,-1.841410,3.710099,7.458860,4.116379,-1.425503,2.854104,2.520606,6.186573,-5.656871,5.450223,9.268307,-5.992738,9.518707,2.784057,-4.393841,2.533404,4.143033,-9.804774,-4.676872,-9.594848,1.175274,-4.449462,1.251160,6.597480,-2.300012,-4.141425,1.500678,-5.437809,-9.663626,2.565137,8.469298,-5.141958,8.525322,4.543635,-2.095080,-5.875571,-5.507023,-7.321485,-1.853042,0.379155,-5.266199,3.545584,-9.009815,-1.028576,2.275938,8.153456,-7.626596,0.937300,-5.475248,-4.862753,8.852787,-9.015360,2.008098,1.951143,-1.026165,0.189892,-6.543062,3.429411,-7.458676,2.732506,9.113315,0.178986,-3.991867,-4.471418,4.269885,4.262625,1.446135,-0.297279,-8.246590,9.039242,1.198269,3.157047,3.080821,-0.229143,7.843373,4.186751,6.326157,-3.597532,-6.913535,-0.835324,4.101200,-2.014608,-0.459339,-7.392567,-2.964882,8.946193,-3.085858,7.258696,5.395110,6.848266,4.539588,-7.658604,4.795238,9.841097,0.012990,-7.052000,2.916762,1.441460,8.597364,1.759719,2.358297,9.436038,1.915402,6.180722,5.538708,7.966242,-0.371364,7.040393,7.645307,4.967858,-6.657496,4.735338,-5.725023,5.988817,-5.744584,9.837126,-5.526199,7.467189,6.535141,-9.705963,-3.747515,2.430026,8.522756,-4.766444,2.926730,4.610299,5.183665,-2.628017,-9.953579,-5.578625,-8.022611,-0.649584,-6.932337,-2.098829,8.078831,-6.554885,0.947200,-4.601520,-2.941852,3.120287,-3.840944,-1.041188,1.522934,1.270542,-2.626224,9.773738,5.294730,8.397511,1.728502,9.192403,1.694517,-5.141261,6.953117,1.768211,-1.681346,-8.763832,-7.643133,-2.785508,9.534532,8.472008,9.470293,-9.530921,-3.442025,1.515145,8.155012,-5.861138,-3.100960,4.114357,4.775074,-1.194066,8.848086,-5.814153,8.609565,-2.581147,-6.364905,-0.999779,-7.863602,-9.845003,5.554854,-8.658736,-6.400623,9.834357,-7.853479,9.898612,8.436778,8.973167,-3.428765,-9.360263,-8.359329,-2.944720,-5.598519,0.676652,2.233567,-5.061518,3.557335,5.061550,0.667835,-9.828270,-9.387441,-5.014216,8.769289,-0.831659,8.430997,4.491251,6.299124,9.938968,8.777669,-1.339119,-6.619964,1.131440,-5.120398,-7.547392,1.735619,6.572956,-3.892178,9.505975,1.971406,1.095126,1.071121,-9.021682,-3.111514,-3.095192,-7.503173,-8.690964,9.439892,-9.379363,-6.729317,-9.566470,-0.817036,8.509449,5.197412,-7.369833,5.686993,8.043118,4.379605,7.095681,9.165128,7.793516,4.048009,2.261249,5.487486,-8.367294,-7.386023,2.115796,-4.676491,4.527811,5.316438,-9.210239,6.210314,7.459843,3.059382,-6.627614,0.896017,1.023284,4.129052,8.535742,-6.379347,-5.787667,-6.613651,5.498045,8.298489,-7.105735,2.563983,6.293675,3.068447,4.472922,8.695254,6.320245,3.061177,2.880349,0.309139,2.541480,-6.300284,-8.918678,0.175314,2.994101,-7.933351,6.370877,-8.434612,-5.892935,-5.631414,7.393629,1.019188,-5.423094,9.961839,0.316800,-7.859458,-1.607129,6.656875,-1.430349,6.959530,5.262159,0.705991,2.359919,6.033609,5.296351,6.511920,3.050460,-8.722223,2.174800,-2.114664,-3.746652,1.268947,0.070867,-4.148028,2.299308,-6.269131,4.744350,3.866786,4.581515,3.377533,-5.815866,0.551775,2.650997,5.046101,0.578201,-3.382830,9.535841,5.776760,-3.074252,-6.214690,3.051890,-5.371832,-3.012073,8.496587,-7.670398,3.573162,4.079070,-2.197678,-3.710742,1.542973,8.557879,7.340602,7.891945,-2.130749,-6.831581,0.825713,3.034555,1.509123,6.727833,4.852895,0.609331,0.915019,-7.271068,4.255410,4.009367,-1.415107,-4.553542,6.441595,-7.660023,4.049827,-2.376603,-0.657525,-7.078118,-1.334280,-1.966740,4.654107,-7.500434,-2.931060,2.735468,7.630964,-9.166017,2.540176,7.911115,-9.541883,-2.576551,8.855918,-9.681740,-9.432148,0.345207,1.651027,0.784679,9.594677,8.716203,-6.478988,5.462058,0.443558,1.569547,7.768416,-2.349907,2.011440,0.933141,9.891176,-7.285920,9.635564,-9.729241,-4.051853,4.168745,7.471210,0.003093,4.019369,0.117350,5.985381,-3.665737,-0.024351,-3.474225,4.454174,-6.382697,-1.089205,6.125252,-5.740972,-4.193582,9.868704,-5.661507,-9.530621,-9.161633,-7.658886,-9.739103,-2.505188,-3.561444,9.775727,-2.686591,8.992057,-8.851003,-0.246299,2.153730,9.368291,4.916797,7.855402,-0.675168,1.285135,-1.288481,-2.046629,0.314468,8.297386,4.584759,8.850510,5.988843,-3.589860,-0.778763,6.541060,7.456926,9.619963,9.501735,-5.362168,-2.052878,-5.567672,-2.140693,0.076740,-6.373050,6.169050,-1.457100,1.244120,2.153922,5.673217,-1.151008,2.275988,9.818955,-7.366678,-8.897753,-8.905863,6.309344,2.309045,-4.882260,4.894336,3.738285,-6.380542,2.971061,8.207761,-5.724821,-8.382144,-0.097091,-5.338507,-2.052720,-6.023617,-1.977116,2.118347,-0.676143,8.161385,-6.841140,6.449379,2.795746,2.371187,4.905420,-8.154207,0.912707,6.879668,-4.373741,5.399637,-4.881961,9.653390,1.111445,-9.845178,8.038932,-3.066553,3.072473,3.823047,9.914046,4.625099,-6.543897,-5.666836,4.916666,7.090674,-1.971344,-3.392122,-1.993838,0.367568,0.415471,1.715749,6.175341,-3.855815,1.468826,3.331621,-7.417954,-0.470727,-6.885701,-5.114632,-6.810938,-4.341971,-6.418806,9.830097,-8.803697,-4.024214,7.298358,6.383539,6.806300,9.037979,3.515142,-8.550515,7.906219,-9.700427,8.871306,0.165586,-4.718610,-6.276457,1.584080,-4.058718,-1.929348,8.948738,-8.194096,-3.795764,-2.574905,7.340849,4.770258,8.364414,-6.903577,-4.548780,-7.770784,3.780159,5.357975,3.579031,3.848830,6.836310,3.616081,2.305995,4.094411,1.180830,2.202726,4.341850,-1.934256,-4.538021,0.694321,4.928763,-9.341288,-2.605119,-1.100721,-5.828086,9.383287,-5.475728,-3.625856,3.662983,1.208341,4.942366,7.405104,6.158648,7.290934,-8.919869,8.981318,-8.640328,-8.207726,9.993441,2.305451,-8.482829,2.015230,3.207173,2.287427,1.887348,0.344929,4.479817,-5.597846,4.620463,-9.470875,-9.691382,4.558232,-4.159980,7.867389,-7.262421,1.607899,-3.174303,1.141632,3.276890,-6.788846,-2.034144,5.680078,-4.384997,-5.644133,-8.563365,9.441329,-4.695928,9.880829,-3.800456,7.805730,1.448166,0.360905,3.836207,8.587384,4.424038,-5.288250,-6.554854,-3.549125,3.150073,-7.981777,5.383376,-3.999362,-4.016866,-0.550897,-1.067731,2.281768,4.435307,9.150093,-1.401965,0.675162,-3.654033,0.529558,4.247430,3.804265,-7.768049,-9.827538,4.083973,-9.689962,8.560603,-4.790990,-4.606068,3.953999,4.143301,-9.198565,-1.521904,0.570042,1.013360,3.519677,-2.022971,2.800795,-2.541860,8.805386,-8.288520,9.491347,-4.919218,-1.903789,6.224946,-2.929819,-5.516062,-7.270430,-6.918152,-0.448002,-4.155716,1.515362,-9.513140,-4.537257,-1.605913,5.198497,1.669799,-4.307047,-7.057408,-3.735546,0.631821,-7.389620,5.084149,-2.053375,3.496421,-9.152656,-6.239292,-0.659732,-5.625345,8.982464,-6.886062,-5.396028,2.104592,-9.027522,9.209651,5.989312,2.873412,-9.717276,3.967434,2.011796,4.366495,-8.818999,0.287175,7.447011,2.093830,-5.270926,5.863941,1.318793,-4.724838,-2.622148,-5.204229,-2.033658,-1.462111,0.132420,1.394490,-1.041101,-8.940592,-3.182315,0.383367,1.869334,-7.955425,3.558684,-5.653579,-7.568955,-9.597334,-4.240864,-4.040433,-7.384592,-1.046268,-0.444007,-6.825774,-7.536686,-3.962267,-1.851654,-7.778599,-2.012908,-4.074131,-1.535543,7.494841,1.262004,-2.083203,-0.495801,-4.909023,4.525725,-0.581192,-8.778852,-5.308426,2.316280,2.102349,-7.582059,-5.610984,-1.165667,-0.490647,3.563948,6.183529,9.879833,8.913636,-4.392197,6.193294,-2.066236,-1.479616,-0.207212,9.140182,8.436577,-3.046023,3.262308,-5.663742,7.692648,-8.814517,-2.422410,9.870353,3.627739,-2.371391,-3.666065,1.677553,9.310562,6.281105,-8.249176,-8.340370,1.308848,-7.909273,2.370960,-7.217521,6.803557,8.640279,-0.688606,-8.233715,3.272595,3.614181,-9.312151,-0.206165,-3.656903,5.323203,5.944889,-9.579184,-9.261898,5.493072,-1.715691,-3.127873,-3.364968,2.870360,-8.473654,4.915244,-8.492357,9.482312,6.487811,4.333772,1.322652,0.621872,-0.143138,6.506310,-8.846257,-9.985202,-8.642704,-2.429165,-8.477534,5.650887,8.149779,2.137097,-1.755638,-6.399316,-3.305402,5.880295,2.176129,-1.792682,8.922296,-2.105233,-7.485888,-4.728386,-1.110343,-1.633292,-0.029434,9.085994,-8.062523,-5.366864,-0.370263,-1.416364,-0.794449,-3.813767,-9.437080,8.840883,6.579938,5.233372,-2.593151,-9.493439,8.138913,2.228403,8.323347,5.736594,0.542405,-5.053281,2.688705,1.024727,-9.553897,5.031974,-5.624042,-6.582083,-0.370873,-5.934123,2.192741,0.800268,7.956381,7.268569,-2.958432,-6.506984,-5.458468,2.885876,4.256877,1.000218,-6.603381,5.899353,9.162021,-0.221573,4.076006,-3.604970,-6.492819,5.407638,-8.344196,-1.943697,-7.733178,3.381178,2.896581,-2.321021,9.412454,-3.747911,-6.638906,-0.320884,-1.412786,7.321896,0.212401,-7.229586,-9.932962,9.855457,-9.556134,0.932319,-1.728040,8.045777,0.468663,1.752697,3.332735,-4.999486,8.736321,0.494213,-3.009956,9.941063,-3.832746,0.569836,-5.971516,-9.869800,-9.447072,6.780454,-2.712740,-8.118153,-9.129880,-1.696783,3.419930,0.564847,9.146968,-9.494702,6.379847,-6.574403,-7.506917,-4.404133,-7.768210,5.593189,-0.759238,-4.745393,-1.188068,-4.639497,-3.377412,-6.840693,-5.693557,-9.121057,4.249811,4.299706,-6.941403,-2.119529,3.302069,7.196954,7.860944,-5.751841,1.662456,-6.986556,1.521312], dtype = "float64")#candidate|8446|(1280,)|const|float64
var_8447 = relay.var("var_8447", dtype = "uint64", shape = (60,))#candidate|8447|(60,)|var|uint64
call_8445 = relay.TupleGetItem(func_1145_call(relay.reshape(const_8446.astype('float64'), [16, 16, 5]), relay.reshape(var_8447.astype('uint64'), [60,]), ), 0)
call_8448 = relay.TupleGetItem(func_1149_call(relay.reshape(const_8446.astype('float64'), [16, 16, 5]), relay.reshape(var_8447.astype('uint64'), [60,]), ), 0)
func_6804_call = mod.get_global_var('func_6804')
func_6806_call = mutated_mod.get_global_var('func_6806')
var_8462 = relay.var("var_8462", dtype = "int64", shape = ())#candidate|8462|()|var|int64
call_8461 = relay.TupleGetItem(func_6804_call(relay.reshape(var_8462.astype('int64'), [])), 2)
call_8463 = relay.TupleGetItem(func_6806_call(relay.reshape(var_8462.astype('int64'), [])), 2)
func_1505_call = mod.get_global_var('func_1505')
func_1507_call = mutated_mod.get_global_var('func_1507')
var_8467 = relay.var("var_8467", dtype = "float32", shape = (140, 2))#candidate|8467|(140, 2)|var|float32
call_8466 = relay.TupleGetItem(func_1505_call(relay.reshape(var_8467.astype('float32'), [2, 14, 10])), 0)
call_8468 = relay.TupleGetItem(func_1507_call(relay.reshape(var_8467.astype('float32'), [2, 14, 10])), 0)
func_7405_call = mod.get_global_var('func_7405')
func_7408_call = mutated_mod.get_global_var('func_7408')
const_8470 = relay.const([-1.484486,-7.672077,-0.875128,4.101745,9.698963,8.050415,6.068807,4.422449,-3.191780,5.872143,2.543356,0.074940,-5.527585,3.250217,-4.815410,-8.187587,3.185064,1.260550,2.006632,3.358330,6.821335,7.406769,-3.851111,0.816650,-5.334681,-1.314762,-4.291043,-9.550186,6.374229,-4.396669,-2.928022,-7.688727,-9.846895,1.983842,-1.941178,-4.855735,4.129061,2.236983,-9.909115,-5.211834,7.752814,1.499351,6.024808,-5.261641,4.992088,-9.882956,7.702918,2.346164,-5.505820,8.449885,-4.524890,-5.350454,-6.197296,4.290017,-1.190715,2.693220,-1.673816,-5.333894,4.442766,7.747895,6.769138,-7.204989,-4.519827,-4.320928,-2.835160,-4.259718,-8.666422,-8.437290,-4.257644,7.477108,7.016922,-0.051995,3.444912,1.084662,6.226616,1.535859,-9.532043,1.123138,-8.964732,5.644537,9.792839,8.209519,8.067670,-3.770819,9.567550,-5.288132,1.356899,-8.710106,3.094530,6.750562,-7.688224,-9.513065,-4.119137,-4.530091,4.070484,4.501204,1.212088,-4.163827,-8.757842,-5.455799,1.135511,-0.650978,5.086447,1.124688,7.504242,3.815544,-0.145089,-8.439359,8.708641,9.649484,0.527805,9.549554,7.080325,2.999127,4.736245,1.116558,-6.560512,0.373158,-4.850630,6.947207,6.345028,-8.125215,-4.674263,-5.712540,0.565413,-8.714444,-9.093295,4.538258,-8.405427,0.258001,-0.812914,-6.386921,-9.936405,-1.884453,-1.956073,-0.860843,-6.105169,5.469943,-8.621416,-5.089428,6.244159,-2.772772,-5.390613,8.845709,-9.921926,-7.951700,7.484195,0.046316,-4.873738,1.244628,7.327094,-5.043611,-8.998636,-8.225777,1.105047,-9.838331,-2.276958,-3.468873,-6.271821,9.210408,-8.742242,4.608642,-2.159991,-5.965883,-0.898961,7.002378,6.977903,2.706753,-3.002659,-9.236286,-6.292172,-6.643886,0.132603,1.243447,2.630541,-5.766745,1.665002,8.635290,5.811824,-2.555029,0.058279,7.318385,-1.916395,-4.583003,3.237954,-4.101118,7.605787,-7.404423,-5.208136,-5.803793,-6.498158,4.786110,-4.556700,6.262149,-9.571199,5.971207,5.544305,5.639569,9.203072,-2.183889,-1.770979,-0.940157,-5.819860,5.182583,4.730688,-3.393582,-6.979019,1.769969,-2.261512,-7.909596,-8.932570,9.530555,4.339248,2.430773,-9.130865,5.470639,9.263698,4.392981,-8.838763,-9.012723,-9.083452,6.157114,-0.406349,-1.767121,8.075800,-8.117482,-2.781967,1.048266,-5.643306,7.928463,3.079225,2.600890,-2.997322,-7.305275,8.806175,-2.294520,6.027624,7.194418,-4.435882,-3.879418,-5.142182,-4.124340,-6.379403,-0.822601,-4.242595,-1.399608,-5.068127,-8.339647,-9.082526,0.239811,8.044161,3.323801,9.931908,9.858682,-5.542518,6.982385,-1.813681,-8.781259,-3.843885,3.561975,-6.534085,-2.980610,9.486229,7.277628,4.030905,-5.657189,8.080000,9.552249,-3.725239,-9.924328,-6.934155,8.550538,3.656811,-7.435339,9.069184,4.330839,0.614989,-5.975685,-9.318343,-2.989808,3.388146,3.466612,-5.668380,3.421655,4.893349,-5.643572,-9.164312,-7.257907,7.767734,9.784070,-9.520759,-3.982593,-0.898727,-7.910058,-2.649834,-3.228789,1.515884,-6.654312,-9.881359,-0.294907,-1.410750,2.132186,6.876950,-2.360048,-3.440053,1.055065,-6.276990,-9.998721,-3.597554,-5.412110,7.546157,-8.171799,-7.927512,7.143399,1.007598,-9.478171,-6.354276,-4.823229,5.788968,-4.374082,-9.804249,-9.479512,3.442178,8.028682,9.871696,-1.264609,-4.087869,-1.182727,-7.932687,8.959489,5.620981,4.452512,1.148394,1.324470,-3.300374,1.409056,1.666025,-0.295893,-4.308266,8.701030,1.102858,8.372726,-2.109435,-1.983062,9.369872,-2.865049,8.496243,-7.951333,7.889803,5.663005,2.305941,-6.875199,-3.700292,1.365113,-1.902417,-4.597604,-7.064883,3.993820,6.524069,1.272552,4.096467,-9.496847,2.469915,-7.392930,-0.614332,4.996305,-1.684653,4.054562,-5.943027,3.329703,0.808879,-1.912450,0.903857,-3.417543,9.645453,3.476221,-5.013317,3.818148,-2.257348,-7.538990,2.282446,-6.589984,-7.257412,-6.747976,-7.086277,2.210953,2.552301,-2.497479,-1.886252,-0.363740,-8.991586,-9.024942,0.959469,3.269363,9.318889,-0.904860,2.139466,-8.942933,-1.686308,-4.846400,5.927754,-6.129938,3.171833,9.342771,-6.520171,3.862070,-0.623929,7.522924,8.113253,3.217632,-2.319059,1.416800,2.330913,5.722595,-9.313160,-4.089508,-4.921461,-7.278014,8.029289,1.492989,4.440872,9.965016,-5.150082,3.223652,6.509222,6.845972,4.150530,1.479026,-1.979366,-9.248599,-0.327391,-6.637051,-0.661192,-9.606978,7.015117,0.343133,-2.185428,-7.753884,3.147531,-1.238694,-3.068869,-6.627828,-9.823865,-1.983212,1.933323,5.879916,-3.207186,-8.354162,-5.536101,-5.395395,-2.858304,6.094709,-9.637625,7.537440,4.598798,-6.146694,1.551005,9.202837,-7.532994,7.242453,2.087283,8.543238,-3.896516,-5.175734,-0.857878,-1.707745,-1.179510,4.509548,6.465860,-1.107696,-3.449368,9.784479,6.663593,6.612861,-8.017323,9.250688,9.262648,4.319028,-4.155124,0.343613,5.387192,4.907010,9.364517,-8.491071,-9.721228,6.213331,-8.716499,-7.169714,-7.847411,3.538349,-7.868139,-8.266065,-9.959801,-9.853206,7.701945,6.156177,7.033262,-7.710835,-0.868301,-0.026290,5.895932,3.331227,-0.617949,3.939197,-2.145445,5.277110,-7.362576,-2.806774,-5.891868,2.133060,-3.343766,-9.880888,-7.706538,-7.107192,5.125645,0.640023,9.130141,-1.445760,-7.855186,-6.827931,1.513692,-4.418826,3.766711,-7.845790,6.476650,0.695542,-6.648389,2.015039,-4.410857,5.452441,-5.877737,-9.163753,-4.479956,4.174978,-9.783656,0.965324,-1.375582,5.540933,-7.754528,8.877555,-4.740844,-2.916618,-8.219020,6.900127,7.177271,-4.605744,2.897707,8.806353,-6.068009,-7.596709], dtype = "float32")#candidate|8470|(550,)|const|float32
call_8469 = relay.TupleGetItem(func_7405_call(relay.reshape(const_8470.astype('float32'), [550,])), 1)
call_8471 = relay.TupleGetItem(func_7408_call(relay.reshape(const_8470.astype('float32'), [550,])), 1)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_8491 = relay.TupleGetItem(func_7653_call(), 0)
call_8492 = relay.TupleGetItem(func_7654_call(), 0)
output = relay.Tuple([call_8426,call_8438,call_8445,const_8446,var_8447,call_8461,var_8462,call_8466,var_8467,call_8469,const_8470,call_8491,])
output2 = relay.Tuple([call_8427,call_8439,call_8448,const_8446,var_8447,call_8463,var_8462,call_8468,var_8467,call_8471,const_8470,call_8492,])
func_8502 = relay.Function([var_8447,var_8462,var_8467,], output)
mod['func_8502'] = func_8502
mod = relay.transform.InferType()(mod)
var_8503 = relay.var("var_8503", dtype = "uint64", shape = (60,))#candidate|8503|(60,)|var|uint64
var_8504 = relay.var("var_8504", dtype = "int64", shape = ())#candidate|8504|()|var|int64
var_8505 = relay.var("var_8505", dtype = "float32", shape = (140, 2))#candidate|8505|(140, 2)|var|float32
output = func_8502(var_8503,var_8504,var_8505,)
func_8506 = relay.Function([var_8503,var_8504,var_8505,], output)
mutated_mod['func_8506'] = func_8506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_8535 = func_7205_call()
call_8536 = func_7205_call()
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_8543 = relay.TupleGetItem(func_7952_call(), 0)
call_8544 = relay.TupleGetItem(func_7954_call(), 0)
func_7405_call = mod.get_global_var('func_7405')
func_7408_call = mutated_mod.get_global_var('func_7408')
const_8548 = relay.const([-7.153186,-1.198340,1.908900,8.018522,-1.708806,6.098408,-8.985625,-2.370730,-0.917643,2.030677,2.666816,6.153899,3.119885,-2.363157,4.347866,2.735180,-7.691308,1.163514,-9.820794,9.737388,-6.259071,-0.879314,-0.353666,5.973674,-9.991620,4.906388,-8.179437,-2.676228,-1.347810,-2.894283,3.344351,-0.015751,7.158887,3.508976,-5.768632,-6.377388,-1.593382,6.552806,8.467864,5.393599,8.420351,6.496309,6.589523,-7.717302,8.837886,-9.730137,-2.462523,-8.909685,-9.175045,1.940495,-6.987380,-6.386773,-9.308668,1.661013,-9.084106,-9.243465,6.705786,-6.038797,9.397885,0.196051,9.995010,8.154651,-6.753794,-7.629288,-9.670481,2.358170,1.083990,0.893085,-8.944031,-3.204742,3.178077,-0.602462,-6.891396,5.689191,5.482723,-7.215447,-3.701808,-6.736785,9.898726,-1.871621,9.180883,-8.576120,4.619163,-9.755228,-4.990886,-6.145316,9.684179,3.306845,9.627481,7.579495,4.739535,-1.691735,-0.290590,-0.534622,8.244719,5.625418,-7.508494,7.937869,6.743340,0.338895,-8.563977,6.694575,9.353327,-9.329855,4.841012,9.381822,3.280260,7.748151,0.079943,-1.878209,-5.414719,7.157897,3.282753,-4.780511,-9.272059,2.719744,5.728238,9.466183,2.955195,-1.839462,7.524590,5.015047,6.936654,-0.744929,-8.608868,7.304414,-0.023865,6.605582,6.299703,-3.511380,-1.544435,0.073686,-2.496641,-7.729947,-4.718531,1.314104,-3.607100,-6.490455,8.139669,-3.768930,1.592471,-2.439267,-2.066708,-8.858844,7.969021,-5.312098,-2.536585,5.662763,-5.013839,-2.538028,-3.450108,-6.253286,-0.609802,-0.852569,-3.225621,0.250165,-6.953313,0.375487,2.527031,1.653696,2.469725,-7.790017,5.677993,-3.715884,6.776261,-5.495201,-3.795356,4.024742,0.152008,-2.890109,-7.403909,-0.115838,8.035563,-4.667857,0.490554,2.408385,1.558845,-0.802678,-1.060378,-7.739025,2.707858,2.449994,5.962614,-5.344657,8.374717,-7.204887,-2.751553,-3.153350,7.309552,-9.199188,-5.343607,4.255353,-3.622744,-8.272551,-9.719202,-6.779488,9.333972,-4.362306,-7.431274,-6.540257,8.944322,-0.138853,6.251303,-9.061192,7.951189,5.868796,-9.607665,6.027735,-3.763951,0.762069,-2.205357,-1.392149,-7.669288,-0.576067,9.090226,-6.611762,-0.577054,-8.559237,6.765334,-6.187627,5.721494,7.505609,-6.957004,-9.966168,-9.328952,0.908379,-1.107260,6.832101,-2.328974,9.317808,-9.867412,1.106210,-9.104581,-3.832646,-2.863904,-7.346675,-7.893644,8.103697,-7.549461,6.175984,-8.797714,7.948908,-4.915916,5.704578,2.503623,-1.903024,-5.635685,-4.872292,6.962336,-5.398223,7.555309,4.777551,-4.629457,-2.790633,8.196809,-5.119750,-8.116028,-8.982804,-9.491116,-1.224515,-5.388242,9.639637,-3.592676,-2.787220,-6.839483,7.013980,6.202595,8.206743,5.199130,4.728621,5.721121,-4.791046,4.010201,-3.536456,-3.347749,7.561387,0.777785,2.936447,-4.941383,8.344042,6.774054,-2.006516,4.331073,-8.399359,2.789679,0.068406,1.028738,4.135619,-6.745722,-0.806459,-5.661715,-2.142116,-4.527435,0.336461,7.170888,5.777895,3.550376,4.141983,9.447898,8.665430,9.459890,6.577856,8.945788,-6.460035,-2.072276,-0.325498,-3.113122,-8.164565,8.459174,-9.742769,-6.592667,3.080535,5.987258,4.859502,-3.042455,-0.853511,5.402238,5.711905,-8.888427,3.354587,-7.280566,3.165973,-9.901815,-4.055495,1.805275,-9.679062,-6.453390,5.821916,-1.041227,6.201943,2.247066,4.957764,2.100412,1.168806,-4.686228,7.124526,7.293045,0.784613,-7.546863,4.222537,-0.298882,-3.316590,3.697588,3.127098,-9.510088,-2.257844,-2.948467,-1.662567,-8.608359,2.928204,-2.072257,-2.757738,8.775881,0.835317,1.732647,9.314022,-4.437035,-4.663349,7.722762,-8.898950,-0.534423,9.745402,-0.769882,7.056304,-1.697286,4.791623,6.288823,-4.032044,1.127686,-4.336875,-0.183474,3.366476,6.394324,-5.835501,4.938869,-8.959538,3.314465,-8.055342,-8.708168,6.590827,-1.781201,3.252014,-1.321123,-4.619289,-8.657793,-1.438637,-7.104547,5.204464,5.508215,-6.238084,-9.791938,4.548419,-9.596203,1.911836,6.993159,0.111820,5.122778,3.156314,-6.964931,-0.108750,-3.436074,3.198755,-1.057838,8.149057,-9.758793,-5.614614,-5.770367,0.496608,3.778565,4.980411,1.961883,-5.427914,-2.601321,-0.870204,7.980209,1.580317,7.912391,-3.541657,6.014465,1.197801,7.129363,1.016590,0.910728,-5.234359,7.546646,1.870739,9.532313,-3.942435,9.033181,-0.852170,4.916479,4.955210,2.729223,-9.676755,4.318893,-6.852498,4.737076,-5.239857,-7.873202,6.618233,2.731941,-0.860454,-8.103214,-9.429747,7.498493,-3.211054,-4.839290,8.656848,0.301825,-0.228675,-9.436029,7.570803,-5.899370,-8.756077,-9.863863,3.046071,3.936787,-5.761819,-2.893071,7.805177,-0.611733,-2.145954,7.149692,-6.200466,4.591954,4.700485,1.773112,4.334878,8.331132,8.529013,2.569412,4.099583,-7.791516,-3.983133,-5.709156,9.704117,3.465490,9.768676,1.837133,4.287260,-3.526542,-9.810691,0.862349,-1.300257,-1.903014,-4.145189,-0.268940,-8.183154,-3.482559,5.895091,-3.406346,4.326761,-5.740882,9.159615,-3.382874,-7.419316,6.546885,-1.651401,-8.575698,3.465963,-4.943022,-8.426874,9.366465,-1.493062,5.140743,-8.877071,-8.067217,6.572553,-1.163501,-6.126577,3.554414,-5.939296,-4.465048,6.732440,8.074916,6.525851,-0.279217,-7.648970,-2.843012,4.253096,-9.083345,5.085698,0.333117,0.614025,6.671294,-3.860581,-6.191240,-6.589845,-7.369455,4.704227,-1.142191,2.002784,-7.511711,2.048618,-7.254837,-0.635819,-5.482983,4.406831,-1.776215,-0.977315,3.879134,-7.318777,7.664280,-1.320585,-5.444817,5.764142,-8.323741,4.117824,-2.692075,6.601164], dtype = "float32")#candidate|8548|(550,)|const|float32
call_8547 = relay.TupleGetItem(func_7405_call(relay.reshape(const_8548.astype('float32'), [550,])), 4)
call_8549 = relay.TupleGetItem(func_7408_call(relay.reshape(const_8548.astype('float32'), [550,])), 4)
output = relay.Tuple([call_8535,call_8543,call_8547,const_8548,])
output2 = relay.Tuple([call_8536,call_8544,call_8549,const_8548,])
func_8553 = relay.Function([], output)
mod['func_8553'] = func_8553
mod = relay.transform.InferType()(mod)
mutated_mod['func_8553'] = func_8553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mutated_mod.get_global_var('func_8553')
call_8554 = func_8553_call()
output = call_8554
func_8555 = relay.Function([], output)
mutated_mod['func_8555'] = func_8555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_8558 = func_7106_call()
call_8559 = func_7106_call()
func_1094_call = mod.get_global_var('func_1094')
func_1099_call = mutated_mod.get_global_var('func_1099')
const_8567 = relay.const(3, dtype = "int16")#candidate|8567|()|const|int16
var_8568 = relay.var("var_8568", dtype = "int16", shape = (1980,))#candidate|8568|(1980,)|var|int16
const_8569 = relay.const([[-1],[2],[-2],[2],[6],[10],[-10],[-7],[6],[5],[-3],[-8],[-8],[-9],[-10],[-3],[-7],[2],[1],[-5],[-7],[-10],[-7],[-1],[6],[4],[-10],[4],[-7],[2],[-7],[-10],[-1],[-6],[-6],[9],[3],[2],[8],[-10],[1],[4],[8],[1],[10],[-5],[-2],[1],[-7],[8],[-5],[9],[-6],[-9],[-4],[9],[-5],[-1],[10],[10]], dtype = "uint64")#candidate|8569|(60, 1)|const|uint64
call_8566 = relay.TupleGetItem(func_1094_call(relay.reshape(const_8567.astype('int16'), []), relay.reshape(var_8568.astype('int16'), [15, 12, 11]), relay.reshape(const_8569.astype('uint64'), [60,]), ), 0)
call_8570 = relay.TupleGetItem(func_1099_call(relay.reshape(const_8567.astype('int16'), []), relay.reshape(var_8568.astype('int16'), [15, 12, 11]), relay.reshape(const_8569.astype('uint64'), [60,]), ), 0)
output = relay.Tuple([call_8558,call_8566,const_8567,var_8568,const_8569,])
output2 = relay.Tuple([call_8559,call_8570,const_8567,var_8568,const_8569,])
func_8572 = relay.Function([var_8568,], output)
mod['func_8572'] = func_8572
mod = relay.transform.InferType()(mod)
var_8573 = relay.var("var_8573", dtype = "int16", shape = (1980,))#candidate|8573|(1980,)|var|int16
output = func_8572(var_8573)
func_8574 = relay.Function([var_8573], output)
mutated_mod['func_8574'] = func_8574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8296_call = mod.get_global_var('func_8296')
func_8298_call = mutated_mod.get_global_var('func_8298')
call_8625 = func_8296_call()
call_8626 = func_8296_call()
output = relay.Tuple([call_8625,])
output2 = relay.Tuple([call_8626,])
func_8630 = relay.Function([], output)
mod['func_8630'] = func_8630
mod = relay.transform.InferType()(mod)
mutated_mod['func_8630'] = func_8630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mutated_mod.get_global_var('func_8630')
call_8631 = func_8630_call()
output = call_8631
func_8632 = relay.Function([], output)
mutated_mod['func_8632'] = func_8632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mod.get_global_var('func_8630')
func_8632_call = mutated_mod.get_global_var('func_8632')
call_8663 = relay.TupleGetItem(func_8630_call(), 0)
call_8664 = relay.TupleGetItem(func_8632_call(), 0)
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_8670 = func_7344_call()
call_8671 = func_7344_call()
output = relay.Tuple([call_8663,call_8670,])
output2 = relay.Tuple([call_8664,call_8671,])
func_8678 = relay.Function([], output)
mod['func_8678'] = func_8678
mod = relay.transform.InferType()(mod)
mutated_mod['func_8678'] = func_8678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8678_call = mutated_mod.get_global_var('func_8678')
call_8679 = func_8678_call()
output = call_8679
func_8680 = relay.Function([], output)
mutated_mod['func_8680'] = func_8680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_8686 = relay.TupleGetItem(func_6751_call(), 0)
call_8687 = relay.TupleGetItem(func_6753_call(), 0)
output = call_8686
output2 = call_8687
func_8696 = relay.Function([], output)
mod['func_8696'] = func_8696
mod = relay.transform.InferType()(mod)
output = func_8696()
func_8697 = relay.Function([], output)
mutated_mod['func_8697'] = func_8697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8709 = relay.var("var_8709", dtype = "float64", shape = (14, 12, 7))#candidate|8709|(14, 12, 7)|var|float64
var_8710 = relay.var("var_8710", dtype = "float64", shape = (14, 12, 7))#candidate|8710|(14, 12, 7)|var|float64
bop_8711 = relay.power(var_8709.astype('float64'), relay.reshape(var_8710.astype('float64'), relay.shape_of(var_8709))) # shape=(14, 12, 7)
output = relay.Tuple([bop_8711,])
output2 = relay.Tuple([bop_8711,])
func_8720 = relay.Function([var_8709,var_8710,], output)
mod['func_8720'] = func_8720
mod = relay.transform.InferType()(mod)
var_8721 = relay.var("var_8721", dtype = "float64", shape = (14, 12, 7))#candidate|8721|(14, 12, 7)|var|float64
var_8722 = relay.var("var_8722", dtype = "float64", shape = (14, 12, 7))#candidate|8722|(14, 12, 7)|var|float64
output = func_8720(var_8721,var_8722,)
func_8723 = relay.Function([var_8721,var_8722,], output)
mutated_mod['func_8723'] = func_8723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mod.get_global_var('func_8553')
func_8555_call = mutated_mod.get_global_var('func_8555')
call_8759 = relay.TupleGetItem(func_8553_call(), 3)
call_8760 = relay.TupleGetItem(func_8555_call(), 3)
uop_8775 = relay.erf(call_8759.astype('float64')) # shape=(550,)
uop_8777 = relay.erf(call_8760.astype('float64')) # shape=(550,)
output = relay.Tuple([uop_8775,])
output2 = relay.Tuple([uop_8777,])
func_8782 = relay.Function([], output)
mod['func_8782'] = func_8782
mod = relay.transform.InferType()(mod)
output = func_8782()
func_8783 = relay.Function([], output)
mutated_mod['func_8783'] = func_8783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7216_call = mod.get_global_var('func_7216')
func_7218_call = mutated_mod.get_global_var('func_7218')
call_8928 = func_7216_call()
call_8929 = func_7216_call()
output = call_8928
output2 = call_8929
func_8930 = relay.Function([], output)
mod['func_8930'] = func_8930
mod = relay.transform.InferType()(mod)
mutated_mod['func_8930'] = func_8930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8930_call = mutated_mod.get_global_var('func_8930')
call_8931 = func_8930_call()
output = call_8931
func_8932 = relay.Function([], output)
mutated_mod['func_8932'] = func_8932
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7355_call = mod.get_global_var('func_7355')
func_7356_call = mutated_mod.get_global_var('func_7356')
call_8974 = func_7355_call()
call_8975 = func_7355_call()
output = relay.Tuple([call_8974,])
output2 = relay.Tuple([call_8975,])
func_8977 = relay.Function([], output)
mod['func_8977'] = func_8977
mod = relay.transform.InferType()(mod)
output = func_8977()
func_8978 = relay.Function([], output)
mutated_mod['func_8978'] = func_8978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_9035 = func_8696_call()
call_9036 = func_8696_call()
var_9043 = relay.var("var_9043", dtype = "float64", shape = (3, 7, 7))#candidate|9043|(3, 7, 7)|var|float64
bop_9044 = relay.multiply(call_9035.astype('int64'), relay.reshape(var_9043.astype('int64'), relay.shape_of(call_9035))) # shape=(3, 7, 7)
bop_9047 = relay.multiply(call_9036.astype('int64'), relay.reshape(var_9043.astype('int64'), relay.shape_of(call_9036))) # shape=(3, 7, 7)
output = relay.Tuple([bop_9044,])
output2 = relay.Tuple([bop_9047,])
func_9069 = relay.Function([var_9043,], output)
mod['func_9069'] = func_9069
mod = relay.transform.InferType()(mod)
var_9070 = relay.var("var_9070", dtype = "float64", shape = (3, 7, 7))#candidate|9070|(3, 7, 7)|var|float64
output = func_9069(var_9070)
func_9071 = relay.Function([var_9070], output)
mutated_mod['func_9071'] = func_9071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mod.get_global_var('func_8630')
func_8632_call = mutated_mod.get_global_var('func_8632')
call_9088 = relay.TupleGetItem(func_8630_call(), 0)
call_9089 = relay.TupleGetItem(func_8632_call(), 0)
output = call_9088
output2 = call_9089
func_9097 = relay.Function([], output)
mod['func_9097'] = func_9097
mod = relay.transform.InferType()(mod)
mutated_mod['func_9097'] = func_9097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9097_call = mutated_mod.get_global_var('func_9097')
call_9098 = func_9097_call()
output = call_9098
func_9099 = relay.Function([], output)
mutated_mod['func_9099'] = func_9099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_9152 = relay.TupleGetItem(func_7523_call(), 0)
call_9153 = relay.TupleGetItem(func_7525_call(), 0)
func_7602_call = mod.get_global_var('func_7602')
func_7604_call = mutated_mod.get_global_var('func_7604')
const_9160 = relay.const([[-2],[8],[1],[9],[10],[-9],[-9],[-1],[4],[-7],[-8],[-2],[6],[-1],[-5],[-10],[-4],[-9],[8],[6],[-1],[3],[5],[-2],[9],[4],[2],[6],[-9],[4],[-8],[10],[-3],[-8],[1],[1],[8],[2],[7],[-2],[5],[-4],[3],[4],[-10],[5],[3],[1],[-8],[-8],[-2],[-1],[-10],[4],[8],[6],[4],[-10],[-1],[-1],[3],[1],[5],[1],[-1],[-10],[-8],[3],[-5],[7],[-5],[-9],[-2],[-5],[3],[4],[-4],[-1],[8],[-10],[-3],[-4],[-3],[-8],[6],[-6],[-6],[-7],[3],[-1],[-10],[4],[1],[10],[-7],[10],[3],[8],[-3],[-6],[2],[7],[6],[6],[7],[-8],[4],[8],[-7],[-7],[-9],[6],[-3],[9],[3],[-4],[-7],[4],[-4],[-5],[-10],[6],[6],[3],[2],[-10],[9],[4],[10],[-7],[-9],[9],[1],[-9],[4],[5],[-6],[-1],[-5],[-8],[4],[-10],[3],[4],[-5],[10],[3],[10],[-3],[-8],[3],[-2],[-4],[-1],[-5],[6],[8],[2],[-7],[-7],[-1],[-8],[6],[-10],[-7],[5],[-2],[8],[2],[-5],[-10],[-8],[-6],[-10],[-1],[7],[5],[8],[-5],[10],[7],[-1],[4],[4],[-1],[-5],[-1],[-9],[-3],[10],[-7],[-6],[6],[4],[2],[-3],[-9],[9],[6],[-9],[4],[9],[-7],[2],[9],[-6],[1],[-9],[-5],[8],[6],[10],[8],[9],[5],[-2],[-2],[-6],[-1],[-10],[10],[-9],[7],[-10],[2],[4],[9],[-3],[1],[2],[10],[7],[-7],[2],[1],[10],[-8],[-2],[10],[7],[-10],[-2],[-5],[8],[5],[-4],[-4],[-6],[3],[-8],[-9],[-6],[9],[2],[-10],[1],[-2],[-10],[8],[-2],[8],[7],[-6],[10],[2],[-4],[6],[10],[7],[-3],[10],[8],[-9],[-8],[-8],[7],[6],[-5],[-8],[2],[5],[-2],[5],[6],[-1],[1],[-5],[5],[9],[10],[-4],[1],[-2],[2],[3],[1],[-9],[1],[-3],[6],[-8],[-9],[-5],[-8],[10],[2],[-4],[3],[1],[-7],[9],[-2],[-8],[-2],[10],[9],[6],[2],[4],[8],[7],[-7],[-2],[8],[-6],[-8],[10],[3],[5],[-3],[5],[4],[1],[3],[-5],[1],[-10],[2],[9],[-3],[-4],[9],[-3],[5],[8],[-2],[1],[-2],[-1],[8],[-5],[-7],[-7],[7],[8],[10],[3],[5],[2],[1],[-8],[-10],[-10],[-1],[-9],[-6],[-10],[-9],[3],[-5],[-8],[-2],[-6],[4],[-6],[5],[9],[-3],[10],[-1],[-5],[-3],[-1],[3],[2],[2],[3],[-8],[10],[5],[8],[-2],[-7],[-7],[10],[-6],[-4],[-1],[-5],[6],[2],[-5],[3],[-4],[-7],[9],[-10],[4],[7],[-4],[7],[4],[-1],[6],[-1],[1],[-2],[6],[2],[-6],[-10],[-6],[-7],[8],[2],[-3],[-4],[-2],[-5],[-10],[1],[-8],[10],[6],[-6],[4],[-9],[-6],[3],[-2],[-10],[7],[5],[-8],[6],[-5],[-1],[-9],[8],[6],[-8],[-10],[1],[5],[2],[2],[-4],[3],[-6],[8],[-10],[10],[7],[-4],[-5],[-7],[-9],[1],[-2],[7],[-6],[5],[5],[9],[-2],[-5],[1],[6],[5],[3],[10],[-4],[-8],[10],[-1],[-6],[-5],[-7],[1],[-4],[-3],[3],[-6],[-2],[-9],[-2],[4],[8],[1],[3],[-7],[9],[10],[-6],[1],[1],[-1],[-6],[3],[2],[2],[1],[-10],[-9],[10],[-2],[-1],[-3],[-8],[9],[9],[3],[-2],[10],[10],[1],[6],[9],[2],[-6],[10],[-1],[3],[-9],[1],[2],[5],[3],[-6],[-7],[5],[-8],[10],[6],[5],[-4],[9],[5],[9],[5],[-1],[-1],[2],[-6],[-9],[7],[-10],[4],[2],[2]], dtype = "uint64")#candidate|9160|(560, 1)|const|uint64
call_9159 = relay.TupleGetItem(func_7602_call(relay.reshape(const_9160.astype('uint64'), [560,])), 2)
call_9161 = relay.TupleGetItem(func_7604_call(relay.reshape(const_9160.astype('uint64'), [560,])), 2)
func_7999_call = mod.get_global_var('func_7999')
func_8004_call = mutated_mod.get_global_var('func_8004')
const_9172 = relay.const([-1,8,-8,9,10,-6,5,-4,-3,-10,6,-4,-6,-3,8,-10,-6,4,-7,6,9,6,1,7,-2,2,3,-5,3,-1,1,-9,2,-10,8,-8,9,1,6,6,6,-8,-4,-6,-10,-7,2,9,-1,5,-7,4,-5,-8,2,-8,3,-7,-8,5,4,2,-8,-10,-10,-8,-7,4,7,4,-7,-10,-10,-9,-2,8,-6,1,-1,-5,-7,-7,5,-8,-3,-4,7,-3,2,7,6,-9,-6,-8,-3,-8,-6,-3,-6,3,-5,2,-2,-1,8,-10,3,-9,-2,-8,10,3,10,-6,1,8,6,-8,-8,5,-6,2,-8,8,8,5,1,1,-8,-2,6,-4,1,-3,2,-6,-6,-8,9,-2,-4,-2,-9,-8,2,5,-9,2,-3,-2,-4,-5,-7,5,-1,-1,-6,-1,8,1,9,-7,6,-2,-6,-6,-3,3,4,-5,4,1,9,-4,-1,-6,-2,-3,-2,-7,-1,9,6,3,-9,-6,-4,-3,-10,9,-4,6,-10,4,3,-2,-6,8,4,-3,-10,4,-7,7,7,-1,-5,-9,-3,6,-6,-2,-1,6,2,6,10,5,10,5,2,-8,-10,-1,-2,2,-7,-4,-5,-4,2,10,-4,7,1,-1,7,-9,8,3,6,8,10,-2,4,3,-5,-8,-9,3,9,2,-3,7,10,-1,-5,-10,3,-1,5,5,-8,9,9,1,3,-6,-4,-10,-2,1,-2,-2,2,-3,9,6,-10,9,6,7,-3,8,5,4,-10,5,-7,-8,2,3,-1,1,4,3,7,-9,-5,10,6,-9,8,-8,-3,-3,10,-6,-6,4,-6,10,-7,6,8,1,-9,-10,-4,-3,7,-2,1,-9,5,-5,-10,-4,7,-8,5,9,-2,10,-9,5,-8,-6,4,-4,-1,-10,5,10,4,-7,7,-5,-6,7,8,5,8,5,-9,1,-7,2,4,5,10,-9,9,6,-10,3,4,6,-9,3,7,9,2,-9,3,-6,-6,-10,10,-10,-2,8,1,7,2,-10,-2,6,-2,2,-7,-8,3,7,7,-4,8,-4,-4,9,-1,-9,-9,6,-8,-7,-7,7,7,5,-1,3,-1,-10,-8,-2,-9,-1,-4,10,-7,6,-3,4,-10,6,-8,-3,-5,-3,-4,-3,8,1,-3,5,-9,-4,5,-4,6,6,-8,4,-2,10,4,8,7,3,2,10,8,-4,1,-9,10,5,-4,3,6,3,7,1,1,-6,3,-4,1,5,8,2,-9,5,-6,1,-4,-3,6,-6,1,7,1,4,-9,-5,10,4,4,5,10,3,2,6,1,2,6,-5,-3,1,5,1,-5,7,8,1,-1,3,-2,1,1,-7,-5,5,9,-3,6,-2,-1,-2,4,-7,10,6,9,7,-1,8,-7,7,3,-2,4,-9,4,1,7,-1,-10,-10,6,-8,2,-6,-8,-4,-3,-9,-10,-9,2,-4,-10,5,-4,8,4,1,-9,-4,-10,-10,-7,-9,9,-3,7,-9,2,8,1,-10,-9,1,-7,-9,-5,1,9,-1,5,-1,-3,3,4,-3,-7,-2,-3,-6,-9,-9,-5,-10,-8,5,7,10,-6,-5,-4,9,-3,-8,5,-1,1,3,-10,-2,-2,-4,5,-8,4,-3,-4,-10,3,-5,3,5,6,10,8,2,1,10,-9,8,2,2,6,-2,1,9,5,-8,1,5,-1,1,5,7,10,7,-9,-7,-2,-5,-6,5,-8,2,-10,-1,6,-3,5,-6,7,6,-2,-10,10,7,10,9,4,9,10,7,4,-8,-1,-4,10,6,-1,-8,2,10,7,9,-3,-7,8,1,-5,-1,-7,-7,-2,-9,-9,-7,2,4,1,3,2,8,-6,-2,-2,-1,7,-6,-3,6,-1,5,-2,-5,10,8,-7,-4,9,-6,-10,-10,7,5,-10,-1,4,4,-3,-1,-6,9,-7,-6,10,7,-1,4,-2,7,2,3,-2,-3,8,1,5,5,2,10,5,1,-6,-3,6,10,-6,1,10,6,-8,-1,-7,-4,-10,-3,4,1,9,-8,-2,10,-1,-9,-6,10,1,8,-8,1,9,-2,-5,2,-7,-8,9,8,-2,-5,-3,4,-6,4,-7,3,8,-8,8,-9,-10,-3,-9,-1,9,9,10,-8,8,-2,8,2,3,-10,-9,6,-10,-10,-2,-7,-6,-5,-2,3,-4,6,2,-9,-9,6,10,7,2,8,-8,-7,3,-1,4,6,10,-1,1,1,-8,8,-10,-7,-2,-8,-10,-5,8,8,1,-3,8,-5,-3,1,-3,9,-3,8,1,-6,-3,-4,6,-5,7,-7,-2,-6,-1,6,5,1,-2,-3,-5,6,1,-8,-3,5,-1,-7,-7,7,9,5,-9,-1,-5,5,-5,-5,10,-5,-6,-5,5,7,-6,-1,8,-10,-2,9,5,-7,-5,-9,6,10,-4,-9,8,2,-2,10,9,-8,-10,10,9,8,-10,8,2,-9,6,7,4,9,-2,-8,8,-4,3,4,1,-7,-10,8,7,-10,3,-7,7,-5,-5,-10,10,-3,-9,-8,-10,3,4,-4,7,1,3,7,6,-9,-6,5,-4,-1,-5,5,-6,7,-8,-8,-5,4,-1,-8,-4,9,5,-8,-2,3,-9,-5,5,-4,5,5,-3,7,-10,2,-1,6,4,-6,2,-8,-6,-6,6,-3,2,-10,6,10,4,2,2,5,9,-6,1,-1,-8,-9,7,-5,9,-5,-7,-3,-8,8,2,-7,7,1,7,6,-1,2,-6,-8,-6,-1,7,-4,8,4,-7,10,-4,1,-7,9,-1,-5,-9,1,-5,6,6,-6,4,-4,-8,-3,7,6,-1,1,7,7,8,-1,10,-4,9,-1,-9,2,-9,-2,10,-8,4,-1,5,6,9,10,-5,8,-4,7,-3,-3,-5,-9,-4,4,-6,10,6,-9,-5,4,5,6,-10,5,1,6,-2,10,1,5,-2,3,10,1,-2,7,-7,-7,5,8,1,-3,8,8,-9,7,7,-9,3,-6,7,2,-6,8,-2,-9,-2,-5,-8,-10,-7,8,8,-3,-9,7,2,-7], dtype = "uint32")#candidate|9172|(1152,)|const|uint32
var_9173 = relay.var("var_9173", dtype = "bool", shape = (1008,))#candidate|9173|(1008,)|var|bool
var_9174 = relay.var("var_9174", dtype = "uint64", shape = (256,))#candidate|9174|(256,)|var|uint64
call_9171 = relay.TupleGetItem(func_7999_call(relay.reshape(const_9172.astype('uint32'), [1152,]), relay.reshape(var_9173.astype('bool'), [1008,]), relay.reshape(var_9174.astype('uint64'), [256,]), ), 1)
call_9175 = relay.TupleGetItem(func_8004_call(relay.reshape(const_9172.astype('uint32'), [1152,]), relay.reshape(var_9173.astype('bool'), [1008,]), relay.reshape(var_9174.astype('uint64'), [256,]), ), 1)
output = relay.Tuple([call_9152,call_9159,const_9160,call_9171,const_9172,var_9173,var_9174,])
output2 = relay.Tuple([call_9153,call_9161,const_9160,call_9175,const_9172,var_9173,var_9174,])
func_9182 = relay.Function([var_9173,var_9174,], output)
mod['func_9182'] = func_9182
mod = relay.transform.InferType()(mod)
var_9183 = relay.var("var_9183", dtype = "bool", shape = (1008,))#candidate|9183|(1008,)|var|bool
var_9184 = relay.var("var_9184", dtype = "uint64", shape = (256,))#candidate|9184|(256,)|var|uint64
output = func_9182(var_9183,var_9184,)
func_9185 = relay.Function([var_9183,var_9184,], output)
mutated_mod['func_9185'] = func_9185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mod.get_global_var('func_8553')
func_8555_call = mutated_mod.get_global_var('func_8555')
call_9312 = relay.TupleGetItem(func_8553_call(), 0)
call_9313 = relay.TupleGetItem(func_8555_call(), 0)
output = relay.Tuple([call_9312,])
output2 = relay.Tuple([call_9313,])
func_9320 = relay.Function([], output)
mod['func_9320'] = func_9320
mod = relay.transform.InferType()(mod)
output = func_9320()
func_9321 = relay.Function([], output)
mutated_mod['func_9321'] = func_9321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_9378 = relay.TupleGetItem(func_7952_call(), 2)
call_9379 = relay.TupleGetItem(func_7954_call(), 2)
output = call_9378
output2 = call_9379
func_9380 = relay.Function([], output)
mod['func_9380'] = func_9380
mod = relay.transform.InferType()(mod)
mutated_mod['func_9380'] = func_9380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9380_call = mutated_mod.get_global_var('func_9380')
call_9381 = func_9380_call()
output = call_9381
func_9382 = relay.Function([], output)
mutated_mod['func_9382'] = func_9382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9428 = relay.var("var_9428", dtype = "float32", shape = (16, 1, 3))#candidate|9428|(16, 1, 3)|var|float32
uop_9429 = relay.cosh(var_9428.astype('float32')) # shape=(16, 1, 3)
output = uop_9429
output2 = uop_9429
func_9439 = relay.Function([var_9428,], output)
mod['func_9439'] = func_9439
mod = relay.transform.InferType()(mod)
mutated_mod['func_9439'] = func_9439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9440 = relay.var("var_9440", dtype = "float32", shape = (16, 1, 3))#candidate|9440|(16, 1, 3)|var|float32
func_9439_call = mutated_mod.get_global_var('func_9439')
call_9441 = func_9439_call(var_9440)
output = call_9441
func_9442 = relay.Function([var_9440], output)
mutated_mod['func_9442'] = func_9442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_9455 = relay.TupleGetItem(func_7653_call(), 0)
call_9456 = relay.TupleGetItem(func_7654_call(), 0)
func_6961_call = mod.get_global_var('func_6961')
func_6964_call = mutated_mod.get_global_var('func_6964')
const_9468 = relay.const([0.238648,-3.309865,-1.584833,7.451442,9.480215,-8.545754,8.766446,3.671223,-1.251586,9.246372,-6.562961,-0.452909,-0.782326,2.563800,-1.191679,8.055364,-5.361292,8.788295,7.280910,5.407828,8.585545,-0.355653,-5.173952,-4.884931,-0.961951,3.808376,9.025273,-5.352591,-2.576346,1.474464,0.026158,-6.101783,-0.319586,-2.057629,-2.925597,0.754872,5.288278,-9.888471,5.045908,-4.354534,-8.996405,-7.211321,8.249375,-4.833890,4.250096,-4.993630,-4.064043,-1.779462,3.682551,0.002482,-6.062400,4.186740,-5.620204,7.549841,-6.441210,6.025575,1.192768,1.631842,5.819193,-9.126577,7.939098,8.629481,6.811450,5.372514,-5.300599,7.163063,2.172232,-7.773126,-6.736363,4.458082,4.791381,-4.927993,8.046683,5.648793,6.028519,4.952557,6.302623,-5.335594,-6.396763,5.269032,-2.548860,5.809173,8.769917,-8.461618,2.443437,1.540359,-2.305310,3.328679,9.790708,-1.007910,6.968358,6.937830,-2.045739,7.253814,7.725443,0.758575,9.972293,5.558169,-8.791254,8.679191,-9.487418,-9.808857,-8.701536,-5.687625,7.726994,-5.377295,-6.197436,5.609786,9.639550,9.140349,8.324135,3.969146,6.279751,2.385422,-9.036750,0.716168,6.281020,3.366099,5.385658,6.160348,4.707572,7.262394,-6.745370,-3.364001,-1.709016,-5.660450,8.050311,-7.316411,7.318984,-6.583468,-9.772584,-9.869007,-7.525673,0.492278,3.244521,-4.234714,-9.475827,-6.509532,-8.372097,2.987548,-7.387505,-3.573803,3.415732,-9.683988,-0.673225,-4.087734,-9.903148,5.064028,-6.527950,-0.174418,4.353962,-4.370411,4.541913,-7.299942,-9.134171,-4.613506,-6.454964,-5.592000,1.196403,-0.851103,1.730582,2.875921,3.457116,-2.078537,1.730965,0.971769,3.363550,0.195338,-6.256767,-3.685318,9.156512,3.142174,8.895751,6.523001,-5.330099,7.798896,-9.322663,4.681160,3.371251,5.404472,-2.845181,0.715795,2.906869,-4.057547,6.246713,-7.674649,2.487990,-9.912961,0.263636,-1.237086,8.631862,0.727611,-1.895479,6.559509,7.026198,-2.430722,3.851946,3.770736,-7.648487,-9.383844,4.086436,-6.403457,-4.557591,7.432564,-4.291997,0.893932,1.878885,9.575526,1.500418,7.955243,-0.618906,-6.608150,-0.252279,-9.689581,-6.120862,-3.179000,1.812069,-8.316815,8.185090,7.666239,8.967493,0.126711,7.669274,-5.298771,5.962777,6.675179,-0.362533,1.633958,-8.390723,3.946345,-0.413966,-9.571086,4.146765,2.777330,-4.523064,-1.249291,4.075615,5.799419,9.615776,9.976509,2.107945,-1.331182,-8.159826,-1.226729,1.664462,7.123708,8.637792,9.909594,6.130569,5.121414,0.008982,7.132964,7.241549,1.636711,5.373495,6.140910,-6.992273,-8.062785,4.061858,7.000839,-5.826130,-7.007000,-1.146072,-9.904013,-5.349072,7.088205,-1.633670,-0.347527,0.225651,-2.034074,-2.026121,-5.425850,8.027028,-2.758238,3.841780,3.103190,-1.406843,-4.613280,3.921387,-2.857612,-4.878755,1.297834,0.275144,0.654187,4.507729,5.927599,0.302409,-8.655832,-3.059724,-1.256768,-3.425182,8.969424,8.930025,1.681335,8.816544,2.268655,-6.369175,-0.640807,-1.432836,-1.417241,5.085805,-6.702170,3.785548,7.200308,5.290080,-9.089535,3.064753,-8.398294,9.358196,6.551853,-7.699741,-5.118419,8.011184,-1.993888,-7.226560,7.589104,-1.730472,5.096427,1.879247,2.909414,-8.339246,-8.169696,9.316822,-0.632516,9.896129,7.924139,-5.141589,-8.394691,-4.846725,-8.169653,7.247012,-5.036259,0.284191,-6.732452,-8.845423,7.462547,1.543583,-3.663169,-6.715028,3.621755,-4.216850,8.896697,-2.671366,-4.856087,-8.944545,-1.142844,8.501028,0.924791,-5.167380,4.994585,1.315554,1.420133,-6.066642,-5.622984,-2.785334,-6.898064,-1.133677,-5.226237,6.116927,-1.556665,0.743511,-6.929914,9.813717,9.051310,4.369840,0.546061,3.319151,4.590673,-7.832927,-3.721204,7.844669,-3.922679,1.395361,-0.463240,5.560467,-7.974170,8.028094,9.548801,7.403711,-3.655638,4.199510,7.896411,-1.590618,2.189820,-9.352645,-2.750729,-5.549102,-5.907269,9.279882,3.837122,6.567678,3.212898,-7.602986,4.284606,1.759310,-2.649838,9.177123,3.006703,-2.182094,6.703591,-8.537399,-5.342728,-7.070656,-3.844205,9.630158,-9.928867,-7.688998,-6.329988,5.082725,-8.944836,3.759231,9.682964,-8.951745,7.187869,4.244091,-2.560519,-4.136172,3.119823,7.243254,-8.650947,7.964549,1.510863,-4.441598,-5.727911,3.378545,-2.317754,4.850454,-6.890969,-1.555562,-8.969858,-9.989096,9.460898,4.433256,5.905109,9.462656,8.270758,-7.297700,-6.656485,-5.545235,-4.300121,4.532426,1.496555,9.027987,-4.925616,0.443520,2.257094,1.562707,-2.357847,3.132948,1.634073,9.076400,5.411885,2.117219,-7.419568,-9.247240,-5.969999,8.055434,-9.540769,9.811048,-9.877415,8.006448,-5.204967,-1.603943,0.267156,-7.817003,-4.396369,-8.823099,2.192299,6.482336,1.151345,1.298446,6.320978,1.594363,4.947071,1.378127,1.657429,0.051562,5.553734,-0.408853,-4.104866,-8.630990,-7.647133,-8.303353,-6.354752,1.940910,-2.886080,1.250554,1.704227,2.963303,5.900023,-8.991650,-3.214137,-4.678282,-7.350654,-7.571078,9.624149,7.597135,3.945340,-7.173936,-9.046913,-7.439121,-2.161633,-5.922012,-0.401087,-7.187294,-1.484416,1.980964,-1.883372,1.123361,-2.622977,8.804445,-1.193049,-9.090347,9.585654,1.090612,-7.131554,-6.978852,-9.462179,8.278549,-6.528377,-1.060878,-9.281241,2.265789,-7.726455,5.940587,1.850692,-5.729145,-3.874794,0.004469,7.256811,7.118047,-3.701102,-5.126106,-2.782234,-1.057355,1.632199,-9.639758,-8.396534,2.429813,-1.597700,0.911086,1.986632,0.465461,-1.554202,2.351329,9.583089,-3.022694,-8.519936,-8.890721,-4.797902], dtype = "float32")#candidate|9468|(550,)|const|float32
call_9467 = relay.TupleGetItem(func_6961_call(relay.reshape(const_9468.astype('float32'), [10, 5, 11])), 0)
call_9469 = relay.TupleGetItem(func_6964_call(relay.reshape(const_9468.astype('float32'), [10, 5, 11])), 0)
output = relay.Tuple([call_9455,call_9467,const_9468,])
output2 = relay.Tuple([call_9456,call_9469,const_9468,])
func_9475 = relay.Function([], output)
mod['func_9475'] = func_9475
mod = relay.transform.InferType()(mod)
output = func_9475()
func_9476 = relay.Function([], output)
mutated_mod['func_9476'] = func_9476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8678_call = mod.get_global_var('func_8678')
func_8680_call = mutated_mod.get_global_var('func_8680')
call_9486 = relay.TupleGetItem(func_8678_call(), 1)
call_9487 = relay.TupleGetItem(func_8680_call(), 1)
output = call_9486
output2 = call_9487
func_9493 = relay.Function([], output)
mod['func_9493'] = func_9493
mod = relay.transform.InferType()(mod)
output = func_9493()
func_9494 = relay.Function([], output)
mutated_mod['func_9494'] = func_9494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_9521 = relay.TupleGetItem(func_7952_call(), 2)
call_9522 = relay.TupleGetItem(func_7954_call(), 2)
func_8349_call = mod.get_global_var('func_8349')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_9543 = func_8349_call()
call_9544 = func_8349_call()
output = relay.Tuple([call_9521,call_9543,])
output2 = relay.Tuple([call_9522,call_9544,])
func_9549 = relay.Function([], output)
mod['func_9549'] = func_9549
mod = relay.transform.InferType()(mod)
output = func_9549()
func_9550 = relay.Function([], output)
mutated_mod['func_9550'] = func_9550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_9564 = func_7106_call()
call_9565 = func_7106_call()
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_9570 = func_7106_call()
call_9571 = func_7106_call()
output = relay.Tuple([call_9564,call_9570,])
output2 = relay.Tuple([call_9565,call_9571,])
func_9607 = relay.Function([], output)
mod['func_9607'] = func_9607
mod = relay.transform.InferType()(mod)
mutated_mod['func_9607'] = func_9607
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9607_call = mutated_mod.get_global_var('func_9607')
call_9608 = func_9607_call()
output = call_9608
func_9609 = relay.Function([], output)
mutated_mod['func_9609'] = func_9609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8192_call = mod.get_global_var('func_8192')
func_8194_call = mutated_mod.get_global_var('func_8194')
call_9618 = relay.TupleGetItem(func_8192_call(), 0)
call_9619 = relay.TupleGetItem(func_8194_call(), 0)
output = call_9618
output2 = call_9619
func_9637 = relay.Function([], output)
mod['func_9637'] = func_9637
mod = relay.transform.InferType()(mod)
mutated_mod['func_9637'] = func_9637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9637_call = mutated_mod.get_global_var('func_9637')
call_9638 = func_9637_call()
output = call_9638
func_9639 = relay.Function([], output)
mutated_mod['func_9639'] = func_9639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9475_call = mod.get_global_var('func_9475')
func_9476_call = mutated_mod.get_global_var('func_9476')
call_9650 = relay.TupleGetItem(func_9475_call(), 2)
call_9651 = relay.TupleGetItem(func_9476_call(), 2)
output = relay.Tuple([call_9650,])
output2 = relay.Tuple([call_9651,])
func_9665 = relay.Function([], output)
mod['func_9665'] = func_9665
mod = relay.transform.InferType()(mod)
output = func_9665()
func_9666 = relay.Function([], output)
mutated_mod['func_9666'] = func_9666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_9673 = relay.TupleGetItem(func_6751_call(), 0)
call_9674 = relay.TupleGetItem(func_6753_call(), 0)
output = relay.Tuple([call_9673,])
output2 = relay.Tuple([call_9674,])
func_9713 = relay.Function([], output)
mod['func_9713'] = func_9713
mod = relay.transform.InferType()(mod)
mutated_mod['func_9713'] = func_9713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9713_call = mutated_mod.get_global_var('func_9713')
call_9714 = func_9713_call()
output = call_9714
func_9715 = relay.Function([], output)
mutated_mod['func_9715'] = func_9715
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9750 = relay.var("var_9750", dtype = "float64", shape = ())#candidate|9750|()|var|float64
var_9751 = relay.var("var_9751", dtype = "float64", shape = (1, 5, 13))#candidate|9751|(1, 5, 13)|var|float64
bop_9752 = relay.divide(var_9750.astype('float64'), var_9751.astype('float64')) # shape=(1, 5, 13)
output = relay.Tuple([bop_9752,])
output2 = relay.Tuple([bop_9752,])
func_9758 = relay.Function([var_9750,var_9751,], output)
mod['func_9758'] = func_9758
mod = relay.transform.InferType()(mod)
var_9759 = relay.var("var_9759", dtype = "float64", shape = ())#candidate|9759|()|var|float64
var_9760 = relay.var("var_9760", dtype = "float64", shape = (1, 5, 13))#candidate|9760|(1, 5, 13)|var|float64
output = func_9758(var_9759,var_9760,)
func_9761 = relay.Function([var_9759,var_9760,], output)
mutated_mod['func_9761'] = func_9761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8192_call = mod.get_global_var('func_8192')
func_8194_call = mutated_mod.get_global_var('func_8194')
call_9826 = relay.TupleGetItem(func_8192_call(), 1)
call_9827 = relay.TupleGetItem(func_8194_call(), 1)
output = relay.Tuple([call_9826,])
output2 = relay.Tuple([call_9827,])
func_9832 = relay.Function([], output)
mod['func_9832'] = func_9832
mod = relay.transform.InferType()(mod)
output = func_9832()
func_9833 = relay.Function([], output)
mutated_mod['func_9833'] = func_9833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_9842 = relay.TupleGetItem(func_7523_call(), 0)
call_9843 = relay.TupleGetItem(func_7525_call(), 0)
output = relay.Tuple([call_9842,])
output2 = relay.Tuple([call_9843,])
func_9894 = relay.Function([], output)
mod['func_9894'] = func_9894
mod = relay.transform.InferType()(mod)
mutated_mod['func_9894'] = func_9894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9894_call = mutated_mod.get_global_var('func_9894')
call_9895 = func_9894_call()
output = call_9895
func_9896 = relay.Function([], output)
mutated_mod['func_9896'] = func_9896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mod.get_global_var('func_8553')
func_8555_call = mutated_mod.get_global_var('func_8555')
call_9929 = relay.TupleGetItem(func_8553_call(), 1)
call_9930 = relay.TupleGetItem(func_8555_call(), 1)
output = relay.Tuple([call_9929,])
output2 = relay.Tuple([call_9930,])
func_9933 = relay.Function([], output)
mod['func_9933'] = func_9933
mod = relay.transform.InferType()(mod)
mutated_mod['func_9933'] = func_9933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9933_call = mutated_mod.get_global_var('func_9933')
call_9934 = func_9933_call()
output = call_9934
func_9935 = relay.Function([], output)
mutated_mod['func_9935'] = func_9935
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8630_call = mod.get_global_var('func_8630')
func_8632_call = mutated_mod.get_global_var('func_8632')
call_9961 = relay.TupleGetItem(func_8630_call(), 0)
call_9962 = relay.TupleGetItem(func_8632_call(), 0)
output = call_9961
output2 = call_9962
func_10020 = relay.Function([], output)
mod['func_10020'] = func_10020
mod = relay.transform.InferType()(mod)
mutated_mod['func_10020'] = func_10020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10020_call = mutated_mod.get_global_var('func_10020')
call_10021 = func_10020_call()
output = call_10021
func_10022 = relay.Function([], output)
mutated_mod['func_10022'] = func_10022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9933_call = mod.get_global_var('func_9933')
func_9935_call = mutated_mod.get_global_var('func_9935')
call_10033 = relay.TupleGetItem(func_9933_call(), 0)
call_10034 = relay.TupleGetItem(func_9935_call(), 0)
output = call_10033
output2 = call_10034
func_10047 = relay.Function([], output)
mod['func_10047'] = func_10047
mod = relay.transform.InferType()(mod)
output = func_10047()
func_10048 = relay.Function([], output)
mutated_mod['func_10048'] = func_10048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_10104 = relay.TupleGetItem(func_8021_call(), 0)
call_10105 = relay.TupleGetItem(func_8022_call(), 0)
output = call_10104
output2 = call_10105
func_10106 = relay.Function([], output)
mod['func_10106'] = func_10106
mod = relay.transform.InferType()(mod)
output = func_10106()
func_10107 = relay.Function([], output)
mutated_mod['func_10107'] = func_10107
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_10192 = relay.TupleGetItem(func_6751_call(), 0)
call_10193 = relay.TupleGetItem(func_6753_call(), 0)
func_531_call = mod.get_global_var('func_531')
func_535_call = mutated_mod.get_global_var('func_535')
const_10195 = relay.const([7,9,9,-2,10,6,-9,-4,-1,2,-3,-5,8,10,-9,-7,9,10,2,2,10,-1,-4,-1,-3,1,3,10,-5,-1,-9,3,-6,4,4,9,8,2,-6,-9,5,-7,-7,2,-7,-8,-1,4,3,7,-8,1,8,-7,6,5,7,10,9,6], dtype = "uint64")#candidate|10195|(60,)|const|uint64
call_10194 = func_531_call(relay.reshape(const_10195.astype('uint64'), [2, 5, 6]), relay.reshape(const_10195.astype('uint64'), [2, 5, 6]), )
call_10196 = func_531_call(relay.reshape(const_10195.astype('uint64'), [2, 5, 6]), relay.reshape(const_10195.astype('uint64'), [2, 5, 6]), )
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_10209 = func_7106_call()
call_10210 = func_7106_call()
func_9758_call = mod.get_global_var('func_9758')
func_9761_call = mutated_mod.get_global_var('func_9761')
const_10239 = relay.const(1.521787, dtype = "float64")#candidate|10239|()|const|float64
var_10240 = relay.var("var_10240", dtype = "float64", shape = (65,))#candidate|10240|(65,)|var|float64
call_10238 = relay.TupleGetItem(func_9758_call(relay.reshape(const_10239.astype('float64'), []), relay.reshape(var_10240.astype('float64'), [1, 5, 13]), ), 0)
call_10241 = relay.TupleGetItem(func_9761_call(relay.reshape(const_10239.astype('float64'), []), relay.reshape(var_10240.astype('float64'), [1, 5, 13]), ), 0)
func_9607_call = mod.get_global_var('func_9607')
func_9609_call = mutated_mod.get_global_var('func_9609')
call_10242 = relay.TupleGetItem(func_9607_call(), 0)
call_10243 = relay.TupleGetItem(func_9609_call(), 0)
func_7602_call = mod.get_global_var('func_7602')
func_7604_call = mutated_mod.get_global_var('func_7604')
const_10251 = relay.const([[-6,-9],[-7,2],[-2,-4],[8,9],[-8,-5],[-5,8],[-4,-10],[2,1],[1,10],[8,5],[-8,-7],[4,-8],[-2,-5],[7,-7],[-8,3],[5,9],[-1,-3],[8,1],[8,4],[5,-6],[4,5],[5,-6],[9,4],[-1,-1],[1,-3],[1,-6],[-5,2],[-2,-8],[10,-2],[7,9],[-7,-1],[5,3],[3,6],[2,-4],[-2,-7],[-5,-5],[-8,9],[4,1],[-2,-10],[-4,4],[10,3],[1,9],[6,-2],[-10,-7],[3,-4],[-5,-6],[7,3],[-8,-9],[8,-10],[-1,-4],[6,-7],[2,-9],[-9,2],[9,-10],[-4,10],[-1,-10],[-10,8],[3,8],[10,8],[-9,-9],[-9,2],[-10,6],[5,-8],[2,-3],[-10,6],[5,-3],[-9,-10],[-9,7],[-1,5],[1,-5],[-5,1],[1,-4],[7,4],[-3,-8],[9,3],[9,5],[-8,1],[-4,-4],[-9,10],[10,-3],[-3,-10],[6,-1],[8,-5],[3,-6],[2,8],[6,-7],[-8,-5],[1,5],[6,2],[-3,-9],[6,-7],[5,8],[3,-5],[10,3],[1,6],[7,7],[5,5],[4,-9],[9,-9],[-1,2],[-5,-10],[1,10],[-1,-5],[8,-2],[-3,2],[-3,8],[-9,8],[6,-4],[9,3],[-7,-1],[1,-7],[-7,-3],[7,8],[8,-6],[4,7],[-4,-8],[-6,2],[-8,-4],[-6,-10],[-1,3],[-10,-10],[8,-7],[9,-10],[-6,-7],[-3,-6],[3,-2],[10,-4],[-6,-8],[10,7],[5,-10],[-8,9],[-1,6],[7,-5],[-1,-1],[-10,1],[4,6],[-9,-1],[7,-9],[2,-10],[-4,6],[-10,4],[-9,-10],[2,9],[-3,7],[6,-4],[-9,-9],[-9,-3],[7,8],[2,7],[-7,-2],[-10,-4],[-6,3],[-8,6],[-10,-6],[3,-5],[1,-8],[-5,4],[-3,2],[9,-6],[-4,-6],[8,10],[6,8],[-9,10],[4,1],[-2,-1],[3,-8],[-7,7],[3,-6],[3,8],[5,-9],[-9,-4],[-6,2],[2,-2],[-7,9],[-3,7],[-10,-9],[-2,4],[-5,4],[3,-6],[-3,-8],[-2,-1],[-1,2],[7,-1],[4,-1],[9,6],[8,7],[-7,2],[-1,-4],[1,1],[6,-5],[5,-9],[10,-7],[-3,4],[-4,5],[-5,-1],[7,1],[-1,-9],[10,-9],[4,5],[-5,-4],[7,2],[-8,-1],[5,-9],[-7,10],[5,-6],[-7,-9],[10,6],[6,6],[5,-5],[6,-6],[-7,-3],[7,4],[-7,8],[-7,7],[-1,-5],[-1,2],[-10,1],[-10,6],[3,-4],[7,4],[-10,7],[9,7],[7,9],[-4,5],[8,9],[-2,7],[-6,-6],[1,-6],[2,10],[-7,1],[8,1],[-3,-5],[2,-8],[1,-10],[8,-2],[5,4],[1,-1],[1,-4],[4,-3],[4,7],[-4,-10],[2,-3],[-7,-1],[-3,2],[-9,4],[-4,2],[-4,4],[-5,-3],[6,5],[5,-10],[3,5],[-8,-9],[7,-8],[-2,9],[-5,3],[4,10],[-1,-9],[3,9],[5,-3],[8,-10],[7,-5],[8,4],[-7,-5],[5,10],[-2,-2],[-10,-2],[-4,8],[7,8],[5,3],[-9,7],[6,-6],[1,6],[-5,-10],[-9,10],[7,7],[3,10],[-1,1],[9,-6],[2,-5],[8,-6]], dtype = "uint64")#candidate|10251|(280, 2)|const|uint64
call_10250 = relay.TupleGetItem(func_7602_call(relay.reshape(const_10251.astype('uint64'), [560,])), 2)
call_10252 = relay.TupleGetItem(func_7604_call(relay.reshape(const_10251.astype('uint64'), [560,])), 2)
func_8419_call = mod.get_global_var('func_8419')
func_8422_call = mutated_mod.get_global_var('func_8422')
const_10256 = relay.const([-3,5,-6,-10,5,-6,-2,2,5,1,7,4,-10,-6,-6,-10,-5,5,-9,4,10,1,-9,5,-2,-7,4,4,-6,-10,1,-1,9,10,1,-2,-3,3,7,-6,-4,9,-8,-4,3,-5,6,-3,-2,-2,6,-3,8,-1,-2,5,1,6,9,2,-3,-8,-2,5,3,-6,3,8,-5,-8,5,5,-9,3,-10,-2,1,4,-1,9,8,3,-5,5,-9,9,6,7,-4,7,-7,-8,9,4,-3,-5,10,-2,-10,-7,10,10,7,-5,-10,-4,1,5,-4,-1,-4,9,6,-9,10,3,9,8,-3,-8,3,-9,-5,-6,5,-7,-6,3,8,8,5,8,7,1,-8,4,-2,-8,9,-6,-1,-5,9,-7,-7,7,-8,-9,2,6,10,1,-5,7,-1,10,7,-9,1,-5,2,-4,10,7,3,2,-3,3,2,-2,6,6,-7,-2,-2,-9,-3,-5,6,3,-5,-1,9,-6,8,7,10,-7,-10,-5,8,-5,9,-1,1,-4,-2,7,-3,-2,1,-4,5,-9,-2,7,10,-8,3,-6,7,3,9,9,-2,-2,4,-5,-9,4,-1,-1,5,4,1,4,-1,7,8,-3,-9,-5,-5,2,7,5,-8,-10,6,-3,-3,-6,8,8,9,8,8,-3,-6,-7,2,10,10,5,2,-4,-6,1,4,-10,3,-5,1,-6,-4,9,-6,-7,9,-2,-9,9,-9,-9,-2,-9,9,5,-1,-9,3,2,9,6,1,-10,-6,-8,-1,-1,-6,-7,-4,6,-1,-2,-5,4,4,-1,-9,5,-3,-4,10,7,-6,2,5,7,5,2,6,5,7,-6,8,-4,6,5,-3,-3,-7,9,7,9,9,-3,7,-6,-3,-3,-6,3,-4,8,-3,8,-10,-5,5,8,-5,-1,-8,-9,1,-1,8,1,-6,-9,1,-10,-6,-7,-9,7,5,-10,-6,3,10,6,-10,10,-5,-5,-8,-9,-2,-5,1,-6,-7,9,-5,1,-6,3,-4,-2,-2,7,-3,-4,5,5,9,-4,10,-2,-8,2,9,-2,8,4,-2,-2,1,2,-3,-4,10,1,-3,-9,-5,7,-8,-9,-4,8,5,-2,6,-4,1,-3,6,-5,4,-2,-4,-5,1,-1,-8,-2,9,-1,8,-5,-3,-1,10,-2,9,7,4,-8,-7,-9,-5,10,-4,8,8,2,2,2,1,-10,7,-6,9,-7,2,-1,-8,-3,-4,6,-6,3,6,-2,9,-9,-9,-9,-10,5,4,-9,9,-5,-4,-4,3,-8,3,6,-10,-10,2,7,6,2,-10,-2,-4,3,-10,-6,-6,-10,4,3,-2,5,2,6,6,10,10,6,-1,-9,7,1,-10,6,-8,-10,-4,6,6,6,1,-7,-9,4,3,-10,1,-8,4,-6,3,-7,-8,-4,7,4,7,-1,-6,8], dtype = "int64")#candidate|10256|(540,)|const|int64
var_10257 = relay.var("var_10257", dtype = "float64", shape = (1280,))#candidate|10257|(1280,)|var|float64
call_10255 = relay.TupleGetItem(func_8419_call(relay.reshape(const_10256.astype('int64'), [540,]), relay.reshape(var_10257.astype('float64'), [1280,]), ), 2)
call_10258 = relay.TupleGetItem(func_8422_call(relay.reshape(const_10256.astype('int64'), [540,]), relay.reshape(var_10257.astype('float64'), [1280,]), ), 2)
output = relay.Tuple([call_10192,call_10194,const_10195,call_10209,call_10238,const_10239,var_10240,call_10242,call_10250,const_10251,call_10255,const_10256,var_10257,])
output2 = relay.Tuple([call_10193,call_10196,const_10195,call_10210,call_10241,const_10239,var_10240,call_10243,call_10252,const_10251,call_10258,const_10256,var_10257,])
func_10259 = relay.Function([var_10240,var_10257,], output)
mod['func_10259'] = func_10259
mod = relay.transform.InferType()(mod)
var_10260 = relay.var("var_10260", dtype = "float64", shape = (65,))#candidate|10260|(65,)|var|float64
var_10261 = relay.var("var_10261", dtype = "float64", shape = (1280,))#candidate|10261|(1280,)|var|float64
output = func_10259(var_10260,var_10261,)
func_10262 = relay.Function([var_10260,var_10261,], output)
mutated_mod['func_10262'] = func_10262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8296_call = mod.get_global_var('func_8296')
func_8298_call = mutated_mod.get_global_var('func_8298')
call_10275 = func_8296_call()
call_10276 = func_8296_call()
uop_10296 = relay.sin(call_10275.astype('float32')) # shape=(3, 7, 7)
uop_10298 = relay.sin(call_10276.astype('float32')) # shape=(3, 7, 7)
func_9549_call = mod.get_global_var('func_9549')
func_9550_call = mutated_mod.get_global_var('func_9550')
call_10303 = relay.TupleGetItem(func_9549_call(), 0)
call_10304 = relay.TupleGetItem(func_9550_call(), 0)
output = relay.Tuple([uop_10296,call_10303,])
output2 = relay.Tuple([uop_10298,call_10304,])
func_10330 = relay.Function([], output)
mod['func_10330'] = func_10330
mod = relay.transform.InferType()(mod)
mutated_mod['func_10330'] = func_10330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10330_call = mutated_mod.get_global_var('func_10330')
call_10331 = func_10330_call()
output = call_10331
func_10332 = relay.Function([], output)
mutated_mod['func_10332'] = func_10332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8782_call = mod.get_global_var('func_8782')
func_8783_call = mutated_mod.get_global_var('func_8783')
call_10336 = relay.TupleGetItem(func_8782_call(), 0)
call_10337 = relay.TupleGetItem(func_8783_call(), 0)
uop_10355 = relay.sigmoid(call_10336.astype('float32')) # shape=(550,)
uop_10357 = relay.sigmoid(call_10337.astype('float32')) # shape=(550,)
output = uop_10355
output2 = uop_10357
func_10383 = relay.Function([], output)
mod['func_10383'] = func_10383
mod = relay.transform.InferType()(mod)
output = func_10383()
func_10384 = relay.Function([], output)
mutated_mod['func_10384'] = func_10384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_10413 = func_7344_call()
call_10414 = func_7344_call()
func_9439_call = mod.get_global_var('func_9439')
func_9442_call = mutated_mod.get_global_var('func_9442')
var_10427 = relay.var("var_10427", dtype = "float32", shape = (48,))#candidate|10427|(48,)|var|float32
call_10426 = func_9439_call(relay.reshape(var_10427.astype('float32'), [16, 1, 3]))
call_10428 = func_9439_call(relay.reshape(var_10427.astype('float32'), [16, 1, 3]))
bop_10440 = relay.right_shift(call_10426.astype('int64'), relay.reshape(var_10427.astype('int64'), relay.shape_of(call_10426))) # shape=(16, 1, 3)
bop_10443 = relay.right_shift(call_10428.astype('int64'), relay.reshape(var_10427.astype('int64'), relay.shape_of(call_10428))) # shape=(16, 1, 3)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_10455 = relay.TupleGetItem(func_7653_call(), 0)
call_10456 = relay.TupleGetItem(func_7654_call(), 0)
func_6804_call = mod.get_global_var('func_6804')
func_6806_call = mutated_mod.get_global_var('func_6806')
const_10458 = relay.const(7, dtype = "int64")#candidate|10458|()|const|int64
call_10457 = relay.TupleGetItem(func_6804_call(relay.reshape(const_10458.astype('int64'), [])), 2)
call_10459 = relay.TupleGetItem(func_6806_call(relay.reshape(const_10458.astype('int64'), [])), 2)
bop_10476 = relay.bitwise_or(call_10426.astype('int16'), relay.reshape(var_10427.astype('int16'), relay.shape_of(call_10426))) # shape=(16, 1, 3)
bop_10479 = relay.bitwise_or(call_10428.astype('int16'), relay.reshape(var_10427.astype('int16'), relay.shape_of(call_10428))) # shape=(16, 1, 3)
output = relay.Tuple([call_10413,bop_10440,call_10455,call_10457,const_10458,bop_10476,])
output2 = relay.Tuple([call_10414,bop_10443,call_10456,call_10459,const_10458,bop_10479,])
func_10483 = relay.Function([var_10427,], output)
mod['func_10483'] = func_10483
mod = relay.transform.InferType()(mod)
mutated_mod['func_10483'] = func_10483
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10484 = relay.var("var_10484", dtype = "float32", shape = (48,))#candidate|10484|(48,)|var|float32
func_10483_call = mutated_mod.get_global_var('func_10483')
call_10485 = func_10483_call(var_10484)
output = call_10485
func_10486 = relay.Function([var_10484], output)
mutated_mod['func_10486'] = func_10486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9637_call = mod.get_global_var('func_9637')
func_9639_call = mutated_mod.get_global_var('func_9639')
call_10488 = func_9637_call()
call_10489 = func_9637_call()
output = relay.Tuple([call_10488,])
output2 = relay.Tuple([call_10489,])
func_10490 = relay.Function([], output)
mod['func_10490'] = func_10490
mod = relay.transform.InferType()(mod)
mutated_mod['func_10490'] = func_10490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10490_call = mutated_mod.get_global_var('func_10490')
call_10491 = func_10490_call()
output = call_10491
func_10492 = relay.Function([], output)
mutated_mod['func_10492'] = func_10492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_10493 = relay.TupleGetItem(func_6751_call(), 0)
call_10494 = relay.TupleGetItem(func_6753_call(), 0)
func_2495_call = mod.get_global_var('func_2495')
func_2497_call = mutated_mod.get_global_var('func_2497')
const_10501 = relay.const([9.331774,8.454801,7.865017,9.157256,4.473582,8.590716,-5.054774,-1.715341,-4.445512,6.087413,4.640916,-9.977863,5.267519,-0.441814,8.724689,8.069825,0.614950,-9.424067,8.013572,2.783961,1.785643,-6.317720,3.925988,-0.083500,3.240075,-6.182009,4.452214,6.475833,4.136915,3.928249,7.571775,9.361709,-9.981990,3.486266,9.590452,-7.842998,-8.638126,0.881960,5.581158,2.590330,1.722625,-8.651629,-8.189696,1.511770,2.114403,0.945062,1.762285,0.256637,-5.356960,9.759492,2.547634,-7.706647,4.158470,0.898359,6.683895,4.521430,-9.183296,6.785087,1.777640,-3.382453,-8.002681,8.563036,2.428305,3.134915,-9.367838,8.882608,-5.376271,2.058154,1.920247,-8.563074,2.091937,8.844987,4.293915,-5.278384,-3.087394,7.004547,-8.596186,-7.446091,3.188185,2.027260,7.411149,7.238609,-6.060049,5.623113,4.450850,-2.008018,1.320817,-3.856042,8.310156,2.553987,-8.434084,-1.116586,0.505409,-6.395355,-1.102964,-3.973605,-0.073581,1.338255,-2.049739,8.521142,-4.360068,-6.212750,9.829327,8.364404,-6.670269,-7.975819,2.542784,9.749283,-8.960154,-2.503485,-1.099225,-0.340931,-6.208117,0.824475,-0.199086,1.680337,3.366196,-9.019290,-8.242274,8.376766,-0.233560,5.987670,-1.729168,-8.299134,-5.608929,6.413275,-8.442279,-1.741616,2.703196,4.263448,-5.742057,-7.991505,0.043317,-5.328552,-7.198265,-0.285798,-0.663065,8.256147,-3.080533,4.775453,-7.003849,6.322584,-6.539604,7.046479,-4.481542,3.829845,7.168735,-1.711942,-1.673355,2.568202,-9.892404,7.756231,9.884105,0.707638,-1.531774,6.305934,4.350096,5.585617,-8.494823,7.607044,-4.119329,4.166085,-4.216786,-9.513471,-4.759861,-6.594784,9.164970,2.792629,-3.272959,-7.882150,2.454562,0.448430,2.509143,-7.340287,9.534547,-7.916398,-8.842623,-1.214235,3.107115,2.049491,-9.654220,-8.273775,0.830407,-4.890746,-8.163503,1.590409,-4.783822,-4.387294,4.977240,1.333965,-0.091934,-2.084640,8.667873,3.174002,4.442670,0.221350,-0.705096,7.670684,7.463659,7.846187,8.116488,-7.722777,9.360991,4.103822,1.718773,-0.824528,-9.514526,0.813764,2.606178,-7.711859,6.477093,-3.048947,4.631424,-8.287700,7.900174,-0.187473,-9.592700,6.310025,4.753087,-8.102096,5.665091,-1.830077,-1.748757,-1.085111,-4.999190,-7.397817,-6.874564,-7.623110,0.318116,-8.103378,-6.745163,0.220418,1.055050,6.502641,2.338569,-8.439012,-2.876182,-8.254566,-8.935979,-4.171655], dtype = "float64")#candidate|10501|(240,)|const|float64
call_10500 = func_2495_call(relay.reshape(const_10501.astype('float64'), [2, 12, 10]))
call_10502 = func_2495_call(relay.reshape(const_10501.astype('float64'), [2, 12, 10]))
bop_10507 = relay.logical_xor(call_10500.astype('uint8'), relay.reshape(const_10501.astype('uint8'), relay.shape_of(call_10500))) # shape=(2, 12, 10)
bop_10510 = relay.logical_xor(call_10502.astype('uint8'), relay.reshape(const_10501.astype('uint8'), relay.shape_of(call_10502))) # shape=(2, 12, 10)
output = relay.Tuple([call_10493,bop_10507,])
output2 = relay.Tuple([call_10494,bop_10510,])
func_10515 = relay.Function([], output)
mod['func_10515'] = func_10515
mod = relay.transform.InferType()(mod)
mutated_mod['func_10515'] = func_10515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10515_call = mutated_mod.get_global_var('func_10515')
call_10516 = func_10515_call()
output = call_10516
func_10517 = relay.Function([], output)
mutated_mod['func_10517'] = func_10517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10541 = relay.var("var_10541", dtype = "float64", shape = (11, 16, 14))#candidate|10541|(11, 16, 14)|var|float64
var_10542 = relay.var("var_10542", dtype = "float64", shape = (11, 16, 14))#candidate|10542|(11, 16, 14)|var|float64
bop_10543 = relay.floor_mod(var_10541.astype('float64'), relay.reshape(var_10542.astype('float64'), relay.shape_of(var_10541))) # shape=(11, 16, 14)
func_9182_call = mod.get_global_var('func_9182')
func_9185_call = mutated_mod.get_global_var('func_9185')
const_10571 = relay.const([False,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,True,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,True,False], dtype = "bool")#candidate|10571|(1008,)|const|bool
var_10572 = relay.var("var_10572", dtype = "uint64", shape = (256,))#candidate|10572|(256,)|var|uint64
call_10570 = relay.TupleGetItem(func_9182_call(relay.reshape(const_10571.astype('bool'), [1008,]), relay.reshape(var_10572.astype('uint64'), [256,]), ), 1)
call_10573 = relay.TupleGetItem(func_9185_call(relay.reshape(const_10571.astype('bool'), [1008,]), relay.reshape(var_10572.astype('uint64'), [256,]), ), 1)
output = relay.Tuple([bop_10543,call_10570,const_10571,var_10572,])
output2 = relay.Tuple([bop_10543,call_10573,const_10571,var_10572,])
func_10577 = relay.Function([var_10541,var_10542,var_10572,], output)
mod['func_10577'] = func_10577
mod = relay.transform.InferType()(mod)
mutated_mod['func_10577'] = func_10577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10577_call = mutated_mod.get_global_var('func_10577')
var_10579 = relay.var("var_10579", dtype = "float64", shape = (11, 16, 14))#candidate|10579|(11, 16, 14)|var|float64
var_10580 = relay.var("var_10580", dtype = "float64", shape = (11, 16, 14))#candidate|10580|(11, 16, 14)|var|float64
var_10581 = relay.var("var_10581", dtype = "uint64", shape = (256,))#candidate|10581|(256,)|var|uint64
call_10578 = func_10577_call(var_10579,var_10580,var_10581,)
output = call_10578
func_10582 = relay.Function([var_10579,var_10580,var_10581,], output)
mutated_mod['func_10582'] = func_10582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10020_call = mod.get_global_var('func_10020')
func_10022_call = mutated_mod.get_global_var('func_10022')
call_10628 = func_10020_call()
call_10629 = func_10020_call()
output = call_10628
output2 = call_10629
func_10653 = relay.Function([], output)
mod['func_10653'] = func_10653
mod = relay.transform.InferType()(mod)
output = func_10653()
func_10654 = relay.Function([], output)
mutated_mod['func_10654'] = func_10654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mod.get_global_var('func_8553')
func_8555_call = mutated_mod.get_global_var('func_8555')
call_10683 = relay.TupleGetItem(func_8553_call(), 0)
call_10684 = relay.TupleGetItem(func_8555_call(), 0)
output = relay.Tuple([call_10683,])
output2 = relay.Tuple([call_10684,])
func_10687 = relay.Function([], output)
mod['func_10687'] = func_10687
mod = relay.transform.InferType()(mod)
mutated_mod['func_10687'] = func_10687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10687_call = mutated_mod.get_global_var('func_10687')
call_10688 = func_10687_call()
output = call_10688
func_10689 = relay.Function([], output)
mutated_mod['func_10689'] = func_10689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_10877 = func_7106_call()
call_10878 = func_7106_call()
output = relay.Tuple([call_10877,])
output2 = relay.Tuple([call_10878,])
func_10909 = relay.Function([], output)
mod['func_10909'] = func_10909
mod = relay.transform.InferType()(mod)
mutated_mod['func_10909'] = func_10909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10909_call = mutated_mod.get_global_var('func_10909')
call_10910 = func_10909_call()
output = call_10910
func_10911 = relay.Function([], output)
mutated_mod['func_10911'] = func_10911
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10975 = relay.var("var_10975", dtype = "float32", shape = (16, 9, 15))#candidate|10975|(16, 9, 15)|var|float32
uop_10976 = relay.asin(var_10975.astype('float32')) # shape=(16, 9, 15)
output = uop_10976
output2 = uop_10976
func_10987 = relay.Function([var_10975,], output)
mod['func_10987'] = func_10987
mod = relay.transform.InferType()(mod)
mutated_mod['func_10987'] = func_10987
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10988 = relay.var("var_10988", dtype = "float32", shape = (16, 9, 15))#candidate|10988|(16, 9, 15)|var|float32
func_10987_call = mutated_mod.get_global_var('func_10987')
call_10989 = func_10987_call(var_10988)
output = call_10989
func_10990 = relay.Function([var_10988], output)
mutated_mod['func_10990'] = func_10990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_11023 = relay.TupleGetItem(func_7952_call(), 2)
call_11024 = relay.TupleGetItem(func_7954_call(), 2)
func_9439_call = mod.get_global_var('func_9439')
func_9442_call = mutated_mod.get_global_var('func_9442')
var_11069 = relay.var("var_11069", dtype = "float32", shape = (48,))#candidate|11069|(48,)|var|float32
call_11068 = func_9439_call(relay.reshape(var_11069.astype('float32'), [16, 1, 3]))
call_11070 = func_9439_call(relay.reshape(var_11069.astype('float32'), [16, 1, 3]))
output = relay.Tuple([call_11023,call_11068,var_11069,])
output2 = relay.Tuple([call_11024,call_11070,var_11069,])
func_11083 = relay.Function([var_11069,], output)
mod['func_11083'] = func_11083
mod = relay.transform.InferType()(mod)
mutated_mod['func_11083'] = func_11083
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11084 = relay.var("var_11084", dtype = "float32", shape = (48,))#candidate|11084|(48,)|var|float32
func_11083_call = mutated_mod.get_global_var('func_11083')
call_11085 = func_11083_call(var_11084)
output = call_11085
func_11086 = relay.Function([var_11084], output)
mutated_mod['func_11086'] = func_11086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10687_call = mod.get_global_var('func_10687')
func_10689_call = mutated_mod.get_global_var('func_10689')
call_11175 = relay.TupleGetItem(func_10687_call(), 0)
call_11176 = relay.TupleGetItem(func_10689_call(), 0)
output = relay.Tuple([call_11175,])
output2 = relay.Tuple([call_11176,])
func_11190 = relay.Function([], output)
mod['func_11190'] = func_11190
mod = relay.transform.InferType()(mod)
output = func_11190()
func_11191 = relay.Function([], output)
mutated_mod['func_11191'] = func_11191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8212_call = mod.get_global_var('func_8212')
func_8214_call = mutated_mod.get_global_var('func_8214')
call_11268 = relay.TupleGetItem(func_8212_call(), 2)
call_11269 = relay.TupleGetItem(func_8214_call(), 2)
func_8553_call = mod.get_global_var('func_8553')
func_8555_call = mutated_mod.get_global_var('func_8555')
call_11285 = relay.TupleGetItem(func_8553_call(), 0)
call_11286 = relay.TupleGetItem(func_8555_call(), 0)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
const_11290 = relay.const([[-8,-4,-8,9,9,-3,-5,7,-3,6,-9,1,-6,-8,4,9,-8,-10,8,-10,1,2,-6,-2,1,4,-8,3,5,9,9,1,3,-6,3,7,-9,-7,-9,-3,8,-2,2,2,-7,7,1,5,-9,4,-9,3,-10,-1,1,1,1,8,9,1,1,5,-5,-5,-3,8,1,-10,-4,-4,-6,6,8,-3,4,-4,3,6,-10,-4,-3,7,-4,7,-7,-4,-5,2,-2,10,-8,-10,4,9,-10,-8,-5,-7,1,8,-4,-3,-3,-2,-10,1,-9,-9,1,-8,2,4,-1,8,-4,10,-1,8,-7,-8,-3,5,2,-4,3,-3,-9,2,-7,-2,1,2,-4,-5,-9,8,-2,5,-6,-6,-2,-3,6,-3,-10,-8,8,2,-8,-4,7,-10,-6,4,5,-2,1,-10,-3,-3,-5,-3,-9,-6,1,4,2,9,-1,10,5,3,-7,6,-3,2,-8,-2,1,3,-7,-2,-3,9,-5,7,2,7,-2,-1,2,4,10,8,-5,-5,-8,-3,7,-2,-2,-2,9,-4,-4,8,8,-5,-10,-2,-4,9,-4,-2,6,-3,4,-3,-9,-6,1,9,5,-10,9,-2,-8,6,5,3,1,-10,-3,8,9,5,7,1,-9,7,-2,-10,9,-2,-3,6,3,9,-10,-10,-2,-10,8,-8,-2,-5,-5,-5,-3,1,-4,-10,-4,4,9,-4,8,7,-5,5,2,-2,-6,-3,5,-3,-2,7,5,1],[-7,4,-7,3,7,-9,-7,8,-7,-2,-5,-5,-9,5,6,-9,-9,2,3,-9,-5,-9,-9,-6,8,-1,5,9,8,8,-10,-9,-10,-6,-6,3,-3,-4,9,-9,1,9,-5,8,2,7,4,10,7,-9,5,4,6,10,-1,-2,10,6,2,9,3,6,10,-3,6,-1,4,8,-5,-5,1,1,-3,-7,3,8,9,-5,-4,9,-10,2,6,-6,-10,9,10,-3,7,7,5,7,-3,-7,1,-8,4,7,-8,1,3,1,2,-8,3,10,-3,4,-7,1,-4,-9,9,-8,-10,-6,3,-8,-9,-5,-4,-2,1,-10,-6,-6,-2,-9,-2,7,-10,-5,-10,7,3,-4,6,-1,2,3,6,10,-6,-6,-8,10,-8,10,-2,-7,-8,10,-7,-8,4,-8,-3,-8,-9,-9,9,-4,8,5,10,3,-3,1,5,10,3,2,8,6,6,4,-7,-4,-4,-3,1,2,10,-5,-3,8,6,-9,-2,4,2,-5,8,-4,-10,-7,-4,6,-2,-10,-7,8,-8,10,4,10,-3,5,-6,-4,-5,-9,9,2,6,6,-2,-9,-3,-2,2,-3,7,-6,8,-9,-2,1,-4,5,-6,-5,5,-1,-2,7,5,1,-9,-6,7,-7,4,10,-2,-7,-8,-9,8,-3,-2,-8,-8,10,-6,-4,2,3,1,3,10,4,-6,-1,10,7,-2,-9,-2,10,5,-2,-5,-4,-8,-2,1,-4,-6,1]], dtype = "uint64")#candidate|11290|(2, 280)|const|uint64
call_11289 = relay.TupleGetItem(func_3471_call(relay.reshape(const_11290.astype('uint64'), [10, 7, 8])), 0)
call_11291 = relay.TupleGetItem(func_3473_call(relay.reshape(const_11290.astype('uint64'), [10, 7, 8])), 0)
output = relay.Tuple([call_11268,call_11285,call_11289,const_11290,])
output2 = relay.Tuple([call_11269,call_11286,call_11291,const_11290,])
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
func_9320_call = mod.get_global_var('func_9320')
func_9321_call = mutated_mod.get_global_var('func_9321')
call_11331 = relay.TupleGetItem(func_9320_call(), 0)
call_11332 = relay.TupleGetItem(func_9321_call(), 0)
output = call_11331
output2 = call_11332
func_11336 = relay.Function([], output)
mod['func_11336'] = func_11336
mod = relay.transform.InferType()(mod)
output = func_11336()
func_11337 = relay.Function([], output)
mutated_mod['func_11337'] = func_11337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8192_call = mod.get_global_var('func_8192')
func_8194_call = mutated_mod.get_global_var('func_8194')
call_11347 = relay.TupleGetItem(func_8192_call(), 2)
call_11348 = relay.TupleGetItem(func_8194_call(), 2)
output = relay.Tuple([call_11347,])
output2 = relay.Tuple([call_11348,])
func_11351 = relay.Function([], output)
mod['func_11351'] = func_11351
mod = relay.transform.InferType()(mod)
output = func_11351()
func_11352 = relay.Function([], output)
mutated_mod['func_11352'] = func_11352
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11379 = relay.var("var_11379", dtype = "float64", shape = (4, 10, 13))#candidate|11379|(4, 10, 13)|var|float64
var_11380 = relay.var("var_11380", dtype = "float64", shape = (4, 10, 13))#candidate|11380|(4, 10, 13)|var|float64
bop_11381 = relay.greater_equal(var_11379.astype('bool'), relay.reshape(var_11380.astype('bool'), relay.shape_of(var_11379))) # shape=(4, 10, 13)
func_7260_call = mod.get_global_var('func_7260')
func_7262_call = mutated_mod.get_global_var('func_7262')
var_11394 = relay.var("var_11394", dtype = "float64", shape = (147,))#candidate|11394|(147,)|var|float64
call_11393 = relay.TupleGetItem(func_7260_call(relay.reshape(var_11394.astype('float64'), [3, 7, 7])), 0)
call_11395 = relay.TupleGetItem(func_7262_call(relay.reshape(var_11394.astype('float64'), [3, 7, 7])), 0)
func_1996_call = mod.get_global_var('func_1996')
func_2000_call = mutated_mod.get_global_var('func_2000')
var_11398 = relay.var("var_11398", dtype = "int64", shape = (540,))#candidate|11398|(540,)|var|int64
var_11399 = relay.var("var_11399", dtype = "float64", shape = (1280,))#candidate|11399|(1280,)|var|float64
var_11400 = relay.var("var_11400", dtype = "uint64", shape = (60,))#candidate|11400|(60,)|var|uint64
call_11397 = relay.TupleGetItem(func_1996_call(relay.reshape(var_11398.astype('int64'), [6, 9, 10]), relay.reshape(var_11399.astype('float64'), [1280,]), relay.reshape(var_11400.astype('uint64'), [60,]), ), 1)
call_11401 = relay.TupleGetItem(func_2000_call(relay.reshape(var_11398.astype('int64'), [6, 9, 10]), relay.reshape(var_11399.astype('float64'), [1280,]), relay.reshape(var_11400.astype('uint64'), [60,]), ), 1)
func_1996_call = mod.get_global_var('func_1996')
func_2000_call = mutated_mod.get_global_var('func_2000')
call_11405 = relay.TupleGetItem(func_1996_call(relay.reshape(var_11398.astype('int64'), [6, 9, 10]), relay.reshape(var_11399.astype('float64'), [1280,]), relay.reshape(var_11400.astype('uint64'), [60,]), ), 2)
call_11406 = relay.TupleGetItem(func_2000_call(relay.reshape(var_11398.astype('int64'), [6, 9, 10]), relay.reshape(var_11399.astype('float64'), [1280,]), relay.reshape(var_11400.astype('uint64'), [60,]), ), 2)
output = relay.Tuple([bop_11381,call_11393,var_11394,call_11397,var_11398,var_11399,var_11400,call_11405,])
output2 = relay.Tuple([bop_11381,call_11395,var_11394,call_11401,var_11398,var_11399,var_11400,call_11406,])
func_11407 = relay.Function([var_11379,var_11380,var_11394,var_11398,var_11399,var_11400,], output)
mod['func_11407'] = func_11407
mod = relay.transform.InferType()(mod)
var_11408 = relay.var("var_11408", dtype = "float64", shape = (4, 10, 13))#candidate|11408|(4, 10, 13)|var|float64
var_11409 = relay.var("var_11409", dtype = "float64", shape = (4, 10, 13))#candidate|11409|(4, 10, 13)|var|float64
var_11410 = relay.var("var_11410", dtype = "float64", shape = (147,))#candidate|11410|(147,)|var|float64
var_11411 = relay.var("var_11411", dtype = "int64", shape = (540,))#candidate|11411|(540,)|var|int64
var_11412 = relay.var("var_11412", dtype = "float64", shape = (1280,))#candidate|11412|(1280,)|var|float64
var_11413 = relay.var("var_11413", dtype = "uint64", shape = (60,))#candidate|11413|(60,)|var|uint64
output = func_11407(var_11408,var_11409,var_11410,var_11411,var_11412,var_11413,)
func_11414 = relay.Function([var_11408,var_11409,var_11410,var_11411,var_11412,var_11413,], output)
mutated_mod['func_11414'] = func_11414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9665_call = mod.get_global_var('func_9665')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_11416 = relay.TupleGetItem(func_9665_call(), 0)
call_11417 = relay.TupleGetItem(func_9666_call(), 0)
func_8090_call = mod.get_global_var('func_8090')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_11420 = relay.TupleGetItem(func_8090_call(), 0)
call_11421 = relay.TupleGetItem(func_8091_call(), 0)
func_8572_call = mod.get_global_var('func_8572')
func_8574_call = mutated_mod.get_global_var('func_8574')
var_11429 = relay.var("var_11429", dtype = "int16", shape = (1980,))#candidate|11429|(1980,)|var|int16
call_11428 = relay.TupleGetItem(func_8572_call(relay.reshape(var_11429.astype('int16'), [1980,])), 3)
call_11430 = relay.TupleGetItem(func_8574_call(relay.reshape(var_11429.astype('int16'), [1980,])), 3)
output = relay.Tuple([call_11416,call_11420,call_11428,var_11429,])
output2 = relay.Tuple([call_11417,call_11421,call_11430,var_11429,])
func_11447 = relay.Function([var_11429,], output)
mod['func_11447'] = func_11447
mod = relay.transform.InferType()(mod)
var_11448 = relay.var("var_11448", dtype = "int16", shape = (1980,))#candidate|11448|(1980,)|var|int16
output = func_11447(var_11448)
func_11449 = relay.Function([var_11448], output)
mutated_mod['func_11449'] = func_11449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_11468 = func_7344_call()
call_11469 = func_7344_call()
func_6309_call = mod.get_global_var('func_6309')
func_6318_call = mutated_mod.get_global_var('func_6318')
const_11471 = relay.const([[8,-1,-7,-7,7,-9,-3,2,3,-5,8,-8,-8,-6,10,4,-1,-10,-1,5,5,10,9,1,2,9,-9,-6,5,-1,10,-4,2,7,4,-5,10,-4,-9,-10,-2,-8,5,7,-8,6,6,8],[7,3,-9,-8,-4,-5,1,4,6,4,8,3,2,5,-1,-5,-6,10,7,-2,2,3,-7,-7,-9,-6,2,4,-9,1,-9,10,5,3,-10,2,-4,-7,2,-6,5,-7,-1,3,7,4,2,-3],[4,10,1,-5,-7,-8,6,-9,7,-8,-6,-10,6,-10,6,7,9,5,7,9,-2,-2,-2,-9,-6,7,9,4,-9,-4,-8,-6,-6,1,1,-9,6,3,-4,-6,3,-2,-1,8,9,-7,-10,-5],[4,-4,-3,-1,-6,-6,-9,3,-6,-4,9,8,-1,6,8,2,9,-8,-8,-3,3,9,4,6,4,8,2,-3,9,-8,5,8,3,6,4,10,-1,-1,-8,4,7,-9,-7,5,4,-2,1,-2],[-9,10,10,-1,6,5,-1,9,-10,-8,-1,-5,-6,5,-1,4,7,-1,3,-7,6,-4,-10,6,1,9,6,-10,-2,-10,4,-1,7,10,-6,8,9,-10,6,1,9,-1,3,-7,-8,6,-10,-5],[-10,6,3,1,-7,1,6,-3,1,2,-7,8,6,9,2,-3,-10,8,7,5,10,-9,9,5,-8,-3,8,2,5,9,7,8,5,3,7,5,-6,-8,-6,5,10,1,-9,-1,6,10,6,-3],[5,-2,-3,-10,1,6,-10,3,8,7,9,-10,10,10,-7,8,8,4,6,2,1,7,6,-1,-4,-2,8,9,3,7,-2,-3,4,-2,3,-10,-2,8,-6,4,9,4,7,9,-1,-9,-9,3],[-10,-6,9,-9,-2,10,-8,-10,10,6,7,7,-2,-1,1,-6,9,5,-7,-10,1,-7,-4,-6,10,2,-7,-5,7,10,10,-8,8,-10,10,-4,-1,10,9,-10,7,-4,10,5,-7,-5,3,-7],[-9,-7,-6,9,-5,3,-6,1,-4,10,-8,1,-4,-10,10,-9,4,-7,1,10,-7,-8,-7,-8,7,4,5,-9,-10,5,8,-8,-1,5,-2,-8,1,2,8,-10,8,-10,-1,-3,2,2,1,4],[-4,-8,5,5,-3,-5,-7,-7,9,9,10,1,-9,2,3,-5,-5,5,-8,-8,-7,5,-6,-10,-2,6,-10,-6,2,-2,3,1,-10,-10,7,1,-8,8,9,-10,-7,-4,5,-8,7,-9,-5,8],[9,4,-5,9,-1,9,3,10,-8,-6,4,8,-4,-4,9,4,2,-5,-5,10,1,4,1,-5,8,-9,-5,-8,4,-10,5,-3,4,-4,10,2,5,7,-2,4,4,-6,10,10,5,-1,3,-5],[-1,5,3,5,5,-6,2,9,-3,5,-7,9,4,-10,3,-6,-6,-6,-2,9,-2,-4,-2,10,-6,-9,1,-4,-10,-4,2,5,-2,-7,3,2,10,10,1,-9,5,1,-8,1,-3,-10,4,3],[8,2,9,-7,-2,-2,6,-1,9,-9,10,6,-4,8,-2,7,2,-5,3,-9,10,-9,3,9,3,3,-7,-7,-5,-10,8,9,7,1,8,7,3,4,8,-10,-1,-6,-1,-9,8,3,7,5],[8,3,10,-1,6,1,-9,6,-3,8,5,-8,7,10,5,-5,5,-10,8,8,-9,9,-9,9,9,-5,7,1,7,7,9,9,-1,-9,-10,-6,-7,6,2,-7,5,7,-5,5,10,-6,-7,2],[-3,9,-9,10,-10,1,4,-4,8,-10,-2,7,-8,-2,9,2,-7,3,6,2,-2,1,-1,-6,8,3,10,3,-6,-10,9,7,3,-1,-7,-6,-8,-6,3,9,5,-3,-4,2,9,7,4,-3],[-5,-7,-9,-1,1,5,9,-5,-6,1,3,3,7,-10,-3,-9,7,-1,10,-3,-1,-5,2,9,6,-9,-3,-1,-10,3,-5,-2,-10,-1,4,3,2,-8,-8,2,6,3,4,2,-8,-9,-1,9],[3,4,-6,7,-7,-4,-3,-8,-10,10,6,9,-1,7,1,-3,-6,6,-6,-9,9,9,-10,10,-8,3,4,-8,-2,5,10,10,7,-9,-8,-7,4,6,2,3,8,-6,1,7,8,7,-2,-6],[-4,1,3,-8,5,-10,-1,7,-10,2,-6,5,1,-3,-10,1,4,-7,-1,4,2,-10,-9,-4,1,-10,-5,2,8,8,-4,5,10,-7,-6,4,6,-1,-3,6,1,3,-3,-1,-10,-1,7,-4],[-8,5,-3,4,-4,-8,9,5,2,-5,2,-7,6,-1,-4,9,8,-7,-4,-4,-5,-9,6,6,1,2,9,8,-9,-8,5,-6,1,4,4,6,-10,-6,9,6,-5,-3,-10,-2,9,-2,7,-7],[-1,6,1,-7,-8,-1,6,7,6,8,1,4,9,-6,4,-5,-6,-2,-4,10,-5,9,6,5,-5,9,4,-8,9,-7,7,10,2,10,3,8,-1,-1,4,-1,10,5,-5,-7,6,7,-6,5],[-1,4,5,3,-10,4,-2,-10,-7,8,-7,8,7,-5,4,-10,6,-8,7,-8,-6,10,-9,2,-5,-8,3,8,-1,2,-4,10,-10,3,-8,4,-3,-3,5,8,4,-4,4,-7,-4,2,-5,10],[-1,-3,-5,-4,-3,1,-10,10,9,-1,8,9,10,2,4,-3,6,-3,-4,9,3,5,-3,7,1,-4,-9,10,4,7,5,-4,-7,-4,-5,-8,7,10,-8,-1,-9,7,9,7,3,-5,5,1],[-8,5,-10,-10,6,-6,-10,-5,-5,5,2,-9,-8,-3,-4,7,1,-5,-4,-9,-6,-7,5,5,6,4,-4,5,9,-8,-6,7,6,-10,7,-3,6,1,-3,9,-6,1,8,-3,8,2,-4,-1],[2,-3,3,-4,-7,8,9,1,-2,5,-10,9,-8,10,-3,-6,-4,-4,6,-6,10,3,1,5,8,-5,8,6,8,-2,9,-4,7,-2,3,-8,-1,-2,-6,-6,-9,-3,-7,-7,-5,6,4,-8],[7,8,7,-4,-4,1,-7,4,-9,5,6,-3,-8,4,8,-7,-4,-8,8,1,10,3,10,5,6,7,1,-2,8,5,2,10,6,8,10,7,1,9,-9,5,6,9,2,8,-9,-6,2,6],[-4,3,2,-5,-2,-8,-1,-8,5,-4,-9,8,3,9,-8,7,-7,-7,8,6,8,-1,-7,6,6,-10,2,5,10,5,6,1,10,-2,9,8,-2,-6,10,10,2,3,5,-9,9,-2,-4,8],[-10,4,-10,7,-3,-10,3,-1,1,-8,3,1,1,-8,-8,-1,-1,-10,-7,-3,-9,3,7,8,-9,2,4,-3,9,-2,-10,-7,-7,-1,3,-5,9,4,-4,-3,9,-7,1,9,-3,-8,3,-3],[-4,7,10,-10,1,-6,8,-10,-5,1,-6,7,-1,-4,2,-7,2,4,5,1,-7,3,-6,-2,9,-8,-4,-6,-2,9,8,10,1,1,7,-4,-9,-10,9,6,5,-2,-9,-4,-9,-4,-1,6],[-2,10,7,6,10,-2,9,-6,2,-5,-8,-1,-4,-1,-1,6,4,-3,-9,-8,6,-5,-8,1,-1,-8,-5,-4,-5,-3,4,10,-5,-10,3,-3,-7,-5,-9,4,3,9,-2,9,9,-4,3,-2],[10,-3,1,-3,4,5,4,-5,3,7,6,3,-9,-2,-2,1,8,6,-9,10,-6,-9,4,9,8,3,3,-1,2,7,10,7,-1,1,-1,-3,6,9,-4,9,6,5,-7,-4,-4,6,-8,-3],[-5,8,5,-3,3,-3,10,-10,4,-8,4,2,4,1,9,8,10,2,-9,-8,-8,-9,3,-7,-5,-7,-6,8,-7,1,-6,-1,-6,4,7,6,-3,6,-6,-4,-7,-1,-2,-2,-9,6,-3,-2],[2,-2,7,6,5,-9,-2,-2,-6,1,-4,-8,7,8,2,7,-7,-3,-9,6,9,-6,8,10,-3,-1,-6,-1,2,-3,1,-8,-10,-3,-10,-6,-4,-1,-10,-6,4,3,-6,-2,-6,-3,-4,-7],[4,5,1,-4,-2,7,8,9,9,-1,-6,5,10,1,1,-8,8,-8,5,-3,-8,10,-2,-7,1,-7,-5,-9,10,-8,-7,-5,-10,-3,-6,-1,-7,-2,10,-1,1,9,2,-8,-9,-3,-3,-1],[-3,7,3,6,10,8,-9,-2,8,-6,-1,-3,3,5,4,10,-4,-9,-6,6,4,8,4,-6,3,-5,8,-5,3,8,7,7,4,8,-2,6,10,-3,-5,-9,3,-5,9,2,1,1,6,1],[5,-10,4,5,1,8,-9,8,-8,-10,2,-1,4,3,10,-1,-3,-2,-8,-1,-6,-9,-8,4,-10,5,8,7,7,-1,-3,-2,3,3,10,4,-5,-1,-10,8,-1,3,10,1,-9,-6,5,9],[9,-3,6,-5,10,3,-10,9,-6,1,4,5,6,-8,-7,-3,10,7,1,8,-9,1,-4,3,7,-7,-7,6,2,-4,-2,-9,-1,10,-2,5,-9,-3,1,4,1,10,-2,9,4,-6,10,-1],[-2,7,7,-7,2,-1,7,2,-7,-4,-1,-4,8,-1,3,-3,3,1,4,8,10,-1,-7,5,-5,2,3,3,5,-4,-8,-7,9,-10,-8,8,-10,-4,-4,-2,9,-7,1,6,5,-6,6,-1],[3,-7,10,10,-6,8,3,-9,3,5,-7,1,2,3,3,3,7,-9,-7,8,3,-5,3,1,1,1,-8,8,-10,-9,6,10,-4,-10,-10,-6,4,1,5,-5,-9,-4,9,-8,4,-5,-9,-6],[6,8,4,-10,7,-6,-5,-1,-7,1,7,-6,-7,3,-6,3,-5,-1,-4,5,-4,4,-2,-4,-9,7,-8,-9,6,3,3,5,6,6,6,-1,-4,2,1,-7,2,-6,-8,5,9,7,5,-9],[-9,3,8,-8,3,10,-5,-2,-2,-7,-3,6,2,3,7,-10,-7,-4,9,9,1,5,10,-2,8,-5,-4,3,6,5,8,-10,10,-1,-5,2,2,9,-5,-4,-4,3,10,6,-4,9,-10,-6],[-2,-1,7,-10,-1,9,-4,8,-2,6,9,-9,-4,-4,9,7,6,8,-1,2,-1,-7,-6,3,-6,-1,10,7,-2,10,-10,3,-5,9,3,-8,-2,1,10,5,10,2,-10,8,9,-3,7,6],[9,7,-5,-10,8,5,3,3,-8,7,-3,9,-3,2,8,-9,3,3,-1,-5,2,6,-9,-1,1,6,3,7,-10,3,8,7,9,7,4,-8,3,-4,-2,-1,2,-8,-5,-8,-5,2,-6,3],[10,-7,4,-1,-9,9,-9,-6,-10,-6,1,-9,-9,-8,-2,2,2,8,-5,3,3,7,4,5,-8,-10,-6,-3,-4,2,3,9,3,1,8,4,-10,5,4,10,2,-1,3,-5,-7,2,-1,7],[-10,-4,4,2,-8,-8,7,-4,-9,7,-9,6,9,7,-3,-8,3,-3,-1,-1,-10,-3,8,-5,-2,-7,-7,8,3,8,2,-8,9,3,4,10,4,4,1,-7,4,-6,8,-6,1,-6,-1,7]], dtype = "uint32")#candidate|11471|(44, 48)|const|uint32
var_11472 = relay.var("var_11472", dtype = "int32", shape = (21,))#candidate|11472|(21,)|var|int32
const_11473 = relay.const([[-8,9,10,-3],[-4,10,-7,4],[-9,1,-10,-10],[6,9,7,-3],[4,7,1,-1],[-7,3,-9,-9],[-3,-2,5,-10],[-7,8,-4,9],[10,-2,-3,6],[-3,-4,-9,9],[-5,5,-2,-1],[-5,2,-10,7],[-6,3,-3,-9],[-9,9,10,-9],[10,5,10,2]], dtype = "uint64")#candidate|11473|(15, 4)|const|uint64
var_11474 = relay.var("var_11474", dtype = "int64", shape = (540,))#candidate|11474|(540,)|var|int64
const_11475 = relay.const([2.654143,1.476106,-0.077258,-7.099655,8.136218,-2.860903,-6.765652,9.178311,5.683279,3.955144,-1.061843,7.690316,-7.044958,-4.094812,6.724782,4.015117,-7.472683,5.622916,4.001693,2.582536,-3.211488,7.969389,7.967452,0.354133,7.206418,-6.741040,5.932331,-2.088539,1.181150,4.100504,6.815475,3.956576,-6.613023,-5.256444,-5.768015,-1.845587,0.480133,-1.433801,-2.798552,0.635866,-9.566476,-2.687058,6.614698,6.025691,7.668732,8.991307,-9.342444,3.480426,7.730739,-5.187812,0.874858,-0.615211,-9.934353,-0.595339,9.928936,-9.556109,3.961750,8.346297,7.972232,8.167655,-3.269465,7.769937,4.902656,1.053001,-1.880137,2.591618,-5.155083,-0.216815,-5.585752,3.354473,-1.837909,3.675485,-1.508926,-9.987068,4.316586,5.058088,-4.359302,-9.919122,9.702759,8.166917,6.518132,3.513715,-4.687813,-2.229433,-1.367740,-4.334847,1.086061,2.593116,8.304284,-1.831387,4.356310,-2.565942,-9.753471,-1.750472,-8.019367,-8.506144,-9.840132,8.014867,3.853996,5.293490,0.283846,8.851342,7.213035,5.329048,-9.947825,9.388986,4.378642,-9.094205,7.420931,5.522611,-2.920243,9.694551,9.587843,1.980101,9.714650,9.239357,8.062193,9.098269,4.650098,6.539067,-2.100121,4.012438,-3.258564,-9.932602,-4.023347,8.193408,5.463677,3.472710,7.129253,4.644121,3.493799,1.592216,4.794602,9.266383,0.303412,1.098166,-8.361880,0.266655,-4.201933,-7.690656,2.851202,0.342071,-5.666418,-2.367558,1.269284,-9.446561,-0.037725,0.584842,0.220377,-8.055145,2.649121,-7.360295,-0.246193,-4.842022,4.296501,-7.388128,-2.377186,8.872502,-6.395678,-3.307820,-2.929702,5.108849,9.735044,-4.252940,7.879828,1.432439,-2.575542,-0.542967,-3.936313,5.381032,4.928538,-3.505431,5.288651,4.793216,0.186493,-2.590123,-7.435887,-4.075391,-1.359305,-3.716224,3.747628,4.989239,-1.997564,7.673652,-5.762748,-1.395010,-8.590511,-7.988743,0.695393,1.033105,5.564614,-7.437207,3.841653,4.694048,4.081075,-3.707237,-3.297835,3.318119,1.263186,3.927999,1.846797,-2.438563,-2.861836,-4.498126,-6.354023,3.773237,1.972201,4.810686,-5.527885,-0.858951,8.790407,4.628313,-0.259998,-6.316888,6.684244,-2.562638,0.394360,-1.353876,6.533322,1.211239,-2.361422,7.905394,-6.127362,8.683808,-6.335077,4.980636,-8.278212,3.251219,3.883221,-2.084790,7.495914,9.312833,6.763523,-9.376416,-1.654722,-7.785828,-7.104609,-7.983308,2.594650,-8.326499,-8.224944,9.447341,-2.298521,4.875680,-7.985564,-8.532842,-9.316561,-0.770252,6.345925,-2.909929,5.376931,-3.139701,0.327469,-4.036283,-8.012785,-5.277315,-2.506189,7.154034,-6.514381,-1.813439,9.269821,-5.583772,4.955920,5.262666,6.251254,-8.062864,1.815972,4.454718,-5.038507,3.049347,-9.122699,8.796410,6.220794,3.772654,8.820771,-3.223817,-3.205071,7.705111,0.899809,-5.106428,-9.162983,0.308832,2.266905,-4.288612,7.757342,8.897719,2.827082,-0.702604,5.320643,-1.346613,-8.964139,0.474264,3.819488,-8.150359,-7.425779,-8.341691,4.430715,-2.937017,-0.168522,-6.485843,-2.837250,6.906986,-5.451789,-4.621337,2.584220,9.705275,2.336989,-7.408129,0.346122,2.676834,4.476330,-6.150390,-7.611140,9.593804,-5.737953,-4.579067,5.202385,-7.891299,6.777134,-1.084550,-7.326824,-4.593727,-1.571262,-8.758305,5.957662,7.020642,2.618391,-4.243268,-6.641950,-0.128312,2.944463,0.640372,-4.232761,2.545081,-5.509171,-5.491728,2.701667,-9.412881,4.959041,5.655913,1.772893,3.541355,-1.867572,-6.057505,-5.889847,2.839733,4.858918,-7.177388,4.558707,2.949295,4.444426,-3.778116,0.164192,4.252043,3.974959,6.745040,7.295590,-8.499898,-4.679955,0.647060,3.303452,8.634830,8.988286,8.481217,3.266784,2.723176,-7.848190,5.110200,-5.745688,0.791443,5.091756,-4.617421,2.346353,-5.664841,1.188134,-6.663977,9.438072,3.655297,-3.940738,4.813020,-8.311644,-0.405563,-1.350393,-8.091757,-8.956332,-4.411090,-6.068904,6.469742,7.221815,-1.171909,4.077122,-2.134289,-5.876526,0.479165,-8.348177,-9.047421,4.947115,3.821453,-6.834617,3.709264,0.643730,-9.851135,-0.419347,-7.892003,4.439513,8.532124,8.998719,3.811167,3.160959,-9.687489,1.935605,-4.713948,-6.777373,-2.626958,0.345731,5.273349,-5.239439,4.862437,4.449304,-0.417078,-9.636663,4.468961,4.779625,0.342275,-9.059779,-0.331536,-6.479375,-7.708796,7.086845,8.404973,-3.462972,5.991162,-0.796099,-7.802443,-4.579503,-1.418743,-9.861178,9.797553,2.229574,-5.631993,-7.535127,3.719815,-0.165894,0.045956,0.613203,-9.240006,-3.391073,-4.102679,-3.225665,-1.686407,2.334301,0.356423,4.370787,-2.458462,3.569232,-9.577756,5.889381,-6.350081,9.979537,0.971428,-0.198037,9.782263,-4.985915,9.425016,-1.126036,7.444178,9.156610,5.935170,9.765420,3.254655,-6.504457,0.161647,1.251358,3.945306,0.745943,9.067674,1.550785,-9.708003,-4.897674,-5.750432,-3.272418,8.810583,4.252343,-3.117774,-5.019468,3.196802,6.432141,-7.497662,9.397856,6.919162,1.285560,-2.399416,7.430352,-1.938030,4.068089,-3.472528,-8.428869,3.178896,-0.271820,5.494617,2.435580,-1.833693,5.902550,5.969542,-7.932368,5.134974,-8.956750,-9.718232,6.713608,9.301445,-3.249206,-3.804248,2.479693,-6.567609,7.341565,-7.912298,-6.099571,8.796970,-2.889798,-5.833386,2.435457,-5.603171,-8.749683,-8.227533,3.737689,-6.095554,4.973870,-5.905561,-4.366128,9.906623,-1.747797,-2.923150,-4.042185,-3.607628,-4.200313,4.187836,7.418622,7.468745,1.950229,3.038471,-8.398902,-5.772487,-8.246293,-5.959523,3.591440,-4.737254,-0.279940,-6.836309,-4.788107,1.941378,-8.303571,-2.821928,-9.207786,7.749525,0.419837,-1.721809,-2.698372,-4.532382,6.306111,0.929485,-6.534546,3.117138,-0.379906,8.495517,-3.818308,8.367967,4.839644,-8.027390,-2.352971,9.725693,-6.345522,3.002603,-7.249120,0.691924,-7.395200,-5.157066,-0.728777,9.512302,-6.642468,2.729100,0.921309,6.533833,1.874888,-4.246846,3.480265,1.738758,9.087081,-8.337074,-5.870184,-6.822504,-4.187502,9.905065,-5.579840,0.120710,7.596247,2.094103,2.854787,-9.108567,7.729383,-6.152714,-0.529476,-9.469757,-0.559657,-4.536300,6.662392,-5.504266,2.439748,-2.727245,-6.247325,-7.916750,0.684024,2.205343,-4.363450,9.768739,-9.285995,-1.677152,7.024587,5.711958,3.930041,9.402629,-9.219423,-5.051689,1.303020,1.441584,-2.955783,-3.100694,1.191337,0.160972,2.125854,9.153457,-7.640947,-2.669665,2.057952,-5.991732,7.108581,5.264108,5.853286,-1.580887,-0.350703,-2.158354,8.951492,-5.770702,-6.354412,7.579969,-5.797012,-4.226951,-4.691403,4.597685,-6.802252,3.673095,7.713672,6.727420,-5.662600,4.986924,7.854912,-6.569017,-4.570617,3.759541,-6.533924,-1.166424,-1.850804,4.614451,-9.834924,-0.771143,-5.262493,-5.123313,-6.046400,-3.410846,8.011729,5.632230,-4.758543,-7.669403,4.250522,4.568226,-3.324999,-3.400753,-1.759750,3.457844,-7.317375,9.724303,3.039578,-5.893182,6.655357,7.730056,6.099690,6.815140,-4.931513,-2.584524,-0.621103,9.278226,-9.484161,1.661134,9.143376,8.770626,-5.935719,1.413343,-0.526760,3.057404,-3.610017,4.816867,3.465617,4.199548,-3.142155,1.707309,-3.984068,7.630129,5.122348,7.555384,1.190560,-5.763037,-7.028186,-1.643899,-1.106946,-9.988993,-0.733076,-0.679609,8.056518,3.545143,3.050277,-6.821125,6.300035,-8.458036,-2.204964,8.931137,-1.382489,1.414831,9.600339,-0.995414,1.861583,0.371908,-1.079256,2.965761,5.348914,5.790338,-2.178666,-6.533920,2.305595,-1.131536,0.016096,1.522229,6.864802,-2.273675,-1.680159,-1.624052,6.392354,5.631590,2.750524,7.303630,6.787806,-7.447048,-6.212219,0.292047,6.140689,4.689355,-3.050941,2.312916,1.873896,-1.026227,-9.689966,3.801335,-1.786315,1.677816,-2.115385,0.481046,1.902284,1.251225,-6.891745,1.200849,-8.034514,-6.481833,1.159375,-5.957433,1.137523,2.284802,-5.655912,-0.156990,0.220109,-2.222977,-0.237552,-7.661609,4.523132,-7.356929,-4.312609,-6.097242,-9.141322,8.812065,-5.671485,4.939539,6.388294,4.458675,2.252029,-3.929565,0.554638,-2.092672,-1.201115,4.073967,-3.823666,-1.465811,9.422411,8.360046,5.811251,0.888655,2.918639,-8.754449,1.220870,-0.332248,4.424187,-9.066900,5.662226,-2.081012,0.593428,-0.726184,4.531379,-1.949435,8.907491,9.079290,0.406024,-5.097945,9.249054,7.189399,-9.976968,1.215974,-8.805889,-5.955360,0.785321,-5.046911,-2.757436,-5.557164,5.456025,-0.980615,0.336003,5.440801,-3.425647,8.854845,-3.393052,1.583913,-3.273339,-6.482408,-9.712909,-5.963781,-4.426276,-8.286655,1.194396,-4.109002,3.241649,0.910734,-2.388524,6.768836,-1.298972,-4.903538,6.320806,9.758905,6.919497,6.603581,-3.389792,7.216283,-1.508080,9.026766,-9.550626,-2.764181,-1.068998,-0.678485,-6.119110,-6.283205,-0.589771,-9.008490,-6.520336,6.417744,5.658838,3.000490,1.558673,-2.977927,-3.493521,6.131471,-3.550377,-8.300145,-2.004369,3.061247,3.562963,2.285994,6.990100,1.148379,-6.059238,4.368991,7.089656,1.636638,2.858423,-3.449830,-9.427260,-1.971170,9.853830,2.307764,-5.045927,1.336548,-5.925614,9.007585,-0.293342,7.456338,-1.752585,-7.168259,8.246824,-6.882395,-6.713526,-7.434506,-7.508890,8.993716,-0.992740,6.129079,7.259295,-7.081139,-7.401840,3.664173,-0.818591,7.562650,5.526209,1.341243,8.619443,6.504918,-6.473860,-8.436833,6.779598,9.563863,0.318345,-3.458763,3.091560,-8.219415,-5.521392,-8.891333,7.162843,0.307453,8.812071,6.415088,-4.688431,-3.393154,7.604545,-6.704399,-7.538692,-5.401441,-9.979881,5.409227,7.331509,2.295439,3.754022,-6.019856,2.147570,-6.287539,-9.094913,-2.091200,-7.646117,-6.701588,1.337882,-7.568226,-4.446433,7.608681,1.107748,-1.886640,5.873887,2.253275,8.162306,3.081637,2.820144,8.344645,8.489372,4.114284,6.922701,8.037978,-1.213665,-9.704404,-9.414509,3.735265,-5.226445,-2.777161,-2.435914,8.092677,-0.477858,-0.290215,-3.054933,8.767533,4.188210,4.809295,-3.578458,-4.131349,3.501895,7.842395,-4.665697,6.091237,-8.070160,-2.167923,6.154830,-4.934209,-0.213945,-7.032878,7.780099,7.921525,-5.742533,8.457540,9.517915,4.465409,-7.460248,4.133208,2.422770,-7.441486,-7.008687,-6.592085,-9.949865,7.788606,-7.671668,4.925845,-6.895326,-4.013016,9.608647,8.354312,9.787399,3.606611,-4.165852,5.479619,-0.545798,2.603580,-0.750219,-6.793370,6.504087,-3.026108,7.304605,1.251710,-1.471698,-1.726590,6.645989,-4.399329,-5.004953,-9.425452,-2.720351,0.979673,1.765999,-3.216055,-7.166296,-9.444925,-3.096478,3.906084,-3.980248,2.453072,1.347386,7.941600,-8.884962,1.995892,3.526798,0.821237,8.575441,-7.422850,5.689221,1.925312,-7.376507,8.599812,-0.314691,-8.215563,7.228335,7.426835,-8.349659,0.619815,-0.091254,6.930416,3.409349,-2.838533,5.446360,3.233993,3.841175,5.915264,2.120433,-6.139009,2.002785,-9.460298,8.317126,3.036915,-1.915840,-0.696594,-1.957623,5.774830,-9.840827,-6.899196,-0.432040,-3.692897,-4.986229,6.142667,7.116267,0.760320,2.742485,3.432964,6.441336,-4.772613,-4.811455,8.545790,-1.911004,-8.630667,-4.190625,9.565445,-1.066796,-4.030742,7.197261,-8.461184,6.915285,9.128994,-6.043203,1.109358,-4.019519,9.303890,-1.691732,0.778285,8.480001,2.497755,-3.162995,5.585426,0.332180,-3.900256,8.128747,6.641541,-8.069226,1.349706,3.628233,1.021553,-7.900230,-8.425654,8.637958,-6.075920,7.678285,-8.766815,-0.122192,2.239150,4.184050,-5.973178,-9.416337,8.398463,-1.652236,4.953775,-7.078257,9.353411,-0.915878,7.227323,4.732288,-4.767988,-7.527328,3.288602,-8.713289,-0.305466,-2.078504,2.644688,-6.504664,7.122938,0.362081,-4.133172,1.598101,0.859545,-0.675200,6.232635,-7.024974,-8.419949,-9.450682,2.214689,-4.624514,-1.530103,-3.781905,-6.032920,9.051975,2.378450,-6.763421,-9.033710,-3.668355,7.263019,-5.414594,-5.976107,6.003283,2.914042,-6.723053,-9.551715,-9.003033,1.960928,-3.636556,0.544309,-8.180303,2.160676,8.414469,-4.115064,6.966243,-1.608648,9.751902,-8.791118,9.203743,-9.413162,-2.599554,3.265552,-2.046843,5.851650,-3.830830,-4.181403,0.810492,7.943452,6.195631,-5.878839,-6.568826,-8.737386,-7.383727,-2.783328,2.039928,9.246754,5.624159,-3.307119,-8.853968,4.525048,5.700138,8.694504,0.084039,3.846189,-8.137678,5.540555,-2.733548,-7.407621,-7.711612,-8.715930,-3.629038,0.438557,-8.023684,8.730705,1.107597,2.773300,-8.939759,3.376479,-3.323494,-3.018846,5.484614,8.779527,8.678838,-5.157320,-4.968749,2.695594,-5.904798,-0.148522,6.707931,2.168206,-1.580568,9.633075,6.936614,-6.508721,9.873719,0.753420,-8.223115,-7.970071,-0.569415,4.890783,8.074942,1.241632,8.293919,0.462589,9.245497,3.547016,6.189273,-4.617254,-1.824440,-6.329080,4.655175,-5.700463,-0.496066,-1.724540,8.875713,5.014469,-4.419359,-6.453958,0.699315,-1.058017,5.150333,-5.647745,-2.766496,1.019897,-3.818705,-8.656271,2.148424,0.926412,7.764612,5.699314,-0.895343,-1.977169,9.051166,-7.321839], dtype = "float64")#candidate|11475|(1280,)|const|float64
var_11476 = relay.var("var_11476", dtype = "float64", shape = (192,))#candidate|11476|(192,)|var|float64
call_11470 = relay.TupleGetItem(func_6309_call(relay.reshape(const_11471.astype('uint32'), [12, 11, 16]), relay.reshape(const_11471.astype('uint32'), [12, 11, 16]), relay.reshape(var_11472.astype('int32'), [21,]), relay.reshape(const_11473.astype('uint64'), [60,]), relay.reshape(var_11474.astype('int64'), [540, 1]), relay.reshape(const_11475.astype('float64'), [320, 4]), relay.reshape(var_11476.astype('float64'), [192,]), ), 2)
call_11477 = relay.TupleGetItem(func_6318_call(relay.reshape(const_11471.astype('uint32'), [12, 11, 16]), relay.reshape(const_11471.astype('uint32'), [12, 11, 16]), relay.reshape(var_11472.astype('int32'), [21,]), relay.reshape(const_11473.astype('uint64'), [60,]), relay.reshape(var_11474.astype('int64'), [540, 1]), relay.reshape(const_11475.astype('float64'), [320, 4]), relay.reshape(var_11476.astype('float64'), [192,]), ), 2)
func_10987_call = mod.get_global_var('func_10987')
func_10990_call = mutated_mod.get_global_var('func_10990')
var_11492 = relay.var("var_11492", dtype = "float32", shape = (2160,))#candidate|11492|(2160,)|var|float32
call_11491 = func_10987_call(relay.reshape(var_11492.astype('float32'), [16, 9, 15]))
call_11493 = func_10987_call(relay.reshape(var_11492.astype('float32'), [16, 9, 15]))
bop_11509 = relay.less_equal(call_11470.astype('bool'), var_11472.astype('bool')) # shape=(21,)
bop_11512 = relay.less_equal(call_11477.astype('bool'), var_11472.astype('bool')) # shape=(21,)
output = relay.Tuple([call_11468,const_11471,const_11473,var_11474,const_11475,var_11476,call_11491,var_11492,bop_11509,])
output2 = relay.Tuple([call_11469,const_11471,const_11473,var_11474,const_11475,var_11476,call_11493,var_11492,bop_11512,])
func_11516 = relay.Function([var_11472,var_11474,var_11476,var_11492,], output)
mod['func_11516'] = func_11516
mod = relay.transform.InferType()(mod)
var_11517 = relay.var("var_11517", dtype = "int32", shape = (21,))#candidate|11517|(21,)|var|int32
var_11518 = relay.var("var_11518", dtype = "int64", shape = (540,))#candidate|11518|(540,)|var|int64
var_11519 = relay.var("var_11519", dtype = "float64", shape = (192,))#candidate|11519|(192,)|var|float64
var_11520 = relay.var("var_11520", dtype = "float32", shape = (2160,))#candidate|11520|(2160,)|var|float32
output = func_11516(var_11517,var_11518,var_11519,var_11520,)
func_11521 = relay.Function([var_11517,var_11518,var_11519,var_11520,], output)
mutated_mod['func_11521'] = func_11521
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11550 = relay.var("var_11550", dtype = "uint8", shape = (1, 1, 14))#candidate|11550|(1, 1, 14)|var|uint8
var_11551 = relay.var("var_11551", dtype = "uint8", shape = (4, 1, 14))#candidate|11551|(4, 1, 14)|var|uint8
bop_11552 = relay.multiply(var_11550.astype('uint8'), var_11551.astype('uint8')) # shape=(4, 1, 14)
output = relay.Tuple([bop_11552,])
output2 = relay.Tuple([bop_11552,])
func_11566 = relay.Function([var_11550,var_11551,], output)
mod['func_11566'] = func_11566
mod = relay.transform.InferType()(mod)
mutated_mod['func_11566'] = func_11566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11566_call = mutated_mod.get_global_var('func_11566')
var_11568 = relay.var("var_11568", dtype = "uint8", shape = (1, 1, 14))#candidate|11568|(1, 1, 14)|var|uint8
var_11569 = relay.var("var_11569", dtype = "uint8", shape = (4, 1, 14))#candidate|11569|(4, 1, 14)|var|uint8
call_11567 = func_11566_call(var_11568,var_11569,)
output = call_11567
func_11570 = relay.Function([var_11568,var_11569,], output)
mutated_mod['func_11570'] = func_11570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_11578 = func_7344_call()
call_11579 = func_7344_call()
output = relay.Tuple([call_11578,])
output2 = relay.Tuple([call_11579,])
func_11580 = relay.Function([], output)
mod['func_11580'] = func_11580
mod = relay.transform.InferType()(mod)
output = func_11580()
func_11581 = relay.Function([], output)
mutated_mod['func_11581'] = func_11581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_11598 = relay.TupleGetItem(func_11351_call(), 0)
call_11599 = relay.TupleGetItem(func_11352_call(), 0)
func_9607_call = mod.get_global_var('func_9607')
func_9609_call = mutated_mod.get_global_var('func_9609')
call_11602 = relay.TupleGetItem(func_9607_call(), 0)
call_11603 = relay.TupleGetItem(func_9609_call(), 0)
output = relay.Tuple([call_11598,call_11602,])
output2 = relay.Tuple([call_11599,call_11603,])
func_11617 = relay.Function([], output)
mod['func_11617'] = func_11617
mod = relay.transform.InferType()(mod)
output = func_11617()
func_11618 = relay.Function([], output)
mutated_mod['func_11618'] = func_11618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mod.get_global_var('func_8349')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_11638 = func_8349_call()
call_11639 = func_8349_call()
output = relay.Tuple([call_11638,])
output2 = relay.Tuple([call_11639,])
func_11648 = relay.Function([], output)
mod['func_11648'] = func_11648
mod = relay.transform.InferType()(mod)
mutated_mod['func_11648'] = func_11648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11648_call = mutated_mod.get_global_var('func_11648')
call_11649 = func_11648_call()
output = call_11649
func_11650 = relay.Function([], output)
mutated_mod['func_11650'] = func_11650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9832_call = mod.get_global_var('func_9832')
func_9833_call = mutated_mod.get_global_var('func_9833')
call_11826 = relay.TupleGetItem(func_9832_call(), 0)
call_11827 = relay.TupleGetItem(func_9833_call(), 0)
output = call_11826
output2 = call_11827
func_11830 = relay.Function([], output)
mod['func_11830'] = func_11830
mod = relay.transform.InferType()(mod)
output = func_11830()
func_11831 = relay.Function([], output)
mutated_mod['func_11831'] = func_11831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8978_call = mutated_mod.get_global_var('func_8978')
call_11855 = relay.TupleGetItem(func_8977_call(), 0)
call_11856 = relay.TupleGetItem(func_8978_call(), 0)
func_10483_call = mod.get_global_var('func_10483')
func_10486_call = mutated_mod.get_global_var('func_10486')
var_11860 = relay.var("var_11860", dtype = "float32", shape = (48,))#candidate|11860|(48,)|var|float32
call_11859 = relay.TupleGetItem(func_10483_call(relay.reshape(var_11860.astype('float32'), [48,])), 3)
call_11861 = relay.TupleGetItem(func_10486_call(relay.reshape(var_11860.astype('float32'), [48,])), 3)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_11892 = relay.TupleGetItem(func_11351_call(), 0)
call_11893 = relay.TupleGetItem(func_11352_call(), 0)
output = relay.Tuple([call_11855,call_11859,var_11860,call_11892,])
output2 = relay.Tuple([call_11856,call_11861,var_11860,call_11893,])
func_11894 = relay.Function([var_11860,], output)
mod['func_11894'] = func_11894
mod = relay.transform.InferType()(mod)
mutated_mod['func_11894'] = func_11894
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11895 = relay.var("var_11895", dtype = "float32", shape = (48,))#candidate|11895|(48,)|var|float32
func_11894_call = mutated_mod.get_global_var('func_11894')
call_11896 = func_11894_call(var_11895)
output = call_11896
func_11897 = relay.Function([var_11895], output)
mutated_mod['func_11897'] = func_11897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9637_call = mod.get_global_var('func_9637')
func_9639_call = mutated_mod.get_global_var('func_9639')
call_11908 = func_9637_call()
call_11909 = func_9637_call()
output = call_11908
output2 = call_11909
func_11923 = relay.Function([], output)
mod['func_11923'] = func_11923
mod = relay.transform.InferType()(mod)
output = func_11923()
func_11924 = relay.Function([], output)
mutated_mod['func_11924'] = func_11924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9380_call = mod.get_global_var('func_9380')
func_9382_call = mutated_mod.get_global_var('func_9382')
call_11961 = func_9380_call()
call_11962 = func_9380_call()
output = call_11961
output2 = call_11962
func_11986 = relay.Function([], output)
mod['func_11986'] = func_11986
mod = relay.transform.InferType()(mod)
mutated_mod['func_11986'] = func_11986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11986_call = mutated_mod.get_global_var('func_11986')
call_11987 = func_11986_call()
output = call_11987
func_11988 = relay.Function([], output)
mutated_mod['func_11988'] = func_11988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9665_call = mod.get_global_var('func_9665')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_12041 = relay.TupleGetItem(func_9665_call(), 0)
call_12042 = relay.TupleGetItem(func_9666_call(), 0)
uop_12054 = relay.log10(call_12041.astype('float32')) # shape=(550,)
uop_12056 = relay.log10(call_12042.astype('float32')) # shape=(550,)
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_12083 = func_11336_call()
call_12084 = func_11336_call()
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_12090 = relay.TupleGetItem(func_6751_call(), 0)
call_12091 = relay.TupleGetItem(func_6753_call(), 0)
uop_12094 = relay.cosh(uop_12054.astype('float32')) # shape=(550,)
uop_12096 = relay.cosh(uop_12056.astype('float32')) # shape=(550,)
func_9894_call = mod.get_global_var('func_9894')
func_9896_call = mutated_mod.get_global_var('func_9896')
call_12108 = relay.TupleGetItem(func_9894_call(), 0)
call_12109 = relay.TupleGetItem(func_9896_call(), 0)
func_1094_call = mod.get_global_var('func_1094')
func_1099_call = mutated_mod.get_global_var('func_1099')
const_12127 = relay.const(7, dtype = "int16")#candidate|12127|()|const|int16
const_12128 = relay.const([-10,-8,-4,-3,-2,-2,5,-1,-8,-6,-2,5,-10,-3,2,5,-4,5,8,8,2,-8,-2,9,-4,6,-2,9,-1,7,4,-5,5,-8,-9,2,-6,10,9,-1,4,9,8,8,-2,-5,6,-5,-2,-3,9,6,-4,-5,-4,6,-4,6,4,-1,8,3,8,5,10,2,-1,-5,5,-8,6,8,10,2,-9,-2,-1,-1,4,-8,3,-6,-10,-1,-2,-5,4,10,9,-8,7,5,7,-4,1,-7,-5,1,5,10,3,-10,1,3,-4,-8,10,-8,9,-8,-5,7,10,-5,9,4,5,1,6,5,4,10,9,3,-9,10,-7,-5,-4,2,10,-7,2,10,-1,-7,-10,-1,6,-9,-8,-10,-8,2,7,-5,-1,-1,-2,10,-6,10,-5,-7,6,7,-6,1,-4,-6,-8,-8,-3,4,2,1,-3,5,2,1,1,4,-5,-1,-7,-9,-10,-5,-8,10,-7,9,10,9,8,-1,-8,-6,9,1,8,10,7,-1,-6,-4,-2,2,6,3,1,-3,-9,3,10,-4,6,-6,-1,7,-8,10,-5,-1,6,-7,7,8,-2,-6,7,-1,-3,-5,4,2,6,-1,6,3,5,1,-9,2,3,6,-5,2,-3,-2,2,2,-8,8,6,-8,-1,-5,-9,4,4,-2,6,-8,-3,-10,4,3,-7,-8,4,4,-4,-10,7,-2,5,-9,-8,-3,-7,5,5,5,-1,-4,10,4,10,-6,-9,7,4,6,5,4,4,-5,-9,10,-5,9,-4,-9,9,3,-6,4,8,-4,1,7,9,-4,-4,10,-1,-7,4,-3,-3,-10,7,-1,-6,-10,-2,2,-10,-10,1,8,-1,-10,2,7,-8,-6,-3,-1,-1,5,1,7,-4,-10,8,-8,2,5,1,-1,1,5,-6,4,-1,-3,8,6,6,6,1,-5,4,-10,4,-6,-1,-10,1,-6,-2,-5,-6,2,-4,-8,-2,1,-2,3,-2,-10,1,-2,3,7,7,-8,2,7,-6,-2,-9,-6,-3,7,-7,-2,9,1,4,-9,-9,-5,5,-8,8,-1,4,-6,-4,4,-3,10,-4,4,-10,-8,10,-9,-7,7,-6,10,6,8,-2,1,-1,-7,-3,-3,-6,1,6,2,-6,7,-7,-3,5,-3,6,-10,5,1,10,9,7,-1,-10,6,-4,-2,-2,-4,-8,3,10,-8,3,-3,7,9,3,-9,-7,-1,-10,9,-9,10,-9,9,10,-4,-9,6,-10,2,-8,-6,-5,-3,-1,-10,5,-6,-5,-4,4,-8,5,-1,-2,8,-3,5,3,-5,-10,5,-5,2,7,6,5,6,-9,-7,-9,3,1,-10,-5,9,9,3,-4,-7,4,-2,-7,-1,7,-9,4,10,7,-8,-4,10,-10,1,-1,-4,-10,-3,7,5,-3,2,-6,3,-2,-8,9,-2,-10,-2,9,-5,4,-8,-4,-5,-7,6,-9,7,-9,8,2,6,2,10,-4,2,2,9,1,3,-2,1,8,-1,-4,7,-8,5,-9,-1,1,10,-3,9,2,-2,-3,-4,-3,-9,5,-1,7,2,3,10,9,7,-7,-4,10,-1,-2,-3,-1,4,-6,-8,-2,-10,6,-9,8,-4,4,-3,-7,7,-1,-4,3,-8,-4,-6,9,-1,6,9,-8,2,-3,8,1,-9,8,-5,-1,1,-1,2,-5,-4,-5,-8,6,-6,-4,8,10,6,-1,8,-3,-7,-8,-4,-2,-3,-1,-1,-10,5,1,-7,-1,8,3,-3,-7,-3,-1,-5,7,-1,10,7,-1,1,-8,-3,-1,-10,-9,3,5,-8,-4,1,-2,2,-6,-1,3,-9,8,1,-4,-4,-6,-8,2,7,-10,9,-1,-5,2,-4,-6,6,-4,5,-8,3,-5,-4,7,-7,10,-1,9,-7,-2,5,-3,-3,-10,7,9,-1,-10,-5,8,6,-10,-8,4,9,8,3,-7,-8,-7,6,-2,-2,3,1,-9,-9,5,7,7,-3,-2,-6,-5,7,-7,9,9,4,-9,3,-4,-7,4,-6,10,3,6,-10,-4,-4,-9,2,4,-9,-1,-1,7,-3,1,-1,9,-10,3,-9,-8,-8,5,4,6,-4,-8,-3,4,7,5,4,-1,-10,-8,-3,-3,-3,9,-10,1,-1,1,-5,9,-8,-9,10,-9,-4,1,-3,-8,-3,-4,-1,6,-3,7,-2,9,3,-4,-7,5,-2,-9,-1,1,-6,-6,7,1,3,-9,8,-6,-5,-6,-5,-4,-7,2,-1,-1,-6,-4,-3,7,4,-10,4,-5,-8,1,-2,-10,1,-9,5,-9,-9,7,7,9,-10,8,-4,-2,4,6,2,4,-10,-6,-5,9,6,-7,8,6,4,1,-7,-2,10,-6,8,6,5,4,-4,3,6,5,-5,-3,7,8,-9,-4,2,1,-1,7,-8,-5,3,4,-9,5,-10,-4,-4,-10,5,-4,-3,5,4,2,-5,6,-5,7,-7,-8,3,-5,-4,-10,8,-6,-8,7,-4,-4,5,7,8,2,6,-4,1,4,2,-6,7,-3,4,-5,-8,9,8,-3,-10,4,6,5,-5,5,-2,-2,-5,-3,5,-9,-8,-6,2,5,-6,-8,-6,2,-1,-1,-9,3,7,3,6,7,-10,-2,-4,-6,5,5,-6,-3,3,9,8,-8,-8,9,4,-9,10,-1,-8,5,1,-5,6,-6,-3,-2,9,-7,2,-2,-3,3,10,-6,-10,-10,-2,10,4,-6,10,-1,8,5,-6,-6,-6,10,2,-4,10,3,-10,7,-8,-2,-3,-5,-1,-10,-5,-5,7,9,-3,4,-7,-3,-10,1,-7,6,6,-10,-2,-1,7,10,-1,-5,-9,8,-6,5,5,-3,10,10,-1,-10,-1,9,-9,3,-7,-4,5,-6,-5,6,8,-2,-1,4,-5,4,-7,3,4,-8,4,1,6,-10,-8,-2,-8,-5,-7,10,5,-9,6,8,9,3,10,3,-9,6,1,-6,-2,-9,-1,-2,-2,-9,-4,10,-5,-5,5,10,2,5,-5,4,3,-8,-2,-1,3,5,-8,-1,6,-9,-5,-8,8,10,-6,3,-8,4,-3,-4,-8,6,-2,1,2,-10,1,-3,3,2,-8,9,-6,-5,9,-7,-6,4,-9,-7,-5,7,-7,4,-4,9,1,-7,10,-6,-1,7,8,-7,-6,-10,-1,8,-9,-2,-3,4,-9,-1,-5,10,-1,-5,-10,-6,5,9,2,8,4,-6,-10,-10,-3,10,7,-6,-8,-7,-1,7,8,-4,3,-4,1,-3,10,2,4,3,-1,-10,-10,-9,10,9,-2,-8,6,-4,-2,9,-2,-5,-2,-6,7,-6,-2,10,-3,-10,1,-1,-10,5,4,1,-7,-10,7,6,3,3,-8,-9,-9,7,-5,-8,-5,-6,-8,-5,-5,6,5,6,-3,-7,-1,6,-5,1,-3,-6,1,-9,1,4,3,8,9,7,-4,-6,9,6,-5,4,5,8,2,-4,3,8,5,3,-1,-9,3,9,-7,7,-1,2,3,-3,9,-9,-5,-10,5,6,4,-1,1,2,-7,2,2,-6,-7,-3,4,1,-8,-10,4,9,3,4,1,6,5,-6,5,3,8,-8,-7,-4,10,10,-3,-10,10,-2,10,-7,-7,3,4,2,3,6,1,-8,7,-4,6,7,-10,5,9,8,-4,6,6,-9,1,10,7,-2,-6,5,4,10,-10,-5,-8,3,-3,-1,10,-9,-7,-1,-9,-1,1,6,5,-9,-2,4,-9,-1,9,-3,-2,-7,5,5,3,8,-9,9,-2,-1,-5,4,5,8,9,-10,-6,-10,-5,7,-9,1,-9,6,-1,8,3,1,7,-1,-1,-7,-9,1,2,-3,-1,2,7,5,-4,-3,5,6,-3,10,1,-2,6,8,9,10,-8,-4,-10,-2,-2,-5,8,8,-10,5,6,4,1,10,5,-2,4,-7,-4,3,5,10,-9,5,7,-5,-7,6,2,8,8,10,5,-8,-8,3,-9,7,3,9,1,-4,-2,-4,6,2,1,4,1,5,5,3,2,1,-1,5,4,-8,-2,1,-4,10,6,1,7,5,3,5,-9,1,7,-3,9,-7,6,7,-2,-5,-2,-4,-4,1,8,-3,2,-8,-3,-10,-2,1,5,-8,-6,3,-3,7,7,-3,5,3,-3,6,2,8,3,2,9,4,6,5,6,5,1,-10,5,4,4,5,6,-10,5,6,3,-1,-1,8,-8,3,-10,-6,8,-6,9,-6,3,3,-9,3,-3,1,-1,-3,2,8,1,-1,-3,-1,6,-7,-5,-8,1,6,-8,-8,-8,9,7,3,3,-6,1,-9,7,8,6,6,-9,-1,-1,-7,-8,-10,8,-4,1,7,9,9,-4,6,6,7,-4,4,7,-8,-10,9,-4,-8,3,7,3,-6,6,7,5,7,4,7,-3,-6,3,-10,8,-4,-3,-3,-10,3,2,-5,-6,8,-4,-3,2,-9,-5,-6,6,4,-2,6,-9,-7,1,-9,4,8,2,4,-1,1,-3,8,6,9,-2,-9,3,1,-7,10,-6,1,10,-4,-10,6,3,-1,6,6,-4,-9,10,-3,-8,10,3,-6,7,-5,-6,-10,-5,-7,-10,10,-7,-5,7,-5,10,1,-9,8,8,4,-4,-2,-7,1,1,3,8,-6,-5,2,-10,-1,-9,-6,-4,-2,7,9,-2,-1,-10,2,2,3,-2,-3,7,1,4,-4,10,-9,9,-8,8,5,-4,8,-6,5,7,10,3,1,-1,-6,-10,-7,-2,-1,4,8,4,6,-6,-9,1,6,-1,9,-1,-2,-1,1,3,4,1,-9,-8,6,6,-7,-3,10,10,-7,-6,4,-9,1,-9,1,-6,5,-5,-8,-4,-9,7,-2,-1,-8,9,6,-6,-10,-3,5,9,-3,-10,-7,-7,-1,6,-9,-2,5,6,-9,-8,7,8,-3,1,3,-9,6,-9,-8,10,-1,6,-6,-7,7,4,9,8,-10,7,2,6,-4,5,-9,1,1,-7,-10,-4,10,-2,9,-10,-9,-6,5,-9,8,-10,10,8,1,-10,2,9,-1,2,1,1,-10,-2,-9,-3,6,-4,9,8,9,-10,-2,-4,9,3,7,1,10,-2,6,-6,1,9,-3,-9,-4,3,7,9,3,-8,-5,-6,2,-4,5,1,9,5,6,4,2,-6,-9,5,-6,-10,1,5,-6,-4,-10,-7,4,1,-6,9,-6,-7,9,-5,-6,-7,-5,-4,3,3,4,10,-2,5,-8,7,9,-9,5,-5], dtype = "int16")#candidate|12128|(1980,)|const|int16
var_12129 = relay.var("var_12129", dtype = "uint64", shape = (60,))#candidate|12129|(60,)|var|uint64
call_12126 = relay.TupleGetItem(func_1094_call(relay.reshape(const_12127.astype('int16'), []), relay.reshape(const_12128.astype('int16'), [15, 12, 11]), relay.reshape(var_12129.astype('uint64'), [60,]), ), 0)
call_12130 = relay.TupleGetItem(func_1099_call(relay.reshape(const_12127.astype('int16'), []), relay.reshape(const_12128.astype('int16'), [15, 12, 11]), relay.reshape(var_12129.astype('uint64'), [60,]), ), 0)
output = relay.Tuple([call_12083,call_12090,uop_12094,call_12108,call_12126,const_12127,const_12128,var_12129,])
output2 = relay.Tuple([call_12084,call_12091,uop_12096,call_12109,call_12130,const_12127,const_12128,var_12129,])
func_12140 = relay.Function([var_12129,], output)
mod['func_12140'] = func_12140
mod = relay.transform.InferType()(mod)
mutated_mod['func_12140'] = func_12140
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12141 = relay.var("var_12141", dtype = "uint64", shape = (60,))#candidate|12141|(60,)|var|uint64
func_12140_call = mutated_mod.get_global_var('func_12140')
call_12142 = func_12140_call(var_12141)
output = call_12142
func_12143 = relay.Function([var_12141], output)
mutated_mod['func_12143'] = func_12143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_12182 = relay.TupleGetItem(func_7952_call(), 0)
call_12183 = relay.TupleGetItem(func_7954_call(), 0)
var_12193 = relay.var("var_12193", dtype = "bool", shape = (10, 7, 8))#candidate|12193|(10, 7, 8)|var|bool
bop_12194 = relay.equal(call_12182.astype('bool'), relay.reshape(var_12193.astype('bool'), relay.shape_of(call_12182))) # shape=(10, 7, 8)
bop_12197 = relay.equal(call_12183.astype('bool'), relay.reshape(var_12193.astype('bool'), relay.shape_of(call_12183))) # shape=(10, 7, 8)
output = bop_12194
output2 = bop_12197
func_12204 = relay.Function([var_12193,], output)
mod['func_12204'] = func_12204
mod = relay.transform.InferType()(mod)
var_12205 = relay.var("var_12205", dtype = "bool", shape = (10, 7, 8))#candidate|12205|(10, 7, 8)|var|bool
output = func_12204(var_12205)
func_12206 = relay.Function([var_12205], output)
mutated_mod['func_12206'] = func_12206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_12213 = func_8696_call()
call_12214 = func_8696_call()
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_12222 = func_8696_call()
call_12223 = func_8696_call()
output = relay.Tuple([call_12213,call_12222,])
output2 = relay.Tuple([call_12214,call_12223,])
func_12235 = relay.Function([], output)
mod['func_12235'] = func_12235
mod = relay.transform.InferType()(mod)
mutated_mod['func_12235'] = func_12235
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12235_call = mutated_mod.get_global_var('func_12235')
call_12236 = func_12235_call()
output = call_12236
func_12237 = relay.Function([], output)
mutated_mod['func_12237'] = func_12237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_12268 = func_11336_call()
call_12269 = func_11336_call()
func_8720_call = mod.get_global_var('func_8720')
func_8723_call = mutated_mod.get_global_var('func_8723')
const_12293 = relay.const([5.935042,-8.282376,-2.561735,-4.734670,-8.585851,-1.195719,9.305903,-7.832392,-5.060425,7.274265,7.859938,-3.537154,1.071021,7.668932,-9.090999,0.157460,-1.460276,-1.007454,-1.654813,-8.229049,4.038312,8.943028,5.875862,2.912008,0.213104,8.311553,2.125984,-9.180165,1.478973,8.891306,-1.981693,2.864650,0.670363,3.791304,2.594684,-1.105273,-4.724887,1.756581,-6.397966,9.106147,4.218577,-2.623694,-2.154080,5.890215,-0.581191,0.784090,5.546535,-6.303979,5.173165,-7.494760,9.517295,8.044957,1.646203,-1.681857,8.549622,6.215604,-1.250073,3.262296,-0.608973,-1.366565,3.458354,-7.519533,4.598246,1.157765,-2.770072,1.202923,1.707573,-4.859292,1.707752,-6.796772,-2.878413,2.655481,7.661500,-2.197743,4.721868,-9.175566,-7.631301,-6.397349,2.470251,-0.231428,5.359297,-1.816093,-4.052970,9.159359,9.618260,-5.565796,-2.929349,-8.123457,-3.701484,6.781034,4.266547,0.751232,-8.559623,1.290544,5.637339,-2.884668,6.671545,6.497192,9.953329,6.872760,-8.381584,-4.287269,8.883564,-2.970876,4.380082,-5.140128,-2.248126,9.405587,8.294596,-3.704863,-2.572603,7.521380,2.276552,-9.450364,-8.710396,5.083327,4.916546,1.898796,-5.706701,2.694807,9.274834,3.685400,3.732050,1.298187,5.829910,2.431010,-7.500711,-7.513674,-7.247677,-6.318667,-8.456042,5.652871,5.198390,1.043185,9.914298,-1.041645,-7.496258,-4.569362,-7.478437,-0.284557,9.106971,7.667379,-6.879143,-2.057006,-2.702881,5.972580,-0.777754,8.371790,1.915935,-7.304185,5.973174,-7.852315,-4.824487,0.578701,-1.723073,-1.609396,0.551040,9.982091,7.939775,-8.817707,-9.866526,3.336433,2.859774,-2.674866,6.044058,9.389022,1.040018,-6.470245,-6.642160,-2.467367,5.918621,-7.102852,5.841779,-6.465721,4.544141,-6.760888,7.314098,6.838925,-0.680614,6.033904,-5.737530,-1.213769,-8.374293,6.145633,-9.106817,6.146107,-3.627711,1.109493,3.905188,9.422850,-9.911927,-3.048789,1.158227,-4.247352,-4.016107,4.406248,-6.176520,-0.126620,-2.591333,5.376927,-4.416044,-0.174959,9.364546,-8.375439,1.314443,0.474695,3.210833,9.564744,6.259356,6.526638,-8.082099,-8.035777,-5.506059,6.401740,-5.647506,-3.032173,-7.825692,-0.257140,-4.800518,-0.555418,-1.274086,2.582643,-5.450659,-3.832798,3.433043,6.809830,-2.658674,-4.410290,-2.692083,3.991594,6.583652,1.418871,-8.673201,3.508944,-2.048901,-2.498497,2.793744,4.131654,2.578107,-9.018853,8.242790,-1.867855,1.356680,-0.351437,-5.701391,3.631186,9.924388,0.783445,-7.366767,-5.257459,7.869891,9.787564,2.067854,-9.933335,-9.164964,1.675849,-6.155701,4.967055,-2.727623,1.321730,7.426739,-4.941597,-8.482440,-6.026323,-1.481651,9.921045,5.994287,5.694699,2.610725,8.120163,-9.578324,4.534995,-9.800752,-4.634036,1.170486,-4.405373,-7.784870,3.568911,-2.065027,9.005979,2.903588,-5.327582,3.313556,4.052447,1.736876,-7.795334,5.544749,-3.307001,-2.644098,-7.005006,9.936818,-3.179147,-3.952239,-7.052576,7.402482,6.788757,-3.530540,-4.175802,6.391596,3.685872,-1.781492,-5.882616,1.124162,-0.324896,-9.890184,3.223769,5.196556,8.265232,-9.234222,-5.652902,-6.469828,-6.986836,-3.520662,-0.706258,-1.378064,-6.832238,-4.910927,-1.102077,-3.644002,1.584813,1.856956,-8.670469,6.433282,-1.338935,1.909881,8.725153,2.601580,-8.094533,-5.511798,4.122680,-8.963085,-6.176508,6.450350,3.239675,1.352617,-6.782771,6.726691,6.758022,-6.666041,-3.811337,-2.790189,0.144266,0.728006,3.861277,6.841893,-7.184983,3.952156,-9.522158,1.350554,-8.826683,-4.177331,-4.743324,0.981516,-0.572666,7.047810,4.767013,6.805084,9.187026,-9.150652,-1.598952,-8.204122,-4.539324,0.520376,-5.048260,-5.679740,7.694184,1.170547,-1.031233,2.236207,-7.765035,-9.058831,2.394189,1.583622,-3.248019,3.155996,6.417796,-9.039762,4.964950,-7.152559,-1.346280,-0.583494,1.916171,7.455119,-4.247880,8.542905,-1.921375,-4.336336,8.030373,-5.815331,-7.229963,-0.383586,7.970442,2.021282,4.276605,-0.585211,-1.546705,3.731831,-5.845556,7.068361,-6.442671,-0.596679,-7.591973,-4.937260,-2.409990,-1.874137,-5.400090,-9.361926,4.374914,0.047322,4.398529,-7.878590,-9.591134,6.874503,0.922397,-0.902338,7.650249,-4.759449,3.670805,0.143502,9.145979,-1.392754,6.348729,-9.569811,-4.528061,2.266030,4.669010,1.518192,8.216856,5.002635,-6.271054,-2.943515,-9.232672,4.856040,0.736638,3.420132,-3.203034,3.086249,-3.823693,-3.514349,8.584015,-5.820899,-1.879203,-7.344422,-3.708555,-6.479306,1.690163,7.641930,4.201659,-8.915144,0.392266,0.530792,2.738706,1.304272,-5.506009,2.350343,8.016404,8.117191,2.997122,-6.527796,9.602099,-1.999107,8.870483,-9.545939,7.374064,-1.032302,-2.083421,-2.683129,-8.034334,7.628240,-2.653200,-8.869002,-9.969728,4.604491,8.533224,0.479757,-4.785409,-1.242753,4.082047,-5.432217,5.665517,-4.845852,-3.058841,5.985920,-9.831983,-4.151615,9.242119,5.708833,-9.520623,-2.070807,-9.387949,-4.759435,1.546328,-8.576365,4.441710,5.864717,2.171511,-3.029444,2.998773,-8.539809,-0.153032,-0.921884,4.456161,2.620021,-3.295589,-1.806213,9.190066,3.363340,7.124940,-3.569132,-5.122684,7.275391,1.705474,2.669986,3.236995,-4.931932,-6.709549,-2.490786,-5.193401,4.554975,6.296405,6.403067,-1.381129,4.614295,3.111041,-0.563526,-1.141380,2.805207,5.186552,-6.540114,4.067339,-8.688468,4.218017,7.374354,-5.268120,-0.118692,-0.235300,9.576136,-6.898089,-2.324526,-7.783567,3.369024,-3.379705,-7.710904,8.687586,8.146130,0.871566,4.248210,-9.521450,3.546733,4.208473,-3.134505,2.156101,5.840765,-1.901421,6.917525,-6.752052,5.253641,-5.690748,2.979594,-3.788082,-8.268440,-4.168621,-1.766445,-7.330940,-1.787425,5.202485,-8.038847,-4.820588,-7.939066,0.802328,1.874842,-2.824028,8.812125,-0.791293,2.256075,0.954728,-8.897942,8.007576,-7.756637,-8.030516,7.285284,7.609024,0.252976,9.282969,-4.751823,6.623547,8.433407,1.796736,-4.445162,7.093067,-2.606829,3.113829,-9.166339,-4.175750,9.510577,5.080575,-3.916509,-6.750453,-8.764070,-6.861300,-7.680712,-6.205025,6.615231,-5.686848,9.144793,3.587947,-2.038748,9.219189,8.659059,5.659725,-0.745226,-5.133427,2.753686,-2.852767,-4.872625,4.395854,0.092857,-6.143075,2.304546,-8.475689,-2.964868,-1.121023,3.665298,-7.610019,0.415561,4.843901,-8.032422,7.405245,-4.058364,-6.876592,-4.673164,0.697391,5.414460,-8.791991,9.757285,-5.128719,5.231393,-3.433121,-3.049868,7.913926,1.409897,2.698423,-6.503302,2.112884,5.306305,-9.049034,3.959870,4.736155,0.020320,4.271112,-8.678852,7.532234,5.450545,-6.047134,-0.118543,6.129019,-8.075805,0.711831,2.955561,9.081961,-9.023263,-4.857639,-0.942680,5.605344,-9.512561,-8.197283,-1.540044,-6.228558,8.760308,3.094849,-3.703432,3.507018,8.917146,-8.712294,-6.265283,8.170457,8.466374,-3.404135,6.873492,7.777786,4.601747,5.800327,6.555104,1.497426,-3.293086,-9.039488,8.700521,-7.381395,2.271528,-1.816307,-1.261304,-8.269858,6.828607,1.016638,-3.222233,-8.797838,-0.745019,1.714685,3.775788,5.371056,4.807643,9.856761,1.997721,-1.142869,-5.292992,-7.400645,-5.021766,-8.341238,-9.402072,0.729591,-4.688470,-6.090049,6.841896,3.417956,-4.611045,-9.584028,-0.655553,-6.544697,1.229726,-0.844690,8.261592,6.325365,-9.752473,-2.827169,0.105090,4.521798,8.227646,4.212525,-9.582054,-8.714921,6.442009,-8.094064,-9.310695,4.040973,6.833931,2.495209,9.790216,6.527464,-5.030218,-6.777989,0.451180,7.422482,7.521717,4.366903,9.278877,-2.227140,-8.916315,7.131231,3.138304,7.527062,-6.735885,-2.167982,7.943933,3.831996,1.507193,7.044120,-3.084048,2.425625,7.652717,0.379150,-6.181014,0.602936,-7.705414,6.204214,-0.959566,3.621532,4.297626,-4.274339,2.756303,-5.147494,6.041276,5.265928,7.459124,1.256029,0.557706,0.885568,-5.087992,-0.946364,5.927495,-6.202719,-5.583158,1.828896,9.209599,-5.188067,9.806411,6.479492,2.219591,-7.557747,-5.107804,9.375314,-5.336615,7.504186,-9.844494,-9.288832,-0.119197,5.879626,-9.934158,-6.525507,-6.461699,-5.043722,-3.265791,-4.677255,-0.150506,-7.860381,-7.722701,-2.732100,-6.517280,7.979218,7.185435,4.003747,-5.441419,1.746732,6.096795,4.428384,-4.403880,7.855967,0.257315,-8.641844,6.057432,-1.185256,0.423401,-8.903518,5.084211,-3.066132,3.372690,-2.494318,-1.503976,-7.362126,9.833240,1.901602,3.477053,-9.476337,-0.672900,-3.679550,7.295400,9.629865,7.892732,0.157151,6.923639,-2.266949,7.919468,-4.152558,-7.056347,2.674384,-1.047315,5.887827,2.703099,8.637164,0.923440,9.515110,-6.152627,4.039550,3.645842,-5.860600,-6.872610,2.657762,8.720641,3.800136,8.148434,-0.453475,8.150458,9.164355,6.577864,-3.677203,7.631077,-8.084826,-9.179501,3.470855,-4.802287,-2.211931,-3.178267,-0.268012,8.475233,0.318107,-3.204921,0.025964,-7.787327,-7.067513,3.474973,-8.122958,1.733564,-3.620348,-2.039700,2.892119,-4.060993,1.300671,1.461837,-4.030098,1.060222,0.420359,3.752028,5.554447,-1.356543,-1.684561,-9.564814,-5.684362,2.437307,5.784264,-5.283495,-9.894494,-2.042804,-4.973201,7.674516,-1.726009,-2.886132,-7.013384,-7.721999,6.787275,6.338048,-3.839068,-2.136847,5.270416,-7.361892,8.566652,8.086047,7.815012,3.644431,-8.467740,-3.757771,5.774483,-4.972519,3.464466,1.333628,5.012939,-3.198998,-8.947930,-5.714744,-5.089582,-8.167061,-6.038548,0.844243,0.180249,1.273240,3.275557,6.786903,-9.252720,-3.924516,-9.916998,9.642226,-8.127624,-5.290283,-9.044559,1.864980,5.925753,8.902789,8.167528,6.722499,3.868976,-8.624176,-1.608527,-6.998049,-6.244896,-7.162368,-1.610649,-7.509416,6.249695,-1.050183,-2.797155,-0.856607,4.600478,2.845345,-4.715682,-9.017999,6.661419,-3.813197,-4.603216,-5.689546,2.046906,7.802892,-9.710379,3.264266,-7.247115,-6.258810,8.589611,-7.579147,-7.827850,2.527520,-2.745012,-9.684078,0.707538,-9.263460,5.869259,-8.462250,8.265479,5.645469,1.504453,-8.113255,-4.770088,-4.775224,2.796032,-2.751624,-3.867093,0.033102,9.036425,-5.935204,-0.384542,-5.049879,-4.279432,9.504282,2.854850,5.504943,9.050031,-2.679408,-6.380194,4.998320,-5.023167,9.868358,5.373739,3.182501,5.782260,9.454466,-6.392794,5.364591,-1.919926,9.588389,8.459140,6.473650,-5.675665,-9.226294,-4.295877,-5.764925,-8.906545,-5.901699,-3.499508,-3.498888,9.441839,-3.428424,-1.362885,-9.139647,-5.322693,-2.520803,6.467486,-6.575116,2.756218,-0.473373,-5.769807,-6.006674,8.339164,-9.296371,7.211881,9.350651,7.112464,-5.681690,8.727173,-9.529955,-4.595912,-3.380193,-1.877086,3.522715,2.323962,-6.517817,8.346575,-7.747755,6.892110,-2.246231,-5.504413,7.695088,2.231285,1.641876,7.718169,-3.705973,-0.148424,8.704613,4.135560,-2.854577,-0.692736,-1.599016,-2.913773,-1.215515,-5.671845,-9.611043,-3.303540,-8.529873,2.088360,0.931348,1.351211,2.839145,-2.715366,2.907792,0.836149,-9.084407,-5.399866,5.313451,-8.116042,-6.337874,4.007170,1.537372,-8.390757,5.524785,0.680538,-4.674287,7.862356,-6.662038,-4.404368,5.143899,2.597634,-0.088490,5.984606,-6.566277,3.631011,-6.931521,6.147910,3.292726,0.169285,-7.569182,7.275608,3.224329,-9.181292,-5.663936,7.436538,-0.007598,8.930146,-8.364167,1.820692,-2.392489,9.754053,5.952339,-7.361034,5.898401,5.249129,-1.850210,-6.613459,7.565953,2.770250,-8.666682,-4.980681,-7.570454,9.165452,-2.602582,6.560526,7.623034,6.404781,-1.593049,0.396629,2.454052,6.483024,6.112983,2.198484,-9.595949,-5.875138,-1.560734,9.655285,6.048106,6.815564,8.222881,-0.774584,-9.615505,8.785763,-1.940915,-2.403123,-7.519121,3.617781,7.774653,-0.999560,-4.148121,-3.003641,5.331491,8.239688,-2.143261,-0.728976,7.400573,3.137679,-3.344348,-5.742873,2.806657,-9.818412,-7.403982,-3.718958,1.883457,4.777549,9.371370,-7.797396,-3.968468,2.513135,-7.229770,-5.024312], dtype = "float64")#candidate|12293|(1176,)|const|float64
call_12292 = relay.TupleGetItem(func_8720_call(relay.reshape(const_12293.astype('float64'), [14, 12, 7]), relay.reshape(const_12293.astype('float64'), [14, 12, 7]), ), 0)
call_12294 = relay.TupleGetItem(func_8723_call(relay.reshape(const_12293.astype('float64'), [14, 12, 7]), relay.reshape(const_12293.astype('float64'), [14, 12, 7]), ), 0)
func_5673_call = mod.get_global_var('func_5673')
func_5678_call = mutated_mod.get_global_var('func_5678')
var_12302 = relay.var("var_12302", dtype = "float64", shape = (160,))#candidate|12302|(160,)|var|float64
var_12303 = relay.var("var_12303", dtype = "int64", shape = ())#candidate|12303|()|var|int64
const_12304 = relay.const([2.378822,5.208234,5.808624,3.982082,2.240326,-4.760579,-7.358196,-1.519690,3.660651,0.871572,2.651309,-2.814040,4.795560,6.926143,-4.601835,-8.035218,1.914606,-6.291792,-6.415454,-0.176330,7.605118,-1.045997,9.738074,5.414985,-8.812931,-6.211821,-1.374417,6.684322,3.259896,8.987783,4.996793,6.133014,1.307331,6.617954,-2.055911,0.628076,-6.970806,0.947133,-8.826706,4.774566,8.943561,-0.658377,-8.783655,7.187993,4.627685,0.742255,8.233473,3.589194,0.740094,-0.071770,-6.401021,0.273745,2.861381,9.009454,0.040746,6.063735,-4.791656,2.355118,8.938315,2.920235,1.181829,0.952669,8.959742,6.773463,9.722466,-9.484229,5.391707,-3.808507,7.166799,3.587241,-1.613060,0.760663,-8.412290,-4.710122,-9.009947,-5.834783,-0.834732,-0.135310,0.199975,-3.580160,1.048822,-5.052694,5.526965,7.832369,-2.665557,4.593138,3.109821,-7.648821,9.770429,0.924981,-5.243912,7.049699,2.503100,-3.804301,7.667584,8.667378,-1.019087,-2.870089,4.763234,-5.438955,-3.296234,-6.041222,-1.162783,6.754580,6.849166,2.542974,6.169912,6.020972,-7.698768,4.958265,-5.204378,-0.937500,-3.418059,-2.211606,0.524077,-0.737671,9.004205,6.160696,2.852185,0.693159,-0.404887,-2.728478,-6.924379,-9.430261,7.241560,-7.094834,5.199122,-5.175484,8.767391,1.040476,7.086297,-5.668614,-6.632339,0.467867,6.765704,1.289376,9.427803,0.974426,4.267400,0.593751,1.191679,-6.106938,-8.733539,-1.634393,-8.319440,-5.628037,8.224182,-3.349620,2.511670,2.106616,-0.334003,-3.638774,-6.167016,5.109483,0.774868,9.449507,1.366953,9.865443,-1.651112,0.800408,0.245286,5.371658,9.528137,3.643235,5.094931,0.909034,1.638327,0.573898,5.143245,3.286435,6.407573,3.412292,-8.088197,0.779666,-2.582649,2.344647,-5.021752,3.138255,-3.031181,-0.586650,7.701986,-5.974768,8.848204,4.834069,-0.189046,-0.103410,6.686325,-1.824311,-3.181430,-9.246225,5.023444,2.929896,-9.525238,8.165882,9.526925,-6.292913,0.454969,4.618845,6.997712,0.339218,2.327494,4.941758,4.224572,-9.840950,4.609348,-8.632516,6.990719,6.375245,-0.140029,-2.164773,-6.470981,6.269709,5.678043,3.636463,9.416228,5.236040,-6.432012,4.134388,-9.083270,4.510314,-5.481487,-1.634991,5.791394,-1.754246,-9.236194,1.184402,5.145322,-2.802593,8.710063,6.078467,-0.268695,7.048762,-2.637394,-2.940687,1.932441,-8.218295,-4.370934,7.040881,-9.773193,4.831030,-3.952405,-5.849402,0.264965,1.819917,-7.847712,3.715639,2.618534,4.022650,9.762759,-9.942997,5.739299,3.812571,-8.796403,-2.424085,-7.352120,8.923513,-8.647470,-9.303258,6.694484,3.016114,2.731111,-5.942917,5.827532,-2.874488,-9.159546,1.153561,7.988725,2.126563,6.588822,1.517015,2.472336,5.304368,-5.373427,-7.523634,2.927915,6.413845,-2.478898,2.969979,7.485309,5.329835,-2.803820,8.308825,8.303709,3.057505,-1.909842,-7.614197,-0.590015,-2.454754,9.989414,-2.717578,-1.424374,4.705799,4.684463,-1.850246,-3.392448,-9.294098,9.069471,5.297437,-1.417118,6.136846,4.460497,8.241452,0.308776,-2.546935,-9.374373,3.069713,-0.035287,0.174636,9.900532,-8.619419,0.611232,0.175651,-8.571924,5.781902,7.402442,-2.282790,-5.598224,-7.904737,3.166290,9.115306,7.604767,-1.743191,4.282704,-3.408363,7.760094,2.674995,7.272104,0.655315,2.057114,7.309814,-2.038242,4.197892,3.533602,-3.311175,-0.561273,-5.777509,9.036027,8.841669,-3.542599,2.040763,-7.655283,3.762406,5.500416,9.268187,1.613737,-7.667668,-9.821484,5.208640,2.967352,-5.146882,7.764164,-1.343673,6.852161,9.803676,4.675345,-3.682343,2.031619,7.671820,-0.493108,9.080071,9.938195,9.622743,1.420793,3.626766,3.645033,-6.136343,-1.911981,4.490350,-9.328949,-6.449521,2.937149,5.248691,-7.926912,-4.897441,-1.022323,-3.509533,5.604286,2.928705,-2.711462,2.567311,6.156360,-2.547792,-1.001388,5.776154,4.351281,-1.431696,-8.729949,9.555289,2.120856,-2.193224,-4.582283,7.169288,-0.729306,-6.455441,-3.381809,-1.351644,-5.375809,3.655517,-4.282667,7.318613,-9.671717,9.830411,-1.055390,8.107800,-3.368442,5.832350,2.531939,-6.999770,8.389972,-6.196503,-0.821040,6.580532,-6.866826,-4.663570,-5.448295,-3.677497,9.880335,5.963219,-3.501940,3.485041,-4.630674,7.276235,-8.780387,-6.184950,5.487429,5.941543,8.136383,-9.070566,5.268654,2.744842,-3.868021,0.059414,3.525767,4.638639,9.521907,-2.123410,2.019847,3.580327,6.216805,-3.342569,5.750543,-6.648187,-6.683112,-0.948413,5.765854,3.226805,2.446675,-1.347127,-9.896483,-5.521432,-4.790840,0.358123,0.929132,3.395394,-2.019989,4.666551,4.170979,2.790524,-4.034083,-4.688898,2.252693,6.952073,-8.574413,0.995172,-8.433580,-1.242323,-2.704602,-5.823251,9.031851,-7.570881,3.747669,4.215114,8.166246,7.567016,-9.592005,-0.803558,8.265452,-1.681128,1.470627,-6.344314,9.157713,-7.938419,0.490219,1.022499,9.930024,-1.750296,9.329889,8.293213,-7.790261,-5.353296,-4.684922,-1.452063,2.336838,2.567681,-2.630829,-6.488364,4.356626,9.253053,9.672899,7.614263,-6.384726,-1.072743,6.473702,6.264292,-8.468332,-9.254112,-1.877146,-0.080919,5.727594,-2.722961,-0.796377,6.268807,9.151618,-0.669095,-5.301230,4.556208,7.775229,-1.992667,-6.170631,0.962412,-6.069812,7.929510,-2.549594,-6.624720,-8.434995,-9.039189,4.553910,-7.994106,-2.215509,0.207260,-3.903650,-9.361803,-8.240790,-0.344602,-1.302603,1.588884,2.261055,4.012599,9.069341,4.750182,-1.790175,-5.900659,2.123536,-8.940192,5.656188,-8.516859,7.893430,9.285801,-7.049393,-3.645739,1.686790,6.136933,-4.240170,0.064021,-1.234624,0.630014,-1.224726,-0.111374,-1.722489,4.538234,-9.344067,4.659379,-5.301726,-2.589693,-6.390850,1.916611,-4.027988,-3.622962,7.868548,-7.375188,-1.266569,-5.576580,7.197410,9.280564,-0.956463,0.777948,-5.809060,-2.945563,-3.259126,9.679916,2.874583,-1.166827,1.102753,-5.166938,-8.079930,-0.639736,7.688073,0.829237,9.597823,-1.349295,-5.676965,0.191749,7.572750,4.978242,-2.845852,-5.995667,-5.454870,7.638861,-5.958819,-3.386531,4.951354,3.709537,-2.903032,0.485702,0.517247,5.696064,-4.679124,6.881998,-2.795666,0.409294,3.599130,-2.126270,-9.386895,-2.122458,8.270895,-6.099953,7.711332,9.115601,-6.541834,-1.913251,4.790401,8.232525,-7.986177,6.882616,-2.318906,3.862719,-9.963658,3.090922,8.785704,6.033147,-3.451773,5.958518,-1.458525,8.666119,-6.181554,-9.832194,7.159115,6.705301,-6.959029,-8.738161,1.266791,7.021046,2.278864,-7.373428,-3.133126,-8.673199,4.677276,-2.522291,-2.899526,2.803551,2.546397,-9.976821,8.110733,-8.399936,-3.023168,-7.440376,-8.013101,-9.501352,-1.275292,8.662904,-0.698806,-7.568093,3.255127,0.366157,-0.155751,-7.297346,3.577123,4.924601,-0.690149,-5.327653,-7.205199,-5.029020,-2.294467,6.213166,-3.324140,1.057406,-2.669686,-3.518016,7.839415,3.707313,-2.620828,9.469441,4.086097,5.599453,7.784783,-8.407815,-8.067108,-8.961977,2.716210,-5.869846,-1.704790,5.323812,1.220705,0.647518,5.603244,-1.709108,-2.622628,8.257823,-8.834620,-3.095640,0.318268,-3.359762,0.509027,-0.003050,-8.793016,-2.643509,2.166300,7.342773,-9.934602,5.515814,5.366735,1.235118,9.405656,1.129231,0.396550,3.583000,9.227109,6.678722,6.187520,0.678801,-7.608392,-4.896890,1.943966,-3.880050,-0.891902,-1.122773,8.157124,-3.112570,-0.731433,7.687122,9.746536,-9.072661,-2.475071,7.286018,-9.201631,8.597234,1.392973,-5.463593,7.174459,-0.601091,-2.557968,0.464208,-5.260394,-6.354897,-9.927669,4.971203,5.629102,-2.260499,4.611352,8.377715,-7.711129,-5.162768,-2.766543,6.220505,0.678043,-4.563163,-5.115259,7.912214,9.647901,4.768046,5.961736,8.630376,7.867112,-2.203848,3.920244,-1.597945,-7.309542,0.971324,1.149750,-0.915381,-9.054269,-3.687069,3.477885,-6.194729,8.606164,-4.547196,-2.325482,1.878178,6.121141,-0.846951,0.679158,-9.997407,7.343991,3.813768,-2.169788,3.882993,-7.767642,8.704477,7.638443,-3.720813,-5.449987,-6.508011,-2.702457,-7.523525,4.824562,-3.930482,4.424921,4.453529,7.003104,9.415633,-7.930141,-7.838400,-7.298567,-9.551223,1.229356,-0.557927,6.373241,-7.575779,9.136340,5.931015,1.508782,3.428441,0.398499,7.979101,3.479629,-6.767634,7.646748,-6.037964,2.541616,-1.755931,0.899567,-3.944881,8.901632,-8.479084,2.779303,5.210143,-3.052975,8.993967,2.023172,-7.130076,2.561174,9.385500,5.052318,-3.305000,-0.619878,-8.119794,0.683503,2.201070,1.036995,5.059121,0.233600,-9.624962,-6.253072,9.910216,-3.995562,-5.549536,4.482411,2.275863,-2.014739,6.045177,-1.398989,-0.796644,-1.133672,-3.100547,-4.193763,-0.406055,-1.876518,5.401338,-2.618646,1.658191,-5.599074,-0.343849,7.098675,-4.745592,4.150610,-6.478447,8.331137,9.083024,-2.397652,-9.591062,-2.272254,1.865228,0.507199,4.101440,2.858389,-6.844461,-4.495305,6.521558,-0.083092,6.184862,8.025303,0.272270,2.657935,-2.338840,-6.091507,-3.032396,8.291061,-1.501390,-5.715712,-5.135758,-4.326447,1.969779,6.198599,-5.413010,-4.407972,4.244551,0.167580,8.883137,-0.501096,7.048264,-3.099320,6.351652,3.796921,-9.030255,9.303186,8.156274,0.404013,-5.121154,-5.598624,7.375092,2.220380,-7.342719,2.240009,6.392010,-5.551482,8.710568,-1.634686,-2.801564,-5.215750,1.109562,-3.528346,4.299491,8.112636,-4.472998,-1.767539,-6.244514,2.509229,-1.593936,-8.603991,-9.476694,-2.608706,9.756743,-7.753328,-7.050862,-7.015480,-2.351003,8.868819,9.927741,6.136010,-7.699655,2.080947,9.315522,4.055946,9.759269,9.009851,-7.060174,8.931541,-2.701057,-0.172179,-1.927867,-4.941888,8.371167,-5.615953,-3.923805,-8.971961,3.062442,-8.401250,-7.371859,1.953058,9.143374,1.359329,-7.074756,-8.130025,-1.481457,-7.821095,0.310259,5.796237,-4.769458,4.730297,-2.857889,4.497061,3.933596,-0.072754,3.092581,-6.169414,7.487262,3.503312,-8.478044,-1.495152,-1.067540,-3.739334,-1.509778,-4.490008,6.872301,8.982650,4.955894,-4.167535,-4.116507,3.156570,-0.988733,4.669146,1.777544,3.877611,-4.278565,9.620828,-0.184939,-2.451724,7.579772,1.000369,0.260731,-5.557802,7.603365,9.744370,-7.438433,-2.103045,-5.782644,-0.014893,-0.147127,-1.434090,5.057370,5.459720,3.710230,-8.290933,-4.245810,8.921874,0.046490,-3.951687,-8.652008,-9.686500,-4.523202,5.657594,-1.333873,6.427327,-0.388407,2.643573,8.308952,6.442308,1.009213,7.751465,-7.560466,9.204405,7.820942,-6.092798,7.450399,-9.043480,0.432215,9.795503,4.772048,-8.814577,-8.669530,4.983877,-7.934603,-6.020050,5.706360,8.065024,-9.111172,3.936378,9.724012,-7.322513,-2.322223,-6.961985,-0.883782,-7.039373,-8.021713,9.278710,-3.768788,-3.871961,-5.055460,-5.668660,8.812529,4.245263,-9.417107,7.757517,-7.860900,1.601734,-2.176434,2.203616,9.007898,-5.470790,-3.608511,-0.665455,-5.240339,-4.014963,9.602508,-5.873541,-0.466364,-5.979344,-7.366721,-1.824235,2.182483,-2.121392,-3.293688,2.373673,8.598243,6.623312,6.460616,-0.428538,5.305785,-3.280365,-0.625517,3.449856,-1.646427,5.669958,8.911770,-2.190812,9.056247,-1.393196,-6.718564,4.703646,1.601670,4.307263,-8.847161,-6.859602,-1.762898,-7.407501,-1.268212,-1.443458,-3.664265,8.475565,5.720121,-5.079588,-7.890692,-3.013631,-5.013675,-3.465891,0.823844,9.247342,-0.865421,3.868118,-7.902851,8.624747,7.783552,-8.736875,0.628388,4.190492,5.937787,-6.600318,-6.093936,-7.989207,-6.096653,-1.950414,-5.378249,-1.415711,8.596327,-8.025051,3.286718,-0.945728,5.397539,-2.847763,2.352211,4.810004,-6.693679,-2.377376,7.313515,2.336533,-8.538976,3.397501,5.665223,2.356446,8.489071,7.063856,6.072095,4.519999,-4.666911,9.501556,4.974759,-0.149461,-9.976847,-3.426940,9.247358,-4.975984,9.926111,-4.551847,8.850419,7.301446,1.973822,4.480182,9.691679,5.833250,2.525211,9.042925,-4.645446,-3.328215,-1.981203,-2.857676,-5.178274,5.896315,-7.693600,8.075542,4.892987,-6.333130,5.263075,7.649116,-1.117809,-9.208153,-1.517758,-0.730767,4.160251,2.192341,3.377159,5.290380,-5.186880,0.136395,-2.144982,-7.554705,8.459882,5.783875,7.182866,1.325503,0.746616,6.271494,3.717702,-0.920293,-0.764824,1.094482,4.127119,0.842631,2.791029,-2.991094,4.698884,-5.308029,9.958267,4.114419,-2.313695,-4.177561,-6.388413,0.151183,2.897646,-3.364925,-6.282509,4.496539,-6.430166,5.368841,0.159608,-0.582184,5.307200,-6.554409,-9.607287,5.630389,-4.866215,-9.280689,1.960165,7.567872,-1.260244,-5.344116,4.753145,-1.821632,-1.530898,4.906411,-0.127203,7.661198,-6.992440,-7.815597,8.063032,-9.615289,-7.480962,1.232266,-4.794556,-9.303744,-0.648917,9.660481,0.120585,-4.474292,-3.247243,9.171394,5.183312,-9.698314,-1.523991,-0.245361,-5.710658,-5.262906,4.125662,-2.261840,-6.909300,-0.033066,4.061505,-0.014040,-8.722452,-2.905723,-8.420080,4.144481,-4.278669,-5.480163,-4.396442,3.244621,1.123472,6.400260,5.080663,-8.809229,0.688893], dtype = "float64")#candidate|12304|(1280,)|const|float64
var_12305 = relay.var("var_12305", dtype = "uint64", shape = (60,))#candidate|12305|(60,)|var|uint64
call_12301 = relay.TupleGetItem(func_5673_call(relay.reshape(var_12302.astype('float64'), [5, 2, 16]), relay.reshape(var_12303.astype('int64'), []), relay.reshape(const_12304.astype('float64'), [1280,]), relay.reshape(var_12305.astype('uint64'), [30, 2]), ), 4)
call_12306 = relay.TupleGetItem(func_5678_call(relay.reshape(var_12302.astype('float64'), [5, 2, 16]), relay.reshape(var_12303.astype('int64'), []), relay.reshape(const_12304.astype('float64'), [1280,]), relay.reshape(var_12305.astype('uint64'), [30, 2]), ), 4)
output = relay.Tuple([call_12268,call_12292,const_12293,call_12301,var_12302,var_12303,const_12304,var_12305,])
output2 = relay.Tuple([call_12269,call_12294,const_12293,call_12306,var_12302,var_12303,const_12304,var_12305,])
func_12310 = relay.Function([var_12302,var_12303,var_12305,], output)
mod['func_12310'] = func_12310
mod = relay.transform.InferType()(mod)
var_12311 = relay.var("var_12311", dtype = "float64", shape = (160,))#candidate|12311|(160,)|var|float64
var_12312 = relay.var("var_12312", dtype = "int64", shape = ())#candidate|12312|()|var|int64
var_12313 = relay.var("var_12313", dtype = "uint64", shape = (60,))#candidate|12313|(60,)|var|uint64
output = func_12310(var_12311,var_12312,var_12313,)
func_12314 = relay.Function([var_12311,var_12312,var_12313,], output)
mutated_mod['func_12314'] = func_12314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10653_call = mod.get_global_var('func_10653')
func_10654_call = mutated_mod.get_global_var('func_10654')
call_12325 = func_10653_call()
call_12326 = func_10653_call()
func_9475_call = mod.get_global_var('func_9475')
func_9476_call = mutated_mod.get_global_var('func_9476')
call_12328 = relay.TupleGetItem(func_9475_call(), 2)
call_12329 = relay.TupleGetItem(func_9476_call(), 2)
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
var_12331 = relay.var("var_12331", dtype = "bool", shape = (2, 504))#candidate|12331|(2, 504)|var|bool
call_12330 = func_1619_call(relay.reshape(var_12331.astype('bool'), [14, 6, 12]), relay.reshape(var_12331.astype('bool'), [14, 6, 12]), )
call_12332 = func_1619_call(relay.reshape(var_12331.astype('bool'), [14, 6, 12]), relay.reshape(var_12331.astype('bool'), [14, 6, 12]), )
func_8502_call = mod.get_global_var('func_8502')
func_8506_call = mutated_mod.get_global_var('func_8506')
var_12337 = relay.var("var_12337", dtype = "uint64", shape = (60,))#candidate|12337|(60,)|var|uint64
var_12338 = relay.var("var_12338", dtype = "int64", shape = ())#candidate|12338|()|var|int64
const_12339 = relay.const([4.415016,-1.637585,-0.125858,-6.028498,2.762409,-1.046644,8.847365,-0.324146,-1.087965,-5.262618,7.216756,8.674007,6.232261,-3.188600,-1.675139,0.291914,-5.266775,4.846314,-3.383951,-6.372955,-6.612985,-7.273713,-5.395997,0.242918,1.428299,2.554930,-8.186196,4.594659,9.563828,-0.063605,-7.765050,5.632091,8.557897,9.177867,-1.302454,-0.703366,6.541377,-3.818735,8.026830,-4.911982,3.995779,-8.516765,-4.543601,2.681915,0.662694,3.997479,-7.456252,-5.254027,1.166750,1.201650,-1.896773,-4.938826,-0.220330,7.431070,-6.565938,-0.897114,1.121080,8.374265,3.801184,7.750221,-8.320109,-2.015630,3.993873,4.372582,-0.497870,8.865463,-3.488056,-0.425005,-6.798718,-1.841577,0.595590,6.166080,0.526292,-3.098999,6.161637,9.972971,-9.828526,-0.160623,9.670291,-7.331892,-2.220602,-2.072973,3.411608,5.447028,-5.093306,-6.986132,1.492344,-0.164847,-6.698580,3.435494,6.406038,-4.848704,-7.964068,4.507612,-9.928029,6.222575,6.952230,0.374951,4.212594,8.733683,-5.300220,1.158598,5.956278,0.932470,7.544821,5.512842,7.385392,-1.771009,7.690797,5.355329,-6.889324,-6.046891,-6.003432,-7.816055,4.961841,6.539116,-9.998730,3.238767,7.590896,1.265287,9.959320,8.871342,-5.965930,-3.373924,9.408082,5.658715,-8.512967,-1.711945,3.843065,-1.029673,-4.570441,6.525991,0.654053,-9.409233,6.700530,8.838049,-4.882364,4.507759,-6.371924,-4.768450,-6.239547,2.036851,-3.181874,1.822997,5.309636,-8.531602,-4.080109,-8.637534,-4.031875,-6.121075,-1.671706,-4.879193,-8.950813,-5.343360,9.479731,-7.312136,-1.247313,-9.504814,9.527977,5.857821,-2.398311,-8.859521,6.350843,-1.535092,8.980628,3.937953,-7.041134,0.406130,5.996730,4.623059,-9.361589,-1.928787,-4.803094,9.413125,6.988880,-7.249045,-5.204944,-8.974733,2.070922,1.246294,9.662824,-0.418636,-6.452509,-3.616335,5.005709,-6.954474,7.643298,5.757492,-5.717000,-9.650895,7.992767,9.845139,3.910576,7.564634,-3.405012,-1.933937,7.249386,6.807068,-9.703068,6.089396,8.526331,3.985723,5.572177,-9.698355,-6.789596,0.985405,8.798054,9.834327,-6.846517,3.272390,-9.759479,-7.712023,8.247558,0.881657,9.787432,5.204298,0.378797,7.412447,1.878847,-4.379813,-9.601585,6.782920,-1.022401,2.702554,8.188928,6.210093,-0.221841,2.449503,0.519895,5.429615,-7.094639,7.517754,2.288756,-3.945259,6.089281,-6.253226,-2.244770,9.961729,2.882759,4.243227,-2.731812,-3.721429,-6.791820,-2.578596,-5.645200,-4.186914,-5.944855,-6.694805,-8.416526,6.034838,6.927826,-9.528523,3.910543,-8.010121,-8.100841,-0.411121,-9.842619,7.023861,-1.527039,-0.329226,4.816522,2.275348,6.378395,1.385191,-5.216648,3.920198,6.380816,4.158167,4.783736,8.164544,8.154064,-8.400005,-3.305259,-0.927008,1.365811,5.487422,7.854422,4.464009,0.996390,1.037724], dtype = "float32")#candidate|12339|(280,)|const|float32
call_12336 = relay.TupleGetItem(func_8502_call(relay.reshape(var_12337.astype('uint64'), [60,]), relay.reshape(var_12338.astype('int64'), []), relay.reshape(const_12339.astype('float32'), [140, 2]), ), 11)
call_12340 = relay.TupleGetItem(func_8506_call(relay.reshape(var_12337.astype('uint64'), [60,]), relay.reshape(var_12338.astype('int64'), []), relay.reshape(const_12339.astype('float32'), [140, 2]), ), 11)
output = relay.Tuple([call_12325,call_12328,call_12330,var_12331,call_12336,var_12337,var_12338,const_12339,])
output2 = relay.Tuple([call_12326,call_12329,call_12332,var_12331,call_12340,var_12337,var_12338,const_12339,])
func_12343 = relay.Function([var_12331,var_12337,var_12338,], output)
mod['func_12343'] = func_12343
mod = relay.transform.InferType()(mod)
var_12344 = relay.var("var_12344", dtype = "bool", shape = (2, 504))#candidate|12344|(2, 504)|var|bool
var_12345 = relay.var("var_12345", dtype = "uint64", shape = (60,))#candidate|12345|(60,)|var|uint64
var_12346 = relay.var("var_12346", dtype = "int64", shape = ())#candidate|12346|()|var|int64
output = func_12343(var_12344,var_12345,var_12346,)
func_12347 = relay.Function([var_12344,var_12345,var_12346,], output)
mutated_mod['func_12347'] = func_12347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10047_call = mod.get_global_var('func_10047')
func_10048_call = mutated_mod.get_global_var('func_10048')
call_12388 = func_10047_call()
call_12389 = func_10047_call()
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_12415 = func_7344_call()
call_12416 = func_7344_call()
uop_12430 = relay.sigmoid(call_12388.astype('float64')) # shape=(10, 7, 8)
uop_12432 = relay.sigmoid(call_12389.astype('float64')) # shape=(10, 7, 8)
var_12441 = relay.var("var_12441", dtype = "float64", shape = (10, 7, 8))#candidate|12441|(10, 7, 8)|var|float64
bop_12442 = relay.not_equal(uop_12430.astype('bool'), relay.reshape(var_12441.astype('bool'), relay.shape_of(uop_12430))) # shape=(10, 7, 8)
bop_12445 = relay.not_equal(uop_12432.astype('bool'), relay.reshape(var_12441.astype('bool'), relay.shape_of(uop_12432))) # shape=(10, 7, 8)
func_7999_call = mod.get_global_var('func_7999')
func_8004_call = mutated_mod.get_global_var('func_8004')
var_12450 = relay.var("var_12450", dtype = "uint32", shape = (96, 12))#candidate|12450|(96, 12)|var|uint32
var_12451 = relay.var("var_12451", dtype = "bool", shape = (1008,))#candidate|12451|(1008,)|var|bool
const_12452 = relay.const([8,-2,-2,10,1,-2,-5,-5,10,3,-6,-2,5,-2,-6,6,2,-3,-7,4,8,4,3,-10,-5,-8,5,9,5,-6,8,-5,2,-5,-10,10,-8,-3,-4,-5,10,-3,-5,-7,-2,1,7,-10,-5,-9,-5,7,3,-6,5,-7,-3,9,3,-10,1,6,-9,-8,-3,-9,7,-4,6,-7,-9,5,5,2,2,-2,3,-2,6,5,8,-10,10,3,-1,-6,-7,4,6,9,-8,-2,10,-3,3,-6,4,6,-9,1,-1,10,-7,-9,8,3,-10,-9,7,1,-2,1,-2,-9,5,-10,-6,-4,3,-7,1,1,5,6,-1,-1,3,-8,-10,5,-6,4,5,8,1,-1,5,6,1,1,-10,-5,-8,-7,10,8,8,10,1,-3,3,-7,-7,10,6,10,-8,8,-7,-4,8,3,-3,-1,-10,7,10,6,6,5,-9,-7,-1,-1,-9,-3,9,2,10,-6,-10,6,8,7,-7,-7,9,-3,8,-1,3,3,2,3,1,-2,6,-10,7,-8,10,-3,9,3,4,-4,8,8,-5,1,4,-8,9,-7,-3,-5,10,6,-5,-7,-1,-5,-10,-10,-8,2,4,4,-8,-2,-6,6,6,-7,10,-10,-7,-9,-2,4,10,1,8,9,-6,8,9,-8,-7,6,1,8,2,4,8,1], dtype = "uint64")#candidate|12452|(256,)|const|uint64
call_12449 = relay.TupleGetItem(func_7999_call(relay.reshape(var_12450.astype('uint32'), [1152,]), relay.reshape(var_12451.astype('bool'), [1008,]), relay.reshape(const_12452.astype('uint64'), [256,]), ), 5)
call_12453 = relay.TupleGetItem(func_8004_call(relay.reshape(var_12450.astype('uint32'), [1152,]), relay.reshape(var_12451.astype('bool'), [1008,]), relay.reshape(const_12452.astype('uint64'), [256,]), ), 5)
output = relay.Tuple([call_12415,bop_12442,call_12449,var_12450,var_12451,const_12452,])
output2 = relay.Tuple([call_12416,bop_12445,call_12453,var_12450,var_12451,const_12452,])
func_12464 = relay.Function([var_12441,var_12450,var_12451,], output)
mod['func_12464'] = func_12464
mod = relay.transform.InferType()(mod)
mutated_mod['func_12464'] = func_12464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12464_call = mutated_mod.get_global_var('func_12464')
var_12466 = relay.var("var_12466", dtype = "float64", shape = (10, 7, 8))#candidate|12466|(10, 7, 8)|var|float64
var_12467 = relay.var("var_12467", dtype = "uint32", shape = (96, 12))#candidate|12467|(96, 12)|var|uint32
var_12468 = relay.var("var_12468", dtype = "bool", shape = (1008,))#candidate|12468|(1008,)|var|bool
call_12465 = func_12464_call(var_12466,var_12467,var_12468,)
output = call_12465
func_12469 = relay.Function([var_12466,var_12467,var_12468,], output)
mutated_mod['func_12469'] = func_12469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_12499 = relay.TupleGetItem(func_11617_call(), 1)
call_12500 = relay.TupleGetItem(func_11618_call(), 1)
func_9637_call = mod.get_global_var('func_9637')
func_9639_call = mutated_mod.get_global_var('func_9639')
call_12519 = func_9637_call()
call_12520 = func_9637_call()
func_11986_call = mod.get_global_var('func_11986')
func_11988_call = mutated_mod.get_global_var('func_11988')
call_12521 = func_11986_call()
call_12522 = func_11986_call()
output = relay.Tuple([call_12499,call_12519,call_12521,])
output2 = relay.Tuple([call_12500,call_12520,call_12522,])
func_12534 = relay.Function([], output)
mod['func_12534'] = func_12534
mod = relay.transform.InferType()(mod)
output = func_12534()
func_12535 = relay.Function([], output)
mutated_mod['func_12535'] = func_12535
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12557 = relay.var("var_12557", dtype = "float64", shape = (1, 10, 1))#candidate|12557|(1, 10, 1)|var|float64
uop_12558 = relay.asinh(var_12557.astype('float64')) # shape=(1, 10, 1)
func_8977_call = mod.get_global_var('func_8977')
func_8978_call = mutated_mod.get_global_var('func_8978')
call_12565 = relay.TupleGetItem(func_8977_call(), 0)
call_12566 = relay.TupleGetItem(func_8978_call(), 0)
uop_12569 = relay.rsqrt(uop_12558.astype('float64')) # shape=(1, 10, 1)
func_10987_call = mod.get_global_var('func_10987')
func_10990_call = mutated_mod.get_global_var('func_10990')
var_12578 = relay.var("var_12578", dtype = "float32", shape = (2160,))#candidate|12578|(2160,)|var|float32
call_12577 = func_10987_call(relay.reshape(var_12578.astype('float32'), [16, 9, 15]))
call_12579 = func_10987_call(relay.reshape(var_12578.astype('float32'), [16, 9, 15]))
var_12585 = relay.var("var_12585", dtype = "float64", shape = (8, 10, 15))#candidate|12585|(8, 10, 15)|var|float64
bop_12586 = relay.maximum(uop_12569.astype('float32'), var_12585.astype('float32')) # shape=(8, 10, 15)
bop_12591 = relay.left_shift(uop_12569.astype('int8'), bop_12586.astype('int8')) # shape=(8, 10, 15)
output = relay.Tuple([call_12565,call_12577,var_12578,bop_12591,])
output2 = relay.Tuple([call_12566,call_12579,var_12578,bop_12591,])
func_12595 = relay.Function([var_12557,var_12578,var_12585,], output)
mod['func_12595'] = func_12595
mod = relay.transform.InferType()(mod)
var_12596 = relay.var("var_12596", dtype = "float64", shape = (1, 10, 1))#candidate|12596|(1, 10, 1)|var|float64
var_12597 = relay.var("var_12597", dtype = "float32", shape = (2160,))#candidate|12597|(2160,)|var|float32
var_12598 = relay.var("var_12598", dtype = "float64", shape = (8, 10, 15))#candidate|12598|(8, 10, 15)|var|float64
output = func_12595(var_12596,var_12597,var_12598,)
func_12599 = relay.Function([var_12596,var_12597,var_12598,], output)
mutated_mod['func_12599'] = func_12599
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10383_call = mod.get_global_var('func_10383')
func_10384_call = mutated_mod.get_global_var('func_10384')
call_12603 = func_10383_call()
call_12604 = func_10383_call()
var_12608 = relay.var("var_12608", dtype = "float32", shape = (550,))#candidate|12608|(550,)|var|float32
bop_12609 = relay.subtract(call_12603.astype('int8'), relay.reshape(var_12608.astype('int8'), relay.shape_of(call_12603))) # shape=(550,)
bop_12612 = relay.subtract(call_12604.astype('int8'), relay.reshape(var_12608.astype('int8'), relay.shape_of(call_12604))) # shape=(550,)
bop_12622 = relay.divide(var_12608.astype('float32'), relay.reshape(call_12603.astype('float32'), relay.shape_of(var_12608))) # shape=(550,)
bop_12625 = relay.divide(var_12608.astype('float32'), relay.reshape(call_12604.astype('float32'), relay.shape_of(var_12608))) # shape=(550,)
func_10490_call = mod.get_global_var('func_10490')
func_10492_call = mutated_mod.get_global_var('func_10492')
call_12627 = relay.TupleGetItem(func_10490_call(), 0)
call_12628 = relay.TupleGetItem(func_10492_call(), 0)
uop_12638 = relay.rsqrt(bop_12609.astype('float64')) # shape=(550,)
uop_12640 = relay.rsqrt(bop_12612.astype('float64')) # shape=(550,)
output = relay.Tuple([bop_12622,call_12627,uop_12638,])
output2 = relay.Tuple([bop_12625,call_12628,uop_12640,])
func_12651 = relay.Function([var_12608,], output)
mod['func_12651'] = func_12651
mod = relay.transform.InferType()(mod)
var_12652 = relay.var("var_12652", dtype = "float32", shape = (550,))#candidate|12652|(550,)|var|float32
output = func_12651(var_12652)
func_12653 = relay.Function([var_12652], output)
mutated_mod['func_12653'] = func_12653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_12747 = relay.TupleGetItem(func_7653_call(), 0)
call_12748 = relay.TupleGetItem(func_7654_call(), 0)
output = call_12747
output2 = call_12748
func_12750 = relay.Function([], output)
mod['func_12750'] = func_12750
mod = relay.transform.InferType()(mod)
mutated_mod['func_12750'] = func_12750
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12750_call = mutated_mod.get_global_var('func_12750')
call_12751 = func_12750_call()
output = call_12751
func_12752 = relay.Function([], output)
mutated_mod['func_12752'] = func_12752
mutated_mod = relay.transform.InferType()(mutated_mod)
const_12758 = relay.const(3.401094, dtype = "float32")#candidate|12758|()|const|float32
const_12759 = relay.const([[[-2.970638,-8.741875,-7.610183,-5.031450,-5.712864],[-7.567783,3.671451,7.162046,-2.672646,1.460031],[1.811861,8.837855,-1.074256,4.471361,1.133659],[-5.345661,-4.439497,-4.174884,2.827388,7.866723],[-6.847865,8.090448,2.326971,8.408903,9.368288],[9.094769,-6.718594,9.793970,-6.357456,-4.303401],[9.688734,-2.404133,5.644053,-4.597513,0.727704],[-5.797492,-6.850320,1.547067,-4.273676,3.953568],[3.685432,-1.631117,9.748640,3.661453,-8.086309],[-9.160584,-9.536616,-2.792719,8.070515,7.023911],[-1.444600,-2.555352,4.273701,-1.624687,-8.499168],[6.322525,1.403647,0.219186,1.156965,-7.829920],[-9.293754,-9.404088,9.292388,-0.979860,7.675643],[-7.751039,-9.186016,-0.641432,-5.546867,9.867614],[-7.652235,6.604441,9.549477,3.414080,1.142339],[-7.634216,-0.208195,-4.074309,8.055296,-6.887615]],[[-9.210137,4.176730,7.068915,-5.756488,-4.831565],[9.317529,3.288601,-6.215797,2.970539,5.369076],[-5.076252,4.575155,-0.757593,-8.620310,-1.372401],[9.598464,0.821345,8.693705,-8.440441,6.558200],[-0.049835,-4.926654,8.067025,-9.133055,-7.747959],[0.257517,7.988447,3.161998,-0.582470,-8.574028],[-5.496216,-7.431190,-0.197357,-6.429736,7.914743],[1.436749,-6.864208,1.936284,7.737618,5.723815],[-0.092756,-2.581058,5.296656,9.413168,1.954813],[-5.428407,7.650888,-9.807138,8.243483,6.612859],[-9.682497,-4.402532,-6.451815,-2.322792,7.211051],[6.295273,-7.615933,9.832073,4.025311,8.282515],[-0.254739,-8.940409,-7.325834,1.948923,3.830056],[9.173474,-4.777580,9.841156,1.966840,-8.029467],[9.937951,-8.113928,2.643041,8.734540,4.628846],[0.228760,-3.007708,1.359217,-0.380162,-3.327511]],[[5.849773,7.006748,1.822372,-0.489745,-6.414531],[2.090771,-8.124894,2.323802,-1.326243,-7.811726],[-1.888531,5.867412,4.266172,1.987874,-6.136070],[-2.848941,5.646125,2.975205,-2.492666,-0.191398],[-0.327582,-4.919590,0.881724,-1.064907,-7.145881],[0.749559,-8.155626,8.522996,-4.785051,-8.715202],[5.823319,-7.073812,-7.695144,8.619540,-3.272945],[-2.084797,-1.986263,3.948286,-9.861692,8.264877],[0.021111,7.147016,9.441767,7.239607,-6.154262],[-7.217553,-3.782914,-9.847807,-0.935222,5.533884],[0.378451,5.479252,-4.288959,-6.063301,-1.541778],[7.085425,-2.455310,-0.139536,-3.387842,9.052180],[1.724355,-7.405173,2.384958,-2.364733,-9.007734],[-0.960807,5.225002,5.594313,-0.893730,7.218977],[1.407650,-4.463050,8.901220,-7.363457,0.018615],[-9.489370,6.743176,-9.404679,-1.756818,9.796672]],[[8.992891,-2.505289,5.179174,-6.770043,0.362411],[4.109196,3.197094,8.306631,-1.136580,-2.159189],[6.488699,-8.247781,9.654697,0.017079,8.838643],[-7.835029,-6.710928,-2.203945,6.145132,-6.588262],[-4.176901,2.086265,3.165978,-1.687549,-6.505602],[7.022425,-2.156212,1.318255,1.901944,6.254445],[0.563812,0.646525,-4.993833,3.679259,-6.606098],[6.085391,7.632731,-8.307652,5.952414,-4.164813],[7.728725,9.203726,1.090569,2.420896,-4.537273],[-8.534668,5.002490,3.692820,0.661094,5.291994],[-7.888648,-5.713157,5.414010,3.056301,1.268113],[1.784389,6.587137,-2.693638,8.398790,3.028510],[-5.109388,6.053501,5.507970,-3.330682,6.115464],[2.579838,-6.863289,-1.455352,-3.228794,-1.631941],[0.493929,8.642961,-6.818097,-9.809162,7.217197],[2.969165,7.313312,0.168107,-7.243379,7.180338]],[[1.827663,4.454925,-6.042311,-5.021782,1.468829],[-0.315351,-0.790452,-6.310618,-1.529902,-4.461885],[-0.054546,6.435361,-1.470689,4.625773,-6.535323],[-1.004339,9.345777,1.068998,9.727945,-5.176893],[-5.217993,-0.888410,-0.156663,-8.491617,0.286067],[1.062041,-9.019477,7.360685,6.410661,9.387151],[3.059560,-8.824171,-9.557472,-7.502524,7.180261],[-3.725966,5.460247,-5.669438,8.724929,-7.350480],[2.435917,6.208800,4.735723,-2.795406,6.265019],[-2.041879,6.090329,3.088017,3.006910,-1.008470],[-5.534790,-8.358054,7.275419,-1.019340,6.448088],[2.060946,-8.865779,2.934388,1.545869,-0.418400],[1.726744,1.729169,2.063012,-0.929052,-9.019203],[7.390495,-7.132249,-4.109783,-9.173217,-4.857944],[-4.076667,-0.853940,-6.520768,-8.050138,9.840118],[-2.700832,8.274864,-4.660219,-7.531578,1.654314]],[[8.048909,-2.442694,9.271021,2.568948,4.780702],[1.285889,7.901654,-7.427437,2.707593,9.851621],[4.125249,-8.722894,2.126261,-3.964816,1.642393],[-1.748788,-3.623797,-8.828943,1.483321,-2.479540],[-3.732489,-2.957288,8.676772,7.088752,1.646230],[-6.310055,5.439257,-1.750733,9.204224,-4.331626],[-7.763604,6.567776,3.637609,-6.581253,9.860170],[9.952097,1.957166,7.596350,-4.692705,0.946243],[6.012144,8.244542,-2.109124,7.019369,-6.618402],[9.108055,-0.823843,1.295621,-1.725987,-5.387345],[-6.701402,2.335956,-2.061624,1.084204,-2.975449],[-4.242474,-4.164219,-1.321419,5.340884,-8.393402],[7.207976,0.557053,-6.552049,-6.169826,-5.737031],[-6.027553,-6.649461,-5.874048,-2.636777,-4.895480],[0.383253,-6.735029,-8.189463,-7.961023,-6.835177],[9.350028,-1.900098,6.361705,2.320832,-8.073603]]], dtype = "float32")#candidate|12759|(6, 16, 5)|const|float32
bop_12760 = relay.floor_mod(const_12758.astype('float32'), const_12759.astype('float32')) # shape=(6, 16, 5)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_12765 = relay.TupleGetItem(func_8021_call(), 0)
call_12766 = relay.TupleGetItem(func_8022_call(), 0)
func_12140_call = mod.get_global_var('func_12140')
func_12143_call = mutated_mod.get_global_var('func_12143')
const_12800 = relay.const([[-9,-5],[-10,-7],[2,7],[1,-8],[6,7],[-8,-6],[-9,9],[-4,-6],[-5,1],[-7,6],[8,-5],[-9,-8],[-4,5],[-9,-5],[3,2],[8,2],[8,1],[-4,7],[2,-10],[4,4],[-3,8],[-1,-2],[6,4],[1,7],[1,-5],[5,-6],[-3,-6],[4,-4],[10,-1],[-6,9]], dtype = "uint64")#candidate|12800|(30, 2)|const|uint64
call_12799 = relay.TupleGetItem(func_12140_call(relay.reshape(const_12800.astype('uint64'), [60,])), 1)
call_12801 = relay.TupleGetItem(func_12143_call(relay.reshape(const_12800.astype('uint64'), [60,])), 1)
output = relay.Tuple([bop_12760,call_12765,call_12799,const_12800,])
output2 = relay.Tuple([bop_12760,call_12766,call_12801,const_12800,])
func_12839 = relay.Function([], output)
mod['func_12839'] = func_12839
mod = relay.transform.InferType()(mod)
mutated_mod['func_12839'] = func_12839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12839_call = mutated_mod.get_global_var('func_12839')
call_12840 = func_12839_call()
output = call_12840
func_12841 = relay.Function([], output)
mutated_mod['func_12841'] = func_12841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_12946 = relay.TupleGetItem(func_11617_call(), 1)
call_12947 = relay.TupleGetItem(func_11618_call(), 1)
output = relay.Tuple([call_12946,])
output2 = relay.Tuple([call_12947,])
func_12960 = relay.Function([], output)
mod['func_12960'] = func_12960
mod = relay.transform.InferType()(mod)
mutated_mod['func_12960'] = func_12960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12960_call = mutated_mod.get_global_var('func_12960')
call_12961 = func_12960_call()
output = call_12961
func_12962 = relay.Function([], output)
mutated_mod['func_12962'] = func_12962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12839_call = mod.get_global_var('func_12839')
func_12841_call = mutated_mod.get_global_var('func_12841')
call_12993 = relay.TupleGetItem(func_12839_call(), 2)
call_12994 = relay.TupleGetItem(func_12841_call(), 2)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_12999 = relay.TupleGetItem(func_11293_call(), 1)
call_13000 = relay.TupleGetItem(func_11295_call(), 1)
func_8244_call = mod.get_global_var('func_8244')
func_8246_call = mutated_mod.get_global_var('func_8246')
call_13010 = relay.TupleGetItem(func_8244_call(), 2)
call_13011 = relay.TupleGetItem(func_8246_call(), 2)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_13013 = relay.TupleGetItem(func_8021_call(), 0)
call_13014 = relay.TupleGetItem(func_8022_call(), 0)
var_13023 = relay.var("var_13023", dtype = "bool", shape = (504, 2))#candidate|13023|(504, 2)|var|bool
bop_13024 = relay.less(call_13010.astype('bool'), relay.reshape(var_13023.astype('bool'), relay.shape_of(call_13010))) # shape=(504, 2)
bop_13027 = relay.less(call_13011.astype('bool'), relay.reshape(var_13023.astype('bool'), relay.shape_of(call_13011))) # shape=(504, 2)
func_10490_call = mod.get_global_var('func_10490')
func_10492_call = mutated_mod.get_global_var('func_10492')
call_13037 = relay.TupleGetItem(func_10490_call(), 0)
call_13038 = relay.TupleGetItem(func_10492_call(), 0)
output = relay.Tuple([call_12993,call_12999,call_13013,bop_13024,call_13037,])
output2 = relay.Tuple([call_12994,call_13000,call_13014,bop_13027,call_13038,])
func_13041 = relay.Function([var_13023,], output)
mod['func_13041'] = func_13041
mod = relay.transform.InferType()(mod)
mutated_mod['func_13041'] = func_13041
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13042 = relay.var("var_13042", dtype = "bool", shape = (504, 2))#candidate|13042|(504, 2)|var|bool
func_13041_call = mutated_mod.get_global_var('func_13041')
call_13043 = func_13041_call(var_13042)
output = call_13043
func_13044 = relay.Function([var_13042], output)
mutated_mod['func_13044'] = func_13044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_13046 = func_8696_call()
call_13047 = func_8696_call()
func_8296_call = mod.get_global_var('func_8296')
func_8298_call = mutated_mod.get_global_var('func_8298')
call_13048 = func_8296_call()
call_13049 = func_8296_call()
output = relay.Tuple([call_13046,call_13048,])
output2 = relay.Tuple([call_13047,call_13049,])
func_13057 = relay.Function([], output)
mod['func_13057'] = func_13057
mod = relay.transform.InferType()(mod)
mutated_mod['func_13057'] = func_13057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13057_call = mutated_mod.get_global_var('func_13057')
call_13058 = func_13057_call()
output = call_13058
func_13059 = relay.Function([], output)
mutated_mod['func_13059'] = func_13059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8930_call = mod.get_global_var('func_8930')
func_8932_call = mutated_mod.get_global_var('func_8932')
call_13123 = func_8930_call()
call_13124 = func_8930_call()
func_8572_call = mod.get_global_var('func_8572')
func_8574_call = mutated_mod.get_global_var('func_8574')
var_13130 = relay.var("var_13130", dtype = "int16", shape = (1980,))#candidate|13130|(1980,)|var|int16
call_13129 = relay.TupleGetItem(func_8572_call(relay.reshape(var_13130.astype('int16'), [1980,])), 4)
call_13131 = relay.TupleGetItem(func_8574_call(relay.reshape(var_13130.astype('int16'), [1980,])), 4)
bop_13144 = relay.greater_equal(call_13129.astype('bool'), var_13130.astype('bool')) # shape=(60, 1980)
bop_13147 = relay.greater_equal(call_13131.astype('bool'), var_13130.astype('bool')) # shape=(60, 1980)
func_7344_call = mod.get_global_var('func_7344')
func_7345_call = mutated_mod.get_global_var('func_7345')
call_13148 = func_7344_call()
call_13149 = func_7344_call()
output = relay.Tuple([call_13123,bop_13144,call_13148,])
output2 = relay.Tuple([call_13124,bop_13147,call_13149,])
func_13154 = relay.Function([var_13130,], output)
mod['func_13154'] = func_13154
mod = relay.transform.InferType()(mod)
var_13155 = relay.var("var_13155", dtype = "int16", shape = (1980,))#candidate|13155|(1980,)|var|int16
output = func_13154(var_13155)
func_13156 = relay.Function([var_13155], output)
mutated_mod['func_13156'] = func_13156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_13188 = relay.TupleGetItem(func_11617_call(), 0)
call_13189 = relay.TupleGetItem(func_11618_call(), 0)
output = relay.Tuple([call_13188,])
output2 = relay.Tuple([call_13189,])
func_13214 = relay.Function([], output)
mod['func_13214'] = func_13214
mod = relay.transform.InferType()(mod)
mutated_mod['func_13214'] = func_13214
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13214_call = mutated_mod.get_global_var('func_13214')
call_13215 = func_13214_call()
output = call_13215
func_13216 = relay.Function([], output)
mutated_mod['func_13216'] = func_13216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8212_call = mod.get_global_var('func_8212')
func_8214_call = mutated_mod.get_global_var('func_8214')
call_13246 = relay.TupleGetItem(func_8212_call(), 2)
call_13247 = relay.TupleGetItem(func_8214_call(), 2)
func_9713_call = mod.get_global_var('func_9713')
func_9715_call = mutated_mod.get_global_var('func_9715')
call_13253 = relay.TupleGetItem(func_9713_call(), 0)
call_13254 = relay.TupleGetItem(func_9715_call(), 0)
uop_13255 = relay.atan(call_13246.astype('float64')) # shape=(550,)
uop_13257 = relay.atan(call_13247.astype('float64')) # shape=(550,)
output = relay.Tuple([call_13253,uop_13255,])
output2 = relay.Tuple([call_13254,uop_13257,])
func_13260 = relay.Function([], output)
mod['func_13260'] = func_13260
mod = relay.transform.InferType()(mod)
mutated_mod['func_13260'] = func_13260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13260_call = mutated_mod.get_global_var('func_13260')
call_13261 = func_13260_call()
output = call_13261
func_13262 = relay.Function([], output)
mutated_mod['func_13262'] = func_13262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10515_call = mod.get_global_var('func_10515')
func_10517_call = mutated_mod.get_global_var('func_10517')
call_13286 = relay.TupleGetItem(func_10515_call(), 1)
call_13287 = relay.TupleGetItem(func_10517_call(), 1)
output = call_13286
output2 = call_13287
func_13290 = relay.Function([], output)
mod['func_13290'] = func_13290
mod = relay.transform.InferType()(mod)
output = func_13290()
func_13291 = relay.Function([], output)
mutated_mod['func_13291'] = func_13291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12750_call = mod.get_global_var('func_12750')
func_12752_call = mutated_mod.get_global_var('func_12752')
call_13307 = func_12750_call()
call_13308 = func_12750_call()
output = relay.Tuple([call_13307,])
output2 = relay.Tuple([call_13308,])
func_13312 = relay.Function([], output)
mod['func_13312'] = func_13312
mod = relay.transform.InferType()(mod)
mutated_mod['func_13312'] = func_13312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13312_call = mutated_mod.get_global_var('func_13312')
call_13313 = func_13312_call()
output = call_13313
func_13314 = relay.Function([], output)
mutated_mod['func_13314'] = func_13314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mod.get_global_var('func_8349')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_13315 = func_8349_call()
call_13316 = func_8349_call()
func_12343_call = mod.get_global_var('func_12343')
func_12347_call = mutated_mod.get_global_var('func_12347')
var_13330 = relay.var("var_13330", dtype = "bool", shape = (1008,))#candidate|13330|(1008,)|var|bool
var_13331 = relay.var("var_13331", dtype = "uint64", shape = (60,))#candidate|13331|(60,)|var|uint64
const_13332 = relay.const(8, dtype = "int64")#candidate|13332|()|const|int64
call_13329 = relay.TupleGetItem(func_12343_call(relay.reshape(var_13330.astype('bool'), [2, 504]), relay.reshape(var_13331.astype('uint64'), [60,]), relay.reshape(const_13332.astype('int64'), []), ), 5)
call_13333 = relay.TupleGetItem(func_12347_call(relay.reshape(var_13330.astype('bool'), [2, 504]), relay.reshape(var_13331.astype('uint64'), [60,]), relay.reshape(const_13332.astype('int64'), []), ), 5)
output = relay.Tuple([call_13315,call_13329,var_13330,var_13331,const_13332,])
output2 = relay.Tuple([call_13316,call_13333,var_13330,var_13331,const_13332,])
func_13341 = relay.Function([var_13330,var_13331,], output)
mod['func_13341'] = func_13341
mod = relay.transform.InferType()(mod)
mutated_mod['func_13341'] = func_13341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13341_call = mutated_mod.get_global_var('func_13341')
var_13343 = relay.var("var_13343", dtype = "bool", shape = (1008,))#candidate|13343|(1008,)|var|bool
var_13344 = relay.var("var_13344", dtype = "uint64", shape = (60,))#candidate|13344|(60,)|var|uint64
call_13342 = func_13341_call(var_13343,var_13344,)
output = call_13342
func_13345 = relay.Function([var_13343,var_13344,], output)
mutated_mod['func_13345'] = func_13345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_13378 = relay.TupleGetItem(func_11351_call(), 0)
call_13379 = relay.TupleGetItem(func_11352_call(), 0)
func_8572_call = mod.get_global_var('func_8572')
func_8574_call = mutated_mod.get_global_var('func_8574')
var_13389 = relay.var("var_13389", dtype = "int16", shape = (1980,))#candidate|13389|(1980,)|var|int16
call_13388 = relay.TupleGetItem(func_8572_call(relay.reshape(var_13389.astype('int16'), [1980,])), 3)
call_13390 = relay.TupleGetItem(func_8574_call(relay.reshape(var_13389.astype('int16'), [1980,])), 3)
func_10909_call = mod.get_global_var('func_10909')
func_10911_call = mutated_mod.get_global_var('func_10911')
call_13399 = relay.TupleGetItem(func_10909_call(), 0)
call_13400 = relay.TupleGetItem(func_10911_call(), 0)
output = relay.Tuple([call_13378,call_13388,var_13389,call_13399,])
output2 = relay.Tuple([call_13379,call_13390,var_13389,call_13400,])
func_13404 = relay.Function([var_13389,], output)
mod['func_13404'] = func_13404
mod = relay.transform.InferType()(mod)
var_13405 = relay.var("var_13405", dtype = "int16", shape = (1980,))#candidate|13405|(1980,)|var|int16
output = func_13404(var_13405)
func_13406 = relay.Function([var_13405], output)
mutated_mod['func_13406'] = func_13406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12750_call = mod.get_global_var('func_12750')
func_12752_call = mutated_mod.get_global_var('func_12752')
call_13484 = func_12750_call()
call_13485 = func_12750_call()
output = relay.Tuple([call_13484,])
output2 = relay.Tuple([call_13485,])
func_13491 = relay.Function([], output)
mod['func_13491'] = func_13491
mod = relay.transform.InferType()(mod)
mutated_mod['func_13491'] = func_13491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13491_call = mutated_mod.get_global_var('func_13491')
call_13492 = func_13491_call()
output = call_13492
func_13493 = relay.Function([], output)
mutated_mod['func_13493'] = func_13493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10653_call = mod.get_global_var('func_10653')
func_10654_call = mutated_mod.get_global_var('func_10654')
call_13538 = func_10653_call()
call_13539 = func_10653_call()
var_13588 = relay.var("var_13588", dtype = "int8", shape = (3, 7, 7))#candidate|13588|(3, 7, 7)|var|int8
bop_13589 = relay.greater_equal(call_13538.astype('bool'), relay.reshape(var_13588.astype('bool'), relay.shape_of(call_13538))) # shape=(3, 7, 7)
bop_13592 = relay.greater_equal(call_13539.astype('bool'), relay.reshape(var_13588.astype('bool'), relay.shape_of(call_13539))) # shape=(3, 7, 7)
output = bop_13589
output2 = bop_13592
func_13605 = relay.Function([var_13588,], output)
mod['func_13605'] = func_13605
mod = relay.transform.InferType()(mod)
mutated_mod['func_13605'] = func_13605
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13606 = relay.var("var_13606", dtype = "int8", shape = (3, 7, 7))#candidate|13606|(3, 7, 7)|var|int8
func_13605_call = mutated_mod.get_global_var('func_13605')
call_13607 = func_13605_call(var_13606)
output = call_13607
func_13608 = relay.Function([var_13606], output)
mutated_mod['func_13608'] = func_13608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_13681 = relay.TupleGetItem(func_7523_call(), 0)
call_13682 = relay.TupleGetItem(func_7525_call(), 0)
output = call_13681
output2 = call_13682
func_13697 = relay.Function([], output)
mod['func_13697'] = func_13697
mod = relay.transform.InferType()(mod)
output = func_13697()
func_13698 = relay.Function([], output)
mutated_mod['func_13698'] = func_13698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10020_call = mod.get_global_var('func_10020')
func_10022_call = mutated_mod.get_global_var('func_10022')
call_13720 = func_10020_call()
call_13721 = func_10020_call()
output = call_13720
output2 = call_13721
func_13745 = relay.Function([], output)
mod['func_13745'] = func_13745
mod = relay.transform.InferType()(mod)
output = func_13745()
func_13746 = relay.Function([], output)
mutated_mod['func_13746'] = func_13746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8244_call = mod.get_global_var('func_8244')
func_8246_call = mutated_mod.get_global_var('func_8246')
call_13764 = relay.TupleGetItem(func_8244_call(), 1)
call_13765 = relay.TupleGetItem(func_8246_call(), 1)
func_6309_call = mod.get_global_var('func_6309')
func_6318_call = mutated_mod.get_global_var('func_6318')
var_13769 = relay.var("var_13769", dtype = "uint32", shape = (2112,))#candidate|13769|(2112,)|var|uint32
const_13770 = relay.const([-2,7,7,10,10,-7,10,2,6,-8,-4,4,-8,-3,10,6,5,10,5,-5,9], dtype = "int32")#candidate|13770|(21,)|const|int32
const_13771 = relay.const([-1,-1,4,-10,10,4,-6,-3,-3,8,4,-9,7,-3,6,-6,-7,-4,8,1,7,6,-4,-10,1,4,-4,-6,9,-7,-3,1,-2,5,8,10,3,9,-6,-6,-4,4,-3,1,10,-8,3,-7,4,-6,9,-8,-5,-2,5,-10,8,9,2,5], dtype = "uint64")#candidate|13771|(60,)|const|uint64
const_13772 = relay.const([7,3,-6,-5,9,-2,6,3,8,6,9,2,7,-7,6,-4,-8,6,-3,-8,-4,-9,-8,10,2,-6,10,-8,-1,-9,-1,-1,-1,-4,-9,5,5,-6,8,-2,4,1,3,-2,8,-3,-4,9,3,-10,-6,-10,10,-5,-3,-1,3,10,-5,2,4,2,2,-5,-3,-9,-9,9,4,10,-10,-2,-4,1,-5,-3,-8,6,4,-5,6,7,3,-5,-1,4,-7,-4,-1,2,-8,4,8,6,-3,3,6,-5,8,-8,6,-8,-8,-5,5,-4,10,9,-8,-4,-7,-10,-6,6,4,1,-5,2,1,-2,-3,-9,4,3,-4,-5,-3,-8,10,3,7,4,4,5,5,2,-6,3,3,-6,-4,-10,7,-5,3,3,-3,9,-6,1,-4,9,7,9,-9,-7,-5,-9,-6,-1,4,6,-2,-5,1,-8,-10,-4,1,5,10,3,8,10,-10,-2,7,-4,-4,9,-4,2,-6,-10,-4,6,-6,9,-5,-9,-2,-1,-8,-9,-3,-2,5,-10,-2,9,7,8,-6,-1,-8,6,-1,2,-2,-6,9,-2,1,9,-6,7,-4,9,6,1,-10,5,-3,-3,-7,-2,6,-5,9,10,10,7,4,4,-5,3,3,7,6,3,-10,4,-10,-2,-2,-2,-2,6,6,8,-6,-7,1,-5,7,-2,2,2,4,-10,-8,9,-3,6,9,-1,6,-2,-5,6,6,6,6,9,-3,6,-1,-9,-4,-4,-10,-7,-4,-5,-7,-10,1,-10,-5,6,-10,-7,-1,-7,-3,7,-7,-2,-3,-1,-10,-3,8,-7,-4,3,9,-9,8,5,-9,7,-7,9,7,-2,3,-7,1,-6,-1,1,10,-10,5,2,-8,-10,-7,6,-8,-1,4,-2,4,-1,10,4,-3,-8,8,2,6,-10,10,-9,4,9,-9,-6,2,7,9,-2,4,3,-8,9,-7,-1,6,-7,-1,2,-1,3,6,-5,-1,-9,7,-8,-5,10,-9,2,2,-10,8,-3,10,4,7,-1,8,-3,10,-9,2,8,4,-1,-9,-1,2,-8,1,-6,-3,5,5,-4,1,1,-7,-7,10,7,-6,8,2,10,-10,-10,-3,2,-4,2,-4,-1,3,1,-5,-3,-7,-10,-9,-2,7,9,10,-8,10,10,-5,6,-8,-9,7,5,-3,5,-5,8,-3,-4,10,5,-3,5,-7,-6,-10,-7,9,3,7,3,-6,-8,1,2,-3,3,-4,-4,1,-6,-6,-10,-7,6,-10,7,-3,-7,-6,-6,-5,-5,-9,-2,10,3,-2,-3,-5,-2,2,-3,6,-7,-8,-1,2,-6,6,1,-3,-6,-7,-4,9,-7,9,4,-9,-10,-6,2,9,-10,5,5,-8,-4,7,7,-6,-5,-4,2,3,-2,5,8,-3,2,-2,7,5,4,1,-8,-6,4,5,7,10,-5], dtype = "int64")#candidate|13772|(540,)|const|int64
const_13773 = relay.const([[-1.504603],[1.645539],[6.144740],[-0.233611],[-2.213181],[3.983600],[6.064619],[-9.410365],[0.008376],[9.373708],[-9.463231],[-2.930106],[7.354932],[-8.346489],[3.205762],[1.349846],[5.958845],[-5.771826],[-9.104536],[7.024454],[-8.374382],[-2.590379],[-2.271287],[-4.253400],[2.837141],[-3.284515],[-7.076304],[-8.291503],[-9.721882],[-8.691629],[2.617317],[8.009842],[-3.051411],[-0.015075],[3.996782],[-8.026832],[-0.438340],[0.622022],[9.528286],[-4.797616],[6.062868],[-9.305853],[9.860850],[1.144781],[3.756163],[5.409558],[2.499686],[1.839945],[-6.397330],[-9.237043],[-8.417781],[8.785318],[-1.675763],[0.574952],[1.514668],[-7.466254],[-4.083937],[-5.877158],[-9.028912],[5.527356],[6.118900],[-1.886484],[-1.762840],[4.215326],[7.185212],[-7.654410],[-4.326415],[-2.225278],[-2.501517],[-5.252822],[-5.737389],[-9.998848],[-5.942170],[-4.511232],[-7.741338],[-1.528975],[7.651080],[8.219437],[2.088043],[-1.923364],[-0.802657],[-7.566518],[4.128292],[7.404765],[-2.604607],[9.580499],[6.355684],[9.378949],[-8.847135],[-4.387637],[3.480402],[8.704708],[3.873018],[-5.608029],[7.008877],[-1.733287],[3.095883],[-1.026904],[9.446158],[-0.088917],[2.002516],[-8.617663],[9.480786],[-2.133762],[-8.444690],[5.902743],[-3.871021],[-7.348193],[8.567160],[-5.357869],[7.902891],[-2.866920],[9.524057],[4.401190],[5.540779],[-5.865150],[5.301941],[5.652705],[-5.631271],[7.063181],[-7.626227],[-6.404154],[9.375925],[-7.459547],[-9.114067],[7.104353],[9.996191],[-8.773207],[-2.105993],[-5.713991],[-1.381604],[-6.891650],[1.465261],[-5.487252],[-9.664726],[-7.006685],[-8.808376],[3.721798],[4.069442],[-0.353960],[-2.215513],[-5.136962],[-6.245194],[-0.913360],[-1.562974],[-0.949748],[1.075290],[9.921902],[-9.247251],[-4.932109],[6.356594],[7.944100],[4.323913],[8.523507],[-0.026421],[-7.387253],[5.840883],[0.495665],[-6.085433],[-8.316622],[-4.372266],[4.566290],[6.049965],[-0.712383],[-8.829442],[-8.613228],[-5.266801],[-3.106997],[-8.083135],[-9.105611],[1.703575],[3.702810],[4.309065],[-6.508283],[-1.741446],[4.056462],[5.510003],[-9.576218],[3.472018],[-0.415114],[0.797327],[9.212374],[-6.132208],[-6.128233],[1.658978],[-4.949156],[0.168209],[3.919149],[-7.834783],[-6.009800],[-6.591225],[1.920721],[-8.940139],[-2.163159],[-5.872637],[-5.621908],[-1.164759],[5.110821],[2.959872],[4.897079],[1.795492],[6.712979],[-6.936232],[1.611434],[2.474746],[7.746795],[7.065446],[2.887985],[9.276500],[3.457971],[1.885776],[7.329558],[0.467709],[-1.261211],[-2.218776],[0.157238],[2.195176],[0.563824],[9.645549],[-5.646664],[-2.695570],[-8.308174],[-6.397701],[-9.073306],[-9.976539],[-7.575812],[7.112306],[8.835626],[-8.111388],[1.739324],[5.797733],[-4.232646],[9.623427],[-5.415993],[2.362801],[5.561053],[5.566719],[9.181819],[-3.275371],[8.691981],[-0.424479],[-1.891124],[5.369549],[-8.731552],[6.757245],[8.596878],[7.179555],[-4.163595],[6.409899],[8.469756],[4.125955],[-1.284072],[4.829370],[5.752428],[1.467777],[-1.527009],[-6.631967],[0.389727],[-1.046086],[9.348139],[5.941345],[-7.924761],[1.047865],[-6.301300],[-2.215828],[7.545567],[-1.115756],[-1.049096],[4.362885],[2.327541],[-2.864643],[-6.594464],[-7.838010],[-0.425040],[-7.878571],[9.548302],[-0.850318],[-1.534000],[-4.173963],[-2.541702],[-3.334367],[-2.384863],[-9.203901],[-7.867416],[-8.751023],[-7.711310],[8.880961],[9.761925],[6.332180],[-6.680367],[-8.625497],[8.685888],[-0.853249],[-6.899545],[-9.848289],[2.438587],[-8.174243],[-4.361894],[-2.292074],[-1.815732],[-6.042174],[4.403957],[-6.933543],[-9.553762],[-5.694382],[7.848800],[-5.592372],[-9.485652],[-5.898932],[2.355405],[7.721897],[8.126917],[-7.800245],[-8.187024],[8.526765],[-8.578459],[-5.038812],[0.441235],[-3.667111],[-1.397506],[9.377061],[7.141468],[-4.097430],[-9.461825],[-7.448798],[-3.329874],[-8.109892],[9.496937],[5.410277],[4.093632],[8.859372],[-0.095102],[5.912700],[-0.480069],[6.845935],[-8.367112],[-9.761707],[-7.910502],[4.920235],[7.396399],[-2.627702],[-5.343335],[7.894417],[-0.074862],[6.279253],[1.835283],[5.211573],[-0.157948],[-4.751550],[-2.230172],[5.139685],[-1.637657],[7.379196],[1.903961],[1.961955],[-7.320637],[-6.460950],[-1.241753],[0.067282],[-2.818301],[-1.879734],[5.740058],[9.155772],[-7.314382],[-5.158064],[-6.524182],[2.099076],[8.363804],[1.752814],[-8.983471],[8.918688],[7.437082],[3.412901],[0.355743],[-1.700412],[4.150723],[-0.923687],[-5.293762],[9.668684],[1.953769],[6.558064],[9.807224],[-7.539749],[2.648838],[7.095302],[-0.133891],[4.278960],[-5.033052],[1.378009],[6.965180],[1.450182],[-2.152152],[5.473851],[-5.853386],[2.054341],[-0.972438],[5.429401],[3.183445],[-7.317100],[9.101237],[-3.297433],[-9.453194],[5.753736],[-9.315762],[-0.265287],[-0.266885],[3.042092],[0.817372],[0.134239],[6.074881],[9.748621],[-1.384603],[0.231357],[-9.849342],[-0.370597],[-4.675501],[7.047365],[-1.601534],[6.976753],[8.575020],[-4.244544],[-4.146453],[-3.421513],[-1.921221],[6.245339],[-5.117685],[1.196780],[1.908470],[1.693642],[-3.841055],[8.421604],[-7.546115],[4.375691],[-0.149066],[-3.954093],[7.938098],[8.805051],[-9.581829],[8.690329],[-6.535182],[-7.200596],[-8.103553],[9.513755],[-7.251714],[6.738626],[-1.948291],[9.564920],[-2.070212],[-9.814293],[-6.765054],[-8.897072],[2.795591],[1.499048],[-3.235671],[9.588342],[3.419505],[9.752826],[5.696251],[7.860604],[2.999887],[3.338443],[0.789704],[8.530461],[0.665152],[-7.949340],[-2.498824],[7.007912],[6.367636],[4.057888],[-8.657156],[-8.561753],[-1.246415],[8.419640],[-7.144311],[2.116742],[3.939761],[8.201428],[-2.288765],[-2.547321],[-0.809171],[7.593464],[-3.755556],[6.570173],[6.371343],[0.685771],[1.464702],[8.573563],[8.184104],[1.694053],[1.869735],[-0.508062],[6.549310],[2.776994],[-3.072972],[-3.092660],[5.280848],[5.135096],[-5.692552],[7.213328],[5.851202],[7.460671],[-6.936762],[-0.517328],[3.215471],[2.723779],[-3.695784],[-3.077605],[4.145385],[0.626108],[6.926428],[6.063581],[4.665040],[-6.985277],[6.501240],[1.843574],[-8.080875],[7.027291],[3.296304],[3.740395],[5.252103],[8.128107],[-5.909456],[-4.587574],[-4.906078],[2.835748],[5.613452],[-7.883360],[0.042980],[-1.185554],[-7.549420],[4.246292],[3.129773],[8.174710],[-8.044644],[8.354625],[5.167606],[4.804395],[-0.653450],[0.699717],[-6.691537],[3.614964],[7.560183],[-1.116624],[-3.945089],[1.397392],[2.325976],[-6.630094],[0.261635],[0.436384],[-2.216533],[-3.030504],[-5.645397],[7.769645],[2.225504],[4.643273],[0.261908],[5.674108],[-5.731800],[6.265178],[-6.969182],[7.374913],[4.621644],[-0.624736],[4.637752],[-9.989270],[4.649111],[5.675030],[-3.456354],[-9.759207],[1.069738],[6.545657],[-1.942998],[-0.883402],[3.754108],[-5.718461],[-7.442794],[0.824592],[4.114033],[2.358486],[2.721902],[-3.648378],[-8.748959],[-4.517890],[-9.256604],[-0.061524],[-7.760463],[-1.031121],[-2.649346],[1.654029],[-8.698453],[5.139470],[2.684194],[-6.568863],[2.802781],[7.692725],[2.041174],[0.891581],[9.198275],[-0.847215],[-2.774047],[-6.299149],[2.458972],[-5.202563],[6.214019],[8.620870],[7.990992],[-0.182083],[4.109308],[8.319791],[-2.226937],[5.179768],[-4.790831],[4.594037],[8.303325],[5.141353],[-3.170132],[-0.442244],[-3.447900],[0.868058],[8.539396],[2.631525],[-5.999212],[6.397996],[-5.079032],[-3.913139],[-9.454023],[-0.792318],[-2.735238],[-2.465927],[2.504121],[1.955984],[1.502994],[0.844106],[-2.800625],[6.955292],[2.545585],[-1.144065],[9.818175],[4.321693],[-7.402338],[-7.526387],[-0.041058],[6.319308],[9.538369],[-7.054812],[6.511647],[-7.493692],[0.849970],[-1.279360],[0.701726],[9.298674],[-1.021621],[-3.827410],[-8.633268],[5.787711],[1.954842],[8.071515],[-1.209566],[-0.198005],[-0.723760],[6.256444],[-8.736216],[8.673169],[6.619078],[-1.490066],[0.218798],[-8.960549],[3.182683],[6.230615],[-6.895665],[3.868800],[5.004633],[8.220177],[7.048888],[3.952456],[-1.203033],[-7.763316],[-7.989969],[0.746997],[4.555353],[-4.492067],[3.423739],[0.029609],[7.974357],[-6.512621],[4.139738],[4.565947],[-0.978950],[4.182858],[-2.813870],[-7.745800],[9.321436],[-3.796596],[-5.507397],[5.695662],[8.493513],[-3.049237],[-5.161581],[9.787043],[9.817553],[-5.253438],[5.812107],[4.950602],[-1.845208],[-1.166070],[0.814017],[-4.378993],[4.578781],[-9.407947],[-9.722298],[3.164937],[-6.432772],[-3.279045],[7.449034],[-9.527081],[-3.350275],[-2.929757],[5.885711],[5.530182],[-2.895085],[-3.818218],[-1.629321],[-5.462650],[6.487740],[7.724098],[-9.395637],[2.983530],[8.427438],[-9.613195],[-4.120015],[0.019423],[5.303927],[-7.009131],[2.099706],[-7.300004],[5.201292],[9.978568],[6.139635],[0.723010],[-2.513725],[-6.778700],[-0.008351],[7.620465],[-6.224051],[-3.477277],[6.375711],[8.309011],[2.489406],[4.196599],[9.331423],[-2.887779],[-3.419128],[1.959783],[1.512081],[2.553854],[0.027377],[8.871961],[3.491925],[6.690444],[-5.588617],[-7.787732],[7.688438],[-1.474642],[-4.270818],[1.703103],[0.555702],[-0.102544],[7.405302],[-5.568689],[7.183328],[8.759300],[0.872153],[-1.752215],[6.396866],[-7.862970],[4.432308],[6.122940],[-7.349137],[-3.676508],[6.109740],[4.311390],[2.544223],[2.653733],[8.807876],[-9.791659],[3.520095],[2.107061],[-7.367964],[6.439877],[-8.363525],[7.625940],[5.350264],[-5.008226],[-8.568979],[-6.818727],[6.745200],[-3.551166],[6.591834],[3.137581],[4.051680],[2.382428],[2.438207],[-9.494278],[-1.131501],[-3.531932],[6.489124],[1.559468],[-5.661558],[2.545475],[-0.406126],[0.592651],[0.319565],[-1.861311],[0.362453],[4.663139],[5.320299],[5.022553],[3.458487],[-2.017769],[5.531985],[-0.595100],[-3.028731],[1.430436],[-3.014598],[9.635405],[-9.392392],[-2.159533],[9.609374],[4.664911],[-2.657820],[8.212258],[2.757071],[8.333501],[-5.800940],[0.548807],[-0.454377],[8.631249],[7.401332],[5.279348],[1.222362],[-8.218493],[5.806822],[8.407496],[5.862108],[8.033600],[9.100920],[-7.399080],[4.836334],[1.696118],[1.701052],[-0.703993],[4.750674],[3.081001],[-1.950928],[-5.633707],[0.727867],[-2.544578],[3.387832],[3.669830],[-4.534268],[-2.431194],[-1.440006],[-1.902073],[-1.930609],[3.816915],[-5.972360],[0.147603],[7.268805],[-8.077357],[-8.126157],[2.835529],[7.969106],[-6.808151],[6.233948],[-3.703239],[6.997097],[8.963191],[4.873820],[7.262271],[-6.178592],[1.495307],[-2.261695],[-0.486400],[2.313062],[-8.387673],[6.121591],[-3.852079],[1.772484],[3.128873],[-4.945731],[-8.389435],[-6.847984],[0.550695],[0.181562],[-0.447393],[-6.905758],[0.636293],[-9.549793],[-0.240106],[-4.585763],[0.285061],[6.283455],[0.857313],[5.671580],[4.815243],[-5.761597],[3.013923],[-3.737426],[-2.759222],[2.439644],[4.594370],[-8.046533],[5.966164],[-8.634034],[4.433558],[-3.462951],[-0.495554],[-6.761225],[-0.641661],[-4.156080],[6.939095],[7.594699],[7.167685],[-2.117169],[5.424940],[-6.027517],[7.806863],[7.397072],[-5.253230],[-0.299014],[1.091157],[-9.524259],[-3.398016],[4.147216],[-6.773299],[2.443603],[-9.438088],[-3.607395],[-4.572501],[3.914212],[4.932220],[-2.866326],[-7.034062],[0.796435],[1.221651],[-7.164986],[-1.873464],[-4.812557],[3.951040],[7.675651],[0.558049],[-3.487761],[2.860611],[2.532996],[2.970984],[0.782884],[0.153958],[2.195301],[-4.996187],[-3.175820],[-6.280701],[-8.383764],[0.466429],[-6.581427],[-8.330912],[0.502642],[-5.328341],[9.048355],[-7.531242],[3.303167],[4.772543],[-0.258925],[-7.833535],[-0.997650],[-9.228447],[-4.706600],[-8.290059],[1.440526],[3.462606],[-1.401074],[9.579076],[3.013900],[6.905604],[2.914856],[1.362684],[8.027685],[-9.054460],[8.224462],[2.069297],[6.118676],[-9.949109],[6.228911],[-5.004855],[5.048866],[-7.888590],[0.773320],[9.521737],[9.824359],[6.011599],[-3.291763],[4.714410],[8.286712],[-6.165639],[-0.021894],[-1.568232],[6.808332],[8.597900],[3.808128],[-0.690342],[8.230800],[1.851958],[-1.081423],[8.355812],[7.920967],[8.956612],[8.519905],[-1.749046],[-8.704591],[-1.462968],[-2.695579],[-0.232595],[7.157752],[-9.307631],[0.042918],[1.984449],[3.108091],[9.942880],[1.027208],[1.340946],[0.469533],[7.989425],[0.096575],[7.531865],[-2.591162],[-6.329629],[-1.152353],[-3.665935],[-0.471829],[2.100256],[3.535618],[-1.299916],[0.980420],[3.798157],[-7.443235],[8.607123],[8.799112],[4.386868],[-8.524146],[-7.402461],[-5.101792],[-4.765670],[3.831934],[-8.813863],[4.490884],[5.585348],[8.248059],[-4.285544],[2.365977],[3.411869],[-8.552986],[7.078225],[9.070277],[8.709580],[4.021939],[-2.643824],[-3.121350],[-1.659644],[-4.770603],[-8.270475],[-6.273768],[-1.706422],[7.250988],[-6.819214],[-2.795983],[6.778836],[7.945186],[-4.416024],[7.688071],[-9.731367],[5.703704],[-0.549080],[4.160912],[2.819194],[0.646906],[-6.265840],[1.474762],[1.661659],[5.302188],[1.843298],[-2.053493],[-6.389784],[2.352484],[-1.929977],[-4.232264],[0.004900],[-0.491497],[-5.156649],[7.169699],[8.048909],[1.284064],[-8.375637],[-6.474876],[8.546378],[-0.798577],[-3.074336],[9.531363],[-6.535730],[1.852237],[4.141536],[4.508759],[-9.523426],[-5.116622],[-6.969483],[-9.807466],[1.173979],[1.663809],[9.407436],[7.259407],[2.183994],[4.046046],[-7.859823],[-9.088732],[-2.472440],[-3.785922],[-6.280085],[-6.433772],[5.345970],[1.466335],[-5.430339],[1.262731],[1.394215],[-4.670649],[-1.665970],[9.314706],[8.792906],[9.277611],[-4.845491],[-6.461984],[-2.167377],[-5.200196],[-7.866965],[8.611295],[-6.271652],[3.073033],[-7.541502],[-1.637249],[4.250114],[-2.608608],[-0.581031],[5.530431],[8.747971],[-0.700186],[6.251177],[-2.121654],[3.216029],[-4.069935],[0.496268],[8.999414],[-5.802505],[9.632308],[5.063292],[-8.362804],[-5.388860],[-1.387664],[-7.812604],[-1.529899],[9.649917],[2.498757],[2.209768],[-3.218024],[0.310131],[-2.866791],[-1.132044],[-9.189060],[9.282982],[0.273046],[6.873532],[5.516655],[1.515858],[-6.703114],[-1.130500],[3.986221],[4.662063],[-2.922929],[-8.123890],[2.190765],[2.292170],[-3.982854],[7.739227],[-3.550401],[-6.130955],[0.949711],[2.914203],[8.273578],[3.478238],[-2.836996],[-4.347386],[9.708652],[1.164334],[-8.499183],[-2.161429],[4.578199],[-6.490890],[9.933688],[-5.403533],[-9.757692],[7.623365],[-8.918640],[-5.681060],[2.426939],[6.230311],[9.218937],[7.840020],[-1.505782],[-5.438741],[-5.369510],[-9.019974],[-5.510825],[-0.759825],[5.107674],[1.330719],[4.314289],[0.732656],[4.446061],[-6.692696],[9.229377],[4.747802],[4.152338],[1.845386],[2.319446],[2.044091],[-5.738095],[9.562797],[-3.124460],[-6.961798],[-0.002674],[6.615712],[1.013456],[1.826491],[-1.518230],[9.624030],[1.466217],[9.993021],[-6.675992],[-1.338642],[-3.688142],[7.700850],[-4.153049],[-4.967551],[-1.823275],[-8.922393],[-8.877607],[5.418621],[-0.091081],[4.976553],[-9.778016],[8.110471],[0.015449],[-4.591825],[6.748153],[2.341933],[-6.120762],[9.310747],[8.587828],[3.896530],[-5.532330],[-9.448731],[1.622219],[-1.609339],[-7.685219],[3.547331],[7.884823],[-0.352841],[7.657425],[-4.345163],[-6.976323],[-7.725230],[-9.421589],[2.922945],[3.893352]], dtype = "float64")#candidate|13773|(1280, 1)|const|float64
var_13774 = relay.var("var_13774", dtype = "float64", shape = (96, 2))#candidate|13774|(96, 2)|var|float64
call_13768 = relay.TupleGetItem(func_6309_call(relay.reshape(var_13769.astype('uint32'), [12, 11, 16]), relay.reshape(var_13769.astype('uint32'), [12, 11, 16]), relay.reshape(const_13770.astype('int32'), [21,]), relay.reshape(const_13771.astype('uint64'), [60,]), relay.reshape(const_13772.astype('int64'), [540, 1]), relay.reshape(const_13773.astype('float64'), [320, 4]), relay.reshape(var_13774.astype('float64'), [192,]), ), 3)
call_13775 = relay.TupleGetItem(func_6318_call(relay.reshape(var_13769.astype('uint32'), [12, 11, 16]), relay.reshape(var_13769.astype('uint32'), [12, 11, 16]), relay.reshape(const_13770.astype('int32'), [21,]), relay.reshape(const_13771.astype('uint64'), [60,]), relay.reshape(const_13772.astype('int64'), [540, 1]), relay.reshape(const_13773.astype('float64'), [320, 4]), relay.reshape(var_13774.astype('float64'), [192,]), ), 3)
uop_13779 = relay.asinh(var_13774.astype('float64')) # shape=(96, 2)
uop_13784 = relay.log2(uop_13779.astype('float64')) # shape=(96, 2)
func_10577_call = mod.get_global_var('func_10577')
func_10582_call = mutated_mod.get_global_var('func_10582')
const_13789 = relay.const([-0.876949,1.195445,-0.928071,6.269890,0.434145,0.415444,-7.074207,4.174584,5.036673,-7.100465,0.195482,2.854323,-7.795882,0.609450,7.640904,-3.190660,5.895574,-6.648593,-2.407143,8.196300,-1.146654,-2.140590,1.456999,3.856437,-5.350770,7.220651,9.078278,1.306340,-2.930099,-9.410976,-3.729179,9.095104,-2.943731,8.749490,1.346709,3.656532,7.012100,-3.838345,2.723433,-7.242267,-8.342451,2.458987,-0.909637,9.542405,4.390936,-9.909808,-8.831385,0.325139,3.966923,8.473277,0.992812,-3.630538,-9.669792,5.890523,-3.343400,-1.063848,7.589754,9.797647,-8.533812,-6.479944,-4.740429,-9.438486,-2.718965,5.647325,-2.181377,-3.797395,2.286997,0.052747,-5.871017,8.061787,-9.165528,9.761090,6.432635,3.376105,4.735467,7.828022,-4.781919,-0.525696,5.197084,2.269604,-1.695946,2.791008,-1.458844,-2.348890,4.047812,-9.226618,9.192265,7.803209,-0.694683,-1.280820,-3.485542,2.094317,3.857420,6.396237,2.936320,7.648795,7.496525,-6.401742,2.185757,-3.966290,-3.968248,-5.708409,-0.725320,9.219328,-1.738548,-8.732608,8.447540,8.445308,5.496085,-1.576727,1.311819,-2.399328,-2.678094,9.507516,2.628445,6.036771,-5.677496,6.497993,9.962672,1.286539,6.789353,5.144959,9.806647,5.640125,5.605218,7.277929,3.893272,7.187311,-4.768887,3.266440,-0.599760,-4.715236,-0.075470,1.520521,-3.665596,9.441903,-2.923661,-9.202433,-5.542719,-5.603274,5.128431,-8.549337,-5.310971,5.423116,-1.100528,-3.163060,9.553629,2.569990,5.938222,5.785549,8.566289,8.700035,9.431723,2.847166,5.887063,-3.293416,-5.137866,-4.353110,-1.173696,1.700576,-9.022205,-6.540053,-8.987096,-4.790489,-6.118942,3.665009,-5.083268,-2.279331,1.389773,2.199941,4.416333,4.798587,6.407135,-8.979501,4.891076,-6.614452,-3.386207,6.744144,5.747019,-3.508105,-7.344619,3.816874,-5.987160,-6.342826,-0.742604,-6.956779,2.254394,6.483809,4.604991,4.300823,4.583551,8.606566,-5.820625,3.505004,-4.226573,6.856538,8.024339,5.278975,-0.607074,8.757899,-0.355598,8.482619,-9.321647,-8.848297,-9.164148,-2.626048,5.822913,1.303318,4.812615,3.330522,-2.984692,-6.589864,-0.494789,1.582294,4.454629,4.152559,3.402347,-7.430481,0.488315,6.735422,-0.573635,9.799825,2.481706,4.414853,6.592908,-4.617238,4.346686,-8.734915,6.067252,0.339162,-5.363926,-2.762807,9.193702,3.660670,0.716046,-7.208107,8.754263,4.085131,6.184710,6.859967,-9.997983,-1.938080,-8.111880,2.238556,1.390828,-2.593272,6.383917,7.762735,3.473386,1.719789,5.205582,-9.220622,3.820305,-6.404739,-3.494059,-5.251915,4.416682,7.070094,7.934910,1.644019,1.806180,-1.821164,-4.382318,5.871815,9.301487,-2.259186,-6.175685,9.672962,0.520435,-5.458576,9.663809,-3.329729,-1.307491,-6.265110,-7.944812,-4.099132,5.859335,-9.504407,-3.850861,-0.351206,-3.810583,-2.359381,6.448209,-7.088503,0.410196,7.875658,7.592471,-7.182984,5.361690,5.909580,-5.048955,4.543358,2.598555,-3.820966,5.768359,7.532128,2.766900,-4.984826,8.535293,9.894779,-1.531532,6.970271,-7.003376,0.316855,-3.022092,1.655438,-5.393325,-8.072320,-2.984710,8.677014,8.989080,0.859141,-8.964892,-6.255020,0.020113,4.781157,-5.995462,3.352953,-8.706238,-3.991936,-6.200214,3.175114,-1.132540,-1.664342,-6.640192,-7.360919,-0.068133,6.670930,8.728716,-7.672363,9.466116,-7.620377,-4.265621,4.308192,-4.976282,1.153486,8.288160,2.752969,-2.056923,7.391935,9.187371,9.816735,4.797818,2.966861,-7.155380,0.194695,1.058258,4.702279,-7.782056,-1.077954,-0.176643,4.768254,-1.377021,6.092640,-8.484819,-8.645243,-2.858437,5.984772,-8.868274,-8.352294,-8.472008,-9.933211,-5.992208,8.843803,-5.989741,7.244631,1.648540,8.683123,-4.504809,-8.556919,4.879337,-6.280029,-5.966751,7.939206,-2.838764,6.291358,-6.047960,-5.851687,2.085916,8.668336,4.754070,-5.146066,2.840504,5.001673,-6.012994,-6.192363,-0.924469,5.421467,-6.184508,0.975940,9.254706,1.783345,-7.446831,-1.275240,3.045154,-0.996858,-8.337718,3.024039,-6.360821,9.650865,-3.947433,-4.391383,6.602286,-0.565970,-5.544013,-2.356165,-9.111299,6.841493,-6.262097,9.994085,7.164847,-3.768287,-0.453690,7.674589,-6.812480,-7.872369,-4.065112,3.656612,-6.650070,8.830402,3.378007,-8.929101,6.577604,1.100353,8.410565,4.360615,-7.029604,5.671206,9.471852,7.089079,3.211423,9.681476,-0.393579,1.264265,-6.454915,8.993439,2.591302,7.172941,-7.285396,-9.362999,5.968329,-2.955959,6.393379,2.491411,5.686861,9.132560,-0.752362,-3.654720,8.854326,9.843698,4.836951,-5.745958,4.112891,7.745623,-2.241917,1.735883,-7.307544,0.719449,3.883042,-5.878810,4.309766,-8.805950,-3.450210,-2.207908,-8.352088,2.775928,-2.360797,-8.438315,-0.052139,9.244874,8.968995,-6.107643,1.629103,-4.686111,-3.965611,6.678350,-1.316366,7.294463,-0.844982,-4.748619,-3.310631,-7.007783,5.123946,-9.096302,3.704226,-7.496066,-6.921248,-9.480551,-1.160953,4.536336,3.242429,-6.268017,-9.488677,3.564422,2.968813,2.058793,6.822801,1.420467,3.257508,-7.560494,1.643720,4.246761,-6.325646,5.382675,-5.217724,9.551728,7.767426,5.031664,-6.947947,7.522116,3.665932,2.131088,-1.279248,0.478479,-1.191435,-4.346552,7.636540,6.906103,2.943255,-9.263578,0.761133,-7.503241,-2.061997,-8.558811,-6.941725,-3.795723,1.272655,-8.786953,-9.642522,6.019527,-3.252676,0.078701,8.836281,6.639393,6.158957,9.544965,1.633822,-1.365386,4.013482,-9.158965,-3.948270,2.255071,-3.448103,8.359780,-7.707861,0.950373,3.335236,-1.530862,-7.115032,4.754603,1.848027,-8.567253,-8.103267,-1.913940,-2.540301,8.691016,-6.667947,-2.990936,9.373343,1.426541,-4.401734,-5.836754,9.352255,-5.463154,-2.547940,-4.861775,-4.324292,-9.814015,0.618016,1.997601,-4.396920,-1.839137,5.565091,6.576442,-1.996403,-7.020378,-3.568165,-8.487046,8.052101,0.762916,8.478694,-7.186750,-8.445880,-3.041730,6.275743,8.078078,0.370386,-0.769069,-4.753704,2.583988,7.557520,0.297808,-9.504058,9.986270,6.548607,7.460205,-0.188683,-7.117030,-6.190196,-7.181303,-5.861581,2.070513,2.348076,1.813196,-4.761384,9.530424,-6.828540,3.821444,-2.704596,9.781705,4.015174,-8.035686,-8.784855,-6.313023,-7.530463,-6.305858,3.830503,-4.124634,-0.783298,-8.598203,-6.373304,-8.586894,9.923051,7.189167,-7.656669,7.916427,3.147464,-3.259153,-6.247106,-6.514910,5.189395,-3.791735,0.028368,-8.119471,-7.671507,-0.487259,-8.095290,1.484118,-3.961753,7.386891,7.046889,-7.018490,5.087969,-3.112622,9.318546,-0.135568,-7.631584,8.122193,8.698797,7.176886,0.336952,-4.101753,-5.682316,6.789260,-4.900361,6.080666,3.629273,-2.134534,-6.624245,-5.886000,1.633813,6.506110,8.167781,6.959803,-0.488608,-1.747813,-5.048142,8.496581,5.621640,0.907402,5.545464,3.527034,-4.063360,5.824355,9.762111,6.598157,-7.321985,-1.416484,2.221422,-7.513065,-3.788510,8.452887,9.456259,1.441227,2.911865,-6.554080,4.007473,1.698103,3.785126,8.290996,3.577507,-7.623560,1.788455,0.644696,-0.741953,-5.844185,3.827369,-4.702629,-0.095897,9.583833,-2.327876,-9.231047,6.430925,-9.267278,3.741215,3.158819,-4.502461,-8.420756,-0.332374,-2.317009,-7.946626,3.885262,0.770237,-6.763822,2.149454,6.414825,-6.446938,-7.370184,-0.623506,-4.148959,-8.317196,-4.920273,9.361708,-3.036324,-5.911500,6.550547,9.230427,-0.370104,-6.017072,-3.322208,-0.666850,5.975507,7.637794,3.162145,-6.192565,0.497306,5.613528,2.069841,3.970183,2.780876,2.631494,-8.424367,3.447715,8.037463,3.612779,-7.969212,2.603613,-8.527125,0.640311,-4.035245,-9.085673,-8.431822,5.944580,-7.352880,9.780762,2.916171,-2.581693,2.711826,-8.900931,2.923450,-9.886002,-7.568888,-3.875745,-7.138105,-7.785775,2.887579,5.342582,-4.966761,-9.285130,7.035735,-4.178083,-3.182762,-3.842274,0.377677,-7.980968,-0.525596,-4.543493,-8.947848,-9.236888,-5.277301,-8.188813,6.381119,7.242234,-6.135015,-0.211173,2.590772,-7.092373,-6.616805,5.485982,-9.893764,-1.475997,-9.813315,8.786059,7.404633,2.286860,-6.293453,-6.883956,8.442665,4.735303,2.126920,9.202689,8.894449,-9.479529,-7.791372,1.129559,5.102565,-1.767537,-6.437870,-4.734210,8.670970,1.362670,7.136072,2.406511,4.247160,9.311121,-9.190548,3.716057,-9.770297,5.500853,9.769334,0.976722,1.600979,-2.498909,2.673991,4.791524,-5.885644,-6.768982,-6.015251,7.989458,9.644827,-6.631635,9.275748,8.560134,4.479568,2.546413,2.839690,3.179574,-5.854517,-5.222009,2.429233,-9.520850,-2.924137,3.677367,-6.699693,-1.057562,6.786097,3.770005,-8.975163,6.883956,-4.888386,-8.311535,7.815868,-8.544452,7.466807,-6.843270,-5.847821,-6.083380,0.062479,-3.355303,-9.302500,7.851636,8.064933,9.532702,7.262841,-8.333714,1.941859,1.796783,-6.000578,-7.431143,-7.350473,-4.906151,7.946670,5.633205,4.900212,-9.738481,-1.870325,1.343343,-8.736869,4.180805,5.582395,0.839798,-8.772283,-9.425319,-1.174569,-2.718240,2.248798,-7.530333,-6.825019,0.342279,9.330270,8.700686,-1.443815,1.360774,8.232222,-0.263581,-1.026421,2.291389,4.521480,-2.015128,-1.882403,-5.414365,0.164596,-3.485517,5.730177,4.678047,8.166702,-2.019176,-8.212337,5.551774,0.426734,-5.880017,5.969849,-8.737026,3.164423,4.509236,-7.958316,4.976497,-4.662435,6.483730,-0.773284,-3.447849,0.597152,0.799553,-8.091183,-6.296603,-3.980614,-3.026444,-7.598695,-9.534436,6.062641,-4.808194,-9.419209,0.899691,7.767422,-7.690464,-8.458641,-6.685026,5.312166,7.086386,-8.382822,3.462007,-4.052568,-3.166194,6.474272,9.605678,-2.576278,-4.926736,6.616994,9.786389,-2.557746,-4.678423,-6.084318,-1.890194,-7.003099,-7.951400,1.553001,-2.921490,6.378770,0.408488,7.130437,4.001411,-9.410181,-5.776295,4.571906,-8.227366,4.848181,-1.578718,9.504044,-5.288282,-7.330948,-5.478118,-0.102528,-4.129648,-3.339648,-8.343028,-0.745622,7.744622,1.740636,-0.968198,-3.561359,-1.796971,-7.026090,0.997282,-1.440363,5.843819,-6.586935,-3.013812,-1.421756,-1.723826,-8.987820,7.904750,-6.511787,9.145123,-1.649819,5.544685,1.304732,9.539220,-1.243339,9.903789,-2.734956,-7.901613,6.019866,4.120651,9.914463,-3.159802,7.887211,-6.172980,-6.159403,0.698117,5.020119,4.256698,1.865503,-1.174376,-9.099194,-8.154236,9.905154,0.492683,7.134285,-0.574831,2.234679,4.283702,-4.089252,-7.985665,5.101474,-7.621744,-6.234612,2.668349,-8.298587,-8.471373,-9.556201,9.971334,6.702422,-0.743510,4.051542,2.191827,8.758907,8.756662,-7.337498,-7.421233,-1.785422,-3.948899,6.695147,-7.039073,-6.038049,-9.115530,0.884780,-3.958619,-1.568660,1.166263,2.919457,-0.839477,9.811158,3.164926,-6.114385,-6.257502,-5.167493,1.071982,-1.678573,1.502682,-8.021702,6.895499,7.759409,-1.826495,-8.350727,4.510880,-5.833438,-1.527961,-2.964375,7.233051,-0.769211,7.581666,4.312450,-0.058017,-6.058792,-9.293873,0.302369,-8.617405,7.405841,-0.174398,-2.181010,7.330134,-5.601592,8.484284,0.450623,9.882659,-0.874866,-6.129549,6.758978,6.405377,-6.043679,7.919719,-1.643345,-3.139297,-9.863039,2.928829,2.311733,-5.301286,9.543450,-6.356149,-8.608839,-6.050809,-9.483542,-3.555060,5.050747,9.896656,7.289317,7.824206,-7.894902,3.433534,-9.451013,3.525352,-7.211083,5.249046,2.284426,-0.472058,8.154399,-7.134741,-8.972715,-9.827363,0.683902,4.744017,-2.957420,-0.921572,9.863118,8.357691,-1.718022,4.199817,-7.681170,-4.159775,-6.396360,-8.205530,0.198509,3.621005,2.161809,9.728291,0.004646,-1.224227,5.186828,-8.433088,-5.007256,6.532349,-5.736448,0.670565,8.443694,8.193025,8.546665,-0.043766,-8.315121,-8.243410,1.427245,-9.317866,-6.392922,-5.939693,7.912305,-3.673483,-2.115584,3.155243,-4.066072,-7.700079,-8.501406,3.365886,9.449661,0.905857,1.005611,1.922477,0.501257,0.562074,-3.693860,-1.301746,-7.095322,-8.770766,-9.687427,-9.247906,-4.653366,-5.275168,-3.356790,-8.306300,1.587180,3.501334,2.692880,6.925071,4.909653,8.516284,-2.989443,4.105121,-8.572004,-8.433162,1.590073,-8.669521,9.305404,5.338316,-3.363526,8.006303,8.276247,2.737176,0.867747,2.923365,5.190898,9.080531,-3.004886,0.509543,-3.479841,6.550545,-5.854560,9.816810,6.743798,0.776166,5.514972,2.198480,4.858289,4.838719,-3.589552,6.203852,7.623859,3.726281,-1.437442,8.815261,-4.882844,-3.357116,-4.768766,-5.138952,-3.713432,3.671474,-3.256073,-4.765023,1.678978,6.697319,8.815421,-0.003527,5.452698,-3.542420,-9.986363,-3.687775,2.493149,5.680271,-3.439875,3.691433,5.809162,-1.293007,2.522218,4.564227,1.814687,-0.378220,-0.087632,9.054957,6.515553,6.192489,9.517221,-9.448191,-5.742716,-2.392241,-1.448558,-5.933413,2.743384,4.763615,1.310462,0.861547,1.387043,3.013995,-2.846139,0.630334,4.077723,3.499895,-7.991545,6.110597,9.767619,-6.614946,2.377046,9.362500,8.797772,7.312567,-5.992349,7.603188,0.976443,1.554170,-7.200093,0.545631,8.244764,-0.170537,-6.074274,-2.461279,-1.123867,9.431722,5.018644,-3.051625,-9.732230,-4.998553,-1.686334,-3.723885,-2.312152,-8.378049,5.586797,-1.270060,-3.374054,-4.243043,-1.404434,4.668311,3.296506,-4.043208,3.287154,-2.623939,2.429746,-4.614499,-0.033356,8.380310,-3.355674,0.819761,4.844247,-4.602266,6.129048,-2.673724,-8.404673,-3.722264,8.909900,-8.149349,1.418754,-6.270630,3.144808,-9.715054,0.336312,3.052861,5.697372,7.830466,-4.975535,0.956127,8.738625,-5.439906,2.620381,1.013867,4.656046,9.429762,-3.117429,6.550742,9.488208,-6.461071,2.788913,-3.153247,-2.452281,7.078564,-5.645518,-6.027254,1.245583,5.332420,7.978209,7.285904,-1.602780,0.920008,-3.531089,3.630570,1.565825,-0.479730,6.494310,9.218378,6.461459,-5.385465,6.266297,9.935870,7.064079,5.552677,6.319460,-3.279505,-5.137665,1.241553,-8.242570,-1.212680,-6.488069,3.287714,9.494009,4.149392,6.274093,-2.068073,9.165124,6.468082,-1.425910,6.802308,4.401728,-2.083689,-1.932401,-1.259781,-7.412989,-8.807913,-4.070315,-6.476539,-0.925592,-6.011829,2.466619,3.931874,-6.732889,-5.644637,4.970772,-6.780593,5.241392,-8.405292,-3.812930,-8.215007,7.695333,7.365860,-4.845093,-6.285438,-2.794635,8.421606,5.600872,-7.634604,5.574906,7.734740,-7.626874,-3.268380,-5.350805,4.325155,1.395863,8.444684,-4.033962,-0.257774,-6.502490,-6.705453,4.241445,-9.192334,-4.568395,-4.518197,3.360131,-8.267318,-6.995321,4.584738,-8.766327,1.038466,9.953820,-6.532269,-0.609935,-7.624933,7.299740,7.667987,-9.722671,-5.940411,-0.847474,6.474203,-8.949228,7.572442,-1.759335,4.566999,-7.073729,-5.036861,5.409714,5.260452,-1.169917,-9.853820,-4.112958,-7.577682,7.997981,7.086923,-5.706375,-3.607257,0.742597,2.602096,-0.816423,-2.832700,2.716806,-0.665319,8.414120,-2.897116,-6.901077,-6.283482,-4.314280,4.944393,1.522245,6.938455,1.483926,-3.923993,-1.316158,-0.984701,-2.796302,5.334104,-3.245780,-1.583520,1.844607,0.806185,2.210924,4.092300,-1.350786,3.263171,9.544276,1.582338,-7.120395,6.576849,2.844481,-2.816763,-5.473018,-1.543119,0.475228,0.781875,5.111119,-8.437494,-2.715633,9.740197,7.341920,-6.348498,7.224691,9.064328,4.071581,-8.508645,9.646907,-1.174850,-7.006008,-9.670535,7.027124,7.547581,-4.524030,6.880939,7.629146,4.230414,6.520833,2.007615,-8.101745,7.662755,-8.548644,-7.659430,-1.542968,2.079998,3.170238,-2.715144,7.975722,-5.026919,-0.595035,-9.865731,-3.826927,-8.713555,3.645761,-5.962639,-3.883317,6.633589,-6.183078,-4.287692,-4.979084,2.927083,6.021637,-4.514143,5.882425,-6.690341,-6.435118,4.153160,2.823642,7.654129,-1.071705,-1.840909,7.563667,0.071785,9.137097,-9.433359,4.825067,-4.636832,3.042943,-6.118095,3.145082,-7.536649,1.054121,-1.192051,4.665828,-0.570162,7.689137,8.353250,-1.741973,-9.233599,-6.785937,-5.655242,4.757099,1.786043,8.245599,9.667354,-9.193849,0.070188,-8.897104,-0.085403,6.194633,8.501211,3.471297,2.419315,5.413150,-1.390844,-2.332093,1.817580,4.931194,-9.090156,-2.879764,0.489394,-7.376103,7.367038,-0.619816,-4.199153,-8.996796,-1.175858,-4.013055,5.554939,-3.305677,-0.677552,-1.302959,-5.121274,-7.765562,0.245823,-5.884186,1.891424,3.842188,9.224342,9.233490,4.580936,3.302699,9.301477,4.977257,0.397512,-2.005487,-0.961145,-8.056599,-7.356055,6.393849,9.421749,-8.360463,-9.716198,8.970055,4.331066,-5.107755,-2.300937,4.621976,5.445054,1.592038,-2.289092,-8.838629,-6.595397,0.395002,3.590346,-9.936373,-9.197684,-2.291611,-0.172936,9.104303,-0.923961,-0.517625,4.298311,-4.413874,-1.492408,-6.365746,-8.686225,2.099113,9.472484,7.868281,-8.692155,5.208830,2.178077,8.914854,-9.047036,7.500143,-8.633409,5.995031,2.424204,5.320356,1.381825,-9.658806,-9.411484,1.878111,-5.813903,0.995394,-8.561997,-6.758430,-9.537768,-8.092539,-8.658042,5.712197,2.387818,-0.465526,-3.680031,9.398653,2.552853,6.549292,6.719141,4.061755,-9.527842,-9.042196,-5.112220,-1.674881,9.126788,2.698299,-6.648109,-6.889269,6.664548,7.741529,-5.236494,-2.700407,-2.989681,-2.448997,-8.032946,-4.149138,-7.057521,0.897450,1.374782,6.834463,-6.169210,-8.383812,6.286948,6.333524,2.275727,-9.153890,3.495680,-2.936366,6.133128,4.863644,-7.565710,-5.628017,9.534946,9.143663,9.300222,8.404551,0.037541,-4.030495,-5.993979,-3.042381,-0.435572,-2.084648,9.684524,-4.543491,9.504017,-4.794894,9.037259,-6.703326,-9.432923,6.831020,-4.327559,-4.412942,-8.676148,-0.114808,-6.566911,-7.867754,8.057786,-5.294024,9.854157,8.322315,-3.924020,4.126290,-5.762527,-9.193006,2.258081,-0.287268,-5.357384,-0.842851,-4.845591,-5.583344,4.761027,5.997267,0.234769,5.785859,-8.198356,0.944295,-1.468846,-9.713383,-5.526230,4.996693,-1.987918,3.359102,-1.799445,5.073093,-3.724564,2.432180,1.430844,-3.058510,-1.176642,1.370562,4.442327,-4.664347,1.260844,-2.903278,8.130378,-0.527058,-1.293953,5.503006,1.039575,8.715256,-2.495039,9.232116,6.512770,-5.342566,4.658808,9.725046,-0.861676,-3.397910,-8.337922,3.721660,-2.820211,-7.553357,4.102133,-1.602907,-4.887308,-7.929059,-3.282114,-1.747540,0.895469,-8.150583,9.240214,4.978422,8.407431,0.917478,1.805098,0.074030,-0.130519,-8.467422,1.826535,-8.551969,-5.923094,-3.062788,-1.796336,-9.632573,6.766974,-6.378369,-3.140108,-7.855031,2.516248,-4.356484,-3.243938,5.556902,4.625254,-7.474661,-7.156432,-1.895632,5.693436,0.819010,-0.450341,-9.766959,-8.242112,-9.868795,-2.717924,-2.313031,-8.230774,-7.261505,5.772418,-5.795702,6.245765,8.741520,4.062176,-7.525191,8.319435,6.273574,-8.515016,5.616339,-3.779670,1.732562,8.012157,8.943878,-0.087100,-0.564511,3.888785,-7.649743,-5.790038,-1.288549,-9.434478,-0.555660,-1.202918,5.633427,9.250642,-2.003779,-8.144922,2.896538,3.671372,7.067409,-3.713841,6.460166,-6.824712,8.438622,-9.354142,0.303189,-1.237870,-8.834947,9.457666,4.418238,-9.727426,-0.249101,-2.877195,-2.571671,-8.126591,6.051073,-5.662505,-0.928832,1.047624,3.916328,8.846710,-7.583095,-8.063248,8.696933,-5.507635,3.366951,-2.482604,5.561288,3.112768,-1.149076,4.124417,-3.770797,5.286778,9.309777,-7.346119,-7.931003,0.449433,-4.525235,5.455362,4.356264,-4.733029,-0.152512,-4.516602,3.959058,-9.873772,-7.511572,-7.513814,5.945791,9.143577,-6.035379,6.345968,-1.315356,8.641329,-5.034262,-2.832234,-5.863104,-8.350225,1.697897,-5.441319,-5.686101,-3.174569,-7.702312,-0.300027,-4.684281,-6.385184,7.230687,1.617422,-7.886615,-9.815634,4.756915,-9.848476,-2.103575,9.248733,-1.211246,-4.383884,-4.331574,2.686201,4.502485,-3.497194,4.351576,-2.475703,-5.088950,-5.957168,-7.215269,3.918238,4.865528,9.426142,6.393043,2.302851,-7.907282,-2.694536,5.863552,-3.738221,2.246656,-9.355309,6.480328,-6.470569,7.260640,9.081821,8.899321,6.073126,-7.282441,-6.879447,3.910776,7.860199,-4.294835,-2.487047,0.606712,-5.515962,5.721176,-9.139834,-1.668349,-7.769526,9.267514,1.708316,3.816017,-2.035314,-1.880055,0.816990,-4.315000,0.885061,-9.029956,-3.961909,-4.802364,9.518757,-6.144924,7.547338,-3.497638,-7.313138,2.072381,-1.242207,-9.700549,-4.364024,-7.588745,1.185771,7.985884,4.612479,-2.213382,9.818576,-3.059023,5.443103,-9.541645,0.187137,-0.850890,2.776008,-3.261055,-0.237740,-6.572708,9.091088,-2.608595,1.881679,6.717862,-9.188821,2.706419,1.707364,-6.051952,-3.542377,2.854346,0.169914,6.822620,8.789509,-4.974509,-8.223469,-2.552583,5.075958,-8.199321,-2.441029,0.907452,-6.884416,4.384966,5.616920,-9.643634,-5.251692,0.379969,4.674937,-0.038661,-1.741893,6.581640,2.945083,-7.615145,-0.417284,-9.326374,7.737397,8.696042,-8.957454,3.956383,-1.222220,4.969747,1.805312,-4.731422,5.284099,1.224052,-5.977190,-2.348671,-9.869197,-0.445527,-3.919222,-3.843804,5.968520,6.899593,-6.190933,6.612726,-3.219788,2.489569,7.976967,-2.782864,2.382386,7.574460,-4.126482,3.633745,-1.376302,-1.028212,-1.490079,-3.426522,-9.641036,2.386735,-0.856361,-4.149882,5.962942,-5.473092,4.026262,0.088641,-9.719049,-7.170622,4.269440,-5.888611,-6.236071,-0.038759,1.228703,-7.124904,-1.663758,-7.715113,-2.838030,3.460741,-7.280059,-6.102064,-0.407807,-4.078547,-7.756953,-9.441412,2.840054,-6.194272,8.687229,-5.942360,8.798588,-8.612611,0.285731,3.316026,9.770246,5.957121,-3.646631,-0.283014,-4.051008,-4.144879,6.039858,-2.377218,4.464660,-6.620762,9.598930,2.598488,7.747864,-5.642468,-4.394160,-4.290354,-1.642437,9.793027,-1.711905,5.704306,3.073187,4.497366,-4.747976,0.048776,-0.561841,-0.075388,-1.430718,7.471719,-7.366545,-2.072056,9.358320,-1.492377,4.456769,-1.785295,8.903957,-0.993709,8.159874,-5.262233,0.759514,0.845498,8.008446,8.470577,9.827309,-7.028282,-5.142391,-4.038519,6.220547,8.662808,6.784775,-3.815519,1.705304,6.162266,2.762232,8.517120,8.559076,-9.519907,-0.044842,-1.616665,-2.531894,9.081692,-0.207689,-6.154908,0.374919,-1.426376,-3.668145,2.290870,2.514805,-1.624635,-9.959194,9.345209,1.059811,5.415807,9.103224,6.023294,-1.701743,-6.908253,7.958990,-9.953871,-7.036543,3.762146,-0.300066,-8.169008,3.659821,-2.586863,-3.106446,5.326744,7.670124,-4.633059,-9.086373,8.670867,-1.991185,1.871960,-9.606848,-0.822089,-9.387498,8.349280,6.242592,-8.527904,9.895758,-9.121661,-7.031970,2.277398,-4.094569,-9.501411,0.174191,8.443362,5.409828,1.861192,2.969329,-9.517737,9.493293,-6.817749,-6.713667,0.433206,9.509190,5.316688,2.623258,3.212576,-6.430819,0.290482,8.650928,-7.903629,2.426760,3.449540,6.221617,4.676096,1.147195,4.301853,-3.574090,9.438676,6.043199,-5.664744,4.939754,-9.465985,4.099440,-7.651880,7.677619,-7.479648,-3.652379,6.732585,5.875567,8.933688,-5.985136,-4.734527,9.361715,-3.985137,2.946100,-6.238023,-5.573952,-1.685608,-6.934285,9.547054,7.375922,-7.354494,2.746061,-9.464070,-3.497970,8.044846,-5.080072,-8.436161,-6.584007,-0.903671,5.930231,-2.037522,-3.973775,1.784351,2.663263,-1.895269,-4.433193,9.300218,-6.333400,6.889781,0.910995,7.649689,-6.661930,4.960093,-9.952074,-3.023755,-7.831878,1.871372,-8.114411,8.794759,2.092886,-6.826766,3.865065,0.183919,8.928234,-6.944052,-3.842337,6.598010,8.614480,0.779797,-8.404518,5.022200,-1.669470,9.826449,-5.233294,7.795378,-3.250191,9.438933,7.204532,2.378207,3.492734,8.016287,5.596630,7.236529,4.928115,-2.132965,-2.076849,0.985140,0.996774,7.068140,7.704383,0.436345,7.926486,8.134359,-2.693749,1.843916,5.823492,6.121662,5.162167,3.084131,2.771241,7.611894,-4.375634,-1.258163,7.289115,0.073416,-0.576752,9.905824,9.422012,-2.729208,4.904902,-2.947451,-5.332221,-0.462899,-6.156453,1.319021,1.123165,0.292134,8.123345,9.552030,-5.124635,4.546474,-3.281931,-6.647195,-0.155140,8.938634,-3.105854,-3.863164,8.057370,3.222413,-3.046105,2.553638,3.874928,1.385657,-0.259888,4.648376,7.300937,-6.393989,9.113682,-2.634017,0.126020,-7.722404,9.008143,9.532332,1.951316,-5.826091,3.566582,5.025227,-7.053578,2.764618,-9.032536,2.178827,2.899178,3.030712,-8.373992,-0.926988,8.042139,-7.574888,8.518216,8.943750,-5.503573,3.663836,3.297558,-8.847718,4.087879,-6.531517,-1.336455,-1.691457,6.022298,8.949734,5.611507,-8.802301,-1.420742,4.515771,-7.543147,-7.123547,-9.603980,-2.441238,-2.896101,5.157338,-1.640970,9.325794,-8.862657,-5.363192,3.855417,3.657681,-0.546827,5.970216,-6.964450,-4.768354,7.552967,0.154962,-2.280324,2.393003,-9.046352,6.202320,9.205455,-3.421124,-6.057997,7.291173,-9.395341,-5.471854,-7.962023,4.363147,-2.485744,0.303472,-2.501977,8.557697,-5.198155,3.916751,9.930100,1.518747,-5.828062,-2.302183,5.565716,-4.618617,3.802229,-9.339915,6.317519,-9.416322,6.448123,8.668089,3.662030,4.621279,-5.869514,-0.877530,1.053746,-7.063149,1.791218,-9.339275,-9.038305,-4.935201,2.499485,-1.083965,-2.234846,-1.303658], dtype = "float64")#candidate|13789|(2464,)|const|float64
const_13790 = relay.const([-10,-6,-3,-2,8,8,6,-5,10,4,1,10,7,-8,9,-3,-6,-5,3,-9,1,-5,5,-5,-9,-4,8,-4,8,-1,7,-5,3,1,-9,-9,10,-1,-3,-9,-5,5,-6,10,2,10,-7,2,7,8,-6,8,8,-8,-6,-5,9,-6,-10,-1,-10,-2,8,-7,-9,-10,-9,-10,10,9,-6,-8,-4,-2,-1,-7,-5,-5,2,7,6,-6,-10,3,-4,-5,-7,-7,-7,7,3,-6,4,-3,-5,10,10,8,2,-9,4,-9,8,3,-5,3,4,-8,3,7,-2,3,4,-3,3,-5,5,-9,1,8,2,-6,1,5,5,-5,-8,2,-8,-8,-6,-1,10,6,1,1,-7,10,-3,3,-6,7,-5,-7,4,7,10,-5,-5,4,-6,9,-2,-3,-3,-2,-5,4,10,6,-7,-5,8,-9,-2,-10,10,2,-10,6,3,2,-9,-9,-8,-2,-7,-5,-1,-9,9,-1,-1,-10,10,-2,-4,-1,3,-1,-5,7,3,7,6,7,5,4,-1,-5,-8,5,3,6,-6,-6,-1,-4,-3,-8,-7,4,-1,8,-3,-6,-1,-5,-7,-2,-8,-7,-1,3,2,-5,-4,-10,7,10,10,1,7,8,8,8,-8,5,3,-3,9,3,7,10,-3,4,-6,-7,-2,6,4,-6,-6,2,-10,6], dtype = "uint64")#candidate|13790|(256,)|const|uint64
call_13788 = relay.TupleGetItem(func_10577_call(relay.reshape(const_13789.astype('float64'), [11, 16, 14]), relay.reshape(const_13789.astype('float64'), [11, 16, 14]), relay.reshape(const_13790.astype('uint64'), [256,]), ), 1)
call_13791 = relay.TupleGetItem(func_10582_call(relay.reshape(const_13789.astype('float64'), [11, 16, 14]), relay.reshape(const_13789.astype('float64'), [11, 16, 14]), relay.reshape(const_13790.astype('uint64'), [256,]), ), 1)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_13795 = relay.TupleGetItem(func_11351_call(), 0)
call_13796 = relay.TupleGetItem(func_11352_call(), 0)
bop_13810 = relay.floor_mod(uop_13779.astype('float64'), relay.reshape(uop_13784.astype('float64'), relay.shape_of(uop_13779))) # shape=(96, 2)
output = relay.Tuple([call_13764,call_13768,var_13769,const_13770,const_13771,const_13772,const_13773,call_13788,const_13789,const_13790,call_13795,bop_13810,])
output2 = relay.Tuple([call_13765,call_13775,var_13769,const_13770,const_13771,const_13772,const_13773,call_13791,const_13789,const_13790,call_13796,bop_13810,])
func_13821 = relay.Function([var_13769,var_13774,], output)
mod['func_13821'] = func_13821
mod = relay.transform.InferType()(mod)
var_13822 = relay.var("var_13822", dtype = "uint32", shape = (2112,))#candidate|13822|(2112,)|var|uint32
var_13823 = relay.var("var_13823", dtype = "float64", shape = (96, 2))#candidate|13823|(96, 2)|var|float64
output = func_13821(var_13822,var_13823,)
func_13824 = relay.Function([var_13822,var_13823,], output)
mutated_mod['func_13824'] = func_13824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9665_call = mod.get_global_var('func_9665')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_13930 = relay.TupleGetItem(func_9665_call(), 0)
call_13931 = relay.TupleGetItem(func_9666_call(), 0)
uop_13934 = relay.asinh(call_13930.astype('float32')) # shape=(550,)
uop_13936 = relay.asinh(call_13931.astype('float32')) # shape=(550,)
output = uop_13934
output2 = uop_13936
func_13938 = relay.Function([], output)
mod['func_13938'] = func_13938
mod = relay.transform.InferType()(mod)
mutated_mod['func_13938'] = func_13938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13938_call = mutated_mod.get_global_var('func_13938')
call_13939 = func_13938_call()
output = call_13939
func_13940 = relay.Function([], output)
mutated_mod['func_13940'] = func_13940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10383_call = mod.get_global_var('func_10383')
func_10384_call = mutated_mod.get_global_var('func_10384')
call_13947 = func_10383_call()
call_13948 = func_10383_call()
func_9894_call = mod.get_global_var('func_9894')
func_9896_call = mutated_mod.get_global_var('func_9896')
call_13951 = relay.TupleGetItem(func_9894_call(), 0)
call_13952 = relay.TupleGetItem(func_9896_call(), 0)
func_11190_call = mod.get_global_var('func_11190')
func_11191_call = mutated_mod.get_global_var('func_11191')
call_13967 = relay.TupleGetItem(func_11190_call(), 0)
call_13968 = relay.TupleGetItem(func_11191_call(), 0)
func_8720_call = mod.get_global_var('func_8720')
func_8723_call = mutated_mod.get_global_var('func_8723')
const_13971 = relay.const([-0.200497,3.235375,-6.348348,-7.035731,3.570468,-3.563377,-7.835835,-5.427471,5.088023,6.031512,9.064133,9.567966,9.980511,-6.983764,8.940487,-2.686592,1.222547,-2.123314,-0.523274,1.196533,3.516506,7.556454,9.277696,2.690257,-9.964126,-1.880383,-6.984483,-7.965758,-9.611006,-4.129715,-0.344437,9.431706,-9.923419,7.224987,2.742988,4.676657,-6.812150,-7.913035,-9.185662,6.879389,8.846152,-0.282282,4.246122,2.836862,6.561289,3.861105,9.593170,-1.837732,7.682967,-5.376680,-5.705173,2.487598,-2.888864,7.475642,-0.599811,4.665496,-9.876362,6.064303,-7.733368,8.369505,0.450884,5.059344,4.005665,-0.352194,5.624398,7.799647,-1.959653,6.204584,3.474482,-8.813869,4.245844,7.409935,3.218558,7.368785,4.619627,-8.212749,1.123174,9.943594,4.680855,5.068382,7.485555,-1.708727,-8.224488,-6.992411,-0.444571,6.722399,1.151479,8.116148,1.829527,-3.423584,0.977245,0.478867,5.696588,-4.119664,8.245776,9.633133,-1.097259,-0.169617,8.102682,-6.383715,5.113984,2.455359,-9.572040,-1.453568,5.680515,7.289450,5.930353,-8.799284,5.723059,7.884649,-0.862279,3.665198,-6.237447,6.473822,5.448685,-8.758276,1.527000,0.750866,-7.096457,-1.955264,-8.627520,1.857835,-1.611697,-4.437290,-4.276395,-0.916983,9.452296,8.782759,-4.707707,7.750162,1.400798,-5.491307,-3.650540,-9.899692,5.114414,-9.297219,-6.925471,7.209932,6.861015,7.384636,7.203425,9.536516,9.652131,1.371190,8.930164,6.361516,-0.637261,-2.149982,0.281034,1.271318,3.675768,6.768501,4.078816,-7.634978,-1.022103,-4.511698,-7.144645,-1.368177,8.590866,0.208409,8.686823,1.832263,-4.427374,-0.156439,-4.896064,3.503921,5.741482,-7.216115,9.128360,-3.858514,-4.607573,-0.086146,-1.718658,-6.087741,-4.776213,-2.240550,7.479993,7.182404,7.924746,0.301063,9.138584,0.146545,7.397112,-9.331311,4.175954,2.679794,9.701758,-6.822363,-4.882798,5.240717,-1.351243,-0.247822,7.710623,5.320533,3.690586,9.058493,8.970054,-0.553660,-3.335953,-3.553702,2.368284,9.631506,8.276226,-9.835613,-9.433378,-4.599011,2.119109,-1.101366,-1.658670,-6.248812,1.547279,-2.119834,-3.209305,8.125409,8.968850,-2.778631,2.137916,-2.408336,7.009386,0.008423,-8.932201,-8.821502,-8.812306,1.866164,7.637238,1.639457,5.339211,3.886463,-1.358765,-6.896606,-0.409050,-9.697785,-2.968780,-0.803037,6.258720,6.877116,8.599932,9.505529,0.754972,-6.009850,-9.695134,4.274832,-0.212483,-1.678725,7.908455,-9.405616,1.167274,-8.156685,9.522358,-8.487917,-8.228715,0.562970,6.164314,1.037835,1.776618,6.688628,8.887832,1.285540,-6.198510,-7.377619,-5.523068,6.160648,6.268233,9.175671,1.554031,4.836989,1.747684,4.217053,-9.089503,0.818809,8.872099,6.899193,2.134732,-3.615285,-8.454149,-5.684878,2.183609,9.963077,1.536874,-5.502996,-2.156323,-8.588487,-2.238429,-0.570018,-7.032493,-9.324792,1.761738,2.679508,-8.243199,-6.549964,-4.751105,9.699189,-7.028317,4.631473,2.239851,-2.018124,7.676904,2.843822,5.151708,-4.626346,-8.652526,7.181486,9.192222,-0.580598,-1.858361,-6.923893,4.709759,-1.914847,-7.828801,1.402491,8.778662,4.379786,-1.738533,-9.220547,0.672209,-2.099977,2.833721,8.966346,-2.090749,-4.389584,-6.826187,8.705746,-0.432352,3.954421,5.777369,-1.974585,5.873813,-2.916768,0.495831,8.842203,6.259802,-5.178138,1.072456,4.683796,3.749312,-8.623114,0.423553,-9.609329,1.924756,-2.852483,-4.600125,-1.809402,2.492561,-8.560067,5.716838,7.747274,5.594516,-0.552252,5.889687,-4.815085,3.790769,-5.156123,-5.743292,2.692024,-4.467080,7.074940,-4.598484,-5.965286,-7.235624,-7.857603,-8.606818,-3.767678,4.018941,-0.149415,3.981252,-6.473477,1.887611,8.059122,4.980097,-0.613346,-5.295148,-5.677336,2.692026,-6.573052,2.561038,2.608118,-0.757029,8.528421,-6.885596,-4.306111,-9.245310,1.398330,5.089027,-3.689951,4.935187,2.622835,-8.186127,-8.488694,-3.168527,1.756294,-1.078959,-4.758267,-4.711078,-1.289453,5.528975,-5.183532,1.763708,-8.436766,-5.491028,9.296735,0.591724,-6.578578,3.320766,3.681943,2.301954,0.663156,8.665369,9.070803,-3.875938,1.567224,-5.781445,4.864469,5.300954,0.376139,-8.694733,6.050721,8.373862,4.405126,-8.556402,-6.776659,2.027141,8.591020,1.097182,4.162399,8.883984,-7.221268,-4.393548,2.673050,6.332294,-6.754766,-6.756948,8.462931,4.553978,-9.121203,9.670134,8.534284,-5.871751,4.743186,4.367855,9.754414,6.630968,8.201655,-4.297809,3.397485,5.153648,2.173199,8.614776,2.663877,-4.044581,0.300355,-9.524674,-2.918545,9.751463,6.691799,-2.717820,9.000049,-4.272054,-0.287710,-0.532826,-9.340752,3.825295,1.428262,-6.319278,8.538900,-8.223554,-7.880639,1.430771,3.300236,-5.461828,-6.812570,-2.825717,8.809816,-6.700575,8.943603,6.316617,-4.446341,7.668809,-9.453716,-3.977001,-5.414625,-5.806975,8.798680,-6.011992,-3.640070,4.805729,5.720434,8.321504,-4.129469,-5.998155,-7.121418,3.559479,-2.852552,-2.314530,-0.144112,-6.300203,3.958285,0.173500,8.511415,5.529257,4.347648,-4.645222,-2.597469,5.408318,9.728618,-5.380277,8.397932,-8.172612,6.640744,-6.962325,5.353421,-5.355786,5.579588,5.922061,9.100017,4.748017,-1.627029,-5.884841,6.346440,5.515343,4.066988,-3.540798,-8.909702,5.954956,9.263440,4.746522,-5.504216,7.758900,-0.655195,-5.311955,8.282167,-3.377494,7.429233,3.619369,-7.963861,0.942843,-4.236742,-3.072582,-2.716562,-9.804547,-1.219781,-5.536407,-8.684120,-0.887842,4.276441,-3.330161,-6.202647,-3.355991,0.613018,-3.105093,-4.169579,-3.336923,1.469924,5.942987,-0.191917,9.148846,-7.502759,5.053710,1.994048,3.684306,0.485133,-8.756194,-8.620761,0.501911,-6.555134,1.740879,-7.595494,0.667554,-0.715892,6.916278,0.519113,7.905518,7.398735,-4.547778,1.867457,4.311488,3.871146,-0.996122,-8.083383,-2.802764,-2.096713,5.964617,2.611391,-1.656261,-5.827739,-7.087314,5.059830,3.736164,-9.560247,9.016738,2.574088,-5.587507,-9.945773,-3.474089,4.087685,4.392153,-5.506149,-7.844507,-9.330585,5.789474,-3.177213,-6.047959,-8.101870,-0.088966,1.096089,-8.363228,-3.111387,2.695343,0.082216,7.070014,-7.209553,-8.946914,-4.052467,-6.186676,-8.574578,3.842598,6.317250,-0.822203,6.746440,3.582414,-9.997993,5.669117,-0.108504,-8.022108,-7.902986,-0.529188,-7.140572,4.798629,1.369121,8.120030,6.499413,9.538670,-0.920620,-8.485192,-2.961091,-0.276683,2.946596,-2.746571,3.079119,-9.825173,-1.405773,-5.604345,5.631739,4.053666,-0.710103,-0.132071,9.186571,-0.798654,4.119890,4.149674,-2.002178,1.211680,1.178025,-9.737414,-5.549658,-4.300242,4.236095,9.466415,-2.911355,-6.024141,-6.562176,5.637700,-1.535537,5.907536,-3.193464,0.923398,0.520161,0.285063,-5.427832,0.848843,-6.240776,-8.008365,-5.406883,-7.333251,-2.329421,7.265686,-2.300885,5.681701,2.493646,-1.621674,2.273009,-9.059248,-4.829828,-2.088597,5.829595,2.030687,6.555688,-0.197597,-3.168690,9.294654,3.343420,1.600140,0.983619,-7.453355,3.139089,-7.536487,-5.732995,1.764538,-5.720283,-4.202969,5.751928,0.476475,8.169044,4.432453,9.183681,-7.432401,4.542552,-8.952898,-0.707894,6.134599,4.951616,1.365263,7.806491,6.997580,-8.404961,4.368269,3.044343,-2.778768,-9.009101,-9.389501,-0.283715,-8.029946,-0.455168,-2.571264,7.941176,9.364978,-5.830828,4.302249,3.576230,1.754932,-1.997314,-5.966377,-9.661165,-1.141532,-0.604656,-8.313316,0.513024,-3.825501,4.681334,6.578660,7.559088,7.672965,6.664851,9.636401,4.504764,-3.762822,4.722109,-4.503344,6.910433,8.027239,8.387514,8.830000,-1.356275,6.847654,-0.528694,6.095255,0.024117,8.510890,7.395432,7.461972,-7.442049,-0.787234,-2.964403,4.200566,7.161957,4.535314,-6.038676,8.732287,8.851173,-7.138192,2.978545,6.223312,-7.415295,5.002473,7.159980,1.173249,-9.931563,2.005710,-8.872459,1.305773,1.824763,-1.868699,2.293588,1.552205,-9.981368,-5.535414,6.013822,-8.080308,0.299855,6.366711,0.352681,-7.465754,-6.071242,-9.182321,-4.434273,-4.111546,3.828630,7.489178,-4.103587,3.591349,-1.067728,6.274042,2.351806,8.396069,2.022568,4.618731,8.190851,8.362941,8.870690,-1.059808,0.776234,-8.347806,-6.344942,0.254943,-4.601205,7.274218,-5.008608,-1.035168,7.273731,-3.303861,-3.562879,8.356553,1.670613,3.637929,-8.977493,-4.190152,-6.490253,-7.885721,-3.554360,1.956814,-8.643032,2.195764,6.975209,-0.852152,-0.178998,-8.024704,-4.123822,-8.206107,-1.916894,2.888591,-0.445775,-3.673849,-4.260418,3.989542,-2.493011,2.467832,8.492095,5.571222,-0.744541,2.038851,0.293636,0.656490,1.281641,0.561317,6.869286,5.565671,0.971395,-0.367989,-2.171184,-6.319860,-4.616155,-9.531408,0.509674,6.638265,1.635995,-5.060292,-4.791432,0.714011,9.948497,9.542507,0.280908,-5.692335,-4.814113,-2.545127,-5.963454,9.858436,-0.448337,7.827301,5.026529,4.804147,5.713936,0.104458,1.449094,-5.417326,-1.468524,3.251985,-2.360606,-0.890339,-3.067268,8.473307,4.867245,6.899642,-0.510153,8.304320,6.998150,8.736320,-3.953296,-3.487960,8.886718,6.696475,-0.628644,2.192005,-0.553237,4.932176,-5.464891,-4.077228,2.152398,9.979849,-8.841750,-3.358238,0.604337,-1.388236,-3.806348,5.094905,8.383188,4.408863,7.861736,-4.858188,-9.216599,-1.805896,6.601709,3.562130,-5.973048,-5.265031,5.229179,5.703123,-2.395771,1.103078,-9.787574,-9.040237,7.616623,-0.288115,-4.170984,-9.285432,-1.895933,1.083566,6.850529,7.587724,3.197464,-5.868203,-4.719060,1.585355,-7.214240,2.253666,9.128865,-9.439479,-2.147685,0.401214,-9.766858,5.865514,-3.805195,-5.280363,9.078361,-3.172704,7.045436,-3.808726,-8.646003,7.635873,-6.542565,2.634144,-5.377243,-5.776943,-2.353410,-0.230132,9.067935,-3.515055,-4.081895,-5.001903,-8.858351,4.889903,8.800255,0.849884,6.163873,-3.165790,1.733203,-2.545396,-0.991263,-5.063528,-9.534821,4.944902,8.377038,-8.074412,-6.378742,5.437512,6.715444,-4.688257,-4.482828,-2.928816,-5.227897,4.234286,-1.794429,-3.495512,-5.540194,-7.996514,5.286169,7.690427,7.946044,-2.500271,-2.680050,-5.114133,-3.584026,-4.797073,-3.186316,6.338934,-1.801269,-9.116452,-1.324379,3.680402,-1.857676,9.011639,3.457047,-5.405986,-1.715489,-4.896162,-9.710887,-1.472229,6.841105,-1.735176,5.625277,7.970700,-4.905927,6.976807,-3.947645,-9.465030,-6.679548,-0.590737,-4.013682,-5.801926,6.492397,6.685379,7.551307,8.351091,-8.314612,-3.175590,4.057808,0.405408,6.873801,-9.346910,1.953387,-7.456281,-3.804793,7.929200,2.092077,-5.923922,-9.742987,0.550705,5.241156,1.794675,-9.589914,-9.133912,7.320816,5.331567,-5.644308,-2.058293,-7.430990,4.382169,2.843445,2.405098,-0.898380,5.143292,5.779583,-3.529797,7.349355,8.130062,1.636442,6.738686,7.880807,3.708767,-2.175342,-2.686382,7.208286,-3.002125,-3.264050,2.113179,9.285164,-5.975605,0.825188,0.789535,-7.273868,-7.051355,-0.234495,-9.629846,2.962650,2.580523,0.822075,-0.609995,0.165970,7.670024,5.440429,-3.572228,3.831685,5.579721,7.584132,-4.083129,9.495389,9.015919,-6.084428,-3.433241,-8.351138,-4.935760,8.496386,-0.414040,8.903926,-5.558256,-8.270682,7.484646,8.278526,1.397291,1.105187,-8.876391,-6.849597,9.981712,6.938883,-7.412679,6.027680,5.676104,-9.538202,-3.328349,2.044314,-6.736185,3.263605,-2.466997,-1.937008,-6.471524,8.986059,0.251328,-6.328991,-4.871124,-2.487069,9.147317,7.004682,-3.776286,-7.667230,2.987699,8.486830,-8.320690,8.924380,-4.810486,-9.091723,-3.909051,9.543003,6.296226,-4.535810,-7.747256,5.894575,-5.208480,-5.756936,-8.018729,9.395890,0.802270,9.544804,-3.375121,-2.192006,-9.810025,5.207768,-2.608216,-3.551057,-1.645942,2.170346,7.318059,3.661745,-7.481856,-7.014829,-1.413958,-8.669048,7.394532,7.063415,0.272419,-8.092641,-4.969249,-3.689546,-4.480525,9.437907,9.340086,5.888496,4.249705,-1.405175], dtype = "float64")#candidate|13971|(1176,)|const|float64
call_13970 = relay.TupleGetItem(func_8720_call(relay.reshape(const_13971.astype('float64'), [14, 12, 7]), relay.reshape(const_13971.astype('float64'), [14, 12, 7]), ), 0)
call_13972 = relay.TupleGetItem(func_8723_call(relay.reshape(const_13971.astype('float64'), [14, 12, 7]), relay.reshape(const_13971.astype('float64'), [14, 12, 7]), ), 0)
func_5673_call = mod.get_global_var('func_5673')
func_5678_call = mutated_mod.get_global_var('func_5678')
var_13974 = relay.var("var_13974", dtype = "float64", shape = (4, 40))#candidate|13974|(4, 40)|var|float64
const_13975 = relay.const(10, dtype = "int64")#candidate|13975|()|const|int64
const_13976 = relay.const([8.623524,8.858073,7.813345,-6.452042,1.595461,4.123832,-9.930668,6.373178,5.122559,-4.943697,-0.685261,1.081213,1.449820,8.034831,5.753982,7.472754,-6.522349,9.291992,-9.477598,-5.101963,-0.566658,-9.348659,-1.437864,2.540535,0.046231,2.881588,4.275571,-3.358749,4.877347,9.596989,5.289818,5.521380,-5.965294,6.742916,6.313676,-3.537664,9.570263,-4.449371,-4.636104,-1.459787,0.557002,8.210379,-6.497516,5.141726,8.205258,-0.301736,8.817299,-1.786718,-7.903370,-4.049322,0.430662,2.668788,-7.254907,-5.283712,9.283990,-7.409185,-4.338266,0.673774,-7.035257,-0.084550,-3.712171,-9.272726,5.431922,3.085659,-7.735553,1.935830,-1.912031,1.432743,-0.696484,4.779655,-5.411147,-3.365873,6.999420,9.634596,-2.942555,3.811638,-4.555496,-4.397254,5.084261,3.556239,8.454576,9.246360,8.526057,-4.163602,5.542712,4.715639,-7.999103,-8.277979,4.530897,1.791468,-1.519875,-4.296644,-8.040174,-2.214017,-8.592532,7.256922,-0.841367,5.882946,2.825807,2.195931,2.477879,-7.945521,-2.053826,7.527647,-8.237158,5.639458,-6.279840,9.628821,-9.775907,-5.146930,0.431094,-8.460638,-4.601905,0.478324,-6.152713,-6.851635,5.990999,0.389705,-8.306607,-3.854743,8.356181,9.921034,5.098418,-8.766947,-5.614596,4.249541,-4.716691,1.019728,7.234649,7.189934,8.498448,-7.100523,-3.181803,-0.913430,-4.074510,-5.101374,-7.523241,6.884986,-2.055514,7.707577,-4.130196,2.855909,-3.805122,-7.784295,9.012853,6.602187,4.492393,-7.361326,3.886237,-7.431655,1.383261,0.196091,-9.979338,3.575854,-0.965630,3.293730,1.349590,-2.278913,7.554402,-1.378412,-5.144446,9.356742,4.340945,3.191856,-5.772484,-5.397940,-5.082598,0.865515,8.523233,-3.341567,9.878810,-5.563460,-0.756997,0.641138,2.681305,-6.305517,0.184844,-6.591893,5.949998,-3.525376,4.867837,5.992855,-7.874499,4.618196,-9.643461,-7.858466,1.536482,-0.989473,0.435068,-8.524519,7.294451,-2.592117,-7.476097,0.415093,-5.074432,-3.434369,9.514787,-2.555858,-0.396790,4.425282,1.084372,8.735518,-1.985847,-5.612776,0.740593,1.584048,5.084850,8.955559,-5.294410,-7.699412,-9.472390,-1.953032,-2.875147,-8.913194,-0.888152,3.985042,2.708600,1.918670,0.594219,7.474233,-7.772753,0.102917,-4.352654,2.570137,-6.812539,3.924277,-1.172623,-8.054059,-1.082406,-6.236345,-9.390853,-5.599567,-3.133831,7.393397,8.295879,-3.565188,6.040340,-4.099185,-1.477169,-6.810505,6.266182,-4.266326,-9.642332,-7.222348,7.158102,2.411775,0.725363,4.538235,6.217772,8.399840,0.369269,-7.954451,6.262684,-0.719827,2.518622,-3.824785,-2.183444,-9.146662,9.024369,-8.817761,4.200659,-0.917365,7.933965,-7.868764,5.742893,-6.719515,8.025873,8.073925,0.742536,0.123613,0.817079,6.360249,-9.908919,-3.222166,-0.790658,-3.757182,-7.867490,-7.905453,-7.381437,1.065790,-0.588059,-9.623751,-2.609851,1.728548,0.734398,-1.803188,-0.793592,-1.824368,-0.684565,8.015899,4.454093,-9.744893,-4.746960,-4.139494,-1.849083,-8.804696,0.376895,-2.852713,8.127596,0.523866,-5.060797,6.412175,7.817361,9.215632,-9.957571,-1.433985,-5.626866,0.011508,-2.744399,5.722241,6.593361,2.718030,-7.807631,1.841805,5.521910,-3.122364,-3.615182,0.316800,-1.970026,9.023930,9.406754,-9.126814,1.627129,-6.274370,0.008798,-2.804424,-2.931035,2.479266,2.358700,-0.116131,3.998912,4.076309,-4.655165,4.554675,2.814559,4.501686,0.145000,7.349649,3.663073,-9.589617,3.246330,-7.701947,-9.309749,3.373824,-1.914977,3.256388,-2.136833,5.518835,3.044575,3.747879,-1.137331,7.735103,7.991284,-4.383342,-8.114805,2.826978,3.110270,4.254759,-6.153822,0.943375,-3.949347,-9.683685,8.999418,4.231384,1.103213,-8.781655,6.346418,2.803858,-7.281591,-4.204929,-2.108559,-1.701293,0.200038,2.352494,-5.060686,-9.663015,4.524713,-3.744201,-2.604391,7.005040,-4.276085,4.117082,6.099306,-1.184904,-2.843238,6.905273,9.504782,-5.043892,8.954118,-1.328943,3.062851,9.707756,9.423077,1.017953,8.398638,9.294857,-8.669705,-8.077566,0.139743,5.957862,8.862302,-1.698715,8.678026,9.748779,6.878031,-6.961141,-2.868574,1.038558,9.435586,7.507581,-6.200945,1.533063,-6.983757,-8.763354,-4.792538,0.575083,-0.399150,-0.209733,4.648634,1.642573,1.699902,8.101369,2.159777,-8.365892,3.697998,6.393268,-1.546382,8.704291,-6.476624,2.611529,0.860441,-8.055903,-0.539555,9.161898,-8.121174,-3.001274,0.603618,6.905339,2.670792,5.589405,-2.753688,-2.654289,2.879900,2.563482,7.157291,4.015619,7.734257,7.315722,-8.786259,8.263671,6.450219,6.969500,1.172418,6.608541,-2.450002,-1.621697,1.207889,2.106077,-7.590624,0.759570,9.335259,-8.647118,-3.017618,4.786423,0.182744,-0.454482,-5.411605,0.484246,-2.012261,-9.572961,1.904210,2.072461,8.121252,-9.592621,5.153922,-6.876915,-5.868351,-3.998635,-5.676358,2.527982,-3.053885,-8.711715,3.496709,7.429890,-2.368323,-6.301741,-5.988006,-7.790093,8.403141,0.717589,-2.954309,8.970946,-0.321448,-7.969909,1.686043,-1.239994,8.088870,9.070419,-1.897147,-3.213925,-1.604362,3.690417,0.283659,0.736728,-0.110865,7.724594,-4.805133,8.861185,-8.966906,8.271805,7.013636,-6.460013,-2.288764,-5.942353,-7.821468,0.439128,4.053204,8.387779,-9.435069,1.866849,3.431347,-0.783821,-5.597279,-8.687339,7.069513,-8.248256,-2.594131,9.399651,-8.692269,7.274463,-3.046845,-4.204843,6.348524,-5.044908,-8.113410,-3.702098,3.705828,9.108212,-2.327128,-4.115466,8.841650,0.949218,6.080212,-5.938521,-7.987980,-6.085038,-8.049000,-9.218680,-7.441770,9.012588,3.868373,-8.453584,-3.112559,-9.134575,-2.327369,-1.599054,3.803928,7.037321,-5.528201,0.379280,3.711993,-5.016070,-3.078315,-8.808351,3.144222,1.154495,2.759626,8.209245,5.470616,3.090541,4.581929,4.173570,6.637016,6.829698,-3.624177,-0.196846,0.233314,2.427281,0.896791,-7.939820,3.333664,0.863842,-5.174352,4.097109,-2.479376,5.581700,-2.805098,7.159099,9.368398,-0.021446,7.565022,9.753418,3.626371,-9.329448,-1.091951,1.836120,-8.290002,0.310862,-7.282439,-1.463909,9.232751,-6.755379,-1.274337,2.689486,-9.227033,0.452686,-5.514599,-1.471050,4.228065,-3.447669,-7.970155,9.122396,1.884140,5.673411,4.513079,-4.979712,5.176084,8.144322,-8.495117,7.264408,-1.427413,-1.432404,9.475776,-0.628690,4.731364,6.066054,-1.823256,-1.047582,6.565229,1.031894,6.323648,0.997058,-3.127119,-5.589978,7.163563,-7.329926,-0.508434,-3.910826,7.053741,-6.786899,6.082013,-0.335609,1.208859,8.786276,-7.598036,7.979503,7.644448,-2.071310,1.442588,-9.176548,-3.538212,-3.496127,-8.452958,0.463637,0.046488,-6.199855,6.916411,7.374369,-5.926054,6.540628,0.282017,-3.664020,5.268876,4.885946,-4.979402,0.669868,-8.398823,5.646817,-1.845874,-5.697432,8.393305,-9.955430,-5.275419,8.339908,0.266590,0.809593,5.319679,8.648616,4.620269,-3.739717,-2.081652,-2.690792,4.336842,9.743757,-7.023611,-3.344211,2.336059,-9.879337,-9.402748,-7.736900,-8.471333,-3.638349,0.977380,-6.735788,-7.184911,-0.113874,-6.900528,0.003008,5.787750,3.009140,3.980860,8.564991,0.690213,-2.660254,6.869386,9.665709,-7.505694,8.428032,6.944724,-3.540162,-3.875047,-5.638430,-1.698841,5.374406,8.896723,9.551459,-6.626139,2.177025,2.903234,9.601281,-2.697648,-0.299725,-6.062344,-8.428219,-9.495529,-5.621646,-7.426774,8.429929,-3.918852,-7.273129,-1.665196,-4.795304,-1.518418,-8.889903,2.727488,-1.510525,-6.827953,7.027981,-0.993464,-0.366622,-3.929454,-0.253025,9.333582,7.287783,-7.073250,3.962129,-7.668103,4.014657,5.000086,-8.157988,5.695376,-1.940929,5.919288,-3.340016,-5.791838,-8.083148,1.640137,4.746416,7.390947,1.707181,-0.069537,-2.654519,-3.861103,5.691244,1.503089,9.120346,-2.756553,-4.600951,5.554176,2.464284,0.692925,-6.427516,-3.800173,2.444162,5.059223,4.373581,-6.821736,-5.162712,5.354709,-2.669136,3.736721,0.469261,-8.024043,8.631275,8.290713,8.517984,6.139803,4.468264,9.087289,6.936576,3.224996,-1.312606,-5.844203,4.785242,-1.362699,-0.035295,3.158322,4.434795,3.396362,6.241571,8.414226,0.386439,-9.764693,8.142610,5.011517,-0.685995,5.332313,-9.586024,2.168454,-9.240105,-3.607818,5.016643,-1.140096,1.451536,-2.903918,-6.820945,0.829454,-2.020192,9.374387,7.140455,-5.934407,8.862290,-6.731770,4.589991,7.864334,3.320068,-0.151658,6.328488,4.199413,-7.331791,9.920032,6.679360,-3.401966,3.136316,0.809927,-7.782369,-7.958995,-2.244105,-0.458790,8.810549,8.672141,6.230264,4.641443,-2.028592,2.831147,-4.261142,-7.873820,9.582291,6.658403,-2.596673,6.726022,-8.551516,-7.823755,-4.456789,-3.778027,0.742981,-7.872420,8.782323,8.733464,-3.846881,-7.764716,-7.491875,-1.222567,7.845501,-9.423904,7.659127,9.733681,3.853641,-3.139662,-8.965156,0.388988,-6.322174,-5.645845,-1.250545,9.188627,-6.299959,2.118304,-0.569360,-9.223424,-8.469977,2.421393,-2.612585,4.091689,1.801745,5.359704,0.958418,3.202052,-4.957234,4.302381,6.108948,7.171291,0.240450,-4.481465,-9.032382,0.400330,6.868804,-7.780260,8.312878,-0.850950,5.252485,-4.502465,-2.371594,-8.125347,3.831900,4.067221,3.396200,-3.978367,-0.437338,-8.037038,1.551177,2.299410,1.793692,-9.358019,9.492969,7.104316,-3.280697,2.356741,7.939334,3.301937,-7.314308,1.451118,8.492299,-9.428547,4.588719,6.176901,-0.840790,0.952142,-5.092955,4.298237,-8.479197,1.372956,-3.358619,-1.415510,-2.605737,3.680778,-8.240562,-7.628195,-6.921111,9.368416,-1.427386,5.488413,7.261063,-5.332724,-0.285426,-6.409940,-3.385132,-4.573851,-2.526647,-4.004778,-0.590343,0.661202,-1.561852,4.345270,-8.900195,-5.621873,6.207626,-2.150798,7.116787,-8.147934,-7.731714,-3.327817,-4.265149,5.382003,9.970287,-4.275323,1.850025,1.812393,1.639994,6.737363,8.270196,-7.286496,5.594536,-3.685082,3.433229,-8.795968,7.883661,-6.736532,9.638951,-4.734318,8.743770,9.115778,2.707181,2.741954,6.315349,-3.362656,-5.282257,5.786671,3.374345,-5.733576,-4.026434,-2.018217,-0.764092,-8.506658,1.638219,-9.168502,6.781404,6.815246,-8.768022,4.807432,5.283471,3.748115,2.945725,5.446459,-5.206426,4.965787,0.097808,-9.830714,7.169824,2.139386,3.276887,7.286697,5.983108,8.920878,6.788069,0.531249,3.829930,8.409141,8.359655,5.927705,-7.355941,7.784426,6.772479,1.602992,-1.062860,6.346692,4.069609,-2.340864,3.469472,-0.884259,-4.193137,-0.396838,-3.263597,-9.270423,-9.828038,4.440697,2.621122,-7.943296,-8.694587,6.483956,3.126454,8.445664,4.036259,2.990615,9.615173,-4.268241,-2.460064,0.037650,-5.520948,-8.700285,-3.874174,6.534285,-9.490754,-1.873950,-0.680379,6.019438,-2.527167,-6.150677,-1.911497,-8.186202,9.548249,-9.188210,5.711770,9.066569,2.493330,5.947325,3.023860,1.886388,-7.004369,2.994140,9.704440,-8.287823,9.104210,-5.304259,7.691919,7.110336,5.937909,-9.507795,-8.047417,-0.486866,5.995044,2.426047,-1.951178,6.281354,-8.910956,1.445859,1.062589,4.459051,-5.950534,7.316244,-9.419457,8.401475,-5.267616,9.881516,4.024914,-8.144072,5.417692,1.546211,3.042053,-1.441046,5.503589,3.842520,-3.091026,2.934533,-3.464912,-3.793284,-8.669000,-7.153727,2.986160,6.259354,5.571834,5.080187,0.809040,8.131052,1.218989,-4.800770,7.753832,-2.805425,-9.327151,6.866738,-0.345257,1.214200,0.280044,0.285840,7.620534,1.662695,-5.096769,8.745023,8.813729,-3.667262,1.408064,-9.383860,0.438357,-4.898677,-3.143502,-7.872956,2.538942,1.226582,-7.906701,6.912829,7.199317,-5.291457,6.255154,6.830384,-4.213448,-1.738556,-6.136335,2.885187,2.910808,5.606931,3.878102,-3.602780,-4.934547,2.949550,-3.946286,-5.292504,5.318658,6.532530,6.145394,7.274165,3.328860,7.354879,-1.686889,5.330754,-4.585404,-3.902566,-2.502679,-5.993394,-0.890917,0.841851,-2.084787,2.772493,3.181849,-3.554212,5.896198,-4.086028,0.123111,9.890698,-5.936438,6.166777,8.171097,-3.043700,-4.829622,-4.634936,-2.633915,9.042731,-6.377715,-3.025572,-2.417146,-8.705832,0.801337,-3.797082,-5.080356,-1.255347,-6.212821,2.648542,6.207414,0.430991,-0.837906,5.810619,-0.876308,4.751788,8.902535,-8.317316,-9.235387,0.654499,8.357813,7.980445,4.981372,5.715126,6.874054,-2.130231,-0.381589,6.942071,1.430949,-7.677203,9.928683,-1.680846,5.735495,-6.652171,3.740853,0.055716,2.163486,-3.447582,5.650675,-1.625512,-4.470350,6.762935,4.391083,0.906469,8.302387,-1.409856,3.251893,3.064013,2.803730,2.276726,-5.157496,5.408956,6.347932,-1.789145,2.184042,8.465009,0.640943,5.800351,6.696068,-8.322088,-5.275880,-7.366179,6.241156,-3.088536,9.844178,-5.116348,3.136244,-2.052774,7.599103,2.769782,9.869343,0.178018,3.170266,8.772098,2.477179,-8.455313,-3.415540,-0.475731,-1.895470,-2.630091,-4.293722,0.756063,6.161450,-9.757579,0.342999,1.491538,-6.400219,5.529689,9.524881,1.032151,-3.834496,-6.259557,-8.086896,7.236115,-2.359364], dtype = "float64")#candidate|13976|(1280,)|const|float64
var_13977 = relay.var("var_13977", dtype = "uint64", shape = (60,))#candidate|13977|(60,)|var|uint64
call_13973 = relay.TupleGetItem(func_5673_call(relay.reshape(var_13974.astype('float64'), [5, 2, 16]), relay.reshape(const_13975.astype('int64'), []), relay.reshape(const_13976.astype('float64'), [1280,]), relay.reshape(var_13977.astype('uint64'), [30, 2]), ), 2)
call_13978 = relay.TupleGetItem(func_5678_call(relay.reshape(var_13974.astype('float64'), [5, 2, 16]), relay.reshape(const_13975.astype('int64'), []), relay.reshape(const_13976.astype('float64'), [1280,]), relay.reshape(var_13977.astype('uint64'), [30, 2]), ), 2)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_13979 = relay.TupleGetItem(func_11293_call(), 1)
call_13980 = relay.TupleGetItem(func_11295_call(), 1)
func_13697_call = mod.get_global_var('func_13697')
func_13698_call = mutated_mod.get_global_var('func_13698')
call_13985 = func_13697_call()
call_13986 = func_13697_call()
func_5673_call = mod.get_global_var('func_5673')
func_5678_call = mutated_mod.get_global_var('func_5678')
call_13993 = relay.TupleGetItem(func_5673_call(relay.reshape(var_13974.astype('float64'), [5, 2, 16]), relay.reshape(call_13973.astype('int64'), []), relay.reshape(const_13976.astype('float64'), [1280,]), relay.reshape(var_13977.astype('uint64'), [30, 2]), ), 6)
call_13994 = relay.TupleGetItem(func_5678_call(relay.reshape(var_13974.astype('float64'), [5, 2, 16]), relay.reshape(call_13973.astype('int64'), []), relay.reshape(const_13976.astype('float64'), [1280,]), relay.reshape(var_13977.astype('uint64'), [30, 2]), ), 6)
output = relay.Tuple([call_13947,call_13951,call_13967,call_13970,const_13971,call_13973,var_13974,const_13975,const_13976,var_13977,call_13979,call_13985,call_13993,])
output2 = relay.Tuple([call_13948,call_13952,call_13968,call_13972,const_13971,call_13978,var_13974,const_13975,const_13976,var_13977,call_13980,call_13986,call_13994,])
func_13995 = relay.Function([var_13974,var_13977,], output)
mod['func_13995'] = func_13995
mod = relay.transform.InferType()(mod)
mutated_mod['func_13995'] = func_13995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13995_call = mutated_mod.get_global_var('func_13995')
var_13997 = relay.var("var_13997", dtype = "float64", shape = (4, 40))#candidate|13997|(4, 40)|var|float64
var_13998 = relay.var("var_13998", dtype = "uint64", shape = (60,))#candidate|13998|(60,)|var|uint64
call_13996 = func_13995_call(var_13997,var_13998,)
output = call_13996
func_13999 = relay.Function([var_13997,var_13998,], output)
mutated_mod['func_13999'] = func_13999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7355_call = mod.get_global_var('func_7355')
func_7356_call = mutated_mod.get_global_var('func_7356')
call_14033 = func_7355_call()
call_14034 = func_7355_call()
output = relay.Tuple([call_14033,])
output2 = relay.Tuple([call_14034,])
func_14041 = relay.Function([], output)
mod['func_14041'] = func_14041
mod = relay.transform.InferType()(mod)
mutated_mod['func_14041'] = func_14041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14041_call = mutated_mod.get_global_var('func_14041')
call_14042 = func_14041_call()
output = call_14042
func_14043 = relay.Function([], output)
mutated_mod['func_14043'] = func_14043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_14076 = relay.TupleGetItem(func_11351_call(), 0)
call_14077 = relay.TupleGetItem(func_11352_call(), 0)
func_13290_call = mod.get_global_var('func_13290')
func_13291_call = mutated_mod.get_global_var('func_13291')
call_14078 = func_13290_call()
call_14079 = func_13290_call()
func_9832_call = mod.get_global_var('func_9832')
func_9833_call = mutated_mod.get_global_var('func_9833')
call_14087 = relay.TupleGetItem(func_9832_call(), 0)
call_14088 = relay.TupleGetItem(func_9833_call(), 0)
output = relay.Tuple([call_14076,call_14078,call_14087,])
output2 = relay.Tuple([call_14077,call_14079,call_14088,])
func_14105 = relay.Function([], output)
mod['func_14105'] = func_14105
mod = relay.transform.InferType()(mod)
output = func_14105()
func_14106 = relay.Function([], output)
mutated_mod['func_14106'] = func_14106
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_14150 = relay.TupleGetItem(func_6751_call(), 0)
call_14151 = relay.TupleGetItem(func_6753_call(), 0)
func_8502_call = mod.get_global_var('func_8502')
func_8506_call = mutated_mod.get_global_var('func_8506')
const_14161 = relay.const([[4,-6,7,2,5,9,3,9,10,7,10,7,4,9,-3,-8,-6,-3,-4,-2,-8,-4,-10,9,4,3,5,-8,-1,-1,-9,-3,-3,-7,-3,7,-9,-4,-3,9,10,-3,-2,-4,-7,9,-3,-10,-1,5,-7,7,1,-7,4,-2,-7,-9,-6,-4]], dtype = "uint64")#candidate|14161|(1, 60)|const|uint64
const_14162 = relay.const(4, dtype = "int64")#candidate|14162|()|const|int64
var_14163 = relay.var("var_14163", dtype = "float32", shape = (280,))#candidate|14163|(280,)|var|float32
call_14160 = relay.TupleGetItem(func_8502_call(relay.reshape(const_14161.astype('uint64'), [60,]), relay.reshape(const_14162.astype('int64'), []), relay.reshape(var_14163.astype('float32'), [140, 2]), ), 11)
call_14164 = relay.TupleGetItem(func_8506_call(relay.reshape(const_14161.astype('uint64'), [60,]), relay.reshape(const_14162.astype('int64'), []), relay.reshape(var_14163.astype('float32'), [140, 2]), ), 11)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_14170 = relay.TupleGetItem(func_7952_call(), 2)
call_14171 = relay.TupleGetItem(func_7954_call(), 2)
bop_14179 = relay.greater(const_14161.astype('bool'), const_14162.astype('bool')) # shape=(1, 60)
func_7355_call = mod.get_global_var('func_7355')
func_7356_call = mutated_mod.get_global_var('func_7356')
call_14183 = func_7355_call()
call_14184 = func_7355_call()
uop_14190 = relay.cos(bop_14179.astype('float64')) # shape=(1, 60)
output = relay.Tuple([call_14150,call_14160,var_14163,call_14170,call_14183,uop_14190,])
output2 = relay.Tuple([call_14151,call_14164,var_14163,call_14171,call_14184,uop_14190,])
func_14196 = relay.Function([var_14163,], output)
mod['func_14196'] = func_14196
mod = relay.transform.InferType()(mod)
mutated_mod['func_14196'] = func_14196
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14197 = relay.var("var_14197", dtype = "float32", shape = (280,))#candidate|14197|(280,)|var|float32
func_14196_call = mutated_mod.get_global_var('func_14196')
call_14198 = func_14196_call(var_14197)
output = call_14198
func_14199 = relay.Function([var_14197], output)
mutated_mod['func_14199'] = func_14199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_14301 = relay.TupleGetItem(func_7653_call(), 0)
call_14302 = relay.TupleGetItem(func_7654_call(), 0)
func_8720_call = mod.get_global_var('func_8720')
func_8723_call = mutated_mod.get_global_var('func_8723')
var_14309 = relay.var("var_14309", dtype = "float64", shape = (1176,))#candidate|14309|(1176,)|var|float64
call_14308 = relay.TupleGetItem(func_8720_call(relay.reshape(var_14309.astype('float64'), [14, 12, 7]), relay.reshape(var_14309.astype('float64'), [14, 12, 7]), ), 0)
call_14310 = relay.TupleGetItem(func_8723_call(relay.reshape(var_14309.astype('float64'), [14, 12, 7]), relay.reshape(var_14309.astype('float64'), [14, 12, 7]), ), 0)
func_8720_call = mod.get_global_var('func_8720')
func_8723_call = mutated_mod.get_global_var('func_8723')
call_14316 = relay.TupleGetItem(func_8720_call(relay.reshape(var_14309.astype('float64'), [14, 12, 7]), relay.reshape(call_14308.astype('float64'), [14, 12, 7]), ), 0)
call_14317 = relay.TupleGetItem(func_8723_call(relay.reshape(var_14309.astype('float64'), [14, 12, 7]), relay.reshape(call_14308.astype('float64'), [14, 12, 7]), ), 0)
output = relay.Tuple([call_14301,call_14308,var_14309,call_14316,])
output2 = relay.Tuple([call_14302,call_14310,var_14309,call_14317,])
func_14326 = relay.Function([var_14309,], output)
mod['func_14326'] = func_14326
mod = relay.transform.InferType()(mod)
var_14327 = relay.var("var_14327", dtype = "float64", shape = (1176,))#candidate|14327|(1176,)|var|float64
output = func_14326(var_14327)
func_14328 = relay.Function([var_14327], output)
mutated_mod['func_14328'] = func_14328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8978_call = mutated_mod.get_global_var('func_8978')
call_14395 = relay.TupleGetItem(func_8977_call(), 0)
call_14396 = relay.TupleGetItem(func_8978_call(), 0)
func_11648_call = mod.get_global_var('func_11648')
func_11650_call = mutated_mod.get_global_var('func_11650')
call_14404 = relay.TupleGetItem(func_11648_call(), 0)
call_14405 = relay.TupleGetItem(func_11650_call(), 0)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
var_14412 = relay.var("var_14412", dtype = "uint64", shape = (560,))#candidate|14412|(560,)|var|uint64
call_14411 = relay.TupleGetItem(func_3471_call(relay.reshape(var_14412.astype('uint64'), [10, 7, 8])), 1)
call_14413 = relay.TupleGetItem(func_3473_call(relay.reshape(var_14412.astype('uint64'), [10, 7, 8])), 1)
output = relay.Tuple([call_14395,call_14404,call_14411,var_14412,])
output2 = relay.Tuple([call_14396,call_14405,call_14413,var_14412,])
func_14426 = relay.Function([var_14412,], output)
mod['func_14426'] = func_14426
mod = relay.transform.InferType()(mod)
mutated_mod['func_14426'] = func_14426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14427 = relay.var("var_14427", dtype = "uint64", shape = (560,))#candidate|14427|(560,)|var|uint64
func_14426_call = mutated_mod.get_global_var('func_14426')
call_14428 = func_14426_call(var_14427)
output = call_14428
func_14429 = relay.Function([var_14427], output)
mutated_mod['func_14429'] = func_14429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13214_call = mod.get_global_var('func_13214')
func_13216_call = mutated_mod.get_global_var('func_13216')
call_14431 = relay.TupleGetItem(func_13214_call(), 0)
call_14432 = relay.TupleGetItem(func_13216_call(), 0)
func_10106_call = mod.get_global_var('func_10106')
func_10107_call = mutated_mod.get_global_var('func_10107')
call_14463 = func_10106_call()
call_14464 = func_10106_call()
output = relay.Tuple([call_14431,call_14463,])
output2 = relay.Tuple([call_14432,call_14464,])
func_14468 = relay.Function([], output)
mod['func_14468'] = func_14468
mod = relay.transform.InferType()(mod)
mutated_mod['func_14468'] = func_14468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14468_call = mutated_mod.get_global_var('func_14468')
call_14469 = func_14468_call()
output = call_14469
func_14470 = relay.Function([], output)
mutated_mod['func_14470'] = func_14470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7205_call = mod.get_global_var('func_7205')
func_7207_call = mutated_mod.get_global_var('func_7207')
call_14517 = func_7205_call()
call_14518 = func_7205_call()
output = call_14517
output2 = call_14518
func_14521 = relay.Function([], output)
mod['func_14521'] = func_14521
mod = relay.transform.InferType()(mod)
output = func_14521()
func_14522 = relay.Function([], output)
mutated_mod['func_14522'] = func_14522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11190_call = mod.get_global_var('func_11190')
func_11191_call = mutated_mod.get_global_var('func_11191')
call_14531 = relay.TupleGetItem(func_11190_call(), 0)
call_14532 = relay.TupleGetItem(func_11191_call(), 0)
func_10909_call = mod.get_global_var('func_10909')
func_10911_call = mutated_mod.get_global_var('func_10911')
call_14534 = relay.TupleGetItem(func_10909_call(), 0)
call_14535 = relay.TupleGetItem(func_10911_call(), 0)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_14536 = relay.TupleGetItem(func_7523_call(), 0)
call_14537 = relay.TupleGetItem(func_7525_call(), 0)
output = relay.Tuple([call_14531,call_14534,call_14536,])
output2 = relay.Tuple([call_14532,call_14535,call_14537,])
func_14546 = relay.Function([], output)
mod['func_14546'] = func_14546
mod = relay.transform.InferType()(mod)
output = func_14546()
func_14547 = relay.Function([], output)
mutated_mod['func_14547'] = func_14547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14546_call = mod.get_global_var('func_14546')
func_14547_call = mutated_mod.get_global_var('func_14547')
call_14621 = relay.TupleGetItem(func_14546_call(), 2)
call_14622 = relay.TupleGetItem(func_14547_call(), 2)
func_13745_call = mod.get_global_var('func_13745')
func_13746_call = mutated_mod.get_global_var('func_13746')
call_14662 = func_13745_call()
call_14663 = func_13745_call()
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
var_14674 = relay.var("var_14674", dtype = "uint64", shape = (560,))#candidate|14674|(560,)|var|uint64
call_14673 = relay.TupleGetItem(func_3471_call(relay.reshape(var_14674.astype('uint64'), [10, 7, 8])), 0)
call_14675 = relay.TupleGetItem(func_3473_call(relay.reshape(var_14674.astype('uint64'), [10, 7, 8])), 0)
output = relay.Tuple([call_14621,call_14662,call_14673,var_14674,])
output2 = relay.Tuple([call_14622,call_14663,call_14675,var_14674,])
func_14681 = relay.Function([var_14674,], output)
mod['func_14681'] = func_14681
mod = relay.transform.InferType()(mod)
mutated_mod['func_14681'] = func_14681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14682 = relay.var("var_14682", dtype = "uint64", shape = (560,))#candidate|14682|(560,)|var|uint64
func_14681_call = mutated_mod.get_global_var('func_14681')
call_14683 = func_14681_call(var_14682)
output = call_14683
func_14684 = relay.Function([var_14682], output)
mutated_mod['func_14684'] = func_14684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9475_call = mod.get_global_var('func_9475')
func_9476_call = mutated_mod.get_global_var('func_9476')
call_14709 = relay.TupleGetItem(func_9475_call(), 2)
call_14710 = relay.TupleGetItem(func_9476_call(), 2)
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
var_14718 = relay.var("var_14718", dtype = "bool", shape = (1008,))#candidate|14718|(1008,)|var|bool
call_14717 = func_1619_call(relay.reshape(var_14718.astype('bool'), [14, 6, 12]), relay.reshape(var_14718.astype('bool'), [14, 6, 12]), )
call_14719 = func_1619_call(relay.reshape(var_14718.astype('bool'), [14, 6, 12]), relay.reshape(var_14718.astype('bool'), [14, 6, 12]), )
uop_14720 = relay.cos(call_14717.astype('float32')) # shape=(14, 6, 12)
uop_14722 = relay.cos(call_14719.astype('float32')) # shape=(14, 6, 12)
func_1996_call = mod.get_global_var('func_1996')
func_2000_call = mutated_mod.get_global_var('func_2000')
var_14731 = relay.var("var_14731", dtype = "int64", shape = (540,))#candidate|14731|(540,)|var|int64
var_14732 = relay.var("var_14732", dtype = "float64", shape = (1280,))#candidate|14732|(1280,)|var|float64
const_14733 = relay.const([-5,-4,-1,-8,-6,-6,-9,-5,10,-7,7,5,-2,9,-10,-2,9,-5,7,-5,2,-6,-2,7,10,9,3,-9,6,1,-6,2,-8,-6,-2,10,4,-4,-6,6,-5,5,10,7,4,3,-2,7,-4,5,-4,10,10,4,-5,3,-7,1,2,5], dtype = "uint64")#candidate|14733|(60,)|const|uint64
call_14730 = relay.TupleGetItem(func_1996_call(relay.reshape(var_14731.astype('int64'), [6, 9, 10]), relay.reshape(var_14732.astype('float64'), [1280,]), relay.reshape(const_14733.astype('uint64'), [60,]), ), 3)
call_14734 = relay.TupleGetItem(func_2000_call(relay.reshape(var_14731.astype('int64'), [6, 9, 10]), relay.reshape(var_14732.astype('float64'), [1280,]), relay.reshape(const_14733.astype('uint64'), [60,]), ), 3)
output = relay.Tuple([call_14709,var_14718,uop_14720,call_14730,var_14731,var_14732,const_14733,])
output2 = relay.Tuple([call_14710,var_14718,uop_14722,call_14734,var_14731,var_14732,const_14733,])
func_14742 = relay.Function([var_14718,var_14731,var_14732,], output)
mod['func_14742'] = func_14742
mod = relay.transform.InferType()(mod)
var_14743 = relay.var("var_14743", dtype = "bool", shape = (1008,))#candidate|14743|(1008,)|var|bool
var_14744 = relay.var("var_14744", dtype = "int64", shape = (540,))#candidate|14744|(540,)|var|int64
var_14745 = relay.var("var_14745", dtype = "float64", shape = (1280,))#candidate|14745|(1280,)|var|float64
output = func_14742(var_14743,var_14744,var_14745,)
func_14746 = relay.Function([var_14743,var_14744,var_14745,], output)
mutated_mod['func_14746'] = func_14746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10490_call = mod.get_global_var('func_10490')
func_10492_call = mutated_mod.get_global_var('func_10492')
call_14825 = relay.TupleGetItem(func_10490_call(), 0)
call_14826 = relay.TupleGetItem(func_10492_call(), 0)
func_13057_call = mod.get_global_var('func_13057')
func_13059_call = mutated_mod.get_global_var('func_13059')
call_14847 = relay.TupleGetItem(func_13057_call(), 0)
call_14848 = relay.TupleGetItem(func_13059_call(), 0)
func_11190_call = mod.get_global_var('func_11190')
func_11191_call = mutated_mod.get_global_var('func_11191')
call_14857 = relay.TupleGetItem(func_11190_call(), 0)
call_14858 = relay.TupleGetItem(func_11191_call(), 0)
func_8630_call = mod.get_global_var('func_8630')
func_8632_call = mutated_mod.get_global_var('func_8632')
call_14866 = relay.TupleGetItem(func_8630_call(), 0)
call_14867 = relay.TupleGetItem(func_8632_call(), 0)
output = relay.Tuple([call_14825,call_14847,call_14857,call_14866,])
output2 = relay.Tuple([call_14826,call_14848,call_14858,call_14867,])
func_14879 = relay.Function([], output)
mod['func_14879'] = func_14879
mod = relay.transform.InferType()(mod)
mutated_mod['func_14879'] = func_14879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14879_call = mutated_mod.get_global_var('func_14879')
call_14880 = func_14879_call()
output = call_14880
func_14881 = relay.Function([], output)
mutated_mod['func_14881'] = func_14881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12235_call = mod.get_global_var('func_12235')
func_12237_call = mutated_mod.get_global_var('func_12237')
call_14890 = relay.TupleGetItem(func_12235_call(), 0)
call_14891 = relay.TupleGetItem(func_12237_call(), 0)
output = call_14890
output2 = call_14891
func_14898 = relay.Function([], output)
mod['func_14898'] = func_14898
mod = relay.transform.InferType()(mod)
output = func_14898()
func_14899 = relay.Function([], output)
mutated_mod['func_14899'] = func_14899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_14911 = relay.TupleGetItem(func_7952_call(), 1)
call_14912 = relay.TupleGetItem(func_7954_call(), 1)
output = call_14911
output2 = call_14912
func_14918 = relay.Function([], output)
mod['func_14918'] = func_14918
mod = relay.transform.InferType()(mod)
output = func_14918()
func_14919 = relay.Function([], output)
mutated_mod['func_14919'] = func_14919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10909_call = mod.get_global_var('func_10909')
func_10911_call = mutated_mod.get_global_var('func_10911')
call_14932 = relay.TupleGetItem(func_10909_call(), 0)
call_14933 = relay.TupleGetItem(func_10911_call(), 0)
func_1619_call = mod.get_global_var('func_1619')
func_1622_call = mutated_mod.get_global_var('func_1622')
const_14936 = relay.const([True,False,False,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,True,False,True,False,True,True,True,True,False,False,True,False,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,True,True,False,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False], dtype = "bool")#candidate|14936|(1008,)|const|bool
call_14935 = func_1619_call(relay.reshape(const_14936.astype('bool'), [14, 6, 12]), relay.reshape(const_14936.astype('bool'), [14, 6, 12]), )
call_14937 = func_1619_call(relay.reshape(const_14936.astype('bool'), [14, 6, 12]), relay.reshape(const_14936.astype('bool'), [14, 6, 12]), )
func_8782_call = mod.get_global_var('func_8782')
func_8783_call = mutated_mod.get_global_var('func_8783')
call_14938 = relay.TupleGetItem(func_8782_call(), 0)
call_14939 = relay.TupleGetItem(func_8783_call(), 0)
func_12343_call = mod.get_global_var('func_12343')
func_12347_call = mutated_mod.get_global_var('func_12347')
var_14950 = relay.var("var_14950", dtype = "uint64", shape = (60,))#candidate|14950|(60,)|var|uint64
const_14951 = relay.const(9, dtype = "int64")#candidate|14951|()|const|int64
call_14949 = relay.TupleGetItem(func_12343_call(relay.reshape(const_14936.astype('bool'), [2, 504]), relay.reshape(var_14950.astype('uint64'), [60,]), relay.reshape(const_14951.astype('int64'), []), ), 6)
call_14952 = relay.TupleGetItem(func_12347_call(relay.reshape(const_14936.astype('bool'), [2, 504]), relay.reshape(var_14950.astype('uint64'), [60,]), relay.reshape(const_14951.astype('int64'), []), ), 6)
output = relay.Tuple([call_14932,call_14935,const_14936,call_14938,call_14949,var_14950,const_14951,])
output2 = relay.Tuple([call_14933,call_14937,const_14936,call_14939,call_14952,var_14950,const_14951,])
func_14984 = relay.Function([var_14950,], output)
mod['func_14984'] = func_14984
mod = relay.transform.InferType()(mod)
mutated_mod['func_14984'] = func_14984
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14985 = relay.var("var_14985", dtype = "uint64", shape = (60,))#candidate|14985|(60,)|var|uint64
func_14984_call = mutated_mod.get_global_var('func_14984')
call_14986 = func_14984_call(var_14985)
output = call_14986
func_14987 = relay.Function([var_14985], output)
mutated_mod['func_14987'] = func_14987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12235_call = mod.get_global_var('func_12235')
func_12237_call = mutated_mod.get_global_var('func_12237')
call_15016 = relay.TupleGetItem(func_12235_call(), 0)
call_15017 = relay.TupleGetItem(func_12237_call(), 0)
output = call_15016
output2 = call_15017
func_15018 = relay.Function([], output)
mod['func_15018'] = func_15018
mod = relay.transform.InferType()(mod)
mutated_mod['func_15018'] = func_15018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15018_call = mutated_mod.get_global_var('func_15018')
call_15019 = func_15018_call()
output = call_15019
func_15020 = relay.Function([], output)
mutated_mod['func_15020'] = func_15020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8553_call = mod.get_global_var('func_8553')
func_8555_call = mutated_mod.get_global_var('func_8555')
call_15025 = relay.TupleGetItem(func_8553_call(), 1)
call_15026 = relay.TupleGetItem(func_8555_call(), 1)
func_13995_call = mod.get_global_var('func_13995')
func_13999_call = mutated_mod.get_global_var('func_13999')
var_15057 = relay.var("var_15057", dtype = "float64", shape = (160,))#candidate|15057|(160,)|var|float64
var_15058 = relay.var("var_15058", dtype = "uint64", shape = (60,))#candidate|15058|(60,)|var|uint64
call_15056 = relay.TupleGetItem(func_13995_call(relay.reshape(var_15057.astype('float64'), [4, 40]), relay.reshape(var_15058.astype('uint64'), [60,]), ), 11)
call_15059 = relay.TupleGetItem(func_13999_call(relay.reshape(var_15057.astype('float64'), [4, 40]), relay.reshape(var_15058.astype('uint64'), [60,]), ), 11)
func_13260_call = mod.get_global_var('func_13260')
func_13262_call = mutated_mod.get_global_var('func_13262')
call_15063 = relay.TupleGetItem(func_13260_call(), 1)
call_15064 = relay.TupleGetItem(func_13262_call(), 1)
output = relay.Tuple([call_15025,call_15056,var_15057,var_15058,call_15063,])
output2 = relay.Tuple([call_15026,call_15059,var_15057,var_15058,call_15064,])
func_15067 = relay.Function([var_15057,var_15058,], output)
mod['func_15067'] = func_15067
mod = relay.transform.InferType()(mod)
var_15068 = relay.var("var_15068", dtype = "float64", shape = (160,))#candidate|15068|(160,)|var|float64
var_15069 = relay.var("var_15069", dtype = "uint64", shape = (60,))#candidate|15069|(60,)|var|uint64
output = func_15067(var_15068,var_15069,)
func_15070 = relay.Function([var_15068,var_15069,], output)
mutated_mod['func_15070'] = func_15070
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_15093 = relay.TupleGetItem(func_11617_call(), 1)
call_15094 = relay.TupleGetItem(func_11618_call(), 1)
func_8296_call = mod.get_global_var('func_8296')
func_8298_call = mutated_mod.get_global_var('func_8298')
call_15099 = func_8296_call()
call_15100 = func_8296_call()
output = relay.Tuple([call_15093,call_15099,])
output2 = relay.Tuple([call_15094,call_15100,])
func_15119 = relay.Function([], output)
mod['func_15119'] = func_15119
mod = relay.transform.InferType()(mod)
mutated_mod['func_15119'] = func_15119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15119_call = mutated_mod.get_global_var('func_15119')
call_15120 = func_15119_call()
output = call_15120
func_15121 = relay.Function([], output)
mutated_mod['func_15121'] = func_15121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12839_call = mod.get_global_var('func_12839')
func_12841_call = mutated_mod.get_global_var('func_12841')
call_15169 = relay.TupleGetItem(func_12839_call(), 3)
call_15170 = relay.TupleGetItem(func_12841_call(), 3)
func_11923_call = mod.get_global_var('func_11923')
func_11924_call = mutated_mod.get_global_var('func_11924')
call_15201 = func_11923_call()
call_15202 = func_11923_call()
output = relay.Tuple([call_15169,call_15201,])
output2 = relay.Tuple([call_15170,call_15202,])
func_15206 = relay.Function([], output)
mod['func_15206'] = func_15206
mod = relay.transform.InferType()(mod)
mutated_mod['func_15206'] = func_15206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15206_call = mutated_mod.get_global_var('func_15206')
call_15207 = func_15206_call()
output = call_15207
func_15208 = relay.Function([], output)
mutated_mod['func_15208'] = func_15208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_15241 = relay.TupleGetItem(func_7523_call(), 0)
call_15242 = relay.TupleGetItem(func_7525_call(), 0)
output = call_15241
output2 = call_15242
func_15250 = relay.Function([], output)
mod['func_15250'] = func_15250
mod = relay.transform.InferType()(mod)
mutated_mod['func_15250'] = func_15250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15250_call = mutated_mod.get_global_var('func_15250')
call_15251 = func_15250_call()
output = call_15251
func_15252 = relay.Function([], output)
mutated_mod['func_15252'] = func_15252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13290_call = mod.get_global_var('func_13290')
func_13291_call = mutated_mod.get_global_var('func_13291')
call_15263 = func_13290_call()
call_15264 = func_13290_call()
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_15267 = func_7106_call()
call_15268 = func_7106_call()
func_13404_call = mod.get_global_var('func_13404')
func_13406_call = mutated_mod.get_global_var('func_13406')
const_15271 = relay.const([[8,-9,7,2,8,-3,6,-6,-10,3,-1,2,8,5,-5,1,8,-4,8,1,3,6,7,6,-1,7,1,-8,-7,2,-4,5,-4,7,5,8,1,9,-8,-7,-3,10,2,-2,3,-2,8,-8,-8,-4,2,-3,6,3,7,2,4,4,2,-8,-2,1,-10,4,-6,3,10,3,7,1,-7,4,7,-9,3,-3,8,9,-4,9,3,8,-7,-1,-8,-10,7,6,9,-4,-3,-1,2,-2,-5,6,5,3,-6,8,-7,9,-10,8,2,-6,-1,-7,-9,9],[2,-1,-9,8,-9,9,5,-1,-5,-6,3,2,-1,4,8,3,9,6,8,-3,-10,-2,4,-2,2,-4,4,-8,-4,4,-8,-1,-2,-4,1,-7,4,10,3,-5,-1,-2,6,9,-4,2,-1,6,-2,-4,-10,7,-10,-1,8,8,6,4,1,2,6,7,10,3,-6,8,7,1,2,-10,8,2,1,-6,9,8,-3,-5,8,7,-6,-9,8,-2,-2,3,-2,3,-10,8,8,-5,8,-6,-1,-2,5,9,1,-8,-6,2,5,-3,-8,-4,-6,-9,-2,-3],[-7,-7,-6,10,10,10,-8,-5,-2,9,9,8,4,-10,-6,7,-7,8,3,-3,-5,-10,-7,-7,3,-1,-9,8,8,-8,-2,-10,1,4,-5,8,10,-4,-5,10,-6,10,1,7,-9,-6,1,-2,3,8,-5,-9,-6,-5,-3,-9,-3,-4,-1,6,5,-1,-5,1,-2,-5,7,3,-8,-6,-1,-9,6,-1,-4,6,-8,-8,-3,10,-9,-4,8,2,6,-6,-5,-3,10,-9,-2,4,6,-2,2,-6,-6,7,-8,9,-9,2,4,6,-1,6,3,-5,1,-10],[9,4,-6,9,-2,-9,7,-6,7,3,-10,-3,-9,2,6,-5,-7,8,1,-9,-8,-5,-10,-6,-4,6,7,7,-10,8,-10,-10,-1,2,8,7,10,10,5,-6,4,5,5,-7,-10,10,-9,10,-9,-4,-6,2,2,-5,-10,6,-6,5,-2,4,-9,-3,-5,8,5,-10,2,-4,-5,-1,-3,9,7,-9,-6,10,-9,4,6,-9,-4,10,2,8,5,2,-8,7,5,-4,-1,6,9,-8,-10,4,8,9,9,7,9,-2,-2,-2,-7,6,3,1,-2,5],[-6,5,4,-1,-3,7,-2,9,-9,1,-7,7,-10,10,-7,-3,7,-4,4,-3,8,9,10,5,8,7,-4,-3,-5,6,1,7,-7,-8,10,10,-1,9,-6,3,2,-9,-6,-3,-9,-7,8,10,-4,-10,2,-2,8,6,-8,8,-1,-8,-3,-10,-2,3,-8,9,3,-6,-9,2,2,1,-9,1,8,-6,4,3,2,8,-1,4,8,3,-10,3,2,-3,-5,-8,-6,5,-10,-6,4,-2,10,-1,6,6,-8,10,-2,-1,-7,-1,-3,3,-5,-6,2,6],[-4,2,10,7,-4,-7,2,-5,-7,4,-3,5,-5,-6,7,-10,-8,2,-8,-5,-8,3,10,-8,6,-9,6,-6,-5,7,4,-4,10,10,6,2,-10,1,3,-9,9,10,3,8,8,-9,-5,-5,-8,-4,-2,8,1,2,-9,5,-10,-7,10,-1,3,3,5,-4,4,-9,4,6,7,1,10,5,-2,-7,10,-1,9,2,1,-7,5,1,3,7,7,5,-6,1,5,-10,-5,-7,-4,-6,-6,-10,-1,10,-10,4,-5,-9,1,10,-8,-2,-1,7,9,-10],[8,-6,3,-3,-5,2,-7,-2,1,-6,-2,1,-9,-9,-4,5,-3,3,9,10,-4,-5,-3,9,10,-4,6,-8,-6,5,-9,3,3,7,3,-7,2,-8,-2,-1,-2,7,-10,5,5,5,-10,4,-4,5,-10,4,6,-9,9,-3,4,-1,6,-2,3,2,8,7,9,-1,6,-1,7,3,9,-7,5,-9,1,3,-1,-9,3,10,8,2,-7,8,-2,-10,-6,-6,-2,-5,4,-8,5,3,1,-3,-7,5,-10,7,-4,5,-3,-5,3,7,10,-4,3,6],[-3,5,3,-3,2,5,9,10,-8,-7,6,10,-3,4,4,-2,-8,6,-8,4,-2,-10,10,5,6,1,-7,-10,7,-6,4,7,-6,3,3,6,6,-6,-5,-4,-2,4,8,-2,8,6,-6,1,-6,-8,2,4,-9,6,-3,6,7,-7,-6,10,6,5,8,4,2,1,-7,4,5,-1,-2,4,-8,4,9,-7,1,7,-10,3,6,-8,9,6,-1,4,5,-3,-10,-7,5,6,-8,5,-7,-1,-2,-5,-8,7,-9,3,1,-8,-6,-2,1,-5,4,-8],[-8,-5,6,1,10,-5,9,4,5,10,9,2,-3,-10,9,-9,6,7,-3,-8,-6,-3,-3,2,-1,1,6,1,-10,-6,8,6,-9,-8,1,7,-10,-2,-9,1,9,-1,5,4,-2,6,6,-8,5,9,-3,-5,9,4,-2,-10,-8,7,3,-1,-4,9,-9,6,2,-3,-10,-5,-6,6,5,8,-9,9,8,8,-6,-1,3,-2,1,-7,-4,1,-3,-7,-5,4,-1,7,-2,1,-4,-5,-10,-2,-4,3,1,-9,4,-3,-2,4,-7,-5,10,6,-8,2],[2,10,-3,6,-10,-8,-1,-3,5,8,-10,2,-1,-5,3,-9,-1,1,-6,8,3,8,5,9,-9,-4,4,-9,6,3,1,-2,-5,-6,1,-6,-8,-8,-8,-6,6,5,6,4,-8,-1,1,1,8,6,9,-4,8,3,1,-10,9,-8,1,-9,8,-10,-5,8,8,3,-8,6,8,-10,1,5,-9,-7,4,-1,-7,-3,4,6,-5,-1,3,-9,-9,10,-10,9,8,2,-1,-6,6,1,-1,1,-3,1,10,-8,10,8,-5,-1,-1,6,-6,10,-4,-1],[7,2,-4,7,4,2,5,6,-5,4,-10,9,5,-7,10,3,-1,7,-10,9,2,-10,1,7,-4,5,-1,1,4,4,-7,-3,-2,4,-7,-7,-4,5,6,-3,-3,6,3,-2,7,-2,3,-5,-8,-6,-3,3,2,5,8,-8,-8,-6,4,-7,4,-5,5,-3,-10,7,3,-1,5,-5,-3,5,9,-2,9,-4,-9,1,9,-8,-2,2,-2,-2,-6,2,-4,-1,-8,6,2,-2,10,-6,9,10,8,9,-3,-9,-10,10,-7,6,6,5,-3,9,-2,2],[1,-3,2,-9,2,7,10,-5,10,4,-3,-6,-6,10,1,9,4,1,3,2,-7,-9,-8,-3,6,-6,6,7,-8,2,-1,-1,5,10,1,7,-2,-4,1,-1,-5,-7,-1,-3,-1,8,5,6,9,-10,-7,8,-3,10,-2,-10,7,5,10,-5,-2,5,-2,9,-5,4,6,-3,-6,3,-3,-4,8,8,-9,1,8,9,6,-3,-7,-7,1,-1,1,5,-5,-6,-8,3,9,-9,1,-7,5,10,-7,4,6,-4,-9,3,-8,1,3,-5,7,9,1,-4],[6,-8,-2,-2,10,-7,7,-7,9,2,1,4,1,-5,-1,-9,-5,-1,-1,-7,-1,2,-2,-2,6,-5,-1,-2,-4,5,7,2,10,9,8,-2,10,-8,2,5,6,-2,1,-9,2,10,-7,1,8,9,-6,7,-5,-8,5,-5,-5,7,-3,-1,-2,4,5,-7,5,-1,6,-9,-4,-8,-2,1,-1,1,9,-9,-5,10,-8,3,2,-4,-3,-1,-10,8,-3,-9,-9,8,-4,-9,-10,9,4,1,5,6,10,4,6,4,-3,4,5,2,-9,-10,-9,-6],[8,-1,-3,-8,-4,-5,-6,-2,1,-3,-7,6,5,4,-5,-9,6,-4,8,-3,8,-3,-6,3,10,-6,10,-3,-9,1,5,-5,-1,-3,-4,-9,6,-5,8,2,4,5,9,1,2,10,-1,10,5,-10,10,9,1,10,4,7,9,1,9,4,3,9,-10,-5,4,3,-5,2,10,5,-4,-1,-4,1,-4,5,10,9,-6,-4,-10,-6,1,2,2,5,-2,8,-9,-1,3,-8,1,2,6,8,3,2,2,5,-1,-9,-7,9,6,-6,-6,-2,6,4],[10,-7,-6,6,10,1,4,-4,-6,4,5,-3,-6,7,8,3,5,-2,-10,-8,-2,4,8,-4,3,8,-9,8,-5,9,-8,3,6,-4,-4,9,-1,1,-10,-6,4,-10,5,2,5,-3,-6,6,-10,10,-5,9,9,7,-4,4,-9,4,-4,-3,-8,4,3,-7,2,-8,-6,5,6,7,-5,9,-7,7,9,-2,8,-2,8,5,-9,-7,9,-10,-3,6,-10,-3,8,-2,-10,6,10,9,9,8,-7,5,-6,-1,-4,7,2,2,-10,8,9,-9,2,-7],[-2,-1,1,-4,-10,5,10,7,4,1,-4,-5,3,-1,4,7,4,-4,5,1,-3,-1,-2,6,-10,9,5,6,-8,4,5,-7,-1,-4,-10,-4,-3,7,-7,-1,-9,-10,4,2,-3,5,8,-4,4,-7,-3,1,-10,-1,-3,-4,5,-7,-10,-3,5,-10,2,4,-2,-4,4,10,4,-8,6,-9,8,9,7,2,2,7,-5,-1,3,-1,1,-10,-5,-3,-4,3,10,-9,-4,9,2,1,8,-4,9,10,9,8,2,-8,-6,6,2,1,10,-3,7,-2],[8,-5,-3,9,-7,-9,-8,5,5,10,-1,-5,-10,-3,-4,1,1,1,3,8,-6,-10,4,-10,9,8,10,10,2,8,-8,-8,-9,3,-8,3,-9,-2,-2,-2,2,-10,-3,-6,-6,3,-5,1,9,-5,8,-4,-5,-8,9,-8,1,-5,10,1,8,-8,-6,-7,6,3,4,-8,2,-3,-7,-3,-9,-5,2,5,-2,2,-3,-3,3,-2,3,-5,6,-7,-9,3,9,-8,-6,8,7,5,1,10,6,-2,-2,6,-6,-2,3,4,-1,-2,7,-4,2,-6],[-9,-10,8,6,8,7,8,1,-5,5,7,-5,-9,-1,-10,5,-3,6,6,1,-7,10,-8,-7,5,-10,-9,-9,4,1,-6,3,3,1,5,-7,-10,8,-9,-2,-6,1,5,-6,-1,-3,7,-6,-7,-2,-7,-5,-8,-9,-7,-3,3,-8,5,9,5,1,-10,-2,4,-9,5,-9,6,-1,-9,6,8,2,10,-7,3,-6,-7,-10,-6,-3,5,-3,-10,-4,9,-2,-3,-2,8,-1,9,4,8,8,-4,-5,3,-10,4,-3,-5,2,3,-5,3,-2,1,-10]], dtype = "int16")#candidate|15271|(18, 110)|const|int16
call_15270 = relay.TupleGetItem(func_13404_call(relay.reshape(const_15271.astype('int16'), [1980,])), 1)
call_15272 = relay.TupleGetItem(func_13406_call(relay.reshape(const_15271.astype('int16'), [1980,])), 1)
func_9097_call = mod.get_global_var('func_9097')
func_9099_call = mutated_mod.get_global_var('func_9099')
call_15277 = func_9097_call()
call_15278 = func_9097_call()
uop_15286 = relay.tan(const_15271.astype('float64')) # shape=(18, 110)
func_8630_call = mod.get_global_var('func_8630')
func_8632_call = mutated_mod.get_global_var('func_8632')
call_15289 = relay.TupleGetItem(func_8630_call(), 0)
call_15290 = relay.TupleGetItem(func_8632_call(), 0)
func_10577_call = mod.get_global_var('func_10577')
func_10582_call = mutated_mod.get_global_var('func_10582')
const_15296 = relay.const([9.514207,-9.357996,9.711887,6.216772,-0.243232,8.408192,4.509844,-9.956705,7.119789,5.288217,-3.457263,-0.473474,4.430949,9.567844,-2.736002,-1.834957,-0.728164,-1.533576,-9.066625,0.579402,-3.160289,8.990826,7.795940,-1.324829,-2.716807,-2.324397,4.002582,6.580549,-7.497716,9.255231,-6.684707,-8.505967,-3.976636,-8.019647,5.402198,-0.409136,-7.730901,7.604461,4.284516,-3.475913,2.901192,-7.597294,-0.428621,-3.064902,7.162507,0.297218,5.792557,-4.775123,-3.777820,8.965594,-0.963886,-0.419467,6.781308,6.245002,0.190262,-2.837263,-8.781878,7.623256,0.880149,4.649642,8.560218,-8.672537,5.235284,-0.633374,1.588413,2.495100,6.140993,-9.960627,1.582009,4.337439,2.051735,-9.758206,2.583378,-5.493156,6.313384,2.377743,1.727347,8.812989,-6.368676,-4.384153,5.240248,8.741435,2.011106,4.716247,9.008296,7.487045,1.126183,3.103315,5.751088,5.857047,4.965993,9.767037,-2.281812,7.303684,3.378883,-4.573702,1.263060,1.801722,8.436931,-1.215242,-1.385758,8.049546,0.711707,-4.805943,2.857008,9.792072,-8.315111,9.972951,4.102103,7.093016,-4.512608,-7.394484,9.919381,9.788173,-6.516379,-1.727467,9.761790,-6.314082,-5.870604,-7.115204,-6.685180,-2.956502,-0.973208,9.494540,6.382957,-0.596239,-0.180919,4.404280,9.921280,-5.600283,-6.934119,-3.615028,1.012496,-4.496060,3.365565,3.010355,-9.511354,-9.403944,3.240734,1.164617,-4.513613,-4.725082,-8.967274,-4.374717,-2.094330,1.238595,7.146442,2.988366,4.202084,-4.588538,-1.557564,-9.370898,-7.085342,9.792658,3.770802,-3.054158,7.494492,-4.301071,-1.729185,8.034710,-4.092271,-8.007565,-8.455371,-7.654977,8.959878,-9.486142,-6.989688,7.598628,9.190541,-6.737155,4.323536,-2.205246,2.760625,-3.082356,9.629751,8.036872,-0.734445,-5.367699,5.861956,-0.467718,7.621426,-9.807491,-4.886476,-4.303373,-3.765987,-5.524622,4.790468,-9.957240,0.868218,1.625041,-5.581337,-6.794234,-8.158178,6.319353,5.746293,-7.570817,-1.147053,-3.427325,-5.662553,-6.363331,6.908480,-3.167541,4.301341,-4.719594,6.357986,-0.578413,-7.425489,4.309879,3.048002,-3.317865,-7.320427,6.467129,8.111617,3.539656,9.854576,-4.874845,-8.785717,7.554457,-6.237691,4.337160,7.991235,0.397499,-1.092376,-3.481037,-8.206241,1.562375,-1.602519,8.275344,-7.952122,5.501204,5.327711,5.490593,4.436748,8.734966,-2.589027,4.783975,-2.283418,7.544982,5.329270,-1.876390,-7.175545,4.845327,2.210406,-4.679704,1.401086,3.468319,8.229905,3.918546,1.254679,-7.378604,5.269502,-3.050201,7.924706,-0.196265,0.173141,-1.234014,-8.372378,-9.456944,-7.143851,-5.272386,4.472244,-1.019415,-9.055002,7.440614,8.051138,1.004403,1.350230,-8.439008,2.012322,-2.433190,-7.436311,-0.804221,-9.317061,-6.007633,5.901508,-5.757052,-3.297042,9.920506,-9.790310,-5.778134,6.861158,-4.263040,3.152002,0.324225,-0.983356,-4.506009,-4.437193,1.722322,1.398175,1.245157,-0.299158,9.735943,9.635012,1.919881,4.659454,6.255720,2.950843,-7.010957,-3.448261,6.198687,9.253993,8.288408,-8.723620,-3.885297,-9.373114,-7.820733,0.839206,0.716779,2.561810,2.270179,3.503815,3.840904,-1.757146,3.516400,4.684685,1.314170,-4.049560,-6.270244,-7.001059,1.650457,-1.062425,3.519628,4.353853,-7.624029,-8.991789,-1.875059,-3.175144,-6.137740,3.985861,-0.421882,8.846626,5.245793,-0.594758,-0.219619,-3.516096,-9.861963,-7.027259,-9.982328,-2.142722,-8.099778,-9.959597,-4.816629,-2.649302,-4.327005,2.966597,-0.633939,-0.331662,-6.830518,1.978257,0.988368,-6.700657,-8.508805,-5.165351,0.071941,-8.475555,1.919423,-1.698118,8.169847,-8.796648,-8.120717,-2.721410,-2.539589,-6.593693,-1.328013,-5.423390,9.131565,4.047784,0.564009,-7.967937,-5.084409,-3.917807,-7.779315,-9.109735,1.337946,1.197598,-4.509624,-5.508816,-4.103731,6.451606,-1.724794,2.101360,3.169406,5.533763,-4.906979,8.412410,-9.444788,-4.561958,-8.373480,7.120529,0.520159,8.395492,-7.016627,7.097630,-8.499708,4.879306,-0.712621,-4.650237,8.116143,-0.578147,2.678075,2.613779,4.735533,-8.883773,-5.217139,4.896672,-9.889650,2.795036,-0.218757,-7.423754,7.599317,2.052485,-7.181378,7.261991,5.519587,9.651664,6.677086,5.810678,-7.631551,-5.414268,5.856863,-1.328482,-6.118324,-8.398481,-4.920895,5.052192,8.565328,3.515215,-6.284063,9.038384,-2.153389,4.401913,5.870816,-0.618391,-6.862488,-8.855162,-7.937266,-9.184500,-1.494504,9.460534,9.827873,8.165877,2.064262,-3.207962,7.030011,-5.807188,-2.042084,-1.761906,-0.782738,3.748327,9.375591,-0.049624,-8.035252,1.598408,2.672238,-7.079180,8.335924,4.474950,-1.695108,6.433149,-6.938988,-0.771678,0.386142,-1.386673,2.365899,-8.274041,-4.259392,3.206323,2.947414,8.690604,5.962851,1.480380,6.608490,-0.322269,-7.244585,-3.495437,5.440740,5.889480,0.991558,-7.985219,2.816624,3.174515,3.259678,9.323622,2.309155,2.567180,-9.336855,-6.430243,-2.939638,3.380617,-7.536227,5.834205,-8.399884,-7.426446,-6.999876,3.351092,7.004075,9.912343,7.852555,-9.590892,-2.950608,8.663802,-9.176025,-1.892531,-5.371999,-3.315281,0.397933,-3.091897,-0.365102,2.817320,9.478638,3.228336,-9.384639,5.941666,6.606813,-5.441796,-1.479970,-8.700328,3.361858,0.469835,-1.849080,-0.940117,3.143531,-0.685060,2.427090,-2.240308,-1.412731,-3.887907,1.310942,-2.942207,6.509213,-4.361999,-7.736316,-2.531632,8.350439,-2.713784,1.379062,-9.935206,1.811044,1.220967,-7.703321,-1.044487,6.789431,8.057912,-5.957417,8.870978,7.288886,9.786419,-1.180738,7.260997,5.452146,0.195445,0.318593,7.062882,-6.318997,9.177640,3.360393,8.036078,-8.802211,0.878729,-7.748473,-5.340872,-0.426106,-6.966039,-4.280910,-1.252923,8.101348,-1.654970,8.413866,5.955455,-8.884804,6.322615,-6.963839,-8.019941,4.191134,-4.854799,-0.934662,1.435426,-2.133527,3.119380,-3.347028,9.322976,-2.521338,-7.934736,6.975918,3.841244,-5.210140,2.441249,-5.937471,-0.292120,9.860823,3.135732,2.486650,-9.066649,-0.765344,-1.687247,-2.735815,-8.341902,-0.718448,-6.949137,7.672926,9.936681,-3.785195,-7.909105,9.388803,6.471649,6.963135,-1.689050,9.895124,8.132156,3.813429,-6.582015,4.896938,-6.657877,8.045096,0.013811,-8.206559,7.260379,-9.951714,3.073056,-6.912548,-6.724111,-9.645425,-5.471009,-2.256249,3.839258,-9.874810,4.711343,5.228186,5.607081,-4.789912,0.550179,1.315348,-3.117120,-5.991302,6.364481,-8.491924,0.949894,6.788836,-1.421728,5.959927,6.315631,-1.284007,3.565466,-9.086824,-2.815977,5.352743,7.287073,-5.407281,-3.338574,-5.231817,0.391695,-7.661174,5.344301,9.411553,5.603939,2.450792,-4.259536,7.204710,1.252366,-4.386038,-8.309997,3.786949,-4.007538,3.990388,2.119919,3.591751,-1.888268,7.729557,6.164536,-8.281870,7.701613,6.758457,7.503177,3.994853,-6.313920,-2.234443,0.526232,-1.358499,-9.751461,2.854203,7.630744,-9.708244,-4.939127,0.245071,-3.024757,-2.332690,-3.017388,2.567517,-1.863509,-6.811759,-2.310721,6.389235,4.318370,-8.516888,-1.745248,1.582491,-2.489879,4.365940,2.719145,-8.735921,-0.010311,2.444921,-3.118191,-3.355438,4.734531,2.421243,-5.322219,1.778951,-1.440123,0.872051,3.184277,0.770766,-0.505965,-5.342703,3.536309,-0.016594,7.111887,-4.837640,-7.434789,-2.450626,-1.079719,-6.472933,1.983133,-6.905497,9.908020,-6.547096,-1.038497,-1.067420,-8.337804,-9.907441,5.354314,-8.778901,-3.744420,-1.600393,2.473973,-3.784894,-4.433528,-2.922975,-9.980805,5.315385,-2.236827,4.391370,7.114541,-6.576698,-7.923107,-9.335883,2.021412,6.270786,7.764064,-2.703747,-6.613724,-1.862029,2.249522,-4.432549,0.131578,8.725717,4.694644,-4.890770,-5.480370,1.007233,9.052933,-9.084496,-7.269807,-8.402724,1.302781,-9.706752,8.946799,-4.819638,-8.524215,2.671447,9.870750,0.642739,1.335542,0.517234,-0.877654,-4.866970,-1.522648,-4.782930,-9.507722,3.357355,-1.174295,-6.837647,-9.716302,-0.640065,5.203446,5.861156,1.557344,-2.563808,-5.049676,-4.355428,-8.525082,9.916579,-9.493266,1.950460,-0.242895,-1.054804,-9.466965,8.404675,-4.240809,0.418044,9.327668,-2.392372,-1.359837,6.506383,-0.027675,0.738963,-3.270258,-1.747736,7.070083,-4.194685,-3.711169,-0.613368,9.832847,4.862592,7.954641,5.023279,6.661074,6.560728,-6.260119,1.921843,2.113510,9.548013,5.666331,-8.632040,9.732971,-7.695935,1.018808,6.801310,-9.186838,-9.010306,6.800827,-5.239656,0.624651,-7.605569,-6.582370,0.323054,4.936011,-8.259461,-3.854521,3.984654,8.040704,9.426984,-5.717107,1.478885,5.415431,-7.997255,7.424036,-9.238275,6.211189,1.791719,-0.484309,1.720605,4.875883,-2.444950,-2.313907,-2.414223,3.883503,-0.924401,-5.908408,0.220364,-5.487062,-4.689304,-2.832566,-6.130998,-0.285674,-4.033285,-6.508661,-1.060194,3.318477,0.744136,-7.913833,8.903005,0.858235,8.017892,0.387850,-6.655038,-8.412742,6.776659,9.234238,-8.606331,2.891506,-1.108429,-1.895883,-7.340839,7.741206,8.309155,3.601502,7.438627,0.872959,-1.123466,5.323159,-0.824950,5.331624,8.854085,1.929413,-1.881047,-2.863601,3.704176,2.116376,-5.759229,4.447504,-7.762626,-7.186375,-6.661602,-3.771582,-9.937903,0.509065,-9.601311,-8.668697,0.632866,1.545625,2.689140,-6.875095,4.007138,-3.940513,-6.874793,4.394352,-5.646331,-6.785730,7.738443,4.627501,2.361237,-4.189026,5.143749,6.503886,3.813632,7.057833,-0.682403,9.097699,9.075887,2.724953,0.579465,2.882687,-2.805894,-0.955849,-7.562994,0.147597,-2.402413,3.108189,-7.127451,-2.581275,-1.387249,-6.191484,1.450881,-1.174417,0.123435,-8.994937,-8.209277,-3.223355,-5.480829,9.360884,-3.765984,-7.418865,-8.625744,3.267855,-6.587914,-0.278083,6.263552,3.864313,-6.795687,7.929733,2.812914,3.008899,6.084531,-7.721525,-7.781562,0.827999,-5.257207,-8.692193,8.184789,1.359192,0.938643,-6.154701,1.709135,-8.162364,2.906931,3.512524,0.633521,8.718589,0.852522,-1.911973,2.515651,-5.382032,1.318888,-2.369248,-9.734632,-3.722969,-1.495019,-8.904074,-1.054420,3.569300,1.139590,-6.716568,6.191316,2.013593,9.304426,0.424091,8.679449,-3.469115,-9.141229,-8.882526,7.352096,-3.218261,1.665003,2.024388,2.187861,-2.339345,7.828403,-9.225787,-8.701228,4.574034,8.228076,-2.708586,2.860409,-6.811421,3.504777,-2.770369,4.389645,-2.336146,-6.659023,3.616849,8.748764,-1.353276,-2.055853,4.147931,-4.640594,5.334455,1.467994,5.826056,-1.981263,-5.357804,-4.917895,-5.759523,-1.237295,-3.688720,-5.219590,-4.554814,6.520632,5.871549,6.971894,-6.330449,3.333276,-3.539108,8.925929,1.008101,7.377335,-4.643967,5.003249,3.886022,8.952056,-5.948338,6.117066,8.818751,8.354936,8.194591,-2.192708,-7.819043,3.491063,-3.490373,-2.308176,-5.988203,-2.851057,8.353195,-0.923154,1.949955,0.160756,9.803044,-5.099143,3.059491,7.215417,4.080977,4.039657,-0.773521,-6.725574,2.978985,-1.875576,-5.961997,-2.418553,-1.358291,-5.937227,3.646555,3.954250,2.367820,7.253740,0.212322,7.801969,-4.880757,7.664661,0.330078,-9.778128,-1.112307,-1.956083,2.256892,0.038886,5.656722,1.758392,4.887738,-6.138363,-5.138966,3.078277,-5.911507,-2.033872,3.844878,7.757437,0.434631,-4.602074,8.855094,-7.089028,3.629595,-7.501546,-6.651509,4.695007,7.436837,-7.220236,-8.378082,6.276661,-9.908210,3.884073,4.773884,-3.495145,-5.645613,5.799389,4.284242,-4.923485,9.138895,-0.796949,-9.239880,2.768246,0.296666,-7.244330,3.671795,-2.391044,9.089852,-1.901271,2.591914,-7.038988,8.096747,5.610247,2.656327,1.108233,-4.252802,-8.647057,-1.167779,-7.464829,1.434625,9.077167,2.214393,-4.693432,8.696112,8.351879,4.760587,0.083063,6.781592,-2.444248,-8.057352,4.343517,6.011443,-2.011078,0.455718,3.027424,1.344875,-5.176006,-2.332284,0.406658,8.204077,-6.812811,-0.142649,7.157620,-6.654206,7.691363,6.578480,-1.099654,-1.341802,-4.783559,4.211569,5.623986,-5.867112,3.285431,-6.739637,9.822590,-7.207186,6.703681,4.575655,-0.190954,-9.892978,-9.679816,1.962148,-8.705113,5.211268,6.380002,-8.961776,4.468675,-4.176313,0.253704,-7.686124,-8.451753,5.112193,3.450769,-8.908330,-9.330860,9.343182,1.087186,8.755264,4.851601,-4.052626,-3.837166,8.918923,-8.751440,-6.153025,-8.212719,-2.373438,6.990829,-7.470919,-2.628285,2.440681,8.139774,8.538212,5.736555,-3.032868,-1.999216,7.243178,0.998640,-6.776697,2.425866,-0.814255,3.526632,-2.730873,-4.309790,-3.850582,-0.703325,6.157372,-0.106409,-7.302238,-0.993215,-9.460754,9.099308,5.166186,-5.033882,-6.431507,-3.219262,-9.260354,6.093926,4.114789,6.521053,-0.846233,8.150739,-3.036817,5.586667,0.755954,0.143925,-5.009995,3.494891,-3.501154,4.160499,5.600369,9.259614,-1.589563,5.962807,-2.341822,4.066411,-1.417944,-4.071116,-8.740823,3.814946,2.012544,-2.167065,0.028609,7.758830,2.651808,0.443180,9.103240,-1.769344,1.107733,0.167867,9.004489,1.647991,8.748653,-0.727868,0.548542,2.989608,-3.912040,-9.034612,4.263567,0.545189,-4.349766,-0.975166,2.080901,1.696820,-4.791395,-8.887388,2.617099,1.170897,-2.320958,8.704259,4.387005,-6.880894,-4.873384,7.670757,6.686015,-9.703439,0.166893,5.901927,-0.896094,-2.952688,3.916697,-2.378095,-5.871592,5.906095,7.665063,-8.006178,0.279965,-9.888804,9.883533,0.831382,8.520314,-6.935240,-4.526105,2.957347,9.847002,0.779850,8.969927,9.488560,5.131502,-3.975494,3.644092,4.921977,7.911363,-5.882192,-0.120793,1.306849,-6.266443,-9.485374,1.779499,2.183216,7.259866,4.521555,-1.709601,-2.246745,5.968559,-4.272754,6.664995,7.734757,2.724854,4.370023,-6.412078,5.177972,5.757859,0.522594,-7.124731,5.057078,-6.789166,-3.063711,2.152579,-7.913361,6.660341,-6.067058,5.973898,0.559363,8.630791,-8.815558,-9.177063,-0.123604,6.635106,-6.867471,-5.073976,-0.544751,4.919698,6.901057,2.598321,1.938783,-2.724416,-6.924638,-5.899542,7.906131,-6.745412,9.881691,8.045633,-6.150567,1.957011,-7.232896,-6.739863,-8.182125,3.085882,4.018982,-8.002233,2.484464,-0.897854,-6.061901,-0.820456,-6.456205,0.459810,5.674896,-9.473014,5.362888,-0.528555,6.671060,-2.082836,-5.711291,-8.973538,1.109106,6.083148,6.976584,-2.922623,-2.193829,9.706992,0.069973,-1.474419,-7.388976,6.226783,-5.652883,5.733945,-7.020843,-6.241401,-0.060200,-6.977140,3.229088,-3.378321,3.918449,-0.066219,2.655177,2.019485,-9.715210,5.587849,-8.344711,-1.967351,4.217940,-4.571798,-0.848381,-0.696328,4.324715,-6.171728,-3.411086,-8.345876,2.990615,4.446128,-0.115061,1.392732,-4.412839,6.958417,3.485991,-4.378255,-5.375978,9.317377,5.401175,9.569143,-7.525619,8.136622,-7.346261,7.755933,-6.626013,6.625962,1.276821,2.563616,4.492786,-2.584408,-7.523427,1.060360,9.619533,8.765077,7.367263,-9.537709,-6.643508,-8.180305,8.344916,-1.130498,7.065992,-7.913544,9.283993,-3.547013,1.112264,3.523356,5.387979,-1.326790,1.224149,3.928585,-3.285292,7.573581,9.896432,5.316790,9.209966,-5.362815,8.698268,5.683587,-1.621929,-3.125532,-3.938978,-6.617029,-5.853822,-8.471651,-0.855125,-4.351690,8.474698,-4.414622,-2.223629,1.495337,1.796508,-2.356538,3.949333,8.671727,3.433724,5.928727,-3.279348,-8.052707,-2.929384,-1.668578,-1.914487,9.534893,-0.808503,4.516111,1.624079,-5.107199,-0.281623,-4.393802,-8.924832,-7.964409,3.930034,2.399426,4.729137,-0.005604,8.433246,-4.323418,-9.254422,2.620420,8.386108,4.566250,-9.299301,-4.949851,-9.104532,-6.032399,-6.794818,-3.912798,-8.824460,9.800940,9.169010,3.541740,9.095992,2.599318,8.539378,-5.526806,9.709935,1.180548,-4.947073,-5.691284,-7.397223,2.154631,3.890187,-7.625939,-5.209348,0.647211,-1.154240,-3.895832,4.751915,5.747995,-7.563113,3.710867,2.601471,0.051478,-4.508279,-8.846842,-4.511309,-7.208337,9.220391,4.129644,-4.578156,-3.208868,7.630924,-3.083927,-0.920913,4.815399,-6.251808,-2.593707,-4.971678,0.753461,1.116450,5.016047,3.897977,-3.771352,5.586039,-5.347597,-5.965697,-1.484565,0.115927,-2.424599,-9.100172,4.034284,4.172787,-0.415378,7.058591,-3.893894,2.510415,6.150335,6.153056,4.817790,3.769941,5.346312,-6.431988,-9.133722,-7.588175,5.601121,-2.071325,9.627489,-4.571875,8.142117,8.137134,4.461440,-1.561240,-2.457102,-6.103679,-4.938933,9.295373,0.179293,8.598314,-1.733398,9.196421,-1.601952,-4.756761,3.821932,3.014578,-9.905360,-7.304237,2.294513,-2.460166,0.430741,3.143360,4.530787,0.422572,4.925777,-8.727993,-5.448266,2.346422,6.963871,1.134840,6.729686,-3.699383,7.775123,4.315518,9.115467,-2.986713,-0.379881,-6.569616,7.905172,-1.754710,-9.051882,-9.779743,-3.223235,1.863789,6.266571,-9.669953,4.280777,-8.412723,-2.434168,5.012846,-0.743354,-3.171431,0.509680,-1.358145,-6.224147,9.469094,6.373024,2.202392,-0.089518,1.297726,2.844344,-0.052009,-9.055535,-4.951832,-5.331832,-9.484596,4.531947,2.939739,3.004263,8.730938,-7.573497,-8.952911,-5.808554,-7.075849,-9.769324,-2.026298,1.816351,-7.391895,-7.892988,-2.007657,-4.338389,3.025066,3.024751,8.870270,-4.570674,-0.688127,9.679785,-0.881657,4.835961,-9.905353,-0.014241,4.869250,2.338194,-7.654526,-5.509451,-3.909480,3.815126,8.438247,-2.223426,-5.440572,6.606795,-3.093140,9.998220,1.239778,4.338240,8.075088,-1.377981,0.172244,-1.827868,6.958674,9.481054,-0.461884,9.041734,5.101233,-2.787386,-9.598969,7.219918,-8.592644,4.942687,3.783342,-0.454243,8.747085,7.786065,-6.084307,-3.846425,9.076447,-8.486628,-5.693888,6.827341,2.165729,4.037581,7.416269,-3.117131,-2.031831,6.260937,-5.400501,-9.828566,5.390572,9.325860,3.812045,8.919815,5.332173,-0.475304,-0.699233,9.166687,4.641250,7.351207,0.733185,9.687296,-2.821907,2.475645,-6.023477,-5.003705,-7.011406,4.121582,5.445881,-8.417493,-8.979937,-5.751434,-6.285685,3.169333,7.593473,-8.834451,-6.171644,-8.451596,4.542780,-2.227867,2.166912,0.780651,-8.877760,9.195331,5.711404,-4.601775,0.087360,-7.172276,-4.193933,9.191865,3.940291,5.043253,0.363878,-9.070710,6.472865,-5.458471,8.771560,-4.318914,4.913782,7.533495,0.432459,-5.354554,-1.676661,-3.047724,-4.836922,-8.759488,-6.163251,-1.451125,2.653752,-1.241175,0.618971,5.741459,-1.759778,-9.533371,-5.461212,-9.294545,4.121511,-5.745607,-4.360026,-8.571949,-5.643889,-7.474193,-8.029877,5.114653,6.331850,5.142388,-2.755754,8.298078,-6.267618,-3.317345,3.801862,9.079569,-1.481340,-4.639288,-5.395799,3.671441,-3.568762,3.912138,-2.912850,-2.380947,-4.003421,-9.779867,8.278911,4.011446,9.455497,-7.264986,4.449253,1.980548,8.143237,-9.413785,2.801545,-1.566840,4.469974,-0.746452,-3.944174,2.410999,-6.609052,-9.211878,9.708996,-7.564315,5.331426,0.317573,-4.586665,-8.701757,-5.333742,5.175166,9.686769,8.615132,-2.454280,-4.035816,9.805694,0.508878,-9.520280,2.655188,-2.403598,-6.575247,-0.009916,-7.851743,9.556667,-9.747530,3.943065,8.096334,2.493794,8.851020,-1.225671,2.203736,4.002143,-4.718176,-8.449058,2.854341,8.714460,-3.057684,4.218741,-3.712849,-5.995759,-2.147714,-3.349689,-0.515300,2.841105,1.065679,6.487826,9.033166,-4.174455,-0.965719,3.716029,8.739997,-0.277348,-5.073493,-1.626639,-9.360303,7.719796,-5.629760,-0.094038,6.777836,-0.699315,3.172562,3.000095,-8.395164,-8.875142,-0.805826,-5.674502,-1.632356,-2.057254,-3.988558,4.438349,1.827833,1.170480,7.731177,-9.949932,3.097496,6.736056,-6.088200,1.584168,-8.187684,-1.036852,4.893317,-6.310369,7.483526,-5.264230,9.890109,-6.005077,-3.482583,-8.648454,3.163525,3.812770,3.454715,2.059907,5.615364,-8.245394,3.507208,7.570497,3.349887,-5.450354,-2.441143,-8.941200,2.649716,-5.220190,2.422651,3.188751,4.735307,6.185170,2.537662,-8.358711,-3.430488,1.480399,0.716889,-9.030425,-6.169050,7.979262,-8.732094,8.468383,-1.999165,7.382795,-1.320582,-8.450403,5.849200,4.269301,2.673229,-5.826982,-7.596277,8.788023,-9.971183,4.840317,-7.546505,7.878735,-4.444607,-1.132523,-5.077286,-5.101825,-5.921252,-0.718429,3.028403,4.052153,0.762586,-8.382669,8.054268,-7.199507,5.346518,-0.878433,-5.948012,-1.005233,-9.764343,-0.331788,9.938160,-2.749384,4.704448,5.200063,-6.275923,2.445980,-3.824500,7.698778,7.901587,1.087333,1.413302,5.614920,9.800723,2.284147,-4.174746,-7.553425,-6.634148,-5.613014,4.808599,-2.397136,-3.883677,-7.954206,4.663240,-1.608485,7.746242,-8.349901,0.736699,-8.794022,8.654138,8.014103,5.252821,8.226039,-7.765161,-1.232190,-3.688565,3.973739,-9.734879,1.467398,3.249867,7.330961,-0.146204,-7.603500,2.793741,-5.308646,-3.495670,-1.324231,-4.011317,8.792531,8.568178,-3.434406,6.940932,-8.952900,8.053407,2.408540,9.745427,9.613583,-6.141106,-9.248685,2.222290,5.049975,-6.927232,6.515103,5.819434,5.761505,-5.620850,-4.243655,6.229080,-0.799369,0.439526,0.578652,-8.136056,-9.406495,-6.870607,-8.516579,2.571008,0.364007,6.585559,-5.053253,-1.454247,-5.616669,-5.486675,-2.581977,6.109128,-5.519133,-1.178384,-5.184651,1.271355,-8.053074,0.779526,0.101444,-2.188346,-9.521981,2.734411,-0.401504,-9.966821,0.224814,-5.988431,-8.898855,-2.527430,-0.140695,-8.283509,0.587610,7.782549,-4.867464,-0.634465,4.361830,-4.482950,-1.679965,3.458864,0.601094,4.125557,-6.476601,-2.793992,-9.243100,6.769556,-2.391724,5.411652,7.176421,4.292048,7.536121,2.438905,-8.265313,-6.476836,-3.833245,5.092783,5.311237,-7.796774,-0.965714,-1.348451,6.180192,5.734667,8.638250,4.205246,0.735866,-8.311614,-8.378380,-1.801788,-6.364335,3.243226,-0.156338,-1.150537,-3.229588,0.159982,-0.901381,7.109163,0.390717,6.086830,8.721390,-7.364095,5.200674,9.854227,-6.545798,-5.084427,-5.061043,1.138979,-2.187288,-3.197635,-7.122082,-6.169992,9.317859,-0.873857,-6.079723,6.879384,-0.695339,1.274634,4.640149,7.004650,-1.483089,-3.622460,-4.719003,4.095749,7.731740,5.407364,3.620767,-0.839547,2.005929,7.043201,-7.472474,3.206765,-8.170287,-0.080198,8.001281,-5.829202,3.272241,-4.650993,-4.251978,0.540766,7.756162,-2.842244,-0.315511,8.626731,5.923794,5.632941,0.687337,4.420784,2.412865,3.849764,7.272493,-4.190076,-6.566255,-5.667613,-0.562935,1.524728,-0.384089,-7.624888,-6.568767,-4.826078,4.519096,-1.165787,-6.730680,-4.938297,9.273116,-6.631252,4.540151,-8.987087,5.990628,8.705811,-4.393980,5.479164,-3.725433,1.064325,8.643945,-7.894640,3.963122,-8.544117,-9.597415,-4.545748,-3.856502,8.507796,6.239796,-9.288539,-2.518791,6.417939,-3.446324,-4.208617,-2.400486,0.726123,4.524273,-2.332642,-1.051005,6.231213,-7.024696,5.564885,-8.344308,-4.209828,-9.201473,0.842401,-7.321340,0.020959,8.515633,6.136435,2.890045,-5.816046,1.018972,5.834127,8.115484,-8.378991,-2.782231,-1.412786,-8.471893,3.557022,7.684463,-4.376806,8.017003,-5.928654,1.695799,-1.199774,2.889056,7.576775,-0.276102,-1.292171,5.795522,0.116816,-6.619165,6.883742,-7.108175,5.228134,4.127111,-9.709719,5.402460,3.327972,-8.459873,1.317284,-9.393904,-6.738514,-2.074520,-8.921091,-7.713617,5.735739,-6.716179,4.431862,2.119996,-5.959850,-2.128037,8.198527,-4.128949,-6.377816,5.383554,-5.055792,3.515289,-3.129033,9.613906,9.965426,-6.676064,7.315046,1.667240,4.683563,6.160915,4.433320,-7.965132,-9.390267,-1.544536,-9.408504,-5.292812,9.393715,7.514034,0.793368,5.070096,-5.095214,-6.417065,-6.567387,6.626541,-7.748599,7.290897,-3.751750,1.393876,-8.815847,-1.653099,1.430827,5.066620,-5.926076,-7.629830,-2.106933,-7.654626,1.353035,-8.883532,3.364910,1.947402,-5.381241,0.421615,8.482221,3.805141,-7.282159,-6.118134,2.830157,9.959576,-7.392223,6.702089,2.136784,-6.347906,-0.082142,-6.426395,-1.687151,-3.242702,-8.745492,4.402680,-1.371818,-1.931351,-1.251563,-6.943211,-3.371721,3.932359,6.154507,7.498482,0.965809,9.908912,-4.808896,8.875345,8.639332,-8.216422,1.116663,6.673438,-8.731968,4.230606,-3.545046,-0.442410,4.237644,-9.701375,9.446864,2.159786,1.602624,-2.916469,-8.166942,-6.150946,6.883465,5.618458,-0.479598,-0.533623,-4.986185,-1.245363,3.195419,-9.395632,-1.489846,1.509591,-8.959548,-5.123329,4.074547,-0.157633,-1.875103,-9.676711,0.187885,8.268128,-2.533870,-8.853034,4.987951,-1.608776,-4.576705,6.886426,0.281055,-3.723193,4.313411,1.550696,7.006102,-9.235081,-0.745410,-4.007239,-8.559639,4.139182,3.085170,-9.040461,-7.433500,-0.660343,2.207858,-3.180734,-3.501404,-1.935916,1.372687,5.540219,3.209412,5.131809,-0.611582,6.334127,5.682127,2.453821,3.328153,9.280199,-6.300054,-6.267131,2.512051,-3.073058,7.765410,6.581290,-8.731824,1.136604,-1.059521,5.261157,-3.850612,7.129824,-1.902099,7.416665,-3.747026,8.093165,-0.725499,-8.078163,-6.979387,9.807033,-4.912612,5.143091,8.460535,-1.729870,2.696509,-7.451849,8.935307,0.391569,3.861939,1.695766,1.729277,-8.649885,-1.654979,5.327431,-8.663396,-0.585125], dtype = "float64")#candidate|15296|(2464,)|const|float64
const_15297 = relay.const([[-8,2,-4,9,5,-5,-5,8,-3,5,4,9,-9,8,10,2,8,5,-10,3,-6,-4,7,8,-4,8,-4,-1,-9,-4,5,-9,1,9,8,7,-4,-4,1,-9,-4,5,5,10,7,6,-1,-6,-7,-4,-9,-9,-1,4,-7,-9,1,9,-1,3,-5,1,4,-10,4,-5,4,8,9,9,4,-6,-3,-2,-6,-4,3,-6,-5,-7,-2,-4,8,-2,-3,-4,-9,1,-7,-6,-7,1,8,-5,8,1,-4,-6,8,-1,1,5,8,-1,8,-6,-10,3,8,10,-1,4,8,10,-10,-7,8,10,-10,9,-10,3,5,7,-5,9,-8,3,-5,-1,8,3,-2,2,-3,9,7,3,-7,5,-7,-10,-9,10,10,8,-9,-3,-5,-2,5,4,-3,-4,-7,-4,3,-9,9,-6,-1,6,-3,-3,-4,-7,-8,9,-7,-4,1,-1,4,-7,-9,1,-5,-2,-7,-9,9,10,-8,-9,-3,3,2,8,-6,-8,-10,-7,-7,-5,3,7,-1,-9,7,6,-2,-4,3,-10,-1,-3,7,-3,-8,-1,2,3,5,4,10,2,9,8,-9,10,-5,10,3,-6,-2,2,-5,9,6,1,-3,2,10,3,-6,-9,6,-3,-3,-1,-8,-2,7,2,-5,1,-8,10,-3,-7,-6,10,-8,-2,-1,-7]], dtype = "uint64")#candidate|15297|(1, 256)|const|uint64
call_15295 = relay.TupleGetItem(func_10577_call(relay.reshape(const_15296.astype('float64'), [11, 16, 14]), relay.reshape(const_15296.astype('float64'), [11, 16, 14]), relay.reshape(const_15297.astype('uint64'), [256,]), ), 3)
call_15298 = relay.TupleGetItem(func_10582_call(relay.reshape(const_15296.astype('float64'), [11, 16, 14]), relay.reshape(const_15296.astype('float64'), [11, 16, 14]), relay.reshape(const_15297.astype('uint64'), [256,]), ), 3)
bop_15299 = relay.bitwise_and(uop_15286.astype('uint64'), relay.reshape(call_15270.astype('uint64'), relay.shape_of(uop_15286))) # shape=(18, 110)
bop_15302 = relay.bitwise_and(uop_15286.astype('uint64'), relay.reshape(call_15272.astype('uint64'), relay.shape_of(uop_15286))) # shape=(18, 110)
uop_15307 = relay.sinh(bop_15299.astype('float64')) # shape=(18, 110)
uop_15309 = relay.sinh(bop_15302.astype('float64')) # shape=(18, 110)
uop_15323 = relay.asin(uop_15286.astype('float32')) # shape=(18, 110)
output = relay.Tuple([call_15263,call_15267,call_15277,call_15289,call_15295,const_15296,const_15297,uop_15307,uop_15323,])
output2 = relay.Tuple([call_15264,call_15268,call_15278,call_15290,call_15298,const_15296,const_15297,uop_15309,uop_15323,])
func_15331 = relay.Function([], output)
mod['func_15331'] = func_15331
mod = relay.transform.InferType()(mod)
mutated_mod['func_15331'] = func_15331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15331_call = mutated_mod.get_global_var('func_15331')
call_15332 = func_15331_call()
output = call_15332
func_15333 = relay.Function([], output)
mutated_mod['func_15333'] = func_15333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13260_call = mod.get_global_var('func_13260')
func_13262_call = mutated_mod.get_global_var('func_13262')
call_15345 = relay.TupleGetItem(func_13260_call(), 0)
call_15346 = relay.TupleGetItem(func_13262_call(), 0)
output = relay.Tuple([call_15345,])
output2 = relay.Tuple([call_15346,])
func_15355 = relay.Function([], output)
mod['func_15355'] = func_15355
mod = relay.transform.InferType()(mod)
output = func_15355()
func_15356 = relay.Function([], output)
mutated_mod['func_15356'] = func_15356
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11190_call = mod.get_global_var('func_11190')
func_11191_call = mutated_mod.get_global_var('func_11191')
call_15357 = relay.TupleGetItem(func_11190_call(), 0)
call_15358 = relay.TupleGetItem(func_11191_call(), 0)
output = relay.Tuple([call_15357,])
output2 = relay.Tuple([call_15358,])
func_15369 = relay.Function([], output)
mod['func_15369'] = func_15369
mod = relay.transform.InferType()(mod)
mutated_mod['func_15369'] = func_15369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15369_call = mutated_mod.get_global_var('func_15369')
call_15370 = func_15369_call()
output = call_15370
func_15371 = relay.Function([], output)
mutated_mod['func_15371'] = func_15371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15392 = relay.var("var_15392", dtype = "float64", shape = (3, 12, 2))#candidate|15392|(3, 12, 2)|var|float64
var_15393 = relay.var("var_15393", dtype = "float64", shape = (3, 12, 2))#candidate|15393|(3, 12, 2)|var|float64
bop_15394 = relay.floor_divide(var_15392.astype('float64'), relay.reshape(var_15393.astype('float64'), relay.shape_of(var_15392))) # shape=(3, 12, 2)
func_15331_call = mod.get_global_var('func_15331')
func_15333_call = mutated_mod.get_global_var('func_15333')
call_15407 = relay.TupleGetItem(func_15331_call(), 5)
call_15408 = relay.TupleGetItem(func_15333_call(), 5)
output = relay.Tuple([bop_15394,call_15407,])
output2 = relay.Tuple([bop_15394,call_15408,])
func_15417 = relay.Function([var_15392,var_15393,], output)
mod['func_15417'] = func_15417
mod = relay.transform.InferType()(mod)
mutated_mod['func_15417'] = func_15417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15417_call = mutated_mod.get_global_var('func_15417')
var_15419 = relay.var("var_15419", dtype = "float64", shape = (3, 12, 2))#candidate|15419|(3, 12, 2)|var|float64
var_15420 = relay.var("var_15420", dtype = "float64", shape = (3, 12, 2))#candidate|15420|(3, 12, 2)|var|float64
call_15418 = func_15417_call(var_15419,var_15420,)
output = call_15418
func_15421 = relay.Function([var_15419,var_15420,], output)
mutated_mod['func_15421'] = func_15421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15250_call = mod.get_global_var('func_15250')
func_15252_call = mutated_mod.get_global_var('func_15252')
call_15509 = func_15250_call()
call_15510 = func_15250_call()
func_10687_call = mod.get_global_var('func_10687')
func_10689_call = mutated_mod.get_global_var('func_10689')
call_15514 = relay.TupleGetItem(func_10687_call(), 0)
call_15515 = relay.TupleGetItem(func_10689_call(), 0)
output = relay.Tuple([call_15509,call_15514,])
output2 = relay.Tuple([call_15510,call_15515,])
func_15520 = relay.Function([], output)
mod['func_15520'] = func_15520
mod = relay.transform.InferType()(mod)
mutated_mod['func_15520'] = func_15520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15520_call = mutated_mod.get_global_var('func_15520')
call_15521 = func_15520_call()
output = call_15521
func_15522 = relay.Function([], output)
mutated_mod['func_15522'] = func_15522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8090_call = mod.get_global_var('func_8090')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_15573 = relay.TupleGetItem(func_8090_call(), 0)
call_15574 = relay.TupleGetItem(func_8091_call(), 0)
func_7115_call = mod.get_global_var('func_7115')
func_7117_call = mutated_mod.get_global_var('func_7117')
call_15586 = func_7115_call()
call_15587 = func_7115_call()
func_8930_call = mod.get_global_var('func_8930')
func_8932_call = mutated_mod.get_global_var('func_8932')
call_15598 = func_8930_call()
call_15599 = func_8930_call()
output = relay.Tuple([call_15573,call_15586,call_15598,])
output2 = relay.Tuple([call_15574,call_15587,call_15599,])
func_15612 = relay.Function([], output)
mod['func_15612'] = func_15612
mod = relay.transform.InferType()(mod)
mutated_mod['func_15612'] = func_15612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15612_call = mutated_mod.get_global_var('func_15612')
call_15613 = func_15612_call()
output = call_15613
func_15614 = relay.Function([], output)
mutated_mod['func_15614'] = func_15614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13745_call = mod.get_global_var('func_13745')
func_13746_call = mutated_mod.get_global_var('func_13746')
call_15615 = func_13745_call()
call_15616 = func_13745_call()
func_13491_call = mod.get_global_var('func_13491')
func_13493_call = mutated_mod.get_global_var('func_13493')
call_15617 = relay.TupleGetItem(func_13491_call(), 0)
call_15618 = relay.TupleGetItem(func_13493_call(), 0)
func_10047_call = mod.get_global_var('func_10047')
func_10048_call = mutated_mod.get_global_var('func_10048')
call_15629 = func_10047_call()
call_15630 = func_10047_call()
func_6309_call = mod.get_global_var('func_6309')
func_6318_call = mutated_mod.get_global_var('func_6318')
var_15632 = relay.var("var_15632", dtype = "uint32", shape = (2112,))#candidate|15632|(2112,)|var|uint32
var_15633 = relay.var("var_15633", dtype = "int32", shape = (21,))#candidate|15633|(21,)|var|int32
const_15634 = relay.const([[-4,-7],[-2,-6],[-8,3],[-7,-2],[-5,-3],[1,-5],[2,-1],[5,-9],[2,10],[3,-10],[10,-8],[-8,-1],[-1,-6],[-4,3],[-4,-1],[2,10],[8,-7],[7,-3],[-3,-5],[-3,-3],[-3,-7],[7,-2],[-4,4],[3,-9],[-5,3],[4,-8],[-6,9],[9,6],[-1,8],[-2,-1]], dtype = "uint64")#candidate|15634|(30, 2)|const|uint64
const_15635 = relay.const([[-7,-1,-4,-10,-3,-3,-2,-10,-7,9,-10,7,-3,-1,-2,2,-7,-6,-1,7,1,-4,6,-9,4,-3,10,6,-10,4],[3,9,8,-2,-2,-4,8,10,-1,9,9,-10,3,-4,-2,-4,4,-6,9,-3,4,7,-5,-7,6,-10,9,5,5,-6],[-10,3,-4,-10,6,5,3,3,9,-4,8,-1,5,9,-9,-6,-3,-7,-7,-9,2,-2,-4,-3,-7,-9,1,9,7,-6],[1,5,1,3,9,-1,-6,6,-8,-4,-3,7,2,-8,4,-5,-5,2,-2,-6,-7,-2,9,-4,6,-3,10,3,-8,10],[4,-10,6,9,-7,1,-1,8,10,9,9,-4,-4,10,7,-5,-5,-4,-6,-9,7,10,2,9,9,9,-2,8,2,-7],[10,-2,6,4,-6,-9,-2,10,-7,7,9,-6,10,8,-2,1,-8,4,6,7,4,4,3,1,6,-5,-5,5,-5,-7],[9,-6,8,10,2,7,-3,2,-6,-5,-1,7,-3,9,-7,-2,4,-1,10,6,9,7,-6,-8,-10,-7,5,-4,8,6],[-2,2,-8,8,-4,-1,-10,5,-5,-8,-7,-7,9,-3,-7,-2,7,4,-7,-7,-9,-6,-7,6,-5,9,1,4,-7,7],[-6,-2,-1,2,1,10,6,-10,6,-6,-10,3,-1,1,6,4,5,6,-4,-5,-6,6,9,-6,2,8,-7,3,-9,-5],[-10,-4,-7,-4,-9,-6,4,-6,8,9,-3,1,-9,-5,-7,-1,1,6,8,-9,-9,-1,-8,5,8,-5,-3,9,1,8],[6,6,7,-7,4,-1,4,-3,8,8,1,6,-10,-6,1,-10,5,8,10,10,-5,4,-2,2,4,-7,3,-1,-10,-5],[-2,10,3,-3,5,-4,4,-8,6,10,9,-8,-1,-9,-7,4,1,9,1,-6,5,7,-9,-8,4,-8,-5,7,-5,-9],[-1,2,-6,-6,2,5,4,-7,-6,10,4,3,2,7,4,-2,2,1,-2,7,10,1,4,5,-4,-10,-2,-10,-10,-4],[7,-3,9,-7,10,-4,7,-4,-3,3,-5,6,5,-4,4,-3,-3,8,-10,-2,10,-3,-3,-10,-8,-6,5,10,9,-4],[1,4,6,7,-8,8,-7,6,10,6,6,-10,-3,10,-2,5,-4,9,-2,5,5,9,-6,2,1,-3,10,-6,2,5],[10,1,-10,3,-7,5,2,4,10,-4,-1,-6,10,4,-9,10,-2,5,-1,5,7,-10,5,-4,7,6,5,-1,-7,9],[-7,-7,-7,-2,-1,6,8,-6,9,9,-10,-6,-8,-9,5,3,6,10,2,-2,8,2,4,-10,-8,9,-6,2,-3,9],[1,-9,-1,10,10,10,-2,5,-10,8,-3,-5,-3,3,2,-5,5,9,2,1,3,-9,4,10,-8,4,-9,-8,-8,10]], dtype = "int64")#candidate|15635|(18, 30)|const|int64
var_15636 = relay.var("var_15636", dtype = "float64", shape = (1280,))#candidate|15636|(1280,)|var|float64
var_15637 = relay.var("var_15637", dtype = "float64", shape = (1, 192))#candidate|15637|(1, 192)|var|float64
call_15631 = relay.TupleGetItem(func_6309_call(relay.reshape(var_15632.astype('uint32'), [12, 11, 16]), relay.reshape(var_15632.astype('uint32'), [12, 11, 16]), relay.reshape(var_15633.astype('int32'), [21,]), relay.reshape(const_15634.astype('uint64'), [60,]), relay.reshape(const_15635.astype('int64'), [540, 1]), relay.reshape(var_15636.astype('float64'), [320, 4]), relay.reshape(var_15637.astype('float64'), [192,]), ), 0)
call_15638 = relay.TupleGetItem(func_6318_call(relay.reshape(var_15632.astype('uint32'), [12, 11, 16]), relay.reshape(var_15632.astype('uint32'), [12, 11, 16]), relay.reshape(var_15633.astype('int32'), [21,]), relay.reshape(const_15634.astype('uint64'), [60,]), relay.reshape(const_15635.astype('int64'), [540, 1]), relay.reshape(var_15636.astype('float64'), [320, 4]), relay.reshape(var_15637.astype('float64'), [192,]), ), 0)
func_8502_call = mod.get_global_var('func_8502')
func_8506_call = mutated_mod.get_global_var('func_8506')
const_15644 = relay.const(2, dtype = "int64")#candidate|15644|()|const|int64
var_15645 = relay.var("var_15645", dtype = "float32", shape = (10, 28))#candidate|15645|(10, 28)|var|float32
call_15643 = relay.TupleGetItem(func_8502_call(relay.reshape(const_15634.astype('uint64'), [60,]), relay.reshape(const_15644.astype('int64'), []), relay.reshape(var_15645.astype('float32'), [140, 2]), ), 1)
call_15646 = relay.TupleGetItem(func_8506_call(relay.reshape(const_15634.astype('uint64'), [60,]), relay.reshape(const_15644.astype('int64'), []), relay.reshape(var_15645.astype('float32'), [140, 2]), ), 1)
output = relay.Tuple([call_15615,call_15617,call_15629,call_15631,var_15632,var_15633,const_15634,const_15635,var_15636,var_15637,call_15643,const_15644,var_15645,])
output2 = relay.Tuple([call_15616,call_15618,call_15630,call_15638,var_15632,var_15633,const_15634,const_15635,var_15636,var_15637,call_15646,const_15644,var_15645,])
func_15649 = relay.Function([var_15632,var_15633,var_15636,var_15637,var_15645,], output)
mod['func_15649'] = func_15649
mod = relay.transform.InferType()(mod)
var_15650 = relay.var("var_15650", dtype = "uint32", shape = (2112,))#candidate|15650|(2112,)|var|uint32
var_15651 = relay.var("var_15651", dtype = "int32", shape = (21,))#candidate|15651|(21,)|var|int32
var_15652 = relay.var("var_15652", dtype = "float64", shape = (1280,))#candidate|15652|(1280,)|var|float64
var_15653 = relay.var("var_15653", dtype = "float64", shape = (1, 192))#candidate|15653|(1, 192)|var|float64
var_15654 = relay.var("var_15654", dtype = "float32", shape = (10, 28))#candidate|15654|(10, 28)|var|float32
output = func_15649(var_15650,var_15651,var_15652,var_15653,var_15654,)
func_15655 = relay.Function([var_15650,var_15651,var_15652,var_15653,var_15654,], output)
mutated_mod['func_15655'] = func_15655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13312_call = mod.get_global_var('func_13312')
func_13314_call = mutated_mod.get_global_var('func_13314')
call_15717 = relay.TupleGetItem(func_13312_call(), 0)
call_15718 = relay.TupleGetItem(func_13314_call(), 0)
output = relay.Tuple([call_15717,])
output2 = relay.Tuple([call_15718,])
func_15725 = relay.Function([], output)
mod['func_15725'] = func_15725
mod = relay.transform.InferType()(mod)
mutated_mod['func_15725'] = func_15725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15725_call = mutated_mod.get_global_var('func_15725')
call_15726 = func_15725_call()
output = call_15726
func_15727 = relay.Function([], output)
mutated_mod['func_15727'] = func_15727
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15773 = relay.var("var_15773", dtype = "bool", shape = (7, 15, 12))#candidate|15773|(7, 15, 12)|var|bool
var_15774 = relay.var("var_15774", dtype = "bool", shape = (7, 15, 12))#candidate|15774|(7, 15, 12)|var|bool
bop_15775 = relay.logical_and(var_15773.astype('bool'), relay.reshape(var_15774.astype('bool'), relay.shape_of(var_15773))) # shape=(7, 15, 12)
func_8782_call = mod.get_global_var('func_8782')
func_8783_call = mutated_mod.get_global_var('func_8783')
call_15786 = relay.TupleGetItem(func_8782_call(), 0)
call_15787 = relay.TupleGetItem(func_8783_call(), 0)
output = relay.Tuple([bop_15775,call_15786,])
output2 = relay.Tuple([bop_15775,call_15787,])
func_15796 = relay.Function([var_15773,var_15774,], output)
mod['func_15796'] = func_15796
mod = relay.transform.InferType()(mod)
var_15797 = relay.var("var_15797", dtype = "bool", shape = (7, 15, 12))#candidate|15797|(7, 15, 12)|var|bool
var_15798 = relay.var("var_15798", dtype = "bool", shape = (7, 15, 12))#candidate|15798|(7, 15, 12)|var|bool
output = func_15796(var_15797,var_15798,)
func_15799 = relay.Function([var_15797,var_15798,], output)
mutated_mod['func_15799'] = func_15799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6751_call = mod.get_global_var('func_6751')
func_6753_call = mutated_mod.get_global_var('func_6753')
call_15801 = relay.TupleGetItem(func_6751_call(), 0)
call_15802 = relay.TupleGetItem(func_6753_call(), 0)
func_8244_call = mod.get_global_var('func_8244')
func_8246_call = mutated_mod.get_global_var('func_8246')
call_15807 = relay.TupleGetItem(func_8244_call(), 1)
call_15808 = relay.TupleGetItem(func_8246_call(), 1)
output = relay.Tuple([call_15801,call_15807,])
output2 = relay.Tuple([call_15802,call_15808,])
func_15824 = relay.Function([], output)
mod['func_15824'] = func_15824
mod = relay.transform.InferType()(mod)
output = func_15824()
func_15825 = relay.Function([], output)
mutated_mod['func_15825'] = func_15825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12960_call = mod.get_global_var('func_12960')
func_12962_call = mutated_mod.get_global_var('func_12962')
call_15829 = relay.TupleGetItem(func_12960_call(), 0)
call_15830 = relay.TupleGetItem(func_12962_call(), 0)
output = call_15829
output2 = call_15830
func_15838 = relay.Function([], output)
mod['func_15838'] = func_15838
mod = relay.transform.InferType()(mod)
output = func_15838()
func_15839 = relay.Function([], output)
mutated_mod['func_15839'] = func_15839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9713_call = mod.get_global_var('func_9713')
func_9715_call = mutated_mod.get_global_var('func_9715')
call_15876 = relay.TupleGetItem(func_9713_call(), 0)
call_15877 = relay.TupleGetItem(func_9715_call(), 0)
output = call_15876
output2 = call_15877
func_15878 = relay.Function([], output)
mod['func_15878'] = func_15878
mod = relay.transform.InferType()(mod)
output = func_15878()
func_15879 = relay.Function([], output)
mutated_mod['func_15879'] = func_15879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_15885 = relay.TupleGetItem(func_7523_call(), 0)
call_15886 = relay.TupleGetItem(func_7525_call(), 0)
func_938_call = mod.get_global_var('func_938')
func_940_call = mutated_mod.get_global_var('func_940')
const_15894 = relay.const([8.797226,-2.362803,-5.529562,-6.065571,-4.055489,9.831863,-5.317131,-5.354097,-2.033461,6.250310,-5.178442,-5.670061,3.001783,-7.789795,0.550304,-0.764541,1.892605,-9.982706,-5.462079,-8.601945,-3.697647,8.831650,-8.958802,-2.970988,-3.793874,7.156755,8.705339,-7.435627,-3.683363,2.789804,-0.963956,-7.489745,3.207835,-4.774324,-7.108197,-6.622431,-6.269394,2.292730,9.797674,2.777311,3.097954,-1.295787,-5.588067,-9.342644,4.634334,7.541189,8.122889,-5.697435,-5.654910,-7.887605,0.662297,9.067416,5.884796,-0.870810,-9.016610,-7.737680,5.125312,4.985811,6.202008,-9.547959], dtype = "float64")#candidate|15894|(60,)|const|float64
call_15893 = func_938_call(relay.reshape(const_15894.astype('float64'), [2, 3, 10]))
call_15895 = func_938_call(relay.reshape(const_15894.astype('float64'), [2, 3, 10]))
output = relay.Tuple([call_15885,call_15893,const_15894,])
output2 = relay.Tuple([call_15886,call_15895,const_15894,])
func_15897 = relay.Function([], output)
mod['func_15897'] = func_15897
mod = relay.transform.InferType()(mod)
output = func_15897()
func_15898 = relay.Function([], output)
mutated_mod['func_15898'] = func_15898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15119_call = mod.get_global_var('func_15119')
func_15121_call = mutated_mod.get_global_var('func_15121')
call_15917 = relay.TupleGetItem(func_15119_call(), 1)
call_15918 = relay.TupleGetItem(func_15121_call(), 1)
func_10515_call = mod.get_global_var('func_10515')
func_10517_call = mutated_mod.get_global_var('func_10517')
call_15941 = relay.TupleGetItem(func_10515_call(), 0)
call_15942 = relay.TupleGetItem(func_10517_call(), 0)
output = relay.Tuple([call_15917,call_15941,])
output2 = relay.Tuple([call_15918,call_15942,])
func_15943 = relay.Function([], output)
mod['func_15943'] = func_15943
mod = relay.transform.InferType()(mod)
output = func_15943()
func_15944 = relay.Function([], output)
mutated_mod['func_15944'] = func_15944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13697_call = mod.get_global_var('func_13697')
func_13698_call = mutated_mod.get_global_var('func_13698')
call_15984 = func_13697_call()
call_15985 = func_13697_call()
func_8502_call = mod.get_global_var('func_8502')
func_8506_call = mutated_mod.get_global_var('func_8506')
var_16010 = relay.var("var_16010", dtype = "uint64", shape = (60,))#candidate|16010|(60,)|var|uint64
const_16011 = relay.const(9, dtype = "int64")#candidate|16011|()|const|int64
var_16012 = relay.var("var_16012", dtype = "float32", shape = (280,))#candidate|16012|(280,)|var|float32
call_16009 = relay.TupleGetItem(func_8502_call(relay.reshape(var_16010.astype('uint64'), [60,]), relay.reshape(const_16011.astype('int64'), []), relay.reshape(var_16012.astype('float32'), [140, 2]), ), 9)
call_16013 = relay.TupleGetItem(func_8506_call(relay.reshape(var_16010.astype('uint64'), [60,]), relay.reshape(const_16011.astype('int64'), []), relay.reshape(var_16012.astype('float32'), [140, 2]), ), 9)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_16020 = func_7106_call()
call_16021 = func_7106_call()
func_9832_call = mod.get_global_var('func_9832')
func_9833_call = mutated_mod.get_global_var('func_9833')
call_16031 = relay.TupleGetItem(func_9832_call(), 0)
call_16032 = relay.TupleGetItem(func_9833_call(), 0)
output = relay.Tuple([call_15984,call_16009,var_16010,const_16011,var_16012,call_16020,call_16031,])
output2 = relay.Tuple([call_15985,call_16013,var_16010,const_16011,var_16012,call_16021,call_16032,])
func_16055 = relay.Function([var_16010,var_16012,], output)
mod['func_16055'] = func_16055
mod = relay.transform.InferType()(mod)
mutated_mod['func_16055'] = func_16055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16055_call = mutated_mod.get_global_var('func_16055')
var_16057 = relay.var("var_16057", dtype = "uint64", shape = (60,))#candidate|16057|(60,)|var|uint64
var_16058 = relay.var("var_16058", dtype = "float32", shape = (280,))#candidate|16058|(280,)|var|float32
call_16056 = func_16055_call(var_16057,var_16058,)
output = call_16056
func_16059 = relay.Function([var_16057,var_16058,], output)
mutated_mod['func_16059'] = func_16059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_16087 = func_11336_call()
call_16088 = func_11336_call()
output = relay.Tuple([call_16087,])
output2 = relay.Tuple([call_16088,])
func_16108 = relay.Function([], output)
mod['func_16108'] = func_16108
mod = relay.transform.InferType()(mod)
output = func_16108()
func_16109 = relay.Function([], output)
mutated_mod['func_16109'] = func_16109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12839_call = mod.get_global_var('func_12839')
func_12841_call = mutated_mod.get_global_var('func_12841')
call_16144 = relay.TupleGetItem(func_12839_call(), 0)
call_16145 = relay.TupleGetItem(func_12841_call(), 0)
uop_16150 = relay.atanh(call_16144.astype('float64')) # shape=(6, 16, 5)
uop_16152 = relay.atanh(call_16145.astype('float64')) # shape=(6, 16, 5)
output = uop_16150
output2 = uop_16152
func_16164 = relay.Function([], output)
mod['func_16164'] = func_16164
mod = relay.transform.InferType()(mod)
output = func_16164()
func_16165 = relay.Function([], output)
mutated_mod['func_16165'] = func_16165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8977_call = mod.get_global_var('func_8977')
func_8978_call = mutated_mod.get_global_var('func_8978')
call_16174 = relay.TupleGetItem(func_8977_call(), 0)
call_16175 = relay.TupleGetItem(func_8978_call(), 0)
func_7056_call = mod.get_global_var('func_7056')
func_7058_call = mutated_mod.get_global_var('func_7058')
call_16186 = relay.TupleGetItem(func_7056_call(relay.reshape(call_16174.astype('float64'), [3, 7, 7])), 1)
call_16187 = relay.TupleGetItem(func_7058_call(relay.reshape(call_16174.astype('float64'), [3, 7, 7])), 1)
func_12140_call = mod.get_global_var('func_12140')
func_12143_call = mutated_mod.get_global_var('func_12143')
var_16210 = relay.var("var_16210", dtype = "uint64", shape = (60,))#candidate|16210|(60,)|var|uint64
call_16209 = relay.TupleGetItem(func_12140_call(relay.reshape(var_16210.astype('uint64'), [60,])), 7)
call_16211 = relay.TupleGetItem(func_12143_call(relay.reshape(var_16210.astype('uint64'), [60,])), 7)
output = relay.Tuple([call_16174,call_16186,call_16209,var_16210,])
output2 = relay.Tuple([call_16175,call_16187,call_16211,var_16210,])
func_16216 = relay.Function([var_16210,], output)
mod['func_16216'] = func_16216
mod = relay.transform.InferType()(mod)
var_16217 = relay.var("var_16217", dtype = "uint64", shape = (60,))#candidate|16217|(60,)|var|uint64
output = func_16216(var_16217)
func_16218 = relay.Function([var_16217], output)
mutated_mod['func_16218'] = func_16218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_16257 = func_7731_call()
call_16258 = func_7731_call()
func_1145_call = mod.get_global_var('func_1145')
func_1149_call = mutated_mod.get_global_var('func_1149')
const_16290 = relay.const([3.926966,-2.117343,-8.412529,-3.404267,-5.366313,0.741011,-9.361449,-3.279794,3.201564,6.903790,3.537662,-3.837364,1.081729,1.898925,8.532448,-0.457033,5.579553,-4.163604,-4.373419,-1.538134,6.253255,4.560874,-3.773342,-9.406710,4.970956,0.441483,-5.667811,-3.549148,7.032729,-6.723855,-4.938784,5.870548,-8.595913,1.409385,-6.006257,8.303988,-3.317411,1.901699,-0.097008,-7.511896,-6.724002,-8.863906,-9.103462,-0.708765,3.515570,-5.886289,-0.002241,1.124473,0.481607,8.851099,-7.366204,4.141055,6.590328,1.882840,9.380968,6.530276,-0.947890,-0.972595,-0.379250,-6.988658,-1.064373,0.085587,-3.772680,4.707434,-1.037151,-7.019834,2.370640,1.974941,-7.116636,6.442855,-2.321409,0.686922,-3.820599,0.921084,0.444284,-9.011504,7.344837,-3.231567,8.187185,3.640093,-1.153065,-0.074424,-0.861119,-1.950375,8.818342,-2.253823,6.494781,-7.820121,1.558760,-7.128274,3.827127,-7.714060,4.116453,-6.614874,-9.374038,-2.746298,3.955637,4.409783,-2.070507,6.342581,7.977990,4.905093,2.162763,-8.683397,-7.785449,2.097338,-8.473701,-6.034792,-9.401765,-7.328608,-9.758673,1.707369,8.049910,5.703400,6.412466,7.078228,-7.231937,2.032269,-3.311143,5.574487,-4.969646,-5.546618,-5.502981,-1.675636,-9.337511,-6.250213,0.927333,-1.853694,-0.804144,-3.628696,-3.019859,-3.947819,8.112954,1.712498,8.570311,-6.523858,5.142797,-2.648392,5.064932,4.205506,9.217453,-7.311179,6.710449,-3.644522,1.963009,8.384415,-0.210211,-3.431643,1.534514,-5.201441,-5.351115,0.005647,0.697874,-2.080436,-4.607527,-9.213311,5.598743,7.670635,-9.070111,-5.347042,-4.613278,2.970143,1.643290,-2.428872,3.450149,0.170033,7.325983,-5.757456,2.530624,3.395305,-5.286538,4.343036,8.385797,-9.133653,-4.802837,3.230281,7.452097,-4.987102,-5.519451,2.997011,2.263958,-7.842830,4.075590,8.253036,4.040634,9.277403,6.172729,3.371633,6.318536,-1.598575,-5.895037,-8.945604,-3.780102,-6.922048,-9.271305,3.637421,-2.222057,-9.298887,-4.896075,-5.391442,4.274006,1.785748,8.138846,8.848772,-4.819986,-7.730644,9.497128,-0.822257,6.020368,-6.020958,6.040293,8.374164,8.017409,6.430342,-3.741093,3.420022,5.030053,-5.315460,7.217697,7.929616,1.317042,-5.932757,4.779091,-8.064768,8.628482,-6.633265,-8.725387,7.001012,7.611064,1.506776,-5.513519,5.733343,2.618860,-6.723133,9.555137,7.363583,-0.707363,4.360734,-2.739425,-4.386208,0.727424,-8.366514,7.401562,2.368632,9.217079,-1.437214,-1.185567,6.685686,6.173012,-4.818938,-2.500398,8.959695,-7.130832,-8.418579,-0.272019,-6.609347,9.456373,-4.069839,-8.994343,4.473230,-7.363078,-3.687089,-3.583243,0.375650,8.746508,-2.862828,7.291891,-9.970523,1.877467,-9.491738,-7.351460,7.212663,-2.848633,-2.655718,6.232600,-2.161634,1.341887,-8.879779,-7.748353,8.706923,-7.795528,3.817898,4.956203,7.909231,-0.370225,-0.763897,-9.692305,-2.781937,5.048529,-8.159661,0.754379,5.402567,5.864599,-7.325819,5.322422,3.289809,9.078731,3.811957,4.208400,9.704665,-5.688078,-5.756206,3.772021,8.014190,1.413107,-0.756983,-8.286122,3.599473,0.228441,-5.862885,5.418115,-2.666711,-5.641848,0.907552,-1.133823,-5.755076,-2.893054,-2.029928,9.734504,2.200195,2.621678,7.072472,5.559700,5.348597,-8.110676,9.398831,2.058475,5.633230,5.109194,5.161130,0.851545,-9.168985,-0.760518,-3.467068,5.806126,-0.830054,9.180462,-7.051341,-9.196239,3.707330,3.105357,-4.808201,9.710043,1.251731,-4.354893,-6.206631,-3.509699,-9.733569,3.288417,-4.712440,-3.549932,8.818561,8.688027,-6.639059,0.953696,-3.402344,-5.877111,-3.946395,-1.470730,-1.156245,-4.017498,8.145269,1.596480,-2.431837,-4.322283,3.423752,3.445489,-9.671172,0.209358,5.883886,-7.679065,6.573188,-6.392240,-1.153265,8.586921,-6.812975,-5.914349,-8.799110,0.761679,-9.782607,-7.169636,-0.073935,5.289227,-8.034346,6.366953,3.478237,0.107780,-6.381165,-5.978242,2.243639,2.939074,-6.847383,9.057563,9.648292,1.084246,-2.773873,-9.436689,5.458980,2.145168,-0.504157,2.771101,-9.206429,-1.204365,3.855294,-9.848651,2.287201,-7.761582,2.759645,-0.633609,-0.293317,-4.371900,0.367437,7.529941,-3.864465,-4.477307,1.558740,9.843989,0.097949,-4.034928,-6.879824,8.626394,-7.612750,9.160033,5.657731,-4.927996,4.677982,-2.475375,0.396775,-2.561580,-1.700622,-0.226258,-5.689336,3.161392,-1.112533,-9.752174,-9.499435,-3.164518,9.775100,-9.227976,1.479690,-1.502172,-0.290246,-8.865433,-6.310898,4.612469,3.104909,-1.809322,2.531175,0.643122,4.456577,0.430534,5.028809,-7.518351,2.174240,3.528829,-3.324139,-7.939760,-1.135629,-8.989306,2.328835,5.099771,-8.566495,-7.726615,-4.493046,1.448734,-8.793285,6.446262,-0.253302,-9.200921,7.419748,-7.370913,-8.232130,-9.816576,9.961635,4.831807,-3.952029,-1.064931,0.438340,7.273437,-1.323384,4.815303,4.512698,0.835249,3.120015,4.535384,0.178761,-8.065814,-0.478642,4.901011,8.638693,-6.891704,0.901641,-1.128778,-3.988473,-9.860315,-7.477912,9.581386,3.780234,3.056804,-6.547520,0.714433,5.201987,1.603390,-1.061629,9.030029,-2.826197,4.342680,-1.673909,-8.206749,3.015300,-4.968430,-9.221433,3.941875,-9.617525,-6.665473,-2.435399,-3.302329,9.570265,3.418561,-0.191676,-1.004724,1.433490,5.495862,6.198428,-8.449790,-6.997739,5.176736,-3.445750,-9.389085,3.995457,1.925913,-9.325669,1.180798,-5.206390,8.165720,-1.567622,4.553309,-6.215081,3.277274,-9.497014,-9.140609,-9.337308,9.573014,7.006417,3.774620,6.174116,-2.762406,7.498341,1.306894,-9.192240,-6.442936,-9.711048,-1.593166,-1.252956,7.597942,3.995177,-8.767896,2.925697,-3.940701,9.509690,8.819582,5.665125,9.812832,-9.887132,-9.560609,6.732783,9.589812,-7.600272,-8.833223,9.633054,9.921902,-6.068993,6.925920,1.043980,-8.197689,4.549798,6.888487,9.198237,1.133973,-3.785205,-8.763017,9.784278,5.462428,-1.980543,-3.642265,1.341923,-2.220326,5.553175,1.479815,-7.310885,-2.843282,-3.987091,-0.358406,-5.483577,7.743582,0.483256,-4.724418,5.321149,-7.310034,-7.355202,4.092038,-2.944267,1.156989,2.399369,-7.047520,-2.457895,-6.193801,8.862792,-6.170964,-5.239404,-4.193406,3.779133,-8.143038,-6.082382,-0.260934,-2.430311,7.409930,-8.642566,-0.003208,8.566612,7.715100,1.477728,-3.043967,-3.965732,-1.831420,-4.782473,-6.781944,-7.770554,-9.317612,4.260409,7.547910,0.816828,-9.742432,6.493977,1.698960,1.256694,-8.199403,-4.291705,4.691223,0.831227,-3.386704,-6.188890,1.641083,7.121522,-7.689351,9.351748,-5.182350,-3.334376,-8.872223,-1.015510,-9.799106,-0.032716,-2.849750,-8.251840,2.722369,-5.288632,4.843437,-5.940043,2.243837,1.482727,-0.480266,0.764145,7.402055,3.866241,1.668088,8.265989,2.642414,-7.732363,6.978612,-4.487603,-5.869623,-6.702753,4.530876,-3.870982,-7.963506,-2.325439,-5.190306,-0.202009,4.377171,2.011118,0.887427,0.878259,-9.103809,-3.542504,-3.110196,-3.519920,7.778887,-4.302093,7.856013,3.920166,-3.198062,-0.738849,8.223490,-7.534929,-1.797563,3.988134,2.623930,6.169759,-6.860076,8.327868,-1.218237,6.352556,-1.559989,-7.834225,6.814485,2.061533,-8.456144,-7.575312,-2.500943,-7.908153,3.633757,-3.373266,-0.572173,-0.552893,-8.320854,3.664151,-8.799780,-6.984487,0.489391,-3.769487,9.588387,-1.348708,-6.265704,1.794168,-1.066498,4.032750,-5.236063,-0.130838,6.045680,8.146079,-9.969360,-8.424590,-3.599068,0.570162,-9.997887,-9.872912,9.252684,3.482340,6.554149,2.935780,-6.997964,5.918834,-2.040889,-5.044741,1.066373,7.564482,-4.676308,-7.175674,8.284092,-4.532336,7.593074,8.490921,-1.946817,-2.013840,2.819735,2.500635,2.601739,-3.349704,-4.126855,4.646659,5.186832,2.233122,9.605974,-7.319325,0.846777,-4.813341,7.136348,0.583869,-3.984325,1.444612,9.311997,1.988331,-6.717064,1.676788,-3.238264,-1.996798,4.973471,-4.396312,7.467924,7.480549,8.834378,3.120141,2.203479,-1.607988,6.921727,-4.622119,-7.384568,1.060729,7.691299,5.266666,8.090339,8.550509,0.872316,0.596927,-1.796345,3.769895,-8.931625,-5.295498,-8.873363,9.103564,0.398560,-4.093249,-0.306463,-1.767291,-3.537102,5.613445,8.744560,5.163878,-6.338607,9.518413,9.304069,9.517811,4.013474,-5.792022,-8.862566,3.541507,3.256943,-8.611961,4.545960,5.162299,-2.107663,-0.789915,-7.229918,7.062329,-5.550654,4.775709,6.819509,-6.982778,5.798626,-5.852473,-4.990524,9.263891,-7.097723,7.695125,-5.638000,3.862492,-9.128978,-1.494754,5.761061,0.383865,-2.410435,-4.248149,4.837579,-4.956385,8.925312,3.106064,9.476216,2.247518,-7.821534,5.340613,2.401696,4.989860,-5.194052,-8.942988,9.575367,-7.514035,5.336117,-9.244323,8.521986,6.538645,6.595534,-6.196590,1.578737,-9.303418,5.779822,-8.695838,9.250690,-6.045669,5.606731,4.291260,-6.120540,-4.887461,-4.046586,4.617343,8.559749,-8.534600,6.729310,1.012382,-5.457896,-7.757052,-8.370677,5.040414,-7.619227,9.477956,-9.629945,5.854119,-9.652435,-4.542144,-1.638959,-2.913083,-1.821208,-4.688074,-4.711875,-6.265229,-5.176769,-7.386221,5.060433,-8.740312,3.523956,6.795583,-7.687419,-8.239843,-9.944680,-2.554686,-8.987169,8.238999,5.332586,-3.761273,4.123839,3.700043,4.445345,-2.205406,7.414778,9.804487,3.089612,-1.757165,6.893222,-5.154963,-4.283868,-6.414881,-1.931023,8.205026,9.774965,7.133066,0.410607,-7.287640,-7.518619,4.053467,2.063751,-5.517584,-5.564263,4.082622,1.248674,1.965552,-5.902846,2.565275,8.415359,-4.099457,-5.635929,-7.345604,-5.175833,9.860222,2.675949,-6.899796,7.866188,7.218398,-5.057580,2.629252,0.189159,4.214766,-8.119013,-3.296985,9.083989,-6.713262,-1.292804,5.611251,-2.782838,3.417387,-4.624635,-5.832253,-4.829915,3.734200,-2.453971,-7.376672,1.220898,2.644037,-3.193795,-0.497769,6.313231,-1.650769,3.016460,-4.449098,-1.197136,0.710416,-7.955136,-9.008400,-4.329113,1.862342,-2.560510,-0.011164,6.490399,2.931239,6.862450,4.657408,-8.615050,-2.481034,-9.615582,6.483850,-3.857360,5.474961,5.352290,7.283385,1.873469,-4.070502,-6.135731,4.487942,3.550648,-7.415036,-2.075140,9.147027,0.878009,-1.259775,-6.317786,-6.390711,8.674002,7.837502,4.516155,-2.705360,2.699095,-3.701545,4.162280,2.238555,-4.125181,7.923321,-0.879684,1.101526,-5.609580,4.543507,-1.930696,6.893192,9.185508,-1.993651,1.441033,7.356301,9.704962,-8.897724,4.989274,4.353454,0.124085,5.330350,4.448421,9.091152,-2.480945,1.773514,-2.147780,-7.170417,9.520943,-3.639632,0.079976,-3.392205,0.168996,7.552279,-8.813106,-8.107019,9.971063,6.067566,1.451813,-1.072764,6.554189,-9.288664,-9.437126,4.502202,2.848659,-0.939804,7.402618,3.526084,-2.821353,-1.251973,-6.697846,-0.736574,-1.846800,-2.067425,2.426716,3.652543,-8.526820,-6.789704,4.097012,0.190512,-3.267556,6.830005,-2.088994,-0.943539,-9.794782,6.202129,-6.101320,-0.418499,-7.460828,-1.271895,-7.075733,-2.413297,0.282659,6.476339,2.610079,9.531766,9.314612,0.610031,0.063049,-9.588640,-7.883145,-7.056169,6.916349,2.047454,-5.307551,4.455719,-1.313582,6.702289,5.932999,-7.971283,5.829363,-4.791109,-3.475327,-9.989422,8.144444,2.192502,4.829194,-4.082006,7.415734,-3.039683,0.792536,-4.274512,7.272580,4.383184,-0.860734,5.891515,8.748732,-0.356747,-2.026372,-9.459370,9.939243,6.775477,1.901062,-7.589613,-9.853447,-6.267708,-7.806765,7.354328,9.309775,-1.951268,-4.858810,7.595089,1.860309,8.540338,8.360878,-4.445036,-3.684230,5.950174,0.042390,-8.499863,-2.861068,-0.393047,9.165479,-8.382734,-3.509341,-9.560936,0.795277,0.545012,-4.734407,-7.273986,-9.518752,-7.934451,-4.682922,-6.829692,2.082072,3.476894,-6.730941,9.964022,7.934223,-1.384692,-3.712144,-7.759677,-0.734781,6.869546,8.883089,-8.449605,-4.423718,-6.359841,-7.743483,-4.536109,8.808788,9.731229,7.900315,0.107599,6.328261,9.121326,-4.718699,3.822109,2.921184,2.215621,-9.628758,-2.934571,4.050713,5.272353,4.475738,0.962656,-3.830615,-7.431914,0.288152,-1.416250,9.485724,6.622074,-7.243481,3.203687,2.761598,-2.301082,-4.117217,-8.730975,2.876045,-6.925566,5.245491,9.657566,-0.509398,-7.723135,9.810884,-5.456883,-3.736457,-3.890664,-8.949255,-5.600668,7.865180,0.888102,8.237819,0.381301,-6.494885,6.286767,6.096460,1.886201,4.165657,-5.756735,-5.916788,0.592341,-0.126454,0.509714,2.456067,-9.026253,-4.140922,0.870102,9.817547,-0.758221,-5.788821,5.002672,-7.655801,6.099838,-9.888519,-0.268635,2.010529,3.685713,-2.514361,-2.337020,-7.841499,-0.355821,9.056139,-8.164127,-0.898943,-7.911900,4.868190,-3.104088,-5.972028,5.903847,2.567005,6.258701,4.601164,-4.997717,-9.502375,-3.321679,5.076251,2.895032,-8.115145,4.105775,4.784698,4.998621,-9.649267,-7.219558,4.205442,9.718663,-7.194413,3.546702,-5.443628,9.576658,4.120160,7.393633,-8.513738,1.750806,1.612889,1.157792,-1.558663,9.039237,-8.242516,4.481788,6.129579,2.124576], dtype = "float64")#candidate|16290|(1280,)|const|float64
const_16291 = relay.const([-10,2,7,5,-3,-8,5,-8,-3,-2,-10,2,-6,-3,-10,7,-9,7,-1,5,9,8,-5,-4,-7,7,7,7,-2,10,-7,1,-4,-4,-3,8,-2,8,3,6,-10,1,-4,3,-9,5,-8,3,-7,6,8,1,-2,-7,-1,-7,8,10,-8,-6], dtype = "uint64")#candidate|16291|(60,)|const|uint64
call_16289 = relay.TupleGetItem(func_1145_call(relay.reshape(const_16290.astype('float64'), [16, 16, 5]), relay.reshape(const_16291.astype('uint64'), [60,]), ), 3)
call_16292 = relay.TupleGetItem(func_1149_call(relay.reshape(const_16290.astype('float64'), [16, 16, 5]), relay.reshape(const_16291.astype('uint64'), [60,]), ), 3)
output = relay.Tuple([call_16257,call_16289,const_16290,const_16291,])
output2 = relay.Tuple([call_16258,call_16292,const_16290,const_16291,])
func_16295 = relay.Function([], output)
mod['func_16295'] = func_16295
mod = relay.transform.InferType()(mod)
mutated_mod['func_16295'] = func_16295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16295_call = mutated_mod.get_global_var('func_16295')
call_16296 = func_16295_call()
output = call_16296
func_16297 = relay.Function([], output)
mutated_mod['func_16297'] = func_16297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_16315 = func_7106_call()
call_16316 = func_7106_call()
output = relay.Tuple([call_16315,])
output2 = relay.Tuple([call_16316,])
func_16322 = relay.Function([], output)
mod['func_16322'] = func_16322
mod = relay.transform.InferType()(mod)
output = func_16322()
func_16323 = relay.Function([], output)
mutated_mod['func_16323'] = func_16323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mod.get_global_var('func_8349')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_16324 = func_8349_call()
call_16325 = func_8349_call()
func_14105_call = mod.get_global_var('func_14105')
func_14106_call = mutated_mod.get_global_var('func_14106')
call_16338 = relay.TupleGetItem(func_14105_call(), 1)
call_16339 = relay.TupleGetItem(func_14106_call(), 1)
output = relay.Tuple([call_16324,call_16338,])
output2 = relay.Tuple([call_16325,call_16339,])
func_16353 = relay.Function([], output)
mod['func_16353'] = func_16353
mod = relay.transform.InferType()(mod)
mutated_mod['func_16353'] = func_16353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16353_call = mutated_mod.get_global_var('func_16353')
call_16354 = func_16353_call()
output = call_16354
func_16355 = relay.Function([], output)
mutated_mod['func_16355'] = func_16355
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16381 = relay.var("var_16381", dtype = "float32", shape = (9, 6, 2))#candidate|16381|(9, 6, 2)|var|float32
var_16382 = relay.var("var_16382", dtype = "float32", shape = (9, 6, 2))#candidate|16382|(9, 6, 2)|var|float32
bop_16383 = relay.floor_divide(var_16381.astype('float32'), relay.reshape(var_16382.astype('float32'), relay.shape_of(var_16381))) # shape=(9, 6, 2)
func_7216_call = mod.get_global_var('func_7216')
func_7218_call = mutated_mod.get_global_var('func_7218')
call_16416 = func_7216_call()
call_16417 = func_7216_call()
output = relay.Tuple([bop_16383,call_16416,])
output2 = relay.Tuple([bop_16383,call_16417,])
func_16425 = relay.Function([var_16381,var_16382,], output)
mod['func_16425'] = func_16425
mod = relay.transform.InferType()(mod)
mutated_mod['func_16425'] = func_16425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16425_call = mutated_mod.get_global_var('func_16425')
var_16427 = relay.var("var_16427", dtype = "float32", shape = (9, 6, 2))#candidate|16427|(9, 6, 2)|var|float32
var_16428 = relay.var("var_16428", dtype = "float32", shape = (9, 6, 2))#candidate|16428|(9, 6, 2)|var|float32
call_16426 = func_16425_call(var_16427,var_16428,)
output = call_16426
func_16429 = relay.Function([var_16427,var_16428,], output)
mutated_mod['func_16429'] = func_16429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9380_call = mod.get_global_var('func_9380')
func_9382_call = mutated_mod.get_global_var('func_9382')
call_16464 = func_9380_call()
call_16465 = func_9380_call()
output = call_16464
output2 = call_16465
func_16466 = relay.Function([], output)
mod['func_16466'] = func_16466
mod = relay.transform.InferType()(mod)
mutated_mod['func_16466'] = func_16466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16466_call = mutated_mod.get_global_var('func_16466')
call_16467 = func_16466_call()
output = call_16467
func_16468 = relay.Function([], output)
mutated_mod['func_16468'] = func_16468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13697_call = mod.get_global_var('func_13697')
func_13698_call = mutated_mod.get_global_var('func_13698')
call_16478 = func_13697_call()
call_16479 = func_13697_call()
output = relay.Tuple([call_16478,])
output2 = relay.Tuple([call_16479,])
func_16526 = relay.Function([], output)
mod['func_16526'] = func_16526
mod = relay.transform.InferType()(mod)
output = func_16526()
func_16527 = relay.Function([], output)
mutated_mod['func_16527'] = func_16527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8090_call = mod.get_global_var('func_8090')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_16553 = relay.TupleGetItem(func_8090_call(), 0)
call_16554 = relay.TupleGetItem(func_8091_call(), 0)
output = call_16553
output2 = call_16554
func_16555 = relay.Function([], output)
mod['func_16555'] = func_16555
mod = relay.transform.InferType()(mod)
mutated_mod['func_16555'] = func_16555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16555_call = mutated_mod.get_global_var('func_16555')
call_16556 = func_16555_call()
output = call_16556
func_16557 = relay.Function([], output)
mutated_mod['func_16557'] = func_16557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9665_call = mod.get_global_var('func_9665')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_16574 = relay.TupleGetItem(func_9665_call(), 0)
call_16575 = relay.TupleGetItem(func_9666_call(), 0)
func_11566_call = mod.get_global_var('func_11566')
func_11570_call = mutated_mod.get_global_var('func_11570')
const_16622 = relay.const([[7,-10,-7,6,6,1,4,2,-9,-3,-10,-9,10,-8]], dtype = "uint8")#candidate|16622|(1, 14)|const|uint8
const_16623 = relay.const([-5,-2,-3,-7,4,-7,-5,4,-8,6,8,-6,2,-4,-10,-6,9,1,-6,1,4,-5,-10,6,6,7,7,10,1,4,4,6,10,5,8,6,-5,-8,-3,-1,8,2,5,-7,-5,8,2,3,1,-8,8,-10,-6,-6,-5,-6], dtype = "uint8")#candidate|16623|(56,)|const|uint8
call_16621 = relay.TupleGetItem(func_11566_call(relay.reshape(const_16622.astype('uint8'), [1, 1, 14]), relay.reshape(const_16623.astype('uint8'), [4, 1, 14]), ), 0)
call_16624 = relay.TupleGetItem(func_11570_call(relay.reshape(const_16622.astype('uint8'), [1, 1, 14]), relay.reshape(const_16623.astype('uint8'), [4, 1, 14]), ), 0)
func_9182_call = mod.get_global_var('func_9182')
func_9185_call = mutated_mod.get_global_var('func_9185')
const_16636 = relay.const([True,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,False,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,False,False,False,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,False], dtype = "bool")#candidate|16636|(1008,)|const|bool
var_16637 = relay.var("var_16637", dtype = "uint64", shape = (256, 1))#candidate|16637|(256, 1)|var|uint64
call_16635 = relay.TupleGetItem(func_9182_call(relay.reshape(const_16636.astype('bool'), [1008,]), relay.reshape(var_16637.astype('uint64'), [256,]), ), 5)
call_16638 = relay.TupleGetItem(func_9185_call(relay.reshape(const_16636.astype('bool'), [1008,]), relay.reshape(var_16637.astype('uint64'), [256,]), ), 5)
output = relay.Tuple([call_16574,call_16621,const_16622,const_16623,call_16635,const_16636,var_16637,])
output2 = relay.Tuple([call_16575,call_16624,const_16622,const_16623,call_16638,const_16636,var_16637,])
func_16642 = relay.Function([var_16637,], output)
mod['func_16642'] = func_16642
mod = relay.transform.InferType()(mod)
var_16643 = relay.var("var_16643", dtype = "uint64", shape = (256, 1))#candidate|16643|(256, 1)|var|uint64
output = func_16642(var_16643)
func_16644 = relay.Function([var_16643], output)
mutated_mod['func_16644'] = func_16644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7653_call = mod.get_global_var('func_7653')
func_7654_call = mutated_mod.get_global_var('func_7654')
call_16646 = relay.TupleGetItem(func_7653_call(), 0)
call_16647 = relay.TupleGetItem(func_7654_call(), 0)
func_10259_call = mod.get_global_var('func_10259')
func_10262_call = mutated_mod.get_global_var('func_10262')
const_16655 = relay.const([[1.421201],[0.356532],[8.611194],[-7.050462],[5.986323],[3.546998],[-8.588597],[4.842341],[0.323308],[7.557090],[0.012069],[8.913504],[8.631638],[-6.112135],[7.721270],[-8.750077],[-9.537725],[6.790220],[8.371588],[-6.774041],[-8.149978],[5.012937],[-6.747387],[6.259601],[-8.100860],[-1.191230],[-6.723325],[0.538700],[3.699629],[4.873069],[-1.248841],[5.387765],[7.554553],[4.487784],[2.406885],[1.817886],[0.720971],[-3.868300],[2.091407],[-3.251621],[7.016090],[-2.045857],[-0.082861],[8.746035],[6.142814],[-3.346743],[3.690681],[4.958273],[-3.601580],[9.641950],[-2.832481],[-0.482420],[6.799717],[7.532161],[-0.418252],[6.604908],[-4.530770],[4.161495],[7.574530],[-5.424086],[-4.797467],[-0.062593],[6.687315],[-9.053843],[-5.830796]], dtype = "float64")#candidate|16655|(65, 1)|const|float64
const_16656 = relay.const([9.542489,-0.248465,2.804780,-6.130346,-2.475730,-4.252474,1.892313,4.961832,4.772558,-5.478775,2.616001,9.154431,0.821892,8.919462,-8.162443,-0.113463,0.126098,-5.335641,5.104827,8.086958,2.414688,-8.294636,1.447061,0.577465,6.078058,4.621059,2.039580,-1.788587,-4.919613,2.104115,-1.295955,-0.656830,-7.120189,8.257678,2.320367,-5.174162,-0.557083,4.816111,-0.808765,-8.922899,-5.994387,-6.836424,-7.491527,3.811179,-4.277455,7.654178,-2.723575,-5.891140,-2.755192,3.318677,0.405754,7.069297,-8.412306,4.600699,0.046064,-7.701336,5.804287,9.813698,8.318503,2.680914,6.066482,2.131395,-5.913975,-9.312927,9.752516,2.228110,8.899700,-5.442096,9.442721,-3.073698,-7.185204,7.888629,7.169024,6.897374,6.555234,-0.032051,-8.081413,-6.765868,-9.464592,6.495165,-1.189941,-0.599050,2.527638,6.740977,-5.239628,4.959683,-4.900785,0.246897,7.565159,2.905641,9.567855,1.016964,0.858801,-5.245351,5.573366,1.885404,-6.449535,5.928574,-6.857432,5.672715,1.170375,5.149475,0.651506,2.472809,-9.759416,3.118176,4.561159,7.524185,-5.178444,-0.435957,3.462436,-7.941305,6.607737,-7.021565,-0.533201,-9.798109,-1.508863,-9.643368,-5.176546,4.277308,-6.609583,-8.163674,0.825110,-5.408813,-2.507966,4.217085,-4.530524,3.278844,-9.965600,1.081693,8.931405,-5.215772,-7.298547,9.263205,-1.489336,0.183207,6.288857,-3.051238,1.907624,3.294253,2.399960,8.675358,-7.008446,8.290764,-2.592404,7.751470,0.927198,-6.370483,-3.039917,-3.986158,-9.976533,5.561995,-5.804860,-2.042667,-7.441539,5.828796,7.980719,6.976692,6.616961,-3.373624,-1.276852,-5.157415,3.718760,4.116902,-1.460926,-3.556448,3.312172,0.377607,-3.437433,0.807460,8.921912,-1.248995,2.230526,-2.856160,8.393335,1.963392,-3.685325,6.651674,-4.841375,-7.542596,-7.664337,8.663588,-6.703201,7.539677,-0.555501,-7.636641,5.209691,-7.636943,-0.485752,-3.576670,9.111112,5.498914,6.477415,6.440561,2.977596,-1.299158,7.871750,0.086487,-1.146840,-0.461786,9.918787,-3.633655,8.830883,-5.688873,8.504780,3.953271,-2.070262,6.140411,7.640431,6.245102,-6.922144,8.832459,1.034812,2.723024,1.777097,-1.669223,-4.280892,-6.651536,-5.296545,-2.874863,1.512362,-1.621637,-6.027383,9.157006,8.728159,0.543077,-3.892945,8.291715,7.245128,-4.211162,-5.228156,-7.813589,2.999865,-7.607071,4.964858,-4.363927,4.186736,-7.733547,-8.174402,5.571169,-4.155048,8.689317,8.136363,-3.477379,8.178999,-0.630733,3.312516,2.739614,8.788684,-8.821536,-4.521069,6.648367,-2.027341,4.219585,5.444366,-4.481240,1.985587,-6.218093,-9.480563,-8.319315,0.698572,5.948192,6.211145,-5.062277,-4.198789,9.731540,7.112375,-3.256023,-9.580760,-0.357657,0.100552,5.307102,-9.886302,0.513919,-1.169123,-2.415055,-5.432714,-7.616155,-2.298992,-5.701156,-9.702920,9.866401,-1.753421,3.109743,-3.029666,-7.856123,-9.739126,-9.134196,-9.691499,8.525873,4.227455,-4.809624,1.425720,5.578333,6.404788,-6.425400,3.061954,7.492584,-2.158880,-6.257823,-9.960013,-8.814885,-0.809033,8.202829,-0.741841,9.444876,2.694386,-0.797514,6.196263,-6.519156,6.127047,-1.274165,6.393096,9.884603,-4.276322,-4.143694,-4.259609,4.429114,6.883370,8.047897,9.115815,-8.189022,1.693327,2.565382,-8.194539,7.985872,-8.528204,5.806991,-8.806035,3.280904,-5.795783,8.293257,-6.907150,-7.810830,-2.432181,-7.868283,-5.291091,-8.465748,6.528621,-8.542170,8.039550,0.510591,7.305262,0.294620,4.078503,-5.662425,-1.896582,8.291081,-1.285681,4.484571,5.392455,-4.378488,-1.112902,1.210489,-2.048889,3.928593,-3.754343,-1.773905,9.425351,2.250122,-2.066802,5.634670,2.997215,-8.225023,-4.378125,-4.759066,9.548745,1.952811,7.352794,5.333199,8.970461,-7.721032,9.566064,9.371685,-8.595763,-4.193608,4.877191,-6.273132,-8.805657,-9.088265,-1.406418,-5.701357,-4.501941,3.076328,3.579324,3.823737,3.914514,-9.478466,-0.666139,-2.756324,-0.904318,-3.689114,-8.818203,-5.497691,2.681933,3.087112,-1.010254,1.764428,6.826672,-2.854372,8.024905,9.012099,2.156077,9.597688,-4.058647,0.835889,-3.873718,-3.435419,-9.060597,0.699433,2.373273,9.721059,7.439627,-4.431164,3.579401,1.901420,2.986649,5.309428,-2.452752,-6.884924,-6.412016,0.242926,0.561938,6.172408,-4.081269,7.933073,9.970798,4.600758,0.105820,-4.148285,9.380101,2.003021,-1.886255,0.333809,-0.143687,9.968103,9.983824,7.366724,-8.270454,-6.255424,-1.727091,8.669833,-0.345641,-0.675578,-1.312871,-5.944526,-1.277648,-3.146657,3.171340,5.739632,-9.122988,-0.023935,2.276995,-6.729957,7.288414,-9.078545,1.605534,4.083191,6.995656,7.559801,-8.938724,5.361056,-6.053437,-5.302875,8.272807,5.097912,-9.975775,-8.718660,2.689959,-1.803842,8.975399,-7.230288,-5.111049,0.136370,8.291313,6.853666,-6.516334,-5.046402,2.802649,-8.227711,-1.335091,-2.220020,-6.652421,-7.344363,2.301357,-5.303927,-1.842993,2.044552,-5.909969,-2.545143,-6.993553,-0.624642,-4.668626,9.591729,5.459334,-2.244585,6.781065,-2.892807,2.001080,4.492481,5.669208,-0.544735,9.067384,-9.335791,-4.689293,4.328422,2.673993,4.068141,8.221110,8.244043,1.670870,-5.613917,-8.898683,-1.513763,-0.547123,-7.398704,0.420473,5.070326,8.971960,-8.479385,-4.623272,-0.709383,7.411284,7.411854,-9.297430,1.229018,-1.903831,-3.328036,5.560601,0.894276,-1.197629,2.998065,-5.912336,-6.320788,7.101356,5.560033,7.263058,8.522128,6.861045,7.299163,1.370842,9.198543,-7.148616,-4.285208,-4.610617,5.085089,3.141930,-4.208499,2.325204,9.131991,-1.725222,-1.086136,-6.652022,-4.357678,-8.181539,7.439089,4.736655,-1.907402,-0.818506,1.465630,-1.264755,-6.418049,6.490117,7.717397,7.532440,2.392825,5.889383,2.941656,5.489793,6.464116,4.440514,8.600017,-8.366985,7.601165,-3.944961,3.761256,1.307765,9.955008,2.110259,-0.713924,9.276086,-1.955477,8.792323,8.910265,9.535979,2.915858,3.509857,6.055586,-6.635751,5.988242,9.114331,3.548389,-0.560201,-1.384038,3.779406,-6.821624,-2.271262,3.092349,9.640472,2.058937,6.069113,5.445348,4.740444,-8.190405,7.267305,1.866191,2.056844,-1.938151,6.590117,4.120409,6.617738,6.275492,-8.378040,8.304068,7.689738,-0.215477,2.617319,-6.642968,4.557283,-4.078182,-7.627715,2.314820,-0.083488,3.822745,-8.036867,-3.108642,-6.904128,-1.539867,-5.289015,-8.069748,-0.357769,5.353424,8.666034,-2.708470,-4.369043,6.605368,-0.953634,-0.005309,-6.210576,-7.984304,-7.262115,-2.094624,4.616000,9.542234,9.719053,2.782677,0.382029,3.122776,-3.530400,6.525438,3.892929,2.785413,0.358841,-5.169559,5.689944,5.165787,-6.717237,7.521847,-6.251826,3.972036,-9.020881,3.286442,0.659537,-3.362659,-2.673821,6.290006,8.312207,-5.699480,-2.993092,-7.613783,6.199171,-3.113683,-1.134333,0.944345,-3.833334,-6.803437,-8.945396,-1.592283,-3.798179,7.184772,-7.044490,-2.776347,-6.786953,5.518137,-6.161909,-2.016716,4.109141,2.106647,-5.405156,-6.050550,2.846334,-0.834291,-0.786799,-5.115434,4.825143,5.871639,-8.098601,6.765810,-7.021420,2.154886,1.882991,5.273821,-1.792432,-5.698678,5.180856,-5.250426,9.393766,-5.204112,5.167532,-9.899453,8.346395,5.740818,-2.489399,-8.711623,6.671047,3.748785,3.155108,1.178620,3.351013,8.029104,-6.549647,5.712533,-7.622439,2.236831,-2.292607,-5.378678,8.683582,8.724422,2.754924,4.996862,-5.919484,6.700027,7.024561,8.894833,-8.081970,2.504910,-8.844664,-5.972004,2.096028,4.300385,8.316176,9.035015,4.209264,-7.855553,-1.294866,4.272112,-3.727594,-1.750530,2.379531,-0.333822,-5.397325,-6.189287,5.090435,0.546252,-4.701852,-3.607983,0.437413,-9.677810,5.751172,5.333757,-9.740764,-9.285236,9.415208,-7.220913,-4.654070,-7.216219,7.496384,-8.830064,1.818392,8.145519,-0.349652,3.365567,7.976959,-8.810030,2.290670,-6.043839,-4.564820,-2.550152,5.971240,-7.017029,-3.780912,9.267008,7.739415,-5.214593,2.929101,-0.186231,5.168402,0.207854,8.128219,3.534174,7.627710,6.768556,-3.908543,5.856198,-0.644888,-7.585476,-6.397764,-7.141235,7.894789,-5.227656,-6.542388,-4.901225,7.447121,-5.312067,1.304866,6.148764,5.683408,-3.873958,-9.519230,-3.381423,1.721114,0.098458,-1.192895,1.817790,-4.609468,-2.833819,-9.056790,0.473424,0.742565,-8.121198,9.325113,1.983252,-4.288585,5.091020,-4.099253,-4.501643,-1.784575,9.064410,6.631070,-5.666607,1.118789,6.497287,8.419528,3.100765,-9.440073,1.750935,3.884921,4.836187,-9.855716,-9.651803,-2.450500,-7.552671,1.901122,8.287639,-7.890694,-3.077087,-0.067908,3.401265,-3.826325,-8.166812,-3.847682,2.888605,7.647110,-0.997615,5.093755,-6.263631,5.108744,-3.402662,-5.574118,6.765602,0.614655,-5.686540,4.581681,1.213022,-4.328968,3.387385,2.111913,-0.135431,5.887694,-0.781000,-0.348654,-3.519690,0.587365,-3.213473,-6.161934,-0.047492,4.779787,9.695659,-3.271439,9.415125,1.456176,1.132695,5.236441,9.978006,-3.675710,5.985072,-3.080680,-0.573463,-9.969282,2.908931,8.440176,-8.581581,4.698011,8.151631,-8.634201,-7.245893,2.422392,-9.214848,-3.763563,7.542848,9.681289,9.549083,-9.255365,3.595291,-9.972192,0.344118,-7.639037,-9.742851,-1.502711,1.298680,-7.022524,-1.305793,2.936240,-4.817391,-6.406544,9.556065,-4.064133,5.685861,-1.524360,6.478862,0.846035,-6.114517,-2.206654,6.488227,5.103936,0.705439,3.357527,8.823635,-3.748522,-6.342751,-5.320529,-9.310498,-8.134772,4.353428,-1.761165,9.010698,-2.602665,6.884654,-0.316860,5.132871,6.486894,-2.180338,-6.132316,-2.059521,2.119440,0.765199,-0.236892,1.868718,1.394239,9.634064,8.611009,6.777720,9.051947,6.783046,-0.390617,9.183624,8.367335,-5.342156,2.508635,6.359873,0.413587,-6.708876,-5.699526,-2.125759,7.098396,-9.767251,-8.950553,-4.832307,-5.903362,1.770724,-3.555121,1.044474,-3.197656,7.124429,-5.521180,5.330380,4.415908,7.049902,0.292514,1.572882,9.982539,1.603568,0.539132,2.992912,0.564297,-2.729132,4.417871,-9.683738,5.277541,-3.879161,-9.653222,5.970179,0.847817,7.879579,-8.169144,2.663172,-7.463148,3.380485,-3.817351,-2.232273,-9.250058,8.118346,-3.006348,0.823931,4.379482,1.615817,9.812053,5.179077,0.352579,6.079149,4.747417,7.037255,-8.697323,-7.823306,-0.845092,-7.099412,8.069169,-8.349334,9.319043,-5.953449,7.140375,-9.654776,-8.574158,-8.572852,5.829957,-5.831884,-1.096258,-7.458695,-4.583695,-8.650997,2.367927,9.919234,-0.418675,-7.411476,-3.673146,2.087173,-8.827274,-4.107720,7.085703,-5.720419,3.145829,-7.954469,9.407729,-8.052990,0.889100,-4.648963,9.794571,1.011379,6.014638,-2.838892,-2.978367,-4.967311,3.231044,-9.092930,2.304383,7.222352,8.824929,-7.935090,5.909307,-1.992653,0.345097,9.058265,4.637667,4.795387,5.613503,-6.813008,3.003762,-5.822536,9.737292,4.695378,-2.366925,3.899270,-6.522066,-2.449934,-6.920713,-3.415800,4.022017,5.879790,7.829239,7.386978,-3.104706,-7.672127,-1.460875,-9.853069,2.565501,-2.084477,1.962535,0.131221,-4.740478,8.067497,5.855262,-6.688415,7.461780,5.380513,-7.044450,9.816840,-4.030825,-1.157056,5.896257,-5.918223,1.918343,-3.452725,7.048714,-1.698942,7.393227,-9.080413,-1.554146,3.168325,-0.448768,-6.926040,5.339365,7.810219,8.108835,4.944727,5.892520,-0.131837,-0.083480,2.955692,-5.775938,4.658115,2.828492,-6.680689,6.179072,3.195408,-4.244405,-1.323037,-7.844755,0.925322,-5.053209,-0.793047,0.574136,-7.527255,6.871544,0.682065,3.711764,4.854462,-4.351552,-0.998311,5.695061,-8.511559,8.649666,8.101051,-0.175440,-8.341355,0.310764,-5.442533,0.335958,5.637938,-7.050105,-9.407749,1.199240,-3.971751,-4.667919,4.221983,9.821672,4.857485,0.791545,-0.373726,-4.466775,-2.554682,6.614361,-7.295581,7.518387,1.217248,-5.333405,5.943170,6.618210,9.398150,2.378662,6.882510,-6.901642,6.680320,1.411833,-9.153658,-5.040088,-9.265078,0.493170,-9.733133,-6.378877,7.593283,-1.143855,-7.290545,-6.790886,9.853339,9.537624,-0.347499,2.827054,0.706070,6.931905,-0.017700,-4.466771,8.994875,5.776233,-4.734194,2.223974,-0.504431,-8.241373,5.853492,6.513813,-4.208501,9.662831,-1.773131,3.406131,-2.964707,3.470863,-3.973932,8.250101,-3.921999,-3.124280,-3.918165,-3.612831,4.858161,4.928692,3.128070,7.337339,7.523847,6.522491,4.226477,4.683784,4.794492,0.784907,-6.148795,-2.002856,0.482269,9.517491,-9.196914,0.157676,3.520973,9.187314,1.683305,-1.481157,9.929791,-5.481643,-0.842771,-3.244838,6.860142,-1.174535,-1.012536,-6.525668,7.796031,0.223699,6.251925,6.215573,-6.005234,7.314261,8.250285,-9.515926,2.268412,9.801830,8.666658,-9.586640,2.279223,-5.705759,2.594104,-4.048286,0.476998,-7.124383,-0.207771,4.142416,-1.765090,-3.253883,-6.390257,3.031706,0.319111,-0.712521,-2.835966,7.099626,4.250212,-3.060768,-0.278579,8.526006,-8.129240,-2.676098,4.317179,5.822620,1.180225,0.159810,7.144481,3.888417,5.683367], dtype = "float64")#candidate|16656|(1280,)|const|float64
call_16654 = relay.TupleGetItem(func_10259_call(relay.reshape(const_16655.astype('float64'), [65,]), relay.reshape(const_16656.astype('float64'), [1280,]), ), 8)
call_16657 = relay.TupleGetItem(func_10262_call(relay.reshape(const_16655.astype('float64'), [65,]), relay.reshape(const_16656.astype('float64'), [1280,]), ), 8)
output = relay.Tuple([call_16646,call_16654,const_16655,const_16656,])
output2 = relay.Tuple([call_16647,call_16657,const_16655,const_16656,])
func_16664 = relay.Function([], output)
mod['func_16664'] = func_16664
mod = relay.transform.InferType()(mod)
output = func_16664()
func_16665 = relay.Function([], output)
mutated_mod['func_16665'] = func_16665
mutated_mod = relay.transform.InferType()(mutated_mod)
const_16669 = relay.const([[[-6.007241,-3.811839,-3.822496,-3.741678,-8.820906,5.755095,-4.302996,-4.128562,-6.692505,2.308563,-9.168984,6.393633],[-7.503850,4.178928,-8.411356,6.275038,8.996281,0.105176,7.762377,3.853413,1.051648,-8.827831,-4.180511,4.977937]],[[7.579731,-8.756487,-2.610879,2.563700,-6.714571,5.741867,8.154822,2.041608,7.994340,-8.267298,-3.881571,-8.435052],[6.051648,-3.484881,6.080181,-8.247834,-1.101698,-0.881923,-7.180597,-8.685752,-8.889305,7.769646,-9.513292,-9.164460]],[[8.665022,-0.973364,-3.292834,7.601733,1.237764,-1.533575,7.078134,1.920604,8.118122,-1.930599,2.329583,-6.043949],[6.976767,4.151119,-5.375022,9.850757,1.367513,-5.333093,-2.560598,4.716418,4.182423,-8.993531,-5.839818,-1.905661]],[[-7.401413,2.882184,0.140990,6.316833,1.236570,-4.986155,7.740767,8.936101,8.673240,-4.027509,8.855096,2.607837],[3.582165,6.477518,7.630147,-4.726379,-9.595885,6.488146,6.409819,-2.373225,-6.944496,8.440215,-6.648415,-4.448670]],[[-1.579723,8.302315,-6.740397,-1.822361,7.178291,6.139733,9.854626,-8.584924,7.915715,-8.777595,-7.472527,9.300971],[0.769697,-9.968133,6.591834,-2.465060,-7.324922,6.103338,-3.006890,-2.225129,0.280918,1.419556,9.483888,-7.078326]]], dtype = "float64")#candidate|16669|(5, 2, 12)|const|float64
uop_16670 = relay.sinh(const_16669.astype('float64')) # shape=(5, 2, 12)
var_16674 = relay.var("var_16674", dtype = "float64", shape = (5, 2, 12))#candidate|16674|(5, 2, 12)|var|float64
bop_16675 = relay.power(const_16669.astype('float64'), relay.reshape(var_16674.astype('float64'), relay.shape_of(const_16669))) # shape=(5, 2, 12)
func_12204_call = mod.get_global_var('func_12204')
func_12206_call = mutated_mod.get_global_var('func_12206')
const_16683 = relay.const([False,False,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True], dtype = "bool")#candidate|16683|(560,)|const|bool
call_16682 = func_12204_call(relay.reshape(const_16683.astype('bool'), [10, 7, 8]))
call_16684 = func_12204_call(relay.reshape(const_16683.astype('bool'), [10, 7, 8]))
func_14879_call = mod.get_global_var('func_14879')
func_14881_call = mutated_mod.get_global_var('func_14881')
call_16690 = relay.TupleGetItem(func_14879_call(), 1)
call_16691 = relay.TupleGetItem(func_14881_call(), 1)
func_6804_call = mod.get_global_var('func_6804')
func_6806_call = mutated_mod.get_global_var('func_6806')
var_16698 = relay.var("var_16698", dtype = "int64", shape = ())#candidate|16698|()|var|int64
call_16697 = relay.TupleGetItem(func_6804_call(relay.reshape(var_16698.astype('int64'), [])), 2)
call_16699 = relay.TupleGetItem(func_6806_call(relay.reshape(var_16698.astype('int64'), [])), 2)
func_15796_call = mod.get_global_var('func_15796')
func_15799_call = mutated_mod.get_global_var('func_15799')
var_16707 = relay.var("var_16707", dtype = "bool", shape = (1260,))#candidate|16707|(1260,)|var|bool
call_16706 = relay.TupleGetItem(func_15796_call(relay.reshape(var_16707.astype('bool'), [7, 15, 12]), relay.reshape(var_16707.astype('bool'), [7, 15, 12]), ), 1)
call_16708 = relay.TupleGetItem(func_15799_call(relay.reshape(var_16707.astype('bool'), [7, 15, 12]), relay.reshape(var_16707.astype('bool'), [7, 15, 12]), ), 1)
output = relay.Tuple([uop_16670,bop_16675,call_16682,const_16683,call_16690,call_16697,var_16698,call_16706,var_16707,])
output2 = relay.Tuple([uop_16670,bop_16675,call_16684,const_16683,call_16691,call_16699,var_16698,call_16708,var_16707,])
func_16709 = relay.Function([var_16674,var_16698,var_16707,], output)
mod['func_16709'] = func_16709
mod = relay.transform.InferType()(mod)
var_16710 = relay.var("var_16710", dtype = "float64", shape = (5, 2, 12))#candidate|16710|(5, 2, 12)|var|float64
var_16711 = relay.var("var_16711", dtype = "int64", shape = ())#candidate|16711|()|var|int64
var_16712 = relay.var("var_16712", dtype = "bool", shape = (1260,))#candidate|16712|(1260,)|var|bool
output = func_16709(var_16710,var_16711,var_16712,)
func_16713 = relay.Function([var_16710,var_16711,var_16712,], output)
mutated_mod['func_16713'] = func_16713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9320_call = mod.get_global_var('func_9320')
func_9321_call = mutated_mod.get_global_var('func_9321')
call_16715 = relay.TupleGetItem(func_9320_call(), 0)
call_16716 = relay.TupleGetItem(func_9321_call(), 0)
output = call_16715
output2 = call_16716
func_16729 = relay.Function([], output)
mod['func_16729'] = func_16729
mod = relay.transform.InferType()(mod)
output = func_16729()
func_16730 = relay.Function([], output)
mutated_mod['func_16730'] = func_16730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9713_call = mod.get_global_var('func_9713')
func_9715_call = mutated_mod.get_global_var('func_9715')
call_16734 = relay.TupleGetItem(func_9713_call(), 0)
call_16735 = relay.TupleGetItem(func_9715_call(), 0)
output = call_16734
output2 = call_16735
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
func_8930_call = mod.get_global_var('func_8930')
func_8932_call = mutated_mod.get_global_var('func_8932')
call_16756 = func_8930_call()
call_16757 = func_8930_call()
func_8349_call = mod.get_global_var('func_8349')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_16765 = func_8349_call()
call_16766 = func_8349_call()
output = relay.Tuple([call_16756,call_16765,])
output2 = relay.Tuple([call_16757,call_16766,])
func_16771 = relay.Function([], output)
mod['func_16771'] = func_16771
mod = relay.transform.InferType()(mod)
output = func_16771()
func_16772 = relay.Function([], output)
mutated_mod['func_16772'] = func_16772
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16931 = relay.var("var_16931", dtype = "float64", shape = (4, 6, 1))#candidate|16931|(4, 6, 1)|var|float64
uop_16932 = relay.tan(var_16931.astype('float64')) # shape=(4, 6, 1)
bop_16944 = relay.greater_equal(uop_16932.astype('bool'), relay.reshape(var_16931.astype('bool'), relay.shape_of(uop_16932))) # shape=(4, 6, 1)
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_16948 = func_8696_call()
call_16949 = func_8696_call()
output = relay.Tuple([bop_16944,call_16948,])
output2 = relay.Tuple([bop_16944,call_16949,])
func_16951 = relay.Function([var_16931,], output)
mod['func_16951'] = func_16951
mod = relay.transform.InferType()(mod)
mutated_mod['func_16951'] = func_16951
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16952 = relay.var("var_16952", dtype = "float64", shape = (4, 6, 1))#candidate|16952|(4, 6, 1)|var|float64
func_16951_call = mutated_mod.get_global_var('func_16951')
call_16953 = func_16951_call(var_16952)
output = call_16953
func_16954 = relay.Function([var_16952], output)
mutated_mod['func_16954'] = func_16954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13214_call = mod.get_global_var('func_13214')
func_13216_call = mutated_mod.get_global_var('func_13216')
call_16976 = relay.TupleGetItem(func_13214_call(), 0)
call_16977 = relay.TupleGetItem(func_13216_call(), 0)
output = call_16976
output2 = call_16977
func_16988 = relay.Function([], output)
mod['func_16988'] = func_16988
mod = relay.transform.InferType()(mod)
output = func_16988()
func_16989 = relay.Function([], output)
mutated_mod['func_16989'] = func_16989
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17007 = relay.var("var_17007", dtype = "float32", shape = (8, 4, 15))#candidate|17007|(8, 4, 15)|var|float32
var_17008 = relay.var("var_17008", dtype = "float32", shape = (8, 4, 15))#candidate|17008|(8, 4, 15)|var|float32
bop_17009 = relay.power(var_17007.astype('float32'), relay.reshape(var_17008.astype('float32'), relay.shape_of(var_17007))) # shape=(8, 4, 15)
func_4568_call = mod.get_global_var('func_4568')
func_4575_call = mutated_mod.get_global_var('func_4575')
const_17019 = relay.const(3, dtype = "int32")#candidate|17019|()|const|int32
const_17020 = relay.const([[1,-5,3,-10,3,-1,1,4,-4,-9,-7,10,-8,4,10,-10,10,-8,1,3,-3]], dtype = "int32")#candidate|17020|(1, 21)|const|int32
var_17021 = relay.var("var_17021", dtype = "uint64", shape = (60,))#candidate|17021|(60,)|var|uint64
var_17022 = relay.var("var_17022", dtype = "int64", shape = (540,))#candidate|17022|(540,)|var|int64
var_17023 = relay.var("var_17023", dtype = "float64", shape = (1280,))#candidate|17023|(1280,)|var|float64
const_17024 = relay.const([[8.167365,5.391946],[-2.640475,-4.269591],[-6.031412,4.975812],[4.925379,-3.619332],[-9.896987,0.990570],[-4.622526,2.727421],[-3.290249,-9.732804],[-5.447790,9.962747],[-0.487038,-9.640112],[-1.745368,-9.675030],[6.417354,0.697880],[9.194446,3.975070],[-0.612756,-8.716779],[-9.215099,2.289582],[-7.194024,3.370543],[5.762659,-0.812997],[0.083386,-7.928260],[8.663598,9.531959],[-4.422151,2.312698],[-3.473225,9.023574],[-5.758125,0.455076],[4.864808,2.273558],[-7.467515,7.156258],[-0.911939,2.593326],[-2.381736,8.846563],[-2.784975,-5.629053],[5.712930,7.227144],[8.836101,-3.917403],[-4.324577,-0.766129],[-9.321651,2.348525],[3.051978,-6.926032],[-7.757597,9.982633],[7.995138,0.426264],[9.317125,-1.500997],[5.777448,4.168385],[-6.614193,-2.903638],[9.516973,4.212779],[7.809703,6.849351],[5.147623,-5.279175],[2.968547,-7.578960],[-5.791947,2.357986],[-1.555717,-8.719456],[7.170350,-2.889460],[1.299564,-5.155150],[2.198374,2.459653],[-8.387782,7.385718],[-7.056534,7.627178],[-9.366508,2.274997],[8.168512,-1.290898],[-7.009391,-6.822970],[-6.683279,-2.628282],[6.837671,8.082461],[-4.020927,2.621907],[2.173534,-6.376118],[-6.864694,8.148491],[1.462416,9.118478],[8.083694,-7.107636],[-1.574787,5.811782],[6.797161,9.207184],[-4.479194,-0.439607],[2.015115,8.401193],[-6.490333,-7.152870],[-1.928932,7.128281],[-4.899091,-4.596755],[0.925193,-4.836490],[1.976369,-6.140859],[8.524414,-3.552987],[-8.480385,-1.127586],[-7.407678,-3.006241],[6.893659,-3.685838],[1.065580,8.531068],[-1.643420,2.293323],[0.433299,-6.653504],[-4.327420,1.775608],[-5.629874,2.669819],[-0.562443,-1.572460],[-9.242359,-2.980340],[7.498581,7.988173],[-1.281503,8.371207],[-5.961267,-5.299441],[-8.622870,2.567580],[-8.665908,-7.828301],[-4.050787,0.066915],[1.567716,0.765337],[5.852690,6.243822],[-9.971217,3.971406],[7.674003,-4.013511],[6.222668,8.878559],[8.894742,-7.974408],[-9.146130,-5.119756],[8.895783,9.083212],[4.987328,-6.801280],[-1.071148,1.648976],[-5.472018,-3.840247],[9.406907,4.473328],[3.022276,-0.773938]], dtype = "float64")#candidate|17024|(96, 2)|const|float64
call_17018 = relay.TupleGetItem(func_4568_call(relay.reshape(const_17019.astype('int32'), []), relay.reshape(const_17020.astype('int32'), [7, 3, 1]), relay.reshape(var_17021.astype('uint64'), [60,]), relay.reshape(var_17022.astype('int64'), [540,]), relay.reshape(var_17023.astype('float64'), [1280,]), relay.reshape(const_17024.astype('float64'), [4, 48]), ), 7)
call_17025 = relay.TupleGetItem(func_4575_call(relay.reshape(const_17019.astype('int32'), []), relay.reshape(const_17020.astype('int32'), [7, 3, 1]), relay.reshape(var_17021.astype('uint64'), [60,]), relay.reshape(var_17022.astype('int64'), [540,]), relay.reshape(var_17023.astype('float64'), [1280,]), relay.reshape(const_17024.astype('float64'), [4, 48]), ), 7)
func_5673_call = mod.get_global_var('func_5673')
func_5678_call = mutated_mod.get_global_var('func_5678')
var_17028 = relay.var("var_17028", dtype = "float64", shape = (160,))#candidate|17028|(160,)|var|float64
call_17027 = relay.TupleGetItem(func_5673_call(relay.reshape(var_17028.astype('float64'), [5, 2, 16]), relay.reshape(const_17019.astype('int64'), []), relay.reshape(var_17023.astype('float64'), [1280,]), relay.reshape(var_17021.astype('uint64'), [30, 2]), ), 4)
call_17029 = relay.TupleGetItem(func_5678_call(relay.reshape(var_17028.astype('float64'), [5, 2, 16]), relay.reshape(const_17019.astype('int64'), []), relay.reshape(var_17023.astype('float64'), [1280,]), relay.reshape(var_17021.astype('uint64'), [30, 2]), ), 4)
func_9933_call = mod.get_global_var('func_9933')
func_9935_call = mutated_mod.get_global_var('func_9935')
call_17031 = relay.TupleGetItem(func_9933_call(), 0)
call_17032 = relay.TupleGetItem(func_9935_call(), 0)
output = relay.Tuple([bop_17009,call_17018,const_17019,const_17020,var_17021,var_17022,var_17023,const_17024,call_17027,var_17028,call_17031,])
output2 = relay.Tuple([bop_17009,call_17025,const_17019,const_17020,var_17021,var_17022,var_17023,const_17024,call_17029,var_17028,call_17032,])
func_17038 = relay.Function([var_17007,var_17008,var_17021,var_17022,var_17023,var_17028,], output)
mod['func_17038'] = func_17038
mod = relay.transform.InferType()(mod)
mutated_mod['func_17038'] = func_17038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17038_call = mutated_mod.get_global_var('func_17038')
var_17040 = relay.var("var_17040", dtype = "float32", shape = (8, 4, 15))#candidate|17040|(8, 4, 15)|var|float32
var_17041 = relay.var("var_17041", dtype = "float32", shape = (8, 4, 15))#candidate|17041|(8, 4, 15)|var|float32
var_17042 = relay.var("var_17042", dtype = "uint64", shape = (60,))#candidate|17042|(60,)|var|uint64
var_17043 = relay.var("var_17043", dtype = "int64", shape = (540,))#candidate|17043|(540,)|var|int64
var_17044 = relay.var("var_17044", dtype = "float64", shape = (1280,))#candidate|17044|(1280,)|var|float64
var_17045 = relay.var("var_17045", dtype = "float64", shape = (160,))#candidate|17045|(160,)|var|float64
call_17039 = func_17038_call(var_17040,var_17041,var_17042,var_17043,var_17044,var_17045,)
output = call_17039
func_17046 = relay.Function([var_17040,var_17041,var_17042,var_17043,var_17044,var_17045,], output)
mutated_mod['func_17046'] = func_17046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15331_call = mod.get_global_var('func_15331')
func_15333_call = mutated_mod.get_global_var('func_15333')
call_17055 = relay.TupleGetItem(func_15331_call(), 4)
call_17056 = relay.TupleGetItem(func_15333_call(), 4)
func_9665_call = mod.get_global_var('func_9665')
func_9666_call = mutated_mod.get_global_var('func_9666')
call_17066 = relay.TupleGetItem(func_9665_call(), 0)
call_17067 = relay.TupleGetItem(func_9666_call(), 0)
func_16555_call = mod.get_global_var('func_16555')
func_16557_call = mutated_mod.get_global_var('func_16557')
call_17070 = func_16555_call()
call_17071 = func_16555_call()
output = relay.Tuple([call_17055,call_17066,call_17070,])
output2 = relay.Tuple([call_17056,call_17067,call_17071,])
func_17072 = relay.Function([], output)
mod['func_17072'] = func_17072
mod = relay.transform.InferType()(mod)
output = func_17072()
func_17073 = relay.Function([], output)
mutated_mod['func_17073'] = func_17073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_17087 = relay.TupleGetItem(func_8021_call(), 0)
call_17088 = relay.TupleGetItem(func_8022_call(), 0)
func_14326_call = mod.get_global_var('func_14326')
func_14328_call = mutated_mod.get_global_var('func_14328')
const_17098 = relay.const([3.335254,1.354522,-0.520816,1.780300,-2.280868,-6.901038,4.670348,-7.850683,-8.126497,-4.686148,-1.417614,-1.134536,-3.116460,-5.676374,3.112708,7.886929,3.864081,9.848317,-0.568448,-8.829440,8.881377,-9.081956,8.209937,0.993924,4.222969,-8.098521,9.340965,-8.309463,3.378414,3.592568,-2.378970,1.281835,5.102336,8.509832,-2.111086,9.851240,4.560301,-0.168078,-7.008898,-8.270104,3.111588,2.329592,-8.213322,-6.361781,-5.488622,-2.901431,-4.569412,9.023537,-6.993802,3.052099,-5.591462,8.417592,-7.960940,-3.684251,3.595921,-3.815325,8.863738,1.051352,1.236119,-4.378740,7.814564,9.776475,-3.228361,-3.200705,6.003689,9.270232,-0.190252,7.245764,-4.390325,0.780792,8.945002,-7.014781,2.662367,-2.248846,2.894186,-2.972483,3.914909,3.147377,-8.395618,-4.720150,3.150055,8.197399,-8.612928,0.362724,-0.435368,5.852540,-7.084732,2.081990,7.014836,3.019255,-9.890788,-4.484211,8.410581,4.177786,7.410673,4.758709,-9.491720,-1.691587,-6.819335,7.911658,-3.506423,-8.332464,6.810875,-4.072127,6.101948,2.084411,3.755589,5.315538,6.931854,9.381693,-6.889074,-8.246556,2.959070,-3.980702,-9.910321,5.676116,-7.155847,6.956239,1.278211,-5.275391,5.676234,-8.383107,0.942089,3.142097,-4.192286,3.757653,-6.528321,8.409040,-4.833875,8.178017,-8.026855,6.261522,-0.199511,-9.907551,-2.542652,-1.516851,-1.300096,9.663492,-6.733807,8.813463,8.865906,7.150869,-0.595376,8.999944,-2.513110,8.384647,3.876919,4.320172,2.697755,2.947094,6.272469,-2.574655,-5.581953,3.748073,-6.409943,-3.764953,-9.542396,6.271375,-4.787581,2.575042,9.975966,2.461748,-0.069119,-2.998877,-9.215086,9.764083,8.365103,-6.883899,5.112044,-3.075812,-8.020549,9.388445,7.903952,8.366970,-6.857436,-2.562047,0.061526,-4.528435,9.279923,7.067530,0.079632,5.751970,-3.872302,-9.045830,9.077093,-1.168206,0.254382,-9.127941,-1.214210,4.698524,1.397481,7.066356,4.181837,-4.774761,-5.792139,6.553444,-2.431269,3.308043,-6.005045,9.351159,-6.282051,9.421412,3.935346,-7.189645,6.480698,-7.084826,-4.912701,6.360921,-4.351914,-9.490642,6.450766,-2.126334,-3.295350,9.315031,8.004997,-1.362032,-5.932422,-6.887824,-3.805011,4.802611,-7.350669,-4.735157,4.653243,-0.728808,8.854251,3.269402,-2.755298,-2.943629,8.778651,2.664867,-9.160381,-6.281112,5.034011,4.198646,-6.133035,2.332339,-8.151608,5.094552,4.420111,7.341651,-5.663974,-0.091051,-4.386272,0.756946,-4.501337,1.893286,-4.852732,8.801435,-4.892780,8.603305,3.232154,0.152664,-7.927750,-5.101493,-7.146343,-0.491564,-9.311645,-0.813666,-7.861695,-9.591510,-5.513040,8.798363,6.047778,3.676068,3.622581,-3.944584,9.870779,6.988419,-2.510469,-2.492897,0.752624,3.721712,1.521719,3.048938,8.396330,-9.888013,3.401238,0.663198,-6.310378,-4.027500,7.426488,-1.843018,-6.330550,4.472100,3.356248,9.199725,-6.322787,-8.183723,-8.670088,9.613184,6.928703,-0.183863,-4.679902,-4.485460,-2.853183,-2.937730,3.746356,-8.601472,-7.918765,0.191557,0.057086,4.801861,6.326223,5.338717,2.350763,-7.349742,-6.499141,3.482072,-2.379291,6.801622,-3.206916,-5.814957,3.629857,7.669922,-1.165460,4.371345,9.490877,-9.959758,8.941904,7.501880,-9.082639,3.958931,-3.293081,1.445962,-4.596804,7.207616,6.372026,5.848397,-6.359747,-7.693268,7.886045,0.359140,-4.872024,5.838258,1.280228,-5.502587,-3.533746,3.709131,-0.225672,3.999369,8.470775,5.162360,1.607271,1.768933,9.860677,-2.316978,-0.510649,-0.072172,0.619408,-5.487228,-4.985410,1.249949,-9.246986,7.393493,6.609403,-3.829958,0.330941,6.183753,-0.410591,-4.994912,0.204059,-2.386332,-8.752263,-1.127161,-8.912479,3.418637,-4.694153,-8.318442,2.283668,0.934642,-5.974075,1.566059,-3.601517,-9.058286,-1.163828,-9.586019,-0.244404,0.059730,5.459642,-3.943956,-2.360447,-4.033862,-6.845712,3.346143,-1.758358,0.964912,-8.496597,-8.701612,3.392838,1.539804,-0.102484,5.728305,-6.337369,2.821657,3.587398,-9.450471,1.229531,-6.245999,1.824800,7.452880,-1.544074,-0.707522,-0.388198,8.835747,-8.795223,3.394775,4.532513,1.695177,3.482916,7.440733,-2.311930,-2.245256,3.804327,-5.426378,-3.763659,-0.044791,-3.076768,-5.494730,-5.310970,-3.552176,-9.989893,7.873953,3.680783,-2.133474,1.555054,8.637997,4.483300,-0.861590,-0.640100,7.072557,-0.787357,3.076631,-5.124054,6.559604,-0.740538,9.165055,3.514170,-5.182350,3.421770,8.047822,-5.668844,9.342077,-0.578797,-0.326545,-0.551016,-4.018064,-5.161246,9.033989,8.622764,5.982991,-9.182180,-6.333860,9.014687,-0.901976,4.573945,2.191847,-9.249835,2.220954,-3.284433,0.219047,2.645057,-9.001550,-5.725540,1.873528,-3.955442,0.885207,2.208120,8.635140,-6.479027,-9.362743,1.064848,9.714645,-3.350460,1.870928,5.793106,2.116928,-5.146603,-4.146210,3.244669,-9.206545,-0.270739,-4.586656,4.259473,-4.954023,-6.854048,-0.662469,-6.897750,8.878897,-4.886427,-5.356120,-0.772018,9.369812,1.628062,8.367763,1.385762,-7.510521,7.690340,8.983538,-2.322088,-5.711482,-3.443811,9.807195,-0.931019,0.377280,6.223150,-6.154381,3.179133,-9.310198,2.496384,3.083804,9.037536,-1.078083,0.244856,8.103533,6.561284,-6.111147,-9.355278,0.245355,-9.784949,-5.935742,-9.124973,9.563639,-8.349935,-0.139838,1.416105,-5.787632,6.058196,8.656728,-3.144885,3.617346,-3.494826,-9.701129,3.663603,-9.039140,-5.331489,2.826440,2.951227,4.562162,-8.179197,-1.521861,0.528045,-9.945352,4.204555,3.963179,-6.759452,-4.162990,-8.465034,-8.891574,-3.977312,-5.075630,3.601596,5.607356,-8.393009,-8.503882,-9.029409,2.970962,2.103265,-1.648766,1.334854,-4.008870,-1.156630,1.607049,3.417935,-3.023596,-7.806391,5.414182,-1.319085,-1.508378,5.473346,3.901742,8.386563,4.039077,-1.422666,-5.282562,-3.625706,-8.610583,4.931910,0.856482,7.947630,-8.433708,-6.556307,6.414033,-7.566317,-8.855843,-6.970803,3.983151,-3.017595,-9.132182,-2.679908,-8.260969,4.242521,-9.806383,-7.441053,-4.912480,8.077004,4.114150,-9.696088,4.322457,7.919220,-4.059998,9.103453,1.187203,-1.915083,2.528390,-2.153943,6.001988,-3.990344,-1.626330,-9.895908,-9.579783,8.802806,2.252262,-9.350965,-0.254269,-5.318798,7.362272,-2.658872,3.011506,-5.675591,-2.781929,4.373847,-7.920119,8.737277,-8.701512,1.220655,9.582348,9.626354,-2.982192,8.167135,9.510822,0.187620,-1.518463,8.798663,7.582182,-4.962253,5.421522,9.592414,9.047976,-8.419486,-8.209129,-4.983547,7.104896,5.564775,9.312738,-4.284687,-9.084139,7.421534,-9.321676,3.952990,-7.705666,5.311324,1.526657,1.904436,2.932665,-3.608666,-9.932687,1.842203,-8.627579,5.680813,-8.068459,-6.649990,-7.140740,6.272221,4.037168,-4.294802,-7.005540,8.559854,-2.396406,-6.379057,-6.388120,-2.326693,9.810266,-0.218698,-0.229933,9.292806,-3.624465,2.633083,1.214194,6.498485,6.842691,-8.684482,5.670440,5.074823,-5.528030,1.586815,7.797235,6.891896,2.250798,-8.795268,-1.880946,-7.055074,-7.867274,4.046446,-3.006017,-1.043197,-7.424642,1.290110,-8.614842,1.639181,-2.032404,1.287647,-1.796537,-4.096270,6.186305,6.631627,-4.199657,-3.395667,-9.718532,-9.630568,-8.140450,-3.565555,5.550350,-8.993659,8.450096,0.067861,-2.090495,5.534362,7.748413,-0.385235,-5.822658,-1.220877,-1.281991,6.628963,-6.053414,0.479036,-3.840690,2.419722,-4.938967,1.095656,-7.032572,9.466547,-2.720117,9.117345,0.841792,-4.726038,-3.519567,-4.251418,8.744045,3.146958,-0.515375,-6.255554,-2.112651,-0.621416,0.434888,-1.539041,-6.461621,-9.172954,-1.098768,5.851510,7.370714,-8.465523,-5.947326,-5.244058,-2.898238,-6.369290,7.818893,-3.972110,-5.548115,-0.419502,-8.122108,8.918419,-2.748242,5.191791,-8.285695,-9.182221,-2.185427,6.070079,-5.165938,-3.901620,0.142126,0.980693,9.209456,-7.937352,-5.383103,2.168043,-7.379493,-1.082721,-9.595126,5.245116,-1.565755,1.671997,-4.804774,1.101040,-9.713693,-3.558878,-6.408291,-6.250613,9.393196,-6.665791,4.536237,-0.627921,-8.010307,3.139853,9.650942,3.657537,-8.919504,-1.373614,9.649437,7.248298,-9.025358,4.575684,7.688852,-7.582189,6.067520,3.512461,2.406635,-3.414309,-8.434901,-5.474702,-6.249649,9.790424,-8.498262,-5.223617,7.460352,-8.796961,8.346890,2.533295,3.977737,4.311097,-1.317464,-3.261636,-7.992426,7.592765,-9.952772,-1.297164,-1.616389,3.912862,-3.508784,-0.029581,-6.998225,3.595095,9.057136,-1.241140,-0.204602,4.636298,-5.414103,-3.961799,-6.127859,0.079541,-3.661864,1.588568,2.606219,9.912849,-0.691909,-8.315326,-6.742012,-7.597865,-3.984933,5.627909,-7.856703,0.982637,-6.103678,-2.974497,0.531360,2.555332,9.168385,-0.435850,2.051453,-2.373491,-6.820617,-1.985842,-0.577174,-8.801770,-3.795281,-7.931181,-9.320888,0.715357,7.745240,0.784598,-0.523848,-9.273338,9.311074,-3.028999,1.496981,4.186399,9.750790,-6.622353,-5.544021,-7.669869,-7.591683,-2.816615,-2.838388,6.589400,7.530792,7.520345,8.356888,5.819103,-5.006700,-1.381441,5.817125,0.990785,7.764777,-0.918498,-8.791206,-8.055200,1.514956,1.515461,1.442167,-4.642576,6.188992,-0.323721,5.056666,-0.240508,2.203465,5.396605,-6.465442,-9.532963,2.456054,3.635705,3.927472,-4.852106,-4.641149,1.104443,6.956407,-0.264681,6.745508,6.255349,4.005689,-6.732480,-5.799295,7.792967,4.021387,4.745042,-5.554007,-3.606508,-1.060510,8.760902,0.786014,-7.454379,-0.323057,3.265083,9.776490,-2.326869,-6.963179,-3.250610,8.504269,7.963986,5.123336,2.926038,-8.076280,2.881288,-1.955493,5.804670,0.917476,-7.391962,2.093368,5.818730,6.849035,0.596595,4.661364,-0.205438,9.165022,1.986224,-6.693871,-7.937834,-9.795353,-9.251462,-6.941823,-6.035937,7.821631,1.367254,5.451840,-1.044445,4.050030,-5.239741,8.409622,1.983220,0.727469,9.335211,4.278105,-8.995648,5.967318,-0.658700,-4.382014,-2.487177,-2.854457,-7.165018,-1.826886,-7.277540,-2.789277,-5.346002,8.582123,-5.171798,-2.891304,2.605311,-0.908831,-9.247757,-2.266188,1.275135,7.862390,-9.144481,-6.212953,7.431987,4.558560,-3.807038,1.020897,6.670439,-9.001830,4.210708,1.836239,-2.447854,-2.885047,-8.945250,1.344257,5.494344,1.691699,-2.051525,9.472505,-8.225934,0.905468,-7.485492,-7.967241,-5.758381,-0.626039,5.171425,-7.123271,3.730367,-9.426799,2.857169,7.842533,7.520727,-7.568826,-0.989322,6.034265,4.088304,4.897207,8.034776,3.203836,-9.680453,6.663977,-1.314084,9.346209,-4.295677,7.079669,-3.512256,5.259757,8.254559,6.060943,1.522697,-7.364520,-1.702429,-9.840715,9.923107,2.151372,2.540598,-5.541396,-4.069547,5.027380,4.094072,-4.290372,-5.586571,5.894328,9.194741,2.019258,-4.292119,6.903905,-1.360570,-3.448430,-2.123893,4.444578,3.554010,7.074585,-3.815940,-7.304672,1.181829,8.945722,-7.614550,9.751807,6.135016,-1.283313,-4.714788,-7.113734,-6.421319,8.736031,-2.159578,-8.633438,-9.638136,3.901588,1.001445,-7.696517,-1.304281,-2.980999,3.732503,7.263853,-6.670506,-0.895501,6.001096,3.637198,2.998057,-0.092291,-4.867121,7.057757,-0.120792,2.145194,7.301958,-8.439048,7.702148,-0.860506,-8.707412,9.815674,-1.056693,-8.640653,3.570705,7.303508,-0.831284,-4.806600,-9.111849,8.365962,5.460009,-8.652258,-9.539800,-3.296946,5.567221,-7.569388,-4.381616,9.918600,8.058979,2.423040,5.832383,-1.190818,-4.841405,-6.151510,-0.457625,-8.452007,-4.058388,-1.414833,3.894549,-3.860460,-7.465811,8.722851,2.752402,8.081781,-1.997215,3.104696,6.084332,2.221036,-5.997344,-1.434057,3.818287,-6.397798,-1.459618,-4.194661,-1.106556,-7.982589,-9.291447,9.665559,-2.515129,-5.595545,0.836012,0.883575,3.498831,0.828138,-8.746734,9.777276,-5.664400,-1.207506,-8.924045,-0.033268,8.359978,5.854957,-2.801719,5.647479,6.058790,7.693710,1.470732,3.098188,0.826121,5.938849,1.946696,6.400083,-9.783289,-8.546216,5.880914,6.132351,7.203252,-5.027425], dtype = "float64")#candidate|17098|(1176,)|const|float64
call_17097 = relay.TupleGetItem(func_14326_call(relay.reshape(const_17098.astype('float64'), [1176,])), 3)
call_17099 = relay.TupleGetItem(func_14328_call(relay.reshape(const_17098.astype('float64'), [1176,])), 3)
func_13404_call = mod.get_global_var('func_13404')
func_13406_call = mutated_mod.get_global_var('func_13406')
const_17107 = relay.const([5,6,-9,3,8,4,8,-5,-1,8,-10,10,-1,10,-1,3,2,-5,8,8,-5,-2,-2,-4,7,-4,8,4,5,7,-10,-1,2,3,5,-9,-4,3,-5,9,-9,-10,9,4,5,9,4,8,-5,7,10,10,5,2,-8,-2,5,2,6,-9,9,-8,5,10,-5,-10,1,1,-1,7,-3,8,1,-4,-8,-9,1,2,3,6,9,5,3,-7,8,-6,3,10,4,2,-7,10,10,3,-4,-3,2,2,-5,-4,2,-7,5,-10,1,2,-3,-5,-2,8,5,8,1,-7,-10,-3,-2,-7,8,-6,9,9,8,-7,-2,8,-8,9,8,-8,-6,1,1,-4,7,-10,-6,10,-2,-6,-2,4,-1,-9,-8,9,10,-3,-10,-2,7,-3,10,6,-10,8,7,4,-6,8,2,9,9,-2,1,8,-5,-10,6,-9,-8,-10,1,-4,-7,-1,2,-8,6,-10,4,-2,10,-4,-7,3,-1,10,-7,9,7,-4,1,-7,-1,-1,-6,-4,6,1,4,-9,-8,-7,3,10,5,8,5,-3,6,-3,-9,-7,6,10,-5,-7,10,-8,9,5,-2,-1,10,-3,-10,-9,3,5,7,1,4,4,1,9,10,5,-8,-8,4,7,6,-4,1,10,5,-9,-7,-5,5,-8,7,-6,2,3,5,-10,5,2,5,5,3,-1,7,9,-1,6,2,2,5,-2,7,-1,-7,-8,7,2,-7,10,-8,-7,-10,6,-6,8,6,-4,-3,5,10,-10,-9,6,-5,2,-9,-2,-4,1,-9,-3,-2,-9,-2,4,-10,-10,7,6,2,5,9,-10,-10,-2,1,-5,2,7,8,7,-6,-6,-3,-6,10,-8,-1,-1,9,-1,1,-5,-7,9,4,3,5,4,2,4,-1,3,1,4,-9,2,10,5,8,5,3,1,-9,-7,4,7,4,-9,3,-4,-10,-4,-4,10,-4,3,4,7,-2,8,-4,3,-2,4,8,8,4,10,1,-9,6,-4,7,-8,4,5,9,-7,-10,8,8,-8,10,-8,2,5,1,-10,9,-7,4,-2,-2,5,9,-2,1,-7,9,-9,-5,9,-6,-4,9,-9,-7,-7,9,1,-7,-2,2,-7,-7,2,-5,-9,9,7,7,2,-6,-3,3,2,8,8,3,10,6,-3,-2,3,6,-1,5,-8,-4,-7,-6,7,-10,3,10,5,-7,6,-3,-1,8,-3,-7,5,4,6,-8,-6,-8,4,-4,6,1,9,1,-2,-3,-2,-6,10,9,-9,-3,-5,-4,10,2,-9,8,-7,-9,-9,-6,3,-8,-3,2,-3,-7,-5,1,-2,1,-6,-1,-9,-5,-5,9,-2,-4,3,-9,1,7,8,1,-1,-1,-1,-3,5,7,7,-9,-3,6,-8,-6,-10,5,1,9,-6,2,-5,8,-2,-1,10,-10,4,3,-10,1,2,-9,9,8,10,-5,-4,6,-7,-5,-8,2,-2,4,-1,-3,8,-7,-3,6,-2,8,-3,2,-1,7,-3,-1,-3,8,-7,-9,4,-6,1,-10,-1,1,-3,4,-9,5,-9,6,9,-7,4,5,-2,-6,-3,5,7,9,-8,-5,-3,8,7,5,-9,-6,8,4,-4,-2,7,2,3,5,4,8,-2,-1,-2,7,-1,-6,-6,-9,-1,9,10,3,5,-3,-9,8,7,10,-8,-1,-2,7,9,10,9,-9,3,2,-1,-6,-6,-4,4,2,-3,-10,-2,-6,-5,3,8,-2,-6,-6,9,-1,-6,8,9,1,-5,-6,10,-9,8,6,4,6,2,10,6,6,4,-2,-4,-4,6,5,4,8,6,10,5,3,-10,1,-4,-7,-3,-3,6,5,9,-7,-5,-7,-2,-4,-10,6,-2,5,-4,-6,3,-3,9,10,-9,3,3,-9,-4,4,10,6,-5,-7,5,-7,5,7,9,3,4,5,5,-4,7,-3,-6,-10,-1,-3,2,-3,1,4,7,9,3,-9,-10,-7,1,-5,-10,9,1,6,-9,2,-8,1,6,-5,5,-9,-8,-1,6,-3,10,6,1,5,-10,3,7,-5,3,-2,-5,3,-7,10,8,-10,5,-10,-9,-10,5,-8,5,-3,-3,-7,6,-2,2,-6,5,-1,-1,1,-7,10,-4,2,2,-8,-2,5,-6,-3,-9,1,5,6,-4,-8,8,2,-6,1,-2,5,7,4,-7,2,-3,1,6,6,4,10,1,6,-6,9,8,-2,6,-8,2,-10,-2,5,-8,-5,-6,-6,7,-6,9,-1,-9,-1,10,7,-9,8,-8,9,-5,-10,-1,10,10,-1,3,-5,-4,9,-8,-7,-5,-10,10,-1,-4,-8,9,3,7,-8,3,-5,4,4,-2,10,-5,-4,-10,10,8,-8,-7,8,-2,-4,-2,5,-5,-9,-9,-6,-1,-1,-7,-2,-8,-2,1,9,-6,10,2,-5,6,3,3,2,-2,-5,-4,4,7,-9,7,4,10,1,-1,8,10,-5,-5,-9,1,-7,-10,7,8,10,3,-9,9,-7,-8,-10,-8,-3,5,1,-7,1,3,9,-5,9,2,-2,-9,1,-4,8,-7,9,7,8,-10,3,8,-5,2,2,1,5,5,-9,-9,4,-2,-8,3,-2,6,6,-7,8,4,-3,5,7,4,-10,-5,-8,7,5,-5,-1,-2,6,8,9,5,-9,2,2,-1,8,9,4,-6,-6,-4,2,3,-5,4,-5,10,9,7,7,-8,-8,2,2,1,-9,-4,2,10,10,-3,-3,6,-4,-5,-5,-5,1,6,-5,3,3,8,-7,-3,2,-2,1,-7,3,4,-7,4,6,1,-7,9,2,-7,6,5,-8,-5,7,3,-5,9,-6,10,-2,-5,-7,-3,2,9,-10,7,3,8,-3,-9,8,10,2,-7,-3,7,9,-1,10,10,-6,9,-1,9,-7,-2,-10,-10,4,-9,4,-9,8,5,-1,9,3,9,6,-8,8,-10,4,-3,9,-9,9,-3,9,-6,-4,10,-4,3,-8,-3,-3,-7,10,9,-1,10,6,9,-5,8,10,9,6,4,-5,2,-7,-8,6,-6,-6,9,4,-9,-2,8,-6,8,9,8,6,-3,-9,-9,8,4,-6,10,-10,8,-8,8,3,6,7,-7,3,5,3,-7,-1,-7,-3,-4,-5,-8,9,7,-1,6,-8,-8,-5,3,9,10,-10,-7,-5,-9,-5,5,3,6,6,2,4,-5,5,6,-7,-3,5,-3,3,1,8,-2,8,7,-9,-8,-10,-2,10,-8,6,3,3,2,-7,-2,10,8,-1,4,3,-10,4,8,2,10,-9,-9,-8,-6,7,1,-1,7,-3,1,2,1,-5,-9,-6,5,1,-6,9,3,-10,-3,-3,-7,1,6,-1,-9,-5,3,7,-5,-2,-7,-2,6,7,5,2,-8,-9,-6,9,-7,8,-8,-6,3,-5,-10,5,9,5,-1,7,10,2,-6,-5,-7,-3,-6,-7,6,3,9,1,-7,-3,5,-8,7,3,10,8,-9,-2,9,-7,-1,2,8,9,2,-4,3,-2,-1,-8,10,-6,-7,5,-10,-3,-3,-3,8,6,6,-5,-3,1,-1,-3,-5,4,-1,-9,3,2,-7,-7,-8,5,3,3,8,-10,-3,3,-5,-9,6,-5,-10,-5,5,1,2,-7,7,-5,-4,-5,-9,4,-3,-8,2,8,-4,10,2,3,7,-3,10,9,-2,-2,3,2,-10,5,-6,6,5,-9,7,-4,-10,1,6,5,-4,-6,-2,3,3,-3,-2,-8,5,5,-7,-8,-8,8,-1,-10,9,-2,-8,-2,4,7,6,-2,-5,7,-5,-1,-6,-5,-4,-9,-2,-4,7,-1,-3,6,6,-4,-4,4,-6,2,-6,6,-3,10,10,-8,-10,-10,9,-4,-4,7,9,-5,6,6,4,9,1,-5,-3,-7,-3,-8,5,-7,-2,4,6,8,-9,-2,-8,-4,-10,7,-1,-10,3,7,2,6,-8,7,2,-4,10,7,8,-7,10,4,2,6,-4,3,6,-1,-2,8,4,6,-9,3,4,-6,6,6,5,-3,-4,6,8,4,-8,3,-4,7,1,1,-4,10,8,-7,-5,-4,9,-8,-9,-6,-3,-8,-7,10,-9,-5,-7,-2,-10,-8,1,5,3,-8,6,-9,4,-7,4,-3,6,5,-3,-8,8,-10,-9,-1,-10,5,5,-4,1,4,-9,-10,4,-10,-4,2,4,1,6,-6,-10,-2,-2,8,10,-1,-6,3,8,-9,-2,2,-2,1,-4,-6,-7,3,-7,-5,2,5,8,-10,-1,-7,-7,-1,6,8,-9,6,3,5,2,-6,-7,4,8,2,-10,-2,-1,-7,3,7,-10,-7,-4,-4,4,3,-8,7,-9,-5,9,10,-10,-5,4,4,4,-8,6,5,1,-1,4,-7,8,-4,9,7,2,-2,-3,-2,-2,5,4,5,-9,6,-8,-6,5,3,5,3,1,4,4,1,6,-3,8,-6,6,-10,-5,1,8,3,-6,-3,-2,3,4,-3,1,-3,-3,8,2,-4,-4,-6,10,6,-6,3,7,-5,1,1,3,5,-4,-7,-10,-3,7,5,-1,-3,1,4,-3,6,8,-10,-3,8,7,-4,-8,1,8,-5,8,-5,-4,-4,-1,-5,-10,-9,9,8,3,-4,9,-8,-3,8,-9,-10,-4,-3,9,-4,-10,-1,2,-6,-3,8,6,-1,-7,10,-1,-2,-7,2,3,-4,-10,-4,4,7,-10,1,9,3,-10,5,-3,10,1,5,-7,7,-4,10,-10,-7,-10,-4,-10,-8,-10,-6,1,5,6,-8,-1,-2,5,-4,9,-5,10,9,-8,2,9,3,2,3,-9,4,-5,4,-10,-7,10,7,1,1,4,-7,1,-4,9,-4,-8,8,-7,-5,3,-8,-4,-2,-3,-6,6,2,3,-2,-3,1,-7,7,3,2,6,8,5,6,-5,-4,6,-10,-4,-5,1,10,-5,3,-1,-4,3,6,4,-5,-6,9,9,-5,4,-9,6,-4,-6,-10,9,3,-8,1,3,-10,-7,3,10,8,-7,-10,6,-3,10,1,-7,-1,-5,6,10,-9,7,-2,1,3,-7,-1,7,-5,-9,-6,3,3,2,6,-7,1,-8,-3,3,6,-10,-2,3,6,8,-8,1,-8,1,7,10,4,-10,-6,-4,4,-1,1,-8,4,10,6,5,6,-10,4,2,-10,6,7,10,1,10,5,-10,-5,-3,2,4,4,3,-8,9,-7,-7,2,-8,9,5], dtype = "int16")#candidate|17107|(1980,)|const|int16
call_17106 = relay.TupleGetItem(func_13404_call(relay.reshape(const_17107.astype('int16'), [1980,])), 2)
call_17108 = relay.TupleGetItem(func_13406_call(relay.reshape(const_17107.astype('int16'), [1980,])), 2)
func_9380_call = mod.get_global_var('func_9380')
func_9382_call = mutated_mod.get_global_var('func_9382')
call_17109 = func_9380_call()
call_17110 = func_9380_call()
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_17114 = relay.TupleGetItem(func_7952_call(), 0)
call_17115 = relay.TupleGetItem(func_7954_call(), 0)
func_10330_call = mod.get_global_var('func_10330')
func_10332_call = mutated_mod.get_global_var('func_10332')
call_17118 = relay.TupleGetItem(func_10330_call(), 1)
call_17119 = relay.TupleGetItem(func_10332_call(), 1)
output = relay.Tuple([call_17087,call_17097,const_17098,call_17106,const_17107,call_17109,call_17114,call_17118,])
output2 = relay.Tuple([call_17088,call_17099,const_17098,call_17108,const_17107,call_17110,call_17115,call_17119,])
func_17156 = relay.Function([], output)
mod['func_17156'] = func_17156
mod = relay.transform.InferType()(mod)
mutated_mod['func_17156'] = func_17156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17156_call = mutated_mod.get_global_var('func_17156')
call_17157 = func_17156_call()
output = call_17157
func_17158 = relay.Function([], output)
mutated_mod['func_17158'] = func_17158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9549_call = mod.get_global_var('func_9549')
func_9550_call = mutated_mod.get_global_var('func_9550')
call_17182 = relay.TupleGetItem(func_9549_call(), 0)
call_17183 = relay.TupleGetItem(func_9550_call(), 0)
func_10653_call = mod.get_global_var('func_10653')
func_10654_call = mutated_mod.get_global_var('func_10654')
call_17187 = func_10653_call()
call_17188 = func_10653_call()
func_7482_call = mod.get_global_var('func_7482')
func_7485_call = mutated_mod.get_global_var('func_7485')
call_17203 = relay.TupleGetItem(func_7482_call(relay.reshape(call_17182.astype('float64'), [5, 2, 7])), 0)
call_17204 = relay.TupleGetItem(func_7485_call(relay.reshape(call_17182.astype('float64'), [5, 2, 7])), 0)
output = relay.Tuple([call_17182,call_17187,call_17203,])
output2 = relay.Tuple([call_17183,call_17188,call_17204,])
func_17216 = relay.Function([], output)
mod['func_17216'] = func_17216
mod = relay.transform.InferType()(mod)
output = func_17216()
func_17217 = relay.Function([], output)
mutated_mod['func_17217'] = func_17217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_17255 = relay.TupleGetItem(func_8021_call(), 0)
call_17256 = relay.TupleGetItem(func_8022_call(), 0)
output = call_17255
output2 = call_17256
func_17286 = relay.Function([], output)
mod['func_17286'] = func_17286
mod = relay.transform.InferType()(mod)
mutated_mod['func_17286'] = func_17286
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17286_call = mutated_mod.get_global_var('func_17286')
call_17287 = func_17286_call()
output = call_17287
func_17288 = relay.Function([], output)
mutated_mod['func_17288'] = func_17288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17072_call = mod.get_global_var('func_17072')
func_17073_call = mutated_mod.get_global_var('func_17073')
call_17327 = relay.TupleGetItem(func_17072_call(), 1)
call_17328 = relay.TupleGetItem(func_17073_call(), 1)
uop_17333 = relay.asin(call_17327.astype('float64')) # shape=(550,)
uop_17335 = relay.asin(call_17328.astype('float64')) # shape=(550,)
output = uop_17333
output2 = uop_17335
func_17339 = relay.Function([], output)
mod['func_17339'] = func_17339
mod = relay.transform.InferType()(mod)
output = func_17339()
func_17340 = relay.Function([], output)
mutated_mod['func_17340'] = func_17340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17377 = relay.var("var_17377", dtype = "float64", shape = (2, 5, 13))#candidate|17377|(2, 5, 13)|var|float64
uop_17378 = relay.asinh(var_17377.astype('float64')) # shape=(2, 5, 13)
func_13745_call = mod.get_global_var('func_13745')
func_13746_call = mutated_mod.get_global_var('func_13746')
call_17391 = func_13745_call()
call_17392 = func_13745_call()
uop_17394 = relay.sigmoid(uop_17378.astype('float32')) # shape=(2, 5, 13)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_17405 = relay.TupleGetItem(func_11617_call(), 0)
call_17406 = relay.TupleGetItem(func_11618_call(), 0)
output = relay.Tuple([call_17391,uop_17394,call_17405,])
output2 = relay.Tuple([call_17392,uop_17394,call_17406,])
func_17429 = relay.Function([var_17377,], output)
mod['func_17429'] = func_17429
mod = relay.transform.InferType()(mod)
mutated_mod['func_17429'] = func_17429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17430 = relay.var("var_17430", dtype = "float64", shape = (2, 5, 13))#candidate|17430|(2, 5, 13)|var|float64
func_17429_call = mutated_mod.get_global_var('func_17429')
call_17431 = func_17429_call(var_17430)
output = call_17431
func_17432 = relay.Function([var_17430], output)
mutated_mod['func_17432'] = func_17432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8782_call = mod.get_global_var('func_8782')
func_8783_call = mutated_mod.get_global_var('func_8783')
call_17455 = relay.TupleGetItem(func_8782_call(), 0)
call_17456 = relay.TupleGetItem(func_8783_call(), 0)
output = relay.Tuple([call_17455,])
output2 = relay.Tuple([call_17456,])
func_17459 = relay.Function([], output)
mod['func_17459'] = func_17459
mod = relay.transform.InferType()(mod)
output = func_17459()
func_17460 = relay.Function([], output)
mutated_mod['func_17460'] = func_17460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13938_call = mod.get_global_var('func_13938')
func_13940_call = mutated_mod.get_global_var('func_13940')
call_17467 = func_13938_call()
call_17468 = func_13938_call()
output = relay.Tuple([call_17467,])
output2 = relay.Tuple([call_17468,])
func_17471 = relay.Function([], output)
mod['func_17471'] = func_17471
mod = relay.transform.InferType()(mod)
mutated_mod['func_17471'] = func_17471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17471_call = mutated_mod.get_global_var('func_17471')
call_17472 = func_17471_call()
output = call_17472
func_17473 = relay.Function([], output)
mutated_mod['func_17473'] = func_17473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_17482 = relay.TupleGetItem(func_11293_call(), 1)
call_17483 = relay.TupleGetItem(func_11295_call(), 1)
func_9380_call = mod.get_global_var('func_9380')
func_9382_call = mutated_mod.get_global_var('func_9382')
call_17504 = func_9380_call()
call_17505 = func_9380_call()
output = relay.Tuple([call_17482,call_17504,])
output2 = relay.Tuple([call_17483,call_17505,])
func_17516 = relay.Function([], output)
mod['func_17516'] = func_17516
mod = relay.transform.InferType()(mod)
output = func_17516()
func_17517 = relay.Function([], output)
mutated_mod['func_17517'] = func_17517
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17534 = relay.var("var_17534", dtype = "uint64", shape = (7, 10, 4))#candidate|17534|(7, 10, 4)|var|uint64
var_17535 = relay.var("var_17535", dtype = "uint64", shape = (7, 10, 4))#candidate|17535|(7, 10, 4)|var|uint64
bop_17536 = relay.greater_equal(var_17534.astype('bool'), relay.reshape(var_17535.astype('bool'), relay.shape_of(var_17534))) # shape=(7, 10, 4)
func_13697_call = mod.get_global_var('func_13697')
func_13698_call = mutated_mod.get_global_var('func_13698')
call_17539 = func_13697_call()
call_17540 = func_13697_call()
func_7482_call = mod.get_global_var('func_7482')
func_7485_call = mutated_mod.get_global_var('func_7485')
var_17576 = relay.var("var_17576", dtype = "float64", shape = (70,))#candidate|17576|(70,)|var|float64
call_17575 = relay.TupleGetItem(func_7482_call(relay.reshape(var_17576.astype('float64'), [5, 2, 7])), 0)
call_17577 = relay.TupleGetItem(func_7485_call(relay.reshape(var_17576.astype('float64'), [5, 2, 7])), 0)
output = relay.Tuple([bop_17536,call_17539,call_17575,var_17576,])
output2 = relay.Tuple([bop_17536,call_17540,call_17577,var_17576,])
func_17587 = relay.Function([var_17534,var_17535,var_17576,], output)
mod['func_17587'] = func_17587
mod = relay.transform.InferType()(mod)
mutated_mod['func_17587'] = func_17587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17587_call = mutated_mod.get_global_var('func_17587')
var_17589 = relay.var("var_17589", dtype = "uint64", shape = (7, 10, 4))#candidate|17589|(7, 10, 4)|var|uint64
var_17590 = relay.var("var_17590", dtype = "uint64", shape = (7, 10, 4))#candidate|17590|(7, 10, 4)|var|uint64
var_17591 = relay.var("var_17591", dtype = "float64", shape = (70,))#candidate|17591|(70,)|var|float64
call_17588 = func_17587_call(var_17589,var_17590,var_17591,)
output = call_17588
func_17592 = relay.Function([var_17589,var_17590,var_17591,], output)
mutated_mod['func_17592'] = func_17592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8212_call = mod.get_global_var('func_8212')
func_8214_call = mutated_mod.get_global_var('func_8214')
call_17621 = relay.TupleGetItem(func_8212_call(), 2)
call_17622 = relay.TupleGetItem(func_8214_call(), 2)
output = relay.Tuple([call_17621,])
output2 = relay.Tuple([call_17622,])
func_17623 = relay.Function([], output)
mod['func_17623'] = func_17623
mod = relay.transform.InferType()(mod)
output = func_17623()
func_17624 = relay.Function([], output)
mutated_mod['func_17624'] = func_17624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17156_call = mod.get_global_var('func_17156')
func_17158_call = mutated_mod.get_global_var('func_17158')
call_17641 = relay.TupleGetItem(func_17156_call(), 4)
call_17642 = relay.TupleGetItem(func_17158_call(), 4)
output = relay.Tuple([call_17641,])
output2 = relay.Tuple([call_17642,])
func_17650 = relay.Function([], output)
mod['func_17650'] = func_17650
mod = relay.transform.InferType()(mod)
mutated_mod['func_17650'] = func_17650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17650_call = mutated_mod.get_global_var('func_17650')
call_17651 = func_17650_call()
output = call_17651
func_17652 = relay.Function([], output)
mutated_mod['func_17652'] = func_17652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8930_call = mod.get_global_var('func_8930')
func_8932_call = mutated_mod.get_global_var('func_8932')
call_17668 = func_8930_call()
call_17669 = func_8930_call()
func_16664_call = mod.get_global_var('func_16664')
func_16665_call = mutated_mod.get_global_var('func_16665')
call_17681 = relay.TupleGetItem(func_16664_call(), 0)
call_17682 = relay.TupleGetItem(func_16665_call(), 0)
output = relay.Tuple([call_17668,call_17681,])
output2 = relay.Tuple([call_17669,call_17682,])
func_17683 = relay.Function([], output)
mod['func_17683'] = func_17683
mod = relay.transform.InferType()(mod)
output = func_17683()
func_17684 = relay.Function([], output)
mutated_mod['func_17684'] = func_17684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15355_call = mod.get_global_var('func_15355')
func_15356_call = mutated_mod.get_global_var('func_15356')
call_17701 = relay.TupleGetItem(func_15355_call(), 0)
call_17702 = relay.TupleGetItem(func_15356_call(), 0)
output = relay.Tuple([call_17701,])
output2 = relay.Tuple([call_17702,])
func_17706 = relay.Function([], output)
mod['func_17706'] = func_17706
mod = relay.transform.InferType()(mod)
mutated_mod['func_17706'] = func_17706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17706_call = mutated_mod.get_global_var('func_17706')
call_17707 = func_17706_call()
output = call_17707
func_17708 = relay.Function([], output)
mutated_mod['func_17708'] = func_17708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15725_call = mod.get_global_var('func_15725')
func_15727_call = mutated_mod.get_global_var('func_15727')
call_17756 = relay.TupleGetItem(func_15725_call(), 0)
call_17757 = relay.TupleGetItem(func_15727_call(), 0)
func_15838_call = mod.get_global_var('func_15838')
func_15839_call = mutated_mod.get_global_var('func_15839')
call_17767 = func_15838_call()
call_17768 = func_15838_call()
func_1094_call = mod.get_global_var('func_1094')
func_1099_call = mutated_mod.get_global_var('func_1099')
var_17770 = relay.var("var_17770", dtype = "int16", shape = ())#candidate|17770|()|var|int16
var_17771 = relay.var("var_17771", dtype = "int16", shape = (18, 110))#candidate|17771|(18, 110)|var|int16
const_17772 = relay.const([7,-2,-3,-3,-8,-2,3,10,-9,5,1,6,7,-9,3,-7,-7,5,-3,-8,7,7,6,-8,-8,-4,10,-6,-6,-3,6,-9,-9,6,5,5,6,3,-1,-6,1,9,1,-10,10,-10,-3,1,3,8,-1,-1,-6,10,5,-8,7,-8,5,-9], dtype = "uint64")#candidate|17772|(60,)|const|uint64
call_17769 = relay.TupleGetItem(func_1094_call(relay.reshape(var_17770.astype('int16'), []), relay.reshape(var_17771.astype('int16'), [15, 12, 11]), relay.reshape(const_17772.astype('uint64'), [60,]), ), 2)
call_17773 = relay.TupleGetItem(func_1099_call(relay.reshape(var_17770.astype('int16'), []), relay.reshape(var_17771.astype('int16'), [15, 12, 11]), relay.reshape(const_17772.astype('uint64'), [60,]), ), 2)
output = relay.Tuple([call_17756,call_17767,call_17769,var_17770,var_17771,const_17772,])
output2 = relay.Tuple([call_17757,call_17768,call_17773,var_17770,var_17771,const_17772,])
func_17789 = relay.Function([var_17770,var_17771,], output)
mod['func_17789'] = func_17789
mod = relay.transform.InferType()(mod)
var_17790 = relay.var("var_17790", dtype = "int16", shape = ())#candidate|17790|()|var|int16
var_17791 = relay.var("var_17791", dtype = "int16", shape = (18, 110))#candidate|17791|(18, 110)|var|int16
output = func_17789(var_17790,var_17791,)
func_17792 = relay.Function([var_17790,var_17791,], output)
mutated_mod['func_17792'] = func_17792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13214_call = mod.get_global_var('func_13214')
func_13216_call = mutated_mod.get_global_var('func_13216')
call_17794 = relay.TupleGetItem(func_13214_call(), 0)
call_17795 = relay.TupleGetItem(func_13216_call(), 0)
func_16988_call = mod.get_global_var('func_16988')
func_16989_call = mutated_mod.get_global_var('func_16989')
call_17805 = func_16988_call()
call_17806 = func_16988_call()
func_7056_call = mod.get_global_var('func_7056')
func_7058_call = mutated_mod.get_global_var('func_7058')
call_17840 = relay.TupleGetItem(func_7056_call(relay.reshape(call_17794.astype('float64'), [3, 7, 7])), 2)
call_17841 = relay.TupleGetItem(func_7058_call(relay.reshape(call_17794.astype('float64'), [3, 7, 7])), 2)
output = relay.Tuple([call_17794,call_17805,call_17840,])
output2 = relay.Tuple([call_17795,call_17806,call_17841,])
func_17844 = relay.Function([], output)
mod['func_17844'] = func_17844
mod = relay.transform.InferType()(mod)
mutated_mod['func_17844'] = func_17844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17844_call = mutated_mod.get_global_var('func_17844')
call_17845 = func_17844_call()
output = call_17845
func_17846 = relay.Function([], output)
mutated_mod['func_17846'] = func_17846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11923_call = mod.get_global_var('func_11923')
func_11924_call = mutated_mod.get_global_var('func_11924')
call_17912 = func_11923_call()
call_17913 = func_11923_call()
func_9493_call = mod.get_global_var('func_9493')
func_9494_call = mutated_mod.get_global_var('func_9494')
call_17934 = func_9493_call()
call_17935 = func_9493_call()
output = relay.Tuple([call_17912,call_17934,])
output2 = relay.Tuple([call_17913,call_17935,])
func_17943 = relay.Function([], output)
mod['func_17943'] = func_17943
mod = relay.transform.InferType()(mod)
output = func_17943()
func_17944 = relay.Function([], output)
mutated_mod['func_17944'] = func_17944
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13491_call = mod.get_global_var('func_13491')
func_13493_call = mutated_mod.get_global_var('func_13493')
call_17954 = relay.TupleGetItem(func_13491_call(), 0)
call_17955 = relay.TupleGetItem(func_13493_call(), 0)
output = call_17954
output2 = call_17955
func_17964 = relay.Function([], output)
mod['func_17964'] = func_17964
mod = relay.transform.InferType()(mod)
output = func_17964()
func_17965 = relay.Function([], output)
mutated_mod['func_17965'] = func_17965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11351_call = mod.get_global_var('func_11351')
func_11352_call = mutated_mod.get_global_var('func_11352')
call_18018 = relay.TupleGetItem(func_11351_call(), 0)
call_18019 = relay.TupleGetItem(func_11352_call(), 0)
func_11190_call = mod.get_global_var('func_11190')
func_11191_call = mutated_mod.get_global_var('func_11191')
call_18025 = relay.TupleGetItem(func_11190_call(), 0)
call_18026 = relay.TupleGetItem(func_11191_call(), 0)
output = relay.Tuple([call_18018,call_18025,])
output2 = relay.Tuple([call_18019,call_18026,])
func_18037 = relay.Function([], output)
mod['func_18037'] = func_18037
mod = relay.transform.InferType()(mod)
mutated_mod['func_18037'] = func_18037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18037_call = mutated_mod.get_global_var('func_18037')
call_18038 = func_18037_call()
output = call_18038
func_18039 = relay.Function([], output)
mutated_mod['func_18039'] = func_18039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15838_call = mod.get_global_var('func_15838')
func_15839_call = mutated_mod.get_global_var('func_15839')
call_18056 = func_15838_call()
call_18057 = func_15838_call()
output = call_18056
output2 = call_18057
func_18060 = relay.Function([], output)
mod['func_18060'] = func_18060
mod = relay.transform.InferType()(mod)
output = func_18060()
func_18061 = relay.Function([], output)
mutated_mod['func_18061'] = func_18061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16108_call = mod.get_global_var('func_16108')
func_16109_call = mutated_mod.get_global_var('func_16109')
call_18082 = relay.TupleGetItem(func_16108_call(), 0)
call_18083 = relay.TupleGetItem(func_16109_call(), 0)
func_16055_call = mod.get_global_var('func_16055')
func_16059_call = mutated_mod.get_global_var('func_16059')
const_18085 = relay.const([5,3,-3,-1,9,-10,-1,9,-1,-2,-7,-1,5,-2,-2,-2,-4,9,5,10,7,-7,2,6,9,10,-4,-4,1,-9,-8,-9,5,10,10,-8,-1,5,-10,-9,-6,-6,9,1,-5,10,1,-8,9,-8,7,8,-10,-3,4,9,10,4,7,-9], dtype = "uint64")#candidate|18085|(60,)|const|uint64
var_18086 = relay.var("var_18086", dtype = "float32", shape = (280,))#candidate|18086|(280,)|var|float32
call_18084 = relay.TupleGetItem(func_16055_call(relay.reshape(const_18085.astype('uint64'), [60,]), relay.reshape(var_18086.astype('float32'), [280,]), ), 3)
call_18087 = relay.TupleGetItem(func_16059_call(relay.reshape(const_18085.astype('uint64'), [60,]), relay.reshape(var_18086.astype('float32'), [280,]), ), 3)
func_15878_call = mod.get_global_var('func_15878')
func_15879_call = mutated_mod.get_global_var('func_15879')
call_18096 = func_15878_call()
call_18097 = func_15878_call()
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_18100 = relay.TupleGetItem(func_8021_call(), 0)
call_18101 = relay.TupleGetItem(func_8022_call(), 0)
func_11923_call = mod.get_global_var('func_11923')
func_11924_call = mutated_mod.get_global_var('func_11924')
call_18106 = func_11923_call()
call_18107 = func_11923_call()
output = relay.Tuple([call_18082,call_18084,const_18085,var_18086,call_18096,call_18100,call_18106,])
output2 = relay.Tuple([call_18083,call_18087,const_18085,var_18086,call_18097,call_18101,call_18107,])
func_18111 = relay.Function([var_18086,], output)
mod['func_18111'] = func_18111
mod = relay.transform.InferType()(mod)
var_18112 = relay.var("var_18112", dtype = "float32", shape = (280,))#candidate|18112|(280,)|var|float32
output = func_18111(var_18112)
func_18113 = relay.Function([var_18112], output)
mutated_mod['func_18113'] = func_18113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14879_call = mod.get_global_var('func_14879')
func_14881_call = mutated_mod.get_global_var('func_14881')
call_18121 = relay.TupleGetItem(func_14879_call(), 2)
call_18122 = relay.TupleGetItem(func_14881_call(), 2)
output = relay.Tuple([call_18121,])
output2 = relay.Tuple([call_18122,])
func_18123 = relay.Function([], output)
mod['func_18123'] = func_18123
mod = relay.transform.InferType()(mod)
output = func_18123()
func_18124 = relay.Function([], output)
mutated_mod['func_18124'] = func_18124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8090_call = mod.get_global_var('func_8090')
func_8091_call = mutated_mod.get_global_var('func_8091')
call_18144 = relay.TupleGetItem(func_8090_call(), 0)
call_18145 = relay.TupleGetItem(func_8091_call(), 0)
output = relay.Tuple([call_18144,])
output2 = relay.Tuple([call_18145,])
func_18161 = relay.Function([], output)
mod['func_18161'] = func_18161
mod = relay.transform.InferType()(mod)
mutated_mod['func_18161'] = func_18161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18161_call = mutated_mod.get_global_var('func_18161')
call_18162 = func_18161_call()
output = call_18162
func_18163 = relay.Function([], output)
mutated_mod['func_18163'] = func_18163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12960_call = mod.get_global_var('func_12960')
func_12962_call = mutated_mod.get_global_var('func_12962')
call_18170 = relay.TupleGetItem(func_12960_call(), 0)
call_18171 = relay.TupleGetItem(func_12962_call(), 0)
output = call_18170
output2 = call_18171
func_18201 = relay.Function([], output)
mod['func_18201'] = func_18201
mod = relay.transform.InferType()(mod)
output = func_18201()
func_18202 = relay.Function([], output)
mutated_mod['func_18202'] = func_18202
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15018_call = mod.get_global_var('func_15018')
func_15020_call = mutated_mod.get_global_var('func_15020')
call_18236 = func_15018_call()
call_18237 = func_15018_call()
func_10106_call = mod.get_global_var('func_10106')
func_10107_call = mutated_mod.get_global_var('func_10107')
call_18262 = func_10106_call()
call_18263 = func_10106_call()
output = relay.Tuple([call_18236,call_18262,])
output2 = relay.Tuple([call_18237,call_18263,])
func_18273 = relay.Function([], output)
mod['func_18273'] = func_18273
mod = relay.transform.InferType()(mod)
mutated_mod['func_18273'] = func_18273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18273_call = mutated_mod.get_global_var('func_18273')
call_18274 = func_18273_call()
output = call_18274
func_18275 = relay.Function([], output)
mutated_mod['func_18275'] = func_18275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16322_call = mod.get_global_var('func_16322')
func_16323_call = mutated_mod.get_global_var('func_16323')
call_18295 = relay.TupleGetItem(func_16322_call(), 0)
call_18296 = relay.TupleGetItem(func_16323_call(), 0)
func_11986_call = mod.get_global_var('func_11986')
func_11988_call = mutated_mod.get_global_var('func_11988')
call_18297 = func_11986_call()
call_18298 = func_11986_call()
output = relay.Tuple([call_18295,call_18297,])
output2 = relay.Tuple([call_18296,call_18298,])
func_18310 = relay.Function([], output)
mod['func_18310'] = func_18310
mod = relay.transform.InferType()(mod)
output = func_18310()
func_18311 = relay.Function([], output)
mutated_mod['func_18311'] = func_18311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13057_call = mod.get_global_var('func_13057')
func_13059_call = mutated_mod.get_global_var('func_13059')
call_18321 = relay.TupleGetItem(func_13057_call(), 0)
call_18322 = relay.TupleGetItem(func_13059_call(), 0)
func_18161_call = mod.get_global_var('func_18161')
func_18163_call = mutated_mod.get_global_var('func_18163')
call_18328 = relay.TupleGetItem(func_18161_call(), 0)
call_18329 = relay.TupleGetItem(func_18163_call(), 0)
output = relay.Tuple([call_18321,call_18328,])
output2 = relay.Tuple([call_18322,call_18329,])
func_18336 = relay.Function([], output)
mod['func_18336'] = func_18336
mod = relay.transform.InferType()(mod)
output = func_18336()
func_18337 = relay.Function([], output)
mutated_mod['func_18337'] = func_18337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15355_call = mod.get_global_var('func_15355')
func_15356_call = mutated_mod.get_global_var('func_15356')
call_18365 = relay.TupleGetItem(func_15355_call(), 0)
call_18366 = relay.TupleGetItem(func_15356_call(), 0)
func_8977_call = mod.get_global_var('func_8977')
func_8978_call = mutated_mod.get_global_var('func_8978')
call_18369 = relay.TupleGetItem(func_8977_call(), 0)
call_18370 = relay.TupleGetItem(func_8978_call(), 0)
func_16295_call = mod.get_global_var('func_16295')
func_16297_call = mutated_mod.get_global_var('func_16297')
call_18374 = relay.TupleGetItem(func_16295_call(), 2)
call_18375 = relay.TupleGetItem(func_16297_call(), 2)
output = relay.Tuple([call_18365,call_18369,call_18374,])
output2 = relay.Tuple([call_18366,call_18370,call_18375,])
func_18384 = relay.Function([], output)
mod['func_18384'] = func_18384
mod = relay.transform.InferType()(mod)
mutated_mod['func_18384'] = func_18384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18384_call = mutated_mod.get_global_var('func_18384')
call_18385 = func_18384_call()
output = call_18385
func_18386 = relay.Function([], output)
mutated_mod['func_18386'] = func_18386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8696_call = mod.get_global_var('func_8696')
func_8697_call = mutated_mod.get_global_var('func_8697')
call_18390 = func_8696_call()
call_18391 = func_8696_call()
func_8782_call = mod.get_global_var('func_8782')
func_8783_call = mutated_mod.get_global_var('func_8783')
call_18398 = relay.TupleGetItem(func_8782_call(), 0)
call_18399 = relay.TupleGetItem(func_8783_call(), 0)
output = relay.Tuple([call_18390,call_18398,])
output2 = relay.Tuple([call_18391,call_18399,])
func_18406 = relay.Function([], output)
mod['func_18406'] = func_18406
mod = relay.transform.InferType()(mod)
mutated_mod['func_18406'] = func_18406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18406_call = mutated_mod.get_global_var('func_18406')
call_18407 = func_18406_call()
output = call_18407
func_18408 = relay.Function([], output)
mutated_mod['func_18408'] = func_18408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18123_call = mod.get_global_var('func_18123')
func_18124_call = mutated_mod.get_global_var('func_18124')
call_18412 = relay.TupleGetItem(func_18123_call(), 0)
call_18413 = relay.TupleGetItem(func_18124_call(), 0)
output = call_18412
output2 = call_18413
func_18424 = relay.Function([], output)
mod['func_18424'] = func_18424
mod = relay.transform.InferType()(mod)
output = func_18424()
func_18425 = relay.Function([], output)
mutated_mod['func_18425'] = func_18425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_18439 = func_7106_call()
call_18440 = func_7106_call()
func_13404_call = mod.get_global_var('func_13404')
func_13406_call = mutated_mod.get_global_var('func_13406')
var_18456 = relay.var("var_18456", dtype = "int16", shape = (90, 22))#candidate|18456|(90, 22)|var|int16
call_18455 = relay.TupleGetItem(func_13404_call(relay.reshape(var_18456.astype('int16'), [1980,])), 2)
call_18457 = relay.TupleGetItem(func_13406_call(relay.reshape(var_18456.astype('int16'), [1980,])), 2)
func_11336_call = mod.get_global_var('func_11336')
func_11337_call = mutated_mod.get_global_var('func_11337')
call_18463 = func_11336_call()
call_18464 = func_11336_call()
output = relay.Tuple([call_18439,call_18455,var_18456,call_18463,])
output2 = relay.Tuple([call_18440,call_18457,var_18456,call_18464,])
func_18471 = relay.Function([var_18456,], output)
mod['func_18471'] = func_18471
mod = relay.transform.InferType()(mod)
mutated_mod['func_18471'] = func_18471
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18472 = relay.var("var_18472", dtype = "int16", shape = (90, 22))#candidate|18472|(90, 22)|var|int16
func_18471_call = mutated_mod.get_global_var('func_18471')
call_18473 = func_18471_call(var_18472)
output = call_18473
func_18474 = relay.Function([var_18472], output)
mutated_mod['func_18474'] = func_18474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12960_call = mod.get_global_var('func_12960')
func_12962_call = mutated_mod.get_global_var('func_12962')
call_18482 = relay.TupleGetItem(func_12960_call(), 0)
call_18483 = relay.TupleGetItem(func_12962_call(), 0)
output = call_18482
output2 = call_18483
func_18489 = relay.Function([], output)
mod['func_18489'] = func_18489
mod = relay.transform.InferType()(mod)
output = func_18489()
func_18490 = relay.Function([], output)
mutated_mod['func_18490'] = func_18490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17706_call = mod.get_global_var('func_17706')
func_17708_call = mutated_mod.get_global_var('func_17708')
call_18491 = relay.TupleGetItem(func_17706_call(), 0)
call_18492 = relay.TupleGetItem(func_17708_call(), 0)
output = call_18491
output2 = call_18492
func_18505 = relay.Function([], output)
mod['func_18505'] = func_18505
mod = relay.transform.InferType()(mod)
output = func_18505()
func_18506 = relay.Function([], output)
mutated_mod['func_18506'] = func_18506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_18564 = relay.TupleGetItem(func_11293_call(), 0)
call_18565 = relay.TupleGetItem(func_11295_call(), 0)
func_16555_call = mod.get_global_var('func_16555')
func_16557_call = mutated_mod.get_global_var('func_16557')
call_18573 = func_16555_call()
call_18574 = func_16555_call()
func_12204_call = mod.get_global_var('func_12204')
func_12206_call = mutated_mod.get_global_var('func_12206')
const_18586 = relay.const([True,True,False,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,True,False,False,True,True,True,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True], dtype = "bool")#candidate|18586|(560,)|const|bool
call_18585 = func_12204_call(relay.reshape(const_18586.astype('bool'), [10, 7, 8]))
call_18587 = func_12204_call(relay.reshape(const_18586.astype('bool'), [10, 7, 8]))
func_11293_call = mod.get_global_var('func_11293')
func_11295_call = mutated_mod.get_global_var('func_11295')
call_18593 = relay.TupleGetItem(func_11293_call(), 1)
call_18594 = relay.TupleGetItem(func_11295_call(), 1)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_18610 = relay.TupleGetItem(func_11617_call(), 1)
call_18611 = relay.TupleGetItem(func_11618_call(), 1)
func_17429_call = mod.get_global_var('func_17429')
func_17432_call = mutated_mod.get_global_var('func_17432')
const_18633 = relay.const([-1.457346,0.001754,-6.365857,-3.279517,-2.219347,-0.256151,-0.863535,-1.841885,-6.557596,0.526188,0.801462,-4.948888,3.446776,-6.144612,5.340949,7.049763,-0.440812,1.572733,-1.287608,3.466169,-3.207285,-0.872312,-0.786489,0.583394,4.262079,-0.117989,-8.569753,7.528105,-9.249254,-0.676901,3.118167,0.758941,-3.954559,-2.317777,-6.791769,6.353828,-8.809691,2.684242,-7.312766,2.053417,-2.250494,5.968253,-7.395429,-8.526900,-1.351223,3.174895,-3.480237,9.886999,9.386654,-6.477330,4.943942,1.274546,2.397506,-0.003078,6.004055,5.629493,-4.254593,-1.629480,-2.349970,6.930711,-9.773292,-6.531591,8.132826,9.333845,-2.767799,-7.332881,-5.365680,4.775568,-0.734964,6.810481,4.370176,2.947409,7.386473,2.300488,-2.321615,-7.225078,3.834611,-1.478137,7.766970,4.950859,7.948598,7.845642,7.545380,4.119910,9.845714,3.262193,2.800308,-1.474767,9.817660,-7.043032,-1.367885,-7.164185,-6.801267,-3.179007,-7.008824,3.671171,9.606108,0.589943,6.847291,-0.512282,-7.007770,7.802033,3.181891,-9.299535,0.218704,-4.582488,-7.337492,0.774351,8.133184,-4.693783,-1.185044,2.446596,-0.568034,-0.092514,9.056876,-4.624902,6.033154,-0.448754,2.382159,7.307000,0.376344,-8.747103,-0.844028,-5.030337,3.997611,9.881083,-4.829741,4.147692,-8.106541,-1.537307], dtype = "float64")#candidate|18633|(130,)|const|float64
call_18632 = relay.TupleGetItem(func_17429_call(relay.reshape(const_18633.astype('float64'), [2, 5, 13])), 2)
call_18634 = relay.TupleGetItem(func_17432_call(relay.reshape(const_18633.astype('float64'), [2, 5, 13])), 2)
output = relay.Tuple([call_18564,call_18573,call_18585,const_18586,call_18593,call_18610,call_18632,const_18633,])
output2 = relay.Tuple([call_18565,call_18574,call_18587,const_18586,call_18594,call_18611,call_18634,const_18633,])
func_18637 = relay.Function([], output)
mod['func_18637'] = func_18637
mod = relay.transform.InferType()(mod)
output = func_18637()
func_18638 = relay.Function([], output)
mutated_mod['func_18638'] = func_18638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18310_call = mod.get_global_var('func_18310')
func_18311_call = mutated_mod.get_global_var('func_18311')
call_18668 = relay.TupleGetItem(func_18310_call(), 1)
call_18669 = relay.TupleGetItem(func_18311_call(), 1)
func_11894_call = mod.get_global_var('func_11894')
func_11897_call = mutated_mod.get_global_var('func_11897')
var_18673 = relay.var("var_18673", dtype = "float32", shape = (48,))#candidate|18673|(48,)|var|float32
call_18672 = relay.TupleGetItem(func_11894_call(relay.reshape(var_18673.astype('float32'), [48,])), 3)
call_18674 = relay.TupleGetItem(func_11897_call(relay.reshape(var_18673.astype('float32'), [48,])), 3)
func_18336_call = mod.get_global_var('func_18336')
func_18337_call = mutated_mod.get_global_var('func_18337')
call_18679 = relay.TupleGetItem(func_18336_call(), 0)
call_18680 = relay.TupleGetItem(func_18337_call(), 0)
func_11447_call = mod.get_global_var('func_11447')
func_11449_call = mutated_mod.get_global_var('func_11449')
var_18682 = relay.var("var_18682", dtype = "int16", shape = (1980,))#candidate|18682|(1980,)|var|int16
call_18681 = relay.TupleGetItem(func_11447_call(relay.reshape(var_18682.astype('int16'), [1980,])), 1)
call_18683 = relay.TupleGetItem(func_11449_call(relay.reshape(var_18682.astype('int16'), [1980,])), 1)
output = relay.Tuple([call_18668,call_18672,var_18673,call_18679,call_18681,var_18682,])
output2 = relay.Tuple([call_18669,call_18674,var_18673,call_18680,call_18683,var_18682,])
func_18693 = relay.Function([var_18673,var_18682,], output)
mod['func_18693'] = func_18693
mod = relay.transform.InferType()(mod)
var_18694 = relay.var("var_18694", dtype = "float32", shape = (48,))#candidate|18694|(48,)|var|float32
var_18695 = relay.var("var_18695", dtype = "int16", shape = (1980,))#candidate|18695|(1980,)|var|int16
output = func_18693(var_18694,var_18695,)
func_18696 = relay.Function([var_18694,var_18695,], output)
mutated_mod['func_18696'] = func_18696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14546_call = mod.get_global_var('func_14546')
func_14547_call = mutated_mod.get_global_var('func_14547')
call_18707 = relay.TupleGetItem(func_14546_call(), 0)
call_18708 = relay.TupleGetItem(func_14547_call(), 0)
func_8192_call = mod.get_global_var('func_8192')
func_8194_call = mutated_mod.get_global_var('func_8194')
call_18713 = relay.TupleGetItem(func_8192_call(), 1)
call_18714 = relay.TupleGetItem(func_8194_call(), 1)
output = relay.Tuple([call_18707,call_18713,])
output2 = relay.Tuple([call_18708,call_18714,])
func_18717 = relay.Function([], output)
mod['func_18717'] = func_18717
mod = relay.transform.InferType()(mod)
output = func_18717()
func_18718 = relay.Function([], output)
mutated_mod['func_18718'] = func_18718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9493_call = mod.get_global_var('func_9493')
func_9494_call = mutated_mod.get_global_var('func_9494')
call_18736 = func_9493_call()
call_18737 = func_9493_call()
func_16164_call = mod.get_global_var('func_16164')
func_16165_call = mutated_mod.get_global_var('func_16165')
call_18749 = func_16164_call()
call_18750 = func_16164_call()
var_18754 = relay.var("var_18754", dtype = "float64", shape = (6, 16, 5))#candidate|18754|(6, 16, 5)|var|float64
bop_18755 = relay.subtract(call_18749.astype('float32'), relay.reshape(var_18754.astype('float32'), relay.shape_of(call_18749))) # shape=(6, 16, 5)
bop_18758 = relay.subtract(call_18750.astype('float32'), relay.reshape(var_18754.astype('float32'), relay.shape_of(call_18750))) # shape=(6, 16, 5)
func_17286_call = mod.get_global_var('func_17286')
func_17288_call = mutated_mod.get_global_var('func_17288')
call_18776 = func_17286_call()
call_18777 = func_17286_call()
uop_18793 = relay.sqrt(var_18754.astype('float32')) # shape=(6, 16, 5)
output = relay.Tuple([call_18736,bop_18755,call_18776,uop_18793,])
output2 = relay.Tuple([call_18737,bop_18758,call_18777,uop_18793,])
func_18795 = relay.Function([var_18754,], output)
mod['func_18795'] = func_18795
mod = relay.transform.InferType()(mod)
var_18796 = relay.var("var_18796", dtype = "float64", shape = (6, 16, 5))#candidate|18796|(6, 16, 5)|var|float64
output = func_18795(var_18796)
func_18797 = relay.Function([var_18796], output)
mutated_mod['func_18797'] = func_18797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13260_call = mod.get_global_var('func_13260')
func_13262_call = mutated_mod.get_global_var('func_13262')
call_18799 = relay.TupleGetItem(func_13260_call(), 1)
call_18800 = relay.TupleGetItem(func_13262_call(), 1)
output = relay.Tuple([call_18799,])
output2 = relay.Tuple([call_18800,])
func_18811 = relay.Function([], output)
mod['func_18811'] = func_18811
mod = relay.transform.InferType()(mod)
mutated_mod['func_18811'] = func_18811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18811_call = mutated_mod.get_global_var('func_18811')
call_18812 = func_18811_call()
output = call_18812
func_18813 = relay.Function([], output)
mutated_mod['func_18813'] = func_18813
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8349_call = mod.get_global_var('func_8349')
func_8350_call = mutated_mod.get_global_var('func_8350')
call_18817 = func_8349_call()
call_18818 = func_8349_call()
func_7925_call = mod.get_global_var('func_7925')
func_7928_call = mutated_mod.get_global_var('func_7928')
const_18831 = relay.const([True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,True,True,False,False,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,False,False], dtype = "bool")#candidate|18831|(1008,)|const|bool
call_18830 = relay.TupleGetItem(func_7925_call(relay.reshape(const_18831.astype('bool'), [1008, 1])), 4)
call_18832 = relay.TupleGetItem(func_7928_call(relay.reshape(const_18831.astype('bool'), [1008, 1])), 4)
bop_18835 = relay.minimum(call_18830.astype('float32'), relay.reshape(const_18831.astype('float32'), relay.shape_of(call_18830))) # shape=(1008, 1)
bop_18838 = relay.minimum(call_18832.astype('float32'), relay.reshape(const_18831.astype('float32'), relay.shape_of(call_18832))) # shape=(1008, 1)
output = relay.Tuple([call_18817,bop_18835,])
output2 = relay.Tuple([call_18818,bop_18838,])
func_18849 = relay.Function([], output)
mod['func_18849'] = func_18849
mod = relay.transform.InferType()(mod)
mutated_mod['func_18849'] = func_18849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18849_call = mutated_mod.get_global_var('func_18849')
call_18850 = func_18849_call()
output = call_18850
func_18851 = relay.Function([], output)
mutated_mod['func_18851'] = func_18851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18384_call = mod.get_global_var('func_18384')
func_18386_call = mutated_mod.get_global_var('func_18386')
call_18932 = relay.TupleGetItem(func_18384_call(), 0)
call_18933 = relay.TupleGetItem(func_18386_call(), 0)
output = call_18932
output2 = call_18933
func_18942 = relay.Function([], output)
mod['func_18942'] = func_18942
mod = relay.transform.InferType()(mod)
output = func_18942()
func_18943 = relay.Function([], output)
mutated_mod['func_18943'] = func_18943
mutated_mod = relay.transform.InferType()(mutated_mod)
var_18944 = relay.var("var_18944", dtype = "float32", shape = (12, 11, 10))#candidate|18944|(12, 11, 10)|var|float32
uop_18945 = relay.log2(var_18944.astype('float32')) # shape=(12, 11, 10)
func_11566_call = mod.get_global_var('func_11566')
func_11570_call = mutated_mod.get_global_var('func_11570')
const_18949 = relay.const([[2,1],[7,-8],[-8,5],[1,7],[-6,-6],[-7,2],[-5,9]], dtype = "uint8")#candidate|18949|(7, 2)|const|uint8
const_18950 = relay.const([-2,-5,10,6,9,4,-1,3,8,-3,10,5,2,-1,7,-4,10,1,-1,9,-10,6,-7,-9,10,9,-2,10,-6,4,-2,2,10,-5,8,-3,-8,-10,-9,9,-9,-9,-5,-8,1,-2,-2,4,-6,3,4,2,6,-6,1,4], dtype = "uint8")#candidate|18950|(56,)|const|uint8
call_18948 = relay.TupleGetItem(func_11566_call(relay.reshape(const_18949.astype('uint8'), [1, 1, 14]), relay.reshape(const_18950.astype('uint8'), [4, 1, 14]), ), 0)
call_18951 = relay.TupleGetItem(func_11570_call(relay.reshape(const_18949.astype('uint8'), [1, 1, 14]), relay.reshape(const_18950.astype('uint8'), [4, 1, 14]), ), 0)
func_18384_call = mod.get_global_var('func_18384')
func_18386_call = mutated_mod.get_global_var('func_18386')
call_18963 = relay.TupleGetItem(func_18384_call(), 1)
call_18964 = relay.TupleGetItem(func_18386_call(), 1)
output = relay.Tuple([uop_18945,call_18948,const_18949,const_18950,call_18963,])
output2 = relay.Tuple([uop_18945,call_18951,const_18949,const_18950,call_18964,])
func_18966 = relay.Function([var_18944,], output)
mod['func_18966'] = func_18966
mod = relay.transform.InferType()(mod)
var_18967 = relay.var("var_18967", dtype = "float32", shape = (12, 11, 10))#candidate|18967|(12, 11, 10)|var|float32
output = func_18966(var_18967)
func_18968 = relay.Function([var_18967], output)
mutated_mod['func_18968'] = func_18968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15612_call = mod.get_global_var('func_15612')
func_15614_call = mutated_mod.get_global_var('func_15614')
call_18985 = relay.TupleGetItem(func_15612_call(), 0)
call_18986 = relay.TupleGetItem(func_15614_call(), 0)
output = relay.Tuple([call_18985,])
output2 = relay.Tuple([call_18986,])
func_19000 = relay.Function([], output)
mod['func_19000'] = func_19000
mod = relay.transform.InferType()(mod)
mutated_mod['func_19000'] = func_19000
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19000_call = mutated_mod.get_global_var('func_19000')
call_19001 = func_19000_call()
output = call_19001
func_19002 = relay.Function([], output)
mutated_mod['func_19002'] = func_19002
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9607_call = mod.get_global_var('func_9607')
func_9609_call = mutated_mod.get_global_var('func_9609')
call_19040 = relay.TupleGetItem(func_9607_call(), 1)
call_19041 = relay.TupleGetItem(func_9609_call(), 1)
output = relay.Tuple([call_19040,])
output2 = relay.Tuple([call_19041,])
func_19044 = relay.Function([], output)
mod['func_19044'] = func_19044
mod = relay.transform.InferType()(mod)
output = func_19044()
func_19045 = relay.Function([], output)
mutated_mod['func_19045'] = func_19045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17471_call = mod.get_global_var('func_17471')
func_17473_call = mutated_mod.get_global_var('func_17473')
call_19052 = relay.TupleGetItem(func_17471_call(), 0)
call_19053 = relay.TupleGetItem(func_17473_call(), 0)
func_14984_call = mod.get_global_var('func_14984')
func_14987_call = mutated_mod.get_global_var('func_14987')
var_19083 = relay.var("var_19083", dtype = "uint64", shape = (30, 2))#candidate|19083|(30, 2)|var|uint64
call_19082 = relay.TupleGetItem(func_14984_call(relay.reshape(var_19083.astype('uint64'), [60,])), 4)
call_19084 = relay.TupleGetItem(func_14987_call(relay.reshape(var_19083.astype('uint64'), [60,])), 4)
func_12534_call = mod.get_global_var('func_12534')
func_12535_call = mutated_mod.get_global_var('func_12535')
call_19106 = relay.TupleGetItem(func_12534_call(), 1)
call_19107 = relay.TupleGetItem(func_12535_call(), 1)
func_9894_call = mod.get_global_var('func_9894')
func_9896_call = mutated_mod.get_global_var('func_9896')
call_19144 = relay.TupleGetItem(func_9894_call(), 0)
call_19145 = relay.TupleGetItem(func_9896_call(), 0)
output = relay.Tuple([call_19052,call_19082,var_19083,call_19106,call_19144,])
output2 = relay.Tuple([call_19053,call_19084,var_19083,call_19107,call_19145,])
func_19150 = relay.Function([var_19083,], output)
mod['func_19150'] = func_19150
mod = relay.transform.InferType()(mod)
var_19151 = relay.var("var_19151", dtype = "uint64", shape = (30, 2))#candidate|19151|(30, 2)|var|uint64
output = func_19150(var_19151)
func_19152 = relay.Function([var_19151], output)
mutated_mod['func_19152'] = func_19152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17286_call = mod.get_global_var('func_17286')
func_17288_call = mutated_mod.get_global_var('func_17288')
call_19159 = func_17286_call()
call_19160 = func_17286_call()
func_9637_call = mod.get_global_var('func_9637')
func_9639_call = mutated_mod.get_global_var('func_9639')
call_19164 = func_9637_call()
call_19165 = func_9637_call()
output = relay.Tuple([call_19159,call_19164,])
output2 = relay.Tuple([call_19160,call_19165,])
func_19175 = relay.Function([], output)
mod['func_19175'] = func_19175
mod = relay.transform.InferType()(mod)
output = func_19175()
func_19176 = relay.Function([], output)
mutated_mod['func_19176'] = func_19176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_19182 = relay.var("var_19182", dtype = "int64", shape = (3, 4, 13))#candidate|19182|(3, 4, 13)|var|int64
var_19183 = relay.var("var_19183", dtype = "int64", shape = (3, 4, 13))#candidate|19183|(3, 4, 13)|var|int64
bop_19184 = relay.bitwise_and(var_19182.astype('int64'), relay.reshape(var_19183.astype('int64'), relay.shape_of(var_19182))) # shape=(3, 4, 13)
func_531_call = mod.get_global_var('func_531')
func_535_call = mutated_mod.get_global_var('func_535')
const_19193 = relay.const([7,-10,-8,1,6,-3,-9,2,9,4,10,1,6,3,5,7,-9,-2,-7,-3,8,5,-10,9,-3,-3,9,-6,-3,6,-10,1,-9,8,-8,8,-6,-5,9,8,-1,4,6,-6,2,-6,-4,-4,1,-10,3,-7,10,-7,-8,-1,-5,-10,5,-9], dtype = "uint64")#candidate|19193|(60,)|const|uint64
call_19192 = func_531_call(relay.reshape(const_19193.astype('uint64'), [2, 5, 6]), relay.reshape(const_19193.astype('uint64'), [2, 5, 6]), )
call_19194 = func_531_call(relay.reshape(const_19193.astype('uint64'), [2, 5, 6]), relay.reshape(const_19193.astype('uint64'), [2, 5, 6]), )
output = relay.Tuple([bop_19184,call_19192,const_19193,])
output2 = relay.Tuple([bop_19184,call_19194,const_19193,])
func_19198 = relay.Function([var_19182,var_19183,], output)
mod['func_19198'] = func_19198
mod = relay.transform.InferType()(mod)
var_19199 = relay.var("var_19199", dtype = "int64", shape = (3, 4, 13))#candidate|19199|(3, 4, 13)|var|int64
var_19200 = relay.var("var_19200", dtype = "int64", shape = (3, 4, 13))#candidate|19200|(3, 4, 13)|var|int64
output = func_19198(var_19199,var_19200,)
func_19201 = relay.Function([var_19199,var_19200,], output)
mutated_mod['func_19201'] = func_19201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17650_call = mod.get_global_var('func_17650')
func_17652_call = mutated_mod.get_global_var('func_17652')
call_19363 = relay.TupleGetItem(func_17650_call(), 0)
call_19364 = relay.TupleGetItem(func_17652_call(), 0)
output = relay.Tuple([call_19363,])
output2 = relay.Tuple([call_19364,])
func_19365 = relay.Function([], output)
mod['func_19365'] = func_19365
mod = relay.transform.InferType()(mod)
output = func_19365()
func_19366 = relay.Function([], output)
mutated_mod['func_19366'] = func_19366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13214_call = mod.get_global_var('func_13214')
func_13216_call = mutated_mod.get_global_var('func_13216')
call_19371 = relay.TupleGetItem(func_13214_call(), 0)
call_19372 = relay.TupleGetItem(func_13216_call(), 0)
output = call_19371
output2 = call_19372
func_19379 = relay.Function([], output)
mod['func_19379'] = func_19379
mod = relay.transform.InferType()(mod)
output = func_19379()
func_19380 = relay.Function([], output)
mutated_mod['func_19380'] = func_19380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15369_call = mod.get_global_var('func_15369')
func_15371_call = mutated_mod.get_global_var('func_15371')
call_19381 = relay.TupleGetItem(func_15369_call(), 0)
call_19382 = relay.TupleGetItem(func_15371_call(), 0)
func_15331_call = mod.get_global_var('func_15331')
func_15333_call = mutated_mod.get_global_var('func_15333')
call_19385 = relay.TupleGetItem(func_15331_call(), 0)
call_19386 = relay.TupleGetItem(func_15333_call(), 0)
output = relay.Tuple([call_19381,call_19385,])
output2 = relay.Tuple([call_19382,call_19386,])
func_19400 = relay.Function([], output)
mod['func_19400'] = func_19400
mod = relay.transform.InferType()(mod)
output = func_19400()
func_19401 = relay.Function([], output)
mutated_mod['func_19401'] = func_19401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15355_call = mod.get_global_var('func_15355')
func_15356_call = mutated_mod.get_global_var('func_15356')
call_19441 = relay.TupleGetItem(func_15355_call(), 0)
call_19442 = relay.TupleGetItem(func_15356_call(), 0)
output = relay.Tuple([call_19441,])
output2 = relay.Tuple([call_19442,])
func_19477 = relay.Function([], output)
mod['func_19477'] = func_19477
mod = relay.transform.InferType()(mod)
output = func_19477()
func_19478 = relay.Function([], output)
mutated_mod['func_19478'] = func_19478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9894_call = mod.get_global_var('func_9894')
func_9896_call = mutated_mod.get_global_var('func_9896')
call_19485 = relay.TupleGetItem(func_9894_call(), 0)
call_19486 = relay.TupleGetItem(func_9896_call(), 0)
func_18123_call = mod.get_global_var('func_18123')
func_18124_call = mutated_mod.get_global_var('func_18124')
call_19512 = relay.TupleGetItem(func_18123_call(), 0)
call_19513 = relay.TupleGetItem(func_18124_call(), 0)
output = relay.Tuple([call_19485,call_19512,])
output2 = relay.Tuple([call_19486,call_19513,])
func_19525 = relay.Function([], output)
mod['func_19525'] = func_19525
mod = relay.transform.InferType()(mod)
output = func_19525()
func_19526 = relay.Function([], output)
mutated_mod['func_19526'] = func_19526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12839_call = mod.get_global_var('func_12839')
func_12841_call = mutated_mod.get_global_var('func_12841')
call_19539 = relay.TupleGetItem(func_12839_call(), 2)
call_19540 = relay.TupleGetItem(func_12841_call(), 2)
output = call_19539
output2 = call_19540
func_19543 = relay.Function([], output)
mod['func_19543'] = func_19543
mod = relay.transform.InferType()(mod)
mutated_mod['func_19543'] = func_19543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19543_call = mutated_mod.get_global_var('func_19543')
call_19544 = func_19543_call()
output = call_19544
func_19545 = relay.Function([], output)
mutated_mod['func_19545'] = func_19545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10330_call = mod.get_global_var('func_10330')
func_10332_call = mutated_mod.get_global_var('func_10332')
call_19568 = relay.TupleGetItem(func_10330_call(), 0)
call_19569 = relay.TupleGetItem(func_10332_call(), 0)
func_16108_call = mod.get_global_var('func_16108')
func_16109_call = mutated_mod.get_global_var('func_16109')
call_19580 = relay.TupleGetItem(func_16108_call(), 0)
call_19581 = relay.TupleGetItem(func_16109_call(), 0)
output = relay.Tuple([call_19568,call_19580,])
output2 = relay.Tuple([call_19569,call_19581,])
func_19589 = relay.Function([], output)
mod['func_19589'] = func_19589
mod = relay.transform.InferType()(mod)
mutated_mod['func_19589'] = func_19589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19589_call = mutated_mod.get_global_var('func_19589')
call_19590 = func_19589_call()
output = call_19590
func_19591 = relay.Function([], output)
mutated_mod['func_19591'] = func_19591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11617_call = mod.get_global_var('func_11617')
func_11618_call = mutated_mod.get_global_var('func_11618')
call_19624 = relay.TupleGetItem(func_11617_call(), 1)
call_19625 = relay.TupleGetItem(func_11618_call(), 1)
output = relay.Tuple([call_19624,])
output2 = relay.Tuple([call_19625,])
func_19631 = relay.Function([], output)
mod['func_19631'] = func_19631
mod = relay.transform.InferType()(mod)
output = func_19631()
func_19632 = relay.Function([], output)
mutated_mod['func_19632'] = func_19632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13290_call = mod.get_global_var('func_13290')
func_13291_call = mutated_mod.get_global_var('func_13291')
call_19711 = func_13290_call()
call_19712 = func_13290_call()
var_19724 = relay.var("var_19724", dtype = "uint8", shape = (2, 12, 10))#candidate|19724|(2, 12, 10)|var|uint8
bop_19725 = relay.floor_mod(call_19711.astype('float64'), relay.reshape(var_19724.astype('float64'), relay.shape_of(call_19711))) # shape=(2, 12, 10)
bop_19728 = relay.floor_mod(call_19712.astype('float64'), relay.reshape(var_19724.astype('float64'), relay.shape_of(call_19712))) # shape=(2, 12, 10)
output = relay.Tuple([bop_19725,])
output2 = relay.Tuple([bop_19728,])
func_19729 = relay.Function([var_19724,], output)
mod['func_19729'] = func_19729
mod = relay.transform.InferType()(mod)
var_19730 = relay.var("var_19730", dtype = "uint8", shape = (2, 12, 10))#candidate|19730|(2, 12, 10)|var|uint8
output = func_19729(var_19730)
func_19731 = relay.Function([var_19730], output)
mutated_mod['func_19731'] = func_19731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7106_call = mod.get_global_var('func_7106')
func_7107_call = mutated_mod.get_global_var('func_7107')
call_19733 = func_7106_call()
call_19734 = func_7106_call()
func_17471_call = mod.get_global_var('func_17471')
func_17473_call = mutated_mod.get_global_var('func_17473')
call_19744 = relay.TupleGetItem(func_17471_call(), 0)
call_19745 = relay.TupleGetItem(func_17473_call(), 0)
output = relay.Tuple([call_19733,call_19744,])
output2 = relay.Tuple([call_19734,call_19745,])
func_19758 = relay.Function([], output)
mod['func_19758'] = func_19758
mod = relay.transform.InferType()(mod)
mutated_mod['func_19758'] = func_19758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19758_call = mutated_mod.get_global_var('func_19758')
call_19759 = func_19758_call()
output = call_19759
func_19760 = relay.Function([], output)
mutated_mod['func_19760'] = func_19760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9097_call = mod.get_global_var('func_9097')
func_9099_call = mutated_mod.get_global_var('func_9099')
call_19775 = func_9097_call()
call_19776 = func_9097_call()
func_938_call = mod.get_global_var('func_938')
func_940_call = mutated_mod.get_global_var('func_940')
const_19788 = relay.const([-1.059460,2.893479,6.962314,6.212242,-1.875339,4.609971,7.487443,2.136570,0.857214,7.987648,-7.086583,-3.958092,-3.470211,3.217091,-6.302387,-4.971445,-4.737739,8.194854,-2.546659,2.259727,0.765690,8.884503,-9.839930,-1.297230,-9.445650,0.364146,-0.793391,9.891353,-9.545074,-3.650374,3.574385,7.835715,-7.180032,-0.904112,-8.930282,-7.080502,-1.768921,-9.161541,-6.955770,4.826505,-5.603353,0.003701,-8.822430,5.685620,5.712481,-6.424243,-3.786988,-2.807257,-7.263011,1.946398,-2.490693,-5.358534,-0.181855,-7.927977,-9.658620,5.424502,-6.203806,3.653020,1.969679,1.182582], dtype = "float64")#candidate|19788|(60,)|const|float64
call_19787 = func_938_call(relay.reshape(const_19788.astype('float64'), [2, 3, 10]))
call_19789 = func_938_call(relay.reshape(const_19788.astype('float64'), [2, 3, 10]))
func_7482_call = mod.get_global_var('func_7482')
func_7485_call = mutated_mod.get_global_var('func_7485')
const_19791 = relay.const([6.093517,-3.002712,-9.032610,-4.958993,-2.252444,-8.941113,0.677667,-5.600477,7.993723,7.763629,1.404714,-0.930752,-2.432486,-2.653525,1.982414,7.105589,-3.339267,6.433233,-9.813069,3.398960,-0.511366,-5.172405,-8.975590,-3.499086,-1.906675,-5.605057,4.094530,-8.432540,5.174624,5.669020,-7.072286,8.780432,4.354214,1.123657,-9.984556,-9.221207,-5.840302,-3.282646,7.512567,-8.026692,-3.959037,8.898223,-4.091096,-1.056445,6.903165,-0.725155,-4.793997,-1.985739,-5.037729,7.511800,-0.432784,0.425822,-0.326483,3.555815,-7.296186,5.010049,-2.266532,-3.406279,-4.250861,1.820050,6.712038,2.864149,9.817281,2.052503,5.286122,9.278980,-8.759006,-7.592498,-8.512032,-3.443663], dtype = "float64")#candidate|19791|(70,)|const|float64
call_19790 = relay.TupleGetItem(func_7482_call(relay.reshape(const_19791.astype('float64'), [5, 2, 7])), 0)
call_19792 = relay.TupleGetItem(func_7485_call(relay.reshape(const_19791.astype('float64'), [5, 2, 7])), 0)
func_10483_call = mod.get_global_var('func_10483')
func_10486_call = mutated_mod.get_global_var('func_10486')
const_19810 = relay.const([8.887843,-7.417269,-6.740099,-3.547731,6.376631,-9.214384,1.832990,-6.060768,-6.267801,0.165466,4.405123,-1.562442,4.165311,-5.549097,0.103913,8.910290,-4.017261,4.177236,-2.143625,9.237427,3.234827,6.935665,-8.840102,7.832557,-3.253692,2.954418,-9.818094,9.234863,-2.958744,-0.664197,-5.601288,-1.044260,-6.961579,1.452156,9.401618,-1.361559,-8.408928,0.393621,8.014101,0.913022,4.601892,-5.004248,5.641170,1.108687,2.158304,5.826614,6.276356,5.898859], dtype = "float32")#candidate|19810|(48,)|const|float32
call_19809 = relay.TupleGetItem(func_10483_call(relay.reshape(const_19810.astype('float32'), [48,])), 5)
call_19811 = relay.TupleGetItem(func_10486_call(relay.reshape(const_19810.astype('float32'), [48,])), 5)
func_14326_call = mod.get_global_var('func_14326')
func_14328_call = mutated_mod.get_global_var('func_14328')
const_19830 = relay.const([-5.068976,-3.337271,-5.086152,5.023208,-1.260136,6.893190,-1.248276,-2.877579,5.733718,-0.466225,0.140383,-0.216153,8.673043,1.341144,8.354789,0.511149,-1.303875,-9.776788,0.246611,-9.710546,-3.049109,-7.126197,5.300286,3.507366,-1.601689,-0.160504,-0.873847,5.834208,-7.736564,2.928393,8.222818,0.299209,-8.650158,-9.212404,2.959461,-2.306318,9.695614,9.736925,6.136597,4.470610,-0.118871,0.442698,1.686027,-9.537626,0.019709,0.999959,9.992529,-4.869785,-8.292184,7.725022,8.448545,-4.203845,-1.208258,3.157702,-9.866497,-9.549561,-0.534402,-1.881549,-9.419151,3.281713,-3.628490,-1.431016,9.745947,4.512985,-3.198010,-4.115857,-5.814486,-9.647959,-0.123038,-7.132074,-2.841284,4.715151,6.522111,-8.323886,7.037013,3.727392,-7.237281,2.271305,9.774230,-2.101083,7.320218,4.594173,0.035506,-8.158670,-5.872071,-9.889554,7.668038,7.391438,9.561554,-6.181109,-0.682862,-8.658616,-9.679541,-3.985231,9.510848,4.207941,8.090669,-0.033437,-6.920035,-6.424516,-3.306960,3.487364,7.135377,-1.123686,7.414657,3.723402,-2.858108,-3.674134,0.019861,-3.415866,6.861871,8.370122,2.643579,1.231445,-4.938185,-3.521188,5.990631,0.786023,-1.770388,5.030057,-8.397781,0.922843,5.187227,9.575061,5.873446,5.697917,5.664947,2.355257,-8.163657,-9.950153,7.900979,1.543801,5.753165,9.669135,-7.137449,7.312291,5.275471,-9.583318,-4.131976,6.210522,8.664104,8.949428,5.131350,6.972022,9.587977,-6.064018,-9.657484,7.759069,-2.760893,-0.717420,-9.963834,-4.776746,-4.991543,-2.757942,-9.688139,-2.921352,-4.439629,0.220804,0.679198,1.649498,-0.219467,6.818115,-5.206959,-7.335087,1.598765,3.557950,-4.680903,4.635789,-2.058769,-6.859888,9.988793,7.775662,-7.721685,6.153610,5.658134,-0.343477,-8.206815,1.901230,6.731853,-1.734674,-2.930141,-6.046131,9.524907,3.319383,4.935769,-5.500325,2.390080,-8.598480,-9.921931,4.475432,-1.667345,-3.908101,9.758137,6.721503,4.910602,0.229903,-0.168317,1.472775,7.811682,6.838931,-2.069075,8.443753,2.872271,1.915205,2.397512,-8.028179,-3.402368,-7.436188,-0.056143,-2.118736,5.682278,6.838119,1.843686,5.702714,4.281506,9.262591,8.964931,5.765562,-4.658005,-4.369587,4.444026,-7.248942,1.259774,8.824831,-1.092026,-0.242809,2.354823,2.385329,-2.645687,3.141724,-7.671153,7.662207,7.016232,-8.833906,2.322565,7.175023,4.505980,-3.558083,7.471227,-1.928790,-9.349095,8.309354,-5.139165,-2.091862,-0.112633,2.560744,6.921603,-7.066771,9.726888,-1.918252,5.544197,-2.181879,8.681063,-3.508725,-4.309392,7.702418,1.617954,1.557309,8.902538,-7.519117,7.879436,-1.936812,-1.462975,-1.846347,-8.784701,-6.345202,-0.362162,-6.380182,0.782634,-1.648931,-8.948782,-6.650717,2.107628,6.406046,-8.896297,-7.319495,4.145171,-0.216631,7.344825,-2.976058,4.817736,6.591425,5.486676,-9.226431,-6.903834,-0.624501,-4.126736,-5.997483,-6.094843,-4.929514,5.965430,8.628733,-3.521844,-3.633699,-5.362718,5.653450,8.713614,1.218340,-5.214977,-4.578558,8.590219,1.692231,9.514030,2.436396,-6.987038,-5.590389,-5.586500,-2.992638,8.506864,-4.624455,4.672246,-8.275660,-1.192374,3.597132,6.038389,-9.285148,9.660366,-0.889847,7.597549,-2.869539,4.488148,-6.387428,-2.419404,-7.767850,1.670295,8.738092,-2.191232,-8.099856,-5.050542,-1.461828,4.288638,-9.775781,-1.583934,5.824972,-3.728737,6.978290,4.210594,2.182572,1.250361,6.780867,-7.538894,7.822007,-7.043499,1.410153,-3.366141,-1.438606,-7.876245,-8.650081,8.045590,5.867576,6.273399,-9.589994,-9.907482,2.264821,1.117076,-3.096347,9.969987,6.503004,6.783117,-8.784156,-1.474574,7.451803,2.440700,0.146069,-6.928309,-4.182612,-7.113868,-4.596427,-3.996129,-0.758041,-5.762870,5.127192,-6.600678,-2.632838,-7.589619,5.304588,1.433544,3.715913,-3.793168,-8.575499,4.896794,8.597326,0.373698,-3.898789,9.768301,2.830428,-2.100959,3.692095,9.960956,-2.967492,4.775607,-5.596971,7.389073,2.679469,0.712566,-2.144532,4.112467,-6.462286,2.178079,-9.754965,3.522899,-3.763000,9.165214,-6.786275,2.265216,-8.263207,3.498174,-8.736914,-5.111663,-0.857028,8.966052,9.937257,-1.029378,8.305516,-4.507404,-9.287108,0.622906,6.774655,0.102736,-8.260056,0.955664,1.157939,3.120635,6.725872,0.698461,1.018972,-6.847457,0.643330,-5.791045,-0.269738,1.519765,-3.360908,9.559944,9.360169,-6.009045,-2.128169,-8.718415,-6.131548,0.473976,0.338545,3.502139,2.488746,9.714583,1.883520,7.885975,5.568379,-7.528971,0.980684,6.425446,-9.861408,-4.849753,3.882629,-4.792828,6.519274,2.492259,9.596135,6.539819,-5.809603,8.682268,8.698254,7.376149,4.728214,-3.024062,-1.002061,2.778544,0.852300,3.767168,-9.898993,-4.042934,0.442038,7.552584,5.624182,7.709979,5.239535,9.881088,1.408048,1.350374,-3.489274,2.990844,-1.687694,-0.673510,6.621154,-7.158927,1.003610,5.716631,2.772801,8.045534,4.241009,-3.049333,-0.897289,5.030989,8.487830,-1.778128,5.565432,-4.811842,7.444545,2.554741,-7.212255,-5.874150,5.865954,-7.455234,-1.160060,0.734976,-2.054366,0.415449,6.977556,-8.703448,0.592828,-5.229047,-8.527057,-6.024340,8.140011,-1.199432,-4.449038,-1.175069,-0.290730,-0.533107,-6.346624,7.012397,4.669377,9.328861,3.733964,0.781427,2.877022,6.683347,-5.676790,5.628595,-1.058328,5.047003,-2.541399,-9.312437,-9.801036,-1.655541,-1.518584,8.353962,-4.345571,-9.180000,-1.838345,-6.040308,0.721678,-1.668758,-6.427364,-0.270997,6.534880,2.260289,9.079232,2.862970,-9.809159,-1.049025,3.450825,-3.964572,9.062942,6.951577,2.646166,2.134698,-3.478661,-2.822676,1.531009,3.506521,6.058508,-7.849024,-2.136893,-5.573402,4.074840,0.248581,0.370028,-5.772677,-2.474806,-9.536594,-4.723451,-9.890278,1.708057,4.420313,2.889493,-7.519029,5.945685,0.863853,-5.911213,-2.860897,6.391773,-5.963870,8.331306,6.992596,-8.121354,6.952300,6.509791,7.110946,3.616292,3.219947,5.931109,6.519292,-2.716718,-3.766672,-0.552518,7.749353,-8.154676,-8.713634,-7.299905,1.592797,-1.655122,1.679617,5.196380,-7.938824,9.264346,7.264728,9.583562,8.388246,-4.930797,-2.048837,-8.017053,-7.237132,3.378520,4.908506,-4.209634,0.109730,8.034301,-3.757960,5.553120,7.304891,-1.955345,-8.093064,0.925581,8.954316,4.133575,4.037944,2.478767,7.584718,-8.342781,3.399834,4.177849,0.336821,0.296929,6.566197,6.797476,-7.226599,-8.320772,8.190335,-7.793876,0.918846,1.999684,-5.188442,-2.701844,0.789826,-2.565908,0.479201,0.924296,-8.734758,-7.051186,-9.641263,7.758028,6.956470,3.656971,8.677468,8.254149,4.408431,3.078241,-2.337875,8.715648,9.468262,-2.698799,-2.949059,4.790291,-5.893275,-5.784385,9.318455,7.673157,8.355215,-6.981996,0.368009,7.828953,-8.317782,-2.247073,-8.364175,-5.669580,4.097885,-5.132477,5.134971,-3.645991,1.466066,-0.653965,-9.830172,2.268398,-5.171494,0.474950,-9.718970,-5.003317,4.053337,8.498717,1.332544,4.487445,-8.258251,-3.106304,-2.867063,9.951911,8.094453,-2.194004,-1.123474,-2.567189,2.622103,-4.308664,-6.756408,-5.019598,1.681181,-2.049520,-4.674444,1.272002,3.004191,-2.395776,-2.880705,-9.471192,1.339271,-7.613798,-9.425951,-7.906323,-1.882545,8.164578,7.692277,-0.652017,3.914304,5.847640,0.433812,-9.199469,-3.971396,-5.530502,0.849792,3.624870,2.725537,-0.321916,-1.879004,-7.942430,5.710175,9.128649,1.158417,1.793119,-4.726494,-6.352208,7.839167,8.603047,8.768119,-9.408606,-3.330739,2.137261,5.940849,7.672527,-6.991542,-4.474774,-7.282478,3.822318,-4.568767,-8.374758,3.909499,-8.001780,-0.085916,0.684695,9.541478,-1.072341,1.611587,8.420339,9.630377,-9.466418,-4.940740,7.313236,-2.308095,4.588307,4.261105,-5.663694,-0.284563,2.478200,-8.758584,5.959655,-8.251387,5.936385,1.584986,1.268305,5.722787,1.554127,-7.347980,-5.884362,2.218207,8.462656,-4.223728,3.254586,-9.350903,7.791074,1.561041,-2.067109,-2.535829,3.986050,1.592257,-0.257191,-5.795340,-4.628076,-0.875721,-4.286684,-1.399066,-0.458711,0.078453,-4.980607,-2.965881,-9.767950,-9.007907,3.774356,-4.295966,-2.377072,9.307373,-1.020986,-0.822849,2.850968,-6.747977,-6.142299,0.989865,5.970908,9.411688,8.462786,8.187983,6.667399,-1.628465,-7.821902,-3.860503,-7.648187,0.944216,0.997493,-6.354785,-6.850747,-7.487611,7.392066,0.481838,-5.373895,-1.017426,-4.611724,8.878916,0.221885,-0.147260,-2.035263,7.035000,6.588903,-4.136946,-9.923840,6.414697,9.979590,-7.762402,1.187904,4.595468,-3.972642,5.673248,9.395222,-8.242945,4.434156,-6.768870,1.256269,-8.100221,-6.578583,-2.004227,9.311161,1.860750,7.502695,-7.981729,2.880318,5.199529,7.534518,-3.366647,0.610457,-8.734223,3.693442,0.408550,-3.422870,7.761742,-4.553018,6.353737,2.389688,-4.154481,-4.122852,-0.033345,-8.025494,9.884281,-7.043532,-3.265385,6.173301,-1.671084,9.958865,8.113368,-8.646762,-5.960204,-2.828196,-8.690611,-3.176442,3.777350,9.338756,-3.919201,3.138117,-8.977002,2.666405,5.214136,2.252254,9.303798,2.205937,-8.581059,-1.165529,-3.268784,-0.894790,-7.478154,1.731978,-9.995614,8.872663,-6.038644,-0.509772,0.876238,8.662041,-8.097185,-2.036979,4.605825,2.338179,6.202314,-9.417840,-6.019430,0.464044,3.845744,-4.294128,0.109507,-8.962064,-7.394882,-3.820286,-3.122785,9.226120,-6.831056,4.518962,7.120789,5.085589,-1.173681,2.969676,1.626630,9.841722,7.805331,-5.755123,-0.576869,9.943824,7.978313,-3.199940,3.570184,9.627556,1.228265,-3.664549,1.830831,-6.456306,3.213351,-0.958445,-2.884358,-8.192024,-1.605268,-4.933179,7.498803,2.282189,-6.587777,5.828070,6.959311,8.707728,0.095760,-2.998637,-1.273003,-9.750638,-0.240568,-5.160525,-4.653171,-2.044148,6.499874,3.406865,-8.254782,7.558510,-3.600152,8.625768,9.211383,3.977474,-7.446220,9.558783,-7.008832,-2.208613,8.119536,3.203865,9.205030,-4.734722,-8.076257,-5.956001,-2.749400,1.664647,-4.271118,3.167314,-5.241193,-2.056298,-0.043908,1.386686,5.560413,2.992017,-3.109211,-4.995083,-9.766234,-0.960577,0.811554,-4.563098,-4.491312,-6.204885,-8.539296,6.761632,-8.854174,3.589227,4.477257,6.644486,-2.680273,0.291581,8.992706,7.495034,-8.455484,7.872542,-1.505024,-4.603634,2.452484,1.187583,-0.135499,-2.649597,-3.671675,5.793912,-3.883519,-4.870432,2.341988,2.934042,7.302449,-2.362878,-8.655268,1.757266,3.694419,-1.808464,8.793501,-9.332414,-7.097371,-0.628970,-4.245128,-7.543933,3.988303,-0.882137,8.430026,8.729516,-2.580482,-4.719874,3.743923,9.032451,0.502207,-1.849529,5.880574,-8.500022,0.611293,-2.701292,-5.293221,0.649926,0.320948,-6.352512,5.185097,4.117815,-9.688889,6.240390,-1.280556,-3.742414,-4.145515,-5.383019,-4.466249,0.057735,5.744910,9.556957,-7.219485,1.227331,-4.211769,-7.273437,-0.965566,5.896467,-0.777340,-1.035614,9.958289,-6.789120,5.983549,3.685831,-8.288445,-1.148737,-9.092213,1.048408,-7.174416,-9.048035,8.859776,-3.724475,4.192389,-8.391859,-3.918196,-1.002487,2.752459,6.551551,7.740372,-9.243308,5.149141,2.100179,3.297049,3.524348,-2.269103,-7.434422,-4.588441,2.795092,7.913686,2.250314,-4.750841,9.390021,7.879900,7.736777,-7.312136,-8.516368,-9.076180,3.941788,-7.176761,5.166561,8.050003,-8.373873,-9.310196,6.306033,3.767185,-0.136108,-8.461626,-6.361551,-3.756169,-6.744577,5.225225,7.839226,-9.820646,2.244055,6.779966,8.507022,6.004159,-4.955194,6.601729,0.212082,0.765142,6.442705,0.732918,6.757009,5.359500,-8.230512,-9.529418,-5.084978,3.685346,5.946467,-7.032171,2.374151,9.166955,1.840561,5.158129,4.557853,-5.014659,-7.087227,-4.205936,-6.174612,5.874886,2.493019,-6.039830,-9.720805,8.734312,-2.315578,2.843941,5.934155,0.805560,5.974050,3.635116,8.366846,6.284277,-4.187080,0.992714,5.381959,2.424448,-4.817034,-9.099266,8.146536,9.057443,2.211764], dtype = "float64")#candidate|19830|(1176,)|const|float64
call_19829 = relay.TupleGetItem(func_14326_call(relay.reshape(const_19830.astype('float64'), [1176,])), 0)
call_19831 = relay.TupleGetItem(func_14328_call(relay.reshape(const_19830.astype('float64'), [1176,])), 0)
output = relay.Tuple([call_19775,call_19787,const_19788,call_19790,const_19791,call_19809,const_19810,call_19829,const_19830,])
output2 = relay.Tuple([call_19776,call_19789,const_19788,call_19792,const_19791,call_19811,const_19810,call_19831,const_19830,])
func_19839 = relay.Function([], output)
mod['func_19839'] = func_19839
mod = relay.transform.InferType()(mod)
mutated_mod['func_19839'] = func_19839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19839_call = mutated_mod.get_global_var('func_19839')
call_19840 = func_19839_call()
output = call_19840
func_19841 = relay.Function([], output)
mutated_mod['func_19841'] = func_19841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9832_call = mod.get_global_var('func_9832')
func_9833_call = mutated_mod.get_global_var('func_9833')
call_19877 = relay.TupleGetItem(func_9832_call(), 0)
call_19878 = relay.TupleGetItem(func_9833_call(), 0)
output = call_19877
output2 = call_19878
func_19887 = relay.Function([], output)
mod['func_19887'] = func_19887
mod = relay.transform.InferType()(mod)
output = func_19887()
func_19888 = relay.Function([], output)
mutated_mod['func_19888'] = func_19888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13260_call = mod.get_global_var('func_13260')
func_13262_call = mutated_mod.get_global_var('func_13262')
call_19894 = relay.TupleGetItem(func_13260_call(), 1)
call_19895 = relay.TupleGetItem(func_13262_call(), 1)
func_19839_call = mod.get_global_var('func_19839')
func_19841_call = mutated_mod.get_global_var('func_19841')
call_19896 = relay.TupleGetItem(func_19839_call(), 6)
call_19897 = relay.TupleGetItem(func_19841_call(), 6)
func_14105_call = mod.get_global_var('func_14105')
func_14106_call = mutated_mod.get_global_var('func_14106')
call_19924 = relay.TupleGetItem(func_14105_call(), 1)
call_19925 = relay.TupleGetItem(func_14106_call(), 1)
output = relay.Tuple([call_19894,call_19896,call_19924,])
output2 = relay.Tuple([call_19895,call_19897,call_19925,])
func_19952 = relay.Function([], output)
mod['func_19952'] = func_19952
mod = relay.transform.InferType()(mod)
mutated_mod['func_19952'] = func_19952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19952_call = mutated_mod.get_global_var('func_19952')
call_19953 = func_19952_call()
output = call_19953
func_19954 = relay.Function([], output)
mutated_mod['func_19954'] = func_19954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_20008 = relay.TupleGetItem(func_7952_call(), 0)
call_20009 = relay.TupleGetItem(func_7954_call(), 0)
uop_20012 = relay.rsqrt(call_20008.astype('float64')) # shape=(10, 7, 8)
uop_20014 = relay.rsqrt(call_20009.astype('float64')) # shape=(10, 7, 8)
func_14546_call = mod.get_global_var('func_14546')
func_14547_call = mutated_mod.get_global_var('func_14547')
call_20019 = relay.TupleGetItem(func_14546_call(), 2)
call_20020 = relay.TupleGetItem(func_14547_call(), 2)
func_18942_call = mod.get_global_var('func_18942')
func_18943_call = mutated_mod.get_global_var('func_18943')
call_20022 = func_18942_call()
call_20023 = func_18942_call()
func_19044_call = mod.get_global_var('func_19044')
func_19045_call = mutated_mod.get_global_var('func_19045')
call_20029 = relay.TupleGetItem(func_19044_call(), 0)
call_20030 = relay.TupleGetItem(func_19045_call(), 0)
func_7952_call = mod.get_global_var('func_7952')
func_7954_call = mutated_mod.get_global_var('func_7954')
call_20039 = relay.TupleGetItem(func_7952_call(), 2)
call_20040 = relay.TupleGetItem(func_7954_call(), 2)
func_12651_call = mod.get_global_var('func_12651')
func_12653_call = mutated_mod.get_global_var('func_12653')
var_20047 = relay.var("var_20047", dtype = "float32", shape = (550,))#candidate|20047|(550,)|var|float32
call_20046 = relay.TupleGetItem(func_12651_call(relay.reshape(var_20047.astype('float32'), [550,])), 2)
call_20048 = relay.TupleGetItem(func_12653_call(relay.reshape(var_20047.astype('float32'), [550,])), 2)
output = relay.Tuple([uop_20012,call_20019,call_20022,call_20029,call_20039,call_20046,var_20047,])
output2 = relay.Tuple([uop_20014,call_20020,call_20023,call_20030,call_20040,call_20048,var_20047,])
func_20049 = relay.Function([var_20047,], output)
mod['func_20049'] = func_20049
mod = relay.transform.InferType()(mod)
mutated_mod['func_20049'] = func_20049
mutated_mod = relay.transform.InferType()(mutated_mod)
var_20050 = relay.var("var_20050", dtype = "float32", shape = (550,))#candidate|20050|(550,)|var|float32
func_20049_call = mutated_mod.get_global_var('func_20049')
call_20051 = func_20049_call(var_20050)
output = call_20051
func_20052 = relay.Function([var_20050], output)
mutated_mod['func_20052'] = func_20052
mutated_mod = relay.transform.InferType()(mutated_mod)
func_18406_call = mod.get_global_var('func_18406')
func_18408_call = mutated_mod.get_global_var('func_18408')
call_20073 = relay.TupleGetItem(func_18406_call(), 1)
call_20074 = relay.TupleGetItem(func_18408_call(), 1)
func_10383_call = mod.get_global_var('func_10383')
func_10384_call = mutated_mod.get_global_var('func_10384')
call_20098 = func_10383_call()
call_20099 = func_10383_call()
func_12204_call = mod.get_global_var('func_12204')
func_12206_call = mutated_mod.get_global_var('func_12206')
const_20101 = relay.const([False,True,False,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,False,True], dtype = "bool")#candidate|20101|(560,)|const|bool
call_20100 = func_12204_call(relay.reshape(const_20101.astype('bool'), [10, 7, 8]))
call_20102 = func_12204_call(relay.reshape(const_20101.astype('bool'), [10, 7, 8]))
uop_20110 = relay.acosh(call_20098.astype('float64')) # shape=(550,)
uop_20112 = relay.acosh(call_20099.astype('float64')) # shape=(550,)
func_19365_call = mod.get_global_var('func_19365')
func_19366_call = mutated_mod.get_global_var('func_19366')
call_20118 = relay.TupleGetItem(func_19365_call(), 0)
call_20119 = relay.TupleGetItem(func_19366_call(), 0)
uop_20120 = relay.tan(uop_20110.astype('float64')) # shape=(550,)
uop_20122 = relay.tan(uop_20112.astype('float64')) # shape=(550,)
func_11566_call = mod.get_global_var('func_11566')
func_11570_call = mutated_mod.get_global_var('func_11570')
const_20126 = relay.const([-5,-1,-8,-10,-7,3,8,6,9,3,-10,4,9,-9], dtype = "uint8")#candidate|20126|(14,)|const|uint8
const_20127 = relay.const([8,-6,4,-8,-7,3,-8,-1,7,6,3,10,-3,9,-1,-5,-6,-2,7,9,6,-1,3,1,-3,7,-2,-5,-5,-9,7,-9,-5,7,10,-5,6,-1,9,8,-8,9,-3,6,-9,6,9,8,6,-5,1,-3,7,7,-3,-9], dtype = "uint8")#candidate|20127|(56,)|const|uint8
call_20125 = relay.TupleGetItem(func_11566_call(relay.reshape(const_20126.astype('uint8'), [1, 1, 14]), relay.reshape(const_20127.astype('uint8'), [4, 1, 14]), ), 0)
call_20128 = relay.TupleGetItem(func_11570_call(relay.reshape(const_20126.astype('uint8'), [1, 1, 14]), relay.reshape(const_20127.astype('uint8'), [4, 1, 14]), ), 0)
func_19198_call = mod.get_global_var('func_19198')
func_19201_call = mutated_mod.get_global_var('func_19201')
const_20132 = relay.const([[-8,9],[-9,-10],[8,-8],[10,2],[4,6],[-6,-9],[-1,3],[-4,3],[6,-10],[2,5],[-8,1],[-10,-7],[-4,-6],[4,-1],[6,5],[1,-2],[9,3],[-1,-1],[1,6],[5,-6],[6,7],[-7,-7],[4,-3],[-9,3],[-4,-9],[-5,6],[4,-7],[-7,6],[-5,5],[5,5],[3,4],[10,10],[-6,-10],[1,8],[2,-4],[8,-2],[5,5],[9,-9],[5,-4],[5,-10],[5,3],[-8,3],[8,-8],[-7,9],[8,-4],[-1,1],[8,-2],[9,3],[2,2],[-1,-1],[-2,7],[-1,-5],[-10,8],[-2,9],[2,3],[3,-7],[-6,-6],[-4,5],[-6,-7],[-9,-8],[9,-2],[2,-3],[3,8],[-3,-1],[-4,5],[-4,3],[-3,8],[3,2],[-1,7],[8,-10],[5,6],[-2,7],[6,3],[-2,-3],[-9,10],[-7,7],[9,-1],[-3,7]], dtype = "int64")#candidate|20132|(78, 2)|const|int64
call_20131 = relay.TupleGetItem(func_19198_call(relay.reshape(const_20132.astype('int64'), [3, 4, 13]), relay.reshape(const_20132.astype('int64'), [3, 4, 13]), ), 1)
call_20133 = relay.TupleGetItem(func_19201_call(relay.reshape(const_20132.astype('int64'), [3, 4, 13]), relay.reshape(const_20132.astype('int64'), [3, 4, 13]), ), 1)
output = relay.Tuple([call_20073,call_20100,const_20101,call_20118,uop_20120,call_20125,const_20126,const_20127,call_20131,const_20132,])
output2 = relay.Tuple([call_20074,call_20102,const_20101,call_20119,uop_20122,call_20128,const_20126,const_20127,call_20133,const_20132,])
func_20135 = relay.Function([], output)
mod['func_20135'] = func_20135
mod = relay.transform.InferType()(mod)
output = func_20135()
func_20136 = relay.Function([], output)
mutated_mod['func_20136'] = func_20136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10330_call = mod.get_global_var('func_10330')
func_10332_call = mutated_mod.get_global_var('func_10332')
call_20174 = relay.TupleGetItem(func_10330_call(), 0)
call_20175 = relay.TupleGetItem(func_10332_call(), 0)
output = call_20174
output2 = call_20175
func_20186 = relay.Function([], output)
mod['func_20186'] = func_20186
mod = relay.transform.InferType()(mod)
mutated_mod['func_20186'] = func_20186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20186_call = mutated_mod.get_global_var('func_20186')
call_20187 = func_20186_call()
output = call_20187
func_20188 = relay.Function([], output)
mutated_mod['func_20188'] = func_20188
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_20209 = func_7731_call()
call_20210 = func_7731_call()
output = call_20209
output2 = call_20210
func_20211 = relay.Function([], output)
mod['func_20211'] = func_20211
mod = relay.transform.InferType()(mod)
output = func_20211()
func_20212 = relay.Function([], output)
mutated_mod['func_20212'] = func_20212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7731_call = mod.get_global_var('func_7731')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_20292 = func_7731_call()
call_20293 = func_7731_call()
output = call_20292
output2 = call_20293
func_20299 = relay.Function([], output)
mod['func_20299'] = func_20299
mod = relay.transform.InferType()(mod)
output = func_20299()
func_20300 = relay.Function([], output)
mutated_mod['func_20300'] = func_20300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_19887_call = mod.get_global_var('func_19887')
func_19888_call = mutated_mod.get_global_var('func_19888')
call_20303 = func_19887_call()
call_20304 = func_19887_call()
func_13057_call = mod.get_global_var('func_13057')
func_13059_call = mutated_mod.get_global_var('func_13059')
call_20340 = relay.TupleGetItem(func_13057_call(), 0)
call_20341 = relay.TupleGetItem(func_13059_call(), 0)
func_16743_call = mod.get_global_var('func_16743')
func_16745_call = mutated_mod.get_global_var('func_16745')
call_20358 = func_16743_call()
call_20359 = func_16743_call()
output = relay.Tuple([call_20303,call_20340,call_20358,])
output2 = relay.Tuple([call_20304,call_20341,call_20359,])
func_20380 = relay.Function([], output)
mod['func_20380'] = func_20380
mod = relay.transform.InferType()(mod)
output = func_20380()
func_20381 = relay.Function([], output)
mutated_mod['func_20381'] = func_20381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8021_call = mod.get_global_var('func_8021')
func_8022_call = mutated_mod.get_global_var('func_8022')
call_20401 = relay.TupleGetItem(func_8021_call(), 0)
call_20402 = relay.TupleGetItem(func_8022_call(), 0)
func_17623_call = mod.get_global_var('func_17623')
func_17624_call = mutated_mod.get_global_var('func_17624')
call_20427 = relay.TupleGetItem(func_17623_call(), 0)
call_20428 = relay.TupleGetItem(func_17624_call(), 0)
output = relay.Tuple([call_20401,call_20427,])
output2 = relay.Tuple([call_20402,call_20428,])
func_20433 = relay.Function([], output)
mod['func_20433'] = func_20433
mod = relay.transform.InferType()(mod)
output = func_20433()
func_20434 = relay.Function([], output)
mutated_mod['func_20434'] = func_20434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14879_call = mod.get_global_var('func_14879')
func_14881_call = mutated_mod.get_global_var('func_14881')
call_20438 = relay.TupleGetItem(func_14879_call(), 3)
call_20439 = relay.TupleGetItem(func_14881_call(), 3)
output = relay.Tuple([call_20438,])
output2 = relay.Tuple([call_20439,])
func_20441 = relay.Function([], output)
mod['func_20441'] = func_20441
mod = relay.transform.InferType()(mod)
mutated_mod['func_20441'] = func_20441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_20441_call = mutated_mod.get_global_var('func_20441')
call_20442 = func_20441_call()
output = call_20442
func_20443 = relay.Function([], output)
mutated_mod['func_20443'] = func_20443
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9475_call = mod.get_global_var('func_9475')
func_9476_call = mutated_mod.get_global_var('func_9476')
call_20510 = relay.TupleGetItem(func_9475_call(), 1)
call_20511 = relay.TupleGetItem(func_9476_call(), 1)
uop_20537 = relay.tan(call_20510.astype('float32')) # shape=(10, 5, 11)
uop_20539 = relay.tan(call_20511.astype('float32')) # shape=(10, 5, 11)
output = uop_20537
output2 = uop_20539
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
	relay.transform.FirstOrderGradient(),
	relay.transform.EliminateCommonSubexpr(),
	relay.transform.MergeCompilerRegions(),
	relay.transform.Inline(),
	relay.transform.LambdaLift(),
	relay.transform.LazyGradientInit(),
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
