import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_138 = relay.var("var_138", dtype = "float32", shape = (8, 7, 13))#candidate|138|(8, 7, 13)|var|float32
uop_139 = relay.atan(var_138.astype('float32')) # shape=(8, 7, 13)
output = relay.Tuple([uop_139,])
output2 = relay.Tuple([uop_139,])
func_141 = relay.Function([var_138,], output)
mod['func_141'] = func_141
mod = relay.transform.InferType()(mod)
var_142 = relay.var("var_142", dtype = "float32", shape = (8, 7, 13))#candidate|142|(8, 7, 13)|var|float32
output = func_141(var_142)
func_143 = relay.Function([var_142], output)
mutated_mod['func_143'] = func_143
mutated_mod = relay.transform.InferType()(mutated_mod)
var_194 = relay.var("var_194", dtype = "int16", shape = (6, 1, 13))#candidate|194|(6, 1, 13)|var|int16
var_195 = relay.var("var_195", dtype = "int16", shape = (6, 7, 13))#candidate|195|(6, 7, 13)|var|int16
bop_196 = relay.multiply(var_194.astype('int16'), var_195.astype('int16')) # shape=(6, 7, 13)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
var_200 = relay.var("var_200", dtype = "float32", shape = (1, 728))#candidate|200|(1, 728)|var|float32
call_199 = relay.TupleGetItem(func_141_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
call_201 = relay.TupleGetItem(func_143_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
call_203 = relay.TupleGetItem(func_141_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
call_204 = relay.TupleGetItem(func_143_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
call_207 = relay.TupleGetItem(func_141_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
call_208 = relay.TupleGetItem(func_143_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
call_212 = relay.TupleGetItem(func_141_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
call_213 = relay.TupleGetItem(func_143_call(relay.reshape(var_200.astype('float32'), [8, 7, 13])), 0)
output = relay.Tuple([bop_196,call_199,var_200,call_203,call_207,call_212,])
output2 = relay.Tuple([bop_196,call_201,var_200,call_204,call_208,call_213,])
func_219 = relay.Function([var_194,var_195,var_200,], output)
mod['func_219'] = func_219
mod = relay.transform.InferType()(mod)
var_220 = relay.var("var_220", dtype = "int16", shape = (6, 1, 13))#candidate|220|(6, 1, 13)|var|int16
var_221 = relay.var("var_221", dtype = "int16", shape = (6, 7, 13))#candidate|221|(6, 7, 13)|var|int16
var_222 = relay.var("var_222", dtype = "float32", shape = (1, 728))#candidate|222|(1, 728)|var|float32
output = func_219(var_220,var_221,var_222,)
func_223 = relay.Function([var_220,var_221,var_222,], output)
mutated_mod['func_223'] = func_223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_344 = relay.var("var_344", dtype = "bool", shape = (1, 2, 16))#candidate|344|(1, 2, 16)|var|bool
var_345 = relay.var("var_345", dtype = "bool", shape = (9, 2, 16))#candidate|345|(9, 2, 16)|var|bool
bop_346 = relay.logical_or(var_344.astype('bool'), var_345.astype('bool')) # shape=(9, 2, 16)
uop_352 = relay.log10(var_344.astype('float32')) # shape=(1, 2, 16)
output = relay.Tuple([bop_346,uop_352,])
output2 = relay.Tuple([bop_346,uop_352,])
func_367 = relay.Function([var_344,var_345,], output)
mod['func_367'] = func_367
mod = relay.transform.InferType()(mod)
mutated_mod['func_367'] = func_367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_367_call = mutated_mod.get_global_var('func_367')
var_369 = relay.var("var_369", dtype = "bool", shape = (1, 2, 16))#candidate|369|(1, 2, 16)|var|bool
var_370 = relay.var("var_370", dtype = "bool", shape = (9, 2, 16))#candidate|370|(9, 2, 16)|var|bool
call_368 = func_367_call(var_369,var_370,)
output = call_368
func_371 = relay.Function([var_369,var_370,], output)
mutated_mod['func_371'] = func_371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_443 = relay.var("var_443", dtype = "float64", shape = (1, 8, 11))#candidate|443|(1, 8, 11)|var|float64
uop_444 = relay.atanh(var_443.astype('float64')) # shape=(1, 8, 11)
var_449 = relay.var("var_449", dtype = "float64", shape = (10, 8, 11))#candidate|449|(10, 8, 11)|var|float64
bop_450 = relay.left_shift(var_443.astype('int8'), var_449.astype('int8')) # shape=(10, 8, 11)
output = relay.Tuple([uop_444,bop_450,])
output2 = relay.Tuple([uop_444,bop_450,])
func_454 = relay.Function([var_443,var_449,], output)
mod['func_454'] = func_454
mod = relay.transform.InferType()(mod)
mutated_mod['func_454'] = func_454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_454_call = mutated_mod.get_global_var('func_454')
var_456 = relay.var("var_456", dtype = "float64", shape = (1, 8, 11))#candidate|456|(1, 8, 11)|var|float64
var_457 = relay.var("var_457", dtype = "float64", shape = (10, 8, 11))#candidate|457|(10, 8, 11)|var|float64
call_455 = func_454_call(var_456,var_457,)
output = call_455
func_458 = relay.Function([var_456,var_457,], output)
mutated_mod['func_458'] = func_458
mutated_mod = relay.transform.InferType()(mutated_mod)
const_923 = relay.const([[[3,9,-5,-9,-1,6,-5,3,-4,-8],[-5,1,-2,10,-1,-2,-4,-2,-10,-1],[9,-4,-6,-6,-10,-1,7,-8,-9,6],[5,-4,-9,-10,-9,-1,10,-5,-4,9],[7,1,-6,-6,-7,4,-10,-1,-7,7],[-3,6,-4,10,-4,-2,-2,7,-1,-2],[-5,10,-7,2,5,-1,8,2,10,7],[-4,7,3,-4,6,5,-2,-9,-8,-2],[2,1,-1,-9,-8,5,7,-10,7,-5],[9,6,-4,2,-6,7,10,-6,-3,-1]],[[5,-5,-9,3,6,-9,-7,-10,-8,5],[9,-1,-9,9,4,-5,8,-3,2,3],[3,6,-6,5,9,7,-1,6,-5,-4],[-4,8,-6,9,7,7,-3,-4,-9,3],[8,-3,-8,10,1,2,10,7,3,5],[9,1,-7,9,3,-2,-1,1,4,-3],[-3,4,7,1,-9,-1,10,-10,-9,3],[-2,5,1,-3,5,-4,2,-2,-9,-10],[-1,7,-5,10,-6,7,9,-1,8,-7],[-1,9,-7,2,-6,-4,-7,8,-6,7]]], dtype = "int32")#candidate|923|(2, 10, 10)|const|int32
var_924 = relay.var("var_924", dtype = "int32", shape = (2, 10, 10))#candidate|924|(2, 10, 10)|var|int32
bop_925 = relay.minimum(const_923.astype('int32'), relay.reshape(var_924.astype('int32'), relay.shape_of(const_923))) # shape=(2, 10, 10)
uop_931 = relay.log2(var_924.astype('float64')) # shape=(2, 10, 10)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
var_950 = relay.var("var_950", dtype = "float32", shape = (728,))#candidate|950|(728,)|var|float32
call_949 = relay.TupleGetItem(func_141_call(relay.reshape(var_950.astype('float32'), [8, 7, 13])), 0)
call_951 = relay.TupleGetItem(func_143_call(relay.reshape(var_950.astype('float32'), [8, 7, 13])), 0)
func_367_call = mod.get_global_var('func_367')
func_371_call = mutated_mod.get_global_var('func_371')
const_960 = relay.const([False,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True], dtype = "bool")#candidate|960|(32,)|const|bool
var_961 = relay.var("var_961", dtype = "bool", shape = (288,))#candidate|961|(288,)|var|bool
call_959 = relay.TupleGetItem(func_367_call(relay.reshape(const_960.astype('bool'), [1, 2, 16]), relay.reshape(var_961.astype('bool'), [9, 2, 16]), ), 1)
call_962 = relay.TupleGetItem(func_371_call(relay.reshape(const_960.astype('bool'), [1, 2, 16]), relay.reshape(var_961.astype('bool'), [9, 2, 16]), ), 1)
func_454_call = mod.get_global_var('func_454')
func_458_call = mutated_mod.get_global_var('func_458')
const_965 = relay.const([1.106496,-8.061209,-8.019280,9.702720,-6.113853,-3.056768,6.891629,2.493838,-2.348453,7.998519,-3.569279,0.573468,-2.382889,-6.434653,-3.502871,-7.576526,7.457878,5.935567,-1.092452,-2.574115,-0.555808,-1.918616,0.086258,-0.509941,4.217211,-2.898333,-7.196287,-1.952446,9.490038,2.862889,1.264593,0.882804,-8.786755,-6.116161,-3.268572,1.877420,0.226205,-4.689303,5.772978,9.471699,-9.950353,8.804682,8.795743,-7.798742,-8.202160,-4.421436,4.952476,-3.447791,-5.317952,5.947863,8.348606,-1.631744,-8.987431,-1.674168,5.236421,-7.421181,7.393722,-0.578255,-7.519921,5.007798,-5.973946,-8.027599,-2.833431,4.303289,0.617215,7.637850,-4.422946,4.673727,-2.516054,-4.228843,0.258235,-1.771924,-7.815508,1.611835,1.123102,0.580938,-3.489386,6.058541,-2.191282,-2.612018,0.855693,2.499206,7.388071,-9.596277,-7.360969,3.399040,-4.775714,-1.601652], dtype = "float64")#candidate|965|(88,)|const|float64
var_966 = relay.var("var_966", dtype = "float64", shape = (880,))#candidate|966|(880,)|var|float64
call_964 = relay.TupleGetItem(func_454_call(relay.reshape(const_965.astype('float64'), [1, 8, 11]), relay.reshape(var_966.astype('float64'), [10, 8, 11]), ), 1)
call_967 = relay.TupleGetItem(func_458_call(relay.reshape(const_965.astype('float64'), [1, 8, 11]), relay.reshape(var_966.astype('float64'), [10, 8, 11]), ), 1)
func_219_call = mod.get_global_var('func_219')
func_223_call = mutated_mod.get_global_var('func_223')
const_969 = relay.const([[5,10,1,-2,-9,3],[-8,2,-8,10,2,4],[-9,-4,-4,9,10,-1],[-9,6,-1,-1,-1,4],[-7,-3,2,3,-6,4],[1,9,3,2,4,-9],[-6,4,7,-7,2,-3],[7,-8,3,5,5,5],[6,9,-7,5,-1,3],[8,-2,9,-7,-1,3],[8,10,-2,1,-4,7],[9,5,2,-9,7,1],[9,6,4,6,7,-5]], dtype = "int16")#candidate|969|(13, 6)|const|int16
var_970 = relay.var("var_970", dtype = "int16", shape = (91, 6))#candidate|970|(91, 6)|var|int16
call_968 = relay.TupleGetItem(func_219_call(relay.reshape(const_969.astype('int16'), [6, 1, 13]), relay.reshape(var_970.astype('int16'), [6, 7, 13]), relay.reshape(call_949.astype('float32'), [1, 728]), ), 1)
call_971 = relay.TupleGetItem(func_223_call(relay.reshape(const_969.astype('int16'), [6, 1, 13]), relay.reshape(var_970.astype('int16'), [6, 7, 13]), relay.reshape(call_949.astype('float32'), [1, 728]), ), 1)
uop_980 = relay.sin(call_959.astype('float32')) # shape=(1, 2, 16)
uop_982 = relay.sin(call_962.astype('float32')) # shape=(1, 2, 16)
output = relay.Tuple([bop_925,uop_931,call_949,var_950,const_960,var_961,call_964,const_965,var_966,call_968,const_969,var_970,uop_980,])
output2 = relay.Tuple([bop_925,uop_931,call_951,var_950,const_960,var_961,call_967,const_965,var_966,call_971,const_969,var_970,uop_982,])
func_986 = relay.Function([var_924,var_950,var_961,var_966,var_970,], output)
mod['func_986'] = func_986
mod = relay.transform.InferType()(mod)
var_987 = relay.var("var_987", dtype = "int32", shape = (2, 10, 10))#candidate|987|(2, 10, 10)|var|int32
var_988 = relay.var("var_988", dtype = "float32", shape = (728,))#candidate|988|(728,)|var|float32
var_989 = relay.var("var_989", dtype = "bool", shape = (288,))#candidate|989|(288,)|var|bool
var_990 = relay.var("var_990", dtype = "float64", shape = (880,))#candidate|990|(880,)|var|float64
var_991 = relay.var("var_991", dtype = "int16", shape = (91, 6))#candidate|991|(91, 6)|var|int16
output = func_986(var_987,var_988,var_989,var_990,var_991,)
func_992 = relay.Function([var_987,var_988,var_989,var_990,var_991,], output)
mutated_mod['func_992'] = func_992
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1061 = relay.var("var_1061", dtype = "uint16", shape = (12, 1, 15))#candidate|1061|(12, 1, 15)|var|uint16
const_1062 = relay.const([[[4,-1,-3,-3,-9,9,7,1,-1,-4,5,-8,9,2,-9],[-9,8,-1,-3,9,9,6,-7,-3,1,9,5,1,-3,3],[9,-6,4,-9,2,-10,6,-8,7,1,-9,6,-10,-10,-9],[-7,-7,-5,-10,9,-2,4,-7,3,4,-3,-6,10,5,-9]],[[3,3,8,-10,-2,-10,-7,4,-7,-9,-1,-7,-3,-3,7],[3,9,-9,-3,7,7,4,4,-2,-7,3,5,-4,-6,-7],[10,-10,-5,8,-9,5,-2,4,9,6,-6,3,-8,-10,-6],[5,6,-7,-8,10,7,5,-6,-5,4,-8,-8,-4,10,1]],[[2,3,5,10,2,1,7,1,7,-8,-5,3,-9,-4,-2],[6,2,1,-1,1,3,5,9,1,1,-7,8,-4,7,-8],[2,3,3,-1,7,10,-5,-7,-10,-10,-10,9,-5,4,8],[2,-4,-4,-9,3,-1,5,7,-10,-10,8,-5,7,8,3]],[[1,-6,10,-4,-8,-4,-2,-3,-1,-6,3,-3,10,2,9],[-6,3,-7,-5,-2,10,10,-9,10,7,-2,-1,3,-3,1],[-10,-4,10,-6,4,6,7,7,10,-5,3,-9,10,-8,-7],[-9,-6,10,6,-3,-5,6,6,8,-1,4,8,-8,7,3]],[[5,-9,-7,-8,-4,-5,1,-10,3,4,-9,-7,2,-7,-3],[3,4,-10,-10,6,-1,-10,10,-9,8,-6,2,5,-1,4],[-3,-2,6,10,10,9,-6,-4,-9,-1,6,3,3,3,10],[-5,-4,-2,1,-6,9,-2,6,-3,-1,-3,4,-7,4,8]],[[-9,9,-4,-4,6,-5,7,1,-5,8,1,-5,7,-1,-5],[-9,5,-8,10,3,-3,-10,-6,-6,7,1,5,-2,-9,7],[5,-10,3,-9,-1,-8,1,-9,-1,1,8,6,7,8,-5],[2,1,8,2,-7,-10,-1,7,9,4,-7,-10,-8,5,3]],[[-10,-7,8,5,5,-5,10,-7,6,6,5,-4,8,-2,-5],[10,1,-6,-5,9,4,-4,-9,-1,6,-7,-3,-6,1,2],[2,-3,1,1,2,-5,-5,-1,1,-1,1,8,9,5,-1],[-7,-10,5,2,7,-8,-10,-3,-7,-7,1,-8,-2,-2,-8]],[[5,-5,10,4,8,5,6,-8,8,-5,-6,3,-5,1,-3],[10,8,10,-9,-9,-10,4,-10,6,10,1,8,-9,10,-2],[-1,-8,10,-5,6,6,8,1,4,4,-9,-9,-8,1,8],[-10,6,6,-9,4,6,-9,-2,2,10,-10,-10,7,7,7]],[[-9,-2,8,10,-2,-1,6,3,-2,6,1,-10,-6,3,5],[9,-9,-9,-3,-4,-7,3,7,-3,-1,3,-6,-4,-2,-8],[-7,10,-1,4,-2,-7,3,2,6,-3,6,-2,2,7,-5],[10,-3,9,-3,-8,-1,-4,6,6,-1,10,6,-10,-10,-2]],[[-3,6,-5,1,-9,-3,-3,5,-2,1,10,3,-3,-4,-1],[7,-9,9,9,-1,7,7,10,-1,-2,6,-6,-8,3,4],[-6,-5,4,-8,3,1,3,4,-9,4,9,-1,-10,-4,1],[-6,-8,2,6,-7,9,-1,-6,-6,9,-6,1,-1,-8,-5]],[[-4,-6,1,-6,-9,-5,3,-3,-10,3,8,-8,-7,-1,6],[2,6,-4,-7,1,7,4,-2,8,5,-1,-9,1,10,8],[9,-7,9,1,6,-10,8,3,-1,3,-10,-9,3,-4,-6],[-10,4,10,-3,-9,-3,-3,5,2,-9,-3,9,-10,4,9]],[[8,-4,9,8,-5,4,-6,-10,5,10,-6,2,5,-2,-6],[8,10,-8,8,-2,1,-2,3,1,-3,-9,-3,6,3,-6],[7,-2,-10,8,4,-2,6,-5,5,6,-8,6,-7,9,8],[-8,-1,-6,3,-10,3,-4,-5,9,-9,-5,1,-6,4,8]]], dtype = "uint16")#candidate|1062|(12, 4, 15)|const|uint16
bop_1063 = relay.maximum(var_1061.astype('uint16'), const_1062.astype('uint16')) # shape=(12, 4, 15)
output = bop_1063
output2 = bop_1063
func_1081 = relay.Function([var_1061,], output)
mod['func_1081'] = func_1081
mod = relay.transform.InferType()(mod)
mutated_mod['func_1081'] = func_1081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1082 = relay.var("var_1082", dtype = "uint16", shape = (12, 1, 15))#candidate|1082|(12, 1, 15)|var|uint16
func_1081_call = mutated_mod.get_global_var('func_1081')
call_1083 = func_1081_call(var_1082)
output = call_1083
func_1084 = relay.Function([var_1082], output)
mutated_mod['func_1084'] = func_1084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1301 = relay.var("var_1301", dtype = "int16", shape = (8, 7, 16))#candidate|1301|(8, 7, 16)|var|int16
var_1302 = relay.var("var_1302", dtype = "int16", shape = (8, 7, 16))#candidate|1302|(8, 7, 16)|var|int16
bop_1303 = relay.minimum(var_1301.astype('int16'), relay.reshape(var_1302.astype('int16'), relay.shape_of(var_1301))) # shape=(8, 7, 16)
output = bop_1303
output2 = bop_1303
func_1306 = relay.Function([var_1301,var_1302,], output)
mod['func_1306'] = func_1306
mod = relay.transform.InferType()(mod)
var_1307 = relay.var("var_1307", dtype = "int16", shape = (8, 7, 16))#candidate|1307|(8, 7, 16)|var|int16
var_1308 = relay.var("var_1308", dtype = "int16", shape = (8, 7, 16))#candidate|1308|(8, 7, 16)|var|int16
output = func_1306(var_1307,var_1308,)
func_1309 = relay.Function([var_1307,var_1308,], output)
mutated_mod['func_1309'] = func_1309
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1321 = relay.const([[[8,5,5,5,-5,-4,2,-9],[-1,-1,-9,-8,-4,-4,6,4],[-1,-1,6,-4,-5,-6,-2,-3],[1,1,-9,-10,4,7,-2,-4],[-9,1,3,8,2,6,2,-7],[3,4,-9,-3,6,2,1,3],[1,7,9,-3,-3,7,8,8],[-3,3,7,-4,-8,-3,2,-10],[1,-10,-5,3,4,1,5,-3],[-2,-2,-2,3,5,-8,-5,-4],[6,-9,7,-8,4,-2,1,-9]],[[4,3,10,-6,4,-3,-2,5],[1,10,-8,10,8,-2,1,-1],[3,-1,-9,-7,2,-10,-7,6],[-1,-7,-3,-2,10,1,3,6],[-5,8,-3,7,-3,4,3,9],[4,-4,2,9,8,-5,1,9],[-6,2,-10,-9,-7,4,-10,-6],[8,5,-6,3,-6,8,-8,5],[-4,7,5,8,8,-4,2,5],[1,-9,6,-2,-10,10,-7,-6],[-4,-4,9,-3,-3,-7,6,-4]],[[-4,4,9,-2,8,9,-9,-6],[-9,3,2,7,2,10,-6,7],[-1,1,8,-9,7,2,4,-10],[10,-3,9,10,1,-3,6,8],[4,-7,3,9,-3,-8,10,-2],[-1,-3,-2,-6,-2,-4,1,-8],[-3,7,9,8,10,-1,-1,-1],[7,-5,-8,5,-9,10,1,5],[3,2,2,5,3,2,-2,-8],[-8,9,-3,-6,3,4,-6,-10],[3,-2,-9,6,-5,-7,1,6]],[[-10,3,-9,-8,9,-6,1,3],[-7,10,1,9,-4,3,-4,3],[5,-7,-7,9,-7,10,-3,1],[-5,8,-6,-4,-5,-4,-7,3],[4,-10,-7,6,6,-9,8,-10],[2,1,-7,10,1,1,2,-3],[5,7,2,5,9,10,-5,-10],[-10,-9,-5,9,5,-3,-5,3],[-10,2,-6,-4,1,4,-4,-7],[5,-1,4,-6,1,8,-6,6],[3,-9,-4,-8,7,-5,8,7]],[[-7,-4,8,2,9,-5,-2,2],[8,-8,4,-1,8,4,-7,9],[-9,7,-5,9,10,1,-5,-9],[6,-9,-3,-5,-4,9,8,-5],[3,4,-2,3,7,6,-1,-6],[10,1,-4,6,-3,-9,-5,8],[8,-9,7,2,10,-5,-3,-9],[-4,8,-7,6,-1,3,-1,7],[4,-10,8,4,-10,-8,-8,7],[7,8,2,-6,-8,3,1,-7],[-4,8,8,1,-9,-2,7,-8]],[[5,-8,9,1,2,-7,4,10],[2,1,7,2,2,-2,-3,3],[6,6,7,3,1,-4,5,-2],[-9,-8,6,2,-4,-7,7,-5],[-3,-8,-8,10,10,-4,-8,-3],[1,3,1,-7,4,-2,-6,-3],[7,9,-2,-5,-3,-9,-5,-7],[-6,-6,-8,2,9,-2,-10,-5],[-4,-2,-3,1,6,-8,4,1],[-6,9,-10,-7,-4,5,1,8],[-2,4,-7,-3,6,-6,-9,-4]]], dtype = "uint32")#candidate|1321|(6, 11, 8)|const|uint32
var_1322 = relay.var("var_1322", dtype = "uint32", shape = (6, 11, 8))#candidate|1322|(6, 11, 8)|var|uint32
bop_1323 = relay.greater_equal(const_1321.astype('bool'), relay.reshape(var_1322.astype('bool'), relay.shape_of(const_1321))) # shape=(6, 11, 8)
uop_1328 = relay.acos(const_1321.astype('float32')) # shape=(6, 11, 8)
output = relay.Tuple([bop_1323,uop_1328,])
output2 = relay.Tuple([bop_1323,uop_1328,])
func_1330 = relay.Function([var_1322,], output)
mod['func_1330'] = func_1330
mod = relay.transform.InferType()(mod)
var_1331 = relay.var("var_1331", dtype = "uint32", shape = (6, 11, 8))#candidate|1331|(6, 11, 8)|var|uint32
output = func_1330(var_1331)
func_1332 = relay.Function([var_1331], output)
mutated_mod['func_1332'] = func_1332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1385 = relay.var("var_1385", dtype = "float32", shape = (8, 6, 6))#candidate|1385|(8, 6, 6)|var|float32
uop_1386 = relay.acosh(var_1385.astype('float32')) # shape=(8, 6, 6)
output = relay.Tuple([uop_1386,])
output2 = relay.Tuple([uop_1386,])
func_1390 = relay.Function([var_1385,], output)
mod['func_1390'] = func_1390
mod = relay.transform.InferType()(mod)
var_1391 = relay.var("var_1391", dtype = "float32", shape = (8, 6, 6))#candidate|1391|(8, 6, 6)|var|float32
output = func_1390(var_1391)
func_1392 = relay.Function([var_1391], output)
mutated_mod['func_1392'] = func_1392
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1478 = relay.var("var_1478", dtype = "bool", shape = (6, 1, 4))#candidate|1478|(6, 1, 4)|var|bool
var_1479 = relay.var("var_1479", dtype = "bool", shape = (6, 15, 4))#candidate|1479|(6, 15, 4)|var|bool
bop_1480 = relay.logical_or(var_1478.astype('bool'), var_1479.astype('bool')) # shape=(6, 15, 4)
output = relay.Tuple([bop_1480,])
output2 = relay.Tuple([bop_1480,])
func_1485 = relay.Function([var_1478,var_1479,], output)
mod['func_1485'] = func_1485
mod = relay.transform.InferType()(mod)
mutated_mod['func_1485'] = func_1485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1485_call = mutated_mod.get_global_var('func_1485')
var_1487 = relay.var("var_1487", dtype = "bool", shape = (6, 1, 4))#candidate|1487|(6, 1, 4)|var|bool
var_1488 = relay.var("var_1488", dtype = "bool", shape = (6, 15, 4))#candidate|1488|(6, 15, 4)|var|bool
call_1486 = func_1485_call(var_1487,var_1488,)
output = call_1486
func_1489 = relay.Function([var_1487,var_1488,], output)
mutated_mod['func_1489'] = func_1489
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1545 = relay.const([[[-6.178634,3.897359,1.661233,8.734755,-2.606707,0.352604,-8.025099,-4.681735,-6.267502,7.934642,-1.999850],[5.099500,2.707288,-0.845976,3.804718,7.176978,-7.979136,5.791060,-6.161837,-8.194415,1.428935,-6.597011]],[[-7.914318,2.947502,-3.194550,2.245053,-8.598428,-9.508058,0.894370,5.959623,1.288417,-6.009556,0.592111],[3.237652,5.348471,-1.450477,7.058293,-1.445204,7.080121,9.401356,-0.626563,-2.691717,7.428730,-8.109570]],[[3.252086,6.053302,8.205971,-0.508260,8.433742,-4.778877,-4.858054,-1.790096,1.049231,2.008933,-3.044767],[-1.808185,-6.506266,8.984434,-9.309188,-8.326152,3.150095,-0.695595,9.252389,9.703238,-7.409421,1.131335]],[[-8.300717,-2.327976,-1.518682,3.555089,-8.116280,6.675990,-4.924785,-1.502411,2.670597,7.533329,6.755147],[5.595501,-8.410501,6.166671,-9.529490,8.893508,-8.140843,3.975064,-7.642365,8.574707,-7.506127,0.165684]],[[-9.741222,4.975723,-4.082530,-7.119508,-9.801840,-7.236212,8.510071,9.251476,3.939734,-3.809185,9.372447],[-5.477397,-1.850944,-5.922806,0.546110,-8.656847,-3.907948,8.051802,-0.086109,-7.743388,2.840052,9.669559]],[[-4.699733,-5.819269,-3.972517,-6.570868,-7.598818,7.204184,-6.770616,-1.066078,1.353278,0.595196,-8.975845],[-9.705377,0.776159,-6.845679,5.188923,6.564545,-3.490337,0.410059,-5.667798,-7.394958,2.760825,-6.135109]],[[-1.930602,4.137423,2.621656,4.431870,5.825248,-3.168086,-1.705342,9.421883,-3.823397,7.332351,-4.893472],[2.815378,-0.908603,-2.275112,6.530002,-0.059773,4.092412,2.869666,-6.127479,-3.880729,-8.888385,-7.260943]],[[5.192542,0.220505,-3.143478,7.352736,9.559316,-1.500966,-0.037970,8.831371,9.215567,6.340898,8.494320],[3.682058,0.306242,7.243926,-6.033690,-3.630042,7.140581,6.551468,2.754754,8.660257,-6.298164,-2.018877]],[[-6.402231,-3.495002,7.159017,-1.911065,8.424105,0.406486,6.993104,-2.594746,-5.275893,-8.399834,-9.682008],[-0.545189,-1.584240,2.343433,8.506696,2.076203,2.132579,3.454401,-1.294227,-2.744215,1.349593,-5.452805]],[[-4.384456,-9.312284,-3.399812,5.650904,-4.654138,-6.623477,5.470364,1.815595,6.470376,-5.431200,6.987163],[-0.946446,8.821142,6.419155,-2.298600,3.194089,-1.653905,8.478449,-8.453632,-1.754518,-3.375410,7.226842]],[[-0.833379,-8.599574,-5.653115,-2.982128,-5.853035,6.794708,5.651495,-3.730684,-6.399757,5.297267,0.009348],[0.920839,5.276807,4.927826,-5.815464,6.804389,3.434100,3.229121,-8.216093,8.124973,-2.872489,-1.563323]]], dtype = "float32")#candidate|1545|(11, 2, 11)|const|float32
uop_1546 = relay.log10(const_1545.astype('float32')) # shape=(11, 2, 11)
output = uop_1546
output2 = uop_1546
func_1561 = relay.Function([], output)
mod['func_1561'] = func_1561
mod = relay.transform.InferType()(mod)
mutated_mod['func_1561'] = func_1561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mutated_mod.get_global_var('func_1561')
call_1562 = func_1561_call()
output = call_1562
func_1563 = relay.Function([], output)
mutated_mod['func_1563'] = func_1563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_1582 = func_1561_call()
call_1583 = func_1561_call()
output = relay.Tuple([call_1582,])
output2 = relay.Tuple([call_1583,])
func_1590 = relay.Function([], output)
mod['func_1590'] = func_1590
mod = relay.transform.InferType()(mod)
mutated_mod['func_1590'] = func_1590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mutated_mod.get_global_var('func_1590')
call_1591 = func_1590_call()
output = call_1591
func_1592 = relay.Function([], output)
mutated_mod['func_1592'] = func_1592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_1611 = relay.TupleGetItem(func_1590_call(), 0)
call_1612 = relay.TupleGetItem(func_1592_call(), 0)
output = call_1611
output2 = call_1612
func_1620 = relay.Function([], output)
mod['func_1620'] = func_1620
mod = relay.transform.InferType()(mod)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mutated_mod.get_global_var('func_1620')
call_1621 = func_1620_call()
output = call_1621
func_1622 = relay.Function([], output)
mutated_mod['func_1622'] = func_1622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_1643 = relay.TupleGetItem(func_1590_call(), 0)
call_1644 = relay.TupleGetItem(func_1592_call(), 0)
output = call_1643
output2 = call_1644
func_1655 = relay.Function([], output)
mod['func_1655'] = func_1655
mod = relay.transform.InferType()(mod)
output = func_1655()
func_1656 = relay.Function([], output)
mutated_mod['func_1656'] = func_1656
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1757 = relay.const([[[-8.294530,-6.434966],[-0.483997,6.959628]],[[3.437061,-1.931429],[6.880791,6.759303]],[[0.096950,2.285836],[1.135151,-7.595740]],[[-8.790677,7.319463],[-4.350100,-4.776902]],[[-4.108610,9.318773],[0.939113,-6.334304]],[[2.233479,-7.675017],[5.298108,-6.347992]],[[5.233535,-6.782943],[1.089945,9.990425]],[[7.822638,-4.080842],[1.593940,-6.835126]],[[4.689446,3.306720],[-9.845270,-1.749321]],[[-9.743688,9.440212],[-1.619945,-3.000401]],[[9.394935,1.853876],[0.468137,2.032106]],[[9.740408,7.353302],[-0.619437,-0.134445]]], dtype = "float32")#candidate|1757|(12, 2, 2)|const|float32
uop_1758 = relay.exp(const_1757.astype('float32')) # shape=(12, 2, 2)
bop_1760 = relay.multiply(uop_1758.astype('int8'), relay.reshape(const_1757.astype('int8'), relay.shape_of(uop_1758))) # shape=(12, 2, 2)
func_1306_call = mod.get_global_var('func_1306')
func_1309_call = mutated_mod.get_global_var('func_1309')
var_1768 = relay.var("var_1768", dtype = "int16", shape = (896,))#candidate|1768|(896,)|var|int16
call_1767 = func_1306_call(relay.reshape(var_1768.astype('int16'), [8, 7, 16]), relay.reshape(var_1768.astype('int16'), [8, 7, 16]), )
call_1769 = func_1306_call(relay.reshape(var_1768.astype('int16'), [8, 7, 16]), relay.reshape(var_1768.astype('int16'), [8, 7, 16]), )
bop_1782 = relay.right_shift(const_1757.astype('int16'), relay.reshape(bop_1760.astype('int16'), relay.shape_of(const_1757))) # shape=(12, 2, 2)
uop_1785 = relay.cos(uop_1758.astype('float64')) # shape=(12, 2, 2)
output = relay.Tuple([call_1767,var_1768,bop_1782,uop_1785,])
output2 = relay.Tuple([call_1769,var_1768,bop_1782,uop_1785,])
func_1788 = relay.Function([var_1768,], output)
mod['func_1788'] = func_1788
mod = relay.transform.InferType()(mod)
var_1789 = relay.var("var_1789", dtype = "int16", shape = (896,))#candidate|1789|(896,)|var|int16
output = func_1788(var_1789)
func_1790 = relay.Function([var_1789], output)
mutated_mod['func_1790'] = func_1790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1655_call = mod.get_global_var('func_1655')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_1797 = func_1655_call()
call_1798 = func_1655_call()
var_1800 = relay.var("var_1800", dtype = "float32", shape = (11, 2, 11))#candidate|1800|(11, 2, 11)|var|float32
bop_1801 = relay.minimum(call_1797.astype('float64'), relay.reshape(var_1800.astype('float64'), relay.shape_of(call_1797))) # shape=(11, 2, 11)
bop_1804 = relay.minimum(call_1798.astype('float64'), relay.reshape(var_1800.astype('float64'), relay.shape_of(call_1798))) # shape=(11, 2, 11)
const_1808 = relay.const([[[6.385539,-1.225176,5.460206,9.018247,5.952826,5.738303,-8.348284,1.871328,-0.608583,-6.221526,9.379216],[-3.561901,-6.420492,-2.098285,3.705872,8.361315,-6.065981,-3.932793,-8.596999,-4.973018,-8.854351,2.912938]],[[2.288120,-1.520929,7.079589,7.842482,-5.697043,1.511167,3.872070,3.245551,-0.403365,2.095636,0.436054],[-3.495888,-7.135186,3.572669,-5.318826,4.081113,8.615773,-4.126511,-5.235535,-5.657150,3.129925,5.693111]],[[4.893219,1.435515,-6.204465,-0.881775,-8.909849,9.074209,3.795065,2.570441,-0.184877,-3.193091,-2.384704],[-6.183560,-8.210996,2.123521,-1.225128,-1.283587,-3.080532,5.698736,8.028377,-5.883655,5.296938,-5.727882]],[[-1.641179,-9.838960,-7.077048,4.048847,0.105172,0.561520,-6.659132,9.225103,-1.931904,-6.279775,-0.868881],[1.425164,3.819939,9.334281,2.547004,4.007279,-2.582271,-0.412565,-8.656938,8.240348,6.211772,3.468004]],[[-3.076007,1.350775,8.873464,2.042394,8.703265,3.460108,-9.607100,1.284970,-0.674937,6.908477,7.637483],[1.668550,0.743732,7.271800,1.390053,-4.930880,-9.874023,-2.906369,3.808149,8.457470,-7.420953,1.706869]],[[1.554961,8.966098,-6.163220,-7.509126,-4.747112,4.340959,4.410292,2.349666,-8.590218,-3.308873,6.549241],[-1.632308,-4.099099,2.160905,-3.865615,6.300899,-9.570149,2.014229,9.559491,-6.516473,4.922948,-1.852849]],[[-3.881783,2.128105,4.851314,2.000239,6.451524,-1.233875,9.297781,-9.191067,-7.894536,-4.300522,-7.905330],[9.026772,4.754059,-3.348346,-5.340688,9.877375,-6.329115,0.961676,-2.800502,-4.066119,-6.255292,0.446040]],[[-3.599247,6.982980,3.117142,1.292717,1.670797,-4.509342,-5.328201,2.160354,7.632416,-8.234004,6.810846],[1.830991,-8.601429,3.564162,-5.292597,3.594520,8.639802,-0.201819,-3.663846,-8.053219,-3.316724,-8.315268]],[[6.207396,1.465391,2.298839,-5.259292,8.729657,-4.385454,4.281498,-5.916189,1.660929,7.076686,-8.623007],[8.653698,2.269214,-8.751619,-5.659964,8.245173,-8.931459,-6.990543,-2.008940,1.255532,0.719984,5.238424]],[[5.792703,-3.234088,8.505972,5.039731,8.201009,-2.741367,5.358498,9.585399,-1.060948,1.433898,8.058967],[-3.856256,1.357970,-4.977601,3.192193,3.796465,5.834564,1.290169,2.061838,9.918364,-8.052973,-5.726283]],[[-6.730678,1.784284,-6.679552,-0.317012,0.648335,7.615300,-5.308687,1.782035,7.609494,-0.754171,-0.512077],[-7.433374,0.291385,2.345249,7.046547,4.239080,6.054152,-8.129687,6.897810,0.548142,2.300980,9.663296]]], dtype = "float32")#candidate|1808|(11, 2, 11)|const|float32
bop_1809 = relay.logical_or(var_1800.astype('bool'), relay.reshape(const_1808.astype('bool'), relay.shape_of(var_1800))) # shape=(11, 2, 11)
bop_1814 = relay.multiply(call_1797.astype('int64'), relay.reshape(var_1800.astype('int64'), relay.shape_of(call_1797))) # shape=(11, 2, 11)
bop_1817 = relay.multiply(call_1798.astype('int64'), relay.reshape(var_1800.astype('int64'), relay.shape_of(call_1798))) # shape=(11, 2, 11)
output = relay.Tuple([bop_1801,bop_1809,bop_1814,])
output2 = relay.Tuple([bop_1804,bop_1809,bop_1817,])
func_1819 = relay.Function([var_1800,], output)
mod['func_1819'] = func_1819
mod = relay.transform.InferType()(mod)
mutated_mod['func_1819'] = func_1819
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1820 = relay.var("var_1820", dtype = "float32", shape = (11, 2, 11))#candidate|1820|(11, 2, 11)|var|float32
func_1819_call = mutated_mod.get_global_var('func_1819')
call_1821 = func_1819_call(var_1820)
output = call_1821
func_1822 = relay.Function([var_1820], output)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1829 = relay.var("var_1829", dtype = "float32", shape = (5, 13, 2))#candidate|1829|(5, 13, 2)|var|float32
uop_1830 = relay.cosh(var_1829.astype('float32')) # shape=(5, 13, 2)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_1846 = relay.const([-6,10,-4,3,-3,4,8,9,-2,8,2,-9,-6,1,-8,1,-5,7,4,-3,-4,3,4,9,4,1,-3,-8,9,-1,6,-4,-5,-2,-2,5,4,8,-9,-6,-4,-3,-7,6,-2,4,10,-1,-8,5,-8,6,8,1,-10,-2,-6,-1,-6,9,-5,8,-1,-2,3,-1,-8,2,10,3,10,4,10,9,4,4,2,-7,-2,-4,-6,8,1,-10,-3,10,-8,-1,2,4,9,5,1,-6,9,-10,6,-9,-7,-7,1,8,-2,8,1,9,-10,-5,6,-6,3,2,-3,6,9,2,3,-1,-1,10,-1,-5,-3,3,-10,-4,4,-2,-6,-9,-4,-7,1,1,-7,5,9,-8,-8,2,10,3,-2,3,3,-5,2,-3,7,6,-6,1,-1,-8,2,9,5,-7,6,7,3,8,3,8,-7,6,-5,7,-8,7,4,-3,7,-6,-2,-4,-4,-10,-4,-6,3,2,-9,-6,-5,-6,-6,-10,8,7,10,5,-4,10,3,6,-8,-4,9,-5,-2,7,-9,-2,-4,9,10,7,-10,9,5,-9,-6,-1,4,1,-6,-3,-5,3,4,3,-7,10,-7,1,6,4,-3,-9,2,3,10,6,1,-5,3,-10,10,10,-1,-9,10,-1,2,-10,-1,4,-8,-9,10,-5,3,3,-5,1,3,3,5,6,3,2,8,-5,6,5,-9,-9,6,-4,-7,9,4,1,5,9,-3,3,-8,-8,-4,10,-1,-4,3,8,-4,7,-8,-9,6,-2,-8,-10,5,3,-1,1,-2,-7,-6,4,-3,-7,-1,-3,-6,-8,1,-3,6,-6,-8,8,-3,-6,1,8,-3,4,-5,1,-3,-6,-6,1,-4,10,-3,4,3,-6,2,-10,-2,8,-1,-7,-7,9,5,-9,6,-2,8,-8,8,7,1,-4,10,-8,-1,5,1,5,-5,-4,-4,3,-4,2,6,-1,-7,-8,7,9,-5,9,-10,2,9,-8,4,-4,2,-10,7,3,-8,-10,9,4,4,1,-8,-1,3,-1,-3,-7,2,3,-1,-3,1,4,3,-5,-1,-2,1,5,5,1,2,-4,5,4,-6,-5,-10,-9,8,9,10,8,7,5,1,1,-4,-8,4,7,8,-9,2,1,-9,7,6,-3,1,6,-6,5,-3,10,-6,-7,8,5,1,-10,-8,4,-4,-6,6,7,10,1,7,-1,10,-9,4,-10,10,7,-7,-2,7,6,-10,3,-4,-3,8,6,-2,6,-1,-10,6,-10,8,6,10,7,4,1,-6,3,-10,2,5,7,4,-8,-5,-5,-10,6,-4,3,-3,-8,-1,-5,-9,5,4,-2,9,1,8,-7,-9,-10,8,-1,-10,-1,1,3,2,-5,-8,-7,5,-3,7,1,4,9], dtype = "uint32")#candidate|1846|(528,)|const|uint32
call_1845 = relay.TupleGetItem(func_1330_call(relay.reshape(const_1846.astype('uint32'), [6, 11, 8])), 0)
call_1847 = relay.TupleGetItem(func_1332_call(relay.reshape(const_1846.astype('uint32'), [6, 11, 8])), 0)
bop_1850 = relay.floor_divide(uop_1830.astype('float64'), relay.reshape(var_1829.astype('float64'), relay.shape_of(uop_1830))) # shape=(5, 13, 2)
func_219_call = mod.get_global_var('func_219')
func_223_call = mutated_mod.get_global_var('func_223')
var_1863 = relay.var("var_1863", dtype = "int16", shape = (78,))#candidate|1863|(78,)|var|int16
const_1864 = relay.const([[5,4,5,10,4,3,-10,-3,4,7,1,5,9,6,3,-3,5,2,9,-5,-2,8,-7,2,-4,-3,-2,-2,4,3,9,6,5,6,-9,-5,-1,-6,6,8,-6,-5,-1,1,7,1,-2,-2,6,-9,10,8,6,10,2,2,-8,8,5,5,3,-8,4,10,-9,-4,2,10,8,2,7,9,2,-7,5,7,-9,-3,-4,-2,1,-1,10,10,3,-9,7,-8,-5,6,-6,-10,-7,-5,-5,5,2,8,9,-9,2,-3,-4,-8,5,-1,-8,-3,3,7,6,5,-9,-8,-4,5,5,-7,-10,-9,10,5,10,-2,-7,-4,-2,-10,5,3,5,7,5,-8,-10,9,7,-9,-3,4,1,-4,-7,6,-2,-1,-5,8,2,-5,5,2,8,-10,2,1,-2,-6,9,10,9,2,-10,5,8,-4,-4,8,-8,2,-2,3,10,-4,-9,4,-8,3,-9,-9,8,2,10,3,8,-7,-10,6,-10,-1,-7,-9,3,4,-10,-9,-6,8,2,-5,-7,-3,-3,-9,1,3,4,2,4,9,9,-2,-10,-3,4,-3,10,-9,6,7,-7,7,10,1,7,8,10,3,2,2,-3,8,2,-8,7,-10,-4,10,-8,10,2,1,9,4,1,-9,1,-10,7,5,-1,-2,4,1,-4,-7,-10,-10,4,10,8,-2,9,5,-9,-1,7,-7,5,3,8,6,10,-7,-10,2,8,-8,-7,4,5,-8,1,5,5,5,-8,3,9,-6,9,-6,3,6,10,8,9,10,-3,-8,-3,-4,-6,-10,-7,5,-6,2,8,1,-10,-3,-5,9,-8,-10,1,-3,-3,3,1,5,-10,7,7,-4,-7,5,2,3,2,2,-7,10,1,-9,3,2,-3,9,-8,-6,-2,8,7,-5,-5,2,-5,2,-6,-10,5,2,2,-7,-6,7,5,3,7,3,-4,-3,-7,-5,-4,-4,9,-6,-7,3,-7,3,-8,-8,-2,-6,-7,-7,4,9,-9,8,1,8,10,-3,-4,10,1,-4,10,3,-10,2,-4,-3,-6,-8,-6,6,8,2,-6,-1,-4,-1,-8,2,7,-2,-6,2,6,10,-6,8,8,5,6,-10,-4,5,-7,10,10,3,-6,8,4,-6,8,4,5,7,-9,2,-2,-5,-1,-3,6,-6,2,4,6,8,-3,-8,-4,-2,6,8,10,-6,-8,-5,-8,5,-7,-8,1,6,8,6,1,-9,-3,-4,10,-7,1,-1,3,1,-8,-2,4,-3,-2,-8,-7,9,-2,3,2,-10,-2,-4,-8,-2,5,-5,3,-3,7,7,6,5,8,-2,10,5,-5,-4,5,9,-1,9,2,-9,3,6,2,9,-1,-2,7,10,6,4,1,1,8,8,-4,-3,-2,6,10,6,8,-2,-3,6,-8,3,4,1,-6,5,5,6,-9,-1]], dtype = "int16")#candidate|1864|(1, 546)|const|int16
var_1865 = relay.var("var_1865", dtype = "float32", shape = (728, 1))#candidate|1865|(728, 1)|var|float32
call_1862 = relay.TupleGetItem(func_219_call(relay.reshape(var_1863.astype('int16'), [6, 1, 13]), relay.reshape(const_1864.astype('int16'), [6, 7, 13]), relay.reshape(var_1865.astype('float32'), [1, 728]), ), 4)
call_1866 = relay.TupleGetItem(func_223_call(relay.reshape(var_1863.astype('int16'), [6, 1, 13]), relay.reshape(const_1864.astype('int16'), [6, 7, 13]), relay.reshape(var_1865.astype('float32'), [1, 728]), ), 4)
output = relay.Tuple([call_1845,const_1846,bop_1850,call_1862,var_1863,const_1864,var_1865,])
output2 = relay.Tuple([call_1847,const_1846,bop_1850,call_1866,var_1863,const_1864,var_1865,])
func_1870 = relay.Function([var_1829,var_1863,var_1865,], output)
mod['func_1870'] = func_1870
mod = relay.transform.InferType()(mod)
var_1871 = relay.var("var_1871", dtype = "float32", shape = (5, 13, 2))#candidate|1871|(5, 13, 2)|var|float32
var_1872 = relay.var("var_1872", dtype = "int16", shape = (78,))#candidate|1872|(78,)|var|int16
var_1873 = relay.var("var_1873", dtype = "float32", shape = (728, 1))#candidate|1873|(728, 1)|var|float32
output = func_1870(var_1871,var_1872,var_1873,)
func_1874 = relay.Function([var_1871,var_1872,var_1873,], output)
mutated_mod['func_1874'] = func_1874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_1876 = func_1620_call()
call_1877 = func_1620_call()
func_454_call = mod.get_global_var('func_454')
func_458_call = mutated_mod.get_global_var('func_458')
const_1879 = relay.const([1.592026,9.951036,8.666991,-5.668207,2.534364,-7.788406,1.428826,3.988788,1.135058,6.842507,6.058672,9.899105,-2.285908,-3.178540,9.258714,5.278071,-2.133413,-0.704536,-3.699728,3.446869,-5.598905,-3.189708,6.185380,-6.856178,-1.486445,2.197763,-8.313052,-2.773479,3.373849,-8.405443,1.784351,3.483751,-3.091305,6.385240,2.525619,-6.655075,-9.810056,4.167606,-4.993604,2.110999,9.272356,1.334523,7.816681,-0.428989,-9.196279,0.807143,-6.408279,6.360885,8.172730,-3.816839,-6.254381,-8.367418,9.049530,-6.949151,2.553272,-7.417773,9.987133,-4.678735,1.897115,9.727370,5.521564,5.873975,7.757453,7.940986,0.520982,1.097823,-0.883164,3.665333,0.766894,-7.115785,2.680668,1.124957,-5.868890,0.928206,5.132561,1.709165,-7.244222,-3.819756,2.568457,-0.388620,5.172909,-2.550480,7.591971,9.105246,-3.315455,-6.036129,-4.805658,-3.388911], dtype = "float64")#candidate|1879|(88,)|const|float64
const_1880 = relay.const([-5.668182,-6.993609,3.034126,-9.977941,-5.356882,-2.957878,1.612208,8.785269,-1.857765,2.028441,-2.068443,-0.532873,-3.753099,1.797616,-7.137343,-9.552363,2.367252,3.793573,6.798240,-3.206629,-7.447878,-6.252822,5.546701,1.616996,-5.022659,-8.932380,-1.635600,-6.706351,7.313325,-6.472349,-8.459358,-4.936596,6.835154,-0.444904,-3.476509,-9.134833,7.974057,-2.355805,0.450274,-0.705043,-6.434571,-8.005149,2.379542,6.022697,7.373781,1.017052,-3.616883,7.992162,9.275637,2.564414,-7.887447,3.571111,-4.020067,9.631019,3.519235,0.725776,-8.335871,-2.936749,-3.055675,7.429023,1.901495,2.328915,-0.298428,-6.698385,1.027915,2.915228,7.158624,1.352625,-4.904470,4.497720,4.162672,-9.729148,0.402698,0.906199,-9.178921,8.325070,3.766398,-6.568037,0.781926,-7.322412,-1.234077,7.120148,-4.735213,9.861839,9.663790,-6.727199,0.846799,-1.513755,0.496489,6.564119,-9.906620,9.558012,5.608373,-0.160816,-0.049250,3.811300,-1.617117,0.538233,-8.777112,-8.354227,7.324430,-2.419565,6.265891,3.649351,-6.129473,-3.727423,6.646168,9.109420,3.866547,-5.006987,-0.516887,-5.024861,-3.578040,8.015495,-5.651391,-1.861310,-4.337388,2.540824,2.426070,-1.877788,6.910242,6.633835,-0.619167,8.921167,-8.260187,-8.681338,-5.643116,3.466854,-1.414047,7.206982,-4.030485,-7.016573,-0.290764,-6.494260,1.381993,6.091587,-9.281994,7.178645,9.557924,-8.509102,-0.782770,-2.897336,-7.483935,3.294089,-5.450967,5.399383,-0.546427,2.406218,3.238972,3.459476,-6.012420,0.243568,4.109697,-9.809312,-7.095577,-8.562032,7.891329,7.909278,-1.547765,-5.943387,4.958933,-4.056829,1.659389,-4.449149,5.237497,9.754538,-7.944350,-7.491396,-1.724284,4.585100,-4.403120,9.554799,-9.367739,6.517480,-8.924019,-0.943435,0.867719,3.423366,-4.196156,-3.331093,7.495604,-1.895514,-6.121287,9.029041,4.471647,1.777130,-4.933340,2.183349,8.862316,-9.139160,-6.939267,2.830424,5.716834,-0.695994,-8.253076,7.830795,4.516359,-3.994066,9.681273,-1.121719,-4.325236,-9.568266,-6.453174,6.545805,-6.007136,5.083532,-6.097614,-0.631694,-8.641048,-3.441155,8.821378,-7.380643,4.349806,2.596047,6.736759,7.368105,1.781734,-2.370019,8.665935,-0.329474,1.838485,-6.498940,-4.164275,1.250401,1.131494,-4.734843,-9.712842,0.040184,8.733729,-9.029838,-1.413108,-3.985140,2.536646,-4.433934,-2.582600,-1.113887,-0.222746,-1.519910,5.148055,8.183722,8.635900,-8.043443,7.927518,4.985209,-8.411511,2.017817,0.286512,-8.619307,-3.768929,7.618132,3.814176,8.295394,-6.200597,9.023946,7.622733,-8.891301,-5.146206,-4.008991,4.548862,-2.782369,7.586761,-7.137186,1.210395,1.667972,8.790446,-1.999476,-0.861179,8.827177,5.383366,4.994140,9.472557,3.416556,-5.935356,4.318521,2.726375,4.163773,9.109566,0.221694,-2.551824,0.717277,1.304841,8.377179,5.158143,-7.885695,9.186344,8.847500,-2.477881,-9.511947,6.355286,-3.214027,2.697137,4.899683,1.435241,6.400630,-5.383699,-6.686949,-7.819780,4.665059,-0.557666,2.668863,4.249270,-6.104469,0.798863,-4.132964,3.887315,-6.060148,-7.517948,2.319607,-2.965963,-0.939325,3.754429,1.592109,-8.907466,3.986172,-6.535498,-4.657453,-1.981660,9.168845,3.028819,-8.600848,-8.222285,5.646592,-0.228032,7.040931,4.766022,8.809234,-2.099483,-9.910660,-9.238570,4.828170,-1.042291,-0.263250,-1.582441,9.847817,-0.193311,-5.889975,-9.972114,6.082606,0.609770,9.146935,-7.748134,3.288119,8.943265,6.891402,-9.902620,9.293359,-2.017505,1.190924,6.530182,-7.782714,-2.002282,7.186726,-3.052389,1.765668,3.299376,-0.576968,-1.737947,-5.529213,-4.827294,3.537418,-5.893691,2.075608,-9.212788,0.817244,1.848955,9.629905,7.639035,-4.387208,-3.597129,7.738656,5.911905,3.784250,4.698531,8.026604,-8.249777,-2.182476,9.454414,0.632580,-5.765677,-5.659189,6.765905,9.089694,-9.715694,-7.693728,-1.009276,-3.342092,-7.532185,2.323148,6.629817,2.125604,8.936414,-8.966487,8.090616,-8.130606,-6.776971,-4.632003,6.625220,-1.680811,9.434444,-7.068897,-7.102367,8.392176,-6.786461,3.097328,-3.047094,2.463651,-6.660267,-6.763788,-9.382747,-0.747431,8.300585,-1.624876,-8.853512,-5.325587,5.718766,1.341985,3.161367,-9.687015,9.219160,4.133288,-8.611677,1.504006,-5.366482,3.703639,8.554687,-0.636591,-2.056138,6.865201,5.835027,-3.687781,-1.603471,3.834679,8.920251,4.183040,5.316778,-0.992124,-4.227222,-4.087476,9.479089,2.657743,1.317137,-8.026092,-3.276068,2.028818,7.248321,-0.765415,6.599515,-9.309909,-3.876550,-1.021826,-5.333497,1.712782,-6.785323,-3.128158,4.811830,-9.074377,8.120443,-9.248024,-9.219567,8.756147,-8.434973,6.326354,9.294574,-4.231551,-5.561559,6.939871,2.585644,6.239142,9.079878,5.096942,0.221999,0.586211,-3.588707,-8.905432,0.187373,8.734769,3.959917,-1.001525,-4.263355,-4.611166,3.316757,2.590319,1.407392,-0.513162,-4.975046,4.258008,-6.252691,-1.587465,4.659164,6.243708,9.973751,-2.903020,-2.714545,0.034005,7.438530,9.309521,-4.392152,4.986738,5.271938,-2.750146,3.994995,9.680458,-9.203999,0.054681,-2.060993,4.378417,8.691870,-4.718161,-3.787237,-6.856243,-5.449997,-4.371627,-5.721479,-6.169299,2.182170,-6.387227,-7.575185,-6.491992,4.584139,-6.365090,6.339707,2.086106,1.867684,-4.658547,-0.446054,6.300201,-6.158773,9.893828,6.766350,-0.998469,-8.505670,-9.662851,-9.180462,8.523986,-5.969305,5.471053,9.138967,-3.115536,-1.301106,-9.684689,1.993650,7.521698,0.100306,-4.660083,-0.242243,-4.254171,3.273638,-2.244656,7.596332,-7.411278,1.996062,3.077961,-0.319959,-6.158132,-7.329275,5.583412,-6.178332,4.886492,5.009614,0.198167,-9.769750,-3.276318,-6.693268,4.218329,1.659932,9.728816,7.776337,4.607517,-0.201547,1.747027,7.116695,-1.982413,2.618771,3.065593,1.023903,1.424139,-5.034817,-5.237874,-1.287913,6.183742,5.368731,-8.175696,3.601121,-5.567388,0.884847,2.214566,1.332399,8.356884,2.307507,6.966530,0.849811,8.493451,5.428766,-6.692458,5.901994,3.164525,-5.074832,-7.877161,2.076350,8.249271,-5.764633,9.664486,-0.690605,-9.276433,-9.966462,-0.339127,-0.344739,5.491676,6.854775,0.441412,3.543550,3.223711,6.463321,-9.064695,7.787728,7.531774,-4.752268,5.742264,4.841902,-4.624572,9.257690,1.453530,-0.338723,0.881201,-4.365256,2.380124,2.793275,8.258735,-1.149526,-5.294959,8.253134,5.415830,-5.274368,-1.298512,-3.612608,8.475768,-8.448425,-8.364943,-8.116704,-9.291405,-9.735451,-2.138706,2.899993,-2.002834,6.810005,0.453051,0.239359,-1.343086,3.371797,2.814081,-5.712790,2.562609,-6.942570,5.509164,-1.589498,2.078509,8.094270,-3.960820,-1.963996,-8.950403,7.448548,-7.552578,-9.342427,5.185519,-4.274864,-8.973414,0.591100,5.367573,1.743699,-5.113511,-4.990805,-3.108439,-4.458686,-8.244755,-4.410085,-3.423352,-7.860050,-2.405527,-4.566749,-6.976195,-5.083389,5.679151,6.962740,4.519323,2.646420,-8.148623,-1.372780,-6.753773,3.706762,3.891459,3.039072,-6.043665,-6.803352,5.666817,-7.655370,8.940904,-0.851030,-4.101710,0.896568,-5.418302,-9.789186,3.190520,1.868246,5.991019,-3.770761,-8.285199,-3.334582,-6.406802,1.490071,3.002452,6.620227,5.896850,6.012880,5.398663,5.597684,-1.522466,-4.997570,-4.240546,0.820091,7.521229,-5.062378,8.215231,-5.157530,-9.642777,3.184114,0.157160,-0.383203,-2.558722,-2.392256,7.566870,4.149273,7.509384,3.809327,-6.528046,8.064627,-9.982681,0.120299,1.274348,9.786990,-2.326118,7.560844,-6.755216,-0.647815,-9.819693,-0.404127,-5.590791,6.155318,-6.958768,-5.726227,8.267738,-1.940452,4.404667,9.142006,9.304956,-0.148554,-0.758968,5.096357,-1.598553,5.794715,-9.241901,-6.930347,-9.496627,6.574373,-5.326631,1.664981,9.165322,5.302898,0.784747,7.609662,-5.402562,-2.108843,-6.872942,4.938040,7.352773,8.569092,-5.847191,0.609330,1.763330,0.921878,-5.265932,2.945945,-3.385042,-9.087674,3.598354,-6.515138,-4.382090,-0.308053,-7.166285,5.729912,0.774463,-6.585614,-7.878440,-1.856574,-1.515003,7.143635,-4.687115,-1.893340,7.996674,-3.229566,1.336172,-6.009384,-5.039770,-0.791151,-8.800803,-7.780990,-2.694241,-7.053644,-3.388201,-1.660149,-5.675048,9.491620,-7.648115,-9.763299,7.648490,-3.873974,8.652392,-3.264732,-8.348594,8.736991,-2.453744,-4.718492,-0.145701,8.723810,1.743663,8.842184,2.275652,-6.044414,-9.151297,6.500233,3.746938,-5.902089,9.615960,-7.643909,6.104986,-1.453722,-3.225607,-2.689199,9.084974,5.023331,6.770804,1.663375,-5.576924,-9.927639,-0.901857,-2.089181,-1.166179,-1.693349,4.667465,6.510864,-2.844782,-6.784058,-1.899009,1.760703,-2.984833,-4.309957,3.968437,-5.354505,0.844670,9.290307,-9.466531,8.510549,-8.574843,-8.903624,4.699892,3.135146,-2.426685,-7.402752,-5.692350,-2.368655,-4.837527,0.145641,-8.939632,0.883600,-7.842747,7.245126,-1.565092,7.749189,0.114929,-5.126137,7.504515], dtype = "float64")#candidate|1880|(880,)|const|float64
call_1878 = relay.TupleGetItem(func_454_call(relay.reshape(const_1879.astype('float64'), [1, 8, 11]), relay.reshape(const_1880.astype('float64'), [10, 8, 11]), ), 1)
call_1881 = relay.TupleGetItem(func_458_call(relay.reshape(const_1879.astype('float64'), [1, 8, 11]), relay.reshape(const_1880.astype('float64'), [10, 8, 11]), ), 1)
output = relay.Tuple([call_1876,call_1878,const_1879,const_1880,])
output2 = relay.Tuple([call_1877,call_1881,const_1879,const_1880,])
func_1885 = relay.Function([], output)
mod['func_1885'] = func_1885
mod = relay.transform.InferType()(mod)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mutated_mod.get_global_var('func_1885')
call_1886 = func_1885_call()
output = call_1886
func_1887 = relay.Function([], output)
mutated_mod['func_1887'] = func_1887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_2067 = relay.TupleGetItem(func_1885_call(), 1)
call_2068 = relay.TupleGetItem(func_1887_call(), 1)
func_1306_call = mod.get_global_var('func_1306')
func_1309_call = mutated_mod.get_global_var('func_1309')
var_2093 = relay.var("var_2093", dtype = "int16", shape = (896,))#candidate|2093|(896,)|var|int16
call_2092 = func_1306_call(relay.reshape(var_2093.astype('int16'), [8, 7, 16]), relay.reshape(var_2093.astype('int16'), [8, 7, 16]), )
call_2094 = func_1306_call(relay.reshape(var_2093.astype('int16'), [8, 7, 16]), relay.reshape(var_2093.astype('int16'), [8, 7, 16]), )
uop_2106 = relay.sin(call_2092.astype('float32')) # shape=(8, 7, 16)
uop_2108 = relay.sin(call_2094.astype('float32')) # shape=(8, 7, 16)
func_1655_call = mod.get_global_var('func_1655')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_2109 = func_1655_call()
call_2110 = func_1655_call()
var_2121 = relay.var("var_2121", dtype = "float32", shape = (8, 7, 16))#candidate|2121|(8, 7, 16)|var|float32
bop_2122 = relay.right_shift(uop_2106.astype('int32'), relay.reshape(var_2121.astype('int32'), relay.shape_of(uop_2106))) # shape=(8, 7, 16)
bop_2125 = relay.right_shift(uop_2108.astype('int32'), relay.reshape(var_2121.astype('int32'), relay.shape_of(uop_2108))) # shape=(8, 7, 16)
output = relay.Tuple([call_2067,var_2093,call_2109,bop_2122,])
output2 = relay.Tuple([call_2068,var_2093,call_2110,bop_2125,])
func_2136 = relay.Function([var_2093,var_2121,], output)
mod['func_2136'] = func_2136
mod = relay.transform.InferType()(mod)
var_2137 = relay.var("var_2137", dtype = "int16", shape = (896,))#candidate|2137|(896,)|var|int16
var_2138 = relay.var("var_2138", dtype = "float32", shape = (8, 7, 16))#candidate|2138|(8, 7, 16)|var|float32
output = func_2136(var_2137,var_2138,)
func_2139 = relay.Function([var_2137,var_2138,], output)
mutated_mod['func_2139'] = func_2139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1655_call = mod.get_global_var('func_1655')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_2141 = func_1655_call()
call_2142 = func_1655_call()
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_2151 = relay.const([[-10,-2,9,9,9,-8,-8,5,2,-6,5,-5,8,-7,-5,3,-1,-4,-3,10,8,-9],[4,4,-5,-6,10,-9,-7,7,3,-9,-7,7,-5,3,5,-4,5,-3,-6,-1,2,-7],[6,3,5,6,-7,1,-9,9,-4,1,1,-10,-6,-5,10,-9,7,-8,8,-4,6,-10],[8,9,2,-5,-7,-10,-5,1,-9,4,4,8,-7,-8,-6,7,8,9,-7,5,-9,-7],[1,4,8,-6,1,6,-4,8,-3,-7,-3,10,-1,4,-1,-6,6,-2,7,1,-2,3],[-1,8,-8,-4,-3,10,1,-6,4,-7,-2,-9,9,-7,6,8,3,-1,3,3,-2,-2],[7,-9,9,-3,7,2,-9,8,10,-3,2,-5,1,-2,1,10,-9,-2,5,9,-7,-9],[-1,4,-4,4,2,2,-9,8,6,9,7,4,-7,5,6,-2,2,8,-2,-2,6,-10],[6,-5,8,-8,7,6,-6,10,6,3,-8,3,-5,-6,9,-6,-6,7,-6,8,8,-9],[-6,10,-1,-7,4,-8,-7,2,10,10,10,1,-4,-3,-2,1,-3,9,4,2,-8,-10],[5,-8,1,-3,7,1,3,-6,-6,5,9,-3,2,4,-6,-4,8,7,1,-2,-6,-2],[7,-5,6,-6,4,10,5,-5,-8,-3,2,-6,2,3,-3,6,-6,6,-1,-9,-2,-10],[-4,-9,7,-9,-5,-3,-4,-6,5,8,-3,3,7,-8,10,-5,6,-7,7,1,10,1],[-4,3,-7,9,5,3,-4,8,-8,8,-6,-4,-10,7,2,-8,-4,-4,-1,-10,-6,8],[-3,-6,9,4,1,-2,-6,-3,-6,-3,-1,1,3,-8,-6,1,-1,2,-10,-9,6,-2],[-8,-9,7,7,10,-7,1,3,2,-9,-10,-4,9,1,-5,-8,-7,9,10,1,-4,-4],[-6,4,-1,-10,6,-9,-9,8,3,-7,4,4,2,3,-4,10,-4,-7,-7,-5,-2,8],[5,5,4,8,-8,10,-8,5,-2,1,1,-2,-4,3,-1,7,-9,-4,2,10,4,9],[5,-3,1,4,9,-2,10,9,8,-7,-8,-9,3,-2,9,9,7,10,4,-4,9,8],[-1,3,4,-6,1,3,-3,10,-8,6,1,-5,-2,-9,-5,4,-3,7,9,10,-7,5],[-7,3,-6,-1,7,-1,7,1,7,7,-4,-9,-6,-10,-1,-4,-2,6,-6,-2,-4,-3],[2,-2,1,1,4,6,-9,4,3,-10,4,10,4,-4,-6,-9,1,7,1,-5,6,-6],[10,-6,-9,-8,6,-5,-4,1,4,-8,3,6,3,-10,7,-5,5,9,-10,9,9,-6],[-10,2,-9,10,-6,-6,2,-10,-10,-5,8,1,3,6,1,-4,9,9,-8,9,-7,-5]], dtype = "uint32")#candidate|2151|(24, 22)|const|uint32
call_2150 = relay.TupleGetItem(func_1330_call(relay.reshape(const_2151.astype('uint32'), [6, 11, 8])), 1)
call_2152 = relay.TupleGetItem(func_1332_call(relay.reshape(const_2151.astype('uint32'), [6, 11, 8])), 1)
const_2156 = relay.const([[[3.294750,6.509390,0.635413,5.057865,-1.379853,8.595646,9.473636,5.405634,2.957890,1.893338,-0.449281],[9.899844,-9.355793,1.750015,-9.830856,1.252224,4.786849,-9.396780,2.693743,-4.291523,1.805401,2.653089]],[[9.523289,8.881904,2.252760,-3.975500,-8.811360,3.147754,-8.518035,-7.635649,2.883475,7.639318,-2.651711],[4.768614,8.150915,2.578828,2.717276,2.193692,4.186932,9.907270,-8.101271,8.714264,5.736049,7.083912]],[[6.793578,-0.383542,3.993350,5.900729,-9.099161,1.972396,5.245060,-4.260683,-0.876842,4.225081,-9.244764],[-6.785019,4.756630,8.072317,-3.690154,-0.307086,-7.948886,-7.586978,-6.489165,1.415644,-9.033363,-7.301156]],[[-2.180193,-1.022284,6.922820,-6.672962,5.434727,-2.628366,-3.941667,8.436890,-6.639806,-7.747444,2.027935],[3.012087,6.870640,-2.090885,2.596107,8.400957,7.803694,-1.704232,1.840694,-7.446718,1.925164,4.273133]],[[9.214670,-3.176888,7.305501,-2.835510,1.771506,-0.116756,3.075293,-5.631700,-2.510766,-0.604254,-6.157247],[-0.950976,6.282622,-0.482522,4.364594,0.147543,-6.107166,-9.244046,-6.113547,-1.413394,-6.557229,-5.890859]],[[3.694399,1.963736,-5.238381,1.391729,-7.047144,0.599528,7.767817,0.481493,3.950484,0.782411,-2.913443],[8.824906,-9.508100,7.160521,2.108302,-6.421305,-1.950296,-2.753234,4.824862,4.463564,5.371670,-0.154048]],[[-5.730977,4.424259,-6.903712,-7.190765,-0.330950,8.060903,6.721669,-6.544720,2.202826,-8.803487,-7.557594],[-2.787933,-0.670139,4.697414,-6.031010,-8.019638,0.147268,2.751530,-3.621201,2.992375,5.261419,-9.125255]],[[9.887066,8.415531,1.646500,-7.904067,-0.696875,-8.287543,9.194988,-4.563646,0.131884,-8.068566,-2.311957],[-9.391185,3.419366,-0.603274,-0.813089,-2.809782,8.360133,-4.362918,7.253050,-3.850666,-3.425542,-2.895735]],[[-1.377940,8.979192,-3.467535,7.198210,1.962090,1.077373,4.803410,-3.738148,-2.623450,3.455348,-3.163598],[5.866614,-8.708344,-8.536273,-2.915126,-9.312868,7.941369,-6.817201,-5.541171,2.452086,6.984118,-7.034489]],[[-8.038011,-5.890230,5.724736,-9.027319,-7.633836,5.154528,1.485720,5.343992,9.321110,-7.531852,3.325941],[-3.450482,-3.020259,-2.653511,-7.103818,-5.865668,2.547914,-4.336182,-7.268861,-6.796326,-3.312248,-1.866048]],[[5.869322,1.312822,2.447199,-3.776628,-7.426706,-5.451093,-9.062685,-0.536341,-7.804665,2.865493,4.643635],[-1.174677,-0.866766,-4.434159,8.901177,-9.060709,-6.091914,7.473674,4.401142,2.028944,-5.457863,9.516787]]], dtype = "float32")#candidate|2156|(11, 2, 11)|const|float32
bop_2157 = relay.subtract(call_2141.astype('int8'), relay.reshape(const_2156.astype('int8'), relay.shape_of(call_2141))) # shape=(11, 2, 11)
bop_2160 = relay.subtract(call_2142.astype('int8'), relay.reshape(const_2156.astype('int8'), relay.shape_of(call_2142))) # shape=(11, 2, 11)
output = relay.Tuple([call_2150,const_2151,bop_2157,])
output2 = relay.Tuple([call_2152,const_2151,bop_2160,])
func_2162 = relay.Function([], output)
mod['func_2162'] = func_2162
mod = relay.transform.InferType()(mod)
mutated_mod['func_2162'] = func_2162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mutated_mod.get_global_var('func_2162')
call_2163 = func_2162_call()
output = call_2163
func_2164 = relay.Function([], output)
mutated_mod['func_2164'] = func_2164
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2186 = relay.var("var_2186", dtype = "float64", shape = (15, 3, 8))#candidate|2186|(15, 3, 8)|var|float64
uop_2187 = relay.sqrt(var_2186.astype('float64')) # shape=(15, 3, 8)
output = uop_2187
output2 = uop_2187
func_2189 = relay.Function([var_2186,], output)
mod['func_2189'] = func_2189
mod = relay.transform.InferType()(mod)
var_2190 = relay.var("var_2190", dtype = "float64", shape = (15, 3, 8))#candidate|2190|(15, 3, 8)|var|float64
output = func_2189(var_2190)
func_2191 = relay.Function([var_2190], output)
mutated_mod['func_2191'] = func_2191
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2216 = relay.var("var_2216", dtype = "float32", shape = (12, 5, 15))#candidate|2216|(12, 5, 15)|var|float32
uop_2217 = relay.asin(var_2216.astype('float32')) # shape=(12, 5, 15)
uop_2220 = relay.cosh(uop_2217.astype('float64')) # shape=(12, 5, 15)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_2226 = relay.TupleGetItem(func_1885_call(), 3)
call_2227 = relay.TupleGetItem(func_1887_call(), 3)
output = relay.Tuple([uop_2220,call_2226,])
output2 = relay.Tuple([uop_2220,call_2227,])
func_2228 = relay.Function([var_2216,], output)
mod['func_2228'] = func_2228
mod = relay.transform.InferType()(mod)
var_2229 = relay.var("var_2229", dtype = "float32", shape = (12, 5, 15))#candidate|2229|(12, 5, 15)|var|float32
output = func_2228(var_2229)
func_2230 = relay.Function([var_2229], output)
mutated_mod['func_2230'] = func_2230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2258 = relay.var("var_2258", dtype = "float32", shape = (15, 12, 2))#candidate|2258|(15, 12, 2)|var|float32
uop_2259 = relay.asin(var_2258.astype('float32')) # shape=(15, 12, 2)
func_1485_call = mod.get_global_var('func_1485')
func_1489_call = mutated_mod.get_global_var('func_1489')
const_2262 = relay.const([False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True], dtype = "bool")#candidate|2262|(24,)|const|bool
call_2261 = relay.TupleGetItem(func_1485_call(relay.reshape(const_2262.astype('bool'), [6, 1, 4]), relay.reshape(var_2258.astype('bool'), [6, 15, 4]), ), 0)
call_2263 = relay.TupleGetItem(func_1489_call(relay.reshape(const_2262.astype('bool'), [6, 1, 4]), relay.reshape(var_2258.astype('bool'), [6, 15, 4]), ), 0)
func_1485_call = mod.get_global_var('func_1485')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2267 = relay.TupleGetItem(func_1485_call(relay.reshape(const_2262.astype('bool'), [6, 1, 4]), relay.reshape(var_2258.astype('bool'), [6, 15, 4]), ), 0)
call_2268 = relay.TupleGetItem(func_1489_call(relay.reshape(const_2262.astype('bool'), [6, 1, 4]), relay.reshape(var_2258.astype('bool'), [6, 15, 4]), ), 0)
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_2269 = relay.TupleGetItem(func_2162_call(), 2)
call_2270 = relay.TupleGetItem(func_2164_call(), 2)
uop_2277 = relay.sigmoid(uop_2259.astype('float32')) # shape=(15, 12, 2)
output = relay.Tuple([call_2261,const_2262,call_2267,call_2269,uop_2277,])
output2 = relay.Tuple([call_2263,const_2262,call_2268,call_2270,uop_2277,])
func_2293 = relay.Function([var_2258,], output)
mod['func_2293'] = func_2293
mod = relay.transform.InferType()(mod)
mutated_mod['func_2293'] = func_2293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2294 = relay.var("var_2294", dtype = "float32", shape = (15, 12, 2))#candidate|2294|(15, 12, 2)|var|float32
func_2293_call = mutated_mod.get_global_var('func_2293')
call_2295 = func_2293_call(var_2294)
output = call_2295
func_2296 = relay.Function([var_2294], output)
mutated_mod['func_2296'] = func_2296
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2311 = relay.const([[[True],[True],[False]],[[True],[False],[False]],[[True],[True],[False]]], dtype = "bool")#candidate|2311|(3, 3, 1)|const|bool
const_2312 = relay.const([[[True,False,False],[False,True,True],[False,False,True]],[[True,True,True],[False,False,False],[False,False,False]],[[False,False,False],[True,False,True],[True,True,True]]], dtype = "bool")#candidate|2312|(3, 3, 3)|const|bool
bop_2313 = relay.logical_and(const_2311.astype('bool'), const_2312.astype('bool')) # shape=(3, 3, 3)
output = relay.Tuple([bop_2313,])
output2 = relay.Tuple([bop_2313,])
func_2318 = relay.Function([], output)
mod['func_2318'] = func_2318
mod = relay.transform.InferType()(mod)
output = func_2318()
func_2319 = relay.Function([], output)
mutated_mod['func_2319'] = func_2319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_2337 = relay.TupleGetItem(func_1590_call(), 0)
call_2338 = relay.TupleGetItem(func_1592_call(), 0)
func_1655_call = mod.get_global_var('func_1655')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_2340 = func_1655_call()
call_2341 = func_1655_call()
func_1390_call = mod.get_global_var('func_1390')
func_1392_call = mutated_mod.get_global_var('func_1392')
var_2344 = relay.var("var_2344", dtype = "float32", shape = (288,))#candidate|2344|(288,)|var|float32
call_2343 = relay.TupleGetItem(func_1390_call(relay.reshape(var_2344.astype('float32'), [8, 6, 6])), 0)
call_2345 = relay.TupleGetItem(func_1392_call(relay.reshape(var_2344.astype('float32'), [8, 6, 6])), 0)
var_2354 = relay.var("var_2354", dtype = "float32", shape = (11, 2, 11))#candidate|2354|(11, 2, 11)|var|float32
bop_2355 = relay.bitwise_or(call_2337.astype('uint64'), relay.reshape(var_2354.astype('uint64'), relay.shape_of(call_2337))) # shape=(11, 2, 11)
bop_2358 = relay.bitwise_or(call_2338.astype('uint64'), relay.reshape(var_2354.astype('uint64'), relay.shape_of(call_2338))) # shape=(11, 2, 11)
output = relay.Tuple([call_2340,call_2343,var_2344,bop_2355,])
output2 = relay.Tuple([call_2341,call_2345,var_2344,bop_2358,])
func_2372 = relay.Function([var_2344,var_2354,], output)
mod['func_2372'] = func_2372
mod = relay.transform.InferType()(mod)
mutated_mod['func_2372'] = func_2372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2372_call = mutated_mod.get_global_var('func_2372')
var_2374 = relay.var("var_2374", dtype = "float32", shape = (288,))#candidate|2374|(288,)|var|float32
var_2375 = relay.var("var_2375", dtype = "float32", shape = (11, 2, 11))#candidate|2375|(11, 2, 11)|var|float32
call_2373 = func_2372_call(var_2374,var_2375,)
output = call_2373
func_2376 = relay.Function([var_2374,var_2375,], output)
mutated_mod['func_2376'] = func_2376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_2388 = relay.TupleGetItem(func_1885_call(), 2)
call_2389 = relay.TupleGetItem(func_1887_call(), 2)
output = call_2388
output2 = call_2389
func_2402 = relay.Function([], output)
mod['func_2402'] = func_2402
mod = relay.transform.InferType()(mod)
output = func_2402()
func_2403 = relay.Function([], output)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2421 = relay.var("var_2421", dtype = "uint32", shape = (14, 7, 16))#candidate|2421|(14, 7, 16)|var|uint32
const_2422 = relay.const([[[7,-8,-9,5,-8,9,-9,7,2,-2,-5,1,-7,1,-2,-1],[-10,7,-3,1,5,7,8,5,-10,-2,-8,-2,-10,2,7,10],[4,9,2,-1,1,-2,-5,-2,4,7,7,-6,6,10,3,3],[9,-7,3,7,-7,6,4,5,9,1,-3,6,6,3,6,-9],[9,6,-5,7,-10,3,8,-3,2,-5,-2,6,-7,-9,8,-9],[-7,8,-6,3,-7,-3,6,4,-1,-7,-1,10,4,2,1,-9],[-4,10,2,-9,2,6,7,8,-10,-10,-9,-1,-4,-7,4,-3]],[[4,10,9,-7,-9,-8,2,6,-10,2,-1,-4,-6,1,-6,-6],[-10,-6,-6,-7,-5,-3,1,-8,-8,-2,-3,-5,9,7,-10,6],[1,-8,-9,2,-10,-1,-4,3,1,-2,-4,-5,3,-8,7,5],[-10,-5,-8,2,-1,8,-4,-9,6,1,-8,-3,-8,-4,-5,-3],[9,-3,-6,-4,8,6,3,-8,7,-9,8,6,2,-1,8,-1],[5,-6,9,-9,2,-8,1,3,7,-2,5,1,7,-6,7,2],[3,2,-5,-8,6,-1,-4,-4,-8,6,-4,3,-10,-4,6,8]],[[3,-1,10,-9,-7,-1,5,-4,2,10,-6,7,2,2,1,-9],[-9,-5,2,-5,-4,-2,4,6,5,-5,-7,-6,6,-6,9,3],[6,6,4,8,10,9,-5,1,8,-10,10,5,5,5,7,-3],[6,4,1,-7,2,-6,-8,-5,-4,-5,-3,10,-2,-4,-1,-3],[-6,-6,-8,1,-9,-5,5,7,-8,-6,1,-1,-1,1,1,10],[10,6,10,-8,-6,8,-6,3,-5,5,4,-10,-10,-8,4,2],[-7,4,8,8,4,3,1,1,4,-4,1,-5,5,-4,5,-5]],[[-4,2,10,4,-6,-3,5,-4,2,-9,-2,-6,10,-7,5,7],[-10,3,-7,-5,6,-1,-4,1,-5,-10,7,-5,7,-9,-4,4],[-5,6,-6,6,-1,-4,-2,-2,9,3,10,-2,9,-9,-8,-9],[-2,5,-7,9,-8,4,9,-6,-8,4,-6,-4,8,8,-8,10],[-5,7,6,2,8,3,-2,6,7,-9,-6,7,-8,-9,3,6],[6,2,9,7,9,-5,-10,-2,-2,-1,-4,4,5,-8,-5,-8],[8,-3,3,-4,-4,5,3,3,8,6,4,4,3,10,8,9]],[[2,-5,-5,-9,-10,-3,2,10,9,2,8,-3,-9,9,4,5],[3,1,9,-5,4,1,3,4,9,-3,1,6,-10,-9,-6,-10],[-4,-4,-1,-1,-6,-1,-6,-9,2,-10,2,4,2,8,-8,6],[9,7,9,-7,2,6,-4,1,-10,10,8,4,9,-9,-8,1],[4,-9,7,2,3,-5,2,4,8,2,10,-5,5,6,-8,-3],[6,-7,-8,-2,6,10,5,8,10,1,-7,8,10,-7,4,3],[4,5,-9,-4,4,3,-10,7,2,-1,-4,-2,5,-3,1,-9]],[[5,8,-10,-1,8,8,-4,9,10,-6,9,9,7,-2,-9,5],[6,-10,-8,1,-4,6,-3,-5,-5,7,6,9,-9,4,-2,2],[4,4,-4,8,5,7,8,-1,2,8,-4,-3,-8,1,-6,9],[4,10,10,7,1,-1,5,-4,10,4,9,-6,-4,6,-9,-8],[8,-10,-7,2,-10,-8,5,-9,4,-8,1,-7,-3,5,-9,3],[-10,-8,2,6,4,-5,4,3,-9,10,-7,9,1,9,6,1],[-9,-4,8,-10,-1,-1,-3,4,7,6,-2,-3,-6,5,6,-7]],[[-5,-5,10,-5,-2,-8,3,7,-6,6,-7,-1,3,4,-3,4],[3,-1,5,-3,-2,-4,-5,-7,-5,10,-1,-4,8,4,8,-9],[9,3,4,3,-9,5,7,6,4,-3,-9,-9,-4,8,3,2],[-7,-8,-2,-9,7,6,5,-5,8,-3,-4,3,7,1,-1,4],[7,-9,2,-2,1,2,-2,4,-6,6,-3,-9,4,-2,2,-1],[9,-9,-9,7,-1,-5,-7,-2,9,-4,-10,-5,-4,7,5,6],[9,3,8,-7,1,3,-4,3,-4,-6,-2,9,7,2,8,-8]],[[-3,7,2,-2,8,1,10,-7,-10,1,3,-6,7,-6,5,-2],[-4,-10,2,7,7,4,-1,2,-4,-3,-2,-9,6,4,9,10],[6,8,-1,-10,5,4,4,7,-10,7,9,10,1,-7,-1,-2],[6,-7,-6,-5,-2,5,6,6,-2,5,6,7,1,-8,10,1],[1,-10,6,8,-4,-6,6,-6,2,8,-1,7,-8,4,8,-3],[-5,8,8,-9,-8,7,-4,10,6,-6,-4,9,-2,1,10,1],[-7,-7,2,1,1,-3,9,-3,-3,4,-5,-1,-5,9,6,-3]],[[8,10,-5,1,9,3,7,-4,6,-10,-10,10,-5,1,8,6],[3,7,9,6,-9,-7,-6,7,-1,-2,7,-6,-10,4,2,-3],[8,-5,-5,-4,-9,-3,3,6,6,-3,-2,5,-8,10,-1,-5],[3,5,-10,-6,-1,5,-8,6,-10,9,9,-2,7,5,6,-6],[-1,-9,-1,1,4,3,-6,8,-9,-6,4,-5,1,-8,1,6],[-4,-4,-7,-4,10,3,-8,2,9,-6,-7,4,3,4,6,6],[4,3,-5,-4,-8,-1,-1,6,10,-5,-4,-6,10,9,-2,6]],[[-6,-9,7,6,-4,2,1,-7,9,-9,-10,-8,-4,6,3,-2],[-10,2,8,-3,-6,-8,-10,-7,7,-1,-10,7,9,10,7,3],[-6,-5,2,7,-2,4,-9,2,-6,3,6,-1,-7,-7,4,-2],[-4,5,6,3,-8,-1,-7,-5,7,-10,-9,-8,-2,9,-4,8],[-9,-3,8,2,-2,-5,5,1,-7,7,-9,-2,-7,-9,-3,10],[-4,6,8,8,-8,-8,-10,-7,7,2,-6,-9,7,-5,-8,2],[-7,-4,4,-6,4,7,2,-2,9,-6,-10,1,6,-8,2,-6]],[[6,-5,-1,-5,4,8,10,-6,-4,4,-9,1,-3,-8,9,-4],[-4,-5,10,10,4,2,8,2,10,7,-3,3,-9,8,4,3],[1,-3,-10,8,10,7,-8,3,-7,7,1,5,-2,-8,-5,4],[-10,8,1,3,6,1,-9,1,-5,5,8,-7,-2,-7,-7,4],[2,-7,-8,4,10,-7,10,-6,-6,-2,-2,-7,6,-3,8,2],[9,-3,-10,2,-2,1,-9,-6,10,3,7,-6,5,9,7,3],[1,-5,-3,-2,-8,-9,-10,3,-3,1,6,6,-9,5,4,-5]],[[6,-7,9,-5,10,5,7,9,-6,-3,-10,-4,-1,6,-8,10],[1,2,7,-8,-1,7,2,-9,6,1,-8,6,7,-5,-3,9],[-4,-5,-10,8,-5,-9,-10,-5,10,-4,-4,-10,-4,-6,-3,10],[-7,10,7,9,10,-9,6,-9,-4,9,-5,9,-7,6,-1,9],[1,-5,5,2,-2,10,-7,-8,-5,-6,-7,10,9,6,-4,8],[-4,6,9,-9,-9,2,-9,6,9,-6,7,2,4,8,5,-3],[-10,-2,-7,3,1,1,-8,-6,8,-5,8,5,-7,9,-8,5]],[[-3,1,8,-7,9,-1,-4,-6,-8,1,10,7,-8,1,9,6],[-3,-2,-10,3,7,-8,10,-7,-5,-6,4,-2,8,-10,1,10],[2,-6,3,4,3,2,8,-6,8,7,3,-4,-5,9,2,-10],[1,9,-7,-3,6,8,5,-6,5,-4,-3,9,-5,-3,-10,-1],[1,7,6,-2,7,6,-3,-6,-6,-7,1,6,-6,2,4,-9],[7,4,-5,-6,6,6,-8,10,-3,4,4,-9,-9,-10,-6,7],[-2,7,-9,2,8,-9,-8,-10,-7,-4,-4,-5,4,5,2,-5]],[[5,4,6,-1,5,9,-8,-4,-3,8,-1,-10,8,-7,9,7],[-6,10,-8,-8,-3,-6,-8,-8,1,6,-10,-9,2,-9,9,-7],[-8,7,-1,8,-4,7,-7,10,-2,9,5,-2,-5,-9,8,7],[6,1,1,-1,4,-4,2,8,-2,-8,7,3,-1,-6,2,-5],[1,6,-5,-6,5,-9,-8,5,-6,-7,2,-6,-6,-4,-8,-5],[-4,1,-7,8,1,-3,4,8,-10,4,-7,-9,-5,-9,3,-1],[6,6,-3,9,4,2,7,-10,5,9,6,-2,10,-3,-9,1]]], dtype = "uint32")#candidate|2422|(14, 7, 16)|const|uint32
bop_2423 = relay.minimum(var_2421.astype('uint32'), relay.reshape(const_2422.astype('uint32'), relay.shape_of(var_2421))) # shape=(14, 7, 16)
uop_2428 = relay.cosh(const_2422.astype('float32')) # shape=(14, 7, 16)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_2431 = relay.const([5,-10,8,-8,-5,-4,-9,10,-5,2,3,-8,9,5,-8,-4,8,9,-10,-8,2,-1,-7,7,-10,-5,-6,6,-8,1,-1,8,-10,5,4,6,7,6,-10,8,-3,1,-8,5,7,-4,2,8,-9,-4,8,8,7,3,-7,5,6,1,4,3,-3,-2,9,7,-6,-10,10,2,-9,7,8,8,-10,9,5,7,-9,3,10,-5,-10,1,-10,-9,9,-7,-10,10,-5,5,-1,8,-3,7,10,10,-4,1,-7,4,-8,3,-7,-5,-4,-2,3,4,-10,1,-2,1,-3,1,-3,-6,-6,-7,3,-5,4,-3,-9,5,9,-1,-7,8,-3,10,2,6,-6,-10,9,-8,-3,2,-10,-3,-2,-2,7,9,-7,-7,-6,8,10,-2,1,1,-3,-10,-9,1,-7,2,-3,5,1,-10,7,-2,-3,-7,6,-2,1,1,-5,5,7,6,-8,9,-5,10,-6,10,-9,-6,4,-4,-10,-9,9,-6,1,6,5,1,-6,-3,-5,4,9,-1,-9,-10,-9,-5,10,7,-5,1,2,-1,4,3,-8,-5,6,-10,10,6,-8,2,-2,9,3,9,-3,4,-6,-9,1,-1,-2,3,-10,5,-10,6,-5,-1,-5,2,3,-7,2,-5,-4,9,9,9,-1,-7,-1,-2,10,-3,-4,-4,2,9,-7,-6,-1,8,8,-1,-2,-1,3,-9,7,-9,8,9,5,5,-2,-5,-5,5,10,4,4,7,9,2,10,6,-5,10,-2,-3,6,-1,1,-8,-2,5,10,-5,9,-4,9,9,-6,3,5,-6,4,-4,3,-7,4,3,5,-4,5,5,9,-7,6,7,-6,4,10,6,-2,6,-5,2,7,8,4,-8,-9,10,-7,-9,-7,4,3,-9,-2,-10,6,-1,-8,6,2,4,1,9,10,10,10,-5,5,-7,2,6,-1,-2,-5,10,-6,-9,10,-4,5,-8,-9,10,-8,1,-6,10,5,6,-4,-7,5,-5,3,5,-5,-3,-5,-10,-1,3,-1,5,-4,-6,-1,9,9,1,5,-10,-9,7,-7,5,10,-5,2,7,-3,4,-5,8,-7,6,4,-4,-2,-7,10,6,1,-2,-3,8,-1,-8,5,10,6,6,3,-3,1,-3,1,2,3,4,3,10,4,8,-5,-3,-6,10,-1,4,4,-2,7,8,7,5,-4,2,4,-1,-10,-1,5,6,6,-7,-5,5,4,3,-5,-3,-5,1,7,-2,6,5,-3,-9,-1,9,-7,10,-10,-3,1,-8,-3,10,10,-8,3,10,-4,-9,5,-1,-4,4,-3,-1,-4,-5,-7,-6,-6,3,-8,7,4,-7,4,1,-8,-4,-3,5,5,4,-4,-8,7,-10,-6,8,-5,-1,4,8,9,3,10,-1], dtype = "uint32")#candidate|2431|(528,)|const|uint32
call_2430 = relay.TupleGetItem(func_1330_call(relay.reshape(const_2431.astype('uint32'), [6, 11, 8])), 1)
call_2432 = relay.TupleGetItem(func_1332_call(relay.reshape(const_2431.astype('uint32'), [6, 11, 8])), 1)
output = relay.Tuple([bop_2423,uop_2428,call_2430,const_2431,])
output2 = relay.Tuple([bop_2423,uop_2428,call_2432,const_2431,])
func_2438 = relay.Function([var_2421,], output)
mod['func_2438'] = func_2438
mod = relay.transform.InferType()(mod)
var_2439 = relay.var("var_2439", dtype = "uint32", shape = (14, 7, 16))#candidate|2439|(14, 7, 16)|var|uint32
output = func_2438(var_2439)
func_2440 = relay.Function([var_2439], output)
mutated_mod['func_2440'] = func_2440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_2542 = relay.TupleGetItem(func_1885_call(), 0)
call_2543 = relay.TupleGetItem(func_1887_call(), 0)
output = relay.Tuple([call_2542,])
output2 = relay.Tuple([call_2543,])
func_2570 = relay.Function([], output)
mod['func_2570'] = func_2570
mod = relay.transform.InferType()(mod)
mutated_mod['func_2570'] = func_2570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mutated_mod.get_global_var('func_2570')
call_2571 = func_2570_call()
output = call_2571
func_2572 = relay.Function([], output)
mutated_mod['func_2572'] = func_2572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_2623 = relay.TupleGetItem(func_1590_call(), 0)
call_2624 = relay.TupleGetItem(func_1592_call(), 0)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_2628 = relay.TupleGetItem(func_2318_call(), 0)
call_2629 = relay.TupleGetItem(func_2319_call(), 0)
func_1870_call = mod.get_global_var('func_1870')
func_1874_call = mutated_mod.get_global_var('func_1874')
const_2631 = relay.const([-9.798195,9.636095,3.021753,-1.420425,4.445023,1.162839,-5.636106,-8.547058,-3.767417,-6.582555,3.629525,0.446536,-8.850478,7.667626,-5.818750,-2.784894,5.128571,-0.473004,8.224800,6.915033,-7.664449,-7.144399,8.196205,5.097715,-0.837814,7.146387,-8.283996,-7.317045,-0.962511,-4.800404,-9.859147,0.560239,-7.698593,-5.142843,-0.131425,-0.523911,-6.183033,9.322631,1.276256,6.822161,-1.050454,5.022232,1.290847,-5.147263,1.107936,-7.068012,4.856522,9.455776,-6.455193,-6.856125,1.456209,7.417904,1.132024,0.636851,-8.877423,-1.240791,3.890752,2.366558,9.769245,-5.527576,-1.727586,-9.756345,-4.502853,8.695189,-1.758055,5.396343,-7.729579,2.655713,1.964405,-3.678323,-2.273754,4.046913,-1.862909,-6.926168,-9.523552,-9.522082,-9.360436,-0.852405,-3.311233,9.998421,4.133798,-9.441833,7.231884,-7.504141,-4.189092,-6.195692,8.116241,2.072432,-5.550647,-7.838462,-2.785875,8.457290,3.537730,-3.255116,9.224605,-4.349199,-3.639241,-1.103031,4.991977,3.256189,7.115491,-9.154810,6.809644,-1.613151,6.915516,-1.841222,2.120969,-7.962878,3.987800,-9.962403,-6.439440,-3.603172,4.276349,5.587045,9.504870,3.158451,-5.353350,1.514580,7.165428,-1.492564,-0.404625,-7.263619,-0.361238,3.168677,0.349262,2.763686,-1.508084,8.400377,-6.167218,-8.016733], dtype = "float32")#candidate|2631|(130,)|const|float32
const_2632 = relay.const([7,-6,2,-7,6,7,7,-5,4,3,4,9,1,-9,10,4,-3,-4,-2,9,-6,-5,4,6,-9,10,-6,-7,2,-10,1,10,6,8,-4,-8,-5,3,-7,5,-10,1,4,3,-5,6,8,-3,-9,4,10,-4,-9,4,10,1,-6,7,2,8,4,-7,-10,-9,-1,-4,7,6,7,-1,3,8,-6,-1,-5,-10,-3,-1], dtype = "int16")#candidate|2632|(78,)|const|int16
const_2633 = relay.const([5.753528,-2.150830,1.117594,6.010737,2.601491,3.363765,2.562984,-6.866871,1.786190,9.535115,8.297880,1.634566,-4.680324,1.450099,4.272747,4.326223,8.058356,8.440006,0.322787,-7.952018,-2.699863,7.054317,3.415590,5.340319,-9.376783,9.935872,-7.978706,2.754551,-0.259663,3.784104,5.335455,6.994866,-9.241616,1.590481,2.666785,-6.238585,0.708831,9.748774,-6.706608,0.626444,-3.725120,-6.047838,2.654748,9.065022,-6.931319,-7.068688,-0.622688,1.367069,-3.439299,-2.624771,-0.023358,4.931610,-8.390834,-6.067031,3.117242,5.643345,2.275184,-9.220842,0.911876,-3.047482,-6.528790,-2.478204,-3.933056,7.768959,-0.221784,-6.644684,2.219499,2.465587,7.678841,-2.012212,0.861593,-0.375372,9.346801,-6.704438,-4.954918,-8.706455,3.348330,6.420339,-2.248215,-2.131985,-1.323576,6.448097,-7.325469,9.641556,9.688236,-4.498536,-5.626450,6.235860,2.232073,-2.498798,-9.975780,9.882060,7.565825,-1.665368,6.271818,2.237571,4.294240,8.377306,8.075030,0.246876,-6.880489,4.113498,-5.571822,-5.197993,-5.599067,-8.864290,-3.590381,-8.598771,-2.987478,6.985171,8.189812,-9.326396,-1.083045,-1.472112,-4.563370,-7.684608,6.926764,6.825993,-5.222986,-0.401662,1.062104,4.205023,-4.011587,3.343009,-4.807958,-5.768050,4.920627,4.418700,4.869584,0.616926,3.292867,-5.635841,-6.692331,1.112229,-5.718737,0.591163,-4.702875,7.530411,3.394904,5.194014,6.841553,7.134046,-6.405090,-0.739590,7.755782,-4.350595,6.296928,9.917999,-6.867987,-5.518984,-6.410182,-2.084354,8.393271,1.973831,1.300565,-2.752561,9.198034,3.580151,-4.270941,4.054773,-8.324520,4.318563,-6.023469,8.645697,8.067024,2.527275,4.427652,-5.471842,3.168495,9.279991,-6.829064,-7.954998,-5.355400,-1.465866,5.743997,-2.241524,6.569009,-5.554849,-0.520442,-0.440060,4.214692,-6.841018,-0.305413,6.216180,-6.435266,-3.381069,0.771301,-9.974860,-9.786013,-5.344103,-7.581304,8.320390,-5.992917,-8.056353,4.940168,-9.029954,-2.278832,-3.961836,6.073490,7.997950,-0.362591,2.475045,-4.324497,0.358311,-0.816840,-8.763847,-3.961168,-7.173435,6.810773,-7.173803,0.794402,-9.262245,3.373846,-9.849741,-4.720496,-8.241302,4.106181,-7.746698,-7.381412,9.731844,-6.017525,4.253226,8.374530,8.328517,-5.785615,-6.007042,3.953037,-9.213874,0.468526,1.364350,-3.866820,-1.845186,9.413499,0.842991,7.477984,-7.443023,-9.066238,-3.867465,3.777639,7.081982,9.526656,-1.863744,-1.781347,6.864622,8.565039,5.357528,2.846541,-9.438849,3.754410,-1.589703,-6.142675,-9.865380,-5.408432,-4.749613,-5.241985,-2.333635,9.747118,-0.911576,6.344362,4.819691,6.502793,-0.978153,2.399062,7.517205,-9.662481,5.315610,2.341916,9.381244,-4.213516,0.930626,8.576649,7.023676,-4.404212,-1.439207,2.421356,9.537414,5.009198,5.007156,-7.049296,6.355605,-9.304210,4.530340,-2.619106,-8.137264,-5.026676,1.446032,3.091626,8.950196,7.404230,9.145057,2.690845,1.626054,-8.440533,3.487490,6.048427,1.690969,8.004814,6.418311,0.838358,3.413662,-7.139225,-3.386219,1.388335,3.124717,9.999213,9.757096,3.228487,2.346292,-3.274456,-6.640943,3.312903,4.037961,-9.848058,-2.479995,-3.939706,-4.638752,6.993717,-6.051062,-2.887182,6.612696,-9.444237,-1.917568,2.746293,9.329988,7.814642,3.432090,5.000322,1.034349,-0.906905,-4.370044,1.452389,8.217035,6.469273,0.170120,1.731342,6.087131,-5.240230,-9.984610,-2.856415,2.640509,2.040726,-7.584864,3.309474,5.212412,-7.040129,6.515278,-7.323473,-5.423614,-2.278063,9.786400,-8.740492,-4.329574,-8.134518,-6.743302,-0.351075,-0.781140,-5.798263,9.002022,7.713205,4.124081,-7.017466,5.989480,9.251268,-8.565864,-1.974038,-2.498183,-2.644355,9.397242,2.656244,5.541481,0.232856,1.074583,4.606408,2.692533,8.427350,-7.928318,7.810960,-8.903043,4.508654,5.828337,-8.842446,-2.654778,-4.953383,-8.026799,3.810534,9.663992,9.038270,-4.832168,8.968281,4.250806,1.044385,-6.801343,-1.784051,1.685434,3.124966,0.368963,-5.223103,0.073636,1.527914,-2.447077,9.992287,7.422599,8.982467,8.641034,7.521183,9.500901,-9.495983,-4.217382,6.942691,-4.251713,-7.045653,-2.145789,1.878489,2.525384,3.660246,5.463201,7.538655,-2.284560,2.636961,-2.486577,-3.156347,3.514049,4.271419,9.791856,5.568807,-1.550149,9.866254,2.506781,-0.332699,0.793376,-9.786451,-3.934867,4.517058,-4.079062,8.992414,-1.803940,9.956035,-3.243061,3.739278,2.209292,-4.411213,-2.680783,-9.926778,-9.805918,-8.622829,5.552682,2.414249,-3.212603,-7.991886,6.560489,5.420810,9.559919,1.610147,-7.411570,-2.897394,0.723489,5.661988,-6.621331,2.294414,-0.129610,3.484880,1.996153,6.965744,2.140121,-7.674005,4.709195,-9.555236,-7.202572,2.432901,-2.238026,-1.151418,-0.110605,5.066556,-9.403732,2.845295,-9.102885,-0.044542,7.878479,-7.760837,8.889841,3.212979,-3.758313,2.938880,8.464048,5.182701,-2.608331,-1.096344,6.139113,-6.680170,-9.337381,-5.546728,-1.828388,-9.610075,3.448456,-3.005833,-0.255018,8.132687,-4.164337,1.231789,2.962905,7.721901,9.803777,-0.463373,-1.118924,-1.253756,8.220354,8.489473,8.660524,4.128671,-7.672566,9.880824,-4.291627,-1.498249,3.130651,-6.721664,-8.464662,4.609508,9.609202,9.474787,-7.617892,6.390283,-0.140867,6.690686,-9.807551,-6.461067,-1.459055,8.161330,7.013031,4.913869,-0.945664,5.363042,-5.040102,-7.699819,6.104298,9.422086,3.434771,9.317350,0.446934,0.218086,1.558236,7.334774,1.179625,-8.509737,-0.607129,3.861464,-2.721544,7.285321,0.579124,-1.577259,2.874035,-7.763068,-1.609589,2.821739,-8.169778,-5.427095,-8.925559,-9.448566,-1.356833,-9.054274,-7.268471,8.122206,0.802883,2.126396,-5.138302,0.516853,6.936728,-6.919283,6.999226,-0.123015,-7.532707,8.302182,-7.400557,-7.900371,2.298709,1.393992,7.727999,-3.087815,3.659007,8.884909,7.842822,-6.701669,9.004813,8.141782,-4.424291,-4.883221,-6.193449,7.731828,9.093712,0.180925,1.583083,0.317813,-8.303633,1.031511,5.350040,2.767529,3.536899,-8.764017,2.570641,0.250144,4.886060,-4.090522,0.894878,-7.638328,-2.428754,6.013470,-7.411075,-9.451931,-1.654739,-3.650350,-3.181463,1.192377,0.508102,-9.361664,2.209468,-3.204023,-1.742924,-6.530410,5.318062,-3.283719,-7.112588,3.846286,-5.598276,1.743171,7.289321,3.446007,-3.492132,3.978068,-3.812141,-9.602391,5.712552,-2.489729,4.571247,6.478459,5.378600,-7.961414,-1.823861,-3.621478,6.048345,1.004119,1.533688,4.430436,0.750558,-6.067961,-5.071532,3.267239,1.436794,8.937933,-9.450069,8.322721,5.894450,-6.337036,1.414233,-9.828255,-4.544922,7.136632,-8.946067,0.342207,4.792203,9.180997,-7.715642,2.048576,-0.771992,8.025269,-9.600856,-8.865884,-2.394033,1.285857,9.890418,6.013869,2.694682,-5.309798,4.345941,-4.735146,5.966374,-0.968094,-2.743256,4.750784,1.166471,-0.874590,-1.417779,9.260126,7.536182,-1.162137,-3.883879,-2.656123,4.567682,-5.843328,1.387407,7.834760,-5.273230,-9.336335,-2.369168,-8.713071,-0.684949,1.040551,6.713283,-2.102620,6.716630,-4.121002,-8.338344,6.690554,7.118635,-7.181256,-4.364688,7.288611,8.201054,-4.296384,7.562536,2.508847,1.167166,-3.300237,6.826415,4.863393,-4.173087,8.337041,-0.397623,-7.984027,-7.732658,-4.981758,-7.948818,4.843506,-1.488796,2.592095,-6.776417,6.964612,1.026068,0.462311,-4.493151], dtype = "float32")#candidate|2633|(728,)|const|float32
call_2630 = relay.TupleGetItem(func_1870_call(relay.reshape(const_2631.astype('float32'), [5, 13, 2]), relay.reshape(const_2632.astype('int16'), [78,]), relay.reshape(const_2633.astype('float32'), [728, 1]), ), 6)
call_2634 = relay.TupleGetItem(func_1874_call(relay.reshape(const_2631.astype('float32'), [5, 13, 2]), relay.reshape(const_2632.astype('int16'), [78,]), relay.reshape(const_2633.astype('float32'), [728, 1]), ), 6)
output = relay.Tuple([call_2623,call_2628,call_2630,const_2631,const_2632,const_2633,])
output2 = relay.Tuple([call_2624,call_2629,call_2634,const_2631,const_2632,const_2633,])
func_2641 = relay.Function([], output)
mod['func_2641'] = func_2641
mod = relay.transform.InferType()(mod)
mutated_mod['func_2641'] = func_2641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2641_call = mutated_mod.get_global_var('func_2641')
call_2642 = func_2641_call()
output = call_2642
func_2643 = relay.Function([], output)
mutated_mod['func_2643'] = func_2643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2680 = relay.var("var_2680", dtype = "float32", shape = (1, 6, 13))#candidate|2680|(1, 6, 13)|var|float32
var_2681 = relay.var("var_2681", dtype = "float32", shape = (8, 6, 13))#candidate|2681|(8, 6, 13)|var|float32
bop_2682 = relay.add(var_2680.astype('float32'), var_2681.astype('float32')) # shape=(8, 6, 13)
output = bop_2682
output2 = bop_2682
func_2706 = relay.Function([var_2680,var_2681,], output)
mod['func_2706'] = func_2706
mod = relay.transform.InferType()(mod)
mutated_mod['func_2706'] = func_2706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2706_call = mutated_mod.get_global_var('func_2706')
var_2708 = relay.var("var_2708", dtype = "float32", shape = (1, 6, 13))#candidate|2708|(1, 6, 13)|var|float32
var_2709 = relay.var("var_2709", dtype = "float32", shape = (8, 6, 13))#candidate|2709|(8, 6, 13)|var|float32
call_2707 = func_2706_call(var_2708,var_2709,)
output = call_2707
func_2710 = relay.Function([var_2708,var_2709,], output)
mutated_mod['func_2710'] = func_2710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_2724 = relay.TupleGetItem(func_2318_call(), 0)
call_2725 = relay.TupleGetItem(func_2319_call(), 0)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
const_2727 = relay.const([[-9.471879,-6.861555,1.585102,3.444631,-2.540681,-4.795584,-0.897302,8.232607,-7.179778,-7.416970,-2.669717,5.398147,9.247039,4.971805,-1.439692,4.497674,4.475385,4.388387,-1.139179,0.720595,5.207624,6.950096,3.833253,6.988688,1.839262,-7.983433,-4.140649,3.202835,7.631876,4.923456,1.763404,-1.800448,-6.465985,0.031681,2.899972,2.230849,0.334724,-5.525824,6.160735,-4.864406,-4.995933,-2.780567,-2.430843,-9.706092,0.701128,1.544251,-9.233855,2.733741,-9.619368,1.816298,7.090144,-7.229195,2.205869,-2.646527,-2.391922,-7.701968,6.181743,2.301041,-0.502049,2.228116,5.875389,-0.172819,4.924721,-7.731176,8.725556,2.702271,-2.942683,5.031179,-6.261397,4.216235,-2.605235,6.711912,-1.353760,2.874529,-7.435711,-9.403016,-7.603913,1.390126,-9.337218,3.633782,-6.428121,7.558243,-8.172719,-0.291641,-6.131895,5.125696,0.765756,-1.586571,-8.707329,-9.866077,5.795079,-5.278120,-9.249828,4.009104,-9.829740,-5.475739,0.717971,0.571214,-8.429471,-9.988719,1.705449,8.621918,0.582362,3.304617,2.154698,-2.017596,-0.467927,-6.684177,9.657055,-2.669020,-0.433658,-4.316910,-7.835886,2.122173,3.614771,1.942048,-6.908657,-2.630337,-2.072110,3.462403,1.541718,-2.578315,-8.747735,-7.213783,-5.878174,3.314548,5.141348,-5.702702,-7.720562,-0.068300,-6.792705,-0.025046,-7.606366,-3.162376,-7.635280,6.522773,2.717016,-5.674394,-0.429708,7.277629,2.675883,-4.100489,-6.042493,-3.631599,-3.712964,6.416801,-2.965690,4.127556,-3.273554,2.690823,3.499139,-8.263283,8.368507,4.320622,-1.019953,-7.926586,5.870988,-8.649459,-4.262535,-2.271666,-5.733531,2.068380,-4.609029,9.683390,-9.665000,3.838206,9.678510,-0.207438,-6.611684,3.361634,5.441735,-9.328408,-0.181200,-9.478317,3.417625,1.288161,-7.576866,-0.974840,-9.633913,9.072476,9.129910,-4.431906,6.267670,1.161983,-3.003529,-0.474790,-4.808736,1.169406,4.937925,1.195838,-8.189267,-4.868969,1.395007,8.621134,4.350228,-8.691397,-4.498985,2.399815,-1.853627,6.079709,7.248792,-3.206769,6.813400,-2.567742,5.017438,7.669673,8.869818,0.009503,7.006396,-7.183373,5.351723,8.096875,4.522570,3.212407,5.943943,6.543359,-8.732596,-8.532260,1.179717,3.938083,8.716995,-6.462750,-6.861954,4.366931,8.457909,-0.909419,0.186236,-9.714549,1.418373,-0.326019,-3.572073,7.212665,2.751630,-0.994618,4.467308,2.940983,5.417333,3.480325,3.813994,6.892295,-7.870025,-8.320156,6.670820,-0.262873,-4.031678,6.903577,-6.325395,-4.008405,-4.789709,-7.930042,-3.317799,-4.441082,-4.692602,6.789867,4.843229,-5.240675,3.831180,4.657204,9.006627,3.493851,-4.583478,-0.962400,2.513440,-3.629052,-6.943537,2.565867,-4.389704,-7.983690,4.839692,5.499142,-6.494414,-8.825015,-3.596020,-5.789390,-4.743106,8.393179,-8.378957,4.482157,-6.767127,9.171543,2.018704,2.948531,9.192443,-5.644272,-6.803563,7.118772,4.516386,-3.286357,2.722270,7.259644,-9.115139,-0.087562,-1.952757,-8.686414,2.229474,7.781107,7.100058,-6.807054,-9.649030,1.716668,-5.145636,7.520853,8.080130,2.904162,-4.228471,-4.486198,-4.207389,8.899905,-9.098407,7.484617,-3.402015,-1.176094,-2.355739,-9.051909,0.119201,8.519303,-0.035763,2.616989,-6.776187,-3.841599,0.733879,4.444540,2.605314,2.860088,-8.623375,4.191624,2.601425,-9.085346,-5.566172,3.271341,4.332913,-4.311318,3.230378,5.519993,-3.257339,5.376668,-7.074996,0.486123,8.861698,1.912164,-2.090331,-8.374932,8.267984,7.953670,4.504676,4.233337,4.590250,-0.101795,-4.386190,-7.918215,6.231041,-9.152150,-2.959030,4.062286,-7.548552,5.895852,5.711106,4.082487,0.369688,0.172057,6.541207,4.941535,-2.035337,4.866475,7.191643,4.660774,1.338366,-1.861196,-7.721844,-6.065925,-7.321496,9.300150,2.042671,-2.293801,7.293837,-0.186126,4.118436,0.223120,9.529793,-9.490574,-5.837130,-7.163530,7.097318,5.670448,-4.171138,3.989088,8.064165,3.661333,8.825728,6.907397,4.325572,1.662189,9.246416,-6.647789,7.013025,2.651514,-2.903726,-2.393970,-4.069257,7.355041,4.282157,-3.069283,4.263935,9.007646,4.475643,0.663069,-3.181922,5.932088,0.106042,1.696674,-2.504282,-8.323525,-2.743916,8.598955,-9.269767,5.671052,2.176412,3.634643,1.790665,3.668151,4.207694,0.948505,5.082519,-6.098471,-5.584137,3.362937,-5.680044,-2.722346,-5.257725,-9.674589,-6.722906,-2.520681,9.982646,6.564800,1.400726,3.051322,1.434020,-7.149624,-7.668915,-3.861407,-5.395340,2.425472,1.982542,3.065379,6.468976,3.377246,-8.190629,0.232276,3.150326,-6.715869,8.918686,3.872615,4.231662,2.069946,-7.564287,-3.069651,-1.478478,-1.627123,8.597437,2.204330,3.113844,0.834428,7.235709,9.972242,8.880719,6.359202,3.126306,0.706513,-8.077048,-2.919455,-9.951276,-9.441209,1.835485,7.567332,-0.835145,6.864864,6.321532,5.296250,-9.173103,0.530777,3.323845,-2.195140,9.200536,3.197939,6.987011,3.375451,-5.143067,-2.363388,-7.304350,7.799752,-8.678956,-0.234356,2.224916,-4.422097,-8.674825,5.481636,-4.489023,-7.444270,6.200381,-3.981627,-1.133840,2.199260,0.921804,-0.791053,7.053822,-9.078345,-6.181491,4.392675,5.577549,9.370287,4.613490,2.918446,0.516537,6.590446,9.683542,1.698886,5.523839,-1.876793,-3.616521,-6.505248,-1.671123,0.215419,2.125554,-4.743545,9.347174,-8.081620,-8.815643,-7.284335,-4.054561,1.530554,0.305572,2.745698,9.801138,2.160655,-2.573942,6.908331,0.530417,6.276482,9.929239,7.156955,-6.053880,4.299153,4.190770,-3.446203,6.856759,0.967232,-4.420241,-2.970727,-6.231669,5.359962,1.058761,-4.415739,5.232441,-9.074347,9.393360,6.696400,5.768060,2.029455,7.213101,-9.849383,4.675730,5.913009,-7.784898,6.851210,-9.972819,9.029002,5.146134,-6.864086,-3.672692,3.649517,-0.280418,5.925836,7.725062,-8.615493,-9.963454,0.064515,-2.553627,0.748515,-2.192736,4.673846,1.686259,6.334961,-4.256019,6.647347,-0.109772,8.913615,-3.392738,-2.926919,0.165683,-5.625939,-2.296975,9.304850,-0.117548,1.975347,8.876417,3.545720,-6.394389,3.829007,-3.651951,5.682718,0.550974,9.650959,5.306350,2.692609,-1.237713,-8.056393,0.913666,9.882917,-8.494505,5.686001,-9.660659,-3.188288,4.789416,3.594356,-8.609139,-9.482295,1.499189,2.883247,4.440528,8.856090,-8.461517,-0.563605,3.122026,-0.414020,1.237767,9.103406,-8.437639,-5.803697,1.142932,-2.856256,-1.164088,9.655430,-9.539025,-2.836298,8.715763,-7.193628,2.121618,-1.656764,-8.626137,-6.683938,-0.157987,8.678367,7.898469,-3.081249,-9.287636,-6.229003,3.940086,-4.831453,6.917254,4.890426,8.680810,-8.785096,1.260137,5.178380,8.352505,7.622832,-2.143651,1.837732,-7.476801,-6.515877,-0.346241,9.896837,0.870138,1.712810,-1.492844,0.096640,-0.965578,-1.088888,-9.364865,-2.404508,9.487460,5.431994,-3.556364,9.304697,-3.113275,7.941064,-1.781447,-4.330140,9.128394,-5.072301,7.403504,5.698783,-4.523984,8.792085,9.022331,-0.806729,6.421142,-8.626467,-2.805287,-2.006126,-8.690091,9.256433,-1.554654,-8.395972,-2.141171,5.585517,-6.409463,1.546711,-8.591175,-4.151596,-9.913338,-2.537177,-9.234879,-5.466835,-6.437123,-6.267730,-7.936194,5.251582,6.515039,-0.524623,8.081608,1.985504,-2.194636,-5.731834,9.895593,7.639720,5.431936,4.056020,-4.917353,8.161560,-8.396605,2.388122,3.739585,0.173903,-2.294140,-2.384689,2.575278,-0.117060]], dtype = "float32")#candidate|2727|(1, 728)|const|float32
call_2726 = relay.TupleGetItem(func_141_call(relay.reshape(const_2727.astype('float32'), [8, 7, 13])), 0)
call_2728 = relay.TupleGetItem(func_143_call(relay.reshape(const_2727.astype('float32'), [8, 7, 13])), 0)
bop_2732 = relay.less_equal(const_2727.astype('bool'), relay.reshape(call_2726.astype('bool'), relay.shape_of(const_2727))) # shape=(1, 728)
bop_2735 = relay.less_equal(const_2727.astype('bool'), relay.reshape(call_2728.astype('bool'), relay.shape_of(const_2727))) # shape=(1, 728)
func_1390_call = mod.get_global_var('func_1390')
func_1392_call = mutated_mod.get_global_var('func_1392')
var_2752 = relay.var("var_2752", dtype = "float32", shape = (288,))#candidate|2752|(288,)|var|float32
call_2751 = relay.TupleGetItem(func_1390_call(relay.reshape(var_2752.astype('float32'), [8, 6, 6])), 0)
call_2753 = relay.TupleGetItem(func_1392_call(relay.reshape(var_2752.astype('float32'), [8, 6, 6])), 0)
output = relay.Tuple([call_2724,bop_2732,call_2751,var_2752,])
output2 = relay.Tuple([call_2725,bop_2735,call_2753,var_2752,])
func_2754 = relay.Function([var_2752,], output)
mod['func_2754'] = func_2754
mod = relay.transform.InferType()(mod)
mutated_mod['func_2754'] = func_2754
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2755 = relay.var("var_2755", dtype = "float32", shape = (288,))#candidate|2755|(288,)|var|float32
func_2754_call = mutated_mod.get_global_var('func_2754')
call_2756 = func_2754_call(var_2755)
output = call_2756
func_2757 = relay.Function([var_2755], output)
mutated_mod['func_2757'] = func_2757
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2815 = relay.var("var_2815", dtype = "int16", shape = (1, 16, 4))#candidate|2815|(1, 16, 4)|var|int16
const_2816 = relay.const([[[2,9,-4,1],[-4,8,9,7],[-6,3,6,-9],[1,-1,-7,-10],[-6,8,1,6],[10,-3,-1,-7],[1,-9,8,-9],[-3,7,5,8],[8,5,-7,-7],[7,10,-10,-7],[8,9,-5,6],[1,7,-3,-7],[-2,10,-5,8],[5,-2,-6,-8],[-6,-2,-3,8],[-2,-10,-1,-5]],[[1,-2,-10,-8],[10,-10,8,3],[-2,6,1,-1],[-10,-9,-10,-4],[8,7,10,-3],[-7,9,2,1],[4,1,-1,2],[5,-10,4,6],[-2,1,10,2],[-10,3,2,-4],[-9,-4,9,-2],[7,-9,-8,4],[8,3,3,3],[6,-3,-10,-5],[-4,-9,-6,7],[-5,-6,-1,-4]],[[-10,-7,2,-4],[8,9,4,6],[4,3,8,-7],[8,7,-6,2],[-10,6,-1,-4],[-10,8,6,4],[-1,4,-8,-4],[4,10,6,3],[1,10,4,2],[7,-7,-3,-7],[-7,4,9,6],[1,3,-7,3],[-10,9,-9,5],[10,2,-3,8],[7,-7,-9,-2],[-10,8,-3,-5]],[[-6,-4,-7,4],[1,3,-3,5],[-10,-8,7,9],[-7,3,8,1],[-2,2,6,-7],[1,10,-10,8],[7,-10,8,-2],[-6,2,-2,-1],[-8,4,-10,10],[2,7,-6,3],[-1,-10,4,-1],[-6,6,6,4],[2,-9,-2,6],[-8,7,8,-9],[-5,-9,10,9],[2,6,5,-3]],[[10,1,-10,6],[-10,4,-5,8],[-2,8,8,10],[3,10,-7,-6],[7,-9,-4,5],[-9,5,-1,-5],[1,-7,-1,7],[-4,-5,-1,10],[-10,-7,5,10],[2,-2,-8,8],[-10,-6,-3,-8],[-3,-7,-6,4],[-5,10,-2,6],[6,9,-4,-5],[1,9,6,10],[-2,4,6,-2]],[[7,-3,-4,5],[8,6,-8,-10],[2,-4,9,-6],[4,9,-7,3],[2,-7,6,8],[3,-7,5,-1],[-7,5,-2,6],[-4,8,-5,7],[8,6,5,9],[10,-10,-3,3],[-7,-5,1,7],[-6,7,5,-9],[-10,-6,-10,5],[-8,4,6,-1],[-6,-4,-10,2],[-5,7,5,-2]],[[2,-1,2,10],[-9,-3,-2,7],[-3,-2,-1,8],[3,5,-1,2],[4,6,9,6],[-2,10,3,9],[8,10,-6,-5],[-4,-9,-9,10],[4,9,-4,1],[4,-8,-1,-5],[-8,2,3,-5],[10,-4,4,-2],[2,6,-8,9],[-10,-1,4,4],[2,8,-3,-4],[8,2,6,4]],[[5,3,7,-5],[9,-8,5,6],[7,-5,-8,3],[-1,-8,9,4],[-2,-7,-8,-5],[-10,3,4,5],[3,4,-10,-7],[-2,-9,-1,-4],[9,1,6,6],[7,-3,9,6],[9,5,-7,-2],[1,9,-4,2],[-6,1,-9,8],[-6,-10,-1,9],[4,-1,8,9],[5,-9,1,-10]],[[-6,-7,-10,2],[-9,1,7,-10],[-5,2,-4,-1],[9,8,5,4],[-1,-8,-9,-6],[-1,8,8,10],[1,-7,3,4],[9,-1,-9,8],[8,-2,-6,-7],[7,6,-7,9],[6,-3,-5,2],[-8,-8,8,1],[-2,4,9,-7],[-9,2,-7,4],[-8,-4,-3,-6],[-9,-1,2,2]],[[-5,4,-8,-2],[1,-2,6,4],[2,-8,-6,9],[-9,-10,-4,-7],[-9,-5,-3,5],[-1,-4,5,-3],[-8,4,-5,7],[7,7,2,-10],[-6,-9,2,-4],[-2,-9,6,4],[3,6,-4,2],[-2,3,-4,4],[-8,10,6,-2],[-2,-5,-3,10],[10,-1,-1,-6],[-1,-7,-1,-6]],[[4,10,10,10],[3,8,-6,-1],[6,-1,-5,10],[-5,3,-9,-7],[-5,-5,-1,4],[-10,-9,5,-3],[1,10,10,-6],[-8,-2,-7,10],[-8,-6,-1,4],[-5,8,-2,-2],[6,1,-1,-2],[5,6,3,-2],[2,-1,-8,-4],[7,-4,-4,3],[8,7,-10,-6],[3,5,-7,-10]],[[-6,-2,7,1],[8,4,-2,4],[-1,-9,8,-4],[-7,-8,9,-5],[-8,-9,-3,-8],[6,4,8,-9],[-7,-10,4,-9],[-6,-9,-4,7],[-1,8,9,-6],[-7,-6,-8,-6],[5,-3,1,-4],[-6,1,5,-3],[-6,-4,-6,-1],[-3,-10,4,-6],[-3,8,1,-2],[-2,9,2,-8]],[[3,-3,-4,-4],[1,-8,1,4],[4,-9,-3,-2],[-5,-6,2,-5],[-8,6,3,7],[-3,1,-8,5],[6,-7,-4,-5],[9,-5,-7,-8],[9,7,1,7],[10,7,2,1],[5,-6,6,-9],[5,6,4,-1],[5,4,3,-1],[1,4,-9,9],[3,-4,-9,2],[8,-9,1,5]],[[7,3,3,4],[3,5,-3,7],[-2,-4,5,-8],[-3,5,-7,1],[2,-6,9,8],[10,-3,10,8],[10,-6,8,-8],[-2,-7,5,-5],[-4,-1,4,5],[3,-6,10,6],[8,5,-7,-10],[-7,-8,-5,-9],[-5,-1,10,-3],[-8,7,-7,-7],[6,-2,6,1],[-9,10,-9,4]]], dtype = "int16")#candidate|2816|(14, 16, 4)|const|int16
bop_2817 = relay.less(var_2815.astype('bool'), const_2816.astype('bool')) # shape=(14, 16, 4)
output = relay.Tuple([bop_2817,])
output2 = relay.Tuple([bop_2817,])
func_2821 = relay.Function([var_2815,], output)
mod['func_2821'] = func_2821
mod = relay.transform.InferType()(mod)
var_2822 = relay.var("var_2822", dtype = "int16", shape = (1, 16, 4))#candidate|2822|(1, 16, 4)|var|int16
output = func_2821(var_2822)
func_2823 = relay.Function([var_2822], output)
mutated_mod['func_2823'] = func_2823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_2860 = func_2402_call()
call_2861 = func_2402_call()
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
const_2871 = relay.const([-7.908571,-7.759037,-2.914667,2.949946,9.047865,3.069795,2.707232,-4.659342,3.752868,1.372199,-8.378532,-9.564842,0.755247,-1.626875,-6.530161,-3.229657,2.936359,6.434490,7.655051,3.838580,-3.505976,-2.210034,3.747257,-1.931591,2.907600,-1.349686,8.317243,3.038020,-6.292900,5.533633,-8.477681,3.008381,-5.369089,1.412998,5.701251,-9.915805,3.554440,5.548103,3.363670,9.409088,-2.064115,-6.993431,-7.529463,-2.269197,-1.924235,7.382859,0.995302,-5.671739,7.097795,-0.681628,-8.785490,9.974045,6.356445,4.694494,-1.714313,-1.348114,-1.610185,-2.253560,-1.622339,7.854432,-2.125645,-7.688429,9.859959,7.309611,-9.782708,-4.865492,5.162832,1.635734,-9.823067,4.747656,5.537396,3.613772,8.201478,4.480682,7.349037,-3.497856,0.031474,0.270633,8.428271,-9.177898,-7.744109,-6.813422,-7.878511,0.701669,-1.753272,1.522002,-9.237207,-3.324067,0.083239,9.244820,-3.890475,-3.500389,-9.474680,1.314040,3.394220,-5.591617,-4.293584,5.830112,-9.710010,0.290842,6.030121,-8.795669,-9.496419,9.022247,-8.302557,-9.524192,-9.387412,1.840608,-8.455918,-9.937172,-3.597877,-9.304454,-5.415041,9.999947,-8.467972,0.538308,7.350079,4.342163,-7.853323,7.411986,4.803829,-5.942426,2.690736,3.904696,-4.324265,9.026142,-8.177648,8.293950,8.912778,4.178733,0.712507,3.118976,-8.685033,-8.915195,-1.019953,-5.568441,6.260678,8.724086,-7.696936,4.697574,6.822739,7.595997,-6.123332,-4.573013,7.681417,1.660546,-0.034742,9.042312,6.316857,-0.472303,-8.053580,4.596442,8.296581,-1.576382,8.477135,-3.789807,-4.945224,-4.331830,-0.217764,-3.379034,-5.835754,-3.487386,-6.670764,-1.678561,-6.081988,0.276097,7.635461,-3.190585,-0.947059,-3.464889,-3.582990,-1.654339,-5.707702,6.370091,7.399245,-3.262817,7.359126,-5.336836,-2.243657,1.708467,2.809138,9.091786,-6.685515,2.244534,-2.997047,-7.500221,-9.482635,7.576203,-8.689978,1.260757,-3.686157,7.708049,5.518730,-5.002883,-4.603781,-7.266772,-8.458889,-0.422775,1.521526,9.110697,8.423791,5.297541,-7.076648,-8.065764,5.805189,-9.431220,2.104997,-9.112196,-2.647820,3.289996,-2.294766,-5.280025,9.513195,6.149899,8.576373,4.055391,6.030912,-3.659182,9.799481,-7.412062,0.961280,7.212581,-9.491450,6.273013,-8.709903,-8.297479,-7.858146,7.407263,8.313488,-1.863365,-1.784037,-1.793712,-9.217513,3.557448,2.098060,5.683399,5.674862,-9.752920,-0.415847,-2.343421,-5.738217,3.946582,0.829841,-1.117786,-9.127559,4.178355,-6.371116,-4.325020,7.139076,6.301961,5.738315,3.825118,5.227206,-1.906608,4.509738,-9.300478,0.919927,-6.722389,-6.562105,-9.422833,9.855392,3.030277,5.378190,7.922550,-7.116532,6.751857,6.600328,-8.523134,-5.822641,-2.974656,6.272597,7.902983,-7.260190,7.582655,9.021212,3.166442,-2.152355,-4.722300,-8.177410,-5.647866,-8.073040,-6.004393,-9.307347,-8.803236,-2.566178,-4.724889,7.804685,-2.743457,9.173876,1.586704,8.984962,4.383888,7.763174,3.278409,3.986000,-4.521363,-5.834578,7.221444,4.447186,4.796154,-7.912611,4.418576,-7.920184,-5.522936,-1.233032,-8.159134,-7.739058,3.556657,3.251928,-3.906141,-5.407659,1.412558,3.398623,7.882236,-3.093855,-1.369241,-7.405239,3.482430,-5.120695,-7.640494,5.006351,-5.324063,-9.972865,0.134029,2.560994,5.861004,9.486397,-8.625184,2.217423,9.457401,-6.014334,4.557944,-5.466898,8.429539,-1.886573,2.809637,-2.708268,2.470816,1.075491,3.317482,-5.696304,-3.101647,3.331504,5.311195,-1.378370,-1.706872,-4.652648,3.363341,-3.370328,1.185018,-0.913293,-3.296498,5.449575,9.583272,8.829942,5.632064,6.951896,4.535971,-8.279529,-8.649818,5.789811,7.292294,-0.073956,-3.694430,-7.226359,1.101080,-7.275356,6.368769,7.241944,-0.800528,6.845664,8.055657,0.894796,3.611619,1.259361,-8.437004,7.154060,-6.861196,-0.045595,-4.732190,0.240011,5.613751,-7.300754,5.502669,-7.571318,-8.867411,4.786299,-7.327685,-8.788927,-7.216994,5.421774,-0.390046,-1.805317,-3.820411,-9.371385,7.369255,-3.860726,8.442129,-6.734037,6.022729,4.853494,-7.858503,1.983455,3.459936,4.199677,9.914684,4.470890,5.084219,-1.472686,-6.110859,-0.292482,-1.547873,0.125185,1.506838,-9.859325,-5.264565,-8.191244,-4.533441,6.479394,6.366458,9.936579,-6.925861,8.104413,9.491168,1.420745,-0.928896,7.043146,8.680375,-4.226511,-8.973599,3.693755,-7.998383,-0.210922,8.815097,6.450951,-3.812224,1.287744,0.875593,-1.591623,-7.098962,-0.862813,3.119945,-3.356791,-4.452815,-4.364082,5.833082,3.437899,6.188831,1.544155,-7.342089,-1.722816,2.777336,4.606278,-0.130871,9.783380,5.655655,2.494854,-3.846095,9.124816,-0.320504,4.075984,8.870172,-6.963105,-5.840611,3.058099,-6.556737,1.876673,0.103614,-1.950373,-9.386756,6.463535,1.753207,8.998849,-6.616106,2.957072,-0.563124,-9.855153,1.425912,-4.813563,-1.612516,-9.284079,6.145227,0.600501,-9.567017,-2.971084,6.429985,0.049898,-4.283825,-7.721800,6.209244,-1.772514,1.592979,-6.717727,8.887196,-6.309299,-2.425370,-5.696205,6.504504,3.245615,1.720096,-8.815079,1.104985,9.094032,-6.693631,-0.270535,7.073287,7.184299,8.025766,-7.379679,5.939419,3.227636,8.637415,9.388295,6.990475,8.928856,4.033434,3.626368,6.076710,-3.001596,6.281037,1.148361,3.777256,7.041874,-7.207067,5.242979,-6.341517,-8.059247,-6.549860,-7.573679,-4.155375,-4.717632,-9.761266,-4.691385,3.537510,6.244540,4.603770,8.578009,-3.134611,5.066202,-5.250067,-0.787483,7.678120,8.078622,-4.453399,7.843723,3.728961,-4.374983,-9.527335,0.204288,-3.788855,-5.780595,0.991019,-2.933283,-3.101891,4.272587,6.740319,5.039433,-0.313722,-0.228134,3.783522,6.995794,-5.345307,-4.567646,-2.076712,-8.857875,-7.711902,-0.248219,-4.629595,3.889888,-6.111540,-5.041759,-4.477488,7.077423,-2.307663,-2.899865,0.955639,-6.374686,2.439415,-8.361359,-8.916508,-3.768932,0.351084,-8.197394,-6.433923,-7.737935,-1.963264,-9.752541,0.553110,9.338643,3.090121,2.668278,7.016414,-8.434711,-3.619944,-9.882412,5.619957,7.771661,6.900092,1.792223,-7.835099,4.696329,-2.652895,0.685540,7.102560,2.638893,-8.288091,4.604120,-5.774308,4.232907,2.712606,3.734151,-9.716208,7.690879,-3.264325,8.583499,9.288999,-9.894424,-1.594590,1.392748,-6.663823,4.907410,5.564258,4.949283,-3.141795,-2.180914,-6.921731,1.027885,-4.356153,9.813841,9.491453,5.808716,8.029652,-9.121993,-6.973870,9.617569,-3.726263,2.029645,4.369943,0.353961,5.113891,4.413109,1.020282,1.713258,-4.858389,-3.600917,5.613451,-9.397861,6.425024,6.088900,-8.916034,9.007830,9.285509,-5.555098,1.078328,-5.385946,1.211665,-5.939593,-4.586465,-0.799767,-6.932912,-4.254732,4.099906,-1.100131,1.168740,-8.831709,-6.505851,-5.417825,-3.406598,9.217684,-6.140987,3.864885,4.337214,-5.983794,2.724051,-7.476475,-0.592209,0.868765,6.535732,-1.244329,8.462926,-5.875041,-1.274935,7.199484,9.220700,-9.725164,1.267554,5.518837,-0.464293,-5.309179,0.629097,4.480876,-8.045877,3.796491,3.208792,-5.847508,-1.008167,-2.154964,-2.218450,0.979818,-1.153294,7.920998,1.695925,0.010508,3.670797,5.173264,-1.688331,-5.728160,-8.277088,8.302642,5.211929,-9.959937,-9.732352,7.933086,8.637947,5.350897,-4.128890,4.310730,9.313625,6.792079,-6.209951,6.115758,-6.751051,6.961840,4.276584,-9.231228,1.664564,-9.099124,9.810584], dtype = "float32")#candidate|2871|(728,)|const|float32
call_2870 = relay.TupleGetItem(func_141_call(relay.reshape(const_2871.astype('float32'), [8, 7, 13])), 0)
call_2872 = relay.TupleGetItem(func_143_call(relay.reshape(const_2871.astype('float32'), [8, 7, 13])), 0)
func_367_call = mod.get_global_var('func_367')
func_371_call = mutated_mod.get_global_var('func_371')
var_2877 = relay.var("var_2877", dtype = "bool", shape = (32,))#candidate|2877|(32,)|var|bool
var_2878 = relay.var("var_2878", dtype = "bool", shape = (288,))#candidate|2878|(288,)|var|bool
call_2876 = relay.TupleGetItem(func_367_call(relay.reshape(var_2877.astype('bool'), [1, 2, 16]), relay.reshape(var_2878.astype('bool'), [9, 2, 16]), ), 1)
call_2879 = relay.TupleGetItem(func_371_call(relay.reshape(var_2877.astype('bool'), [1, 2, 16]), relay.reshape(var_2878.astype('bool'), [9, 2, 16]), ), 1)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_2894 = func_1620_call()
call_2895 = func_1620_call()
uop_2902 = relay.log(const_2871.astype('float32')) # shape=(728,)
func_2570_call = mod.get_global_var('func_2570')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_2904 = relay.TupleGetItem(func_2570_call(), 0)
call_2905 = relay.TupleGetItem(func_2572_call(), 0)
output = relay.Tuple([call_2860,call_2870,call_2876,var_2877,var_2878,call_2894,uop_2902,call_2904,])
output2 = relay.Tuple([call_2861,call_2872,call_2879,var_2877,var_2878,call_2895,uop_2902,call_2905,])
func_2907 = relay.Function([var_2877,var_2878,], output)
mod['func_2907'] = func_2907
mod = relay.transform.InferType()(mod)
var_2908 = relay.var("var_2908", dtype = "bool", shape = (32,))#candidate|2908|(32,)|var|bool
var_2909 = relay.var("var_2909", dtype = "bool", shape = (288,))#candidate|2909|(288,)|var|bool
output = func_2907(var_2908,var_2909,)
func_2910 = relay.Function([var_2908,var_2909,], output)
mutated_mod['func_2910'] = func_2910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_2915 = relay.TupleGetItem(func_1590_call(), 0)
call_2916 = relay.TupleGetItem(func_1592_call(), 0)
func_1081_call = mod.get_global_var('func_1081')
func_1084_call = mutated_mod.get_global_var('func_1084')
const_2922 = relay.const([-9,8,-8,2,-10,-7,6,5,-5,-9,2,7,-8,-4,-9,-4,-2,4,-1,-5,1,-5,-5,-10,-1,1,7,-3,5,8,6,4,-4,9,5,6,6,-4,4,-5,-4,-10,4,-8,1,-5,-5,7,7,7,-10,1,-6,10,10,-7,-2,7,-10,-5,8,10,-8,7,4,1,-10,-9,7,8,-5,-4,-4,2,-6,7,-8,-1,5,-4,-3,3,7,-10,3,2,5,-2,-10,2,-1,2,-5,6,1,1,4,7,-7,-6,7,8,-5,-8,5,1,-9,5,-7,8,-2,-2,-4,-8,8,-3,1,6,2,-2,-3,4,9,-10,4,-4,6,3,-7,-2,6,-1,-7,-6,10,-7,-3,7,-4,-8,-4,5,8,-9,-2,1,6,-6,8,3,9,1,3,-6,4,5,4,-7,1,-9,-8,-10,2,-9,-7,-8,-2,-10,6,2,-8,7,9,6,1,1,-6,4,-7,8], dtype = "uint16")#candidate|2922|(180,)|const|uint16
call_2921 = func_1081_call(relay.reshape(const_2922.astype('uint16'), [12, 1, 15]))
call_2923 = func_1081_call(relay.reshape(const_2922.astype('uint16'), [12, 1, 15]))
output = relay.Tuple([call_2915,call_2921,const_2922,])
output2 = relay.Tuple([call_2916,call_2923,const_2922,])
func_2935 = relay.Function([], output)
mod['func_2935'] = func_2935
mod = relay.transform.InferType()(mod)
output = func_2935()
func_2936 = relay.Function([], output)
mutated_mod['func_2936'] = func_2936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2641_call = mod.get_global_var('func_2641')
func_2643_call = mutated_mod.get_global_var('func_2643')
call_2943 = relay.TupleGetItem(func_2641_call(), 4)
call_2944 = relay.TupleGetItem(func_2643_call(), 4)
func_1485_call = mod.get_global_var('func_1485')
func_1489_call = mutated_mod.get_global_var('func_1489')
var_2957 = relay.var("var_2957", dtype = "bool", shape = (24,))#candidate|2957|(24,)|var|bool
var_2958 = relay.var("var_2958", dtype = "bool", shape = (1, 360))#candidate|2958|(1, 360)|var|bool
call_2956 = relay.TupleGetItem(func_1485_call(relay.reshape(var_2957.astype('bool'), [6, 1, 4]), relay.reshape(var_2958.astype('bool'), [6, 15, 4]), ), 0)
call_2959 = relay.TupleGetItem(func_1489_call(relay.reshape(var_2957.astype('bool'), [6, 1, 4]), relay.reshape(var_2958.astype('bool'), [6, 15, 4]), ), 0)
func_454_call = mod.get_global_var('func_454')
func_458_call = mutated_mod.get_global_var('func_458')
var_2961 = relay.var("var_2961", dtype = "float64", shape = (88,))#candidate|2961|(88,)|var|float64
const_2962 = relay.const([8.292394,-2.417514,8.536884,6.185876,6.096441,3.063486,9.192873,-2.157915,-0.455461,-0.055759,-8.594522,7.279875,2.411821,3.869504,-4.147847,1.012421,-2.976898,9.936606,-0.590220,0.967393,6.851987,-3.088929,-9.306935,-7.001894,-4.562089,7.710515,-1.657023,6.782904,-1.708420,-7.192135,-9.370340,3.294495,-8.738221,-3.256217,0.822978,-8.575346,-8.109745,0.444336,-0.149466,0.959226,2.596970,3.491603,8.747873,9.120304,6.216511,-4.265373,2.523481,-6.950769,-8.144084,8.492340,-7.595664,-0.382268,-7.916803,-9.885041,6.701110,9.685789,-9.083217,-4.394695,5.358170,-9.697448,-0.852621,-4.317086,-1.370274,5.346859,5.105380,-2.828030,-2.513079,-7.717246,0.123156,6.668285,-6.557333,7.131868,1.593853,0.020594,2.767469,8.496907,-8.787093,-7.292518,-3.156343,-2.126060,-6.567499,-1.665005,3.766545,1.657638,1.069565,-7.248817,6.648370,-6.550638,4.216871,9.948671,7.655171,-3.731419,-4.833236,-2.642080,-6.238734,-1.868640,-8.326130,-8.393727,8.504619,-9.399861,-5.444051,-8.198973,-5.793822,0.769413,-1.943011,-7.760257,2.354188,-1.092781,7.582796,0.104958,5.683059,-1.592900,-2.980434,8.714374,-7.006288,-8.155914,-4.132569,-3.682069,6.808834,5.138810,-9.061348,-9.438995,-4.003018,1.499596,5.088666,-0.072256,-4.099402,-1.040658,6.151011,-2.625806,7.592357,-9.079002,-0.241289,-2.850077,-5.673640,7.122003,-3.640645,0.484255,-2.119505,-3.024145,4.279530,-8.769352,-8.867264,-7.635097,4.945996,8.383508,6.965033,-4.984831,1.045263,0.296699,-8.800660,-2.720252,-1.673156,-8.430917,9.882527,3.700566,0.451295,-5.221316,-6.986700,5.610757,-5.686813,5.440763,-6.094322,5.164630,-4.994764,-0.154924,9.943582,7.064927,-7.173599,9.350257,0.605243,-0.591004,-6.455044,-7.052604,2.810416,-4.669184,-1.634004,7.120941,-3.246027,-2.529773,1.118475,3.343343,-0.144542,2.882863,-6.955521,-1.381786,5.381865,-3.427252,0.437629,-8.916648,-8.547303,-0.579962,-1.887798,-6.037938,-4.960015,-0.299822,3.149545,1.492382,-4.656806,-3.607047,9.053449,-5.729806,3.188598,-7.773468,0.717774,2.693563,-8.321888,7.294781,2.504618,4.400162,-9.651598,5.906205,1.266372,1.750638,1.492032,2.279065,-9.982094,6.199919,-3.083101,2.399206,1.061093,-3.401392,-3.750904,-9.329424,2.725258,-8.316292,0.187341,9.210187,-9.270996,6.924716,-1.520131,-3.948896,-1.555421,-3.006495,6.868905,3.473579,-6.242709,-9.092615,6.610085,-5.921931,-4.875553,-2.257644,-9.234581,4.553560,7.787815,7.064460,6.935656,-3.330606,7.541007,-0.746523,-7.601853,4.978337,5.711170,-2.113640,5.035557,7.498497,9.826025,7.785263,4.471986,-2.415483,2.914325,-8.309000,7.941387,8.217579,5.103610,6.660929,6.634920,-2.954678,2.179334,7.081631,6.032541,-2.777085,-7.498077,5.526552,-7.663285,-1.043390,2.177183,-9.656309,-9.420229,1.146284,-1.692911,2.067601,-7.835787,-8.563323,-4.940327,-7.771858,9.771892,-8.911562,-1.124767,8.819992,2.844463,1.370127,7.469946,6.014289,8.701144,7.557332,-4.713797,5.838317,2.063864,-2.348582,9.141939,9.375365,7.091516,-7.626799,0.640701,8.957015,-5.020101,3.123067,-3.016053,1.501185,-6.843504,1.139922,1.284063,0.716862,7.973440,5.356601,-6.626574,5.830022,-6.925483,8.592296,2.211487,9.355922,9.115536,3.074543,5.557807,4.029330,-4.177544,-7.082014,1.958344,-7.053611,1.788360,8.975245,-4.679968,-9.789202,5.977267,4.253067,-4.115782,-4.177858,7.866831,4.883536,-4.435876,-8.838596,-9.754793,-6.252800,-8.219147,-6.637461,-1.313526,7.992450,-4.623608,-2.510244,-3.421861,-9.514306,-2.869902,-5.181059,9.510866,-0.974654,8.937582,-8.637816,-3.316877,3.409564,6.981313,-1.221919,-2.600379,-4.013956,8.741366,-9.183236,-1.893712,-4.697768,2.226933,6.465463,8.618574,-7.274982,-9.897685,-3.112176,3.767223,-7.317549,2.254925,4.110809,-1.490543,-5.631610,-2.335106,0.550742,8.236823,8.231782,6.938266,6.986395,-8.069824,3.214459,-5.576428,1.950461,6.366447,-0.865478,9.554084,-6.250900,-3.509439,2.147769,9.065391,7.455349,7.514373,2.519432,0.615043,5.029808,-1.617992,0.280399,-4.145212,9.397706,-6.168821,-0.720154,7.674448,4.627794,9.108561,-1.230864,-4.580654,0.868163,-6.794053,-1.434793,-3.354622,9.962794,-1.433810,1.217866,-5.125334,-4.421418,4.118604,-5.950095,-7.599236,-6.571298,-2.795819,-5.980913,-3.178708,-5.695256,5.202313,7.231050,-0.986391,-7.655551,5.181772,1.255917,-5.096437,-5.289247,-7.451860,-2.060791,-8.012525,-3.977574,4.248251,9.160509,2.153775,-6.758800,-0.548678,-8.787210,6.014629,1.181027,-6.674722,-2.693789,7.478813,-2.578874,8.618471,-0.188170,4.949136,-5.677383,6.408046,8.097998,-1.155091,9.337777,7.245128,7.234576,9.771868,1.928616,-2.907751,-0.558008,-2.481870,9.729999,-3.957415,9.387431,4.810682,-9.032799,-3.587025,7.064125,-9.141703,1.074731,-7.145572,-0.631213,-5.949649,2.946735,8.383209,-5.296975,9.761252,3.899185,5.321167,1.587666,-9.969963,0.599461,7.884186,3.460013,-6.336841,7.922414,-0.720111,-5.942892,6.757739,9.042426,9.418842,-6.676888,4.754890,-5.828614,1.545882,7.668759,-7.076800,-3.579858,1.501772,4.534034,-8.096764,-6.596521,-8.187060,0.081574,4.899431,-1.245303,-4.891822,0.122388,-1.859716,-5.808672,0.516888,1.698622,1.118143,-7.554845,-0.635783,-0.760318,-0.475212,6.161665,1.120695,6.609214,7.607055,0.113509,-3.186583,7.455218,2.850389,-0.591057,-5.869861,-4.994272,3.700999,-8.323230,-0.732161,1.080136,-0.722852,0.925232,1.419593,-6.800605,-6.622118,4.920404,-7.275455,9.082617,-0.846750,-9.214088,9.532925,-8.078544,6.697367,-7.924454,4.269156,5.805287,-3.539590,7.646404,6.358431,-9.015686,-3.073761,-7.417036,8.059622,-2.530416,-0.076047,-9.853301,7.459078,-9.291416,6.561979,-2.657470,-0.991190,-8.463143,-8.184292,4.697827,6.971391,2.854429,2.881017,-2.799825,5.132355,-0.978202,-3.381631,6.403593,-4.505931,-9.776414,8.694781,-8.743448,-5.340214,-7.813472,3.912320,-2.060090,-2.567132,-4.126713,-6.922483,-9.317556,8.301428,8.613924,9.695184,4.988810,-4.239274,8.728737,-7.878907,-7.312067,4.259069,9.895964,-9.255967,6.714668,0.443402,-8.027469,7.368350,7.942992,5.952842,-8.501419,0.194303,-3.084577,1.212990,0.739615,-8.612285,2.287668,3.985393,-8.173912,-3.082079,-2.605829,6.367947,5.179473,3.699316,1.311349,4.218558,9.820239,5.453394,2.688412,7.420117,-6.954667,-6.198320,1.456743,-0.243067,3.092673,-7.236683,-7.196347,-9.821655,-3.945812,-7.170821,-7.716991,0.165477,-4.632720,-8.424362,5.849122,3.866793,9.118397,7.456387,8.829746,-2.131354,9.642676,-9.336375,-5.744717,9.869237,-1.523851,-9.721620,-5.579860,-8.165001,-2.970518,-0.398981,-4.873328,5.200345,8.082211,4.188868,-0.716124,5.314179,-3.315017,8.884694,-7.542075,1.301658,-6.267318,9.876488,5.826167,1.165086,-2.735243,4.027633,1.755018,-4.509413,-2.879268,4.568063,4.695044,-9.106477,-9.430579,-2.969727,-9.718893,2.694791,9.859397,0.707133,-0.303619,-0.416312,-8.601485,-4.019099,-4.464296,-7.476422,-5.069974,3.138176,-3.463298,6.343896,9.231702,5.778043,1.696369,-8.753183,-5.524833,4.837841,6.011470,8.292602,3.062851,9.067808,9.436074,-9.290119,-6.255282,8.743174,3.427894,4.449548,5.163965,5.183815,-0.601965,5.933614,2.536450,9.716220,2.207743,3.117203,-8.595894,-5.118566,-7.673764,0.420248,3.592616,-5.265232,8.441379,4.602397,-4.962193,2.823414,1.678284,5.341156,8.435861,2.752227,-6.128631,-3.815522,8.753346,-4.200278,7.142451,-8.902929,-0.286098,-0.182854,2.900949,-6.164339,-5.313471,-7.466683,1.452899,-1.968361,-8.420112,8.005098,-8.827257,-8.338848,-8.871296,-3.682142,-6.982537,-3.654006,0.371417,1.354793,4.520205,-9.494917,8.379604,7.887302,0.082364,-2.354274,7.675600,-6.263201,7.724075,9.130398,2.619086,8.419217,9.446404,-6.203761,-9.594122,9.794775,-6.452824,2.391956,-2.472629,-5.761983,6.472077,4.904296,-5.462653,-6.407900,-1.469340,1.161810,3.090650,-1.688934,7.198369,0.789758,-6.810715,6.163291,2.365621,-7.765878,3.254773,9.615740,2.243568,3.243462,-3.031683,0.342254,8.413517,-4.706722,-3.263700,8.123419,2.964486,3.399882,1.332541,-0.877196,-1.573418,-4.657477,1.888562,-6.057933,6.464777,-5.213363,9.995589,-0.080359,3.737485,-8.203259,2.412372,7.333571,-2.336625,-5.128115,7.740407,-2.418544,-2.321500,8.208561,-0.913969,-0.104102,1.758204,4.974731,9.967750,5.163920,-3.145374,-9.535704,-6.039815,1.489895,-5.965607,-2.819219,-9.880500,4.198206,-5.084415,8.501582,-6.595281,-5.539341,-3.307032,7.615586,3.752119,-1.775553,-0.378909,-8.031615,-6.400624,0.207211,8.977368,-5.823456,2.173035,-6.330619,-3.615453,-9.005444,-5.865541,-8.896089,3.807960,-6.858371,9.009135,-1.454348,7.321721,-5.734398,-6.478682,-0.991508,0.915295,-0.430398,0.836940,-3.163005,-6.687857,-5.602450,2.002994,0.633960,-1.470893,-5.672728,1.410128], dtype = "float64")#candidate|2962|(880,)|const|float64
call_2960 = relay.TupleGetItem(func_454_call(relay.reshape(var_2961.astype('float64'), [1, 8, 11]), relay.reshape(const_2962.astype('float64'), [10, 8, 11]), ), 0)
call_2963 = relay.TupleGetItem(func_458_call(relay.reshape(var_2961.astype('float64'), [1, 8, 11]), relay.reshape(const_2962.astype('float64'), [10, 8, 11]), ), 0)
uop_2975 = relay.atan(const_2962.astype('float64')) # shape=(880,)
output = relay.Tuple([call_2943,call_2956,var_2957,var_2958,call_2960,var_2961,uop_2975,])
output2 = relay.Tuple([call_2944,call_2959,var_2957,var_2958,call_2963,var_2961,uop_2975,])
func_2984 = relay.Function([var_2957,var_2958,var_2961,], output)
mod['func_2984'] = func_2984
mod = relay.transform.InferType()(mod)
mutated_mod['func_2984'] = func_2984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2984_call = mutated_mod.get_global_var('func_2984')
var_2986 = relay.var("var_2986", dtype = "bool", shape = (24,))#candidate|2986|(24,)|var|bool
var_2987 = relay.var("var_2987", dtype = "bool", shape = (1, 360))#candidate|2987|(1, 360)|var|bool
var_2988 = relay.var("var_2988", dtype = "float64", shape = (88,))#candidate|2988|(88,)|var|float64
call_2985 = func_2984_call(var_2986,var_2987,var_2988,)
output = call_2985
func_2989 = relay.Function([var_2986,var_2987,var_2988,], output)
mutated_mod['func_2989'] = func_2989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_3081 = relay.TupleGetItem(func_2570_call(), 0)
call_3082 = relay.TupleGetItem(func_2572_call(), 0)
func_2293_call = mod.get_global_var('func_2293')
func_2296_call = mutated_mod.get_global_var('func_2296')
var_3100 = relay.var("var_3100", dtype = "float32", shape = (360,))#candidate|3100|(360,)|var|float32
call_3099 = relay.TupleGetItem(func_2293_call(relay.reshape(var_3100.astype('float32'), [15, 12, 2])), 2)
call_3101 = relay.TupleGetItem(func_2296_call(relay.reshape(var_3100.astype('float32'), [15, 12, 2])), 2)
output = relay.Tuple([call_3081,call_3099,var_3100,])
output2 = relay.Tuple([call_3082,call_3101,var_3100,])
func_3102 = relay.Function([var_3100,], output)
mod['func_3102'] = func_3102
mod = relay.transform.InferType()(mod)
mutated_mod['func_3102'] = func_3102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3103 = relay.var("var_3103", dtype = "float32", shape = (360,))#candidate|3103|(360,)|var|float32
func_3102_call = mutated_mod.get_global_var('func_3102')
call_3104 = func_3102_call(var_3103)
output = call_3104
func_3105 = relay.Function([var_3103], output)
mutated_mod['func_3105'] = func_3105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_3112 = func_2402_call()
call_3113 = func_2402_call()
func_3102_call = mod.get_global_var('func_3102')
func_3105_call = mutated_mod.get_global_var('func_3105')
var_3136 = relay.var("var_3136", dtype = "float32", shape = (360,))#candidate|3136|(360,)|var|float32
call_3135 = relay.TupleGetItem(func_3102_call(relay.reshape(var_3136.astype('float32'), [360,])), 0)
call_3137 = relay.TupleGetItem(func_3105_call(relay.reshape(var_3136.astype('float32'), [360,])), 0)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_3164 = relay.const([-7,-8,-4,-5,-1,5,10,-2,10,-9,6,8,9,-8,-10,-5,-3,1,3,8,-3,-9,-8,1,7,-5,-4,-5,-9,-6,-1,-8,-5,-4,5,4,2,10,-4,-9,1,-4,-5,7,-9,4,5,-6,1,1,-1,-3,-6,-4,3,3,-7,8,5,7,10,6,3,6,-4,-9,1,8,4,10,-5,-1,10,-4,7,-9,-3,10,6,2,-4,5,-3,-3,-4,4,5,-4,7,10,-3,8,-1,-4,8,-9,6,-8,-4,6,5,1,-5,7,-7,5,3,6,6,2,-3,-6,4,8,4,-10,-3,-1,8,-2,4,-2,5,-2,5,6,-7,-9,-6,-1,-10,-1,1,-3,9,-1,5,9,-1,-4,5,6,-2,-2,-3,-1,1,-8,-6,-9,-8,-8,-6,-4,8,-5,8,4,8,10,-9,4,5,-2,5,-7,-4,6,4,6,10,4,3,-7,7,2,-10,-6,2,-7,-3,-10,1,-8,-7,-6,8,-6,1,-1,3,-4,4,8,-10,-1,-9,-2,6,-5,6,2,1,-4,3,1,-3,-7,-5,-2,-1,-9,-5,-1,5,-6,7,-5,-5,-3,8,-2,-8,-9,7,-9,-4,9,3,10,5,-9,3,-3,6,-7,-9,-7,-2,-2,-6,5,3,-1,3,-4,-7,-1,8,-9,1,9,6,8,10,7,3,8,-6,-2,-10,9,1,10,-5,4,-4,5,8,-10,-3,6,6,4,5,-3,4,4,4,-3,-2,5,9,-8,3,-5,4,4,5,4,-4,7,-10,1,5,-3,2,-3,-7,-8,-10,7,-4,3,-9,-3,5,10,1,9,7,2,-9,-2,5,-7,5,-8,6,-2,8,7,5,1,9,1,4,-7,6,1,1,8,-3,7,-8,4,4,3,9,5,-6,5,-8,4,4,-7,5,-1,4,10,6,-1,-5,10,-8,3,-9,-3,1,-3,3,1,7,-8,9,6,2,-6,2,3,10,6,-4,-8,-6,-1,-3,9,-4,3,-5,-1,-6,5,4,8,4,5,4,-5,6,-1,10,-9,9,8,-10,-2,-7,-2,7,-6,5,10,-7,-10,-5,-10,-3,1,-10,7,-9,4,-7,6,-8,6,-4,-1,-5,1,-3,5,9,-9,7,9,-8,10,1,9,8,3,4,-10,6,-9,2,7,1,2,-6,2,4,-7,-9,6,-4,9,4,6,-1,-1,2,4,-5,-1,-7,-3,6,8,10,5,3,-1,3,7,6,-7,-9,10,-7,-5,6,7,-1,9,9,5,-8,-6,-8,5,4,-10,4,7,3,-8,-3,10,10,-5,-5,-10,1,-6,-1,-10,-4,8,-4,-1,-8,-5,4,4,9,2,4,-7,-7,1,-5,-5,-5,8,9,-4,8,5,-9,7,-2,9,2,8], dtype = "uint32")#candidate|3164|(528,)|const|uint32
call_3163 = relay.TupleGetItem(func_1330_call(relay.reshape(const_3164.astype('uint32'), [6, 11, 8])), 1)
call_3165 = relay.TupleGetItem(func_1332_call(relay.reshape(const_3164.astype('uint32'), [6, 11, 8])), 1)
func_367_call = mod.get_global_var('func_367')
func_371_call = mutated_mod.get_global_var('func_371')
var_3176 = relay.var("var_3176", dtype = "bool", shape = (32, 1))#candidate|3176|(32, 1)|var|bool
const_3177 = relay.const([True,True,False,True,False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True], dtype = "bool")#candidate|3177|(288,)|const|bool
call_3175 = relay.TupleGetItem(func_367_call(relay.reshape(var_3176.astype('bool'), [1, 2, 16]), relay.reshape(const_3177.astype('bool'), [9, 2, 16]), ), 1)
call_3178 = relay.TupleGetItem(func_371_call(relay.reshape(var_3176.astype('bool'), [1, 2, 16]), relay.reshape(const_3177.astype('bool'), [9, 2, 16]), ), 1)
output = relay.Tuple([call_3112,call_3135,var_3136,call_3163,const_3164,call_3175,var_3176,const_3177,])
output2 = relay.Tuple([call_3113,call_3137,var_3136,call_3165,const_3164,call_3178,var_3176,const_3177,])
func_3179 = relay.Function([var_3136,var_3176,], output)
mod['func_3179'] = func_3179
mod = relay.transform.InferType()(mod)
var_3180 = relay.var("var_3180", dtype = "float32", shape = (360,))#candidate|3180|(360,)|var|float32
var_3181 = relay.var("var_3181", dtype = "bool", shape = (32, 1))#candidate|3181|(32, 1)|var|bool
output = func_3179(var_3180,var_3181,)
func_3182 = relay.Function([var_3180,var_3181,], output)
mutated_mod['func_3182'] = func_3182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_3206 = func_1620_call()
call_3207 = func_1620_call()
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
const_3210 = relay.const([[8.664577,-1.348548,-5.129643,-4.116181,7.041512,3.644458,3.330211,7.210126,0.028292,-8.759815,-6.882849,6.348314,-9.854775,4.202614,-0.453651,9.412467,-7.288163,4.141018,2.235521,8.427751,1.301453,-8.430808,5.281706,-4.611098,-3.032121,9.730613,7.851303,8.166951,7.927397,-9.801174,7.835850,2.653833,0.281595,-9.173083,-9.428918,-0.653478,9.570757,-1.709026,-8.477240,8.520437,-7.249588,0.134018,-1.905969,7.452069,3.851495,1.756179,0.541091,-9.484895,8.598346,9.655762,-5.020745,1.369407],[-1.241586,-9.629653,-6.206467,2.789638,6.984021,-2.643502,7.862742,0.995570,-8.358615,-1.294519,-8.008095,-5.222905,3.461690,0.345136,9.985094,9.011005,5.465069,-1.545140,-1.119867,-8.791981,-7.795927,0.430479,-5.216722,-4.793970,3.762926,-9.655967,3.246867,8.313923,2.403358,8.868705,4.759922,-8.935205,-2.124986,-4.292647,4.202255,-2.363569,6.964660,8.320530,7.806923,-9.744921,-0.969297,-9.307974,-2.474073,0.842967,-7.836703,-2.978183,7.911092,-3.908913,-4.419494,-1.785359,9.444053,5.245036],[-8.370787,-4.796577,2.964807,-0.243484,-3.751176,6.663212,-7.532560,-7.902621,1.433225,-5.632698,2.654825,8.248659,8.279851,1.371725,-3.788164,-2.082205,-5.903302,-3.932022,9.613126,0.659672,0.272094,-8.846063,2.004513,5.349419,-3.164692,-5.266206,-2.108149,9.236759,4.430970,5.035346,1.523459,2.160764,-9.044492,2.389686,-2.642124,7.108359,-1.254984,-9.046594,-1.351298,-1.537978,3.328408,2.649477,-2.334058,-2.143152,7.124118,-3.450906,4.347225,-1.444789,4.088778,7.968506,3.839321,-7.808903],[1.652848,3.071727,-0.281360,-0.159703,-9.963301,8.569249,-9.896830,5.511824,9.275536,-8.316882,8.272742,8.128621,3.391631,-4.870049,3.659101,-3.009999,0.883694,9.959081,3.554853,-1.800044,7.614848,4.122948,1.432070,5.270813,-3.738264,1.492140,6.744395,-6.086797,2.155267,3.560194,8.081137,3.582277,8.642201,-3.153066,-7.112473,6.178049,6.627298,2.776565,3.417194,2.342740,2.863595,5.008893,8.670913,1.383562,-3.323158,-9.430366,-6.266801,5.720283,-2.180571,-4.677546,-4.994276,-9.636797],[-4.125872,-1.926459,-0.281664,8.596823,-5.844967,-8.648944,5.072183,-8.742033,-5.756509,5.153598,9.306659,9.024641,4.391624,-7.467744,2.389771,2.354062,7.468283,6.224219,9.475835,9.711452,2.852077,-2.187024,4.033855,-5.114410,7.221221,-1.427309,-4.017988,-5.281206,4.453596,4.601719,7.564007,6.637019,-7.398223,-5.203468,2.863494,4.347263,-2.412471,2.857828,9.749603,4.817665,-7.954916,2.018356,5.791111,-4.589256,-6.514920,8.786873,-7.947423,-4.049550,8.767503,-1.826325,-2.548217,8.407468],[7.341459,-2.568741,5.701248,4.628655,3.557257,-7.830514,-1.653254,-9.729343,1.790473,-7.857687,-8.958749,-8.610694,-4.100655,-9.036225,7.322152,6.365095,8.149551,3.621874,4.243121,-2.157333,9.382332,-9.227573,7.457444,-8.399358,-7.182848,-2.936296,-7.162163,1.485635,9.583547,6.996447,0.186263,-1.646904,4.783985,1.512662,-4.925174,2.523500,5.213343,-3.282540,-2.644770,2.826760,9.064613,8.529101,-7.466174,-7.904539,0.587105,-9.298666,-3.175343,4.414072,-9.459413,7.047471,-4.333493,-3.746014],[-6.111785,-9.334145,-3.197053,7.939730,0.014802,1.185729,4.281719,0.420350,4.203080,-0.426241,-0.857155,5.493732,-9.528231,-9.077669,-4.713188,-2.938964,1.228135,8.103332,-0.908231,7.978240,-7.439136,-1.605224,6.737714,-2.107705,1.327800,-1.927273,-2.742373,9.168370,-1.970458,2.649927,-5.034620,4.354103,-6.813069,2.211719,-9.233797,-7.589166,4.931068,-8.887309,-3.849454,-3.813636,1.946633,-5.008206,-6.246177,8.299713,8.695270,4.950831,-0.210036,6.345600,-8.748031,-5.051306,4.475281,6.568256],[2.833742,6.752029,-4.971393,7.765145,7.555840,1.527845,1.227650,-2.213216,9.103600,3.068762,8.306062,-4.994261,1.324391,-3.347858,8.680297,-5.517203,0.924485,-5.567588,4.642185,-9.057738,0.613510,-4.982723,-9.947282,5.208940,6.121584,0.571852,1.824451,-0.058069,-4.859689,-1.612870,-5.021646,-0.492312,-7.539780,6.866279,8.619397,-5.626098,3.604308,4.801533,-9.560639,2.803443,4.072672,-9.214034,-1.339789,-1.563142,2.942486,-5.370004,7.933053,7.169645,5.522704,1.723355,-5.308147,-1.850522],[-4.159741,5.999388,-8.174003,-3.698306,-1.536242,7.867051,0.493957,8.809656,-9.783732,-5.929893,2.741915,6.509045,-9.141645,7.803744,5.029709,-2.009962,7.374141,-2.224057,-3.771732,-6.572780,4.312039,4.355185,2.907362,6.002156,-4.982224,4.340308,3.856537,5.572095,6.705747,3.769300,-7.643916,-9.051542,9.686783,7.773143,-1.661961,-2.640196,8.266040,-5.678463,9.494482,-6.684033,-1.947652,6.150596,8.344903,7.580964,3.435508,9.477318,2.358146,3.801109,-9.971791,-0.470718,-1.574302,-2.231450],[2.492408,-3.006663,-2.858995,-6.379461,-8.460729,-2.117260,-0.960817,-3.111076,-4.840136,2.756734,-5.009115,2.302003,-8.508727,9.340318,-9.379287,-0.886923,-7.960634,-5.152275,-5.690919,4.811816,-3.325581,-3.030821,-9.957141,-4.153927,-5.395975,-1.021361,8.391700,1.998898,7.537942,-5.039770,-5.636950,6.184033,-1.717377,1.516176,3.796169,7.513211,-3.082486,-1.652764,8.793990,-2.702029,3.945852,-7.390320,-8.920437,-3.576750,-7.845178,4.829396,1.489823,8.306907,3.131909,-9.244121,-9.661448,-2.141451],[9.404123,0.034186,-5.166118,-8.617169,-2.551293,-4.579369,-1.647445,-0.753289,5.089125,2.610645,3.565857,-9.316888,4.647499,3.634255,8.870093,5.075785,-6.756798,5.490688,-8.630725,-9.181565,-8.894934,9.122482,8.558688,4.411927,0.953122,-2.225349,2.160716,7.032382,8.557770,-7.323240,5.624583,-7.072572,-7.541678,-7.228240,5.898992,6.444724,3.296568,9.520761,6.706617,8.775854,4.631052,3.420671,5.534652,-8.962557,8.082203,4.640830,-6.335216,-2.986184,8.493429,7.325285,-7.597348,-0.148962],[5.532003,-4.315486,-3.791211,7.350457,0.187893,-7.184013,-8.297319,-9.665734,-6.362885,-2.434865,6.172346,0.161178,4.489614,8.160065,-6.982508,6.946862,7.971644,-9.810987,9.428969,-5.947718,-4.884864,5.620415,9.429261,-9.682731,3.795268,-5.999325,0.411809,2.862300,-3.006730,-3.489972,-3.360139,-0.932204,-1.228733,6.624145,-1.146353,-0.501865,0.973367,4.330363,9.489958,-8.826549,-6.529641,1.888623,-9.307089,-7.455916,-6.689238,7.558379,-8.301406,-3.673370,-9.334339,8.127016,7.287974,3.036012],[3.235695,6.374353,-1.027974,-8.881540,-5.251218,6.480822,-9.334163,8.530513,-0.603437,-7.559030,-9.670467,0.476793,-6.453481,-9.183266,6.035064,-4.633844,-7.062506,9.113461,1.066254,-2.652669,-7.776152,3.448096,9.668560,6.213430,4.668185,9.031797,-9.151622,2.203955,3.982241,6.327420,4.354487,3.060878,3.671836,0.336209,-1.289233,3.799618,1.273351,-8.566488,8.731189,-0.478043,0.485050,9.382486,4.412598,-8.231018,-1.954511,3.704417,-3.783366,8.657004,7.704225,-6.209671,-5.909680,-4.313720],[-7.137799,2.455973,-5.287879,3.888117,5.765165,-7.657364,8.045095,8.695296,-6.418811,6.018695,7.397361,-4.141348,1.947472,4.261310,-5.118024,0.952954,-1.021741,9.947906,5.326835,-9.631905,0.792232,1.917622,1.427326,-6.236467,0.640173,-2.237436,-7.944175,8.705950,-6.886595,-5.860431,6.593715,1.564368,-6.339601,-8.927521,1.636854,-7.496323,3.853199,3.972779,-2.304024,-1.092055,-6.266351,-7.310903,-7.615793,-3.872084,-8.124510,2.529541,6.351291,3.772030,1.585441,9.304659,-2.341466,0.255513]], dtype = "float32")#candidate|3210|(14, 52)|const|float32
call_3209 = relay.TupleGetItem(func_141_call(relay.reshape(const_3210.astype('float32'), [8, 7, 13])), 0)
call_3211 = relay.TupleGetItem(func_143_call(relay.reshape(const_3210.astype('float32'), [8, 7, 13])), 0)
output = relay.Tuple([call_3206,call_3209,const_3210,])
output2 = relay.Tuple([call_3207,call_3211,const_3210,])
func_3219 = relay.Function([], output)
mod['func_3219'] = func_3219
mod = relay.transform.InferType()(mod)
mutated_mod['func_3219'] = func_3219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3219_call = mutated_mod.get_global_var('func_3219')
call_3220 = func_3219_call()
output = call_3220
func_3221 = relay.Function([], output)
mutated_mod['func_3221'] = func_3221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_3252 = relay.TupleGetItem(func_2162_call(), 0)
call_3253 = relay.TupleGetItem(func_2164_call(), 0)
func_3179_call = mod.get_global_var('func_3179')
func_3182_call = mutated_mod.get_global_var('func_3182')
var_3299 = relay.var("var_3299", dtype = "float32", shape = (360,))#candidate|3299|(360,)|var|float32
const_3300 = relay.const([[True,True],[False,True],[True,False],[False,False],[True,True],[True,False],[True,False],[False,True],[True,True],[False,False],[False,True],[True,True],[True,False],[True,True],[False,False],[True,False]], dtype = "bool")#candidate|3300|(16, 2)|const|bool
call_3298 = relay.TupleGetItem(func_3179_call(relay.reshape(var_3299.astype('float32'), [360,]), relay.reshape(const_3300.astype('bool'), [32, 1]), ), 2)
call_3301 = relay.TupleGetItem(func_3182_call(relay.reshape(var_3299.astype('float32'), [360,]), relay.reshape(const_3300.astype('bool'), [32, 1]), ), 2)
output = relay.Tuple([call_3252,call_3298,var_3299,const_3300,])
output2 = relay.Tuple([call_3253,call_3301,var_3299,const_3300,])
func_3304 = relay.Function([var_3299,], output)
mod['func_3304'] = func_3304
mod = relay.transform.InferType()(mod)
mutated_mod['func_3304'] = func_3304
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3305 = relay.var("var_3305", dtype = "float32", shape = (360,))#candidate|3305|(360,)|var|float32
func_3304_call = mutated_mod.get_global_var('func_3304')
call_3306 = func_3304_call(var_3305)
output = call_3306
func_3307 = relay.Function([var_3305], output)
mutated_mod['func_3307'] = func_3307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_3354 = func_2402_call()
call_3355 = func_2402_call()
output = call_3354
output2 = call_3355
func_3358 = relay.Function([], output)
mod['func_3358'] = func_3358
mod = relay.transform.InferType()(mod)
output = func_3358()
func_3359 = relay.Function([], output)
mutated_mod['func_3359'] = func_3359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2935_call = mod.get_global_var('func_2935')
func_2936_call = mutated_mod.get_global_var('func_2936')
call_3368 = relay.TupleGetItem(func_2935_call(), 0)
call_3369 = relay.TupleGetItem(func_2936_call(), 0)
output = relay.Tuple([call_3368,])
output2 = relay.Tuple([call_3369,])
func_3383 = relay.Function([], output)
mod['func_3383'] = func_3383
mod = relay.transform.InferType()(mod)
mutated_mod['func_3383'] = func_3383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3383_call = mutated_mod.get_global_var('func_3383')
call_3384 = func_3383_call()
output = call_3384
func_3385 = relay.Function([], output)
mutated_mod['func_3385'] = func_3385
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3410 = relay.const([[[0.033982,-1.151208],[8.817543,3.839422],[-7.768893,5.457009]],[[-7.062228,9.529127],[-7.543960,-6.719433],[0.067011,-3.073294]],[[8.633831,-7.903328],[-7.765070,-2.556612],[-3.144051,-1.916018]],[[6.744317,1.835042],[8.602386,3.395700],[-9.703141,7.565872]],[[9.509122,4.781975],[-0.557635,-5.763220],[-2.355135,2.741795]],[[-0.200633,-0.484522],[9.907057,2.502086],[5.553126,-1.495601]],[[3.184989,-2.480025],[4.797537,-5.603632],[6.303217,5.797491]],[[-8.722726,1.222908],[-8.589696,6.927246],[-9.489062,6.732465]],[[-8.820177,6.447930],[2.786439,1.946413],[9.674838,-9.086410]],[[0.505493,3.521178],[5.761795,3.951766],[-3.135161,-0.421194]],[[9.374782,7.711549],[1.616700,6.722688],[6.418809,4.866097]],[[5.545796,2.060087],[-7.219367,2.023535],[8.078681,-0.156217]],[[7.150636,-6.802883],[-2.505693,-5.338798],[-3.373751,-3.886494]],[[1.576918,-4.212964],[-8.391262,8.088460],[-1.421438,-0.637542]],[[6.177455,-4.284430],[-9.834288,9.122551],[-0.558529,3.332053]],[[-7.161487,2.470724],[9.242851,-2.141585],[8.277097,-6.366237]]], dtype = "float32")#candidate|3410|(16, 3, 2)|const|float32
uop_3411 = relay.log10(const_3410.astype('float32')) # shape=(16, 3, 2)
uop_3416 = relay.log(const_3410.astype('float32')) # shape=(16, 3, 2)
output = relay.Tuple([uop_3411,uop_3416,])
output2 = relay.Tuple([uop_3411,uop_3416,])
func_3425 = relay.Function([], output)
mod['func_3425'] = func_3425
mod = relay.transform.InferType()(mod)
mutated_mod['func_3425'] = func_3425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3425_call = mutated_mod.get_global_var('func_3425')
call_3426 = func_3425_call()
output = call_3426
func_3427 = relay.Function([], output)
mutated_mod['func_3427'] = func_3427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_3428 = relay.TupleGetItem(func_1885_call(), 2)
call_3429 = relay.TupleGetItem(func_1887_call(), 2)
output = relay.Tuple([call_3428,])
output2 = relay.Tuple([call_3429,])
func_3431 = relay.Function([], output)
mod['func_3431'] = func_3431
mod = relay.transform.InferType()(mod)
output = func_3431()
func_3432 = relay.Function([], output)
mutated_mod['func_3432'] = func_3432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3358_call = mod.get_global_var('func_3358')
func_3359_call = mutated_mod.get_global_var('func_3359')
call_3438 = func_3358_call()
call_3439 = func_3358_call()
uop_3461 = relay.acos(call_3438.astype('float32')) # shape=(88,)
uop_3463 = relay.acos(call_3439.astype('float32')) # shape=(88,)
uop_3496 = relay.atanh(uop_3461.astype('float32')) # shape=(88,)
uop_3498 = relay.atanh(uop_3463.astype('float32')) # shape=(88,)
uop_3507 = relay.cos(uop_3496.astype('float64')) # shape=(88,)
uop_3509 = relay.cos(uop_3498.astype('float64')) # shape=(88,)
output = relay.Tuple([uop_3507,])
output2 = relay.Tuple([uop_3509,])
func_3510 = relay.Function([], output)
mod['func_3510'] = func_3510
mod = relay.transform.InferType()(mod)
output = func_3510()
func_3511 = relay.Function([], output)
mutated_mod['func_3511'] = func_3511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3358_call = mod.get_global_var('func_3358')
func_3359_call = mutated_mod.get_global_var('func_3359')
call_3538 = func_3358_call()
call_3539 = func_3358_call()
output = relay.Tuple([call_3538,])
output2 = relay.Tuple([call_3539,])
func_3540 = relay.Function([], output)
mod['func_3540'] = func_3540
mod = relay.transform.InferType()(mod)
mutated_mod['func_3540'] = func_3540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3540_call = mutated_mod.get_global_var('func_3540')
call_3541 = func_3540_call()
output = call_3541
func_3542 = relay.Function([], output)
mutated_mod['func_3542'] = func_3542
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3551 = relay.var("var_3551", dtype = "bool", shape = (6, 3, 1))#candidate|3551|(6, 3, 1)|var|bool
var_3552 = relay.var("var_3552", dtype = "bool", shape = (6, 3, 11))#candidate|3552|(6, 3, 11)|var|bool
bop_3553 = relay.logical_or(var_3551.astype('bool'), var_3552.astype('bool')) # shape=(6, 3, 11)
uop_3558 = relay.log(var_3552.astype('float32')) # shape=(6, 3, 11)
bop_3570 = relay.not_equal(uop_3558.astype('bool'), relay.reshape(var_3552.astype('bool'), relay.shape_of(uop_3558))) # shape=(6, 3, 11)
bop_3577 = relay.multiply(var_3551.astype('int32'), bop_3553.astype('int32')) # shape=(6, 3, 11)
bop_3581 = relay.greater_equal(uop_3558.astype('bool'), relay.reshape(bop_3577.astype('bool'), relay.shape_of(uop_3558))) # shape=(6, 3, 11)
output = relay.Tuple([bop_3570,bop_3581,])
output2 = relay.Tuple([bop_3570,bop_3581,])
func_3593 = relay.Function([var_3551,var_3552,], output)
mod['func_3593'] = func_3593
mod = relay.transform.InferType()(mod)
var_3594 = relay.var("var_3594", dtype = "bool", shape = (6, 3, 1))#candidate|3594|(6, 3, 1)|var|bool
var_3595 = relay.var("var_3595", dtype = "bool", shape = (6, 3, 11))#candidate|3595|(6, 3, 11)|var|bool
output = func_3593(var_3594,var_3595,)
func_3596 = relay.Function([var_3594,var_3595,], output)
mutated_mod['func_3596'] = func_3596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_3678 = relay.TupleGetItem(func_2318_call(), 0)
call_3679 = relay.TupleGetItem(func_2319_call(), 0)
func_2935_call = mod.get_global_var('func_2935')
func_2936_call = mutated_mod.get_global_var('func_2936')
call_3699 = relay.TupleGetItem(func_2935_call(), 2)
call_3700 = relay.TupleGetItem(func_2936_call(), 2)
func_2754_call = mod.get_global_var('func_2754')
func_2757_call = mutated_mod.get_global_var('func_2757')
var_3721 = relay.var("var_3721", dtype = "float32", shape = (288,))#candidate|3721|(288,)|var|float32
call_3720 = relay.TupleGetItem(func_2754_call(relay.reshape(var_3721.astype('float32'), [288,])), 2)
call_3722 = relay.TupleGetItem(func_2757_call(relay.reshape(var_3721.astype('float32'), [288,])), 2)
func_1561_call = mod.get_global_var('func_1561')
func_1563_call = mutated_mod.get_global_var('func_1563')
call_3735 = func_1561_call()
call_3736 = func_1561_call()
func_2402_call = mod.get_global_var('func_2402')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_3767 = func_2402_call()
call_3768 = func_2402_call()
output = relay.Tuple([call_3678,call_3699,call_3720,var_3721,call_3735,call_3767,])
output2 = relay.Tuple([call_3679,call_3700,call_3722,var_3721,call_3736,call_3768,])
func_3786 = relay.Function([var_3721,], output)
mod['func_3786'] = func_3786
mod = relay.transform.InferType()(mod)
mutated_mod['func_3786'] = func_3786
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3787 = relay.var("var_3787", dtype = "float32", shape = (288,))#candidate|3787|(288,)|var|float32
func_3786_call = mutated_mod.get_global_var('func_3786')
call_3788 = func_3786_call(var_3787)
output = call_3788
func_3789 = relay.Function([var_3787], output)
mutated_mod['func_3789'] = func_3789
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3880 = relay.const([[[-4,1,-5,4],[-3,8,-1,-4],[-1,7,3,8],[-9,4,7,-4],[-8,-2,-2,-4],[1,1,-2,9],[1,5,-7,7],[-5,-10,4,-3],[8,7,4,-5],[3,8,-10,1],[3,5,-10,6],[3,8,-9,-2]],[[-6,7,10,6],[-7,-1,3,8],[7,-8,8,-2],[1,8,1,-6],[-9,-1,-6,-10],[-1,-2,2,-2],[5,-8,7,4],[2,-9,4,-1],[10,-9,9,9],[-10,-6,-3,1],[-2,1,-1,-7],[-8,5,4,4]],[[8,-10,3,-6],[-2,-7,-3,-3],[9,4,10,2],[-10,2,1,-9],[9,7,-1,-7],[7,8,-4,7],[-4,5,4,3],[-2,-9,-1,3],[10,-2,-5,5],[-4,-4,-3,-4],[-5,10,6,-5],[-8,-3,-5,-9]],[[-6,-7,1,-3],[-7,3,-1,7],[-6,5,-10,-8],[7,9,8,8],[-10,-7,8,-6],[-8,-5,6,2],[8,-1,8,-9],[3,-6,8,6],[-10,1,-4,3],[7,-10,-9,-4],[2,7,9,2],[4,4,3,-1]],[[5,-10,-2,1],[-2,-2,-5,-10],[-4,-4,3,-4],[7,10,-7,10],[-7,-1,3,8],[-2,8,9,-4],[-7,7,-8,8],[8,-3,10,-9],[4,-6,1,-4],[-4,-2,-4,-9],[7,-2,6,8],[9,3,5,-6]],[[9,7,6,4],[-8,5,3,3],[-2,2,-5,6],[-4,-3,8,-1],[1,-6,1,-7],[6,-1,7,-6],[-8,-9,-3,-9],[1,-7,3,-5],[-5,-1,2,-5],[1,-5,9,9],[2,-4,-2,-1],[7,1,5,4]],[[8,-8,3,-7],[9,-3,5,-10],[10,1,9,7],[9,5,6,6],[5,6,-7,-2],[-7,7,-7,-9],[2,-2,-2,-6],[9,-7,-3,10],[-6,7,9,10],[-4,-8,-5,-9],[6,8,10,-9],[9,3,10,1]],[[-10,-9,-8,5],[-9,3,7,-3],[-3,1,6,4],[9,-9,-1,-4],[1,-7,4,10],[-2,-7,7,4],[-10,-5,8,-6],[-5,5,-9,6],[-2,-8,-5,-10],[-3,10,7,-10],[-2,7,-2,-6],[-10,-4,9,9]],[[-5,8,7,-8],[4,-10,3,-10],[-3,-4,2,6],[2,10,-2,-3],[-6,-6,8,5],[2,-3,-3,10],[9,-5,-6,2],[-2,1,1,-2],[4,2,-2,4],[-10,10,9,3],[4,9,-8,-7],[-3,-6,-4,-1]],[[-4,2,2,1],[2,-7,-1,-9],[8,-6,8,7],[-4,4,-1,6],[-2,5,-4,-5],[-10,-7,3,-8],[3,7,7,-1],[-9,9,-3,-9],[-5,6,1,-8],[-4,-1,-3,9],[-1,7,4,-1],[4,5,6,2]],[[-8,-1,-10,9],[-5,4,-9,4],[-1,10,-9,-8],[-10,2,-9,-7],[3,-8,-6,8],[9,-7,-6,10],[2,-3,-10,3],[6,-6,-10,-1],[-1,-5,-8,-8],[6,5,8,1],[3,8,7,-5],[-9,-9,4,-1]],[[1,-3,10,3],[-9,-9,-4,-5],[-4,-2,6,-5],[8,3,4,-10],[9,-3,5,4],[6,2,-4,7],[-2,9,6,-3],[8,8,-8,-8],[-2,-6,8,-2],[3,-4,-1,-3],[10,10,-7,-2],[-9,-10,9,-3]],[[-10,-9,-9,5],[-6,-7,10,9],[3,9,4,-7],[-4,-9,-5,-5],[1,5,4,2],[-9,-7,8,-2],[-7,2,-2,2],[8,-8,-6,-9],[-6,9,-6,-2],[-7,-5,-6,9],[-8,5,-2,6],[10,2,-9,-5]]], dtype = "uint64")#candidate|3880|(13, 12, 4)|const|uint64
const_3881 = relay.const([[[3,-5,-2,10],[7,-8,-5,-3],[-8,-9,1,9],[-10,-5,2,-10],[-3,-7,-6,-6],[4,-7,-9,-5],[-5,7,-2,-1],[-3,-5,-2,-7],[2,9,-10,10],[-10,-2,-7,8],[-1,7,-9,6],[-9,-6,-9,-5]],[[6,8,10,9],[-5,9,-8,-4],[-1,-2,3,2],[-2,2,-3,10],[-4,5,-6,-2],[-7,-5,-7,4],[1,-8,-6,6],[-1,7,9,3],[-10,5,-5,9],[9,7,-4,-6],[6,1,6,-8],[-8,-3,6,10]],[[6,-2,-4,3],[4,1,-10,4],[1,-6,5,-6],[-2,-1,4,-4],[9,-1,6,6],[3,-9,2,-9],[-1,2,10,10],[-6,2,-4,-2],[4,-6,7,-2],[9,5,9,6],[8,7,-5,-2],[1,3,-2,-10]],[[8,7,-8,-8],[-4,-10,-7,-2],[-2,3,-7,-8],[-2,-4,6,3],[10,1,-10,-6],[-4,-5,3,-3],[6,4,-4,-2],[5,-1,1,-7],[3,-10,-7,-9],[-5,9,4,6],[-2,5,-5,2],[-4,3,6,-6]],[[-7,6,-5,4],[-9,-9,-7,-5],[5,4,-9,-4],[-9,10,-6,-6],[5,7,-7,1],[4,-1,4,1],[-7,1,-1,-3],[-3,-8,9,4],[-8,-5,3,-2],[-5,9,2,1],[7,7,9,10],[3,3,-4,8]],[[-9,8,3,9],[5,-9,10,-8],[2,-6,-5,4],[-4,2,5,9],[-6,-8,-7,7],[6,10,-6,4],[-4,-2,5,-9],[-5,7,2,6],[1,7,10,9],[-9,-4,5,-4],[8,-10,-2,-2],[-1,-8,4,-10]],[[-5,-10,-10,3],[-6,-6,-4,-2],[6,5,-2,-6],[-7,3,-8,4],[-10,8,-3,-9],[7,2,6,4],[-5,-4,10,-7],[4,-10,-4,6],[1,4,-7,5],[-10,5,-10,-10],[2,1,3,10],[-1,-2,5,1]],[[-1,1,7,2],[-4,5,-10,10],[-8,3,-2,-3],[-3,8,-10,-7],[-3,1,-6,-9],[-1,-6,-9,2],[-9,1,10,-4],[6,3,10,-10],[-10,-5,3,-9],[-8,7,1,-5],[4,2,1,-9],[8,4,3,3]],[[5,2,-1,4],[7,-7,9,-1],[-9,9,8,6],[1,6,-3,7],[-6,-6,9,-4],[-9,7,2,-5],[10,8,3,6],[3,-5,-10,4],[1,-10,-8,-9],[7,7,3,-10],[-5,4,2,1],[1,-2,10,4]],[[-6,4,-9,2],[-10,-5,10,-7],[-4,4,-1,1],[-1,-3,-1,-2],[1,2,10,8],[-3,-2,-8,8],[2,-8,-7,6],[-6,-10,-6,-5],[-10,-9,-10,-10],[-1,4,3,-3],[-5,9,4,1],[4,6,-6,9]],[[5,-8,-6,-8],[3,8,5,3],[6,2,-9,7],[-6,3,3,2],[1,-3,-10,-6],[4,-1,7,8],[7,-3,-5,-10],[-3,-5,-7,6],[-6,-5,-1,-9],[6,1,7,-9],[9,1,-2,5],[7,4,6,4]],[[-9,8,1,-5],[1,-2,-5,-1],[1,-8,-6,-10],[2,9,-4,-2],[3,4,-9,-10],[-5,7,3,2],[-3,-9,-5,3],[5,-7,-4,-3],[-9,10,-6,-8],[-3,10,-4,-10],[-5,7,-7,7],[-10,-10,-5,1]],[[2,4,2,-10],[7,-2,4,-10],[-2,1,5,3],[4,2,-8,3],[-4,1,-9,4],[-3,-8,8,-10],[-3,2,-8,-5],[-8,-2,-2,10],[2,-4,4,-8],[4,-8,2,-5],[-6,4,1,6],[8,10,5,-6]]], dtype = "uint64")#candidate|3881|(13, 12, 4)|const|uint64
bop_3882 = relay.bitwise_or(const_3880.astype('uint64'), relay.reshape(const_3881.astype('uint64'), relay.shape_of(const_3880))) # shape=(13, 12, 4)
output = bop_3882
output2 = bop_3882
func_3886 = relay.Function([], output)
mod['func_3886'] = func_3886
mod = relay.transform.InferType()(mod)
output = func_3886()
func_3887 = relay.Function([], output)
mutated_mod['func_3887'] = func_3887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_3953 = relay.TupleGetItem(func_2162_call(), 1)
call_3954 = relay.TupleGetItem(func_2164_call(), 1)
output = call_3953
output2 = call_3954
func_3965 = relay.Function([], output)
mod['func_3965'] = func_3965
mod = relay.transform.InferType()(mod)
mutated_mod['func_3965'] = func_3965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3965_call = mutated_mod.get_global_var('func_3965')
call_3966 = func_3965_call()
output = call_3966
func_3967 = relay.Function([], output)
mutated_mod['func_3967'] = func_3967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3383_call = mod.get_global_var('func_3383')
func_3385_call = mutated_mod.get_global_var('func_3385')
call_3986 = relay.TupleGetItem(func_3383_call(), 0)
call_3987 = relay.TupleGetItem(func_3385_call(), 0)
output = call_3986
output2 = call_3987
func_3994 = relay.Function([], output)
mod['func_3994'] = func_3994
mod = relay.transform.InferType()(mod)
mutated_mod['func_3994'] = func_3994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mutated_mod.get_global_var('func_3994')
call_3995 = func_3994_call()
output = call_3995
func_3996 = relay.Function([], output)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_3997 = func_3965_call()
call_3998 = func_3965_call()
output = relay.Tuple([call_3997,])
output2 = relay.Tuple([call_3998,])
func_4032 = relay.Function([], output)
mod['func_4032'] = func_4032
mod = relay.transform.InferType()(mod)
mutated_mod['func_4032'] = func_4032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4032_call = mutated_mod.get_global_var('func_4032')
call_4033 = func_4032_call()
output = call_4033
func_4034 = relay.Function([], output)
mutated_mod['func_4034'] = func_4034
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_4101 = relay.TupleGetItem(func_1885_call(), 1)
call_4102 = relay.TupleGetItem(func_1887_call(), 1)
func_3886_call = mod.get_global_var('func_3886')
func_3887_call = mutated_mod.get_global_var('func_3887')
call_4104 = func_3886_call()
call_4105 = func_3886_call()
output = relay.Tuple([call_4101,call_4104,])
output2 = relay.Tuple([call_4102,call_4105,])
func_4135 = relay.Function([], output)
mod['func_4135'] = func_4135
mod = relay.transform.InferType()(mod)
output = func_4135()
func_4136 = relay.Function([], output)
mutated_mod['func_4136'] = func_4136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3510_call = mod.get_global_var('func_3510')
func_3511_call = mutated_mod.get_global_var('func_3511')
call_4170 = relay.TupleGetItem(func_3510_call(), 0)
call_4171 = relay.TupleGetItem(func_3511_call(), 0)
output = call_4170
output2 = call_4171
func_4179 = relay.Function([], output)
mod['func_4179'] = func_4179
mod = relay.transform.InferType()(mod)
output = func_4179()
func_4180 = relay.Function([], output)
mutated_mod['func_4180'] = func_4180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3358_call = mod.get_global_var('func_3358')
func_3359_call = mutated_mod.get_global_var('func_3359')
call_4183 = func_3358_call()
call_4184 = func_3358_call()
func_3994_call = mod.get_global_var('func_3994')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_4190 = func_3994_call()
call_4191 = func_3994_call()
output = relay.Tuple([call_4183,call_4190,])
output2 = relay.Tuple([call_4184,call_4191,])
func_4236 = relay.Function([], output)
mod['func_4236'] = func_4236
mod = relay.transform.InferType()(mod)
mutated_mod['func_4236'] = func_4236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4236_call = mutated_mod.get_global_var('func_4236')
call_4237 = func_4236_call()
output = call_4237
func_4238 = relay.Function([], output)
mutated_mod['func_4238'] = func_4238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4236_call = mod.get_global_var('func_4236')
func_4238_call = mutated_mod.get_global_var('func_4238')
call_4257 = relay.TupleGetItem(func_4236_call(), 0)
call_4258 = relay.TupleGetItem(func_4238_call(), 0)
output = call_4257
output2 = call_4258
func_4263 = relay.Function([], output)
mod['func_4263'] = func_4263
mod = relay.transform.InferType()(mod)
mutated_mod['func_4263'] = func_4263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4263_call = mutated_mod.get_global_var('func_4263')
call_4264 = func_4263_call()
output = call_4264
func_4265 = relay.Function([], output)
mutated_mod['func_4265'] = func_4265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2641_call = mod.get_global_var('func_2641')
func_2643_call = mutated_mod.get_global_var('func_2643')
call_4298 = relay.TupleGetItem(func_2641_call(), 3)
call_4299 = relay.TupleGetItem(func_2643_call(), 3)
const_4303 = relay.const([-4.953525,-6.903060,-3.759904,9.228699,-1.840022,8.306942,-8.310225,-4.442524,-3.351418,2.372568,2.267001,4.619813,7.626310,-2.546974,-9.449979,3.260467,0.282189,0.174763,-0.167544,-5.314523,6.251054,-9.441094,7.454853,-6.802492,8.203005,-1.021435,-5.135056,-9.190573,4.087064,-2.165568,9.058128,-7.258481,-8.751173,-2.391954,-0.560652,6.832616,-6.840241,-0.022944,-1.868305,-0.269889,-3.263775,-1.827920,-9.203976,-7.354281,5.929303,3.515964,-4.974268,-0.336263,3.800443,-5.177783,6.204682,-3.923400,4.572100,4.194572,7.999653,5.997091,-2.314788,-4.093917,-4.016432,5.763901,7.097083,-8.594398,-9.518796,-9.506132,-5.753272,-5.533067,-4.448799,7.844567,1.213316,8.657714,-6.957117,-8.748233,2.237220,-5.696793,-1.421654,8.936980,-3.082182,9.597037,-1.850319,2.606474,-0.341294,2.276277,-5.351542,-3.402074,4.388377,-2.675703,-5.081859,8.427472,4.736281,-7.788450,2.901472,7.659068,3.610004,-8.813003,9.701388,-2.959659,6.553370,-5.016223,2.742747,2.055132,9.377545,-3.793222,9.825152,6.225615,6.295835,-8.094561,3.211483,3.844896,-4.373901,8.729504,4.433733,-5.776294,5.231510,-1.142978,4.050553,3.804838,6.358925,7.516436,9.390574,1.066048,-3.735537,5.725784,9.901839,-7.453124,0.549569,0.191320,-4.803949,7.813696,1.605291,-0.209950], dtype = "float32")#candidate|4303|(130,)|const|float32
bop_4304 = relay.floor_divide(call_4298.astype('float64'), relay.reshape(const_4303.astype('float64'), relay.shape_of(call_4298))) # shape=(130,)
bop_4307 = relay.floor_divide(call_4299.astype('float64'), relay.reshape(const_4303.astype('float64'), relay.shape_of(call_4299))) # shape=(130,)
bop_4308 = relay.bitwise_or(bop_4304.astype('int32'), relay.reshape(call_4298.astype('int32'), relay.shape_of(bop_4304))) # shape=(130,)
bop_4311 = relay.bitwise_or(bop_4307.astype('int32'), relay.reshape(call_4299.astype('int32'), relay.shape_of(bop_4307))) # shape=(130,)
output = bop_4308
output2 = bop_4311
func_4320 = relay.Function([], output)
mod['func_4320'] = func_4320
mod = relay.transform.InferType()(mod)
mutated_mod['func_4320'] = func_4320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4320_call = mutated_mod.get_global_var('func_4320')
call_4321 = func_4320_call()
output = call_4321
func_4322 = relay.Function([], output)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4135_call = mod.get_global_var('func_4135')
func_4136_call = mutated_mod.get_global_var('func_4136')
call_4387 = relay.TupleGetItem(func_4135_call(), 0)
call_4388 = relay.TupleGetItem(func_4136_call(), 0)
output = relay.Tuple([call_4387,])
output2 = relay.Tuple([call_4388,])
func_4400 = relay.Function([], output)
mod['func_4400'] = func_4400
mod = relay.transform.InferType()(mod)
output = func_4400()
func_4401 = relay.Function([], output)
mutated_mod['func_4401'] = func_4401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_4407 = relay.TupleGetItem(func_1885_call(), 0)
call_4408 = relay.TupleGetItem(func_1887_call(), 0)
const_4413 = relay.const([[[-2.374341,-0.004192,3.829166,3.405337,9.938215,-1.847127,-8.219138,-2.194044,-4.729901,-9.786851,-4.623080],[7.879903,2.154920,-9.008040,9.797995,3.003721,-7.956522,-3.980246,-8.346293,1.117281,7.152635,1.028766]],[[-0.014902,8.251838,-6.491079,-2.690508,-5.830708,-1.261326,-2.423439,-8.580522,-5.278451,3.175243,-4.872024],[-7.638008,3.798263,-1.261537,8.184819,-2.483708,1.501482,7.720274,-0.811044,8.537501,3.731113,-8.528756]],[[-3.231299,6.510712,-7.293828,0.231001,-1.913884,4.874193,0.730740,-3.436574,-0.195667,7.532230,-4.631332],[4.926884,-2.229037,6.608637,-8.370970,7.443198,2.707133,-0.950480,6.740309,-8.417960,2.774587,3.547493]],[[7.264220,-7.951164,5.499782,8.742115,-7.905506,-5.832460,5.796884,-9.080738,1.402340,5.947129,-2.426046],[6.252691,1.706145,7.493011,8.051938,-3.310129,-8.483304,-2.252017,-2.130338,6.321695,6.179857,8.835962]],[[0.660358,-2.577459,1.942074,2.201383,8.490317,1.941767,-3.253114,-5.564633,9.064016,-4.127253,1.285098],[1.954524,4.731224,-9.950161,-6.230905,0.102250,6.229273,6.946866,4.549021,-8.165729,8.916597,-1.773432]],[[-9.155306,4.663372,8.286027,3.237543,1.640345,-1.145080,1.377973,1.336854,-1.901695,7.430849,-7.791051],[-3.131022,-6.852798,6.610570,-7.302933,6.256410,-7.920789,-1.941542,5.754331,-7.536802,6.590671,0.646167]],[[1.430118,-0.467647,4.662386,6.952243,-5.516213,-2.837648,-3.351835,-9.714756,6.267116,6.804143,4.113745],[0.171572,5.060401,3.499277,-4.641266,1.855975,4.499200,6.295375,9.881477,-5.628060,-9.167915,-3.266072]],[[-9.612001,7.719332,5.151542,4.595752,-6.022978,3.748530,-1.436868,-6.938173,3.001378,-4.917009,-4.248773],[8.299755,-0.642905,5.494187,-5.789973,8.352903,9.153661,-9.752303,6.951741,7.247969,-9.492808,0.511144]],[[5.532116,0.030391,0.168047,8.780986,5.185493,-8.689661,-2.986347,-9.466051,0.236418,-4.725338,-7.616118],[7.494090,-7.479731,-1.891876,6.511686,-8.305185,5.675929,8.591574,7.976032,-5.650408,-3.719510,4.715641]],[[2.330168,2.608246,3.718559,0.336892,4.869983,-8.472214,1.441332,-6.124783,-0.914078,4.501583,1.995870],[5.068676,4.205524,8.934284,-7.671892,-4.782988,8.689600,-6.981575,2.250809,-9.540603,0.389264,9.112548]],[[0.938154,6.045226,-9.124427,-9.093019,-1.183872,-0.184427,5.629427,0.067142,-2.629146,1.816032,5.829494],[1.940385,5.921166,0.152589,-4.111096,1.171638,6.158526,5.707787,8.632735,2.620458,3.152595,5.840155]]], dtype = "float32")#candidate|4413|(11, 2, 11)|const|float32
bop_4414 = relay.right_shift(call_4407.astype('uint8'), relay.reshape(const_4413.astype('uint8'), relay.shape_of(call_4407))) # shape=(11, 2, 11)
bop_4417 = relay.right_shift(call_4408.astype('uint8'), relay.reshape(const_4413.astype('uint8'), relay.shape_of(call_4408))) # shape=(11, 2, 11)
output = bop_4414
output2 = bop_4417
func_4421 = relay.Function([], output)
mod['func_4421'] = func_4421
mod = relay.transform.InferType()(mod)
mutated_mod['func_4421'] = func_4421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mutated_mod.get_global_var('func_4421')
call_4422 = func_4421_call()
output = call_4422
func_4423 = relay.Function([], output)
mutated_mod['func_4423'] = func_4423
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mod.get_global_var('func_3994')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_4438 = func_3994_call()
call_4439 = func_3994_call()
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_4443 = relay.TupleGetItem(func_1590_call(), 0)
call_4444 = relay.TupleGetItem(func_1592_call(), 0)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
var_4455 = relay.var("var_4455", dtype = "uint32", shape = (4, 132))#candidate|4455|(4, 132)|var|uint32
call_4454 = relay.TupleGetItem(func_1330_call(relay.reshape(var_4455.astype('uint32'), [6, 11, 8])), 1)
call_4456 = relay.TupleGetItem(func_1332_call(relay.reshape(var_4455.astype('uint32'), [6, 11, 8])), 1)
bop_4458 = relay.logical_or(var_4455.astype('bool'), relay.reshape(call_4454.astype('bool'), relay.shape_of(var_4455))) # shape=(4, 132)
bop_4461 = relay.logical_or(var_4455.astype('bool'), relay.reshape(call_4456.astype('bool'), relay.shape_of(var_4455))) # shape=(4, 132)
uop_4470 = relay.exp(call_4454.astype('float32')) # shape=(6, 11, 8)
uop_4472 = relay.exp(call_4456.astype('float32')) # shape=(6, 11, 8)
output = relay.Tuple([call_4438,call_4443,bop_4458,uop_4470,])
output2 = relay.Tuple([call_4439,call_4444,bop_4461,uop_4472,])
func_4480 = relay.Function([var_4455,], output)
mod['func_4480'] = func_4480
mod = relay.transform.InferType()(mod)
var_4481 = relay.var("var_4481", dtype = "uint32", shape = (4, 132))#candidate|4481|(4, 132)|var|uint32
output = func_4480(var_4481)
func_4482 = relay.Function([var_4481], output)
mutated_mod['func_4482'] = func_4482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_4495 = func_3965_call()
call_4496 = func_3965_call()
output = call_4495
output2 = call_4496
func_4498 = relay.Function([], output)
mod['func_4498'] = func_4498
mod = relay.transform.InferType()(mod)
output = func_4498()
func_4499 = relay.Function([], output)
mutated_mod['func_4499'] = func_4499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4320_call = mod.get_global_var('func_4320')
func_4322_call = mutated_mod.get_global_var('func_4322')
call_4528 = func_4320_call()
call_4529 = func_4320_call()
output = relay.Tuple([call_4528,])
output2 = relay.Tuple([call_4529,])
func_4530 = relay.Function([], output)
mod['func_4530'] = func_4530
mod = relay.transform.InferType()(mod)
mutated_mod['func_4530'] = func_4530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mutated_mod.get_global_var('func_4530')
call_4531 = func_4530_call()
output = call_4531
func_4532 = relay.Function([], output)
mutated_mod['func_4532'] = func_4532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3994_call = mod.get_global_var('func_3994')
func_3996_call = mutated_mod.get_global_var('func_3996')
call_4550 = func_3994_call()
call_4551 = func_3994_call()
func_4400_call = mod.get_global_var('func_4400')
func_4401_call = mutated_mod.get_global_var('func_4401')
call_4552 = relay.TupleGetItem(func_4400_call(), 0)
call_4553 = relay.TupleGetItem(func_4401_call(), 0)
func_1819_call = mod.get_global_var('func_1819')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_4554 = relay.TupleGetItem(func_1819_call(relay.reshape(call_4550.astype('float32'), [11, 2, 11])), 0)
call_4555 = relay.TupleGetItem(func_1822_call(relay.reshape(call_4550.astype('float32'), [11, 2, 11])), 0)
func_3358_call = mod.get_global_var('func_3358')
func_3359_call = mutated_mod.get_global_var('func_3359')
call_4559 = func_3358_call()
call_4560 = func_3358_call()
func_3102_call = mod.get_global_var('func_3102')
func_3105_call = mutated_mod.get_global_var('func_3105')
var_4580 = relay.var("var_4580", dtype = "float32", shape = (2, 180))#candidate|4580|(2, 180)|var|float32
call_4579 = relay.TupleGetItem(func_3102_call(relay.reshape(var_4580.astype('float32'), [360,])), 2)
call_4581 = relay.TupleGetItem(func_3105_call(relay.reshape(var_4580.astype('float32'), [360,])), 2)
func_2984_call = mod.get_global_var('func_2984')
func_2989_call = mutated_mod.get_global_var('func_2989')
const_4609 = relay.const([False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True], dtype = "bool")#candidate|4609|(24,)|const|bool
call_4608 = relay.TupleGetItem(func_2984_call(relay.reshape(const_4609.astype('bool'), [24,]), relay.reshape(call_4579.astype('bool'), [1, 360]), relay.reshape(call_4559.astype('float64'), [88,]), ), 4)
call_4610 = relay.TupleGetItem(func_2989_call(relay.reshape(const_4609.astype('bool'), [24,]), relay.reshape(call_4579.astype('bool'), [1, 360]), relay.reshape(call_4559.astype('float64'), [88,]), ), 4)
func_1330_call = mod.get_global_var('func_1330')
func_1332_call = mutated_mod.get_global_var('func_1332')
const_4615 = relay.const([[2,6,1,-7,6,3,-3,-7,9,-1,-10,-4,-4,-8,1,-10,-1,-6,-8,5,2,-8,-6,-1,8,5,10,-8,4,-9,-4,-9,5,5,-10,-7,-8,-7,-2,9,-10,-6,6,9,2,5,6,8,1,7,4,6,-1,-6,3,2,2,6,-2,7,2,7,-6,-1,10,10],[4,-8,1,7,-9,-5,-7,-6,7,-2,-5,-9,5,10,10,1,-8,-8,-1,10,3,1,-10,8,10,6,-10,8,5,-3,10,6,1,6,8,-3,3,3,-1,-9,-1,-8,-8,-8,-6,7,-5,3,-8,9,5,8,-6,-1,2,-9,3,-3,6,5,4,-10,-6,6,-4,-1],[-9,-8,10,1,7,4,-9,-4,-10,-9,-2,3,1,-3,4,-3,1,-7,1,2,10,-2,4,-6,-5,-7,1,7,9,7,2,-8,3,5,-3,-4,4,4,1,10,-2,-5,1,6,-9,-5,5,5,9,4,10,7,-3,10,10,2,-1,6,8,-1,-5,10,-2,-7,-7,-4],[-10,-1,-3,-9,-4,-6,7,-6,4,-1,-8,8,-8,-2,8,3,7,3,6,-5,-4,-7,5,-5,3,-7,-9,-10,1,-3,7,9,2,8,-5,-10,5,7,1,10,-9,4,3,-4,-7,5,3,-2,5,4,-10,-8,-10,-5,-8,4,2,-3,5,1,-6,-7,-10,5,6,7],[4,3,10,-6,4,6,-1,3,8,-7,10,-3,-3,-8,-10,7,8,-9,-9,-7,-8,-3,3,2,-1,6,-2,-4,9,-4,-6,-2,-2,-5,7,-7,6,-3,-5,-2,3,10,9,10,5,-9,-8,7,6,-2,3,-10,-7,-8,8,-1,-10,-6,-4,-10,-4,-1,-2,2,-10,2],[4,-10,7,-5,10,5,6,8,10,10,7,-6,-2,8,5,-3,6,-1,-3,-5,4,-2,1,-10,-8,-5,-2,5,-3,5,-6,6,2,-2,-6,10,9,10,-2,3,1,-6,-10,8,-3,-1,1,-1,-7,-10,2,-2,-3,-2,-3,6,2,-6,2,-6,-6,6,-6,-10,1,-7],[1,-5,2,-9,10,-6,9,5,-7,-8,9,8,-2,10,8,6,7,-4,-7,-3,-10,9,2,-1,-6,1,3,-3,-6,8,-10,-3,-4,-7,10,7,-10,9,10,-10,9,4,-1,-8,-9,2,1,-10,2,7,7,2,-10,-9,1,9,-1,3,-9,8,9,9,5,6,-7,1],[-7,-9,-4,-9,8,-6,-10,-2,3,-7,1,-4,-7,6,-3,6,-10,7,3,-10,4,9,-8,-3,10,5,5,-8,10,-6,10,5,7,1,-9,-1,8,9,3,-9,1,4,3,-10,-7,8,-8,-5,-6,-7,9,8,-1,7,8,-7,-10,-4,-7,8,9,-1,-10,4,-3,8]], dtype = "uint32")#candidate|4615|(8, 66)|const|uint32
call_4614 = relay.TupleGetItem(func_1330_call(relay.reshape(const_4615.astype('uint32'), [6, 11, 8])), 1)
call_4616 = relay.TupleGetItem(func_1332_call(relay.reshape(const_4615.astype('uint32'), [6, 11, 8])), 1)
func_141_call = mod.get_global_var('func_141')
func_143_call = mutated_mod.get_global_var('func_143')
var_4618 = relay.var("var_4618", dtype = "float32", shape = (728,))#candidate|4618|(728,)|var|float32
call_4617 = relay.TupleGetItem(func_141_call(relay.reshape(var_4618.astype('float32'), [8, 7, 13])), 0)
call_4619 = relay.TupleGetItem(func_143_call(relay.reshape(var_4618.astype('float32'), [8, 7, 13])), 0)
output = relay.Tuple([call_4550,call_4552,call_4554,call_4559,call_4579,var_4580,call_4608,const_4609,call_4614,const_4615,call_4617,var_4618,])
output2 = relay.Tuple([call_4551,call_4553,call_4555,call_4560,call_4581,var_4580,call_4610,const_4609,call_4616,const_4615,call_4619,var_4618,])
func_4625 = relay.Function([var_4580,var_4618,], output)
mod['func_4625'] = func_4625
mod = relay.transform.InferType()(mod)
mutated_mod['func_4625'] = func_4625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4625_call = mutated_mod.get_global_var('func_4625')
var_4627 = relay.var("var_4627", dtype = "float32", shape = (2, 180))#candidate|4627|(2, 180)|var|float32
var_4628 = relay.var("var_4628", dtype = "float32", shape = (728,))#candidate|4628|(728,)|var|float32
call_4626 = func_4625_call(var_4627,var_4628,)
output = call_4626
func_4629 = relay.Function([var_4627,var_4628,], output)
mutated_mod['func_4629'] = func_4629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mod.get_global_var('func_4530')
func_4532_call = mutated_mod.get_global_var('func_4532')
call_4639 = relay.TupleGetItem(func_4530_call(), 0)
call_4640 = relay.TupleGetItem(func_4532_call(), 0)
func_3102_call = mod.get_global_var('func_3102')
func_3105_call = mutated_mod.get_global_var('func_3105')
const_4642 = relay.const([2.758050,4.757649,-1.354004,-2.943539,-0.018079,-1.567320,-2.895248,2.708474,-0.592039,6.401358,-1.569603,0.076091,-2.407015,3.221350,-1.399745,-6.138463,6.899963,0.641623,0.479718,7.342592,5.737402,8.325563,-6.233577,-5.424741,1.029747,-6.329998,5.313974,-3.359445,-9.827504,-6.235209,5.105415,-8.455678,-6.326327,-9.705925,6.110498,-2.955982,0.880707,-9.560595,-9.235799,-4.251467,-8.093894,5.382720,-6.890307,-7.795091,-9.493298,8.180915,9.269989,-8.796551,-8.917400,6.257073,5.304935,-2.566758,4.185501,-6.806397,7.073159,-0.346754,7.176901,3.319715,9.454881,-1.302718,-9.181576,4.498583,3.198697,-2.050546,1.780751,6.965354,9.278369,7.529789,-3.748812,-1.361592,0.878260,6.587685,-5.639899,-9.826269,-4.363859,9.490554,0.587289,-1.836500,9.279018,-3.869907,-4.123083,0.787584,7.041480,0.266144,-0.181419,2.303117,-7.488587,-1.755216,7.064733,-7.225417,4.229999,1.884981,4.295292,2.326496,-0.016182,2.327620,2.791349,-0.488336,2.620176,-3.211007,9.244695,0.488992,-7.742154,-0.374020,9.339429,-2.702891,1.572481,9.643420,3.963337,7.223529,-2.703313,3.923901,0.211060,-7.874375,5.286063,-9.183770,-4.737321,-9.253363,2.706597,-1.844043,5.222450,0.607424,-5.077994,2.059796,6.603054,2.651797,9.494903,6.556355,-6.606777,-9.678305,-7.590584,-2.647116,-0.761136,0.256188,-0.064205,-1.952920,-2.357391,-5.289379,-8.435171,1.165134,-7.165999,6.729204,3.506366,-5.690950,-3.577640,3.251215,0.191115,2.269968,-3.003651,9.542248,6.816680,-5.407100,7.761410,-1.864783,9.013622,3.513415,2.031606,2.013638,1.404273,-7.359728,-9.160093,-2.994876,-1.021785,-6.894462,-2.001923,1.050196,8.292004,-9.827374,-6.093043,6.008806,-6.166297,4.119508,3.534543,-7.825547,-9.672967,0.476461,-1.967137,-2.477053,6.372383,9.147648,-9.015054,8.151907,-2.195579,-6.039095,1.349503,-8.590928,-6.361643,8.187878,7.253281,-4.773657,-6.781637,-3.781820,8.451780,1.763517,2.335350,-3.031816,8.134350,-3.373747,0.404616,-4.918323,-6.373313,-4.447408,-9.565577,-6.795855,0.843829,6.472663,-2.926999,-0.693280,-5.621435,6.378766,-7.775336,1.881020,6.784160,-0.211791,-1.446671,2.418712,8.903545,6.201185,3.078819,8.153266,-6.496510,3.614642,6.998275,-1.721456,1.528465,3.664702,-3.852243,-9.973560,-5.179213,-1.032727,5.058019,4.664953,-2.488097,1.584345,3.666088,-5.490463,9.725853,-8.927107,-9.788545,8.037014,-2.898737,6.309789,3.752856,8.040012,-3.218776,5.069725,1.650705,5.992994,8.191695,-8.779505,2.363402,2.846346,-7.919048,5.645539,-0.635107,-4.150646,-3.319080,7.852553,4.198332,7.463633,6.874354,-1.239369,-5.733233,-8.240843,-7.553230,-6.701206,5.894632,-0.423164,6.570810,-4.303518,-9.788705,8.652269,5.442280,6.766405,0.878891,-7.132434,7.424906,9.102639,-8.266543,1.299841,-7.974728,2.595439,2.635105,1.353326,8.967363,6.830461,6.832540,-7.052835,1.235481,1.486684,1.543267,8.676269,-0.265293,-5.683966,-4.323310,9.376005,9.119609,7.789241,6.502472,7.759297,-5.839789,-9.081489,2.030562,-5.420916,-4.151830,6.002166,-0.106285,-9.579129,-9.558286,9.273107,1.624980,6.555126,1.372556,1.315767,-0.921232,-0.742668,0.557034,-5.592906,0.086477,-6.700628,-1.575938,4.120749,-9.260604,-0.010486,-6.190884,-3.698031,-4.705978,-3.739877,-8.741343,-6.218600,0.258076,4.792671,-9.704807,5.757265,0.541168,0.364476,-9.301047,-2.481747,8.885068,9.517156,-1.520041,8.668574,8.938630,5.990128,4.470661,-4.499975,-0.839151,-2.873784,1.626178,-7.463129,2.663816,6.080703,8.731759,-7.068024,-9.841242,-9.842682,3.236336,8.877450,-7.465831,-7.551261], dtype = "float32")#candidate|4642|(360,)|const|float32
call_4641 = relay.TupleGetItem(func_3102_call(relay.reshape(const_4642.astype('float32'), [360,])), 2)
call_4643 = relay.TupleGetItem(func_3105_call(relay.reshape(const_4642.astype('float32'), [360,])), 2)
func_1885_call = mod.get_global_var('func_1885')
func_1887_call = mutated_mod.get_global_var('func_1887')
call_4650 = relay.TupleGetItem(func_1885_call(), 0)
call_4651 = relay.TupleGetItem(func_1887_call(), 0)
uop_4654 = relay.acos(const_4642.astype('float64')) # shape=(360,)
output = relay.Tuple([call_4639,call_4641,call_4650,uop_4654,])
output2 = relay.Tuple([call_4640,call_4643,call_4651,uop_4654,])
func_4680 = relay.Function([], output)
mod['func_4680'] = func_4680
mod = relay.transform.InferType()(mod)
mutated_mod['func_4680'] = func_4680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4680_call = mutated_mod.get_global_var('func_4680')
call_4681 = func_4680_call()
output = call_4681
func_4682 = relay.Function([], output)
mutated_mod['func_4682'] = func_4682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_4683 = func_4421_call()
call_4684 = func_4421_call()
func_1655_call = mod.get_global_var('func_1655')
func_1656_call = mutated_mod.get_global_var('func_1656')
call_4690 = func_1655_call()
call_4691 = func_1655_call()
func_4680_call = mod.get_global_var('func_4680')
func_4682_call = mutated_mod.get_global_var('func_4682')
call_4692 = relay.TupleGetItem(func_4680_call(), 1)
call_4693 = relay.TupleGetItem(func_4682_call(), 1)
uop_4703 = relay.cos(call_4692.astype('float64')) # shape=(360,)
uop_4705 = relay.cos(call_4693.astype('float64')) # shape=(360,)
uop_4706 = relay.acosh(call_4690.astype('float64')) # shape=(11, 2, 11)
uop_4708 = relay.acosh(call_4691.astype('float64')) # shape=(11, 2, 11)
func_3540_call = mod.get_global_var('func_3540')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_4717 = relay.TupleGetItem(func_3540_call(), 0)
call_4718 = relay.TupleGetItem(func_3542_call(), 0)
func_1390_call = mod.get_global_var('func_1390')
func_1392_call = mutated_mod.get_global_var('func_1392')
const_4720 = relay.const([6.562375,1.211848,-8.407183,8.322929,-1.866260,-5.925647,-9.472282,-3.629905,-1.213802,0.347089,-5.142232,-2.345621,-1.944663,-9.505001,8.366537,-9.827950,-5.441479,-1.906070,2.398443,-1.390979,-8.426902,-5.701116,-9.174235,-9.956285,0.115550,3.129676,8.513103,-8.367285,-6.622874,-0.962383,-9.447351,5.824905,-5.918153,-2.226505,5.144711,5.051855,6.651100,-0.407480,-7.048437,-9.429450,-9.032095,2.740558,0.641670,-5.861888,2.788458,-1.904468,8.832022,-8.841318,7.313153,3.129254,0.789736,9.252100,9.387364,6.576667,-9.749821,1.564020,5.681060,4.546525,-7.033322,-2.053345,-3.653754,-6.112180,-2.982035,5.290402,4.165195,-2.497168,4.486493,0.607980,-7.614087,8.058638,-6.564817,6.864257,5.749948,-4.311717,-0.058437,8.965404,2.922729,8.352018,-6.811667,-8.346765,3.324005,1.967152,-0.503885,7.425555,9.419675,6.879576,-4.873482,0.370511,5.685471,3.606580,-3.353778,-3.697524,-1.523910,-6.703871,-5.357569,-6.927970,6.854651,9.030676,-2.835220,-9.061146,9.436664,9.859901,3.797488,9.088168,6.386254,-0.435872,-3.893696,3.462802,-3.584806,3.986882,-8.532535,7.317718,7.629244,9.886802,5.609591,9.226713,-8.424972,-2.693137,1.426348,-3.615743,3.008854,1.646978,-9.573141,-5.370780,-0.562881,6.356113,-0.625929,-6.006689,7.989107,0.881572,-3.844057,4.748030,-2.131859,-5.914654,-0.085379,-1.280390,5.558846,3.107323,-6.973595,1.693209,1.054342,-6.038755,9.075638,-0.289344,-2.857418,3.125594,-9.202042,8.805347,0.841299,6.737995,3.260111,7.298242,6.639019,-1.145062,-8.354591,-6.608677,-7.329381,0.714022,0.270747,2.024618,-8.230984,-8.375460,6.228102,9.622317,3.461931,-9.541918,-4.742562,-3.394205,-8.006256,2.793723,-6.204233,6.710095,-1.965275,-1.098627,-3.128174,-0.996091,-4.701201,5.324770,-6.285509,-9.965121,4.606124,-0.903967,-1.295624,5.136762,4.391997,-7.172798,-3.094377,6.933052,-4.456059,3.154615,0.776615,4.104441,-4.472119,6.319167,8.283238,9.952754,0.924403,-2.600829,-4.947998,-5.028105,2.116314,5.216704,-0.768483,-6.621768,-5.209227,9.399732,9.071441,9.648981,-3.329710,1.530381,2.744201,-9.077354,-1.068213,-3.768059,6.256549,0.903687,6.171449,-5.886113,8.737777,0.189288,-1.441678,0.707443,8.732395,-3.353519,1.115902,-8.906241,-1.821149,9.493131,4.608252,3.035061,4.632901,7.868689,6.158637,-1.659111,9.821510,-7.102963,1.780207,5.058420,-4.501277,-9.603173,4.823721,-3.155536,9.032182,0.919777,-8.696493,0.921626,5.230966,-2.451029,1.987843,6.682325,-5.725357,-9.296526,6.830587,5.399592,5.118616,3.764212,-1.631176,-9.385033,-1.596599,-6.849282,-8.812037,-5.538253,3.033190,-4.537754,2.914749,7.710744,3.964369,9.236888,6.541511,8.207053,-8.775561,-0.469626,-7.344304,9.998318,-4.225370,2.503720,1.614836,-1.769448,2.165866,2.589085,-0.607534,-4.762660,5.198072,-5.635266,-7.391198,2.296341,-6.266651,1.556833], dtype = "float32")#candidate|4720|(288,)|const|float32
call_4719 = relay.TupleGetItem(func_1390_call(relay.reshape(const_4720.astype('float32'), [8, 6, 6])), 0)
call_4721 = relay.TupleGetItem(func_1392_call(relay.reshape(const_4720.astype('float32'), [8, 6, 6])), 0)
output = relay.Tuple([call_4683,uop_4703,uop_4706,call_4717,call_4719,const_4720,])
output2 = relay.Tuple([call_4684,uop_4705,uop_4708,call_4718,call_4721,const_4720,])
func_4727 = relay.Function([], output)
mod['func_4727'] = func_4727
mod = relay.transform.InferType()(mod)
output = func_4727()
func_4728 = relay.Function([], output)
mutated_mod['func_4728'] = func_4728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_4768 = func_4421_call()
call_4769 = func_4421_call()
output = call_4768
output2 = call_4769
func_4791 = relay.Function([], output)
mod['func_4791'] = func_4791
mod = relay.transform.InferType()(mod)
mutated_mod['func_4791'] = func_4791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4791_call = mutated_mod.get_global_var('func_4791')
call_4792 = func_4791_call()
output = call_4792
func_4793 = relay.Function([], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_4831 = func_3965_call()
call_4832 = func_3965_call()
const_4833 = relay.const([[7,4,-5,4,-1,4,3,9,-7,5,-5,3,-3,6,4,4,7,5,2,5,4,-3],[9,-1,7,6,9,5,-4,2,8,-9,-1,7,4,9,3,-6,-5,9,-7,6,-6,9],[-6,8,-6,9,5,-3,7,-8,-7,5,3,6,8,-7,-6,6,7,4,-3,1,8,-7],[-9,7,1,-7,-5,6,6,-10,8,-2,2,-10,-8,2,-6,-3,8,-10,2,-3,10,-2],[1,-9,-10,7,7,-6,8,-3,1,-1,3,-5,-9,-4,8,-7,10,1,7,1,-5,10],[-6,-8,-6,5,-10,-6,1,-2,-4,9,5,5,9,-7,-2,8,8,5,4,-5,10,-5],[-9,-1,6,-8,-1,-6,-8,3,-7,-8,-6,1,2,-6,7,-5,-10,9,6,10,2,-8],[-6,8,1,-2,-10,-8,-9,7,8,2,8,-6,1,-2,10,3,2,-3,7,1,-6,-10],[-7,-3,-8,-5,-6,-3,-4,2,-6,4,-6,2,-10,-3,-3,-5,1,-5,3,-7,8,-10],[6,10,4,-1,-1,-6,-5,-9,-1,9,2,-10,4,6,9,8,-5,-7,-4,-1,-1,-6],[-5,5,9,9,1,-6,9,9,-5,3,-9,3,1,8,3,8,-9,6,-10,9,4,-6],[-5,-1,4,-4,-8,-6,-3,1,-8,-5,-4,5,6,3,7,-5,4,7,-3,3,-10,-10],[-3,2,-2,8,-8,9,-5,5,4,8,-7,-10,-8,2,1,-4,3,-6,2,2,-7,5],[-7,-7,4,1,-10,2,3,9,-5,8,6,-4,10,-8,9,10,-6,7,2,-1,-8,-4],[8,4,-4,-3,10,9,-5,8,2,10,-7,-8,-2,5,4,2,1,-5,-10,-5,8,-10],[-3,-7,-6,-3,-3,-4,-3,-6,6,-9,3,2,-4,2,3,7,10,-10,-10,-1,-7,-7],[-4,7,10,-9,-2,4,1,10,-10,1,10,6,8,4,-4,6,-5,-2,-9,-9,3,6],[1,-10,-4,1,-6,-7,-8,-10,3,2,6,-6,4,-5,9,3,-1,3,7,1,-4,-8],[9,-3,-3,-2,-9,-6,-4,-10,-4,4,-7,1,4,-7,-2,9,2,-6,8,-6,6,10],[2,-2,-2,-4,-7,2,8,-10,-4,-4,2,3,-7,9,-10,-5,10,1,-6,-2,9,-4],[3,7,-2,4,-10,8,-6,3,7,-8,-7,-8,3,8,3,-7,4,4,7,-2,6,4],[-6,-8,7,9,-7,9,-6,-10,-8,5,-2,-10,10,-6,1,-10,9,9,6,-1,2,2],[8,-6,8,-8,4,-1,-1,3,-7,6,-1,-1,2,9,-4,3,3,-8,-5,-3,-6,3],[1,9,9,1,2,-6,-6,8,7,1,1,3,8,4,2,3,-5,9,-10,3,-4,6]], dtype = "uint32")#candidate|4833|(24, 22)|const|uint32
bop_4834 = relay.power(call_4831.astype('float32'), relay.reshape(const_4833.astype('float32'), relay.shape_of(call_4831))) # shape=(24, 22)
bop_4837 = relay.power(call_4832.astype('float32'), relay.reshape(const_4833.astype('float32'), relay.shape_of(call_4832))) # shape=(24, 22)
func_3304_call = mod.get_global_var('func_3304')
func_3307_call = mutated_mod.get_global_var('func_3307')
var_4842 = relay.var("var_4842", dtype = "float32", shape = (360,))#candidate|4842|(360,)|var|float32
call_4841 = relay.TupleGetItem(func_3304_call(relay.reshape(var_4842.astype('float32'), [360,])), 3)
call_4843 = relay.TupleGetItem(func_3307_call(relay.reshape(var_4842.astype('float32'), [360,])), 3)
uop_4865 = relay.sinh(bop_4834.astype('float32')) # shape=(24, 22)
uop_4867 = relay.sinh(bop_4837.astype('float32')) # shape=(24, 22)
uop_4872 = relay.erf(uop_4865.astype('float32')) # shape=(24, 22)
uop_4874 = relay.erf(uop_4867.astype('float32')) # shape=(24, 22)
func_2754_call = mod.get_global_var('func_2754')
func_2757_call = mutated_mod.get_global_var('func_2757')
var_4878 = relay.var("var_4878", dtype = "float32", shape = (288,))#candidate|4878|(288,)|var|float32
call_4877 = relay.TupleGetItem(func_2754_call(relay.reshape(var_4878.astype('float32'), [288,])), 0)
call_4879 = relay.TupleGetItem(func_2757_call(relay.reshape(var_4878.astype('float32'), [288,])), 0)
bop_4883 = relay.less_equal(uop_4872.astype('bool'), relay.reshape(uop_4865.astype('bool'), relay.shape_of(uop_4872))) # shape=(24, 22)
bop_4886 = relay.less_equal(uop_4874.astype('bool'), relay.reshape(uop_4867.astype('bool'), relay.shape_of(uop_4874))) # shape=(24, 22)
func_4263_call = mod.get_global_var('func_4263')
func_4265_call = mutated_mod.get_global_var('func_4265')
call_4888 = func_4263_call()
call_4889 = func_4263_call()
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_4892 = func_1620_call()
call_4893 = func_1620_call()
bop_4894 = relay.add(uop_4865.astype('uint16'), relay.reshape(bop_4834.astype('uint16'), relay.shape_of(uop_4865))) # shape=(24, 22)
bop_4897 = relay.add(uop_4867.astype('uint16'), relay.reshape(bop_4837.astype('uint16'), relay.shape_of(uop_4867))) # shape=(24, 22)
output = relay.Tuple([call_4841,var_4842,call_4877,var_4878,bop_4883,call_4888,call_4892,bop_4894,])
output2 = relay.Tuple([call_4843,var_4842,call_4879,var_4878,bop_4886,call_4889,call_4893,bop_4897,])
func_4904 = relay.Function([var_4842,var_4878,], output)
mod['func_4904'] = func_4904
mod = relay.transform.InferType()(mod)
mutated_mod['func_4904'] = func_4904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4904_call = mutated_mod.get_global_var('func_4904')
var_4906 = relay.var("var_4906", dtype = "float32", shape = (360,))#candidate|4906|(360,)|var|float32
var_4907 = relay.var("var_4907", dtype = "float32", shape = (288,))#candidate|4907|(288,)|var|float32
call_4905 = func_4904_call(var_4906,var_4907,)
output = call_4905
func_4908 = relay.Function([var_4906,var_4907,], output)
mutated_mod['func_4908'] = func_4908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3383_call = mod.get_global_var('func_3383')
func_3385_call = mutated_mod.get_global_var('func_3385')
call_4932 = relay.TupleGetItem(func_3383_call(), 0)
call_4933 = relay.TupleGetItem(func_3385_call(), 0)
func_4530_call = mod.get_global_var('func_4530')
func_4532_call = mutated_mod.get_global_var('func_4532')
call_4943 = relay.TupleGetItem(func_4530_call(), 0)
call_4944 = relay.TupleGetItem(func_4532_call(), 0)
output = relay.Tuple([call_4932,call_4943,])
output2 = relay.Tuple([call_4933,call_4944,])
func_4946 = relay.Function([], output)
mod['func_4946'] = func_4946
mod = relay.transform.InferType()(mod)
mutated_mod['func_4946'] = func_4946
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4946_call = mutated_mod.get_global_var('func_4946')
call_4947 = func_4946_call()
output = call_4947
func_4948 = relay.Function([], output)
mutated_mod['func_4948'] = func_4948
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3383_call = mod.get_global_var('func_3383')
func_3385_call = mutated_mod.get_global_var('func_3385')
call_4961 = relay.TupleGetItem(func_3383_call(), 0)
call_4962 = relay.TupleGetItem(func_3385_call(), 0)
uop_4974 = relay.log(call_4961.astype('float64')) # shape=(11, 2, 11)
uop_4976 = relay.log(call_4962.astype('float64')) # shape=(11, 2, 11)
output = uop_4974
output2 = uop_4976
func_5003 = relay.Function([], output)
mod['func_5003'] = func_5003
mod = relay.transform.InferType()(mod)
output = func_5003()
func_5004 = relay.Function([], output)
mutated_mod['func_5004'] = func_5004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_5022 = relay.TupleGetItem(func_2162_call(), 0)
call_5023 = relay.TupleGetItem(func_2164_call(), 0)
uop_5024 = relay.sigmoid(call_5022.astype('float32')) # shape=(6, 11, 8)
uop_5026 = relay.sigmoid(call_5023.astype('float32')) # shape=(6, 11, 8)
bop_5029 = relay.left_shift(uop_5024.astype('uint64'), relay.reshape(call_5022.astype('uint64'), relay.shape_of(uop_5024))) # shape=(6, 11, 8)
bop_5032 = relay.left_shift(uop_5026.astype('uint64'), relay.reshape(call_5023.astype('uint64'), relay.shape_of(uop_5026))) # shape=(6, 11, 8)
output = bop_5029
output2 = bop_5032
func_5039 = relay.Function([], output)
mod['func_5039'] = func_5039
mod = relay.transform.InferType()(mod)
mutated_mod['func_5039'] = func_5039
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5039_call = mutated_mod.get_global_var('func_5039')
call_5040 = func_5039_call()
output = call_5040
func_5041 = relay.Function([], output)
mutated_mod['func_5041'] = func_5041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3383_call = mod.get_global_var('func_3383')
func_3385_call = mutated_mod.get_global_var('func_3385')
call_5059 = relay.TupleGetItem(func_3383_call(), 0)
call_5060 = relay.TupleGetItem(func_3385_call(), 0)
func_2754_call = mod.get_global_var('func_2754')
func_2757_call = mutated_mod.get_global_var('func_2757')
const_5099 = relay.const([0.395643,0.787945,-8.834093,-9.219740,7.687833,-2.644506,7.831795,-9.699981,2.973545,8.804696,4.864316,-2.232937,-4.508078,-9.376461,3.702176,0.352666,-7.174731,6.542611,6.543794,-6.209164,-0.455380,2.365010,-2.696676,6.483020,-1.121174,4.168497,7.773330,-9.084447,-2.425450,4.023317,-9.642329,-0.289671,-1.303813,-9.335305,-4.252483,-4.131621,7.124008,-9.579531,-8.497279,7.702715,-3.841369,-1.751014,-8.634146,6.574713,-8.147195,-1.733932,3.602043,8.928220,-1.445757,-4.245314,-4.051249,3.103681,-4.583357,-7.877945,-7.651506,7.848878,-6.177772,-6.645202,-6.725018,6.890868,-5.899342,-7.728188,2.895137,0.712742,3.428366,-0.900216,6.175681,3.870304,7.571244,-8.697064,7.816429,-5.553374,3.127867,-9.989603,-3.668108,-1.421479,9.660846,-6.210759,-0.498472,-3.251494,3.939568,-1.388932,-2.493002,-6.491918,3.186644,4.634652,-4.248462,-4.195321,-1.216519,-6.474336,-2.170771,-5.048753,1.230054,-1.640105,-0.924140,5.128959,3.953926,-6.820910,5.372459,1.407581,9.051621,0.668693,-4.088225,-7.315924,-9.441823,7.125329,1.140884,-3.480750,5.913494,5.872893,6.317972,4.328583,-0.447776,-8.180957,7.914447,-5.888389,0.137636,-3.785540,1.699678,-5.560673,7.177801,-2.699625,7.745334,9.598587,-1.526737,2.553058,3.169687,-5.332816,-2.999807,4.565224,7.370063,7.742962,8.023038,-8.902084,-4.232224,-0.600821,6.855650,-4.243749,6.293100,4.720920,-6.555386,3.912000,4.371000,1.834695,5.051318,4.776824,-0.984043,9.772930,1.995209,-0.528112,-0.175302,1.332055,-7.645236,7.713591,-7.685226,5.311266,8.984575,-3.036597,-1.522788,-3.821332,1.091405,-5.571567,-3.690868,4.427744,-2.199294,2.227043,6.948826,-1.931252,9.732797,5.898079,-8.913301,-2.900071,-9.942019,-3.796269,3.745305,-0.095862,1.765121,-9.073970,-6.323063,5.355026,-7.967922,0.141933,6.531919,7.814829,2.131916,-0.109739,0.110566,7.274860,-5.381857,-8.972939,9.831254,-4.072869,-2.798303,-6.154402,-9.533251,6.173915,8.970718,-9.303664,-0.018957,7.264532,0.419057,8.756807,-0.074020,-8.044622,-2.896504,-9.255023,8.923333,-5.505763,-5.606968,-1.730828,-9.523531,7.932089,-6.640343,3.648654,9.358028,5.352463,-4.013467,4.352281,4.733691,4.497111,-7.409011,7.716951,-6.778925,9.957079,3.188414,-5.990465,4.237140,0.466528,8.475161,-3.896305,6.054641,0.242258,-4.090511,-6.615956,-9.105406,-4.663768,-0.223923,-5.592334,8.704229,3.982690,6.314256,1.010802,3.615166,3.733435,6.111244,8.187088,6.746054,-0.939882,0.104537,4.341518,7.169062,-2.715592,-8.806475,-9.284833,1.149154,-2.681696,2.262217,4.224022,-6.477517,-5.286288,9.569525,-0.530344,-3.860279,-9.337727,8.481758,-5.256730,2.510488,-6.926748,7.294933,-1.887294,-0.664249,-3.277562,-3.168763,-8.541974,-6.725387,-9.871915,-0.177777,-6.159198,6.167532,-8.237969,-8.086497,1.150883,-0.529739,7.996461,3.916518,-5.577331,-6.788746,9.861062], dtype = "float32")#candidate|5099|(288,)|const|float32
call_5098 = relay.TupleGetItem(func_2754_call(relay.reshape(const_5099.astype('float32'), [288,])), 3)
call_5100 = relay.TupleGetItem(func_2757_call(relay.reshape(const_5099.astype('float32'), [288,])), 3)
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_5106 = relay.TupleGetItem(func_2162_call(), 1)
call_5107 = relay.TupleGetItem(func_2164_call(), 1)
output = relay.Tuple([call_5059,call_5098,const_5099,call_5106,])
output2 = relay.Tuple([call_5060,call_5100,const_5099,call_5107,])
func_5110 = relay.Function([], output)
mod['func_5110'] = func_5110
mod = relay.transform.InferType()(mod)
mutated_mod['func_5110'] = func_5110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5110_call = mutated_mod.get_global_var('func_5110')
call_5111 = func_5110_call()
output = call_5111
func_5112 = relay.Function([], output)
mutated_mod['func_5112'] = func_5112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4530_call = mod.get_global_var('func_4530')
func_4532_call = mutated_mod.get_global_var('func_4532')
call_5132 = relay.TupleGetItem(func_4530_call(), 0)
call_5133 = relay.TupleGetItem(func_4532_call(), 0)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_5137 = relay.TupleGetItem(func_1590_call(), 0)
call_5138 = relay.TupleGetItem(func_1592_call(), 0)
output = relay.Tuple([call_5132,call_5137,])
output2 = relay.Tuple([call_5133,call_5138,])
func_5139 = relay.Function([], output)
mod['func_5139'] = func_5139
mod = relay.transform.InferType()(mod)
output = func_5139()
func_5140 = relay.Function([], output)
mutated_mod['func_5140'] = func_5140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_5182 = relay.TupleGetItem(func_1590_call(), 0)
call_5183 = relay.TupleGetItem(func_1592_call(), 0)
output = call_5182
output2 = call_5183
func_5190 = relay.Function([], output)
mod['func_5190'] = func_5190
mod = relay.transform.InferType()(mod)
output = func_5190()
func_5191 = relay.Function([], output)
mutated_mod['func_5191'] = func_5191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4135_call = mod.get_global_var('func_4135')
func_4136_call = mutated_mod.get_global_var('func_4136')
call_5216 = relay.TupleGetItem(func_4135_call(), 1)
call_5217 = relay.TupleGetItem(func_4136_call(), 1)
output = call_5216
output2 = call_5217
func_5227 = relay.Function([], output)
mod['func_5227'] = func_5227
mod = relay.transform.InferType()(mod)
output = func_5227()
func_5228 = relay.Function([], output)
mutated_mod['func_5228'] = func_5228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2318_call = mod.get_global_var('func_2318')
func_2319_call = mutated_mod.get_global_var('func_2319')
call_5301 = relay.TupleGetItem(func_2318_call(), 0)
call_5302 = relay.TupleGetItem(func_2319_call(), 0)
output = call_5301
output2 = call_5302
func_5303 = relay.Function([], output)
mod['func_5303'] = func_5303
mod = relay.transform.InferType()(mod)
mutated_mod['func_5303'] = func_5303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mutated_mod.get_global_var('func_5303')
call_5304 = func_5303_call()
output = call_5304
func_5305 = relay.Function([], output)
mutated_mod['func_5305'] = func_5305
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3431_call = mod.get_global_var('func_3431')
func_3432_call = mutated_mod.get_global_var('func_3432')
call_5319 = relay.TupleGetItem(func_3431_call(), 0)
call_5320 = relay.TupleGetItem(func_3432_call(), 0)
func_1390_call = mod.get_global_var('func_1390')
func_1392_call = mutated_mod.get_global_var('func_1392')
const_5335 = relay.const([[0.258601,4.084644],[8.979992,-5.139859],[9.200293,9.419325],[1.822846,-1.145360],[8.575113,6.413609],[8.647298,-3.096603],[-5.777691,-0.891487],[7.449721,-6.487636],[-1.261368,-8.162337],[-5.106630,3.293567],[-5.432330,6.336308],[-2.584609,2.944367],[4.026277,6.407651],[-9.435559,-4.589072],[-3.188088,0.762294],[-8.952127,-3.948094],[9.755592,5.217217],[-8.319162,-4.978832],[5.223272,-0.108473],[2.669766,1.824135],[-4.527995,3.804620],[0.851682,8.599751],[1.332493,1.953900],[3.753822,-8.408952],[-2.373821,-2.123009],[-4.411264,9.753717],[-7.658502,6.197154],[-1.252127,7.360836],[-8.079327,2.412278],[-9.459224,5.778246],[3.964490,6.902163],[-4.205079,8.330681],[9.359263,3.579878],[-6.940723,-8.778600],[-7.437228,-6.756784],[-4.864867,1.016432],[5.160679,-0.018072],[-2.234518,1.669558],[-4.260059,-0.366843],[-2.216255,-3.929183],[8.446662,7.170055],[-4.608904,1.236274],[3.613827,1.990927],[4.134359,-7.030318],[2.665532,-6.369015],[-7.822227,5.745046],[-0.108644,-2.295031],[-2.142564,3.672264],[-7.578535,5.412251],[-4.890144,-6.474438],[2.506591,0.345509],[-3.241513,2.390251],[6.869345,2.394116],[7.460301,-8.181817],[-3.720212,-0.513905],[4.456463,6.902558],[-8.347157,8.451778],[4.030541,-5.565599],[8.940644,6.459870],[-3.042408,-6.760231],[-9.987616,0.884043],[-1.910224,7.899328],[-2.000065,0.610592],[6.451868,-3.360347],[-0.733762,-6.105937],[6.207935,-4.287994],[8.795671,-3.763569],[-6.378248,3.812223],[4.127527,-7.017637],[-3.184182,-9.507205],[4.753939,5.570707],[-7.293073,-6.280829],[4.398260,-2.566767],[0.852694,9.975816],[-4.658820,-3.313522],[-8.845928,8.434387],[4.675499,-8.838062],[-8.166523,-2.417536],[-7.600417,-6.129055],[3.311457,0.609707],[-6.307117,8.837188],[-6.643565,-1.723539],[8.232156,2.577550],[-8.729673,5.017788],[-7.119723,0.588550],[-4.622811,-3.462196],[5.616346,-8.334103],[8.088772,5.924911],[6.280982,-7.305335],[-2.331196,3.982376],[9.405079,2.721045],[8.189849,5.492477],[-2.093172,-1.415983],[7.391512,-3.319431],[-8.386905,8.304936],[-4.706740,5.225202],[-6.515513,-3.262534],[-8.261352,-2.033514],[-4.664416,5.649311],[-2.940644,-3.995621],[1.242993,7.987907],[2.926390,-8.504389],[-7.586156,-9.109399],[-6.638184,3.146484],[7.088049,8.626920],[2.730310,5.606601],[-2.728289,9.001440],[-4.890906,0.402169],[7.309523,-6.128176],[-6.132599,-9.727846],[-5.358083,-4.991573],[-0.865232,1.641090],[0.270415,0.749157],[-9.976860,-0.681065],[8.793080,0.058420],[9.437977,3.909860],[-6.679148,-9.011019],[-3.883134,1.420637],[9.452436,-4.830028],[4.425479,4.195345],[-5.281262,1.701271],[9.607781,7.590379],[-5.329021,-2.825246],[-0.605873,-8.319172],[5.880833,4.231998],[4.131976,0.322545],[-7.986143,-9.168380],[0.128126,-8.476685],[-6.307303,1.868878],[-4.110845,-3.791420],[7.679114,-2.493761],[-0.351636,-2.887324],[0.396551,-3.164670],[2.123257,3.718542],[3.347262,6.029696],[9.556631,-0.765610],[-8.976835,-5.161760],[2.828927,1.181905],[6.677455,-6.916625],[-9.396833,-9.473148],[-1.768210,-2.938617],[-9.990756,-0.482308],[3.307883,-7.740543],[5.515463,-0.610009]], dtype = "float32")#candidate|5335|(144, 2)|const|float32
call_5334 = relay.TupleGetItem(func_1390_call(relay.reshape(const_5335.astype('float32'), [8, 6, 6])), 0)
call_5336 = relay.TupleGetItem(func_1392_call(relay.reshape(const_5335.astype('float32'), [8, 6, 6])), 0)
func_2136_call = mod.get_global_var('func_2136')
func_2139_call = mutated_mod.get_global_var('func_2139')
const_5345 = relay.const([7,5,3,-9,3,9,8,2,-4,4,-3,-5,2,-5,-4,-6,-2,-5,5,1,2,3,-9,-5,9,8,-2,1,8,9,-8,3,8,-6,-3,-10,-6,-9,7,7,-3,9,9,-1,8,7,5,-6,9,7,-7,-1,9,8,-1,-3,10,-2,-10,4,-5,3,-4,-4,-1,6,-9,10,6,5,3,-4,7,-1,-10,-8,9,-4,2,-5,10,-10,-10,-8,-10,-4,10,7,-3,-8,-5,-8,8,5,-10,3,-2,1,-7,8,2,2,9,3,8,-7,-10,5,-6,9,3,-10,-7,8,-9,-1,8,5,3,-3,1,-3,-4,-10,1,10,1,10,8,2,-4,-10,-6,-2,-5,9,-5,-9,-3,1,8,7,-9,9,-4,-7,-4,1,-2,-1,7,4,-2,-1,4,8,-3,-1,-3,10,-1,-8,-3,-9,5,1,7,4,-10,6,-8,6,-9,-4,9,-4,2,-7,2,-8,-5,-8,8,-4,8,-4,4,6,7,8,3,-6,3,-9,-1,-3,-8,9,-3,-6,-4,-5,-8,-10,2,-3,-9,9,-4,8,-5,-2,-3,1,-5,-9,5,5,-7,-2,-4,-4,-6,6,1,-5,-6,3,9,5,1,3,8,-3,5,-3,-2,6,2,-8,-8,1,-2,-5,-10,-5,6,9,7,10,9,5,-2,7,-2,7,8,8,-4,-10,-5,7,4,5,10,-7,9,-10,10,-5,2,4,1,1,5,2,-8,-1,-5,-8,-10,-5,5,-1,3,-9,9,-7,7,8,1,4,-10,-4,9,-1,-6,-1,-2,-8,-10,9,2,2,4,-3,-1,-4,2,-6,-9,2,-3,-8,7,7,-3,-7,-4,6,8,-5,-8,7,-7,3,-2,-5,9,-10,-7,2,-5,7,-7,-9,4,-3,3,2,-5,-7,-1,-1,-6,-5,-8,-5,7,4,6,-10,-5,3,-4,-7,-2,-3,-9,-1,5,-9,2,-8,9,6,5,-6,-10,-8,5,-3,-4,-8,-3,9,5,-1,-6,-10,10,8,10,6,4,4,1,-4,6,-7,3,6,-6,6,3,6,-10,9,-10,-1,6,2,5,-2,10,-9,-9,-10,10,-8,-10,8,-9,-1,1,5,-9,7,-5,-6,-2,7,-10,6,-2,6,-9,3,1,-8,8,-10,-10,-3,-7,1,4,9,-4,-3,-9,8,3,-7,7,-9,-1,-4,-7,8,-5,-1,7,-2,-7,7,6,-6,-1,5,10,-3,-4,-2,3,3,10,-7,-6,-8,-4,10,4,-8,1,-3,9,2,4,-2,-5,-6,-1,-2,2,9,-6,-5,-7,5,8,8,3,-1,-5,5,10,-7,-4,7,8,1,4,-6,3,-8,-7,-10,-8,7,-6,5,4,6,-10,4,-8,4,3,5,-9,-6,-9,7,7,-1,8,8,8,2,4,8,2,-8,-1,-10,-5,-7,3,4,-1,5,-2,3,-7,-8,2,-5,-7,9,5,10,-6,-6,2,10,-6,-5,10,-8,7,-7,3,3,-4,-10,2,1,-7,-8,9,-4,-7,-3,9,1,1,-4,2,4,10,7,2,-3,-4,-9,10,-8,-2,-3,4,6,-4,10,8,1,10,3,5,2,-6,2,4,-3,3,-7,10,4,4,7,2,1,8,-5,-9,-4,-9,10,-6,-10,-9,-8,10,10,-8,7,6,1,1,7,-4,-6,-7,6,7,4,3,-4,6,7,10,-5,2,-10,-3,-5,-8,-9,7,-10,-9,2,-8,5,8,-9,5,-7,-9,2,-4,6,9,-8,-1,1,-5,-4,-9,9,10,-8,-2,-4,1,-3,-4,-10,-4,-9,9,7,-3,6,-9,-1,-5,-5,-5,-7,4,3,9,-1,4,-10,-10,-4,9,4,9,10,-4,2,-4,6,-9,8,-4,2,8,8,2,-10,-6,-10,10,10,5,-5,-8,-8,2,6,-4,-4,2,-8,-6,7,3,-8,9,10,7,-4,-4,4,10,-2,8,-7,-9,-9,5,6,5,-2,-1,10,-8,3,-9,-10,6,-1,9,9,5,1,-1,-8,3,1,-4,10,-5,6,9,-3,7,1,2,-1,5,-6,3,5,8,9,-6,6,5,5,7,1,2,9,2,-2,4,-5,6,4,-7,7,-6,-7,6,-3,10,6,-5,-7,-5,-6,-10,7,-5,9,-3,-5,1,8,-4,10,-8,-7,1,2,4,4,-10,-10,-1,-5,9,-5,-2,10,7,-9,6,8,1,-3,7,-10,10,10,-1,8,-8,10,6,-5,10,8,1,5,-3,6,-6,4,8,-7,-2,-1,-8,10,3,-8,1,-10,9,4,-2,1,9,-3,-1,10,-7,-4,3,8,-1,-8,-10,5,-2,1,-1,3,8,-9,-8,4,9,10,-4,-6,5,-7,2,4], dtype = "int16")#candidate|5345|(896,)|const|int16
call_5344 = relay.TupleGetItem(func_2136_call(relay.reshape(const_5345.astype('int16'), [896,]), relay.reshape(const_5345.astype('float32'), [8, 7, 16]), ), 3)
call_5346 = relay.TupleGetItem(func_2139_call(relay.reshape(const_5345.astype('int16'), [896,]), relay.reshape(const_5345.astype('float32'), [8, 7, 16]), ), 3)
output = relay.Tuple([call_5319,call_5334,const_5335,call_5344,const_5345,])
output2 = relay.Tuple([call_5320,call_5336,const_5335,call_5346,const_5345,])
func_5353 = relay.Function([], output)
mod['func_5353'] = func_5353
mod = relay.transform.InferType()(mod)
output = func_5353()
func_5354 = relay.Function([], output)
mutated_mod['func_5354'] = func_5354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_5355 = func_4421_call()
call_5356 = func_4421_call()
output = call_5355
output2 = call_5356
func_5361 = relay.Function([], output)
mod['func_5361'] = func_5361
mod = relay.transform.InferType()(mod)
mutated_mod['func_5361'] = func_5361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5361_call = mutated_mod.get_global_var('func_5361')
call_5362 = func_5361_call()
output = call_5362
func_5363 = relay.Function([], output)
mutated_mod['func_5363'] = func_5363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4421_call = mod.get_global_var('func_4421')
func_4423_call = mutated_mod.get_global_var('func_4423')
call_5460 = func_4421_call()
call_5461 = func_4421_call()
var_5472 = relay.var("var_5472", dtype = "uint8", shape = (11, 2, 11))#candidate|5472|(11, 2, 11)|var|uint8
bop_5473 = relay.bitwise_and(call_5460.astype('int32'), relay.reshape(var_5472.astype('int32'), relay.shape_of(call_5460))) # shape=(11, 2, 11)
bop_5476 = relay.bitwise_and(call_5461.astype('int32'), relay.reshape(var_5472.astype('int32'), relay.shape_of(call_5461))) # shape=(11, 2, 11)
var_5485 = relay.var("var_5485", dtype = "int32", shape = (11, 2, 11))#candidate|5485|(11, 2, 11)|var|int32
bop_5486 = relay.logical_and(bop_5473.astype('bool'), relay.reshape(var_5485.astype('bool'), relay.shape_of(bop_5473))) # shape=(11, 2, 11)
bop_5489 = relay.logical_and(bop_5476.astype('bool'), relay.reshape(var_5485.astype('bool'), relay.shape_of(bop_5476))) # shape=(11, 2, 11)
func_2372_call = mod.get_global_var('func_2372')
func_2376_call = mutated_mod.get_global_var('func_2376')
var_5501 = relay.var("var_5501", dtype = "float32", shape = (288,))#candidate|5501|(288,)|var|float32
call_5500 = relay.TupleGetItem(func_2372_call(relay.reshape(var_5501.astype('float32'), [288,]), relay.reshape(var_5472.astype('float32'), [11, 2, 11]), ), 1)
call_5502 = relay.TupleGetItem(func_2376_call(relay.reshape(var_5501.astype('float32'), [288,]), relay.reshape(var_5472.astype('float32'), [11, 2, 11]), ), 1)
func_2907_call = mod.get_global_var('func_2907')
func_2910_call = mutated_mod.get_global_var('func_2910')
const_5505 = relay.const([True,False,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False], dtype = "bool")#candidate|5505|(32,)|const|bool
call_5504 = relay.TupleGetItem(func_2907_call(relay.reshape(const_5505.astype('bool'), [32,]), relay.reshape(call_5500.astype('bool'), [288,]), ), 7)
call_5506 = relay.TupleGetItem(func_2910_call(relay.reshape(const_5505.astype('bool'), [32,]), relay.reshape(call_5500.astype('bool'), [288,]), ), 7)
func_1390_call = mod.get_global_var('func_1390')
func_1392_call = mutated_mod.get_global_var('func_1392')
call_5514 = relay.TupleGetItem(func_1390_call(relay.reshape(call_5500.astype('float32'), [8, 6, 6])), 0)
call_5515 = relay.TupleGetItem(func_1392_call(relay.reshape(call_5500.astype('float32'), [8, 6, 6])), 0)
uop_5516 = relay.cosh(call_5504.astype('float64')) # shape=(11, 2, 11)
uop_5518 = relay.cosh(call_5506.astype('float64')) # shape=(11, 2, 11)
func_1485_call = mod.get_global_var('func_1485')
func_1489_call = mutated_mod.get_global_var('func_1489')
const_5527 = relay.const([False,False,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False], dtype = "bool")#candidate|5527|(24,)|const|bool
const_5528 = relay.const([[True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,False,True,True,False],[True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False]], dtype = "bool")#candidate|5528|(2, 180)|const|bool
call_5526 = relay.TupleGetItem(func_1485_call(relay.reshape(const_5527.astype('bool'), [6, 1, 4]), relay.reshape(const_5528.astype('bool'), [6, 15, 4]), ), 0)
call_5529 = relay.TupleGetItem(func_1489_call(relay.reshape(const_5527.astype('bool'), [6, 1, 4]), relay.reshape(const_5528.astype('bool'), [6, 15, 4]), ), 0)
output = relay.Tuple([bop_5486,call_5500,var_5501,const_5505,call_5514,uop_5516,call_5526,const_5527,const_5528,])
output2 = relay.Tuple([bop_5489,call_5502,var_5501,const_5505,call_5515,uop_5518,call_5529,const_5527,const_5528,])
func_5535 = relay.Function([var_5472,var_5485,var_5501,], output)
mod['func_5535'] = func_5535
mod = relay.transform.InferType()(mod)
mutated_mod['func_5535'] = func_5535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5535_call = mutated_mod.get_global_var('func_5535')
var_5537 = relay.var("var_5537", dtype = "uint8", shape = (11, 2, 11))#candidate|5537|(11, 2, 11)|var|uint8
var_5538 = relay.var("var_5538", dtype = "int32", shape = (11, 2, 11))#candidate|5538|(11, 2, 11)|var|int32
var_5539 = relay.var("var_5539", dtype = "float32", shape = (288,))#candidate|5539|(288,)|var|float32
call_5536 = func_5535_call(var_5537,var_5538,var_5539,)
output = call_5536
func_5540 = relay.Function([var_5537,var_5538,var_5539,], output)
mutated_mod['func_5540'] = func_5540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5039_call = mod.get_global_var('func_5039')
func_5041_call = mutated_mod.get_global_var('func_5041')
call_5589 = func_5039_call()
call_5590 = func_5039_call()
uop_5606 = relay.sinh(call_5589.astype('float64')) # shape=(6, 11, 8)
uop_5608 = relay.sinh(call_5590.astype('float64')) # shape=(6, 11, 8)
func_3965_call = mod.get_global_var('func_3965')
func_3967_call = mutated_mod.get_global_var('func_3967')
call_5617 = func_3965_call()
call_5618 = func_3965_call()
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_5621 = func_5190_call()
call_5622 = func_5190_call()
output = relay.Tuple([uop_5606,call_5617,call_5621,])
output2 = relay.Tuple([uop_5608,call_5618,call_5622,])
func_5623 = relay.Function([], output)
mod['func_5623'] = func_5623
mod = relay.transform.InferType()(mod)
mutated_mod['func_5623'] = func_5623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5623_call = mutated_mod.get_global_var('func_5623')
call_5624 = func_5623_call()
output = call_5624
func_5625 = relay.Function([], output)
mutated_mod['func_5625'] = func_5625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3510_call = mod.get_global_var('func_3510')
func_3511_call = mutated_mod.get_global_var('func_3511')
call_5648 = relay.TupleGetItem(func_3510_call(), 0)
call_5649 = relay.TupleGetItem(func_3511_call(), 0)
output = call_5648
output2 = call_5649
func_5655 = relay.Function([], output)
mod['func_5655'] = func_5655
mod = relay.transform.InferType()(mod)
output = func_5655()
func_5656 = relay.Function([], output)
mutated_mod['func_5656'] = func_5656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4179_call = mod.get_global_var('func_4179')
func_4180_call = mutated_mod.get_global_var('func_4180')
call_5673 = func_4179_call()
call_5674 = func_4179_call()
output = relay.Tuple([call_5673,])
output2 = relay.Tuple([call_5674,])
func_5675 = relay.Function([], output)
mod['func_5675'] = func_5675
mod = relay.transform.InferType()(mod)
mutated_mod['func_5675'] = func_5675
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5675_call = mutated_mod.get_global_var('func_5675')
call_5676 = func_5675_call()
output = call_5676
func_5677 = relay.Function([], output)
mutated_mod['func_5677'] = func_5677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mod.get_global_var('func_5003')
func_5004_call = mutated_mod.get_global_var('func_5004')
call_5678 = func_5003_call()
call_5679 = func_5003_call()
func_1819_call = mod.get_global_var('func_1819')
func_1822_call = mutated_mod.get_global_var('func_1822')
call_5694 = relay.TupleGetItem(func_1819_call(relay.reshape(call_5678.astype('float32'), [11, 2, 11])), 0)
call_5695 = relay.TupleGetItem(func_1822_call(relay.reshape(call_5678.astype('float32'), [11, 2, 11])), 0)
output = relay.Tuple([call_5678,call_5694,])
output2 = relay.Tuple([call_5679,call_5695,])
func_5698 = relay.Function([], output)
mod['func_5698'] = func_5698
mod = relay.transform.InferType()(mod)
mutated_mod['func_5698'] = func_5698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5698_call = mutated_mod.get_global_var('func_5698')
call_5699 = func_5698_call()
output = call_5699
func_5700 = relay.Function([], output)
mutated_mod['func_5700'] = func_5700
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5747 = relay.var("var_5747", dtype = "float64", shape = (10, 3, 7))#candidate|5747|(10, 3, 7)|var|float64
uop_5748 = relay.sinh(var_5747.astype('float64')) # shape=(10, 3, 7)
func_1390_call = mod.get_global_var('func_1390')
func_1392_call = mutated_mod.get_global_var('func_1392')
const_5758 = relay.const([2.208258,7.063767,8.090751,-2.678103,1.631031,-6.790336,0.173224,8.786677,4.349912,1.535411,-3.364072,-8.514310,-4.757385,-7.289572,-2.932831,-1.820605,-3.249355,1.570472,2.823145,6.010809,-6.169250,-3.850018,-2.767983,-5.314087,0.281591,-3.459799,-4.678009,-3.781514,-4.969933,-2.048660,5.768898,-3.006892,8.846379,9.241303,4.466025,1.992250,-9.602377,1.970528,4.866787,-9.127794,6.664627,-6.571298,-6.277743,-6.047543,-4.439795,1.441928,0.831699,4.457035,2.540844,-9.183819,6.595652,-7.962035,9.498753,0.582770,-6.449962,7.511901,-9.895448,4.814401,-6.765900,2.971143,-8.360403,5.104763,2.638951,-1.298805,6.044459,3.294745,1.164189,0.431030,-2.636605,9.959158,-3.437759,-4.321764,7.736289,1.113424,-7.459051,-7.906252,7.991831,-0.028002,-1.619799,0.435172,9.792292,5.310804,5.929889,2.040982,7.898036,-4.014068,-2.395220,-5.114591,-9.211620,9.760116,-5.420667,4.745779,9.895327,-2.319144,8.704941,-2.651356,5.721512,8.211473,-8.625810,-4.702105,0.552226,1.859796,9.797959,7.160427,-3.993495,-8.534570,-5.949194,-2.472223,-9.765710,-8.526815,8.729645,-1.738191,-8.894658,4.463296,6.080907,-9.732605,-6.944309,-8.546667,9.685179,0.214143,-4.073039,-9.913367,3.628670,2.825581,-7.005633,1.756723,-2.899036,-5.863553,2.586074,1.544390,0.180474,-2.574616,1.229888,9.266750,-1.872905,-8.479782,0.795711,-6.197328,-8.863706,-3.169222,2.631422,-6.995731,2.741769,-1.087286,-5.127255,0.534890,0.229103,5.889544,-1.945397,8.168422,1.598620,-4.196592,-3.589581,5.728488,-9.571016,0.705189,-9.230530,4.933080,-4.034704,-1.364375,6.949402,-6.933997,5.341535,3.417161,8.727411,3.687472,1.183818,4.929702,-4.985455,-5.745140,-8.445751,-8.133008,1.788708,-7.668150,0.085503,-3.494410,4.413176,0.945644,-8.954225,-2.080674,4.765302,-4.605548,6.028099,-5.919077,-1.362740,-3.345049,7.379100,8.395148,-7.437006,-9.223717,6.551761,-3.394272,-1.958807,7.376803,9.327926,-9.816492,7.238855,8.392693,-1.640627,-5.665477,-0.696701,8.588705,6.857393,-9.453062,-6.460209,6.079688,7.131978,-8.221507,5.617255,-2.148134,-4.283219,7.937124,4.068374,-2.830789,5.906435,-9.675545,-9.646039,7.312255,5.230159,9.805036,-8.669275,0.565588,1.566279,3.674149,2.078845,9.381939,-6.119434,-4.693592,5.197812,2.007039,1.553312,-1.294381,1.552331,-0.232391,6.033167,9.308955,-8.765368,0.504653,-2.281658,4.898538,-4.370192,0.886429,0.574327,-9.822239,9.002848,4.475421,7.211146,-2.257048,6.395851,6.681209,-7.683407,6.243874,4.525393,-9.848852,3.442378,-5.080065,-4.656770,2.167450,8.152209,-2.660968,6.509868,2.155693,9.499149,-9.826388,-4.719372,2.292702,-7.734941,-9.719832,6.640693,7.647838,-9.809238,-6.238657,-4.499552,-7.202770,2.625334,-8.480720,5.541617,-9.995823,5.486218,6.411700,-8.255801,-7.572943,1.350218,9.793722,-1.963893,-7.077887,-7.819851,1.468525], dtype = "float32")#candidate|5758|(288,)|const|float32
call_5757 = relay.TupleGetItem(func_1390_call(relay.reshape(const_5758.astype('float32'), [8, 6, 6])), 0)
call_5759 = relay.TupleGetItem(func_1392_call(relay.reshape(const_5758.astype('float32'), [8, 6, 6])), 0)
bop_5763 = relay.minimum(uop_5748.astype('int8'), relay.reshape(var_5747.astype('int8'), relay.shape_of(uop_5748))) # shape=(10, 3, 7)
func_4263_call = mod.get_global_var('func_4263')
func_4265_call = mutated_mod.get_global_var('func_4265')
call_5767 = func_4263_call()
call_5768 = func_4263_call()
bop_5769 = relay.less(bop_5763.astype('bool'), relay.reshape(uop_5748.astype('bool'), relay.shape_of(bop_5763))) # shape=(10, 3, 7)
output = relay.Tuple([call_5757,const_5758,call_5767,bop_5769,])
output2 = relay.Tuple([call_5759,const_5758,call_5768,bop_5769,])
func_5778 = relay.Function([var_5747,], output)
mod['func_5778'] = func_5778
mod = relay.transform.InferType()(mod)
mutated_mod['func_5778'] = func_5778
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5779 = relay.var("var_5779", dtype = "float64", shape = (10, 3, 7))#candidate|5779|(10, 3, 7)|var|float64
func_5778_call = mutated_mod.get_global_var('func_5778')
call_5780 = func_5778_call(var_5779)
output = call_5780
func_5781 = relay.Function([var_5779], output)
mutated_mod['func_5781'] = func_5781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4791_call = mod.get_global_var('func_4791')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_5802 = func_4791_call()
call_5803 = func_4791_call()
func_1306_call = mod.get_global_var('func_1306')
func_1309_call = mutated_mod.get_global_var('func_1309')
const_5827 = relay.const([-8,9,-7,1,-3,2,2,-1,2,2,6,6,-5,1,4,-4,-2,10,-9,-9,-7,-2,-6,-3,-8,-10,7,6,-4,-9,-6,-1,-5,-8,-3,7,-8,9,1,2,-9,2,8,-7,-9,-1,1,-3,-4,-1,10,8,-8,-1,1,10,6,7,2,-8,-2,5,-2,2,-1,-4,-2,10,1,2,-7,-3,4,8,-4,8,9,1,-4,-9,5,-8,8,-10,-9,3,3,-8,-6,3,-7,5,-4,7,-1,-5,-4,5,2,2,-8,-7,1,-5,6,-6,-9,-8,9,-5,4,7,4,9,-7,-7,-8,-5,-2,5,-10,-10,3,-4,-3,-5,8,4,-3,-7,-8,7,-9,-4,-3,-6,9,2,3,-4,-4,5,10,5,4,8,-6,-7,-7,7,-9,5,-8,10,4,10,-5,-1,4,-2,7,2,5,10,10,6,-10,-5,-9,-2,9,2,-6,-10,-8,-9,-2,-10,-10,-1,-8,10,-9,10,2,-2,5,6,6,2,-6,-8,-3,7,9,-4,6,-8,-10,4,2,2,1,-9,-4,10,-3,10,7,7,-5,4,8,-6,-2,-10,-8,2,-2,6,-3,8,5,9,-5,-7,-9,4,6,-6,2,-3,-2,-2,7,10,2,-5,8,-8,-10,5,-9,9,-9,-2,-4,-3,-1,1,-3,-7,3,-4,5,5,-9,9,9,1,-6,1,1,6,-9,1,10,-6,1,-3,2,-4,-10,8,2,9,6,7,6,-9,-10,6,8,4,-4,6,7,-8,2,6,5,1,5,-9,1,5,-6,-3,7,-4,6,-6,1,-10,9,-6,-1,-8,-4,9,-2,-7,9,5,-9,6,10,-10,7,-3,-6,-5,-7,-7,-9,-4,-5,1,3,10,4,7,10,-4,-7,-5,7,4,-2,-3,-9,2,-10,-8,9,-2,3,-1,-7,2,-2,-9,-9,-3,5,-4,2,8,8,-4,-3,-4,-8,-1,-9,-10,-4,-2,-3,-5,-10,3,-4,-6,9,1,-6,10,9,-8,-8,9,-9,-6,5,-1,10,-9,-6,-9,4,-9,-5,4,-4,-2,1,4,-4,2,-4,6,-8,-8,-9,1,7,2,1,-5,10,-7,3,-1,-4,8,-8,1,1,-10,8,-4,1,8,3,7,3,4,-7,-4,-10,8,9,3,3,-10,3,8,1,-8,-9,6,8,9,7,-6,-6,-4,-8,-6,-8,-1,-2,7,-5,6,9,-8,-3,2,-8,6,5,-10,-5,-3,5,-4,-5,10,5,5,-1,-10,-8,4,-1,10,10,-8,-8,-8,6,-10,4,-2,6,-4,8,1,4,-4,8,2,5,3,-2,-4,2,1,4,4,1,-8,1,9,-7,-2,-6,-2,-6,-2,-5,-7,2,2,3,9,3,-7,9,2,6,2,8,-2,-1,3,3,-1,-9,-5,9,10,-1,8,2,7,-4,9,5,8,-6,-1,10,7,5,6,6,-9,3,-9,9,-3,5,7,-3,-5,8,1,-8,-9,-8,10,-3,1,6,10,-5,10,-5,1,4,1,2,1,-8,-4,7,2,-2,-5,4,8,10,-1,-7,-5,6,4,-7,9,-5,-4,8,-4,3,-1,-7,-8,6,-2,-10,5,-2,-6,-4,-4,10,3,6,-10,-9,7,9,4,5,-10,2,2,2,3,-7,-7,5,-6,-9,1,7,-7,5,4,7,4,-9,3,6,-7,3,9,6,-2,-2,-5,2,5,-1,-7,3,8,-8,3,-9,7,6,3,-1,-9,7,-2,-3,-8,6,-5,-7,-2,5,10,-10,7,5,10,-2,-9,-2,-2,7,-1,5,5,10,8,-5,-1,-5,10,6,-6,-8,1,-5,7,5,7,4,4,9,1,-2,8,-1,-9,-10,-7,-1,10,-3,10,-5,-8,10,6,5,5,10,-7,4,7,-1,6,-5,10,5,8,8,10,-9,7,-4,1,6,2,-2,-5,5,6,8,-10,5,-1,-5,9,9,-7,-8,4,4,3,-5,2,-8,10,2,8,-1,10,-2,-7,7,-2,2,-9,4,-4,-2,8,5,-7,1,6,-4,7,7,9,-10,9,8,8,-1,10,-1,5,-10,4,-8,3,-9,10,-4,8,-1,-6,4,-1,-8,-10,1,6,-8,1,3,9,-4,-5,-7,2,1,-7,2,10,8,1,-5,-1,9,8,7,3,-8,2,3,-3,10,9,-9,1,1,9,1,1,-3,2,-8,-1,-5,-2,-7,-3,7,10,-3,3,5,9,3,5,-1,-6,-4,-3,-10,-7,10,-5,-4,-2,5,10,-9,-7,-1,8,1,-10,1,-4,-8,9,5,-6,-6,-7,-8,-3,7,1,2,1,1,8,7,-4,-5,5,-4,8,-3,-3,1,10,-9,8,-8,5,-10,-3], dtype = "int16")#candidate|5827|(896,)|const|int16
call_5826 = func_1306_call(relay.reshape(const_5827.astype('int16'), [8, 7, 16]), relay.reshape(const_5827.astype('int16'), [8, 7, 16]), )
call_5828 = func_1306_call(relay.reshape(const_5827.astype('int16'), [8, 7, 16]), relay.reshape(const_5827.astype('int16'), [8, 7, 16]), )
func_4179_call = mod.get_global_var('func_4179')
func_4180_call = mutated_mod.get_global_var('func_4180')
call_5836 = func_4179_call()
call_5837 = func_4179_call()
output = relay.Tuple([call_5802,call_5826,const_5827,call_5836,])
output2 = relay.Tuple([call_5803,call_5828,const_5827,call_5837,])
func_5839 = relay.Function([], output)
mod['func_5839'] = func_5839
mod = relay.transform.InferType()(mod)
mutated_mod['func_5839'] = func_5839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5839_call = mutated_mod.get_global_var('func_5839')
call_5840 = func_5839_call()
output = call_5840
func_5841 = relay.Function([], output)
mutated_mod['func_5841'] = func_5841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4680_call = mod.get_global_var('func_4680')
func_4682_call = mutated_mod.get_global_var('func_4682')
call_5847 = relay.TupleGetItem(func_4680_call(), 3)
call_5848 = relay.TupleGetItem(func_4682_call(), 3)
output = relay.Tuple([call_5847,])
output2 = relay.Tuple([call_5848,])
func_5868 = relay.Function([], output)
mod['func_5868'] = func_5868
mod = relay.transform.InferType()(mod)
output = func_5868()
func_5869 = relay.Function([], output)
mutated_mod['func_5869'] = func_5869
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5877 = relay.const([[[-9.055366,1.836093,5.319116,-1.439404,8.116825,1.911777,-6.067580,-0.249803,-7.213758,-5.501990,8.294289,0.763999,3.784555,-9.610233],[8.249631,2.537283,0.438030,-0.192637,0.594760,-2.951175,1.199731,9.568335,-3.164636,9.590914,-2.606990,-3.615619,-9.880252,-2.379381],[8.279691,-4.015499,-0.921795,-0.494191,-8.499810,-0.784409,-4.147370,5.357707,6.608378,6.765321,-3.459076,-1.140440,-5.706225,-5.748331],[0.388743,6.363145,8.791987,1.909167,9.839758,6.330458,-9.360482,0.452428,-1.062848,6.798134,9.370077,-7.056811,1.467416,-4.548155],[6.841476,3.165642,8.723386,0.407021,-4.821772,2.000310,-5.871777,6.864094,-3.179951,9.368601,9.085397,-7.865221,-3.978598,-7.632007],[-5.252649,1.991078,8.188750,-4.023474,6.201138,-6.167770,-3.474839,0.821246,-4.360477,-5.174473,-1.082271,-6.325620,-6.805543,-9.109203],[9.180795,-6.500295,-2.787866,7.392743,-4.156618,-2.611341,2.528977,0.625669,-5.420568,-3.596687,-1.587256,-7.515021,7.773933,-7.452862],[6.803709,-3.712029,-3.088600,-3.654997,-4.040225,-3.644046,7.619137,1.581940,8.084678,6.885463,4.697510,7.897709,-0.366571,-4.771672],[-1.451665,2.484591,-1.898927,-0.291245,-9.005551,6.496982,-6.719472,-8.878987,-6.973820,-6.455815,-1.604365,-2.738305,2.194065,3.552372],[5.237614,1.601749,6.977445,9.629738,-4.750679,-9.999700,0.797223,-2.535431,4.939554,5.321349,-9.692756,-1.962820,8.338054,-9.953329],[-1.152139,-1.181435,-3.322604,6.525258,-3.951327,8.139384,-1.526098,-3.046552,8.194114,4.288469,0.812025,-9.037950,-7.608158,-9.060017],[9.771475,-0.059034,6.798342,3.426790,1.692266,2.758829,-0.843447,-3.069630,-1.871817,-8.462646,8.430923,-6.848489,-0.247878,-0.487063],[9.869563,1.058492,-6.716549,-3.160331,-9.261704,0.985661,-1.200231,-0.538224,3.468415,5.776511,1.876127,8.500971,7.102029,3.056644],[-8.886331,-6.555001,-4.049392,5.170403,-4.150861,-4.477644,1.580881,-4.266989,-5.767470,-3.091917,8.749552,4.573286,8.971417,-8.328445],[5.642744,4.536040,4.995085,0.087598,5.692305,-7.390887,8.173772,-4.208980,-3.812982,-7.224492,2.013550,-0.256356,2.323168,7.505222],[-1.033573,3.446451,3.004955,-1.291651,2.559257,1.078089,-1.120672,-1.757131,-6.517387,-0.223953,5.837972,-8.062031,-6.787188,8.686090]],[[-9.564459,-2.392926,-8.384594,-9.559078,-7.640809,7.627941,8.975241,-9.342385,-8.070747,3.233720,-5.334245,-0.854203,-0.481561,-5.402809],[2.229772,-4.616698,0.298921,5.086675,0.805476,2.298946,-4.220741,4.651579,9.779891,7.320725,-6.266298,5.097731,-8.140344,-0.743933],[-3.652826,5.974465,-5.052211,1.336842,0.562140,-6.109014,1.019103,-3.703060,-5.632673,2.639180,-5.088185,5.865797,9.867621,8.838949],[-2.071083,-1.256795,-4.468055,2.043411,-4.829895,-4.706783,2.239939,-3.864205,0.427001,-1.870252,-6.914205,1.213530,-9.024428,4.098973],[8.691157,3.663519,-9.931536,-3.323781,-0.869085,5.605164,0.854704,-6.289861,-6.072379,8.318159,5.294033,1.817934,2.976749,-2.141009],[-9.927603,5.422030,-8.685164,9.944550,-0.880516,-7.364435,2.676434,1.833354,0.344219,5.145461,-3.823800,9.539638,-2.416235,5.512774],[-6.057618,0.577810,6.838350,-0.825193,-6.375720,-3.211919,-4.994074,3.802648,0.252530,-7.423500,-1.058255,-7.336668,-5.853572,-9.927576],[2.090695,-0.654864,-3.323108,-3.282767,-3.783457,1.293574,-4.264995,4.536326,-0.185526,9.808456,-3.380046,1.695988,4.143955,9.299297],[3.131036,1.961368,-1.747673,-5.856430,8.195895,-9.203155,-7.540487,-1.706746,-3.249681,9.234813,-6.934040,-5.046174,-5.637404,1.187153],[4.016665,7.395687,0.433518,8.885933,-4.948355,-8.340493,-6.294022,8.904298,-8.028485,-0.628449,2.158711,-5.473738,-0.148080,-4.302467],[-2.835828,-7.247592,1.190347,-8.082159,-4.067325,-8.156446,-9.618807,6.405713,6.099358,4.451374,-1.757774,-2.792845,8.561688,-5.394964],[3.800271,-8.195301,-0.357268,-9.557860,-2.269778,-1.373157,-7.140775,3.811838,1.087310,-7.831566,0.749110,0.267488,1.065481,9.806833],[-2.734457,-9.462954,0.559534,3.039621,2.673145,4.321153,-5.343852,4.737546,-4.770557,2.713065,0.657949,-6.903675,4.174546,-0.973575],[-1.051207,2.841354,6.741403,-3.764684,-5.067233,5.074281,2.308347,8.709281,-2.995280,2.867895,1.444679,2.771264,-0.072699,3.440096],[0.517895,-5.961950,-3.492001,-4.351076,3.150244,-7.699672,-7.650525,9.824997,-4.482826,5.739839,9.597292,6.452930,-5.196841,1.187270],[-2.869812,-4.988389,1.750981,4.475957,4.894157,5.485379,0.936913,-2.699104,5.589633,7.137612,2.613197,0.644045,8.427094,9.991616]],[[4.458920,-1.135796,-3.583324,1.663490,4.881003,4.682499,-3.354955,7.340708,-9.751739,8.656488,-4.569372,6.327672,5.628701,-0.370955],[0.008548,-0.277440,7.554682,-1.781876,-7.249956,4.023630,5.963205,-7.579526,8.997982,0.847871,8.059848,-4.545503,2.343840,6.307491],[-2.513083,-4.724662,-8.994559,-1.323249,9.507474,5.762491,-6.472201,-0.151146,1.400312,8.042922,-2.094850,-1.691157,8.559848,1.073319],[-1.320950,4.324955,9.419816,-4.374884,3.355787,7.358026,8.262772,-9.367575,0.200330,7.200326,6.916443,4.825232,8.689812,0.028389],[-9.216941,-0.247240,-1.097751,9.368576,1.123435,7.614515,-2.723270,6.042809,4.093954,1.611970,-8.679264,4.269375,6.760424,-9.084320],[-4.205667,7.510866,-3.833659,2.033359,-4.486421,-4.651368,-1.018400,-5.797806,-3.807587,-2.696331,9.510700,-1.946964,8.467062,1.866458],[6.683753,0.051301,6.547491,-2.724627,-3.541056,-9.149929,9.382025,-1.666153,-8.909536,-7.682743,9.471137,-8.721733,8.738216,-5.978708],[-1.517991,4.984451,0.244660,8.706741,-7.328432,9.750424,2.231322,7.452023,-2.598976,-2.251743,-7.913819,-0.286191,-1.417606,-2.951011],[1.638469,-2.659641,-5.481197,9.011670,-0.517314,-5.866570,9.652805,-2.841854,-5.767014,3.296801,7.894856,0.407196,-0.621579,4.473869],[5.640679,-1.838997,1.990561,-8.789687,3.905525,6.716123,6.082312,-1.253871,4.500274,9.432968,-8.915410,8.344398,3.145217,0.422527],[-4.978468,-8.852739,-2.612569,-7.871788,8.013933,9.461631,4.321775,-3.977563,-3.654507,1.939940,4.479862,0.967793,5.461652,-9.366420],[-8.457825,-1.867111,-8.714114,-6.148440,-1.488249,-6.317760,3.635015,-8.701330,5.821803,9.231890,8.768997,3.183085,-9.338671,-3.759226],[8.702716,-3.472881,-8.599601,-3.855557,8.843406,4.795394,-6.031506,9.993533,1.502877,-7.342883,-9.753950,-0.285323,-5.482981,7.275425],[8.112151,-0.007735,-8.731970,-5.910089,6.697824,9.347183,5.681001,-7.708130,8.606723,4.495514,6.756916,3.417048,-8.471194,5.369739],[3.261265,8.702329,-4.537902,-9.549374,-7.969849,2.948264,2.048461,-4.749296,8.513339,-5.881776,-2.889184,0.735164,8.401774,3.933566],[0.090605,-4.321445,1.711867,5.989374,1.361894,-2.348948,-3.733549,-1.562076,6.290531,-2.347130,2.034554,6.525435,-0.572178,-2.841747]],[[7.048885,2.834779,-2.108455,5.641173,9.445441,-2.692488,-9.118315,-3.713720,-0.347964,8.250092,4.175081,7.411801,-4.436660,-3.107380],[6.868813,2.226033,5.079019,7.256163,-7.762064,3.364765,8.682815,8.235301,9.915911,-5.100382,-4.076456,4.038265,8.372527,-5.964115],[6.179146,4.860447,6.840336,3.827280,4.934614,6.308683,5.676404,-0.618981,-7.790737,1.249954,0.596290,2.007986,1.850255,-6.499756],[2.982189,-4.461901,2.161396,-2.099594,-6.540904,6.048550,-8.166801,-6.458053,-0.034737,0.914491,-1.489044,-0.043339,-1.874236,3.180338],[-8.664574,3.623404,-2.187393,-0.331993,7.364832,0.779930,-1.608510,3.906822,8.261309,-3.066353,-8.379141,-4.393014,-2.871128,8.651681],[-6.093144,-7.192621,-6.187703,9.909587,-3.920649,-2.015009,-9.274911,1.184037,7.483229,4.459911,-6.353125,-8.679311,6.450616,3.718912],[5.759127,4.435288,0.246208,-7.397666,8.538633,1.717943,8.991592,6.578237,8.860233,-4.302589,7.479753,4.016444,0.856648,1.020388],[-4.337949,5.176410,3.039907,3.461708,-3.046773,-2.249596,2.134256,9.171590,0.300929,-6.314561,-2.512412,4.550689,1.124259,7.642149],[-6.031489,5.921645,-9.850762,-8.571680,8.770246,-3.916102,4.093294,0.720873,-3.987416,3.574619,3.232067,-5.756304,-1.174878,-0.188812],[-2.997238,2.014393,-7.971671,6.808694,5.780105,-5.246470,-5.055070,-1.454686,0.487623,-4.869645,6.257665,4.525388,-1.844237,-0.241665],[-6.901356,-1.537036,-5.458088,7.233533,-9.780013,0.290074,3.495152,3.716278,0.151893,2.652270,3.271528,-5.763262,-8.836671,-5.105644],[-1.217449,0.277856,8.462451,5.121137,7.769674,-5.053482,-4.678135,4.809715,4.995715,8.415413,6.165751,5.544664,-4.831160,2.137418],[2.422751,0.116154,-5.272118,-5.542034,-4.918441,3.570090,0.632385,-2.997801,-4.223833,9.415961,-2.583665,-2.593685,9.703597,-6.207758],[4.900556,-0.939312,1.128135,-0.541378,3.358153,4.573643,6.535349,0.560812,-9.070633,-1.790298,-1.862095,-6.727082,-7.537957,-3.143139],[-0.084210,3.149526,-8.171105,5.205762,-5.603778,4.220061,-3.110234,3.476036,6.935953,-3.287121,-2.802035,-0.733828,-7.242539,2.460346],[8.413510,0.306288,3.653753,-7.264604,-8.686388,5.848962,4.977409,-9.890693,-1.232389,8.217689,7.304308,8.958976,-5.833205,-9.153739]],[[5.123044,4.744368,0.303863,-5.594880,-4.830546,-6.947454,-0.894074,0.436098,-2.411780,-7.947743,7.495867,-3.379847,1.804471,0.891855],[-2.030112,8.893711,6.477920,-8.313447,6.776160,1.710477,4.548616,-0.023974,-4.511823,-2.344100,-3.081859,6.178706,-0.759365,-0.455733],[0.503588,-1.999474,2.799296,3.992102,-2.031578,4.939371,6.174279,0.781638,-6.045890,-0.893620,7.643838,6.120871,0.165838,-3.007316],[-7.815782,-8.437205,-9.162255,9.761579,-8.121652,-5.356554,7.442989,-6.515577,4.122598,6.702380,0.192098,-0.811863,-6.933169,-0.331713],[-6.054014,-4.671830,6.385364,-7.158487,1.143621,6.879879,6.893738,-1.088501,5.737015,7.584699,0.520262,-7.691978,-2.685786,7.380523],[-6.549911,4.085695,-1.693337,-8.144971,-3.120519,5.692137,-0.229245,6.388074,2.209680,-5.007685,-6.060580,4.185906,7.419580,-8.525578],[-5.085617,-2.795677,-3.325507,0.851776,4.996099,-3.682443,-9.445409,0.191502,7.794548,-5.003014,4.775623,3.904641,-7.003285,7.123153],[9.990417,-4.498669,6.339643,-6.366260,-2.186712,8.078842,9.985492,6.721033,5.629710,4.364921,0.159794,2.463842,-7.397118,-1.323213],[4.526161,-9.990873,6.391049,-6.984240,-4.738525,-0.769565,-4.558071,-9.358940,-2.810336,-5.415049,9.975969,-6.017894,0.714086,3.132526],[-7.081606,4.473495,0.225271,-4.333525,-1.688362,5.237822,-1.604810,4.480197,9.673781,-5.700746,8.121679,-0.027833,-0.307856,4.080460],[-6.794035,-4.372622,-6.150035,0.824052,4.034880,-3.952209,-6.359351,-6.531564,-5.556724,-8.528621,-3.422457,9.837168,8.709548,-8.579916],[-3.454637,5.485255,-3.536486,2.083808,2.560883,-4.571052,3.337440,-2.598091,-5.512140,-6.980785,-8.674410,6.966016,4.864297,-1.019552],[-2.407166,9.583518,-2.157802,9.121323,-3.891424,2.184977,7.135698,-6.963761,1.766566,7.124427,-3.864518,-6.119036,-8.951438,0.097167],[-4.380084,-9.283970,-8.609741,9.049249,-9.286293,6.267241,7.256799,4.753070,-9.698443,8.876177,-5.153436,1.846204,-6.172800,-4.164682],[1.262093,7.640897,9.540440,-6.882719,0.110893,8.683975,3.493962,-4.820011,4.495998,3.318113,3.456582,2.901858,9.607450,-0.915671],[-9.104324,-2.785502,-6.905927,9.592326,4.618001,7.625905,2.547709,3.791971,9.972349,-9.473067,9.719603,-0.223545,-3.787283,-8.881028]],[[5.996030,-7.694845,0.589034,7.367768,-0.685884,-1.596619,2.912655,-8.953998,-7.043479,2.595838,8.082248,-8.799224,4.426434,5.383728],[2.151471,-2.445489,4.011382,-3.852078,1.081400,-1.116628,0.680621,-6.140218,7.019218,3.871620,-9.847576,9.587241,-7.558945,-3.278412],[0.474516,-4.276998,3.115756,7.959761,6.058204,-7.644701,1.544773,-6.362855,6.054940,5.382236,7.385908,-1.386837,1.754115,2.061986],[9.954506,-4.692207,9.896847,2.870966,2.417431,1.298720,2.656929,8.866872,8.056320,6.110394,-3.473237,6.179415,9.146183,7.531813],[1.971629,0.339446,-0.749074,6.088481,-4.520501,8.905612,5.578873,-7.796976,-6.194754,-9.305700,2.915155,-8.171767,-1.366465,9.496198],[9.661683,9.827554,9.436535,3.541150,-2.238240,1.349369,-7.250070,-1.899942,-5.393794,-5.939015,-8.439573,-6.352175,-7.174293,-4.984356],[-8.610990,-8.463470,-0.617259,-2.403255,-5.216846,-3.628456,7.359885,5.571202,-1.039606,8.891374,-1.490906,0.302990,-7.738169,-7.748946],[-3.333415,-1.960732,-9.499614,-1.603201,-5.324494,-7.483317,-8.472745,0.831252,4.097711,3.401518,-8.135153,-2.046122,-3.217827,9.538693],[4.498982,9.729151,-0.541200,-8.859969,0.363573,-0.119728,5.747576,-1.410860,1.104854,1.031175,6.507727,-4.383929,-6.565274,-3.645976],[-2.412830,9.148685,-0.472766,2.028885,-9.210062,3.266880,-5.205992,0.178015,3.001820,0.133033,1.249044,0.505671,-7.910577,-0.947434],[-0.383206,0.260142,1.018903,-8.226912,-7.620825,-2.702114,0.640957,-0.575825,3.910718,4.391353,2.033935,9.143045,-9.640884,1.922827],[-0.451448,1.480161,4.882344,2.413381,0.095134,-9.575612,4.731074,8.404439,-8.011545,-7.213976,7.813477,-7.913944,2.230710,-1.061548],[-8.728551,-2.457632,3.938705,5.173875,-9.326256,6.729213,-4.987361,3.681406,3.436081,-1.903939,-6.973440,5.101755,8.457168,1.213250],[-8.507018,-1.294371,0.946489,9.963068,-9.209327,6.847877,-5.945034,-6.483333,-5.698106,-3.309551,-6.487595,-8.839309,-9.339882,8.633866],[0.581759,-5.652526,-4.875176,0.527589,8.054494,-3.983698,4.853602,-3.138207,7.353488,8.280248,2.256482,6.218677,-9.704151,-9.195445],[3.064650,-1.934605,-5.635810,-5.923181,7.516623,2.167894,7.937824,-6.143740,3.017477,-5.905602,-1.219958,1.093315,2.331963,4.195896]],[[-2.434593,-1.028330,7.339740,-9.373476,1.499224,-3.764427,-1.503845,4.557396,-9.122035,3.589865,8.062343,-2.914617,7.406046,6.753361],[-2.224993,-8.678564,-7.846799,-9.031688,-3.268914,-4.688298,-8.261664,-2.900143,-8.275160,-8.782307,-7.991202,-7.046758,4.213024,2.069379],[-3.496663,7.685095,9.613342,4.204969,8.881885,-0.137482,9.780294,2.902692,9.951455,-8.064071,-7.421422,-0.520692,-7.184357,-2.810985],[0.240036,-8.488562,-2.346466,-3.242841,-5.964937,9.569874,-0.741443,7.886011,-7.536627,5.121432,-0.337438,9.232709,-9.494262,8.071726],[2.528965,-1.639942,9.150906,-0.371249,-9.462906,-8.827341,0.541738,-2.285577,5.693080,1.955122,4.216184,8.621783,-6.161144,-4.499437],[7.933354,-6.636417,7.369531,8.928250,5.846874,-1.265876,1.160695,-1.997775,-3.301360,-0.809440,-8.278404,-9.554817,-9.403704,-4.519252],[-3.686809,5.759397,-1.587606,-1.438690,-6.303966,9.975617,-9.478557,6.022186,-0.798774,-0.548706,5.871412,-4.771426,-0.638147,3.874659],[-4.207042,5.494615,-7.439444,-5.381412,-7.355186,-3.242318,0.158386,0.071897,6.393133,3.698862,-0.935136,-8.751747,-9.960309,-6.797688],[3.816407,6.460407,7.261064,1.500653,6.952965,-8.668102,-0.508598,-9.671735,-4.188002,1.562935,-9.775658,9.066788,-2.849302,-2.673964],[-9.186025,7.775496,-0.228563,-8.478127,-4.837690,8.332927,4.021732,3.850421,-0.469287,4.949205,8.757901,-9.604593,4.975513,0.812090],[-1.170893,-5.694009,-3.976620,-1.380773,-8.425210,-8.280073,-9.217189,-0.566149,8.270795,-1.367819,2.210641,2.283872,-1.520568,4.079370],[4.086449,-7.893769,-3.850167,6.276591,-6.022803,-3.925840,-4.559787,5.071512,-7.364191,-6.033317,-9.982523,-5.648336,3.381253,-7.181268],[7.003493,2.570659,-3.772189,-4.893265,6.970368,4.449800,-0.108646,-5.905669,-5.952816,4.315958,-8.875774,5.545159,-6.498886,-4.128655],[2.762541,-7.802194,-0.250291,7.065387,0.891319,-6.000589,4.446013,-0.911895,1.093467,-8.116516,7.498662,-5.882085,-0.825275,-9.223434],[1.868038,-2.844057,1.642957,-4.208010,-0.845033,2.227084,2.239006,-4.979732,0.324647,-9.143533,-1.631003,6.209633,4.150009,3.067963],[0.726296,-5.183018,-2.523081,5.084102,8.016627,-6.618633,3.188622,4.520893,6.248061,-3.064050,4.808379,2.379052,2.119322,4.953774]]], dtype = "float32")#candidate|5877|(7, 16, 14)|const|float32
var_5878 = relay.var("var_5878", dtype = "float32", shape = (7, 16, 14))#candidate|5878|(7, 16, 14)|var|float32
bop_5879 = relay.add(const_5877.astype('float32'), relay.reshape(var_5878.astype('float32'), relay.shape_of(const_5877))) # shape=(7, 16, 14)
bop_5882 = relay.floor_divide(const_5877.astype('float64'), relay.reshape(var_5878.astype('float64'), relay.shape_of(const_5877))) # shape=(7, 16, 14)
uop_5885 = relay.sinh(bop_5882.astype('float32')) # shape=(7, 16, 14)
func_219_call = mod.get_global_var('func_219')
func_223_call = mutated_mod.get_global_var('func_223')
const_5890 = relay.const([[6,5,-7,-7,-8,2,-3,4,-4,-9,-3,1,-1,-4,-4,-9,8,-2,-1,-8,9,2,7,-4,-6,6,-4,-5,-1,10,-9,8,2,-2,10,-3,-4,-1,-2,-1,-7,-10,-3,-8,5,-2,4,4,9,-9,8,1,9,-2,-8,9,-10,-6,3,-7,-1,-5,-8,-1,2,9,-3,1,-2,-3,4,6,3,8,8,-6,-4,-4]], dtype = "int16")#candidate|5890|(1, 78)|const|int16
const_5891 = relay.const([[-3,10,10,4,2,7,10,-8,5,-4,-10,9,5,-4,9,1,-6,-6,10,10,-7,6,6,4,7,-4,-8,7,-4,2,-1,-7,-3,-3,-4,7,-7,9,-6,7,-3,-2,-5,4,-2,-5,9,-9,-7,-7,3,-2,-4,-8,-6,-6,7,9,1,-3,2,-5,2,-5,-6,1,4,-2,6,3,-6,-10,8,-6,5,-1,7,-7,-2,7,-3,-7,-2,7,10,2,10,-8,-1,9,-4,-2,6,10,-10,-6,-7,-1,-4,7,-8,-10,10,9,4,9,8,-9,-9,-2,5,-1,3,-1,10,-10,8,-9,2,10,-5,4,-10,-8,9,7,10,-8,2,9,-9,2,-3,-6,8,8,6,-7,-4,-5,-6,9,-4,10,-8,10,2,-5,-3,-9,-8,6,-9,-10,7,6,-10,1,3,2,4,9,1,10,-6,7,-6,-7,6,-9,-3,-8,1,-8,3,-8,-9,-3,-2,6,-2,3,8,4,-7,6,-10,-4,-4,-7,-4,5,3,-6,1,-4,-9,-10,5,10,8,2,10,9,10,-2,1,10,5,9,-9,8,10,-4,3,6,10,7,6,6,4,-2,7,-8,-7,-8,-2,6,-4,4,4,7,10,4,2,3,9,-10,7,-9,-7,-3,-3,8,9,5,3,-7,-5,-10,10,2,1,8,-10,-4,-3,-5,-8,-4,-4,-10,10,-2,8,-4,5,10,10,4,2,-8,-7,-3,-5,-1,5,-9,-1,-10,3,7,-3,-4,4,4,5,3,4,-6,3,9,-9,5,-9,8,10,-10,4,-6,1,6,-2,10,7,7,3,9,4,3,10,7,-9,-3,-10,-3,6,1,-10,-4,-6,8,8,-1,-3,8,-6,-3,2,9,-4,-7,6,10,10,5,-6,-5,-2,7,-3,-9,9,-5,8,5,8,2,-9,-2,-8,-4,9,7,10,-7,8,-1,7,-8,-1,7,-4,-5,-3,3,-1,-6,-10,4,-6,2,-8,-2,10,2,-4,5,9,-2,-7,4,6,10,4,8,4,5,-7,-7,-9,-10,-7,1,-5,10,2,9,5,-7,-3,10,-7,1,6,-10,-8,-7,5,3,-3,-1,-9,4,-2,-5,-6,-4,2,4,3,2,-4,8,-7,1,-4,-4,3,-8,-10,9,10,8,9,1,-10,3,9,5,-2,5,-7,10,-8,-4,-3,-6,-4,-4,-10,5,5,-4,-1,2,5,1,6,-3,-2,-7,-10,6,7,9,5,7,-3,-6,-10,-10,-6,9,4,8,-9,-3,-8,-2,-10,-4,4,7,-4,4,1,-9,4,-9,-9,6,-2,8,-9,6,-3,4,-2,5,-4,-10,-2,10,-8,-4,-5,-9,-9,-8,-7,-8,5,-8,-3,-2,3,-1,-4,8,-9,-1,5,3,6,4,6,-2,6,-7,-2,-5,3,-9,-7,1,1,2,3,-4,9,-10,2,5,1,-6]], dtype = "int16")#candidate|5891|(1, 546)|const|int16
var_5892 = relay.var("var_5892", dtype = "float32", shape = (728,))#candidate|5892|(728,)|var|float32
call_5889 = relay.TupleGetItem(func_219_call(relay.reshape(const_5890.astype('int16'), [6, 1, 13]), relay.reshape(const_5891.astype('int16'), [6, 7, 13]), relay.reshape(var_5892.astype('float32'), [1, 728]), ), 3)
call_5893 = relay.TupleGetItem(func_223_call(relay.reshape(const_5890.astype('int16'), [6, 1, 13]), relay.reshape(const_5891.astype('int16'), [6, 7, 13]), relay.reshape(var_5892.astype('float32'), [1, 728]), ), 3)
bop_5897 = relay.floor_mod(var_5878.astype('float64'), relay.reshape(const_5877.astype('float64'), relay.shape_of(var_5878))) # shape=(7, 16, 14)
output = relay.Tuple([bop_5879,uop_5885,call_5889,const_5890,const_5891,var_5892,bop_5897,])
output2 = relay.Tuple([bop_5879,uop_5885,call_5893,const_5890,const_5891,var_5892,bop_5897,])
func_5903 = relay.Function([var_5878,var_5892,], output)
mod['func_5903'] = func_5903
mod = relay.transform.InferType()(mod)
var_5904 = relay.var("var_5904", dtype = "float32", shape = (7, 16, 14))#candidate|5904|(7, 16, 14)|var|float32
var_5905 = relay.var("var_5905", dtype = "float32", shape = (728,))#candidate|5905|(728,)|var|float32
output = func_5903(var_5904,var_5905,)
func_5906 = relay.Function([var_5904,var_5905,], output)
mutated_mod['func_5906'] = func_5906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4135_call = mod.get_global_var('func_4135')
func_4136_call = mutated_mod.get_global_var('func_4136')
call_5962 = relay.TupleGetItem(func_4135_call(), 1)
call_5963 = relay.TupleGetItem(func_4136_call(), 1)
uop_5972 = relay.atan(call_5962.astype('float32')) # shape=(13, 12, 4)
uop_5974 = relay.atan(call_5963.astype('float32')) # shape=(13, 12, 4)
output = uop_5972
output2 = uop_5974
func_5975 = relay.Function([], output)
mod['func_5975'] = func_5975
mod = relay.transform.InferType()(mod)
mutated_mod['func_5975'] = func_5975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mutated_mod.get_global_var('func_5975')
call_5976 = func_5975_call()
output = call_5976
func_5977 = relay.Function([], output)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6060 = relay.var("var_6060", dtype = "float32", shape = (10, 7, 11))#candidate|6060|(10, 7, 11)|var|float32
uop_6061 = relay.sigmoid(var_6060.astype('float32')) # shape=(10, 7, 11)
output = uop_6061
output2 = uop_6061
func_6071 = relay.Function([var_6060,], output)
mod['func_6071'] = func_6071
mod = relay.transform.InferType()(mod)
mutated_mod['func_6071'] = func_6071
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6072 = relay.var("var_6072", dtype = "float32", shape = (10, 7, 11))#candidate|6072|(10, 7, 11)|var|float32
func_6071_call = mutated_mod.get_global_var('func_6071')
call_6073 = func_6071_call(var_6072)
output = call_6073
func_6074 = relay.Function([var_6072], output)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5675_call = mod.get_global_var('func_5675')
func_5677_call = mutated_mod.get_global_var('func_5677')
call_6079 = relay.TupleGetItem(func_5675_call(), 0)
call_6080 = relay.TupleGetItem(func_5677_call(), 0)
func_1590_call = mod.get_global_var('func_1590')
func_1592_call = mutated_mod.get_global_var('func_1592')
call_6082 = relay.TupleGetItem(func_1590_call(), 0)
call_6083 = relay.TupleGetItem(func_1592_call(), 0)
func_1485_call = mod.get_global_var('func_1485')
func_1489_call = mutated_mod.get_global_var('func_1489')
var_6085 = relay.var("var_6085", dtype = "bool", shape = (24,))#candidate|6085|(24,)|var|bool
const_6086 = relay.const([[False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,True,False],[False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True],[True,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,True,True,True],[False,False,True,False,True,True,True,True,False,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,True,False,True],[False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,False,True],[True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True]], dtype = "bool")#candidate|6086|(6, 60)|const|bool
call_6084 = relay.TupleGetItem(func_1485_call(relay.reshape(var_6085.astype('bool'), [6, 1, 4]), relay.reshape(const_6086.astype('bool'), [6, 15, 4]), ), 0)
call_6087 = relay.TupleGetItem(func_1489_call(relay.reshape(var_6085.astype('bool'), [6, 1, 4]), relay.reshape(const_6086.astype('bool'), [6, 15, 4]), ), 0)
var_6102 = relay.var("var_6102", dtype = "bool", shape = (6, 15, 4))#candidate|6102|(6, 15, 4)|var|bool
bop_6103 = relay.right_shift(call_6084.astype('int32'), relay.reshape(var_6102.astype('int32'), relay.shape_of(call_6084))) # shape=(6, 15, 4)
bop_6106 = relay.right_shift(call_6087.astype('int32'), relay.reshape(var_6102.astype('int32'), relay.shape_of(call_6087))) # shape=(6, 15, 4)
func_4498_call = mod.get_global_var('func_4498')
func_4499_call = mutated_mod.get_global_var('func_4499')
call_6145 = func_4498_call()
call_6146 = func_4498_call()
uop_6174 = relay.exp(call_6145.astype('float64')) # shape=(24, 22)
uop_6176 = relay.exp(call_6146.astype('float64')) # shape=(24, 22)
output = relay.Tuple([call_6079,call_6082,var_6085,const_6086,bop_6103,uop_6174,])
output2 = relay.Tuple([call_6080,call_6083,var_6085,const_6086,bop_6106,uop_6176,])
func_6178 = relay.Function([var_6085,var_6102,], output)
mod['func_6178'] = func_6178
mod = relay.transform.InferType()(mod)
mutated_mod['func_6178'] = func_6178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6178_call = mutated_mod.get_global_var('func_6178')
var_6180 = relay.var("var_6180", dtype = "bool", shape = (24,))#candidate|6180|(24,)|var|bool
var_6181 = relay.var("var_6181", dtype = "bool", shape = (6, 15, 4))#candidate|6181|(6, 15, 4)|var|bool
call_6179 = func_6178_call(var_6180,var_6181,)
output = call_6179
func_6182 = relay.Function([var_6180,var_6181,], output)
mutated_mod['func_6182'] = func_6182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3358_call = mod.get_global_var('func_3358')
func_3359_call = mutated_mod.get_global_var('func_3359')
call_6190 = func_3358_call()
call_6191 = func_3358_call()
output = relay.Tuple([call_6190,])
output2 = relay.Tuple([call_6191,])
func_6198 = relay.Function([], output)
mod['func_6198'] = func_6198
mod = relay.transform.InferType()(mod)
output = func_6198()
func_6199 = relay.Function([], output)
mutated_mod['func_6199'] = func_6199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5868_call = mod.get_global_var('func_5868')
func_5869_call = mutated_mod.get_global_var('func_5869')
call_6207 = relay.TupleGetItem(func_5868_call(), 0)
call_6208 = relay.TupleGetItem(func_5869_call(), 0)
func_2754_call = mod.get_global_var('func_2754')
func_2757_call = mutated_mod.get_global_var('func_2757')
var_6210 = relay.var("var_6210", dtype = "float32", shape = (288,))#candidate|6210|(288,)|var|float32
call_6209 = relay.TupleGetItem(func_2754_call(relay.reshape(var_6210.astype('float32'), [288,])), 0)
call_6211 = relay.TupleGetItem(func_2757_call(relay.reshape(var_6210.astype('float32'), [288,])), 0)
output = relay.Tuple([call_6207,call_6209,var_6210,])
output2 = relay.Tuple([call_6208,call_6211,var_6210,])
func_6238 = relay.Function([var_6210,], output)
mod['func_6238'] = func_6238
mod = relay.transform.InferType()(mod)
mutated_mod['func_6238'] = func_6238
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6239 = relay.var("var_6239", dtype = "float32", shape = (288,))#candidate|6239|(288,)|var|float32
func_6238_call = mutated_mod.get_global_var('func_6238')
call_6240 = func_6238_call(var_6239)
output = call_6240
func_6241 = relay.Function([var_6239], output)
mutated_mod['func_6241'] = func_6241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3510_call = mod.get_global_var('func_3510')
func_3511_call = mutated_mod.get_global_var('func_3511')
call_6290 = relay.TupleGetItem(func_3510_call(), 0)
call_6291 = relay.TupleGetItem(func_3511_call(), 0)
output = call_6290
output2 = call_6291
func_6314 = relay.Function([], output)
mod['func_6314'] = func_6314
mod = relay.transform.InferType()(mod)
mutated_mod['func_6314'] = func_6314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6314_call = mutated_mod.get_global_var('func_6314')
call_6315 = func_6314_call()
output = call_6315
func_6316 = relay.Function([], output)
mutated_mod['func_6316'] = func_6316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6322 = relay.var("var_6322", dtype = "float32", shape = (10, 14, 9))#candidate|6322|(10, 14, 9)|var|float32
uop_6323 = relay.exp(var_6322.astype('float32')) # shape=(10, 14, 9)
output = relay.Tuple([uop_6323,])
output2 = relay.Tuple([uop_6323,])
func_6325 = relay.Function([var_6322,], output)
mod['func_6325'] = func_6325
mod = relay.transform.InferType()(mod)
mutated_mod['func_6325'] = func_6325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6326 = relay.var("var_6326", dtype = "float32", shape = (10, 14, 9))#candidate|6326|(10, 14, 9)|var|float32
func_6325_call = mutated_mod.get_global_var('func_6325')
call_6327 = func_6325_call(var_6326)
output = call_6327
func_6328 = relay.Function([var_6326], output)
mutated_mod['func_6328'] = func_6328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2570_call = mod.get_global_var('func_2570')
func_2572_call = mutated_mod.get_global_var('func_2572')
call_6353 = relay.TupleGetItem(func_2570_call(), 0)
call_6354 = relay.TupleGetItem(func_2572_call(), 0)
output = call_6353
output2 = call_6354
func_6364 = relay.Function([], output)
mod['func_6364'] = func_6364
mod = relay.transform.InferType()(mod)
mutated_mod['func_6364'] = func_6364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6364_call = mutated_mod.get_global_var('func_6364')
call_6365 = func_6364_call()
output = call_6365
func_6366 = relay.Function([], output)
mutated_mod['func_6366'] = func_6366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5039_call = mod.get_global_var('func_5039')
func_5041_call = mutated_mod.get_global_var('func_5041')
call_6401 = func_5039_call()
call_6402 = func_5039_call()
func_5778_call = mod.get_global_var('func_5778')
func_5781_call = mutated_mod.get_global_var('func_5781')
var_6417 = relay.var("var_6417", dtype = "float64", shape = (210,))#candidate|6417|(210,)|var|float64
call_6416 = relay.TupleGetItem(func_5778_call(relay.reshape(var_6417.astype('float64'), [10, 3, 7])), 3)
call_6418 = relay.TupleGetItem(func_5781_call(relay.reshape(var_6417.astype('float64'), [10, 3, 7])), 3)
output = relay.Tuple([call_6401,call_6416,var_6417,])
output2 = relay.Tuple([call_6402,call_6418,var_6417,])
func_6419 = relay.Function([var_6417,], output)
mod['func_6419'] = func_6419
mod = relay.transform.InferType()(mod)
mutated_mod['func_6419'] = func_6419
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6420 = relay.var("var_6420", dtype = "float64", shape = (210,))#candidate|6420|(210,)|var|float64
func_6419_call = mutated_mod.get_global_var('func_6419')
call_6421 = func_6419_call(var_6420)
output = call_6421
func_6422 = relay.Function([var_6420], output)
mutated_mod['func_6422'] = func_6422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5361_call = mod.get_global_var('func_5361')
func_5363_call = mutated_mod.get_global_var('func_5363')
call_6430 = func_5361_call()
call_6431 = func_5361_call()
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_6452 = relay.TupleGetItem(func_2162_call(), 0)
call_6453 = relay.TupleGetItem(func_2164_call(), 0)
output = relay.Tuple([call_6430,call_6452,])
output2 = relay.Tuple([call_6431,call_6453,])
func_6463 = relay.Function([], output)
mod['func_6463'] = func_6463
mod = relay.transform.InferType()(mod)
output = func_6463()
func_6464 = relay.Function([], output)
mutated_mod['func_6464'] = func_6464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6314_call = mod.get_global_var('func_6314')
func_6316_call = mutated_mod.get_global_var('func_6316')
call_6473 = func_6314_call()
call_6474 = func_6314_call()
uop_6483 = relay.sqrt(call_6473.astype('float32')) # shape=(88,)
uop_6485 = relay.sqrt(call_6474.astype('float32')) # shape=(88,)
output = uop_6483
output2 = uop_6485
func_6486 = relay.Function([], output)
mod['func_6486'] = func_6486
mod = relay.transform.InferType()(mod)
mutated_mod['func_6486'] = func_6486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6486_call = mutated_mod.get_global_var('func_6486')
call_6487 = func_6486_call()
output = call_6487
func_6488 = relay.Function([], output)
mutated_mod['func_6488'] = func_6488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2935_call = mod.get_global_var('func_2935')
func_2936_call = mutated_mod.get_global_var('func_2936')
call_6493 = relay.TupleGetItem(func_2935_call(), 0)
call_6494 = relay.TupleGetItem(func_2936_call(), 0)
func_1870_call = mod.get_global_var('func_1870')
func_1874_call = mutated_mod.get_global_var('func_1874')
var_6499 = relay.var("var_6499", dtype = "float32", shape = (130,))#candidate|6499|(130,)|var|float32
var_6500 = relay.var("var_6500", dtype = "int16", shape = (78,))#candidate|6500|(78,)|var|int16
var_6501 = relay.var("var_6501", dtype = "float32", shape = (1, 728))#candidate|6501|(1, 728)|var|float32
call_6498 = relay.TupleGetItem(func_1870_call(relay.reshape(var_6499.astype('float32'), [5, 13, 2]), relay.reshape(var_6500.astype('int16'), [78,]), relay.reshape(var_6501.astype('float32'), [728, 1]), ), 6)
call_6502 = relay.TupleGetItem(func_1874_call(relay.reshape(var_6499.astype('float32'), [5, 13, 2]), relay.reshape(var_6500.astype('int16'), [78,]), relay.reshape(var_6501.astype('float32'), [728, 1]), ), 6)
output = relay.Tuple([call_6493,call_6498,var_6499,var_6500,var_6501,])
output2 = relay.Tuple([call_6494,call_6502,var_6499,var_6500,var_6501,])
func_6503 = relay.Function([var_6499,var_6500,var_6501,], output)
mod['func_6503'] = func_6503
mod = relay.transform.InferType()(mod)
var_6504 = relay.var("var_6504", dtype = "float32", shape = (130,))#candidate|6504|(130,)|var|float32
var_6505 = relay.var("var_6505", dtype = "int16", shape = (78,))#candidate|6505|(78,)|var|int16
var_6506 = relay.var("var_6506", dtype = "float32", shape = (1, 728))#candidate|6506|(1, 728)|var|float32
output = func_6503(var_6504,var_6505,var_6506,)
func_6507 = relay.Function([var_6504,var_6505,var_6506,], output)
mutated_mod['func_6507'] = func_6507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_6509 = func_5975_call()
call_6510 = func_5975_call()
const_6536 = relay.const([[[1.489511,-8.875925,0.155924,6.319038],[3.321253,-5.203867,-3.952258,-2.209870],[8.982954,6.823280,9.163997,6.553638],[-5.961955,-5.667511,-5.112007,-6.770212],[3.939498,-9.455181,-0.255727,-9.515860],[2.385453,-0.224137,1.985134,4.545720],[-6.595571,-1.033182,2.017217,7.518046],[-2.661099,9.434131,9.560881,0.353164],[9.390048,0.701957,5.619549,8.185816],[-4.066671,-0.060007,-1.169683,1.401033],[-7.431439,-2.410829,8.329667,-7.304871],[5.760947,-1.849385,3.566806,3.487126]],[[0.680358,-7.850081,5.240772,-4.712261],[-4.413184,1.109703,-4.613922,1.081929],[1.368512,-5.254237,5.742173,-5.708829],[7.252967,0.901214,-4.759315,5.801046],[7.785675,-1.211933,8.257626,2.213738],[1.391457,-5.037358,8.134594,2.697475],[6.966723,3.994479,-2.910777,5.720980],[5.438844,-1.547251,5.886697,5.787079],[-2.335864,2.766276,-8.659480,7.788506],[-3.336478,6.966287,5.064210,-4.327874],[7.935553,-4.743783,5.118109,8.621506],[-5.180376,9.656291,1.175753,2.190716]],[[-7.844238,7.809620,5.704124,6.869683],[-6.785932,7.664363,5.203993,-8.626152],[3.533994,-4.790434,-5.560190,6.881877],[3.639417,-9.049075,-5.752127,-1.502889],[2.330166,7.937175,-7.364726,-8.259662],[-7.375729,2.036519,6.067368,-0.403605],[-0.019507,0.966763,-1.975909,7.198005],[1.719035,-6.340296,9.657282,5.842001],[-4.930239,8.580931,1.814225,6.286912],[0.784497,0.642247,-9.085877,-0.206384],[-2.289764,6.921090,-9.531827,-7.645195],[-1.390565,8.955802,-5.930833,-1.448331]],[[-5.059895,8.505749,0.688851,7.113621],[2.702667,6.346494,-8.224940,-7.917044],[-6.407624,1.964110,5.281733,-2.560120],[-0.567687,3.356173,-1.625583,8.613813],[-9.349912,-1.263331,4.797888,-3.913169],[-7.238694,-0.412330,0.227149,6.130311],[-1.816418,1.881215,9.048985,1.993837],[0.820950,-4.934192,6.502847,-1.019192],[-6.853947,6.669956,-7.812966,1.474454],[-7.534459,6.835022,-8.949912,1.120099],[9.497635,-6.831515,-5.802896,-2.522108],[9.218857,-6.692029,-3.892361,-9.462895]],[[8.704215,-7.850690,8.305355,4.705545],[8.318318,-9.491713,0.484394,-7.410638],[-1.736475,8.346538,3.820778,-3.849541],[-9.405755,7.910334,-2.324571,-6.281053],[7.817235,6.189843,-0.263754,-7.260025],[-7.852405,6.515228,-0.632505,-1.366652],[7.883918,-7.396542,-4.057894,3.817556],[5.449100,7.609092,-6.056541,0.790069],[9.872649,-3.158571,1.788484,9.109946],[1.895392,-7.664793,3.189205,-7.162563],[-4.106571,8.345565,-6.478938,-5.852243],[6.241040,0.282274,8.142343,1.248000]],[[9.815918,-9.141689,1.958277,-1.457808],[-1.414093,-3.201216,-0.223692,-8.969208],[0.452868,3.253217,-3.659751,3.850407],[7.846581,7.947014,-4.091190,8.663352],[6.603812,-6.622874,-8.780072,8.331201],[1.465301,-6.240370,2.898937,3.482231],[-7.098577,-0.311201,-0.837322,-0.200554],[-8.846533,-7.454997,-0.810947,-2.100291],[4.925393,-9.832089,-8.084606,-0.875733],[-8.991012,1.474528,-9.523368,-4.707682],[8.684710,0.767707,1.785974,6.157207],[-7.616811,-8.813400,-5.928547,-4.941389]],[[2.488672,8.979963,-1.023209,-1.492521],[-7.418756,-9.069955,-8.395508,1.393861],[2.971864,8.282664,-9.556943,-0.585801],[-1.654083,1.154081,-4.795465,-4.952891],[6.220981,1.358898,7.754293,-6.968445],[1.181036,-9.600587,9.824214,1.215371],[7.425207,5.462711,6.843828,-8.145978],[-8.727053,-6.693373,5.617129,1.224550],[-8.776272,-6.830134,-7.042627,5.856348],[-5.071627,4.805214,4.578879,-5.129462],[0.153201,-8.682028,-8.588480,-9.773587],[3.857079,7.795182,4.157389,7.719924]],[[6.890245,5.496808,-7.037212,2.212285],[9.342152,-7.182047,4.738889,3.800796],[0.003958,6.707210,-8.120105,-6.789601],[9.359899,-5.450031,-9.405019,-5.201351],[3.157096,4.590579,5.562530,-8.791287],[8.315602,7.276069,-3.340889,7.619692],[5.664100,2.876600,-0.666079,6.789300],[2.233779,-3.031350,8.333901,2.728917],[1.191342,-9.269454,9.513115,8.186011],[8.996621,4.866948,4.026714,6.600484],[3.930938,-0.656170,6.392903,7.980964],[3.619732,-5.049702,0.423071,8.616159]],[[1.132330,2.077653,6.232120,8.186139],[9.671730,-9.288762,-8.220349,3.409758],[-1.493100,5.770705,9.375225,-0.674057],[3.795539,9.214883,-7.376207,2.707366],[-5.705852,-6.173218,7.670526,0.724546],[-7.559035,3.611323,7.340932,-4.780669],[-6.909234,0.291314,1.479886,-1.641276],[0.478559,6.352877,-2.564814,3.594290],[0.718168,-6.661967,9.891851,9.617215],[9.163423,-5.880548,-4.106469,-0.635508],[2.028695,-5.074963,1.011928,0.689996],[3.489663,-9.163534,9.348684,-3.035422]],[[2.318665,0.166376,-5.158837,-1.764820],[0.034710,2.370308,-1.393719,-2.544149],[1.370356,-8.719845,3.170038,6.024258],[-9.215613,-5.142163,8.058471,-2.119544],[-6.477433,-3.333722,-0.400984,-2.418877],[6.658506,8.502886,-6.233218,2.517407],[5.568220,-3.037664,2.113315,9.638349],[-6.731802,8.661068,-6.494205,-3.436473],[1.934527,-8.627391,-7.989009,6.526379],[-6.054968,6.673513,-7.700847,-4.698431],[-0.196314,-0.314208,5.578203,1.398103],[-4.194536,4.682371,-3.888399,9.507857]],[[-7.794748,1.674963,-5.596863,8.084015],[-1.425105,3.456577,2.251102,-6.031577],[8.982292,-1.604698,-5.204040,-2.931547],[-7.915492,1.930879,1.485503,0.447314],[-8.564659,-2.190750,9.886385,2.934424],[-1.420282,6.638999,1.933721,4.695203],[-6.935299,9.326957,2.656095,3.618542],[7.667207,-8.856791,6.141318,3.903515],[1.132942,7.663203,6.606368,-7.162933],[3.680762,3.026773,3.747111,8.011345],[-0.805695,-0.810186,-0.098837,-0.595586],[-2.553058,8.315374,-6.492559,-3.218278]],[[-6.791818,-5.402264,-3.717697,-5.083719],[-2.863978,-2.998775,-1.215872,-1.212972],[-4.522583,7.669368,-1.997417,7.490492],[-4.736237,6.406873,8.630374,-4.657441],[2.983663,4.242568,4.498030,9.726585],[9.546190,0.947548,-6.402783,2.308393],[-5.566927,3.424458,-6.312904,-0.168783],[7.228863,9.763545,7.868750,7.052069],[-0.818812,-0.968215,-5.941467,-1.107953],[-8.884663,1.438559,0.033775,5.736459],[0.284941,-7.824561,8.655536,0.826917],[-6.323919,5.532162,-0.110128,-7.630176]],[[9.377630,9.182424,9.360303,-4.669354],[1.555003,-8.502798,-9.234926,8.584569],[-9.155243,4.355834,-2.236074,8.589904],[8.276783,-5.716975,3.805394,-6.043981],[5.089825,-7.518410,7.533318,-9.716764],[-4.759492,8.691910,4.149958,6.384597],[9.956575,4.530943,5.108754,-3.461463],[-5.458880,-4.756803,-2.829985,-2.320739],[-7.856979,-3.879160,2.998787,4.463848],[7.473270,-5.732190,6.262051,-0.920933],[-3.046956,-3.539718,-3.905091,-2.547151],[9.001958,-3.215759,-6.952685,5.070660]]], dtype = "float32")#candidate|6536|(13, 12, 4)|const|float32
bop_6537 = relay.logical_or(call_6509.astype('bool'), relay.reshape(const_6536.astype('bool'), relay.shape_of(call_6509))) # shape=(13, 12, 4)
bop_6540 = relay.logical_or(call_6510.astype('bool'), relay.reshape(const_6536.astype('bool'), relay.shape_of(call_6510))) # shape=(13, 12, 4)
output = bop_6537
output2 = bop_6540
func_6547 = relay.Function([], output)
mod['func_6547'] = func_6547
mod = relay.transform.InferType()(mod)
mutated_mod['func_6547'] = func_6547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6547_call = mutated_mod.get_global_var('func_6547')
call_6548 = func_6547_call()
output = call_6548
func_6549 = relay.Function([], output)
mutated_mod['func_6549'] = func_6549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5698_call = mod.get_global_var('func_5698')
func_5700_call = mutated_mod.get_global_var('func_5700')
call_6609 = relay.TupleGetItem(func_5698_call(), 1)
call_6610 = relay.TupleGetItem(func_5700_call(), 1)
func_2754_call = mod.get_global_var('func_2754')
func_2757_call = mutated_mod.get_global_var('func_2757')
const_6618 = relay.const([-4.188771,-2.249846,0.664234,5.726826,4.197020,-0.886191,-3.207788,-1.969341,-6.379387,-5.987190,0.288195,6.355220,7.070310,0.337304,8.576040,-6.609627,-3.598322,-0.795841,5.883793,-1.032436,-2.191385,-9.912156,-7.333079,-0.818817,-1.533932,9.919078,-5.687681,-8.775829,4.603882,-8.349530,-4.382271,8.326665,0.250050,-2.585487,7.471420,-2.364880,9.098332,3.153021,2.332031,-7.873525,-4.574059,9.020792,-4.708110,-0.892194,6.909609,-3.258186,6.515684,-2.675703,4.488033,0.186887,-1.654734,1.297710,-2.442447,3.405361,-2.105291,8.687965,4.313407,3.253252,-0.711539,7.545746,-1.378785,2.824277,7.132606,2.705747,-4.349847,-7.964922,-6.872941,-7.638567,-5.640894,-7.900211,-0.102206,1.504863,-0.238984,9.063258,-5.704593,-7.625091,5.294125,-4.577293,4.444702,1.712329,-1.356568,-6.250001,1.332494,6.281116,-0.457637,7.905487,6.556375,-9.547583,0.177550,-7.034800,5.918193,0.507144,-0.157931,0.647241,0.310101,2.742717,-7.021001,-2.042488,-5.311857,2.117697,0.538279,9.919582,6.765147,-1.532889,-5.874374,-7.241203,0.437834,-6.781684,3.096637,3.937543,-0.626417,-6.675622,1.831778,6.584302,-0.695849,-5.513731,5.670190,-7.136036,-1.197325,4.794079,2.470201,-6.583611,7.655667,-5.615910,-5.598717,7.609867,-3.834994,-3.744935,-8.842654,-5.531834,-5.162768,-6.643343,-5.105443,0.280531,5.859034,2.192248,-0.486378,0.484972,-3.009594,5.199349,-2.198332,-6.870280,-7.028697,-2.678496,-4.116079,-8.451435,3.585560,-1.021635,5.181541,-2.049554,-1.423559,-5.478997,2.834866,8.778209,9.704882,8.214179,6.221979,6.354199,-9.409103,7.088601,-9.120466,5.062397,-8.014378,1.537879,4.994736,0.072205,-7.650358,4.820854,6.463263,0.382828,3.174573,-6.128300,-5.828194,-1.237097,8.006316,3.333477,8.573531,-3.644379,-1.078192,-6.005558,9.596720,-6.891809,7.976303,-9.836720,-5.683979,0.074511,-4.171729,-0.717052,5.577577,8.317525,-2.199226,-6.156442,5.125727,-6.312772,8.069288,-0.887937,-7.758690,-9.377149,-6.181137,-9.908774,-2.049934,-4.236105,-2.888884,-3.808022,3.865843,-4.093282,-3.450611,-9.159453,5.434239,-2.576042,3.148662,-1.124958,5.791373,0.549922,4.641794,-5.407740,5.003937,-4.837481,4.358340,-9.829881,-4.370860,0.938993,4.600237,-9.189835,-4.948511,8.478021,5.053594,6.433958,-9.464096,-1.938846,-4.840156,-1.478084,1.456487,9.953858,8.105232,-5.317555,4.393973,-9.369989,9.933502,7.375110,7.445617,9.573965,-6.794064,7.300748,6.716022,-8.172139,-1.232843,3.966434,7.222766,2.649469,-7.534450,-6.987488,6.241024,0.075331,-5.987861,-6.380549,7.153363,-2.583799,-1.353070,3.259367,-7.477595,1.146517,-2.978204,-1.129450,-9.209288,-9.938463,4.991815,-8.635545,1.167846,3.401516,-8.740577,-4.912716,2.602187,-5.842288,-7.106695,0.678729,0.931154,-2.587236,-2.625931,-1.247937,-1.678672,9.596178,5.812418,-6.866559,5.796239,-4.917284,1.130685,-1.060017], dtype = "float32")#candidate|6618|(288,)|const|float32
call_6617 = relay.TupleGetItem(func_2754_call(relay.reshape(const_6618.astype('float32'), [288,])), 2)
call_6619 = relay.TupleGetItem(func_2757_call(relay.reshape(const_6618.astype('float32'), [288,])), 2)
output = relay.Tuple([call_6609,call_6617,const_6618,])
output2 = relay.Tuple([call_6610,call_6619,const_6618,])
func_6630 = relay.Function([], output)
mod['func_6630'] = func_6630
mod = relay.transform.InferType()(mod)
mutated_mod['func_6630'] = func_6630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6630_call = mutated_mod.get_global_var('func_6630')
call_6631 = func_6630_call()
output = call_6631
func_6632 = relay.Function([], output)
mutated_mod['func_6632'] = func_6632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_6652 = func_5303_call()
call_6653 = func_5303_call()
output = relay.Tuple([call_6652,])
output2 = relay.Tuple([call_6653,])
func_6689 = relay.Function([], output)
mod['func_6689'] = func_6689
mod = relay.transform.InferType()(mod)
mutated_mod['func_6689'] = func_6689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6689_call = mutated_mod.get_global_var('func_6689')
call_6690 = func_6689_call()
output = call_6690
func_6691 = relay.Function([], output)
mutated_mod['func_6691'] = func_6691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3425_call = mod.get_global_var('func_3425')
func_3427_call = mutated_mod.get_global_var('func_3427')
call_6695 = relay.TupleGetItem(func_3425_call(), 1)
call_6696 = relay.TupleGetItem(func_3427_call(), 1)
func_4791_call = mod.get_global_var('func_4791')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_6700 = func_4791_call()
call_6701 = func_4791_call()
func_5778_call = mod.get_global_var('func_5778')
func_5781_call = mutated_mod.get_global_var('func_5781')
var_6703 = relay.var("var_6703", dtype = "float64", shape = (210,))#candidate|6703|(210,)|var|float64
call_6702 = relay.TupleGetItem(func_5778_call(relay.reshape(var_6703.astype('float64'), [10, 3, 7])), 0)
call_6704 = relay.TupleGetItem(func_5781_call(relay.reshape(var_6703.astype('float64'), [10, 3, 7])), 0)
output = relay.Tuple([call_6695,call_6700,call_6702,var_6703,])
output2 = relay.Tuple([call_6696,call_6701,call_6704,var_6703,])
func_6706 = relay.Function([var_6703,], output)
mod['func_6706'] = func_6706
mod = relay.transform.InferType()(mod)
var_6707 = relay.var("var_6707", dtype = "float64", shape = (210,))#candidate|6707|(210,)|var|float64
output = func_6706(var_6707)
func_6708 = relay.Function([var_6707], output)
mutated_mod['func_6708'] = func_6708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5698_call = mod.get_global_var('func_5698')
func_5700_call = mutated_mod.get_global_var('func_5700')
call_6744 = relay.TupleGetItem(func_5698_call(), 1)
call_6745 = relay.TupleGetItem(func_5700_call(), 1)
output = relay.Tuple([call_6744,])
output2 = relay.Tuple([call_6745,])
func_6760 = relay.Function([], output)
mod['func_6760'] = func_6760
mod = relay.transform.InferType()(mod)
output = func_6760()
func_6761 = relay.Function([], output)
mutated_mod['func_6761'] = func_6761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6779 = relay.var("var_6779", dtype = "int32", shape = ())#candidate|6779|()|var|int32
var_6780 = relay.var("var_6780", dtype = "int32", shape = (6, 6, 11))#candidate|6780|(6, 6, 11)|var|int32
bop_6781 = relay.less(var_6779.astype('bool'), var_6780.astype('bool')) # shape=(6, 6, 11)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_6784 = func_5190_call()
call_6785 = func_5190_call()
uop_6786 = relay.sinh(var_6780.astype('float64')) # shape=(6, 6, 11)
bop_6788 = relay.divide(uop_6786.astype('float32'), var_6779.astype('float32')) # shape=(6, 6, 11)
func_1306_call = mod.get_global_var('func_1306')
func_1309_call = mutated_mod.get_global_var('func_1309')
const_6792 = relay.const([3,2,-1,-4,2,4,8,5,-9,4,6,-5,2,-2,5,5,-1,10,2,8,4,3,2,-7,-5,-4,6,-9,5,1,7,10,5,-10,5,-2,-10,8,-7,2,-5,2,6,-10,-5,10,9,9,-9,-2,7,-1,10,-8,6,6,-6,3,-2,-2,-7,8,-2,9,-6,-8,-4,-1,-10,-1,8,-8,-10,4,-7,8,9,-10,-2,4,10,10,-3,-10,9,1,-3,-2,3,2,2,-4,5,-4,4,5,-10,-10,8,-5,-3,4,7,-6,2,10,9,5,-9,1,6,5,-2,10,7,9,-4,-6,1,-1,2,-6,-5,-7,1,6,-5,-5,8,-9,3,-4,10,-7,-4,3,8,-8,-2,7,-4,-1,8,8,-1,10,2,8,8,3,6,9,-5,8,4,1,8,1,-7,-1,-5,-10,-9,-10,-8,8,-9,7,-5,-1,10,-1,3,-6,10,-9,-10,-1,-1,-7,-4,-2,-3,-8,2,9,3,-2,-1,-9,6,3,10,7,7,-10,-1,5,-1,-6,4,7,-7,-8,-5,-9,-8,7,8,-9,9,7,2,-8,7,-6,-9,-2,9,-5,8,5,8,-4,-7,-1,-2,8,2,-5,-8,-10,3,5,2,6,4,8,3,-8,4,-7,-10,10,-1,-1,-7,7,-4,4,2,6,1,-8,5,-9,9,-5,2,-3,2,3,-4,1,-5,-4,5,3,-5,4,-10,8,8,-10,-1,-5,-6,6,9,10,2,-10,-5,7,-7,9,-4,9,-4,-4,2,10,8,-8,3,2,1,4,-7,5,2,3,4,-1,1,-3,-5,-10,1,1,-7,1,4,-3,6,7,3,7,-6,-4,-4,-1,-2,-3,1,6,6,6,-3,-1,7,9,1,-7,-4,3,10,6,-5,4,2,3,-5,6,-6,-7,8,-4,3,4,-2,3,1,1,-10,-1,5,10,1,-10,-4,1,-4,-9,-6,-4,1,8,9,-5,6,-1,10,-3,-7,9,1,-3,4,-1,8,9,-3,9,-10,-2,2,9,5,4,-8,-5,-2,-3,-2,-9,10,-10,-6,-6,3,3,1,9,8,8,-6,-3,1,7,2,6,5,-4,2,7,8,-3,6,5,-3,9,3,-8,-10,8,4,-4,7,-1,-10,6,-10,8,-9,1,-3,-1,-2,1,-7,-6,4,-9,-7,-1,9,-8,-4,-7,7,-5,8,-9,7,4,10,5,9,-4,-6,-7,10,-6,-10,-7,10,-1,10,-9,-9,-2,-3,2,3,-10,9,-4,1,-5,-4,1,-8,2,-10,6,-6,-10,-7,10,-6,-1,-8,-8,-6,1,9,3,2,-5,6,6,10,-10,-6,-7,3,-1,-4,1,4,-9,3,8,9,2,5,-7,1,1,2,-4,-7,-7,6,10,-9,2,-5,9,-6,-9,-6,5,8,9,-4,-4,-9,-4,6,-4,-5,6,1,-3,-6,-7,1,-2,-5,-8,5,2,10,1,-1,2,3,5,-3,10,-1,2,6,2,8,-4,9,-8,-3,-6,4,-10,7,-3,-4,-2,10,10,9,-1,9,1,-3,-8,8,1,-1,2,-6,10,10,8,5,7,-9,2,-4,-5,-2,5,6,-3,-7,-5,-10,5,-7,9,1,8,6,8,-5,-9,6,8,-10,-9,5,-1,10,-4,-1,1,-1,-3,-10,-7,6,3,-9,-1,1,-9,-5,1,8,-4,-10,-2,5,6,-8,4,10,-3,-8,10,-6,8,-9,9,-6,-6,-8,-7,-6,10,-7,-6,-2,6,5,3,-6,5,2,3,-6,6,7,-9,-6,7,-5,-10,3,-1,3,4,-5,-5,2,6,-6,4,-8,8,-3,-9,9,-7,5,-3,-10,-10,-5,-5,-2,4,5,-5,8,7,8,2,-5,-10,-5,-1,-9,3,5,-10,8,8,10,4,-7,-1,-7,2,10,-2,-6,-1,5,10,1,-8,-2,10,-10,-1,-7,1,5,-6,7,3,3,10,-7,8,10,7,-4,5,-3,-10,1,4,5,3,10,-7,10,-10,8,7,4,4,-10,2,5,4,1,2,-2,8,-10,4,2,7,2,2,7,-3,-2,2,7,5,-6,4,3,9,-8,-1,8,2,5,7,-9,1,-7,1,7,-2,5,2,-9,-1,-3,-7,2,3,5,-9,10,6,-3,1,-6,-4,8,-9,6,-6,-2,-1,4,4,-2,4,3,1,-8,5,-5,5,4,2,3,10,-1,-2,5,-6,10,-10,1,-8,-4,-5,3,-4,-5,8,4,-7,-9,2,6,-10,10,-9,1,-4,-2,6,10,-4,-4,-6,10,-5,-4,-2,7,-7,2,-1,-3,10,3,-1,-3,9,7,8,-9,-8,-10,-3,4,5,4,-1,-1,2,-6,-9,10,-8], dtype = "int16")#candidate|6792|(896,)|const|int16
call_6791 = func_1306_call(relay.reshape(const_6792.astype('int16'), [8, 7, 16]), relay.reshape(const_6792.astype('int16'), [8, 7, 16]), )
call_6793 = func_1306_call(relay.reshape(const_6792.astype('int16'), [8, 7, 16]), relay.reshape(const_6792.astype('int16'), [8, 7, 16]), )
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_6818 = relay.TupleGetItem(func_2162_call(), 2)
call_6819 = relay.TupleGetItem(func_2164_call(), 2)
uop_6831 = relay.sin(uop_6786.astype('float32')) # shape=(6, 6, 11)
output = relay.Tuple([bop_6781,call_6784,bop_6788,call_6791,const_6792,call_6818,uop_6831,])
output2 = relay.Tuple([bop_6781,call_6785,bop_6788,call_6793,const_6792,call_6819,uop_6831,])
func_6833 = relay.Function([var_6779,var_6780,], output)
mod['func_6833'] = func_6833
mod = relay.transform.InferType()(mod)
mutated_mod['func_6833'] = func_6833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6833_call = mutated_mod.get_global_var('func_6833')
var_6835 = relay.var("var_6835", dtype = "int32", shape = ())#candidate|6835|()|var|int32
var_6836 = relay.var("var_6836", dtype = "int32", shape = (6, 6, 11))#candidate|6836|(6, 6, 11)|var|int32
call_6834 = func_6833_call(var_6835,var_6836,)
output = call_6834
func_6837 = relay.Function([var_6835,var_6836,], output)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3383_call = mod.get_global_var('func_3383')
func_3385_call = mutated_mod.get_global_var('func_3385')
call_6852 = relay.TupleGetItem(func_3383_call(), 0)
call_6853 = relay.TupleGetItem(func_3385_call(), 0)
func_4946_call = mod.get_global_var('func_4946')
func_4948_call = mutated_mod.get_global_var('func_4948')
call_6854 = relay.TupleGetItem(func_4946_call(), 1)
call_6855 = relay.TupleGetItem(func_4948_call(), 1)
uop_6902 = relay.tan(call_6854.astype('float64')) # shape=(130,)
uop_6904 = relay.tan(call_6855.astype('float64')) # shape=(130,)
output = relay.Tuple([call_6852,uop_6902,])
output2 = relay.Tuple([call_6853,uop_6904,])
func_6907 = relay.Function([], output)
mod['func_6907'] = func_6907
mod = relay.transform.InferType()(mod)
mutated_mod['func_6907'] = func_6907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6907_call = mutated_mod.get_global_var('func_6907')
call_6908 = func_6907_call()
output = call_6908
func_6909 = relay.Function([], output)
mutated_mod['func_6909'] = func_6909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_6988 = func_2402_call()
call_6989 = func_2402_call()
output = relay.Tuple([call_6988,])
output2 = relay.Tuple([call_6989,])
func_6990 = relay.Function([], output)
mod['func_6990'] = func_6990
mod = relay.transform.InferType()(mod)
mutated_mod['func_6990'] = func_6990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6990_call = mutated_mod.get_global_var('func_6990')
call_6991 = func_6990_call()
output = call_6991
func_6992 = relay.Function([], output)
mutated_mod['func_6992'] = func_6992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6364_call = mod.get_global_var('func_6364')
func_6366_call = mutated_mod.get_global_var('func_6366')
call_6995 = func_6364_call()
call_6996 = func_6364_call()
output = call_6995
output2 = call_6996
func_7007 = relay.Function([], output)
mod['func_7007'] = func_7007
mod = relay.transform.InferType()(mod)
output = func_7007()
func_7008 = relay.Function([], output)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_7018 = func_5190_call()
call_7019 = func_5190_call()
output = call_7018
output2 = call_7019
func_7024 = relay.Function([], output)
mod['func_7024'] = func_7024
mod = relay.transform.InferType()(mod)
output = func_7024()
func_7025 = relay.Function([], output)
mutated_mod['func_7025'] = func_7025
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7033 = relay.var("var_7033", dtype = "float32", shape = (13, 5, 7))#candidate|7033|(13, 5, 7)|var|float32
uop_7034 = relay.asinh(var_7033.astype('float32')) # shape=(13, 5, 7)
uop_7045 = relay.asin(uop_7034.astype('float64')) # shape=(13, 5, 7)
output = relay.Tuple([uop_7045,])
output2 = relay.Tuple([uop_7045,])
func_7065 = relay.Function([var_7033,], output)
mod['func_7065'] = func_7065
mod = relay.transform.InferType()(mod)
mutated_mod['func_7065'] = func_7065
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7066 = relay.var("var_7066", dtype = "float32", shape = (13, 5, 7))#candidate|7066|(13, 5, 7)|var|float32
func_7065_call = mutated_mod.get_global_var('func_7065')
call_7067 = func_7065_call(var_7066)
output = call_7067
func_7068 = relay.Function([var_7066], output)
mutated_mod['func_7068'] = func_7068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7101 = relay.var("var_7101", dtype = "float32", shape = (16, 12, 10))#candidate|7101|(16, 12, 10)|var|float32
uop_7102 = relay.tan(var_7101.astype('float32')) # shape=(16, 12, 10)
output = relay.Tuple([uop_7102,])
output2 = relay.Tuple([uop_7102,])
func_7106 = relay.Function([var_7101,], output)
mod['func_7106'] = func_7106
mod = relay.transform.InferType()(mod)
var_7107 = relay.var("var_7107", dtype = "float32", shape = (16, 12, 10))#candidate|7107|(16, 12, 10)|var|float32
output = func_7106(var_7107)
func_7108 = relay.Function([var_7107], output)
mutated_mod['func_7108'] = func_7108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2641_call = mod.get_global_var('func_2641')
func_2643_call = mutated_mod.get_global_var('func_2643')
call_7112 = relay.TupleGetItem(func_2641_call(), 2)
call_7113 = relay.TupleGetItem(func_2643_call(), 2)
func_4032_call = mod.get_global_var('func_4032')
func_4034_call = mutated_mod.get_global_var('func_4034')
call_7116 = relay.TupleGetItem(func_4032_call(), 0)
call_7117 = relay.TupleGetItem(func_4034_call(), 0)
var_7132 = relay.var("var_7132", dtype = "uint32", shape = (24, 22))#candidate|7132|(24, 22)|var|uint32
bop_7133 = relay.maximum(call_7116.astype('float32'), relay.reshape(var_7132.astype('float32'), relay.shape_of(call_7116))) # shape=(24, 22)
bop_7136 = relay.maximum(call_7117.astype('float32'), relay.reshape(var_7132.astype('float32'), relay.shape_of(call_7117))) # shape=(24, 22)
func_2293_call = mod.get_global_var('func_2293')
func_2296_call = mutated_mod.get_global_var('func_2296')
const_7140 = relay.const([-3.490104,-1.244134,1.293868,-9.007428,6.571836,4.579284,8.999832,-2.129318,-3.369100,3.859546,-2.538737,-0.258708,-2.071874,8.211461,-8.798001,-4.036661,-1.655617,0.874787,6.212743,1.670408,-1.473658,0.977750,-9.213418,2.305424,8.642717,-0.970297,-0.930943,5.053977,3.745783,-4.140503,3.795982,0.528634,-8.595444,-1.542128,-7.690609,-6.318739,-9.134342,-2.449187,4.770778,1.659556,-6.037128,4.029743,-5.413859,8.389482,4.557180,3.211496,-5.148474,-8.108506,-5.731389,-1.083387,-2.149301,8.112936,7.858398,8.009470,5.561302,2.864171,-0.334281,7.179007,1.007955,1.814462,-0.950483,-9.368204,4.266177,8.126506,1.355999,-5.948094,4.610242,-6.826497,5.469656,4.361298,-6.686291,-0.914611,6.597200,-4.083396,-2.394146,6.009795,-1.639856,-4.844277,-7.600253,3.925948,0.250654,9.685562,-5.123669,1.106470,4.724162,-6.757435,8.552751,5.808014,-7.645069,-3.212464,8.199180,-6.518175,4.902029,3.307887,-7.334515,7.272362,-6.574497,-9.540121,-1.733609,-3.732759,6.238170,2.467444,9.026263,1.807864,-5.401322,-8.089366,-5.371988,-3.542065,1.750484,3.669504,-3.285840,-4.845299,-9.035882,9.492998,-7.266224,-0.082040,0.169541,2.572933,-4.783855,-2.049978,-2.316427,-9.859419,7.218282,-2.412204,-1.855824,8.499256,-2.960206,2.453789,-4.752334,3.805454,-0.765569,-4.915689,9.245753,-2.693678,1.427851,8.855556,-0.971459,-2.444114,-4.984644,-3.227351,-5.494997,4.333588,9.255063,4.142704,-2.297256,7.403968,8.983704,-6.400970,9.282756,-0.220284,1.981639,-8.591955,-0.775416,-0.641734,3.763941,9.490571,-7.700382,-1.854676,-3.675803,9.692029,-4.824472,5.658201,0.876530,-0.928917,7.285465,3.195893,-6.132681,-5.054663,-4.878527,6.042302,2.610489,5.539061,-9.867084,-4.965070,-4.754594,7.839755,-8.271470,-6.003910,-7.335804,-6.624764,3.815249,-9.371494,9.568458,-9.047895,4.799659,2.606183,6.130008,-5.999874,-0.142022,-7.298743,1.910557,7.625868,-2.390343,1.257452,-9.331742,-6.812724,6.792674,-7.849831,0.356314,-8.692679,-7.874315,-4.914374,-7.579425,6.321053,6.949542,7.473803,0.447738,-3.945148,-6.045282,-6.221447,3.455689,1.066443,-0.072054,1.361976,-1.188636,-4.247888,5.558021,-3.757673,-9.778043,-1.294452,3.903544,-2.588015,-0.072924,0.847282,-9.777173,9.610022,-2.966253,-0.129006,-1.714688,3.222361,3.885063,-3.875591,-8.163794,-8.792426,-2.189966,-8.125665,1.653260,9.625824,4.707217,-9.513272,-1.239692,7.278348,-2.530610,3.153209,7.899967,-6.283078,1.214408,3.829385,9.087951,-6.871109,-4.036961,-3.739363,4.264329,7.109115,-2.608074,-4.292722,0.830192,4.726861,9.496603,3.164289,0.177980,2.346352,-0.256430,-1.874682,-4.411159,2.724673,8.623875,-0.570550,9.547364,2.611767,-6.589583,1.392228,7.587801,3.104142,8.631973,4.750240,-2.473669,6.010424,6.831206,1.804159,-9.322614,-4.271987,-5.744354,-9.673057,-3.206880,2.203259,9.029334,7.376362,7.896084,0.122099,8.312845,-6.551066,1.612228,-8.333775,4.470233,8.418562,-1.348760,-2.313720,-6.635629,9.554666,-6.536250,4.714926,1.870130,0.975997,-7.513048,9.749576,3.939732,2.181741,-6.310747,-6.000924,1.682353,9.510505,6.310902,-1.586350,6.600621,3.856647,-2.210619,4.600327,2.406620,7.367045,-1.096508,3.007546,-8.072992,-9.198905,-8.119226,-3.210310,-0.219174,9.671756,8.012875,-1.736004,8.868161,3.517371,-7.742257,5.133016,3.820591,9.858096,-3.896842,3.082067,-1.996491,4.966658,-0.634560,-8.658365,0.544881,6.738157,-2.211168,6.285840,6.526637,3.440143,-4.917619,2.577459,1.841636,5.080947,5.442058,-4.184988,-7.188984,-5.126045,-0.448795,-8.075451,-9.301684,-4.211273], dtype = "float32")#candidate|7140|(360,)|const|float32
call_7139 = relay.TupleGetItem(func_2293_call(relay.reshape(const_7140.astype('float32'), [15, 12, 2])), 0)
call_7141 = relay.TupleGetItem(func_2296_call(relay.reshape(const_7140.astype('float32'), [15, 12, 2])), 0)
output = relay.Tuple([call_7112,bop_7133,call_7139,const_7140,])
output2 = relay.Tuple([call_7113,bop_7136,call_7141,const_7140,])
func_7147 = relay.Function([var_7132,], output)
mod['func_7147'] = func_7147
mod = relay.transform.InferType()(mod)
mutated_mod['func_7147'] = func_7147
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7148 = relay.var("var_7148", dtype = "uint32", shape = (24, 22))#candidate|7148|(24, 22)|var|uint32
func_7147_call = mutated_mod.get_global_var('func_7147')
call_7149 = func_7147_call(var_7148)
output = call_7149
func_7150 = relay.Function([var_7148], output)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1620_call = mod.get_global_var('func_1620')
func_1622_call = mutated_mod.get_global_var('func_1622')
call_7172 = func_1620_call()
call_7173 = func_1620_call()
func_6503_call = mod.get_global_var('func_6503')
func_6507_call = mutated_mod.get_global_var('func_6507')
const_7183 = relay.const([-2.145087,3.289034,-0.763288,4.981162,-6.317066,6.516165,-4.269118,4.450323,9.345589,-5.719259,-0.447550,2.666159,-1.973673,2.467298,-6.803431,5.118039,-6.756777,-4.103809,-0.472460,-9.009887,-5.227245,3.467935,-2.592514,7.222390,7.718592,4.422672,-5.258558,-5.532617,-1.439467,-2.607650,1.956197,-7.090842,-5.711913,-1.318574,-5.691442,2.029132,-3.278149,5.351238,-4.887600,-2.765093,-0.655215,8.057146,3.970689,5.438653,3.145775,-3.635452,-0.634533,0.089527,9.106442,8.886459,-7.668150,9.007077,-7.430562,2.997144,7.269118,-5.558546,5.114174,-0.427125,3.203846,-3.231889,0.094406,8.196669,6.711792,4.442970,3.461461,4.970795,4.826215,-4.865084,8.206449,-2.637298,-5.117387,0.263288,2.647479,-7.279875,3.703823,9.051352,7.362466,-8.542815,5.847816,-9.214962,8.708984,-9.755347,-8.324036,-1.810578,-1.717705,-4.427757,7.682834,-5.686245,5.227648,-2.918612,-8.584868,8.022718,-1.633438,-1.276838,1.159623,-2.294374,-7.939443,-5.920369,-6.989851,9.896264,7.065519,2.956646,9.877817,5.430053,-3.654200,5.708879,-4.189442,-3.582565,2.553710,-8.698112,7.347888,4.832892,-8.423574,-1.260932,-2.517314,8.379038,2.748053,-9.792004,5.706420,0.195234,6.703268,-4.715431,-2.795295,2.892408,9.417799,-3.960944,-3.861650,4.405677,8.373837,0.339233], dtype = "float32")#candidate|7183|(130,)|const|float32
const_7184 = relay.const([5,-10,3,6,-9,-1,-6,-2,-4,-7,-1,-2,-5,-10,-4,3,-6,-8,3,9,5,-8,1,-5,9,1,4,8,2,4,-2,7,1,1,9,7,-9,8,7,6,3,7,3,-1,-5,10,1,9,5,6,-9,-10,10,-2,-1,-4,-8,-6,-10,5,-9,3,4,-3,-2,-3,-6,1,2,2,10,2,8,-8,-2,-4,-9,4], dtype = "int16")#candidate|7184|(78,)|const|int16
var_7185 = relay.var("var_7185", dtype = "float32", shape = (728,))#candidate|7185|(728,)|var|float32
call_7182 = relay.TupleGetItem(func_6503_call(relay.reshape(const_7183.astype('float32'), [130,]), relay.reshape(const_7184.astype('int16'), [78,]), relay.reshape(var_7185.astype('float32'), [1, 728]), ), 2)
call_7186 = relay.TupleGetItem(func_6507_call(relay.reshape(const_7183.astype('float32'), [130,]), relay.reshape(const_7184.astype('int16'), [78,]), relay.reshape(var_7185.astype('float32'), [1, 728]), ), 2)
func_5139_call = mod.get_global_var('func_5139')
func_5140_call = mutated_mod.get_global_var('func_5140')
call_7201 = relay.TupleGetItem(func_5139_call(), 0)
call_7202 = relay.TupleGetItem(func_5140_call(), 0)
output = relay.Tuple([call_7172,call_7182,const_7183,const_7184,var_7185,call_7201,])
output2 = relay.Tuple([call_7173,call_7186,const_7183,const_7184,var_7185,call_7202,])
func_7220 = relay.Function([var_7185,], output)
mod['func_7220'] = func_7220
mod = relay.transform.InferType()(mod)
var_7221 = relay.var("var_7221", dtype = "float32", shape = (728,))#candidate|7221|(728,)|var|float32
output = func_7220(var_7221)
func_7222 = relay.Function([var_7221], output)
mutated_mod['func_7222'] = func_7222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6547_call = mod.get_global_var('func_6547')
func_6549_call = mutated_mod.get_global_var('func_6549')
call_7224 = func_6547_call()
call_7225 = func_6547_call()
var_7231 = relay.var("var_7231", dtype = "bool", shape = (13, 12, 4))#candidate|7231|(13, 12, 4)|var|bool
bop_7232 = relay.greater_equal(call_7224.astype('bool'), relay.reshape(var_7231.astype('bool'), relay.shape_of(call_7224))) # shape=(13, 12, 4)
bop_7235 = relay.greater_equal(call_7225.astype('bool'), relay.reshape(var_7231.astype('bool'), relay.shape_of(call_7225))) # shape=(13, 12, 4)
func_5975_call = mod.get_global_var('func_5975')
func_5977_call = mutated_mod.get_global_var('func_5977')
call_7240 = func_5975_call()
call_7241 = func_5975_call()
output = relay.Tuple([bop_7232,call_7240,])
output2 = relay.Tuple([bop_7235,call_7241,])
func_7249 = relay.Function([var_7231,], output)
mod['func_7249'] = func_7249
mod = relay.transform.InferType()(mod)
mutated_mod['func_7249'] = func_7249
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7250 = relay.var("var_7250", dtype = "bool", shape = (13, 12, 4))#candidate|7250|(13, 12, 4)|var|bool
func_7249_call = mutated_mod.get_global_var('func_7249')
call_7251 = func_7249_call(var_7250)
output = call_7251
func_7252 = relay.Function([var_7250], output)
mutated_mod['func_7252'] = func_7252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2162_call = mod.get_global_var('func_2162')
func_2164_call = mutated_mod.get_global_var('func_2164')
call_7254 = relay.TupleGetItem(func_2162_call(), 0)
call_7255 = relay.TupleGetItem(func_2164_call(), 0)
func_6547_call = mod.get_global_var('func_6547')
func_6549_call = mutated_mod.get_global_var('func_6549')
call_7260 = func_6547_call()
call_7261 = func_6547_call()
output = relay.Tuple([call_7254,call_7260,])
output2 = relay.Tuple([call_7255,call_7261,])
func_7290 = relay.Function([], output)
mod['func_7290'] = func_7290
mod = relay.transform.InferType()(mod)
output = func_7290()
func_7291 = relay.Function([], output)
mutated_mod['func_7291'] = func_7291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4791_call = mod.get_global_var('func_4791')
func_4793_call = mutated_mod.get_global_var('func_4793')
call_7303 = func_4791_call()
call_7304 = func_4791_call()
output = relay.Tuple([call_7303,])
output2 = relay.Tuple([call_7304,])
func_7308 = relay.Function([], output)
mod['func_7308'] = func_7308
mod = relay.transform.InferType()(mod)
output = func_7308()
func_7309 = relay.Function([], output)
mutated_mod['func_7309'] = func_7309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2402_call = mod.get_global_var('func_2402')
func_2403_call = mutated_mod.get_global_var('func_2403')
call_7312 = func_2402_call()
call_7313 = func_2402_call()
func_2907_call = mod.get_global_var('func_2907')
func_2910_call = mutated_mod.get_global_var('func_2910')
var_7317 = relay.var("var_7317", dtype = "bool", shape = (32,))#candidate|7317|(32,)|var|bool
const_7318 = relay.const([False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,True,True,False,False,True], dtype = "bool")#candidate|7318|(288,)|const|bool
call_7316 = relay.TupleGetItem(func_2907_call(relay.reshape(var_7317.astype('bool'), [32,]), relay.reshape(const_7318.astype('bool'), [288,]), ), 7)
call_7319 = relay.TupleGetItem(func_2910_call(relay.reshape(var_7317.astype('bool'), [32,]), relay.reshape(const_7318.astype('bool'), [288,]), ), 7)
output = relay.Tuple([call_7312,call_7316,var_7317,const_7318,])
output2 = relay.Tuple([call_7313,call_7319,var_7317,const_7318,])
func_7341 = relay.Function([var_7317,], output)
mod['func_7341'] = func_7341
mod = relay.transform.InferType()(mod)
var_7342 = relay.var("var_7342", dtype = "bool", shape = (32,))#candidate|7342|(32,)|var|bool
output = func_7341(var_7342)
func_7343 = relay.Function([var_7342], output)
mutated_mod['func_7343'] = func_7343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4032_call = mod.get_global_var('func_4032')
func_4034_call = mutated_mod.get_global_var('func_4034')
call_7347 = relay.TupleGetItem(func_4032_call(), 0)
call_7348 = relay.TupleGetItem(func_4034_call(), 0)
const_7349 = relay.const([[8,-6,3,2,-3,3,-9,4,-6,5,-10,6,2,2,-7,-1,-4,-5,1,4,6,-5],[8,-6,6,8,-2,-3,8,-8,-2,1,-7,2,6,3,-5,4,-10,8,2,9,2,2],[1,-6,8,8,4,5,-8,-9,-7,-8,5,-10,-2,3,-2,2,5,-6,-5,-10,8,8],[-2,-1,-4,-5,-5,-8,-5,-8,5,2,-10,-5,-7,-6,10,1,3,-10,-10,-5,-1,1],[3,-5,-1,-10,-7,6,10,7,7,2,9,-6,9,4,-6,4,-4,10,5,-6,7,-6],[-5,-8,10,-2,-4,-10,2,10,10,-9,-2,2,1,10,4,-6,9,-1,6,10,4,10],[7,-5,-4,3,-3,7,-5,-3,-3,7,-3,-2,4,8,5,3,7,-1,10,1,1,9],[-5,6,-9,3,-3,-2,9,4,-9,-10,-5,-1,6,-10,10,-4,2,-4,-3,5,-1,3],[-1,8,4,-8,8,5,3,-1,-5,-9,-5,7,9,-5,3,4,7,-5,9,-1,5,1],[1,1,4,-2,3,8,3,4,-5,9,-2,4,-10,-10,-9,10,-2,-6,9,7,7,-5],[1,6,10,10,2,5,7,6,6,-7,-5,7,1,7,9,8,-1,-10,4,5,1,9],[-7,5,-8,-4,-7,8,-2,8,7,5,-2,9,2,5,3,-3,-8,-6,3,1,8,8],[6,-5,-3,1,5,3,-3,1,2,-8,2,-7,3,-5,-7,5,10,-6,-8,10,8,-1],[2,9,-5,4,-3,2,-7,9,1,-1,1,6,6,-5,1,-5,7,7,-3,9,10,-1],[10,4,3,-6,5,-6,-10,-5,-4,-4,-6,-2,1,-6,5,-1,9,-6,-3,7,-4,6],[1,-5,-4,7,-9,9,-2,-3,2,10,1,4,-10,-9,1,8,-9,-10,-1,2,-7,10],[-6,6,6,1,-6,9,-5,10,-8,-9,-9,-9,-7,-10,2,4,2,-7,-10,6,-3,-1],[7,-4,8,-1,4,9,9,-4,1,8,-1,-2,3,-8,2,3,-1,-4,10,-7,-3,4],[8,-4,9,2,9,3,-1,6,-8,-3,-6,7,-2,10,5,-1,3,1,9,4,-7,-10],[5,2,-5,-4,3,6,-8,-3,10,5,9,-7,-3,-8,5,-1,-4,-6,9,9,-3,-9],[1,5,6,-7,8,-7,5,1,3,-2,4,-5,10,-7,9,6,-10,3,3,-4,8,-1],[-7,4,-6,-7,6,5,6,-3,-2,6,1,9,-3,-4,4,-3,10,1,6,6,7,-2],[-5,-9,3,8,-7,6,10,9,5,-3,1,-1,-1,1,-8,3,5,2,-5,1,-7,-2],[-7,1,4,9,9,2,-6,-7,5,10,10,-9,-2,9,-9,6,-3,-10,-10,-2,-6,6]], dtype = "uint32")#candidate|7349|(24, 22)|const|uint32
bop_7350 = relay.not_equal(call_7347.astype('bool'), relay.reshape(const_7349.astype('bool'), relay.shape_of(call_7347))) # shape=(24, 22)
bop_7353 = relay.not_equal(call_7348.astype('bool'), relay.reshape(const_7349.astype('bool'), relay.shape_of(call_7348))) # shape=(24, 22)
bop_7359 = relay.minimum(call_7347.astype('int8'), relay.reshape(const_7349.astype('int8'), relay.shape_of(call_7347))) # shape=(24, 22)
bop_7362 = relay.minimum(call_7348.astype('int8'), relay.reshape(const_7349.astype('int8'), relay.shape_of(call_7348))) # shape=(24, 22)
func_6419_call = mod.get_global_var('func_6419')
func_6422_call = mutated_mod.get_global_var('func_6422')
var_7367 = relay.var("var_7367", dtype = "float64", shape = (210,))#candidate|7367|(210,)|var|float64
call_7366 = relay.TupleGetItem(func_6419_call(relay.reshape(var_7367.astype('float64'), [210,])), 2)
call_7368 = relay.TupleGetItem(func_6422_call(relay.reshape(var_7367.astype('float64'), [210,])), 2)
output = relay.Tuple([bop_7350,bop_7359,call_7366,var_7367,])
output2 = relay.Tuple([bop_7353,bop_7362,call_7368,var_7367,])
func_7370 = relay.Function([var_7367,], output)
mod['func_7370'] = func_7370
mod = relay.transform.InferType()(mod)
mutated_mod['func_7370'] = func_7370
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7371 = relay.var("var_7371", dtype = "float64", shape = (210,))#candidate|7371|(210,)|var|float64
func_7370_call = mutated_mod.get_global_var('func_7370')
call_7372 = func_7370_call(var_7371)
output = call_7372
func_7373 = relay.Function([var_7371], output)
mutated_mod['func_7373'] = func_7373
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7392 = relay.var("var_7392", dtype = "int64", shape = ())#candidate|7392|()|var|int64
var_7393 = relay.var("var_7393", dtype = "int64", shape = (14, 5, 15))#candidate|7393|(14, 5, 15)|var|int64
bop_7394 = relay.logical_xor(var_7392.astype('int64'), var_7393.astype('int64')) # shape=(14, 5, 15)
output = bop_7394
output2 = bop_7394
F = relay.Function([var_7392,var_7393,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7392,var_7393,], output2)
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
	relay.transform.InferType(),
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
