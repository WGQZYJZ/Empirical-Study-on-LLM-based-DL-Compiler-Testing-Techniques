import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_36 = relay.var("var_36", dtype = "uint64", shape = (8, 5, 3))#candidate|36|(8, 5, 3)|var|uint64
var_37 = relay.var("var_37", dtype = "uint64", shape = (8, 5, 3))#candidate|37|(8, 5, 3)|var|uint64
bop_38 = relay.multiply(var_36.astype('uint64'), relay.reshape(var_37.astype('uint64'), relay.shape_of(var_36))) # shape=(8, 5, 3)
output = relay.Tuple([bop_38,])
output2 = relay.Tuple([bop_38,])
func_41 = relay.Function([var_36,var_37,], output)
mod['func_41'] = func_41
mod = relay.transform.InferType()(mod)
var_42 = relay.var("var_42", dtype = "uint64", shape = (8, 5, 3))#candidate|42|(8, 5, 3)|var|uint64
var_43 = relay.var("var_43", dtype = "uint64", shape = (8, 5, 3))#candidate|43|(8, 5, 3)|var|uint64
output = func_41(var_42,var_43,)
func_44 = relay.Function([var_42,var_43,], output)
mutated_mod['func_44'] = func_44
mutated_mod = relay.transform.InferType()(mutated_mod)
var_54 = relay.var("var_54", dtype = "uint32", shape = (11, 1, 7))#candidate|54|(11, 1, 7)|var|uint32
var_55 = relay.var("var_55", dtype = "uint32", shape = (11, 16, 7))#candidate|55|(11, 16, 7)|var|uint32
bop_56 = relay.left_shift(var_54.astype('uint32'), var_55.astype('uint32')) # shape=(11, 16, 7)
output = bop_56
output2 = bop_56
func_60 = relay.Function([var_54,var_55,], output)
mod['func_60'] = func_60
mod = relay.transform.InferType()(mod)
var_61 = relay.var("var_61", dtype = "uint32", shape = (11, 1, 7))#candidate|61|(11, 1, 7)|var|uint32
var_62 = relay.var("var_62", dtype = "uint32", shape = (11, 16, 7))#candidate|62|(11, 16, 7)|var|uint32
output = func_60(var_61,var_62,)
func_63 = relay.Function([var_61,var_62,], output)
mutated_mod['func_63'] = func_63
mutated_mod = relay.transform.InferType()(mutated_mod)
const_151 = relay.const([[[5.682984,-7.193492],[-5.432435,7.905782],[4.268678,-7.157278],[5.906166,5.288123],[-5.921737,2.362714],[8.912881,7.001318],[-1.698324,3.823861]]], dtype = "float64")#candidate|151|(1, 7, 2)|const|float64
var_152 = relay.var("var_152", dtype = "float64", shape = (16, 7, 2))#candidate|152|(16, 7, 2)|var|float64
bop_153 = relay.mod(const_151.astype('float64'), var_152.astype('float64')) # shape=(16, 7, 2)
bop_164 = relay.bitwise_or(bop_153.astype('int64'), const_151.astype('int64')) # shape=(16, 7, 2)
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
const_174 = relay.const([4,-1,3,7,-9,8,2,2,3,9,-7,-4,7,-8,-2,8,-8,2,2,-7,4,-8,-5,2,-10,-8,1,9,-1,-8,4,8,-7,-5,-10,2,6,-10,-10,-10,5,-5,-9,2,-5,-2,-8,-3,1,-4,10,4,-5,8,-9,6,-6,10,-7,-7,5,-3,2,-8,4,3,-1,10,5,1,-8,-8,10,-2,-2,-1,-2], dtype = "uint32")#candidate|174|(77,)|const|uint32
var_175 = relay.var("var_175", dtype = "uint32", shape = (1232,))#candidate|175|(1232,)|var|uint32
call_173 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(var_175.astype('uint32'), [11, 16, 7]), )
call_176 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(var_175.astype('uint32'), [11, 16, 7]), )
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
call_185 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(call_173.astype('uint32'), [11, 16, 7]), )
call_186 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(call_173.astype('uint32'), [11, 16, 7]), )
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
call_187 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(call_185.astype('uint32'), [11, 16, 7]), )
call_188 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(call_185.astype('uint32'), [11, 16, 7]), )
func_41_call = mod.get_global_var('func_41')
func_44_call = mutated_mod.get_global_var('func_44')
const_190 = relay.const([9,-5,-2,9,1,1,-2,2,4,7,10,5,5,7,6,-4,-3,-9,-9,-6,-4,2,-8,1,8,10,-7,4,-5,-1,-8,-5,-2,-5,-3,-3,6,4,-10,3,-2,5,-2,-1,-1,-9,5,-9,10,-10,-5,-9,-10,6,-7,7,-6,1,3,-4,-2,3,-6,-6,8,-9,-1,-7,-3,-1,4,2,-10,5,-6,-6,-1,-6,3,3,-8,-6,3,9,6,6,6,9,2,-9,-2,-7,-4,-10,-6,6,-7,4,8,4,3,-4,-10,7,7,-2,-1,-2,5,9,8,7,10,5,-5,1,-1,-9,10,-4], dtype = "uint64")#candidate|190|(120,)|const|uint64
call_189 = relay.TupleGetItem(func_41_call(relay.reshape(const_190.astype('uint64'), [8, 5, 3]), relay.reshape(const_190.astype('uint64'), [8, 5, 3]), ), 0)
call_191 = relay.TupleGetItem(func_44_call(relay.reshape(const_190.astype('uint64'), [8, 5, 3]), relay.reshape(const_190.astype('uint64'), [8, 5, 3]), ), 0)
bop_193 = relay.power(const_190.astype('float32'), relay.reshape(call_189.astype('float32'), relay.shape_of(const_190))) # shape=(120,)
bop_196 = relay.power(const_190.astype('float32'), relay.reshape(call_191.astype('float32'), relay.shape_of(const_190))) # shape=(120,)
bop_200 = relay.equal(bop_153.astype('bool'), relay.reshape(bop_164.astype('bool'), relay.shape_of(bop_153))) # shape=(16, 7, 2)
var_205 = relay.var("var_205", dtype = "uint32", shape = (11, 16, 7))#candidate|205|(11, 16, 7)|var|uint32
bop_206 = relay.bitwise_and(call_173.astype('uint32'), relay.reshape(var_205.astype('uint32'), relay.shape_of(call_173))) # shape=(11, 16, 7)
bop_209 = relay.bitwise_and(call_176.astype('uint32'), relay.reshape(var_205.astype('uint32'), relay.shape_of(call_176))) # shape=(11, 16, 7)
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
call_211 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(bop_206.astype('uint32'), [11, 16, 7]), )
call_212 = func_60_call(relay.reshape(const_174.astype('uint32'), [11, 1, 7]), relay.reshape(bop_206.astype('uint32'), [11, 16, 7]), )
uop_228 = relay.sin(call_173.astype('float32')) # shape=(11, 16, 7)
uop_230 = relay.sin(call_176.astype('float32')) # shape=(11, 16, 7)
output = relay.Tuple([const_174,var_175,call_185,call_187,bop_193,bop_200,bop_206,call_211,uop_228,])
output2 = relay.Tuple([const_174,var_175,call_186,call_188,bop_196,bop_200,bop_209,call_212,uop_230,])
func_242 = relay.Function([var_152,var_175,var_205,], output)
mod['func_242'] = func_242
mod = relay.transform.InferType()(mod)
var_243 = relay.var("var_243", dtype = "float64", shape = (16, 7, 2))#candidate|243|(16, 7, 2)|var|float64
var_244 = relay.var("var_244", dtype = "uint32", shape = (1232,))#candidate|244|(1232,)|var|uint32
var_245 = relay.var("var_245", dtype = "uint32", shape = (11, 16, 7))#candidate|245|(11, 16, 7)|var|uint32
output = func_242(var_243,var_244,var_245,)
func_246 = relay.Function([var_243,var_244,var_245,], output)
mutated_mod['func_246'] = func_246
mutated_mod = relay.transform.InferType()(mutated_mod)
var_372 = relay.var("var_372", dtype = "float64", shape = ())#candidate|372|()|var|float64
var_373 = relay.var("var_373", dtype = "float64", shape = (1, 14, 11))#candidate|373|(1, 14, 11)|var|float64
bop_374 = relay.divide(var_372.astype('float64'), var_373.astype('float64')) # shape=(1, 14, 11)
func_242_call = mod.get_global_var('func_242')
func_246_call = mutated_mod.get_global_var('func_246')
var_380 = relay.var("var_380", dtype = "float64", shape = (1, 224))#candidate|380|(1, 224)|var|float64
var_381 = relay.var("var_381", dtype = "uint32", shape = (1232,))#candidate|381|(1232,)|var|uint32
call_379 = relay.TupleGetItem(func_242_call(relay.reshape(var_380.astype('float64'), [16, 7, 2]), relay.reshape(var_381.astype('uint32'), [1232,]), relay.reshape(var_381.astype('uint32'), [11, 16, 7]), ), 5)
call_382 = relay.TupleGetItem(func_246_call(relay.reshape(var_380.astype('float64'), [16, 7, 2]), relay.reshape(var_381.astype('uint32'), [1232,]), relay.reshape(var_381.astype('uint32'), [11, 16, 7]), ), 5)
func_41_call = mod.get_global_var('func_41')
func_44_call = mutated_mod.get_global_var('func_44')
var_384 = relay.var("var_384", dtype = "uint64", shape = (120,))#candidate|384|(120,)|var|uint64
call_383 = relay.TupleGetItem(func_41_call(relay.reshape(var_384.astype('uint64'), [8, 5, 3]), relay.reshape(var_384.astype('uint64'), [8, 5, 3]), ), 0)
call_385 = relay.TupleGetItem(func_44_call(relay.reshape(var_384.astype('uint64'), [8, 5, 3]), relay.reshape(var_384.astype('uint64'), [8, 5, 3]), ), 0)
var_387 = relay.var("var_387", dtype = "uint64", shape = (8, 5, 3))#candidate|387|(8, 5, 3)|var|uint64
bop_388 = relay.maximum(call_383.astype('uint16'), relay.reshape(var_387.astype('uint16'), relay.shape_of(call_383))) # shape=(8, 5, 3)
bop_391 = relay.maximum(call_385.astype('uint16'), relay.reshape(var_387.astype('uint16'), relay.shape_of(call_385))) # shape=(8, 5, 3)
func_242_call = mod.get_global_var('func_242')
func_246_call = mutated_mod.get_global_var('func_246')
call_392 = relay.TupleGetItem(func_242_call(relay.reshape(call_379.astype('float64'), [16, 7, 2]), relay.reshape(var_381.astype('uint32'), [1232,]), relay.reshape(var_381.astype('uint32'), [11, 16, 7]), ), 3)
call_393 = relay.TupleGetItem(func_246_call(relay.reshape(call_379.astype('float64'), [16, 7, 2]), relay.reshape(var_381.astype('uint32'), [1232,]), relay.reshape(var_381.astype('uint32'), [11, 16, 7]), ), 3)
output = relay.Tuple([bop_374,call_379,var_380,var_381,var_384,bop_388,call_392,])
output2 = relay.Tuple([bop_374,call_382,var_380,var_381,var_384,bop_391,call_393,])
func_397 = relay.Function([var_372,var_373,var_380,var_381,var_384,var_387,], output)
mod['func_397'] = func_397
mod = relay.transform.InferType()(mod)
var_398 = relay.var("var_398", dtype = "float64", shape = ())#candidate|398|()|var|float64
var_399 = relay.var("var_399", dtype = "float64", shape = (1, 14, 11))#candidate|399|(1, 14, 11)|var|float64
var_400 = relay.var("var_400", dtype = "float64", shape = (1, 224))#candidate|400|(1, 224)|var|float64
var_401 = relay.var("var_401", dtype = "uint32", shape = (1232,))#candidate|401|(1232,)|var|uint32
var_402 = relay.var("var_402", dtype = "uint64", shape = (120,))#candidate|402|(120,)|var|uint64
var_403 = relay.var("var_403", dtype = "uint64", shape = (8, 5, 3))#candidate|403|(8, 5, 3)|var|uint64
output = func_397(var_398,var_399,var_400,var_401,var_402,var_403,)
func_404 = relay.Function([var_398,var_399,var_400,var_401,var_402,var_403,], output)
mutated_mod['func_404'] = func_404
mutated_mod = relay.transform.InferType()(mutated_mod)
const_470 = relay.const([[[-1,9,-6,-6,3,-7,-4,5,-9,-10,2,-5,9]],[[-7,10,-10,-6,10,7,10,3,8,-4,-5,-2,1]],[[4,-10,-10,9,-10,2,7,7,7,-7,-7,-8,-8]],[[5,-2,3,2,7,10,-3,-5,6,4,10,-3,2]],[[10,10,-4,7,1,2,-3,5,-4,-6,3,3,-7]],[[1,-9,-1,-4,8,-6,-6,7,10,6,7,-4,-1]],[[5,6,-8,-4,-1,-8,6,5,-5,6,-8,3,-2]],[[7,3,4,-1,-2,7,-8,10,1,5,7,8,1]]], dtype = "int16")#candidate|470|(8, 1, 13)|const|int16
var_471 = relay.var("var_471", dtype = "int16", shape = (8, 14, 13))#candidate|471|(8, 14, 13)|var|int16
bop_472 = relay.minimum(const_470.astype('int16'), var_471.astype('int16')) # shape=(8, 14, 13)
bop_475 = relay.left_shift(const_470.astype('int32'), bop_472.astype('int32')) # shape=(8, 14, 13)
output = bop_475
output2 = bop_475
func_479 = relay.Function([var_471,], output)
mod['func_479'] = func_479
mod = relay.transform.InferType()(mod)
mutated_mod['func_479'] = func_479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_480 = relay.var("var_480", dtype = "int16", shape = (8, 14, 13))#candidate|480|(8, 14, 13)|var|int16
func_479_call = mutated_mod.get_global_var('func_479')
call_481 = func_479_call(var_480)
output = call_481
func_482 = relay.Function([var_480], output)
mutated_mod['func_482'] = func_482
mutated_mod = relay.transform.InferType()(mutated_mod)
var_730 = relay.var("var_730", dtype = "float32", shape = (6, 7, 8))#candidate|730|(6, 7, 8)|var|float32
var_731 = relay.var("var_731", dtype = "float32", shape = (6, 7, 8))#candidate|731|(6, 7, 8)|var|float32
bop_732 = relay.greater_equal(var_730.astype('bool'), relay.reshape(var_731.astype('bool'), relay.shape_of(var_730))) # shape=(6, 7, 8)
func_41_call = mod.get_global_var('func_41')
func_44_call = mutated_mod.get_global_var('func_44')
var_738 = relay.var("var_738", dtype = "uint64", shape = (120,))#candidate|738|(120,)|var|uint64
call_737 = relay.TupleGetItem(func_41_call(relay.reshape(var_738.astype('uint64'), [8, 5, 3]), relay.reshape(var_738.astype('uint64'), [8, 5, 3]), ), 0)
call_739 = relay.TupleGetItem(func_44_call(relay.reshape(var_738.astype('uint64'), [8, 5, 3]), relay.reshape(var_738.astype('uint64'), [8, 5, 3]), ), 0)
bop_749 = relay.multiply(var_731.astype('uint64'), relay.reshape(var_730.astype('uint64'), relay.shape_of(var_731))) # shape=(6, 7, 8)
uop_765 = relay.acos(bop_749.astype('float64')) # shape=(6, 7, 8)
bop_771 = relay.logical_and(uop_765.astype('bool'), relay.reshape(var_731.astype('bool'), relay.shape_of(uop_765))) # shape=(6, 7, 8)
uop_775 = relay.log(uop_765.astype('float64')) # shape=(6, 7, 8)
output = relay.Tuple([bop_732,call_737,var_738,bop_771,uop_775,])
output2 = relay.Tuple([bop_732,call_739,var_738,bop_771,uop_775,])
func_777 = relay.Function([var_730,var_731,var_738,], output)
mod['func_777'] = func_777
mod = relay.transform.InferType()(mod)
var_778 = relay.var("var_778", dtype = "float32", shape = (6, 7, 8))#candidate|778|(6, 7, 8)|var|float32
var_779 = relay.var("var_779", dtype = "float32", shape = (6, 7, 8))#candidate|779|(6, 7, 8)|var|float32
var_780 = relay.var("var_780", dtype = "uint64", shape = (120,))#candidate|780|(120,)|var|uint64
output = func_777(var_778,var_779,var_780,)
func_781 = relay.Function([var_778,var_779,var_780,], output)
mutated_mod['func_781'] = func_781
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1149 = relay.var("var_1149", dtype = "float64", shape = (4, 1, 1))#candidate|1149|(4, 1, 1)|var|float64
uop_1150 = relay.atanh(var_1149.astype('float64')) # shape=(4, 1, 1)
output = uop_1150
output2 = uop_1150
func_1152 = relay.Function([var_1149,], output)
mod['func_1152'] = func_1152
mod = relay.transform.InferType()(mod)
var_1153 = relay.var("var_1153", dtype = "float64", shape = (4, 1, 1))#candidate|1153|(4, 1, 1)|var|float64
output = func_1152(var_1153)
func_1154 = relay.Function([var_1153], output)
mutated_mod['func_1154'] = func_1154
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1891 = relay.var("var_1891", dtype = "int64", shape = (11, 11, 5))#candidate|1891|(11, 11, 5)|var|int64
const_1892 = relay.const([[[5,7,3,10,-7],[-5,-3,6,-10,7],[-10,2,4,-2,5],[2,-5,1,-8,7],[-8,-2,3,10,2],[9,-10,2,2,2],[9,-7,-4,4,3],[-7,-8,-4,1,-2],[-1,-5,-1,6,4],[-3,3,-7,10,9],[5,-6,9,3,4]],[[-2,-6,8,5,-3],[4,-2,-7,4,-2],[-3,-2,-1,-9,-2],[-8,5,-3,-3,7],[-9,-1,-9,-2,8],[-9,3,9,4,-6],[8,1,8,-8,-4],[7,7,-4,6,9],[-10,-4,10,4,-9],[8,-4,3,-5,-3],[6,-10,-7,7,-10]],[[7,5,-10,-7,6],[-5,-5,7,1,9],[-1,-1,7,-7,1],[-1,7,4,-10,4],[-8,2,7,1,9],[1,6,1,2,-10],[-5,-3,-8,2,7],[3,6,-9,5,3],[4,6,-8,3,-6],[2,3,-6,4,6],[5,-9,5,5,9]],[[-5,-6,3,7,3],[-1,7,-4,-5,-10],[-2,-2,-5,10,-8],[2,4,-4,1,4],[-7,2,-9,6,5],[-6,-2,-9,-9,8],[7,-3,-7,7,2],[-5,8,-4,4,-2],[-7,-7,9,5,4],[-5,5,-2,-7,-4],[2,-8,5,-9,2]],[[-9,10,-8,-1,-6],[6,3,-9,6,6],[3,-7,10,2,2],[-1,-5,-6,-9,-5],[9,-6,3,-9,-1],[8,7,-6,-9,8],[-6,-2,-9,1,-3],[-5,-8,-7,6,1],[-3,3,4,6,-10],[7,-3,-7,5,-2],[-6,1,8,4,-5]],[[3,-6,5,8,5],[6,-3,9,3,8],[2,-2,8,2,6],[-9,-3,-7,-4,4],[2,1,10,7,-6],[9,-9,-3,-3,-10],[-2,9,-3,6,3],[9,1,-3,2,2],[-5,5,4,-2,5],[-5,1,2,2,5],[7,1,6,9,-3]],[[5,4,3,-10,-4],[-7,9,6,-5,-9],[-4,-4,6,-10,-7],[10,1,4,3,-1],[8,-9,-7,10,3],[-2,-10,1,-6,3],[-4,-7,-8,-2,-4],[7,10,-1,-10,1],[-10,10,1,6,-2],[3,3,-4,-1,-9],[7,7,3,-6,-8]],[[-6,-10,-10,8,8],[-6,-8,1,9,8],[6,-5,3,-10,-1],[-4,9,-3,-4,-5],[-3,-3,10,-4,-7],[7,6,-6,-2,-9],[-7,1,-8,-4,-7],[5,10,10,-4,-8],[-7,-4,-9,-3,7],[3,7,-9,-10,7],[2,5,10,9,-2]],[[-2,-2,-1,7,1],[7,9,9,9,2],[5,8,5,9,-9],[-3,-9,7,5,7],[-9,9,8,-7,5],[3,-5,-4,-6,-4],[-4,-7,-1,7,10],[1,6,-7,-8,-3],[6,-5,-6,9,1],[-8,10,10,-10,7],[-8,-9,-8,1,3]],[[-1,10,9,-6,-10],[4,4,3,-5,-10],[5,3,-4,-2,-1],[1,-3,-9,-10,3],[-3,-8,-2,10,8],[-2,-8,8,-7,9],[5,-9,2,3,4],[2,4,4,-4,5],[-4,6,-3,-8,-5],[8,8,10,-7,3],[-2,9,-6,-4,-1]],[[4,-6,-9,-5,9],[3,-9,5,2,6],[-3,10,-4,9,7],[-5,-5,-1,9,-1],[-5,-6,-7,8,2],[3,-10,-9,9,2],[-8,-9,9,-7,-6],[-7,-7,9,-5,-1],[9,-4,7,5,1],[-2,-8,4,-10,6],[-3,1,9,2,-5]]], dtype = "int64")#candidate|1892|(11, 11, 5)|const|int64
bop_1893 = relay.add(var_1891.astype('int64'), relay.reshape(const_1892.astype('int64'), relay.shape_of(var_1891))) # shape=(11, 11, 5)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
const_1904 = relay.const([-3.889191,-6.689825,9.562815,-4.396036], dtype = "float64")#candidate|1904|(4,)|const|float64
call_1903 = func_1152_call(relay.reshape(const_1904.astype('float64'), [4, 1, 1]))
call_1905 = func_1152_call(relay.reshape(const_1904.astype('float64'), [4, 1, 1]))
output = relay.Tuple([bop_1893,call_1903,const_1904,])
output2 = relay.Tuple([bop_1893,call_1905,const_1904,])
func_1912 = relay.Function([var_1891,], output)
mod['func_1912'] = func_1912
mod = relay.transform.InferType()(mod)
mutated_mod['func_1912'] = func_1912
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1913 = relay.var("var_1913", dtype = "int64", shape = (11, 11, 5))#candidate|1913|(11, 11, 5)|var|int64
func_1912_call = mutated_mod.get_global_var('func_1912')
call_1914 = func_1912_call(var_1913)
output = call_1914
func_1915 = relay.Function([var_1913], output)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2221 = relay.var("var_2221", dtype = "float32", shape = (1, 7, 3))#candidate|2221|(1, 7, 3)|var|float32
uop_2222 = relay.asinh(var_2221.astype('float32')) # shape=(1, 7, 3)
bop_2224 = relay.equal(uop_2222.astype('bool'), relay.reshape(var_2221.astype('bool'), relay.shape_of(uop_2222))) # shape=(1, 7, 3)
const_2236 = relay.const([[[-5.819731,-8.967636,-7.904538],[-9.457547,-2.241980,-0.243713],[0.179302,-8.384118,-4.333220],[-3.188269,0.995812,1.964701],[8.671875,-8.067063,1.597702],[-6.048122,2.010601,5.115412],[8.767784,4.921030,-5.896690]],[[-9.114602,7.377045,-3.271744],[-2.634459,-1.827547,-6.857020],[5.100223,-7.758783,8.750487],[-6.849334,8.377845,4.446261],[1.907780,-0.031549,-0.336121],[-9.311089,4.104908,4.926947],[4.504839,-3.523741,-5.773284]],[[-2.761479,-8.827027,4.755716],[-2.505604,-1.417851,2.837172],[-8.163335,-0.311946,1.565479],[-9.951983,0.771189,-5.367766],[1.296914,8.644093,4.262480],[-3.375349,8.376169,-4.404653],[9.553688,-8.162216,8.739071]],[[8.966130,1.889737,-3.544171],[-7.835722,-0.007748,-2.521813],[-7.232824,5.640800,7.436542],[4.787694,-4.019972,3.218053],[-5.760862,8.254049,-7.710549],[-9.645666,-2.943366,6.680407],[3.061286,7.411131,2.118688]],[[-3.573207,5.575129,2.402586],[-7.841041,2.798476,-9.226133],[0.001089,2.874919,5.105821],[7.253793,0.627553,9.347843],[3.005941,-6.450503,0.505005],[-1.447054,1.261154,2.327515],[6.329070,-6.312543,-1.286456]],[[6.652533,5.294890,-7.297482],[-7.442560,-1.827372,6.587583],[-3.568518,-2.822112,-4.388445],[-6.264733,5.926657,-3.684043],[2.422922,-7.169854,-6.266079],[-1.394134,1.537352,-0.217737],[-8.781934,0.141692,-8.632392]]], dtype = "float32")#candidate|2236|(6, 7, 3)|const|float32
bop_2237 = relay.equal(var_2221.astype('bool'), const_2236.astype('bool')) # shape=(6, 7, 3)
func_479_call = mod.get_global_var('func_479')
func_482_call = mutated_mod.get_global_var('func_482')
const_2247 = relay.const([1,10,-1,10,-10,6,-8,-6,-1,1,5,-3,3,7,9,7,-1,5,-3,-5,-9,6,-5,-6,-9,10,-6,10,-7,3,3,6,-6,-8,-8,-1,-4,-4,1,3,-6,-3,-8,-2,-2,-2,4,8,1,-8,-1,-5,5,-3,-9,6,3,-8,4,5,6,10,-7,9,-8,-8,3,5,-3,6,-7,7,-4,1,4,4,5,-7,4,-2,-2,-1,-4,-5,-5,8,5,-1,10,-7,-10,-4,4,-7,9,1,10,4,-8,-10,2,-4,5,6,-9,-2,3,-4,-7,-5,10,8,8,5,-3,-9,-5,1,-10,9,-9,8,7,3,3,-2,6,5,2,-9,5,9,1,-3,-7,2,-3,2,-4,-6,2,2,-6,1,-8,-4,-8,-4,2,-2,10,-5,-6,-3,-1,-9,-4,9,9,1,-10,-10,-7,7,-4,8,-5,-6,-1,1,-7,3,3,-5,-1,10,9,-10,-6,4,6,-1,7,1,-8,8,-5,9,2,-10,10,8,8,6,3,-4,-3,9,4,-6,4,-10,-4,7,-2,-2,-7,-2,6,-10,7,1,9,-10,2,7,-9,-7,7,10,10,-2,2,-3,1,1,-5,1,-2,9,6,-2,-5,9,-2,9,-3,-1,6,-5,-7,-8,1,-8,-10,-9,-3,3,-7,-7,-3,2,-1,1,7,8,-6,-6,-6,8,-9,4,7,1,-8,-4,7,7,9,7,5,9,2,8,10,-5,4,-3,5,-4,2,-5,4,-7,1,-8,-7,-10,4,8,4,3,1,9,-9,10,-1,-10,-7,7,-1,6,5,9,-2,3,8,-5,3,-6,5,8,1,2,-7,5,5,9,7,-9,-5,-6,10,4,3,10,6,-7,-5,4,-7,1,-2,2,-6,-8,-5,6,4,-1,-1,-9,8,-3,-3,5,8,2,6,-9,8,5,-2,1,2,4,-4,2,7,4,-4,9,-5,-4,-6,-5,-10,8,-3,7,2,1,-2,-5,-8,-10,8,-6,10,-5,-3,-3,-3,3,1,-3,1,6,-7,-4,-1,-9,4,5,-7,2,-3,3,9,1,-7,-4,8,-2,2,2,-10,4,8,8,10,-5,9,8,-5,-10,5,1,-4,10,10,-1,5,-4,7,-10,6,-9,-5,-2,9,-5,6,10,10,9,-6,-10,-8,-5,8,1,3,8,-8,-2,-4,1,-4,3,-3,-6,3,-1,2,-3,1,6,-3,-4,7,-7,-3,-5,9,3,-8,-2,-4,-9,9,9,-7,6,1,2,5,1,8,-9,3,1,-10,10,8,-4,-5,-6,10,-4,-3,-1,6,8,-9,10,-8,1,6,4,5,10,3,-4,-10,-3,7,-1,5,6,6,-4,-9,-2,8,-8,8,-3,-5,-1,5,8,-8,-6,6,-9,-8,-7,-9,3,-9,-10,-2,-5,10,-2,1,-9,-6,-6,-5,-5,7,3,4,-5,8,7,10,6,1,-5,7,3,-8,-6,-3,7,6,8,-7,-1,10,-6,-4,-10,-10,7,-10,-9,-9,-1,-9,-2,10,2,-5,-4,-3,-7,3,-1,-4,-8,-1,3,5,2,-4,-6,-6,-4,3,6,-10,-4,2,-6,6,-9,3,6,-5,2,3,-6,8,10,9,9,10,-10,1,-7,10,-3,-9,4,7,5,-4,9,-10,5,-4,7,-10,-6,-5,-5,2,-9,-6,7,9,-5,3,-8,2,10,-10,2,6,-8,-3,-5,10,8,-8,-1,-6,-1,10,-10,5,-8,9,-2,10,-5,2,9,-7,-1,-9,4,-1,-4,6,-3,6,-3,-5,-1,4,9,-7,9,-3,-8,3,10,9,-6,8,4,-5,8,-2,5,4,-2,-10,6,1,10,6,-9,3,-7,-7,4,8,1,10,5,-10,6,8,-5,-6,5,4,8,-3,8,-8,1,-6,-5,8,2,-7,-8,-2,5,10,3,-8,-3,6,9,6,1,4,-8,-7,2,3,-10,5,-7,7,-10,9,-4,-5,-2,-6,-2,-8,-3,-3,9,-5,2,-4,6,9,6,7,6,4,-4,-8,1,7,10,-8,-9,-10,2,2,-5,4,-8,1,7,-1,-6,-5,4,10,3,7,-1,-5,-10,3,-5,-7,9,8,-3,-7,7,-3,-6,-8,-1,1,1,4,-2,-5,3,-1,-9,-10,-9,9,-7,-8,7,1,9,7,9,-1,8,9,7,-4,10,-7,9,4,10,10,-6,-3,-7,6,2,1,3,-1,-10,7,1,9,-9,7,-5,-7,1,7,-2,8,-8,6,-6,2,-4,-8,-2,-6,-9,2,-3,4,-3,-4,4,1,-8,5,-5,-2,5,-5,-6,-2,3,1,-5,10,6,4,-5,-1,-3,-8,3,-9,-1,-7,-5,-4,-3,4,1,-7,-9,6,6,-6,-6,-7,-6,9,-1,6,7,6,-6,9,6,4,-9,-7,10,3,-10,4,9,5,2,-5,3,9,2,7,-8,-1,-3,-1,4,6,-6,-1,-4,4,10,-2,-1,-4,-3,-2,4,-7,4,8,3,3,6,4,-2,5,10,-7,-10,-5,-10,3,2,10,7,-3,2,8,4,8,-2,8,-10,-2,-5,-5,-6,8,-8,4,-6,4,5,-8,5,4,8,-9,8,3,10,8,-8,-6,7,-10,6,-3,-7,1,8,9,-1,8,-10,3,-9,-8,9,3,-1,-1,8,-2,-6,7,10,1,4,1,10,-4,4,8,-5,9,6,4,3,-1,1,-4,5,2,-5,-3,-6,-6,8,-4,-4,8,-3,4,-10,-7,-4,-2,6,-8,1,-8,8,-9,-7,-7,8,-9,-8,8,-9,-9,-6,1,8,-5,-1,-6,-6,-3,-10,1,8,8,4,-5,3,-7,-8,-2,-8,-5,-1,-7,-8,7,-5,-5,-10,-10,-10,-1,-1,-3,5,-5,-4,3,3,-10,2,-8,-10,9,-5,8,4,-8,6,-1,-7,-7,7,6,-9,1,-8,10,2,-7,8,2,-3,-4,2,-3,2,-1,7,10,-6,9,2,9,9,-2,-1,9,-5,-6,-10,7,6,-2,-5,-3,7,-4,-3,4,-9,9,1,8,10,-4,-3,-2,-8,6,-1,6,-10,7,-1,5,7,4,3,5,-5,6,9,7,-4,-3,-1,-1,7,-6,8,2,9,-5,-7,-8,7,-10,-1,6,-1,10,-5,-5,-10,-3,-4,6,-1,4,9,-8,-5,5,-7,-1,9,10,-4,-8,-4,3,-6,-1,-9,-4,-6,-7,3,7,4,-8,-9,6,-1,-8,-7,-5,1,1,1,-10,-10,-8,-8,2,-2,4,-7,7,-7,5,9,1,7,9,9,-5,-6,-1,9,-6,-6,-4,-1,2,-7,3,8,7,-8,-3,8,6,-10,-8,-2,2,5,10,-9,5,9,4,-4,3,9,-6,4,1,-1,-5,-5,3,-4,-7,5,-1,-4,4,-7,-9,-4,5,9,4,-5,4,-7,-2,-2,-6,-3,-5,-3,4,-7,8,7,1,-9,7,3,4,10,3,-4,-1,5,3,-5,9,9,-5,-3,2,1,-8,1,-8,-7,-3,7,10,-9,1,-2,-8,-2,-5,1,-8,7,1,-9,8,-10,-9,-6,1,1,-9,-4,4,-4,-4,-8,-1,10,4,-1,-5,5,7,10,7,2,6,5,-6,3,-5,-2,-6,6,-10,-2,9,-7,-9,6,2,-1,6,2,-6,9,4,6,4,1,3,8,-3,8,-6,7,2,8,-6,1,-5,-3,-4,2,3,1,-9,7,8,5,10,1,9,-2,-2,-5,3,-8,9,4,-3,7,6,5,9,-7,1,-3,-1,-5,7,-10,10,-9,7,-10,-10,4,10,9,1,-8,-6,-3,5,-10,10,5,9,6,7,6,-2,3,-2,-1,10,5,4,3,-8,4], dtype = "int16")#candidate|2247|(1456,)|const|int16
call_2246 = func_479_call(relay.reshape(const_2247.astype('int16'), [8, 14, 13]))
call_2248 = func_479_call(relay.reshape(const_2247.astype('int16'), [8, 14, 13]))
func_1912_call = mod.get_global_var('func_1912')
func_1915_call = mutated_mod.get_global_var('func_1915')
var_2258 = relay.var("var_2258", dtype = "int64", shape = (605,))#candidate|2258|(605,)|var|int64
call_2257 = relay.TupleGetItem(func_1912_call(relay.reshape(var_2258.astype('int64'), [11, 11, 5])), 0)
call_2259 = relay.TupleGetItem(func_1915_call(relay.reshape(var_2258.astype('int64'), [11, 11, 5])), 0)
output = relay.Tuple([bop_2224,bop_2237,call_2246,const_2247,call_2257,var_2258,])
output2 = relay.Tuple([bop_2224,bop_2237,call_2248,const_2247,call_2259,var_2258,])
func_2260 = relay.Function([var_2221,var_2258,], output)
mod['func_2260'] = func_2260
mod = relay.transform.InferType()(mod)
mutated_mod['func_2260'] = func_2260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2260_call = mutated_mod.get_global_var('func_2260')
var_2262 = relay.var("var_2262", dtype = "float32", shape = (1, 7, 3))#candidate|2262|(1, 7, 3)|var|float32
var_2263 = relay.var("var_2263", dtype = "int64", shape = (605,))#candidate|2263|(605,)|var|int64
call_2261 = func_2260_call(var_2262,var_2263,)
output = call_2261
func_2264 = relay.Function([var_2262,var_2263,], output)
mutated_mod['func_2264'] = func_2264
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2320 = relay.var("var_2320", dtype = "float32", shape = (10, 16, 11))#candidate|2320|(10, 16, 11)|var|float32
uop_2321 = relay.log(var_2320.astype('float32')) # shape=(10, 16, 11)
bop_2339 = relay.right_shift(var_2320.astype('int8'), relay.reshape(uop_2321.astype('int8'), relay.shape_of(var_2320))) # shape=(10, 16, 11)
func_479_call = mod.get_global_var('func_479')
func_482_call = mutated_mod.get_global_var('func_482')
var_2345 = relay.var("var_2345", dtype = "int16", shape = (1456,))#candidate|2345|(1456,)|var|int16
call_2344 = func_479_call(relay.reshape(var_2345.astype('int16'), [8, 14, 13]))
call_2346 = func_479_call(relay.reshape(var_2345.astype('int16'), [8, 14, 13]))
bop_2350 = relay.floor_divide(bop_2339.astype('float64'), relay.reshape(uop_2321.astype('float64'), relay.shape_of(bop_2339))) # shape=(10, 16, 11)
uop_2361 = relay.acos(uop_2321.astype('float32')) # shape=(10, 16, 11)
output = relay.Tuple([call_2344,var_2345,bop_2350,uop_2361,])
output2 = relay.Tuple([call_2346,var_2345,bop_2350,uop_2361,])
func_2363 = relay.Function([var_2320,var_2345,], output)
mod['func_2363'] = func_2363
mod = relay.transform.InferType()(mod)
mutated_mod['func_2363'] = func_2363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2363_call = mutated_mod.get_global_var('func_2363')
var_2365 = relay.var("var_2365", dtype = "float32", shape = (10, 16, 11))#candidate|2365|(10, 16, 11)|var|float32
var_2366 = relay.var("var_2366", dtype = "int16", shape = (1456,))#candidate|2366|(1456,)|var|int16
call_2364 = func_2363_call(var_2365,var_2366,)
output = call_2364
func_2367 = relay.Function([var_2365,var_2366,], output)
mutated_mod['func_2367'] = func_2367
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2670 = relay.var("var_2670", dtype = "float32", shape = (5, 5, 6))#candidate|2670|(5, 5, 6)|var|float32
uop_2671 = relay.cos(var_2670.astype('float32')) # shape=(5, 5, 6)
bop_2673 = relay.right_shift(uop_2671.astype('int8'), relay.reshape(var_2670.astype('int8'), relay.shape_of(uop_2671))) # shape=(5, 5, 6)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
var_2679 = relay.var("var_2679", dtype = "float64", shape = (1, 4))#candidate|2679|(1, 4)|var|float64
call_2678 = func_1152_call(relay.reshape(var_2679.astype('float64'), [4, 1, 1]))
call_2680 = func_1152_call(relay.reshape(var_2679.astype('float64'), [4, 1, 1]))
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
call_2681 = func_1152_call(relay.reshape(call_2678.astype('float64'), [4, 1, 1]))
call_2682 = func_1152_call(relay.reshape(call_2678.astype('float64'), [4, 1, 1]))
output = relay.Tuple([bop_2673,call_2678,var_2679,call_2681,])
output2 = relay.Tuple([bop_2673,call_2680,var_2679,call_2682,])
func_2688 = relay.Function([var_2670,var_2679,], output)
mod['func_2688'] = func_2688
mod = relay.transform.InferType()(mod)
var_2689 = relay.var("var_2689", dtype = "float32", shape = (5, 5, 6))#candidate|2689|(5, 5, 6)|var|float32
var_2690 = relay.var("var_2690", dtype = "float64", shape = (1, 4))#candidate|2690|(1, 4)|var|float64
output = func_2688(var_2689,var_2690,)
func_2691 = relay.Function([var_2689,var_2690,], output)
mutated_mod['func_2691'] = func_2691
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2925 = relay.const([[[1.909847,2.143100,-3.077071,7.641329,5.736713,5.909314,-3.277472,6.421345],[-2.083297,4.346361,-1.981592,-3.264819,2.821131,-8.360245,-1.071837,-2.351015],[-1.906464,1.365442,0.773572,-2.638489,3.021347,6.769839,6.393049,2.568645],[4.722298,2.829595,6.028719,-3.042350,2.809907,-7.161054,-7.109404,4.516440],[-3.776826,3.013600,-3.739238,-5.676133,4.651826,5.978527,9.059844,-5.520155],[-1.882865,-0.468896,-4.799150,-1.865362,7.748070,8.886945,1.826503,-1.174049],[6.363978,4.687283,-1.703537,5.839055,4.779504,-3.270578,-9.574853,-7.546893],[-0.251965,-9.191744,8.151972,1.028879,1.552416,-7.109635,0.238878,-7.275197],[2.118555,-1.665546,-2.153700,1.841959,9.986904,-7.267493,3.968541,-5.347968],[2.091538,-0.465044,7.830626,-9.869656,-0.316109,7.401441,9.851508,2.472859],[-2.218684,-5.874812,6.164984,-5.824334,-6.128341,-3.280617,9.218593,8.959865]],[[4.954138,2.657498,3.050354,3.037246,6.201276,-7.024807,4.556974,1.278043],[3.110850,-8.440965,3.585203,8.123589,5.785185,9.652930,-2.664914,7.446258],[-2.464169,-6.735679,-7.626493,-8.832279,9.552177,4.943269,-9.365966,-1.707793],[-1.988503,-6.627309,4.197071,2.419128,-8.333531,-4.813433,-5.233876,-3.360816],[-7.620072,-2.754468,9.716447,-1.542036,5.529143,4.425735,-4.326044,-5.527605],[-4.331339,9.701351,-5.114392,-9.329786,2.192947,-5.286651,-0.209624,6.388973],[7.724848,-7.194340,-1.714749,2.514193,-1.773685,2.261220,-2.348624,3.786592],[-7.393806,2.184495,-4.335937,5.037844,-2.399275,8.643331,5.929316,1.042879],[-5.039528,1.563352,5.442322,3.986776,5.013587,-1.964340,-8.327393,-0.921929],[-5.826581,3.727141,6.834338,9.128976,-3.297016,-6.693142,3.906477,6.949176],[6.226778,-7.636512,7.281769,-8.619655,-5.745955,0.590375,3.108285,3.317148]],[[0.737879,-7.203695,-3.390929,-5.216523,-2.350777,-0.112504,-4.830249,1.103570],[-0.113278,-9.490431,2.218335,-8.222863,-9.356191,-1.715823,0.946912,2.098284],[1.661729,8.384926,8.255667,-9.878613,-8.488477,7.431342,-8.779254,7.993099],[-6.771710,5.146418,-7.058569,2.922128,0.689158,-9.999007,-1.405602,2.497681],[7.769882,1.728861,-5.935802,-6.214381,-4.590865,8.066360,7.448620,3.183123],[0.129462,9.208217,-0.032136,-7.413595,5.831036,-0.275044,-5.639911,6.802175],[-3.893559,0.746928,-5.363560,9.070587,6.735795,-1.315838,3.064775,4.029790],[-7.364253,2.432274,0.718085,-6.082001,-7.985857,-7.786520,-4.812192,2.766607],[-5.129142,1.253444,-8.178857,1.828893,3.894822,-7.169813,1.531945,9.706725],[8.832687,-2.734766,-6.113753,2.684255,6.478993,-3.190516,5.170131,-5.092915],[-7.405476,-1.985097,7.590021,-0.996215,1.048919,4.211786,-9.483845,-2.415477]],[[9.130795,9.463395,5.914962,9.631299,-8.543078,-6.432503,1.011725,-2.904451],[-0.651793,-4.227021,-9.455667,8.101906,-7.181970,4.385163,7.770661,-6.626324],[-1.669560,1.385281,-8.123877,6.410366,-4.912879,-0.320877,-6.361105,3.745273],[5.710094,-9.902139,-5.260904,-9.169680,3.945102,-2.308956,5.916463,8.478682],[-2.783093,-5.193828,1.727217,6.885769,4.446920,0.981846,-6.760548,2.830925],[4.947282,-9.440237,8.104477,-3.517080,-5.426236,6.764107,2.479705,5.620018],[1.755791,-3.875076,9.099854,-7.207004,9.830465,0.536166,-5.943709,5.304547],[-8.818935,-8.336929,-2.472868,-8.259400,3.584543,2.530277,7.523526,-2.506377],[-9.627178,7.898699,-1.860170,-7.707774,-7.965396,-1.725182,-2.888950,-1.130211],[6.599953,-7.130392,8.255438,-5.877196,7.777864,7.120068,-7.308069,0.774998],[-2.044616,6.127852,8.565532,-0.668689,8.806275,-3.275393,-8.460360,-9.070096]],[[4.378808,-7.697435,-0.801701,1.411662,-1.171651,-3.483413,-0.189057,3.066485],[-4.769040,-0.344027,-7.859325,0.439265,6.248628,-0.007976,-7.598797,9.390918],[7.588879,-8.105230,-8.408262,8.061859,-6.637682,7.167777,-5.150338,3.362404],[0.033251,-4.498964,-1.334236,4.716502,8.916531,-8.869644,9.729808,-6.691211],[1.716329,-8.772348,-4.832962,-2.465379,6.619294,-2.178729,-1.454805,-2.749634],[7.849997,8.751749,5.938275,2.102952,-2.925524,-1.058936,5.638827,0.723403],[-7.856377,-5.027302,6.060952,3.386124,-5.962021,-9.389545,-3.581310,2.417802],[4.113283,7.233280,1.387267,-5.107024,-8.979364,1.982390,6.967290,-7.688249],[-2.365532,-2.515979,3.960736,-9.803902,9.330132,-9.231042,-5.411402,9.684313],[9.791799,-6.916992,5.869069,-8.762506,1.746118,3.502595,-1.048946,-0.222638],[-7.155401,6.421875,8.906703,-5.631621,-1.479854,-5.979558,-6.609047,3.643824]],[[-7.811748,-8.143730,-4.625906,-1.504546,1.748770,-1.800733,1.371590,-1.235425],[2.597369,-3.646219,-7.681935,-4.117058,8.172513,9.862838,-2.751793,2.647571],[-5.222586,4.532706,2.529709,-5.823129,8.481784,-1.066334,-8.304852,2.097110],[-4.778379,-9.425508,-6.535229,-9.218962,8.689570,6.631437,-9.321084,-4.695370],[-9.713374,1.082415,7.745277,-1.893886,-2.420555,-5.580860,-9.506480,-2.747469],[4.543817,4.121594,2.894849,3.581977,4.217708,1.684371,-4.884349,-6.957359],[6.571073,-3.294296,4.160324,6.569155,1.840496,-9.292852,3.223815,2.518893],[8.318909,-8.903494,-6.605105,3.608119,-8.386625,1.349327,7.778879,-4.736136],[3.983666,6.762540,9.341662,-7.822457,-4.866188,-4.616243,4.031220,-4.070790],[-2.420722,-6.811312,8.424406,-5.177087,-7.425292,-5.488146,3.496558,-1.593548],[3.909881,-9.309232,-3.042040,0.820964,3.322453,2.683863,9.017853,-1.570498]],[[-2.654652,-5.720376,-7.462561,-1.656413,-9.612444,-5.632045,6.729098,-6.966878],[7.670538,8.497655,8.406306,-7.783494,5.674879,-6.625834,-6.961358,-4.169547],[8.040852,-0.163882,-7.796718,-4.581382,0.355504,-4.245513,7.992838,4.547168],[0.009783,-8.107306,6.393097,-3.780391,-0.940796,-0.058983,3.779066,-2.120324],[3.928800,-9.304938,3.175154,4.440973,-1.256800,2.302100,-8.167711,-6.239067],[3.150841,6.839154,4.733256,1.169434,-6.709927,-9.022511,0.029134,-9.919358],[7.599771,-3.440826,7.280299,4.145761,7.803689,9.739066,9.990104,-9.132868],[-6.377795,-2.421945,5.549905,-0.443992,5.847748,0.856609,9.896414,4.130269],[-9.736046,1.407720,3.805419,5.366489,7.598418,7.409098,-4.642261,3.772760],[8.784829,4.328837,-1.454134,-1.617135,-1.940367,-9.589777,3.837789,4.376166],[9.494714,9.661564,9.875738,1.499891,6.251453,-1.074210,-8.416290,-8.053931]],[[7.827833,-1.974665,6.026935,6.994804,-1.307590,4.896370,8.788944,-7.454402],[0.493114,-7.477602,-2.643205,1.482020,-8.453356,-9.774120,-1.472127,-2.167224],[-3.832320,6.168399,1.056385,5.838991,-6.032630,9.880501,6.797949,-7.480907],[5.020196,-5.733375,-9.923733,7.453977,7.586539,-5.322293,-4.806751,3.167471],[9.313934,7.678643,8.405432,9.712018,5.289655,6.011741,-2.078082,-8.368733],[-8.119169,2.661700,-9.517266,1.240943,-8.160385,8.493133,-5.082341,6.963481],[3.065716,-6.099114,-9.743024,-0.375373,-0.769539,-9.265600,8.433380,-8.581592],[2.899830,2.648907,-0.848345,1.665499,-9.667939,-7.358132,5.372516,-9.149330],[-8.966096,5.377867,-7.157427,-2.126867,-8.761972,7.373239,5.770482,2.980838],[-2.993434,5.449941,-8.955630,7.742055,3.164985,8.369781,-7.279173,-9.484904],[5.822469,4.255226,4.207243,-1.393956,-1.940351,-8.347538,-9.899262,2.691191]],[[-8.590449,2.241506,2.163904,9.574963,-5.330667,-6.079656,-2.554930,1.651462],[-8.117411,-1.588587,1.060701,1.300748,-9.133246,5.881249,-7.541134,8.230159],[4.141145,1.975167,-1.433937,-9.045053,6.980995,7.641857,4.168288,6.715067],[3.905835,1.224302,2.643110,-5.035831,-4.456096,-6.016816,-2.119352,3.741576],[-9.880413,8.444832,7.465499,-4.363419,-4.423355,9.812435,-5.367184,2.149513],[-9.069102,-2.870487,-0.588109,1.011932,9.100674,7.556515,-0.395891,7.515342],[2.170913,3.685978,-7.801707,7.703855,4.162317,-0.053912,-5.121887,3.160500],[5.281694,-9.393939,-7.851255,-0.749790,8.558792,-2.694078,3.732456,-8.785656],[-9.030201,7.608229,5.727491,9.207583,5.828275,4.900659,8.552761,-5.830538],[-6.746179,-2.236702,5.030978,-8.818097,-7.718472,-6.543325,3.631466,-3.931679],[-7.543620,-8.231134,3.213745,-2.574523,-9.502087,-2.800070,-6.676764,-7.051722]],[[7.533000,0.893107,4.707355,8.282198,-0.843070,0.321866,-5.531933,5.304234],[-8.754377,1.007572,5.799062,-6.363709,0.384796,-8.719347,-1.031324,-8.306196],[8.599847,-9.582406,-7.969547,2.466342,5.240860,-9.496269,-6.161247,-7.145050],[1.373859,-6.794968,6.195125,-5.889978,7.496111,-3.019769,4.282725,4.295340],[-6.476923,-0.237110,9.026267,-4.592505,-4.402693,1.266115,-7.405078,7.612969],[7.057353,8.461843,4.669106,5.035877,-7.166738,-2.068200,-1.621353,-8.707104],[8.451132,7.186755,-2.447532,3.369287,-8.619434,-4.344609,-1.948925,3.534384],[1.183871,-9.722649,-9.638390,-0.697877,8.722438,5.873690,-7.821810,-6.363524],[-2.104976,1.496383,4.613468,3.430567,6.547068,4.731375,-5.925208,2.619619],[0.342422,-4.234546,9.897396,-9.164334,9.208505,-9.425391,1.303621,7.212218],[2.733855,3.122138,1.937517,-0.598312,-4.833889,-1.628787,-9.877753,-7.291625]],[[9.448169,-7.156023,5.498457,4.846737,-8.132581,7.029868,-3.491680,0.063459],[0.153380,6.869924,3.691044,2.103573,6.730755,-8.480004,7.269615,8.110734],[3.471217,1.024101,-4.080361,8.881725,-1.264422,-3.024177,9.295378,-7.112351],[-6.044598,7.378715,-8.395235,0.342212,-7.451679,9.262542,1.662634,-8.726542],[-2.337856,6.979789,-0.150895,3.052073,2.811606,-5.738690,2.832596,8.084683],[-7.114168,-6.683618,4.027502,-2.415434,1.127561,6.903689,-5.525828,-2.843363],[8.779509,1.527294,-9.246441,6.277755,-1.893687,3.040658,-6.375725,-2.241207],[0.203383,2.441333,-5.321253,8.100314,-4.954698,-7.717656,-9.366627,5.947437],[1.078345,-7.773696,-3.442020,3.276176,9.783218,-5.062868,-2.680462,-0.014438],[6.332731,-9.968399,6.165554,-4.917169,1.454596,-7.659845,6.284920,9.327185],[-7.832470,-6.714865,0.733309,5.039238,-3.258456,1.795007,-6.006730,6.201899]]], dtype = "float32")#candidate|2925|(11, 11, 8)|const|float32
uop_2926 = relay.atan(const_2925.astype('float32')) # shape=(11, 11, 8)
output = uop_2926
output2 = uop_2926
func_2943 = relay.Function([], output)
mod['func_2943'] = func_2943
mod = relay.transform.InferType()(mod)
mutated_mod['func_2943'] = func_2943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mutated_mod.get_global_var('func_2943')
call_2944 = func_2943_call()
output = call_2944
func_2945 = relay.Function([], output)
mutated_mod['func_2945'] = func_2945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_3014 = func_2943_call()
call_3015 = func_2943_call()
output = relay.Tuple([call_3014,])
output2 = relay.Tuple([call_3015,])
func_3025 = relay.Function([], output)
mod['func_3025'] = func_3025
mod = relay.transform.InferType()(mod)
mutated_mod['func_3025'] = func_3025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mutated_mod.get_global_var('func_3025')
call_3026 = func_3025_call()
output = call_3026
func_3027 = relay.Function([], output)
mutated_mod['func_3027'] = func_3027
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_3062 = func_2943_call()
call_3063 = func_2943_call()
output = call_3062
output2 = call_3063
func_3064 = relay.Function([], output)
mod['func_3064'] = func_3064
mod = relay.transform.InferType()(mod)
mutated_mod['func_3064'] = func_3064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mutated_mod.get_global_var('func_3064')
call_3065 = func_3064_call()
output = call_3065
func_3066 = relay.Function([], output)
mutated_mod['func_3066'] = func_3066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3119 = relay.var("var_3119", dtype = "float64", shape = (3, 8, 3))#candidate|3119|(3, 8, 3)|var|float64
uop_3120 = relay.cos(var_3119.astype('float64')) # shape=(3, 8, 3)
func_397_call = mod.get_global_var('func_397')
func_404_call = mutated_mod.get_global_var('func_404')
var_3132 = relay.var("var_3132", dtype = "float64", shape = ())#candidate|3132|()|var|float64
var_3133 = relay.var("var_3133", dtype = "float64", shape = (154,))#candidate|3133|(154,)|var|float64
const_3134 = relay.const([[-9.279675,7.428253,-1.382948,9.458299,-1.751671,1.613547,-9.117030,-7.373040,-3.579332,0.647383,-3.107395,-3.922177,-1.074416,0.176027],[6.865867,-4.574624,-0.033422,-4.838934,5.491334,-9.735822,-7.869990,3.536575,-1.318932,4.432719,-9.711904,7.167021,-6.812443,-8.520606],[3.148078,4.938915,-2.117795,-6.797301,3.938096,-5.635391,-2.306686,-9.203592,-8.159787,-5.769089,-1.066810,0.115258,-7.500257,7.372446],[7.276813,8.179097,-1.212170,8.759558,-7.801669,9.661126,-3.756940,8.490392,-1.309832,0.304908,9.741376,0.923647,7.325608,-9.556345],[3.625705,-5.622526,4.710961,1.265940,-8.861522,2.466245,-1.665491,4.785208,-9.952358,-4.904453,-9.231712,6.834372,3.956331,0.961695],[7.669841,-9.390626,-7.338780,2.496229,7.423126,0.582995,-6.791835,-2.522311,2.451729,1.792011,-9.529120,-0.022372,-3.340561,0.394204],[-3.374404,-0.475098,-6.458479,-3.162168,-0.410147,2.301691,-2.256469,7.869112,8.210358,6.279304,5.946289,-4.557879,-3.318099,1.052914],[-5.466415,-7.161337,5.383391,-3.072071,-8.759332,-6.896401,5.925536,-7.919006,-0.690287,-1.766956,4.318040,-6.020692,-4.307841,9.245305],[3.114464,7.052755,6.310374,-5.250922,8.341682,-0.818542,8.336145,-0.226768,-7.828563,-6.246365,-7.146037,-9.002681,5.897533,8.685380],[7.881363,-7.272591,5.734126,-4.146974,-5.088281,2.256870,-4.617660,7.846994,6.430764,-4.435249,-7.770276,-4.302203,6.654936,-7.606202],[-0.787740,-7.004877,-3.089967,-8.952991,7.498896,-3.680292,-5.803243,6.733715,-0.326403,-2.882917,-6.604682,4.623834,-0.894337,2.593999],[1.433090,-5.199393,7.232112,9.038042,0.176042,1.607287,0.375329,-1.008069,-2.843216,-0.052650,-3.068301,-5.510968,9.233558,7.782698],[1.220164,0.574582,7.437446,-9.407457,-3.009010,-5.454386,-5.081328,-6.103707,-8.276901,1.799736,-7.378369,5.609405,-6.007064,7.203408],[1.945056,2.603796,-6.446433,5.693414,-5.685097,-3.851517,-7.983217,2.443708,7.898003,-0.594897,-4.908139,-6.564723,2.205174,-9.734393],[8.599822,6.540449,-1.264352,1.987733,9.460326,-4.408251,4.024924,-8.784008,-8.089042,-6.189688,-2.275256,1.274584,-0.814523,1.594154],[5.047931,9.362109,-1.135342,3.152952,-6.037407,3.515459,-1.496155,3.315949,-9.114919,6.641424,5.278631,-2.197083,-8.363724,3.833608]], dtype = "float64")#candidate|3134|(16, 14)|const|float64
const_3135 = relay.const([2,10,-4,-9,-9,-7,-6,-9,-4,6,2,4,-5,-5,10,9,-2,2,-5,-8,-5,-3,1,-3,-2,3,-5,8,-7,9,10,9,-9,9,-3,6,1,10,-1,7,2,-7,-4,-4,-9,8,3,1,-2,3,5,-5,1,8,-8,5,-4,4,-7,-1,-3,4,-10,-7,-3,-8,-2,-7,-6,-4,2,4,-2,-6,-7,3,-9,8,-2,-10,7,-5,10,-1,7,-3,-5,-4,5,3,-10,4,5,-9,-8,2,-6,6,9,6,-3,6,6,-2,-2,3,-1,-1,2,3,-8,7,4,-4,9,10,7,-9,-5,-3,5,-1,6,5,4,8,-3,-8,8,-1,-9,10,-6,-10,9,-10,-1,1,6,5,-3,10,2,4,-9,9,-5,-4,8,-2,7,-1,6,8,-9,-10,10,10,-9,1,1,-3,-1,-7,-1,7,-2,8,10,2,1,-2,3,10,-8,1,3,6,-3,2,-2,3,7,4,7,5,-9,8,8,-5,9,6,9,5,-4,5,-5,-2,2,-10,-3,9,-1,-3,5,9,-3,7,8,-4,-8,-8,9,-5,-7,10,-9,1,5,3,3,3,7,-10,1,-7,4,4,-7,-4,4,-4,2,5,9,-7,-7,10,2,9,3,2,1,-1,-5,-3,-9,-3,4,8,3,-8,6,6,-6,-1,1,6,-9,2,-2,-2,4,3,3,-3,-7,-9,-9,-10,8,-5,5,10,-10,10,9,-4,7,-1,9,9,5,10,2,8,-1,8,-4,-2,3,6,-5,-5,8,-5,1,4,1,-7,-3,-3,-8,4,1,4,-9,-10,-1,-7,2,-7,-5,9,6,-6,-1,-5,10,-8,-7,-7,-3,3,1,-4,-1,7,3,-1,-10,-7,-4,1,-6,-6,-3,1,1,1,-3,6,7,1,7,-8,7,-9,2,6,1,10,5,2,-7,-8,10,-6,5,-9,-7,1,-6,6,2,-5,2,-9,-9,10,3,-6,-10,-2,-10,-9,-9,1,-5,-1,-9,-2,-2,-7,-9,6,-5,-7,-5,-1,-9,1,5,1,-1,6,1,-10,-8,-5,-3,1,5,4,8,-6,8,-6,9,2,2,-1,-8,9,9,-7,6,10,-7,-3,10,3,-7,2,6,10,-3,-2,-2,-1,6,-3,5,6,-10,8,-10,-9,-9,5,-6,-5,5,-2,-10,-10,-10,-9,-8,10,5,9,10,-4,-10,6,5,-5,-9,-9,-1,-5,2,7,-8,10,-6,1,-9,-4,-4,-5,2,-9,-6,-1,-7,-7,10,-1,-10,2,-1,1,-7,-1,7,-2,-3,-1,-9,-7,9,-5,7,-7,-8,4,-3,-3,9,-3,-7,5,-6,-10,-1,1,-10,-8,6,-5,-6,6,-1,-10,-3,9,8,2,2,-8,1,-4,-8,8,-10,8,2,-7,-5,5,10,7,-8,3,-1,5,-10,2,5,-4,5,-3,8,-9,-7,-10,-10,8,-6,-10,-9,10,7,-9,-4,-7,7,-7,10,-7,-2,-7,-5,-2,3,9,-8,3,-3,-8,-9,7,5,-10,-9,3,5,-6,4,-3,-10,10,1,3,-10,-10,-6,-3,-10,7,10,-3,-1,-7,-6,1,-3,4,-6,8,8,3,7,-4,-8,6,-2,-5,9,7,2,-1,-8,-9,-2,10,-6,-3,-8,-8,9,-4,-5,3,1,-9,-7,-8,-7,-3,5,-10,-6,-4,1,1,-9,10,-6,-8,-4,-1,-9,-8,-5,5,4,-3,-2,5,2,-5,2,3,-10,-6,7,-5,-6,3,6,3,7,10,-4,3,2,-5,3,4,-10,-8,-10,5,8,7,-8,-5,8,-4,-2,-8,-3,9,-4,9,-5,-3,2,1,8,3,10,-2,-3,3,-1,10,-6,2,-1,-4,-10,3,6,1,2,9,1,-2,-6,-2,8,3,-10,-5,-7,-9,-7,8,-6,5,-2,4,6,2,1,-10,-3,-2,-9,-3,-6,-5,7,-6,4,-5,-8,2,2,-7,-5,3,-2,-2,-2,9,-9,10,-10,1,8,8,2,1,3,1,4,7,-9,-9,6,-8,4,3,6,6,9,-1,6,-8,-7,9,3,9,9,-2,8,9,9,4,3,9,-5,-4,-2,2,-1,5,8,-5,-4,1,-6,3,-10,1,8,7,2,-4,8,-6,-6,-5,6,3,-7,-1,-5,-8,-5,10,9,-7,-3,-5,-9,-9,3,3,-2,-9,-3,1,9,2,-6,-7,2,-6,-7,3,6,-2,4,10,2,-6,-2,-2,6,-4,8,9,-7,4,-8,1,9,-2,-1,-10,4,9,-4,-8,6,-3,3,-6,-9,-6,9,10,1,2,4,6,-9,5,-5,-4,-5,9,8,-10,-10,-3,-4,-7,-5,-6,3,9,6,-5,-7,3,-5,1,10,2,6,8,-8,-4,6,-4,-3,-10,8,-1,4,8,8,5,-1,-7,2,-8,2,3,-3,8,-3,6,-6,8,-10,-9,6,-6,1,-5,-3,-3,-4,-3,-7,-4,9,-2,6,5,6,6,-10,-10,-8,-5,-5,-5,7,5,-1,4,8,5,6,10,5,-6,10,7,-9,8,1,1,3,1,5,-6,-9,-7,-2,-7,-4,-4,-8,-2,-3,9,6,-1,-5,5,-6,-3,3,-2,-8,1,-3,-4,-6,-8,-9,-1,6,-5,4,3,2,-9,-7,-9,-3,4,-5,-6,7,8,-10,2,-2,-1,9,-8,-1,8,-7,2,7,-5,6,-3,-7,10,9,5,9,8,9,10,3,7,-3,2,-7,-2,2,8,6,9,10,-9,-2,-8,2,-1,4,-7,-9,8,-7,8,8,9,6,9,1,-6,6,-4,-1,-5,6,-3,10,2,-4,5,8,5,-1,1,-6,-5,-2,1,5,-10,8,8,7,-5,10,-4,-5,4,7,8,-2,-4,-5,8,10,10,1,6,-8,10,3,6,-5,4,6,5,-8,-4,3,2,2,-1,-2,3,-10,-9,9,10,8,7,-9,-3,1,-9,-1,-10,-7,-8,-10,10,-5,10,4,1,-6,-3,-1,2,-4,-10,4,-10,3,-9,-8,-10,5,1,1,-1,-10,-4,3,-5,-6,3,-5,8,-8,8,5,-1,1,2,-1,1,-7,2,-8,8,2,-4,4,-4,1,10,-1,8,2,3,3,7,-8,2,10,2,1,8,9,8,5,8,1,-1,8,-8,-10,2,8,4,4,-7,-1,10,10,-2,8,-4,-7,-1,8,7,4,6,3,-7,7,4,2,9,-2,8,2,6,-4,-6,6,-10,5,4,5,9,-7,1,-4,3], dtype = "uint32")#candidate|3135|(1232,)|const|uint32
const_3136 = relay.const([5,-3,7,-10,10,10,-6,-6,-5,4,-3,4,2,4,6,-7,5,4,7,-6,-9,7,-1,8,3,9,-2,-2,3,-4,-5,1,-10,1,10,6,-2,-7,-5,-9,6,8,3,6,8,-8,-10,-3,6,10,1,-7,9,8,-8,6,-6,-2,4,6,8,7,3,-8,5,-6,4,-1,-7,10,-7,9,-3,-2,-1,-1,2,-4,-7,5,2,10,5,2,-2,7,-1,3,-7,10,-3,6,-8,-10,5,-9,-7,5,-2,-5,-1,4,-9,5,3,-6,6,-4,2,-9,9,6,-7,-9,-1,-3,-7,4,3,-3], dtype = "uint64")#candidate|3136|(120,)|const|uint64
call_3131 = relay.TupleGetItem(func_397_call(relay.reshape(var_3132.astype('float64'), []), relay.reshape(var_3133.astype('float64'), [1, 14, 11]), relay.reshape(const_3134.astype('float64'), [1, 224]), relay.reshape(const_3135.astype('uint32'), [1232,]), relay.reshape(const_3136.astype('uint64'), [120,]), relay.reshape(const_3136.astype('uint64'), [8, 5, 3]), ), 3)
call_3137 = relay.TupleGetItem(func_404_call(relay.reshape(var_3132.astype('float64'), []), relay.reshape(var_3133.astype('float64'), [1, 14, 11]), relay.reshape(const_3134.astype('float64'), [1, 224]), relay.reshape(const_3135.astype('uint32'), [1232,]), relay.reshape(const_3136.astype('uint64'), [120,]), relay.reshape(const_3136.astype('uint64'), [8, 5, 3]), ), 3)
func_2260_call = mod.get_global_var('func_2260')
func_2264_call = mutated_mod.get_global_var('func_2264')
var_3146 = relay.var("var_3146", dtype = "float32", shape = (21,))#candidate|3146|(21,)|var|float32
const_3147 = relay.const([-1,7,9,1,6,9,10,-8,-1,3,5,5,10,9,6,10,-8,5,4,-5,7,6,4,-6,10,-5,7,-10,-3,-5,-9,-8,-2,8,10,10,-9,-7,-4,-10,-2,1,4,-8,-2,-7,8,10,10,-7,3,-10,-6,5,-9,6,9,-1,-1,-9,-2,4,4,9,1,-6,5,-7,2,3,-7,3,8,-7,4,2,6,5,9,8,2,-4,-10,10,-3,3,1,5,1,10,10,3,-5,8,4,4,9,-3,-1,5,3,3,6,-5,2,6,5,-9,-8,4,4,8,-8,-4,-1,2,-9,-9,-2,3,2,-7,-7,-9,3,8,1,-3,-4,-7,-8,-10,3,1,6,1,-3,4,5,6,-7,7,10,-9,7,-1,5,1,1,-5,-5,-2,7,8,-1,9,-1,-8,-8,-7,-4,-1,2,-9,5,-9,-2,-9,-10,2,3,7,-10,5,3,3,4,6,-6,-8,-1,-1,9,4,7,9,7,-4,-3,5,4,-3,3,-2,-6,-10,-9,-10,1,8,-9,-9,-6,-5,5,7,9,-8,1,1,-4,2,4,-2,3,-4,-10,9,10,-5,4,-6,9,-5,-8,8,9,-5,-10,-7,-8,7,8,2,-10,4,-6,-8,6,7,-2,-6,-5,-4,-10,9,-4,4,2,1,-4,7,5,6,1,-7,-10,-3,-6,1,-8,1,-5,-7,4,1,2,7,5,1,1,-8,1,-6,-6,2,-7,7,10,1,1,2,-1,-3,4,-2,-3,6,2,2,10,4,-7,-9,7,2,5,-1,3,-5,-9,-2,9,-8,-9,-9,-4,-6,5,9,9,-10,-5,1,9,7,-4,2,-6,-2,-9,-5,5,-4,-9,4,4,4,-7,1,10,-3,8,8,6,-10,3,7,-9,2,-4,9,10,-1,-8,-4,2,-5,-3,-4,-2,-3,4,-5,-3,-2,-3,8,4,-2,-2,1,4,-4,-8,7,5,-7,3,1,-10,4,-5,7,-2,2,-5,-7,10,7,2,-9,5,-5,9,4,-10,-3,1,-6,10,8,-2,6,8,9,-9,-4,-6,5,-6,5,9,5,-9,-4,9,-6,-9,-3,6,-5,-2,-1,2,6,-7,6,-10,-8,1,9,6,-1,8,1,5,10,9,-8,9,8,4,2,4,4,-3,-5,8,7,-7,-1,6,-2,5,5,3,-8,5,2,1,5,8,-7,4,-4,2,-5,-7,5,-6,-5,-2,-7,-4,-8,-6,-3,3,-3,-3,9,-4,-6,-9,4,9,-6,4,-8,4,-5,9,7,9,-8,-8,-8,9,-5,4,6,1,-4,5,3,-10,-10,-8,10,6,2,2,8,5,-2,5,2,-9,-10,10,6,4,8,10,1,-3,9,2,-7,-1,6,6,-1,-6,-3,-4,8,-2,10,-4,9,-4,5,8,-5,-2,6,-10,-4,7,5,-4,-9,-1,2,2,5,2,1,3,-10,8,-2,2,-5,3,10,4,6,10,1,9,-7,-5,2,6,-10,7,-3,7,-10,9,-8,1,8,-3,-3,-2,-3,1,-4,7,-1,5,-3,-1,3,-5,3,-6,-9,-10,1,-3,1,-2,-10,9,1,-3,-6,-9,6,-1], dtype = "int64")#candidate|3147|(605,)|const|int64
call_3145 = relay.TupleGetItem(func_2260_call(relay.reshape(var_3146.astype('float32'), [1, 7, 3]), relay.reshape(const_3147.astype('int64'), [605,]), ), 0)
call_3148 = relay.TupleGetItem(func_2264_call(relay.reshape(var_3146.astype('float32'), [1, 7, 3]), relay.reshape(const_3147.astype('int64'), [605,]), ), 0)
output = relay.Tuple([uop_3120,call_3131,var_3132,var_3133,const_3134,const_3135,const_3136,call_3145,var_3146,const_3147,])
output2 = relay.Tuple([uop_3120,call_3137,var_3132,var_3133,const_3134,const_3135,const_3136,call_3148,var_3146,const_3147,])
func_3151 = relay.Function([var_3119,var_3132,var_3133,var_3146,], output)
mod['func_3151'] = func_3151
mod = relay.transform.InferType()(mod)
mutated_mod['func_3151'] = func_3151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3151_call = mutated_mod.get_global_var('func_3151')
var_3153 = relay.var("var_3153", dtype = "float64", shape = (3, 8, 3))#candidate|3153|(3, 8, 3)|var|float64
var_3154 = relay.var("var_3154", dtype = "float64", shape = ())#candidate|3154|()|var|float64
var_3155 = relay.var("var_3155", dtype = "float64", shape = (154,))#candidate|3155|(154,)|var|float64
var_3156 = relay.var("var_3156", dtype = "float32", shape = (21,))#candidate|3156|(21,)|var|float32
call_3152 = func_3151_call(var_3153,var_3154,var_3155,var_3156,)
output = call_3152
func_3157 = relay.Function([var_3153,var_3154,var_3155,var_3156,], output)
mutated_mod['func_3157'] = func_3157
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_3163 = func_3064_call()
call_3164 = func_3064_call()
func_2688_call = mod.get_global_var('func_2688')
func_2691_call = mutated_mod.get_global_var('func_2691')
const_3172 = relay.const([[-7.022806,-2.158553,7.231893,9.312683,-0.852991,7.458015,-2.048323,-7.783162,9.944491,-2.259323,-2.739994,-8.302721,-5.905077,-9.769564,-8.949970,-7.390227,-0.732200,2.900349,8.945275,6.696306,-0.973908,-0.836936,6.361698,-0.348360,9.148856,1.624803,9.224570,-6.017694,0.113707,-5.642779],[0.003212,2.802620,-5.334914,1.244563,3.261779,0.913524,-0.759336,-1.205861,-1.096897,-1.707989,7.847691,0.516082,6.804668,5.906877,-0.272983,5.702540,-7.673793,3.516749,8.970078,-9.642036,9.040142,1.586971,5.389345,-5.871836,-0.555939,-1.548761,-0.691759,-9.400807,8.905142,4.453815],[-7.452003,0.735700,2.113955,7.936605,-3.235061,9.338704,5.384616,3.960422,-9.663902,-3.547779,-8.443218,-4.627704,-6.497143,0.914323,-1.991999,4.859410,5.348431,-0.282238,-0.285411,8.385084,8.602391,-5.850906,0.114110,-0.596912,4.304989,6.942584,2.161828,7.729931,-1.635422,7.793783],[5.792450,8.521391,2.909271,1.268653,7.706654,-3.053636,0.399751,9.436022,-2.857756,-8.183029,-6.253749,-8.061041,9.826284,8.664440,-3.975032,4.690804,-1.455833,-7.471036,-6.332818,8.661413,-1.376768,-1.586233,-2.398903,8.132826,0.927090,7.269454,4.590303,3.593040,8.041499,-6.568060],[8.820915,2.025779,3.414630,-7.945520,2.003547,8.657883,6.144852,7.963033,-4.930114,3.473976,-2.971662,6.738703,-9.475301,-9.882914,-8.621585,8.648142,-3.689110,8.968279,-4.500757,0.993012,0.632893,7.598549,6.327017,-0.186867,2.857740,2.087564,-2.038323,0.081719,-7.059268,-5.672442]], dtype = "float32")#candidate|3172|(5, 30)|const|float32
const_3173 = relay.const([[4.265513],[5.357577],[-4.599158],[1.745639]], dtype = "float64")#candidate|3173|(4, 1)|const|float64
call_3171 = relay.TupleGetItem(func_2688_call(relay.reshape(const_3172.astype('float32'), [5, 5, 6]), relay.reshape(const_3173.astype('float64'), [1, 4]), ), 2)
call_3174 = relay.TupleGetItem(func_2691_call(relay.reshape(const_3172.astype('float32'), [5, 5, 6]), relay.reshape(const_3173.astype('float64'), [1, 4]), ), 2)
func_2363_call = mod.get_global_var('func_2363')
func_2367_call = mutated_mod.get_global_var('func_2367')
var_3188 = relay.var("var_3188", dtype = "float32", shape = (1760,))#candidate|3188|(1760,)|var|float32
var_3189 = relay.var("var_3189", dtype = "int16", shape = (1456,))#candidate|3189|(1456,)|var|int16
call_3187 = relay.TupleGetItem(func_2363_call(relay.reshape(var_3188.astype('float32'), [10, 16, 11]), relay.reshape(var_3189.astype('int16'), [1456,]), ), 1)
call_3190 = relay.TupleGetItem(func_2367_call(relay.reshape(var_3188.astype('float32'), [10, 16, 11]), relay.reshape(var_3189.astype('int16'), [1456,]), ), 1)
bop_3205 = relay.floor_divide(call_3187.astype('float32'), relay.reshape(var_3189.astype('float32'), relay.shape_of(call_3187))) # shape=(1456,)
bop_3208 = relay.floor_divide(call_3190.astype('float32'), relay.reshape(var_3189.astype('float32'), relay.shape_of(call_3190))) # shape=(1456,)
output = relay.Tuple([call_3163,call_3171,const_3172,const_3173,var_3188,bop_3205,])
output2 = relay.Tuple([call_3164,call_3174,const_3172,const_3173,var_3188,bop_3208,])
func_3213 = relay.Function([var_3188,var_3189,], output)
mod['func_3213'] = func_3213
mod = relay.transform.InferType()(mod)
var_3214 = relay.var("var_3214", dtype = "float32", shape = (1760,))#candidate|3214|(1760,)|var|float32
var_3215 = relay.var("var_3215", dtype = "int16", shape = (1456,))#candidate|3215|(1456,)|var|int16
output = func_3213(var_3214,var_3215,)
func_3216 = relay.Function([var_3214,var_3215,], output)
mutated_mod['func_3216'] = func_3216
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_3218 = relay.TupleGetItem(func_3025_call(), 0)
call_3219 = relay.TupleGetItem(func_3027_call(), 0)
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
const_3235 = relay.const([[4.956419,-8.574068],[-2.511405,8.954639]], dtype = "float64")#candidate|3235|(2, 2)|const|float64
call_3234 = func_1152_call(relay.reshape(const_3235.astype('float64'), [4, 1, 1]))
call_3236 = func_1152_call(relay.reshape(const_3235.astype('float64'), [4, 1, 1]))
output = relay.Tuple([call_3218,call_3234,const_3235,])
output2 = relay.Tuple([call_3219,call_3236,const_3235,])
func_3244 = relay.Function([], output)
mod['func_3244'] = func_3244
mod = relay.transform.InferType()(mod)
mutated_mod['func_3244'] = func_3244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mutated_mod.get_global_var('func_3244')
call_3245 = func_3244_call()
output = call_3245
func_3246 = relay.Function([], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_3304 = relay.TupleGetItem(func_3244_call(), 0)
call_3305 = relay.TupleGetItem(func_3246_call(), 0)
func_397_call = mod.get_global_var('func_397')
func_404_call = mutated_mod.get_global_var('func_404')
const_3317 = relay.const(-7.487543, dtype = "float64")#candidate|3317|()|const|float64
var_3318 = relay.var("var_3318", dtype = "float64", shape = (154,))#candidate|3318|(154,)|var|float64
var_3319 = relay.var("var_3319", dtype = "float64", shape = (224,))#candidate|3319|(224,)|var|float64
var_3320 = relay.var("var_3320", dtype = "uint32", shape = (56, 22))#candidate|3320|(56, 22)|var|uint32
const_3321 = relay.const([-4,-2,8,1,9,-1,6,4,-6,3,-10,6,8,8,3,3,-8,6,-4,-3,5,-7,10,9,6,-7,8,2,-5,6,-10,7,3,-5,10,-10,-2,6,-10,-7,-8,5,-10,-6,9,-4,10,-6,-7,-7,-9,-2,4,10,-4,2,-3,-1,-4,-9,6,2,7,6,9,8,2,8,9,-10,8,8,9,-6,4,-5,-9,6,-7,7,-10,5,-9,8,4,3,-1,1,10,-4,3,5,-8,-7,5,-2,-10,-7,-9,-7,2,-5,2,-3,-5,7,6,-9,2,1,9,2,-8,10,-3,-2,-8,-8,-3,3], dtype = "uint64")#candidate|3321|(120,)|const|uint64
call_3316 = relay.TupleGetItem(func_397_call(relay.reshape(const_3317.astype('float64'), []), relay.reshape(var_3318.astype('float64'), [1, 14, 11]), relay.reshape(var_3319.astype('float64'), [1, 224]), relay.reshape(var_3320.astype('uint32'), [1232,]), relay.reshape(const_3321.astype('uint64'), [120,]), relay.reshape(const_3321.astype('uint64'), [8, 5, 3]), ), 4)
call_3322 = relay.TupleGetItem(func_404_call(relay.reshape(const_3317.astype('float64'), []), relay.reshape(var_3318.astype('float64'), [1, 14, 11]), relay.reshape(var_3319.astype('float64'), [1, 224]), relay.reshape(var_3320.astype('uint32'), [1232,]), relay.reshape(const_3321.astype('uint64'), [120,]), relay.reshape(const_3321.astype('uint64'), [8, 5, 3]), ), 4)
const_3332 = relay.const([[[-4.415638,2.620138,-7.101987,-6.718640,-0.666825,-4.641131,-3.762537,-4.835395],[3.365662,0.616315,7.013420,-8.021308,9.198039,-1.698921,-1.093747,4.029314],[6.520493,-5.800481,-4.893906,-2.004916,6.536333,-0.451618,7.724696,-0.860362],[0.542092,-0.950934,7.914016,4.724153,2.591835,-8.645422,4.858015,-0.447557],[-9.883949,-4.863242,6.380127,-4.946087,1.065351,1.528209,2.655432,-1.657991],[9.393970,6.271099,4.547832,4.109621,1.014273,-4.896914,3.301520,9.063406],[-8.856506,-4.298624,-4.281455,-9.882414,7.141109,-6.287897,8.671870,9.679736],[0.979117,0.377507,-3.480750,2.210438,-0.678792,-9.880655,-1.262354,-5.738441],[-8.592537,8.104201,7.834149,-6.417021,4.878895,7.622310,9.482466,4.385037],[9.974675,-7.645101,0.461101,8.253382,3.620056,-1.685649,6.543845,-8.071964],[9.414577,6.164578,0.222122,-2.201073,-2.298394,-0.912207,-0.880269,6.773201]],[[-8.956099,7.253450,6.258536,-5.810731,0.494496,1.337702,5.466848,-4.365694],[0.809436,5.077393,4.453916,0.492808,9.858990,-5.374807,2.486997,9.368125],[7.368128,0.121473,-4.308926,5.642663,-8.085011,-6.215363,4.976378,8.627479],[-9.633464,0.622023,-3.213195,-4.344215,-3.239741,4.379825,-4.651786,-5.667607],[-4.157956,-4.199509,5.016964,-1.261867,-4.872153,6.629624,6.045716,-1.690464],[3.895828,1.396510,-4.166557,8.369418,-5.464374,-8.201492,0.969616,-7.280291],[9.748271,-4.134362,5.945794,-2.500044,-2.878174,2.100207,-5.595408,9.188865],[5.907658,9.396800,-8.131839,8.270233,-7.340306,3.337561,-9.733921,7.632870],[9.191914,-8.207432,-7.926590,-9.790512,-2.661472,-0.368624,-1.329466,-2.158857],[-3.120664,6.415175,-2.377587,-5.975155,2.569270,-1.075860,5.271772,5.733731],[-0.753853,9.121089,-4.296708,8.806233,2.427528,-4.289919,5.408314,-5.434793]],[[-4.251752,9.100447,-2.168830,6.604865,2.537743,3.330854,7.144316,0.152619],[-6.619199,-9.739376,4.150187,7.096791,1.369991,-9.065435,-0.400711,7.794676],[-8.528540,8.316822,-8.265092,-1.653540,-7.528928,-7.173755,-0.222761,3.934360],[4.666074,-0.195117,1.932123,9.923336,6.044918,-4.932290,-2.949582,-9.673717],[-1.685002,8.377419,6.034336,-1.457952,2.408730,4.017010,2.763915,-5.398378],[0.587023,3.159733,-5.507933,6.577947,-6.159940,6.970586,5.479041,8.989137],[1.644321,-2.243337,9.701941,2.548796,-6.699204,-3.070803,1.997115,-7.681335],[8.229015,-5.085067,-7.536418,7.216799,7.347519,-7.772310,1.058309,-0.817169],[-5.396140,7.529394,8.397596,6.632992,4.396014,0.077151,-6.877708,0.142186],[1.594172,-7.018339,-6.432522,-0.666245,-0.774292,-4.934267,5.649778,3.690956],[-9.623171,4.447199,2.587706,3.451281,-9.167193,4.212072,-0.796254,4.517609]],[[-2.191131,4.633574,0.251059,-8.550911,-9.571555,9.119658,9.612608,-1.639850],[7.558969,-3.460242,-3.345339,-3.565307,-1.066247,4.785572,-0.544709,6.180278],[-1.542034,6.486687,-5.570279,-5.804873,8.710716,-0.497659,-1.821742,-4.889054],[-7.761241,-9.894358,-9.856576,-3.837779,-6.085620,4.180387,-0.064032,-9.481812],[0.383540,-4.718090,5.298305,1.671447,3.999638,-4.227626,-8.518209,4.868222],[1.852333,0.827905,-3.309716,-3.728106,1.263676,-8.657970,-7.296507,3.871750],[-0.732387,-7.917552,-4.252399,-0.895665,6.502113,6.843443,3.074090,6.554479],[-0.404453,-6.703599,-6.905485,7.143927,-0.921008,3.461874,-8.676234,6.929345],[-4.514065,0.466436,3.165262,-2.307881,-0.267202,-5.079622,5.074078,-4.518045],[-1.392551,-4.190709,7.924494,-8.462584,7.313025,7.154605,-0.926394,2.855636],[-1.882953,2.947245,-9.291988,-8.946548,5.164403,6.329457,-8.483252,-8.650615]],[[-1.919921,6.167792,9.371707,-6.421520,1.476053,-6.224455,-2.066343,4.173910],[-6.292079,-4.739284,-6.132666,8.346507,6.239802,-9.017130,-5.959954,-3.537691],[-9.653473,0.916899,0.491002,-2.771017,7.614927,9.579714,-6.402822,-6.296381],[0.438189,-2.768108,0.302135,-5.853190,-2.709812,8.014224,7.610069,9.785322],[2.893783,5.736385,-0.955798,-8.278031,2.717223,6.328443,-1.562428,-4.057320],[-9.956100,2.493272,2.209771,-4.566255,1.935781,-1.861715,5.616185,-6.798998],[-2.766693,-5.342108,5.472032,-9.491056,-4.076462,0.799582,0.534092,-5.033032],[-2.827918,-7.297276,7.104218,8.846493,-7.121907,-7.423970,7.297995,-4.553496],[-5.847947,1.516661,0.480465,-3.770505,2.212824,-6.976653,-6.613481,9.470133],[6.295517,-5.472439,-0.110681,2.665694,3.065667,6.854928,-8.417917,3.194759],[-4.957429,-6.281048,-5.702262,7.547504,-1.324437,3.634313,-0.922924,1.869585]],[[-6.314762,4.029042,4.974156,3.833437,-6.788007,-1.980170,-2.256219,0.770954],[-0.060286,5.323188,1.811593,-0.083762,-6.306628,-9.284457,-7.525677,-1.619881],[9.323659,-2.973401,-1.202849,1.753161,-1.917354,6.045787,5.938418,3.522201],[6.234486,3.161853,5.873950,-6.016768,4.331159,-7.437988,4.061336,-0.963374],[-1.824417,6.086362,-8.848269,8.354757,-3.616476,9.855747,-7.120683,4.455650],[8.823088,-9.892113,2.204785,1.090409,4.369416,-1.174589,-8.981566,9.091654],[9.435217,-2.308860,6.401479,-3.803406,-8.852165,-6.958324,-5.557959,-9.571497],[-9.656214,-0.541010,-1.562637,-4.352216,-8.122847,-2.867569,7.916217,7.970502],[-8.398672,-6.851877,-7.513866,-6.732388,-5.907375,8.656138,-6.734825,4.413009],[-9.443312,-3.573397,9.992888,-0.074665,-4.952355,-9.566164,-4.990792,-0.167704],[6.169307,-4.672885,-4.145304,7.336214,8.066264,1.646681,-4.880052,-9.298858]],[[2.829714,5.734220,5.720306,-5.566923,-6.978183,0.871464,-9.480244,-0.325139],[-9.754511,3.110564,3.618303,-1.606011,6.653514,-3.467982,-9.323888,-1.932573],[-9.714302,-0.399815,6.347180,2.671658,4.887222,-2.994345,-7.472712,-2.022709],[-3.248063,6.454888,-4.409898,-5.525010,-5.933511,7.008647,-8.276865,-8.002724],[-0.280474,-3.175435,2.169217,9.073475,8.014498,-7.208431,-6.888440,-6.071067],[7.914520,-0.218254,8.793364,0.957062,-8.198910,-2.980446,6.054496,8.659799],[9.208935,9.762073,3.832870,-5.234461,1.961553,-2.604057,2.617395,-0.559685],[8.445910,-9.822826,5.816502,-2.703526,-3.749927,-6.564088,0.814965,8.400960],[-8.374555,9.386870,-3.539829,-8.955322,-3.916602,3.629721,8.761683,-9.291678],[7.622393,-1.169015,1.209943,-0.382876,8.732588,9.719900,-6.164907,-8.868857],[5.361808,-5.513472,1.190080,8.093643,3.826890,7.101186,-8.730394,3.056608]],[[-4.925647,2.379836,-2.870377,2.476454,-0.566921,-8.689099,-1.365135,3.794484],[-4.041372,5.502518,-1.154244,-2.860070,5.917698,6.984454,2.536339,4.619998],[-7.146992,8.934451,-2.891476,-3.232868,9.010153,0.448155,7.531159,-5.548192],[-0.855370,8.313961,-0.785343,8.480579,6.854159,-2.357110,2.966555,-7.542165],[-1.907988,1.211501,9.128390,8.518824,-7.874681,-2.775295,-4.635154,-8.931784],[-9.369377,3.865504,3.576353,-8.712411,1.504099,2.630403,1.911952,-6.824449],[-0.325921,-3.179362,-8.951852,-5.019398,7.355967,-8.434339,3.533328,-4.807228],[7.378523,5.207495,-9.497338,1.545348,-6.620378,0.029420,3.926121,9.552833],[8.115224,4.322296,7.270153,-0.647740,-3.695437,-5.944756,6.567275,8.739760],[3.188627,4.539159,-3.137119,4.580440,-4.296399,-6.191674,4.381930,9.893956],[-6.327683,-8.882781,-8.631064,-3.852650,5.753722,3.943073,3.967340,2.337778]],[[6.777398,9.064807,-3.898520,-1.552144,2.672977,-3.526943,-6.656125,4.657671],[-8.232783,-3.899586,-4.824060,8.363408,-6.562744,2.068947,3.665439,-0.639557],[3.968042,-2.704582,-3.281284,-7.546756,-6.354382,-0.079477,-7.569844,4.107894],[1.624248,-6.991692,-2.387145,-0.855114,-2.930477,-4.494375,-9.002322,-9.451204],[-1.907797,6.945952,9.130335,-3.448382,-8.099825,-1.137939,-5.838001,4.913924],[1.374298,-4.209649,4.908788,-7.977713,-5.452969,0.064273,4.615162,-1.898556],[3.838980,4.228175,-5.663863,-2.503637,-1.381584,6.028693,-1.777908,1.907085],[-7.613473,3.387487,-5.977733,3.787442,-0.222832,6.436605,-4.033617,-8.480610],[-2.015423,-5.629117,7.909002,6.269688,3.811821,5.178169,-4.384603,-4.602896],[-1.555266,-2.194503,6.510316,0.507913,9.636639,-1.194716,-1.717270,9.969183],[-9.039358,9.964391,-0.115432,4.535875,-0.894178,4.205957,9.721310,4.634533]],[[2.459976,-5.632245,-6.974056,-8.824751,5.922183,5.550289,7.349772,-8.744083],[2.721598,-3.181115,-0.014318,9.031665,-1.355153,1.971320,-8.031198,7.779522],[7.838380,3.910874,6.754090,0.675821,-9.683494,-9.606007,9.750940,7.090424],[4.923670,-1.013857,0.207300,-7.373467,-7.502647,-6.866862,-0.251477,-0.550831],[3.288646,6.308498,5.670972,6.287382,-8.764058,-6.266986,-8.640082,-4.185058],[3.842346,-3.744610,-2.413564,-2.250573,-8.895085,-7.906565,-4.694119,-2.949547],[-4.500819,-7.202947,-0.167930,3.255110,5.540754,-2.703525,3.250398,9.539262],[3.867219,4.221413,-9.300893,-1.406729,-6.045300,-4.255724,1.517656,1.365059],[-0.594888,-6.729465,7.104287,6.767446,9.939361,6.781152,-3.832240,0.050768],[-6.694301,-0.842756,-2.531588,6.947216,6.186451,9.149826,7.728568,-8.389323],[-0.729051,-0.429293,-2.234484,-5.262672,-0.055711,-7.241629,0.247474,-9.693310]],[[-2.470453,-4.101979,-0.650341,-5.694097,8.949864,-1.714137,-4.751482,4.716400],[7.480263,-5.105922,5.454616,8.583845,-0.232417,9.702697,3.358039,4.188244],[-0.601187,-2.496293,-8.887095,-7.430729,-2.348734,-6.465061,3.972228,4.275931],[4.192783,-3.009340,8.676097,-2.591834,0.250814,0.565148,-0.755290,-4.011259],[-2.534137,3.857088,1.500167,2.928718,-7.806387,-0.068424,8.385108,5.200899],[-8.697439,3.030905,1.978337,6.706030,7.499388,-4.576302,-8.814041,-1.229169],[2.519128,8.864938,7.192222,3.696273,-4.179756,4.800214,5.026426,-3.673960],[-8.511395,3.665775,-0.958749,-1.122309,7.604331,6.235403,-6.537644,7.607741],[9.302736,-9.159356,6.265804,-9.141141,-5.575479,8.566845,-0.465191,2.823152],[3.708000,0.341790,7.914643,-5.888048,-2.341142,-9.295898,1.458441,-7.254877],[-2.483676,-3.928626,-7.546071,7.989304,-7.390638,7.738113,9.964987,-5.224037]]], dtype = "float32")#candidate|3332|(11, 11, 8)|const|float32
bop_3333 = relay.floor_mod(call_3304.astype('float64'), relay.reshape(const_3332.astype('float64'), relay.shape_of(call_3304))) # shape=(11, 11, 8)
bop_3336 = relay.floor_mod(call_3305.astype('float64'), relay.reshape(const_3332.astype('float64'), relay.shape_of(call_3305))) # shape=(11, 11, 8)
output = relay.Tuple([call_3316,const_3317,var_3318,var_3319,var_3320,const_3321,bop_3333,])
output2 = relay.Tuple([call_3322,const_3317,var_3318,var_3319,var_3320,const_3321,bop_3336,])
func_3338 = relay.Function([var_3318,var_3319,var_3320,], output)
mod['func_3338'] = func_3338
mod = relay.transform.InferType()(mod)
var_3339 = relay.var("var_3339", dtype = "float64", shape = (154,))#candidate|3339|(154,)|var|float64
var_3340 = relay.var("var_3340", dtype = "float64", shape = (224,))#candidate|3340|(224,)|var|float64
var_3341 = relay.var("var_3341", dtype = "uint32", shape = (56, 22))#candidate|3341|(56, 22)|var|uint32
output = func_3338(var_3339,var_3340,var_3341,)
func_3342 = relay.Function([var_3339,var_3340,var_3341,], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_3399 = relay.TupleGetItem(func_3025_call(), 0)
call_3400 = relay.TupleGetItem(func_3027_call(), 0)
const_3406 = relay.const([[[8.442724,0.287183,-2.691881,1.459752,2.203402,2.799356,5.425349,6.982806],[2.357593,6.538317,9.818226,-2.356648,0.619384,-2.877251,-5.518162,-4.638215],[-5.505610,-4.703430,-7.679274,-9.387344,6.512695,8.423012,8.398968,-0.279757],[8.103637,-5.913837,-9.108631,1.006089,-8.228859,6.336699,7.186892,-2.105476],[4.831809,-3.628963,6.135210,-7.059731,-3.424696,3.836762,-7.455487,0.002552],[4.735193,-9.361084,-4.182559,9.711513,2.635397,0.966851,3.245880,-8.380623],[2.444186,-9.133277,-4.971480,8.137330,5.828081,-4.785801,-2.214854,8.298832],[0.346535,-6.734345,6.162584,-7.358798,-0.850420,0.900976,-9.797855,1.995253],[-5.739638,-1.560702,-3.348703,5.223163,-6.968732,1.184191,3.631561,-5.277957],[-6.016122,1.363204,3.030841,-4.930681,6.009171,0.459253,2.495851,7.887940],[-6.728241,-8.490160,-6.812744,-0.951358,-0.430089,6.275635,-4.241042,-9.566079]],[[-2.300713,-1.325716,-6.733595,-4.840611,-1.102764,7.980147,-3.246481,8.291264],[-1.582825,5.778915,-0.977582,6.442419,6.506424,-0.795308,-4.768872,-6.607004],[-8.265308,-0.701175,3.227010,4.220066,-7.769310,4.181592,5.602996,-0.780778],[6.748412,-9.227800,2.068602,-8.788793,2.098908,3.791742,8.665823,-4.390797],[-5.540686,-4.087009,2.477452,-3.084992,-3.619394,-5.120688,-4.457384,1.761939],[-9.457189,8.811121,1.696458,-8.992226,4.189926,1.870440,0.281989,-1.437677],[-6.406054,6.919067,-7.123352,-5.161359,-4.096694,7.827542,8.109769,-3.044872],[-7.019088,1.940903,0.750442,-0.033180,4.650925,8.876404,-6.403905,9.291711],[9.642860,-6.919974,-4.062205,-6.571428,-8.300702,5.188239,3.043516,1.293465],[-8.912473,8.879738,0.724880,-5.431639,2.285967,2.747348,8.036997,0.788386],[-8.617628,9.359797,-4.876345,0.467009,8.103968,-5.584727,-6.006510,-0.008200]],[[-8.338909,-5.316186,-7.406602,0.619104,-7.685759,0.580842,0.587217,-6.333951],[-8.360647,-2.639246,-7.374424,0.343204,-0.806023,-6.729087,-5.806830,5.172803],[-7.469278,-8.762243,-0.743700,4.974549,-4.359694,4.082343,1.068017,4.800993],[1.082009,-9.884334,8.026468,7.641747,6.529859,-1.815132,-4.128729,-0.730254],[6.474104,5.966712,-4.586925,0.298587,5.980756,-0.100317,-1.292776,0.435157],[6.656520,8.785680,0.488795,7.796450,-8.720041,-5.644080,2.954957,-6.306541],[7.421501,4.706756,-8.733696,1.164310,5.669590,-1.935673,0.790292,2.270310],[9.556401,-4.243478,1.693679,2.627867,1.459317,-3.899509,-8.308708,-7.920260],[3.904427,-7.154456,-9.484516,4.216085,6.177045,9.101086,7.525454,-7.504535],[-5.362452,-2.161197,-8.703917,0.699765,7.019766,-9.072328,-7.877357,-6.073047],[-2.981700,5.480261,-5.164511,-6.589586,-6.673368,-7.952254,-0.429264,-4.130656]],[[0.166937,-4.850818,-9.438062,-7.498615,-8.363396,-6.790616,7.140933,-0.809762],[4.936566,-8.893821,-1.086984,3.130751,-0.525215,8.975676,-6.784955,6.471855],[-7.125526,7.782089,-2.472879,-5.223019,2.849753,1.456012,6.385797,-6.881079],[-8.642933,-0.192598,-6.581683,7.372850,-5.919846,9.386635,6.743323,-3.534241],[9.442283,-4.735052,9.790135,-0.195850,9.559859,2.183317,3.275807,7.050321],[-9.292530,-3.748428,-8.092039,-0.536485,-8.075092,4.171415,-7.622469,3.980655],[-8.621731,2.387840,1.256267,-9.495205,-1.306211,9.789816,9.576795,3.763105],[0.376954,-3.295026,9.320222,-7.638610,1.793845,8.570679,3.295065,5.238178],[7.166737,-9.479064,-0.544812,8.171116,-6.583280,-0.065244,-7.230632,-5.835199],[0.254428,8.000118,2.339649,0.418028,5.524836,-7.076487,3.946009,-1.793700],[6.877571,3.667684,0.702262,-7.651225,-2.122641,-2.086772,-1.453246,-3.472550]],[[9.247735,-1.974137,8.969475,4.712045,4.440036,9.394643,9.487338,4.174859],[-8.793292,-6.604034,4.219796,-9.857624,3.108339,-9.285507,8.456244,-4.637479],[-4.733203,9.339567,-1.460860,7.034365,-8.723975,-0.777040,-8.534915,-8.205808],[3.531453,0.540392,1.580588,-0.613044,-2.359781,-6.655163,8.701323,-1.493272],[-5.350580,3.257870,1.003509,-8.096689,8.669818,0.956373,-5.048060,8.502029],[5.070394,-1.807994,-5.691055,6.730102,-9.037833,-5.986282,-4.776310,5.626860],[-8.606519,7.070677,4.579761,5.764740,2.621005,8.207069,7.873840,2.178997],[6.092235,6.666542,-1.197641,-6.665414,4.002705,-9.286098,5.667921,-3.859716],[-7.014517,5.981067,2.492828,-3.802794,-9.703704,-6.635033,-6.100300,-4.083974],[7.310041,0.290492,-2.105825,-5.327822,-7.901426,-8.462788,0.685284,9.019114],[-0.641392,5.872279,-7.366060,-0.790329,2.423191,-9.887009,-3.320412,2.055744]],[[-5.446168,7.914411,-7.022793,-7.702379,-4.154477,0.970970,3.624003,0.599759],[3.227802,6.552100,8.001724,-2.632037,-9.633894,-8.453987,9.137365,7.533548],[9.526289,0.838731,-9.866034,-5.078616,-8.178829,-5.615445,5.752219,2.203255],[0.352986,-9.595449,3.949126,1.264860,5.413575,-1.208618,-8.866658,-6.211249],[9.542643,2.495043,-6.794545,-3.820070,0.634600,-0.692560,4.210556,-4.226224],[6.706784,5.707763,8.729968,-0.553543,-6.447610,-8.084583,-5.879665,-3.151511],[-0.666012,-2.103592,-6.577680,0.731458,1.943893,-9.454681,5.680858,5.584789],[2.782132,8.248105,-8.913292,3.598972,7.101743,6.494183,-4.715703,7.971666],[0.845249,8.217249,-4.196089,-8.412796,3.530877,-3.099463,5.180667,6.242484],[-4.843175,2.150069,-3.211686,-9.011108,-7.642908,-2.918983,8.683776,9.415950],[6.270268,-7.199076,3.282424,9.961954,8.074857,-5.015639,-1.377812,8.743773]],[[-1.309024,4.622413,5.358356,-1.377434,2.232126,9.621810,-2.422914,2.560036],[2.691913,-3.028774,-4.956561,4.308411,2.336379,-5.256103,5.591095,9.203977],[1.119316,1.189570,-1.342168,-6.595589,-1.486747,-3.467988,1.532221,-0.441536],[-8.627902,0.562169,-0.411674,-4.783525,-6.871459,4.811829,0.653753,-3.664155],[0.283783,3.640549,3.210428,4.046516,9.241519,5.956307,-7.924539,-9.183351],[-5.516875,8.715210,-8.568776,-9.020400,9.064021,0.065808,-8.175675,2.325547],[0.829732,2.825598,-4.912239,-3.730639,8.903089,-8.610472,5.752188,-8.630938],[9.321409,-2.429966,9.703893,-6.739070,0.334612,3.624517,4.047918,6.317070],[-5.716049,-4.619908,-5.251197,-1.101338,-9.323367,1.634540,9.402144,9.385955],[2.191502,2.128854,-7.556597,4.349417,5.788353,-8.823285,4.250678,4.135407],[-2.460655,3.574503,-9.666516,-8.511865,-7.856490,-1.536918,1.834132,-7.893112]],[[8.739613,-1.334919,-7.922939,0.191534,-6.683673,-9.838801,-1.293783,6.836851],[2.660240,4.238739,3.945604,-1.285444,0.302882,4.488415,-8.080989,1.647072],[2.761341,-3.747289,-5.228557,8.969528,3.133373,-3.190132,6.527214,-3.001862],[-5.700197,-8.949359,-5.257487,-2.512786,7.800678,-6.937100,2.959621,-5.732652],[3.339154,-9.590575,-8.712891,8.171445,-8.588046,8.253427,6.460603,-1.024634],[3.677787,2.790279,-6.220370,8.793733,-5.939206,9.349658,-9.463692,-1.140591],[-5.913604,6.180684,7.208437,-6.714449,-9.707348,4.723467,-1.528973,-7.974148],[3.952973,6.017010,3.832029,6.545293,-5.873298,6.939432,-9.750636,3.221871],[9.831829,-8.786674,9.893757,-8.417140,-9.366184,7.150713,5.099710,1.379633],[-5.239741,-9.354078,4.299686,5.960764,9.353651,-4.232859,-0.302932,-8.137000],[-5.826013,-4.612219,-3.681774,-0.369646,4.054469,7.752858,8.274214,7.716070]],[[8.394100,5.566425,7.709104,-3.061254,3.788741,8.292775,-2.801844,2.569963],[-6.573756,-8.152553,-1.013354,0.323234,3.018707,1.849913,1.581292,-1.438530],[-2.796518,-3.457359,-9.131697,-3.225224,8.244544,9.978711,-7.497436,2.995386],[8.050866,7.483145,-9.139590,8.404562,0.277182,-1.482272,0.289652,3.157732],[-5.418369,8.399725,-9.712872,-1.213736,8.414177,-2.474572,0.051066,-8.670503],[2.858943,-6.550117,2.093620,8.209535,-3.285965,5.918816,-9.294852,-3.495559],[-6.921423,7.968797,1.054114,0.679740,-3.725767,-6.664278,5.504559,-2.309171],[-1.254822,-3.915841,-7.405016,-8.971014,3.071342,-6.213009,-1.018720,-4.607349],[-5.617783,-8.219523,3.525562,4.422147,1.303538,2.323153,-8.096373,7.384528],[2.176249,-2.944954,-6.867480,-0.745309,2.153606,2.677748,5.559276,-4.434579],[-7.030385,-4.939516,-3.750808,1.459244,9.043477,-2.754806,-5.465690,3.101988]],[[1.763494,6.862072,-9.997099,9.430839,-6.935142,-5.990978,-3.381460,8.592002],[1.548744,2.995152,1.929450,8.891289,7.647650,2.818853,7.315255,6.183080],[-9.906419,-7.991895,4.653792,-6.347176,5.575189,7.347455,-0.491001,-3.851568],[-7.099611,6.638746,-5.559969,6.694422,7.230445,5.122738,7.249990,9.822851],[9.593508,-1.615374,-6.924211,-7.373825,7.855359,2.542809,-9.990019,4.880414],[2.679762,6.281748,0.436283,-1.238486,5.725319,-9.809205,-4.076011,-0.805256],[4.880264,-7.901180,-3.146425,7.756048,4.725730,2.510891,-3.609823,-6.962530],[2.389608,3.187551,-3.763972,5.596681,4.618502,-1.385080,-5.715849,3.583149],[-4.516614,1.374565,-9.105065,-7.038852,0.978886,-0.624679,6.381173,-2.966065],[-5.101877,4.793564,6.719681,-1.370315,-6.575103,-6.067731,0.739930,8.168448],[-8.383277,-0.282285,6.937055,-6.925232,-4.716863,1.906638,8.157051,4.604511]],[[2.212028,7.243260,1.508131,-0.834915,-6.351118,-9.266725,-7.006166,4.844307],[-9.213237,-8.958016,6.848933,5.366225,2.138505,6.214222,-4.766965,-6.417979],[5.594254,-9.417317,4.196926,0.378237,0.390353,2.319822,5.330466,-2.215641],[8.274255,1.903852,8.918238,-6.706877,9.271304,-4.951077,-3.473840,-4.043242],[-9.149589,1.496358,6.384244,1.668709,-0.407997,-7.384383,-2.861909,-4.232801],[6.164191,-7.798737,-9.635547,9.511307,-0.562034,6.410441,-4.661796,-6.355669],[-6.092435,-0.265988,-4.600276,-4.850017,8.857041,-2.764901,-5.305822,0.950996],[5.307827,-3.117437,-5.152412,1.716420,7.667880,-8.343316,-3.219012,-5.150521],[-1.367982,-2.118290,7.425021,4.401055,-4.748938,-6.758059,-3.601163,-9.343921],[0.444260,8.182081,3.865055,-9.377843,9.571429,-8.514573,1.034203,-3.519920],[-1.825155,7.045815,-3.141048,-6.567239,-7.339054,3.812324,-3.567595,-9.453450]]], dtype = "float32")#candidate|3406|(11, 11, 8)|const|float32
bop_3407 = relay.logical_or(call_3399.astype('bool'), relay.reshape(const_3406.astype('bool'), relay.shape_of(call_3399))) # shape=(11, 11, 8)
bop_3410 = relay.logical_or(call_3400.astype('bool'), relay.reshape(const_3406.astype('bool'), relay.shape_of(call_3400))) # shape=(11, 11, 8)
output = bop_3407
output2 = bop_3410
func_3418 = relay.Function([], output)
mod['func_3418'] = func_3418
mod = relay.transform.InferType()(mod)
output = func_3418()
func_3419 = relay.Function([], output)
mutated_mod['func_3419'] = func_3419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_3420 = relay.TupleGetItem(func_3244_call(), 0)
call_3421 = relay.TupleGetItem(func_3246_call(), 0)
output = call_3420
output2 = call_3421
func_3428 = relay.Function([], output)
mod['func_3428'] = func_3428
mod = relay.transform.InferType()(mod)
output = func_3428()
func_3429 = relay.Function([], output)
mutated_mod['func_3429'] = func_3429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3428_call = mod.get_global_var('func_3428')
func_3429_call = mutated_mod.get_global_var('func_3429')
call_3500 = func_3428_call()
call_3501 = func_3428_call()
output = call_3500
output2 = call_3501
func_3507 = relay.Function([], output)
mod['func_3507'] = func_3507
mod = relay.transform.InferType()(mod)
mutated_mod['func_3507'] = func_3507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mutated_mod.get_global_var('func_3507')
call_3508 = func_3507_call()
output = call_3508
func_3509 = relay.Function([], output)
mutated_mod['func_3509'] = func_3509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3419_call = mutated_mod.get_global_var('func_3419')
call_3599 = func_3418_call()
call_3600 = func_3418_call()
var_3616 = relay.var("var_3616", dtype = "bool", shape = (11, 11, 8))#candidate|3616|(11, 11, 8)|var|bool
bop_3617 = relay.minimum(call_3599.astype('int16'), relay.reshape(var_3616.astype('int16'), relay.shape_of(call_3599))) # shape=(11, 11, 8)
bop_3620 = relay.minimum(call_3600.astype('int16'), relay.reshape(var_3616.astype('int16'), relay.shape_of(call_3600))) # shape=(11, 11, 8)
func_41_call = mod.get_global_var('func_41')
func_44_call = mutated_mod.get_global_var('func_44')
var_3632 = relay.var("var_3632", dtype = "uint64", shape = (120,))#candidate|3632|(120,)|var|uint64
call_3631 = relay.TupleGetItem(func_41_call(relay.reshape(var_3632.astype('uint64'), [8, 5, 3]), relay.reshape(var_3632.astype('uint64'), [8, 5, 3]), ), 0)
call_3633 = relay.TupleGetItem(func_44_call(relay.reshape(var_3632.astype('uint64'), [8, 5, 3]), relay.reshape(var_3632.astype('uint64'), [8, 5, 3]), ), 0)
func_2688_call = mod.get_global_var('func_2688')
func_2691_call = mutated_mod.get_global_var('func_2691')
const_3665 = relay.const([1.122390,-6.711082,-7.201126,9.767236,9.689501,-1.324437,-6.010169,9.785620,-3.573041,-2.502592,6.620049,5.409389,-8.602286,2.647295,7.081885,6.281338,-1.690172,0.478074,3.486791,6.190218,3.633619,-1.993692,-4.248130,0.228262,0.336343,1.223560,-8.167408,0.161451,8.887267,-6.258342,-0.337335,-3.224311,-4.058606,5.330576,-5.316910,-6.258020,-0.323031,9.102903,-0.299133,-5.436508,-3.698819,4.031831,-1.510027,-0.514939,1.463005,-3.656254,-3.382366,-1.112207,2.440590,-8.337482,5.485053,6.778126,-3.881608,-5.947820,8.257443,-2.612779,-4.133619,4.495383,3.583373,-3.951883,-1.519891,-3.109559,8.215570,1.611416,-6.284762,-7.423445,-3.432687,6.631125,-8.963247,-6.500501,-9.011505,-6.568214,-0.695897,-6.873478,6.346990,-1.771439,3.767326,-6.072293,6.169567,6.596308,-4.351368,7.339644,-1.113150,7.920997,-7.797431,-6.707715,-4.576675,7.153524,-2.274381,-2.115442,5.426323,-0.743189,9.912957,7.911892,-2.779183,-9.811608,1.839487,-8.192207,2.461081,-3.423896,7.737614,-7.960434,3.151449,-5.086325,6.308998,1.764599,3.318410,-9.513220,2.067153,4.093165,-0.195101,-7.246922,-7.440223,1.685465,-0.219515,8.465509,8.141986,6.346722,-2.411963,-0.784399,2.658032,-6.382063,7.264648,2.382516,-8.200930,6.641720,6.526257,-1.422170,-7.760119,2.928190,-0.502859,-9.228320,-0.316159,-2.906649,0.375880,5.957793,1.763652,2.520503,-7.600089,8.782572,3.242522,6.020843,-2.340850,-5.631694,-1.460432,3.763346,2.840070,-1.502945,4.020325,-9.244250], dtype = "float32")#candidate|3665|(150,)|const|float32
const_3666 = relay.const([5.322283,-1.888743,-5.949553,-4.304235], dtype = "float64")#candidate|3666|(4,)|const|float64
call_3664 = relay.TupleGetItem(func_2688_call(relay.reshape(const_3665.astype('float32'), [5, 5, 6]), relay.reshape(const_3666.astype('float64'), [1, 4]), ), 0)
call_3667 = relay.TupleGetItem(func_2691_call(relay.reshape(const_3665.astype('float32'), [5, 5, 6]), relay.reshape(const_3666.astype('float64'), [1, 4]), ), 0)
output = relay.Tuple([bop_3617,call_3631,var_3632,call_3664,const_3665,const_3666,])
output2 = relay.Tuple([bop_3620,call_3633,var_3632,call_3667,const_3665,const_3666,])
func_3668 = relay.Function([var_3616,var_3632,], output)
mod['func_3668'] = func_3668
mod = relay.transform.InferType()(mod)
var_3669 = relay.var("var_3669", dtype = "bool", shape = (11, 11, 8))#candidate|3669|(11, 11, 8)|var|bool
var_3670 = relay.var("var_3670", dtype = "uint64", shape = (120,))#candidate|3670|(120,)|var|uint64
output = func_3668(var_3669,var_3670,)
func_3671 = relay.Function([var_3669,var_3670,], output)
mutated_mod['func_3671'] = func_3671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3678 = relay.var("var_3678", dtype = "float64", shape = ())#candidate|3678|()|var|float64
var_3679 = relay.var("var_3679", dtype = "float64", shape = (3, 6, 3))#candidate|3679|(3, 6, 3)|var|float64
bop_3680 = relay.mod(var_3678.astype('float64'), var_3679.astype('float64')) # shape=(3, 6, 3)
output = bop_3680
output2 = bop_3680
func_3703 = relay.Function([var_3678,var_3679,], output)
mod['func_3703'] = func_3703
mod = relay.transform.InferType()(mod)
mutated_mod['func_3703'] = func_3703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3703_call = mutated_mod.get_global_var('func_3703')
var_3705 = relay.var("var_3705", dtype = "float64", shape = ())#candidate|3705|()|var|float64
var_3706 = relay.var("var_3706", dtype = "float64", shape = (3, 6, 3))#candidate|3706|(3, 6, 3)|var|float64
call_3704 = func_3703_call(var_3705,var_3706,)
output = call_3704
func_3707 = relay.Function([var_3705,var_3706,], output)
mutated_mod['func_3707'] = func_3707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_3746 = func_2943_call()
call_3747 = func_2943_call()
output = call_3746
output2 = call_3747
func_3760 = relay.Function([], output)
mod['func_3760'] = func_3760
mod = relay.transform.InferType()(mod)
output = func_3760()
func_3761 = relay.Function([], output)
mutated_mod['func_3761'] = func_3761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_3833 = func_2943_call()
call_3834 = func_2943_call()
output = relay.Tuple([call_3833,])
output2 = relay.Tuple([call_3834,])
func_3862 = relay.Function([], output)
mod['func_3862'] = func_3862
mod = relay.transform.InferType()(mod)
output = func_3862()
func_3863 = relay.Function([], output)
mutated_mod['func_3863'] = func_3863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_3872 = func_3064_call()
call_3873 = func_3064_call()
output = call_3872
output2 = call_3873
func_3874 = relay.Function([], output)
mod['func_3874'] = func_3874
mod = relay.transform.InferType()(mod)
mutated_mod['func_3874'] = func_3874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3874_call = mutated_mod.get_global_var('func_3874')
call_3875 = func_3874_call()
output = call_3875
func_3876 = relay.Function([], output)
mutated_mod['func_3876'] = func_3876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_3903 = func_2943_call()
call_3904 = func_2943_call()
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
const_3906 = relay.const([[-0.937050,-6.282717,4.101789,-6.381154,-3.379157,-8.528900,-6.099348,-5.559003,0.376076,1.674365,-3.782619,-4.079798,-3.354132,-8.451586,-4.170219,-3.278409,-7.730359,0.689764,2.385457,-4.048075,7.187499,4.306481,-5.414774,9.341813,3.001184,-8.224056,-5.780798,4.946094,0.878225,-9.415905,-3.688855,-7.140526,4.067320,5.465864,3.522262,-7.615944,-6.196861,-9.758184,-6.227703,-0.088110,-6.400455,2.457812,3.613534,5.988938,-0.645401,0.734877,-2.317068,9.605838,1.712867,9.141663,-3.802404,1.016956,1.995095,0.245703,0.157161,-7.934429,1.686398,7.662150,-6.929705,6.523257,-7.804085,9.084774,-2.791408,-0.570592,6.494705,-3.494564,5.335674,3.336309,4.642538,-1.588038,-7.014927,-1.481577,-2.659075,7.799673,0.990610,8.320509,5.434793,-2.272603,7.445731,2.158317,-3.534252,6.100248,-6.045386,1.192457,1.473510,-4.532470,-8.450787,4.597719,-3.904109,9.532024,6.557925,2.832881,5.639312,-5.711552,-4.289726,-0.690136,4.423687,8.294323,-8.758974,5.350129,-9.168876,5.140535,9.907219,-2.297651,5.159637,4.120803,-5.471157,7.541105,-2.750362,3.112610,-8.167822,-6.156685,4.853030,9.623226,-7.182126,0.036032,-4.603843,9.665804,-6.894267,-9.068308,4.743027,-2.031222,-5.192805,8.865090,-7.356568,-5.472592,-8.090875,-6.173105,-0.373894,5.610592,8.552896,2.305833,-0.685683,1.796562,-1.560573,-9.022319,6.445270,-3.123252,9.542089,-1.603843,-5.936123,-5.360938,6.708671,-1.328129,-7.707656,-7.414557,-5.954532,0.686769,-1.828092,1.637646,-0.856475,-6.586187,9.860036,-8.726657,9.825299,-6.605817,0.103666,-9.352861,6.023360,-5.727854,7.198714,4.899525,-2.111007,-2.774894,2.241635,-0.068298,7.061042,1.199433,7.705828,4.583875,6.947859,-9.247566,-9.421249,2.603304,8.578246,1.948349,4.813350,-0.216359,-3.963836,-8.172083,3.755804,2.295505,-3.641960,3.828421,-7.873625,-8.261485,-6.674103,-5.992010,5.715796,-0.740495,7.712870,1.414314,2.904218,1.091658,-7.668636,4.269027,-6.434887,5.884685,-7.563031,-3.202295,2.598087,-7.821134,1.048025,7.762159,-5.408660,2.664255,3.888422,-2.816557,-0.458037,-3.624906,-6.611176,-1.703579,0.263068,3.126342,-8.614965,-4.654819,-3.299165,9.940889,-7.245079,-2.359531,5.668296,-5.232926,4.756910,6.948764,-7.599628,-3.468225,5.247179,7.664168,-8.367147,-3.585967,-5.510460,9.780885,3.159127,-9.790515,0.699316,2.255108,-4.653675,3.520091,-4.270961,-2.795535,5.327831,1.980895,9.048917,5.143206,8.424814,8.689685,-7.350746,-0.774407,4.215068,0.983978,-7.585318,3.471998,0.942973,-1.768652,5.068698,-2.241013,6.036183,-9.026403,6.036921,9.819910,0.239432,-6.785574,1.992149,-7.243563,-3.921726,5.630636,-8.193437,9.664348,9.550153,3.818770,-0.426711,9.701862,-7.352348,3.025449,8.095654,-9.310263,2.872530,0.969155,-5.769207,4.597298,0.103158,1.054428,-3.802226,5.250150,-9.563378,-1.486979,3.227732,-5.694640,9.641072,8.737460,-6.363792,-2.376085,-7.751745,-6.312542,5.914727,3.503715,-5.092958,-5.928934,-7.481971,5.049748,-3.915257,0.099531,4.829558,5.759948,6.997177,-6.360535,7.095171,7.146265,-0.048676,-2.952999,-3.264444,-3.036610,-9.150085,1.233553,5.246856,9.116035,-8.678822,8.692607,-6.421294,0.604021,1.225555,-4.734036,-0.596231,-4.484194,2.607721,-5.649060,2.336784,0.904260,9.206028,-7.909178,7.877176,-2.779898,-8.183938,3.517563,1.158186,4.159266]], dtype = "float32")#candidate|3906|(1, 336)|const|float32
const_3907 = relay.const([-9,8,-5,7,10,-6,3,-1,-2,-4,6,6,-3,1,10,-3,4,-4,-2,8,-10,-4,-6,8,9,-6,2,-7,7,-2,-4,9,8,-9,-6,-4,-3,1,-3,-7,1,-7,5,7,-4,10,5,7,3,-8,7,9,-10,9,-9,8,-8,-2,-1,-5,-9,-4,-6,-2,7,10,-9,3,-9,-5,-9,-10,-9,9,1,-4,1,-7,-9,6,8,-9,6,8,-4,-8,7,-9,-8,6,-2,-2,-10,-8,9,-4,-1,-3,7,-4,6,6,-10,10,3,9,-10,-8,1,7,1,6,6,-9,-1,-4,7,-10,4,4], dtype = "uint64")#candidate|3907|(120,)|const|uint64
call_3905 = relay.TupleGetItem(func_777_call(relay.reshape(const_3906.astype('float32'), [6, 7, 8]), relay.reshape(const_3906.astype('float32'), [6, 7, 8]), relay.reshape(const_3907.astype('uint64'), [120,]), ), 1)
call_3908 = relay.TupleGetItem(func_781_call(relay.reshape(const_3906.astype('float32'), [6, 7, 8]), relay.reshape(const_3906.astype('float32'), [6, 7, 8]), relay.reshape(const_3907.astype('uint64'), [120,]), ), 1)
func_3418_call = mod.get_global_var('func_3418')
func_3419_call = mutated_mod.get_global_var('func_3419')
call_3909 = func_3418_call()
call_3910 = func_3418_call()
const_3921 = relay.const([[-1.176796,-8.916444,3.860302,-3.980152,7.724000,-9.853543,4.191427,9.081631,7.053722,-6.000231,-1.191682,-4.934825,-5.020385,0.577353,-1.513025,2.811489,-8.527874,-1.790525,3.615248,6.512765,-3.284497,-3.127814,-2.162891,-2.530196,2.393229,-4.962688,-4.272689,-8.551247,-4.592068,-7.193360,-1.005503,1.823992,6.607558,-4.235562,-1.862316,1.133422,-9.305883,7.662714,-8.217472,-5.264817,-9.256038,6.023804,-7.151447,3.414383,9.310618,2.802311,0.278135,-9.630175,-4.077545,8.121014,-8.219008,0.125520,-6.318840,6.778406,-4.668494,-6.312637,-7.711718,-1.472403,6.355725,8.774990,4.641104,2.389809,5.951326,-9.650353,-1.499125,7.003145,-0.626582,4.811834,4.471412,6.537165,8.054310,-1.794569,0.287234,-2.558339,-5.854641,0.950815,-6.172888,2.895540,-2.370119,5.971927,7.256739,9.573664,-9.940478,2.043905,2.781170,1.304328,-6.162335,2.487024,-7.533216,9.534855,5.091168,8.503001,4.584529,-6.895212,-1.366689,-7.568718,-0.155337,0.831352,7.273043,-0.142042,-0.296964,5.793792,4.278804,-6.338332,-7.026410,-0.163317,0.276605,2.744191,-9.253715,-9.891865,0.714217,7.720725,9.750268,-2.518992,6.164043,3.081388,5.902896,-6.615290,7.962499,-8.282772,-7.517871,-1.920795,-6.445114,-2.220740,5.015368,6.323433,-3.003625,-9.082255,-9.282694,-0.374785,3.468213,7.070369,-8.860610,4.117865,-4.646673,5.225605,-2.621368,-4.815743,7.889070,-7.926818,-0.634493,5.260146,-1.505531,-5.608973,8.950393,-3.499468,-4.200621,2.408077,1.024547,4.220636,-8.969919,1.009748,-5.770625,-2.284886,-2.380962,-7.459750,-1.872560,8.143115,6.043725,9.848674,-3.952891,4.219885,2.843426,4.026278,8.194929,5.282843,8.410124,-7.964291,-1.915837,4.597742,2.281211,9.651400,-2.517316,-0.292621,-2.409852,-8.322578,8.764522,-4.378409,-9.113787,-9.665240,-2.915555,0.386060,-7.208858,5.459398,-9.356124,8.088510,-5.009475,-6.409778,-4.725530,-3.052802,-0.428713,1.157834,-6.410558,8.125850,-0.046125,-4.344590,7.362825,-6.097569,8.902678,-7.325683,4.351056,-8.640980,2.733866,-5.804622,0.420887,-3.605471,9.272357,-8.489358,2.348821,-5.705856,4.541231,-4.098945,-9.744923,-0.517720,-5.777031,-2.879136,-3.956844,0.035045,1.559031,6.553393,-1.636997,-7.561301,-9.575005,1.822197,-3.774658,7.701713,-2.652236,-2.525657,-7.013762,6.386470,-3.321812,-7.315898,-8.343759,-2.795462,3.871801,-4.335098,7.471833,4.532479,0.447069,-4.061800,-3.423751,9.406268,6.964345,-6.245793,-7.139826,4.151825,1.453750,-1.773661,6.775444,1.793845,-5.134162,6.935405,-4.808468,4.660545,0.377257,-7.669989,6.423222,7.218576,7.831840,2.892701,3.079383,-2.386457,-2.991239,-7.411315,7.171502,0.017850,9.318209,-3.162940,0.166497,-2.983743,3.752622,9.875157,-9.418890,8.715330,-1.702407,-4.875246,4.714519,-7.106788,7.088480,-0.018178,-6.041823,-7.795795,-1.175255,8.712481,2.076597,-5.972108,-9.922648,8.223402,-1.672749,0.478883,7.119831,-0.232737,-9.653259,9.879191,2.215131,3.472023,9.988485,-4.897179,-0.806477,4.813553,4.936892,-7.612248,3.442270,-6.692863,-8.563543,-1.015216,0.256619,5.282591,4.104973,1.733785,-6.644009,-3.504872,2.428987,1.661687,5.089110,9.221673,-9.882779,-8.410351,1.030132,-9.008357,-9.026241,-4.832107,6.599273,-8.717833,-8.267294,-9.432084,-1.613080,-9.021976,1.583754,0.981544,-0.464904,3.653220,-5.004503,7.285473,-3.252542,8.386006],[-2.772936,5.168064,4.629418,6.623536,4.590466,-7.503019,-5.573649,3.962097,-8.245056,-9.969450,1.716940,-8.710461,-8.936320,-0.199830,3.514160,7.215657,0.494958,8.217460,-4.061484,-8.574101,-6.772494,3.827105,7.974266,-5.129594,1.714636,-7.207269,-3.140256,-9.179198,-7.166289,-0.602652,2.729307,-5.029678,-5.387097,4.447832,-8.697236,-5.714731,5.543389,4.220487,6.767509,-8.107136,0.768411,6.128788,4.935999,-3.987532,-5.131052,6.690246,-8.059607,-0.265213,-5.040714,-7.088563,8.928812,3.093737,-4.468051,1.820117,7.476178,3.001302,8.143867,-9.068723,-9.322873,-5.533864,6.996844,-3.023359,8.689933,-1.625108,2.634615,-9.537496,-5.026461,8.658363,8.030215,-0.445075,-3.771164,6.240736,-7.951302,1.551122,-7.447000,-4.403748,9.676040,2.718873,5.862138,-8.311860,-7.633680,-8.329490,1.692095,-7.709485,-3.489264,7.850522,-5.091253,-7.197736,-4.007722,0.758589,-5.817861,8.704702,5.228413,-9.995548,-7.158292,0.099549,-6.045222,5.292965,5.466234,-6.845008,-4.075099,-3.823420,-4.568226,-4.066710,-3.703287,4.682594,8.182773,0.959289,8.803884,3.308494,-6.908061,1.072875,-4.224169,-6.294296,-8.504512,-4.713897,-9.225946,2.511805,0.857279,-5.905683,3.324883,-3.672127,-1.807951,8.613855,-2.863657,5.097970,9.681845,2.493850,-9.831522,4.244457,-6.528363,9.415489,2.625623,0.220443,-7.974392,-6.822986,7.766968,-6.477821,-7.540197,5.733578,4.693191,-0.200655,3.388949,-6.487563,2.247757,-9.627023,5.723412,4.375529,-5.419289,-1.422262,-4.636258,7.104207,0.238322,7.080736,6.159397,-1.936834,7.687292,-9.078651,-6.095914,-4.314954,-4.671160,5.412806,0.864661,-5.858744,3.527523,-4.955468,-0.626162,6.569047,-6.636154,4.367321,-4.566013,-2.908977,-2.502536,-0.104102,8.241491,3.267004,-6.714416,-3.773254,7.983431,6.825045,4.678129,-0.527534,4.346734,3.602920,-2.689513,-3.537424,9.723800,-0.136484,4.075577,-9.058335,-9.998837,-4.619460,4.213604,-4.800773,-6.364485,0.999236,0.603334,4.993488,-5.634920,-8.302115,2.342262,8.162647,1.772691,6.930080,-7.655590,-9.441287,5.666832,6.939682,1.424177,0.955852,-3.088623,4.661010,-8.644508,-1.297846,0.022581,4.105909,6.959470,1.518506,-4.327124,4.550462,7.362572,5.022935,7.722025,1.483627,-6.446537,-8.433219,7.218989,6.685163,-5.263577,-8.444714,-0.084453,-3.236022,-4.579325,6.986235,-4.956075,-1.979795,-2.286368,-6.011545,-4.631166,-5.268323,-7.433693,9.866780,-6.167636,9.479257,3.367447,-5.436239,0.849985,2.777559,4.867753,4.780499,-5.802356,8.421202,2.011307,-0.641979,3.550247,2.270168,2.545213,1.729134,9.338530,-9.353032,6.708452,-3.229536,5.903969,-4.390339,-5.574907,5.190398,9.190889,8.985741,-6.199773,0.341415,-1.979817,-9.870341,1.534180,5.189713,-1.273775,1.620099,0.490616,6.713480,-8.547145,5.572463,0.737444,5.435743,3.995023,9.598830,-4.969311,5.005242,9.691071,-7.678259,9.050768,5.004377,5.078022,0.308550,1.898314,9.081710,6.966482,-2.839420,9.097907,7.856059,6.885954,9.970049,5.562925,-6.215383,-3.299018,-2.618892,7.950490,5.078736,-8.602642,7.698948,5.742099,6.861485,3.762018,8.472700,3.402476,9.708760,-7.966400,-8.989693,4.963043,-2.817488,9.334595,8.297205,4.376431,3.465042,-9.997624,5.139580,-5.551552,-2.000816,-9.942917,-8.444488,-9.286070,-6.504320,-9.007696,7.741170,-1.995973,8.650394,-8.434986,-1.480809],[-6.833786,3.618521,-6.964806,-0.024737,-2.689627,-4.840842,1.801115,-6.879139,-8.637537,-7.156004,-8.974221,-5.931223,2.973997,-1.351169,-0.972594,6.662573,7.371094,4.436684,9.021736,-9.488382,-1.845264,2.104723,6.039788,-7.034165,-5.917851,0.568947,-0.630223,9.729848,4.581431,3.797958,-6.342715,-9.440724,6.231210,1.831707,-3.137412,-8.076092,-9.700066,-7.787594,-4.130113,0.611296,3.382416,4.038584,-2.823321,1.752275,-8.975979,-3.139779,-8.383750,-1.025042,-7.548255,-3.331173,6.603119,-3.984840,-7.718219,-1.261076,6.442360,-4.216797,-2.903153,-8.398979,-8.621477,-7.182434,-2.513417,-7.533783,-0.201811,-0.298693,-1.018977,7.601310,-3.168197,-4.995448,-0.026295,9.989726,-9.517574,-2.757466,4.738403,-3.430716,-7.022197,-5.472248,9.680486,8.901297,-2.223737,-8.611196,0.515953,-3.031008,9.209091,-8.313003,6.058427,9.464217,3.226782,-8.167680,-2.014210,6.731778,-3.882785,1.661864,-7.621518,4.225709,6.646381,4.522220,7.422810,-0.952596,-8.984684,-7.173386,-9.740664,-8.015314,4.806318,-1.687457,9.725234,-9.709248,6.435337,0.931440,6.647121,-2.300408,-5.217946,3.110957,-2.825747,3.283742,-0.084192,-6.794267,8.851541,9.055366,-4.154931,5.586677,9.631499,3.133700,8.473619,-1.749248,0.364021,0.730387,-0.036556,0.083284,-1.091026,-5.170382,-1.604056,6.897537,9.502388,-8.855725,-6.635333,2.057801,9.099094,1.959890,5.153351,7.871531,-1.880154,-5.096752,9.920263,7.244306,-6.236827,5.699824,5.360184,0.342994,7.566772,-2.776699,3.518564,6.339431,-7.256426,2.504306,-2.437867,-4.512628,-1.674330,3.786078,-2.930056,6.836423,-0.223210,4.035133,-2.838007,-2.082321,-5.094654,4.735872,-5.591722,-3.819362,7.818001,-9.371378,3.585445,9.537250,-0.170980,3.593580,8.611448,4.851600,0.725126,4.911801,0.079037,3.847658,-2.809390,6.476418,2.294484,2.700055,-2.594254,-1.627884,-4.502870,4.038859,1.547747,5.492036,3.811190,-2.196149,7.617308,-1.485790,-5.756305,-1.682904,0.043138,6.967156,-5.410091,3.093635,7.989727,-3.934656,5.025146,-8.070844,-9.370800,-2.896359,-3.938949,5.073615,-9.494612,7.316361,9.515553,-8.301612,9.929311,-0.862254,-8.257778,-0.251392,0.629429,-7.864863,-3.213295,0.828261,-1.126037,9.409234,1.730677,2.992005,-9.837035,-0.829794,-7.225855,-5.112605,-2.210462,3.348188,5.885502,-3.118083,-7.472694,9.703751,8.376631,-2.273542,-4.733161,6.309104,-9.478888,-0.053314,4.643665,-5.194194,3.391247,1.975297,2.813624,-0.621665,2.765461,-5.622781,6.182865,-8.507304,-0.172683,2.010992,-0.629329,-0.987850,7.643765,-3.778798,8.730958,-0.359026,1.812728,9.563038,2.772354,4.316093,-5.398666,-9.957769,-3.739270,0.473472,8.703628,3.376398,5.049197,-9.232402,-5.021251,2.827351,-2.024777,-1.698515,4.835460,-9.805742,-7.809509,5.370878,3.545628,-4.217629,3.758017,3.138046,-0.983092,-0.943566,-6.172403,-7.916595,2.667765,3.473788,-3.792975,-4.791723,4.599711,-7.834065,-5.958103,-3.782064,3.509384,6.530642,-0.111335,-1.221956,-3.004134,-4.857969,1.668130,6.494454,-2.527310,-4.942226,2.334740,4.866981,-0.924098,-5.512543,1.017720,-0.930709,4.861747,0.467283,-8.964160,4.863914,7.612344,-3.217478,-1.674398,6.287355,-2.680268,2.225924,-7.514650,-0.851917,-3.402657,-6.600403,8.965168,4.624700,-9.679087,8.967479,-8.405647,8.133708,-2.929143,-5.516711,-2.447003,-2.654369,-6.011754,-0.876893],[-1.376402,0.748329,4.734259,-3.887991,-7.660309,2.771282,7.227433,-9.790010,8.164679,1.772960,8.326308,4.146387,3.553017,-2.942462,3.951890,2.987062,7.378142,1.802895,-7.926249,7.179171,6.719070,1.220981,3.898209,-6.753983,-1.252102,7.723522,8.219031,8.088768,-5.497779,-5.677188,-5.277946,8.735000,-2.825209,-1.022299,-1.974329,-0.585377,-3.425904,-8.769354,0.659546,3.534184,-6.005575,6.285444,1.480329,9.927236,-9.048855,4.570530,7.120894,-7.949360,8.109798,-2.171018,-8.756077,2.705992,-0.141301,7.800378,-2.968706,2.730829,4.331723,4.709499,0.925856,-1.773706,-6.341748,-7.034647,-3.334008,-1.796986,2.194454,5.482328,1.234437,5.950565,1.585097,9.153332,5.450640,-7.911392,6.479056,1.673788,-8.137359,-1.749530,0.304909,-4.942467,2.629223,-6.358507,5.072751,-3.063740,-5.856127,0.589183,-6.189713,-1.848216,3.545038,-1.275744,-8.825980,-1.589441,6.576054,1.707963,7.153146,-3.573787,-8.197292,-8.326690,0.494110,-8.997391,-4.014036,1.415658,-1.269308,-3.074891,-4.289344,-1.621171,-8.735991,-5.559780,2.248651,-7.919631,9.318952,1.039373,5.232026,-9.391929,1.712739,6.830697,-5.022732,-4.370740,-4.190083,-7.115906,-1.824052,3.654176,5.658495,-3.171430,9.766163,-5.391152,-8.228334,0.704195,8.312742,-9.029400,-5.021122,-4.210446,-8.893304,-6.780686,1.728116,6.706440,6.605137,-1.696853,-3.531201,-3.271452,8.606266,9.399548,-3.043934,-3.096637,-5.351394,-1.448114,-7.054454,5.245846,-3.366876,6.095396,-1.736240,8.669250,0.406152,4.994106,-1.749707,5.337092,-5.378794,4.299143,3.095208,-8.348716,-5.757990,9.140096,7.561902,5.633299,-7.249007,4.692706,-8.924504,-4.725802,-5.613643,7.732320,1.294657,-0.100696,3.855805,4.310261,8.852285,-6.903390,-1.511496,-4.014727,-2.426183,0.113678,-6.475154,-8.890074,9.609289,-1.025611,-5.016565,6.903519,9.354222,8.427082,6.091905,6.630490,-8.789165,3.347843,6.879340,-4.406095,4.316329,-8.729067,-1.789618,-6.128762,-5.971903,9.083438,8.832791,-9.491231,-6.149244,7.485113,-5.843750,5.061703,9.259322,-9.971783,-4.908094,-5.737854,-9.555793,-5.619344,7.489640,0.868267,7.071239,-3.498321,4.744549,2.048415,-8.546271,4.699346,-4.088245,8.837148,4.656126,-1.545243,-5.618930,-8.995191,-6.925430,7.212453,8.748285,7.504977,1.826762,2.250437,-4.597742,0.583764,-3.368616,-1.888228,1.607644,-6.072532,5.771446,-8.914353,4.377790,-3.316287,4.681935,-9.935808,-5.486876,-1.003148,1.217954,-7.561404,-2.266065,1.000000,2.953583,0.222380,0.070298,9.361051,4.557399,6.614437,-6.537688,-3.650538,3.486154,0.699836,-0.108028,-5.003787,2.477725,7.339339,-9.790769,-5.361959,-7.468657,-8.787600,0.622214,-0.349417,6.521184,-8.083348,-1.491738,-0.980899,6.059260,3.122592,1.606066,8.623765,5.977275,-5.728576,5.019757,4.632127,2.515454,-0.083797,4.499225,5.771238,-5.682103,7.066205,-1.249405,-5.018308,0.823512,3.856091,5.632049,5.341779,4.079844,-3.760092,7.175329,5.143782,1.853335,5.243093,-3.113522,-4.298832,-6.877514,2.879283,1.969890,-4.862015,-3.343982,8.032745,1.510354,-2.231533,-6.308085,5.676946,-8.174742,-2.479337,-4.769942,-8.433686,-8.286927,0.924489,-3.283678,6.976252,6.946455,-3.432846,3.035971,1.462581,7.116615,-7.409639,4.030681,7.477599,-1.870147,5.080497,8.004850,1.104972,-1.486886,1.808927,-3.192176,-0.728054,-5.499391,1.358317],[-9.150005,-1.104384,-6.276115,-1.406568,2.216731,3.870642,0.839143,-0.143612,-8.652438,4.089134,5.617192,-0.124692,1.411433,4.477961,2.290146,-5.888411,9.106101,8.657902,3.407591,3.109117,1.261084,-2.108560,-9.596130,-1.453896,-9.413799,7.602663,-0.731608,7.914421,7.828464,2.378612,9.549576,-7.890960,3.821961,-0.697997,2.900772,4.058908,-0.942484,-2.951700,-7.421858,-1.421696,-2.043629,-5.808805,0.165241,-1.327257,-7.337923,6.134169,5.886545,6.913189,-4.108047,5.877502,5.045592,-8.933948,-5.246058,-3.633319,9.360893,-8.958493,5.388997,-7.412200,-1.701564,7.454145,7.779352,4.395553,-9.941809,3.899643,-6.485694,8.935529,2.603226,-3.073789,-6.054862,-8.788028,9.406102,8.574205,-7.982148,5.563023,-2.513146,1.653882,9.392241,6.306660,5.846450,-6.429850,4.280626,-2.088394,-2.783934,4.080242,8.307019,-3.780394,-2.221188,1.426604,-0.422106,3.557068,8.404032,-3.435142,2.447486,8.604410,-6.837978,8.519553,6.296657,-8.652127,-4.961814,-1.506308,7.536952,-9.630311,-8.416593,-6.886364,-2.687680,5.203013,7.184890,-4.909517,9.811194,5.505812,-8.189911,-5.158494,-4.501504,1.774355,-8.507146,4.525640,-0.429525,3.602303,0.996697,4.842870,4.350999,-1.462827,-8.888735,-0.763901,-2.117823,1.017813,-4.367411,-7.072234,-2.379033,1.713100,8.634351,4.925270,-0.700390,-8.103076,-0.344920,4.435573,-2.875467,-9.996182,-9.483441,3.931590,5.865126,4.741306,-3.746590,-5.039322,0.374289,0.474720,-2.971404,2.000621,2.876613,5.812381,4.539143,4.627429,-7.932800,5.002079,-9.245703,0.807723,2.382631,1.842084,-4.854425,5.488580,8.540397,-0.784085,5.286273,-0.413163,3.579308,-4.513257,-9.316423,-2.617327,-2.533284,-2.942900,-2.322971,-7.880732,-0.310921,3.284461,4.124661,1.788331,6.960422,4.129307,5.047152,9.660752,6.471223,3.472538,-3.813592,-9.823119,2.758997,8.203877,-6.831074,-1.408739,-7.073612,1.028028,-3.993037,-2.904281,-6.457459,-6.073386,-8.913470,-2.090821,8.962338,2.046378,2.541899,-9.285638,-6.264717,0.726013,8.233971,-5.376301,8.231286,-2.695013,-8.445140,-5.131670,-2.482628,-9.463877,-6.923487,-9.067950,-3.397910,2.139589,5.406616,8.676678,-3.542996,-8.267291,-0.617281,5.896853,-1.963976,1.362313,-0.306104,6.355440,-8.478004,2.093094,-7.982035,-1.073043,-5.607013,-0.246908,-8.263879,9.023385,-1.076989,-9.425210,-4.213148,1.895787,8.163564,1.061650,-3.484721,-1.976378,-6.882369,3.975341,1.253649,-4.281517,-5.766442,8.714562,-3.250737,2.525575,-3.187575,3.541703,5.307758,5.863100,3.366756,-0.546305,9.236959,-5.696832,1.185728,-8.102043,4.784220,-3.867241,-9.734546,-2.820321,-5.391753,3.317721,-4.202330,-0.525231,1.933237,-0.318666,-5.670054,-7.058608,-0.718845,-2.566304,6.383575,-0.843585,2.411603,-1.653055,9.164076,-9.441007,-4.366400,-2.213674,-3.854130,-0.200828,9.509520,-7.560192,2.667449,9.913374,7.675744,2.242745,7.073631,5.300120,-7.676818,-1.687945,1.334071,-9.816548,-2.756983,-1.533922,0.168169,0.870718,1.702498,-4.517236,-3.778628,-6.352828,8.221053,-8.802167,-8.148159,3.854164,9.213734,-9.960000,-4.671407,-8.845376,8.431985,5.084307,7.066705,2.945523,-7.008283,-4.060707,-9.453683,-5.303527,-3.368251,-7.517671,1.227342,-1.036946,8.440732,6.799239,9.064452,-5.338967,-5.706211,3.766068,-7.644986,-6.179155,-7.287035,-6.523232,-2.376280,7.131592,2.403031,7.833245],[2.600254,-0.940390,-5.636428,4.095018,9.238216,-7.624419,3.455468,-6.144106,8.464747,6.325647,2.312247,-9.405320,-7.536333,-0.789622,8.231711,-4.937203,0.228039,7.436006,-3.781544,2.429410,-8.184381,2.013664,2.283843,-4.449007,8.938735,5.759494,8.809242,-8.963571,0.855934,1.481067,-2.457460,9.391029,-0.212359,9.078098,4.686130,2.876816,-2.398333,-7.286705,-3.607836,-6.574269,-9.496910,-5.029817,3.686870,0.039736,1.236583,9.797551,2.452031,-8.616233,3.333984,-2.399563,-4.497163,8.159735,5.861077,0.294546,-5.097973,5.142076,4.828007,-0.420646,-6.558661,6.971466,-4.204598,3.826669,3.792657,-8.543440,7.443980,-4.243413,-5.711179,-3.809415,2.335343,8.560598,-4.824693,-3.917285,-3.221403,-7.929120,-0.358493,-5.956152,6.097328,-9.888028,0.419299,7.861102,-9.886628,9.554558,2.888519,-8.882143,0.713943,-3.749511,-5.087402,8.526060,6.521408,6.077411,4.211031,3.095252,4.031480,2.431736,-9.939519,7.354852,-9.561415,5.718336,-3.324101,-2.478821,8.503067,1.297589,9.433517,-5.210488,5.568702,5.263087,1.974627,9.129372,-8.732907,-8.764417,3.988732,1.500036,-2.666932,-7.739496,-4.485861,-5.971918,9.326338,5.651853,-5.139995,-3.556587,4.886657,-7.012262,-1.970977,0.482694,-0.189415,1.639330,3.470874,-9.489648,7.821638,4.150742,0.588983,3.574860,3.617120,-7.202316,-0.739098,9.024549,-7.648707,-9.022604,6.786082,2.793875,4.039295,-6.257003,-6.491230,-0.749596,1.250784,1.745975,3.062641,6.221797,-0.802569,-9.643677,-9.201166,-8.834547,9.210057,6.916706,8.417991,5.795507,5.265470,5.420488,-7.355793,4.425538,4.735047,-7.134303,8.195263,-1.880500,9.574187,-0.627939,-6.385666,-1.648690,-3.519724,4.967832,8.040154,-6.314862,-9.972733,-9.739682,-3.946695,-1.649951,-3.376829,-9.445027,-2.043083,8.362601,-7.303432,-9.833706,3.511218,-1.009870,-8.807152,4.728560,-9.139258,9.959988,9.852512,2.159578,9.792211,-2.960020,5.800423,-1.453889,5.013857,1.728169,9.347908,-1.733941,2.991526,-6.812950,-2.167237,1.501105,-3.533652,9.372646,-6.457709,4.124717,-2.092322,9.970300,-4.736551,-6.144375,-6.388980,4.671324,1.705788,-9.729918,1.130985,-9.760851,-5.906448,-0.111501,-2.732360,-0.995198,7.584937,6.014150,4.291156,8.758012,-7.533307,7.610531,8.591329,-4.436153,6.510450,5.669935,-7.851827,-0.939682,0.360377,6.281670,4.905471,-5.490557,7.830035,-6.146667,4.367224,-6.703342,0.408985,-7.863842,1.155222,7.035989,5.068088,9.026767,8.806857,-3.050118,-5.342660,-5.133573,1.231739,-2.652564,-0.793372,-1.422587,-1.882418,4.902799,-5.065535,4.889407,0.020458,-3.574313,5.087641,-2.274977,-5.713511,-5.189606,-5.524795,-8.210828,4.904253,-4.362646,8.751318,3.272565,3.188327,-8.364116,-0.754863,7.596909,-5.508241,-6.017664,1.135443,-3.645679,0.490631,2.362212,-0.635000,-4.143551,-4.165559,4.181233,8.627043,-8.510656,-7.519789,-1.525460,-2.774028,-2.472582,-2.346701,-4.315357,8.392397,4.204768,8.155552,-5.866104,-7.778242,-2.083220,4.283879,-4.328093,-1.727265,9.498735,2.338153,-9.786115,-2.926416,4.320575,4.946883,-5.411553,-6.667798,-1.587355,-4.645722,5.428295,9.491731,-0.089820,-4.787036,7.156804,9.913880,3.880380,-9.771432,-4.681760,-4.528141,0.453337,0.817508,-1.324851,0.960796,-9.640406,6.071380,-7.642480,0.758627,1.477661,-4.532311,-1.112113,4.813657,-0.311443,9.069037,-1.084122],[-7.240565,-2.825090,-9.258946,-8.722682,1.142233,4.637255,-8.555479,0.382751,-1.374239,9.269092,8.939251,-2.719167,0.303979,-4.537650,6.384430,-8.850571,8.026325,-2.316521,0.597320,3.920570,8.749258,0.890555,7.223069,1.355479,7.592904,-5.134132,-0.142748,-4.824709,0.218189,5.183546,5.695220,5.398028,-2.647179,-3.488397,-5.650893,-8.077105,2.524841,0.796518,-7.026070,-0.716812,-5.926216,-9.877349,-0.403866,-5.789643,4.676241,-7.100419,-6.590533,2.264069,9.953528,-6.225414,-2.614163,8.290397,4.223341,-4.608833,6.237221,9.893294,6.286415,2.083629,-3.324101,4.805482,8.968570,7.731907,4.419053,-8.399447,-8.746182,-9.711812,2.850124,-8.949437,8.937248,-1.114534,-5.571605,-4.357189,6.148435,7.348137,2.636151,4.511202,-9.526010,-3.701519,-1.423596,0.433360,-5.208341,0.848449,0.616233,-3.305162,-7.158299,-5.450923,-3.643117,-0.987427,-9.532612,-0.041875,-4.654540,-0.551729,-0.548295,6.668785,2.170876,0.504256,-4.623948,9.698251,2.542369,-4.427085,-5.052844,-5.759636,9.193117,-0.303934,-3.813187,-5.246567,-6.772989,5.295633,8.854219,0.811652,9.426043,-4.560659,5.016080,-5.094421,9.877585,-5.415985,6.232494,4.405455,5.950869,-1.127285,-8.019663,2.548739,1.511568,9.801564,9.027952,2.845406,8.506391,-7.444102,1.310458,3.173684,-2.626614,-7.248721,-4.471931,-1.411170,8.154481,7.324167,1.555644,-8.564596,-6.482490,-7.330219,9.526609,-0.902403,9.503734,8.731051,0.481185,-0.066717,8.143862,4.219127,-2.195786,0.395839,-6.243531,5.785182,5.418325,-1.435492,9.680813,5.785987,-9.426104,4.562453,6.079685,-3.797373,-9.539158,-5.759434,4.808681,3.726892,1.505855,9.721116,-4.925230,-2.455086,6.529628,9.030307,6.459411,8.050293,-5.787414,2.257982,9.286013,2.586838,-6.588188,1.037329,7.797659,0.875046,-3.966805,2.824491,7.461143,-1.691794,-9.148556,5.667622,3.157645,-7.098217,-0.574571,4.806433,7.565936,4.603960,-8.799836,-9.791693,7.022087,-9.215363,-0.596829,-3.093971,2.009037,-3.392795,-7.565591,7.111824,-2.368460,-4.221904,-0.134552,9.310698,-6.610439,7.852903,2.791060,-2.156702,-3.994057,-7.327849,-2.041564,-9.748246,-7.674044,-8.161780,3.462198,-1.434386,4.182731,-1.929832,-2.939947,6.053840,-3.711107,3.846554,-0.391653,-0.313662,-3.220647,-9.723760,-3.507356,7.263734,9.125241,4.418663,0.396436,2.077325,-7.252698,-3.416799,4.354340,9.492036,8.999579,5.987285,1.758198,-5.390733,0.292182,-1.243364,6.553357,-6.247602,9.166611,3.765029,5.583323,4.158630,-1.219076,-7.549600,-2.525529,8.988042,-2.779327,0.500702,9.588378,7.321660,-5.203861,-3.928008,3.546243,5.785222,-3.727654,-7.046369,6.771541,-5.357970,8.384465,7.131954,-7.983884,4.406597,2.687274,-0.659390,-5.601182,5.969434,-3.462107,5.728596,-7.668115,-4.133849,8.440541,-6.786960,4.248247,8.613415,5.800139,-1.622521,7.880113,-5.717759,-6.679367,4.647309,4.026890,-1.313201,-3.000638,3.675933,-7.885926,-8.188082,-2.394238,-2.919364,4.936741,8.319504,-5.948294,-9.568908,0.499939,-5.796986,-5.996304,0.039719,4.689856,0.409435,2.672685,-5.881418,-5.431266,7.359065,-9.315288,-0.119920,5.102173,-4.488419,9.956793,-4.184687,-7.104402,0.147349,-2.352910,-5.624758,-7.565005,-7.493565,-0.586051,5.575396,9.887151,-4.681132,-5.774596,3.531134,-0.261559,7.303082,-3.015477,-1.841027,-0.005067,2.610580,-2.611551,-0.168704]], dtype = "float32")#candidate|3921|(7, 336)|const|float32
bop_3922 = relay.right_shift(const_3906.astype('int32'), const_3921.astype('int32')) # shape=(7, 336)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_3930 = func_2943_call()
call_3931 = func_2943_call()
bop_3937 = relay.logical_xor(const_3906.astype('uint32'), const_3921.astype('uint32')) # shape=(7, 336)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_3954 = relay.TupleGetItem(func_3862_call(), 0)
call_3955 = relay.TupleGetItem(func_3863_call(), 0)
output = relay.Tuple([call_3903,call_3905,const_3907,call_3909,bop_3922,call_3930,bop_3937,call_3954,])
output2 = relay.Tuple([call_3904,call_3908,const_3907,call_3910,bop_3922,call_3931,bop_3937,call_3955,])
func_3957 = relay.Function([], output)
mod['func_3957'] = func_3957
mod = relay.transform.InferType()(mod)
output = func_3957()
func_3958 = relay.Function([], output)
mutated_mod['func_3958'] = func_3958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3419_call = mutated_mod.get_global_var('func_3419')
call_3986 = func_3418_call()
call_3987 = func_3418_call()
func_3668_call = mod.get_global_var('func_3668')
func_3671_call = mutated_mod.get_global_var('func_3671')
var_3989 = relay.var("var_3989", dtype = "uint64", shape = (120,))#candidate|3989|(120,)|var|uint64
call_3988 = relay.TupleGetItem(func_3668_call(relay.reshape(call_3986.astype('bool'), [11, 11, 8]), relay.reshape(var_3989.astype('uint64'), [120,]), ), 5)
call_3990 = relay.TupleGetItem(func_3671_call(relay.reshape(call_3986.astype('bool'), [11, 11, 8]), relay.reshape(var_3989.astype('uint64'), [120,]), ), 5)
output = relay.Tuple([call_3986,call_3988,var_3989,])
output2 = relay.Tuple([call_3987,call_3990,var_3989,])
func_3991 = relay.Function([var_3989,], output)
mod['func_3991'] = func_3991
mod = relay.transform.InferType()(mod)
mutated_mod['func_3991'] = func_3991
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3992 = relay.var("var_3992", dtype = "uint64", shape = (120,))#candidate|3992|(120,)|var|uint64
func_3991_call = mutated_mod.get_global_var('func_3991')
call_3993 = func_3991_call(var_3992)
output = call_3993
func_3994 = relay.Function([var_3992], output)
mutated_mod['func_3994'] = func_3994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3957_call = mod.get_global_var('func_3957')
func_3958_call = mutated_mod.get_global_var('func_3958')
call_3996 = relay.TupleGetItem(func_3957_call(), 0)
call_3997 = relay.TupleGetItem(func_3958_call(), 0)
func_3703_call = mod.get_global_var('func_3703')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_4002 = relay.var("var_4002", dtype = "float64", shape = ())#candidate|4002|()|var|float64
const_4003 = relay.const([[-8.091732,8.919333,2.697457,4.279315,1.647322,6.035197],[0.614574,-5.088803,-2.360744,7.154822,-7.666449,9.758690],[-9.866496,-2.903777,0.595713,7.291435,-8.016498,-6.052671],[-4.643820,4.893865,9.355602,5.304866,8.675563,-8.323824],[-8.786310,4.281226,-5.311448,-4.807565,4.727262,-1.740962],[1.742612,-1.751892,-7.704504,5.051908,0.416235,5.082517],[0.539794,8.615825,-0.605980,0.347821,2.808472,7.292104],[6.989769,-6.213006,-5.966223,4.460501,2.367802,6.293864],[-5.588519,-5.103054,9.235641,-3.756719,-4.493106,0.059948]], dtype = "float64")#candidate|4003|(9, 6)|const|float64
call_4001 = func_3703_call(relay.reshape(var_4002.astype('float64'), []), relay.reshape(const_4003.astype('float64'), [3, 6, 3]), )
call_4004 = func_3703_call(relay.reshape(var_4002.astype('float64'), []), relay.reshape(const_4003.astype('float64'), [3, 6, 3]), )
output = relay.Tuple([call_3996,call_4001,var_4002,const_4003,])
output2 = relay.Tuple([call_3997,call_4004,var_4002,const_4003,])
func_4008 = relay.Function([var_4002,], output)
mod['func_4008'] = func_4008
mod = relay.transform.InferType()(mod)
mutated_mod['func_4008'] = func_4008
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4009 = relay.var("var_4009", dtype = "float64", shape = ())#candidate|4009|()|var|float64
func_4008_call = mutated_mod.get_global_var('func_4008')
call_4010 = func_4008_call(var_4009)
output = call_4010
func_4011 = relay.Function([var_4009], output)
mutated_mod['func_4011'] = func_4011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4024 = func_3507_call()
call_4025 = func_3507_call()
output = call_4024
output2 = call_4025
func_4030 = relay.Function([], output)
mod['func_4030'] = func_4030
mod = relay.transform.InferType()(mod)
output = func_4030()
func_4031 = relay.Function([], output)
mutated_mod['func_4031'] = func_4031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3428_call = mod.get_global_var('func_3428')
func_3429_call = mutated_mod.get_global_var('func_3429')
call_4034 = func_3428_call()
call_4035 = func_3428_call()
func_479_call = mod.get_global_var('func_479')
func_482_call = mutated_mod.get_global_var('func_482')
var_4040 = relay.var("var_4040", dtype = "int16", shape = (1456,))#candidate|4040|(1456,)|var|int16
call_4039 = func_479_call(relay.reshape(var_4040.astype('int16'), [8, 14, 13]))
call_4041 = func_479_call(relay.reshape(var_4040.astype('int16'), [8, 14, 13]))
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
const_4043 = relay.const([[-4.322504,-7.421353,0.941385,8.324253,2.360522,-9.211134,6.925310,-3.889269,-5.769165,8.698494,1.622680,-6.023974,8.835417,1.035878,-3.140433,-3.600124,-8.467828,8.940947,-8.770972,-2.099900,-4.695536,7.279013,-2.653415,0.697429,2.605327,-9.744697,-8.523562,-9.135495,-0.631406,6.797043,0.448167,-4.307635,-8.005861,0.031395,-9.930199,0.916185,-0.777120,-9.562486,-2.548013,2.087142,-4.305632,-2.193564,0.987573,1.332897,-1.596264,-9.894946,-6.141696,-6.371942,-2.905509,-5.190642,9.049604,4.073095,-3.241144,-5.798266,-9.913978,-3.301379,6.515431,9.306758,0.745500,-5.221871,-2.241451,0.462283,1.425289,3.137717,-4.721476,2.562675,0.513189,2.548393,-4.009465,-0.041435,-5.799983,-4.396691,-3.340441,-6.401823,-6.263292,3.989163,3.500622,1.673743,-7.468170,-5.336834,-7.470614,-2.458627,-1.399764,7.919524,6.154437,7.279414,-9.865050,5.603762,-8.568996,-6.179434,4.571697,9.806368,9.061279,2.201586,0.433584,-9.609822,1.956597,-6.030917,-2.490901,9.031803,2.021332,4.864158,-0.263004,-2.155196,-8.087776,8.580746,1.568850,-6.217106,0.979802,-8.754237,3.077169,4.206634,-4.851123,5.932605,5.889674,-1.681666,5.528571,6.101092,9.353167,-6.437643,-0.430997,5.151315,-5.899700,-1.655290,4.350434,7.374737,9.884539,-2.053879,-6.808609,6.542963,-5.019011,-6.638468,5.091817,4.231945,-2.351550,1.329961,6.859263,-2.994900,-8.499636,4.855873,7.300772,7.280049,2.077454,-6.334046,0.646910,-5.723169,-1.515254,3.996441,-2.863607,-1.209389,5.834813,2.393124,-0.043151,-3.344715,3.904596,-3.995788,-0.535143,6.292012,8.629523,8.891040,3.725998,-5.324152,0.938415,-1.125347,-9.936647,-2.395613,-8.278335,-3.794877],[5.132315,3.402485,5.165705,8.405521,7.339397,6.259451,6.349125,0.587105,-0.671591,-9.609817,-3.087020,6.960207,0.395656,-7.464181,-0.456312,-7.734594,4.702536,-7.182615,6.454252,0.856486,-7.489758,-7.829799,8.918939,0.783873,5.241637,3.757430,-7.204309,8.157819,-1.899792,3.859621,-2.539533,-2.139945,3.809784,-7.554139,8.908599,-1.416848,3.505275,2.440579,-3.004765,-6.869494,-0.162553,8.063926,7.734165,-0.336311,-7.326587,-8.286290,4.501942,2.675636,2.560820,7.183496,2.588850,-3.907039,-4.282311,6.956096,-1.871302,3.920066,-0.057210,6.507854,4.271714,9.417381,8.432947,-2.495921,1.235517,-7.298401,-2.397889,9.292380,6.661759,-8.809837,3.661481,-8.549497,4.547693,-6.644647,1.929996,5.288447,2.349485,-4.982784,-7.483174,0.732694,-8.461555,-2.136342,7.795924,-8.872666,-2.223864,9.633733,5.012164,5.237277,2.863684,-8.089583,-7.542547,7.327694,-4.051412,-8.290898,-8.500831,-4.877020,9.465785,0.842633,-3.159457,7.946315,-2.616308,-2.919411,0.792691,1.793247,2.389339,9.300118,0.806143,9.953417,-2.439318,9.762842,8.967919,-5.687964,-8.513728,-1.987886,8.350178,6.657485,-7.622806,3.497303,-8.659835,-2.484086,-0.018432,9.105549,-1.397299,-2.014942,-8.962743,8.283890,7.356577,2.920008,-3.477166,7.716589,4.868920,6.741339,-7.793147,9.022587,9.050688,3.637670,4.369576,-0.623480,3.596943,9.062268,-6.562732,-8.198069,-9.024052,3.916711,2.528762,-4.226036,-0.264435,-3.355497,9.448365,8.138852,0.077385,-8.499172,6.047895,-9.408688,7.000063,-0.084519,-5.858081,-7.454503,-8.964234,4.960685,-1.247906,8.065504,-0.166789,9.549525,5.789861,-0.733888,0.750585,-3.050586,8.562043,-4.520825]], dtype = "float32")#candidate|4043|(2, 168)|const|float32
var_4044 = relay.var("var_4044", dtype = "uint64", shape = (120,))#candidate|4044|(120,)|var|uint64
call_4042 = relay.TupleGetItem(func_777_call(relay.reshape(const_4043.astype('float32'), [6, 7, 8]), relay.reshape(const_4043.astype('float32'), [6, 7, 8]), relay.reshape(var_4044.astype('uint64'), [120,]), ), 3)
call_4045 = relay.TupleGetItem(func_781_call(relay.reshape(const_4043.astype('float32'), [6, 7, 8]), relay.reshape(const_4043.astype('float32'), [6, 7, 8]), relay.reshape(var_4044.astype('uint64'), [120,]), ), 3)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_4052 = relay.TupleGetItem(func_3025_call(), 0)
call_4053 = relay.TupleGetItem(func_3027_call(), 0)
bop_4061 = relay.right_shift(const_4043.astype('uint16'), relay.reshape(call_4042.astype('uint16'), relay.shape_of(const_4043))) # shape=(2, 168)
bop_4064 = relay.right_shift(const_4043.astype('uint16'), relay.reshape(call_4045.astype('uint16'), relay.shape_of(const_4043))) # shape=(2, 168)
func_3668_call = mod.get_global_var('func_3668')
func_3671_call = mutated_mod.get_global_var('func_3671')
call_4072 = relay.TupleGetItem(func_3668_call(relay.reshape(call_4052.astype('bool'), [11, 11, 8]), relay.reshape(var_4044.astype('uint64'), [120,]), ), 1)
call_4073 = relay.TupleGetItem(func_3671_call(relay.reshape(call_4052.astype('bool'), [11, 11, 8]), relay.reshape(var_4044.astype('uint64'), [120,]), ), 1)
func_3703_call = mod.get_global_var('func_3703')
func_3707_call = mutated_mod.get_global_var('func_3707')
var_4077 = relay.var("var_4077", dtype = "float64", shape = ())#candidate|4077|()|var|float64
const_4078 = relay.const([-4.295387,-5.946889,6.308800,1.910952,8.454360,6.387669,6.502968,-4.894819,-2.633021,3.989818,-8.722339,1.804925,1.615043,7.579421,-6.205366,-6.344471,5.132836,-8.448487,-5.979257,-6.461978,-0.274078,-4.707054,-8.578030,2.560933,-4.873553,9.776120,-8.741980,-7.989651,-0.261269,-3.474615,-3.213422,-0.845238,0.487342,-8.422420,-4.023328,7.376296,-6.574973,-8.977922,2.135367,8.983715,2.171397,-8.620067,9.945235,6.220747,-9.705971,3.902414,-3.157271,-4.805567,-6.760832,5.259489,-5.150391,9.024227,2.534427,8.368243], dtype = "float64")#candidate|4078|(54,)|const|float64
call_4076 = func_3703_call(relay.reshape(var_4077.astype('float64'), []), relay.reshape(const_4078.astype('float64'), [3, 6, 3]), )
call_4079 = func_3703_call(relay.reshape(var_4077.astype('float64'), []), relay.reshape(const_4078.astype('float64'), [3, 6, 3]), )
output = relay.Tuple([call_4034,call_4039,var_4040,var_4044,call_4052,bop_4061,call_4072,call_4076,var_4077,const_4078,])
output2 = relay.Tuple([call_4035,call_4041,var_4040,var_4044,call_4053,bop_4064,call_4073,call_4079,var_4077,const_4078,])
func_4088 = relay.Function([var_4040,var_4044,var_4077,], output)
mod['func_4088'] = func_4088
mod = relay.transform.InferType()(mod)
mutated_mod['func_4088'] = func_4088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4088_call = mutated_mod.get_global_var('func_4088')
var_4090 = relay.var("var_4090", dtype = "int16", shape = (1456,))#candidate|4090|(1456,)|var|int16
var_4091 = relay.var("var_4091", dtype = "uint64", shape = (120,))#candidate|4091|(120,)|var|uint64
var_4092 = relay.var("var_4092", dtype = "float64", shape = ())#candidate|4092|()|var|float64
call_4089 = func_4088_call(var_4090,var_4091,var_4092,)
output = call_4089
func_4093 = relay.Function([var_4090,var_4091,var_4092,], output)
mutated_mod['func_4093'] = func_4093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3957_call = mod.get_global_var('func_3957')
func_3958_call = mutated_mod.get_global_var('func_3958')
call_4125 = relay.TupleGetItem(func_3957_call(), 0)
call_4126 = relay.TupleGetItem(func_3958_call(), 0)
uop_4137 = relay.log10(call_4125.astype('float64')) # shape=(11, 11, 8)
uop_4139 = relay.log10(call_4126.astype('float64')) # shape=(11, 11, 8)
uop_4141 = relay.log2(call_4125.astype('float64')) # shape=(11, 11, 8)
uop_4143 = relay.log2(call_4126.astype('float64')) # shape=(11, 11, 8)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_4153 = relay.TupleGetItem(func_3244_call(), 1)
call_4154 = relay.TupleGetItem(func_3246_call(), 1)
output = relay.Tuple([uop_4137,uop_4141,call_4153,])
output2 = relay.Tuple([uop_4139,uop_4143,call_4154,])
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
call_4195 = relay.TupleGetItem(func_4167_call(), 1)
call_4196 = relay.TupleGetItem(func_4169_call(), 1)
output = relay.Tuple([call_4195,])
output2 = relay.Tuple([call_4196,])
func_4210 = relay.Function([], output)
mod['func_4210'] = func_4210
mod = relay.transform.InferType()(mod)
output = func_4210()
func_4211 = relay.Function([], output)
mutated_mod['func_4211'] = func_4211
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4284 = relay.var("var_4284", dtype = "float64", shape = (1, 15, 16))#candidate|4284|(1, 15, 16)|var|float64
uop_4285 = relay.sqrt(var_4284.astype('float64')) # shape=(1, 15, 16)
output = relay.Tuple([uop_4285,])
output2 = relay.Tuple([uop_4285,])
func_4295 = relay.Function([var_4284,], output)
mod['func_4295'] = func_4295
mod = relay.transform.InferType()(mod)
var_4296 = relay.var("var_4296", dtype = "float64", shape = (1, 15, 16))#candidate|4296|(1, 15, 16)|var|float64
output = func_4295(var_4296)
func_4297 = relay.Function([var_4296], output)
mutated_mod['func_4297'] = func_4297
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_4331 = func_3064_call()
call_4332 = func_3064_call()
func_3428_call = mod.get_global_var('func_3428')
func_3429_call = mutated_mod.get_global_var('func_3429')
call_4344 = func_3428_call()
call_4345 = func_3428_call()
func_4210_call = mod.get_global_var('func_4210')
func_4211_call = mutated_mod.get_global_var('func_4211')
call_4348 = relay.TupleGetItem(func_4210_call(), 0)
call_4349 = relay.TupleGetItem(func_4211_call(), 0)
func_3703_call = mod.get_global_var('func_3703')
func_3707_call = mutated_mod.get_global_var('func_3707')
const_4365 = relay.const(9.341354, dtype = "float64")#candidate|4365|()|const|float64
const_4366 = relay.const([[3.679053,1.710231],[-3.112514,6.751511],[-9.653813,5.128598],[6.874489,5.428885],[8.247240,-8.535922],[6.470577,4.834223],[1.000336,-1.083336],[0.722565,4.018969],[-5.580207,7.085440],[0.619581,5.636598],[-5.113166,-1.498606],[-8.060019,9.630414],[-5.561019,-3.907212],[9.086886,-6.939666],[2.302363,9.111327],[-7.205774,0.404703],[7.564690,-6.347437],[7.115511,-9.840969],[-3.816146,9.783401],[-8.521078,6.013846],[8.388204,9.625913],[7.795899,1.733657],[-1.641067,1.044165],[-0.142677,0.521535],[9.347017,-7.252559],[-5.574562,1.805061],[2.865221,7.236046]], dtype = "float64")#candidate|4366|(27, 2)|const|float64
call_4364 = func_3703_call(relay.reshape(const_4365.astype('float64'), []), relay.reshape(const_4366.astype('float64'), [3, 6, 3]), )
call_4367 = func_3703_call(relay.reshape(const_4365.astype('float64'), []), relay.reshape(const_4366.astype('float64'), [3, 6, 3]), )
func_1152_call = mod.get_global_var('func_1152')
func_1154_call = mutated_mod.get_global_var('func_1154')
var_4369 = relay.var("var_4369", dtype = "float64", shape = (4,))#candidate|4369|(4,)|var|float64
call_4368 = func_1152_call(relay.reshape(var_4369.astype('float64'), [4, 1, 1]))
call_4370 = func_1152_call(relay.reshape(var_4369.astype('float64'), [4, 1, 1]))
func_4088_call = mod.get_global_var('func_4088')
func_4093_call = mutated_mod.get_global_var('func_4093')
const_4380 = relay.const([-3,-10,-8,-2,-4,-5,2,-3,9,4,2,-10,4,-2,-6,2,-9,-4,5,-4,-1,-1,7,7,-8,3,-4,6,6,-3,-2,2,1,8,4,-6,1,9,3,-3,-6,9,-9,8,-5,-8,7,-8,-5,-6,-8,-3,2,-8,7,-6,-8,-5,-1,4,3,3,-1,-10,-7,5,-1,-6,-2,7,-6,6,-9,-2,-1,6,-10,8,8,-10,-6,-10,-5,1,-1,-9,-3,-2,6,-3,-2,-3,-8,8,8,-2,-2,3,-9,5,3,6,10,8,-1,3,10,8,8,3,-3,-2,7,10,-10,-5,-2,-10,-8,8,-7,-3,-8,4,-8,-4,4,-3,5,-7,2,-9,3,-7,-6,-10,-6,2,5,-2,5,-3,-5,-1,4,5,-2,-10,-4,7,2,6,2,3,-4,-2,2,9,4,8,-8,3,7,-4,-10,2,-8,-9,-6,10,9,10,-7,-9,-9,-8,9,-6,5,-7,2,-9,2,3,-2,10,4,3,1,2,-6,-8,2,-1,-7,-1,2,3,10,1,-8,-1,3,6,5,-7,-8,8,-10,-4,9,-9,-7,-4,6,-9,6,-1,-4,-4,-2,-2,5,-10,-8,5,-2,-8,-5,-6,-8,9,6,5,-4,-9,-10,-9,-10,4,-3,-7,1,6,10,1,8,1,8,2,-5,-10,-3,-1,-8,-2,4,-6,5,-3,3,-2,-3,-4,9,5,-8,-10,-6,7,6,6,9,4,-3,10,10,8,-6,-4,-8,-2,8,1,-3,-9,-8,-10,7,2,1,-6,7,-6,-6,-10,3,-3,4,-4,-10,7,-10,-4,10,-4,1,4,8,1,-2,8,-4,6,-5,-6,-5,-3,-9,9,7,4,7,-6,-10,9,-1,-9,10,-3,-6,-9,2,-6,-1,2,-2,5,-4,4,-1,8,-2,7,10,6,-6,9,-9,9,-1,9,9,3,-9,9,-2,4,-2,7,-10,10,-9,6,-3,7,7,-7,10,-2,-1,-8,6,8,-2,3,-7,10,3,4,-2,-2,-7,-7,-1,7,-10,4,9,-5,6,-5,-1,8,2,10,5,4,2,-10,-10,6,5,5,1,-7,8,-1,6,2,3,1,-5,9,-8,-10,-7,-10,6,6,-5,-6,4,3,9,9,9,-10,-7,-2,10,-3,2,-1,9,8,2,-9,3,8,7,-6,5,3,-6,7,10,-5,3,1,-5,6,-2,6,4,9,-9,-2,-2,-8,-1,-6,-3,3,9,8,4,-3,-6,4,-1,5,-8,4,-1,8,-5,5,5,6,4,8,-7,-4,10,-4,1,-10,-6,10,-7,1,3,4,4,2,3,7,10,2,9,10,-3,10,-3,7,9,3,-4,9,-6,-7,10,-8,5,-10,-6,-6,-9,8,-7,3,5,-7,5,-8,-5,-2,10,5,10,2,4,-4,-4,-8,-1,6,-8,-4,9,6,8,-8,5,-6,9,-10,-5,7,-7,2,-5,-4,3,8,2,5,9,10,5,1,-3,-6,-5,8,7,10,8,6,3,-1,-5,9,-10,-10,-7,10,1,-6,10,-8,4,10,1,-3,-2,-1,1,-3,-1,7,-3,5,4,10,-7,-2,4,3,1,-2,-10,-10,-5,3,5,3,8,1,1,-7,-10,1,4,1,-10,6,8,-1,8,-10,-8,10,2,10,-5,-6,-8,8,1,-5,2,8,-7,4,7,-8,-8,-10,10,-8,7,-9,-10,-6,6,-9,5,8,-8,-7,8,-9,4,9,-1,10,-10,2,-5,1,2,-10,7,8,4,-2,3,-9,3,2,6,2,10,-7,6,8,6,-4,-8,2,-10,-4,-8,-1,-4,6,2,5,-6,6,-10,8,2,3,-6,4,9,-10,-3,-1,3,-7,7,-6,-6,-3,-9,-4,-4,-5,-10,-8,-6,-10,-1,-8,-8,1,10,-6,-2,-3,-1,5,4,8,8,-6,6,7,-5,-4,-3,8,-2,10,-3,-6,1,-2,3,10,-5,8,-2,-9,-2,-2,5,6,4,1,10,6,1,8,-5,5,-5,-1,8,6,2,2,-7,7,6,-3,-7,8,4,-4,-6,-10,4,10,3,1,-3,5,5,5,9,-8,6,6,3,2,-9,-10,6,-4,-5,4,-9,-2,-10,6,5,-6,1,3,-2,-3,9,-5,-5,-4,5,10,7,-10,9,6,9,6,-6,6,-6,-10,-6,10,5,2,1,3,4,-5,-9,-8,7,-10,5,-2,9,-7,-8,-4,10,2,-10,9,8,8,7,8,1,8,6,-8,3,-9,2,-3,-1,-4,-1,4,7,9,-9,-7,-6,4,-6,-6,8,9,1,2,6,-3,-7,6,-1,7,3,10,-10,1,7,-2,-5,4,-2,7,2,-6,-1,2,-9,-3,2,2,-8,-5,-4,-1,-7,-6,3,8,-5,6,-9,7,-7,10,2,1,-9,-6,-5,-2,3,-5,3,-2,8,-4,6,4,-2,3,10,-5,-2,2,7,2,-3,-6,10,3,-6,4,-10,5,7,-7,2,6,4,-1,-3,1,-10,10,-5,-8,2,4,2,-4,-9,-8,5,-5,3,8,-1,-1,5,8,6,2,-10,2,8,-3,-6,-8,-6,-10,2,-6,-8,-1,8,-5,-7,-4,3,-9,1,6,4,10,8,10,9,-3,2,-2,-7,-7,-3,-1,5,5,-3,-3,6,8,5,-6,-5,3,-2,8,-3,-4,-5,3,7,6,-1,-9,-4,3,-7,6,-5,-9,-6,-8,3,-7,7,8,10,-5,5,-9,3,10,8,-1,-7,-2,9,-3,-2,-3,-4,4,-5,6,3,8,-5,5,4,-8,6,3,-10,2,-1,-10,5,9,-10,-9,10,8,-8,1,-9,-3,9,-4,4,-10,10,10,-3,-5,-3,10,4,1,3,3,2,-8,-4,1,-10,-3,-2,-6,-3,2,7,-1,1,2,5,5,3,-10,6,3,4,-8,10,-5,-7,8,8,9,-3,-1,-8,10,10,6,-3,3,6,6,-5,10,-6,10,-10,-5,-9,3,-3,-9,-3,10,-6,3,-4,10,10,3,-8,1,-1,-3,3,8,-9,10,1,-9,-2,-9,-1,-8,-10,-8,4,-8,-6,-7,-7,4,1,-9,3,-9,10,1,-10,-6,-2,1,-4,2,2,-6,4,6,-5,10,-2,-2,9,-8,4,1,8,3,5,-9,-7,-5,-6,-6,7,-8,-7,3,-6,6,7,-8,-1,5,8,-2,-1,-6,9,10,10,-7,10,2,3,8,7,-4,-8,-4,-3,3,-5,-10,3,-2,-10,7,-9,8,8,1,-3,-4,4,-9,-6,10,1,8,2,6,-1,3,-3,1,6,-7,-8,10,-8,-8,3,-8,10,10,-7,5,1,-7,9,-8,-3,4,3,-1,6,5,-7,-6,8,8,-6,5,-3,4,2,8,6,-7,7,1,-7,-5,-1,1,10,-7,4,-4,6,-8,-1,-6,-8,7,8,1,6,10,-8,7,10,-2,7,9,7,4,2,6,-10,5,3,-5,-1,-6,-6,5,-6,10,7,7,-7,-2,10,10,3,1,-3,-4,-3,-5,3,7,-1,3,6,-9,-2,5,1,5,5,1,-2,4,7,-6,-3,10,-10,9,-4,1,3,9,3,9,9,6,7,7,-1,-6,6,8,8,3,8,-1,10,-7,3,-1,-8,-4,-8,10,-5,-6,10,-8,1,-4,3,-4,-5,-10,-6,3,-9,-8,-9,8,3,-7,-10,-5,4,2,5,4,6,10,-4,-4,7,10,10,-2,-4,8,-1,4,2,-5,-1,-9,-1,-9,-10,-8,4,-5,-5,-7,-5,10,-8,1,10,9,5,10,-6,2,9,7,9,-8,-10,-3,10,8,10,9,5,3,7,7,2,1,9,-7], dtype = "int16")#candidate|4380|(1456,)|const|int16
const_4381 = relay.const([-3,9,-3,1,-6,1,3,5,-8,-1,6,-6,5,7,4,-8,-5,4,6,9,10,-9,-10,1,7,-4,-5,1,6,5,-4,-8,8,8,1,7,-9,-4,-3,6,-9,4,-1,-6,-3,-6,2,9,-7,-5,4,10,10,-4,-9,4,3,1,-3,10,8,6,-1,1,1,6,7,1,-10,-2,-7,8,-4,-5,-8,6,2,-7,6,3,-3,5,5,-9,10,5,-8,7,-3,-1,-7,8,-9,-4,-2,-2,-6,-7,2,-5,9,-2,-6,-3,1,-2,8,-10,7,-4,1,-6,-5,-7,10,9,-3,-10,-10,-7], dtype = "uint64")#candidate|4381|(120,)|const|uint64
call_4379 = relay.TupleGetItem(func_4088_call(relay.reshape(const_4380.astype('int16'), [1456,]), relay.reshape(const_4381.astype('uint64'), [120,]), relay.reshape(const_4365.astype('float64'), []), ), 1)
call_4382 = relay.TupleGetItem(func_4093_call(relay.reshape(const_4380.astype('int16'), [1456,]), relay.reshape(const_4381.astype('uint64'), [120,]), relay.reshape(const_4365.astype('float64'), []), ), 1)
output = relay.Tuple([call_4331,call_4344,call_4348,call_4364,const_4365,const_4366,call_4368,var_4369,call_4379,const_4380,const_4381,])
output2 = relay.Tuple([call_4332,call_4345,call_4349,call_4367,const_4365,const_4366,call_4370,var_4369,call_4382,const_4380,const_4381,])
func_4395 = relay.Function([var_4369,], output)
mod['func_4395'] = func_4395
mod = relay.transform.InferType()(mod)
var_4396 = relay.var("var_4396", dtype = "float64", shape = (4,))#candidate|4396|(4,)|var|float64
output = func_4395(var_4396)
func_4397 = relay.Function([var_4396], output)
mutated_mod['func_4397'] = func_4397
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3428_call = mod.get_global_var('func_3428')
func_3429_call = mutated_mod.get_global_var('func_3429')
call_4405 = func_3428_call()
call_4406 = func_3428_call()
output = call_4405
output2 = call_4406
func_4407 = relay.Function([], output)
mod['func_4407'] = func_4407
mod = relay.transform.InferType()(mod)
mutated_mod['func_4407'] = func_4407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mutated_mod.get_global_var('func_4407')
call_4408 = func_4407_call()
output = call_4408
func_4409 = relay.Function([], output)
mutated_mod['func_4409'] = func_4409
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_4497 = relay.TupleGetItem(func_3025_call(), 0)
call_4498 = relay.TupleGetItem(func_3027_call(), 0)
var_4520 = relay.var("var_4520", dtype = "float32", shape = (11, 11, 8))#candidate|4520|(11, 11, 8)|var|float32
bop_4521 = relay.logical_xor(call_4497.astype('uint32'), relay.reshape(var_4520.astype('uint32'), relay.shape_of(call_4497))) # shape=(11, 11, 8)
bop_4524 = relay.logical_xor(call_4498.astype('uint32'), relay.reshape(var_4520.astype('uint32'), relay.shape_of(call_4498))) # shape=(11, 11, 8)
output = bop_4521
output2 = bop_4524
func_4526 = relay.Function([var_4520,], output)
mod['func_4526'] = func_4526
mod = relay.transform.InferType()(mod)
var_4527 = relay.var("var_4527", dtype = "float32", shape = (11, 11, 8))#candidate|4527|(11, 11, 8)|var|float32
output = func_4526(var_4527)
func_4528 = relay.Function([var_4527], output)
mutated_mod['func_4528'] = func_4528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_4530 = relay.TupleGetItem(func_3244_call(), 0)
call_4531 = relay.TupleGetItem(func_3246_call(), 0)
output = call_4530
output2 = call_4531
func_4544 = relay.Function([], output)
mod['func_4544'] = func_4544
mod = relay.transform.InferType()(mod)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4544_call = mutated_mod.get_global_var('func_4544')
call_4545 = func_4544_call()
output = call_4545
func_4546 = relay.Function([], output)
mutated_mod['func_4546'] = func_4546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4210_call = mod.get_global_var('func_4210')
func_4211_call = mutated_mod.get_global_var('func_4211')
call_4552 = relay.TupleGetItem(func_4210_call(), 0)
call_4553 = relay.TupleGetItem(func_4211_call(), 0)
output = relay.Tuple([call_4552,])
output2 = relay.Tuple([call_4553,])
func_4565 = relay.Function([], output)
mod['func_4565'] = func_4565
mod = relay.transform.InferType()(mod)
mutated_mod['func_4565'] = func_4565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4565_call = mutated_mod.get_global_var('func_4565')
call_4566 = func_4565_call()
output = call_4566
func_4567 = relay.Function([], output)
mutated_mod['func_4567'] = func_4567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4544_call = mod.get_global_var('func_4544')
func_4546_call = mutated_mod.get_global_var('func_4546')
call_4579 = func_4544_call()
call_4580 = func_4544_call()
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
const_4582 = relay.const([[-5.401583,-5.421190],[-5.669326,-2.311995],[7.372184,-6.132089],[9.700597,7.951094],[1.895315,4.341204],[8.833958,-3.327347],[-6.598174,6.917775],[0.710246,3.102722],[-6.998088,-7.426749],[-4.739247,-4.840449],[9.005165,-1.084525],[1.441394,-3.151128],[7.406780,4.325089],[3.557394,-5.231931],[5.035491,-6.512697],[2.175813,1.313259],[8.876814,0.772845],[-6.331494,-4.209064],[-1.485808,0.879397],[-3.130644,-4.338969],[3.477595,9.279671],[-1.903460,2.670640],[9.702528,-0.750675],[0.347548,1.367312],[4.644884,-4.947305],[-4.158040,9.529191],[-1.996182,-1.527524],[0.554471,-0.815234],[-5.841978,5.144172],[8.309479,3.498100],[0.836821,-0.282808],[2.586187,2.475136],[-7.296558,-0.700496],[-8.472152,6.560282],[-0.452143,-8.574929],[-6.931949,2.771624],[-2.775625,4.460913],[9.894380,-4.320676],[-2.939542,9.237165],[-5.706125,4.416830],[-5.346795,3.968868],[5.434451,3.153150],[-7.628918,8.589660],[0.896706,-4.665569],[-8.298501,7.748767],[-1.086877,-4.709172],[-1.192835,-5.338609],[-7.349187,2.504150],[8.222206,-6.340171],[1.411092,8.944519],[2.708673,2.975583],[7.548958,-3.569253],[2.426048,4.825124],[1.531695,5.207365],[8.547832,1.513928],[7.257645,-3.993233],[8.695900,0.695068],[9.781023,6.872747],[-8.525956,3.442807],[-4.442526,8.278439],[6.468882,6.754521],[-3.558239,4.151785],[-6.440277,0.501976],[4.315322,-6.541166],[-5.995133,-0.409598],[-9.021755,-5.118170],[-2.180951,-8.494457],[0.007067,-9.108430],[-2.084600,-2.921539],[-5.928771,-4.693597],[-6.671195,-4.127925],[-6.339087,-9.485317],[7.356947,-8.059683],[-2.699463,-4.733734],[-6.641514,2.269864],[-7.239716,-4.038954],[1.773162,1.345076],[-0.839343,-7.023863],[6.667668,3.082337],[-0.917669,3.116390],[-8.817127,8.300949],[-0.194507,2.022152],[1.496844,9.462889],[-0.402023,-2.087084],[-0.321512,-5.515846],[-0.163990,8.384410],[0.014241,4.307389],[-9.357442,9.666341],[-2.987526,-5.741089],[-2.640735,2.037529],[-8.074256,6.180300],[-6.320171,9.642933],[3.623177,-0.123830],[-9.513430,-7.568677],[-8.946034,0.322079],[-0.474617,0.398835],[-0.964550,7.420927],[5.851944,-6.339539],[0.773414,-4.716939],[9.355591,-4.695385],[2.918382,-6.695627],[-9.241819,-2.886141],[-4.130351,-1.730943],[-7.107815,3.426058],[0.830572,-2.144760],[2.814283,-0.780290],[-4.016942,5.130955],[-7.666435,6.626511],[-4.064308,-0.573928],[-8.267142,3.061429],[-6.143020,4.222136],[8.768061,5.418089],[4.650572,6.466362],[-4.031623,-2.003085],[-4.312310,3.590218],[8.698568,4.653837],[-9.969036,7.067148],[-4.187604,-9.260609],[-2.703036,5.222845],[-9.674325,-5.347695],[-0.642236,2.460494],[3.766327,-1.328796],[6.591044,0.049991],[-9.175278,-6.533561],[-5.147971,7.516053],[-3.664433,2.938404],[5.254252,-6.608877],[-4.034142,7.979487],[-0.992399,1.326060],[-9.322800,4.490985],[4.569869,0.766974],[4.879254,9.832115],[2.969238,-3.732729],[-1.853589,-9.660601],[3.777470,2.556426],[2.353709,-4.717064],[5.451257,1.573412],[5.274491,9.860905],[4.645079,-5.795654],[-1.012271,-9.654204],[-9.967100,7.054141],[0.957000,-1.780631],[-7.093290,-0.075717],[0.599949,0.282034],[-2.512292,-9.993456],[-1.496970,9.778642],[-1.291418,-8.562330],[3.505992,-9.676951],[-8.615870,-1.327835],[1.721544,-7.210337],[-6.664269,2.231214],[7.461699,4.859309],[-2.353320,-3.474295],[8.955973,-4.096580],[0.243611,8.679769],[-3.667470,4.393144],[1.925165,-3.853418],[-5.955633,3.980232],[9.746202,-7.298576],[6.912268,-8.539477],[-8.711605,-5.821121],[-6.165663,6.349408],[-7.847207,-6.814848],[1.495912,0.609294],[9.589379,5.021397],[-5.846442,0.964556],[-5.961806,-9.121914],[7.501324,0.474144]], dtype = "float32")#candidate|4582|(168, 2)|const|float32
const_4583 = relay.const([[9,-6,10,-2,-3,-4,8,10,-9,3,-7,-3,9,-6,10,-1,-10,7,-4,-7,-2,5,4,-3,8,-1,2,-5,-10,7,7,-8,4,-6,-8,5,-3,3,8,2],[-3,-1,1,-6,-7,8,1,-10,3,3,-9,1,-1,-1,2,6,-8,-10,3,7,-9,3,-3,4,10,-7,-8,-1,5,-9,-5,2,-4,-10,8,-8,-2,-6,-5,-3],[8,4,-10,-6,-6,4,1,-3,-8,-3,-10,-3,3,9,10,5,-2,5,-5,-1,-7,2,-2,-5,10,7,3,2,7,-6,-3,-6,-1,9,3,6,-4,8,-5,-6]], dtype = "uint64")#candidate|4583|(3, 40)|const|uint64
call_4581 = relay.TupleGetItem(func_777_call(relay.reshape(const_4582.astype('float32'), [6, 7, 8]), relay.reshape(const_4582.astype('float32'), [6, 7, 8]), relay.reshape(const_4583.astype('uint64'), [120,]), ), 4)
call_4584 = relay.TupleGetItem(func_781_call(relay.reshape(const_4582.astype('float32'), [6, 7, 8]), relay.reshape(const_4582.astype('float32'), [6, 7, 8]), relay.reshape(const_4583.astype('uint64'), [120,]), ), 4)
output = relay.Tuple([call_4579,call_4581,const_4582,const_4583,])
output2 = relay.Tuple([call_4580,call_4584,const_4582,const_4583,])
func_4593 = relay.Function([], output)
mod['func_4593'] = func_4593
mod = relay.transform.InferType()(mod)
mutated_mod['func_4593'] = func_4593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4593_call = mutated_mod.get_global_var('func_4593')
call_4594 = func_4593_call()
output = call_4594
func_4595 = relay.Function([], output)
mutated_mod['func_4595'] = func_4595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_4624 = func_3507_call()
call_4625 = func_3507_call()
var_4633 = relay.var("var_4633", dtype = "float32", shape = (11, 11, 8))#candidate|4633|(11, 11, 8)|var|float32
bop_4634 = relay.divide(call_4624.astype('float64'), relay.reshape(var_4633.astype('float64'), relay.shape_of(call_4624))) # shape=(11, 11, 8)
bop_4637 = relay.divide(call_4625.astype('float64'), relay.reshape(var_4633.astype('float64'), relay.shape_of(call_4625))) # shape=(11, 11, 8)
func_3338_call = mod.get_global_var('func_3338')
func_3342_call = mutated_mod.get_global_var('func_3342')
var_4645 = relay.var("var_4645", dtype = "float64", shape = (154,))#candidate|4645|(154,)|var|float64
var_4646 = relay.var("var_4646", dtype = "float64", shape = (224,))#candidate|4646|(224,)|var|float64
var_4647 = relay.var("var_4647", dtype = "uint32", shape = (1232,))#candidate|4647|(1232,)|var|uint32
call_4644 = relay.TupleGetItem(func_3338_call(relay.reshape(var_4645.astype('float64'), [154,]), relay.reshape(var_4646.astype('float64'), [224,]), relay.reshape(var_4647.astype('uint32'), [56, 22]), ), 5)
call_4648 = relay.TupleGetItem(func_3342_call(relay.reshape(var_4645.astype('float64'), [154,]), relay.reshape(var_4646.astype('float64'), [224,]), relay.reshape(var_4647.astype('uint32'), [56, 22]), ), 5)
func_4088_call = mod.get_global_var('func_4088')
func_4093_call = mutated_mod.get_global_var('func_4093')
var_4662 = relay.var("var_4662", dtype = "int16", shape = (1456, 1))#candidate|4662|(1456, 1)|var|int16
var_4663 = relay.var("var_4663", dtype = "float64", shape = ())#candidate|4663|()|var|float64
call_4661 = relay.TupleGetItem(func_4088_call(relay.reshape(var_4662.astype('int16'), [1456,]), relay.reshape(call_4644.astype('uint64'), [120,]), relay.reshape(var_4663.astype('float64'), []), ), 5)
call_4664 = relay.TupleGetItem(func_4093_call(relay.reshape(var_4662.astype('int16'), [1456,]), relay.reshape(call_4644.astype('uint64'), [120,]), relay.reshape(var_4663.astype('float64'), []), ), 5)
output = relay.Tuple([bop_4634,call_4644,var_4645,var_4646,var_4647,call_4661,var_4662,var_4663,])
output2 = relay.Tuple([bop_4637,call_4648,var_4645,var_4646,var_4647,call_4664,var_4662,var_4663,])
func_4686 = relay.Function([var_4633,var_4645,var_4646,var_4647,var_4662,var_4663,], output)
mod['func_4686'] = func_4686
mod = relay.transform.InferType()(mod)
var_4687 = relay.var("var_4687", dtype = "float32", shape = (11, 11, 8))#candidate|4687|(11, 11, 8)|var|float32
var_4688 = relay.var("var_4688", dtype = "float64", shape = (154,))#candidate|4688|(154,)|var|float64
var_4689 = relay.var("var_4689", dtype = "float64", shape = (224,))#candidate|4689|(224,)|var|float64
var_4690 = relay.var("var_4690", dtype = "uint32", shape = (1232,))#candidate|4690|(1232,)|var|uint32
var_4691 = relay.var("var_4691", dtype = "int16", shape = (1456, 1))#candidate|4691|(1456, 1)|var|int16
var_4692 = relay.var("var_4692", dtype = "float64", shape = ())#candidate|4692|()|var|float64
output = func_4686(var_4687,var_4688,var_4689,var_4690,var_4691,var_4692,)
func_4693 = relay.Function([var_4687,var_4688,var_4689,var_4690,var_4691,var_4692,], output)
mutated_mod['func_4693'] = func_4693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_4719 = relay.TupleGetItem(func_3025_call(), 0)
call_4720 = relay.TupleGetItem(func_3027_call(), 0)
func_2363_call = mod.get_global_var('func_2363')
func_2367_call = mutated_mod.get_global_var('func_2367')
const_4731 = relay.const([[3.632566,-8.686423,-9.092409,4.810113,-6.609421,6.100898,9.198987,9.805680,6.136164,-9.688226,-7.602738,-3.221044,-0.433839,5.239838,-1.992753,6.629609,1.246858,3.175460,-0.600336,7.195682,-4.772874,5.712309,3.055525,3.455069,-8.738158,2.552034,6.521099,-8.917652,5.066820,4.338150,-7.953438,1.274934,-8.175262,0.280593,1.088626,6.983622,-0.421208,4.614354,7.655818,-3.355134,-2.429924,-5.100073,7.580674,6.896961,2.925525,-9.134922,-1.611645,0.961397,-3.302941,3.046652,4.219146,-3.788118,-6.605151,2.976592,-4.653242,9.009270,6.082499,-5.663402,1.232514,1.209659,-9.967964,-3.914644,9.893815,8.983295,0.421880,1.344438,9.738550,-3.085763,9.314308,-4.612112,8.947824,-3.897324,7.363851,7.430582,8.319259,6.938768,7.124423,-2.476565,2.450852,-2.295073,-6.502476,-9.370662,9.206067,2.392998,-8.710049,-4.661151,-3.793582,2.007272,-0.631555,-8.067166,0.126341,9.294720,3.162349,-6.045845,-0.702131,1.094678,-2.691599,-2.928523,-2.602118,6.658124,9.591212,-3.645476,-4.503444,-8.505613,7.803664,-7.613527,-1.926149,6.027324,4.574454,0.041972,-9.025052,9.453534,-5.092240,9.153424,6.479954,8.381768,-9.204725,-6.819579,0.455717,5.333701,8.880543,-3.561222,-5.209427,-9.145040,6.725508,4.080820,-6.645907,-1.322887,-6.808318,-1.869164,-9.483415,0.598972,0.245328,-8.467654,-3.275578,9.726698,2.119839,6.357413,1.542578,-8.522207,4.600843,4.283928,-5.866524,-4.745093,8.071902,-1.406088,5.780109,-2.233658,-2.935941,2.335402,0.110786,-6.754539,-8.885665,-5.152187,4.957250,-2.877638,-3.277289,4.859539,-2.137761,1.885056,-7.937992,8.329901,0.415751,-5.970936,-9.236965,-1.754076,1.148859,4.120290,1.809028,9.554388,-0.894661,8.710261,6.681832,8.296225,0.206316,6.115385,-0.012427,1.687888,1.302442,0.338023,4.024216,7.887862,0.666722,7.160522,-9.110514,4.025599,-8.284570,2.649168,1.083379,1.222046,8.140875,-7.763510,-8.504496,-3.344585,-5.095077,5.424556,5.794697,-8.548997,1.809837,2.216716,-6.471090,-1.246972,-3.647795,7.590620,-7.125330,-5.805137,3.450621,-9.178696,-2.591499,2.011385,-7.968288,-2.713103,0.552609,-4.179544,-9.925793,-9.156411,0.186504,-0.703999,-4.136307,1.439004,-6.800688,2.649474,4.599114,3.102689,-4.020839,-6.497648,-8.663879,-5.659875,9.871161,-8.224603,2.298414,-3.171541,-2.642864,-7.532003,-3.623588,5.817635,8.880451,2.972066,-2.925379,-0.024412,2.136877,-4.381050,8.363729,-4.514472,0.949268,4.972151,7.317525,5.377528,-4.120407,2.497139,-5.087210,6.997097,6.714657,-7.269930,-7.585045,-1.756360,7.631707,9.767330,7.095600,6.727179,-3.002689,9.537737,-9.717366,2.585679,-3.934552,-9.968819,-4.936502,-6.085507,-0.052710,7.054956,7.184605,-9.548397,-8.968250,-7.942025,4.770944,4.647489,-6.363041,-6.470712,9.984161,4.394229,-4.146653,-7.952839,5.950229,-0.678380,0.807812,-1.128343,7.504505,3.672679,-6.569959,6.581195,4.933421,-6.924370,-7.022225,2.859609,-8.097506,8.050008,-2.602998,8.616365,7.535492,9.632168,-3.454663,0.081620,-4.053937,8.264784,-5.538155,3.452764,2.694669,7.422241,-2.031446,-8.630627,8.021216,7.321385,3.113309,-9.043476,-5.660852,-0.007057,5.357452,-3.288319,-9.842671,6.726411,-5.459225,2.307612,-3.984204,8.166091,6.180646,0.760055,-3.475349,-7.115349,-0.062733,-2.716440,-4.717914,7.575767,-8.424519,8.891556,6.980658,-2.899245,9.362508,-0.922286,-4.933272,-4.561288,2.561210,1.430974,-7.736016,2.348576,-7.226584,1.412574,-4.130391,-9.333090,-9.545003,-5.311091,-1.753830,-0.519417,-0.071753,8.896635,-9.089642,-4.237177,-8.825687,9.627166,9.821462,3.149403,-0.582492,-1.095869,6.804544,-6.735152,-2.057103,1.294862,5.317483,5.548774,-3.335160,-9.699148,-9.848635,-3.224862,-9.883185,-2.250650,3.105910,8.494363,-9.413968,-5.362732,1.520539,-7.088088,7.760154,-5.386429,0.888704,-9.311801,9.087462,-3.198464,7.646897,-8.358380,8.294203,5.378494,-3.037600,-3.703269,-5.098645,-2.739408,0.500991,-1.458508,-3.727659,5.904751,-4.660526,-8.326983,4.350900,7.633581,8.367952,-1.446490,-1.176777,6.824261,7.676810,-3.559188,5.388838,5.334779,4.603551,3.115192,-9.668313,2.320839,0.811703,-7.286041,-7.081171,8.538794,5.223382,-4.841289,-5.837696,-4.773342,-9.439141,7.037937,5.702224,-3.890915,-5.514490,2.689169,3.769848,1.515972,-0.025711,3.092192,-2.813625,-1.406758,-6.327505,2.880528,0.900676,-2.307219,-1.528953,1.686033,-9.134432,-6.714100,0.823361,-9.140632,-0.638444,8.379314,6.728547,-1.218498,-3.636296,-9.786372,7.222058,0.233439,8.538912,-8.328737,7.415261,-5.859540,-9.548787,7.669317,-5.024989,-1.320385,4.446766,1.415978,-7.318104,-1.459111,-1.134140,1.051382,1.664690,-9.085420,8.320716,-6.567000,-2.060892,-2.732756,-3.953201,4.104708,9.258697,6.561760,7.369974,-4.733930,-7.441200,-2.598833,5.701740,2.315750,-5.378463,4.865206,-0.792940,9.141390,-9.083512,5.596514,3.369297,3.651093,-7.733489,7.646621,2.337167,3.173228,9.870266,7.061806,-3.096044,3.059664,-0.183824,-3.538839,-9.238149,-0.352808,2.296860,3.825492,-9.817621,-7.148328,-6.332478,-4.998254,5.782134,8.698234,-6.435872,9.165128,7.266897,7.216241,6.964110,1.570397,6.501590,1.805138,7.228960,4.220439,1.969073,9.055033,-9.425989,-9.727082,6.161296,-5.143593,-0.256838,-6.916520,-4.542673,3.058112,5.696123,2.770735,-9.361484,-4.905598,-5.587515,0.517597,5.385541,8.729425,5.734834,4.834848,0.035903,-9.119416,7.895897,-7.027631,-1.224462,2.611062,-4.179063,0.257397,5.439232,-0.001456,1.896063,-2.591309,-3.899182,-8.982038,7.232084,1.426643,7.469756,-1.773155,-2.287620,-1.136352,-3.157126,1.807639,4.925547,-0.576342,-5.560951,-6.242112,-6.750135,-4.250109,-4.646726,-6.073953,-3.533177,-0.813047,4.314792,-7.053483,3.759707,8.410064,-8.396495,-4.349553,9.095297,3.142333,-6.487889,2.044101,-3.345808,6.126655,4.693492,-9.879866,7.055324,2.180556,4.468087,5.538117,6.310663,-9.699676,3.324292,1.927686,4.279574,-4.423616,-8.419129,5.250974,4.588767,6.407756,-1.839223,-3.055005,-2.744083,1.653626,6.715421,8.531829,3.608282,-4.264594,-1.865082,4.364568,-8.730906,1.881007,2.005480,2.321753,-3.669725,4.849765,-8.369128,-4.792775,-9.445608,-8.863051,-3.789604,-0.010943,-4.335600,-1.758226,-7.900923,-2.918387,5.620756,2.910344,-9.210959,2.755144,6.724424,-8.562588,-0.537185,-0.105477,-5.762172,-4.050847,-1.868466,-1.449618,-6.536662,-5.890954,-4.781948,6.591646,-6.335724,-6.730434,-4.969660,4.917599,3.835968,0.189608,2.483170,-8.977238,2.181494,-4.052662,9.022856,-9.900465,-3.114370,-5.121076,6.385817,-3.788526,-4.293843,8.176407,0.185425,-6.831499,-8.690348,-1.624734,0.454011,6.997314,-3.760456,9.212870,-8.940790,8.702469,-2.611303,5.489656,4.035371,4.672501,-4.027251,-4.238976,-3.273301,-3.855862,3.676287,-9.472650,4.868878,3.359606,0.424111,6.824403,-8.286541,-2.173036,-1.303243,-7.405896,-8.831415,4.582101,-4.769688,-5.342946,-9.337312,2.480559,8.387875,8.280628,2.273265,-9.120820,7.705550,-3.748872,-4.301095,-8.278685,-3.126273,1.252621,-0.331564,-8.403026,-9.954202,1.328106,5.249048,-8.034891,-3.328705,-8.028537,-8.028449,3.668012,-8.554237,9.825086,-9.392634,-1.635379,6.092413,6.874149,-9.544626,-6.507291,-8.908254,-1.687616,1.754860,1.861622,-8.284435,6.848270,-3.903687,-8.325733,5.461028,-3.989165,1.760814,-3.191390,-5.920010,-5.088649,1.114730,2.873996,9.830848,-8.391558,9.545920,-8.964152,9.673310,-9.180760,-2.643735,-2.802761,9.422001,-8.534901,5.788030,7.257417,-5.871661,0.382159,-7.755105,-8.026836,-8.010027,-6.063964,-9.050019,7.554090,3.919513,8.732216,-7.648088,2.035703,-8.919750,-4.210112,-3.236799,9.914487,3.133631,2.527372,-8.252237,3.577385,-3.573378,-6.352631,2.493911,-4.422906,3.396155,-9.439809,9.963782,2.572155,4.343673,-3.899580,2.043224,6.481417,-2.462489,8.214374,-5.513197,2.366755,-1.462037,8.669764,4.423148,-4.632187,6.159581,-0.748344,-5.723469,5.425996,5.054012,-4.826770,0.865007,0.436053,-6.098047,-8.713240,-2.513428,0.086470,3.502089,-9.741653,-3.202019,-2.403409,6.264323,-1.130641,-5.527029,-9.466065,9.166606,6.294866,-3.070773,-0.995595,3.099142,1.962713,-6.311194,-0.510428,2.480472,-7.287419,-9.319435,1.383643,2.690596,4.131579,8.515016,5.621920,-5.533195,-5.304486,-4.127769,2.721948,3.956002,8.754479,8.693316,-2.734163,-9.684177,-0.765802,6.371056,-3.642400,-1.151058,-5.324331,5.760360,-3.363827,-3.101499,-6.597403,-7.641809,-6.831539,-8.209978,9.953079,-9.535358,-6.377704,6.024927,6.375189,0.928982,1.540020,1.938839,5.101862,-5.448134,7.968262,-0.061746,5.256055,1.069753,0.026363,8.414988,-1.202771,-9.094449,-0.655420,6.869410,-1.773036,8.886689,-0.002529,4.084570,-9.212973,-9.627044,1.901175,3.897841,3.113283,-6.676375,0.008293,7.805515,4.825157,-8.759134,8.277943,9.908653,-3.445267,-6.067895,-0.825791,6.399340,8.558610,-9.952913,-3.303480,1.472277,-2.713978,-9.995756,2.580263,6.457012,3.127160,-4.407023,-1.675938,-6.648771,-1.298219,0.867566,4.903948,5.928952,-0.644865,4.794897,-8.649411,-4.803098,-4.686584,-7.780356,1.389662,8.013501,7.616827,3.165483,1.813285,2.478784,-3.361024,-8.149816,8.324953,-5.833190,7.279749,-5.556883,-2.525101,1.981025,-7.896949,-9.063169,5.782992,-5.483162,2.723818,-5.119024,-9.381638,2.060483,7.921130,-8.865726,8.368155,-4.283016,-4.097290,-0.496588,-9.321723,3.652466,0.247805,-4.280661,3.225553,-8.196600,-0.087214,-2.593732,-7.515081,-1.066778,7.465771,-5.925128,5.843497,-8.318498,8.394973,7.279144,-7.015022,-0.990104,-0.925526,-7.372706,-5.936570,3.817333,-8.808204,0.086328,0.224340,-0.853386,-0.476821,8.013943,6.964364,9.960865,8.902691,-5.993037,3.916341,8.186153,7.331773,-7.622965,-7.063511,5.868537,5.170364,1.810777,-4.697286,6.159442,-2.522652,-2.950826,-2.094321,7.528394,-5.354233,2.438871,-0.617468,-2.080568,2.854060,4.972493,-4.974259,-8.839839,5.171879,-5.271097,8.060412,-0.930819,-1.173939,2.090905,-3.497604,-3.245703,7.585456,2.254885,8.469075,5.593237,-6.104331,-2.800912,3.308250,-5.623883,4.652990,-6.822502,-6.248788,-1.214679,-6.035505,-5.196167,-9.788477,0.955883,-0.280473,-1.513362,-7.446866,-8.946873,-6.312946,5.152648,8.916023,8.629065,-2.350937,9.602063,-6.640571,-7.038606,-3.290517,-2.980978,5.257361,-6.565504,-8.101048,4.548273,-6.904720,9.021170,6.499616,3.019109,-5.540060,2.494802,-4.716706,7.228375,-7.987168,9.300844,-2.992752,-3.149000,-3.920181,-1.278282,2.231231,9.689193,8.865823,-6.012460,-6.272231,-3.704217,-0.028568,1.935481,-9.089112,-7.731243,-7.482286,7.383938,6.493222,0.744818,-5.960603,-8.353608,4.928184,-2.407139,-7.194075,0.054440,-8.730911,8.801010,8.811579,7.279350,3.690184,1.987422,-4.752245,5.707674,-3.831661,8.453830,-9.235058,-1.961909,4.769139,-6.363778,6.872688,-9.153059,3.921242,0.356964,2.731500,5.863664,-5.212663,-7.054330,8.303859,-3.822240,-6.569613,3.471874,9.823274,3.094517,-2.509166,-7.270058,7.635703,7.160097,-8.334461,-0.538469,8.907136,-8.295364,-8.659257,-5.047481,-7.771940,7.879958,-4.618873,1.134001,-0.543672,5.288419,0.274695,-5.918145,-5.326615,3.568002,-6.271521,-9.128391,3.378044,8.021251,-4.731654,-5.040623,-9.486711,4.845386,-4.167102,-1.209411,9.960821,9.994190,9.433679,-8.897694,2.012711,-1.681856,8.097245,0.722587,-7.152984,-3.986004,8.412645,7.323189,-0.555654,-0.634255,-9.018110,4.730794,-1.628036,-7.429121,-6.441181,-7.328294,-0.763548,-6.803435,3.469516,6.097370,-6.747969,-7.803780,-8.451151,-7.118973,8.107188,6.320905,9.880909,5.284998,1.830854,-2.855029,-9.972839,2.638554,2.727269,-9.037461,6.448169,-0.414382,5.117465,5.286585,0.208764,-1.197911,9.485657,-3.660274,-1.690167,-6.497418,5.289202,-6.187682,5.272855,-0.740929,3.485261,-7.150341,-4.597242,-2.654524,5.694911,8.901588,0.294942,7.601099,9.879110,-4.326344,-3.669643,7.521155,2.851300,5.270122,2.231287,1.818196,5.622095,-1.871599,2.588573,4.146717,-6.328045,8.357910,7.330311,-2.497197,-0.248748,-1.194615,-7.598158,-3.186797,8.504492,-0.764745,9.933805,4.344572,3.821945,8.314993,0.039651,-2.471592,0.290702,0.766248,-8.333946,-4.761818,-9.335408,2.589592,-5.198852,-9.789145,-7.221726,7.135121,6.428701,-3.903065,-0.966589,2.523371,-3.191575,1.506530,6.486261,-2.186248,2.896040,-6.445852,-8.006527,-2.568056,6.722290,-2.928203,0.923619,0.786461,6.889203,-9.602977,3.080413,2.005313,5.170720,-9.237883,6.958488,-6.848979,4.988610,1.039901,0.207364,-9.034829,-1.190183,-8.423137,-3.826599,-6.348596,1.999947,7.629572,-7.240035,-6.065244,-4.435405,-2.226694,-2.950632,-1.436877,8.830824,3.811095,6.422966,0.095286,-5.886934,3.241698,-8.066250,-3.211215,-8.999959,-7.641498,-3.050189,-9.935175,5.945738,3.041052,-8.931252,1.187931,1.550761,-6.203124,3.632738,-8.323851,0.530274,-1.480265,-4.811952,1.939135,0.083252,5.408852,-4.672471,-4.976414,9.846775,0.578769,1.369151,2.453914,4.385621,4.558911,-6.391774,1.553498,6.237239,2.076542,-0.881779,6.071678,-4.868722,-0.843150,-5.535944,7.616644,-4.334600,2.782885,5.511541,-9.519179,-2.175485,4.523145,4.768741,-3.116663,6.208195,-1.126522,-0.588349,2.032886,9.105886,-2.971806,-4.285889,2.026770,-8.349415,-7.789830,6.697449,8.899162,-9.471856,-8.208716,5.662147,-2.019710,-8.247561,-6.750284,-0.996322,-5.995937,9.809702,-8.152768,-0.934807,-9.670967,-4.270690,-7.831669,0.767943,-5.906201,3.402989,-8.165974,2.479660,0.981605,5.713696,3.127776,1.112083,7.068026,-4.560067,-0.385818,8.350555,4.439593,1.924008,-0.481898,3.056347,-8.635710,1.809807,5.237116,4.843094,0.050736,8.017630,0.774124,-0.285578,8.325304,-2.547425,8.711123,5.783219,7.572871,-3.729940,3.367093,-8.727632,-7.711923,-1.739337,4.111642,-5.376304,5.981137,8.412554,-7.451393,9.098423,-0.146849,0.163459,-1.181422,-2.647336,2.524477,0.845816,9.735444,-5.846066,0.334083,0.744167,7.917026,6.974108,7.419558,2.818070,-0.468640,-2.166640,-2.873978,-6.114118,-7.194037,-2.501147,-3.122719,-9.703565,-9.298304,6.803982,-4.077671,-9.394319,9.045996,-4.634038,-3.266916,-3.191255,-0.985369,9.348959,0.388588,5.352449,-9.305186,5.326948,0.545276,-3.995758,1.015478,-1.909182,7.949116,9.295088,-6.229212,2.706269,7.564965,-8.212190,-9.754659,-0.893597,3.176355,9.953933,0.560171,-5.159832,6.098432,-8.801296,5.696076,-0.323890,7.843730,5.857394,4.565823,-3.530757,-7.200324,-9.580457,-0.001014,-3.990661,1.871311,-5.285257,4.620177,6.164074,5.615328,6.764928,-6.993723,5.598902,2.509147,-7.481881,-8.247494,3.876049,8.948916,4.546182,-7.392162,4.759657,-2.011841,-9.704473,3.112851,-1.830581,-2.264631,0.735658,8.351170,-3.952990,5.102744,1.922631,-1.508691,-5.095303,-2.956921,6.476944,-4.343070,-8.154987,-7.269242,-2.300161,5.636375,7.674414,-3.934676,-5.088795,8.118121,-9.289190,3.866393,-5.478270,-7.242117,6.135242,9.835653,6.753544,-8.260817,-8.730088,-1.932425,-8.669999,3.634866,9.944166,-3.976009,2.678187,2.863851,-5.031360,2.999594,-3.607637,3.297989,-7.974161,-7.029642,-3.065756,-4.624892,-7.606807,7.242399,-1.691374,-4.603234,-6.183032,6.180126,-9.295432,9.938285,-7.738159,-0.952639,-8.034096,-3.603795,-1.103606,-8.394597,4.534592,9.369554,-9.080233,-3.999557,3.195585,-7.270786,6.325044,0.145963,-3.366043,-1.449029,4.913899,9.256574,1.472558,-7.608644,5.760127,-6.868048,2.505467,-6.447751,7.084370,-1.118767,2.661672,-8.135226,8.772694,-2.683849,9.449680,-4.764611,7.782527,-3.403444,4.224076,-0.632753,-1.501481,-4.253654,-5.181616,0.899967,0.376042,-1.997383,-1.870074,-9.365613,-5.061963,-4.773493,8.744133,-2.333714,-4.097099,2.304918,-6.242422,-5.735790,3.348311,-6.324507,4.209745,7.886056,-3.368659,5.404637,-6.895677,-7.405150,0.172684,-9.656623,3.958704,8.620981,-6.446421,3.162368,4.095885,0.292579,-2.032825,-2.920126,7.433952,4.296335,-0.092337,-0.001810,-0.314163,3.870113,8.132257,-2.889846,1.478908,7.048122,7.411915,-2.833994,-9.057697,5.207823,3.868344,8.815578,2.009713,-8.227281,0.625940,-6.424568,4.432763,1.196497,-7.086628,7.294632,-8.092808,4.869653,-5.535871,-1.439634,5.676183,3.148003,2.208318,6.159867,1.051995,-7.949045,-5.629665,-1.530465,3.280895,3.880368,-1.949186,2.247812,9.599827,-0.100339,-4.497322,-2.911605,-2.284850,-3.530354,-4.447847,-8.525218,-2.733277,8.938697,4.607595,-0.083766,3.641881,-8.739439,6.878525,-8.083004,-1.231270,-5.236787,5.156565,-4.475280,-6.949941,-3.612742,-1.236378,9.052208,8.698354,-7.646299,-1.536949,9.876834,-4.553823,4.286251,6.344394,-1.599919,-4.811083,-0.351775,5.723557,8.091328,-4.069537,8.578225,-5.139819,8.725033,5.114333,9.357139,-6.801752,4.289621,-4.444492,-0.587762,5.282084,-5.246820,2.641325,6.389660,9.660816,9.365004,-2.878902,4.516530,5.078076,5.629936,-9.483046,-6.865822,2.476525,4.750433,0.699705,-5.854846,-7.251046,-8.299922,3.188966,-9.334179,3.837463,-9.393586,-0.428539,-1.622035,-4.299427,-0.924945,-5.673737,-7.599181,7.767170,-5.446089,6.388125,9.632371,5.108496,-7.395756,8.619305,9.378967,-0.500667,7.457134,1.173721,-6.039534,6.151113,-4.739615,0.782657,7.346170,-3.743610,8.488437,-6.213147,6.140611,4.561715,7.220249,1.585186,3.075227,-9.195955,-4.996913,-0.159064,-0.163368,-8.403040,-7.135472,0.284853,-3.944067,2.938441,8.416469,-5.829559,1.568551,-4.412915,-9.771070,2.893530,6.729278,-8.980363,-2.119609,-5.625729,-7.725049,4.280216,4.796797,1.776034,6.081583,0.211738,-3.239654,5.356651,8.917890,-5.676599,6.478591,4.081626,-2.702630,8.531299,8.456757,8.189246]], dtype = "float32")#candidate|4731|(1, 1760)|const|float32
var_4732 = relay.var("var_4732", dtype = "int16", shape = (1, 1456))#candidate|4732|(1, 1456)|var|int16
call_4730 = relay.TupleGetItem(func_2363_call(relay.reshape(const_4731.astype('float32'), [10, 16, 11]), relay.reshape(var_4732.astype('int16'), [1456,]), ), 0)
call_4733 = relay.TupleGetItem(func_2367_call(relay.reshape(const_4731.astype('float32'), [10, 16, 11]), relay.reshape(var_4732.astype('int16'), [1456,]), ), 0)
output = relay.Tuple([call_4719,call_4730,const_4731,var_4732,])
output2 = relay.Tuple([call_4720,call_4733,const_4731,var_4732,])
func_4734 = relay.Function([var_4732,], output)
mod['func_4734'] = func_4734
mod = relay.transform.InferType()(mod)
var_4735 = relay.var("var_4735", dtype = "int16", shape = (1, 1456))#candidate|4735|(1, 1456)|var|int16
output = func_4734(var_4735)
func_4736 = relay.Function([var_4735], output)
mutated_mod['func_4736'] = func_4736
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4738 = relay.const([[[9,-7,10,-10,-5,-6,9,-10,-9,-6,-9,-10],[5,3,9,7,3,-5,-1,-9,3,-9,-7,7],[2,-6,4,-4,-7,10,2,4,-9,-8,3,-7],[5,9,2,5,-1,5,-8,-8,-7,10,4,-5],[-10,3,2,-10,-3,6,-4,1,3,-3,-6,5],[7,-3,9,4,-2,-5,-5,1,1,-5,-10,2],[-2,-4,4,-2,-7,2,4,9,2,-2,6,-5],[1,-6,6,-2,-1,-5,-8,-7,-5,-2,4,-6],[-3,3,2,-10,10,1,4,-2,-2,1,5,6],[7,-10,-9,-7,-5,-4,10,9,10,4,5,-10],[-5,8,8,-2,2,-6,-6,-5,-5,9,3,-5]],[[-8,-10,7,10,8,3,-4,1,-5,-8,1,-6],[-2,-2,-3,-1,-8,-3,-8,8,-5,-2,-6,-6],[1,3,-9,6,4,-8,5,-7,10,-9,-7,4],[7,-10,10,-3,-1,-3,-5,-4,7,5,1,6],[-6,-10,1,2,2,9,9,5,8,2,6,-2],[8,-6,1,-2,6,-7,-6,5,2,-9,7,1],[-1,9,-9,-10,-10,7,10,-10,1,-3,10,-2],[3,-3,7,-8,-7,6,9,4,-4,-5,-2,1],[4,-8,-6,-7,6,-1,-4,-1,-5,-6,5,-6],[-2,-3,5,8,2,6,-8,8,2,7,6,6],[5,6,1,8,10,-8,9,-6,1,10,-6,-3]],[[6,4,-8,-3,-10,2,10,5,-5,-7,-6,-7],[7,-8,4,1,1,-1,-4,1,-5,7,5,5],[4,6,7,1,-9,-6,8,4,-1,-8,1,-10],[4,-2,-1,1,-1,7,10,-3,-7,-3,-6,-4],[-2,-3,4,9,-3,7,2,-9,-6,-2,-6,-7],[-5,8,5,-8,6,2,-5,8,-4,1,-4,10],[1,-8,8,-2,4,-2,-3,8,2,-9,-10,4],[-1,-1,-7,7,-4,7,-10,3,-10,-3,-7,-2],[2,5,-8,10,-4,-8,-2,1,2,8,-8,6],[-7,-10,-1,-1,-4,4,5,-5,5,-2,-8,4],[2,2,2,7,-6,-4,-1,-9,-3,-9,9,9]],[[-7,2,3,-7,-8,6,-8,1,-2,-2,-2,-10],[-8,-3,-2,2,3,-9,1,-3,7,-1,2,1],[-9,-9,-6,5,-7,-10,3,10,-5,4,7,7],[7,-10,-1,7,6,10,2,-5,-6,-9,4,-6],[-8,-4,-10,-8,-10,9,1,-1,1,-6,-1,-3],[-5,-7,-10,7,3,-3,-4,-1,-1,-8,-6,7],[2,-10,6,9,4,10,1,3,1,-9,9,1],[-10,-10,10,2,3,-7,5,-10,-4,-4,8,-8],[-3,7,-7,-10,9,-5,-7,3,1,9,-7,-5],[-9,-5,6,9,-2,-9,-5,10,-9,5,2,-8],[-7,8,-7,-7,4,7,-9,9,-3,2,7,3]],[[7,-6,7,9,-4,-10,-4,1,-10,7,-5,1],[-5,7,5,2,10,-8,-3,-1,-7,-9,-9,-8],[9,8,-4,-3,2,-2,9,-8,1,6,-6,-2],[9,6,2,-8,-1,-4,-3,-1,6,-3,-7,-6],[10,4,-10,-1,-8,8,10,10,10,4,2,2],[3,4,8,-10,-1,-4,-1,-3,-3,8,7,-5],[-3,-4,-8,-2,2,1,-6,-8,-7,2,-9,-8],[4,-4,-5,9,9,4,8,8,-2,9,2,-6],[10,-7,-1,-9,-3,7,3,-6,7,-2,6,4],[1,-7,-1,-9,1,1,-3,10,-5,-3,-2,5],[-9,-4,-6,-4,-6,-9,-3,9,6,-9,-10,6]],[[5,6,-8,-5,-7,-1,-1,-2,-5,-3,1,6],[2,8,-4,7,-2,7,3,7,2,7,-5,2],[9,-10,-7,-8,4,9,10,7,9,4,-5,6],[-10,-3,-1,5,-10,8,3,-6,-4,5,3,10],[6,-5,-4,8,-5,1,8,4,2,5,10,4],[-8,-9,-1,-2,2,7,10,2,-8,1,-8,4],[-9,-9,2,-4,-2,-1,2,9,-1,-2,4,8],[8,8,4,-7,-2,-3,-10,7,2,7,1,1],[-4,5,-6,10,2,-9,-9,-1,-5,-7,5,-10],[-4,-2,5,-7,6,-7,-4,-6,4,-7,4,-7],[-4,7,-10,6,-2,-9,2,7,7,-10,-2,1]],[[4,2,6,8,-4,1,9,-10,-8,9,-4,-7],[2,-5,-4,4,-4,7,-4,2,-9,3,-2,1],[1,-9,-10,-7,-4,9,-7,-7,7,-3,-8,-10],[9,6,-8,1,-9,-2,7,-3,2,-10,-5,1],[2,5,-10,8,2,-1,1,8,10,-10,1,-7],[-5,1,-3,-4,-6,-6,7,6,-8,-8,8,-10],[7,-7,-5,-1,-1,-2,5,-1,6,9,-1,-3],[-3,7,-8,-2,-1,5,-3,-8,-7,1,8,-4],[1,-8,-10,1,-3,-7,-9,7,-9,-8,7,9],[8,-7,-3,-1,-8,-5,9,4,-6,2,-3,3],[-9,4,-7,-1,2,1,3,-8,-10,-1,-10,-10]],[[7,10,-1,2,6,-8,-1,-9,-1,8,4,-4],[2,-3,2,7,-5,1,-1,-6,3,1,-4,-6],[-5,-8,-4,-1,-10,7,8,-3,-2,-1,-9,4],[-10,5,9,9,-10,1,1,-8,-8,3,10,1],[2,9,-8,5,-7,-3,6,10,-9,7,3,-1],[2,-7,3,4,-1,-9,5,-8,-6,1,-5,7],[-10,-3,2,5,1,-6,-1,2,-5,-2,4,-3],[3,4,4,1,8,10,10,-5,7,-7,-4,-4],[-9,9,6,-8,5,6,-5,-7,1,-6,1,3],[-5,-8,-9,-7,-9,-4,8,6,3,-7,9,1],[9,2,-9,10,7,-4,-2,-7,-9,8,4,-3]],[[7,5,-1,-5,-6,-2,4,-8,2,9,4,7],[-10,1,8,-1,5,1,4,8,-5,-4,4,1],[-5,2,-10,-5,1,-4,-1,3,3,-1,2,-9],[-10,9,7,2,4,-3,10,-5,-3,1,4,-7],[-10,7,8,2,-9,5,-2,-7,-8,1,10,10],[-2,7,-7,-6,5,-2,9,2,-6,3,-4,4],[-3,-2,10,-6,5,2,-8,-2,2,-5,-9,-1],[5,-2,-6,-3,-3,4,8,-8,3,-8,8,3],[3,5,6,6,-9,10,-7,4,7,3,-8,-10],[-1,-2,-8,3,3,-3,1,2,-8,-5,7,-6],[9,-2,2,-8,2,-6,-4,-4,-4,-8,8,6]],[[4,2,-3,8,10,9,-3,7,-4,8,9,-7],[-10,-9,-6,-6,-6,-4,7,-1,9,8,-6,7],[-5,9,8,-8,-2,-7,-2,9,-9,9,4,-2],[-1,-6,5,-8,-8,-4,-3,-5,9,-3,2,1],[4,9,3,2,-2,-10,2,7,4,-6,-2,-4],[-2,-4,-9,-8,-6,-3,-8,2,3,-7,1,-5],[-5,-6,4,10,4,-2,8,8,-5,-2,7,-5],[9,3,5,-6,9,-1,-9,8,-4,8,8,-7],[-8,8,-4,-6,-4,-2,-5,1,-8,6,5,5],[-6,-1,-1,-9,-7,6,9,-4,-9,4,-3,-9],[-9,-2,-2,-4,-10,-3,5,-1,9,6,9,3]],[[-6,-5,1,-4,10,-5,-3,-1,3,-5,3,1],[-5,-2,-6,-4,9,1,-3,2,-1,6,-5,-6],[-8,-7,8,5,-4,8,1,2,1,-3,8,-6],[2,2,10,6,-2,-10,-10,6,5,5,5,-7],[-3,-9,-6,2,10,5,-4,7,-3,-6,4,-8],[3,-5,3,7,4,8,4,8,-4,1,6,-1],[6,2,7,-1,5,3,9,7,5,-3,-5,-2],[-6,6,2,10,3,2,-6,-2,-10,-1,4,-4],[3,-7,-10,7,3,-9,9,5,-3,-5,9,-10],[-4,-7,8,7,-1,-10,-5,-9,10,-5,9,-2],[8,-1,-7,-5,-3,9,-6,-5,-3,9,1,8]]], dtype = "uint8")#candidate|4738|(11, 11, 12)|const|uint8
var_4739 = relay.var("var_4739", dtype = "uint8", shape = (11, 11, 12))#candidate|4739|(11, 11, 12)|var|uint8
bop_4740 = relay.minimum(const_4738.astype('uint8'), relay.reshape(var_4739.astype('uint8'), relay.shape_of(const_4738))) # shape=(11, 11, 12)
uop_4746 = relay.rsqrt(bop_4740.astype('float64')) # shape=(11, 11, 12)
var_4752 = relay.var("var_4752", dtype = "float64", shape = (11, 11, 12))#candidate|4752|(11, 11, 12)|var|float64
bop_4753 = relay.add(uop_4746.astype('int32'), relay.reshape(var_4752.astype('int32'), relay.shape_of(uop_4746))) # shape=(11, 11, 12)
bop_4758 = relay.maximum(bop_4740.astype('uint64'), relay.reshape(var_4752.astype('uint64'), relay.shape_of(bop_4740))) # shape=(11, 11, 12)
bop_4765 = relay.bitwise_xor(uop_4746.astype('int16'), relay.reshape(const_4738.astype('int16'), relay.shape_of(uop_4746))) # shape=(11, 11, 12)
func_777_call = mod.get_global_var('func_777')
func_781_call = mutated_mod.get_global_var('func_781')
var_4772 = relay.var("var_4772", dtype = "float32", shape = (336,))#candidate|4772|(336,)|var|float32
var_4773 = relay.var("var_4773", dtype = "uint64", shape = (120,))#candidate|4773|(120,)|var|uint64
call_4771 = relay.TupleGetItem(func_777_call(relay.reshape(var_4772.astype('float32'), [6, 7, 8]), relay.reshape(var_4772.astype('float32'), [6, 7, 8]), relay.reshape(var_4773.astype('uint64'), [120,]), ), 0)
call_4774 = relay.TupleGetItem(func_781_call(relay.reshape(var_4772.astype('float32'), [6, 7, 8]), relay.reshape(var_4772.astype('float32'), [6, 7, 8]), relay.reshape(var_4773.astype('uint64'), [120,]), ), 0)
output = relay.Tuple([bop_4753,bop_4758,bop_4765,call_4771,var_4772,var_4773,])
output2 = relay.Tuple([bop_4753,bop_4758,bop_4765,call_4774,var_4772,var_4773,])
func_4778 = relay.Function([var_4739,var_4752,var_4772,var_4773,], output)
mod['func_4778'] = func_4778
mod = relay.transform.InferType()(mod)
var_4779 = relay.var("var_4779", dtype = "uint8", shape = (11, 11, 12))#candidate|4779|(11, 11, 12)|var|uint8
var_4780 = relay.var("var_4780", dtype = "float64", shape = (11, 11, 12))#candidate|4780|(11, 11, 12)|var|float64
var_4781 = relay.var("var_4781", dtype = "float32", shape = (336,))#candidate|4781|(336,)|var|float32
var_4782 = relay.var("var_4782", dtype = "uint64", shape = (120,))#candidate|4782|(120,)|var|uint64
output = func_4778(var_4779,var_4780,var_4781,var_4782,)
func_4783 = relay.Function([var_4779,var_4780,var_4781,var_4782,], output)
mutated_mod['func_4783'] = func_4783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4409_call = mutated_mod.get_global_var('func_4409')
call_4813 = func_4407_call()
call_4814 = func_4407_call()
func_2363_call = mod.get_global_var('func_2363')
func_2367_call = mutated_mod.get_global_var('func_2367')
var_4821 = relay.var("var_4821", dtype = "float32", shape = (1760,))#candidate|4821|(1760,)|var|float32
const_4822 = relay.const([-2,-6,-7,2,9,-10,2,-10,3,1,-3,3,-1,2,-4,8,6,-4,6,3,-1,-6,4,7,5,7,3,8,3,-7,-10,2,1,-9,3,2,-6,1,6,7,-8,-1,-4,-4,6,-3,-8,-4,-2,-6,8,3,6,-6,-1,-6,-9,9,4,10,5,-8,-8,-2,9,9,5,1,-5,-6,10,-5,-6,2,-6,-4,6,5,-6,6,6,3,7,-3,-9,-9,10,9,8,8,4,6,3,3,10,-5,7,6,-1,8,-9,-10,1,-4,1,-3,-3,-2,-2,-8,-6,-7,-10,-7,-3,1,-4,-10,10,-3,6,-3,-7,-7,-4,9,7,-3,10,-10,-6,6,3,4,10,4,5,8,6,1,10,10,-8,8,4,5,-10,10,7,-7,-3,-4,10,-10,-7,6,1,-7,-8,10,-3,-4,6,-4,-9,-1,-4,1,-6,10,-2,-3,2,-5,-4,-2,10,10,9,-8,-7,-1,3,-6,-4,4,-3,-2,-6,-7,4,9,-5,-9,-5,5,7,2,1,-10,-4,-5,-1,4,-6,10,-2,3,10,-4,-10,-4,8,-8,3,3,2,6,7,-3,-3,-2,-3,-2,8,5,-6,6,6,2,1,1,-5,7,9,6,2,-6,-2,8,-6,-7,-6,8,-8,5,6,-5,3,5,-3,-3,-9,-1,-7,1,6,8,5,-5,-6,2,-6,-5,8,-10,-2,-5,-2,-4,-7,-4,4,-4,10,2,10,8,-1,-5,-6,10,-10,9,-3,-2,-7,-3,10,2,9,-6,7,4,-8,9,-6,3,5,-7,-4,-1,5,6,3,7,-1,8,-8,10,-3,-3,-9,4,-8,-4,-10,-5,-9,4,8,-2,6,-1,-6,4,9,10,-2,1,7,-2,10,-6,10,-3,-3,9,8,-6,10,-4,7,-8,10,1,-7,-6,2,-8,-10,-1,7,-4,2,9,-2,-3,-7,-10,-2,-4,-3,8,2,8,-8,-7,-10,1,-1,-4,-3,3,-9,9,-3,-10,5,10,5,-9,6,7,-7,8,9,2,-2,-4,-8,-4,-9,-7,-4,2,-6,2,7,10,10,-5,-3,-2,3,-7,10,4,-8,2,8,9,4,-8,3,-8,-7,1,-1,-4,-9,-5,-2,6,10,2,-3,1,-4,-2,-6,-9,5,-2,3,1,7,-10,-5,-9,-8,2,-1,1,-2,2,5,-1,-9,5,9,3,1,4,-2,2,5,-1,9,-2,5,10,-5,-10,-4,-8,2,8,7,-3,7,8,1,8,3,2,-6,-10,5,-7,7,-3,-9,4,3,6,3,3,5,-4,1,-8,10,8,-8,-4,2,-3,8,-6,3,2,8,-9,-7,3,1,-5,-1,-6,-9,3,-8,10,-4,-7,-2,2,-6,-5,6,-9,3,-9,8,-1,-8,8,-1,-1,7,-1,-1,-1,5,-8,-5,-9,-4,3,8,8,-10,-1,5,5,4,-2,-2,1,-8,10,9,-2,-10,4,-10,-3,9,1,-7,-5,-4,-5,-8,4,7,-9,-3,-7,7,2,-4,-8,-8,4,-7,6,7,-10,8,-1,7,-9,-5,7,10,1,-2,-4,8,-6,10,-6,3,-2,-9,-4,-6,-1,1,-3,5,4,3,-10,7,-5,9,-6,7,-3,-2,5,4,-9,1,-6,3,6,8,-6,5,4,3,8,9,-8,-10,8,-8,9,-6,8,4,7,1,9,-7,9,4,-9,1,-3,-10,-5,6,10,8,5,-3,4,-8,-1,7,-4,-9,3,10,-9,4,1,-9,-6,-10,-8,5,-6,-6,-9,-8,3,6,5,1,10,-9,9,-3,-4,-6,-3,-6,-4,-7,5,-6,1,6,1,2,-5,2,1,-9,-6,9,5,-10,10,-4,1,3,3,7,-7,3,2,-5,1,-7,-10,6,-4,6,4,-8,9,8,-3,4,-6,3,4,-10,-4,2,5,-9,8,2,-3,-8,2,-2,3,-4,-5,-6,6,6,4,4,-9,8,-6,9,1,-2,3,7,-4,-4,9,-9,-9,3,-4,5,-9,9,5,5,-3,-8,-4,2,-7,6,8,1,2,-1,10,-8,-8,4,-4,9,9,6,6,9,4,-9,3,-10,-5,-9,-6,4,3,7,-9,5,-6,1,-8,-5,-8,-7,-6,3,-9,-6,9,-10,10,-10,-6,8,5,-3,-10,5,7,-8,-10,-4,-3,-7,2,7,-7,-2,-1,6,-2,6,1,1,-5,1,-9,-6,5,7,1,1,10,-2,8,6,8,3,5,-7,2,-6,3,3,7,7,-5,-7,-4,7,-8,-1,7,8,-5,-2,3,7,-4,-5,-2,9,1,-4,7,-6,-6,-3,-8,-5,-6,-1,9,-6,-8,-3,1,10,10,-6,7,1,-8,6,-7,-8,-10,-3,-7,-1,8,-5,-6,3,-1,2,-3,-1,9,-7,-10,9,-4,-10,-1,-7,-5,-2,-9,8,7,6,-6,1,4,-2,-4,4,-3,-10,5,5,-10,-2,3,-9,-1,10,-1,3,-10,-8,5,-4,-6,7,4,1,1,2,-3,-4,-5,-2,-7,2,9,4,3,6,-6,1,7,3,3,-1,8,1,-2,-10,9,10,1,5,6,3,6,-10,-6,-10,10,-7,9,-2,2,-3,5,2,9,-1,-9,-5,-10,6,9,7,7,10,2,8,7,9,-7,7,6,-9,4,-10,2,-2,-3,-2,3,-8,-5,10,-2,-1,10,2,-8,1,-8,10,-8,-9,-1,3,3,10,-2,10,-1,-10,1,-7,5,-4,-8,3,7,8,4,-4,5,-7,-6,10,9,8,-3,2,-2,1,1,9,7,-7,-1,8,-5,-4,3,10,-3,2,5,4,-10,-1,-10,-8,10,-5,-6,-8,9,4,5,2,6,3,-9,1,3,-2,-2,9,-8,2,1,-7,-3,2,6,-7,-9,-4,-9,-10,6,-7,-2,8,-5,4,-10,6,-1,-1,-2,9,-1,2,5,2,3,10,8,-5,-8,-10,-9,4,-5,-7,5,10,7,4,3,-5,-7,-2,-3,-9,6,-1,-6,-5,2,-7,7,1,-1,-8,-2,1,-10,-8,9,-3,-7,-2,-1,-3,8,-8,-9,-9,-5,-5,1,-10,-8,-3,-6,-6,3,7,4,9,-3,-6,-7,3,3,-2,-5,-5,-1,-3,-7,1,6,7,1,3,2,-6,-6,10,-10,-6,-5,9,-1,4,-1,1,-6,-9,-2,-10,-6,3,7,5,-8,-2,4,-10,4,-5,10,2,4,-2,8,3,8,7,-1,-5,-3,-3,-10,2,-8,7,-4,-5,-2,7,1,-3,-7,-6,-3,1,-10,3,-9,2,-1,-9,-9,3,3,1,-3,-5,-7,1,2,5,6,3,-10,-7,5,-6,-10,6,-3,9,1,8,-5,-7,-1,-10,-10,-4,-8,-5,-7,-7,-2,-2,2,-2,-7,3,9,10,4,-9,-5,-9,6,-7,-5,-1,9,-5,-9,4,-7,-10,6,-8,-10,-9,4,9,9,4,-10,2,-10,-10,4,-7,-10,-9,4,1,6,10,-5,1,-5,-10,2,4,-1,-3,10,-7,-4,1,2,6,9,8,-7,1,-4,6,-5,7,7,-10,-9,-9,3,-5,-1,5,-8,-5,-3,-6,-7,2,7,7,-1,-2,6,-5,1,-4,-10,-2,3,5,4,-1,-8,-5,4,8,1,-6,-1,-7,-1,-3,-1,1,-4,8,-10,9,3,10,7,5,-7,-6,1,3,6,5,2,-1,-6,2,-9,-3,-6,2,-2,1,7,2,-3,-2,-10,6,6,-6,-4,8,1,6,6,-1,6,-10,9,2,4,1,-2,-3,2,-1,-2,-2,10,-2,-7,-5,-5,5,-6,8,-1,-3,5,3,7,-6,5,-2,7,1,7,6,-10,5,-7,3,1,-3,2], dtype = "int16")#candidate|4822|(1456,)|const|int16
call_4820 = relay.TupleGetItem(func_2363_call(relay.reshape(var_4821.astype('float32'), [10, 16, 11]), relay.reshape(const_4822.astype('int16'), [1456,]), ), 2)
call_4823 = relay.TupleGetItem(func_2367_call(relay.reshape(var_4821.astype('float32'), [10, 16, 11]), relay.reshape(const_4822.astype('int16'), [1456,]), ), 2)
func_3874_call = mod.get_global_var('func_3874')
func_3876_call = mutated_mod.get_global_var('func_3876')
call_4836 = func_3874_call()
call_4837 = func_3874_call()
func_4210_call = mod.get_global_var('func_4210')
func_4211_call = mutated_mod.get_global_var('func_4211')
call_4842 = relay.TupleGetItem(func_4210_call(), 0)
call_4843 = relay.TupleGetItem(func_4211_call(), 0)
bop_4844 = relay.less(call_4813.astype('bool'), relay.reshape(call_4842.astype('bool'), relay.shape_of(call_4813))) # shape=(11, 11, 8)
bop_4847 = relay.less(call_4814.astype('bool'), relay.reshape(call_4843.astype('bool'), relay.shape_of(call_4814))) # shape=(11, 11, 8)
func_479_call = mod.get_global_var('func_479')
func_482_call = mutated_mod.get_global_var('func_482')
call_4851 = func_479_call(relay.reshape(const_4822.astype('int16'), [8, 14, 13]))
call_4852 = func_479_call(relay.reshape(const_4822.astype('int16'), [8, 14, 13]))
func_3338_call = mod.get_global_var('func_3338')
func_3342_call = mutated_mod.get_global_var('func_3342')
const_4863 = relay.const([[-5.957671],[8.488050],[8.197546],[-2.109849],[3.474706],[-7.526192],[4.649145],[-6.743044],[-3.175743],[5.537838],[-8.861651],[-1.960427],[6.689726],[-1.055678],[6.279088],[0.296254],[8.423535],[1.562945],[-8.472094],[8.424569],[0.258285],[-4.930585],[-4.277459],[-9.312930],[9.085930],[-8.884298],[-2.985345],[-9.530315],[-1.463812],[-3.400738],[1.805525],[-4.968328],[-3.574421],[-9.479097],[2.273522],[-8.971962],[4.001586],[2.778208],[4.239788],[-3.059864],[8.946031],[-3.803792],[1.788066],[-2.032563],[-2.158935],[3.407170],[-0.664039],[-8.857335],[-7.772933],[2.831732],[-7.020052],[-5.101579],[-4.631074],[-4.352795],[-6.595829],[-4.562446],[3.461579],[7.512209],[-1.816651],[6.366672],[-8.179304],[-7.738462],[-0.315093],[2.977060],[5.931873],[-7.314315],[-0.635223],[7.905056],[-4.377886],[1.620700],[7.232590],[1.410908],[-6.715407],[0.723036],[-1.745565],[2.528020],[-8.416921],[2.624465],[-6.035321],[4.697031],[1.978074],[-7.668804],[-1.234769],[-2.920067],[8.375247],[0.888909],[-5.581573],[0.995597],[-7.220826],[7.845491],[7.783029],[6.692151],[-4.537956],[-4.240245],[-4.301320],[5.517718],[6.346862],[9.618263],[1.390676],[4.017649],[3.533421],[9.194599],[0.257274],[1.446353],[-6.508651],[-9.511444],[0.947960],[2.166218],[-6.093173],[3.895621],[9.323271],[-4.124469],[-5.120545],[-4.371570],[8.916541],[-0.430608],[1.985305],[-8.441313],[-7.729613],[-9.297507],[-4.817623],[9.008007],[-3.327916],[-1.844043],[-1.403522],[7.513000],[-8.257644],[3.344295],[-5.521449],[-8.073956],[2.925683],[-5.712389],[1.921880],[3.981327],[-9.557932],[-8.815966],[-1.144450],[8.625501],[-8.921976],[5.097788],[4.661085],[-0.210831],[-3.668685],[-8.371304],[7.494220],[-1.154846],[5.598396],[3.212705],[-5.716579],[-7.934570],[-0.077751],[2.185166],[-1.499791],[-0.952957]], dtype = "float64")#candidate|4863|(154, 1)|const|float64
var_4864 = relay.var("var_4864", dtype = "float64", shape = (224,))#candidate|4864|(224,)|var|float64
var_4865 = relay.var("var_4865", dtype = "uint32", shape = (1232,))#candidate|4865|(1232,)|var|uint32
call_4862 = relay.TupleGetItem(func_3338_call(relay.reshape(const_4863.astype('float64'), [154,]), relay.reshape(var_4864.astype('float64'), [224,]), relay.reshape(var_4865.astype('uint32'), [56, 22]), ), 0)
call_4866 = relay.TupleGetItem(func_3342_call(relay.reshape(const_4863.astype('float64'), [154,]), relay.reshape(var_4864.astype('float64'), [224,]), relay.reshape(var_4865.astype('uint32'), [56, 22]), ), 0)
output = relay.Tuple([call_4820,var_4821,const_4822,call_4836,bop_4844,call_4851,call_4862,const_4863,var_4864,var_4865,])
output2 = relay.Tuple([call_4823,var_4821,const_4822,call_4837,bop_4847,call_4852,call_4866,const_4863,var_4864,var_4865,])
func_4893 = relay.Function([var_4821,var_4864,var_4865,], output)
mod['func_4893'] = func_4893
mod = relay.transform.InferType()(mod)
mutated_mod['func_4893'] = func_4893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mutated_mod.get_global_var('func_4893')
var_4895 = relay.var("var_4895", dtype = "float32", shape = (1760,))#candidate|4895|(1760,)|var|float32
var_4896 = relay.var("var_4896", dtype = "float64", shape = (224,))#candidate|4896|(224,)|var|float64
var_4897 = relay.var("var_4897", dtype = "uint32", shape = (1232,))#candidate|4897|(1232,)|var|uint32
call_4894 = func_4893_call(var_4895,var_4896,var_4897,)
output = call_4894
func_4898 = relay.Function([var_4895,var_4896,var_4897,], output)
mutated_mod['func_4898'] = func_4898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_4949 = relay.TupleGetItem(func_4167_call(), 2)
call_4950 = relay.TupleGetItem(func_4169_call(), 2)
func_4008_call = mod.get_global_var('func_4008')
func_4011_call = mutated_mod.get_global_var('func_4011')
const_4954 = relay.const(8.420899, dtype = "float64")#candidate|4954|()|const|float64
call_4953 = relay.TupleGetItem(func_4008_call(relay.reshape(const_4954.astype('float64'), [])), 3)
call_4955 = relay.TupleGetItem(func_4011_call(relay.reshape(const_4954.astype('float64'), [])), 3)
output = relay.Tuple([call_4949,call_4953,const_4954,])
output2 = relay.Tuple([call_4950,call_4955,const_4954,])
func_4956 = relay.Function([], output)
mod['func_4956'] = func_4956
mod = relay.transform.InferType()(mod)
mutated_mod['func_4956'] = func_4956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4956_call = mutated_mod.get_global_var('func_4956')
call_4957 = func_4956_call()
output = call_4957
func_4958 = relay.Function([], output)
mutated_mod['func_4958'] = func_4958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4956_call = mod.get_global_var('func_4956')
func_4958_call = mutated_mod.get_global_var('func_4958')
call_4968 = relay.TupleGetItem(func_4956_call(), 0)
call_4969 = relay.TupleGetItem(func_4958_call(), 0)
output = relay.Tuple([call_4968,])
output2 = relay.Tuple([call_4969,])
func_4973 = relay.Function([], output)
mod['func_4973'] = func_4973
mod = relay.transform.InferType()(mod)
output = func_4973()
func_4974 = relay.Function([], output)
mutated_mod['func_4974'] = func_4974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5044 = relay.TupleGetItem(func_4167_call(), 2)
call_5045 = relay.TupleGetItem(func_4169_call(), 2)
uop_5049 = relay.log10(call_5044.astype('float64')) # shape=(4, 1, 1)
uop_5051 = relay.log10(call_5045.astype('float64')) # shape=(4, 1, 1)
bop_5052 = relay.logical_xor(uop_5049.astype('uint16'), relay.reshape(call_5044.astype('uint16'), relay.shape_of(uop_5049))) # shape=(4, 1, 1)
bop_5055 = relay.logical_xor(uop_5051.astype('uint16'), relay.reshape(call_5045.astype('uint16'), relay.shape_of(uop_5051))) # shape=(4, 1, 1)
bop_5056 = relay.logical_or(bop_5052.astype('bool'), relay.reshape(uop_5049.astype('bool'), relay.shape_of(bop_5052))) # shape=(4, 1, 1)
bop_5059 = relay.logical_or(bop_5055.astype('bool'), relay.reshape(uop_5051.astype('bool'), relay.shape_of(bop_5055))) # shape=(4, 1, 1)
output = bop_5056
output2 = bop_5059
func_5061 = relay.Function([], output)
mod['func_5061'] = func_5061
mod = relay.transform.InferType()(mod)
output = func_5061()
func_5062 = relay.Function([], output)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5097 = relay.var("var_5097", dtype = "float64", shape = (6, 11, 12))#candidate|5097|(6, 11, 12)|var|float64
uop_5098 = relay.log2(var_5097.astype('float64')) # shape=(6, 11, 12)
func_1912_call = mod.get_global_var('func_1912')
func_1915_call = mutated_mod.get_global_var('func_1915')
var_5104 = relay.var("var_5104", dtype = "int64", shape = (605,))#candidate|5104|(605,)|var|int64
call_5103 = relay.TupleGetItem(func_1912_call(relay.reshape(var_5104.astype('int64'), [11, 11, 5])), 0)
call_5105 = relay.TupleGetItem(func_1915_call(relay.reshape(var_5104.astype('int64'), [11, 11, 5])), 0)
output = relay.Tuple([uop_5098,call_5103,var_5104,])
output2 = relay.Tuple([uop_5098,call_5105,var_5104,])
func_5120 = relay.Function([var_5097,var_5104,], output)
mod['func_5120'] = func_5120
mod = relay.transform.InferType()(mod)
var_5121 = relay.var("var_5121", dtype = "float64", shape = (6, 11, 12))#candidate|5121|(6, 11, 12)|var|float64
var_5122 = relay.var("var_5122", dtype = "int64", shape = (605,))#candidate|5122|(605,)|var|int64
output = func_5120(var_5121,var_5122,)
func_5123 = relay.Function([var_5121,var_5122,], output)
mutated_mod['func_5123'] = func_5123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3957_call = mod.get_global_var('func_3957')
func_3958_call = mutated_mod.get_global_var('func_3958')
call_5147 = relay.TupleGetItem(func_3957_call(), 4)
call_5148 = relay.TupleGetItem(func_3958_call(), 4)
var_5149 = relay.var("var_5149", dtype = "int32", shape = (7, 336))#candidate|5149|(7, 336)|var|int32
bop_5150 = relay.subtract(call_5147.astype('uint8'), relay.reshape(var_5149.astype('uint8'), relay.shape_of(call_5147))) # shape=(7, 336)
bop_5153 = relay.subtract(call_5148.astype('uint8'), relay.reshape(var_5149.astype('uint8'), relay.shape_of(call_5148))) # shape=(7, 336)
bop_5156 = relay.less(var_5149.astype('bool'), relay.reshape(call_5147.astype('bool'), relay.shape_of(var_5149))) # shape=(7, 336)
bop_5159 = relay.less(var_5149.astype('bool'), relay.reshape(call_5148.astype('bool'), relay.shape_of(var_5149))) # shape=(7, 336)
output = relay.Tuple([bop_5150,bop_5156,])
output2 = relay.Tuple([bop_5153,bop_5159,])
func_5163 = relay.Function([var_5149,], output)
mod['func_5163'] = func_5163
mod = relay.transform.InferType()(mod)
var_5164 = relay.var("var_5164", dtype = "int32", shape = (7, 336))#candidate|5164|(7, 336)|var|int32
output = func_5163(var_5164)
func_5165 = relay.Function([var_5164], output)
mutated_mod['func_5165'] = func_5165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5167 = relay.TupleGetItem(func_4167_call(), 0)
call_5168 = relay.TupleGetItem(func_4169_call(), 0)
output = relay.Tuple([call_5167,])
output2 = relay.Tuple([call_5168,])
func_5190 = relay.Function([], output)
mod['func_5190'] = func_5190
mod = relay.transform.InferType()(mod)
output = func_5190()
func_5191 = relay.Function([], output)
mutated_mod['func_5191'] = func_5191
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5205 = relay.var("var_5205", dtype = "uint32", shape = (13, 1, 14))#candidate|5205|(13, 1, 14)|var|uint32
var_5206 = relay.var("var_5206", dtype = "uint32", shape = (13, 11, 14))#candidate|5206|(13, 11, 14)|var|uint32
bop_5207 = relay.minimum(var_5205.astype('uint32'), var_5206.astype('uint32')) # shape=(13, 11, 14)
const_5221 = relay.const([[[-10,4,-1,5,6,1,4,-9,-7,2,-1,-6,9,3],[-4,6,1,7,4,7,-1,-8,-10,-7,-8,-2,-3,-7],[2,2,2,1,7,7,-1,3,-3,-4,-8,3,-9,-6],[-3,-5,-2,2,-7,7,-4,-7,-7,6,9,-4,-2,2],[1,-6,-10,1,9,4,-10,-10,-5,9,5,-3,-7,3],[3,-3,-3,1,1,5,-9,4,2,-4,-10,1,10,4],[-3,9,2,2,-2,-9,9,2,5,-7,-1,3,4,1],[-10,-3,1,8,-5,-9,5,1,1,10,-1,-2,8,6],[-1,-7,-1,1,2,3,2,-8,9,-3,-5,8,-1,-8],[8,-2,10,-8,-10,3,2,3,8,-3,3,9,8,-1],[8,8,5,2,9,-6,-1,-3,5,-7,7,9,-5,-5]],[[-6,1,-8,-9,-9,8,-3,7,3,8,-7,-8,6,-4],[8,3,-10,7,3,2,-6,-2,-7,2,-10,-6,7,1],[3,-2,9,-4,-10,-8,4,-7,-2,-9,7,-9,-2,-3],[-10,2,-2,-6,-2,9,-1,6,-8,-6,-9,9,6,2],[4,-9,-2,10,7,-4,-8,10,-1,-5,-7,-1,-7,4],[-8,-5,4,9,-7,7,-6,-1,-5,4,-5,-6,3,1],[-10,3,-3,-2,-2,-10,-9,1,9,2,4,1,6,-4],[-7,-8,9,-4,-10,9,7,-1,6,4,5,-9,-1,-8],[10,-7,-8,3,-6,2,-5,-10,-10,-1,-4,-4,-10,-9],[5,-9,1,3,8,-7,-5,2,9,4,-2,6,9,-6],[2,1,5,4,3,5,3,10,2,10,2,3,-1,10]],[[8,9,1,9,10,-4,-1,6,3,-6,8,8,-1,3],[-9,-2,-1,9,10,10,3,3,-4,-2,7,-6,5,6],[-5,8,6,-3,10,10,1,-2,-5,10,7,8,9,10],[8,-10,7,-8,-7,-7,-2,8,9,8,4,5,10,-7],[7,-3,-3,9,10,-10,-8,-3,-6,-6,1,-8,3,-8],[7,4,-1,9,9,-4,5,5,1,-6,8,-3,-7,4],[4,-5,-5,5,5,2,1,-2,-7,10,4,6,-7,1],[-10,3,6,7,6,-9,-7,4,6,6,4,3,1,10],[-10,1,-5,-6,-4,-4,4,-1,8,-8,-5,8,-10,7],[-4,-1,-9,6,9,-7,-6,5,-8,-10,-6,-1,-3,-8],[1,4,6,2,8,-1,2,1,-3,-8,5,-9,8,-1]],[[8,2,7,-5,-1,-10,6,7,-9,6,7,5,3,4],[-2,2,4,-9,2,-6,2,-4,-7,-4,1,10,-5,-1],[-9,-2,10,10,8,7,-5,4,10,4,1,4,10,-2],[-9,5,-10,8,1,-5,7,-8,6,-10,10,-2,1,-2],[9,8,-1,-5,-10,-10,-1,9,-9,-2,8,1,-3,-6],[-10,7,-6,-9,-10,5,-7,2,-4,-8,7,-7,-10,-1],[-3,1,-9,3,5,-10,6,6,4,3,-8,-10,1,-10],[-8,-5,-9,-2,-7,4,9,-7,-3,10,1,-5,6,-4],[5,-9,-4,-3,3,3,-2,-9,3,8,9,3,-3,8],[6,-10,5,-5,4,-6,-5,6,-8,-10,3,8,6,-3],[-2,10,-3,10,-10,1,-4,10,7,-9,-10,-7,5,-4]],[[-7,-1,8,-6,4,2,-10,9,-1,-5,6,3,-3,9],[-6,-10,-2,9,-2,2,10,1,7,5,-8,6,4,-10],[-10,4,3,-8,-5,-4,1,-5,8,-2,-6,4,-7,8],[2,8,-6,-9,-6,-2,3,10,-2,6,10,6,6,10],[2,5,-3,-5,7,7,-2,-6,7,-10,10,-8,5,8],[5,5,5,1,-6,8,2,-9,-6,-9,1,-1,-7,-3],[2,6,-1,-5,4,8,-4,-1,6,9,5,5,9,-8],[5,-9,-5,8,-9,-6,-9,-10,3,-9,3,10,-8,-3],[3,1,3,6,-8,-3,7,7,4,-1,1,5,-8,2],[-10,-10,6,-2,5,6,2,10,1,-9,7,3,8,1],[-2,1,-8,6,6,3,-6,7,-8,-1,-6,-3,8,2]],[[3,1,8,1,5,-2,-5,-2,-3,1,8,2,10,-9],[-1,-6,4,-4,-9,10,10,5,-8,6,-8,5,-1,-9],[2,1,9,-2,3,7,8,-8,-1,4,1,-1,9,4],[2,-10,1,10,9,5,7,-5,-9,-3,-5,-2,-9,3],[8,9,-3,6,2,-4,-9,4,10,9,2,2,9,4],[-6,7,6,-7,6,-3,-3,-9,7,-8,-3,-8,1,4],[3,-9,7,-4,3,-2,-7,7,-3,2,-2,-6,-7,3],[2,7,5,6,-3,7,-4,-5,7,10,-10,9,-1,8],[7,6,-9,7,-1,8,-5,-8,-5,9,4,-1,10,-6],[-2,10,6,-9,1,8,10,5,-10,-4,5,8,-3,-6],[8,-5,-6,10,-3,4,-6,5,8,-1,3,3,1,9]],[[-10,-8,-7,-7,-7,5,-7,-3,3,10,8,-10,-7,10],[4,-1,-6,-3,1,6,-8,-10,-1,-9,-1,-6,10,-1],[-8,-4,-10,-7,5,9,-9,-6,5,-1,2,-3,-8,-3],[2,5,3,-2,-8,9,-8,-9,-5,-3,4,-9,7,9],[-10,4,-4,-1,2,-2,-4,-4,-1,-1,-10,9,10,10],[1,-5,-2,2,-1,5,-8,-4,9,-7,2,9,2,-8],[7,2,-9,-6,5,1,10,-9,-4,-3,2,-5,5,8],[5,2,6,-9,-10,-8,-2,-10,6,5,2,-4,5,1],[-5,-9,-5,-2,2,7,-6,-6,-5,-3,6,10,-5,6],[-4,-1,-6,-1,9,1,3,-5,5,9,8,1,-1,3],[5,-7,-6,10,-9,2,-4,-1,-3,8,-10,7,1,5]],[[1,10,-9,7,-3,7,7,2,-4,-10,1,-6,5,10],[-3,9,-3,10,-6,-7,-3,1,-6,5,5,-9,-3,9],[10,5,-4,-7,-5,-1,5,10,-4,2,-5,2,-10,8],[7,3,-7,-3,5,2,-9,1,-2,-4,5,8,10,-9],[2,4,-7,1,5,6,3,2,-10,-8,5,1,-5,-9],[1,-5,-7,6,-8,-7,8,5,-9,7,-9,4,-4,-5],[3,4,-3,-1,-2,6,4,4,-7,5,-5,7,-5,9],[5,-10,7,-4,-5,-1,-2,8,10,-7,-1,5,7,2],[-3,3,5,8,-7,10,-9,-10,8,8,2,-5,10,-10],[3,8,3,4,5,9,4,6,2,6,-6,10,-2,2],[4,-8,4,-3,-9,6,-10,-6,6,-10,9,-8,10,4]],[[2,5,-8,5,1,8,6,6,8,-10,5,3,-8,1],[-1,-2,-1,-1,10,-10,3,-2,3,-4,-1,7,8,10],[-5,6,7,10,-6,6,6,-8,-5,1,10,3,2,7],[-2,-8,9,-2,5,-6,-3,-7,-10,2,-9,5,10,1],[8,4,9,8,7,6,-3,2,-5,-9,-6,-10,5,4],[-5,-7,-7,6,4,-3,5,-4,-10,-6,-5,-9,5,-8],[9,6,-9,9,-4,3,9,1,-5,-2,-9,-1,-3,-7],[-2,-9,-7,4,-7,-5,10,-1,3,-4,-6,5,-7,2],[-1,-8,-4,-5,-3,-8,-4,1,10,-6,5,1,-8,-9],[-7,7,-3,-10,-4,-9,-3,-7,-9,-2,4,2,-8,3],[3,3,4,-7,-6,4,-3,-9,10,-5,6,-2,7,-10]],[[-8,5,4,3,-9,-6,1,-7,3,-3,3,5,-9,-2],[10,-3,4,2,-5,5,-7,-1,1,5,5,10,-7,-9],[-2,3,10,4,4,-1,3,3,7,10,-1,3,-2,3],[-9,-6,-3,5,-4,7,-7,7,4,-1,5,10,-8,-1],[7,-2,8,7,6,5,3,10,-2,-9,10,-9,1,10],[-4,10,6,-6,-9,-6,-7,6,4,-7,6,5,5,-8],[3,4,8,-9,-5,1,-1,10,7,-7,4,9,1,-6],[6,-1,-4,8,-10,-8,-3,-10,3,2,5,-3,3,-9],[-4,1,10,10,-8,6,7,-6,1,7,-3,6,-6,9],[10,6,-2,5,8,4,6,-5,-3,5,6,-8,9,-8],[-2,6,2,6,-8,8,10,1,3,1,6,8,8,-10]],[[-7,-3,3,10,3,1,-1,-5,-2,-7,2,-9,-3,-8],[-2,-7,-7,9,-4,-7,-7,8,9,6,-10,6,-2,2],[-1,-6,9,3,8,5,-1,8,-3,5,-10,5,6,3],[6,3,6,-2,5,-2,-9,4,1,9,6,8,-5,-7],[-4,-8,8,8,1,10,7,-8,10,6,3,9,-9,7],[-10,6,-7,-4,6,-10,4,-2,1,-9,1,4,1,5],[-10,6,7,6,6,8,4,6,7,10,9,10,-5,6],[-10,7,-1,2,5,-3,-7,-3,-8,-10,-9,4,-10,-10],[1,-4,-8,2,6,-9,-1,-3,3,1,5,8,-4,3],[-9,2,10,-10,6,8,-6,-4,9,-7,-1,6,2,1],[-8,-1,-7,6,8,8,8,6,2,10,7,-6,6,6]],[[9,5,10,-4,-10,6,6,1,-9,7,9,7,-5,-4],[-6,-10,-6,2,-4,4,-9,-3,6,1,3,9,7,7],[8,2,4,8,-10,7,-9,7,5,2,-6,-7,3,10],[-1,-2,10,4,8,5,4,-2,-5,8,-1,-9,5,5],[-3,8,3,2,3,-9,-10,1,-6,-5,-5,1,5,-2],[-8,-6,3,-5,-3,-4,-5,-1,9,6,-6,8,-6,-9],[9,-9,10,7,1,-4,1,3,10,10,8,7,-9,-7],[-4,-5,-8,1,4,-3,-2,-1,4,-8,10,6,-7,1],[-7,-2,5,-3,4,2,4,2,2,-8,9,-3,-5,6],[1,10,10,-1,9,-9,-10,10,-6,-9,-8,-7,2,-8],[10,-10,3,-10,-2,-7,7,-6,7,-10,-10,3,5,-5]],[[-1,-7,-6,3,9,-2,4,-1,-7,7,-3,-7,5,1],[2,-8,-8,6,-2,-5,2,-1,9,9,-9,10,-5,-6],[-8,2,-2,3,-5,-4,-7,7,6,-10,-2,-1,-7,-4],[9,-3,-7,-5,5,-7,-8,-7,-9,6,4,2,-5,8],[5,4,-2,-1,4,-5,5,-7,-4,7,1,-1,-1,1],[-8,-10,1,-7,3,-1,3,5,-10,10,-9,9,4,6],[-3,-3,-8,-3,1,3,9,2,-1,-1,-9,5,10,1],[4,-1,-6,7,1,2,-2,-5,-8,3,4,-10,-7,-3],[1,-2,3,1,2,-3,7,-3,2,-10,-5,-2,8,-3],[1,3,10,-6,-1,-2,4,-5,5,-10,10,-9,-2,5],[5,5,2,5,-5,8,-7,-10,8,-9,-5,-9,-6,1]]], dtype = "uint32")#candidate|5221|(13, 11, 14)|const|uint32
bop_5222 = relay.bitwise_xor(var_5206.astype('uint32'), relay.reshape(const_5221.astype('uint32'), relay.shape_of(var_5206))) # shape=(13, 11, 14)
bop_5227 = relay.divide(var_5206.astype('float32'), relay.reshape(bop_5207.astype('float32'), relay.shape_of(var_5206))) # shape=(13, 11, 14)
func_3760_call = mod.get_global_var('func_3760')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_5230 = func_3760_call()
call_5231 = func_3760_call()
var_5234 = relay.var("var_5234", dtype = "uint32", shape = (13, 15, 14))#candidate|5234|(13, 15, 14)|var|uint32
bop_5235 = relay.left_shift(var_5205.astype('uint16'), var_5234.astype('uint16')) # shape=(13, 15, 14)
func_3213_call = mod.get_global_var('func_3213')
func_3216_call = mutated_mod.get_global_var('func_3216')
var_5243 = relay.var("var_5243", dtype = "float32", shape = (1760,))#candidate|5243|(1760,)|var|float32
var_5244 = relay.var("var_5244", dtype = "int16", shape = (1456,))#candidate|5244|(1456,)|var|int16
call_5242 = relay.TupleGetItem(func_3213_call(relay.reshape(var_5243.astype('float32'), [1760,]), relay.reshape(var_5244.astype('int16'), [1456,]), ), 3)
call_5245 = relay.TupleGetItem(func_3216_call(relay.reshape(var_5243.astype('float32'), [1760,]), relay.reshape(var_5244.astype('int16'), [1456,]), ), 3)
output = relay.Tuple([bop_5222,bop_5227,call_5230,bop_5235,call_5242,var_5243,var_5244,])
output2 = relay.Tuple([bop_5222,bop_5227,call_5231,bop_5235,call_5245,var_5243,var_5244,])
func_5260 = relay.Function([var_5205,var_5206,var_5234,var_5243,var_5244,], output)
mod['func_5260'] = func_5260
mod = relay.transform.InferType()(mod)
var_5261 = relay.var("var_5261", dtype = "uint32", shape = (13, 1, 14))#candidate|5261|(13, 1, 14)|var|uint32
var_5262 = relay.var("var_5262", dtype = "uint32", shape = (13, 11, 14))#candidate|5262|(13, 11, 14)|var|uint32
var_5263 = relay.var("var_5263", dtype = "uint32", shape = (13, 15, 14))#candidate|5263|(13, 15, 14)|var|uint32
var_5264 = relay.var("var_5264", dtype = "float32", shape = (1760,))#candidate|5264|(1760,)|var|float32
var_5265 = relay.var("var_5265", dtype = "int16", shape = (1456,))#candidate|5265|(1456,)|var|int16
output = func_5260(var_5261,var_5262,var_5263,var_5264,var_5265,)
func_5266 = relay.Function([var_5261,var_5262,var_5263,var_5264,var_5265,], output)
mutated_mod['func_5266'] = func_5266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4973_call = mod.get_global_var('func_4973')
func_4974_call = mutated_mod.get_global_var('func_4974')
call_5290 = relay.TupleGetItem(func_4973_call(), 0)
call_5291 = relay.TupleGetItem(func_4974_call(), 0)
func_5163_call = mod.get_global_var('func_5163')
func_5165_call = mutated_mod.get_global_var('func_5165')
const_5302 = relay.const([3,-1,-1,-4,-7,3,-7,5,10,-10,10,-8,-5,-6,-2,-4,10,-1,-4,-5,3,-6,2,-2,-1,-1,4,-4,8,3,6,4,-5,-8,-10,-10,5,-5,7,-9,-10,9,-10,2,2,10,5,3,-9,-8,8,-1,-6,-7,-4,3,-9,-7,-7,8,6,-7,-2,-10,-3,-9,10,1,-8,1,7,7,6,4,5,-3,10,2,10,2,-2,-4,2,-10,-4,-2,5,-6,5,4,-1,-9,-7,-2,2,-10,-4,-9,-10,7,-10,-4,10,5,9,5,6,-3,-4,-10,9,-1,2,1,8,7,-1,-2,2,-6,7,-3,5,6,10,-6,-5,6,-8,1,-7,6,9,8,-5,4,-6,-5,-2,-2,8,-5,-6,2,8,-2,2,-10,7,-4,-2,6,-5,1,-1,-4,-3,-2,8,3,-9,-8,6,-4,5,7,6,7,4,1,-3,6,3,-4,-4,-6,5,-4,1,-4,-5,6,-6,-3,1,6,8,-1,-2,2,6,-8,10,-2,9,-1,-8,-4,-10,-5,-10,6,-2,8,5,-1,6,2,1,-10,1,-7,-6,3,9,-6,10,-8,2,8,6,8,9,1,-3,2,-10,-3,1,4,-6,10,4,-10,-4,4,6,-3,2,-6,-4,-9,9,-3,-1,-2,-7,5,-8,10,1,-3,5,-3,1,2,-10,-2,-4,-1,9,-2,-4,8,1,-6,-1,1,-9,5,-6,7,-7,-6,1,-5,-1,-9,-5,-8,6,-7,5,4,-4,5,-5,9,9,-4,5,5,8,2,2,8,-6,-6,4,-6,-1,10,3,-8,7,5,9,7,-5,-1,-10,6,5,-8,5,9,5,10,9,10,-7,-7,8,-6,-4,1,-5,10,10,8,4,-1,-7,8,-8,3,5,6,5,-6,10,-2,6,-6,2,4,-1,4,6,7,2,1,-1,3,-8,6,-8,-4,2,1,-6,-7,-9,-7,5,-1,4,-4,-7,-3,-6,5,-7,8,-9,-1,-5,-1,1,1,4,3,-4,-2,-4,7,2,-3,3,6,2,8,-8,-6,-9,-7,9,-10,8,3,7,-3,-4,-7,10,8,3,-3,-6,-1,6,-5,-9,9,7,1,-5,-2,-3,-5,-4,-6,10,-7,-8,1,-8,2,-1,7,6,1,-4,-10,2,9,10,-3,7,-7,10,-3,-6,8,-8,7,-4,-5,3,-5,-3,-3,4,-5,5,7,2,4,7,-5,-6,10,1,8,3,1,10,6,7,4,-3,-9,-3,3,6,8,8,-4,3,5,5,-1,9,8,1,9,-5,1,3,1,-9,3,-6,10,-9,7,-10,-1,-8,-4,3,2,-4,-9,6,8,10,5,-10,-7,-10,5,5,-1,-8,-1,-10,2,-8,3,-10,9,4,-6,-9,-3,9,2,-7,6,-8,6,-10,4,-9,1,-9,1,-4,-6,-2,-3,9,5,-8,1,10,8,8,-9,10,-10,10,-10,10,9,-5,5,10,9,-2,8,10,3,7,-4,-2,3,6,8,1,10,-4,1,-4,3,-3,-8,-4,-10,3,-9,-10,6,-8,-4,2,5,6,9,6,-7,-3,-3,-6,-2,-7,-1,-3,-3,-1,-10,-10,8,-10,-7,1,7,-9,-4,1,3,7,7,2,1,-8,4,-3,-3,9,1,-3,5,9,6,-5,2,-2,-10,-8,6,1,3,4,8,7,5,-10,-10,2,-10,5,-7,-10,1,-1,5,1,-7,-5,10,6,2,8,6,-9,6,-10,-1,1,10,1,3,5,-6,-5,-4,4,9,-7,-1,-1,10,-10,-2,5,3,1,-9,-6,-9,-3,-3,1,6,-7,6,-2,9,-9,2,-7,3,3,-4,-9,3,8,-9,-8,-8,-2,2,1,7,-4,-6,-8,-7,-1,1,6,1,9,-4,5,-3,4,-2,-9,-7,-1,-4,-1,9,5,-1,-5,-6,4,-3,-10,5,-2,-1,7,-5,-10,-7,-1,-3,10,7,8,-2,-3,-1,-1,-1,5,-5,-1,-3,9,-1,10,-7,10,8,7,-2,4,5,2,-10,7,1,6,-8,6,5,5,-6,8,-7,-3,7,-4,5,-8,3,2,3,8,5,5,9,4,9,1,-6,6,-4,-6,6,-5,9,-3,-7,8,-4,-2,2,-8,7,-6,-6,6,5,-10,-4,-2,-4,9,-5,-3,-7,1,10,-10,-9,-8,1,6,6,8,2,-4,4,-2,-8,7,-10,7,-8,-7,-7,3,-10,5,4,5,1,6,3,-4,3,-8,-10,4,-6,-6,-5,3,7,-9,-9,-10,-6,-8,6,-1,3,-3,6,4,8,7,8,-9,7,-9,4,1,-8,8,10,5,9,-8,-5,9,2,-7,7,9,-3,4,-8,7,1,1,3,5,-4,-6,-7,2,-2,-2,-4,5,-9,-7,4,-4,7,8,-3,-1,8,-6,2,-6,1,-3,9,4,-7,-7,-3,5,8,2,-6,8,10,-1,-6,-7,3,1,10,-1,6,-7,1,-1,-5,2,-5,7,6,8,-3,8,6,9,7,-2,-10,-2,-1,1,7,1,-4,9,-6,-2,3,6,-9,5,7,-9,-6,-7,5,5,9,-5,-4,-1,-3,-1,4,6,-2,-9,8,-5,10,-3,8,-8,6,10,-8,-2,5,-7,-1,-4,4,4,-3,8,1,-8,-1,-7,-10,7,-1,10,4,-7,-2,2,4,10,6,-9,-1,-9,-5,-7,7,-4,-7,-6,-4,10,4,2,9,-5,1,-6,-3,5,3,-3,-8,-9,-1,-9,-8,1,-10,-9,-6,-6,8,-9,8,9,6,2,-8,2,-5,-4,-8,6,7,-9,-10,10,-8,1,3,-7,-3,-4,9,-10,-6,1,7,-2,-3,-7,-5,-2,-6,-6,4,-1,-2,10,10,8,-4,10,6,-6,-2,-1,2,9,-6,-8,-10,-9,-3,-4,9,-10,2,-4,1,-5,-5,-9,10,4,3,-6,10,-5,-4,-7,-4,-6,9,3,2,-3,6,5,-10,-2,4,7,-5,8,-3,4,3,2,-2,2,-6,-2,-6,8,9,-10,10,-6,10,-6,-2,-8,10,7,-8,-5,-3,-7,-5,7,-7,-8,4,3,9,-5,-8,6,-7,-10,-3,9,4,-4,-3,5,-8,6,-7,6,-8,7,-7,6,7,9,2,5,-4,-5,2,4,2,-1,-10,-7,9,-4,8,-10,-7,6,-7,-5,9,-5,-1,2,2,4,-2,10,-6,10,6,10,9,5,6,4,-2,-8,-1,-8,-6,4,-5,9,-9,-7,9,8,-3,3,-3,-7,-9,9,5,-4,4,-9,2,-2,9,8,7,7,1,1,6,-10,-5,4,8,3,5,3,-1,10,4,-9,6,-3,5,-10,4,-5,-8,-10,-6,10,-4,9,-8,7,-7,-3,4,9,-9,-10,6,1,4,-4,-2,-10,-9,-4,-9,1,1,8,-1,7,-5,-3,2,-7,-5,7,-7,-6,7,3,4,2,9,5,9,10,-8,-5,6,9,4,1,-4,-8,-10,4,7,1,6,-4,7,8,-8,10,-4,-7,6,10,6,8,10,-2,-8,1,-1,10,2,7,-1,-3,-7,-5,-10,-4,4,-4,6,1,3,1,-10,3,-6,-9,-7,-4,-5,-9,4,3,5,-4,7,6,-7,3,-5,7,-5,10,1,8,3,-10,9,6,-3,5,-6,-8,-8,-10,7,6,-6,-6,2,-4,9,1,7,2,-10,2,9,-10,-2,10,8,1,-4,-2,3,1,-9,-2,2,10,2,-9,-1,8,9,-1,5,2,3,6,-1,-7,-9,-1,-2,4,-1,7,-4,-5,4,-2,2,-10,10,-10,-1,3,6,1,-5,4,-10,7,-7,-6,8,1,4,2,7,6,1,-8,-5,6,5,-3,-2,-10,-3,-1,-6,9,-6,-3,5,1,-1,4,7,4,-10,9,-9,3,7,3,8,3,-6,-9,6,-8,8,-10,10,6,-3,3,6,-6,-10,6,2,6,-6,9,-4,6,9,-6,2,-10,-9,-10,9,-7,4,10,5,-4,-10,10,1,3,-3,-8,3,1,1,6,-7,10,8,-1,-6,1,-9,-10,-10,8,-4,-10,4,-8,5,6,8,-7,-8,7,-3,-1,-3,1,-6,7,-5,8,10,-8,-9,-7,2,3,-2,7,-1,6,-1,-7,5,-8,3,-4,1,6,-8,-7,8,-4,10,-6,10,-7,8,-10,10,-7,-4,-5,-5,-5,7,3,3,6,9,-6,-3,-1,-9,-5,-9,-3,3,7,1,1,7,-3,-1,4,2,-10,3,5,-2,-2,-1,3,-2,-4,-6,3,8,2,7,-9,7,4,-1,-3,-9,6,-7,6,1,4,-2,1,-3,9,-10,-10,10,-7,5,5,-5,4,2,-3,9,-2,-4,-2,5,-10,-2,2,-6,-4,-8,-5,-2,7,10,-8,-9,1,-1,-4,-4,1,-5,-9,-1,4,-4,6,-1,-9,-5,1,7,-7,6,-7,6,-10,3,3,-2,7,9,1,6,-2,-7,3,6,-4,-3,-7,-1,3,-6,-9,-5,-2,10,4,-3,5,9,6,1,-2,-3,5,-5,9,5,8,6,4,-3,-2,-5,8,6,-1,-6,-1,-1,-6,-5,8,4,-9,5,-6,2,-7,-4,2,9,-5,6,5,-10,-4,7,-4,7,1,7,-2,-5,7,-4,-7,2,-9,8,6,6,-5,-9,3,-2,-9,10,-9,10,4,7,-6,-3,-9,-10,9,2,-10,2,-8,6,5,-9,-2,-2,-1,-8,-2,-6,2,-4,4,4,9,-7,-10,6,-10,-2,2,-1,-5,-1,-1,-7,-5,-5,-9,4,7,-6,-4,-4,5,-9,10,-1,-8,-1,1,4,-9,4,-8,-7,-10,1,5,-10,-1,-7,-8,3,1,7,-4,-8,9,-2,-2,1,-9,-6,10,-7,5,-10,-2,-1,1,-7,-8,-9,-8,-6,-7,2,1,-4,-6,-2,3,-3,6,-10,-3,-9,1,-10,8,-9,2,5,-1,-4,8,-9,-5,7,-8,6,5,2,7,7,7,2,-9,-1,-4,9,-1,4,-1,-7,10,-10,-3,3,4,5,7,-1,2,7,8,-9,-4,-5,4,4,5,10,-8,-8,-4,4,-8,-8,-6,8,2,-1,10,1,-7,-1,1,-2,6,-1,-3,-4,7,-3,8,7,1,-6,5,7,4,-4,-9,4,-6,-8,10,-4,-5,-2,-10,-4,-8,-2,-8,2,-4,7,-5,-1,-5,-2,2,-2,2,-1,-2,3,-5,-2,1,5,2,-1,4,-8,10,4,5,-10,-9,-1,-7,-2,9,-7,7,10,-5,-6,2,8,5,5,-7,9,7,8,6,8,3,10,7,-1,10,9,-3,-5,8,-8,-6,-10,9,-8,-5,2,2,-8,-9,-1,-8,10,-7,8,6,8,-3,4,-6,6,-3,-9,-10,3,-8,10,-5,7,-7,7,1,3,6,7,-4,-5,-1,1,5,-3,-8,-1,5,-9,3,6,-3,-9,10,3,8,10,-4,5,5,-2,-2,10,-1,2,6,9,10,-10,-5,-4,-3,-6,-5,6,-8,-7,-3,2,7,-7,3,-2,-5,3,7,5,-2,-9,-10,1,5,-2,6,-2,9,5,7,-7,10,-4,-7,-7,10,10,-2,1,8,6,9,-6,-9,-2,-8,3,-1,5,6,9,-9,-7,9,-8,3,-2,6,-1,-10,-3,4,-6,-3,-2,-2,-6,-9,2,2,8,8,8,-1,8,1,-10,7,7,9,-8,2,2,8,-1,7,-6,1,-8,-2,-4,8,-10,-1,5,-8,-1,-9,-2,-8,-7,-4,2,8,10,6,7,-9,1,5,10,-8,-4,5,-2,-10,-9,-6,2,1,-6,-5,3,9,3,-7,-7,-3,2,6,-10,4,3,-10,-4,6,-8,-4,-2,-4,-8,8,-5,-6,-9,-10,-1,2,-6,8,3,-1,-2,3,-9,8,9,-3,-9,1,3,8,-10,7,-3,6,-6,9,4,-1,1,2,-7,4,6,-3,1,-3,4,-6,5,-2,-9,-9,7,7,1,-9,6,6,3,1,3,-4,3,1,-2,-9,8,-5,7,-4,-5,9,-6,-3,4,-2,7,-1,6,8,-9,-10,-4,3,-8,2,-9,5,5,4,-10,-8,2,9,3,7,-6,-8,-3,4,7,-7,6,-2,9,-2,-2,-8,-10,-6,6,-5,-10,3,-6,-5,2,9,-3,10,-7,-1,-3,-7,7,7,9,-6,-9,-2,-5,-9,-10,-6,9,7,8,-9,8,-5,-1,6,8,-9,-2,-1,-2,5,-9], dtype = "int32")#candidate|5302|(2352,)|const|int32
call_5301 = relay.TupleGetItem(func_5163_call(relay.reshape(const_5302.astype('int32'), [7, 336])), 1)
call_5303 = relay.TupleGetItem(func_5165_call(relay.reshape(const_5302.astype('int32'), [7, 336])), 1)
output = relay.Tuple([call_5290,call_5301,const_5302,])
output2 = relay.Tuple([call_5291,call_5303,const_5302,])
func_5308 = relay.Function([], output)
mod['func_5308'] = func_5308
mod = relay.transform.InferType()(mod)
output = func_5308()
func_5309 = relay.Function([], output)
mutated_mod['func_5309'] = func_5309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3419_call = mutated_mod.get_global_var('func_3419')
call_5326 = func_3418_call()
call_5327 = func_3418_call()
output = call_5326
output2 = call_5327
func_5331 = relay.Function([], output)
mod['func_5331'] = func_5331
mod = relay.transform.InferType()(mod)
output = func_5331()
func_5332 = relay.Function([], output)
mutated_mod['func_5332'] = func_5332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5061_call = mod.get_global_var('func_5061')
func_5062_call = mutated_mod.get_global_var('func_5062')
call_5407 = func_5061_call()
call_5408 = func_5061_call()
uop_5410 = relay.cosh(call_5407.astype('float64')) # shape=(4, 1, 1)
uop_5412 = relay.cosh(call_5408.astype('float64')) # shape=(4, 1, 1)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_5415 = relay.TupleGetItem(func_4167_call(), 1)
call_5416 = relay.TupleGetItem(func_4169_call(), 1)
uop_5417 = relay.cosh(call_5415.astype('float64')) # shape=(11, 11, 8)
uop_5419 = relay.cosh(call_5416.astype('float64')) # shape=(11, 11, 8)
func_4686_call = mod.get_global_var('func_4686')
func_4693_call = mutated_mod.get_global_var('func_4693')
const_5421 = relay.const([5.533927,9.004495,-7.068205,-8.669580,-4.597467,6.088018,-2.776974,4.202933,2.381891,3.404321,2.552517,4.854129,-7.254509,-7.610875,-9.065256,-4.031440,9.533417,-5.638856,-2.610756,-4.972138,-0.187103,0.911877,8.446128,5.852733,-7.652259,6.380094,9.477546,-3.051651,5.963837,8.916840,-8.306693,5.917463,-7.815753,-8.335515,-7.562568,8.239905,-7.452347,-7.435105,7.712571,7.118017,-9.945016,-9.670752,1.069743,8.535882,8.674306,-2.960640,-7.358844,7.240295,5.866171,1.279714,-3.316512,-4.162536,5.408362,0.954829,-4.648672,3.839179,1.948804,4.917105,-7.768637,0.943545,7.761421,8.917107,-5.762070,-2.859453,-5.471975,0.303403,-2.841820,-5.040931,-0.505749,7.654064,-9.129903,7.741473,-5.410943,-3.259267,8.656928,-4.044230,-0.919601,-2.873418,-0.507648,-3.586956,3.566896,9.993190,-6.405297,3.076750,0.381678,6.049474,5.600633,8.392244,7.256364,-3.973192,-1.844754,-5.704031,7.108006,8.068801,7.173859,-6.009916,3.579233,5.168638,0.183768,8.167096,4.746028,-3.116761,0.181735,-6.728112,-5.847902,-3.109357,6.783432,8.159961,3.666602,-0.901774,-2.631497,2.145557,-3.232437,7.098863,-1.500688,7.031018,-8.004825,-0.230959,2.670463,-7.677086,-6.336844,-2.234860,1.576003,-8.691379,-5.600610,-8.187785,5.381744,4.736811,-5.551324,-3.519275,1.135479,-9.077281,7.916316,0.894818,3.511303,-4.902523,-0.587260,6.280448,-5.230684,3.721134,-5.028374,-7.712415,3.417794,0.463785,-7.102509,-9.668779,1.785162,6.905895,-2.476850,-1.252432,1.769595,0.468692,3.810379,9.288478], dtype = "float64")#candidate|5421|(154,)|const|float64
var_5422 = relay.var("var_5422", dtype = "float64", shape = (224,))#candidate|5422|(224,)|var|float64
var_5423 = relay.var("var_5423", dtype = "uint32", shape = (4, 308))#candidate|5423|(4, 308)|var|uint32
const_5424 = relay.const([-1,8,4,-5,1,-7,-5,5,-6,10,-6,-4,-9,-2,-4,-5,-4,6,-10,-1,10,7,-6,-3,-5,-10,3,7,-10,6,-2,8,-3,3,5,6,2,3,8,-2,-6,-5,6,-10,1,-10,-7,8,-5,5,7,-7,7,-8,-5,-9,3,-1,-5,3,9,10,2,-5,-1,8,2,-8,5,-3,8,-3,-7,8,-7,10,6,1,-8,-4,-7,-8,8,-7,3,5,-3,2,5,3,-1,-10,-3,-5,-9,1,-3,-6,-6,-8,-2,-10,-1,6,2,-8,2,-2,-8,7,9,-3,8,5,-2,-5,-6,-3,9,3,-9,-6,10,6,-4,7,-5,-8,-2,9,6,10,10,10,-1,1,-5,-10,5,-5,3,2,4,10,-5,-10,2,-4,3,2,-7,3,7,9,3,1,-7,3,5,7,-4,-10,7,1,-7,4,-5,6,-2,6,-8,-1,-1,8,10,7,-2,-4,-10,9,-9,1,-9,6,9,-9,8,-4,6,7,7,4,1,-10,-5,10,1,-8,8,4,-7,-8,2,-5,4,-8,6,-4,-10,-9,3,-8,3,-5,-1,10,-1,-2,8,3,7,-7,-3,-1,-7,-9,10,-3,5,-3,6,-4,-10,9,-4,-4,-6,-6,-3,-4,-5,-9,4,9,-1,-8,4,3,8,3,-6,3,-9,-3,-5,-3,1,7,-5,9,-7,-6,-8,-6,-2,-10,-8,-2,-3,-9,3,-9,3,2,-10,-7,-7,-9,-1,3,6,6,8,10,3,10,-1,-10,2,-2,4,-1,-2,8,-5,-9,-6,-4,-10,-8,6,-1,-8,9,5,-4,3,-10,4,-8,-10,-2,1,3,-10,6,-10,3,10,-7,7,5,-7,-5,-2,-1,-2,-9,9,-4,-2,7,9,-9,3,-3,-9,10,-3,8,10,10,-2,-4,-2,4,-3,7,2,-1,3,-3,4,6,-10,5,-4,1,5,-1,-8,-10,-5,-10,-4,-9,-7,-7,8,10,-10,8,-1,1,6,4,4,-4,-2,5,-7,1,9,-7,-3,-6,2,-6,5,-3,-9,5,-1,-4,3,-9,6,-4,-7,-3,-8,3,1,4,-7,6,-4,-9,2,-9,5,-7,7,-3,4,5,4,-1,7,10,-4,8,-1,-2,2,-10,-9,-5,10,-9,5,6,1,-4,-7,-2,3,9,-9,-9,-4,10,-7,8,-5,4,4,-1,1,5,2,-9,7,10,-10,-9,-7,-8,3,4,6,10,-9,-4,8,8,-7,6,-4,-10,-5,-7,-7,7,-2,8,8,-5,-2,-7,8,-2,-10,-9,-5,9,7,4,-2,3,-3,-1,10,-8,-4,-3,-10,-9,3,7,8,-2,5,-10,9,2,-4,-5,-8,7,9,8,6,2,-7,7,-8,-10,-5,1,-4,9,5,-2,-8,8,-2,-9,-4,-6,-1,-8,-4,-1,1,-6,-4,-2,-9,-3,-7,4,-7,-6,3,6,8,4,-2,-2,6,7,3,10,-6,-8,-6,-10,5,-6,1,4,-5,1,1,10,1,1,7,-5,6,3,6,-7,-3,-9,4,-2,-10,-6,-6,2,4,-5,-5,-3,4,5,3,-10,4,9,-3,-6,-5,7,1,-3,3,5,6,8,-7,-1,4,7,3,5,8,-10,-8,-6,-6,-1,5,-4,-7,5,5,6,-7,7,-10,5,-6,3,-2,2,-8,-7,-10,-7,7,-10,-8,-4,-9,3,3,-9,5,-4,3,-6,-8,7,6,-4,-6,7,-1,8,-10,-1,-3,4,4,-4,4,9,3,-10,2,3,-8,-3,-9,-1,4,-4,4,-4,5,-7,-5,1,-2,8,6,-1,10,-5,7,-10,10,9,-1,4,8,-7,6,3,-10,4,-10,10,1,3,-3,-10,-6,-9,-1,-2,-2,3,8,10,7,-6,8,-1,3,-8,4,9,8,-6,9,-1,-7,-3,-2,-5,-4,8,-6,3,-10,4,-1,-3,-1,10,-4,-4,-5,8,-7,-6,3,-5,10,6,10,-3,5,2,2,-9,-2,9,-8,-7,-1,8,-7,-1,-2,9,9,1,-8,3,4,8,2,5,6,7,-7,9,9,-4,-9,10,-5,-5,5,-2,-7,-9,8,1,8,-1,-6,-10,2,-5,-7,10,-10,-2,2,-6,-6,10,-8,8,-10,2,1,10,-6,-4,-1,-2,3,6,1,4,8,1,-6,4,10,-1,-10,4,-7,-6,7,9,-5,5,8,3,-5,4,5,-9,-5,-6,3,-10,2,-9,7,9,7,-8,-3,-3,-5,-2,-6,-5,-1,-8,3,-5,4,-4,-5,3,-6,7,1,-10,8,7,4,4,5,10,-10,2,10,-4,-8,-7,7,-6,3,-7,9,-4,5,8,2,7,2,5,-5,7,8,-10,7,5,1,2,5,-2,-3,-2,6,-6,-9,10,-4,9,-2,-8,2,-10,5,-2,-5,-5,-5,-5,6,-9,4,1,8,-9,9,-9,3,8,9,-10,-6,-7,10,2,-3,3,2,-7,-5,1,6,-7,-7,-4,-6,-3,9,-3,-1,-9,8,4,-5,10,-9,-6,-1,1,7,-8,-2,-5,-10,4,-3,-8,4,-1,-4,8,4,-8,6,-6,-7,-8,-5,1,-1,-9,-7,-3,2,9,5,-9,3,5,-9,6,3,-4,-9,6,-2,-2,3,-10,-9,10,10,4,-9,7,-8,-1,-9,1,-9,-7,9,10,7,6,-2,-2,6,-8,-5,-10,-9,5,-5,3,-1,-7,-2,-4,-8,4,7,-2,4,-7,-4,3,9,1,-4,9,7,-8,2,5,-4,-8,9,-3,2,1,8,-9,-1,10,7,1,-5,10,-10,-5,-7,5,-5,-10,-2,-2,6,7,4,-3,7,4,2,9,-10,-8,1,5,-4,4,-8,4,10,1,1,6,9,-9,-3,-3,-5,3,4,2,5,-4,2,6,1,7,-3,-9,-2,-3,9,9,-9,-9,-2,-1,-7,-1,2,3,7,5,-3,-2,3,10,-3,7,1,5,7,2,10,4,-1,7,-7,7,7,2,7,3,1,4,-5,7,4,7,3,7,-10,-9,9,4,-7,7,10,-6,1,5,8,10,-3,7,2,-9,10,-7,6,-2,-10,9,-10,-1,4,7,-9,-3,5,8,3,10,-5,-10,-10,6,-3,2,-7,-4,-10,-2,-9,-1,2,-4,7,8,-10,-5,-5,2,3,1,6,2,8,3,8,4,3,4,-1,-2,-3,3,5,5,-9,9,-4,9,4,1,-8,-1,-2,-1,-9,6,-1,9,-4,5,3,-9,4,2,4,1,8,-2,-8,3,-9,3,-10,5,9,7,5,-2,6,8,-7,1,-10,-8,-8,-8,-2,7,3,5,-4,-5,-2,10,1,9,5,-7,-3,-5,-8,9,4,-3,10,1,2,-6,5,4,2,-5,-1,3,-7,-8,1,-6,-5,-4,-9,-2,-10,-5,2,10,3,10,10,-10,2,-4,5,-8,1,5,6,10,4,1,-7,10,6,3,-5,-5,-1,2,10,-4,3,-10,-7,-4,-6,-6,6,2,-8,-10,-8,-2,5,-4,-5,6,8,-6,6,5,-5,-6,7,-4,5,-9,-8,-3,-6,-8,3,-2,1,5,10,-1,1,7,-9,2,-5,-6,-6,6,4,-5,-7,8,-7,-7,-3,3,8,-1,-10,-9,-5,-8,6,5,7,8,8,-3,-1,1,9,-7,5,1,10,-10,7,-8,-3,2,2,5,-8,-5,9,10,-2,-4,-4,10,-7,10,10,8,8,5,-1,-10,-9,5,-10,5,-3,-7,-3,10,-1,3,-6,-7,10,4,10,-8,8,-8,-10,10,-1,-10,-6,-4,9,-8,-8,-1,7,-10,1,8,3,10,9,7,-1,-6,-5,5,8,1,8,-6,9,-4,6,-2,7,10], dtype = "int16")#candidate|5424|(1456,)|const|int16
const_5425 = relay.const(-2.056069, dtype = "float64")#candidate|5425|()|const|float64
call_5420 = relay.TupleGetItem(func_4686_call(relay.reshape(call_5415.astype('float32'), [11, 11, 8]), relay.reshape(const_5421.astype('float64'), [154,]), relay.reshape(var_5422.astype('float64'), [224,]), relay.reshape(var_5423.astype('uint32'), [1232,]), relay.reshape(const_5424.astype('int16'), [1456, 1]), relay.reshape(const_5425.astype('float64'), []), ), 7)
call_5426 = relay.TupleGetItem(func_4693_call(relay.reshape(call_5415.astype('float32'), [11, 11, 8]), relay.reshape(const_5421.astype('float64'), [154,]), relay.reshape(var_5422.astype('float64'), [224,]), relay.reshape(var_5423.astype('uint32'), [1232,]), relay.reshape(const_5424.astype('int16'), [1456, 1]), relay.reshape(const_5425.astype('float64'), []), ), 7)
output = relay.Tuple([uop_5410,uop_5417,call_5420,const_5421,var_5422,var_5423,const_5424,const_5425,])
output2 = relay.Tuple([uop_5412,uop_5419,call_5426,const_5421,var_5422,var_5423,const_5424,const_5425,])
func_5430 = relay.Function([var_5422,var_5423,], output)
mod['func_5430'] = func_5430
mod = relay.transform.InferType()(mod)
mutated_mod['func_5430'] = func_5430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5430_call = mutated_mod.get_global_var('func_5430')
var_5432 = relay.var("var_5432", dtype = "float64", shape = (224,))#candidate|5432|(224,)|var|float64
var_5433 = relay.var("var_5433", dtype = "uint32", shape = (4, 308))#candidate|5433|(4, 308)|var|uint32
call_5431 = func_5430_call(var_5432,var_5433,)
output = call_5431
func_5434 = relay.Function([var_5432,var_5433,], output)
mutated_mod['func_5434'] = func_5434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_5464 = relay.TupleGetItem(func_3862_call(), 0)
call_5465 = relay.TupleGetItem(func_3863_call(), 0)
var_5479 = relay.var("var_5479", dtype = "float32", shape = (11, 11, 8))#candidate|5479|(11, 11, 8)|var|float32
bop_5480 = relay.logical_and(call_5464.astype('bool'), relay.reshape(var_5479.astype('bool'), relay.shape_of(call_5464))) # shape=(11, 11, 8)
bop_5483 = relay.logical_and(call_5465.astype('bool'), relay.reshape(var_5479.astype('bool'), relay.shape_of(call_5465))) # shape=(11, 11, 8)
output = relay.Tuple([bop_5480,])
output2 = relay.Tuple([bop_5483,])
func_5487 = relay.Function([var_5479,], output)
mod['func_5487'] = func_5487
mod = relay.transform.InferType()(mod)
var_5488 = relay.var("var_5488", dtype = "float32", shape = (11, 11, 8))#candidate|5488|(11, 11, 8)|var|float32
output = func_5487(var_5488)
func_5489 = relay.Function([var_5488], output)
mutated_mod['func_5489'] = func_5489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3760_call = mod.get_global_var('func_3760')
func_3761_call = mutated_mod.get_global_var('func_3761')
call_5593 = func_3760_call()
call_5594 = func_3760_call()
func_3507_call = mod.get_global_var('func_3507')
func_3509_call = mutated_mod.get_global_var('func_3509')
call_5601 = func_3507_call()
call_5602 = func_3507_call()
func_242_call = mod.get_global_var('func_242')
func_246_call = mutated_mod.get_global_var('func_246')
var_5605 = relay.var("var_5605", dtype = "float64", shape = (224,))#candidate|5605|(224,)|var|float64
const_5606 = relay.const([6,-10,7,-5,2,-9,4,-9,-1,9,-1,5,-7,-2,-7,-10,-6,-6,-6,8,-6,-10,-2,1,3,7,-6,-9,-5,2,1,5,-4,10,3,8,6,-10,-9,4,-8,8,-1,-9,-8,-10,-2,-8,-5,-4,10,-8,4,-5,-8,6,7,-1,1,-9,-2,-1,4,-9,-10,7,-9,-4,-10,7,-7,-5,-9,5,8,-10,-2,3,10,5,6,-10,5,-7,5,5,9,8,-6,-9,-8,-3,1,8,-9,-3,-3,2,-9,4,-5,7,7,-3,10,-7,2,-3,-7,6,4,-3,-4,-6,5,8,9,5,3,-10,9,-5,7,-4,7,-4,-9,9,-3,-8,-4,-8,4,-10,-3,-1,-6,-5,-2,-1,9,1,10,3,4,-2,8,3,7,-6,-4,5,3,4,1,4,9,-1,-5,4,4,8,-10,-1,-4,7,5,-9,6,-4,9,8,-5,-8,-1,-10,10,8,-10,-9,7,-4,10,3,-5,2,6,1,-8,4,3,6,-3,-5,3,-9,10,7,5,7,-8,5,10,7,-8,7,4,-7,6,-10,-6,1,2,-9,7,-10,-4,1,2,-1,-1,-4,-10,4,2,6,4,-7,5,-5,1,-9,10,-10,10,-5,-10,7,-9,-7,-6,-3,2,9,6,-2,-7,2,3,-2,-3,-5,7,2,-5,-10,-2,3,3,-1,-4,-5,-4,-10,9,9,2,-3,-7,8,-4,5,1,9,-8,2,5,-4,-6,-7,10,-7,1,-3,6,2,-10,-5,-3,-5,-7,4,6,-3,6,-7,6,-1,5,7,7,-1,-4,-8,-3,9,-1,3,5,-2,-6,9,5,10,6,-1,-5,-8,1,8,-10,-7,4,-10,6,1,-3,3,-2,9,-10,-9,-5,6,4,1,4,6,-5,-8,10,-4,-4,2,2,4,-2,-9,-1,-2,-10,8,8,-2,2,-8,3,-7,9,-1,-3,-2,-7,1,-7,-2,5,-1,-5,9,-4,2,-9,4,-2,-10,9,1,5,3,-6,-9,8,7,-4,3,-5,7,7,3,-6,4,7,1,-9,5,3,8,3,-7,2,-7,6,-9,5,2,-7,7,4,-7,6,8,-6,-1,10,8,-9,-6,-8,7,9,5,8,9,3,4,-7,-9,7,-4,9,8,4,2,-1,7,10,9,7,-1,5,8,-8,-5,-8,-1,-10,2,4,-7,-2,-8,-8,4,4,-6,1,-1,2,3,6,4,4,9,1,-3,-2,-7,8,8,7,1,9,-6,-9,-10,4,10,-1,5,6,-4,1,-1,-3,10,-6,-7,-4,-5,-3,-7,-10,-4,-5,2,1,2,-1,2,5,-5,5,-3,4,-2,-4,3,-4,-4,8,-2,3,-2,8,-8,5,1,5,1,-3,-6,9,-8,6,6,7,-4,2,7,-9,-1,8,6,-8,-3,-7,-6,8,-3,-8,-10,-7,-7,10,8,-9,-4,3,-10,-7,1,-2,2,3,-4,-4,-5,-9,-9,8,-8,6,-4,2,-9,-7,-2,-7,6,-2,2,5,9,2,4,-5,7,-4,10,4,-2,-2,-9,3,-1,-6,-2,-2,8,9,6,-2,-3,5,-2,-5,-2,-1,5,6,8,1,-4,1,9,-2,1,-9,2,-2,-4,9,3,7,-3,-8,-5,-2,-1,1,-2,4,-10,-2,8,-9,10,-8,-9,2,10,-4,8,5,1,-1,2,-10,10,-7,5,-1,-3,9,6,5,-3,10,-6,-3,5,-2,9,9,4,-8,-9,6,-7,-5,8,8,8,-3,5,1,-9,-6,3,-8,9,-7,-4,-2,8,4,7,9,2,-2,-7,-6,6,-5,-5,-7,8,5,-7,-4,6,4,10,3,-5,-8,7,-9,5,-1,6,9,2,-9,-2,-7,-1,-6,-4,2,3,2,-5,1,4,4,-10,5,6,-4,-4,-1,-1,5,-5,5,-8,-7,5,-7,-10,8,-2,5,-6,8,-9,5,7,5,1,-9,-6,-4,-4,9,-1,-7,9,-5,-8,-5,4,-7,3,3,4,3,-8,-9,9,10,7,5,7,3,2,2,-9,7,3,-6,-1,6,-7,4,5,7,1,-9,1,6,9,1,1,10,5,-2,2,-8,5,6,-7,-3,7,1,-4,-3,-6,-1,-2,2,4,6,2,-6,5,6,-6,-2,-10,3,9,5,10,-2,-6,2,8,5,-3,6,6,1,8,-5,6,2,-3,3,-2,8,9,7,9,7,6,9,3,4,-3,2,8,-9,1,-4,6,3,3,5,6,5,7,-4,4,-4,6,10,-1,4,-10,-7,2,6,-3,-1,-4,9,-10,4,10,3,-5,1,-4,10,-7,2,10,-7,10,-10,-4,-8,3,-8,-1,2,-6,3,-1,-3,1,-8,-5,4,2,-4,6,-1,-5,3,-2,1,9,7,9,6,7,-3,-10,-2,10,1,7,4,-10,7,3,9,5,3,6,-6,-5,7,-3,-8,-2,-10,10,2,-2,-4,-10,10,-9,-1,-2,7,-3,3,-3,10,1,-6,-3,-2,1,3,-9,9,6,2,-5,7,5,-4,2,-4,4,-7,2,4,-7,7,10,5,-3,3,-6,-6,10,-9,-5,-9,-7,-8,8,-2,-8,1,4,1,-3,-7,-7,-9,-4,1,-3,10,7,-1,-7,9,4,3,-8,-5,-1,9,7,4,10,3,-8,-5,9,1,9,-3,-2,10,3,10,-10,-1,-8,-8,-2,2,-4,-6,-3,8,7,-6,10,-8,3,-6,-8,10,3,4,9,-7,5,5,-8,-1,-6,3,-2,8,8,8,10,2,8,-1,6,-9,1,8,-8,-4,5,-2,-8,-2,-4,-4,8,10,-4,2,-10,8,8,-1,-6,-3,-2,-7,5,9,-10,4,9,-6,8,10,1,-1,7,-5,7,-1,3,3,7,-7,-7,5,-8,8,8,-6,-9,10,-9,6,-3,6,6,5,-3,8,-7,5,-3,3,-2,-2,4,-4,5,8,8,-7,5,-6,8,8,9,1,8,-3,3,-9,5,1,-5,1,4,6,2,10,5,5,5,6,-2,-2,-4,3,6,1,-4,3,-2,9,-10,-6,-9,9,-1,-7,-5,9,10,1,7,-5,6,-10,6,4,8,-1,5,3,6,-10,-9,-10,-2,-2,3,-1,-7,9,10,-7,5,7,7,-5,-10,-4,3,-7,-5,5,8,8,9,-7,3,7,-4,-8,-6,6,8,-4,-3,6,-10,7,1,3,3,8,6,3,-2,2,6,4,7,-2,7,-10,1,6,5,1,-1], dtype = "uint32")#candidate|5606|(1232,)|const|uint32
call_5604 = relay.TupleGetItem(func_242_call(relay.reshape(var_5605.astype('float64'), [16, 7, 2]), relay.reshape(const_5606.astype('uint32'), [1232,]), relay.reshape(const_5606.astype('uint32'), [11, 16, 7]), ), 2)
call_5607 = relay.TupleGetItem(func_246_call(relay.reshape(var_5605.astype('float64'), [16, 7, 2]), relay.reshape(const_5606.astype('uint32'), [1232,]), relay.reshape(const_5606.astype('uint32'), [11, 16, 7]), ), 2)
bop_5613 = relay.equal(call_5593.astype('bool'), relay.reshape(call_5601.astype('bool'), relay.shape_of(call_5593))) # shape=(11, 11, 8)
bop_5616 = relay.equal(call_5594.astype('bool'), relay.reshape(call_5602.astype('bool'), relay.shape_of(call_5594))) # shape=(11, 11, 8)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_5622 = relay.TupleGetItem(func_3862_call(), 0)
call_5623 = relay.TupleGetItem(func_3863_call(), 0)
output = relay.Tuple([call_5604,var_5605,const_5606,bop_5613,call_5622,])
output2 = relay.Tuple([call_5607,var_5605,const_5606,bop_5616,call_5623,])
func_5630 = relay.Function([var_5605,], output)
mod['func_5630'] = func_5630
mod = relay.transform.InferType()(mod)
var_5631 = relay.var("var_5631", dtype = "float64", shape = (224,))#candidate|5631|(224,)|var|float64
output = func_5630(var_5631)
func_5632 = relay.Function([var_5631], output)
mutated_mod['func_5632'] = func_5632
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4973_call = mod.get_global_var('func_4973')
func_4974_call = mutated_mod.get_global_var('func_4974')
call_5637 = relay.TupleGetItem(func_4973_call(), 0)
call_5638 = relay.TupleGetItem(func_4974_call(), 0)
uop_5646 = relay.rsqrt(call_5637.astype('float32')) # shape=(4, 1, 1)
uop_5648 = relay.rsqrt(call_5638.astype('float32')) # shape=(4, 1, 1)
uop_5657 = relay.sin(uop_5646.astype('float32')) # shape=(4, 1, 1)
uop_5659 = relay.sin(uop_5648.astype('float32')) # shape=(4, 1, 1)
uop_5662 = relay.sigmoid(uop_5657.astype('float32')) # shape=(4, 1, 1)
uop_5664 = relay.sigmoid(uop_5659.astype('float32')) # shape=(4, 1, 1)
uop_5666 = relay.sinh(uop_5646.astype('float64')) # shape=(4, 1, 1)
uop_5668 = relay.sinh(uop_5648.astype('float64')) # shape=(4, 1, 1)
output = relay.Tuple([uop_5662,uop_5666,])
output2 = relay.Tuple([uop_5664,uop_5668,])
func_5673 = relay.Function([], output)
mod['func_5673'] = func_5673
mod = relay.transform.InferType()(mod)
output = func_5673()
func_5674 = relay.Function([], output)
mutated_mod['func_5674'] = func_5674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5061_call = mod.get_global_var('func_5061')
func_5062_call = mutated_mod.get_global_var('func_5062')
call_5689 = func_5061_call()
call_5690 = func_5061_call()
uop_5692 = relay.acosh(call_5689.astype('float32')) # shape=(4, 1, 1)
uop_5694 = relay.acosh(call_5690.astype('float32')) # shape=(4, 1, 1)
output = uop_5692
output2 = uop_5694
func_5699 = relay.Function([], output)
mod['func_5699'] = func_5699
mod = relay.transform.InferType()(mod)
mutated_mod['func_5699'] = func_5699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5699_call = mutated_mod.get_global_var('func_5699')
call_5700 = func_5699_call()
output = call_5700
func_5701 = relay.Function([], output)
mutated_mod['func_5701'] = func_5701
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5712 = relay.var("var_5712", dtype = "int32", shape = (10, 1, 5))#candidate|5712|(10, 1, 5)|var|int32
const_5713 = relay.const([[[9,-7,-9,1,-2],[1,-3,-5,7,5],[9,-8,-10,-10,-5],[3,4,-10,8,10],[-8,-9,1,-9,8],[-10,-5,-9,-7,8],[-9,-8,2,9,-9],[-9,8,-9,-5,-9],[4,9,6,-4,6],[-8,4,9,4,-5],[5,-2,-5,-5,-1],[1,-2,5,-8,-4],[1,-9,-8,3,6],[-6,4,-5,-1,7],[-5,-7,9,-8,1]],[[9,-3,-8,-7,-4],[-9,-4,-10,-9,-1],[5,7,4,4,-2],[3,-6,2,-7,7],[3,-2,6,-8,-3],[5,7,-9,-9,3],[7,-5,-2,9,9],[1,-1,-9,-6,-3],[-7,8,2,3,10],[3,3,2,-6,-5],[6,-6,-10,3,-3],[-7,-7,-2,-2,-10],[-2,2,10,1,5],[-2,-3,-10,-5,-10],[-1,7,-2,9,-6]],[[6,2,5,2,-10],[1,9,-2,6,-2],[-6,-3,-3,1,-9],[-10,7,5,-6,8],[-3,9,3,-1,-9],[-5,-5,7,3,9],[9,9,3,-9,-10],[-4,6,-6,-7,5],[-9,-4,-9,4,10],[-6,-5,6,8,7],[-2,4,8,-4,9],[4,2,-4,-8,-4],[6,-9,4,10,-1],[-3,-2,1,-7,7],[-6,3,7,-10,-10]],[[3,-4,-6,8,-10],[5,-1,10,-6,-9],[-4,4,-3,-7,-5],[-7,2,3,-10,5],[1,5,8,-6,-4],[-9,-9,6,-3,-7],[9,-9,7,-10,-6],[-9,7,-8,1,1],[-8,6,3,-9,6],[-7,2,-7,-9,-6],[-1,1,-10,3,5],[-9,-6,10,8,8],[-7,-10,-2,-10,3],[7,2,2,-8,-5],[10,-6,10,10,7]],[[-3,-2,7,-1,6],[-4,2,10,2,-10],[1,-1,-8,4,1],[5,-10,-9,2,6],[6,10,8,1,-6],[-6,-10,-3,-10,-8],[10,2,-10,-7,-1],[-10,-2,6,-10,1],[7,-4,-6,9,6],[4,-1,-6,-7,5],[3,-6,8,7,10],[-4,5,8,-5,-7],[4,-6,8,-10,-2],[-5,-4,4,-5,-10],[8,4,1,7,8]],[[-8,-3,-9,-6,-8],[-6,7,-3,2,1],[3,-5,5,8,4],[5,-10,8,-1,-10],[5,9,-6,3,10],[-9,3,3,-9,-1],[-9,-7,-5,10,-1],[5,8,10,-6,-3],[8,3,-3,-1,-7],[5,9,7,-9,9],[9,6,10,1,-8],[4,4,7,-6,-2],[-3,1,9,5,6],[7,-10,1,6,5],[8,-2,-9,-2,9]],[[9,10,-3,7,6],[2,7,6,-9,1],[8,3,4,1,8],[7,-2,-5,-6,3],[-8,-7,4,-4,-8],[8,8,8,-7,5],[8,1,9,-7,10],[8,2,4,9,-2],[7,-4,5,-5,10],[-6,-2,-10,-2,-5],[-6,2,-8,-5,-4],[-7,9,6,-3,6],[10,4,8,-4,-1],[-5,-2,5,1,9],[9,8,7,-3,6]],[[-6,1,10,-3,2],[-3,-9,3,-5,5],[2,1,-5,-6,1],[-8,-8,-6,-10,3],[3,8,1,7,6],[1,8,-9,-4,-1],[-9,-3,-10,7,8],[-4,6,-2,-5,-2],[-2,10,6,-5,6],[-5,-5,-4,-9,-8],[1,-7,-6,-3,-9],[4,7,-5,3,3],[-6,-6,9,7,-9],[5,9,-6,-3,5],[-1,7,-3,2,2]],[[7,6,-8,-3,4],[-2,-3,-3,5,7],[1,-9,7,1,-9],[-5,-1,-10,-9,-8],[7,2,-2,-7,2],[-6,-4,-1,8,10],[-7,4,9,10,8],[-9,-9,-3,5,-5],[5,-9,-8,-10,4],[-2,7,10,-1,-2],[-8,4,-1,6,8],[-4,-5,-4,7,9],[-3,2,-8,-4,3],[-8,6,-8,-8,4],[8,-10,4,5,-7]],[[-3,-7,8,9,2],[5,-5,-1,-9,-9],[-4,-2,-9,-10,10],[-3,6,7,-3,6],[-2,-7,-4,-10,-7],[6,8,-10,6,5],[5,-6,6,-5,-4],[8,1,-3,-6,-8],[3,-6,1,10,-4],[-3,1,-2,-7,-7],[7,6,-3,-3,-3],[-9,2,-7,-1,-2],[2,-6,9,1,4],[-8,5,6,-3,4],[9,-2,1,6,6]]], dtype = "int32")#candidate|5713|(10, 15, 5)|const|int32
bop_5714 = relay.not_equal(var_5712.astype('bool'), const_5713.astype('bool')) # shape=(10, 15, 5)
func_1912_call = mod.get_global_var('func_1912')
func_1915_call = mutated_mod.get_global_var('func_1915')
const_5719 = relay.const([-9,8,5,10,5,3,9,5,-7,-4,-2,1,-7,-5,-4,-8,9,6,9,1,-2,-8,-2,-1,-5,-1,7,6,7,-6,10,-3,-9,3,7,-2,8,9,4,-8,6,-5,5,8,3,-10,-7,1,2,-4,6,9,7,-6,10,1,5,-1,-7,2,-3,2,7,-6,5,-9,5,9,-6,4,-10,3,10,8,5,5,2,9,-1,8,4,-9,5,-10,4,6,8,-1,-5,6,-9,-1,-10,-2,-5,9,10,-8,-7,-6,4,-4,3,-3,-4,-10,3,4,4,-6,-8,8,-4,-3,-9,-3,10,9,3,-4,2,10,7,-9,-1,10,10,7,8,-7,6,-10,-7,4,1,-7,-3,-8,-2,-1,-2,4,3,-5,9,6,10,-6,6,-7,5,10,2,10,5,-8,-4,-8,-2,-6,3,-8,1,-1,1,4,5,-8,3,2,-7,6,3,-8,7,7,7,4,-9,-5,-5,10,2,-7,-4,-3,-9,4,-3,10,8,9,-5,7,7,6,-10,2,-4,7,7,-3,-10,-10,-1,2,-8,-9,3,-6,-8,2,1,-8,-2,7,6,6,6,9,-4,1,4,-4,-5,-1,3,1,-9,10,-3,-9,-6,-4,-10,-2,-6,6,-2,-10,1,2,-7,9,-1,5,8,2,8,-6,1,-3,-2,8,1,3,-1,3,7,2,-3,-1,-3,-4,-10,-1,2,-7,-5,10,-5,6,-9,4,5,3,4,-8,8,-8,-4,-7,-5,1,-1,7,-4,-2,6,-9,3,-6,8,4,5,2,4,-6,-6,-10,5,-3,-2,4,-4,-6,6,5,-7,-10,2,-4,3,-5,6,-6,-5,-2,5,-5,-8,5,5,10,1,-6,1,-1,-9,-1,-4,-6,5,5,5,-8,-1,8,5,9,7,-10,7,-1,8,1,-9,2,-6,-6,7,3,1,5,9,-3,-3,-5,2,7,7,3,-5,-2,2,-2,-3,8,-6,9,10,4,-3,-4,-2,-7,6,-5,-5,-4,4,-7,-8,-1,9,-2,2,-2,4,1,6,-4,-8,-5,-7,-1,2,-10,-4,-7,-10,1,6,8,9,5,-7,-10,-10,-9,4,10,9,-8,-2,5,-5,-6,10,-8,-3,-6,2,7,-9,-10,8,10,-1,-2,5,-9,-6,1,10,6,-4,4,-6,-7,7,9,7,-5,-10,-3,6,3,-6,-7,6,10,6,4,-4,9,10,9,9,-8,-2,-2,-5,-2,1,-7,-3,-5,-2,-10,-1,8,-7,1,-10,5,-1,2,-3,-7,4,-9,3,-5,-4,3,-6,-7,7,-10,-6,-1,-1,-3,7,-9,5,7,4,7,7,-3,9,5,-7,-5,10,-2,-10,9,6,-6,8,1,5,1,-7,4,-6,4,-6,10,6,10,6,3,7,-5,3,8,5,2,8,8,7,-1,2,2,3,5,-9,-3,8,-3,5,10,3,-2,8,-6,3,-1,-9,4,-4,3,-5,-10,-8,5,6,-5,-9,-1,8,-3,7,7,-6,-9,-8,-4,3,-10,-8,-4,2,3,-8,-8,4,-1,-7,6,-9,-6,9,4,5,-5,-10,-7,-10,-4,7,-7,5,-1,-8,8,5,-4,5,8,-1], dtype = "int64")#candidate|5719|(605,)|const|int64
call_5718 = relay.TupleGetItem(func_1912_call(relay.reshape(const_5719.astype('int64'), [11, 11, 5])), 0)
call_5720 = relay.TupleGetItem(func_1915_call(relay.reshape(const_5719.astype('int64'), [11, 11, 5])), 0)
uop_5721 = relay.sigmoid(var_5712.astype('float64')) # shape=(10, 1, 5)
bop_5724 = relay.add(uop_5721.astype('uint16'), bop_5714.astype('uint16')) # shape=(10, 15, 5)
var_5738 = relay.var("var_5738", dtype = "int64", shape = (11, 11, 5))#candidate|5738|(11, 11, 5)|var|int64
bop_5739 = relay.left_shift(call_5718.astype('int16'), relay.reshape(var_5738.astype('int16'), relay.shape_of(call_5718))) # shape=(11, 11, 5)
bop_5742 = relay.left_shift(call_5720.astype('int16'), relay.reshape(var_5738.astype('int16'), relay.shape_of(call_5720))) # shape=(11, 11, 5)
output = relay.Tuple([const_5719,bop_5724,bop_5739,])
output2 = relay.Tuple([const_5719,bop_5724,bop_5742,])
func_5744 = relay.Function([var_5712,var_5738,], output)
mod['func_5744'] = func_5744
mod = relay.transform.InferType()(mod)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5744_call = mutated_mod.get_global_var('func_5744')
var_5746 = relay.var("var_5746", dtype = "int32", shape = (10, 1, 5))#candidate|5746|(10, 1, 5)|var|int32
var_5747 = relay.var("var_5747", dtype = "int64", shape = (11, 11, 5))#candidate|5747|(11, 11, 5)|var|int64
call_5745 = func_5744_call(var_5746,var_5747,)
output = call_5745
func_5748 = relay.Function([var_5746,var_5747,], output)
mutated_mod['func_5748'] = func_5748
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5794 = relay.const([[[-8],[5],[-7],[1],[-6],[-8],[4],[-6],[-3],[-7],[-6],[-10],[-6]],[[10],[-5],[-9],[-9],[4],[-9],[9],[-3],[2],[7],[6],[-10],[10]],[[1],[3],[-1],[3],[-1],[8],[1],[7],[-6],[7],[3],[7],[-5]],[[2],[6],[-3],[4],[-6],[10],[-10],[6],[-2],[9],[-6],[6],[-4]],[[-3],[3],[-6],[5],[-8],[2],[-4],[-4],[10],[5],[3],[2],[7]],[[-9],[-3],[3],[6],[4],[-2],[-5],[-7],[10],[-5],[-8],[-10],[2]],[[2],[-9],[2],[-3],[-3],[-3],[-2],[-2],[-7],[-5],[-5],[-8],[9]],[[7],[8],[-5],[1],[-9],[-2],[-2],[-9],[-5],[-1],[7],[3],[2]]], dtype = "int8")#candidate|5794|(8, 13, 1)|const|int8
const_5795 = relay.const([[[8,3,5,3,4,-6,9],[-7,2,-3,9,3,1,10],[-3,3,-10,5,2,7,-1],[10,10,10,-5,10,-8,2],[8,5,8,1,6,5,-5],[3,5,6,1,9,3,-2],[4,-10,-5,-6,-3,-10,4],[-5,8,-4,1,10,8,-10],[1,-1,5,9,-8,-2,1],[-10,-9,-1,4,10,7,-1],[-9,7,-10,-5,2,6,7],[3,-2,-3,9,-6,1,-2],[5,-5,-4,-2,-1,-1,1]],[[2,-5,-7,7,6,4,-3],[-9,5,-8,-8,-3,7,7],[6,5,-7,-3,5,-4,10],[-6,-7,7,9,-2,-8,-7],[-6,4,4,2,-10,-8,6],[10,2,-8,1,10,-3,-8],[7,9,-2,7,-4,7,-5],[1,-7,-9,6,-9,-5,10],[-1,-10,-4,2,-1,1,-8],[-9,5,4,10,-2,-1,5],[8,-3,-2,7,-1,1,6],[7,-10,6,-4,-7,2,-1],[10,8,-1,-9,5,8,-3]],[[-5,-1,-4,9,-4,10,9],[1,-6,8,-9,8,-10,3],[6,7,6,6,-8,-10,9],[-4,-4,8,3,8,3,-9],[-9,-2,-8,-8,8,-4,10],[9,-6,8,5,3,-4,-2],[-7,3,-5,10,-6,8,2],[-10,-8,4,9,5,9,-4],[7,1,8,9,-9,-9,-5],[8,-10,4,7,-1,9,2],[4,-1,3,6,-6,-9,1],[-7,-6,6,3,-4,-7,9],[-3,-1,9,9,-6,7,9]],[[4,-3,-6,7,-5,-3,3],[7,5,-2,-8,-10,3,1],[7,-6,-10,3,-10,-10,-3],[3,5,7,-2,6,-10,-7],[4,4,10,4,1,-5,-10],[-5,10,-8,-9,-4,-3,-9],[1,-7,5,-6,-1,2,10],[2,-4,2,4,10,-4,-4],[-7,2,-8,2,-8,8,-1],[-3,10,10,4,-10,1,-4],[6,-1,-1,-10,-2,6,-5],[1,-7,-6,2,2,7,6],[2,2,-8,-1,-8,1,5]],[[1,-10,-5,-9,-3,-10,-6],[-7,-4,4,6,-1,-2,8],[-8,-9,-5,1,7,5,-10],[-8,-2,1,-3,2,-9,-6],[1,-4,-9,9,-5,7,10],[-5,5,-7,8,2,4,-1],[-6,-6,3,5,-5,9,5],[-6,-6,-3,4,-9,-1,4],[-5,-10,3,8,-6,-1,9],[2,4,7,9,-2,-4,-5],[-3,8,-3,-1,-4,4,1],[-10,-3,-4,-2,-8,5,-4],[-4,1,6,-7,10,7,6]],[[4,7,10,8,-1,-7,1],[-1,-10,-2,4,2,10,9],[6,9,3,-5,7,6,-6],[-7,4,2,4,-5,-3,-10],[-9,-10,-4,-8,-6,9,6],[3,8,-9,-1,6,-4,-6],[10,-9,4,-7,-2,-5,-5],[4,-10,5,1,2,-4,7],[-1,-4,8,-1,7,-1,10],[7,-2,9,2,-10,10,2],[10,2,2,-4,3,3,3],[9,1,9,9,-7,-3,-1],[-9,-7,-4,-4,-6,5,4]],[[-9,3,10,-4,-1,-8,3],[5,4,-6,-5,-9,7,7],[-3,1,8,10,1,-7,-6],[-9,6,-2,8,-1,-10,-1],[-4,-10,-9,-10,6,3,5],[-8,-4,-9,-10,1,9,-2],[10,6,2,-4,-7,-8,-6],[10,2,2,4,-8,-2,-4],[-9,-10,10,5,-3,4,3],[3,-6,1,-1,-6,4,-1],[1,7,-2,8,-4,7,-4],[-7,5,-8,-5,9,-2,10],[8,-2,9,-10,-6,-6,-3]],[[-10,-3,4,9,1,1,-9],[-6,10,-2,-5,-2,5,-3],[-2,3,-3,-1,6,-1,5],[8,6,4,-2,-8,1,-1],[-8,5,-1,2,-7,-3,4],[-10,5,-4,6,4,-8,4],[-2,6,-9,2,9,8,-8],[9,-4,-2,10,9,-7,3],[-7,5,-2,-9,-1,-5,-6],[6,-3,-7,-7,5,6,3],[-8,9,3,-5,4,-8,-5],[-7,3,5,10,2,-1,-3],[2,2,-4,5,6,4,2]]], dtype = "int8")#candidate|5795|(8, 13, 7)|const|int8
bop_5796 = relay.bitwise_xor(const_5794.astype('int8'), const_5795.astype('int8')) # shape=(8, 13, 7)
bop_5813 = relay.mod(const_5795.astype('float64'), relay.reshape(bop_5796.astype('float64'), relay.shape_of(const_5795))) # shape=(8, 13, 7)
output = relay.Tuple([bop_5813,])
output2 = relay.Tuple([bop_5813,])
func_5818 = relay.Function([], output)
mod['func_5818'] = func_5818
mod = relay.transform.InferType()(mod)
mutated_mod['func_5818'] = func_5818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mutated_mod.get_global_var('func_5818')
call_5819 = func_5818_call()
output = call_5819
func_5820 = relay.Function([], output)
mutated_mod['func_5820'] = func_5820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5820_call = mutated_mod.get_global_var('func_5820')
call_5845 = relay.TupleGetItem(func_5818_call(), 0)
call_5846 = relay.TupleGetItem(func_5820_call(), 0)
func_41_call = mod.get_global_var('func_41')
func_44_call = mutated_mod.get_global_var('func_44')
const_5873 = relay.const([8,-2,-1,-2,-1,10,8,-6,10,-3,3,-6,1,6,-3,-3,-2,-3,-1,-9,9,6,-3,-6,2,-6,7,9,5,2,-10,-8,-3,-5,-6,-9,-6,-4,-7,2,10,-6,7,-8,5,-10,-6,7,-9,-6,-9,-10,1,-3,-6,10,2,4,-5,4,2,-5,10,8,4,-4,10,-9,-10,9,-9,4,7,3,-10,-2,-8,-1,-8,-10,4,7,-10,4,1,7,-4,-3,9,-5,-2,-1,5,-3,-10,3,-6,9,9,5,-9,-1,-3,8,-2,-1,1,7,4,6,4,10,-4,-6,-4,-2,-5,-8,9,2], dtype = "uint64")#candidate|5873|(120,)|const|uint64
call_5872 = relay.TupleGetItem(func_41_call(relay.reshape(const_5873.astype('uint64'), [8, 5, 3]), relay.reshape(const_5873.astype('uint64'), [8, 5, 3]), ), 0)
call_5874 = relay.TupleGetItem(func_44_call(relay.reshape(const_5873.astype('uint64'), [8, 5, 3]), relay.reshape(const_5873.astype('uint64'), [8, 5, 3]), ), 0)
output = relay.Tuple([call_5845,call_5872,const_5873,])
output2 = relay.Tuple([call_5846,call_5874,const_5873,])
func_5906 = relay.Function([], output)
mod['func_5906'] = func_5906
mod = relay.transform.InferType()(mod)
output = func_5906()
func_5907 = relay.Function([], output)
mutated_mod['func_5907'] = func_5907
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5908 = relay.const([[[0.835395,7.920737,-7.685301,-2.069455,-4.437656,-6.162134,7.651875,5.144216,-8.185019,-8.755244,-0.628391,-2.453920,-2.274945,-4.521585],[6.663465,-6.000779,8.725033,1.655908,-6.428070,1.102527,-3.382115,-1.938652,0.697135,-5.476683,-8.095620,-2.662584,4.279419,-8.021995],[-0.514966,-5.087540,-6.246107,6.406738,-4.980525,-5.526479,-9.480628,-5.457115,0.971386,-7.443938,-2.698683,-9.210692,-6.094942,6.483521]],[[3.354320,5.241262,6.581002,-7.659162,-9.957855,3.164814,-0.640546,7.835469,4.065334,7.454768,8.898902,-9.154484,-7.760942,-0.284451],[1.640298,-7.111391,6.521893,-8.311208,-9.765935,-1.785441,-3.039666,2.910530,4.325135,9.435203,-8.328899,4.727961,9.385196,0.809618],[3.680172,-7.959201,-2.006516,2.405455,-6.573080,-3.495811,-3.508964,-8.043399,-4.139884,9.689497,-0.048133,3.083495,-4.960953,-5.073667]],[[-3.839165,8.480848,6.625326,-0.997196,2.431743,3.746984,8.298480,-7.465831,5.775297,2.227531,-2.813994,8.051030,7.812223,-5.851935],[-9.112467,1.602908,-5.805021,-5.598263,-4.800867,8.927373,-2.175823,-1.847146,-9.741606,-3.672216,8.800780,-8.269181,-1.872625,-8.155703],[-4.080765,8.282852,-4.972218,5.143192,-6.476526,-2.504359,-0.783133,-5.617358,7.573233,-3.884902,4.510680,7.589029,-3.203357,-1.869823]],[[8.684013,9.297421,7.587487,-6.866690,3.159440,9.718698,1.178982,8.394783,0.394485,5.285346,-4.515667,3.069777,-9.652407,-9.604500],[-1.098589,0.507867,1.112612,6.645740,-7.005456,-9.464251,8.075634,6.273017,-9.052154,-9.989564,-1.006463,-9.785201,8.642371,-1.200238],[-8.557376,0.633608,0.920850,-0.761297,5.620135,-0.046027,-2.819262,7.178914,-2.865859,-1.726175,9.836703,-7.538536,-8.291813,-6.526683]],[[-3.737351,0.977237,5.775377,7.754636,-5.821684,-1.683402,8.089893,2.851959,1.329575,4.167506,3.119181,-3.625960,-9.710453,-0.428776],[3.329627,0.334823,7.157374,-4.525823,6.560652,7.908377,-8.767322,2.764275,-5.809630,7.255079,8.048556,1.760808,-3.594872,-0.809047],[6.902413,-9.511322,8.679772,-9.508814,-5.521611,-0.222410,2.543220,2.325759,9.612461,5.058859,9.969325,3.324769,-9.117249,2.713505]],[[7.217289,1.646621,-8.537109,5.467493,4.683366,-2.644036,3.442734,8.514132,2.606364,-3.481276,6.620593,-6.511510,-2.826326,-8.676938],[6.902183,8.174337,2.061147,6.936763,-8.868139,2.218144,-1.136484,-1.987589,-3.919458,-6.579369,-0.096230,-7.231224,5.268018,2.021109],[7.516078,-3.183056,1.786743,4.422956,-2.616189,9.587535,8.882224,6.094047,-9.329738,0.225006,0.370792,-8.828678,-5.332211,-4.932367]],[[-3.762388,7.388328,8.576718,-2.367778,-9.714549,0.165854,-1.343197,0.517477,4.274741,1.473665,-2.844673,9.709904,1.553957,-8.676975],[-6.782054,9.975075,-3.239880,-9.399242,-2.778296,-1.359513,-9.017792,1.186891,-2.853263,0.560609,2.409553,-0.833069,7.744790,-4.924494],[9.339941,9.043067,2.502103,-8.085199,5.865661,0.955540,7.059994,-8.141418,6.487119,-3.006018,0.590973,1.521706,3.507919,-8.234973]],[[8.435424,4.705038,6.309117,3.413609,2.865344,-4.072708,-7.761833,-0.079672,-8.879997,-2.451210,-8.745001,4.736739,-2.682865,3.373168],[-2.121374,-1.156563,-5.122599,9.372386,-8.695087,-9.965606,-6.375650,9.870601,-0.857131,2.833130,-1.978996,-5.067325,-0.237400,-3.297157],[-9.542392,-7.725472,-6.294115,0.935338,-0.387048,-8.565596,7.979070,-6.940871,-7.730956,-5.699982,2.752394,3.312142,0.987366,3.679515]],[[2.214111,-7.719194,8.491710,4.236639,-7.266373,-8.188492,6.041183,1.181868,4.369553,-9.246726,9.563771,-7.808124,-4.832014,7.619183],[0.129952,-7.719183,-9.626358,-8.424165,5.402261,8.289770,-5.206802,9.002218,7.670082,-5.258318,-0.501303,-8.585764,-2.389874,2.097173],[-4.378956,-5.955444,7.444386,-9.957278,-7.798620,9.252203,-1.500267,1.713825,-2.579494,-4.684762,3.010318,-1.895359,-2.850896,-3.208767]]], dtype = "float64")#candidate|5908|(9, 3, 14)|const|float64
uop_5909 = relay.log(const_5908.astype('float64')) # shape=(9, 3, 14)
bop_5913 = relay.bitwise_or(const_5908.astype('int8'), relay.reshape(uop_5909.astype('int8'), relay.shape_of(const_5908))) # shape=(9, 3, 14)
output = bop_5913
output2 = bop_5913
func_5916 = relay.Function([], output)
mod['func_5916'] = func_5916
mod = relay.transform.InferType()(mod)
mutated_mod['func_5916'] = func_5916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5916_call = mutated_mod.get_global_var('func_5916')
call_5917 = func_5916_call()
output = call_5917
func_5918 = relay.Function([], output)
mutated_mod['func_5918'] = func_5918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3862_call = mod.get_global_var('func_3862')
func_3863_call = mutated_mod.get_global_var('func_3863')
call_5950 = relay.TupleGetItem(func_3862_call(), 0)
call_5951 = relay.TupleGetItem(func_3863_call(), 0)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_5961 = relay.TupleGetItem(func_3244_call(), 0)
call_5962 = relay.TupleGetItem(func_3246_call(), 0)
output = relay.Tuple([call_5950,call_5961,])
output2 = relay.Tuple([call_5951,call_5962,])
func_5963 = relay.Function([], output)
mod['func_5963'] = func_5963
mod = relay.transform.InferType()(mod)
mutated_mod['func_5963'] = func_5963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5963_call = mutated_mod.get_global_var('func_5963')
call_5964 = func_5963_call()
output = call_5964
func_5965 = relay.Function([], output)
mutated_mod['func_5965'] = func_5965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4544_call = mod.get_global_var('func_4544')
func_4546_call = mutated_mod.get_global_var('func_4546')
call_6052 = func_4544_call()
call_6053 = func_4544_call()
output = relay.Tuple([call_6052,])
output2 = relay.Tuple([call_6053,])
func_6060 = relay.Function([], output)
mod['func_6060'] = func_6060
mod = relay.transform.InferType()(mod)
output = func_6060()
func_6061 = relay.Function([], output)
mutated_mod['func_6061'] = func_6061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4956_call = mod.get_global_var('func_4956')
func_4958_call = mutated_mod.get_global_var('func_4958')
call_6141 = relay.TupleGetItem(func_4956_call(), 1)
call_6142 = relay.TupleGetItem(func_4958_call(), 1)
output = relay.Tuple([call_6141,])
output2 = relay.Tuple([call_6142,])
func_6143 = relay.Function([], output)
mod['func_6143'] = func_6143
mod = relay.transform.InferType()(mod)
mutated_mod['func_6143'] = func_6143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6143_call = mutated_mod.get_global_var('func_6143')
call_6144 = func_6143_call()
output = call_6144
func_6145 = relay.Function([], output)
mutated_mod['func_6145'] = func_6145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4544_call = mod.get_global_var('func_4544')
func_4546_call = mutated_mod.get_global_var('func_4546')
call_6188 = func_4544_call()
call_6189 = func_4544_call()
output = relay.Tuple([call_6188,])
output2 = relay.Tuple([call_6189,])
func_6211 = relay.Function([], output)
mod['func_6211'] = func_6211
mod = relay.transform.InferType()(mod)
output = func_6211()
func_6212 = relay.Function([], output)
mutated_mod['func_6212'] = func_6212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5673_call = mod.get_global_var('func_5673')
func_5674_call = mutated_mod.get_global_var('func_5674')
call_6235 = relay.TupleGetItem(func_5673_call(), 0)
call_6236 = relay.TupleGetItem(func_5674_call(), 0)
func_3668_call = mod.get_global_var('func_3668')
func_3671_call = mutated_mod.get_global_var('func_3671')
var_6241 = relay.var("var_6241", dtype = "bool", shape = (968, 1))#candidate|6241|(968, 1)|var|bool
var_6242 = relay.var("var_6242", dtype = "uint64", shape = (120,))#candidate|6242|(120,)|var|uint64
call_6240 = relay.TupleGetItem(func_3668_call(relay.reshape(var_6241.astype('bool'), [11, 11, 8]), relay.reshape(var_6242.astype('uint64'), [120,]), ), 2)
call_6243 = relay.TupleGetItem(func_3671_call(relay.reshape(var_6241.astype('bool'), [11, 11, 8]), relay.reshape(var_6242.astype('uint64'), [120,]), ), 2)
uop_6252 = relay.log(var_6241.astype('float64')) # shape=(968, 1)
bop_6269 = relay.equal(uop_6252.astype('bool'), call_6235.astype('bool')) # shape=(4, 968, 1)
bop_6272 = relay.equal(uop_6252.astype('bool'), call_6236.astype('bool')) # shape=(4, 968, 1)
uop_6278 = relay.acos(call_6235.astype('float64')) # shape=(4, 1, 1)
uop_6280 = relay.acos(call_6236.astype('float64')) # shape=(4, 1, 1)
func_60_call = mod.get_global_var('func_60')
func_63_call = mutated_mod.get_global_var('func_63')
const_6282 = relay.const([-2,-6,6,-3,-5,-9,-1,3,-1,-3,3,-4,-1,8,10,3,2,6,3,10,-8,-2,6,-6,8,-3,9,9,6,9,-1,-5,4,-1,-1,-8,-2,7,8,4,-5,6,4,-3,-3,4,7,-6,-3,9,-2,4,-9,-3,-6,-2,-5,4,4,-10,2,-2,7,1,9,-3,-8,4,-8,4,-5,5,-5,-9,-8,7,-5], dtype = "uint32")#candidate|6282|(77,)|const|uint32
var_6283 = relay.var("var_6283", dtype = "uint32", shape = (1232,))#candidate|6283|(1232,)|var|uint32
call_6281 = func_60_call(relay.reshape(const_6282.astype('uint32'), [11, 1, 7]), relay.reshape(var_6283.astype('uint32'), [11, 16, 7]), )
call_6284 = func_60_call(relay.reshape(const_6282.astype('uint32'), [11, 1, 7]), relay.reshape(var_6283.astype('uint32'), [11, 16, 7]), )
bop_6286 = relay.greater(var_6283.astype('bool'), var_6241.astype('bool')) # shape=(968, 1232)
const_6295 = relay.const([[[-0.648147,-7.496203,-5.481127,-8.675298,7.720514],[8.861454,-7.972349,-8.921125,-0.495807,5.844062],[9.783083,2.215719,5.921202,9.535003,-9.760759],[9.220754,-2.742884,-0.082817,7.132407,5.696422],[9.720233,-1.236311,-0.439736,5.942939,6.125134],[-7.468861,5.328569,6.804549,-0.441017,0.124112],[5.268032,-9.709974,-1.723140,-7.950503,4.596436],[-7.426129,9.692494,-8.878595,-3.593053,-0.978922],[-7.669163,-2.985459,-3.908624,5.280093,-7.102498],[4.166781,7.884634,0.994468,5.238298,6.351396],[0.373194,2.853445,4.919977,-7.789847,1.816415]],[[7.970759,-5.632439,-1.575312,8.735638,8.823036],[-2.460406,8.798130,-0.902780,-4.738380,8.583047],[4.182620,2.281241,7.184198,-0.347455,-0.884726],[-4.032156,-8.632158,3.405884,-8.420007,-2.689161],[-4.258228,-4.662554,-5.141316,-8.543682,-8.345621],[-0.584071,-9.563859,2.216408,-9.576407,-4.655430],[8.612086,-8.065528,9.203438,-8.200627,-6.941530],[6.384620,-7.449745,2.332671,9.110924,1.274220],[8.629646,3.971302,1.938708,8.303974,-2.387123],[8.438468,-2.940986,0.582135,9.209052,1.401622],[-0.415260,5.630692,5.749285,5.752777,-6.855645]],[[-5.819430,8.067523,-4.485943,-8.501023,-7.991425],[7.417718,6.751742,-5.841141,7.013026,-0.351213],[9.809096,5.517909,6.438680,6.456143,4.004176],[1.848873,3.531524,3.737936,-1.652465,2.976668],[0.261471,-3.414725,9.296026,8.627359,-9.652015],[9.402646,9.310384,-7.970555,2.013243,0.497016],[-0.941327,0.086445,3.624728,6.728183,-7.395553],[9.050637,0.555198,-9.244853,-3.151057,1.605682],[-2.494480,-7.474144,7.596473,-8.063570,6.326195],[-7.458926,3.213131,9.484474,-9.451240,-8.214107],[-4.484459,-1.280555,3.923138,-5.141860,1.090364]],[[-0.889136,-2.644178,9.077280,-1.686791,2.209997],[7.120208,7.010478,9.057873,-6.501735,1.925454],[-0.037990,-7.123184,8.947797,-8.321606,2.372346],[1.207642,8.035568,-8.502932,8.697249,-6.464505],[-9.253238,-5.042093,-9.040577,0.582063,-2.754767],[3.709492,-5.815475,6.307642,1.917970,3.713928],[3.156683,6.781271,-9.505869,5.435890,-9.146106],[-8.360117,-0.863103,-5.030281,-7.145075,8.405958],[-3.235703,-5.828756,-6.646649,-0.282339,0.043728],[-0.134754,-5.997788,2.858749,6.245050,-7.418786],[-0.945127,4.278246,-8.131892,-6.295891,0.651492]]], dtype = "float64")#candidate|6295|(4, 11, 5)|const|float64
bop_6296 = relay.mod(uop_6278.astype('float64'), const_6295.astype('float64')) # shape=(4, 11, 5)
bop_6299 = relay.mod(uop_6280.astype('float64'), const_6295.astype('float64')) # shape=(4, 11, 5)
output = relay.Tuple([call_6240,var_6242,bop_6269,call_6281,const_6282,bop_6286,bop_6296,])
output2 = relay.Tuple([call_6243,var_6242,bop_6272,call_6284,const_6282,bop_6286,bop_6299,])
func_6308 = relay.Function([var_6241,var_6242,var_6283,], output)
mod['func_6308'] = func_6308
mod = relay.transform.InferType()(mod)
var_6309 = relay.var("var_6309", dtype = "bool", shape = (968, 1))#candidate|6309|(968, 1)|var|bool
var_6310 = relay.var("var_6310", dtype = "uint64", shape = (120,))#candidate|6310|(120,)|var|uint64
var_6311 = relay.var("var_6311", dtype = "uint32", shape = (1232,))#candidate|6311|(1232,)|var|uint32
output = func_6308(var_6309,var_6310,var_6311,)
func_6312 = relay.Function([var_6309,var_6310,var_6311,], output)
mutated_mod['func_6312'] = func_6312
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6370 = relay.var("var_6370", dtype = "int64", shape = ())#candidate|6370|()|var|int64
var_6371 = relay.var("var_6371", dtype = "int64", shape = (12, 4, 14))#candidate|6371|(12, 4, 14)|var|int64
bop_6372 = relay.right_shift(var_6370.astype('int64'), var_6371.astype('int64')) # shape=(12, 4, 14)
bop_6379 = relay.multiply(bop_6372.astype('int8'), var_6370.astype('int8')) # shape=(12, 4, 14)
func_5331_call = mod.get_global_var('func_5331')
func_5332_call = mutated_mod.get_global_var('func_5332')
call_6384 = func_5331_call()
call_6385 = func_5331_call()
output = relay.Tuple([bop_6379,call_6384,])
output2 = relay.Tuple([bop_6379,call_6385,])
func_6397 = relay.Function([var_6370,var_6371,], output)
mod['func_6397'] = func_6397
mod = relay.transform.InferType()(mod)
var_6398 = relay.var("var_6398", dtype = "int64", shape = ())#candidate|6398|()|var|int64
var_6399 = relay.var("var_6399", dtype = "int64", shape = (12, 4, 14))#candidate|6399|(12, 4, 14)|var|int64
output = func_6397(var_6398,var_6399,)
func_6400 = relay.Function([var_6398,var_6399,], output)
mutated_mod['func_6400'] = func_6400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4407_call = mod.get_global_var('func_4407')
func_4409_call = mutated_mod.get_global_var('func_4409')
call_6454 = func_4407_call()
call_6455 = func_4407_call()
uop_6471 = relay.sigmoid(call_6454.astype('float32')) # shape=(11, 11, 8)
uop_6473 = relay.sigmoid(call_6455.astype('float32')) # shape=(11, 11, 8)
output = relay.Tuple([uop_6471,])
output2 = relay.Tuple([uop_6473,])
func_6478 = relay.Function([], output)
mod['func_6478'] = func_6478
mod = relay.transform.InferType()(mod)
mutated_mod['func_6478'] = func_6478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6478_call = mutated_mod.get_global_var('func_6478')
call_6479 = func_6478_call()
output = call_6479
func_6480 = relay.Function([], output)
mutated_mod['func_6480'] = func_6480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2943_call = mod.get_global_var('func_2943')
func_2945_call = mutated_mod.get_global_var('func_2945')
call_6513 = func_2943_call()
call_6514 = func_2943_call()
func_6308_call = mod.get_global_var('func_6308')
func_6312_call = mutated_mod.get_global_var('func_6312')
var_6516 = relay.var("var_6516", dtype = "uint64", shape = (120,))#candidate|6516|(120,)|var|uint64
const_6517 = relay.const([-7,-2,9,8,7,-4,4,-4,4,3,4,-6,8,2,7,-9,-6,-5,-10,7,-2,10,1,-2,-7,-10,10,9,1,-2,-5,-3,1,-6,-2,8,-3,1,-4,6,-10,2,4,10,5,2,-2,-10,2,1,10,9,10,5,2,5,10,4,9,7,-7,-3,-5,-9,3,-2,-9,-6,8,-3,5,-4,5,6,3,9,4,6,-7,8,-5,2,-1,5,2,-10,7,-3,-2,-8,4,-5,-1,10,6,-5,6,6,-8,7,-8,8,-2,10,1,9,7,-6,4,4,3,10,-1,-7,7,10,2,3,-10,-8,-2,8,10,8,1,-6,5,4,-2,2,6,7,9,-1,-4,2,5,-7,-8,-1,-9,1,-2,-8,7,-6,-4,-10,4,4,8,3,-9,-10,-5,4,-7,6,2,-4,5,-2,4,4,3,5,5,7,-10,9,-10,-7,-9,-6,8,4,1,-2,7,-2,-3,2,-7,-2,-7,-2,5,2,6,-9,-10,-8,8,-8,8,-5,-9,1,-7,-4,-7,9,-8,7,1,-8,8,5,-10,3,5,10,-7,3,-7,8,5,-5,-10,-7,-8,-5,-1,-2,-3,8,3,5,3,3,7,4,-9,-3,9,2,-4,-4,7,-5,-3,2,5,7,5,7,-1,2,-8,-9,-6,4,5,-5,8,-5,-7,10,-4,9,6,1,-5,-5,9,-1,4,3,7,-4,-9,7,-5,5,3,9,10,-5,5,9,6,7,7,-1,-9,9,-3,-2,-3,-10,-3,-6,-8,-7,2,7,5,-10,-5,7,6,-1,-2,9,-2,-4,7,5,2,8,-7,6,8,-4,-4,6,7,-9,8,6,7,4,-9,-9,10,-7,-2,-1,-8,1,8,-2,-5,-3,10,-5,-9,-1,6,1,7,5,2,10,-10,2,10,-2,8,8,-5,7,9,-10,9,-3,1,6,5,-1,-8,-5,-8,3,-2,-4,-3,-9,-10,-1,2,5,-3,7,8,-3,1,-7,4,-5,-1,3,1,-8,5,-7,-5,-2,-3,6,-7,10,-8,-6,-4,-1,1,1,-8,-10,2,9,10,-6,10,-6,3,-4,-10,-5,3,-1,10,4,-5,-10,-2,2,2,-4,-10,-1,6,-5,-6,-1,6,3,4,-3,-2,5,2,5,-5,-8,1,9,-5,-4,-7,-1,-6,1,2,10,9,-7,3,4,-2,3,2,-3,-10,-7,3,-2,-10,1,-10,-5,8,-9,5,9,8,3,5,6,-4,-2,8,-7,10,-2,3,-7,-1,-2,-10,4,-4,-7,-4,4,-5,-6,-2,-3,3,1,5,6,4,2,10,3,2,3,-2,-5,-3,10,-6,-10,-2,-6,10,-5,-2,10,1,-6,-3,9,5,-2,7,-8,7,-3,-8,6,-2,2,-5,8,6,-1,4,-4,-5,1,-8,-4,-4,2,7,10,8,-5,-6,3,10,3,-3,5,3,10,5,-6,1,3,-7,-9,-6,-2,-1,6,-6,-5,6,-8,6,-10,-2,-9,4,2,6,-8,10,-7,-2,10,2,10,-5,-6,-6,1,-5,-2,-4,-2,-8,3,10,-6,-4,4,-4,-5,3,-4,-10,-9,-7,3,5,-2,-6,10,-6,10,-7,-10,-1,3,-8,4,-2,-4,2,-10,5,-2,8,8,-10,-6,5,9,-2,-9,-7,-2,-6,10,6,-6,4,5,-2,6,3,9,9,-5,10,5,7,-10,4,10,10,4,-6,5,-1,-9,6,-4,8,8,-1,7,10,2,7,-5,-10,2,7,-1,10,-5,-8,1,-8,3,-2,9,8,-6,-3,-4,2,-8,-3,9,9,-8,-3,-2,-10,10,7,-3,-1,2,10,9,-9,-10,6,-6,5,1,-6,9,-9,-7,-8,-3,-9,-7,10,2,-10,4,4,-10,-5,-7,3,-7,4,-9,4,5,5,-2,-5,6,7,-3,9,9,2,7,1,8,-7,10,-8,-7,-5,10,5,7,-4,-4,2,9,9,-1,-1,6,7,1,8,-10,9,3,6,6,10,4,-3,-8,-8,-3,-10,-9,6,2,-8,-9,4,10,3,9,4,-7,-6,-9,6,5,2,4,-4,4,-9,-10,4,-3,6,2,5,8,6,10,-1,7,1,-3,-8,-10,9,-1,9,-2,8,-4,-1,6,10,-9,-5,6,10,2,6,8,-1,8,3,-3,-4,-3,1,-4,9,2,2,9,-7,1,-10,-9,-7,1,7,-2,2,5,7,6,3,-10,-6,-6,-8,6,-5,1,2,-4,5,-1,1,2,-7,6,6,4,6,7,-8,-4,-8,7,-6,-10,-6,9,8,9,-2,3,2,-2,-9,2,1,-4,-2,10,1,10,10,-9,3,-4,-3,-10,6,5,10,7,-7,8,-2,-7,8,-4,-7,9,-9,2,1,10,6,5,5,5,10,1,-4,7,-6,-2,-2,-2,3,-6,7,-2,-1,9,6,10,-9,-10,-9,-5,-7,-1,-8,-1,-8,5,-3,10,-3,-2,5,7,-2,7,5,10,8,3,4,-7,3,8,9,1,-9,3,6,-7,6,-4,7,4,-5,1,3,2,2,-1,9,2,-7,-1,-4,5,-6,2,-3,9,3,9,-8,1,4,10,6,-3,-9,-7,-5,-5,-1,4,-5,-4,-3,-4,6,10,5,-3,-5,3,-1,9,3,8,-2,10,5,4,8,8,3,-4,-1,-1,-5,10,-7,5,4,-5,-6,-2,8,-9,-5,-10,7,7,5,4,-4,-8,-5,10,8,6,10,-5,7,3,-10,-2,-9,7,-7,-1,-9,-2,6,4,9,6,-9,8,-4,9,5,1,10,-5,-2,8,9,-6,3,-7,-1,2,3,-7,4,-10,-5,1,2,-2,4,4,3,-6,-1,9,-7,3,4,8,-5,-6,-1,8,3,-8,4,-2,-3,3,1,-7,6,10,-1,7,7,8,10,-3,-8,2,4,-6,2,2,-3,4,10,-9,-2,-7,-10,9,3,-5,-5,-2,10,-10,9,-8,3,-2,-7,4,-9,-8,-7,1,1,10,2,6,10,-6,8,-1,-7,-3,-6,-6,9,-6,-3,6,-2,1,-6,5,3,-5,7,-3,9,-3,-5,9,-4,-2,-3,-2,-5,-8,2,-9,7,5,7,10,-5,10,1,4,6,4,-4,-2,-1,-10,-6,-7,2,-8,-1,-5,-3,-4,6,-2,4,2,2,5,-6,4,5,-6,-3,-5,3,1,-9,-10,3,-9,-8,4,-9,-3,7,9,-9,8,7,8,-7,8,4,-3,10,7,-5,7,-2,-8], dtype = "uint32")#candidate|6517|(1232,)|const|uint32
call_6515 = relay.TupleGetItem(func_6308_call(relay.reshape(call_6513.astype('bool'), [968, 1]), relay.reshape(var_6516.astype('uint64'), [120,]), relay.reshape(const_6517.astype('uint32'), [1232,]), ), 3)
call_6518 = relay.TupleGetItem(func_6312_call(relay.reshape(call_6513.astype('bool'), [968, 1]), relay.reshape(var_6516.astype('uint64'), [120,]), relay.reshape(const_6517.astype('uint32'), [1232,]), ), 3)
var_6531 = relay.var("var_6531", dtype = "uint32", shape = (1232,))#candidate|6531|(1232,)|var|uint32
bop_6532 = relay.floor_mod(const_6517.astype('float32'), relay.reshape(var_6531.astype('float32'), relay.shape_of(const_6517))) # shape=(1232,)
func_4686_call = mod.get_global_var('func_4686')
func_4693_call = mutated_mod.get_global_var('func_4693')
const_6548 = relay.const([8.798449,1.434947,7.329565,-2.109679,8.891883,-0.256354,-2.514334,-9.649893,-9.939768,4.896790,-0.742709,-4.850136,6.172264,-0.793466,-7.372282,-5.917995,-3.726569,0.338786,2.356293,-4.426217,4.115919,4.515688,-3.375893,0.860589,-5.218299,-0.214269,-6.295357,2.939862,-7.025579,-8.123088,3.261902,-1.309697,-8.554006,3.542961,-3.107355,-9.775297,-7.342985,2.144706,3.674474,2.325562,4.578523,5.814372,4.587809,6.472983,-8.675319,-8.709346,-3.039753,1.221958,-2.384705,6.742200,-5.573489,1.313553,3.756918,-2.722521,4.755686,-7.855706,9.313483,-3.449151,-4.726777,-5.200588,0.110669,-9.756990,3.881904,9.076612,-1.850567,-3.398768,-7.547640,8.710403,-7.709822,2.187343,4.163386,-5.350603,0.176511,6.597870,-1.320067,-5.584742,-4.512479,-7.216285,-6.624435,-6.478218,-9.126453,4.660627,-5.672730,-8.974916,-2.337316,-9.341201,8.534533,-4.982222,5.535509,-3.940818,1.052052,8.385830,2.812292,-9.079298,0.806479,-4.940220,9.683333,3.617656,-5.066518,0.426302,1.272843,-1.900555,-0.983869,2.361638,2.135607,-3.945296,-0.497406,-0.465197,9.782982,9.350067,2.640212,-4.558586,8.591140,-2.143582,4.725826,6.896583,3.872905,1.543573,-1.393309,5.634961,-9.106060,3.139009,-8.269968,-5.934135,-2.015553,-2.392602,1.828687,-5.316746,-8.986856,-9.069089,-6.489051,-2.198162,4.016775,-7.639729,-9.410638,0.209280,5.905482,0.023619,2.095989,3.459278,0.872673,6.313377,-6.744612,-5.815039,7.741815,-0.046139,-4.768473,5.067916,-1.776452,6.025819,-1.521101,0.690738,4.760774,8.455465], dtype = "float64")#candidate|6548|(154,)|const|float64
var_6549 = relay.var("var_6549", dtype = "float64", shape = (224,))#candidate|6549|(224,)|var|float64
var_6550 = relay.var("var_6550", dtype = "int16", shape = (728, 2))#candidate|6550|(728, 2)|var|int16
const_6551 = relay.const(2.125128, dtype = "float64")#candidate|6551|()|const|float64
call_6547 = relay.TupleGetItem(func_4686_call(relay.reshape(call_6513.astype('float32'), [11, 11, 8]), relay.reshape(const_6548.astype('float64'), [154,]), relay.reshape(var_6549.astype('float64'), [224,]), relay.reshape(bop_6532.astype('uint32'), [1232,]), relay.reshape(var_6550.astype('int16'), [1456, 1]), relay.reshape(const_6551.astype('float64'), []), ), 3)
call_6552 = relay.TupleGetItem(func_4693_call(relay.reshape(call_6513.astype('float32'), [11, 11, 8]), relay.reshape(const_6548.astype('float64'), [154,]), relay.reshape(var_6549.astype('float64'), [224,]), relay.reshape(bop_6532.astype('uint32'), [1232,]), relay.reshape(var_6550.astype('int16'), [1456, 1]), relay.reshape(const_6551.astype('float64'), []), ), 3)
bop_6557 = relay.add(const_6517.astype('int64'), const_6551.astype('int64')) # shape=(1232,)
uop_6560 = relay.erf(var_6550.astype('float32')) # shape=(728, 2)
output = relay.Tuple([call_6513,call_6515,var_6516,bop_6532,call_6547,const_6548,var_6549,bop_6557,uop_6560,])
output2 = relay.Tuple([call_6514,call_6518,var_6516,bop_6532,call_6552,const_6548,var_6549,bop_6557,uop_6560,])
func_6562 = relay.Function([var_6516,var_6531,var_6549,var_6550,], output)
mod['func_6562'] = func_6562
mod = relay.transform.InferType()(mod)
var_6563 = relay.var("var_6563", dtype = "uint64", shape = (120,))#candidate|6563|(120,)|var|uint64
var_6564 = relay.var("var_6564", dtype = "uint32", shape = (1232,))#candidate|6564|(1232,)|var|uint32
var_6565 = relay.var("var_6565", dtype = "float64", shape = (224,))#candidate|6565|(224,)|var|float64
var_6566 = relay.var("var_6566", dtype = "int16", shape = (728, 2))#candidate|6566|(728, 2)|var|int16
output = func_6562(var_6563,var_6564,var_6565,var_6566,)
func_6567 = relay.Function([var_6563,var_6564,var_6565,var_6566,], output)
mutated_mod['func_6567'] = func_6567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_6629 = relay.TupleGetItem(func_5190_call(), 0)
call_6630 = relay.TupleGetItem(func_5191_call(), 0)
func_5963_call = mod.get_global_var('func_5963')
func_5965_call = mutated_mod.get_global_var('func_5965')
call_6646 = relay.TupleGetItem(func_5963_call(), 0)
call_6647 = relay.TupleGetItem(func_5965_call(), 0)
func_5744_call = mod.get_global_var('func_5744')
func_5748_call = mutated_mod.get_global_var('func_5748')
const_6651 = relay.const([1,7,9,1,6,6,-10,-3,5,-5,3,7,8,3,3,1,8,-5,-1,10,8,9,-2,3,2,-2,-10,6,2,-5,3,-8,5,-7,-10,4,-4,-5,5,6,8,2,-6,-7,-10,-5,10,2,-7,-2], dtype = "int32")#candidate|6651|(50,)|const|int32
var_6652 = relay.var("var_6652", dtype = "int64", shape = (605,))#candidate|6652|(605,)|var|int64
call_6650 = relay.TupleGetItem(func_5744_call(relay.reshape(const_6651.astype('int32'), [10, 1, 5]), relay.reshape(var_6652.astype('int64'), [11, 11, 5]), ), 0)
call_6653 = relay.TupleGetItem(func_5748_call(relay.reshape(const_6651.astype('int32'), [10, 1, 5]), relay.reshape(var_6652.astype('int64'), [11, 11, 5]), ), 0)
output = relay.Tuple([call_6629,call_6646,call_6650,const_6651,var_6652,])
output2 = relay.Tuple([call_6630,call_6647,call_6653,const_6651,var_6652,])
func_6664 = relay.Function([var_6652,], output)
mod['func_6664'] = func_6664
mod = relay.transform.InferType()(mod)
var_6665 = relay.var("var_6665", dtype = "int64", shape = (605,))#candidate|6665|(605,)|var|int64
output = func_6664(var_6665)
func_6666 = relay.Function([var_6665], output)
mutated_mod['func_6666'] = func_6666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3957_call = mod.get_global_var('func_3957')
func_3958_call = mutated_mod.get_global_var('func_3958')
call_6673 = relay.TupleGetItem(func_3957_call(), 3)
call_6674 = relay.TupleGetItem(func_3958_call(), 3)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_6683 = relay.TupleGetItem(func_3244_call(), 0)
call_6684 = relay.TupleGetItem(func_3246_call(), 0)
func_5061_call = mod.get_global_var('func_5061')
func_5062_call = mutated_mod.get_global_var('func_5062')
call_6691 = func_5061_call()
call_6692 = func_5061_call()
bop_6697 = relay.add(call_6683.astype('uint32'), relay.reshape(call_6673.astype('uint32'), relay.shape_of(call_6683))) # shape=(11, 11, 8)
bop_6700 = relay.add(call_6684.astype('uint32'), relay.reshape(call_6674.astype('uint32'), relay.shape_of(call_6684))) # shape=(11, 11, 8)
func_5120_call = mod.get_global_var('func_5120')
func_5123_call = mutated_mod.get_global_var('func_5123')
const_6702 = relay.const([[-1.650095,-1.414272,-4.323150,5.527018,-9.825163,-0.601770,-8.156965,2.980151,9.814761,0.675218,5.271055,-3.499260,1.797792,2.669673,4.898580,6.637232,-9.811180,-2.418086,-3.066802,4.716232,-2.135180,-5.432401,4.972999,-0.205184,-9.231469,7.626889,7.235103,9.387242,-7.156675,-2.045875,-2.156955,9.840995,0.423722,2.320136,-6.693241,-8.521001,-3.969361,3.889699,-6.646864,-3.503856,2.577686,2.280456,-1.606530,9.281612,8.044604,-8.247809,4.635736,4.105928,8.033548,-8.184069,0.493446,-9.770921,2.355610,0.217861,9.332534,-5.847937,-7.729088,5.866857,-0.461206,1.755903,-7.753911,0.343047,2.830326,-8.801006,-4.148728,-3.784735],[-3.907090,9.852579,-6.554661,6.853140,8.821125,-2.612058,4.216076,-4.084307,-6.536114,-7.569439,1.527338,-0.139222,-9.134999,7.663785,6.312067,-0.542089,-9.813385,2.823747,-5.036457,-3.161333,-9.457571,2.845627,-6.591163,2.905265,3.783516,7.533816,-0.230178,-5.517397,-0.122883,3.817837,6.164904,8.100433,9.389406,0.330773,-8.436567,2.963659,-5.283264,-1.344701,-6.889334,-9.085034,8.947635,-2.473887,4.395466,-3.830421,-2.056525,-4.136337,8.353254,5.706363,-2.247297,8.429010,-5.396355,-2.514324,8.155869,1.250095,-2.743915,-3.413824,7.224713,3.452293,5.774154,1.293745,2.345949,6.687366,3.694917,-2.985931,8.223680,-6.852786],[-6.609255,6.184846,-1.927293,-1.262732,-1.865501,-5.711046,4.334482,-7.754058,-7.981982,4.457132,4.736567,-3.180832,9.060700,0.801525,-3.391090,9.894578,-1.259403,8.403652,3.784066,2.225720,-3.140183,-0.513982,-5.527576,-9.709829,-5.537314,-4.059706,-1.670509,-2.992384,8.634331,4.217653,-6.615163,0.771905,2.590084,5.526581,-5.479390,-1.505155,-7.723073,-0.369953,9.713776,8.634493,-3.500267,-8.586911,1.071239,6.169298,-7.245493,-6.885193,7.925804,4.153392,-0.941359,6.714566,2.642091,1.675232,-0.805952,-2.514320,-2.177128,4.523393,-2.121597,-6.729748,3.035026,-0.235193,-9.393871,-6.510069,-8.888776,-8.515258,-3.003607,4.108808],[7.033684,1.350581,9.638287,5.779085,-8.694658,-8.914060,-7.705001,-9.640572,-4.453624,0.472267,3.116110,-8.893052,8.567898,2.583536,4.730949,-9.677125,3.638879,-4.407452,2.107773,7.698390,5.459074,-6.904546,-7.044677,1.289671,-7.188341,3.463099,-8.651049,3.771300,-7.495934,6.566491,-7.533719,-4.227273,9.600109,-5.057417,-9.725933,-9.534256,0.579083,-4.304295,1.997827,4.438734,-0.016842,-1.262302,-0.403688,7.452606,-4.060159,-9.994756,-0.314077,-0.611264,-5.514220,-3.508455,-3.104794,-6.545841,-0.073949,4.395058,-0.286861,8.434844,2.504791,3.406664,6.239729,-1.607679,0.492542,-7.628799,2.621071,7.096141,5.488747,2.815751],[5.092480,-2.273029,-2.472291,6.158659,-0.440494,8.047027,-6.442035,9.207074,0.485300,2.349907,9.137738,-0.408828,6.269134,-5.517250,-0.929215,-7.286815,0.909918,3.292369,3.721943,-8.265348,4.669522,5.097072,-1.547481,9.198289,6.453447,-1.248728,7.897214,4.725216,-5.170018,7.911595,3.623837,-0.791459,-9.600185,-6.679343,8.599725,3.935963,6.117835,-4.094618,-0.999166,5.797590,0.937232,-0.470681,7.275449,4.423263,7.294748,-9.747124,-1.269503,9.090729,-0.217317,-8.803110,-7.049613,-2.373398,3.257847,4.051677,-0.814572,0.196103,-5.838401,-5.470628,7.474469,3.570616,6.445009,-6.518643,1.716663,-3.584474,9.155661,8.605576],[3.732002,2.545248,-5.960976,-1.028414,-8.504793,-5.302958,5.722865,-3.073823,-1.557514,5.107946,7.020128,-7.302698,8.270878,-5.768256,2.810803,-1.136186,7.329681,8.836489,-4.902373,-6.285837,8.936669,2.447675,-6.498992,-1.490588,2.483012,-0.408887,7.863079,9.264172,5.289870,2.067377,4.986286,6.608154,-2.001082,9.970817,-8.228295,8.898535,-2.388409,-0.646304,-7.351441,-3.591863,-3.238366,-5.357429,6.662581,-2.705761,2.213563,6.456574,5.876178,2.802390,-8.290669,-2.498837,-3.058521,-6.108083,-5.617844,9.356386,6.046037,4.858485,-4.053602,5.651424,2.240821,7.524876,-4.031451,-9.454011,6.851580,3.040892,-9.054407,6.378741],[1.907454,9.137977,-4.988702,-9.366960,-6.472776,-0.057307,3.493569,-4.002578,5.791062,1.369807,3.704608,-9.789288,3.454393,-0.994941,9.226980,-9.218358,8.387393,4.711946,4.245770,-7.310233,4.855441,-8.923006,-1.105982,5.543027,-3.249082,8.446253,-3.428490,1.747320,9.361253,0.945183,6.646309,3.096989,-4.115976,-7.229927,-5.724028,4.547792,6.870427,-7.562207,6.453773,-8.494201,-4.343689,5.170217,0.287972,-9.704828,-1.792851,3.234897,-0.819780,-6.584801,0.960883,-5.482461,0.109436,9.606136,0.101502,4.786159,-9.901430,7.605232,5.631660,2.928506,9.040421,-5.360331,-2.274956,3.533267,-0.959143,1.624944,-8.354389,-5.539081],[6.424790,2.153489,7.267225,3.099883,-6.171531,3.686320,8.496084,-7.703397,-5.724273,-4.411725,-7.690662,9.570810,-9.032446,6.295068,-9.558616,-3.837667,4.099104,8.806089,-7.846551,-4.478130,3.739734,7.270827,5.446028,7.171245,-8.278921,-3.992000,9.822781,2.738951,-6.559228,-2.603919,-0.729854,-4.256995,-5.025278,6.072583,4.926254,0.612298,5.208933,3.573916,-9.261859,-6.456102,6.469745,-7.102591,7.008768,-7.134900,-6.764687,-4.959697,3.166192,-5.991720,-3.326506,9.928240,-7.973567,-1.427462,0.972067,-8.701806,-7.582116,-7.867871,7.125867,-6.057043,-3.857052,-8.953283,-6.277152,-8.074787,9.517467,9.347320,-1.954158,3.259467],[-3.075708,-7.502678,-4.653081,5.166765,4.365723,-4.144230,-1.549173,7.535495,4.121390,8.367739,8.088005,9.090640,1.629228,-7.390979,6.212096,-8.608617,-2.291491,5.266787,2.627288,7.114329,-8.137503,6.282660,7.761345,-0.804313,-0.581746,-2.271218,7.498586,-8.878518,-7.022294,-2.726882,0.919788,0.947595,7.806128,-9.742819,-5.880983,1.184478,7.335537,6.791710,-0.385955,2.581239,-8.078297,-4.352825,0.076551,-5.292914,6.545624,-1.459213,5.222425,-2.901655,-7.551816,5.332495,3.570445,-0.339592,1.529466,6.124885,5.840655,-6.226779,-1.681886,3.460033,2.427606,7.555844,-6.765086,7.702885,-2.529941,-4.813684,-0.499664,4.225719],[-8.590805,-7.076273,2.877202,2.761318,-8.812071,-7.151093,-7.295056,4.966716,0.939916,3.398820,-4.110164,7.685604,-3.461137,7.419991,3.609172,-2.427426,-8.120303,2.444328,-9.191742,-6.755849,-3.928417,8.491219,-8.433949,8.360173,-2.432364,7.792961,2.086289,1.095949,-3.152429,3.874906,5.500088,-3.594672,-7.412311,4.495761,-5.045944,-0.748610,1.623494,-2.706759,-2.374769,5.663676,-6.913653,0.867763,-0.110451,4.606405,5.279531,-3.889947,2.603285,1.776831,0.374150,-1.397583,-2.434749,-4.735210,8.209689,-6.585418,-3.519456,-7.691146,-5.213452,2.127863,-1.993308,-2.787648,2.351380,-8.402722,8.960128,-5.697256,-6.668656,-0.880763],[7.119700,-0.457478,2.671746,-6.646131,1.337839,-4.859171,-4.404200,-0.582490,5.506594,5.617001,6.226415,0.311289,6.100320,6.930848,-7.925317,-6.718006,8.267274,-4.922998,9.421419,-1.807109,3.616772,2.987074,-0.321263,-6.115016,-6.062620,-7.404326,8.572175,-8.901457,-2.856021,9.631212,2.816237,-9.206742,-5.019817,-9.105943,-8.021654,-9.943369,8.128982,2.689435,1.613400,9.689239,5.827029,-7.523298,9.407801,5.906852,-3.618905,4.749549,5.656244,-1.487081,-1.879264,5.541335,-7.091754,5.893410,3.814402,2.852841,-3.225085,-2.926559,0.430378,6.787435,3.843351,-8.412118,6.749932,-3.144124,5.328303,-1.871016,0.958261,-0.062273],[-5.755042,2.462253,4.268014,-2.407596,-5.283578,0.863122,9.053632,-4.235472,-4.399332,4.535522,-1.445539,-3.261593,-0.941706,-3.193766,-1.855299,3.619430,-2.163294,4.990795,-7.992346,9.121177,-7.631192,-9.025637,4.921932,2.765726,2.816132,4.729921,-7.649281,6.542309,5.782346,-2.713890,6.482305,-1.376615,-9.580207,0.710861,0.810326,0.854238,5.225165,-2.216856,2.351482,-5.392288,-3.216084,-7.167112,0.894610,3.678920,1.120740,8.749971,-2.694469,-8.685667,1.075051,0.037036,1.498767,-7.467755,-1.634232,5.728062,-1.895205,-2.845887,-5.082748,1.745186,-5.158663,-7.827233,-7.382065,-6.859862,3.189008,-5.044084,-5.702411,7.185445]], dtype = "float64")#candidate|6702|(12, 66)|const|float64
var_6703 = relay.var("var_6703", dtype = "int64", shape = (605,))#candidate|6703|(605,)|var|int64
call_6701 = relay.TupleGetItem(func_5120_call(relay.reshape(const_6702.astype('float64'), [6, 11, 12]), relay.reshape(var_6703.astype('int64'), [605,]), ), 2)
call_6704 = relay.TupleGetItem(func_5123_call(relay.reshape(const_6702.astype('float64'), [6, 11, 12]), relay.reshape(var_6703.astype('int64'), [605,]), ), 2)
output = relay.Tuple([call_6691,bop_6697,call_6701,const_6702,var_6703,])
output2 = relay.Tuple([call_6692,bop_6700,call_6704,const_6702,var_6703,])
func_6707 = relay.Function([var_6703,], output)
mod['func_6707'] = func_6707
mod = relay.transform.InferType()(mod)
mutated_mod['func_6707'] = func_6707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6708 = relay.var("var_6708", dtype = "int64", shape = (605,))#candidate|6708|(605,)|var|int64
func_6707_call = mutated_mod.get_global_var('func_6707')
call_6709 = func_6707_call(var_6708)
output = call_6709
func_6710 = relay.Function([var_6708], output)
mutated_mod['func_6710'] = func_6710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3064_call = mod.get_global_var('func_3064')
func_3066_call = mutated_mod.get_global_var('func_3066')
call_6755 = func_3064_call()
call_6756 = func_3064_call()
func_3874_call = mod.get_global_var('func_3874')
func_3876_call = mutated_mod.get_global_var('func_3876')
call_6782 = func_3874_call()
call_6783 = func_3874_call()
output = relay.Tuple([call_6755,call_6782,])
output2 = relay.Tuple([call_6756,call_6783,])
func_6786 = relay.Function([], output)
mod['func_6786'] = func_6786
mod = relay.transform.InferType()(mod)
mutated_mod['func_6786'] = func_6786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mutated_mod.get_global_var('func_6786')
call_6787 = func_6786_call()
output = call_6787
func_6788 = relay.Function([], output)
mutated_mod['func_6788'] = func_6788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6786_call = mod.get_global_var('func_6786')
func_6788_call = mutated_mod.get_global_var('func_6788')
call_6849 = relay.TupleGetItem(func_6786_call(), 0)
call_6850 = relay.TupleGetItem(func_6788_call(), 0)
output = relay.Tuple([call_6849,])
output2 = relay.Tuple([call_6850,])
func_6883 = relay.Function([], output)
mod['func_6883'] = func_6883
mod = relay.transform.InferType()(mod)
output = func_6883()
func_6884 = relay.Function([], output)
mutated_mod['func_6884'] = func_6884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3418_call = mod.get_global_var('func_3418')
func_3419_call = mutated_mod.get_global_var('func_3419')
call_6908 = func_3418_call()
call_6909 = func_3418_call()
func_3213_call = mod.get_global_var('func_3213')
func_3216_call = mutated_mod.get_global_var('func_3216')
const_6945 = relay.const([[-8.597921,9.564328],[-7.819657,-9.626566],[5.009519,9.721985],[-7.556512,2.078869],[-3.334260,4.231046],[8.194695,-5.441280],[5.697120,-5.133926],[-4.456687,-6.201802],[-0.052112,8.666492],[6.852532,-0.389495],[8.454245,-7.096541],[-0.237387,1.502346],[9.605945,-3.348609],[-0.683507,9.808211],[2.604132,3.327236],[7.482719,-5.775068],[2.520886,5.434193],[-6.839278,-8.579278],[8.174925,5.155825],[-8.759301,-5.956083],[1.524737,-8.443066],[6.969793,4.621900],[2.751044,-2.676868],[-1.709291,-5.598097],[-2.606775,3.165770],[2.963673,2.503914],[-7.245656,0.194411],[8.920000,4.237398],[-8.925986,-6.411757],[7.683978,-6.908094],[-8.254710,-4.646575],[-1.093310,5.158082],[-2.653323,7.410858],[-4.964561,-4.044832],[1.904965,8.034981],[3.958062,6.973047],[-6.095870,7.256765],[2.424997,-9.385010],[-9.701105,-2.678704],[4.508914,1.830389],[-0.666149,3.209230],[2.321822,-1.328908],[9.413570,4.855908],[-1.640245,7.474466],[-7.684826,-7.111621],[-4.058222,-4.233610],[7.179112,3.077420],[-7.632402,-7.476932],[7.002307,0.002088],[2.140742,1.349667],[4.530637,8.497885],[2.430175,-2.536916],[4.553318,2.034634],[6.908898,-1.890785],[2.128769,5.315986],[9.603534,-4.266744],[8.392698,2.478605],[4.804171,-6.926446],[-0.201172,-4.551794],[-9.822007,4.912837],[-4.055107,2.729220],[-4.901836,-5.891738],[-3.114609,0.109134],[-2.273764,-9.870362],[4.930490,-1.107788],[0.417451,9.412647],[4.625741,8.775990],[-1.463264,5.980034],[-0.377584,-3.311765],[7.288436,-9.165641],[-8.453678,5.920982],[7.964516,8.174233],[2.280108,-7.385383],[-8.875651,-6.851372],[2.062822,4.618409],[4.079907,-9.267538],[8.482944,-8.603194],[-1.497417,-7.995456],[0.793936,9.001749],[-4.040932,2.088301],[-2.568428,-0.514322],[-1.746027,-0.367824],[-2.455664,6.326304],[9.886512,7.631552],[8.420284,4.265481],[-1.972261,-2.317978],[7.421616,2.979788],[-5.823563,8.274130],[-0.085693,4.435576],[9.495535,-1.847695],[5.572852,8.841787],[-9.481940,-8.419825],[-9.914065,4.105216],[0.304670,-6.904386],[4.435180,-8.879489],[4.514446,-5.546814],[7.612699,-4.965266],[-5.217723,8.669675],[-4.998793,-4.212903],[2.431786,-1.927941],[-9.353661,3.255428],[-9.373052,-1.562109],[2.123292,8.065740],[-5.799237,-4.846923],[-0.189334,-2.244608],[3.475730,-8.277475],[-1.865868,-1.039227],[8.527593,-8.557242],[-7.550940,-3.470044],[6.647776,-9.227513],[5.973880,9.592303],[-9.002586,-3.599923],[-5.103114,5.724683],[-9.254507,-4.683687],[-5.948777,-5.185043],[9.430329,5.319162],[-9.696147,-5.590813],[-4.375462,-4.568491],[3.601406,2.206493],[9.500404,-8.849392],[4.792351,-1.416746],[5.923433,-5.795526],[3.418029,-7.372867],[6.910174,8.550967],[7.820321,-0.043189],[-4.752041,4.352573],[-5.734758,8.322211],[-8.744651,-3.982083],[5.242938,9.804790],[0.050318,-5.902085],[3.099482,4.861190],[-9.975688,-3.941947],[4.047915,6.803793],[-1.007564,5.876867],[-6.349202,-8.045216],[-3.272870,-4.319374],[8.534571,-7.588020],[0.707811,-8.484054],[6.523919,-0.267885],[-6.050265,4.612524],[0.771286,9.575150],[-6.678227,-5.759631],[-9.086561,0.936284],[2.363227,-2.842040],[-7.491197,1.851701],[-4.554930,-3.634446],[-6.164367,5.159439],[9.716134,-9.304394],[-3.555453,-7.103145],[-4.957187,0.633377],[-3.423129,5.053233],[-4.292220,-3.997490],[-3.262904,-8.646866],[8.414499,5.168539],[3.103873,-1.136265],[1.011379,5.110420],[5.251166,-0.680169],[1.090650,-0.109490],[8.587808,1.387728],[3.282274,-3.868712],[-4.638340,-6.991706],[0.420469,8.213799],[0.389360,7.454443],[-1.585222,-9.605411],[5.528958,8.162715],[-0.152288,-9.574298],[7.775180,0.774733],[9.374913,-7.184821],[-4.084787,-1.855856],[-4.272850,0.565823],[6.902018,4.406955],[1.448441,5.025366],[-0.497345,5.489053],[-3.654715,-2.943215],[-4.190650,9.807472],[9.177897,7.024636],[-0.500545,9.508169],[1.567874,-4.123156],[-6.098192,-9.323079],[0.119805,-9.795738],[-2.130235,-6.109119],[3.143918,-4.705407],[-0.682803,3.064032],[6.337692,-7.869434],[-7.075386,7.922366],[-8.758572,4.044796],[8.300585,-4.454470],[1.053654,-4.316479],[5.027657,6.632427],[-9.624549,-1.234927],[1.250374,-5.314498],[-9.349199,-6.563603],[9.766986,-7.240057],[-7.868467,-0.994596],[2.738105,-1.421197],[5.188106,-0.999741],[-4.908948,7.516288],[1.229696,4.655302],[8.354269,5.702096],[-1.389231,1.059156],[5.681666,6.268222],[6.943192,5.840286],[6.919459,8.376667],[6.986103,1.957718],[1.248197,-1.986366],[-2.431631,1.422065],[4.174853,6.734981],[8.444617,7.280131],[-2.653681,-9.575863],[-0.094006,-2.543075],[4.146692,-5.066417],[3.749901,-9.830197],[-1.306267,8.562691],[6.577764,4.355281],[7.209599,-4.238693],[2.594400,-0.737087],[9.559901,6.344417],[-5.218649,1.343804],[1.125550,-0.701121],[1.800292,-1.146294],[0.027504,-3.053935],[-4.325979,-2.946885],[-9.021304,-8.440433],[-7.791640,5.218429],[2.792416,-3.401603],[-8.003183,-1.949475],[3.711365,-8.891487],[8.743466,4.859744],[-1.147934,5.514022],[5.696918,-2.891328],[6.519665,4.902765],[9.269924,1.008938],[9.267812,3.075848],[8.246701,4.793555],[-8.866960,8.439521],[-9.281347,6.030677],[-3.977272,-2.270270],[-9.199549,2.267100],[4.739417,8.577117],[1.491040,-2.650573],[-8.538017,-0.897320],[3.294514,6.599447],[7.988844,8.699247],[0.403631,-4.556630],[-9.675817,0.346038],[6.576865,-0.326631],[7.064799,-7.237693],[-2.083386,9.644402],[-2.130435,-2.445934],[3.518597,9.838220],[-0.325364,0.337539],[4.557792,9.331294],[-5.850003,-2.798293],[2.776211,-9.558961],[8.263257,5.484218],[5.857919,-0.567833],[-4.711578,2.948789],[-7.544544,-5.933590],[-8.823058,-7.137388],[5.164171,5.572281],[-8.922343,5.768020],[-6.708826,-6.399164],[-1.508668,0.795471],[-7.773523,2.950247],[-3.336381,5.557797],[-1.125976,1.380213],[1.340211,-3.523021],[2.344567,-4.526218],[-0.840476,0.512323],[0.098314,-1.125977],[7.285711,-6.691644],[2.829503,-5.953603],[-5.910385,6.191855],[1.986342,5.943716],[-8.616200,5.913118],[1.696380,-5.752969],[0.338964,-8.282442],[5.879987,3.543451],[-0.489404,8.406126],[7.915176,3.437412],[2.707200,-4.262862],[1.217923,9.158727],[-0.146596,3.547575],[-0.719922,8.522051],[8.618908,-7.577924],[-3.256383,6.625759],[2.226291,-8.023259],[-7.176926,2.869676],[-8.139950,-3.135837],[8.655237,-1.232039],[-3.508569,-5.713774],[2.964353,8.873556],[8.624501,6.025716],[9.026486,2.164341],[9.590307,1.121525],[7.850592,0.777274],[8.011517,-8.106032],[5.254073,-0.912929],[-6.559877,-5.891398],[-7.996834,3.762260],[-4.255264,7.970754],[3.652731,-6.737906],[-5.166919,5.355533],[-4.710526,-3.597840],[-5.227446,9.989636],[8.215907,-5.394446],[-0.256171,6.157228],[-0.878849,-8.370283],[1.632602,-2.245462],[-4.284776,-1.702473],[-1.482869,9.523495],[-8.234866,-6.663866],[-7.416861,8.044211],[7.654615,8.862640],[-9.274624,-9.899577],[3.879425,7.469549],[-5.561896,-0.254961],[8.886714,-9.895887],[-4.203518,-4.158968],[8.699574,1.005070],[-7.328467,5.606609],[-8.126207,8.958349],[1.856427,2.229337],[3.848827,1.261158],[-4.356309,-0.452759],[-7.798078,-5.184207],[-5.856716,-8.492035],[7.692308,5.314327],[-5.925455,-3.044751],[-0.253796,1.092799],[6.499245,-2.246293],[-1.437492,6.688104],[6.235255,-2.981728],[-2.836786,-1.622740],[0.904262,-0.614220],[4.351252,0.139412],[-7.624919,-2.778280],[7.419136,-3.987592],[5.689946,0.012647],[-7.198101,-0.200042],[1.105932,-2.164087],[8.149708,-8.864463],[7.700824,-2.623919],[6.882836,-0.589163],[9.273833,-3.459967],[-5.523327,3.409070],[9.058866,8.804002],[2.914480,-7.554584],[-9.043685,-9.750224],[1.259727,8.363882],[5.233081,5.999500],[1.526013,-3.934743],[0.017941,5.431429],[1.123256,5.571783],[-1.341666,4.431791],[-6.063939,-6.190448],[-2.388050,6.071517],[7.726497,-1.069438],[-7.620726,0.310298],[5.093507,-3.030700],[-0.461690,-9.781805],[-6.131127,3.147742],[2.217439,5.616100],[-3.860607,-9.490222],[-7.947957,-6.376254],[-9.802846,5.196420],[1.344116,-7.825467],[-2.831928,9.279408],[3.363503,0.382326],[2.318524,-3.478456],[4.493349,-8.690869],[6.908647,-5.483809],[-1.758700,6.126679],[7.247239,0.832735],[-9.555119,0.565519],[-4.587223,2.407474],[-3.591902,-1.557060],[4.526254,-8.308008],[-5.740268,-4.191522],[-9.343703,2.544080],[-7.753896,3.027079],[7.181350,-4.507618],[6.686162,1.674578],[-0.633447,5.379947],[6.515275,-3.199386],[-0.223417,8.368937],[3.788147,-5.709418],[-7.153558,1.558775],[-9.072303,-9.449290],[2.695640,7.574873],[-9.301107,8.130301],[-6.660770,7.608911],[-5.286392,-7.615481],[6.972776,4.586098],[-6.813894,-1.687480],[9.522865,5.337403],[-5.783757,-9.802110],[-1.413569,-3.440167],[-9.764332,5.588147],[-1.284616,-4.656219],[-8.395563,2.733476],[-0.128778,-5.792469],[-3.757978,5.778542],[-6.004030,-8.281903],[-0.811252,0.563622],[-3.407388,1.005075],[5.274160,0.585184],[1.999282,-4.095566],[8.662029,5.256263],[-7.951542,-1.054884],[-9.161187,-9.035668],[-1.940882,-0.485222],[5.420194,6.578166],[1.516958,-0.213982],[9.298990,9.395847],[8.766490,-8.493427],[4.435398,-4.173092],[9.515828,5.389405],[-6.038680,4.653355],[-4.618385,7.912062],[9.209368,5.798009],[1.200770,8.823053],[-5.450595,-7.149915],[-3.479265,-5.990616],[-8.873687,6.050401],[9.642002,-5.762524],[-5.059383,-8.668947],[0.401819,3.525771],[-6.133494,2.483236],[-9.831652,-9.952892],[7.171696,2.597833],[5.122114,-8.037264],[-3.188553,3.217315],[-8.556159,-4.345304],[8.516555,5.223125],[-6.005389,0.448556],[4.737781,6.107726],[2.845156,-4.848011],[-6.273407,-9.209006],[3.576794,0.221510],[-1.579856,1.539985],[-6.789672,-3.938618],[-9.667467,-7.827036],[-0.341673,0.744055],[5.350237,7.183788],[-3.307791,3.944043],[5.808508,-6.322240],[-0.054139,1.293157],[0.785692,2.361235],[-1.989117,7.692294],[4.857071,9.701021],[-5.087049,-0.476756],[6.448381,-2.714815],[5.838435,-4.619262],[-5.716355,-8.889806],[0.802217,2.040721],[-5.443869,-9.266203],[-4.613121,-7.809576],[-4.572685,0.311551],[-8.863412,-8.952755],[-0.799350,-9.582942],[-1.707213,-7.036595],[7.230710,-6.482541],[-4.080201,1.317922],[-5.891036,2.641637],[-6.281747,1.333264],[-5.089430,2.048124],[-4.968633,-5.881027],[-4.494229,-6.350478],[-6.856747,5.523177],[8.635770,-3.210509],[-0.782376,2.194098],[6.218712,7.310649],[-4.667031,-5.849307],[-0.154012,5.834857],[3.177692,1.758322],[-1.669222,9.870778],[-6.641599,8.485412],[-9.657047,-3.203008],[5.469448,0.631849],[-5.136837,-6.314943],[6.896969,3.728076],[-6.499409,-1.700329],[7.444554,-8.340851],[-1.851707,-4.648291],[-8.571862,-3.414017],[6.237935,4.702018],[-8.476072,5.199409],[-2.760432,0.149035],[2.246103,4.791982],[-9.881935,7.759251],[9.053856,6.895193],[4.621716,-7.301815],[6.932249,-3.682239],[2.492476,-0.502620],[2.188399,9.894428],[2.736717,6.595483],[4.369666,6.272517],[6.333026,2.466298],[-3.169060,-7.576309],[-8.523491,0.057202],[1.583248,-9.798740],[-5.596555,4.741757],[2.756763,2.499657],[5.059619,3.148298],[3.085448,-4.320953],[7.648790,0.595494],[4.802853,-9.357130],[-8.026584,5.865680],[1.442295,2.147878],[-7.218768,4.335032],[5.495228,3.878335],[-1.559731,1.081836],[0.456328,-4.431453],[-4.036854,-1.279011],[2.654640,6.814258],[-1.445079,6.588360],[4.696458,8.526872],[0.660700,0.622713],[7.583403,-3.960628],[3.544771,8.527838],[4.387806,7.843220],[0.489481,6.467219],[-3.124098,7.043176],[-9.915919,6.629796],[1.068281,3.856250],[6.191274,9.937571],[3.330099,-0.217420],[7.338421,0.458910],[4.300479,-9.924320],[-4.289359,6.507979],[0.383898,-1.317354],[-8.553864,0.303937],[-1.548612,-2.784575],[6.532689,6.067208],[5.926813,8.087778],[0.626223,-1.974463],[4.369831,-5.297712],[-0.513784,6.331737],[-6.070934,5.353255],[1.506461,-6.934679],[-3.651726,0.941276],[-9.267300,-9.244629],[4.158168,-7.158382],[4.310914,5.717116],[-4.039671,-6.701915],[-9.208363,-7.793393],[7.521348,5.955098],[-8.217794,0.965915],[-2.198135,-1.370254],[0.802259,0.381038],[-0.180876,1.706367],[-2.614147,-9.178174],[-9.023571,8.123789],[-3.911716,2.204198],[-3.146310,-0.573123],[-8.638047,5.603221],[4.618906,0.779209],[-3.114672,5.240934],[5.463168,-6.564441],[5.564491,-2.508424],[-1.146791,-8.744420],[2.596846,-2.028252],[-1.807475,-0.885942],[-7.125399,-0.347330],[2.109180,-8.074158],[-9.409114,-7.190008],[1.316703,5.607913],[3.742174,-0.205322],[3.247697,2.431843],[8.043062,-7.819108],[-7.407604,-3.736780],[-6.053228,-9.841762],[5.139532,-8.569056],[-2.837908,1.812735],[4.932701,6.840692],[-3.068584,-0.055977],[-1.884816,-2.476683],[-6.307805,-4.725768],[1.562799,4.636020],[4.506621,9.586152],[8.362787,-7.432565],[-0.637948,3.108733],[-4.540191,-6.458889],[-5.953919,-4.229640],[-7.022406,-2.744895],[-0.928326,-9.122251],[-0.271782,3.827272],[9.153356,-6.454130],[-3.734651,9.203340],[-7.147659,9.933167],[6.148554,9.747838],[-6.532126,-3.318220],[-2.465050,8.302011],[9.692323,-7.774245],[-7.556480,8.206302],[-9.135482,-0.434094],[-8.049302,4.242829],[-7.497819,8.247017],[-8.992765,7.329272],[0.202540,-9.086902],[2.675377,-5.062686],[3.596210,-0.625550],[-8.256072,8.826321],[9.259637,-1.926620],[8.916119,-7.952528],[-1.837350,6.304079],[-5.090440,3.097089],[2.321697,4.697093],[-2.495089,1.298043],[-5.504225,2.297891],[-1.491880,6.963805],[-2.227267,5.344490],[7.661412,3.798238],[-1.382277,-0.579145],[9.675167,-5.161871],[5.071336,4.631893],[3.979873,9.459541],[-6.514370,-9.141965],[-2.280770,-8.871152],[5.231410,-3.107086],[9.049384,-3.652151],[3.821474,-8.387670],[4.112084,0.268920],[-4.350865,-8.595102],[3.174116,2.326686],[-6.767229,-6.985667],[2.534379,1.276623],[6.108076,2.216127],[6.059814,-7.867883],[6.118659,5.422960],[7.401051,6.596023],[-3.615485,5.773867],[-4.188398,1.684627],[-1.326796,1.276187],[7.334560,7.048411],[-3.127650,9.271253],[-2.305156,-4.692769],[1.967087,-9.225136],[-6.174170,-4.807741],[7.318191,5.888157],[3.133364,-7.112584],[-6.363092,8.516814],[-9.998224,-5.059471],[-9.540691,-0.396409],[2.223360,-2.902642],[4.164376,5.184551],[-4.289651,-7.822470],[8.563172,9.540544],[-0.973690,5.098422],[0.720698,-9.255654],[5.085815,4.653956],[9.377360,-8.813058],[-0.018810,5.814358],[-2.106801,-5.631768],[-2.642846,-8.372933],[-0.737247,-9.744099],[-2.721774,9.874107],[0.240276,1.304957],[8.289336,-3.152857],[6.523651,2.321668],[5.465375,9.695390],[-7.107852,-5.144663],[-8.817883,-0.033413],[1.143660,6.674457],[-5.670533,8.442112],[5.311304,-6.688457],[6.226200,0.895001],[-0.952744,5.338564],[4.793626,6.970943],[-2.095515,-2.034701],[-6.793467,1.240095],[-4.136118,3.891167],[1.948345,-7.644737],[-7.452169,4.140266],[4.319394,-2.749103],[-1.880242,0.230667],[-0.083059,3.347088],[-0.673677,5.739254],[-6.518689,-0.890651],[9.965970,-2.514023],[0.437067,7.242043],[7.516565,6.437727],[3.193618,-6.619415],[4.494284,6.898095],[-5.558146,-5.022638],[6.970360,-3.096643],[-2.989349,-7.499503],[-0.171436,7.217992],[1.402439,0.392456],[8.871820,7.347138],[-1.593427,-4.334671],[6.587102,6.255629],[-1.204506,-5.385175],[9.172752,-9.563879],[-3.439211,-5.983393],[9.091404,-6.105673],[-0.630204,5.463228],[-8.264282,6.548397],[4.983960,4.973214],[4.256736,-5.027969],[-2.662251,5.405134],[1.341000,-3.936262],[-0.673165,0.060523],[-2.713977,-6.793680],[9.756121,-1.033712],[-7.909454,9.852432],[-0.487373,-3.634732],[1.943260,2.900005],[-4.747415,-7.088802],[-5.147814,4.452274],[9.425501,-7.564972],[-2.596885,-2.843345],[2.096032,8.761131],[-1.874851,7.829984],[5.457113,0.223005],[-5.685943,2.910108],[3.357899,8.391152],[-0.910013,9.122436],[5.065875,1.476836],[-8.425394,9.556314],[-0.186268,-3.285106],[2.400821,2.060735],[3.660006,-9.965617],[-6.728897,-8.364526],[7.014257,8.142250],[-2.664617,7.657281],[6.124806,9.356294],[-9.137336,5.946205],[-4.675730,-9.992880],[4.999869,-3.071879],[-3.698802,-4.032576],[-7.365870,-3.433059],[-4.950735,8.295131],[-1.431635,-7.717282],[7.631781,-8.106362],[3.902730,6.379052],[3.295367,8.374070],[8.938770,6.210597],[-3.831414,-9.070558],[4.164410,-8.559288],[0.281775,-3.134901],[-9.101674,3.706998],[9.451020,-2.432135],[6.276710,-7.588434],[1.919401,7.696514],[3.621695,-6.569180],[-1.022694,4.945611],[9.990738,-8.898293],[4.236888,6.185207],[6.030750,-1.005291],[-7.670144,0.142419],[-8.915523,-5.643925],[-2.622196,-8.515511],[-3.530009,7.769686],[-6.090840,-3.844459],[7.549428,-8.477041],[-0.163083,-1.602949],[-2.854857,-0.784491],[6.869663,-8.121688],[8.802274,6.447970],[-5.021472,0.962145],[-1.790341,6.867192],[0.987042,2.180545],[-8.859740,-3.146608],[7.909016,7.670987],[5.034896,-0.772804],[1.148760,-1.209498],[0.842167,-6.147438],[9.048024,-6.981854],[2.938843,-7.948212],[-0.973493,1.556811],[3.481989,8.789031],[-0.085764,-2.038494],[-0.247733,3.683236],[4.880084,-8.689250],[1.378471,-0.118059],[-7.711960,6.398980],[2.608209,4.946959],[2.971536,-6.756805],[-4.348522,3.333627],[-3.721519,-0.906040],[-6.436999,8.508084],[1.194218,-1.513652],[-5.673484,6.176434],[6.388817,-2.375754],[5.658176,-1.957376],[-7.767030,6.962471],[-4.760271,-0.159860],[1.016853,4.051173],[-8.278202,0.937294],[-7.231047,-2.161894],[2.730414,-3.667463],[-1.799795,7.979218],[-0.155581,-9.710086],[-6.376629,0.924066],[-0.264791,-8.169316],[-6.513220,1.374084],[-0.459041,-1.698924],[-3.451062,5.602833],[-0.549963,2.277316],[6.521949,-6.421297],[-2.743290,-2.108809],[9.765040,-4.951224],[9.699066,6.927265],[-4.407053,-2.240804],[3.776026,-7.029381],[-8.447635,2.633044],[6.075064,7.488665],[0.563746,-1.433095],[9.951995,7.538463],[-5.148184,-2.695229],[-8.311207,4.535735],[0.289617,1.194325],[-6.110733,-1.464628],[4.282859,7.740208],[-6.114773,1.346106],[5.228674,-9.603792],[1.273872,1.449221],[3.407902,4.726366],[0.129822,-0.480084],[4.182705,0.119549],[7.781485,-9.034172],[-0.754570,5.355533],[-0.259609,-7.340460],[-2.417481,-9.858854],[-6.886726,2.104185],[-7.881235,0.413003],[3.114508,-1.651404],[5.839279,-2.665353],[2.720842,-7.358663],[4.110241,3.653737],[-2.421687,1.620820],[-7.531573,-2.464760],[3.166163,-5.146026],[8.555238,1.700227],[9.772619,4.534968],[0.364991,-9.974757],[-5.329133,-5.556568],[-4.739551,8.062478],[-8.767892,-1.207042],[4.667258,8.483039],[-6.576649,-7.383365],[-3.202544,6.209412],[6.480449,-4.551860],[-2.528189,6.543294],[3.497370,-7.628412],[8.167738,7.536064],[-4.942500,-1.341996],[-1.252413,-1.034590],[5.160884,-7.673113],[-7.350809,-3.472905],[-3.241006,7.516601],[3.012557,6.832418],[-5.748659,-4.267093],[-0.100464,6.470291],[3.749418,-9.663548],[-5.273151,3.772431],[1.590568,8.153316],[5.987522,6.856961],[-0.656496,-4.427200],[9.107313,0.852988],[-4.970183,-1.099917],[5.087263,7.182447],[9.648876,-4.840120],[1.313913,-9.617375],[-2.229292,-4.921166],[5.099827,2.627118],[-0.257879,7.683676],[-7.091240,-6.592450],[-6.739434,2.107762],[-7.475111,2.033260],[-3.133552,5.270358],[7.056139,-8.012157],[2.896656,4.890794],[-9.125760,8.628951],[-7.778715,-7.037825],[2.822751,8.978450],[9.968640,7.950149],[-7.291849,-5.378410]], dtype = "float32")#candidate|6945|(880, 2)|const|float32
var_6946 = relay.var("var_6946", dtype = "int16", shape = (1456,))#candidate|6946|(1456,)|var|int16
call_6944 = relay.TupleGetItem(func_3213_call(relay.reshape(const_6945.astype('float32'), [1760,]), relay.reshape(var_6946.astype('int16'), [1456,]), ), 2)
call_6947 = relay.TupleGetItem(func_3216_call(relay.reshape(const_6945.astype('float32'), [1760,]), relay.reshape(var_6946.astype('int16'), [1456,]), ), 2)
const_6951 = relay.const([[-4.002278,-2.642822],[-5.716230,-1.394812],[-8.609199,9.825390],[-8.552908,-6.230178],[-4.035088,-7.385344],[7.969232,0.687190],[-1.273207,-7.741485],[7.698841,-9.278978],[2.677927,9.382548],[3.073436,6.877750],[1.782338,5.726977],[-8.742901,-8.032989],[1.419032,-4.086600],[-3.333830,-7.194278],[1.132822,2.176494],[-0.457791,3.428564],[6.670955,1.789238],[-8.087464,-6.950292],[-0.312784,-7.818706],[1.199462,3.073830],[1.589657,-8.162206],[8.775828,-6.550521],[6.454403,3.899100],[-4.226958,5.948643],[2.174489,-6.565423],[8.851292,4.844094],[6.196635,-1.558203],[-0.622206,2.235735],[-0.834495,2.598913],[6.564438,-4.714484],[-5.598376,-1.501899],[-1.299261,-6.000443],[1.853835,-5.699522],[8.533513,-3.478912],[9.073686,3.661651],[-8.100775,3.769787],[-9.324080,-4.755396],[9.627911,4.729883],[-8.973855,-6.989057],[8.159583,-5.259887],[7.055469,-1.325120],[-6.650257,4.421242],[7.622859,9.594718],[-4.791978,-7.954009],[-2.669774,-7.503480],[-0.630158,2.828334],[1.205915,0.992737],[-1.698354,3.050220],[-7.066973,-3.595144],[-7.648781,-0.720171],[-4.958785,6.804590],[3.196526,-1.598461],[-0.426981,7.858595],[-6.012842,0.385671],[-4.769685,-7.953853],[-3.408581,-7.347668],[0.895095,8.024772],[2.224679,-6.908563],[-8.668058,-4.889004],[0.094288,6.253748],[2.178027,-8.422133],[0.272351,3.545253],[8.323639,-2.482502],[-3.807159,-1.843918],[5.358908,7.254990],[-7.402144,-6.001602],[-7.857338,-5.557108],[8.685152,3.822175],[-5.090138,-7.878834],[-5.320426,7.729586],[-5.932011,2.058039],[-3.260409,-4.968870],[-6.510128,-0.301311],[7.731620,0.996819],[2.622311,-1.648684],[4.447368,5.701903],[6.268024,1.057270],[-8.990906,8.464420],[-8.483053,8.421884],[6.301638,-2.224401],[6.012638,-4.381803],[8.655037,-7.246901],[8.629521,-9.223360],[3.961232,-2.422995],[7.430910,-2.886518],[-3.657151,-2.010324],[-0.198312,2.817095],[-6.799536,2.682590],[9.446222,-5.987548],[2.116683,9.590211],[2.291946,1.607752],[-2.786383,-4.898072],[3.829664,3.225070],[-9.219597,-2.492019],[4.386670,-6.547335],[1.152222,7.432895],[7.978298,-1.373106],[2.449821,2.176936],[5.597532,8.990219],[-7.855792,7.447969],[-8.812837,0.987867],[3.403492,1.750055],[-0.452236,-3.885901],[-1.900615,-6.631259],[1.688593,-6.677677],[-7.439832,-5.290294],[3.615948,6.172379],[1.812563,5.446275],[6.311080,-0.181854],[3.243701,9.844554],[-5.831597,7.491471],[-2.058789,-8.736078],[-8.924292,-5.664280],[6.650720,-3.232401],[-3.640176,-9.020006],[7.937695,8.720851],[7.950803,9.942483],[8.760611,-2.948319],[-2.574490,-9.204241],[3.006539,-8.225676],[-3.506324,-9.776001],[1.204233,-8.073806],[3.668295,4.474922],[-5.014648,2.416630],[0.565105,-2.667777],[-2.337907,-9.324478],[0.421580,0.978986],[1.077333,-2.712827],[-9.269462,1.766433],[-8.701658,2.329808],[4.525507,-5.121730],[1.016772,0.655985],[-0.384884,9.852894],[-3.741092,7.216872],[6.383527,-3.807903],[-3.242092,-5.100425],[5.421074,9.790101],[9.759146,1.031870],[3.488274,-7.047858],[-7.538376,9.206889],[-5.956510,6.385480],[-1.280310,-6.724832],[2.576818,1.931988],[8.941869,-3.008658],[0.960720,-9.830949],[-2.968844,3.262875],[2.343625,-4.909107],[6.165246,-9.694838],[-9.443729,-1.160754],[-5.637835,-8.815781],[2.049354,-6.352065],[2.331605,-3.755908],[-6.838406,5.272495],[-7.284527,-6.541085],[1.590851,8.924592],[4.961356,-9.696412],[5.731800,-1.023851],[8.593825,6.870582],[-4.748939,4.328265],[-9.435060,5.727376],[2.644780,8.248038],[0.106704,5.442958],[-8.505389,-3.858506],[4.773154,-9.560388],[5.947234,-7.619450],[0.371744,-6.484401],[5.425516,-0.615047],[0.004643,-8.050361],[-8.166420,-0.289946],[-0.094389,-4.556906],[9.125051,-9.654069],[2.163542,8.294575],[5.270255,3.660970],[-5.703104,1.430429],[-9.050001,7.379382],[2.675158,-7.178230],[-9.849324,0.898772],[-5.748260,1.032671],[-5.076187,-6.361916],[-3.806695,5.371352],[-1.156687,6.010719],[-4.279650,-1.605232],[-7.604788,-4.112890],[-2.513987,9.384368],[4.244197,0.817200],[0.980294,9.195851],[-5.531378,8.885056],[-4.902490,-3.496950],[-8.555083,9.173987],[-6.208184,9.831236],[0.121205,-5.351654],[-0.301075,-6.145930],[0.548431,1.556605],[4.849798,-8.111286],[9.222635,-7.483217],[-4.641472,-9.512211],[-6.853736,7.821458],[0.975957,7.234320],[-5.134755,-5.915808],[-6.040421,3.644630],[-5.367894,-8.455551],[5.823281,5.660631],[-9.674723,-2.689936],[2.520501,5.328871],[-1.837785,-4.253287],[7.828449,9.225753],[-9.484780,-3.266264],[-3.738447,-1.306838],[8.883626,-9.115068],[6.712480,6.432888],[-6.276576,9.596566],[-3.018051,7.334645],[3.901771,-0.824166],[-5.175305,7.893990],[-1.504642,8.024187],[6.899632,8.118485],[-7.102016,0.178906],[-8.833289,3.957343],[6.810916,-1.826887],[-5.569236,-2.107486],[1.881107,-6.124510],[-3.255182,-4.068125],[-7.081417,-4.878693],[4.611157,-5.465211],[8.022777,-9.058876],[-0.544654,-4.805076],[-5.437859,8.095143],[8.245307,-8.143992],[-4.070598,-3.040898],[-4.893751,8.364209],[-9.312818,-6.564755],[-3.007863,7.202417],[6.770676,8.844164],[6.406621,4.302994],[-3.680079,-0.176656],[-2.268361,-0.449921],[-9.947077,-8.056907],[-2.352517,3.298760],[0.634403,-1.524082],[-6.491754,4.993225],[9.221719,6.602638],[5.424409,-1.103089],[1.024948,7.658178],[-3.080133,-6.876825],[-6.071882,8.498133],[3.705866,8.085090],[2.794342,-1.537909],[0.278774,0.324712],[-9.274359,2.862813],[8.575188,7.048053],[6.997426,-0.626110],[-9.132289,-6.671125],[0.721493,7.555290],[-6.972559,9.419431],[4.267308,7.689598],[-9.856473,1.790220],[7.983275,-0.073830],[9.606458,6.714972],[-0.486682,-9.967141],[-5.345499,9.131924],[-7.060217,-3.350632],[2.791767,-8.166878],[3.370738,7.823420],[-9.638294,-6.549896],[1.988771,-0.069316],[-8.030234,5.838825],[-6.208379,-8.199097],[-1.039693,-4.262014],[-6.808687,0.564892],[3.474099,-5.867804],[5.922782,-9.177157],[1.734052,7.548670],[6.677557,9.730745],[2.206365,-9.110886],[-9.631988,8.522353],[-8.323771,6.022236],[-7.190065,-3.960388],[7.517278,4.773493],[-9.634863,-5.350554],[-7.171595,-1.569931],[-8.151956,-4.439781],[7.698426,0.922582],[1.354053,-9.947160],[-3.604845,-0.876550],[8.773134,-9.546065],[-7.091188,7.649848],[2.450332,-1.374260],[-6.415434,4.499906],[-7.220659,-7.170003],[-4.752962,6.269399],[-9.174665,0.011953],[4.858568,-6.634131],[-0.352102,1.730972],[-2.976625,6.459153],[9.771681,7.158893],[1.423508,-3.994482],[-9.702369,5.590757],[-3.195285,-1.378884],[-3.922236,5.674119],[-1.606035,-7.562035],[5.088244,1.773523],[9.758960,2.431520],[-4.016787,-5.712397],[-6.962271,8.585240],[2.764449,7.748966],[1.164312,5.932552],[-4.953347,7.299585],[-3.772269,0.522834],[-6.238970,7.189411],[-8.481751,-4.661092],[4.803430,-1.543621],[6.175727,9.033440],[-4.080134,-2.311224],[-8.392567,0.145479],[-8.174239,8.788580],[6.739205,-5.464069],[5.771837,9.209528],[2.305187,-2.059663],[-8.721004,-8.553318],[-4.336950,-3.630900],[-5.293308,-4.462232],[-4.550204,8.754396],[6.591435,6.696686],[-8.091331,-0.384360],[6.709521,2.473960],[0.651013,-8.968326],[-5.361293,8.591419],[-5.283078,6.015882],[-9.933647,4.463199],[5.905973,1.411344],[-1.111782,5.213709],[8.616327,-7.376879],[6.375008,6.860457],[-2.611508,-0.666596],[-9.460271,9.680372],[-2.141720,0.458759],[7.347221,8.064630],[-2.155413,4.320115],[-0.838489,4.793928],[-6.035122,-2.370919],[0.146187,-0.969507],[1.334197,-4.256994],[-1.663784,-0.505291],[-3.606645,2.569266],[9.768522,-6.961007],[9.400411,-9.604349],[0.466303,7.038861],[7.319691,3.841115],[8.683071,-0.995055],[2.177364,-3.313320],[9.338501,-4.071968],[5.327780,0.254093],[-7.811344,-6.561088],[6.688197,5.578004],[-3.722537,-5.052295],[2.198484,-8.238180],[9.362346,7.917861],[9.688894,-8.511530],[6.855795,-0.182316],[-0.206077,1.881883],[4.913014,-2.006053],[-6.394008,1.321502],[5.463534,-9.139816],[-1.328259,1.713492],[-9.471554,-0.986313],[5.008871,-8.008111],[6.869123,5.029266],[-6.447779,-6.157498],[-2.648308,-8.326395],[1.679163,1.110106],[7.100573,2.071852],[-5.612001,0.431570],[0.537066,-5.871341],[-7.764089,1.434683],[4.160428,1.636256],[8.434946,1.066967],[-9.185782,-3.059418],[-4.644775,-7.276531],[-5.997751,6.792190],[1.970002,4.244868],[-1.658775,6.445542],[-9.071372,-9.594231],[0.418008,6.046267],[9.789850,-1.299273],[-1.925090,2.695394],[-8.353190,-4.300814],[6.000288,9.692498],[-4.001010,-2.989043],[-9.816282,0.383145],[-4.169245,-5.738788],[4.527326,6.512763],[-4.709557,-9.787680],[-8.134974,3.557783],[-5.140836,5.516863],[3.578645,-8.401929],[0.956641,-6.991609],[-5.579861,-8.627183],[2.998954,-8.349474],[-4.618463,-4.497934],[0.411996,4.897331],[-9.302251,-4.766752],[-7.395311,2.127062],[-5.271953,6.136053],[-0.111598,1.988517],[3.353707,8.296463],[-4.356643,5.508651],[5.960236,8.578968],[3.871638,9.683123],[-4.252395,-9.043582],[0.270724,-7.901894],[9.025125,-5.595572],[-7.274518,-8.417365],[1.480288,-3.003424],[9.007511,5.379792],[7.612887,9.303113],[3.741048,7.798111],[-3.342322,3.033393],[3.469219,3.479154],[4.860374,-8.039470],[8.867015,-5.140343],[-1.850054,-4.288772],[-5.569070,5.540576],[-2.076718,-6.996206],[0.160323,5.594314],[9.458224,3.603292],[2.613234,4.988060],[-2.073962,-9.064634],[-4.754901,8.904174],[9.501680,-5.942886],[3.636511,-9.659837],[-3.132573,8.150904],[-9.568220,7.069576],[8.890036,-3.291934],[0.649593,-3.581400],[9.907288,8.658955],[1.003330,-1.907683],[-5.225055,-2.914957],[-6.284772,-7.530581],[-6.056636,-9.522204],[-2.051187,-8.859311],[4.579390,-8.397374],[2.204170,-8.834243],[2.223011,-3.219616],[-2.844828,-3.257594],[-7.914218,-1.273455],[0.461789,7.981697],[2.855181,-6.647723],[-5.500753,5.770333],[5.728493,-8.107107],[-7.027152,2.238122],[2.178451,-0.940307],[-7.265768,-8.198791],[-1.362083,-0.575450],[2.226886,4.707805],[7.714526,3.125701],[-7.629764,1.958996],[-4.669257,-4.452848],[6.666599,4.394139],[-3.957040,-0.654081],[-4.079390,0.188731],[-1.038663,-2.376209],[4.227699,-0.349376],[1.809764,-6.726643],[-2.682254,0.039326],[-2.941799,-1.743489],[2.647555,-6.081976],[2.176100,-1.647832],[5.527161,-1.421528],[2.334753,-2.305474],[-4.974093,-5.998384],[-0.153177,-0.927840],[-5.490637,7.420576],[2.162032,-6.645045],[9.422108,-8.989859],[-0.247395,-7.878976],[-6.601283,3.316366],[0.756181,5.975989],[-0.321285,8.413022],[-4.330657,9.877445],[8.397967,1.506540],[-4.620291,0.366590],[-7.596221,3.042023],[7.127765,6.983703],[-5.782065,3.134792],[-3.327509,-0.543431],[-8.392538,8.498843],[1.940501,-1.729966],[3.314726,0.490648],[8.420663,-7.333146],[9.975856,-2.608542],[6.502099,-5.738103],[-3.905510,-5.054870],[-5.443966,7.929500],[-6.135749,-7.827931],[-1.871059,9.613410],[-3.901858,0.217112],[0.815157,-7.927933],[1.035989,2.428584],[-8.055055,7.474211],[-3.404402,9.040039],[-2.312511,0.956571],[4.408654,-9.611330],[-6.460354,3.057149],[-1.331308,8.649010],[-2.830460,-7.649796],[-5.529495,6.681331],[-4.199303,-9.540501],[-9.921503,3.381100],[-4.519683,4.128662],[-3.008892,4.844270],[4.807326,-6.242889],[-1.836194,-5.894087],[0.116127,-8.138090],[-5.102122,-0.201791],[-7.199394,4.025321],[-9.248685,8.109142],[-2.767148,-0.735000],[-3.468152,6.628814],[-2.891240,-2.295777],[1.488987,-2.474910],[2.135361,9.308080],[-7.042634,-6.663852],[-0.086151,8.751743],[2.421996,9.517114],[9.021327,-4.802819],[-4.954416,-1.065596],[4.874708,7.763598],[2.497042,1.864968],[-2.877078,-8.538873],[-5.345789,-0.340095],[9.631101,4.000904],[-3.174366,-0.885411],[-6.128771,-1.157928],[-7.945196,-3.914102],[1.167094,8.150484],[1.169514,5.961521],[0.976818,-5.393717],[8.867036,-6.253620],[-6.724748,0.717416],[-9.704740,-0.666601],[-8.751125,4.337937],[5.740771,4.334698],[5.885880,2.525190],[2.234802,6.747992],[8.066865,0.720835],[-2.011062,2.374524],[3.492846,6.650322],[-1.754347,8.003278],[-9.250415,7.551325],[-6.505494,-3.421487],[7.091602,-7.365305],[3.936337,9.006616],[3.979178,4.069934],[-3.689263,-3.802990],[8.136978,-0.564393],[2.693939,-8.220551],[-0.156280,-1.818904],[-8.321610,0.496016],[-4.041786,8.764643],[4.155981,-0.259227],[0.552879,-5.931597],[-8.598498,5.791558],[-0.622560,6.216708],[4.725321,-8.057909],[-4.063551,-4.544676],[1.717211,-8.502239],[9.329086,3.967865],[3.547804,4.387818],[1.909473,-1.440072],[-2.091018,8.432018],[4.134004,1.131773],[5.098542,7.183142],[-3.746893,-4.324727],[0.968168,4.494283],[-7.334305,4.897251],[7.123401,-4.376730],[-7.743828,-9.351471],[2.546888,7.471374],[9.683532,0.036487],[-1.012938,-8.802551],[0.831996,8.115444],[8.754063,8.428485],[0.284855,6.362460],[-2.316331,-4.633812],[8.096343,5.032890],[-6.391177,9.385374],[6.868117,-9.607659],[0.548108,-2.668042],[-2.119888,4.221391],[4.738896,8.460970],[8.674382,7.753693],[0.817110,-1.470666],[-7.267700,3.905717],[7.331685,-2.165249],[0.826216,-0.618588],[6.976443,9.206166],[-8.172079,-2.916500],[-6.834390,7.045867],[-4.008446,9.022966],[-7.007392,-7.217725],[4.037382,7.496750],[6.820878,-7.955806],[0.705319,5.311681],[1.492389,-1.543182],[-7.420617,2.728710],[-2.526138,-7.116366],[0.324649,-4.492252],[-7.732462,2.958388],[-2.349123,-6.192780],[-5.902176,9.623275],[0.309336,7.967792],[2.077911,8.483631],[-5.357578,-5.150726],[5.261915,4.720070],[-3.799662,-0.745548],[0.387610,0.726576],[-4.061775,0.861577],[-7.383919,-6.793175],[6.832404,-4.578838],[5.633982,-5.877749],[4.880816,3.072031],[-4.880736,7.800763],[-0.382368,6.189585],[0.080372,-8.932874],[-5.315545,5.471897],[-6.933208,-4.258165],[0.977207,-3.655184],[-9.399098,-6.857926],[-6.653953,-4.022115],[-0.689607,9.403144],[2.039025,-4.094210],[2.640370,3.676953],[-6.607475,-2.341240],[-1.677514,4.839301],[-1.001360,4.933757],[-0.936654,-0.049721],[7.650311,7.160301],[-8.010575,-9.794045],[2.932864,0.514701],[9.609232,-4.922561],[0.360129,-0.124955],[-3.685938,7.764980],[-2.346582,1.740976],[-1.576499,3.981793],[4.292113,6.801601],[4.887050,8.478196],[2.012139,-3.233025],[9.878651,-5.859083],[0.357838,3.890441],[-2.321334,-1.717702],[3.830346,-0.379628],[0.601418,2.227018],[-4.732381,2.412940],[-1.144252,3.579324],[5.029534,3.947602],[-5.886695,8.725993],[-0.387296,8.101776],[5.739855,0.181501],[-8.362235,-7.886763],[2.776982,-2.500179],[-0.025949,-9.998305],[-1.528360,-0.875589],[5.340773,0.577533],[-5.903768,9.155779],[4.086565,1.285236],[8.893787,2.755399],[-5.308847,5.591272],[5.269142,-7.416434],[1.838729,-6.529310],[-2.401924,5.576034],[-3.586108,6.153657],[8.485269,-6.150094],[-8.385046,9.608870],[-5.782181,0.952072],[-1.870800,8.554561],[-3.447140,-3.399745],[-6.557683,0.080080],[6.908437,-2.614620],[6.759215,-7.754775],[-6.411011,4.928772],[6.685891,-4.105572],[5.329488,-0.661189],[9.121582,8.640408],[4.867189,3.716226],[0.921698,-6.198579],[-3.715249,-6.388756],[9.205583,-1.442373],[5.380103,-1.868413],[9.744246,4.019731],[-8.522353,-4.072209],[2.228944,0.350193],[8.868187,-1.427942],[3.376243,-4.850949],[3.401223,-8.793607],[8.086556,-1.870484],[-2.869954,0.424645],[-5.916555,4.922635],[9.376377,-6.052811],[3.944606,4.906012],[-9.607269,8.963780],[2.244232,8.791237],[1.469253,3.797275],[2.995446,6.703978],[-7.410674,6.469376],[0.226534,2.934190],[-6.936986,9.994288],[9.866117,6.497219],[-7.242609,0.224456],[-0.496418,-1.531660],[-5.711541,-8.885993],[-6.752925,-0.019862],[8.286085,2.300813],[-5.423507,5.840387],[-1.693018,-0.676784],[5.955632,4.367729],[0.962258,1.904839],[-8.334283,3.441451],[0.629419,-8.134292],[0.214646,-7.598889],[-3.912642,-4.892568],[-0.613562,8.848009],[-3.353198,-8.896492],[9.474989,-6.175954],[5.072138,-7.894138],[9.017550,-6.829128],[-6.125700,-0.107784],[2.502911,-3.517585],[-3.648036,-0.511594],[-0.223515,3.486574],[-3.448469,-8.897139],[-8.232007,-8.312238],[7.214218,2.705941],[-5.978859,7.564435],[-2.727341,-8.751952],[6.643261,6.705229],[8.442074,-9.926248],[6.054853,1.577793],[-9.539737,-2.378297],[-4.044861,-9.583115],[4.110038,-9.682320],[6.148698,-4.628723],[-1.428385,-1.686866],[1.407428,1.342913],[8.786768,-9.310795],[-6.511605,-0.137679],[-7.327550,5.396629],[1.635288,-1.135890],[0.003781,-5.315055],[-2.650143,-0.040273],[-6.621773,-2.461529],[-7.148089,-2.882744],[-5.091207,-9.414415],[-4.969023,1.481191],[6.286880,0.042894],[-8.366658,-7.252406],[8.659247,-7.280317],[9.272973,-3.652191],[0.652639,-4.107480],[-5.962336,-2.361638],[9.285068,5.879101],[0.325245,-1.963523],[9.899195,-0.896393],[9.449715,6.385080],[9.896660,2.591655],[-2.254367,-8.080304],[-3.472587,0.580365],[-5.290570,9.240103],[8.238094,2.116202],[0.051169,4.742616],[-5.650931,-0.057616],[-4.982180,-4.543773],[-2.017720,6.058143],[2.740745,-7.760466],[-5.848106,-0.511648],[3.995186,-7.851277],[1.415851,-4.324044],[-6.551946,4.270293],[0.138016,-6.851315],[-3.554614,5.630772],[-3.580190,0.726020],[8.980068,-3.496728],[-8.783960,-4.955817],[-1.503269,-6.600106],[-7.055088,3.331817],[-8.376374,1.782212],[-5.260194,-6.761568],[-5.428978,7.695310],[-9.812166,-2.742691],[5.216601,2.122802],[-1.336106,2.729019],[-9.392668,-7.727565],[-2.549052,4.760193],[-4.848486,-8.670977],[9.544467,1.252060],[0.262395,-4.210044],[-8.201657,5.746806],[9.451589,9.495286],[-7.147737,4.854647],[-2.231516,2.255236],[4.853895,1.321553],[-8.106016,-3.236728],[-9.267655,5.384455],[4.840111,7.356011],[6.084131,0.761237],[5.195626,-5.302092],[6.478898,8.474328],[6.394499,0.908315],[9.562356,-1.205075],[-4.088819,5.280873],[6.040759,-5.394483],[9.327194,-2.349731],[-0.183995,5.477009],[-6.972801,3.397844],[2.699148,1.952763],[-7.939666,4.865110],[5.191878,1.750850],[4.542738,4.480320],[3.743797,0.180266],[1.220791,0.441123],[6.305157,-9.566972],[-3.279852,3.850792],[-4.681845,-1.925838],[1.257139,-6.170871],[-1.040744,0.333723],[5.403012,-8.031589],[-9.739605,5.135915],[6.287683,-6.539891],[9.727962,-2.343324],[-4.759443,-7.548771],[-8.041860,0.121889],[-4.797105,-7.500319],[0.986892,-8.387875],[-1.075450,-7.356799],[-2.556087,1.140505],[-8.432742,-9.130729],[-0.902007,-4.120356],[4.218173,2.150951],[8.482639,1.716680],[-1.781013,-7.420769],[4.967386,-8.320603],[7.178509,5.333392],[-3.646183,1.089468],[-2.886173,6.336746],[-7.306759,2.629332],[-4.904113,6.007718],[-8.202426,5.450558],[5.197990,-9.440922],[8.096667,-8.853238],[4.329386,-4.523064],[-6.505471,3.960764],[-4.402329,0.078292],[-3.865317,-1.114429],[1.307241,-4.967365],[-9.693458,9.349336],[-6.293987,6.872754],[-3.582176,-7.742379],[0.903322,-6.767161],[7.491170,-0.031726],[-9.368192,-3.466702],[-8.118732,0.897224],[7.282993,9.944755],[2.392854,8.431301],[2.548419,9.563667],[-3.369217,0.200374],[6.358216,-2.918456],[8.766540,-3.850830],[-9.424938,-5.236330],[0.870968,8.415474],[-5.725962,-6.592273],[3.187460,5.500258],[-4.429753,-2.815877],[-5.207143,-7.460358],[3.100928,-1.682041],[3.174529,-6.738790],[-2.108147,3.466540],[-4.079531,-7.337441],[6.572993,1.700935],[-8.973622,4.942026],[1.948888,4.152057],[-9.842888,9.963935]], dtype = "float32")#candidate|6951|(880, 2)|const|float32
bop_6952 = relay.logical_and(const_6945.astype('bool'), relay.reshape(const_6951.astype('bool'), relay.shape_of(const_6945))) # shape=(880, 2)
bop_6955 = relay.right_shift(const_6945.astype('uint16'), relay.reshape(bop_6952.astype('uint16'), relay.shape_of(const_6945))) # shape=(880, 2)
func_3703_call = mod.get_global_var('func_3703')
func_3707_call = mutated_mod.get_global_var('func_3707')
const_6964 = relay.const(-1.365259, dtype = "float64")#candidate|6964|()|const|float64
const_6965 = relay.const([1.926753,-8.993537,-4.649844,0.482574,3.512446,-2.387649,-1.877369,-5.578659,-8.329595,-8.611565,-1.744323,0.283978,-1.074827,1.360419,-1.003586,1.381877,-1.093183,-6.190035,5.881097,-5.518686,9.048669,-8.931180,-9.012832,7.977310,-3.247679,-3.540433,-3.028064,-3.667100,5.495304,-1.020201,-8.306776,-3.978935,4.041440,4.684254,-9.018598,4.088271,-2.227232,2.216292,-3.337601,6.295965,-4.400340,9.094788,-2.860822,-7.451608,-2.987327,7.605286,-0.151327,7.587503,4.782439,-4.180691,-0.749996,4.875683,-2.457368,6.421470], dtype = "float64")#candidate|6965|(54,)|const|float64
call_6963 = func_3703_call(relay.reshape(const_6964.astype('float64'), []), relay.reshape(const_6965.astype('float64'), [3, 6, 3]), )
call_6966 = func_3703_call(relay.reshape(const_6964.astype('float64'), []), relay.reshape(const_6965.astype('float64'), [3, 6, 3]), )
output = relay.Tuple([call_6908,call_6944,var_6946,bop_6955,call_6963,const_6964,const_6965,])
output2 = relay.Tuple([call_6909,call_6947,var_6946,bop_6955,call_6966,const_6964,const_6965,])
func_6968 = relay.Function([var_6946,], output)
mod['func_6968'] = func_6968
mod = relay.transform.InferType()(mod)
var_6969 = relay.var("var_6969", dtype = "int16", shape = (1456,))#candidate|6969|(1456,)|var|int16
output = func_6968(var_6969)
func_6970 = relay.Function([var_6969], output)
mutated_mod['func_6970'] = func_6970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_7006 = relay.TupleGetItem(func_3244_call(), 0)
call_7007 = relay.TupleGetItem(func_3246_call(), 0)
output = call_7006
output2 = call_7007
func_7022 = relay.Function([], output)
mod['func_7022'] = func_7022
mod = relay.transform.InferType()(mod)
mutated_mod['func_7022'] = func_7022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7022_call = mutated_mod.get_global_var('func_7022')
call_7023 = func_7022_call()
output = call_7023
func_7024 = relay.Function([], output)
mutated_mod['func_7024'] = func_7024
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7028 = relay.var("var_7028", dtype = "float32", shape = (4, 14, 8))#candidate|7028|(4, 14, 8)|var|float32
uop_7029 = relay.atan(var_7028.astype('float32')) # shape=(4, 14, 8)
output = relay.Tuple([uop_7029,])
output2 = relay.Tuple([uop_7029,])
func_7033 = relay.Function([var_7028,], output)
mod['func_7033'] = func_7033
mod = relay.transform.InferType()(mod)
var_7034 = relay.var("var_7034", dtype = "float32", shape = (4, 14, 8))#candidate|7034|(4, 14, 8)|var|float32
output = func_7033(var_7034)
func_7035 = relay.Function([var_7034], output)
mutated_mod['func_7035'] = func_7035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7059 = relay.var("var_7059", dtype = "float64", shape = (9, 4, 16))#candidate|7059|(9, 4, 16)|var|float64
uop_7060 = relay.log(var_7059.astype('float64')) # shape=(9, 4, 16)
output = relay.Tuple([uop_7060,])
output2 = relay.Tuple([uop_7060,])
func_7063 = relay.Function([var_7059,], output)
mod['func_7063'] = func_7063
mod = relay.transform.InferType()(mod)
var_7064 = relay.var("var_7064", dtype = "float64", shape = (9, 4, 16))#candidate|7064|(9, 4, 16)|var|float64
output = func_7063(var_7064)
func_7065 = relay.Function([var_7064], output)
mutated_mod['func_7065'] = func_7065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3957_call = mod.get_global_var('func_3957')
func_3958_call = mutated_mod.get_global_var('func_3958')
call_7124 = relay.TupleGetItem(func_3957_call(), 4)
call_7125 = relay.TupleGetItem(func_3958_call(), 4)
func_5916_call = mod.get_global_var('func_5916')
func_5918_call = mutated_mod.get_global_var('func_5918')
call_7139 = func_5916_call()
call_7140 = func_5916_call()
output = relay.Tuple([call_7124,call_7139,])
output2 = relay.Tuple([call_7125,call_7140,])
func_7143 = relay.Function([], output)
mod['func_7143'] = func_7143
mod = relay.transform.InferType()(mod)
mutated_mod['func_7143'] = func_7143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7143_call = mutated_mod.get_global_var('func_7143')
call_7144 = func_7143_call()
output = call_7144
func_7145 = relay.Function([], output)
mutated_mod['func_7145'] = func_7145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_7146 = relay.TupleGetItem(func_4167_call(), 2)
call_7147 = relay.TupleGetItem(func_4169_call(), 2)
output = call_7146
output2 = call_7147
func_7148 = relay.Function([], output)
mod['func_7148'] = func_7148
mod = relay.transform.InferType()(mod)
output = func_7148()
func_7149 = relay.Function([], output)
mutated_mod['func_7149'] = func_7149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_7163 = relay.TupleGetItem(func_3025_call(), 0)
call_7164 = relay.TupleGetItem(func_3027_call(), 0)
output = relay.Tuple([call_7163,])
output2 = relay.Tuple([call_7164,])
func_7178 = relay.Function([], output)
mod['func_7178'] = func_7178
mod = relay.transform.InferType()(mod)
mutated_mod['func_7178'] = func_7178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7178_call = mutated_mod.get_global_var('func_7178')
call_7179 = func_7178_call()
output = call_7179
func_7180 = relay.Function([], output)
mutated_mod['func_7180'] = func_7180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3025_call = mod.get_global_var('func_3025')
func_3027_call = mutated_mod.get_global_var('func_3027')
call_7181 = relay.TupleGetItem(func_3025_call(), 0)
call_7182 = relay.TupleGetItem(func_3027_call(), 0)
func_4088_call = mod.get_global_var('func_4088')
func_4093_call = mutated_mod.get_global_var('func_4093')
var_7187 = relay.var("var_7187", dtype = "int16", shape = (1456,))#candidate|7187|(1456,)|var|int16
var_7188 = relay.var("var_7188", dtype = "uint64", shape = (120,))#candidate|7188|(120,)|var|uint64
const_7189 = relay.const(-6.510104, dtype = "float64")#candidate|7189|()|const|float64
call_7186 = relay.TupleGetItem(func_4088_call(relay.reshape(var_7187.astype('int16'), [1456,]), relay.reshape(var_7188.astype('uint64'), [120,]), relay.reshape(const_7189.astype('float64'), []), ), 9)
call_7190 = relay.TupleGetItem(func_4093_call(relay.reshape(var_7187.astype('int16'), [1456,]), relay.reshape(var_7188.astype('uint64'), [120,]), relay.reshape(const_7189.astype('float64'), []), ), 9)
uop_7201 = relay.log(var_7187.astype('float32')) # shape=(1456,)
func_4544_call = mod.get_global_var('func_4544')
func_4546_call = mutated_mod.get_global_var('func_4546')
call_7211 = func_4544_call()
call_7212 = func_4544_call()
output = relay.Tuple([call_7181,call_7186,var_7188,const_7189,uop_7201,call_7211,])
output2 = relay.Tuple([call_7182,call_7190,var_7188,const_7189,uop_7201,call_7212,])
func_7215 = relay.Function([var_7187,var_7188,], output)
mod['func_7215'] = func_7215
mod = relay.transform.InferType()(mod)
mutated_mod['func_7215'] = func_7215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7215_call = mutated_mod.get_global_var('func_7215')
var_7217 = relay.var("var_7217", dtype = "int16", shape = (1456,))#candidate|7217|(1456,)|var|int16
var_7218 = relay.var("var_7218", dtype = "uint64", shape = (120,))#candidate|7218|(120,)|var|uint64
call_7216 = func_7215_call(var_7217,var_7218,)
output = call_7216
func_7219 = relay.Function([var_7217,var_7218,], output)
mutated_mod['func_7219'] = func_7219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5673_call = mod.get_global_var('func_5673')
func_5674_call = mutated_mod.get_global_var('func_5674')
call_7221 = relay.TupleGetItem(func_5673_call(), 1)
call_7222 = relay.TupleGetItem(func_5674_call(), 1)
const_7224 = relay.const([[[-3.600256],[8.105497],[9.202661],[0.639370],[-2.888134],[-0.573429],[9.745744],[-8.235142],[5.807076],[4.486898],[0.893490],[-4.044443],[-0.352834],[2.202896],[-9.162990]],[[9.828979],[9.718951],[-8.406169],[-1.999803],[9.760291],[-2.079902],[-4.934166],[5.802967],[-8.566112],[-4.488883],[1.834843],[-0.471253],[3.939094],[4.383152],[-6.109657]],[[3.858911],[-5.780889],[7.018095],[-1.271186],[-7.058131],[-7.463933],[3.708824],[5.779457],[2.347334],[0.436135],[6.165009],[4.357194],[3.775099],[5.389005],[0.929060]],[[-3.600657],[9.881212],[0.793784],[1.496531],[-6.543212],[-1.528333],[-8.423891],[2.146071],[-1.496067],[2.627283],[5.970284],[-6.456520],[6.532397],[3.361580],[4.108088]]], dtype = "float64")#candidate|7224|(4, 15, 1)|const|float64
bop_7225 = relay.less(call_7221.astype('bool'), const_7224.astype('bool')) # shape=(4, 15, 1)
bop_7228 = relay.less(call_7222.astype('bool'), const_7224.astype('bool')) # shape=(4, 15, 1)
output = bop_7225
output2 = bop_7228
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
var_7246 = relay.var("var_7246", dtype = "float32", shape = (2, 1, 5))#candidate|7246|(2, 1, 5)|var|float32
uop_7247 = relay.asinh(var_7246.astype('float32')) # shape=(2, 1, 5)
bop_7249 = relay.floor_divide(uop_7247.astype('float32'), relay.reshape(var_7246.astype('float32'), relay.shape_of(uop_7247))) # shape=(2, 1, 5)
uop_7252 = relay.atanh(bop_7249.astype('float64')) # shape=(2, 1, 5)
output = uop_7252
output2 = uop_7252
func_7266 = relay.Function([var_7246,], output)
mod['func_7266'] = func_7266
mod = relay.transform.InferType()(mod)
var_7267 = relay.var("var_7267", dtype = "float32", shape = (2, 1, 5))#candidate|7267|(2, 1, 5)|var|float32
output = func_7266(var_7267)
func_7268 = relay.Function([var_7267], output)
mutated_mod['func_7268'] = func_7268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4167_call = mod.get_global_var('func_4167')
func_4169_call = mutated_mod.get_global_var('func_4169')
call_7300 = relay.TupleGetItem(func_4167_call(), 0)
call_7301 = relay.TupleGetItem(func_4169_call(), 0)
output = call_7300
output2 = call_7301
func_7306 = relay.Function([], output)
mod['func_7306'] = func_7306
mod = relay.transform.InferType()(mod)
mutated_mod['func_7306'] = func_7306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7306_call = mutated_mod.get_global_var('func_7306')
call_7307 = func_7306_call()
output = call_7307
func_7308 = relay.Function([], output)
mutated_mod['func_7308'] = func_7308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7143_call = mod.get_global_var('func_7143')
func_7145_call = mutated_mod.get_global_var('func_7145')
call_7371 = relay.TupleGetItem(func_7143_call(), 1)
call_7372 = relay.TupleGetItem(func_7145_call(), 1)
func_4407_call = mod.get_global_var('func_4407')
func_4409_call = mutated_mod.get_global_var('func_4409')
call_7388 = func_4407_call()
call_7389 = func_4407_call()
func_5308_call = mod.get_global_var('func_5308')
func_5309_call = mutated_mod.get_global_var('func_5309')
call_7392 = relay.TupleGetItem(func_5308_call(), 2)
call_7393 = relay.TupleGetItem(func_5309_call(), 2)
output = relay.Tuple([call_7371,call_7388,call_7392,])
output2 = relay.Tuple([call_7372,call_7389,call_7393,])
func_7394 = relay.Function([], output)
mod['func_7394'] = func_7394
mod = relay.transform.InferType()(mod)
mutated_mod['func_7394'] = func_7394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7394_call = mutated_mod.get_global_var('func_7394')
call_7395 = func_7394_call()
output = call_7395
func_7396 = relay.Function([], output)
mutated_mod['func_7396'] = func_7396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6143_call = mod.get_global_var('func_6143')
func_6145_call = mutated_mod.get_global_var('func_6145')
call_7419 = relay.TupleGetItem(func_6143_call(), 0)
call_7420 = relay.TupleGetItem(func_6145_call(), 0)
func_3991_call = mod.get_global_var('func_3991')
func_3994_call = mutated_mod.get_global_var('func_3994')
var_7434 = relay.var("var_7434", dtype = "uint64", shape = (6, 20))#candidate|7434|(6, 20)|var|uint64
call_7433 = relay.TupleGetItem(func_3991_call(relay.reshape(var_7434.astype('uint64'), [120,])), 0)
call_7435 = relay.TupleGetItem(func_3994_call(relay.reshape(var_7434.astype('uint64'), [120,])), 0)
output = relay.Tuple([call_7419,call_7433,var_7434,])
output2 = relay.Tuple([call_7420,call_7435,var_7434,])
func_7440 = relay.Function([var_7434,], output)
mod['func_7440'] = func_7440
mod = relay.transform.InferType()(mod)
var_7441 = relay.var("var_7441", dtype = "uint64", shape = (6, 20))#candidate|7441|(6, 20)|var|uint64
output = func_7440(var_7441)
func_7442 = relay.Function([var_7441], output)
mutated_mod['func_7442'] = func_7442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5190_call = mod.get_global_var('func_5190')
func_5191_call = mutated_mod.get_global_var('func_5191')
call_7485 = relay.TupleGetItem(func_5190_call(), 0)
call_7486 = relay.TupleGetItem(func_5191_call(), 0)
func_6308_call = mod.get_global_var('func_6308')
func_6312_call = mutated_mod.get_global_var('func_6312')
const_7489 = relay.const([[3,7,7,7,-10,7,-7,-2,9,-5,1,6,10,-9,-6,-6,-10,-10,-9,-2,-10,-10,-7,-3,-8,9,4,-5,-3,-3,-1,6,2,-8,-3,-1,-3,-9,-5,5,1,-7,9,-1,4,9,-3,-9,-3,7,9,-8,-10,1,1,3,1,-1,1,3,8,-3,9,7,8,9,-3,-2,-5,-2,-10,-2,-4,1,3,-3,6,-3,9,-10,-3,8,7,10,-2,2,-5,3,5,7,8,10,-7,2,2,-6,-2,-10,-2,-2,-1,8,-9,7,7,-2,5,10,5,-9,5,-2,10,7,-10,-6,-3,9,7,6]], dtype = "uint64")#candidate|7489|(1, 120)|const|uint64
var_7490 = relay.var("var_7490", dtype = "uint32", shape = (1232,))#candidate|7490|(1232,)|var|uint32
call_7488 = relay.TupleGetItem(func_6308_call(relay.reshape(call_7485.astype('bool'), [968, 1]), relay.reshape(const_7489.astype('uint64'), [120,]), relay.reshape(var_7490.astype('uint32'), [1232,]), ), 1)
call_7491 = relay.TupleGetItem(func_6312_call(relay.reshape(call_7485.astype('bool'), [968, 1]), relay.reshape(const_7489.astype('uint64'), [120,]), relay.reshape(var_7490.astype('uint32'), [1232,]), ), 1)
func_6968_call = mod.get_global_var('func_6968')
func_6970_call = mutated_mod.get_global_var('func_6970')
const_7493 = relay.const([7,1,7,-6,-6,2,-10,6,4,1,-8,-2,-1,-10,-10,10,1,3,-9,5,-5,-5,-7,7,3,-9,-6,-1,-1,-8,8,-10,-1,-8,-1,-6,-8,-3,3,8,-8,6,9,3,-8,3,-10,6,-8,-2,7,-5,-10,-2,8,7,-7,2,-2,-8,-7,-8,-5,-8,9,10,-7,-1,-5,10,-2,-1,-1,7,-7,4,5,3,-8,-1,-1,3,7,-5,-8,8,-3,9,2,-7,-10,-5,5,-4,-8,-10,-5,-9,8,9,-10,-5,5,-4,9,-8,-4,-3,10,10,2,9,4,2,-3,-7,7,3,-6,-1,-10,-6,-1,-1,-6,-8,-4,6,6,-9,8,-9,8,8,-1,-10,7,5,-5,-6,-1,9,-5,3,-2,10,8,6,-3,3,5,-7,9,8,-2,5,3,9,9,-9,6,-3,-9,2,5,-8,-9,1,-10,-4,-7,6,-4,-8,-10,-6,-6,-9,-7,-7,-8,-3,3,-7,-4,5,-1,-1,-7,10,4,2,-4,-5,5,3,10,-10,-9,5,-9,5,1,-7,-5,-6,4,10,-2,-10,8,10,-9,-10,9,-4,-6,-10,-6,-5,-3,-1,2,6,-8,-1,-10,-4,-3,-9,-2,3,-3,2,10,-2,2,-2,7,-8,-2,9,2,-1,10,1,3,9,-7,-9,10,-9,-7,7,-9,-6,6,1,3,-6,1,4,-1,4,-5,4,4,-8,-6,-4,-1,-4,-10,-8,-8,-5,-2,-5,-3,3,-1,3,-2,-6,-7,-3,-3,-7,3,-5,10,2,-2,-8,-7,4,10,5,10,2,4,-8,-2,9,2,6,5,-5,8,-1,-4,5,4,-6,1,-4,3,9,8,-1,-1,2,9,-10,-9,-10,-8,7,-4,8,2,8,5,1,7,-2,10,-4,-1,4,7,-7,10,1,-8,9,1,9,7,9,-3,2,-7,4,1,2,-5,-5,2,1,4,-3,-7,3,2,8,5,1,-6,-1,-3,5,1,-3,5,-2,3,-8,-6,8,2,-3,8,8,9,9,2,1,3,6,-9,-8,4,5,-6,-9,-1,-5,8,-10,-3,-10,2,-8,-5,-4,-3,-7,10,-8,-6,-5,1,5,3,8,-6,-3,-10,-5,7,9,4,10,7,2,-7,10,7,7,1,-10,-4,5,-7,-8,2,6,-3,-1,4,-6,8,-9,3,9,-3,-1,1,2,-8,2,-8,-5,-5,-3,-8,10,-7,5,6,4,-2,-8,-2,-10,-1,-2,3,3,-4,8,7,1,8,-4,7,-4,4,3,2,-10,-8,-3,-10,10,3,7,10,4,2,-4,7,-10,-10,10,-6,5,3,-4,4,-6,-4,7,-8,3,10,-3,-5,-9,-7,9,1,7,3,4,9,-4,-2,-8,1,-2,-7,7,9,-9,9,10,-1,2,2,9,8,4,-4,10,-2,-6,9,-2,-1,7,-6,-10,7,1,9,-1,-5,7,-9,-7,-1,-1,8,3,4,-9,-8,-9,10,4,-10,-6,-2,-4,-2,-2,-4,5,6,-9,-7,-3,7,10,2,7,-9,-6,-10,9,-9,-6,6,5,1,-4,-4,3,-3,-1,7,6,2,6,-2,3,8,6,-3,7,5,-10,10,-2,-8,-7,-10,-8,7,-6,1,-2,-1,2,-9,5,10,-7,-3,-5,-2,4,9,6,-8,-7,-4,-7,-9,-10,-7,4,-2,-10,-10,6,9,-5,3,-4,-8,1,2,-8,6,9,2,-1,-6,9,-7,-9,-6,5,-10,4,2,9,-3,4,4,3,9,-10,6,-3,8,-1,10,6,7,-7,5,-4,4,6,-3,6,4,7,9,4,3,2,1,3,-7,-6,10,-1,-8,-4,5,-3,8,-10,3,4,7,-9,-5,-6,-5,-5,6,9,2,-7,5,-7,-1,10,8,9,-10,-6,3,7,8,-4,7,-8,-1,9,6,-9,-2,-2,2,10,2,-7,9,4,6,-4,5,6,-9,-10,-1,-2,9,-3,-5,-3,8,1,-3,-7,-7,4,2,-6,2,-4,6,-6,-9,-5,2,1,-7,-9,1,9,-6,-8,2,-7,-1,-9,-8,3,4,2,-8,-7,-7,-7,-2,-4,1,5,5,8,-5,-4,-2,10,5,-1,5,9,-4,-8,-5,5,4,9,-5,5,4,3,-8,-1,3,7,-9,7,5,10,-8,5,-6,-1,-1,-1,8,2,-6,-9,4,8,4,-5,-3,-10,1,-2,2,-7,4,10,3,7,7,-8,-6,2,-4,-1,-3,7,-8,2,6,3,-9,-9,-8,-10,6,6,8,2,-7,8,-5,4,6,3,7,-2,-2,-7,-9,5,-8,-9,-7,8,-5,-5,-1,-4,-7,1,-5,-8,-3,-7,-3,10,-1,8,10,-3,-2,5,-7,10,-8,-8,3,-9,-1,1,-9,7,-9,-2,-3,-4,-5,-8,-8,8,1,-10,-2,-1,7,8,2,-10,4,-10,6,2,4,6,10,9,-8,6,-10,-4,8,5,-9,2,6,10,7,5,-2,3,-5,-1,-1,-2,5,-8,-7,-4,-9,-10,10,8,2,1,4,-5,-6,1,-5,-10,10,3,4,-6,6,7,5,-5,9,-10,10,2,-2,-7,8,5,-7,7,-8,4,8,9,-7,10,-10,2,6,8,-9,-4,2,6,8,3,-8,-1,8,-10,6,-4,-2,6,10,-7,9,-7,1,-10,-9,-6,-10,3,-6,-7,-7,-9,-7,9,1,6,7,10,-9,6,5,-6,10,-5,4,-9,10,2,-4,-5,-6,4,-6,-1,7,4,-1,7,2,8,-1,-9,-6,10,-1,-5,-8,2,5,1,-3,2,-7,-7,-10,-7,3,-5,6,-1,2,7,6,6,-3,1,-3,-9,-5,-9,3,-7,-1,-7,10,5,-3,4,2,-1,8,-10,-7,1,-7,-7,4,9,6,2,6,-10,2,8,-5,-8,1,5,-6,1,5,-6,-2,4,-4,6,6,9,-1,3,-6,-8,-8,6,-9,9,-7,-3,-3,8,3,-7,1,10,-3,-7,-1,-7,-10,-5,1,3,3,6,-2,5,-2,6,-8,-7,-7,-9,1,-1,2,10,-2,-1,8,2,6,5,8,3,-8,-7,5,7,-4,7,-4,9,-1,-10,-10,10,8,5,-9,-3,7,3,-6,7,9,-7,-4,-9,-7,-5,1,-6,-3,6,9,10,-9,-9,-3,6,2,-7,10,-1,-4,7,-4,-8,-3,-10,6,-8,2,10,6,1,1,-4,3,9,4,5,-8,6,9,-2,5,-10,9,-6,7,-3,-5,-9,-4,6,-4,-7,-5,-2,8,-1,-5,-4,2,1,7,-8,-3,-1,-7,7,9,2,5,-2,9,10,2,-10,3,-4,7,5,2,9,4,-9,-9,10,-4,-1,-4,6,-4,-10,10,-9,7,9,1,-7,3,7,8,8,-8,6,9,-7,10,1,-3,-7,6,10,-3,2,4,9,-7,-5,-5,8,-4,-6,4,4,-10,10,6,-3,6,6,5,3,4,10,8,5,4,-6,-1,-10,1,6,7,-6,-5,6,-8,5,-6,1,-2,7,8,-8,4,-9,-7,2,-2,-10,1,-8,-2,8,5,-3,-6,7,-4,4,-5,4,-7,8,7,8,-2,6,7,-4,-3,-3,7,-4,9,8,-2,7,-1,9,-3,-3,-1,-10,2,5,3,6,-10,-1,-2,-2,-3,2,-4,-1,7,-3,-2,-9,9,2,1,-1,2,-7,-3,7,-8,10,-9,6,-5,-4,-3,3,-6,3,-5,-6,8,-9,4,7,-4,-1,-7,7,-7,-1,6,2,9,9,2,8,1,-9,3,7,4,-8,-7,5,8,6,-7,5,-4,9,10,-3,5,5,9,-5,2,-4,-10,4,-4,-1,-9,-9,1,-10,-5,1], dtype = "int16")#candidate|7493|(1456,)|const|int16
call_7492 = relay.TupleGetItem(func_6968_call(relay.reshape(const_7493.astype('int16'), [1456,])), 5)
call_7494 = relay.TupleGetItem(func_6970_call(relay.reshape(const_7493.astype('int16'), [1456,])), 5)
func_3703_call = mod.get_global_var('func_3703')
func_3707_call = mutated_mod.get_global_var('func_3707')
const_7496 = relay.const([[1.562260,0.610952,-5.996872,-3.860174,-2.280607,-8.668771,6.037965,9.429471,-4.500307,-5.969539,-7.821561,7.576664,6.829992,-4.786272,-4.896618,7.375709,1.297941,-0.407619],[-7.773993,-5.431244,8.791026,-0.746555,-3.583265,4.468622,3.471153,-0.266923,2.538295,-3.480163,-0.186211,-3.049521,0.462381,-3.580147,-7.697252,4.391321,4.049406,3.618994],[-4.301055,8.576192,-3.189217,2.183356,-2.998223,9.211903,7.921899,5.873685,5.123030,-2.595312,7.541005,0.727431,8.012982,-5.962303,6.186356,7.134997,-8.458301,-0.207657]], dtype = "float64")#candidate|7496|(3, 18)|const|float64
call_7495 = func_3703_call(relay.reshape(call_7492.astype('float64'), []), relay.reshape(const_7496.astype('float64'), [3, 6, 3]), )
call_7497 = func_3703_call(relay.reshape(call_7492.astype('float64'), []), relay.reshape(const_7496.astype('float64'), [3, 6, 3]), )
func_2260_call = mod.get_global_var('func_2260')
func_2264_call = mutated_mod.get_global_var('func_2264')
const_7503 = relay.const([8.166999,-3.129601,5.159700,-6.356587,6.205569,-6.370356,-2.803361,-3.477767,-0.748388,5.529478,-7.612466,-0.602527,-7.716560,3.202849,3.845150,-4.089541,0.098846,-6.104331,-0.795849,9.773472,-0.430479], dtype = "float32")#candidate|7503|(21,)|const|float32
var_7504 = relay.var("var_7504", dtype = "int64", shape = (605,))#candidate|7504|(605,)|var|int64
call_7502 = relay.TupleGetItem(func_2260_call(relay.reshape(const_7503.astype('float32'), [1, 7, 3]), relay.reshape(var_7504.astype('int64'), [605,]), ), 2)
call_7505 = relay.TupleGetItem(func_2264_call(relay.reshape(const_7503.astype('float32'), [1, 7, 3]), relay.reshape(var_7504.astype('int64'), [605,]), ), 2)
uop_7513 = relay.tan(const_7503.astype('float32')) # shape=(21,)
bop_7521 = relay.right_shift(uop_7513.astype('int8'), relay.reshape(const_7503.astype('int8'), relay.shape_of(uop_7513))) # shape=(21,)
uop_7529 = relay.log(const_7503.astype('float32')) # shape=(21,)
output = relay.Tuple([call_7485,call_7488,const_7489,var_7490,call_7492,const_7493,call_7495,const_7496,call_7502,var_7504,bop_7521,uop_7529,])
output2 = relay.Tuple([call_7486,call_7491,const_7489,var_7490,call_7494,const_7493,call_7497,const_7496,call_7505,var_7504,bop_7521,uop_7529,])
F = relay.Function([var_7490,var_7504,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7490,var_7504,], output2)
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
