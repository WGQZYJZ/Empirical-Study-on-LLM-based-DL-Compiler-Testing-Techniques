import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_184 = relay.var("var_184", dtype = "int64", shape = (8, 5, 9))#candidate|184|(8, 5, 9)|var|int64
var_185 = relay.var("var_185", dtype = "int64", shape = (8, 5, 9))#candidate|185|(8, 5, 9)|var|int64
bop_186 = relay.subtract(var_184.astype('int64'), relay.reshape(var_185.astype('int64'), relay.shape_of(var_184))) # shape=(8, 5, 9)
output = bop_186
output2 = bop_186
func_190 = relay.Function([var_184,var_185,], output)
mod['func_190'] = func_190
mod = relay.transform.InferType()(mod)
var_191 = relay.var("var_191", dtype = "int64", shape = (8, 5, 9))#candidate|191|(8, 5, 9)|var|int64
var_192 = relay.var("var_192", dtype = "int64", shape = (8, 5, 9))#candidate|192|(8, 5, 9)|var|int64
output = func_190(var_191,var_192,)
func_193 = relay.Function([var_191,var_192,], output)
mutated_mod['func_193'] = func_193
mutated_mod = relay.transform.InferType()(mutated_mod)
var_416 = relay.var("var_416", dtype = "bool", shape = (15, 9, 6))#candidate|416|(15, 9, 6)|var|bool
var_417 = relay.var("var_417", dtype = "bool", shape = (15, 9, 6))#candidate|417|(15, 9, 6)|var|bool
bop_418 = relay.logical_and(var_416.astype('bool'), relay.reshape(var_417.astype('bool'), relay.shape_of(var_416))) # shape=(15, 9, 6)
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
var_429 = relay.var("var_429", dtype = "int64", shape = (360,))#candidate|429|(360,)|var|int64
call_428 = func_190_call(relay.reshape(var_429.astype('int64'), [8, 5, 9]), relay.reshape(var_429.astype('int64'), [8, 5, 9]), )
call_430 = func_190_call(relay.reshape(var_429.astype('int64'), [8, 5, 9]), relay.reshape(var_429.astype('int64'), [8, 5, 9]), )
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
call_445 = func_190_call(relay.reshape(call_428.astype('int64'), [8, 5, 9]), relay.reshape(call_428.astype('int64'), [8, 5, 9]), )
call_446 = func_190_call(relay.reshape(call_428.astype('int64'), [8, 5, 9]), relay.reshape(call_428.astype('int64'), [8, 5, 9]), )
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
call_447 = func_190_call(relay.reshape(call_445.astype('int64'), [8, 5, 9]), relay.reshape(var_429.astype('int64'), [8, 5, 9]), )
call_448 = func_190_call(relay.reshape(call_445.astype('int64'), [8, 5, 9]), relay.reshape(var_429.astype('int64'), [8, 5, 9]), )
uop_451 = relay.tan(var_417.astype('float32')) # shape=(15, 9, 6)
bop_454 = relay.bitwise_or(uop_451.astype('int16'), relay.reshape(bop_418.astype('int16'), relay.shape_of(uop_451))) # shape=(15, 9, 6)
bop_458 = relay.add(bop_454.astype('uint16'), relay.reshape(uop_451.astype('uint16'), relay.shape_of(bop_454))) # shape=(15, 9, 6)
uop_465 = relay.log(bop_454.astype('float64')) # shape=(15, 9, 6)
output = relay.Tuple([call_428,var_429,call_445,call_447,bop_458,uop_465,])
output2 = relay.Tuple([call_430,var_429,call_446,call_448,bop_458,uop_465,])
func_469 = relay.Function([var_416,var_417,var_429,], output)
mod['func_469'] = func_469
mod = relay.transform.InferType()(mod)
var_470 = relay.var("var_470", dtype = "bool", shape = (15, 9, 6))#candidate|470|(15, 9, 6)|var|bool
var_471 = relay.var("var_471", dtype = "bool", shape = (15, 9, 6))#candidate|471|(15, 9, 6)|var|bool
var_472 = relay.var("var_472", dtype = "int64", shape = (360,))#candidate|472|(360,)|var|int64
output = func_469(var_470,var_471,var_472,)
func_473 = relay.Function([var_470,var_471,var_472,], output)
mutated_mod['func_473'] = func_473
mutated_mod = relay.transform.InferType()(mutated_mod)
var_557 = relay.var("var_557", dtype = "float32", shape = (11, 7, 1))#candidate|557|(11, 7, 1)|var|float32
var_558 = relay.var("var_558", dtype = "float32", shape = (11, 7, 2))#candidate|558|(11, 7, 2)|var|float32
bop_559 = relay.mod(var_557.astype('float32'), var_558.astype('float32')) # shape=(11, 7, 2)
output = bop_559
output2 = bop_559
func_562 = relay.Function([var_557,var_558,], output)
mod['func_562'] = func_562
mod = relay.transform.InferType()(mod)
var_563 = relay.var("var_563", dtype = "float32", shape = (11, 7, 1))#candidate|563|(11, 7, 1)|var|float32
var_564 = relay.var("var_564", dtype = "float32", shape = (11, 7, 2))#candidate|564|(11, 7, 2)|var|float32
output = func_562(var_563,var_564,)
func_565 = relay.Function([var_563,var_564,], output)
mutated_mod['func_565'] = func_565
mutated_mod = relay.transform.InferType()(mutated_mod)
const_584 = relay.const(5, dtype = "int64")#candidate|584|()|const|int64
const_585 = relay.const([[7,-1,-7,-3,3,4,-1,-8,7,-8]], dtype = "int64")#candidate|585|(1, 10)|const|int64
bop_586 = relay.less(const_584.astype('bool'), const_585.astype('bool')) # shape=(1, 10)
output = relay.Tuple([bop_586,])
output2 = relay.Tuple([bop_586,])
func_589 = relay.Function([], output)
mod['func_589'] = func_589
mod = relay.transform.InferType()(mod)
output = func_589()
func_590 = relay.Function([], output)
mutated_mod['func_590'] = func_590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_618 = relay.TupleGetItem(func_589_call(), 0)
call_619 = relay.TupleGetItem(func_590_call(), 0)
output = call_618
output2 = call_619
func_650 = relay.Function([], output)
mod['func_650'] = func_650
mod = relay.transform.InferType()(mod)
output = func_650()
func_651 = relay.Function([], output)
mutated_mod['func_651'] = func_651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_675 = func_650_call()
call_676 = func_650_call()
output = relay.Tuple([call_675,])
output2 = relay.Tuple([call_676,])
func_677 = relay.Function([], output)
mod['func_677'] = func_677
mod = relay.transform.InferType()(mod)
mutated_mod['func_677'] = func_677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_677_call = mutated_mod.get_global_var('func_677')
call_678 = func_677_call()
output = call_678
func_679 = relay.Function([], output)
mutated_mod['func_679'] = func_679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_734 = relay.TupleGetItem(func_589_call(), 0)
call_735 = relay.TupleGetItem(func_590_call(), 0)
output = call_734
output2 = call_735
func_741 = relay.Function([], output)
mod['func_741'] = func_741
mod = relay.transform.InferType()(mod)
output = func_741()
func_742 = relay.Function([], output)
mutated_mod['func_742'] = func_742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_818 = relay.TupleGetItem(func_589_call(), 0)
call_819 = relay.TupleGetItem(func_590_call(), 0)
output = call_818
output2 = call_819
func_820 = relay.Function([], output)
mod['func_820'] = func_820
mod = relay.transform.InferType()(mod)
mutated_mod['func_820'] = func_820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mutated_mod.get_global_var('func_820')
call_821 = func_820_call()
output = call_821
func_822 = relay.Function([], output)
mutated_mod['func_822'] = func_822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_865 = relay.var("var_865", dtype = "float64", shape = (2, 13, 9))#candidate|865|(2, 13, 9)|var|float64
uop_866 = relay.acos(var_865.astype('float64')) # shape=(2, 13, 9)
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_868 = relay.TupleGetItem(func_677_call(), 0)
call_869 = relay.TupleGetItem(func_679_call(), 0)
var_872 = relay.var("var_872", dtype = "float64", shape = (2, 13, 9))#candidate|872|(2, 13, 9)|var|float64
bop_873 = relay.floor_mod(uop_866.astype('float32'), relay.reshape(var_872.astype('float32'), relay.shape_of(uop_866))) # shape=(2, 13, 9)
output = relay.Tuple([call_868,bop_873,])
output2 = relay.Tuple([call_869,bop_873,])
func_880 = relay.Function([var_865,var_872,], output)
mod['func_880'] = func_880
mod = relay.transform.InferType()(mod)
var_881 = relay.var("var_881", dtype = "float64", shape = (2, 13, 9))#candidate|881|(2, 13, 9)|var|float64
var_882 = relay.var("var_882", dtype = "float64", shape = (2, 13, 9))#candidate|882|(2, 13, 9)|var|float64
output = func_880(var_881,var_882,)
func_883 = relay.Function([var_881,var_882,], output)
mutated_mod['func_883'] = func_883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_899 = func_741_call()
call_900 = func_741_call()
output = relay.Tuple([call_899,])
output2 = relay.Tuple([call_900,])
func_902 = relay.Function([], output)
mod['func_902'] = func_902
mod = relay.transform.InferType()(mod)
mutated_mod['func_902'] = func_902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_902_call = mutated_mod.get_global_var('func_902')
call_903 = func_902_call()
output = call_903
func_904 = relay.Function([], output)
mutated_mod['func_904'] = func_904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_902_call = mod.get_global_var('func_902')
func_904_call = mutated_mod.get_global_var('func_904')
call_927 = relay.TupleGetItem(func_902_call(), 0)
call_928 = relay.TupleGetItem(func_904_call(), 0)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_932 = relay.TupleGetItem(func_589_call(), 0)
call_933 = relay.TupleGetItem(func_590_call(), 0)
output = relay.Tuple([call_927,call_932,])
output2 = relay.Tuple([call_928,call_933,])
func_938 = relay.Function([], output)
mod['func_938'] = func_938
mod = relay.transform.InferType()(mod)
output = func_938()
func_939 = relay.Function([], output)
mutated_mod['func_939'] = func_939
mutated_mod = relay.transform.InferType()(mutated_mod)
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_967 = func_741_call()
call_968 = func_741_call()
output = relay.Tuple([call_967,])
output2 = relay.Tuple([call_968,])
func_979 = relay.Function([], output)
mod['func_979'] = func_979
mod = relay.transform.InferType()(mod)
mutated_mod['func_979'] = func_979
mutated_mod = relay.transform.InferType()(mutated_mod)
func_979_call = mutated_mod.get_global_var('func_979')
call_980 = func_979_call()
output = call_980
func_981 = relay.Function([], output)
mutated_mod['func_981'] = func_981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_990 = func_650_call()
call_991 = func_650_call()
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_994 = func_650_call()
call_995 = func_650_call()
output = relay.Tuple([call_990,call_994,])
output2 = relay.Tuple([call_991,call_995,])
func_997 = relay.Function([], output)
mod['func_997'] = func_997
mod = relay.transform.InferType()(mod)
mutated_mod['func_997'] = func_997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_997_call = mutated_mod.get_global_var('func_997')
call_998 = func_997_call()
output = call_998
func_999 = relay.Function([], output)
mutated_mod['func_999'] = func_999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_1011 = func_820_call()
call_1012 = func_820_call()
output = call_1011
output2 = call_1012
func_1013 = relay.Function([], output)
mod['func_1013'] = func_1013
mod = relay.transform.InferType()(mod)
mutated_mod['func_1013'] = func_1013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mutated_mod.get_global_var('func_1013')
call_1014 = func_1013_call()
output = call_1014
func_1015 = relay.Function([], output)
mutated_mod['func_1015'] = func_1015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_997_call = mod.get_global_var('func_997')
func_999_call = mutated_mod.get_global_var('func_999')
call_1056 = relay.TupleGetItem(func_997_call(), 0)
call_1057 = relay.TupleGetItem(func_999_call(), 0)
func_562_call = mod.get_global_var('func_562')
func_565_call = mutated_mod.get_global_var('func_565')
var_1059 = relay.var("var_1059", dtype = "float32", shape = (77,))#candidate|1059|(77,)|var|float32
var_1060 = relay.var("var_1060", dtype = "float32", shape = (154,))#candidate|1060|(154,)|var|float32
call_1058 = func_562_call(relay.reshape(var_1059.astype('float32'), [11, 7, 1]), relay.reshape(var_1060.astype('float32'), [11, 7, 2]), )
call_1061 = func_562_call(relay.reshape(var_1059.astype('float32'), [11, 7, 1]), relay.reshape(var_1060.astype('float32'), [11, 7, 2]), )
output = relay.Tuple([call_1056,call_1058,var_1059,var_1060,])
output2 = relay.Tuple([call_1057,call_1061,var_1059,var_1060,])
func_1064 = relay.Function([var_1059,var_1060,], output)
mod['func_1064'] = func_1064
mod = relay.transform.InferType()(mod)
var_1065 = relay.var("var_1065", dtype = "float32", shape = (77,))#candidate|1065|(77,)|var|float32
var_1066 = relay.var("var_1066", dtype = "float32", shape = (154,))#candidate|1066|(154,)|var|float32
output = func_1064(var_1065,var_1066,)
func_1067 = relay.Function([var_1065,var_1066,], output)
mutated_mod['func_1067'] = func_1067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_979_call = mod.get_global_var('func_979')
func_981_call = mutated_mod.get_global_var('func_981')
call_1113 = relay.TupleGetItem(func_979_call(), 0)
call_1114 = relay.TupleGetItem(func_981_call(), 0)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
var_1132 = relay.var("var_1132", dtype = "float64", shape = (234,))#candidate|1132|(234,)|var|float64
call_1131 = relay.TupleGetItem(func_880_call(relay.reshape(var_1132.astype('float64'), [2, 13, 9]), relay.reshape(var_1132.astype('float64'), [2, 13, 9]), ), 1)
call_1133 = relay.TupleGetItem(func_883_call(relay.reshape(var_1132.astype('float64'), [2, 13, 9]), relay.reshape(var_1132.astype('float64'), [2, 13, 9]), ), 1)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
call_1137 = relay.TupleGetItem(func_880_call(relay.reshape(var_1132.astype('float64'), [2, 13, 9]), relay.reshape(call_1131.astype('float64'), [2, 13, 9]), ), 0)
call_1138 = relay.TupleGetItem(func_883_call(relay.reshape(var_1132.astype('float64'), [2, 13, 9]), relay.reshape(call_1131.astype('float64'), [2, 13, 9]), ), 0)
output = relay.Tuple([call_1113,call_1131,var_1132,call_1137,])
output2 = relay.Tuple([call_1114,call_1133,var_1132,call_1138,])
func_1154 = relay.Function([var_1132,], output)
mod['func_1154'] = func_1154
mod = relay.transform.InferType()(mod)
var_1155 = relay.var("var_1155", dtype = "float64", shape = (234,))#candidate|1155|(234,)|var|float64
output = func_1154(var_1155)
func_1156 = relay.Function([var_1155], output)
mutated_mod['func_1156'] = func_1156
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1171 = relay.var("var_1171", dtype = "int16", shape = (9, 3, 10))#candidate|1171|(9, 3, 10)|var|int16
var_1172 = relay.var("var_1172", dtype = "int16", shape = (9, 3, 10))#candidate|1172|(9, 3, 10)|var|int16
bop_1173 = relay.minimum(var_1171.astype('int16'), relay.reshape(var_1172.astype('int16'), relay.shape_of(var_1171))) # shape=(9, 3, 10)
uop_1184 = relay.asinh(var_1172.astype('float64')) # shape=(9, 3, 10)
output = relay.Tuple([bop_1173,uop_1184,])
output2 = relay.Tuple([bop_1173,uop_1184,])
func_1189 = relay.Function([var_1171,var_1172,], output)
mod['func_1189'] = func_1189
mod = relay.transform.InferType()(mod)
mutated_mod['func_1189'] = func_1189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1189_call = mutated_mod.get_global_var('func_1189')
var_1191 = relay.var("var_1191", dtype = "int16", shape = (9, 3, 10))#candidate|1191|(9, 3, 10)|var|int16
var_1192 = relay.var("var_1192", dtype = "int16", shape = (9, 3, 10))#candidate|1192|(9, 3, 10)|var|int16
call_1190 = func_1189_call(var_1191,var_1192,)
output = call_1190
func_1193 = relay.Function([var_1191,var_1192,], output)
mutated_mod['func_1193'] = func_1193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_979_call = mod.get_global_var('func_979')
func_981_call = mutated_mod.get_global_var('func_981')
call_1328 = relay.TupleGetItem(func_979_call(), 0)
call_1329 = relay.TupleGetItem(func_981_call(), 0)
output = relay.Tuple([call_1328,])
output2 = relay.Tuple([call_1329,])
func_1334 = relay.Function([], output)
mod['func_1334'] = func_1334
mod = relay.transform.InferType()(mod)
mutated_mod['func_1334'] = func_1334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mutated_mod.get_global_var('func_1334')
call_1335 = func_1334_call()
output = call_1335
func_1336 = relay.Function([], output)
mutated_mod['func_1336'] = func_1336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_1369 = func_650_call()
call_1370 = func_650_call()
func_1154_call = mod.get_global_var('func_1154')
func_1156_call = mutated_mod.get_global_var('func_1156')
var_1399 = relay.var("var_1399", dtype = "float64", shape = (234,))#candidate|1399|(234,)|var|float64
call_1398 = relay.TupleGetItem(func_1154_call(relay.reshape(var_1399.astype('float64'), [234,])), 3)
call_1400 = relay.TupleGetItem(func_1156_call(relay.reshape(var_1399.astype('float64'), [234,])), 3)
bop_1407 = relay.multiply(call_1398.astype('uint8'), relay.reshape(call_1369.astype('uint8'), relay.shape_of(call_1398))) # shape=(1, 10)
bop_1410 = relay.multiply(call_1400.astype('uint8'), relay.reshape(call_1370.astype('uint8'), relay.shape_of(call_1400))) # shape=(1, 10)
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_1411 = relay.TupleGetItem(func_677_call(), 0)
call_1412 = relay.TupleGetItem(func_679_call(), 0)
output = relay.Tuple([var_1399,bop_1407,call_1411,])
output2 = relay.Tuple([var_1399,bop_1410,call_1412,])
func_1417 = relay.Function([var_1399,], output)
mod['func_1417'] = func_1417
mod = relay.transform.InferType()(mod)
mutated_mod['func_1417'] = func_1417
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1418 = relay.var("var_1418", dtype = "float64", shape = (234,))#candidate|1418|(234,)|var|float64
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1419 = func_1417_call(var_1418)
output = call_1419
func_1420 = relay.Function([var_1418], output)
mutated_mod['func_1420'] = func_1420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_1476 = relay.TupleGetItem(func_1334_call(), 0)
call_1477 = relay.TupleGetItem(func_1336_call(), 0)
func_979_call = mod.get_global_var('func_979')
func_981_call = mutated_mod.get_global_var('func_981')
call_1480 = relay.TupleGetItem(func_979_call(), 0)
call_1481 = relay.TupleGetItem(func_981_call(), 0)
output = relay.Tuple([call_1476,call_1480,])
output2 = relay.Tuple([call_1477,call_1481,])
func_1488 = relay.Function([], output)
mod['func_1488'] = func_1488
mod = relay.transform.InferType()(mod)
output = func_1488()
func_1489 = relay.Function([], output)
mutated_mod['func_1489'] = func_1489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_1504 = relay.TupleGetItem(func_1334_call(), 0)
call_1505 = relay.TupleGetItem(func_1336_call(), 0)
output = call_1504
output2 = call_1505
func_1512 = relay.Function([], output)
mod['func_1512'] = func_1512
mod = relay.transform.InferType()(mod)
mutated_mod['func_1512'] = func_1512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1512_call = mutated_mod.get_global_var('func_1512')
call_1513 = func_1512_call()
output = call_1513
func_1514 = relay.Function([], output)
mutated_mod['func_1514'] = func_1514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_1538 = relay.TupleGetItem(func_1334_call(), 0)
call_1539 = relay.TupleGetItem(func_1336_call(), 0)
func_1417_call = mod.get_global_var('func_1417')
func_1420_call = mutated_mod.get_global_var('func_1420')
var_1546 = relay.var("var_1546", dtype = "float64", shape = (234,))#candidate|1546|(234,)|var|float64
call_1545 = relay.TupleGetItem(func_1417_call(relay.reshape(var_1546.astype('float64'), [234,])), 0)
call_1547 = relay.TupleGetItem(func_1420_call(relay.reshape(var_1546.astype('float64'), [234,])), 0)
output = relay.Tuple([call_1538,call_1545,var_1546,])
output2 = relay.Tuple([call_1539,call_1547,var_1546,])
func_1552 = relay.Function([var_1546,], output)
mod['func_1552'] = func_1552
mod = relay.transform.InferType()(mod)
mutated_mod['func_1552'] = func_1552
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1553 = relay.var("var_1553", dtype = "float64", shape = (234,))#candidate|1553|(234,)|var|float64
func_1552_call = mutated_mod.get_global_var('func_1552')
call_1554 = func_1552_call(var_1553)
output = call_1554
func_1555 = relay.Function([var_1553], output)
mutated_mod['func_1555'] = func_1555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_997_call = mod.get_global_var('func_997')
func_999_call = mutated_mod.get_global_var('func_999')
call_1557 = relay.TupleGetItem(func_997_call(), 0)
call_1558 = relay.TupleGetItem(func_999_call(), 0)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_1566 = relay.TupleGetItem(func_589_call(), 0)
call_1567 = relay.TupleGetItem(func_590_call(), 0)
func_1013_call = mod.get_global_var('func_1013')
func_1015_call = mutated_mod.get_global_var('func_1015')
call_1569 = func_1013_call()
call_1570 = func_1013_call()
output = relay.Tuple([call_1557,call_1566,call_1569,])
output2 = relay.Tuple([call_1558,call_1567,call_1570,])
func_1571 = relay.Function([], output)
mod['func_1571'] = func_1571
mod = relay.transform.InferType()(mod)
mutated_mod['func_1571'] = func_1571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1571_call = mutated_mod.get_global_var('func_1571')
call_1572 = func_1571_call()
output = call_1572
func_1573 = relay.Function([], output)
mutated_mod['func_1573'] = func_1573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_1601 = func_650_call()
call_1602 = func_650_call()
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_1612 = relay.TupleGetItem(func_677_call(), 0)
call_1613 = relay.TupleGetItem(func_679_call(), 0)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
var_1618 = relay.var("var_1618", dtype = "float64", shape = (3, 78))#candidate|1618|(3, 78)|var|float64
call_1617 = relay.TupleGetItem(func_880_call(relay.reshape(var_1618.astype('float64'), [2, 13, 9]), relay.reshape(var_1618.astype('float64'), [2, 13, 9]), ), 1)
call_1619 = relay.TupleGetItem(func_883_call(relay.reshape(var_1618.astype('float64'), [2, 13, 9]), relay.reshape(var_1618.astype('float64'), [2, 13, 9]), ), 1)
bop_1621 = relay.logical_and(var_1618.astype('bool'), relay.reshape(call_1617.astype('bool'), relay.shape_of(var_1618))) # shape=(3, 78)
bop_1624 = relay.logical_and(var_1618.astype('bool'), relay.reshape(call_1619.astype('bool'), relay.shape_of(var_1618))) # shape=(3, 78)
output = relay.Tuple([call_1601,call_1612,bop_1621,])
output2 = relay.Tuple([call_1602,call_1613,bop_1624,])
func_1628 = relay.Function([var_1618,], output)
mod['func_1628'] = func_1628
mod = relay.transform.InferType()(mod)
mutated_mod['func_1628'] = func_1628
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1629 = relay.var("var_1629", dtype = "float64", shape = (3, 78))#candidate|1629|(3, 78)|var|float64
func_1628_call = mutated_mod.get_global_var('func_1628')
call_1630 = func_1628_call(var_1629)
output = call_1630
func_1631 = relay.Function([var_1629], output)
mutated_mod['func_1631'] = func_1631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_1650 = func_820_call()
call_1651 = func_820_call()
func_997_call = mod.get_global_var('func_997')
func_999_call = mutated_mod.get_global_var('func_999')
call_1662 = relay.TupleGetItem(func_997_call(), 0)
call_1663 = relay.TupleGetItem(func_999_call(), 0)
func_1417_call = mod.get_global_var('func_1417')
func_1420_call = mutated_mod.get_global_var('func_1420')
const_1676 = relay.const([[-5.728555],[5.255622],[4.781226],[-0.551262],[5.102467],[3.853725],[9.007662],[2.382614],[-2.614735],[-8.608298],[7.938565],[4.123781],[9.695047],[-4.466637],[-9.046581],[7.336698],[9.818497],[-1.636573],[-1.751686],[-4.346631],[4.623038],[7.227866],[9.222102],[2.601418],[3.649434],[4.471211],[3.693987],[-0.006503],[9.198298],[1.363717],[-7.467029],[9.166139],[1.359001],[-1.416329],[-6.527388],[2.642338],[-6.361431],[-6.548630],[3.408274],[-8.587467],[8.233442],[5.930366],[-7.275813],[-2.264239],[-0.862038],[0.866617],[-6.054837],[-9.543130],[-9.005698],[1.224681],[8.078207],[6.033343],[-1.977715],[-9.208665],[6.965220],[-6.551711],[-8.895553],[6.126081],[7.907201],[-8.861871],[4.478845],[4.503014],[-2.003677],[-6.225002],[-6.380609],[4.360951],[-7.424331],[-2.136473],[-0.799084],[4.620420],[2.866119],[6.421695],[5.228888],[-1.478013],[-0.187819],[9.911184],[-6.772211],[2.423237],[-0.561008],[8.283570],[1.288125],[7.011712],[8.804413],[-5.563522],[-3.996977],[8.899432],[6.941059],[5.439615],[-7.583564],[-2.353293],[-5.331880],[-0.756262],[-0.186577],[-4.469170],[5.245623],[4.893087],[-7.400033],[8.079246],[-5.391862],[-4.703285],[7.661596],[-3.497558],[-3.625786],[6.755380],[5.573827],[0.110954],[9.970040],[-2.964164],[9.772186],[2.382521],[4.091646],[4.118875],[1.729388],[2.970664],[4.767328],[-9.826628],[-1.178833],[1.827444],[-4.965393],[2.445661],[-6.299428],[6.679943],[-1.066469],[7.584532],[-4.333858],[3.738436],[-9.122664],[-1.375615],[3.933327],[2.294939],[3.051102],[8.944437],[6.925764],[-4.867228],[4.228633],[9.032760],[-8.807253],[-6.302080],[2.057865],[-3.091718],[-1.737613],[5.709088],[-3.458263],[-4.204141],[6.733116],[-5.826698],[9.206651],[-6.245193],[5.691139],[-8.751514],[-1.496823],[-9.393377],[-7.107791],[-5.547239],[1.956171],[-4.250719],[-2.748053],[-0.701695],[4.255633],[-7.660807],[-4.924625],[0.023277],[-2.750582],[-7.685230],[-5.391470],[-3.811788],[7.063086],[8.735318],[8.061353],[7.686378],[-9.350275],[-0.330418],[1.136839],[1.714506],[6.081251],[1.085440],[8.726340],[9.021230],[7.161836],[8.211661],[-4.067070],[-4.961824],[-0.011425],[-3.339296],[2.748308],[-1.929538],[5.063620],[-1.537227],[4.386053],[9.292108],[0.468044],[5.103200],[9.540617],[-9.607962],[-7.169350],[-9.482760],[-9.670937],[-4.927222],[-0.367619],[-9.830396],[-7.724421],[8.687841],[-3.330041],[-2.566323],[1.862450],[-9.289503],[3.997567],[4.460313],[2.633341],[3.742483],[5.336225],[-9.739794],[-4.410367],[6.170611],[1.992995],[4.257401],[-5.776857],[7.067030],[-8.939748],[8.323086],[0.236703],[4.987093],[6.119457],[1.630109],[-4.452466],[-3.435150],[-8.703881],[1.380054],[-2.422201],[6.138974],[9.551454],[2.077956],[5.040233],[-4.991370]], dtype = "float64")#candidate|1676|(234, 1)|const|float64
call_1675 = relay.TupleGetItem(func_1417_call(relay.reshape(const_1676.astype('float64'), [234,])), 2)
call_1677 = relay.TupleGetItem(func_1420_call(relay.reshape(const_1676.astype('float64'), [234,])), 2)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1680 = relay.TupleGetItem(func_1488_call(), 1)
call_1681 = relay.TupleGetItem(func_1489_call(), 1)
func_979_call = mod.get_global_var('func_979')
func_981_call = mutated_mod.get_global_var('func_981')
call_1689 = relay.TupleGetItem(func_979_call(), 0)
call_1690 = relay.TupleGetItem(func_981_call(), 0)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1699 = relay.TupleGetItem(func_1488_call(), 1)
call_1700 = relay.TupleGetItem(func_1489_call(), 1)
func_1628_call = mod.get_global_var('func_1628')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_1701 = relay.TupleGetItem(func_1628_call(relay.reshape(const_1676.astype('float64'), [3, 78])), 2)
call_1702 = relay.TupleGetItem(func_1631_call(relay.reshape(const_1676.astype('float64'), [3, 78])), 2)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_1709 = relay.TupleGetItem(func_589_call(), 0)
call_1710 = relay.TupleGetItem(func_590_call(), 0)
output = relay.Tuple([call_1650,call_1662,call_1675,const_1676,call_1680,call_1689,call_1699,call_1701,call_1709,])
output2 = relay.Tuple([call_1651,call_1663,call_1677,const_1676,call_1681,call_1690,call_1700,call_1702,call_1710,])
func_1713 = relay.Function([], output)
mod['func_1713'] = func_1713
mod = relay.transform.InferType()(mod)
mutated_mod['func_1713'] = func_1713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1713_call = mutated_mod.get_global_var('func_1713')
call_1714 = func_1713_call()
output = call_1714
func_1715 = relay.Function([], output)
mutated_mod['func_1715'] = func_1715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_902_call = mod.get_global_var('func_902')
func_904_call = mutated_mod.get_global_var('func_904')
call_1724 = relay.TupleGetItem(func_902_call(), 0)
call_1725 = relay.TupleGetItem(func_904_call(), 0)
output = relay.Tuple([call_1724,])
output2 = relay.Tuple([call_1725,])
func_1736 = relay.Function([], output)
mod['func_1736'] = func_1736
mod = relay.transform.InferType()(mod)
mutated_mod['func_1736'] = func_1736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mutated_mod.get_global_var('func_1736')
call_1737 = func_1736_call()
output = call_1737
func_1738 = relay.Function([], output)
mutated_mod['func_1738'] = func_1738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mod.get_global_var('func_1013')
func_1015_call = mutated_mod.get_global_var('func_1015')
call_1739 = func_1013_call()
call_1740 = func_1013_call()
func_1064_call = mod.get_global_var('func_1064')
func_1067_call = mutated_mod.get_global_var('func_1067')
var_1742 = relay.var("var_1742", dtype = "float32", shape = (77,))#candidate|1742|(77,)|var|float32
var_1743 = relay.var("var_1743", dtype = "float32", shape = (154,))#candidate|1743|(154,)|var|float32
call_1741 = relay.TupleGetItem(func_1064_call(relay.reshape(var_1742.astype('float32'), [77,]), relay.reshape(var_1743.astype('float32'), [154,]), ), 0)
call_1744 = relay.TupleGetItem(func_1067_call(relay.reshape(var_1742.astype('float32'), [77,]), relay.reshape(var_1743.astype('float32'), [154,]), ), 0)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_1745 = relay.TupleGetItem(func_589_call(), 0)
call_1746 = relay.TupleGetItem(func_590_call(), 0)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
var_1748 = relay.var("var_1748", dtype = "float64", shape = (234,))#candidate|1748|(234,)|var|float64
call_1747 = relay.TupleGetItem(func_880_call(relay.reshape(var_1748.astype('float64'), [2, 13, 9]), relay.reshape(var_1748.astype('float64'), [2, 13, 9]), ), 1)
call_1749 = relay.TupleGetItem(func_883_call(relay.reshape(var_1748.astype('float64'), [2, 13, 9]), relay.reshape(var_1748.astype('float64'), [2, 13, 9]), ), 1)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
call_1750 = relay.TupleGetItem(func_880_call(relay.reshape(call_1747.astype('float64'), [2, 13, 9]), relay.reshape(var_1748.astype('float64'), [2, 13, 9]), ), 0)
call_1751 = relay.TupleGetItem(func_883_call(relay.reshape(call_1747.astype('float64'), [2, 13, 9]), relay.reshape(var_1748.astype('float64'), [2, 13, 9]), ), 0)
bop_1756 = relay.power(call_1747.astype('float32'), relay.reshape(var_1748.astype('float32'), relay.shape_of(call_1747))) # shape=(2, 13, 9)
bop_1759 = relay.power(call_1749.astype('float32'), relay.reshape(var_1748.astype('float32'), relay.shape_of(call_1749))) # shape=(2, 13, 9)
output = relay.Tuple([call_1739,call_1741,var_1742,var_1743,call_1745,call_1750,bop_1756,])
output2 = relay.Tuple([call_1740,call_1744,var_1742,var_1743,call_1746,call_1751,bop_1759,])
func_1773 = relay.Function([var_1742,var_1743,var_1748,], output)
mod['func_1773'] = func_1773
mod = relay.transform.InferType()(mod)
var_1774 = relay.var("var_1774", dtype = "float32", shape = (77,))#candidate|1774|(77,)|var|float32
var_1775 = relay.var("var_1775", dtype = "float32", shape = (154,))#candidate|1775|(154,)|var|float32
var_1776 = relay.var("var_1776", dtype = "float64", shape = (234,))#candidate|1776|(234,)|var|float64
output = func_1773(var_1774,var_1775,var_1776,)
func_1777 = relay.Function([var_1774,var_1775,var_1776,], output)
mutated_mod['func_1777'] = func_1777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_938_call = mod.get_global_var('func_938')
func_939_call = mutated_mod.get_global_var('func_939')
call_1779 = relay.TupleGetItem(func_938_call(), 1)
call_1780 = relay.TupleGetItem(func_939_call(), 1)
output = call_1779
output2 = call_1780
func_1790 = relay.Function([], output)
mod['func_1790'] = func_1790
mod = relay.transform.InferType()(mod)
output = func_1790()
func_1791 = relay.Function([], output)
mutated_mod['func_1791'] = func_1791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1811 = relay.var("var_1811", dtype = "uint64", shape = ())#candidate|1811|()|var|uint64
var_1812 = relay.var("var_1812", dtype = "uint64", shape = (15, 9, 1))#candidate|1812|(15, 9, 1)|var|uint64
bop_1813 = relay.right_shift(var_1811.astype('uint64'), var_1812.astype('uint64')) # shape=(15, 9, 1)
output = bop_1813
output2 = bop_1813
func_1822 = relay.Function([var_1811,var_1812,], output)
mod['func_1822'] = func_1822
mod = relay.transform.InferType()(mod)
mutated_mod['func_1822'] = func_1822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1822_call = mutated_mod.get_global_var('func_1822')
var_1824 = relay.var("var_1824", dtype = "uint64", shape = ())#candidate|1824|()|var|uint64
var_1825 = relay.var("var_1825", dtype = "uint64", shape = (15, 9, 1))#candidate|1825|(15, 9, 1)|var|uint64
call_1823 = func_1822_call(var_1824,var_1825,)
output = call_1823
func_1826 = relay.Function([var_1824,var_1825,], output)
mutated_mod['func_1826'] = func_1826
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1846 = relay.var("var_1846", dtype = "int32", shape = ())#candidate|1846|()|var|int32
var_1847 = relay.var("var_1847", dtype = "int32", shape = (11, 12, 4))#candidate|1847|(11, 12, 4)|var|int32
bop_1848 = relay.greater_equal(var_1846.astype('bool'), var_1847.astype('bool')) # shape=(11, 12, 4)
func_469_call = mod.get_global_var('func_469')
func_473_call = mutated_mod.get_global_var('func_473')
const_1854 = relay.const([[True],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True]], dtype = "bool")#candidate|1854|(810, 1)|const|bool
var_1855 = relay.var("var_1855", dtype = "int64", shape = (360,))#candidate|1855|(360,)|var|int64
call_1853 = relay.TupleGetItem(func_469_call(relay.reshape(const_1854.astype('bool'), [15, 9, 6]), relay.reshape(const_1854.astype('bool'), [15, 9, 6]), relay.reshape(var_1855.astype('int64'), [360,]), ), 5)
call_1856 = relay.TupleGetItem(func_473_call(relay.reshape(const_1854.astype('bool'), [15, 9, 6]), relay.reshape(const_1854.astype('bool'), [15, 9, 6]), relay.reshape(var_1855.astype('int64'), [360,]), ), 5)
output = relay.Tuple([bop_1848,call_1853,const_1854,var_1855,])
output2 = relay.Tuple([bop_1848,call_1856,const_1854,var_1855,])
func_1867 = relay.Function([var_1846,var_1847,var_1855,], output)
mod['func_1867'] = func_1867
mod = relay.transform.InferType()(mod)
var_1868 = relay.var("var_1868", dtype = "int32", shape = ())#candidate|1868|()|var|int32
var_1869 = relay.var("var_1869", dtype = "int32", shape = (11, 12, 4))#candidate|1869|(11, 12, 4)|var|int32
var_1870 = relay.var("var_1870", dtype = "int64", shape = (360,))#candidate|1870|(360,)|var|int64
output = func_1867(var_1868,var_1869,var_1870,)
func_1871 = relay.Function([var_1868,var_1869,var_1870,], output)
mutated_mod['func_1871'] = func_1871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1896 = relay.var("var_1896", dtype = "float64", shape = ())#candidate|1896|()|var|float64
var_1897 = relay.var("var_1897", dtype = "float64", shape = (10, 2, 2))#candidate|1897|(10, 2, 2)|var|float64
bop_1898 = relay.divide(var_1896.astype('float64'), var_1897.astype('float64')) # shape=(10, 2, 2)
func_1713_call = mod.get_global_var('func_1713')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_1902 = relay.TupleGetItem(func_1713_call(), 6)
call_1903 = relay.TupleGetItem(func_1715_call(), 6)
bop_1909 = relay.maximum(var_1897.astype('uint32'), var_1896.astype('uint32')) # shape=(10, 2, 2)
output = relay.Tuple([bop_1898,call_1902,bop_1909,])
output2 = relay.Tuple([bop_1898,call_1903,bop_1909,])
func_1926 = relay.Function([var_1896,var_1897,], output)
mod['func_1926'] = func_1926
mod = relay.transform.InferType()(mod)
var_1927 = relay.var("var_1927", dtype = "float64", shape = ())#candidate|1927|()|var|float64
var_1928 = relay.var("var_1928", dtype = "float64", shape = (10, 2, 2))#candidate|1928|(10, 2, 2)|var|float64
output = func_1926(var_1927,var_1928,)
func_1929 = relay.Function([var_1927,var_1928,], output)
mutated_mod['func_1929'] = func_1929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_1999 = relay.TupleGetItem(func_1488_call(), 0)
call_2000 = relay.TupleGetItem(func_1489_call(), 0)
func_902_call = mod.get_global_var('func_902')
func_904_call = mutated_mod.get_global_var('func_904')
call_2022 = relay.TupleGetItem(func_902_call(), 0)
call_2023 = relay.TupleGetItem(func_904_call(), 0)
func_562_call = mod.get_global_var('func_562')
func_565_call = mutated_mod.get_global_var('func_565')
var_2063 = relay.var("var_2063", dtype = "float32", shape = (11, 7))#candidate|2063|(11, 7)|var|float32
var_2064 = relay.var("var_2064", dtype = "float32", shape = (11, 14))#candidate|2064|(11, 14)|var|float32
call_2062 = func_562_call(relay.reshape(var_2063.astype('float32'), [11, 7, 1]), relay.reshape(var_2064.astype('float32'), [11, 7, 2]), )
call_2065 = func_562_call(relay.reshape(var_2063.astype('float32'), [11, 7, 1]), relay.reshape(var_2064.astype('float32'), [11, 7, 2]), )
output = relay.Tuple([call_1999,call_2022,call_2062,var_2063,var_2064,])
output2 = relay.Tuple([call_2000,call_2023,call_2065,var_2063,var_2064,])
func_2075 = relay.Function([var_2063,var_2064,], output)
mod['func_2075'] = func_2075
mod = relay.transform.InferType()(mod)
mutated_mod['func_2075'] = func_2075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2075_call = mutated_mod.get_global_var('func_2075')
var_2077 = relay.var("var_2077", dtype = "float32", shape = (11, 7))#candidate|2077|(11, 7)|var|float32
var_2078 = relay.var("var_2078", dtype = "float32", shape = (11, 14))#candidate|2078|(11, 14)|var|float32
call_2076 = func_2075_call(var_2077,var_2078,)
output = call_2076
func_2079 = relay.Function([var_2077,var_2078,], output)
mutated_mod['func_2079'] = func_2079
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2084 = relay.TupleGetItem(func_1488_call(), 1)
call_2085 = relay.TupleGetItem(func_1489_call(), 1)
func_1926_call = mod.get_global_var('func_1926')
func_1929_call = mutated_mod.get_global_var('func_1929')
const_2100 = relay.const(-4.751788, dtype = "float64")#candidate|2100|()|const|float64
const_2101 = relay.const([-9.507424,3.057042,-9.888145,-3.465412,-8.557829,0.851011,5.999935,-8.152438,1.186994,8.357779,4.708194,4.370629,-0.746072,8.727469,2.369857,6.054984,-4.340850,-2.291093,0.105877,-4.748767,8.561515,3.701203,9.137666,-3.250508,-2.510945,2.793636,-8.359718,8.592007,-9.042502,-4.898925,0.197543,4.707833,9.805289,-2.590750,6.905427,-1.769026,-9.707258,1.757347,5.928659,-3.683029], dtype = "float64")#candidate|2101|(40,)|const|float64
call_2099 = relay.TupleGetItem(func_1926_call(relay.reshape(const_2100.astype('float64'), []), relay.reshape(const_2101.astype('float64'), [10, 2, 2]), ), 2)
call_2102 = relay.TupleGetItem(func_1929_call(relay.reshape(const_2100.astype('float64'), []), relay.reshape(const_2101.astype('float64'), [10, 2, 2]), ), 2)
func_1628_call = mod.get_global_var('func_1628')
func_1631_call = mutated_mod.get_global_var('func_1631')
var_2111 = relay.var("var_2111", dtype = "float64", shape = (39, 6))#candidate|2111|(39, 6)|var|float64
call_2110 = relay.TupleGetItem(func_1628_call(relay.reshape(var_2111.astype('float64'), [3, 78])), 1)
call_2112 = relay.TupleGetItem(func_1631_call(relay.reshape(var_2111.astype('float64'), [3, 78])), 1)
bop_2120 = relay.floor_divide(call_2099.astype('float32'), relay.reshape(const_2101.astype('float32'), relay.shape_of(call_2099))) # shape=(10, 2, 2)
bop_2123 = relay.floor_divide(call_2102.astype('float32'), relay.reshape(const_2101.astype('float32'), relay.shape_of(call_2102))) # shape=(10, 2, 2)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
call_2126 = relay.TupleGetItem(func_880_call(relay.reshape(var_2111.astype('float64'), [2, 13, 9]), relay.reshape(var_2111.astype('float64'), [2, 13, 9]), ), 1)
call_2127 = relay.TupleGetItem(func_883_call(relay.reshape(var_2111.astype('float64'), [2, 13, 9]), relay.reshape(var_2111.astype('float64'), [2, 13, 9]), ), 1)
bop_2128 = relay.greater_equal(bop_2120.astype('bool'), relay.reshape(call_2099.astype('bool'), relay.shape_of(bop_2120))) # shape=(10, 2, 2)
bop_2131 = relay.greater_equal(bop_2123.astype('bool'), relay.reshape(call_2102.astype('bool'), relay.shape_of(bop_2123))) # shape=(10, 2, 2)
output = relay.Tuple([call_2084,const_2100,call_2110,var_2111,call_2126,bop_2128,])
output2 = relay.Tuple([call_2085,const_2100,call_2112,var_2111,call_2127,bop_2131,])
func_2137 = relay.Function([var_2111,], output)
mod['func_2137'] = func_2137
mod = relay.transform.InferType()(mod)
var_2138 = relay.var("var_2138", dtype = "float64", shape = (39, 6))#candidate|2138|(39, 6)|var|float64
output = func_2137(var_2138)
func_2139 = relay.Function([var_2138], output)
mutated_mod['func_2139'] = func_2139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2143 = relay.var("var_2143", dtype = "float32", shape = (5, 4, 4))#candidate|2143|(5, 4, 4)|var|float32
uop_2144 = relay.sinh(var_2143.astype('float32')) # shape=(5, 4, 4)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_2167 = relay.TupleGetItem(func_1488_call(), 1)
call_2168 = relay.TupleGetItem(func_1489_call(), 1)
output = relay.Tuple([uop_2144,call_2167,])
output2 = relay.Tuple([uop_2144,call_2168,])
func_2174 = relay.Function([var_2143,], output)
mod['func_2174'] = func_2174
mod = relay.transform.InferType()(mod)
mutated_mod['func_2174'] = func_2174
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2175 = relay.var("var_2175", dtype = "float32", shape = (5, 4, 4))#candidate|2175|(5, 4, 4)|var|float32
func_2174_call = mutated_mod.get_global_var('func_2174')
call_2176 = func_2174_call(var_2175)
output = call_2176
func_2177 = relay.Function([var_2175], output)
mutated_mod['func_2177'] = func_2177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_2261 = relay.TupleGetItem(func_677_call(), 0)
call_2262 = relay.TupleGetItem(func_679_call(), 0)
func_562_call = mod.get_global_var('func_562')
func_565_call = mutated_mod.get_global_var('func_565')
var_2271 = relay.var("var_2271", dtype = "float32", shape = (77,))#candidate|2271|(77,)|var|float32
const_2272 = relay.const([-0.672356,-9.318471,-0.678946,-2.554530,8.791966,4.914374,-4.371312,-7.492240,8.177245,5.511766,-0.048519,9.309128,3.784488,6.681968,-8.343550,-3.765860,-0.098809,1.185289,0.006383,4.470241,6.965799,-3.965507,-5.581565,3.883255,6.169883,-5.679778,4.619883,-4.085995,0.161098,8.703027,5.587232,1.143563,-7.241854,-8.095252,-6.988128,7.159474,-5.603391,7.729604,-0.529926,-5.068359,-7.828700,-0.830201,4.663583,-2.430459,-1.688995,-9.017649,1.607809,7.022922,-1.512612,9.912574,0.520629,-5.410143,-0.528098,9.948269,-8.580161,-0.214781,-4.254365,-2.623294,-5.408823,-6.075797,-5.435325,-2.446975,-9.197447,5.896714,8.894726,-4.824185,4.268894,-6.336920,-1.718577,7.844943,-5.588874,7.524425,-9.410474,-3.298834,-7.814325,3.286186,0.852030,-8.953726,4.876330,-3.376274,9.334736,2.929190,2.354691,-8.144533,0.970328,-6.018124,-7.306162,-0.268699,4.581814,9.372125,-4.610085,-9.398380,-9.738727,7.658280,-6.599792,-5.280425,-8.989786,1.699846,8.898529,-3.544059,5.839316,-8.658579,-1.136865,-5.939846,1.069460,-1.144873,-5.290416,4.706260,1.667822,-0.027938,-7.113525,0.100211,-3.874439,-3.904172,0.998170,3.903790,4.707976,-9.158876,-7.840732,9.754841,-3.327035,0.176870,-1.643222,8.045752,-6.995402,-8.177848,-7.913578,5.998257,-3.302800,-8.370129,-0.583815,-8.680139,-9.414424,-9.639520,7.602586,-0.968286,6.278478,-2.748138,3.496312,2.670745,6.029064,-8.074857,-3.108180,-6.944959,-9.899727,-2.718964,-6.599194,-9.224827,8.729423,-1.630466,3.367486,-8.269087,-2.938048,-6.576332], dtype = "float32")#candidate|2272|(154,)|const|float32
call_2270 = func_562_call(relay.reshape(var_2271.astype('float32'), [11, 7, 1]), relay.reshape(const_2272.astype('float32'), [11, 7, 2]), )
call_2273 = func_562_call(relay.reshape(var_2271.astype('float32'), [11, 7, 1]), relay.reshape(const_2272.astype('float32'), [11, 7, 2]), )
bop_2275 = relay.logical_or(call_2270.astype('bool'), relay.reshape(const_2272.astype('bool'), relay.shape_of(call_2270))) # shape=(11, 7, 2)
bop_2278 = relay.logical_or(call_2273.astype('bool'), relay.reshape(const_2272.astype('bool'), relay.shape_of(call_2273))) # shape=(11, 7, 2)
func_1867_call = mod.get_global_var('func_1867')
func_1871_call = mutated_mod.get_global_var('func_1871')
const_2282 = relay.const(-2, dtype = "int32")#candidate|2282|()|const|int32
var_2283 = relay.var("var_2283", dtype = "int32", shape = (264, 2))#candidate|2283|(264, 2)|var|int32
var_2284 = relay.var("var_2284", dtype = "int64", shape = (360,))#candidate|2284|(360,)|var|int64
call_2281 = relay.TupleGetItem(func_1867_call(relay.reshape(const_2282.astype('int32'), []), relay.reshape(var_2283.astype('int32'), [11, 12, 4]), relay.reshape(var_2284.astype('int64'), [360,]), ), 2)
call_2285 = relay.TupleGetItem(func_1871_call(relay.reshape(const_2282.astype('int32'), []), relay.reshape(var_2283.astype('int32'), [11, 12, 4]), relay.reshape(var_2284.astype('int64'), [360,]), ), 2)
output = relay.Tuple([call_2261,var_2271,bop_2275,call_2281,const_2282,var_2283,var_2284,])
output2 = relay.Tuple([call_2262,var_2271,bop_2278,call_2285,const_2282,var_2283,var_2284,])
func_2289 = relay.Function([var_2271,var_2283,var_2284,], output)
mod['func_2289'] = func_2289
mod = relay.transform.InferType()(mod)
mutated_mod['func_2289'] = func_2289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2289_call = mutated_mod.get_global_var('func_2289')
var_2291 = relay.var("var_2291", dtype = "float32", shape = (77,))#candidate|2291|(77,)|var|float32
var_2292 = relay.var("var_2292", dtype = "int32", shape = (264, 2))#candidate|2292|(264, 2)|var|int32
var_2293 = relay.var("var_2293", dtype = "int64", shape = (360,))#candidate|2293|(360,)|var|int64
call_2290 = func_2289_call(var_2291,var_2292,var_2293,)
output = call_2290
func_2294 = relay.Function([var_2291,var_2292,var_2293,], output)
mutated_mod['func_2294'] = func_2294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_2356 = relay.TupleGetItem(func_677_call(), 0)
call_2357 = relay.TupleGetItem(func_679_call(), 0)
output = call_2356
output2 = call_2357
func_2364 = relay.Function([], output)
mod['func_2364'] = func_2364
mod = relay.transform.InferType()(mod)
mutated_mod['func_2364'] = func_2364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mutated_mod.get_global_var('func_2364')
call_2365 = func_2364_call()
output = call_2365
func_2366 = relay.Function([], output)
mutated_mod['func_2366'] = func_2366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_2440 = func_820_call()
call_2441 = func_820_call()
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_2449 = func_741_call()
call_2450 = func_741_call()
output = relay.Tuple([call_2440,call_2449,])
output2 = relay.Tuple([call_2441,call_2450,])
func_2454 = relay.Function([], output)
mod['func_2454'] = func_2454
mod = relay.transform.InferType()(mod)
mutated_mod['func_2454'] = func_2454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mutated_mod.get_global_var('func_2454')
call_2455 = func_2454_call()
output = call_2455
func_2456 = relay.Function([], output)
mutated_mod['func_2456'] = func_2456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_2502 = relay.TupleGetItem(func_2454_call(), 1)
call_2503 = relay.TupleGetItem(func_2456_call(), 1)
func_2075_call = mod.get_global_var('func_2075')
func_2079_call = mutated_mod.get_global_var('func_2079')
var_2509 = relay.var("var_2509", dtype = "float32", shape = (1, 77))#candidate|2509|(1, 77)|var|float32
var_2510 = relay.var("var_2510", dtype = "float32", shape = (154,))#candidate|2510|(154,)|var|float32
call_2508 = relay.TupleGetItem(func_2075_call(relay.reshape(var_2509.astype('float32'), [11, 7]), relay.reshape(var_2510.astype('float32'), [11, 14]), ), 4)
call_2511 = relay.TupleGetItem(func_2079_call(relay.reshape(var_2509.astype('float32'), [11, 7]), relay.reshape(var_2510.astype('float32'), [11, 14]), ), 4)
func_1926_call = mod.get_global_var('func_1926')
func_1929_call = mutated_mod.get_global_var('func_1929')
const_2528 = relay.const(6.088652, dtype = "float64")#candidate|2528|()|const|float64
const_2529 = relay.const([7.226569,6.782362,8.019793,-0.245308,7.680065,-8.941098,3.934808,2.459514,-7.726282,6.696405,5.089906,8.620531,-6.887495,3.368936,6.466711,9.886403,8.424089,-0.462244,6.306143,1.455142,9.547305,-4.755928,9.180537,2.897554,4.679443,-2.304068,5.880457,1.041258,0.405312,-7.798844,5.570757,3.374114,-6.296159,2.445731,-2.897660,-9.772623,-4.575740,-2.876783,-5.861758,-0.092263], dtype = "float64")#candidate|2529|(40,)|const|float64
call_2527 = relay.TupleGetItem(func_1926_call(relay.reshape(const_2528.astype('float64'), []), relay.reshape(const_2529.astype('float64'), [10, 2, 2]), ), 0)
call_2530 = relay.TupleGetItem(func_1929_call(relay.reshape(const_2528.astype('float64'), []), relay.reshape(const_2529.astype('float64'), [10, 2, 2]), ), 0)
output = relay.Tuple([call_2502,call_2508,var_2509,var_2510,call_2527,const_2528,const_2529,])
output2 = relay.Tuple([call_2503,call_2511,var_2509,var_2510,call_2530,const_2528,const_2529,])
func_2557 = relay.Function([var_2509,var_2510,], output)
mod['func_2557'] = func_2557
mod = relay.transform.InferType()(mod)
mutated_mod['func_2557'] = func_2557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2557_call = mutated_mod.get_global_var('func_2557')
var_2559 = relay.var("var_2559", dtype = "float32", shape = (1, 77))#candidate|2559|(1, 77)|var|float32
var_2560 = relay.var("var_2560", dtype = "float32", shape = (154,))#candidate|2560|(154,)|var|float32
call_2558 = func_2557_call(var_2559,var_2560,)
output = call_2558
func_2561 = relay.Function([var_2559,var_2560,], output)
mutated_mod['func_2561'] = func_2561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1790_call = mod.get_global_var('func_1790')
func_1791_call = mutated_mod.get_global_var('func_1791')
call_2563 = func_1790_call()
call_2564 = func_1790_call()
func_1628_call = mod.get_global_var('func_1628')
func_1631_call = mutated_mod.get_global_var('func_1631')
var_2599 = relay.var("var_2599", dtype = "float64", shape = (234,))#candidate|2599|(234,)|var|float64
call_2598 = relay.TupleGetItem(func_1628_call(relay.reshape(var_2599.astype('float64'), [3, 78])), 2)
call_2600 = relay.TupleGetItem(func_1631_call(relay.reshape(var_2599.astype('float64'), [3, 78])), 2)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_2605 = relay.TupleGetItem(func_1334_call(), 0)
call_2606 = relay.TupleGetItem(func_1336_call(), 0)
func_2075_call = mod.get_global_var('func_2075')
func_2079_call = mutated_mod.get_global_var('func_2079')
var_2615 = relay.var("var_2615", dtype = "float32", shape = (11, 7))#candidate|2615|(11, 7)|var|float32
const_2616 = relay.const([2.095175,-7.044439,6.375624,-6.549205,-6.979990,-1.179099,-9.463364,-2.735403,-0.191756,4.911863,-0.687495,1.088415,-5.028010,-1.856329,4.667747,-9.825688,0.020851,2.531665,3.626130,8.838234,-1.175350,3.166260,-0.158811,4.443399,-2.287748,2.615815,-0.993986,2.634733,4.325117,1.640840,2.250007,-3.834635,-1.766817,5.732831,4.000156,0.902908,-8.614557,-3.649344,5.180710,0.233174,-5.551903,-2.587065,3.931553,-6.871787,4.232166,-1.703745,5.410065,8.897546,-9.271552,-2.234550,9.897383,5.052703,-3.083752,1.963174,6.605820,4.536010,0.673278,0.558509,7.153334,0.557583,9.425793,4.022758,-7.079251,-2.907210,4.045654,2.080122,8.109954,-7.201769,-0.001110,4.197323,-3.434609,-3.958682,-8.570046,9.891338,9.763577,-3.890439,-8.962033,3.315548,-2.085830,0.079250,-8.107151,-5.077549,4.850165,5.681634,-2.801523,-7.373626,9.834391,-1.320147,-7.840009,4.268101,3.534010,-7.480130,6.346280,-2.050901,5.681152,3.954952,-5.527872,2.762725,-8.249911,-2.341889,2.005400,-2.719146,5.869884,-9.675496,-4.818088,1.213546,0.436122,8.458671,0.734345,-8.907338,5.126991,4.158559,-6.798467,2.598096,6.708655,4.437162,-9.674269,-1.878807,8.191338,9.659472,-6.199370,4.193974,-5.534372,4.664058,-9.966133,7.555110,1.516547,-1.250028,7.976748,9.018877,0.044845,-2.281126,-6.863852,1.361069,5.916314,9.685227,3.446513,-1.045749,6.426537,6.721354,1.041806,2.513642,2.869178,-2.223272,1.127015,-2.564549,9.473487,0.069775,8.929506,2.946679,2.853991,-7.605501,3.556772,4.795243], dtype = "float32")#candidate|2616|(154,)|const|float32
call_2614 = relay.TupleGetItem(func_2075_call(relay.reshape(var_2615.astype('float32'), [11, 7]), relay.reshape(const_2616.astype('float32'), [11, 14]), ), 0)
call_2617 = relay.TupleGetItem(func_2079_call(relay.reshape(var_2615.astype('float32'), [11, 7]), relay.reshape(const_2616.astype('float32'), [11, 14]), ), 0)
output = relay.Tuple([call_2563,call_2598,var_2599,call_2605,call_2614,var_2615,const_2616,])
output2 = relay.Tuple([call_2564,call_2600,var_2599,call_2606,call_2617,var_2615,const_2616,])
func_2621 = relay.Function([var_2599,var_2615,], output)
mod['func_2621'] = func_2621
mod = relay.transform.InferType()(mod)
var_2622 = relay.var("var_2622", dtype = "float64", shape = (234,))#candidate|2622|(234,)|var|float64
var_2623 = relay.var("var_2623", dtype = "float32", shape = (11, 7))#candidate|2623|(11, 7)|var|float32
output = func_2621(var_2622,var_2623,)
func_2624 = relay.Function([var_2622,var_2623,], output)
mutated_mod['func_2624'] = func_2624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_2657 = relay.TupleGetItem(func_1736_call(), 0)
call_2658 = relay.TupleGetItem(func_1738_call(), 0)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_2671 = relay.TupleGetItem(func_1571_call(), 0)
call_2672 = relay.TupleGetItem(func_1573_call(), 0)
output = relay.Tuple([call_2657,call_2671,])
output2 = relay.Tuple([call_2658,call_2672,])
func_2678 = relay.Function([], output)
mod['func_2678'] = func_2678
mod = relay.transform.InferType()(mod)
mutated_mod['func_2678'] = func_2678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2678_call = mutated_mod.get_global_var('func_2678')
call_2679 = func_2678_call()
output = call_2679
func_2680 = relay.Function([], output)
mutated_mod['func_2680'] = func_2680
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2704 = relay.const([[[9,9,-1],[-6,7,9],[-9,5,-3],[9,3,-2],[3,-1,10],[7,9,-7]],[[6,-9,1],[-4,-10,-8],[-6,-9,-8],[-7,8,-10],[-2,-10,-4],[3,10,10]],[[2,2,3],[-7,6,-5],[-6,9,-10],[4,5,-5],[3,-8,4],[4,6,-7]],[[7,7,9],[-10,-6,-1],[-8,-2,-1],[4,9,-6],[-4,6,-8],[8,-7,1]]], dtype = "uint16")#candidate|2704|(4, 6, 3)|const|uint16
var_2705 = relay.var("var_2705", dtype = "uint16", shape = (4, 6, 3))#candidate|2705|(4, 6, 3)|var|uint16
bop_2706 = relay.less_equal(const_2704.astype('bool'), relay.reshape(var_2705.astype('bool'), relay.shape_of(const_2704))) # shape=(4, 6, 3)
uop_2717 = relay.exp(var_2705.astype('float32')) # shape=(4, 6, 3)
output = relay.Tuple([bop_2706,uop_2717,])
output2 = relay.Tuple([bop_2706,uop_2717,])
func_2755 = relay.Function([var_2705,], output)
mod['func_2755'] = func_2755
mod = relay.transform.InferType()(mod)
var_2756 = relay.var("var_2756", dtype = "uint16", shape = (4, 6, 3))#candidate|2756|(4, 6, 3)|var|uint16
output = func_2755(var_2756)
func_2757 = relay.Function([var_2756], output)
mutated_mod['func_2757'] = func_2757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_2807 = func_820_call()
call_2808 = func_820_call()
output = call_2807
output2 = call_2808
func_2815 = relay.Function([], output)
mod['func_2815'] = func_2815
mod = relay.transform.InferType()(mod)
output = func_2815()
func_2816 = relay.Function([], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_997_call = mod.get_global_var('func_997')
func_999_call = mutated_mod.get_global_var('func_999')
call_2842 = relay.TupleGetItem(func_997_call(), 0)
call_2843 = relay.TupleGetItem(func_999_call(), 0)
output = relay.Tuple([call_2842,])
output2 = relay.Tuple([call_2843,])
func_2846 = relay.Function([], output)
mod['func_2846'] = func_2846
mod = relay.transform.InferType()(mod)
mutated_mod['func_2846'] = func_2846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2846_call = mutated_mod.get_global_var('func_2846')
call_2847 = func_2846_call()
output = call_2847
func_2848 = relay.Function([], output)
mutated_mod['func_2848'] = func_2848
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2884 = relay.var("var_2884", dtype = "int16", shape = (12, 11, 15))#candidate|2884|(12, 11, 15)|var|int16
const_2885 = relay.const([[[-8,-5,9,-5,-6,4,-10,1,3,-1,-9,-2,4,-9,10],[9,4,-6,-4,5,-7,-1,-1,6,6,-6,-8,1,4,4],[-3,-1,-7,-1,7,10,-6,-2,-5,-9,-6,3,5,9,-4],[-1,-8,-6,-1,-7,-3,-2,-9,-6,-3,-3,-1,-6,-10,6],[-7,-3,-1,-1,5,1,-4,9,-7,6,-1,2,5,10,2],[9,5,6,10,8,-3,7,4,-1,-2,-3,-5,-7,-3,-6],[-5,4,-9,-5,8,-6,4,10,-3,9,7,-10,-8,-5,-6],[-8,7,10,-4,5,-2,-3,-8,2,-4,-7,-6,-3,6,7],[-10,4,9,-3,10,-5,3,-7,-10,2,-4,5,6,4,8],[3,-6,-7,-10,8,-10,-2,-2,4,2,6,-5,-5,10,10],[-1,-10,-9,-4,7,8,-6,2,1,-9,-2,-6,7,7,-1]],[[9,-1,2,4,-8,1,-2,-6,4,10,10,-8,10,-10,-5],[3,4,1,-3,-6,-7,9,-2,4,2,-9,8,1,-5,5],[1,-1,4,-2,6,10,-3,-5,-5,2,4,2,-1,10,-1],[3,4,6,6,5,-4,-7,5,5,-2,-7,-8,-8,1,4],[-4,-1,-3,-4,-5,-10,5,7,1,10,-8,-10,8,-7,8],[9,10,-8,-9,1,3,-2,-9,8,10,3,-9,-4,5,-5],[5,-4,-8,-10,-7,8,2,-8,-8,3,8,-3,3,3,-1],[10,4,4,8,-6,7,-5,-5,-2,-3,8,2,-8,3,10],[10,1,-4,8,1,9,10,-6,8,6,4,-3,-9,1,2],[5,1,-10,3,9,1,-1,-3,-6,7,-2,-9,-7,-8,8],[10,-6,1,10,-3,7,6,-7,-5,9,6,-2,10,1,10]],[[2,5,2,3,2,-10,1,7,6,8,3,-1,-9,6,1],[-1,3,10,-4,7,8,-4,-5,7,-2,-9,9,10,10,-7],[-10,-1,-6,10,3,-7,7,2,-2,-5,3,9,-3,9,-7],[-4,7,-1,8,3,3,4,1,3,-4,2,-2,9,-2,-7],[-5,5,8,-4,-1,8,7,3,-8,5,-5,-7,-8,2,-5],[8,-2,3,-2,6,6,-7,-6,4,1,5,-6,2,-9,5],[-5,-5,9,9,-6,7,1,-4,-6,-2,-8,2,-9,10,-3],[3,2,-7,7,2,-10,-5,3,-9,-8,8,8,-9,-6,-9],[6,7,2,-8,-9,-4,1,10,-9,-5,-10,2,-2,-6,-10],[9,7,-5,-7,9,7,-5,-3,4,-5,-6,1,4,-8,4],[-7,7,9,4,7,4,-7,2,-5,9,-5,-5,-4,2,1]],[[-2,-10,-2,-3,5,-10,-3,9,4,-2,-3,1,-3,-9,8],[10,-8,-1,9,7,-3,2,-3,-9,-4,1,8,-7,8,6],[8,10,-6,6,-4,-9,9,2,6,-8,-4,10,-2,3,-3],[-8,4,-6,-8,8,-7,-10,2,-10,-5,9,-9,1,5,3],[-2,-10,-10,1,-9,9,-7,4,-1,8,-3,5,-7,5,-10],[-10,1,1,6,-7,-10,-3,-7,8,9,6,-4,-6,-7,3],[-9,-2,-4,-2,-4,7,9,-2,-5,6,8,-8,3,5,4],[7,-4,-4,1,-9,6,2,-4,-4,5,-4,2,-7,-7,4],[2,-5,-10,5,6,10,-7,-9,-7,3,3,-6,1,-9,-6],[8,-4,-4,-3,-10,2,2,2,-2,4,-4,-3,1,4,2],[1,-9,4,-1,-4,-7,3,-6,1,-8,5,2,-10,4,3]],[[7,-8,10,2,1,6,-2,7,6,8,-3,-3,1,-9,9],[-8,7,3,-10,-3,-10,-10,8,10,3,5,1,2,3,-4],[1,-9,10,6,-6,2,7,-10,-9,-8,-10,-10,-3,10,2],[-8,-8,3,-8,9,-9,-2,2,1,4,-6,2,-7,8,9],[-3,-5,4,8,-7,6,9,2,1,3,-1,-2,-4,-8,-6],[2,-5,-2,-5,1,-9,-7,4,-10,-3,2,3,-8,5,-1],[4,2,-2,-8,-7,8,3,-2,5,4,6,-1,-2,-8,-5],[-7,4,-8,-6,-1,5,-8,-5,9,-4,-7,1,-9,-8,-9],[6,4,9,-6,8,5,9,4,-4,5,6,-8,1,-1,4],[4,7,-10,9,1,-3,3,-2,5,9,-5,3,1,1,-5],[-1,-5,-6,-7,8,4,-4,3,-3,-1,-10,7,-10,-9,10]],[[3,2,2,-10,-5,-4,-2,-4,-4,5,9,-4,9,7,-2],[-10,10,3,-4,-10,-5,-5,-5,-2,-8,-6,2,-5,1,-7],[-9,-8,-2,1,-5,-2,5,7,-8,9,-8,5,5,1,2],[-1,-6,1,1,4,1,6,5,6,-4,1,9,10,-8,2],[-10,2,-1,5,-3,7,7,1,-9,-7,-1,-5,-4,4,7],[-1,-8,-2,-6,-10,6,-6,-3,4,4,-6,-10,3,5,6],[-5,8,2,2,-7,-10,2,-7,-2,8,4,1,5,8,3],[-2,2,10,10,-3,-4,1,8,-10,10,-6,-4,-8,1,8],[1,2,8,7,-4,4,-5,6,2,6,6,6,-9,8,10],[5,6,5,9,-1,-6,5,-1,-5,-6,6,-4,-3,-9,-4],[7,-10,-7,8,-9,-3,5,6,-8,2,3,8,-2,-10,-4]],[[-10,4,-5,-7,10,-9,10,-2,1,-9,-6,10,-8,6,3],[-10,10,-5,6,-5,5,-1,9,3,-3,-4,-3,-4,-1,8],[-10,-9,4,-3,-3,1,2,6,5,-5,2,-9,8,-7,-6],[2,-5,4,2,-2,-6,4,-4,1,-10,10,-8,6,-6,2],[9,-6,5,-4,9,-2,10,3,8,5,-2,9,-6,5,-9],[-4,1,3,-1,-2,2,3,4,5,-2,10,-5,-6,-6,-5],[-10,-3,8,-6,2,9,-6,7,-10,1,-3,10,10,1,8],[10,2,8,9,10,4,7,-2,9,7,6,1,-7,1,-4],[3,-5,-7,-6,-9,-10,-6,4,-9,9,-2,-7,-2,-1,-2],[2,-1,10,-1,6,3,-4,1,4,-8,-8,-2,3,-9,7],[-9,9,-5,10,5,8,10,-6,8,4,5,-8,7,10,-6]],[[-1,3,7,-9,6,2,4,3,-4,-10,-1,-2,-3,-10,7],[2,-1,8,-5,-4,2,4,-8,6,2,-2,-2,-9,3,1],[-5,10,8,-1,-6,3,-1,-6,5,-2,-9,-9,-1,7,8],[-8,1,-9,7,-1,7,4,10,-8,1,4,-8,-10,-1,-5],[-7,4,-10,-4,-4,-1,-8,10,5,4,10,6,1,7,3],[1,-4,7,-9,-10,-5,-6,5,10,4,8,4,-3,7,4],[-3,-1,1,8,8,-3,-10,5,-4,7,-1,-3,-6,9,-10],[7,-2,-10,-4,-3,8,-5,-4,4,-5,6,-6,2,-9,7],[-6,3,-3,-10,-3,1,-10,10,7,2,8,2,10,6,-7],[-7,9,2,2,9,7,-7,-8,-1,-4,1,-4,6,6,-3],[6,7,-1,5,1,9,6,4,-6,1,1,-1,-4,1,8]],[[-5,4,-8,-1,8,-9,-9,-6,8,-10,-3,-10,6,-1,4],[-10,2,10,-9,-2,-10,-8,7,2,8,-6,-2,3,-10,6],[-2,2,-8,-5,-1,6,8,-2,9,-2,-5,6,-5,-7,3],[-7,-8,10,-1,-7,-2,4,8,-6,-10,-2,7,4,6,6],[-7,-4,-4,-4,-9,-5,-3,-2,-5,-8,7,1,7,-5,-9],[2,-6,2,3,2,7,5,-10,-3,-5,1,-2,-5,10,-1],[1,-4,4,-6,1,10,-9,8,-2,-4,3,-7,8,3,2],[-6,9,-1,-7,1,6,8,6,3,-8,-3,2,3,1,-7],[-1,-9,4,-3,-6,-9,-6,8,-4,8,-9,2,-2,-1,-2],[-8,-5,3,-7,-10,-1,-7,-7,-8,9,-2,10,10,-8,5],[-3,-1,9,6,10,-1,7,9,7,5,-7,4,1,-7,5]],[[9,4,6,3,1,10,-6,2,-10,-5,4,-2,-9,-2,-1],[8,-7,-9,-8,-5,-4,1,-9,-5,1,-6,4,-3,2,-9],[2,-3,2,10,-4,8,-7,10,-1,6,7,-7,9,-1,-3],[6,-10,4,10,-3,-8,-4,2,-2,-1,7,2,8,-5,-4],[1,-6,8,-2,-2,5,-6,7,-5,2,-9,3,-2,3,-1],[-8,7,-5,1,-3,2,5,9,7,10,7,8,-1,2,-10],[2,-5,-9,4,-10,5,7,2,-3,-7,10,-4,-5,-1,-8],[-1,-8,-9,-7,-8,-10,-8,4,-2,-1,-2,4,-1,1,-7],[2,1,-4,-6,-5,-9,7,1,-1,10,1,-5,10,-5,6],[1,-2,8,5,9,6,3,7,-9,-9,2,-3,-7,1,-3],[8,6,8,-5,6,1,4,-9,9,1,9,2,-8,-4,-2]],[[9,2,-7,-9,-1,6,1,7,-3,8,-6,7,8,6,-8],[10,8,3,2,8,9,7,-8,-9,-3,-4,3,-7,-9,-2],[3,4,-6,7,-1,5,-2,1,9,10,-9,10,-8,-5,-2],[-3,3,-6,-6,-8,9,8,-6,-1,1,6,6,5,5,-10],[-1,1,10,-2,10,3,3,-1,10,-3,-3,-4,5,4,1],[6,-5,-5,-4,-1,-7,6,-6,9,10,9,-9,4,-4,3],[-2,-5,-3,4,-7,4,1,-6,-6,5,4,-1,8,-8,-4],[6,-7,-3,-3,-10,3,-6,3,-1,6,-6,9,5,3,-10],[2,4,-10,2,5,-6,3,3,6,6,10,-2,7,8,1],[-8,-5,2,9,-9,-5,3,8,3,-1,-4,1,10,3,8],[6,-7,-8,6,-5,4,-1,8,-4,-1,-2,-6,3,10,3]],[[-2,-6,2,1,3,-5,4,5,-5,-4,6,3,8,-7,6],[8,1,-8,-8,-4,-5,-10,-5,2,6,6,4,3,5,-2],[-1,10,4,8,-9,5,-1,2,9,-6,3,-8,-1,-1,-2],[7,3,9,7,9,8,-7,-8,5,-6,4,-2,6,-3,10],[-2,-1,6,2,7,-7,-5,6,-5,1,-1,-1,-5,-4,8],[4,-3,-2,-6,10,6,-10,2,-2,-6,-10,-6,-10,2,9],[-10,-7,-1,9,5,-3,-9,-10,1,-9,5,-8,4,3,-3],[-5,7,-7,-3,8,-8,-9,-5,7,4,-5,-5,1,-10,-5],[-9,8,-4,-6,3,-7,4,5,6,5,8,-1,4,4,8],[-9,-2,3,-3,-3,3,-7,-5,-8,4,2,-5,7,-5,-3],[2,8,-2,10,-1,4,-2,-5,-3,7,-4,1,2,-9,1]]], dtype = "int16")#candidate|2885|(12, 11, 15)|const|int16
bop_2886 = relay.bitwise_and(var_2884.astype('int16'), relay.reshape(const_2885.astype('int16'), relay.shape_of(var_2884))) # shape=(12, 11, 15)
bop_2893 = relay.maximum(var_2884.astype('int16'), relay.reshape(const_2885.astype('int16'), relay.shape_of(var_2884))) # shape=(12, 11, 15)
bop_2907 = relay.bitwise_or(bop_2893.astype('int16'), relay.reshape(var_2884.astype('int16'), relay.shape_of(bop_2893))) # shape=(12, 11, 15)
func_1154_call = mod.get_global_var('func_1154')
func_1156_call = mutated_mod.get_global_var('func_1156')
const_2911 = relay.const([-4.084441,1.017597,5.038036,-8.500547,9.917708,4.718176,7.178748,-5.549432,-7.054137,1.174605,2.606926,-8.482719,7.738985,-7.168895,1.997623,-8.398673,3.826174,-8.243052,-1.232589,3.838259,-6.762827,-4.248578,-1.516499,-5.534895,6.466591,-0.394715,4.092017,9.567233,1.361542,6.904763,-6.812418,-9.354925,0.381192,6.014786,4.162667,-5.687735,2.976112,2.194135,6.211500,-7.662022,8.650843,2.465827,4.378053,-2.769872,3.185294,6.712020,9.051469,1.396069,-0.134683,7.148344,3.515086,-8.102616,-9.028328,-1.352583,2.033770,-4.032471,-7.336690,-8.279704,-6.898597,-8.366125,-8.277378,-6.638943,4.724316,8.069507,-6.343794,-3.523263,-6.078421,-6.451734,-1.375683,-7.644453,5.845116,1.950340,-8.418770,-4.254113,-5.935875,-1.898161,-6.629232,-1.989072,5.870764,-3.755470,-8.609867,4.144477,7.818763,7.434257,3.704927,6.913533,-4.266829,-1.188794,-6.415445,-8.437469,9.032571,-3.719845,5.281053,0.110745,-7.671355,-3.374304,-4.712610,0.622398,1.792638,-9.106079,-5.595985,2.715980,-0.589914,0.838614,-6.628640,4.549500,1.177587,-0.676045,-7.571747,0.634751,4.642312,-9.166231,7.099901,6.830903,-5.112674,4.823960,1.071991,-7.353307,-8.231543,6.443108,8.208045,-2.395495,-3.412745,0.351715,6.409539,2.320213,-0.727771,-9.007588,4.204347,-9.942598,6.135944,-6.712872,-9.188728,-5.382915,-7.835389,-4.845051,-8.970827,-4.381821,7.726622,-4.300621,-7.353798,9.376405,2.946855,2.205779,8.542018,-2.259562,6.016089,9.368361,4.847008,7.544797,6.094391,0.853903,-1.611974,-2.585799,3.074853,-0.353101,-9.353195,-9.635605,-6.665038,-6.911227,1.908405,-3.798431,6.344610,8.030967,-9.517283,4.375187,-4.299555,6.492214,-4.215647,-4.773272,-5.253437,-9.398507,-3.947689,-6.190325,-6.546803,-9.618663,-4.943161,-5.885082,-9.119384,-3.852254,-8.662270,5.430714,0.082614,-5.419407,-2.833562,5.189819,5.410001,-2.918437,5.592007,-0.247657,5.526834,1.876499,-7.674872,-2.064431,1.883390,0.192090,-3.578127,-7.017293,5.235032,3.649022,0.797615,0.413485,-7.795521,-0.008890,-5.070059,4.306641,4.850144,6.137676,0.098602,3.181186,7.014960,-5.093352,1.300607,4.153697,1.072635,-5.817341,0.153551,-3.694356,5.618559,8.089672,9.323896,-1.453344,-9.054555,-2.151946,7.326983,-1.758119,-3.350014,-4.441266,-9.374546,9.837128,-9.401389,-4.447039,7.955444,-9.412628], dtype = "float64")#candidate|2911|(234,)|const|float64
call_2910 = relay.TupleGetItem(func_1154_call(relay.reshape(const_2911.astype('float64'), [234,])), 0)
call_2912 = relay.TupleGetItem(func_1156_call(relay.reshape(const_2911.astype('float64'), [234,])), 0)
uop_2914 = relay.acos(bop_2907.astype('float32')) # shape=(12, 11, 15)
output = relay.Tuple([bop_2886,call_2910,const_2911,uop_2914,])
output2 = relay.Tuple([bop_2886,call_2912,const_2911,uop_2914,])
func_2916 = relay.Function([var_2884,], output)
mod['func_2916'] = func_2916
mod = relay.transform.InferType()(mod)
mutated_mod['func_2916'] = func_2916
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2917 = relay.var("var_2917", dtype = "int16", shape = (12, 11, 15))#candidate|2917|(12, 11, 15)|var|int16
func_2916_call = mutated_mod.get_global_var('func_2916')
call_2918 = func_2916_call(var_2917)
output = call_2918
func_2919 = relay.Function([var_2917], output)
mutated_mod['func_2919'] = func_2919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2846_call = mod.get_global_var('func_2846')
func_2848_call = mutated_mod.get_global_var('func_2848')
call_2921 = relay.TupleGetItem(func_2846_call(), 0)
call_2922 = relay.TupleGetItem(func_2848_call(), 0)
output = relay.Tuple([call_2921,])
output2 = relay.Tuple([call_2922,])
func_2940 = relay.Function([], output)
mod['func_2940'] = func_2940
mod = relay.transform.InferType()(mod)
mutated_mod['func_2940'] = func_2940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2940_call = mutated_mod.get_global_var('func_2940')
call_2941 = func_2940_call()
output = call_2941
func_2942 = relay.Function([], output)
mutated_mod['func_2942'] = func_2942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_3033 = func_2815_call()
call_3034 = func_2815_call()
func_2678_call = mod.get_global_var('func_2678')
func_2680_call = mutated_mod.get_global_var('func_2680')
call_3035 = relay.TupleGetItem(func_2678_call(), 0)
call_3036 = relay.TupleGetItem(func_2680_call(), 0)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_3045 = relay.TupleGetItem(func_2454_call(), 0)
call_3046 = relay.TupleGetItem(func_2456_call(), 0)
func_2289_call = mod.get_global_var('func_2289')
func_2294_call = mutated_mod.get_global_var('func_2294')
var_3054 = relay.var("var_3054", dtype = "float32", shape = (77,))#candidate|3054|(77,)|var|float32
var_3055 = relay.var("var_3055", dtype = "int32", shape = (528,))#candidate|3055|(528,)|var|int32
const_3056 = relay.const([-2,-8,5,-4,-5,-2,-8,1,5,3,10,8,10,3,2,2,2,5,-9,8,3,9,3,7,-5,-7,6,2,-5,-5,-7,-1,8,8,-2,5,6,-7,5,-7,8,3,1,-9,4,-3,2,-2,9,10,-4,-1,9,1,5,4,4,-7,-7,-3,-10,-2,10,3,-1,3,5,8,-3,8,9,-9,-1,9,-3,-7,-9,-5,2,-10,-10,10,8,-1,-9,7,3,10,-4,-2,-3,10,-9,-3,-3,-3,6,10,3,5,10,-7,-9,7,-8,-10,7,5,5,6,-8,2,-4,10,-2,9,-6,-7,3,-10,-10,-4,-2,-4,6,6,-10,-10,1,-4,-4,6,-9,-8,-6,5,-1,-4,9,-10,9,9,-6,-6,10,1,2,5,-2,-4,-1,6,-10,-5,-10,2,-4,-1,-1,-7,-8,4,-8,1,-9,-8,-6,4,-5,-2,5,4,-8,-10,-1,-9,-5,-9,1,-3,-5,-3,-5,6,8,-3,-4,2,2,-1,9,2,-3,9,10,-4,-2,7,-6,7,1,-6,-9,-8,-2,-5,-1,7,1,7,9,-8,2,10,8,-1,9,7,6,10,6,-9,6,10,3,9,-1,-4,-2,-9,4,-1,-7,-3,-4,9,10,-7,-5,4,-2,-1,-9,6,-1,-4,-4,10,-3,-4,-5,7,2,-10,10,-6,-8,-7,-4,-10,7,2,9,3,-2,-9,2,2,1,-3,-7,-5,-6,2,3,-4,6,-2,-7,-6,-1,-6,2,-7,2,-4,-8,4,1,-3,7,-3,-3,-9,9,9,-10,-3,5,-5,-9,-5,-10,-1,2,3,1,-4,2,-5,9,-3,1,1,-5,2,-9,-8,-4,8,-1,9,1,-8,-7,6,-7,4,4,-3,-4,-10,1,-2,7,1,4,-1,5,10,10,-7,6,6,-1,-8,3,-9,-7,7,2,-1,-2,-1,-2,7,8,1,-9,5], dtype = "int64")#candidate|3056|(360,)|const|int64
call_3053 = relay.TupleGetItem(func_2289_call(relay.reshape(var_3054.astype('float32'), [77,]), relay.reshape(var_3055.astype('int32'), [264, 2]), relay.reshape(const_3056.astype('int64'), [360,]), ), 3)
call_3057 = relay.TupleGetItem(func_2294_call(relay.reshape(var_3054.astype('float32'), [77,]), relay.reshape(var_3055.astype('int32'), [264, 2]), relay.reshape(const_3056.astype('int64'), [360,]), ), 3)
bop_3067 = relay.equal(var_3054.astype('bool'), call_3053.astype('bool')) # shape=(810, 77)
bop_3070 = relay.equal(var_3054.astype('bool'), call_3057.astype('bool')) # shape=(810, 77)
bop_3086 = relay.minimum(call_3045.astype('float64'), call_3053.astype('float64')) # shape=(810, 10)
bop_3089 = relay.minimum(call_3046.astype('float64'), call_3057.astype('float64')) # shape=(810, 10)
bop_3107 = relay.not_equal(call_3053.astype('bool'), call_3045.astype('bool')) # shape=(810, 10)
bop_3110 = relay.not_equal(call_3057.astype('bool'), call_3046.astype('bool')) # shape=(810, 10)
bop_3125 = relay.greater(bop_3086.astype('bool'), relay.reshape(bop_3107.astype('bool'), relay.shape_of(bop_3086))) # shape=(810, 10)
bop_3128 = relay.greater(bop_3089.astype('bool'), relay.reshape(bop_3110.astype('bool'), relay.shape_of(bop_3089))) # shape=(810, 10)
bop_3130 = relay.bitwise_xor(bop_3067.astype('int8'), call_3053.astype('int8')) # shape=(810, 77)
bop_3133 = relay.bitwise_xor(bop_3070.astype('int8'), call_3057.astype('int8')) # shape=(810, 77)
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
call_3135 = func_190_call(relay.reshape(const_3056.astype('int64'), [8, 5, 9]), relay.reshape(const_3056.astype('int64'), [8, 5, 9]), )
call_3136 = func_190_call(relay.reshape(const_3056.astype('int64'), [8, 5, 9]), relay.reshape(const_3056.astype('int64'), [8, 5, 9]), )
bop_3138 = relay.minimum(bop_3067.astype('int8'), relay.reshape(bop_3130.astype('int8'), relay.shape_of(bop_3067))) # shape=(810, 77)
bop_3141 = relay.minimum(bop_3070.astype('int8'), relay.reshape(bop_3133.astype('int8'), relay.shape_of(bop_3070))) # shape=(810, 77)
bop_3142 = relay.left_shift(bop_3107.astype('uint64'), call_3045.astype('uint64')) # shape=(810, 10)
bop_3145 = relay.left_shift(bop_3110.astype('uint64'), call_3046.astype('uint64')) # shape=(810, 10)
bop_3149 = relay.logical_or(bop_3142.astype('bool'), relay.reshape(bop_3125.astype('bool'), relay.shape_of(bop_3142))) # shape=(810, 10)
bop_3152 = relay.logical_or(bop_3145.astype('bool'), relay.reshape(bop_3128.astype('bool'), relay.shape_of(bop_3145))) # shape=(810, 10)
bop_3156 = relay.less(bop_3149.astype('bool'), relay.reshape(bop_3125.astype('bool'), relay.shape_of(bop_3149))) # shape=(810, 10)
bop_3159 = relay.less(bop_3152.astype('bool'), relay.reshape(bop_3128.astype('bool'), relay.shape_of(bop_3152))) # shape=(810, 10)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3162 = relay.TupleGetItem(func_1488_call(), 1)
call_3163 = relay.TupleGetItem(func_1489_call(), 1)
uop_3171 = relay.sinh(bop_3130.astype('float64')) # shape=(810, 77)
uop_3173 = relay.sinh(bop_3133.astype('float64')) # shape=(810, 77)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_3192 = func_2364_call()
call_3193 = func_2364_call()
output = relay.Tuple([call_3033,call_3035,var_3055,const_3056,call_3135,bop_3138,bop_3156,call_3162,uop_3171,call_3192,])
output2 = relay.Tuple([call_3034,call_3036,var_3055,const_3056,call_3136,bop_3141,bop_3159,call_3163,uop_3173,call_3193,])
func_3194 = relay.Function([var_3054,var_3055,], output)
mod['func_3194'] = func_3194
mod = relay.transform.InferType()(mod)
var_3195 = relay.var("var_3195", dtype = "float32", shape = (77,))#candidate|3195|(77,)|var|float32
var_3196 = relay.var("var_3196", dtype = "int32", shape = (528,))#candidate|3196|(528,)|var|int32
output = func_3194(var_3195,var_3196,)
func_3197 = relay.Function([var_3195,var_3196,], output)
mutated_mod['func_3197'] = func_3197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2940_call = mod.get_global_var('func_2940')
func_2942_call = mutated_mod.get_global_var('func_2942')
call_3230 = relay.TupleGetItem(func_2940_call(), 0)
call_3231 = relay.TupleGetItem(func_2942_call(), 0)
output = call_3230
output2 = call_3231
func_3236 = relay.Function([], output)
mod['func_3236'] = func_3236
mod = relay.transform.InferType()(mod)
mutated_mod['func_3236'] = func_3236
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mutated_mod.get_global_var('func_3236')
call_3237 = func_3236_call()
output = call_3237
func_3238 = relay.Function([], output)
mutated_mod['func_3238'] = func_3238
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_3270 = func_650_call()
call_3271 = func_650_call()
func_2940_call = mod.get_global_var('func_2940')
func_2942_call = mutated_mod.get_global_var('func_2942')
call_3294 = relay.TupleGetItem(func_2940_call(), 0)
call_3295 = relay.TupleGetItem(func_2942_call(), 0)
bop_3315 = relay.bitwise_or(call_3270.astype('uint32'), relay.reshape(call_3294.astype('uint32'), relay.shape_of(call_3270))) # shape=(1, 10)
bop_3318 = relay.bitwise_or(call_3271.astype('uint32'), relay.reshape(call_3295.astype('uint32'), relay.shape_of(call_3271))) # shape=(1, 10)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_3320 = relay.TupleGetItem(func_1488_call(), 1)
call_3321 = relay.TupleGetItem(func_1489_call(), 1)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_3339 = func_820_call()
call_3340 = func_820_call()
func_1628_call = mod.get_global_var('func_1628')
func_1631_call = mutated_mod.get_global_var('func_1631')
const_3344 = relay.const([[-7.812939,0.402307],[6.070157,2.891696],[-7.020122,-8.715012],[-1.917665,-3.163188],[2.215632,-4.175020],[9.785204,-4.854983],[-4.564113,0.757586],[7.271795,2.865834],[-4.482003,0.606106],[7.366760,6.072212],[3.406580,6.029625],[8.484357,-3.706143],[-1.935590,5.569437],[-5.024483,1.600741],[1.545727,4.334629],[5.821680,8.428346],[4.028150,6.592629],[7.224255,3.415621],[-7.348059,-0.238929],[-7.846354,9.712150],[-3.954457,-5.019385],[-7.710804,7.684734],[-2.481009,-2.335238],[2.876356,-4.838026],[-4.578546,-3.721221],[-4.372765,-2.914218],[-1.432022,0.222686],[4.070805,-4.498037],[3.319547,-1.149030],[-1.925139,-5.399006],[-3.277879,-9.772974],[-5.677479,3.826649],[-8.184817,-5.267800],[7.604095,-2.960290],[-8.406427,-2.650568],[-3.304523,6.572936],[0.320259,8.505233],[4.444117,-2.360654],[-9.504042,3.586490],[1.734725,-5.822484],[-7.855265,4.388971],[9.348676,-5.107003],[8.379155,-1.292227],[4.942465,4.794851],[9.815256,-7.365350],[-2.737215,4.989059],[-8.918642,4.965196],[5.650007,9.909245],[1.558203,1.561783],[-4.993153,-1.890961],[-3.213734,3.563935],[-2.970825,-6.484711],[9.543428,-0.186097],[8.336233,2.210843],[-1.534877,-9.384281],[-8.730340,-3.855374],[-5.306269,-5.209185],[9.119020,-3.978531],[7.525390,2.443507],[-0.598598,-0.641579],[-6.087334,-0.850108],[-3.502747,4.907028],[-4.050389,-9.543668],[-4.731821,-5.831228],[-2.323244,6.171395],[7.760796,8.548765],[-1.984673,-0.261399],[-8.032820,-6.600746],[4.407470,-1.112123],[-3.988773,7.865013],[7.286854,9.533816],[-0.620086,-9.952929],[4.471035,-0.307454],[3.066466,5.231044],[-0.908159,5.887494],[-4.270017,1.406162],[-2.339301,1.082303],[-6.681571,7.191984],[-7.856345,8.548935],[5.246773,5.228879],[8.151901,4.663247],[4.155993,-0.605286],[8.040062,-5.675635],[-9.632897,6.508095],[-0.017067,6.541331],[5.223197,-5.569892],[-3.762460,-7.145459],[-7.618203,-1.704589],[8.026375,-0.592176],[-3.648700,-9.933686],[-5.678231,-2.186461],[9.495067,3.027697],[-8.900340,-6.666997],[-3.907070,-9.423138],[-2.445052,-6.819852],[-8.795895,-6.083895],[-7.769328,0.415196],[-7.902570,-0.836431],[-8.090356,9.720489],[3.505622,5.651349],[4.218217,8.688350],[3.139364,-5.766505],[3.918303,-0.261016],[8.468701,6.372268],[5.759561,5.540247],[4.968428,3.213870],[-3.171982,4.694982],[5.014965,2.435585],[-2.073231,-1.024598],[-6.558347,0.378333],[3.852381,-2.626058],[-8.410669,7.429516],[-1.466697,8.326755],[-3.322242,4.478378],[2.226982,-7.783697],[-2.467385,-8.209502],[9.938818,-8.900258]], dtype = "float64")#candidate|3344|(117, 2)|const|float64
call_3343 = relay.TupleGetItem(func_1628_call(relay.reshape(const_3344.astype('float64'), [3, 78])), 0)
call_3345 = relay.TupleGetItem(func_1631_call(relay.reshape(const_3344.astype('float64'), [3, 78])), 0)
func_938_call = mod.get_global_var('func_938')
func_939_call = mutated_mod.get_global_var('func_939')
call_3367 = relay.TupleGetItem(func_938_call(), 1)
call_3368 = relay.TupleGetItem(func_939_call(), 1)
func_2557_call = mod.get_global_var('func_2557')
func_2561_call = mutated_mod.get_global_var('func_2561')
var_3371 = relay.var("var_3371", dtype = "float32", shape = (11, 7))#candidate|3371|(11, 7)|var|float32
const_3372 = relay.const([[-1.733834],[2.428024],[-3.819940],[-5.493433],[-4.602782],[0.795699],[9.244202],[9.763264],[-9.101950],[-1.868064],[-3.986229],[1.016766],[0.874629],[2.712693],[8.620943],[-6.832758],[0.479005],[-8.572028],[7.466398],[4.496900],[-2.943218],[-4.973793],[-7.830056],[-1.315887],[-0.319364],[5.193175],[3.348245],[-9.035451],[-6.147181],[1.433581],[5.283355],[4.651538],[2.907426],[6.554674],[-0.153163],[-5.513670],[2.798288],[3.903703],[-1.699432],[-1.801714],[-7.884913],[-3.175104],[0.252952],[-7.408125],[-7.523570],[3.666391],[2.982198],[-2.970394],[-2.717152],[2.744489],[0.878854],[8.374593],[-4.561162],[-7.334565],[5.496682],[-6.652689],[-7.813565],[7.715514],[8.804432],[5.612078],[8.565144],[-2.610216],[9.920043],[-4.466464],[-3.034721],[8.729528],[2.158911],[-4.090275],[7.636981],[2.141652],[-3.997054],[-7.897941],[-7.793741],[-4.551546],[1.850810],[0.807058],[-3.389692],[1.042351],[5.598753],[-7.008181],[5.503338],[1.881649],[-8.365362],[7.589827],[-7.307451],[-8.225270],[-9.358844],[3.062766],[8.813377],[-3.932961],[-5.332927],[0.818062],[9.761195],[-8.589206],[-1.082933],[-0.639894],[-5.024139],[9.110989],[-5.653644],[-3.268367],[8.394219],[4.770432],[4.524307],[-5.640453],[-8.615661],[7.743690],[-2.293652],[6.334683],[2.953784],[-0.810695],[-8.056358],[-7.909348],[-9.935020],[-2.628069],[-8.550540],[0.695044],[8.119235],[4.160920],[-4.961313],[1.657536],[-0.317317],[6.806191],[-6.444388],[2.196604],[-0.030519],[6.706494],[-3.644242],[-2.685656],[9.769475],[2.061022],[3.962766],[5.625261],[8.737140],[-0.498681],[-3.134047],[-6.465302],[-7.763965],[-0.546019],[7.760737],[8.445525],[4.339017],[-9.691872],[-6.547128],[0.155130],[4.004969],[0.114452],[3.651093],[-8.997430],[4.437527],[-8.682746],[-5.942844],[-7.898915],[-6.700092],[3.067447]], dtype = "float32")#candidate|3372|(154, 1)|const|float32
call_3370 = relay.TupleGetItem(func_2557_call(relay.reshape(var_3371.astype('float32'), [1, 77]), relay.reshape(const_3372.astype('float32'), [154,]), ), 5)
call_3373 = relay.TupleGetItem(func_2561_call(relay.reshape(var_3371.astype('float32'), [1, 77]), relay.reshape(const_3372.astype('float32'), [154,]), ), 5)
output = relay.Tuple([bop_3315,call_3320,call_3339,call_3343,const_3344,call_3367,call_3370,var_3371,const_3372,])
output2 = relay.Tuple([bop_3318,call_3321,call_3340,call_3345,const_3344,call_3368,call_3373,var_3371,const_3372,])
func_3375 = relay.Function([var_3371,], output)
mod['func_3375'] = func_3375
mod = relay.transform.InferType()(mod)
mutated_mod['func_3375'] = func_3375
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3376 = relay.var("var_3376", dtype = "float32", shape = (11, 7))#candidate|3376|(11, 7)|var|float32
func_3375_call = mutated_mod.get_global_var('func_3375')
call_3377 = func_3375_call(var_3376)
output = call_3377
func_3378 = relay.Function([var_3376], output)
mutated_mod['func_3378'] = func_3378
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3380 = relay.var("var_3380", dtype = "bool", shape = ())#candidate|3380|()|var|bool
var_3381 = relay.var("var_3381", dtype = "bool", shape = (10, 2, 7))#candidate|3381|(10, 2, 7)|var|bool
bop_3382 = relay.logical_or(var_3380.astype('bool'), var_3381.astype('bool')) # shape=(10, 2, 7)
output = bop_3382
output2 = bop_3382
func_3388 = relay.Function([var_3380,var_3381,], output)
mod['func_3388'] = func_3388
mod = relay.transform.InferType()(mod)
mutated_mod['func_3388'] = func_3388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3388_call = mutated_mod.get_global_var('func_3388')
var_3390 = relay.var("var_3390", dtype = "bool", shape = ())#candidate|3390|()|var|bool
var_3391 = relay.var("var_3391", dtype = "bool", shape = (10, 2, 7))#candidate|3391|(10, 2, 7)|var|bool
call_3389 = func_3388_call(var_3390,var_3391,)
output = call_3389
func_3392 = relay.Function([var_3390,var_3391,], output)
mutated_mod['func_3392'] = func_3392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_3425 = func_3236_call()
call_3426 = func_3236_call()
output = relay.Tuple([call_3425,])
output2 = relay.Tuple([call_3426,])
func_3428 = relay.Function([], output)
mod['func_3428'] = func_3428
mod = relay.transform.InferType()(mod)
mutated_mod['func_3428'] = func_3428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3428_call = mutated_mod.get_global_var('func_3428')
call_3429 = func_3428_call()
output = call_3429
func_3430 = relay.Function([], output)
mutated_mod['func_3430'] = func_3430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_3468 = relay.TupleGetItem(func_589_call(), 0)
call_3469 = relay.TupleGetItem(func_590_call(), 0)
output = relay.Tuple([call_3468,])
output2 = relay.Tuple([call_3469,])
func_3471 = relay.Function([], output)
mod['func_3471'] = func_3471
mod = relay.transform.InferType()(mod)
mutated_mod['func_3471'] = func_3471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mutated_mod.get_global_var('func_3471')
call_3472 = func_3471_call()
output = call_3472
func_3473 = relay.Function([], output)
mutated_mod['func_3473'] = func_3473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_3493 = relay.TupleGetItem(func_2454_call(), 1)
call_3494 = relay.TupleGetItem(func_2456_call(), 1)
output = relay.Tuple([call_3493,])
output2 = relay.Tuple([call_3494,])
func_3535 = relay.Function([], output)
mod['func_3535'] = func_3535
mod = relay.transform.InferType()(mod)
mutated_mod['func_3535'] = func_3535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3535_call = mutated_mod.get_global_var('func_3535')
call_3536 = func_3535_call()
output = call_3536
func_3537 = relay.Function([], output)
mutated_mod['func_3537'] = func_3537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_3561 = func_2364_call()
call_3562 = func_2364_call()
func_1773_call = mod.get_global_var('func_1773')
func_1777_call = mutated_mod.get_global_var('func_1777')
var_3564 = relay.var("var_3564", dtype = "float32", shape = (1, 77))#candidate|3564|(1, 77)|var|float32
const_3565 = relay.const([-0.331669,-3.493756,-2.753420,-9.048685,-8.584904,2.877996,-7.196438,6.643937,7.328541,-7.551449,-7.786086,3.297874,-1.284555,0.305881,-2.361023,0.809010,0.762551,-7.362219,1.665394,-9.541447,-2.270691,2.418895,-9.383683,7.128267,9.224056,-5.101718,-7.329118,-7.538096,-8.025649,9.809995,-7.084176,2.705007,-2.328342,8.779135,-8.592658,5.411163,-6.811789,4.609925,6.828253,-0.970674,5.387706,7.212365,-1.345958,-5.231379,0.645885,1.644883,-1.224864,-6.713425,1.424939,-3.217451,7.657860,-2.614694,-9.072124,-4.017100,-9.126862,4.366769,1.388907,8.837340,-7.416383,-4.691114,9.212697,-4.107917,0.782535,-3.886927,-1.401358,-7.054858,1.558556,8.021187,9.618419,0.590326,2.034944,4.573856,0.738936,-6.195507,-1.054271,-9.160495,2.325658,5.770706,3.117154,5.512145,8.209981,6.237575,-0.915744,-1.586001,-4.287388,8.065384,-1.068610,-0.507495,1.587873,-8.073179,-0.717574,-7.589825,8.253052,-7.230822,3.464525,-7.452949,5.972265,4.453210,9.720808,1.803533,-0.150339,9.214516,6.470443,-5.711744,-2.664463,-7.950388,5.827487,-1.444340,4.670459,1.943793,-8.426827,1.277787,9.266722,0.827200,-2.703906,-6.494791,7.345364,-8.609945,-4.208293,-0.376722,9.743884,5.510933,8.510024,6.897927,-0.271172,3.949160,-0.774648,-5.414265,-7.200315,-6.383197,5.635384,9.579592,-2.084663,7.419734,-2.190311,-0.121656,6.938377,3.050661,6.844424,9.109464,8.309233,3.292188,0.170485,-1.797096,3.509765,-8.074558,2.797634,-4.185292,9.457552,-2.173587,3.975871,3.689861,-0.088808,3.915556], dtype = "float32")#candidate|3565|(154,)|const|float32
const_3566 = relay.const([4.153296,3.814043,6.895099,-7.775901,-4.383257,6.823543,-4.012630,-1.342408,7.028300,-5.325407,4.561122,6.915394,-9.454970,7.770921,2.231054,-6.007653,3.971387,9.157329,2.620363,-9.963378,0.290126,-3.405281,2.359424,8.874632,6.132773,0.876395,-5.283851,3.774615,7.683556,-5.991810,6.956268,9.382713,-6.113465,0.631937,9.484522,-8.254748,0.574833,-3.012370,1.226889,-9.143261,3.617578,8.345711,-7.091986,-4.017806,9.843615,1.333729,-9.870791,-5.274146,0.603899,-0.816845,8.298399,9.374284,1.889273,6.785334,-6.691420,-9.127542,2.562558,9.913435,-2.974478,8.073252,-1.544843,-7.658519,0.726673,-2.774855,3.559680,5.715080,0.797511,8.404682,9.343043,5.947222,-4.941071,3.200978,9.494556,-4.327195,3.498097,9.797564,-1.311325,-2.323533,-0.805279,-6.022138,2.877345,-0.629987,7.861156,-1.866809,-7.672354,-5.933491,6.369285,-4.216960,-4.326671,-4.241065,-6.719777,0.566192,5.109976,6.340260,-6.683646,0.955760,9.220523,-7.460946,-1.369804,7.685577,-9.047488,7.118776,-7.787384,-1.756040,-9.458760,-6.066967,8.387647,4.105596,5.577296,-9.629748,3.546535,8.304179,-4.569022,4.570829,-6.060468,4.929547,-9.258726,-1.431587,3.050372,0.286452,6.662716,-0.635637,2.842609,-5.279387,-5.998909,6.126673,-4.941751,6.004837,-7.293934,1.270264,3.634140,-7.020112,-5.470213,-3.405257,8.978349,0.095962,5.730933,5.184973,-5.289789,0.687370,0.869779,-4.307076,-6.125184,-5.470055,-1.354655,2.766332,-4.021749,2.244399,9.127555,-9.986327,0.249722,3.565787,-1.848708,8.274459,-7.206922,2.624783,6.453441,-5.458659,1.025904,9.482659,-8.995706,-2.009310,-0.303707,1.720212,1.100776,-5.148946,-9.608214,-3.650655,4.629916,1.838544,-0.997766,6.311000,-3.242042,7.845529,-9.836642,7.466450,-3.394317,1.552120,5.689951,-0.175848,7.303005,0.682693,-8.349998,-9.451609,5.354981,-6.888581,-3.246901,-6.798698,0.685793,3.045132,-0.059722,-5.915993,-0.187546,2.357253,6.438744,-0.949757,-2.301017,-2.163039,7.476748,-9.199778,-4.514277,4.320713,-9.788018,9.535782,1.433549,7.975608,2.859058,-2.361948,-9.609330,8.365724,1.894571,-9.739748,0.812055,0.846668,9.724720,2.730450,-9.410736,-1.654385,-1.144859,-6.130659,-2.846758,6.776447,4.412521,4.737453,1.418637,9.240098,4.912098,6.238311,-4.068983,7.296796,-0.304368,1.738280,1.787920,-6.449964], dtype = "float64")#candidate|3566|(234,)|const|float64
call_3563 = relay.TupleGetItem(func_1773_call(relay.reshape(var_3564.astype('float32'), [77,]), relay.reshape(const_3565.astype('float32'), [154,]), relay.reshape(const_3566.astype('float64'), [234,]), ), 3)
call_3567 = relay.TupleGetItem(func_1777_call(relay.reshape(var_3564.astype('float32'), [77,]), relay.reshape(const_3565.astype('float32'), [154,]), relay.reshape(const_3566.astype('float64'), [234,]), ), 3)
func_1571_call = mod.get_global_var('func_1571')
func_1573_call = mutated_mod.get_global_var('func_1573')
call_3574 = relay.TupleGetItem(func_1571_call(), 2)
call_3575 = relay.TupleGetItem(func_1573_call(), 2)
const_3577 = relay.const([[-2.901487,3.538827,-9.030094,7.650285,-8.900952,-2.952432,-3.961908,-4.036508,3.501988,-9.806760,5.099826,0.894489,5.134996,8.702983,-3.607464,8.963404,5.684736,5.133543,-8.158829,-0.434405,6.039250,3.652320,-9.596503,5.094498,5.950261,3.289714,-1.532552,1.848545,-1.637735,4.042664,1.428989,6.980509,-3.501554,-3.575574,0.599494,4.347117,7.676359,-8.972109,6.324983,0.827831,-5.524945,8.033287,-4.375285,-2.098120,7.244753,3.613638,-2.537986,7.584715,-8.597086,-4.241440,2.215272,-1.162646,-6.857580,-8.271371,-3.057944,5.516561,-9.729033,1.002074,3.664292,9.341382,7.945776,8.680232,-2.742811,-9.177328,-0.307843,-3.823680,2.316998,5.186712,-3.180240,4.858737,6.217370,4.379886,4.882918,-9.854051,-5.615923,-6.858665,9.461668],[-1.965378,-9.991271,-1.585039,7.225638,-6.650665,2.181967,-9.355303,-3.061701,-2.685071,-9.616872,8.334232,-9.321641,-4.076930,-0.735524,-7.371095,-8.645479,8.870545,-5.803413,-9.820487,-0.784141,-4.514280,-9.297883,1.666542,-6.682289,-6.633889,6.450790,-8.661232,-9.466841,9.071419,4.627921,-8.674972,-3.179663,1.446596,0.948726,-4.479309,-7.119101,7.836635,6.767154,4.434689,-7.334237,1.626504,-1.560630,0.178218,-3.672101,0.589440,-5.013740,-6.479873,2.831535,0.658504,4.729621,-6.291163,-5.206694,-9.192103,0.120639,8.529429,3.469098,6.114064,6.991709,-1.406412,9.169518,3.009668,7.294294,-9.617411,4.909201,2.862774,4.796526,8.882425,0.740325,-6.684194,6.319176,-9.780951,-0.513562,-0.327778,-2.218376,9.593564,-2.660305,-2.228224],[-1.949539,-0.108437,-1.007221,-9.230783,-4.385932,-9.212156,4.183675,-7.694664,-3.146126,-7.368960,-5.537404,-4.525649,5.750571,0.609630,9.074492,-9.779585,-8.505233,3.729737,-1.463555,7.466411,4.733727,8.744479,-3.194845,-3.969133,-8.517913,3.427318,9.941244,-8.453561,8.856628,6.736864,9.568541,2.145838,-2.778687,-2.215534,-5.664175,8.230646,7.555530,1.354027,-1.814809,0.092325,-7.114694,-8.975855,-1.937249,-1.217070,-4.406968,-1.679013,4.216378,3.413943,0.822802,1.322603,0.268841,7.080490,3.675728,-5.209632,-6.073389,-6.111250,-3.625892,6.575057,8.565228,4.761294,7.346502,4.704025,5.085578,-0.644663,8.056925,-1.533547,9.301952,6.783917,-5.771083,-5.429249,9.001473,8.861622,0.464320,4.563508,3.329246,-0.485843,-4.577862],[6.974913,3.427651,-3.614474,6.694742,8.453276,0.332022,4.487114,7.403200,-8.498368,4.931018,-5.490063,-1.136597,4.162173,-1.689235,-9.729513,-2.093538,-7.407381,-0.247997,-6.945072,-8.663813,-0.307866,-0.524941,8.548959,3.924982,5.838006,-4.878736,-4.586260,6.559006,-6.544583,6.413306,-4.034803,-6.091606,0.874837,-2.242486,4.573067,-2.128933,-9.757852,6.015202,-1.856815,1.425383,2.491732,5.907806,7.865110,-8.574365,1.470387,-3.840829,8.905495,-9.425590,6.071171,-6.108378,8.745601,-7.974295,7.164965,-3.219832,2.302283,4.998946,5.778881,-6.225822,3.991217,-5.306129,-6.726556,6.267715,0.299997,7.642586,-7.283312,0.059149,-5.981205,4.780828,-9.354650,5.238066,7.330839,-3.341977,4.666017,3.296772,4.061378,7.432094,3.054189],[6.688475,2.513374,1.677756,-4.353176,2.661323,5.773865,6.893970,-3.399876,4.735908,9.846435,-2.505237,-6.592368,-5.280951,2.534248,0.413596,-4.362371,-0.335914,2.353720,3.141504,-6.106187,-3.976086,2.629053,0.160543,-9.583286,6.363000,2.122809,8.167742,-0.685058,0.808922,5.971477,-3.506532,-5.427100,5.578531,-0.129509,7.185497,-4.861587,-3.786337,3.002043,2.847176,-9.681368,-1.164450,8.916296,2.359224,4.614452,3.077305,-8.749696,-3.863892,-0.994071,-6.472496,-7.918159,-7.965666,-2.066295,-8.630953,-9.283202,7.532869,-4.549404,-8.079035,3.440522,0.678714,3.427882,-2.472144,-0.039403,-1.107083,-9.261731,-3.206889,-0.918082,4.190877,6.168264,2.830452,-0.946775,5.799717,-9.663500,-2.033365,9.946296,-1.357372,-9.894233,-2.947083],[3.874216,-4.121338,-0.431105,-8.876538,3.615869,8.319537,3.325030,-1.935608,8.356095,-1.239480,-2.780942,-5.352963,9.352338,-6.359784,3.069932,-1.076416,1.305508,-0.674257,1.529651,-4.713954,4.548302,-6.145384,-8.650653,-2.220099,-0.108409,7.371881,1.155700,-6.947526,-5.687532,-6.189327,-2.871123,-3.607866,0.383886,5.302555,7.588404,3.763086,1.617950,4.980910,6.461261,9.336381,3.277114,-6.180777,-8.825319,9.210082,7.174956,-0.716436,-0.299917,0.391972,-2.741614,6.756431,-0.634105,-8.233333,-6.246736,-6.301637,8.319987,1.393976,-7.155211,7.554466,-0.186652,-0.041305,-8.283795,4.364281,3.822781,8.937798,3.394724,-3.020494,3.241889,5.005454,-8.784852,1.299125,-6.010100,-7.990283,-4.884157,9.011016,-2.182155,-4.761637,3.728184],[-4.294771,-6.962316,-6.455839,-7.955627,-5.385367,5.304989,1.640164,1.465388,1.423562,6.242745,-2.168739,7.697272,-8.908014,9.437876,-6.190163,9.697564,-6.672213,-0.018558,7.331302,9.117668,2.286532,-0.695728,-5.810769,4.221342,6.023908,-0.078852,4.244128,7.730217,8.080589,-2.122406,0.988679,-7.124357,-7.905937,-4.238570,4.634370,2.496918,-9.729517,2.625025,2.837192,-8.173053,8.398479,-7.924362,-7.749468,0.363991,3.184174,-5.625014,3.708108,-0.570206,7.779016,0.338992,-6.686705,3.684542,-2.217983,4.145581,-2.536361,-3.116885,-2.016966,-0.909781,5.299157,4.324856,4.153172,6.753520,-9.263604,-8.110749,7.993822,4.666147,-0.744141,-6.293866,6.451755,-3.670864,-9.864271,-7.532105,-9.662606,2.759718,-7.642096,-0.900602,-7.190702],[-9.896687,7.308487,8.825659,-1.874806,-2.079001,9.272395,-2.585816,-2.979035,-6.883596,1.293695,-0.853237,3.654646,1.813315,-7.202120,-4.271363,-3.707829,2.898814,4.060690,-9.124022,6.369443,1.305885,0.978893,-5.938624,-1.205559,-7.049473,0.898468,9.170536,6.058615,-1.419733,-9.214584,-1.029497,6.438206,-3.401276,-1.509539,-7.657899,5.715408,3.628804,2.864699,3.118711,-2.099985,-3.204262,-4.460723,9.118026,-8.536946,7.958295,-5.341091,4.072449,2.375530,-3.034600,-0.517004,-2.259657,-6.354123,6.968791,4.086568,-3.100214,-9.425187,6.862569,-8.669770,-4.102461,-1.741589,-9.968407,-0.529864,-2.590625,9.924547,9.239363,9.276888,-2.982997,9.851602,-3.906959,-1.230952,6.148673,6.436844,7.933910,9.452015,-0.821682,6.577703,-8.691469],[9.317079,2.000204,5.250847,-9.994090,-4.717148,5.039118,-2.380476,-7.831431,-0.231988,-2.154121,-1.318666,5.041109,8.271501,2.292341,-9.280956,-6.151394,-6.384636,3.346380,9.307177,7.666579,-7.528810,1.299663,-8.447249,3.289944,2.094286,-8.274849,7.828376,8.436450,3.433503,4.703585,-2.169288,6.646119,5.939065,9.370676,3.924889,3.856409,4.085877,-0.496877,-1.744830,-4.587554,0.737097,-9.409001,-6.099804,-0.504205,-8.331348,-5.058959,4.463177,-3.690649,-5.758078,0.005121,-3.742207,5.528307,-8.077766,0.907396,5.109094,-9.815324,-9.111295,9.542963,1.428033,-6.351552,0.877788,-4.332310,4.737020,7.495392,-1.676114,9.711162,6.509507,-8.409452,-4.641525,1.938807,1.423869,0.862334,-2.133282,9.941591,-1.317794,0.841534,-7.864397],[-6.481113,-8.239304,3.228409,2.177171,9.005457,3.766925,-6.752182,0.702319,1.016930,4.914408,-8.538376,6.910584,1.026631,-2.371192,6.508991,7.427817,-9.976363,3.450304,-3.810691,-2.864871,-1.478327,-6.212096,6.335798,-3.007261,-2.105261,7.762519,6.861059,-8.435322,-1.831338,2.838054,7.438203,-9.371819,3.030122,6.840053,-1.980807,1.333367,2.222548,4.175337,-2.929498,2.093801,0.453944,7.551978,4.490799,-1.798095,-4.364876,2.390459,-7.964768,8.951321,-2.291816,0.348165,-1.126643,1.299668,-2.365543,3.926131,-4.639292,-4.771930,5.858982,-7.461505,0.496060,4.266150,-2.949581,-9.977221,-8.654596,-2.419037,-9.236677,0.420346,6.658121,3.783553,1.682338,-8.807514,0.933052,6.826481,-1.743863,-3.470283,-0.556979,-7.897500,-2.525434],[4.710142,-2.432934,4.442341,-4.638680,-4.847331,2.111407,6.647754,-5.701739,-6.951757,-7.656239,-6.497097,5.300990,1.132648,-6.923872,6.777927,-1.558888,5.108375,-6.187931,9.278096,8.690112,-8.789431,7.904991,6.725254,1.944501,-8.434337,-2.512131,7.698952,9.709618,8.943879,-5.807230,-0.433940,-8.516603,8.435261,4.745112,2.653139,-7.969048,3.762148,6.907731,1.027908,0.226912,1.189998,9.076406,8.359902,3.449885,-0.196943,0.947747,-3.239586,0.484944,4.414946,-1.522995,3.212945,-3.801434,6.992475,-6.973433,5.628089,-1.631846,6.025961,2.712245,-6.145411,4.234148,-5.375263,5.473365,-3.124098,-1.334809,2.773761,-8.294391,-5.019106,-2.922022,2.218977,-2.072536,-2.421182,2.145782,-9.506993,-3.245838,9.399470,-8.458066,1.969926],[-4.790522,-1.851274,5.883290,9.663904,-1.560137,-8.511261,3.426909,4.911908,-0.949679,-1.961768,8.001128,-9.766649,2.182276,-0.094408,5.479390,-7.449589,8.635812,1.834227,-6.845557,6.654396,-9.166411,9.094717,9.920374,9.543741,-3.243113,2.053366,4.794151,-6.415558,3.161730,-3.151389,-7.830143,-6.675862,0.333949,-5.179578,-3.113732,-5.887273,4.140510,3.080879,6.128986,6.815828,-7.410152,3.904729,-8.021943,7.447059,-9.575740,2.273756,-7.229555,4.724750,6.740718,9.385969,1.953371,-9.646130,-5.672127,5.245811,-4.171161,9.692948,6.367739,-5.800196,-8.230910,0.236068,6.974514,1.272524,-3.212725,9.011159,-7.344063,9.730310,4.045968,9.233290,3.336181,6.153435,0.460749,5.320185,3.937091,-6.007688,0.228867,8.825415,-4.211184],[-5.774397,1.583056,-9.729379,-5.727842,6.969854,2.637388,4.733199,7.663920,7.165368,-6.479285,6.305194,-7.966762,8.643733,5.814751,2.289325,-8.271235,-5.327472,3.599012,3.068839,-5.773531,3.940475,9.632009,4.676306,7.112767,0.071165,9.469905,-2.298278,0.955477,1.503092,-5.835615,-9.824341,-5.943873,-6.409855,-0.283345,1.837980,-4.611489,-1.878875,-9.412836,-2.299165,-3.052728,7.426802,-2.314152,-5.221983,2.909304,-5.607161,-6.937472,-3.459409,7.431932,-9.368960,5.078140,-3.544275,8.845944,9.540854,-6.555428,8.333652,-0.155601,-3.107316,-5.404234,-3.653104,-8.361039,9.624120,5.142348,5.766479,-4.024208,-8.485539,-6.173629,3.734647,-6.418373,7.401398,-5.028520,5.372547,5.187756,9.272149,-6.081305,1.933663,-4.913277,8.546893],[0.549361,-9.508846,8.701954,9.710114,-9.965601,9.385428,8.234933,6.458969,9.291001,-7.033416,3.960520,5.931095,8.309278,-5.182735,7.160647,-3.707991,1.604839,2.125848,8.031289,-1.212619,3.490915,-0.661221,-1.349023,3.089680,1.774983,-8.801970,1.611027,-8.882865,-0.878451,4.407557,9.778780,-8.646632,-7.956963,6.898770,-9.018532,1.716075,6.211730,8.569311,-8.942233,7.479443,-1.354199,-1.160083,2.244421,6.046817,0.041503,-2.002755,-7.062433,4.324062,-7.967055,-0.391917,-3.085413,-0.505491,-0.905022,8.732716,-0.531239,-0.549736,-7.303927,2.686493,7.359668,-4.599477,6.905423,1.322983,3.780100,-5.726660,2.168972,6.977934,5.883616,4.232136,6.207742,-8.944598,-0.426666,-9.837511,5.010327,-4.937147,-9.213625,1.129727,9.019211]], dtype = "float32")#candidate|3577|(14, 77)|const|float32
bop_3578 = relay.minimum(var_3564.astype('int8'), const_3577.astype('int8')) # shape=(14, 77)
bop_3581 = relay.multiply(const_3577.astype('float32'), var_3564.astype('float32')) # shape=(14, 77)
uop_3635 = relay.log(bop_3578.astype('float32')) # shape=(14, 77)
uop_3639 = relay.sin(uop_3635.astype('float64')) # shape=(14, 77)
bop_3641 = relay.maximum(uop_3635.astype('uint8'), relay.reshape(const_3577.astype('uint8'), relay.shape_of(uop_3635))) # shape=(14, 77)
func_1552_call = mod.get_global_var('func_1552')
func_1555_call = mutated_mod.get_global_var('func_1555')
call_3645 = relay.TupleGetItem(func_1552_call(relay.reshape(const_3566.astype('float64'), [234,])), 1)
call_3646 = relay.TupleGetItem(func_1555_call(relay.reshape(const_3566.astype('float64'), [234,])), 1)
uop_3653 = relay.asinh(uop_3639.astype('float64')) # shape=(14, 77)
output = relay.Tuple([call_3561,call_3563,const_3565,const_3566,call_3574,bop_3581,bop_3641,call_3645,uop_3653,])
output2 = relay.Tuple([call_3562,call_3567,const_3565,const_3566,call_3575,bop_3581,bop_3641,call_3646,uop_3653,])
func_3656 = relay.Function([var_3564,], output)
mod['func_3656'] = func_3656
mod = relay.transform.InferType()(mod)
mutated_mod['func_3656'] = func_3656
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3657 = relay.var("var_3657", dtype = "float32", shape = (1, 77))#candidate|3657|(1, 77)|var|float32
func_3656_call = mutated_mod.get_global_var('func_3656')
call_3658 = func_3656_call(var_3657)
output = call_3658
func_3659 = relay.Function([var_3657], output)
mutated_mod['func_3659'] = func_3659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_3688 = relay.TupleGetItem(func_1334_call(), 0)
call_3689 = relay.TupleGetItem(func_1336_call(), 0)
output = call_3688
output2 = call_3689
func_3706 = relay.Function([], output)
mod['func_3706'] = func_3706
mod = relay.transform.InferType()(mod)
output = func_3706()
func_3707 = relay.Function([], output)
mutated_mod['func_3707'] = func_3707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_3767 = func_2364_call()
call_3768 = func_2364_call()
output = call_3767
output2 = call_3768
func_3779 = relay.Function([], output)
mod['func_3779'] = func_3779
mod = relay.transform.InferType()(mod)
mutated_mod['func_3779'] = func_3779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mutated_mod.get_global_var('func_3779')
call_3780 = func_3779_call()
output = call_3780
func_3781 = relay.Function([], output)
mutated_mod['func_3781'] = func_3781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_3940 = relay.TupleGetItem(func_2454_call(), 1)
call_3941 = relay.TupleGetItem(func_2456_call(), 1)
output = call_3940
output2 = call_3941
func_3970 = relay.Function([], output)
mod['func_3970'] = func_3970
mod = relay.transform.InferType()(mod)
output = func_3970()
func_3971 = relay.Function([], output)
mutated_mod['func_3971'] = func_3971
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3988 = relay.var("var_3988", dtype = "float32", shape = (8, 1, 1))#candidate|3988|(8, 1, 1)|var|float32
uop_3989 = relay.asinh(var_3988.astype('float32')) # shape=(8, 1, 1)
output = uop_3989
output2 = uop_3989
func_3993 = relay.Function([var_3988,], output)
mod['func_3993'] = func_3993
mod = relay.transform.InferType()(mod)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3994 = relay.var("var_3994", dtype = "float32", shape = (8, 1, 1))#candidate|3994|(8, 1, 1)|var|float32
func_3993_call = mutated_mod.get_global_var('func_3993')
call_3995 = func_3993_call(var_3994)
output = call_3995
func_3996 = relay.Function([var_3994], output)
mutated_mod['func_3996'] = func_3996
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_4191 = relay.TupleGetItem(func_1488_call(), 1)
call_4192 = relay.TupleGetItem(func_1489_call(), 1)
output = relay.Tuple([call_4191,])
output2 = relay.Tuple([call_4192,])
func_4195 = relay.Function([], output)
mod['func_4195'] = func_4195
mod = relay.transform.InferType()(mod)
mutated_mod['func_4195'] = func_4195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4195_call = mutated_mod.get_global_var('func_4195')
call_4196 = func_4195_call()
output = call_4196
func_4197 = relay.Function([], output)
mutated_mod['func_4197'] = func_4197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mod.get_global_var('func_1013')
func_1015_call = mutated_mod.get_global_var('func_1015')
call_4275 = func_1013_call()
call_4276 = func_1013_call()
func_741_call = mod.get_global_var('func_741')
func_742_call = mutated_mod.get_global_var('func_742')
call_4289 = func_741_call()
call_4290 = func_741_call()
output = relay.Tuple([call_4275,call_4289,])
output2 = relay.Tuple([call_4276,call_4290,])
func_4298 = relay.Function([], output)
mod['func_4298'] = func_4298
mod = relay.transform.InferType()(mod)
output = func_4298()
func_4299 = relay.Function([], output)
mutated_mod['func_4299'] = func_4299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_4309 = func_2364_call()
call_4310 = func_2364_call()
output = relay.Tuple([call_4309,])
output2 = relay.Tuple([call_4310,])
func_4313 = relay.Function([], output)
mod['func_4313'] = func_4313
mod = relay.transform.InferType()(mod)
output = func_4313()
func_4314 = relay.Function([], output)
mutated_mod['func_4314'] = func_4314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mod.get_global_var('func_1013')
func_1015_call = mutated_mod.get_global_var('func_1015')
call_4382 = func_1013_call()
call_4383 = func_1013_call()
func_2621_call = mod.get_global_var('func_2621')
func_2624_call = mutated_mod.get_global_var('func_2624')
const_4388 = relay.const([9.656296,-8.754363,-9.750407,7.694870,2.344699,8.205775,8.603021,-5.768155,-7.396907,-4.066339,-3.881892,3.718821,9.845949,7.612307,-5.339975,-2.755065,4.529195,7.307089,5.237283,4.509257,-2.675639,-3.409303,2.871412,-2.521899,-7.392506,1.594785,-9.793767,-1.190210,9.625955,5.702724,5.338861,5.424762,-0.151540,-4.093595,-8.047620,-1.134424,9.887134,-6.424306,-0.384429,-9.930925,8.671771,7.686533,7.801822,-9.257177,0.039310,-7.142834,7.823780,7.491293,6.176270,6.971464,0.210247,-0.126233,-6.169443,-0.814015,6.359327,8.535219,-7.801540,8.347342,-9.319177,-5.761046,1.227858,0.265542,4.435165,-4.749231,-6.831338,-4.718714,9.212919,-4.768408,0.673491,-7.061009,-4.499771,7.797388,-5.545220,-8.366208,-0.274764,-6.458465,7.025263,8.255765,6.652785,7.271308,4.887595,6.964613,-2.802137,0.999799,-1.758519,4.630941,9.189999,9.312013,6.259482,5.003750,8.707796,2.720358,8.278692,2.296967,-5.778529,-4.626167,-9.698345,-1.547413,-7.073210,-5.024015,-4.746483,8.184973,-3.530084,5.393688,-5.139604,-8.984331,0.618487,-5.735818,-0.148897,0.354107,5.519533,-3.581579,5.767782,-5.720597,-3.525214,7.380193,-2.805352,5.442074,1.698088,-3.772644,4.052037,6.307589,-3.624314,2.911882,2.421621,6.948539,-9.260227,-2.431093,6.387674,9.077422,8.038797,-2.887433,9.992758,2.753422,-8.074434,-0.319224,-8.605742,-1.262682,-7.868354,9.888585,-7.084505,-3.248702,-0.699460,2.841627,9.202312,-1.528647,2.375007,8.120613,-9.469746,4.048562,-1.220876,-9.372943,-5.552503,-2.961689,-8.150036,-3.416690,-6.926778,6.954422,-2.112744,-6.652294,-6.145904,-3.624113,0.315951,-6.194687,-9.720556,7.060582,-3.692539,9.650146,-8.160397,4.313223,2.540997,-3.491903,-5.238597,5.360373,-1.144026,-1.394686,-6.814773,-4.355731,-2.199373,3.750664,-4.427648,-0.391151,-1.159008,3.918807,9.552030,7.102651,0.599345,-5.515660,9.015125,-8.894984,-1.709147,-0.301538,6.219236,-1.962199,-6.611330,1.504854,-7.030354,7.241382,8.414694,-6.084405,6.776949,-3.120146,0.774992,-9.123348,-8.068818,-2.014418,0.753361,7.161592,3.037816,7.009081,5.696718,-9.378384,-4.963996,-1.023204,9.084049,-6.253591,-2.656475,0.210694,5.185015,-3.254232,-2.396661,-8.271077,-3.517244,-3.732740,-7.079292,8.291009,-8.042372,7.329244,5.257493,4.423107,-6.410384,6.788791,-8.432025,-1.013922], dtype = "float64")#candidate|4388|(234,)|const|float64
var_4389 = relay.var("var_4389", dtype = "float32", shape = (77,))#candidate|4389|(77,)|var|float32
call_4387 = relay.TupleGetItem(func_2621_call(relay.reshape(const_4388.astype('float64'), [234,]), relay.reshape(var_4389.astype('float32'), [11, 7]), ), 6)
call_4390 = relay.TupleGetItem(func_2624_call(relay.reshape(const_4388.astype('float64'), [234,]), relay.reshape(var_4389.astype('float32'), [11, 7]), ), 6)
output = relay.Tuple([call_4382,call_4387,const_4388,var_4389,])
output2 = relay.Tuple([call_4383,call_4390,const_4388,var_4389,])
func_4391 = relay.Function([var_4389,], output)
mod['func_4391'] = func_4391
mod = relay.transform.InferType()(mod)
var_4392 = relay.var("var_4392", dtype = "float32", shape = (77,))#candidate|4392|(77,)|var|float32
output = func_4391(var_4392)
func_4393 = relay.Function([var_4392], output)
mutated_mod['func_4393'] = func_4393
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4445 = relay.var("var_4445", dtype = "float32", shape = (12, 16, 12))#candidate|4445|(12, 16, 12)|var|float32
const_4446 = relay.const([[[4.490883,5.083161,-8.494758,3.921531,6.693765,-3.066918,-4.768575,0.071747,-5.844999,-0.873748,8.670783,6.312777],[-3.815858,-5.047614,9.596421,-5.229804,-0.814309,7.887569,-9.366848,-4.251518,-2.357590,1.985633,-6.278952,-0.175705],[-0.431537,1.554509,3.761669,9.239166,-3.811314,-6.398062,5.790136,-8.784642,-1.573502,-0.882920,8.220628,5.228526],[6.244796,-1.273236,4.025992,-2.393428,3.050879,-1.757271,4.372583,-9.217039,5.824135,7.689397,5.818380,-1.507963],[3.887491,8.264993,2.071213,-4.642151,7.288832,-4.646030,4.510246,3.211140,4.119134,5.571367,2.845998,-0.695717],[5.468530,-2.849330,-3.792634,-1.954019,4.741110,-5.807396,-5.765373,-2.066959,6.503341,2.772351,2.259004,-4.176849],[-2.004971,1.124932,0.933572,-7.753384,-7.154431,-8.466844,1.238281,-2.528444,-7.548808,-1.927327,-6.798182,-4.896630],[8.660962,-1.427278,-8.806976,1.444021,3.914407,2.922546,4.312107,1.513657,-2.594979,-0.510154,-0.195993,-8.703487],[8.485532,-4.962788,7.950170,4.287992,-8.312904,-4.415261,-9.631677,0.793370,-4.577041,5.368987,-2.656253,6.152194],[-3.847565,-5.471782,5.129697,1.495421,5.821201,-0.490676,-8.191414,-9.138953,2.768026,-3.625079,-5.667183,2.129788],[-3.541237,-8.066364,8.270112,3.577003,3.840427,4.308945,-2.295038,0.190009,-9.685042,7.124858,-0.113169,1.044449],[-8.500072,6.125571,2.835149,9.684035,5.365646,-7.191978,-3.873996,-6.294755,3.949704,-8.787383,-8.903021,-5.925202],[2.784823,-1.420443,7.331330,4.030737,3.976200,-6.046118,-5.252241,-6.773879,-2.855672,-3.418748,-6.417699,-0.946308],[-2.644582,0.107375,5.564088,0.215046,9.845871,-5.222080,6.603215,-7.317771,-3.552184,9.703471,3.588202,0.354158],[-4.644381,-1.419634,-0.565232,3.318003,6.567576,-5.242644,-4.224546,2.580019,4.937043,-6.169640,3.900002,1.854711],[7.917989,-8.435060,-8.812919,-7.262495,-7.499749,1.363132,-2.958525,9.643593,6.897886,-6.900970,-5.528166,-9.539473]],[[3.498185,-3.627314,8.780317,-6.942034,7.525966,8.096494,-2.048518,-9.789822,-1.959744,-9.507012,-1.793174,-7.496937],[1.073349,0.568854,-5.789780,2.817247,-7.288092,0.136471,6.529425,2.545627,-1.574860,-9.461050,-9.370426,7.675270],[-7.670777,5.833560,-3.056109,-8.640251,-9.484521,8.595964,4.020880,-7.793088,-1.315245,-7.475080,-4.827649,-3.646402],[-6.401958,3.196707,-8.316563,-0.962167,-1.659335,0.623308,0.571805,-8.105912,-9.338188,4.274940,-0.828876,2.946661],[0.112207,-2.899863,1.109438,-8.487848,2.331401,0.066279,7.792033,-5.359071,4.609913,-0.746519,-6.417205,7.663705],[-2.965404,-2.952164,-2.499454,5.983693,9.922709,5.489534,5.463379,4.913228,-1.852932,-2.625911,-0.981560,0.898201],[-4.973491,-4.734747,4.793323,3.372510,-5.920361,-2.732585,-6.744472,-2.419252,-3.309519,-8.259341,-2.704935,-1.292137],[-6.337220,-5.659947,-1.771444,0.331859,4.571961,6.424703,1.693965,-7.388266,-9.000212,-2.493607,-5.488881,5.129620],[8.680476,-0.116466,8.128484,-9.032489,3.432178,-3.237291,-0.446550,8.416275,5.359833,-1.846679,6.587433,0.630848],[-8.329344,-0.221247,-6.696224,1.536024,-7.523332,0.132427,-7.684368,9.172643,-9.225898,1.089265,3.920855,-0.772539],[0.817276,0.757851,7.911254,2.657496,8.719105,3.801127,1.243028,9.835640,-1.350336,9.997605,-0.022745,8.949412],[-6.120312,8.379339,7.887078,-5.106826,2.817161,0.622541,-5.001183,-9.165909,0.569559,-6.151528,-1.209646,-3.689419],[-2.472613,2.600843,-5.294452,-8.603902,-8.110890,9.221796,4.951992,-2.404146,2.039247,-7.863566,-7.022466,2.955278],[-8.463352,-5.572262,3.045278,1.441347,-4.812098,-7.298897,6.884757,2.857494,6.643867,8.110988,6.387516,0.802193],[-9.105747,-8.755723,-3.660659,-8.196943,0.051882,6.555676,5.273108,9.382513,0.435168,-6.100258,-5.483405,-9.300622],[-4.990060,-6.928151,-6.368755,7.920781,8.725177,1.693559,6.034902,-8.798884,6.733122,-5.572456,9.807895,-2.841504]],[[0.576442,3.070971,6.907858,3.518997,-4.387970,2.832302,5.215322,2.840066,-5.105117,-5.043950,-9.470899,3.640036],[-0.729540,-1.009869,0.016677,2.589949,1.481713,-9.718645,-5.547803,0.249391,1.378170,1.891540,9.181624,-8.997777],[-1.915621,1.889276,2.803050,-8.932137,-8.491481,7.027813,0.287516,0.894919,-4.777490,6.911593,5.795008,4.578982],[1.721082,-4.324783,5.217534,9.138432,8.695876,-8.585799,2.912131,6.099359,3.084909,8.829751,8.290326,7.086628],[-6.109461,-7.651549,8.261109,-4.824558,4.380201,3.106632,9.252968,-2.067212,-3.300004,-1.098613,8.631584,7.009673],[-0.041227,4.729228,7.645857,4.101491,-6.524140,-8.182518,6.242036,-5.717803,8.495240,3.266656,-0.083835,1.044406],[-6.295558,-1.368420,1.608121,-3.651619,-5.001279,1.410938,0.031693,0.799958,8.601693,3.389687,9.019284,4.363779],[-2.718376,2.106454,-0.813290,8.646178,-6.985995,-7.775195,2.783415,-5.993613,-2.121574,-4.281700,-9.164663,2.451882],[0.258690,2.508480,9.607656,5.890387,7.945326,-0.997082,5.069053,0.990581,-5.879063,-6.844260,-3.439808,7.256551],[-6.073256,-2.770997,-3.958963,-2.818472,0.734148,-2.665411,-6.000216,-8.444022,-6.208094,1.722603,-9.210338,-1.391065],[-4.789687,-4.552837,6.651393,-8.474820,6.818708,-9.451392,-8.565844,5.345095,-8.603310,-8.653202,9.829793,4.325393],[-1.731820,-3.262141,6.921245,1.187551,3.603163,-2.076236,6.770027,-9.108456,-1.405487,-7.687257,-8.394375,-0.063620],[5.888477,4.616820,5.605046,6.429577,-4.553430,-7.158374,-2.724110,4.097790,2.960488,-2.814667,-6.738579,-9.304718],[0.853677,-3.269095,-3.482340,9.696614,0.740502,7.065887,4.098597,-7.187295,-1.396973,9.366906,-9.398293,-8.969834],[-5.225342,1.555455,3.568444,2.892869,-0.897549,-2.462864,-4.903706,1.280355,4.215751,-1.507949,4.593354,-2.922088],[5.478004,-5.651011,-1.427641,-9.548497,0.013692,-5.938096,2.039162,3.698585,8.640822,-1.609904,6.416695,9.224642]],[[-1.925475,9.080960,5.434230,8.385969,3.444220,-5.682888,-4.862444,5.408020,-7.031044,4.827458,5.037529,-4.823801],[-0.906473,6.540027,-8.145543,-3.538206,-6.849187,-5.416762,6.845054,0.500476,9.815130,4.188140,-9.185783,6.102297],[-7.905201,-3.953765,5.925689,-5.515069,4.433309,-9.744045,-7.485662,1.443394,-6.596603,-4.087883,0.984809,2.053676],[-3.194643,5.840052,8.179397,9.114480,5.221869,9.606089,-7.664370,-9.735393,6.529089,6.043566,-8.270800,8.983594],[-7.752282,-4.797257,3.875380,-9.667819,-1.826983,-9.564397,-2.813417,0.058574,4.114844,9.369056,-8.929968,6.346093],[-1.460956,-3.869037,4.765710,1.184177,3.046033,-8.347528,2.559977,-0.795712,-3.291037,3.381595,9.954990,-1.200318],[-6.310342,-1.578629,2.856188,-5.127496,8.324652,-1.791660,-2.153436,-7.045311,-5.698360,-0.427334,-3.759061,3.720766],[6.620406,0.750535,-3.759990,9.590495,0.043548,3.454079,-8.027055,-9.297093,-3.821053,-7.698474,9.968020,6.515453],[0.559009,7.575315,-8.013651,-0.647401,-9.707697,-9.118134,5.707416,1.281284,-7.448451,-2.552180,-2.870463,-0.226802],[0.689738,-5.611385,7.180536,-9.892942,7.129209,-7.068393,1.285029,-5.874074,5.600230,-2.668936,-5.905558,1.466996],[-9.749319,8.448944,8.059739,-8.862620,1.229000,9.090700,-5.472355,1.815987,3.408776,6.875198,7.643188,-7.528328],[7.904519,2.926284,-5.158803,-4.454840,-8.234107,-9.653057,4.005853,8.293571,5.798968,9.842315,-4.507686,9.515888],[2.721320,-9.083253,-3.065105,6.579654,6.814589,-2.742665,2.577183,8.707274,-0.993936,8.227820,-6.855392,-7.161075],[5.869762,7.843367,9.257589,-3.429785,8.090984,7.339642,9.064493,9.576273,8.160535,6.190869,-3.178420,7.635310],[-7.306017,-8.658163,2.547736,-8.266807,7.424953,-0.243418,-3.731537,9.336973,-3.093051,-6.502021,6.086429,-6.412367],[9.839965,3.080387,-3.644764,-1.090364,-9.914988,9.453884,-8.261559,-3.598720,8.715289,-5.001246,5.665513,-5.898966]],[[-4.921013,-5.309944,-6.822978,-5.673253,-4.689334,-8.413701,-6.922190,7.295202,0.843855,-0.854326,-5.055746,0.846021],[-6.170323,2.249907,7.456246,2.087929,-2.524694,5.131814,-6.913217,-2.338371,-9.945885,-0.946803,-8.202596,5.545675],[-4.994393,7.683252,-2.819780,2.674268,-8.667629,3.090109,-5.289553,1.493844,-2.693258,2.269921,-4.801264,3.770524],[-5.357488,-7.222874,1.548160,9.821856,9.662730,-7.991237,6.097027,-3.768380,-2.988749,-7.062747,-4.582796,-5.083122],[-0.154296,-3.191990,8.547358,9.255616,4.455224,-1.651349,3.636811,-7.924488,-5.487876,6.003017,-4.102347,0.755945],[0.784946,9.357914,8.524864,-8.081218,-6.226282,3.084764,-0.263234,5.980054,-4.323109,-0.652403,6.955370,-4.425192],[5.585777,-9.621345,-7.753377,-0.569720,5.373067,8.916945,9.099376,-6.289218,-8.088000,-2.805568,3.055960,-5.480831],[8.644751,1.596353,-9.156886,1.416029,9.005638,3.206833,3.071077,4.732768,-8.607869,-6.765267,-9.662568,4.500379],[-9.949848,2.584977,7.275872,5.103504,-8.950617,-6.117839,-9.615264,-3.127476,2.112148,0.451056,-6.130193,8.283986],[-0.046056,-7.332385,-0.177561,5.051178,4.092959,-7.981911,0.581954,-0.495491,6.709055,-6.637512,-6.691612,8.596315],[-7.547637,-8.545612,-3.997820,0.722066,4.737914,9.120990,6.635727,-7.157533,-2.668249,-4.666367,-0.687346,7.739348],[2.893711,-1.631683,8.608810,7.238189,-1.293246,-1.205274,3.798331,7.537185,7.832191,-4.386521,-2.773533,-8.300105],[-4.151436,-0.982732,5.814392,-6.904566,1.290211,-1.455019,-6.703260,-6.366478,2.167104,2.644533,1.827088,-3.264008],[-7.917176,5.337959,6.452383,0.798537,-6.992900,6.311098,4.006096,-4.616898,-8.259690,1.424319,-5.187393,1.563761],[-2.918970,-4.902242,-8.849385,9.403268,-1.739957,6.492328,-2.339964,7.822045,-8.193547,-0.033189,-2.666468,-4.004686],[0.097191,2.971839,4.300013,6.290075,-0.179497,7.219111,-3.658415,7.961174,-3.818533,7.695438,6.775197,5.102680]],[[8.829225,7.628247,1.222937,-6.580761,-7.691771,-1.534362,-0.480481,4.013632,-8.535746,5.955142,5.849604,3.061708],[0.296179,-2.116685,1.814213,-8.019281,2.759922,-6.113378,6.276726,4.615194,-5.247704,-9.244373,-6.928356,0.648077],[-5.223445,9.509681,5.352429,7.460389,5.240247,7.485233,-5.480291,6.959824,-1.508326,-8.846267,-6.411193,2.597749],[3.154323,-8.946138,2.769044,-5.513071,-7.741280,-9.030886,-6.616702,8.921302,1.295159,-1.182252,-8.278476,-2.219801],[0.574362,3.571031,-8.211462,6.151772,-8.861587,4.325803,9.766121,7.999845,-4.595558,-8.141506,-2.857905,-6.391249],[-6.131269,5.744821,7.278220,6.357701,-3.854895,-8.601638,9.399480,-8.682663,5.304380,-0.086532,-8.997117,1.393457],[4.416660,3.536784,8.489080,0.963778,8.589273,-5.066788,-8.790879,0.308302,-7.025629,-2.509626,4.999405,9.098182],[-1.321508,-3.991234,-2.014115,1.916041,1.872822,6.434490,4.349960,-6.499259,6.521955,6.392303,7.924439,-5.189782],[-5.436178,0.965905,3.123380,2.229503,-2.882061,-2.871317,9.273135,-8.725479,8.690900,6.966574,7.786987,3.967050],[-6.154384,-4.023114,4.904132,-0.080248,1.046520,-1.542571,-6.660448,8.737730,0.308152,0.195225,9.260432,8.813846],[9.020540,6.652471,-4.062284,3.736622,0.287677,-5.139176,-5.933362,6.370691,8.397453,4.682286,0.544612,-3.308273],[-0.304778,3.664456,-6.639068,-3.028759,0.929825,-6.901515,-1.551608,-6.796344,3.496954,3.912166,1.974180,-1.693245],[-2.993085,7.675797,-4.129528,-7.796311,8.241125,-1.181616,-7.678762,-3.140440,8.985408,6.046838,-3.170340,1.021153],[8.611455,-7.017341,9.846295,3.610730,-4.011671,9.500022,-7.918617,1.484795,6.926747,1.144357,1.256383,2.766015],[-8.227731,-3.431944,4.711747,2.858443,-3.042770,7.719886,-6.871007,2.910358,6.931805,2.386760,-6.745302,-3.216496],[-4.574528,2.644432,1.787967,-5.107280,-9.572575,-6.411270,2.858595,-7.401143,6.566997,2.142706,-9.708300,-1.961309]],[[-7.722852,4.019126,9.550703,-1.928541,-9.599013,5.558084,2.260159,2.644030,-4.275370,7.622692,5.773212,-7.702680],[9.880362,-6.545204,-6.436954,-8.867000,-9.765892,-3.381005,2.777000,-4.073481,-0.162347,5.299617,1.531925,2.506689],[-3.122788,4.464325,-9.930290,9.930811,-2.457504,6.410227,-2.391854,2.970315,-2.427193,-8.263345,-5.145503,0.672553],[-8.243749,-0.717207,3.280946,-5.577798,-9.340298,-9.620993,6.655514,2.677099,6.704734,-1.891753,-9.401960,2.571392],[8.154124,-3.519703,-6.465345,0.950781,-5.290381,-4.149099,3.849695,0.027183,4.230149,6.686125,8.908414,-2.934486],[9.587343,4.977608,-7.577931,-4.892491,-3.237810,8.568690,-5.460989,-9.780324,6.672492,3.488141,8.339045,-8.274039],[-4.946436,6.977117,-5.040876,-7.049134,-9.219301,1.559319,-7.411158,8.890831,-7.271612,6.405503,9.129282,9.882098],[4.277072,3.128200,-8.184975,5.307011,1.501448,-0.611850,-5.605854,-7.898979,-3.510922,2.702597,7.315531,-0.884287],[5.348624,2.959981,4.363598,6.022086,7.005479,9.088832,3.213474,-8.767393,1.701352,-4.469516,0.329896,-8.039184],[4.453894,6.247107,-6.892520,-2.009287,5.402507,-0.272122,1.426562,8.986301,0.853631,-6.289973,4.349234,0.365577],[7.711099,-1.735592,-3.243809,5.800789,-5.361110,5.485357,-8.835277,6.119618,2.469302,-2.797337,2.024175,8.300685],[-8.604084,2.932883,-1.336004,-3.538228,7.966106,-9.968556,2.511323,4.529544,-8.523427,5.410424,-5.010771,5.537326],[-7.057359,-2.717426,1.228257,-2.918299,4.397097,-5.994599,4.293265,-4.160808,3.684845,-2.747424,-3.117078,2.545101],[-2.142105,2.239999,6.634856,-3.504461,-0.423870,8.191337,-3.104972,5.769829,-0.459282,2.937327,-9.295824,-9.426757],[3.826864,-8.804877,-3.461049,-7.544248,-3.404059,6.731832,-7.420332,-3.137475,2.866008,9.893127,4.136394,7.341599],[-4.713319,8.321812,-9.856640,-8.241499,7.018800,3.158698,-6.547114,-9.351777,6.704532,-5.560974,-0.249137,-7.329775]],[[1.007218,7.068178,-0.750223,-0.861542,-2.980684,6.243657,6.302320,-0.591711,3.643733,-5.460073,5.105252,-5.164940],[-0.437473,9.476105,8.156438,-2.338342,2.662314,-0.451198,5.374046,-7.908602,-4.486464,-5.949809,7.661618,-9.216828],[6.163767,0.865004,-4.751218,2.238167,-2.547656,3.706880,3.061798,-4.240401,4.610315,-1.265328,6.979891,-0.588286],[2.780220,6.164957,9.094941,3.363047,-3.461372,-6.056327,-4.959001,-0.878714,-7.502038,9.580078,4.734674,-5.567290],[-4.395265,4.154464,3.077588,1.754936,8.486410,6.328556,5.493417,2.531726,8.801611,-9.072553,1.062608,7.933226],[-2.164641,2.330196,-5.731544,-2.312223,0.493960,8.204325,-3.344561,0.369636,4.834597,-3.021820,1.358657,5.323705],[6.023351,-8.374006,-7.580817,-4.066589,-3.113713,-5.900493,3.298165,6.405372,8.742404,3.205489,-3.288804,0.886249],[-0.707769,-1.005270,2.858134,-9.870402,8.166344,0.413354,-9.354301,-1.068250,-2.252679,-3.278697,2.025977,-0.851100],[-8.894373,-9.200306,-0.281395,-0.001940,-2.352743,-0.593641,-4.716640,-9.585635,1.867672,5.441963,-1.459222,2.635231],[1.064517,-0.475479,4.057302,0.851569,8.160675,-2.840755,5.984320,-4.041257,5.392535,9.631596,7.762369,9.428894],[6.390049,4.107921,-6.616424,-1.044408,-5.531990,1.129639,4.270935,7.665576,-1.371363,-0.724503,-6.142045,1.519057],[7.124153,-7.824657,6.566701,-5.544705,-3.903771,-1.427996,-7.124171,-6.968253,2.202783,-6.464902,-3.955427,3.080968],[-9.787172,-8.807955,-7.765516,-1.541200,-1.736781,5.260922,3.918384,9.005321,7.924157,-9.977691,-1.594578,-2.339719],[-6.891909,7.948842,-0.292344,-8.888967,-5.464284,7.861396,-6.173372,4.166654,-5.010288,-5.765335,-6.134316,-9.729783],[2.841139,3.658861,2.774949,-2.183837,-5.850418,9.226781,-2.093438,5.513741,-2.215608,-0.283462,9.685055,-5.012878],[-3.727464,1.177540,-5.064212,-2.028719,-5.701690,4.673688,7.930239,-6.091922,7.849431,-4.210952,7.185880,6.696495]],[[-7.757154,-7.580376,1.214928,-3.435511,-6.640932,-9.013699,7.231932,-4.004704,-3.712252,2.469787,8.477844,3.429495],[3.822873,2.035715,-6.275767,1.568978,-0.609789,-3.279757,-5.479022,0.190221,-5.924575,6.470869,-9.004774,7.834304],[0.116714,-3.797830,-4.311332,-2.172090,7.257785,-9.742530,-0.081137,-5.945088,-0.867045,-8.782829,7.529035,7.427906],[3.563956,6.524954,-9.362094,-0.714911,-3.011473,2.323977,-8.327610,-0.409878,4.219698,1.791239,-3.980755,-2.866130],[-1.601472,7.390552,-9.113329,5.452982,3.304221,4.299548,-5.217017,-2.845337,-4.445985,9.421493,9.461147,-0.945799],[1.326859,-1.966770,8.708247,-7.216718,2.311299,-6.904150,-8.448775,2.290686,-7.414488,4.124311,-6.020460,6.115152],[8.668111,2.707847,2.070630,9.448143,-0.835775,-9.872323,-4.940218,3.077919,6.125545,1.666113,-4.290419,8.503829],[0.023760,7.562917,-1.368072,-5.839988,6.145458,-4.368307,2.260169,5.154885,1.165873,-8.126230,-8.570182,5.227670],[7.498771,1.716275,6.775533,-6.978686,-6.024847,-8.550848,2.394415,-6.940871,6.230202,5.911638,2.429820,-0.026768],[-8.452747,-7.510582,-4.609844,-6.803239,8.859788,5.921937,5.186435,5.638565,9.803877,-2.449686,8.074592,-2.294903],[-6.882107,9.475514,-9.874444,-0.620384,-0.009071,-8.774205,6.642036,-0.957350,-2.544028,8.348398,-5.938297,7.733906],[8.542876,-2.798913,7.687092,8.819049,-8.310555,9.626863,-1.188661,0.871240,-0.111827,4.654443,4.104032,-5.297682],[-7.828058,4.481321,1.304682,-0.133158,-8.726036,3.652602,6.124473,2.728666,3.629847,5.743007,7.935113,1.194570],[-8.661368,4.038932,-1.001416,7.736192,1.852093,3.909906,-6.214472,2.728282,-8.547467,-3.294374,9.225469,0.386512],[-8.206485,-9.100196,-8.887362,6.509755,0.473122,-4.690401,7.012147,-1.467224,-1.833097,7.123929,2.938065,4.296708],[9.114739,-6.523387,-5.237008,3.699843,-3.174415,-3.172135,4.166825,4.448439,-9.109670,2.234476,1.181870,-4.874317]],[[7.316754,-3.027601,5.033768,0.718080,6.518061,9.691271,8.470550,-2.297311,7.139413,-2.618516,4.323685,0.636546],[5.474609,1.419126,-9.629379,-2.931831,4.677490,-1.010154,8.767771,2.924681,0.057685,-0.035919,0.211181,-2.595485],[9.707407,-1.983805,-4.328667,-7.595420,-6.010890,5.827357,7.763151,-4.495349,-4.135750,1.398970,-7.451885,4.829412],[-3.223422,2.125111,-4.822953,-0.444109,-4.636230,-2.708682,-8.959538,4.273694,-5.930026,5.337192,-2.396287,-3.872452],[-2.301024,-4.034522,-1.077967,0.874598,3.915519,3.039987,-9.037837,5.466563,-4.916149,-1.347477,-2.194396,6.930342],[-1.563785,0.371308,-7.186110,0.563822,0.776929,-4.115463,2.480478,-7.819330,-1.562732,1.914811,9.426872,3.232445],[-2.036027,-5.958635,0.955550,-5.623572,-0.265715,7.738138,4.572975,-4.426543,-9.377843,3.996442,-8.716045,8.383048],[4.497594,2.047570,2.246031,-8.615620,-7.034858,9.411372,-7.323063,3.457963,8.847071,5.817004,-6.755524,6.873410],[-2.834152,-0.357831,8.599460,1.763718,-4.576301,5.059988,-9.288358,-2.199267,1.310129,-6.696987,2.491355,-0.242189],[-6.511463,3.076874,5.386788,-5.256398,8.028774,-0.613041,-4.004386,7.557166,3.868230,-6.551836,-4.409751,-9.658400],[-0.775940,0.052658,1.282626,-2.022921,-4.684220,-4.362522,8.539932,4.030555,4.031254,1.980213,-4.449103,6.931433],[6.128563,1.283533,-7.195322,4.490001,-3.317692,-3.119656,5.680751,-7.553524,-3.643925,0.428367,2.759088,3.657025],[9.111973,-6.074703,8.128601,2.337699,3.617104,3.709090,-5.778035,3.887197,7.968291,-5.404829,-7.486265,-6.478776],[9.389792,-2.369993,4.441014,-2.851267,-7.745211,-7.011589,-5.693539,4.818060,-9.355082,9.788517,7.694685,8.768471],[-6.495398,7.237462,-3.496694,1.682404,-7.716117,-0.722680,0.537336,-5.156960,1.444336,-3.431329,-4.400140,-4.037618],[-9.859992,2.823632,-0.550724,-0.559945,4.644409,9.384717,-0.070744,2.318923,3.355683,-3.527136,-1.199040,-7.237616]],[[3.510711,2.836164,-7.159795,-8.478837,8.498032,2.065765,-9.995703,-5.113158,2.913776,-8.053567,3.457833,-1.762623],[1.393659,5.413420,5.603241,-4.220403,-3.976653,-5.275208,0.163039,1.011251,0.159349,-6.649194,8.653660,7.235454],[-4.989462,-2.767725,7.082817,-0.350414,7.276081,5.157294,-4.339690,2.997170,3.434833,4.229482,-8.781810,-8.186291],[2.263979,5.500732,1.830547,-1.401645,-2.179091,6.260332,1.212893,1.703107,-2.291128,-1.382103,-8.540943,5.581684],[0.969693,-0.929493,-7.647737,3.821614,9.675246,-8.645662,2.119503,-9.354530,4.034336,-3.559187,-7.512732,4.526791],[-6.554777,5.856265,8.688259,-1.620949,3.578687,-5.950764,6.059740,-4.649542,-0.145503,-9.031474,8.177401,-7.123933],[-6.932343,5.132033,-7.494798,7.547211,-6.206702,0.065074,-1.832317,9.066620,-2.190224,4.024647,6.730082,-1.873504],[-6.040734,-3.408369,2.426511,-9.924454,7.768652,-0.557128,-1.863300,-2.624229,-1.415504,-0.372632,5.926720,5.295987],[3.437158,-7.929335,-1.879447,-0.690759,2.788869,-8.989899,5.443142,-8.372936,-0.564312,-1.152197,0.700983,-4.359287],[-2.016018,-8.277796,-2.196662,3.120430,-0.028580,-8.108875,-4.570487,5.486361,0.737328,2.211202,-0.010954,2.974362],[-7.151953,0.197558,-0.598724,-3.991598,-9.298619,0.376716,-9.947664,-7.595986,-6.777085,7.142641,8.870580,-8.602503],[-3.071754,-7.255657,3.783050,7.474457,8.151344,9.665339,-6.289778,6.825230,-4.817990,3.899049,8.148154,7.178401],[2.118414,7.224197,7.814690,7.422969,3.677600,-4.955616,-8.849627,-5.977699,-1.613810,3.773833,3.084482,4.329660],[1.686887,-0.344719,-2.163102,-5.615560,-1.109583,3.605293,1.314260,8.788613,-5.750493,-5.188961,-7.149384,-3.893358],[-4.281214,0.104815,-9.085879,-3.066464,-6.059536,4.189381,-3.162580,-6.071659,5.405249,5.827932,-7.410904,5.038200],[-5.467861,5.669437,-0.270347,-7.605094,-1.819415,3.638001,-5.488431,-8.925731,-7.842715,-3.290991,-6.964242,-7.953899]],[[-1.295370,-4.856551,-6.727640,1.990662,9.324963,2.730900,-3.007616,1.617927,-6.169603,-2.278428,-6.878988,2.471200],[-4.651298,5.170899,-0.917829,-0.094496,6.592480,9.300046,-5.311316,8.245021,-6.850627,1.968139,-8.567925,0.818674],[1.434090,5.586362,-5.832828,8.398716,-8.788729,8.002054,-0.796824,7.937836,7.165717,4.510746,2.346579,1.134357],[-1.554530,0.039034,2.684822,8.070556,-1.415723,-0.741719,2.307914,2.096240,8.758776,-5.499525,-0.496813,9.971987],[-2.592715,8.213132,6.553695,4.283709,4.094776,-6.493698,9.914404,-2.061377,7.858060,6.028604,-0.185918,-9.463021],[0.214271,7.758737,3.990410,3.879617,5.940825,1.864895,-3.996099,-4.416144,1.047339,-2.321144,-6.434462,-2.256932],[-5.074747,-9.315515,-1.584339,-9.813276,4.320546,0.421047,-8.953717,4.617743,3.971090,8.212728,2.745046,-6.643138],[-2.743475,-3.501739,5.153635,-0.647426,-1.749122,-7.958290,-6.762757,-5.635068,-7.179217,-6.460096,3.149608,-1.182871],[-9.582185,-5.833577,-0.688363,3.733646,2.239318,0.424498,-2.673551,-2.502475,7.131396,-4.167269,8.304512,4.770475],[-0.391335,0.718618,3.990337,0.311084,7.790857,-3.209968,-0.445942,-2.664367,3.015935,-8.986186,-2.203648,-1.389178],[5.131852,5.969624,5.419273,-0.911718,-6.070966,1.247245,9.385183,4.785572,-1.112336,-0.583018,4.656817,0.258884],[9.697609,7.335026,-7.751725,4.797016,-2.370149,6.138354,8.525557,5.507710,5.397869,-4.955902,1.756135,2.268705],[2.043978,-2.939189,-9.396330,6.466820,1.397790,1.300585,-9.819995,1.946974,1.386675,-1.074305,-1.394983,-6.053987],[5.259274,3.006458,8.923382,-6.132824,-4.351166,1.794801,-2.603043,-0.063158,0.393148,-0.440156,-7.983638,-7.207320],[-9.993001,6.830379,0.036297,-5.110788,-8.108113,1.793353,-1.358251,-3.340584,1.245019,8.317900,-0.431555,4.681238],[-3.682811,7.999481,-6.083751,-1.641978,-7.624646,8.551762,-2.216997,-8.442959,4.545987,-3.424865,-8.854480,3.619293]]], dtype = "float32")#candidate|4446|(12, 16, 12)|const|float32
bop_4447 = relay.multiply(var_4445.astype('float32'), relay.reshape(const_4446.astype('float32'), relay.shape_of(var_4445))) # shape=(12, 16, 12)
output = relay.Tuple([bop_4447,])
output2 = relay.Tuple([bop_4447,])
func_4459 = relay.Function([var_4445,], output)
mod['func_4459'] = func_4459
mod = relay.transform.InferType()(mod)
var_4460 = relay.var("var_4460", dtype = "float32", shape = (12, 16, 12))#candidate|4460|(12, 16, 12)|var|float32
output = func_4459(var_4460)
func_4461 = relay.Function([var_4460], output)
mutated_mod['func_4461'] = func_4461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_997_call = mod.get_global_var('func_997')
func_999_call = mutated_mod.get_global_var('func_999')
call_4484 = relay.TupleGetItem(func_997_call(), 0)
call_4485 = relay.TupleGetItem(func_999_call(), 0)
output = relay.Tuple([call_4484,])
output2 = relay.Tuple([call_4485,])
func_4502 = relay.Function([], output)
mod['func_4502'] = func_4502
mod = relay.transform.InferType()(mod)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4502_call = mutated_mod.get_global_var('func_4502')
call_4503 = func_4502_call()
output = call_4503
func_4504 = relay.Function([], output)
mutated_mod['func_4504'] = func_4504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3428_call = mod.get_global_var('func_3428')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_4550 = relay.TupleGetItem(func_3428_call(), 0)
call_4551 = relay.TupleGetItem(func_3430_call(), 0)
output = relay.Tuple([call_4550,])
output2 = relay.Tuple([call_4551,])
func_4552 = relay.Function([], output)
mod['func_4552'] = func_4552
mod = relay.transform.InferType()(mod)
output = func_4552()
func_4553 = relay.Function([], output)
mutated_mod['func_4553'] = func_4553
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4554 = relay.var("var_4554", dtype = "float64", shape = (8, 2, 8))#candidate|4554|(8, 2, 8)|var|float64
uop_4555 = relay.rsqrt(var_4554.astype('float64')) # shape=(8, 2, 8)
func_979_call = mod.get_global_var('func_979')
func_981_call = mutated_mod.get_global_var('func_981')
call_4564 = relay.TupleGetItem(func_979_call(), 0)
call_4565 = relay.TupleGetItem(func_981_call(), 0)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_4572 = func_820_call()
call_4573 = func_820_call()
func_3388_call = mod.get_global_var('func_3388')
func_3392_call = mutated_mod.get_global_var('func_3392')
const_4575 = relay.const(True, dtype = "bool")#candidate|4575|()|const|bool
const_4576 = relay.const([False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|4576|(140,)|const|bool
call_4574 = func_3388_call(relay.reshape(const_4575.astype('bool'), []), relay.reshape(const_4576.astype('bool'), [10, 2, 7]), )
call_4577 = func_3388_call(relay.reshape(const_4575.astype('bool'), []), relay.reshape(const_4576.astype('bool'), [10, 2, 7]), )
uop_4588 = relay.atan(uop_4555.astype('float32')) # shape=(8, 2, 8)
func_1773_call = mod.get_global_var('func_1773')
func_1777_call = mutated_mod.get_global_var('func_1777')
var_4593 = relay.var("var_4593", dtype = "float32", shape = (1, 77))#candidate|4593|(1, 77)|var|float32
const_4594 = relay.const([5.345979,6.531302,5.192319,7.340713,-2.657783,-4.771458,-6.236451,-2.951196,1.062490,-5.294112,-5.426467,-5.929349,3.086053,-7.563140,-1.455413,8.701945,-7.128056,8.966523,7.655566,-5.250100,8.370065,-9.333233,-9.327238,2.394204,-9.887324,6.265607,-7.268476,3.738547,-7.535546,-3.761497,-6.740574,-3.249235,1.407886,-6.837568,-0.332312,-1.856442,9.626264,4.822244,-8.883356,-0.015906,3.004594,2.177854,7.773787,0.129399,-1.151429,7.056988,0.398768,-7.512045,1.157759,1.423867,0.983545,6.358115,-4.236081,-6.980170,2.857887,3.082047,1.768651,-3.271451,-0.524357,-7.900754,-0.152691,6.098900,0.394540,-0.748356,-1.044217,-1.214967,5.962774,1.492320,-9.578125,-0.723810,-1.799325,-2.806198,-0.737683,-3.280448,-1.388172,-1.440390,-9.764943,-5.181111,7.632755,2.602175,0.583855,3.841660,4.158084,-7.402400,4.534185,-2.813838,4.033106,6.730495,3.057873,-2.737133,-8.402998,-0.515047,-8.404536,-4.665343,1.080806,4.623570,8.735327,-7.011099,2.003191,-6.226540,4.511618,-7.302558,-7.241475,3.705350,-3.323648,0.514317,-5.522780,1.875793,1.914398,-6.900679,3.866080,9.532636,-5.236659,-6.039373,-1.237885,-0.948172,4.455218,-2.318961,-3.307942,6.856168,6.252881,3.812656,2.246387,-4.124000,-0.670525,4.236803,9.789500,-6.515143,-3.859361,2.495447,-1.895813,8.872278,6.687244,4.476460,5.246972,-4.691394,2.618710,-0.904043,-3.095124,0.342117,1.869352,2.864912,2.142048,-2.273436,-8.085045,4.453531,-2.175149,-7.785867,-6.889799,8.111910,-4.999625,5.375104,-2.554619,-6.021663], dtype = "float32")#candidate|4594|(154,)|const|float32
var_4595 = relay.var("var_4595", dtype = "float64", shape = (234,))#candidate|4595|(234,)|var|float64
call_4592 = relay.TupleGetItem(func_1773_call(relay.reshape(var_4593.astype('float32'), [77,]), relay.reshape(const_4594.astype('float32'), [154,]), relay.reshape(var_4595.astype('float64'), [234,]), ), 4)
call_4596 = relay.TupleGetItem(func_1777_call(relay.reshape(var_4593.astype('float32'), [77,]), relay.reshape(const_4594.astype('float32'), [154,]), relay.reshape(var_4595.astype('float64'), [234,]), ), 4)
output = relay.Tuple([call_4564,call_4572,call_4574,const_4575,const_4576,uop_4588,call_4592,var_4593,const_4594,var_4595,])
output2 = relay.Tuple([call_4565,call_4573,call_4577,const_4575,const_4576,uop_4588,call_4596,var_4593,const_4594,var_4595,])
func_4619 = relay.Function([var_4554,var_4593,var_4595,], output)
mod['func_4619'] = func_4619
mod = relay.transform.InferType()(mod)
var_4620 = relay.var("var_4620", dtype = "float64", shape = (8, 2, 8))#candidate|4620|(8, 2, 8)|var|float64
var_4621 = relay.var("var_4621", dtype = "float32", shape = (1, 77))#candidate|4621|(1, 77)|var|float32
var_4622 = relay.var("var_4622", dtype = "float64", shape = (234,))#candidate|4622|(234,)|var|float64
output = func_4619(var_4620,var_4621,var_4622,)
func_4623 = relay.Function([var_4620,var_4621,var_4622,], output)
mutated_mod['func_4623'] = func_4623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4298_call = mod.get_global_var('func_4298')
func_4299_call = mutated_mod.get_global_var('func_4299')
call_4643 = relay.TupleGetItem(func_4298_call(), 1)
call_4644 = relay.TupleGetItem(func_4299_call(), 1)
output = relay.Tuple([call_4643,])
output2 = relay.Tuple([call_4644,])
func_4649 = relay.Function([], output)
mod['func_4649'] = func_4649
mod = relay.transform.InferType()(mod)
mutated_mod['func_4649'] = func_4649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4649_call = mutated_mod.get_global_var('func_4649')
call_4650 = func_4649_call()
output = call_4650
func_4651 = relay.Function([], output)
mutated_mod['func_4651'] = func_4651
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4710 = relay.var("var_4710", dtype = "float64", shape = (6, 14, 13))#candidate|4710|(6, 14, 13)|var|float64
uop_4711 = relay.atan(var_4710.astype('float64')) # shape=(6, 14, 13)
func_1334_call = mod.get_global_var('func_1334')
func_1336_call = mutated_mod.get_global_var('func_1336')
call_4726 = relay.TupleGetItem(func_1334_call(), 0)
call_4727 = relay.TupleGetItem(func_1336_call(), 0)
bop_4729 = relay.maximum(uop_4711.astype('float64'), relay.reshape(var_4710.astype('float64'), relay.shape_of(uop_4711))) # shape=(6, 14, 13)
output = relay.Tuple([call_4726,bop_4729,])
output2 = relay.Tuple([call_4727,bop_4729,])
func_4738 = relay.Function([var_4710,], output)
mod['func_4738'] = func_4738
mod = relay.transform.InferType()(mod)
var_4739 = relay.var("var_4739", dtype = "float64", shape = (6, 14, 13))#candidate|4739|(6, 14, 13)|var|float64
output = func_4738(var_4739)
func_4740 = relay.Function([var_4739], output)
mutated_mod['func_4740'] = func_4740
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_4771 = func_3236_call()
call_4772 = func_3236_call()
func_2678_call = mod.get_global_var('func_2678')
func_2680_call = mutated_mod.get_global_var('func_2680')
call_4783 = relay.TupleGetItem(func_2678_call(), 1)
call_4784 = relay.TupleGetItem(func_2680_call(), 1)
output = relay.Tuple([call_4771,call_4783,])
output2 = relay.Tuple([call_4772,call_4784,])
func_4786 = relay.Function([], output)
mod['func_4786'] = func_4786
mod = relay.transform.InferType()(mod)
mutated_mod['func_4786'] = func_4786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mutated_mod.get_global_var('func_4786')
call_4787 = func_4786_call()
output = call_4787
func_4788 = relay.Function([], output)
mutated_mod['func_4788'] = func_4788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3535_call = mod.get_global_var('func_3535')
func_3537_call = mutated_mod.get_global_var('func_3537')
call_4794 = relay.TupleGetItem(func_3535_call(), 0)
call_4795 = relay.TupleGetItem(func_3537_call(), 0)
output = call_4794
output2 = call_4795
func_4803 = relay.Function([], output)
mod['func_4803'] = func_4803
mod = relay.transform.InferType()(mod)
mutated_mod['func_4803'] = func_4803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4803_call = mutated_mod.get_global_var('func_4803')
call_4804 = func_4803_call()
output = call_4804
func_4805 = relay.Function([], output)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_4832 = relay.TupleGetItem(func_1488_call(), 1)
call_4833 = relay.TupleGetItem(func_1489_call(), 1)
func_2557_call = mod.get_global_var('func_2557')
func_2561_call = mutated_mod.get_global_var('func_2561')
var_4843 = relay.var("var_4843", dtype = "float32", shape = (77,))#candidate|4843|(77,)|var|float32
var_4844 = relay.var("var_4844", dtype = "float32", shape = (154,))#candidate|4844|(154,)|var|float32
call_4842 = relay.TupleGetItem(func_2557_call(relay.reshape(var_4843.astype('float32'), [1, 77]), relay.reshape(var_4844.astype('float32'), [154,]), ), 4)
call_4845 = relay.TupleGetItem(func_2561_call(relay.reshape(var_4843.astype('float32'), [1, 77]), relay.reshape(var_4844.astype('float32'), [154,]), ), 4)
output = relay.Tuple([call_4832,call_4842,var_4843,var_4844,])
output2 = relay.Tuple([call_4833,call_4845,var_4843,var_4844,])
func_4858 = relay.Function([var_4843,var_4844,], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
mutated_mod['func_4858'] = func_4858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4858_call = mutated_mod.get_global_var('func_4858')
var_4860 = relay.var("var_4860", dtype = "float32", shape = (77,))#candidate|4860|(77,)|var|float32
var_4861 = relay.var("var_4861", dtype = "float32", shape = (154,))#candidate|4861|(154,)|var|float32
call_4859 = func_4858_call(var_4860,var_4861,)
output = call_4859
func_4862 = relay.Function([var_4860,var_4861,], output)
mutated_mod['func_4862'] = func_4862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3706_call = mod.get_global_var('func_3706')
func_3707_call = mutated_mod.get_global_var('func_3707')
call_4914 = func_3706_call()
call_4915 = func_3706_call()
output = relay.Tuple([call_4914,])
output2 = relay.Tuple([call_4915,])
func_4920 = relay.Function([], output)
mod['func_4920'] = func_4920
mod = relay.transform.InferType()(mod)
output = func_4920()
func_4921 = relay.Function([], output)
mutated_mod['func_4921'] = func_4921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4552_call = mod.get_global_var('func_4552')
func_4553_call = mutated_mod.get_global_var('func_4553')
call_4947 = relay.TupleGetItem(func_4552_call(), 0)
call_4948 = relay.TupleGetItem(func_4553_call(), 0)
output = relay.Tuple([call_4947,])
output2 = relay.Tuple([call_4948,])
func_5011 = relay.Function([], output)
mod['func_5011'] = func_5011
mod = relay.transform.InferType()(mod)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5011_call = mutated_mod.get_global_var('func_5011')
call_5012 = func_5011_call()
output = call_5012
func_5013 = relay.Function([], output)
mutated_mod['func_5013'] = func_5013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4502_call = mod.get_global_var('func_4502')
func_4504_call = mutated_mod.get_global_var('func_4504')
call_5122 = relay.TupleGetItem(func_4502_call(), 0)
call_5123 = relay.TupleGetItem(func_4504_call(), 0)
func_1713_call = mod.get_global_var('func_1713')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_5152 = relay.TupleGetItem(func_1713_call(), 8)
call_5153 = relay.TupleGetItem(func_1715_call(), 8)
output = relay.Tuple([call_5122,call_5152,])
output2 = relay.Tuple([call_5123,call_5153,])
func_5162 = relay.Function([], output)
mod['func_5162'] = func_5162
mod = relay.transform.InferType()(mod)
mutated_mod['func_5162'] = func_5162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5162_call = mutated_mod.get_global_var('func_5162')
call_5163 = func_5162_call()
output = call_5163
func_5164 = relay.Function([], output)
mutated_mod['func_5164'] = func_5164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_5185 = func_3236_call()
call_5186 = func_3236_call()
output = relay.Tuple([call_5185,])
output2 = relay.Tuple([call_5186,])
func_5192 = relay.Function([], output)
mod['func_5192'] = func_5192
mod = relay.transform.InferType()(mod)
output = func_5192()
func_5193 = relay.Function([], output)
mutated_mod['func_5193'] = func_5193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_5291 = relay.TupleGetItem(func_4195_call(), 0)
call_5292 = relay.TupleGetItem(func_4197_call(), 0)
output = relay.Tuple([call_5291,])
output2 = relay.Tuple([call_5292,])
func_5299 = relay.Function([], output)
mod['func_5299'] = func_5299
mod = relay.transform.InferType()(mod)
mutated_mod['func_5299'] = func_5299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5299_call = mutated_mod.get_global_var('func_5299')
call_5300 = func_5299_call()
output = call_5300
func_5301 = relay.Function([], output)
mutated_mod['func_5301'] = func_5301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_5408 = relay.TupleGetItem(func_2454_call(), 1)
call_5409 = relay.TupleGetItem(func_2456_call(), 1)
func_4858_call = mod.get_global_var('func_4858')
func_4862_call = mutated_mod.get_global_var('func_4862')
const_5417 = relay.const([[7.578630,-3.350390,-2.711065,-8.641627,9.765803,2.812827,-4.979192,-1.467189,3.602653,-7.556527,8.686414,0.090816,-5.827245,8.433900,-7.440025,-7.740369,8.283445,8.010013,-7.644656,9.506654,-4.882346,8.335469,5.247379,-2.739132,1.350979,2.001020,5.314522,0.454679,3.948875,0.177714,-9.887319,-2.200355,-9.033503,2.796891,2.866204,-8.020040,8.523144,9.122667,0.349839,7.465913,-0.286452,8.081831,-2.776148,-5.351992,-8.054886,1.283566,5.373267,-6.406818,-0.110870,-8.823001,-0.501859,0.266198,-8.549991,-8.181258,1.566482,-0.041863,-8.916160,8.568117,-4.536852,1.547219,5.615375,-9.970980,-0.893090,-2.174863,-2.239749,-7.514225,5.601490,7.512174,-5.336215,-3.987203,1.185511,-2.791744,-2.372482,-5.547796,7.727169,2.825581,6.057832]], dtype = "float32")#candidate|5417|(1, 77)|const|float32
const_5418 = relay.const([-3.886696,-1.756065,-4.893950,-1.318094,-2.676519,-2.033897,-3.813784,3.640583,5.331944,7.871515,6.658888,9.591947,8.515990,-9.490118,-3.787436,7.176868,2.806931,-4.231042,2.496940,7.108248,4.627989,-5.158348,-5.039098,-7.258520,-4.449258,6.637501,-1.277480,-7.248836,0.402975,-2.958414,-0.624851,-6.970596,-6.108456,-9.779974,-5.454007,0.525612,3.072574,9.417349,1.554412,4.469630,1.010973,5.252693,-6.579400,-6.288278,-8.302488,3.227106,-4.239134,5.352641,-2.601618,-2.077738,5.784307,8.247208,-2.948981,-2.690723,-4.450930,1.464291,3.062463,-6.560316,-9.055861,0.830426,8.651803,-0.361713,2.508743,-9.728354,0.511193,-8.392546,-5.573781,8.494739,-0.486267,4.378165,0.411357,5.327885,1.528056,-6.041809,-3.520243,0.045286,5.851021,3.460252,9.760182,-7.755331,-1.747402,6.527967,-6.868126,6.890891,2.782933,-7.280001,4.913741,1.397480,2.923780,1.432756,3.155533,6.461019,-1.641356,0.264966,5.448267,-6.770511,-6.001733,-5.906124,-7.728821,-2.339380,-8.600570,-9.231624,-5.614868,8.382890,-8.106454,9.696851,1.811846,-0.285394,9.946980,3.583533,6.856827,-1.951945,2.839826,7.174532,2.570467,7.146084,-8.390240,9.182445,7.255328,-2.927528,2.808896,-3.825361,-9.806791,-4.553234,-7.964113,-9.479228,5.377933,-4.779579,-5.603847,-0.253800,8.254531,9.623487,-9.636761,-7.320660,6.946356,9.876536,-1.655690,0.778573,-8.212716,-0.086072,2.834234,-6.811450,8.611304,-2.784405,-1.098548,1.637898,-6.073774,3.473724,-2.753068,6.505057,-2.399066,-2.392967,-0.671602,-5.741720], dtype = "float32")#candidate|5418|(154,)|const|float32
call_5416 = relay.TupleGetItem(func_4858_call(relay.reshape(const_5417.astype('float32'), [77,]), relay.reshape(const_5418.astype('float32'), [154,]), ), 2)
call_5419 = relay.TupleGetItem(func_4862_call(relay.reshape(const_5417.astype('float32'), [77,]), relay.reshape(const_5418.astype('float32'), [154,]), ), 2)
output = relay.Tuple([call_5408,call_5416,const_5417,const_5418,])
output2 = relay.Tuple([call_5409,call_5419,const_5417,const_5418,])
func_5425 = relay.Function([], output)
mod['func_5425'] = func_5425
mod = relay.transform.InferType()(mod)
mutated_mod['func_5425'] = func_5425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5425_call = mutated_mod.get_global_var('func_5425')
call_5426 = func_5425_call()
output = call_5426
func_5427 = relay.Function([], output)
mutated_mod['func_5427'] = func_5427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mod.get_global_var('func_4786')
func_4788_call = mutated_mod.get_global_var('func_4788')
call_5434 = relay.TupleGetItem(func_4786_call(), 0)
call_5435 = relay.TupleGetItem(func_4788_call(), 0)
output = relay.Tuple([call_5434,])
output2 = relay.Tuple([call_5435,])
func_5440 = relay.Function([], output)
mod['func_5440'] = func_5440
mod = relay.transform.InferType()(mod)
mutated_mod['func_5440'] = func_5440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5440_call = mutated_mod.get_global_var('func_5440')
call_5441 = func_5440_call()
output = call_5441
func_5442 = relay.Function([], output)
mutated_mod['func_5442'] = func_5442
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5453 = relay.var("var_5453", dtype = "float32", shape = (13, 8, 9))#candidate|5453|(13, 8, 9)|var|float32
uop_5454 = relay.log10(var_5453.astype('float32')) # shape=(13, 8, 9)
var_5475 = relay.var("var_5475", dtype = "float32", shape = (13, 8, 9))#candidate|5475|(13, 8, 9)|var|float32
bop_5476 = relay.greater_equal(uop_5454.astype('bool'), relay.reshape(var_5475.astype('bool'), relay.shape_of(uop_5454))) # shape=(13, 8, 9)
output = relay.Tuple([bop_5476,])
output2 = relay.Tuple([bop_5476,])
func_5479 = relay.Function([var_5453,var_5475,], output)
mod['func_5479'] = func_5479
mod = relay.transform.InferType()(mod)
var_5480 = relay.var("var_5480", dtype = "float32", shape = (13, 8, 9))#candidate|5480|(13, 8, 9)|var|float32
var_5481 = relay.var("var_5481", dtype = "float32", shape = (13, 8, 9))#candidate|5481|(13, 8, 9)|var|float32
output = func_5479(var_5480,var_5481,)
func_5482 = relay.Function([var_5480,var_5481,], output)
mutated_mod['func_5482'] = func_5482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_5484 = func_2364_call()
call_5485 = func_2364_call()
output = relay.Tuple([call_5484,])
output2 = relay.Tuple([call_5485,])
func_5490 = relay.Function([], output)
mod['func_5490'] = func_5490
mod = relay.transform.InferType()(mod)
output = func_5490()
func_5491 = relay.Function([], output)
mutated_mod['func_5491'] = func_5491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4502_call = mod.get_global_var('func_4502')
func_4504_call = mutated_mod.get_global_var('func_4504')
call_5504 = relay.TupleGetItem(func_4502_call(), 0)
call_5505 = relay.TupleGetItem(func_4504_call(), 0)
func_4313_call = mod.get_global_var('func_4313')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_5515 = relay.TupleGetItem(func_4313_call(), 0)
call_5516 = relay.TupleGetItem(func_4314_call(), 0)
output = relay.Tuple([call_5504,call_5515,])
output2 = relay.Tuple([call_5505,call_5516,])
func_5520 = relay.Function([], output)
mod['func_5520'] = func_5520
mod = relay.transform.InferType()(mod)
mutated_mod['func_5520'] = func_5520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5520_call = mutated_mod.get_global_var('func_5520')
call_5521 = func_5520_call()
output = call_5521
func_5522 = relay.Function([], output)
mutated_mod['func_5522'] = func_5522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_997_call = mod.get_global_var('func_997')
func_999_call = mutated_mod.get_global_var('func_999')
call_5557 = relay.TupleGetItem(func_997_call(), 0)
call_5558 = relay.TupleGetItem(func_999_call(), 0)
func_3993_call = mod.get_global_var('func_3993')
func_3996_call = mutated_mod.get_global_var('func_3996')
const_5564 = relay.const([-0.072252,2.243554,4.197536,4.501291,8.565672,4.696243,2.692791,4.978861], dtype = "float32")#candidate|5564|(8,)|const|float32
call_5563 = func_3993_call(relay.reshape(const_5564.astype('float32'), [8, 1, 1]))
call_5565 = func_3993_call(relay.reshape(const_5564.astype('float32'), [8, 1, 1]))
func_2755_call = mod.get_global_var('func_2755')
func_2757_call = mutated_mod.get_global_var('func_2757')
const_5569 = relay.const([-3,-2,1,1,5,4,9,-6,-7,3,1,3,6,-8,-4,10,-8,-4,6,-5,-3,-1,-10,5,7,9,2,7,-5,7,-4,5,-9,-8,-4,8,-6,10,-3,3,-10,10,-2,4,-4,7,7,-9,-2,-1,-2,4,5,3,-8,10,9,-4,8,10,-6,-9,10,-9,-5,-9,-9,-6,-8,6,7,5], dtype = "uint16")#candidate|5569|(72,)|const|uint16
call_5568 = relay.TupleGetItem(func_2755_call(relay.reshape(const_5569.astype('uint16'), [4, 6, 3])), 1)
call_5570 = relay.TupleGetItem(func_2757_call(relay.reshape(const_5569.astype('uint16'), [4, 6, 3])), 1)
func_5299_call = mod.get_global_var('func_5299')
func_5301_call = mutated_mod.get_global_var('func_5301')
call_5574 = relay.TupleGetItem(func_5299_call(), 0)
call_5575 = relay.TupleGetItem(func_5301_call(), 0)
output = relay.Tuple([call_5557,call_5563,const_5564,call_5568,const_5569,call_5574,])
output2 = relay.Tuple([call_5558,call_5565,const_5564,call_5570,const_5569,call_5575,])
func_5589 = relay.Function([], output)
mod['func_5589'] = func_5589
mod = relay.transform.InferType()(mod)
output = func_5589()
func_5590 = relay.Function([], output)
mutated_mod['func_5590'] = func_5590
mutated_mod = relay.transform.InferType()(mutated_mod)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_5601 = func_820_call()
call_5602 = func_820_call()
output = call_5601
output2 = call_5602
func_5603 = relay.Function([], output)
mod['func_5603'] = func_5603
mod = relay.transform.InferType()(mod)
mutated_mod['func_5603'] = func_5603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5603_call = mutated_mod.get_global_var('func_5603')
call_5604 = func_5603_call()
output = call_5604
func_5605 = relay.Function([], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5615 = relay.var("var_5615", dtype = "int8", shape = (6, 13, 4))#candidate|5615|(6, 13, 4)|var|int8
var_5616 = relay.var("var_5616", dtype = "int8", shape = (6, 13, 4))#candidate|5616|(6, 13, 4)|var|int8
bop_5617 = relay.add(var_5615.astype('int8'), relay.reshape(var_5616.astype('int8'), relay.shape_of(var_5615))) # shape=(6, 13, 4)
func_4786_call = mod.get_global_var('func_4786')
func_4788_call = mutated_mod.get_global_var('func_4788')
call_5628 = relay.TupleGetItem(func_4786_call(), 0)
call_5629 = relay.TupleGetItem(func_4788_call(), 0)
output = relay.Tuple([bop_5617,call_5628,])
output2 = relay.Tuple([bop_5617,call_5629,])
func_5640 = relay.Function([var_5615,var_5616,], output)
mod['func_5640'] = func_5640
mod = relay.transform.InferType()(mod)
var_5641 = relay.var("var_5641", dtype = "int8", shape = (6, 13, 4))#candidate|5641|(6, 13, 4)|var|int8
var_5642 = relay.var("var_5642", dtype = "int8", shape = (6, 13, 4))#candidate|5642|(6, 13, 4)|var|int8
output = func_5640(var_5641,var_5642,)
func_5643 = relay.Function([var_5641,var_5642,], output)
mutated_mod['func_5643'] = func_5643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4920_call = mod.get_global_var('func_4920')
func_4921_call = mutated_mod.get_global_var('func_4921')
call_5683 = relay.TupleGetItem(func_4920_call(), 0)
call_5684 = relay.TupleGetItem(func_4921_call(), 0)
output = call_5683
output2 = call_5684
func_5686 = relay.Function([], output)
mod['func_5686'] = func_5686
mod = relay.transform.InferType()(mod)
output = func_5686()
func_5687 = relay.Function([], output)
mutated_mod['func_5687'] = func_5687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2678_call = mod.get_global_var('func_2678')
func_2680_call = mutated_mod.get_global_var('func_2680')
call_5709 = relay.TupleGetItem(func_2678_call(), 0)
call_5710 = relay.TupleGetItem(func_2680_call(), 0)
func_1417_call = mod.get_global_var('func_1417')
func_1420_call = mutated_mod.get_global_var('func_1420')
var_5716 = relay.var("var_5716", dtype = "float64", shape = (234,))#candidate|5716|(234,)|var|float64
call_5715 = relay.TupleGetItem(func_1417_call(relay.reshape(var_5716.astype('float64'), [234,])), 0)
call_5717 = relay.TupleGetItem(func_1420_call(relay.reshape(var_5716.astype('float64'), [234,])), 0)
uop_5719 = relay.tan(call_5715.astype('float64')) # shape=(234,)
uop_5721 = relay.tan(call_5717.astype('float64')) # shape=(234,)
output = relay.Tuple([call_5709,var_5716,uop_5719,])
output2 = relay.Tuple([call_5710,var_5716,uop_5721,])
func_5724 = relay.Function([var_5716,], output)
mod['func_5724'] = func_5724
mod = relay.transform.InferType()(mod)
var_5725 = relay.var("var_5725", dtype = "float64", shape = (234,))#candidate|5725|(234,)|var|float64
output = func_5724(var_5725)
func_5726 = relay.Function([var_5725], output)
mutated_mod['func_5726'] = func_5726
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_5755 = func_2364_call()
call_5756 = func_2364_call()
output = call_5755
output2 = call_5756
func_5765 = relay.Function([], output)
mod['func_5765'] = func_5765
mod = relay.transform.InferType()(mod)
output = func_5765()
func_5766 = relay.Function([], output)
mutated_mod['func_5766'] = func_5766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2678_call = mod.get_global_var('func_2678')
func_2680_call = mutated_mod.get_global_var('func_2680')
call_5840 = relay.TupleGetItem(func_2678_call(), 0)
call_5841 = relay.TupleGetItem(func_2680_call(), 0)
output = call_5840
output2 = call_5841
func_5873 = relay.Function([], output)
mod['func_5873'] = func_5873
mod = relay.transform.InferType()(mod)
mutated_mod['func_5873'] = func_5873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5873_call = mutated_mod.get_global_var('func_5873')
call_5874 = func_5873_call()
output = call_5874
func_5875 = relay.Function([], output)
mutated_mod['func_5875'] = func_5875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3236_call = mod.get_global_var('func_3236')
func_3238_call = mutated_mod.get_global_var('func_3238')
call_5888 = func_3236_call()
call_5889 = func_3236_call()
output = call_5888
output2 = call_5889
func_5904 = relay.Function([], output)
mod['func_5904'] = func_5904
mod = relay.transform.InferType()(mod)
mutated_mod['func_5904'] = func_5904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5904_call = mutated_mod.get_global_var('func_5904')
call_5905 = func_5904_call()
output = call_5905
func_5906 = relay.Function([], output)
mutated_mod['func_5906'] = func_5906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5904_call = mod.get_global_var('func_5904')
func_5906_call = mutated_mod.get_global_var('func_5906')
call_5914 = func_5904_call()
call_5915 = func_5904_call()
output = call_5914
output2 = call_5915
func_5918 = relay.Function([], output)
mod['func_5918'] = func_5918
mod = relay.transform.InferType()(mod)
output = func_5918()
func_5919 = relay.Function([], output)
mutated_mod['func_5919'] = func_5919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5011_call = mod.get_global_var('func_5011')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_5922 = relay.TupleGetItem(func_5011_call(), 0)
call_5923 = relay.TupleGetItem(func_5013_call(), 0)
func_2755_call = mod.get_global_var('func_2755')
func_2757_call = mutated_mod.get_global_var('func_2757')
var_5939 = relay.var("var_5939", dtype = "uint16", shape = (72,))#candidate|5939|(72,)|var|uint16
call_5938 = relay.TupleGetItem(func_2755_call(relay.reshape(var_5939.astype('uint16'), [4, 6, 3])), 1)
call_5940 = relay.TupleGetItem(func_2757_call(relay.reshape(var_5939.astype('uint16'), [4, 6, 3])), 1)
bop_5955 = relay.right_shift(call_5938.astype('uint32'), relay.reshape(var_5939.astype('uint32'), relay.shape_of(call_5938))) # shape=(4, 6, 3)
bop_5958 = relay.right_shift(call_5940.astype('uint32'), relay.reshape(var_5939.astype('uint32'), relay.shape_of(call_5940))) # shape=(4, 6, 3)
output = relay.Tuple([call_5922,bop_5955,])
output2 = relay.Tuple([call_5923,bop_5958,])
func_5970 = relay.Function([var_5939,], output)
mod['func_5970'] = func_5970
mod = relay.transform.InferType()(mod)
var_5971 = relay.var("var_5971", dtype = "uint16", shape = (72,))#candidate|5971|(72,)|var|uint16
output = func_5970(var_5971)
func_5972 = relay.Function([var_5971], output)
mutated_mod['func_5972'] = func_5972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5490_call = mod.get_global_var('func_5490')
func_5491_call = mutated_mod.get_global_var('func_5491')
call_5984 = relay.TupleGetItem(func_5490_call(), 0)
call_5985 = relay.TupleGetItem(func_5491_call(), 0)
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_6000 = relay.TupleGetItem(func_4195_call(), 0)
call_6001 = relay.TupleGetItem(func_4197_call(), 0)
func_5686_call = mod.get_global_var('func_5686')
func_5687_call = mutated_mod.get_global_var('func_5687')
call_6013 = func_5686_call()
call_6014 = func_5686_call()
output = relay.Tuple([call_5984,call_6000,call_6013,])
output2 = relay.Tuple([call_5985,call_6001,call_6014,])
func_6021 = relay.Function([], output)
mod['func_6021'] = func_6021
mod = relay.transform.InferType()(mod)
output = func_6021()
func_6022 = relay.Function([], output)
mutated_mod['func_6022'] = func_6022
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6028 = relay.var("var_6028", dtype = "float32", shape = (10, 15, 9))#candidate|6028|(10, 15, 9)|var|float32
uop_6029 = relay.sigmoid(var_6028.astype('float32')) # shape=(10, 15, 9)
func_1926_call = mod.get_global_var('func_1926')
func_1929_call = mutated_mod.get_global_var('func_1929')
var_6033 = relay.var("var_6033", dtype = "float64", shape = ())#candidate|6033|()|var|float64
const_6034 = relay.const([3.695014,-6.899023,1.122769,0.471543,8.426465,0.722525,3.000312,3.085588,-3.004646,-4.225363,-7.000800,1.995803,-6.458976,-0.175947,9.297289,-7.962380,7.568885,-4.557890,-8.481763,-6.967168,7.831074,5.492318,-8.602721,-4.182611,-4.020277,-0.929439,1.826042,-6.965901,7.111438,9.610795,-9.691650,9.839151,8.754868,5.171278,-5.058431,3.144070,2.569067,-0.893442,0.475400,-0.504694], dtype = "float64")#candidate|6034|(40,)|const|float64
call_6032 = relay.TupleGetItem(func_1926_call(relay.reshape(var_6033.astype('float64'), []), relay.reshape(const_6034.astype('float64'), [10, 2, 2]), ), 2)
call_6035 = relay.TupleGetItem(func_1929_call(relay.reshape(var_6033.astype('float64'), []), relay.reshape(const_6034.astype('float64'), [10, 2, 2]), ), 2)
output = relay.Tuple([uop_6029,call_6032,var_6033,const_6034,])
output2 = relay.Tuple([uop_6029,call_6035,var_6033,const_6034,])
func_6046 = relay.Function([var_6028,var_6033,], output)
mod['func_6046'] = func_6046
mod = relay.transform.InferType()(mod)
var_6047 = relay.var("var_6047", dtype = "float32", shape = (10, 15, 9))#candidate|6047|(10, 15, 9)|var|float32
var_6048 = relay.var("var_6048", dtype = "float64", shape = ())#candidate|6048|()|var|float64
output = func_6046(var_6047,var_6048,)
func_6049 = relay.Function([var_6047,var_6048,], output)
mutated_mod['func_6049'] = func_6049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4649_call = mod.get_global_var('func_4649')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_6051 = relay.TupleGetItem(func_4649_call(), 0)
call_6052 = relay.TupleGetItem(func_4651_call(), 0)
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_6068 = func_820_call()
call_6069 = func_820_call()
func_820_call = mod.get_global_var('func_820')
func_822_call = mutated_mod.get_global_var('func_822')
call_6074 = func_820_call()
call_6075 = func_820_call()
output = relay.Tuple([call_6051,call_6068,call_6074,])
output2 = relay.Tuple([call_6052,call_6069,call_6075,])
func_6088 = relay.Function([], output)
mod['func_6088'] = func_6088
mod = relay.transform.InferType()(mod)
output = func_6088()
func_6089 = relay.Function([], output)
mutated_mod['func_6089'] = func_6089
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6212 = relay.const([[[5.758036,4.919081,-6.863566,-8.676150,6.960921,-7.009226,-1.440948,-0.366920],[1.218272,-1.024069,-1.299296,-1.567266,-8.763815,-8.638018,3.399764,7.014625],[6.726369,9.831894,1.856001,2.744118,-1.058180,-1.369319,-9.140108,-6.761177],[5.584250,-0.687749,9.990844,0.658685,-9.934479,-4.020320,5.579418,-1.967036],[-6.820554,-1.006652,1.538279,2.776725,8.174403,-9.026938,-9.935387,5.158791],[7.961820,-9.520232,6.017503,-4.915452,9.112467,0.709679,-2.604348,0.220580],[6.462048,-2.631290,2.428900,1.396443,-5.433767,2.304320,-8.501207,-1.832784],[-3.770999,9.944006,-0.713546,5.311733,-0.110665,-0.968839,-2.610231,-9.533251],[6.794038,3.975345,-7.616650,7.617692,-4.604593,8.256274,3.507396,8.855677],[-7.401522,2.951298,-3.650935,-1.721057,9.943023,-8.955180,-2.539490,-6.898645],[1.888433,8.343374,-8.679468,-4.202584,5.596731,8.484838,7.108867,-1.385325]]], dtype = "float32")#candidate|6212|(1, 11, 8)|const|float32
uop_6213 = relay.tan(const_6212.astype('float32')) # shape=(1, 11, 8)
bop_6224 = relay.add(const_6212.astype('int32'), relay.reshape(uop_6213.astype('int32'), relay.shape_of(const_6212))) # shape=(1, 11, 8)
func_1713_call = mod.get_global_var('func_1713')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_6245 = relay.TupleGetItem(func_1713_call(), 0)
call_6246 = relay.TupleGetItem(func_1715_call(), 0)
uop_6250 = relay.sqrt(uop_6213.astype('float64')) # shape=(1, 11, 8)
func_2364_call = mod.get_global_var('func_2364')
func_2366_call = mutated_mod.get_global_var('func_2366')
call_6261 = func_2364_call()
call_6262 = func_2364_call()
func_3388_call = mod.get_global_var('func_3388')
func_3392_call = mutated_mod.get_global_var('func_3392')
const_6274 = relay.const(True, dtype = "bool")#candidate|6274|()|const|bool
var_6275 = relay.var("var_6275", dtype = "bool", shape = (140,))#candidate|6275|(140,)|var|bool
call_6273 = func_3388_call(relay.reshape(const_6274.astype('bool'), []), relay.reshape(var_6275.astype('bool'), [10, 2, 7]), )
call_6276 = func_3388_call(relay.reshape(const_6274.astype('bool'), []), relay.reshape(var_6275.astype('bool'), [10, 2, 7]), )
output = relay.Tuple([bop_6224,call_6245,uop_6250,call_6261,call_6273,const_6274,var_6275,])
output2 = relay.Tuple([bop_6224,call_6246,uop_6250,call_6262,call_6276,const_6274,var_6275,])
func_6280 = relay.Function([var_6275,], output)
mod['func_6280'] = func_6280
mod = relay.transform.InferType()(mod)
var_6281 = relay.var("var_6281", dtype = "bool", shape = (140,))#candidate|6281|(140,)|var|bool
output = func_6280(var_6281)
func_6282 = relay.Function([var_6281], output)
mutated_mod['func_6282'] = func_6282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5686_call = mod.get_global_var('func_5686')
func_5687_call = mutated_mod.get_global_var('func_5687')
call_6358 = func_5686_call()
call_6359 = func_5686_call()
output = relay.Tuple([call_6358,])
output2 = relay.Tuple([call_6359,])
func_6362 = relay.Function([], output)
mod['func_6362'] = func_6362
mod = relay.transform.InferType()(mod)
output = func_6362()
func_6363 = relay.Function([], output)
mutated_mod['func_6363'] = func_6363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4313_call = mod.get_global_var('func_4313')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_6372 = relay.TupleGetItem(func_4313_call(), 0)
call_6373 = relay.TupleGetItem(func_4314_call(), 0)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_6374 = func_5765_call()
call_6375 = func_5765_call()
func_4391_call = mod.get_global_var('func_4391')
func_4393_call = mutated_mod.get_global_var('func_4393')
const_6379 = relay.const([-2.336632,4.041084,0.025409,6.141325,-9.470370,9.457515,-9.938119,6.670817,7.339045,-5.597598,6.766072,9.998247,-2.888971,-1.952708,-3.597598,8.426527,-1.014459,-8.801158,9.764631,3.339395,-1.318081,-1.184723,1.550461,8.729766,-3.606836,5.644446,-2.945455,-3.551532,6.340811,-4.433271,-1.233226,-3.558664,-6.481470,4.354336,-4.244436,-0.140035,4.352350,0.632443,-5.644594,-7.837214,4.255763,-9.841213,-5.424729,-5.883561,-5.870278,1.938999,-0.004124,0.150935,-0.142922,-2.031735,2.612026,6.025302,0.274219,-5.565718,0.149050,3.221160,-9.361082,8.135231,-5.088951,4.396737,-6.630735,-4.000894,-8.107935,-0.591417,-0.905380,-1.390985,7.262989,-7.254531,-7.342192,-8.944595,6.929201,-8.036602,-8.828777,9.988660,8.576595,6.710605,2.465009], dtype = "float32")#candidate|6379|(77,)|const|float32
call_6378 = relay.TupleGetItem(func_4391_call(relay.reshape(const_6379.astype('float32'), [77,])), 0)
call_6380 = relay.TupleGetItem(func_4393_call(relay.reshape(const_6379.astype('float32'), [77,])), 0)
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
var_6384 = relay.var("var_6384", dtype = "int64", shape = (1, 360))#candidate|6384|(1, 360)|var|int64
call_6383 = func_190_call(relay.reshape(var_6384.astype('int64'), [8, 5, 9]), relay.reshape(var_6384.astype('int64'), [8, 5, 9]), )
call_6385 = func_190_call(relay.reshape(var_6384.astype('int64'), [8, 5, 9]), relay.reshape(var_6384.astype('int64'), [8, 5, 9]), )
func_4619_call = mod.get_global_var('func_4619')
func_4623_call = mutated_mod.get_global_var('func_4623')
var_6414 = relay.var("var_6414", dtype = "float64", shape = (4, 32))#candidate|6414|(4, 32)|var|float64
var_6415 = relay.var("var_6415", dtype = "float64", shape = (234,))#candidate|6415|(234,)|var|float64
call_6413 = relay.TupleGetItem(func_4619_call(relay.reshape(var_6414.astype('float64'), [8, 2, 8]), relay.reshape(const_6379.astype('float32'), [1, 77]), relay.reshape(var_6415.astype('float64'), [234,]), ), 9)
call_6416 = relay.TupleGetItem(func_4623_call(relay.reshape(var_6414.astype('float64'), [8, 2, 8]), relay.reshape(const_6379.astype('float32'), [1, 77]), relay.reshape(var_6415.astype('float64'), [234,]), ), 9)
output = relay.Tuple([call_6372,call_6374,call_6378,const_6379,call_6383,var_6384,call_6413,var_6414,var_6415,])
output2 = relay.Tuple([call_6373,call_6375,call_6380,const_6379,call_6385,var_6384,call_6416,var_6414,var_6415,])
func_6424 = relay.Function([var_6384,var_6414,var_6415,], output)
mod['func_6424'] = func_6424
mod = relay.transform.InferType()(mod)
var_6425 = relay.var("var_6425", dtype = "int64", shape = (1, 360))#candidate|6425|(1, 360)|var|int64
var_6426 = relay.var("var_6426", dtype = "float64", shape = (4, 32))#candidate|6426|(4, 32)|var|float64
var_6427 = relay.var("var_6427", dtype = "float64", shape = (234,))#candidate|6427|(234,)|var|float64
output = func_6424(var_6425,var_6426,var_6427,)
func_6428 = relay.Function([var_6425,var_6426,var_6427,], output)
mutated_mod['func_6428'] = func_6428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4502_call = mod.get_global_var('func_4502')
func_4504_call = mutated_mod.get_global_var('func_4504')
call_6455 = relay.TupleGetItem(func_4502_call(), 0)
call_6456 = relay.TupleGetItem(func_4504_call(), 0)
output = relay.Tuple([call_6455,])
output2 = relay.Tuple([call_6456,])
func_6510 = relay.Function([], output)
mod['func_6510'] = func_6510
mod = relay.transform.InferType()(mod)
mutated_mod['func_6510'] = func_6510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6510_call = mutated_mod.get_global_var('func_6510')
call_6511 = func_6510_call()
output = call_6511
func_6512 = relay.Function([], output)
mutated_mod['func_6512'] = func_6512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_6581 = relay.TupleGetItem(func_1488_call(), 0)
call_6582 = relay.TupleGetItem(func_1489_call(), 0)
func_5873_call = mod.get_global_var('func_5873')
func_5875_call = mutated_mod.get_global_var('func_5875')
call_6603 = func_5873_call()
call_6604 = func_5873_call()
output = relay.Tuple([call_6581,call_6603,])
output2 = relay.Tuple([call_6582,call_6604,])
func_6615 = relay.Function([], output)
mod['func_6615'] = func_6615
mod = relay.transform.InferType()(mod)
output = func_6615()
func_6616 = relay.Function([], output)
mutated_mod['func_6616'] = func_6616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6615_call = mod.get_global_var('func_6615')
func_6616_call = mutated_mod.get_global_var('func_6616')
call_6631 = relay.TupleGetItem(func_6615_call(), 0)
call_6632 = relay.TupleGetItem(func_6616_call(), 0)
output = call_6631
output2 = call_6632
func_6638 = relay.Function([], output)
mod['func_6638'] = func_6638
mod = relay.transform.InferType()(mod)
output = func_6638()
func_6639 = relay.Function([], output)
mutated_mod['func_6639'] = func_6639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6510_call = mod.get_global_var('func_6510')
func_6512_call = mutated_mod.get_global_var('func_6512')
call_6652 = relay.TupleGetItem(func_6510_call(), 0)
call_6653 = relay.TupleGetItem(func_6512_call(), 0)
output = call_6652
output2 = call_6653
func_6664 = relay.Function([], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
mutated_mod['func_6664'] = func_6664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6664_call = mutated_mod.get_global_var('func_6664')
call_6665 = func_6664_call()
output = call_6665
func_6666 = relay.Function([], output)
mutated_mod['func_6666'] = func_6666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_6669 = relay.TupleGetItem(func_2454_call(), 0)
call_6670 = relay.TupleGetItem(func_2456_call(), 0)
func_6021_call = mod.get_global_var('func_6021')
func_6022_call = mutated_mod.get_global_var('func_6022')
call_6690 = relay.TupleGetItem(func_6021_call(), 2)
call_6691 = relay.TupleGetItem(func_6022_call(), 2)
output = relay.Tuple([call_6669,call_6690,])
output2 = relay.Tuple([call_6670,call_6691,])
func_6693 = relay.Function([], output)
mod['func_6693'] = func_6693
mod = relay.transform.InferType()(mod)
mutated_mod['func_6693'] = func_6693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6693_call = mutated_mod.get_global_var('func_6693')
call_6694 = func_6693_call()
output = call_6694
func_6695 = relay.Function([], output)
mutated_mod['func_6695'] = func_6695
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_6707 = relay.TupleGetItem(func_5192_call(), 0)
call_6708 = relay.TupleGetItem(func_5193_call(), 0)
output = relay.Tuple([call_6707,])
output2 = relay.Tuple([call_6708,])
func_6739 = relay.Function([], output)
mod['func_6739'] = func_6739
mod = relay.transform.InferType()(mod)
mutated_mod['func_6739'] = func_6739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mutated_mod.get_global_var('func_6739')
call_6740 = func_6739_call()
output = call_6740
func_6741 = relay.Function([], output)
mutated_mod['func_6741'] = func_6741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_902_call = mod.get_global_var('func_902')
func_904_call = mutated_mod.get_global_var('func_904')
call_6767 = relay.TupleGetItem(func_902_call(), 0)
call_6768 = relay.TupleGetItem(func_904_call(), 0)
func_5724_call = mod.get_global_var('func_5724')
func_5726_call = mutated_mod.get_global_var('func_5726')
const_6770 = relay.const([5.964868,0.278343,4.736986,-9.275297,-8.669577,-4.007472,-9.344725,6.125754,-9.499597,-2.643860,-0.577003,-3.096255,3.926777,4.328972,9.644305,-1.013290,-6.239868,-5.095060,3.931891,-5.211180,7.906065,-7.205140,3.513927,0.915331,3.024331,4.968070,-5.765170,3.444455,9.487962,-8.033613,4.395876,2.643269,2.504950,3.150475,-6.117498,-6.379199,-5.700142,-4.587876,-2.034041,-5.771027,6.562029,-4.091093,6.935388,-8.852706,-1.998266,1.447749,0.651489,7.971677,7.276821,2.070438,8.616812,3.864688,-4.610780,6.653759,-4.728001,-6.649401,5.246075,1.296041,-9.620392,5.720150,-0.031392,-6.695024,7.408791,-2.443739,-0.839734,3.451697,3.845076,-1.099546,-0.891806,7.536538,7.337831,-4.033140,-2.659286,1.337198,1.447750,0.609656,-0.236208,6.123801,-4.899059,-5.751346,-4.150217,-6.825602,-7.116641,5.264654,-4.603183,8.119206,7.529702,-9.861249,3.154558,-9.511455,-5.057636,7.130451,-3.517020,-2.708907,-7.512106,9.801557,-3.273217,9.149284,-9.743142,1.013046,5.397446,-5.639526,8.511116,-8.153336,9.810408,3.049385,-5.880960,-4.881848,-9.232318,4.849072,5.998990,1.525747,-8.850357,-1.241047,6.522657,4.071696,8.323540,3.870304,-2.965434,1.354499,4.161520,7.928068,8.320522,-1.859616,2.313791,7.523850,-4.604427,-5.301151,7.901712,-1.078824,7.355166,7.298550,9.067007,8.109420,-3.415503,1.065594,9.648620,1.039615,-1.764096,-6.772925,-2.711738,-7.459238,-3.017783,8.400261,-2.960756,1.803494,-3.088424,-3.439252,5.338739,8.690042,-9.599863,1.357370,-4.950704,6.826664,-0.018146,-2.481711,2.771229,-5.292212,0.889113,1.222729,3.487860,7.925831,8.457822,3.780447,5.908646,-1.378949,-1.458064,-9.853312,-6.775619,6.957684,2.614654,0.465942,9.668200,7.864261,-4.972641,-0.845565,1.176436,8.665552,6.463880,9.685156,5.185529,-4.272444,-3.137432,-3.224395,-8.426020,2.827076,5.541304,-0.775813,-1.440182,-0.280517,-3.344865,-5.708295,-1.235339,-6.999072,9.952753,8.666114,0.145553,-5.777331,-9.211780,8.529883,-6.609996,-3.929931,1.576371,-9.286833,-7.778897,-5.160963,4.814707,-9.007907,-2.663481,7.769255,9.756851,8.298906,6.112462,-8.790720,-8.675850,-0.909535,-1.504309,9.308042,-8.974630,-6.124887,-3.003187,1.056494,9.524747,8.273182,5.983431,1.813786,0.280609,6.812643,-2.912093,-5.814112,6.947550,-9.297136,-4.693745,-4.113571], dtype = "float64")#candidate|6770|(234,)|const|float64
call_6769 = relay.TupleGetItem(func_5724_call(relay.reshape(const_6770.astype('float64'), [234,])), 0)
call_6771 = relay.TupleGetItem(func_5726_call(relay.reshape(const_6770.astype('float64'), [234,])), 0)
func_5520_call = mod.get_global_var('func_5520')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_6778 = relay.TupleGetItem(func_5520_call(), 1)
call_6779 = relay.TupleGetItem(func_5522_call(), 1)
func_5904_call = mod.get_global_var('func_5904')
func_5906_call = mutated_mod.get_global_var('func_5906')
call_6797 = func_5904_call()
call_6798 = func_5904_call()
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_6807 = func_650_call()
call_6808 = func_650_call()
output = relay.Tuple([call_6767,call_6769,const_6770,call_6778,call_6797,call_6807,])
output2 = relay.Tuple([call_6768,call_6771,const_6770,call_6779,call_6798,call_6808,])
func_6812 = relay.Function([], output)
mod['func_6812'] = func_6812
mod = relay.transform.InferType()(mod)
mutated_mod['func_6812'] = func_6812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mutated_mod.get_global_var('func_6812')
call_6813 = func_6812_call()
output = call_6813
func_6814 = relay.Function([], output)
mutated_mod['func_6814'] = func_6814
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6822 = relay.var("var_6822", dtype = "float32", shape = (4, 8, 15))#candidate|6822|(4, 8, 15)|var|float32
uop_6823 = relay.erf(var_6822.astype('float32')) # shape=(4, 8, 15)
output = uop_6823
output2 = uop_6823
func_6847 = relay.Function([var_6822,], output)
mod['func_6847'] = func_6847
mod = relay.transform.InferType()(mod)
var_6848 = relay.var("var_6848", dtype = "float32", shape = (4, 8, 15))#candidate|6848|(4, 8, 15)|var|float32
output = func_6847(var_6848)
func_6849 = relay.Function([var_6848], output)
mutated_mod['func_6849'] = func_6849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_6853 = relay.TupleGetItem(func_6812_call(), 4)
call_6854 = relay.TupleGetItem(func_6814_call(), 4)
func_3656_call = mod.get_global_var('func_3656')
func_3659_call = mutated_mod.get_global_var('func_3659')
const_6891 = relay.const([[8.952357,-2.532724,-8.850244,0.557467,7.686756,-5.324805,7.790745],[9.409526,-8.503597,-7.063530,-3.835882,4.642342,-9.472782,5.918059],[4.189425,8.166168,-9.465688,-6.251009,2.576118,1.257145,-9.443892],[3.278435,-6.405361,-9.972363,-3.252562,-3.787272,0.597870,5.530228],[-9.536933,-9.984856,-7.011181,-2.672509,2.349867,3.361499,-0.059133],[9.917922,2.665978,-3.719276,6.980329,-6.242833,0.702853,7.682554],[-5.009657,-9.152346,0.774923,-7.724264,-2.674806,-4.420504,9.448978],[-0.839522,-2.788560,-4.425249,-6.549586,-7.397889,-4.188274,-2.780330],[1.654203,-9.735247,-2.987028,-6.326361,9.042564,2.797550,5.226912],[-4.727616,-0.478585,-3.324639,-7.644045,-2.624155,8.114048,2.632440],[3.665170,9.189618,3.156344,-0.990841,-9.614254,1.427084,-8.472996]], dtype = "float32")#candidate|6891|(11, 7)|const|float32
call_6890 = relay.TupleGetItem(func_3656_call(relay.reshape(const_6891.astype('float32'), [1, 77])), 3)
call_6892 = relay.TupleGetItem(func_3659_call(relay.reshape(const_6891.astype('float32'), [1, 77])), 3)
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_6906 = relay.TupleGetItem(func_677_call(), 0)
call_6907 = relay.TupleGetItem(func_679_call(), 0)
output = relay.Tuple([call_6853,call_6890,const_6891,call_6906,])
output2 = relay.Tuple([call_6854,call_6892,const_6891,call_6907,])
func_6913 = relay.Function([], output)
mod['func_6913'] = func_6913
mod = relay.transform.InferType()(mod)
output = func_6913()
func_6914 = relay.Function([], output)
mutated_mod['func_6914'] = func_6914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2940_call = mod.get_global_var('func_2940')
func_2942_call = mutated_mod.get_global_var('func_2942')
call_6931 = relay.TupleGetItem(func_2940_call(), 0)
call_6932 = relay.TupleGetItem(func_2942_call(), 0)
func_2557_call = mod.get_global_var('func_2557')
func_2561_call = mutated_mod.get_global_var('func_2561')
const_6936 = relay.const([-1.899296,-5.020941,-7.411464,1.577471,-6.233950,7.590654,3.084694,-7.032405,6.872183,2.052294,8.093282,7.271775,6.032448,-8.646272,-7.964262,0.143103,-9.811239,8.422472,2.118794,-6.960939,-1.635797,-4.369349,1.493235,9.513107,-1.723060,-3.340981,-2.934973,5.460165,-5.127359,-5.183998,-2.184238,3.817426,-4.477884,1.240575,-3.764630,0.613964,1.906162,-7.577914,0.624810,-2.093543,-4.579271,6.897818,-2.180835,3.530909,1.780238,1.626084,5.931338,-3.665486,-9.726424,-0.575299,5.469178,9.820843,2.880296,2.951322,2.966548,-9.946121,-5.740266,1.794225,-0.981643,0.857517,-8.739206,-2.801903,-7.840797,1.519366,-7.412436,1.306101,-9.017354,1.845420,-5.772621,-8.524575,-5.004192,-0.498897,-8.300776,0.921679,-1.177400,-8.976688,8.658831], dtype = "float32")#candidate|6936|(77,)|const|float32
var_6937 = relay.var("var_6937", dtype = "float32", shape = (154,))#candidate|6937|(154,)|var|float32
call_6935 = relay.TupleGetItem(func_2557_call(relay.reshape(const_6936.astype('float32'), [1, 77]), relay.reshape(var_6937.astype('float32'), [154,]), ), 1)
call_6938 = relay.TupleGetItem(func_2561_call(relay.reshape(const_6936.astype('float32'), [1, 77]), relay.reshape(var_6937.astype('float32'), [154,]), ), 1)
var_6945 = relay.var("var_6945", dtype = "float32", shape = (77,))#candidate|6945|(77,)|var|float32
bop_6946 = relay.logical_or(const_6936.astype('bool'), relay.reshape(var_6945.astype('bool'), relay.shape_of(const_6936))) # shape=(77,)
output = relay.Tuple([call_6931,call_6935,var_6937,bop_6946,])
output2 = relay.Tuple([call_6932,call_6938,var_6937,bop_6946,])
func_6969 = relay.Function([var_6937,var_6945,], output)
mod['func_6969'] = func_6969
mod = relay.transform.InferType()(mod)
var_6970 = relay.var("var_6970", dtype = "float32", shape = (154,))#candidate|6970|(154,)|var|float32
var_6971 = relay.var("var_6971", dtype = "float32", shape = (77,))#candidate|6971|(77,)|var|float32
output = func_6969(var_6970,var_6971,)
func_6972 = relay.Function([var_6970,var_6971,], output)
mutated_mod['func_6972'] = func_6972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4313_call = mod.get_global_var('func_4313')
func_4314_call = mutated_mod.get_global_var('func_4314')
call_6979 = relay.TupleGetItem(func_4313_call(), 0)
call_6980 = relay.TupleGetItem(func_4314_call(), 0)
func_1154_call = mod.get_global_var('func_1154')
func_1156_call = mutated_mod.get_global_var('func_1156')
var_6982 = relay.var("var_6982", dtype = "float64", shape = (234,))#candidate|6982|(234,)|var|float64
call_6981 = relay.TupleGetItem(func_1154_call(relay.reshape(var_6982.astype('float64'), [234,])), 0)
call_6983 = relay.TupleGetItem(func_1156_call(relay.reshape(var_6982.astype('float64'), [234,])), 0)
output = relay.Tuple([call_6979,call_6981,var_6982,])
output2 = relay.Tuple([call_6980,call_6983,var_6982,])
func_7011 = relay.Function([var_6982,], output)
mod['func_7011'] = func_7011
mod = relay.transform.InferType()(mod)
var_7012 = relay.var("var_7012", dtype = "float64", shape = (234,))#candidate|7012|(234,)|var|float64
output = func_7011(var_7012)
func_7013 = relay.Function([var_7012], output)
mutated_mod['func_7013'] = func_7013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3781_call = mutated_mod.get_global_var('func_3781')
call_7048 = func_3779_call()
call_7049 = func_3779_call()
func_1822_call = mod.get_global_var('func_1822')
func_1826_call = mutated_mod.get_global_var('func_1826')
var_7081 = relay.var("var_7081", dtype = "uint64", shape = ())#candidate|7081|()|var|uint64
const_7082 = relay.const([3,6,-1,2,3,-5,7,-7,-5,-2,3,7,-9,5,-8,-8,10,-6,-4,-9,10,10,-6,-4,5,7,8,-3,-7,-8,7,-7,1,-1,2,4,4,1,-10,-10,-9,-2,5,7,-6,-6,-2,-3,8,7,-6,4,-4,1,-10,-8,-7,7,6,3,-8,6,-4,2,-4,2,10,1,10,8,10,8,-4,9,-8,3,-1,-7,-1,7,-10,7,-2,3,-8,-2,5,-8,-3,-1,1,-1,7,7,9,-3,-2,8,-9,-8,2,-9,-7,5,4,-5,2,-9,-5,8,2,-4,4,-10,3,-1,-7,-1,7,-6,-4,8,-6,6,5,5,5,-2,1,3,-10,-10,-5,9,9], dtype = "uint64")#candidate|7082|(135,)|const|uint64
call_7080 = func_1822_call(relay.reshape(var_7081.astype('uint64'), []), relay.reshape(const_7082.astype('uint64'), [15, 9, 1]), )
call_7083 = func_1822_call(relay.reshape(var_7081.astype('uint64'), []), relay.reshape(const_7082.astype('uint64'), [15, 9, 1]), )
output = relay.Tuple([call_7048,call_7080,var_7081,const_7082,])
output2 = relay.Tuple([call_7049,call_7083,var_7081,const_7082,])
func_7090 = relay.Function([var_7081,], output)
mod['func_7090'] = func_7090
mod = relay.transform.InferType()(mod)
var_7091 = relay.var("var_7091", dtype = "uint64", shape = ())#candidate|7091|()|var|uint64
output = func_7090(var_7091)
func_7092 = relay.Function([var_7091], output)
mutated_mod['func_7092'] = func_7092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4920_call = mod.get_global_var('func_4920')
func_4921_call = mutated_mod.get_global_var('func_4921')
call_7107 = relay.TupleGetItem(func_4920_call(), 0)
call_7108 = relay.TupleGetItem(func_4921_call(), 0)
output = call_7107
output2 = call_7108
func_7132 = relay.Function([], output)
mod['func_7132'] = func_7132
mod = relay.transform.InferType()(mod)
output = func_7132()
func_7133 = relay.Function([], output)
mutated_mod['func_7133'] = func_7133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5589_call = mod.get_global_var('func_5589')
func_5590_call = mutated_mod.get_global_var('func_5590')
call_7187 = relay.TupleGetItem(func_5589_call(), 2)
call_7188 = relay.TupleGetItem(func_5590_call(), 2)
output = call_7187
output2 = call_7188
func_7207 = relay.Function([], output)
mod['func_7207'] = func_7207
mod = relay.transform.InferType()(mod)
mutated_mod['func_7207'] = func_7207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7207_call = mutated_mod.get_global_var('func_7207')
call_7208 = func_7207_call()
output = call_7208
func_7209 = relay.Function([], output)
mutated_mod['func_7209'] = func_7209
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7273 = relay.var("var_7273", dtype = "float32", shape = (5, 14, 15))#candidate|7273|(5, 14, 15)|var|float32
var_7274 = relay.var("var_7274", dtype = "float32", shape = (5, 14, 15))#candidate|7274|(5, 14, 15)|var|float32
bop_7275 = relay.floor_divide(var_7273.astype('float32'), relay.reshape(var_7274.astype('float32'), relay.shape_of(var_7273))) # shape=(5, 14, 15)
output = bop_7275
output2 = bop_7275
func_7281 = relay.Function([var_7273,var_7274,], output)
mod['func_7281'] = func_7281
mod = relay.transform.InferType()(mod)
mutated_mod['func_7281'] = func_7281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7281_call = mutated_mod.get_global_var('func_7281')
var_7283 = relay.var("var_7283", dtype = "float32", shape = (5, 14, 15))#candidate|7283|(5, 14, 15)|var|float32
var_7284 = relay.var("var_7284", dtype = "float32", shape = (5, 14, 15))#candidate|7284|(5, 14, 15)|var|float32
call_7282 = func_7281_call(var_7283,var_7284,)
output = call_7282
func_7285 = relay.Function([var_7283,var_7284,], output)
mutated_mod['func_7285'] = func_7285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_7295 = relay.TupleGetItem(func_5192_call(), 0)
call_7296 = relay.TupleGetItem(func_5193_call(), 0)
func_7011_call = mod.get_global_var('func_7011')
func_7013_call = mutated_mod.get_global_var('func_7013')
var_7312 = relay.var("var_7312", dtype = "float64", shape = (234,))#candidate|7312|(234,)|var|float64
call_7311 = relay.TupleGetItem(func_7011_call(relay.reshape(var_7312.astype('float64'), [234,])), 2)
call_7313 = relay.TupleGetItem(func_7013_call(relay.reshape(var_7312.astype('float64'), [234,])), 2)
bop_7316 = relay.subtract(call_7311.astype('uint64'), relay.reshape(var_7312.astype('uint64'), relay.shape_of(call_7311))) # shape=(234,)
bop_7319 = relay.subtract(call_7313.astype('uint64'), relay.reshape(var_7312.astype('uint64'), relay.shape_of(call_7313))) # shape=(234,)
output = relay.Tuple([call_7295,bop_7316,])
output2 = relay.Tuple([call_7296,bop_7319,])
func_7332 = relay.Function([var_7312,], output)
mod['func_7332'] = func_7332
mod = relay.transform.InferType()(mod)
mutated_mod['func_7332'] = func_7332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7333 = relay.var("var_7333", dtype = "float64", shape = (234,))#candidate|7333|(234,)|var|float64
func_7332_call = mutated_mod.get_global_var('func_7332')
call_7334 = func_7332_call(var_7333)
output = call_7334
func_7335 = relay.Function([var_7333], output)
mutated_mod['func_7335'] = func_7335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3428_call = mod.get_global_var('func_3428')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_7337 = relay.TupleGetItem(func_3428_call(), 0)
call_7338 = relay.TupleGetItem(func_3430_call(), 0)
func_4920_call = mod.get_global_var('func_4920')
func_4921_call = mutated_mod.get_global_var('func_4921')
call_7339 = relay.TupleGetItem(func_4920_call(), 0)
call_7340 = relay.TupleGetItem(func_4921_call(), 0)
func_6615_call = mod.get_global_var('func_6615')
func_6616_call = mutated_mod.get_global_var('func_6616')
call_7341 = relay.TupleGetItem(func_6615_call(), 1)
call_7342 = relay.TupleGetItem(func_6616_call(), 1)
func_3194_call = mod.get_global_var('func_3194')
func_3197_call = mutated_mod.get_global_var('func_3197')
var_7347 = relay.var("var_7347", dtype = "float32", shape = (77, 1))#candidate|7347|(77, 1)|var|float32
const_7348 = relay.const([[-7,4,-2,-9,6,4,-1,-6,-3,-4,9,-8,-5,5,-2,-4,7,4,3,-6,7,10],[6,10,-4,-6,2,-4,-10,4,2,-2,-6,-10,4,-9,-6,6,-6,5,-3,-2,5,-3],[-5,-7,-5,-9,5,-1,7,-9,10,9,4,-7,-5,3,5,2,-2,-8,-8,-1,8,4],[-3,-10,-8,8,-3,8,-4,-7,-6,-10,10,7,-6,-2,10,10,1,-6,-9,3,-1,-1],[4,5,-8,10,10,-7,8,1,-7,3,10,-9,8,-4,-4,6,-2,-10,4,10,1,-2],[-7,9,3,4,-3,-4,-6,2,3,10,6,8,1,-6,5,1,9,10,4,-7,8,10],[10,-7,-9,-10,8,7,-6,-4,-10,-5,-7,-3,8,9,-3,-3,2,-8,7,-10,-6,6],[9,-2,-5,8,-1,-2,-10,6,-2,8,9,7,-4,10,-3,1,-6,-10,4,-4,10,-6],[9,-6,3,6,-10,7,-1,3,5,7,10,4,-7,9,-6,-10,6,-9,9,-8,-10,2],[-4,-7,-10,-2,-4,-4,-9,-8,5,2,-5,-10,-6,-3,5,-10,-2,-10,3,-3,-8,-8],[10,-2,8,-8,-6,-7,-9,1,-6,3,-9,-10,-4,-9,-2,1,-7,-10,-10,-5,-9,9],[3,-3,2,-8,-10,-3,-3,-9,1,8,-3,-2,9,9,10,-9,7,-3,-8,10,-7,-2],[-7,-7,1,8,-6,-8,8,6,-5,-2,-4,3,-3,-2,8,-3,7,5,5,-5,-6,7],[-10,3,-7,10,-9,5,-10,4,-5,4,7,3,5,-5,8,-6,-5,6,5,5,-10,5],[9,7,6,-9,3,5,7,8,1,6,2,-8,-7,-10,-3,-9,6,-10,9,5,1,-9],[-9,-4,10,6,9,10,9,4,-7,-6,-1,5,-6,-2,-8,5,-8,8,8,-10,8,-4],[-10,-10,-1,9,-5,-4,3,-9,-6,10,3,2,2,10,-1,-8,3,9,-4,-10,3,9],[-9,-10,-3,1,-8,7,6,-3,-2,-2,-1,-2,7,4,-3,7,3,9,8,2,-4,10],[-8,8,6,-8,-9,1,-10,10,-10,-5,4,1,-3,-8,5,8,-10,7,6,-2,4,5],[-8,7,-1,5,8,7,-8,-2,-2,-8,5,-10,-1,-8,-4,8,5,4,-2,1,-2,5],[3,6,-6,-10,10,-3,-2,5,-3,10,10,6,-2,4,-5,-7,-6,6,5,-4,7,5],[8,5,-3,-1,-10,7,-4,-7,1,9,-5,9,10,7,1,-5,2,-10,7,-7,8,1],[4,3,10,-3,7,-6,-5,4,-5,-5,-3,1,6,-8,-4,10,-5,-3,7,9,-8,-10],[-8,-9,7,1,8,-9,1,-1,-4,-3,4,-3,4,4,9,-6,-10,1,6,-7,-5,9]], dtype = "int32")#candidate|7348|(24, 22)|const|int32
call_7346 = relay.TupleGetItem(func_3194_call(relay.reshape(var_7347.astype('float32'), [77,]), relay.reshape(const_7348.astype('int32'), [528,]), ), 8)
call_7349 = relay.TupleGetItem(func_3197_call(relay.reshape(var_7347.astype('float32'), [77,]), relay.reshape(const_7348.astype('int32'), [528,]), ), 8)
output = relay.Tuple([call_7337,call_7339,call_7341,call_7346,var_7347,const_7348,])
output2 = relay.Tuple([call_7338,call_7340,call_7342,call_7349,var_7347,const_7348,])
func_7365 = relay.Function([var_7347,], output)
mod['func_7365'] = func_7365
mod = relay.transform.InferType()(mod)
mutated_mod['func_7365'] = func_7365
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7366 = relay.var("var_7366", dtype = "float32", shape = (77, 1))#candidate|7366|(77, 1)|var|float32
func_7365_call = mutated_mod.get_global_var('func_7365')
call_7367 = func_7365_call(var_7366)
output = call_7367
func_7368 = relay.Function([var_7366], output)
mutated_mod['func_7368'] = func_7368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5520_call = mod.get_global_var('func_5520')
func_5522_call = mutated_mod.get_global_var('func_5522')
call_7412 = relay.TupleGetItem(func_5520_call(), 0)
call_7413 = relay.TupleGetItem(func_5522_call(), 0)
func_6021_call = mod.get_global_var('func_6021')
func_6022_call = mutated_mod.get_global_var('func_6022')
call_7433 = relay.TupleGetItem(func_6021_call(), 2)
call_7434 = relay.TupleGetItem(func_6022_call(), 2)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_7444 = relay.TupleGetItem(func_6812_call(), 0)
call_7445 = relay.TupleGetItem(func_6814_call(), 0)
func_6615_call = mod.get_global_var('func_6615')
func_6616_call = mutated_mod.get_global_var('func_6616')
call_7454 = relay.TupleGetItem(func_6615_call(), 1)
call_7455 = relay.TupleGetItem(func_6616_call(), 1)
output = relay.Tuple([call_7412,call_7433,call_7444,call_7454,])
output2 = relay.Tuple([call_7413,call_7434,call_7445,call_7455,])
func_7466 = relay.Function([], output)
mod['func_7466'] = func_7466
mod = relay.transform.InferType()(mod)
mutated_mod['func_7466'] = func_7466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7466_call = mutated_mod.get_global_var('func_7466')
call_7467 = func_7466_call()
output = call_7467
func_7468 = relay.Function([], output)
mutated_mod['func_7468'] = func_7468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_7518 = func_2815_call()
call_7519 = func_2815_call()
func_902_call = mod.get_global_var('func_902')
func_904_call = mutated_mod.get_global_var('func_904')
call_7540 = relay.TupleGetItem(func_902_call(), 0)
call_7541 = relay.TupleGetItem(func_904_call(), 0)
func_5873_call = mod.get_global_var('func_5873')
func_5875_call = mutated_mod.get_global_var('func_5875')
call_7557 = func_5873_call()
call_7558 = func_5873_call()
func_3428_call = mod.get_global_var('func_3428')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_7578 = relay.TupleGetItem(func_3428_call(), 0)
call_7579 = relay.TupleGetItem(func_3430_call(), 0)
output = relay.Tuple([call_7518,call_7540,call_7557,call_7578,])
output2 = relay.Tuple([call_7519,call_7541,call_7558,call_7579,])
func_7582 = relay.Function([], output)
mod['func_7582'] = func_7582
mod = relay.transform.InferType()(mod)
output = func_7582()
func_7583 = relay.Function([], output)
mutated_mod['func_7583'] = func_7583
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7635 = relay.const(True, dtype = "bool")#candidate|7635|()|const|bool
const_7636 = relay.const([[[False,True,False,True],[False,False,True,False],[False,True,False,True]],[[True,False,True,True],[False,True,True,False],[True,True,True,True]]], dtype = "bool")#candidate|7636|(2, 3, 4)|const|bool
bop_7637 = relay.logical_or(const_7635.astype('bool'), const_7636.astype('bool')) # shape=(2, 3, 4)
output = bop_7637
output2 = bop_7637
func_7644 = relay.Function([], output)
mod['func_7644'] = func_7644
mod = relay.transform.InferType()(mod)
mutated_mod['func_7644'] = func_7644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7644_call = mutated_mod.get_global_var('func_7644')
call_7645 = func_7644_call()
output = call_7645
func_7646 = relay.Function([], output)
mutated_mod['func_7646'] = func_7646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_7667 = relay.TupleGetItem(func_1736_call(), 0)
call_7668 = relay.TupleGetItem(func_1738_call(), 0)
output = call_7667
output2 = call_7668
func_7678 = relay.Function([], output)
mod['func_7678'] = func_7678
mod = relay.transform.InferType()(mod)
mutated_mod['func_7678'] = func_7678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7678_call = mutated_mod.get_global_var('func_7678')
call_7679 = func_7678_call()
output = call_7679
func_7680 = relay.Function([], output)
mutated_mod['func_7680'] = func_7680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6088_call = mod.get_global_var('func_6088')
func_6089_call = mutated_mod.get_global_var('func_6089')
call_7686 = relay.TupleGetItem(func_6088_call(), 2)
call_7687 = relay.TupleGetItem(func_6089_call(), 2)
output = call_7686
output2 = call_7687
func_7698 = relay.Function([], output)
mod['func_7698'] = func_7698
mod = relay.transform.InferType()(mod)
output = func_7698()
func_7699 = relay.Function([], output)
mutated_mod['func_7699'] = func_7699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_7714 = relay.TupleGetItem(func_1488_call(), 1)
call_7715 = relay.TupleGetItem(func_1489_call(), 1)
output = call_7714
output2 = call_7715
func_7726 = relay.Function([], output)
mod['func_7726'] = func_7726
mod = relay.transform.InferType()(mod)
output = func_7726()
func_7727 = relay.Function([], output)
mutated_mod['func_7727'] = func_7727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_7814 = relay.TupleGetItem(func_6739_call(), 0)
call_7815 = relay.TupleGetItem(func_6741_call(), 0)
func_1064_call = mod.get_global_var('func_1064')
func_1067_call = mutated_mod.get_global_var('func_1067')
var_7818 = relay.var("var_7818", dtype = "float32", shape = (11, 7))#candidate|7818|(11, 7)|var|float32
var_7819 = relay.var("var_7819", dtype = "float32", shape = (154,))#candidate|7819|(154,)|var|float32
call_7817 = relay.TupleGetItem(func_1064_call(relay.reshape(var_7818.astype('float32'), [77,]), relay.reshape(var_7819.astype('float32'), [154,]), ), 1)
call_7820 = relay.TupleGetItem(func_1067_call(relay.reshape(var_7818.astype('float32'), [77,]), relay.reshape(var_7819.astype('float32'), [154,]), ), 1)
output = relay.Tuple([call_7814,call_7817,var_7818,var_7819,])
output2 = relay.Tuple([call_7815,call_7820,var_7818,var_7819,])
func_7824 = relay.Function([var_7818,var_7819,], output)
mod['func_7824'] = func_7824
mod = relay.transform.InferType()(mod)
mutated_mod['func_7824'] = func_7824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7824_call = mutated_mod.get_global_var('func_7824')
var_7826 = relay.var("var_7826", dtype = "float32", shape = (11, 7))#candidate|7826|(11, 7)|var|float32
var_7827 = relay.var("var_7827", dtype = "float32", shape = (154,))#candidate|7827|(154,)|var|float32
call_7825 = func_7824_call(var_7826,var_7827,)
output = call_7825
func_7828 = relay.Function([var_7826,var_7827,], output)
mutated_mod['func_7828'] = func_7828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_7842 = relay.TupleGetItem(func_1736_call(), 0)
call_7843 = relay.TupleGetItem(func_1738_call(), 0)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_7848 = relay.TupleGetItem(func_2454_call(), 1)
call_7849 = relay.TupleGetItem(func_2456_call(), 1)
func_880_call = mod.get_global_var('func_880')
func_883_call = mutated_mod.get_global_var('func_883')
var_7855 = relay.var("var_7855", dtype = "float64", shape = (1, 234))#candidate|7855|(1, 234)|var|float64
call_7854 = relay.TupleGetItem(func_880_call(relay.reshape(var_7855.astype('float64'), [2, 13, 9]), relay.reshape(var_7855.astype('float64'), [2, 13, 9]), ), 0)
call_7856 = relay.TupleGetItem(func_883_call(relay.reshape(var_7855.astype('float64'), [2, 13, 9]), relay.reshape(var_7855.astype('float64'), [2, 13, 9]), ), 0)
output = relay.Tuple([call_7842,call_7848,call_7854,var_7855,])
output2 = relay.Tuple([call_7843,call_7849,call_7856,var_7855,])
func_7879 = relay.Function([var_7855,], output)
mod['func_7879'] = func_7879
mod = relay.transform.InferType()(mod)
mutated_mod['func_7879'] = func_7879
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7880 = relay.var("var_7880", dtype = "float64", shape = (1, 234))#candidate|7880|(1, 234)|var|float64
func_7879_call = mutated_mod.get_global_var('func_7879')
call_7881 = func_7879_call(var_7880)
output = call_7881
func_7882 = relay.Function([var_7880], output)
mutated_mod['func_7882'] = func_7882
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7726_call = mod.get_global_var('func_7726')
func_7727_call = mutated_mod.get_global_var('func_7727')
call_7886 = func_7726_call()
call_7887 = func_7726_call()
func_3428_call = mod.get_global_var('func_3428')
func_3430_call = mutated_mod.get_global_var('func_3430')
call_7924 = relay.TupleGetItem(func_3428_call(), 0)
call_7925 = relay.TupleGetItem(func_3430_call(), 0)
func_5162_call = mod.get_global_var('func_5162')
func_5164_call = mutated_mod.get_global_var('func_5164')
call_7926 = relay.TupleGetItem(func_5162_call(), 1)
call_7927 = relay.TupleGetItem(func_5164_call(), 1)
output = relay.Tuple([call_7886,call_7924,call_7926,])
output2 = relay.Tuple([call_7887,call_7925,call_7927,])
func_7932 = relay.Function([], output)
mod['func_7932'] = func_7932
mod = relay.transform.InferType()(mod)
output = func_7932()
func_7933 = relay.Function([], output)
mutated_mod['func_7933'] = func_7933
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7945 = relay.var("var_7945", dtype = "int64", shape = (2, 15, 3))#candidate|7945|(2, 15, 3)|var|int64
var_7946 = relay.var("var_7946", dtype = "int64", shape = (2, 15, 3))#candidate|7946|(2, 15, 3)|var|int64
bop_7947 = relay.left_shift(var_7945.astype('int64'), relay.reshape(var_7946.astype('int64'), relay.shape_of(var_7945))) # shape=(2, 15, 3)
bop_7959 = relay.logical_or(bop_7947.astype('bool'), relay.reshape(var_7945.astype('bool'), relay.shape_of(bop_7947))) # shape=(2, 15, 3)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_7967 = relay.TupleGetItem(func_2454_call(), 0)
call_7968 = relay.TupleGetItem(func_2456_call(), 0)
func_7281_call = mod.get_global_var('func_7281')
func_7285_call = mutated_mod.get_global_var('func_7285')
var_7975 = relay.var("var_7975", dtype = "float32", shape = (1050,))#candidate|7975|(1050,)|var|float32
call_7974 = func_7281_call(relay.reshape(var_7975.astype('float32'), [5, 14, 15]), relay.reshape(var_7975.astype('float32'), [5, 14, 15]), )
call_7976 = func_7281_call(relay.reshape(var_7975.astype('float32'), [5, 14, 15]), relay.reshape(var_7975.astype('float32'), [5, 14, 15]), )
func_4803_call = mod.get_global_var('func_4803')
func_4805_call = mutated_mod.get_global_var('func_4805')
call_7980 = func_4803_call()
call_7981 = func_4803_call()
var_7989 = relay.var("var_7989", dtype = "bool", shape = (2, 15, 3))#candidate|7989|(2, 15, 3)|var|bool
bop_7990 = relay.floor_divide(bop_7959.astype('float32'), relay.reshape(var_7989.astype('float32'), relay.shape_of(bop_7959))) # shape=(2, 15, 3)
func_5440_call = mod.get_global_var('func_5440')
func_5442_call = mutated_mod.get_global_var('func_5442')
call_7993 = relay.TupleGetItem(func_5440_call(), 0)
call_7994 = relay.TupleGetItem(func_5442_call(), 0)
output = relay.Tuple([call_7967,call_7974,var_7975,call_7980,bop_7990,call_7993,])
output2 = relay.Tuple([call_7968,call_7976,var_7975,call_7981,bop_7990,call_7994,])
func_8006 = relay.Function([var_7945,var_7946,var_7975,var_7989,], output)
mod['func_8006'] = func_8006
mod = relay.transform.InferType()(mod)
mutated_mod['func_8006'] = func_8006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8006_call = mutated_mod.get_global_var('func_8006')
var_8008 = relay.var("var_8008", dtype = "int64", shape = (2, 15, 3))#candidate|8008|(2, 15, 3)|var|int64
var_8009 = relay.var("var_8009", dtype = "int64", shape = (2, 15, 3))#candidate|8009|(2, 15, 3)|var|int64
var_8010 = relay.var("var_8010", dtype = "float32", shape = (1050,))#candidate|8010|(1050,)|var|float32
var_8011 = relay.var("var_8011", dtype = "bool", shape = (2, 15, 3))#candidate|8011|(2, 15, 3)|var|bool
call_8007 = func_8006_call(var_8008,var_8009,var_8010,var_8011,)
output = call_8007
func_8012 = relay.Function([var_8008,var_8009,var_8010,var_8011,], output)
mutated_mod['func_8012'] = func_8012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3706_call = mod.get_global_var('func_3706')
func_3707_call = mutated_mod.get_global_var('func_3707')
call_8019 = func_3706_call()
call_8020 = func_3706_call()
var_8054 = relay.var("var_8054", dtype = "bool", shape = (5, 10))#candidate|8054|(5, 10)|var|bool
bop_8055 = relay.less_equal(call_8019.astype('bool'), var_8054.astype('bool')) # shape=(5, 10)
bop_8058 = relay.less_equal(call_8020.astype('bool'), var_8054.astype('bool')) # shape=(5, 10)
func_6847_call = mod.get_global_var('func_6847')
func_6849_call = mutated_mod.get_global_var('func_6849')
const_8083 = relay.const([[1.519769,5.241996,-0.333787,4.187143,-7.208561,-0.139115,5.818851,-9.855405,1.058650,0.571353,-7.378663,-2.172764,-3.514401,-3.524310,3.953790,2.007983,-7.412246,6.235792,-4.907539,-2.416970,3.815243,5.956754,-8.908554,4.099633,6.947923,6.474115,-8.387102,-7.471475,5.125284,-3.351826,-9.780994,-8.558697,-0.303233,4.595459,-3.138476,2.301562,-1.149587,-7.059640,-8.565725,8.735171,-2.665652,-0.627101,-5.549864,1.324137,8.729269,-1.957311,2.431213,-8.085001,-7.074512,6.568588,8.759432,4.400604,0.295685,5.285344,0.795025,0.429891,4.900687,-4.994809,4.864294,6.816587,9.479256,-1.441659,-3.804537,5.238711,1.081315,6.952695,9.146462,-1.912182,-3.521791,4.280431,-8.111913,3.536479,-0.117735,4.580107,9.568056,-9.477147,-3.058926,-1.111583,3.205206,-0.290006,-5.555140,9.397526,-7.116098,-6.855380,9.798434,-0.631755,1.028216,9.146016,6.759381,2.750647,-5.559439,-3.534010,-8.427983,2.444002,-4.779971,-5.819288,-5.671548,-3.955354,-1.502798,1.712210,-2.343165,6.045060,-6.922100,2.294224,-2.756596,-4.385932,-8.061221,0.694742,8.422706,-9.120345,-2.397635,-3.053929,7.387807,4.033532,-0.117816,5.599990,-9.062878,-8.234475,-2.502732,2.182280,-3.403025,6.647218,-7.106642,3.723878,7.878264,5.883171,0.505884,-4.154141,-7.975550,-3.418292,5.436696,-8.143920,-0.438281,-5.389030,-9.887533,8.620179,0.451395,-6.532013,-3.832038,-0.519167,6.054628,9.710807,9.446041,6.418192,-9.373502,-0.753555,-4.753307,1.035830,9.782967,2.214382,4.054589,-2.557040,5.403844,-7.347506,9.937460,0.826171,-6.814705,9.248585,2.001653,-9.009531,-7.553209,6.253618,5.152069,5.139394,-2.920062,-7.826638,-7.161039,-2.197629,3.437810,6.803259,8.359178,-0.529954,1.770804,-4.326710,-3.819317,-0.178431,7.687416,9.304004,0.608064,-4.495840,1.729249,2.918070,4.733724,3.809045,4.593731,3.701691,-8.796573,-4.093526,8.081013,-3.675943,9.173140,-5.217999,-5.199667,3.119609,4.207604,7.697092,5.290654,-4.171431,-9.984600,4.190387,-7.241003,8.818020,-4.178060,-0.036944,-2.693062,-0.082171,-2.984581,-3.768577,-1.614500,-1.952998,9.982475,9.617307,-0.501593,-5.736769,6.974585,-3.532899,-0.426067,-5.634652,-5.996358,0.438725,2.170169,-2.956593,-1.347877,-9.919743,5.584627,-6.469085,-2.568064,0.017327,6.065844,-2.529559,1.637045,-7.079554,-7.784450,8.285260,-9.520651,9.743858,-6.257891,0.862371,-3.914490,4.861591,-1.548594,7.371278,7.144158,9.564462,-8.007757,-8.570066,5.606850,8.652109,2.692257,-5.657938,2.475910,-5.539507,1.021125,0.088434,9.102682,3.517267,-5.769877,5.335797,5.991375,0.493106,-2.506359,-6.877816,-8.745021,5.524542,-2.724201,5.820543,8.324031,5.302918,2.520777,-1.003441,9.954667,-4.787099,-2.313302,-1.500265,4.995284,9.808464,8.114632,4.073410,-8.524387,2.437063,-7.457692,-6.950946,-9.412420,-6.972739,-1.914787,5.441763,4.742812,-5.016503,6.935793,9.224519,-3.670190,-5.447869,-0.959385,1.947049,-2.878641,7.958691,-7.807869,-0.339272,3.656843,-7.802770,0.629063,-9.252079,-8.703948,4.991100,9.563161,-6.820547,0.636192,3.482675,-3.579235,-2.345289,9.810944,7.750016,-4.176928,5.055544,-4.146963,2.148851,4.826332,-3.605326,-9.729016,2.278730,2.813899,0.402403,-6.831428,-8.110713,-3.262839,8.918482,9.635484,8.933340,-8.275552,4.039964,-8.951082,-0.530715,-4.296187,4.840463,-6.614399,-1.541851,-0.052498,1.878544,-2.907830,2.991910,-2.034357,0.153403,9.727556,9.003045,9.002413,4.416004,-1.855995,0.734224,-5.201527,9.856148,0.141502,-4.392240,-5.961746,-7.212009,-9.375553,7.725406,-4.721893,-4.214787,0.773071,7.152011,-7.308035,-1.664903,-6.882661,-3.930996,9.354520,-1.323292,9.134042,-8.838079,-6.802213,6.290391,9.097469,4.445288,3.347566,8.483611,-8.465025,9.522912,0.255982,1.689891,4.009272,6.168357,9.848908,5.448026,-1.712923,-9.835554,-3.965620,1.773838,-3.035943,8.830164,-7.859698,-6.540254,9.228087,-7.139635,-6.842482,-4.283518,1.725202,-2.601524,1.185741,7.342544,5.243596,-1.996068,7.884248,0.149902,4.965448,8.409618,-0.751480,-3.516940,7.814700,-6.194545,-8.310274,9.886615,-4.024908,-5.316935,7.028147,-3.977827,-6.495900,-8.660097,-5.045314,2.546672,-7.411228,-1.269676,3.959842,-9.785196,8.796320,-3.313517,-5.516675,4.829617,5.606474,-3.932569,2.807836,6.421171,-0.436840,-8.878805,-0.041982,-1.807343,-4.238864,2.871661,1.278119,7.141393,-5.056314,-3.798789,0.591166,-8.265568,1.454639,-3.753130,1.552005,-3.997831,8.199033,-0.165990,3.921807,8.637160,6.000592,0.744622,-9.046581,4.235130,-6.845259,8.301435,7.401587,-7.525186,2.282049,-7.932989,-2.871000,-2.071852,7.365831,8.616254,2.832245,-1.569709,8.321852,8.441742,-8.847157,9.159381,-6.293354,7.274126,-8.242506,-1.948203,-2.518324,-1.109846,-8.741533,-2.946513,9.951393,-5.999458]], dtype = "float32")#candidate|8083|(1, 480)|const|float32
call_8082 = func_6847_call(relay.reshape(const_8083.astype('float32'), [4, 8, 15]))
call_8084 = func_6847_call(relay.reshape(const_8083.astype('float32'), [4, 8, 15]))
func_3993_call = mod.get_global_var('func_3993')
func_3996_call = mutated_mod.get_global_var('func_3996')
var_8093 = relay.var("var_8093", dtype = "float32", shape = (8,))#candidate|8093|(8,)|var|float32
call_8092 = func_3993_call(relay.reshape(var_8093.astype('float32'), [8, 1, 1]))
call_8094 = func_3993_call(relay.reshape(var_8093.astype('float32'), [8, 1, 1]))
output = relay.Tuple([bop_8055,call_8082,const_8083,call_8092,var_8093,])
output2 = relay.Tuple([bop_8058,call_8084,const_8083,call_8094,var_8093,])
func_8097 = relay.Function([var_8054,var_8093,], output)
mod['func_8097'] = func_8097
mod = relay.transform.InferType()(mod)
mutated_mod['func_8097'] = func_8097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8097_call = mutated_mod.get_global_var('func_8097')
var_8099 = relay.var("var_8099", dtype = "bool", shape = (5, 10))#candidate|8099|(5, 10)|var|bool
var_8100 = relay.var("var_8100", dtype = "float32", shape = (8,))#candidate|8100|(8,)|var|float32
call_8098 = func_8097_call(var_8099,var_8100,)
output = call_8098
func_8101 = relay.Function([var_8099,var_8100,], output)
mutated_mod['func_8101'] = func_8101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mod.get_global_var('func_4786')
func_4788_call = mutated_mod.get_global_var('func_4788')
call_8113 = relay.TupleGetItem(func_4786_call(), 1)
call_8114 = relay.TupleGetItem(func_4788_call(), 1)
output = relay.Tuple([call_8113,])
output2 = relay.Tuple([call_8114,])
func_8130 = relay.Function([], output)
mod['func_8130'] = func_8130
mod = relay.transform.InferType()(mod)
output = func_8130()
func_8131 = relay.Function([], output)
mutated_mod['func_8131'] = func_8131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_589_call = mod.get_global_var('func_589')
func_590_call = mutated_mod.get_global_var('func_590')
call_8164 = relay.TupleGetItem(func_589_call(), 0)
call_8165 = relay.TupleGetItem(func_590_call(), 0)
func_8130_call = mod.get_global_var('func_8130')
func_8131_call = mutated_mod.get_global_var('func_8131')
call_8166 = relay.TupleGetItem(func_8130_call(), 0)
call_8167 = relay.TupleGetItem(func_8131_call(), 0)
func_938_call = mod.get_global_var('func_938')
func_939_call = mutated_mod.get_global_var('func_939')
call_8168 = relay.TupleGetItem(func_938_call(), 0)
call_8169 = relay.TupleGetItem(func_939_call(), 0)
output = relay.Tuple([call_8164,call_8166,call_8168,])
output2 = relay.Tuple([call_8165,call_8167,call_8169,])
func_8185 = relay.Function([], output)
mod['func_8185'] = func_8185
mod = relay.transform.InferType()(mod)
output = func_8185()
func_8186 = relay.Function([], output)
mutated_mod['func_8186'] = func_8186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1713_call = mod.get_global_var('func_1713')
func_1715_call = mutated_mod.get_global_var('func_1715')
call_8207 = relay.TupleGetItem(func_1713_call(), 4)
call_8208 = relay.TupleGetItem(func_1715_call(), 4)
func_5724_call = mod.get_global_var('func_5724')
func_5726_call = mutated_mod.get_global_var('func_5726')
var_8214 = relay.var("var_8214", dtype = "float64", shape = (234,))#candidate|8214|(234,)|var|float64
call_8213 = relay.TupleGetItem(func_5724_call(relay.reshape(var_8214.astype('float64'), [234,])), 2)
call_8215 = relay.TupleGetItem(func_5726_call(relay.reshape(var_8214.astype('float64'), [234,])), 2)
func_6969_call = mod.get_global_var('func_6969')
func_6972_call = mutated_mod.get_global_var('func_6972')
const_8231 = relay.const([[2.443056,2.545918,7.750133,-8.367990,-0.983737,-3.687545,-9.302609],[-3.708344,-8.927552,-1.872058,4.117338,7.753682,4.206583,8.629327],[4.376339,8.884108,6.081452,-2.767881,-1.170498,0.665091,1.709676],[0.161822,-5.947633,-1.174232,-6.817327,-7.141886,4.447702,-3.003647],[-0.718605,-1.863657,-0.299634,-1.909520,2.847356,3.091938,0.251571],[-3.266831,-3.037208,-3.501569,1.501887,9.953444,-3.383244,7.367904],[-5.689813,-5.160932,-7.462978,-2.581167,3.676624,-6.575750,7.578440],[-9.435783,-9.421863,3.222558,-9.870132,8.609528,-4.615750,-2.461705],[-1.693828,-1.084707,3.036643,9.773328,2.074012,-9.925400,-3.860204],[4.653047,-9.711489,6.335754,-2.376931,-6.290651,-2.163288,-4.840129],[-7.890187,9.999340,8.883711,5.638900,1.413854,-3.342216,-0.720744],[1.333811,6.010206,-3.847801,-8.234309,-1.962777,-0.497824,6.155376],[-1.536752,3.906914,-1.434763,6.216588,-4.433782,-7.565904,7.893301],[1.123640,-0.633753,-5.797427,8.210999,1.758743,-7.183382,7.321016],[-1.819894,-8.986559,-4.478064,-1.145361,-2.300542,-8.165217,-0.413619],[-7.612555,4.918722,-5.023032,-8.349776,4.481960,2.606384,7.592827],[-2.558035,5.931596,-1.090824,4.516942,6.726255,1.897453,3.813351],[0.756786,3.925527,4.605229,6.123083,-3.749188,8.628245,1.086740],[-9.162025,-2.339967,5.503976,-9.718153,6.147207,4.398761,0.495172],[1.553983,-6.595165,-6.346103,-7.848892,6.305601,2.349480,-0.817307],[0.192111,-6.353546,-8.415832,7.965458,-4.396905,8.077842,3.248391],[-4.070476,-8.235782,-9.139951,-7.626405,-1.925980,-3.133273,-8.431693]], dtype = "float32")#candidate|8231|(22, 7)|const|float32
const_8232 = relay.const([9.287281,-0.805007,-7.229734,3.126591,1.949753,-1.838490,5.962908,6.727314,-4.738368,8.017016,6.344440,-2.408193,5.737888,1.674531,6.988937,0.403981,-9.535294,-9.824247,5.153305,2.481788,6.652291,-4.189629,1.706760,-8.831648,3.308421,-8.418508,8.788756,-5.381739,-0.420430,4.435575,-8.554405,-1.352190,-9.830174,1.551429,-1.248254,3.921889,-0.212071,6.639236,6.030931,-9.167472,0.293374,2.076542,7.147212,9.286963,-7.973642,6.878190,2.041381,0.549695,-4.935355,-3.945769,-0.285471,-6.173311,5.308192,-3.107211,4.608276,7.687247,4.470234,8.558251,-8.947117,-3.631797,7.874341,9.030586,2.163130,4.607298,8.689790,1.498723,4.634900,8.116531,1.449482,6.953359,-4.383422,9.966781,-6.621478,-8.824053,1.605014,9.173524,-8.684051], dtype = "float32")#candidate|8232|(77,)|const|float32
call_8230 = relay.TupleGetItem(func_6969_call(relay.reshape(const_8231.astype('float32'), [154,]), relay.reshape(const_8232.astype('float32'), [77,]), ), 3)
call_8233 = relay.TupleGetItem(func_6972_call(relay.reshape(const_8231.astype('float32'), [154,]), relay.reshape(const_8232.astype('float32'), [77,]), ), 3)
bop_8237 = relay.logical_xor(call_8230.astype('int64'), relay.reshape(const_8232.astype('int64'), relay.shape_of(call_8230))) # shape=(77,)
bop_8240 = relay.logical_xor(call_8233.astype('int64'), relay.reshape(const_8232.astype('int64'), relay.shape_of(call_8233))) # shape=(77,)
func_938_call = mod.get_global_var('func_938')
func_939_call = mutated_mod.get_global_var('func_939')
call_8242 = relay.TupleGetItem(func_938_call(), 1)
call_8243 = relay.TupleGetItem(func_939_call(), 1)
const_8246 = relay.const([False,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True], dtype = "bool")#candidate|8246|(77,)|const|bool
bop_8247 = relay.equal(call_8230.astype('bool'), relay.reshape(const_8246.astype('bool'), relay.shape_of(call_8230))) # shape=(77,)
bop_8250 = relay.equal(call_8233.astype('bool'), relay.reshape(const_8246.astype('bool'), relay.shape_of(call_8233))) # shape=(77,)
func_6693_call = mod.get_global_var('func_6693')
func_6695_call = mutated_mod.get_global_var('func_6695')
call_8253 = relay.TupleGetItem(func_6693_call(), 0)
call_8254 = relay.TupleGetItem(func_6695_call(), 0)
uop_8262 = relay.tan(bop_8237.astype('float32')) # shape=(77,)
uop_8264 = relay.tan(bop_8240.astype('float32')) # shape=(77,)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_8266 = func_5765_call()
call_8267 = func_5765_call()
output = relay.Tuple([call_8207,call_8213,var_8214,const_8231,call_8242,bop_8247,call_8253,uop_8262,call_8266,])
output2 = relay.Tuple([call_8208,call_8215,var_8214,const_8231,call_8243,bop_8250,call_8254,uop_8264,call_8267,])
func_8277 = relay.Function([var_8214,], output)
mod['func_8277'] = func_8277
mod = relay.transform.InferType()(mod)
var_8278 = relay.var("var_8278", dtype = "float64", shape = (234,))#candidate|8278|(234,)|var|float64
output = func_8277(var_8278)
func_8279 = relay.Function([var_8278], output)
mutated_mod['func_8279'] = func_8279
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8317 = relay.const([[[2.251597,3.967075],[0.799628,9.225764],[4.598869,6.002189],[-0.032716,7.312409],[-3.697299,1.358954],[-8.154663,7.318945],[0.679171,-2.995550],[2.432519,3.978362],[6.188690,5.142293],[-7.982386,5.657003],[0.391704,-8.298583],[-4.260482,0.906096],[-5.846097,-6.572943],[-1.305710,3.748366],[-5.703726,4.686659]],[[-9.084072,-4.933066],[0.738035,-6.839160],[4.018838,0.628617],[-5.939266,-7.875881],[6.259989,6.329545],[-8.690101,-6.918627],[6.141508,3.887079],[-7.399682,0.617684],[9.130150,-5.635345],[-7.995795,1.917626],[-6.897539,-0.045135],[-1.383576,0.207805],[-7.178727,-5.053044],[-8.932862,3.487045],[-0.247191,-6.387199]],[[2.332974,5.680473],[7.099013,4.932707],[-4.993158,1.732157],[0.641354,9.752263],[2.412539,2.549451],[-8.259906,-7.796416],[4.555358,-8.085095],[-5.621431,-7.738067],[0.645218,5.393022],[6.078439,-2.660393],[4.486845,-0.761775],[0.285498,-2.563460],[-8.556856,6.781810],[5.451438,-9.670102],[7.051616,1.625008]],[[4.386796,-0.609983],[2.279984,3.960432],[-6.084385,4.131844],[-0.465684,7.292742],[6.768899,-9.608788],[6.316469,-8.477424],[4.269892,0.978906],[-2.967933,2.695622],[-0.881331,-5.106006],[5.715081,-1.446938],[9.925634,3.790665],[9.894080,2.855627],[-8.199286,0.604261],[2.950206,7.456541],[-2.319785,-7.680712]],[[4.354693,-1.722656],[2.211279,6.538232],[-4.340930,-7.357120],[5.687456,0.539432],[-3.950853,-9.263846],[-1.863770,5.473276],[8.533813,1.725629],[5.356850,-1.603045],[1.754859,3.362554],[9.306330,4.711628],[-7.250943,5.794526],[0.103929,0.273486],[-8.942439,-4.342944],[9.177004,-4.498653],[-2.556217,-3.721659]],[[0.665679,-4.550565],[3.229096,3.555232],[8.369933,-5.852856],[4.556329,7.361069],[4.682647,-3.330952],[-7.078241,-6.271470],[-0.816626,6.688132],[-1.336533,2.905657],[-7.179955,-1.964979],[6.847890,3.814477],[-1.819259,-6.797946],[7.739882,-9.655256],[-0.157154,-0.236177],[-8.044077,-3.702477],[-8.896791,7.113782]],[[7.041688,-1.430434],[3.451510,6.475100],[7.236737,6.419511],[1.155674,6.280295],[4.651542,3.627989],[-9.757576,9.769614],[-9.031774,-6.713640],[0.789250,-4.871249],[-8.187803,-4.179437],[3.103991,-0.315760],[-0.264182,1.370412],[3.175180,4.213491],[-4.389530,3.193704],[-9.106154,9.950004],[-4.158252,5.116292]],[[-9.429552,7.030267],[1.923791,-6.678028],[9.648282,7.745818],[-5.623751,6.843950],[4.086338,-1.940087],[4.522324,-5.763845],[-5.719301,2.416528],[7.935117,-8.093337],[-5.632316,-0.170355],[-1.639494,-0.385893],[0.033468,9.680538],[-2.515217,-6.923053],[3.456555,-9.822004],[-1.387880,7.786577],[-9.409718,2.417151]],[[0.982202,5.739992],[0.492509,2.139804],[-6.401871,-7.100405],[5.591567,2.259503],[-6.875859,9.263660],[8.574103,8.018211],[5.388586,-5.828045],[5.418177,7.233946],[-1.548892,-7.344987],[3.316321,4.194798],[7.882945,0.209382],[7.035967,1.248707],[-1.496859,-0.195939],[-9.500657,4.275751],[-4.948328,7.839301]],[[-7.176065,-3.655021],[-3.995940,-4.337416],[0.542409,1.289262],[6.610263,7.956243],[-7.198340,2.251873],[-2.565615,-2.717781],[6.501585,-6.349841],[1.293705,6.343851],[-4.007785,-6.313733],[-6.700068,-6.261168],[-0.323043,-6.197514],[0.943711,0.926846],[-7.855070,-1.306308],[-2.521634,5.363463],[3.958960,4.182227]]], dtype = "float32")#candidate|8317|(10, 15, 2)|const|float32
uop_8318 = relay.log(const_8317.astype('float32')) # shape=(10, 15, 2)
func_1417_call = mod.get_global_var('func_1417')
func_1420_call = mutated_mod.get_global_var('func_1420')
var_8325 = relay.var("var_8325", dtype = "float64", shape = (234,))#candidate|8325|(234,)|var|float64
call_8324 = relay.TupleGetItem(func_1417_call(relay.reshape(var_8325.astype('float64'), [234,])), 0)
call_8326 = relay.TupleGetItem(func_1420_call(relay.reshape(var_8325.astype('float64'), [234,])), 0)
output = relay.Tuple([uop_8318,call_8324,var_8325,])
output2 = relay.Tuple([uop_8318,call_8326,var_8325,])
func_8338 = relay.Function([var_8325,], output)
mod['func_8338'] = func_8338
mod = relay.transform.InferType()(mod)
mutated_mod['func_8338'] = func_8338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8339 = relay.var("var_8339", dtype = "float64", shape = (234,))#candidate|8339|(234,)|var|float64
func_8338_call = mutated_mod.get_global_var('func_8338')
call_8340 = func_8338_call(var_8339)
output = call_8340
func_8341 = relay.Function([var_8339], output)
mutated_mod['func_8341'] = func_8341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3471_call = mod.get_global_var('func_3471')
func_3473_call = mutated_mod.get_global_var('func_3473')
call_8356 = relay.TupleGetItem(func_3471_call(), 0)
call_8357 = relay.TupleGetItem(func_3473_call(), 0)
func_6739_call = mod.get_global_var('func_6739')
func_6741_call = mutated_mod.get_global_var('func_6741')
call_8361 = relay.TupleGetItem(func_6739_call(), 0)
call_8362 = relay.TupleGetItem(func_6741_call(), 0)
func_6693_call = mod.get_global_var('func_6693')
func_6695_call = mutated_mod.get_global_var('func_6695')
call_8379 = relay.TupleGetItem(func_6693_call(), 1)
call_8380 = relay.TupleGetItem(func_6695_call(), 1)
func_2454_call = mod.get_global_var('func_2454')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_8392 = relay.TupleGetItem(func_2454_call(), 1)
call_8393 = relay.TupleGetItem(func_2456_call(), 1)
func_1512_call = mod.get_global_var('func_1512')
func_1514_call = mutated_mod.get_global_var('func_1514')
call_8396 = func_1512_call()
call_8397 = func_1512_call()
func_469_call = mod.get_global_var('func_469')
func_473_call = mutated_mod.get_global_var('func_473')
var_8405 = relay.var("var_8405", dtype = "bool", shape = (81, 10))#candidate|8405|(81, 10)|var|bool
var_8406 = relay.var("var_8406", dtype = "int64", shape = (360,))#candidate|8406|(360,)|var|int64
call_8404 = relay.TupleGetItem(func_469_call(relay.reshape(var_8405.astype('bool'), [15, 9, 6]), relay.reshape(var_8405.astype('bool'), [15, 9, 6]), relay.reshape(var_8406.astype('int64'), [360,]), ), 5)
call_8407 = relay.TupleGetItem(func_473_call(relay.reshape(var_8405.astype('bool'), [15, 9, 6]), relay.reshape(var_8405.astype('bool'), [15, 9, 6]), relay.reshape(var_8406.astype('int64'), [360,]), ), 5)
var_8412 = relay.var("var_8412", dtype = "bool", shape = (81, 10))#candidate|8412|(81, 10)|var|bool
bop_8413 = relay.floor_divide(var_8405.astype('float64'), relay.reshape(var_8412.astype('float64'), relay.shape_of(var_8405))) # shape=(81, 10)
func_5904_call = mod.get_global_var('func_5904')
func_5906_call = mutated_mod.get_global_var('func_5906')
call_8419 = func_5904_call()
call_8420 = func_5904_call()
bop_8422 = relay.logical_and(call_8396.astype('bool'), var_8405.astype('bool')) # shape=(81, 10)
bop_8425 = relay.logical_and(call_8397.astype('bool'), var_8405.astype('bool')) # shape=(81, 10)
uop_8426 = relay.atan(var_8412.astype('float32')) # shape=(81, 10)
bop_8433 = relay.multiply(call_8396.astype('float64'), bop_8422.astype('float64')) # shape=(81, 10)
bop_8436 = relay.multiply(call_8397.astype('float64'), bop_8425.astype('float64')) # shape=(81, 10)
bop_8441 = relay.mod(bop_8413.astype('float32'), call_8361.astype('float32')) # shape=(81, 10)
bop_8444 = relay.mod(bop_8413.astype('float32'), call_8362.astype('float32')) # shape=(81, 10)
output = relay.Tuple([call_8356,call_8379,call_8392,call_8404,var_8406,call_8419,uop_8426,bop_8433,bop_8441,])
output2 = relay.Tuple([call_8357,call_8380,call_8393,call_8407,var_8406,call_8420,uop_8426,bop_8436,bop_8444,])
func_8447 = relay.Function([var_8405,var_8406,var_8412,], output)
mod['func_8447'] = func_8447
mod = relay.transform.InferType()(mod)
var_8448 = relay.var("var_8448", dtype = "bool", shape = (81, 10))#candidate|8448|(81, 10)|var|bool
var_8449 = relay.var("var_8449", dtype = "int64", shape = (360,))#candidate|8449|(360,)|var|int64
var_8450 = relay.var("var_8450", dtype = "bool", shape = (81, 10))#candidate|8450|(81, 10)|var|bool
output = func_8447(var_8448,var_8449,var_8450,)
func_8451 = relay.Function([var_8448,var_8449,var_8450,], output)
mutated_mod['func_8451'] = func_8451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5011_call = mod.get_global_var('func_5011')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_8455 = relay.TupleGetItem(func_5011_call(), 0)
call_8456 = relay.TupleGetItem(func_5013_call(), 0)
func_1790_call = mod.get_global_var('func_1790')
func_1791_call = mutated_mod.get_global_var('func_1791')
call_8477 = func_1790_call()
call_8478 = func_1790_call()
output = relay.Tuple([call_8455,call_8477,])
output2 = relay.Tuple([call_8456,call_8478,])
func_8479 = relay.Function([], output)
mod['func_8479'] = func_8479
mod = relay.transform.InferType()(mod)
mutated_mod['func_8479'] = func_8479
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8479_call = mutated_mod.get_global_var('func_8479')
call_8480 = func_8479_call()
output = call_8480
func_8481 = relay.Function([], output)
mutated_mod['func_8481'] = func_8481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5192_call = mod.get_global_var('func_5192')
func_5193_call = mutated_mod.get_global_var('func_5193')
call_8515 = relay.TupleGetItem(func_5192_call(), 0)
call_8516 = relay.TupleGetItem(func_5193_call(), 0)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_8517 = relay.TupleGetItem(func_1736_call(), 0)
call_8518 = relay.TupleGetItem(func_1738_call(), 0)
output = relay.Tuple([call_8515,call_8517,])
output2 = relay.Tuple([call_8516,call_8518,])
func_8519 = relay.Function([], output)
mod['func_8519'] = func_8519
mod = relay.transform.InferType()(mod)
output = func_8519()
func_8520 = relay.Function([], output)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1013_call = mod.get_global_var('func_1013')
func_1015_call = mutated_mod.get_global_var('func_1015')
call_8531 = func_1013_call()
call_8532 = func_1013_call()
func_7466_call = mod.get_global_var('func_7466')
func_7468_call = mutated_mod.get_global_var('func_7468')
call_8549 = relay.TupleGetItem(func_7466_call(), 1)
call_8550 = relay.TupleGetItem(func_7468_call(), 1)
output = relay.Tuple([call_8531,call_8549,])
output2 = relay.Tuple([call_8532,call_8550,])
func_8555 = relay.Function([], output)
mod['func_8555'] = func_8555
mod = relay.transform.InferType()(mod)
output = func_8555()
func_8556 = relay.Function([], output)
mutated_mod['func_8556'] = func_8556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3781_call = mutated_mod.get_global_var('func_3781')
call_8571 = func_3779_call()
call_8572 = func_3779_call()
func_5479_call = mod.get_global_var('func_5479')
func_5482_call = mutated_mod.get_global_var('func_5482')
var_8581 = relay.var("var_8581", dtype = "float32", shape = (936,))#candidate|8581|(936,)|var|float32
call_8580 = relay.TupleGetItem(func_5479_call(relay.reshape(var_8581.astype('float32'), [13, 8, 9]), relay.reshape(var_8581.astype('float32'), [13, 8, 9]), ), 0)
call_8582 = relay.TupleGetItem(func_5482_call(relay.reshape(var_8581.astype('float32'), [13, 8, 9]), relay.reshape(var_8581.astype('float32'), [13, 8, 9]), ), 0)
func_5724_call = mod.get_global_var('func_5724')
func_5726_call = mutated_mod.get_global_var('func_5726')
var_8591 = relay.var("var_8591", dtype = "float64", shape = (234,))#candidate|8591|(234,)|var|float64
call_8590 = relay.TupleGetItem(func_5724_call(relay.reshape(var_8591.astype('float64'), [234,])), 2)
call_8592 = relay.TupleGetItem(func_5726_call(relay.reshape(var_8591.astype('float64'), [234,])), 2)
bop_8594 = relay.floor_mod(var_8591.astype('float32'), relay.reshape(call_8590.astype('float32'), relay.shape_of(var_8591))) # shape=(234,)
bop_8597 = relay.floor_mod(var_8591.astype('float32'), relay.reshape(call_8592.astype('float32'), relay.shape_of(var_8591))) # shape=(234,)
output = relay.Tuple([call_8571,call_8580,var_8581,bop_8594,])
output2 = relay.Tuple([call_8572,call_8582,var_8581,bop_8597,])
func_8598 = relay.Function([var_8581,var_8591,], output)
mod['func_8598'] = func_8598
mod = relay.transform.InferType()(mod)
mutated_mod['func_8598'] = func_8598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8598_call = mutated_mod.get_global_var('func_8598')
var_8600 = relay.var("var_8600", dtype = "float32", shape = (936,))#candidate|8600|(936,)|var|float32
var_8601 = relay.var("var_8601", dtype = "float64", shape = (234,))#candidate|8601|(234,)|var|float64
call_8599 = func_8598_call(var_8600,var_8601,)
output = call_8599
func_8602 = relay.Function([var_8600,var_8601,], output)
mutated_mod['func_8602'] = func_8602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6088_call = mod.get_global_var('func_6088')
func_6089_call = mutated_mod.get_global_var('func_6089')
call_8610 = relay.TupleGetItem(func_6088_call(), 2)
call_8611 = relay.TupleGetItem(func_6089_call(), 2)
func_1736_call = mod.get_global_var('func_1736')
func_1738_call = mutated_mod.get_global_var('func_1738')
call_8612 = relay.TupleGetItem(func_1736_call(), 0)
call_8613 = relay.TupleGetItem(func_1738_call(), 0)
func_2289_call = mod.get_global_var('func_2289')
func_2294_call = mutated_mod.get_global_var('func_2294')
const_8636 = relay.const([-4.171964,-6.875645,9.757566,7.201114,7.899357,-5.672502,-3.988314,7.996458,0.320902,0.829387,-7.265825,-2.475115,9.724404,-7.825400,5.630869,7.993862,-7.539701,-1.574723,3.799337,-6.585580,-3.532940,-1.282286,7.501478,-0.403611,-5.965039,0.057492,-1.950471,6.781856,-7.741566,-2.438741,1.587420,8.056516,-6.283196,9.336066,-7.562972,-7.145344,-9.340863,7.916520,-1.064225,-0.821967,4.734354,-0.137040,9.533714,7.495400,0.968151,1.437964,8.064078,-4.534271,7.596350,6.555093,1.100870,-9.084250,-4.908509,-5.412372,1.074001,8.149869,-4.572561,3.345788,8.373843,0.544550,-9.451190,1.304099,2.286507,8.141299,-4.046556,-6.734527,2.298170,6.298643,-2.102528,-6.667356,3.712806,-9.530709,5.234053,0.674129,2.579280,-2.083135,-7.682779], dtype = "float32")#candidate|8636|(77,)|const|float32
const_8637 = relay.const([-4,4,5,-9,4,-6,7,10,-10,-1,3,6,3,-5,4,3,-10,5,2,4,2,-8,5,-2,8,2,5,5,7,-9,9,10,-10,7,-9,-7,-2,9,-2,-2,6,-6,-2,-9,10,-4,1,-10,-9,2,-9,8,-3,-1,-9,7,-7,-8,-3,-9,-6,-10,7,7,-9,3,-5,9,7,3,3,3,5,10,-10,-9,-6,-5,-10,-8,-9,-5,1,2,-6,-3,-9,10,10,9,2,8,6,-10,4,-5,8,-9,6,6,10,-2,6,2,3,-5,9,3,-5,-2,-3,-5,-9,-10,10,6,3,-9,-1,4,2,8,-1,7,-6,-8,-7,9,-9,-10,5,9,5,9,-8,-9,10,-2,-2,10,7,6,3,10,6,-1,8,-1,9,-1,2,-9,-9,5,9,9,5,10,5,-10,-1,-4,-10,-4,-4,7,-4,8,5,-5,1,10,3,4,3,-9,-6,5,-7,-6,-3,6,-7,-3,10,-7,-3,-8,9,4,-7,-6,3,8,10,10,-7,5,3,-8,-7,5,-4,-8,-5,6,-3,-5,-4,8,-7,9,7,9,3,4,-2,10,1,10,-10,8,-9,-4,5,8,10,-9,-1,-6,6,4,10,4,4,7,-10,-1,-9,-1,7,-10,7,6,6,4,-4,9,-2,3,-1,-4,-9,-2,-10,-5,-2,-5,-4,9,-3,-3,-1,8,9,3,-6,-1,-2,5,5,10,-7,-8,-6,-3,2,-5,-10,8,8,9,8,1,2,5,-8,-7,-2,7,2,8,-6,6,-7,5,-8,9,6,-10,-6,8,-10,10,-7,-9,-7,-4,-1,8,9,-5,-10,4,6,4,9,-7,-4,10,-4,-4,-7,3,-3,7,-6,10,9,-2,8,-9,8,5,-5,-7,5,1,2,-1,4,-6,2,-6,9,-8,-4,3,4,-5,-2,-9,4,10,-3,10,9,-10,3,4,4,1,10,1,4,5,6,5,-6,-7,-4,-10,4,-5,-6,1,2,7,5,-6,-3,5,6,1,-2,3,-7,2,3,-8,-6,-8,-10,10,4,-4,-8,-8,8,-8,-10,-8,-6,-8,-8,7,-7,4,-1,-3,-2,-3,6,5,-3,-4,-8,9,5,-4,-6,-8,-7,10,-7,-6,-2,9,10,-3,9,-7,-2,-2,4,1,-6,-2,-1,4,9,-7,6,-10,10,-1,-3,-7,-3,-3,4,6,4,4,2,5,7,-4,-8,1,-8,-8,-1,5,3,-2,3,-6,7,2,9,3,-1,-8,9,-8,2,-7,2,-6,1,1,-5,1,-10,-3,2,4,-1,4,-2,1,8,-6,2,-7,-7,9,9,5,-6,-8,-4,-4,5,-9,8,-2,7,-1,7,4,-8,9,4,7,-4,-10,9,7,10,2,5,-8,-9,1,-7,-3], dtype = "int32")#candidate|8637|(528,)|const|int32
const_8638 = relay.const([-2,-8,5,-6,-2,7,-9,-3,-6,-3,1,5,2,-1,7,-7,-5,10,6,-2,-8,-8,-5,8,-9,8,-4,4,-5,3,4,-2,6,6,-7,10,7,-4,9,6,4,-10,8,-6,-8,4,-8,1,-8,6,7,-1,-4,-9,-7,-2,2,9,5,-3,-2,-7,3,4,6,7,6,10,-4,-6,5,-2,-10,-6,-8,-10,-6,-3,-4,2,-7,-5,-6,-4,5,3,-7,-8,-8,4,5,-8,-10,2,8,-3,-3,-9,-5,-1,-2,-2,-9,-8,9,5,-7,-5,-4,10,-10,-8,-3,-4,-9,-1,-9,-3,-7,7,4,-8,-7,-7,-9,-6,2,-2,10,-5,2,3,1,2,-7,-2,3,2,-2,-4,6,9,-3,-2,8,-3,3,2,1,2,4,-9,-3,-8,9,-3,9,4,-5,-6,-4,-3,-6,1,-8,-5,6,-9,4,1,9,-10,-7,10,-1,-5,7,1,3,-1,6,1,-8,10,-8,-5,6,5,10,-7,4,-5,2,-4,-2,5,-9,-10,9,-10,1,-5,-3,-2,8,3,5,-4,-7,-1,-3,7,-5,10,-8,-4,-8,-8,1,-3,3,-2,-5,5,-5,1,5,2,6,7,-4,5,-9,-2,-6,9,2,-8,-8,-9,3,2,7,-1,8,8,-6,6,7,4,-5,-1,-4,4,-5,-4,-2,-8,10,3,-5,2,6,-9,-5,4,-7,7,-5,-3,5,-1,-2,7,8,2,4,7,9,1,-10,-6,-10,-8,7,9,9,-8,-9,-4,8,10,-7,10,-4,2,3,-3,-4,-2,-2,-10,9,1,4,4,-9,-1,-1,4,1,-1,5,-1,-7,-9,-2,-10,-10,10,6,5,-6,4,9,-7,6,-7,4,-2,-9,-9,-2,5,-10,6,-8,-3,-9,-6,-7,-1,10,3,-5,4,6,8,-2,9,-7,10,-8,-2,2,-9,8,1,9,-4], dtype = "int64")#candidate|8638|(360,)|const|int64
call_8635 = relay.TupleGetItem(func_2289_call(relay.reshape(const_8636.astype('float32'), [77,]), relay.reshape(const_8637.astype('int32'), [264, 2]), relay.reshape(const_8638.astype('int64'), [360,]), ), 4)
call_8639 = relay.TupleGetItem(func_2294_call(relay.reshape(const_8636.astype('float32'), [77,]), relay.reshape(const_8637.astype('int32'), [264, 2]), relay.reshape(const_8638.astype('int64'), [360,]), ), 4)
output = relay.Tuple([call_8610,call_8612,call_8635,const_8636,const_8637,const_8638,])
output2 = relay.Tuple([call_8611,call_8613,call_8639,const_8636,const_8637,const_8638,])
func_8643 = relay.Function([], output)
mod['func_8643'] = func_8643
mod = relay.transform.InferType()(mod)
output = func_8643()
func_8644 = relay.Function([], output)
mutated_mod['func_8644'] = func_8644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4649_call = mod.get_global_var('func_4649')
func_4651_call = mutated_mod.get_global_var('func_4651')
call_8672 = relay.TupleGetItem(func_4649_call(), 0)
call_8673 = relay.TupleGetItem(func_4651_call(), 0)
output = call_8672
output2 = call_8673
func_8682 = relay.Function([], output)
mod['func_8682'] = func_8682
mod = relay.transform.InferType()(mod)
mutated_mod['func_8682'] = func_8682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8682_call = mutated_mod.get_global_var('func_8682')
call_8683 = func_8682_call()
output = call_8683
func_8684 = relay.Function([], output)
mutated_mod['func_8684'] = func_8684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_8699 = relay.TupleGetItem(func_6812_call(), 1)
call_8700 = relay.TupleGetItem(func_6814_call(), 1)
output = call_8699
output2 = call_8700
func_8707 = relay.Function([], output)
mod['func_8707'] = func_8707
mod = relay.transform.InferType()(mod)
mutated_mod['func_8707'] = func_8707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8707_call = mutated_mod.get_global_var('func_8707')
call_8708 = func_8707_call()
output = call_8708
func_8709 = relay.Function([], output)
mutated_mod['func_8709'] = func_8709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6812_call = mod.get_global_var('func_6812')
func_6814_call = mutated_mod.get_global_var('func_6814')
call_8717 = relay.TupleGetItem(func_6812_call(), 0)
call_8718 = relay.TupleGetItem(func_6814_call(), 0)
func_8447_call = mod.get_global_var('func_8447')
func_8451_call = mutated_mod.get_global_var('func_8451')
const_8720 = relay.const([False,False,False,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,False,True,False,False,True,True,True,True,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,False,True,True,False,True,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,False,True,False,False,False], dtype = "bool")#candidate|8720|(810,)|const|bool
const_8721 = relay.const([4,-5,-8,6,-8,4,-10,8,-6,9,7,3,10,-6,-3,-6,-7,-2,3,10,2,-3,-8,4,-1,6,-3,-10,4,-3,-2,-4,2,-3,-1,-8,-1,-7,-3,3,-4,-2,9,7,9,-10,10,10,-9,7,-10,-5,8,-9,1,-7,-2,1,10,-7,-9,-9,-3,1,4,2,-4,4,-8,-5,5,-3,8,10,-1,8,-4,-7,8,8,7,-7,-6,-3,5,3,-7,-9,-10,6,4,3,2,4,9,3,2,5,2,2,5,9,4,10,5,-7,-9,-6,2,3,9,-5,6,9,-9,5,-8,9,-10,-8,-4,-3,-7,4,-8,1,2,8,-8,-6,-10,5,7,10,3,-4,2,10,6,-9,2,2,5,-2,7,-4,-10,4,2,-5,-9,4,6,-3,9,-9,-1,4,2,-3,-5,7,5,-3,3,-4,6,-8,-1,7,2,-10,8,2,-2,-9,1,4,-5,-3,-6,-5,-4,-7,3,-4,1,-1,-1,-6,-8,-2,1,5,5,-6,-8,3,5,8,5,4,-7,4,-10,1,-7,6,-10,-4,2,4,-3,1,-7,8,10,-6,9,-7,2,4,2,5,-3,-5,-1,3,5,1,-3,-2,1,2,-9,8,6,9,3,7,5,1,10,9,9,7,-9,7,-10,1,-9,-3,10,-4,-7,9,5,-7,5,2,8,-10,-2,-8,-9,4,-7,-2,8,-7,8,-7,7,8,2,8,1,8,6,-6,6,-2,6,7,1,-8,-10,-10,3,-9,-1,-6,6,6,1,-8,3,-7,3,2,9,-2,7,8,-3,-4,5,-7,-3,6,6,-10,-3,7,-2,-1,-8,-10,7,4,4,-4,-7,3,-3,-5,-10,-9,5,-8,-6,-8,3,9,5,-2,1,-1,7,10,2,3,2,4,8,4,2,-8,9,7,-3,6,-4,-2,-10,5,10,5,-7,-9], dtype = "int64")#candidate|8721|(360,)|const|int64
call_8719 = relay.TupleGetItem(func_8447_call(relay.reshape(const_8720.astype('bool'), [81, 10]), relay.reshape(const_8721.astype('int64'), [360,]), relay.reshape(const_8720.astype('bool'), [81, 10]), ), 6)
call_8722 = relay.TupleGetItem(func_8451_call(relay.reshape(const_8720.astype('bool'), [81, 10]), relay.reshape(const_8721.astype('int64'), [360,]), relay.reshape(const_8720.astype('bool'), [81, 10]), ), 6)
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
call_8732 = func_190_call(relay.reshape(const_8721.astype('int64'), [8, 5, 9]), relay.reshape(const_8721.astype('int64'), [8, 5, 9]), )
call_8733 = func_190_call(relay.reshape(const_8721.astype('int64'), [8, 5, 9]), relay.reshape(const_8721.astype('int64'), [8, 5, 9]), )
func_7207_call = mod.get_global_var('func_7207')
func_7209_call = mutated_mod.get_global_var('func_7209')
call_8744 = func_7207_call()
call_8745 = func_7207_call()
func_7365_call = mod.get_global_var('func_7365')
func_7368_call = mutated_mod.get_global_var('func_7368')
const_8750 = relay.const([8.072230,5.855440,4.974855,-5.947779,6.419479,6.721488,1.779570,-2.766238,7.016127,-5.845568,3.562132,-8.634997,2.390370,-6.647157,-0.291079,-7.839224,6.184397,1.781119,7.534170,7.526451,-0.492074,1.370332,6.587010,1.898592,4.557234,3.373121,-8.738030,-3.773522,8.942737,-1.276583,-4.237524,3.162914,-9.018440,5.827036,8.052675,-6.103982,5.590924,1.767501,5.696904,0.288500,8.203300,1.216567,-3.345586,5.227498,-7.708964,8.928285,-2.042155,-5.874106,-1.113110,3.935186,-6.459686,9.656765,4.730081,-8.681588,6.011163,-9.459505,-5.540159,-6.034162,7.937858,-9.322971,8.055903,-1.802309,-3.670295,-1.335940,-8.175636,-0.191405,4.475130,9.448846,3.027037,0.761607,1.842092,8.288488,7.972840,4.543322,4.539198,-3.639211,3.600290], dtype = "float32")#candidate|8750|(77,)|const|float32
call_8749 = relay.TupleGetItem(func_7365_call(relay.reshape(const_8750.astype('float32'), [77, 1])), 4)
call_8751 = relay.TupleGetItem(func_7368_call(relay.reshape(const_8750.astype('float32'), [77, 1])), 4)
output = relay.Tuple([call_8717,call_8719,const_8720,const_8721,call_8732,call_8744,call_8749,const_8750,])
output2 = relay.Tuple([call_8718,call_8722,const_8720,const_8721,call_8733,call_8745,call_8751,const_8750,])
func_8755 = relay.Function([], output)
mod['func_8755'] = func_8755
mod = relay.transform.InferType()(mod)
mutated_mod['func_8755'] = func_8755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8755_call = mutated_mod.get_global_var('func_8755')
call_8756 = func_8755_call()
output = call_8756
func_8757 = relay.Function([], output)
mutated_mod['func_8757'] = func_8757
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8798 = relay.var("var_8798", dtype = "float64", shape = (15, 6, 11))#candidate|8798|(15, 6, 11)|var|float64
uop_8799 = relay.acos(var_8798.astype('float64')) # shape=(15, 6, 11)
func_1064_call = mod.get_global_var('func_1064')
func_1067_call = mutated_mod.get_global_var('func_1067')
var_8807 = relay.var("var_8807", dtype = "float32", shape = (77, 1))#candidate|8807|(77, 1)|var|float32
const_8808 = relay.const([-6.709612,-0.983024,-5.744591,-2.213820,0.156011,7.964091,-4.655561,3.501629,9.131047,3.670539,-0.294769,0.511970,9.642289,-7.202856,0.383871,-6.028179,-7.030371,-2.748531,-7.941854,-1.626687,4.587510,-3.964484,7.248404,3.751277,6.735667,9.299374,0.449676,7.696017,-6.405871,4.758884,8.591429,3.787122,7.774782,-5.133687,6.324025,8.273268,2.137997,-9.289938,-1.964561,1.209812,-3.953348,4.224104,3.843450,3.432240,-5.573311,-6.479567,-1.299520,5.671905,7.812050,8.532619,-5.436402,-0.581352,-2.580574,3.575013,-3.206504,5.236676,8.418548,-3.126006,4.239655,-6.513169,7.332836,2.705195,8.007955,7.872769,-2.128544,8.499232,9.322501,-8.585538,-3.524778,-9.258809,1.597982,4.809162,-3.567314,5.724604,8.644577,7.228196,-5.492610,-9.668080,-7.156993,0.519239,9.706818,2.006788,-9.065401,-0.148869,6.675522,5.608242,-8.300154,7.025705,7.788692,-2.340691,9.668871,1.499228,-8.117034,9.787672,0.987006,-3.630015,6.814835,6.058199,3.003837,-5.554495,0.641852,0.723575,-3.874382,-3.674615,-2.755254,0.885562,5.938973,4.026995,-0.327181,-8.418677,1.947005,-5.179381,-9.468642,-4.524918,-6.406405,9.997746,7.465933,3.177457,9.331793,4.605639,7.491328,8.590399,6.241577,-9.779837,9.629478,2.289342,9.423666,8.614824,0.174896,-8.260884,-6.820808,8.761216,-9.463039,-0.961297,7.663983,0.278732,-2.683986,0.076658,-3.073724,9.530578,-0.319704,-0.143028,5.330835,3.000149,-1.257872,-4.225028,4.671360,-4.699737,-6.425041,-3.321375,-2.852794,-6.959960,-4.690289,-7.093576], dtype = "float32")#candidate|8808|(154,)|const|float32
call_8806 = relay.TupleGetItem(func_1064_call(relay.reshape(var_8807.astype('float32'), [77,]), relay.reshape(const_8808.astype('float32'), [154,]), ), 1)
call_8809 = relay.TupleGetItem(func_1067_call(relay.reshape(var_8807.astype('float32'), [77,]), relay.reshape(const_8808.astype('float32'), [154,]), ), 1)
func_5970_call = mod.get_global_var('func_5970')
func_5972_call = mutated_mod.get_global_var('func_5972')
const_8814 = relay.const([-1,-6,7,-7,8,-9,-4,-8,-8,-1,1,-2,9,-7,9,1,-6,-8,-9,-1,7,-5,3,-1,8,-6,9,2,-2,-8,3,-2,8,-2,-6,-4,-5,7,2,-10,7,1,-8,4,2,-2,3,3,-5,-8,10,-6,-1,-4,1,5,-2,4,9,-1,-1,-7,-8,-6,7,-5,-6,-3,-6,-9,-3,-6], dtype = "uint16")#candidate|8814|(72,)|const|uint16
call_8813 = relay.TupleGetItem(func_5970_call(relay.reshape(const_8814.astype('uint16'), [72,])), 1)
call_8815 = relay.TupleGetItem(func_5972_call(relay.reshape(const_8814.astype('uint16'), [72,])), 1)
func_5918_call = mod.get_global_var('func_5918')
func_5919_call = mutated_mod.get_global_var('func_5919')
call_8817 = func_5918_call()
call_8818 = func_5918_call()
uop_8830 = relay.sin(var_8807.astype('float64')) # shape=(77, 1)
output = relay.Tuple([uop_8799,call_8806,const_8808,call_8813,const_8814,call_8817,uop_8830,])
output2 = relay.Tuple([uop_8799,call_8809,const_8808,call_8815,const_8814,call_8818,uop_8830,])
func_8835 = relay.Function([var_8798,var_8807,], output)
mod['func_8835'] = func_8835
mod = relay.transform.InferType()(mod)
mutated_mod['func_8835'] = func_8835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8835_call = mutated_mod.get_global_var('func_8835')
var_8837 = relay.var("var_8837", dtype = "float64", shape = (15, 6, 11))#candidate|8837|(15, 6, 11)|var|float64
var_8838 = relay.var("var_8838", dtype = "float32", shape = (77, 1))#candidate|8838|(77, 1)|var|float32
call_8836 = func_8835_call(var_8837,var_8838,)
output = call_8836
func_8839 = relay.Function([var_8837,var_8838,], output)
mutated_mod['func_8839'] = func_8839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5011_call = mod.get_global_var('func_5011')
func_5013_call = mutated_mod.get_global_var('func_5013')
call_8916 = relay.TupleGetItem(func_5011_call(), 0)
call_8917 = relay.TupleGetItem(func_5013_call(), 0)
func_677_call = mod.get_global_var('func_677')
func_679_call = mutated_mod.get_global_var('func_679')
call_8923 = relay.TupleGetItem(func_677_call(), 0)
call_8924 = relay.TupleGetItem(func_679_call(), 0)
output = relay.Tuple([call_8916,call_8923,])
output2 = relay.Tuple([call_8917,call_8924,])
func_8942 = relay.Function([], output)
mod['func_8942'] = func_8942
mod = relay.transform.InferType()(mod)
output = func_8942()
func_8943 = relay.Function([], output)
mutated_mod['func_8943'] = func_8943
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9014 = relay.var("var_9014", dtype = "uint16", shape = (8, 14, 9))#candidate|9014|(8, 14, 9)|var|uint16
var_9015 = relay.var("var_9015", dtype = "uint16", shape = (8, 14, 9))#candidate|9015|(8, 14, 9)|var|uint16
bop_9016 = relay.bitwise_and(var_9014.astype('uint16'), relay.reshape(var_9015.astype('uint16'), relay.shape_of(var_9014))) # shape=(8, 14, 9)
output = relay.Tuple([bop_9016,])
output2 = relay.Tuple([bop_9016,])
func_9019 = relay.Function([var_9014,var_9015,], output)
mod['func_9019'] = func_9019
mod = relay.transform.InferType()(mod)
mutated_mod['func_9019'] = func_9019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9019_call = mutated_mod.get_global_var('func_9019')
var_9021 = relay.var("var_9021", dtype = "uint16", shape = (8, 14, 9))#candidate|9021|(8, 14, 9)|var|uint16
var_9022 = relay.var("var_9022", dtype = "uint16", shape = (8, 14, 9))#candidate|9022|(8, 14, 9)|var|uint16
call_9020 = func_9019_call(var_9021,var_9022,)
output = call_9020
func_9023 = relay.Function([var_9021,var_9022,], output)
mutated_mod['func_9023'] = func_9023
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9030 = relay.var("var_9030", dtype = "float32", shape = (4, 6, 8))#candidate|9030|(4, 6, 8)|var|float32
uop_9031 = relay.erf(var_9030.astype('float32')) # shape=(4, 6, 8)
output = uop_9031
output2 = uop_9031
func_9035 = relay.Function([var_9030,], output)
mod['func_9035'] = func_9035
mod = relay.transform.InferType()(mod)
mutated_mod['func_9035'] = func_9035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9036 = relay.var("var_9036", dtype = "float32", shape = (4, 6, 8))#candidate|9036|(4, 6, 8)|var|float32
func_9035_call = mutated_mod.get_global_var('func_9035')
call_9037 = func_9035_call(var_9036)
output = call_9037
func_9038 = relay.Function([var_9036], output)
mutated_mod['func_9038'] = func_9038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6088_call = mod.get_global_var('func_6088')
func_6089_call = mutated_mod.get_global_var('func_6089')
call_9040 = relay.TupleGetItem(func_6088_call(), 0)
call_9041 = relay.TupleGetItem(func_6089_call(), 0)
output = call_9040
output2 = call_9041
func_9049 = relay.Function([], output)
mod['func_9049'] = func_9049
mod = relay.transform.InferType()(mod)
output = func_9049()
func_9050 = relay.Function([], output)
mutated_mod['func_9050'] = func_9050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7726_call = mod.get_global_var('func_7726')
func_7727_call = mutated_mod.get_global_var('func_7727')
call_9055 = func_7726_call()
call_9056 = func_7726_call()
func_6969_call = mod.get_global_var('func_6969')
func_6972_call = mutated_mod.get_global_var('func_6972')
var_9083 = relay.var("var_9083", dtype = "float32", shape = (154,))#candidate|9083|(154,)|var|float32
const_9084 = relay.const([-4.187796,-4.326218,5.361692,-2.800671,-4.578177,0.456699,0.689329,6.797948,4.988209,-7.503864,-0.369833,1.351585,3.314142,-9.610340,-3.888494,7.923548,0.177419,-5.625662,1.737205,-2.934375,-9.352138,1.143086,-0.415521,-7.529676,4.978328,4.988703,0.782412,-3.621838,6.398858,4.590874,0.849198,1.879265,-1.899504,0.844093,-4.249217,7.763741,3.370463,-9.746281,6.618185,5.326472,8.106299,-0.144716,5.991795,-8.484350,-7.884556,8.561521,-5.420770,-9.074125,-9.224617,-5.748572,3.304062,8.804877,-7.593507,-2.161787,-6.028462,-2.802121,1.375085,-3.255363,-0.754589,8.243421,-1.359318,-4.114813,2.390197,4.519632,-9.124227,-7.767175,0.788094,9.939331,-1.914078,-9.917708,0.831689,-4.196739,5.182836,-0.875191,3.054267,-9.781049,-8.434823], dtype = "float32")#candidate|9084|(77,)|const|float32
call_9082 = relay.TupleGetItem(func_6969_call(relay.reshape(var_9083.astype('float32'), [154,]), relay.reshape(const_9084.astype('float32'), [77,]), ), 1)
call_9085 = relay.TupleGetItem(func_6972_call(relay.reshape(var_9083.astype('float32'), [154,]), relay.reshape(const_9084.astype('float32'), [77,]), ), 1)
func_7466_call = mod.get_global_var('func_7466')
func_7468_call = mutated_mod.get_global_var('func_7468')
call_9091 = relay.TupleGetItem(func_7466_call(), 3)
call_9092 = relay.TupleGetItem(func_7468_call(), 3)
var_9116 = relay.var("var_9116", dtype = "float32", shape = (77,))#candidate|9116|(77,)|var|float32
bop_9117 = relay.maximum(const_9084.astype('float32'), relay.reshape(var_9116.astype('float32'), relay.shape_of(const_9084))) # shape=(77,)
func_1822_call = mod.get_global_var('func_1822')
func_1826_call = mutated_mod.get_global_var('func_1826')
var_9130 = relay.var("var_9130", dtype = "uint64", shape = ())#candidate|9130|()|var|uint64
var_9131 = relay.var("var_9131", dtype = "uint64", shape = (135,))#candidate|9131|(135,)|var|uint64
call_9129 = func_1822_call(relay.reshape(var_9130.astype('uint64'), []), relay.reshape(var_9131.astype('uint64'), [15, 9, 1]), )
call_9132 = func_1822_call(relay.reshape(var_9130.astype('uint64'), []), relay.reshape(var_9131.astype('uint64'), [15, 9, 1]), )
uop_9138 = relay.cosh(const_9084.astype('float64')) # shape=(77,)
func_1552_call = mod.get_global_var('func_1552')
func_1555_call = mutated_mod.get_global_var('func_1555')
const_9146 = relay.const([-6.080511,-3.598887,6.029756,2.553692,1.502063,-9.359224,7.514329,-0.500003,5.344261,8.334901,8.072546,8.000751,-9.752756,8.991973,-1.122568,-3.521668,6.409309,-8.770429,-5.597005,-3.912610,1.772185,0.698648,6.768878,8.851818,-6.688507,8.617939,2.739156,6.408257,4.798046,3.981796,7.663015,-7.051913,-9.676609,6.415348,-2.506891,-6.015118,-3.386333,-9.549458,2.770987,-0.082871,-6.945564,8.943871,-1.809082,4.312903,0.303166,8.102350,-0.426185,2.669967,-8.700203,-0.899448,-3.563853,7.786832,-2.872583,-0.295329,5.215192,3.002184,-0.987360,5.874689,1.946667,-9.692494,9.228382,2.269602,9.170622,-0.354478,8.128626,6.716213,7.472817,-5.984149,-5.480286,5.677985,6.676119,-8.421909,8.834741,-2.857601,-7.492245,2.494389,3.411317,-4.523349,8.749009,-6.558126,8.047386,-4.299446,-5.393087,-7.128426,6.376033,0.514700,-8.255028,-5.620548,1.551270,-2.669519,5.221309,-8.237706,-0.174927,-7.052028,2.757481,-6.228282,-2.195547,-8.583976,8.430114,5.414975,-4.906145,3.325318,-5.006676,0.319682,-8.061831,-5.292462,0.288871,-2.815415,2.129002,-8.592070,-3.397393,8.954906,5.128867,9.112659,-6.117381,-5.018306,6.990345,9.021203,5.357408,-9.169629,-6.977964,-4.534495,0.509845,9.466370,5.098265,7.301178,-3.417729,-1.475008,-9.038604,-1.005227,-7.463893,-4.749105,-6.851951,-9.133604,-0.451385,9.496770,8.564397,-3.950719,1.854975,3.038531,8.892037,-1.360232,1.454281,-2.497616,-5.628241,-3.166549,2.714340,4.930068,-7.804918,7.447760,-6.682480,5.272653,-2.230622,-2.711493,1.155740,-2.459239,-8.803567,-9.821014,4.302629,-9.007655,1.642168,7.179065,3.198241,-1.013001,-8.138965,-9.782669,-7.882435,-8.206081,5.182509,-3.272304,-9.846930,-3.010421,7.995672,-3.831050,8.928919,4.336175,3.798467,3.931853,9.884620,-0.291557,8.017456,-5.907790,-9.153959,2.533879,4.247720,-7.948197,-9.841228,-5.926877,1.780702,6.315953,8.600595,0.812164,9.246743,8.612106,-9.359811,-1.383322,-7.546724,3.918208,3.906869,9.509054,1.629128,-5.193892,-7.565649,2.806958,5.638729,-2.889476,0.704869,6.125607,-3.793298,0.352346,-0.597448,-7.255681,-9.601014,8.565207,-2.754268,-1.227100,-4.397629,-8.886700,-7.083028,-5.141836,-9.370194,-6.122548,-2.811273,-0.924967,4.629944,1.878396,6.553732,-3.622060,3.944612,5.262437,-5.256184,1.535901,-6.796215,2.747122], dtype = "float64")#candidate|9146|(234,)|const|float64
call_9145 = relay.TupleGetItem(func_1552_call(relay.reshape(const_9146.astype('float64'), [234,])), 1)
call_9147 = relay.TupleGetItem(func_1555_call(relay.reshape(const_9146.astype('float64'), [234,])), 1)
output = relay.Tuple([call_9055,call_9082,var_9083,call_9091,bop_9117,call_9129,var_9130,var_9131,uop_9138,call_9145,const_9146,])
output2 = relay.Tuple([call_9056,call_9085,var_9083,call_9092,bop_9117,call_9132,var_9130,var_9131,uop_9138,call_9147,const_9146,])
func_9150 = relay.Function([var_9083,var_9116,var_9130,var_9131,], output)
mod['func_9150'] = func_9150
mod = relay.transform.InferType()(mod)
var_9151 = relay.var("var_9151", dtype = "float32", shape = (154,))#candidate|9151|(154,)|var|float32
var_9152 = relay.var("var_9152", dtype = "float32", shape = (77,))#candidate|9152|(77,)|var|float32
var_9153 = relay.var("var_9153", dtype = "uint64", shape = ())#candidate|9153|()|var|uint64
var_9154 = relay.var("var_9154", dtype = "uint64", shape = (135,))#candidate|9154|(135,)|var|uint64
output = func_9150(var_9151,var_9152,var_9153,var_9154,)
func_9155 = relay.Function([var_9151,var_9152,var_9153,var_9154,], output)
mutated_mod['func_9155'] = func_9155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7132_call = mod.get_global_var('func_7132')
func_7133_call = mutated_mod.get_global_var('func_7133')
call_9194 = func_7132_call()
call_9195 = func_7132_call()
func_2621_call = mod.get_global_var('func_2621')
func_2624_call = mutated_mod.get_global_var('func_2624')
var_9197 = relay.var("var_9197", dtype = "float64", shape = (234,))#candidate|9197|(234,)|var|float64
const_9198 = relay.const([[-0.944754,8.011970,7.318471,-4.535043,-9.173185,5.321959,-0.798358],[-9.335014,7.692140,-8.334215,6.914310,4.200141,9.460072,-3.637996],[5.065847,-7.060163,5.554025,2.317026,-7.269121,0.088209,-6.937725],[-9.371090,-8.958080,3.828046,5.158845,2.138727,4.610668,-1.171909],[-5.283751,-6.231741,6.088591,3.628295,-9.146734,-4.871632,-8.050034],[-6.427948,-0.275140,1.365700,4.232117,-6.007523,0.954640,-7.699129],[-9.978928,6.005643,7.989240,-3.014643,-1.269228,3.032606,1.846615],[7.550956,7.021840,-5.801553,-1.655003,1.231834,4.582159,8.549303],[4.246195,5.078405,-3.888297,-8.095660,-5.942013,-0.060090,-7.390799],[9.423497,6.406595,3.716793,-9.946914,-5.000463,-7.140856,5.678018],[4.163762,-6.763564,-7.486316,-5.714032,-5.399289,-3.884827,-1.299505]], dtype = "float32")#candidate|9198|(11, 7)|const|float32
call_9196 = relay.TupleGetItem(func_2621_call(relay.reshape(var_9197.astype('float64'), [234,]), relay.reshape(const_9198.astype('float32'), [11, 7]), ), 1)
call_9199 = relay.TupleGetItem(func_2624_call(relay.reshape(var_9197.astype('float64'), [234,]), relay.reshape(const_9198.astype('float32'), [11, 7]), ), 1)
func_190_call = mod.get_global_var('func_190')
func_193_call = mutated_mod.get_global_var('func_193')
var_9204 = relay.var("var_9204", dtype = "int64", shape = (360,))#candidate|9204|(360,)|var|int64
call_9203 = func_190_call(relay.reshape(var_9204.astype('int64'), [8, 5, 9]), relay.reshape(var_9204.astype('int64'), [8, 5, 9]), )
call_9205 = func_190_call(relay.reshape(var_9204.astype('int64'), [8, 5, 9]), relay.reshape(var_9204.astype('int64'), [8, 5, 9]), )
output = relay.Tuple([call_9194,call_9196,var_9197,const_9198,call_9203,var_9204,])
output2 = relay.Tuple([call_9195,call_9199,var_9197,const_9198,call_9205,var_9204,])
func_9212 = relay.Function([var_9197,var_9204,], output)
mod['func_9212'] = func_9212
mod = relay.transform.InferType()(mod)
mutated_mod['func_9212'] = func_9212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9212_call = mutated_mod.get_global_var('func_9212')
var_9214 = relay.var("var_9214", dtype = "float64", shape = (234,))#candidate|9214|(234,)|var|float64
var_9215 = relay.var("var_9215", dtype = "int64", shape = (360,))#candidate|9215|(360,)|var|int64
call_9213 = func_9212_call(var_9214,var_9215,)
output = call_9213
func_9216 = relay.Function([var_9214,var_9215,], output)
mutated_mod['func_9216'] = func_9216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7207_call = mod.get_global_var('func_7207')
func_7209_call = mutated_mod.get_global_var('func_7209')
call_9221 = func_7207_call()
call_9222 = func_7207_call()
func_9019_call = mod.get_global_var('func_9019')
func_9023_call = mutated_mod.get_global_var('func_9023')
var_9229 = relay.var("var_9229", dtype = "uint16", shape = (1008,))#candidate|9229|(1008,)|var|uint16
call_9228 = relay.TupleGetItem(func_9019_call(relay.reshape(var_9229.astype('uint16'), [8, 14, 9]), relay.reshape(var_9229.astype('uint16'), [8, 14, 9]), ), 0)
call_9230 = relay.TupleGetItem(func_9023_call(relay.reshape(var_9229.astype('uint16'), [8, 14, 9]), relay.reshape(var_9229.astype('uint16'), [8, 14, 9]), ), 0)
output = relay.Tuple([call_9221,call_9228,var_9229,])
output2 = relay.Tuple([call_9222,call_9230,var_9229,])
func_9244 = relay.Function([var_9229,], output)
mod['func_9244'] = func_9244
mod = relay.transform.InferType()(mod)
var_9245 = relay.var("var_9245", dtype = "uint16", shape = (1008,))#candidate|9245|(1008,)|var|uint16
output = func_9244(var_9245)
func_9246 = relay.Function([var_9245], output)
mutated_mod['func_9246'] = func_9246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_9302 = relay.TupleGetItem(func_4195_call(), 0)
call_9303 = relay.TupleGetItem(func_4197_call(), 0)
func_8643_call = mod.get_global_var('func_8643')
func_8644_call = mutated_mod.get_global_var('func_8644')
call_9309 = relay.TupleGetItem(func_8643_call(), 2)
call_9310 = relay.TupleGetItem(func_8644_call(), 2)
output = relay.Tuple([call_9302,call_9309,])
output2 = relay.Tuple([call_9303,call_9310,])
func_9317 = relay.Function([], output)
mod['func_9317'] = func_9317
mod = relay.transform.InferType()(mod)
mutated_mod['func_9317'] = func_9317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9317_call = mutated_mod.get_global_var('func_9317')
call_9318 = func_9317_call()
output = call_9318
func_9319 = relay.Function([], output)
mutated_mod['func_9319'] = func_9319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9326 = relay.var("var_9326", dtype = "uint8", shape = ())#candidate|9326|()|var|uint8
var_9327 = relay.var("var_9327", dtype = "uint8", shape = (2, 14, 8))#candidate|9327|(2, 14, 8)|var|uint8
bop_9328 = relay.subtract(var_9326.astype('uint8'), var_9327.astype('uint8')) # shape=(2, 14, 8)
output = bop_9328
output2 = bop_9328
func_9334 = relay.Function([var_9326,var_9327,], output)
mod['func_9334'] = func_9334
mod = relay.transform.InferType()(mod)
mutated_mod['func_9334'] = func_9334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9334_call = mutated_mod.get_global_var('func_9334')
var_9336 = relay.var("var_9336", dtype = "uint8", shape = ())#candidate|9336|()|var|uint8
var_9337 = relay.var("var_9337", dtype = "uint8", shape = (2, 14, 8))#candidate|9337|(2, 14, 8)|var|uint8
call_9335 = func_9334_call(var_9336,var_9337,)
output = call_9335
func_9338 = relay.Function([var_9336,var_9337,], output)
mutated_mod['func_9338'] = func_9338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2815_call = mod.get_global_var('func_2815')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_9364 = func_2815_call()
call_9365 = func_2815_call()
output = relay.Tuple([call_9364,])
output2 = relay.Tuple([call_9365,])
func_9375 = relay.Function([], output)
mod['func_9375'] = func_9375
mod = relay.transform.InferType()(mod)
mutated_mod['func_9375'] = func_9375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9375_call = mutated_mod.get_global_var('func_9375')
call_9376 = func_9375_call()
output = call_9376
func_9377 = relay.Function([], output)
mutated_mod['func_9377'] = func_9377
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9383 = relay.const([[[-7.497519],[3.592828],[-3.458683],[-6.650171],[4.108559],[2.436667],[-2.542721]],[[-9.523818],[-5.697230],[4.233351],[-8.220360],[-1.542650],[-1.521087],[5.353667]],[[7.071807],[0.689258],[5.086575],[-0.538573],[-7.444756],[2.273675],[3.824398]],[[4.790608],[-5.140114],[1.857429],[3.678073],[4.704197],[-5.712386],[6.855105]]], dtype = "float64")#candidate|9383|(4, 7, 1)|const|float64
uop_9384 = relay.rsqrt(const_9383.astype('float64')) # shape=(4, 7, 1)
uop_9389 = relay.asin(uop_9384.astype('float32')) # shape=(4, 7, 1)
bop_9393 = relay.maximum(uop_9384.astype('int8'), relay.reshape(uop_9389.astype('int8'), relay.shape_of(uop_9384))) # shape=(4, 7, 1)
output = bop_9393
output2 = bop_9393
func_9396 = relay.Function([], output)
mod['func_9396'] = func_9396
mod = relay.transform.InferType()(mod)
mutated_mod['func_9396'] = func_9396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9396_call = mutated_mod.get_global_var('func_9396')
call_9397 = func_9396_call()
output = call_9397
func_9398 = relay.Function([], output)
mutated_mod['func_9398'] = func_9398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_650_call = mod.get_global_var('func_650')
func_651_call = mutated_mod.get_global_var('func_651')
call_9427 = func_650_call()
call_9428 = func_650_call()
output = relay.Tuple([call_9427,])
output2 = relay.Tuple([call_9428,])
func_9443 = relay.Function([], output)
mod['func_9443'] = func_9443
mod = relay.transform.InferType()(mod)
output = func_9443()
func_9444 = relay.Function([], output)
mutated_mod['func_9444'] = func_9444
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9578 = relay.const([[[-6.357815],[-9.912963],[8.676198],[-4.588373],[-5.182979]],[[5.117775],[-3.854473],[-1.038703],[-3.630646],[1.566482]],[[-5.547441],[-6.827434],[-2.126184],[-6.724534],[-4.721938]],[[1.380333],[-0.037999],[3.334504],[-8.084336],[-6.586227]],[[3.024171],[-6.324598],[0.596121],[-9.451728],[-4.729809]],[[8.965084],[1.087991],[3.925134],[1.379553],[8.018309]],[[-0.761969],[7.198216],[-9.011952],[-5.754284],[-5.819621]],[[3.726885],[8.115403],[3.730939],[-8.008606],[-6.596177]],[[-2.314816],[-8.503029],[2.865145],[2.292849],[6.534769]],[[-8.559685],[7.707402],[-3.664064],[-2.415557],[-7.559727]],[[0.115394],[9.357614],[-7.636651],[-9.604566],[-9.629289]],[[3.604369],[-5.574739],[-3.943918],[7.994306],[7.310606]],[[-3.036472],[-7.406409],[6.892286],[-6.962168],[-1.709574]],[[-3.462523],[-5.686075],[-5.823946],[3.313135],[-2.523704]],[[0.733765],[-4.280463],[1.243056],[0.981134],[-1.393809]],[[0.752909],[-6.369950],[-5.911223],[-8.882392],[-1.195678]]], dtype = "float64")#candidate|9578|(16, 5, 1)|const|float64
uop_9579 = relay.atan(const_9578.astype('float64')) # shape=(16, 5, 1)
bop_9583 = relay.power(uop_9579.astype('float64'), relay.reshape(const_9578.astype('float64'), relay.shape_of(uop_9579))) # shape=(16, 5, 1)
func_6088_call = mod.get_global_var('func_6088')
func_6089_call = mutated_mod.get_global_var('func_6089')
call_9586 = relay.TupleGetItem(func_6088_call(), 0)
call_9587 = relay.TupleGetItem(func_6089_call(), 0)
output = relay.Tuple([bop_9583,call_9586,])
output2 = relay.Tuple([bop_9583,call_9587,])
func_9611 = relay.Function([], output)
mod['func_9611'] = func_9611
mod = relay.transform.InferType()(mod)
output = func_9611()
func_9612 = relay.Function([], output)
mutated_mod['func_9612'] = func_9612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9375_call = mod.get_global_var('func_9375')
func_9377_call = mutated_mod.get_global_var('func_9377')
call_9625 = relay.TupleGetItem(func_9375_call(), 0)
call_9626 = relay.TupleGetItem(func_9377_call(), 0)
func_2678_call = mod.get_global_var('func_2678')
func_2680_call = mutated_mod.get_global_var('func_2680')
call_9648 = relay.TupleGetItem(func_2678_call(), 1)
call_9649 = relay.TupleGetItem(func_2680_call(), 1)
output = relay.Tuple([call_9625,call_9648,])
output2 = relay.Tuple([call_9626,call_9649,])
func_9683 = relay.Function([], output)
mod['func_9683'] = func_9683
mod = relay.transform.InferType()(mod)
output = func_9683()
func_9684 = relay.Function([], output)
mutated_mod['func_9684'] = func_9684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8755_call = mod.get_global_var('func_8755')
func_8757_call = mutated_mod.get_global_var('func_8757')
call_9749 = relay.TupleGetItem(func_8755_call(), 3)
call_9750 = relay.TupleGetItem(func_8757_call(), 3)
func_2075_call = mod.get_global_var('func_2075')
func_2079_call = mutated_mod.get_global_var('func_2079')
var_9781 = relay.var("var_9781", dtype = "float32", shape = (77,))#candidate|9781|(77,)|var|float32
var_9782 = relay.var("var_9782", dtype = "float32", shape = (154,))#candidate|9782|(154,)|var|float32
call_9780 = relay.TupleGetItem(func_2075_call(relay.reshape(var_9781.astype('float32'), [11, 7]), relay.reshape(var_9782.astype('float32'), [11, 14]), ), 0)
call_9783 = relay.TupleGetItem(func_2079_call(relay.reshape(var_9781.astype('float32'), [11, 7]), relay.reshape(var_9782.astype('float32'), [11, 14]), ), 0)
func_5765_call = mod.get_global_var('func_5765')
func_5766_call = mutated_mod.get_global_var('func_5766')
call_9784 = func_5765_call()
call_9785 = func_5765_call()
func_7824_call = mod.get_global_var('func_7824')
func_7828_call = mutated_mod.get_global_var('func_7828')
call_9797 = relay.TupleGetItem(func_7824_call(relay.reshape(var_9781.astype('float32'), [11, 7]), relay.reshape(var_9782.astype('float32'), [154,]), ), 0)
call_9798 = relay.TupleGetItem(func_7828_call(relay.reshape(var_9781.astype('float32'), [11, 7]), relay.reshape(var_9782.astype('float32'), [154,]), ), 0)
output = relay.Tuple([call_9749,call_9780,var_9781,var_9782,call_9784,call_9797,])
output2 = relay.Tuple([call_9750,call_9783,var_9781,var_9782,call_9785,call_9798,])
func_9824 = relay.Function([var_9781,var_9782,], output)
mod['func_9824'] = func_9824
mod = relay.transform.InferType()(mod)
mutated_mod['func_9824'] = func_9824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9824_call = mutated_mod.get_global_var('func_9824')
var_9826 = relay.var("var_9826", dtype = "float32", shape = (77,))#candidate|9826|(77,)|var|float32
var_9827 = relay.var("var_9827", dtype = "float32", shape = (154,))#candidate|9827|(154,)|var|float32
call_9825 = func_9824_call(var_9826,var_9827,)
output = call_9825
func_9828 = relay.Function([var_9826,var_9827,], output)
mutated_mod['func_9828'] = func_9828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9830 = relay.var("var_9830", dtype = "bool", shape = (10, 6, 11))#candidate|9830|(10, 6, 11)|var|bool
var_9831 = relay.var("var_9831", dtype = "bool", shape = (10, 6, 11))#candidate|9831|(10, 6, 11)|var|bool
bop_9832 = relay.logical_and(var_9830.astype('bool'), relay.reshape(var_9831.astype('bool'), relay.shape_of(var_9830))) # shape=(10, 6, 11)
func_902_call = mod.get_global_var('func_902')
func_904_call = mutated_mod.get_global_var('func_904')
call_9837 = relay.TupleGetItem(func_902_call(), 0)
call_9838 = relay.TupleGetItem(func_904_call(), 0)
func_8479_call = mod.get_global_var('func_8479')
func_8481_call = mutated_mod.get_global_var('func_8481')
call_9847 = relay.TupleGetItem(func_8479_call(), 1)
call_9848 = relay.TupleGetItem(func_8481_call(), 1)
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_9853 = relay.TupleGetItem(func_4195_call(), 0)
call_9854 = relay.TupleGetItem(func_4197_call(), 0)
func_5904_call = mod.get_global_var('func_5904')
func_5906_call = mutated_mod.get_global_var('func_5906')
call_9858 = func_5904_call()
call_9859 = func_5904_call()
uop_9872 = relay.atanh(var_9830.astype('float32')) # shape=(10, 6, 11)
func_7207_call = mod.get_global_var('func_7207')
func_7209_call = mutated_mod.get_global_var('func_7209')
call_9874 = func_7207_call()
call_9875 = func_7207_call()
const_9876 = relay.const([[[-4.502662,-7.280791,7.782863,2.351749,6.971621,-3.532296,6.016530,1.760151,-0.649477,3.895535,2.588897],[0.662792,-5.589477,-0.408685,-4.200574,2.295641,0.522221,5.570649,-6.309906,5.360880,2.363188,8.783768],[1.397042,5.323745,9.126212,-8.462133,1.890957,-5.474339,-3.001576,-4.757727,1.534895,6.640688,7.074977],[2.232809,4.355417,4.138086,-3.512552,-0.488009,-8.121849,-8.648512,-4.760574,-5.302386,-3.742310,4.418978],[8.432701,-2.618136,-2.679362,5.226852,-3.076861,2.354564,8.503166,-5.292872,4.838668,1.507230,-2.155616],[-4.067994,6.602842,4.063612,1.223419,-1.324046,-5.542922,2.278407,-4.348997,-6.878569,4.655768,-2.067247]],[[6.866037,4.852237,1.186986,-3.853384,-3.701027,5.959264,6.187622,2.183824,3.334693,4.208498,-7.559646],[-4.251027,2.476083,6.013354,-1.331366,-3.179484,-8.638311,0.871561,-8.700301,-1.265990,-6.802138,-1.696115],[-2.518893,-5.562309,0.328332,7.405769,5.262966,-7.231150,-9.453735,1.350634,-9.851954,-3.551803,8.059548],[-2.519049,8.954655,-8.250708,-8.085746,5.092708,9.067262,1.859937,4.550971,-3.009427,-7.124790,-2.274217],[1.255247,-5.138675,8.797461,-7.932113,-9.894579,-7.970661,4.850402,0.830727,-6.700241,-0.061570,-1.114307],[-9.387956,-5.549201,-4.506435,-0.925750,-7.617721,4.008165,2.005596,9.107917,4.888833,-7.766759,-9.496702]],[[3.288450,-5.255606,-9.924398,2.594307,-4.354776,1.648853,-6.086392,2.869294,-3.842870,-0.292067,-7.940648],[-6.280904,-4.788835,4.410133,3.776541,-5.385722,4.443165,-8.283222,-0.437771,0.603967,-4.815152,9.996952],[-9.729517,8.666458,-8.246228,-8.203379,8.956780,4.873959,2.219934,-1.181918,-6.259535,4.982241,2.384846],[5.167124,1.606267,-0.016298,3.663984,-4.510470,1.159720,-5.215088,-1.533255,-5.772592,3.143961,5.024592],[9.139869,-8.141169,-7.132300,1.118739,9.815261,3.493982,7.015399,-4.594863,-3.988508,2.356864,-7.261275],[2.029927,-6.534420,-7.775922,5.178323,-6.884030,-0.413773,-0.546950,-6.593505,-8.336861,9.972402,-8.938455]],[[-6.162370,1.216987,-7.915582,-6.584882,1.651837,5.996643,6.814142,3.976239,5.339014,6.289510,-6.193939],[-0.747222,-0.845453,6.435163,6.225585,-1.791253,-9.470657,-6.144082,-9.312029,-8.834902,-6.322176,-3.349953],[4.137424,2.447089,2.077466,-9.682854,-0.918368,9.673269,-5.286331,-0.247714,-7.744163,6.327680,6.080107],[2.135650,-0.733561,0.833653,9.281185,-9.915033,2.503724,6.672701,0.478947,3.314952,2.647427,-0.453538],[2.473659,8.533066,6.343319,-9.077300,-6.600837,9.624796,8.432467,8.163410,-8.777343,-1.651300,6.976427],[-7.712379,0.187415,0.346863,-6.469816,-0.064182,-0.484139,-1.523992,-0.065232,-6.642580,-2.511718,2.538420]],[[-4.206803,3.294869,5.964924,0.811393,8.442730,9.271729,0.825193,8.756365,-3.868162,6.627525,3.158599],[-3.631141,-0.368092,-1.911497,-8.595110,1.583433,2.820489,9.032173,-0.584781,3.198216,4.923223,-1.889163],[9.743744,-4.654295,-9.639690,4.694543,8.577298,8.080971,-5.631631,1.007371,-0.999283,-0.155647,1.187058],[-6.779914,-6.979673,9.001152,-2.873251,-5.269285,-9.465426,8.088472,-1.240626,-4.261485,-4.841291,7.445084],[-6.039956,-6.134363,3.758097,-2.276958,-5.251060,-4.613022,-2.200550,-6.143908,-0.762963,8.786666,-6.453569],[1.927175,1.354670,-8.640360,2.572838,-5.745439,-9.353496,-3.760393,4.892546,-3.035139,4.764993,-7.494076]],[[6.211419,-5.677640,8.595258,-1.418835,-7.294778,-0.830309,7.239423,-7.581906,0.178404,-2.667863,1.423591],[3.274215,3.316601,-3.643244,2.507349,7.097814,-3.175509,-9.038369,3.576403,9.523117,-7.559295,4.491996],[-9.400331,-4.986422,-7.780869,-5.161428,-4.702450,9.958213,9.626924,-7.589932,-5.803723,9.711856,-0.648779],[2.653856,-4.826622,4.375343,-7.341899,0.385561,-8.816862,-5.893842,-3.023838,-6.974642,0.645502,3.036540],[-4.633303,5.631546,5.650034,5.259522,-3.256223,5.541890,7.553366,5.447300,2.322033,-6.356609,-5.980503],[-5.340048,4.591775,1.644141,-0.195044,-7.084476,1.884223,-1.723316,-3.220031,-6.043478,-7.467389,-6.966646]],[[-9.669959,3.705340,-0.831037,-0.901553,1.251510,9.954215,8.308564,9.547220,6.038183,-1.189863,5.259774],[2.026637,-4.342947,-0.145787,0.628088,-4.408946,-8.950983,1.540032,-2.944663,9.361254,4.914819,-3.764002],[-6.569308,-0.354585,3.343144,-3.031506,6.861061,1.337050,7.277165,-4.285192,-7.733979,-3.643955,4.033450],[5.603948,6.810234,1.125265,6.127872,-5.095664,7.653875,-3.007796,7.406316,6.409921,-6.463722,5.369047],[-0.685616,7.635321,-7.662927,0.866469,1.279213,9.518767,3.674093,8.764104,0.634217,-8.482148,1.546510],[2.665069,7.668802,1.201409,8.069963,0.218916,6.699654,-6.668408,8.964309,5.065329,-4.628688,8.224047]],[[5.253084,3.640442,-3.781241,5.618207,-8.599072,2.499118,6.377465,2.744091,6.513121,-8.388317,3.945325],[-0.095874,-1.438661,-1.972889,5.135151,-2.948205,-3.792011,7.868158,-7.989533,-7.728122,9.378679,-8.767532],[5.912715,-4.504814,0.887351,9.965733,5.095231,9.896504,6.827766,6.287464,3.087498,8.224790,9.482087],[4.515767,1.600440,-8.377491,5.288801,7.796326,-4.011098,8.747156,-4.241586,2.766264,-7.238562,5.597095],[-0.674924,-2.531125,-5.092314,6.977948,-2.204278,2.905301,2.125989,8.770624,0.402247,6.354091,-3.454225],[2.627922,0.235974,-3.500894,8.751385,2.309325,-3.166664,9.053052,7.484477,-1.077487,9.533400,7.545603]],[[6.827605,7.009240,1.874990,2.585072,8.568271,-0.669161,1.313661,4.509321,-5.437339,-0.482830,-1.017644],[8.717381,-9.680290,-7.587035,-9.518508,-0.952467,-5.632373,-8.036204,-1.694084,8.371552,-9.698662,-8.699759],[-6.365076,-2.198084,-2.305330,-4.649658,-0.196247,-9.947325,2.226379,7.142182,-8.240350,-6.668770,5.520424],[-7.984573,-3.886828,-1.424415,6.759656,-8.924879,-9.084066,-0.985267,1.567911,4.037248,5.760238,-4.874890],[-6.285908,-5.829281,-5.959986,7.064127,6.353792,9.204777,6.699313,-2.295115,9.915489,4.719849,1.814451],[-4.620859,-9.881345,-0.624928,-6.255647,-0.861678,-4.872331,6.677477,2.623221,5.019544,5.325282,-2.227291]],[[-0.261365,4.373653,7.104521,0.263174,5.307398,5.810174,7.395426,9.248182,0.270088,4.513507,-5.298504],[-1.726425,5.088713,-0.872764,-6.782318,-1.500173,1.337500,-5.216478,-9.723525,3.618574,-4.811705,0.018154],[-8.426825,9.171815,-3.365413,-4.281305,7.042674,2.563789,-9.657459,5.020399,-5.386225,8.393350,-0.717091],[4.185448,3.621989,-5.777778,7.123564,9.161616,-4.632540,8.221233,9.016846,4.088730,-8.722400,-3.976501],[-3.860139,-0.547542,0.078534,-5.531595,9.913309,-3.056550,-3.519866,-8.291764,-6.411183,3.644033,-8.786534],[4.189344,-2.889846,8.291694,5.902212,0.975383,5.649024,6.865605,5.396762,-5.262293,4.098189,1.196520]]], dtype = "float32")#candidate|9876|(10, 6, 11)|const|float32
bop_9877 = relay.add(uop_9872.astype('int8'), relay.reshape(const_9876.astype('int8'), relay.shape_of(uop_9872))) # shape=(10, 6, 11)
func_7365_call = mod.get_global_var('func_7365')
func_7368_call = mutated_mod.get_global_var('func_7368')
var_9889 = relay.var("var_9889", dtype = "float32", shape = (11, 7))#candidate|9889|(11, 7)|var|float32
call_9888 = relay.TupleGetItem(func_7365_call(relay.reshape(var_9889.astype('float32'), [77, 1])), 5)
call_9890 = relay.TupleGetItem(func_7368_call(relay.reshape(var_9889.astype('float32'), [77, 1])), 5)
func_5873_call = mod.get_global_var('func_5873')
func_5875_call = mutated_mod.get_global_var('func_5875')
call_9893 = func_5873_call()
call_9894 = func_5873_call()
output = relay.Tuple([bop_9832,call_9837,call_9847,call_9853,call_9858,call_9874,bop_9877,call_9888,var_9889,call_9893,])
output2 = relay.Tuple([bop_9832,call_9838,call_9848,call_9854,call_9859,call_9875,bop_9877,call_9890,var_9889,call_9894,])
func_9906 = relay.Function([var_9830,var_9831,var_9889,], output)
mod['func_9906'] = func_9906
mod = relay.transform.InferType()(mod)
mutated_mod['func_9906'] = func_9906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9906_call = mutated_mod.get_global_var('func_9906')
var_9908 = relay.var("var_9908", dtype = "bool", shape = (10, 6, 11))#candidate|9908|(10, 6, 11)|var|bool
var_9909 = relay.var("var_9909", dtype = "bool", shape = (10, 6, 11))#candidate|9909|(10, 6, 11)|var|bool
var_9910 = relay.var("var_9910", dtype = "float32", shape = (11, 7))#candidate|9910|(11, 7)|var|float32
call_9907 = func_9906_call(var_9908,var_9909,var_9910,)
output = call_9907
func_9911 = relay.Function([var_9908,var_9909,var_9910,], output)
mutated_mod['func_9911'] = func_9911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4195_call = mod.get_global_var('func_4195')
func_4197_call = mutated_mod.get_global_var('func_4197')
call_9918 = relay.TupleGetItem(func_4195_call(), 0)
call_9919 = relay.TupleGetItem(func_4197_call(), 0)
func_7582_call = mod.get_global_var('func_7582')
func_7583_call = mutated_mod.get_global_var('func_7583')
call_9930 = relay.TupleGetItem(func_7582_call(), 3)
call_9931 = relay.TupleGetItem(func_7583_call(), 3)
func_9035_call = mod.get_global_var('func_9035')
func_9038_call = mutated_mod.get_global_var('func_9038')
var_9933 = relay.var("var_9933", dtype = "float32", shape = (192,))#candidate|9933|(192,)|var|float32
call_9932 = func_9035_call(relay.reshape(var_9933.astype('float32'), [4, 6, 8]))
call_9934 = func_9035_call(relay.reshape(var_9933.astype('float32'), [4, 6, 8]))
func_4858_call = mod.get_global_var('func_4858')
func_4862_call = mutated_mod.get_global_var('func_4862')
const_9941 = relay.const([-0.022445,-9.172975,1.078866,3.962480,5.064293,5.534879,2.599419,4.747494,-9.157671,4.021226,6.892712,-4.460886,4.456836,1.368622,-0.508017,-3.119860,5.209649,8.405462,-7.419853,4.534431,-4.110425,-5.387073,-4.731692,-4.229617,2.454313,1.750676,-8.605569,-6.106866,-7.777391,-0.709600,-6.347704,-3.971809,0.512720,-7.094894,-6.878276,1.365276,3.669926,-2.312019,6.341382,-2.274674,0.855013,-5.700301,-5.747571,1.516758,-5.294020,5.838120,6.448496,-6.550500,-6.853278,-2.740238,-6.365694,5.344609,3.931704,-5.803749,1.336871,4.257013,-5.821476,-8.503992,-1.926123,7.399799,-6.569564,7.128570,-5.701626,-8.240347,-2.700046,-3.786664,6.388071,-0.980455,6.651962,9.913354,-4.273899,3.501930,-7.699484,5.897559,-5.516488,5.011563,2.411236], dtype = "float32")#candidate|9941|(77,)|const|float32
var_9942 = relay.var("var_9942", dtype = "float32", shape = (154,))#candidate|9942|(154,)|var|float32
call_9940 = relay.TupleGetItem(func_4858_call(relay.reshape(const_9941.astype('float32'), [77,]), relay.reshape(var_9942.astype('float32'), [154,]), ), 1)
call_9943 = relay.TupleGetItem(func_4862_call(relay.reshape(const_9941.astype('float32'), [77,]), relay.reshape(var_9942.astype('float32'), [154,]), ), 1)
output = relay.Tuple([call_9918,call_9930,call_9932,var_9933,call_9940,const_9941,var_9942,])
output2 = relay.Tuple([call_9919,call_9931,call_9934,var_9933,call_9943,const_9941,var_9942,])
func_9945 = relay.Function([var_9933,var_9942,], output)
mod['func_9945'] = func_9945
mod = relay.transform.InferType()(mod)
mutated_mod['func_9945'] = func_9945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9945_call = mutated_mod.get_global_var('func_9945')
var_9947 = relay.var("var_9947", dtype = "float32", shape = (192,))#candidate|9947|(192,)|var|float32
var_9948 = relay.var("var_9948", dtype = "float32", shape = (154,))#candidate|9948|(154,)|var|float32
call_9946 = func_9945_call(var_9947,var_9948,)
output = call_9946
func_9949 = relay.Function([var_9947,var_9948,], output)
mutated_mod['func_9949'] = func_9949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7132_call = mod.get_global_var('func_7132')
func_7133_call = mutated_mod.get_global_var('func_7133')
call_9954 = func_7132_call()
call_9955 = func_7132_call()
output = relay.Tuple([call_9954,])
output2 = relay.Tuple([call_9955,])
func_9959 = relay.Function([], output)
mod['func_9959'] = func_9959
mod = relay.transform.InferType()(mod)
output = func_9959()
func_9960 = relay.Function([], output)
mutated_mod['func_9960'] = func_9960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1488_call = mod.get_global_var('func_1488')
func_1489_call = mutated_mod.get_global_var('func_1489')
call_9989 = relay.TupleGetItem(func_1488_call(), 1)
call_9990 = relay.TupleGetItem(func_1489_call(), 1)
output = relay.Tuple([call_9989,])
output2 = relay.Tuple([call_9990,])
func_9999 = relay.Function([], output)
mod['func_9999'] = func_9999
mod = relay.transform.InferType()(mod)
mutated_mod['func_9999'] = func_9999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9999_call = mutated_mod.get_global_var('func_9999')
call_10000 = func_9999_call()
output = call_10000
func_10001 = relay.Function([], output)
mutated_mod['func_10001'] = func_10001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8643_call = mod.get_global_var('func_8643')
func_8644_call = mutated_mod.get_global_var('func_8644')
call_10027 = relay.TupleGetItem(func_8643_call(), 4)
call_10028 = relay.TupleGetItem(func_8644_call(), 4)
func_5440_call = mod.get_global_var('func_5440')
func_5442_call = mutated_mod.get_global_var('func_5442')
call_10062 = relay.TupleGetItem(func_5440_call(), 0)
call_10063 = relay.TupleGetItem(func_5442_call(), 0)
func_1417_call = mod.get_global_var('func_1417')
func_1420_call = mutated_mod.get_global_var('func_1420')
var_10082 = relay.var("var_10082", dtype = "float64", shape = (234,))#candidate|10082|(234,)|var|float64
call_10081 = relay.TupleGetItem(func_1417_call(relay.reshape(var_10082.astype('float64'), [234,])), 1)
call_10083 = relay.TupleGetItem(func_1420_call(relay.reshape(var_10082.astype('float64'), [234,])), 1)
output = relay.Tuple([call_10027,call_10062,call_10081,var_10082,])
output2 = relay.Tuple([call_10028,call_10063,call_10083,var_10082,])
func_10089 = relay.Function([var_10082,], output)
mod['func_10089'] = func_10089
mod = relay.transform.InferType()(mod)
var_10090 = relay.var("var_10090", dtype = "float64", shape = (234,))#candidate|10090|(234,)|var|float64
output = func_10089(var_10090)
func_10091 = relay.Function([var_10090], output)
mutated_mod['func_10091'] = func_10091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7698_call = mod.get_global_var('func_7698')
func_7699_call = mutated_mod.get_global_var('func_7699')
call_10146 = func_7698_call()
call_10147 = func_7698_call()
output = relay.Tuple([call_10146,])
output2 = relay.Tuple([call_10147,])
func_10169 = relay.Function([], output)
mod['func_10169'] = func_10169
mod = relay.transform.InferType()(mod)
mutated_mod['func_10169'] = func_10169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10169_call = mutated_mod.get_global_var('func_10169')
call_10170 = func_10169_call()
output = call_10170
func_10171 = relay.Function([], output)
mutated_mod['func_10171'] = func_10171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4786_call = mod.get_global_var('func_4786')
func_4788_call = mutated_mod.get_global_var('func_4788')
call_10197 = relay.TupleGetItem(func_4786_call(), 1)
call_10198 = relay.TupleGetItem(func_4788_call(), 1)
output = call_10197
output2 = call_10198
func_10208 = relay.Function([], output)
mod['func_10208'] = func_10208
mod = relay.transform.InferType()(mod)
output = func_10208()
func_10209 = relay.Function([], output)
mutated_mod['func_10209'] = func_10209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_938_call = mod.get_global_var('func_938')
func_939_call = mutated_mod.get_global_var('func_939')
call_10218 = relay.TupleGetItem(func_938_call(), 1)
call_10219 = relay.TupleGetItem(func_939_call(), 1)
output = relay.Tuple([call_10218,])
output2 = relay.Tuple([call_10219,])
func_10221 = relay.Function([], output)
mod['func_10221'] = func_10221
mod = relay.transform.InferType()(mod)
mutated_mod['func_10221'] = func_10221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10221_call = mutated_mod.get_global_var('func_10221')
call_10222 = func_10221_call()
output = call_10222
func_10223 = relay.Function([], output)
mutated_mod['func_10223'] = func_10223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4502_call = mod.get_global_var('func_4502')
func_4504_call = mutated_mod.get_global_var('func_4504')
call_10309 = relay.TupleGetItem(func_4502_call(), 0)
call_10310 = relay.TupleGetItem(func_4504_call(), 0)
output = call_10309
output2 = call_10310
func_10337 = relay.Function([], output)
mod['func_10337'] = func_10337
mod = relay.transform.InferType()(mod)
output = func_10337()
func_10338 = relay.Function([], output)
mutated_mod['func_10338'] = func_10338
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10341 = relay.var("var_10341", dtype = "uint64", shape = ())#candidate|10341|()|var|uint64
var_10342 = relay.var("var_10342", dtype = "uint64", shape = (2, 11, 3))#candidate|10342|(2, 11, 3)|var|uint64
bop_10343 = relay.less_equal(var_10341.astype('bool'), var_10342.astype('bool')) # shape=(2, 11, 3)
func_2678_call = mod.get_global_var('func_2678')
func_2680_call = mutated_mod.get_global_var('func_2680')
call_10349 = relay.TupleGetItem(func_2678_call(), 1)
call_10350 = relay.TupleGetItem(func_2680_call(), 1)
func_5873_call = mod.get_global_var('func_5873')
func_5875_call = mutated_mod.get_global_var('func_5875')
call_10358 = func_5873_call()
call_10359 = func_5873_call()
output = relay.Tuple([bop_10343,call_10349,call_10358,])
output2 = relay.Tuple([bop_10343,call_10350,call_10359,])
func_10361 = relay.Function([var_10341,var_10342,], output)
mod['func_10361'] = func_10361
mod = relay.transform.InferType()(mod)
var_10362 = relay.var("var_10362", dtype = "uint64", shape = ())#candidate|10362|()|var|uint64
var_10363 = relay.var("var_10363", dtype = "uint64", shape = (2, 11, 3))#candidate|10363|(2, 11, 3)|var|uint64
output = func_10361(var_10362,var_10363,)
func_10364 = relay.Function([var_10362,var_10363,], output)
mutated_mod['func_10364'] = func_10364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5603_call = mod.get_global_var('func_5603')
func_5605_call = mutated_mod.get_global_var('func_5605')
call_10425 = func_5603_call()
call_10426 = func_5603_call()
output = call_10425
output2 = call_10426
func_10444 = relay.Function([], output)
mod['func_10444'] = func_10444
mod = relay.transform.InferType()(mod)
output = func_10444()
func_10445 = relay.Function([], output)
mutated_mod['func_10445'] = func_10445
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10450 = relay.const([[[9,7,1,4,2,5],[10,9,5,-8,-5,-8],[1,-5,6,-6,-9,7],[-2,3,8,5,4,-9],[-2,-1,-8,-7,-8,7],[-10,-9,6,8,-6,4],[-2,1,5,-2,-8,5],[-3,9,3,-3,9,-3],[-7,-2,5,-6,-7,1],[-6,-2,-10,-4,-9,2],[9,8,-7,-10,3,7],[2,-3,2,-2,10,5],[-2,1,-2,-5,8,6],[4,2,-9,-3,6,-9],[-3,7,6,-1,2,10]],[[-7,-4,8,-4,7,-10],[-7,-9,-3,1,1,7],[-1,8,4,-9,4,-8],[3,-7,-8,-7,1,7],[-6,10,-8,7,-7,5],[2,2,9,-8,-2,3],[1,-4,-5,6,1,9],[3,1,10,3,1,-7],[5,-3,8,6,5,2],[3,3,6,-5,7,-10],[3,-10,9,5,1,-5],[-3,10,3,9,-2,1],[-4,8,4,10,-3,10],[-8,-10,-2,-9,5,2],[-3,-5,-3,4,5,-9]],[[-2,-4,1,-9,-10,7],[-3,10,8,-6,-5,6],[9,3,2,5,-3,10],[-5,-3,9,1,-8,8],[3,5,-6,3,-10,9],[10,-7,3,9,8,4],[-3,9,-4,-7,2,-4],[-2,-4,-5,4,7,10],[-1,-9,-2,6,8,7],[2,-8,6,3,-10,8],[-9,1,-6,-7,4,3],[9,-3,5,-8,6,3],[9,-9,4,4,-2,1],[-8,2,-4,-7,-8,-9],[-10,2,-4,-7,-5,-2]],[[4,4,1,-3,-4,10],[-1,5,7,4,3,-3],[-3,2,7,-6,-9,6],[-6,10,3,1,7,5],[10,-1,-5,9,-7,7],[4,6,6,5,10,-3],[3,8,2,4,-5,4],[-3,8,-6,7,-10,3],[-2,7,4,-4,-6,9],[-8,-1,-1,-10,9,-6],[5,-5,4,-1,6,8],[-8,9,7,-3,10,-5],[-8,-5,7,4,-5,-8],[-6,-7,5,-4,-10,-8],[-10,9,2,1,10,-8]],[[9,10,-10,-5,7,1],[-7,-4,8,3,10,10],[-7,5,8,4,-7,1],[3,4,-8,-2,9,-4],[-8,7,-1,4,-7,-5],[4,2,6,-7,-1,-10],[5,8,10,3,8,-7],[-4,-7,10,7,1,-5],[5,7,4,-9,-9,-5],[8,6,5,-5,6,1],[3,-2,-7,1,-9,-2],[-6,-2,-7,-4,2,-10],[-5,7,6,7,-3,-4],[-6,-2,3,-5,-4,-4],[3,-3,9,-3,8,-8]],[[-5,-4,6,9,-10,6],[-7,-2,10,-2,-7,-10],[-10,-3,-3,3,-7,-10],[-2,4,2,-7,1,-1],[-9,-3,-10,5,8,-8],[-10,-10,-7,-2,1,-5],[8,-3,-3,-1,9,-1],[9,-1,-3,-7,-10,-3],[-9,-8,-3,-5,-4,3],[5,2,-9,5,6,-4],[-4,5,2,-1,-3,3],[-1,-10,-7,2,6,-7],[6,3,-9,4,-10,7],[7,2,8,-9,-4,-4],[1,-4,-2,3,7,10]],[[3,-9,-3,2,6,-1],[9,-5,-8,-3,-7,-9],[2,-6,6,-4,10,-9],[-4,4,-4,6,6,4],[10,-4,-8,7,2,6],[-9,-6,-8,5,-5,1],[5,-3,-9,-4,6,-8],[-10,-4,-6,2,-3,-8],[3,-2,-2,8,-10,-6],[-7,8,8,-10,10,-3],[-4,-6,1,-9,-5,3],[-4,3,-1,3,-9,5],[-8,8,-1,-6,3,-4],[-4,-9,6,4,-4,-3],[8,-6,8,6,8,-4]],[[2,4,10,10,-2,2],[-4,7,-5,-4,8,-2],[1,2,10,8,4,9],[-7,7,-9,-7,-7,-10],[7,-5,-4,-3,5,-6],[-1,-8,4,10,-6,3],[6,-10,-4,-5,-6,8],[-9,7,-6,8,-7,4],[-4,5,1,-5,7,2],[-6,4,9,-2,-5,-2],[-3,-10,-7,-2,-9,10],[4,-9,-1,-4,-9,-10],[2,-9,-2,6,1,6],[10,-10,-6,9,6,-10],[-10,-5,-5,-9,7,-2]],[[9,4,5,10,1,-4],[-8,6,-2,2,-3,3],[10,-2,10,-5,1,-10],[3,-2,10,9,1,-4],[4,-7,1,-6,1,-9],[2,-1,5,-1,-1,-3],[1,9,-9,-4,-8,-1],[-2,9,5,-6,2,-1],[-1,7,7,3,2,-9],[6,6,-6,-3,6,-2],[2,9,7,4,4,10],[-1,-9,-6,6,2,5],[2,6,4,8,-6,-1],[-9,-1,-6,4,3,-2],[2,10,-1,1,5,-9]],[[5,-6,-8,-6,-3,2],[9,9,-1,-10,9,4],[4,-1,-3,9,-2,9],[-3,-7,-3,8,-6,3],[-9,10,-2,8,-2,-9],[1,-2,-5,3,7,6],[2,3,2,7,8,1],[-4,10,-8,-8,6,-6],[-3,9,-10,10,-1,-1],[-9,-8,6,1,-6,3],[-7,-7,-2,-4,-1,-5],[-9,4,-9,7,-3,-7],[2,-8,-6,-6,-3,7],[-5,10,-5,-8,1,-8],[-9,8,-2,3,-2,4]],[[-4,-4,3,-4,-2,4],[-1,-6,4,-3,-1,-3],[8,8,-6,10,3,9],[-5,4,-7,-9,-9,-1],[10,-4,-4,5,4,2],[6,-2,-7,-6,-3,-4],[-7,9,7,-10,3,-10],[-2,9,-8,10,6,-2],[-4,-7,-9,7,3,3],[-5,9,-7,-5,3,9],[-6,5,10,4,8,-10],[2,2,-1,-7,9,4],[-2,9,4,9,6,3],[3,-9,-1,-7,-4,10],[5,-4,1,4,-9,-3]],[[8,5,5,-9,5,1],[-7,-1,-9,-10,6,1],[-4,-3,8,7,7,10],[-2,-2,9,3,4,-10],[-2,-9,6,8,-7,-6],[8,-10,7,-8,-1,6],[-6,9,-2,2,1,4],[3,9,6,2,-9,10],[-4,-5,-9,-8,-9,-6],[6,-4,-3,-4,2,-4],[-7,2,-1,-1,1,2],[6,-6,7,-5,3,-9],[10,1,-7,10,-5,1],[5,3,-10,7,-6,-3],[6,-7,-9,-5,2,-1]],[[-5,4,-5,8,-8,7],[7,-4,-8,8,-4,5],[3,-2,-8,-5,-6,-4],[5,3,2,-1,-6,2],[1,8,-4,9,-2,10],[4,4,-4,10,-10,-3],[7,-1,-9,6,2,-5],[8,-2,5,-2,-9,8],[7,-5,3,9,-3,2],[3,2,-4,2,1,2],[-9,-6,1,4,-1,6],[8,-3,-8,-3,-5,-8],[1,2,-5,-9,-9,3],[-8,9,-7,-3,-10,7],[1,1,-2,6,-9,7]]], dtype = "uint8")#candidate|10450|(13, 15, 6)|const|uint8
var_10451 = relay.var("var_10451", dtype = "uint8", shape = (13, 15, 6))#candidate|10451|(13, 15, 6)|var|uint8
bop_10452 = relay.equal(const_10450.astype('bool'), relay.reshape(var_10451.astype('bool'), relay.shape_of(const_10450))) # shape=(13, 15, 6)
bop_10470 = relay.divide(bop_10452.astype('float64'), relay.reshape(const_10450.astype('float64'), relay.shape_of(bop_10452))) # shape=(13, 15, 6)
uop_10473 = relay.asinh(var_10451.astype('float32')) # shape=(13, 15, 6)
output = relay.Tuple([bop_10470,uop_10473,])
output2 = relay.Tuple([bop_10470,uop_10473,])
F = relay.Function([var_10451,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_10451,], output2)
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
