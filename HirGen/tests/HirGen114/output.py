import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_178 = relay.var("var_178", dtype = "int32", shape = (1, 15, 7))#candidate|178|(1, 15, 7)|var|int32
var_179 = relay.var("var_179", dtype = "int32", shape = (1, 15, 7))#candidate|179|(1, 15, 7)|var|int32
bop_180 = relay.greater_equal(var_178.astype('bool'), relay.reshape(var_179.astype('bool'), relay.shape_of(var_178))) # shape=(1, 15, 7)
bop_195 = relay.subtract(bop_180.astype('float64'), relay.reshape(var_178.astype('float64'), relay.shape_of(bop_180))) # shape=(1, 15, 7)
output = bop_195
output2 = bop_195
func_200 = relay.Function([var_178,var_179,], output)
mod['func_200'] = func_200
mod = relay.transform.InferType()(mod)
var_201 = relay.var("var_201", dtype = "int32", shape = (1, 15, 7))#candidate|201|(1, 15, 7)|var|int32
var_202 = relay.var("var_202", dtype = "int32", shape = (1, 15, 7))#candidate|202|(1, 15, 7)|var|int32
output = func_200(var_201,var_202,)
func_203 = relay.Function([var_201,var_202,], output)
mutated_mod['func_203'] = func_203
mutated_mod = relay.transform.InferType()(mutated_mod)
const_322 = relay.const([[-3.950017,2.650831,6.915806,-5.853321,-9.617232,2.077502,-8.859136,1.563544,-5.084027,5.852185,-4.623056],[6.342269,-4.926076,6.477138,-2.521220,5.152764,-5.918108,9.707202,-2.342803,3.344807,-7.441088,-5.557084],[-3.491759,9.249453,-5.677549,0.731596,2.076719,-1.444877,2.681856,-2.936520,-6.867078,-5.749169,-8.391036]], dtype = "float64")#candidate|322|(3, 11)|const|float64
uop_323 = relay.rsqrt(const_322.astype('float64')) # shape=(3, 11)
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
var_359 = relay.var("var_359", dtype = "int32", shape = (105,))#candidate|359|(105,)|var|int32
call_358 = func_200_call(relay.reshape(var_359.astype('int32'), [1, 15, 7]), relay.reshape(var_359.astype('int32'), [1, 15, 7]), )
call_360 = func_200_call(relay.reshape(var_359.astype('int32'), [1, 15, 7]), relay.reshape(var_359.astype('int32'), [1, 15, 7]), )
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
call_376 = func_200_call(relay.reshape(call_358.astype('int32'), [1, 15, 7]), relay.reshape(call_358.astype('int32'), [1, 15, 7]), )
call_377 = func_200_call(relay.reshape(call_358.astype('int32'), [1, 15, 7]), relay.reshape(call_358.astype('int32'), [1, 15, 7]), )
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
call_399 = func_200_call(relay.reshape(var_359.astype('int32'), [1, 15, 7]), relay.reshape(call_376.astype('int32'), [1, 15, 7]), )
call_400 = func_200_call(relay.reshape(var_359.astype('int32'), [1, 15, 7]), relay.reshape(call_376.astype('int32'), [1, 15, 7]), )
output = relay.Tuple([uop_323,call_358,var_359,call_376,call_399,])
output2 = relay.Tuple([uop_323,call_360,var_359,call_377,call_400,])
func_411 = relay.Function([var_359,], output)
mod['func_411'] = func_411
mod = relay.transform.InferType()(mod)
var_412 = relay.var("var_412", dtype = "int32", shape = (105,))#candidate|412|(105,)|var|int32
output = func_411(var_412)
func_413 = relay.Function([var_412], output)
mutated_mod['func_413'] = func_413
mutated_mod = relay.transform.InferType()(mutated_mod)
var_532 = relay.var("var_532", dtype = "uint32", shape = ())#candidate|532|()|var|uint32
var_533 = relay.var("var_533", dtype = "uint32", shape = (11, 11, 14))#candidate|533|(11, 11, 14)|var|uint32
bop_534 = relay.less(var_532.astype('bool'), var_533.astype('bool')) # shape=(11, 11, 14)
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
var_583 = relay.var("var_583", dtype = "int32", shape = (105,))#candidate|583|(105,)|var|int32
call_582 = func_200_call(relay.reshape(var_583.astype('int32'), [1, 15, 7]), relay.reshape(var_583.astype('int32'), [1, 15, 7]), )
call_584 = func_200_call(relay.reshape(var_583.astype('int32'), [1, 15, 7]), relay.reshape(var_583.astype('int32'), [1, 15, 7]), )
output = relay.Tuple([bop_534,call_582,var_583,])
output2 = relay.Tuple([bop_534,call_584,var_583,])
func_597 = relay.Function([var_532,var_533,var_583,], output)
mod['func_597'] = func_597
mod = relay.transform.InferType()(mod)
mutated_mod['func_597'] = func_597
mutated_mod = relay.transform.InferType()(mutated_mod)
func_597_call = mutated_mod.get_global_var('func_597')
var_599 = relay.var("var_599", dtype = "uint32", shape = ())#candidate|599|()|var|uint32
var_600 = relay.var("var_600", dtype = "uint32", shape = (11, 11, 14))#candidate|600|(11, 11, 14)|var|uint32
var_601 = relay.var("var_601", dtype = "int32", shape = (105,))#candidate|601|(105,)|var|int32
call_598 = func_597_call(var_599,var_600,var_601,)
output = call_598
func_602 = relay.Function([var_599,var_600,var_601,], output)
mutated_mod['func_602'] = func_602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_684 = relay.var("var_684", dtype = "uint64", shape = ())#candidate|684|()|var|uint64
var_685 = relay.var("var_685", dtype = "uint64", shape = (8, 2, 10))#candidate|685|(8, 2, 10)|var|uint64
bop_686 = relay.greater_equal(var_684.astype('bool'), var_685.astype('bool')) # shape=(8, 2, 10)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
var_699 = relay.var("var_699", dtype = "int32", shape = (105,))#candidate|699|(105,)|var|int32
call_698 = relay.TupleGetItem(func_411_call(relay.reshape(var_699.astype('int32'), [105,])), 0)
call_700 = relay.TupleGetItem(func_413_call(relay.reshape(var_699.astype('int32'), [105,])), 0)
func_597_call = mod.get_global_var('func_597')
func_602_call = mutated_mod.get_global_var('func_602')
var_725 = relay.var("var_725", dtype = "uint32", shape = (1694,))#candidate|725|(1694,)|var|uint32
call_724 = relay.TupleGetItem(func_597_call(relay.reshape(var_684.astype('uint32'), []), relay.reshape(var_725.astype('uint32'), [11, 11, 14]), relay.reshape(var_699.astype('int32'), [105,]), ), 0)
call_726 = relay.TupleGetItem(func_602_call(relay.reshape(var_684.astype('uint32'), []), relay.reshape(var_725.astype('uint32'), [11, 11, 14]), relay.reshape(var_699.astype('int32'), [105,]), ), 0)
func_597_call = mod.get_global_var('func_597')
func_602_call = mutated_mod.get_global_var('func_602')
call_729 = relay.TupleGetItem(func_597_call(relay.reshape(var_684.astype('uint32'), []), relay.reshape(var_725.astype('uint32'), [11, 11, 14]), relay.reshape(var_699.astype('int32'), [105,]), ), 2)
call_730 = relay.TupleGetItem(func_602_call(relay.reshape(var_684.astype('uint32'), []), relay.reshape(var_725.astype('uint32'), [11, 11, 14]), relay.reshape(var_699.astype('int32'), [105,]), ), 2)
var_735 = relay.var("var_735", dtype = "uint64", shape = (6, 7, 7))#candidate|735|(6, 7, 7)|var|uint64
bop_736 = relay.subtract(var_684.astype('float32'), var_735.astype('float32')) # shape=(6, 7, 7)
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
call_744 = func_200_call(relay.reshape(var_699.astype('int32'), [1, 15, 7]), relay.reshape(var_699.astype('int32'), [1, 15, 7]), )
call_745 = func_200_call(relay.reshape(var_699.astype('int32'), [1, 15, 7]), relay.reshape(var_699.astype('int32'), [1, 15, 7]), )
const_750 = relay.const([[[True,False,False,True,False,False,True,False,True,True,True,False,True,False],[False,False,True,False,False,True,False,False,False,True,False,False,False,True],[False,False,True,True,True,True,True,True,True,False,False,True,True,True],[True,False,True,True,False,False,True,False,True,False,True,False,True,True],[False,False,False,False,False,True,False,True,False,True,True,False,True,True],[True,False,False,False,False,True,True,True,True,True,True,True,True,False],[True,False,True,True,False,True,True,True,False,True,False,True,False,True],[True,True,False,False,True,False,False,False,True,True,True,True,False,False],[False,True,True,True,False,False,False,False,False,True,True,False,True,False],[True,True,True,False,True,False,False,False,False,False,False,False,False,True],[True,False,False,True,False,True,False,False,True,False,False,True,True,False]],[[False,False,False,True,False,True,False,True,True,False,True,False,True,False],[False,True,True,True,True,True,False,True,False,False,True,False,False,False],[True,True,False,True,False,False,True,False,True,True,True,True,True,False],[True,False,False,True,True,False,False,True,True,False,False,False,False,False],[False,False,False,True,True,False,True,True,False,False,True,True,True,False],[False,False,True,True,True,True,False,False,True,False,True,True,False,False],[True,False,False,True,False,False,False,False,False,True,True,False,True,True],[True,False,True,False,True,False,True,False,False,False,False,True,False,False],[False,True,False,True,True,False,False,False,False,True,False,False,False,True],[False,False,False,True,False,False,True,True,False,True,True,False,True,False],[False,True,False,False,False,False,False,False,False,False,False,False,True,False]],[[False,False,True,False,False,False,True,False,False,True,False,False,False,True],[True,True,True,True,False,True,True,True,True,True,True,True,False,True],[True,True,True,True,True,False,True,True,False,True,False,False,False,False],[True,False,True,False,True,True,True,True,False,False,False,False,False,True],[True,False,False,True,True,True,False,True,False,False,False,False,True,False],[True,True,False,False,True,False,False,False,True,True,True,True,True,False],[True,True,True,True,True,False,False,True,True,False,False,True,False,False],[False,True,True,True,False,True,True,True,True,True,True,False,False,True],[False,True,True,True,True,False,False,False,False,False,True,False,True,True],[True,True,False,True,True,True,False,True,False,True,True,False,False,False],[False,False,True,False,False,False,False,True,True,False,True,True,True,True]],[[True,False,False,True,True,False,False,False,True,True,False,False,False,True],[False,True,True,False,True,True,True,True,True,True,False,False,True,False],[False,False,True,True,False,True,False,False,False,True,False,True,False,False],[True,False,True,True,True,True,False,True,False,True,False,True,False,True],[False,True,True,False,False,False,True,False,True,False,False,True,True,True],[True,True,True,False,True,True,False,True,False,False,False,False,True,False],[True,True,True,True,False,False,True,False,False,True,True,False,True,True],[True,False,False,False,True,False,True,False,True,True,True,True,True,True],[True,False,False,False,True,True,False,True,False,True,False,False,False,True],[False,True,False,False,True,True,False,False,True,True,True,False,False,False],[True,True,False,False,True,False,False,False,True,False,False,True,False,False]],[[False,False,True,False,False,True,False,True,False,True,False,True,False,True],[True,True,True,False,False,True,False,False,True,True,False,True,True,False],[False,True,False,False,False,True,True,False,True,True,True,True,False,True],[True,True,False,False,False,False,True,False,True,True,False,True,False,True],[False,False,True,False,True,False,True,True,True,False,True,False,True,True],[False,False,False,True,True,True,True,True,True,False,True,False,False,False],[True,False,True,True,False,False,False,False,False,True,True,False,True,True],[False,False,False,False,False,False,True,True,True,True,False,False,True,False],[True,True,False,False,False,True,False,False,True,False,False,False,True,False],[False,False,True,False,False,True,True,True,True,False,False,True,True,True],[True,True,True,False,False,True,True,False,False,True,True,True,True,True]],[[True,False,True,True,False,False,False,False,True,True,True,True,True,False],[False,True,True,True,False,False,False,False,True,True,True,True,False,False],[False,True,True,False,True,True,True,True,True,True,True,True,False,True],[False,False,True,False,True,False,True,True,False,True,True,True,False,False],[False,False,False,False,True,False,False,False,True,False,True,False,True,True],[True,False,False,True,False,True,True,True,True,True,False,True,False,True],[False,True,False,False,True,False,False,True,False,True,True,True,True,True],[False,False,False,True,False,False,True,False,True,False,True,False,True,True],[True,False,True,True,True,True,True,False,True,True,True,False,False,True],[True,True,False,True,False,False,True,False,False,False,True,True,False,False],[True,False,False,False,False,True,True,True,False,False,True,True,True,True]],[[True,False,False,True,True,False,False,True,False,True,False,False,True,True],[True,False,True,False,False,True,False,False,False,True,True,False,True,False],[False,False,True,True,False,True,False,False,True,True,True,True,False,True],[True,False,False,False,False,False,False,False,True,False,False,False,True,True],[False,False,True,False,True,True,False,True,False,False,True,False,True,True],[True,False,False,True,False,True,True,False,True,False,False,False,False,False],[False,False,True,True,False,False,True,True,True,True,True,False,False,False],[False,True,True,True,True,False,False,True,True,False,True,False,False,True],[False,False,True,True,False,False,False,True,True,True,False,False,True,True],[False,True,False,False,False,True,False,False,True,False,True,False,False,True],[False,False,False,True,True,False,False,True,False,False,False,True,True,True]],[[False,False,False,False,True,False,True,False,False,True,False,True,True,True],[False,False,False,False,False,True,True,True,True,True,True,True,True,True],[True,True,False,True,True,True,True,True,True,False,True,True,True,True],[True,True,False,True,True,True,True,True,False,True,True,True,False,False],[False,False,True,True,True,False,False,False,True,False,True,False,False,False],[False,False,True,True,True,False,False,False,True,True,True,True,False,False],[False,True,False,False,True,False,False,False,False,False,False,True,False,False],[True,True,False,True,True,False,False,False,False,False,False,True,False,True],[False,False,False,False,True,False,False,False,False,False,False,False,True,True],[True,True,True,True,False,True,False,True,True,True,True,True,True,True],[False,True,True,False,False,True,False,True,True,True,False,False,True,False]],[[False,False,True,False,False,False,True,False,False,True,False,True,False,True],[True,False,True,True,True,False,False,True,True,False,True,False,True,True],[False,True,True,True,True,True,True,True,True,False,False,True,True,False],[True,False,True,False,False,False,True,True,False,True,True,True,False,False],[False,True,True,False,False,False,True,False,True,False,True,True,False,True],[False,False,True,True,False,True,True,False,True,True,True,False,False,False],[True,False,False,True,False,True,False,False,False,True,False,True,False,False],[False,False,True,True,False,True,False,False,False,False,False,True,True,False],[True,True,False,True,False,True,False,False,False,False,False,False,False,True],[False,False,True,False,False,False,True,True,True,False,True,True,False,False],[True,True,False,False,False,False,True,False,True,False,False,False,False,True]],[[False,False,False,False,False,True,True,True,True,False,False,True,False,True],[False,False,True,True,True,True,False,False,False,True,False,True,True,True],[True,False,False,False,False,False,False,True,True,True,False,False,False,False],[True,False,True,False,True,True,True,False,False,True,False,False,True,True],[False,False,False,True,False,False,True,True,False,False,False,True,True,False],[True,True,False,True,False,True,True,True,False,False,True,True,False,False],[True,True,True,True,True,True,True,False,True,False,True,True,False,True],[False,False,True,True,True,True,False,True,False,True,False,True,False,False],[False,False,False,True,True,True,True,False,False,False,False,True,False,True],[False,True,False,False,True,True,True,False,False,False,False,True,True,False],[False,True,False,False,True,False,True,False,True,False,True,True,False,True]],[[False,True,True,False,False,True,False,True,True,False,True,True,False,True],[False,True,False,False,True,False,False,False,True,False,True,False,False,False],[False,True,True,False,False,False,True,False,False,True,True,True,True,False],[False,True,False,True,True,False,True,False,False,False,False,True,False,True],[False,False,True,False,True,True,False,True,True,True,True,True,True,False],[False,False,True,True,False,True,False,True,True,True,True,True,True,True],[True,True,True,True,False,False,True,True,True,True,True,True,True,False],[False,False,True,True,False,False,False,False,True,False,True,False,True,False],[True,True,False,False,False,True,True,False,True,False,False,True,False,True],[False,True,True,False,True,False,True,True,False,True,False,True,True,True],[True,True,False,True,False,False,True,False,True,True,True,False,True,True]]], dtype = "bool")#candidate|750|(11, 11, 14)|const|bool
bop_751 = relay.left_shift(call_724.astype('uint8'), relay.reshape(const_750.astype('uint8'), relay.shape_of(call_724))) # shape=(11, 11, 14)
bop_754 = relay.left_shift(call_726.astype('uint8'), relay.reshape(const_750.astype('uint8'), relay.shape_of(call_726))) # shape=(11, 11, 14)
bop_762 = relay.equal(const_750.astype('bool'), relay.reshape(call_724.astype('bool'), relay.shape_of(const_750))) # shape=(11, 11, 14)
bop_765 = relay.equal(const_750.astype('bool'), relay.reshape(call_726.astype('bool'), relay.shape_of(const_750))) # shape=(11, 11, 14)
output = relay.Tuple([bop_686,call_698,var_699,var_725,call_729,bop_736,call_744,bop_751,bop_762,])
output2 = relay.Tuple([bop_686,call_700,var_699,var_725,call_730,bop_736,call_745,bop_754,bop_765,])
func_767 = relay.Function([var_684,var_685,var_699,var_725,var_735,], output)
mod['func_767'] = func_767
mod = relay.transform.InferType()(mod)
mutated_mod['func_767'] = func_767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_767_call = mutated_mod.get_global_var('func_767')
var_769 = relay.var("var_769", dtype = "uint64", shape = ())#candidate|769|()|var|uint64
var_770 = relay.var("var_770", dtype = "uint64", shape = (8, 2, 10))#candidate|770|(8, 2, 10)|var|uint64
var_771 = relay.var("var_771", dtype = "int32", shape = (105,))#candidate|771|(105,)|var|int32
var_772 = relay.var("var_772", dtype = "uint32", shape = (1694,))#candidate|772|(1694,)|var|uint32
var_773 = relay.var("var_773", dtype = "uint64", shape = (6, 7, 7))#candidate|773|(6, 7, 7)|var|uint64
call_768 = func_767_call(var_769,var_770,var_771,var_772,var_773,)
output = call_768
func_774 = relay.Function([var_769,var_770,var_771,var_772,var_773,], output)
mutated_mod['func_774'] = func_774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_966 = relay.var("var_966", dtype = "uint64", shape = (15, 9, 10))#candidate|966|(15, 9, 10)|var|uint64
var_967 = relay.var("var_967", dtype = "uint64", shape = (15, 9, 10))#candidate|967|(15, 9, 10)|var|uint64
bop_968 = relay.bitwise_xor(var_966.astype('uint64'), relay.reshape(var_967.astype('uint64'), relay.shape_of(var_966))) # shape=(15, 9, 10)
bop_977 = relay.bitwise_or(var_966.astype('int32'), relay.reshape(var_967.astype('int32'), relay.shape_of(var_966))) # shape=(15, 9, 10)
output = relay.Tuple([bop_968,bop_977,])
output2 = relay.Tuple([bop_968,bop_977,])
func_1006 = relay.Function([var_966,var_967,], output)
mod['func_1006'] = func_1006
mod = relay.transform.InferType()(mod)
var_1007 = relay.var("var_1007", dtype = "uint64", shape = (15, 9, 10))#candidate|1007|(15, 9, 10)|var|uint64
var_1008 = relay.var("var_1008", dtype = "uint64", shape = (15, 9, 10))#candidate|1008|(15, 9, 10)|var|uint64
output = func_1006(var_1007,var_1008,)
func_1009 = relay.Function([var_1007,var_1008,], output)
mutated_mod['func_1009'] = func_1009
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1092 = relay.var("var_1092", dtype = "float32", shape = (16, 3, 7))#candidate|1092|(16, 3, 7)|var|float32
uop_1093 = relay.rsqrt(var_1092.astype('float32')) # shape=(16, 3, 7)
output = uop_1093
output2 = uop_1093
func_1104 = relay.Function([var_1092,], output)
mod['func_1104'] = func_1104
mod = relay.transform.InferType()(mod)
mutated_mod['func_1104'] = func_1104
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1105 = relay.var("var_1105", dtype = "float32", shape = (16, 3, 7))#candidate|1105|(16, 3, 7)|var|float32
func_1104_call = mutated_mod.get_global_var('func_1104')
call_1106 = func_1104_call(var_1105)
output = call_1106
func_1107 = relay.Function([var_1105], output)
mutated_mod['func_1107'] = func_1107
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1291 = relay.var("var_1291", dtype = "float32", shape = (9, 1, 7))#candidate|1291|(9, 1, 7)|var|float32
var_1292 = relay.var("var_1292", dtype = "float32", shape = (9, 5, 7))#candidate|1292|(9, 5, 7)|var|float32
bop_1293 = relay.not_equal(var_1291.astype('bool'), var_1292.astype('bool')) # shape=(9, 5, 7)
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
var_1312 = relay.var("var_1312", dtype = "int32", shape = (105, 1))#candidate|1312|(105, 1)|var|int32
call_1311 = func_200_call(relay.reshape(var_1312.astype('int32'), [1, 15, 7]), relay.reshape(var_1312.astype('int32'), [1, 15, 7]), )
call_1313 = func_200_call(relay.reshape(var_1312.astype('int32'), [1, 15, 7]), relay.reshape(var_1312.astype('int32'), [1, 15, 7]), )
func_597_call = mod.get_global_var('func_597')
func_602_call = mutated_mod.get_global_var('func_602')
var_1326 = relay.var("var_1326", dtype = "uint32", shape = ())#candidate|1326|()|var|uint32
const_1327 = relay.const([-8,-1,-5,-8,10,-10,7,6,3,6,-6,-5,-3,-2,-7,2,-10,-6,5,5,-5,6,9,1,5,-2,-6,-9,9,-3,-10,2,8,-4,-2,-8,4,-9,7,6,5,-5,6,1,3,4,9,-3,3,-7,6,4,-3,-6,-2,4,-10,-10,3,4,5,1,-3,8,4,3,-5,2,9,-10,-10,-10,-5,7,-2,-6,-8,-1,-5,-6,-6,-9,-7,1,-8,-7,-5,-9,7,-10,6,8,-5,4,1,7,1,10,-8,4,-10,-4,-9,-5,6,7,-1,5,-7,-6,-9,6,10,7,-5,-3,3,-1,-10,-9,2,-10,5,1,-4,-8,1,-2,10,-10,-10,1,10,-6,-8,9,-2,-5,4,-9,-4,-3,1,-9,-5,-5,1,10,7,4,-10,-5,3,9,7,-8,-5,9,6,-6,-6,8,6,-9,-2,8,5,4,5,-5,-1,7,-4,1,-4,-1,-7,-8,-6,8,9,10,1,-1,-9,-1,1,-6,4,-3,4,9,-4,8,3,8,2,-7,3,-1,6,3,-2,2,-6,-6,-2,4,3,4,8,7,1,2,2,6,-7,-7,8,5,-8,-6,8,-4,2,7,9,9,-10,6,4,1,-1,-10,-2,4,-6,8,-10,4,-10,1,7,-1,-1,-8,-9,6,-1,-2,1,-1,-8,-2,-1,10,7,1,1,10,9,7,-1,7,-1,-5,4,-1,4,1,-10,-7,4,1,-9,7,1,5,9,3,10,-2,5,9,9,-7,4,-7,1,4,-1,10,-7,3,7,-5,6,-5,5,10,-5,2,-10,-8,7,3,-4,-9,5,6,7,-9,1,4,8,-9,-1,-2,9,2,-1,1,5,6,-1,-10,-6,-1,-4,2,-9,7,-3,10,1,8,-4,-9,9,7,-8,10,9,-2,8,-7,6,-8,-6,-8,10,-1,5,3,5,-7,8,-8,1,-10,-3,-8,2,7,6,-5,1,1,5,-3,-4,5,8,-1,-1,-9,-9,-3,-5,-8,-6,-7,8,7,2,4,-2,9,2,10,2,-10,-8,-3,5,-4,-6,-2,-1,-10,10,-2,-4,-4,-1,-2,6,6,-4,5,-10,-2,3,3,-2,-8,8,7,-1,10,7,-6,3,5,1,-9,-10,-7,5,-7,-4,1,5,8,9,9,-10,-9,7,10,-5,-8,2,-9,9,5,-1,7,-4,-3,3,-1,8,-5,3,4,-4,2,-10,-2,7,2,4,5,4,-3,1,-1,-3,6,2,1,-2,4,3,1,-5,-7,4,-9,1,7,-5,3,-5,-3,10,-2,6,-6,-4,-7,2,8,-6,-4,6,-1,10,-10,-4,1,-6,8,-9,-10,-3,-9,-3,-1,-3,-7,8,1,-3,-2,-3,-5,-6,-10,-9,-7,1,1,5,4,9,-9,1,-3,-3,5,8,7,-3,8,-9,-8,2,-6,-1,5,4,-5,3,1,-6,4,-6,-9,-9,-5,-1,1,-2,10,-7,-1,8,6,-7,1,-7,7,-5,-4,-3,-3,2,8,10,5,-5,-8,6,8,5,5,4,5,8,6,-10,6,4,6,-3,3,9,5,-9,9,2,-6,-5,10,2,-3,-6,4,4,-5,-3,7,2,-9,4,-3,-1,-5,-1,10,-2,8,3,-7,4,-3,10,8,1,3,7,-2,-6,-5,-3,-2,1,10,-4,2,-10,-4,7,4,-1,-3,-4,7,1,1,-8,-8,5,-4,6,-6,10,-1,-1,-5,4,3,3,10,-1,-10,3,9,-8,6,6,2,-9,-5,8,5,9,9,-7,8,7,-8,-5,-8,-7,-7,-4,2,-2,6,-8,1,10,-1,-7,4,6,6,-8,-6,-7,-9,-2,6,8,3,4,5,-1,2,7,4,9,-7,-4,-1,6,2,1,-3,10,8,9,2,2,-2,2,-2,-7,8,-2,2,9,9,2,10,9,9,-1,-1,-5,-2,8,7,-3,-7,-4,-4,-3,-4,6,-8,-1,-4,-6,-7,-6,7,1,1,9,-8,7,7,-6,4,6,-8,8,1,-8,4,-7,10,-3,1,-9,4,-2,7,-3,-3,-2,5,-4,-4,7,6,7,2,-9,1,-4,5,7,6,-10,6,-10,3,-9,6,-5,2,10,-1,6,6,-8,-6,10,4,8,5,-2,4,5,9,-4,-1,4,-3,5,-10,10,-7,-7,2,10,-5,-6,-6,-1,-1,8,1,-6,-2,-6,4,-8,8,-2,1,10,8,5,6,-1,-4,1,-10,-2,5,-5,-7,2,8,-8,7,5,3,-9,9,-8,-8,-8,5,1,9,-1,-10,-4,6,-7,9,10,3,2,1,3,-10,-8,-1,9,8,8,2,6,3,2,-5,-5,4,-8,-9,4,2,-8,-2,6,-6,8,8,7,7,-3,-6,1,-6,-2,-10,6,-8,-6,1,2,8,-7,-6,-6,-8,5,9,-1,-7,-2,9,10,4,10,9,3,2,4,6,10,10,7,3,8,3,8,10,1,-5,-9,3,-4,4,4,7,-6,-1,-8,-3,4,-6,7,-10,2,-1,2,5,-2,1,2,10,-6,-3,7,1,-9,6,7,-8,3,-9,5,10,-4,-3,-10,-4,-4,-1,2,-4,2,-1,-6,-7,-6,2,10,-7,5,-1,-3,-1,4,9,7,9,3,-8,6,-6,10,6,-1,6,-4,-3,6,5,-8,-7,10,-6,-7,2,10,8,7,1,8,6,-6,9,2,1,-2,7,-6,7,-5,-7,-6,-6,10,4,7,-9,8,-3,4,2,-2,-10,-2,-10,-5,-4,1,-5,-7,8,-9,-7,7,-9,1,6,10,2,2,-9,-8,-7,4,1,-1,5,7,6,1,-4,-7,-6,8,-1,9,-7,-4,5,6,-9,-6,-6,-8,7,-8,-2,1,3,7,10,-5,-4,-1,9,6,2,-4,-4,-1,-4,10,-5,7,2,4,-1,-9,10,-3,-7,6,-10,8,-5,-5,-9,4,-7,1,-4,-3,4,9,4,-2,10,10,8,-3,6,-1,-2,8,7,-1,4,7,8,3,-7,-10,-5,-8,8,-6,-9,1,4,-3,9,-4,-9,-5,7,8,-5,3,-1,-2,2,5,-7,-3,6,-1,-1,1,4,-9,-4,-6,-7,8,2,5,8,-3,8,5,1,2,1,-4,-9,-9,-9,-1,-6,4,-9,-9,-1,-3,10,5,-5,5,-10,2,-3,-10,6,1,-2,-9,4,-9,2,-3,1,-4,-7,-10,-10,-4,-3,-7,10,2,-1,-5,1,-9,8,-5,-2,-3,2,5,8,-4,6,4,7,9,7,2,-8,10,5,-4,6,5,3,-9,1,-3,-5,4,3,2,7,-5,-9,2,-10,-2,-6,-4,8,9,7,6,-1,7,-4,-3,5,8,4,-9,-6,3,-7,-10,-2,-2,-3,2,9,-9,10,-5,-1,-10,-3,-1,7,3,-3,-7,-2,-6,7,2,-9,10,4,-4,-8,-9,-3,-2,-6,-4,-5,-6,4,-5,-3,-9,-7,-4,4,-5,-4,5,-7,-10,9,-4,7,-3,-5,1,3,-2,1,-1,-6,9,-1,7,-1,-10,1,5,7,10,-6,10,5,2,-10,2,9,5,-6,-7,9,7,3,-9,-10,2,4,-7,-6,2,2,-3,5,-1,10,8,-5,-9,-7,-1,-1,-2,5,-1,-10,8,-9,3,6,-5,-3,-6,-9,9,7,-2,-10,-1,-6,7,-7,6,-5,10,-6,-10,1,7,4,6,5,10,-2,2,5,-2,6,10,10,5,-8,-2,4,7,-5,-9,-10,-6,10,-10,9,1,1,-7,3,6,-8,8,-10,-9,-7,5,-5,-10,9,4,-2,-3,4,6,1,-9,-2,2,2,-5,8,-8,3,10,10,9,-8,-8,2,2,-6,6,-5,-10,-8,10,6,-10,8,10,5,1,-2,6,3,-1,6,-8,4,2,2,-9,-9,-7,1,6,-7,-7,-8,-4,10,1,-3,-9,-7,-8,-2,-9,-5,8,4,-10,-1,-1,-2,9,2,-8,-8,-1,-7,-4,-7,-7,-9,-8,9,5,7,-8,-5,-8,6,2,-2,-9,-4,-7,-5,-1,3,9,-9,3,-2,-4,-9,-4,10,-9,10,3,-10,-5,9,1,-7,-4,-7,-2,-8,-6,9,-4,-9,-3,-2,5,9,8,7,-7,-10,-3,-8,5,-3,4,4,-3,10,4,-2,-5,2,-8,1,-5,6,9,5,1,7,-10,-3,6,8,-7,-10,3,4,-10,9,-9,5,1,9,8,7,-9,-2,4,-4,2,3,-5,-9,3,10,4,-7,-7,-7,6,-2,6,7,-6,3,4,-3,3,4,1,10,-1,-10,-5,3,3,-6,1,-3,4,-5,1,9,-2,-4,9,6,-8,8,5,7,-7,9,6,-5,7,1,9,-4,3,4,1,-1,8,4,-1,3,4,9,3,10,-5,-2,3,5,-3,9,9,-2,-1,10,9,-3,-5,-3,-6,2,6,-4,-9,6,-6,-5,6,1,8,-1,-5,10,-7,-10,-7,-2,4,3], dtype = "uint32")#candidate|1327|(1694,)|const|uint32
call_1325 = relay.TupleGetItem(func_597_call(relay.reshape(var_1326.astype('uint32'), []), relay.reshape(const_1327.astype('uint32'), [11, 11, 14]), relay.reshape(var_1312.astype('int32'), [105,]), ), 1)
call_1328 = relay.TupleGetItem(func_602_call(relay.reshape(var_1326.astype('uint32'), []), relay.reshape(const_1327.astype('uint32'), [11, 11, 14]), relay.reshape(var_1312.astype('int32'), [105,]), ), 1)
func_1104_call = mod.get_global_var('func_1104')
func_1107_call = mutated_mod.get_global_var('func_1107')
var_1341 = relay.var("var_1341", dtype = "float32", shape = (336,))#candidate|1341|(336,)|var|float32
call_1340 = func_1104_call(relay.reshape(var_1341.astype('float32'), [16, 3, 7]))
call_1342 = func_1104_call(relay.reshape(var_1341.astype('float32'), [16, 3, 7]))
bop_1347 = relay.logical_and(bop_1293.astype('bool'), var_1291.astype('bool')) # shape=(9, 5, 7)
output = relay.Tuple([call_1311,var_1312,call_1325,var_1326,const_1327,call_1340,var_1341,bop_1347,])
output2 = relay.Tuple([call_1313,var_1312,call_1328,var_1326,const_1327,call_1342,var_1341,bop_1347,])
func_1354 = relay.Function([var_1291,var_1292,var_1312,var_1326,var_1341,], output)
mod['func_1354'] = func_1354
mod = relay.transform.InferType()(mod)
var_1355 = relay.var("var_1355", dtype = "float32", shape = (9, 1, 7))#candidate|1355|(9, 1, 7)|var|float32
var_1356 = relay.var("var_1356", dtype = "float32", shape = (9, 5, 7))#candidate|1356|(9, 5, 7)|var|float32
var_1357 = relay.var("var_1357", dtype = "int32", shape = (105, 1))#candidate|1357|(105, 1)|var|int32
var_1358 = relay.var("var_1358", dtype = "uint32", shape = ())#candidate|1358|()|var|uint32
var_1359 = relay.var("var_1359", dtype = "float32", shape = (336,))#candidate|1359|(336,)|var|float32
output = func_1354(var_1355,var_1356,var_1357,var_1358,var_1359,)
func_1360 = relay.Function([var_1355,var_1356,var_1357,var_1358,var_1359,], output)
mutated_mod['func_1360'] = func_1360
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1401 = relay.var("var_1401", dtype = "int16", shape = (1, 15, 9))#candidate|1401|(1, 15, 9)|var|int16
var_1402 = relay.var("var_1402", dtype = "int16", shape = (5, 15, 9))#candidate|1402|(5, 15, 9)|var|int16
bop_1403 = relay.not_equal(var_1401.astype('bool'), var_1402.astype('bool')) # shape=(5, 15, 9)
uop_1411 = relay.asinh(bop_1403.astype('float32')) # shape=(5, 15, 9)
func_1354_call = mod.get_global_var('func_1354')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_1418 = relay.const([-3.620803,-9.820640,-0.730264,6.403072,3.980556,1.968491,8.104728,8.294825,-9.679811,0.694822,9.065734,8.649617,-8.798175,9.804219,-6.367475,-5.291853,-5.213070,6.436771,9.178331,-2.609794,-3.767109,1.853436,0.832161,-6.020466,-6.224468,-1.171214,-5.605467,8.577809,3.565799,-7.558929,9.750078,-2.113638,9.989584,-6.862329,-0.846070,9.687602,-5.768371,-7.662641,-6.356476,9.153967,-8.682001,-2.736275,-1.054748,-4.204045,-7.179504,7.863237,3.468944,4.707762,4.562545,-5.109454,6.105425,-6.132011,-4.330231,4.311607,6.736410,-4.976209,-0.181216,-7.515687,-6.256518,-2.587013,4.046261,-6.464635,-3.443875], dtype = "float32")#candidate|1418|(63,)|const|float32
const_1419 = relay.const([[0.010172,3.082648,9.730791,-8.407305,-9.466330,-7.863311,9.060726,8.383158,2.153823,-9.963404,6.375970,-8.677987,2.920663,3.049863,1.652059,9.035535,-9.768525,-4.124733,9.967408,-3.625472,4.215995,-8.979713,1.222576,-0.816198,-9.714492,9.250138,-9.374122,4.510299,9.346658,3.814316,5.830900,9.716669,2.556179,7.994234,9.302101,-6.494617,7.350248,3.923087,-5.239848,8.192394,3.253134,-3.116059,-6.590609,5.174559,-9.467500,-9.390262,8.787674,9.348665,-0.945330,4.854050,-7.455791,-6.229538,-6.569559,-9.477995,-9.869615,4.626974,-5.186349,9.405960,5.110877,-9.799015,9.330466,-0.061052,0.477463,0.728878,-0.933995,1.368595,9.199823,-2.859311,0.227247,-8.979333,0.652400,2.808255,-1.180790,-2.801343,0.460781,5.599321,-0.884597,6.408183,-5.736317,8.040443,5.133465,4.463627,-6.948139,2.592618,1.323971,6.839156,4.094190,-4.745182,8.366119,-2.275819,-2.521132,1.175857,1.654611,-0.314843,-4.028878,-9.081098,-6.826440,-1.584419,-1.733042,-2.082510,4.170281,-6.990269,7.780782,-2.544815,8.975523,4.984083,4.604360,-1.371589,-7.524183,-0.097724,-6.278155,-9.792658,-8.759068,-7.788210,-4.371338,-5.637470,-7.317963,9.127234,-5.126134,0.826204,-5.614373,7.292214,1.408375,-9.161213,-3.151101,-3.689798,2.942481,1.650057,2.198303,-3.652682,-9.868026,-6.616599,1.463003,-8.447941,4.962060,-8.320570,4.390990,8.079478,1.604414,-4.648328,-8.703658,1.557295,0.677966,-1.282637,-1.998934,8.302250,6.982725,2.425791,4.343084,-8.021316,7.378834,-0.122250,-7.895575,-1.632820,6.860147,1.148416,4.803130,7.408803,3.161090,-3.674405,4.065207,2.678496,2.502930,8.485603,-5.754899,8.234858,-2.616638,-6.394241,-6.919242,9.920364,3.756510,6.327472,4.440918,-0.512900,-4.263789,-4.616966,-9.222832,5.403153,-3.978634,-5.929304,-0.247177,2.037670,6.673015,-5.837961,-5.516086,3.475852,-6.384823,-6.046864,9.930799,6.925327,7.473486,3.880447,0.134061,9.952933,-4.422214,-0.083954,-3.789079,6.438565,-5.233591,4.509891,9.278740,-4.079210,8.695654,7.910981,6.353804,9.806532,-2.078299,-9.100921,4.634451,-7.681215,4.213873,-2.666503,-7.789719,4.229468,9.817569,8.460691,6.834097,4.249384,-3.284097,-0.332440,3.231201,3.529275,-4.837489,2.843884,8.160554,7.562242,-9.739348,-3.904285,-5.959553,9.275484,-5.172048,-7.384331,1.160320,3.074017,1.701793,6.751304,4.396631,-7.294515,0.343130,7.146910,9.476094,2.995262,-5.873240,-1.880067,-5.544768,2.100346,-9.255639,-3.956070,1.677522,-7.385175,7.604475,7.833285,-9.551352,7.010943,3.750626,-7.193056,9.404164,-3.537073,-4.137163,-8.363554,3.605373,8.563256,-8.940840,6.518762,1.541350,-8.477133,4.884095,4.797178,2.849386,0.350847,1.607604,-9.163472,-9.435737,7.705049,8.455033,5.269199,0.487811,4.183183,-7.461733,3.862636,-9.940261,0.868951,6.402901,5.715274,9.208298,0.444592,-8.031507,7.833721,-7.284807,1.734112,6.962244,-2.896279,-2.239229,-2.312729,-7.654371,-7.169099,2.011636,5.914556,8.450382,3.303600,1.069683,2.838314,-6.945977,-1.307937,6.365252,8.554580,-8.351162,5.170323,5.856734,-2.459405,3.884673,-0.444552,-2.400613,0.930490,-2.243568]], dtype = "float32")#candidate|1419|(1, 315)|const|float32
var_1420 = relay.var("var_1420", dtype = "int32", shape = (105,))#candidate|1420|(105,)|var|int32
const_1421 = relay.const(4, dtype = "uint32")#candidate|1421|()|const|uint32
var_1422 = relay.var("var_1422", dtype = "float32", shape = (2, 168))#candidate|1422|(2, 168)|var|float32
call_1417 = relay.TupleGetItem(func_1354_call(relay.reshape(const_1418.astype('float32'), [9, 1, 7]), relay.reshape(const_1419.astype('float32'), [9, 5, 7]), relay.reshape(var_1420.astype('int32'), [105, 1]), relay.reshape(const_1421.astype('uint32'), []), relay.reshape(var_1422.astype('float32'), [336,]), ), 0)
call_1423 = relay.TupleGetItem(func_1360_call(relay.reshape(const_1418.astype('float32'), [9, 1, 7]), relay.reshape(const_1419.astype('float32'), [9, 5, 7]), relay.reshape(var_1420.astype('int32'), [105, 1]), relay.reshape(const_1421.astype('uint32'), []), relay.reshape(var_1422.astype('float32'), [336,]), ), 0)
uop_1425 = relay.acosh(var_1420.astype('float32')) # shape=(105,)
output = relay.Tuple([uop_1411,call_1417,const_1418,const_1419,const_1421,var_1422,uop_1425,])
output2 = relay.Tuple([uop_1411,call_1423,const_1418,const_1419,const_1421,var_1422,uop_1425,])
func_1430 = relay.Function([var_1401,var_1402,var_1420,var_1422,], output)
mod['func_1430'] = func_1430
mod = relay.transform.InferType()(mod)
var_1431 = relay.var("var_1431", dtype = "int16", shape = (1, 15, 9))#candidate|1431|(1, 15, 9)|var|int16
var_1432 = relay.var("var_1432", dtype = "int16", shape = (5, 15, 9))#candidate|1432|(5, 15, 9)|var|int16
var_1433 = relay.var("var_1433", dtype = "int32", shape = (105,))#candidate|1433|(105,)|var|int32
var_1434 = relay.var("var_1434", dtype = "float32", shape = (2, 168))#candidate|1434|(2, 168)|var|float32
output = func_1430(var_1431,var_1432,var_1433,var_1434,)
func_1435 = relay.Function([var_1431,var_1432,var_1433,var_1434,], output)
mutated_mod['func_1435'] = func_1435
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1620 = relay.var("var_1620", dtype = "float32", shape = (15, 11, 3))#candidate|1620|(15, 11, 3)|var|float32
uop_1621 = relay.erf(var_1620.astype('float32')) # shape=(15, 11, 3)
bop_1625 = relay.logical_and(uop_1621.astype('bool'), relay.reshape(var_1620.astype('bool'), relay.shape_of(uop_1621))) # shape=(15, 11, 3)
func_1430_call = mod.get_global_var('func_1430')
func_1435_call = mutated_mod.get_global_var('func_1435')
const_1632 = relay.const([-4,-6,-4,-7,3,-9,8,-3,2,9,-6,5,-8,4,-7,-3,4,9,-2,4,8,6,-1,-2,-10,4,-7,6,9,5,-7,-6,10,8,-6,7,8,-9,10,-1,-10,6,5,-3,4,-10,-10,3,-4,2,-5,-5,2,-1,5,5,-6,5,5,-6,9,1,2,9,-6,7,2,4,8,-6,-7,10,-4,-7,-6,9,8,-7,5,-8,1,-2,-9,-6,-4,-10,5,-8,-9,-7,5,2,-5,4,7,1,-1,-10,1,-9,-10,10,1,4,3,4,-7,-3,-7,2,-1,3,-8,-4,1,-4,2,-10,-1,2,-8,-4,-7,9,6,-8,-6,10,-6,-3,-6,1,2,-1,-6], dtype = "int16")#candidate|1632|(135,)|const|int16
const_1633 = relay.const([-3,8,1,-4,1,-3,4,3,8,8,4,1,9,-10,-9,8,5,-4,7,5,-1,-7,2,5,-7,-3,4,-6,10,-9,-9,2,5,2,3,10,-6,9,8,-7,8,-3,-5,-5,-8,-3,3,1,-1,-10,10,8,-8,3,10,-10,-1,-3,3,-1,-4,8,-10,-5,-1,5,6,7,-8,-9,-10,1,3,6,-1,7,-1,-3,5,2,-5,-7,-8,-5,5,-9,5,4,1,4,-9,9,7,1,-2,-7,-9,7,1,8,-8,-8,-4,-10,6,-10,6,-5,1,-6,10,-7,-2,-8,6,6,2,8,-10,-4,-2,-9,2,-5,3,-6,-7,-4,9,9,-8,3,10,-6,8,7,2,2,2,-9,-9,8,1,-2,-3,-8,-7,-9,-2,9,6,-2,2,6,-1,8,1,-5,-5,-5,-7,9,3,3,6,-5,-6,3,-5,1,-4,-8,-3,9,10,-8,8,1,7,9,5,-6,-5,8,-7,-5,-8,-8,-4,10,-3,-10,-8,-4,-6,10,9,4,-4,1,1,-2,9,-1,9,6,4,2,-9,-8,-1,8,-2,-1,5,6,8,-7,8,-9,-1,-8,2,-6,-8,8,1,-9,-8,-1,-4,9,7,-8,-5,-1,-1,9,10,-6,10,-10,-10,5,-3,1,3,9,7,4,-4,6,3,1,-3,-2,1,-3,2,8,-4,3,10,-7,9,1,-6,1,4,-1,-8,-1,6,1,4,5,10,-5,-10,-9,4,4,-7,-9,8,-10,-4,7,-5,-10,-8,8,3,-10,6,1,1,1,-10,-3,-10,-5,3,6,8,10,-1,8,2,6,-9,-9,2,-2,-10,-9,7,-7,-3,2,-1,1,-9,-7,-7,8,-9,8,-8,-2,-5,-1,4,-5,-2,-2,7,6,-2,-6,3,-7,-2,-4,5,-9,6,5,1,-8,-4,8,4,9,7,5,9,4,6,2,-3,-6,-2,-10,-8,7,-9,-5,-1,10,-8,-7,8,-8,9,-10,2,1,4,8,2,-5,-4,-5,-3,-2,4,9,1,8,9,2,1,-7,7,-6,3,-9,2,-2,10,5,3,8,5,-6,2,-8,-3,10,2,-8,-7,-2,10,-3,9,-6,4,-10,10,3,-6,-6,6,9,-10,-3,-4,6,-2,-6,-7,-3,6,1,-9,-9,5,-4,-9,-1,9,-10,10,7,-4,-10,7,5,-9,1,-3,5,-6,-1,1,6,5,-3,1,-4,4,10,-9,5,1,8,-6,2,-1,7,-4,-1,10,-3,-5,7,-2,1,2,-1,-5,9,-3,5,5,-5,-6,9,2,6,10,9,10,5,-9,7,9,-7,-10,-6,4,-5,10,4,-7,-1,2,10,3,6,-4,-6,-10,5,5,4,-3,-8,2,-4,2,7,-7,-6,2,2,4,7,1,3,-3,3,-5,-6,-3,-7,6,-9,-10,-1,8,8,-1,7,7,10,-4,-6,6,-5,2,5,7,-1,2,9,5,-3,2,-10,9,-9,-5,-3,6,-1,1,8,-2,5,1,6,-3,4,-7,6,-6,-1,1,3,2,-8,2,1,3,9,-3,-9,4,-2,8,6,-5,7,1,-3,-4,5,7,3,5,-3,7,-5,-7,-1,-6,-1,6,-7,7,-9,1,8,-2,-7,3,7,1,-10,-10,-3,9,-9,1,-1,6,-9,6,4,-8,-8,10,-2,7,1,-2,6,-10,6,1,-10,-9,-5,-8,-6,-9,-9,10,-1,-3,6,7,-7,-7,8,2,4,-7,-10,-7,3,-1,-6,-4,-9,1,2,-7,7,-2,1,-3], dtype = "int16")#candidate|1633|(675,)|const|int16
const_1634 = relay.const([3,6,4,-5,-2,7,10,-10,-1,-9,1,-2,10,-9,6,2,-3,-1,-8,3,9,-3,-8,-10,-9,-9,4,5,3,-7,-2,-10,9,-2,-8,-8,-7,-8,8,-3,-6,7,-4,-5,6,7,3,3,-9,-3,-1,5,-2,10,10,4,8,7,-4,6,-4,-10,-10,-1,1,7,-2,8,7,3,5,-5,-1,-2,5,-6,3,-8,-10,-4,-2,3,-5,-2,-10,2,-4,-6,-7,9,10,-1,-3,6,9,-4,-2,6,7,2,3,-3,-10,2,-9], dtype = "int32")#candidate|1634|(105,)|const|int32
const_1635 = relay.const([-5.321596,8.357622,-7.530278,1.218394,-6.926100,6.525688,3.055367,-5.869745,8.553216,-0.945207,3.572628,4.494957,-1.913714,7.936169,6.296273,-7.554263,4.403395,-3.651111,-1.102699,8.466934,-8.674648,-5.553090,4.896831,6.104036,-4.716569,-6.519224,3.117020,-9.589011,5.968430,-8.248301,-3.556506,8.001318,-6.421977,-2.341638,2.048146,-4.457942,-2.187444,1.494455,5.788384,4.825779,-4.248860,-1.435775,0.962885,8.152030,-0.096191,0.256300,0.058457,-8.660570,-2.632551,-7.106775,7.339291,0.704373,-6.301767,3.352926,1.253470,0.405649,-7.853568,-9.957872,-3.234642,-4.347915,5.681454,-5.295711,-7.172321,-0.532735,9.390531,-9.247821,7.079569,-2.580793,-3.764154,-7.248671,-2.952989,-5.715630,0.449095,-7.910091,-5.955968,-9.781206,-2.042212,-4.833536,2.499263,6.973709,-7.263059,7.452514,1.371019,2.350052,7.017236,-3.592305,4.445476,-7.075040,6.569890,-8.408368,-4.699254,6.258917,9.491502,1.945827,-8.561746,1.785311,3.071398,4.921372,5.083629,-2.633810,-9.353759,-2.295376,7.120730,-6.216968,-8.730028,5.877217,6.864465,2.533953,-4.556780,2.781616,-3.677430,7.471466,-7.482716,-7.105019,4.123738,-6.165211,9.735013,1.782549,-0.085750,7.598522,1.435178,9.705313,9.678325,0.932891,8.669680,4.853926,-3.250069,9.708741,7.701612,-7.047005,9.073987,-4.206959,2.678174,7.744659,2.686647,-9.854111,9.247037,0.678679,7.701202,0.107396,7.538639,-4.651324,2.176320,-6.670940,3.438996,-0.793353,-9.308212,-5.496180,-4.506392,6.810800,-1.806982,-2.620624,4.160071,1.011604,6.425967,0.675144,3.406673,-5.803807,-5.987539,0.339366,1.529325,-2.791482,-3.577913,0.806079,-2.359595,-9.499778,8.399680,2.816265,-7.145460,6.198197,8.987286,-3.812970,-3.927881,6.499731,-2.970954,-9.523395,-9.595054,3.932077,5.915484,-6.919015,5.617079,0.795651,9.398418,6.556043,3.088778,5.979670,8.894657,1.772176,-0.588949,-9.170502,3.507003,-9.697719,4.383963,-6.679602,6.162730,3.194960,6.750956,6.175621,0.928083,-4.762067,0.276038,1.856251,5.211271,-6.081798,1.353096,-0.310663,5.188727,5.372743,-4.302345,-4.021575,-0.913291,-8.939938,-6.457085,-8.322214,-1.376407,-4.784861,7.824938,9.880357,-3.205467,-4.816843,-9.247296,-7.503742,-9.052568,9.948738,2.731641,-8.060898,6.726639,3.597678,-7.795876,3.241697,-1.026802,-3.537590,6.997160,-8.809485,1.507869,2.445179,-2.460706,0.907484,5.944978,5.124457,-4.531616,-3.778225,8.401950,9.918594,-4.559244,-3.414311,-9.106800,-4.251460,-8.688888,6.024031,2.264598,-5.625962,-7.803525,-3.641763,-9.845322,-3.551733,5.285164,-4.272213,-1.631323,-2.694674,-0.400956,0.379929,4.923466,-8.364843,7.678391,6.579787,-2.232286,-5.537142,-6.165774,8.513583,-3.366685,0.843178,-5.557448,-9.989528,-7.716758,5.577530,-1.009749,1.096995,-7.746308,6.989695,-5.065441,4.655173,-4.365156,5.537654,-3.084923,1.906425,1.078520,3.765192,-1.480370,-4.325902,-7.340068,3.329299,6.148887,8.890984,-5.294199,6.957373,5.024350,-4.293810,-1.471425,-8.875182,-0.896709,6.470515,6.600225,3.086082,8.444905,-5.543873,-6.843376,-1.415991,-7.225163,7.972074,-6.039489,0.263311,1.688475,-1.750474,-5.066205,7.146888,-1.680971,-9.307272,9.268736,-4.997285,4.306338,-2.606758,-5.784355,0.825837,-0.351739,-1.597995,6.927519,1.171415,6.638120,-5.276100,-8.805882,-6.494119,9.569482,-8.172800,-7.836030,5.750384], dtype = "float32")#candidate|1635|(336,)|const|float32
call_1631 = relay.TupleGetItem(func_1430_call(relay.reshape(const_1632.astype('int16'), [1, 15, 9]), relay.reshape(const_1633.astype('int16'), [5, 15, 9]), relay.reshape(const_1634.astype('int32'), [105,]), relay.reshape(const_1635.astype('float32'), [2, 168]), ), 3)
call_1636 = relay.TupleGetItem(func_1435_call(relay.reshape(const_1632.astype('int16'), [1, 15, 9]), relay.reshape(const_1633.astype('int16'), [5, 15, 9]), relay.reshape(const_1634.astype('int32'), [105,]), relay.reshape(const_1635.astype('float32'), [2, 168]), ), 3)
output = relay.Tuple([bop_1625,call_1631,const_1632,const_1633,const_1634,const_1635,])
output2 = relay.Tuple([bop_1625,call_1636,const_1632,const_1633,const_1634,const_1635,])
func_1640 = relay.Function([var_1620,], output)
mod['func_1640'] = func_1640
mod = relay.transform.InferType()(mod)
mutated_mod['func_1640'] = func_1640
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1641 = relay.var("var_1641", dtype = "float32", shape = (15, 11, 3))#candidate|1641|(15, 11, 3)|var|float32
func_1640_call = mutated_mod.get_global_var('func_1640')
call_1642 = func_1640_call(var_1641)
output = call_1642
func_1643 = relay.Function([var_1641], output)
mutated_mod['func_1643'] = func_1643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1862 = relay.var("var_1862", dtype = "bool", shape = ())#candidate|1862|()|var|bool
var_1863 = relay.var("var_1863", dtype = "bool", shape = (1, 4, 11))#candidate|1863|(1, 4, 11)|var|bool
bop_1864 = relay.logical_and(var_1862.astype('bool'), var_1863.astype('bool')) # shape=(1, 4, 11)
func_1006_call = mod.get_global_var('func_1006')
func_1009_call = mutated_mod.get_global_var('func_1009')
const_1869 = relay.const([-1,-9,-4,-10,-2,-10,-1,-7,10,-8,5,7,-7,-3,10,-9,2,3,4,2,-2,1,7,-2,5,1,3,3,6,7,8,6,5,-6,5,-7,2,-10,-7,7,2,1,7,-5,2,8,-9,1,-4,-5,7,-5,9,8,-8,5,5,5,-1,-3,-4,2,5,-9,2,-9,-3,6,10,7,8,-9,-9,-3,7,-3,8,6,1,-4,7,-10,8,4,9,-9,3,-10,-4,-5,10,2,7,3,3,-1,-3,-1,-8,-2,-6,5,-8,-4,-7,-3,-8,5,5,3,7,8,-6,10,6,2,2,-3,-2,1,7,6,-1,3,1,1,10,8,8,2,2,6,-1,2,-8,-3,-9,2,-2,-5,1,-4,5,8,2,9,-4,-5,6,8,-2,-6,-2,2,-3,8,3,6,-4,5,-4,9,9,-5,-3,8,-4,8,-5,9,-9,4,10,4,-4,-9,1,-8,-4,-7,6,2,-10,-3,5,2,10,8,6,4,-8,10,-3,-4,-1,-3,8,4,-10,-2,-2,8,4,2,7,2,10,-9,-10,3,-5,8,-4,1,3,6,2,7,-2,-6,6,-6,-7,3,-7,-1,-3,-8,-3,-10,4,4,-1,-10,2,4,3,8,5,9,10,-6,1,1,-3,-4,8,-3,-1,-4,10,-2,-7,4,4,6,5,6,-6,-4,9,-7,8,-9,-4,1,-2,6,-5,-1,-6,-10,9,-1,-6,-5,4,3,-2,10,-5,10,6,-7,8,8,5,7,8,10,-2,7,8,10,2,8,1,-7,7,5,-3,1,5,-3,-5,-4,-9,7,-3,-1,-4,-6,-8,1,-10,1,3,3,-2,-8,-1,-8,-5,2,-9,-7,-2,10,-8,5,9,-1,-10,10,-3,10,1,8,10,-8,-3,-4,7,-2,4,1,3,-8,8,-6,-4,-9,-2,-5,-7,3,-5,4,10,-7,3,-10,1,1,3,2,-4,6,-10,-10,3,6,2,-10,-7,-9,-4,-7,6,-6,-7,-8,-9,-7,-5,-5,-2,-6,2,9,4,10,-6,3,-8,2,-7,-6,-5,7,-2,10,-5,10,-4,-9,-6,6,-7,-5,10,-8,-8,-5,-9,-4,-7,7,-9,-1,8,1,10,-8,-6,10,8,3,6,8,-2,-4,-5,3,8,8,6,1,-7,-1,-10,9,2,-4,1,2,4,-4,-9,-4,-3,-4,-4,-2,-2,3,7,9,-3,-8,5,-2,7,8,5,4,6,6,3,-8,3,8,-3,-7,-2,-5,-6,7,-4,-9,9,-6,1,3,-10,-10,2,2,7,-4,-6,-9,5,-4,-1,8,8,2,-8,5,8,10,5,7,-1,2,-9,8,7,5,-6,-7,-8,6,-6,3,-6,7,-5,5,7,-5,-8,-2,-8,-4,-1,1,-10,5,-5,3,3,5,6,6,-7,10,6,2,-1,8,-7,-1,-5,-6,-5,2,-9,-8,6,8,6,1,-4,-6,1,-6,5,7,6,-10,2,-8,8,-8,1,10,-4,1,-7,-2,3,7,9,-9,9,5,1,4,1,-6,8,10,-8,-1,-8,-3,4,2,-8,-6,8,8,-7,1,-4,10,4,5,3,-8,10,-3,-3,-8,3,8,7,3,8,-10,2,6,2,-9,-1,5,10,8,2,-6,1,-10,-10,2,6,2,-4,3,4,-10,-1,-6,4,8,-1,-4,-8,3,-7,10,1,-1,-2,2,8,-1,-6,4,3,7,-6,-8,-3,-6,10,-4,-8,5,-1,8,-8,10,9,5,6,8,2,8,-9,-8,8,9,8,8,10,9,-6,-3,5,-7,-1,-4,-2,-10,7,-1,9,3,-3,-7,6,2,-6,-6,-4,-3,7,10,2,-10,6,-5,9,-4,-10,9,6,-9,8,-7,-8,9,-10,3,-7,-2,-4,9,7,-8,-4,-7,8,-7,3,9,4,7,7,5,-2,-8,-4,-10,2,-9,4,-1,4,-9,9,8,-7,5,-4,-7,-7,-5,-4,3,-4,6,-10,2,-2,9,-10,3,4,3,-2,6,-7,-10,9,-1,-6,3,-2,10,-8,5,7,-7,-10,9,-1,9,10,-1,5,-10,-6,8,9,-2,-6,5,7,-6,-2,-6,2,1,9,8,1,-6,2,7,-2,8,-7,3,7,-10,-6,2,-4,-9,4,-6,9,3,5,-5,-8,5,8,-9,9,3,-6,3,-7,-2,10,-5,-9,10,-10,-9,10,4,-3,-10,-2,8,-8,-9,-1,-4,-10,-2,9,1,9,-8,5,6,6,-10,8,10,7,1,-2,-3,-5,-9,8,-6,9,7,-7,-2,10,-5,8,-4,-5,-4,-1,-7,-1,3,-8,10,4,-1,-2,-7,-5,-9,-8,-7,-10,-7,-8,-9,3,-10,-2,8,8,8,4,-10,-8,1,6,8,-1,-8,3,7,9,7,-6,7,8,-3,3,-1,-6,8,4,-7,2,3,-3,1,8,1,-7,-9,6,-7,-7,9,-3,-3,-4,2,-8,-1,-5,-2,4,-8,-4,4,-9,8,-9,9,-5,-1,-5,-6,9,-7,-2,9,4,7,-4,-9,-1,-9,3,4,-10,-8,-9,-9,2,5,7,-1,1,1,8,8,-7,2,5,-2,3,2,-2,10,-9,7,-9,8,-6,-7,9,6,6,-9,-5,8,9,-2,4,-5,7,10,-2,-9,-7,5,-6,3,-10,-3,-3,3,-4,3,6,-3,-3,2,1,-4,-8,6,1,-5,2,-5,10,7,2,-2,-1,5,9,-9,-7,-1,-5,10,-6,4,5,-5,7,9,-5,2,-7,1,-2,-6,-5,-7,-4,6,-4,-2,-10,-1,10,-8,2,-2,-7,-7,-3,-10,-2,9,-6,7,-5,-6,-5,-2,1,-1,-2,-4,-4,-7,-3,-5,6,10,1,1,-8,1,-5,10,4,9,-2,4,1,5,10,9,-6,-9,8,-4,-8,10,1,9,1,3,10,-1,1,-5,8,9,2,-2,2,7,-3,3,-6,1,-10,-1,2,-3,8,3,1,1,-4,6,-8,-5,-7,-7,1,-10,-10,1,-3,-4,2,8,-1,-9,-9,-10,7,2,-2,-6,-6,-3,-7,10,-9,-10,2,-6,-4,-8,1,2,3,-1,2,9,-4,-4,-7,9,-9,-8,-5,-3,-1,-4,9,8,1,-9,5,-2,-10,-9,3,4,-7,2,-9,2,6,-10,-5,10,-6,-10,-7,-1,1,6,10,-5,-4,-10,1,-1,-10,-5,9,-1,-4,-7,3,10,10,7,7,6,8,4,-7,-10,8,-2,-1,-2,-5,-8,9,-2,3,8,1,3,9,3,-4,3,-10,-1,-9,8,3,2,-3,2,4,-7,-5,8,-10,10,-6,10,-1,7,-3,3,10,-8,2,10,-10,-2,-1,-9,-3,-7,-1,5,7,1,8,3,-1,-2,1,-8,-2,5,3,4,-10,-5,9,4,-3,-3,-3,10,7,7,-7,-10,9,10,-9,8,-7,-4,-2,-2,5,7,-2,-4,-10,-1,-7,-3,6,8,2,-5,-8,5,7,-6,-3,-2,1,-7,6,7,-9,-2,6,8,-6,6,2,-6,1,3,7,2,-1,9,7,3,-6,10,-4,9,3,-4,9,6], dtype = "uint64")#candidate|1869|(1350,)|const|uint64
call_1868 = relay.TupleGetItem(func_1006_call(relay.reshape(const_1869.astype('uint64'), [15, 9, 10]), relay.reshape(const_1869.astype('uint64'), [15, 9, 10]), ), 0)
call_1870 = relay.TupleGetItem(func_1009_call(relay.reshape(const_1869.astype('uint64'), [15, 9, 10]), relay.reshape(const_1869.astype('uint64'), [15, 9, 10]), ), 0)
output = relay.Tuple([bop_1864,call_1868,const_1869,])
output2 = relay.Tuple([bop_1864,call_1870,const_1869,])
func_1874 = relay.Function([var_1862,var_1863,], output)
mod['func_1874'] = func_1874
mod = relay.transform.InferType()(mod)
var_1875 = relay.var("var_1875", dtype = "bool", shape = ())#candidate|1875|()|var|bool
var_1876 = relay.var("var_1876", dtype = "bool", shape = (1, 4, 11))#candidate|1876|(1, 4, 11)|var|bool
output = func_1874(var_1875,var_1876,)
func_1877 = relay.Function([var_1875,var_1876,], output)
mutated_mod['func_1877'] = func_1877
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2601 = relay.const([[[-9,-8,3,-8,-8],[-7,-1,-6,8,6],[5,10,8,1,7],[10,1,1,-3,-2],[8,-9,-10,7,-2],[2,3,-5,1,4],[6,-7,3,-8,7],[-9,-1,-7,3,7],[-7,3,2,-2,4],[4,-2,-4,7,1],[-3,-2,-1,3,10]],[[-1,2,10,2,8],[8,5,-3,4,2],[-5,-8,-1,-3,-4],[8,-4,7,-4,-6],[4,-6,-3,-7,-8],[-4,6,-1,10,-5],[1,-10,-4,8,8],[4,-7,1,7,9],[-9,-2,5,-3,-9],[1,-2,4,-10,7],[6,1,10,-3,2]],[[-6,-3,5,4,-2],[8,3,-6,9,-9],[5,-8,7,8,6],[-2,-8,-3,-2,5],[-7,9,5,7,3],[-10,9,3,-5,8],[1,-6,-4,6,-5],[3,-3,2,-10,-4],[4,1,4,-1,-7],[2,8,8,6,-9],[-6,3,-7,-9,-5]],[[-9,-1,-10,4,-5],[10,-8,-7,10,2],[-6,-2,-8,-5,5],[4,-7,-4,-9,10],[-1,1,-7,-8,2],[6,8,7,6,-5],[-10,-7,-1,5,1],[-3,-4,-2,5,-7],[9,6,-1,5,5],[-10,-8,-3,10,-10],[1,-3,-10,-5,-4]],[[1,-8,-1,10,-8],[-6,1,5,-5,-9],[-6,-8,5,-6,4],[-7,-3,2,3,2],[8,-10,-1,10,-10],[1,-1,-4,9,-9],[2,-8,10,-1,-5],[-4,2,-1,-9,-1],[3,-4,10,-1,8],[2,7,-4,-3,9],[9,-10,-9,6,-3]],[[4,6,10,-6,7],[-4,-5,-2,-7,-8],[-10,2,-10,2,-7],[-10,2,-1,-5,7],[4,-2,10,9,-6],[6,4,9,-8,-9],[-9,8,-6,-6,-7],[-3,-4,-9,9,-4],[5,-5,7,-2,-7],[8,9,-7,-6,-5],[8,3,5,6,7]]], dtype = "uint8")#candidate|2601|(6, 11, 5)|const|uint8
var_2602 = relay.var("var_2602", dtype = "uint8", shape = (6, 11, 5))#candidate|2602|(6, 11, 5)|var|uint8
bop_2603 = relay.bitwise_and(const_2601.astype('uint8'), relay.reshape(var_2602.astype('uint8'), relay.shape_of(const_2601))) # shape=(6, 11, 5)
func_1104_call = mod.get_global_var('func_1104')
func_1107_call = mutated_mod.get_global_var('func_1107')
var_2612 = relay.var("var_2612", dtype = "float32", shape = (336,))#candidate|2612|(336,)|var|float32
call_2611 = func_1104_call(relay.reshape(var_2612.astype('float32'), [16, 3, 7]))
call_2613 = func_1104_call(relay.reshape(var_2612.astype('float32'), [16, 3, 7]))
func_1640_call = mod.get_global_var('func_1640')
func_1643_call = mutated_mod.get_global_var('func_1643')
const_2615 = relay.const([8.192779,-7.794570,-3.488737,6.801445,0.654819,-4.955224,8.509003,-0.360056,6.177399,-9.649386,-2.870585,-0.447495,6.037866,-5.930299,-9.422609,7.362567,8.286015,5.270750,2.896866,2.117521,-7.668508,1.184115,-2.551161,6.554948,-1.222573,-7.823519,-3.536431,-5.265427,8.004430,-6.491785,7.660621,6.197576,-9.161202,-3.482491,-2.803441,-0.857290,8.117196,-9.307310,2.090606,8.278427,4.276059,-4.687976,-0.854653,3.988275,-1.614495,5.097888,-1.095109,-1.260336,6.637494,-2.587496,-4.660311,-1.502110,-0.786372,-1.283986,-8.517899,1.695847,2.624127,9.910018,4.122749,4.889152,3.229859,8.754831,9.161346,-2.412951,-6.980236,-2.023742,0.049196,-0.041345,-9.172340,0.682622,-9.993490,-2.282032,3.950291,7.536891,7.348497,-2.634282,8.967331,-9.049569,4.728258,0.201441,2.907708,9.406157,-3.298689,-0.544470,-0.874819,5.880354,-8.147467,-4.864563,6.807771,-3.075554,-9.500008,9.138339,-5.836887,-0.222409,-4.328533,0.248006,-2.559082,-6.536106,-9.194628,0.874956,6.956183,0.432481,-3.419045,4.652580,9.193246,-1.863588,-2.198567,2.885392,8.570978,-2.129467,4.965693,9.539137,-4.347836,-7.472746,-1.545399,1.544739,-3.179832,-8.415220,-8.885845,5.787465,5.087561,1.497203,9.562051,8.587304,3.851001,3.875237,4.493437,-3.094490,-6.023599,0.590573,-0.100545,-8.099792,4.102962,6.859479,-8.992352,-7.988887,1.677799,4.214227,-8.236105,3.034324,9.950852,2.419886,-2.897242,-7.109516,-0.746510,9.549996,2.290366,-6.324040,-5.245476,-8.889223,-2.896611,9.536737,6.155110,-1.483704,8.946110,3.239438,-0.176122,6.644886,-0.073161,-5.358777,5.523721,5.356921,2.907641,-8.061005,7.028549,7.419926,1.594752,4.005418,0.314547,-6.677644,-4.343572,2.070256,-4.853440,2.023483,2.286996,-7.092714,8.424285,5.623137,8.565460,9.058321,-9.462086,-9.166287,5.768725,-1.961423,4.289983,8.125717,-2.735216,9.945791,9.293403,8.581063,-9.364698,-6.547737,4.388005,-9.171121,3.745569,-3.138420,-4.960263,0.155999,-4.677465,1.837381,-5.336068,0.840911,8.569605,-2.431376,6.831155,7.153865,4.396388,-8.476767,6.053781,2.827686,-8.064429,5.209444,-7.491406,-5.799272,-3.262798,-7.632102,-4.342541,-0.328790,-3.975601,-4.244756,-4.012630,9.707219,8.279439,0.243751,1.557223,7.126205,-1.227762,-2.176249,2.352053,6.776410,-3.502479,4.653923,-8.983165,3.060619,-2.577177,-7.418310,1.151423,-6.081692,7.611269,-5.590195,-1.036076,-1.895923,-9.029481,1.256056,0.247952,3.282734,-6.298078,-0.072376,-2.894098,-8.169351,-1.397578,-4.491862,-4.608447,-4.290410,-8.060828,-3.224767,7.698783,1.875648,-7.710616,9.697448,2.178326,0.001147,5.705247,-5.700693,8.244933,-2.599625,-8.757219,-2.835496,3.300620,-5.474305,9.134353,-7.672410,-1.217064,-4.627067,-0.080225,-9.988869,-7.624233,-3.449592,-2.750013,-9.737123,4.492807,9.730017,0.034963,-5.650421,-7.954153,-2.586407,-0.774229,-5.041601,-9.651465,8.339433,1.631235,-1.264282,4.975998,8.226362,-5.628994,-1.102710,5.130676,3.242530,6.823935,6.776183,-5.586683,6.614603,8.769480,5.597961,-7.573612,-9.883432,7.050797,9.417245,3.634663,-2.990318,-6.047118,1.737466,-8.149958,-0.374230,3.702557,8.664786,4.944855,-5.795145,5.578368,-5.727795,-4.765354,4.141014,-4.066651,-7.352888,6.881942,7.367162,5.923762,0.796465,6.206651,2.749116,-7.667830,-4.096355,4.958593,-2.976467,7.283751,-5.236668,4.352182,4.081347,8.152747,-3.699492,-6.569376,-1.153742,-4.556996,0.749368,-8.303546,-5.390187,2.077505,-7.818955,5.944867,1.048811,-4.181984,-8.080407,9.059310,8.239910,-4.179136,-9.989796,7.145904,-2.661889,-4.687720,1.935382,8.602519,7.729802,-1.445919,5.243629,-5.189884,-9.861045,4.337477,0.899551,-9.940581,5.407432,-9.301417,7.168864,-1.340227,7.705898,0.315521,9.063726,9.746967,-0.907749,2.150668,7.506768,-9.033649,-5.220028,8.021538,8.878663,-0.783881,-3.322330,-6.056223,-3.347538,8.363266,9.674531,-1.658794,8.769673,-3.678860,9.471143,-2.364586,0.124796,8.285665,-4.397375,5.031805,-5.960324,-1.563323,-0.919738,7.468521,3.264905,8.236899,2.903411,-3.433667,5.757493,-5.671858,-4.622929,4.452400,-3.661511,9.768987,7.584691,-0.456134,-9.792239,-4.793636,4.367519,0.800634,9.722910,3.746210,-4.453042,9.598208,-4.014939,-3.470028,-6.913297,2.090779,-7.062817,1.107840,1.216066,-0.663253,-9.234703,9.047912,-4.265652,8.643131,4.963701,-4.391158,-4.414736,8.117270,-7.005627,3.225528,2.603229,8.164415,3.495523,-9.093085,-4.198749,-2.180865,5.568273,-4.294723,-6.568728,9.880105,-7.571472,1.709117,-2.055700,-5.200391,-1.997344,6.802972,-8.742937,-4.927795,-7.672184,-3.882025,0.820321,8.505283,-2.780018,-4.902955,7.964185,-0.644956,7.919787,-3.730063,-6.832500,-1.604854,-1.177579,7.808666,-9.499182,-9.649496,-0.344013,5.116728,6.719129,-5.004347,-5.042346,-1.433790,3.310317,-2.264036,-8.873704,-6.140474,9.293970,-5.385945,-6.531349,-7.571228,5.894155,1.295862,8.069896,4.555664,-4.250848,2.083789], dtype = "float32")#candidate|2615|(495,)|const|float32
call_2614 = relay.TupleGetItem(func_1640_call(relay.reshape(const_2615.astype('float32'), [15, 11, 3])), 1)
call_2616 = relay.TupleGetItem(func_1643_call(relay.reshape(const_2615.astype('float32'), [15, 11, 3])), 1)
func_1354_call = mod.get_global_var('func_1354')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_2620 = relay.const([2.565893,-0.380514,2.549685,5.145232,-1.574111,-0.780985,-7.318231,1.212742,-8.721137,2.826316,7.515308,8.091527,9.086623,5.907615,-5.296943,4.976237,-1.412180,-1.656250,-8.045485,-9.504930,0.557919,-9.854846,3.759518,-7.069851,4.362645,4.769497,2.505531,6.012344,6.418357,9.668808,-9.465471,-3.287019,4.344268,2.964205,-9.374687,-0.778137,-7.308060,4.169018,3.632202,-7.947874,-7.009349,2.747316,-9.800632,-6.152323,7.336482,9.496657,6.152618,6.922376,-2.796491,-2.905310,-8.037802,7.800444,0.663598,-5.024138,-4.569913,6.337007,-5.807794,6.663566,-3.151852,7.528212,9.653510,3.144089,-2.082474], dtype = "float32")#candidate|2620|(63,)|const|float32
const_2621 = relay.const([9,3,-4,5,4,-10,3,-5,-7,7,6,3,5,-2,-8,-2,-2,2,-8,8,4,2,-1,-4,5,10,-5,7,-4,8,10,8,6,10,6,-9,-5,8,8,-6,5,6,8,-9,-4,4,-8,-8,4,-2,7,9,-2,9,10,3,-3,5,-4,-4,5,4,2,-10,1,7,3,1,-4,5,8,-7,-9,-10,1,5,2,9,-3,-8,-1,4,2,1,-8,8,-6,-6,-1,10,-10,6,-4,6,4,-6,1,-2,7,-7,-10,10,-1,-3,-3], dtype = "int32")#candidate|2621|(105,)|const|int32
var_2622 = relay.var("var_2622", dtype = "uint32", shape = ())#candidate|2622|()|var|uint32
call_2619 = relay.TupleGetItem(func_1354_call(relay.reshape(const_2620.astype('float32'), [9, 1, 7]), relay.reshape(call_2614.astype('float32'), [9, 5, 7]), relay.reshape(const_2621.astype('int32'), [105, 1]), relay.reshape(var_2622.astype('uint32'), []), relay.reshape(call_2611.astype('float32'), [336,]), ), 2)
call_2623 = relay.TupleGetItem(func_1360_call(relay.reshape(const_2620.astype('float32'), [9, 1, 7]), relay.reshape(call_2614.astype('float32'), [9, 5, 7]), relay.reshape(const_2621.astype('int32'), [105, 1]), relay.reshape(var_2622.astype('uint32'), []), relay.reshape(call_2611.astype('float32'), [336,]), ), 2)
bop_2625 = relay.logical_xor(bop_2603.astype('uint16'), var_2622.astype('uint16')) # shape=(6, 11, 5)
output = relay.Tuple([call_2611,var_2612,call_2614,const_2615,call_2619,const_2620,const_2621,bop_2625,])
output2 = relay.Tuple([call_2613,var_2612,call_2616,const_2615,call_2623,const_2620,const_2621,bop_2625,])
func_2633 = relay.Function([var_2602,var_2612,var_2622,], output)
mod['func_2633'] = func_2633
mod = relay.transform.InferType()(mod)
mutated_mod['func_2633'] = func_2633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2633_call = mutated_mod.get_global_var('func_2633')
var_2635 = relay.var("var_2635", dtype = "uint8", shape = (6, 11, 5))#candidate|2635|(6, 11, 5)|var|uint8
var_2636 = relay.var("var_2636", dtype = "float32", shape = (336,))#candidate|2636|(336,)|var|float32
var_2637 = relay.var("var_2637", dtype = "uint32", shape = ())#candidate|2637|()|var|uint32
call_2634 = func_2633_call(var_2635,var_2636,var_2637,)
output = call_2634
func_2638 = relay.Function([var_2635,var_2636,var_2637,], output)
mutated_mod['func_2638'] = func_2638
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2650 = relay.var("var_2650", dtype = "int64", shape = (4, 10, 5))#candidate|2650|(4, 10, 5)|var|int64
var_2651 = relay.var("var_2651", dtype = "int64", shape = (4, 10, 5))#candidate|2651|(4, 10, 5)|var|int64
bop_2652 = relay.bitwise_xor(var_2650.astype('int64'), relay.reshape(var_2651.astype('int64'), relay.shape_of(var_2650))) # shape=(4, 10, 5)
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
var_2660 = relay.var("var_2660", dtype = "int32", shape = (105,))#candidate|2660|(105,)|var|int32
call_2659 = func_200_call(relay.reshape(var_2660.astype('int32'), [1, 15, 7]), relay.reshape(var_2660.astype('int32'), [1, 15, 7]), )
call_2661 = func_200_call(relay.reshape(var_2660.astype('int32'), [1, 15, 7]), relay.reshape(var_2660.astype('int32'), [1, 15, 7]), )
func_1640_call = mod.get_global_var('func_1640')
func_1643_call = mutated_mod.get_global_var('func_1643')
var_2672 = relay.var("var_2672", dtype = "float32", shape = (495,))#candidate|2672|(495,)|var|float32
call_2671 = relay.TupleGetItem(func_1640_call(relay.reshape(var_2672.astype('float32'), [15, 11, 3])), 1)
call_2673 = relay.TupleGetItem(func_1643_call(relay.reshape(var_2672.astype('float32'), [15, 11, 3])), 1)
output = relay.Tuple([bop_2652,call_2659,var_2660,call_2671,var_2672,])
output2 = relay.Tuple([bop_2652,call_2661,var_2660,call_2673,var_2672,])
func_2679 = relay.Function([var_2650,var_2651,var_2660,var_2672,], output)
mod['func_2679'] = func_2679
mod = relay.transform.InferType()(mod)
var_2680 = relay.var("var_2680", dtype = "int64", shape = (4, 10, 5))#candidate|2680|(4, 10, 5)|var|int64
var_2681 = relay.var("var_2681", dtype = "int64", shape = (4, 10, 5))#candidate|2681|(4, 10, 5)|var|int64
var_2682 = relay.var("var_2682", dtype = "int32", shape = (105,))#candidate|2682|(105,)|var|int32
var_2683 = relay.var("var_2683", dtype = "float32", shape = (495,))#candidate|2683|(495,)|var|float32
output = func_2679(var_2680,var_2681,var_2682,var_2683,)
func_2684 = relay.Function([var_2680,var_2681,var_2682,var_2683,], output)
mutated_mod['func_2684'] = func_2684
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2726 = relay.var("var_2726", dtype = "float64", shape = (1, 5, 8))#candidate|2726|(1, 5, 8)|var|float64
const_2727 = relay.const([[[-7.584473,-1.700530,-0.788127,-1.305368,-5.647869,2.516393,0.732441,-3.776236],[-1.816354,7.561666,9.104780,-0.071288,6.206837,6.474325,0.459233,2.957399],[7.206367,4.056779,-6.578317,-7.042051,-3.289246,-0.818417,8.098040,-4.129278],[4.714452,8.924862,-0.190285,-5.705416,4.362388,-4.015690,8.599799,-0.831157],[5.237118,-8.862885,-3.815995,5.660165,-4.677826,-0.272628,-8.960105,-7.669069]]], dtype = "float64")#candidate|2727|(1, 5, 8)|const|float64
bop_2728 = relay.subtract(var_2726.astype('float64'), relay.reshape(const_2727.astype('float64'), relay.shape_of(var_2726))) # shape=(1, 5, 8)
uop_2733 = relay.cos(bop_2728.astype('float64')) # shape=(1, 5, 8)
func_2679_call = mod.get_global_var('func_2679')
func_2684_call = mutated_mod.get_global_var('func_2684')
var_2736 = relay.var("var_2736", dtype = "int64", shape = (200,))#candidate|2736|(200,)|var|int64
const_2737 = relay.const([6,8,-8,-4,6,-10,-6,4,3,8,3,-6,5,-5,9,-2,7,-5,-8,1,-7,-1,-1,4,1,9,8,-10,-9,3,-8,3,6,-8,8,-8,-2,8,4,-7,-4,2,10,-4,-6,7,1,-9,1,-1,9,-4,10,2,3,-10,4,6,5,-4,-6,-5,2,-6,-1,2,8,-9,-7,4,-10,5,-8,9,3,-4,-4,-6,1,1,-2,-2,-8,-1,-1,3,9,7,-2,-1,-10,2,4,-2,3,-8,4,-3,8,7,9,3,9,5,4], dtype = "int32")#candidate|2737|(105,)|const|int32
var_2738 = relay.var("var_2738", dtype = "float32", shape = (495,))#candidate|2738|(495,)|var|float32
call_2735 = relay.TupleGetItem(func_2679_call(relay.reshape(var_2736.astype('int64'), [4, 10, 5]), relay.reshape(var_2736.astype('int64'), [4, 10, 5]), relay.reshape(const_2737.astype('int32'), [105,]), relay.reshape(var_2738.astype('float32'), [495,]), ), 2)
call_2739 = relay.TupleGetItem(func_2684_call(relay.reshape(var_2736.astype('int64'), [4, 10, 5]), relay.reshape(var_2736.astype('int64'), [4, 10, 5]), relay.reshape(const_2737.astype('int32'), [105,]), relay.reshape(var_2738.astype('float32'), [495,]), ), 2)
output = relay.Tuple([uop_2733,call_2735,var_2736,const_2737,var_2738,])
output2 = relay.Tuple([uop_2733,call_2739,var_2736,const_2737,var_2738,])
func_2741 = relay.Function([var_2726,var_2736,var_2738,], output)
mod['func_2741'] = func_2741
mod = relay.transform.InferType()(mod)
mutated_mod['func_2741'] = func_2741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2741_call = mutated_mod.get_global_var('func_2741')
var_2743 = relay.var("var_2743", dtype = "float64", shape = (1, 5, 8))#candidate|2743|(1, 5, 8)|var|float64
var_2744 = relay.var("var_2744", dtype = "int64", shape = (200,))#candidate|2744|(200,)|var|int64
var_2745 = relay.var("var_2745", dtype = "float32", shape = (495,))#candidate|2745|(495,)|var|float32
call_2742 = func_2741_call(var_2743,var_2744,var_2745,)
output = call_2742
func_2746 = relay.Function([var_2743,var_2744,var_2745,], output)
mutated_mod['func_2746'] = func_2746
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2868 = relay.var("var_2868", dtype = "float64", shape = (13, 15, 2))#candidate|2868|(13, 15, 2)|var|float64
uop_2869 = relay.cos(var_2868.astype('float64')) # shape=(13, 15, 2)
const_2880 = relay.const([[[7.065140,-6.323012],[9.027396,4.198211],[-5.736262,-5.224081],[8.877329,-4.112535],[-2.532321,-8.519660],[1.940287,6.395832],[-4.900370,4.645569],[-6.568132,9.274118],[0.536331,-9.300160],[-8.945814,-7.667005],[-1.144394,4.183684],[5.527604,1.174812],[-2.705004,7.649354],[-4.544675,-2.290238],[-4.131432,5.973699]],[[-4.685054,-6.190060],[-4.747114,5.834778],[0.885596,-3.862072],[-7.234258,9.669172],[1.287335,-2.677102],[-7.199597,-0.612934],[-0.180304,-6.344485],[-0.992900,6.024644],[-6.531937,-5.329715],[-5.468938,5.075463],[-3.975421,-4.810399],[-7.718296,-0.532318],[-8.332690,8.653560],[-1.419485,4.089206],[8.063615,3.327015]],[[5.669946,-1.779744],[4.969584,1.958214],[-2.785541,2.464867],[-0.747239,-1.971438],[2.979345,-2.691047],[5.723059,4.577369],[8.713121,-5.742654],[-8.044190,-4.798425],[-6.557916,8.979097],[-6.698168,7.894430],[6.050091,4.659188],[-2.251601,-6.953297],[-0.873544,1.056441],[4.767463,5.740328],[3.402124,2.599674]],[[-3.781035,-5.592850],[-5.595194,-4.071231],[-9.917306,-2.771472],[-3.110049,6.951785],[7.089815,-3.316042],[-8.134836,8.876893],[-2.577126,8.448724],[-7.743548,0.712467],[-8.012048,0.083954],[1.100154,9.533353],[6.559044,-5.212395],[0.498840,5.632474],[4.658640,-9.031834],[7.847217,9.108033],[7.369744,-8.986504]],[[2.824107,-4.064318],[7.025956,2.450782],[6.004062,-9.846966],[-2.195738,-9.796451],[-2.175498,-9.842786],[1.372799,0.004765],[-6.456101,4.186415],[8.959168,9.894052],[3.574724,2.641376],[1.871014,-2.740629],[9.888089,0.798891],[6.348836,-7.139943],[4.783296,7.098244],[8.313630,-8.228037],[-2.469817,8.426794]],[[2.872364,-4.174522],[-1.387917,5.514293],[-4.217550,-0.049903],[-0.739452,6.940631],[7.048635,8.758508],[-8.952040,-1.460323],[3.614999,5.969418],[-3.362292,-1.439806],[6.688438,-9.483626],[-8.867552,1.700797],[5.852826,-2.962655],[-0.372703,3.362537],[6.827568,-7.000032],[-1.883977,-3.518826],[5.594489,9.569071]],[[-9.925357,1.527651],[-2.826769,-8.042216],[6.782803,-6.202708],[1.672023,-1.079289],[-4.021890,-3.973120],[-4.385732,-3.255738],[1.812568,0.791064],[-0.498359,-8.328817],[-9.484291,8.037082],[1.555629,1.909517],[5.723059,-6.876767],[-6.897829,-5.211888],[-3.402873,2.600347],[-4.610772,5.054423],[-5.634774,-5.386266]],[[5.628617,9.124903],[9.085679,4.567210],[-2.963422,5.430239],[-8.013317,3.149356],[8.501447,3.648334],[-0.049430,-3.030799],[-1.492712,-7.721562],[-8.914858,-3.506789],[1.043877,4.089979],[-3.379218,3.417306],[2.501315,-3.838923],[-9.578084,7.907055],[-1.200586,-6.697572],[1.017153,3.557915],[-9.203277,-0.173969]],[[-6.536112,9.509281],[-6.806937,-3.382993],[7.290419,-0.734380],[7.433168,-2.264761],[-3.742903,4.486529],[-2.457083,6.407121],[-7.721267,-5.329865],[-2.008435,-0.398757],[9.222997,-6.422970],[-6.236113,-6.786009],[-5.512690,6.179304],[1.934501,-8.891768],[2.156882,-5.908491],[4.211982,1.039035],[-3.324526,-4.743151]],[[-0.635878,-6.959948],[-2.080592,7.145730],[3.444686,-9.837181],[-3.875174,5.833226],[2.627394,9.268932],[4.947942,1.331141],[0.879969,5.350592],[-1.232894,-4.999164],[-8.660435,-3.618838],[9.153021,9.527080],[4.790515,6.790158],[2.635388,1.254953],[-7.980151,2.554485],[7.816019,-5.492842],[6.229657,-2.538346]],[[7.538726,-0.965225],[7.932725,9.124285],[2.381178,-5.649517],[-0.416363,-4.424645],[-6.318270,0.229322],[7.412255,0.814084],[8.857563,8.045663],[5.944756,-5.018055],[3.037169,-9.113602],[0.306693,3.327480],[-2.331522,0.260313],[2.191355,6.375041],[9.036697,-1.710481],[8.381849,1.501139],[0.868114,-7.389193]],[[9.394164,-7.968793],[1.691290,7.963052],[-5.283375,3.548636],[-1.052113,3.575501],[5.699372,-7.845783],[2.875627,1.444185],[-9.663775,0.395002],[4.334088,-9.930529],[-3.875297,2.289485],[5.285949,-8.751689],[-4.876014,-8.086415],[-4.177576,-6.783645],[-6.594214,3.433775],[-2.626836,1.415252],[1.652751,-5.321912]],[[-0.469117,3.558541],[0.332320,-7.087756],[-5.296166,-7.534432],[6.140184,7.000833],[6.054596,8.296121],[-9.986650,0.846548],[2.230415,1.885707],[-0.137957,2.560699],[-3.282324,8.988566],[-5.425208,-3.803669],[7.608274,2.191399],[-4.984081,-9.858540],[-6.483432,3.309704],[-5.999793,6.276561],[0.915659,2.012731]]], dtype = "float64")#candidate|2880|(13, 15, 2)|const|float64
bop_2881 = relay.right_shift(var_2868.astype('uint32'), relay.reshape(const_2880.astype('uint32'), relay.shape_of(var_2868))) # shape=(13, 15, 2)
output = relay.Tuple([uop_2869,bop_2881,])
output2 = relay.Tuple([uop_2869,bop_2881,])
func_2908 = relay.Function([var_2868,], output)
mod['func_2908'] = func_2908
mod = relay.transform.InferType()(mod)
var_2909 = relay.var("var_2909", dtype = "float64", shape = (13, 15, 2))#candidate|2909|(13, 15, 2)|var|float64
output = func_2908(var_2909)
func_2910 = relay.Function([var_2909], output)
mutated_mod['func_2910'] = func_2910
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3194 = relay.var("var_3194", dtype = "float32", shape = (10, 5, 15))#candidate|3194|(10, 5, 15)|var|float32
uop_3195 = relay.atanh(var_3194.astype('float32')) # shape=(10, 5, 15)
func_1430_call = mod.get_global_var('func_1430')
func_1435_call = mutated_mod.get_global_var('func_1435')
var_3199 = relay.var("var_3199", dtype = "int16", shape = (15, 9))#candidate|3199|(15, 9)|var|int16
var_3200 = relay.var("var_3200", dtype = "int16", shape = (675,))#candidate|3200|(675,)|var|int16
const_3201 = relay.const([[8],[-2],[1],[-10],[-6],[3],[-6],[10],[-4],[-1],[-4],[-6],[5],[9],[5],[-8],[-1],[10],[2],[5],[6],[7],[-6],[1],[5],[3],[-3],[4],[-8],[-6],[4],[-8],[6],[9],[9],[-5],[1],[-8],[-10],[6],[-1],[7],[-10],[3],[-5],[1],[-5],[-6],[-6],[-9],[8],[-1],[-8],[5],[9],[5],[2],[3],[-4],[10],[-5],[1],[-7],[-9],[4],[7],[1],[-1],[8],[-9],[7],[7],[10],[3],[-8],[5],[1],[3],[5],[-2],[-1],[-10],[-8],[3],[7],[5],[8],[7],[-3],[1],[-3],[-5],[4],[-4],[-10],[-9],[5],[3],[-2],[-1],[8],[7],[7],[-5],[-4]], dtype = "int32")#candidate|3201|(105, 1)|const|int32
var_3202 = relay.var("var_3202", dtype = "float32", shape = (336,))#candidate|3202|(336,)|var|float32
call_3198 = relay.TupleGetItem(func_1430_call(relay.reshape(var_3199.astype('int16'), [1, 15, 9]), relay.reshape(var_3200.astype('int16'), [5, 15, 9]), relay.reshape(const_3201.astype('int32'), [105,]), relay.reshape(var_3202.astype('float32'), [2, 168]), ), 6)
call_3203 = relay.TupleGetItem(func_1435_call(relay.reshape(var_3199.astype('int16'), [1, 15, 9]), relay.reshape(var_3200.astype('int16'), [5, 15, 9]), relay.reshape(const_3201.astype('int32'), [105,]), relay.reshape(var_3202.astype('float32'), [2, 168]), ), 6)
uop_3204 = relay.sin(uop_3195.astype('float32')) # shape=(10, 5, 15)
func_1006_call = mod.get_global_var('func_1006')
func_1009_call = mutated_mod.get_global_var('func_1009')
const_3215 = relay.const([6,4,-10,8,5,-3,4,-2,-1,-10,7,8,8,-3,7,-10,1,1,-4,-1,2,1,-1,6,-3,7,-2,6,-10,8,10,-10,-9,-2,-9,9,7,9,5,10,-4,8,3,-7,-2,8,-3,2,-9,-5,7,10,-8,-2,6,8,10,-5,1,-3,1,4,-4,-5,1,1,-8,2,2,6,5,-8,-4,-5,9,10,3,-3,2,-10,-10,3,-4,3,-8,-5,-6,7,8,-5,-3,-6,-10,-3,-8,5,6,7,2,9,2,-4,-7,-8,-4,3,-9,4,-9,-4,-2,7,9,-9,6,3,-1,6,-8,2,-7,-9,-5,6,4,1,8,-5,1,-8,-3,7,-9,-2,5,-9,1,9,-5,-8,-6,4,-6,-3,-4,-4,-3,10,3,-9,8,-1,9,4,6,2,10,7,6,3,-10,-8,-9,5,10,10,-3,6,-2,4,2,-1,-4,10,-8,-2,3,3,8,-4,3,6,-7,-8,3,-9,9,-9,10,-3,-6,1,4,-1,-2,-1,-1,3,-9,8,-2,-9,9,-6,-9,1,3,-5,4,9,1,2,-7,1,-5,-10,-6,-10,6,7,-4,-9,8,5,-9,1,2,-5,10,7,-5,-4,3,-7,1,-4,-10,-3,-8,4,1,-9,-1,-4,-8,-6,-7,3,6,10,-4,2,9,6,-2,-7,6,-7,-10,-7,3,1,-4,1,6,7,10,-6,3,-8,-2,9,1,-4,1,9,-5,-6,-7,-8,10,7,-5,9,-4,-6,-2,-2,-2,-1,-8,-9,-1,9,-1,4,-4,-1,3,8,7,-2,8,-1,2,5,4,-10,-8,4,-8,9,9,-3,-2,-10,7,-9,7,7,-3,7,8,-2,-8,4,-7,10,-6,10,5,6,-1,-7,4,6,-10,-5,-2,-5,-5,6,3,-10,8,5,-10,-7,6,9,-10,9,10,8,-9,2,-1,6,4,-3,5,-8,-10,4,-9,-8,-8,8,-1,9,7,-3,-10,2,-6,8,4,-4,3,2,3,-2,9,10,-6,9,2,4,3,-8,1,-10,-6,-9,4,-2,3,7,-5,9,6,9,-10,-10,8,-1,5,-4,-4,9,-6,5,8,9,-9,-9,6,4,10,8,1,-7,-9,-9,-5,2,-1,1,1,5,8,-6,1,-10,-4,-8,-6,-3,-7,-1,-1,4,-2,-3,4,-4,1,7,-1,-4,-5,-2,-9,-7,9,9,-1,-4,-7,-5,-7,3,10,-2,9,6,8,5,2,4,-2,-1,-5,5,4,-2,10,8,7,10,6,10,-3,1,-8,7,5,2,-5,-3,10,9,-5,1,7,-8,5,-8,2,4,-2,2,2,-9,-3,-7,10,-5,3,6,5,-6,1,-1,-1,7,-9,-3,4,-8,-4,2,-1,10,-2,7,-2,10,-4,10,-7,9,5,4,3,8,7,5,6,-3,2,6,10,9,6,-9,6,10,9,-3,-8,-2,-1,-4,-10,3,-4,10,-2,5,-8,-4,4,10,-10,6,3,4,4,-1,2,8,1,-7,9,-5,-8,-5,-5,-6,7,-2,9,-6,-1,-7,9,8,-5,6,-8,-3,2,-9,-1,1,-6,-10,-8,-7,-1,3,-4,-3,7,-3,2,1,3,10,-4,4,3,-6,10,3,10,3,-8,-2,-6,8,-2,2,1,-1,-3,7,-7,-1,6,10,2,1,2,3,-10,-5,-1,10,-1,7,4,-3,6,-9,8,10,5,-7,5,-4,-4,9,-8,-7,2,4,-7,8,-1,-6,10,-8,-7,1,-7,-9,6,6,9,-4,9,-6,6,-2,4,-7,-5,-9,-10,-4,-5,-9,1,6,3,2,1,10,3,-4,1,-3,-6,9,-3,6,8,-9,-3,10,7,7,1,5,1,-2,3,-1,6,-7,-6,8,-8,-4,4,-6,7,10,5,1,9,10,-9,-2,-4,-5,-4,2,-10,5,-2,6,6,-5,-3,9,-10,-3,2,3,6,4,-8,2,-5,-1,-9,4,3,8,-8,8,-4,6,-8,-1,8,6,4,-4,-4,5,4,-9,-1,-2,2,8,5,-3,4,9,1,-7,-3,1,-10,3,6,-10,8,5,-4,-9,6,3,-8,-3,8,-2,-3,-10,-1,-6,4,-3,9,-6,2,3,-7,-9,1,-6,4,-1,2,1,-6,-10,4,-5,-3,8,-6,5,-7,10,8,8,3,8,-3,-9,-7,-9,2,4,5,-9,4,4,-8,-1,10,8,-9,9,7,-8,4,-7,-1,10,-4,-5,-4,-10,-3,1,-8,-5,7,-8,-9,-1,4,-9,-9,-1,7,9,-4,6,-10,9,5,-7,-7,5,3,-10,3,4,-6,5,10,7,-5,-1,9,4,-5,4,-8,-9,6,8,9,-1,6,10,-10,-1,-1,1,-4,4,8,3,-9,-8,4,-4,7,-7,1,-8,4,7,2,5,-3,-7,-7,8,7,-10,-10,-5,2,-2,9,6,-9,-9,1,1,3,6,10,-5,-9,-9,1,-8,6,-8,9,-8,-6,-3,3,4,2,5,3,-1,6,1,-4,10,8,4,-1,8,-1,6,-5,-1,10,8,-7,6,-9,-1,-8,2,7,5,-10,7,6,-7,-6,7,-4,1,-4,-5,8,3,-4,-1,-2,-1,3,-6,-1,-1,1,5,3,-7,5,-7,5,-6,-8,4,-7,-4,2,9,-3,2,-6,-9,3,7,7,8,5,-3,-4,5,-3,-10,-9,8,-7,7,-7,6,2,7,-7,-3,2,-7,4,-8,1,2,8,5,2,1,-10,-1,-10,4,-7,10,-5,-6,1,6,3,-5,7,8,-1,1,6,6,2,3,-6,-7,-2,-10,8,-6,-3,3,10,-1,10,4,4,4,-9,5,2,6,6,6,3,6,2,8,-3,-2,-1,-1,-6,10,1,-1,-7,8,5,7,7,-4,7,10,-8,-2,-1,-5,9,-2,-3,5,2,-3,-7,-4,8,-3,9,4,10,-10,1,7,1,10,6,3,-7,6,-1,-10,10,3,-9,-1,-2,-7,4,-3,-7,10,6,-1,4,-9,-8,3,2,-9,4,9,1,-9,4,-2,4,-2,7,-7,1,-5,7,-8,5,-10,-7,5,7,-5,-7,-1,10,3,-9,10,6,-8,5,-2,5,-7,4,-2,-5,1,-3,5,8,-1,-8,-4,6,9,-1,-10,-4,-1,-1,9,-10,-10,-5,-6,-2,-9,-8,7,8,-5,-7,-5,4,-9,-9,-2,1,3,6,-10,-8,1,3,-10,-3,7,-2,3,10,-2,2,-9,-6,10,4,2,-8,-8,2,9,-4,9,1,-5,-6,10,-3,-3,-3,-2,-3,-9,-1,2,-6,1,1,8,-2,5,-4,-5,5,-7,-1,5,7,-4,10,10,-1,6,10,4,-10,7,-5,10,-10,-10,8,-4,-1,3,-8,-7,-5,9,-10,-5,-3,6,-7,-9,5,-10,5,8,-4,-7,-6,-1,1,4,4,-2,4,-6,4,9,-5,4,3,-7,-5,-9,-1,1,10,-1,-7,-3,3,-3,9,10,-1,5,8,-2,6,-3,-2,9,10,-8,7,9,3,8,-5,7,3,-1,3,2,-5,-8,-1,-8,-9,9,8,-3], dtype = "uint64")#candidate|3215|(1350,)|const|uint64
call_3214 = relay.TupleGetItem(func_1006_call(relay.reshape(const_3215.astype('uint64'), [15, 9, 10]), relay.reshape(const_3215.astype('uint64'), [15, 9, 10]), ), 0)
call_3216 = relay.TupleGetItem(func_1009_call(relay.reshape(const_3215.astype('uint64'), [15, 9, 10]), relay.reshape(const_3215.astype('uint64'), [15, 9, 10]), ), 0)
bop_3225 = relay.mod(uop_3204.astype('float32'), relay.reshape(uop_3195.astype('float32'), relay.shape_of(uop_3204))) # shape=(10, 5, 15)
uop_3231 = relay.sinh(uop_3204.astype('float64')) # shape=(10, 5, 15)
output = relay.Tuple([call_3198,var_3199,var_3200,const_3201,var_3202,call_3214,const_3215,bop_3225,uop_3231,])
output2 = relay.Tuple([call_3203,var_3199,var_3200,const_3201,var_3202,call_3216,const_3215,bop_3225,uop_3231,])
func_3234 = relay.Function([var_3194,var_3199,var_3200,var_3202,], output)
mod['func_3234'] = func_3234
mod = relay.transform.InferType()(mod)
var_3235 = relay.var("var_3235", dtype = "float32", shape = (10, 5, 15))#candidate|3235|(10, 5, 15)|var|float32
var_3236 = relay.var("var_3236", dtype = "int16", shape = (15, 9))#candidate|3236|(15, 9)|var|int16
var_3237 = relay.var("var_3237", dtype = "int16", shape = (675,))#candidate|3237|(675,)|var|int16
var_3238 = relay.var("var_3238", dtype = "float32", shape = (336,))#candidate|3238|(336,)|var|float32
output = func_3234(var_3235,var_3236,var_3237,var_3238,)
func_3239 = relay.Function([var_3235,var_3236,var_3237,var_3238,], output)
mutated_mod['func_3239'] = func_3239
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3617 = relay.var("var_3617", dtype = "uint16", shape = (10, 4, 15))#candidate|3617|(10, 4, 15)|var|uint16
var_3618 = relay.var("var_3618", dtype = "uint16", shape = (10, 4, 15))#candidate|3618|(10, 4, 15)|var|uint16
bop_3619 = relay.right_shift(var_3617.astype('uint16'), relay.reshape(var_3618.astype('uint16'), relay.shape_of(var_3617))) # shape=(10, 4, 15)
uop_3630 = relay.asin(bop_3619.astype('float32')) # shape=(10, 4, 15)
func_2908_call = mod.get_global_var('func_2908')
func_2910_call = mutated_mod.get_global_var('func_2910')
var_3645 = relay.var("var_3645", dtype = "float64", shape = (5, 78))#candidate|3645|(5, 78)|var|float64
call_3644 = relay.TupleGetItem(func_2908_call(relay.reshape(var_3645.astype('float64'), [13, 15, 2])), 1)
call_3646 = relay.TupleGetItem(func_2910_call(relay.reshape(var_3645.astype('float64'), [13, 15, 2])), 1)
func_767_call = mod.get_global_var('func_767')
func_774_call = mutated_mod.get_global_var('func_774')
var_3652 = relay.var("var_3652", dtype = "uint64", shape = ())#candidate|3652|()|var|uint64
const_3653 = relay.const([[4],[-3],[-2],[-3],[5],[1],[-2],[2],[2],[6],[-8],[-1],[-8],[-6],[-10],[-4],[-4],[1],[7],[8],[-5],[9],[4],[1],[7],[-7],[-10],[10],[3],[6],[8],[-10],[-10],[-8],[-4],[-10],[5],[-6],[1],[4],[5],[-3],[-10],[-4],[-10],[-8],[4],[-9],[-10],[1],[5],[-1],[-1],[1],[4],[-7],[7],[-7],[2],[-3],[4],[1],[1],[2],[8],[5],[3],[6],[-5],[-5],[2],[-10],[-2],[9],[-8],[8],[-4],[-2],[10],[-8],[5],[2],[1],[3],[6],[-5],[-10],[7],[-5],[9],[9],[-7],[-6],[-1],[1],[5],[-3],[8],[-8],[10],[-9],[-10],[3],[4],[-6],[-1],[-10],[-1],[5],[3],[9],[6],[6],[6],[4],[-5],[10],[-3],[-5],[-8],[10],[9],[8],[-6],[-9],[-3],[-6],[2],[10],[5],[-5],[-7],[8],[-7],[9],[-7],[7],[-8],[-5],[9],[1],[4],[-8],[1],[-6],[4],[-9],[-6],[10],[-3],[1],[7],[3],[2],[-10],[-1],[3],[-10],[4],[1]], dtype = "uint64")#candidate|3653|(160, 1)|const|uint64
var_3654 = relay.var("var_3654", dtype = "int32", shape = (105,))#candidate|3654|(105,)|var|int32
const_3655 = relay.const([[9],[6],[-7],[5],[4],[-9],[2],[9],[9],[5],[10],[-10],[9],[-9],[-5],[10],[2],[-7],[2],[-6],[-3],[-7],[-4],[9],[8],[9],[3],[9],[3],[6],[5],[-4],[-2],[10],[3],[10],[3],[-3],[4],[2],[7],[-9],[3],[4],[-8],[-5],[-8],[1],[-10],[-4],[7],[8],[-1],[-8],[-4],[8],[2],[-6],[7],[-2],[-2],[-5],[-6],[10],[9],[8],[10],[-9],[9],[-8],[8],[6],[3],[-4],[2],[3],[-4],[4],[-9],[3],[-10],[6],[-7],[1],[-10],[10],[-4],[7],[-8],[8],[-10],[-4],[3],[2],[6],[-10],[8],[-6],[-10],[-2],[-7],[10],[1],[-1],[-10],[-1],[-1],[-3],[-6],[-4],[4],[-9],[-9],[7],[6],[-2],[6],[-4],[-9],[5],[3],[-10],[-2],[-9],[-9],[1],[9],[6],[-6],[9],[-6],[5],[-1],[8],[4],[-9],[-1],[1],[1],[-2],[-5],[4],[2],[1],[-2],[-10],[-1],[10],[-3],[-4],[-2],[-4],[-2],[-6],[7],[5],[-10],[5],[8],[-10],[6],[1],[-4],[-1],[-7],[-4],[8],[2],[4],[-2],[8],[2],[-6],[-10],[3],[-5],[1],[-8],[6],[1],[-4],[2],[2],[-9],[2],[7],[1],[-7],[-4],[-1],[10],[-8],[3],[7],[-5],[1],[-3],[1],[-7],[-4],[-4],[-8],[-8],[-1],[-4],[1],[-10],[7],[7],[1],[2],[1],[-4],[-5],[-3],[-9],[-7],[3],[4],[2],[-8],[-3],[4],[-10],[-4],[2],[4],[5],[6],[-9],[6],[7],[9],[-1],[-5],[4],[-5],[-2],[9],[-9],[4],[10],[7],[-5],[5],[3],[6],[-7],[1],[7],[-10],[-9],[-9],[6],[-4],[10],[-6],[-3],[-8],[-5],[4],[2],[-9],[2],[-8],[8],[-1],[-5],[-10],[8],[-7],[10],[-1],[-8],[3],[9],[3],[-5],[2],[-4],[8],[8],[-1],[-2],[5],[-4],[10],[-8],[9],[9],[-1],[-9],[-4],[7],[-4],[8],[-5],[3],[-1],[-6],[7],[-3],[-4],[-10],[-6],[4],[9],[-2],[-8],[1],[-9],[3],[-5],[-9],[-5],[7],[5],[-1],[-10],[1],[-7],[-5],[-8],[9],[5],[-7],[-9],[10],[1],[2],[-2],[-10],[-10],[5],[9],[8],[-3],[-4],[2],[-9],[5],[1],[8],[-8],[1],[-5],[-1],[-2],[-5],[3],[-5],[1],[5],[-8],[-1],[4],[-3],[-2],[8],[-10],[-1],[4],[1],[5],[2],[-9],[10],[-2],[-7],[4],[5],[6],[4],[-9],[-7],[3],[-5],[2],[-10],[-3],[8],[7],[3],[-4],[10],[-10],[5],[5],[3],[2],[-4],[-10],[2],[6],[-2],[2],[2],[-5],[-1],[-5],[7],[9],[1],[-1],[-7],[-6],[10],[1],[-1],[-1],[5],[-10],[-7],[2],[-6],[-10],[-4],[4],[5],[2],[10],[5],[6],[-9],[-1],[10],[8],[-5],[-7],[-2],[5],[5],[-2],[-5],[-6],[-9],[6],[6],[9],[1],[-10],[8],[-8],[-10],[1],[7],[5],[-7],[3],[-6],[-10],[-7],[10],[-10],[-1],[-9],[-1],[8],[3],[4],[1],[1],[-5],[4],[10],[-7],[4],[7],[-7],[3],[10],[-10],[2],[-10],[-9],[6],[-8],[-7],[5],[1],[1],[6],[-1],[-1],[1],[-8],[-7],[-2],[10],[1],[-8],[9],[-6],[-9],[8],[-4],[7],[6],[2],[8],[-3],[-6],[9],[-9],[-10],[8],[9],[-6],[-6],[6],[4],[-4],[-2],[10],[-2],[-9],[7],[5],[-3],[-4],[-5],[3],[-2],[9],[-3],[-1],[-6],[7],[-7],[-2],[-7],[4],[-6],[7],[3],[4],[-6],[4],[-5],[3],[9],[-4],[-10],[3],[-10],[-8],[7],[9],[3],[5],[-9],[-6],[8],[-10],[-2],[-1],[-10],[-5],[8],[10],[4],[2],[-4],[-7],[1],[2],[2],[5],[-7],[-3],[10],[1],[-10],[10],[6],[-5],[2],[2],[-10],[-2],[10],[1],[2],[-4],[-10],[10],[-2],[10],[7],[10],[-2],[2],[4],[-9],[-2],[7],[4],[5],[-3],[7],[-5],[-3],[-7],[-1],[-5],[-6],[7],[10],[-3],[-6],[-9],[-8],[-3],[1],[10],[-1],[-6],[-2],[-9],[7],[-3],[10],[2],[-1],[-6],[-1],[-2],[-8],[-10],[2],[8],[4],[8],[-4],[10],[-1],[-4],[-5],[9],[-3],[-3],[-2],[3],[-1],[-10],[4],[-6],[9],[-8],[-1],[6],[-1],[2],[-9],[2],[-10],[10],[1],[3],[-6],[-6],[-10],[-1],[-6],[-5],[5],[-10],[-2],[-4],[5],[-6],[-2],[-8],[-8],[6],[-3],[-6],[-7],[-5],[-6],[-2],[2],[1],[6],[6],[3],[8],[-6],[8],[-7],[-2],[9],[7],[-7],[-8],[5],[-5],[-2],[10],[2],[-3],[5],[10],[-10],[-9],[-3],[9],[-1],[7],[-1],[2],[-5],[-2],[5],[-6],[5],[4],[1],[-5],[-2],[-7],[-7],[6],[-7],[7],[-8],[-5],[-6],[-9],[-6],[-8],[6],[-2],[5],[7],[-4],[-2],[-5],[9],[3],[-9],[5],[-3],[10],[1],[-7],[-8],[2],[10],[-1],[-5],[-5],[4],[-7],[-1],[6],[-9],[-5],[-1],[-4],[-4],[5],[6],[4],[-7],[4],[8],[10],[9],[-4],[6],[-4],[3],[9],[6],[-10],[4],[2],[5],[5],[3],[-3],[-9],[4],[8],[2],[-9],[1],[6],[6],[3],[4],[-1],[7],[-4],[-7],[4],[-9],[-3],[-4],[-10],[9],[3],[-9],[-9],[-2],[-1],[10],[-5],[-8],[-3],[-8],[-5],[3],[8],[2],[-4],[-7],[-10],[7],[-1],[2],[7],[6],[10],[1],[-6],[-2],[5],[-10],[-3],[-3],[3],[5],[8],[1],[-10],[3],[-6],[9],[2],[-1],[10],[1],[1],[2],[-6],[-2],[-7],[-10],[-8],[4],[5],[-5],[-8],[-7],[4],[-9],[3],[2],[3],[-7],[-9],[8],[7],[-10],[-1],[3],[4],[7],[2],[-10],[-3],[-1],[-1],[10],[4],[-5],[-8],[8],[-2],[-2],[-3],[-1],[5],[-6],[-1],[3],[7],[10],[-6],[-4],[-8],[5],[3],[-1],[2],[-2],[-8],[-1],[-10],[-10],[-3],[-6],[-7],[-8],[5],[-3],[-10],[-8],[2],[2],[3],[-8],[-8],[6],[5],[-10],[8],[-9],[-10],[-8],[-9],[-7],[9],[-6],[5],[4],[3],[-2],[10],[8],[5],[6],[-3],[8],[1],[10],[7],[1],[-5],[7],[-6],[-9],[-5],[-9],[-1],[2],[4],[-9],[2],[2],[-3],[3],[2],[-6],[-10],[6],[-5],[4],[-7],[7],[-9],[-4],[-9],[-2],[10],[4],[6],[3],[-3],[2],[3],[-9],[6],[10],[-6],[1],[-8],[-10],[8],[7],[6],[1],[-1],[8],[3],[-9],[-10],[7],[-2],[9],[-6],[5],[7],[-2],[-7],[-3],[2],[-3],[-8],[9],[10],[10],[-6],[8],[-5],[-10],[-9],[-6],[10],[1],[9],[-2],[-8],[8],[-7],[7],[-6],[-9],[-5],[-4],[4],[-3],[9],[-9],[-9],[8],[-6],[3],[-7],[-10],[-7],[-4],[-6],[-7],[2],[5],[-5],[2],[10],[-3],[-4],[1],[5],[-6],[2],[-9],[-4],[3],[-9],[-5],[4],[-10],[-8],[3],[4],[9],[8],[7],[-1],[-8],[-10],[-3],[1],[6],[-10],[3],[-1],[-3],[5],[-9],[1],[-4],[7],[4],[6],[-2],[-8],[-3],[-4],[-1],[2],[-6],[-6],[3],[4],[-10],[-9],[4],[10],[7],[-2],[4],[-5],[1],[6],[4],[7],[-2],[-9],[-4],[-9],[8],[1],[-6],[-3],[-6],[-4],[-5],[7],[-8],[7],[2],[4],[-6],[-1],[7],[-9],[7],[-10],[10],[8],[6],[-6],[10],[-6],[-4],[-2],[8],[-10],[-10],[7],[8],[2],[-5],[-10],[6],[8],[-9],[5],[-8],[8],[6],[8],[-6],[10],[-1],[3],[2],[-7],[-10],[1],[7],[9],[6],[5],[-7],[-5],[5],[-8],[-4],[-8],[5],[6],[-9],[-6],[10],[-6],[-1],[-2],[3],[2],[-2],[-4],[4],[7],[10],[5],[-7],[5],[-2],[6],[2],[-10],[8],[-3],[-1],[2],[4],[8],[8],[6],[-1],[3],[1],[-3],[-1],[-6],[2],[8],[-10],[-3],[-8],[2],[-9],[-9],[-6],[-6],[7],[-4],[-9],[3],[7],[-7],[-5],[-10],[-5],[-6],[6],[-4],[6],[3],[-10],[10],[8],[8],[-2],[-1],[10],[9],[2],[10],[10],[2],[-4],[2],[-2],[4],[4],[1],[-8],[3],[-8],[1],[10],[-3],[9],[10],[1],[-7],[8],[5],[-4],[2],[-4],[2],[-2],[2],[-9],[7],[-4],[10],[6],[-5],[3],[2],[-1],[3],[-7],[-5],[-10],[3],[-4],[-1],[1],[-10],[8],[8],[-3],[-9],[-5],[8],[-7],[3],[-8],[4],[-5],[-9],[3],[2],[7],[9],[-4],[-7],[10],[-3],[-8],[-2],[4],[10],[-4],[-9],[3],[-10],[7],[2],[-3],[-7],[-10],[4],[-4],[-6],[10],[7],[3],[-5],[4],[-8],[3],[5],[9],[3],[-10],[1],[-7],[-9],[-3],[-1],[-5],[6],[-8],[5],[-6],[-8],[10],[-8],[3],[-10],[-2],[-3],[7],[-7],[-7],[5],[1],[-9],[2],[-10],[6],[7],[3],[4],[-7],[-1],[7],[-5],[3],[7],[4],[-3],[-5],[3],[-6],[-8],[-3],[8],[-2],[-4],[-9],[7],[6],[-2],[-6],[3],[3],[5],[8],[-5],[-3],[9],[-8],[3],[-1],[9],[3],[-6],[8],[10],[-7],[5],[8],[-7],[-10],[-3],[3],[-10],[-8],[3],[4],[-9],[-9],[-4],[5],[4],[8],[3],[9],[-4],[-10],[3],[-6],[-6],[-10],[6],[-4],[8],[2],[-2],[-7],[-10],[-6],[-3],[-2],[-4],[-4],[8],[2],[4],[5],[-3],[-5],[-2],[-5],[5],[-1],[-7],[7],[-1],[-8],[3],[-4],[10],[5],[9],[6],[-10],[-4],[-7],[7],[1],[8],[-6],[-9],[-3],[-2],[7],[-7],[5],[2],[3],[5],[-8],[-6],[-8],[-8],[4],[6],[-10],[6],[9],[2],[-5],[4],[-3],[3],[6],[-1],[-7],[-1],[1],[-1],[-7],[4],[-1],[3],[-10],[8],[7],[7],[-10],[-8],[-8],[-1],[8],[-1],[3],[-6],[10],[-10],[-10],[-3],[-1],[8],[-4],[-8],[7],[3],[4],[2],[7],[-1],[-5],[5],[-6],[-6],[-9],[1],[-9],[7],[-3],[-10],[-10],[-6],[8],[-8],[-1],[-9],[7],[2],[8],[-4],[-5],[8],[1],[7],[-10],[-6],[1],[-7],[-2],[-6],[-6],[-1],[-9],[-8],[1],[6],[4],[-9],[-9],[3],[-5],[-10],[-3],[-5],[-3],[-9],[-8],[-6],[5],[7],[-6],[1],[-9],[7],[9],[5],[-10],[-2],[3],[-7],[-10],[9],[-9],[8],[7],[-10],[-8],[-4],[-1],[5],[2],[-6],[7],[5],[-5],[8],[3],[7],[2],[-5],[-9],[-3],[6],[-6],[-2],[-9],[-10],[-9],[2],[9],[-8],[-5],[6],[-2],[7],[7],[-4],[7],[-10],[9],[1],[-6],[-10],[10],[-9],[-1],[5],[8],[8],[-10],[-9],[3],[7],[-5],[2],[-7],[-1],[-5],[-8],[-5],[1],[-3],[-2],[10],[1],[6],[-6],[7],[-10],[10],[-6],[4],[2],[8],[-4],[4],[-7],[-4],[8],[-10],[3],[-2],[7],[-2],[-2],[9],[-3],[-5],[4],[-4],[6],[-4],[7],[-3],[-1],[5],[-9],[2],[-4],[4],[-9],[4],[-10],[7],[-2],[-2],[9],[5],[-5],[10],[-1],[7],[1],[9],[4],[-1],[-6],[6],[-6],[10],[4],[-10]], dtype = "uint32")#candidate|3655|(1694, 1)|const|uint32
var_3656 = relay.var("var_3656", dtype = "uint64", shape = (294,))#candidate|3656|(294,)|var|uint64
call_3651 = relay.TupleGetItem(func_767_call(relay.reshape(var_3652.astype('uint64'), []), relay.reshape(const_3653.astype('uint64'), [8, 2, 10]), relay.reshape(var_3654.astype('int32'), [105,]), relay.reshape(const_3655.astype('uint32'), [1694,]), relay.reshape(var_3656.astype('uint64'), [6, 7, 7]), ), 4)
call_3657 = relay.TupleGetItem(func_774_call(relay.reshape(var_3652.astype('uint64'), []), relay.reshape(const_3653.astype('uint64'), [8, 2, 10]), relay.reshape(var_3654.astype('int32'), [105,]), relay.reshape(const_3655.astype('uint32'), [1694,]), relay.reshape(var_3656.astype('uint64'), [6, 7, 7]), ), 4)
output = relay.Tuple([uop_3630,call_3644,var_3645,call_3651,var_3652,const_3653,var_3654,const_3655,var_3656,])
output2 = relay.Tuple([uop_3630,call_3646,var_3645,call_3657,var_3652,const_3653,var_3654,const_3655,var_3656,])
func_3668 = relay.Function([var_3617,var_3618,var_3645,var_3652,var_3654,var_3656,], output)
mod['func_3668'] = func_3668
mod = relay.transform.InferType()(mod)
mutated_mod['func_3668'] = func_3668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3668_call = mutated_mod.get_global_var('func_3668')
var_3670 = relay.var("var_3670", dtype = "uint16", shape = (10, 4, 15))#candidate|3670|(10, 4, 15)|var|uint16
var_3671 = relay.var("var_3671", dtype = "uint16", shape = (10, 4, 15))#candidate|3671|(10, 4, 15)|var|uint16
var_3672 = relay.var("var_3672", dtype = "float64", shape = (5, 78))#candidate|3672|(5, 78)|var|float64
var_3673 = relay.var("var_3673", dtype = "uint64", shape = ())#candidate|3673|()|var|uint64
var_3674 = relay.var("var_3674", dtype = "int32", shape = (105,))#candidate|3674|(105,)|var|int32
var_3675 = relay.var("var_3675", dtype = "uint64", shape = (294,))#candidate|3675|(294,)|var|uint64
call_3669 = func_3668_call(var_3670,var_3671,var_3672,var_3673,var_3674,var_3675,)
output = call_3669
func_3676 = relay.Function([var_3670,var_3671,var_3672,var_3673,var_3674,var_3675,], output)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3792 = relay.var("var_3792", dtype = "uint64", shape = (7, 15, 8))#candidate|3792|(7, 15, 8)|var|uint64
var_3793 = relay.var("var_3793", dtype = "uint64", shape = (7, 15, 8))#candidate|3793|(7, 15, 8)|var|uint64
bop_3794 = relay.equal(var_3792.astype('bool'), relay.reshape(var_3793.astype('bool'), relay.shape_of(var_3792))) # shape=(7, 15, 8)
func_3234_call = mod.get_global_var('func_3234')
func_3239_call = mutated_mod.get_global_var('func_3239')
const_3799 = relay.const([-3.601120,-1.499295,0.748711,8.687020,-3.549637,-8.551083,-0.043120,3.353906,-7.432317,-4.026188,1.647107,-9.021591,5.535264,-0.762658,1.597436,5.607597,-2.076716,6.315739,-5.063051,6.008039,-5.497545,-1.191871,-5.728594,-6.657705,8.414946,4.495479,-2.315133,5.895653,-1.621937,-3.917439,-6.715886,7.433313,-5.535185,-1.597283,2.026267,0.265627,-7.397429,-0.619376,-8.680509,5.339701,-1.492830,-8.784967,-4.213768,-3.068458,2.145568,3.807282,-3.519238,1.421455,6.511473,-8.274327,1.102390,-9.530089,4.552925,-1.698853,3.360617,1.954787,-1.005845,-4.321410,-2.749338,6.625259,-6.342560,3.825158,-1.992094,5.996903,-7.073201,-8.642234,5.298007,5.955757,-9.674026,-4.727915,4.186498,0.057137,6.274249,5.288007,-2.167730,-5.440835,4.483606,6.153690,-3.916887,3.076264,-4.643218,-9.329987,-7.476239,2.745175,-3.715084,3.143453,3.896224,4.790200,-0.513533,-7.033757,-4.851490,7.831513,-8.468410,7.558361,3.003295,-8.342562,-5.692428,-8.990005,-6.768121,7.741776,6.682926,1.016192,4.353776,-4.248013,7.188222,-5.735694,0.995306,3.788915,5.575106,-9.146038,1.784247,-8.729377,3.633469,-6.026531,-2.338324,-6.914460,-8.847742,6.009876,0.758768,-2.723217,-5.019013,-3.066583,-5.684256,-1.239529,-9.095113,5.733201,9.009496,0.182272,-2.407504,-5.791266,-4.948009,-2.507199,-8.696165,-0.857570,7.112471,-6.323442,-6.544233,0.361364,-4.603986,-9.688004,-1.651202,-8.079219,6.015612,1.839345,-3.323739,6.260954,-1.334237,9.383424,1.957208,-6.990745,-7.112730,-1.100309,3.951862,-6.448926,6.724191,-3.390271,-1.435354,2.816563,5.566791,6.817346,3.890888,-3.635473,-2.613385,-9.241595,4.218071,7.064767,-0.024229,-7.744019,0.873945,5.607017,5.768076,9.740762,8.768223,-5.279205,2.881446,-5.834729,-2.321121,-9.914326,-7.312015,-5.402993,-4.176929,-7.418778,3.229949,-3.826665,6.113065,-3.241277,-4.670195,-4.722978,-4.015063,-7.094229,-2.914959,-4.344901,6.930876,4.199619,-6.385310,3.436651,7.936707,9.820699,4.140816,-0.615442,9.316816,0.068422,-0.780498,9.468585,-2.664472,-6.856435,-4.288578,6.334502,1.021738,-9.470322,-2.373370,-9.739225,0.574872,8.148736,-7.526557,2.165823,-2.497022,1.149268,-1.522905,5.380001,-1.627676,5.314935,9.953156,-2.209701,6.006629,-4.805927,-2.854694,-0.224951,-2.421425,-3.902122,7.476040,-8.884418,8.423184,-8.816687,5.917864,-7.491129,3.662785,-4.548752,4.199195,9.157703,7.078521,-6.631452,0.187453,2.644471,-1.141946,-6.863460,3.487856,0.669688,-4.502303,-3.469224,-1.241559,4.232756,-7.413088,-1.919435,-6.625831,4.912933,5.636309,8.325593,-2.234102,-3.581020,4.638928,-5.541385,5.623557,3.915921,8.820205,1.712747,-8.099445,2.530207,1.721005,-3.803541,2.080799,0.722519,-3.751872,6.352795,-5.551767,2.564340,-4.476708,-9.599867,-6.988584,2.738946,-1.009025,1.557801,8.164596,3.435332,-4.688428,-9.284805,0.510033,-7.347017,7.130003,-1.603713,7.103885,1.044793,7.505164,7.024058,5.151899,4.315224,-0.040802,-2.781716,3.633590,-9.756253,-1.953899,-5.404525,-6.168829,4.808210,-4.560053,8.839511,3.900694,-3.722955,8.724819,-1.988035,-8.553269,-7.310432,-4.626395,2.067574,-4.633873,5.305102,-8.004891,2.043822,-6.513623,-5.757719,-0.330508,-6.032059,-8.594912,6.711286,6.574455,-1.987608,2.054822,-7.944540,-9.175790,-7.062222,2.815616,8.536810,9.258116,-4.835761,2.179945,-0.289723,0.549145,8.171881,2.201086,9.881226,4.522964,8.418961,-4.869941,-8.080586,6.335147,3.482460,0.597249,-1.481237,5.253077,-4.287045,-5.477367,5.567063,-5.228238,6.282684,9.729030,-9.095845,0.510219,2.330139,7.593368,-3.365476,-2.637171,1.036262,-8.676615,-3.450117,-3.188576,-8.467197,-6.076170,-4.170286,-4.603734,-3.143614,-3.481538,-6.979916,-0.019811,8.111889,-8.947560,-0.923975,-9.310008,-8.014018,-7.500574,-1.417374,5.946252,1.157072,-8.916162,-0.601489,4.716155,-2.356051,3.978882,3.155058,0.690948,1.976980,-5.458445,-5.631948,2.283215,4.643817,-4.830584,3.581692,-5.009410,6.854204,-3.899114,-3.952905,-6.405999,-0.598866,8.628655,-4.113708,-5.927720,-7.280879,5.971080,3.812184,8.467714,-0.989210,5.696124,-5.673854,-3.925555,-5.609174,6.604949,2.023708,-7.905157,-8.037864,4.222319,-0.967180,-8.359694,6.362060,5.968541,6.951482,6.633540,-9.255548,9.592463,4.153592,-4.496815,-3.029793,-9.659281,-8.147543,6.793413,-6.780889,6.676938,2.502519,-9.700019,1.921853,2.952493,-7.148686,9.167185,7.373425,6.411701,-5.099002,8.243587,-9.460629,-7.556025,-9.645030,2.930840,3.556332,8.265992,-4.761496,2.354210,9.483700,-4.784095,4.227846,2.710531,-0.488220,4.399645,-7.660098,-4.389999,-1.647808,5.990140,-9.651122,-3.155095,8.709853,-8.370121,9.769544,-9.286419,7.822552,-4.067742,-4.780507,5.834738,9.536121,3.068071,9.185422,-6.155663,3.051470,-8.680146,-7.260819,0.937605,-8.164434,0.955996,8.880890,9.095043,0.736495,2.296195,3.986005,-2.645055,-1.434026,-2.163288,8.781866,8.506717,0.451653,6.514413,-2.236323,7.141186,-0.110068,-8.258746,-4.291349,-1.482934,-7.645221,8.244192,8.087473,-6.090251,-9.512855,8.734074,7.684578,-6.109934,3.125657,-7.262956,-6.635610,-8.508055,-9.168979,-5.002235,-7.900836,-5.817362,-3.498440,-4.497069,-8.038182,2.294606,-4.316098,-1.605892,-9.103233,-6.710843,-2.938558,9.354825,-0.386671,-4.761157,4.272627,-4.920635,9.220890,-2.433163,-3.205800,2.826709,5.114797,1.036926,-0.342348,6.881263,-2.011183,-7.989957,-0.993906,8.912810,3.630080,8.180103,-8.075692,9.137596,3.457813,-0.578076,-2.742316,-2.847313,-7.671102,5.341437,6.381288,3.157901,-1.723224,6.562818,-0.332516,-1.122425,-9.511409,-2.677778,8.344920,-1.892150,3.390107,-0.675510,8.601000,5.859820,8.223311,-6.942407,2.016158,-9.177514,7.807095,-1.579461,2.716649,7.735941,-3.971350,-3.032620,2.083648,-6.661325,5.624210,4.976038,5.036282,7.504211,9.067067,-5.601659,7.009918,3.974821,-1.830579,-0.116256,-4.582355,1.817775,1.016724,-7.689847,-9.211296,3.701302,0.574386,-7.537684,1.395049,8.793953,7.233521,5.614577,7.218979,5.503557,-9.339329,6.124796,-2.281114,-3.316245,-8.513394,-5.099582,4.009605,5.628346,-9.871506,-6.186121,5.900405,8.390144,0.217580,8.892777,8.146746,-9.768157,5.939794,-4.086369,-2.785319,3.552547,4.200715,2.079279,-9.821215,4.479881,9.997344,-0.889408,-9.024536,1.040530,3.760546,-2.669716,-7.752424,-1.424909,-5.145416,9.641264,2.994987,8.366947,-4.675003,-8.989129,6.850173,-2.248796,4.801911,4.245034,-9.467391,9.110052,-8.053480,-1.561425,-1.258197,-4.448457,5.532366,0.599665,-6.326338,5.254118,5.548389,1.718179,7.399984,2.631081,8.950338,-1.610379,-8.752541,8.829486,7.877673,3.717722,-6.814853,-2.057715,5.026148,9.910442,6.975648,-0.144547,-1.981665,0.606907,8.874245,-4.323706,-3.478896,-7.488760,-4.035757,9.994764,7.135404,0.822526,-3.087498,2.069124,9.978693,8.769025,5.085168,2.380472,-3.894846,-6.945501,-8.784030,-8.955573,7.883625,7.487680,-5.424736,-1.592776,1.367007,4.558458,8.986304,2.269088,2.849818,6.210657,-2.655715,-3.898017,-6.042565,5.750247,6.592953,5.254674,-4.208502,-5.513347,8.139236,5.486833,-0.194801,-8.894888,9.973823,-9.648399,-8.382887,-3.060603,0.324575,3.443759,2.470997,-9.973726,-7.409194,5.723191,-8.664816,6.977391,-4.942151,-4.447143,-1.219245,6.162917,-1.145367,-7.734539,3.618530,4.603073,-3.069407,-9.563675,7.963981,-9.403626,-0.478686,6.615995,-5.340723,-0.275290,0.162132,7.710145,8.321399,4.814885,0.240067,9.975791,-9.358329,5.444021,2.267815], dtype = "float32")#candidate|3799|(750,)|const|float32
var_3800 = relay.var("var_3800", dtype = "int16", shape = (15, 9))#candidate|3800|(15, 9)|var|int16
const_3801 = relay.const([-9,-2,8,8,1,-10,-2,6,-3,-10,-10,-8,-8,9,2,7,-9,-8,4,-8,-7,5,-7,7,-3,6,1,-8,-3,-10,-7,8,-7,-4,-10,10,-1,7,8,-7,3,4,7,5,-9,7,-2,-3,-1,4,9,1,10,7,-3,9,-10,-10,-5,9,9,-1,10,4,10,5,3,-1,-5,9,5,-6,10,-3,2,-8,-7,4,4,-3,7,6,-5,10,-5,9,-8,-4,2,3,9,-5,-10,-6,-6,-1,-6,-2,5,-2,-3,-10,-6,9,-2,-2,-4,9,-5,-10,-3,-5,-9,-1,-8,-5,-2,4,-9,-7,-5,-4,-5,3,-10,-2,-6,-2,-3,1,6,2,1,7,9,3,-1,3,1,-6,8,2,5,1,8,9,8,-3,7,10,-4,-10,-9,-2,8,9,-8,-2,-8,-8,6,10,9,2,-3,-4,5,-3,6,5,3,-1,-7,-3,7,1,9,7,7,5,-4,-9,2,3,7,-3,-2,-1,-7,-3,-6,-8,-6,-4,-6,2,-6,9,3,6,-10,10,3,-10,-8,7,-5,-10,1,3,2,7,6,-8,10,9,-4,1,-2,10,-1,-5,-1,9,-10,-1,-8,4,6,5,5,5,4,-9,-4,8,5,6,-10,-7,-7,-7,-9,-3,1,1,3,-9,10,5,6,-1,-9,-6,2,-1,4,-6,-9,5,6,-9,-2,7,-6,-7,-6,-1,7,-3,-3,-8,2,-7,2,10,10,8,-8,3,5,-4,8,5,-5,4,1,-2,-5,-6,2,6,5,-1,7,7,-4,5,6,-9,6,-10,5,-4,2,-9,5,-4,7,5,1,-8,-1,-1,2,-2,5,-9,-4,3,2,8,-5,-8,-2,-8,3,2,-10,-4,4,3,6,8,-7,-5,2,4,8,2,5,4,6,5,-10,-8,-3,-2,5,8,-2,8,-6,1,-6,-7,1,-2,-9,4,-4,-2,5,7,-5,-3,7,10,8,1,-4,-7,-10,-3,6,6,2,-8,-3,1,9,6,-7,-1,-6,9,9,-5,4,7,7,-1,-3,-8,-1,8,-2,8,-9,-2,-1,6,-6,-10,1,2,1,9,-2,2,-5,-3,-5,6,-10,-8,1,5,-5,10,10,-3,7,7,-8,-3,9,2,9,-7,-10,1,9,1,-9,-9,4,2,-6,3,7,-1,-3,2,2,-10,4,-4,-7,6,-5,-9,-9,-4,-9,10,-2,4,-3,5,4,8,9,1,-8,-6,-2,-3,5,5,-4,-9,4,-2,-8,2,4,-1,3,-9,-9,-3,-9,1,6,7,10,8,9,-1,-7,-10,7,4,-5,3,7,6,-4,9,4,-2,1,-8,-10,-9,6,-7,-3,2,-3,2,1,-7,5,-7,-3,-1,10,7,10,6,5,8,-4,6,5,9,-5,3,4,7,10,2,-9,10,4,7,1,9,-6,-7,4,5,4,-7,9,-4,4,-8,6,4,8,-1,-5,-6,-9,9,1,-1,3,1,-4,10,-2,8,-8,8,-4,-7,-1,-9,8,-4,-4,-3,-2,9,-1,3,9,9,-4,5,6,-6,-5,-7,-2,1,5,5,10,5,-4,3,10,1,1,-3,-6,-3,-5,-5,3,-5,1,8,-5,-3,1,-2,-9,6,-9,-4,7,9,2,-1,9,3,-7,3,4,-10,-1,-6,5,8,-1,10,-4,2,-2,-10,10,-3,6,8,2,-7,-2,1,6,-3,6,7,-2,-5,-3,-7,8,-9,-6,4,-6,-8,5,6,-1,-8,-2,-6,-5,1,5,10,-8,8,7,1,-5,2,2], dtype = "int16")#candidate|3801|(675,)|const|int16
const_3802 = relay.const([-5.271835,5.438318,1.437937,-5.363022,-0.739496,-4.892843,5.985944,4.601103,3.820135,8.824237,6.561543,-9.708194,1.092904,0.469182,-6.955113,-9.869647,-9.923945,8.211437,-5.318399,7.214957,9.130841,-7.691347,8.755284,1.102680,-1.967922,-1.818413,-6.511712,5.635883,-2.818610,-7.654023,7.365903,6.379848,-5.426571,2.490266,-4.939827,-2.534839,2.430058,-6.109123,-3.368335,6.679173,-3.714087,-2.258034,-7.554995,5.250988,-7.900547,7.190266,-6.368432,-2.784226,9.758463,-2.463743,-0.249688,-9.547632,2.378413,-3.011702,-6.784377,-6.860060,7.478178,0.722222,1.600650,-6.798263,7.987573,0.049115,-6.785761,-9.362131,6.899371,-4.553012,4.245856,7.799934,2.217201,-3.392127,-6.686902,3.951325,-3.573287,9.944487,5.857892,2.888482,-2.441609,-8.189712,-3.871588,-8.714826,5.483772,1.859119,8.789482,-3.569262,-1.449455,4.620516,9.603788,-5.216511,1.432586,1.478664,9.161579,8.108051,9.153214,8.717554,1.191193,-5.910663,-2.353464,1.977298,-1.413334,-5.303879,2.766246,5.278985,-8.707639,-0.881540,-7.972380,-3.572191,-1.609512,8.705838,-1.557685,-7.176054,-6.981607,-5.367855,-1.170815,9.056491,0.999211,-4.212978,6.926748,-5.001206,1.958370,6.086619,-0.637202,-5.266270,-6.024884,5.809019,-5.988007,-9.848975,-7.729701,1.588729,-1.482148,3.805382,-4.813114,-6.839661,-7.319121,-9.706771,8.044269,4.663423,8.288069,9.662245,0.485277,-7.205348,-2.260240,-3.282081,-3.056792,4.572645,-6.530006,-7.680000,-7.123049,-8.821703,7.195268,4.482810,5.842477,1.859609,-0.862705,-9.872023,1.725074,9.074980,1.440513,-7.206764,1.206601,-9.594095,-6.240712,-0.725507,-8.458616,6.403939,7.131845,-3.028097,5.665786,-5.680706,-6.858958,1.706380,8.258455,3.144761,4.564866,-8.551130,-9.866224,-0.538752,-7.561827,3.479746,-1.456245,-3.696665,8.547607,-9.293395,-6.501784,-4.462801,5.779290,-8.349332,-4.108926,1.601603,9.508265,-3.336788,-4.635655,6.901668,-7.306466,7.168281,9.893030,-3.977969,1.225562,-7.647155,5.075126,-6.675567,-8.336771,-8.528743,0.709223,-9.699047,3.814603,-3.226599,-7.301196,-9.674332,-4.834610,9.029807,-4.081407,6.717184,-8.726327,1.374900,-5.216297,-3.115699,3.973185,-8.276925,-2.062269,1.910411,8.508562,9.587698,9.844996,-7.550891,-6.477559,-2.705620,-1.112111,-6.112686,1.795949,-0.268642,8.616022,-3.348563,7.043841,8.712655,-6.134339,-8.107008,-4.514875,0.696564,2.804787,-7.060126,6.489718,-4.498495,-0.885379,-8.455704,0.633730,0.809356,7.240964,1.471183,-8.708518,-0.334341,0.062752,8.002743,-3.531804,-7.739774,-1.325786,8.828683,9.732841,5.720000,-8.162691,6.034453,9.485695,4.096111,-9.421482,9.379402,5.563530,9.680669,-2.280021,8.020337,6.205623,1.013280,-5.877095,0.068321,-5.134090,2.454208,-8.986582,-9.008713,1.180865,-1.429997,-7.097444,3.998123,1.022152,6.631156,5.979919,5.070157,-0.616973,-2.420955,6.039294,-6.933608,6.640286,6.661464,-2.685727,8.986018,5.353898,4.566473,3.154031,2.082799,-0.693902,9.829329,7.618596,-4.026125,8.677354,-2.253140,6.956414,-8.138381,-1.769941,-0.064940,-2.509356,1.426026,-5.278894,0.122423,9.476231,-4.585799,6.113059,4.202300,-7.855935,-9.132331,-0.355548,9.236068,9.469398,-3.926877,6.019361,-6.851494,-6.231081,3.568332,6.233740,2.993172,9.415659,-9.746407,3.530808,-6.449222,3.632461,4.383594,2.700438,2.391197,-2.858153,5.438564], dtype = "float32")#candidate|3802|(336,)|const|float32
call_3798 = relay.TupleGetItem(func_3234_call(relay.reshape(const_3799.astype('float32'), [10, 5, 15]), relay.reshape(var_3800.astype('int16'), [15, 9]), relay.reshape(const_3801.astype('int16'), [675,]), relay.reshape(const_3802.astype('float32'), [336,]), ), 8)
call_3803 = relay.TupleGetItem(func_3239_call(relay.reshape(const_3799.astype('float32'), [10, 5, 15]), relay.reshape(var_3800.astype('int16'), [15, 9]), relay.reshape(const_3801.astype('int16'), [675,]), relay.reshape(const_3802.astype('float32'), [336,]), ), 8)
func_2633_call = mod.get_global_var('func_2633')
func_2638_call = mutated_mod.get_global_var('func_2638')
const_3809 = relay.const([10,9,-3,9,-1,3,8,7,8,-9,3,-5,-3,5,-7,-1,-2,10,1,1,4,1,4,1,9,8,-4,-3,8,-3,10,-4,8,10,-3,-1,-5,-10,-4,10,-3,-7,1,-3,8,4,4,10,3,-1,-3,7,9,-6,10,-6,4,9,-3,-4,10,9,-9,-4,-1,3,9,1,-7,1,-10,-2,2,2,6,6,-8,-8,4,-1,8,8,-4,-5,5,-2,-5,-1,-6,2,-3,-7,-5,-9,-8,-5,-4,4,-1,3,-7,3,9,-8,-9,8,1,2,-10,-7,1,3,-5,7,7,4,-5,5,10,-1,-4,-8,2,-10,-1,1,9,9,-2,-1,-6,-3,3,7,9,-2,-6,-7,2,-3,6,-7,7,-10,4,-7,8,1,6,-5,-5,8,-7,10,-4,-4,-6,-5,9,-1,7,-3,-6,6,-2,8,8,-9,-3,-6,-3,-5,-3,9,6,-5,7,-7,2,-6,-4,4,-10,-9,-3,8,-5,-2,-7,-10,-4,-5,-3,-4,6,9,-4,-4,-5,5,-7,-3,-10,-5,-9,-10,-10,-2,7,-9,-5,5,-1,-4,-3,6,6,6,-8,4,6,10,9,10,-9,-1,7,-6,6,-7,-10,8,-4,-3,5,-10,1,8,2,-6,-7,9,-2,2,-6,-4,4,4,8,10,5,6,-10,6,10,-6,6,1,-10,-3,-4,3,-10,-7,4,-4,7,-7,-2,-10,-4,1,2,7,7,-6,-10,8,-8,10,2,3,4,8,-2,10,7,-5,3,8,-3,-10,7,-4,-3,-7,8,6,-1,-8,5,8,-1,-8,6,-6,-4,3,-4,-6,-1,4,6,-1,-4,-1,-9,10,3,-6,-8,9,9,-5,1,2,6,-9,-7,7], dtype = "uint8")#candidate|3809|(330,)|const|uint8
var_3810 = relay.var("var_3810", dtype = "uint32", shape = ())#candidate|3810|()|var|uint32
call_3808 = relay.TupleGetItem(func_2633_call(relay.reshape(const_3809.astype('uint8'), [6, 11, 5]), relay.reshape(const_3802.astype('float32'), [336,]), relay.reshape(var_3810.astype('uint32'), []), ), 7)
call_3811 = relay.TupleGetItem(func_2638_call(relay.reshape(const_3809.astype('uint8'), [6, 11, 5]), relay.reshape(const_3802.astype('float32'), [336,]), relay.reshape(var_3810.astype('uint32'), []), ), 7)
func_597_call = mod.get_global_var('func_597')
func_602_call = mutated_mod.get_global_var('func_602')
const_3824 = relay.const([-5,4,-4,7,9,7,-5,7,-3,6,-1,-7,6,-4,9,3,-6,-2,-10,-2,-8,8,3,-9,-2,-6,-7,-3,6,-4,-5,-3,-3,-3,-5,1,3,-7,7,-5,-10,1,5,2,1,8,-2,9,3,-8,7,2,-1,8,-6,6,-3,-3,10,10,1,7,7,1,-8,-10,10,-8,-2,8,9,-2,-10,-1,-10,10,-6,-5,5,-5,-6,-1,-7,-5,5,-7,-9,7,5,10,8,7,8,-7,9,-7,6,-9,-5,2,-10,-6,-7,8,2,7,7,4,-5,8,4,7,3,1,-2,10,1,1,-1,-1,-5,5,-2,7,1,-9,3,4,-4,4,9,8,-1,9,-7,7,1,-6,-2,-10,10,-7,-7,-9,-8,-5,-8,-7,3,3,8,-4,3,-2,4,-7,1,-9,6,7,2,1,6,-9,3,9,-1,2,4,8,-6,-6,10,5,-5,10,-8,-5,8,-5,7,4,-8,3,-2,4,7,-5,5,-3,-6,-8,-5,-9,9,5,10,4,-8,2,8,-6,-5,-2,-4,-3,-9,5,5,6,-9,-10,10,9,-2,8,8,-7,-8,5,5,10,-8,9,-8,7,-7,6,-4,-7,-5,-6,-10,6,-3,8,7,-5,3,-8,10,8,-6,-7,9,-5,-1,-7,-8,-7,-2,-1,4,-5,10,8,3,-7,2,7,10,-6,-7,-9,6,3,4,-8,-10,5,-10,-9,-1,-2,-4,4,3,2,5,-2,-1,8,1,-4,-8,-2,-6,-1,-1,1,4,-7,7,6,5,10,6,-1,-3,1,-8,2,-4,-10,-8,10,6,8,1,3,5,-1,-1,-10,-9,-8,4,10,4,4,-9,-3,-4,-6,8,-8,-5,4,3,-2,6,1,1,7,9,7,-6,3,-3,2,2,-4,10,3,-5,8,-7,9,-10,3,-8,9,1,1,-5,-5,4,2,-1,-9,-1,8,-6,6,-3,-5,-9,4,-8,-4,-9,-8,10,9,6,-8,5,-7,-4,6,3,-8,-4,10,7,-5,-3,-1,2,6,10,-6,-1,7,-5,-3,-4,1,-3,-2,-5,9,7,-2,-2,8,4,8,-5,9,9,10,-2,1,-2,-8,-9,8,6,6,8,-9,-8,-8,-5,-4,-8,8,-5,-7,-4,-5,-1,1,-3,-5,-3,-5,-5,-5,-9,-5,-3,-9,3,-5,-1,10,-5,9,-9,1,1,4,-7,4,-6,-3,1,-9,-9,1,-7,4,-3,-10,-7,6,-4,-4,9,-7,9,6,-3,4,1,10,8,10,6,6,2,3,-4,9,7,10,7,7,3,9,-9,-2,4,-10,3,-6,-8,10,-8,-5,6,-2,-3,2,2,-8,2,-10,3,7,-6,10,1,-5,-1,-3,-8,-2,2,5,-5,7,-4,-4,-4,2,3,3,-1,1,1,-9,-9,-7,4,6,-6,9,-7,8,3,3,-1,-7,7,4,-4,-4,-3,5,-5,-9,2,-5,-10,-2,3,6,-4,-6,-3,-8,3,-1,4,-6,-6,4,-2,9,-3,4,8,10,4,-4,6,7,5,6,3,2,6,9,4,1,-9,-3,-6,1,-9,-1,9,4,8,-5,9,-2,3,4,-7,7,1,-7,5,1,4,-10,-9,-7,2,8,1,-8,-1,-4,-7,-6,-2,-7,2,-4,-9,-9,9,-5,-10,-4,-3,5,-5,4,-1,10,5,2,-3,-2,-1,1,9,-10,-9,1,-7,7,5,-3,4,-2,9,4,10,-4,-1,10,-1,10,-7,5,5,-7,5,-1,-3,6,8,-6,8,-1,7,8,4,-9,8,6,-7,-8,-4,9,-1,-9,-5,-7,-5,3,-8,9,10,2,3,1,-2,10,7,3,-4,-5,5,5,10,1,8,1,-9,6,-4,2,8,-2,-3,5,7,-8,3,4,1,3,-5,-9,-9,8,6,9,-6,-10,-6,-8,-4,5,2,-1,5,4,8,8,-8,1,8,9,1,-5,-4,-9,-1,-8,-6,-6,4,-2,-3,2,-9,-7,-4,-3,6,1,-2,10,9,-6,6,-7,-4,-5,-9,8,1,-7,2,10,-7,-9,3,2,-7,6,-2,4,-2,-3,-5,1,8,10,9,9,-1,4,-6,-6,7,-6,7,-7,10,-3,2,-2,-3,10,2,-7,8,7,-10,-8,-8,-9,6,-5,-5,3,4,6,8,9,-7,-3,10,10,-2,8,-5,-5,3,9,-10,-3,-10,2,-9,9,7,-3,-1,-6,3,5,1,3,1,9,-6,6,5,7,-6,10,-8,8,-7,-6,-8,-2,-2,2,7,-7,-6,-3,10,5,-4,-7,9,6,2,10,-3,-7,-9,2,-2,1,3,-9,1,7,10,-10,3,-8,-7,3,3,9,-10,-8,-10,-10,-2,-4,-2,10,6,2,-7,-4,-9,6,-8,-3,-6,1,-9,-10,8,6,6,-4,8,-4,8,-1,5,-10,2,1,4,5,1,-8,1,2,2,4,4,6,7,1,-5,-5,4,-5,6,-4,9,-9,-8,10,7,-9,-3,4,-10,-4,-4,2,-2,8,10,8,-4,10,8,-1,5,7,-4,-1,-8,9,-1,1,9,5,9,-9,-10,6,-10,-4,-6,-4,-4,5,10,-3,7,6,3,-7,5,-7,4,3,-4,-10,8,3,1,-5,1,1,1,-6,-7,7,9,-6,-1,9,-6,6,-3,7,6,-4,-9,7,-10,-6,-5,10,-9,9,7,-7,-6,-8,-3,-2,6,-8,-1,-5,-7,10,6,-8,-8,6,4,8,-6,9,-1,8,9,2,-10,-10,10,3,-2,10,7,-5,9,10,-10,-7,-10,-10,-1,-8,1,-10,-2,6,3,1,-2,-2,10,8,-9,-2,-10,-9,-7,3,-6,9,-7,9,-9,-1,-9,-1,3,10,4,2,-6,-6,7,-1,4,1,4,-3,-4,-3,-5,3,-4,9,-7,-4,1,6,-3,3,6,1,7,1,6,6,10,9,-2,-4,1,-2,1,-4,-4,4,-2,7,8,-3,-6,8,-8,-2,7,-1,-7,3,-10,2,4,3,-10,-7,10,5,-1,-2,9,-1,-1,5,5,5,6,9,-5,10,-3,-6,-7,9,-3,8,4,-8,-2,-2,-2,-4,4,10,6,-5,-7,1,3,3,-2,7,10,2,8,-1,-1,-1,-10,6,-1,6,3,3,9,9,-8,-9,2,2,-5,10,-10,5,-2,-8,2,-2,-1,-1,2,2,-8,10,-4,10,5,-7,9,-5,-5,-5,-6,3,3,-10,6,6,-4,-6,7,8,-3,7,9,4,-4,2,-5,7,-9,-4,-8,-10,5,1,-1,-5,3,10,-3,-7,-5,-7,4,-10,-3,-9,-3,3,7,3,2,4,-10,-9,-9,10,-3,-4,-4,-9,9,8,-9,3,7,-5,3,-4,4,-6,10,-6,-4,2,-7,3,-9,9,1,5,7,7,-9,-1,-8,5,2,1,-4,-3,3,6,-6,3,8,-7,10,-4,-9,-4,-3,-3,10,10,8,-6,9,7,8,3,8,10,-6,-8,9,-9,1,-7,7,-7,-1,8,-7,-5,4,3,-10,9,7,-8,-9,1,9,1,7,3,-10,-10,-5,-4,-5,-1,7,-8,9,-3,4,-8,-1,-1,6,-8,4,-7,-3,9,5,-2,2,-9,7,-9,5,6,-6,-4,-10,3,10,-6,-9,10,7,-8,-3,9,-10,-3,-6,1,-7,-8,-9,4,1,2,-4,-5,4,9,-2,-9,9,-7,2,-8,-7,7,-7,5,10,-9,-10,9,-10,5,-9,6,8,-4,5,1,-10,8,-9,5,-10,8,-9,-8,-5,2,-7,1,-6,-6,-7,-3,-5,-4,3,6,4,-5,-10,5,-6,-9,-7,-10,3,4,-5,7,-5,4,10,1,-5,8,-9,-1,2,-2,10,2,8,-5,2,-2,-1,-4,8,5,-2,-9,10,8,1,10,1,-9,9,-1,4,-7,2,5,9,-3,7,-1,-3,-6,10,10,-10,-2,10,2,-9,-10,2,-10,7,9,-7,-8,3,7,-2,7,-7,-2,4,-3,-3,-3,8,4,-9,7,5,-6,-9,-4,-1,2,-9,7,8,-6,10,-4,5,2,-2,9,4,8,8,6,-4,-9,5,-8,-3,4,6,-4,7,-4,-6,-6,8,-6,5,-8,-2,-4,3,2,6,1,-3,2,2,-6,-1,-1,-8,5,-10,-4,2,-1,-8,10,6,-6,8,-10,-4,-1,1,-3,-8,2,-5,-2,4,1,4,-6,5,-3,9,-3,10,-7,-5,-1,3,1,-10,5,6,-8,7,3,5,5,9,-7,2,-1,-6,-10,-6,9,5,9,-1,-2,-10,-2,-10,9,5,-8,1,5,-2,8,-7,-3,4,2,1,-4,8,8,-3,7,4,-8,-5,-4,-10,-4,-3,1,-8,-1,-6,2,2,-2,-6,6,4,-6,-9,-7,-5,7,-9,3,1,8,2,-3,-9,-3,6,6,-3,3,5,2,3,7,-8,-1,8,-8,9,-7,6,3,9,-4,-2,-6,-6,-6], dtype = "uint32")#candidate|3824|(1694,)|const|uint32
var_3825 = relay.var("var_3825", dtype = "int32", shape = (21, 5))#candidate|3825|(21, 5)|var|int32
call_3823 = relay.TupleGetItem(func_597_call(relay.reshape(var_3810.astype('uint32'), []), relay.reshape(const_3824.astype('uint32'), [11, 11, 14]), relay.reshape(var_3825.astype('int32'), [105,]), ), 0)
call_3826 = relay.TupleGetItem(func_602_call(relay.reshape(var_3810.astype('uint32'), []), relay.reshape(const_3824.astype('uint32'), [11, 11, 14]), relay.reshape(var_3825.astype('int32'), [105,]), ), 0)
uop_3827 = relay.atanh(const_3799.astype('float64')) # shape=(750,)
func_2679_call = mod.get_global_var('func_2679')
func_2684_call = mutated_mod.get_global_var('func_2684')
const_3835 = relay.const([[-9,-8],[1,-9],[7,8],[-6,-8],[7,1],[-8,3],[6,-8],[-10,-6],[7,-3],[3,9],[-5,6],[3,8],[3,-8],[-6,3],[-6,2],[7,-6],[-4,-3],[2,7],[-9,1],[-6,-6],[10,10],[-2,9],[-3,-6],[3,-3],[5,-3],[9,6],[-4,2],[6,1],[-9,-6],[-3,10],[8,-4],[-10,-5],[6,3],[2,1],[-6,8],[-10,-2],[9,1],[10,7],[7,-6],[-10,-3],[-3,-10],[-6,2],[6,4],[8,-7],[1,-8],[9,-1],[-9,-5],[-2,-7],[-7,-1],[-10,4],[3,-3],[3,8],[8,-9],[3,3],[-8,3],[9,6],[-7,-8],[10,-6],[-10,-3],[-1,-1],[9,7],[-9,-6],[-1,7],[-8,-7],[-10,3],[-8,4],[-10,-3],[8,-1],[3,2],[8,-8],[-8,-10],[-10,3],[-3,1],[-7,-9],[1,-9],[7,9],[6,1],[9,3],[-6,4],[-10,-7],[5,-4],[4,1],[-9,-8],[8,6],[7,8],[-9,-5],[-3,-3],[8,-6],[10,9],[-5,-1],[1,-9],[-5,5],[-4,-1],[-5,8],[-7,-9],[-2,10],[-4,6],[-1,2],[-6,-3],[7,6]], dtype = "int64")#candidate|3835|(100, 2)|const|int64
var_3836 = relay.var("var_3836", dtype = "float32", shape = (495,))#candidate|3836|(495,)|var|float32
call_3834 = relay.TupleGetItem(func_2679_call(relay.reshape(const_3835.astype('int64'), [4, 10, 5]), relay.reshape(const_3835.astype('int64'), [4, 10, 5]), relay.reshape(var_3825.astype('int32'), [105,]), relay.reshape(var_3836.astype('float32'), [495,]), ), 2)
call_3837 = relay.TupleGetItem(func_2684_call(relay.reshape(const_3835.astype('int64'), [4, 10, 5]), relay.reshape(const_3835.astype('int64'), [4, 10, 5]), relay.reshape(var_3825.astype('int32'), [105,]), relay.reshape(var_3836.astype('float32'), [495,]), ), 2)
func_200_call = mod.get_global_var('func_200')
func_203_call = mutated_mod.get_global_var('func_203')
call_3848 = func_200_call(relay.reshape(var_3825.astype('int32'), [1, 15, 7]), relay.reshape(var_3825.astype('int32'), [1, 15, 7]), )
call_3849 = func_200_call(relay.reshape(var_3825.astype('int32'), [1, 15, 7]), relay.reshape(var_3825.astype('int32'), [1, 15, 7]), )
output = relay.Tuple([bop_3794,call_3798,var_3800,const_3801,const_3802,call_3808,const_3809,var_3810,call_3823,const_3824,var_3825,uop_3827,call_3834,const_3835,var_3836,call_3848,])
output2 = relay.Tuple([bop_3794,call_3803,var_3800,const_3801,const_3802,call_3811,const_3809,var_3810,call_3826,const_3824,var_3825,uop_3827,call_3837,const_3835,var_3836,call_3849,])
func_3852 = relay.Function([var_3792,var_3793,var_3800,var_3810,var_3825,var_3836,], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
mutated_mod['func_3852'] = func_3852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3852_call = mutated_mod.get_global_var('func_3852')
var_3854 = relay.var("var_3854", dtype = "uint64", shape = (7, 15, 8))#candidate|3854|(7, 15, 8)|var|uint64
var_3855 = relay.var("var_3855", dtype = "uint64", shape = (7, 15, 8))#candidate|3855|(7, 15, 8)|var|uint64
var_3856 = relay.var("var_3856", dtype = "int16", shape = (15, 9))#candidate|3856|(15, 9)|var|int16
var_3857 = relay.var("var_3857", dtype = "uint32", shape = ())#candidate|3857|()|var|uint32
var_3858 = relay.var("var_3858", dtype = "int32", shape = (21, 5))#candidate|3858|(21, 5)|var|int32
var_3859 = relay.var("var_3859", dtype = "float32", shape = (495,))#candidate|3859|(495,)|var|float32
call_3853 = func_3852_call(var_3854,var_3855,var_3856,var_3857,var_3858,var_3859,)
output = call_3853
func_3860 = relay.Function([var_3854,var_3855,var_3856,var_3857,var_3858,var_3859,], output)
mutated_mod['func_3860'] = func_3860
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3995 = relay.const([[[8.545496,-8.165231,-0.126674,5.615841,2.424607,2.528221,9.975397,-6.651582,9.324852,-7.213737,6.264781,5.998615],[-1.277865,6.274593,-1.765357,-6.172364,7.913202,-7.466086,-3.768761,-6.738635,-1.798075,-2.933531,0.066136,-1.186936],[-1.717886,-9.302788,2.894474,-0.543331,-1.749530,2.413829,-3.714848,-4.093038,-2.319457,1.816970,-7.232997,6.818447],[1.645756,8.300783,-5.616796,-5.385902,-3.406031,6.677911,-0.123327,1.774218,0.272429,-1.171817,8.712141,0.916850],[9.842803,-8.525153,-6.869691,-1.835205,9.753471,5.942570,7.156519,-2.320107,-6.799665,-2.327212,1.196393,0.368785],[-9.399338,2.544743,-3.036178,0.225923,2.796279,-3.132234,5.652337,-7.125048,-4.528848,2.466324,3.017778,7.910515],[4.823231,-6.841894,0.140832,8.063075,6.670442,5.112287,4.061772,-6.395329,-4.535117,-9.701008,3.461399,-8.840736]]], dtype = "float64")#candidate|3995|(1, 7, 12)|const|float64
uop_3996 = relay.erf(const_3995.astype('float64')) # shape=(1, 7, 12)
func_3852_call = mod.get_global_var('func_3852')
func_3860_call = mutated_mod.get_global_var('func_3860')
const_3999 = relay.const([-7,10,-8,6,1,7,9,7,9,6,8,10,-7,8,-8,2,7,-3,-9,6,-2,-2,-6,-2,2,-2,-4,-8,1,-6,-6,-6,-10,-7,7,-9,-10,-1,7,-3,1,-1,-8,-7,4,7,2,2,4,1,7,-10,10,-3,-5,7,-2,3,7,10,-3,-1,2,-7,5,6,7,-8,9,5,10,2,-10,3,-6,9,1,4,-3,8,8,-1,1,-3,3,-4,10,6,-2,-9,5,8,6,-9,-3,-9,2,10,-9,6,3,-6,10,4,4,-2,1,-5,4,-8,-1,-1,-6,10,4,-7,8,1,-7,9,10,10,-3,-10,7,5,-4,-2,-7,-4,-10,9,4,7,-5,-3,-10,-8,-6,-10,-6,-2,1,-1,-8,-9,-7,8,8,-5,2,10,10,4,6,-10,9,3,8,8,8,-8,-8,8,-2,1,-10,-7,-8,-6,-5,7,10,5,3,-6,3,-5,2,8,-6,-9,9,7,-7,2,-3,7,8,-1,-7,1,3,-2,-1,1,7,-6,-6,-4,9,-6,-4,4,-4,2,-6,-1,8,5,4,-9,-4,9,-9,4,8,10,10,3,-1,-5,-5,7,2,5,6,6,10,-1,-8,-6,-4,8,10,-9,-4,7,3,-7,6,10,7,-3,1,7,-10,6,9,7,5,2,2,-1,3,-9,-9,2,-5,4,-10,7,-3,-3,7,2,6,9,3,-5,7,7,5,3,-6,-7,-7,-6,7,3,-9,-4,-8,5,5,10,-3,2,-8,-7,-4,-1,-9,3,6,10,10,-10,-8,-10,4,9,-8,-3,-7,-1,7,4,-8,-3,-1,-10,8,-9,-7,-3,10,-8,2,7,6,-10,9,-10,-9,3,-8,2,7,4,4,-6,-9,5,10,1,-9,8,3,6,2,3,-4,-8,8,-6,-1,-7,9,-2,-3,4,1,1,-9,-7,8,-3,-7,-5,4,7,6,-6,7,5,-10,-3,10,-9,1,-9,8,-3,-4,-9,-2,6,2,4,-3,-9,-7,-5,6,-5,2,6,-8,4,-7,-2,9,6,3,9,10,-8,10,-5,9,-3,-6,8,10,-7,5,6,9,-3,6,6,-2,3,8,-8,8,8,4,7,8,-3,-3,-6,2,5,-3,-4,-7,-7,-6,2,8,-5,5,-6,-6,-7,7,3,5,9,-1,1,1,1,-2,-1,-2,-5,-10,2,-2,-7,2,-10,10,-5,6,8,-5,-5,3,-9,2,-2,7,-10,-2,-7,1,-5,9,-1,-7,2,-10,-1,3,-10,6,-9,7,-9,8,-5,-5,9,10,9,-1,-1,10,-3,-4,7,-4,-4,-8,8,-10,5,3,9,6,-3,1,-5,8,3,9,-3,-6,4,1,-2,-6,6,10,5,5,2,-1,-6,-5,2,-9,-6,3,1,-3,5,-9,-9,8,7,-1,1,6,-1,-6,-4,8,-4,-2,-5,9,4,-10,-8,-4,-2,-6,7,10,-2,10,5,-9,-9,3,8,5,-1,3,-3,-6,4,-6,3,-10,4,4,8,-8,4,4,-5,-4,-1,-6,5,-9,-6,-1,-3,-6,1,-6,-3,9,-6,-1,-9,7,-1,-6,7,-9,-2,-1,-3,4,9,4,-6,9,-7,5,5,-8,7,7,1,6,-8,8,6,-5,4,6,6,4,-8,-9,-2,-1,1,2,4,5,7,-3,-7,-9,-2,3,-10,9,-7,-1,5,8,10,10,-10,-7,-10,3,1,-10,-6,-8,1,4,-8,-7,-9,-1,-4,4,-3,2,-1,3,-4,-2,-8,-7,-2,9,8,-2,-8,5,-3,-6,9,-2,-3,-2,-7,-9,7,-6,-9,-8,10,1,5,1,-4,-6,9,5,2,10,2,-6,9,7,-6,4,-4,-7,-2,7,-9,1,1,-9,3,-2,-3,3,8,-8,4,-4,9,-7,2,-7,7,1,5,-8,-1,3,-7,-4,8,-3,5,9,1,-5,10,-7,9,4,8,-2,2,-3,-4,6,-2,-2,-8,-1,9,-3,-7,7,-6,1,2,-3,9,-5,-4,2,-2,2,-7,9,10,-6,-2,-4,3,4,-9,2,-2,10,8,1,6,7,8,-1,10,3,10,10,-3,1,-1,9,-7,-1,-10,-2,6,10,-7,-2,8,-7,-5,2,-1,-9,5,8,-6,7,-1,-2,2,3,-5,-6,-10,-1,-2,-2,-7,7,-10,6,-4,-2,3,4,-8,-5,-1,5,-6,6,-1,-2,1,10,6,7,-8], dtype = "uint64")#candidate|3999|(840,)|const|uint64
const_4000 = relay.const([2,4,5,-1,1,-1,1,-1,-3,10,-9,-2,1,-1,1,-4,3,6,-5,-5,1,5,8,-2,4,6,7,8,-1,6,-5,8,10,6,-1,2,-6,5,-5,-6,10,-2,10,-2,-1,3,-1,-1,-5,8,9,7,9,9,8,4,-7,-3,-8,-6,-3,2,3,7,-2,1,5,9,9,-7,-3,-5,9,7,-2,4,-5,-1,4,6,3,9,7,-3,6,-3,2,1,-5,9,-3,-3,1,-7,-4,-1,10,6,-6,6,-8,10,9,1,10,-1,3,3,10,7,5,-10,7,-4,2,4,-1,1,-6,3,-10,-10,8,7,7,9,-3,7,-4,5,-3,5,-3,-5,9], dtype = "int16")#candidate|4000|(135,)|const|int16
var_4001 = relay.var("var_4001", dtype = "uint32", shape = ())#candidate|4001|()|var|uint32
var_4002 = relay.var("var_4002", dtype = "int32", shape = (105,))#candidate|4002|(105,)|var|int32
var_4003 = relay.var("var_4003", dtype = "float32", shape = (495, 1))#candidate|4003|(495, 1)|var|float32
call_3998 = relay.TupleGetItem(func_3852_call(relay.reshape(const_3999.astype('uint64'), [7, 15, 8]), relay.reshape(const_3999.astype('uint64'), [7, 15, 8]), relay.reshape(const_4000.astype('int16'), [15, 9]), relay.reshape(var_4001.astype('uint32'), []), relay.reshape(var_4002.astype('int32'), [21, 5]), relay.reshape(var_4003.astype('float32'), [495,]), ), 6)
call_4004 = relay.TupleGetItem(func_3860_call(relay.reshape(const_3999.astype('uint64'), [7, 15, 8]), relay.reshape(const_3999.astype('uint64'), [7, 15, 8]), relay.reshape(const_4000.astype('int16'), [15, 9]), relay.reshape(var_4001.astype('uint32'), []), relay.reshape(var_4002.astype('int32'), [21, 5]), relay.reshape(var_4003.astype('float32'), [495,]), ), 6)
func_2908_call = mod.get_global_var('func_2908')
func_2910_call = mutated_mod.get_global_var('func_2910')
var_4008 = relay.var("var_4008", dtype = "float64", shape = (195, 2))#candidate|4008|(195, 2)|var|float64
call_4007 = relay.TupleGetItem(func_2908_call(relay.reshape(var_4008.astype('float64'), [13, 15, 2])), 1)
call_4009 = relay.TupleGetItem(func_2910_call(relay.reshape(var_4008.astype('float64'), [13, 15, 2])), 1)
bop_4016 = relay.logical_xor(var_4008.astype('uint16'), var_4001.astype('uint16')) # shape=(195, 2)
func_3234_call = mod.get_global_var('func_3234')
func_3239_call = mutated_mod.get_global_var('func_3239')
const_4020 = relay.const([[3.352263,4.205096,-0.564361,-1.804391,-6.213719,9.784271,-2.751716,5.873919,-1.806753,1.939931,2.758381,6.513815,4.095001,-1.053748,3.017044,-5.554874,-9.264461,7.076218,-4.421379,-4.810464,1.495611,2.443009,-8.371074,4.195076,4.944223,0.714896,-1.855025,-4.089548,4.564573,2.617749,-9.596656,6.323354,5.254148,-6.328072,-2.649704,-6.872086,-7.441366,-6.548613,2.489553,6.800863,-6.173761,4.602147,2.864865,-9.357286,9.610344,6.070051,6.120700,-5.890146,-0.615433,6.727895,0.416360,-8.820760,3.942899,-4.778255,-3.276889,-0.544855,-4.040772,0.475875,8.593934,6.630457,5.401657,-9.182471,8.940375,5.893076,9.624249,6.973474,-6.255970,0.073528,-1.316448,-0.674296,3.331183,9.507365,4.065837,-2.048729,-5.622613],[4.143923,-3.956378,6.121171,-3.274707,0.986853,4.371669,5.712233,-9.477342,0.639317,-6.334259,3.858317,-6.263664,-5.236038,0.753520,-1.732823,-4.425392,1.125956,-3.425168,-1.404986,6.470961,-5.054527,-9.004750,8.742971,-0.625332,4.456011,-8.763517,6.209314,8.890315,-1.021409,-8.655054,5.329861,-3.792909,8.846806,8.606892,-7.161602,-5.518353,2.877302,-1.346331,9.223331,2.294096,3.689776,-4.901460,2.915080,-0.963418,-8.148517,-6.825849,4.940709,0.884596,5.488240,2.728419,7.846115,7.497060,-4.069497,2.171466,-4.644435,0.533236,2.602330,-5.065721,2.201374,-5.084370,0.988529,9.151806,-7.417090,-7.079987,7.680190,1.898876,9.140798,2.321005,-9.194426,9.626978,-0.106253,-0.672911,-6.299817,-8.315177,-3.799624],[-5.859070,4.125733,-5.712186,-7.599367,-4.145043,-9.709154,-4.341173,-1.410960,-4.505383,3.012802,5.021118,-3.334415,5.948950,4.681729,-2.480977,-4.524368,7.204969,6.771733,1.002700,-6.165320,9.642290,8.618203,-0.113886,-0.561551,-4.457266,7.170796,5.010036,-1.689371,-3.812384,-8.029497,0.308501,4.031984,-4.366091,-4.738732,-3.215528,8.054706,-1.112980,-8.895960,-5.658745,7.329499,-1.393167,4.328973,-9.984092,-0.928501,0.989133,1.350278,6.102063,4.985009,3.865845,-7.299361,7.748275,-0.888256,-3.835127,-9.258315,7.184656,-9.116036,-5.857317,5.754087,6.483615,-8.815484,-3.532660,7.712532,-9.658994,1.730501,-5.682507,-6.356598,-7.691543,3.370243,9.605648,7.443205,4.166689,-3.565726,6.053431,-6.940175,5.660331],[7.932597,6.793080,7.550179,-2.655743,5.857053,-8.358298,-3.279593,-3.338398,-9.512914,3.179002,-4.513168,5.944544,3.024728,-6.617843,3.957960,-0.354454,2.769303,6.018067,1.527574,-4.316115,-1.748332,-6.207076,9.596145,2.423402,-3.639937,9.640501,7.651051,4.256181,-4.916559,1.458973,5.518785,-9.602302,2.206406,-1.259487,7.080932,7.637606,1.270839,-6.807099,9.410007,-5.877729,4.170416,-0.506691,-8.652423,0.718578,-3.510763,-2.100554,-8.406112,-8.922843,-8.748127,-3.381143,8.644353,-9.098953,-3.185973,7.648781,-4.993298,1.038795,-1.945839,-0.134358,-5.236574,7.045500,-0.378306,-9.150206,-9.310745,-0.566174,1.146388,6.391019,0.163537,-5.364099,-4.366184,0.027650,9.099127,-0.198529,-0.838578,5.924632,-2.274746],[3.996933,-2.204317,5.624213,6.894925,-6.743573,0.523554,3.540180,7.715687,-9.619599,-0.638513,-2.001135,-4.033736,2.212233,8.190642,5.454116,7.973253,7.103391,8.983452,-6.758695,-5.057573,2.846820,-2.396066,-1.565410,-1.856125,-2.244097,-1.975541,6.588564,1.898729,-2.112712,9.663144,6.698611,-4.856566,-8.766911,9.485056,-6.041840,8.235923,4.442490,9.215425,2.410041,-5.077212,-3.758567,-1.903839,-7.975589,-7.099731,6.301924,-5.305440,-0.735191,4.241220,-8.421038,8.695814,-0.405924,0.783038,4.215720,-3.878361,-2.325619,-6.380060,3.480870,-2.015188,-5.525854,-3.026129,-7.720620,-0.759372,-2.652455,-8.898217,1.093625,2.769398,-3.165634,1.579447,2.330183,5.636175,0.390561,-7.860063,-3.537953,-9.436090,6.306143],[-1.644055,8.950344,-3.767251,-5.193921,3.120006,5.973647,-6.261977,0.449754,2.396878,4.773023,-9.869564,-4.604982,5.604079,-7.157762,0.658068,5.284597,9.993213,5.100813,-3.573902,-7.653336,0.998225,-6.797767,-2.391053,1.855948,5.735848,-4.063287,2.613987,-3.455328,7.157535,-3.154464,6.611185,2.309615,1.792139,-2.056695,-0.084630,6.773236,-1.300135,5.691931,1.354318,-8.097950,7.588855,-7.055096,4.599338,-0.532934,4.513651,-5.991451,-0.391164,-7.874313,-5.059350,0.111412,9.874494,-2.190363,-8.253617,-2.953835,-4.510306,-5.246861,1.986451,3.386183,-3.450114,-3.112880,-7.966584,-2.957402,-6.129405,-2.361280,6.963560,5.369856,-5.698879,6.549665,-1.011686,-3.276685,-6.382631,-5.983665,-9.573784,9.322474,7.398380],[-9.979691,-8.547454,-4.285488,9.969053,1.785685,-4.664863,-7.444101,-8.690974,-1.943584,9.098362,6.680456,7.122846,-9.078901,8.676089,-9.965726,6.455139,9.351459,7.984463,-8.655038,-0.884069,-4.572019,-4.224282,-4.892098,-1.682247,9.657041,9.175441,4.090172,0.614559,-7.400294,9.853498,0.636969,-0.320188,-5.346619,0.319485,-2.257979,-9.532056,-8.098868,1.343919,4.188965,9.680385,-6.567195,-3.822486,-2.435059,0.894310,-5.776753,7.259212,1.643626,-8.929967,-9.790280,-9.196126,-3.470894,9.330193,1.309260,8.973204,-1.465471,-3.536966,3.515434,-7.381599,-7.910262,5.166984,5.102092,-8.293693,-9.143528,-5.564811,-1.906868,4.937767,-5.344016,-9.420166,-7.423868,-6.272388,-8.536067,8.959715,5.676512,7.257428,0.807394],[4.377828,-3.201073,8.903659,-0.154919,2.096347,-6.093569,8.706644,8.641380,-1.424327,4.114889,-9.555224,8.883803,-7.964881,2.193336,-8.803267,-2.373442,9.182034,-0.402524,6.372307,4.423931,0.810641,2.100533,-0.014665,-4.829750,-5.433742,2.078459,-7.958084,-6.153915,-8.850515,-4.018307,-0.158343,-9.534399,6.790520,-7.877405,3.646552,7.867325,1.927841,-0.247839,2.215056,1.546194,-3.087671,-3.195840,7.325055,7.971121,0.070773,6.779355,-6.172377,3.319193,-1.576133,-1.202637,4.043469,-7.998374,1.507914,-9.566592,-0.194615,-9.076658,7.471213,2.425857,-3.625534,-2.098654,-0.833804,6.845612,8.583056,7.160398,1.834135,2.193240,6.478119,0.845876,-2.725688,-6.778184,3.871637,-4.283614,9.132118,-8.550415,-9.030653],[9.997737,-2.219878,-4.860455,-1.076390,8.180391,4.245881,-3.243184,-0.160863,6.081604,-5.271219,6.070408,3.634231,-8.952257,0.484614,-1.801344,2.875142,9.263182,-0.435069,3.099423,9.090701,-9.948099,9.689721,8.286983,1.021168,2.095282,-4.855006,8.571895,-6.850701,3.781073,-4.129713,5.996551,7.699689,1.317892,-6.837110,-9.324654,7.968759,3.444024,-8.781159,9.039818,3.403231,1.025572,6.327304,0.510155,-2.164342,-4.263050,-5.365251,-8.445318,-0.146826,-6.619060,-9.077620,-5.068543,2.972898,-6.073169,-5.053356,0.783494,-2.420245,-2.949448,-9.541915,3.731376,-8.623314,5.815125,-0.426696,-2.135567,-3.062562,6.623424,-9.196972,-6.114656,5.735079,0.051505,-9.111986,-1.740542,1.624553,0.880600,-4.514350,-5.195707],[-4.268789,-4.075224,9.080861,6.240559,1.238445,-5.637358,-1.616839,5.427651,7.609216,8.347040,-9.348070,6.661512,-8.939740,4.608300,9.592522,0.844287,9.338812,-7.901095,1.366963,-0.186770,3.612337,-0.734147,-3.108312,1.099868,-6.066071,7.155963,-1.201085,-0.707722,1.209955,-5.793155,9.296392,-0.047334,7.331449,0.661594,-1.455476,6.093923,-5.496525,2.141154,9.616912,-2.965492,-8.038541,-6.089898,-6.307405,4.053821,-8.385105,0.479700,-2.721233,8.775108,-6.549121,-1.367618,-3.459376,-4.775507,4.061707,4.937251,5.248599,-8.678543,-0.026674,-9.213351,4.115403,-5.402865,4.419608,8.931333,-1.661457,4.838099,3.366723,7.045805,7.916900,-1.935258,-0.322045,-9.407410,0.973689,2.231769,8.260433,3.867520,9.029405]], dtype = "float32")#candidate|4020|(10, 75)|const|float32
const_4021 = relay.const([-9,-3,8,-1,-4,-9,-3,-8,-6,3,-3,-4,-2,-4,-4,-2,-9,-4,-9,-3,-5,6,3,-3,3,2,6,6,9,-10,4,8,7,2,8,-8,10,-2,-8,-3,2,10,-3,7,6,-5,-7,8,4,9,7,-6,3,-9,-3,-3,10,-3,10,3,7,-6,10,10,4,-7,-9,8,-10,-5,3,-6,-1,-4,-8,7,-6,2,9,-1,1,5,-10,4,-4,-3,-6,8,7,-10,-10,2,2,-1,6,-5,9,-1,-3,-8,-5,-3,-9,10,-2,5,-9,-5,3,-3,7,7,6,-2,-2,-7,3,-10,1,-2,-2,5,6,-4,8,-5,3,-9,-10,9,5,-9,-6,-3,-8,-9,4,4,6,6,-3,-6,-4,5,-8,-6,-2,1,5,-6,1,-5,-1,-2,7,8,-2,6,1,-10,8,4,-2,-2,3,9,-3,-6,3,1,9,-10,6,-6,9,-10,1,-9,-10,-1,-8,6,7,6,-1,2,6,8,-9,-1,-10,5,4,6,6,-9,-10,-6,9,6,8,-10,9,-8,-4,-5,9,-6,8,9,1,-6,6,-7,3,5,-9,-8,2,-7,3,1,-5,-7,2,5,-5,-4,5,6,-5,1,-5,-4,-5,3,4,1,2,-10,-3,8,8,-1,-3,2,7,4,2,-8,9,-8,7,2,-9,-4,9,-2,-3,-9,1,6,5,-9,8,-8,1,1,7,-9,-8,-7,-2,4,-6,-2,6,-5,10,2,3,6,-5,-6,-10,7,6,5,-6,3,-3,7,5,-2,7,-2,3,-8,2,-3,7,-2,-5,-2,7,-3,2,-2,3,1,-10,-2,-10,-3,4,-7,-7,5,6,-5,5,-3,-7,6,-1,-1,10,3,-6,2,-6,1,8,5,5,8,7,7,-6,-5,-9,-7,-2,1,-9,-7,2,8,6,-7,-3,-1,6,-4,2,-9,-8,2,-7,1,5,-10,-8,8,-2,-4,-10,5,4,8,1,-7,-2,-2,-1,4,10,3,-2,1,10,9,10,-5,3,2,-1,-6,9,1,-10,-6,-8,-8,3,-4,-5,-4,5,3,3,6,4,6,-10,3,-1,-2,-1,-9,2,-9,6,-5,-3,1,-2,9,-8,9,-1,10,5,-2,4,5,7,-4,9,4,-6,7,3,-3,-2,-3,-7,8,-4,-2,-4,-6,-1,1,-8,2,-3,1,9,-9,8,-6,4,9,-4,8,-8,-6,3,-8,6,4,-3,5,10,-2,5,-3,2,7,-5,-4,9,1,-1,2,3,5,2,-7,-4,-1,9,-8,-10,-8,1,-7,4,-2,-10,-2,-2,-10,-9,-9,8,-5,-5,-7,-9,-1,9,-1,-7,9,9,10,-2,-8,-7,-5,-6,-1,3,-8,-5,5,7,6,-10,1,8,-9,-4,-3,-3,-8,-9,1,-7,8,-8,-5,-8,-8,9,8,-3,-10,-5,9,-9,6,-6,-4,6,6,-5,-8,5,1,-7,1,-7,8,2,-7,-6,3,-10,4,8,-1,-2,-8,-6,1,10,-7,5,-7,5,-9,9,-1,-10,-4,-7,-3,-5,-6,-2,6,10,-6,-9,1,-9,4,-4,-6,4,-7,6,-9,-3,-9,3,4,9,8,5,3,-10,1,-4,2,-8,8,-9,2,-2,-6,8,-8,-1,6,-4,1,6,1,10,9,-2,-1,-1,-4,8,8,1,-5,-10,8,10,1,-3,7,6,1,-10,-3,-9,-6,9,3,7,2,-10,3,-10,-5,7,-6,7,-2,-4,-10,2,-10,-7,10,-2,5,-3,-2,-3,7,3,4,5,-7,-9,-1,-2], dtype = "int16")#candidate|4021|(675,)|const|int16
const_4022 = relay.const([[-9.857775,-5.880371],[-8.141401,5.860985],[9.713380,1.660548],[6.678784,-2.772118],[-7.505520,-5.908716],[-8.658630,6.477594],[9.893911,-9.871186],[0.283032,7.587724],[8.747047,-6.450140],[5.588409,5.253785],[-4.335534,-2.354116],[7.540847,8.638830],[-4.977791,-0.092347],[-1.878854,-1.112745],[-0.521777,8.053051],[-5.490511,-7.524187],[-3.304694,-8.799206],[-4.181992,-6.681130],[-1.601433,0.714904],[9.751680,6.502263],[-7.639101,-1.373659],[1.901341,-4.537476],[6.524547,-8.993951],[-0.233426,0.513842],[4.564581,-2.914599],[-3.875597,-0.937838],[9.768808,-6.387974],[-2.716712,7.809556],[-1.982750,0.375010],[-7.019304,7.993333],[8.932293,3.545371],[-4.373948,-1.972973],[-3.957322,-9.044230],[-2.554760,8.783107],[-2.922897,-3.843106],[3.679536,2.985433],[-0.582124,-5.902268],[7.793732,-0.304333],[2.950550,-5.907121],[2.772454,9.169884],[-8.478721,-1.833602],[-2.174252,-4.129433],[0.388509,9.170771],[-1.682926,-5.808647],[5.326939,6.147335],[8.222187,7.117856],[-3.114648,-5.144345],[-5.175530,5.951311],[9.983128,9.921274],[-9.299636,-1.462351],[7.686574,-2.825533],[9.781776,-4.658775],[9.302432,2.286126],[2.379247,5.843234],[-4.895880,5.219277],[6.514783,5.357502],[-9.291368,-7.023044],[9.895504,2.766566],[-6.719926,-2.537162],[-6.923413,-1.700208],[6.554159,-8.893024],[-0.684084,-0.581676],[-9.571019,-4.941048],[-2.793227,-0.545536],[-5.347835,6.031068],[-9.702476,-0.261947],[3.926904,-2.611436],[0.244021,1.177027],[-5.728124,-4.663549],[-8.972623,7.065583],[-1.933455,-6.472309],[-5.704701,-8.269751],[-8.370386,-8.444553],[-9.772914,0.773751],[6.963077,3.186725],[0.050414,2.525745],[8.285775,-0.248960],[-2.070870,-5.888630],[9.001729,-7.370010],[3.270326,5.790058],[-5.715855,-4.828373],[-5.815836,-2.004244],[1.528323,9.724959],[3.808882,-8.486353],[-5.198723,-6.666075],[8.484646,6.935366],[6.041238,-8.139610],[-4.650929,-8.533170],[3.232901,8.343387],[2.947357,1.818952],[-8.335010,1.836989],[-8.586634,-8.148189],[-6.859677,5.408300],[2.522257,8.024019],[-1.841181,5.491182],[3.757538,-0.964528],[1.560204,-6.835247],[1.401341,7.621972],[-5.815348,0.415422],[6.224871,5.303713],[-2.867755,8.056235],[-9.558507,1.357896],[-8.886141,2.230879],[-1.780203,-4.099781],[-1.854810,-1.015067],[-8.797046,4.119246],[-1.870015,7.359909],[-7.151155,-2.977883],[-0.575071,-2.224362],[-9.142059,4.211360],[-3.868931,-5.367349],[-7.796374,-5.209360],[4.163522,5.774232],[6.648687,3.067020],[1.506417,1.895667],[2.278311,9.192186],[9.765640,-8.158217],[9.629047,-8.527876],[8.934904,-2.021741],[5.683240,-2.054568],[-7.868799,-7.496764],[-0.803445,8.200660],[8.252663,1.762770],[-2.064395,-9.878600],[-0.037606,1.298372],[-9.351510,6.733818],[-7.490926,-5.614218],[2.323631,4.652310],[-0.380951,3.643097],[8.465152,-5.949271],[6.449691,4.380150],[-9.514332,5.854270],[7.067310,-4.557963],[-9.108751,0.022132],[-0.224470,-9.149096],[-9.801548,8.064539],[2.696670,3.600258],[8.910301,8.619109],[2.025680,3.209232],[-4.986928,-2.374066],[8.495483,-3.121181],[-2.824771,0.727613],[3.558895,-3.964794],[2.565188,-2.555341],[-6.852704,8.572435],[0.847730,-9.730972],[8.309706,7.063382],[-8.327125,1.842741],[-4.551052,0.548028],[4.529338,3.851857],[-2.620255,-2.645453],[3.597498,7.676193],[-3.241794,-4.620894],[2.601256,-8.436565],[-8.187039,8.156211],[5.711815,-0.809292],[-5.675817,0.299460],[-8.704632,-9.565095],[-0.973644,-0.812059],[4.542065,-7.363907],[-8.703935,6.203982],[0.368681,9.656892],[1.309804,9.111374],[3.652204,8.217198],[5.732271,-5.030738],[2.515505,9.305131],[6.859356,-2.779764],[4.453652,8.290483]], dtype = "float32")#candidate|4022|(168, 2)|const|float32
call_4019 = relay.TupleGetItem(func_3234_call(relay.reshape(const_4020.astype('float32'), [10, 5, 15]), relay.reshape(const_4000.astype('int16'), [15, 9]), relay.reshape(const_4021.astype('int16'), [675,]), relay.reshape(const_4022.astype('float32'), [336,]), ), 5)
call_4023 = relay.TupleGetItem(func_3239_call(relay.reshape(const_4020.astype('float32'), [10, 5, 15]), relay.reshape(const_4000.astype('int16'), [15, 9]), relay.reshape(const_4021.astype('int16'), [675,]), relay.reshape(const_4022.astype('float32'), [336,]), ), 5)
output = relay.Tuple([uop_3996,call_3998,const_3999,const_4000,var_4002,var_4003,call_4007,bop_4016,call_4019,const_4020,const_4021,const_4022,])
output2 = relay.Tuple([uop_3996,call_4004,const_3999,const_4000,var_4002,var_4003,call_4009,bop_4016,call_4023,const_4020,const_4021,const_4022,])
func_4025 = relay.Function([var_4001,var_4002,var_4003,var_4008,], output)
mod['func_4025'] = func_4025
mod = relay.transform.InferType()(mod)
mutated_mod['func_4025'] = func_4025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4025_call = mutated_mod.get_global_var('func_4025')
var_4027 = relay.var("var_4027", dtype = "uint32", shape = ())#candidate|4027|()|var|uint32
var_4028 = relay.var("var_4028", dtype = "int32", shape = (105,))#candidate|4028|(105,)|var|int32
var_4029 = relay.var("var_4029", dtype = "float32", shape = (495, 1))#candidate|4029|(495, 1)|var|float32
var_4030 = relay.var("var_4030", dtype = "float64", shape = (195, 2))#candidate|4030|(195, 2)|var|float64
call_4026 = func_4025_call(var_4027,var_4028,var_4029,var_4030,)
output = call_4026
func_4031 = relay.Function([var_4027,var_4028,var_4029,var_4030,], output)
mutated_mod['func_4031'] = func_4031
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4378 = relay.var("var_4378", dtype = "int64", shape = (7, 14, 8))#candidate|4378|(7, 14, 8)|var|int64
var_4379 = relay.var("var_4379", dtype = "int64", shape = (7, 14, 8))#candidate|4379|(7, 14, 8)|var|int64
bop_4380 = relay.logical_xor(var_4378.astype('int64'), relay.reshape(var_4379.astype('int64'), relay.shape_of(var_4378))) # shape=(7, 14, 8)
output = relay.Tuple([bop_4380,])
output2 = relay.Tuple([bop_4380,])
func_4392 = relay.Function([var_4378,var_4379,], output)
mod['func_4392'] = func_4392
mod = relay.transform.InferType()(mod)
mutated_mod['func_4392'] = func_4392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4392_call = mutated_mod.get_global_var('func_4392')
var_4394 = relay.var("var_4394", dtype = "int64", shape = (7, 14, 8))#candidate|4394|(7, 14, 8)|var|int64
var_4395 = relay.var("var_4395", dtype = "int64", shape = (7, 14, 8))#candidate|4395|(7, 14, 8)|var|int64
call_4393 = func_4392_call(var_4394,var_4395,)
output = call_4393
func_4396 = relay.Function([var_4394,var_4395,], output)
mutated_mod['func_4396'] = func_4396
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4646 = relay.var("var_4646", dtype = "int8", shape = (14, 5, 7))#candidate|4646|(14, 5, 7)|var|int8
var_4647 = relay.var("var_4647", dtype = "int8", shape = (14, 5, 7))#candidate|4647|(14, 5, 7)|var|int8
bop_4648 = relay.not_equal(var_4646.astype('bool'), relay.reshape(var_4647.astype('bool'), relay.shape_of(var_4646))) # shape=(14, 5, 7)
uop_4654 = relay.exp(var_4646.astype('float32')) # shape=(14, 5, 7)
func_597_call = mod.get_global_var('func_597')
func_602_call = mutated_mod.get_global_var('func_602')
var_4662 = relay.var("var_4662", dtype = "uint32", shape = ())#candidate|4662|()|var|uint32
var_4663 = relay.var("var_4663", dtype = "uint32", shape = (1694,))#candidate|4663|(1694,)|var|uint32
var_4664 = relay.var("var_4664", dtype = "int32", shape = (105,))#candidate|4664|(105,)|var|int32
call_4661 = relay.TupleGetItem(func_597_call(relay.reshape(var_4662.astype('uint32'), []), relay.reshape(var_4663.astype('uint32'), [11, 11, 14]), relay.reshape(var_4664.astype('int32'), [105,]), ), 1)
call_4665 = relay.TupleGetItem(func_602_call(relay.reshape(var_4662.astype('uint32'), []), relay.reshape(var_4663.astype('uint32'), [11, 11, 14]), relay.reshape(var_4664.astype('int32'), [105,]), ), 1)
output = relay.Tuple([bop_4648,uop_4654,call_4661,var_4662,var_4663,var_4664,])
output2 = relay.Tuple([bop_4648,uop_4654,call_4665,var_4662,var_4663,var_4664,])
func_4667 = relay.Function([var_4646,var_4647,var_4662,var_4663,var_4664,], output)
mod['func_4667'] = func_4667
mod = relay.transform.InferType()(mod)
var_4668 = relay.var("var_4668", dtype = "int8", shape = (14, 5, 7))#candidate|4668|(14, 5, 7)|var|int8
var_4669 = relay.var("var_4669", dtype = "int8", shape = (14, 5, 7))#candidate|4669|(14, 5, 7)|var|int8
var_4670 = relay.var("var_4670", dtype = "uint32", shape = ())#candidate|4670|()|var|uint32
var_4671 = relay.var("var_4671", dtype = "uint32", shape = (1694,))#candidate|4671|(1694,)|var|uint32
var_4672 = relay.var("var_4672", dtype = "int32", shape = (105,))#candidate|4672|(105,)|var|int32
output = func_4667(var_4668,var_4669,var_4670,var_4671,var_4672,)
func_4673 = relay.Function([var_4668,var_4669,var_4670,var_4671,var_4672,], output)
mutated_mod['func_4673'] = func_4673
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4749 = relay.var("var_4749", dtype = "int64", shape = ())#candidate|4749|()|var|int64
var_4750 = relay.var("var_4750", dtype = "int64", shape = (4, 1, 10))#candidate|4750|(4, 1, 10)|var|int64
bop_4751 = relay.maximum(var_4749.astype('int64'), var_4750.astype('int64')) # shape=(4, 1, 10)
output = relay.Tuple([bop_4751,])
output2 = relay.Tuple([bop_4751,])
func_4760 = relay.Function([var_4749,var_4750,], output)
mod['func_4760'] = func_4760
mod = relay.transform.InferType()(mod)
var_4761 = relay.var("var_4761", dtype = "int64", shape = ())#candidate|4761|()|var|int64
var_4762 = relay.var("var_4762", dtype = "int64", shape = (4, 1, 10))#candidate|4762|(4, 1, 10)|var|int64
output = func_4760(var_4761,var_4762,)
func_4763 = relay.Function([var_4761,var_4762,], output)
mutated_mod['func_4763'] = func_4763
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4786 = relay.var("var_4786", dtype = "float64", shape = (5, 8, 12))#candidate|4786|(5, 8, 12)|var|float64
uop_4787 = relay.sinh(var_4786.astype('float64')) # shape=(5, 8, 12)
func_1640_call = mod.get_global_var('func_1640')
func_1643_call = mutated_mod.get_global_var('func_1643')
var_4791 = relay.var("var_4791", dtype = "float32", shape = (495,))#candidate|4791|(495,)|var|float32
call_4790 = relay.TupleGetItem(func_1640_call(relay.reshape(var_4791.astype('float32'), [15, 11, 3])), 0)
call_4792 = relay.TupleGetItem(func_1643_call(relay.reshape(var_4791.astype('float32'), [15, 11, 3])), 0)
const_4793 = relay.const([[[5.781388,2.298389,-2.269397,-5.846483,3.314287,5.200677,2.727874,-2.500965,-0.918183,9.453138,8.658315,-4.564826],[-4.587023,-7.466952,0.613628,1.330375,-1.601219,8.673293,-6.464204,2.839344,-1.172158,-6.698465,3.224876,0.016227],[-7.293954,-8.011922,-7.798217,2.069224,-2.744403,-0.420045,2.297779,-6.113415,9.707814,-8.707384,3.551188,4.459447],[-1.552460,-4.647340,-4.774281,6.960600,-3.627130,-1.845135,-9.682601,-6.336244,9.963976,-3.214621,-5.663886,-5.818724],[8.216494,6.677596,-3.084204,-8.636173,-0.152026,3.918669,-4.300067,-7.032772,-7.763934,7.461776,-1.084080,6.319962],[4.339317,-7.641744,1.143084,0.113825,2.222894,1.213181,1.954438,-6.317134,-8.636520,-7.184075,-2.996826,-7.028086],[6.190960,8.542648,2.155159,6.483085,-6.015590,-7.493056,-5.939075,-9.075559,-0.724131,6.795166,5.091695,7.321141],[1.619721,-5.082841,-3.795186,-0.438276,4.801026,9.048611,5.303210,0.480986,-1.290500,5.404967,4.784576,-7.215788]],[[1.321173,3.599460,9.757735,6.850957,-3.743202,-1.440667,-1.038751,-4.821445,-1.503180,-9.292344,-4.447207,-9.927405],[6.453583,4.002599,4.093068,-2.980731,5.582413,-7.108261,-7.245528,-6.295702,1.177526,-5.781210,5.886665,6.313657],[-4.996648,0.246540,0.768519,-9.487830,8.018558,8.970319,3.511896,-5.677860,9.903744,-3.370644,-4.850577,-0.441412],[1.302294,4.686761,2.537315,7.005183,-3.810207,-9.304822,-9.474563,-6.475891,-9.990269,-6.050109,6.475539,4.617027],[0.155923,-1.381359,-5.523253,-5.737484,8.389859,-9.201077,-0.708928,8.771322,9.839093,3.929603,-0.296211,3.714494],[4.100207,-3.396427,-9.823024,-0.925640,2.827760,2.757327,3.874908,-0.181242,5.192158,-5.238118,-8.776345,-0.482325],[4.564081,7.852820,6.100142,6.316819,-9.168914,5.500144,6.212466,3.209679,4.271594,-6.801381,-8.725744,7.137222],[9.567697,3.948982,1.550700,3.100565,4.497037,-3.188596,-6.072261,-1.624582,-8.810132,4.350809,9.855851,-5.258593]],[[-2.790126,5.308921,4.476453,-0.831698,-5.116254,-0.711400,-3.573136,4.922171,-0.035959,-6.152652,6.823045,-6.490483],[0.039488,5.789004,-9.642436,1.709851,-4.206816,2.888706,5.694704,-0.971380,8.444141,-8.735658,7.289268,-4.210035],[1.320131,-7.093694,7.034331,-0.212450,-8.113502,6.148434,-7.947550,6.739463,1.805744,-5.238610,0.129949,4.028364],[-1.351403,-3.178327,2.869542,7.966525,2.741729,0.324460,-7.703627,9.171671,7.280399,4.678358,7.384236,-2.394217],[1.603807,-9.321150,8.553890,-3.346070,4.253815,1.189636,3.334190,1.170560,-2.947119,2.056133,7.095280,-8.325161],[3.707813,-8.693236,-8.369107,5.166531,6.278813,-7.325289,5.001595,-8.838208,5.570533,3.946157,6.759605,-4.857883],[6.908534,-7.965610,-1.250536,0.195373,7.566706,0.861860,-8.148556,9.862134,-3.442121,3.407590,-0.447886,-1.187813],[5.531433,-1.218419,-6.567570,7.787280,-0.222615,-0.134794,-6.835283,-7.801927,9.347102,0.760241,3.299723,-7.251403]],[[0.645945,7.187759,2.275525,3.134602,-6.997934,9.545686,-6.328108,-5.697630,4.889050,-6.729409,1.213708,4.946459],[-6.530916,-8.805575,0.244837,9.724681,-9.671423,3.568994,-8.326952,5.739163,-5.447035,3.659622,3.292088,-0.547612],[7.151977,-2.836019,0.036715,0.242625,-0.393051,9.719236,-1.446396,-9.439853,-5.624422,7.217695,5.866540,3.503167],[0.390868,-5.344081,-6.584679,8.319644,5.613524,-2.356728,2.900936,-9.394847,-2.420415,-2.801717,-6.336003,7.105248],[-7.053015,2.231323,5.524382,3.933155,-8.690747,8.351953,-6.842645,-8.722701,-5.691461,1.285435,-9.037792,-2.859312],[5.658315,-7.550512,0.934094,-5.216242,-3.474199,7.443889,-0.018506,-4.411665,7.635252,-5.191381,1.323657,4.338117],[5.873826,1.754763,3.584259,-2.638828,-9.951419,-7.402613,2.233692,0.799950,4.047791,4.242868,-9.292372,-8.819413],[-4.996677,9.776366,4.443112,3.249867,4.058346,-6.519657,-9.202687,-0.966734,5.378319,7.628062,7.099867,-4.374495]],[[3.261728,8.928734,-4.441665,0.045367,-6.832523,-8.585914,-3.396139,-6.825558,-4.841460,-7.069003,-2.313931,-7.087028],[7.999826,-1.096380,-2.260311,9.765653,-9.212228,4.096349,-6.846824,8.942566,-7.864966,-3.309313,-3.773465,-5.558410],[-1.614238,2.102100,1.142187,-3.753405,4.121525,-7.725844,-3.038134,-7.735273,-8.096585,1.290851,-3.274798,4.623736],[-4.483128,8.115751,-0.172117,1.437638,-0.169319,5.213216,-0.375830,0.450426,-4.978168,-8.304621,9.886030,-9.418106],[-7.382217,7.510085,-3.828339,2.415255,-2.971759,9.012350,7.503969,3.197001,-0.633076,3.269772,2.093630,-3.893193],[-2.715601,-2.001635,0.455599,7.249449,-5.191302,3.916994,4.644204,2.058665,1.533163,1.071283,9.926648,4.322594],[5.842399,2.832283,1.755783,1.487497,-0.211068,4.329901,-3.853655,4.461977,5.601928,1.806831,-1.614810,3.021833],[-3.768403,-0.880132,5.991936,7.556836,-3.621998,7.353790,-0.588354,-8.260068,-5.483379,4.844658,-8.877756,2.738390]]], dtype = "float64")#candidate|4793|(5, 8, 12)|const|float64
bop_4794 = relay.floor_mod(uop_4787.astype('float32'), relay.reshape(const_4793.astype('float32'), relay.shape_of(uop_4787))) # shape=(5, 8, 12)
func_4667_call = mod.get_global_var('func_4667')
func_4673_call = mutated_mod.get_global_var('func_4673')
const_4804 = relay.const([-5,10,-5,-6,-7,-8,-4,-3,4,-3,-7,2,8,9,-2,-7,-1,3,-2,-8,9,-3,10,5,5,7,-10,-4,-3,-2,-5,1,6,3,-6,6,-6,-10,6,10,-7,3,-8,-6,4,-5,6,7,4,1,-3,-7,7,7,7,5,6,1,-9,-4,-4,-3,9,-4,2,-2,4,5,-9,5,10,9,-7,2,7,10,9,2,3,-10,3,3,-5,9,1,-9,-3,8,1,8,8,-7,-1,-4,7,1,-9,-7,3,6,9,6,8,-4,6,4,7,-8,2,-3,7,9,10,-10,-4,-8,4,7,-8,10,10,-7,-5,5,8,-6,-4,2,-1,-9,-9,-7,9,-6,4,2,-9,-3,3,-2,8,7,-3,9,9,6,-3,2,1,-2,3,-1,2,-7,-3,-7,8,-4,2,2,1,1,3,7,-3,-8,-2,9,2,10,-6,6,-10,-3,-6,-6,-5,1,2,3,-9,-2,-2,7,-6,9,4,5,8,10,5,2,-5,-9,3,2,4,2,-4,10,-6,1,-6,7,4,-7,3,8,-2,-5,-10,-6,-3,-10,7,-5,1,-4,2,-9,9,5,7,10,-2,-4,-3,7,-9,3,9,9,-5,4,-4,-4,-1,5,-4,-7,3,9,4,-4,-2,-10,-4,-8,-4,4,5,1,7,-4,-2,-7,4,2,1,2,-10,4,-1,-3,-7,3,7,10,1,-6,6,-7,-9,-2,-5,-6,7,1,2,-5,2,-3,-3,4,-6,6,-4,-6,-3,5,-3,5,1,-9,9,-4,-3,10,9,-9,-4,8,-7,-1,3,8,-7,5,10,-2,10,-2,2,-9,5,5,1,7,8,-10,-6,-6,-3,10,4,2,8,7,5,-1,3,2,-9,-4,9,-7,-2,7,-3,9,-10,1,5,10,-5,-2,8,2,3,6,8,6,-8,5,1,-9,5,1,-10,-1,3,-3,9,8,-1,-3,-8,9,3,7,8,-7,8,2,-8,-4,8,1,3,9,-4,3,5,-9,-5,-2,-2,5,-6,9,2,6,1,9,-9,-9,3,6,-5,-6,-1,3,-9,7,-7,-1,10,-9,7,8,-8,-8,1,1,-10,8,7,-7,2,-4,-10,6,-4,-2,4,-6,9,3,9,7,1,1,9,-6,3,7,-7,-3,1,4,7,10,-6,-7,-9,6,-2,-9,6,1,7,3,3,9,-5,-3,-4,10,6,-7,-4,4,-2,8,-10,7,6,-5,10,-5,6,-7,1,-2,-7,-3,-4,8,1,3,-2,1,4,9,10,7,3,8,-1,2], dtype = "int8")#candidate|4804|(490,)|const|int8
var_4805 = relay.var("var_4805", dtype = "uint32", shape = ())#candidate|4805|()|var|uint32
var_4806 = relay.var("var_4806", dtype = "uint32", shape = (1694,))#candidate|4806|(1694,)|var|uint32
const_4807 = relay.const([-8,3,-6,-4,3,4,10,-9,2,2,6,10,3,3,4,-1,-8,6,9,4,-7,-5,4,3,6,6,1,9,7,7,-6,6,3,8,1,4,-2,-5,5,-2,5,2,-4,-10,-1,-4,7,10,1,2,2,2,-6,-10,-8,1,-8,1,-4,-3,-10,-1,-7,9,-9,-4,6,4,-4,5,7,-5,-3,-7,9,-3,8,-8,-4,-3,-7,-7,2,6,-6,-7,-1,7,3,10,-5,3,-6,6,-7,5,7,-8,3,-6,7,3,-8,-3,-6], dtype = "int32")#candidate|4807|(105,)|const|int32
call_4803 = relay.TupleGetItem(func_4667_call(relay.reshape(const_4804.astype('int8'), [14, 5, 7]), relay.reshape(const_4804.astype('int8'), [14, 5, 7]), relay.reshape(var_4805.astype('uint32'), []), relay.reshape(var_4806.astype('uint32'), [1694,]), relay.reshape(const_4807.astype('int32'), [105,]), ), 4)
call_4808 = relay.TupleGetItem(func_4673_call(relay.reshape(const_4804.astype('int8'), [14, 5, 7]), relay.reshape(const_4804.astype('int8'), [14, 5, 7]), relay.reshape(var_4805.astype('uint32'), []), relay.reshape(var_4806.astype('uint32'), [1694,]), relay.reshape(const_4807.astype('int32'), [105,]), ), 4)
func_4760_call = mod.get_global_var('func_4760')
func_4763_call = mutated_mod.get_global_var('func_4763')
var_4811 = relay.var("var_4811", dtype = "int64", shape = (40,))#candidate|4811|(40,)|var|int64
call_4810 = relay.TupleGetItem(func_4760_call(relay.reshape(var_4805.astype('int64'), []), relay.reshape(var_4811.astype('int64'), [4, 1, 10]), ), 0)
call_4812 = relay.TupleGetItem(func_4763_call(relay.reshape(var_4805.astype('int64'), []), relay.reshape(var_4811.astype('int64'), [4, 1, 10]), ), 0)
output = relay.Tuple([call_4790,var_4791,bop_4794,call_4803,const_4804,var_4805,var_4806,const_4807,call_4810,var_4811,])
output2 = relay.Tuple([call_4792,var_4791,bop_4794,call_4808,const_4804,var_4805,var_4806,const_4807,call_4812,var_4811,])
func_4814 = relay.Function([var_4786,var_4791,var_4805,var_4806,var_4811,], output)
mod['func_4814'] = func_4814
mod = relay.transform.InferType()(mod)
mutated_mod['func_4814'] = func_4814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mutated_mod.get_global_var('func_4814')
var_4816 = relay.var("var_4816", dtype = "float64", shape = (5, 8, 12))#candidate|4816|(5, 8, 12)|var|float64
var_4817 = relay.var("var_4817", dtype = "float32", shape = (495,))#candidate|4817|(495,)|var|float32
var_4818 = relay.var("var_4818", dtype = "uint32", shape = ())#candidate|4818|()|var|uint32
var_4819 = relay.var("var_4819", dtype = "uint32", shape = (1694,))#candidate|4819|(1694,)|var|uint32
var_4820 = relay.var("var_4820", dtype = "int64", shape = (40,))#candidate|4820|(40,)|var|int64
call_4815 = func_4814_call(var_4816,var_4817,var_4818,var_4819,var_4820,)
output = call_4815
func_4821 = relay.Function([var_4816,var_4817,var_4818,var_4819,var_4820,], output)
mutated_mod['func_4821'] = func_4821
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4915 = relay.var("var_4915", dtype = "uint16", shape = (7, 3, 5))#candidate|4915|(7, 3, 5)|var|uint16
const_4916 = relay.const([[[-2,-10,6,-7,-6],[7,-9,1,1,-4],[-10,-6,3,7,-3]],[[1,-5,-10,-2,-3],[-9,-4,-1,10,1],[-2,8,-1,7,6]],[[-3,5,-7,9,2],[-10,2,-7,-8,-6],[3,-1,-7,2,10]],[[-4,-7,1,2,5],[-9,4,8,-8,-8],[-7,-4,4,3,-7]],[[-3,6,-8,4,-4],[-7,-6,8,-2,-2],[3,-3,-10,-10,10]],[[5,-8,3,-9,-9],[8,10,5,-7,6],[-7,-9,-6,7,1]],[[5,3,9,9,-3],[-3,-2,-4,-8,-4],[-10,-3,-1,-9,7]]], dtype = "uint16")#candidate|4916|(7, 3, 5)|const|uint16
bop_4917 = relay.less_equal(var_4915.astype('bool'), relay.reshape(const_4916.astype('bool'), relay.shape_of(var_4915))) # shape=(7, 3, 5)
bop_4925 = relay.minimum(bop_4917.astype('uint32'), relay.reshape(var_4915.astype('uint32'), relay.shape_of(bop_4917))) # shape=(7, 3, 5)
uop_4931 = relay.log10(bop_4917.astype('float32')) # shape=(7, 3, 5)
uop_4953 = relay.log(uop_4931.astype('float32')) # shape=(7, 3, 5)
var_4955 = relay.var("var_4955", dtype = "float32", shape = (7, 3, 5))#candidate|4955|(7, 3, 5)|var|float32
bop_4956 = relay.mod(uop_4931.astype('float64'), relay.reshape(var_4955.astype('float64'), relay.shape_of(uop_4931))) # shape=(7, 3, 5)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_4978 = relay.TupleGetItem(func_411_call(relay.reshape(uop_4931.astype('int32'), [105,])), 4)
call_4979 = relay.TupleGetItem(func_413_call(relay.reshape(uop_4931.astype('int32'), [105,])), 4)
uop_4990 = relay.atanh(uop_4953.astype('float64')) # shape=(7, 3, 5)
bop_5000 = relay.logical_or(uop_4990.astype('bool'), relay.reshape(bop_4925.astype('bool'), relay.shape_of(uop_4990))) # shape=(7, 3, 5)
func_4814_call = mod.get_global_var('func_4814')
func_4821_call = mutated_mod.get_global_var('func_4821')
var_5004 = relay.var("var_5004", dtype = "float64", shape = (480,))#candidate|5004|(480,)|var|float64
var_5005 = relay.var("var_5005", dtype = "float32", shape = (495,))#candidate|5005|(495,)|var|float32
const_5006 = relay.const(-8, dtype = "uint32")#candidate|5006|()|const|uint32
const_5007 = relay.const([-7,-4,1,10,4,4,-3,8,10,9,-3,-7,-1,2,-1,-3,-9,5,-8,7,-9,6,7,-3,7,5,7,2,-10,1,5,-10,-2,6,2,-4,4,2,5,10,-7,4,6,-4,-2,8,1,-2,4,3,-1,4,-6,-7,-2,-2,2,3,-4,6,3,3,-3,5,3,3,4,7,4,10,3,-2,-10,6,-1,-7,-6,8,-5,7,2,10,-7,-5,-5,6,-7,-6,3,-10,-2,-1,-9,-8,-4,2,6,10,-1,4,-10,-3,-1,5,-10,-10,-3,-3,-10,7,-7,-9,-9,6,-4,5,3,2,-8,7,3,10,-8,8,-3,1,-2,-5,-9,-2,-5,10,6,1,-10,-3,8,9,-8,4,-10,3,7,-4,1,3,4,4,-5,7,7,-8,-3,1,-4,5,1,-7,-8,-9,10,4,3,-5,5,4,1,-7,7,-10,-2,-6,-2,5,5,-8,-4,-8,-10,-5,-6,-7,1,5,-1,-10,7,9,-6,-9,8,5,-2,1,7,-7,5,1,-9,5,-9,-4,-8,6,-7,6,-6,7,5,8,-4,-4,-10,-6,-9,-10,3,-7,-4,6,9,7,4,-1,-2,8,7,-6,8,7,-2,-8,-8,-7,-7,8,-4,1,-8,6,5,-5,-7,-9,-2,2,3,8,-4,-8,7,-7,10,10,2,8,-1,10,-6,3,-9,-2,7,-6,5,2,-1,-7,-6,-8,3,8,3,-2,-10,6,1,2,8,-9,-3,8,-9,-4,10,-5,-8,-6,2,-9,-2,10,3,-1,9,7,-10,-5,-8,6,-10,2,4,8,-6,10,2,-9,-1,9,10,-3,2,1,-6,-9,-8,4,-1,-9,1,-2,9,-9,4,2,5,8,5,7,-6,8,9,5,-6,6,-4,-10,4,3,9,-3,1,2,-1,-7,-7,-9,9,-6,-8,2,-3,-5,2,-6,-3,5,-10,-2,-8,-8,-4,-1,10,-9,4,-2,-6,5,-3,10,9,2,4,2,2,9,6,-2,1,-9,-5,-1,6,-8,6,6,5,7,-3,3,9,-1,2,-5,5,8,-3,-10,7,-9,-7,-10,-5,4,-8,-3,-1,-3,-10,-7,-2,-4,4,-3,3,5,7,2,2,9,-7,6,7,-10,-10,1,-4,7,10,-10,-4,-2,-10,-2,-2,-2,-3,6,2,6,-5,-3,1,-6,4,1,10,-8,8,3,-2,1,-7,-5,5,2,6,8,7,-8,1,-8,3,-1,5,2,-3,3,2,-1,-9,6,8,5,-9,6,-4,-10,10,9,7,5,6,2,-7,-4,3,4,-3,7,-3,1,7,6,5,5,7,-4,9,3,-8,-2,7,2,-8,4,-2,-9,-8,-8,-10,-7,-2,-2,-8,7,-1,6,-9,-10,9,-6,-10,-2,2,3,3,-1,-2,8,-7,5,7,10,2,-1,-5,-2,6,5,-1,9,10,-1,-2,-2,5,9,-1,-6,-8,-3,-5,-1,-8,8,7,-5,7,9,6,-8,-9,1,-7,-2,-3,1,-10,7,-7,1,-2,10,4,-9,-1,9,8,-9,-6,-2,-7,-7,3,7,8,-5,4,-2,-5,9,1,-5,10,4,6,-5,8,2,-7,-3,-8,-7,-4,-3,1,-4,-1,-3,-4,7,4,-6,5,6,-8,-6,9,-9,4,1,-5,10,-5,-9,10,2,-9,8,6,-3,-5,1,4,-7,3,6,5,7,8,3,-1,4,3,1,6,-2,-7,-4,-4,-1,-1,6,-2,-7,7,10,5,8,-6,5,-5,4,1,-2,9,1,-10,-7,10,-5,-4,-6,9,-6,5,8,2,3,-9,8,10,-9,8,3,10,8,-2,-4,10,-7,-1,8,-6,7,-6,5,-8,-6,-10,8,-8,-3,-3,-3,-7,10,7,1,9,-1,7,-2,-10,-3,9,8,10,-8,-8,-5,-3,-3,5,4,-6,-2,10,-9,-6,1,-6,3,-2,-8,-3,-7,2,-5,-6,4,3,-6,-1,3,7,-3,3,-10,6,-7,-3,-5,6,1,-10,-5,-2,-8,-4,-10,-5,6,8,4,4,-5,8,1,2,6,-8,5,-4,2,-3,10,5,7,2,9,5,-2,-4,6,4,5,5,-1,-4,6,3,-7,-4,4,-6,-1,-7,-3,-7,-6,-3,4,-3,-8,7,-4,1,-1,-6,10,-7,4,-5,4,9,4,3,1,-2,4,-4,10,-2,10,-5,1,-3,-8,5,10,-4,-6,-10,-4,8,2,8,9,4,-9,2,-2,8,-1,6,9,-6,8,3,-8,3,5,3,-3,-5,-5,4,-2,-9,-5,6,4,10,8,7,-6,-8,-2,-7,8,-5,1,-2,2,-5,8,-3,-3,-8,6,-9,-4,5,9,-8,6,-2,5,-7,9,7,5,-4,5,-9,5,-5,-6,6,-2,2,10,-2,-2,-3,3,8,2,-6,4,-7,-5,10,3,-5,-10,3,-5,-6,-6,-5,1,-6,-7,-9,8,-10,8,-2,-5,8,-8,-5,7,-7,10,-1,9,-5,10,5,-10,10,-4,1,-1,-5,9,3,1,9,6,-4,7,-9,-3,-4,-1,1,7,7,10,-1,1,-4,-6,6,3,4,1,-9,-10,-7,7,6,-9,-4,-4,7,8,10,6,-3,7,-1,3,-5,2,1,2,-3,-2,-10,-3,2,2,-5,-7,9,8,-6,-1,3,5,-3,3,5,-3,4,6,7,-7,4,1,-9,5,-1,6,-8,-7,-7,-6,-8,9,-5,7,3,-4,-9,10,7,5,2,9,-4,2,9,-4,-7,10,-10,-3,10,-7,4,8,7,-7,-7,-8,7,10,7,4,9,-5,-8,9,8,8,7,1,-9,2,9,5,-1,-1,-1,2,8,10,-6,5,-6,5,-8,7,7,5,1,-1,9,1,-6,1,-10,9,9,-9,-6,8,3,5,-7,5,2,-2,-7,-10,-6,6,-1,4,-8,3,-9,1,-8,-9,7,-5,-1,10,10,2,9,1,-4,10,-8,-9,-5,9,7,10,-4,-4,2,5,-2,-5,7,-10,3,-5,4,9,2,-3,-8,4,-10,8,-10,1,10,-4,-5,9,6,-8,6,8,-5,-9,-7,-4,-1,6,-5,-5,6,3,-6,7,4,10,5,10,-2,3,-1,-4,-9,-8,-9,1,-2,7,7,-10,1,5,-10,6,-3,1,7,-10,6,-5,1,-2,-10,-3,-3,2,-4,2,1,6,-8,-1,2,5,9,5,-6,7,8,-5,-4,6,5,2,5,-1,6,-2,-3,-6,-7,-6,-2,10,-2,8,3,6,2,-3,7,-4,8,-1,2,-7,10,3,6,-9,-8,6,5,-1,-1,5,-10,1,6,-1,9,9,-9,3,-6,4,1,7,-4,-4,5,-3,10,-3,3,-7,1,-4,-10,6,9,-2,-1,-10,-7,8,-4,7,4,-2,-5,1,-7,-6,4,-3,-1,-7,3,-7,-10,6,-5,-1,4,-8,-4,-5,-6,8,-5,2,7,8,7,-4,-10,4,-3,4,10,-8,-1,-7,-6,-4,7,6,-7,6,10,2,10,5,1,-3,-1,5,-6,8,7,-2,2,-2,2,3,-10,10,-1,5,4,10,1,-9,8,-8,3,-1,7,4,-3,-1,-3,3,6,5,10,-9,-3,-7,-8,-5,-6,-8,2,-4,2,-8,-8,9,2,6,-1,2,-5,-2,7,-6,8,8,7,-6,9,3,6,-1,-8,-8,-4,-1,-1,-2,4,1,-1,3,5,6,-5,1,-1,-10,1,-5,10,4,1,-2,-5,9,6,-5,-3,-4,1,2,10,-10,1,8,3,7,-1,1,3,-3,1,-7,10,-5,-9,-3,-8,-9,-8,2,-10,-7,7,-6,-9,-7,-8,7,8,-1,8,3,6,-4,-1,-8,-5,-4,7,1,1,-6,-4,1,4,6,-3,-5,5,5,-8,-8,10,-5,4,-2,-6,7,1,2,7,7,-9,1,4,9,-9,-4,3,-5,-5,-3,5,-1,-8,-4,-10,-7,3,-2,-1,10,-2,-8,-4,-1,2,-2,-3,-5,-3,-8,-8,-2,10,-10,7,-3,-4,3,6,9,-5,4,1,1,-6,6,3,-7,-4,-5,6,-9,1,-8,-3,4,5,9,7,1,10,-7,7,-5,-10,-3,10,-7,-3,9,-2,-7,-3,7,8,-3,-7,-3,-6,-7,-1,-5,2,6,-8,3,-10,-9,9,-10,5,-7,-6,7,1,8,-4,-4,4,-2,-5,-2,-9,5,-8,7,2,6,-6,-8,6,-8,-9,-7,-2,-5,5,-1,8,-2,-5,-2,5,-3,-10,10,8,-8,-2,-2,-1,-1,-4,-1,-10,-3,-2,-2,-10,9,-7,-7,9,-6,8,5,-4,-8,-1,-5,9,-8,10,9,-6,-1,9,9,-3,1,2,-5,-4,-9,9,8,1,-1,7,-2,-8,7,2,7,3,-1,4,3,6,-3,-7,4,-6,-8,5,-5,6,-10,7,6,-3,-7,10,5,4,-2,8,9,-3,8,-9,-10,-4,-3,-6,-3,7,-6,-9,-4], dtype = "uint32")#candidate|5007|(1694,)|const|uint32
var_5008 = relay.var("var_5008", dtype = "int64", shape = (40,))#candidate|5008|(40,)|var|int64
call_5003 = relay.TupleGetItem(func_4814_call(relay.reshape(var_5004.astype('float64'), [5, 8, 12]), relay.reshape(var_5005.astype('float32'), [495,]), relay.reshape(const_5006.astype('uint32'), []), relay.reshape(const_5007.astype('uint32'), [1694,]), relay.reshape(var_5008.astype('int64'), [40,]), ), 5)
call_5009 = relay.TupleGetItem(func_4821_call(relay.reshape(var_5004.astype('float64'), [5, 8, 12]), relay.reshape(var_5005.astype('float32'), [495,]), relay.reshape(const_5006.astype('uint32'), []), relay.reshape(const_5007.astype('uint32'), [1694,]), relay.reshape(var_5008.astype('int64'), [40,]), ), 5)
func_3668_call = mod.get_global_var('func_3668')
func_3676_call = mutated_mod.get_global_var('func_3676')
var_5017 = relay.var("var_5017", dtype = "uint16", shape = (600,))#candidate|5017|(600,)|var|uint16
const_5018 = relay.const([[-5.052374,-5.890109,7.013851,-2.015034,-4.557566,-4.611933],[-1.742905,1.885825,-5.634898,-4.084919,9.266861,1.267043],[-1.511748,9.286500,2.099696,0.047635,5.285811,-3.984702],[1.926409,7.972528,6.542703,-0.033270,4.414174,-1.332358],[1.960405,-7.682451,6.507087,-2.328870,-4.027607,-7.949292],[-0.990692,5.400296,0.907354,-9.741670,-1.690175,2.306748],[2.607559,0.086510,1.125602,8.309200,5.846044,7.776206],[6.270216,-7.632617,0.689774,1.134615,9.618503,-0.863463],[5.787944,9.760731,-2.333281,4.310162,2.878239,-2.280050],[-4.353454,2.012006,2.902929,-3.690370,2.950589,-0.494761],[5.744126,-5.324695,-2.611014,-0.078605,-5.974196,8.975575],[-1.661104,-4.101638,-6.523532,-4.354315,-8.940003,-7.699878],[-2.494874,-9.497776,3.779708,-0.671259,3.493131,6.070311],[3.825055,1.062378,-4.474918,-3.085982,0.941456,-1.663165],[6.030117,-7.129373,-7.505747,8.294926,-6.203313,-1.484912],[-2.131862,-2.619290,-2.837687,2.273293,2.788058,8.601883],[-6.241669,-2.701013,-7.989068,6.482060,5.818921,-6.595701],[-9.746711,-6.539788,9.689177,-3.196506,-8.607741,4.169310],[3.986852,-5.897167,5.081697,-4.429948,-4.675229,2.321737],[2.078608,-9.762187,6.835859,-6.441022,8.878836,-8.423652],[-3.090968,-1.710258,1.178104,4.094068,8.766258,-7.058237],[5.828942,-1.040939,7.266209,-2.943360,-3.091323,-3.685677],[1.104787,4.582735,1.286607,-1.172251,-3.876237,-3.723463],[-8.586210,-3.210702,-0.350955,7.729605,8.089698,5.862984],[1.092863,0.216957,-0.465726,0.366751,7.543188,-6.284560],[-8.965264,-2.330112,-3.299540,5.196301,-1.035009,-0.492346],[-5.961818,-7.751804,1.869523,-5.773720,7.129234,-3.414939],[5.678904,-3.336442,-2.131969,-0.756605,4.298111,3.558465],[4.795476,-0.943332,3.330873,-8.452853,-4.880820,9.281377],[-0.674638,2.417373,-8.946941,-2.569583,2.433815,-2.013089],[2.130520,0.420037,1.581173,-4.704276,6.375657,-1.024201],[7.119852,-6.888992,8.984692,6.072181,7.530695,7.881321],[-8.748283,-0.321566,-1.607663,7.009403,9.813377,-5.727372],[-1.358720,1.832684,-1.769947,-4.659070,5.115396,0.217018],[-6.091669,-2.073143,7.112402,9.715516,0.106979,-4.804330],[-7.334648,-6.270367,-1.673696,-0.687351,2.315820,-1.621021],[2.249170,-2.290659,0.684502,0.944631,-5.755808,2.324296],[-5.221635,-1.739193,-3.035830,7.532442,-0.793423,-6.671970],[3.810643,2.221070,1.117286,-4.180164,-5.486258,0.618301],[-0.348220,-3.593164,-0.655164,0.528077,-2.017794,0.105731],[-9.578350,-2.041195,-6.756932,2.711566,7.114161,-5.168915],[-5.429181,-5.565294,7.657753,-4.435819,-2.329979,8.494875],[-1.689612,3.303165,-0.612108,-3.523729,-2.053193,2.154487],[4.106094,-7.340821,-5.543859,9.077170,4.892397,4.644457],[5.940550,-7.268073,-4.894721,9.040680,-9.058636,-3.266264],[8.619347,9.618307,8.793575,-0.639762,6.167560,3.790757],[3.901956,-9.285324,-0.903193,-9.631740,0.348971,-3.002145],[-0.399943,3.768096,-6.896018,6.331315,-8.432321,2.811175],[0.777277,-9.014547,-6.270955,-0.210980,6.635987,-5.674371],[6.474650,5.594238,-5.322631,-2.551062,0.950822,2.982098],[5.775812,4.083704,-9.455001,1.681389,-6.465293,-0.577677],[-3.293916,8.122504,-6.800082,3.191055,-6.405843,-8.783291],[-3.728740,6.386873,-9.006829,-3.825124,3.206392,4.625384],[-5.030617,1.816317,8.576626,-3.717675,9.395527,9.803305],[4.529655,3.183345,5.493824,-9.415563,-6.882240,-0.667861],[3.673606,3.941966,-4.691753,-0.385129,5.576020,-9.765106],[8.821558,-5.051377,-9.501326,-3.948396,7.791576,2.732374],[-1.327163,-2.695948,6.540387,3.802122,9.310212,7.235301],[-7.362023,6.623965,6.291524,-7.083826,-1.455260,7.470403],[-9.824082,-4.415870,7.868574,-2.381009,-8.818504,1.706220],[5.761532,-2.797568,2.263714,0.167449,4.128504,3.150316],[-4.300720,0.752923,3.828088,2.481642,5.646288,0.401066],[1.652383,-3.018008,-2.157161,8.023543,-3.492455,7.733226],[7.224924,3.860416,9.040594,1.769483,-0.261519,-9.067984],[-2.109783,6.201629,7.018346,-5.820198,0.114800,-4.055330]], dtype = "float64")#candidate|5018|(65, 6)|const|float64
const_5019 = relay.const([[9,-10,-5,8,10,-2],[-2,8,8,8,8,10],[3,3,-2,-6,4,-7],[-9,-4,-6,-8,1,6],[9,-1,-9,5,1,-4],[8,-1,-3,3,5,3],[-4,-4,6,6,3,-4],[-10,-4,8,-1,-7,-1],[5,6,-1,-3,-7,10],[4,1,-3,2,4,2],[6,-8,-10,-7,5,4],[10,9,-4,-3,4,8],[6,1,-7,-2,10,8],[-9,4,-8,-9,8,8],[-8,-2,2,2,-1,-8],[7,1,-7,9,4,1],[-4,10,10,-5,8,3],[-7,-8,7,5,3,3],[-5,-8,-6,10,-1,3],[10,-10,-5,-8,7,1],[1,9,-3,4,7,-8],[-2,4,-1,-5,-4,1],[5,2,-9,-7,2,-4],[10,-5,-9,1,-1,7],[1,5,4,-5,-9,-2],[-1,-7,-4,-7,9,3],[-3,1,1,-6,-7,-8],[-8,1,-9,6,-3,2],[-3,4,-9,10,-5,-5],[-9,9,-5,7,1,1],[-5,9,-9,5,-9,2],[10,-9,-2,-1,9,-7],[8,-6,-5,8,-3,6],[-9,-1,-4,6,6,-8],[2,-1,1,3,-3,-8],[-7,8,7,-1,-9,-7],[-9,6,8,6,-5,-9],[5,6,3,8,-4,10],[-4,-10,-5,-5,-7,10],[7,5,2,-10,8,-9],[-4,10,5,9,-1,2],[3,-2,10,-10,-1,1],[-1,-2,-7,-9,-8,-8],[9,4,-6,7,6,4],[5,-3,8,-10,4,-5],[5,-3,3,5,1,-1],[6,6,1,-7,3,5],[-3,8,8,-2,9,3],[-9,3,10,4,-6,-7]], dtype = "uint64")#candidate|5019|(49, 6)|const|uint64
call_5016 = relay.TupleGetItem(func_3668_call(relay.reshape(var_5017.astype('uint16'), [10, 4, 15]), relay.reshape(var_5017.astype('uint16'), [10, 4, 15]), relay.reshape(const_5018.astype('float64'), [5, 78]), relay.reshape(call_5003.astype('uint64'), []), relay.reshape(const_4916.astype('int32'), [105,]), relay.reshape(const_5019.astype('uint64'), [294,]), ), 3)
call_5020 = relay.TupleGetItem(func_3676_call(relay.reshape(var_5017.astype('uint16'), [10, 4, 15]), relay.reshape(var_5017.astype('uint16'), [10, 4, 15]), relay.reshape(const_5018.astype('float64'), [5, 78]), relay.reshape(call_5003.astype('uint64'), []), relay.reshape(const_4916.astype('int32'), [105,]), relay.reshape(const_5019.astype('uint64'), [294,]), ), 3)
output = relay.Tuple([bop_4956,call_4978,bop_5000,call_5003,var_5004,var_5005,const_5006,const_5007,var_5008,call_5016,var_5017,const_5018,const_5019,])
output2 = relay.Tuple([bop_4956,call_4979,bop_5000,call_5009,var_5004,var_5005,const_5006,const_5007,var_5008,call_5020,var_5017,const_5018,const_5019,])
func_5028 = relay.Function([var_4915,var_4955,var_5004,var_5005,var_5008,var_5017,], output)
mod['func_5028'] = func_5028
mod = relay.transform.InferType()(mod)
mutated_mod['func_5028'] = func_5028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5028_call = mutated_mod.get_global_var('func_5028')
var_5030 = relay.var("var_5030", dtype = "uint16", shape = (7, 3, 5))#candidate|5030|(7, 3, 5)|var|uint16
var_5031 = relay.var("var_5031", dtype = "float32", shape = (7, 3, 5))#candidate|5031|(7, 3, 5)|var|float32
var_5032 = relay.var("var_5032", dtype = "float64", shape = (480,))#candidate|5032|(480,)|var|float64
var_5033 = relay.var("var_5033", dtype = "float32", shape = (495,))#candidate|5033|(495,)|var|float32
var_5034 = relay.var("var_5034", dtype = "int64", shape = (40,))#candidate|5034|(40,)|var|int64
var_5035 = relay.var("var_5035", dtype = "uint16", shape = (600,))#candidate|5035|(600,)|var|uint16
call_5029 = func_5028_call(var_5030,var_5031,var_5032,var_5033,var_5034,var_5035,)
output = call_5029
func_5036 = relay.Function([var_5030,var_5031,var_5032,var_5033,var_5034,var_5035,], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5521 = relay.var("var_5521", dtype = "int32", shape = (13, 4, 13))#candidate|5521|(13, 4, 13)|var|int32
const_5522 = relay.const([[[3,6,-9,9,9,7,-1,8,-6,-3,-7,-6,-7],[-6,4,-8,-4,-2,3,-10,1,4,2,9,2,10],[-1,2,-1,-6,6,3,-8,2,-6,-4,10,6,9],[-9,-9,8,-3,7,-9,-10,-7,-5,-8,6,1,-9]],[[-5,2,-2,5,-10,-1,-5,9,-3,1,4,3,-4],[3,9,6,-1,-10,-9,-6,9,-4,-8,-10,-3,-1],[10,-6,4,-2,5,9,-6,1,-3,4,4,6,-10],[3,1,10,-9,-6,10,-6,-5,1,3,5,-8,-9]],[[7,-4,-4,-2,-10,-6,1,-2,9,-5,2,-6,-9],[10,-1,10,4,5,-1,-5,-7,8,3,10,7,-8],[1,-3,-6,8,3,3,1,7,3,1,-1,10,10],[-7,5,-5,1,9,-2,-3,6,-2,6,-7,1,10]],[[8,7,-2,-6,-2,-5,10,10,-2,8,-1,-5,10],[-5,-9,-3,7,-8,6,5,-6,1,-6,-1,-6,-6],[-7,-5,2,-8,-8,-1,-2,-3,-2,8,-3,-5,2],[7,3,6,-4,-1,-2,7,-1,-5,7,5,10,-7]],[[-2,2,-8,-3,-4,-5,1,-5,6,-5,2,1,-1],[9,8,6,10,-6,-9,-3,10,-3,3,-6,-2,5],[-2,-3,3,-4,-8,4,10,-8,1,-4,-1,-3,-5],[-5,-9,-8,7,2,3,-4,8,-1,-8,-9,-2,1]],[[10,-8,-3,9,-3,1,-10,1,-2,-6,-3,-1,8],[1,5,-3,-5,9,4,-10,-6,-7,5,-10,5,9],[3,-8,-2,-10,2,-3,4,5,-1,-3,7,5,-1],[10,1,3,-3,-6,1,-3,7,10,-7,9,3,7]],[[3,-1,-7,2,4,1,-8,2,2,2,1,-3,10],[-8,-6,-2,-5,5,6,9,3,-7,8,10,-5,1],[8,-6,-6,3,9,10,8,5,3,6,-5,-6,-4],[-3,1,-7,-8,7,-7,-7,-6,10,4,-10,1,-4]],[[-10,-9,7,3,6,6,1,1,4,4,-4,-3,-2],[-7,10,-9,-2,-7,10,6,10,-1,5,-10,-9,8],[1,-4,-6,-7,-4,1,3,-4,5,-1,2,-7,4],[-4,4,-8,3,9,5,-8,-10,-5,-6,-8,-9,-8]],[[-10,5,-2,9,-1,10,-1,7,-5,-6,-5,-8,10],[-2,4,9,4,-10,-3,2,-7,1,-3,7,3,-3],[-4,9,-8,2,-10,-7,-3,3,-7,-1,9,-4,8],[10,-5,-2,-3,-1,-10,2,4,-6,-6,4,-4,-10]],[[6,-7,5,10,8,9,10,2,-4,2,4,6,5],[-3,-6,-3,-9,1,-6,6,-10,7,6,10,6,10],[9,1,-8,4,9,8,-6,2,7,-7,-2,7,-8],[9,-10,-5,9,-3,-10,2,-2,5,-9,-1,-2,5]],[[7,-3,-2,10,-3,9,10,-10,-8,-10,-3,10,2],[2,2,-10,-1,3,-5,-5,7,-2,-7,5,-5,8],[10,1,9,-7,-3,9,10,-7,-4,-5,8,8,-8],[-1,-10,10,-6,3,6,-6,7,-3,9,1,-4,-6]],[[2,10,-1,-2,9,-2,-4,-10,-4,-9,4,-7,-4],[8,-5,-2,10,-6,2,-1,-3,-6,7,9,-4,4],[2,3,-2,-6,3,1,-10,4,8,-3,-6,7,-8],[-9,-7,-2,-6,7,-4,-4,-8,2,-3,-2,-2,1]],[[-5,-3,7,5,7,-4,-2,3,-3,7,-2,-1,-5],[-8,-5,5,9,3,2,-1,7,5,8,7,5,-3],[5,5,-5,7,2,-2,-3,-7,6,5,-5,5,8],[-7,8,-1,-3,2,-9,-10,2,10,-10,10,6,9]]], dtype = "int32")#candidate|5522|(13, 4, 13)|const|int32
bop_5523 = relay.left_shift(var_5521.astype('int32'), relay.reshape(const_5522.astype('int32'), relay.shape_of(var_5521))) # shape=(13, 4, 13)
output = bop_5523
output2 = bop_5523
func_5526 = relay.Function([var_5521,], output)
mod['func_5526'] = func_5526
mod = relay.transform.InferType()(mod)
mutated_mod['func_5526'] = func_5526
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5527 = relay.var("var_5527", dtype = "int32", shape = (13, 4, 13))#candidate|5527|(13, 4, 13)|var|int32
func_5526_call = mutated_mod.get_global_var('func_5526')
call_5528 = func_5526_call(var_5527)
output = call_5528
func_5529 = relay.Function([var_5527], output)
mutated_mod['func_5529'] = func_5529
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5539 = relay.var("var_5539", dtype = "float32", shape = (14, 8, 8))#candidate|5539|(14, 8, 8)|var|float32
var_5540 = relay.var("var_5540", dtype = "float32", shape = (14, 8, 8))#candidate|5540|(14, 8, 8)|var|float32
bop_5541 = relay.mod(var_5539.astype('float32'), relay.reshape(var_5540.astype('float32'), relay.shape_of(var_5539))) # shape=(14, 8, 8)
output = bop_5541
output2 = bop_5541
func_5550 = relay.Function([var_5539,var_5540,], output)
mod['func_5550'] = func_5550
mod = relay.transform.InferType()(mod)
var_5551 = relay.var("var_5551", dtype = "float32", shape = (14, 8, 8))#candidate|5551|(14, 8, 8)|var|float32
var_5552 = relay.var("var_5552", dtype = "float32", shape = (14, 8, 8))#candidate|5552|(14, 8, 8)|var|float32
output = func_5550(var_5551,var_5552,)
func_5553 = relay.Function([var_5551,var_5552,], output)
mutated_mod['func_5553'] = func_5553
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5573 = relay.var("var_5573", dtype = "float64", shape = (2, 8, 7))#candidate|5573|(2, 8, 7)|var|float64
var_5574 = relay.var("var_5574", dtype = "float64", shape = (2, 8, 7))#candidate|5574|(2, 8, 7)|var|float64
bop_5575 = relay.mod(var_5573.astype('float64'), relay.reshape(var_5574.astype('float64'), relay.shape_of(var_5573))) # shape=(2, 8, 7)
uop_5578 = relay.exp(var_5573.astype('float32')) # shape=(2, 8, 7)
func_1006_call = mod.get_global_var('func_1006')
func_1009_call = mutated_mod.get_global_var('func_1009')
var_5590 = relay.var("var_5590", dtype = "uint64", shape = (1350,))#candidate|5590|(1350,)|var|uint64
call_5589 = relay.TupleGetItem(func_1006_call(relay.reshape(var_5590.astype('uint64'), [15, 9, 10]), relay.reshape(var_5590.astype('uint64'), [15, 9, 10]), ), 1)
call_5591 = relay.TupleGetItem(func_1009_call(relay.reshape(var_5590.astype('uint64'), [15, 9, 10]), relay.reshape(var_5590.astype('uint64'), [15, 9, 10]), ), 1)
output = relay.Tuple([bop_5575,uop_5578,call_5589,var_5590,])
output2 = relay.Tuple([bop_5575,uop_5578,call_5591,var_5590,])
func_5598 = relay.Function([var_5573,var_5574,var_5590,], output)
mod['func_5598'] = func_5598
mod = relay.transform.InferType()(mod)
var_5599 = relay.var("var_5599", dtype = "float64", shape = (2, 8, 7))#candidate|5599|(2, 8, 7)|var|float64
var_5600 = relay.var("var_5600", dtype = "float64", shape = (2, 8, 7))#candidate|5600|(2, 8, 7)|var|float64
var_5601 = relay.var("var_5601", dtype = "uint64", shape = (1350,))#candidate|5601|(1350,)|var|uint64
output = func_5598(var_5599,var_5600,var_5601,)
func_5602 = relay.Function([var_5599,var_5600,var_5601,], output)
mutated_mod['func_5602'] = func_5602
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5618 = relay.var("var_5618", dtype = "float32", shape = (2, 15, 9))#candidate|5618|(2, 15, 9)|var|float32
uop_5619 = relay.asin(var_5618.astype('float32')) # shape=(2, 15, 9)
output = uop_5619
output2 = uop_5619
func_5627 = relay.Function([var_5618,], output)
mod['func_5627'] = func_5627
mod = relay.transform.InferType()(mod)
mutated_mod['func_5627'] = func_5627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5628 = relay.var("var_5628", dtype = "float32", shape = (2, 15, 9))#candidate|5628|(2, 15, 9)|var|float32
func_5627_call = mutated_mod.get_global_var('func_5627')
call_5629 = func_5627_call(var_5628)
output = call_5629
func_5630 = relay.Function([var_5628], output)
mutated_mod['func_5630'] = func_5630
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5697 = relay.var("var_5697", dtype = "uint32", shape = (11, 11, 3))#candidate|5697|(11, 11, 3)|var|uint32
const_5698 = relay.const([[[10,8,5],[7,10,2],[-2,-2,7],[8,-1,7],[-6,7,-4],[7,-6,-7],[-1,-6,2],[5,-10,8],[10,-7,-6],[-4,-1,6],[-7,-1,-9]],[[1,5,-9],[7,9,-4],[5,3,-7],[-8,1,-4],[-7,9,-4],[-4,-10,-4],[6,-6,1],[9,4,-9],[1,1,-7],[9,6,1],[10,-6,-6]],[[1,4,-4],[7,-10,-9],[1,-8,-2],[-7,-10,10],[-2,-7,-1],[9,-5,-7],[-7,-4,7],[-9,3,-1],[4,-7,1],[-4,-10,-3],[3,10,6]],[[-7,-4,-1],[-6,9,10],[6,8,-6],[3,-3,-2],[3,-8,-5],[4,7,-5],[-9,3,-2],[-10,4,-4],[-8,-4,-1],[9,2,-8],[-4,-9,10]],[[-3,6,-9],[-6,-7,-8],[5,-1,10],[5,-7,-9],[-6,-5,5],[-10,6,-2],[-4,-5,-3],[3,10,-6],[5,10,-8],[7,3,8],[9,4,-4]],[[10,7,9],[10,-7,-8],[-1,-6,-5],[9,10,-3],[-9,8,8],[2,-10,-5],[10,-4,6],[-3,5,5],[4,1,7],[2,-8,9],[-2,6,-1]],[[-2,-8,9],[-6,-8,-10],[10,-8,-7],[9,-1,2],[5,-1,6],[3,3,4],[-3,4,1],[6,-9,-6],[-1,8,4],[-2,-1,-1],[6,-5,-5]],[[-1,-9,-2],[1,4,4],[6,7,-9],[-3,-1,5],[3,5,-10],[-7,9,-8],[-8,8,-8],[-4,-10,-10],[3,10,-8],[-5,6,-1],[8,-1,-5]],[[7,7,7],[-10,2,3],[6,5,-1],[1,-8,-6],[7,-6,-3],[7,-6,7],[-4,6,6],[-9,-7,-8],[-1,-4,10],[-5,-4,-5],[-4,8,7]],[[-3,4,-6],[-9,1,-1],[-4,-10,9],[-6,6,7],[-8,-4,-9],[4,3,-9],[8,-5,-4],[10,9,4],[-1,-2,4],[-10,10,-1],[-4,-1,4]],[[-7,-10,1],[-9,9,4],[-5,8,4],[9,-4,-6],[8,-1,9],[10,8,-6],[-3,-2,2],[10,1,-7],[7,6,6],[6,4,-4],[-3,-8,-6]]], dtype = "uint32")#candidate|5698|(11, 11, 3)|const|uint32
bop_5699 = relay.add(var_5697.astype('uint32'), relay.reshape(const_5698.astype('uint32'), relay.shape_of(var_5697))) # shape=(11, 11, 3)
func_1354_call = mod.get_global_var('func_1354')
func_1360_call = mutated_mod.get_global_var('func_1360')
const_5706 = relay.const([-6.005330,5.018840,4.088806,1.859809,-4.350898,7.117844,-0.837447,-6.646076,9.243962,6.662669,-1.361540,-4.140158,8.122554,-7.707613,-4.712760,1.137177,-0.290335,-9.701343,6.254929,4.367703,-2.458177,3.647427,4.731830,0.733521,-8.138199,-1.217532,6.942781,-9.683093,-9.370805,2.495764,-1.653888,2.793394,3.953301,-5.761901,-1.588750,-1.437393,-4.174493,6.210411,9.053905,-5.047462,4.997768,-4.738738,5.572823,8.553818,5.747296,-0.758367,4.503737,-0.327229,5.601561,0.132817,-7.108586,2.637009,5.037966,1.147554,4.920153,5.510062,-1.631614,2.851968,-6.187647,-8.393487,5.198119,6.557917,-0.602639], dtype = "float32")#candidate|5706|(63,)|const|float32
const_5707 = relay.const([0.730254,-7.950074,-3.297228,-2.538016,-0.709650,-2.344689,-5.576783,-8.426060,-1.875259,1.763725,-6.708920,-7.386632,2.299721,-3.749474,-6.514074,-1.942196,6.672783,-3.957028,-9.630870,4.042911,-7.442737,-5.813648,6.927759,-0.697840,-2.089335,-6.805749,-2.957715,-1.318486,8.763103,-8.605454,-1.884312,-5.891489,8.356427,-8.032692,4.819589,3.471227,3.141534,-2.103318,-0.921583,-4.659660,-6.022235,4.512534,3.969453,0.843492,-0.805462,3.617558,-3.444674,9.031399,-7.360252,7.746621,1.144560,-3.111595,0.141360,6.265590,1.180853,-2.423220,-2.573641,5.182326,5.191511,5.830805,-2.350799,1.629445,-6.633743,0.857385,-4.490101,-6.439967,0.999359,-1.706048,4.739518,-8.692343,7.120076,5.502287,-9.969330,-4.884540,7.713057,-7.226647,-8.590753,-7.025084,-9.702002,7.051456,-1.430551,-7.135803,-5.753579,-6.769799,6.993188,0.859623,2.731270,-1.408089,0.573236,-0.407649,-8.813616,-5.518191,-1.288974,6.498255,-9.197804,2.338141,-2.549938,-0.739758,-2.921894,9.754081,7.167828,-9.526826,8.946237,7.940635,0.176987,2.743291,-0.095902,-7.917461,-6.488694,7.005677,7.153954,8.362654,-9.449059,-6.005677,5.891410,-8.439537,-2.870328,6.306389,-2.697606,-7.986964,-1.009475,8.494967,-5.586301,1.304911,-1.813733,0.929798,6.207190,0.966942,2.705992,-6.786097,8.009958,0.448146,-5.903331,4.745100,7.746239,-7.700374,9.984670,-2.503042,-8.006969,-3.507727,-9.879613,-1.331834,7.371333,-4.559747,2.692329,2.885976,5.080893,0.392737,0.244090,-9.980902,-7.029471,2.340632,6.867576,7.974118,5.223161,-6.127707,-3.332092,-6.476171,-6.883550,-5.781391,5.966508,0.491003,-9.359537,-2.269875,5.343527,8.487694,-9.563079,-6.558045,-1.334272,3.629946,9.899822,-5.902017,-9.824337,7.030956,4.772623,-1.335190,8.082479,2.822227,-4.236352,-2.566778,0.731648,-7.984555,-8.300462,4.678879,-0.352328,-2.934457,-7.238601,4.028066,3.024025,6.744460,-6.739110,-7.260400,7.570576,-1.226086,9.754036,-3.307679,-4.146081,-1.945634,3.236676,9.512546,-0.861273,9.156516,-6.081795,1.865966,-6.270891,-4.157276,2.747042,-0.596510,0.768768,-0.840835,7.562938,0.091281,4.282604,-4.049349,0.794979,6.439827,-0.945008,-2.741941,8.447820,-1.897991,-9.888521,4.020464,1.050322,5.157675,-2.802884,-9.768890,-6.925182,1.027510,7.786156,-1.708236,9.773422,3.492563,-4.732104,2.961445,4.592586,5.936511,-3.347565,0.829421,4.778540,-3.639325,2.534500,9.494187,-9.566948,0.582485,2.041854,-0.648965,7.054431,-0.967188,3.518709,-2.194330,7.959433,4.223969,-1.473479,-1.556175,8.254802,0.338658,0.076743,-2.215757,1.975308,4.118223,8.319310,3.730773,9.324060,-9.516639,1.878415,-1.339662,7.662392,5.642276,-8.965094,4.518805,-1.268433,-0.762234,5.416674,-3.825996,6.526376,1.526896,9.030736,6.256516,-5.654477,-9.535977,-6.385315,8.595247,-1.234747,3.003514,-1.040248,-6.686940,5.779445,-1.777567,0.926202,1.735592,-0.421735,7.847409,-9.187151,6.482044,-8.179235,-1.248331,-9.414381,-8.423780,-8.273701,3.612944,-3.992916,-0.537251,4.890676,1.249406,8.916251,4.560191,9.630758,6.780590,7.225833,2.056417,-5.444063,4.942632,3.452791,0.820293,4.616604], dtype = "float32")#candidate|5707|(315,)|const|float32
var_5708 = relay.var("var_5708", dtype = "int32", shape = (7, 15))#candidate|5708|(7, 15)|var|int32
const_5709 = relay.const(-4, dtype = "uint32")#candidate|5709|()|const|uint32
var_5710 = relay.var("var_5710", dtype = "float32", shape = (336,))#candidate|5710|(336,)|var|float32
call_5705 = relay.TupleGetItem(func_1354_call(relay.reshape(const_5706.astype('float32'), [9, 1, 7]), relay.reshape(const_5707.astype('float32'), [9, 5, 7]), relay.reshape(var_5708.astype('int32'), [105, 1]), relay.reshape(const_5709.astype('uint32'), []), relay.reshape(var_5710.astype('float32'), [336,]), ), 6)
call_5711 = relay.TupleGetItem(func_1360_call(relay.reshape(const_5706.astype('float32'), [9, 1, 7]), relay.reshape(const_5707.astype('float32'), [9, 5, 7]), relay.reshape(var_5708.astype('int32'), [105, 1]), relay.reshape(const_5709.astype('uint32'), []), relay.reshape(var_5710.astype('float32'), [336,]), ), 6)
bop_5717 = relay.floor_mod(const_5706.astype('float64'), const_5709.astype('float64')) # shape=(63,)
bop_5721 = relay.floor_divide(var_5710.astype('float64'), relay.reshape(call_5705.astype('float64'), relay.shape_of(var_5710))) # shape=(336,)
bop_5724 = relay.floor_divide(var_5710.astype('float64'), relay.reshape(call_5711.astype('float64'), relay.shape_of(var_5710))) # shape=(336,)
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
call_5741 = relay.TupleGetItem(func_411_call(relay.reshape(var_5708.astype('int32'), [105,])), 0)
call_5742 = relay.TupleGetItem(func_413_call(relay.reshape(var_5708.astype('int32'), [105,])), 0)
output = relay.Tuple([bop_5699,const_5707,var_5708,bop_5717,bop_5721,call_5741,])
output2 = relay.Tuple([bop_5699,const_5707,var_5708,bop_5717,bop_5724,call_5742,])
func_5756 = relay.Function([var_5697,var_5708,var_5710,], output)
mod['func_5756'] = func_5756
mod = relay.transform.InferType()(mod)
mutated_mod['func_5756'] = func_5756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5756_call = mutated_mod.get_global_var('func_5756')
var_5758 = relay.var("var_5758", dtype = "uint32", shape = (11, 11, 3))#candidate|5758|(11, 11, 3)|var|uint32
var_5759 = relay.var("var_5759", dtype = "int32", shape = (7, 15))#candidate|5759|(7, 15)|var|int32
var_5760 = relay.var("var_5760", dtype = "float32", shape = (336,))#candidate|5760|(336,)|var|float32
call_5757 = func_5756_call(var_5758,var_5759,var_5760,)
output = call_5757
func_5761 = relay.Function([var_5758,var_5759,var_5760,], output)
mutated_mod['func_5761'] = func_5761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5775 = relay.var("var_5775", dtype = "float32", shape = (9, 5))#candidate|5775|(9, 5)|var|float32
uop_5776 = relay.erf(var_5775.astype('float32')) # shape=(9, 5)
output = uop_5776
output2 = uop_5776
func_5783 = relay.Function([var_5775,], output)
mod['func_5783'] = func_5783
mod = relay.transform.InferType()(mod)
mutated_mod['func_5783'] = func_5783
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5784 = relay.var("var_5784", dtype = "float32", shape = (9, 5))#candidate|5784|(9, 5)|var|float32
func_5783_call = mutated_mod.get_global_var('func_5783')
call_5785 = func_5783_call(var_5784)
output = call_5785
func_5786 = relay.Function([var_5784], output)
mutated_mod['func_5786'] = func_5786
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5829 = relay.var("var_5829", dtype = "float64", shape = (3, 12, 1))#candidate|5829|(3, 12, 1)|var|float64
uop_5830 = relay.rsqrt(var_5829.astype('float64')) # shape=(3, 12, 1)
output = uop_5830
output2 = uop_5830
func_5840 = relay.Function([var_5829,], output)
mod['func_5840'] = func_5840
mod = relay.transform.InferType()(mod)
var_5841 = relay.var("var_5841", dtype = "float64", shape = (3, 12, 1))#candidate|5841|(3, 12, 1)|var|float64
output = func_5840(var_5841)
func_5842 = relay.Function([var_5841], output)
mutated_mod['func_5842'] = func_5842
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5846 = relay.const([[[-2.583236,-2.121860,-8.682613,4.263508,-1.096347,-3.034672,-2.311857,-6.805744,-7.818395],[-8.354191,-9.081725,8.743494,3.010533,-4.043150,6.239816,-3.995375,3.692154,-1.120703],[-3.707212,7.005453,-3.753203,0.300135,2.109281,-7.052263,-0.097803,2.300895,3.972253],[5.274758,-5.457679,1.591100,0.456971,4.401361,3.612435,-1.426837,-6.340917,-6.984492]],[[1.461418,7.334003,2.243579,-7.222931,-9.680496,0.220803,-2.680097,-6.563123,-4.047977],[-6.586605,-3.203037,-8.252159,6.560905,2.474034,-9.082870,-6.829004,3.873173,-1.950122],[2.007523,5.421540,-5.619038,0.537177,4.364368,-7.644958,-5.780262,-6.989314,-6.913010],[-0.031877,2.420101,5.475916,7.670530,-5.446538,-2.671613,5.604164,7.609274,6.075481]],[[2.512188,4.756832,8.744096,-5.444793,-9.631740,-8.723648,9.230150,9.890999,-2.211116],[-8.815111,-6.150413,-0.949109,2.121123,9.066364,-9.510724,3.600664,9.518349,2.419485],[-3.106501,-8.382672,-6.210006,5.914704,5.622642,-0.576733,-1.855524,1.927210,3.044538],[1.723574,-4.412870,-3.893949,7.845942,-9.784755,-9.485716,7.202992,-3.266370,7.865524]],[[-9.493209,-0.190555,5.440497,6.509985,-1.542144,3.749923,5.897484,-1.951549,4.612189],[-7.960281,-1.031118,2.663387,-0.629282,4.242169,5.709646,1.888130,-1.158941,4.392995],[4.349511,4.358053,-2.486928,0.803481,8.826600,2.868496,-1.817413,7.006626,-9.060325],[1.502156,-7.776802,1.770232,-5.475305,2.187353,1.351709,-4.927068,-3.235209,-5.334056]]], dtype = "float64")#candidate|5846|(4, 4, 9)|const|float64
var_5847 = relay.var("var_5847", dtype = "float64", shape = (4, 4, 9))#candidate|5847|(4, 4, 9)|var|float64
bop_5848 = relay.less(const_5846.astype('bool'), relay.reshape(var_5847.astype('bool'), relay.shape_of(const_5846))) # shape=(4, 4, 9)
func_1874_call = mod.get_global_var('func_1874')
func_1877_call = mutated_mod.get_global_var('func_1877')
const_5855 = relay.const(False, dtype = "bool")#candidate|5855|()|const|bool
var_5856 = relay.var("var_5856", dtype = "bool", shape = (44,))#candidate|5856|(44,)|var|bool
call_5854 = relay.TupleGetItem(func_1874_call(relay.reshape(const_5855.astype('bool'), []), relay.reshape(var_5856.astype('bool'), [1, 4, 11]), ), 0)
call_5857 = relay.TupleGetItem(func_1877_call(relay.reshape(const_5855.astype('bool'), []), relay.reshape(var_5856.astype('bool'), [1, 4, 11]), ), 0)
func_5526_call = mod.get_global_var('func_5526')
func_5529_call = mutated_mod.get_global_var('func_5529')
var_5865 = relay.var("var_5865", dtype = "int32", shape = (676,))#candidate|5865|(676,)|var|int32
call_5864 = func_5526_call(relay.reshape(var_5865.astype('int32'), [13, 4, 13]))
call_5866 = func_5526_call(relay.reshape(var_5865.astype('int32'), [13, 4, 13]))
func_411_call = mod.get_global_var('func_411')
func_413_call = mutated_mod.get_global_var('func_413')
const_5868 = relay.const([8,3,8,5,8,-9,-10,5,-4,-9,8,2,3,-7,8,1,2,5,-8,6,-8,8,5,-1,4,8,6,-7,4,5,-4,7,10,5,-6,-5,7,2,9,-1,-3,-8,-8,7,-8,3,9,-7,-6,7,5,-4,-7,4,-10,-10,1,2,-10,-3,-9,10,8,7,10,-6,7,-5,8,10,-2,1,-6,-5,9,-7,-6,-8,-2,8,8,7,6,10,1,2,-10,-1,3,5,3,2,-6,-4,5,2,-8,9,-1,9,-10,-7,3,9,3], dtype = "int32")#candidate|5868|(105,)|const|int32
call_5867 = relay.TupleGetItem(func_411_call(relay.reshape(const_5868.astype('int32'), [105,])), 4)
call_5869 = relay.TupleGetItem(func_413_call(relay.reshape(const_5868.astype('int32'), [105,])), 4)
var_5871 = relay.var("var_5871", dtype = "bool", shape = (44,))#candidate|5871|(44,)|var|bool
bop_5872 = relay.bitwise_and(var_5856.astype('int64'), relay.reshape(var_5871.astype('int64'), relay.shape_of(var_5856))) # shape=(44,)
uop_5876 = relay.exp(var_5865.astype('float32')) # shape=(676,)
bop_5907 = relay.logical_xor(call_5867.astype('int16'), const_5855.astype('int16')) # shape=(1, 15, 7)
bop_5910 = relay.logical_xor(call_5869.astype('int16'), const_5855.astype('int16')) # shape=(1, 15, 7)
func_5840_call = mod.get_global_var('func_5840')
func_5842_call = mutated_mod.get_global_var('func_5842')
var_5925 = relay.var("var_5925", dtype = "float64", shape = (36,))#candidate|5925|(36,)|var|float64
call_5924 = func_5840_call(relay.reshape(var_5925.astype('float64'), [3, 12, 1]))
call_5926 = func_5840_call(relay.reshape(var_5925.astype('float64'), [3, 12, 1]))
func_1640_call = mod.get_global_var('func_1640')
func_1643_call = mutated_mod.get_global_var('func_1643')
var_5929 = relay.var("var_5929", dtype = "float32", shape = (165, 3))#candidate|5929|(165, 3)|var|float32
call_5928 = relay.TupleGetItem(func_1640_call(relay.reshape(var_5929.astype('float32'), [15, 11, 3])), 0)
call_5930 = relay.TupleGetItem(func_1643_call(relay.reshape(var_5929.astype('float32'), [15, 11, 3])), 0)
bop_5935 = relay.not_equal(call_5928.astype('bool'), const_5855.astype('bool')) # shape=(15, 11, 3)
bop_5938 = relay.not_equal(call_5930.astype('bool'), const_5855.astype('bool')) # shape=(15, 11, 3)
func_3234_call = mod.get_global_var('func_3234')
func_3239_call = mutated_mod.get_global_var('func_3239')
var_5943 = relay.var("var_5943", dtype = "float32", shape = (750,))#candidate|5943|(750,)|var|float32
const_5944 = relay.const([-7,10,6,7,-1,8,-10,6,-7,-5,-4,-4,-10,5,-5,2,1,-1,10,-3,-7,-4,5,3,5,-2,-4,10,-7,7,-7,5,-10,5,6,-10,6,-2,-6,-2,2,9,-2,9,4,-1,-6,9,5,-8,9,-6,2,7,-2,10,-2,-1,10,4,-7,-2,-5,8,4,-3,-4,9,8,7,-4,-5,5,-3,-5,8,-5,-2,3,10,-10,2,3,-1,9,10,-4,-2,-10,-6,5,6,4,10,-10,7,-3,-3,4,7,1,-9,-2,-3,-9,9,3,-3,3,-6,-4,-4,-6,3,-10,-3,8,5,-4,-4,7,6,9,7,-3,-7,-8,3,-8,1,-7,-1,8,-4,-6], dtype = "int16")#candidate|5944|(135,)|const|int16
const_5945 = relay.const([4,-3,5,4,-5,-4,-2,4,-5,9,3,4,-8,6,-9,-7,-6,-7,-2,-8,4,9,-1,5,2,-8,6,6,2,-7,-5,-5,9,-4,5,-10,-6,-4,-6,4,2,2,-6,3,-2,-1,9,8,10,-10,5,-3,-1,-9,5,-4,7,-7,8,-1,2,-5,-7,-6,-8,3,6,-4,10,-3,-1,2,-7,-1,10,-3,-1,1,3,7,6,5,-4,1,4,-1,-3,5,3,-2,5,3,-6,-5,4,2,-2,1,6,1,6,-9,4,-8,7,8,-5,-9,7,-10,6,10,9,-5,3,-8,-10,9,-8,-1,-7,6,-3,-5,-9,-9,6,-4,-1,1,6,5,6,-2,-1,7,3,9,8,-6,8,-1,-5,3,-5,9,6,9,-8,-4,3,4,-7,-4,9,-2,-3,5,-8,-3,-5,-6,6,2,-4,2,10,-3,-3,1,-7,10,8,8,-4,-10,-5,9,-10,7,9,-1,-7,5,-3,1,1,-10,9,-4,-10,3,9,-9,4,2,7,-10,10,-6,4,-1,-1,4,10,4,-4,-5,8,3,2,-5,1,-3,3,-1,7,3,-4,7,-9,-4,-7,-6,-5,-6,6,-3,-7,7,-6,-8,-2,-2,-10,-2,1,1,-7,2,8,8,-1,1,9,-9,-6,-9,-8,7,-1,8,-5,1,-6,3,-5,9,1,-4,-10,7,-10,8,-1,-7,-2,-6,1,-8,-2,-4,3,3,-7,-6,9,-7,-4,-6,-8,7,5,-10,3,-7,10,-4,-7,6,-3,1,8,1,-2,6,10,-1,-1,5,-8,10,4,-10,-10,-4,-9,-7,4,-10,6,6,3,5,10,-9,10,8,-3,4,-5,8,-5,4,4,-6,1,-8,-1,8,3,-2,7,7,-8,-7,1,-8,2,-6,5,-9,-5,-3,-2,-10,8,-5,3,7,7,6,-9,6,6,10,-5,-10,-5,-7,-3,9,-8,-8,-10,-2,-1,5,-3,-1,-5,4,9,-8,-8,9,-1,-5,-5,-2,10,-2,-4,-10,1,8,4,4,10,8,-7,1,9,9,-1,-1,-6,-1,-1,7,-6,-8,9,-6,3,6,2,10,-3,5,1,-4,-10,-5,-10,5,-9,8,2,-8,-7,7,-2,-3,5,9,-6,2,2,7,10,-9,4,9,-1,-2,-3,-2,-5,10,-2,7,5,-4,-7,-8,2,7,7,3,-5,8,4,-3,-4,-1,3,6,5,5,-2,8,2,-1,3,7,-7,-6,-7,-1,1,9,10,-1,7,7,-9,-5,-4,10,-8,-7,-3,7,-3,1,10,7,-9,-5,2,-6,-8,-2,7,2,-10,-2,2,-3,8,9,7,-8,-4,-1,-6,7,-9,-8,2,2,7,-5,3,-5,3,9,-10,6,-9,-10,5,-8,-10,-3,-6,-4,-10,3,-8,-6,-2,3,-3,6,8,-8,-5,1,5,-8,10,-4,-3,-6,5,4,-9,7,-9,-4,1,2,-10,-1,-5,-6,9,7,-6,4,5,9,6,3,-1,2,1,-7,-5,8,5,8,3,-7,6,-10,-9,4,5,3,-8,-7,9,2,2,7,-3,3,-10,-4,-2,-9,3,8,-3,-5,8,-10,10,2,-9,9,-5,7,-3,-2,-5,-7,4,-10,8,6,9,-2,5,1,4,7,2,-5,-4,1,-5,2,4,6,7,-10,5,7,8,5,8,3,7,7,4,3,-6,9,-6,6,5,10,-7,-2,-5,-1,1,4,-2,9,9,-5,8,-9,-9,8,8,-7,-4,-4,-8,-1,10,8,6,-8,-3,2,-9,6,5], dtype = "int16")#candidate|5945|(675,)|const|int16
const_5946 = relay.const([9.325608,5.410558,0.444320,-8.870938,2.506911,-2.798129,-3.769711,-1.906058,8.485653,-7.275293,0.275618,2.678430,-5.568122,-8.508405,3.117824,-1.566413,-6.368756,-6.155246,2.313623,5.657390,-5.882662,-4.687176,2.303149,-6.215175,0.587378,-3.745679,-6.451822,4.053251,-6.045273,-5.628723,-6.424536,-7.023692,-7.653636,0.335250,6.945819,-9.136944,-0.404782,-5.978536,0.708889,4.768658,-4.939220,2.911013,6.345084,7.290979,5.809711,6.855788,-3.796578,-2.411390,1.247467,7.151166,-5.484468,-7.451242,-8.426831,-9.493806,5.612129,2.353025,8.033300,-0.913778,3.500413,-5.605073,9.397319,0.389544,7.223882,-2.625472,7.723187,-1.779556,-0.036857,-5.835202,8.357887,-9.541063,-9.884400,-7.081422,0.113380,-4.633658,4.785098,5.847178,8.316317,-7.647956,-5.104120,2.273918,-2.325583,-5.508441,-5.308207,-6.752323,5.841765,-8.383720,-1.079320,-9.656402,1.424043,-0.091011,3.477673,3.741996,-2.902202,-7.371170,-5.364953,-3.950449,8.334909,0.430216,-9.605725,6.242449,3.855251,1.189093,6.926778,6.244927,5.415855,6.999539,4.453372,2.499484,-9.205666,-9.157174,7.560972,-8.057175,7.835788,-7.857363,4.618529,-4.152230,4.543749,-4.502548,1.467916,0.357623,1.855595,3.991346,7.481714,4.430956,-0.851590,-5.306595,-0.038124,-1.409293,5.795492,4.328116,3.393318,3.005058,-0.167139,2.470342,8.570297,-6.450291,6.594791,5.573953,-1.366719,-0.175851,-1.036100,-4.858439,4.551026,6.882448,0.052344,0.415827,-0.755991,3.211531,-5.621462,-2.784167,7.614324,6.797863,-7.634028,5.919686,7.535308,-1.611010,-0.899517,-8.714926,7.349382,-5.138186,4.353954,5.918671,-2.061109,-6.794859,5.806845,-5.597698,7.403119,4.683299,-5.270181,-8.692242,4.439158,-8.993055,6.311504,0.161390,-1.709485,9.362973,-1.443368,7.815816,2.958770,4.581967,-2.114660,9.109507,2.503842,4.846503,4.036820,2.018165,-3.883621,-5.308840,7.167372,3.358025,-2.246883,6.361636,6.518097,9.734664,-3.558818,-7.989304,4.883291,-0.565466,-5.567143,-8.346095,5.011170,-3.239088,9.971225,6.431493,0.615508,-3.745019,8.613476,-2.199330,-7.772328,2.186881,-6.055421,6.923003,1.341530,8.857065,-4.068605,6.557574,9.429022,4.172991,-5.103976,6.916346,0.459978,3.591487,6.181676,-9.874854,-2.877128,-0.012742,5.169567,-3.249125,8.631786,-5.636292,4.875904,8.617090,-7.275041,-0.356426,3.930935,-1.725121,2.444027,4.794503,3.302022,6.736571,8.535961,-8.883223,2.142336,4.750270,-3.510221,-0.842945,2.140366,1.546270,2.223153,3.295321,3.238973,6.185249,6.129203,-5.981575,-7.490590,-9.089017,1.651447,-6.196462,7.175753,-3.667092,-9.303448,-2.305320,-5.795725,0.167330,8.289553,8.653471,-5.231842,5.757104,9.310391,-1.032403,3.514174,-8.104174,8.170151,-2.734336,-6.404435,9.595663,7.174733,4.440852,5.062603,8.137368,5.837102,1.095920,-0.338569,7.203303,-5.236892,4.865782,9.951773,8.956609,9.119283,6.981618,-0.954367,-2.520869,-1.426144,5.606203,-3.868006,-7.413217,4.732798,9.130551,4.902289,-4.555434,-2.572148,8.407828,8.241606,-7.223827,-9.391170,-4.530094,-1.253271,3.687140,-9.109280,-3.667304,9.528516,-3.591001,6.771769,-2.324063,8.982831,-1.901533,0.432147,1.524176,-9.173901,3.689603,7.927391,5.987623,-0.563299,9.730892,-1.982605,2.608799,-2.500848,-2.253900,9.827321,-0.337406,6.766304,-5.053175,3.319271,2.971204,2.135712,-8.552492], dtype = "float32")#candidate|5946|(336,)|const|float32
call_5942 = relay.TupleGetItem(func_3234_call(relay.reshape(var_5943.astype('float32'), [10, 5, 15]), relay.reshape(const_5944.astype('int16'), [15, 9]), relay.reshape(const_5945.astype('int16'), [675,]), relay.reshape(const_5946.astype('float32'), [336,]), ), 7)
call_5947 = relay.TupleGetItem(func_3239_call(relay.reshape(var_5943.astype('float32'), [10, 5, 15]), relay.reshape(const_5944.astype('int16'), [15, 9]), relay.reshape(const_5945.astype('int16'), [675,]), relay.reshape(const_5946.astype('float32'), [336,]), ), 7)
uop_5953 = relay.log10(uop_5876.astype('float32')) # shape=(676,)
output = relay.Tuple([bop_5848,call_5854,call_5864,const_5868,bop_5872,bop_5907,call_5924,var_5925,var_5929,bop_5935,call_5942,var_5943,const_5944,const_5945,const_5946,uop_5953,])
output2 = relay.Tuple([bop_5848,call_5857,call_5866,const_5868,bop_5872,bop_5910,call_5926,var_5925,var_5929,bop_5938,call_5947,var_5943,const_5944,const_5945,const_5946,uop_5953,])
func_5955 = relay.Function([var_5847,var_5856,var_5865,var_5871,var_5925,var_5929,var_5943,], output)
mod['func_5955'] = func_5955
mod = relay.transform.InferType()(mod)
var_5956 = relay.var("var_5956", dtype = "float64", shape = (4, 4, 9))#candidate|5956|(4, 4, 9)|var|float64
var_5957 = relay.var("var_5957", dtype = "bool", shape = (44,))#candidate|5957|(44,)|var|bool
var_5958 = relay.var("var_5958", dtype = "int32", shape = (676,))#candidate|5958|(676,)|var|int32
var_5959 = relay.var("var_5959", dtype = "bool", shape = (44,))#candidate|5959|(44,)|var|bool
var_5960 = relay.var("var_5960", dtype = "float64", shape = (36,))#candidate|5960|(36,)|var|float64
var_5961 = relay.var("var_5961", dtype = "float32", shape = (165, 3))#candidate|5961|(165, 3)|var|float32
var_5962 = relay.var("var_5962", dtype = "float32", shape = (750,))#candidate|5962|(750,)|var|float32
output = func_5955(var_5956,var_5957,var_5958,var_5959,var_5960,var_5961,var_5962,)
func_5963 = relay.Function([var_5956,var_5957,var_5958,var_5959,var_5960,var_5961,var_5962,], output)
mutated_mod['func_5963'] = func_5963
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6385 = relay.var("var_6385", dtype = "int32", shape = (16, 3, 14))#candidate|6385|(16, 3, 14)|var|int32
const_6386 = relay.const([[[-5,-6,4,8,-5,10,4,5,-4,6,-2,6,8,-4],[1,2,-10,10,6,-3,-2,-2,8,-6,10,2,8,10],[4,-10,-8,8,5,-2,-6,10,8,8,-1,8,-8,-5]],[[-8,6,-1,-4,1,6,10,6,5,-7,10,-10,-10,4],[7,-6,-4,-7,-1,3,3,-9,-7,10,-3,-6,-10,5],[5,10,1,-6,-8,-10,-4,-2,-2,9,-6,-5,3,3]],[[8,-5,-9,4,1,-5,-3,-8,9,3,3,-3,10,-9],[9,-8,1,-9,-8,-2,-3,8,3,-4,-7,6,-10,8],[-8,6,-8,6,8,2,10,-5,-1,10,10,-6,2,7]],[[-10,-5,4,6,4,1,-7,9,7,10,-8,9,6,-5],[7,2,6,6,7,-2,-5,-6,-6,-10,1,-10,-2,-7],[6,7,-3,-3,-6,-9,-2,-5,-5,-1,-8,-5,-3,-9]],[[4,3,7,5,1,-9,8,10,-10,-9,8,6,-1,6],[-6,8,1,9,-5,10,-2,-3,-6,10,-9,-10,7,4],[9,-1,-5,4,-2,5,-7,3,1,-10,8,4,-9,4]],[[-10,-5,8,-3,-6,-8,10,-6,-8,8,3,-8,-10,-8],[-7,-6,-1,-6,-8,10,6,2,1,4,-7,9,-10,10],[-9,8,1,5,-6,10,1,-10,10,-2,-10,-2,-1,-6]],[[10,-1,-2,-5,5,-6,-2,-7,-6,8,10,9,-10,-6],[4,2,-8,2,-1,5,-8,7,7,1,-10,1,10,-10],[3,-1,-10,10,5,-9,9,-10,-5,5,10,7,-6,2]],[[2,-8,9,-3,-2,6,5,4,9,10,-1,-8,-10,1],[-7,2,4,-6,9,2,4,-1,-3,-2,-6,-8,7,8],[-3,5,-3,-9,9,1,-7,-1,1,10,4,-8,-2,9]],[[-2,-9,7,5,3,8,1,9,-2,-9,-2,-9,-8,-9],[3,2,-7,10,-6,-6,9,10,3,8,-10,10,-3,-10],[-10,-3,-9,8,-5,1,-3,2,-9,2,2,9,4,-5]],[[10,9,-8,-3,-5,-4,9,-6,10,-2,8,1,3,-3],[-9,5,-6,1,5,3,-5,4,10,-4,-6,9,2,6],[-10,-4,9,-8,4,-1,3,2,-8,-10,6,9,2,-10]],[[8,2,6,6,-5,-2,-6,-7,6,-7,-6,5,10,-6],[5,-9,-1,-2,-4,2,-5,-8,7,9,5,-10,-2,-4],[10,-7,5,8,6,3,-8,-9,7,-3,-3,8,8,-2]],[[2,3,8,-8,5,-9,8,10,6,9,9,8,6,-3],[-5,-3,2,2,5,1,8,10,1,-3,1,10,6,5],[7,6,-2,-10,4,-4,-4,8,6,-9,10,-6,6,3]],[[6,-5,6,7,-2,-2,-1,-7,1,8,-5,-6,10,8],[-8,1,-10,8,-10,6,4,-10,4,9,-5,5,-5,-7],[-1,-5,7,-4,2,3,-9,-6,6,-7,3,8,-6,-6]],[[-3,7,7,2,8,2,-10,-4,5,1,5,-4,7,-4],[4,-3,4,-1,-2,6,-1,-1,-5,-1,6,2,1,10],[7,-10,-8,9,2,5,-5,5,-9,-8,-3,5,-2,-1]],[[-2,-2,6,1,4,4,-10,-2,-1,-2,3,-7,8,4],[-8,4,5,-10,-5,-3,-10,6,7,6,5,10,-7,-4],[6,6,2,-3,-3,8,-3,8,-1,7,4,-7,1,-7]],[[-4,-3,9,-4,9,-10,2,2,-10,-1,7,-10,-1,-10],[-6,-3,7,1,-5,-7,-6,-7,-4,6,-1,6,6,1],[-4,-2,-7,1,10,8,-8,-2,-1,-5,-1,-6,7,-10]]], dtype = "int32")#candidate|6386|(16, 3, 14)|const|int32
bop_6387 = relay.right_shift(var_6385.astype('int32'), relay.reshape(const_6386.astype('int32'), relay.shape_of(var_6385))) # shape=(16, 3, 14)
output = relay.Tuple([bop_6387,])
output2 = relay.Tuple([bop_6387,])
func_6390 = relay.Function([var_6385,], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
var_6391 = relay.var("var_6391", dtype = "int32", shape = (16, 3, 14))#candidate|6391|(16, 3, 14)|var|int32
output = func_6390(var_6391)
func_6392 = relay.Function([var_6391], output)
mutated_mod['func_6392'] = func_6392
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6417 = relay.var("var_6417", dtype = "float32", shape = (3, 6, 8))#candidate|6417|(3, 6, 8)|var|float32
uop_6418 = relay.atan(var_6417.astype('float32')) # shape=(3, 6, 8)
output = relay.Tuple([uop_6418,])
output2 = relay.Tuple([uop_6418,])
func_6426 = relay.Function([var_6417,], output)
mod['func_6426'] = func_6426
mod = relay.transform.InferType()(mod)
mutated_mod['func_6426'] = func_6426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6427 = relay.var("var_6427", dtype = "float32", shape = (3, 6, 8))#candidate|6427|(3, 6, 8)|var|float32
func_6426_call = mutated_mod.get_global_var('func_6426')
call_6428 = func_6426_call(var_6427)
output = call_6428
func_6429 = relay.Function([var_6427], output)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6465 = relay.var("var_6465", dtype = "float32", shape = (13, 6, 5))#candidate|6465|(13, 6, 5)|var|float32
const_6466 = relay.const([[[-1.505245,9.384864,-5.202481,-3.720027,4.543592],[-2.757375,9.200214,-0.478527,7.644081,-8.708373],[-1.496385,-5.388985,0.464861,-1.571290,3.723713],[7.801754,-2.175589,-3.774292,-0.219263,-1.242103],[-9.179731,4.556250,-1.532477,0.660472,-4.232942],[7.738475,9.402722,7.828170,4.369106,-4.853057]],[[9.094375,5.089119,4.053463,4.033426,-9.305171],[3.893673,-4.336051,-2.522831,-5.391159,-7.265130],[2.421326,-7.954784,2.708246,-0.476126,2.340184],[-5.059814,-0.633554,-3.160816,2.696230,2.413253],[6.561991,-6.890492,2.276032,8.950419,-8.873997],[-5.905630,0.993208,-2.128706,6.247635,-1.457270]],[[-7.617386,0.548956,-8.214585,-7.498852,8.966107],[0.939403,-7.750054,7.990746,-4.382107,1.063965],[-4.905208,-4.964386,-4.974340,3.402138,3.183988],[4.884910,-1.312979,-5.313665,-7.740549,-8.663095],[6.460833,0.328194,2.592501,0.249509,0.485366],[-2.858930,8.598880,1.749539,1.807531,8.141118]],[[-7.664149,-3.015244,2.777691,9.621717,7.251623],[-5.476575,5.484276,-4.206251,-6.511294,-4.098747],[9.244649,8.679007,-3.823444,-2.945758,3.698531],[-0.699181,-5.582370,-4.317449,-8.656348,-6.468086],[3.054161,-8.708478,-2.845977,3.191619,-0.946080],[-9.073955,-1.955081,-1.758294,-7.357367,2.154224]],[[-5.980786,-1.111678,-1.350395,4.130821,-2.907384],[3.578335,-7.596297,3.422175,-6.782852,3.492908],[-0.380551,-5.749974,6.637263,4.209396,-9.613439],[-3.908168,1.851512,4.699970,9.386400,-6.720121],[-6.871183,-1.266145,5.756722,7.909242,-6.314417],[-2.191808,-6.746472,-2.682912,-3.012774,-2.815657]],[[-1.227972,0.840543,6.489031,1.904758,4.832962],[-3.426524,0.688383,-6.896138,-6.317727,7.361275],[-1.958876,-9.796530,-6.241376,6.258392,-8.868776],[6.584815,-6.127639,-8.123559,-5.138736,-4.618372],[3.207602,3.969820,4.099621,2.455862,-2.663366],[1.201814,2.125346,4.325098,-2.260537,-7.700636]],[[-9.803856,1.881206,-1.762320,-6.534524,4.988120],[4.948097,-4.336813,-9.347909,-5.131367,8.947347],[-3.946183,-5.530153,-7.859797,7.075789,-0.699270],[-8.380469,-9.721278,2.500545,9.686778,0.271135],[-6.174257,-0.709693,2.276084,8.791870,-9.875357],[-2.825851,8.196057,-6.277075,0.652959,-1.719706]],[[6.306860,-5.499486,-5.302746,7.657272,-3.151993],[-2.652375,2.254065,6.084598,6.351165,-6.806927],[5.549190,-0.976652,9.657201,8.288219,0.192518],[-0.879702,-4.180153,-8.237344,-0.281787,-6.880908],[-7.918515,-2.606089,8.663428,-2.091388,-0.389936],[9.999416,-7.346362,-0.042395,-4.610856,-7.660136]],[[4.683394,0.987434,0.579078,-0.484219,4.125398],[-6.572611,3.577784,8.399645,-3.372767,-9.640968],[-3.028248,0.101467,1.901913,5.669586,1.147966],[7.329287,-0.449416,-3.805936,-8.393858,-0.200426],[2.815910,9.496606,5.833188,-2.004862,4.792038],[-3.202723,-9.596581,-3.431402,0.108669,2.532513]],[[8.873059,7.793445,4.575649,5.966740,-1.127122],[3.681006,7.183724,-9.408075,6.410083,-3.800462],[1.631344,2.630290,-3.370413,-6.652807,3.104185],[-0.541277,-4.470986,-9.453175,3.902532,-8.767548],[6.601523,-4.155442,-3.330920,9.989629,5.177510],[-0.462923,-7.115708,-2.141024,9.382329,-3.500970]],[[-2.782455,1.522168,-9.905018,9.856079,-1.927664],[2.122534,9.404998,-8.680198,0.373829,-3.134287],[3.683721,9.618111,-2.152284,5.829106,-0.308497],[-1.373230,-6.714653,-8.600101,5.117623,4.739845],[2.953514,-8.611069,-7.751111,-4.789630,-4.057666],[-6.966842,-8.874389,-0.584478,5.869594,-5.352764]],[[2.312654,-0.626752,5.088971,0.657880,-5.370188],[-5.783874,4.725054,2.319253,9.579131,6.069042],[-8.104059,5.875796,-9.676571,4.603551,8.830665],[7.121795,-7.155417,2.025154,-1.759215,-5.793207],[7.505364,-6.966882,3.056897,-3.969075,-4.377930],[6.726236,4.600352,9.361159,-3.321207,5.880967]],[[-2.816563,-4.273472,-7.239231,-8.458003,-6.746172],[-7.666650,6.379352,7.144364,-0.563217,1.260381],[3.999051,6.384935,-3.554478,-2.372463,8.258759],[-9.945984,0.702286,-7.326082,-0.787894,-1.151968],[3.414967,-9.876445,-5.108059,-6.028216,1.405180],[2.641639,-6.726510,3.291931,5.194934,6.136058]]], dtype = "float32")#candidate|6466|(13, 6, 5)|const|float32
bop_6467 = relay.floor_mod(var_6465.astype('float32'), relay.reshape(const_6466.astype('float32'), relay.shape_of(var_6465))) # shape=(13, 6, 5)
const_6475 = relay.const([[[-7.729696,-5.990654,8.351744,-2.315749,-5.754825],[-6.477344,-2.291210,-4.628056,-2.034156,8.938879],[7.362336,5.642680,-6.616118,-5.511319,5.575572],[-8.018566,2.931573,0.606956,5.806322,-6.212772],[4.151875,-5.627465,3.421987,-6.348491,-6.355914],[-7.775544,8.941453,1.526810,5.561902,-6.858185]],[[0.837444,6.546252,8.019958,-8.617683,-1.957672],[0.861886,2.467308,6.088125,-2.234970,-6.225858],[5.619106,-0.406251,-1.239241,1.130341,8.342974],[-0.423847,-4.332653,4.002040,-2.948946,2.973642],[9.803334,-6.831035,-2.173669,6.685789,6.273603],[4.025465,-5.374154,4.256205,2.932124,8.601077]],[[-5.654944,-1.500062,3.913691,7.277433,4.777552],[-5.040971,1.345208,7.123192,9.451752,-3.172596],[-7.584214,2.044552,5.753060,9.170448,7.454297],[7.347995,-5.893232,8.456912,0.740573,3.127830],[9.000941,0.621839,-3.370613,-3.708937,-6.299493],[-3.918659,-7.550031,4.439270,-9.003284,-2.743492]],[[4.845922,-1.108749,7.967704,6.840549,-7.088881],[3.048078,8.529830,-8.142525,3.677430,2.248350],[1.398240,-7.128714,4.311369,1.818512,-6.479890],[-0.230292,9.325925,3.621767,-5.691416,2.696566],[0.518928,-8.192755,-8.618473,-8.506699,9.453125],[2.878096,6.720131,-2.886254,5.535546,1.961957]],[[4.224979,-5.567163,-9.042322,-2.768961,-2.510654],[1.563184,-0.636958,-1.837736,-1.012515,0.124639],[-0.865606,-9.304649,-4.633765,7.774540,-4.154438],[-3.672194,-7.492969,-8.886441,-7.595976,7.458855],[-2.451450,9.537093,-8.922733,8.241444,-2.865044],[-3.931586,9.260640,3.116809,7.326701,-6.165773]],[[0.007414,7.182831,4.803945,-3.624760,-8.848753],[-7.778857,-7.328159,-4.769922,-8.317154,0.740545],[-9.312001,7.829788,-4.828336,7.606060,7.566125],[3.378773,-5.467294,-6.269445,-3.564327,-0.693068],[-7.711590,3.422173,-0.890262,2.779104,-0.150084],[4.688532,-8.517215,-5.073792,8.413057,-4.607962]],[[0.143912,0.128603,5.775097,4.543394,-7.583471],[-2.200278,5.242286,7.044432,4.884829,-7.684567],[8.546739,-9.622701,-6.151145,-5.916320,0.403127],[7.603200,-0.683724,-6.127687,-3.041850,8.022975],[3.276924,-4.832395,-4.125764,-4.453617,-6.765312],[8.532688,7.733409,-8.724630,-2.178573,1.246146]],[[1.040326,0.386048,-7.536152,2.587836,5.549867],[6.319865,9.433950,2.622691,-5.604314,7.682620],[-7.497173,-6.029814,6.270692,-1.106526,-9.472209],[1.057072,-5.945609,0.938718,-5.344149,2.329164],[-6.115021,3.747912,-6.412681,4.374859,-8.243320],[-3.077771,0.792365,-8.588850,1.956239,-9.706672]],[[0.606063,0.047970,-2.712624,-7.143912,-1.813167],[2.220012,-5.617036,-7.635781,9.765821,2.711081],[-9.468514,7.269715,8.575023,-5.050450,-7.556799],[-8.479689,-7.153108,9.521668,-2.345593,-3.599696],[7.971807,3.138873,-6.986604,3.993388,9.975622],[0.971475,-0.087149,2.374967,5.397565,-7.783652]],[[0.417231,3.490085,-0.913537,-4.790764,-7.397193],[1.666869,-1.819964,2.066251,-0.562162,6.050827],[-9.758584,-3.786443,0.965105,-6.508299,6.498836],[-9.473875,1.441390,6.694694,-5.838100,-9.033967],[-5.175275,-4.964556,5.618746,5.955358,-0.738422],[8.870476,2.328829,9.469691,-5.338270,7.327545]],[[-5.450023,-9.325842,5.630091,-6.132564,6.745365],[-2.292944,-6.193854,0.813622,4.499475,-7.014785],[6.819481,-1.537489,7.892173,3.585705,9.592557],[7.372901,-9.345016,7.296828,8.643029,0.161456],[-7.946947,-3.498221,-4.918515,-6.941288,-7.059614],[-4.871581,1.270154,7.962363,-8.119987,-1.135552]],[[7.964177,-3.948768,3.249017,-4.383533,0.607483],[2.125366,9.945338,-1.660902,1.538743,7.250213],[2.535206,3.330178,-6.277667,6.705704,2.265109],[-7.804177,-3.532193,-2.700922,-2.782735,-3.395860],[-4.715112,-6.480382,-2.279698,-2.712330,6.926111],[1.305941,4.648603,8.920944,2.989501,-9.906205]],[[-2.073685,-7.918536,9.312342,-6.445174,6.810263],[4.821809,3.656832,6.320394,3.798998,0.432219],[-3.561797,3.368114,-9.834042,3.420997,-8.993085],[-0.307374,7.438132,5.177208,-2.410964,-9.560509],[-8.760352,2.494921,9.570156,8.250939,-4.494608],[-4.365730,-2.754900,-8.732827,-7.540788,-2.481833]]], dtype = "float32")#candidate|6475|(13, 6, 5)|const|float32
bop_6476 = relay.bitwise_or(var_6465.astype('uint64'), relay.reshape(const_6475.astype('uint64'), relay.shape_of(var_6465))) # shape=(13, 6, 5)
output = relay.Tuple([bop_6467,bop_6476,])
output2 = relay.Tuple([bop_6467,bop_6476,])
func_6481 = relay.Function([var_6465,], output)
mod['func_6481'] = func_6481
mod = relay.transform.InferType()(mod)
mutated_mod['func_6481'] = func_6481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6482 = relay.var("var_6482", dtype = "float32", shape = (13, 6, 5))#candidate|6482|(13, 6, 5)|var|float32
func_6481_call = mutated_mod.get_global_var('func_6481')
call_6483 = func_6481_call(var_6482)
output = call_6483
func_6484 = relay.Function([var_6482], output)
mutated_mod['func_6484'] = func_6484
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6626 = relay.var("var_6626", dtype = "float32", shape = (15, 11, 14))#candidate|6626|(15, 11, 14)|var|float32
const_6627 = relay.const([[[2.863569,-4.202204,-5.738720,-5.518103,7.606855,-7.544969,-1.376468,-9.838292,3.512678,-1.512386,-2.842138,-8.017494,-5.525418,-7.059151],[4.256534,-0.200636,-8.663399,-9.417400,-6.426572,-1.655214,3.837409,-5.884832,-5.765914,-4.183116,2.140970,4.863048,-9.854615,5.206267],[-4.212559,0.477909,8.342047,-8.726049,-8.266155,-0.692743,-0.579329,0.457699,6.933988,4.471589,-5.035344,6.662960,-7.322006,7.211092],[1.124060,2.386673,-4.097161,6.799401,-4.192173,9.696932,-5.342009,-2.047560,-6.076555,0.055191,0.713628,-2.030264,-1.814868,3.716265],[-1.793447,-2.822709,0.183714,-3.451322,-7.924734,7.669872,7.811122,-7.703348,3.002787,-2.201930,-5.302605,7.019183,-5.033872,7.904908],[-9.811537,-9.137198,3.286436,-3.110088,-3.774516,9.939412,-6.718936,-7.442547,9.392385,-4.195583,0.183301,6.697588,-7.696173,6.951281],[-5.368511,2.711788,2.165730,3.865315,-8.859338,3.268773,-7.404420,-0.075942,4.387263,5.643205,8.661846,8.990940,-7.361501,-9.013347],[-1.094521,-8.279918,-0.951701,8.075176,4.442698,-2.688414,-0.842976,-4.020652,-7.994602,1.111068,4.043198,7.221408,-0.725962,0.945985],[2.167449,4.119377,0.359816,-3.259878,-2.042565,7.685932,-5.744752,6.582327,1.764996,-0.394060,-8.547332,-7.197640,-1.099713,-0.529107],[-1.416268,6.591954,8.825913,5.549984,-6.151728,-4.599368,2.995266,-9.537768,-3.402551,-5.856617,-0.205235,5.549417,5.578163,-6.736035],[5.148178,-9.558046,2.103422,2.812190,1.021724,2.933815,-5.720523,-3.839317,-0.796694,-6.977648,-9.016448,-9.250576,5.832765,-3.861346]],[[9.631310,-7.359039,7.834024,1.842759,-6.421504,-4.246368,6.046569,-6.481628,1.235210,-5.633489,8.675839,-3.164002,4.108683,-0.453374],[1.102526,0.174410,-9.676877,2.039598,2.311690,-1.841046,-8.320855,6.839212,-6.154456,2.786248,-8.254408,9.171233,-8.110303,4.949603],[6.277125,-3.653239,-9.432633,8.253287,6.427799,2.842706,3.104117,7.128472,-6.724615,-4.596219,-9.156851,-5.824888,1.100192,-2.324823],[-7.113572,9.182225,-5.989264,-6.144497,-1.293010,0.446782,-5.039293,-8.069556,-3.809464,2.603792,-8.461825,8.353176,-3.714192,2.906069],[-0.222586,8.025938,6.782601,-8.994351,2.508161,1.550010,-8.360121,1.048622,5.019123,5.070180,4.558422,-9.351428,-0.787114,-5.042035],[8.591966,-0.932499,-4.311708,-4.092947,-2.686357,2.770391,8.650176,6.713454,0.227073,9.083629,-9.058211,-2.194133,6.366591,1.777958],[-8.575501,-9.290341,8.588015,6.412895,4.031813,-5.248203,-7.665790,0.578477,-4.677842,-5.716336,8.162568,-9.605020,-9.912329,-8.338833],[1.692390,4.291019,9.383112,4.736415,-9.398814,-4.724069,6.400815,5.510786,-6.820460,5.982943,-8.253609,-6.529871,9.398766,7.129062],[3.743248,-8.784850,-3.734281,9.364576,4.515239,-0.500222,9.104476,9.019513,3.742200,1.029213,2.747892,-4.063836,-7.452118,-4.788308],[5.135536,4.802681,1.299480,7.587712,2.510435,0.508494,-2.093375,-2.257263,6.047223,-6.127740,-6.125207,-7.566542,-5.809343,7.987521],[-0.543484,6.272643,-8.243131,-4.448187,-4.359939,6.452440,-5.344849,-6.780238,-9.715194,9.885063,6.819158,6.950219,0.637720,8.992787]],[[-9.997313,-8.301904,-4.931732,6.173597,-7.395355,-7.167381,7.609055,-5.069174,2.890999,-6.418025,0.308189,5.580645,8.343873,-8.862898],[-5.651593,1.580807,2.738375,7.401798,1.454858,-0.964340,2.504141,-2.359238,-2.153424,-2.855151,7.519934,5.293674,-1.322284,6.850531],[7.230157,-7.931403,-9.942545,9.951238,6.847014,9.837498,0.211940,-5.448688,3.005043,0.654196,1.764019,6.336335,6.308140,3.634935],[7.892836,7.347392,1.064125,-5.324135,1.052910,9.885390,8.399549,7.991312,-2.018974,9.238842,-6.248114,4.434853,-9.220007,0.002769],[7.628330,-3.226922,0.553719,-2.584862,5.938163,-0.547505,-8.868811,-2.605210,4.348215,-8.974337,1.838640,7.198215,-4.771966,-1.352643],[4.252669,-3.905118,-2.028335,7.898718,3.139024,-2.445162,-8.992344,2.300415,-6.722229,-6.802790,-0.578209,0.745770,-9.359374,2.796670],[1.726184,-5.391641,4.198742,-6.732747,9.861774,-6.388074,8.785816,1.742587,1.493351,-0.651284,-7.472389,8.940561,0.275728,8.578572],[6.229400,-5.420806,-5.657802,5.599173,-2.245190,1.317526,1.567711,-6.016209,9.236903,9.699132,-0.252402,-7.639312,-3.564336,1.051415],[9.190653,-1.924331,-0.215986,5.871375,3.601473,-0.985686,-5.326708,8.509316,4.936705,-2.775569,5.539916,-7.220715,4.937322,1.821590],[-8.903937,5.957514,1.047345,9.106810,4.242021,-6.407856,4.788163,-7.873123,-1.156591,-9.383301,2.645960,-8.429008,-0.938848,-1.003275],[-4.052268,7.842532,6.900780,-1.291139,-7.237528,-5.625306,-0.893690,-6.542806,3.678120,-9.080824,-9.695598,-1.835908,9.252912,0.389833]],[[7.569560,-3.021696,7.219580,-9.387331,-0.569428,9.981571,-2.594872,-8.073369,-9.953747,9.545128,1.807068,1.182796,-2.804197,9.550681],[9.430867,2.192554,0.103325,-1.165223,2.883182,7.164005,6.390674,0.240499,-1.206986,-2.592553,-3.913251,-9.665470,5.618697,-6.310352],[3.625796,-9.739601,-7.415783,4.852740,6.544595,-8.842481,0.476013,-3.756691,-0.645943,-5.055491,-0.181728,7.100567,-5.030405,-5.909123],[4.286976,9.791760,9.272252,7.599743,1.237383,0.034837,-4.198112,-9.167533,1.004525,-2.915972,-9.208542,-3.266336,-7.589276,9.279324],[4.060537,-0.574363,-0.251634,-9.586568,6.543897,0.422907,-1.635476,6.483502,-5.966131,-3.128194,2.537201,6.820603,-7.700181,-2.706507],[4.982406,4.768531,3.493081,-5.298010,-7.931217,8.235524,-1.938239,-1.638494,3.851307,-8.325322,1.511085,9.132300,6.782480,-8.028489],[-2.864750,-9.364784,7.241676,5.484762,-6.650711,-1.093158,-4.743834,-3.532658,9.919304,1.962933,5.319305,-2.921219,0.770048,2.336207],[9.626976,-7.455843,-9.577912,9.843994,-7.958731,-3.963973,-8.415862,4.718435,2.470462,-4.524281,2.143818,2.249402,7.071950,5.783238],[-1.906047,2.036440,4.676392,8.281267,2.136760,0.458967,8.699640,-8.763031,-9.189864,-6.112144,7.758778,-2.283624,9.563526,1.650710],[-8.171632,2.256349,4.030310,-0.354554,-6.420226,-8.148354,-1.173440,5.059960,-9.508835,-5.097048,-1.260142,-6.761369,5.721194,-8.313965],[-6.694843,0.466578,-7.672975,9.674217,5.811123,-0.267417,-9.241654,5.864372,-4.453549,-9.326909,-7.026114,-1.162446,-1.815011,5.172522]],[[2.926965,-3.008344,7.687902,-7.003203,-9.724281,-0.212184,3.820893,5.429974,6.336494,6.313774,3.405944,-3.385415,-7.228134,-0.405910],[9.086410,-4.682423,9.905421,4.650923,-5.684671,9.183197,4.191689,-9.300795,-8.950062,-2.613807,2.340045,-3.637760,-2.924627,-6.281559],[5.501812,6.548904,-9.098504,5.497873,-9.763604,0.370873,5.259392,5.984014,-6.392204,8.191659,7.377659,-7.818432,1.125176,8.287779],[-5.017290,-3.902166,0.087120,-8.214176,0.483182,4.683835,-1.963108,-9.176698,0.712594,3.455635,-1.077303,3.057096,-4.175586,-0.314386],[-0.818572,8.646449,2.278617,-0.782212,7.005863,3.640537,-7.587662,-7.086875,0.666221,-4.086387,-3.951974,-2.847135,1.154500,-2.514792],[8.869006,3.650206,8.646893,-4.676765,8.127721,0.726858,-6.518270,5.832951,5.227380,1.381185,6.477428,-2.910638,8.251353,-4.202689],[-5.540350,3.149429,5.688618,0.856389,0.063523,4.373051,-1.916262,-6.012644,9.120044,2.261329,0.435721,6.937887,0.688608,0.232684],[-8.513123,0.381812,-1.453408,6.825236,8.943543,-9.525390,-3.884055,4.522597,-4.526948,3.191018,-4.140770,7.332729,-6.022092,-2.297888],[-6.040807,-6.024239,3.611421,0.171838,-4.930602,5.781275,0.142234,6.767748,0.084995,-6.110860,-9.658506,-2.520313,-5.557219,-0.422003],[-9.721629,-6.021041,-7.779429,-8.784745,-7.526800,-9.822613,-7.251151,3.726493,1.754655,1.161502,7.630785,0.882116,-8.695673,-6.086908],[1.876079,4.807608,2.464420,-5.054325,-9.294268,9.846756,-2.584644,-4.286701,9.779881,-2.843349,-9.710995,-2.697912,4.900458,5.243172]],[[4.451476,-1.254297,-4.942278,-8.276431,-6.438144,-6.099174,7.756985,4.824646,3.490456,-6.637935,9.213367,2.113820,1.173717,-9.901793],[6.758375,-9.339912,3.830954,6.576752,-3.716022,-2.015080,-9.565827,1.212414,-3.519029,8.562882,-1.224671,8.621038,-4.684423,3.167852],[-8.491561,-9.683640,4.655603,-0.864190,-3.488884,4.651220,7.006184,1.175016,-2.231110,-0.702120,6.826619,-1.329757,0.726025,-0.382877],[-9.367123,6.137914,3.007065,8.216883,-8.378188,6.705640,7.353307,3.208671,-8.432809,0.300577,-6.865186,-2.340415,3.829852,9.961702],[-7.942510,4.497997,-8.167006,9.369425,-9.432565,-5.258974,-4.944889,9.834757,-5.223234,-4.266935,3.748246,6.032819,2.214865,-4.459899],[-7.782441,-5.660456,8.573783,-4.274229,-3.329998,6.415006,-7.887968,-6.290282,5.824389,-2.158671,-4.566450,0.036129,-0.650806,0.501168],[-3.429478,7.694230,-8.793391,3.293376,8.982996,4.205978,0.720182,-9.038899,-7.988745,-0.892144,6.889012,-8.055487,2.209907,7.242914],[-7.028682,-6.999119,-3.532904,-5.915186,0.992783,-6.686470,8.398474,-7.834499,-9.261980,-1.188796,6.274097,2.622673,7.503474,5.192650],[8.713164,0.844241,3.669552,-1.321352,3.085658,-7.015130,-6.537728,7.269130,-3.823098,-4.918155,-2.015161,-5.003762,5.768695,-2.067407],[2.024838,1.787468,1.151074,-5.524042,-3.951821,-3.332625,8.578732,-8.901006,-7.163465,6.397743,-6.947445,1.242640,-3.434947,-2.174049],[4.003337,0.421641,-8.811297,9.763411,0.859541,9.828954,-0.267197,3.532746,-1.509469,4.650792,4.465434,-6.455807,-9.448855,-0.828703]],[[6.040939,-1.868038,-0.506333,9.847753,2.786652,-5.393756,-7.916887,-9.197677,2.064139,9.594846,-4.825590,-8.852110,1.663592,3.716783],[6.044385,1.036671,-7.915049,4.702116,4.371575,-3.662745,-1.332635,1.754705,-9.793791,5.019833,9.981531,7.736978,-6.146903,1.259253],[-7.989774,8.127197,-9.315861,-8.168276,7.629522,3.498279,-1.240865,7.436019,-2.160346,-4.329272,-4.408815,8.859602,-7.875481,6.299037],[-8.067905,-0.856798,9.189938,-2.051248,-7.948792,8.252534,0.561002,-6.190804,-4.249213,-6.087440,-9.311598,8.514275,-5.022186,-6.560911],[9.778158,8.503570,-1.405586,0.911355,-3.331051,-0.035366,-5.920162,-2.435574,-8.154653,-8.439574,-8.291137,-2.435099,1.948098,5.227423],[-5.954221,-9.261510,-2.909602,0.071953,6.959591,-6.227035,2.616757,5.546647,-4.429440,7.098133,-0.975691,3.866185,-7.886879,-8.894822],[4.127255,2.995107,6.472080,-9.134079,-7.076341,7.500573,-9.444559,6.554188,-6.393807,5.696237,-3.906835,3.235744,-9.904863,5.194432],[-5.200023,-9.199494,1.095445,7.927289,3.498886,-2.867763,-5.523903,-1.861358,-7.103495,-7.255225,-7.239495,1.152206,-7.395679,0.872510],[-2.714622,1.083707,-1.682775,-0.609033,1.346612,4.744732,1.114809,-2.861965,9.895119,-4.847359,-3.164807,-7.535682,8.067661,4.533546],[-3.917601,-1.998568,3.786303,-9.234302,-4.892428,-7.507331,-5.610314,-5.232878,2.152340,4.724484,0.847031,-1.627069,-3.921003,-7.056775],[9.394805,5.836477,1.298904,-6.278019,8.004115,-9.626296,3.552849,-0.293298,-7.217323,-7.968076,4.800961,-0.822126,1.260974,7.950234]],[[1.858082,2.340371,3.622685,4.232297,6.038398,-7.530546,-2.888737,-4.480354,7.072030,3.479936,3.416345,4.640864,-8.558574,-0.965329],[2.795248,9.104234,0.384122,3.381682,-1.293072,2.341151,-2.434254,-8.212322,4.732074,-1.575162,1.433572,-2.732173,4.259245,-9.017632],[-9.525715,-5.605660,-2.143259,-3.853685,-7.084043,-6.239658,-7.824356,-7.478532,3.956435,2.145133,4.491780,8.903295,-6.918149,-5.754959],[-6.589703,2.571088,3.083420,-5.678201,6.027579,4.081161,-0.681095,-1.730457,-5.049766,0.486539,-2.086210,-2.561367,-7.962278,-8.163152],[4.689075,6.525166,0.212970,-7.568312,-4.520892,-5.940659,-4.964890,9.581588,-9.132707,3.874502,2.753514,-9.883750,-1.489815,2.643639],[3.942163,8.215893,-1.610432,-7.140057,3.942510,-8.839030,1.567708,3.119863,3.067807,-6.907434,8.282470,-3.746465,-6.934438,-0.483045],[9.723778,6.860521,3.323659,0.348077,1.901418,-6.254250,6.702884,-1.938224,5.654584,-2.580482,3.334952,-0.174776,-4.357052,1.433670],[-2.063855,5.767260,9.403088,-0.824654,7.620699,1.514970,9.281613,9.022097,-7.557291,0.053835,-1.933468,-7.241058,-4.079950,-2.852083],[8.364633,8.286319,8.298907,8.469155,3.617634,4.669600,-4.127315,-7.034853,-6.803957,-8.613073,4.304247,5.368986,9.373948,7.673990],[-9.425374,-6.474793,0.370479,1.985026,0.123640,-4.495441,-5.988570,4.116346,-3.455818,-7.704146,-5.055406,3.717387,-6.748296,5.755498],[8.187108,8.433300,-5.141529,6.579596,3.088362,-7.068804,-6.101789,-0.960429,-5.496746,8.573912,7.538119,-3.686521,-2.042471,4.885695]],[[-3.810663,-7.742493,-1.577488,5.967124,1.903428,-1.163235,-9.581049,0.061316,4.634554,5.465392,-0.766559,-2.749847,1.829502,6.844402],[7.398385,-6.604714,5.648236,4.634053,1.423126,-4.791850,7.375869,4.916133,4.077354,-6.197359,-9.799153,-5.460550,-3.818490,-1.761013],[3.708025,7.328151,8.910186,-4.110828,-6.717653,-9.713721,5.409134,4.033000,8.534020,-7.805986,2.695757,-0.490624,-9.804926,-1.964877],[8.762714,-1.356857,-4.574296,9.008520,-3.624111,-1.738390,0.708604,-5.372362,9.784749,-0.907030,-4.403254,9.147716,8.397258,-8.905404],[0.743508,8.140488,6.673148,1.207767,3.115068,2.631641,2.639040,0.811538,-5.572149,9.395791,8.773655,0.868620,-6.743500,5.980313],[-7.923701,8.243973,2.715735,-6.012089,4.917073,-7.100693,0.783337,-1.397682,-2.669986,9.491238,3.775531,-8.041099,-4.401297,-2.547286],[8.864384,6.091093,9.292390,2.782524,2.872462,-1.053332,2.488289,6.582481,-1.560298,9.235825,6.188705,-3.615255,9.279658,6.554667],[-4.846290,-8.287289,-6.913498,1.079443,7.210601,-8.208993,-4.479455,8.858037,3.188137,-8.308538,-6.183521,-9.057746,1.903870,-9.926900],[-8.650835,-3.529698,1.382698,-8.861539,-0.270853,-4.505894,-4.243758,-7.625136,0.717862,-6.702159,2.323386,-6.494124,0.224740,2.329165],[7.594644,6.369259,-9.276139,-1.819936,5.565844,6.708274,-1.735779,5.625123,-7.855081,-4.347810,0.406486,-4.669609,6.314734,-9.962857],[-1.121006,9.345861,5.366492,1.127626,6.049415,4.416916,-3.817420,-7.547915,-5.049414,6.281211,-4.643394,-4.792999,-0.300854,-3.652145]],[[-4.372974,-7.073206,-2.612463,-3.203803,2.756696,4.737396,-8.502691,4.116342,2.226179,8.915048,4.700126,-4.656144,-0.705403,9.368518],[-4.367345,5.527092,-7.555647,1.150454,8.004971,-3.616587,2.739954,3.551312,-6.531884,-3.200352,2.945663,-3.492798,-3.289769,-9.567562],[8.069145,8.426466,4.042048,-3.108036,7.147350,-4.987397,-7.360048,7.281504,3.962776,0.434879,5.933027,3.219587,2.793649,0.847665],[1.318749,0.946551,4.623948,-0.869403,0.268074,-8.988875,-0.577941,6.411599,0.564525,-0.652115,-7.304350,-9.530076,3.522534,-0.605919],[3.074526,-8.580680,0.621521,-9.215032,-3.398070,9.335008,3.144593,-5.799699,-9.008969,-4.601613,-0.284573,-6.211137,-7.090852,-3.956979],[1.661479,3.963163,-8.432562,2.346855,7.855169,-1.741606,-5.606209,5.097602,4.737341,9.546205,5.887049,4.266815,-4.355438,-9.249505],[3.737216,-1.765288,3.164489,6.884269,1.831685,4.664240,-4.581276,-4.004633,0.156648,7.027340,-2.464599,8.583587,-9.213099,9.550256],[-9.918285,-0.002742,4.074645,-1.772943,-9.615971,-5.266234,-0.429770,-5.926807,-2.297267,6.894164,-9.399110,-0.090858,0.522569,-4.030131],[1.444438,-0.102302,-3.194578,9.160262,8.702885,-4.317147,0.010982,9.221260,4.836671,0.531797,7.022645,0.281939,7.805858,-3.913684],[8.856302,-8.556629,-8.049731,4.972557,5.255398,-5.984456,-3.564567,-4.235987,-3.103214,-9.612093,1.296224,2.670501,-4.650237,-5.051609],[-8.019275,5.310762,-1.550846,-5.710996,-8.131200,0.039052,-2.959084,0.565591,-8.208336,0.861828,4.540213,-2.580214,5.076093,1.846325]],[[0.618738,9.732691,-7.870000,4.234870,-0.385305,-4.785481,1.868926,1.756755,8.263606,9.474799,-8.960734,-4.207188,-5.367129,1.485183],[-5.277766,8.251610,-6.037688,-9.116827,4.118295,5.872923,7.698702,3.864391,6.917871,5.387241,8.220004,2.926365,1.622142,4.234115],[-7.438187,3.964219,-4.639750,-4.031719,1.323983,6.857107,3.543010,-4.249805,-5.066847,6.357921,-7.235345,8.195064,1.829446,-6.802579],[-9.981464,-2.351134,-2.439741,-4.104776,4.644979,9.518590,5.611004,1.999195,-3.151596,8.031025,1.061917,-1.865886,1.025047,1.241970],[-1.606614,4.825404,-2.786377,-4.170650,7.415379,5.351515,9.662589,3.868354,7.256444,2.578561,0.632048,5.789331,-3.010756,-8.647641],[2.436336,-6.436230,5.798820,-0.567752,-4.897387,-4.552639,6.634220,-5.518217,4.189651,7.266494,-1.637966,-6.333302,-0.261264,3.058773],[1.515106,-9.510622,8.916456,8.931694,0.054650,-6.367327,-6.219204,1.788640,-3.701954,-8.529657,-2.650146,8.328627,1.635124,-2.616815],[3.311737,-8.805207,2.354106,6.297206,1.625845,-1.564157,-2.132112,-6.195596,3.967602,2.714979,1.114194,8.360775,1.946044,8.421227],[-8.892909,-1.232242,2.168541,6.691099,-9.418191,0.656857,9.582770,-2.518577,2.659107,-6.269808,-9.720477,-0.868405,2.289789,1.131930],[-4.777110,0.004722,-4.149085,-8.812168,-2.198717,5.760696,-4.572315,0.003569,-2.060766,-5.859047,-6.203573,-2.240132,-7.667799,0.907198],[1.727593,-7.234696,9.868835,-0.215418,-0.351113,0.925697,-5.086683,7.924056,4.452654,-0.430452,-3.599140,9.223780,3.559614,2.120026]],[[7.530885,-3.460581,-6.541689,-8.803959,-7.920437,2.442731,-8.685510,-8.433492,5.623510,1.142535,-8.997236,-6.534399,-1.698839,0.061236],[-5.076052,8.839010,9.709549,-3.489208,6.734177,2.089756,3.478509,-6.437975,0.371565,6.005079,-2.343912,-7.750618,-3.546131,9.625080],[-0.195651,7.441541,2.129999,-3.062544,-6.401042,-4.946386,-2.323627,0.009716,5.926703,4.289501,-1.344688,2.582377,4.358079,6.316415],[2.664810,4.225132,-7.940537,-3.024051,3.489901,-3.068957,6.901347,3.315971,2.450018,2.327492,-9.274370,7.494648,6.817305,3.953232],[-9.689311,0.194164,9.436153,-3.700212,3.825749,-6.722946,7.681424,-9.392243,4.738899,-1.012236,-1.335765,9.298360,-6.788942,-4.531662],[-3.837842,8.924314,-7.230565,-6.688735,8.029954,7.302380,1.830128,2.539479,7.609379,7.455935,-4.768003,7.336460,9.447075,2.240213],[3.992779,-6.893122,-8.819818,0.046584,-9.647708,-0.421918,-2.821353,-7.876459,6.798819,-5.469294,0.083775,-8.688355,-0.499206,-9.090150],[-0.832275,6.852354,4.014024,6.001387,4.433529,4.607478,-5.619133,4.404532,8.817480,-3.405370,-3.775121,3.409257,-1.988003,4.809348],[3.049021,1.464826,1.798951,-0.573397,-1.695826,-6.877059,-4.624715,9.236582,-2.207227,5.425495,-1.319626,-6.242901,-6.690619,-3.761070],[7.262249,6.412889,8.964606,4.588766,-5.145229,-6.826963,7.596156,-0.536583,-5.431252,9.593614,4.534810,-0.836234,-4.174354,-6.680318],[3.130181,-0.338361,-7.389903,0.727856,-3.020178,-7.371523,-4.886554,1.762821,-8.143697,1.039039,9.539260,4.164057,5.348794,-1.110294]],[[-2.730355,5.305017,2.531783,3.577517,9.804646,7.729308,8.569864,-9.345092,-9.830107,8.205659,-9.671810,2.181355,3.514370,-7.315955],[3.019230,4.275856,8.907046,9.068249,-5.356920,-2.020593,8.716249,9.697939,2.765896,3.126530,7.923553,-4.934341,8.581059,4.863616],[-4.661733,-1.112390,-2.962234,-6.488357,-5.465459,-1.286342,-7.400974,-9.876175,-6.822162,-0.758795,-0.270973,-1.184172,-0.412737,9.630212],[-4.068622,4.583038,-2.292660,-2.018539,6.723564,-7.628767,-6.309178,-4.369403,7.646295,3.510861,-5.224342,6.309485,5.841950,-5.810459],[4.796940,7.788745,-6.384576,-0.114999,-8.209363,9.985480,2.951681,8.327041,-6.985982,-0.278208,6.792785,5.573644,2.837561,-9.729679],[-4.027963,6.869766,-2.439998,-4.310046,8.535582,4.277877,6.350157,9.827281,-1.214678,0.359812,-0.040442,-7.774567,7.154820,1.023533],[-1.572604,7.324186,-0.656205,-0.330440,4.637495,6.673262,-4.937638,1.033064,7.315217,-2.633846,2.701865,-9.803588,-9.938511,7.657182],[-8.566044,-2.859105,-8.408454,-2.123577,-7.828071,7.143740,6.788305,-8.980382,9.420961,8.276502,-8.854590,-1.613720,9.211396,0.588897],[2.002997,2.674314,3.743802,8.206226,9.574068,-6.799105,-1.800538,-0.499514,-3.090717,0.719320,-5.965109,-6.817477,5.347478,-8.736763],[8.485900,-7.383875,5.623442,0.943020,2.301867,-6.640415,-3.967456,1.466614,2.724254,-4.361691,-2.173675,5.030131,-8.643614,-3.463565],[4.476922,4.516292,-4.242215,7.413375,1.997393,6.109760,7.637520,-3.242258,-4.327854,9.880733,0.087756,-7.590735,5.259424,-8.405920]],[[4.157563,3.823923,9.751958,-3.683199,-0.154512,5.332233,-9.906969,8.513638,7.445223,8.931624,2.147306,1.900408,-5.723179,-3.481527],[9.965363,9.000753,7.627711,0.586574,9.709822,8.191568,-9.294292,-0.437764,1.978244,-5.819134,9.516578,-0.829851,-9.780347,7.322773],[9.577548,7.437731,-0.714388,-6.131240,7.191080,-5.273990,8.040751,4.723876,4.887493,-1.878075,6.013722,5.632031,-6.078917,2.738627],[2.447323,6.105247,-0.010739,2.731221,8.438002,8.360800,-2.371154,-3.433062,8.711075,0.205057,2.595960,1.427427,-6.584829,4.773854],[-7.722518,-6.990050,7.943421,0.965102,-7.900666,-4.527588,-8.772518,-6.592653,3.223083,-7.639274,-5.610050,3.182208,4.281950,-8.329713],[9.363175,-1.545622,-3.858002,5.405904,-3.138608,-7.378996,-7.359004,-4.439756,-6.859414,3.951717,0.233667,-6.035737,9.047505,7.385847],[-6.805261,-9.051612,8.347600,6.432251,5.683368,6.234254,5.539410,-4.586878,-4.772115,-4.741286,-1.947590,4.672885,1.423708,4.534548],[9.352903,0.577436,1.854389,-6.388520,-3.744724,-5.644210,-9.394019,2.364245,8.916595,0.965795,4.540501,-5.078108,3.396540,9.349589],[3.030358,2.641688,-2.182566,-4.707967,7.996117,-5.587622,1.995473,9.584983,5.296036,3.322859,2.400547,-3.273988,6.805635,-5.543751],[-9.699852,6.402070,-0.736690,4.910691,-8.911270,-0.723439,-3.150112,8.396345,-5.028461,2.132225,-5.491830,-9.344751,-4.245721,-4.913633],[-3.516270,-5.428213,-9.571649,-0.577714,8.508906,2.310108,-6.174146,4.786532,4.027087,-5.811889,5.051505,0.551811,-6.540981,8.758749]],[[-2.711664,-1.837877,-6.558932,-2.317882,1.855588,-2.461190,-6.879548,-4.409040,9.971031,4.796127,-1.237650,-3.206581,6.571636,3.658394],[-3.170886,-3.152050,-6.548871,3.203137,-6.261374,-7.924891,-7.832788,-7.794564,-0.470982,9.150646,-5.674595,-2.313407,-6.865665,-0.670261],[-6.788061,-9.222744,3.292248,-7.250118,3.550288,-8.286836,5.182897,7.396078,9.608907,-2.238177,-4.802949,-6.039243,-8.536732,-8.268605],[9.398675,-0.490256,-9.214355,-3.757481,-5.436578,-7.760078,-5.617107,4.502107,6.304214,-8.892827,-6.664951,-3.024659,-4.133030,9.560149],[-3.174538,-0.045883,-7.850335,9.987290,7.122574,-1.749069,-7.907256,3.292139,-0.639752,-0.096623,-8.586552,-4.510653,3.551221,9.791525],[6.835147,-8.373993,-7.228423,-7.262967,-9.976102,-5.136665,8.445485,3.595745,3.446291,2.821741,0.089499,3.132368,-0.175846,-2.990720],[-0.421276,6.763543,-8.223415,1.369347,-1.342087,8.631320,-5.746657,-7.024701,4.165543,9.700851,9.622025,-0.828231,9.180141,-0.019730],[2.181068,1.891881,-9.397917,-0.638498,3.210155,-4.439700,8.756685,-8.507992,1.590061,8.616803,-4.127846,8.964295,4.274679,-8.959649],[7.743416,-9.030377,5.702431,-1.674145,9.087350,-6.611726,1.919946,-2.213836,-6.138231,-2.420249,-7.629012,-4.296329,-1.351219,-2.090651],[2.128086,-9.068740,8.957407,-0.317318,0.295335,-8.609204,3.907223,2.338239,2.365444,1.424719,-4.143669,5.774827,4.246537,9.137077],[0.540772,-6.898681,-4.270172,8.321345,4.714674,-1.975410,5.727093,4.023160,7.690551,3.010587,9.599547,-5.137419,-0.514921,-5.343541]]], dtype = "float32")#candidate|6627|(15, 11, 14)|const|float32
bop_6628 = relay.floor_divide(var_6626.astype('float32'), relay.reshape(const_6627.astype('float32'), relay.shape_of(var_6626))) # shape=(15, 11, 14)
bop_6632 = relay.greater_equal(var_6626.astype('bool'), relay.reshape(const_6627.astype('bool'), relay.shape_of(var_6626))) # shape=(15, 11, 14)
output = relay.Tuple([bop_6628,bop_6632,])
output2 = relay.Tuple([bop_6628,bop_6632,])
func_6636 = relay.Function([var_6626,], output)
mod['func_6636'] = func_6636
mod = relay.transform.InferType()(mod)
mutated_mod['func_6636'] = func_6636
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6637 = relay.var("var_6637", dtype = "float32", shape = (15, 11, 14))#candidate|6637|(15, 11, 14)|var|float32
func_6636_call = mutated_mod.get_global_var('func_6636')
call_6638 = func_6636_call(var_6637)
output = call_6638
func_6639 = relay.Function([var_6637], output)
mutated_mod['func_6639'] = func_6639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6863 = relay.var("var_6863", dtype = "bool", shape = (14, 13, 10))#candidate|6863|(14, 13, 10)|var|bool
var_6864 = relay.var("var_6864", dtype = "bool", shape = (14, 13, 10))#candidate|6864|(14, 13, 10)|var|bool
bop_6865 = relay.logical_or(var_6863.astype('bool'), relay.reshape(var_6864.astype('bool'), relay.shape_of(var_6863))) # shape=(14, 13, 10)
func_2741_call = mod.get_global_var('func_2741')
func_2746_call = mutated_mod.get_global_var('func_2746')
const_6871 = relay.const([-8.691177,-3.359461,7.154608,4.750651,9.413423,-2.304461,7.522377,5.355403,7.142373,-8.482037,-3.051551,1.566421,-4.786082,2.156489,1.145262,-8.867831,-3.096947,-5.772194,7.797047,6.373380,-3.533400,9.865814,6.126751,-5.925717,4.067642,-2.915643,6.977397,-1.144180,-5.744718,5.445807,1.061709,8.753619,1.206161,9.544929,-5.494925,8.292544,-4.942061,-7.547817,5.343047,4.117223], dtype = "float64")#candidate|6871|(40,)|const|float64
const_6872 = relay.const([[-8,5,-1,-4,-9,-10,10,4,2,7,1,4,2,-1,-7,10,-7,-7,-5,9,-3,-4,-4,8,-2,-5,-2,-6,-8,5,9,9,2,8,-9,1,5,-5,-4,5,8,8,1,-6,10,-4,-9,-8,-1,8,1,-3,5,-7,3,-4,6,-2,-9,-5,2,-9,-4,-1,1,-6,1,3,7,6,4,10,-5,6,-1,-10,-2,-5,5,-1,7,3,7,7,-5,-4,4,-8,6,-10,5,-1,10,3,-4,-6,-4,-3,4,-2,1,-8,10,4,10,-5,4,1,-4,1,-3,-2,-3,-5,-3,8,5,-10,1,-2,-6,7,-5,-3,-5,8,1,-4,-3,3,-9,1,-6,10,-5,-2,9,2,-8,-10,1,-2,8,-7,6,-8,-3,-9,-1,10,-1,-10,10,2,-9,2,2,4,-9,-2,3,9,2,4,-7,1,5,-8,-5,4,3,-8,9,7,-3,4,-1,-9,-3,8,7,9,3,10,6,-4,1,5,3,1,-3,9,10,-8,-3,2,-6,-4,8,8]], dtype = "int64")#candidate|6872|(1, 200)|const|int64
var_6873 = relay.var("var_6873", dtype = "float32", shape = (495,))#candidate|6873|(495,)|var|float32
call_6870 = relay.TupleGetItem(func_2741_call(relay.reshape(const_6871.astype('float64'), [1, 5, 8]), relay.reshape(const_6872.astype('int64'), [200,]), relay.reshape(var_6873.astype('float32'), [495,]), ), 2)
call_6874 = relay.TupleGetItem(func_2746_call(relay.reshape(const_6871.astype('float64'), [1, 5, 8]), relay.reshape(const_6872.astype('int64'), [200,]), relay.reshape(var_6873.astype('float32'), [495,]), ), 2)
output = relay.Tuple([bop_6865,call_6870,const_6871,const_6872,var_6873,])
output2 = relay.Tuple([bop_6865,call_6874,const_6871,const_6872,var_6873,])
func_6901 = relay.Function([var_6863,var_6864,var_6873,], output)
mod['func_6901'] = func_6901
mod = relay.transform.InferType()(mod)
mutated_mod['func_6901'] = func_6901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6901_call = mutated_mod.get_global_var('func_6901')
var_6903 = relay.var("var_6903", dtype = "bool", shape = (14, 13, 10))#candidate|6903|(14, 13, 10)|var|bool
var_6904 = relay.var("var_6904", dtype = "bool", shape = (14, 13, 10))#candidate|6904|(14, 13, 10)|var|bool
var_6905 = relay.var("var_6905", dtype = "float32", shape = (495,))#candidate|6905|(495,)|var|float32
call_6902 = func_6901_call(var_6903,var_6904,var_6905,)
output = call_6902
func_6906 = relay.Function([var_6903,var_6904,var_6905,], output)
mutated_mod['func_6906'] = func_6906
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6931 = relay.var("var_6931", dtype = "int8", shape = (14, 11, 13))#candidate|6931|(14, 11, 13)|var|int8
var_6932 = relay.var("var_6932", dtype = "int8", shape = (14, 11, 13))#candidate|6932|(14, 11, 13)|var|int8
bop_6933 = relay.multiply(var_6931.astype('int8'), relay.reshape(var_6932.astype('int8'), relay.shape_of(var_6931))) # shape=(14, 11, 13)
output = relay.Tuple([bop_6933,])
output2 = relay.Tuple([bop_6933,])
func_6947 = relay.Function([var_6931,var_6932,], output)
mod['func_6947'] = func_6947
mod = relay.transform.InferType()(mod)
var_6948 = relay.var("var_6948", dtype = "int8", shape = (14, 11, 13))#candidate|6948|(14, 11, 13)|var|int8
var_6949 = relay.var("var_6949", dtype = "int8", shape = (14, 11, 13))#candidate|6949|(14, 11, 13)|var|int8
output = func_6947(var_6948,var_6949,)
func_6950 = relay.Function([var_6948,var_6949,], output)
mutated_mod['func_6950'] = func_6950
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7381 = relay.var("var_7381", dtype = "uint16", shape = ())#candidate|7381|()|var|uint16
const_7382 = relay.const([[[10,2,-9,-7,-5,1,5,2,6,8,-9,-6,-1],[10,-7,-5,8,-8,-6,-2,-8,-8,10,6,-9,2]],[[7,3,-6,-4,-5,-1,-10,1,-4,8,-6,4,6],[4,6,3,5,-1,-8,-5,8,7,-6,4,1,-3]],[[-8,-5,-9,-2,-6,-6,1,-3,4,4,-5,-10,9],[-1,5,7,1,10,2,4,-8,-8,-10,10,8,-8]],[[4,6,-9,2,-2,-9,-3,-4,-2,-1,-9,-1,-2],[2,4,-5,-7,10,7,-2,-4,-4,10,2,-6,-4]],[[3,-3,4,-5,7,-7,-10,-10,2,7,-3,-5,-9],[-4,-9,10,-4,7,10,8,-3,-10,5,-1,4,-5]],[[9,9,-4,-4,3,-6,-7,-5,-8,-2,8,-3,6],[10,-2,-6,-4,2,7,-2,8,-7,5,-1,3,-4]],[[-7,-5,-1,-2,9,-7,-2,10,4,2,-2,-8,1],[7,-3,8,-10,-3,-8,-5,3,-10,10,6,2,8]],[[7,10,-3,3,-10,6,-3,-10,-5,8,8,3,-7],[-3,-9,4,5,5,3,-6,10,-2,10,-4,10,3]],[[7,7,6,-3,-1,2,-1,5,-6,6,2,9,-1],[-9,2,-8,-9,-2,-4,-2,2,-2,1,-6,8,-5]],[[9,4,-6,2,4,-8,4,10,7,-5,-3,3,-6],[-3,10,-7,-1,-10,4,8,1,-3,-7,4,-4,-6]],[[-8,3,7,-8,-3,7,-6,2,8,-9,7,5,6],[10,10,7,7,2,5,3,7,-3,-7,-2,-6,-8]],[[-5,-6,4,-9,4,-2,5,6,-6,-9,9,5,-8],[4,1,6,5,-7,2,1,3,8,9,-9,3,9]],[[1,-1,-4,2,7,1,3,-10,3,2,7,3,4],[-5,9,2,-2,8,7,1,-1,-5,8,1,9,7]]], dtype = "uint16")#candidate|7382|(13, 2, 13)|const|uint16
bop_7383 = relay.logical_xor(var_7381.astype('uint16'), const_7382.astype('uint16')) # shape=(13, 2, 13)
func_6481_call = mod.get_global_var('func_6481')
func_6484_call = mutated_mod.get_global_var('func_6484')
const_7388 = relay.const([1.724976,2.966935,-7.436894,6.026408,-9.762808,-7.808241,-7.134111,5.955172,5.327750,3.078249,-6.059956,0.921943,5.291272,-8.091984,3.022567,5.502321,4.889085,2.642195,-7.511041,-1.235210,4.328890,0.346126,7.407985,-8.405390,-3.183784,9.845362,3.213248,6.572860,-9.431607,7.267595,-0.754907,-0.114150,5.271346,2.051334,-4.169585,-1.743095,-5.659247,1.800089,-3.977873,-0.063981,6.603056,-4.356750,-3.126572,-3.430213,6.012287,-3.669272,-1.681225,1.817128,-0.463380,9.366066,-8.410257,0.047489,-9.696036,5.804520,-3.393665,0.154949,4.229561,-3.430740,1.535211,-4.066900,-6.451298,-3.949031,6.911581,-1.734191,-3.933859,9.978123,-8.345505,-1.930196,8.946470,1.787259,5.197520,-4.242133,-8.452220,1.619870,6.150003,7.714586,-7.153329,-1.189920,7.630527,-2.132594,8.132930,2.103131,-1.921293,-4.997844,0.605679,4.432367,-1.081069,0.179570,-2.395807,-7.333330,1.665852,4.631649,-0.261809,2.050707,-2.822774,5.509200,0.610146,4.125695,-3.203783,-4.977788,-7.114248,9.498993,5.405731,3.416963,0.140806,1.994524,0.735921,-9.726793,-0.635954,-6.710554,9.052830,-7.711126,-5.103774,-1.457041,7.423796,-1.185836,-8.858128,-7.297406,-8.531979,7.898934,-0.797643,-9.711174,2.610553,6.651087,1.363985,1.032203,5.298223,1.333492,5.774704,6.380119,-0.936700,-4.715324,5.644257,-2.374583,4.144885,2.201512,-5.205150,6.853219,-6.409194,-3.604635,-9.360254,2.910279,5.657114,2.632969,-8.872810,-5.586397,-6.106384,-6.656528,4.851477,-3.539550,-8.643509,-0.808026,6.980099,3.841435,-7.737702,4.764150,2.700726,4.315762,-2.789447,0.989125,5.076249,6.737292,9.033449,2.168933,4.786572,8.122014,2.575793,-1.786623,7.499658,-5.422741,7.217328,7.350979,-9.730040,-7.264322,1.869182,-7.929151,7.018731,8.413221,3.611947,1.508439,-5.477999,-1.173489,8.819467,-4.508829,-3.388188,-7.978065,1.223219,-3.614515,-3.456106,-0.896460,6.437085,-2.425040,-1.112284,4.191319,-8.114770,-5.660642,5.111653,-5.171172,-9.527113,6.742728,-2.431963,-1.186926,8.041954,3.059704,5.540798,-9.337649,-4.371476,9.772053,-2.642336,-2.761097,-4.293838,4.765746,-5.145783,-6.936478,-9.231699,8.524029,4.862568,-3.993632,3.797423,0.963989,4.365826,8.647471,-5.133898,8.167213,2.330293,-1.897228,-8.812769,3.359601,4.707270,5.701800,6.347767,-9.578057,8.746984,-6.312377,7.331208,9.033019,7.467161,-5.395927,-1.102736,-3.248852,-1.854859,1.692772,-6.610373,2.920346,-0.601538,0.822429,2.204674,-9.040123,7.502450,7.180363,-2.047685,9.050373,4.116897,-9.488295,2.061761,5.603339,9.762905,0.360931,1.397217,1.504557,7.184451,-8.002169,6.579515,1.501212,2.542264,6.738840,-8.823095,4.117222,-4.181335,5.564574,-8.508039,8.265011,4.070472,1.093958,9.434156,-5.159136,2.150369,-1.062315,8.415039,0.397389,-4.336598,7.510729,-4.034370,7.183411,-6.785680,-3.691188,7.457091,-5.455752,-7.011283,-1.196792,-9.008978,4.935860,7.602051,-8.363890,1.173140,2.844537,-0.584051,-4.617383,6.272008,-2.739414,-7.814300,-5.412634,-2.138291,-0.259394,-6.308777,5.650261,3.122432,-5.972036,-8.721982,-5.943068,6.579988,4.929814,-3.437413,-0.706837,7.849586,4.541634,6.529562,-1.156704,-9.199488,4.338712,4.826184,3.225824,7.519617,0.639216,9.974655,9.563555,2.831369,-5.815748,5.951413,0.134547,5.172307,-2.894036,-7.913216,7.217187,-6.709650,0.714971,8.204582,-0.421127,-9.671242,-2.256911,0.166780,-5.912843,-3.462688,-9.732486,8.719704,5.355451,-3.752942,-7.705876,-5.650562,6.409152,-0.346798,-5.154213,-8.612171,-1.859909,-9.635636,-9.853224,-5.905895,-6.419430,5.563089,-5.205114,-7.089697,-3.878584,-3.477684,7.335486,-6.392822,7.995503,8.800595,-2.538292,-0.452652,-9.864106,3.322547,3.725139,-7.703345,-0.963987,-9.798862,-8.598079,-5.063840,-0.246563,1.828012,5.688826,-8.787308,-9.087886,-8.779306,7.009160,1.400569,6.861462,-3.771396,5.955347,-7.865303,0.024558], dtype = "float32")#candidate|7388|(390,)|const|float32
call_7387 = relay.TupleGetItem(func_6481_call(relay.reshape(const_7388.astype('float32'), [13, 6, 5])), 0)
call_7389 = relay.TupleGetItem(func_6484_call(relay.reshape(const_7388.astype('float32'), [13, 6, 5])), 0)
output = relay.Tuple([bop_7383,call_7387,const_7388,])
output2 = relay.Tuple([bop_7383,call_7389,const_7388,])
func_7391 = relay.Function([var_7381,], output)
mod['func_7391'] = func_7391
mod = relay.transform.InferType()(mod)
mutated_mod['func_7391'] = func_7391
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7392 = relay.var("var_7392", dtype = "uint16", shape = ())#candidate|7392|()|var|uint16
func_7391_call = mutated_mod.get_global_var('func_7391')
call_7393 = func_7391_call(var_7392)
output = call_7393
func_7394 = relay.Function([var_7392], output)
mutated_mod['func_7394'] = func_7394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7421 = relay.var("var_7421", dtype = "float32", shape = (7, 10, 7))#candidate|7421|(7, 10, 7)|var|float32
uop_7422 = relay.sigmoid(var_7421.astype('float32')) # shape=(7, 10, 7)
func_4760_call = mod.get_global_var('func_4760')
func_4763_call = mutated_mod.get_global_var('func_4763')
var_7425 = relay.var("var_7425", dtype = "int64", shape = ())#candidate|7425|()|var|int64
const_7426 = relay.const([-4,3,8,4,2,5,7,-4,-7,-7,-5,6,-6,-4,-3,6,-7,3,-9,-7,1,10,6,-2,-7,5,-7,3,-5,-6,3,-6,-2,-6,-7,9,-7,-8,3,7], dtype = "int64")#candidate|7426|(40,)|const|int64
call_7424 = relay.TupleGetItem(func_4760_call(relay.reshape(var_7425.astype('int64'), []), relay.reshape(const_7426.astype('int64'), [4, 1, 10]), ), 0)
call_7427 = relay.TupleGetItem(func_4763_call(relay.reshape(var_7425.astype('int64'), []), relay.reshape(const_7426.astype('int64'), [4, 1, 10]), ), 0)
bop_7433 = relay.maximum(uop_7422.astype('uint16'), var_7425.astype('uint16')) # shape=(7, 10, 7)
func_1874_call = mod.get_global_var('func_1874')
func_1877_call = mutated_mod.get_global_var('func_1877')
const_7437 = relay.const([False,False,True,False,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,False,True,True,False,False,False,False,True,False,True], dtype = "bool")#candidate|7437|(44,)|const|bool
call_7436 = relay.TupleGetItem(func_1874_call(relay.reshape(var_7425.astype('bool'), []), relay.reshape(const_7437.astype('bool'), [1, 4, 11]), ), 0)
call_7438 = relay.TupleGetItem(func_1877_call(relay.reshape(var_7425.astype('bool'), []), relay.reshape(const_7437.astype('bool'), [1, 4, 11]), ), 0)
func_5526_call = mod.get_global_var('func_5526')
func_5529_call = mutated_mod.get_global_var('func_5529')
var_7454 = relay.var("var_7454", dtype = "int32", shape = (676,))#candidate|7454|(676,)|var|int32
call_7453 = func_5526_call(relay.reshape(var_7454.astype('int32'), [13, 4, 13]))
call_7455 = func_5526_call(relay.reshape(var_7454.astype('int32'), [13, 4, 13]))
output = relay.Tuple([call_7424,const_7426,bop_7433,call_7436,const_7437,call_7453,var_7454,])
output2 = relay.Tuple([call_7427,const_7426,bop_7433,call_7438,const_7437,call_7455,var_7454,])
func_7461 = relay.Function([var_7421,var_7425,var_7454,], output)
mod['func_7461'] = func_7461
mod = relay.transform.InferType()(mod)
mutated_mod['func_7461'] = func_7461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7461_call = mutated_mod.get_global_var('func_7461')
var_7463 = relay.var("var_7463", dtype = "float32", shape = (7, 10, 7))#candidate|7463|(7, 10, 7)|var|float32
var_7464 = relay.var("var_7464", dtype = "int64", shape = ())#candidate|7464|()|var|int64
var_7465 = relay.var("var_7465", dtype = "int32", shape = (676,))#candidate|7465|(676,)|var|int32
call_7462 = func_7461_call(var_7463,var_7464,var_7465,)
output = call_7462
func_7466 = relay.Function([var_7463,var_7464,var_7465,], output)
mutated_mod['func_7466'] = func_7466
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7470 = relay.var("var_7470", dtype = "float32", shape = (15, 10, 4))#candidate|7470|(15, 10, 4)|var|float32
const_7471 = relay.const([[[-8.873759,8.196588,-7.342222,5.733045],[6.725028,-5.986236,-1.016033,4.658399],[-8.381306,-6.066996,6.308409,3.477932],[-2.153171,5.301099,-3.189682,1.165743],[0.439871,-3.356957,-2.589740,-6.545880],[7.758465,-0.802087,-1.486072,4.896688],[2.234095,-4.318617,-5.474711,0.554022],[8.007008,8.014376,0.105692,-3.832147],[3.869798,0.730671,-0.358130,-2.545825],[-5.392914,8.523385,-6.665840,6.771457]],[[-1.443225,-6.239576,5.349543,-7.862978],[-6.136079,-8.767199,-0.516400,-4.830270],[4.908486,-2.230782,8.661363,2.184997],[4.968006,5.469043,-7.633685,-3.039396],[-4.186744,4.103232,-5.225887,-0.473393],[3.344180,-1.193668,6.237752,-4.169472],[-7.558418,-8.713713,8.452161,9.974142],[-7.917056,-1.162937,8.847328,-2.301074],[1.276500,-8.319818,9.870459,-5.592610],[2.910312,-8.324226,7.001726,-1.030402]],[[7.309265,4.961469,-6.679398,-5.097024],[8.367605,3.626657,4.104240,-0.765509],[9.428241,-2.886812,8.323346,-0.892795],[8.909908,7.593699,8.795643,8.610149],[-6.351793,0.233345,0.827332,-1.603876],[-6.668473,-8.555431,1.251957,-6.212902],[7.610020,3.173842,6.548735,0.707246],[-3.079434,2.188600,-4.750251,6.967304],[6.870174,-3.062558,-0.060100,-6.862159],[-4.111837,-8.524862,3.506714,1.126046]],[[3.513365,-5.734070,-4.407681,2.119129],[-7.053919,-5.839058,7.870617,-6.767762],[-1.005816,-1.424145,5.705546,2.971150],[0.466741,0.607120,-3.912323,7.526273],[5.464852,-9.716819,0.464272,-5.463894],[-1.967566,3.131533,-4.408878,-0.962428],[-7.059831,7.110865,2.904515,7.928975],[-9.227496,-7.411421,2.923070,-2.684908],[4.650817,-2.720522,9.325865,-8.957517],[8.070985,8.201679,6.188994,-4.309541]],[[-3.111074,4.152433,-8.268387,-9.242724],[8.216513,3.334260,-1.240716,9.242421],[-1.100273,9.470379,6.801806,4.835568],[3.011597,-1.992056,6.403571,-2.738875],[3.039273,7.482731,-3.043004,-0.093704],[-9.136938,3.960145,-7.726001,-5.505435],[-8.328298,-2.590678,-5.580336,1.083641],[-0.898793,-8.912364,-3.548010,-5.571149],[9.746460,-1.123457,6.733751,2.275338],[-2.759044,9.383654,-8.705480,-2.863469]],[[7.642691,-5.955725,-1.897180,9.533673],[8.093563,-7.782797,-6.564552,2.540696],[9.274416,5.070289,1.650665,-0.119089],[6.170337,-4.944476,-3.812514,6.014046],[7.467029,6.386950,7.338261,-4.012666],[-5.139645,-1.604046,7.965528,-6.630135],[7.026922,-1.801791,4.818793,5.464675],[-2.478879,-4.235259,-0.828984,-6.404206],[0.895975,3.392152,-3.222140,1.484688],[6.675906,1.410702,-4.828288,9.027301]],[[9.087836,-5.916197,-7.447282,-5.717235],[3.520390,6.071257,-0.282108,2.313433],[3.743778,-7.132604,-1.777231,2.438583],[3.665604,9.805435,-1.646927,-4.348684],[-9.750018,-3.982176,-1.404008,5.086711],[0.565863,5.463736,-1.180775,9.562001],[0.232564,8.740933,-9.683190,3.141343],[8.031333,2.297001,8.596020,2.010386],[-9.758280,0.394922,-7.282273,-9.400612],[3.807554,9.967299,-2.600131,-1.447218]],[[-5.665396,8.253394,-9.491306,0.689447],[5.973900,4.125739,-0.257549,-1.350168],[0.608528,2.977488,-4.585532,0.296167],[8.747877,7.926936,-3.531904,3.738492],[2.449691,3.258261,-8.583589,2.580538],[1.218433,-0.952808,-4.347754,-8.592790],[-8.229914,6.968146,6.119219,6.222955],[-1.746708,-0.623719,-0.338025,1.373711],[-9.668609,3.817757,6.261061,0.015474],[7.043555,-6.881684,-8.617458,5.026677]],[[-5.779582,-8.653979,-9.900708,-9.144765],[-4.384013,3.140971,0.798616,2.293846],[6.928421,-8.646156,0.405062,0.876864],[3.674396,-4.531285,-5.309394,4.351237],[4.929827,-7.518066,6.698385,-4.722786],[5.966934,-9.853948,-6.005953,-8.701854],[-1.097858,7.904270,-5.959885,-8.518977],[-4.844563,-6.913182,2.841302,-5.729571],[1.578224,-0.449515,9.792424,-4.097979],[-1.759019,6.888819,-7.135607,-3.229039]],[[-3.374162,3.490191,-5.071265,5.678528],[-3.878714,3.669812,8.437377,-4.050771],[-8.034537,3.951328,4.049906,-1.734352],[-5.206169,9.303703,7.652270,8.703323],[0.121286,9.469680,-1.624890,-6.328770],[-0.450101,-8.897328,0.061585,-4.983293],[1.523340,-6.429469,4.392923,-8.095900],[-6.894693,8.915622,8.593035,-3.069365],[7.508505,-5.731066,-8.711826,-8.260417],[-4.704330,-3.790823,-7.283553,1.996017]],[[-8.633584,-3.075367,-6.605317,2.714987],[-2.986547,4.808299,1.302143,-2.325906],[0.590907,-1.118825,-1.957811,-2.987569],[-5.810061,-3.844608,9.536493,-4.720425],[0.315707,0.099399,-0.786948,3.897639],[3.979388,-1.352135,-4.672204,9.506061],[-9.144743,2.632836,6.747656,1.225924],[-4.011504,-6.820328,-3.884079,9.037780],[3.238149,2.329519,2.750366,6.920010],[7.422622,2.100349,-6.738700,2.742960]],[[-2.570841,0.240095,-1.066388,2.429710],[0.751176,-1.600120,2.696632,9.704378],[1.772985,-6.774764,8.409189,6.213417],[8.089908,-1.473607,-6.909326,-2.554055],[-6.981616,-9.389752,1.241695,0.690216],[9.993509,-0.503730,1.936238,4.996019],[-4.936158,9.974368,9.625722,0.914876],[9.600535,8.146126,2.240575,4.770245],[8.197423,3.189776,5.226082,1.323308],[-7.657404,9.135212,-3.506004,-5.256228]],[[-3.802863,-9.865860,5.819950,9.191416],[-6.467587,-5.582318,-4.345942,7.083193],[0.986561,-7.395267,-0.926442,2.003145],[4.649013,-4.520627,0.127758,1.243471],[3.174258,-0.990255,5.361825,0.612909],[-2.483482,6.457600,8.424464,-5.849391],[7.607606,-3.860643,3.024803,1.988019],[-2.351582,-4.155664,-9.525025,-1.408678],[6.633200,-4.738472,-8.487644,-4.826626],[3.413412,7.619610,1.890666,4.697916]],[[8.432303,-6.217639,3.940433,2.067511],[8.162256,-3.642923,6.670582,6.417188],[9.068720,5.919078,-5.381484,-0.371078],[-5.860257,-2.897025,6.110301,-3.664095],[0.733056,3.543209,-8.529813,5.523636],[-4.143921,-2.698050,-3.043933,6.322810],[4.622352,2.046623,-7.314163,-8.343320],[3.305751,-5.546542,-8.561206,6.503005],[9.235699,4.355458,-7.752188,-0.329894],[-6.214860,-2.572089,-8.815193,-0.195581]],[[5.264163,7.111523,3.525370,-7.982035],[9.104414,6.305771,3.630470,0.469749],[-4.657532,6.357106,3.642033,4.804463],[-3.582791,-8.592934,3.240990,-8.823015],[-3.383403,9.392681,2.338216,5.274930],[-9.638485,5.415266,3.322277,9.717401],[6.683025,-9.559998,-5.098709,-0.925981],[-9.882082,6.020272,8.767326,-8.347465],[-4.505291,3.556699,0.683897,-8.196534],[6.691774,4.291514,-5.323216,-7.243157]]], dtype = "float32")#candidate|7471|(15, 10, 4)|const|float32
bop_7472 = relay.floor_divide(var_7470.astype('float32'), relay.reshape(const_7471.astype('float32'), relay.shape_of(var_7470))) # shape=(15, 10, 4)
output = bop_7472
output2 = bop_7472
func_7485 = relay.Function([var_7470,], output)
mod['func_7485'] = func_7485
mod = relay.transform.InferType()(mod)
mutated_mod['func_7485'] = func_7485
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7486 = relay.var("var_7486", dtype = "float32", shape = (15, 10, 4))#candidate|7486|(15, 10, 4)|var|float32
func_7485_call = mutated_mod.get_global_var('func_7485')
call_7487 = func_7485_call(var_7486)
output = call_7487
func_7488 = relay.Function([var_7486], output)
mutated_mod['func_7488'] = func_7488
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7498 = relay.const([[[4,-4,-10,-5,-3,-7,2,2,10,8,-8,-1,-9,-4,10,10]],[[5,3,8,-4,-2,-2,5,-4,7,6,-8,-6,1,-1,-3,-9]],[[8,2,1,-9,-9,9,-2,10,-6,5,-3,-8,-1,7,3,-10]],[[7,7,2,-1,4,4,5,-7,2,5,-3,2,-4,-5,7,8]],[[-1,-4,-8,3,-8,-1,-3,-2,-2,-10,1,-6,5,2,1,7]],[[-2,3,9,5,5,8,4,-2,-8,9,6,-4,1,2,5,-1]],[[4,8,-2,-9,-9,-6,1,-9,-2,-10,-6,-9,10,8,-3,-4]],[[-5,-10,-7,7,-10,-7,10,-1,4,1,6,8,3,3,7,5]],[[-2,-2,-6,5,1,-6,-7,5,6,5,8,-8,-1,9,10,3]],[[-8,3,3,9,-9,7,2,9,-8,10,10,-6,-10,-3,8,-4]],[[-1,2,2,-8,-6,7,6,6,2,9,3,-5,2,-3,3,7]],[[-4,-8,10,-7,2,4,10,4,-3,4,-10,-9,8,-3,1,5]],[[-8,-2,-8,5,-1,-9,-7,2,8,6,-4,2,-10,3,6,-7]],[[-10,3,5,1,4,-6,-5,-3,-4,-2,-5,-2,-1,6,-4,2]]], dtype = "int32")#candidate|7498|(14, 1, 16)|const|int32
var_7499 = relay.var("var_7499", dtype = "int32", shape = (14, 15, 16))#candidate|7499|(14, 15, 16)|var|int32
bop_7500 = relay.maximum(const_7498.astype('int32'), var_7499.astype('int32')) # shape=(14, 15, 16)
func_6390_call = mod.get_global_var('func_6390')
func_6392_call = mutated_mod.get_global_var('func_6392')
var_7504 = relay.var("var_7504", dtype = "int32", shape = (672,))#candidate|7504|(672,)|var|int32
call_7503 = relay.TupleGetItem(func_6390_call(relay.reshape(var_7504.astype('int32'), [16, 3, 14])), 0)
call_7505 = relay.TupleGetItem(func_6392_call(relay.reshape(var_7504.astype('int32'), [16, 3, 14])), 0)
func_4667_call = mod.get_global_var('func_4667')
func_4673_call = mutated_mod.get_global_var('func_4673')
const_7511 = relay.const([-3,-7,1,1,-4,7,4,-3,10,4,-7,-10,-2,9,3,6,-8,-4,5,-7,4,-5,2,3,-5,-8,2,1,-8,-5,-10,-7,-6,-9,8,-3,8,3,6,-1,-2,5,-8,7,9,-9,3,-9,-10,-1,4,3,2,1,-1,-2,3,7,6,-1,6,-5,-7,7,3,-8,-3,-9,8,-6,-4,1,8,3,2,10,-4,-6,-9,8,2,-9,8,4,9,4,8,3,5,-1,-9,-4,6,-4,2,7,10,1,-7,2,4,-1,3,-10,9,-5,2,1,-7,3,7,-7,9,2,4,-1,-2,-3,-4,3,-4,-4,-8,-6,-8,-6,10,-9,-1,4,9,-4,-6,5,-9,5,-9,-2,4,1,7,-6,-1,8,9,9,-7,-8,9,-5,4,-4,1,-9,3,6,7,1,-8,-2,-2,3,-4,-4,-4,3,-3,2,-2,8,9,7,7,-4,6,-9,6,2,3,-3,7,7,-3,-3,-8,-10,8,-4,5,7,5,2,10,-3,9,1,2,-7,7,-9,2,5,-7,4,-9,3,-9,-5,-8,1,4,5,-10,-10,2,-5,9,6,-8,-7,-1,9,5,8,-4,-3,1,-6,-2,-9,8,-1,-1,-2,-7,-4,-9,-10,-10,-8,-7,5,-10,-8,-7,-7,10,-1,-6,2,4,-6,2,5,-4,8,-5,1,4,-8,-8,-8,-4,1,-6,5,-8,10,7,-2,2,2,3,-5,-3,-9,-9,-1,-8,4,5,1,-10,-5,-8,-8,7,8,-3,8,-7,9,4,10,2,5,5,3,8,-4,5,7,-2,-3,-9,3,7,-3,-3,2,-8,5,2,-1,-3,7,7,-1,2,-5,6,6,-3,-4,-3,-2,-3,6,-4,-6,-2,-7,8,9,2,10,4,-1,6,-3,-2,-7,3,-8,2,6,-8,4,-8,7,-9,-10,-4,1,-8,8,3,-3,-1,-5,-7,-7,-1,3,6,-3,-9,-9,6,5,-6,4,-8,-8,-7,2,-4,-9,9,-6,1,9,4,5,6,6,2,-1,-4,-1,-2,5,1,-2,-5,5,-2,8,-10,8,4,10,-3,-8,2,9,2,1,-7,4,-5,-8,1,3,-10,7,-6,-1,10,7,9,-7,10,-4,4,9,-7,6,-4,1,-1,-9,7,-5,9,10,-8,9,-8,-6,-5,2,5,-1,-9,4,-1,7,1,7,-4,8,-6,1,-3,6,6,-9,-10,-10,3,8,-7,5,5,-9,-1,-10,-5,-2,-9,-4,10,6,6,-6,-1,4,-9,5,-1,2,1,-10,6,3,-2,-2,2,10], dtype = "int8")#candidate|7511|(490,)|const|int8
var_7512 = relay.var("var_7512", dtype = "uint32", shape = ())#candidate|7512|()|var|uint32
var_7513 = relay.var("var_7513", dtype = "uint32", shape = (121, 14))#candidate|7513|(121, 14)|var|uint32
const_7514 = relay.const([1,-9,-1,9,-6,2,-9,5,6,7,6,8,2,10,7,-2,-3,5,5,9,-8,3,-5,-3,2,10,-6,1,4,5,-5,2,-10,-3,2,-8,4,-8,-10,2,9,-1,-4,-4,-6,-2,7,-10,-2,4,6,4,3,-10,3,6,6,8,10,8,2,-8,5,-6,10,5,-1,-7,-1,9,9,-5,-5,-4,-6,2,6,6,5,-2,-5,-4,-4,-3,7,10,-9,10,-9,-10,1,-2,9,8,-4,-2,5,-5,6,5,-10,-9,9,3,-6], dtype = "int32")#candidate|7514|(105,)|const|int32
call_7510 = relay.TupleGetItem(func_4667_call(relay.reshape(const_7511.astype('int8'), [14, 5, 7]), relay.reshape(const_7511.astype('int8'), [14, 5, 7]), relay.reshape(var_7512.astype('uint32'), []), relay.reshape(var_7513.astype('uint32'), [1694,]), relay.reshape(const_7514.astype('int32'), [105,]), ), 3)
call_7515 = relay.TupleGetItem(func_4673_call(relay.reshape(const_7511.astype('int8'), [14, 5, 7]), relay.reshape(const_7511.astype('int8'), [14, 5, 7]), relay.reshape(var_7512.astype('uint32'), []), relay.reshape(var_7513.astype('uint32'), [1694,]), relay.reshape(const_7514.astype('int32'), [105,]), ), 3)
output = relay.Tuple([bop_7500,call_7503,var_7504,call_7510,const_7511,var_7512,var_7513,const_7514,])
output2 = relay.Tuple([bop_7500,call_7505,var_7504,call_7515,const_7511,var_7512,var_7513,const_7514,])
func_7524 = relay.Function([var_7499,var_7504,var_7512,var_7513,], output)
mod['func_7524'] = func_7524
mod = relay.transform.InferType()(mod)
mutated_mod['func_7524'] = func_7524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7524_call = mutated_mod.get_global_var('func_7524')
var_7526 = relay.var("var_7526", dtype = "int32", shape = (14, 15, 16))#candidate|7526|(14, 15, 16)|var|int32
var_7527 = relay.var("var_7527", dtype = "int32", shape = (672,))#candidate|7527|(672,)|var|int32
var_7528 = relay.var("var_7528", dtype = "uint32", shape = ())#candidate|7528|()|var|uint32
var_7529 = relay.var("var_7529", dtype = "uint32", shape = (121, 14))#candidate|7529|(121, 14)|var|uint32
call_7525 = func_7524_call(var_7526,var_7527,var_7528,var_7529,)
output = call_7525
func_7530 = relay.Function([var_7526,var_7527,var_7528,var_7529,], output)
mutated_mod['func_7530'] = func_7530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7553 = relay.var("var_7553", dtype = "float64", shape = (1, 2, 15))#candidate|7553|(1, 2, 15)|var|float64
uop_7554 = relay.cosh(var_7553.astype('float64')) # shape=(1, 2, 15)
func_3668_call = mod.get_global_var('func_3668')
func_3676_call = mutated_mod.get_global_var('func_3676')
var_7573 = relay.var("var_7573", dtype = "uint16", shape = (6, 100))#candidate|7573|(6, 100)|var|uint16
const_7574 = relay.const([1.933937,-3.830670,3.482408,8.648026,3.510537,2.138068,-3.136192,-1.255701,-9.472493,3.441420,-6.496297,-1.432862,1.229725,-1.058892,5.600115,3.031687,8.495910,3.774850,4.576383,7.622095,-4.450183,-4.257624,-4.661068,-5.306766,5.652123,5.255703,7.875522,-0.011859,8.088907,3.181389,-2.909908,7.865801,-1.413001,4.858037,7.888263,2.265267,6.262247,3.848984,-7.727144,-4.106538,8.664062,2.086340,6.983239,1.124711,9.214769,-6.409800,-2.104245,3.441416,-7.464165,-1.916809,3.802365,0.305338,-8.736592,-6.791348,-0.351830,-6.254628,-3.610163,4.214644,8.759247,3.118716,5.455110,-0.330287,9.242878,5.457936,-1.178847,-9.296979,1.206086,-3.746828,-7.879545,-3.464980,4.513973,-6.126030,-0.023325,-3.433571,1.113664,-3.110692,5.908631,-6.213945,-3.111503,-7.494406,0.114650,0.548583,-7.620162,-3.583084,-4.910152,-5.126659,7.989109,-2.522104,-1.126972,9.548627,-7.393677,-0.862662,5.790637,-8.542117,-2.677336,-4.898993,2.992377,-5.081831,-3.333295,-7.386830,2.566722,-9.761364,-1.837482,7.845420,8.749612,-9.553287,-3.228583,3.312492,3.703638,-8.569697,-1.877043,5.135096,-1.141166,-5.852603,9.632613,6.372114,3.396094,8.051667,-6.668210,-2.752012,-9.253120,5.839836,8.104150,-2.432927,8.313813,5.905818,9.465343,7.519120,-1.447164,-5.416932,2.755626,8.116226,-8.057180,-0.860179,9.531917,-0.636737,9.792686,-5.696258,9.307535,3.445391,2.942613,-1.040814,9.626623,-5.099956,0.214466,0.855263,5.396883,6.471817,-4.984009,-4.835728,-4.481258,7.550633,9.773269,8.162299,-6.877021,7.608504,0.335836,-6.333995,8.706706,-0.679212,-7.372169,4.822958,-4.542127,5.048666,-5.630591,-8.189513,-1.741104,-8.813838,-8.505699,-5.345354,-1.557261,-6.673067,-4.255268,4.436384,-8.935981,-7.239895,0.451487,-8.259945,5.977580,-3.953593,4.270379,-2.065861,-9.022756,8.805774,-1.779498,5.901299,9.584595,-2.150558,7.806876,-1.592931,-8.519175,-7.257588,-1.537750,2.414969,-8.101253,-6.761837,9.183374,0.598341,9.172280,-7.311375,3.512846,7.419555,1.600011,-5.738132,2.702418,-4.136253,2.942327,9.126911,0.315575,5.664549,0.293488,-4.775374,2.500820,-6.466201,-7.736295,-7.742584,1.668962,8.752882,-2.908737,1.846367,-6.634884,5.529088,-9.652920,3.792483,6.498461,7.197237,-5.431440,7.284656,8.194044,9.070839,-0.599366,0.817907,8.505862,9.384711,-1.549832,9.657275,-1.652868,0.498129,7.720991,7.508722,2.583083,6.377039,-0.188566,4.175944,1.860279,4.722478,9.157421,3.155610,5.807405,-5.517381,1.967429,-0.485852,-5.720424,-6.529416,6.595247,-5.027170,-5.226131,-2.259519,6.074385,-3.664512,-3.480099,-0.083128,4.866039,-2.261869,-6.417917,-9.850058,-0.117881,-7.808650,-7.203923,2.625687,-2.083493,3.904864,2.001092,8.516948,9.876078,2.402269,4.591640,8.258386,0.979328,-5.663812,-4.109361,1.326350,4.087243,4.647286,-9.063093,3.139671,5.210649,7.633392,4.324328,0.565496,8.398326,-8.178545,-0.393519,1.570451,-1.335945,-2.273682,-1.800397,4.575851,1.594516,-0.213762,3.864982,-4.534957,-6.751986,-2.074400,-5.128541,-4.468366,-6.339686,-1.064378,3.279762,2.345893,7.738858,-9.957072,6.078276,-4.711428,3.359848,8.015796,-9.078934,2.160613,7.953163,-5.934934,2.254253,5.738049,-4.229365,-2.365667,9.475572,6.983591,9.602105,6.383368,7.083204,8.839469,-0.493382,-3.493591,-2.271635,6.635345,2.356256,9.082873,-8.056299,-7.078050,9.644644,-9.285379,-1.354972,1.405870,-6.731915,5.336236,-4.488690,-2.615473,9.492820,-1.520149,-0.393316,7.650595,1.729173,-7.517713,-9.899298,-6.338329,9.173550,-3.359581,-7.839472,-8.184311,-7.998923,1.941563,-2.833381,9.157075,-7.822571,-4.469549,6.384987,-7.927245,-7.802261,8.547323,8.062794,-0.458277,-0.976248,6.191599,7.021092,8.543955,7.567080,-2.317226,-3.878321,6.279921,4.811870,5.754272,5.407519,-8.011311,-8.377671,-0.904823,0.064139,3.214282,-2.544090,4.446525,-8.401111,4.271884], dtype = "float64")#candidate|7574|(390,)|const|float64
const_7575 = relay.const(-7, dtype = "uint64")#candidate|7575|()|const|uint64
var_7576 = relay.var("var_7576", dtype = "int32", shape = (105,))#candidate|7576|(105,)|var|int32
var_7577 = relay.var("var_7577", dtype = "uint64", shape = (294,))#candidate|7577|(294,)|var|uint64
call_7572 = relay.TupleGetItem(func_3668_call(relay.reshape(var_7573.astype('uint16'), [10, 4, 15]), relay.reshape(var_7573.astype('uint16'), [10, 4, 15]), relay.reshape(const_7574.astype('float64'), [5, 78]), relay.reshape(const_7575.astype('uint64'), []), relay.reshape(var_7576.astype('int32'), [105,]), relay.reshape(var_7577.astype('uint64'), [294,]), ), 3)
call_7578 = relay.TupleGetItem(func_3676_call(relay.reshape(var_7573.astype('uint16'), [10, 4, 15]), relay.reshape(var_7573.astype('uint16'), [10, 4, 15]), relay.reshape(const_7574.astype('float64'), [5, 78]), relay.reshape(const_7575.astype('uint64'), []), relay.reshape(var_7576.astype('int32'), [105,]), relay.reshape(var_7577.astype('uint64'), [294,]), ), 3)
bop_7579 = relay.multiply(uop_7554.astype('uint16'), relay.reshape(var_7553.astype('uint16'), relay.shape_of(uop_7554))) # shape=(1, 2, 15)
bop_7583 = relay.left_shift(bop_7579.astype('int16'), const_7575.astype('int16')) # shape=(1, 2, 15)
output = relay.Tuple([call_7572,var_7573,const_7574,var_7576,var_7577,bop_7583,])
output2 = relay.Tuple([call_7578,var_7573,const_7574,var_7576,var_7577,bop_7583,])
func_7587 = relay.Function([var_7553,var_7573,var_7576,var_7577,], output)
mod['func_7587'] = func_7587
mod = relay.transform.InferType()(mod)
var_7588 = relay.var("var_7588", dtype = "float64", shape = (1, 2, 15))#candidate|7588|(1, 2, 15)|var|float64
var_7589 = relay.var("var_7589", dtype = "uint16", shape = (6, 100))#candidate|7589|(6, 100)|var|uint16
var_7590 = relay.var("var_7590", dtype = "int32", shape = (105,))#candidate|7590|(105,)|var|int32
var_7591 = relay.var("var_7591", dtype = "uint64", shape = (294,))#candidate|7591|(294,)|var|uint64
output = func_7587(var_7588,var_7589,var_7590,var_7591,)
func_7592 = relay.Function([var_7588,var_7589,var_7590,var_7591,], output)
mutated_mod['func_7592'] = func_7592
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7601 = relay.const([[[0.724100,-6.125330],[5.468332,-0.730592],[-8.814452,7.710561],[-5.435579,6.539192]],[[-1.165283,8.809795],[5.324709,-8.130495],[-7.581957,-4.896106],[-5.150624,-0.400677]],[[5.075525,2.588872],[-2.325141,-5.589290],[8.541517,-8.187536],[-0.066066,-3.846422]],[[-4.136372,-7.641107],[7.825334,8.852208],[5.746799,4.623978],[7.776887,-1.127139]],[[-9.231264,-8.380813],[0.595779,-3.518032],[-2.199353,-0.789026],[-6.967435,-0.900767]],[[8.508301,-3.653708],[4.944830,-7.851193],[-8.060096,-1.778665],[9.845593,-1.541347]],[[2.705787,-4.232915],[8.204783,4.374872],[7.940375,-7.074682],[5.521585,-9.773744]]], dtype = "float32")#candidate|7601|(7, 4, 2)|const|float32
const_7602 = relay.const([[[8.450378,-9.385422],[-3.224269,5.942343],[2.652220,7.041026],[1.082055,-0.898558]],[[8.232990,-7.580394],[3.474088,2.457582],[4.039662,-6.994670],[0.574213,9.081340]],[[9.136260,-9.444575],[-9.093059,-3.302952],[-5.744286,7.122252],[-7.579210,0.464227]],[[3.205588,5.853709],[8.391127,-5.459176],[8.069909,-4.150947],[7.582469,0.313011]],[[-5.691578,-2.708125],[-2.654776,-7.113079],[-5.459600,-8.053049],[6.478823,-1.434124]],[[5.904317,9.717159],[-6.167991,5.267736],[0.965608,-4.471182],[2.470045,0.057535]],[[4.104120,-6.996065],[-2.734264,-5.271153],[-6.319096,-1.920520],[-2.953568,-0.452292]]], dtype = "float32")#candidate|7602|(7, 4, 2)|const|float32
bop_7603 = relay.divide(const_7601.astype('float32'), relay.reshape(const_7602.astype('float32'), relay.shape_of(const_7601))) # shape=(7, 4, 2)
bop_7606 = relay.add(bop_7603.astype('int32'), relay.reshape(const_7602.astype('int32'), relay.shape_of(bop_7603))) # shape=(7, 4, 2)
output = relay.Tuple([bop_7606,])
output2 = relay.Tuple([bop_7606,])
func_7614 = relay.Function([], output)
mod['func_7614'] = func_7614
mod = relay.transform.InferType()(mod)
output = func_7614()
func_7615 = relay.Function([], output)
mutated_mod['func_7615'] = func_7615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_7618 = relay.TupleGetItem(func_7614_call(), 0)
call_7619 = relay.TupleGetItem(func_7615_call(), 0)
func_3852_call = mod.get_global_var('func_3852')
func_3860_call = mutated_mod.get_global_var('func_3860')
var_7640 = relay.var("var_7640", dtype = "uint64", shape = (840,))#candidate|7640|(840,)|var|uint64
var_7641 = relay.var("var_7641", dtype = "int16", shape = (135,))#candidate|7641|(135,)|var|int16
const_7642 = relay.const(-9, dtype = "uint32")#candidate|7642|()|const|uint32
var_7643 = relay.var("var_7643", dtype = "int32", shape = (105,))#candidate|7643|(105,)|var|int32
var_7644 = relay.var("var_7644", dtype = "float32", shape = (495,))#candidate|7644|(495,)|var|float32
call_7639 = relay.TupleGetItem(func_3852_call(relay.reshape(var_7640.astype('uint64'), [7, 15, 8]), relay.reshape(var_7640.astype('uint64'), [7, 15, 8]), relay.reshape(var_7641.astype('int16'), [15, 9]), relay.reshape(const_7642.astype('uint32'), []), relay.reshape(var_7643.astype('int32'), [21, 5]), relay.reshape(var_7644.astype('float32'), [495,]), ), 13)
call_7645 = relay.TupleGetItem(func_3860_call(relay.reshape(var_7640.astype('uint64'), [7, 15, 8]), relay.reshape(var_7640.astype('uint64'), [7, 15, 8]), relay.reshape(var_7641.astype('int16'), [15, 9]), relay.reshape(const_7642.astype('uint32'), []), relay.reshape(var_7643.astype('int32'), [21, 5]), relay.reshape(var_7644.astype('float32'), [495,]), ), 13)
func_5627_call = mod.get_global_var('func_5627')
func_5630_call = mutated_mod.get_global_var('func_5630')
const_7654 = relay.const([[-4.197672,-5.524850,5.753706],[-9.732416,6.153502,3.499512],[6.733099,2.120113,-3.738316],[6.599030,3.766000,-1.608391],[-6.915753,7.200490,7.354152],[9.047596,-0.009197,3.852442],[9.693495,-2.417172,-2.170941],[8.186509,1.862290,2.265843],[-2.750374,-4.846530,3.203195],[-6.183496,-6.378672,-6.593240],[9.056465,7.329102,9.733312],[9.948436,0.172792,6.049595],[5.929372,2.428011,2.834602],[-5.554185,5.860059,-4.233692],[-8.042968,9.378139,-2.337675],[-0.697281,9.658432,8.074823],[-5.256882,5.087764,-0.948381],[-1.271629,8.644212,-7.103519],[-7.925687,1.879424,7.543192],[-5.933045,-4.234508,-3.526733],[6.043501,-4.609504,6.176400],[-8.630516,2.658687,9.138083],[-9.587949,4.592385,1.318641],[9.863322,4.786582,-5.703599],[-2.112974,-5.789431,-6.154922],[2.013441,1.327679,-2.388950],[8.016870,-6.400389,6.575117],[-2.573453,7.664005,4.441262],[-4.916476,-3.611396,5.782780],[-2.086942,0.586855,0.705645],[-1.574044,-1.586064,-5.514960],[-1.566180,2.049281,-7.017659],[-1.722614,-3.339686,6.495441],[-6.082039,-0.160998,1.574729],[9.310625,7.571422,-3.307240],[-8.705644,6.318930,-0.479947],[-5.373781,4.534596,0.788974],[-6.341728,3.741570,-1.208903],[-4.896334,-2.625303,9.237909],[0.051820,6.909096,-1.217553],[2.878242,-0.222422,3.883555],[-9.630117,8.912786,0.848236],[-3.350381,-4.486579,-0.207911],[-2.945485,-1.390519,-1.408521],[-1.810895,-0.229937,-0.487728],[8.145671,-5.226828,1.654898],[-4.711025,3.448584,5.368714],[-7.984635,-2.633746,3.609137],[1.248684,9.822165,-3.147395],[-5.193859,1.365296,2.457045],[0.378965,8.114598,-6.014580],[6.152616,4.695427,6.587543],[5.526195,-0.307749,-3.097466],[-0.947161,8.120048,3.793486],[7.414331,-6.771386,1.626093],[6.428864,-7.800114,-4.514265],[7.871611,6.726358,-5.292372],[1.783791,-1.516949,6.581656],[-5.553355,8.544438,8.707488],[8.734819,-0.010050,-5.334091],[7.704266,-9.684866,-7.465573],[2.603258,-7.203639,-6.770221],[4.285730,-1.728627,4.011397],[-9.474613,8.490207,4.594446],[1.429686,-2.725761,-2.271160],[7.146155,-1.916047,0.627284],[-2.472756,-7.972192,3.946616],[2.075800,-8.561645,2.168655],[3.325845,8.806262,9.650785],[8.454512,-6.301467,-6.246884],[-6.024448,-9.220336,1.809130],[-0.014515,-8.385081,-5.087165],[9.154287,-7.855935,4.957165],[-9.624040,-3.462459,9.455226],[-7.097415,-8.104476,-9.301464],[-6.382773,-5.731958,9.612487],[-6.172334,0.962118,-3.577131],[4.762860,6.817549,-8.793031],[7.965112,8.895093,-3.163163],[6.304762,8.915727,2.128376],[-9.260922,0.046338,9.868417],[-6.681158,-2.967507,-8.771753],[4.435962,-8.196823,-6.557647],[1.008112,0.055803,4.091498],[1.890580,3.664108,-1.962322],[9.803763,-4.180202,1.666499],[5.545647,2.255772,3.015071],[1.374193,0.360525,5.392636],[-1.963869,5.205318,8.483300],[5.721757,9.564297,7.240257]], dtype = "float32")#candidate|7654|(90, 3)|const|float32
call_7653 = func_5627_call(relay.reshape(const_7654.astype('float32'), [2, 15, 9]))
call_7655 = func_5627_call(relay.reshape(const_7654.astype('float32'), [2, 15, 9]))
func_1874_call = mod.get_global_var('func_1874')
func_1877_call = mutated_mod.get_global_var('func_1877')
const_7660 = relay.const([True,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False], dtype = "bool")#candidate|7660|(44,)|const|bool
call_7659 = relay.TupleGetItem(func_1874_call(relay.reshape(const_7642.astype('bool'), []), relay.reshape(const_7660.astype('bool'), [1, 4, 11]), ), 0)
call_7661 = relay.TupleGetItem(func_1877_call(relay.reshape(const_7642.astype('bool'), []), relay.reshape(const_7660.astype('bool'), [1, 4, 11]), ), 0)
func_7524_call = mod.get_global_var('func_7524')
func_7530_call = mutated_mod.get_global_var('func_7530')
const_7669 = relay.const([10,-9,3,8,7,-2,-8,-8,-9,1,8,-4,9,9,6,8,-8,-8,-2,8,8,2,-8,-6,5,2,3,4,-2,10,5,-5,-5,-3,-1,-8,-10,7,-3,6,10,-1,-2,7,-2,-3,4,-9,2,8,4,4,-8,-3,-6,1,4,3,9,-3,8,7,3,3,-7,-9,-8,-6,-6,9,5,-9,2,-9,3,-3,8,-3,5,6,-8,4,10,2,6,-9,1,-1,2,-5,2,6,-9,10,-4,7,-3,-7,2,10,-1,10,1,-5,3,-9,-8,-4,-3,-3,3,6,3,-9,-3,3,-2,-5,6,9,2,6,-3,8,-5,1,-1,3,2,-6,-5,-10,2,1,7,-9,7,8,-6,-4,-7,10,-5,9,7,2,-4,10,-8,-8,-10,-4,2,7,-8,10,9,3,-3,1,8,3,-6,2,3,-10,6,-1,8,6,-10,-1,-6,-1,7,-10,-5,-10,7,6,-1,4,10,6,3,6,-6,-10,-3,1,3,6,-8,9,-10,5,3,9,-7,3,-4,-3,6,-5,6,-1,-9,9,5,3,4,7,9,1,10,8,-1,-8,-6,-5,9,3,3,7,1,3,10,-1,5,-5,-5,1,-3,4,2,-2,-7,10,9,10,-9,-5,5,6,-7,-7,3,10,-8,7,-6,-2,-6,-5,-2,-6,7,8,7,-4,-6,-9,-2,8,5,-10,4,6,-4,6,-5,7,-4,-6,10,5,2,6,5,3,-9,3,-7,-3,9,9,4,5,-10,8,10,5,-1,5,-6,8,-3,1,9,1,5,-1,5,-6,-7,-4,-10,-1,1,-7,-4,6,-5,7,1,3,9,5,-7,8,7,-3,2,-10,-9,4,1,3,7,1,10,-3,7,5,-1,8,-7,-5,-4,-4,1,8,-7,1,1,-1,-7,3,2,-7,-3,1,7,-10,2,-4,1,-8,-1,4,10,-6,-10,10,-7,5,2,-9,-3,-10,3,1,-3,6,-5,-9,-6,5,-6,-7,1,-4,-9,4,1,10,-7,2,7,6,-8,10,-2,9,-9,-10,10,5,-6,-5,2,-5,-6,7,-4,-7,9,-6,2,8,2,4,-9,-1,-8,4,-2,7,3,-1,-8,-9,6,8,9,-3,-4,-2,6,8,2,1,10,-9,-3,-1,-9,-8,8,-6,3,-9,-6,10,6,5,-1,-9,-6,5,1,8,8,8,3,-2,-3,3,-2,3,-10,-4,-7,-1,3,2,-4,5,-8,8,7,8,-3,-1,-4,2,7,5,1,6,-4,10,-9,-9,-6,-8,9,4,9,-8,2,-4,-6,-2,5,-10,8,-6,-3,-6,4,-3,-2,-8,2,1,-3,-4,6,-5,8,1,-5,7,-3,-10,-6,1,-10,8,-2,10,6,6,2,4,-7,5,1,2,4,-1,3,-10,-1,-8,7,-10,-2,6,6,-3,6,-4,10,1,6,-6,-5,5,-5,9,-1,-9,-3,-6,-7,-3,6,2,-5,-4,4,-1,6,-5,1,5,2,6,10,-6,2,10,7,8,4,3,1,8,-2,-10,-8,-6,8,-6,5,-5,-1,6,8,10,-5,-3,10,4,8,-6,9,-5,-5,7,-2,8,-9,3,-10,1,-9,2,8,1,9,2,-1,-9,9,8,-8,7,5,-5,5,8,2,1,-5,-6,2,-6,-5,1,9,-5,10,-4,-2,-7,5,-10,7,-7,-8,9,-2,-4,10,-1,5,-7,8,9,10,-10,3,-2,-3,-3,3,-2,-6,10,-10,-6,8,1,3,-7,-7,-8,9,1,10,-5,-5,-7,-1,-9,-9,9,6,-3,-1,-4,9,7,1,-10,-1,3,1,-8,-9,5,-2,3,-4,9,-9,2,-4,-8,8,-7,4,-6,1,9,-3,-6,-9,-4,-7,8,7,-8,10,7,5,-6,5,-3,-6,-4,9,5,-1,10,-6,-8,10,-6,-1,8,-9,4,-6,8,-1,2,-4,-5,6,7,-6,4,10,-6,-5,6,1,-5,6,1,-8,5,-2,1,8,1,-2,9,7,4,2,-3,9,-1,3,-2,7,-7,10,8,-5,-3,3,10,9,-1,5,5,-4,-8,-10,-10,-8,5,-4,-5,1,-7,-9,-4,2,-1,-1,-10,1,-4,8,10,-2,1,10,-6,-3,-5,9,-1,5,5,-8,-3,-2,-2,2,6,6,1,-3,-5,7,1,9,6,-3,4,-7,-2,3,-1,5,10,-5,5,7,6,-4,-1,-8,9,-1,5,-9,8,1,10,7,7,-2,-9,6,4,-2,-3,3,4,-6,-1,-7,8,8,-6,-5,-6,5,5,-1,-1,7,3,-5,-5,5,-5,-4,-2,8,-9,9,1,1,7,-8,-2,2,4,-2,10,4,-2,8,-5,2,-3,-9,6,2,-1,4,5,1,-5,10,-4,3,-5,10,9,-3,-2,9,-2,3,-1,-7,3,10,2,-7,4,-2,3,8,5,-6,-4,7,6,-9,7,7,-5,1,-5,-4,10,-8,10,-7,-5,-2,-10,5,10,-4,10,-8,6,-2,10,10,2,5,3,-8,6,7,10,-1,6,7,5,-8,-7,-2,6,8,-1,1,6,-2,9,8,3,-10,-5,4,-4,-10,3,-1,5,7,4,-10,9,-3,-3,-8,2,-5,6,-6,-2,-3,-10,3,4,1,-10,-6,-3,7,-2,2,4,-3,-9,-9,7,5,6,5,10,6,7,8,3,-7,10,-2,-9,3,4,-10,-5,10,-4,9,-3,1,7,1,5,-8,7,9,3,-5,-5,-9,9,10,-6,-5,-6,-10,-8,-4,7,7,-1,2,-8,2,10,-4,3,-2,4,10,6,2,1,8,-9,-3,-3,4,-2,7,-10,-2,-6,3,-2,2,5,3,-4,-5,9,-3,5,-8,-4,10,7,-6,-4,4,4,-5,2,4,-2,8,8,-6,9,-9,-6,-8,1,-7,-4,3,7,-8,8,4,10,-3,-1,1,-10,4,9,10,-7,7,6,-1,7,-3,-1,9,6,2,-9,-9,3,-5,-9,-4,-10,10,-10,10,-2,4,-7,-7,-3,2,1,-10,-9,9,-10,4,4,7,-9,-1,9,6,-10,-10,-3,-6,-6,-1,3,-2,-4,4,-2,-4,-7,2,2,-3,1,7,8,10,-10,-8,2,-6,6,-8,1,7,-9,-6,-7,5,-4,1,6,5,-4,-8,3,-7,-6,-7,-9,6,3,10,5,-7,-8,1,2,9,-9,4,-1,-10,6,-3,-4,-2,5,7,7,-6,-6,8,-3,4,2,-3,-1,-1,2,3,-6,-3,6,8,-7,10,-3,1,-5,-7,5,1,5,-4,-7,5,1,-2,-9,2,-7,9,-1,6,-5,3,5,7,-6,-8,-5,4,-10,-5,-9,7,9,5,-4,6,-4,-3,-4,10,1,-3,-1,-4,-5,2,-6,-9,-2,-5,-5,-10,-1,-9,-1,-5,7,9,-6,10,2,3,-10,-2,-7,1,-9,1,3,-7,9,7,9,-5,-10,4,7,-9,2,-1,8,10,-4,9,3,4,-5,9,8,9,-10,-2,-4,6,-4,-4,-1,-2,-7,4,5,3,8,6,-5,6,9,2,2,-9,7,1,-10,-6,-3,9,8,-8,4,-4,10,-4,-9,4,8,-8,-1,-4,-1,9,3,-2,10,9,5,-2,-5,-5,5,-8,5,8,6,-6,-2,-10,3,-8,-3,4,2,2,2,-4,7,10,7,-7,-9,9,-7,8,3,2,3,-2,4,2,3,5,-7,3,2,-8,-2,4,-8,-1,10,-4,3,-8,2,-5,8,-7,4,9,-10,8,-6,3,-7,-2,2,-10,4,2,-9,-10,-6,2,-7,-7,-9,-10,9,6,10,5,-6,6,2,-5,-2,8,2,-9,10,-5,-5,2,8,2,-6,1,9,-1,3,3,-10,5,-8,2,-4,-5,-2,3,-4,10,-1,3,8,2,-1,9,4,5,2,-10,-4,5,3,-6,4,-7,8,-4,8,-10,-1,-10,4,-8,5,-5,2,-5,-10,2,-8,1,-2,2,3,7,-10,-10,6,-3,6,10,-7,-3,-7,-3,5,-10,-8,-5,6,-6,10,-1,2,9,-9,5,3,3,4,-4,-9,-8,-9,-10,6,1,2,4,5,3,2,2,-8,7,2,-3,-8,-9,-3,-3,-5,-4,-6,2,-2,5,-2,9,-1,-2,-10,5,-5,8,-3,4,3,6,8,1,2,-4,-5,2,1,-1,8,-10,10,8,7,1,2,1,5,10,10,-2,6,2,-8,8,-9,-1,-6,-10,3,-5,1,6,10,5,-7,6,3,-1,-1,8,-9,6,-10,-8,-2,-7,-9,-2,9,10,6,-1,1,9,5,1,8,7,8,10,-8,-2,2,-7,-1,8,2,6,5,7,-5,-2,-6,3,-4,-3,-4,7,-8,8,1,7,-7,-7,10,-2,2,10,-3,-3,9,-7,-10,-10,1,8,-6,-5,9,7,6,4,5,8,-10,5,5,-4,-10,-5,-2,5,1,-3,4,10,1,-9,-2,4,-6,-3,3,-9,-2,4,-7,-4,-8,9,-8,3,-6,6,9,-10,-7,7,-10,2,9,8,4,-6,-10,6,5,7,-2,-9,-3,6,-4,1,-9,6,9,-8,7,-7,1,6,3,-9,-6,-7,-9,-10,-8,-7,-4,-7,-8,-5,-10,-3,-6,-9,4,-7,10,1,7,-2,-10,1,1,-6,4,-5,4,5,9,-10,-6,3,-10,-3,6,3,-4,10,4,-8,7,-3,3,2,4,3,10,-3,-10,1,-4,2,1,-7,7,-3,9,7,4,2,-1,5,2,-6,-4,10,1,8,-5,-7,8,-9,6,9,-5,-5,9,-10,7,5,10,1,-9,-3,4,7,8,3,9,-3,4,-3,-9,3,-8,1,-4,-1,-3,-5,2,3,7,-5,5,-3,7,1,6,6,-10,3,-9,-7,7,-1,6,-1,7,9,6,-2,-5,-1,-7,-6,3,-3,2,-7,3,-9,2,-10,-8,3,-1,8,-10,-9,-7,-5,4,5,7,-6,7,-9,-5,-8,-10,-6,-7,-8,-5,-5,-6,5,6,8,9,4,-1,-5,-4,9,5,8,2,-1,5,-9,6,-2,1,6,6,-8,-6,3,-7,5,-10,5,9,6,4,6,1,-2,10,2,9,4,2,-5,-2,2,3,1,-7,-7,-6,1,-1,-10,3,8,2,9,-9,-5,-7,2,-4,4,-4,2,-4,-7,-10,-5,-9,-6,4,6,-4,-4,-8,2,3,-3,7,-7,2,5,1,4,-2,10,10,9,7,-4,2,-6,4,-2,-7,-3,4,-1,-9,-4,7,-6,10,-10,1,-1,-2,9,-8,-6,-3,6,-6,-2,-1,-5,-8,5,10,-4,-7,-5,-4,4,9,-7,-8,8,9,10,-6,-8,8,4,-9,9,5,-7,-10,1,3,-10,2,-7,-9,2,-10,2,6,-5,4,2,-8,8,-10,-5,-8,3,4,2,-7,-1,-7,-6,-8,-9,-3,-4,10,8,1,-4,-10,-1,-9,10,-7,2,5,-8,-6,-7,-8,1,3,1,-5,-4,-3,9,-8,-7,-1,1,-8,-1,6,5,-9,3,8,-7,-8,-7,-8,5,7,-2,-3,-6,-4,7,-5,5,1,-5,3,-3,2,3,8,7,2,-8,4,7,-3,1,7,1,5,8,-9,-8,2,-3,1,-10,1,7,-1,5,-9,1,2,3,-1,5,1,-3,7,7,-5,-1,2,2,-4,-7,-3,8,-2,5,1,3,5,9,9,-10,-1,-3,-8,-8,1,-5,6,4,-4,1,-10,9,10,9,-2,-6,-9,7,3,2,-3,-10,2,-6,2,-2,-2,8,-9,-3,-6,-5,7,4,9,6,5,-8,-10,3,-4,4,8,-9,-9,-9,3,-9,7,-2,3,8,-4,5,3,-5,5,-4,-1,9,5,-2,3,9,-9,8,-9,-10,-3,6,-4,-4,2,1,10,1,9,6,-9,4,7,9,-8,-8,7,8,5,-10,7,10,3,-5,-9,6,5,7,4,8,7,5,-10,-5,5,3,7,1,7,2,-6,-5,10,3,-7,6,-8,10,-3,4,2,-2,-3,1,-9,-7,3,6,-1,7,-1,-4,5,-9,-10,-6,2,-3,1,6,-9,2,2,-5,-8,-3,-7,-2,-4,1,-3,8,5,4,-5,5,-3,6,-7,-10,-3,-8,3,-1,8,-1,-8,-10,-10,8,-5,1,-2,-7,8,-5,-2,1,10,10,-5,3,-2,8,-9,9,-1,-4,-7,-9,-8,-8,-7,8,3,9,1,-3,7,4,10,-10,2,-2,-4,-6,7,-5,-2,-6,-2,-7,9,3,3,-1,-1,-2,4,-3,-6,3,2,-10,2,3,2,-5,2,-6,7,8,6,-10,5,-1,2,-8,3,-3,5,8,-6,6,-3,4,10,8,3,8,-1,1,-2,-2,-7,9,10,9,2,-5,10,5,-1,-7,2,4,-6,-9,-4,-3,-3,-4,2,1,1,-9,5,-2,-10,3,-4,-5,2,9,4,-8,8,2,-9,4,-10,10,10,4,-3,-9,-1,-9,10,-10,2,3,-2,-10,9,1,-10,7,-5,9,7,6,4,-3,-3,-9,1,-5,-9,5,10,9,9,9,6,-1,-5,1,2,4,-8,-10,-8,-3,-1,-7,4,-2,-2,4,-6,9,4,1,-5,-3,1,-2,-10,6,-3,4,-8,10,-5,8,-1,-5,8,-3,2,-7,-9,1,-6,-1,-1,8,-1,-1,-3,8,-7,-3,8,9,-3,-4,-7,-4,-4,-4,1,-6,2,-9,-8,3,1,-10,3,10,6,-10,8,6,10,9,-3,4,-4,-2,-9,8,10,-8,7,-9,-1,-4,3,-5,1,2,10,-1,8,-9,-8,-8,6,1,5,4,7,7,1,2,-5,-8,-2,-9,6,-9,6,-3,5,-4,4,-6,-10,-2,6,-3,-8,-6,-1,3,5,-2,-1,-3,-2,9,-7,-8,10,5,4,7,-10,4,-9,9,-1,5,9,-2,-5,7,-6,8,-7,-1,3,-4,-2,4,-7,5,7,4,8,-9,7,-6,2,-10,-8,-9,3,-4,4,-6,5,1,-1,-10,-10,-3,-6,1,-2,-9,6,-1,-3,-3,5,6,-1,1,-1,-1,1,-8,-3,-9,2,5,-7,-8,-1,5,-10,-5,-9,1,1,-1,-7,1,9,-5,9,-2,4,7,1,-3,-5,2,-7,4,-6,-10,5,5,3,-7,-9,1,9,1,9,10,2,-8,6,7,-8,-7,10,6,-3,8,-2,-5,6,-10,2,1,-2,3,2,2,-8,-2,2,-4,3,-4,2,5,-7,-2,-6,5,1,-8,9,-4,8,5,-6,-2,2,3,9,-1,4,7,6,10,7,2,-5,-3,2,4,9,-6,-3,-5,6,9,9,2,8,-7,-7,3,7,8,5,7,9,7,2,-6,-7,-10,3,-6,-3,5,1,-5,-3,-8,-4,-6,-10,-7,-4,3,-8,-10,7,1,6,-4,-2,-7,-4,7,4,3,4,-6,-10,2,4,-8,-5,-4,5,-1,-9,-5,-5,-10,-4,3,-2,-8,2,10,-1,10,9,8,4,-2,8,-5,-10,4,-10,1,7,-4,-9,-6,7,6,-10,2,4,6,-1,-6,7,-4,6,1,-7,6,-1,8,-6,4,1,-9,-1,-8,7,-3,6,3,5,9,9,9,6,8,2,-10,-9,9,-4,-2,2,5,-3,2,-2,-9,6,3,-5,-6,4,-1,6,10,-8,-3,8,-2,8,-10,-7,-3,4,7,-8,8,8,2,-1,6,-7,-2,6,-9,-8,-5,5,-7,6,10,-4,4,10,-10,2,-10,2,5,6,2,-10,-8,-7,-6,7,-6,6,7,-8,7,-10,1,9,-1,10,8,2,-7,-8,-5,10,-10,-3,-4,-3,-3,8,-6,-9,-3,-2,-9,6,7,-8,1,-4,-6,-7,10,-3,-2,6,-9,8,-4,-2,7,8,4,-8,7,7,1,-6,-3,-5,-2,-4,5,-3,-2,-3,-5,-7,-8,5,7,1,-3,8,-7,-2,3,10,-7,9,9,10,-3,-4,-2,-8,-8,-6,7,-8,8,-3,-5,-8,-7,-4,9,2,-1,-2,-7,1,-1,-8,-2,3,6,10,1,6,7,6,-3,7,-7,8,-3,-9,9,-3,6,10,3,5,-10,-4,10,4,-10,-9,1,-3,8,9,3,-8,-7,1,10,6,9,-8,9,2,2,10,-1,-10,-9,6,-8,-9,3,-6,9,5,-1,-7,-5,-2,4,-2,7,4,10,5,2,-6,-7,-2,-2,4,-1,4,4,5,-9,1,-1,-9,-4,-1,-10,5,-7,4,3,-5,-1,-10,-4,-2,-2,-9,9,3,4,-2,-9,4,4,-7,7,9,10,4,-4,9,3,-8,7,6,5,8,6,2,-1,5,3,-8,5,9,10,7,5,6,9,5,-1,-10,6,-7,2,-3,-9,-8,-2,-6,-2,-8,10,-2,7,3,-2,-4,-4,3,4,1,-8,-8,3,-7,-8,-5,-8,-7,4,-2,4,5,9,-8,-8,6,7,8,-7,6,-9,-6,-7,9,-5,-8,-7,1,-2,8,-7,6,10,3,-1,5,-9,9,3,7,-1,1,9,5,-8,-9,-9,8,-1,9,9,3,4,-5,-2,-7,1,-10,-7,-10,-7,-1,-6,-6,-9,10,-8,9,7,-10,-8,3,-4,-8,7,7,8,2,8,-2,4,6,-7,3,9,-6,-10,-6,9,5,-3,1,2,-7,1,9,3,7,-10,-5,-6,6,7,10,8,-3,-2,6,6,-6,3,2,1,-6,-2,10,2,-5,7,-7,3,-10,2,8,-7,7,-10,-8,10,9,-6,9,-4,7,2,-10,3,9,-4,-5,3,-5,-3,-1,-8,3,3,2,-8,1,-2,-4,-1,-10,2,-9,9,6,-8,5,1,-10,1,2,-10,9,5,4,-6,4], dtype = "int32")#candidate|7669|(3360,)|const|int32
var_7670 = relay.var("var_7670", dtype = "int32", shape = (672,))#candidate|7670|(672,)|var|int32
var_7671 = relay.var("var_7671", dtype = "uint32", shape = (1694,))#candidate|7671|(1694,)|var|uint32
call_7668 = relay.TupleGetItem(func_7524_call(relay.reshape(const_7669.astype('int32'), [14, 15, 16]), relay.reshape(var_7670.astype('int32'), [672,]), relay.reshape(const_7642.astype('uint32'), []), relay.reshape(var_7671.astype('uint32'), [121, 14]), ), 2)
call_7672 = relay.TupleGetItem(func_7530_call(relay.reshape(const_7669.astype('int32'), [14, 15, 16]), relay.reshape(var_7670.astype('int32'), [672,]), relay.reshape(const_7642.astype('uint32'), []), relay.reshape(var_7671.astype('uint32'), [121, 14]), ), 2)
uop_7684 = relay.atan(var_7644.astype('float64')) # shape=(495,)
output = relay.Tuple([call_7618,call_7639,var_7640,var_7641,const_7642,var_7643,call_7653,const_7654,call_7659,const_7660,call_7668,const_7669,var_7670,var_7671,uop_7684,])
output2 = relay.Tuple([call_7619,call_7645,var_7640,var_7641,const_7642,var_7643,call_7655,const_7654,call_7661,const_7660,call_7672,const_7669,var_7670,var_7671,uop_7684,])
func_7709 = relay.Function([var_7640,var_7641,var_7643,var_7644,var_7670,var_7671,], output)
mod['func_7709'] = func_7709
mod = relay.transform.InferType()(mod)
mutated_mod['func_7709'] = func_7709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7709_call = mutated_mod.get_global_var('func_7709')
var_7711 = relay.var("var_7711", dtype = "uint64", shape = (840,))#candidate|7711|(840,)|var|uint64
var_7712 = relay.var("var_7712", dtype = "int16", shape = (135,))#candidate|7712|(135,)|var|int16
var_7713 = relay.var("var_7713", dtype = "int32", shape = (105,))#candidate|7713|(105,)|var|int32
var_7714 = relay.var("var_7714", dtype = "float32", shape = (495,))#candidate|7714|(495,)|var|float32
var_7715 = relay.var("var_7715", dtype = "int32", shape = (672,))#candidate|7715|(672,)|var|int32
var_7716 = relay.var("var_7716", dtype = "uint32", shape = (1694,))#candidate|7716|(1694,)|var|uint32
call_7710 = func_7709_call(var_7711,var_7712,var_7713,var_7714,var_7715,var_7716,)
output = call_7710
func_7717 = relay.Function([var_7711,var_7712,var_7713,var_7714,var_7715,var_7716,], output)
mutated_mod['func_7717'] = func_7717
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7725 = relay.const([[[-6,-10,7,7,6,3],[-10,-8,-3,-9,2,6],[-10,-2,5,7,-6,-8],[8,-6,3,-6,10,1],[-1,-4,-4,3,-3,5],[7,-9,10,-6,3,3],[-1,10,3,5,-4,8],[-1,2,-8,-2,-8,7],[-6,-4,-7,8,-8,-9],[10,4,5,1,-5,-2],[7,-7,4,-1,-1,1],[6,5,-8,2,10,-3],[1,3,-7,8,-8,9],[3,4,6,9,7,-5]]], dtype = "int32")#candidate|7725|(1, 14, 6)|const|int32
var_7726 = relay.var("var_7726", dtype = "int32", shape = (2, 14, 6))#candidate|7726|(2, 14, 6)|var|int32
bop_7727 = relay.minimum(const_7725.astype('int32'), var_7726.astype('int32')) # shape=(2, 14, 6)
output = bop_7727
output2 = bop_7727
func_7735 = relay.Function([var_7726,], output)
mod['func_7735'] = func_7735
mod = relay.transform.InferType()(mod)
mutated_mod['func_7735'] = func_7735
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7736 = relay.var("var_7736", dtype = "int32", shape = (2, 14, 6))#candidate|7736|(2, 14, 6)|var|int32
func_7735_call = mutated_mod.get_global_var('func_7735')
call_7737 = func_7735_call(var_7736)
output = call_7737
func_7738 = relay.Function([var_7736], output)
mutated_mod['func_7738'] = func_7738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_7742 = relay.TupleGetItem(func_7614_call(), 0)
call_7743 = relay.TupleGetItem(func_7615_call(), 0)
output = relay.Tuple([call_7742,])
output2 = relay.Tuple([call_7743,])
func_7753 = relay.Function([], output)
mod['func_7753'] = func_7753
mod = relay.transform.InferType()(mod)
output = func_7753()
func_7754 = relay.Function([], output)
mutated_mod['func_7754'] = func_7754
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7805 = relay.const([[[-8.202981,7.325163,-7.445806,-4.956672,-9.607313,-1.854350,3.285527,-9.180653,-4.605481,-1.876107,3.601845,-8.889197,-8.609843,1.620144,-3.185429]],[[2.474067,-9.468071,-8.041810,0.005510,-6.196332,-0.140905,3.519533,-3.901613,-7.697493,-2.614402,3.277765,-2.632967,-3.015281,3.434129,-3.741595]],[[-0.100295,3.770366,0.716494,3.546895,-3.803419,-3.712939,-1.691117,-3.403305,-9.466048,1.804505,-0.111448,-8.844940,-3.084996,6.444224,-1.813037]],[[5.602650,5.166171,6.658227,-1.806715,-9.419326,-2.892041,1.619840,-8.875632,-5.201143,6.102290,9.443426,-7.135243,-5.453334,-9.287171,8.307518]],[[2.066271,6.546570,5.461837,5.290343,7.282875,-5.711096,6.064744,-2.297766,-3.368734,-4.061862,-9.218327,5.408029,8.514433,2.892185,0.891408]],[[-7.082623,-2.152578,-4.968328,-9.395327,1.299702,8.818181,-2.845764,-0.467673,-1.639133,2.217016,-8.635509,-8.431424,-4.713633,4.965967,-2.902736]],[[-9.211892,0.727119,-1.540598,-8.277731,-6.506592,7.379058,-4.080606,-7.449491,-6.735457,9.878922,6.227063,-7.901741,8.545507,2.355930,-7.965435]],[[4.054821,-9.053097,1.753073,-4.522818,3.163379,-4.354415,-9.239720,-7.072596,9.194378,4.457563,-5.929393,-4.827380,4.689740,-3.107214,-5.275078]]], dtype = "float32")#candidate|7805|(8, 1, 15)|const|float32
uop_7806 = relay.erf(const_7805.astype('float32')) # shape=(8, 1, 15)
output = uop_7806
output2 = uop_7806
func_7814 = relay.Function([], output)
mod['func_7814'] = func_7814
mod = relay.transform.InferType()(mod)
output = func_7814()
func_7815 = relay.Function([], output)
mutated_mod['func_7815'] = func_7815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7829 = relay.var("var_7829", dtype = "float32", shape = ())#candidate|7829|()|var|float32
var_7830 = relay.var("var_7830", dtype = "float32", shape = (9, 3, 10))#candidate|7830|(9, 3, 10)|var|float32
bop_7831 = relay.divide(var_7829.astype('float32'), var_7830.astype('float32')) # shape=(9, 3, 10)
output = relay.Tuple([bop_7831,])
output2 = relay.Tuple([bop_7831,])
func_7837 = relay.Function([var_7829,var_7830,], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mutated_mod.get_global_var('func_7837')
var_7839 = relay.var("var_7839", dtype = "float32", shape = ())#candidate|7839|()|var|float32
var_7840 = relay.var("var_7840", dtype = "float32", shape = (9, 3, 10))#candidate|7840|(9, 3, 10)|var|float32
call_7838 = func_7837_call(var_7839,var_7840,)
output = call_7838
func_7841 = relay.Function([var_7839,var_7840,], output)
mutated_mod['func_7841'] = func_7841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_7851 = relay.TupleGetItem(func_7614_call(), 0)
call_7852 = relay.TupleGetItem(func_7615_call(), 0)
uop_7855 = relay.sigmoid(call_7851.astype('float64')) # shape=(7, 4, 2)
uop_7857 = relay.sigmoid(call_7852.astype('float64')) # shape=(7, 4, 2)
output = relay.Tuple([uop_7855,])
output2 = relay.Tuple([uop_7857,])
func_7862 = relay.Function([], output)
mod['func_7862'] = func_7862
mod = relay.transform.InferType()(mod)
mutated_mod['func_7862'] = func_7862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7862_call = mutated_mod.get_global_var('func_7862')
call_7863 = func_7862_call()
output = call_7863
func_7864 = relay.Function([], output)
mutated_mod['func_7864'] = func_7864
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_7882 = relay.TupleGetItem(func_7614_call(), 0)
call_7883 = relay.TupleGetItem(func_7615_call(), 0)
func_7461_call = mod.get_global_var('func_7461')
func_7466_call = mutated_mod.get_global_var('func_7466')
var_7887 = relay.var("var_7887", dtype = "float32", shape = (490,))#candidate|7887|(490,)|var|float32
const_7888 = relay.const(-5, dtype = "int64")#candidate|7888|()|const|int64
var_7889 = relay.var("var_7889", dtype = "int32", shape = (676,))#candidate|7889|(676,)|var|int32
call_7886 = relay.TupleGetItem(func_7461_call(relay.reshape(var_7887.astype('float32'), [7, 10, 7]), relay.reshape(const_7888.astype('int64'), []), relay.reshape(var_7889.astype('int32'), [676,]), ), 3)
call_7890 = relay.TupleGetItem(func_7466_call(relay.reshape(var_7887.astype('float32'), [7, 10, 7]), relay.reshape(const_7888.astype('int64'), []), relay.reshape(var_7889.astype('int32'), [676,]), ), 3)
output = relay.Tuple([call_7882,call_7886,var_7887,const_7888,var_7889,])
output2 = relay.Tuple([call_7883,call_7890,var_7887,const_7888,var_7889,])
func_7892 = relay.Function([var_7887,var_7889,], output)
mod['func_7892'] = func_7892
mod = relay.transform.InferType()(mod)
var_7893 = relay.var("var_7893", dtype = "float32", shape = (490,))#candidate|7893|(490,)|var|float32
var_7894 = relay.var("var_7894", dtype = "int32", shape = (676,))#candidate|7894|(676,)|var|int32
output = func_7892(var_7893,var_7894,)
func_7895 = relay.Function([var_7893,var_7894,], output)
mutated_mod['func_7895'] = func_7895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_7915 = relay.TupleGetItem(func_7614_call(), 0)
call_7916 = relay.TupleGetItem(func_7615_call(), 0)
output = call_7915
output2 = call_7916
func_7925 = relay.Function([], output)
mod['func_7925'] = func_7925
mod = relay.transform.InferType()(mod)
output = func_7925()
func_7926 = relay.Function([], output)
mutated_mod['func_7926'] = func_7926
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7963 = relay.var("var_7963", dtype = "float32", shape = (10, 11, 3))#candidate|7963|(10, 11, 3)|var|float32
uop_7964 = relay.asinh(var_7963.astype('float32')) # shape=(10, 11, 3)
output = relay.Tuple([uop_7964,])
output2 = relay.Tuple([uop_7964,])
func_7970 = relay.Function([var_7963,], output)
mod['func_7970'] = func_7970
mod = relay.transform.InferType()(mod)
var_7971 = relay.var("var_7971", dtype = "float32", shape = (10, 11, 3))#candidate|7971|(10, 11, 3)|var|float32
output = func_7970(var_7971)
func_7972 = relay.Function([var_7971], output)
mutated_mod['func_7972'] = func_7972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_7976 = relay.TupleGetItem(func_7614_call(), 0)
call_7977 = relay.TupleGetItem(func_7615_call(), 0)
output = call_7976
output2 = call_7977
func_7980 = relay.Function([], output)
mod['func_7980'] = func_7980
mod = relay.transform.InferType()(mod)
output = func_7980()
func_7981 = relay.Function([], output)
mutated_mod['func_7981'] = func_7981
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7980_call = mod.get_global_var('func_7980')
func_7981_call = mutated_mod.get_global_var('func_7981')
call_8024 = func_7980_call()
call_8025 = func_7980_call()
uop_8031 = relay.cos(call_8024.astype('float64')) # shape=(7, 4, 2)
uop_8033 = relay.cos(call_8025.astype('float64')) # shape=(7, 4, 2)
uop_8036 = relay.erf(call_8024.astype('float64')) # shape=(7, 4, 2)
uop_8038 = relay.erf(call_8025.astype('float64')) # shape=(7, 4, 2)
uop_8047 = relay.sinh(uop_8031.astype('float64')) # shape=(7, 4, 2)
uop_8049 = relay.sinh(uop_8033.astype('float64')) # shape=(7, 4, 2)
bop_8052 = relay.floor_mod(uop_8036.astype('float64'), relay.reshape(uop_8031.astype('float64'), relay.shape_of(uop_8036))) # shape=(7, 4, 2)
bop_8055 = relay.floor_mod(uop_8038.astype('float64'), relay.reshape(uop_8033.astype('float64'), relay.shape_of(uop_8038))) # shape=(7, 4, 2)
output = relay.Tuple([uop_8047,bop_8052,])
output2 = relay.Tuple([uop_8049,bop_8055,])
func_8057 = relay.Function([], output)
mod['func_8057'] = func_8057
mod = relay.transform.InferType()(mod)
output = func_8057()
func_8058 = relay.Function([], output)
mutated_mod['func_8058'] = func_8058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_8076 = relay.TupleGetItem(func_7614_call(), 0)
call_8077 = relay.TupleGetItem(func_7615_call(), 0)
func_1006_call = mod.get_global_var('func_1006')
func_1009_call = mutated_mod.get_global_var('func_1009')
var_8087 = relay.var("var_8087", dtype = "uint64", shape = (1350,))#candidate|8087|(1350,)|var|uint64
call_8086 = relay.TupleGetItem(func_1006_call(relay.reshape(var_8087.astype('uint64'), [15, 9, 10]), relay.reshape(var_8087.astype('uint64'), [15, 9, 10]), ), 0)
call_8088 = relay.TupleGetItem(func_1009_call(relay.reshape(var_8087.astype('uint64'), [15, 9, 10]), relay.reshape(var_8087.astype('uint64'), [15, 9, 10]), ), 0)
func_597_call = mod.get_global_var('func_597')
func_602_call = mutated_mod.get_global_var('func_602')
var_8101 = relay.var("var_8101", dtype = "uint32", shape = ())#candidate|8101|()|var|uint32
var_8102 = relay.var("var_8102", dtype = "uint32", shape = (1694,))#candidate|8102|(1694,)|var|uint32
const_8103 = relay.const([-6,-9,-5,-8,2,-7,-6,-5,2,3,6,3,-10,10,-3,-1,3,1,-3,-6,5,-3,8,-1,-10,4,4,4,10,-7,-9,1,-8,-8,3,5,-7,9,8,6,6,-6,9,6,3,4,10,4,8,-9,5,-9,6,-10,1,4,7,-8,9,-6,5,-4,5,-5,9,-6,-1,9,-4,-10,6,-2,4,-9,-4,-3,5,8,-5,-7,-6,-9,7,-4,6,7,8,4,1,-4,8,-8,7,7,8,8,-6,-2,-2,7,10,1,5,-1,9], dtype = "int32")#candidate|8103|(105,)|const|int32
call_8100 = relay.TupleGetItem(func_597_call(relay.reshape(var_8101.astype('uint32'), []), relay.reshape(var_8102.astype('uint32'), [11, 11, 14]), relay.reshape(const_8103.astype('int32'), [105,]), ), 0)
call_8104 = relay.TupleGetItem(func_602_call(relay.reshape(var_8101.astype('uint32'), []), relay.reshape(var_8102.astype('uint32'), [11, 11, 14]), relay.reshape(const_8103.astype('int32'), [105,]), ), 0)
func_7709_call = mod.get_global_var('func_7709')
func_7717_call = mutated_mod.get_global_var('func_7717')
var_8110 = relay.var("var_8110", dtype = "uint64", shape = (840,))#candidate|8110|(840,)|var|uint64
const_8111 = relay.const([-3,7,-10,-5,-10,-2,-5,-3,-1,3,2,-6,10,3,-1,7,3,-3,8,10,10,10,7,10,4,5,-5,1,9,1,10,-7,1,-6,7,-7,-7,4,-2,3,8,-4,-1,8,10,-1,9,-3,-7,1,4,10,-7,-5,-1,-9,-8,-1,7,-8,-1,7,-8,-2,9,6,-3,5,5,3,10,-4,-4,-9,4,-7,-10,-7,-5,1,4,7,8,-1,2,8,5,-2,8,-7,-1,-9,1,7,-7,-1,-10,2,10,2,7,-6,3,-9,-7,5,-3,7,10,-1,4,2,10,-1,-7,-4,4,-7,8,-8,-4,-3,7,2,-7,8,5,-5,-4,-7,3,7,3,-4,2], dtype = "int16")#candidate|8111|(135,)|const|int16
const_8112 = relay.const([-5.225873,6.432550,4.971133,-0.343570,-5.254759,2.428770,-8.553238,-4.857442,9.760003,-5.231751,-6.390825,2.970889,6.370454,5.818899,-8.040114,-9.664275,-7.681434,-6.390301,-0.270812,-4.379021,-6.254132,-0.545927,-5.608910,9.364420,-0.593317,-4.907603,-8.801736,-0.221695,9.898440,-5.572443,-0.318721,-2.811803,-5.047519,1.958713,8.367072,-0.742143,6.748019,-7.511817,8.969451,9.498506,-4.074175,-8.445631,-4.957062,-6.440803,-2.100419,2.235892,6.581246,1.890333,-4.286916,-3.874202,-6.299969,-2.925560,-8.672237,-9.701436,-9.287227,8.696896,6.595154,8.407796,-1.547594,2.529699,-6.514767,-2.063150,-9.237697,-3.187750,-3.696537,-9.653855,2.483943,-9.426077,6.208213,5.694544,0.528067,-0.870733,-3.281892,-5.072655,0.512388,1.729015,-3.068198,1.855135,-5.933067,-0.648454,8.629118,7.912710,0.288277,-8.239032,-2.250269,-3.418731,-5.293187,-3.160918,-0.099317,9.493726,-7.238111,1.934186,-4.000568,7.267474,-0.418392,6.053438,-5.109913,-8.396026,5.579462,8.651943,-1.600577,2.183494,-6.961845,3.374039,-0.950506,7.059330,-5.154169,1.518181,1.276902,9.499341,-9.347593,3.328587,1.263822,-2.092277,-4.400818,9.593445,8.133923,5.056453,-5.299455,-8.042713,-8.670320,-7.159006,8.715304,5.950989,-2.640099,-7.612935,-7.768289,-7.056556,-9.425426,-5.776832,-4.776323,2.046167,-6.170530,0.496592,-0.245886,1.153662,9.834095,4.680348,1.005893,-4.960929,4.574153,2.044916,-0.287458,1.712763,-7.257853,-3.545768,4.566974,0.584109,-9.550480,7.968651,-6.861922,8.280624,-6.326203,-0.683290,-8.617318,5.407539,-4.284334,6.184213,-6.681576,1.100601,-6.925802,1.875306,7.601892,1.696046,-4.508819,-7.239631,6.355421,-1.413474,-1.725726,6.639445,4.786184,-4.432721,3.830519,8.185752,9.055934,6.916847,-6.659145,2.292813,3.711841,6.482496,8.494684,-3.289931,-0.543477,-2.034791,-4.399031,0.509250,9.512665,6.246072,0.563489,-0.563995,9.731873,-7.947704,5.000161,8.255867,-0.233839,-6.700352,7.404167,-3.626097,6.232832,-0.557689,-5.613895,-4.481587,-9.111032,1.013153,-0.921331,-4.522910,5.704724,1.341292,-2.361746,9.104945,5.901889,9.892478,-0.106068,-9.196527,-6.343690,8.076897,-2.167536,-4.510586,8.039566,-0.894926,-0.409372,0.774664,8.688894,-0.686660,-5.505968,-6.059335,5.045528,-4.443099,0.976632,7.369939,2.808557,5.060088,-6.385907,-5.200220,7.340439,1.337036,9.343133,5.475315,3.059087,9.580631,4.484716,-2.143381,1.018739,-6.799529,7.343849,-7.222790,9.967909,9.844223,-2.804599,1.669841,-8.209158,7.449961,-3.900915,6.744342,-2.037214,6.417701,-3.223286,-8.260216,-6.400651,9.702052,-7.065708,-1.218532,6.458555,-0.962927,-0.230809,1.754424,-4.930883,-5.678830,8.075566,3.979990,-9.650848,2.042437,-4.222536,-5.072825,-8.682861,-1.570672,-8.765521,-2.206776,-7.091387,2.739819,5.443534,-8.570628,4.246597,-7.592313,-8.766613,-0.465055,-0.813871,2.349000,7.728119,0.728596,3.926004,-2.439097,-3.576424,6.268520,2.505292,7.808765,2.637325,5.737009,1.842270,7.355401,1.286204,-2.606466,6.099287,-2.038454,-9.165998,6.461981,7.265144,5.321408,-1.140812,5.070802,4.483057,-6.928071,-5.056213,5.231652,8.722804,5.894214,-2.941601,-0.396350,4.110621,-9.540105,-4.193313,-6.737634,4.766007,-6.156991,-8.729664,-5.441191,-9.254601,8.839447,-7.622997,-1.961160,9.840847,-5.921772,-2.714038,-0.006923,3.759817,3.804111,-0.004706,7.866342,2.833151,6.205920,0.635705,2.930515,9.672272,-0.648701,9.764804,0.103107,-2.528925,-4.473502,6.411618,8.539891,7.882482,-6.414566,-0.239921,3.544805,2.529281,6.126210,-8.172589,7.043651,2.280512,5.223960,-8.760027,-6.746397,-7.008201,1.018733,3.475023,-6.205761,9.222848,-1.276880,6.446052,4.462336,-7.586556,2.803574,6.261132,-7.343598,4.162601,5.820201,0.592576,-6.622485,-2.439289,7.561484,-9.222658,-0.246528,-7.450537,5.368417,7.376974,2.509945,-0.756459,-7.234607,2.968474,-2.994973,4.329587,-1.692634,2.616003,-4.632913,3.522367,8.668126,-5.041790,7.190146,-9.082350,-9.726503,-1.879383,-1.269618,-2.656731,-4.961389,2.013819,-9.999045,1.869848,2.797760,-0.652016,-7.770047,5.900525,0.317458,-6.076908,5.929955,-5.893707,-8.655482,2.793605,6.894739,5.120223,6.110846,-1.277854,6.138683,-2.459868,9.197985,1.050115,-7.901596,0.987342,-9.408301,8.944883,9.575892,8.144078,-8.835426,-8.248159,-3.951162,1.128093,-9.920377,-7.970606,0.295341,6.559637,0.654071,9.346816,4.704707,8.697073,-9.604403,1.666890,-9.707410,6.768497,6.884803,-0.460345,7.797504,1.923176,-7.173801,-8.687804,3.640927,-6.039797,-6.986605,-9.707701,-4.246287,1.035934,-9.489341,-4.345763,6.738663,5.229763,8.593918,-5.305327,-0.710159,7.318872,2.348892,-7.053772,1.608712,4.129755,-1.699740,5.277059,-5.120270,0.006113,-4.057063,0.638860,7.907831,-8.955568,8.580675,-5.173205,1.507479,-1.347831,1.800083,1.622985,9.020906,-1.106802,-2.211772,-1.187987,-4.553816,-0.007134,-5.906229,-6.913015,-6.083551,-0.902552], dtype = "float32")#candidate|8112|(495,)|const|float32
const_8113 = relay.const([-4,-1,-10,5,-5,6,-3,8,-7,3,5,-6,6,3,-7,-8,-1,-2,-9,5,-7,2,7,4,-7,7,-2,9,5,6,4,-2,2,-8,-10,-5,-3,7,-8,-5,9,5,6,-1,-3,4,-8,6,2,-3,8,-1,6,2,-8,7,10,-9,7,7,5,-1,10,5,3,4,5,-6,-3,4,-7,9,4,-4,-7,1,2,7,9,-4,9,8,3,-6,2,10,-1,-5,-6,-6,-9,5,8,5,-3,2,7,5,-1,8,10,-3,6,8,8,-7,2,2,1,7,-6,-5,8,5,-2,5,3,-7,-9,-3,10,5,1,1,-5,-7,9,6,-3,-9,5,8,-5,7,1,-2,-1,2,6,-3,4,-6,1,2,-2,-8,8,-5,1,8,3,3,-1,-7,2,2,9,1,-7,-5,-6,5,10,-9,-1,5,9,9,4,-8,5,2,-5,7,8,2,4,-9,9,-5,7,6,9,7,-1,-10,5,2,7,-4,1,10,-5,-10,-7,5,-7,1,6,9,-2,-6,5,9,-9,-8,8,6,6,-8,-4,-6,-1,7,4,-7,-7,3,2,5,-4,-2,10,6,7,-9,-4,-2,-4,6,-4,-4,5,4,-9,1,-1,-6,2,-7,7,-9,-2,7,7,2,6,6,-5,-1,9,-10,4,3,9,4,-7,6,-2,-3,-8,-4,-3,8,-1,2,2,2,7,1,-5,-3,-7,-2,-4,2,2,-8,6,-4,-8,9,-8,5,6,3,-2,6,5,-10,4,3,-8,2,-1,-1,3,-9,10,-8,2,2,6,-7,7,-10,-1,-9,-5,3,9,5,3,-3,-9,-1,-2,9,2,-9,-3,-2,-5,3,3,-6,-7,4,-6,-3,10,10,-7,-10,-4,10,1,2,-2,-5,-1,7,5,-10,-8,8,8,-10,6,6,10,-7,-5,-6,-6,-1,-4,-6,10,10,2,-6,5,-7,-5,-10,8,-7,-6,3,-7,-10,-3,-2,4,-10,1,9,3,8,1,-4,-5,6,-5,-3,3,3,-10,10,-6,-2,-8,4,9,9,10,-10,6,4,3,4,-1,-4,4,6,-6,-9,-1,8,-5,-1,2,-9,7,8,3,8,10,6,7,4,-2,10,5,5,-6,-4,8,-5,-7,7,-6,5,-8,-2,2,-10,8,-10,-7,5,-1,-10,-2,-4,-9,-10,-7,-2,5,9,9,-4,9,-2,-8,10,5,8,6,-6,-2,-3,-1,-3,-9,6,4,-7,-3,-1,-7,10,-4,9,10,-6,-4,-1,-4,-1,-1,-4,-6,-9,-1,2,3,10,-2,-9,4,5,6,5,2,-4,-3,-9,-9,-10,9,10,5,1,-9,-10,-6,3,2,-2,1,9,-4,7,-7,8,10,-9,-6,-4,1,-7,8,-8,7,-7,8,4,-6,-7,-9,-8,1,-4,8,-3,2,5,-2,-2,-5,-7,7,-4,4,4,8,-10,9,-7,4,5,2,5,5,10,6,-4,9,-6,1,6,-3,-8,2,1,-7,-9,-8,-2,-4,6,10,-5,-8,-3,2,-10,-6,9,-6,-4,-9,-4,9,-4,6,3,10,6,8,8,-7,-6,9,-10,8,-9,-7,5,-9,-9,9,-3,-7,-8,6,-6,6,-7,9,-1,-3,5,-5,8,-9,1,6,-8,2,-1,-4,3,-10,5,10,-8,6,5,-2,-5,9,-9,-9,1,3,-10,-8,6,-3,-9,9,-6,-9,-6,5,3,7,-10,-1,6,2,2,8,9,-1,4,4,-4,-2,-5,2,-10,10,-3,-2,4,6,-5], dtype = "int32")#candidate|8113|(672,)|const|int32
call_8109 = relay.TupleGetItem(func_7709_call(relay.reshape(var_8110.astype('uint64'), [840,]), relay.reshape(const_8111.astype('int16'), [135,]), relay.reshape(const_8103.astype('int32'), [105,]), relay.reshape(const_8112.astype('float32'), [495,]), relay.reshape(const_8113.astype('int32'), [672,]), relay.reshape(var_8102.astype('uint32'), [1694,]), ), 4)
call_8114 = relay.TupleGetItem(func_7717_call(relay.reshape(var_8110.astype('uint64'), [840,]), relay.reshape(const_8111.astype('int16'), [135,]), relay.reshape(const_8103.astype('int32'), [105,]), relay.reshape(const_8112.astype('float32'), [495,]), relay.reshape(const_8113.astype('int32'), [672,]), relay.reshape(var_8102.astype('uint32'), [1694,]), ), 4)
output = relay.Tuple([call_8076,call_8086,var_8087,call_8100,var_8101,var_8102,const_8103,call_8109,var_8110,const_8111,const_8112,const_8113,])
output2 = relay.Tuple([call_8077,call_8088,var_8087,call_8104,var_8101,var_8102,const_8103,call_8114,var_8110,const_8111,const_8112,const_8113,])
func_8115 = relay.Function([var_8087,var_8101,var_8102,var_8110,], output)
mod['func_8115'] = func_8115
mod = relay.transform.InferType()(mod)
var_8116 = relay.var("var_8116", dtype = "uint64", shape = (1350,))#candidate|8116|(1350,)|var|uint64
var_8117 = relay.var("var_8117", dtype = "uint32", shape = ())#candidate|8117|()|var|uint32
var_8118 = relay.var("var_8118", dtype = "uint32", shape = (1694,))#candidate|8118|(1694,)|var|uint32
var_8119 = relay.var("var_8119", dtype = "uint64", shape = (840,))#candidate|8119|(840,)|var|uint64
output = func_8115(var_8116,var_8117,var_8118,var_8119,)
func_8120 = relay.Function([var_8116,var_8117,var_8118,var_8119,], output)
mutated_mod['func_8120'] = func_8120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7753_call = mod.get_global_var('func_7753')
func_7754_call = mutated_mod.get_global_var('func_7754')
call_8145 = relay.TupleGetItem(func_7753_call(), 0)
call_8146 = relay.TupleGetItem(func_7754_call(), 0)
uop_8150 = relay.sin(call_8145.astype('float32')) # shape=(7, 4, 2)
uop_8152 = relay.sin(call_8146.astype('float32')) # shape=(7, 4, 2)
func_7461_call = mod.get_global_var('func_7461')
func_7466_call = mutated_mod.get_global_var('func_7466')
var_8165 = relay.var("var_8165", dtype = "float32", shape = (1, 490))#candidate|8165|(1, 490)|var|float32
const_8166 = relay.const(-5, dtype = "int64")#candidate|8166|()|const|int64
const_8167 = relay.const([-8,-4,-6,8,-4,-8,6,4,-10,9,1,-2,-4,8,1,-5,-6,-7,6,10,6,5,-6,9,10,-3,-8,4,7,3,-7,8,7,-10,1,-5,8,2,-8,7,1,-9,-8,2,4,5,6,-7,-1,8,-6,2,10,7,8,-8,-7,9,1,-3,7,-8,-3,7,-1,7,-5,-1,-4,-7,-4,1,-3,7,2,-10,-7,-3,3,-6,5,2,-4,-7,3,1,8,-9,4,4,5,6,-10,4,-1,8,4,5,4,6,-5,-5,3,-3,-1,3,-1,-1,10,-6,6,6,-5,7,5,9,2,-5,9,10,-7,7,3,-10,-3,-5,-2,8,4,-9,7,-2,-1,2,5,9,6,-9,-5,-4,-5,7,10,5,9,6,3,6,5,3,3,-1,9,10,8,2,2,1,3,9,-1,1,-1,7,9,5,3,1,-7,-5,4,8,-5,10,-6,-3,2,-10,-2,-10,-6,-3,2,-10,4,5,1,3,-2,-5,10,5,1,-6,2,-4,-10,7,10,2,-3,9,2,-7,5,-5,9,6,5,2,7,-10,-4,10,4,-5,2,-10,-8,-9,8,-9,-1,-8,-6,-8,8,-1,-4,-6,6,7,7,-10,-4,-9,10,3,10,2,2,2,-7,-2,-5,-1,-10,-9,-8,2,-10,8,7,-3,-1,-7,-6,-2,-2,-6,-3,-10,-9,-9,-9,-1,-4,-1,10,-9,3,-5,7,-2,4,-7,-6,9,7,-2,-3,-7,2,7,4,-3,6,-5,-5,-1,4,-5,5,8,6,-8,3,-5,5,-6,-1,-5,-9,9,7,3,10,-4,6,6,-3,10,-2,-4,-10,-8,-1,10,-3,-4,-1,-2,8,5,-1,5,-9,-4,1,-10,8,4,8,9,-6,-2,1,7,3,1,-7,9,-1,-7,-9,-5,-2,4,6,-3,-6,9,-10,-7,10,-6,4,1,6,-10,-4,2,6,5,-1,4,3,5,10,4,-9,5,6,9,-3,-9,-3,-2,-10,3,-5,-9,10,2,5,8,-6,7,10,-8,-4,1,-1,-10,-1,-10,-10,5,-2,-10,2,-9,2,4,2,8,-8,-7,3,10,8,10,-9,-8,1,6,-5,-4,2,2,10,2,-8,-9,-6,-4,-6,-2,9,-6,7,6,6,2,7,-2,1,-5,4,-1,2,5,-10,-5,-9,3,-10,10,6,3,-6,-10,-2,-6,-10,7,4,10,-8,-7,3,-5,-7,-10,-8,8,-2,1,-3,10,-5,3,-8,-3,7,5,8,-4,4,-9,7,-6,-4,-2,-3,-10,9,8,-8,4,-1,-7,9,-5,5,5,9,-10,-8,2,3,8,7,9,-6,-5,4,-7,3,-7,-8,-10,-6,2,3,3,-7,-7,-8,-4,-1,-3,-10,9,-6,2,1,-1,-2,-8,8,-10,6,-1,-6,-3,1,6,-8,-5,-3,8,-10,-8,-1,-9,2,4,-9,-4,-10,-3,-3,-4,-4,-5,7,9,-2,4,-5,-10,2,-5,-9,-7,-4,-1,7,-7,-4,8,-6,3,-5,-1,9,9,7,4,5,-4,10,-7,1,-10,6,10,-6,-2,-7,-5,-4,8,10,-7,3,-5,9,2,6,6,-9,-8,9,-9,-2,-3,-9,-10,-4,8,-10,-10,5,-10,-3,2,3,8,9,8,-2,-10,3,3,-4,-7,-2,-5,9,7,-2,-6,1,8,-1,-1,-9,-5,-8,-2,-9,-9,7,7,9,-10,5,9,9,-5,-4,-5,-7,7,-3,10,-9,-3,2,4,6,-6,9,-8,-5,-1,9,-3,-10,-2,9,-3,10,9], dtype = "int32")#candidate|8167|(676,)|const|int32
call_8164 = relay.TupleGetItem(func_7461_call(relay.reshape(var_8165.astype('float32'), [7, 10, 7]), relay.reshape(const_8166.astype('int64'), []), relay.reshape(const_8167.astype('int32'), [676,]), ), 2)
call_8168 = relay.TupleGetItem(func_7466_call(relay.reshape(var_8165.astype('float32'), [7, 10, 7]), relay.reshape(const_8166.astype('int64'), []), relay.reshape(const_8167.astype('int32'), [676,]), ), 2)
output = relay.Tuple([uop_8150,call_8164,var_8165,const_8166,const_8167,])
output2 = relay.Tuple([uop_8152,call_8168,var_8165,const_8166,const_8167,])
func_8169 = relay.Function([var_8165,], output)
mod['func_8169'] = func_8169
mod = relay.transform.InferType()(mod)
var_8170 = relay.var("var_8170", dtype = "float32", shape = (1, 490))#candidate|8170|(1, 490)|var|float32
output = func_8169(var_8170)
func_8171 = relay.Function([var_8170], output)
mutated_mod['func_8171'] = func_8171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7753_call = mod.get_global_var('func_7753')
func_7754_call = mutated_mod.get_global_var('func_7754')
call_8197 = relay.TupleGetItem(func_7753_call(), 0)
call_8198 = relay.TupleGetItem(func_7754_call(), 0)
output = relay.Tuple([call_8197,])
output2 = relay.Tuple([call_8198,])
func_8205 = relay.Function([], output)
mod['func_8205'] = func_8205
mod = relay.transform.InferType()(mod)
output = func_8205()
func_8206 = relay.Function([], output)
mutated_mod['func_8206'] = func_8206
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7980_call = mod.get_global_var('func_7980')
func_7981_call = mutated_mod.get_global_var('func_7981')
call_8234 = func_7980_call()
call_8235 = func_7980_call()
output = call_8234
output2 = call_8235
func_8239 = relay.Function([], output)
mod['func_8239'] = func_8239
mod = relay.transform.InferType()(mod)
mutated_mod['func_8239'] = func_8239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8239_call = mutated_mod.get_global_var('func_8239')
call_8240 = func_8239_call()
output = call_8240
func_8241 = relay.Function([], output)
mutated_mod['func_8241'] = func_8241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7753_call = mod.get_global_var('func_7753')
func_7754_call = mutated_mod.get_global_var('func_7754')
call_8256 = relay.TupleGetItem(func_7753_call(), 0)
call_8257 = relay.TupleGetItem(func_7754_call(), 0)
var_8264 = relay.var("var_8264", dtype = "int32", shape = (7, 4, 2))#candidate|8264|(7, 4, 2)|var|int32
bop_8265 = relay.multiply(call_8256.astype('int16'), relay.reshape(var_8264.astype('int16'), relay.shape_of(call_8256))) # shape=(7, 4, 2)
bop_8268 = relay.multiply(call_8257.astype('int16'), relay.reshape(var_8264.astype('int16'), relay.shape_of(call_8257))) # shape=(7, 4, 2)
func_4760_call = mod.get_global_var('func_4760')
func_4763_call = mutated_mod.get_global_var('func_4763')
var_8270 = relay.var("var_8270", dtype = "int64", shape = ())#candidate|8270|()|var|int64
var_8271 = relay.var("var_8271", dtype = "int64", shape = (2, 20))#candidate|8271|(2, 20)|var|int64
call_8269 = relay.TupleGetItem(func_4760_call(relay.reshape(var_8270.astype('int64'), []), relay.reshape(var_8271.astype('int64'), [4, 1, 10]), ), 0)
call_8272 = relay.TupleGetItem(func_4763_call(relay.reshape(var_8270.astype('int64'), []), relay.reshape(var_8271.astype('int64'), [4, 1, 10]), ), 0)
output = relay.Tuple([bop_8265,call_8269,var_8270,var_8271,])
output2 = relay.Tuple([bop_8268,call_8272,var_8270,var_8271,])
func_8273 = relay.Function([var_8264,var_8270,var_8271,], output)
mod['func_8273'] = func_8273
mod = relay.transform.InferType()(mod)
mutated_mod['func_8273'] = func_8273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8273_call = mutated_mod.get_global_var('func_8273')
var_8275 = relay.var("var_8275", dtype = "int32", shape = (7, 4, 2))#candidate|8275|(7, 4, 2)|var|int32
var_8276 = relay.var("var_8276", dtype = "int64", shape = ())#candidate|8276|()|var|int64
var_8277 = relay.var("var_8277", dtype = "int64", shape = (2, 20))#candidate|8277|(2, 20)|var|int64
call_8274 = func_8273_call(var_8275,var_8276,var_8277,)
output = call_8274
func_8278 = relay.Function([var_8275,var_8276,var_8277,], output)
mutated_mod['func_8278'] = func_8278
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8294 = relay.var("var_8294", dtype = "bool", shape = ())#candidate|8294|()|var|bool
var_8295 = relay.var("var_8295", dtype = "bool", shape = (16, 16, 16))#candidate|8295|(16, 16, 16)|var|bool
bop_8296 = relay.logical_or(var_8294.astype('bool'), var_8295.astype('bool')) # shape=(16, 16, 16)
func_7391_call = mod.get_global_var('func_7391')
func_7394_call = mutated_mod.get_global_var('func_7394')
call_8314 = relay.TupleGetItem(func_7391_call(relay.reshape(var_8294.astype('uint16'), [])), 0)
call_8315 = relay.TupleGetItem(func_7394_call(relay.reshape(var_8294.astype('uint16'), [])), 0)
func_5526_call = mod.get_global_var('func_5526')
func_5529_call = mutated_mod.get_global_var('func_5529')
const_8322 = relay.const([-2,7,9,-4,6,9,10,2,5,-2,8,-3,-5,-7,-3,-9,-1,2,4,10,2,4,3,5,3,6,-7,8,5,6,6,-2,-4,6,-10,10,8,-5,-1,-9,-6,-6,6,-6,-3,-9,-8,5,7,3,-10,1,-8,10,-7,-4,6,7,-7,-2,-5,-9,-4,-6,6,8,2,-5,-8,-10,6,9,3,3,-10,10,8,10,-4,2,-8,9,10,10,10,4,-3,9,2,8,9,-9,7,-8,8,4,-8,5,8,-7,-5,-4,5,-4,7,9,10,-2,7,-2,10,2,1,-8,-5,5,8,-8,-7,8,-6,2,4,7,-6,8,-4,-5,-10,-4,-10,4,-2,-10,9,-3,-6,-3,8,4,6,1,-4,7,-9,-8,-1,8,-5,10,-10,-8,-9,9,-8,3,-6,-8,-1,4,-7,3,-5,9,1,5,-6,8,-6,3,9,-10,10,-7,4,-3,6,-8,8,2,-9,-1,-1,-10,-7,3,-1,-2,2,4,-3,-6,4,9,-1,1,9,7,-4,-1,10,-8,-6,1,-2,-5,-3,-3,4,9,4,-7,6,6,-9,-3,-8,1,3,-5,9,9,10,-9,3,-2,-1,-9,3,9,2,-2,-4,6,4,-4,1,5,7,-6,3,7,-8,-3,4,2,5,-8,-6,-8,-6,-3,10,-8,1,7,-3,10,-3,-10,-6,-4,-8,-9,7,-7,4,9,10,-8,3,-7,-2,-8,1,-3,-2,-9,9,5,7,-8,3,-2,-5,4,-8,4,1,4,-2,10,-3,-6,-6,6,-4,4,-2,-10,1,-6,-6,-8,4,10,8,-2,8,-3,1,-8,6,4,-10,-6,10,-9,-10,-5,10,2,5,1,4,-8,5,-1,7,8,10,10,4,8,10,-10,-1,10,-6,9,-5,4,2,1,-1,-9,-3,-2,-2,-2,-6,-1,-7,-4,2,-3,-10,-6,-2,-4,-8,-3,3,9,-8,8,-7,10,9,-7,7,9,6,-2,6,3,-10,-6,-2,10,8,-3,-6,9,6,8,5,-3,-5,-3,-2,5,-1,-8,-8,4,-6,-2,-9,-10,6,-8,-7,6,-5,-3,3,10,-8,10,7,-1,10,-7,-4,-4,5,3,-3,4,-6,-7,-6,5,-5,10,-9,-7,6,-8,1,3,5,7,-5,-8,-9,-3,1,-1,-3,10,-3,8,1,2,-9,-7,2,-4,7,9,-6,1,10,-4,4,-2,-1,8,8,5,4,-4,5,3,-2,8,-7,-5,-2,10,3,2,-4,-9,10,-2,5,1,7,-2,6,-7,10,10,1,5,-1,9,7,8,9,2,-9,3,-4,-5,6,5,-3,5,2,7,9,7,-3,3,-6,-7,-5,10,-7,2,-6,7,-2,3,-4,-7,8,1,10,3,-1,2,-3,7,-9,5,-8,5,7,-3,-10,-6,-4,-10,-2,-2,-5,9,9,10,-7,-3,9,2,-8,7,-5,8,1,-6,3,6,-4,-8,2,-1,6,3,-2,9,2,-9,2,-6,5,8,10,8,10,9,5,-1,3,-6,9,-6,3,5,3,8,5,-6,9,-1,9,3,1,6,-7,1,-8,-6,2,-6,-5,3,-10,5,2,-10,-7,8,6,9,6,9,9,-7,-9,6,-7,3,7,-9,-5,1,-4,7,-10,-3,-8,-4,-10,-8,4,-2,-2,-10,-5,7,10,2,-4,3,-7,4,-1,-4,9,-9,-5,-8,9,5,9,-4,7,-2,-6,7,-1,1,-9,-4,-7,3,-7,-1,9,8,8,-8,9,8,-4,1,7,-9,8,-5,8,9], dtype = "int32")#candidate|8322|(676,)|const|int32
call_8321 = func_5526_call(relay.reshape(const_8322.astype('int32'), [13, 4, 13]))
call_8323 = func_5526_call(relay.reshape(const_8322.astype('int32'), [13, 4, 13]))
output = relay.Tuple([bop_8296,call_8314,call_8321,const_8322,])
output2 = relay.Tuple([bop_8296,call_8315,call_8323,const_8322,])
func_8329 = relay.Function([var_8294,var_8295,], output)
mod['func_8329'] = func_8329
mod = relay.transform.InferType()(mod)
var_8330 = relay.var("var_8330", dtype = "bool", shape = ())#candidate|8330|()|var|bool
var_8331 = relay.var("var_8331", dtype = "bool", shape = (16, 16, 16))#candidate|8331|(16, 16, 16)|var|bool
output = func_8329(var_8330,var_8331,)
func_8332 = relay.Function([var_8330,var_8331,], output)
mutated_mod['func_8332'] = func_8332
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8403 = relay.var("var_8403", dtype = "float64", shape = (2, 16, 9))#candidate|8403|(2, 16, 9)|var|float64
var_8404 = relay.var("var_8404", dtype = "float64", shape = (2, 16, 9))#candidate|8404|(2, 16, 9)|var|float64
bop_8405 = relay.mod(var_8403.astype('float64'), relay.reshape(var_8404.astype('float64'), relay.shape_of(var_8403))) # shape=(2, 16, 9)
output = bop_8405
output2 = bop_8405
func_8408 = relay.Function([var_8403,var_8404,], output)
mod['func_8408'] = func_8408
mod = relay.transform.InferType()(mod)
var_8409 = relay.var("var_8409", dtype = "float64", shape = (2, 16, 9))#candidate|8409|(2, 16, 9)|var|float64
var_8410 = relay.var("var_8410", dtype = "float64", shape = (2, 16, 9))#candidate|8410|(2, 16, 9)|var|float64
output = func_8408(var_8409,var_8410,)
func_8411 = relay.Function([var_8409,var_8410,], output)
mutated_mod['func_8411'] = func_8411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7980_call = mod.get_global_var('func_7980')
func_7981_call = mutated_mod.get_global_var('func_7981')
call_8453 = func_7980_call()
call_8454 = func_7980_call()
func_4760_call = mod.get_global_var('func_4760')
func_4763_call = mutated_mod.get_global_var('func_4763')
const_8460 = relay.const(1, dtype = "int64")#candidate|8460|()|const|int64
var_8461 = relay.var("var_8461", dtype = "int64", shape = (40,))#candidate|8461|(40,)|var|int64
call_8459 = relay.TupleGetItem(func_4760_call(relay.reshape(const_8460.astype('int64'), []), relay.reshape(var_8461.astype('int64'), [4, 1, 10]), ), 0)
call_8462 = relay.TupleGetItem(func_4763_call(relay.reshape(const_8460.astype('int64'), []), relay.reshape(var_8461.astype('int64'), [4, 1, 10]), ), 0)
output = relay.Tuple([call_8453,call_8459,const_8460,var_8461,])
output2 = relay.Tuple([call_8454,call_8462,const_8460,var_8461,])
func_8475 = relay.Function([var_8461,], output)
mod['func_8475'] = func_8475
mod = relay.transform.InferType()(mod)
mutated_mod['func_8475'] = func_8475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8476 = relay.var("var_8476", dtype = "int64", shape = (40,))#candidate|8476|(40,)|var|int64
func_8475_call = mutated_mod.get_global_var('func_8475')
call_8477 = func_8475_call(var_8476)
output = call_8477
func_8478 = relay.Function([var_8476], output)
mutated_mod['func_8478'] = func_8478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mod.get_global_var('func_8205')
func_8206_call = mutated_mod.get_global_var('func_8206')
call_8575 = relay.TupleGetItem(func_8205_call(), 0)
call_8576 = relay.TupleGetItem(func_8206_call(), 0)
func_6947_call = mod.get_global_var('func_6947')
func_6950_call = mutated_mod.get_global_var('func_6950')
const_8578 = relay.const([3,-3,8,4,4,-3,2,3,8,-10,1,-2,4,-5,3,10,-5,-5,-6,1,4,4,-5,9,-8,-2,1,-3,1,-1,-8,-10,-3,-8,-5,-2,-4,5,5,3,-3,4,1,10,-7,-4,-1,8,1,-6,6,3,4,1,2,-5,-1,8,6,1,10,-6,2,-6,1,-9,-1,1,2,7,8,-6,8,-10,-5,-8,8,5,-10,-5,4,2,-8,-3,4,2,-9,-8,4,3,-9,-4,5,-7,10,-7,-5,2,-1,4,4,-7,4,-1,-5,10,5,1,3,8,1,10,6,1,-8,3,1,-6,-5,-5,-3,-6,-9,10,-6,-5,-4,7,8,7,3,7,-10,-10,10,-7,10,-1,10,-9,2,7,9,-7,-4,-3,4,2,3,-1,7,5,-1,4,-10,10,-7,7,3,-4,-8,-5,-9,6,-8,2,-7,1,-3,-9,-10,-6,-8,-4,9,-7,7,9,8,5,-4,-3,5,-9,1,-3,7,-7,-2,-7,10,-8,-7,-10,-4,-2,1,-1,9,5,8,-10,-9,1,9,4,3,4,-1,-4,9,-7,-1,-7,8,10,-3,-10,-9,-6,8,-10,2,-10,10,9,-10,-10,-5,-3,2,-7,-4,-7,-10,3,-3,-9,-9,-9,5,-6,6,-7,-6,4,-4,3,9,-2,3,7,2,-2,-8,-8,10,-9,-4,9,-9,-8,-5,-2,10,-5,3,8,1,4,10,-2,8,7,10,-1,-9,1,-7,2,8,10,-1,-7,-8,-10,3,-9,5,-4,-1,3,4,-6,8,-10,-5,-8,-1,-9,-5,7,2,2,1,-2,1,-2,9,9,6,-4,10,-9,6,-1,-10,-1,-4,10,9,10,7,-8,-10,4,6,8,9,-8,7,7,8,10,3,9,-3,-5,-1,-9,-9,8,2,-3,5,-7,1,-10,4,-10,1,2,-10,-8,-1,3,-1,-7,-9,3,2,-6,4,1,-5,8,2,-2,6,-5,-7,8,1,1,8,4,4,2,-8,-7,-3,1,-4,10,-2,-8,3,-7,3,-6,1,-10,2,4,-4,2,-5,-5,-5,8,7,-6,-4,-9,-2,8,5,-10,-10,6,3,-3,1,7,2,5,1,-2,-4,-2,5,2,7,-6,4,5,2,-8,-6,10,10,7,-5,-6,1,-7,-9,-6,-1,-7,6,4,10,2,-7,-3,-6,-8,-9,-3,-4,7,-1,4,-7,7,-3,-3,5,6,-8,10,-9,-8,-5,-1,3,-6,2,8,-1,5,8,-4,5,-6,10,8,6,-10,-9,2,10,8,-8,-3,3,-2,6,-7,-7,-4,1,-6,8,-8,8,10,-9,-2,-7,5,-1,-3,2,-9,-5,6,5,-2,10,1,-1,-6,1,9,-2,-10,-3,3,-4,-4,3,4,-2,2,-6,9,-4,-2,-4,-5,-5,-1,-7,-4,5,10,8,8,10,-3,3,-8,7,-3,10,7,-2,-6,3,2,9,-9,-7,10,-7,8,3,10,-5,-10,3,-2,8,-6,9,-2,-3,9,8,-1,-10,-8,4,-4,-10,-6,6,10,8,-8,5,7,-10,9,-6,4,9,1,-7,2,1,-2,6,2,9,2,9,3,-8,7,5,9,1,-5,5,10,3,-5,-6,-2,-7,1,4,5,-8,-5,4,-5,4,-5,-5,-6,-9,-7,10,-9,4,2,4,1,10,5,9,-8,9,-3,10,-5,4,3,-3,-10,-2,8,-8,10,-4,1,-4,-8,6,-9,3,-5,-8,-9,-1,-2,1,-1,-9,-6,-7,-8,-8,5,-8,-10,10,7,6,-1,-7,1,2,-7,-4,-6,2,3,-10,5,3,-10,3,-1,3,5,4,8,-10,7,-7,-5,6,-10,6,-4,-1,4,-10,-2,-8,7,-4,7,9,10,-8,-5,-4,-9,-8,-1,-7,-2,1,-2,-2,-2,3,2,5,7,8,-8,-7,-5,1,-6,3,5,-6,5,-7,6,-6,1,-2,-7,-10,-5,3,6,7,10,1,-6,-4,5,-7,3,-9,7,5,-4,-10,-4,8,-4,-1,5,-4,9,1,1,-4,1,1,7,-1,-10,9,-3,3,3,4,6,-8,-7,-10,7,3,9,6,-9,-6,-8,-3,1,-10,10,2,-3,-2,1,9,5,-8,7,10,-10,4,-1,-9,-3,-9,-3,8,3,-6,-3,4,6,-4,-5,8,-1,3,9,8,-1,4,10,-1,3,9,2,-6,7,-5,4,-8,-8,-9,-3,1,-4,1,9,6,1,10,1,6,-5,8,4,2,-7,9,10,7,4,-7,-1,-7,-10,-8,4,-7,-2,-6,-3,8,-3,-1,6,-6,-5,3,8,6,10,9,7,3,-2,-8,9,-4,-3,-5,10,-9,-6,1,-4,-4,-1,10,-10,7,-2,-5,-1,3,-6,10,2,1,2,4,8,-2,-2,9,5,-3,3,8,-9,-7,-1,-10,-6,3,-4,-6,6,3,2,1,10,-2,2,-4,-5,5,-7,1,6,3,-2,4,1,-7,9,-8,-9,-9,-4,-1,5,-5,9,-8,-1,-6,-4,-10,-8,-7,6,-6,-10,6,-2,-3,3,9,-5,8,2,8,6,10,-6,3,-6,6,5,-10,-9,4,-10,-3,-2,10,6,-9,-5,-6,-7,2,7,-9,-2,-9,-1,-4,-8,7,-9,-3,4,-7,10,-1,-4,10,3,-6,-10,5,-10,4,5,7,10,-8,9,-5,-1,-5,9,8,7,-4,-1,-8,-7,10,-6,5,4,-4,1,3,6,-6,-5,7,-10,-9,-2,-3,-1,-1,9,-5,-1,7,8,3,8,-9,6,7,6,9,2,7,5,10,-5,-7,6,8,4,8,-3,-6,-10,6,-10,-4,-7,6,8,-5,3,-9,6,4,9,3,-8,2,4,6,1,6,10,9,8,-10,6,3,-7,1,9,-9,-2,5,-8,-10,2,6,-8,9,-9,-10,-10,-6,-7,4,-10,1,5,2,8,2,-9,-1,5,4,10,-10,4,7,4,7,6,10,5,-3,-5,4,-3,-1,-6,-4,-7,-5,2,-2,3,2,9,-9,3,9,6,2,-10,-2,5,1,2,-5,-7,-1,-6,10,-5,2,-10,8,6,-9,-10,-3,7,-9,1,3,10,-8,7,4,6,3,-8,-4,-10,1,6,-7,7,1,-9,-5,8,-9,-1,10,8,-3,-4,-1,2,4,-3,10,-6,-9,5,8,-7,-10,-10,6,-4,6,-8,2,-8,-7,-7,2,-7,-2,7,6,7,-2,8,6,-9,-10,9,6,-8,10,-9,9,-5,10,1,6,6,4,8,-6,2,3,-9,1,-3,3,3,-1,2,-10,9,-10,4,7,-4,8,-2,-1,1,10,-3,7,4,-6,-9,-1,10,1,5,-5,-4,7,5,9,-10,-1,10,10,-8,-2,3,-5,-5,7,8,-9,7,10,-3,-8,-6,7,9,-3,6,-3,-9,1,7,-1,2,-7,5,-10,6,1,-7,1,-6,4,-10,-2,-5,2,-3,-7,3,5,-3,6,3,5,-6,7,-3,-5,-7,-1,-1,6,-7,10,-1,8,10,-5,-1,-4,-9,10,-3,4,-1,-4,-9,6,-5,6,3,-10,-9,-5,-7,7,9,9,-2,2,9,6,8,4,10,1,-5,6,8,-4,10,5,9,-3,-7,6,3,-4,6,8,7,9,10,5,7,-5,1,8,1,2,-6,-4,10,4,5,10,-9,5,4,-7,9,8,9,-1,7,10,2,6,1,8,10,-9,8,-10,4,-3,-9,-5,7,1,-1,-9,5,5,-3,-2,-10,6,5,-8,3,-1,2,-3,4,-5,4,-8,-7,-3,-3,-5,-7,8,-5,10,10,2,-7,-5,8,-6,1,-9,4,-1,8,9,-7,7,7,-1,9,1,8,-9,-3,7,10,6,-10,2,-1,3,-9,-1,8,-3,5,4,-9,2,-9,-8,4,2,1,4,-6,1,9,-2,-3,-5,1,4,4,2,4,2,-5,6,10,-7,6,4,9,-6,2,-5,-3,-1,-6,2,-4,-9,-1,-5,4,-9,-2,-8,8,-5,7,3,8,7,-6,3,-3,9,1,7,7,-8,7,-10,-1,-7,-5,-6,-4,-9,4,-10,-6,3,4,3,-3,8,8,-9,3,5,4,-2,-8,9,-3,-9,10,8,-9,5,1,-4,-1,8,-8,-3,6,-1,6,-6,-10,10,6,-4,-1,1,-2,1,-7,-9,-1,9,8,4,1,5,-5,-1,-4,-10,-6,7,5,1,-8,-8,1,-8,7,-6,-2,-2,-7,9,-10,6,-9,3,-2,5,5,1,-9,6,1,-6,3,9,1,-3,9,8,-4,-10,-5,8,-8,-5,-8,-5,-3,1,7,7,-9,10,10,6,8,4,-10,-3,-1,-7,9,7,1,9,-9,-9,-7,-6,6,4,-5,9,-1,6,-1,5,5,4,-2,-5,1,7,4,4,-3,-5,-7,8,9,3,6,-1,-10,6,-10,-2,8,7,-3,1,-1,8,5,7,-7,3,8,6,-9,-9,5,9,1,5,-9,1,7,2,-5,-3,1,8,9,7,-6,6,10,-7,3,6,-8,-4,8,6,-6,6,6,7,7,5,2,5,9,4,3,4,7,-8,-5,-8,5,6,-7,-9,9,-8,-7,5,-6,-8,9,10,-1,2,-5,4,-4,1,5,4,6,-5,6,1,-8,-10,-10,-4,-1,8,9,-5,-4,4,8,5,1,-1,9,8,-10,8,-9,4,1,5,3,2,-8,-9,4,4,-4,-10,-6,4,-7,7,-5,7,2,5,-3,3,3,10,5,-1,-9,-2,1,3,8,-7,3,-8,-7,-10,-2,-4,6,10,-9,10,6,-7,10,7,1,1,-8,-1,-4,7,-6,8,-8,3,1,-7,7,-6,-5,-5,8,2,-6,3,6,3,3,-3,-2,-8,10,-2,3,-4,-2,5,-4,8,-2,10,-10,-1,6,6,2,5,-1,-1,-6,3,3,-7,-4,8,5,5,1,-8,10,9,8,-6,-10,5,1,3,5,2,5,7,-10,-5,10,9,9,-4,1,-8,-4,-6,-1,10,1,5,-3,-5,-7,-5,-6,-7,-4,2,10,8,-2,-10,5,9,3,1,-8,-1,9,-4,-2,-7,-3,-4,8,-8,8,5,5,9,-8,3,7,5,-10,10,-3,10,8,10,6,8,3,7,-7,-7,7,5,6,1,-10,-9,7,-8,3,-5,-3,5,6,5,10,-10,-3,-2,-2,4,1,-4,3,7,7,7,5,-7,3,4,-5,-10,-9,7,5,-3,7,7,9,-5,6,-8,1,-1,1,-10,2,-5,4,4,5,6,-7], dtype = "int8")#candidate|8578|(2002,)|const|int8
call_8577 = relay.TupleGetItem(func_6947_call(relay.reshape(const_8578.astype('int8'), [14, 11, 13]), relay.reshape(const_8578.astype('int8'), [14, 11, 13]), ), 0)
call_8579 = relay.TupleGetItem(func_6950_call(relay.reshape(const_8578.astype('int8'), [14, 11, 13]), relay.reshape(const_8578.astype('int8'), [14, 11, 13]), ), 0)
uop_8580 = relay.log(call_8577.astype('float32')) # shape=(14, 11, 13)
uop_8582 = relay.log(call_8579.astype('float32')) # shape=(14, 11, 13)
func_2741_call = mod.get_global_var('func_2741')
func_2746_call = mutated_mod.get_global_var('func_2746')
const_8593 = relay.const([-8.295034,0.364431,-1.216489,-4.857413,4.226530,-4.451099,-5.230563,-0.524950,-1.610479,-7.434167,-8.158913,-0.133104,-5.727576,-6.584716,-2.492323,-9.038931,-7.295871,7.265609,2.952992,4.790791,-2.247334,8.997194,7.496374,-8.600140,3.796920,-3.258718,-1.465455,4.290362,6.511698,-7.651648,9.180697,-9.175356,7.883943,6.388504,0.275808,0.487383,-6.435459,-2.647364,8.826550,2.654685], dtype = "float64")#candidate|8593|(40,)|const|float64
const_8594 = relay.const([-4,1,-8,-7,-1,1,1,-4,-1,6,-7,1,-4,-10,-4,-10,-4,8,6,-2,-10,2,8,-2,7,1,10,-8,9,-5,-7,-1,6,4,5,-10,7,-8,-1,6,-8,-2,10,-3,1,2,-5,-8,4,-4,8,-2,9,1,-10,-8,3,9,3,4,1,2,1,-6,4,2,5,6,-5,4,6,-6,-3,4,-8,-7,-4,-5,-1,-2,1,8,9,2,2,3,-7,7,-5,-3,1,4,-3,2,9,10,7,8,1,-4,-7,1,6,-3,2,6,9,9,-8,-5,-7,9,-2,-4,8,-8,-4,8,-8,1,-10,-3,6,1,5,2,-5,-7,-7,-2,8,-9,-10,2,-1,-9,-1,-2,-6,-2,-2,-4,5,-4,2,-7,-5,-3,-7,-2,-8,-9,-3,8,5,10,-4,2,6,4,-1,10,-9,-10,6,7,3,4,9,5,2,1,2,7,-9,-7,2,-8,-10,9,2,-1,2,-3,9,-6,3,-9,1,2,9,-2,-9,-3,-1,-3,10,10,-1,-4], dtype = "int64")#candidate|8594|(200,)|const|int64
var_8595 = relay.var("var_8595", dtype = "float32", shape = (1, 495))#candidate|8595|(1, 495)|var|float32
call_8592 = relay.TupleGetItem(func_2741_call(relay.reshape(const_8593.astype('float64'), [1, 5, 8]), relay.reshape(const_8594.astype('int64'), [200,]), relay.reshape(var_8595.astype('float32'), [495,]), ), 2)
call_8596 = relay.TupleGetItem(func_2746_call(relay.reshape(const_8593.astype('float64'), [1, 5, 8]), relay.reshape(const_8594.astype('int64'), [200,]), relay.reshape(var_8595.astype('float32'), [495,]), ), 2)
func_6947_call = mod.get_global_var('func_6947')
func_6950_call = mutated_mod.get_global_var('func_6950')
call_8609 = relay.TupleGetItem(func_6947_call(relay.reshape(call_8577.astype('int8'), [14, 11, 13]), relay.reshape(uop_8580.astype('int8'), [14, 11, 13]), ), 0)
call_8610 = relay.TupleGetItem(func_6950_call(relay.reshape(call_8577.astype('int8'), [14, 11, 13]), relay.reshape(uop_8580.astype('int8'), [14, 11, 13]), ), 0)
output = relay.Tuple([call_8575,const_8578,uop_8580,call_8592,const_8593,const_8594,var_8595,call_8609,])
output2 = relay.Tuple([call_8576,const_8578,uop_8582,call_8596,const_8593,const_8594,var_8595,call_8610,])
func_8613 = relay.Function([var_8595,], output)
mod['func_8613'] = func_8613
mod = relay.transform.InferType()(mod)
var_8614 = relay.var("var_8614", dtype = "float32", shape = (1, 495))#candidate|8614|(1, 495)|var|float32
output = func_8613(var_8614)
func_8615 = relay.Function([var_8614], output)
mutated_mod['func_8615'] = func_8615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7614_call = mod.get_global_var('func_7614')
func_7615_call = mutated_mod.get_global_var('func_7615')
call_8629 = relay.TupleGetItem(func_7614_call(), 0)
call_8630 = relay.TupleGetItem(func_7615_call(), 0)
output = relay.Tuple([call_8629,])
output2 = relay.Tuple([call_8630,])
func_8648 = relay.Function([], output)
mod['func_8648'] = func_8648
mod = relay.transform.InferType()(mod)
mutated_mod['func_8648'] = func_8648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8648_call = mutated_mod.get_global_var('func_8648')
call_8649 = func_8648_call()
output = call_8649
func_8650 = relay.Function([], output)
mutated_mod['func_8650'] = func_8650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8735 = relay.var("var_8735", dtype = "float64", shape = (5, 9, 11))#candidate|8735|(5, 9, 11)|var|float64
uop_8736 = relay.acosh(var_8735.astype('float64')) # shape=(5, 9, 11)
func_8648_call = mod.get_global_var('func_8648')
func_8650_call = mutated_mod.get_global_var('func_8650')
call_8744 = relay.TupleGetItem(func_8648_call(), 0)
call_8745 = relay.TupleGetItem(func_8650_call(), 0)
output = relay.Tuple([uop_8736,call_8744,])
output2 = relay.Tuple([uop_8736,call_8745,])
func_8760 = relay.Function([var_8735,], output)
mod['func_8760'] = func_8760
mod = relay.transform.InferType()(mod)
mutated_mod['func_8760'] = func_8760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8761 = relay.var("var_8761", dtype = "float64", shape = (5, 9, 11))#candidate|8761|(5, 9, 11)|var|float64
func_8760_call = mutated_mod.get_global_var('func_8760')
call_8762 = func_8760_call(var_8761)
output = call_8762
func_8763 = relay.Function([var_8761], output)
mutated_mod['func_8763'] = func_8763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8648_call = mod.get_global_var('func_8648')
func_8650_call = mutated_mod.get_global_var('func_8650')
call_8808 = relay.TupleGetItem(func_8648_call(), 0)
call_8809 = relay.TupleGetItem(func_8650_call(), 0)
func_6947_call = mod.get_global_var('func_6947')
func_6950_call = mutated_mod.get_global_var('func_6950')
const_8820 = relay.const([-3,1,-9,-10,-8,-7,6,-8,4,-1,-9,4,1,-5,10,-2,6,7,-6,-10,-4,3,-8,-10,-10,-3,-5,10,6,-3,-7,1,10,-9,-5,-9,7,-2,2,9,-2,-2,-7,7,10,-2,-4,-2,-1,9,9,8,1,-1,1,-6,10,1,10,5,-7,9,-9,6,-4,-7,-4,-1,4,-7,-1,9,-10,-3,10,2,-4,-1,-4,5,5,-2,-9,-3,4,10,-4,7,1,4,-5,-1,9,-3,10,-4,-10,-5,9,3,-9,-7,2,-6,-3,4,-9,8,-8,5,-9,-4,-3,-7,6,-6,-3,-9,6,-7,8,-8,8,-8,-6,-4,-2,-5,7,9,-4,-10,5,-1,5,-1,-1,3,-4,-6,4,7,-8,10,8,9,-2,8,-8,-2,1,7,10,-1,-9,-7,7,-8,10,-10,-7,10,-8,9,-9,9,4,-4,-6,-1,4,-9,-5,5,4,4,6,1,4,10,-10,-5,-8,1,6,10,-1,10,-7,1,-2,-5,1,-4,5,-8,6,-1,2,8,-3,7,-9,-10,-4,10,-8,-6,-10,-3,4,-3,-7,-5,-8,7,1,-7,-9,-7,-10,8,-3,-8,-5,-9,4,-1,6,-10,-7,6,-8,-8,-2,1,3,1,-6,-8,-3,3,-9,-8,10,-9,-4,-7,-10,1,-10,-5,6,1,-6,-4,-8,-6,-1,3,-2,-10,-1,-9,10,2,-6,6,-2,3,-8,7,-6,-4,-7,10,-1,-4,-7,-3,4,-8,-4,-2,1,-6,-6,4,6,-1,-5,10,1,-8,8,-5,9,-5,-10,-9,4,-10,8,2,-4,-5,-4,-6,-1,-3,-6,-3,6,5,-5,-6,10,1,10,2,-6,2,1,5,2,1,10,2,2,-1,2,9,-1,-1,-2,4,9,-10,-4,2,-4,-4,9,-10,3,-9,9,8,8,3,-2,10,3,-2,4,4,9,2,-6,-10,-6,-6,8,-4,-5,6,4,-1,-5,-5,-8,-7,-9,-6,3,-3,-6,-3,5,1,-4,9,5,4,-2,-9,10,-7,6,5,1,8,9,2,-9,-3,-9,1,-2,-6,-6,5,2,6,-7,-7,10,-6,9,2,10,-2,-10,5,-10,6,-7,-3,-5,6,1,-2,1,2,5,-9,-1,-6,-6,3,-5,3,10,-10,6,-8,-9,9,-10,1,9,2,3,-3,2,-4,-4,6,2,10,-2,-4,-1,-3,8,-6,-8,-6,-8,-9,-4,-5,9,-4,-7,-8,5,2,-6,8,-10,8,-3,-6,-3,1,-7,4,8,-6,2,-6,5,4,-2,5,7,8,8,-2,1,8,8,6,2,4,6,-3,-9,-2,1,3,-1,-1,8,-1,5,-9,-3,-2,6,1,8,-3,-2,8,-10,-5,-1,-9,-8,-8,-10,-9,-3,-8,-8,1,2,3,-8,-9,-9,9,-1,-10,1,-3,4,-5,-4,6,-1,-10,-10,7,1,6,2,-1,-6,-3,9,-9,9,-2,7,9,-4,9,1,3,5,3,5,-2,6,-9,1,-10,9,5,9,-4,-2,-10,-10,-4,-2,-6,-2,-9,4,-5,-5,-7,-6,-10,8,-9,-8,3,2,5,-4,-1,9,-7,10,-8,-9,-9,7,2,-5,6,-2,1,4,-7,9,9,10,9,-9,4,1,-3,-5,2,7,-3,-6,-4,4,-1,9,-1,5,10,-8,-2,-8,-7,-3,2,8,-1,-2,5,6,1,5,6,-3,-5,-9,-1,-5,7,-7,8,-6,10,-3,6,-10,-5,-10,-6,-5,5,2,-10,-2,5,-8,7,-3,4,1,-7,8,7,-3,10,-5,-4,10,-4,-5,-4,-3,8,5,3,-1,-6,-2,-6,7,5,-2,-1,-4,-5,-7,1,9,7,9,-9,-2,-3,1,1,7,1,4,-4,-8,-5,-9,4,-6,-1,5,-9,-6,-3,-2,-4,-8,-10,9,-1,2,-2,4,6,-9,7,6,10,8,10,8,1,-1,10,-5,-6,1,-8,6,-7,3,-8,1,5,-3,-9,1,9,-1,3,-2,-4,9,-7,10,-9,-7,-3,6,8,-5,10,-9,1,8,7,-4,-2,-5,-7,3,7,2,-8,10,-8,5,2,-9,-5,8,8,4,-5,8,-1,10,9,-10,2,5,4,2,-5,10,7,-3,-9,2,6,-10,1,7,-3,6,-4,7,-10,-7,-9,6,-4,-10,6,1,-2,-8,-10,-2,9,-6,1,-4,-2,8,7,-7,5,-6,-9,-2,5,-5,-7,5,7,1,-9,-2,6,-4,6,-4,9,9,-6,-1,2,-5,3,7,5,9,-4,5,-1,-3,-10,-5,6,7,8,2,-1,9,8,5,3,-7,5,7,1,-2,-6,10,-4,5,-4,-1,3,-1,5,4,10,-7,3,10,5,-7,-8,4,-5,-1,5,5,2,-8,-4,9,4,-10,9,3,9,-4,8,-8,-6,-1,2,6,4,5,8,1,-7,1,10,-9,-5,-5,-2,3,5,-6,9,-3,7,10,-1,9,1,-5,3,9,8,8,-10,-7,-6,2,-6,-10,-4,-10,1,-4,-7,-3,-2,8,-8,-1,1,1,-10,5,-1,-10,-3,-9,-8,-7,1,-7,2,-4,-4,-7,2,4,-5,7,2,-1,6,1,5,8,8,9,-1,-10,-10,1,9,2,-4,9,6,3,4,-5,2,4,-1,9,8,8,-8,-9,-4,-8,10,6,-9,-8,-5,-1,8,-6,-10,10,4,-7,-9,-9,7,-1,7,5,-8,-1,9,7,-9,8,-8,9,-8,-6,5,8,-1,3,10,-5,2,-1,-8,-8,-3,-6,5,-5,-4,-8,4,-2,-8,-4,2,7,5,-5,-6,8,1,10,-1,-9,-4,3,6,3,-2,-4,-6,10,-9,-4,10,-2,-8,-7,7,-2,-4,9,4,-3,8,-3,-8,-8,8,10,6,8,-6,10,10,4,-1,-1,-4,-3,4,1,-7,-7,-10,2,10,-9,5,-2,3,7,1,-1,6,9,10,-10,-8,-1,-5,-4,4,-3,-5,4,-3,4,-10,-8,10,6,7,6,-4,-4,1,6,-3,4,8,-8,8,-4,8,7,-1,-8,9,-6,1,4,1,-7,2,2,7,10,3,-6,-6,-9,-5,9,-10,-9,-6,3,6,2,9,-6,6,-4,10,2,-2,-4,9,-3,10,-2,-6,4,4,7,-1,-2,1,-10,7,-8,2,-5,7,1,-9,-4,7,4,3,5,-8,-5,-2,-9,-6,7,1,10,-10,-5,-6,-4,4,-2,-3,5,3,-8,4,3,4,-9,-2,3,1,-2,5,-8,8,-10,-1,2,-4,9,10,9,2,1,8,-7,-1,4,7,-7,-5,7,1,-10,-10,2,-10,3,10,5,7,-4,1,4,-3,-4,-7,6,10,2,4,-7,-4,8,4,1,5,10,5,-5,-5,9,-2,10,1,-2,-6,3,1,6,-5,7,-2,6,-10,-10,-2,7,-3,3,-8,1,4,-4,5,10,-6,-10,5,10,8,2,-8,-1,-7,9,9,-1,-5,-10,6,-10,1,5,-5,3,4,3,-4,6,-9,9,4,5,-5,-10,4,-3,8,-1,2,8,9,1,6,-7,10,-6,-3,4,5,9,3,-4,-2,8,1,2,-7,-5,10,-1,5,-7,-8,10,-4,-3,-3,-10,4,-10,3,-6,5,-7,-1,-5,6,9,-2,5,8,-7,-7,-7,-4,-7,-9,1,-2,8,7,-4,-7,4,1,-9,9,9,2,6,-3,7,6,5,-6,-5,-10,3,9,-9,9,9,-4,4,6,-4,-5,-10,-8,-10,10,7,-2,9,8,-4,-6,4,5,7,-10,-2,-3,5,-9,-6,-10,-1,5,-8,10,1,6,5,5,-3,-5,9,9,-9,-9,-9,10,-3,-2,8,-4,-7,6,2,-5,6,1,-8,-9,9,6,9,10,10,5,-5,9,-9,-5,8,-5,-2,2,-7,8,1,5,-9,3,8,-1,9,6,-7,-9,3,-1,-10,-6,4,-4,10,-6,-6,-10,9,9,1,9,6,-5,4,3,-9,-3,-5,-9,-6,-3,3,9,5,3,-5,6,-10,2,8,-8,-6,-3,7,3,-6,10,-10,-5,-6,2,1,-5,-2,-7,-2,-1,-5,7,-6,-9,-9,-4,-7,5,-7,7,9,-3,6,-3,-4,-5,9,-2,4,-5,-2,1,8,-5,5,5,1,-6,7,-5,6,-9,-4,7,-4,-1,1,-6,-10,-6,-2,-10,8,-1,-9,-5,8,7,-4,-10,-9,7,-4,1,-5,-8,7,-9,6,-9,6,-10,-7,-8,3,3,10,-2,-4,-6,-7,5,4,8,-4,7,-2,-6,-5,-3,-2,-8,6,-5,-10,-9,-7,10,10,3,6,6,8,10,4,-10,10,9,8,6,6,7,-2,7,5,-6,2,3,-1,3,-4,4,-3,-10,6,10,-1,-7,4,-5,-6,3,2,-9,-7,-8,7,7,-4,2,-2,2,-1,-8,-5,-7,-3,-8,-4,-8,1,-4,-10,2,-7,-4,9,2,-6,-7,3,-1,-4,-1,-10,-1,-5,-1,7,8,8,-3,-9,8,-3,-8,9,-3,10,1,-3,1,7,-2,5,-8,-2,-9,6,-8,-4,-7,8,6,-4,-10,-1,-4,4,5,-5,-2,4,10,1,-8,6,10,5,-4,4,5,-6,4,-4,1,1,-6,7,4,-4,2,8,-6,9,2,-5,-9,-6,2,3,9,7,1,-9,-1,-7,-5,-7,10,10,-9,10,7,-10,-8,-2,-7,2,2,-2,4,-8,-6,7,-8,9,3,5,9,-9,-6,-6,2,10,-9,7,-2,2,7,-6,-8,4,8,3,5,-4,5,-6,8,-10,-8,10,-1,10,4,5,-2,-5,-10,-6,10,-8,2,1,1,8,-8,1,-1,-7,6,-8,5,-7,-4,2,4,9,5,9,9,7,-6,-7,7,3,-8,-2,-6,7,-1,-2,-8,-3,10,1,9,-9,6,9,1,-9,-3,-1,-7,9,-5,4,-3,-8,-9,4,-9,-3,10,8,-6,-10,7,9,8,-3,8,-8,-4,-4,7,3,1,-1,-9,-2,-8,-5,-4,9,10,-6,-7,9,-5,8,-9,10,-6,10,-1,-2,5,-6,-2,2,6,10,6,-7,-10,-5,-6,10,-7,1,3,9,-1,-8,9,-4,-1,8,-4,10,-2,7,-9,1,-5,4,-6,-7,-7,1,-8,10,-9,-7,-7,-1,2,-8,4,5,-4,9,-3,8,-3,7,-3,-1,9,-7,4,7,5,7,5,-9,4,-10,6,6,-4,-1,9,-9,-9,-5,6,3,5,1,3,-2,9,3,-9,-5,1,2,-7,8,-9,10,-3,7,2,-2,9], dtype = "int8")#candidate|8820|(2002,)|const|int8
call_8819 = relay.TupleGetItem(func_6947_call(relay.reshape(const_8820.astype('int8'), [14, 11, 13]), relay.reshape(const_8820.astype('int8'), [14, 11, 13]), ), 0)
call_8821 = relay.TupleGetItem(func_6950_call(relay.reshape(const_8820.astype('int8'), [14, 11, 13]), relay.reshape(const_8820.astype('int8'), [14, 11, 13]), ), 0)
func_6426_call = mod.get_global_var('func_6426')
func_6429_call = mutated_mod.get_global_var('func_6429')
const_8832 = relay.const([2.757828,5.128249,9.499994,-1.198587,8.053741,-9.628197,-9.879620,2.537846,0.009584,0.024112,5.293837,-7.386637,-3.774020,6.641024,9.863847,4.420341,1.743919,-6.678629,-1.152851,7.804121,-3.881999,6.137200,-1.810627,2.506829,-7.633540,-0.799671,-9.845484,0.448068,-7.558797,-6.714334,9.628365,-6.595452,-0.392070,5.746325,9.022162,-8.728906,-9.281450,-6.849319,-2.340265,-5.611982,4.982013,-8.080466,-2.510745,-0.668827,-2.151277,-9.172244,-3.915640,-0.541032,7.660464,8.296288,6.315638,-6.408522,-7.140467,-2.193892,-4.280879,8.390392,6.250548,0.811261,0.638865,-5.658596,5.386245,-9.877013,-4.765493,-1.725609,-9.264490,-4.822935,-7.041867,-3.942504,-1.020140,5.763238,2.487893,-1.046638,7.258714,-8.188547,9.503485,-6.783845,5.143684,3.806039,-9.648610,5.300410,0.924060,-3.195552,-0.803078,-2.949286,4.285836,-6.770391,1.730479,-3.989513,-1.283480,8.339234,6.447222,-1.802411,-1.118570,-2.628048,-2.665788,-6.315348,-4.308983,1.974577,4.297846,5.949809,2.167122,2.588001,-4.749757,6.517189,8.155045,-6.701716,9.897150,4.007620,-4.304124,-3.584769,-9.350825,1.206865,9.239503,0.520795,-6.738594,5.246696,-7.234031,-4.036022,-4.113162,-7.536283,9.593468,0.449906,0.027010,-4.176246,-8.029676,-2.207864,9.024238,1.649403,-7.981450,1.716577,1.385972,5.387954,-7.744438,-1.744084,2.904778,-9.765509,-4.880079,9.364001,-6.760869,1.047530,-3.725394,5.153115,6.270673,-6.077896], dtype = "float32")#candidate|8832|(144,)|const|float32
call_8831 = relay.TupleGetItem(func_6426_call(relay.reshape(const_8832.astype('float32'), [3, 6, 8])), 0)
call_8833 = relay.TupleGetItem(func_6429_call(relay.reshape(const_8832.astype('float32'), [3, 6, 8])), 0)
output = relay.Tuple([call_8808,call_8819,const_8820,call_8831,const_8832,])
output2 = relay.Tuple([call_8809,call_8821,const_8820,call_8833,const_8832,])
func_8834 = relay.Function([], output)
mod['func_8834'] = func_8834
mod = relay.transform.InferType()(mod)
mutated_mod['func_8834'] = func_8834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8834_call = mutated_mod.get_global_var('func_8834')
call_8835 = func_8834_call()
output = call_8835
func_8836 = relay.Function([], output)
mutated_mod['func_8836'] = func_8836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8239_call = mod.get_global_var('func_8239')
func_8241_call = mutated_mod.get_global_var('func_8241')
call_8872 = func_8239_call()
call_8873 = func_8239_call()
output = call_8872
output2 = call_8873
func_8889 = relay.Function([], output)
mod['func_8889'] = func_8889
mod = relay.transform.InferType()(mod)
output = func_8889()
func_8890 = relay.Function([], output)
mutated_mod['func_8890'] = func_8890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mod.get_global_var('func_8205')
func_8206_call = mutated_mod.get_global_var('func_8206')
call_8891 = relay.TupleGetItem(func_8205_call(), 0)
call_8892 = relay.TupleGetItem(func_8206_call(), 0)
output = relay.Tuple([call_8891,])
output2 = relay.Tuple([call_8892,])
func_8899 = relay.Function([], output)
mod['func_8899'] = func_8899
mod = relay.transform.InferType()(mod)
mutated_mod['func_8899'] = func_8899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8899_call = mutated_mod.get_global_var('func_8899')
call_8900 = func_8899_call()
output = call_8900
func_8901 = relay.Function([], output)
mutated_mod['func_8901'] = func_8901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8205_call = mod.get_global_var('func_8205')
func_8206_call = mutated_mod.get_global_var('func_8206')
call_8908 = relay.TupleGetItem(func_8205_call(), 0)
call_8909 = relay.TupleGetItem(func_8206_call(), 0)
const_8913 = relay.const([[[-10,9],[-10,-9],[1,-8],[9,-5]],[[-8,-7],[7,-10],[6,2],[6,1]],[[-6,-1],[7,7],[7,10],[-9,-7]],[[5,-9],[-3,-1],[-6,-8],[1,-10]],[[8,-5],[-5,-3],[-10,-10],[-6,-5]],[[2,-3],[3,-4],[7,1],[9,-6]],[[5,4],[-4,2],[-7,-4],[-9,4]]], dtype = "int32")#candidate|8913|(7, 4, 2)|const|int32
bop_8914 = relay.power(call_8908.astype('float64'), relay.reshape(const_8913.astype('float64'), relay.shape_of(call_8908))) # shape=(7, 4, 2)
bop_8917 = relay.power(call_8909.astype('float64'), relay.reshape(const_8913.astype('float64'), relay.shape_of(call_8909))) # shape=(7, 4, 2)
output = relay.Tuple([bop_8914,])
output2 = relay.Tuple([bop_8917,])
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
