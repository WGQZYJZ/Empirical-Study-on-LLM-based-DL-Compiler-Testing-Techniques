import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_412 = relay.var("var_412", dtype = "float64", shape = ())#candidate|412|()|var|float64
var_413 = relay.var("var_413", dtype = "float64", shape = (2, 13, 1))#candidate|413|(2, 13, 1)|var|float64
bop_414 = relay.floor_divide(var_412.astype('float64'), var_413.astype('float64')) # shape=(2, 13, 1)
output = bop_414
output2 = bop_414
func_418 = relay.Function([var_412,var_413,], output)
mod['func_418'] = func_418
mod = relay.transform.InferType()(mod)
var_419 = relay.var("var_419", dtype = "float64", shape = ())#candidate|419|()|var|float64
var_420 = relay.var("var_420", dtype = "float64", shape = (2, 13, 1))#candidate|420|(2, 13, 1)|var|float64
output = func_418(var_419,var_420,)
func_421 = relay.Function([var_419,var_420,], output)
mutated_mod['func_421'] = func_421
mutated_mod = relay.transform.InferType()(mutated_mod)
var_431 = relay.var("var_431", dtype = "int16", shape = ())#candidate|431|()|var|int16
var_432 = relay.var("var_432", dtype = "int16", shape = (3, 3, 7))#candidate|432|(3, 3, 7)|var|int16
bop_433 = relay.not_equal(var_431.astype('bool'), var_432.astype('bool')) # shape=(3, 3, 7)
func_418_call = mod.get_global_var('func_418')
func_421_call = mutated_mod.get_global_var('func_421')
var_440 = relay.var("var_440", dtype = "float64", shape = (26,))#candidate|440|(26,)|var|float64
call_439 = func_418_call(relay.reshape(var_431.astype('float64'), []), relay.reshape(var_440.astype('float64'), [2, 13, 1]), )
call_441 = func_418_call(relay.reshape(var_431.astype('float64'), []), relay.reshape(var_440.astype('float64'), [2, 13, 1]), )
output = relay.Tuple([bop_433,call_439,var_440,])
output2 = relay.Tuple([bop_433,call_441,var_440,])
func_443 = relay.Function([var_431,var_432,var_440,], output)
mod['func_443'] = func_443
mod = relay.transform.InferType()(mod)
var_444 = relay.var("var_444", dtype = "int16", shape = ())#candidate|444|()|var|int16
var_445 = relay.var("var_445", dtype = "int16", shape = (3, 3, 7))#candidate|445|(3, 3, 7)|var|int16
var_446 = relay.var("var_446", dtype = "float64", shape = (26,))#candidate|446|(26,)|var|float64
output = func_443(var_444,var_445,var_446,)
func_447 = relay.Function([var_444,var_445,var_446,], output)
mutated_mod['func_447'] = func_447
mutated_mod = relay.transform.InferType()(mutated_mod)
var_480 = relay.var("var_480", dtype = "uint64", shape = ())#candidate|480|()|var|uint64
const_481 = relay.const([[[9,9,-1,-10,-6,1,-3,-6,8,-5,-8,2,-8,-8],[7,-8,9,10,8,5,9,6,6,3,5,-4,-4,5],[-5,-4,-1,9,-2,2,-8,-8,2,3,7,1,5,6],[-2,-1,6,-9,10,6,6,-5,-2,5,8,-1,-5,-8],[-10,8,-5,-10,6,5,7,9,-9,2,-7,7,-5,2],[-5,-10,3,6,1,-9,5,-5,7,-10,10,10,-10,-3]],[[-7,7,-5,6,7,6,-8,-4,-8,7,-5,-2,10,-10],[-8,5,10,-7,9,3,-5,-3,-3,-8,-6,-8,4,5],[1,4,10,5,3,5,3,-7,6,-1,-7,-1,4,5],[9,-3,5,10,-1,9,6,6,-1,-10,-5,7,-10,6],[-10,-5,10,9,-7,3,5,2,6,-5,-4,-8,-5,-10],[7,-10,-6,-6,-3,4,-6,-10,10,4,-1,-7,-3,-2]],[[1,-5,10,5,-10,-4,6,7,-6,-4,-8,-4,-9,-3],[-5,-1,9,-7,3,6,-3,-8,-10,-10,3,-3,-2,1],[-8,-6,-1,3,4,10,-2,-1,-9,-3,-6,-3,6,-10],[-5,-2,5,-7,-6,6,-10,5,5,8,-7,-2,3,3],[-3,8,4,-10,9,-5,10,2,10,-4,5,10,3,6],[7,-5,-4,8,-4,-9,8,5,7,-7,-7,5,-5,8]]], dtype = "uint64")#candidate|481|(3, 6, 14)|const|uint64
bop_482 = relay.bitwise_xor(var_480.astype('uint64'), const_481.astype('uint64')) # shape=(3, 6, 14)
output = relay.Tuple([bop_482,])
output2 = relay.Tuple([bop_482,])
func_492 = relay.Function([var_480,], output)
mod['func_492'] = func_492
mod = relay.transform.InferType()(mod)
var_493 = relay.var("var_493", dtype = "uint64", shape = ())#candidate|493|()|var|uint64
output = func_492(var_493)
func_494 = relay.Function([var_493], output)
mutated_mod['func_494'] = func_494
mutated_mod = relay.transform.InferType()(mutated_mod)
var_737 = relay.var("var_737", dtype = "int32", shape = (10, 3, 4))#candidate|737|(10, 3, 4)|var|int32
const_738 = relay.const([[[9,2,5,-1],[-5,-5,7,-7],[-5,-10,5,5]],[[8,1,-10,-9],[-3,10,2,4],[2,-6,-3,-4]],[[7,-3,-9,8],[-8,3,6,-6],[6,10,9,-3]],[[-3,-8,3,-9],[5,-3,-10,2],[-8,5,-8,6]],[[1,1,-9,-3],[-5,-1,2,-9],[1,1,-2,9]],[[-7,-7,-9,10],[8,10,-8,-10],[-3,-1,10,-3]],[[-3,2,9,-9],[-8,-3,9,7],[-7,-5,-9,7]],[[-5,-8,-10,3],[7,-9,9,-3],[4,3,3,3]],[[6,-4,2,-6],[10,9,5,3],[9,8,-2,4]],[[1,1,5,4],[1,-6,-7,-9],[4,-9,2,-3]]], dtype = "int32")#candidate|738|(10, 3, 4)|const|int32
bop_739 = relay.maximum(var_737.astype('int32'), relay.reshape(const_738.astype('int32'), relay.shape_of(var_737))) # shape=(10, 3, 4)
func_492_call = mod.get_global_var('func_492')
func_494_call = mutated_mod.get_global_var('func_494')
var_743 = relay.var("var_743", dtype = "uint64", shape = ())#candidate|743|()|var|uint64
call_742 = relay.TupleGetItem(func_492_call(relay.reshape(var_743.astype('uint64'), [])), 0)
call_744 = relay.TupleGetItem(func_494_call(relay.reshape(var_743.astype('uint64'), [])), 0)
uop_746 = relay.acosh(const_738.astype('float32')) # shape=(10, 3, 4)
output = relay.Tuple([bop_739,call_742,var_743,uop_746,])
output2 = relay.Tuple([bop_739,call_744,var_743,uop_746,])
func_761 = relay.Function([var_737,var_743,], output)
mod['func_761'] = func_761
mod = relay.transform.InferType()(mod)
var_762 = relay.var("var_762", dtype = "int32", shape = (10, 3, 4))#candidate|762|(10, 3, 4)|var|int32
var_763 = relay.var("var_763", dtype = "uint64", shape = ())#candidate|763|()|var|uint64
output = func_761(var_762,var_763,)
func_764 = relay.Function([var_762,var_763,], output)
mutated_mod['func_764'] = func_764
mutated_mod = relay.transform.InferType()(mutated_mod)
const_916 = relay.const([[[1,4,-1,5,-9,7,-9,-10,2,4,8],[7,3,-7,4,-10,3,2,-9,8,-10,-7],[-2,3,6,6,-1,8,-4,6,-10,-4,-10],[-9,-3,-8,-1,-6,-3,9,-6,-1,-7,-1],[-7,-3,-5,10,-3,-8,-5,1,-3,-3,6],[6,-6,-9,8,-7,10,2,7,3,-2,-8],[9,-4,-8,1,-8,6,-3,-10,6,4,7],[1,7,-4,9,7,-3,2,-8,5,-7,-2],[7,-9,-9,-9,10,-2,8,-5,10,-2,-3],[-4,7,-6,10,7,10,-10,-1,-7,1,-8],[-5,-3,-7,8,3,-2,9,5,8,5,-7],[8,4,-9,-5,3,1,5,-4,9,-2,6],[-1,-1,4,-8,10,1,1,10,-8,-8,-8],[-7,5,-10,7,10,-8,6,6,-4,-9,-2],[-6,8,5,5,10,-8,9,2,5,-3,-3]]], dtype = "uint32")#candidate|916|(1, 15, 11)|const|uint32
var_917 = relay.var("var_917", dtype = "uint32", shape = (8, 15, 11))#candidate|917|(8, 15, 11)|var|uint32
bop_918 = relay.less_equal(const_916.astype('bool'), var_917.astype('bool')) # shape=(8, 15, 11)
func_492_call = mod.get_global_var('func_492')
func_494_call = mutated_mod.get_global_var('func_494')
const_933 = relay.const(4, dtype = "uint64")#candidate|933|()|const|uint64
call_932 = relay.TupleGetItem(func_492_call(relay.reshape(const_933.astype('uint64'), [])), 0)
call_934 = relay.TupleGetItem(func_494_call(relay.reshape(const_933.astype('uint64'), [])), 0)
func_418_call = mod.get_global_var('func_418')
func_421_call = mutated_mod.get_global_var('func_421')
var_949 = relay.var("var_949", dtype = "float64", shape = (26,))#candidate|949|(26,)|var|float64
call_948 = func_418_call(relay.reshape(const_933.astype('float64'), []), relay.reshape(var_949.astype('float64'), [2, 13, 1]), )
call_950 = func_418_call(relay.reshape(const_933.astype('float64'), []), relay.reshape(var_949.astype('float64'), [2, 13, 1]), )
bop_953 = relay.logical_or(call_948.astype('bool'), const_933.astype('bool')) # shape=(2, 13, 1)
bop_956 = relay.logical_or(call_950.astype('bool'), const_933.astype('bool')) # shape=(2, 13, 1)
bop_969 = relay.greater(var_949.astype('bool'), const_933.astype('bool')) # shape=(26,)
uop_977 = relay.atanh(bop_953.astype('float64')) # shape=(2, 13, 1)
uop_979 = relay.atanh(bop_956.astype('float64')) # shape=(2, 13, 1)
bop_980 = relay.equal(bop_969.astype('bool'), relay.reshape(uop_977.astype('bool'), relay.shape_of(bop_969))) # shape=(26,)
bop_983 = relay.equal(bop_969.astype('bool'), relay.reshape(uop_979.astype('bool'), relay.shape_of(bop_969))) # shape=(26,)
func_418_call = mod.get_global_var('func_418')
func_421_call = mutated_mod.get_global_var('func_421')
call_985 = func_418_call(relay.reshape(const_933.astype('float64'), []), relay.reshape(bop_953.astype('float64'), [2, 13, 1]), )
call_986 = func_418_call(relay.reshape(const_933.astype('float64'), []), relay.reshape(bop_953.astype('float64'), [2, 13, 1]), )
output = relay.Tuple([bop_918,call_932,bop_980,call_985,])
output2 = relay.Tuple([bop_918,call_934,bop_983,call_986,])
func_988 = relay.Function([var_917,var_949,], output)
mod['func_988'] = func_988
mod = relay.transform.InferType()(mod)
var_989 = relay.var("var_989", dtype = "uint32", shape = (8, 15, 11))#candidate|989|(8, 15, 11)|var|uint32
var_990 = relay.var("var_990", dtype = "float64", shape = (26,))#candidate|990|(26,)|var|float64
output = func_988(var_989,var_990,)
func_991 = relay.Function([var_989,var_990,], output)
mutated_mod['func_991'] = func_991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1135 = relay.var("var_1135", dtype = "float64", shape = (11, 5, 5))#candidate|1135|(11, 5, 5)|var|float64
uop_1136 = relay.log(var_1135.astype('float64')) # shape=(11, 5, 5)
output = uop_1136
output2 = uop_1136
func_1142 = relay.Function([var_1135,], output)
mod['func_1142'] = func_1142
mod = relay.transform.InferType()(mod)
var_1143 = relay.var("var_1143", dtype = "float64", shape = (11, 5, 5))#candidate|1143|(11, 5, 5)|var|float64
output = func_1142(var_1143)
func_1144 = relay.Function([var_1143], output)
mutated_mod['func_1144'] = func_1144
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1525 = relay.var("var_1525", dtype = "float32", shape = (13, 6, 1))#candidate|1525|(13, 6, 1)|var|float32
uop_1526 = relay.sinh(var_1525.astype('float32')) # shape=(13, 6, 1)
func_761_call = mod.get_global_var('func_761')
func_764_call = mutated_mod.get_global_var('func_764')
const_1529 = relay.const([-6,4,7,1,8,-5,2,10,3,-4,10,-9,4,-6,6,7,-8,-6,-4,10,-6,-5,-9,4,-2,-8,-8,7,10,6,-5,-1,-1,7,3,7,2,-8,7,-6,2,3,-2,10,6,-9,-9,1,7,-7,-5,10,8,-2,-9,6,-2,-9,-9,-8,7,3,10,-9,-4,-5,-3,-10,-4,8,9,-5,10,9,5,4,5,-9,3,-1,-6,-10,3,2,10,-1,3,-4,-9,4,-8,-5,6,-9,-4,10,7,1,-7,9,2,-8,5,-7,5,-8,10,10,-9,-6,9,5,5,-10,-10,2,7,6,-4,-6], dtype = "int32")#candidate|1529|(120,)|const|int32
var_1530 = relay.var("var_1530", dtype = "uint64", shape = ())#candidate|1530|()|var|uint64
call_1528 = relay.TupleGetItem(func_761_call(relay.reshape(const_1529.astype('int32'), [10, 3, 4]), relay.reshape(var_1530.astype('uint64'), []), ), 3)
call_1531 = relay.TupleGetItem(func_764_call(relay.reshape(const_1529.astype('int32'), [10, 3, 4]), relay.reshape(var_1530.astype('uint64'), []), ), 3)
func_443_call = mod.get_global_var('func_443')
func_447_call = mutated_mod.get_global_var('func_447')
var_1537 = relay.var("var_1537", dtype = "int16", shape = (7, 9))#candidate|1537|(7, 9)|var|int16
const_1538 = relay.const([6.864679,-3.235420,4.577491,-0.704525,7.633619,5.501389,1.083541,-5.654730,-0.855162,2.003868,0.660610,-5.173681,-1.499865,3.271406,-3.761233,4.166058,2.853714,7.767141,-6.685148,-0.306524,7.146490,-3.462802,-3.125440,-2.977257,-5.405732,8.140444], dtype = "float64")#candidate|1538|(26,)|const|float64
call_1536 = relay.TupleGetItem(func_443_call(relay.reshape(var_1530.astype('int16'), []), relay.reshape(var_1537.astype('int16'), [3, 3, 7]), relay.reshape(const_1538.astype('float64'), [26,]), ), 2)
call_1539 = relay.TupleGetItem(func_447_call(relay.reshape(var_1530.astype('int16'), []), relay.reshape(var_1537.astype('int16'), [3, 3, 7]), relay.reshape(const_1538.astype('float64'), [26,]), ), 2)
func_492_call = mod.get_global_var('func_492')
func_494_call = mutated_mod.get_global_var('func_494')
call_1546 = relay.TupleGetItem(func_492_call(relay.reshape(var_1530.astype('uint64'), [])), 0)
call_1547 = relay.TupleGetItem(func_494_call(relay.reshape(var_1530.astype('uint64'), [])), 0)
func_492_call = mod.get_global_var('func_492')
func_494_call = mutated_mod.get_global_var('func_494')
call_1554 = relay.TupleGetItem(func_492_call(relay.reshape(var_1530.astype('uint64'), [])), 0)
call_1555 = relay.TupleGetItem(func_494_call(relay.reshape(var_1530.astype('uint64'), [])), 0)
output = relay.Tuple([uop_1526,call_1528,const_1529,var_1530,call_1536,var_1537,const_1538,call_1546,call_1554,])
output2 = relay.Tuple([uop_1526,call_1531,const_1529,var_1530,call_1539,var_1537,const_1538,call_1547,call_1555,])
func_1577 = relay.Function([var_1525,var_1530,var_1537,], output)
mod['func_1577'] = func_1577
mod = relay.transform.InferType()(mod)
mutated_mod['func_1577'] = func_1577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1577_call = mutated_mod.get_global_var('func_1577')
var_1579 = relay.var("var_1579", dtype = "float32", shape = (13, 6, 1))#candidate|1579|(13, 6, 1)|var|float32
var_1580 = relay.var("var_1580", dtype = "uint64", shape = ())#candidate|1580|()|var|uint64
var_1581 = relay.var("var_1581", dtype = "int16", shape = (7, 9))#candidate|1581|(7, 9)|var|int16
call_1578 = func_1577_call(var_1579,var_1580,var_1581,)
output = call_1578
func_1582 = relay.Function([var_1579,var_1580,var_1581,], output)
mutated_mod['func_1582'] = func_1582
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1840 = relay.var("var_1840", dtype = "float32", shape = (2, 16, 15))#candidate|1840|(2, 16, 15)|var|float32
uop_1841 = relay.log2(var_1840.astype('float32')) # shape=(2, 16, 15)
func_492_call = mod.get_global_var('func_492')
func_494_call = mutated_mod.get_global_var('func_494')
const_1856 = relay.const(-7, dtype = "uint64")#candidate|1856|()|const|uint64
call_1855 = relay.TupleGetItem(func_492_call(relay.reshape(const_1856.astype('uint64'), [])), 0)
call_1857 = relay.TupleGetItem(func_494_call(relay.reshape(const_1856.astype('uint64'), [])), 0)
uop_1871 = relay.atan(uop_1841.astype('float32')) # shape=(2, 16, 15)
output = relay.Tuple([call_1855,const_1856,uop_1871,])
output2 = relay.Tuple([call_1857,const_1856,uop_1871,])
func_1890 = relay.Function([var_1840,], output)
mod['func_1890'] = func_1890
mod = relay.transform.InferType()(mod)
mutated_mod['func_1890'] = func_1890
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1891 = relay.var("var_1891", dtype = "float32", shape = (2, 16, 15))#candidate|1891|(2, 16, 15)|var|float32
func_1890_call = mutated_mod.get_global_var('func_1890')
call_1892 = func_1890_call(var_1891)
output = call_1892
func_1893 = relay.Function([var_1891], output)
mutated_mod['func_1893'] = func_1893
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1943 = relay.var("var_1943", dtype = "int16", shape = (14, 14, 8))#candidate|1943|(14, 14, 8)|var|int16
var_1944 = relay.var("var_1944", dtype = "int16", shape = (14, 14, 8))#candidate|1944|(14, 14, 8)|var|int16
bop_1945 = relay.equal(var_1943.astype('bool'), relay.reshape(var_1944.astype('bool'), relay.shape_of(var_1943))) # shape=(14, 14, 8)
output = bop_1945
output2 = bop_1945
func_1965 = relay.Function([var_1943,var_1944,], output)
mod['func_1965'] = func_1965
mod = relay.transform.InferType()(mod)
mutated_mod['func_1965'] = func_1965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1965_call = mutated_mod.get_global_var('func_1965')
var_1967 = relay.var("var_1967", dtype = "int16", shape = (14, 14, 8))#candidate|1967|(14, 14, 8)|var|int16
var_1968 = relay.var("var_1968", dtype = "int16", shape = (14, 14, 8))#candidate|1968|(14, 14, 8)|var|int16
call_1966 = func_1965_call(var_1967,var_1968,)
output = call_1966
func_1969 = relay.Function([var_1967,var_1968,], output)
mutated_mod['func_1969'] = func_1969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2340 = relay.var("var_2340", dtype = "int32", shape = (15, 1, 6))#candidate|2340|(15, 1, 6)|var|int32
const_2341 = relay.const([[[-6,8,5,-9,-2,4],[-5,8,2,-2,8,10],[-7,-4,-5,2,6,-3],[9,-5,-9,6,6,3],[-2,9,-5,3,-5,-4],[8,2,-7,4,-7,8],[10,9,9,-3,9,10],[2,5,-8,6,6,-9],[-2,-10,2,6,-3,9],[1,3,-4,5,6,-3],[-10,10,8,-10,2,1],[9,9,6,-7,8,8],[-3,-7,-2,1,9,9]],[[-3,-8,-10,-1,10,-4],[6,3,9,7,4,-1],[4,10,5,3,-10,-3],[3,1,5,-10,-5,6],[-4,-6,-9,-7,-8,8],[-10,-1,3,-1,9,-10],[7,5,4,-8,6,-9],[2,8,6,-5,-9,7],[10,10,1,-4,-1,2],[2,-4,-3,-5,-10,5],[1,10,-8,-5,6,10],[7,-6,4,-6,8,-9],[2,6,-7,7,2,-9]],[[6,-9,-9,-2,2,7],[-5,-6,-2,4,9,7],[10,5,3,10,-7,-2],[7,-5,1,9,-4,1],[-2,-1,6,8,-1,-7],[6,-4,10,1,9,8],[-7,-9,2,8,-6,4],[4,9,-4,10,6,2],[9,3,9,-1,8,9],[2,3,-4,-2,-8,6],[7,-1,9,1,7,9],[5,2,1,-3,-1,-1],[-5,5,-3,-7,-6,-5]],[[2,-4,-10,-4,-4,10],[10,-6,-2,-5,-1,-2],[1,3,6,4,-4,6],[3,8,-6,3,-4,6],[8,-2,-2,-1,4,10],[-2,9,-3,9,-6,-3],[9,-10,-5,-8,-10,1],[-7,-4,-6,4,-1,5],[9,-1,-5,7,10,-5],[-4,7,-7,5,-1,-6],[5,7,2,-1,-8,-4],[-7,-6,-6,2,-6,-3],[7,9,-7,5,3,-10]],[[-3,-6,1,5,2,-5],[-4,10,5,-5,1,10],[-6,-10,4,8,10,10],[5,-1,9,-5,4,3],[9,2,1,-8,7,-8],[7,-10,-9,8,8,-10],[7,7,1,1,-7,1],[-6,-5,-6,-4,8,-2],[4,2,1,-6,7,2],[-5,-9,-7,-10,-9,8],[7,-2,5,3,-4,-3],[7,5,-5,4,-9,2],[-5,-1,-7,-4,10,-3]],[[-8,6,1,10,9,4],[2,5,2,9,2,-4],[8,5,-3,-3,-5,4],[-6,-6,10,2,7,-7],[-5,-8,6,-5,-1,-10],[-1,7,2,1,-8,7],[-6,-1,-6,-4,5,-9],[-6,-5,7,3,-10,3],[4,10,-1,-9,5,2],[8,-2,9,-6,-6,-6],[-8,-2,-1,-10,8,-6],[-8,8,7,-5,-7,10],[8,3,-8,-8,9,-5]],[[-4,-7,7,-1,-10,-8],[-10,-4,2,5,3,-8],[8,-7,8,7,-9,4],[8,10,-6,-9,-3,-5],[8,-7,-9,-1,-10,4],[-10,-8,5,-4,-9,3],[5,4,-4,3,1,4],[-2,7,-3,10,9,-4],[-1,-7,3,6,3,-5],[10,-10,7,-9,1,3],[-6,-9,4,-9,-4,-7],[-10,6,-4,-2,-9,3],[8,-7,9,-5,6,2]],[[-7,-4,9,7,-6,-5],[-4,-3,1,10,-2,-10],[-10,8,9,3,10,9],[9,-1,1,-5,4,1],[-6,9,-10,8,4,-4],[-5,10,-6,-5,9,2],[-3,-6,-5,-6,-7,-10],[4,7,-4,-10,9,2],[-3,2,6,-9,-1,8],[1,8,9,-3,3,-10],[2,-6,1,6,-9,-5],[2,-4,10,-8,7,7],[3,-8,1,-5,-7,-1]],[[3,4,8,6,5,3],[-1,-6,-9,4,-6,-10],[10,9,-8,-8,10,2],[-1,-7,8,4,3,10],[5,-3,8,-8,-1,-6],[7,-2,5,-4,4,-3],[-3,2,8,-7,-7,4],[8,-2,8,7,-1,2],[-3,-2,-8,-9,-3,7],[4,4,8,7,-1,2],[8,-3,-8,-4,-1,-8],[-3,-10,-8,10,2,-3],[4,-4,-10,4,-8,6]],[[-4,-7,-1,6,3,-2],[4,5,8,8,-10,10],[-1,-8,3,-4,-6,-4],[7,-1,-7,-3,7,-8],[-6,8,9,5,-2,10],[7,-4,5,10,-7,4],[5,6,-5,-6,1,8],[2,3,-6,-1,4,-6],[3,-5,-8,-4,-8,3],[-5,4,-5,-7,6,2],[2,3,-9,7,6,2],[-2,-4,-7,4,8,-9],[2,9,-7,-8,-6,-4]],[[-3,-7,-2,-10,7,5],[-3,-7,8,-3,1,8],[4,-4,-10,-7,9,9],[-5,8,-5,8,-5,-8],[-9,3,4,10,9,10],[2,2,3,5,-10,-10],[9,2,2,-4,2,3],[-3,2,6,-3,9,-2],[-7,-10,3,4,9,3],[-8,2,-8,-6,5,3],[1,-2,1,5,-4,-7],[-7,6,-8,7,7,8],[4,4,-1,3,-5,2]],[[-10,6,-4,-8,3,-6],[4,-9,-5,-4,-10,-8],[-7,2,-7,-10,3,-10],[8,-7,3,-3,9,8],[10,2,-2,2,-3,-3],[-3,7,8,5,7,-8],[7,7,-5,1,9,-9],[6,-2,8,-1,-8,-6],[-8,-4,-5,7,-4,-10],[-1,8,6,1,-9,-3],[8,-7,-6,5,-8,-1],[1,-4,4,8,5,-5],[1,5,9,-8,-5,3]],[[2,7,7,10,8,5],[-6,-7,-8,3,8,-1],[5,-2,-6,10,-1,5],[-5,-7,9,-4,6,-5],[4,4,-6,-7,-6,-9],[-3,10,8,-5,-10,-7],[-4,-1,4,5,-6,10],[-5,2,7,4,4,8],[-7,6,-3,6,8,10],[-5,-10,3,2,-8,-9],[-8,6,5,4,7,1],[5,-9,-5,4,5,3],[-3,-8,-1,-5,10,-9]],[[-7,8,2,-4,-7,1],[4,-3,7,-7,-3,3],[-1,-3,2,-7,4,3],[-7,5,9,-7,1,-2],[-4,-1,5,10,-2,9],[6,5,5,8,-2,-7],[10,4,2,10,-6,-6],[4,-6,-9,-2,-3,7],[-2,2,-9,-7,-3,-2],[8,4,4,-4,3,7],[-7,9,6,9,-2,-6],[-10,-1,3,-7,-7,6],[8,-2,-9,7,7,-5]],[[-3,-5,-3,-5,1,5],[1,-8,2,10,1,5],[8,-6,-9,2,-3,-8],[-5,1,-10,3,-8,-10],[4,-2,-9,-6,8,-5],[-3,10,3,4,2,-5],[2,4,10,10,-3,10],[-7,10,-8,-2,-2,-7],[-2,-3,6,7,-8,8],[6,-2,10,10,10,-5],[-4,9,1,9,9,-8],[-9,-5,-5,-5,-2,-7],[-2,-2,-6,3,5,-6]]], dtype = "int32")#candidate|2341|(15, 13, 6)|const|int32
bop_2342 = relay.greater_equal(var_2340.astype('bool'), const_2341.astype('bool')) # shape=(15, 13, 6)
var_2354 = relay.var("var_2354", dtype = "int32", shape = (15, 13, 6))#candidate|2354|(15, 13, 6)|var|int32
bop_2355 = relay.logical_xor(var_2340.astype('int16'), var_2354.astype('int16')) # shape=(15, 13, 6)
func_492_call = mod.get_global_var('func_492')
func_494_call = mutated_mod.get_global_var('func_494')
const_2360 = relay.const(-7, dtype = "uint64")#candidate|2360|()|const|uint64
call_2359 = relay.TupleGetItem(func_492_call(relay.reshape(const_2360.astype('uint64'), [])), 0)
call_2361 = relay.TupleGetItem(func_494_call(relay.reshape(const_2360.astype('uint64'), [])), 0)
bop_2365 = relay.bitwise_xor(bop_2355.astype('uint64'), var_2340.astype('uint64')) # shape=(15, 13, 6)
func_418_call = mod.get_global_var('func_418')
func_421_call = mutated_mod.get_global_var('func_421')
var_2373 = relay.var("var_2373", dtype = "float64", shape = (26,))#candidate|2373|(26,)|var|float64
call_2372 = func_418_call(relay.reshape(const_2360.astype('float64'), []), relay.reshape(var_2373.astype('float64'), [2, 13, 1]), )
call_2374 = func_418_call(relay.reshape(const_2360.astype('float64'), []), relay.reshape(var_2373.astype('float64'), [2, 13, 1]), )
output = relay.Tuple([bop_2342,call_2359,const_2360,bop_2365,call_2372,var_2373,])
output2 = relay.Tuple([bop_2342,call_2361,const_2360,bop_2365,call_2374,var_2373,])
func_2375 = relay.Function([var_2340,var_2354,var_2373,], output)
mod['func_2375'] = func_2375
mod = relay.transform.InferType()(mod)
var_2376 = relay.var("var_2376", dtype = "int32", shape = (15, 1, 6))#candidate|2376|(15, 1, 6)|var|int32
var_2377 = relay.var("var_2377", dtype = "int32", shape = (15, 13, 6))#candidate|2377|(15, 13, 6)|var|int32
var_2378 = relay.var("var_2378", dtype = "float64", shape = (26,))#candidate|2378|(26,)|var|float64
output = func_2375(var_2376,var_2377,var_2378,)
func_2379 = relay.Function([var_2376,var_2377,var_2378,], output)
mutated_mod['func_2379'] = func_2379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2510 = relay.var("var_2510", dtype = "float64", shape = ())#candidate|2510|()|var|float64
var_2511 = relay.var("var_2511", dtype = "float64", shape = (16, 16, 12))#candidate|2511|(16, 16, 12)|var|float64
bop_2512 = relay.minimum(var_2510.astype('float64'), var_2511.astype('float64')) # shape=(16, 16, 12)
func_2375_call = mod.get_global_var('func_2375')
func_2379_call = mutated_mod.get_global_var('func_2379')
const_2521 = relay.const([-3,7,-8,-7,10,7,-6,-8,-9,-2,-7,8,-4,-4,9,-2,8,4,-2,6,-8,-7,-4,-7,-7,3,-7,4,7,8,5,8,1,-1,5,-4,-10,9,-7,-6,-5,-8,1,4,10,-6,3,-10,8,-7,9,-5,-4,3,-1,6,10,-8,8,1,-5,-4,-10,3,4,-10,3,3,10,-1,-7,-8,-2,9,2,9,6,-6,-6,4,-2,6,-10,3,7,2,10,4,-8,-4], dtype = "int32")#candidate|2521|(90,)|const|int32
const_2522 = relay.const([[-8,5,-1,9,-7,8,-1,5,6,-4,-10,5,-2,10,10,-10,-9,4,-9,4,5,10,-2,9,-7,-8,-6,2,10,9,-4,-10,-3,4,9,-1,-4,2,8,-4,2,1,5,-5,5,-6,-2,-5,1,10,9,-4,-10,9,-6,2,4,-6,-9,5,5,-5,6,-2,9,-8,-1,1,9,-1,10,-4,9,3,-1,1,10,2,8,-4,6,-5,-4,-2,4,-7,9,1,1,5,4,7,4,9,-3,-6,5,-8,8,10,-5,8,-6,3,3,-9,-4,9,4,-9,-1,6,8,2,5,-8,9,-6,3,4,7,-4,-10,10,-3,10,4,9,-1,-8,3,7,-1,8,-2,3,8,10,-10,-1,-9,-6,-1,7,-6,-8,-2,-2,10,9,2,9,7,7,10,-10,-3,2,-9,-7,3,-3,-2,7,5,-4,-6,-9,4,2,-8,-3,-7,6,-3,3,8,-10,-3,4,3,-6,-3,-5,5,-3,8,-3,-8,-4,-9,8,5,10,8,-5,-4,-1,-10,-7,4,7,3,-10,8,-5,-1,6,2,-5,2,1,-2,6,-1,-6,-1,6,2,7,1,9,-5,-9,3,-5,-3,2,1,7,10,-6,8,-7],[9,10,-7,2,-4,-9,7,3,-2,-5,-2,4,10,5,1,6,-5,10,7,-2,-4,-7,6,-1,4,1,10,10,-5,-8,4,-8,2,10,1,10,6,-8,-7,1,7,-9,-1,-7,-5,-5,-8,-9,3,10,5,3,7,-4,-10,-8,-8,6,-10,-6,-7,-4,-5,7,-4,4,-7,1,-8,-10,9,-7,-9,-6,5,1,-2,9,8,5,-5,1,6,7,4,-2,7,10,10,4,8,7,10,9,-2,-2,-5,-10,-7,-3,-6,4,4,-9,1,-10,-9,-9,5,-9,-4,5,-7,10,-1,5,-2,1,4,-10,3,4,-1,3,2,-2,-4,-8,3,5,5,-3,10,2,-6,-8,6,-1,6,-2,5,-9,-2,-1,8,-1,5,-9,10,8,-6,2,-10,-9,-6,-9,7,-1,-6,6,-8,7,2,8,-9,-7,5,-7,6,-3,8,-5,-1,-4,1,-1,8,4,-5,-6,-1,9,4,-2,3,3,1,-6,6,-9,1,-6,7,-3,-4,-7,1,4,-4,-6,-4,-10,-8,-7,-10,3,-6,2,-1,-8,-3,-2,2,2,2,7,-8,3,7,2,8,-9,-4,-10,8,-10,4,7,-7,6,-6,7,1,-2],[2,4,-9,4,5,-10,3,-6,-3,-7,-2,2,-5,2,1,-4,9,-2,-2,4,4,4,4,-6,-3,-7,-5,4,10,-8,1,-3,-10,9,-5,3,6,7,-7,7,8,-6,-5,-5,-8,7,4,10,-6,8,-3,-1,8,9,10,5,9,3,4,10,-10,1,-6,-8,3,4,-8,-5,4,10,-9,4,-8,4,2,2,-9,-7,-6,-9,-2,-7,9,-7,-5,7,-1,3,-5,-1,-9,2,-10,4,4,6,-6,8,-4,-8,-9,-4,5,2,-4,-8,8,2,-9,-3,-2,10,-2,3,3,-5,-6,7,-8,-1,3,-7,3,10,-8,6,-4,7,-7,1,2,4,-5,-1,-9,-5,-6,-3,4,1,-6,3,5,5,-10,2,2,-4,-7,2,-7,-10,1,-2,-9,-8,-9,-5,1,-6,6,-7,-6,-7,-5,-10,-6,-7,-4,-2,1,-7,1,3,-4,4,-9,-10,1,-7,-6,9,5,-9,-5,1,-10,-6,-2,4,-10,-8,9,-1,7,9,2,7,5,8,6,-6,8,1,1,-6,4,-7,5,-7,5,-8,-3,-6,-1,-8,4,5,-6,-1,-2,5,2,2,1,10,3,-2,-2,-7,-3,-2,-9,-8],[-5,-1,6,4,-9,7,-4,-7,-6,-5,7,3,-7,6,4,-10,-1,-6,8,-6,6,8,-10,-9,3,-7,8,-2,-5,-2,2,-5,-2,1,1,-8,3,-9,10,-1,3,-3,8,-7,-4,9,10,1,7,3,-3,6,-6,1,2,9,8,10,7,-8,-6,-1,2,-2,5,-8,-8,-4,-1,10,-7,-1,-1,10,8,-3,6,3,-7,9,-2,-10,-5,-5,-1,10,-4,-2,1,6,-1,-8,-4,-7,5,3,-4,8,-1,-6,7,-2,-6,-9,8,10,6,-8,-8,3,10,-1,-3,6,1,8,-7,-9,7,-3,5,6,-1,4,-7,3,7,4,4,-5,1,10,-6,-2,-9,9,8,7,-10,-9,10,-6,5,-4,-9,3,-4,9,-4,-2,6,8,7,-3,6,5,3,10,3,-8,-5,-4,4,9,-2,2,2,-2,-5,5,-7,7,2,-10,5,9,7,-1,5,-10,10,-7,-3,-1,-5,2,-7,-4,10,5,-1,7,6,-10,7,9,3,-2,-4,7,-9,1,-9,4,8,7,4,7,2,-2,-9,-8,7,-9,3,10,4,-6,6,-2,-3,-4,-3,-8,10,5,3,2,-3,2,-6,6,2,4],[-5,-2,7,5,9,-6,7,10,5,1,4,4,6,1,5,7,4,-8,7,1,-9,7,-8,-6,-9,-3,-2,3,10,-5,-1,-4,-2,-4,-6,-5,1,2,8,-4,-7,-10,-3,-5,8,7,2,4,4,3,4,6,9,-5,-6,-4,6,-1,6,4,-8,5,2,2,-7,5,-2,-7,9,-7,-2,7,4,9,-4,4,-3,1,-8,9,-7,-7,7,1,-7,-8,-9,9,5,-3,-2,-10,-6,8,4,-1,4,-2,-3,7,-1,-1,2,-4,-1,-5,-4,5,7,-5,-5,-4,6,1,6,9,5,-8,1,3,8,4,4,-5,-5,4,7,-10,-3,-2,9,6,3,-10,-7,8,-2,9,-2,-8,5,8,9,6,-8,-1,-10,-10,1,7,2,3,-6,9,7,6,1,-3,-3,-2,-7,-10,2,-10,-2,10,2,8,-8,-7,-6,8,-8,-8,9,-4,5,-3,-3,-9,-10,9,-6,2,-7,10,4,1,-8,5,-10,-4,-2,-9,2,2,-9,-5,-1,9,-6,1,5,-3,10,-10,8,5,-5,-7,-4,-10,-1,8,-10,7,-5,7,10,-5,-2,3,3,2,-2,-4,7,1,-8,9,5,-5,6,-4]], dtype = "int32")#candidate|2522|(5, 234)|const|int32
var_2523 = relay.var("var_2523", dtype = "float64", shape = (26,))#candidate|2523|(26,)|var|float64
call_2520 = relay.TupleGetItem(func_2375_call(relay.reshape(const_2521.astype('int32'), [15, 1, 6]), relay.reshape(const_2522.astype('int32'), [15, 13, 6]), relay.reshape(var_2523.astype('float64'), [26,]), ), 5)
call_2524 = relay.TupleGetItem(func_2379_call(relay.reshape(const_2521.astype('int32'), [15, 1, 6]), relay.reshape(const_2522.astype('int32'), [15, 13, 6]), relay.reshape(var_2523.astype('float64'), [26,]), ), 5)
output = relay.Tuple([bop_2512,call_2520,const_2521,const_2522,var_2523,])
output2 = relay.Tuple([bop_2512,call_2524,const_2521,const_2522,var_2523,])
func_2531 = relay.Function([var_2510,var_2511,var_2523,], output)
mod['func_2531'] = func_2531
mod = relay.transform.InferType()(mod)
mutated_mod['func_2531'] = func_2531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2531_call = mutated_mod.get_global_var('func_2531')
var_2533 = relay.var("var_2533", dtype = "float64", shape = ())#candidate|2533|()|var|float64
var_2534 = relay.var("var_2534", dtype = "float64", shape = (16, 16, 12))#candidate|2534|(16, 16, 12)|var|float64
var_2535 = relay.var("var_2535", dtype = "float64", shape = (26,))#candidate|2535|(26,)|var|float64
call_2532 = func_2531_call(var_2533,var_2534,var_2535,)
output = call_2532
func_2536 = relay.Function([var_2533,var_2534,var_2535,], output)
mutated_mod['func_2536'] = func_2536
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2630 = relay.var("var_2630", dtype = "bool", shape = (3, 16, 6))#candidate|2630|(3, 16, 6)|var|bool
const_2631 = relay.const([[[False,False,False,True,False,False],[False,False,False,False,False,False],[False,True,True,True,True,True],[True,True,True,False,False,False],[False,False,True,True,True,False],[True,True,False,False,True,True],[False,True,True,False,False,True],[True,False,True,False,False,False],[True,True,True,False,True,True],[True,True,True,False,True,True],[False,False,False,True,False,True],[False,False,True,True,True,True],[False,False,True,True,False,True],[True,True,False,False,False,True],[False,True,True,True,True,False],[False,True,False,True,False,True]],[[False,False,True,True,True,False],[False,False,False,False,True,False],[True,True,False,False,True,False],[True,True,True,False,True,False],[False,True,True,True,False,False],[False,True,False,True,False,False],[False,True,False,False,True,True],[True,False,False,True,False,False],[True,False,True,False,False,False],[False,True,False,True,False,False],[True,False,True,False,True,False],[False,True,True,False,False,False],[True,True,False,False,False,True],[False,True,True,True,True,True],[False,True,False,False,False,False],[False,False,False,False,False,False]],[[False,False,True,True,False,True],[True,True,False,True,True,False],[False,True,True,True,True,False],[True,True,True,True,True,False],[False,True,False,False,True,False],[False,True,False,False,False,False],[True,True,True,False,True,True],[False,True,False,False,True,True],[False,False,False,False,True,True],[False,True,True,False,False,False],[False,False,False,False,False,False],[False,False,False,True,False,True],[False,False,False,True,False,True],[False,True,True,True,True,True],[False,True,False,True,True,False],[False,True,True,False,True,True]]], dtype = "bool")#candidate|2631|(3, 16, 6)|const|bool
bop_2632 = relay.logical_or(var_2630.astype('bool'), relay.reshape(const_2631.astype('bool'), relay.shape_of(var_2630))) # shape=(3, 16, 6)
output = relay.Tuple([bop_2632,])
output2 = relay.Tuple([bop_2632,])
func_2639 = relay.Function([var_2630,], output)
mod['func_2639'] = func_2639
mod = relay.transform.InferType()(mod)
mutated_mod['func_2639'] = func_2639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2640 = relay.var("var_2640", dtype = "bool", shape = (3, 16, 6))#candidate|2640|(3, 16, 6)|var|bool
func_2639_call = mutated_mod.get_global_var('func_2639')
call_2641 = func_2639_call(var_2640)
output = call_2641
func_2642 = relay.Function([var_2640], output)
mutated_mod['func_2642'] = func_2642
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3208 = relay.var("var_3208", dtype = "float32", shape = (6, 7, 13))#candidate|3208|(6, 7, 13)|var|float32
uop_3209 = relay.log10(var_3208.astype('float32')) # shape=(6, 7, 13)
output = relay.Tuple([uop_3209,])
output2 = relay.Tuple([uop_3209,])
func_3222 = relay.Function([var_3208,], output)
mod['func_3222'] = func_3222
mod = relay.transform.InferType()(mod)
mutated_mod['func_3222'] = func_3222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3223 = relay.var("var_3223", dtype = "float32", shape = (6, 7, 13))#candidate|3223|(6, 7, 13)|var|float32
func_3222_call = mutated_mod.get_global_var('func_3222')
call_3224 = func_3222_call(var_3223)
output = call_3224
func_3225 = relay.Function([var_3223], output)
mutated_mod['func_3225'] = func_3225
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3229 = relay.var("var_3229", dtype = "float64", shape = (8, 8, 13))#candidate|3229|(8, 8, 13)|var|float64
var_3230 = relay.var("var_3230", dtype = "float64", shape = (8, 8, 13))#candidate|3230|(8, 8, 13)|var|float64
bop_3231 = relay.equal(var_3229.astype('bool'), relay.reshape(var_3230.astype('bool'), relay.shape_of(var_3229))) # shape=(8, 8, 13)
uop_3242 = relay.sqrt(bop_3231.astype('float64')) # shape=(8, 8, 13)
output = relay.Tuple([uop_3242,])
output2 = relay.Tuple([uop_3242,])
func_3244 = relay.Function([var_3229,var_3230,], output)
mod['func_3244'] = func_3244
mod = relay.transform.InferType()(mod)
var_3245 = relay.var("var_3245", dtype = "float64", shape = (8, 8, 13))#candidate|3245|(8, 8, 13)|var|float64
var_3246 = relay.var("var_3246", dtype = "float64", shape = (8, 8, 13))#candidate|3246|(8, 8, 13)|var|float64
output = func_3244(var_3245,var_3246,)
func_3247 = relay.Function([var_3245,var_3246,], output)
mutated_mod['func_3247'] = func_3247
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3470 = relay.var("var_3470", dtype = "float32", shape = (16, 4, 6))#candidate|3470|(16, 4, 6)|var|float32
uop_3471 = relay.atan(var_3470.astype('float32')) # shape=(16, 4, 6)
output = uop_3471
output2 = uop_3471
func_3477 = relay.Function([var_3470,], output)
mod['func_3477'] = func_3477
mod = relay.transform.InferType()(mod)
mutated_mod['func_3477'] = func_3477
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3478 = relay.var("var_3478", dtype = "float32", shape = (16, 4, 6))#candidate|3478|(16, 4, 6)|var|float32
func_3477_call = mutated_mod.get_global_var('func_3477')
call_3479 = func_3477_call(var_3478)
output = call_3479
func_3480 = relay.Function([var_3478], output)
mutated_mod['func_3480'] = func_3480
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3482 = relay.var("var_3482", dtype = "float64", shape = ())#candidate|3482|()|var|float64
var_3483 = relay.var("var_3483", dtype = "float64", shape = (9, 7, 1))#candidate|3483|(9, 7, 1)|var|float64
bop_3484 = relay.multiply(var_3482.astype('float64'), var_3483.astype('float64')) # shape=(9, 7, 1)
uop_3488 = relay.exp(bop_3484.astype('float64')) # shape=(9, 7, 1)
func_1142_call = mod.get_global_var('func_1142')
func_1144_call = mutated_mod.get_global_var('func_1144')
var_3495 = relay.var("var_3495", dtype = "float64", shape = (275,))#candidate|3495|(275,)|var|float64
call_3494 = func_1142_call(relay.reshape(var_3495.astype('float64'), [11, 5, 5]))
call_3496 = func_1142_call(relay.reshape(var_3495.astype('float64'), [11, 5, 5]))
bop_3500 = relay.left_shift(uop_3488.astype('uint64'), relay.reshape(var_3483.astype('uint64'), relay.shape_of(uop_3488))) # shape=(9, 7, 1)
output = relay.Tuple([call_3494,var_3495,bop_3500,])
output2 = relay.Tuple([call_3496,var_3495,bop_3500,])
func_3505 = relay.Function([var_3482,var_3483,var_3495,], output)
mod['func_3505'] = func_3505
mod = relay.transform.InferType()(mod)
mutated_mod['func_3505'] = func_3505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3505_call = mutated_mod.get_global_var('func_3505')
var_3507 = relay.var("var_3507", dtype = "float64", shape = ())#candidate|3507|()|var|float64
var_3508 = relay.var("var_3508", dtype = "float64", shape = (9, 7, 1))#candidate|3508|(9, 7, 1)|var|float64
var_3509 = relay.var("var_3509", dtype = "float64", shape = (275,))#candidate|3509|(275,)|var|float64
call_3506 = func_3505_call(var_3507,var_3508,var_3509,)
output = call_3506
func_3510 = relay.Function([var_3507,var_3508,var_3509,], output)
mutated_mod['func_3510'] = func_3510
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3659 = relay.var("var_3659", dtype = "float64", shape = (16, 4, 13))#candidate|3659|(16, 4, 13)|var|float64
uop_3660 = relay.atanh(var_3659.astype('float64')) # shape=(16, 4, 13)
output = uop_3660
output2 = uop_3660
func_3675 = relay.Function([var_3659,], output)
mod['func_3675'] = func_3675
mod = relay.transform.InferType()(mod)
mutated_mod['func_3675'] = func_3675
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3676 = relay.var("var_3676", dtype = "float64", shape = (16, 4, 13))#candidate|3676|(16, 4, 13)|var|float64
func_3675_call = mutated_mod.get_global_var('func_3675')
call_3677 = func_3675_call(var_3676)
output = call_3677
func_3678 = relay.Function([var_3676], output)
mutated_mod['func_3678'] = func_3678
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3812 = relay.const([[[10,2]],[[-7,-3]],[[-4,8]],[[4,-5]],[[5,9]],[[5,-3]],[[-3,1]],[[2,2]],[[7,4]],[[-7,-2]],[[5,2]]], dtype = "int16")#candidate|3812|(11, 1, 2)|const|int16
var_3813 = relay.var("var_3813", dtype = "int16", shape = (11, 15, 2))#candidate|3813|(11, 15, 2)|var|int16
bop_3814 = relay.maximum(const_3812.astype('int16'), var_3813.astype('int16')) # shape=(11, 15, 2)
uop_3823 = relay.sin(var_3813.astype('float32')) # shape=(11, 15, 2)
output = relay.Tuple([bop_3814,uop_3823,])
output2 = relay.Tuple([bop_3814,uop_3823,])
func_3831 = relay.Function([var_3813,], output)
mod['func_3831'] = func_3831
mod = relay.transform.InferType()(mod)
var_3832 = relay.var("var_3832", dtype = "int16", shape = (11, 15, 2))#candidate|3832|(11, 15, 2)|var|int16
output = func_3831(var_3832)
func_3833 = relay.Function([var_3832], output)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3958 = relay.var("var_3958", dtype = "int32", shape = (7, 13, 3))#candidate|3958|(7, 13, 3)|var|int32
var_3959 = relay.var("var_3959", dtype = "int32", shape = (7, 13, 3))#candidate|3959|(7, 13, 3)|var|int32
bop_3960 = relay.greater_equal(var_3958.astype('bool'), relay.reshape(var_3959.astype('bool'), relay.shape_of(var_3958))) # shape=(7, 13, 3)
output = relay.Tuple([bop_3960,])
output2 = relay.Tuple([bop_3960,])
func_3977 = relay.Function([var_3958,var_3959,], output)
mod['func_3977'] = func_3977
mod = relay.transform.InferType()(mod)
var_3978 = relay.var("var_3978", dtype = "int32", shape = (7, 13, 3))#candidate|3978|(7, 13, 3)|var|int32
var_3979 = relay.var("var_3979", dtype = "int32", shape = (7, 13, 3))#candidate|3979|(7, 13, 3)|var|int32
output = func_3977(var_3978,var_3979,)
func_3980 = relay.Function([var_3978,var_3979,], output)
mutated_mod['func_3980'] = func_3980
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4228 = relay.const([[[-9.256449],[-5.957869],[8.905060],[-1.440471],[-6.365784]],[[4.022143],[-0.926844],[3.527754],[7.882500],[4.957677]]], dtype = "float32")#candidate|4228|(2, 5, 1)|const|float32
uop_4229 = relay.log(const_4228.astype('float32')) # shape=(2, 5, 1)
bop_4242 = relay.add(uop_4229.astype('int32'), relay.reshape(const_4228.astype('int32'), relay.shape_of(uop_4229))) # shape=(2, 5, 1)
bop_4245 = relay.floor_divide(const_4228.astype('float64'), relay.reshape(bop_4242.astype('float64'), relay.shape_of(const_4228))) # shape=(2, 5, 1)
output = bop_4245
output2 = bop_4245
func_4250 = relay.Function([], output)
mod['func_4250'] = func_4250
mod = relay.transform.InferType()(mod)
output = func_4250()
func_4251 = relay.Function([], output)
mutated_mod['func_4251'] = func_4251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_4268 = func_4250_call()
call_4269 = func_4250_call()
uop_4273 = relay.asinh(call_4268.astype('float64')) # shape=(2, 5, 1)
uop_4275 = relay.asinh(call_4269.astype('float64')) # shape=(2, 5, 1)
func_3977_call = mod.get_global_var('func_3977')
func_3980_call = mutated_mod.get_global_var('func_3980')
var_4280 = relay.var("var_4280", dtype = "int32", shape = (273, 1))#candidate|4280|(273, 1)|var|int32
call_4279 = relay.TupleGetItem(func_3977_call(relay.reshape(var_4280.astype('int32'), [7, 13, 3]), relay.reshape(var_4280.astype('int32'), [7, 13, 3]), ), 0)
call_4281 = relay.TupleGetItem(func_3980_call(relay.reshape(var_4280.astype('int32'), [7, 13, 3]), relay.reshape(var_4280.astype('int32'), [7, 13, 3]), ), 0)
output = relay.Tuple([uop_4273,call_4279,var_4280,])
output2 = relay.Tuple([uop_4275,call_4281,var_4280,])
func_4291 = relay.Function([var_4280,], output)
mod['func_4291'] = func_4291
mod = relay.transform.InferType()(mod)
mutated_mod['func_4291'] = func_4291
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4292 = relay.var("var_4292", dtype = "int32", shape = (273, 1))#candidate|4292|(273, 1)|var|int32
func_4291_call = mutated_mod.get_global_var('func_4291')
call_4293 = func_4291_call(var_4292)
output = call_4293
func_4294 = relay.Function([var_4292], output)
mutated_mod['func_4294'] = func_4294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_4303 = func_4250_call()
call_4304 = func_4250_call()
output = relay.Tuple([call_4303,])
output2 = relay.Tuple([call_4304,])
func_4317 = relay.Function([], output)
mod['func_4317'] = func_4317
mod = relay.transform.InferType()(mod)
output = func_4317()
func_4318 = relay.Function([], output)
mutated_mod['func_4318'] = func_4318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_4319 = relay.TupleGetItem(func_4317_call(), 0)
call_4320 = relay.TupleGetItem(func_4318_call(), 0)
func_3505_call = mod.get_global_var('func_3505')
func_3510_call = mutated_mod.get_global_var('func_3510')
const_4322 = relay.const(-5.603960, dtype = "float64")#candidate|4322|()|const|float64
const_4323 = relay.const([7.984030,9.604420,0.638046,-7.672231,7.413842,-6.445439,8.870367,-1.564015,6.848141,6.662009,-0.444886,3.040797,-8.065048,-8.104683,3.869522,2.486417,-7.848921,9.804947,-3.084158,9.179368,-1.993855,-9.315095,-3.077505,-7.034340,-3.228168,4.622902,-5.781099,-1.192449,-6.591135,-3.526263,-2.464542,3.111146,-2.970833,5.304811,-9.991581,-0.232115,-8.799153,-3.633481,1.366906,9.482667,-7.944939,2.221652,9.900340,8.639417,-7.771376,4.067275,-5.664284,2.458129,0.195628,8.472613,-2.968368,9.003783,-3.573868,6.533255,-8.492677,6.307200,-6.044849,-2.253400,1.806335,2.386686,5.246428,-4.923632,5.419131], dtype = "float64")#candidate|4323|(63,)|const|float64
const_4324 = relay.const([[-2.973219],[-8.645424],[9.012427],[8.294792],[-1.499938],[5.791014],[6.245559],[-2.895654],[7.826470],[-8.362885],[6.989035],[-9.746411],[-8.316415],[2.381248],[2.884478],[5.232001],[9.487860],[-1.883350],[-8.901263],[3.704405],[7.353596],[0.980128],[-6.021715],[0.406338],[5.218011],[-6.482541],[-9.939804],[-9.951234],[-2.138010],[-6.857111],[3.543244],[-2.147380],[8.798788],[-5.143001],[-1.766984],[-9.896101],[-7.676880],[-3.821008],[4.118865],[-6.188128],[5.744268],[2.763742],[-7.368435],[-2.439629],[-5.565639],[-2.002446],[1.314767],[-5.453277],[4.409498],[-4.744357],[-4.893292],[8.675341],[-1.408182],[9.574228],[0.889663],[-1.079481],[1.401052],[6.807639],[3.976800],[-7.335458],[-1.955149],[-9.429357],[2.012394],[-0.351218],[4.506139],[-1.377982],[2.931635],[-3.170336],[3.653890],[7.829260],[0.652313],[9.844797],[-5.272943],[-9.838655],[2.290645],[4.145955],[2.887729],[7.868460],[-0.677420],[-9.798198],[-5.118151],[-8.051542],[-7.269672],[7.588347],[-1.557188],[3.792435],[-4.241826],[-9.336713],[1.349610],[5.858150],[-3.021617],[-2.934730],[-7.039515],[-4.752551],[2.027709],[-5.219313],[-2.057711],[3.448299],[0.057338],[-1.471930],[5.992889],[6.800974],[0.736726],[-9.912813],[0.907881],[1.780695],[-1.685350],[5.676109],[3.503353],[-9.625803],[-3.158103],[-7.890371],[4.443185],[-2.510026],[-2.024520],[-8.394918],[-5.603245],[8.123824],[-1.090058],[-9.546598],[2.179997],[6.860529],[8.535440],[-4.716114],[-9.382932],[1.175389],[4.087264],[5.246532],[5.985147],[1.850445],[1.124813],[3.525550],[-0.441407],[7.073048],[3.020827],[-4.804784],[4.566607],[-0.844297],[-1.632133],[7.165807],[0.626461],[-8.159481],[-7.881331],[5.942386],[4.005791],[5.829474],[0.260116],[-4.880161],[0.937475],[-7.356603],[9.934114],[-7.372564],[-6.318136],[5.139916],[8.787021],[5.352830],[7.816722],[-6.300283],[-6.065354],[2.315971],[-8.238328],[-7.623820],[1.565204],[7.382044],[-6.705379],[3.582937],[-8.256020],[-9.717348],[8.716368],[-5.260580],[-6.099992],[2.285638],[1.940236],[2.138792],[-1.621356],[4.192215],[5.816999],[-5.983456],[-5.207471],[4.094436],[2.263029],[-8.649881],[-2.810020],[-7.093906],[-8.544769],[9.004210],[-9.462477],[-9.472731],[-9.928319],[8.212181],[-4.714670],[2.495919],[-8.084955],[-4.810602],[-9.949930],[2.231948],[9.355102],[1.869327],[-6.894069],[7.250639],[-2.288084],[5.087560],[0.247572],[-8.619411],[9.366683],[-3.162265],[-3.292131],[2.182892],[6.916676],[5.068301],[-2.662708],[0.794280],[-6.809448],[8.330746],[-7.787692],[1.365183],[5.170005],[-8.035670],[-2.285104],[-7.564209],[-8.729651],[7.435831],[0.806751],[-1.502703],[6.083793],[-1.395275],[-3.039002],[5.048292],[-8.571344],[-6.033570],[5.921468],[-4.424567],[-8.236213],[9.824045],[1.258466],[2.599184],[1.991729],[8.754566],[3.791019],[1.700146],[6.569300],[-8.486727],[-4.926442],[2.413796],[4.115516],[3.507115],[0.158901],[1.320024],[-5.065808],[6.707607],[5.992568],[-6.311139],[8.451662],[7.741103],[9.008127],[5.052602],[-5.564239],[-1.279249],[5.493837],[0.760287],[1.335829],[2.053533],[-0.065902],[7.637417],[-6.199476],[3.754939],[0.275411],[-1.639736],[9.730597],[3.746005],[-9.776431],[7.962761],[7.722692],[4.265057],[5.415248]], dtype = "float64")#candidate|4324|(275, 1)|const|float64
call_4321 = relay.TupleGetItem(func_3505_call(relay.reshape(const_4322.astype('float64'), []), relay.reshape(const_4323.astype('float64'), [9, 7, 1]), relay.reshape(const_4324.astype('float64'), [275,]), ), 0)
call_4325 = relay.TupleGetItem(func_3510_call(relay.reshape(const_4322.astype('float64'), []), relay.reshape(const_4323.astype('float64'), [9, 7, 1]), relay.reshape(const_4324.astype('float64'), [275,]), ), 0)
output = relay.Tuple([call_4319,call_4321,const_4322,const_4323,const_4324,])
output2 = relay.Tuple([call_4320,call_4325,const_4322,const_4323,const_4324,])
func_4331 = relay.Function([], output)
mod['func_4331'] = func_4331
mod = relay.transform.InferType()(mod)
mutated_mod['func_4331'] = func_4331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mutated_mod.get_global_var('func_4331')
call_4332 = func_4331_call()
output = call_4332
func_4333 = relay.Function([], output)
mutated_mod['func_4333'] = func_4333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4340 = relay.TupleGetItem(func_4331_call(), 4)
call_4341 = relay.TupleGetItem(func_4333_call(), 4)
uop_4347 = relay.sqrt(call_4340.astype('float32')) # shape=(275, 1)
uop_4349 = relay.sqrt(call_4341.astype('float32')) # shape=(275, 1)
uop_4351 = relay.sin(call_4340.astype('float32')) # shape=(275, 1)
uop_4353 = relay.sin(call_4341.astype('float32')) # shape=(275, 1)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4355 = relay.TupleGetItem(func_4331_call(), 0)
call_4356 = relay.TupleGetItem(func_4333_call(), 0)
output = relay.Tuple([uop_4347,uop_4351,call_4355,])
output2 = relay.Tuple([uop_4349,uop_4353,call_4356,])
func_4364 = relay.Function([], output)
mod['func_4364'] = func_4364
mod = relay.transform.InferType()(mod)
mutated_mod['func_4364'] = func_4364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mutated_mod.get_global_var('func_4364')
call_4365 = func_4364_call()
output = call_4365
func_4366 = relay.Function([], output)
mutated_mod['func_4366'] = func_4366
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4367 = relay.var("var_4367", dtype = "float32", shape = (8, 4, 2))#candidate|4367|(8, 4, 2)|var|float32
var_4368 = relay.var("var_4368", dtype = "float32", shape = (8, 4, 2))#candidate|4368|(8, 4, 2)|var|float32
bop_4369 = relay.divide(var_4367.astype('float32'), relay.reshape(var_4368.astype('float32'), relay.shape_of(var_4367))) # shape=(8, 4, 2)
func_3222_call = mod.get_global_var('func_3222')
func_3225_call = mutated_mod.get_global_var('func_3225')
const_4373 = relay.const([[0.336592],[9.718680],[6.100342],[4.134298],[-4.601690],[-6.408921],[7.644363],[-8.854266],[8.003122],[0.761497],[4.494777],[5.221985],[7.252520],[-0.831691],[2.844787],[1.877582],[7.077542],[-4.464063],[-9.556202],[7.558837],[-4.648405],[-0.090651],[-7.376029],[-2.475800],[-3.925359],[8.828941],[-9.379692],[0.621702],[4.847615],[-3.474893],[0.256789],[-6.775130],[-0.128722],[1.914000],[-7.135976],[-9.528109],[-3.781919],[-7.265048],[0.700162],[-8.432051],[-7.854895],[4.571125],[8.326908],[-2.107332],[8.108773],[4.499301],[6.671354],[5.718636],[-9.787843],[-3.000558],[2.010339],[3.944902],[6.127569],[5.304312],[2.325311],[7.569289],[2.244598],[-6.638085],[2.132485],[-7.684482],[5.728465],[-9.193845],[4.254577],[9.054287],[-8.755021],[-0.347566],[-5.678984],[-3.934964],[8.694987],[-2.963560],[3.644263],[-7.387327],[2.469490],[4.460342],[-2.620414],[0.587271],[7.260857],[-2.725597],[6.313699],[2.900511],[2.074272],[-1.543724],[1.968076],[-6.389801],[-6.804200],[6.314075],[-2.938221],[-2.681652],[8.880048],[-6.808696],[2.878329],[7.194579],[9.130569],[2.523817],[4.063605],[7.400197],[-7.088449],[-2.285984],[-2.129956],[-6.076598],[-2.826929],[-8.806891],[-1.859471],[-0.624429],[6.568517],[5.180229],[-7.525822],[6.241668],[-9.396246],[-7.806121],[4.710713],[-4.030643],[5.526004],[-5.442093],[5.317526],[-8.186628],[-1.950083],[-2.509884],[-1.521083],[-4.049632],[-9.033839],[-3.845013],[9.065503],[-2.156228],[9.387063],[0.995474],[-4.771786],[-3.727137],[3.539078],[4.219660],[-5.052575],[-7.114147],[0.752202],[7.927412],[0.133415],[5.899032],[0.400015],[-5.913649],[3.265824],[-2.770002],[0.710577],[-9.179640],[8.880141],[-5.608236],[0.345527],[-2.794948],[9.639509],[-2.329070],[2.606531],[-1.452329],[-4.249852],[-7.690436],[-6.583432],[-5.393530],[-4.134820],[-2.540810],[-1.161473],[6.658747],[0.302588],[-5.028377],[-9.416395],[-1.037583],[7.661149],[-1.140132],[-0.898246],[6.042952],[-5.101060],[-2.637776],[-6.602541],[-6.542672],[8.536854],[2.877076],[3.727596],[-0.093491],[-3.601453],[1.398208],[2.876816],[-3.357580],[1.116798],[2.233006],[-9.535083],[-9.690867],[9.825394],[5.705034],[6.409336],[-8.837449],[-3.885102],[-0.385269],[-5.480304],[-6.931273],[-7.687315],[3.402225],[-6.452596],[-1.858305],[-3.247916],[1.585654],[4.947224],[5.626102],[3.546817],[-5.849396],[7.824483],[9.638586],[-3.098988],[5.248360],[-6.106634],[1.145230],[-3.444348],[-2.655227],[4.670591],[-0.473636],[1.063944],[-5.630399],[9.314591],[5.060494],[-8.271070],[6.996670],[-0.306888],[9.252900],[-3.805452],[7.747659],[-6.882119],[5.657875],[-9.084925],[2.050131],[1.549762],[7.528821],[-6.785967],[4.759681],[-0.928863],[-9.259471],[-3.116933],[-7.795582],[-5.261703],[-0.680988],[-8.578377],[-4.956582],[-1.277722],[8.387562],[0.830167],[-9.169194],[-9.995015],[5.851213],[4.806504],[-5.197186],[2.341192],[-7.407091],[-9.740581],[-3.098334],[-8.949850],[-7.824679],[3.357108],[-9.933367],[-9.392938],[-9.473281],[-7.306029],[-1.804710],[-1.666345],[5.872931],[-5.134574],[9.980385],[-1.660448],[-6.038255],[-9.828372],[-2.589749],[9.279417],[-9.755603],[3.556187],[-3.728354],[-1.334665],[0.196552],[-4.900706],[-7.506319],[-1.082842],[-6.495293],[6.633304],[-8.128276],[-7.381221],[2.278986],[-4.410948],[1.926280],[-9.453914],[-8.098666],[-7.173579],[1.067184],[6.311171],[-5.504625],[2.484793],[-1.408413],[-4.251629],[-0.165293],[8.064663],[-6.565169],[5.144471],[-7.981491],[2.032538],[9.636132],[0.012398],[4.254872],[6.408836],[7.722232],[6.810308],[-5.758431],[-2.822472],[-7.600432],[9.386983],[-4.348419],[-4.690305],[-0.245276],[-8.723577],[8.729229],[9.741626],[0.825870],[-2.876768],[-0.533829],[-0.916672],[-2.981967],[8.816539],[-1.677467],[2.638734],[2.997685],[2.298599],[2.154938],[-6.069595],[-0.592732],[8.733418],[-0.431213],[-4.469248],[6.786177],[-3.749845],[-2.416130],[7.978340],[-9.998426],[6.970662],[-1.363867],[-4.914439],[-7.524789],[-5.005907],[2.765593],[2.460925],[8.431606],[4.256852],[8.463552],[-5.372789],[-3.110194],[8.117408],[1.835971],[8.999701],[4.764500],[-3.694690],[5.041151],[8.207570],[-5.266609],[-4.077944],[-7.568142],[3.969284],[-5.221900],[1.008909],[7.694468],[-8.841597],[-8.268559],[-0.871055],[7.126846],[-8.097076],[3.199631],[-1.166060],[8.498644],[-9.872956],[6.740579],[9.243882],[-0.216266],[-8.099467],[6.673268],[5.542476],[5.776425],[-1.817172],[4.311356],[5.703965],[-0.634004],[5.796237],[-7.268056],[-1.809768],[-2.712300],[5.802871],[1.391413],[5.182478],[-7.028489],[-9.667560],[-3.991272],[-0.870246],[-8.765373],[1.584472],[8.679068],[-4.724156],[-8.194784],[3.056074],[2.108193],[-4.070496],[-1.960684],[-6.115013],[-3.765525],[-7.419511],[4.451501],[-4.562741],[-7.220904],[6.074973],[5.350350],[-4.090725],[7.828966],[-1.675055],[-0.301241],[-9.048577],[-0.822430],[2.674374],[-8.428012],[-9.660215],[-4.828522],[9.555158],[-0.771066],[9.209191],[-2.715774],[0.746921],[3.889118],[3.747157],[-2.204711],[7.451138],[7.324004],[-1.692639],[-6.877445],[0.948499],[4.438119],[-2.548824],[-4.745132],[2.760171],[6.427323],[3.991435],[0.457054],[-9.931720],[-9.798325],[2.743939],[2.320535],[8.739469],[-4.829261],[-2.940670],[-2.863881],[-9.874536],[-7.662843],[0.506842],[-3.400324],[9.922810],[1.658063],[-1.579486],[8.318156],[6.747653],[-3.922339],[-7.551488],[1.396311],[-3.116077],[3.141949],[0.242579],[-3.557208],[-8.360953],[-9.894393],[6.453453],[-2.995414],[-7.121876],[1.421070],[0.579844],[2.395311],[-1.290135],[1.733092],[-2.300270],[5.884490],[2.929114],[2.383212],[-6.717901],[-4.347366],[-5.279102],[-2.796087],[4.374437],[-0.893173],[-9.025748],[-4.313067],[-2.999319],[-7.816367],[5.236425],[8.696296],[6.888088],[2.062072],[-7.009598],[7.102836],[-5.040788],[6.251795],[-0.262685],[8.738892],[-6.100376],[1.715888],[8.298794],[-4.246710],[-3.652688],[5.334192],[8.878456],[3.385591],[1.600803],[2.430812],[2.141405],[-0.182107],[-0.546417],[2.019460],[4.071042],[-1.818142],[-7.134005],[-4.387425],[-4.108580],[-7.112240],[2.897545],[-8.060528],[-9.137397],[6.311859],[-0.234054],[1.806411],[7.220895],[-2.066275],[0.507129],[-0.433394],[-7.303175],[0.722077],[3.510904],[-9.963116],[-1.464716],[-6.904016],[-0.048063],[-7.649249],[-1.945256],[-5.791620],[-8.021425],[-2.622323],[6.310713],[2.126390],[-9.118433],[1.983775],[2.626342],[-4.936535],[-4.549025],[-9.512002],[2.899422],[1.401534]], dtype = "float32")#candidate|4373|(546, 1)|const|float32
call_4372 = relay.TupleGetItem(func_3222_call(relay.reshape(const_4373.astype('float32'), [6, 7, 13])), 0)
call_4374 = relay.TupleGetItem(func_3225_call(relay.reshape(const_4373.astype('float32'), [6, 7, 13])), 0)
func_1965_call = mod.get_global_var('func_1965')
func_1969_call = mutated_mod.get_global_var('func_1969')
const_4380 = relay.const([-8,10,1,8,-2,7,9,-9,8,7,9,-6,2,-7,3,10,-2,-7,-6,5,5,8,-10,6,-4,7,-4,-8,-10,5,10,3,6,5,2,-1,-3,-4,7,2,2,3,-2,-2,8,6,-5,-10,-6,4,-4,-8,4,-2,9,-2,-5,8,-8,10,10,-3,-4,5,-7,-9,-3,-10,6,-10,7,-7,-9,-10,5,-2,-7,-1,10,-10,-4,10,5,-6,1,5,8,-2,8,3,-3,10,9,-10,5,8,8,-7,-7,3,9,-7,3,5,1,-3,-2,-4,-4,2,6,-1,7,7,-2,-3,2,9,9,-5,1,-7,-2,-8,7,8,-9,8,-10,9,7,3,3,-5,6,-5,9,-4,4,9,-1,3,-7,-5,7,-7,7,4,-3,-4,-8,-8,10,-7,-1,6,-3,-1,9,7,9,10,5,-7,4,7,-10,-8,6,-5,-2,-8,-9,7,-2,-5,10,8,3,6,-7,-9,8,7,7,-1,-2,-5,-8,2,5,-3,-5,2,8,-5,-1,-10,-4,-4,-9,-9,4,4,6,-1,5,8,7,-6,-8,-10,7,-1,-6,-1,10,8,6,7,9,-3,-6,-2,10,7,-1,8,-4,-9,4,7,-2,1,6,9,7,-8,4,-5,-10,-4,-9,8,-1,-6,-9,-10,-6,10,-10,7,-5,-10,5,-3,10,-7,-10,-10,6,-8,9,-7,-1,-6,9,8,-8,-3,6,1,1,-4,-7,-2,2,-7,1,5,2,-3,-5,-7,3,-10,-3,-6,-1,5,-5,-8,-10,6,-10,3,2,-4,-9,4,10,1,-4,-8,-7,2,4,7,-6,5,-5,1,6,-8,8,-9,5,10,6,6,-2,3,10,-2,-6,6,7,3,-3,-10,-3,7,-8,-9,6,-8,-4,6,5,-2,-7,4,-4,-9,6,-7,-8,-6,3,3,-1,-10,3,10,-8,-1,-1,-8,2,3,9,-8,6,5,9,1,-8,6,-8,1,9,10,-7,-8,-8,-6,2,-3,-7,-10,-6,-8,-3,-6,-1,9,-7,3,-7,-2,1,-3,-9,3,-5,-2,-5,5,-5,1,8,-7,8,10,8,-2,7,1,-2,-1,9,-7,-6,-2,-3,-6,-2,-7,-2,6,8,-8,-3,-10,5,-1,-9,-9,-3,3,-6,9,1,-8,3,-2,4,-6,10,2,-1,10,-3,4,-9,-4,-7,3,-10,-2,5,-6,5,5,-9,-9,-10,-2,-7,9,-5,-1,5,-2,-2,-8,10,5,-5,9,5,-6,-8,-10,-7,10,-1,6,-2,-10,5,-3,-3,10,-7,4,10,1,-8,-2,-9,7,-3,7,-1,2,-7,3,-1,10,4,4,-3,10,3,8,-6,1,10,-7,-6,-9,5,-5,-4,6,6,-10,4,-2,-3,10,-5,-1,10,-6,-10,-9,6,1,6,8,9,3,-9,2,-5,-5,7,7,-5,-4,-1,-8,-7,-9,-8,7,6,-1,-6,8,9,-4,-9,-2,8,-1,-8,-6,-10,10,-1,-5,8,3,-3,7,-6,8,4,2,-7,10,2,10,10,-9,-6,1,2,-10,-7,-5,-8,8,3,3,-3,-5,1,-6,-7,4,-1,9,-9,6,-4,8,-4,-3,8,-8,10,-7,-3,2,10,-5,-10,-4,-3,-6,-1,-10,-3,-5,8,-4,-1,9,-6,3,-6,-8,-3,7,3,5,-8,-3,6,3,-5,4,2,7,-6,-5,-7,1,7,5,1,-8,-5,-1,-10,8,-5,-9,-8,4,-7,10,-6,-5,1,5,-2,-3,1,-9,-2,6,9,-4,-2,-5,-1,-6,-6,-10,-2,10,-5,2,-9,-8,-10,-8,-10,8,-3,4,7,-1,-10,9,3,6,2,-5,-1,-10,7,-1,-10,-10,3,-7,1,-3,-8,-3,-2,8,-8,-5,-5,-3,-4,-7,3,-9,1,-5,5,-5,10,3,-8,-6,-3,-9,-7,-9,5,7,-7,-4,-4,3,7,-10,4,1,-4,10,9,6,-10,-8,4,2,-4,10,-5,7,10,1,1,-8,10,-2,5,-6,6,-7,1,-4,8,-5,6,7,9,10,1,-5,-5,-1,-7,-3,-10,5,-4,10,-2,4,-7,6,10,-6,-5,3,7,8,8,-9,4,4,3,-7,-9,5,-4,3,-8,-5,7,-10,-2,10,-10,2,3,1,10,-2,-10,8,-9,-6,-10,-7,10,3,4,4,2,-7,2,2,-7,-4,3,-9,-2,9,-9,-9,4,1,-5,3,10,6,-9,5,-5,2,-10,-2,7,4,-8,5,5,1,10,1,3,4,-6,-7,-10,10,-10,-4,-6,3,3,7,3,-10,-9,4,8,3,9,-4,-6,10,-9,-3,5,10,-3,6,6,-10,8,-6,-2,-8,-8,9,-9,2,-3,6,10,-8,4,10,1,-4,3,-5,10,3,8,-5,-3,8,1,-6,1,-5,-7,4,4,8,9,-2,7,-10,-9,5,-2,-8,6,-6,-7,1,-10,3,-4,-3,2,-1,-1,7,5,-4,4,2,5,8,-10,5,5,-4,-6,-1,2,-1,-4,5,-10,-8,10,-6,-5,6,-5,-7,-8,1,-10,6,6,-5,6,2,8,10,-10,-2,3,2,10,8,2,5,4,4,-9,-2,10,2,-6,7,-1,10,-8,1,4,7,1,-8,3,4,-2,6,-4,3,1,3,8,5,8,3,9,5,-1,-4,-6,4,-7,-1,1,1,3,-5,9,-6,-7,-8,10,6,-8,-4,1,4,10,-10,-1,-4,-7,5,10,3,-4,-6,4,-6,4,-9,-9,4,-10,2,-5,8,-5,8,-8,-5,-1,7,-4,-10,-2,-5,3,10,-4,-7,-9,3,-9,1,3,10,-8,-1,-7,-3,9,-7,7,-8,-10,-4,-3,2,9,9,-1,7,-5,4,-9,-10,6,5,-7,-6,9,3,-8,-3,-10,10,1,-3,-6,-8,-5,-7,8,-6,-4,-1,2,-4,10,-7,10,-2,-5,-9,1,7,-8,8,-4,-2,-7,-1,8,9,-5,-10,6,-7,-6,-1,6,6,-4,-9,-9,7,3,-6,5,10,-4,6,2,-10,-2,7,2,-9,8,-3,8,-6,1,-1,-9,-6,-1,4,8,4,-6,-7,6,3,5,-2,9,5,10,-6,-6,4,7,-1,-2,6,-7,8,-2,-7,10,-1,7,-9,-3,-6,9,8,-7,-4,5,-9,-4,6,-10,4,-2,9,2,-6,2,6,3,-9,5,9,3,2,7,-5,1,-4,-6,-2,-10,-5,-2,4,-5,6,-4,1,3,5,1,6,9,5,-3,-6,-7,3,-10,-5,-8,4,-3,9,8,7,-6,-5,3,2,9,8,7,-5,8,1,-8,10,-9,1,-7,-1,1,7,6,-1,5,10,9,-8,-5,5,-5,-9,5,4,-8,4,10,5,-1,10,-6,-10,8,-3,9,8,-4,8,7,-3,8,-6,7,6,-10,5,-1,-2,-3,1,5,-3,4,-10,7,6,9,6,5,-5,2,-2,5,1,-9,9,2,10,-7,-9,-2,-2,6,8,-1,8,-4,-8,2,-8,-4,2,-3,1,5,-6,4,-9,-5,-4,1,-2,2,-6,3,-5,5,10,2,-9,3,3,1,-10,10,-5,-5,7,-8,2,-9,8,-4,3,2,-2,-7,-4,8,7,7,-10,8,10,10,-7,8,-4,-6,8,-1,4,-7,6,-2,3,4,2,1,-8,-5,-4,2,5,7,5,8,-5,8,10,6,-1,-9,2,6,-4,9,-4,-8,-9,6,4,-3,-9,-10,-3,4,-9,-7,-6,-3,4,10,10,-8,-2,5,8,-5,-1,6,5,7,5,-5,9,-1,7,-2,9,8,-4,-9,10,-7,-1,4,3,10,-7,8,10,-8,3,7,-10,5,-9,8,8,-10,-10,-7,-8,-2,-1,-1,-2,-1,1,-8,3,6,-8,1,2,9,8,5,-4,-10,-9,-7,2,-9,5,3,-1,-2,-5,-6,-6,9,10,1,2,8,-4,4,4,10,-1,9,-2,-10,4,4,-9,-6,-6,5,-10,-1,10,2,-9,3,-5,-9,-1,-4,4,-7,-10,2,-9,5,-9,-4,2,-3,8,10,-8,10,9,-6,-3,-6,5,-10,6,-4,2,4,-3,6,4,-5,-6,-2,9,5,-3,7,-8,2,4,9,-3,-1,-1,-10,-2,5,-9,2,7,10,-10,-9,3], dtype = "int16")#candidate|4380|(1568,)|const|int16
call_4379 = func_1965_call(relay.reshape(const_4380.astype('int16'), [14, 14, 8]), relay.reshape(const_4380.astype('int16'), [14, 14, 8]), )
call_4381 = func_1965_call(relay.reshape(const_4380.astype('int16'), [14, 14, 8]), relay.reshape(const_4380.astype('int16'), [14, 14, 8]), )
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_4408 = relay.TupleGetItem(func_4317_call(), 0)
call_4409 = relay.TupleGetItem(func_4318_call(), 0)
uop_4416 = relay.acosh(call_4408.astype('float32')) # shape=(2, 5, 1)
uop_4418 = relay.acosh(call_4409.astype('float32')) # shape=(2, 5, 1)
bop_4435 = relay.logical_and(uop_4416.astype('bool'), relay.reshape(call_4408.astype('bool'), relay.shape_of(uop_4416))) # shape=(2, 5, 1)
bop_4438 = relay.logical_and(uop_4418.astype('bool'), relay.reshape(call_4409.astype('bool'), relay.shape_of(uop_4418))) # shape=(2, 5, 1)
output = relay.Tuple([bop_4369,call_4372,const_4373,call_4379,const_4380,bop_4435,])
output2 = relay.Tuple([bop_4369,call_4374,const_4373,call_4381,const_4380,bop_4438,])
func_4442 = relay.Function([var_4367,var_4368,], output)
mod['func_4442'] = func_4442
mod = relay.transform.InferType()(mod)
var_4443 = relay.var("var_4443", dtype = "float32", shape = (8, 4, 2))#candidate|4443|(8, 4, 2)|var|float32
var_4444 = relay.var("var_4444", dtype = "float32", shape = (8, 4, 2))#candidate|4444|(8, 4, 2)|var|float32
output = func_4442(var_4443,var_4444,)
func_4445 = relay.Function([var_4443,var_4444,], output)
mutated_mod['func_4445'] = func_4445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4538 = relay.TupleGetItem(func_4331_call(), 2)
call_4539 = relay.TupleGetItem(func_4333_call(), 2)
output = relay.Tuple([call_4538,])
output2 = relay.Tuple([call_4539,])
func_4542 = relay.Function([], output)
mod['func_4542'] = func_4542
mod = relay.transform.InferType()(mod)
mutated_mod['func_4542'] = func_4542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mutated_mod.get_global_var('func_4542')
call_4543 = func_4542_call()
output = call_4543
func_4544 = relay.Function([], output)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4562 = relay.const([[[-7,9,4,-6,-10,8,5,-6,2,-9,-2,-10,7],[7,2,-1,-4,4,8,8,-3,9,-2,-6,-8,1],[-4,-8,-5,-2,1,-6,8,5,-2,-2,-7,10,-6],[4,-3,-8,8,-10,1,9,-7,-4,-7,-9,-10,-1],[-3,-8,9,-5,-9,-3,-8,-9,7,8,-5,1,3],[-10,-10,-4,3,-4,-6,-9,3,-9,7,10,5,7],[4,1,-7,-2,3,-2,8,3,4,-8,-5,9,-6],[-5,-9,-3,2,2,-7,8,2,8,-7,-3,-2,9],[-9,-9,-7,8,-7,-1,-6,-8,-9,5,-8,3,-4],[8,9,-3,-8,-5,-7,1,5,10,-6,6,-7,-9],[6,2,-10,7,-10,10,-3,2,-10,-3,-6,-6,-3],[2,-5,-5,-4,-10,9,-4,8,-6,-6,2,-1,1]],[[-9,-4,1,-2,-6,9,6,-4,7,-4,9,5,-8],[3,3,9,-3,4,-8,2,3,-5,1,4,9,-10],[-7,6,-5,7,5,7,10,3,8,-3,7,10,9],[-5,-3,7,-1,7,3,3,1,-5,-1,-8,-4,-10],[1,10,-5,8,-9,7,-9,-7,10,2,9,-2,-8],[1,-3,6,2,-4,10,-4,9,10,-8,2,-6,-3],[6,7,-8,-7,-1,5,-8,8,-10,-6,6,7,-2],[5,-5,-4,4,4,-2,-4,-3,-4,-7,8,7,-6],[-9,-8,-4,-8,-1,-10,6,8,-5,8,-1,-1,-9],[6,5,8,5,-7,-8,5,-7,-4,-9,10,-5,3],[3,2,7,7,-8,-7,2,1,9,1,1,1,-8],[-5,1,6,-4,-7,6,4,-10,8,-3,4,-3,9]],[[8,5,1,8,-7,-6,-3,-1,-7,-5,-6,-9,-10],[-2,-5,8,-1,1,2,-1,-4,-10,-10,-7,8,5],[3,-4,6,5,-4,-9,7,-6,9,-9,-6,1,-2],[4,8,-5,-1,3,2,1,2,-3,-9,-9,-6,-5],[-7,-8,-5,-2,-2,-6,-3,-2,-9,-5,2,2,-6],[-2,-1,-7,-3,9,9,-5,-8,4,3,6,-9,-5],[-8,-2,9,-1,3,1,6,6,-1,6,3,1,-6],[-8,-10,5,1,6,-3,2,-6,-2,3,8,10,-5],[6,8,3,-8,-8,-2,-10,1,-7,9,-6,-6,10],[4,9,-10,-3,8,6,-2,-9,-5,3,4,1,-5],[-6,-7,-6,6,-10,4,-7,-3,8,-7,-8,-8,10],[-4,7,1,10,-10,1,-6,2,-4,2,-2,-3,-7]],[[-3,3,-7,6,6,-5,-5,5,-3,-7,-8,-6,10],[-1,8,3,3,7,-5,-1,-2,7,5,3,10,-3],[-3,-9,8,4,-7,1,5,7,-3,-8,9,2,7],[10,-7,8,-3,-3,-6,-10,5,3,9,9,2,-9],[-5,3,-8,9,-7,5,3,-4,6,4,-5,-1,-8],[-8,-8,-1,8,4,8,-3,-10,6,8,-4,4,-6],[-6,-3,7,-7,8,7,4,4,-5,-7,-7,10,-5],[-2,4,-9,-6,7,4,10,5,-10,1,9,4,2],[-2,-9,-7,-9,-8,3,1,-7,7,-8,5,9,5],[1,-7,1,3,8,10,3,6,-1,-6,-3,-4,-5],[-1,4,-4,5,5,-1,-5,-2,-8,2,1,-10,-2],[1,-4,-4,1,-2,2,-4,-5,-9,6,7,8,-10]]], dtype = "uint64")#candidate|4562|(4, 12, 13)|const|uint64
const_4563 = relay.const([[[9,4,-10,6,3,7,-4,-4,8,9,-2,-10,8],[-1,6,-10,7,-8,4,-4,-7,10,4,6,-6,5],[7,2,-1,-4,-2,3,2,-8,-7,-5,3,-8,1],[-6,3,4,7,7,9,-6,-10,2,-2,8,3,6],[1,3,-1,9,-10,-4,-1,6,2,4,-5,-4,9],[8,5,7,1,-8,-1,-6,1,8,1,-3,10,-7],[-4,-1,2,6,-3,-3,-5,7,-7,-6,3,10,2],[6,-1,-4,-3,9,-4,1,9,2,-7,9,1,2],[-1,-7,6,-2,8,3,3,-5,6,-6,3,9,8],[4,5,-5,-2,9,6,6,-9,5,10,1,-7,-3],[5,-10,1,-4,4,3,10,4,5,-1,-9,-10,-4],[5,8,-4,1,7,10,10,-9,-7,-7,6,-1,8]],[[-1,8,-9,-1,-4,-1,-6,7,-10,-9,-2,-9,-9],[10,-1,-3,9,2,-6,-7,5,-5,6,1,1,-6],[-8,1,-1,-1,-1,9,-6,8,-3,2,2,-2,-1],[6,-1,-2,-1,-8,4,-9,4,5,-8,-1,7,-10],[3,7,5,4,8,-6,-9,-3,4,9,9,-7,6],[-9,-1,2,-3,8,2,3,-7,1,3,-2,4,-6],[-5,2,-1,6,2,-6,5,-2,-5,9,3,-2,3],[-3,5,-2,2,-4,6,5,-8,-2,4,-1,8,2],[9,-8,-8,-1,-2,-3,-6,-5,7,-10,-2,9,6],[-6,-10,-8,2,3,-6,-3,7,3,3,6,10,6],[-10,-8,4,3,-2,-3,6,2,-10,2,-1,1,-5],[-5,-4,-6,7,-3,6,5,6,2,-5,5,1,3]],[[2,-5,2,1,4,-2,-1,-2,-10,7,-4,-9,-3],[-4,-4,6,2,5,5,2,3,-10,9,-5,8,7],[1,3,-2,10,-4,2,-10,-2,10,6,-7,2,-10],[-7,7,2,-9,3,2,7,-10,3,-3,6,-8,9],[-9,-1,7,7,3,-3,-4,6,-8,1,-10,-9,-9],[6,-5,3,9,-3,4,-10,9,9,-10,9,-8,7],[7,10,-10,3,3,-1,2,9,-4,-2,4,8,10],[1,10,-5,3,2,2,-1,3,-9,6,2,-9,-6],[-10,7,2,6,-8,-8,6,6,-7,-5,7,-7,2],[-4,6,3,4,3,-10,5,-2,10,-3,6,-1,2],[4,4,9,-6,8,8,-1,-8,-2,8,-6,-1,-5],[10,-5,8,2,-5,10,3,-5,9,-3,-7,-10,10]],[[5,6,8,8,10,5,7,-2,-3,4,7,-4,-10],[7,7,-5,-9,-4,1,-2,-9,-5,-7,5,4,-8],[5,-5,-10,-5,10,-9,3,7,7,-4,-6,-3,8],[5,-9,4,2,7,2,10,1,4,-5,9,2,-8],[-4,3,1,3,8,2,-9,-5,2,-4,7,1,8],[-3,3,1,2,-9,-2,1,-4,-2,-3,-3,-4,-1],[4,2,10,-2,-7,-2,7,-2,-6,10,7,2,-1],[-6,-3,-6,9,-10,-3,3,7,1,-7,-4,-5,4],[8,-1,-2,-4,5,3,-7,-2,7,-2,-3,10,-5],[4,9,-1,5,-6,10,3,1,7,2,2,-7,4],[9,-1,-8,-4,2,-4,7,5,3,1,7,-5,1],[8,4,-9,8,7,4,3,-5,4,-10,-9,8,-8]]], dtype = "uint64")#candidate|4563|(4, 12, 13)|const|uint64
bop_4564 = relay.greater_equal(const_4562.astype('bool'), relay.reshape(const_4563.astype('bool'), relay.shape_of(const_4562))) # shape=(4, 12, 13)
output = relay.Tuple([bop_4564,])
output2 = relay.Tuple([bop_4564,])
func_4567 = relay.Function([], output)
mod['func_4567'] = func_4567
mod = relay.transform.InferType()(mod)
output = func_4567()
func_4568 = relay.Function([], output)
mutated_mod['func_4568'] = func_4568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4575 = relay.TupleGetItem(func_4331_call(), 1)
call_4576 = relay.TupleGetItem(func_4333_call(), 1)
func_2375_call = mod.get_global_var('func_2375')
func_2379_call = mutated_mod.get_global_var('func_2379')
const_4581 = relay.const([[7],[5],[7],[1],[4],[-2],[-1],[-5],[-7],[-4],[-6],[-2],[8],[7],[-3],[9],[-3],[2],[-2],[2],[7],[10],[2],[8],[-8],[4],[-3],[-4],[-8],[6],[-2],[-3],[-1],[6],[8],[-9],[4],[2],[7],[-5],[4],[-10],[-6],[7],[-5],[-5],[-2],[-3],[5],[-8],[9],[-9],[-9],[9],[1],[-2],[5],[-2],[-4],[5],[6],[10],[2],[2],[-5],[2],[2],[-7],[2],[-8],[1],[-8],[9],[9],[2],[5],[-6],[5],[8],[-5],[2],[9],[9],[-4],[1],[4],[9],[8],[5],[-1]], dtype = "int32")#candidate|4581|(90, 1)|const|int32
const_4582 = relay.const([-3,3,-7,9,-6,-1,2,10,-1,-7,2,-10,-4,-8,-1,5,8,-4,-10,8,4,2,9,4,-4,-6,9,-7,-10,1,7,-5,-5,1,4,5,9,7,-1,10,4,-2,-4,9,5,7,-8,-7,3,-10,7,8,3,6,6,9,-3,-6,-1,3,5,-8,-2,5,2,4,-1,7,-8,7,-8,4,9,-10,-5,6,3,-4,-8,-10,-6,-2,-7,-10,2,8,8,-3,4,-5,6,-10,5,4,6,-8,10,-9,10,1,1,-4,-3,-3,-4,-7,-2,-9,-4,-4,9,-1,3,6,-1,5,-8,10,10,10,4,4,8,-4,-10,-3,8,6,5,-5,8,-10,-3,-8,4,6,-9,1,-8,10,-1,5,-6,-3,10,1,9,4,10,4,-2,-1,3,-10,6,8,-2,9,3,-3,1,1,-3,-2,7,-8,-6,-1,10,-1,1,6,-2,3,8,-8,-10,-8,4,-8,8,1,7,-5,5,-3,-5,2,-3,-3,-3,-1,10,5,-1,-6,-1,3,2,4,3,-6,6,6,-4,-2,1,-1,-3,8,1,3,2,-3,3,2,7,-4,7,-4,-2,10,-10,-6,-7,-6,-8,-4,4,-5,-5,3,-6,-6,-1,-1,-9,-6,-2,-1,-7,-1,6,5,5,7,6,1,-8,-4,9,2,8,8,-10,-1,8,2,-9,5,5,-3,3,5,-5,10,4,-4,2,2,-9,-1,-7,2,-9,2,-9,9,1,3,2,-9,-7,-9,-3,3,6,-10,8,-2,6,-3,9,7,3,-5,3,-1,7,1,3,-3,-1,-3,-4,6,-9,7,8,-9,3,-7,-7,9,10,-5,8,-3,2,8,3,8,-4,1,8,-4,-1,9,1,4,-2,6,7,-8,9,7,-3,-5,9,-10,3,9,-7,6,8,1,10,-9,9,8,-7,-10,-9,7,1,6,-1,10,5,6,-7,-3,-6,-4,10,-3,-6,-7,-9,2,10,-4,4,9,-1,3,1,4,8,4,-1,-7,1,-9,-8,8,8,-1,7,2,-4,-7,2,-2,-1,-2,-3,-7,-3,-5,-7,9,7,10,9,-4,-10,7,4,4,-8,-8,-5,7,3,-9,7,8,7,9,-3,-8,-6,6,-6,7,-9,5,10,-2,-4,-3,-8,-6,-10,-2,10,7,4,-7,-8,-4,-9,-10,9,-10,-2,1,-6,4,3,-3,5,10,5,-10,4,-9,3,2,1,2,-6,3,1,10,-5,-7,-2,10,6,2,5,3,-1,9,-6,5,-5,4,8,-2,-6,3,-7,7,4,3,3,9,-10,5,-9,-8,1,-4,5,-1,-4,10,7,5,9,3,6,5,10,10,2,-6,1,1,-6,8,7,1,7,5,6,9,8,7,-4,7,-6,-9,3,-2,4,-8,10,-3,7,-7,6,6,10,3,-10,-1,5,3,4,6,-7,-7,4,-6,-9,-6,8,10,3,3,-6,-2,-8,7,-2,8,-7,-8,8,-4,6,-4,1,-4,7,-10,4,2,-6,-2,3,-10,6,5,-2,10,10,2,-8,-8,4,8,1,-9,-2,-7,-2,7,-5,-1,3,4,-7,-5,-5,-10,2,-8,-1,-1,-10,9,-7,10,-1,10,-6,7,3,6,6,10,5,2,6,10,4,-8,8,-5,-2,-4,9,2,5,3,-6,-1,2,-9,-9,-4,10,7,3,10,-7,4,6,-2,-3,-4,8,2,-9,8,-1,4,-6,3,3,3,-8,7,-4,-6,-6,8,6,-3,2,-4,4,6,6,-7,3,-10,10,4,8,1,-10,7,-8,10,2,2,-1,5,-8,-8,-6,-1,-8,10,-4,-8,-7,-10,-5,-4,-4,2,5,-5,-4,3,3,-6,-8,7,-7,-6,-9,-1,5,-1,10,-6,-5,-7,8,-8,-3,-4,-3,2,-5,4,5,10,1,-10,-7,7,9,-10,3,10,4,-8,2,-5,-10,-10,-8,-4,-2,-1,1,2,1,9,-9,3,-10,8,-3,-8,6,8,8,5,6,-10,4,-9,3,-1,6,6,7,7,-1,-4,4,-2,-4,4,-3,-9,6,3,7,-4,10,-8,-7,6,1,-6,-2,7,7,7,6,6,5,3,-3,-6,6,1,-10,-1,9,-4,-8,-8,-2,3,-3,10,-10,2,8,8,2,9,-8,-1,-8,7,-7,10,-10,-7,-4,10,10,7,8,5,-7,-9,5,-10,-8,10,2,5,3,-2,1,-10,4,10,-3,1,9,4,2,8,1,-5,10,-4,6,-9,-7,-9,-6,-2,-3,-10,-5,-8,-8,-8,6,3,-5,-8,-2,9,6,2,-6,1,-1,4,5,4,-10,-4,8,-2,-4,-6,-7,-10,5,-5,8,2,8,5,10,9,-4,4,-10,-6,7,3,-1,7,4,-6,-9,-2,-6,2,-8,4,4,5,4,-10,-7,7,7,3,7,6,8,4,-6,-8,5,-8,9,5,-7,6,-10,-2,-8,-6,4,2,-9,6,1,2,7,7,7,3,4,10,4,-9,-6,-7,9,2,6,-7,-3,4,-3,8,-10,-4,10,-10,-5,-7,8,-3,7,-6,5,-9,4,-10,4,-5,-9,-1,-2,-5,10,1,-10,-4,10,-10,-5,5,4,-6,-5,5,1,-7,4,3,-6,1,-9,-2,5,5,-3,-1,8,-7,10,7,7,6,5,-5,-4,-8,-1,1,4,-10,-6,6,-8,-7,7,10,7,5,-5,-5,-9,9,3,8,8,6,8,-8,-9,3,-8,-9,-8,8,-7,2,6,-7,-3,-6,-2,-5,-6,-7,7,-10,2,1,-6,-5,2,10,-9,6,-2,3,7,-4,-2,-8,10,5,9,-4,-4,7,-6,-3,4,9,4,-9,1,-5,-4,-1,3,8,1,-5,1,-1,1,-4,-5,-10,-4,-1,-2,-5,1,1,-3,4,-1,8,-4,-10,7,9,-6,1,8,2,-8,8,-2,-1,-10,-8,-7,4,9,6,8,8,-4,2,8,-2,3,-6,-1,-2,4,-9,-8,2,-6,5,-4,10,9,10,7,6,3,5,-8,2,-6,-3,-5,6,-5,-7,-4,-9,-8,2,2,-5,7,7,-6,-7,10,-1,-9,6,7,-7,10,-4], dtype = "int32")#candidate|4582|(1170,)|const|int32
var_4583 = relay.var("var_4583", dtype = "float64", shape = (26,))#candidate|4583|(26,)|var|float64
call_4580 = relay.TupleGetItem(func_2375_call(relay.reshape(const_4581.astype('int32'), [15, 1, 6]), relay.reshape(const_4582.astype('int32'), [15, 13, 6]), relay.reshape(var_4583.astype('float64'), [26,]), ), 1)
call_4584 = relay.TupleGetItem(func_2379_call(relay.reshape(const_4581.astype('int32'), [15, 1, 6]), relay.reshape(const_4582.astype('int32'), [15, 13, 6]), relay.reshape(var_4583.astype('float64'), [26,]), ), 1)
func_3977_call = mod.get_global_var('func_3977')
func_3980_call = mutated_mod.get_global_var('func_3980')
var_4590 = relay.var("var_4590", dtype = "int32", shape = (273,))#candidate|4590|(273,)|var|int32
call_4589 = relay.TupleGetItem(func_3977_call(relay.reshape(var_4590.astype('int32'), [7, 13, 3]), relay.reshape(var_4590.astype('int32'), [7, 13, 3]), ), 0)
call_4591 = relay.TupleGetItem(func_3980_call(relay.reshape(var_4590.astype('int32'), [7, 13, 3]), relay.reshape(var_4590.astype('int32'), [7, 13, 3]), ), 0)
uop_4592 = relay.cosh(call_4575.astype('float32')) # shape=(11, 5, 5)
uop_4594 = relay.cosh(call_4576.astype('float32')) # shape=(11, 5, 5)
func_3244_call = mod.get_global_var('func_3244')
func_3247_call = mutated_mod.get_global_var('func_3247')
var_4600 = relay.var("var_4600", dtype = "float64", shape = (832,))#candidate|4600|(832,)|var|float64
call_4599 = relay.TupleGetItem(func_3244_call(relay.reshape(var_4600.astype('float64'), [8, 8, 13]), relay.reshape(var_4600.astype('float64'), [8, 8, 13]), ), 0)
call_4601 = relay.TupleGetItem(func_3247_call(relay.reshape(var_4600.astype('float64'), [8, 8, 13]), relay.reshape(var_4600.astype('float64'), [8, 8, 13]), ), 0)
func_761_call = mod.get_global_var('func_761')
func_764_call = mutated_mod.get_global_var('func_764')
const_4608 = relay.const([-7,4,7,-7,3,-7,5,5,-9,-4,8,8,2,7,-5,6,7,-1,6,-9,6,-3,9,7,-1,-10,10,-10,9,6,10,-6,-4,3,7,-8,-9,-5,10,-8,-4,-2,6,7,-1,-9,-5,-8,-4,-8,5,5,8,2,-2,1,-1,-8,-6,2,10,-6,6,5,-9,10,-10,7,3,-7,4,-10,-4,-1,5,-6,3,-1,8,-9,-10,10,-2,-1,-10,1,-8,-6,1,-3,-1,3,-2,4,-2,-8,10,6,7,-10,-6,9,-3,-8,-4,-1,9,10,-8,-3,5,-7,-9,10,8,3,10,10,8,-6], dtype = "int32")#candidate|4608|(120,)|const|int32
const_4609 = relay.const(6, dtype = "uint64")#candidate|4609|()|const|uint64
call_4607 = relay.TupleGetItem(func_761_call(relay.reshape(const_4608.astype('int32'), [10, 3, 4]), relay.reshape(const_4609.astype('uint64'), []), ), 0)
call_4610 = relay.TupleGetItem(func_764_call(relay.reshape(const_4608.astype('int32'), [10, 3, 4]), relay.reshape(const_4609.astype('uint64'), []), ), 0)
const_4627 = relay.const([[[2.927978,-8.439891,8.165717,1.893786,-2.255194],[0.329344,-7.334058,4.802890,-4.593751,-1.783970],[-6.740032,6.599669,-0.673312,6.006295,7.009522],[-3.729513,-7.059203,2.325256,-7.749581,-5.826883],[9.528679,3.388958,-7.546539,-2.524980,0.001241]],[[4.131519,2.767097,-7.172303,-8.431626,-5.818780],[-0.272103,-3.995445,2.122525,-5.915729,6.566732],[-4.204488,-2.694374,-5.158771,-9.474346,2.340930],[9.235008,2.340729,9.136973,-1.699986,-9.098112],[9.917487,-3.000728,7.288270,0.069729,2.005087]],[[-7.476405,-6.337732,4.591398,-6.643683,2.176961],[2.832772,-1.664845,9.283212,-7.386890,5.291222],[-9.083844,4.863000,9.427652,0.727475,-4.169388],[5.976218,-4.940621,4.969968,-5.717400,-2.572015],[2.759687,7.264607,-0.238016,-8.752121,-6.903729]],[[4.290020,-3.545867,8.068348,-9.286377,3.299573],[2.997604,9.619602,-1.468835,3.589068,-3.403755],[-1.359549,-4.748735,4.691605,7.425423,3.552178],[-8.889372,-7.521407,-9.918506,-5.498271,-1.601818],[0.491255,-3.356029,-6.589576,-5.515034,5.626099]],[[7.096445,-0.126084,2.253293,-6.719430,7.406772],[8.130388,8.773515,5.631982,9.139495,-5.857345],[1.046886,-0.584965,-5.066917,-5.540077,-1.682041],[-1.475378,1.218392,0.399961,-2.864114,3.126861],[-7.071876,7.152687,1.193707,0.794203,-3.273687]],[[-3.111940,5.350180,0.387503,7.866421,-8.839069],[-5.263660,5.430049,-8.352826,-4.419137,8.804808],[-0.167023,-3.819984,9.130147,-8.441241,5.093612],[-6.852622,-4.615985,-7.318730,0.422307,5.422941],[7.419673,-6.058857,-2.002057,-8.091127,-4.434120]],[[-5.716007,9.533844,-2.463477,-0.140981,4.526933],[-7.721557,-3.703650,5.762496,-8.206868,-0.783287],[5.273530,9.806850,2.670377,-3.109373,7.015462],[0.913208,0.994197,-2.729815,2.167545,9.934562],[-3.248647,-5.520168,-2.517243,0.251093,-9.068279]],[[5.028021,-0.755631,-4.515448,-6.085399,2.883134],[5.160430,6.415041,0.870650,-7.974601,7.077594],[6.889436,4.208491,-9.710754,4.838151,0.979253],[1.027359,6.969819,0.713138,7.475725,-5.850424],[6.078239,4.290286,8.739635,3.727515,1.822130]],[[8.491073,-5.587067,-3.261509,-8.848169,0.589345],[-1.444819,-8.675065,-4.884543,0.980666,7.507265],[-4.578108,6.336064,-6.101413,-7.398419,-7.963158],[-8.506631,-5.332191,8.419108,4.086862,-2.506913],[5.923443,1.899795,2.950761,9.802466,-7.595837]],[[-0.572851,-1.932102,-2.617115,-6.219638,-6.821560],[9.724482,-0.386654,0.844280,-4.724729,-1.082776],[3.168585,8.921995,4.309289,-5.835930,7.084605],[-6.056996,8.335900,5.359734,1.876563,-6.911736],[7.026350,-0.010891,5.828399,3.959472,-1.675369]],[[9.098338,5.301197,-4.153871,5.997851,3.142496],[9.798630,-0.897869,-2.639032,6.593322,-0.340997],[2.832936,1.461434,3.863145,-0.080198,-1.344497],[-9.464921,-7.760440,3.969515,3.102912,-8.517522],[1.225724,-3.786137,-7.844943,-9.303812,-3.826420]]], dtype = "float32")#candidate|4627|(11, 5, 5)|const|float32
bop_4628 = relay.greater(uop_4592.astype('bool'), relay.reshape(const_4627.astype('bool'), relay.shape_of(uop_4592))) # shape=(11, 5, 5)
bop_4631 = relay.greater(uop_4594.astype('bool'), relay.reshape(const_4627.astype('bool'), relay.shape_of(uop_4594))) # shape=(11, 5, 5)
uop_4632 = relay.atanh(bop_4628.astype('float64')) # shape=(11, 5, 5)
uop_4634 = relay.atanh(bop_4631.astype('float64')) # shape=(11, 5, 5)
uop_4641 = relay.sinh(uop_4632.astype('float64')) # shape=(11, 5, 5)
uop_4643 = relay.sinh(uop_4634.astype('float64')) # shape=(11, 5, 5)
func_2531_call = mod.get_global_var('func_2531')
func_2536_call = mutated_mod.get_global_var('func_2536')
const_4651 = relay.const([5.076301,-1.949837,-4.227489,-6.663177,2.881109,2.506555,8.651172,-5.919718,-2.749528,6.256504,3.850475,8.580307,6.535458,8.734314,8.652883,6.834837,1.139623,9.331431,8.892255,-5.056126,5.610101,0.332218,8.683123,-6.085413,6.775641,1.417478,-0.852740,-2.127617,-9.389111,-3.198917,-2.394531,-5.131455,8.097195,7.977668,9.182311,2.941299,-4.070886,6.435386,1.715006,4.936525,-7.958141,9.547721,1.511788,-2.805913,-4.816226,9.064560,4.784800,-1.180706,8.963821,5.877970,9.050716,9.938824,-8.895280,7.260292,9.605018,-4.858145,9.502141,-9.239823,1.904130,-8.257489,-3.202568,-8.588883,8.769128,-8.697071,1.392402,4.987416,5.054133,-1.146638,-2.475603,2.015824,-3.445857,0.596889,3.129373,-0.160622,-3.286396,-6.290805,-7.304908,-1.808915,2.952075,-9.175646,3.619438,7.720241,-8.768020,-7.173456,-0.947347,-6.492312,9.365248,-5.142685,-2.197956,9.504963,-8.109818,2.070859,5.918216,-3.623771,-2.187967,5.987408,3.934808,-8.405360,-3.229478,-3.510900,-7.991393,4.994079,-2.724440,4.043777,-6.061870,5.065268,-5.372127,9.485079,9.411502,3.992479,-5.173499,3.802547,9.152423,7.762476,-0.413899,-4.734076,0.911279,-0.066509,-5.138141,-5.152270,-3.597258,1.501289,-7.948393,-8.036821,-3.496044,2.135108,-3.590842,-0.969146,2.006917,9.737451,2.533254,-2.176868,2.426059,-9.417583,-6.215803,-9.801710,2.289848,-3.655178,-1.150518,4.378374,-4.717225,3.528296,8.105431,-8.063744,-3.224934,-5.132384,-8.857865,-7.202950,9.368268,9.409307,8.541897,-6.073439,9.093193,-5.223159,-0.361134,-1.354908,-6.442802,4.242098,-6.368228,-0.215341,-0.898051,-6.005182,-7.092104,-1.377288,-9.114862,0.865140,-1.976772,-9.202139,-6.559731,7.512838,-1.287419,6.227861,-8.316137,-4.705133,5.354579,8.525423,8.823058,-1.714584,-7.349791,4.315825,-5.303620,-6.070797,-0.644001,-0.061918,0.694888,9.679430,2.304329,-7.331826,-0.854811,-9.105220,-9.388014,3.525613,-5.510368,7.569786,-1.594706,8.980450,7.229161,7.676942,-0.178980,5.700209,-9.864713,8.020785,5.190996,0.415695,-2.049327,6.380942,4.575639,-3.525088,-1.126235,-5.889801,-8.191452,2.725429,2.045316,6.731209,-3.866201,8.954123,-7.866923,0.934192,-1.811742,1.728963,-7.054995,3.015176,7.753386,2.606905,5.342218,-1.221653,5.199056,-7.811477,2.743828,-3.282523,-1.586984,-9.802140,-2.045805,-3.199854,-2.402742,5.390748,7.922439,-4.396989,-7.344180,-4.274858,0.937868,4.453185,9.633867,8.703804,-4.219152,-8.613841,2.191050,4.451615,-3.954842,-4.315617,5.872813,-6.886885,8.321557,3.269310,-4.592534,3.458217,-3.987156,3.658779,-2.112609,-8.290996,-8.211241,8.989546,0.387491,-4.970843,9.854471,-4.923564,-4.771461,0.428952,6.621352,-5.659360,-3.991224,5.103451,-3.651344,-0.817233,6.985972,4.309059,-8.158963,1.372043,9.997002,2.359933,7.327469,0.670619,-1.493466,1.411198,8.447915,-3.515797,3.680995,5.472296,-1.631726,6.009141,-0.095738,2.046560,0.739229,0.296775,-5.860099,9.526245,-7.988893,-3.248756,6.102132,8.320801,5.155289,6.245089,4.172670,-4.821712,-9.457916,-2.664815,9.738569,8.767517,-2.118787,6.596324,-6.361099,-6.670966,-5.056294,6.411992,-4.590208,-8.366720,-6.824313,3.990742,-7.746257,5.843731,5.034875,-2.604452,-3.352883,8.680540,-9.764430,6.013970,-8.606167,4.804461,-8.194663,-5.053783,7.323989,-0.460684,-1.864424,-7.041258,-8.773499,-8.194830,2.157633,-4.980595,-3.596912,-6.558968,-2.204363,9.412683,-3.603421,6.831306,-4.650658,4.352780,6.313721,6.386937,4.211188,-6.915161,-8.613937,4.220291,3.101791,1.266838,-5.033332,-5.849983,0.277615,0.027814,6.712256,0.470465,-8.100665,3.149422,-6.776059,-1.913127,-7.738777,1.148684,9.680679,-5.564860,-4.593356,-2.961339,-7.196813,-7.870949,5.137587,4.079716,-8.741558,-5.662283,7.750161,-1.837961,-2.855938,-5.587134,-1.912369,1.123121,-3.042385,-8.968468,8.828887,7.878569,-9.349567,-4.822650,6.292807,-9.968824,-8.022967,2.587576,-6.030435,4.886167,-8.701824,-5.764018,-7.129101,-2.716236,6.631421,7.320172,7.019187,-0.576480,-9.970171,5.447554,-0.380956,-9.964786,-5.564027,0.436878,8.106001,-3.772330,-1.795702,-2.518768,-9.176873,8.292432,-5.318364,4.412890,-7.946928,1.076822,-4.207856,-9.344592,-8.652747,3.759506,-0.956512,6.788268,9.960968,4.985966,-1.347688,-4.985511,-9.151065,7.860660,0.484733,7.812726,-6.885520,-1.628256,3.899878,-2.685936,4.357789,0.658963,-5.134325,-1.649658,-5.696754,6.176501,9.230027,9.206171,9.822438,-1.686024,3.615446,-4.378203,-5.076582,-2.642853,-1.185166,3.529082,-0.202730,7.301904,-1.700695,4.832888,-6.685715,6.838657,-7.166933,2.947466,2.517355,-4.719004,5.010673,1.528660,-6.716627,-2.426938,-4.202144,-9.385349,-0.481747,9.810270,4.850479,4.810033,5.976314,-0.027333,3.863577,6.972618,2.910012,-4.856288,6.479535,0.829315,9.162649,-5.319499,9.534202,8.175258,-4.027857,-5.963015,8.379963,0.065642,2.263727,-4.634569,-5.417521,6.760717,-4.768789,-1.658843,2.984430,8.213660,6.129037,-9.284185,-2.942651,-8.498422,-4.099269,4.497100,-1.585696,-0.349657,-4.084234,1.974575,8.219467,-5.326630,-8.967080,8.581807,-0.945035,-3.683862,-9.437779,5.968532,-1.389443,3.958081,-5.107294,-5.207436,-7.896965,-5.213621,-1.794728,1.816852,7.444342,0.737468,-1.916535,3.298579,2.071205,5.485836,5.370622,-1.232867,-1.353751,-3.848001,-9.260472,-4.108438,-1.647137,5.366661,-5.644235,-8.717866,4.924963,4.926979,-5.570647,-0.805014,-6.446977,7.132320,-7.836845,-8.183335,2.778188,-5.621312,6.385454,-7.621937,3.897260,-9.905780,-8.932487,0.305945,-2.914122,-2.675067,-1.958315,-3.382793,-5.305205,-4.502432,-7.588185,5.570627,2.624249,4.884618,-0.272287,-3.284380,-0.303962,1.243292,9.920001,-8.076796,4.061446,-5.723387,0.598517,1.623067,-5.918244,2.110215,-7.398597,5.873610,-4.694906,-2.352885,-7.600285,-0.946410,-8.011192,-4.467783,2.649780,5.143040,2.557980,-5.151329,9.955520,-7.395162,4.860679,-6.119270,-4.099708,2.412977,-5.717457,-0.813079,0.655075,6.868290,-8.790753,9.540409,-5.163010,1.331263,3.178171,6.790540,3.282613,-7.343128,5.121005,-4.507888,-0.641252,-0.674484,5.106054,-1.920567,0.533511,-9.157488,8.988282,3.989980,9.945439,0.021099,-6.768284,4.715937,-9.899727,-8.891862,-1.007544,2.122505,8.274337,6.501446,-7.236925,4.133956,-8.032506,-4.949597,9.463277,9.485449,-0.881698,1.091654,1.817000,-5.784662,3.641876,6.803664,8.371288,-8.053701,-6.456286,2.189705,9.318862,0.201914,4.843882,0.542873,9.566871,8.277979,1.059396,7.670185,7.329539,-1.362908,-3.018810,-3.548857,1.115751,-2.500871,-8.663924,-3.131013,-6.360327,5.120776,3.858234,4.280797,-8.180354,-6.833005,3.145461,-4.216663,4.983776,1.300984,0.622402,1.737387,6.252540,-4.618470,-2.944552,1.730450,-2.564009,-1.953024,-3.487366,8.778546,-0.092697,-7.308806,1.876459,-5.048946,-1.737883,-3.552431,7.369804,-0.889328,-2.357206,-5.122535,1.733012,4.194846,4.982575,-1.522807,5.534518,-2.431402,9.289902,-9.987197,8.850728,-6.223884,-4.019072,8.837611,-0.740130,-5.645033,2.661848,9.839665,6.556335,-4.495745,-1.325222,-7.156136,-4.028188,4.275178,3.387990,-3.775938,-9.419997,-4.111297,-7.361360,-3.857182,2.117115,4.998858,-3.333108,-1.918913,2.046221,-5.046669,7.705920,-2.521386,9.666262,6.482423,6.761289,9.234394,-1.553024,-9.098061,-1.149014,-5.490436,-6.553631,-9.794468,-2.195942,-8.490056,6.155008,-1.207557,1.218128,8.339053,-9.647948,2.240016,-3.566995,-4.340009,0.656694,9.495051,6.811179,3.148637,1.400172,-9.396668,-4.213804,-5.199835,7.195679,-4.660038,2.024928,0.316312,7.695514,0.855844,-1.298813,-8.478812,-7.288988,8.873867,8.020857,4.873948,-8.514832,7.326204,-9.325417,-1.846280,-7.601096,-5.140150,-1.167122,1.934342,6.687779,-7.137225,-5.867338,4.121477,-2.829154,9.693885,7.933970,0.799706,-2.651407,3.319276,-3.069419,1.378545,-6.265433,-8.714444,5.761180,-5.628948,-6.975314,-6.585426,-9.988432,0.791042,-7.701205,-4.123016,-4.234434,4.490082,-2.053024,1.170920,1.605904,9.328250,7.026792,-9.089834,-4.695984,4.189077,1.296363,5.426245,6.768370,1.669262,5.570336,4.603465,2.885820,6.127104,9.781246,-2.080883,8.276630,5.349499,4.756646,4.372812,-3.228685,-8.650419,6.133927,0.243819,-5.943719,-2.356639,4.104571,1.516074,2.895913,-9.417565,-1.680958,9.887151,2.366448,-1.180154,-3.441380,-2.770589,-3.457456,7.004646,-1.244498,-8.815272,6.690109,9.394646,-5.015336,5.128595,0.245267,2.140825,-8.600151,4.782269,8.603385,-2.085460,4.547884,-0.067419,6.157440,8.283516,2.482255,-8.245512,6.759077,9.365610,9.347904,8.565894,-9.484234,-2.840307,6.212423,-7.773343,6.799894,-0.897661,0.435268,-6.858765,-6.252456,1.760490,0.125159,-8.418967,2.106896,-4.757035,-4.579542,1.743549,-7.247108,0.756033,2.977827,-1.672402,-0.732150,5.496036,-6.602389,-0.624759,-6.065564,-1.170461,-0.992820,-8.887382,-3.836909,-7.568013,-4.023084,4.396231,6.666901,-8.103321,1.946761,5.831157,1.807853,8.414672,-0.515576,9.297111,5.163255,-6.524532,-8.516910,7.338524,7.219559,-6.088622,6.159982,6.858466,-3.161889,9.273582,-0.176958,-1.868485,-9.759358,5.119435,0.131098,5.763306,-3.902167,-6.517762,-5.279480,8.497522,6.461061,3.172237,-4.702521,0.197363,-0.892308,-4.926613,1.334039,-4.463638,-2.304692,-8.716366,-5.654263,8.942605,4.381476,-3.118924,3.795829,-9.528990,7.231011,-4.634184,-4.972882,-8.973420,-2.465410,2.554850,5.851518,1.652671,-6.955251,-2.564766,0.047126,9.127164,2.586290,-3.792656,-8.563683,-4.814801,-2.415633,0.819211,-9.578362,6.080006,-9.061081,1.681190,3.188727,8.878095,-2.273890,-7.084571,3.808865,2.847413,3.989285,-1.771558,-1.946767,9.906665,0.350813,8.088453,6.125912,-0.110193,2.805085,8.381122,7.895424,-6.358492,-3.772114,8.580083,5.143344,9.338550,0.852577,-6.362977,-8.580199,-8.644851,-9.478731,3.532332,3.883262,4.622478,2.680249,5.530529,7.646750,1.511744,-2.209446,-7.620074,7.163382,7.837896,3.811894,-2.338471,7.279685,7.344660,-7.528019,2.727456,-1.619640,-7.099311,-3.337786,-2.662272,-0.930521,1.116957,3.364951,-3.187059,9.484829,2.221962,8.631104,-1.129829,-4.382862,-3.193979,0.586738,-1.185866,-1.290533,5.626839,-9.940997,-6.212120,9.489896,-9.259626,4.514920,2.138735,-9.501319,3.692070,-0.977946,-7.919440,0.740587,4.214857,6.096437,0.083888,5.434310,-5.542742,-1.096192,-8.929841,-8.188726,-2.557362,8.539447,1.819393,-5.404940,0.181268,-7.217511,-2.534346,-2.243467,-3.829386,3.628409,9.500572,6.640042,2.922116,-4.524625,3.432599,-6.688164,7.282703,-3.701495,3.565123,1.002293,9.790114,-8.776290,-2.649402,-2.565834,-0.102536,-2.195103,-2.083609,1.036029,1.325235,4.088980,2.653366,0.258915,9.707092,8.782442,-0.925849,9.118664,-2.155156,5.845656,-9.012591,-5.105463,-9.245974,-9.997934,-2.277421,-2.123484,1.354083,-3.403942,9.010920,0.411377,1.430577,3.007973,-1.659129,-4.460016,-3.583381,9.043773,2.544652,-9.451831,-3.691937,-3.743763,-3.561927,-1.532984,-9.153470,-9.722645,-0.322741,-9.423634,-6.820020,-3.864972,-0.889125,-2.745474,-1.299073,2.718033,7.204747,5.012801,-4.835796,-5.534490,-9.573831,-0.274221,8.152853,-3.461983,2.906897,-3.812733,-3.301932,-7.496539,9.375560,-3.887945,-7.221807,2.206379,4.583168,5.812212,-9.479484,-3.664640,-4.446660,3.528270,-8.133852,-5.648485,-3.360435,5.192433,8.481904,5.440492,-7.340149,-9.039940,6.056868,-7.311616,9.063743,-0.706052,1.506660,-6.013363,8.524066,-1.115887,-6.772012,6.068009,3.984433,5.614618,-5.810885,1.958112,-8.725541,1.845631,1.680135,-5.848711,6.935686,-2.908825,-6.558476,8.269918,-0.564460,6.368740,-2.612083,2.344599,5.824866,-5.325187,7.294258,5.348472,2.004503,0.315878,-6.672105,1.222379,-7.333142,3.798067,2.506248,-4.103280,-4.182484,-0.619532,4.632028,-1.972483,-4.084635,-8.312644,-0.337071,-3.171796,6.885226,-8.905765,4.586760,5.343369,0.822728,-8.073514,9.733827,-7.730632,-3.992263,-6.870665,-1.956571,7.643408,5.049811,-5.798066,2.394966,-6.159967,-8.341949,-9.546532,-2.070638,9.731794,-6.393722,-6.636615,-5.041235,5.409377,6.427814,-7.248844,-7.905602,3.342805,-0.325350,6.307924,-6.276568,-1.858879,-2.510467,-9.767853,-3.954272,-6.689541,-0.243017,7.043452,3.597292,4.972798,-9.497718,-7.754718,6.850561,8.831276,3.338016,6.473001,-8.399918,-4.175725,2.899575,7.067560,-2.500665,-9.605149,6.181635,-5.013014,1.314287,3.718507,6.890223,-8.232272,0.061096,-8.393557,5.285078,-1.231136,8.261198,-6.410664,-6.058444,8.998089,-1.321612,1.861721,6.888884,-1.179450,5.509993,-4.742053,-9.396172,-4.912080,-6.700750,-6.420420,-1.974532,6.085743,-4.993399,-8.583385,-8.987793,6.146554,-5.245004,-5.538715,-6.870860,-6.442922,-4.834368,4.157171,4.720171,4.524044,-8.053249,7.948605,-0.612640,6.586305,4.076895,7.848775,1.507841,-4.875415,1.303929,0.960766,5.022334,-5.850081,-3.107698,-6.902420,0.629680,-3.625278,-3.448659,-6.102267,-0.098491,0.173513,-6.056439,5.626383,1.261426,4.654298,-7.168919,5.654591,-4.631554,-7.729122,1.527043,-6.532457,-4.809801,-5.768864,6.983631,3.519757,-2.994412,5.204343,-4.997358,-0.231008,-0.538364,-8.550795,-5.152917,-5.226320,9.038471,-5.677521,-7.730374,9.483895,9.728620,9.845437,5.912918,-9.197004,4.220523,-4.405019,5.828258,5.871901,-9.165940,-9.368736,7.705157,3.625295,3.309681,0.046171,-9.688757,-6.348615,6.435046,-2.946570,0.692577,-6.481620,-6.286306,-3.596546,-8.513424,8.933974,4.665622,3.841722,2.003590,-3.686465,-0.718290,-8.873976,-7.754367,-6.344742,-9.464997,-3.258893,-1.479653,-3.883039,1.897095,-5.418647,-2.261284,-5.447799,0.370450,2.543470,-5.865507,-8.340319,5.399463,-1.807606,2.364390,8.936961,4.769383,3.674907,5.627461,0.046702,-9.996271,-9.193074,7.464112,4.482050,-0.297530,2.299765,-5.109080,-7.494951,-2.541906,8.923982,6.206606,0.395557,7.269550,-9.381633,-8.174597,5.971827,2.957823,-8.131938,8.391981,-3.122008,-5.270496,-6.722263,7.982430,-7.234014,5.108742,2.070078,3.695490,-1.924436,-6.571270,3.365324,-1.174378,0.157072,-7.180630,-9.397648,7.809785,1.210168,8.938849,-9.313390,-2.931494,-4.347965,8.365296,3.646008,9.126006,9.702001,-8.695206,-3.067440,9.440607,7.558830,3.887126,4.954592,-3.778639,-9.536838,7.265099,-0.365128,-8.771881,8.636568,-1.760430,-1.110351,-7.228478,5.918908,-3.513843,6.234781,-2.307855,5.331451,3.316525,-7.713663,5.045325,7.749626,-8.767327,9.889680,-8.831454,-9.982377,1.877133,-0.467834,-7.977689,-2.132115,-3.751998,-0.555672,-1.203307,-3.570082,5.030920,0.988052,-3.936756,3.908666,-0.014730,6.391417,0.210440,-5.829165,-1.415818,6.647527,-1.573455,5.450771,0.499516,2.401546,4.866655,8.763309,6.679897,1.506744,8.474943,-3.833691,8.122836,5.286258,0.341821,7.207788,-6.817252,-2.396800,5.571632,2.292436,4.655440,-6.606482,3.117583,3.182928,9.475430,-8.454710,9.376433,-4.243933,-3.061660,-8.869342,9.745609,7.607264,-0.431098,6.298444,1.358616,-8.485173,1.096930,7.369524,0.224283,8.492380,4.163846,7.741317,-7.815819,-6.502241,7.870405,-0.548414,-6.091522,2.998169,2.640589,-1.808615,5.131959,-3.553293,-1.126491,3.619498,-0.578735,-6.932614,-7.732437,6.107077,1.208581,8.698689,-9.214203,-6.015520,8.161836,6.342634,-6.795168,0.502874,-0.200164,-0.058130,8.039599,-8.145986,1.991597,-6.770539,7.489775,-1.032020,8.914085,8.209088,-8.178396,-8.110119,5.436184,-7.710357,-9.367633,-2.714894,1.523171,4.839673,-7.819464,5.614395,-3.214052,-1.576062,6.476685,-6.223032,-8.382216,-6.528382,0.255975,9.947874,-1.978678,-6.588358,2.938674,4.930439,-8.906612,-5.130749,8.287832,-6.223252,8.462673,5.948968,0.883158,5.480082,7.476784,-3.886700,-3.212532,-4.924204,-2.737428,9.689878,2.101929,-4.727004,9.967086,-9.274850,-1.602556,-0.790679,1.987223,-5.783058,-1.369155,0.559560,6.652076,-2.850374,7.802600,-5.172288,-7.601802,7.910311,8.188852,1.137598,-7.612046,6.657513,-4.946402,-8.796450,0.220957,-0.164861,-7.526744,0.646918,-1.599265,-3.056002,-0.308429,0.881689,-1.538729,-4.879198,-0.332934,5.998311,-4.499896,-9.091113,-5.651317,-2.916985,2.554440,8.316866,-0.577204,-8.897731,9.884724,-8.388956,6.114888,-3.528364,8.525131,1.457598,-6.401749,-4.052443,4.130764,1.357138,-5.639349,0.548105,-1.437062,7.378397,-4.138364,0.634868,-4.380926,8.803640,7.956047,-6.360318,2.844706,3.448738,-1.879489,-8.826417,-3.584635,5.975563,5.565099,-2.078468,-4.706842,9.397971,0.447267,-5.940030,-7.065136,-6.727306,0.403356,-1.996649,-0.352833,-6.851123,-9.001728,4.878656,-5.772193,4.621253,6.384657,0.589295,6.679434,-2.249892,-9.672526,7.063218,0.001346,-6.237691,-2.401961,0.381000,-3.383012,8.128979,-4.452811,5.618630,0.736214,-6.637463,0.524210,-0.009200,-1.714045,7.284227,7.415533,-0.479814,-6.236563,0.346975,2.131396,-7.036812,-0.137342,-3.634730,-8.819117,0.364672,-3.040871,-8.738948,-9.413285,8.764657,-7.429084,5.225827,3.084607,-5.005746,-6.893738,-2.082565,-4.787175,-7.129973,-3.506356,4.089990,-3.487703,-1.102309,-2.939291,-0.543124,-6.555609,-6.531189,1.188175,-3.216662,4.209502,-7.390060,4.678685,9.621117,9.618989,-4.362665,3.259881,-3.904985,8.630559,-9.589313,-0.850005,-8.716556,-5.168809,3.221323,-4.669516,-8.253777,-8.987976,6.029652,6.779648,8.965322,-4.168156,-7.611482,0.411277,-3.556285,-7.022738,-4.075914,6.778946,6.557179,5.905640,1.969283,-6.477395,5.550864,8.850297,-7.645740,-4.907110,3.244585,-2.833746,-0.875241,2.557238,-9.987743,4.453005,-1.559790,9.226020,8.626551,-1.951172,-8.396122,-4.915259,9.968569,-9.612033,9.405770,8.432898,-5.011995,-6.053082,0.598936,7.221949,2.832700,-3.912920,8.661669,5.831033,4.862778,-1.363797,4.794068,3.514093,-1.252069,-5.290997,-9.509440,-1.443114,1.057970,6.637391,-8.481858,-8.390614,-2.610517,8.407557,-6.044579,-2.352446,-3.209723,5.322907,6.001372,-2.168648,6.339377,2.022972,-8.016358,-1.630172,2.261247,-5.189258,-6.060714,9.440152,-8.661562,-7.743290,-7.204929,-3.093712,6.861812,-0.912577,-2.252424,-1.095900,8.614849,-3.514281,-7.023718,-1.477186,-4.497654,2.367444,1.868312,6.014953,-5.472868,2.925685,-4.374007,7.728771,7.524709,8.118885,1.060394,6.342988,1.684064,-2.780286,-2.169798,0.617567,-5.411826,1.548515,-2.528322,3.769104,3.695661,4.933628,-6.258623,0.919590,-3.085201,4.701713,0.379235,-0.130647,-2.793103,-6.960143,5.538528,-8.016199,-1.069161,-7.381776,-8.227157,0.479587,-5.399915,-6.492029,-2.688609,-1.032366,-3.080334,-0.779493,5.575883,-2.145386,7.176014,-1.571155,0.734828,-9.314849,9.322524,-2.988131,-9.305095,3.447108,-4.738680,6.587338,7.858336,6.852886,-0.352206,3.972536,-6.213544,3.093687,-8.817746,0.361136,-4.217074,-0.355011,-7.541355,-2.755643,-4.765695,6.061615,3.663449,0.444039,-6.086874,-5.108367,-0.964431,-1.393628,8.290183,1.888657,-5.265383,6.349315,-3.184271,-1.347881,-7.884830,-4.209302,-2.878418,4.901344,-4.780639,-7.533893,5.983896,2.296075,6.239246,4.986927,-1.018172,-1.208263,0.453398,8.629527,7.793424,-4.376780,-3.546552,8.287781,-2.957583,-0.047108,5.181934,8.439945,9.523371,7.025338,5.841414,-9.666030,1.847809,-9.605702,-9.691971,-8.868453,4.009175,-2.232042,8.483842,-2.553953,-1.535074,6.320928,1.245037,2.829998,3.326682,6.296719,9.945690,-7.223566,9.655546,9.152008,6.239026,4.427980,-9.906814,-1.361413,5.741148,1.732602,-6.149931,-1.610871,0.743613,-2.140931,-7.581597,2.410712,3.863337,-1.773131,-0.472442,7.688522,1.199842,-7.957564,-8.505139,-6.578976,5.446960,8.384679,-8.963899,-9.593052,4.359426,-7.417760,-1.702557,8.369587,-0.946525,-6.319489,8.030442,-6.125848,5.843422,-5.161825,6.103429,1.524123,-9.999982,-3.784004,-2.509146,1.067709,-0.517754,1.578040,6.976389,-3.432749,-2.090945,0.581678,-3.545892,3.854840,-2.991626,1.634294,-4.328304,9.859016,-3.666115,2.655655,-3.239569,-1.788958,-4.608700,6.161958,8.905946,6.079862,4.043308,7.766781,-6.718854,8.814258,8.891521,2.475221,4.183316,-2.076655,-7.696445,3.935275,-8.128711,6.283717,3.790950,2.464168,0.935093,5.798800,2.684794,-2.897267,0.492803,-8.523667,4.235224,-5.969442,-9.251435,-4.845205,-6.635115,6.444640,9.858763,2.729603,-4.562936,1.427290,-1.133215,-7.448550,-9.136409,3.393764,-8.184350,-6.855224,6.042856,-1.943657,1.372207,1.576975,-4.667418,5.958689,3.806754,3.152054,8.298783,9.808745,0.591556,5.688162,1.969754,4.519051,-5.760117,4.090868,-5.172518,-3.098145,-5.106359,1.937209,-9.227423,-2.911135,3.251532,9.892338,1.109324,-4.929074,-0.090394,-9.492726,5.071798,2.945924,1.251156,4.029980,5.038331,8.012812,2.626950,-4.328913,2.649838,-0.046867,-2.351193,9.829348,-7.469942,-4.083177,1.608638,-1.252799,-9.407848,5.355709,-1.977064,9.992407,-4.306563,5.549547,4.912743,4.321961,1.758049,-3.360156,-4.361592,9.983204,0.915920,3.854285,-8.825723,2.987170,-5.257339,-4.516631,-1.790829,-3.933013,-2.774217,-0.389965,2.592514,0.315799,8.024827,8.855314,5.929307,3.517802,-4.714318,-1.505842,-3.287986,-3.612588,-2.660670,-9.979007,-8.579096,5.890784,-8.124314,3.824539,6.625319,-3.542513,-5.670295,-7.643153,-3.662540,-2.419539,2.216806,0.737337,7.856279,-4.112246,-2.664375,-4.221621,3.880706,-6.607899,2.190730,3.962242,-0.240258,-7.376079,2.061480,-8.504443,-3.188182,8.554374,2.519371,8.171151,-5.459890,-4.239062,-6.933157,2.281838,-6.498106,-1.642230,1.489913,2.743204,3.541496,-0.416233,-9.132708,2.724890,-1.155100,-6.842801,4.687595,-0.571670,1.305830,4.953602,3.229716,8.524973,-9.001340,5.350973,-0.958878,8.343141,-7.918588,-9.199756,-2.713643,4.258283,-3.372406,9.597602,-7.778100,3.602483,-0.055454,5.243244,-5.438968,-6.813599,-4.173614,-4.659851,-2.181115,4.515482,-0.687786,9.831676,2.455899,5.090107,5.200178,8.819796,-7.796752,1.546813,5.865972,-7.360632,-8.617172,-1.641066,-5.672900,5.827392,-7.021438,-8.218787,-2.391284,-2.635115,-7.267773,-8.599605,-1.806493,0.942803,-7.988810,2.053865,-5.286886,0.114316,-0.787553,5.869623,9.447961,0.519435,9.027279,-5.542224,-7.113819,0.190099,-0.242117,-3.849084,-7.373520,7.487347,-4.253852,-6.057783,-5.167277,0.176566,-2.118246,5.375450,0.873949,5.653586,-7.655299,1.834023,-4.047108,-6.906350,-4.508576,0.483060,-8.711821,4.431323,-1.282628,5.108244,-8.400392,1.141522,-0.018451,-4.505964,-0.896694,-2.622617,1.056384,2.675464,8.833123,-8.230525,-6.326434,-4.142614,-1.759021,6.066954,4.900955,8.848462,-1.490098,-6.338099,5.848551,-1.855393,8.296936,4.006723,-5.287138,-0.132879,-2.054641,9.442726,6.681491,9.346625,-5.965927,-6.662238,-9.721121,9.740439,-4.604315,5.146488,-9.867378,5.449082,-3.265992,-1.961527,8.865600,-2.462908,5.653470,-0.713144,3.699804,-3.471939,0.700603,-6.501558,-7.896935,-4.247818,3.506941,-9.101082,1.762137,4.731995,-9.836687,0.341433,8.888914,4.811756,7.247074,4.730667,-3.872199,-3.642331,-1.135440,7.476817,-9.171166,1.705857,2.935219,7.332597,-1.133293,-7.950093,-9.980683,-1.598569,-0.021473,-1.405565,-0.362783,-1.083718,1.432748,-7.444073,3.168897,-3.943301,5.972140,-5.850467,-9.021071,5.409486,-8.872786,0.845447,5.774038,-7.568465,-8.257704,-8.085154,-8.112385,3.455778,7.780957,6.717905,7.008625,4.894214,-5.516846,9.147739,0.700133,6.733479,-8.784678,0.910309,-9.405308,3.570508,-6.347598,7.750154,1.637822,5.800718,-9.315085,1.830747,-2.073746,-8.883773,-0.157162,7.694313,0.806222,-0.320645,-7.465822,5.094308,6.651924,8.942990,-2.939630,2.726282,4.452997,1.953325,3.241406,4.526747,5.000747,-1.955410,8.460211,3.113794,-3.469234,-0.106231,7.015624,-9.283115,5.377697,3.596932,-4.495190,1.098330,0.832502,-0.895012,6.938595,-7.557115,2.407967,7.505785,9.908957,9.642127,-1.335025,-1.105725,-6.168711,-1.392553,-2.648142,1.106704,-6.855115,-4.395042,9.371872,8.895448,-1.112715,8.936194,-9.409542,-7.100031,-8.624539,-8.583502,9.463005,-5.052638,0.861648,8.710148,-6.237427,-5.525926,8.849368,-3.618632,2.368997,-8.567172,-3.528014,-6.474062,-6.949697,-8.777833,-3.622394,5.786072,1.186530,5.322986,-6.714787,-3.802262,-6.985981,-7.953129,3.735732,-2.296442,-2.364241,-6.304464,8.191775,0.151022,6.580873,-6.808900,-4.696902,6.835936,4.309105,-5.869668,-0.028502,8.708038,-4.752753,-3.662623,-1.675074,-9.544439,7.260533,6.464288,9.568216,-6.521587,-2.745816,3.051074,-5.576576,-6.804390,9.538564,-1.894521,9.161123,-3.888466,1.209680,6.356774,-8.737719,-6.822004,-3.210794,-7.714505,-8.263537,-8.010151,4.010826,-8.182840,1.129398,3.806408,2.752358,-6.371169,2.928407,-4.620205,5.522739,0.258886,-7.410756,-2.332813,8.039913,-9.024596,1.730930,0.611253,-0.931651,5.291379,-8.205748,7.590314,-1.982184,0.971780,-7.400084,-9.106403,3.742171,4.430299,9.817664,8.827395,-9.185051,-6.202792,-8.799787,-9.692367,8.635719,-8.043292,8.017463,-4.814879,7.733741,2.276272,6.651729,-0.085025,8.113326,-9.045098,9.507243,-7.160449,-6.953478,3.058187,-9.131475,6.703367,3.789447,6.923813,4.127251,-4.166798,1.910388,8.483641,7.444719,-9.501436,7.916811,4.280348,-1.851265,3.635191,0.498770,7.980620,-4.236353,1.480057,6.253475,-3.472275,-9.878834,8.539629,2.125343,7.487623,-8.641354,6.734509,-7.644623,-1.062116,-2.832188,9.440523,0.876098,5.290435,-8.277218,8.849218,-1.600531,-5.456019,0.977393,-6.092551,-0.977300,8.345680,9.793969,1.351700,-8.860853,-1.546985,4.487223,-9.032876,7.604830,-9.351304,-9.958465,3.597897,-0.195875,-5.836868,3.406428,-1.194533,-2.571090,5.023421,-9.824401,5.350478,-7.710380,-7.754007,-8.893674,-4.245906,-6.908272,2.994032,7.156445,9.158991,-4.465772,5.064385,2.526441,-5.721192,5.489401,5.109309,-8.854212,-3.167385,5.453562,-2.822084,0.876512,6.903819,4.762766,1.876279,1.594390,-4.426890,-0.034382,1.484639,3.897709,1.842182,2.775938,7.537505,9.172578,5.097564,-6.796978,-7.331981,-3.519755,1.597498,-2.305819,-9.025928,-9.255384,-0.343943,-5.346469,-5.114496,6.387324,3.700691,-5.258430,-7.220489,-8.304853,-7.643252,4.428906,8.882206,-8.549300,5.645713,9.432232,-0.627972,2.858846,-5.557379,1.800178,0.672479,-4.968398,4.988063,9.727239,-0.183229,2.379988,-9.666675,-3.365866,4.585372,6.408029,8.158485,-8.716913,-0.025863,-7.449167,-2.256678,2.101399,-9.420136,-8.625888,-7.892468,7.254712,0.172449,-5.087690,2.049263,4.307461,4.015916,-8.090466,6.404838,8.921365,-7.534573,-8.932665,0.920935,-5.423311,6.215766,3.151230,0.036735,2.724945,-9.715420,-8.734491,-1.641164,-8.458368,-1.548579,-1.826514,6.499167,2.192557,-9.273734,-5.267383,9.320518,4.783904,0.781318,3.556156,-2.895600,-5.982278,-0.239714,-7.276070,-4.392793,-0.580263,3.416961,8.910187,-0.177710,-1.555232,-8.086390,-8.854571,-9.605836,7.816070,3.747998,-6.245088,4.307122,-1.676227,7.954125,-0.099997,1.698857,4.047867,0.679916,8.609396,9.578058,-9.299449,1.449234,-0.283434,5.879585,7.175727,-8.436324,-5.948082,-1.825750,1.215687,4.236985,-8.473940,-1.377626,-1.258716,-8.212421,-0.228643,6.007826,8.688011,9.418609,-4.361519,8.083103,6.215521,0.819337,7.277640,-4.835325,-5.434242,-7.006332,-7.456428,-5.582083,6.723383,0.163542,-3.065647,-8.016580,8.314273,2.587327,-7.197666,2.344709,-8.598783,0.557228,9.398088,-7.602574,-0.198772,-1.973981,-9.808181,9.627966,7.774890,4.096494,7.456114,4.851338,6.353634,5.619338,-3.124062,-5.729977,8.380389,-6.032035,7.364661,-4.319676,-8.052583,3.281695,4.156596,-5.621136,4.652876,5.491115,6.559332,8.764658,8.615343,9.248846,7.921797,2.400285,4.181572,7.923834,-0.071884,-2.950580,-5.951999,4.825645,-3.015532,-3.949582,6.604940,0.315234,9.921499,-1.028196,6.948554,-7.913095,2.289780,3.708288,7.504180,6.542226,6.551245,-2.889380,5.388506,1.313484,3.774608,0.472742,2.752374,-5.894621,1.218797,-9.059797,-1.989346,-6.276744,-0.753537,-4.823250,-8.004147,4.354283,-0.737507,-4.427713,-2.790823,7.207094,4.393056,-6.352925,5.867500,9.233850,1.114137,0.760094,-8.891466,2.287100,-5.496611,4.317157,-6.563202,-1.150652,-9.804086,-2.513107,-9.548190,3.786759,8.711485,9.312880,-5.888469,6.500544,-9.071854,2.459960,-3.374882,3.206572,-7.870396,-4.544845,0.180671,2.285003,7.837355,-4.380425,-9.603440,1.797077,-6.313896,-8.148248,-4.836182,-3.659011,1.676998,7.890194,9.448514,-8.917946,6.787348,-0.647625,0.405310,3.217182,8.491511,-5.127678,3.718057,3.036865,-8.494015,-4.307545,-3.212304,4.344080,-0.727276,4.235760,5.994584,7.402213,-5.763280,-3.019095,-2.255256,-1.804726,0.628793,0.957075,2.769953,-8.499792,-6.304054,-2.758929,-4.543634,-2.295769,-4.416627,-4.115842,1.499864,8.043977,3.003995,7.045451,3.631588,1.053966,4.058471,0.936992,-2.601091,-6.846997,-3.309004,4.911247,4.021539,6.354474,8.063157,0.714466,7.254684,9.442279,-4.653535,-1.155338,-7.087720,7.506299,-6.565736,-1.057806,-3.525730,-3.560538,7.968114,6.834372,0.752071,0.621685,-2.984813,-4.363258,1.724846,-9.991006,-8.715853,4.447378,7.605243,-9.409848,5.092254,-7.053096,-4.186293,-1.555211,-7.893251,-6.896977,-3.946228,-6.747452,-4.132430,-5.112844,-4.487769,-2.019121,-5.619530,-7.226154,-6.774817,2.344000,7.638961,5.941741,-0.664571,-4.805912,-8.812386,6.319306,-9.324517,5.887070,-6.044630,-4.452677,4.274617,5.073299,-1.682561,6.298673,6.594774,-1.758523,-4.310112,-0.939687,3.715226,7.320992,4.488916,-4.297130,-0.037429,-2.435042,7.001370,-1.005397,0.338147,-5.746499,5.045637,-6.404183,3.199625,0.184798,4.502042,-5.758343,-9.142910,-0.907950,-9.041499,3.800187,-6.969915,5.668216,-5.704897,-3.749045,-9.575790,6.343457,-6.032610,-1.198703,-7.357209,9.543135,9.432945,-5.709608,6.678190,3.210145,4.001681,8.950053,-0.251076,-3.144953,-2.632020,8.377891,0.699375,-3.795867,-3.457677,6.570634,-1.859677,-3.550950,5.584462,-9.679269,8.839551,-9.910553,-3.370487,9.419630,3.679525,-7.939402,-3.228800,-5.234983,-7.070871,-7.107598,1.771450,-0.024378,-9.005432,6.997995,7.426560,9.032574,0.715399,-9.301466,4.138946,-9.044960,0.660749,-9.540341,-6.776540,5.625898,2.067067,-3.418148,-6.014988,-8.542461,0.118088,-3.863765,0.642303,-1.396164,3.315877,7.039670,-1.083503,6.151550,-5.701122,3.087994,-9.775072,5.583572,-3.222790,-3.908870,-4.353960,-3.923496,-2.684963,6.704044,-6.382378,-3.763733,-3.014957,-7.067709,-4.650896,-4.008493,3.491741,5.274971,-5.691520,0.191431,-5.523603,3.851996,-3.576835,8.066253,-3.755375,7.400085,-0.950759,5.781539,3.934528,0.436329,9.392932,-0.391095,8.262503,3.777866,-3.980655,5.874654,-3.895858,-1.206673,-1.472463,-2.950071,-2.171052,2.733110,1.882749,6.111770,-2.124703,-8.432394,-5.818956,-9.238472,3.884678,1.628469,-1.435057,-6.320713,-7.933514,7.354195,-5.827739,4.000534], dtype = "float64")#candidate|4651|(3072,)|const|float64
call_4650 = relay.TupleGetItem(func_2531_call(relay.reshape(const_4609.astype('float64'), []), relay.reshape(const_4651.astype('float64'), [16, 16, 12]), relay.reshape(var_4583.astype('float64'), [26,]), ), 0)
call_4652 = relay.TupleGetItem(func_2536_call(relay.reshape(const_4609.astype('float64'), []), relay.reshape(const_4651.astype('float64'), [16, 16, 12]), relay.reshape(var_4583.astype('float64'), [26,]), ), 0)
func_443_call = mod.get_global_var('func_443')
func_447_call = mutated_mod.get_global_var('func_447')
var_4662 = relay.var("var_4662", dtype = "int16", shape = (63,))#candidate|4662|(63,)|var|int16
call_4661 = relay.TupleGetItem(func_443_call(relay.reshape(const_4609.astype('int16'), []), relay.reshape(var_4662.astype('int16'), [3, 3, 7]), relay.reshape(var_4583.astype('float64'), [26,]), ), 0)
call_4663 = relay.TupleGetItem(func_447_call(relay.reshape(const_4609.astype('int16'), []), relay.reshape(var_4662.astype('int16'), [3, 3, 7]), relay.reshape(var_4583.astype('float64'), [26,]), ), 0)
output = relay.Tuple([call_4580,const_4581,const_4582,var_4583,call_4589,var_4590,call_4599,var_4600,call_4607,const_4608,const_4609,uop_4641,call_4650,const_4651,call_4661,var_4662,])
output2 = relay.Tuple([call_4584,const_4581,const_4582,var_4583,call_4591,var_4590,call_4601,var_4600,call_4610,const_4608,const_4609,uop_4643,call_4652,const_4651,call_4663,var_4662,])
func_4676 = relay.Function([var_4583,var_4590,var_4600,var_4662,], output)
mod['func_4676'] = func_4676
mod = relay.transform.InferType()(mod)
mutated_mod['func_4676'] = func_4676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4676_call = mutated_mod.get_global_var('func_4676')
var_4678 = relay.var("var_4678", dtype = "float64", shape = (26,))#candidate|4678|(26,)|var|float64
var_4679 = relay.var("var_4679", dtype = "int32", shape = (273,))#candidate|4679|(273,)|var|int32
var_4680 = relay.var("var_4680", dtype = "float64", shape = (832,))#candidate|4680|(832,)|var|float64
var_4681 = relay.var("var_4681", dtype = "int16", shape = (63,))#candidate|4681|(63,)|var|int16
call_4677 = func_4676_call(var_4678,var_4679,var_4680,var_4681,)
output = call_4677
func_4682 = relay.Function([var_4678,var_4679,var_4680,var_4681,], output)
mutated_mod['func_4682'] = func_4682
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_4697 = func_4250_call()
call_4698 = func_4250_call()
const_4701 = relay.const([[[-5.333916,-0.958490,1.539986,-8.323092,3.481299,-3.077611,9.623636],[6.773480,1.153664,-1.992163,4.533284,-8.414692,7.223819,-2.782380],[-1.277493,7.436550,2.780777,4.118347,0.169486,4.499046,8.988323],[-2.702618,-6.880307,7.381008,-5.869566,3.649157,-0.333828,0.544890],[-7.206694,9.152339,6.163743,4.789071,-9.207454,0.213690,9.642685]],[[-0.816085,-7.530241,9.091378,-7.140600,4.820644,-1.459345,-5.220856],[-8.667798,-2.454009,1.860581,-0.847108,5.841793,-0.848159,-8.004475],[1.508134,-6.022801,-5.126001,7.293810,-1.730024,4.348422,-6.638925],[-1.667691,-2.805874,-2.243019,2.660006,-7.977127,3.011283,8.018572],[1.014233,3.152171,1.587377,9.702607,3.331585,3.484973,-7.333330]]], dtype = "float64")#candidate|4701|(2, 5, 7)|const|float64
bop_4702 = relay.divide(call_4697.astype('float64'), const_4701.astype('float64')) # shape=(2, 5, 7)
bop_4705 = relay.divide(call_4698.astype('float64'), const_4701.astype('float64')) # shape=(2, 5, 7)
func_1890_call = mod.get_global_var('func_1890')
func_1893_call = mutated_mod.get_global_var('func_1893')
var_4707 = relay.var("var_4707", dtype = "float32", shape = (240, 2))#candidate|4707|(240, 2)|var|float32
call_4706 = relay.TupleGetItem(func_1890_call(relay.reshape(var_4707.astype('float32'), [2, 16, 15])), 1)
call_4708 = relay.TupleGetItem(func_1893_call(relay.reshape(var_4707.astype('float32'), [2, 16, 15])), 1)
uop_4709 = relay.sin(const_4701.astype('float64')) # shape=(2, 5, 7)
func_4442_call = mod.get_global_var('func_4442')
func_4445_call = mutated_mod.get_global_var('func_4445')
const_4722 = relay.const([-8.025400,9.427494,2.251202,-9.959034,8.425283,4.765244,8.672630,-8.259276,-8.373379,0.238293,7.695704,1.198128,6.352263,4.533154,-2.082435,-1.278295,-9.616327,9.060538,2.732323,5.765011,-4.472935,8.131076,-5.902178,-6.861474,-7.828649,-9.540694,-5.245841,-7.041038,2.145303,-0.367738,-4.706955,8.633549,4.641200,-5.709968,-1.432519,7.848185,-7.629092,1.292830,-3.374623,5.988400,9.642812,6.211934,-3.156653,3.863503,4.749160,5.658478,-9.569977,-1.657080,6.590328,3.019853,6.837398,-3.740846,7.577172,-1.966450,9.929209,-5.857777,0.965566,-8.158187,-6.351832,-5.818688,-1.282520,8.338183,-6.894470,-1.055138], dtype = "float32")#candidate|4722|(64,)|const|float32
call_4721 = relay.TupleGetItem(func_4442_call(relay.reshape(const_4722.astype('float32'), [8, 4, 2]), relay.reshape(const_4722.astype('float32'), [8, 4, 2]), ), 1)
call_4723 = relay.TupleGetItem(func_4445_call(relay.reshape(const_4722.astype('float32'), [8, 4, 2]), relay.reshape(const_4722.astype('float32'), [8, 4, 2]), ), 1)
func_1890_call = mod.get_global_var('func_1890')
func_1893_call = mutated_mod.get_global_var('func_1893')
call_4724 = relay.TupleGetItem(func_1890_call(relay.reshape(var_4707.astype('float32'), [2, 16, 15])), 2)
call_4725 = relay.TupleGetItem(func_1893_call(relay.reshape(var_4707.astype('float32'), [2, 16, 15])), 2)
func_3244_call = mod.get_global_var('func_3244')
func_3247_call = mutated_mod.get_global_var('func_3247')
const_4731 = relay.const([-6.025254,-0.957994,7.461900,9.223422,-0.011063,-6.475290,8.975191,9.667985,6.466199,-3.505436,2.581851,-7.313244,7.989584,4.919165,-6.830951,-5.382018,8.362360,3.165600,5.265385,3.926494,0.474577,-6.659515,4.517319,0.459404,-7.874353,5.164183,5.192586,-2.190627,-4.385332,9.351155,-0.120160,7.930877,-8.111264,-9.511650,-0.537402,-9.925381,1.418647,-7.118437,-3.237233,9.948938,-2.555761,-8.878949,-8.108709,-5.286688,9.918583,-3.477150,-1.232939,3.712997,-1.502691,-0.467285,-8.574989,-8.987726,1.355985,-5.043580,-9.933647,-0.866177,-0.229951,-4.250992,6.494159,-5.787483,5.984578,2.327900,-8.388752,-4.334236,-5.624564,4.798960,8.402783,3.275023,4.907406,-3.753819,0.860529,-7.978512,-6.319286,6.143561,4.102754,-2.398289,-7.966253,-7.635532,-1.982702,4.458314,2.634999,3.241028,-9.484349,6.700435,-3.531751,4.218430,5.660720,-3.524499,6.618752,4.946666,4.671759,4.894617,9.795928,-8.867099,-7.950516,6.288122,9.979686,4.089685,6.742067,9.563478,-4.528460,8.123269,-4.954453,9.615172,7.773116,-8.520774,-7.160715,-2.065955,-3.534172,-8.932799,-9.219232,-1.539656,-1.756678,4.446561,1.193029,-1.514277,-3.180783,8.048475,5.116510,-0.634919,5.585356,4.544693,-9.366746,-5.849468,-3.422337,2.684146,-7.983964,-6.042563,7.460795,-0.072901,-5.241906,9.813648,-4.124976,4.332133,1.315075,8.257241,4.263473,8.345285,-7.756783,-9.201379,-8.075621,-4.233630,3.080537,9.441162,-5.687145,9.053764,-7.859653,4.313544,3.719040,-8.231465,-0.307789,-6.870618,-4.481622,9.867304,9.752729,-2.308921,-4.022135,-9.174869,7.097985,-7.678850,4.338724,7.081202,-4.880105,-3.643044,5.205085,8.437088,-1.262975,5.966409,9.417398,-4.936764,-9.225428,-9.723222,5.513005,2.449839,-6.334057,-1.782701,5.476729,-9.666595,6.331816,-1.572877,6.035556,-0.273064,6.506273,8.760182,1.447234,0.170384,-4.193736,-8.222747,-4.989876,-3.515746,4.364828,-7.337041,-3.964155,4.564409,6.676098,4.190994,6.559623,2.064993,5.544224,2.600401,-5.296274,1.417673,-3.845458,-3.093282,4.183304,7.132083,1.646215,9.487461,-1.544942,5.757539,-2.305013,8.362266,4.653746,-6.587116,9.769949,5.081292,-8.298586,-9.246496,-8.258894,5.232307,4.615094,-4.000047,-5.728420,6.748247,-6.161658,2.030000,7.551544,-4.866384,2.806388,8.528166,-3.370897,-7.389337,0.946193,0.436193,0.018069,9.457182,-0.606127,7.435462,-7.565383,9.836757,-9.425336,4.857305,9.217808,-2.899519,9.157492,5.346504,-4.425790,-1.728514,-2.698031,4.753168,4.984951,5.961001,-6.875215,-4.936073,8.545350,-3.042615,-4.056076,0.201623,4.394771,-9.718077,1.271901,6.022061,3.119034,-5.810009,3.179316,9.536669,-7.555479,-8.247804,-5.970979,7.541478,4.257433,2.023628,-3.442772,8.504883,-5.779885,-8.747621,-8.050237,1.237691,5.965200,0.777601,0.517512,0.741406,4.884185,-3.058079,7.494598,6.440517,5.185968,-6.725285,2.025531,-3.267057,-7.393364,-0.214267,-1.136903,-7.748234,9.636637,-7.768470,4.771093,-7.977385,-1.363570,-5.891900,2.825671,-2.320833,-3.087395,-2.080653,-0.140887,0.452016,1.105171,3.392584,8.184438,4.985165,-6.894455,9.879262,-0.967658,-6.462485,-6.848192,-0.582726,3.171173,1.144092,4.548697,2.050237,-9.649425,-3.239725,-6.574422,8.612529,-7.804408,-0.450270,-4.710838,-7.159958,-3.254262,8.913643,4.838562,-3.780351,-8.470540,-0.550247,5.900844,-9.486124,-5.927271,2.149204,-8.390743,-6.849562,7.061705,3.014761,-5.023237,-9.193024,5.281025,7.853759,2.154822,1.059874,1.911799,-0.767696,9.657501,-2.217340,3.494940,5.812533,-8.117024,-8.392822,-9.604406,-0.179028,9.976651,7.248836,-0.508280,1.918899,-6.411147,-4.209900,-7.564209,-6.644718,5.695254,1.701705,-9.442792,-5.787396,-7.875362,5.334224,4.226000,0.885812,-8.714914,6.624493,-9.130938,4.541188,7.431406,-1.200082,-3.705666,1.734495,-7.796817,-6.330466,6.644346,7.073805,-2.338090,3.988784,-1.804514,-2.141663,9.245277,-0.690769,7.862861,4.916336,0.447866,-3.563001,-5.553352,9.731054,5.320352,-5.935632,-5.352781,-7.412797,-0.728083,-4.323527,9.868795,4.617680,-6.438987,-6.301873,1.717671,-7.516275,1.238676,-1.596838,2.044462,-1.915405,-3.964011,5.749179,8.232017,0.255024,7.660738,-7.317894,-5.245925,-2.986001,0.266668,-4.102577,-1.947571,4.603556,-4.324086,4.601159,6.660793,-0.172647,-0.421276,6.473208,7.440197,6.155654,-6.902830,6.581174,-9.239943,-7.413801,-1.139766,-5.864703,5.252879,5.288798,-6.778850,0.465157,-0.095408,9.028371,-1.909359,-6.081222,1.974468,-4.370749,-6.339750,-2.140874,8.062441,-0.994037,-4.597760,-7.083276,6.470879,7.459719,9.171113,9.361510,-5.894368,-9.320581,0.934637,-6.172904,2.029087,0.940063,3.647033,-9.893590,-0.959168,-0.989112,3.318027,-8.452085,-2.169965,-0.679194,8.705349,-7.554103,-5.545185,-1.063899,6.735981,-2.985015,9.849742,-8.908539,-1.319193,-7.043250,-3.820886,9.488649,3.111276,-8.810688,8.772167,8.664472,-9.634965,-2.248051,2.052807,5.033359,5.161864,7.189312,6.429475,7.066407,-9.462166,-4.696650,3.444496,-8.303372,4.058793,-0.504483,-7.495144,8.031351,5.584997,6.766538,-4.706603,-3.927468,7.734279,2.683539,5.869702,-8.084426,-9.113778,-1.223793,-9.203261,-6.472819,3.177038,-8.887297,8.413144,9.567388,3.187218,7.918252,4.329485,3.069934,3.673812,5.964662,-5.782822,-2.914828,-6.343127,-4.956339,5.005177,-1.620550,2.447539,-8.675017,9.253239,-0.544597,7.905461,-0.179665,5.154904,4.685482,-0.550931,4.045798,-0.372029,2.816685,6.520645,8.418707,0.989847,1.979111,-5.874253,2.203099,2.373736,-5.786411,6.786631,0.003942,-4.808234,2.698065,0.010021,3.216562,-4.104792,-1.746727,-0.756440,-7.674723,-8.774202,8.455073,-9.325917,-5.865366,-1.531874,-2.512227,5.545791,-8.232706,-3.287105,0.452222,-8.265613,8.764614,8.607064,-9.184500,0.025319,7.492385,2.223069,-8.898074,2.233946,6.154394,0.764066,2.648990,-4.459700,-3.599258,7.932510,-5.217695,7.848101,-6.681122,-7.647695,-2.998074,-4.711257,6.954595,-7.614518,0.938702,-9.064965,5.486523,-8.533272,-1.264174,-9.256699,7.430059,-5.571911,-2.759958,1.853564,8.106634,2.520985,5.626425,7.855634,7.615191,-6.519479,-8.791162,-0.714714,-6.278400,-5.787039,6.560854,3.368996,2.792154,-1.918308,6.661361,-4.714025,6.402231,8.426381,9.773737,0.954155,-9.527809,6.213891,-0.118378,0.028312,-7.560640,-6.372720,-7.567821,-7.728564,4.708932,8.277934,-0.912870,9.352402,-1.008144,-6.609031,-3.035809,-8.591706,9.373610,3.141594,7.297995,-5.371713,-1.128951,5.164029,9.629863,-9.657217,4.968726,8.639124,-1.468422,1.375971,9.048862,-5.644449,-9.352745,0.411457,2.195539,7.804551,4.551816,-3.640712,-1.603446,-9.331130,-5.436756,4.189611,6.939832,0.445750,9.935525,-3.232573,8.427190,-3.008419,7.406417,3.050220,-3.828434,-4.379994,3.557063,-0.491738,-5.614418,5.900526,9.717052,-2.727653,2.457088,-5.195215,2.127937,-3.279832,-6.674591,-1.312255,-2.779589,-5.951189,-4.269550,-6.400777,4.479119,-1.715603,4.350924,-3.371163,-2.677559,7.090089,5.317324,-1.456674,-8.849649,5.847962,-5.237629,1.037659,9.822504,0.853372,-0.491513,9.058382,-7.635878,5.579761,3.702921,4.609424,3.427467,-7.970268,-4.605683,6.850609,9.005043,3.779176,-1.468142,-3.804690,-8.524675,7.917059,0.105116,3.591681,-8.952672,5.119092,-4.083502,6.960889,-3.135009,-2.836290,2.164042,3.388082,-4.167978,-9.134472,4.096920,4.025075,-0.280800,-9.635170,1.644180,-5.719484,1.964852,-7.517443,-4.853718,7.219368,4.093188,0.247776,5.026600,7.719435,-5.937282,-8.296870,-1.222837,2.055339,-3.371831,-3.290039,3.261211,-0.099624,-0.650731,7.678909,-3.963384,1.245824,-6.717985,-7.804618,-3.089665,-7.376536,7.774774,-2.041747,-3.163742,7.379330,-7.776873,-1.487407,-2.374912,-4.965750,2.615732,4.371009,-6.009245,3.673596,6.411269,-3.024506,8.410048,-3.627637,1.631840,-5.322611,6.633153,-4.943069,2.386198,7.030586,7.335272,6.071960,5.672136,8.248821,5.847170,8.770631,-9.350288,-4.742151,-2.466637,0.618571,-7.021801,6.228947,7.969541,7.093197,-6.089920,-8.963078,-0.974129,2.758608,-6.264506,4.314194,1.930934,-1.146345,-0.874889,-9.366930,-2.178348,-4.097427,2.868661,-2.762885,6.193318,-2.574159,-5.046266,-9.017409,-5.913047,5.693609,-2.364912,-6.922411,0.268119,3.477729,-1.515112,-2.671597,9.547427,0.408725,-6.219680,7.217126,2.159957], dtype = "float64")#candidate|4731|(832,)|const|float64
call_4730 = relay.TupleGetItem(func_3244_call(relay.reshape(const_4731.astype('float64'), [8, 8, 13]), relay.reshape(const_4731.astype('float64'), [8, 8, 13]), ), 0)
call_4732 = relay.TupleGetItem(func_3247_call(relay.reshape(const_4731.astype('float64'), [8, 8, 13]), relay.reshape(const_4731.astype('float64'), [8, 8, 13]), ), 0)
var_4737 = relay.var("var_4737", dtype = "float64", shape = (2, 5, 7))#candidate|4737|(2, 5, 7)|var|float64
bop_4738 = relay.left_shift(uop_4709.astype('int8'), relay.reshape(var_4737.astype('int8'), relay.shape_of(uop_4709))) # shape=(2, 5, 7)
func_1577_call = mod.get_global_var('func_1577')
func_1582_call = mutated_mod.get_global_var('func_1582')
const_4752 = relay.const([9.471581,-7.033731,-6.942756,1.123643,2.101492,2.981225,9.353117,0.891670,2.969169,2.565075,5.307097,-2.936999,0.595734,4.241386,-2.114319,1.203888,5.738457,-2.890152,-7.019027,1.889600,7.329823,9.711716,3.972575,0.942262,-3.808147,2.120865,-2.523206,-2.176420,-6.259933,-3.620168,-8.150857,-6.592586,6.637578,3.656587,-3.784808,1.303877,4.337287,1.254143,8.664029,5.746512,6.424507,-7.164212,-0.008745,5.198561,-6.603499,6.328933,8.897264,-8.452909,-1.155629,-1.925425,-7.481626,-0.154094,-9.531175,-4.680705,0.941497,0.780009,3.666656,-1.166704,-7.275915,-3.342329,3.514528,2.996300,5.411688,4.087207,9.020188,-0.940048,4.597462,7.922200,-8.029147,8.417360,2.947642,-5.676538,-7.854470,-8.424413,-9.412629,2.001947,-4.181410,-5.935053], dtype = "float32")#candidate|4752|(78,)|const|float32
var_4753 = relay.var("var_4753", dtype = "int16", shape = (63,))#candidate|4753|(63,)|var|int16
call_4751 = relay.TupleGetItem(func_1577_call(relay.reshape(const_4752.astype('float32'), [13, 6, 1]), relay.reshape(call_4706.astype('uint64'), []), relay.reshape(var_4753.astype('int16'), [7, 9]), ), 1)
call_4754 = relay.TupleGetItem(func_1582_call(relay.reshape(const_4752.astype('float32'), [13, 6, 1]), relay.reshape(call_4706.astype('uint64'), []), relay.reshape(var_4753.astype('int16'), [7, 9]), ), 1)
bop_4755 = relay.greater(bop_4738.astype('bool'), relay.reshape(bop_4702.astype('bool'), relay.shape_of(bop_4738))) # shape=(2, 5, 7)
bop_4758 = relay.greater(bop_4738.astype('bool'), relay.reshape(bop_4705.astype('bool'), relay.shape_of(bop_4738))) # shape=(2, 5, 7)
uop_4766 = relay.exp(uop_4709.astype('float64')) # shape=(2, 5, 7)
func_2639_call = mod.get_global_var('func_2639')
func_2642_call = mutated_mod.get_global_var('func_2642')
const_4795 = relay.const([[False,True],[False,True],[True,False],[False,False],[True,False],[False,True],[False,False],[False,True],[False,False],[True,False],[False,False],[False,True],[False,False],[False,False],[False,True],[False,False],[True,False],[True,False],[True,True],[False,False],[True,False],[True,True],[True,False],[True,True],[False,False],[True,False],[False,True],[True,False],[True,False],[False,True],[True,False],[True,False],[True,False],[False,False],[True,False],[False,True],[True,True],[False,False],[True,True],[True,False],[True,False],[False,False],[False,False],[False,True],[False,True],[True,True],[True,False],[False,False],[True,False],[False,False],[True,False],[True,False],[False,False],[False,True],[True,True],[True,True],[True,False],[True,True],[False,True],[True,False],[False,False],[True,False],[False,True],[False,True],[False,True],[False,True],[True,True],[True,True],[True,True],[True,True],[False,False],[False,True],[False,True],[True,False],[False,False],[False,True],[False,False],[True,False],[True,True],[False,True],[False,False],[False,False],[True,True],[True,True],[False,False],[False,False],[True,False],[False,True],[True,True],[False,True],[True,False],[False,True],[False,True],[True,False],[True,True],[True,True],[True,False],[True,True],[True,True],[False,False],[True,False],[False,False],[False,False],[False,True],[True,False],[False,False],[False,True],[True,True],[False,True],[True,True],[False,False],[True,False],[False,False],[True,False],[True,True],[False,True],[True,False],[True,True],[True,True],[False,False],[True,False],[True,False],[True,False],[True,False],[True,False],[True,False],[False,False],[False,True],[True,True],[True,False],[False,True],[True,True],[True,True],[False,False],[False,False],[True,False],[False,False],[False,False],[False,True],[False,False],[True,True],[False,True],[False,False],[False,True]], dtype = "bool")#candidate|4795|(144, 2)|const|bool
call_4794 = relay.TupleGetItem(func_2639_call(relay.reshape(const_4795.astype('bool'), [3, 16, 6])), 0)
call_4796 = relay.TupleGetItem(func_2642_call(relay.reshape(const_4795.astype('bool'), [3, 16, 6])), 0)
output = relay.Tuple([call_4706,var_4707,call_4721,const_4722,call_4724,call_4730,const_4731,call_4751,const_4752,var_4753,bop_4755,uop_4766,call_4794,const_4795,])
output2 = relay.Tuple([call_4708,var_4707,call_4723,const_4722,call_4725,call_4732,const_4731,call_4754,const_4752,var_4753,bop_4758,uop_4766,call_4796,const_4795,])
func_4797 = relay.Function([var_4707,var_4737,var_4753,], output)
mod['func_4797'] = func_4797
mod = relay.transform.InferType()(mod)
var_4798 = relay.var("var_4798", dtype = "float32", shape = (240, 2))#candidate|4798|(240, 2)|var|float32
var_4799 = relay.var("var_4799", dtype = "float64", shape = (2, 5, 7))#candidate|4799|(2, 5, 7)|var|float64
var_4800 = relay.var("var_4800", dtype = "int16", shape = (63,))#candidate|4800|(63,)|var|int16
output = func_4797(var_4798,var_4799,var_4800,)
func_4801 = relay.Function([var_4798,var_4799,var_4800,], output)
mutated_mod['func_4801'] = func_4801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_4808 = relay.TupleGetItem(func_4331_call(), 1)
call_4809 = relay.TupleGetItem(func_4333_call(), 1)
const_4813 = relay.const([[[-5.047639,8.452620,0.974163,-4.173808,6.184955],[-3.652496,2.964204,7.348743,7.721151,7.498938],[7.497113,6.014979,-6.393218,-9.824220,7.149867],[6.277437,-5.751187,9.654355,-0.541037,-5.358329],[4.615599,-9.750368,-2.128608,3.850040,-1.874543]],[[6.935771,-1.262076,-7.511652,-1.962019,-9.426352],[5.382459,2.692955,-2.631209,1.206794,4.540597],[-0.220521,-9.510252,0.217432,-9.253026,4.862510],[6.467152,-8.345077,4.765999,-8.438348,3.964335],[5.629047,0.942207,3.479306,2.761832,-8.013432]],[[-7.429343,8.478970,7.738288,-9.088602,7.099916],[-6.065203,-8.487395,-7.033420,-8.508371,8.284664],[9.249117,-5.950331,-4.087316,-2.286038,-9.811716],[-6.672430,3.268292,-3.837083,-6.682823,-1.849687],[-5.246741,-6.959246,3.416366,-4.381341,-3.917702]],[[-3.969169,-2.251866,-8.009842,-0.691054,-3.801087],[8.487677,4.719689,-3.093873,6.934788,-7.906556],[-5.755627,-3.108839,-1.569138,3.225563,6.309509],[-2.842529,6.835490,-5.021929,4.380611,-7.223054],[-7.564888,-1.166020,-8.816893,1.458664,3.862623]],[[2.312657,-5.066526,6.056490,6.694732,2.377022],[-4.957327,-9.498414,-4.939889,1.046976,1.715243],[9.031868,5.984826,-4.167075,-2.176993,0.594993],[8.209895,4.911620,-8.187153,-3.677508,2.240809],[5.396144,-6.021195,1.757058,-2.198290,-6.376316]],[[-7.892144,4.890090,-3.735739,8.036663,2.543961],[-7.192645,5.041549,-4.179080,-9.745083,3.015915],[-8.346520,4.275433,0.287480,6.107195,2.669255],[6.169213,8.719390,0.446144,-5.645512,-6.167419],[3.179392,4.350179,-0.015540,6.967737,-7.140641]],[[-5.759716,5.511038,4.134313,-4.215055,-9.261045],[7.020120,9.950604,6.400104,-6.600017,0.976775],[5.503746,3.098261,9.330065,3.706384,9.553145],[-3.130600,-0.792092,2.911551,-4.500452,9.588476],[-5.300661,-3.722808,5.345580,-2.962099,-3.323723]],[[1.859242,0.549028,-8.658590,-4.053418,0.776291],[7.956350,-7.079557,7.584781,-8.694564,2.262048],[-3.943626,-8.739209,-5.313027,-8.880852,3.831083],[-9.621625,8.527721,1.989453,2.906585,9.237250],[4.642152,-9.777198,-8.637215,-8.763604,4.045504]],[[-7.408962,6.784372,-1.032292,0.023630,-9.548026],[5.872481,8.503126,-7.223361,-8.263522,-2.482384],[-0.018082,7.822851,8.058555,-3.727019,-0.175878],[-3.304297,-8.260900,7.196688,6.253197,9.014786],[6.062296,-5.414197,5.143418,2.090539,-6.461553]],[[8.577256,-5.588788,2.995880,4.775155,8.809517],[7.314922,-9.169309,8.656892,1.204707,-0.976501],[-0.653188,2.340867,-2.096881,-8.082854,4.468313],[-5.360776,6.483825,9.726531,-5.193141,4.393915],[-5.611326,2.335505,-9.552888,-4.227276,7.042304]],[[-0.047472,-7.989089,6.877467,6.955211,-3.228302],[-3.263510,6.899192,6.623332,0.244472,7.868312],[5.076192,0.617696,0.977875,0.474520,9.089288],[-6.305028,7.784971,-4.449951,-9.396369,-3.116826],[-9.743485,4.098282,-6.199379,-5.010627,-9.049048]]], dtype = "float64")#candidate|4813|(11, 5, 5)|const|float64
bop_4814 = relay.floor_divide(call_4808.astype('float32'), relay.reshape(const_4813.astype('float32'), relay.shape_of(call_4808))) # shape=(11, 5, 5)
bop_4817 = relay.floor_divide(call_4809.astype('float32'), relay.reshape(const_4813.astype('float32'), relay.shape_of(call_4809))) # shape=(11, 5, 5)
output = bop_4814
output2 = bop_4817
func_4821 = relay.Function([], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
mutated_mod['func_4821'] = func_4821
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mutated_mod.get_global_var('func_4821')
call_4822 = func_4821_call()
output = call_4822
func_4823 = relay.Function([], output)
mutated_mod['func_4823'] = func_4823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_4828 = relay.TupleGetItem(func_4317_call(), 0)
call_4829 = relay.TupleGetItem(func_4318_call(), 0)
func_418_call = mod.get_global_var('func_418')
func_421_call = mutated_mod.get_global_var('func_421')
var_4831 = relay.var("var_4831", dtype = "float64", shape = ())#candidate|4831|()|var|float64
var_4832 = relay.var("var_4832", dtype = "float64", shape = (26,))#candidate|4832|(26,)|var|float64
call_4830 = func_418_call(relay.reshape(var_4831.astype('float64'), []), relay.reshape(var_4832.astype('float64'), [2, 13, 1]), )
call_4833 = func_418_call(relay.reshape(var_4831.astype('float64'), []), relay.reshape(var_4832.astype('float64'), [2, 13, 1]), )
func_4542_call = mod.get_global_var('func_4542')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_4844 = relay.TupleGetItem(func_4542_call(), 0)
call_4845 = relay.TupleGetItem(func_4544_call(), 0)
output = relay.Tuple([call_4828,call_4830,var_4831,var_4832,call_4844,])
output2 = relay.Tuple([call_4829,call_4833,var_4831,var_4832,call_4845,])
func_4851 = relay.Function([var_4831,var_4832,], output)
mod['func_4851'] = func_4851
mod = relay.transform.InferType()(mod)
var_4852 = relay.var("var_4852", dtype = "float64", shape = ())#candidate|4852|()|var|float64
var_4853 = relay.var("var_4853", dtype = "float64", shape = (26,))#candidate|4853|(26,)|var|float64
output = func_4851(var_4852,var_4853,)
func_4854 = relay.Function([var_4852,var_4853,], output)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_4868 = func_4821_call()
call_4869 = func_4821_call()
func_4567_call = mod.get_global_var('func_4567')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_4888 = relay.TupleGetItem(func_4567_call(), 0)
call_4889 = relay.TupleGetItem(func_4568_call(), 0)
uop_4907 = relay.atan(call_4888.astype('float32')) # shape=(4, 12, 13)
uop_4909 = relay.atan(call_4889.astype('float32')) # shape=(4, 12, 13)
func_4851_call = mod.get_global_var('func_4851')
func_4854_call = mutated_mod.get_global_var('func_4854')
const_4911 = relay.const(-4.609925, dtype = "float64")#candidate|4911|()|const|float64
const_4912 = relay.const([-4.170336,-2.875805,-9.778845,5.599095,8.137413,0.056523,-9.966399,9.534011,-2.861857,-7.038520,-7.211271,-8.846285,3.485820,7.230770,8.458806,6.642304,3.757612,4.198311,-9.251764,6.874963,-1.903556,-8.502737,7.746742,-5.832880,1.776787,-3.431715], dtype = "float64")#candidate|4912|(26,)|const|float64
call_4910 = relay.TupleGetItem(func_4851_call(relay.reshape(const_4911.astype('float64'), []), relay.reshape(const_4912.astype('float64'), [26,]), ), 2)
call_4913 = relay.TupleGetItem(func_4854_call(relay.reshape(const_4911.astype('float64'), []), relay.reshape(const_4912.astype('float64'), [26,]), ), 2)
output = relay.Tuple([call_4868,uop_4907,call_4910,const_4911,const_4912,])
output2 = relay.Tuple([call_4869,uop_4909,call_4913,const_4911,const_4912,])
func_4914 = relay.Function([], output)
mod['func_4914'] = func_4914
mod = relay.transform.InferType()(mod)
mutated_mod['func_4914'] = func_4914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4914_call = mutated_mod.get_global_var('func_4914')
call_4915 = func_4914_call()
output = call_4915
func_4916 = relay.Function([], output)
mutated_mod['func_4916'] = func_4916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mod.get_global_var('func_4364')
func_4366_call = mutated_mod.get_global_var('func_4366')
call_4937 = relay.TupleGetItem(func_4364_call(), 1)
call_4938 = relay.TupleGetItem(func_4366_call(), 1)
const_4940 = relay.const([[1.047854],[-3.189991],[2.306477],[5.988293],[-7.385101],[-6.251244],[6.552267],[-2.479778],[-5.680847],[9.601239],[-3.642508],[8.064002],[8.302579],[-7.748199],[-3.256005],[-4.214770],[8.929420],[-7.571885],[3.874617],[-8.358782],[5.810935],[5.158076],[-8.576214],[8.335233],[-2.571338],[-9.137691],[-7.292558],[9.339359],[-3.868774],[-2.107153],[7.878649],[-7.547088],[1.064122],[2.430419],[4.163264],[-6.130917],[2.606017],[6.589775],[-5.626487],[-4.794887],[0.252835],[5.403843],[-3.100463],[7.134062],[-7.938789],[-9.335566],[1.810783],[-4.196297],[2.261915],[7.934226],[-7.570519],[2.849716],[7.874872],[2.764786],[-1.872790],[-9.182468],[-5.545530],[8.446267],[-9.061447],[3.108610],[-8.641055],[-4.210756],[-4.863900],[-4.852367],[-3.254553],[-5.498019],[-3.614915],[-7.833297],[-9.608500],[9.521539],[-6.998907],[6.298370],[3.918379],[6.982188],[6.127876],[-4.098836],[-3.467981],[8.748545],[-8.705330],[-4.069315],[4.965513],[7.778825],[5.035461],[1.928678],[5.191806],[-9.101872],[-6.150674],[-3.772561],[-6.680643],[8.001346],[-5.574380],[6.313020],[-5.773039],[3.327255],[-2.735825],[-2.340430],[4.304073],[0.121523],[0.135427],[-9.659668],[5.773285],[-3.092083],[-7.800839],[3.076536],[9.737099],[6.746204],[8.255231],[-6.044644],[1.464947],[-5.749801],[-3.172349],[-1.432034],[-0.752289],[-0.815563],[-0.514454],[-6.743283],[6.304168],[-0.293671],[4.326524],[-7.826275],[-9.626355],[-1.344238],[-1.053687],[-8.306530],[-5.040274],[3.082892],[8.248179],[-3.646038],[-7.154619],[1.926480],[-9.094237],[-1.493587],[6.854621],[5.164076],[8.749362],[6.334234],[8.040863],[3.660879],[-5.379248],[-9.231708],[-4.805399],[3.515498],[9.518145],[2.139077],[-4.207372],[-1.082014],[-4.425510],[-8.984478],[8.174910],[-2.646945],[7.351532],[6.916111],[5.885379],[-3.388486],[-9.360029],[-2.234843],[3.436032],[-2.589134],[-1.224573],[-6.248558],[-4.332545],[9.456591],[4.288044],[-7.450145],[8.716557],[4.845791],[-9.943004],[-8.312029],[8.473087],[-2.036994],[2.315405],[-0.610907],[-8.958887],[1.083305],[-4.014331],[-3.884061],[-8.681098],[1.612190],[7.468055],[6.605409],[-9.049696],[-6.400757],[3.800952],[-6.982974],[8.872372],[-1.174745],[-0.846262],[1.474316],[2.160176],[8.587822],[-8.248257],[-3.738842],[2.764040],[5.447555],[-0.364324],[0.861705],[9.245766],[0.141883],[-9.834672],[-7.801474],[-6.198585],[-5.980631],[6.194214],[-1.082017],[-5.423474],[7.719820],[5.795826],[-8.365096],[3.185801],[5.125974],[-6.937329],[1.190270],[-0.254889],[-2.140002],[-7.989441],[1.020609],[0.073882],[3.435951],[6.847541],[2.304690],[3.158125],[1.179212],[-1.158088],[8.034580],[1.683624],[9.907863],[-9.614263],[0.192307],[-9.179674],[5.046499],[-5.275554],[4.880912],[5.631715],[9.230688],[-4.265889],[-3.199763],[3.779625],[-7.644140],[5.782886],[7.097445],[4.094664],[-5.222257],[6.280852],[-9.831332],[3.536290],[0.568341],[-2.236123],[2.571471],[3.929199],[9.550433],[9.683857],[-3.866133],[8.626521],[6.172791],[-5.400310],[1.127567],[5.877097],[2.420968],[0.723218],[-9.511513],[-4.358543],[9.203539],[6.529444],[-2.871206],[8.384728],[-6.871178],[1.587714],[7.433243],[-3.639051],[-8.211879],[7.162829],[-0.845302],[4.026231],[-4.332755],[0.253035]], dtype = "float32")#candidate|4940|(275, 1)|const|float32
bop_4941 = relay.bitwise_or(call_4937.astype('int32'), relay.reshape(const_4940.astype('int32'), relay.shape_of(call_4937))) # shape=(275, 1)
bop_4944 = relay.bitwise_or(call_4938.astype('int32'), relay.reshape(const_4940.astype('int32'), relay.shape_of(call_4938))) # shape=(275, 1)
uop_4946 = relay.tan(call_4937.astype('float64')) # shape=(275, 1)
uop_4948 = relay.tan(call_4938.astype('float64')) # shape=(275, 1)
var_4957 = relay.var("var_4957", dtype = "float32", shape = (275, 2))#candidate|4957|(275, 2)|var|float32
bop_4958 = relay.greater_equal(const_4940.astype('bool'), var_4957.astype('bool')) # shape=(275, 2)
output = relay.Tuple([bop_4941,uop_4946,bop_4958,])
output2 = relay.Tuple([bop_4944,uop_4948,bop_4958,])
func_4962 = relay.Function([var_4957,], output)
mod['func_4962'] = func_4962
mod = relay.transform.InferType()(mod)
mutated_mod['func_4962'] = func_4962
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4963 = relay.var("var_4963", dtype = "float32", shape = (275, 2))#candidate|4963|(275, 2)|var|float32
func_4962_call = mutated_mod.get_global_var('func_4962')
call_4964 = func_4962_call(var_4963)
output = call_4964
func_4965 = relay.Function([var_4963], output)
mutated_mod['func_4965'] = func_4965
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4991 = relay.const([[[-8],[6],[-2],[4]],[[-2],[7],[-5],[-9]],[[-2],[8],[-3],[-3]],[[8],[-10],[-8],[-8]],[[7],[-8],[-2],[3]]], dtype = "int64")#candidate|4991|(5, 4, 1)|const|int64
const_4992 = relay.const([[[9,6,-6,5,2,-9,-3,-10,-3,-3,-5,-6,9],[3,4,-1,5,-9,6,7,3,5,-2,-2,3,7],[-6,-9,10,9,2,-5,7,-10,-9,3,2,2,2],[10,-1,-3,9,-6,-6,3,6,4,3,8,-10,5]],[[-10,-7,-3,8,-5,3,-3,-3,3,-8,3,2,-8],[7,1,4,-3,4,8,-9,2,-7,10,-7,-5,10],[1,-3,2,10,3,5,-3,-1,-2,3,4,-1,9],[5,-5,1,7,-6,3,-2,-8,-4,5,-3,6,1]],[[6,-2,1,9,4,-3,-4,-10,5,-3,9,3,3],[-3,1,-10,-7,4,-2,6,-10,7,-10,-1,8,-5],[3,3,5,6,-9,5,-1,-5,-1,-10,-2,7,3],[4,-3,-10,-10,-4,-8,-2,-9,2,7,4,8,9]],[[1,1,-5,7,7,-6,-2,-3,3,7,2,3,-7],[-7,8,-7,5,3,5,8,9,1,4,-2,-7,8],[-8,-1,7,2,-8,-4,-6,-1,-9,5,10,-9,-9],[-1,10,10,-10,3,-10,3,-3,-9,6,-2,-8,4]],[[2,-6,4,9,-7,-2,-9,6,-9,7,8,10,7],[-10,8,7,-7,3,10,-5,-3,6,3,1,-3,-5],[6,4,9,10,-7,-9,10,8,-6,-9,-2,-10,8],[-9,2,1,-3,-1,10,10,-10,4,3,-2,-4,7]]], dtype = "int64")#candidate|4992|(5, 4, 13)|const|int64
bop_4993 = relay.subtract(const_4991.astype('int64'), const_4992.astype('int64')) # shape=(5, 4, 13)
bop_4999 = relay.add(bop_4993.astype('uint64'), const_4991.astype('uint64')) # shape=(5, 4, 13)
func_4797_call = mod.get_global_var('func_4797')
func_4801_call = mutated_mod.get_global_var('func_4801')
var_5004 = relay.var("var_5004", dtype = "float32", shape = (480,))#candidate|5004|(480,)|var|float32
const_5005 = relay.const([[-2.614747,6.974383,-0.180824,7.072841,-8.865489],[0.623439,-9.740349,-7.995825,-6.593213,-1.733066],[0.482219,-6.571790,5.100604,1.034635,-6.452943],[-3.940142,-5.385833,9.277259,1.531409,0.623691],[-1.729471,-0.977690,1.600797,-4.926335,-8.772787],[-7.240407,6.699432,2.843130,-8.276982,8.456653],[4.624277,2.100512,9.049409,-1.095069,7.649738],[-1.576933,8.356115,8.314173,4.701252,-7.788233],[-9.173180,2.377328,0.651478,-5.007908,6.414981],[-4.373721,1.741579,-5.517908,4.520087,5.132969],[9.819525,-8.751114,7.202440,4.504556,8.318358],[-1.520478,-7.579186,-0.739255,-1.704367,4.732423],[-2.237389,-9.100941,-0.093325,-0.843776,1.061468],[-0.805677,0.472654,2.707984,-0.292100,5.559097]], dtype = "float64")#candidate|5005|(14, 5)|const|float64
var_5006 = relay.var("var_5006", dtype = "int16", shape = (63,))#candidate|5006|(63,)|var|int16
call_5003 = relay.TupleGetItem(func_4797_call(relay.reshape(var_5004.astype('float32'), [240, 2]), relay.reshape(const_5005.astype('float64'), [2, 5, 7]), relay.reshape(var_5006.astype('int16'), [63,]), ), 13)
call_5007 = relay.TupleGetItem(func_4801_call(relay.reshape(var_5004.astype('float32'), [240, 2]), relay.reshape(const_5005.astype('float64'), [2, 5, 7]), relay.reshape(var_5006.astype('int16'), [63,]), ), 13)
func_3977_call = mod.get_global_var('func_3977')
func_3980_call = mutated_mod.get_global_var('func_3980')
const_5017 = relay.const([[-3,4,3,-5,8,1,5,3,-4,-9,4,4,1,-8,1,-8,8,-4,-3,10,-2,-3,8,9,10,-1,-6,-8,-10,9,-2,-10,10,3,-2,-3,3,-1,9,7,8,6,4,2,-2,-9,-7,-7,2,-8,-5,9,6,1,10,7,-5,-3,-6,-4,5,5,2,-10,-5,9,1,8,-5,-5,6,-2,-4,1,-9,10,-10,-9,10,7,8,-7,-1,8,-3,-3,-4,3,2,-10,1,-7,9,-3,5,-6,5,4,8,6,-3,-4,5,-5,-1,8,-8,-3,2,8,6,-2,7,9,-6,-9,-3,5,10,3,-8,-1,9,-3,-2,8,-7,10,-6,1,3,10,5,-2,-7,4,9,10,-1,-8,-6,-10,-9,-6,9,-5,-7,6,10,5,-6,-1,-6,10,-5,-8,-7,1,9,8,-5,10,-10,4,-8,-7,1,9,10,3,-10,-8,1,2,9,10,5,-5,-8,-6,1,-1,3,8,-9,-1,-1,-5,-10,-4,7,10,2,6,6,6,-5,-8,5,2,-6,-5,3,1,5,2,-7,-5,-2,1,-4,5,-6,-8,8,6,-6,-3,1,4,-1,-9,3,-1,6,10,1,-9,-8,-9,-8,10,-8,-5,-9,4,-5,10,8,2,-3,1,-8,2,-9,2,-8,3,9,4,7,10,2,2,1,-1,6,10,-4,10,5,-3,8,8,6,-7,-9,-4,9,8,-8,6,-3]], dtype = "int32")#candidate|5017|(1, 273)|const|int32
call_5016 = relay.TupleGetItem(func_3977_call(relay.reshape(const_5017.astype('int32'), [7, 13, 3]), relay.reshape(const_5017.astype('int32'), [7, 13, 3]), ), 0)
call_5018 = relay.TupleGetItem(func_3980_call(relay.reshape(const_5017.astype('int32'), [7, 13, 3]), relay.reshape(const_5017.astype('int32'), [7, 13, 3]), ), 0)
func_4567_call = mod.get_global_var('func_4567')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_5022 = relay.TupleGetItem(func_4567_call(), 0)
call_5023 = relay.TupleGetItem(func_4568_call(), 0)
output = relay.Tuple([bop_4999,call_5003,var_5004,const_5005,var_5006,call_5016,const_5017,call_5022,])
output2 = relay.Tuple([bop_4999,call_5007,var_5004,const_5005,var_5006,call_5018,const_5017,call_5023,])
func_5033 = relay.Function([var_5004,var_5006,], output)
mod['func_5033'] = func_5033
mod = relay.transform.InferType()(mod)
mutated_mod['func_5033'] = func_5033
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5033_call = mutated_mod.get_global_var('func_5033')
var_5035 = relay.var("var_5035", dtype = "float32", shape = (480,))#candidate|5035|(480,)|var|float32
var_5036 = relay.var("var_5036", dtype = "int16", shape = (63,))#candidate|5036|(63,)|var|int16
call_5034 = func_5033_call(var_5035,var_5036,)
output = call_5034
func_5037 = relay.Function([var_5035,var_5036,], output)
mutated_mod['func_5037'] = func_5037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4914_call = mod.get_global_var('func_4914')
func_4916_call = mutated_mod.get_global_var('func_4916')
call_5069 = relay.TupleGetItem(func_4914_call(), 0)
call_5070 = relay.TupleGetItem(func_4916_call(), 0)
output = call_5069
output2 = call_5070
func_5102 = relay.Function([], output)
mod['func_5102'] = func_5102
mod = relay.transform.InferType()(mod)
output = func_5102()
func_5103 = relay.Function([], output)
mutated_mod['func_5103'] = func_5103
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_5157 = func_4821_call()
call_5158 = func_4821_call()
uop_5159 = relay.rsqrt(call_5157.astype('float64')) # shape=(11, 5, 5)
uop_5161 = relay.rsqrt(call_5158.astype('float64')) # shape=(11, 5, 5)
func_4962_call = mod.get_global_var('func_4962')
func_4965_call = mutated_mod.get_global_var('func_4965')
var_5173 = relay.var("var_5173", dtype = "float32", shape = (550,))#candidate|5173|(550,)|var|float32
call_5172 = relay.TupleGetItem(func_4962_call(relay.reshape(var_5173.astype('float32'), [275, 2])), 1)
call_5174 = relay.TupleGetItem(func_4965_call(relay.reshape(var_5173.astype('float32'), [275, 2])), 1)
output = relay.Tuple([uop_5159,call_5172,var_5173,])
output2 = relay.Tuple([uop_5161,call_5174,var_5173,])
func_5176 = relay.Function([var_5173,], output)
mod['func_5176'] = func_5176
mod = relay.transform.InferType()(mod)
mutated_mod['func_5176'] = func_5176
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5177 = relay.var("var_5177", dtype = "float32", shape = (550,))#candidate|5177|(550,)|var|float32
func_5176_call = mutated_mod.get_global_var('func_5176')
call_5178 = func_5176_call(var_5177)
output = call_5178
func_5179 = relay.Function([var_5177], output)
mutated_mod['func_5179'] = func_5179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_5195 = func_4821_call()
call_5196 = func_4821_call()
func_3222_call = mod.get_global_var('func_3222')
func_3225_call = mutated_mod.get_global_var('func_3225')
var_5198 = relay.var("var_5198", dtype = "float32", shape = (546,))#candidate|5198|(546,)|var|float32
call_5197 = relay.TupleGetItem(func_3222_call(relay.reshape(var_5198.astype('float32'), [6, 7, 13])), 0)
call_5199 = relay.TupleGetItem(func_3225_call(relay.reshape(var_5198.astype('float32'), [6, 7, 13])), 0)
func_4851_call = mod.get_global_var('func_4851')
func_4854_call = mutated_mod.get_global_var('func_4854')
const_5211 = relay.const(2.390534, dtype = "float64")#candidate|5211|()|const|float64
const_5212 = relay.const([-4.671833,-7.733396,-4.061396,-2.575080,0.893950,3.662738,-8.431320,-6.520754,-8.831109,-3.571677,-5.678033,1.319320,5.267711,-8.676475,-8.767177,-4.567830,7.468952,7.064782,2.854746,-4.718462,4.823738,-9.046969,-8.202778,2.147386,-8.021889,-8.289494], dtype = "float64")#candidate|5212|(26,)|const|float64
call_5210 = relay.TupleGetItem(func_4851_call(relay.reshape(const_5211.astype('float64'), []), relay.reshape(const_5212.astype('float64'), [26,]), ), 2)
call_5213 = relay.TupleGetItem(func_4854_call(relay.reshape(const_5211.astype('float64'), []), relay.reshape(const_5212.astype('float64'), [26,]), ), 2)
func_4797_call = mod.get_global_var('func_4797')
func_4801_call = mutated_mod.get_global_var('func_4801')
var_5225 = relay.var("var_5225", dtype = "float32", shape = (480,))#candidate|5225|(480,)|var|float32
var_5226 = relay.var("var_5226", dtype = "float64", shape = (7, 10))#candidate|5226|(7, 10)|var|float64
const_5227 = relay.const([-2,-6,9,-2,-1,1,2,10,3,6,1,-3,-8,-7,-3,-2,5,3,9,1,10,-2,6,-8,1,8,-10,8,3,2,10,-1,3,8,-9,4,1,-2,7,9,6,4,8,5,9,-9,3,-3,4,-8,2,-2,7,1,-6,4,6,9,9,-7,-1,-7,-6], dtype = "int16")#candidate|5227|(63,)|const|int16
call_5224 = relay.TupleGetItem(func_4797_call(relay.reshape(var_5225.astype('float32'), [240, 2]), relay.reshape(var_5226.astype('float64'), [2, 5, 7]), relay.reshape(const_5227.astype('int16'), [63,]), ), 13)
call_5228 = relay.TupleGetItem(func_4801_call(relay.reshape(var_5225.astype('float32'), [240, 2]), relay.reshape(var_5226.astype('float64'), [2, 5, 7]), relay.reshape(const_5227.astype('int16'), [63,]), ), 13)
const_5231 = relay.const([-1.213283,-9.696132,-4.321891,7.133358,-2.880568,3.358889,4.016981,-6.622480,-4.192884,7.524743,-8.583530,-0.670826,-5.888829,0.705016,2.726246,8.000516,-2.110960,2.141521,-2.084278,-3.052656,6.047890,8.876246,5.424945,2.017686,6.842550,1.757381], dtype = "float64")#candidate|5231|(26,)|const|float64
bop_5232 = relay.bitwise_xor(const_5212.astype('uint16'), relay.reshape(const_5231.astype('uint16'), relay.shape_of(const_5212))) # shape=(26,)
uop_5259 = relay.cos(const_5231.astype('float32')) # shape=(26,)
func_3977_call = mod.get_global_var('func_3977')
func_3980_call = mutated_mod.get_global_var('func_3980')
const_5266 = relay.const([3,-6,-1,3,-1,10,-3,4,-1,-1,4,-4,7,-3,9,-6,7,-7,1,8,8,5,4,-5,4,1,-1,-6,-9,9,-6,4,-9,6,3,-1,-3,-4,-6,9,6,9,7,6,-6,-7,9,8,2,-7,-5,8,7,-2,-3,-4,-4,-4,10,-8,4,9,-7,-3,-8,-6,1,2,7,10,6,9,-8,-1,-5,-7,4,-4,4,4,10,-6,5,8,1,-2,-3,-8,-3,9,8,9,-3,-7,-2,8,10,-10,3,8,5,2,-10,9,7,-3,6,-9,7,-6,6,9,-10,-2,7,9,-10,10,-1,-5,-8,5,10,-3,-1,-4,-4,4,1,9,8,2,8,9,-10,8,-3,-2,-9,10,5,-7,-8,-5,9,-9,-9,-4,-2,6,7,1,-7,3,-9,5,8,3,3,4,-1,10,3,-8,-8,6,6,-5,10,8,2,3,5,7,3,3,-4,5,6,-2,-6,2,-6,5,-7,-7,-8,1,6,3,-9,5,-7,3,-2,10,1,-9,10,-5,9,-8,-2,-10,8,10,-10,-3,5,-2,10,4,5,10,-9,2,5,-7,-10,-5,-2,6,-10,-9,-6,4,3,7,1,-3,2,-10,-7,4,-6,6,6,8,-10,2,7,1,-4,-10,-6,7,10,5,-6,5,-9,-10,2,2,-6,-7,10,5,-6,9,9,10,-3,7,3,9,-4,7,-6,9,3,5,5], dtype = "int32")#candidate|5266|(273,)|const|int32
call_5265 = relay.TupleGetItem(func_3977_call(relay.reshape(const_5266.astype('int32'), [7, 13, 3]), relay.reshape(const_5266.astype('int32'), [7, 13, 3]), ), 0)
call_5267 = relay.TupleGetItem(func_3980_call(relay.reshape(const_5266.astype('int32'), [7, 13, 3]), relay.reshape(const_5266.astype('int32'), [7, 13, 3]), ), 0)
func_2375_call = mod.get_global_var('func_2375')
func_2379_call = mutated_mod.get_global_var('func_2379')
var_5274 = relay.var("var_5274", dtype = "int32", shape = (90,))#candidate|5274|(90,)|var|int32
var_5275 = relay.var("var_5275", dtype = "int32", shape = (1170,))#candidate|5275|(1170,)|var|int32
call_5273 = relay.TupleGetItem(func_2375_call(relay.reshape(var_5274.astype('int32'), [15, 1, 6]), relay.reshape(var_5275.astype('int32'), [15, 13, 6]), relay.reshape(bop_5232.astype('float64'), [26,]), ), 5)
call_5276 = relay.TupleGetItem(func_2379_call(relay.reshape(var_5274.astype('int32'), [15, 1, 6]), relay.reshape(var_5275.astype('int32'), [15, 13, 6]), relay.reshape(bop_5232.astype('float64'), [26,]), ), 5)
output = relay.Tuple([call_5195,call_5197,var_5198,call_5210,const_5211,call_5224,var_5225,var_5226,const_5227,bop_5232,uop_5259,call_5265,const_5266,call_5273,var_5274,var_5275,])
output2 = relay.Tuple([call_5196,call_5199,var_5198,call_5213,const_5211,call_5228,var_5225,var_5226,const_5227,bop_5232,uop_5259,call_5267,const_5266,call_5276,var_5274,var_5275,])
func_5287 = relay.Function([var_5198,var_5225,var_5226,var_5274,var_5275,], output)
mod['func_5287'] = func_5287
mod = relay.transform.InferType()(mod)
mutated_mod['func_5287'] = func_5287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5287_call = mutated_mod.get_global_var('func_5287')
var_5289 = relay.var("var_5289", dtype = "float32", shape = (546,))#candidate|5289|(546,)|var|float32
var_5290 = relay.var("var_5290", dtype = "float32", shape = (480,))#candidate|5290|(480,)|var|float32
var_5291 = relay.var("var_5291", dtype = "float64", shape = (7, 10))#candidate|5291|(7, 10)|var|float64
var_5292 = relay.var("var_5292", dtype = "int32", shape = (90,))#candidate|5292|(90,)|var|int32
var_5293 = relay.var("var_5293", dtype = "int32", shape = (1170,))#candidate|5293|(1170,)|var|int32
call_5288 = func_5287_call(var_5289,var_5290,var_5291,var_5292,var_5293,)
output = call_5288
func_5294 = relay.Function([var_5289,var_5290,var_5291,var_5292,var_5293,], output)
mutated_mod['func_5294'] = func_5294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_5305 = relay.TupleGetItem(func_4317_call(), 0)
call_5306 = relay.TupleGetItem(func_4318_call(), 0)
func_1577_call = mod.get_global_var('func_1577')
func_1582_call = mutated_mod.get_global_var('func_1582')
var_5314 = relay.var("var_5314", dtype = "float32", shape = (26, 3))#candidate|5314|(26, 3)|var|float32
var_5315 = relay.var("var_5315", dtype = "uint64", shape = ())#candidate|5315|()|var|uint64
var_5316 = relay.var("var_5316", dtype = "int16", shape = (63,))#candidate|5316|(63,)|var|int16
call_5313 = relay.TupleGetItem(func_1577_call(relay.reshape(var_5314.astype('float32'), [13, 6, 1]), relay.reshape(var_5315.astype('uint64'), []), relay.reshape(var_5316.astype('int16'), [7, 9]), ), 6)
call_5317 = relay.TupleGetItem(func_1582_call(relay.reshape(var_5314.astype('float32'), [13, 6, 1]), relay.reshape(var_5315.astype('uint64'), []), relay.reshape(var_5316.astype('int16'), [7, 9]), ), 6)
func_2531_call = mod.get_global_var('func_2531')
func_2536_call = mutated_mod.get_global_var('func_2536')
const_5321 = relay.const([-3.683982,-2.577452,0.812735,5.209535,-7.788557,8.476064,-2.955425,-4.569778,-1.139914,3.900790,2.658532,-4.576184,3.910398,-7.229688,-8.469840,8.289451,4.582667,1.478201,3.584118,-3.125664,-2.079330,-3.708129,-7.712116,7.683241,-8.336921,-3.914537,3.549414,6.070042,-9.483602,2.060763,4.486934,1.699646,-9.465540,6.141558,-6.195733,6.977217,0.187060,8.364860,0.774491,-4.330222,-7.150745,4.309703,-1.206878,-0.863514,-3.271636,6.962667,-3.900311,-0.670553,5.220433,-6.674156,9.853005,-6.975481,-3.292498,3.292914,-0.160560,4.453468,-2.008596,-0.059483,1.639880,-1.203311,-4.587148,5.434754,-2.695128,2.623369,3.174036,4.787224,8.801089,-3.540414,-4.522350,1.777827,0.795322,1.608753,8.677965,-0.758318,-5.012147,-8.776267,-6.482819,4.902406,7.256265,-1.137875,-9.287250,-8.389299,7.357450,1.867064,-8.106626,-8.379602,9.674705,0.526352,6.725217,8.846764,-6.916966,-1.077844,3.343973,-9.992568,-1.692964,-1.835186,-3.677345,4.731579,7.856952,6.789327,6.004465,5.416540,6.924631,-5.127405,7.597745,-4.932547,8.242935,-2.326999,-0.434522,-5.264172,-9.636783,-6.707410,3.241842,-0.518945,-1.762321,-6.830924,-3.598909,9.275753,-8.316964,-2.652575,6.471028,-8.191040,-8.825952,-4.919497,4.777473,8.608050,0.346020,-5.694692,9.541336,4.805520,0.905690,-2.742353,4.398532,3.255908,9.588015,1.118850,4.824030,2.997436,4.582152,-2.981105,-2.022999,-1.468262,7.573911,-1.961959,3.851131,4.211431,0.231751,-3.290973,3.285312,0.051140,-8.532937,9.905465,-6.123969,3.991941,-0.322113,-3.870526,4.749362,-4.882881,3.782506,-5.989334,-2.940672,3.472669,8.396294,6.416043,-7.888172,0.704998,6.502248,-1.902523,4.137501,0.548023,2.845425,1.588379,-0.959498,-5.758026,-9.877570,1.197747,-9.138410,5.549685,-7.472435,-5.555318,7.636941,3.456279,-4.798197,-0.317708,3.650017,-2.880858,9.546288,-6.732009,6.790087,8.745030,0.328837,9.067799,-1.254149,4.786989,1.138056,0.670234,9.020231,8.539037,-4.274916,1.298691,-9.113098,-0.041956,0.251619,3.285807,0.018936,6.803461,7.384427,-3.891181,5.616329,4.980172,7.407346,3.178937,2.570200,1.109522,-7.473369,-1.715544,-5.699955,-4.840391,0.999796,-7.043254,-1.899297,8.644837,-4.514918,1.959363,1.184550,-7.768154,7.650468,3.569197,4.344530,-5.901976,3.667399,-9.924832,-4.306600,-5.172908,-6.027640,-2.503936,-9.400204,1.630194,-0.098007,-5.256490,9.667910,-4.491736,-4.176221,9.608269,-7.044840,6.343704,-7.666229,8.309817,-8.944146,-2.060265,4.985643,9.233716,-1.031634,-7.318060,-7.077852,-0.292569,-0.861899,-4.017655,-0.726613,-9.368675,-5.473336,6.249669,8.118254,1.477117,-0.201912,-7.556319,-9.356635,3.723817,-4.541222,5.928001,-3.915323,-6.909943,0.435595,2.462300,2.941922,-0.049760,4.233163,-6.478311,4.998016,-2.701119,-0.105027,0.106126,-7.388525,6.829826,-4.004630,0.226018,8.783305,4.784215,7.734871,-1.592108,-2.406321,-3.577136,-6.709969,-9.991079,-7.366116,8.204331,-0.324960,8.757233,8.145192,4.646228,-3.780494,-9.498318,8.090658,-3.050268,-0.826711,5.292034,0.169401,-4.210076,-0.856408,3.264956,8.955894,9.194622,7.900464,6.797523,-5.363474,9.527453,5.734417,-7.287573,6.314724,6.015349,5.849085,8.693613,-1.822453,5.476974,-3.804346,6.611803,3.603674,8.596472,-5.110073,-4.174591,-1.704371,2.018462,1.049173,-7.531837,-8.420178,4.115166,-4.591064,-2.281807,-2.313075,2.640407,8.379014,4.503459,-8.738780,8.076797,7.946354,5.273246,8.512174,1.012843,-1.157885,-2.967838,-1.381129,-5.577799,-2.368263,6.584534,-1.636917,2.443736,-3.476909,3.361731,-6.738079,8.263308,-1.444906,0.100098,8.844803,-8.825534,-9.745710,-3.296262,-7.277860,9.510300,0.852663,-1.789813,2.847836,1.012348,-5.238767,-6.929049,-4.435513,-1.322835,-0.522506,-0.975054,-1.476071,2.813216,6.000686,6.596671,0.148043,-7.292045,-8.175519,-3.129128,4.037086,5.252937,-6.681369,-0.529810,6.802421,6.701314,-9.263499,4.754409,9.410312,8.821020,-8.939073,-9.398357,0.900523,-3.680043,0.802778,5.764064,0.934042,-9.895634,6.989597,-1.976493,2.008903,-2.835711,6.335576,2.266692,8.545020,-7.379951,2.504400,5.514791,5.048687,-4.898750,-2.314524,4.813354,-4.773674,-4.219372,-7.935314,-9.424921,-8.941805,9.318622,-7.760642,-0.602487,2.682369,5.864953,-6.096739,3.101814,6.784326,-7.402212,-8.945637,7.705538,-1.207303,-8.264729,-9.135269,-1.468389,1.008918,-4.758215,-4.188393,7.621452,3.169233,8.831863,8.303826,-6.387340,-8.894195,1.938728,-9.851292,-0.100924,-9.764922,-1.000188,3.473649,7.520262,-9.853891,5.926675,2.261199,7.255988,5.807523,-9.655750,6.950744,8.081692,7.704069,-0.759833,3.320118,-5.881594,9.866108,-9.210443,-5.861423,-8.199177,-0.284576,7.631887,-2.981860,-6.112351,6.910638,8.414936,1.593978,5.155177,2.390988,6.518849,-6.834391,-7.824487,-3.256305,-1.451359,-7.469476,1.282722,-3.040653,-9.657649,6.014227,5.555985,8.762514,-7.781008,7.600971,-8.730342,7.956711,-0.647073,5.951004,-9.413788,4.152550,-1.699105,9.391223,-8.231989,2.622522,-6.479298,-0.967275,2.179022,-6.759663,-6.138851,9.876439,-8.467273,-1.581200,-5.702390,8.509194,6.312743,-0.156570,8.561557,-9.497827,1.571511,-9.374321,-6.293146,6.641937,4.849693,6.653243,-3.825317,-3.535868,-9.194785,5.131160,-8.766434,9.549008,4.849519,-7.658228,9.492947,0.791927,-7.399208,-1.257965,-2.123177,-0.087539,-8.077994,5.524767,2.884652,7.905334,2.782424,-0.511994,-8.731233,4.864442,0.377119,-1.205377,-8.141707,-1.043174,9.112194,-9.458971,-4.307929,2.012045,-8.373147,0.510313,-9.312063,1.809565,4.981145,-2.856233,4.615964,-9.273661,9.532157,3.266837,-5.085244,-7.604809,9.674189,2.210671,1.056986,-8.421283,7.522748,0.396442,-0.667661,2.063338,4.110311,0.529198,-2.702518,8.706844,-0.791176,6.817723,-3.575362,3.523962,-3.258713,-0.061424,5.919659,-8.275746,-8.432767,6.827136,-8.848787,8.790605,-9.143155,8.932420,-4.814252,-6.592203,6.158765,5.961487,5.384603,3.661865,3.506655,1.516351,-5.482079,2.319027,-5.877347,-1.279290,-3.012329,-8.263820,-6.980941,6.931414,-0.426846,-6.017990,7.704626,-7.931531,-5.678089,4.366767,5.457866,-1.971546,-8.448789,-0.978954,-9.395042,8.410154,-1.483363,3.930638,0.876827,6.530417,-8.035424,-3.641830,7.875176,-3.726757,-7.869430,0.672626,8.752705,-0.808586,-2.969114,-6.602077,2.921427,0.107439,4.427531,-8.347739,7.007432,-2.311501,5.027358,4.490404,4.191557,-7.846011,1.837123,7.819481,-5.926487,-2.631660,0.093675,7.919264,6.631861,-0.633442,-7.513549,7.165094,8.671925,7.384218,-2.916085,8.773784,6.272326,-9.606199,-5.076921,3.776604,8.932904,0.225780,-3.360060,7.102367,9.755884,-1.423135,-1.211499,1.522484,7.240160,7.609652,8.036947,-6.172768,-1.515761,-5.612538,-9.624487,5.302617,0.782586,-5.645837,-1.220219,9.993372,-0.882910,4.345916,-8.567697,-9.019271,7.558429,2.730037,-8.193675,7.046230,-5.663361,7.566236,5.431533,-3.415857,9.634277,-0.324809,-3.964868,2.624088,2.693849,-7.557720,0.757410,-0.201036,-4.553631,-7.133591,5.007835,4.064979,6.750464,-6.327511,-8.341709,8.565023,-7.301435,9.119372,-4.551942,4.580474,8.720038,1.389270,-3.088412,8.486004,5.920531,7.051142,-9.807602,8.830088,-2.898071,-4.522377,-5.714199,-5.656508,-2.890882,-9.637551,6.149535,-9.030019,1.697391,3.384427,9.329792,-7.771448,-0.147019,4.191666,-6.762384,-0.096924,5.309545,9.181964,5.003613,-2.557780,8.392387,-9.464020,-0.892608,7.903723,-5.605912,5.035265,-2.438609,-8.945446,8.740678,5.691733,-6.075444,-6.219296,-2.528197,-3.350205,-6.612664,9.013811,8.167190,-5.192884,6.199025,6.063849,-6.061018,2.801713,-5.009571,-9.524944,-4.036134,9.994439,3.194509,-8.137868,-7.502693,8.786212,6.979545,-3.067205,-3.417407,-2.472728,0.320923,1.883184,-6.769462,-5.081575,4.471428,-1.126363,-3.955324,-7.812746,-4.856338,7.404650,5.138264,7.147435,-0.052652,9.736867,-8.477220,-0.844268,1.786550,0.484671,-3.608527,-7.865135,-6.717041,8.288027,3.458294,1.177981,-6.363108,-7.963762,1.107072,-1.051780,1.059169,6.590595,0.237058,6.273173,2.435518,-7.117662,-9.647527,1.835334,-3.422817,1.123116,6.809345,9.585923,-4.279135,3.785357,9.510818,2.604782,-9.192409,-5.279418,-8.860695,-7.677931,-1.489810,3.866051,-4.189038,-2.283523,-4.867652,-7.635756,-8.167447,8.330361,6.080742,-5.212405,4.042589,1.756880,-2.860528,5.472066,-7.347447,6.260128,5.725578,4.054240,3.384922,-7.988460,-8.836651,4.092578,-4.093041,7.123862,-3.935663,-5.101807,8.313544,7.114049,7.687565,-6.871545,-6.504036,-1.552752,-7.061295,9.937021,8.967894,8.273335,-8.764897,-0.930496,-2.864755,-3.950165,-4.091010,-5.461969,0.382386,4.788342,-5.567600,-6.570465,2.211727,-0.129396,-3.633060,-4.518803,9.343357,0.925109,-5.597043,-7.512734,6.424616,2.139179,5.792663,0.897720,7.846998,0.781328,-9.250982,1.970015,1.601616,-3.020558,4.844476,9.637617,-8.901313,6.852182,4.522156,3.375761,-9.721731,-0.766341,-9.393420,-6.051278,-6.725166,-3.036467,1.266247,6.383770,5.658071,9.664767,-2.900611,-9.342088,1.612059,3.116855,8.169310,-3.286921,-5.132959,-6.695363,-1.796003,-9.986296,-3.596276,-2.580806,-4.391431,-3.042373,9.786680,2.332462,9.139389,-4.117419,7.576927,5.512407,0.101742,-1.209290,-4.265000,-6.622161,-3.089305,8.507397,0.481255,-3.925177,3.621988,-3.493779,-8.934209,-8.497269,9.808576,6.619370,8.807103,4.614752,-0.125499,-5.592287,-7.760534,6.953318,1.341403,-9.644658,-3.479411,1.336622,0.642064,-1.307710,8.297440,0.334722,-3.391503,1.020079,7.095347,-3.975979,-2.865229,-8.323197,3.080425,4.797199,6.704807,-9.058335,8.380112,6.149316,6.791785,-2.375182,1.489947,4.356998,-6.318784,9.827526,8.553264,5.566535,-5.332793,0.817291,-0.773913,-3.294097,-8.555267,0.683381,-2.938851,-9.280062,8.517251,-9.730169,2.333895,-1.625889,-3.948002,1.584959,2.182967,-3.023149,6.931965,1.003536,-8.693704,2.778797,-0.259861,-1.144472,7.482143,-8.014880,-7.307402,3.870786,-1.026642,3.219450,5.459604,4.008155,-3.004141,-3.394713,7.221041,9.199221,-1.710154,-8.184050,9.820183,7.342555,5.645795,7.073364,0.761344,4.413281,-0.398175,-2.927584,-4.663375,-4.053390,5.565151,-0.075200,4.206642,8.386405,-7.292614,-0.238026,-5.539285,-3.326090,-9.350894,5.614545,6.211415,6.120913,-5.385682,2.656471,4.140331,6.641149,6.500107,5.010036,2.836049,-2.153588,-1.112863,1.327719,-1.122148,0.481407,-8.416860,-6.589452,2.891570,8.236911,-3.150925,-2.856608,3.227741,-1.920484,1.943555,5.179420,-6.380850,-1.656094,-2.417216,-0.864058,-2.915973,0.954596,-9.905681,-8.499018,-7.121048,5.860276,-4.008621,-9.668610,7.498712,-4.338835,9.097856,5.305114,0.998833,-8.697068,-8.303473,7.755374,-6.862466,1.417087,-6.965765,6.931259,7.276211,3.852733,-7.232953,6.780472,6.057809,3.986972,1.388217,-1.010972,-8.276796,5.619442,3.066193,0.922983,0.348132,0.568571,-0.086054,-0.633758,8.851080,-8.552536,-8.025461,-9.424238,8.146949,-2.305996,-6.571850,-1.042794,5.664082,1.855155,-5.003423,2.271528,5.977671,3.470915,8.435080,-0.610006,-7.982343,-1.743590,-4.863757,-6.783847,-6.943615,3.250880,5.925881,-7.240998,0.588318,-9.825748,-1.618373,7.462228,-3.338921,-3.010888,0.742972,-0.452266,5.190807,-3.661454,8.087996,9.508153,4.368574,8.815689,-6.363738,6.148698,5.753771,9.884980,2.779421,-1.825644,-5.927299,9.419536,0.304193,5.340358,4.152342,-5.876269,-5.840824,-6.813456,-5.220415,-5.249556,8.621424,-8.109001,4.047394,0.775041,2.686235,-1.173695,-6.833854,3.088581,-9.230627,-3.271622,-2.812874,-6.516291,-4.591169,-0.852715,-4.089418,-0.961848,-7.169330,3.706868,-6.624997,6.732088,-0.558004,5.794450,7.274114,-1.450818,4.795543,8.520490,4.605993,-7.075275,9.165955,8.089125,-4.915195,5.015988,-2.647841,-2.921688,8.002885,-1.459133,-6.756159,-0.867858,-6.866896,2.584649,3.541067,3.202840,-1.757821,3.942566,-7.421954,-1.011362,-3.812728,-8.157631,-4.387410,8.574258,-8.593202,7.566257,-6.173753,-3.901895,-6.482971,-9.915039,6.813922,-1.959042,-0.250265,6.867891,-1.090017,2.064731,7.872632,-0.403596,-3.538634,-9.951245,6.261645,4.726407,1.603802,1.540666,5.101334,-5.053854,7.583075,5.436531,-1.795945,7.511478,-5.777438,6.723122,-7.162747,7.579516,8.909360,1.147257,7.336476,-1.277005,-7.330119,-6.117499,-0.670906,-3.601849,9.348388,1.939109,-7.164184,6.133892,4.329826,5.761491,-0.408452,-9.367744,-0.462202,-6.548855,6.285838,-7.133475,-6.478641,6.507447,7.031791,2.330895,1.526203,-6.703439,2.253894,-0.435572,-1.635645,-3.589018,-5.977698,9.432741,-0.279163,-6.118030,-0.069740,6.324121,2.912872,0.226134,4.245938,-0.605515,7.350657,-0.224960,-9.210651,4.364572,-4.487119,3.926518,0.362411,9.353465,-2.168520,2.262068,0.208685,-1.732091,4.900499,3.109212,-0.575295,-8.757004,5.527695,-8.917736,1.702724,-3.390291,5.732372,5.097484,-8.062667,-7.983846,-3.312290,-0.981637,-4.748441,3.300968,-4.220954,-4.646241,-9.111752,5.952950,-8.634307,1.236681,7.244953,8.840026,0.241995,7.715281,-4.039990,-4.986813,5.141624,-4.316011,9.856734,-5.340623,-8.886210,-9.555677,7.368473,-1.847341,1.301233,7.601950,-9.477132,3.011814,1.701960,8.997505,-7.475609,1.262706,-6.255227,-5.299455,2.681998,-3.162346,6.647544,-8.196520,-8.467322,-8.379434,-5.321371,-8.684785,2.754800,-2.514932,4.284299,-6.937493,6.320971,1.448576,1.992594,-8.030528,-8.367767,-4.198257,2.413704,-6.844322,-5.676216,-7.096313,0.289024,8.487502,-7.499401,4.359708,9.561994,-6.747952,1.500859,1.123791,6.250631,1.376870,-5.021099,4.629752,-3.896200,3.629389,1.121335,0.483180,-1.159849,0.371300,-5.244240,-5.530107,-4.794391,8.949972,0.333211,-5.805693,-4.837928,-6.137308,8.841820,-8.520183,-2.313837,-8.304686,4.297269,-7.139060,-1.142693,2.845194,-3.602090,9.225876,-2.673235,5.087796,7.064321,-3.841887,1.231407,-9.763886,-8.262413,4.598822,-9.703761,-4.476919,0.432827,8.275757,-0.888256,2.873104,3.657233,9.039282,4.224739,0.548304,-4.139617,-0.498323,-0.466031,7.974474,6.465726,6.626795,-2.297335,-4.582887,-2.027471,-7.833906,-2.165151,-5.119459,-8.587673,4.567918,-2.249583,-8.783822,-1.537460,-2.793605,1.722164,2.130439,-6.057193,-7.003045,9.217953,2.937795,-7.121211,-1.394973,4.614934,-9.345325,3.197905,8.234317,-4.077264,-8.488446,-9.361972,-7.995350,-7.831260,-4.384963,-3.839538,-2.261521,5.011773,-8.601249,1.754039,-9.995973,7.382019,-5.715445,-9.561541,-1.932954,8.201268,9.518954,2.302274,7.867924,-7.661214,5.261209,-5.025966,-9.466735,4.398557,2.194470,2.085969,4.421363,3.798498,8.354212,1.402445,-8.013133,8.406271,-1.932110,9.867545,-3.741263,9.332671,1.695752,6.776832,-5.731555,-1.902987,7.250851,8.551440,-8.825572,-0.750332,9.382450,0.402490,-4.391438,2.465590,4.880175,-5.879891,-2.997298,3.833254,0.205321,0.626065,9.970425,-6.970300,-8.124665,5.874606,-9.174956,-9.189747,4.229248,2.241364,-0.910858,-9.341087,-0.169961,-7.938501,1.363733,-4.062559,-2.679538,-3.624761,9.093147,2.227576,-2.946378,-9.361087,-9.293204,-8.389494,-2.998478,-0.284378,9.817069,-5.720842,2.721184,-9.006250,7.312224,-1.664177,2.643270,2.373079,7.134137,-8.518448,-7.273004,-6.860647,1.490503,-8.566587,-4.977710,7.914975,-9.457202,2.541317,-2.417795,-2.553294,-7.799370,6.331969,8.412502,-4.696617,4.686338,-9.757091,1.019301,5.590919,-5.785657,-2.090827,-8.105659,-3.732010,-6.407789,-5.735268,2.628871,-0.628672,2.735032,6.268718,-0.237973,9.456294,-7.620132,8.300936,-4.134862,6.234730,3.245574,-2.639045,4.693553,-7.544899,-4.086597,-3.669353,3.783371,-3.928743,-7.590526,2.212028,2.386774,8.932492,-0.395374,-3.798845,9.327750,6.323684,7.606524,-6.094035,-2.656996,-5.071517,4.648417,0.302148,2.350646,-4.965131,0.553809,7.641714,-7.391241,6.219205,4.403672,-4.397366,2.813016,4.409536,5.738784,7.315810,-0.456227,-2.901890,-8.621060,-1.719286,2.355889,7.633606,-8.913352,-5.451240,7.688500,-5.837834,9.485383,9.270383,-5.250786,8.520592,-1.904429,-1.874183,7.842900,5.668296,-9.762932,5.500905,-5.019137,-3.366904,9.906491,3.365874,-5.793903,-3.634020,-3.235869,-9.247805,-0.205370,-5.090689,-8.328962,-6.867129,-8.729754,1.648877,4.262540,-4.445495,-7.988308,3.690999,8.105516,-7.184363,-5.921056,7.764030,6.447708,6.352745,-8.058905,-0.725005,-7.073986,-9.759708,-8.873733,4.804097,-9.651346,3.123138,5.279277,9.113480,-5.263209,-6.422049,-4.884374,8.125173,-5.258075,3.854529,8.113828,5.429134,-2.101376,-2.581840,-9.979868,9.485933,0.163872,3.229983,3.805215,-6.357818,-2.822066,-5.840854,-4.019133,-0.948875,-5.899652,6.145298,-7.810225,-2.755237,-0.325489,0.002305,-0.920321,-5.973902,-5.530032,-4.110608,-7.276672,9.930422,-7.463753,4.793830,0.764670,7.664996,9.461521,9.642109,4.140997,9.600374,-4.592158,-6.794985,6.463564,4.882603,-0.280405,0.169412,-5.655783,-3.727914,-2.522979,0.386019,1.734298,1.868088,-7.979754,-9.778166,-1.417541,9.796262,9.827541,-2.694962,-9.189146,-0.867987,2.507529,7.042112,-2.091023,-2.504549,9.644612,-4.929901,-3.625844,-3.901747,2.827172,2.595974,-4.539382,-1.040623,-7.005793,-8.349186,-7.856584,-7.828351,-1.113251,8.510246,9.783997,9.699766,-9.404007,4.199605,7.438739,1.300243,0.067537,6.645045,9.853760,7.724198,-8.909933,2.924712,-1.516514,-2.007008,4.527366,0.593248,-2.369816,-9.325276,-7.601461,3.589432,9.095766,-9.027707,7.415746,-7.567292,-5.808097,8.281270,8.211846,6.596425,-1.785985,-4.468379,-6.487010,-9.423099,-6.707969,6.584311,-3.227581,-8.653618,8.837275,-1.086841,-9.702249,2.551805,-9.058123,0.923283,1.199181,6.275007,8.888840,-2.608441,8.016599,-6.908700,6.252125,2.769646,-2.750748,6.146266,-6.434404,5.447178,-4.244345,2.028944,0.640975,-4.708875,-5.393634,-2.645535,4.730897,0.067211,5.744678,-7.629526,9.604035,-4.433046,6.796752,9.700438,-1.235616,4.247943,7.177396,5.186156,9.470649,-9.364217,-2.457091,6.775396,1.651092,-8.602873,-6.539982,7.014729,-9.748346,-2.089876,4.163429,-1.044589,-0.669562,-8.497368,-6.942068,-2.230391,3.146644,9.457687,8.945087,6.265063,0.814829,7.297253,-4.857490,2.785007,-1.089552,-0.169164,9.864844,5.461427,-3.442992,-5.893886,-1.718504,3.297145,5.633953,2.746371,4.673924,3.990365,-0.623234,3.925330,7.151077,-0.087843,-7.884145,9.543476,5.281752,9.832056,-1.340707,-1.869597,-4.070316,-9.875540,8.610427,-7.585803,-4.272823,7.573892,-0.818489,4.423553,-4.799334,2.324713,-9.149737,-8.837706,-6.019886,-0.794543,4.638038,2.804495,-3.065262,5.278940,2.933701,-8.072100,8.706440,-3.623969,-2.359459,1.992956,5.370408,7.269513,8.534429,9.648235,2.670654,-5.141856,9.472099,-8.214433,9.793388,6.938771,7.072728,-4.791780,0.019788,-5.873622,-4.997107,-9.830517,4.826097,-5.970559,-2.376390,-7.406598,0.346988,-2.302076,-1.598587,-1.878005,0.485382,-9.062904,4.067242,2.967215,6.211737,8.303120,-0.087755,-3.921886,7.197687,-0.891752,-8.894992,-9.377401,-3.131283,-8.934291,7.307445,-0.843024,-5.155707,-6.356865,-8.292611,2.114697,7.158027,3.617695,-4.181636,1.523971,-4.124525,1.620286,-8.846548,-2.973818,7.363683,8.117629,0.003762,8.517211,-0.681650,-2.619514,9.778007,4.609544,-8.678464,-8.626282,-1.960806,-3.056436,-4.356713,0.237688,8.307103,4.099296,8.652084,-0.246989,-6.270581,-8.349156,5.187672,7.339760,-2.391018,9.301091,-4.504009,-7.179646,-7.835867,8.259617,-7.343109,6.473525,6.013419,-9.375553,-7.129817,0.371739,-2.770205,7.442785,-9.147196,5.193399,1.087224,4.194746,-0.540721,-7.653708,1.570675,6.792329,8.147324,7.627005,7.141357,8.061823,-2.903295,8.158622,-9.616617,-3.485326,2.021336,-4.388773,9.073964,-7.570416,7.835844,-2.597313,2.958956,-5.353923,-7.399563,5.065918,-8.575076,1.168353,6.832954,1.378918,-4.587625,5.075643,3.606987,-7.168864,4.960602,0.914891,-4.661034,6.802033,3.623069,-7.295026,-2.469530,-5.524455,-6.143009,3.848451,-0.554918,5.087283,5.904082,-9.578176,-0.411231,7.864380,-7.677559,-2.215820,-0.097211,-6.689658,-0.111292,4.841304,-9.001911,4.035732,-6.028708,-7.758025,9.276412,3.655909,-4.248796,-3.024273,-8.057337,7.651631,-9.520049,5.290187,4.393085,-5.199509,-7.452035,-1.370916,5.349255,5.983387,8.031435,-2.431980,-0.270315,0.415664,-8.558893,1.191086,5.552720,3.632818,3.955315,-7.308626,-3.600177,-9.667632,-7.555144,0.401082,-9.327372,7.044606,-5.334700,-6.955980,2.230843,-9.120120,7.105347,4.802431,-7.217265,-3.434457,3.831240,-1.335367,-5.468739,1.734540,-2.474032,-8.014573,0.725690,-2.676027,-1.015779,-5.136677,-4.432145,0.761737,4.533925,-0.699482,8.883713,5.329648,0.416262,-0.838623,-5.780986,-9.472168,-1.645158,5.330890,4.307579,2.812980,-0.108018,7.834582,-8.476283,3.310222,2.715023,3.927044,-7.514648,-4.625579,4.615798,1.329641,-0.833676,-0.771272,8.371254,-8.359155,3.254061,-0.639263,-8.426254,-6.321446,-6.605308,-5.663618,3.794953,-9.071494,-3.898544,7.495179,9.025445,7.192926,-1.591199,-5.495638,7.924627,-7.618836,-8.999685,-0.925560,1.269271,-5.805349,-7.465881,2.635233,-5.098043,-1.409264,-8.533812,-2.091002,-3.912680,9.169598,6.806215,-2.458699,5.705742,9.947373,6.977600,-1.380981,-0.297332,-7.008187,2.177758,-8.104415,5.932407,-8.090274,-9.926184,2.706562,-2.709687,-2.823961,-5.843887,-0.626753,3.685395,-8.064656,6.784530,4.537193,0.607098,5.452261,-6.671370,-6.394731,-3.158265,3.241039,-8.504423,4.320123,-6.299535,-2.913128,2.666428,-9.072599,0.843443,2.642855,5.808387,-5.774371,9.837821,1.270771,-8.779207,9.059138,-6.003866,1.985024,-5.826225,8.449285,-1.721296,7.151913,-1.282234,3.663301,-8.174534,-4.581547,7.230519,-4.740697,-7.617815,-8.402206,-8.222358,5.803102,0.055500,7.243790,-5.420482,-4.561582,-4.771130,-5.275458,5.672646,-7.724024,-2.124132,7.807015,-4.867212,-8.594712,4.576867,2.339251,2.523711,-0.978614,5.177416,-8.722821,-0.613193,6.639654,-7.542251,9.395568,4.196706,-9.902093,-2.974496,8.271210,4.281882,-8.975281,0.637998,-4.404780,-1.521772,5.074580,-4.101186,0.271118,-8.998348,-6.117422,-6.046786,-5.133999,0.122360,-3.602870,-8.832998,-7.673373,9.798138,-8.369209,-5.133782,5.813834,6.958701,7.792313,-3.719600,-8.986122,0.768940,-2.307796,-8.752572,7.531578,3.840111,5.333117,1.775168,3.041165,-1.195892,4.627858,1.280136,-1.965961,1.493442,-1.041335,-6.915049,-6.673161,5.643542,-3.952394,6.077025,-6.724909,5.049440,-4.238246,0.726119,0.241998,5.422851,6.672889,-9.838972,7.691597,9.992812,1.924399,-3.206971,0.812279,-5.162794,0.319935,4.277252,-8.265915,-9.365561,6.378007,8.246940,5.806617,-6.058438,7.344889,-5.069373,-8.305536,-1.618620,-7.473657,-3.155580,0.643260,8.234070,-2.231554,-7.828065,8.431584,-3.226989,-6.259446,6.797566,-0.883539,-9.351151,-8.469866,6.476964,-0.221131,3.094617,-1.729778,-9.486478,-9.435271,8.363066,-2.809997,-3.720859,-8.192348,0.542162,-5.029120,-9.637338,-1.737125,-7.070582,-3.934749,4.491966,3.132758,2.646627,-7.954468,7.161741,2.822087,-6.572961,-8.076703,1.562543,6.148371,-4.455223,9.594736,-9.353999,8.515193,5.094678,-8.237891,9.973961,7.795738,-4.190145,-1.654372,-5.895112,-2.537856,-1.819422,0.935030,0.328360,-0.896394,-9.018602,-0.818531,8.427146,5.292135,9.238709,8.210670,-2.874260,6.443711,0.332732,-5.424979,1.554963,-6.048805,-3.012828,3.819995,-6.683820,7.650136,-3.607181,0.444871,2.678107,-2.095608,1.990771,3.409994,-9.243640,-2.503834,7.810826,9.008970,1.527085,-1.206354,-8.287711,6.691516,0.743967,8.082762,-3.386098,3.085417,-4.426067,2.346300,8.281214,5.604728,1.544785,5.745136,-7.908648,-3.690951,-7.550230,4.011241,-4.045133,6.225111,3.022567,6.051220,-2.925343,-6.311655,-7.349840,-9.640494,-2.866115,0.680570,0.765929,-9.197307,-2.024230,3.738404,3.157477,2.053311,6.716967,0.575294,4.409135,-8.882752,1.498324,-8.841809,-9.962496,-8.898356,-5.858263,7.491451,-5.537903,-4.476070,-1.181333,-0.086296,-1.580056,6.339651,-9.318636,4.847828,-8.781453,7.222549,-1.001456,3.638810,-0.978713,9.409481,-6.207345,-0.553722,0.677607,3.289312,-1.637216,8.410475,0.036237,-2.628211,-2.782951,5.033278,-0.056738,-3.148211,7.359745,4.779128,6.473534,-5.271496,6.764825,9.118686,1.374027,-3.181646,-0.310234,1.349672,5.228116,1.964969,1.985716,-1.509303,-3.480159,-2.441550,-1.341060,2.284643,-7.002606,5.425043,9.385252,-0.500047,4.353010,-8.831547,4.098725,1.626902,-5.085534,-3.884723,-0.657494,1.272612,4.949085,-9.955206,8.934688,-7.009148,3.353806,-4.829923,-7.948219,-9.737283,2.957498,0.189898,-7.890356,1.183509,9.930851,-6.156026,-1.233203,-0.418147,9.027631,-0.043319,2.570634,-3.778485,-1.207391,1.827017,-5.647207,7.117695,-8.592146,-3.387976,5.094334,4.064835,6.321042,-8.818276,5.083344,0.074647,1.609814,-3.424609,-4.724814,-1.941811,5.248733,9.188582,7.952200,2.066184,2.300481,-9.789960,-6.607294,-7.416152,8.136096,3.389644,4.039830,8.350922,-0.564753,7.795052,-2.694784,-1.930929,8.909536,4.301495,-7.877209,0.829809,-8.584470,-5.109182,7.569683,-3.978247,-9.086478,-8.908969,4.197279,-4.028358,3.539385,-6.668891,3.008149,4.385401,6.806659,7.814507,4.590736,8.725489,-0.141318,-4.816409,-7.196526,-6.945367,2.621971,9.794319,-1.679920,-7.180000,3.331027,-3.755960,9.865421,-4.992241,-9.837693,-6.088291,-0.405237,-5.532359,-7.242129,-0.469815,4.184178,2.982452,9.608304,5.417122,-7.396425,5.772160,0.152320,6.823776,1.536886,1.740360,3.099686,-0.159903,5.492227,8.470731,0.796642,5.136430,-9.176856,4.577394,0.254549,-3.414283,6.861425,4.698585,1.979454,9.487023,-4.021864,-3.712483,0.946971,7.496192,2.378908,-1.688791,0.667389,-9.329938,-4.609950,3.488330,-6.629325,8.459217,-2.527621,-6.791836,7.032397,-0.216386,-7.586885,-9.258852,6.337980,7.506490,-0.514842,-2.179427,9.953929,2.144304,-1.719600,4.329503,-9.883477,-7.069341,1.108197,-9.694846,4.769512,4.392199,-9.385863,4.963892,6.479520,-8.251931,-2.824862,8.780627,3.731848,9.281105,-0.672497,6.460217,9.833865,0.386204,-3.492624,-8.440475,-6.353197,-3.040211,2.674886,1.497143,-7.222809,-5.989504,-3.737358,-5.894544,-9.744915,5.245676,-0.587409,-2.840927,6.375054,-7.549928,2.657426,5.334993,-7.253034,-7.364090,7.198502,6.120420,-4.781649,-2.043587,3.003346,-2.363616,-2.741491,-0.632660,-2.310644,-7.630842,-5.515740,-9.137831,7.559118,-7.369786,3.031438,0.381420,-8.225920,-0.963841,-5.890258,1.030287,1.331019,-7.183620,2.224853,-7.691400,4.703904,6.648393,7.532408,7.496655,3.820480,1.421551,1.807213,3.244174,3.213020,-9.133016,-6.429375,1.897717,6.325910,9.395288,7.984386,6.656944,4.310023,-8.356371,-7.020176,7.938580,4.462555,-0.458251,-1.109776,-7.535390,4.060570,8.610005,-9.561853,5.329492,-1.484086,1.131561,-3.841392,-2.257964,5.158244,-9.270204,2.609055,-0.799840,-7.786963,4.674717,-2.073177,-7.041668,-3.243558,-0.634795,0.819022,-7.890681,-7.784291,1.624851,-8.752559,-2.170661,-0.895869,9.787151,0.113821,2.256679,-3.097791,-9.289124,-9.598232,-2.156025,-3.465195,-1.651461,-4.227305,-2.482992,-4.488036,5.734910,9.666825,-9.079950,6.742281,0.222882,9.623806,-7.835004,9.985424,3.960604,-7.444720,-4.640452,-6.142652,-3.716058,-6.243103,5.454757,-5.791552,2.466539,5.528923,9.401873,-0.472598,1.186390,1.726945,5.983410,-5.116765,3.528434,8.707877,6.060339,-8.808607,-7.801327,-0.144179,5.835393,7.736568,2.268699,-9.255521,7.080334,9.988861,4.450650,-6.284192,-1.316760,1.785651,7.950307,5.392542,-9.175200,-6.957351,-8.231645,-2.153260,7.896339,4.392691,-3.652439,-3.945199,-5.593954,-4.829219,-3.241833,-4.221800,9.003943,-9.227014,-6.949260,-1.850745,0.913130,-8.549650,2.143776,5.811623,-7.854045,4.016053,1.120360,-8.529513,-1.922805,6.555463,8.388093,4.200278,7.560787,-3.370432,2.638526,-5.287028,9.435109,1.480536,5.194082,-4.247469,9.947068,7.660166,2.962742,-2.809583,-0.248696,-8.851706,1.902635,1.322595,-0.147870,4.480005,-9.854796,-4.535443,-7.295719,-8.404082,0.867583,7.914867,2.665177,7.887313,-5.720797,-7.227043,2.746761,-4.625307,-6.076228,8.785257,2.871702,-8.940858,-8.327475,-9.254804,-6.646385,-6.398938,4.368221,-7.081944,-9.386775,0.934814,6.222706,-4.567517,-8.441890,-6.742262,-3.258113,3.615720,-2.090005,9.989015,8.575394,4.014357,-3.889752,1.837565,0.026623,-2.899073,7.240316,-7.047447,6.865695,5.961643,7.785552,-4.797733,3.914280,-5.373208,-0.834970,-9.304303,6.034131,6.306254,2.056126,1.583155,9.549548,4.994441,8.296792,5.065433,-0.643022,-6.678817,-6.392131,5.679234,5.608522,6.188450,2.882264,7.019137,3.141179,-0.896794,8.205649,7.980579,-6.928269,6.432771,-8.535935,-2.744975,8.767667,0.134475,-8.523207,8.547323,-4.044267,4.230539,-8.381142,-8.295781,2.646794,-4.433978,-2.314056,4.162519,-1.718208,-4.678053,-3.493920,9.289071,6.596769,5.842098,8.249877,2.596022,-7.877317,7.680632,7.345251,-9.969926,9.721288,2.192023,0.609698,-3.974254,0.285669,-6.272207,7.916936,8.141946,-9.436535,-8.398668,7.820176,5.937930,-1.645478,-8.904965,-6.635696,4.635901,-6.633249,7.862435,9.103535,8.391879,-1.192818,-5.357734,-5.360490,8.113133,3.192615,-3.578187,9.406613,-1.645915,6.348090,-1.595812,9.955578,4.306317,-5.384733,5.315633,-0.900400,3.275351,1.821190,-9.233897,2.432302,-8.549304,-8.932858,-3.682495,9.330830,4.505996,0.961622,-4.441971,0.585661,-1.012324,8.182022,-2.063391,4.712313,-0.140584,1.870682,-8.851721,-4.546275,4.560766,5.492491,2.731117,-4.666115,1.947955,-3.237636,2.473352,8.474249,3.445706,3.262068,-1.294512,2.231303,2.470941,-6.408612,-4.066317,5.090053,8.093322,1.649041,4.120077,9.433103,8.015939,-9.010114,-4.512306,8.714134,-3.816306,1.879777,9.681370,-4.238906,2.987495,-9.500780,7.795164,-4.004609,-1.200535,1.995109,0.786373,1.212954,-4.436235,5.574074,0.311039,5.529190,-8.520740,1.169924,0.197474,-6.655434,-6.490408,-9.154693,-8.434729,-6.100363,-5.378296,-2.167341,-1.080826,9.648644,-6.302582,0.891670,7.332695,4.472942,1.668845,1.009351,-9.138860,-2.982486,-1.601279,9.491992,6.035143,2.183936,1.372292,2.035348,7.820860,0.262994,-6.543083,-6.998348,2.731542,9.039395,-7.003483,4.573674,-5.570419,8.932105,6.427598,-7.436988,-3.180878,-6.576893,1.584810,9.190168,-8.135705,-8.419459,-7.254233,-6.595553,9.615299,-4.174732,-2.148588,-6.688963,7.196626,1.409043,-5.735547,0.709369,-1.024219,3.520337,-4.436880,-9.159107,8.976331,1.418972,8.548780,4.623007,4.389370,-2.564086,3.866985,-5.190801,-1.551007,8.992196,4.729134,1.931463,4.508746,-7.152444,-6.933725,-1.211261,6.616004,5.026896,-1.249893,7.712610,-9.912851,6.507462,7.319911,8.949431,-8.239490,-2.164625], dtype = "float64")#candidate|5321|(3072,)|const|float64
call_5320 = relay.TupleGetItem(func_2531_call(relay.reshape(var_5315.astype('float64'), []), relay.reshape(const_5321.astype('float64'), [16, 16, 12]), relay.reshape(call_5313.astype('float64'), [26,]), ), 0)
call_5322 = relay.TupleGetItem(func_2536_call(relay.reshape(var_5315.astype('float64'), []), relay.reshape(const_5321.astype('float64'), [16, 16, 12]), relay.reshape(call_5313.astype('float64'), [26,]), ), 0)
output = relay.Tuple([call_5305,call_5313,var_5314,var_5315,var_5316,call_5320,const_5321,])
output2 = relay.Tuple([call_5306,call_5317,var_5314,var_5315,var_5316,call_5322,const_5321,])
func_5327 = relay.Function([var_5314,var_5315,var_5316,], output)
mod['func_5327'] = func_5327
mod = relay.transform.InferType()(mod)
var_5328 = relay.var("var_5328", dtype = "float32", shape = (26, 3))#candidate|5328|(26, 3)|var|float32
var_5329 = relay.var("var_5329", dtype = "uint64", shape = ())#candidate|5329|()|var|uint64
var_5330 = relay.var("var_5330", dtype = "int16", shape = (63,))#candidate|5330|(63,)|var|int16
output = func_5327(var_5328,var_5329,var_5330,)
func_5331 = relay.Function([var_5328,var_5329,var_5330,], output)
mutated_mod['func_5331'] = func_5331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_5338 = relay.TupleGetItem(func_4331_call(), 2)
call_5339 = relay.TupleGetItem(func_4333_call(), 2)
var_5353 = relay.var("var_5353", dtype = "float64", shape = (13, 15, 6))#candidate|5353|(13, 15, 6)|var|float64
bop_5354 = relay.less(call_5338.astype('bool'), var_5353.astype('bool')) # shape=(13, 15, 6)
bop_5357 = relay.less(call_5339.astype('bool'), var_5353.astype('bool')) # shape=(13, 15, 6)
output = bop_5354
output2 = bop_5357
func_5358 = relay.Function([var_5353,], output)
mod['func_5358'] = func_5358
mod = relay.transform.InferType()(mod)
mutated_mod['func_5358'] = func_5358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5359 = relay.var("var_5359", dtype = "float64", shape = (13, 15, 6))#candidate|5359|(13, 15, 6)|var|float64
func_5358_call = mutated_mod.get_global_var('func_5358')
call_5360 = func_5358_call(var_5359)
output = call_5360
func_5361 = relay.Function([var_5359], output)
mutated_mod['func_5361'] = func_5361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mod.get_global_var('func_4364')
func_4366_call = mutated_mod.get_global_var('func_4366')
call_5474 = relay.TupleGetItem(func_4364_call(), 2)
call_5475 = relay.TupleGetItem(func_4366_call(), 2)
output = call_5474
output2 = call_5475
func_5476 = relay.Function([], output)
mod['func_5476'] = func_5476
mod = relay.transform.InferType()(mod)
output = func_5476()
func_5477 = relay.Function([], output)
mutated_mod['func_5477'] = func_5477
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_5548 = relay.TupleGetItem(func_4331_call(), 4)
call_5549 = relay.TupleGetItem(func_4333_call(), 4)
output = call_5548
output2 = call_5549
func_5551 = relay.Function([], output)
mod['func_5551'] = func_5551
mod = relay.transform.InferType()(mod)
mutated_mod['func_5551'] = func_5551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5551_call = mutated_mod.get_global_var('func_5551')
call_5552 = func_5551_call()
output = call_5552
func_5553 = relay.Function([], output)
mutated_mod['func_5553'] = func_5553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_5613 = relay.TupleGetItem(func_4542_call(), 0)
call_5614 = relay.TupleGetItem(func_4544_call(), 0)
func_3977_call = mod.get_global_var('func_3977')
func_3980_call = mutated_mod.get_global_var('func_3980')
const_5632 = relay.const([1,-3,-9,-6,-6,8,-4,10,10,-6,7,6,6,3,3,7,3,7,-1,-3,-8,10,-2,5,10,-10,5,-2,-8,-10,-10,5,9,5,4,6,-1,-4,-9,-6,-8,-7,10,4,6,-9,1,10,-7,-1,-5,3,-5,10,5,4,10,-8,5,-10,-4,-7,-4,-4,-6,-2,-1,-8,3,2,-3,3,2,-6,1,-5,-7,-1,-3,-10,1,-9,-8,-1,-2,10,1,-9,-5,7,-2,-3,9,10,1,1,3,-6,-5,-1,-2,-4,-4,-6,-9,5,7,10,5,8,-9,10,8,-4,-7,-4,6,3,-3,9,2,-3,5,7,-3,-8,5,-6,-5,10,5,-10,1,3,2,8,-7,5,6,3,-10,-4,8,9,-10,3,2,8,-7,-1,-2,-3,10,4,3,-7,-8,-7,3,-8,-7,-10,-6,-4,9,2,-2,2,-4,-2,-4,9,2,-6,3,9,7,-9,-10,-4,6,-4,-10,4,5,-2,-7,-10,-8,-3,2,-1,5,-10,2,-6,1,-9,-6,-6,1,9,10,6,-6,8,-2,5,-8,-2,2,-9,8,5,-4,-7,10,2,5,-9,-6,-7,8,4,10,6,-4,6,-6,-7,3,-3,8,-4,-3,4,-9,-8,6,3,-9,-7,-8,4,3,2,3,-8,3,6,2,-7,-2,8,-8,3,1,-8,-2,-1,-4,-10,10,-2,7,-1,9,-1,-3,-8,-9,-8,-8], dtype = "int32")#candidate|5632|(273,)|const|int32
call_5631 = relay.TupleGetItem(func_3977_call(relay.reshape(const_5632.astype('int32'), [7, 13, 3]), relay.reshape(const_5632.astype('int32'), [7, 13, 3]), ), 0)
call_5633 = relay.TupleGetItem(func_3980_call(relay.reshape(const_5632.astype('int32'), [7, 13, 3]), relay.reshape(const_5632.astype('int32'), [7, 13, 3]), ), 0)
output = relay.Tuple([call_5613,call_5631,const_5632,])
output2 = relay.Tuple([call_5614,call_5633,const_5632,])
func_5646 = relay.Function([], output)
mod['func_5646'] = func_5646
mod = relay.transform.InferType()(mod)
output = func_5646()
func_5647 = relay.Function([], output)
mutated_mod['func_5647'] = func_5647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5551_call = mod.get_global_var('func_5551')
func_5553_call = mutated_mod.get_global_var('func_5553')
call_5648 = func_5551_call()
call_5649 = func_5551_call()
output = relay.Tuple([call_5648,])
output2 = relay.Tuple([call_5649,])
func_5653 = relay.Function([], output)
mod['func_5653'] = func_5653
mod = relay.transform.InferType()(mod)
mutated_mod['func_5653'] = func_5653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5653_call = mutated_mod.get_global_var('func_5653')
call_5654 = func_5653_call()
output = call_5654
func_5655 = relay.Function([], output)
mutated_mod['func_5655'] = func_5655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4317_call = mod.get_global_var('func_4317')
func_4318_call = mutated_mod.get_global_var('func_4318')
call_5687 = relay.TupleGetItem(func_4317_call(), 0)
call_5688 = relay.TupleGetItem(func_4318_call(), 0)
func_1142_call = mod.get_global_var('func_1142')
func_1144_call = mutated_mod.get_global_var('func_1144')
var_5693 = relay.var("var_5693", dtype = "float64", shape = (275,))#candidate|5693|(275,)|var|float64
call_5692 = func_1142_call(relay.reshape(var_5693.astype('float64'), [11, 5, 5]))
call_5694 = func_1142_call(relay.reshape(var_5693.astype('float64'), [11, 5, 5]))
func_761_call = mod.get_global_var('func_761')
func_764_call = mutated_mod.get_global_var('func_764')
const_5703 = relay.const([9,-10,-6,-2,-8,5,8,-3,1,5,7,6,5,-7,10,9,7,-2,2,-8,-10,10,4,-10,-7,10,-4,-5,2,-7,-3,-4,6,5,-1,-8,-5,-9,-2,-4,6,4,8,-9,3,-5,-2,7,6,-6,7,7,4,1,-7,-4,-8,-10,-10,-9,5,-9,2,5,-10,-6,-6,-8,-9,6,-3,6,9,-8,-7,3,-10,8,-8,1,-3,4,-9,10,1,-1,-6,-8,5,5,-4,3,-9,-7,6,-7,-6,-10,3,-1,4,3,-1,5,8,9,6,-5,4,4,-9,-1,-1,-9,1,-1,4,-4,-6,2], dtype = "int32")#candidate|5703|(120,)|const|int32
const_5704 = relay.const(10, dtype = "uint64")#candidate|5704|()|const|uint64
call_5702 = relay.TupleGetItem(func_761_call(relay.reshape(const_5703.astype('int32'), [10, 3, 4]), relay.reshape(const_5704.astype('uint64'), []), ), 1)
call_5705 = relay.TupleGetItem(func_764_call(relay.reshape(const_5703.astype('int32'), [10, 3, 4]), relay.reshape(const_5704.astype('uint64'), []), ), 1)
output = relay.Tuple([call_5687,call_5692,var_5693,call_5702,const_5703,const_5704,])
output2 = relay.Tuple([call_5688,call_5694,var_5693,call_5705,const_5703,const_5704,])
func_5707 = relay.Function([var_5693,], output)
mod['func_5707'] = func_5707
mod = relay.transform.InferType()(mod)
mutated_mod['func_5707'] = func_5707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5708 = relay.var("var_5708", dtype = "float64", shape = (275,))#candidate|5708|(275,)|var|float64
func_5707_call = mutated_mod.get_global_var('func_5707')
call_5709 = func_5707_call(var_5708)
output = call_5709
func_5710 = relay.Function([var_5708], output)
mutated_mod['func_5710'] = func_5710
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5729 = relay.const(True, dtype = "bool")#candidate|5729|()|const|bool
const_5730 = relay.const([[[True,True,True,False,False,False,False,False,True,False],[False,True,True,False,False,True,True,True,False,True],[False,True,False,False,False,False,True,False,True,True],[True,False,False,False,False,True,False,True,True,True],[True,False,True,False,False,True,False,True,False,False],[True,False,True,True,False,True,True,True,False,True],[False,True,True,True,True,False,False,False,True,True],[True,False,True,False,True,True,True,True,True,True],[True,False,True,False,True,True,False,True,True,False],[False,True,True,True,False,False,True,False,False,False]],[[False,False,True,True,False,False,True,False,True,False],[True,False,False,True,False,True,False,False,False,True],[False,False,True,True,False,True,False,True,False,False],[False,False,False,True,True,True,True,False,True,False],[False,False,False,False,True,False,False,False,True,False],[True,True,True,False,True,True,False,True,False,False],[True,False,False,False,True,True,True,False,False,False],[False,False,False,False,True,False,True,True,False,False],[True,True,True,False,False,False,True,False,True,False],[False,True,False,False,True,False,True,False,False,True]],[[False,True,False,False,True,True,False,False,False,False],[False,True,False,False,False,False,False,True,False,False],[True,False,True,False,False,False,False,True,False,False],[True,False,True,True,False,True,False,True,True,False],[True,False,True,True,False,True,True,False,True,True],[False,False,True,True,False,True,True,False,True,True],[True,False,True,False,True,False,True,True,True,True],[True,False,True,False,False,True,False,True,True,True],[True,False,True,False,True,False,False,True,False,True],[False,True,True,False,False,False,False,True,True,True]],[[False,False,True,True,False,True,False,False,True,False],[True,False,False,True,False,True,True,False,False,True],[True,True,True,False,True,True,False,True,False,True],[False,True,True,True,False,False,True,True,False,False],[True,False,False,True,True,False,False,False,True,True],[True,False,False,False,True,True,True,True,False,False],[True,False,True,False,True,True,False,False,False,True],[False,True,True,False,False,False,True,True,False,False],[False,True,False,False,False,True,True,True,True,True],[True,False,True,False,False,False,False,True,True,False]],[[False,True,False,True,False,False,True,True,True,True],[True,True,False,True,True,False,True,False,False,False],[True,True,False,False,False,False,True,False,True,False],[False,True,True,False,False,True,True,True,False,False],[False,True,False,True,True,True,True,False,False,True],[False,True,True,False,False,True,False,True,True,False],[True,True,True,False,False,False,False,True,True,False],[True,False,False,True,True,True,True,False,True,True],[False,True,False,True,True,False,False,True,True,True],[True,False,False,True,True,False,True,True,True,False]],[[True,True,False,True,False,True,False,True,False,True],[False,False,False,True,True,True,True,True,True,True],[False,False,True,False,True,False,True,False,True,False],[True,True,True,True,False,False,True,True,True,True],[False,False,True,True,True,False,False,False,True,True],[True,True,False,True,True,True,True,False,False,True],[True,True,False,False,False,False,False,True,True,False],[False,False,False,True,True,True,True,True,True,False],[True,True,True,True,False,True,False,True,True,False],[False,False,True,False,True,False,True,True,True,False]],[[True,False,False,True,True,True,False,True,True,False],[True,False,True,True,True,True,False,True,False,True],[False,True,False,True,True,True,True,False,False,True],[True,False,True,True,True,False,True,False,True,False],[False,True,False,True,False,True,False,False,False,False],[True,False,True,True,False,True,False,True,True,True],[False,False,True,True,False,False,False,True,False,True],[True,False,False,True,True,False,False,True,False,False],[False,False,True,True,True,True,False,False,False,False],[True,True,False,False,False,False,False,False,True,True]]], dtype = "bool")#candidate|5730|(7, 10, 10)|const|bool
bop_5731 = relay.logical_or(const_5729.astype('bool'), const_5730.astype('bool')) # shape=(7, 10, 10)
bop_5744 = relay.add(const_5730.astype('uint32'), relay.reshape(bop_5731.astype('uint32'), relay.shape_of(const_5730))) # shape=(7, 10, 10)
output = relay.Tuple([bop_5744,])
output2 = relay.Tuple([bop_5744,])
func_5749 = relay.Function([], output)
mod['func_5749'] = func_5749
mod = relay.transform.InferType()(mod)
mutated_mod['func_5749'] = func_5749
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5749_call = mutated_mod.get_global_var('func_5749')
call_5750 = func_5749_call()
output = call_5750
func_5751 = relay.Function([], output)
mutated_mod['func_5751'] = func_5751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_5767 = relay.TupleGetItem(func_4331_call(), 0)
call_5768 = relay.TupleGetItem(func_4333_call(), 0)
output = call_5767
output2 = call_5768
func_5773 = relay.Function([], output)
mod['func_5773'] = func_5773
mod = relay.transform.InferType()(mod)
output = func_5773()
func_5774 = relay.Function([], output)
mutated_mod['func_5774'] = func_5774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5749_call = mod.get_global_var('func_5749')
func_5751_call = mutated_mod.get_global_var('func_5751')
call_5783 = relay.TupleGetItem(func_5749_call(), 0)
call_5784 = relay.TupleGetItem(func_5751_call(), 0)
output = relay.Tuple([call_5783,])
output2 = relay.Tuple([call_5784,])
func_5785 = relay.Function([], output)
mod['func_5785'] = func_5785
mod = relay.transform.InferType()(mod)
output = func_5785()
func_5786 = relay.Function([], output)
mutated_mod['func_5786'] = func_5786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mod.get_global_var('func_5773')
func_5774_call = mutated_mod.get_global_var('func_5774')
call_5796 = func_5773_call()
call_5797 = func_5773_call()
func_988_call = mod.get_global_var('func_988')
func_991_call = mutated_mod.get_global_var('func_991')
const_5812 = relay.const([6,9,10,-8,6,-1,-9,-4,-2,-5,-4,7,3,-8,-3,-3,6,-9,-2,5,2,4,4,-6,10,1,8,-2,7,7,-3,-7,4,3,2,-3,-8,8,5,-8,-5,-1,-7,2,-4,-4,-1,6,-4,1,-9,-2,3,8,-4,-5,5,2,10,8,4,3,-2,1,7,3,8,4,-7,-9,9,2,1,-6,9,-7,5,-10,-10,-4,-5,-7,-2,2,1,2,7,-4,7,9,5,1,-7,-10,2,-6,-10,-9,3,-4,5,6,10,-10,1,3,9,-9,-6,5,-2,-6,3,-7,-7,1,-8,5,7,5,7,6,-3,-2,4,9,-10,8,-8,-10,-7,8,9,1,1,6,3,3,8,7,5,-8,8,-8,1,3,10,3,-7,9,-2,5,10,-3,5,10,3,3,-4,-2,-9,-4,8,-2,4,4,-8,-1,-9,7,-4,4,-5,-1,-7,3,-9,7,-6,2,-2,-8,-7,9,5,2,2,-9,4,-5,4,-9,7,-8,-6,-7,-1,9,5,-6,5,-10,-5,-4,-10,9,9,4,-3,2,-7,8,-3,-7,-6,-9,-10,-9,-9,-1,-4,-2,8,10,10,-5,-1,6,1,-2,-6,-9,3,9,-1,-2,3,-9,-10,6,-10,-9,-3,5,-8,-2,-2,-1,9,7,-2,-6,-3,-10,3,-4,-7,4,-10,6,7,-4,-1,4,-5,-1,-9,6,1,6,-1,8,3,-8,2,1,-3,8,10,-3,4,3,-10,-7,2,6,-2,-1,-6,-8,-4,8,5,-1,-10,9,-10,-7,-9,5,8,7,4,6,7,-8,6,8,6,4,6,9,-6,-10,3,-6,-5,-10,1,10,-4,8,-8,9,6,9,-9,-9,7,7,3,8,8,-8,7,-6,-8,-9,1,-10,3,10,-10,-4,8,-6,9,-10,3,8,8,3,10,-4,-1,-1,-6,6,-2,2,6,-3,-1,3,-3,-5,7,-8,-9,-2,-9,-5,-4,10,5,-7,1,5,-5,7,9,10,2,-7,-2,-1,1,-5,-1,2,10,-5,9,2,-8,3,-3,-5,3,-5,-10,6,-6,-6,-10,3,6,-1,-7,1,6,-5,7,3,4,2,8,-5,1,-3,8,10,-3,-10,-8,8,-5,2,-4,9,-6,-2,-1,1,6,2,8,-9,5,-3,-10,-6,3,4,-4,5,-6,-4,-6,8,7,-8,-3,7,-8,-2,1,-3,5,-2,-2,9,-8,4,8,-5,-3,-1,2,6,-8,8,6,4,1,-2,-4,3,-4,3,-1,6,-3,-2,-6,-3,-7,-4,2,-6,-3,-8,-9,-7,9,4,2,6,6,-8,-8,-7,-2,10,8,-7,-6,7,5,8,-8,4,2,-3,9,3,4,4,2,10,-2,2,-3,3,5,-1,-4,2,8,4,-9,-5,-6,9,-5,-7,-7,4,8,-9,9,-7,-7,-6,-6,-4,-7,10,-10,-1,-9,9,-7,-7,10,-9,5,9,7,-9,-10,-10,2,2,8,-6,-2,-4,-7,6,-6,-6,1,3,5,-2,4,1,1,-9,-7,-7,-9,-1,-1,-4,2,-6,-7,2,4,4,6,-6,-9,6,-10,-8,-4,-3,-6,10,9,2,8,6,9,-9,-7,10,2,3,-8,10,10,5,-2,-5,-2,5,-2,-1,2,4,9,-5,-1,-2,3,-9,5,10,-10,6,-1,-3,1,4,5,3,3,6,10,2,-10,-6,-6,2,-1,-1,9,-5,-7,-8,-8,-8,-10,-4,-2,4,7,7,-6,3,-7,-8,-8,1,-4,10,9,-3,-4,-9,-3,-8,-3,-8,-6,-4,5,1,9,-9,-2,-4,-8,-10,-4,-9,-10,-1,-6,1,10,-4,9,8,-9,10,-7,2,1,-8,-9,-6,-7,-3,6,2,-9,-10,-4,-6,-5,-4,-1,8,8,-9,-6,-9,1,-6,6,-2,-4,5,1,1,-10,-8,3,2,-3,-8,7,-2,9,-7,5,2,-2,-9,10,8,-7,10,-4,9,5,-8,7,3,7,-3,-7,-2,-3,1,1,3,8,7,-6,-1,8,-3,1,-10,-6,-1,-9,-4,-5,6,-6,3,-4,6,-1,-1,10,3,-2,10,-6,-4,5,7,-5,-6,-4,5,-3,8,-1,2,-4,3,-6,7,7,8,9,1,-10,7,10,-6,6,-7,-4,8,-2,6,-7,1,-2,5,-8,-9,5,-6,9,-6,-5,-10,9,-7,-3,10,-3,2,-4,1,3,-10,-6,-3,-8,10,3,-10,-9,5,7,-2,6,10,-10,2,10,2,-8,-1,-6,-10,2,-1,-5,3,-2,6,8,10,6,-1,-3,4,-10,10,7,-2,7,10,-10,8,7,-9,-10,10,8,6,-6,5,-7,-9,2,-3,-5,-3,-5,4,-4,6,-10,4,10,1,8,2,-10,2,-2,-1,8,-1,-6,7,-10,6,1,-1,-9,9,-8,-5,-1,10,-9,-2,6,2,-2,2,3,-3,-7,5,7,-3,4,3,4,3,-4,-2,2,-10,4,8,1,2,-6,-4,-3,-7,-7,-4,-4,6,-2,8,-4,-8,-2,8,8,1,-8,-8,-2,-8,7,-9,9,-9,-4,6,-5,10,1,-1,9,4,7,-8,6,5,8,-4,-9,-9,-8,-3,-9,2,-1,10,5,5,5,10,-9,-5,-10,5,2,4,-9,4,-8,-10,1,8,4,-9,-9,2,-5,7,8,5,-6,-1,-6,2,3,-4,2,2,7,6,-10,6,-5,-1,4,2,-6,2,-8,-7,-6,5,5,5,9,-2,8,-4,-10,8,2,-4,3,-10,2,-1,-10,-10,4,-9,-7,-1,8,9,-2,-3,-5,3,-5,-8,-10,-9,7,-7,5,3,-8,6,-10,3,-2,-6,-3,6,10,7,4,4,3,2,7,9,-10,1,-10,1,1,8,6,4,-9,-8,4,4,-3,-7,-2,8,-1,-1,3,2,1,10,5,5,-2,7,-5,5,-9,-10,9,2,-7,3,-9,6,7,7,-9,-8,-5,8,7,-10,4,-9,8,-2,-8,-6,10,-7,5,10,8,6,-2,5,-6,8,-7,-4,10,-3,-3,-3,9,1,-6,10,9,-9,-8,4,3,5,-1,-6,-7,9,-8,-2,-4,10,5,8,-6,7,-3,-2,-3,6,-8,-4,3,-6,8,5,2,-4,7,-1,8,9,-8,-8,7,-6,-8,1,-4,2,4,3,-7,1,10,-7,9,-2,8,-10,5,2,-6,7,-2,1,-8,-2,-5,9,4,-4,5,-1,-5,9,-5,-3,6,1,9,-3,-8,4,-7,-9,-10,-5,-10,-7,7,6,7,-3,1,2,-7,9,-10,-1,5,-10,-4,9,1,-8,9,2,-5,-2,8,6,-9,-3,9,7,-5,-8,-4,-2,10,5,5,-9,2,-7,-5,8,-2,-6,8,-5,-2,1,-8,3,4,-1,-5,1,2,-10,5,-5,-2,7,4,-10,-5,-2,-5,-2,5,9,-4,9,-2,-4,-8,3,-10,9,-2,-10,-1,9,9,4,5,-4,-4,6], dtype = "uint32")#candidate|5812|(1320,)|const|uint32
var_5813 = relay.var("var_5813", dtype = "float64", shape = (26,))#candidate|5813|(26,)|var|float64
call_5811 = relay.TupleGetItem(func_988_call(relay.reshape(const_5812.astype('uint32'), [8, 15, 11]), relay.reshape(var_5813.astype('float64'), [26,]), ), 2)
call_5814 = relay.TupleGetItem(func_991_call(relay.reshape(const_5812.astype('uint32'), [8, 15, 11]), relay.reshape(var_5813.astype('float64'), [26,]), ), 2)
func_4914_call = mod.get_global_var('func_4914')
func_4916_call = mutated_mod.get_global_var('func_4916')
call_5823 = relay.TupleGetItem(func_4914_call(), 0)
call_5824 = relay.TupleGetItem(func_4916_call(), 0)
func_4567_call = mod.get_global_var('func_4567')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_5830 = relay.TupleGetItem(func_4567_call(), 0)
call_5831 = relay.TupleGetItem(func_4568_call(), 0)
output = relay.Tuple([call_5796,call_5811,const_5812,var_5813,call_5823,call_5830,])
output2 = relay.Tuple([call_5797,call_5814,const_5812,var_5813,call_5824,call_5831,])
func_5834 = relay.Function([var_5813,], output)
mod['func_5834'] = func_5834
mod = relay.transform.InferType()(mod)
mutated_mod['func_5834'] = func_5834
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5835 = relay.var("var_5835", dtype = "float64", shape = (26,))#candidate|5835|(26,)|var|float64
func_5834_call = mutated_mod.get_global_var('func_5834')
call_5836 = func_5834_call(var_5835)
output = call_5836
func_5837 = relay.Function([var_5835], output)
mutated_mod['func_5837'] = func_5837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5551_call = mod.get_global_var('func_5551')
func_5553_call = mutated_mod.get_global_var('func_5553')
call_5885 = func_5551_call()
call_5886 = func_5551_call()
uop_5894 = relay.cos(call_5885.astype('float64')) # shape=(275, 1)
uop_5896 = relay.cos(call_5886.astype('float64')) # shape=(275, 1)
func_761_call = mod.get_global_var('func_761')
func_764_call = mutated_mod.get_global_var('func_764')
const_5900 = relay.const([[4,5,4,2,-4,-5,4,-6,4,-8,8,2,-7,6,-6,-6,-4,4,10,1,-9,-6,4,1,-7,-1,-6,-5,-7,2,7,8,6,-1,-7,2,-1,-2,-10,10],[-3,-4,-8,-9,-2,-10,10,-2,9,-5,-8,-4,-5,3,-9,-5,-6,1,-10,8,-3,2,-8,10,-10,8,3,-8,-10,4,-3,-4,-7,-2,-7,-10,-3,-4,9,-2],[10,-10,2,1,-6,-1,-3,-10,2,-7,4,-9,-10,-10,10,1,-10,5,6,3,-1,4,1,-2,6,2,-7,-7,-6,7,8,6,-6,9,-6,-7,-1,9,-5,-5]], dtype = "int32")#candidate|5900|(3, 40)|const|int32
var_5901 = relay.var("var_5901", dtype = "uint64", shape = ())#candidate|5901|()|var|uint64
call_5899 = relay.TupleGetItem(func_761_call(relay.reshape(const_5900.astype('int32'), [10, 3, 4]), relay.reshape(var_5901.astype('uint64'), []), ), 2)
call_5902 = relay.TupleGetItem(func_764_call(relay.reshape(const_5900.astype('int32'), [10, 3, 4]), relay.reshape(var_5901.astype('uint64'), []), ), 2)
func_5646_call = mod.get_global_var('func_5646')
func_5647_call = mutated_mod.get_global_var('func_5647')
call_5908 = relay.TupleGetItem(func_5646_call(), 0)
call_5909 = relay.TupleGetItem(func_5647_call(), 0)
output = relay.Tuple([uop_5894,call_5899,const_5900,var_5901,call_5908,])
output2 = relay.Tuple([uop_5896,call_5902,const_5900,var_5901,call_5909,])
func_5915 = relay.Function([var_5901,], output)
mod['func_5915'] = func_5915
mod = relay.transform.InferType()(mod)
mutated_mod['func_5915'] = func_5915
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5916 = relay.var("var_5916", dtype = "uint64", shape = ())#candidate|5916|()|var|uint64
func_5915_call = mutated_mod.get_global_var('func_5915')
call_5917 = func_5915_call(var_5916)
output = call_5917
func_5918 = relay.Function([var_5916], output)
mutated_mod['func_5918'] = func_5918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_5939 = relay.TupleGetItem(func_4542_call(), 0)
call_5940 = relay.TupleGetItem(func_4544_call(), 0)
func_3222_call = mod.get_global_var('func_3222')
func_3225_call = mutated_mod.get_global_var('func_3225')
const_5942 = relay.const([[-6.027715,4.286662,9.788672,-3.376260,6.793762,-3.102755,-0.330696,9.831367,-9.808787,6.592746,8.024097,9.271314,-7.779851,-6.959372,7.299719,4.088531,-4.169671,-2.785085,-3.841919,9.854466,-6.112955,5.036496,-0.459739,-1.272565,9.679241,7.552096,4.036067,0.661053,7.874335,-2.401120,-5.035479,-7.195424,-7.245359,9.674901,-3.939023,-9.489672,-4.597373,9.108674,-0.118522,7.181284,2.238421,-6.287911,3.549889,-6.582407,-1.740115,-2.718551,-8.671726,5.139643,9.732691,2.725469,-9.836268,6.721530,-5.762738,8.892357,-1.795898,-4.701230,9.113390,5.270674,-1.015438,-1.727832,-7.929756,-1.898367,9.702141,-0.200511,-7.106810,-4.970939,6.716733,1.019171,-6.126356,1.600312,0.002852,-8.921848,-6.084207,4.423696,0.129896,7.530410,-7.148063,7.687304],[-9.809198,1.438074,9.880247,3.273260,1.030663,-0.648984,2.574252,-4.336751,-8.036290,3.421769,-9.716664,4.919697,-2.417429,-9.313533,-8.155672,9.660080,8.029325,3.386722,-3.820003,7.728663,6.144883,-0.185899,2.722868,7.626912,0.396089,1.926854,-1.137885,-3.492567,5.825905,2.314767,-1.114207,-9.187941,0.111395,-5.898512,-5.701714,8.661489,-9.108100,-5.565655,2.455500,5.373989,2.819355,-2.779411,7.814035,-0.374011,4.439166,3.769451,-0.023502,5.079585,4.037458,-1.796833,-6.149475,-3.122026,4.816610,-4.702650,-5.346367,7.439172,-0.477791,6.215448,-1.228328,4.850248,-6.474735,7.155246,-6.429857,-5.142233,0.800704,-0.237129,6.889303,-6.046876,0.678372,9.616006,-2.629519,0.387362,-5.679582,-9.585618,9.769527,7.196894,-8.345279,-6.818474],[5.855944,6.051604,1.496638,-4.477397,-6.475229,9.936903,-7.370605,8.236064,-9.262651,9.579718,-8.532317,5.193528,1.436661,9.219839,-8.854835,5.811979,-5.188433,-1.728943,-8.569086,-1.058070,3.672906,-5.795992,-6.292213,-6.788384,5.060593,-7.213355,6.043981,3.557691,-3.231066,3.651882,-2.154540,-5.237956,8.853485,3.870222,-4.309384,-3.587480,5.429759,2.324900,-1.409273,-9.641786,2.666428,7.715721,1.759775,-5.843539,7.433133,-6.694324,-8.932652,7.054249,0.462207,9.799859,-6.179991,1.308130,-8.119745,-6.041883,-4.984215,-8.750455,8.340572,-0.151299,-8.933230,-5.165005,-8.000176,-3.928160,7.698946,-9.322888,-1.016165,-6.443135,6.691923,-0.338148,-8.650973,4.596735,-5.559555,7.778816,6.384281,-7.454438,-0.779577,-2.769572,3.955175,8.036191],[-0.082504,7.334038,4.897001,7.315297,5.735514,-0.321858,-8.411758,-8.484310,-1.898398,-9.480716,8.029155,0.359892,4.262810,6.827961,-7.655765,-9.946717,-6.100198,1.319228,6.695765,0.807451,2.294787,6.633327,8.711693,-0.383313,5.796215,4.888256,7.980265,-9.077510,-2.194191,9.060652,-2.163219,1.959250,8.775421,-3.275884,-9.033465,1.829475,7.216431,5.501080,-0.713271,-3.857883,1.266081,-9.913822,2.868801,4.644877,-2.078978,-4.498881,-2.941798,-7.983579,9.756638,7.677346,-4.877921,0.828097,9.614398,-7.845054,-6.585497,8.045785,-9.458368,-5.786791,-0.473797,-0.494905,-3.265050,9.584566,-6.465305,-5.462307,-4.401973,0.316895,-2.441805,-5.625862,-1.539564,7.778014,-9.696156,-2.949684,-7.546788,-6.189113,-4.150875,-3.641008,9.129324,-4.123852],[8.075396,8.563132,-8.231676,-2.955384,3.924866,-3.753032,3.268876,-1.143553,-1.792680,-2.537280,5.560504,5.558387,7.786854,-6.473688,5.876638,0.027609,3.948475,-7.801905,4.954560,-6.213911,8.080816,-9.625223,-5.776561,-5.154976,8.090173,-2.318474,1.094450,3.928405,7.066838,-5.291995,-8.886310,2.049691,-0.571368,8.035132,-7.082473,7.317226,-4.211080,-3.076688,-4.287529,6.380591,6.875276,4.187547,6.562090,-1.287364,-4.324742,9.093178,-4.911817,9.593073,-1.460287,-9.881164,-6.366987,-8.066923,-9.353736,-4.540409,-8.932017,-1.700273,5.766386,-5.475808,-3.164429,1.305592,7.321948,4.263640,9.636820,1.979604,0.037978,-4.851545,4.034806,-3.851668,8.882067,-1.626218,-8.681682,6.629276,-7.862126,-4.405259,-7.068862,-9.979981,-5.137806,7.820240],[-2.524636,6.594695,3.365921,7.938090,8.178320,-7.250768,-0.381631,-7.496467,8.874808,-0.542061,6.992338,6.293081,-9.871046,-5.991519,9.312378,-3.584547,-1.730775,-6.756518,0.071707,-9.224080,0.850122,7.625581,0.753825,1.480560,-5.653609,7.414878,-5.311371,3.629933,-1.351865,-5.647654,-0.660439,6.097618,-4.566471,-8.927695,8.486765,-1.987774,0.641242,0.145702,0.869176,2.015534,-2.462742,-2.167268,6.069276,-0.420564,1.151119,-3.557715,0.960435,-9.055849,9.213383,-7.932919,1.149336,9.008972,-6.472263,4.727182,6.166851,2.967306,7.686136,0.358881,-8.636377,-2.135151,-1.124580,6.902016,-1.683574,2.545415,-6.713908,6.581887,6.010128,-8.503389,7.186645,3.516000,-7.068555,-6.109780,-6.651907,1.187104,6.458757,-9.391467,-8.544848,-2.965019],[6.176012,-6.656544,1.695200,8.140174,-4.837438,-7.459980,-7.101484,7.006867,6.050814,-2.710850,1.375956,-3.002750,-0.288070,-0.356964,-3.359919,0.044299,-0.446068,9.690735,9.362099,-5.568706,-4.906845,2.279170,8.138585,4.586687,6.760603,-1.746591,8.246203,5.056081,-4.051489,-6.462673,-6.324831,-8.409574,2.090874,-1.914343,6.601863,2.992805,-6.921563,-0.111132,3.900030,-4.449973,3.775665,2.416956,5.564219,-4.677599,-7.019509,-8.525424,9.174354,8.330316,-7.762470,1.905693,8.768616,4.594235,-1.265069,2.730326,0.326306,-7.537185,-3.264456,-8.502982,-1.499988,8.790075,5.727515,-3.734361,7.964699,-9.270138,7.000675,0.736528,-9.747781,-1.943289,-0.942674,-1.223298,6.472957,-1.814299,-5.019284,9.267814,-0.140619,6.114053,-6.473463,-3.016011]], dtype = "float32")#candidate|5942|(7, 78)|const|float32
call_5941 = relay.TupleGetItem(func_3222_call(relay.reshape(const_5942.astype('float32'), [6, 7, 13])), 0)
call_5943 = relay.TupleGetItem(func_3225_call(relay.reshape(const_5942.astype('float32'), [6, 7, 13])), 0)
var_5953 = relay.var("var_5953", dtype = "float32", shape = (7, 78))#candidate|5953|(7, 78)|var|float32
bop_5954 = relay.logical_xor(const_5942.astype('uint8'), relay.reshape(var_5953.astype('uint8'), relay.shape_of(const_5942))) # shape=(7, 78)
output = relay.Tuple([call_5939,call_5941,bop_5954,])
output2 = relay.Tuple([call_5940,call_5943,bop_5954,])
func_5974 = relay.Function([var_5953,], output)
mod['func_5974'] = func_5974
mod = relay.transform.InferType()(mod)
mutated_mod['func_5974'] = func_5974
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5975 = relay.var("var_5975", dtype = "float32", shape = (7, 78))#candidate|5975|(7, 78)|var|float32
func_5974_call = mutated_mod.get_global_var('func_5974')
call_5976 = func_5974_call(var_5975)
output = call_5976
func_5977 = relay.Function([var_5975], output)
mutated_mod['func_5977'] = func_5977
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4567_call = mod.get_global_var('func_4567')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_5997 = relay.TupleGetItem(func_4567_call(), 0)
call_5998 = relay.TupleGetItem(func_4568_call(), 0)
uop_6003 = relay.exp(call_5997.astype('float64')) # shape=(4, 12, 13)
uop_6005 = relay.exp(call_5998.astype('float64')) # shape=(4, 12, 13)
output = uop_6003
output2 = uop_6005
func_6009 = relay.Function([], output)
mod['func_6009'] = func_6009
mod = relay.transform.InferType()(mod)
output = func_6009()
func_6010 = relay.Function([], output)
mutated_mod['func_6010'] = func_6010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_6041 = relay.TupleGetItem(func_4331_call(), 2)
call_6042 = relay.TupleGetItem(func_4333_call(), 2)
var_6069 = relay.var("var_6069", dtype = "float64", shape = (3, 16, 14))#candidate|6069|(3, 16, 14)|var|float64
bop_6070 = relay.logical_and(call_6041.astype('bool'), var_6069.astype('bool')) # shape=(3, 16, 14)
bop_6073 = relay.logical_and(call_6042.astype('bool'), var_6069.astype('bool')) # shape=(3, 16, 14)
output = relay.Tuple([bop_6070,])
output2 = relay.Tuple([bop_6073,])
func_6074 = relay.Function([var_6069,], output)
mod['func_6074'] = func_6074
mod = relay.transform.InferType()(mod)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6075 = relay.var("var_6075", dtype = "float64", shape = (3, 16, 14))#candidate|6075|(3, 16, 14)|var|float64
func_6074_call = mutated_mod.get_global_var('func_6074')
call_6076 = func_6074_call(var_6075)
output = call_6076
func_6077 = relay.Function([var_6075], output)
mutated_mod['func_6077'] = func_6077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4567_call = mod.get_global_var('func_4567')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_6117 = relay.TupleGetItem(func_4567_call(), 0)
call_6118 = relay.TupleGetItem(func_4568_call(), 0)
output = relay.Tuple([call_6117,])
output2 = relay.Tuple([call_6118,])
func_6127 = relay.Function([], output)
mod['func_6127'] = func_6127
mod = relay.transform.InferType()(mod)
output = func_6127()
func_6128 = relay.Function([], output)
mutated_mod['func_6128'] = func_6128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_6169 = func_4821_call()
call_6170 = func_4821_call()
func_5785_call = mod.get_global_var('func_5785')
func_5786_call = mutated_mod.get_global_var('func_5786')
call_6174 = relay.TupleGetItem(func_5785_call(), 0)
call_6175 = relay.TupleGetItem(func_5786_call(), 0)
output = relay.Tuple([call_6169,call_6174,])
output2 = relay.Tuple([call_6170,call_6175,])
func_6205 = relay.Function([], output)
mod['func_6205'] = func_6205
mod = relay.transform.InferType()(mod)
output = func_6205()
func_6206 = relay.Function([], output)
mutated_mod['func_6206'] = func_6206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5785_call = mod.get_global_var('func_5785')
func_5786_call = mutated_mod.get_global_var('func_5786')
call_6209 = relay.TupleGetItem(func_5785_call(), 0)
call_6210 = relay.TupleGetItem(func_5786_call(), 0)
uop_6213 = relay.asinh(call_6209.astype('float32')) # shape=(7, 10, 10)
uop_6215 = relay.asinh(call_6210.astype('float32')) # shape=(7, 10, 10)
output = uop_6213
output2 = uop_6215
func_6218 = relay.Function([], output)
mod['func_6218'] = func_6218
mod = relay.transform.InferType()(mod)
output = func_6218()
func_6219 = relay.Function([], output)
mutated_mod['func_6219'] = func_6219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5646_call = mod.get_global_var('func_5646')
func_5647_call = mutated_mod.get_global_var('func_5647')
call_6307 = relay.TupleGetItem(func_5646_call(), 0)
call_6308 = relay.TupleGetItem(func_5647_call(), 0)
func_6205_call = mod.get_global_var('func_6205')
func_6206_call = mutated_mod.get_global_var('func_6206')
call_6319 = relay.TupleGetItem(func_6205_call(), 0)
call_6320 = relay.TupleGetItem(func_6206_call(), 0)
output = relay.Tuple([call_6307,call_6319,])
output2 = relay.Tuple([call_6308,call_6320,])
func_6321 = relay.Function([], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
mutated_mod['func_6321'] = func_6321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6321_call = mutated_mod.get_global_var('func_6321')
call_6322 = func_6321_call()
output = call_6322
func_6323 = relay.Function([], output)
mutated_mod['func_6323'] = func_6323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5476_call = mod.get_global_var('func_5476')
func_5477_call = mutated_mod.get_global_var('func_5477')
call_6365 = func_5476_call()
call_6366 = func_5476_call()
output = call_6365
output2 = call_6366
func_6376 = relay.Function([], output)
mod['func_6376'] = func_6376
mod = relay.transform.InferType()(mod)
mutated_mod['func_6376'] = func_6376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mutated_mod.get_global_var('func_6376')
call_6377 = func_6376_call()
output = call_6377
func_6378 = relay.Function([], output)
mutated_mod['func_6378'] = func_6378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5476_call = mod.get_global_var('func_5476')
func_5477_call = mutated_mod.get_global_var('func_5477')
call_6382 = func_5476_call()
call_6383 = func_5476_call()
output = call_6382
output2 = call_6383
func_6391 = relay.Function([], output)
mod['func_6391'] = func_6391
mod = relay.transform.InferType()(mod)
mutated_mod['func_6391'] = func_6391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6391_call = mutated_mod.get_global_var('func_6391')
call_6392 = func_6391_call()
output = call_6392
func_6393 = relay.Function([], output)
mutated_mod['func_6393'] = func_6393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_6422 = func_4821_call()
call_6423 = func_4821_call()
output = call_6422
output2 = call_6423
func_6442 = relay.Function([], output)
mod['func_6442'] = func_6442
mod = relay.transform.InferType()(mod)
mutated_mod['func_6442'] = func_6442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6442_call = mutated_mod.get_global_var('func_6442')
call_6443 = func_6442_call()
output = call_6443
func_6444 = relay.Function([], output)
mutated_mod['func_6444'] = func_6444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6321_call = mod.get_global_var('func_6321')
func_6323_call = mutated_mod.get_global_var('func_6323')
call_6456 = relay.TupleGetItem(func_6321_call(), 1)
call_6457 = relay.TupleGetItem(func_6323_call(), 1)
uop_6463 = relay.tan(call_6456.astype('float32')) # shape=(11, 5, 5)
uop_6465 = relay.tan(call_6457.astype('float32')) # shape=(11, 5, 5)
output = relay.Tuple([uop_6463,])
output2 = relay.Tuple([uop_6465,])
func_6475 = relay.Function([], output)
mod['func_6475'] = func_6475
mod = relay.transform.InferType()(mod)
output = func_6475()
func_6476 = relay.Function([], output)
mutated_mod['func_6476'] = func_6476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4914_call = mod.get_global_var('func_4914')
func_4916_call = mutated_mod.get_global_var('func_4916')
call_6496 = relay.TupleGetItem(func_4914_call(), 3)
call_6497 = relay.TupleGetItem(func_4916_call(), 3)
output = relay.Tuple([call_6496,])
output2 = relay.Tuple([call_6497,])
func_6504 = relay.Function([], output)
mod['func_6504'] = func_6504
mod = relay.transform.InferType()(mod)
output = func_6504()
func_6505 = relay.Function([], output)
mutated_mod['func_6505'] = func_6505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4823_call = mutated_mod.get_global_var('func_4823')
call_6523 = func_4821_call()
call_6524 = func_4821_call()
var_6528 = relay.var("var_6528", dtype = "float32", shape = (11, 5, 5))#candidate|6528|(11, 5, 5)|var|float32
bop_6529 = relay.maximum(call_6523.astype('uint64'), relay.reshape(var_6528.astype('uint64'), relay.shape_of(call_6523))) # shape=(11, 5, 5)
bop_6532 = relay.maximum(call_6524.astype('uint64'), relay.reshape(var_6528.astype('uint64'), relay.shape_of(call_6524))) # shape=(11, 5, 5)
func_5785_call = mod.get_global_var('func_5785')
func_5786_call = mutated_mod.get_global_var('func_5786')
call_6533 = relay.TupleGetItem(func_5785_call(), 0)
call_6534 = relay.TupleGetItem(func_5786_call(), 0)
func_4914_call = mod.get_global_var('func_4914')
func_4916_call = mutated_mod.get_global_var('func_4916')
call_6554 = relay.TupleGetItem(func_4914_call(), 2)
call_6555 = relay.TupleGetItem(func_4916_call(), 2)
func_6442_call = mod.get_global_var('func_6442')
func_6444_call = mutated_mod.get_global_var('func_6444')
call_6565 = func_6442_call()
call_6566 = func_6442_call()
func_2639_call = mod.get_global_var('func_2639')
func_2642_call = mutated_mod.get_global_var('func_2642')
var_6569 = relay.var("var_6569", dtype = "bool", shape = (288,))#candidate|6569|(288,)|var|bool
call_6568 = relay.TupleGetItem(func_2639_call(relay.reshape(var_6569.astype('bool'), [3, 16, 6])), 0)
call_6570 = relay.TupleGetItem(func_2642_call(relay.reshape(var_6569.astype('bool'), [3, 16, 6])), 0)
uop_6577 = relay.sigmoid(call_6523.astype('float32')) # shape=(11, 5, 5)
uop_6579 = relay.sigmoid(call_6524.astype('float32')) # shape=(11, 5, 5)
uop_6584 = relay.atan(call_6568.astype('float32')) # shape=(3, 16, 6)
uop_6586 = relay.atan(call_6570.astype('float32')) # shape=(3, 16, 6)
func_5327_call = mod.get_global_var('func_5327')
func_5331_call = mutated_mod.get_global_var('func_5331')
const_6589 = relay.const([-9.401182,5.424328,5.852622,-0.359242,2.277451,6.333115,1.561882,-1.731093,-8.181240,-9.200003,5.377814,-2.207498,4.999908,-7.146666,7.314532,-9.769848,-7.321142,-5.585709,3.316140,9.732833,1.088664,8.688686,-7.192004,8.900931,7.503660,5.306434,3.805500,-2.035557,-3.200493,3.504060,-2.486719,1.952092,-1.612283,-2.305297,-0.538664,-1.065386,4.492546,-8.844644,-8.118332,-5.505553,1.831334,-3.616784,-7.176470,2.205662,4.384955,-0.399500,-5.864640,-6.766514,-9.858479,-8.525740,-9.264719,-5.844474,7.387075,0.323470,1.846027,5.095502,-3.781934,1.052574,-9.896769,5.286717,-3.036933,9.566843,7.771768,7.365324,0.733463,-9.667845,-6.692157,8.219193,8.652189,7.619439,-8.995851,2.649838,2.044819,3.338254,8.284929,9.374393,7.934552,8.089465], dtype = "float32")#candidate|6589|(78,)|const|float32
var_6590 = relay.var("var_6590", dtype = "int16", shape = (7, 9))#candidate|6590|(7, 9)|var|int16
call_6588 = relay.TupleGetItem(func_5327_call(relay.reshape(const_6589.astype('float32'), [26, 3]), relay.reshape(call_6554.astype('uint64'), []), relay.reshape(var_6590.astype('int16'), [63,]), ), 0)
call_6591 = relay.TupleGetItem(func_5331_call(relay.reshape(const_6589.astype('float32'), [26, 3]), relay.reshape(call_6554.astype('uint64'), []), relay.reshape(var_6590.astype('int16'), [63,]), ), 0)
func_3831_call = mod.get_global_var('func_3831')
func_3833_call = mutated_mod.get_global_var('func_3833')
const_6617 = relay.const([-7,7,5,5,3,-7,-1,-8,-5,7,-9,6,8,-6,-7,6,-7,-9,2,-10,9,-5,4,1,-6,-7,-1,-1,-7,7,-9,7,-7,-10,-2,4,-8,4,-2,3,-5,7,7,4,-4,-7,-5,10,-3,-1,-1,-6,3,2,5,5,8,-6,1,-7,1,7,8,-6,-6,-6,1,7,-2,-9,-6,8,10,7,4,-4,9,8,9,-8,2,-3,8,5,2,-8,2,-2,-10,2,4,8,9,1,-2,2,-5,-7,8,-2,7,9,-5,-2,2,10,9,-9,6,6,-1,3,5,8,3,-4,-7,2,3,-9,-7,3,9,-6,-4,-6,-1,10,9,9,-5,6,5,-5,1,5,5,6,10,2,4,-6,6,-1,1,9,-3,9,3,8,8,-4,9,-10,1,2,7,-10,-3,8,-1,1,3,3,6,2,3,8,7,3,-9,3,3,10,4,-4,-6,8,7,-7,-1,6,8,-9,3,3,9,9,-1,9,-7,-8,-10,-6,8,-9,-6,-6,-10,-9,9,6,-10,-1,1,6,-5,-5,-1,-3,4,-1,-8,5,1,2,8,9,10,-10,-2,-1,9,3,6,-2,-7,-1,7,4,9,-2,-1,-4,-1,-3,9,1,1,1,-9,8,-3,2,2,-9,-9,6,2,-2,-6,-9,3,4,-5,1,-7,1,-5,-9,-6,-8,1,-6,5,7,6,-6,-7,3,7,-5,1,4,8,5,-4,-10,8,-2,-7,4,-7,2,-3,4,-9,2,-5,-7,2,9,-6,4,9,7,-5,9,3,3,-6,-6,6,-6,6,5,9,5,7,9,3,1,-9,9,-2,10,1,-7,-7,9,-8,3,-2,-3,6,-2,10,-9,4,4], dtype = "int16")#candidate|6617|(330,)|const|int16
call_6616 = relay.TupleGetItem(func_3831_call(relay.reshape(const_6617.astype('int16'), [11, 15, 2])), 1)
call_6618 = relay.TupleGetItem(func_3833_call(relay.reshape(const_6617.astype('int16'), [11, 15, 2])), 1)
output = relay.Tuple([bop_6529,call_6533,call_6554,call_6565,var_6569,uop_6577,uop_6584,call_6588,const_6589,var_6590,call_6616,const_6617,])
output2 = relay.Tuple([bop_6532,call_6534,call_6555,call_6566,var_6569,uop_6579,uop_6586,call_6591,const_6589,var_6590,call_6618,const_6617,])
func_6628 = relay.Function([var_6528,var_6569,var_6590,], output)
mod['func_6628'] = func_6628
mod = relay.transform.InferType()(mod)
mutated_mod['func_6628'] = func_6628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6628_call = mutated_mod.get_global_var('func_6628')
var_6630 = relay.var("var_6630", dtype = "float32", shape = (11, 5, 5))#candidate|6630|(11, 5, 5)|var|float32
var_6631 = relay.var("var_6631", dtype = "bool", shape = (288,))#candidate|6631|(288,)|var|bool
var_6632 = relay.var("var_6632", dtype = "int16", shape = (7, 9))#candidate|6632|(7, 9)|var|int16
call_6629 = func_6628_call(var_6630,var_6631,var_6632,)
output = call_6629
func_6633 = relay.Function([var_6630,var_6631,var_6632,], output)
mutated_mod['func_6633'] = func_6633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5476_call = mod.get_global_var('func_5476')
func_5477_call = mutated_mod.get_global_var('func_5477')
call_6640 = func_5476_call()
call_6641 = func_5476_call()
output = call_6640
output2 = call_6641
func_6646 = relay.Function([], output)
mod['func_6646'] = func_6646
mod = relay.transform.InferType()(mod)
mutated_mod['func_6646'] = func_6646
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6646_call = mutated_mod.get_global_var('func_6646')
call_6647 = func_6646_call()
output = call_6647
func_6648 = relay.Function([], output)
mutated_mod['func_6648'] = func_6648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4567_call = mod.get_global_var('func_4567')
func_4568_call = mutated_mod.get_global_var('func_4568')
call_6649 = relay.TupleGetItem(func_4567_call(), 0)
call_6650 = relay.TupleGetItem(func_4568_call(), 0)
output = call_6649
output2 = call_6650
func_6656 = relay.Function([], output)
mod['func_6656'] = func_6656
mod = relay.transform.InferType()(mod)
output = func_6656()
func_6657 = relay.Function([], output)
mutated_mod['func_6657'] = func_6657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_6658 = func_6009_call()
call_6659 = func_6009_call()
output = relay.Tuple([call_6658,])
output2 = relay.Tuple([call_6659,])
func_6661 = relay.Function([], output)
mod['func_6661'] = func_6661
mod = relay.transform.InferType()(mod)
output = func_6661()
func_6662 = relay.Function([], output)
mutated_mod['func_6662'] = func_6662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6218_call = mod.get_global_var('func_6218')
func_6219_call = mutated_mod.get_global_var('func_6219')
call_6686 = func_6218_call()
call_6687 = func_6218_call()
var_6689 = relay.var("var_6689", dtype = "float32", shape = (7, 10, 10))#candidate|6689|(7, 10, 10)|var|float32
bop_6690 = relay.equal(call_6686.astype('bool'), relay.reshape(var_6689.astype('bool'), relay.shape_of(call_6686))) # shape=(7, 10, 10)
bop_6693 = relay.equal(call_6687.astype('bool'), relay.reshape(var_6689.astype('bool'), relay.shape_of(call_6687))) # shape=(7, 10, 10)
output = bop_6690
output2 = bop_6693
func_6699 = relay.Function([var_6689,], output)
mod['func_6699'] = func_6699
mod = relay.transform.InferType()(mod)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6700 = relay.var("var_6700", dtype = "float32", shape = (7, 10, 10))#candidate|6700|(7, 10, 10)|var|float32
func_6699_call = mutated_mod.get_global_var('func_6699')
call_6701 = func_6699_call(var_6700)
output = call_6701
func_6702 = relay.Function([var_6700], output)
mutated_mod['func_6702'] = func_6702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_6769 = relay.TupleGetItem(func_4542_call(), 0)
call_6770 = relay.TupleGetItem(func_4544_call(), 0)
output = call_6769
output2 = call_6770
func_6781 = relay.Function([], output)
mod['func_6781'] = func_6781
mod = relay.transform.InferType()(mod)
output = func_6781()
func_6782 = relay.Function([], output)
mutated_mod['func_6782'] = func_6782
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mod.get_global_var('func_4250')
func_4251_call = mutated_mod.get_global_var('func_4251')
call_6823 = func_4250_call()
call_6824 = func_4250_call()
var_6825 = relay.var("var_6825", dtype = "float64", shape = (2, 5, 12))#candidate|6825|(2, 5, 12)|var|float64
bop_6826 = relay.bitwise_xor(call_6823.astype('int16'), var_6825.astype('int16')) # shape=(2, 5, 12)
bop_6829 = relay.bitwise_xor(call_6824.astype('int16'), var_6825.astype('int16')) # shape=(2, 5, 12)
output = bop_6826
output2 = bop_6829
func_6835 = relay.Function([var_6825,], output)
mod['func_6835'] = func_6835
mod = relay.transform.InferType()(mod)
var_6836 = relay.var("var_6836", dtype = "float64", shape = (2, 5, 12))#candidate|6836|(2, 5, 12)|var|float64
output = func_6835(var_6836)
func_6837 = relay.Function([var_6836], output)
mutated_mod['func_6837'] = func_6837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6442_call = mod.get_global_var('func_6442')
func_6444_call = mutated_mod.get_global_var('func_6444')
call_6946 = func_6442_call()
call_6947 = func_6442_call()
output = call_6946
output2 = call_6947
func_6953 = relay.Function([], output)
mod['func_6953'] = func_6953
mod = relay.transform.InferType()(mod)
mutated_mod['func_6953'] = func_6953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6953_call = mutated_mod.get_global_var('func_6953')
call_6954 = func_6953_call()
output = call_6954
func_6955 = relay.Function([], output)
mutated_mod['func_6955'] = func_6955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mod.get_global_var('func_6376')
func_6378_call = mutated_mod.get_global_var('func_6378')
call_6972 = func_6376_call()
call_6973 = func_6376_call()
var_6992 = relay.var("var_6992", dtype = "float64", shape = (2, 5, 13))#candidate|6992|(2, 5, 13)|var|float64
bop_6993 = relay.multiply(call_6972.astype('int64'), var_6992.astype('int64')) # shape=(2, 5, 13)
bop_6996 = relay.multiply(call_6973.astype('int64'), var_6992.astype('int64')) # shape=(2, 5, 13)
func_5646_call = mod.get_global_var('func_5646')
func_5647_call = mutated_mod.get_global_var('func_5647')
call_7012 = relay.TupleGetItem(func_5646_call(), 1)
call_7013 = relay.TupleGetItem(func_5647_call(), 1)
output = relay.Tuple([bop_6993,call_7012,])
output2 = relay.Tuple([bop_6996,call_7013,])
func_7014 = relay.Function([var_6992,], output)
mod['func_7014'] = func_7014
mod = relay.transform.InferType()(mod)
var_7015 = relay.var("var_7015", dtype = "float64", shape = (2, 5, 13))#candidate|7015|(2, 5, 13)|var|float64
output = func_7014(var_7015)
func_7016 = relay.Function([var_7015], output)
mutated_mod['func_7016'] = func_7016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6442_call = mod.get_global_var('func_6442')
func_6444_call = mutated_mod.get_global_var('func_6444')
call_7078 = func_6442_call()
call_7079 = func_6442_call()
var_7091 = relay.var("var_7091", dtype = "float32", shape = (11, 5, 5))#candidate|7091|(11, 5, 5)|var|float32
bop_7092 = relay.logical_or(call_7078.astype('bool'), relay.reshape(var_7091.astype('bool'), relay.shape_of(call_7078))) # shape=(11, 5, 5)
bop_7095 = relay.logical_or(call_7079.astype('bool'), relay.reshape(var_7091.astype('bool'), relay.shape_of(call_7079))) # shape=(11, 5, 5)
output = bop_7092
output2 = bop_7095
func_7097 = relay.Function([var_7091,], output)
mod['func_7097'] = func_7097
mod = relay.transform.InferType()(mod)
var_7098 = relay.var("var_7098", dtype = "float32", shape = (11, 5, 5))#candidate|7098|(11, 5, 5)|var|float32
output = func_7097(var_7098)
func_7099 = relay.Function([var_7098], output)
mutated_mod['func_7099'] = func_7099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6661_call = mod.get_global_var('func_6661')
func_6662_call = mutated_mod.get_global_var('func_6662')
call_7144 = relay.TupleGetItem(func_6661_call(), 0)
call_7145 = relay.TupleGetItem(func_6662_call(), 0)
func_4676_call = mod.get_global_var('func_4676')
func_4682_call = mutated_mod.get_global_var('func_4682')
const_7151 = relay.const([9.542714,-5.350772,-0.964597,4.274747,-3.274044,-3.287520,-9.590651,-2.108300,0.557251,-8.369030,1.220163,5.092698,-3.942011,-2.069532,8.022744,9.193960,-1.277442,-2.678513,2.855348,8.460837,-1.672823,-9.285647,4.332849,8.630845,8.569484,4.951586], dtype = "float64")#candidate|7151|(26,)|const|float64
const_7152 = relay.const([1,2,-2,9,-1,9,9,-7,8,8,8,10,-4,-7,6,-3,3,-6,6,-7,2,4,-7,2,-6,1,-10,6,-3,-8,-5,7,8,3,9,-2,7,4,-8,9,-7,-10,1,-8,8,-5,-10,-1,6,-4,-5,7,4,-5,-8,-8,5,9,-3,2,6,4,-10,4,-2,-4,-5,-8,2,1,10,-2,-9,-10,-9,-6,10,1,-7,-7,-3,6,1,7,9,-3,9,-5,8,3,-8,2,-6,-7,8,-4,6,-9,5,-2,5,-5,-1,-5,6,6,-4,1,9,-5,-3,-8,-8,-9,4,-7,-7,3,3,-6,-3,-2,-1,9,10,-9,-2,5,3,-2,5,5,-4,-9,8,7,-8,-10,-3,-10,-2,9,5,3,7,-6,7,-2,2,1,7,-3,8,-3,-4,-5,2,-10,7,5,-1,6,-2,2,-2,-6,-2,5,6,-2,-10,5,-2,-9,2,-4,-4,-2,1,-2,8,3,9,-1,-5,-3,1,-7,7,-5,9,-2,2,-1,10,7,1,10,-7,7,6,-6,-10,-4,-10,-5,-8,6,-1,-2,-10,2,10,-3,3,-8,-10,7,-1,8,-10,2,10,-8,5,-3,-1,-6,7,10,9,-10,-6,10,10,9,-1,-7,-9,3,7,8,-10,-10,6,-6,10,8,3,-3,8,-4,-3,1,8,-7,-7,-2,1,-4,4,4,6,-9,-9,-3,-4,-7,7,-10,-9,9,-4], dtype = "int32")#candidate|7152|(273,)|const|int32
const_7153 = relay.const([[-3.768233,-8.193800,-2.567245,-4.525474,1.717971,-1.717921,8.776330,0.975155,-9.251054,-4.952252,6.471242,4.338520,-5.038338,9.993932,6.143414,5.523280,7.775084,-6.227283,-9.781626,-2.128216,-3.279299,3.245991,-5.451654,3.877767,-7.098010,6.137903,-8.142399,4.581080,8.916737,-8.840140,8.950842,-5.942182,5.985359,-3.418493,5.480404,5.582618,6.862408,-4.979545,0.232866,8.489138,3.688639,8.928274,7.269232,6.747022,7.445773,2.576451,7.882532,-1.802697,5.298238,-7.790956,1.138708,-7.933562,0.617899,-1.154967,-0.627420,-4.782886,-8.881330,-2.719235,-2.174688,-8.278569,7.944376,9.896102,7.613680,0.873644,-7.989184,-5.601505,1.406481,6.931239,1.896465,8.958745,4.880690,3.003650,1.123200,5.015862,1.671171,-5.602986,-4.670797,-8.214718,3.874140,-3.974077,3.250875,8.113438,4.979694,6.526591,-3.343802,-1.158670,-1.498624,-3.356550,2.348535,-5.471615,0.957385,5.593361,-8.281497,-5.552948,3.472816,8.078254,0.568174,8.452527,2.351116,4.358861,0.157645,4.517449,9.411349,-0.334936,-6.901879,-4.933736,6.711247,4.304042,5.713964,8.249082,-9.058225,7.771452,4.389575,-5.202896,-9.536261,-8.215292,2.790044,0.548364,3.040359,-6.536831,-7.309933,-1.143499,-5.063452,9.880651,5.054773,1.162074,-8.895344,0.888615,2.774314,-1.775943,0.318646,-6.852379,3.621757,3.669152,3.012839,-8.111313,-6.647653,7.727408,-2.876092,-2.366905,4.788340,4.422105,9.713388,6.906438,-9.536432,-7.579974,-5.757842,-5.705057,-5.983042,4.805667,5.385801,-0.361668,-0.284515,6.736328,-6.021464,-7.264791,7.713540,1.320327,-7.771948,8.742323,7.598711,-8.370530,-1.921555,7.032972,-3.698703,-1.354177,-7.199398,-5.004992,-6.147396,4.190055,2.601584,-2.591855,7.698026,9.533599,-9.167861,-4.262214,-6.651177,-0.731686,4.595722,-6.686671,-0.950114,-5.621995,2.931046,0.123649,-9.873285,-3.836117,-3.602542,-6.477622,3.660314,1.875269,-5.376373,6.329360,-6.356060,-3.329176,4.200618,5.999893,3.868400,-7.613693,-9.905393,2.153008,-2.379003,0.536956,-9.287694,-0.413844,7.738567,-3.063537,4.158961,3.577975],[9.526056,8.077262,-8.490093,-6.486059,-4.104223,-8.833305,-5.339730,0.726475,1.597090,1.870887,-6.433645,0.348852,9.358347,-0.913153,5.721658,-9.455887,5.949614,2.324642,-5.469396,8.645688,-4.034719,-0.343986,7.778147,8.602694,-6.388583,1.014342,-5.349693,-5.394431,-8.355422,-7.373328,-7.490416,-4.994086,6.297760,4.366265,7.892957,-1.059277,-5.923090,-4.850346,2.768323,8.863244,-1.333451,-5.474483,9.064357,-6.146190,5.388388,-3.022544,6.746552,9.481128,-0.547165,-7.915974,-7.685169,-2.625607,9.951854,-9.651475,-1.744090,-6.946567,-4.920550,-0.649530,-0.602781,0.376869,0.954311,7.258425,-8.653722,5.037878,-0.791935,-7.676765,3.845510,7.767686,3.911582,6.784229,7.916883,-2.217365,-1.949049,-1.965490,4.578963,5.755713,0.014333,2.400555,7.780176,-4.122175,1.981879,-8.241090,6.283395,9.376825,-4.122815,7.446362,4.183184,0.492208,-7.621945,-3.464524,-5.978703,-5.285227,-3.197611,3.347430,8.735473,9.006616,8.731464,6.936486,-4.264293,7.548406,3.650737,-1.699209,6.857259,-0.349293,9.726174,9.138838,-6.766410,9.392151,-9.870296,0.216686,5.710271,-9.826583,-1.599733,9.251872,-5.590832,0.652245,4.770139,-8.638445,-5.806784,-6.951961,2.450227,6.534408,-6.739422,9.958694,0.524240,-7.195327,8.199891,2.453209,-8.620621,-2.712724,-7.253382,-3.264672,-9.872774,-2.602761,3.013012,-5.371195,-1.460954,0.401744,4.115993,8.581419,6.837020,2.419789,-8.352849,-0.890933,9.867175,-7.747596,2.747460,-7.183595,0.437698,-8.678937,0.296113,-8.970070,-5.823701,-2.076594,-3.891726,-4.400054,9.134166,-4.419512,7.805727,-6.022553,-5.146920,-1.658340,3.790828,9.272909,2.828130,-0.617024,-1.146280,-8.303610,-6.536933,-0.293186,3.512925,-1.329205,-2.503667,-8.697274,2.779866,8.594798,0.127386,1.730323,-3.789053,-4.374679,-5.565656,-4.869515,6.451446,2.802171,-1.682292,-6.222629,8.168665,-0.550655,0.688002,4.527962,-8.513725,-5.810563,-6.703797,-9.802215,-6.284856,-0.294020,7.044501,-0.329346,8.538976,-8.041513,6.444835,1.945900,2.630035,8.095813,4.584675,-7.776277,7.727873,1.539787],[-6.884618,-9.241226,-7.759191,-1.928990,7.134917,-0.451543,-9.097577,-4.272586,2.870092,-3.391680,-0.213937,-1.901483,-5.434512,1.513475,4.928931,6.848178,-4.436248,1.968185,-5.209289,8.851788,-7.940711,7.232905,-5.801619,-4.330334,8.781971,2.432482,-7.348466,7.418659,-5.453724,-4.572609,-3.736869,3.359957,0.064237,4.193399,-7.274221,-3.300579,9.845143,-3.225318,7.351190,2.672434,9.828315,-1.572631,-9.513637,3.973357,-8.441568,2.496366,5.233895,-6.315308,8.576702,8.819937,-3.622461,-2.064329,4.015048,9.220124,6.715395,3.150802,7.933120,1.709147,-4.550343,-0.610606,-4.284754,0.656331,4.510921,3.310417,2.446899,-0.878359,-6.697333,3.579537,8.136758,-3.989084,-4.196621,-9.565539,-1.959933,3.690140,-4.068561,0.910069,5.047318,-2.799318,-0.469838,3.877175,-3.713941,0.071877,-1.702135,-6.886382,-7.490866,0.441956,4.604903,-2.397493,0.206154,-2.418622,-3.847946,-5.972853,-0.241920,-2.844053,-0.709355,-2.476560,4.186243,1.435335,8.665052,-4.645141,4.849711,-2.448386,9.498457,-7.626382,-3.480596,-0.180901,-9.683139,5.511176,0.571452,-1.537243,7.195249,2.464408,-8.246839,9.960576,-8.208955,6.642123,4.389584,-4.799723,4.052974,2.582836,7.104363,-7.341842,-4.051816,-5.031997,5.510070,-3.030496,-6.392037,2.918495,-0.896245,-2.774061,-9.635846,-8.933807,6.976131,-7.542667,9.600728,-0.039217,7.490276,7.621969,-5.972724,-2.600270,-9.596312,2.115143,-6.565019,5.458272,8.036361,3.667946,-5.088794,8.002749,4.310811,-3.972231,2.040379,4.867596,4.573300,-7.689949,5.432521,4.225824,1.946004,-0.069767,8.334148,4.600489,5.117992,3.796731,-2.994133,4.819962,-2.946639,8.995017,-2.976702,1.853182,1.635695,-5.238244,-9.437140,-2.306680,-6.385696,3.704648,-8.151565,-1.232022,9.808205,1.596804,-7.138497,7.264002,-0.632026,-0.397196,-7.754380,-6.018718,8.580323,-7.264535,-1.093867,-0.188678,3.557160,5.911844,-7.045347,7.169160,8.869303,7.936961,6.491527,-2.424236,8.566928,-4.466309,-7.178338,7.413135,8.640229,9.050968,-3.069558,-2.345100,5.745382,-2.047621,7.939410,-4.706638],[-4.069278,-3.310187,-5.155822,-6.264354,2.671171,4.933216,9.644919,-7.949982,-4.212912,0.540556,8.708014,-1.924528,3.989770,-7.071107,-9.315361,0.749052,-5.078757,-6.802922,-0.182672,9.384739,-0.191282,-6.745564,4.881150,-3.225181,-2.567503,2.366659,-2.278213,5.159158,-9.734884,-4.610743,-0.945304,0.536627,-3.658074,1.235878,-6.132779,-4.390677,-8.031457,1.793548,4.775918,8.611887,8.361773,9.845749,8.215966,7.319507,-5.826937,-1.859243,4.418411,-4.408839,-7.640213,-6.917697,-8.359171,0.929423,4.894180,-6.211167,-5.633132,3.945429,-1.829427,7.040369,3.457387,9.336367,8.692242,-2.614021,-3.089789,-3.226428,-4.289418,4.130350,9.520486,7.917877,8.067132,-8.428589,-7.603323,7.468054,-5.040313,-3.706229,6.529402,-7.072296,5.298221,4.827373,1.016968,-9.251923,6.066206,-6.321692,-0.367816,3.893339,0.437209,-8.432209,1.976520,2.150263,-5.869107,5.501857,4.136285,-3.614252,-0.116418,-7.009249,6.625325,-5.463744,9.158945,-9.063838,-3.536269,0.898478,6.173424,7.122621,-7.862238,-6.174392,-1.495701,-6.695558,2.378639,2.456339,1.471183,6.395415,-5.329259,8.379836,-6.939531,-7.672615,2.043211,5.212607,6.778762,-4.699546,2.747304,-9.038584,-7.990227,6.002076,-9.714878,-6.549413,2.463801,-6.303635,4.803832,1.750003,0.783374,-0.596689,7.231302,5.318733,2.617324,-0.601437,5.464005,-6.979404,-4.551015,6.710709,-4.446291,-4.752468,-5.357926,-3.351058,-6.958902,2.731396,7.824861,-0.631083,3.834580,0.171437,2.748047,4.473669,-3.223228,0.613952,-9.889222,8.577037,-6.317804,-7.101071,8.522720,-0.707178,-5.058520,0.316466,4.534263,-4.988990,-2.978641,6.122132,-0.127941,-3.370537,3.035851,4.247226,-0.147064,-8.382878,-7.335863,8.070360,6.789715,2.002585,-0.217000,5.605592,-1.659902,-8.420699,1.417606,7.220624,8.714131,1.028670,6.658588,-0.099186,0.948737,-3.886313,8.706050,8.974392,2.125240,-5.015524,-2.764720,5.105465,6.012933,0.197487,-9.990863,-9.381380,-1.042581,-4.934084,-0.588066,9.269779,3.993983,3.988580,-1.671036,-8.114147,1.176227,7.763889,-6.386776,5.366142]], dtype = "float64")#candidate|7153|(4, 208)|const|float64
var_7154 = relay.var("var_7154", dtype = "int16", shape = (63,))#candidate|7154|(63,)|var|int16
call_7150 = relay.TupleGetItem(func_4676_call(relay.reshape(const_7151.astype('float64'), [26,]), relay.reshape(const_7152.astype('int32'), [273,]), relay.reshape(const_7153.astype('float64'), [832,]), relay.reshape(var_7154.astype('int16'), [63,]), ), 0)
call_7155 = relay.TupleGetItem(func_4682_call(relay.reshape(const_7151.astype('float64'), [26,]), relay.reshape(const_7152.astype('int32'), [273,]), relay.reshape(const_7153.astype('float64'), [832,]), relay.reshape(var_7154.astype('int16'), [63,]), ), 0)
func_5915_call = mod.get_global_var('func_5915')
func_5918_call = mutated_mod.get_global_var('func_5918')
const_7157 = relay.const(1, dtype = "uint64")#candidate|7157|()|const|uint64
call_7156 = relay.TupleGetItem(func_5915_call(relay.reshape(const_7157.astype('uint64'), [])), 4)
call_7158 = relay.TupleGetItem(func_5918_call(relay.reshape(const_7157.astype('uint64'), [])), 4)
output = relay.Tuple([call_7144,call_7150,const_7151,const_7152,const_7153,var_7154,call_7156,const_7157,])
output2 = relay.Tuple([call_7145,call_7155,const_7151,const_7152,const_7153,var_7154,call_7158,const_7157,])
func_7162 = relay.Function([var_7154,], output)
mod['func_7162'] = func_7162
mod = relay.transform.InferType()(mod)
mutated_mod['func_7162'] = func_7162
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7163 = relay.var("var_7163", dtype = "int16", shape = (63,))#candidate|7163|(63,)|var|int16
func_7162_call = mutated_mod.get_global_var('func_7162')
call_7164 = func_7162_call(var_7163)
output = call_7164
func_7165 = relay.Function([var_7163], output)
mutated_mod['func_7165'] = func_7165
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7187 = relay.const([[[2.304680,-3.405013,-4.178882,-5.702365,1.065217,-8.053772,4.784892,8.641279,1.426624,0.829513,0.761895,-6.437568,-5.737177],[1.364564,-6.943446,0.189844,6.973802,1.858456,-3.235625,-3.646587,3.763567,9.673296,-2.644271,-3.861018,-4.075770,7.409050],[-9.569025,0.685041,-0.780440,-2.997905,6.120323,6.857670,-4.231296,-5.608787,-1.088807,-4.716626,2.367395,9.201040,-4.979585],[5.213660,2.118373,6.619750,6.540957,-5.342327,4.730504,-1.728960,9.246326,9.267838,-2.202845,-6.503141,-1.400623,-2.225887],[-0.743459,4.408249,-7.622775,-7.624609,5.020306,9.063866,-4.226411,0.417109,-4.848984,-1.096299,5.818421,2.314799,6.331796],[-5.003660,-2.045538,-0.896192,-9.929406,-5.531409,-3.885718,6.324360,-2.552670,-1.842895,-6.137435,-4.447358,5.776803,-2.043637],[-0.411315,2.736849,-7.398087,1.265257,-4.529610,7.579141,2.097403,2.255689,-1.415867,-6.110521,0.738866,5.013813,-9.019600],[2.329654,-1.693997,-4.375313,7.093843,7.087042,7.186001,0.193870,-1.131051,6.011054,-2.051851,5.370082,1.895871,9.296198],[9.638138,-1.724581,-9.458324,2.326768,-6.420217,5.316714,9.687410,8.456500,9.250219,3.812511,2.334809,2.096116,8.894562],[4.423196,-5.916906,-8.833138,2.223579,2.598989,-7.175508,8.526789,-1.372187,-9.323699,2.897057,6.168052,-3.181044,-5.312374],[5.331368,4.267838,-2.911758,0.378752,6.887446,-9.495845,-1.664200,-7.564234,5.885466,8.370631,-1.724363,2.801130,6.555332],[-4.221891,1.312043,-6.021749,4.761284,-0.974617,-2.123018,-0.529964,6.257068,-8.232557,7.006313,-4.575493,-5.916628,-5.145545],[2.135458,-2.555817,-6.694483,4.382398,6.793277,-3.339403,3.981279,4.210336,-8.889973,-4.487311,-7.950237,-1.753411,9.644074],[-2.588041,-8.722540,2.110795,6.559535,7.718224,-0.527707,6.150437,-0.046478,-4.090999,-8.478922,9.476966,-3.777394,-9.867488],[-0.053892,-9.025539,4.738178,-0.383510,8.487837,-2.331508,3.987136,5.076858,-6.940930,-5.773250,-8.654399,-8.896988,-3.201706],[-6.086736,8.795599,5.734085,9.122914,-5.292315,0.859184,-1.271744,-2.691747,4.353767,-3.211241,1.361928,1.441990,5.467485]],[[0.161388,0.123305,6.562094,-0.643450,-1.872379,4.417934,9.450179,2.499351,-6.071439,1.214894,-9.895844,-9.128423,1.865566],[1.445372,1.742364,2.328623,-6.514103,-3.085706,-3.382201,9.006745,2.116523,-6.474274,-9.076400,5.205068,5.451221,5.315412],[1.169394,3.977941,5.807985,9.804544,8.638250,2.093147,4.261307,-0.977891,-6.499172,8.082045,-7.352510,-9.192719,9.439442],[2.541184,3.483529,-0.333329,-7.337700,8.733642,-8.765136,7.056863,8.889725,9.674502,-5.344782,-5.904811,3.945592,-4.698171],[9.498322,-3.157277,-0.271657,-2.776527,-8.459496,-2.647320,-6.417799,5.697827,1.045992,-8.705042,6.359080,2.889726,6.749016],[4.176199,7.462631,-4.119419,-8.121120,2.344234,-8.201974,-5.727108,-4.487338,-9.683992,1.535181,2.206801,-9.150132,8.526555],[-1.507649,1.792093,8.398253,-9.556260,9.188607,8.913890,-8.856449,-7.811683,-3.948929,3.303249,-4.350195,2.697168,3.191186],[-8.898247,5.817521,-0.125965,-5.227187,7.459988,-3.334585,3.423158,7.411481,1.946388,1.078970,-8.205944,4.429976,5.667967],[1.373317,7.188379,6.721617,-9.835556,0.043297,-4.245625,8.095607,3.158689,-7.925676,6.935623,-0.954797,4.109069,-3.902454],[4.816387,8.659746,4.310181,-6.688575,-4.048664,-2.433810,-5.546226,8.174920,-7.427734,-3.832999,-6.811778,-5.031874,-3.451224],[-9.590939,-1.200365,-8.929210,-4.019218,-0.247250,-4.820456,-2.912467,1.010202,-9.849488,8.128077,-7.182397,-2.698798,7.185824],[0.654127,-6.882752,-9.364231,8.082360,8.222713,4.638350,-4.078186,-4.595706,-6.000199,7.117636,6.205595,0.887604,2.877015],[-6.407707,-9.763785,-5.504487,6.321067,-0.736538,9.364044,9.126632,1.978963,6.479126,-6.707777,-8.762632,-5.897557,-7.085476],[4.227072,-5.986039,-0.745031,-5.111446,0.681914,-1.115088,9.723326,-9.367237,3.286994,-7.414375,-9.516770,-9.002014,9.671712],[5.625770,-4.596062,7.364274,8.621600,-4.741916,7.108826,6.579340,1.518042,3.263941,-7.580908,7.966168,1.747552,-2.969493],[1.681874,7.108871,8.179304,3.792935,-1.340249,-5.576427,-6.365194,3.125551,3.061998,-5.960901,9.752238,-7.973969,-8.235273]],[[3.453743,5.904848,6.506691,-0.713768,4.676574,-5.567725,7.059804,1.235960,-5.369747,-1.600606,2.801291,-8.476601,-0.200484],[-2.752467,3.202983,-5.604908,-9.536555,-6.328441,9.369081,-7.152886,8.471003,1.111145,-0.571804,-5.807426,-4.152948,-7.235779],[-7.640259,-1.166470,-8.843673,8.630372,1.286968,-5.296697,8.402972,3.144775,8.678093,9.867253,-2.756048,5.485723,-0.125333],[-1.846838,-4.422571,-3.163005,6.855198,0.999764,4.803914,-1.417770,6.670276,9.311831,9.924167,8.313069,-7.657945,1.574301],[1.877954,1.540177,-9.590745,-8.712827,5.796645,-6.070935,3.306662,-6.404499,-1.300732,8.959459,-9.474127,2.441600,-2.258065],[-2.986126,2.887045,9.615347,0.466672,-1.587180,-0.716161,-0.664833,-5.297692,8.478378,1.378119,-8.898677,-9.980038,3.845482],[-7.642682,-5.370917,4.636727,-7.698879,9.725029,8.757681,-9.112409,-7.546742,-3.193007,-1.313616,2.176498,8.219637,-1.897645],[5.339771,7.276547,4.418519,4.123144,-6.485631,-3.683746,3.034105,9.542635,-7.368041,0.554724,-5.423945,-5.771900,-0.022309],[-1.977342,-6.461096,9.197895,0.889776,-6.907194,4.018519,4.940180,-2.968897,-6.156067,5.884099,-8.007613,3.522160,-3.530434],[3.537242,1.624906,4.605219,1.686053,-7.167663,6.090780,-2.500320,-2.770984,6.134564,7.911686,0.691548,4.448670,6.747605],[8.416931,8.766803,0.119211,-3.043984,-3.152485,-5.949156,4.066794,9.720524,8.382402,-2.863393,1.456934,3.425061,1.583936],[-5.993090,5.612755,-3.035478,-0.564382,-4.397161,-7.763426,-7.239936,-3.698285,7.340637,0.108259,-3.991596,-2.548841,-4.210760],[-7.153423,-5.908234,7.614230,5.252481,1.588594,5.933366,7.156493,0.877852,-7.672963,0.335497,-6.103158,-7.958120,2.183896],[-2.404759,8.902280,8.314166,-5.817915,3.620552,-1.180884,-1.139818,-6.981175,3.427185,-7.919932,6.355833,9.407570,8.043037],[6.864981,0.400630,2.429762,-7.522587,0.044012,-6.341867,-6.211929,0.753775,-1.563326,-2.798723,7.035820,6.731941,-3.373430],[-5.414613,6.113361,8.256081,4.849826,5.762648,0.591203,3.532933,0.872292,-0.351469,6.940166,-2.742613,-9.677522,-5.856357]],[[-8.344443,1.672684,-3.842915,-7.112879,8.589482,9.233146,9.920767,1.378130,-3.584678,9.209344,9.312337,6.860764,9.118523],[-9.068085,-5.678316,0.268569,-5.807527,2.025578,-2.019298,-1.616772,-1.604046,-2.808294,-7.004793,-5.548366,-1.983971,-1.111362],[9.319276,-6.996565,4.230431,-3.886622,9.995566,6.644232,-9.369259,-7.612289,-4.982013,4.928854,-9.055638,-3.365367,0.986187],[-4.881914,-6.350419,4.229663,-8.322588,-7.490198,7.682726,-6.399678,-8.559947,-3.314251,-1.620998,2.545173,-1.051309,6.333854],[-7.991581,5.848186,-9.250864,3.145339,3.457506,8.048840,-8.296080,0.795167,-2.815495,-3.798052,6.695740,-9.239470,-3.393596],[0.799146,-6.201685,3.687616,-9.594596,-3.076358,-4.248831,-0.896001,9.345772,-3.792565,7.286275,9.631457,5.928680,3.289398],[-4.036012,-8.781685,3.608284,0.528108,4.763867,1.995455,-0.410388,-2.149460,7.141186,-6.531799,-0.025999,7.982459,-3.854912],[-1.153867,-6.832103,8.468225,8.596764,0.084279,7.343903,-0.553947,-7.174519,-6.622825,6.551840,9.416591,3.468971,6.272107],[-7.339640,-2.429926,2.099152,-6.300716,-6.682641,7.886214,-8.760404,-6.714607,6.073069,-2.312057,-4.048858,-3.218027,5.170335],[2.849463,8.647583,2.070845,9.288724,5.393954,-1.773593,-5.612101,8.461939,-6.684782,8.216429,4.769937,5.224319,-1.105495],[-3.210599,7.463663,-1.892774,9.496875,-9.891915,-6.684036,-1.518201,-0.936067,3.939193,5.940668,-3.250397,-0.556045,-8.878768],[5.581607,3.123837,-0.347485,-1.095146,-0.586324,-7.214026,7.481606,-8.242803,-9.319373,3.811058,9.762385,4.564677,0.281736],[-0.399855,6.706735,3.031825,-1.748558,-4.658988,-7.307409,-2.635201,-5.231561,-3.140624,9.696745,4.272353,5.708489,7.930159],[3.608600,7.385229,-7.163040,0.170367,6.887495,-4.415920,0.351750,-2.289062,-9.053897,-2.448829,2.629924,-1.343086,3.967487],[-4.048682,-9.994118,9.191129,-7.981208,-9.023732,-4.539951,1.017757,-8.301544,5.078840,-5.240766,7.287986,8.979217,7.366802],[9.105316,5.020419,9.306867,9.288249,8.304482,-6.104313,-3.912331,3.892911,-3.925530,-0.699061,-3.753647,-8.113290,1.312538]],[[7.046920,-1.386870,2.249221,-2.329848,-9.128724,-6.297165,9.023687,6.473540,1.906012,-8.886535,-7.584193,9.040872,2.306585],[1.815833,0.919562,-4.093151,5.444834,0.006117,-5.184988,8.638235,-0.362433,-4.866091,-6.912278,9.802563,7.396585,-5.960653],[-7.705912,-7.376200,0.211644,2.970733,-6.604020,-7.665717,-3.755581,-3.861307,4.261905,-9.324571,0.744532,-9.559095,-3.135014],[-7.094880,5.128687,2.505580,-7.586061,-7.090866,7.046577,-6.119388,0.355138,5.798636,7.580552,-4.855704,-4.246511,-6.314384],[9.358310,9.606475,-0.502211,-7.570479,-1.660233,5.968544,7.782320,-2.730205,3.530542,6.809122,8.774257,2.827981,-8.039321],[-9.108497,-5.990568,0.640110,7.906772,6.400018,-6.859140,5.629705,7.153121,9.468262,-8.070778,-5.455829,6.155829,-4.354661],[-0.793223,0.956015,8.439096,4.496558,-5.828239,-7.905567,1.898279,2.126999,7.581215,-4.118208,3.679449,4.451779,-7.479774],[0.937040,6.233545,-2.942919,5.403579,6.980339,4.897628,-3.501008,4.934781,3.225934,-2.428013,-3.526300,-8.379060,2.964752],[-7.507008,6.321555,-5.786123,-5.922205,8.189814,1.331436,-4.926792,5.173148,-3.300918,8.943931,-9.150927,-8.839768,4.258471],[-3.562940,-0.691982,3.630163,3.526795,6.322967,-7.005072,0.158802,-5.153082,-6.013789,5.637993,9.842243,-7.083284,2.256518],[1.028565,4.513338,-9.311585,-3.664972,2.840370,-0.666610,3.783502,-6.651026,3.694152,9.060080,5.266122,7.647860,6.415281],[-0.176360,7.628859,5.453786,7.364995,-9.279855,-3.000383,-0.904319,-9.525875,-3.644497,-4.172369,8.509105,1.940554,-1.464326],[0.031998,2.214131,-4.854563,-0.972269,-1.384253,-9.299095,-9.107596,9.873123,-2.212016,6.645350,-6.985013,-7.948868,-0.386223],[3.071648,-8.837770,-8.399417,4.220107,-2.929440,8.398859,0.412065,-2.925975,-5.748217,-5.355248,-4.639410,8.232128,-8.882997],[8.838854,6.348666,-8.169495,3.418151,-2.423943,-4.361222,-0.191346,9.314161,0.730472,7.402775,-5.988642,0.837801,5.344675],[7.314185,4.406297,9.700808,-6.080609,-8.697849,4.130962,3.579722,-0.801222,9.880170,9.783659,-5.490722,6.525038,-1.149220]],[[3.887098,2.023819,2.071129,-4.575201,-4.252442,-8.313653,-7.675477,7.297429,-7.480054,3.923210,3.333780,3.532828,7.019461],[0.488681,8.980365,-5.348750,9.076614,-1.110706,0.254021,5.838210,-4.598163,-9.981902,9.669415,-2.781761,4.628522,-1.983345],[-1.040375,5.226894,1.325599,-9.942472,-6.813877,-5.538605,-6.191188,9.212658,7.163145,8.891636,-1.828266,-8.445194,-2.503388],[5.875938,-5.932846,-6.758145,-3.405605,-5.446563,-7.859684,-5.543221,8.554039,0.097974,2.113892,4.319781,7.131836,-9.313548],[8.845504,3.030792,7.527688,5.107483,-1.178911,-1.736587,3.708516,6.179785,-9.173572,-3.074105,-3.462551,7.239245,-7.917768],[-4.858626,-4.158902,6.483414,0.591182,1.728159,-1.568107,-4.953025,-5.344013,4.269449,9.211986,1.136364,-6.161471,6.404876],[0.867582,9.462069,-5.237139,-1.344328,-9.243971,-9.846518,-5.293786,5.383958,-8.124124,-2.936782,-1.986923,-5.149818,-9.869813],[9.928434,9.147158,9.487099,-6.042204,5.318302,-5.354887,0.175674,8.324013,-4.919540,3.945585,-9.557918,0.495308,-9.373421],[-6.024737,9.645339,-3.022615,-1.177081,1.814612,3.749654,-6.495839,-4.034778,-6.649611,6.737862,3.476411,3.203597,6.640872],[-4.736303,-5.276060,6.210308,1.223395,3.225138,2.785615,-4.471438,0.381251,-8.247948,-5.089296,-6.306872,-7.630501,-4.998028],[9.999680,-3.684394,-2.525154,7.521086,4.128430,3.252146,2.138077,2.459098,-5.749848,-2.217377,2.305022,9.342209,2.049619],[-3.791732,-7.705310,-3.188344,-9.524483,-8.680800,4.774938,-8.925972,-0.549951,-8.195771,-0.775793,9.162458,5.442483,7.490781],[-9.621267,-4.502887,-6.109912,-2.965539,4.810474,1.163139,0.229856,-1.735729,0.233312,-5.036416,9.018867,-3.989552,-6.971634],[-3.447461,9.162204,-1.144843,3.553911,9.515033,8.803686,-2.234021,-8.162281,-5.576690,6.377583,8.140023,5.285949,6.270201],[-2.463183,9.824675,6.706601,-6.350025,3.714002,-5.274112,5.317919,-0.032856,7.600131,8.323654,-6.607979,-7.627075,2.165659],[2.391902,7.818954,0.554964,-7.836558,-7.598425,-5.865771,-0.123647,3.059274,-5.714781,-5.173419,2.955064,4.123963,-0.458308]],[[-2.342765,-8.264685,-3.095052,2.913148,-0.145445,1.464664,6.556624,-5.642969,-2.892803,8.848460,4.790640,-2.358678,-4.109558],[-9.000135,-6.181098,-3.274285,5.907133,-8.774299,-8.522098,6.230324,-3.013775,8.869363,-9.160540,-5.302519,-1.051959,-3.683465],[8.390109,5.554405,-3.021715,-1.541821,-3.833201,4.482664,3.414622,1.724214,5.603904,-4.952710,2.118102,5.876232,6.814355],[-6.760123,2.307852,2.959715,4.248544,4.570004,-6.328083,2.932112,-3.644888,-6.175939,-0.002612,7.598764,-3.125748,-0.696636],[7.512565,1.880056,0.857637,-8.746793,-4.255448,3.678859,-5.405040,1.420665,-9.379427,-6.892624,-1.933801,-8.458356,-2.840552],[-4.217483,6.903480,1.212819,9.694441,1.725578,-4.175859,6.985435,-1.720533,5.210320,6.725072,6.937235,6.264229,-9.758058],[7.393864,-9.723460,-9.685273,-7.342306,8.510162,-0.476876,1.165308,2.701063,5.845044,-8.205214,-4.987723,1.589760,8.229646],[9.124429,-8.237269,-6.024109,7.598146,4.316368,2.791892,8.671566,5.714080,5.910552,-5.569109,3.634393,-8.157540,2.706291],[5.806341,-1.961305,8.170746,0.842686,-6.380581,7.539348,-0.238387,7.463018,3.117763,0.912089,4.991694,5.250171,9.852694],[8.445610,-4.326770,-2.879801,2.585082,-3.313979,4.124234,-4.172217,2.676252,1.979831,5.780482,-3.260352,3.290644,6.816566],[-3.703201,-7.004133,7.213535,3.565834,-1.269753,0.992471,1.211515,7.527344,1.018891,-5.396091,7.164866,3.411230,-2.018817],[4.331262,7.039268,-1.347103,9.606759,2.877494,7.477534,1.891187,4.636341,5.618207,-9.088347,0.658679,9.785307,1.696252],[9.405488,4.709412,-3.109733,6.283725,3.167664,5.611118,9.419758,-7.287296,-7.080331,-9.909345,-1.743221,-4.348905,-0.102869],[3.447392,8.030815,0.113108,3.581010,-2.001741,7.214069,1.006593,-6.894074,-8.788829,9.031579,-5.741506,-4.957081,1.357402],[-0.663378,2.727031,5.951264,-1.922612,4.960429,7.333936,-1.226826,-0.372016,-9.578168,8.718793,2.285410,-5.860150,-8.910763],[-6.334121,5.020366,7.383107,3.727342,5.074839,0.511863,2.885960,0.676459,9.889461,-5.457638,5.336254,3.264346,7.833462]]], dtype = "float64")#candidate|7187|(7, 16, 13)|const|float64
uop_7188 = relay.erf(const_7187.astype('float64')) # shape=(7, 16, 13)
output = uop_7188
output2 = uop_7188
func_7192 = relay.Function([], output)
mod['func_7192'] = func_7192
mod = relay.transform.InferType()(mod)
output = func_7192()
func_7193 = relay.Function([], output)
mutated_mod['func_7193'] = func_7193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5646_call = mod.get_global_var('func_5646')
func_5647_call = mutated_mod.get_global_var('func_5647')
call_7225 = relay.TupleGetItem(func_5646_call(), 1)
call_7226 = relay.TupleGetItem(func_5647_call(), 1)
var_7238 = relay.var("var_7238", dtype = "bool", shape = (7, 13, 3))#candidate|7238|(7, 13, 3)|var|bool
bop_7239 = relay.divide(call_7225.astype('float32'), relay.reshape(var_7238.astype('float32'), relay.shape_of(call_7225))) # shape=(7, 13, 3)
bop_7242 = relay.divide(call_7226.astype('float32'), relay.reshape(var_7238.astype('float32'), relay.shape_of(call_7226))) # shape=(7, 13, 3)
uop_7253 = relay.log2(var_7238.astype('float32')) # shape=(7, 13, 3)
output = relay.Tuple([bop_7239,uop_7253,])
output2 = relay.Tuple([bop_7242,uop_7253,])
func_7255 = relay.Function([var_7238,], output)
mod['func_7255'] = func_7255
mod = relay.transform.InferType()(mod)
var_7256 = relay.var("var_7256", dtype = "bool", shape = (7, 13, 3))#candidate|7256|(7, 13, 3)|var|bool
output = func_7255(var_7256)
func_7257 = relay.Function([var_7256], output)
mutated_mod['func_7257'] = func_7257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5476_call = mod.get_global_var('func_5476')
func_5477_call = mutated_mod.get_global_var('func_5477')
call_7312 = func_5476_call()
call_7313 = func_5476_call()
output = call_7312
output2 = call_7313
func_7326 = relay.Function([], output)
mod['func_7326'] = func_7326
mod = relay.transform.InferType()(mod)
output = func_7326()
func_7327 = relay.Function([], output)
mutated_mod['func_7327'] = func_7327
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7345 = relay.const([[[0.013661,2.236813,-3.951402],[9.452329,-4.009065,5.473132],[5.690283,5.828592,5.089424],[3.796431,6.282273,8.317487],[-2.831659,-1.743618,-7.820122],[3.111437,9.408663,4.833630],[5.118992,-3.819398,-3.981466],[-8.797914,4.372316,4.262815],[-4.937800,-0.153530,-1.143794],[1.156908,-7.170747,6.075834],[8.018630,-9.887504,3.763597],[1.595802,2.901876,-0.829064]],[[0.261550,4.492377,-6.692836],[-3.305176,-9.574402,8.905208],[-9.561254,1.284702,-1.161200],[4.219325,4.443245,-4.599534],[6.068363,-2.064527,3.769894],[5.580861,1.505202,-0.447925],[5.859311,-8.137085,0.832157],[-1.830811,-6.958416,-6.175169],[-2.607597,4.813242,-2.207328],[-0.646086,8.183463,-9.333711],[0.683325,9.908366,-9.734516],[3.093017,-5.665667,3.421418]],[[0.809047,0.917454,-6.902168],[-2.370017,-3.067802,-5.158250],[3.905631,-0.679788,8.067694],[-2.265400,-1.743658,9.426636],[6.210012,-6.772241,8.835882],[7.059757,-4.333475,-6.998654],[1.425194,4.580038,-4.131370],[-6.373450,6.095396,-7.908210],[2.384980,5.624174,5.235844],[-4.873909,3.281850,-1.621875],[5.848089,5.101419,0.198834],[-0.819098,-2.319170,-1.558262]]], dtype = "float32")#candidate|7345|(3, 12, 3)|const|float32
uop_7346 = relay.sqrt(const_7345.astype('float32')) # shape=(3, 12, 3)
func_4291_call = mod.get_global_var('func_4291')
func_4294_call = mutated_mod.get_global_var('func_4294')
var_7350 = relay.var("var_7350", dtype = "int32", shape = (273,))#candidate|7350|(273,)|var|int32
call_7349 = relay.TupleGetItem(func_4291_call(relay.reshape(var_7350.astype('int32'), [273, 1])), 2)
call_7351 = relay.TupleGetItem(func_4294_call(relay.reshape(var_7350.astype('int32'), [273, 1])), 2)
output = relay.Tuple([uop_7346,call_7349,var_7350,])
output2 = relay.Tuple([uop_7346,call_7351,var_7350,])
func_7355 = relay.Function([var_7350,], output)
mod['func_7355'] = func_7355
mod = relay.transform.InferType()(mod)
var_7356 = relay.var("var_7356", dtype = "int32", shape = (273,))#candidate|7356|(273,)|var|int32
output = func_7355(var_7356)
func_7357 = relay.Function([var_7356], output)
mutated_mod['func_7357'] = func_7357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7192_call = mod.get_global_var('func_7192')
func_7193_call = mutated_mod.get_global_var('func_7193')
call_7374 = func_7192_call()
call_7375 = func_7192_call()
func_6699_call = mod.get_global_var('func_6699')
func_6702_call = mutated_mod.get_global_var('func_6702')
const_7384 = relay.const([[-0.713949],[2.400167],[4.423252],[-5.569818],[-8.178437],[-0.816412],[-4.409535],[9.159925],[2.157697],[6.036806],[7.460594],[-3.082956],[-6.957284],[3.970673],[-0.009832],[-9.613174],[-0.859446],[7.516360],[-8.863272],[8.813076],[2.524539],[-2.125983],[8.055872],[9.445575],[-0.716004],[-4.912622],[-7.291308],[2.165654],[-1.554988],[1.221405],[-5.192629],[5.935162],[8.890011],[2.111037],[-4.637705],[-7.979307],[-6.510768],[0.537039],[-5.817664],[-8.222124],[-7.777504],[-5.192722],[3.573007],[3.830652],[-3.373827],[-6.518705],[-1.103579],[3.821996],[-4.941716],[0.600716],[-8.599171],[-4.524861],[-5.758332],[-6.924925],[9.540126],[7.385809],[-2.670259],[-4.730313],[7.599478],[9.543392],[-1.742983],[-2.576932],[-5.089356],[-3.637723],[-0.235039],[6.094877],[-3.444549],[-6.009698],[-4.382539],[6.866814],[6.086133],[7.910592],[7.878365],[-2.744496],[3.693698],[-9.438622],[9.483210],[-1.137040],[9.420735],[4.986342],[-3.719787],[-1.237540],[-9.334073],[2.693315],[0.364280],[-4.197825],[7.788526],[-8.810724],[1.221614],[5.078203],[4.229843],[-1.248134],[-6.363733],[-5.529863],[-6.494496],[-9.072132],[-6.139019],[9.939999],[4.297770],[9.361818],[9.351672],[4.708860],[1.567298],[7.376077],[-6.616118],[6.728595],[4.680222],[1.424698],[-8.828914],[0.800272],[8.406169],[1.653213],[-8.400025],[-3.880301],[4.850999],[-5.418707],[-9.655229],[8.480928],[-9.282662],[-2.485881],[7.351618],[-0.154223],[-7.184023],[6.686312],[3.613374],[7.260779],[-9.024331],[-4.414398],[4.019135],[-9.453445],[1.070558],[2.411298],[-0.683219],[2.017703],[-2.325070],[-7.211693],[-7.582184],[-1.791196],[-6.214572],[6.422852],[-1.904283],[-5.428292],[-6.081521],[9.131998],[6.584773],[-7.501995],[-5.872398],[-0.166776],[1.317847],[1.372329],[-8.403008],[6.690075],[-8.125654],[7.074033],[4.961222],[-0.562690],[1.981749],[-0.459988],[-1.168288],[5.331208],[8.176422],[-2.119253],[5.323874],[2.683244],[-2.590297],[-8.132229],[-7.554374],[5.571439],[5.806177],[1.720957],[-4.062870],[-5.200933],[-0.654091],[1.352596],[-0.036537],[-8.170505],[-4.278548],[-5.703643],[-2.278402],[-5.953420],[-4.416747],[2.912168],[2.204247],[-1.054259],[3.714433],[6.197684],[9.286591],[4.603956],[1.172852],[-0.312533],[1.508717],[4.219594],[4.318681],[6.469429],[9.744790],[0.383352],[0.479014],[-7.789537],[7.835966],[1.207925],[-3.181712],[-1.044879],[7.709996],[1.177857],[-3.155050],[-2.402138],[8.373912],[-9.534382],[5.669991],[-9.937574],[9.720523],[5.792767],[-2.573719],[8.892663],[-0.609391],[-4.900396],[-6.323580],[-0.009150],[-7.056594],[-6.140253],[-2.051317],[-0.079072],[-6.943244],[-6.391299],[-4.629828],[7.750785],[-9.480384],[-2.609366],[-0.266526],[5.092806],[3.194506],[-6.591017],[-9.607694],[4.626395],[-9.733763],[-5.401200],[-3.616558],[-8.589095],[7.472054],[1.344230],[6.367035],[5.573858],[6.515293],[-0.464038],[-2.290799],[-0.493833],[1.579036],[2.188476],[8.898841],[-0.094417],[-0.970828],[-9.993003],[5.018322],[9.406057],[-5.604413],[4.384038],[9.340266],[2.680720],[-2.967450],[8.259341],[3.300448],[-9.098634],[-7.766026],[7.328908],[-4.935483],[1.541837],[-7.888451],[-0.637354],[1.366332],[-5.897177],[-8.770939],[1.534487],[-4.002104],[-5.018776],[3.308147],[9.683665],[7.936810],[6.331209],[2.567559],[4.060410],[5.884268],[-4.093491],[2.017921],[5.251064],[2.376999],[-8.413740],[0.361085],[5.051064],[-5.614180],[4.275382],[5.590835],[2.427077],[-0.158511],[-3.972814],[3.936718],[-2.644012],[4.887768],[-6.758646],[6.596914],[0.347150],[2.556283],[-8.625947],[0.503815],[-2.129848],[6.319104],[6.985224],[5.554712],[5.897796],[-3.905222],[0.176136],[4.454199],[-6.760562],[4.173789],[0.375864],[-1.016325],[0.494398],[-2.171394],[2.785294],[3.773669],[-2.495305],[5.826380],[-1.338067],[-2.485922],[-6.453313],[3.273604],[-8.798789],[0.304483],[1.559164],[1.373507],[8.951131],[7.691798],[0.398827],[-7.774594],[-8.560313],[-2.282911],[-0.769403],[-5.996854],[-8.696994],[-7.636432],[1.615525],[7.132413],[5.490274],[-1.196668],[6.388723],[0.572968],[-8.156373],[0.113699],[8.440112],[-2.535954],[5.414906],[-4.400125],[-4.295226],[-3.989294],[4.452771],[7.640789],[4.383431],[-2.546868],[-4.101669],[4.431964],[-0.594075],[-5.824806],[-2.486583],[-2.453130],[-0.639349],[2.773154],[4.542906],[9.604624],[-3.154324],[1.091441],[0.620242],[7.912056],[6.868660],[5.650663],[-3.750859],[4.575506],[0.338814],[2.061611],[0.958792],[2.520269],[-7.001788],[0.628612],[-7.100946],[5.336225],[4.958908],[-8.757225],[-1.746457],[1.355939],[4.022583],[8.284735],[3.090524],[-5.327724],[-4.707640],[-1.084047],[5.602002],[4.693914],[-6.804285],[-0.520155],[-2.745254],[-9.310790],[-9.879725],[-5.828867],[-1.080885],[-9.232136],[-5.299643],[5.442824],[-7.797288],[-7.459782],[-9.647061],[-4.484240],[3.303417],[0.825097],[-6.585960],[-9.622137],[-9.709034],[-7.270981],[-5.623980],[1.194987],[-6.913281],[-3.823046],[9.454232],[9.533633],[-4.122188],[-7.019444],[-5.894944],[-4.148859],[1.824019],[-2.274748],[3.735653],[-6.383850],[4.242418],[-0.369106],[8.025885],[-2.411141],[7.866798],[-5.875623],[-4.936352],[-4.973851],[0.442027],[8.536434],[3.556659],[6.441248],[-9.290491],[8.075473],[7.527978],[3.067401],[-4.314227],[-6.569253],[7.832114],[-1.104801],[8.600542],[3.187313],[-6.647140],[-3.779076],[-5.223091],[2.000143],[-5.411244],[-5.976391],[-7.959102],[-4.845180],[8.675440],[-5.732869],[-0.401083],[0.448837],[9.290002],[-9.631644],[-4.341765],[6.496993],[-9.031752],[6.288865],[5.692379],[-8.053416],[5.460496],[-9.275630],[-5.402214],[6.394529],[-0.882830],[-6.247852],[-7.909179],[-9.293488],[5.646809],[7.050833],[-3.908830],[-9.164825],[-3.627410],[-7.551545],[-9.520757],[3.116396],[6.511254],[-7.087144],[1.805567],[-5.747056],[5.909060],[-3.983455],[-3.059432],[-8.162359],[5.061389],[-6.009795],[-9.655907],[-0.404265],[-1.657723],[-9.916870],[-4.766958],[-9.483733],[-2.049654],[3.841970],[1.533870],[4.037393],[-6.028445],[-3.854607],[4.398883],[-7.412336],[-4.594441],[-3.406246],[1.956790],[-5.986685],[9.961827],[1.196576],[-1.277088],[-7.028037],[-6.256672],[-1.935221],[5.093045],[-0.021436],[6.245817],[-2.539950],[0.244751],[-0.785262],[4.077251],[-2.550730],[8.173980],[-9.518169],[-3.399187],[-8.418984],[-2.448196],[6.248913],[7.767145],[-6.592002],[6.716107],[-9.401112],[7.207739],[5.824394],[-0.614133],[1.994290],[2.629619],[-2.642319],[-3.245383],[8.540255],[-0.275793],[9.765103],[-8.880859],[5.454018],[5.317819],[-1.209585],[5.740030],[3.695877],[-9.713309],[7.692947],[-5.276407],[-2.497940],[0.001736],[2.219114],[-6.569338],[-2.102725],[-4.164956],[2.243999],[-2.597802],[-2.093695],[-7.601632],[-8.708347],[-4.394852],[-8.748362],[5.250836],[4.605219],[-1.019202],[0.083881],[-9.002637],[4.130499],[5.943200],[-2.081117],[-4.406674],[5.690388],[-6.872160],[-4.582208],[-7.680984],[-0.254237],[-6.148088],[9.368398],[4.031316],[-7.991791],[7.982792],[0.123169],[-3.292577],[-6.691487],[-2.602024],[9.978247],[-9.420459],[0.840335],[8.182028],[9.951736],[-2.955652],[-4.613890],[-5.559685],[-0.988710],[-1.322977],[-3.524800],[-9.365463],[8.945248],[-5.670865],[2.811971],[-9.454852],[9.340012],[3.362254],[-2.520213],[-5.634875],[-0.604166],[4.620113],[-4.411642],[5.905312],[0.029167],[6.968063],[0.506308],[6.953792],[-7.666423],[-9.653095],[-2.170897],[-1.135169],[1.998931],[-8.643065],[-1.001477],[0.579434],[-3.043624],[0.885769],[-9.430922],[5.219650],[-1.993833],[8.513392],[5.116430],[2.920441],[6.409428],[5.740438],[-4.514362],[7.386079],[9.950986],[3.238476],[6.009757],[-3.478005],[-7.134666],[-5.507351],[-1.464348],[-6.575588],[-9.728126],[-3.433229],[1.453801],[8.415066],[4.926656],[-6.558209],[-7.816313],[6.999651],[-9.875887],[-2.266737],[4.214707],[8.867855],[-1.284386],[0.082302],[3.945362],[-0.154604],[7.061231],[8.496552],[-4.235703],[4.234634],[5.353841],[3.651939],[-2.309965],[2.484858],[-1.601492],[-8.759927],[8.222493],[5.837225],[3.863919],[-4.043179],[-4.621500],[-7.616646],[-7.244437],[-9.607120],[-3.841956],[-7.552463],[-1.650075],[6.680376],[0.045931],[9.685278],[-3.483631],[3.985015],[7.847653],[-3.910844],[7.132872],[8.425972],[7.327252],[-3.813129],[-2.809472],[-7.809370]], dtype = "float32")#candidate|7384|(700, 1)|const|float32
call_7383 = func_6699_call(relay.reshape(const_7384.astype('float32'), [7, 10, 10]))
call_7385 = func_6699_call(relay.reshape(const_7384.astype('float32'), [7, 10, 10]))
uop_7403 = relay.tan(const_7384.astype('float64')) # shape=(700, 1)
func_3831_call = mod.get_global_var('func_3831')
func_3833_call = mutated_mod.get_global_var('func_3833')
const_7419 = relay.const([[4,3,3,8,5,4],[4,3,1,8,-1,-5],[1,7,-2,5,10,-9],[-3,-2,10,-4,9,6],[7,6,-10,6,-8,3],[-1,-5,-6,3,1,8],[3,-4,9,-4,3,4],[-2,-7,7,-10,10,-9],[-8,-6,10,-10,7,-5],[5,-5,-1,6,-1,-4],[2,-7,7,-9,-10,6],[2,-3,4,-7,9,-1],[-1,2,9,2,-9,-4],[-7,-3,-7,-7,7,-7],[-7,-9,-6,-5,-7,-1],[-4,-8,6,-7,-2,-1],[1,9,7,-10,2,-1],[10,-5,4,3,-1,-8],[2,1,8,-4,-10,-9],[-3,-9,8,3,-5,-7],[6,-4,-3,-5,10,9],[-8,6,-10,-2,2,5],[-1,-10,-9,-5,8,-4],[-4,6,-7,-9,-1,-4],[10,1,-9,-3,-7,9],[9,10,5,-8,7,2],[-2,10,8,4,1,-1],[6,-3,9,8,5,-5],[6,-1,9,8,4,7],[-3,9,10,4,-6,-8],[8,10,8,6,-1,8],[10,-3,5,6,3,-1],[5,-1,-4,-5,9,-6],[3,2,10,-5,-5,7],[-8,-7,8,8,-5,6],[7,10,9,4,1,-9],[5,3,2,-1,1,-3],[-8,-2,-9,-2,2,-4],[-9,6,-4,1,6,-1],[-4,-9,2,5,5,3],[-8,2,-7,2,5,-6],[-2,8,2,8,-4,4],[1,8,-7,-9,7,6],[8,-10,5,-9,6,4],[-9,-8,9,2,9,5],[-2,4,8,1,-7,8],[-10,6,-6,-6,3,1],[3,-2,-3,2,-5,-3],[6,10,9,-3,7,-5],[-10,-10,-4,-4,4,1],[3,3,10,1,-1,7],[-9,9,2,10,6,4],[3,-8,4,-8,-3,-2],[-8,8,4,-1,10,10],[5,-3,-2,-10,-6,3]], dtype = "int16")#candidate|7419|(55, 6)|const|int16
call_7418 = relay.TupleGetItem(func_3831_call(relay.reshape(const_7419.astype('int16'), [11, 15, 2])), 0)
call_7420 = relay.TupleGetItem(func_3833_call(relay.reshape(const_7419.astype('int16'), [11, 15, 2])), 0)
func_5551_call = mod.get_global_var('func_5551')
func_5553_call = mutated_mod.get_global_var('func_5553')
call_7454 = func_5551_call()
call_7455 = func_5551_call()
func_6656_call = mod.get_global_var('func_6656')
func_6657_call = mutated_mod.get_global_var('func_6657')
call_7456 = func_6656_call()
call_7457 = func_6656_call()
uop_7473 = relay.cos(call_7456.astype('float64')) # shape=(4, 12, 13)
uop_7475 = relay.cos(call_7457.astype('float64')) # shape=(4, 12, 13)
output = relay.Tuple([call_7374,call_7383,uop_7403,call_7418,const_7419,call_7454,uop_7473,])
output2 = relay.Tuple([call_7375,call_7385,uop_7403,call_7420,const_7419,call_7455,uop_7475,])
func_7485 = relay.Function([], output)
mod['func_7485'] = func_7485
mod = relay.transform.InferType()(mod)
output = func_7485()
func_7486 = relay.Function([], output)
mutated_mod['func_7486'] = func_7486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_7510 = relay.TupleGetItem(func_4331_call(), 1)
call_7511 = relay.TupleGetItem(func_4333_call(), 1)
output = call_7510
output2 = call_7511
func_7516 = relay.Function([], output)
mod['func_7516'] = func_7516
mod = relay.transform.InferType()(mod)
mutated_mod['func_7516'] = func_7516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7516_call = mutated_mod.get_global_var('func_7516')
call_7517 = func_7516_call()
output = call_7517
func_7518 = relay.Function([], output)
mutated_mod['func_7518'] = func_7518
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5653_call = mod.get_global_var('func_5653')
func_5655_call = mutated_mod.get_global_var('func_5655')
call_7540 = relay.TupleGetItem(func_5653_call(), 0)
call_7541 = relay.TupleGetItem(func_5655_call(), 0)
output = relay.Tuple([call_7540,])
output2 = relay.Tuple([call_7541,])
func_7566 = relay.Function([], output)
mod['func_7566'] = func_7566
mod = relay.transform.InferType()(mod)
output = func_7566()
func_7567 = relay.Function([], output)
mutated_mod['func_7567'] = func_7567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6205_call = mod.get_global_var('func_6205')
func_6206_call = mutated_mod.get_global_var('func_6206')
call_7612 = relay.TupleGetItem(func_6205_call(), 0)
call_7613 = relay.TupleGetItem(func_6206_call(), 0)
uop_7620 = relay.cos(call_7612.astype('float64')) # shape=(11, 5, 5)
uop_7622 = relay.cos(call_7613.astype('float64')) # shape=(11, 5, 5)
uop_7631 = relay.exp(call_7612.astype('float32')) # shape=(11, 5, 5)
uop_7633 = relay.exp(call_7613.astype('float32')) # shape=(11, 5, 5)
bop_7639 = relay.minimum(uop_7631.astype('uint32'), relay.reshape(uop_7620.astype('uint32'), relay.shape_of(uop_7631))) # shape=(11, 5, 5)
bop_7642 = relay.minimum(uop_7633.astype('uint32'), relay.reshape(uop_7622.astype('uint32'), relay.shape_of(uop_7633))) # shape=(11, 5, 5)
func_6646_call = mod.get_global_var('func_6646')
func_6648_call = mutated_mod.get_global_var('func_6648')
call_7680 = func_6646_call()
call_7681 = func_6646_call()
uop_7683 = relay.sin(call_7612.astype('float32')) # shape=(11, 5, 5)
uop_7685 = relay.sin(call_7613.astype('float32')) # shape=(11, 5, 5)
output = relay.Tuple([bop_7639,call_7680,uop_7683,])
output2 = relay.Tuple([bop_7642,call_7681,uop_7685,])
func_7687 = relay.Function([], output)
mod['func_7687'] = func_7687
mod = relay.transform.InferType()(mod)
mutated_mod['func_7687'] = func_7687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7687_call = mutated_mod.get_global_var('func_7687')
call_7688 = func_7687_call()
output = call_7688
func_7689 = relay.Function([], output)
mutated_mod['func_7689'] = func_7689
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_7729 = func_6009_call()
call_7730 = func_6009_call()
var_7735 = relay.var("var_7735", dtype = "float64", shape = (4, 12, 13))#candidate|7735|(4, 12, 13)|var|float64
bop_7736 = relay.bitwise_and(call_7729.astype('uint16'), relay.reshape(var_7735.astype('uint16'), relay.shape_of(call_7729))) # shape=(4, 12, 13)
bop_7739 = relay.bitwise_and(call_7730.astype('uint16'), relay.reshape(var_7735.astype('uint16'), relay.shape_of(call_7730))) # shape=(4, 12, 13)
bop_7744 = relay.multiply(call_7729.astype('uint32'), relay.reshape(var_7735.astype('uint32'), relay.shape_of(call_7729))) # shape=(4, 12, 13)
bop_7747 = relay.multiply(call_7730.astype('uint32'), relay.reshape(var_7735.astype('uint32'), relay.shape_of(call_7730))) # shape=(4, 12, 13)
output = relay.Tuple([bop_7736,bop_7744,])
output2 = relay.Tuple([bop_7739,bop_7747,])
func_7752 = relay.Function([var_7735,], output)
mod['func_7752'] = func_7752
mod = relay.transform.InferType()(mod)
var_7753 = relay.var("var_7753", dtype = "float64", shape = (4, 12, 13))#candidate|7753|(4, 12, 13)|var|float64
output = func_7752(var_7753)
func_7754 = relay.Function([var_7753], output)
mutated_mod['func_7754'] = func_7754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6376_call = mod.get_global_var('func_6376')
func_6378_call = mutated_mod.get_global_var('func_6378')
call_7794 = func_6376_call()
call_7795 = func_6376_call()
func_6391_call = mod.get_global_var('func_6391')
func_6393_call = mutated_mod.get_global_var('func_6393')
call_7826 = func_6391_call()
call_7827 = func_6391_call()
output = relay.Tuple([call_7794,call_7826,])
output2 = relay.Tuple([call_7795,call_7827,])
func_7828 = relay.Function([], output)
mod['func_7828'] = func_7828
mod = relay.transform.InferType()(mod)
mutated_mod['func_7828'] = func_7828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7828_call = mutated_mod.get_global_var('func_7828')
call_7829 = func_7828_call()
output = call_7829
func_7830 = relay.Function([], output)
mutated_mod['func_7830'] = func_7830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7192_call = mod.get_global_var('func_7192')
func_7193_call = mutated_mod.get_global_var('func_7193')
call_7834 = func_7192_call()
call_7835 = func_7192_call()
func_4676_call = mod.get_global_var('func_4676')
func_4682_call = mutated_mod.get_global_var('func_4682')
var_7843 = relay.var("var_7843", dtype = "float64", shape = (1, 26))#candidate|7843|(1, 26)|var|float64
var_7844 = relay.var("var_7844", dtype = "int32", shape = (273,))#candidate|7844|(273,)|var|int32
var_7845 = relay.var("var_7845", dtype = "float64", shape = (832,))#candidate|7845|(832,)|var|float64
var_7846 = relay.var("var_7846", dtype = "int16", shape = (63,))#candidate|7846|(63,)|var|int16
call_7842 = relay.TupleGetItem(func_4676_call(relay.reshape(var_7843.astype('float64'), [26,]), relay.reshape(var_7844.astype('int32'), [273,]), relay.reshape(var_7845.astype('float64'), [832,]), relay.reshape(var_7846.astype('int16'), [63,]), ), 12)
call_7847 = relay.TupleGetItem(func_4682_call(relay.reshape(var_7843.astype('float64'), [26,]), relay.reshape(var_7844.astype('int32'), [273,]), relay.reshape(var_7845.astype('float64'), [832,]), relay.reshape(var_7846.astype('int16'), [63,]), ), 12)
output = relay.Tuple([call_7834,call_7842,var_7843,var_7844,var_7845,var_7846,])
output2 = relay.Tuple([call_7835,call_7847,var_7843,var_7844,var_7845,var_7846,])
func_7852 = relay.Function([var_7843,var_7844,var_7845,var_7846,], output)
mod['func_7852'] = func_7852
mod = relay.transform.InferType()(mod)
var_7853 = relay.var("var_7853", dtype = "float64", shape = (1, 26))#candidate|7853|(1, 26)|var|float64
var_7854 = relay.var("var_7854", dtype = "int32", shape = (273,))#candidate|7854|(273,)|var|int32
var_7855 = relay.var("var_7855", dtype = "float64", shape = (832,))#candidate|7855|(832,)|var|float64
var_7856 = relay.var("var_7856", dtype = "int16", shape = (63,))#candidate|7856|(63,)|var|int16
output = func_7852(var_7853,var_7854,var_7855,var_7856,)
func_7857 = relay.Function([var_7853,var_7854,var_7855,var_7856,], output)
mutated_mod['func_7857'] = func_7857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7931 = relay.var("var_7931", dtype = "float64", shape = (3, 2, 2))#candidate|7931|(3, 2, 2)|var|float64
uop_7932 = relay.exp(var_7931.astype('float64')) # shape=(3, 2, 2)
output = relay.Tuple([uop_7932,])
output2 = relay.Tuple([uop_7932,])
func_7937 = relay.Function([var_7931,], output)
mod['func_7937'] = func_7937
mod = relay.transform.InferType()(mod)
mutated_mod['func_7937'] = func_7937
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7938 = relay.var("var_7938", dtype = "float64", shape = (3, 2, 2))#candidate|7938|(3, 2, 2)|var|float64
func_7937_call = mutated_mod.get_global_var('func_7937')
call_7939 = func_7937_call(var_7938)
output = call_7939
func_7940 = relay.Function([var_7938], output)
mutated_mod['func_7940'] = func_7940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6218_call = mod.get_global_var('func_6218')
func_6219_call = mutated_mod.get_global_var('func_6219')
call_7950 = func_6218_call()
call_7951 = func_6218_call()
output = relay.Tuple([call_7950,])
output2 = relay.Tuple([call_7951,])
func_7953 = relay.Function([], output)
mod['func_7953'] = func_7953
mod = relay.transform.InferType()(mod)
mutated_mod['func_7953'] = func_7953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7953_call = mutated_mod.get_global_var('func_7953')
call_7954 = func_7953_call()
output = call_7954
func_7955 = relay.Function([], output)
mutated_mod['func_7955'] = func_7955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_7961 = relay.TupleGetItem(func_4542_call(), 0)
call_7962 = relay.TupleGetItem(func_4544_call(), 0)
func_418_call = mod.get_global_var('func_418')
func_421_call = mutated_mod.get_global_var('func_421')
const_7975 = relay.const([7.497405,-8.072098,7.542016,2.557653,6.367372,9.732326,-0.217988,-2.999454,7.366618,9.201784,5.000548,-2.203959,7.982357,9.286137,-0.837804,-8.719080,5.402858,5.152791,3.024898,4.262170,0.004341,-3.648845,-3.812643,5.924829,-4.189903,6.893809], dtype = "float64")#candidate|7975|(26,)|const|float64
call_7974 = func_418_call(relay.reshape(call_7961.astype('float64'), []), relay.reshape(const_7975.astype('float64'), [2, 13, 1]), )
call_7976 = func_418_call(relay.reshape(call_7961.astype('float64'), []), relay.reshape(const_7975.astype('float64'), [2, 13, 1]), )
bop_7989 = relay.power(call_7974.astype('float64'), relay.reshape(const_7975.astype('float64'), relay.shape_of(call_7974))) # shape=(2, 13, 1)
bop_7992 = relay.power(call_7976.astype('float64'), relay.reshape(const_7975.astype('float64'), relay.shape_of(call_7976))) # shape=(2, 13, 1)
output = relay.Tuple([call_7961,bop_7989,])
output2 = relay.Tuple([call_7962,bop_7992,])
func_8007 = relay.Function([], output)
mod['func_8007'] = func_8007
mod = relay.transform.InferType()(mod)
mutated_mod['func_8007'] = func_8007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8007_call = mutated_mod.get_global_var('func_8007')
call_8008 = func_8007_call()
output = call_8008
func_8009 = relay.Function([], output)
mutated_mod['func_8009'] = func_8009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4364_call = mod.get_global_var('func_4364')
func_4366_call = mutated_mod.get_global_var('func_4366')
call_8090 = relay.TupleGetItem(func_4364_call(), 0)
call_8091 = relay.TupleGetItem(func_4366_call(), 0)
output = relay.Tuple([call_8090,])
output2 = relay.Tuple([call_8091,])
func_8100 = relay.Function([], output)
mod['func_8100'] = func_8100
mod = relay.transform.InferType()(mod)
output = func_8100()
func_8101 = relay.Function([], output)
mutated_mod['func_8101'] = func_8101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6475_call = mod.get_global_var('func_6475')
func_6476_call = mutated_mod.get_global_var('func_6476')
call_8127 = relay.TupleGetItem(func_6475_call(), 0)
call_8128 = relay.TupleGetItem(func_6476_call(), 0)
output = call_8127
output2 = call_8128
func_8129 = relay.Function([], output)
mod['func_8129'] = func_8129
mod = relay.transform.InferType()(mod)
output = func_8129()
func_8130 = relay.Function([], output)
mutated_mod['func_8130'] = func_8130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6218_call = mod.get_global_var('func_6218')
func_6219_call = mutated_mod.get_global_var('func_6219')
call_8131 = func_6218_call()
call_8132 = func_6218_call()
uop_8135 = relay.acosh(call_8131.astype('float64')) # shape=(7, 10, 10)
uop_8137 = relay.acosh(call_8132.astype('float64')) # shape=(7, 10, 10)
func_988_call = mod.get_global_var('func_988')
func_991_call = mutated_mod.get_global_var('func_991')
const_8148 = relay.const([-7,1,-7,10,10,3,2,8,3,-5,1,5,-8,-2,-9,3,-10,-1,-5,10,-1,-7,-6,-8,4,-6,-3,-8,-5,4,-1,-1,1,-9,-5,2,-3,10,4,8,1,-3,-6,-5,-3,-6,-6,-5,-1,3,-5,-3,-6,10,10,9,6,6,-5,3,-10,2,6,-4,4,-4,-6,9,-1,-3,-9,-4,8,-6,-1,-1,-8,10,10,2,3,3,4,-1,-3,7,1,-6,1,2,-1,-4,3,2,8,-7,9,-10,4,-9,8,-8,5,-5,-5,10,-9,-2,10,8,-7,9,-7,-2,-10,7,-7,6,8,-10,-10,7,-5,-4,5,3,6,-10,2,-3,3,2,-6,3,10,9,4,-1,-6,-3,4,-3,-9,5,-6,-4,10,-8,4,2,-3,-6,-6,-5,2,5,6,-8,4,-4,2,7,6,10,-7,6,5,6,-8,6,-10,8,1,-9,-9,-5,-5,-5,-10,-2,9,-6,1,6,4,1,-4,-10,-3,10,-5,5,9,-2,-4,3,-2,6,2,3,5,-2,1,4,2,-7,10,7,-1,8,3,7,-2,-9,6,-4,5,9,-9,-1,-8,-2,-10,8,7,-7,9,8,-8,10,8,-4,-2,-7,4,4,8,-10,4,-10,-8,-5,-10,10,9,-1,-6,8,-7,-8,4,-5,-9,-1,-7,-8,-7,-1,6,-6,-3,-10,3,6,-4,5,8,8,-6,-2,9,7,-5,-6,2,-5,-10,-4,4,5,2,-4,9,-10,1,10,-4,-8,7,-7,6,6,9,-9,7,9,-5,4,4,-2,5,-5,-1,5,6,1,-6,-8,-6,-7,4,-4,8,-4,1,-7,10,-5,-4,-2,-4,2,9,-6,8,8,9,10,2,-10,-2,1,-9,-4,7,-5,9,3,-9,3,-2,1,4,9,-9,-1,7,2,8,-1,4,-8,-5,-10,-9,6,-3,3,10,5,2,-10,-10,5,2,5,-1,-6,-3,3,-9,-3,7,2,-7,-7,-5,-6,-3,4,-6,-9,3,3,4,-10,-6,9,-9,3,10,-7,-8,1,-5,-7,4,-7,-3,-3,-10,-4,-7,2,-6,4,-4,10,-5,5,5,-2,-10,-6,-1,2,3,8,10,6,4,1,-2,-1,-1,-8,8,5,-8,1,-1,1,-2,2,10,8,-9,-1,2,-9,-8,-9,-6,6,-7,-3,1,-2,2,7,-3,5,5,-2,-8,10,-7,-4,-5,-7,7,-1,-4,5,7,8,-8,2,9,-10,5,4,-9,7,9,8,-1,-6,2,-1,-3,10,1,3,-6,-6,-3,6,-9,7,4,3,4,2,-9,4,-1,-3,6,2,-1,6,-9,7,3,5,9,5,-5,9,10,-8,-10,5,7,10,8,-1,8,6,-1,-1,8,2,-4,9,-4,7,8,-10,1,-2,-5,7,-10,-7,5,9,-7,-7,2,7,3,-10,7,-5,-1,7,-9,-3,9,-7,-9,6,-7,-7,8,-5,-7,1,8,-2,2,-6,6,-7,-9,-9,-1,4,-9,7,4,-10,10,7,-7,6,2,10,1,-5,2,-9,-3,2,-4,1,2,3,5,1,-10,-1,1,10,-1,-2,-9,7,-6,5,-8,9,8,-6,-1,4,4,-4,1,6,-1,4,-1,-3,9,-6,2,1,-7,-4,-3,-2,8,-1,1,10,6,-3,4,-4,2,2,-7,-8,9,5,-2,9,4,-10,7,-9,5,-2,6,4,5,-3,-10,-7,5,-10,-8,9,-7,8,-3,7,-9,-7,-4,-4,-10,3,2,-8,1,-3,7,2,-5,7,9,3,2,4,4,5,9,-5,-8,-5,1,2,4,-1,6,6,-10,3,1,-8,-7,1,2,6,-9,3,-3,-7,10,-5,-3,-2,-9,7,-4,9,1,-9,5,7,6,-5,6,5,7,-10,10,7,9,-1,2,-6,1,-8,-9,-2,6,6,-9,-7,3,-9,1,4,10,3,-7,-7,-2,-5,-1,-10,4,8,-8,-10,-2,6,6,5,5,-10,-7,-1,1,4,4,-6,9,-4,10,-8,4,8,-3,-6,1,3,10,-8,1,-10,5,7,-3,-1,-4,5,-4,-8,6,-5,9,-4,3,1,-6,-1,8,-5,9,-5,-4,3,-3,-4,6,-5,-9,-5,5,-6,-6,9,7,6,-9,-2,-1,-2,-7,-5,-8,-7,1,7,5,-4,2,-6,9,-8,-3,1,7,-8,10,7,-4,-4,6,3,-7,-4,-2,2,10,-10,-10,7,-4,10,-8,1,3,9,9,1,-8,-8,5,2,8,8,-2,-5,-10,10,4,-10,-9,6,-10,5,-4,-8,3,-4,-1,10,7,-8,2,7,-1,3,-5,-7,8,10,-7,10,-8,2,9,3,-7,5,8,5,8,-9,-9,-7,-10,-10,7,6,6,-5,8,-3,8,6,1,-5,-1,1,1,-6,6,8,6,9,2,9,3,-6,-9,6,4,-8,-8,-3,-8,9,-7,-9,1,-6,-3,2,4,-6,-10,2,6,9,8,2,-2,-2,-6,-3,9,9,-4,-8,8,-3,10,4,-5,9,-6,-3,-2,7,-6,-6,-10,6,7,-2,2,5,1,8,-2,-3,-10,7,1,-1,-6,1,3,8,3,-6,7,7,-1,-6,-1,-3,5,-2,-6,1,-3,6,10,-7,5,-10,-5,10,1,10,7,3,-3,-8,2,-9,-4,1,10,-8,1,7,6,-1,5,9,5,4,10,5,1,-7,8,10,-7,-2,8,-4,9,9,9,8,1,1,3,-1,9,-1,7,-4,-10,3,-8,-10,4,-2,9,-8,1,-10,-5,-1,1,1,1,-10,-2,9,-2,6,10,1,-10,-8,8,7,10,-6,-10,-9,-2,2,-4,1,-1,1,7,-9,-9,-9,-4,10,6,7,3,-9,-4,9,3,3,-7,3,4,-10,-10,2,9,10,-8,-3,2,7,2,-4,-6,-9,1,6,6,2,6,2,6,1,8,8,-4,5,-1,-3,8,-7,-7,-6,-10,1,-2,9,4,3,-4,1,8,-7,7,-5,3,-5,6,5,10,9,-8,2,-2,5,8,5,-4,-4,-2,9,10,8,-5,-9,1,-1,-10,-5,9,-8,8,4,6,4,-8,5,-6,3,8,-8,-4,1,3,-6,-6,3,8,5,-7,1,-3,-3,-1,-2,-8,9,-1,-6,6,7,8,5,7,-9,-10,-10,-9,4,9,1,6,9,-10,-10,-9,-10,8,3,7,2,6,-2,6,7,10,5,7,1,-1,8,9,8,-1,-7,-7,-6,2,10,-4,5,6,-7,-4,-4,1,-6,8,-2,-5,9,-7,-4,5,-8,2,2,-1,-1,-9,-1,-5,-3,-9,3,-1,7,-7,6,5,-10,7,-5,3,5,-10,-2,-3,9,-9,7,5,9,-5,6,1,6,-10,-8,6,-4,-10,-3,-1,-7,5,4,8,-3,-10,-2,7,-1,-9,-9,-2,1,-9,-7,5,3,-7,-1,2,-7,-5,5,7,10,-5,-10,1,-9,4,-1], dtype = "uint32")#candidate|8148|(1320,)|const|uint32
const_8149 = relay.const([-0.672488,5.303417,-4.298218,-8.136437,3.587995,-9.112245,-7.862600,8.982846,4.770038,-0.317988,8.936812,0.129906,-3.246123,1.563710,-2.668279,6.246565,8.734872,-6.748287,-0.287278,-0.393465,9.378271,4.926839,-5.417832,2.271117,-6.199956,5.743624], dtype = "float64")#candidate|8149|(26,)|const|float64
call_8147 = relay.TupleGetItem(func_988_call(relay.reshape(const_8148.astype('uint32'), [8, 15, 11]), relay.reshape(const_8149.astype('float64'), [26,]), ), 1)
call_8150 = relay.TupleGetItem(func_991_call(relay.reshape(const_8148.astype('uint32'), [8, 15, 11]), relay.reshape(const_8149.astype('float64'), [26,]), ), 1)
output = relay.Tuple([uop_8135,call_8147,const_8148,const_8149,])
output2 = relay.Tuple([uop_8137,call_8150,const_8148,const_8149,])
func_8159 = relay.Function([], output)
mod['func_8159'] = func_8159
mod = relay.transform.InferType()(mod)
output = func_8159()
func_8160 = relay.Function([], output)
mutated_mod['func_8160'] = func_8160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4542_call = mod.get_global_var('func_4542')
func_4544_call = mutated_mod.get_global_var('func_4544')
call_8215 = relay.TupleGetItem(func_4542_call(), 0)
call_8216 = relay.TupleGetItem(func_4544_call(), 0)
output = relay.Tuple([call_8215,])
output2 = relay.Tuple([call_8216,])
func_8231 = relay.Function([], output)
mod['func_8231'] = func_8231
mod = relay.transform.InferType()(mod)
output = func_8231()
func_8232 = relay.Function([], output)
mutated_mod['func_8232'] = func_8232
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4914_call = mod.get_global_var('func_4914')
func_4916_call = mutated_mod.get_global_var('func_4916')
call_8347 = relay.TupleGetItem(func_4914_call(), 3)
call_8348 = relay.TupleGetItem(func_4916_call(), 3)
func_6321_call = mod.get_global_var('func_6321')
func_6323_call = mutated_mod.get_global_var('func_6323')
call_8355 = relay.TupleGetItem(func_6321_call(), 1)
call_8356 = relay.TupleGetItem(func_6323_call(), 1)
uop_8374 = relay.atan(call_8355.astype('float32')) # shape=(11, 5, 5)
uop_8376 = relay.atan(call_8356.astype('float32')) # shape=(11, 5, 5)
output = relay.Tuple([call_8347,uop_8374,])
output2 = relay.Tuple([call_8348,uop_8376,])
func_8378 = relay.Function([], output)
mod['func_8378'] = func_8378
mod = relay.transform.InferType()(mod)
output = func_8378()
func_8379 = relay.Function([], output)
mutated_mod['func_8379'] = func_8379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8100_call = mod.get_global_var('func_8100')
func_8101_call = mutated_mod.get_global_var('func_8101')
call_8398 = relay.TupleGetItem(func_8100_call(), 0)
call_8399 = relay.TupleGetItem(func_8101_call(), 0)
output = relay.Tuple([call_8398,])
output2 = relay.Tuple([call_8399,])
func_8402 = relay.Function([], output)
mod['func_8402'] = func_8402
mod = relay.transform.InferType()(mod)
output = func_8402()
func_8403 = relay.Function([], output)
mutated_mod['func_8403'] = func_8403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6442_call = mod.get_global_var('func_6442')
func_6444_call = mutated_mod.get_global_var('func_6444')
call_8412 = func_6442_call()
call_8413 = func_6442_call()
output = relay.Tuple([call_8412,])
output2 = relay.Tuple([call_8413,])
func_8450 = relay.Function([], output)
mod['func_8450'] = func_8450
mod = relay.transform.InferType()(mod)
mutated_mod['func_8450'] = func_8450
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8450_call = mutated_mod.get_global_var('func_8450')
call_8451 = func_8450_call()
output = call_8451
func_8452 = relay.Function([], output)
mutated_mod['func_8452'] = func_8452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4333_call = mutated_mod.get_global_var('func_4333')
call_8481 = relay.TupleGetItem(func_4331_call(), 0)
call_8482 = relay.TupleGetItem(func_4333_call(), 0)
func_8402_call = mod.get_global_var('func_8402')
func_8403_call = mutated_mod.get_global_var('func_8403')
call_8486 = relay.TupleGetItem(func_8402_call(), 0)
call_8487 = relay.TupleGetItem(func_8403_call(), 0)
func_2375_call = mod.get_global_var('func_2375')
func_2379_call = mutated_mod.get_global_var('func_2379')
var_8498 = relay.var("var_8498", dtype = "int32", shape = (90,))#candidate|8498|(90,)|var|int32
var_8499 = relay.var("var_8499", dtype = "int32", shape = (1170,))#candidate|8499|(1170,)|var|int32
var_8500 = relay.var("var_8500", dtype = "float64", shape = (26,))#candidate|8500|(26,)|var|float64
call_8497 = relay.TupleGetItem(func_2375_call(relay.reshape(var_8498.astype('int32'), [15, 1, 6]), relay.reshape(var_8499.astype('int32'), [15, 13, 6]), relay.reshape(var_8500.astype('float64'), [26,]), ), 3)
call_8501 = relay.TupleGetItem(func_2379_call(relay.reshape(var_8498.astype('int32'), [15, 1, 6]), relay.reshape(var_8499.astype('int32'), [15, 13, 6]), relay.reshape(var_8500.astype('float64'), [26,]), ), 3)
func_8231_call = mod.get_global_var('func_8231')
func_8232_call = mutated_mod.get_global_var('func_8232')
call_8511 = relay.TupleGetItem(func_8231_call(), 0)
call_8512 = relay.TupleGetItem(func_8232_call(), 0)
uop_8520 = relay.sqrt(call_8481.astype('float64')) # shape=(2, 5, 1)
uop_8522 = relay.sqrt(call_8482.astype('float64')) # shape=(2, 5, 1)
bop_8533 = relay.right_shift(uop_8520.astype('int16'), var_8500.astype('int16')) # shape=(2, 5, 26)
bop_8536 = relay.right_shift(uop_8522.astype('int16'), var_8500.astype('int16')) # shape=(2, 5, 26)
uop_8553 = relay.cos(uop_8520.astype('float32')) # shape=(2, 5, 1)
uop_8555 = relay.cos(uop_8522.astype('float32')) # shape=(2, 5, 1)
func_7014_call = mod.get_global_var('func_7014')
func_7016_call = mutated_mod.get_global_var('func_7016')
var_8568 = relay.var("var_8568", dtype = "float64", shape = (130,))#candidate|8568|(130,)|var|float64
call_8567 = relay.TupleGetItem(func_7014_call(relay.reshape(var_8568.astype('float64'), [2, 5, 13])), 1)
call_8569 = relay.TupleGetItem(func_7016_call(relay.reshape(var_8568.astype('float64'), [2, 5, 13])), 1)
uop_8578 = relay.cosh(call_8481.astype('float64')) # shape=(2, 5, 1)
uop_8580 = relay.cosh(call_8482.astype('float64')) # shape=(2, 5, 1)
func_6218_call = mod.get_global_var('func_6218')
func_6219_call = mutated_mod.get_global_var('func_6219')
call_8581 = func_6218_call()
call_8582 = func_6218_call()
output = relay.Tuple([call_8486,call_8497,var_8498,var_8499,call_8511,bop_8533,uop_8553,call_8567,var_8568,uop_8578,call_8581,])
output2 = relay.Tuple([call_8487,call_8501,var_8498,var_8499,call_8512,bop_8536,uop_8555,call_8569,var_8568,uop_8580,call_8582,])
func_8586 = relay.Function([var_8498,var_8499,var_8500,var_8568,], output)
mod['func_8586'] = func_8586
mod = relay.transform.InferType()(mod)
var_8587 = relay.var("var_8587", dtype = "int32", shape = (90,))#candidate|8587|(90,)|var|int32
var_8588 = relay.var("var_8588", dtype = "int32", shape = (1170,))#candidate|8588|(1170,)|var|int32
var_8589 = relay.var("var_8589", dtype = "float64", shape = (26,))#candidate|8589|(26,)|var|float64
var_8590 = relay.var("var_8590", dtype = "float64", shape = (130,))#candidate|8590|(130,)|var|float64
output = func_8586(var_8587,var_8588,var_8589,var_8590,)
func_8591 = relay.Function([var_8587,var_8588,var_8589,var_8590,], output)
mutated_mod['func_8591'] = func_8591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6391_call = mod.get_global_var('func_6391')
func_6393_call = mutated_mod.get_global_var('func_6393')
call_8607 = func_6391_call()
call_8608 = func_6391_call()
var_8615 = relay.var("var_8615", dtype = "float64", shape = (2, 5, 2))#candidate|8615|(2, 5, 2)|var|float64
bop_8616 = relay.equal(call_8607.astype('bool'), var_8615.astype('bool')) # shape=(2, 5, 2)
bop_8619 = relay.equal(call_8608.astype('bool'), var_8615.astype('bool')) # shape=(2, 5, 2)
output = bop_8616
output2 = bop_8619
func_8628 = relay.Function([var_8615,], output)
mod['func_8628'] = func_8628
mod = relay.transform.InferType()(mod)
mutated_mod['func_8628'] = func_8628
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8629 = relay.var("var_8629", dtype = "float64", shape = (2, 5, 2))#candidate|8629|(2, 5, 2)|var|float64
func_8628_call = mutated_mod.get_global_var('func_8628')
call_8630 = func_8628_call(var_8629)
output = call_8630
func_8631 = relay.Function([var_8629], output)
mutated_mod['func_8631'] = func_8631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8650 = relay.var("var_8650", dtype = "float32", shape = (15, 2, 3))#candidate|8650|(15, 2, 3)|var|float32
uop_8651 = relay.log10(var_8650.astype('float32')) # shape=(15, 2, 3)
func_1142_call = mod.get_global_var('func_1142')
func_1144_call = mutated_mod.get_global_var('func_1144')
const_8656 = relay.const([-1.714148,-1.155152,-0.835135,-6.749584,0.283683,6.076710,-1.468354,7.641267,-3.380450,-6.440607,8.725950,6.347225,8.959900,-9.294408,-3.398284,4.617100,1.040697,-7.168625,-3.458620,-8.236787,4.276136,0.237449,-5.824787,7.130515,-0.960579,-1.644169,1.036474,7.021873,-7.079547,2.360126,1.177576,8.017131,-3.217596,-6.155338,-2.261262,2.262947,-4.069475,-3.086662,2.152810,2.571822,3.124417,4.846421,4.068862,6.197940,-1.778870,5.918169,8.076244,-9.812168,-2.181200,-7.855088,5.286618,-6.578857,-3.694942,3.732468,7.250089,1.963432,-3.578566,2.897009,0.046385,5.713043,2.388276,-8.942232,5.437517,4.916906,5.436120,5.496007,7.885276,1.938879,-9.088221,3.910228,9.629153,-2.005389,7.123640,-3.443612,-8.822479,-0.645404,-0.583269,-8.761729,3.759059,4.555919,0.854410,-9.600590,7.701904,-5.444018,-5.519819,6.401910,-4.834979,7.985566,9.248754,4.215225,8.968666,8.434958,-0.458791,5.487207,7.267764,-0.167435,2.458922,6.137065,-8.330966,-4.555743,2.360305,9.018837,3.151572,1.980130,-4.286359,-8.099081,-2.527008,2.881511,5.304581,7.667730,7.774842,1.136806,-6.488714,1.212700,-9.976294,1.872381,6.740008,-7.338834,0.176621,0.624495,-8.487729,2.678180,-2.755667,3.273846,1.627125,-1.450900,-4.109501,-6.723424,0.847669,-4.919644,4.097458,1.794485,-0.121945,-4.453468,-0.982630,2.203349,0.908116,0.914605,4.697035,-4.020185,0.835517,5.192686,-6.502156,-0.542550,-0.172402,-6.205108,-3.948119,-0.700311,1.718144,-3.928253,1.255710,-8.420690,-4.113272,-5.052246,-5.735285,9.020522,6.480097,1.813688,-7.053066,3.685536,-7.848037,-3.010169,-8.843540,2.156318,6.366288,9.101273,9.202391,-7.261052,7.402554,1.104317,8.071305,-0.916497,-1.693696,-8.805223,3.254496,3.999762,4.873117,3.523993,-1.361975,9.103435,-1.326228,-6.596586,-1.425249,-7.995582,3.681325,9.705393,-2.239240,-7.404314,-7.068902,7.686611,-2.551478,1.071255,-9.405382,2.856049,-6.372184,2.457786,0.324278,-1.438636,-3.271798,-4.321930,5.750423,-5.638966,1.733313,-8.050729,8.231004,2.913674,-3.300809,-6.423973,7.109057,3.959721,-8.550163,7.458476,9.416923,-5.651502,-8.532341,8.697959,-3.018051,6.088182,-2.334012,2.057569,1.994800,-8.684049,-1.447453,-4.572950,-2.221052,1.921343,-8.153561,5.807669,-1.618123,3.374316,-2.221557,-2.251820,-6.072818,-8.595174,8.706644,4.710825,-1.438849,-5.847561,-7.013737,1.257747,8.995429,4.402100,7.400433,2.888174,-8.540573,-9.816154,2.755282,-1.698850,-1.048593,1.277666,-5.870779,-0.273471,-5.202333,5.390198,4.300339,1.579628,8.412936,4.242518,5.794448,6.310928,3.012799,-5.511251,-1.533984,7.956743,7.036107,9.355916,0.281806,5.350490,-1.368266,-3.313716,1.173666,-7.800192,-8.776110,1.169625,-7.164457], dtype = "float64")#candidate|8656|(275,)|const|float64
call_8655 = func_1142_call(relay.reshape(const_8656.astype('float64'), [11, 5, 5]))
call_8657 = func_1142_call(relay.reshape(const_8656.astype('float64'), [11, 5, 5]))
output = relay.Tuple([uop_8651,call_8655,const_8656,])
output2 = relay.Tuple([uop_8651,call_8657,const_8656,])
func_8665 = relay.Function([var_8650,], output)
mod['func_8665'] = func_8665
mod = relay.transform.InferType()(mod)
var_8666 = relay.var("var_8666", dtype = "float32", shape = (15, 2, 3))#candidate|8666|(15, 2, 3)|var|float32
output = func_8665(var_8666)
func_8667 = relay.Function([var_8666], output)
mutated_mod['func_8667'] = func_8667
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8696 = relay.var("var_8696", dtype = "float32", shape = (1, 11, 13))#candidate|8696|(1, 11, 13)|var|float32
const_8697 = relay.const([[[0.339441,-7.921745,-7.081654,0.854321,9.657073,2.551725,-3.004849,-7.826945,2.465257,-8.028321,-3.985043,-8.897551,-8.109735],[4.198765,-9.216583,-4.761673,4.296967,3.731773,-7.754034,-2.403450,-7.684137,7.117412,-1.996957,8.966089,9.348677,4.928690],[7.213189,5.674325,-4.262495,-7.248799,7.041867,-3.770949,6.175142,9.996735,3.815518,2.338368,5.907993,-9.682816,7.392191],[6.461067,6.217979,-4.897065,-6.869826,2.467520,-3.282942,-5.288088,-7.138025,0.135912,-2.690267,-2.996404,-9.756617,6.652071],[-4.331590,0.297902,-2.890176,-2.987690,7.453733,-5.572127,-1.436373,4.259714,7.992794,2.432795,-9.005256,0.726454,1.206365],[-9.095640,-2.451948,4.786071,-3.042612,-6.899425,3.311331,-0.247192,8.310454,-7.633085,-0.958337,-2.243563,1.313206,-5.732635],[-8.826536,-5.431886,1.736653,9.380307,4.342040,-3.922804,-8.627368,-4.667418,-3.349363,-1.732513,8.855928,0.491327,-2.939080],[-9.124287,8.645369,-7.689572,-0.820801,4.111189,0.405736,5.398254,8.593632,-2.781844,-7.400898,5.874754,-9.282677,-6.512512],[9.539807,0.666516,-3.149326,3.101540,-2.059779,1.525616,2.400105,-6.335060,-5.010328,4.867792,-9.718704,7.433127,-2.075748],[7.266658,-7.558463,-5.459586,5.739480,-9.073101,5.669895,-1.730852,2.264596,7.895019,-7.610561,8.078060,7.160385,3.898102],[7.416642,3.327878,7.854106,-0.797626,-5.535566,8.997419,-9.282375,9.882905,-6.577599,-8.972033,-3.044477,-9.143123,9.040599]],[[7.163052,-2.695499,-5.705340,8.221675,2.168455,-9.915202,-1.106940,-7.615904,9.041643,9.572917,9.132824,-1.159694,5.465304],[3.597272,2.262048,-1.148153,5.843528,4.642310,-1.021063,4.831698,-5.022023,1.448767,8.025263,-5.726361,-9.488990,0.885480],[9.442406,5.385420,-5.855996,-9.794640,-7.000183,-9.591775,0.022298,8.979094,-4.449916,5.435155,8.311986,-7.541867,9.747375],[1.589438,-7.570997,3.704245,-3.639906,9.272182,4.368604,-9.372835,-8.819220,8.679692,3.437588,8.675096,-4.217092,-5.070113],[3.735882,-9.875611,7.912586,-0.140940,-6.257343,-9.516407,0.009248,-0.933966,2.067007,-8.786607,6.171517,-6.782021,-8.168899],[1.127549,-9.370949,-9.666092,-3.872520,-3.840614,-1.833098,9.661634,-0.525805,0.062172,7.932095,-8.636664,8.777332,-9.535404],[0.478457,6.869987,-8.898738,-5.547053,-4.784508,-2.756519,9.395886,-0.054885,-3.606688,-1.118051,3.611041,-9.795545,8.677187],[-3.686485,5.615591,-5.474358,8.624861,-5.937333,-0.255956,-6.459489,-6.464425,3.060654,-8.781318,6.681836,5.345682,9.773402],[-7.677089,-8.157800,0.643536,-2.424217,3.425169,6.806267,-2.752142,7.180367,-7.390273,3.258574,-5.458132,-6.875280,-0.302939],[2.429494,5.111493,6.283334,-5.875597,-2.945921,-2.665498,-5.874150,4.358627,-6.138412,-1.949394,-9.617605,1.550431,8.503981],[-6.966241,-5.036345,0.816256,-0.458850,9.434077,-2.996003,9.818215,7.696405,2.171377,-9.210402,1.126798,-2.959632,-6.894025]],[[-0.995520,-2.861081,3.183767,7.139076,-8.706245,-6.515992,5.262840,-5.313731,7.300454,-3.767774,4.228236,4.689835,-6.496461],[-2.606605,-7.588215,8.843541,-8.102972,-9.405642,-6.155393,-4.059456,-4.937532,-7.250364,-2.332645,-5.218565,-8.793864,-4.799376],[-1.170765,6.485023,-0.189647,-3.007325,-0.540552,1.618287,2.606351,8.477928,3.963748,-5.049197,-2.344568,2.671680,9.852252],[-5.234626,4.776837,6.554454,-8.805158,-0.124885,-7.560417,5.231302,0.787658,-3.688798,-6.115755,-7.709061,7.955956,-8.222964],[8.349809,-4.944402,3.826420,8.588197,2.972990,-1.905599,0.113373,-0.579065,2.976241,0.456497,-9.742215,-9.834759,0.562023],[-6.700558,4.560999,-4.147207,-4.706460,-4.759055,2.102455,-9.046093,-3.339027,0.771503,-3.356967,-9.768355,6.012197,-2.704437],[9.937472,9.991959,2.671646,9.838215,-0.279783,-8.126979,-1.296417,-9.288989,-5.923396,-8.134529,6.631788,-9.077310,6.604439],[-7.383252,-4.333573,-2.150391,6.988112,-1.341240,0.372374,9.109645,3.239831,-6.138612,-8.510036,-8.867453,-5.161921,-9.090032],[-3.146417,8.188281,7.707466,-3.383232,-7.421510,8.880551,-9.380981,-5.131083,7.850611,1.299933,6.924273,-4.433820,-2.593678],[-5.478213,1.311378,3.307678,-6.689170,4.848009,-3.652762,8.996269,-1.028975,-3.351366,9.389280,-9.296611,-2.935392,3.461555],[9.964413,-0.037454,-5.391368,-8.227723,1.233591,7.630229,-8.936970,1.364027,1.993228,0.735968,8.072474,-1.811600,9.804324]],[[0.355453,2.384571,1.636924,-2.501065,-3.906622,7.218901,-2.295805,-8.707730,-7.383317,-6.392514,0.398911,-0.783683,1.543160],[-7.632384,-4.869806,-2.575381,-7.782490,4.439774,-5.850446,1.105882,-6.393692,-0.206946,8.860273,0.230076,0.118547,6.292943],[3.828800,-8.870515,0.020241,-7.246444,-0.229915,6.998502,-4.390090,-9.604525,-3.375313,-0.046954,-5.554807,6.343769,9.587280],[3.747939,-6.084890,-8.807662,8.203954,-0.569478,0.537189,-3.647164,7.308912,-6.558402,-4.684989,-8.941974,-7.732660,-6.062418],[7.048177,-5.630924,-8.004953,-2.174063,-0.360522,-9.065215,6.892346,-8.106714,4.464839,-2.839049,-3.928432,0.008881,0.627412],[2.370636,-6.587863,9.929622,9.840439,-1.026580,1.542049,-3.800275,3.786783,1.650449,0.735681,-0.368818,3.555840,7.146589],[0.935995,-9.334395,0.068899,0.305837,0.197595,0.328207,-3.995393,-2.309656,-2.713083,-8.789864,1.915202,-2.200809,9.401477],[-4.696801,4.292630,3.063806,-0.868735,-8.724033,9.478276,3.807608,-9.591818,-6.718956,-9.391898,-6.408860,4.725490,9.893546],[8.742900,-7.640811,-4.508282,0.725784,-4.970815,-5.709857,-8.500363,-4.096725,-4.282235,8.691730,3.616509,-4.925695,-7.871007],[-0.951218,0.862216,6.412075,-5.997163,3.746201,-8.348061,-4.012865,5.868502,3.106397,7.827522,-8.794496,7.507314,-7.740442],[6.477898,-1.663404,-0.412525,5.997142,-8.938313,-8.749854,-6.350641,7.290206,-6.854890,-8.566718,4.012469,1.205969,8.408062]],[[-8.204218,4.300935,4.280952,3.761728,1.231371,4.666000,8.335379,0.667686,-9.661181,-6.959357,-5.924589,0.241891,-4.700935],[-7.224773,-0.278747,7.450384,-1.455501,3.060402,8.463731,2.657525,-3.180764,-4.457106,5.448815,6.558011,8.840625,0.688599],[-5.847743,-3.891509,5.949752,1.796892,5.201390,8.467415,5.418059,1.317126,4.581887,1.119979,3.241648,-7.942346,7.296537],[-7.806230,1.050941,-0.185600,1.796321,-0.858765,4.135651,-9.471455,9.712983,-1.683032,-2.240856,0.990529,3.701384,-3.382404],[-5.376176,4.708283,-7.675912,3.196841,7.242482,-9.722747,-4.941844,-4.864445,-7.817579,-4.373697,-8.501102,-2.093510,9.980695],[-7.333141,1.545729,6.075995,1.501741,0.915152,0.883841,3.844740,8.244790,0.928182,6.880476,0.820817,-9.197400,4.694129],[7.279292,6.773863,1.918032,2.430990,-0.320811,0.460907,4.520919,-9.367904,1.638840,2.613343,1.677213,-9.331656,-0.784702],[-0.944369,-7.953737,8.687430,9.481903,-8.538532,4.174518,8.356241,-4.841330,8.958325,-3.343932,-0.324194,-3.015868,-2.699386],[-6.555788,-9.043652,-7.177381,4.104905,-8.485679,-4.050126,-8.280244,-9.098032,-6.604233,2.232704,-5.323802,-3.210350,-7.244418],[-3.774469,9.148045,-8.787678,-4.198685,-9.823225,7.909414,0.749417,1.059754,-3.659990,-4.998153,3.226775,-9.529458,5.795616],[2.808289,8.706098,6.805153,-9.200549,-8.096064,-6.949789,4.132197,-5.169729,8.292410,-1.245396,4.385354,-9.232671,-8.792645]]], dtype = "float32")#candidate|8697|(5, 11, 13)|const|float32
bop_8698 = relay.minimum(var_8696.astype('float32'), const_8697.astype('float32')) # shape=(5, 11, 13)
func_6009_call = mod.get_global_var('func_6009')
func_6010_call = mutated_mod.get_global_var('func_6010')
call_8706 = func_6009_call()
call_8707 = func_6009_call()
output = relay.Tuple([bop_8698,call_8706,])
output2 = relay.Tuple([bop_8698,call_8707,])
func_8711 = relay.Function([var_8696,], output)
mod['func_8711'] = func_8711
mod = relay.transform.InferType()(mod)
mutated_mod['func_8711'] = func_8711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8712 = relay.var("var_8712", dtype = "float32", shape = (1, 11, 13))#candidate|8712|(1, 11, 13)|var|float32
func_8711_call = mutated_mod.get_global_var('func_8711')
call_8713 = func_8711_call(var_8712)
output = call_8713
func_8714 = relay.Function([var_8712], output)
mutated_mod['func_8714'] = func_8714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8100_call = mod.get_global_var('func_8100')
func_8101_call = mutated_mod.get_global_var('func_8101')
call_8755 = relay.TupleGetItem(func_8100_call(), 0)
call_8756 = relay.TupleGetItem(func_8101_call(), 0)
uop_8764 = relay.sinh(call_8755.astype('float32')) # shape=(275, 1)
uop_8766 = relay.sinh(call_8756.astype('float32')) # shape=(275, 1)
output = uop_8764
output2 = uop_8766
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
