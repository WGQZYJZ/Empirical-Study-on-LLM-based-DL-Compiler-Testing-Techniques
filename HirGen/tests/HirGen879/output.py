import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_546 = relay.var("var_546", dtype = "uint32", shape = ())#candidate|546|()|var|uint32
var_547 = relay.var("var_547", dtype = "uint32", shape = (1, 4))#candidate|547|(1, 4)|var|uint32
bop_548 = relay.maximum(var_546.astype('uint32'), var_547.astype('uint32')) # shape=(1, 4)
output = bop_548
output2 = bop_548
func_559 = relay.Function([var_546,var_547,], output)
mod['func_559'] = func_559
mod = relay.transform.InferType()(mod)
mutated_mod['func_559'] = func_559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_559_call = mutated_mod.get_global_var('func_559')
var_561 = relay.var("var_561", dtype = "uint32", shape = ())#candidate|561|()|var|uint32
var_562 = relay.var("var_562", dtype = "uint32", shape = (1, 4))#candidate|562|(1, 4)|var|uint32
call_560 = func_559_call(var_561,var_562,)
output = call_560
func_563 = relay.Function([var_561,var_562,], output)
mutated_mod['func_563'] = func_563
mutated_mod = relay.transform.InferType()(mutated_mod)
var_689 = relay.var("var_689", dtype = "uint32", shape = (15, 5, 1))#candidate|689|(15, 5, 1)|var|uint32
const_690 = relay.const([[[-9],[5],[5],[-4],[-9]],[[-5],[-7],[-4],[-7],[-7]],[[-9],[-4],[-2],[-6],[-8]],[[-6],[-9],[-10],[4],[-9]],[[-9],[9],[5],[4],[-4]],[[-7],[-2],[3],[-1],[-8]],[[3],[3],[-9],[-8],[9]],[[8],[-4],[-3],[10],[10]],[[-2],[8],[-7],[-7],[-1]],[[7],[-1],[8],[7],[2]],[[5],[-3],[-7],[-9],[8]],[[1],[-6],[2],[-2],[-4]],[[-4],[-7],[-3],[-4],[2]],[[6],[6],[-8],[8],[9]],[[5],[-5],[-1],[-6],[8]]], dtype = "uint32")#candidate|690|(15, 5, 1)|const|uint32
bop_691 = relay.bitwise_and(var_689.astype('uint32'), relay.reshape(const_690.astype('uint32'), relay.shape_of(var_689))) # shape=(15, 5, 1)
func_559_call = mod.get_global_var('func_559')
func_563_call = mutated_mod.get_global_var('func_563')
const_695 = relay.const(8, dtype = "uint32")#candidate|695|()|const|uint32
var_696 = relay.var("var_696", dtype = "uint32", shape = (4,))#candidate|696|(4,)|var|uint32
call_694 = func_559_call(relay.reshape(const_695.astype('uint32'), []), relay.reshape(var_696.astype('uint32'), [1, 4]), )
call_697 = func_559_call(relay.reshape(const_695.astype('uint32'), []), relay.reshape(var_696.astype('uint32'), [1, 4]), )
output = relay.Tuple([bop_691,call_694,const_695,var_696,])
output2 = relay.Tuple([bop_691,call_697,const_695,var_696,])
func_700 = relay.Function([var_689,var_696,], output)
mod['func_700'] = func_700
mod = relay.transform.InferType()(mod)
mutated_mod['func_700'] = func_700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_700_call = mutated_mod.get_global_var('func_700')
var_702 = relay.var("var_702", dtype = "uint32", shape = (15, 5, 1))#candidate|702|(15, 5, 1)|var|uint32
var_703 = relay.var("var_703", dtype = "uint32", shape = (4,))#candidate|703|(4,)|var|uint32
call_701 = func_700_call(var_702,var_703,)
output = call_701
func_704 = relay.Function([var_702,var_703,], output)
mutated_mod['func_704'] = func_704
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1023 = relay.var("var_1023", dtype = "uint64", shape = (14, 12, 8))#candidate|1023|(14, 12, 8)|var|uint64
const_1024 = relay.const([[[-7,6,2,-2,10,5,7,-10],[-7,-2,1,2,8,4,-10,-10],[9,-8,6,6,-4,-1,3,3],[6,-4,-5,-4,10,-10,10,9],[6,4,9,-9,-3,1,-2,7],[-2,-2,7,1,-7,10,-1,-9],[-6,10,-3,8,9,-3,8,6],[2,6,-7,-9,-9,10,-7,8],[1,1,-9,3,10,9,-5,7],[-7,9,1,-8,6,-2,-8,10],[-10,-5,-10,9,4,8,-6,-9],[8,-7,-3,-1,3,-5,4,10]],[[4,5,6,6,3,-9,8,4],[-3,7,7,8,1,-1,-7,-9],[10,7,-7,4,-6,10,1,10],[-6,2,6,3,1,4,-7,-1],[6,-3,-10,6,-1,9,-10,-6],[9,8,-5,-7,-5,4,-4,2],[-2,5,-3,-9,-7,8,1,-4],[1,-10,-4,-3,-5,-4,-4,1],[1,-2,-8,3,-3,-3,-5,7],[-2,2,-3,7,-6,9,9,-7],[-5,-7,2,-8,-10,-1,1,-1],[-6,-1,10,7,10,5,5,10]],[[-5,-4,-8,3,-5,-5,4,-9],[10,9,7,5,3,7,-6,-9],[3,-7,8,-10,-6,-7,-2,-3],[6,4,10,-1,1,-3,4,-7],[7,-9,-6,6,-6,4,-1,2],[-9,-3,6,-1,1,-6,-6,-5],[9,-8,4,10,-8,10,3,9],[10,10,5,5,-7,-2,-5,8],[10,10,-1,-6,5,10,-9,10],[10,-7,5,-10,4,7,-10,3],[2,-4,4,-2,5,8,3,-3],[-2,-8,2,-9,-2,6,-3,2]],[[2,8,5,6,-4,-5,-2,9],[-9,-1,7,-7,-8,10,2,9],[-7,2,9,-3,-2,-1,7,8],[-9,6,1,-4,8,2,-8,-8],[10,-9,7,5,2,-4,9,6],[-3,5,-8,4,-5,-10,9,-7],[5,9,10,1,-1,-3,-1,8],[3,-7,-2,-9,-9,-7,-6,-7],[-2,4,10,6,-2,-2,9,-6],[-3,5,6,-2,4,1,-6,10],[-7,-2,2,10,10,-9,-2,-1],[-10,10,-2,-10,2,6,-2,-7]],[[-3,-9,8,8,-1,-7,4,10],[6,-1,-4,5,-4,5,-7,6],[3,4,-5,7,1,-3,-2,10],[-4,-6,-2,6,2,-2,6,-1],[-5,10,9,-8,-3,-7,5,-5],[-6,9,4,4,9,-8,-7,-5],[4,-2,5,3,-4,-5,8,10],[-2,4,6,-3,5,1,-10,4],[-4,-9,10,-6,-2,3,-2,-6],[4,10,9,7,5,-5,6,1],[6,8,-9,10,7,5,-6,4],[10,-4,-7,2,2,-9,7,-10]],[[-7,8,-5,9,-2,3,-7,10],[1,8,-6,2,-8,-6,-8,-7],[-5,10,3,-3,-6,-5,-5,10],[-10,6,9,-3,6,3,6,-8],[4,2,-9,-4,-3,-8,3,-6],[8,-8,7,-5,3,-8,7,9],[-4,-3,-7,-10,6,-1,-7,2],[7,4,3,9,-9,-2,-3,-10],[-5,-1,-7,-5,8,2,2,-3],[-3,-7,8,10,-2,-4,7,-3],[-4,-5,3,4,5,-9,9,10],[-10,-10,-2,6,5,9,3,-4]],[[-4,9,-8,-1,10,-4,9,-3],[-10,7,-5,3,6,-4,4,7],[-9,-7,1,2,5,2,-9,-5],[10,-8,-9,-5,-5,-4,-8,-6],[7,-4,1,-2,1,2,-1,-8],[1,7,6,-2,2,-9,7,5],[-1,4,4,-10,-2,-4,9,5],[5,7,4,4,7,4,9,10],[10,-3,10,9,6,-4,-3,-5],[10,2,3,-10,9,4,7,1],[-8,10,-8,1,-10,6,-3,-4],[3,9,-3,-6,-4,4,6,9]],[[-10,1,7,9,-6,-5,-8,-6],[-6,-6,-3,-5,5,-10,-5,-5],[7,-10,-10,4,-5,-7,-7,-3],[7,3,-4,-8,-8,-9,7,-7],[-2,9,-7,7,1,5,8,-2],[-7,-6,-3,-9,-5,3,6,8],[-8,-9,-1,5,4,-1,-7,-5],[10,-5,-6,-6,-5,-4,-1,-1],[9,-2,-8,-4,6,-3,10,7],[-1,-3,-7,9,7,4,-6,-7],[-5,-3,7,-5,3,-7,-10,-3],[5,10,-6,-5,-4,3,2,-3]],[[8,-9,-5,9,4,3,8,-7],[-3,-6,-5,1,10,7,3,-10],[-8,-5,5,1,10,5,1,3],[-6,2,-2,3,7,7,-2,1],[7,-4,-10,2,-10,-7,9,-6],[1,-8,-1,8,-5,-7,1,8],[4,10,7,-3,1,8,2,-4],[-2,-9,-5,10,-3,6,5,-1],[6,-2,-5,9,-8,3,3,-4],[-10,-7,-1,5,-5,7,-5,-6],[4,-3,4,-5,9,2,-7,-6],[-3,-4,-3,8,9,6,6,6]],[[-2,8,-9,8,-3,1,-9,1],[-1,6,-3,1,-10,10,3,-5],[-3,10,-6,-1,1,10,-8,-3],[5,4,-4,4,6,-1,7,3],[-6,1,3,2,-3,-5,-3,-9],[-10,8,10,9,3,-4,-3,-10],[1,-3,-5,-10,7,-7,-8,1],[-1,-1,3,6,9,8,-8,4],[-4,-6,2,-7,-5,-3,3,8],[-5,7,-10,-5,5,-2,-4,2],[5,-6,6,-8,-8,-2,5,6],[-1,-9,8,-2,7,-5,2,8]],[[-7,-4,8,4,3,10,7,1],[1,-9,-3,-1,6,-5,7,-8],[10,9,-6,-5,-8,10,-10,-3],[10,-9,4,-5,-10,-3,-6,3],[-4,3,3,10,10,9,10,1],[6,5,4,2,-10,10,5,1],[4,-9,9,-2,-1,1,3,-3],[5,-8,-8,2,-5,-6,-6,10],[-1,10,-10,1,3,5,7,4],[-4,1,-3,1,-5,-8,2,-2],[-1,-4,-7,4,-8,-8,7,-9],[4,-4,-2,5,-10,10,-5,6]],[[7,6,-5,-3,-9,8,-3,-8],[6,4,-5,-7,3,8,10,-3],[1,2,-10,-9,-8,-7,-3,-7],[-7,6,1,-6,1,-4,7,9],[-5,-4,-7,-5,9,5,-7,2],[7,-5,-1,5,-6,-4,-6,-8],[3,-7,-4,-7,-4,-6,7,6],[-8,-4,-3,-1,-10,1,8,-7],[3,5,-6,-2,-5,3,8,7],[2,5,10,6,2,6,-7,3],[8,-7,8,-7,2,4,1,6],[-3,-3,-8,5,-6,-10,-7,-5]],[[10,-9,3,-3,8,-5,-1,4],[-5,-8,-8,2,7,9,6,-9],[5,-7,4,3,7,10,-2,-1],[5,-9,6,9,5,7,3,10],[-4,8,4,9,-1,9,-7,-10],[2,5,5,1,-1,3,-4,2],[7,7,1,-3,7,10,4,6],[1,4,-5,-8,-3,10,2,-5],[-2,-2,-8,-7,-7,-3,-9,7],[-2,8,5,-4,4,6,-6,7],[-3,10,4,-10,-6,-3,4,7],[-10,3,-8,4,1,-10,-10,4]],[[7,-9,-3,5,-2,6,-10,-1],[-7,-8,1,1,-1,-10,9,6],[-8,-1,4,4,-6,-3,3,-7],[-10,7,6,-5,10,-9,9,-7],[8,10,5,7,4,6,-4,10],[-9,-5,-7,-3,8,-8,-7,4],[4,-7,-9,8,6,3,-10,-6],[-1,7,3,-7,-2,-8,9,-6],[7,3,10,1,7,8,8,8],[6,9,5,-10,2,-8,1,5],[-7,-6,-10,-5,-5,-8,-6,4],[2,-3,1,6,3,-4,9,-2]]], dtype = "uint64")#candidate|1024|(14, 12, 8)|const|uint64
bop_1025 = relay.bitwise_xor(var_1023.astype('uint64'), relay.reshape(const_1024.astype('uint64'), relay.shape_of(var_1023))) # shape=(14, 12, 8)
func_559_call = mod.get_global_var('func_559')
func_563_call = mutated_mod.get_global_var('func_563')
var_1040 = relay.var("var_1040", dtype = "uint32", shape = ())#candidate|1040|()|var|uint32
const_1041 = relay.const([-6,6,10,-6], dtype = "uint32")#candidate|1041|(4,)|const|uint32
call_1039 = func_559_call(relay.reshape(var_1040.astype('uint32'), []), relay.reshape(const_1041.astype('uint32'), [1, 4]), )
call_1042 = func_559_call(relay.reshape(var_1040.astype('uint32'), []), relay.reshape(const_1041.astype('uint32'), [1, 4]), )
output = relay.Tuple([bop_1025,call_1039,var_1040,const_1041,])
output2 = relay.Tuple([bop_1025,call_1042,var_1040,const_1041,])
func_1044 = relay.Function([var_1023,var_1040,], output)
mod['func_1044'] = func_1044
mod = relay.transform.InferType()(mod)
var_1045 = relay.var("var_1045", dtype = "uint64", shape = (14, 12, 8))#candidate|1045|(14, 12, 8)|var|uint64
var_1046 = relay.var("var_1046", dtype = "uint32", shape = ())#candidate|1046|()|var|uint32
output = func_1044(var_1045,var_1046,)
func_1047 = relay.Function([var_1045,var_1046,], output)
mutated_mod['func_1047'] = func_1047
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1721 = relay.var("var_1721", dtype = "float64", shape = (13, 16, 7))#candidate|1721|(13, 16, 7)|var|float64
uop_1722 = relay.atan(var_1721.astype('float64')) # shape=(13, 16, 7)
func_700_call = mod.get_global_var('func_700')
func_704_call = mutated_mod.get_global_var('func_704')
var_1729 = relay.var("var_1729", dtype = "uint32", shape = (75,))#candidate|1729|(75,)|var|uint32
const_1730 = relay.const([[10,-10],[-10,-6]], dtype = "uint32")#candidate|1730|(2, 2)|const|uint32
call_1728 = relay.TupleGetItem(func_700_call(relay.reshape(var_1729.astype('uint32'), [15, 5, 1]), relay.reshape(const_1730.astype('uint32'), [4,]), ), 1)
call_1731 = relay.TupleGetItem(func_704_call(relay.reshape(var_1729.astype('uint32'), [15, 5, 1]), relay.reshape(const_1730.astype('uint32'), [4,]), ), 1)
func_559_call = mod.get_global_var('func_559')
func_563_call = mutated_mod.get_global_var('func_563')
var_1743 = relay.var("var_1743", dtype = "uint32", shape = ())#candidate|1743|()|var|uint32
call_1742 = func_559_call(relay.reshape(var_1743.astype('uint32'), []), relay.reshape(const_1730.astype('uint32'), [1, 4]), )
call_1744 = func_559_call(relay.reshape(var_1743.astype('uint32'), []), relay.reshape(const_1730.astype('uint32'), [1, 4]), )
output = relay.Tuple([uop_1722,call_1728,var_1729,const_1730,call_1742,var_1743,])
output2 = relay.Tuple([uop_1722,call_1731,var_1729,const_1730,call_1744,var_1743,])
func_1748 = relay.Function([var_1721,var_1729,var_1743,], output)
mod['func_1748'] = func_1748
mod = relay.transform.InferType()(mod)
mutated_mod['func_1748'] = func_1748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1748_call = mutated_mod.get_global_var('func_1748')
var_1750 = relay.var("var_1750", dtype = "float64", shape = (13, 16, 7))#candidate|1750|(13, 16, 7)|var|float64
var_1751 = relay.var("var_1751", dtype = "uint32", shape = (75,))#candidate|1751|(75,)|var|uint32
var_1752 = relay.var("var_1752", dtype = "uint32", shape = ())#candidate|1752|()|var|uint32
call_1749 = func_1748_call(var_1750,var_1751,var_1752,)
output = call_1749
func_1753 = relay.Function([var_1750,var_1751,var_1752,], output)
mutated_mod['func_1753'] = func_1753
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1805 = relay.var("var_1805", dtype = "int64", shape = (15, 11, 11))#candidate|1805|(15, 11, 11)|var|int64
var_1806 = relay.var("var_1806", dtype = "int64", shape = (15, 11, 11))#candidate|1806|(15, 11, 11)|var|int64
bop_1807 = relay.greater_equal(var_1805.astype('bool'), relay.reshape(var_1806.astype('bool'), relay.shape_of(var_1805))) # shape=(15, 11, 11)
output = bop_1807
output2 = bop_1807
func_1811 = relay.Function([var_1805,var_1806,], output)
mod['func_1811'] = func_1811
mod = relay.transform.InferType()(mod)
mutated_mod['func_1811'] = func_1811
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1811_call = mutated_mod.get_global_var('func_1811')
var_1813 = relay.var("var_1813", dtype = "int64", shape = (15, 11, 11))#candidate|1813|(15, 11, 11)|var|int64
var_1814 = relay.var("var_1814", dtype = "int64", shape = (15, 11, 11))#candidate|1814|(15, 11, 11)|var|int64
call_1812 = func_1811_call(var_1813,var_1814,)
output = call_1812
func_1815 = relay.Function([var_1813,var_1814,], output)
mutated_mod['func_1815'] = func_1815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2288 = relay.var("var_2288", dtype = "int16", shape = (9, 6, 16))#candidate|2288|(9, 6, 16)|var|int16
const_2289 = relay.const([[[-9,-4,-1,-1,-8,-10,-2,9,-1,7,4,10,3,-3,9,7],[-10,-1,4,6,3,-2,4,-10,-10,2,-2,-9,-2,-2,-2,-9],[3,-3,-9,8,-2,10,4,3,-8,8,-9,5,-9,2,-7,4],[-10,5,-8,5,3,-8,-5,3,-7,-3,9,-10,6,-10,5,-1],[2,6,10,10,7,2,-10,-7,-5,-7,-10,-3,-9,7,6,10],[-5,10,8,-9,-9,-8,6,-9,-6,5,1,10,8,5,7,-6]],[[4,8,-5,6,7,-6,-9,-4,-9,-9,-7,-4,10,1,-7,-10],[2,-2,4,-2,1,-4,2,5,6,-6,7,-10,-9,4,9,-6],[1,-9,-7,-8,10,1,1,-5,-10,-10,3,3,2,-10,9,-1],[6,-9,-2,1,8,-3,-8,8,1,6,-9,-6,4,1,1,-8],[-1,-10,-4,4,-7,-1,-9,-4,8,-6,6,-5,7,-8,7,9],[-10,10,2,-6,-2,3,-7,-4,6,9,2,-4,1,1,-5,5]],[[-9,-1,-10,1,5,5,-10,4,-7,-8,8,-7,-4,-6,-7,6],[7,-9,4,1,6,9,3,4,8,-8,-5,-7,3,10,6,10],[-5,2,-10,7,9,4,3,1,-1,2,-5,-9,-4,-10,6,6],[8,-1,1,4,7,-1,7,2,4,-6,-2,-7,3,-9,-7,2],[-2,-4,2,4,-8,-10,8,1,-7,-1,1,7,5,-4,-10,-8],[9,5,9,-1,-6,-2,-4,-8,-1,9,-7,7,-10,-4,5,-3]],[[3,-6,-9,1,-7,-10,5,1,7,7,8,-7,5,9,3,-4],[1,-1,6,-6,5,7,7,6,-10,9,-9,6,-6,-3,8,7],[7,10,10,-10,5,4,7,-6,-5,5,-1,-7,8,8,-7,-5],[-3,-10,2,-7,-7,-9,-3,1,9,-1,9,-7,-7,-2,10,-7],[-2,-7,8,3,4,-10,-8,4,-9,8,-2,4,2,2,-3,6],[-7,-4,-6,10,1,-7,-5,6,8,3,-1,-9,-4,6,1,5]],[[-4,3,-5,7,7,5,-7,-5,7,4,4,2,4,5,9,-5],[8,10,-5,9,5,1,7,6,3,-5,-5,6,6,-7,1,7],[-4,-5,7,10,-10,-5,-6,-2,-3,7,-5,-9,4,5,10,7],[10,-2,5,-1,2,3,-7,8,-3,9,-9,8,-4,3,4,7],[-3,3,10,5,9,1,-5,7,-5,-6,5,-2,-5,-3,6,-5],[9,-10,-1,3,5,8,-3,9,-3,6,9,5,2,4,-7,10]],[[-6,-9,7,9,-5,1,-3,-8,5,2,-2,9,6,4,2,-1],[6,5,1,-3,-10,6,7,10,8,8,-1,-3,-8,-2,3,-9],[3,-10,10,3,-10,-5,-1,-10,7,8,-5,-4,-8,-3,10,-9],[8,9,5,-9,-1,5,-9,10,5,3,8,10,4,8,7,-8],[9,4,9,10,-10,-1,-1,7,10,-3,9,-6,-1,8,-2,-5],[-6,-4,4,5,10,-7,1,-7,5,-1,5,9,2,4,-6,4]],[[9,6,-3,-9,1,5,9,-2,2,-9,3,-1,-7,-6,3,6],[-7,5,-5,6,-2,7,1,-6,-7,9,4,2,4,-6,-9,1],[7,7,-2,-10,-3,8,10,-8,10,4,7,7,3,2,-8,-7],[9,-8,8,7,-7,-5,8,4,9,4,-4,-1,2,1,4,-6],[-4,6,-4,-3,-10,10,10,-8,1,-8,10,-4,-3,-4,-4,2],[5,-10,-2,10,1,-2,3,3,1,-1,-1,5,9,-10,2,-1]],[[-1,5,-5,-7,-4,-9,-8,-3,2,-10,-8,-6,6,9,8,-4],[2,4,4,-6,-8,-7,7,-5,-3,-3,-2,9,-5,-4,10,-1],[7,4,7,-2,-4,3,-1,2,7,-9,4,-7,-6,-3,-10,1],[-2,-9,-4,5,-1,1,9,10,-9,-5,6,-4,-2,9,3,-9],[6,3,-8,7,-7,5,-2,-1,3,5,-7,-2,-6,-1,2,4],[-8,5,3,9,-10,5,-9,-4,4,4,10,2,-4,7,-5,-3]],[[7,-10,9,2,4,-5,6,7,-9,-1,4,5,6,-5,2,-3],[5,-9,3,-8,-9,-1,-2,-2,1,2,-7,-5,-8,2,-10,8],[8,-2,9,9,-4,-2,3,7,-9,9,-5,-7,-7,-4,-5,2],[2,-6,5,10,10,-6,-7,-4,4,-2,-10,-6,9,-3,4,10],[3,-8,3,-8,9,-3,6,3,-3,-1,-4,-9,6,-9,-1,-8],[-3,3,-6,9,6,2,-1,4,-9,-6,-1,-8,-1,7,6,-6]]], dtype = "int16")#candidate|2289|(9, 6, 16)|const|int16
bop_2290 = relay.minimum(var_2288.astype('int16'), relay.reshape(const_2289.astype('int16'), relay.shape_of(var_2288))) # shape=(9, 6, 16)
output = bop_2290
output2 = bop_2290
func_2296 = relay.Function([var_2288,], output)
mod['func_2296'] = func_2296
mod = relay.transform.InferType()(mod)
var_2297 = relay.var("var_2297", dtype = "int16", shape = (9, 6, 16))#candidate|2297|(9, 6, 16)|var|int16
output = func_2296(var_2297)
func_2298 = relay.Function([var_2297], output)
mutated_mod['func_2298'] = func_2298
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2318 = relay.var("var_2318", dtype = "int32", shape = (8, 12, 11))#candidate|2318|(8, 12, 11)|var|int32
const_2319 = relay.const([[[-3,10,-5,5,1,-1,-8,-1,-3,6,-2],[2,-9,-8,10,-5,-7,10,-3,5,-7,-9],[1,1,-2,8,9,-2,6,3,10,-9,-2],[-8,-2,-1,7,-3,9,6,1,5,-2,10],[1,-6,-1,7,-5,-10,-7,-5,2,5,-2],[-5,5,-2,-9,6,6,-10,-10,2,-1,10],[5,4,-5,-1,2,-9,5,3,-4,5,-5],[-8,-1,8,-5,10,8,-1,3,-2,-7,-1],[2,10,6,-7,10,6,8,-5,-4,4,9],[5,-7,-10,-7,1,-6,7,-6,-5,-2,8],[-4,-2,8,-10,-1,-2,1,-7,2,8,-8],[-1,1,-3,-6,-10,3,-9,-10,-1,-6,-3]],[[6,5,-7,9,-2,-2,-8,-6,3,7,10],[1,6,10,7,-9,3,-5,1,-6,4,-3],[-10,-9,5,-2,-1,-4,7,9,9,-8,-3],[3,-7,-4,8,3,8,-2,7,7,-9,5],[7,1,-3,8,-4,-8,1,-1,-9,8,8],[10,6,-3,10,-10,-3,1,-9,-10,2,-3],[-9,-4,9,-8,2,2,7,10,5,-2,-2],[-4,6,4,-3,-2,1,5,-6,9,-2,5],[-8,7,-6,2,6,8,2,-9,-1,9,5],[-6,-6,-10,-5,10,-1,-7,-9,-4,6,8],[-6,-5,8,-2,8,5,-2,6,1,1,6],[8,8,2,-5,-2,-7,-9,2,7,9,6]],[[8,-9,10,10,9,-1,1,-10,4,-7,-10],[-6,-10,-2,7,-8,-2,6,6,-7,-6,-9],[4,3,-3,10,9,-4,1,5,6,6,2],[-9,10,1,-4,2,2,-7,8,-8,3,7],[10,3,7,3,3,-8,-7,8,-1,-1,-8],[10,4,-4,-2,3,4,9,7,-3,-3,1],[9,-5,-10,7,-5,-5,-7,-7,1,-4,-6],[-8,-6,-1,-9,-10,2,1,2,-9,7,5],[4,-6,2,9,2,10,8,6,4,8,-1],[-7,8,-9,1,-10,8,9,7,-7,-7,6],[6,5,-10,-5,3,-6,-9,10,9,-6,-8],[-6,-5,4,9,7,2,7,-6,-2,6,2]],[[3,7,1,-10,10,-4,10,-7,5,-4,8],[10,-4,3,-2,-7,-6,-8,10,6,5,-5],[7,6,5,-1,-1,-7,5,7,4,2,-8],[6,10,8,-3,4,2,-2,-8,-4,-5,-6],[-2,10,8,-5,-6,-4,5,4,4,8,8],[7,-4,-6,1,-3,-6,-8,-7,-3,-5,9],[-9,-8,3,-1,5,-6,8,-1,-6,1,-7],[10,-3,7,10,-8,1,3,1,4,1,-6],[-3,-7,1,-3,-8,-4,-4,9,-9,4,-10],[-3,-1,8,6,-3,2,8,-2,2,5,-1],[9,4,4,7,5,6,6,9,7,-2,4],[2,2,3,2,-8,-3,-8,-8,-2,4,8]],[[9,3,-9,-5,-5,-8,3,-6,-7,-5,-5],[-7,7,-8,7,-2,-5,-4,-9,9,6,-5],[-9,3,5,6,10,-5,-5,9,-10,10,-5],[2,-3,-2,-6,-9,7,-3,-1,-2,-6,-9],[1,5,-8,-9,-1,-9,-9,5,-7,4,-8],[6,-10,8,7,-9,5,2,-10,8,-1,6],[-7,9,7,10,2,3,-8,6,-10,6,10],[1,-8,-1,-8,-10,2,-1,-1,-2,-8,-3],[-8,2,5,-7,7,-6,9,-5,-8,1,2],[-7,-2,-8,-6,7,-1,3,-10,-4,8,-1],[7,3,-10,-5,6,-7,-3,-9,5,4,-6],[5,-9,2,-7,6,10,1,-4,2,8,-8]],[[-4,9,-4,7,-2,-7,-9,8,-1,-4,-4],[1,-1,9,4,-10,6,-8,-4,4,7,-5],[-10,4,9,-4,-3,2,10,5,1,-4,9],[-9,7,7,5,-10,-8,6,-2,-8,-5,-1],[2,-1,-3,9,-9,5,4,-1,7,-3,6],[10,-10,-5,9,-2,-1,-5,9,8,-4,5],[-4,-8,8,4,1,-3,2,-7,-3,-5,3],[-1,-4,10,2,8,2,9,-7,5,6,-8],[6,-3,-4,7,8,10,9,-4,7,-8,-9],[-8,-9,4,-9,-6,-10,7,-9,1,-2,-3],[-3,1,8,9,-6,4,8,-1,-2,5,7],[-6,-6,-6,-10,-9,-4,4,-2,9,-10,1]],[[3,-8,-8,7,-6,-2,1,-1,6,7,4],[2,-4,2,-6,-5,-5,-3,5,8,4,4],[-7,8,8,-3,-7,-8,10,9,5,6,-7],[4,-9,-3,-4,8,-3,5,2,-4,5,-1],[4,-2,4,-10,6,-2,6,-8,4,2,-4],[1,-6,-6,8,7,-9,-10,4,-3,4,5],[-3,-10,3,-4,-10,-5,-1,9,-8,1,5],[2,3,-10,-1,9,-2,-10,-3,-1,9,-1],[-5,-10,-9,2,-6,3,-10,-8,-8,6,8],[-4,-2,7,-9,4,1,8,-6,-3,-7,-4],[9,-1,-3,-6,4,-3,5,8,10,-9,-7],[-2,9,7,-2,-2,-5,8,1,8,-6,-2]],[[2,-4,-3,5,9,-2,5,-4,-8,-9,-1],[-10,3,-8,10,-1,-1,7,9,3,-3,6],[-2,-6,9,5,4,-2,5,7,1,10,-2],[-5,10,9,-1,-1,7,3,-3,-6,6,-4],[-8,-6,9,-1,2,-2,-4,-6,-9,-7,-4],[-2,1,-6,6,7,10,-2,-7,10,9,-2],[6,-7,4,-1,6,-9,-3,-5,-4,-10,-4],[-5,-5,10,8,4,-9,1,7,-4,-7,-10],[-8,7,5,-10,2,-2,10,-1,-6,-6,-8],[-10,9,7,-9,-6,2,-10,-5,-8,6,3],[1,-8,-1,-2,9,3,8,-6,7,-3,-9],[5,-3,-10,10,7,-9,8,9,-10,-4,8]]], dtype = "int32")#candidate|2319|(8, 12, 11)|const|int32
bop_2320 = relay.subtract(var_2318.astype('int32'), relay.reshape(const_2319.astype('int32'), relay.shape_of(var_2318))) # shape=(8, 12, 11)
func_1748_call = mod.get_global_var('func_1748')
func_1753_call = mutated_mod.get_global_var('func_1753')
var_2333 = relay.var("var_2333", dtype = "float64", shape = (1456,))#candidate|2333|(1456,)|var|float64
const_2334 = relay.const([[-1,5,6,-3,-10,7,7,-2,-9,2,6,8,-7,6,6,-9,9,-6,-3,-9,-6,-3,-8,-9,1,-9,-7,4,-9,-1,8,-1,6,-10,-8,6,-7,-8,5,10,-1,10,5,-4,-4,-1,-7,-9,-2,5,-10,-8,9,2,5,9,-2,-6,5,-3,-4,-1,-7,-5,-9,-2,1,-8,8,-4,3,-9,-2,-1,-4]], dtype = "uint32")#candidate|2334|(1, 75)|const|uint32
var_2335 = relay.var("var_2335", dtype = "uint32", shape = ())#candidate|2335|()|var|uint32
call_2332 = relay.TupleGetItem(func_1748_call(relay.reshape(var_2333.astype('float64'), [13, 16, 7]), relay.reshape(const_2334.astype('uint32'), [75,]), relay.reshape(var_2335.astype('uint32'), []), ), 3)
call_2336 = relay.TupleGetItem(func_1753_call(relay.reshape(var_2333.astype('float64'), [13, 16, 7]), relay.reshape(const_2334.astype('uint32'), [75,]), relay.reshape(var_2335.astype('uint32'), []), ), 3)
func_1811_call = mod.get_global_var('func_1811')
func_1815_call = mutated_mod.get_global_var('func_1815')
const_2342 = relay.const([-6,-2,-4,-7,-1,3,-1,6,-5,-2,2,-7,-2,5,4,9,-6,6,-3,2,-4,-9,7,6,2,-3,9,7,2,7,7,-3,-7,2,5,-4,-6,5,-8,-7,1,5,1,-9,5,8,-4,-4,1,-2,7,-5,-9,-8,3,9,7,-4,-5,1,1,-1,-10,7,-10,-10,-5,10,7,-2,5,-4,5,-1,1,10,3,8,-6,-7,-5,3,-1,-5,3,9,-9,10,-1,4,-5,5,-8,3,9,10,6,4,-8,-6,-8,-9,-9,3,-4,-3,3,-8,2,-5,-1,5,-8,-5,-9,7,9,4,-9,-10,-6,-1,-3,-10,-2,6,-7,1,1,2,-10,-9,7,6,10,8,-3,5,-7,10,7,3,10,-3,-3,-3,6,-1,-5,10,5,3,6,-3,-2,-4,-3,-5,4,-4,-3,-9,8,3,-7,1,10,9,2,8,-6,-3,1,2,7,2,4,10,-1,5,7,-9,2,10,-1,7,3,8,9,-9,7,-8,-3,3,3,-2,-6,5,1,1,8,-3,8,-6,3,-5,7,1,2,-5,-4,5,-8,-7,8,4,7,-6,9,4,-7,4,2,5,-1,-1,7,-4,-6,7,10,9,-7,2,7,1,5,-10,-3,3,5,-9,-9,9,-4,9,-8,-1,5,4,-1,6,10,-3,10,9,9,10,-10,3,-7,-10,-3,1,-4,2,10,1,3,-7,1,10,3,-8,-3,7,-3,7,7,6,5,-9,7,6,-6,-4,-6,-9,-6,-4,-7,-1,9,10,7,7,5,4,-8,1,3,2,-8,10,7,-5,4,-7,-3,7,5,10,2,10,-6,5,-4,9,-8,-8,-1,-1,10,-6,-7,2,10,9,-10,3,8,5,5,-6,3,7,-10,8,6,-2,8,-2,10,2,10,7,-3,2,8,-10,5,-4,-4,4,8,-1,-1,-7,-4,-4,6,2,6,9,3,5,-5,-2,3,8,-1,-10,-4,7,7,4,-3,-5,2,2,-3,3,6,-8,-3,-2,7,-1,10,1,-9,3,3,10,-1,-1,9,-2,-1,-6,7,1,2,7,9,-9,4,2,-9,-3,5,5,-7,-1,-7,5,6,8,-7,10,-4,6,-3,5,9,2,-1,-9,6,-9,8,-7,-9,4,1,-3,5,2,6,-9,7,-10,-2,7,9,-1,9,1,4,-7,9,1,-9,-1,-2,9,-6,8,-8,-6,-10,-3,-6,10,-10,-6,-6,5,1,8,8,3,-8,4,5,-2,6,7,-10,3,-1,-10,-5,2,-1,-9,10,5,-4,-2,10,5,1,-9,8,-2,-10,-8,7,10,10,9,5,6,6,8,3,-1,5,7,1,-2,2,-7,-10,1,8,10,5,-3,-7,6,-6,6,8,-7,-1,-1,1,-5,6,-2,7,10,-9,4,5,8,8,5,7,6,-10,-2,6,-1,5,-9,-5,-4,-1,4,8,-7,6,-2,-3,1,-5,4,2,4,-9,8,1,2,-10,-9,-8,3,-8,7,1,-5,-4,-8,6,-4,4,-1,-5,4,-9,2,-9,3,1,-3,1,1,-8,-2,10,9,7,6,5,7,-4,3,-7,-5,10,1,5,-5,-10,7,-2,-5,-8,-2,2,9,10,3,10,-6,-3,10,-8,3,1,-9,6,-1,-6,7,4,-5,-8,2,6,6,4,9,2,-9,2,5,1,-2,1,-4,-5,-9,-9,9,-8,5,3,-1,8,10,-9,9,3,6,3,6,1,9,6,-5,6,-6,6,6,9,-5,10,-8,-5,4,-4,-6,-6,5,4,4,-10,9,-8,-1,10,5,9,-1,-8,4,5,-9,4,3,-5,-10,-9,-4,-5,-6,-10,4,-4,6,10,-6,-2,6,-10,-6,5,-4,6,-1,-3,-5,-8,2,2,4,2,6,6,9,-10,2,2,2,-4,-6,-2,7,10,1,-1,-3,-8,4,3,-9,10,-10,7,-8,-7,-5,-9,-8,-6,-10,-8,10,4,-10,-9,1,10,2,5,8,8,2,10,4,-1,-4,9,-4,10,-1,-3,-8,6,-10,-2,7,-6,7,9,3,-8,-2,1,-4,-10,-9,9,-7,9,-10,-10,1,3,3,1,-5,-4,-8,3,-7,-6,7,6,-2,1,-8,-6,6,-6,3,-6,-8,5,7,-5,2,-3,-7,-5,3,-1,-9,-9,8,6,5,-2,-4,9,9,-8,-7,2,-7,5,4,-3,2,-10,9,4,9,9,4,-7,-3,-4,3,4,-2,1,4,-9,-6,-9,-4,-3,6,8,-9,3,-7,2,-2,1,-5,1,8,10,-8,1,9,-7,-7,6,-10,-9,5,-1,8,-2,6,-6,3,8,-2,-7,4,-7,1,-6,4,1,7,-10,-4,9,6,-4,-9,10,5,4,3,2,-9,-6,6,-4,-9,-7,7,-7,-1,-9,5,-6,1,2,3,8,2,5,-1,-10,-5,5,5,2,3,10,5,10,6,-9,-6,1,9,6,6,2,5,3,9,7,1,4,3,-1,6,8,-7,1,-2,5,5,9,-5,9,10,-10,3,-6,-7,-5,-6,-6,9,-8,4,-3,3,8,-6,3,-5,6,6,6,8,-6,-4,9,10,8,-3,5,-3,-3,2,-5,-3,-4,-3,-2,-4,9,-3,-3,6,-10,-2,-4,-10,6,-6,-8,3,8,2,1,10,-4,-8,9,10,-2,6,9,-6,-7,-7,-1,-5,-8,-9,-5,-7,-4,-7,9,-4,-2,-1,-4,8,-9,-4,-7,9,10,-4,-1,-5,8,-9,9,-9,4,2,5,9,6,6,6,9,-7,10,-6,2,7,8,-7,-9,-7,8,2,7,1,-1,1,3,-5,-4,8,-2,9,2,-10,-6,-1,-10,2,-1,3,1,6,-9,-7,-1,-3,3,-4,10,4,-1,-2,10,-10,-6,4,6,1,10,-2,-6,-5,-7,-2,5,4,-4,8,-8,-2,-1,4,-8,-5,-5,-9,-10,-8,3,5,-9,-3,3,5,-10,-6,5,8,-4,-2,-10,10,5,-8,-9,6,9,-8,-1,-4,2,-1,1,-2,4,4,5,5,-1,8,-5,-7,-6,-9,-10,9,6,-10,-1,1,-6,-9,-8,-1,-7,-10,-5,-9,4,9,4,7,-10,-6,-1,6,4,10,-10,-1,-2,-9,8,10,-9,-7,7,-2,2,7,5,-3,-1,-10,-6,5,-4,8,6,3,7,6,-3,-2,-6,-8,-4,-9,6,5,-10,3,-7,-5,9,6,-7,1,-3,-5,-3,10,-6,4,8,-5,10,-2,8,-9,7,-2,-2,-4,-5,-5,-2,8,6,9,9,-4,-1,-7,-6,-6,6,5,9,4,-8,2,2,9,10,-1,3,2,-2,3,-7,-10,6,-2,5,-9,-3,-7,9,-4,-4,-9,-10,1,10,-1,4,2,7,5,8,-8,-4,-5,-9,-3,-3,1,3,-9,-7,-4,2,-1,9,-2,9,-7,3,6,-2,8,-1,-1,1,9,-10,9,8,10,5,4,2,-6,5,10,9,5,4,-4,5,3,8,-5,3,6,9,-3,-3,-7,-9,8,-4,-9,10,-3,7,-8,9,3,-3,9,9,3,1,2,9,-9,4,1,-9,9,-2,3,2,-3,-5,5,4,-5,9,4,-9,1,1,7,10,-10,-3,-6,-10,-10,-1,8,4,-2,-3,3,9,7,-7,2,2,-2,6,2,6,1,-8,7,-4,-8,-3,-1,4,4,6,-1,-7,-5,-10,9,10,5,8,-3,1,1,2,-8,-4,10,-10,10,3,-10,-4,-10,8,-6,9,1,1,-4,6,7,-6,-9,9,4,5,-6,-5,-5,6,-3,9,5,-6,2,2,-1,8,3,-7,9,2,-3,4,2,-7,4,-7,-7,9,6,-9,-10,-4,4,1,-7,9,-8,6,-4,4,-3,1,3,-9,3,-5,5,-7,5,2,-9,-10,7,-8,2,-1,3,5,3,-7,2,-9,-1,7,4,-8,2,3,-5,-10,-3,2,-4,3,10,4,-2,-10,9,9,-7,-8,6,-6,-2,-7,-9,2,5,1,-3,-9,9,-8,-7,4,5,-2,-3,3,5,2,-1,7,10,-3,-4,8,4,-2,2,-4,9,-9,4,-10,1,3,8,10,-10,1,-7,-7,-2,9,-6,2,-9,-8,2,-2,-1,7,-6,7,9,-10,-4,5,-10,1,-9,1,-5,-3,-8,2,-1,-1,3,1,-6,8,1,-10,-10,-7,6,-1,9,-10,8,-6,-10,-5,7,-4,-8,6,8,10,-7,-10,-7,5,-4,2,-6,2,7,8,-3,8,-9,-3,-10,-6,2,-1,-9,-6,3,7,-10,5,6,3,10,-3,6,5,-10,5,8,-2,2,10,-8,5,5,5,-5,-3,10,3,3,-3,8,-5,-2,3,-5,-1,7,-10,8,-6,-4,10,-4,-1,1,-9,10,5,-1,7,-1,-10,4,1,-7,-7,-5,-4,-9,7,7,-9,10,-10,-4,10,7,4,-1,-5,1,7,8,6,-6,-9,6,1,-6,8,10,-5,-9,-8,5,7,5,3,-7,5,9,8,2,5,2,9,-3,-7,-5,-1,8,6,3,-1,8,4,7,-7,3,8,7,-5,2,-1,9,-7,1,2,-3,-4,6,2,-2,-4,-1,10,2,8,-9,2,2,-5,-3,9,-10,8,-3,-9,9,9,8,8,5,5,-5,-2,-6,-2,-3,-6,-5,7,5,2,1,-6,1,2,-1,9,-6,5,-7,-3,-9,3,1,2,8,-2,5,10,3,3,-9,-10,-5,-8,-1,5,8,-5,-8,7,-3,4,8,-6,-8,-4,3,-3,-6,-3,10], dtype = "int64")#candidate|2342|(1815,)|const|int64
call_2341 = func_1811_call(relay.reshape(const_2342.astype('int64'), [15, 11, 11]), relay.reshape(const_2342.astype('int64'), [15, 11, 11]), )
call_2343 = func_1811_call(relay.reshape(const_2342.astype('int64'), [15, 11, 11]), relay.reshape(const_2342.astype('int64'), [15, 11, 11]), )
func_1044_call = mod.get_global_var('func_1044')
func_1047_call = mutated_mod.get_global_var('func_1047')
const_2360 = relay.const([[-6,8,-3,2,-2,-7,5,5,7,2,7,-9,10,9,-5,-10,3,-4,9,-8,1,1,9,5,10,-1,7,-10,-7,10,1,-4,-10,-5,-2,-1,8,-10,8,1,3,6,4,-7,-4,3,-7,-2,-5,5,9,2,-7,-2,-8,-4,-7,-10,-6,-3,4,-8,5,9,8,-7,1,4,-2,5,-1,10,9,2,7,-8,5,5,5,-10,-9,9,8,9,4,-9,-7,5,-9,3,-4,8,-4,-9,-6,-3,-6,4,-8,6,-1,6,-6,-3,-10,2,5,3,-10,10,9,-10,8,3,-10,-7,-5,-8,6,7,-8,-1,-6,4,-5,3,-10,3,8,-3,4,-9,4,2,-1,-9,-6,3,3,10,-6,3,6,3,3,-4,7,-8,5,5,6,6,-2,-4,10,4,6,1,5,-10,9,5,-9,9,10,-9,-5,8,6,4,-5,2,-6,-5,-5,9,-9,2,-7,4,-4,-6,8,8,-6,-1,-3,-4,4,-1,-6,-4,7,5,-8,3,-1,-3,-3,-4,7,3,6,8,9,-10,-2,-10,-2,-6,3,4,-10,-3,-2,-5,-2,-7,-8,-8,-8,1,-5,-10,-9,9,8,4,-4,1,5,3,4,6,8,-8,2,-6,-4,6,-5,-5,-10,-10,-7,-10,-7,-8,4,-5,-7,9,-4,-8,3,10,-9,-2,-6,-3,5,3,-6,-5,6,5,2,-7,-10,3,-9,5,9,-6,10,-8,-5,-7,4,3,1,-7,3,9,9,1,6,5,-3,-10,2,-10,-1,-8,-8,-6,1,3,-5,1,4,-1,8,-6,7,-8,6,-6,4,1,-6,-2,-10,3,9,1,-6,4,8,-8,7,-6,1,-1,7,-6,1,-10,-5,10,6,7,-4,7,2,7,-1,-4,6,-5,1,5,-3,5,-9,4,-6,9,-2,4,-4,-3,5,-7,-7,1,6,-10,-3,7,-1,9,-1,-9,-7,-7,3,5,-9,8,-5,-4,7,9,8,-3,-8,8,1,10,-10,10,-9,3,7,4,2,-4,9,-10,3,7,6,-9,-3,-4,8,-8,10,4,5,-1,5,8,3,2,1,-7,3,3,-9,-10,-2,-5,-2,-2,-7,3,-10,-6,9,1,5,9,6,-7,1,-3,8,7,-6,-6,-2,5,-2,-9,8,2,-7,-3,-3,1,8,8,1,5,-6,10,-9,-2,-7,1,10,-9,2,-4,-2,10,-7,5,8,5,8,2,4,10,4,5,5,-2,7,6,1,9,-6,7,-4,-6,10,2,3,-3,5,2,5,-1,-2,-10,-2,-10,-5,2,9,-2,9,3,7,-8,8,-4,-6,3,-1,10,6,-4,6,8,6,-4,-3,-7,-7,-1,-7,-7,-10,-2,7,-4,9,-2,6,10,-10,-8,-3,3,10,-6,9,-3,-6,-9,4,-6,3,-7,9,-10,-2,-2,-1,-7,-9,1,6,8,-6,7,-2,2,2,-4,-7,-8,1,5,4,-7,5,-10,4,5,7,-2,4,4,-5,6,1,10,3,7,7,10,-4,3,8,-7,-9,-4,5,10,6,-4,10,-10,1,-10,-1,-10,-1,-2,2,-6,2,-5,-7,9,-3,-10,-6,5,8,-8,8,-6,1,-9,-9,4,-4,8,-8,-7,-9,3,7,-5,-5,-8,10,-1,-3,-6,5,6,2,1,1,8,-4,7,9,10,6,-7,1,-9,-6,7,-4,-1,6,-6,-1,-9,7,10,-8,2,-8,10,4,-6,-4,-2,-5,-7,-6,-10,-7,-3,4,10,6,8,10,-5,-9,5,-3,4,-3,-1,-1,-7,9,-3,-3,-9,-7,-3,8,1,9,1,-4,-10,-3,5,1,2,-2,-6,-10,-4,-3,1,-6,-9,8,-7,-2,-1,-7,10,-8,9,-9,-5,-8,-5,-7,-4,-1,-10,-10,5,-3,10,-3,-7,3,1,8,3,6,-9,-6,-7,-4,8,-3,10,9,3,8,-3,3,5,1,-7,7,1,9,-2,7,10,3,6,-8,4,-9,9,2,-5,-3,9,10,-5,7,5,7,4,3,-2,8,-7,4,1,9,6,-10,-1,-2,-1,-2,-5,-10,-9,-2,4,-8,9,4,-5,-5,4,-7,-6,-9,-9,3,-2,-6,6,5,-8,-8,4,-6,-4,1,8,2,6,-3,6,3,-7,-10,-7,-4,7,-3,-5,-9,3,8,9,-7,3,2,-4,-7,3,5,-2,6,-10,-10,9,-5,-1,-4,-2,5,-1,-5,3,-7,1,8,-10,3,-5,-8,-2,7,-5,-4,-3,4,-6,-8,-3,5,6,9,10,-9,-5,-3,9,10,2,3,-3,-9,6,-7,-2,-4,8,6,5,6,2,7,-9,5,1,9,5,-2,-5,1,-3,-8,10,10,-1,5,6,-9,1,8,-4,-3,-3,9,5,-9,-6,-9,3,2,-8,1,1,10,-4,1,3,6,-10,-8,-6,3,-4,-10,6,2,3,9,-5,-5,7,-6,1,-10,6,7,-5,-8,7,-7,-2,-4,-4,8,-3,-8,-8,-3,-6,-3,9,6,2,-4,-4,9,-1,10,9,-7,-10,1,9,8,-6,-2,10,-10,4,1,-4,1,-7,-3,10,7,6,7,-3,-3,-5,-4,4,7,-10,3,3,1,8,6,-5,7,2,-9,8,-6,8,8,-5,-10,-3,1,1,-6,8,-7,5,-6,-6,6,6,7,-3,8,9,-5,2,-10,7,-2,-8,-8,10,3,-7,-2,-2,-9,-3,5,6,4,-3,1,-10,5,-1,-4,4,-9,-6,-6,-1,3,3,-5,7,6,-6,10,-1,8,7,-5,9,2,6,-6,-2,-2,-7,3,-8,4,8,-4,10,-1,3,-7,-1,-8,4,5,-2,-2,-3,3,-6,9,-2,10,-2,8,-8,-8,2,7,9,-6,10,2,-5,-7,1,-2,7,-4,5,-6,6,2,-1,8,3,-3,-1,6,-7,6,9,2,2,-8,-7,-1,-10,5,-4,-1,6,-9,6,-5,-2,-2,1,-8,-9,1,3,-1,7,-2,8,9,5,10,-5,8,-6,-8,-4,1,7,1,3,10,-9,-2,-6,-10,-9,6,-5,-3,5,-9,2,-4,9,-6,9,-4,-10,5,7,1,-6,-2,-1,2,-8,9,-9,8,10,4,-2,10,-5,10,-10,10,9,-7,-8,-8,-9,6,-10,8,8,1,-10,-2,6,9,-2,-10,-10,3,5,4,-8,2,7,-10,-3,5,-2,8,-10,1,-5,-4,7,1,-9,-8,9,7,-1,1,9,-7,4,6,2,5,-10,10,-4,-1,-10,-2,-8,-5,7,3,1,-7,-5,8,-2,-7,-1,2,-10,8,2,10,-8,-1,10,-1,3,-7,-2,-8,-7,-5,-1,-4,9,-4,-4,3,7,9,7,10,9,-8,2,3,10,8,6,4,-5,-8,-1,3,4,-7,3,1,-5,-2,5,-8,5,8,-9,-9,-1,5,8,1,-9,3,8,-1,2,-1,9,4,9,-7,4,-5,3,-6,8,-4,-10,9,2,-10,-5,3,-4,10,-9,-4,-5,8,10,10,5,-7,5,-10,7,-1,-5,-10,1,2,9,3,-4,-1,-6]], dtype = "uint64")#candidate|2360|(1, 1344)|const|uint64
call_2359 = relay.TupleGetItem(func_1044_call(relay.reshape(const_2360.astype('uint64'), [14, 12, 8]), relay.reshape(var_2335.astype('uint32'), []), ), 3)
call_2361 = relay.TupleGetItem(func_1047_call(relay.reshape(const_2360.astype('uint64'), [14, 12, 8]), relay.reshape(var_2335.astype('uint32'), []), ), 3)
func_1748_call = mod.get_global_var('func_1748')
func_1753_call = mutated_mod.get_global_var('func_1753')
call_2362 = relay.TupleGetItem(func_1748_call(relay.reshape(var_2333.astype('float64'), [13, 16, 7]), relay.reshape(const_2334.astype('uint32'), [75,]), relay.reshape(var_2335.astype('uint32'), []), ), 5)
call_2363 = relay.TupleGetItem(func_1753_call(relay.reshape(var_2333.astype('float64'), [13, 16, 7]), relay.reshape(const_2334.astype('uint32'), [75,]), relay.reshape(var_2335.astype('uint32'), []), ), 5)
func_700_call = mod.get_global_var('func_700')
func_704_call = mutated_mod.get_global_var('func_704')
call_2365 = relay.TupleGetItem(func_700_call(relay.reshape(const_2334.astype('uint32'), [15, 5, 1]), relay.reshape(call_2332.astype('uint32'), [4,]), ), 1)
call_2366 = relay.TupleGetItem(func_704_call(relay.reshape(const_2334.astype('uint32'), [15, 5, 1]), relay.reshape(call_2332.astype('uint32'), [4,]), ), 1)
output = relay.Tuple([bop_2320,call_2332,var_2333,const_2334,var_2335,call_2341,const_2342,call_2359,const_2360,call_2362,call_2365,])
output2 = relay.Tuple([bop_2320,call_2336,var_2333,const_2334,var_2335,call_2343,const_2342,call_2361,const_2360,call_2363,call_2366,])
func_2367 = relay.Function([var_2318,var_2333,var_2335,], output)
mod['func_2367'] = func_2367
mod = relay.transform.InferType()(mod)
var_2368 = relay.var("var_2368", dtype = "int32", shape = (8, 12, 11))#candidate|2368|(8, 12, 11)|var|int32
var_2369 = relay.var("var_2369", dtype = "float64", shape = (1456,))#candidate|2369|(1456,)|var|float64
var_2370 = relay.var("var_2370", dtype = "uint32", shape = ())#candidate|2370|()|var|uint32
output = func_2367(var_2368,var_2369,var_2370,)
func_2371 = relay.Function([var_2368,var_2369,var_2370,], output)
mutated_mod['func_2371'] = func_2371
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2413 = relay.var("var_2413", dtype = "float64", shape = (7, 5, 1))#candidate|2413|(7, 5, 1)|var|float64
uop_2414 = relay.cos(var_2413.astype('float64')) # shape=(7, 5, 1)
output = relay.Tuple([uop_2414,])
output2 = relay.Tuple([uop_2414,])
func_2431 = relay.Function([var_2413,], output)
mod['func_2431'] = func_2431
mod = relay.transform.InferType()(mod)
mutated_mod['func_2431'] = func_2431
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2432 = relay.var("var_2432", dtype = "float64", shape = (7, 5, 1))#candidate|2432|(7, 5, 1)|var|float64
func_2431_call = mutated_mod.get_global_var('func_2431')
call_2433 = func_2431_call(var_2432)
output = call_2433
func_2434 = relay.Function([var_2432], output)
mutated_mod['func_2434'] = func_2434
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2531 = relay.const([[[-10],[-5],[5],[6],[-1],[2],[7]]], dtype = "uint8")#candidate|2531|(1, 7, 1)|const|uint8
var_2532 = relay.var("var_2532", dtype = "uint8", shape = (13, 7, 16))#candidate|2532|(13, 7, 16)|var|uint8
bop_2533 = relay.minimum(const_2531.astype('uint8'), var_2532.astype('uint8')) # shape=(13, 7, 16)
func_1044_call = mod.get_global_var('func_1044')
func_1047_call = mutated_mod.get_global_var('func_1047')
var_2545 = relay.var("var_2545", dtype = "uint64", shape = (672, 2))#candidate|2545|(672, 2)|var|uint64
const_2546 = relay.const(-7, dtype = "uint32")#candidate|2546|()|const|uint32
call_2544 = relay.TupleGetItem(func_1044_call(relay.reshape(var_2545.astype('uint64'), [14, 12, 8]), relay.reshape(const_2546.astype('uint32'), []), ), 0)
call_2547 = relay.TupleGetItem(func_1047_call(relay.reshape(var_2545.astype('uint64'), [14, 12, 8]), relay.reshape(const_2546.astype('uint32'), []), ), 0)
func_2431_call = mod.get_global_var('func_2431')
func_2434_call = mutated_mod.get_global_var('func_2434')
const_2554 = relay.const([-7.145578,-3.399643,-8.117499,-3.145569,0.397679,-5.903737,6.424379,-1.846806,1.179515,-5.660540,-3.247249,0.215623,3.651687,-5.884266,-0.466149,-2.995439,3.963623,-8.196801,-1.666420,1.164924,-7.166840,2.820993,9.557566,9.045531,-7.173751,7.447652,-4.721441,6.653026,-5.082347,-1.044735,5.687352,-9.091278,5.929763,-1.974727,3.441687], dtype = "float64")#candidate|2554|(35,)|const|float64
call_2553 = relay.TupleGetItem(func_2431_call(relay.reshape(const_2554.astype('float64'), [7, 5, 1])), 0)
call_2555 = relay.TupleGetItem(func_2434_call(relay.reshape(const_2554.astype('float64'), [7, 5, 1])), 0)
var_2558 = relay.var("var_2558", dtype = "float64", shape = (7, 5, 4))#candidate|2558|(7, 5, 4)|var|float64
bop_2559 = relay.logical_and(call_2553.astype('bool'), var_2558.astype('bool')) # shape=(7, 5, 4)
bop_2562 = relay.logical_and(call_2555.astype('bool'), var_2558.astype('bool')) # shape=(7, 5, 4)
output = relay.Tuple([bop_2533,call_2544,var_2545,const_2546,const_2554,bop_2559,])
output2 = relay.Tuple([bop_2533,call_2547,var_2545,const_2546,const_2554,bop_2562,])
func_2563 = relay.Function([var_2532,var_2545,var_2558,], output)
mod['func_2563'] = func_2563
mod = relay.transform.InferType()(mod)
var_2564 = relay.var("var_2564", dtype = "uint8", shape = (13, 7, 16))#candidate|2564|(13, 7, 16)|var|uint8
var_2565 = relay.var("var_2565", dtype = "uint64", shape = (672, 2))#candidate|2565|(672, 2)|var|uint64
var_2566 = relay.var("var_2566", dtype = "float64", shape = (7, 5, 4))#candidate|2566|(7, 5, 4)|var|float64
output = func_2563(var_2564,var_2565,var_2566,)
func_2567 = relay.Function([var_2564,var_2565,var_2566,], output)
mutated_mod['func_2567'] = func_2567
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3082 = relay.var("var_3082", dtype = "float64", shape = (15, 3, 10))#candidate|3082|(15, 3, 10)|var|float64
uop_3083 = relay.erf(var_3082.astype('float64')) # shape=(15, 3, 10)
output = uop_3083
output2 = uop_3083
func_3087 = relay.Function([var_3082,], output)
mod['func_3087'] = func_3087
mod = relay.transform.InferType()(mod)
var_3088 = relay.var("var_3088", dtype = "float64", shape = (15, 3, 10))#candidate|3088|(15, 3, 10)|var|float64
output = func_3087(var_3088)
func_3089 = relay.Function([var_3088], output)
mutated_mod['func_3089'] = func_3089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3352 = relay.var("var_3352", dtype = "float64", shape = (1, 15, 8))#candidate|3352|(1, 15, 8)|var|float64
uop_3353 = relay.tan(var_3352.astype('float64')) # shape=(1, 15, 8)
uop_3369 = relay.erf(uop_3353.astype('float32')) # shape=(1, 15, 8)
output = relay.Tuple([uop_3369,])
output2 = relay.Tuple([uop_3369,])
func_3372 = relay.Function([var_3352,], output)
mod['func_3372'] = func_3372
mod = relay.transform.InferType()(mod)
var_3373 = relay.var("var_3373", dtype = "float64", shape = (1, 15, 8))#candidate|3373|(1, 15, 8)|var|float64
output = func_3372(var_3373)
func_3374 = relay.Function([var_3373], output)
mutated_mod['func_3374'] = func_3374
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3609 = relay.var("var_3609", dtype = "bool", shape = ())#candidate|3609|()|var|bool
const_3610 = relay.const([[[False,False,True,True,False,True,True,True,True],[False,True,False,False,False,True,False,True,False],[False,True,True,False,True,False,True,True,True],[True,False,True,True,False,True,False,True,True],[False,False,False,True,True,True,True,True,False],[False,False,True,True,False,True,False,False,False],[False,True,True,True,False,True,False,True,True],[True,False,False,True,False,False,True,True,True],[True,True,True,True,True,True,False,False,True],[True,False,True,True,False,True,False,True,True],[True,True,True,False,True,True,False,False,True],[True,True,False,False,False,True,True,True,True],[False,False,True,True,True,False,True,True,False],[False,True,False,True,True,True,False,True,False]],[[True,False,False,False,True,False,True,True,False],[False,True,False,True,True,False,True,True,True],[True,False,False,True,False,False,True,True,True],[True,False,False,True,True,False,False,False,True],[False,True,True,False,True,False,False,True,True],[False,False,False,False,True,False,False,False,False],[False,False,False,True,True,False,False,False,True],[False,False,True,False,False,False,True,True,False],[True,True,True,False,False,True,True,False,False],[True,False,False,False,True,False,False,False,True],[False,False,False,True,True,False,True,True,True],[True,False,False,True,True,True,False,True,True],[True,False,True,True,False,False,False,False,True],[False,False,True,False,False,False,False,True,True]],[[False,False,False,True,False,False,True,True,True],[True,False,False,False,True,True,False,True,True],[False,True,True,True,True,True,False,True,True],[False,True,False,True,False,True,True,True,True],[True,True,False,False,False,False,True,False,False],[False,False,True,True,False,False,False,True,True],[True,False,True,False,False,False,False,False,False],[True,True,False,False,True,True,True,True,True],[True,False,True,True,False,False,False,True,False],[False,True,False,False,False,False,True,False,False],[True,True,False,False,False,False,False,True,True],[True,False,False,False,True,True,True,True,True],[True,True,True,False,False,False,False,False,True],[False,True,True,False,False,False,True,False,True]],[[True,False,False,False,True,False,False,True,True],[True,True,False,True,False,False,False,False,False],[False,False,False,True,False,True,True,True,True],[True,False,False,False,True,False,False,True,False],[False,True,True,False,True,False,False,False,True],[False,False,True,False,False,False,False,False,False],[True,True,True,True,False,True,True,True,False],[True,True,True,True,False,True,True,False,False],[True,False,False,False,True,False,False,True,False],[False,False,False,False,True,True,False,False,False],[True,True,True,False,True,False,True,False,False],[False,True,False,False,True,True,False,True,False],[False,True,True,True,True,True,True,False,True],[True,False,True,True,True,True,False,True,False]],[[False,True,False,True,True,False,True,False,True],[False,False,False,False,True,False,False,False,True],[True,True,True,False,False,True,False,True,True],[True,True,False,True,False,True,True,True,True],[True,False,True,False,True,True,True,True,False],[True,True,False,False,True,False,False,True,False],[True,True,False,False,False,True,True,True,True],[False,True,False,True,False,True,False,True,False],[False,False,True,False,True,True,True,True,False],[True,True,True,True,True,True,True,True,True],[True,False,True,False,True,False,True,False,False],[False,True,True,False,True,True,True,True,False],[False,False,False,False,True,True,False,True,False],[True,False,False,False,True,False,True,False,True]],[[True,True,False,False,True,True,True,True,False],[True,False,True,True,True,False,True,True,True],[True,True,False,True,False,True,True,True,False],[False,False,False,True,False,True,True,False,False],[False,True,True,False,False,False,False,False,True],[False,True,False,True,False,False,False,False,False],[True,True,True,True,True,False,False,True,False],[True,False,False,False,True,True,True,True,False],[True,True,False,False,True,True,True,True,False],[True,True,False,True,False,True,True,True,True],[True,True,False,True,True,False,True,True,True],[False,False,True,False,False,False,False,False,False],[False,True,True,False,False,False,False,False,False],[True,True,True,False,False,True,False,True,False]],[[True,False,True,False,False,True,True,True,True],[False,True,False,False,True,True,True,True,False],[True,True,False,True,True,True,False,True,True],[True,False,False,True,True,False,False,True,False],[False,True,True,True,True,True,True,True,False],[True,False,False,True,True,True,True,False,False],[False,False,False,True,False,False,True,True,True],[True,False,False,True,False,True,True,True,False],[False,True,True,False,False,True,False,True,False],[False,False,False,False,False,True,False,True,True],[False,False,False,True,True,False,False,False,False],[True,True,False,False,True,True,True,False,True],[True,False,False,True,False,False,False,True,False],[True,True,True,False,False,True,False,True,False]],[[True,True,False,True,True,False,True,True,True],[False,False,True,True,True,False,True,True,False],[True,True,True,True,False,True,False,False,True],[True,False,False,True,True,False,False,True,True],[False,False,False,True,True,False,True,False,False],[True,False,True,True,True,False,True,True,False],[False,True,False,True,True,False,True,False,False],[True,False,True,False,False,True,False,False,False],[True,True,True,True,False,True,False,True,False],[False,False,True,False,False,True,False,True,False],[False,True,False,False,False,True,True,True,True],[True,True,True,True,False,False,False,True,False],[True,True,False,False,True,False,True,True,True],[False,True,False,False,False,True,True,False,False]],[[False,False,True,True,True,False,True,False,True],[True,True,False,False,False,False,False,False,True],[False,False,True,True,False,False,False,True,False],[True,False,True,True,False,True,False,True,False],[True,False,False,False,False,True,False,False,False],[False,False,False,False,False,False,True,False,True],[True,False,False,False,True,False,True,True,False],[False,True,True,False,False,False,False,False,False],[False,True,False,False,True,False,False,True,False],[True,False,False,False,False,False,False,False,False],[False,True,True,False,True,False,True,True,True],[True,True,True,True,True,False,True,True,False],[True,False,True,False,True,False,False,True,False],[True,True,False,True,True,True,False,True,False]],[[False,False,True,True,False,False,True,True,False],[True,True,True,True,False,True,True,False,False],[True,True,True,True,False,False,True,True,True],[False,True,False,False,True,True,True,True,True],[True,False,False,True,True,True,True,True,False],[False,False,False,True,True,True,False,False,True],[True,True,False,False,True,True,True,True,True],[False,False,False,True,True,False,True,True,True],[True,False,False,True,False,False,True,True,True],[True,False,True,False,True,False,True,True,True],[False,False,False,True,False,False,True,True,False],[True,True,True,True,False,True,True,True,True],[False,False,True,True,True,True,True,False,False],[True,True,True,True,True,False,True,True,False]],[[False,False,False,False,False,True,True,True,True],[False,False,False,True,False,False,False,False,False],[True,True,False,True,False,True,True,True,False],[True,True,True,True,True,False,True,True,False],[False,False,True,True,False,True,True,True,False],[False,False,False,False,True,True,False,True,True],[True,False,True,True,True,False,True,False,True],[True,False,False,True,False,False,False,False,False],[True,True,True,True,True,True,True,True,True],[False,True,False,False,False,False,True,False,True],[True,True,True,False,False,True,False,True,False],[False,True,False,False,False,True,True,False,True],[True,True,False,False,False,False,False,False,False],[False,True,False,True,False,True,False,False,True]],[[False,False,False,False,False,True,False,False,False],[True,True,False,False,False,True,True,False,True],[True,False,True,True,False,False,False,True,False],[True,False,False,True,False,False,True,False,False],[True,False,False,True,True,False,True,False,False],[False,True,True,False,False,True,True,True,False],[False,True,True,False,True,True,True,False,True],[True,True,True,False,False,True,False,True,True],[False,False,True,True,True,False,False,True,False],[True,False,True,True,False,True,True,True,False],[False,False,False,False,True,True,True,True,False],[True,False,True,False,False,False,True,True,True],[True,True,False,True,True,False,False,False,True],[True,True,False,True,False,False,True,False,True]],[[True,True,True,True,False,True,False,False,True],[False,True,True,True,False,False,True,True,True],[False,False,False,True,True,True,True,True,True],[True,False,True,False,True,True,True,False,True],[False,True,False,False,True,True,True,True,False],[True,False,True,True,False,True,True,True,True],[False,False,False,False,True,False,True,False,False],[False,True,False,False,False,True,False,False,True],[True,True,False,True,False,False,True,True,True],[False,False,False,True,True,True,True,True,False],[False,False,False,False,True,False,False,True,False],[False,True,False,True,False,True,True,False,True],[True,True,True,False,True,True,True,True,False],[False,False,True,False,False,False,True,False,True]]], dtype = "bool")#candidate|3610|(13, 14, 9)|const|bool
bop_3611 = relay.logical_or(var_3609.astype('bool'), const_3610.astype('bool')) # shape=(13, 14, 9)
output = relay.Tuple([bop_3611,])
output2 = relay.Tuple([bop_3611,])
func_3630 = relay.Function([var_3609,], output)
mod['func_3630'] = func_3630
mod = relay.transform.InferType()(mod)
mutated_mod['func_3630'] = func_3630
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3631 = relay.var("var_3631", dtype = "bool", shape = ())#candidate|3631|()|var|bool
func_3630_call = mutated_mod.get_global_var('func_3630')
call_3632 = func_3630_call(var_3631)
output = call_3632
func_3633 = relay.Function([var_3631], output)
mutated_mod['func_3633'] = func_3633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3972 = relay.var("var_3972", dtype = "float32", shape = (5, 10, 8))#candidate|3972|(5, 10, 8)|var|float32
uop_3973 = relay.sigmoid(var_3972.astype('float32')) # shape=(5, 10, 8)
output = relay.Tuple([uop_3973,])
output2 = relay.Tuple([uop_3973,])
func_3981 = relay.Function([var_3972,], output)
mod['func_3981'] = func_3981
mod = relay.transform.InferType()(mod)
mutated_mod['func_3981'] = func_3981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3982 = relay.var("var_3982", dtype = "float32", shape = (5, 10, 8))#candidate|3982|(5, 10, 8)|var|float32
func_3981_call = mutated_mod.get_global_var('func_3981')
call_3983 = func_3981_call(var_3982)
output = call_3983
func_3984 = relay.Function([var_3982], output)
mutated_mod['func_3984'] = func_3984
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4407 = relay.const([[[7.781636,2.353306,0.660657,-2.550495,0.271899,9.284942,2.410676,3.892425,-6.455516,6.168730,-6.124635,8.778203,5.284609],[-3.889147,-0.444210,1.093013,-4.222002,-9.374218,3.857415,-0.645455,2.525424,-4.588302,-0.170510,-9.642995,8.740317,7.067797],[4.266579,3.318612,-3.283420,-7.796278,5.079526,-7.031006,-6.849570,0.374973,8.445927,9.068559,3.445454,-6.355231,7.338943],[-0.395262,-4.448101,-3.098710,-9.756176,-2.088761,8.822432,3.316235,-5.040854,6.041029,4.371510,8.766530,-5.740613,4.687929],[-2.920492,2.556878,4.962694,-9.791471,9.547559,5.746179,-0.515191,-0.262711,-0.800656,-2.912952,0.596089,-5.566065,-0.088436]],[[-4.637117,-4.574273,-0.316423,7.443295,-6.618892,5.799706,-4.207265,-5.721489,1.869749,2.182369,-4.296126,2.209996,1.687537],[-7.232256,9.350187,3.682024,8.706803,-9.291475,-9.715401,8.387766,-2.530522,9.778275,-0.497894,-5.511679,2.497374,6.163127],[-9.664000,-5.507409,-4.560736,4.432391,-7.597736,4.124022,-8.171129,7.175569,8.225604,0.493024,-2.081275,-1.969830,-0.724348],[-8.262521,-0.137727,-1.564605,-8.598107,-4.739170,0.880038,6.516781,-8.977288,-3.525967,-7.586145,7.824133,-2.383402,8.978854],[-8.315679,6.662334,-9.912812,-3.263418,-3.864728,6.235014,3.688569,3.657367,1.652512,-8.502180,9.244592,-2.429583,1.500060]],[[4.241304,1.063339,-1.359764,-5.564896,-3.786177,1.653570,7.785052,8.345150,-8.432633,9.883754,-6.782952,-5.816802,-6.686683],[6.689109,6.282760,8.739425,-9.426384,3.428450,-9.024221,8.853814,5.192299,1.839291,-4.245967,7.419682,6.731597,-2.634839],[-6.631484,7.867450,-9.966302,6.703062,8.379051,-8.457692,0.930129,-4.686812,6.917656,7.887079,-4.586480,9.386870,5.992403],[7.873106,2.179096,-0.167816,9.207877,5.671397,-3.255482,3.428452,0.993781,-2.412655,-4.715444,-5.843920,-9.324505,-7.758823],[-7.288690,2.999445,-7.744093,-7.958791,-9.142753,6.534700,-0.436953,9.228721,-3.709455,-1.567991,-5.903090,-3.160814,6.257137]],[[-5.877093,-3.368401,-2.824820,-0.187684,2.253434,5.605985,7.818881,-8.222373,3.168813,1.116283,-9.345449,3.341761,7.383358],[2.522941,-6.384084,-5.016493,-1.100026,0.848952,5.402788,-2.233868,3.222387,-8.558427,2.588080,4.242703,-0.778797,8.404618],[-1.514828,1.296039,-1.838828,-8.715597,-5.047403,1.898846,1.592247,1.024097,-2.383465,8.904906,1.768413,-6.791834,3.766658],[2.115112,-3.239104,-2.770870,-9.099448,-4.340638,-1.061437,1.652499,7.190706,6.563896,-8.256309,0.196269,-9.644324,-2.901594],[2.975822,-0.533080,-8.875628,-5.460860,-2.986759,-8.586915,-2.104384,1.409658,0.311765,5.165998,8.809103,5.786579,-7.141041]],[[-0.010236,-0.249843,-8.070170,-4.847982,-4.032388,4.205120,1.669211,6.934159,-4.481231,1.395033,-0.734222,-9.864156,0.409461],[-9.648618,6.730444,-3.570931,3.958744,-0.656231,-5.477610,-6.796581,-1.277962,6.467529,2.239883,6.410979,-9.855060,3.227887],[2.111797,3.893065,6.213728,1.181173,-8.881674,-4.565043,-7.514962,9.428900,6.870972,7.796858,5.805243,-5.524138,0.227723],[-8.196742,-1.669645,-8.517557,-1.214787,-3.566496,4.453571,-2.722248,5.467377,7.519292,-7.367651,-2.323724,-5.830814,5.187262],[-9.173364,-0.862943,6.478179,-7.954650,-2.033902,0.581093,-0.331797,-0.227790,1.947703,0.715313,-3.638076,0.787499,7.174078]],[[-2.839542,1.501814,-8.364562,9.950375,-9.218558,3.851829,-6.059356,0.663994,-9.892182,-3.543534,-8.296003,-8.239725,-3.333037],[-8.729657,5.731948,-8.300737,-2.130693,8.771682,8.642346,2.871694,4.346307,-1.736879,5.466111,0.168135,3.845708,-8.853955],[8.771067,3.265156,9.687773,4.240090,-4.331318,8.002082,-6.229296,3.947559,2.034371,8.522115,2.460404,0.006932,6.713231],[6.409541,-1.660784,-9.967520,-0.868110,9.373469,-9.740315,-3.324884,-0.474473,7.108760,-6.173450,3.003521,9.910620,-9.630740],[-3.855415,0.235131,-0.645796,7.081335,3.244884,-8.889919,8.925339,5.476646,6.176653,-4.129376,9.311814,-9.203959,-2.645700]],[[-4.376748,-1.705238,1.946794,-6.650412,-2.407860,2.162132,3.321457,-2.080309,-2.022176,5.665568,7.161003,6.064420,5.926041],[8.234233,-1.120706,7.909911,2.635485,3.704816,-2.778173,-8.608652,-6.682864,-2.892439,-9.397128,8.967971,8.032334,-8.891593],[5.653488,-4.783516,4.520346,-9.316197,-3.392087,-2.752107,7.762554,-9.818341,7.587238,9.200298,-1.377147,7.954471,-7.646130],[9.060720,9.599211,-3.847255,1.289260,7.338651,-5.874559,-8.689056,6.199583,-8.880599,-5.592717,0.286841,5.877576,8.314424],[-5.143718,-4.504080,1.037596,-8.126619,-6.824921,-1.438371,-5.261356,-6.112841,5.695140,1.833425,1.615769,-1.567335,-9.551894]],[[8.701909,-2.239936,9.335433,1.503445,1.551186,6.589664,4.380562,-9.155608,6.346539,-7.022119,0.509537,-3.109393,-5.398393],[-3.027375,9.443213,-3.150576,1.397047,6.462729,-0.002058,-9.152134,8.963918,1.503367,9.489141,-7.919710,-2.280432,-3.435734],[9.725887,-7.871792,-8.312608,-4.129218,7.908617,-9.737233,3.270303,4.094343,-6.765670,3.795583,0.143096,0.473362,-2.447513],[4.125875,-1.008027,-9.969048,-0.575341,4.878800,8.539053,-8.147935,3.738763,5.772790,-6.955097,-0.956664,8.084808,7.123919],[-4.248468,8.225213,-7.358665,-7.178724,8.112939,-5.380534,6.473388,-6.486092,9.257327,-7.356976,-6.941371,9.983602,-0.371342]],[[0.386661,8.579547,8.963231,0.164699,-0.722472,7.661970,-4.872818,7.451164,4.545343,9.050644,-0.718323,-6.285592,5.202649],[-2.415409,-5.951258,-2.613312,-2.085718,-2.406825,8.288320,3.580998,4.721949,-9.363009,1.348132,2.608373,3.098648,-8.024887],[3.501989,-2.157267,9.949542,-4.447267,8.354264,-4.144366,-8.046582,0.435605,-5.988356,-3.062734,-3.205244,-9.956086,-3.061091],[-5.648748,-2.108398,5.959200,9.834295,-8.073869,6.460019,-3.115140,4.208014,-4.070081,3.783269,7.162340,-2.380563,-8.331947],[7.888742,-0.143714,-2.338064,9.668020,-3.635188,-0.594890,-2.187147,-7.471993,3.331564,-2.674275,5.925969,3.344433,9.053575]],[[1.502331,-0.415723,-0.048412,-3.028425,9.049413,9.377165,1.366446,-1.255996,9.039729,-3.994835,-2.736375,9.461232,-8.718422],[9.294140,7.562461,-2.449811,9.255659,-9.873003,-2.352931,-4.380923,1.102060,-8.063463,4.350230,6.425746,2.378935,3.341408],[9.472760,0.686183,7.198756,9.650150,6.516231,3.840079,-5.105303,-0.251632,-2.747927,0.025408,-2.956756,-3.489128,-1.232724],[-0.976861,8.036187,4.827204,-3.099451,-4.886722,3.906472,0.117099,-2.507252,4.547555,-7.846001,3.219817,7.074650,3.150839],[9.216012,6.977978,3.523080,5.936853,3.925102,0.341835,8.780721,-1.100630,-0.593563,6.500766,-9.405552,2.926654,-3.593428]],[[-2.483899,3.007153,8.187430,1.033591,-1.396357,2.582425,-4.526648,-7.521125,-8.016065,0.325812,0.143758,-9.459062,-2.562434],[1.771869,-1.625836,6.395358,0.260982,-5.429533,7.911253,-9.848659,-4.116460,7.265813,-4.800421,-8.621462,-7.180389,1.599618],[4.824583,-0.267961,4.849529,-4.128975,-8.499381,-8.392882,-5.149496,-7.512048,-6.913404,-1.676651,-5.604950,6.968019,5.178710],[-6.032750,-4.260577,1.521986,9.096644,5.488895,-8.257451,-1.650192,7.151290,-3.184692,1.658984,2.612983,1.593906,-4.767277],[-8.046484,6.092441,-9.954934,7.447763,0.413829,-4.712586,-1.895197,6.583676,9.413244,7.390648,-1.361291,9.807670,3.958686]],[[-4.125365,-1.662902,-8.958163,-8.829530,-9.387969,4.998825,5.920571,6.391610,-9.073677,-6.777431,-8.948021,2.576034,-6.684631],[4.684504,-4.467674,1.547679,-7.127991,3.200920,-5.026681,-4.135774,-0.125584,-1.540507,-9.179662,-8.188591,8.047696,7.685281],[-4.705033,-9.535303,-2.309598,-5.656720,-6.617409,2.452717,5.771820,4.166800,2.457942,7.358660,-2.361096,5.448401,3.467833],[5.821775,-9.795298,-0.062076,7.412622,-2.539366,-2.913144,-4.626436,-7.109075,3.883896,7.592067,4.641971,-5.448229,-1.379539],[-6.788918,-8.855998,9.750631,-8.517765,-7.365153,7.239461,9.437881,6.883261,-8.334252,-0.749761,-7.966891,7.816972,2.059407]],[[-8.383500,3.087526,-0.039729,-8.529472,2.924957,-2.718591,-2.879917,-2.908022,-8.214690,9.068849,3.316492,-8.323148,-7.607546],[-9.509516,-0.244746,-7.059891,6.217818,4.594537,0.519466,-7.195812,-6.393348,-2.600930,8.008492,-6.626696,0.644257,-5.595149],[5.466928,-2.120033,7.334664,4.221636,-3.939544,-5.855017,5.468515,8.455393,4.331913,3.790697,-4.116401,-4.509736,-3.429544],[-0.569350,-3.844333,8.223855,2.188440,7.930315,-3.049555,-8.793114,-1.941803,-4.216185,-7.056507,-2.584250,-0.865880,7.890330],[-5.493186,-3.930692,-8.801808,-2.941710,8.776726,4.158419,3.986727,1.964665,3.990104,2.567638,-6.788135,-2.933529,9.966715]],[[2.661982,-7.417374,0.155435,-2.272969,-0.560227,-9.825215,-7.344749,-4.319181,-1.560013,-0.042200,5.045686,2.806971,-3.967004],[-0.437323,-9.115813,8.598596,9.795775,3.462772,-0.594297,8.825347,-4.976140,7.770885,6.443808,-1.980374,-7.521438,-0.056005],[2.743118,-1.466170,0.476821,-7.598651,-7.919479,5.652510,7.009694,-2.685327,6.367499,-4.680794,9.173277,-5.241629,7.444441],[-4.767895,3.781681,3.842490,-1.170147,-0.006218,1.173689,-5.281036,1.541220,4.550453,-6.576482,-8.909995,8.691082,5.682313],[7.329007,-4.757996,7.785750,-3.311043,7.750666,6.374051,6.869029,6.722422,-3.151128,-7.130125,-8.564183,-6.346561,-8.757570]]], dtype = "float32")#candidate|4407|(14, 5, 13)|const|float32
uop_4408 = relay.atanh(const_4407.astype('float32')) # shape=(14, 5, 13)
output = relay.Tuple([uop_4408,])
output2 = relay.Tuple([uop_4408,])
func_4410 = relay.Function([], output)
mod['func_4410'] = func_4410
mod = relay.transform.InferType()(mod)
mutated_mod['func_4410'] = func_4410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mutated_mod.get_global_var('func_4410')
call_4411 = func_4410_call()
output = call_4411
func_4412 = relay.Function([], output)
mutated_mod['func_4412'] = func_4412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4424 = relay.TupleGetItem(func_4410_call(), 0)
call_4425 = relay.TupleGetItem(func_4412_call(), 0)
func_3087_call = mod.get_global_var('func_3087')
func_3089_call = mutated_mod.get_global_var('func_3089')
var_4436 = relay.var("var_4436", dtype = "float64", shape = (450,))#candidate|4436|(450,)|var|float64
call_4435 = func_3087_call(relay.reshape(var_4436.astype('float64'), [15, 3, 10]))
call_4437 = func_3087_call(relay.reshape(var_4436.astype('float64'), [15, 3, 10]))
output = relay.Tuple([call_4424,call_4435,var_4436,])
output2 = relay.Tuple([call_4425,call_4437,var_4436,])
func_4445 = relay.Function([var_4436,], output)
mod['func_4445'] = func_4445
mod = relay.transform.InferType()(mod)
mutated_mod['func_4445'] = func_4445
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4446 = relay.var("var_4446", dtype = "float64", shape = (450,))#candidate|4446|(450,)|var|float64
func_4445_call = mutated_mod.get_global_var('func_4445')
call_4447 = func_4445_call(var_4446)
output = call_4447
func_4448 = relay.Function([var_4446], output)
mutated_mod['func_4448'] = func_4448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4458 = relay.TupleGetItem(func_4410_call(), 0)
call_4459 = relay.TupleGetItem(func_4412_call(), 0)
output = call_4458
output2 = call_4459
func_4460 = relay.Function([], output)
mod['func_4460'] = func_4460
mod = relay.transform.InferType()(mod)
mutated_mod['func_4460'] = func_4460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mutated_mod.get_global_var('func_4460')
call_4461 = func_4460_call()
output = call_4461
func_4462 = relay.Function([], output)
mutated_mod['func_4462'] = func_4462
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4471 = relay.var("var_4471", dtype = "int64", shape = (14, 4, 11))#candidate|4471|(14, 4, 11)|var|int64
var_4472 = relay.var("var_4472", dtype = "int64", shape = (14, 4, 11))#candidate|4472|(14, 4, 11)|var|int64
bop_4473 = relay.not_equal(var_4471.astype('bool'), relay.reshape(var_4472.astype('bool'), relay.shape_of(var_4471))) # shape=(14, 4, 11)
bop_4477 = relay.less(var_4471.astype('bool'), relay.reshape(var_4472.astype('bool'), relay.shape_of(var_4471))) # shape=(14, 4, 11)
output = relay.Tuple([bop_4473,bop_4477,])
output2 = relay.Tuple([bop_4473,bop_4477,])
func_4485 = relay.Function([var_4471,var_4472,], output)
mod['func_4485'] = func_4485
mod = relay.transform.InferType()(mod)
mutated_mod['func_4485'] = func_4485
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4485_call = mutated_mod.get_global_var('func_4485')
var_4487 = relay.var("var_4487", dtype = "int64", shape = (14, 4, 11))#candidate|4487|(14, 4, 11)|var|int64
var_4488 = relay.var("var_4488", dtype = "int64", shape = (14, 4, 11))#candidate|4488|(14, 4, 11)|var|int64
call_4486 = func_4485_call(var_4487,var_4488,)
output = call_4486
func_4489 = relay.Function([var_4487,var_4488,], output)
mutated_mod['func_4489'] = func_4489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4538 = relay.TupleGetItem(func_4410_call(), 0)
call_4539 = relay.TupleGetItem(func_4412_call(), 0)
func_1811_call = mod.get_global_var('func_1811')
func_1815_call = mutated_mod.get_global_var('func_1815')
const_4549 = relay.const([-7,-6,-10,-3,-1,-4,-9,9,5,7,-3,-6,-10,4,-10,8,6,2,-3,8,1,2,-5,3,-9,5,-9,9,-9,5,-8,9,-7,9,-7,5,10,-7,-8,-4,3,1,2,5,10,1,3,1,2,-1,6,-6,-3,3,3,8,-9,-2,-6,-2,-7,6,4,9,9,6,7,-4,-3,2,4,-6,7,-6,4,-3,3,-10,-9,5,-10,3,-1,8,6,3,-9,5,-6,-1,6,-1,3,8,-10,-10,-1,8,2,9,-7,7,1,2,-2,-10,-8,9,-2,-3,-7,-5,-8,2,10,-9,4,-2,10,6,10,-2,7,-10,-6,3,10,2,10,9,7,-8,-7,-10,8,-1,-2,-7,-2,-1,-1,-2,2,-8,-1,-4,-8,3,-3,-2,-9,-9,6,3,2,8,8,-4,-5,-3,-3,7,9,7,-3,5,4,6,-10,9,2,-7,7,-1,8,-1,10,2,-5,3,10,1,-2,5,5,5,-3,-8,-6,5,4,4,-1,5,-5,-6,-6,8,-4,-1,-7,6,1,-2,-4,10,2,-4,-10,1,-7,10,-3,-3,-1,6,5,8,8,2,7,-2,5,2,-2,9,-1,5,7,-3,-6,-6,2,4,6,-4,7,-1,-9,-6,-7,4,-5,-4,-7,-3,-5,-4,7,-7,-4,-5,4,-3,-3,7,5,-10,8,-5,10,-10,10,-1,1,-9,6,8,-4,-6,10,-6,3,-7,7,-10,1,1,-5,8,10,-5,-1,-10,-5,-1,8,-2,-1,-5,-3,7,-8,-5,1,-1,1,9,10,-7,4,10,3,-6,-2,-5,8,9,10,-9,7,4,-5,-10,-2,9,-6,1,-2,-6,-10,9,4,-1,4,-7,-9,9,-6,10,7,-8,-8,-4,8,5,2,-5,2,1,6,-6,-3,-1,-5,8,10,-7,-7,-9,1,-4,-7,-9,4,4,-10,-7,7,-1,-10,-8,-7,9,6,-2,3,1,-2,9,-10,6,-3,-4,-2,3,-6,-2,-6,8,10,-2,-3,-3,5,10,2,7,10,8,-6,4,3,-4,7,-4,1,10,-9,8,-4,1,-6,-3,-2,8,1,-10,8,-3,8,-3,-3,3,-5,-8,-3,5,7,-6,9,7,-8,4,4,2,-7,1,8,-2,8,4,-10,1,-8,-6,-2,9,-1,5,-2,-7,2,9,-5,2,2,5,4,-9,4,1,10,6,-3,-9,10,6,-6,-1,-7,-4,-1,-2,4,9,-9,-4,10,-2,-2,2,7,-3,2,-3,9,9,-6,-4,4,-10,6,2,7,1,-5,3,-10,4,-10,-2,-4,-8,-5,5,-10,2,1,1,10,-9,-6,6,9,-7,-8,-10,3,-5,2,8,4,-7,-6,5,2,-2,8,-4,9,-8,2,9,7,4,3,1,-1,-4,-7,-4,5,-7,5,10,3,-1,5,2,8,-1,-7,-10,-1,9,5,8,1,-3,-9,8,-10,-8,-3,-6,6,1,10,-6,-6,-2,10,3,7,6,8,9,7,2,10,8,-7,-1,-10,9,-4,9,3,5,-7,-8,-7,4,6,3,-5,-2,-1,9,-2,7,1,1,-9,6,9,2,10,-1,1,-2,4,7,7,-7,6,8,-2,-1,-7,-9,-10,-4,5,9,-9,2,-5,1,7,-4,1,-10,2,8,-10,-8,5,3,9,-8,4,-2,-9,2,10,-6,-7,8,10,1,-10,-2,-2,7,-8,-10,2,-1,4,6,-9,-6,1,-6,-7,-2,-7,-2,-1,10,3,-2,-3,-8,8,10,-6,-6,10,9,10,-2,8,-7,2,-8,9,-2,7,-9,1,4,8,4,3,-3,7,-9,-1,3,6,-10,1,7,-9,-5,-8,10,9,1,-9,5,2,-10,2,8,-5,3,10,6,-8,2,7,1,-7,-8,-9,-2,-6,-3,6,-6,-10,8,9,-9,-2,3,2,9,-6,-6,9,5,-2,4,10,10,-9,9,-2,-4,-9,6,-1,-3,-2,-2,-10,-6,5,-2,-2,-6,1,-8,4,-7,-9,8,-10,8,1,2,-7,4,2,1,-10,-4,2,4,-6,-9,-8,6,8,-9,-4,-2,1,4,-6,9,2,7,-7,-8,-3,-7,-5,-8,-7,-4,8,-3,-6,4,4,7,9,9,-4,9,5,-10,-9,5,-3,-8,-9,-2,7,-6,-1,6,7,-8,-4,10,-2,-2,-7,8,8,-3,-6,9,-2,4,-9,5,-6,9,-9,1,-9,10,-10,10,-4,-4,-7,-4,9,4,8,6,-2,6,-3,-1,-10,2,1,9,-2,-8,7,10,9,5,-3,3,-3,-7,6,1,-2,9,3,-1,-2,-6,2,-4,-9,-10,10,-8,-2,1,4,5,7,9,3,-6,2,3,-9,-5,-8,1,-10,-4,5,-2,9,4,5,-5,7,1,-7,-3,3,-5,5,-2,-6,-9,2,-1,-3,9,10,4,7,-5,2,-1,8,-8,3,-7,-6,3,10,-1,6,-10,-3,-4,-2,7,8,10,5,8,10,8,-6,4,-4,10,6,-8,4,1,2,-9,7,8,-9,-9,-4,7,-9,-5,-7,-5,-4,-1,-5,-2,2,9,1,1,-4,1,9,-7,10,-3,6,1,9,6,-6,-2,2,-10,-7,-4,-1,-8,-4,1,6,4,-10,-3,7,-4,10,3,-5,4,4,-2,7,-7,2,7,-2,1,-6,-2,6,7,-9,-9,-3,-8,-2,-4,-8,-2,-9,-2,9,-4,10,9,-1,3,9,6,-6,9,-5,-9,-5,7,9,6,3,-5,3,10,-2,-6,6,3,6,-1,6,-6,-8,-5,-2,-5,9,9,-7,10,3,-10,-7,10,6,6,1,3,7,-8,-8,-6,-4,3,-4,-1,-8,-6,4,10,-9,-2,-10,-2,4,8,3,-3,6,8,-8,7,-2,10,-10,5,-7,-2,3,-6,3,3,5,-5,-3,-3,6,8,4,1,8,-5,-5,4,10,9,3,1,7,2,-3,-10,8,4,-7,8,-4,-2,10,9,7,5,-9,9,4,-5,-8,-7,-4,-8,9,6,-9,-2,-4,8,8,-1,-2,2,-4,5,3,-10,-5,8,6,-7,2,-3,8,-8,-7,-3,1,-4,-2,1,-3,2,1,3,-2,10,8,10,7,4,9,4,5,-9,9,2,-10,3,2,7,-4,10,2,-10,8,-4,3,8,-6,-5,-4,-10,-1,6,-6,-9,-3,4,9,-6,-8,-5,-10,9,10,4,8,10,4,-3,2,3,-3,1,-9,-10,-1,9,1,-1,9,7,-7,7,7,-4,-3,4,-3,9,-4,-10,7,-8,7,-9,5,6,-3,5,-4,-6,-7,-7,7,-4,-7,8,6,-10,7,9,-5,6,-9,-5,2,-2,-4,-1,4,-4,2,3,-1,-10,4,10,4,7,-7,-6,6,9,-6,-2,8,1,1,-7,-1,-1,-4,-6,9,2,6,6,-6,3,-7,-4,3,2,-3,6,-6,1,-10,-10,8,4,10,5,6,1,5,6,-3,3,9,-2,-6,5,-7,6,7,-9,-1,4,-4,-9,-2,-6,5,-3,-9,-9,5,3,-9,7,-9,2,3,-7,2,-4,3,9,9,4,6,-3,7,3,2,-1,-8,-1,2,-6,4,-9,1,-6,-10,10,-4,-7,8,-7,9,3,5,-8,4,3,5,-6,10,9,-2,5,2,7,9,-10,5,6,9,-9,8,-2,2,9,2,1,7,-10,-8,-8,-2,-5,-4,-7,7,-6,7,-7,-6,10,-6,-1,-9,-3,9,-3,-10,8,-1,6,10,-2,10,6,8,5,1,1,9,8,-5,-9,-1,-8,-1,-10,-8,9,-6,5,5,9,8,-7,-6,-4,-3,-6,9,7,-10,-10,3,-8,6,-2,3,-6,-3,-9,5,-10,6,5,1,5,2,2,7,-4,-3,-4,10,-1,-1,4,4,6,-1,7,-4,-7,-10,-2,9,1,-4,10,5,9,-2,3,8,-7,-2,-10,9,-5,-6,-7,2,-9,-3,10,-2,3,3,-9,-7,7,3,10,-7,-10,-1,-8,-2,-9,7,10,-10,3,-1,6,1,9,-3,5,-3,2,9,-7,8,6,7,7,1,3,-4,-1,-4,-10,-9,-6,-9,6,-10,-1,-1,4,-4,-7,10,-8,1,-1,10,-2,6,3,6,-3,4,-5,-10,-3,1,-9,10,-7,-7,-3,-8,7,-3,-9,-4,7,6,-3,4,-1,3,-8,-9,1,-5,-6,1,9,6,3,2,-7,4,7,5,-5,-9,-1,-9,-8,-9,9,8,4,-6,5,8,6,-2,-2,-10,5,-1,2,9,6,4,9,-1,-7,9,5,-4,1,-4,2,9,5,-2,-10,7,-10,-1,-3,2,-1,2,8,7,-9,-2,4,6,1,-6,-2,9,4,-1,-2,6,3,9,1,1,-6,-3,-4,2,9,-8,-1,-3,7,-3,-6,-4,7,2,-1,10,-8,10,3,9,9,3,2,-6,-1,-10,8,-7,7,-4,4,6,8,4,-7,3,10,-10,3,3,-5,-2,5,7,-9,-8,7,-5,-9,6,1,6,7,-6,-1,4,-2,-8,-6,-8,-8,-7,10,9,10,9,-5,5,-10,2,-9,-9,3,-7,4,1,10,4,10,3,-9,1,7,3,6,3,2,-6,9,3,7,-5,1,-10,3,1,6,-5,8,4,-5,-1,9,3,1,3,-9,-6,10,-3,9,-6,-6,2,8,9,-3,2,8,-1,-1,-8,5,-1,9,-7,-8,7,-1,-9,5,6,-8,1,4,-6,6,-5,7,-5,2,9,2,-3,5,6,9,7,8,7,9,7,7,-8,10,3,5,1], dtype = "int64")#candidate|4549|(1815,)|const|int64
call_4548 = func_1811_call(relay.reshape(const_4549.astype('int64'), [15, 11, 11]), relay.reshape(const_4549.astype('int64'), [15, 11, 11]), )
call_4550 = func_1811_call(relay.reshape(const_4549.astype('int64'), [15, 11, 11]), relay.reshape(const_4549.astype('int64'), [15, 11, 11]), )
func_3630_call = mod.get_global_var('func_3630')
func_3633_call = mutated_mod.get_global_var('func_3633')
var_4553 = relay.var("var_4553", dtype = "bool", shape = ())#candidate|4553|()|var|bool
call_4552 = relay.TupleGetItem(func_3630_call(relay.reshape(var_4553.astype('bool'), [])), 0)
call_4554 = relay.TupleGetItem(func_3633_call(relay.reshape(var_4553.astype('bool'), [])), 0)
output = relay.Tuple([call_4538,call_4548,const_4549,call_4552,var_4553,])
output2 = relay.Tuple([call_4539,call_4550,const_4549,call_4554,var_4553,])
func_4564 = relay.Function([var_4553,], output)
mod['func_4564'] = func_4564
mod = relay.transform.InferType()(mod)
var_4565 = relay.var("var_4565", dtype = "bool", shape = ())#candidate|4565|()|var|bool
output = func_4564(var_4565)
func_4566 = relay.Function([var_4565], output)
mutated_mod['func_4566'] = func_4566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4576 = relay.TupleGetItem(func_4410_call(), 0)
call_4577 = relay.TupleGetItem(func_4412_call(), 0)
output = call_4576
output2 = call_4577
func_4580 = relay.Function([], output)
mod['func_4580'] = func_4580
mod = relay.transform.InferType()(mod)
output = func_4580()
func_4581 = relay.Function([], output)
mutated_mod['func_4581'] = func_4581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4581_call = mutated_mod.get_global_var('func_4581')
call_4607 = func_4580_call()
call_4608 = func_4580_call()
output = relay.Tuple([call_4607,])
output2 = relay.Tuple([call_4608,])
func_4612 = relay.Function([], output)
mod['func_4612'] = func_4612
mod = relay.transform.InferType()(mod)
mutated_mod['func_4612'] = func_4612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mutated_mod.get_global_var('func_4612')
call_4613 = func_4612_call()
output = call_4613
func_4614 = relay.Function([], output)
mutated_mod['func_4614'] = func_4614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4628 = relay.TupleGetItem(func_4410_call(), 0)
call_4629 = relay.TupleGetItem(func_4412_call(), 0)
uop_4631 = relay.log10(call_4628.astype('float32')) # shape=(14, 5, 13)
uop_4633 = relay.log10(call_4629.astype('float32')) # shape=(14, 5, 13)
output = relay.Tuple([uop_4631,])
output2 = relay.Tuple([uop_4633,])
func_4637 = relay.Function([], output)
mod['func_4637'] = func_4637
mod = relay.transform.InferType()(mod)
mutated_mod['func_4637'] = func_4637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mutated_mod.get_global_var('func_4637')
call_4638 = func_4637_call()
output = call_4638
func_4639 = relay.Function([], output)
mutated_mod['func_4639'] = func_4639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_4661 = func_4460_call()
call_4662 = func_4460_call()
output = call_4661
output2 = call_4662
func_4666 = relay.Function([], output)
mod['func_4666'] = func_4666
mod = relay.transform.InferType()(mod)
mutated_mod['func_4666'] = func_4666
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mutated_mod.get_global_var('func_4666')
call_4667 = func_4666_call()
output = call_4667
func_4668 = relay.Function([], output)
mutated_mod['func_4668'] = func_4668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4581_call = mutated_mod.get_global_var('func_4581')
call_4695 = func_4580_call()
call_4696 = func_4580_call()
func_559_call = mod.get_global_var('func_559')
func_563_call = mutated_mod.get_global_var('func_563')
var_4702 = relay.var("var_4702", dtype = "uint32", shape = ())#candidate|4702|()|var|uint32
var_4703 = relay.var("var_4703", dtype = "uint32", shape = (4,))#candidate|4703|(4,)|var|uint32
call_4701 = func_559_call(relay.reshape(var_4702.astype('uint32'), []), relay.reshape(var_4703.astype('uint32'), [1, 4]), )
call_4704 = func_559_call(relay.reshape(var_4702.astype('uint32'), []), relay.reshape(var_4703.astype('uint32'), [1, 4]), )
func_3630_call = mod.get_global_var('func_3630')
func_3633_call = mutated_mod.get_global_var('func_3633')
call_4728 = relay.TupleGetItem(func_3630_call(relay.reshape(var_4702.astype('bool'), [])), 0)
call_4729 = relay.TupleGetItem(func_3633_call(relay.reshape(var_4702.astype('bool'), [])), 0)
func_4564_call = mod.get_global_var('func_4564')
func_4566_call = mutated_mod.get_global_var('func_4566')
call_4738 = relay.TupleGetItem(func_4564_call(relay.reshape(var_4702.astype('bool'), [])), 4)
call_4739 = relay.TupleGetItem(func_4566_call(relay.reshape(var_4702.astype('bool'), [])), 4)
output = relay.Tuple([call_4695,call_4701,var_4702,var_4703,call_4728,call_4738,])
output2 = relay.Tuple([call_4696,call_4704,var_4702,var_4703,call_4729,call_4739,])
func_4743 = relay.Function([var_4702,var_4703,], output)
mod['func_4743'] = func_4743
mod = relay.transform.InferType()(mod)
mutated_mod['func_4743'] = func_4743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4743_call = mutated_mod.get_global_var('func_4743')
var_4745 = relay.var("var_4745", dtype = "uint32", shape = ())#candidate|4745|()|var|uint32
var_4746 = relay.var("var_4746", dtype = "uint32", shape = (4,))#candidate|4746|(4,)|var|uint32
call_4744 = func_4743_call(var_4745,var_4746,)
output = call_4744
func_4747 = relay.Function([var_4745,var_4746,], output)
mutated_mod['func_4747'] = func_4747
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_4762 = func_4460_call()
call_4763 = func_4460_call()
uop_4774 = relay.sqrt(call_4762.astype('float64')) # shape=(14, 5, 13)
uop_4776 = relay.sqrt(call_4763.astype('float64')) # shape=(14, 5, 13)
output = uop_4774
output2 = uop_4776
func_4777 = relay.Function([], output)
mod['func_4777'] = func_4777
mod = relay.transform.InferType()(mod)
output = func_4777()
func_4778 = relay.Function([], output)
mutated_mod['func_4778'] = func_4778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_4804 = func_4666_call()
call_4805 = func_4666_call()
output = relay.Tuple([call_4804,])
output2 = relay.Tuple([call_4805,])
func_4814 = relay.Function([], output)
mod['func_4814'] = func_4814
mod = relay.transform.InferType()(mod)
mutated_mod['func_4814'] = func_4814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mutated_mod.get_global_var('func_4814')
call_4815 = func_4814_call()
output = call_4815
func_4816 = relay.Function([], output)
mutated_mod['func_4816'] = func_4816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_4847 = relay.TupleGetItem(func_4612_call(), 0)
call_4848 = relay.TupleGetItem(func_4614_call(), 0)
output = relay.Tuple([call_4847,])
output2 = relay.Tuple([call_4848,])
func_4849 = relay.Function([], output)
mod['func_4849'] = func_4849
mod = relay.transform.InferType()(mod)
output = func_4849()
func_4850 = relay.Function([], output)
mutated_mod['func_4850'] = func_4850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_4874 = relay.TupleGetItem(func_4637_call(), 0)
call_4875 = relay.TupleGetItem(func_4639_call(), 0)
func_2296_call = mod.get_global_var('func_2296')
func_2298_call = mutated_mod.get_global_var('func_2298')
const_4877 = relay.const([-9,4,1,-8,-1,-3,-5,2,9,6,1,-1,-4,-4,-5,8,9,9,10,-4,8,-6,4,-6,7,4,2,4,2,-8,-4,-9,8,1,-5,7,-4,6,-4,-9,-4,8,10,2,1,-9,8,-5,7,-4,-3,-6,7,-5,6,-1,-6,-6,10,-8,-10,5,-4,4,-8,-6,1,-10,-3,9,-8,10,9,2,-6,2,7,1,6,7,-4,-7,-2,-5,-9,-4,5,2,-2,5,5,1,3,-7,9,-4,-4,8,-7,3,-9,4,-3,-10,-1,10,-10,-1,-6,5,4,-6,10,6,-9,5,8,-2,8,-3,-6,-8,-7,-1,-9,6,-6,2,8,-7,-7,-7,-4,5,10,2,2,-4,8,9,4,1,-10,9,-10,-7,9,-1,4,6,3,-1,9,-3,-5,-4,-10,8,-7,9,3,4,1,-6,1,-10,1,9,-1,7,-7,-2,6,-6,-8,10,-1,1,2,-9,-1,-9,-2,-10,-3,6,10,6,9,10,-4,-9,7,-9,9,-3,-6,-1,-5,1,10,9,-9,-5,-4,6,-7,5,6,4,1,-4,-2,-7,-7,-6,-8,-6,-9,-7,-6,-2,-9,7,-10,-9,-10,10,-9,10,5,-3,-2,-2,-10,3,4,-10,-2,-6,-8,5,-9,10,10,-4,-8,2,7,-1,4,4,-9,9,-1,-4,-2,-7,-4,7,-8,10,9,8,-7,5,-10,9,3,-1,-5,-5,5,-7,2,-2,-6,-8,6,3,4,-7,4,4,-6,-4,-1,9,3,-5,-2,5,1,5,1,3,3,-10,7,-8,10,-7,3,8,-4,2,10,-7,3,8,-9,9,-10,3,-2,2,5,4,-7,-7,-3,-8,8,-4,7,-7,3,-10,-5,-2,-6,-9,-6,-8,-5,-4,3,3,-5,-4,-9,1,-7,4,-4,6,-3,-10,10,-1,-2,-5,-9,8,-5,8,-1,5,10,9,6,-5,-10,9,2,5,9,2,-8,1,1,5,-8,2,-10,3,6,-6,-2,8,-8,-1,3,-2,4,-4,5,-8,10,3,3,-9,-4,7,1,-2,-8,-6,6,2,3,4,-5,-5,4,-6,-3,-6,-1,5,-8,-1,-7,7,-4,3,5,9,10,5,-1,-3,-8,-3,3,1,2,8,-8,5,4,-1,-5,-8,-4,1,8,10,-4,-4,-1,-8,8,2,-1,-8,-5,5,-1,7,8,3,-1,-3,-7,1,4,9,-5,8,10,-2,-6,4,-2,5,8,-7,2,-5,-8,7,6,-4,6,7,-9,-2,-8,4,-9,9,10,10,5,-1,4,5,-3,-10,-2,-7,-8,7,5,-3,2,-4,9,4,-9,-8,-2,-2,-1,-6,-1,-5,-1,-4,-4,3,-10,-10,-10,4,-1,4,-5,-10,1,1,-8,3,-7,-6,-6,6,-7,-7,-1,10,-3,-7,3,5,1,7,2,-9,-9,-9,7,10,-4,-2,-10,-8,9,1,1,5,4,3,2,-5,10,-5,-9,-10,-4,7,7,6,1,5,5,-5,-1,-3,2,-5,1,-7,7,-3,-10,-2,6,-2,-5,-8,-8,-7,3,6,-9,-6,-3,1,2,8,6,10,7,-10,8,3,3,7,-4,-9,-1,5,8,3,-10,2,10,8,4,2,-6,-10,-8,4,7,7,8,4,-6,8,8,3,-3,-7,-1,-1,-5,7,-5,5,4,-1,-2,10,10,7,7,-5,-3,7,1,-10,-8,-10,-7,6,7,-6,10,8,-2,-9,-6,-1,-9,2,8,-10,10,9,7,1,-1,-4,10,5,8,3,2,-3,-4,-3,-7,-9,5,4,-3,5,-1,9,2,5,1,3,4,4,-1,2,-4,-4,-9,8,-5,-8,-1,-2,-2,-4,-7,-6,-3,2,-1,-1,-5,1,-5,-6,1,1,-2,6,9,6,-7,8,-3,5,5,7,2,2,7,2,-3,-2,5,8,10,-2,4,-10,-10,-1,4,5,-7,5,-6,-4,1,5,-5,-2,8,-5,-5,1,1,-2,-1,-1,5,-2,5,1,1,-4,2,-5,-1,3,7,-1,8,-5,10,9,4,-6,9,-6,5,1,9,8,-6,6,-6,4,-10,-5,5,-8,7,-9,-3,-7,9,8,3,6,8,7,-8,-8,-9,3,-6,4,-4,10,-10,-8,6,-6,1,-2,-3,2,9,-4,-2,-4,-5,-4,5,-8,2,5,1,8,-3,-2,-7,-10,4,-7,-8,-7,-3,-3,2,3,-7,-1,-10,-4,-9,-9,-1,-3,2,3,10,4,10,2,-9,7,5,-8,-7,10,-9,2,-10,8,6,-2,1,2], dtype = "int16")#candidate|4877|(864,)|const|int16
call_4876 = func_2296_call(relay.reshape(const_4877.astype('int16'), [9, 6, 16]))
call_4878 = func_2296_call(relay.reshape(const_4877.astype('int16'), [9, 6, 16]))
uop_4881 = relay.tan(call_4874.astype('float64')) # shape=(14, 5, 13)
uop_4883 = relay.tan(call_4875.astype('float64')) # shape=(14, 5, 13)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_4884 = func_4666_call()
call_4885 = func_4666_call()
output = relay.Tuple([call_4876,const_4877,uop_4881,call_4884,])
output2 = relay.Tuple([call_4878,const_4877,uop_4883,call_4885,])
func_4893 = relay.Function([], output)
mod['func_4893'] = func_4893
mod = relay.transform.InferType()(mod)
output = func_4893()
func_4894 = relay.Function([], output)
mutated_mod['func_4894'] = func_4894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_4918 = func_4666_call()
call_4919 = func_4666_call()
func_1748_call = mod.get_global_var('func_1748')
func_1753_call = mutated_mod.get_global_var('func_1753')
var_4928 = relay.var("var_4928", dtype = "float64", shape = (1456,))#candidate|4928|(1456,)|var|float64
const_4929 = relay.const([[-7],[-6],[3],[5],[-3],[10],[-6],[-2],[9],[-1],[9],[-1],[-10],[9],[10],[-2],[10],[4],[-5],[-7],[-2],[10],[6],[-10],[-3],[1],[-5],[-10],[1],[-6],[5],[-8],[7],[-10],[10],[1],[-4],[1],[-2],[-6],[4],[-8],[-10],[-3],[10],[-3],[-9],[-1],[4],[-1],[1],[-10],[2],[5],[-4],[8],[8],[6],[6],[10],[3],[10],[4],[-10],[-5],[7],[-2],[10],[-8],[-9],[-6],[10],[-5],[-4],[10]], dtype = "uint32")#candidate|4929|(75, 1)|const|uint32
const_4930 = relay.const(2, dtype = "uint32")#candidate|4930|()|const|uint32
call_4927 = relay.TupleGetItem(func_1748_call(relay.reshape(var_4928.astype('float64'), [13, 16, 7]), relay.reshape(const_4929.astype('uint32'), [75,]), relay.reshape(const_4930.astype('uint32'), []), ), 0)
call_4931 = relay.TupleGetItem(func_1753_call(relay.reshape(var_4928.astype('float64'), [13, 16, 7]), relay.reshape(const_4929.astype('uint32'), [75,]), relay.reshape(const_4930.astype('uint32'), []), ), 0)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_4932 = relay.TupleGetItem(func_4410_call(), 0)
call_4933 = relay.TupleGetItem(func_4412_call(), 0)
func_2367_call = mod.get_global_var('func_2367')
func_2371_call = mutated_mod.get_global_var('func_2371')
var_4938 = relay.var("var_4938", dtype = "int32", shape = (528, 2))#candidate|4938|(528, 2)|var|int32
call_4937 = relay.TupleGetItem(func_2367_call(relay.reshape(var_4938.astype('int32'), [8, 12, 11]), relay.reshape(var_4928.astype('float64'), [1456,]), relay.reshape(const_4930.astype('uint32'), []), ), 3)
call_4939 = relay.TupleGetItem(func_2371_call(relay.reshape(var_4938.astype('int32'), [8, 12, 11]), relay.reshape(var_4928.astype('float64'), [1456,]), relay.reshape(const_4930.astype('uint32'), []), ), 3)
func_2431_call = mod.get_global_var('func_2431')
func_2434_call = mutated_mod.get_global_var('func_2434')
var_4941 = relay.var("var_4941", dtype = "float64", shape = (35,))#candidate|4941|(35,)|var|float64
call_4940 = relay.TupleGetItem(func_2431_call(relay.reshape(var_4941.astype('float64'), [7, 5, 1])), 0)
call_4942 = relay.TupleGetItem(func_2434_call(relay.reshape(var_4941.astype('float64'), [7, 5, 1])), 0)
output = relay.Tuple([call_4918,call_4927,var_4928,const_4929,const_4930,call_4932,call_4937,var_4938,call_4940,var_4941,])
output2 = relay.Tuple([call_4919,call_4931,var_4928,const_4929,const_4930,call_4933,call_4939,var_4938,call_4942,var_4941,])
func_4945 = relay.Function([var_4928,var_4938,var_4941,], output)
mod['func_4945'] = func_4945
mod = relay.transform.InferType()(mod)
var_4946 = relay.var("var_4946", dtype = "float64", shape = (1456,))#candidate|4946|(1456,)|var|float64
var_4947 = relay.var("var_4947", dtype = "int32", shape = (528, 2))#candidate|4947|(528, 2)|var|int32
var_4948 = relay.var("var_4948", dtype = "float64", shape = (35,))#candidate|4948|(35,)|var|float64
output = func_4945(var_4946,var_4947,var_4948,)
func_4949 = relay.Function([var_4946,var_4947,var_4948,], output)
mutated_mod['func_4949'] = func_4949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_4989 = relay.TupleGetItem(func_4612_call(), 0)
call_4990 = relay.TupleGetItem(func_4614_call(), 0)
func_559_call = mod.get_global_var('func_559')
func_563_call = mutated_mod.get_global_var('func_563')
var_4997 = relay.var("var_4997", dtype = "uint32", shape = ())#candidate|4997|()|var|uint32
var_4998 = relay.var("var_4998", dtype = "uint32", shape = (4,))#candidate|4998|(4,)|var|uint32
call_4996 = func_559_call(relay.reshape(var_4997.astype('uint32'), []), relay.reshape(var_4998.astype('uint32'), [1, 4]), )
call_4999 = func_559_call(relay.reshape(var_4997.astype('uint32'), []), relay.reshape(var_4998.astype('uint32'), [1, 4]), )
func_1044_call = mod.get_global_var('func_1044')
func_1047_call = mutated_mod.get_global_var('func_1047')
var_5004 = relay.var("var_5004", dtype = "uint64", shape = (1344, 1))#candidate|5004|(1344, 1)|var|uint64
call_5003 = relay.TupleGetItem(func_1044_call(relay.reshape(var_5004.astype('uint64'), [14, 12, 8]), relay.reshape(var_4997.astype('uint32'), []), ), 1)
call_5005 = relay.TupleGetItem(func_1047_call(relay.reshape(var_5004.astype('uint64'), [14, 12, 8]), relay.reshape(var_4997.astype('uint32'), []), ), 1)
output = relay.Tuple([call_4989,call_4996,var_4997,var_4998,call_5003,var_5004,])
output2 = relay.Tuple([call_4990,call_4999,var_4997,var_4998,call_5005,var_5004,])
func_5006 = relay.Function([var_4997,var_4998,var_5004,], output)
mod['func_5006'] = func_5006
mod = relay.transform.InferType()(mod)
mutated_mod['func_5006'] = func_5006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5006_call = mutated_mod.get_global_var('func_5006')
var_5008 = relay.var("var_5008", dtype = "uint32", shape = ())#candidate|5008|()|var|uint32
var_5009 = relay.var("var_5009", dtype = "uint32", shape = (4,))#candidate|5009|(4,)|var|uint32
var_5010 = relay.var("var_5010", dtype = "uint64", shape = (1344, 1))#candidate|5010|(1344, 1)|var|uint64
call_5007 = func_5006_call(var_5008,var_5009,var_5010,)
output = call_5007
func_5011 = relay.Function([var_5008,var_5009,var_5010,], output)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_5015 = relay.TupleGetItem(func_4637_call(), 0)
call_5016 = relay.TupleGetItem(func_4639_call(), 0)
output = call_5015
output2 = call_5016
func_5024 = relay.Function([], output)
mod['func_5024'] = func_5024
mod = relay.transform.InferType()(mod)
mutated_mod['func_5024'] = func_5024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5024_call = mutated_mod.get_global_var('func_5024')
call_5025 = func_5024_call()
output = call_5025
func_5026 = relay.Function([], output)
mutated_mod['func_5026'] = func_5026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_5029 = relay.TupleGetItem(func_4410_call(), 0)
call_5030 = relay.TupleGetItem(func_4412_call(), 0)
func_4564_call = mod.get_global_var('func_4564')
func_4566_call = mutated_mod.get_global_var('func_4566')
var_5033 = relay.var("var_5033", dtype = "bool", shape = ())#candidate|5033|()|var|bool
call_5032 = relay.TupleGetItem(func_4564_call(relay.reshape(var_5033.astype('bool'), [])), 4)
call_5034 = relay.TupleGetItem(func_4566_call(relay.reshape(var_5033.astype('bool'), [])), 4)
output = relay.Tuple([call_5029,call_5032,var_5033,])
output2 = relay.Tuple([call_5030,call_5034,var_5033,])
func_5059 = relay.Function([var_5033,], output)
mod['func_5059'] = func_5059
mod = relay.transform.InferType()(mod)
mutated_mod['func_5059'] = func_5059
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5060 = relay.var("var_5060", dtype = "bool", shape = ())#candidate|5060|()|var|bool
func_5059_call = mutated_mod.get_global_var('func_5059')
call_5061 = func_5059_call(var_5060)
output = call_5061
func_5062 = relay.Function([var_5060], output)
mutated_mod['func_5062'] = func_5062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mod.get_global_var('func_4893')
func_4894_call = mutated_mod.get_global_var('func_4894')
call_5087 = relay.TupleGetItem(func_4893_call(), 2)
call_5088 = relay.TupleGetItem(func_4894_call(), 2)
output = relay.Tuple([call_5087,])
output2 = relay.Tuple([call_5088,])
func_5146 = relay.Function([], output)
mod['func_5146'] = func_5146
mod = relay.transform.InferType()(mod)
mutated_mod['func_5146'] = func_5146
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mutated_mod.get_global_var('func_5146')
call_5147 = func_5146_call()
output = call_5147
func_5148 = relay.Function([], output)
mutated_mod['func_5148'] = func_5148
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_5187 = relay.TupleGetItem(func_4849_call(), 0)
call_5188 = relay.TupleGetItem(func_4850_call(), 0)
func_3087_call = mod.get_global_var('func_3087')
func_3089_call = mutated_mod.get_global_var('func_3089')
const_5200 = relay.const([2.558678,-2.319855,2.888978,-5.578513,7.122891,-6.874474,2.584806,4.171536,-4.936763,-9.755266,4.734751,-3.078288,-9.835547,-5.333462,-8.291645,-4.791316,7.021888,-3.920391,2.158627,-0.478504,5.490997,7.842701,-1.611181,7.410759,-6.809881,-1.090121,2.705990,-6.698442,-0.911228,3.836800,5.529623,-2.439538,-9.214727,3.135650,7.585722,5.273908,-1.920045,6.911133,7.867107,-8.669876,-2.141511,4.868110,9.781361,9.226832,-2.042181,-2.347286,4.998656,-7.956311,4.820299,1.398676,-5.942226,-8.447243,-2.104483,4.296093,-7.196109,0.183006,-3.712780,-5.751186,-2.910508,9.466067,-4.432879,-3.693439,-4.955475,-3.422713,6.113270,-0.361600,-9.982882,-2.590569,8.954070,-1.738030,6.396421,-7.200688,-0.749971,8.762884,4.363402,-9.798004,-4.476423,3.640983,4.118965,0.402705,6.706904,-4.739966,-2.654378,-8.085694,-1.025453,1.952390,-5.170593,-3.597251,1.622741,-8.221113,-6.775138,-4.253353,2.303047,-0.512210,7.911275,6.623787,7.065505,-7.564493,5.348775,9.826870,9.387695,7.861365,8.785694,6.458290,-7.847640,3.709314,-0.070729,8.340216,2.306848,-4.597790,6.414451,9.290518,-9.378797,-0.343273,5.881569,8.216182,5.002036,-8.397240,-6.906214,5.008851,1.497865,-1.674377,-0.338883,-1.425934,4.160122,1.197929,-9.316897,7.345172,-7.138431,-3.315569,-5.910649,0.786054,9.126584,-7.316808,0.955683,-6.022853,-3.047688,-2.507509,-2.517137,-4.994526,9.510402,0.351273,-4.334625,-0.794359,-3.382753,-6.249957,8.411238,-6.278922,-1.897164,-2.185736,-5.934833,-5.935646,8.993414,-1.925263,9.077266,0.341422,-4.054372,5.855312,-0.358298,5.013558,-5.090396,0.639337,2.283313,-3.273349,-0.348448,3.131444,9.306501,6.209523,-9.792588,7.110590,-7.719009,6.574760,2.167277,4.697359,-7.535196,-0.658229,2.897010,-4.459659,-7.485531,-8.022686,-2.974347,1.485701,6.901863,-4.118132,-4.997086,-7.454226,8.010604,8.340223,-6.624882,-1.250868,-8.072597,3.640694,-8.675390,-1.142614,9.684005,0.282979,6.892596,6.576789,4.471419,-8.605266,7.072255,-3.551033,-8.070361,5.814099,-4.077591,-3.274329,6.362512,-8.758483,9.793166,-3.431306,4.202226,-4.905287,-6.344153,-2.853177,-8.437940,-7.060417,4.123072,-5.377189,-6.588884,-8.543288,1.636251,0.940566,-7.619142,-7.436302,7.510013,-6.726552,-0.559827,7.870607,2.934602,-1.112786,-7.849528,0.148846,3.278426,-7.228339,-7.716836,-3.768629,5.795046,-8.091431,-9.413527,2.640109,0.133347,-9.916053,3.880100,-8.444588,8.732168,-7.939304,3.384645,5.432872,6.061100,0.532720,-1.411355,5.915023,4.377158,-0.895863,-5.442349,4.676163,2.714316,0.577558,1.273437,8.391264,-7.151227,0.587041,-3.542594,-1.851579,-7.256292,0.730118,0.322356,-7.022835,-7.143304,-3.727416,-2.407521,-1.073270,-2.330786,-2.561017,5.279964,-4.532481,0.829882,-2.812499,2.482638,1.910419,-0.373744,-0.608026,2.078316,-7.481548,3.915038,-1.367828,5.971383,-8.332449,-1.102912,7.036521,-8.262845,4.038196,0.002047,0.481695,-6.835655,-7.063675,0.057468,0.093547,1.805256,-9.465273,-7.939586,1.558444,0.607301,2.731900,-3.043368,-8.876057,9.177533,0.866940,8.958959,1.332562,2.772793,-4.081247,-8.639551,-1.041143,3.414761,4.886591,5.913781,9.865343,-0.594694,1.637508,-3.513906,2.161139,4.065395,-6.995190,-6.044162,5.804120,-8.187018,-0.936120,0.552906,-5.529449,-2.339586,-9.208631,-6.684403,-3.373619,7.696692,-4.831997,5.304786,1.099956,-6.082288,5.489854,3.409468,-0.395807,-7.741036,-4.962441,7.905044,2.741144,-8.568424,-5.789827,7.893740,0.054141,-1.777987,-0.883018,-5.874181,-1.180944,-2.007051,9.158962,-4.228671,2.203701,-5.762361,-7.611629,-1.545990,7.446205,-7.706807,-3.699456,6.067093,-7.835048,3.893320,5.720505,-3.856663,-6.887640,-7.155056,-2.751712,8.287869,5.937267,2.852784,-8.355507,0.725646,5.953536,5.268635,-2.960264,8.244267,-6.204043,6.721564,-9.311105,4.149752,-0.259108,-1.088432,6.618764,-8.524840,-3.958591,-3.696649,-6.933370,-0.928181,7.325665,3.604379,-4.478743,-0.146146,5.680534,5.829497,7.972974,-3.086181,-7.209321,-3.469783,-1.852487,-5.664097,9.656750,0.600749,4.524833,6.538328,4.346333,-6.954125,2.646941,-2.583405,-0.608799,9.347703,8.765828,-4.978121,-2.395306,1.329126,8.359828,3.216045,-9.478263,-2.051765,4.749106,5.248098,-3.804702,-8.385003,-2.311227,-7.410537,-5.183099,8.193885,7.157820,0.910440,-4.053507,6.821465,9.384595,-3.064905,0.117763,8.686826,-7.137101,-4.989228,-3.840079,2.563224,6.706872,3.358827,6.853789,7.189234,-4.744590,-7.199500,7.380879], dtype = "float64")#candidate|5200|(450,)|const|float64
call_5199 = func_3087_call(relay.reshape(const_5200.astype('float64'), [15, 3, 10]))
call_5201 = func_3087_call(relay.reshape(const_5200.astype('float64'), [15, 3, 10]))
output = relay.Tuple([call_5187,call_5199,const_5200,])
output2 = relay.Tuple([call_5188,call_5201,const_5200,])
func_5203 = relay.Function([], output)
mod['func_5203'] = func_5203
mod = relay.transform.InferType()(mod)
mutated_mod['func_5203'] = func_5203
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mutated_mod.get_global_var('func_5203')
call_5204 = func_5203_call()
output = call_5204
func_5205 = relay.Function([], output)
mutated_mod['func_5205'] = func_5205
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4777_call = mod.get_global_var('func_4777')
func_4778_call = mutated_mod.get_global_var('func_4778')
call_5255 = func_4777_call()
call_5256 = func_4777_call()
output = relay.Tuple([call_5255,])
output2 = relay.Tuple([call_5256,])
func_5257 = relay.Function([], output)
mod['func_5257'] = func_5257
mod = relay.transform.InferType()(mod)
mutated_mod['func_5257'] = func_5257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5257_call = mutated_mod.get_global_var('func_5257')
call_5258 = func_5257_call()
output = call_5258
func_5259 = relay.Function([], output)
mutated_mod['func_5259'] = func_5259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_5262 = relay.TupleGetItem(func_5146_call(), 0)
call_5263 = relay.TupleGetItem(func_5148_call(), 0)
output = relay.Tuple([call_5262,])
output2 = relay.Tuple([call_5263,])
func_5269 = relay.Function([], output)
mod['func_5269'] = func_5269
mod = relay.transform.InferType()(mod)
mutated_mod['func_5269'] = func_5269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5269_call = mutated_mod.get_global_var('func_5269')
call_5270 = func_5269_call()
output = call_5270
func_5271 = relay.Function([], output)
mutated_mod['func_5271'] = func_5271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mod.get_global_var('func_4814')
func_4816_call = mutated_mod.get_global_var('func_4816')
call_5283 = relay.TupleGetItem(func_4814_call(), 0)
call_5284 = relay.TupleGetItem(func_4816_call(), 0)
func_3630_call = mod.get_global_var('func_3630')
func_3633_call = mutated_mod.get_global_var('func_3633')
const_5300 = relay.const(False, dtype = "bool")#candidate|5300|()|const|bool
call_5299 = relay.TupleGetItem(func_3630_call(relay.reshape(const_5300.astype('bool'), [])), 0)
call_5301 = relay.TupleGetItem(func_3633_call(relay.reshape(const_5300.astype('bool'), [])), 0)
func_4485_call = mod.get_global_var('func_4485')
func_4489_call = mutated_mod.get_global_var('func_4489')
var_5303 = relay.var("var_5303", dtype = "int64", shape = (616,))#candidate|5303|(616,)|var|int64
call_5302 = relay.TupleGetItem(func_4485_call(relay.reshape(var_5303.astype('int64'), [14, 4, 11]), relay.reshape(var_5303.astype('int64'), [14, 4, 11]), ), 1)
call_5304 = relay.TupleGetItem(func_4489_call(relay.reshape(var_5303.astype('int64'), [14, 4, 11]), relay.reshape(var_5303.astype('int64'), [14, 4, 11]), ), 1)
func_4445_call = mod.get_global_var('func_4445')
func_4448_call = mutated_mod.get_global_var('func_4448')
const_5311 = relay.const([-5.613679,-7.744991,-8.473953,-7.655442,4.469346,4.281573,-0.912481,-3.528738,7.102287,-8.583291,6.627873,9.907700,-8.211241,-2.175866,8.401673,3.507630,2.014610,5.563557,-2.099631,-6.692058,-7.378922,-0.172940,2.330543,-9.138433,-5.142714,0.983687,2.512282,-1.315783,-6.342468,0.298970,3.712644,-6.185981,-8.715811,-2.937822,3.572598,0.456942,8.099321,-7.808401,-9.813481,1.883842,-7.294003,-1.595585,-4.500332,9.001564,-6.460881,-5.000948,6.335159,-3.591298,-6.361422,-6.228080,5.875001,-4.596586,6.978855,-0.799093,0.660702,7.447985,-7.218299,9.326154,-4.219177,-4.489944,-3.957049,-9.994787,8.133440,3.875870,9.753522,8.957048,2.480866,7.367396,6.102556,9.020265,-3.352071,-6.998947,-6.499616,8.643653,-3.382427,2.914587,-2.567111,-6.502760,-7.247249,4.611697,1.077946,4.189080,-6.924879,9.441600,-9.224048,9.683297,5.436777,5.935329,1.733871,-2.815483,-7.511150,-9.624135,3.408736,-4.989248,5.146428,-6.499393,9.980757,8.577741,-8.009489,1.941227,7.598199,8.246782,-8.092471,9.908715,8.604625,7.416496,7.873001,-0.357991,-6.727073,2.075208,1.409644,-2.141370,0.761484,-7.806977,-8.255895,-7.286255,-6.955102,6.081653,-7.777506,9.230388,-2.099111,-4.541048,-4.815473,7.283411,9.544355,-4.482798,-0.909703,0.409638,0.367296,3.427623,5.952389,8.064389,-2.269890,-7.605025,7.108265,-5.089769,-4.364645,-3.307570,-6.254871,7.677332,-2.897240,-8.089299,-6.444463,-2.900557,0.168728,-3.382373,9.364393,5.751170,-6.799826,-3.282468,5.836266,2.807522,2.030607,-0.705649,0.362595,-9.599752,-1.879531,-0.691639,-4.758714,-7.747087,9.228136,0.252689,-8.923114,-0.339369,-2.326083,9.943395,0.808555,-2.548483,-2.906917,-6.913970,-1.053777,8.576774,7.217272,-0.198988,-6.964390,-2.351470,3.801488,-5.786692,-7.747741,-0.677903,0.582872,-9.237490,-0.122877,-2.111510,3.008411,5.812520,3.074567,-8.520434,-1.293587,-5.384775,5.427309,-6.531557,-2.058625,5.228262,1.586715,-7.521470,0.521043,-2.163288,0.848128,-4.679100,2.416533,-9.846761,-9.953700,-1.908498,9.619954,8.386480,5.316191,9.977814,-3.384400,-2.218239,-0.991483,-5.201057,3.450156,-3.258296,2.990283,7.049876,-4.591132,1.965964,8.512873,5.516078,9.548065,5.078182,6.988584,-5.856901,3.316505,3.321160,4.045972,4.994211,-2.922252,5.205542,-9.265315,3.136597,4.957735,4.699725,-2.323595,3.508732,1.315799,-9.545182,-4.257153,-2.891704,2.306724,1.305461,-8.759729,4.160568,-0.554933,-7.139670,7.926570,7.421096,3.232660,7.577634,-2.661478,8.297481,-0.982570,-9.309712,-8.877097,-6.902342,-0.203820,8.252408,3.416550,-8.289623,9.956309,-1.716987,-4.213204,5.681572,1.464915,6.209113,-7.307633,0.552561,-4.588118,9.808155,7.100063,-8.895682,9.996670,-0.685132,-9.935189,7.479149,5.612026,-2.931553,7.356152,2.649032,5.167900,-1.385785,4.731774,-1.559089,3.261143,1.338206,3.189986,2.729737,0.001685,5.566938,-9.487496,0.296950,6.196481,3.227658,-8.571756,7.981240,2.107876,3.128929,6.793142,-8.733068,1.213833,6.717930,0.701784,4.105838,-5.465409,-4.106007,5.151611,0.546311,1.876774,-6.845927,3.480027,8.464516,4.580082,-7.617583,-6.992897,-8.427943,-3.837050,6.259841,-3.279084,-4.373771,0.710915,5.892722,-1.666234,3.868216,5.936296,9.829303,6.058191,2.791443,3.921721,-8.340004,-7.699532,6.566506,-3.380108,-8.577814,-0.865421,-1.437624,1.731261,-1.775340,-7.142857,8.201904,9.560735,-9.940660,-3.396390,-2.206155,4.193568,2.457617,9.415569,-1.660858,7.460354,-6.843734,2.357659,-0.072262,-2.323959,1.073745,-0.851924,-0.298497,6.950881,5.691959,-3.709225,-0.129109,-4.036009,5.539252,-1.932741,3.082743,-6.604772,1.805020,-6.650589,-2.061305,5.398731,5.176417,-3.894138,7.650897,2.003919,4.578206,-6.850145,0.010014,-7.061752,-0.868578,1.677644,-6.960572,9.416624,8.158032,9.750597,-4.761660,9.596478,5.523513,5.492921,-4.586668,8.734546,-3.764040,9.486978,-6.442288,-9.612635,-1.744218,-0.647038,1.167692,0.513838,-8.848245,-2.835314,3.071713,-6.962943,-0.232126,7.909318,-6.453367,-6.558190,7.155295,9.924229,0.862924,-8.293462,4.622609,2.826806,2.578403,1.177251,6.230836,-1.973747,-3.897452,3.845723,0.539914,1.402752,0.707458,-6.919014,5.162442,-4.166467,-2.086749,-0.720812,-9.864187,-0.128166,-3.336817,1.545576,-7.930464,-3.447812,-8.041008,8.770280,1.400523,-2.333554,-4.026635,4.778275,-0.456981,0.387974,-3.407349,-6.901165,1.172961,-8.621876,-1.327763,8.555331,-3.081686,9.859463,-2.871749,-4.915597,1.732511], dtype = "float64")#candidate|5311|(450,)|const|float64
call_5310 = relay.TupleGetItem(func_4445_call(relay.reshape(const_5311.astype('float64'), [450,])), 1)
call_5312 = relay.TupleGetItem(func_4448_call(relay.reshape(const_5311.astype('float64'), [450,])), 1)
output = relay.Tuple([call_5283,call_5299,const_5300,call_5302,var_5303,call_5310,const_5311,])
output2 = relay.Tuple([call_5284,call_5301,const_5300,call_5304,var_5303,call_5312,const_5311,])
func_5326 = relay.Function([var_5303,], output)
mod['func_5326'] = func_5326
mod = relay.transform.InferType()(mod)
mutated_mod['func_5326'] = func_5326
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5327 = relay.var("var_5327", dtype = "int64", shape = (616,))#candidate|5327|(616,)|var|int64
func_5326_call = mutated_mod.get_global_var('func_5326')
call_5328 = func_5326_call(var_5327)
output = call_5328
func_5329 = relay.Function([var_5327], output)
mutated_mod['func_5329'] = func_5329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5331 = relay.var("var_5331", dtype = "float64", shape = (3, 1, 13))#candidate|5331|(3, 1, 13)|var|float64
uop_5332 = relay.asinh(var_5331.astype('float64')) # shape=(3, 1, 13)
func_4485_call = mod.get_global_var('func_4485')
func_4489_call = mutated_mod.get_global_var('func_4489')
var_5336 = relay.var("var_5336", dtype = "int64", shape = (616,))#candidate|5336|(616,)|var|int64
call_5335 = relay.TupleGetItem(func_4485_call(relay.reshape(var_5336.astype('int64'), [14, 4, 11]), relay.reshape(var_5336.astype('int64'), [14, 4, 11]), ), 1)
call_5337 = relay.TupleGetItem(func_4489_call(relay.reshape(var_5336.astype('int64'), [14, 4, 11]), relay.reshape(var_5336.astype('int64'), [14, 4, 11]), ), 1)
output = relay.Tuple([uop_5332,call_5335,var_5336,])
output2 = relay.Tuple([uop_5332,call_5337,var_5336,])
func_5342 = relay.Function([var_5331,var_5336,], output)
mod['func_5342'] = func_5342
mod = relay.transform.InferType()(mod)
var_5343 = relay.var("var_5343", dtype = "float64", shape = (3, 1, 13))#candidate|5343|(3, 1, 13)|var|float64
var_5344 = relay.var("var_5344", dtype = "int64", shape = (616,))#candidate|5344|(616,)|var|int64
output = func_5342(var_5343,var_5344,)
func_5345 = relay.Function([var_5343,var_5344,], output)
mutated_mod['func_5345'] = func_5345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_5363 = func_4460_call()
call_5364 = func_4460_call()
func_3087_call = mod.get_global_var('func_3087')
func_3089_call = mutated_mod.get_global_var('func_3089')
const_5376 = relay.const([[-6.703640,-0.902088,-3.757516,-8.568170,8.231177,4.148156,6.937350,-5.313224,-9.470946,4.489720,-6.009610,1.208495,-6.520036,9.417114,6.040640,6.961616,6.879026,-4.914413,-1.136562,-3.827967,8.867694,-4.847704,7.837181,-5.074278,-8.277580,2.353921,-8.307608,4.603092,-6.313343,4.889453,-1.992884,6.681129,5.324250,2.366578,-6.504051,7.329306,-0.441874,5.539377,-5.312789,3.326387,8.371940,-9.770389,9.375970,-5.124710,-8.982475,6.268734,-3.594383,-8.367889,-4.756410,1.391312,-7.253619,-3.515793,8.674200,-9.544749,2.311925,-9.996485,-9.263725,5.121164,-7.213391,2.284032,9.804890,-1.393699,-7.254121,1.957014,-8.471197,0.732709,-3.495300,7.209331,1.668023,3.986267,4.228460,9.836481,-9.431313,7.494602,4.830336,-0.277432,4.998862,-9.402015,3.932819,-3.604979,7.213902,-6.844156,3.185880,5.828491,8.271872,-6.319360,-7.111843,9.679615,-6.948586,-4.242446],[7.112608,-1.442763,9.584862,-7.032515,9.363848,-5.706449,9.988317,-2.280231,1.785613,0.485569,-8.732322,8.741367,-0.467287,-8.103099,-7.120030,-8.112738,5.835522,-1.301797,4.682713,4.126928,-3.338175,9.588175,5.079519,-8.592404,9.133035,9.770437,4.530643,7.760621,9.324754,-7.332332,-4.264725,-2.802671,-3.648672,-4.712403,6.329592,-0.219836,6.873249,5.639745,8.818285,5.694169,-2.626231,-5.001687,-9.062057,2.720107,1.402446,7.562970,-7.828370,4.633381,-0.371913,-8.426013,-5.284040,9.561800,2.067402,-6.036150,0.618739,8.394843,-0.722350,9.505183,5.071888,2.840307,8.002114,-7.987108,-5.645785,-2.408246,0.085824,-0.402625,7.886188,-5.541611,9.425865,1.998301,-2.815097,-4.733620,-7.487535,0.036672,-0.285000,3.127839,0.802400,5.017339,2.681331,2.531377,-9.082764,-4.092091,9.787469,-8.519645,5.238608,7.337826,3.737535,7.930124,-1.136689,7.192645],[2.630294,-2.337832,1.736027,-4.595373,9.528322,9.916893,5.815767,2.342410,-7.716323,9.785468,9.749168,-8.439131,-3.084388,-8.092498,-9.281758,3.624850,-9.589473,7.464846,1.712845,1.871075,1.025140,2.628829,-8.028789,5.883641,-5.907813,6.893104,-0.317138,-3.469136,1.424076,7.792562,2.543524,5.952538,-6.006996,9.003622,-7.280118,-3.914090,1.872944,-4.372797,-0.364457,7.520795,4.433186,-1.595348,-6.397454,-2.159736,1.292439,8.163187,5.281208,1.141015,9.770590,4.414785,4.253116,1.779697,6.643904,-7.398354,-5.321343,1.360251,-6.982481,2.939307,-6.068479,-6.525928,3.046276,-5.187421,-5.233315,-3.740685,-9.361661,0.701199,8.813813,9.987250,1.230876,-7.306047,0.397580,4.491136,6.743622,-1.024596,-6.044471,1.395014,-6.601297,-9.472376,9.869841,5.768269,6.326569,9.162707,2.165593,8.850875,3.372791,-6.965500,3.876871,-5.857687,-9.553842,2.584565],[-4.407085,-7.079638,-4.129346,1.842395,8.610392,-4.563363,-7.319373,5.246526,-4.787486,-4.432728,-6.101391,-8.733229,-7.395908,-9.161876,9.431007,4.451013,7.298053,-4.669221,7.815661,9.483829,-5.604070,6.728641,-5.811517,6.642832,9.199806,-7.317989,-1.637342,-8.180376,5.227490,-3.784161,-8.024372,-4.190088,1.024471,8.876691,6.685929,-6.980842,-7.618456,-5.105233,-6.486217,2.267213,9.464088,-7.823005,-4.409512,-8.161404,9.713706,-0.347225,-9.852809,5.315834,-8.166899,-4.615759,-5.493760,9.783696,-7.789808,2.140734,1.469726,2.653433,-9.132570,5.550280,-2.223713,-4.635224,-9.241511,8.705025,-8.290916,-5.871833,9.085708,-1.919460,5.646307,7.072127,5.621315,2.398662,9.608035,1.262609,-2.581990,8.019598,-4.838207,-7.055818,-5.905072,9.296924,6.232765,8.490761,2.923128,-2.965608,-2.807208,-6.481102,-4.638875,-5.463676,-5.877767,3.146512,-8.676824,2.373241],[-1.034759,1.846999,2.230834,1.758822,6.314772,-5.349120,-0.094127,8.422647,-6.076990,-9.972879,6.524577,-6.884742,-2.433700,-9.205146,-3.273102,2.351963,-0.865067,-5.698667,-0.628998,-6.911202,-4.306559,-0.240629,4.154596,2.798746,6.990207,-2.832037,3.934123,5.214746,-7.208100,-9.030454,6.103468,4.039917,0.194681,-8.699144,-6.811288,4.772622,1.039807,0.748590,8.361796,-5.706377,2.103923,-6.067442,4.597562,-6.712829,9.699226,2.018765,4.131355,-2.121651,-7.522468,-9.392911,1.097931,0.091220,3.503427,1.537427,-5.324840,2.297266,-8.501255,-0.411396,6.438957,6.564762,5.324115,-2.569245,-9.179858,7.803777,4.337364,5.486326,7.482749,1.688888,1.203495,-8.870366,-0.098645,6.889945,6.800128,-4.052477,5.371696,2.120784,-8.928212,0.234065,8.458718,8.457942,-6.752602,5.885180,-5.639337,-5.414096,-7.935099,7.997541,-9.068947,0.440699,-4.600756,2.635586]], dtype = "float64")#candidate|5376|(5, 90)|const|float64
call_5375 = func_3087_call(relay.reshape(const_5376.astype('float64'), [15, 3, 10]))
call_5377 = func_3087_call(relay.reshape(const_5376.astype('float64'), [15, 3, 10]))
output = relay.Tuple([call_5363,call_5375,const_5376,])
output2 = relay.Tuple([call_5364,call_5377,const_5376,])
func_5383 = relay.Function([], output)
mod['func_5383'] = func_5383
mod = relay.transform.InferType()(mod)
mutated_mod['func_5383'] = func_5383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5383_call = mutated_mod.get_global_var('func_5383')
call_5384 = func_5383_call()
output = call_5384
func_5385 = relay.Function([], output)
mutated_mod['func_5385'] = func_5385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5269_call = mod.get_global_var('func_5269')
func_5271_call = mutated_mod.get_global_var('func_5271')
call_5419 = relay.TupleGetItem(func_5269_call(), 0)
call_5420 = relay.TupleGetItem(func_5271_call(), 0)
func_5059_call = mod.get_global_var('func_5059')
func_5062_call = mutated_mod.get_global_var('func_5062')
var_5428 = relay.var("var_5428", dtype = "bool", shape = ())#candidate|5428|()|var|bool
call_5427 = relay.TupleGetItem(func_5059_call(relay.reshape(var_5428.astype('bool'), [])), 0)
call_5429 = relay.TupleGetItem(func_5062_call(relay.reshape(var_5428.astype('bool'), [])), 0)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_5440 = relay.TupleGetItem(func_5383_call(), 1)
call_5441 = relay.TupleGetItem(func_5385_call(), 1)
bop_5444 = relay.logical_xor(var_5428.astype('int64'), call_5419.astype('int64')) # shape=(14, 5, 13)
bop_5447 = relay.logical_xor(var_5428.astype('int64'), call_5420.astype('int64')) # shape=(14, 5, 13)
output = relay.Tuple([call_5427,call_5440,bop_5444,])
output2 = relay.Tuple([call_5429,call_5441,bop_5447,])
func_5461 = relay.Function([var_5428,], output)
mod['func_5461'] = func_5461
mod = relay.transform.InferType()(mod)
mutated_mod['func_5461'] = func_5461
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5462 = relay.var("var_5462", dtype = "bool", shape = ())#candidate|5462|()|var|bool
func_5461_call = mutated_mod.get_global_var('func_5461')
call_5463 = func_5461_call(var_5462)
output = call_5463
func_5464 = relay.Function([var_5462], output)
mutated_mod['func_5464'] = func_5464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_5531 = relay.TupleGetItem(func_5383_call(), 0)
call_5532 = relay.TupleGetItem(func_5385_call(), 0)
func_2296_call = mod.get_global_var('func_2296')
func_2298_call = mutated_mod.get_global_var('func_2298')
var_5539 = relay.var("var_5539", dtype = "int16", shape = (216, 4))#candidate|5539|(216, 4)|var|int16
call_5538 = func_2296_call(relay.reshape(var_5539.astype('int16'), [9, 6, 16]))
call_5540 = func_2296_call(relay.reshape(var_5539.astype('int16'), [9, 6, 16]))
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_5546 = relay.TupleGetItem(func_5203_call(), 2)
call_5547 = relay.TupleGetItem(func_5205_call(), 2)
bop_5550 = relay.power(call_5538.astype('float64'), relay.reshape(var_5539.astype('float64'), relay.shape_of(call_5538))) # shape=(9, 6, 16)
bop_5553 = relay.power(call_5540.astype('float64'), relay.reshape(var_5539.astype('float64'), relay.shape_of(call_5540))) # shape=(9, 6, 16)
output = relay.Tuple([call_5531,call_5546,bop_5550,])
output2 = relay.Tuple([call_5532,call_5547,bop_5553,])
func_5567 = relay.Function([var_5539,], output)
mod['func_5567'] = func_5567
mod = relay.transform.InferType()(mod)
var_5568 = relay.var("var_5568", dtype = "int16", shape = (216, 4))#candidate|5568|(216, 4)|var|int16
output = func_5567(var_5568)
func_5569 = relay.Function([var_5568], output)
mutated_mod['func_5569'] = func_5569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mod.get_global_var('func_4893')
func_4894_call = mutated_mod.get_global_var('func_4894')
call_5602 = relay.TupleGetItem(func_4893_call(), 2)
call_5603 = relay.TupleGetItem(func_4894_call(), 2)
output = relay.Tuple([call_5602,])
output2 = relay.Tuple([call_5603,])
func_5604 = relay.Function([], output)
mod['func_5604'] = func_5604
mod = relay.transform.InferType()(mod)
mutated_mod['func_5604'] = func_5604
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5604_call = mutated_mod.get_global_var('func_5604')
call_5605 = func_5604_call()
output = call_5605
func_5606 = relay.Function([], output)
mutated_mod['func_5606'] = func_5606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_5617 = func_4460_call()
call_5618 = func_4460_call()
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_5619 = func_4460_call()
call_5620 = func_4460_call()
output = relay.Tuple([call_5617,call_5619,])
output2 = relay.Tuple([call_5618,call_5620,])
func_5622 = relay.Function([], output)
mod['func_5622'] = func_5622
mod = relay.transform.InferType()(mod)
output = func_5622()
func_5623 = relay.Function([], output)
mutated_mod['func_5623'] = func_5623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mod.get_global_var('func_4893')
func_4894_call = mutated_mod.get_global_var('func_4894')
call_5629 = relay.TupleGetItem(func_4893_call(), 3)
call_5630 = relay.TupleGetItem(func_4894_call(), 3)
func_2431_call = mod.get_global_var('func_2431')
func_2434_call = mutated_mod.get_global_var('func_2434')
const_5646 = relay.const([[8.912000,-6.349582,-5.695870,-8.190405,3.694837],[8.923242,-6.155533,5.773453,9.796941,-3.856657],[-9.146402,-6.737937,6.445756,3.545524,3.192949],[-5.584449,-8.152384,-8.483841,-9.565347,9.734912],[6.706463,-7.761137,-9.560651,0.419908,0.554510],[-8.664680,8.551431,-5.212931,-3.251045,-2.725023],[-4.567523,3.401499,8.640272,4.496784,-1.257046]], dtype = "float64")#candidate|5646|(7, 5)|const|float64
call_5645 = relay.TupleGetItem(func_2431_call(relay.reshape(const_5646.astype('float64'), [7, 5, 1])), 0)
call_5647 = relay.TupleGetItem(func_2434_call(relay.reshape(const_5646.astype('float64'), [7, 5, 1])), 0)
func_3372_call = mod.get_global_var('func_3372')
func_3374_call = mutated_mod.get_global_var('func_3374')
var_5655 = relay.var("var_5655", dtype = "float64", shape = (120,))#candidate|5655|(120,)|var|float64
call_5654 = relay.TupleGetItem(func_3372_call(relay.reshape(var_5655.astype('float64'), [1, 15, 8])), 0)
call_5656 = relay.TupleGetItem(func_3374_call(relay.reshape(var_5655.astype('float64'), [1, 15, 8])), 0)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_5657 = func_5024_call()
call_5658 = func_5024_call()
func_4485_call = mod.get_global_var('func_4485')
func_4489_call = mutated_mod.get_global_var('func_4489')
var_5676 = relay.var("var_5676", dtype = "int64", shape = (616,))#candidate|5676|(616,)|var|int64
call_5675 = relay.TupleGetItem(func_4485_call(relay.reshape(var_5676.astype('int64'), [14, 4, 11]), relay.reshape(var_5676.astype('int64'), [14, 4, 11]), ), 0)
call_5677 = relay.TupleGetItem(func_4489_call(relay.reshape(var_5676.astype('int64'), [14, 4, 11]), relay.reshape(var_5676.astype('int64'), [14, 4, 11]), ), 0)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_5692 = relay.TupleGetItem(func_4612_call(), 0)
call_5693 = relay.TupleGetItem(func_4614_call(), 0)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_5712 = relay.TupleGetItem(func_4612_call(), 0)
call_5713 = relay.TupleGetItem(func_4614_call(), 0)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_5718 = relay.TupleGetItem(func_4612_call(), 0)
call_5719 = relay.TupleGetItem(func_4614_call(), 0)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_5729 = relay.TupleGetItem(func_5146_call(), 0)
call_5730 = relay.TupleGetItem(func_5148_call(), 0)
func_5342_call = mod.get_global_var('func_5342')
func_5345_call = mutated_mod.get_global_var('func_5345')
var_5735 = relay.var("var_5735", dtype = "float64", shape = (39,))#candidate|5735|(39,)|var|float64
call_5734 = relay.TupleGetItem(func_5342_call(relay.reshape(var_5735.astype('float64'), [3, 1, 13]), relay.reshape(var_5676.astype('int64'), [616,]), ), 0)
call_5736 = relay.TupleGetItem(func_5345_call(relay.reshape(var_5735.astype('float64'), [3, 1, 13]), relay.reshape(var_5676.astype('int64'), [616,]), ), 0)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_5737 = func_5024_call()
call_5738 = func_5024_call()
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_5745 = func_4666_call()
call_5746 = func_4666_call()
func_4814_call = mod.get_global_var('func_4814')
func_4816_call = mutated_mod.get_global_var('func_4816')
call_5751 = relay.TupleGetItem(func_4814_call(), 0)
call_5752 = relay.TupleGetItem(func_4816_call(), 0)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_5758 = relay.TupleGetItem(func_4612_call(), 0)
call_5759 = relay.TupleGetItem(func_4614_call(), 0)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_5770 = func_5024_call()
call_5771 = func_5024_call()
output = relay.Tuple([call_5629,call_5645,const_5646,call_5654,var_5655,call_5657,call_5675,var_5676,call_5692,call_5712,call_5718,call_5729,call_5734,var_5735,call_5737,call_5745,call_5751,call_5758,call_5770,])
output2 = relay.Tuple([call_5630,call_5647,const_5646,call_5656,var_5655,call_5658,call_5677,var_5676,call_5693,call_5713,call_5719,call_5730,call_5736,var_5735,call_5738,call_5746,call_5752,call_5759,call_5771,])
func_5773 = relay.Function([var_5655,var_5676,var_5735,], output)
mod['func_5773'] = func_5773
mod = relay.transform.InferType()(mod)
mutated_mod['func_5773'] = func_5773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5773_call = mutated_mod.get_global_var('func_5773')
var_5775 = relay.var("var_5775", dtype = "float64", shape = (120,))#candidate|5775|(120,)|var|float64
var_5776 = relay.var("var_5776", dtype = "int64", shape = (616,))#candidate|5776|(616,)|var|int64
var_5777 = relay.var("var_5777", dtype = "float64", shape = (39,))#candidate|5777|(39,)|var|float64
call_5774 = func_5773_call(var_5775,var_5776,var_5777,)
output = call_5774
func_5778 = relay.Function([var_5775,var_5776,var_5777,], output)
mutated_mod['func_5778'] = func_5778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_5823 = relay.TupleGetItem(func_4637_call(), 0)
call_5824 = relay.TupleGetItem(func_4639_call(), 0)
output = relay.Tuple([call_5823,])
output2 = relay.Tuple([call_5824,])
func_5831 = relay.Function([], output)
mod['func_5831'] = func_5831
mod = relay.transform.InferType()(mod)
mutated_mod['func_5831'] = func_5831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5831_call = mutated_mod.get_global_var('func_5831')
call_5832 = func_5831_call()
output = call_5832
func_5833 = relay.Function([], output)
mutated_mod['func_5833'] = func_5833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_5893 = relay.TupleGetItem(func_4612_call(), 0)
call_5894 = relay.TupleGetItem(func_4614_call(), 0)
output = relay.Tuple([call_5893,])
output2 = relay.Tuple([call_5894,])
func_5900 = relay.Function([], output)
mod['func_5900'] = func_5900
mod = relay.transform.InferType()(mod)
output = func_5900()
func_5901 = relay.Function([], output)
mutated_mod['func_5901'] = func_5901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mod.get_global_var('func_4893')
func_4894_call = mutated_mod.get_global_var('func_4894')
call_5950 = relay.TupleGetItem(func_4893_call(), 3)
call_5951 = relay.TupleGetItem(func_4894_call(), 3)
output = call_5950
output2 = call_5951
func_5961 = relay.Function([], output)
mod['func_5961'] = func_5961
mod = relay.transform.InferType()(mod)
output = func_5961()
func_5962 = relay.Function([], output)
mutated_mod['func_5962'] = func_5962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5831_call = mod.get_global_var('func_5831')
func_5833_call = mutated_mod.get_global_var('func_5833')
call_5974 = relay.TupleGetItem(func_5831_call(), 0)
call_5975 = relay.TupleGetItem(func_5833_call(), 0)
func_5461_call = mod.get_global_var('func_5461')
func_5464_call = mutated_mod.get_global_var('func_5464')
var_5984 = relay.var("var_5984", dtype = "bool", shape = ())#candidate|5984|()|var|bool
call_5983 = relay.TupleGetItem(func_5461_call(relay.reshape(var_5984.astype('bool'), [])), 0)
call_5985 = relay.TupleGetItem(func_5464_call(relay.reshape(var_5984.astype('bool'), [])), 0)
output = relay.Tuple([call_5974,call_5983,var_5984,])
output2 = relay.Tuple([call_5975,call_5985,var_5984,])
func_5987 = relay.Function([var_5984,], output)
mod['func_5987'] = func_5987
mod = relay.transform.InferType()(mod)
mutated_mod['func_5987'] = func_5987
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5988 = relay.var("var_5988", dtype = "bool", shape = ())#candidate|5988|()|var|bool
func_5987_call = mutated_mod.get_global_var('func_5987')
call_5989 = func_5987_call(var_5988)
output = call_5989
func_5990 = relay.Function([var_5988], output)
mutated_mod['func_5990'] = func_5990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5831_call = mod.get_global_var('func_5831')
func_5833_call = mutated_mod.get_global_var('func_5833')
call_6045 = relay.TupleGetItem(func_5831_call(), 0)
call_6046 = relay.TupleGetItem(func_5833_call(), 0)
func_3981_call = mod.get_global_var('func_3981')
func_3984_call = mutated_mod.get_global_var('func_3984')
var_6064 = relay.var("var_6064", dtype = "float32", shape = (400,))#candidate|6064|(400,)|var|float32
call_6063 = relay.TupleGetItem(func_3981_call(relay.reshape(var_6064.astype('float32'), [5, 10, 8])), 0)
call_6065 = relay.TupleGetItem(func_3984_call(relay.reshape(var_6064.astype('float32'), [5, 10, 8])), 0)
uop_6066 = relay.asinh(var_6064.astype('float32')) # shape=(400,)
output = relay.Tuple([call_6045,call_6063,uop_6066,])
output2 = relay.Tuple([call_6046,call_6065,uop_6066,])
func_6068 = relay.Function([var_6064,], output)
mod['func_6068'] = func_6068
mod = relay.transform.InferType()(mod)
var_6069 = relay.var("var_6069", dtype = "float32", shape = (400,))#candidate|6069|(400,)|var|float32
output = func_6068(var_6069)
func_6070 = relay.Function([var_6069], output)
mutated_mod['func_6070'] = func_6070
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6074 = relay.var("var_6074", dtype = "float32", shape = (11, 5, 1))#candidate|6074|(11, 5, 1)|var|float32
uop_6075 = relay.log10(var_6074.astype('float32')) # shape=(11, 5, 1)
bop_6080 = relay.bitwise_xor(uop_6075.astype('uint16'), relay.reshape(var_6074.astype('uint16'), relay.shape_of(uop_6075))) # shape=(11, 5, 1)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_6083 = func_5024_call()
call_6084 = func_5024_call()
uop_6089 = relay.log2(uop_6075.astype('float32')) # shape=(11, 5, 1)
output = relay.Tuple([bop_6080,call_6083,uop_6089,])
output2 = relay.Tuple([bop_6080,call_6084,uop_6089,])
func_6091 = relay.Function([var_6074,], output)
mod['func_6091'] = func_6091
mod = relay.transform.InferType()(mod)
mutated_mod['func_6091'] = func_6091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6092 = relay.var("var_6092", dtype = "float32", shape = (11, 5, 1))#candidate|6092|(11, 5, 1)|var|float32
func_6091_call = mutated_mod.get_global_var('func_6091')
call_6093 = func_6091_call(var_6092)
output = call_6093
func_6094 = relay.Function([var_6092], output)
mutated_mod['func_6094'] = func_6094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_6126 = relay.TupleGetItem(func_5146_call(), 0)
call_6127 = relay.TupleGetItem(func_5148_call(), 0)
output = call_6126
output2 = call_6127
func_6130 = relay.Function([], output)
mod['func_6130'] = func_6130
mod = relay.transform.InferType()(mod)
mutated_mod['func_6130'] = func_6130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6130_call = mutated_mod.get_global_var('func_6130')
call_6131 = func_6130_call()
output = call_6131
func_6132 = relay.Function([], output)
mutated_mod['func_6132'] = func_6132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_6140 = relay.TupleGetItem(func_4637_call(), 0)
call_6141 = relay.TupleGetItem(func_4639_call(), 0)
output = relay.Tuple([call_6140,])
output2 = relay.Tuple([call_6141,])
func_6150 = relay.Function([], output)
mod['func_6150'] = func_6150
mod = relay.transform.InferType()(mod)
output = func_6150()
func_6151 = relay.Function([], output)
mutated_mod['func_6151'] = func_6151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_6160 = relay.TupleGetItem(func_5146_call(), 0)
call_6161 = relay.TupleGetItem(func_5148_call(), 0)
func_2296_call = mod.get_global_var('func_2296')
func_2298_call = mutated_mod.get_global_var('func_2298')
const_6165 = relay.const([-7,2,-8,9,-2,1,-5,-3,-8,-9,-6,-8,8,-7,1,8,3,-7,9,-5,2,10,8,2,10,7,-8,1,8,-8,10,-6,-8,-5,8,-5,-7,-10,10,5,7,8,-6,-3,6,1,7,-2,2,-9,9,-3,-3,-3,8,5,-7,3,1,-8,-7,-5,-8,-9,-4,1,4,-10,-10,10,-1,3,7,3,-4,-6,-10,7,-8,8,-7,-7,-4,10,10,-2,-6,-10,3,-4,2,9,-3,-2,7,4,1,-8,8,9,-9,-10,-7,9,-4,8,5,10,6,-8,1,6,3,7,2,-1,6,-8,-4,3,-2,-3,-8,4,2,6,3,-5,6,8,-7,-10,2,6,-7,-3,-9,7,-7,3,2,-5,1,-3,-4,-6,-2,6,4,-10,-2,-1,7,-10,10,8,-3,9,6,1,-3,-1,-3,8,8,10,3,2,-1,6,8,-5,8,-4,-8,-4,-2,-7,-1,-2,-5,10,-4,-7,7,-10,1,5,-1,-4,2,9,1,8,-1,3,-1,-5,5,1,9,-8,-7,8,2,9,9,9,-4,-4,-7,4,-9,-4,10,8,-7,8,1,-5,9,8,-2,10,4,-2,2,-9,-4,7,8,-3,-4,-2,10,-8,1,-7,-3,-8,2,9,5,-4,1,-3,7,-8,1,-5,-7,-8,-1,1,3,-4,-9,-10,1,5,5,4,8,-4,4,-7,-6,-1,-3,2,2,-2,9,7,-6,-3,-4,5,-1,-10,10,-5,-6,3,7,-5,9,1,-9,-7,5,-6,-9,1,-1,2,-10,-8,-3,6,-4,10,8,3,-4,-2,2,-7,10,8,1,-3,-9,9,-9,4,4,9,9,-9,2,-9,-1,3,6,-3,5,2,-6,-8,6,8,-9,-3,-9,-9,-6,-3,-9,-10,-2,-4,10,3,-6,1,-4,-1,-4,-1,-7,-3,-3,1,5,-6,8,-3,5,6,-6,3,-4,5,9,2,-10,-2,-3,4,-6,-4,2,7,-3,1,10,1,8,-5,-6,4,3,-7,-9,-4,-3,3,6,-5,1,-10,7,6,-9,-4,-7,1,4,-4,-10,10,-7,-1,3,1,9,6,3,5,10,-9,6,6,-9,-5,-9,2,-9,6,-8,-7,-8,-7,4,7,9,-2,-5,7,9,2,-6,-3,-7,7,7,6,-7,-8,-3,7,-10,-9,7,8,-7,-3,5,7,6,9,8,-9,-8,-5,2,5,1,7,-1,4,-7,10,-3,-6,-1,-2,-2,-1,2,1,8,-7,1,6,1,9,-7,10,6,-10,-10,-7,7,-1,5,-4,10,-3,5,3,9,6,1,-9,9,-7,4,-1,1,2,8,1,5,-8,-3,-10,5,2,9,4,-3,-9,4,-9,-6,4,-7,1,-9,4,-2,-8,-8,2,2,-9,8,3,2,8,3,9,7,3,8,9,2,8,8,9,-7,-6,-8,8,8,-7,8,-2,5,4,-3,-5,10,4,5,-9,-4,7,3,4,-3,-4,-7,7,-2,-7,-4,9,-8,-6,-8,5,-2,-6,10,-6,-10,-4,-1,-1,4,9,2,5,-10,-3,6,2,2,2,-9,5,-3,8,-3,-6,-7,-6,10,1,2,10,-3,5,10,9,8,-1,-4,4,10,-4,-2,7,4,3,3,-6,-8,4,-10,9,7,-8,1,-8,-1,-7,7,-6,2,-6,5,-3,-3,-10,10,-3,-1,7,3,2,-10,-9,-3,-7,-6,-1,-7,5,9,-4,-7,5,-8,-10,8,6,-1,6,-2,8,-9,1,1,-7,3,1,-8,8,9,-10,-9,6,3,-3,-8,-5,8,-3,1,-1,-3,4,9,9,1,-4,6,-10,3,-6,-2,7,6,-1,10,-3,6,-6,9,-2,5,-1,-7,1,-4,-2,7,-8,-9,-2,-3,-4,2,4,3,2,-4,-10,5,1,-8,8,2,8,7,2,5,-10,6,-8,2,9,-4,6,-8,-9,-10,2,2,-3,2,-10,-1,-5,8,6,-5,5,1,1,8,8,6,2,-1,-9,-2,1,-3,10,10,-1,-10,6,-10,5,-6,8,2,-2,-8,-8,-1,-4,5,-6,-2,4,3,-7,7,-3,-2,7,-4,7,-9,10,5,-4,2,7,-7,7,-3,7,4,-4,-2,2,-7,5,5,-8,3,-1,4,-8,3,4,-10,5,-10,2,-10,-5,-5,-5,-8,-1,4,6,3,8,-9,-1,3,3,-7,-3,-9,-5,1,-7,2,-1,-1,4,-1,2,-5,9,1,1,-6,6,-5,2,-1,-6,-6,-7,4,-2,4,-6,-9,8,6,-7], dtype = "int16")#candidate|6165|(864,)|const|int16
call_6164 = func_2296_call(relay.reshape(const_6165.astype('int16'), [9, 6, 16]))
call_6166 = func_2296_call(relay.reshape(const_6165.astype('int16'), [9, 6, 16]))
func_5257_call = mod.get_global_var('func_5257')
func_5259_call = mutated_mod.get_global_var('func_5259')
call_6171 = relay.TupleGetItem(func_5257_call(), 0)
call_6172 = relay.TupleGetItem(func_5259_call(), 0)
output = relay.Tuple([call_6160,call_6164,const_6165,call_6171,])
output2 = relay.Tuple([call_6161,call_6166,const_6165,call_6172,])
func_6225 = relay.Function([], output)
mod['func_6225'] = func_6225
mod = relay.transform.InferType()(mod)
mutated_mod['func_6225'] = func_6225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6225_call = mutated_mod.get_global_var('func_6225')
call_6226 = func_6225_call()
output = call_6226
func_6227 = relay.Function([], output)
mutated_mod['func_6227'] = func_6227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_6371 = relay.TupleGetItem(func_5203_call(), 2)
call_6372 = relay.TupleGetItem(func_5205_call(), 2)
func_5342_call = mod.get_global_var('func_5342')
func_5345_call = mutated_mod.get_global_var('func_5345')
var_6393 = relay.var("var_6393", dtype = "float64", shape = (39,))#candidate|6393|(39,)|var|float64
var_6394 = relay.var("var_6394", dtype = "int64", shape = (616,))#candidate|6394|(616,)|var|int64
call_6392 = relay.TupleGetItem(func_5342_call(relay.reshape(var_6393.astype('float64'), [3, 1, 13]), relay.reshape(var_6394.astype('int64'), [616,]), ), 2)
call_6395 = relay.TupleGetItem(func_5345_call(relay.reshape(var_6393.astype('float64'), [3, 1, 13]), relay.reshape(var_6394.astype('int64'), [616,]), ), 2)
var_6396 = relay.var("var_6396", dtype = "float64", shape = (39,))#candidate|6396|(39,)|var|float64
bop_6397 = relay.greater_equal(var_6393.astype('bool'), relay.reshape(var_6396.astype('bool'), relay.shape_of(var_6393))) # shape=(39,)
func_4945_call = mod.get_global_var('func_4945')
func_4949_call = mutated_mod.get_global_var('func_4949')
const_6401 = relay.const([-2.073579,2.395807,-2.852582,-0.860727,-9.835490,-6.866250,-8.900593,3.634532,-8.995297,0.676160,7.363541,-7.858900,5.033079,7.391455,-2.162760,9.013012,1.269370,5.694862,5.417767,2.568227,3.025080,-9.903786,-1.988896,4.053429,6.599985,-7.758038,-1.137734,-8.996092,-0.560680,-2.829737,-5.968925,2.503060,5.201785,8.961766,2.516836,-7.138237,-4.133160,-2.976263,-9.181075,9.924587,-0.416247,5.504447,-2.267143,9.635955,0.101445,3.999007,6.933909,-0.145987,-6.363929,5.288112,-9.004539,-4.962100,-7.665599,3.762343,-0.815905,-9.186558,-8.743131,1.533878,2.978336,4.061901,-3.437359,-7.602860,-1.231242,-0.008084,-8.341773,-3.184778,7.676786,6.584885,1.921040,5.624577,2.971744,-9.752849,6.251468,-2.746028,-9.746432,6.448546,5.794578,-6.732296,-3.473528,-3.881857,-4.431198,1.951718,9.727303,0.146304,-4.384491,-6.028668,-2.436713,6.517264,-5.348035,9.227339,-9.264737,6.466962,-2.527758,8.771991,4.024860,-1.026364,-6.937940,7.871702,-7.816452,-0.744474,6.832715,8.007555,7.793579,0.339893,-1.510239,3.439094,-1.337591,-7.026786,-6.777105,9.541422,6.931105,-7.611087,-3.352626,9.321743,-6.185019,7.412441,-3.943262,-9.662656,9.235442,5.618992,-2.663201,-7.605650,-6.027646,4.810418,-3.185612,-6.757950,-3.438074,1.083555,-3.096074,-3.286642,-8.456893,4.705635,-1.528563,0.818452,2.158263,5.619749,4.382612,-9.694699,6.241046,-7.866877,6.504680,5.714855,8.234621,-4.503041,-8.976290,0.822071,-7.292197,5.998397,-1.008571,-2.663952,-0.811439,6.047657,-9.757931,8.178103,5.530583,6.687061,-1.212045,5.591634,-0.302832,7.501509,-7.513139,5.432634,6.676107,5.178136,9.052109,-5.675026,1.626019,8.503567,3.235355,8.356306,4.866135,3.284557,-7.352486,1.979596,-2.209728,1.798472,9.751995,4.222485,5.084440,-0.519757,8.617909,-0.449652,-3.477383,-2.932574,-1.884398,7.936572,-8.825497,1.391289,5.069656,8.046475,-6.955662,-6.361320,-4.352482,-1.282810,-4.350197,-5.140638,7.285042,-2.616854,7.301172,-1.341971,1.631235,9.425967,-1.497479,-1.594777,8.446092,-1.695318,-8.583259,-2.743961,-8.147297,-5.036439,0.712755,-5.697343,-8.530376,0.959585,2.260168,3.538003,0.656014,3.602035,-2.029356,1.388099,5.929480,0.238012,-6.399673,-1.921623,-4.669596,7.627084,-0.636996,0.605590,-8.796598,-4.598724,-7.377904,-4.966700,-1.091607,3.606804,3.786914,-2.809830,-0.587905,-4.340620,9.298760,-6.640580,-2.311379,-8.549917,2.988668,7.995485,-9.196950,-8.194327,5.673794,-1.127250,-1.279146,-6.933357,-1.580648,-0.479581,-8.071248,2.273203,-6.606121,-8.152543,5.055725,8.157134,-2.499949,-6.710806,-7.699063,7.613343,-7.274679,1.996119,8.218972,-6.709583,-4.309844,5.639712,-8.786253,7.485980,-1.933544,8.254567,-2.211976,-2.690478,8.203765,4.704803,4.770362,8.002626,-5.562684,-0.012946,6.441128,5.364197,-7.849075,-7.486937,3.505381,6.003560,4.780075,4.407682,7.694423,-1.587550,-4.726463,-4.601847,-8.515371,4.356426,-0.369055,1.648639,1.874218,4.536260,0.707313,-5.788548,3.764594,-3.384841,-4.363195,-5.598886,7.190807,-9.265252,-8.404673,-3.106344,-1.746571,0.747448,9.710615,-6.388761,7.058548,-6.525760,-9.393049,9.889868,-4.969491,-8.817399,3.773937,-0.694128,-7.695676,7.026800,4.883905,1.476154,7.853893,-1.623203,8.438760,7.997340,8.577296,5.166612,-5.630571,9.550793,-5.053702,1.172771,2.360784,1.707247,-3.205747,-9.233456,-0.177823,-8.131935,0.306485,-1.153351,4.508073,3.861369,-8.995481,-3.225626,-0.616126,6.804302,-6.780304,-1.606813,2.268146,6.864878,-1.653697,3.621389,1.275841,3.741485,1.242194,-4.061922,6.049374,1.785860,-0.908624,2.607215,8.515758,-0.802503,9.436375,5.988701,-9.847061,8.238517,0.388443,8.211507,-8.716674,7.754312,-9.928966,-8.127905,7.494210,2.574111,-0.963102,-5.502242,-2.077728,2.412318,-7.993976,-7.473740,1.093145,3.561224,-2.604894,9.215146,1.732810,-4.750874,-4.882591,-9.603608,-5.212893,-5.404599,-6.648676,2.378620,5.159977,-7.217860,5.751220,-1.358037,-8.051011,6.534778,-5.107747,2.583144,3.742558,3.770765,9.792693,-0.183821,-2.765283,-3.941758,0.231141,9.173896,-0.224853,-5.085162,-6.325176,-1.956444,0.355406,0.003118,-9.613667,6.992069,5.334506,-3.156305,-7.162749,-9.867631,3.122152,9.355610,-1.326487,1.846682,2.017087,2.234896,-9.033336,-6.001911,3.818104,0.611178,5.729826,-7.354747,2.750533,5.048670,3.577042,-2.587985,-7.784041,4.964310,-7.910512,9.668970,6.550685,7.070134,-1.566405,9.168238,-9.296516,3.530574,2.524003,-2.132536,-4.270060,9.503204,5.012934,-5.049077,9.911848,0.332008,-4.536563,6.021199,0.803259,0.711362,8.193474,0.444059,1.085658,5.569459,-2.519438,-2.082457,9.444322,-9.535266,8.544135,-5.815906,8.526038,0.280104,-0.637050,0.342510,1.285647,6.124483,8.186480,-7.115306,7.685972,8.494893,8.749251,8.155320,0.979452,-0.292369,-4.535719,-3.315289,-0.242592,-0.396939,-6.563257,-4.129033,-3.175511,-8.929416,-9.644620,1.791689,-7.956359,-6.257127,-1.861590,-3.516046,4.242547,-9.901353,7.614306,4.202455,-0.112454,-0.711596,3.984870,5.510055,-7.533966,1.247551,-1.584435,7.128918,-6.628038,8.531694,5.164343,-3.037733,-1.481369,-4.188681,0.534768,4.531854,0.444553,9.134677,-2.474503,0.818751,-1.201315,4.436036,3.878492,-1.009091,-9.292394,-2.072397,1.700156,5.128794,2.921996,-3.380628,1.020213,6.972871,2.692018,-3.114326,6.883014,0.104033,-3.628876,-7.521838,3.732615,0.305883,-9.744307,1.348999,9.645832,4.899353,-1.931816,2.267490,6.420604,2.908296,6.782350,-2.468951,9.145693,4.091077,8.293043,5.168004,-1.539471,-7.099740,-2.500045,-4.767385,-3.348086,-5.102564,7.013230,3.936874,-4.361256,-0.670739,-1.404435,-8.032126,-5.294604,0.774198,-0.225828,-0.875498,-6.645133,8.794706,-0.260126,-1.239186,-0.138758,4.677839,-1.337533,-0.272719,5.489918,9.047183,-0.390604,9.755608,5.108183,-5.665088,1.637954,-6.349213,3.210264,-6.222861,3.293228,3.912142,-6.076849,-3.741512,1.446324,7.120694,4.140401,-4.108393,6.775247,-1.939960,-1.692559,-3.419635,9.946319,1.478913,-7.185635,-8.015844,-9.186207,6.004698,-4.300198,-1.359640,6.578066,9.409684,-9.906212,-5.540991,1.343915,-3.938803,8.868701,-7.861466,1.650858,4.389590,1.603720,0.756216,3.959144,-7.264833,-6.284244,9.962784,0.862556,-9.609052,-9.769269,7.198544,2.294227,-0.951874,-0.611878,9.925909,-5.131537,8.164612,-2.624101,-2.387603,-1.869562,-8.933875,4.677600,-1.125968,-8.897881,-8.197332,5.717519,-7.791515,1.997929,3.683257,8.428091,7.026773,5.352828,-3.436834,7.904834,-2.615335,5.649543,1.285583,-5.362826,7.342492,-6.621350,-6.171725,5.370129,1.303894,9.682977,-7.474071,0.210829,-1.985354,5.677739,5.670552,6.081774,-1.270250,-0.650694,2.668167,1.960833,1.356648,-8.135784,5.819828,-8.795641,-1.901339,8.698895,4.722303,-5.683250,5.273056,-2.483255,3.417680,-1.358824,-8.406209,2.340639,-4.632500,8.184310,-0.573164,3.261931,4.962426,-7.027266,5.366178,6.710220,6.308646,-5.966275,7.160716,0.721105,7.136409,-7.771128,-6.108058,2.999489,-6.781237,-7.147199,7.777187,-0.199503,9.317864,-0.957060,-8.752251,7.257933,-1.261631,-5.046155,-5.842780,-5.702644,-1.281282,-7.381279,-9.097861,2.822016,-8.060122,9.984943,4.070168,-9.542306,1.030350,1.832791,-3.049828,6.101114,-8.408256,-9.865357,5.674171,-4.039906,3.832494,-2.062885,2.793365,-5.649509,2.092554,1.074776,5.031340,0.928398,-3.274255,-0.615943,-4.688381,3.069584,-8.964108,4.889853,-0.986603,1.050044,-5.986876,7.607187,5.273572,3.757904,-8.045125,4.795262,5.674736,-1.257035,4.432308,-8.206988,-3.922670,-8.184832,-0.613805,-7.849975,-3.923214,-5.303515,2.376821,-6.720540,-6.959931,6.940287,-0.370896,-9.578291,0.052454,8.663394,-7.509980,-2.158688,-6.215846,8.405286,7.372798,0.122640,1.518961,-5.025496,-6.659077,6.336102,4.364010,4.275396,1.599349,7.762273,-5.050199,3.205208,-1.143755,8.639824,-5.380408,6.164713,-6.422857,6.861887,9.122782,-3.458129,-8.265284,-6.123794,-1.331284,0.436973,7.905220,-4.437899,-9.728619,-3.367447,-6.382696,4.931425,-9.322027,-1.391241,2.873891,-1.111746,8.259702,-9.403070,-9.385994,8.231140,-4.733243,-5.261004,9.480965,2.961754,-6.749035,2.205880,9.475666,-0.460033,5.425412,-8.891354,-5.119391,7.118707,9.112620,-9.061364,-0.200048,-2.519896,-3.414867,4.713934,-5.235713,6.208328,-9.253022,6.967806,4.010714,-9.683108,-1.079517,-4.944615,5.571304,-5.019527,8.298213,0.518664,0.474965,8.054180,-5.234198,5.178395,7.816563,-5.821398,0.954242,-2.978031,3.021953,-6.699543,0.215086,-3.124188,-8.202102,-3.358772,9.916365,-3.527649,5.939186,9.027685,-1.305034,-9.833117,8.122588,1.522197,-3.596069,-9.897906,-7.992838,9.757233,8.652517,9.236143,5.019359,3.165825,7.512131,2.364408,7.322838,-6.292830,3.870855,-4.818757,6.772153,-8.436859,0.584187,2.589910,3.874866,6.379418,6.467932,-5.075460,-5.646702,7.906683,8.272638,1.538159,6.260309,-1.152484,-6.783296,-2.882167,7.919221,-5.602400,9.465761,-7.624694,-0.945296,9.723537,-6.732767,-8.998410,7.079524,-8.841907,-0.800968,-0.679318,-0.608636,1.955574,8.269216,-7.599212,-3.841403,8.016742,8.463246,-9.395713,8.996191,3.709704,8.008855,6.818707,6.217113,-1.001275,9.085427,-3.955925,5.747634,-2.556704,9.532162,0.035220,8.862950,3.386197,6.806092,2.554831,8.847796,-2.655794,-5.840613,2.431666,-5.728940,-7.580701,-2.548263,7.473288,-4.465257,-6.817011,-7.493991,0.701589,-3.057858,-3.865344,-4.806738,5.796304,-5.221987,-4.587582,4.281514,8.961114,6.995125,2.462647,-1.935440,-1.044963,-8.888953,-9.193252,-3.764648,0.292038,-1.559163,-2.961372,9.788401,-9.755891,-5.105301,-4.345402,-3.947705,7.242711,6.763509,-2.837002,8.984305,-5.499206,9.010607,-1.403056,-9.257363,8.116870,-5.529768,5.866049,9.266325,6.110733,6.777511,3.627471,1.967303,9.933344,3.480058,-3.739489,-9.162693,-9.686491,1.688614,-0.858828,-7.317101,-1.433997,6.339377,-1.418149,1.141275,-3.281721,-6.986465,6.033123,-9.407708,-7.979879,-3.060746,-2.260918,-3.682714,-4.117976,-5.507256,5.789621,-9.971828,5.548640,-6.488802,-8.882597,1.229094,-2.329763,-3.436265,-8.838901,-9.329294,-0.129906,1.999470,-4.629726,-4.911362,-9.162283,5.114956,7.454555,4.226258,6.698612,4.689252,-3.034342,8.595482,-1.548223,-2.932638,-3.997112,6.733798,5.219498,-6.846394,-2.636384,-7.414037,7.339493,7.741895,-2.088408,0.033273,-4.072710,7.646801,3.116358,0.960915,4.889536,-6.909775,-0.727123,-8.956773,9.982963,3.990097,0.354202,-9.335337,4.943170,-9.863754,-0.300644,-5.599283,-7.952550,3.669564,-0.135380,3.263670,-1.789740,9.793339,1.265844,-5.093345,-5.755695,1.514085,-5.071094,-1.725286,1.910983,7.514850,-8.642730,-2.181517,0.525321,2.049412,-5.838736,1.923740,-8.302339,8.419095,6.293253,-5.889604,-7.715469,2.355406,8.292523,-0.669055,-0.331228,8.179264,0.750242,5.328399,9.449801,-7.952388,9.280220,6.117552,0.693251,-4.672377,-0.658799,-2.380599,-8.094037,7.272388,-3.984083,-8.475955,9.936581,6.234900,0.219283,-6.334878,6.504980,-4.441389,-4.262775,9.572709,-4.777425,-3.956900,-6.665387,8.034171,7.685049,5.248120,7.050026,-8.779796,0.191907,1.952262,7.572256,8.146614,9.546326,6.615898,7.056611,3.782488,-5.074005,8.977262,-6.768735,1.679166,7.247016,2.229173,-8.724745,-8.383527,-9.593984,-0.393861,4.449938,-5.190223,0.526117,-4.891518,-9.207175,4.771379,-1.225221,-5.797457,6.397647,-8.006241,-3.500419,1.391855,4.333333,-5.584154,-5.817019,2.900820,-2.082610,-8.272554,-1.560833,3.390923,-9.088841,6.993547,0.705834,5.752194,-6.707797,2.888232,-3.775853,9.450862,-1.656407,5.840875,2.512151,-3.788960,-9.913148,4.162588,-9.248357,-0.582770,1.579098,6.702362,1.638827,-2.305818,-8.480214,-2.845069,-9.934169,-0.860403,8.462669,9.655319,0.773519,-9.462710,-7.021110,-9.270345,-5.236094,5.103665,-2.448828,-5.526588,-4.988098,3.158712,9.209360,3.435845,-4.406065,-6.056754,2.596774,-7.132008,-5.245902,-3.787624,-1.102694,6.035003,5.487351,8.792988,1.406271,0.980458,-3.364994,-8.343723,-6.120910,4.828838,7.362703,-5.864106,-7.198960,5.901648,-2.956911,7.725844,-0.315561,2.129162,-0.664944,-8.034445,4.296044,2.691975,-6.781837,9.832697,0.840228,5.199412,-0.802297,6.364039,-3.931890,9.277313,-2.666978,-1.085276,4.066898,5.823929,-8.182733,0.744371,3.833234,8.167743,-9.059357,2.991718,3.316934,8.122794,-1.325902,-8.885024,3.192083,9.043727,1.310974,5.711148,-5.164389,-3.468418,-3.407251,-9.632337,-8.300378,2.949740,-6.387495,-4.043275,-9.203246,7.289910,-9.683168,5.958567,-5.664894,0.122659,-5.581312,-5.675393,7.465719,3.374266,2.191150,-1.455662,5.452537,-5.251649,-8.486567,-1.586495,-8.691221,5.036296,3.398470,9.629383,-7.563949,2.798293,9.479958,7.467496,-4.704805,-1.612025,-8.992746,6.751973,-7.103703,8.593588,-2.758225,6.706978,4.199249,3.536507,-7.117561,-5.980827,-6.761762,4.057953,-3.082447,-7.446631,-2.663297,-3.654187,2.691930,-8.561601,0.428215,-6.668953,1.475292,8.921345,1.437897,-1.059313,7.376610,-8.059103,-0.693623,3.868933,-2.570977,-7.764690,-7.250946,3.302724,-8.922003,9.419731,3.465807,-9.714801,-9.692295,1.416519,-5.031371,5.678777,5.274670,8.942904,8.668005,-7.021142,2.707140,-9.317140,4.846551,8.544461,-6.253218,8.182637,2.365893,-4.789658,0.253737,1.916119,1.074968,1.588665,-2.110322,4.592941,3.522272,4.265856,-7.798066,-3.312811,5.263299,8.584045,2.374007,9.231186,-8.019340,-3.263534,3.179931,-6.860974,-9.247068,4.188682,-2.784157,-6.234630,-2.322149,-0.234440,-0.305504,-2.517990,2.999829,8.513362,2.226286,1.968117,-4.208088,7.203447,1.096523,0.480282,-1.310839,-6.773363,6.854817,-3.058173,-2.261686,-9.070899,-1.597310,-1.078127,-0.881929,-3.782774,-0.048471,-0.978644,2.066545,-6.931111,6.198961,-0.300380,0.355435,-7.909148,1.280326,-4.223791,-3.577827,-3.063559,-6.866781,-4.709472,-3.316344,-3.390389,-2.208831,-8.307202,-3.971968,-3.673746,-1.241129,6.513969,6.054113,-1.117435,0.752070,-2.564205,5.758353,-8.848945,0.745801,-7.894449,8.704131,-2.780892,6.742925,0.075231,1.818079,3.278809,-7.859979,8.212200,0.035300,-6.307360,0.968025,-9.929842,-1.506433,-9.635421,8.023118,6.805572,7.878202,-5.977402,-1.066557,-3.302221,6.989346,8.066003,1.346228,1.762602,-4.205249,5.289895,-6.711740,-3.360737,-0.275230,-4.658688,-2.847153,-5.839426,9.445085,-4.525396,-7.088016,6.646765,1.206288,4.978958,-0.194457,7.392076,-1.993995,-9.750423,-9.950024,1.288534,8.471503,-4.665587,-9.329760,9.640086,2.435813,4.151515,-1.775493,9.736924], dtype = "float64")#candidate|6401|(1456,)|const|float64
var_6402 = relay.var("var_6402", dtype = "int32", shape = (1, 1056))#candidate|6402|(1, 1056)|var|int32
const_6403 = relay.const([[0.318130,8.452494,6.427991,-3.764727,-9.760430,4.154381,5.898006,2.431031,1.049516,6.824348,8.404462,-7.876719,9.986294,7.245849,8.190052,-4.019813,7.416363,5.581282,9.956106,-4.413866,4.233569,4.561805,0.313057,2.644195,2.359084,-9.547636,-5.065456,4.080338,-2.267877,-4.016979,-3.762453,-5.868848,-5.867061,-0.113340,9.642448]], dtype = "float64")#candidate|6403|(1, 35)|const|float64
call_6400 = relay.TupleGetItem(func_4945_call(relay.reshape(const_6401.astype('float64'), [1456,]), relay.reshape(var_6402.astype('int32'), [528, 2]), relay.reshape(const_6403.astype('float64'), [35,]), ), 8)
call_6404 = relay.TupleGetItem(func_4949_call(relay.reshape(const_6401.astype('float64'), [1456,]), relay.reshape(var_6402.astype('int32'), [528, 2]), relay.reshape(const_6403.astype('float64'), [35,]), ), 8)
bop_6405 = relay.add(var_6393.astype('int32'), call_6400.astype('int32')) # shape=(7, 5, 39)
bop_6408 = relay.add(var_6393.astype('int32'), call_6404.astype('int32')) # shape=(7, 5, 39)
output = relay.Tuple([call_6371,call_6392,var_6394,bop_6397,const_6401,var_6402,const_6403,bop_6405,])
output2 = relay.Tuple([call_6372,call_6395,var_6394,bop_6397,const_6401,var_6402,const_6403,bop_6408,])
func_6433 = relay.Function([var_6393,var_6394,var_6396,var_6402,], output)
mod['func_6433'] = func_6433
mod = relay.transform.InferType()(mod)
var_6434 = relay.var("var_6434", dtype = "float64", shape = (39,))#candidate|6434|(39,)|var|float64
var_6435 = relay.var("var_6435", dtype = "int64", shape = (616,))#candidate|6435|(616,)|var|int64
var_6436 = relay.var("var_6436", dtype = "float64", shape = (39,))#candidate|6436|(39,)|var|float64
var_6437 = relay.var("var_6437", dtype = "int32", shape = (1, 1056))#candidate|6437|(1, 1056)|var|int32
output = func_6433(var_6434,var_6435,var_6436,var_6437,)
func_6438 = relay.Function([var_6434,var_6435,var_6436,var_6437,], output)
mutated_mod['func_6438'] = func_6438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6130_call = mod.get_global_var('func_6130')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_6471 = func_6130_call()
call_6472 = func_6130_call()
output = call_6471
output2 = call_6472
func_6491 = relay.Function([], output)
mod['func_6491'] = func_6491
mod = relay.transform.InferType()(mod)
output = func_6491()
func_6492 = relay.Function([], output)
mutated_mod['func_6492'] = func_6492
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_6493 = relay.TupleGetItem(func_5383_call(), 1)
call_6494 = relay.TupleGetItem(func_5385_call(), 1)
output = call_6493
output2 = call_6494
func_6500 = relay.Function([], output)
mod['func_6500'] = func_6500
mod = relay.transform.InferType()(mod)
mutated_mod['func_6500'] = func_6500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6500_call = mutated_mod.get_global_var('func_6500')
call_6501 = func_6500_call()
output = call_6501
func_6502 = relay.Function([], output)
mutated_mod['func_6502'] = func_6502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_6547 = func_5024_call()
call_6548 = func_5024_call()
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_6586 = relay.TupleGetItem(func_5900_call(), 0)
call_6587 = relay.TupleGetItem(func_5901_call(), 0)
var_6594 = relay.var("var_6594", dtype = "float32", shape = (14, 5, 13))#candidate|6594|(14, 5, 13)|var|float32
bop_6595 = relay.bitwise_and(call_6586.astype('int8'), relay.reshape(var_6594.astype('int8'), relay.shape_of(call_6586))) # shape=(14, 5, 13)
bop_6598 = relay.bitwise_and(call_6587.astype('int8'), relay.reshape(var_6594.astype('int8'), relay.shape_of(call_6587))) # shape=(14, 5, 13)
output = relay.Tuple([call_6547,bop_6595,])
output2 = relay.Tuple([call_6548,bop_6598,])
func_6631 = relay.Function([var_6594,], output)
mod['func_6631'] = func_6631
mod = relay.transform.InferType()(mod)
mutated_mod['func_6631'] = func_6631
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6632 = relay.var("var_6632", dtype = "float32", shape = (14, 5, 13))#candidate|6632|(14, 5, 13)|var|float32
func_6631_call = mutated_mod.get_global_var('func_6631')
call_6633 = func_6631_call(var_6632)
output = call_6633
func_6634 = relay.Function([var_6632], output)
mutated_mod['func_6634'] = func_6634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5257_call = mod.get_global_var('func_5257')
func_5259_call = mutated_mod.get_global_var('func_5259')
call_6639 = relay.TupleGetItem(func_5257_call(), 0)
call_6640 = relay.TupleGetItem(func_5259_call(), 0)
func_5269_call = mod.get_global_var('func_5269')
func_5271_call = mutated_mod.get_global_var('func_5271')
call_6658 = relay.TupleGetItem(func_5269_call(), 0)
call_6659 = relay.TupleGetItem(func_5271_call(), 0)
func_2563_call = mod.get_global_var('func_2563')
func_2567_call = mutated_mod.get_global_var('func_2567')
var_6667 = relay.var("var_6667", dtype = "uint8", shape = (8, 182))#candidate|6667|(8, 182)|var|uint8
var_6668 = relay.var("var_6668", dtype = "uint64", shape = (1344,))#candidate|6668|(1344,)|var|uint64
var_6669 = relay.var("var_6669", dtype = "float64", shape = (140, 1))#candidate|6669|(140, 1)|var|float64
call_6666 = relay.TupleGetItem(func_2563_call(relay.reshape(var_6667.astype('uint8'), [13, 7, 16]), relay.reshape(var_6668.astype('uint64'), [672, 2]), relay.reshape(var_6669.astype('float64'), [7, 5, 4]), ), 0)
call_6670 = relay.TupleGetItem(func_2567_call(relay.reshape(var_6667.astype('uint8'), [13, 7, 16]), relay.reshape(var_6668.astype('uint64'), [672, 2]), relay.reshape(var_6669.astype('float64'), [7, 5, 4]), ), 0)
uop_6681 = relay.log2(var_6667.astype('float32')) # shape=(8, 182)
output = relay.Tuple([call_6639,call_6658,call_6666,var_6668,var_6669,uop_6681,])
output2 = relay.Tuple([call_6640,call_6659,call_6670,var_6668,var_6669,uop_6681,])
func_6686 = relay.Function([var_6667,var_6668,var_6669,], output)
mod['func_6686'] = func_6686
mod = relay.transform.InferType()(mod)
mutated_mod['func_6686'] = func_6686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6686_call = mutated_mod.get_global_var('func_6686')
var_6688 = relay.var("var_6688", dtype = "uint8", shape = (8, 182))#candidate|6688|(8, 182)|var|uint8
var_6689 = relay.var("var_6689", dtype = "uint64", shape = (1344,))#candidate|6689|(1344,)|var|uint64
var_6690 = relay.var("var_6690", dtype = "float64", shape = (140, 1))#candidate|6690|(140, 1)|var|float64
call_6687 = func_6686_call(var_6688,var_6689,var_6690,)
output = call_6687
func_6691 = relay.Function([var_6688,var_6689,var_6690,], output)
mutated_mod['func_6691'] = func_6691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6500_call = mod.get_global_var('func_6500')
func_6502_call = mutated_mod.get_global_var('func_6502')
call_6756 = func_6500_call()
call_6757 = func_6500_call()
output = relay.Tuple([call_6756,])
output2 = relay.Tuple([call_6757,])
func_6758 = relay.Function([], output)
mod['func_6758'] = func_6758
mod = relay.transform.InferType()(mod)
mutated_mod['func_6758'] = func_6758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6758_call = mutated_mod.get_global_var('func_6758')
call_6759 = func_6758_call()
output = call_6759
func_6760 = relay.Function([], output)
mutated_mod['func_6760'] = func_6760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_6803 = func_5024_call()
call_6804 = func_5024_call()
uop_6807 = relay.cos(call_6803.astype('float64')) # shape=(14, 5, 13)
uop_6809 = relay.cos(call_6804.astype('float64')) # shape=(14, 5, 13)
func_6491_call = mod.get_global_var('func_6491')
func_6492_call = mutated_mod.get_global_var('func_6492')
call_6810 = func_6491_call()
call_6811 = func_6491_call()
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_6821 = relay.TupleGetItem(func_4410_call(), 0)
call_6822 = relay.TupleGetItem(func_4412_call(), 0)
output = relay.Tuple([uop_6807,call_6810,call_6821,])
output2 = relay.Tuple([uop_6809,call_6811,call_6822,])
func_6827 = relay.Function([], output)
mod['func_6827'] = func_6827
mod = relay.transform.InferType()(mod)
output = func_6827()
func_6828 = relay.Function([], output)
mutated_mod['func_6828'] = func_6828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_6911 = func_4666_call()
call_6912 = func_4666_call()
output = relay.Tuple([call_6911,])
output2 = relay.Tuple([call_6912,])
func_6927 = relay.Function([], output)
mod['func_6927'] = func_6927
mod = relay.transform.InferType()(mod)
mutated_mod['func_6927'] = func_6927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6927_call = mutated_mod.get_global_var('func_6927')
call_6928 = func_6927_call()
output = call_6928
func_6929 = relay.Function([], output)
mutated_mod['func_6929'] = func_6929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6927_call = mod.get_global_var('func_6927')
func_6929_call = mutated_mod.get_global_var('func_6929')
call_6951 = relay.TupleGetItem(func_6927_call(), 0)
call_6952 = relay.TupleGetItem(func_6929_call(), 0)
output = relay.Tuple([call_6951,])
output2 = relay.Tuple([call_6952,])
func_6956 = relay.Function([], output)
mod['func_6956'] = func_6956
mod = relay.transform.InferType()(mod)
output = func_6956()
func_6957 = relay.Function([], output)
mutated_mod['func_6957'] = func_6957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_6995 = func_4666_call()
call_6996 = func_4666_call()
output = call_6995
output2 = call_6996
func_6997 = relay.Function([], output)
mod['func_6997'] = func_6997
mod = relay.transform.InferType()(mod)
mutated_mod['func_6997'] = func_6997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6997_call = mutated_mod.get_global_var('func_6997')
call_6998 = func_6997_call()
output = call_6998
func_6999 = relay.Function([], output)
mutated_mod['func_6999'] = func_6999
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_7044 = relay.TupleGetItem(func_4410_call(), 0)
call_7045 = relay.TupleGetItem(func_4412_call(), 0)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_7047 = relay.TupleGetItem(func_5383_call(), 1)
call_7048 = relay.TupleGetItem(func_5385_call(), 1)
output = relay.Tuple([call_7044,call_7047,])
output2 = relay.Tuple([call_7045,call_7048,])
func_7049 = relay.Function([], output)
mod['func_7049'] = func_7049
mod = relay.transform.InferType()(mod)
output = func_7049()
func_7050 = relay.Function([], output)
mutated_mod['func_7050'] = func_7050
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_7072 = relay.TupleGetItem(func_5383_call(), 0)
call_7073 = relay.TupleGetItem(func_5385_call(), 0)
func_5342_call = mod.get_global_var('func_5342')
func_5345_call = mutated_mod.get_global_var('func_5345')
var_7083 = relay.var("var_7083", dtype = "float64", shape = (39,))#candidate|7083|(39,)|var|float64
const_7084 = relay.const([5,-6,-2,7,-10,5,-2,5,5,6,4,-4,-5,7,-8,-6,4,1,-8,-3,5,-6,-10,6,7,-1,10,-5,-6,4,7,-6,10,7,6,-8,10,9,-7,5,-9,-4,4,5,2,-5,-1,-9,10,1,-6,8,-5,7,-4,-5,-9,-1,8,4,-7,-10,3,1,5,-1,3,6,8,1,6,-2,-4,-9,-1,4,-3,8,2,-9,-3,8,10,5,9,-8,1,9,5,8,10,-7,4,9,7,3,-8,6,-6,6,9,2,7,5,-1,9,-5,-6,-2,-7,5,-8,2,3,-7,5,4,-5,-9,3,5,3,10,9,6,-2,-5,-6,-4,-4,7,-6,7,1,6,-7,-8,1,10,2,7,9,-4,-8,3,9,3,2,-1,-9,-7,-7,9,-4,9,6,-10,7,-1,2,9,5,-9,6,-10,-6,-1,3,-3,8,-3,-6,-1,-8,-8,-6,4,-10,8,2,3,4,-2,-6,4,-5,-10,1,-3,-2,9,-9,9,5,-9,5,4,-6,6,1,5,6,-6,7,-8,-4,8,10,-7,7,2,6,1,6,1,7,1,1,2,1,-6,-7,-8,-4,-3,-9,-10,5,-6,-1,6,2,5,9,3,7,2,-6,2,5,8,4,-8,3,10,10,-4,-5,8,-6,1,2,9,4,-9,-1,-3,-7,4,5,-4,7,-9,-6,-6,10,8,-1,-2,-2,-3,8,-8,7,4,3,6,7,4,-4,6,10,-8,2,-7,10,7,-6,-4,-4,-4,8,9,-7,7,-5,-5,-8,5,2,-2,2,10,-2,-2,3,-5,7,-6,-9,6,-7,-9,4,5,-8,8,-6,-9,-5,7,6,-8,-8,-7,-9,-2,-4,3,7,-5,5,-6,-4,-9,5,-6,2,3,-10,6,5,-8,-9,8,7,2,9,-2,4,-1,-9,-1,10,-10,6,10,4,-2,-8,-10,6,-6,-3,-7,2,-7,4,2,3,6,10,3,-5,8,7,-6,-3,7,3,-2,-1,-5,-6,-9,-1,-8,-1,6,6,-7,1,6,-10,-9,-7,7,9,-1,1,5,4,-4,6,1,1,5,-3,-5,3,5,4,-6,-2,-1,6,6,3,5,7,3,1,-1,10,7,-1,-3,-2,9,5,-10,9,-3,3,2,-1,9,5,-8,5,8,8,10,-10,8,10,8,-2,-2,8,-7,10,-3,-4,-2,8,5,-1,8,6,9,-5,-7,-10,4,-2,-9,6,9,-2,-1,1,6,2,5,3,-6,-5,-5,-2,4,-9,8,2,-7,6,-5,-5,1,9,7,-10,-8,6,9,-2,1,6,7,7,-4,-4,-2,-4,-8,6,4,-8,2,-4,1,-6,7,2,-1,2,1,-8,6,-5,4,-10,1,9,-2,-6,10,5,-5,-3,-5,-4,2,-9,-4,3,-8,-4,-10,2,-7,5,10,5,7,2,7,-8,7,-7,2,9,-4,-10,-6,-8,-9,-10,-3,4,7,1,3,-10,7,-3,9,10,3,-10,2,-1,1,2,6,-5,4,-4,-7,9,-6,-4,4,-8,6,9,-6,-9,-10,2,-8,1,-6,9,3,-5,2,-4,3,-7,-2,7,7,-6,8,4,-8,8,-2,-5,-6,-2,2,-9,7,-6], dtype = "int64")#candidate|7084|(616,)|const|int64
call_7082 = relay.TupleGetItem(func_5342_call(relay.reshape(var_7083.astype('float64'), [3, 1, 13]), relay.reshape(const_7084.astype('int64'), [616,]), ), 1)
call_7085 = relay.TupleGetItem(func_5345_call(relay.reshape(var_7083.astype('float64'), [3, 1, 13]), relay.reshape(const_7084.astype('int64'), [616,]), ), 1)
var_7091 = relay.var("var_7091", dtype = "float64", shape = (39,))#candidate|7091|(39,)|var|float64
bop_7092 = relay.logical_and(var_7083.astype('bool'), relay.reshape(var_7091.astype('bool'), relay.shape_of(var_7083))) # shape=(39,)
output = relay.Tuple([call_7072,call_7082,const_7084,bop_7092,])
output2 = relay.Tuple([call_7073,call_7085,const_7084,bop_7092,])
func_7108 = relay.Function([var_7083,var_7091,], output)
mod['func_7108'] = func_7108
mod = relay.transform.InferType()(mod)
var_7109 = relay.var("var_7109", dtype = "float64", shape = (39,))#candidate|7109|(39,)|var|float64
var_7110 = relay.var("var_7110", dtype = "float64", shape = (39,))#candidate|7110|(39,)|var|float64
output = func_7108(var_7109,var_7110,)
func_7111 = relay.Function([var_7109,var_7110,], output)
mutated_mod['func_7111'] = func_7111
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4777_call = mod.get_global_var('func_4777')
func_4778_call = mutated_mod.get_global_var('func_4778')
call_7131 = func_4777_call()
call_7132 = func_4777_call()
output = relay.Tuple([call_7131,])
output2 = relay.Tuple([call_7132,])
func_7157 = relay.Function([], output)
mod['func_7157'] = func_7157
mod = relay.transform.InferType()(mod)
output = func_7157()
func_7158 = relay.Function([], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5604_call = mod.get_global_var('func_5604')
func_5606_call = mutated_mod.get_global_var('func_5606')
call_7161 = relay.TupleGetItem(func_5604_call(), 0)
call_7162 = relay.TupleGetItem(func_5606_call(), 0)
output = call_7161
output2 = call_7162
func_7163 = relay.Function([], output)
mod['func_7163'] = func_7163
mod = relay.transform.InferType()(mod)
mutated_mod['func_7163'] = func_7163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7163_call = mutated_mod.get_global_var('func_7163')
call_7164 = func_7163_call()
output = call_7164
func_7165 = relay.Function([], output)
mutated_mod['func_7165'] = func_7165
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5961_call = mod.get_global_var('func_5961')
func_5962_call = mutated_mod.get_global_var('func_5962')
call_7224 = func_5961_call()
call_7225 = func_5961_call()
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_7229 = relay.TupleGetItem(func_4612_call(), 0)
call_7230 = relay.TupleGetItem(func_4614_call(), 0)
output = relay.Tuple([call_7224,call_7229,])
output2 = relay.Tuple([call_7225,call_7230,])
func_7238 = relay.Function([], output)
mod['func_7238'] = func_7238
mod = relay.transform.InferType()(mod)
output = func_7238()
func_7239 = relay.Function([], output)
mutated_mod['func_7239'] = func_7239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7157_call = mod.get_global_var('func_7157')
func_7158_call = mutated_mod.get_global_var('func_7158')
call_7240 = relay.TupleGetItem(func_7157_call(), 0)
call_7241 = relay.TupleGetItem(func_7158_call(), 0)
output = relay.Tuple([call_7240,])
output2 = relay.Tuple([call_7241,])
func_7242 = relay.Function([], output)
mod['func_7242'] = func_7242
mod = relay.transform.InferType()(mod)
output = func_7242()
func_7243 = relay.Function([], output)
mutated_mod['func_7243'] = func_7243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7277 = relay.var("var_7277", dtype = "int16", shape = (15, 7, 2))#candidate|7277|(15, 7, 2)|var|int16
const_7278 = relay.const([[[5,2],[10,4],[-2,3],[2,5],[-1,-10],[8,6],[9,6]],[[4,-3],[-3,1],[-4,9],[9,-3],[3,-3],[-4,-9],[-6,10]],[[8,-7],[-3,-1],[7,2],[-10,5],[-2,-2],[-8,-9],[-10,5]],[[-1,1],[-3,4],[-9,4],[9,-7],[-6,8],[-3,-3],[7,-3]],[[10,1],[5,3],[-10,-7],[1,7],[9,9],[-8,-3],[9,-4]],[[-8,3],[9,1],[8,3],[10,9],[3,-3],[1,8],[-1,2]],[[9,-8],[7,6],[9,-9],[3,7],[3,-9],[5,9],[-4,-7]],[[7,4],[-7,2],[-8,-9],[8,-6],[-9,-8],[-10,-1],[9,-2]],[[4,-7],[-1,9],[-5,-4],[-1,-10],[1,4],[8,4],[-9,6]],[[2,10],[-7,9],[7,-8],[8,5],[-4,-10],[2,5],[-6,-9]],[[-4,4],[3,4],[-10,-10],[10,9],[-9,-9],[3,8],[-5,-5]],[[-1,-5],[-9,1],[-2,4],[7,-9],[1,6],[6,4],[7,3]],[[4,3],[4,10],[-9,-7],[-3,3],[6,-8],[-1,8],[-2,-7]],[[4,-2],[-9,6],[3,7],[5,2],[-7,-8],[8,2],[10,7]],[[4,-2],[-3,9],[-9,3],[10,-3],[6,-3],[-2,-7],[-8,-10]]], dtype = "int16")#candidate|7278|(15, 7, 2)|const|int16
bop_7279 = relay.greater_equal(var_7277.astype('bool'), relay.reshape(const_7278.astype('bool'), relay.shape_of(var_7277))) # shape=(15, 7, 2)
output = bop_7279
output2 = bop_7279
func_7287 = relay.Function([var_7277,], output)
mod['func_7287'] = func_7287
mod = relay.transform.InferType()(mod)
var_7288 = relay.var("var_7288", dtype = "int16", shape = (15, 7, 2))#candidate|7288|(15, 7, 2)|var|int16
output = func_7287(var_7288)
func_7289 = relay.Function([var_7288], output)
mutated_mod['func_7289'] = func_7289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4777_call = mod.get_global_var('func_4777')
func_4778_call = mutated_mod.get_global_var('func_4778')
call_7358 = func_4777_call()
call_7359 = func_4777_call()
output = relay.Tuple([call_7358,])
output2 = relay.Tuple([call_7359,])
func_7381 = relay.Function([], output)
mod['func_7381'] = func_7381
mod = relay.transform.InferType()(mod)
mutated_mod['func_7381'] = func_7381
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7381_call = mutated_mod.get_global_var('func_7381')
call_7382 = func_7381_call()
output = call_7382
func_7383 = relay.Function([], output)
mutated_mod['func_7383'] = func_7383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_7412 = relay.TupleGetItem(func_5146_call(), 0)
call_7413 = relay.TupleGetItem(func_5148_call(), 0)
func_6130_call = mod.get_global_var('func_6130')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_7428 = func_6130_call()
call_7429 = func_6130_call()
func_6130_call = mod.get_global_var('func_6130')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_7447 = func_6130_call()
call_7448 = func_6130_call()
uop_7457 = relay.exp(call_7447.astype('float32')) # shape=(14, 5, 13)
uop_7459 = relay.exp(call_7448.astype('float32')) # shape=(14, 5, 13)
func_5269_call = mod.get_global_var('func_5269')
func_5271_call = mutated_mod.get_global_var('func_5271')
call_7471 = relay.TupleGetItem(func_5269_call(), 0)
call_7472 = relay.TupleGetItem(func_5271_call(), 0)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_7476 = func_4666_call()
call_7477 = func_4666_call()
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_7494 = relay.TupleGetItem(func_4612_call(), 0)
call_7495 = relay.TupleGetItem(func_4614_call(), 0)
output = relay.Tuple([call_7412,call_7428,uop_7457,call_7471,call_7476,call_7494,])
output2 = relay.Tuple([call_7413,call_7429,uop_7459,call_7472,call_7477,call_7495,])
func_7502 = relay.Function([], output)
mod['func_7502'] = func_7502
mod = relay.transform.InferType()(mod)
output = func_7502()
func_7503 = relay.Function([], output)
mutated_mod['func_7503'] = func_7503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6758_call = mod.get_global_var('func_6758')
func_6760_call = mutated_mod.get_global_var('func_6760')
call_7518 = relay.TupleGetItem(func_6758_call(), 0)
call_7519 = relay.TupleGetItem(func_6760_call(), 0)
func_4743_call = mod.get_global_var('func_4743')
func_4747_call = mutated_mod.get_global_var('func_4747')
var_7523 = relay.var("var_7523", dtype = "uint32", shape = ())#candidate|7523|()|var|uint32
var_7524 = relay.var("var_7524", dtype = "uint32", shape = (4,))#candidate|7524|(4,)|var|uint32
call_7522 = relay.TupleGetItem(func_4743_call(relay.reshape(var_7523.astype('uint32'), []), relay.reshape(var_7524.astype('uint32'), [4,]), ), 5)
call_7525 = relay.TupleGetItem(func_4747_call(relay.reshape(var_7523.astype('uint32'), []), relay.reshape(var_7524.astype('uint32'), [4,]), ), 5)
output = relay.Tuple([call_7518,call_7522,var_7523,var_7524,])
output2 = relay.Tuple([call_7519,call_7525,var_7523,var_7524,])
func_7526 = relay.Function([var_7523,var_7524,], output)
mod['func_7526'] = func_7526
mod = relay.transform.InferType()(mod)
mutated_mod['func_7526'] = func_7526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7526_call = mutated_mod.get_global_var('func_7526')
var_7528 = relay.var("var_7528", dtype = "uint32", shape = ())#candidate|7528|()|var|uint32
var_7529 = relay.var("var_7529", dtype = "uint32", shape = (4,))#candidate|7529|(4,)|var|uint32
call_7527 = func_7526_call(var_7528,var_7529,)
output = call_7527
func_7530 = relay.Function([var_7528,var_7529,], output)
mutated_mod['func_7530'] = func_7530
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_7562 = relay.TupleGetItem(func_4849_call(), 0)
call_7563 = relay.TupleGetItem(func_4850_call(), 0)
output = relay.Tuple([call_7562,])
output2 = relay.Tuple([call_7563,])
func_7566 = relay.Function([], output)
mod['func_7566'] = func_7566
mod = relay.transform.InferType()(mod)
mutated_mod['func_7566'] = func_7566
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7566_call = mutated_mod.get_global_var('func_7566')
call_7567 = func_7566_call()
output = call_7567
func_7568 = relay.Function([], output)
mutated_mod['func_7568'] = func_7568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7502_call = mod.get_global_var('func_7502')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_7600 = relay.TupleGetItem(func_7502_call(), 3)
call_7601 = relay.TupleGetItem(func_7503_call(), 3)
func_4445_call = mod.get_global_var('func_4445')
func_4448_call = mutated_mod.get_global_var('func_4448')
const_7612 = relay.const([-6.615462,-5.712914,-3.488550,-5.835402,4.030453,4.755191,7.056116,6.249602,-9.519063,-8.023839,7.206104,6.056094,-5.057952,-7.439261,-1.712272,-2.387166,-4.916547,2.245161,-1.135233,-1.580950,0.012397,0.426144,0.173032,5.569838,8.968197,5.665796,5.607211,5.083247,6.130122,-4.920966,6.609793,1.797589,9.431108,-1.243893,-8.263654,-5.177122,-9.175486,-8.155683,-8.795613,0.689665,3.847058,2.959673,-3.154917,-8.312925,-6.722856,2.985393,-0.220427,7.350956,-1.623681,0.963565,4.304109,-8.530471,-2.671508,4.104095,-3.196873,-6.517583,-0.931553,5.418958,3.260240,-8.013536,-4.171503,7.294430,-1.410927,-6.255174,7.323172,6.129208,0.809038,-9.181022,-7.730498,2.401663,3.458080,-7.420924,9.023402,-5.104607,-5.845033,-4.313088,-6.192050,9.153896,5.328069,4.951389,8.923620,6.975314,4.466007,-0.733310,8.157300,-6.826242,-2.993336,-2.137571,-7.745509,-5.877190,-7.523768,5.668956,-4.556863,9.180345,7.370889,-6.892909,-6.638376,8.617602,-8.379859,8.837216,8.548583,-4.728002,2.770417,0.026580,5.805099,-4.572158,6.823961,-0.421593,-0.802493,8.222976,6.230742,-8.865903,0.483428,4.678161,-3.418036,6.430429,-0.558094,4.547151,0.905811,-7.893330,-1.534797,-4.839126,-2.515238,0.977726,-5.511867,-9.041531,5.879432,0.610932,5.305038,-3.905644,-3.838063,9.751280,5.101892,-1.866241,-2.074458,6.615874,7.066452,-2.044922,-9.107399,-1.454044,-9.113551,-1.752067,5.853924,-6.836641,-7.770547,-2.887592,-5.811461,-1.719456,-7.694724,-9.431457,0.364159,3.170266,4.569431,-7.196271,-9.108890,1.925701,-8.576359,-0.070428,0.325235,-7.963249,3.679827,-5.022790,-9.319279,7.868473,9.571379,6.400605,8.512917,3.915107,-9.766877,-7.420871,-6.961693,9.171909,-4.239763,5.845826,-4.734248,8.230939,-4.035041,-9.405947,-2.451530,-7.190128,2.904446,-2.168548,-9.060485,-5.539517,-5.895929,4.618858,-5.030638,2.317495,-0.598811,-5.111399,-1.285758,-6.182490,-9.990800,9.945898,-1.434331,-6.309902,-3.446640,-5.106445,6.096002,1.671111,-2.097210,-2.084684,-0.832594,6.605878,-0.868646,3.971499,5.224596,-5.854059,-0.280504,9.606379,1.617927,5.582991,-7.311540,-2.682856,-9.184577,2.531439,1.867804,9.129480,2.506550,-6.229506,-8.103951,-8.055941,-6.174969,1.792190,5.597264,6.351490,5.789040,-4.812435,6.866470,1.561325,-9.075388,-3.670521,-9.562672,6.447663,-7.499666,-6.832663,-1.557521,-9.118141,7.340118,6.606601,-2.479504,1.666976,1.571114,-0.440177,-3.456055,-2.527999,-9.926289,-1.038732,-5.139042,5.010962,-2.537756,-6.858006,-3.444701,4.111834,-0.626145,-5.885538,7.958543,-6.350667,4.619321,1.755591,-8.398501,2.122065,-9.807988,-3.139265,6.717146,6.542203,1.797879,-7.081089,1.661366,8.549978,2.531581,-0.037160,1.207125,4.628158,3.947375,-0.447067,0.925932,4.827160,-4.618200,-4.303449,0.332664,3.784109,4.993276,-6.736748,2.910186,7.960194,-6.412346,4.914841,-8.891995,-6.838923,-1.037271,-0.445760,-8.640882,1.368360,1.909574,4.117249,-0.045922,2.947217,-7.244938,-4.427649,2.878611,-7.162602,9.895345,5.994966,4.968471,-9.966906,-9.050179,6.713256,-1.672098,1.220480,-3.328396,-2.045365,0.218264,6.052919,5.504027,8.038506,7.936728,-3.079252,-6.014455,-6.814535,-6.664410,3.018246,6.196379,3.276644,8.618924,0.812445,4.001627,-5.653058,2.841117,1.492657,2.168830,4.374063,-8.045238,-4.802250,4.609825,-8.841582,8.834543,7.696472,-6.224860,-1.058509,4.886980,-6.955752,2.237894,-6.055567,-8.495434,2.428368,-6.426603,-4.197495,5.078998,8.456135,6.916299,-2.575863,0.081850,-4.799599,-4.727384,-3.927014,-9.672694,3.924829,0.431890,9.470275,3.073064,-2.319281,8.946899,-4.226997,8.601310,-8.612318,-7.821266,3.686868,-4.649483,9.930615,-9.093512,-6.224342,-6.771978,-8.292805,7.838585,5.489223,-3.459193,7.784389,-0.660996,-5.880396,8.477718,1.992318,8.877998,-8.562734,-1.977611,8.785441,0.714228,5.943551,6.921186,8.996323,1.612565,0.667590,-0.542019,-8.565011,-9.290099,-1.713294,6.521617,4.193859,-9.912478,-7.541482,-4.486840,5.461001,4.840753,6.330386,-9.466840,-2.482061,-9.132677,-7.676353,-4.986776,3.937653,2.861571,-3.122838,4.830613,-3.597686,6.891408,-6.770430,-0.572530,7.571860,9.570101,-1.358009,-2.959928,2.941597,-6.664357,0.078576,-1.680548,0.780069,6.609784,-4.733706,-3.195580,-4.434190,3.638841,4.140953,1.586404,-0.155590,3.839927,-2.181835,6.024570,-3.552653,2.863660,-5.312770,4.473322,-9.676001,8.206376,5.813771,5.479585,-9.159018,1.326717,-9.574057,-8.474422,1.572872], dtype = "float64")#candidate|7612|(450,)|const|float64
call_7611 = relay.TupleGetItem(func_4445_call(relay.reshape(const_7612.astype('float64'), [450,])), 2)
call_7613 = relay.TupleGetItem(func_4448_call(relay.reshape(const_7612.astype('float64'), [450,])), 2)
func_559_call = mod.get_global_var('func_559')
func_563_call = mutated_mod.get_global_var('func_563')
var_7625 = relay.var("var_7625", dtype = "uint32", shape = ())#candidate|7625|()|var|uint32
const_7626 = relay.const([-10,10,-5,8], dtype = "uint32")#candidate|7626|(4,)|const|uint32
call_7624 = func_559_call(relay.reshape(var_7625.astype('uint32'), []), relay.reshape(const_7626.astype('uint32'), [1, 4]), )
call_7627 = func_559_call(relay.reshape(var_7625.astype('uint32'), []), relay.reshape(const_7626.astype('uint32'), [1, 4]), )
output = relay.Tuple([call_7600,call_7611,const_7612,call_7624,var_7625,const_7626,])
output2 = relay.Tuple([call_7601,call_7613,const_7612,call_7627,var_7625,const_7626,])
func_7633 = relay.Function([var_7625,], output)
mod['func_7633'] = func_7633
mod = relay.transform.InferType()(mod)
mutated_mod['func_7633'] = func_7633
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7634 = relay.var("var_7634", dtype = "uint32", shape = ())#candidate|7634|()|var|uint32
func_7633_call = mutated_mod.get_global_var('func_7633')
call_7635 = func_7633_call(var_7634)
output = call_7635
func_7636 = relay.Function([var_7634], output)
mutated_mod['func_7636'] = func_7636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6758_call = mod.get_global_var('func_6758')
func_6760_call = mutated_mod.get_global_var('func_6760')
call_7762 = relay.TupleGetItem(func_6758_call(), 0)
call_7763 = relay.TupleGetItem(func_6760_call(), 0)
output = relay.Tuple([call_7762,])
output2 = relay.Tuple([call_7763,])
func_7775 = relay.Function([], output)
mod['func_7775'] = func_7775
mod = relay.transform.InferType()(mod)
output = func_7775()
func_7776 = relay.Function([], output)
mutated_mod['func_7776'] = func_7776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6225_call = mod.get_global_var('func_6225')
func_6227_call = mutated_mod.get_global_var('func_6227')
call_7789 = relay.TupleGetItem(func_6225_call(), 1)
call_7790 = relay.TupleGetItem(func_6227_call(), 1)
func_7163_call = mod.get_global_var('func_7163')
func_7165_call = mutated_mod.get_global_var('func_7165')
call_7793 = func_7163_call()
call_7794 = func_7163_call()
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_7797 = relay.TupleGetItem(func_4637_call(), 0)
call_7798 = relay.TupleGetItem(func_4639_call(), 0)
func_7242_call = mod.get_global_var('func_7242')
func_7243_call = mutated_mod.get_global_var('func_7243')
call_7815 = relay.TupleGetItem(func_7242_call(), 0)
call_7816 = relay.TupleGetItem(func_7243_call(), 0)
output = relay.Tuple([call_7789,call_7793,call_7797,call_7815,])
output2 = relay.Tuple([call_7790,call_7794,call_7798,call_7816,])
func_7830 = relay.Function([], output)
mod['func_7830'] = func_7830
mod = relay.transform.InferType()(mod)
mutated_mod['func_7830'] = func_7830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7830_call = mutated_mod.get_global_var('func_7830')
call_7831 = func_7830_call()
output = call_7831
func_7832 = relay.Function([], output)
mutated_mod['func_7832'] = func_7832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mod.get_global_var('func_4893')
func_4894_call = mutated_mod.get_global_var('func_4894')
call_7849 = relay.TupleGetItem(func_4893_call(), 1)
call_7850 = relay.TupleGetItem(func_4894_call(), 1)
output = relay.Tuple([call_7849,])
output2 = relay.Tuple([call_7850,])
func_7852 = relay.Function([], output)
mod['func_7852'] = func_7852
mod = relay.transform.InferType()(mod)
mutated_mod['func_7852'] = func_7852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7852_call = mutated_mod.get_global_var('func_7852')
call_7853 = func_7852_call()
output = call_7853
func_7854 = relay.Function([], output)
mutated_mod['func_7854'] = func_7854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7163_call = mod.get_global_var('func_7163')
func_7165_call = mutated_mod.get_global_var('func_7165')
call_7874 = func_7163_call()
call_7875 = func_7163_call()
func_2296_call = mod.get_global_var('func_2296')
func_2298_call = mutated_mod.get_global_var('func_2298')
const_7883 = relay.const([-1,-9,1,-3,-7,-7,-2,3,8,6,-9,5,10,8,-10,-6,5,9,5,5,3,-5,2,7,-7,5,-3,1,-6,1,-1,7,2,4,-8,-9,10,7,3,-1,10,8,8,9,2,2,-8,-9,-6,10,-3,-6,3,6,-1,8,-3,-7,8,9,-7,-3,-9,-9,-9,-9,-8,-7,10,6,-10,-5,1,-6,-9,10,5,2,10,-10,-10,3,-6,8,-4,9,9,7,-7,2,9,3,9,-1,-9,-8,-10,7,-1,-3,-9,7,8,9,-10,-1,-5,4,-10,-1,-5,-7,1,-2,7,5,10,4,-9,-5,-4,-9,-1,-10,-9,-1,3,-1,10,-5,9,-4,6,-6,1,-4,-8,-3,-8,-1,6,-1,-9,-3,6,-7,2,3,-1,2,10,6,-9,-8,-2,3,-2,6,9,-10,9,-9,3,8,-10,-4,4,-10,-9,-1,-9,8,1,3,-5,-4,-2,-7,6,9,-4,10,-4,-3,1,3,-8,-1,7,10,7,-10,8,6,-3,-4,9,-6,-4,-6,-3,-5,10,-4,10,-10,-8,7,-6,-4,9,5,-1,3,-2,-10,-5,-7,-3,-9,5,-1,10,10,5,6,-1,-4,-3,-8,5,9,-5,3,9,4,-3,-6,-6,-8,2,5,-4,8,7,2,5,9,10,-9,-8,-1,-9,4,5,4,-8,3,-9,1,6,-9,-7,-3,2,3,5,3,-3,7,10,7,2,4,-2,1,-10,-1,9,-1,-5,3,10,-4,-2,3,4,-2,2,10,-10,-4,-9,5,-10,-9,3,-3,-7,-8,-9,2,2,10,1,10,2,2,-10,1,7,2,-3,5,-3,-8,-3,-6,6,9,-7,-1,-2,10,3,-1,-3,-2,-10,-4,-9,7,-7,-7,10,-2,-6,6,9,-9,9,-3,-2,7,-2,-7,7,3,7,-7,-7,-4,4,-2,-7,-5,2,9,3,-8,-8,3,6,-9,7,8,7,-8,3,3,-10,8,-6,-6,4,-3,-6,10,-4,5,-7,5,6,-4,-1,8,-7,3,-3,2,10,10,4,8,-8,-9,-7,-8,8,-1,-3,2,5,-3,2,-6,3,-8,3,-4,10,-6,8,9,10,-4,-9,2,2,4,3,8,-3,2,4,-9,-9,-1,-10,2,-2,-2,-5,-7,-8,-10,-9,6,5,-10,-5,-5,-3,-1,9,-3,-2,-2,-7,-3,-7,7,-1,8,2,5,6,-4,-8,-1,10,6,1,8,-4,-5,6,-9,-7,-3,6,8,9,10,-7,-4,9,9,-7,-7,10,4,-8,-4,-9,-5,6,6,7,5,-10,-1,9,8,8,9,-1,-5,5,3,-6,-10,4,-10,-5,-5,5,4,7,-2,-9,-5,3,7,-9,3,-9,-10,10,-3,6,-9,-1,5,-5,3,7,4,7,-7,4,-4,4,7,3,-8,-8,-9,10,-9,2,-10,-9,10,-10,4,8,10,-1,5,-8,4,10,5,9,6,5,2,-4,3,9,7,-7,-1,-5,4,-9,-9,10,-8,9,2,-4,9,-7,10,-2,-5,-6,-7,3,4,10,9,-7,-10,-5,-10,5,4,4,7,-3,-4,9,1,5,-3,7,6,1,10,-6,-4,10,4,4,-1,-6,-7,8,-6,-3,9,-1,4,1,-9,-4,10,10,9,5,-10,-5,-5,-7,8,-2,-8,4,-8,-5,1,-9,-5,-5,3,-4,-1,2,-4,1,-8,10,7,-9,-6,1,6,-8,-8,-5,3,6,8,9,6,3,2,-10,-7,5,3,-3,-5,10,-4,-4,6,-10,-7,-4,1,-9,-3,6,-7,-3,7,1,-9,-7,8,1,-1,-8,-1,3,2,-9,-10,2,3,8,-3,4,-2,6,-2,3,9,-4,-4,6,-1,-10,7,-8,9,-2,7,-6,-7,-10,-1,-2,6,3,-5,5,-2,-8,-9,1,4,-2,-9,1,-3,5,-6,4,-5,2,-4,9,-6,-4,3,2,-9,10,5,4,-4,3,7,4,4,3,4,7,9,4,-9,9,3,5,-1,-7,7,-9,-9,8,8,3,-5,2,4,-6,-2,-8,-4,-4,-2,-2,-1,5,3,-3,-5,2,9,-4,2,3,-2,-1,-5,-3,-4,-8,-5,6,8,-10,-10,-3,-8,1,6,6,-8,-4,9,-2,2,9,4,-9,7,-5,4,5,6,4,3,-10,6,-3,-3,10,-6,-7,6,-3,5,-7,10,1,-9,8,6,2,3,-4,10,-4,-3,-7,6,2,-9,-8,-3,5,-5,-6,2,-10,-3,3,-10,-2,-9,6,10,-5,-8,-10,-6,-5,-9], dtype = "int16")#candidate|7883|(864,)|const|int16
call_7882 = func_2296_call(relay.reshape(const_7883.astype('int16'), [9, 6, 16]))
call_7884 = func_2296_call(relay.reshape(const_7883.astype('int16'), [9, 6, 16]))
output = relay.Tuple([call_7874,call_7882,const_7883,])
output2 = relay.Tuple([call_7875,call_7884,const_7883,])
func_7885 = relay.Function([], output)
mod['func_7885'] = func_7885
mod = relay.transform.InferType()(mod)
output = func_7885()
func_7886 = relay.Function([], output)
mutated_mod['func_7886'] = func_7886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5622_call = mod.get_global_var('func_5622')
func_5623_call = mutated_mod.get_global_var('func_5623')
call_8005 = relay.TupleGetItem(func_5622_call(), 0)
call_8006 = relay.TupleGetItem(func_5623_call(), 0)
func_7830_call = mod.get_global_var('func_7830')
func_7832_call = mutated_mod.get_global_var('func_7832')
call_8028 = relay.TupleGetItem(func_7830_call(), 1)
call_8029 = relay.TupleGetItem(func_7832_call(), 1)
func_5831_call = mod.get_global_var('func_5831')
func_5833_call = mutated_mod.get_global_var('func_5833')
call_8051 = relay.TupleGetItem(func_5831_call(), 0)
call_8052 = relay.TupleGetItem(func_5833_call(), 0)
output = relay.Tuple([call_8005,call_8028,call_8051,])
output2 = relay.Tuple([call_8006,call_8029,call_8052,])
func_8056 = relay.Function([], output)
mod['func_8056'] = func_8056
mod = relay.transform.InferType()(mod)
mutated_mod['func_8056'] = func_8056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8056_call = mutated_mod.get_global_var('func_8056')
call_8057 = func_8056_call()
output = call_8057
func_8058 = relay.Function([], output)
mutated_mod['func_8058'] = func_8058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6130_call = mod.get_global_var('func_6130')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_8100 = func_6130_call()
call_8101 = func_6130_call()
func_6433_call = mod.get_global_var('func_6433')
func_6438_call = mutated_mod.get_global_var('func_6438')
var_8132 = relay.var("var_8132", dtype = "float64", shape = (39,))#candidate|8132|(39,)|var|float64
const_8133 = relay.const([9,3,-2,-6,-7,9,-4,4,-2,-6,-6,10,9,-4,-7,-9,1,-10,6,-7,5,-3,-2,-2,3,9,3,7,-3,-4,-2,-9,-7,-5,-7,10,-8,-2,1,-7,2,-6,-5,-6,1,-9,5,5,-10,-6,5,-8,8,5,6,4,8,-4,2,-1,1,8,-9,9,5,6,-1,3,6,1,-10,3,-6,10,8,2,1,-7,-3,2,2,-8,-2,-4,-8,2,9,-5,4,-2,-7,4,-4,-10,9,-7,-10,4,3,-10,-3,9,8,9,-1,4,7,6,1,10,-10,9,-1,9,2,-5,4,9,9,-5,2,8,9,3,-2,8,-2,-1,3,-7,1,-2,-7,8,2,6,-3,3,10,10,1,-5,8,-7,8,-7,-7,6,9,-2,7,5,4,-10,6,-8,1,-1,9,-9,2,-6,5,3,-3,-7,4,-10,9,-3,-1,1,2,2,-10,8,9,8,-5,-7,5,1,-5,-8,-1,7,-1,6,10,5,-1,9,9,3,8,2,-6,-5,-4,-3,-3,8,1,-7,4,-1,7,4,-9,7,6,3,4,3,10,-2,-8,-4,8,2,-3,6,2,5,-6,-9,6,4,-1,-8,5,-1,-2,-6,8,2,-10,5,-8,-3,5,-9,-5,10,2,-4,-8,1,-4,10,-4,5,-9,-6,-1,3,3,8,7,-2,6,5,5,-3,5,-2,6,-5,-10,-3,-9,10,8,-10,7,-3,1,6,8,-6,-5,-3,10,5,8,4,4,-1,-1,9,-2,1,-10,1,10,-10,8,5,3,9,-8,1,6,-6,3,-6,-8,2,6,6,1,-9,1,-8,-4,8,-9,-5,2,-3,-9,-2,6,4,7,5,8,-6,10,5,-10,-7,1,5,5,8,7,-10,-6,-4,-4,1,-3,-3,1,-6,-1,2,-6,5,5,5,7,-4,2,10,-6,-10,-9,3,-10,-3,-3,3,1,1,5,-7,-5,-9,-10,-3,-9,-9,-5,-8,-3,-6,-5,-8,-8,2,6,8,-4,-8,-4,-3,1,9,4,1,-10,6,5,-2,2,8,7,1,3,-6,-8,9,-2,-7,10,4,4,-5,-3,-4,5,4,8,-3,-5,-9,1,4,8,10,9,6,-3,4,10,-10,2,6,9,2,-10,7,-8,-5,-4,4,6,-9,-3,-4,5,-9,-9,-8,6,-2,-2,8,-2,8,-5,-9,4,-1,-3,3,10,-4,7,-7,1,-9,-10,2,-9,6,-3,-6,-7,8,-3,-7,-3,2,-4,-2,10,-9,-8,10,1,3,5,5,-6,1,3,2,10,3,5,-10,-9,-5,9,-6,5,6,-7,-1,3,-10,-9,-10,8,-4,3,8,-2,8,-2,2,2,-7,-9,3,10,10,-8,2,-6,-7,-10,-10,1,2,2,1,1,4,6,-6,1,-6,6,2,-4,-10,7,-7,-8,2,-4,-6,10,-7,-9,1,-8,-8,-6,-6,-3,-7,8,9,-4,8,5,-2,-5,-9,3,4,-10,-6,3,7,10,-6,-7,-4,9,8,7,-9,3,7,-2,9,-3,6,-9,-4,6,-7,7,5,-3,-10,-5,3,10,5,-10,4,9,9,-5,-9,3,6,-5,-5,-4,-9,5,6,-1,-7,-5,-2,1,4], dtype = "int64")#candidate|8133|(616,)|const|int64
var_8134 = relay.var("var_8134", dtype = "int32", shape = (1056,))#candidate|8134|(1056,)|var|int32
call_8131 = relay.TupleGetItem(func_6433_call(relay.reshape(var_8132.astype('float64'), [39,]), relay.reshape(const_8133.astype('int64'), [616,]), relay.reshape(var_8132.astype('float64'), [39,]), relay.reshape(var_8134.astype('int32'), [1, 1056]), ), 5)
call_8135 = relay.TupleGetItem(func_6438_call(relay.reshape(var_8132.astype('float64'), [39,]), relay.reshape(const_8133.astype('int64'), [616,]), relay.reshape(var_8132.astype('float64'), [39,]), relay.reshape(var_8134.astype('int32'), [1, 1056]), ), 5)
output = relay.Tuple([call_8100,call_8131,var_8132,const_8133,var_8134,])
output2 = relay.Tuple([call_8101,call_8135,var_8132,const_8133,var_8134,])
func_8147 = relay.Function([var_8132,var_8134,], output)
mod['func_8147'] = func_8147
mod = relay.transform.InferType()(mod)
mutated_mod['func_8147'] = func_8147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8147_call = mutated_mod.get_global_var('func_8147')
var_8149 = relay.var("var_8149", dtype = "float64", shape = (39,))#candidate|8149|(39,)|var|float64
var_8150 = relay.var("var_8150", dtype = "int32", shape = (1056,))#candidate|8150|(1056,)|var|int32
call_8148 = func_8147_call(var_8149,var_8150,)
output = call_8148
func_8151 = relay.Function([var_8149,var_8150,], output)
mutated_mod['func_8151'] = func_8151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5604_call = mod.get_global_var('func_5604')
func_5606_call = mutated_mod.get_global_var('func_5606')
call_8193 = relay.TupleGetItem(func_5604_call(), 0)
call_8194 = relay.TupleGetItem(func_5606_call(), 0)
output = relay.Tuple([call_8193,])
output2 = relay.Tuple([call_8194,])
func_8226 = relay.Function([], output)
mod['func_8226'] = func_8226
mod = relay.transform.InferType()(mod)
mutated_mod['func_8226'] = func_8226
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8226_call = mutated_mod.get_global_var('func_8226')
call_8227 = func_8226_call()
output = call_8227
func_8228 = relay.Function([], output)
mutated_mod['func_8228'] = func_8228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6827_call = mod.get_global_var('func_6827')
func_6828_call = mutated_mod.get_global_var('func_6828')
call_8270 = relay.TupleGetItem(func_6827_call(), 1)
call_8271 = relay.TupleGetItem(func_6828_call(), 1)
output = call_8270
output2 = call_8271
func_8272 = relay.Function([], output)
mod['func_8272'] = func_8272
mod = relay.transform.InferType()(mod)
output = func_8272()
func_8273 = relay.Function([], output)
mutated_mod['func_8273'] = func_8273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_8276 = func_4666_call()
call_8277 = func_4666_call()
output = call_8276
output2 = call_8277
func_8278 = relay.Function([], output)
mod['func_8278'] = func_8278
mod = relay.transform.InferType()(mod)
mutated_mod['func_8278'] = func_8278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8278_call = mutated_mod.get_global_var('func_8278')
call_8279 = func_8278_call()
output = call_8279
func_8280 = relay.Function([], output)
mutated_mod['func_8280'] = func_8280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_8281 = relay.TupleGetItem(func_7885_call(), 1)
call_8282 = relay.TupleGetItem(func_7886_call(), 1)
func_6631_call = mod.get_global_var('func_6631')
func_6634_call = mutated_mod.get_global_var('func_6634')
var_8298 = relay.var("var_8298", dtype = "float32", shape = (7, 130))#candidate|8298|(7, 130)|var|float32
call_8297 = relay.TupleGetItem(func_6631_call(relay.reshape(var_8298.astype('float32'), [14, 5, 13])), 1)
call_8299 = relay.TupleGetItem(func_6634_call(relay.reshape(var_8298.astype('float32'), [14, 5, 13])), 1)
output = relay.Tuple([call_8281,call_8297,var_8298,])
output2 = relay.Tuple([call_8282,call_8299,var_8298,])
func_8300 = relay.Function([var_8298,], output)
mod['func_8300'] = func_8300
mod = relay.transform.InferType()(mod)
var_8301 = relay.var("var_8301", dtype = "float32", shape = (7, 130))#candidate|8301|(7, 130)|var|float32
output = func_8300(var_8301)
func_8302 = relay.Function([var_8301], output)
mutated_mod['func_8302'] = func_8302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8325 = relay.var("var_8325", dtype = "bool", shape = (11, 13, 15))#candidate|8325|(11, 13, 15)|var|bool
var_8326 = relay.var("var_8326", dtype = "bool", shape = (11, 13, 15))#candidate|8326|(11, 13, 15)|var|bool
bop_8327 = relay.logical_and(var_8325.astype('bool'), relay.reshape(var_8326.astype('bool'), relay.shape_of(var_8325))) # shape=(11, 13, 15)
output = bop_8327
output2 = bop_8327
func_8337 = relay.Function([var_8325,var_8326,], output)
mod['func_8337'] = func_8337
mod = relay.transform.InferType()(mod)
var_8338 = relay.var("var_8338", dtype = "bool", shape = (11, 13, 15))#candidate|8338|(11, 13, 15)|var|bool
var_8339 = relay.var("var_8339", dtype = "bool", shape = (11, 13, 15))#candidate|8339|(11, 13, 15)|var|bool
output = func_8337(var_8338,var_8339,)
func_8340 = relay.Function([var_8338,var_8339,], output)
mutated_mod['func_8340'] = func_8340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6150_call = mod.get_global_var('func_6150')
func_6151_call = mutated_mod.get_global_var('func_6151')
call_8354 = relay.TupleGetItem(func_6150_call(), 0)
call_8355 = relay.TupleGetItem(func_6151_call(), 0)
output = call_8354
output2 = call_8355
func_8367 = relay.Function([], output)
mod['func_8367'] = func_8367
mod = relay.transform.InferType()(mod)
output = func_8367()
func_8368 = relay.Function([], output)
mutated_mod['func_8368'] = func_8368
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_8377 = relay.TupleGetItem(func_5900_call(), 0)
call_8378 = relay.TupleGetItem(func_5901_call(), 0)
func_3372_call = mod.get_global_var('func_3372')
func_3374_call = mutated_mod.get_global_var('func_3374')
var_8380 = relay.var("var_8380", dtype = "float64", shape = (120,))#candidate|8380|(120,)|var|float64
call_8379 = relay.TupleGetItem(func_3372_call(relay.reshape(var_8380.astype('float64'), [1, 15, 8])), 0)
call_8381 = relay.TupleGetItem(func_3374_call(relay.reshape(var_8380.astype('float64'), [1, 15, 8])), 0)
output = relay.Tuple([call_8377,call_8379,var_8380,])
output2 = relay.Tuple([call_8378,call_8381,var_8380,])
func_8417 = relay.Function([var_8380,], output)
mod['func_8417'] = func_8417
mod = relay.transform.InferType()(mod)
mutated_mod['func_8417'] = func_8417
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8418 = relay.var("var_8418", dtype = "float64", shape = (120,))#candidate|8418|(120,)|var|float64
func_8417_call = mutated_mod.get_global_var('func_8417')
call_8419 = func_8417_call(var_8418)
output = call_8419
func_8420 = relay.Function([var_8418], output)
mutated_mod['func_8420'] = func_8420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6491_call = mod.get_global_var('func_6491')
func_6492_call = mutated_mod.get_global_var('func_6492')
call_8436 = func_6491_call()
call_8437 = func_6491_call()
output = relay.Tuple([call_8436,])
output2 = relay.Tuple([call_8437,])
func_8456 = relay.Function([], output)
mod['func_8456'] = func_8456
mod = relay.transform.InferType()(mod)
output = func_8456()
func_8457 = relay.Function([], output)
mutated_mod['func_8457'] = func_8457
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7775_call = mod.get_global_var('func_7775')
func_7776_call = mutated_mod.get_global_var('func_7776')
call_8460 = relay.TupleGetItem(func_7775_call(), 0)
call_8461 = relay.TupleGetItem(func_7776_call(), 0)
output = call_8460
output2 = call_8461
func_8468 = relay.Function([], output)
mod['func_8468'] = func_8468
mod = relay.transform.InferType()(mod)
mutated_mod['func_8468'] = func_8468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8468_call = mutated_mod.get_global_var('func_8468')
call_8469 = func_8468_call()
output = call_8469
func_8470 = relay.Function([], output)
mutated_mod['func_8470'] = func_8470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8278_call = mod.get_global_var('func_8278')
func_8280_call = mutated_mod.get_global_var('func_8280')
call_8473 = func_8278_call()
call_8474 = func_8278_call()
output = call_8473
output2 = call_8474
func_8479 = relay.Function([], output)
mod['func_8479'] = func_8479
mod = relay.transform.InferType()(mod)
output = func_8479()
func_8480 = relay.Function([], output)
mutated_mod['func_8480'] = func_8480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_8481 = relay.TupleGetItem(func_5900_call(), 0)
call_8482 = relay.TupleGetItem(func_5901_call(), 0)
output = call_8481
output2 = call_8482
func_8489 = relay.Function([], output)
mod['func_8489'] = func_8489
mod = relay.transform.InferType()(mod)
mutated_mod['func_8489'] = func_8489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8489_call = mutated_mod.get_global_var('func_8489')
call_8490 = func_8489_call()
output = call_8490
func_8491 = relay.Function([], output)
mutated_mod['func_8491'] = func_8491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7502_call = mod.get_global_var('func_7502')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_8529 = relay.TupleGetItem(func_7502_call(), 2)
call_8530 = relay.TupleGetItem(func_7503_call(), 2)
output = relay.Tuple([call_8529,])
output2 = relay.Tuple([call_8530,])
func_8532 = relay.Function([], output)
mod['func_8532'] = func_8532
mod = relay.transform.InferType()(mod)
mutated_mod['func_8532'] = func_8532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mutated_mod.get_global_var('func_8532')
call_8533 = func_8532_call()
output = call_8533
func_8534 = relay.Function([], output)
mutated_mod['func_8534'] = func_8534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7502_call = mod.get_global_var('func_7502')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_8540 = relay.TupleGetItem(func_7502_call(), 3)
call_8541 = relay.TupleGetItem(func_7503_call(), 3)
output = call_8540
output2 = call_8541
func_8581 = relay.Function([], output)
mod['func_8581'] = func_8581
mod = relay.transform.InferType()(mod)
mutated_mod['func_8581'] = func_8581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8581_call = mutated_mod.get_global_var('func_8581')
call_8582 = func_8581_call()
output = call_8582
func_8583 = relay.Function([], output)
mutated_mod['func_8583'] = func_8583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_8649 = relay.TupleGetItem(func_4612_call(), 0)
call_8650 = relay.TupleGetItem(func_4614_call(), 0)
uop_8655 = relay.rsqrt(call_8649.astype('float32')) # shape=(14, 5, 13)
uop_8657 = relay.rsqrt(call_8650.astype('float32')) # shape=(14, 5, 13)
output = relay.Tuple([uop_8655,])
output2 = relay.Tuple([uop_8657,])
func_8662 = relay.Function([], output)
mod['func_8662'] = func_8662
mod = relay.transform.InferType()(mod)
mutated_mod['func_8662'] = func_8662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8662_call = mutated_mod.get_global_var('func_8662')
call_8663 = func_8662_call()
output = call_8663
func_8664 = relay.Function([], output)
mutated_mod['func_8664'] = func_8664
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7381_call = mod.get_global_var('func_7381')
func_7383_call = mutated_mod.get_global_var('func_7383')
call_8685 = relay.TupleGetItem(func_7381_call(), 0)
call_8686 = relay.TupleGetItem(func_7383_call(), 0)
func_8489_call = mod.get_global_var('func_8489')
func_8491_call = mutated_mod.get_global_var('func_8491')
call_8734 = func_8489_call()
call_8735 = func_8489_call()
func_8581_call = mod.get_global_var('func_8581')
func_8583_call = mutated_mod.get_global_var('func_8583')
call_8745 = func_8581_call()
call_8746 = func_8581_call()
func_7566_call = mod.get_global_var('func_7566')
func_7568_call = mutated_mod.get_global_var('func_7568')
call_8756 = relay.TupleGetItem(func_7566_call(), 0)
call_8757 = relay.TupleGetItem(func_7568_call(), 0)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_8758 = relay.TupleGetItem(func_4612_call(), 0)
call_8759 = relay.TupleGetItem(func_4614_call(), 0)
func_7852_call = mod.get_global_var('func_7852')
func_7854_call = mutated_mod.get_global_var('func_7854')
call_8797 = relay.TupleGetItem(func_7852_call(), 0)
call_8798 = relay.TupleGetItem(func_7854_call(), 0)
output = relay.Tuple([call_8685,call_8734,call_8745,call_8756,call_8758,call_8797,])
output2 = relay.Tuple([call_8686,call_8735,call_8746,call_8757,call_8759,call_8798,])
func_8804 = relay.Function([], output)
mod['func_8804'] = func_8804
mod = relay.transform.InferType()(mod)
mutated_mod['func_8804'] = func_8804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8804_call = mutated_mod.get_global_var('func_8804')
call_8805 = func_8804_call()
output = call_8805
func_8806 = relay.Function([], output)
mutated_mod['func_8806'] = func_8806
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8845 = relay.var("var_8845", dtype = "uint64", shape = ())#candidate|8845|()|var|uint64
var_8846 = relay.var("var_8846", dtype = "uint64", shape = (4, 13, 8))#candidate|8846|(4, 13, 8)|var|uint64
bop_8847 = relay.right_shift(var_8845.astype('uint64'), var_8846.astype('uint64')) # shape=(4, 13, 8)
output = relay.Tuple([bop_8847,])
output2 = relay.Tuple([bop_8847,])
func_8852 = relay.Function([var_8845,var_8846,], output)
mod['func_8852'] = func_8852
mod = relay.transform.InferType()(mod)
mutated_mod['func_8852'] = func_8852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8852_call = mutated_mod.get_global_var('func_8852')
var_8854 = relay.var("var_8854", dtype = "uint64", shape = ())#candidate|8854|()|var|uint64
var_8855 = relay.var("var_8855", dtype = "uint64", shape = (4, 13, 8))#candidate|8855|(4, 13, 8)|var|uint64
call_8853 = func_8852_call(var_8854,var_8855,)
output = call_8853
func_8856 = relay.Function([var_8854,var_8855,], output)
mutated_mod['func_8856'] = func_8856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_8897 = relay.TupleGetItem(func_4612_call(), 0)
call_8898 = relay.TupleGetItem(func_4614_call(), 0)
output = call_8897
output2 = call_8898
func_8933 = relay.Function([], output)
mod['func_8933'] = func_8933
mod = relay.transform.InferType()(mod)
mutated_mod['func_8933'] = func_8933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8933_call = mutated_mod.get_global_var('func_8933')
call_8934 = func_8933_call()
output = call_8934
func_8935 = relay.Function([], output)
mutated_mod['func_8935'] = func_8935
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9079 = relay.var("var_9079", dtype = "float32", shape = (13, 2, 14))#candidate|9079|(13, 2, 14)|var|float32
var_9080 = relay.var("var_9080", dtype = "float32", shape = (13, 2, 14))#candidate|9080|(13, 2, 14)|var|float32
bop_9081 = relay.floor_divide(var_9079.astype('float32'), relay.reshape(var_9080.astype('float32'), relay.shape_of(var_9079))) # shape=(13, 2, 14)
output = relay.Tuple([bop_9081,])
output2 = relay.Tuple([bop_9081,])
func_9118 = relay.Function([var_9079,var_9080,], output)
mod['func_9118'] = func_9118
mod = relay.transform.InferType()(mod)
var_9119 = relay.var("var_9119", dtype = "float32", shape = (13, 2, 14))#candidate|9119|(13, 2, 14)|var|float32
var_9120 = relay.var("var_9120", dtype = "float32", shape = (13, 2, 14))#candidate|9120|(13, 2, 14)|var|float32
output = func_9118(var_9119,var_9120,)
func_9121 = relay.Function([var_9119,var_9120,], output)
mutated_mod['func_9121'] = func_9121
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9170 = relay.const([[[-7.909630,7.259420,-7.480634,3.377122,-0.955839,-1.567155,2.457265,-2.880501,1.808558,4.363023],[-0.280494,9.437597,0.521971,6.809727,-4.968891,-4.440534,0.034917,7.916780,-4.511501,-2.339264],[-2.193194,-8.217474,2.421953,-8.845639,-2.315566,6.205687,7.164077,7.720320,-4.207566,0.381089],[2.171971,5.007279,4.379286,-8.298245,5.308780,-6.477362,-9.467033,5.161484,-5.839921,-6.621381],[-0.162293,1.857320,-4.743898,-5.219629,6.704079,0.386815,5.096139,4.607798,1.676402,-1.176403],[-8.795627,4.659709,1.068907,-5.871668,-0.894211,-1.400876,3.954035,1.884810,-8.131907,-7.296008],[8.672272,7.872762,-9.881856,5.173628,-8.960100,-0.824475,1.394516,7.870653,-9.438064,-8.912218],[-6.970445,2.200568,-2.400260,-8.669517,-7.988522,-1.613070,-6.478636,1.610084,1.196476,4.070894],[-0.970216,-6.519021,0.204936,1.504988,-5.211240,-4.837561,-7.563752,-3.343021,-1.566720,-6.677271],[7.029011,-3.040317,-8.147023,-3.678735,4.989560,5.543109,8.512579,7.759170,-4.787324,-9.990978],[-9.826627,1.123385,8.434238,7.249086,-5.663272,-0.222810,-3.047383,-3.040599,-9.678226,-7.957958],[-4.826997,-5.435765,-0.031899,-8.398251,-1.616623,4.103682,8.298657,2.124706,-7.635814,0.337142],[-7.838554,-0.509723,-3.231988,9.473980,5.706167,-2.115208,-8.848248,8.634849,-0.579641,0.354252]],[[-5.966898,3.376151,2.869746,-5.544815,7.921172,2.361781,-1.028462,4.598259,-9.890451,2.224769],[-5.409385,4.783045,-3.312977,4.673667,-8.579761,6.806976,8.779350,-9.751315,-4.541937,-1.988115],[-6.179065,3.200373,8.368748,-8.692274,-6.074218,2.525963,6.650572,0.594083,3.777980,7.097766],[9.814131,9.558025,5.172515,2.540982,-5.540596,-8.888190,2.997086,8.921576,-4.054874,-6.279693],[-3.720586,2.944479,-3.238483,4.244445,-4.952733,9.757078,-5.785527,-5.149836,2.419514,3.789272],[-3.724212,-4.938008,0.468462,-6.975087,3.694717,-3.636971,6.926732,-5.432315,-2.176307,0.930967],[-3.301169,-0.414869,6.348578,-7.866787,7.385637,6.706331,5.265140,5.236110,9.296405,-8.575801],[8.549434,-9.011487,1.308370,-8.613279,0.975044,-3.580445,0.957355,-9.769130,2.797284,8.598965],[-1.404604,-4.820500,-4.587827,-6.808511,-5.242087,5.699770,-7.959037,-6.722227,-4.151209,6.698518],[-6.125434,4.875473,4.362799,6.899040,-6.460011,2.969926,0.083943,0.579869,0.447716,3.696181],[-9.425705,3.189119,2.804678,-2.503480,9.278994,5.208378,3.174111,2.165454,-4.764749,-3.167700],[2.329423,6.582402,9.008693,-3.745618,-3.254762,-7.388636,-8.985160,1.823336,4.498373,0.674948],[-4.230591,8.430794,2.235312,-8.536286,0.734430,5.034719,-5.652962,0.888324,7.524247,-2.966778]],[[6.190678,-4.432346,0.994758,2.681195,-0.662808,5.087541,5.498483,-3.727852,2.877685,-6.028463],[1.322604,3.427059,-7.729864,-0.528278,-2.468459,-2.546234,4.048030,-3.501076,-8.333999,-1.552212],[-8.226732,7.702340,-9.510158,5.607479,-3.214058,-1.092228,2.798342,6.807655,-0.564832,6.726908],[2.175527,-1.220198,-9.099630,7.304607,9.462389,0.572034,1.151830,9.077312,9.018725,5.248304],[9.245919,1.077781,7.276058,-7.019323,-3.769486,-7.040475,8.868521,4.879287,1.666422,8.520464],[-8.620713,8.768247,0.247296,7.959043,7.276205,6.443454,-8.477633,1.595694,4.668059,8.501571],[0.454427,9.783491,-3.083673,-2.168502,3.655085,-0.598736,7.940947,5.060130,7.395742,2.742228],[3.624891,9.220213,5.866256,3.636236,-6.044232,7.087566,0.102872,0.506734,2.394608,2.708742],[7.206080,-2.293516,7.516210,3.683478,-9.927092,0.350092,4.155089,1.490521,5.388467,-6.127457],[6.587938,2.555971,-9.819274,-3.485615,8.133164,3.258397,-3.482857,3.369676,8.893541,-8.406124],[1.777701,-3.771874,-3.560845,6.432213,-5.927811,3.215121,0.245988,-6.515777,3.140097,3.488950],[8.701923,5.147587,-4.929641,2.122365,-6.569807,4.074397,-1.483662,-8.273007,5.784213,-4.608897],[6.070578,9.842612,0.278672,3.212834,2.460341,5.698934,0.655025,-5.956613,1.076711,3.097496]],[[4.324803,6.319510,-8.448215,-0.651893,2.657302,-9.563997,-0.869763,-5.700212,5.419179,3.564311],[-4.269349,1.371043,6.227063,-3.299007,-9.697800,-6.760219,-0.891527,2.040500,-4.009411,5.264161],[-0.736787,-4.477614,8.664860,-7.429650,-5.377691,7.764981,-7.472217,-8.154551,-6.107015,-3.175832],[8.658240,-8.797904,-3.107616,-5.481130,0.490740,0.434072,9.856501,3.987090,-7.680918,-1.730814],[3.723667,5.591554,-5.424675,9.093043,-8.815674,0.413652,0.394555,-2.160326,5.325795,-7.282830],[-8.044208,0.536172,9.332673,-9.432268,-0.729341,6.751683,4.781727,-9.093077,-5.452046,-0.911950],[4.298531,-3.747536,-5.873160,8.896592,-0.441771,-3.988714,7.842416,-1.536563,-9.743928,-5.150368],[8.993127,-4.978949,-3.536560,4.057565,4.699089,-4.193153,3.919659,3.361508,1.339359,-3.125936],[-9.802380,-6.432270,-8.303804,-8.763705,1.230824,9.181941,-1.661387,4.775756,-8.844594,-6.522141],[7.236226,5.629247,2.503597,-0.917591,3.373918,-0.113682,9.546540,0.963406,-3.137485,8.090305],[-8.106673,-5.844655,-3.802180,6.487622,-3.136898,-7.222460,-2.399017,7.887005,-1.968216,-5.624361],[-9.533064,8.962395,9.695169,7.240435,9.859309,-3.358733,5.499550,-6.256738,-3.177586,9.101791],[4.143603,-9.281078,2.622576,-2.346828,3.561761,0.192779,3.762390,-5.534949,3.722478,-5.242083]],[[-3.421305,-2.036348,-1.905772,7.416307,-2.772933,1.656505,1.318513,-9.167584,7.854710,-4.109151],[5.709119,-5.822472,4.721937,-5.213372,-8.181577,3.832187,7.057321,7.592552,-3.322931,-0.674558],[6.154334,0.419664,-2.452856,5.912248,-2.476350,-4.867213,1.255359,-0.679592,1.435655,3.262789],[-8.300826,-7.913164,-9.517844,8.729310,6.228918,5.659480,2.672481,7.488910,-4.309444,-0.006956],[-9.641899,9.703721,5.260402,-1.570552,-9.138314,5.746802,-2.332758,-0.127243,4.770409,-0.996950],[5.421322,4.314574,-5.246190,-3.859164,9.589894,0.887909,-0.950936,6.591128,-0.006632,-8.853755],[6.271359,8.340756,-6.164027,-0.693114,6.147419,-5.038681,-6.086352,-2.927477,-8.061730,-9.401026],[5.222903,2.572665,-5.586348,3.105775,5.702483,6.593984,9.261966,-3.337232,-7.209064,5.896235],[7.747745,-6.316483,2.624981,-2.881981,-9.326019,1.903414,-0.093515,3.496735,2.353423,-1.699133],[-2.066038,7.854831,-2.919399,5.443047,-3.077437,5.911619,-2.573523,-2.603464,-7.303942,2.378274],[8.613590,-8.624089,-2.492124,-8.998792,-3.955616,-9.015755,-9.737568,9.060463,9.619166,9.600888],[0.372513,-2.308800,-1.289779,-1.908590,8.150450,3.507751,-1.877365,9.241818,1.939682,4.829181],[-3.376165,5.628425,7.898720,4.367984,1.953834,3.331235,5.324408,8.738148,-3.020868,-0.606564]],[[7.374024,-9.858530,6.854260,-5.805922,5.838916,0.954152,4.807613,-5.571062,8.433611,-2.728931],[-1.363792,5.089454,9.130045,5.751746,-3.183648,9.069108,-2.154671,-4.000172,6.121747,-0.863093],[-4.345437,-2.712279,-2.452977,-9.548779,6.914921,7.180779,-1.419332,8.349591,9.745222,9.120205],[2.509088,2.826142,-0.692305,2.549450,7.668135,-4.716212,1.591315,5.857140,1.018531,7.497774],[-1.296210,-4.084472,-4.000530,-8.158804,2.429622,5.955849,7.256669,-5.647575,-2.527188,2.984584],[3.771667,4.469540,5.035375,4.678616,9.199658,0.625803,8.063680,-3.216460,1.651739,5.633932],[1.016270,1.732354,0.800480,-7.647860,-0.855676,4.024577,-7.666487,-2.817765,-6.455588,-8.199549],[2.448904,1.597145,-9.378889,-5.308059,2.106891,-8.573913,-7.624791,1.157839,5.324743,-0.925083],[2.715404,1.354019,-4.670933,0.525074,1.748124,-1.678479,9.466218,7.927478,-3.603753,-2.103189],[5.454887,-3.311050,-7.897874,-2.997709,9.652517,1.115003,-2.513152,-7.440300,1.492738,9.034008],[-0.961309,0.485872,-8.500134,7.131547,-9.228837,-9.924861,-6.784371,1.999415,-0.215332,-4.916051],[-1.113932,-0.627268,-4.432194,-5.853631,4.268103,6.971016,7.377665,9.270314,2.456391,-2.371228],[-6.258349,-9.960296,1.100385,-0.310697,7.555784,-2.262638,-0.157703,-8.960878,7.661523,-7.368045]],[[0.895552,-7.469886,-8.752615,-1.770107,-9.280443,6.579820,9.209679,7.322428,-7.227906,-2.241703],[-1.705059,8.529232,8.348580,-6.793972,-0.277636,1.672285,-7.511705,1.139492,-3.177980,-8.431981],[-8.196596,0.062795,4.969694,4.233704,-4.644555,0.906501,-9.365001,-6.614620,8.811221,-9.400120],[0.815307,7.931276,-1.104428,7.410713,-2.146858,1.050448,1.769978,-4.413094,-4.348132,-4.044286],[6.258490,2.609626,6.874949,4.518653,-2.677793,-0.920435,-8.262003,9.572597,-5.285608,7.535965],[4.560931,-0.004915,8.381386,3.283750,-7.984326,6.786302,-2.453312,9.268864,-6.187738,-0.799095],[-8.138157,-4.058690,-3.571806,2.167609,-8.511360,6.806784,-8.636633,1.418985,-1.964187,8.596363],[-7.699141,-7.318825,2.346623,-9.518271,-9.669127,0.878406,-7.412730,4.420417,3.096919,5.564553],[2.403896,1.502690,-4.077366,-5.185470,-4.705880,8.507766,-3.198082,3.696242,0.382027,9.437963],[-4.174387,1.061482,-9.710499,6.554091,0.616712,-1.146231,7.485077,-6.541150,-7.930924,-6.028050],[-5.172746,1.762827,8.170482,4.537255,2.475685,-3.697207,7.210987,-1.833454,6.523331,7.212234],[-7.770807,9.684846,-6.554965,-7.023703,-5.945382,5.818227,-7.015018,6.778446,3.778369,8.406473],[8.813031,-6.900128,3.103549,6.718478,-1.460576,9.142198,-6.159042,-5.536815,9.327541,8.436112]],[[1.379237,-2.498791,5.306688,5.527016,-8.986228,1.170736,-1.191317,-4.089871,-6.237085,-6.194097],[7.236840,-8.359407,0.817140,-9.114505,9.187972,-4.197446,-3.169133,-8.098380,9.061557,-7.242453],[-1.354590,9.150417,5.590158,-0.764854,6.403186,-6.294680,0.606222,-2.817766,7.852652,8.314826],[-1.899677,9.617546,-9.037106,8.651344,3.599757,-1.721539,5.678217,-4.484891,9.212293,5.560622],[-9.840085,3.392937,-0.760556,-3.520290,-4.653718,-5.352716,9.001774,0.019905,5.245511,8.395288],[-9.697044,8.635207,-4.667886,-6.712630,-6.760334,-6.249287,1.963660,-6.256269,-6.346444,6.840715],[-3.855997,0.613002,1.243770,-6.220549,1.286935,4.100254,3.579120,-9.123784,8.741122,1.438635],[-1.087289,-3.217133,-3.333664,3.202813,7.303796,1.101655,-5.534916,7.110293,-6.649815,-4.826486],[-7.759294,6.070860,-1.664976,8.410201,8.300988,-5.439156,-3.482882,0.114175,1.082187,9.350016],[-2.242357,7.062557,-0.368272,-6.099949,-1.371860,-9.777751,4.747437,-4.310975,5.394432,2.788689],[-2.063053,-3.189486,-1.790519,6.124009,-0.054788,-4.789563,-6.083215,4.433332,-7.465031,0.576579],[7.754431,0.093119,2.413883,-9.623908,5.021280,9.500083,4.469048,7.350575,-1.766392,-8.415149],[9.258605,4.001705,-6.905918,-8.041343,-0.136731,2.017112,-4.188980,-5.921996,-9.427065,-4.347265]],[[-4.359214,6.065203,-5.940461,0.168107,-0.351044,4.582746,-5.136835,9.647904,-6.962038,-4.532030],[4.184453,-4.036210,-1.580621,6.326712,2.817298,8.948825,-1.343419,-3.033843,6.636875,9.048064],[3.857482,2.405804,9.220859,-7.425903,1.496712,-1.749000,-8.461986,-3.488644,-9.470849,9.524509],[1.085449,8.600450,8.031895,-2.329643,-7.695937,-2.386205,6.966291,7.703978,-5.142562,-2.521618],[-8.391135,-0.478869,1.959940,-3.932138,9.718087,7.576607,-0.985817,-1.098423,-2.984743,-7.162970],[-4.453607,-5.748907,-8.813933,-0.489796,2.669642,-9.384196,5.653954,-1.368684,7.689316,-7.306208],[-9.291861,-1.354919,2.759458,6.798405,5.202615,-5.072972,-7.040083,2.429493,-9.189552,-3.555415],[-8.270012,-0.626785,1.741746,-9.387313,8.185527,9.470899,4.869115,-2.475560,-8.438624,-6.376917],[5.248386,6.082075,-9.398803,-9.607940,-1.933256,-6.865658,-6.369908,1.108949,-6.817873,-4.009387],[-7.932440,2.394783,5.548744,-1.432763,6.328335,-4.316724,4.994917,0.793200,-9.627799,6.551509],[-9.709633,-5.496700,-6.063752,-9.819388,2.887930,-8.922953,8.098551,8.505699,8.683811,-8.064631],[7.944279,7.275606,0.677751,-6.607130,-4.763565,-3.476316,2.507521,4.101081,-2.910666,-1.322450],[6.479466,-8.340457,7.289818,2.892280,6.407400,3.038425,-9.185222,-6.914471,9.110390,-6.915780]],[[-5.527682,-7.435947,4.529273,1.780030,-7.461144,0.073659,-1.946987,-1.706648,-1.922619,-9.481405],[4.390132,-8.635097,-3.571640,9.946914,3.664671,9.679281,8.550344,3.260531,-1.994985,-9.995277],[8.222500,-4.392221,7.063111,4.521608,-3.936849,-0.878159,7.161942,-4.098171,5.112215,-3.644088],[4.050898,-3.499509,9.477515,8.395521,-2.962816,-6.726519,5.628341,8.792462,2.862795,-5.984768],[-2.424467,-7.779653,6.982749,0.465975,-2.761462,8.437537,4.492826,-7.520242,-8.076571,-1.313246],[-2.856902,-8.040596,9.076921,-6.510200,-9.786501,4.457701,1.118826,-9.160767,-6.464309,1.469416],[6.188318,-7.953045,-4.455649,-5.307444,-2.494973,1.856387,5.680358,-8.750428,7.719951,-0.228125],[-9.998667,-9.917908,9.180623,-0.832336,-5.725635,-8.889013,1.551010,9.766004,-2.185259,-8.807094],[-5.500855,7.064755,7.782848,1.993434,-8.872024,-5.009697,3.496727,8.905828,1.476852,-6.528593],[4.421347,-4.529081,9.580428,2.458468,7.526972,-2.914682,9.596164,9.279507,9.807761,-2.270162],[-5.121790,-2.492502,7.035761,-1.452045,-8.990341,6.121276,-9.966183,-6.970940,4.190871,3.208704],[8.498746,-3.604246,0.012273,0.635638,-4.839078,-2.062642,-3.273407,-6.587860,-2.221967,-8.809844],[2.221100,9.476738,2.812326,2.714487,7.138252,2.409518,-0.531640,7.679616,-8.136851,9.046289]],[[-8.669144,9.049727,-6.123803,0.231834,4.040453,3.192903,3.564647,-0.601322,-9.510044,5.614519],[-9.754972,-3.297340,-9.371650,-1.078679,-3.086409,-8.435296,7.697864,6.688386,8.222433,1.126004],[1.833426,-4.926427,5.920487,6.662050,-9.583999,3.990729,-8.702821,-5.319338,5.974252,6.451362],[-6.976774,8.114905,6.900087,8.110916,2.678471,6.611632,-7.092003,5.301152,-9.704369,1.791225],[8.215276,2.459779,5.790314,-2.632638,-8.508613,-7.579186,5.045649,1.227808,9.014363,-9.094635],[0.182738,9.939282,4.473675,4.177768,3.740807,-3.342573,8.505194,-0.722117,2.068790,1.594538],[-8.716574,-8.718778,8.750421,3.363078,7.855795,0.755601,6.215821,-1.077117,9.548915,1.542255],[-7.688951,1.549771,8.471959,-9.506904,0.576185,8.786868,-6.817142,2.774070,4.153931,-1.453400],[-3.420427,2.090586,-2.171118,-9.174314,8.977206,-3.088868,-0.192514,7.201234,-6.594684,-1.348142],[6.751822,7.052773,-1.523014,-6.279604,9.714873,-2.160148,-1.374476,-9.567803,3.443160,8.551912],[-2.157693,-4.214365,2.850790,-7.179377,-2.370102,3.233056,-6.484245,3.532382,-0.974261,-3.694032],[-4.564397,6.875610,-6.045855,4.289406,5.049215,-2.909714,-6.050773,-5.455148,-9.377215,4.940814],[4.392593,9.191991,-9.433295,-8.334411,-4.036404,-9.010034,8.894092,0.746890,8.292060,2.851018]],[[8.090517,-8.315596,5.790734,-0.729818,-1.531376,-1.534767,-0.538815,1.732190,-9.626945,7.178335],[8.996406,1.532892,-2.068119,-3.116532,0.361487,-4.617321,-3.569707,-2.695713,0.847846,4.925274],[0.602815,8.540497,1.080369,-1.901945,0.605562,-7.590128,0.229947,8.412825,8.578623,-4.183953],[-5.427963,6.154115,7.998236,-9.500378,-2.053153,-3.433874,4.494183,-7.490275,7.780012,-5.574456],[-4.921723,1.383615,-2.590567,4.991946,-6.355727,-8.940532,-5.797405,3.787404,8.720372,-4.570788],[-5.009903,5.873866,8.649259,-6.143675,-6.259730,7.389834,-5.516744,7.378504,5.983972,-6.186303],[-6.717378,-2.133525,-7.036123,-0.228034,7.581317,-1.746292,-4.827014,5.910622,4.596242,-4.264056],[-4.973538,-7.009321,-6.135486,6.531522,7.592059,7.603221,-2.115361,-7.498034,-9.865203,3.861536],[-9.080459,4.505734,9.935643,-9.040126,-6.047075,6.267040,-8.782767,5.983914,5.962477,-8.637617],[-6.128064,-1.073948,-8.258587,-9.045854,9.005706,-9.163039,6.610613,-1.841740,6.571803,0.780456],[5.716447,-4.481620,-6.402885,-7.253119,0.533394,-6.161233,0.173310,-3.789994,-5.671825,-9.782362],[-7.212666,1.750976,-6.368617,2.245008,-6.845687,9.393693,9.537997,0.086104,-4.781476,8.772757],[-7.017216,2.092281,-8.270365,1.982184,-2.257366,-3.394115,5.420493,-3.597634,-8.462075,9.486307]],[[-5.547254,-2.444693,-9.598688,-8.447387,-0.681825,-4.346969,6.992124,-3.457031,-7.831491,-9.694373],[4.916002,4.239585,-8.887625,-3.076569,4.449273,7.767969,-8.010241,6.845665,5.895558,6.687722],[8.047778,8.143675,-0.425709,-3.818973,9.592558,9.323016,-1.128850,8.679623,8.512747,0.458372],[6.679205,-7.884378,-1.522497,6.607283,5.478236,2.743278,-9.443924,-4.830493,-8.224411,8.312255],[7.192479,-6.992972,-1.380633,3.729046,2.732482,-7.174285,6.226263,8.143347,8.483057,-5.292220],[6.193838,3.177486,-2.432783,-9.356965,6.581329,-7.139091,6.290057,-9.456298,4.932017,2.250197],[-5.709457,0.304000,-8.861337,7.064510,1.716578,8.185651,-9.245848,8.432051,-8.556997,7.700522],[1.442460,-9.393789,6.948342,-1.465375,-4.705596,4.143424,-9.927267,7.772091,5.778520,-3.857361],[-2.939023,-0.349386,-0.624938,0.192547,3.572799,-7.143122,-9.579180,1.247606,7.665940,-9.446759],[3.819930,-5.740568,8.423235,3.184872,8.016813,5.368528,2.087465,-2.105514,0.849319,-4.645501],[-8.025065,-7.589801,0.905497,-8.378224,1.472105,1.043537,2.844132,-6.289515,9.092464,9.392191],[1.807460,-8.759614,-1.984713,2.137445,-0.526067,0.966242,-9.146739,6.811772,0.447138,3.324678],[1.191566,-9.836471,-2.168987,9.400700,-7.827491,-9.476443,5.217264,-4.443430,2.824461,-2.517815]],[[8.786894,1.868602,5.879259,0.669047,-3.036425,0.144237,6.719660,-3.733273,4.124095,2.839653],[8.758940,0.004482,-7.788287,-6.474760,7.867577,2.447349,-0.747161,0.857630,-8.226429,9.363993],[3.991006,-7.522294,-5.753238,-2.249304,-9.511227,9.267845,-1.051020,-3.637785,-4.982123,-8.843447],[9.053383,-7.049298,-3.536611,4.496107,-1.089053,-4.828938,-7.924607,0.025443,3.593591,-3.241707],[9.150333,3.834131,-6.835071,2.435823,2.363069,0.113590,9.298970,-9.772974,3.896442,-4.340948],[-4.004232,5.295317,2.354199,5.256828,-9.562377,-1.638722,4.373355,9.973073,-7.544172,-4.425236],[7.754245,-0.764910,8.289824,-4.822312,7.082506,5.543353,9.265106,-1.824190,9.848116,-0.648157],[2.908328,7.106313,-0.335712,-1.214586,8.510859,-2.052852,-5.869282,-2.981829,-1.821430,-7.099225],[5.286038,4.481128,-5.017217,-3.102419,-8.476429,-9.821838,4.883654,-0.618001,-6.658524,-8.035788],[-5.396458,-0.070666,-7.474137,-2.502598,-1.693108,-8.984777,-2.493532,-4.314549,0.579233,-3.420658],[0.015023,4.688613,1.958335,9.129406,-4.746198,1.256251,-9.591098,-2.109510,-8.763228,0.857275],[6.261545,3.079337,-2.378831,7.323322,-3.949445,4.352121,-2.782197,-3.133290,-9.016210,0.369256],[-5.829524,1.903622,6.886645,0.132932,5.466216,-6.422903,-8.899735,-3.435538,7.009449,-9.693122]]], dtype = "float64")#candidate|9170|(14, 13, 10)|const|float64
var_9171 = relay.var("var_9171", dtype = "float64", shape = (14, 13, 10))#candidate|9171|(14, 13, 10)|var|float64
bop_9172 = relay.floor_divide(const_9170.astype('float64'), relay.reshape(var_9171.astype('float64'), relay.shape_of(const_9170))) # shape=(14, 13, 10)
output = bop_9172
output2 = bop_9172
func_9177 = relay.Function([var_9171,], output)
mod['func_9177'] = func_9177
mod = relay.transform.InferType()(mod)
mutated_mod['func_9177'] = func_9177
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9178 = relay.var("var_9178", dtype = "float64", shape = (14, 13, 10))#candidate|9178|(14, 13, 10)|var|float64
func_9177_call = mutated_mod.get_global_var('func_9177')
call_9179 = func_9177_call(var_9178)
output = call_9179
func_9180 = relay.Function([var_9178], output)
mutated_mod['func_9180'] = func_9180
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9199 = relay.var("var_9199", dtype = "float32", shape = (1, 11, 14))#candidate|9199|(1, 11, 14)|var|float32
uop_9200 = relay.acos(var_9199.astype('float32')) # shape=(1, 11, 14)
bop_9206 = relay.mod(uop_9200.astype('float64'), relay.reshape(var_9199.astype('float64'), relay.shape_of(uop_9200))) # shape=(1, 11, 14)
func_8479_call = mod.get_global_var('func_8479')
func_8480_call = mutated_mod.get_global_var('func_8480')
call_9211 = func_8479_call()
call_9212 = func_8479_call()
func_5326_call = mod.get_global_var('func_5326')
func_5329_call = mutated_mod.get_global_var('func_5329')
var_9219 = relay.var("var_9219", dtype = "int64", shape = (616,))#candidate|9219|(616,)|var|int64
call_9218 = relay.TupleGetItem(func_5326_call(relay.reshape(var_9219.astype('int64'), [616,])), 4)
call_9220 = relay.TupleGetItem(func_5329_call(relay.reshape(var_9219.astype('int64'), [616,])), 4)
bop_9221 = relay.bitwise_or(bop_9206.astype('uint32'), relay.reshape(var_9199.astype('uint32'), relay.shape_of(bop_9206))) # shape=(1, 11, 14)
bop_9248 = relay.logical_xor(bop_9206.astype('int64'), relay.reshape(bop_9221.astype('int64'), relay.shape_of(bop_9206))) # shape=(1, 11, 14)
func_6068_call = mod.get_global_var('func_6068')
func_6070_call = mutated_mod.get_global_var('func_6070')
const_9260 = relay.const([[4.960565,-2.094600],[1.474563,-9.422331],[5.201517,3.161459],[-4.190159,4.714194],[4.670697,2.695794],[-6.790845,-2.732620],[3.661760,-2.816606],[-8.983918,-7.261632],[-1.470840,-1.733726],[-2.591224,0.647584],[6.602299,-1.666513],[8.779757,-4.652917],[0.106331,-4.759429],[-9.205493,3.802837],[-4.824347,-6.169076],[-2.082460,-5.782370],[2.832701,3.002503],[-4.946818,0.745107],[3.442012,8.735417],[2.586469,0.252074],[8.681814,7.055765],[-8.212603,3.388949],[-2.054794,-3.109502],[2.578996,3.561175],[7.538970,-2.666859],[2.908034,5.475884],[1.354508,-8.706129],[-8.743358,7.599206],[5.426290,9.195722],[8.854334,-5.470961],[-7.111803,8.765086],[3.178777,-9.043155],[7.415386,-8.228987],[3.060904,8.776157],[4.041566,1.052653],[2.982387,5.862407],[0.099054,4.722498],[-6.726580,5.831373],[-7.083789,-0.723153],[4.354223,-3.317152],[5.461686,-8.495933],[-3.557054,3.872276],[7.105102,3.008265],[-5.213185,5.743641],[4.328476,-1.127509],[-7.220935,4.172798],[-4.068967,-5.512031],[-5.930761,-0.810074],[-2.694331,-8.129304],[-0.977712,-1.684607],[7.368060,3.179772],[-4.848371,6.032049],[2.862979,0.400069],[3.593915,-4.425379],[-2.500728,-6.762913],[1.574373,-5.953281],[6.081578,-8.533698],[6.267671,2.804539],[-0.564435,-2.740587],[2.082446,-5.353219],[8.497344,-6.414012],[-4.409410,8.875928],[4.911492,-6.347500],[-5.949587,-1.910239],[3.686376,-3.089952],[7.984162,6.903873],[-1.762906,9.494789],[-0.887780,-7.798358],[3.294564,-5.798673],[1.669461,8.981437],[1.679342,5.489486],[-6.998111,5.270945],[-6.932997,-3.327491],[8.442327,0.305081],[4.870562,8.336882],[-6.447759,-5.087843],[-1.877204,-4.728064],[-2.113882,4.442845],[0.388978,7.925870],[-3.217306,2.499241],[-6.405293,7.992176],[-8.822696,0.789259],[5.370998,5.951071],[-7.339003,5.927781],[-6.486500,-4.043694],[5.461119,8.654380],[-6.708611,1.735916],[1.363679,9.395797],[-3.108411,-8.250509],[7.271223,7.820907],[-6.221288,5.283004],[-8.764903,-9.078008],[-1.755899,7.839941],[-6.062630,-8.186031],[3.023587,0.706751],[-2.946794,5.930684],[6.968331,3.352050],[7.101737,1.836621],[3.064397,1.878495],[-4.736939,9.054451],[-1.607111,-3.618060],[9.542268,-1.731170],[-1.629875,7.404314],[-9.987956,-4.866646],[-4.920575,8.419096],[-0.543856,-2.664156],[8.946879,5.497881],[6.192507,-7.908718],[8.885125,-2.773346],[1.954759,4.819627],[-1.987500,-4.910846],[0.468088,1.823402],[9.532713,-8.618939],[5.376030,0.557982],[-9.370471,-7.396952],[8.009581,8.691928],[-6.408186,2.457244],[-8.243610,4.648959],[-9.404444,-3.120255],[-6.633724,4.416946],[-8.346385,3.876704],[-3.246554,-1.280480],[4.634300,-2.083953],[3.959339,3.634231],[8.802807,5.434860],[-8.041674,9.475951],[-6.327110,-4.716805],[5.896956,-3.477111],[7.087760,0.580276],[9.546247,-8.429763],[4.904535,7.228947],[7.012938,-3.734128],[-5.080319,-2.603532],[-3.039843,5.146731],[9.553620,-0.184924],[0.094321,-7.598377],[-1.339814,1.053476],[3.084697,8.808079],[-4.401691,1.066019],[6.743918,5.097971],[9.696183,-7.205369],[1.988321,0.895112],[-2.351550,9.595268],[-5.650780,-2.033501],[4.457738,-8.455597],[-8.933001,1.402130],[1.836992,-2.192242],[-8.161869,-6.154461],[4.348007,-5.602575],[-4.351580,-0.848282],[2.636749,-9.628520],[2.023994,-8.111800],[-5.705963,-5.032275],[-3.984360,-5.811689],[-7.420080,7.652698],[-7.112416,5.348591],[-4.194251,-7.224676],[7.892364,9.837364],[-1.416309,-0.318656],[6.538734,-8.127956],[-4.882047,-9.175091],[1.718381,-0.733710],[4.489186,-7.289303],[1.319158,8.122679],[3.674416,-8.056314],[-1.310581,4.236083],[3.401429,3.982767],[6.763684,3.481593],[-6.518636,-5.726839],[-6.386359,0.316279],[-5.317205,3.418171],[6.554820,-2.452070],[-4.966392,2.649835],[-9.044196,8.957007],[5.616513,-7.036406],[-7.497531,-9.052092],[7.861515,-1.836316],[2.714239,1.465340],[-1.967052,1.835535],[-2.633265,-8.345714],[-7.539499,0.798723],[2.738414,-6.113564],[7.466206,8.869215],[-3.637598,-1.160411],[-1.964360,9.306310],[4.069942,-5.433267],[0.330957,8.530457],[2.756401,-6.493219],[-8.184732,-8.488864],[-3.821364,-4.513932],[-3.677391,-8.975841],[2.409265,-5.280192],[0.435459,2.371616],[9.207156,-9.644907],[9.682320,-5.069402],[-6.151377,-3.402086],[-0.430975,-2.125524],[1.946878,5.958173],[-9.349481,7.588170],[-8.960591,6.072982]], dtype = "float32")#candidate|9260|(200, 2)|const|float32
call_9259 = relay.TupleGetItem(func_6068_call(relay.reshape(const_9260.astype('float32'), [400,])), 1)
call_9261 = relay.TupleGetItem(func_6070_call(relay.reshape(const_9260.astype('float32'), [400,])), 1)
bop_9265 = relay.floor_divide(bop_9206.astype('float32'), relay.reshape(var_9199.astype('float32'), relay.shape_of(bop_9206))) # shape=(1, 11, 14)
bop_9280 = relay.subtract(bop_9221.astype('uint32'), relay.reshape(bop_9265.astype('uint32'), relay.shape_of(bop_9221))) # shape=(1, 11, 14)
uop_9292 = relay.rsqrt(bop_9206.astype('float32')) # shape=(1, 11, 14)
func_5257_call = mod.get_global_var('func_5257')
func_5259_call = mutated_mod.get_global_var('func_5259')
call_9297 = relay.TupleGetItem(func_5257_call(), 0)
call_9298 = relay.TupleGetItem(func_5259_call(), 0)
func_6225_call = mod.get_global_var('func_6225')
func_6227_call = mutated_mod.get_global_var('func_6227')
call_9305 = relay.TupleGetItem(func_6225_call(), 0)
call_9306 = relay.TupleGetItem(func_6227_call(), 0)
bop_9320 = relay.not_equal(uop_9292.astype('bool'), relay.reshape(bop_9248.astype('bool'), relay.shape_of(uop_9292))) # shape=(1, 11, 14)
uop_9326 = relay.log10(uop_9200.astype('float64')) # shape=(1, 11, 14)
output = relay.Tuple([call_9211,call_9218,var_9219,call_9259,const_9260,bop_9280,call_9297,call_9305,bop_9320,uop_9326,])
output2 = relay.Tuple([call_9212,call_9220,var_9219,call_9261,const_9260,bop_9280,call_9298,call_9306,bop_9320,uop_9326,])
func_9332 = relay.Function([var_9199,var_9219,], output)
mod['func_9332'] = func_9332
mod = relay.transform.InferType()(mod)
mutated_mod['func_9332'] = func_9332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9332_call = mutated_mod.get_global_var('func_9332')
var_9334 = relay.var("var_9334", dtype = "float32", shape = (1, 11, 14))#candidate|9334|(1, 11, 14)|var|float32
var_9335 = relay.var("var_9335", dtype = "int64", shape = (616,))#candidate|9335|(616,)|var|int64
call_9333 = func_9332_call(var_9334,var_9335,)
output = call_9333
func_9336 = relay.Function([var_9334,var_9335,], output)
mutated_mod['func_9336'] = func_9336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8056_call = mod.get_global_var('func_8056')
func_8058_call = mutated_mod.get_global_var('func_8058')
call_9356 = relay.TupleGetItem(func_8056_call(), 0)
call_9357 = relay.TupleGetItem(func_8058_call(), 0)
output = call_9356
output2 = call_9357
func_9385 = relay.Function([], output)
mod['func_9385'] = func_9385
mod = relay.transform.InferType()(mod)
output = func_9385()
func_9386 = relay.Function([], output)
mutated_mod['func_9386'] = func_9386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6500_call = mod.get_global_var('func_6500')
func_6502_call = mutated_mod.get_global_var('func_6502')
call_9491 = func_6500_call()
call_9492 = func_6500_call()
output = relay.Tuple([call_9491,])
output2 = relay.Tuple([call_9492,])
func_9508 = relay.Function([], output)
mod['func_9508'] = func_9508
mod = relay.transform.InferType()(mod)
mutated_mod['func_9508'] = func_9508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9508_call = mutated_mod.get_global_var('func_9508')
call_9509 = func_9508_call()
output = call_9509
func_9510 = relay.Function([], output)
mutated_mod['func_9510'] = func_9510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7381_call = mod.get_global_var('func_7381')
func_7383_call = mutated_mod.get_global_var('func_7383')
call_9513 = relay.TupleGetItem(func_7381_call(), 0)
call_9514 = relay.TupleGetItem(func_7383_call(), 0)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_9519 = relay.TupleGetItem(func_5383_call(), 1)
call_9520 = relay.TupleGetItem(func_5385_call(), 1)
output = relay.Tuple([call_9513,call_9519,])
output2 = relay.Tuple([call_9514,call_9520,])
func_9531 = relay.Function([], output)
mod['func_9531'] = func_9531
mod = relay.transform.InferType()(mod)
mutated_mod['func_9531'] = func_9531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9531_call = mutated_mod.get_global_var('func_9531')
call_9532 = func_9531_call()
output = call_9532
func_9533 = relay.Function([], output)
mutated_mod['func_9533'] = func_9533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4580_call = mod.get_global_var('func_4580')
func_4581_call = mutated_mod.get_global_var('func_4581')
call_9582 = func_4580_call()
call_9583 = func_4580_call()
func_8804_call = mod.get_global_var('func_8804')
func_8806_call = mutated_mod.get_global_var('func_8806')
call_9585 = relay.TupleGetItem(func_8804_call(), 2)
call_9586 = relay.TupleGetItem(func_8806_call(), 2)
func_7502_call = mod.get_global_var('func_7502')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_9589 = relay.TupleGetItem(func_7502_call(), 0)
call_9590 = relay.TupleGetItem(func_7503_call(), 0)
output = relay.Tuple([call_9582,call_9585,call_9589,])
output2 = relay.Tuple([call_9583,call_9586,call_9590,])
func_9612 = relay.Function([], output)
mod['func_9612'] = func_9612
mod = relay.transform.InferType()(mod)
output = func_9612()
func_9613 = relay.Function([], output)
mutated_mod['func_9613'] = func_9613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_9632 = relay.TupleGetItem(func_5900_call(), 0)
call_9633 = relay.TupleGetItem(func_5901_call(), 0)
output = call_9632
output2 = call_9633
func_9644 = relay.Function([], output)
mod['func_9644'] = func_9644
mod = relay.transform.InferType()(mod)
output = func_9644()
func_9645 = relay.Function([], output)
mutated_mod['func_9645'] = func_9645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_9779 = relay.TupleGetItem(func_4637_call(), 0)
call_9780 = relay.TupleGetItem(func_4639_call(), 0)
output = call_9779
output2 = call_9780
func_9797 = relay.Function([], output)
mod['func_9797'] = func_9797
mod = relay.transform.InferType()(mod)
mutated_mod['func_9797'] = func_9797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9797_call = mutated_mod.get_global_var('func_9797')
call_9798 = func_9797_call()
output = call_9798
func_9799 = relay.Function([], output)
mutated_mod['func_9799'] = func_9799
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_9825 = relay.TupleGetItem(func_5900_call(), 0)
call_9826 = relay.TupleGetItem(func_5901_call(), 0)
func_7526_call = mod.get_global_var('func_7526')
func_7530_call = mutated_mod.get_global_var('func_7530')
const_9828 = relay.const(6, dtype = "uint32")#candidate|9828|()|const|uint32
var_9829 = relay.var("var_9829", dtype = "uint32", shape = (4,))#candidate|9829|(4,)|var|uint32
call_9827 = relay.TupleGetItem(func_7526_call(relay.reshape(const_9828.astype('uint32'), []), relay.reshape(var_9829.astype('uint32'), [4,]), ), 2)
call_9830 = relay.TupleGetItem(func_7530_call(relay.reshape(const_9828.astype('uint32'), []), relay.reshape(var_9829.astype('uint32'), [4,]), ), 2)
func_4777_call = mod.get_global_var('func_4777')
func_4778_call = mutated_mod.get_global_var('func_4778')
call_9831 = func_4777_call()
call_9832 = func_4777_call()
output = relay.Tuple([call_9825,call_9827,const_9828,var_9829,call_9831,])
output2 = relay.Tuple([call_9826,call_9830,const_9828,var_9829,call_9832,])
func_9833 = relay.Function([var_9829,], output)
mod['func_9833'] = func_9833
mod = relay.transform.InferType()(mod)
var_9834 = relay.var("var_9834", dtype = "uint32", shape = (4,))#candidate|9834|(4,)|var|uint32
output = func_9833(var_9834)
func_9835 = relay.Function([var_9834], output)
mutated_mod['func_9835'] = func_9835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9860 = relay.var("var_9860", dtype = "float32", shape = (8, 6, 15))#candidate|9860|(8, 6, 15)|var|float32
uop_9861 = relay.sigmoid(var_9860.astype('float32')) # shape=(8, 6, 15)
output = uop_9861
output2 = uop_9861
func_9867 = relay.Function([var_9860,], output)
mod['func_9867'] = func_9867
mod = relay.transform.InferType()(mod)
mutated_mod['func_9867'] = func_9867
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9868 = relay.var("var_9868", dtype = "float32", shape = (8, 6, 15))#candidate|9868|(8, 6, 15)|var|float32
func_9867_call = mutated_mod.get_global_var('func_9867')
call_9869 = func_9867_call(var_9868)
output = call_9869
func_9870 = relay.Function([var_9868], output)
mutated_mod['func_9870'] = func_9870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_9874 = relay.TupleGetItem(func_7885_call(), 2)
call_9875 = relay.TupleGetItem(func_7886_call(), 2)
output = relay.Tuple([call_9874,])
output2 = relay.Tuple([call_9875,])
func_9878 = relay.Function([], output)
mod['func_9878'] = func_9878
mod = relay.transform.InferType()(mod)
mutated_mod['func_9878'] = func_9878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9878_call = mutated_mod.get_global_var('func_9878')
call_9879 = func_9878_call()
output = call_9879
func_9880 = relay.Function([], output)
mutated_mod['func_9880'] = func_9880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5622_call = mod.get_global_var('func_5622')
func_5623_call = mutated_mod.get_global_var('func_5623')
call_9892 = relay.TupleGetItem(func_5622_call(), 1)
call_9893 = relay.TupleGetItem(func_5623_call(), 1)
output = relay.Tuple([call_9892,])
output2 = relay.Tuple([call_9893,])
func_9905 = relay.Function([], output)
mod['func_9905'] = func_9905
mod = relay.transform.InferType()(mod)
mutated_mod['func_9905'] = func_9905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9905_call = mutated_mod.get_global_var('func_9905')
call_9906 = func_9905_call()
output = call_9906
func_9907 = relay.Function([], output)
mutated_mod['func_9907'] = func_9907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_9911 = func_5024_call()
call_9912 = func_5024_call()
output = call_9911
output2 = call_9912
func_9917 = relay.Function([], output)
mod['func_9917'] = func_9917
mod = relay.transform.InferType()(mod)
output = func_9917()
func_9918 = relay.Function([], output)
mutated_mod['func_9918'] = func_9918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8933_call = mod.get_global_var('func_8933')
func_8935_call = mutated_mod.get_global_var('func_8935')
call_9925 = func_8933_call()
call_9926 = func_8933_call()
output = call_9925
output2 = call_9926
func_9933 = relay.Function([], output)
mod['func_9933'] = func_9933
mod = relay.transform.InferType()(mod)
output = func_9933()
func_9934 = relay.Function([], output)
mutated_mod['func_9934'] = func_9934
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6827_call = mod.get_global_var('func_6827')
func_6828_call = mutated_mod.get_global_var('func_6828')
call_10007 = relay.TupleGetItem(func_6827_call(), 1)
call_10008 = relay.TupleGetItem(func_6828_call(), 1)
func_8278_call = mod.get_global_var('func_8278')
func_8280_call = mutated_mod.get_global_var('func_8280')
call_10013 = func_8278_call()
call_10014 = func_8278_call()
output = relay.Tuple([call_10007,call_10013,])
output2 = relay.Tuple([call_10008,call_10014,])
func_10021 = relay.Function([], output)
mod['func_10021'] = func_10021
mod = relay.transform.InferType()(mod)
output = func_10021()
func_10022 = relay.Function([], output)
mutated_mod['func_10022'] = func_10022
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10025 = relay.const([[[-6,-7,8,4,-1],[4,-2,-4,3,5],[9,9,-6,4,-2],[6,-3,6,6,1],[-3,-3,-9,9,2],[1,9,-9,-2,-7],[-5,-4,-5,2,-10]],[[-9,5,7,8,5],[10,-3,5,4,-4],[4,5,10,8,-3],[2,-1,-3,-2,-4],[3,2,-5,-8,4],[1,1,-6,5,-2],[2,10,2,10,6]],[[-10,8,-7,-7,-1],[8,9,-9,2,-8],[-2,-10,-2,8,6],[-7,-5,8,-7,10],[10,-1,9,3,-4],[6,1,-8,8,-6],[2,-3,-8,10,10]],[[5,-7,-8,-8,8],[1,-10,7,5,6],[2,-5,-4,5,-8],[3,4,2,6,2],[4,7,-8,-1,-2],[6,-2,8,-4,9],[10,7,-4,6,9]],[[-6,-3,-4,-9,-6],[10,6,3,-10,-9],[-10,3,-2,6,-8],[10,-5,-7,4,4],[9,-1,7,-1,4],[-6,-8,4,5,-10],[3,5,2,7,-9]],[[7,-4,-5,6,-8],[5,-7,-4,-2,8],[-9,3,9,9,-3],[-6,8,-1,-10,10],[-7,5,-5,2,-5],[-1,-3,10,10,-9],[-10,3,4,-3,-1]],[[6,8,-2,8,2],[6,10,8,3,-1],[-8,9,9,5,10],[4,4,7,5,-9],[3,-8,7,4,3],[4,8,-5,9,-8],[-6,4,2,-5,1]],[[4,1,6,8,-8],[7,2,-7,10,-9],[-4,-1,-6,-4,-2],[6,6,7,-7,-1],[-6,9,2,9,4],[2,-2,8,8,2],[6,3,7,-3,-7]]], dtype = "int64")#candidate|10025|(8, 7, 5)|const|int64
var_10026 = relay.var("var_10026", dtype = "int64", shape = (8, 7, 5))#candidate|10026|(8, 7, 5)|var|int64
bop_10027 = relay.bitwise_xor(const_10025.astype('int64'), relay.reshape(var_10026.astype('int64'), relay.shape_of(const_10025))) # shape=(8, 7, 5)
func_6091_call = mod.get_global_var('func_6091')
func_6094_call = mutated_mod.get_global_var('func_6094')
const_10033 = relay.const([2.093762,6.211250,-1.792388,0.386292,-5.239987,-2.486916,0.780663,5.604269,-6.708872,3.639524,5.865215,5.213233,-8.343143,-9.049222,3.391084,2.886564,9.148600,-9.000756,8.252486,3.697570,1.616093,-5.283323,-3.852444,8.620609,0.821172,-8.624558,-9.371795,-2.298009,8.841420,0.974896,7.029217,6.752690,8.183964,-6.084362,6.162803,3.240928,-5.874362,8.248339,8.695216,6.843283,-2.301281,2.226010,3.081319,4.856630,1.001537,5.492422,7.941600,7.005850,-9.319408,5.975692,4.032807,9.720436,-8.202356,6.041279,2.030891], dtype = "float32")#candidate|10033|(55,)|const|float32
call_10032 = relay.TupleGetItem(func_6091_call(relay.reshape(const_10033.astype('float32'), [11, 5, 1])), 0)
call_10034 = relay.TupleGetItem(func_6094_call(relay.reshape(const_10033.astype('float32'), [11, 5, 1])), 0)
output = relay.Tuple([bop_10027,call_10032,const_10033,])
output2 = relay.Tuple([bop_10027,call_10034,const_10033,])
func_10035 = relay.Function([var_10026,], output)
mod['func_10035'] = func_10035
mod = relay.transform.InferType()(mod)
var_10036 = relay.var("var_10036", dtype = "int64", shape = (8, 7, 5))#candidate|10036|(8, 7, 5)|var|int64
output = func_10035(var_10036)
func_10037 = relay.Function([var_10036], output)
mutated_mod['func_10037'] = func_10037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_10076 = relay.TupleGetItem(func_5203_call(), 2)
call_10077 = relay.TupleGetItem(func_5205_call(), 2)
func_8933_call = mod.get_global_var('func_8933')
func_8935_call = mutated_mod.get_global_var('func_8935')
call_10079 = func_8933_call()
call_10080 = func_8933_call()
output = relay.Tuple([call_10076,call_10079,])
output2 = relay.Tuple([call_10077,call_10080,])
func_10094 = relay.Function([], output)
mod['func_10094'] = func_10094
mod = relay.transform.InferType()(mod)
mutated_mod['func_10094'] = func_10094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10094_call = mutated_mod.get_global_var('func_10094')
call_10095 = func_10094_call()
output = call_10095
func_10096 = relay.Function([], output)
mutated_mod['func_10096'] = func_10096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8479_call = mod.get_global_var('func_8479')
func_8480_call = mutated_mod.get_global_var('func_8480')
call_10103 = func_8479_call()
call_10104 = func_8479_call()
func_1044_call = mod.get_global_var('func_1044')
func_1047_call = mutated_mod.get_global_var('func_1047')
const_10108 = relay.const([-8,-1,2,-8,3,-6,-4,-7,-4,6,-10,-10,-3,-10,-3,-7,4,1,-6,-2,8,-7,7,-7,-6,-6,1,-7,10,-7,8,5,2,7,-6,-8,7,7,7,4,6,4,-8,6,-10,-5,7,-10,6,8,6,-6,-9,-6,8,-4,2,4,10,-1,10,-9,-4,7,-6,-1,9,3,10,-8,1,-3,-3,4,8,4,-9,-7,1,4,7,10,-3,-7,4,3,9,-8,-4,6,6,-10,-2,-10,10,-10,9,4,5,-7,7,6,-6,10,7,-4,7,-9,-2,4,5,9,-6,-8,-2,-3,4,7,-2,-2,5,1,1,-3,-1,4,-2,9,-6,2,9,9,3,-5,-4,-3,4,-5,5,9,6,1,-8,8,5,-2,-5,10,-8,2,-4,5,2,5,7,-3,-9,10,3,9,-8,-4,3,-3,-9,-7,2,10,-1,1,-9,10,9,5,-8,1,7,-2,-9,3,10,10,-1,7,-5,9,-5,2,-9,-7,1,-6,5,-1,1,-6,-6,-2,-7,9,7,6,7,5,6,4,2,-6,-7,5,2,8,8,-5,1,8,1,2,-3,5,-1,-7,-10,3,-1,-5,10,9,7,4,7,6,8,-10,-6,-10,-6,1,-1,5,-3,-3,6,-2,7,1,-9,-3,-6,6,10,1,5,3,-4,-8,-1,-1,-4,-9,10,6,-8,4,4,8,-8,-9,10,-10,2,-3,-8,9,-9,2,10,-9,-9,-6,3,-6,-2,-5,-8,-9,3,-1,-6,3,-9,-5,5,9,4,-8,9,1,8,6,-1,6,4,-4,-8,-6,-4,-7,-4,4,2,-7,5,-2,4,-8,-10,-10,4,7,-3,-10,-3,-7,-3,-4,-2,-4,9,-9,-4,7,-5,-10,-2,-10,9,1,7,8,-10,7,-3,8,-8,4,-8,-6,1,10,3,8,2,-2,9,10,-4,1,9,1,8,9,-8,9,-3,3,-2,5,-10,2,-9,-7,1,-2,7,6,-9,-3,2,-8,-4,-8,-10,10,-2,-9,5,5,6,-6,1,10,7,-6,-9,3,-5,-10,5,-7,2,-9,-4,3,-10,-2,-1,10,6,-8,-2,8,3,2,-8,5,5,-7,8,6,10,-8,10,10,6,1,-8,-5,9,-1,4,-4,-1,7,-2,-7,1,-3,7,-9,1,1,10,-2,-1,5,10,6,10,-1,8,-5,5,-2,-1,-5,10,2,10,-9,9,-10,-3,8,-2,8,-9,1,-10,6,5,-2,7,-6,-9,2,9,7,-8,7,-6,-10,-9,10,-5,9,-10,-6,6,-6,7,5,1,1,-8,9,-5,-10,-1,2,-7,-7,-3,-5,-3,5,10,9,1,1,8,7,1,6,8,-8,-10,-3,8,-1,9,-2,-4,-10,-10,-8,1,2,3,-3,-7,-5,8,9,5,6,3,-1,-8,6,4,-6,7,6,-5,10,-2,10,-4,3,-8,1,8,10,5,-5,10,-3,-1,-7,-9,-10,-4,10,-9,5,-3,-9,-10,-8,5,-5,7,1,6,4,-7,-6,-5,8,1,-1,10,5,7,7,9,8,-10,3,9,3,4,-6,8,-4,7,-3,-3,9,2,-3,-9,-4,-10,-7,6,4,3,-8,-3,-10,-8,-7,9,-1,3,-1,-5,-3,4,1,-2,-10,4,-8,2,5,-10,9,10,2,3,8,-10,10,-1,-4,7,-9,-3,8,-4,-5,7,4,3,-3,-9,6,-1,3,-9,-8,2,7,-4,-1,10,-1,-10,-6,-10,1,1,-9,4,-6,-9,-1,-2,8,-3,-6,-7,-10,3,1,-7,3,2,2,-3,10,3,-5,-2,-2,-4,-8,5,-9,7,2,-6,2,8,-3,2,-3,7,-1,4,5,-4,-10,-4,9,-3,-3,-7,-7,9,-6,-5,6,-10,2,2,2,2,-7,5,6,-9,6,-4,-1,-3,3,-7,-2,8,10,3,10,-6,-10,2,-8,6,9,7,2,8,-7,-8,3,-5,10,5,-3,-6,3,-2,-1,8,-8,-1,-4,8,5,2,-4,8,-7,1,-7,7,-4,-4,-5,6,-5,4,5,3,-9,-5,2,-4,-10,10,-1,7,4,-2,-4,-2,5,-10,-1,-10,8,3,1,-10,2,8,7,-3,-9,-1,3,-3,1,-1,-4,3,6,-1,-1,10,1,1,7,8,-8,10,2,2,-5,-6,-1,3,4,6,7,3,8,-7,-7,-1,-3,6,4,-1,-8,10,-7,-9,-8,-6,-5,-4,-2,-7,5,-4,1,-6,-8,4,5,7,8,4,-3,3,-9,10,-8,-10,9,3,-4,4,5,7,-3,-3,10,-7,8,-10,6,10,-1,9,6,9,-9,1,-3,4,-3,-7,4,6,5,-9,-10,-7,3,10,-5,9,-3,10,1,2,-2,-4,4,-8,-8,9,10,-8,9,-2,8,-10,2,-7,-3,6,7,-4,2,9,1,-9,-2,-3,6,5,7,-6,-5,-3,-3,6,8,2,-1,1,9,-2,8,1,-1,9,2,-8,-10,5,-7,-5,10,7,8,-1,8,5,-1,10,-3,-1,-6,-3,-7,2,-1,10,-6,-1,3,-1,-7,6,5,3,7,-4,-4,-1,-5,-6,-4,8,-1,2,10,8,-10,-9,-10,-2,8,-2,-2,3,10,6,6,-1,2,3,-9,-3,-5,5,-5,-4,4,5,-1,-5,-8,4,-6,2,-10,-4,-6,-9,7,10,-10,5,2,-10,-8,5,-8,1,6,6,8,5,4,9,-8,5,3,2,2,2,6,8,-8,10,4,-10,-5,-8,-8,2,6,-4,9,-6,-7,-1,-6,7,-9,6,4,-6,10,9,3,-6,9,9,7,9,4,8,-2,-3,-3,-6,4,5,-8,-4,8,-1,3,6,-3,-5,-8,6,8,-3,-8,-8,-1,-10,9,-3,5,3,1,-7,6,-1,5,-4,-9,-1,-4,-3,6,-7,5,-2,-1,10,6,-6,9,7,-9,6,6,6,8,8,-1,9,-4,-10,-7,6,-8,-6,-4,-1,-3,-10,4,-10,5,8,-2,4,7,-10,-4,8,1,-9,8,-5,-6,-10,2,7,-8,5,-10,-6,5,-3,-2,-1,6,5,9,-5,-6,-9,8,8,-9,-8,4,-7,-9,7,3,6,7,5,3,3,6,-10,8,-2,10,9,3,-2,8,4,7,-1,1,-10,-8,8,5,-8,-7,-1,10,3,-5,4,4,7,9,-6,3,-9,-9,5,-4,-8,-5,9,8,-9,-7,-8,-2,-6,2,5,10,-10,-10,4,10,-6,2,2,-9,4,-3,-9,-9,8,-9,-1,-9,-9,-6,5,-4,2,-8,5,-5,-3,3,-5,-9,4,-8,-8,-5,-7,9,-6,-5,-10,-5,10,5,-8,9,1,-8,7,-1,4,1,7,-3,2,1,1,-6,6,6,2,-9,3,-1,5,5,-9,3,6,-9,2,-10,-8,3,10,9,-5,6,-8,-10,10,-4,-4,5,3,-8,-5,-7,7,-6,9,10,6,2,4,8,-7,-2,-9,1,-10,6,-7,10,-3,2,4,6,9,-3,-9,-6,-3,-9,5,4,-1,5,-3,2,1,-8], dtype = "uint64")#candidate|10108|(1344,)|const|uint64
var_10109 = relay.var("var_10109", dtype = "uint32", shape = ())#candidate|10109|()|var|uint32
call_10107 = relay.TupleGetItem(func_1044_call(relay.reshape(const_10108.astype('uint64'), [14, 12, 8]), relay.reshape(var_10109.astype('uint32'), []), ), 1)
call_10110 = relay.TupleGetItem(func_1047_call(relay.reshape(const_10108.astype('uint64'), [14, 12, 8]), relay.reshape(var_10109.astype('uint32'), []), ), 1)
func_6927_call = mod.get_global_var('func_6927')
func_6929_call = mutated_mod.get_global_var('func_6929')
call_10125 = relay.TupleGetItem(func_6927_call(), 0)
call_10126 = relay.TupleGetItem(func_6929_call(), 0)
func_8226_call = mod.get_global_var('func_8226')
func_8228_call = mutated_mod.get_global_var('func_8228')
call_10167 = relay.TupleGetItem(func_8226_call(), 0)
call_10168 = relay.TupleGetItem(func_8228_call(), 0)
func_4945_call = mod.get_global_var('func_4945')
func_4949_call = mutated_mod.get_global_var('func_4949')
const_10171 = relay.const([5.278730,6.611721,-0.279949,8.280078,9.637109,-3.920188,0.498548,-3.985635,2.518039,-6.839898,-7.390969,4.788896,-7.792862,-6.910844,3.330526,-7.000441,-0.919374,-3.392908,1.299850,-1.556464,-3.934153,7.447659,7.302930,-1.118169,-9.131219,-4.358664,-1.014913,1.358118,5.859563,9.301662,0.388041,7.231785,1.086073,-6.478511,-1.460825,4.479049,6.376221,-0.187428,-4.997458,5.301623,5.645070,5.233012,7.237140,-5.115980,-8.639985,-4.505083,-7.210123,-6.539059,6.536379,-2.838923,4.321377,2.862122,-0.525273,7.921882,-3.716860,-6.849136,-9.105647,-9.124588,-5.667386,-0.552751,-1.285633,-0.335464,9.810044,-5.991516,-5.927763,-4.402949,4.729338,-6.443882,5.089331,-3.670337,4.718068,2.508132,3.291226,1.654335,1.714411,-9.509536,-7.530126,-5.296555,5.923868,6.239363,4.358628,7.435226,5.332297,-0.847165,7.569954,-9.039184,4.066896,-5.864106,7.180262,3.503541,-1.512647,-9.874302,-5.953979,-3.192768,-1.661054,8.339887,1.937546,-4.805528,2.043198,0.268745,4.519738,6.876504,8.710339,8.199417,8.076696,4.808949,3.565812,6.952628,-9.578315,5.403014,8.451565,-2.573573,-5.140001,3.743525,-6.201713,-2.074676,-6.414054,-5.312827,-8.240895,4.653907,-7.228382,2.876933,-9.381464,-5.077586,-9.439336,7.258018,-2.487385,-0.856784,-4.701380,-8.704634,-2.694104,5.298644,-6.522051,-1.307073,7.791886,4.252095,5.355629,1.757511,9.438806,-1.431442,-9.065625,0.116725,-6.861277,2.896973,2.048245,9.201071,-7.197525,-1.818370,-8.873162,0.542364,-4.207606,-4.550022,1.030579,-3.444428,6.478045,-5.717846,-9.363385,-4.158767,1.024203,-4.702656,-5.937816,-3.256670,-2.237775,3.860992,-1.448946,-4.941455,0.863253,-8.220341,6.812846,5.116562,6.560002,-4.172404,2.310824,-2.374591,-9.384453,5.710302,-4.804487,7.073534,1.800533,-6.228943,-4.676991,-2.494675,7.617523,-1.738831,8.149914,7.268136,-6.883826,8.300885,-3.519866,-7.694779,-4.780711,8.658646,-5.725403,4.222920,-0.486215,0.407712,-3.115411,-4.372510,-5.914231,-0.712806,1.559047,-6.731253,1.575204,3.530770,-8.222202,-1.244619,-0.251255,9.838000,5.114628,-7.394222,-8.630792,-9.827358,2.477663,-7.607957,2.770265,-8.359880,-9.803219,-5.259648,-7.712974,-7.291282,-9.592639,7.609196,-3.624751,3.690144,9.887511,1.069791,7.507778,-9.125949,3.044999,-3.672060,-9.631808,1.841851,7.896944,-1.614303,6.181941,-0.261057,-1.208700,-5.642470,7.749357,-0.596222,5.144186,-3.752270,9.530455,-9.444219,-3.066750,5.626790,4.463303,1.538473,5.914861,-3.118330,-6.200047,-8.483207,-8.725316,-1.642721,-2.757888,-4.998712,-7.078224,-6.183207,3.305112,-7.772115,0.277571,-4.734698,-9.645137,6.598541,-8.516756,3.023307,4.014804,8.814778,-5.893735,5.086600,-3.115414,7.348490,-3.757692,-1.804328,-0.571534,8.925996,-3.091707,-9.324593,-2.513114,-3.710471,0.700745,3.396315,1.733406,-1.557831,-5.661420,-3.207146,5.063248,-1.984904,4.712808,6.924795,5.114950,0.556899,5.210466,7.936745,-7.016867,-0.806979,6.548771,-5.765979,-8.495221,-0.194620,-4.686656,0.924097,-4.068250,4.704574,-8.934296,1.287092,-1.575933,4.488509,-7.194662,3.103307,0.460132,-4.588810,6.276932,6.833693,4.272012,6.922091,1.009592,0.535909,-4.646963,5.120698,-1.923960,-1.216724,-9.608731,-9.451536,-9.519372,0.029806,0.974129,-8.507632,-7.945330,-6.876693,-5.303252,7.515551,-8.043371,7.703437,6.763275,2.828334,-6.118530,-6.846870,0.759727,3.417264,-6.577021,7.190154,3.755005,4.285644,-7.247104,0.157761,6.002537,-3.935448,-0.614451,-1.978548,-2.827832,8.883426,5.997798,9.771960,-0.819258,2.590076,0.471085,-3.077162,-7.897639,-9.962425,7.099569,3.731998,-1.015072,-9.844396,-9.080306,3.735825,-8.501569,9.344621,-3.056680,-8.205447,4.785813,-6.615181,6.963176,9.633156,-6.341181,-5.077053,-2.519248,-0.861155,6.205889,2.407852,3.290033,-2.181699,3.286600,6.933612,2.955671,-1.098795,5.476647,1.703844,0.899572,2.124041,6.979937,0.164783,9.579639,-4.896111,-2.244550,-5.954432,-9.217408,8.996666,-6.866116,-9.440664,-8.879157,5.122287,9.763928,-5.414074,3.095710,-2.024980,7.752125,-0.061263,1.351788,5.011230,-7.930762,8.677151,4.622512,-6.934704,5.635555,4.236801,8.963342,-2.499580,4.643690,5.117952,-9.545780,8.303330,8.221773,-6.794254,0.334052,-2.262880,-3.879495,-8.741081,-6.884085,9.070825,2.060979,-5.975078,6.604697,0.905574,5.923473,-7.085806,-3.972012,-9.466508,3.364094,-4.960684,-9.049437,7.462259,-4.506332,-8.538576,-1.507319,1.302390,-2.217387,8.766198,-7.634463,1.377834,2.647894,6.733572,2.327180,-5.470601,-3.886111,5.703664,1.911877,4.074606,0.569346,1.955140,-4.072158,2.555241,-9.769359,-2.310841,-8.327116,-9.306523,1.879133,2.381615,6.992296,-1.211203,3.656146,7.965834,-0.281397,-7.805067,-5.727697,8.041127,-6.660721,-2.658784,4.846818,4.531916,-1.729841,-5.463076,0.119729,-8.004664,9.556650,7.414689,3.463887,8.513890,5.694348,2.244381,6.345828,-2.677127,3.157131,-3.332574,-6.533546,-5.247502,-0.791226,-2.179358,4.681870,-2.478521,7.840581,6.586263,-4.072359,-6.114744,-5.460721,-2.022419,4.314222,-2.304842,7.685889,1.394986,-8.652533,-3.087739,-1.109882,0.996895,2.912234,-9.816326,0.946615,2.605838,2.044691,1.236780,6.735460,4.572793,0.542545,-8.092644,6.731778,-1.202932,3.751243,-8.633216,7.960396,0.524784,7.331484,-7.204389,9.982256,8.734988,1.350522,3.850124,-6.022753,3.611111,-4.951422,-8.197143,-4.038921,0.813419,1.122832,6.159559,5.249929,9.854218,8.417693,3.020267,-0.901433,1.236182,-0.795513,-4.894082,7.505330,-5.716415,2.884978,9.788717,1.542060,-4.647864,-0.004050,9.414180,-6.871562,3.594604,-8.677978,0.576846,3.462105,1.430692,9.766257,-9.966123,7.689491,-8.090417,2.341800,-6.043040,-8.124210,3.100423,5.436851,3.711755,1.461352,1.601562,7.145912,-0.315965,3.156281,-5.477035,-8.350295,3.227195,7.701899,-6.642668,-7.765323,5.883365,8.851535,0.408214,-8.129491,4.065486,8.644834,5.484928,8.383587,1.988024,7.175933,8.757761,-1.892488,-2.628283,-5.593915,-1.397026,6.896635,4.973805,-7.849090,2.059010,7.493971,2.951812,6.276713,-5.173885,-4.312827,1.437676,3.667547,4.454330,-7.409197,-0.208194,4.080101,8.163183,-3.106835,4.812197,1.671293,6.310440,8.763708,-6.015381,-0.293695,5.737091,-0.620847,-1.767562,7.631779,-2.161066,3.106325,-8.905468,4.085436,-6.648211,1.779177,3.469007,-4.842989,4.585403,8.155459,4.745578,-9.831945,-0.571186,6.655559,4.171582,0.688536,-1.623265,-4.254988,7.245670,-3.244589,1.587489,5.404134,8.822791,-4.457686,-2.431733,-1.574657,7.213524,-9.866338,0.108271,-9.565756,2.576521,-5.679912,2.833604,-8.125043,1.376660,-2.986368,-7.863367,8.607079,9.691169,2.922417,0.809951,3.253865,-9.147678,-2.442958,-3.932166,-6.624716,-1.254856,4.373400,9.798423,-2.030165,0.188230,-3.231581,4.386263,0.770400,9.086797,-2.389614,-4.942780,2.910283,9.822182,-4.676646,-2.392037,7.345836,-3.909902,-2.154300,8.686583,-2.685694,7.331549,-8.988773,-0.693213,-0.377924,-2.642478,-1.384767,-8.671492,-5.171742,0.022984,9.644179,4.469764,2.053142,-3.227812,-5.074084,-1.299604,-8.431684,0.322555,-1.128756,-2.721739,7.393561,1.213487,3.098353,5.704967,-9.753058,-7.881651,-1.518511,-6.847420,1.598232,-1.354324,-0.912354,-1.581369,-2.306247,-8.423775,7.657000,5.825500,7.237319,-4.955777,8.363515,-0.849940,4.118171,5.982928,8.783815,6.045599,-4.513117,-6.147866,-5.073097,7.653471,-6.574526,-2.334494,-0.369489,-5.677390,-1.915260,-8.140378,-9.184661,7.365614,-9.189027,6.180951,5.086956,-0.073325,-8.890346,-1.362507,-0.997143,-0.333553,3.740895,-8.776503,-0.314238,-8.638689,-2.759115,-8.056123,4.079357,-6.823850,8.546580,0.777028,-4.812190,-3.268959,-6.043846,8.551110,0.487471,6.979447,-6.348222,-6.897826,-0.314062,-3.453212,-7.248950,1.303662,-3.630455,9.681284,-8.934321,-3.185230,-6.753616,2.658733,-3.544637,5.246450,-3.673868,-5.124838,6.099062,-3.833474,8.374109,-9.898545,5.696847,-9.674155,6.012706,8.200117,-3.912549,-4.973956,4.163809,-4.055002,-9.837913,6.409622,-2.170296,-6.538793,-9.259295,-9.414551,1.016107,8.789781,-6.643372,-8.343008,4.742311,6.546637,-5.059361,8.875272,-8.947465,7.067747,2.649241,7.505206,-9.443772,8.791736,-1.682658,5.088479,-6.419658,7.027054,-6.166203,-7.997080,3.111746,4.758626,9.164615,2.257820,-9.004021,1.145888,4.972524,-0.094090,-6.763831,2.084950,7.627869,-5.521057,0.760700,-6.504383,4.658663,-6.412662,9.507908,-8.319092,-0.426669,-3.189727,-8.536297,-5.075799,-3.981046,-9.936402,8.507902,-0.376328,-5.256268,-6.052180,-4.969344,9.099330,-5.174036,-1.561079,7.483226,-4.427593,1.701002,2.659495,-4.770087,0.690893,-6.670181,2.431273,5.486148,-9.268288,-0.414563,-1.401739,8.570976,8.277612,7.299881,2.706338,-6.563471,-4.202735,-8.284852,-8.020869,2.976643,-0.630286,5.273429,1.180954,6.422681,-1.948017,3.974858,-9.067989,-5.819503,-6.046628,1.158157,-4.238535,7.199365,8.024518,-4.206494,2.390561,-4.856308,9.583764,4.220916,-9.909013,-0.451974,0.402858,8.657672,9.249902,5.742014,2.025407,0.857480,-1.718499,-9.746561,2.275808,5.478617,6.841331,-1.385448,4.405949,4.175818,-4.986315,-2.595950,6.191237,6.357585,9.268218,-0.593971,6.307186,6.994895,6.887054,-1.854702,-1.843886,5.422756,9.391839,7.945139,3.314894,-2.065493,-8.071949,9.798991,8.438001,-1.602153,8.260503,0.344686,7.942626,9.283386,6.553360,6.474518,7.966449,2.702106,-1.133711,-5.637469,1.867882,6.675839,2.843526,-8.377367,2.652634,-6.009860,5.343485,3.387423,-5.987841,4.713254,-7.074713,9.304130,5.634105,-6.730077,2.113520,-4.079382,-8.681295,4.398736,-0.228543,-6.806097,-2.528884,1.755588,-5.710388,-2.607751,7.734704,-2.593791,-7.093242,0.518015,-0.834937,5.507485,-9.474765,7.250443,2.957675,0.149276,-7.810651,3.463135,-6.347166,-7.725185,-5.789898,1.322021,2.762552,0.572987,6.508136,8.013941,6.989012,-2.750747,-3.319358,-3.672090,-9.710255,-0.368000,9.353909,8.900922,-7.110580,-8.338790,7.434104,-8.046909,-7.954041,-4.581551,-1.256106,4.635646,7.108144,-0.464215,0.099344,2.379220,-0.183424,-2.391863,-7.442488,4.840277,-5.694979,7.274436,9.432502,-0.145813,4.235714,8.145894,-6.454610,6.067388,-4.829838,-4.494234,-4.072830,7.352414,5.646698,-9.015780,-3.634043,-1.532137,-1.382497,-8.785415,0.405521,0.930491,9.612196,-9.199950,7.796301,2.915290,1.501839,-1.686697,-8.352413,-1.583647,0.724607,2.924304,-3.809380,-3.904724,0.934223,-4.968439,4.444494,2.566451,1.117514,3.934131,-4.291787,-4.938124,-7.097807,3.877825,0.049685,-0.931569,3.353452,-7.939385,7.462687,-7.529702,9.773685,2.693415,-7.873505,5.470758,-7.003986,-5.729325,-2.935913,5.518517,6.504614,3.081702,-1.052396,-7.230184,3.761157,-2.242594,9.574806,0.136565,7.254777,-2.299188,7.621666,8.162886,-1.763685,-2.013959,6.248187,7.732147,2.076108,2.925684,-6.733083,8.150403,-7.807461,-4.803873,-6.678335,-5.896181,-6.827879,3.165726,-0.411941,1.096867,-9.292266,4.488961,7.081059,8.749779,1.820661,4.622630,-3.924771,2.892816,-8.839578,-9.090259,9.742400,-1.977311,5.201668,-7.702750,4.233503,-5.827468,1.823200,5.965789,-9.047800,6.392861,3.647665,5.600210,2.990774,-6.356997,-7.441495,-3.251664,6.748895,3.727028,-4.853248,-2.670729,-7.744629,-2.870846,1.005963,-6.702654,-4.808823,0.411601,-7.706382,3.473615,-9.112659,6.288224,-9.702408,-2.251807,7.542406,8.850689,5.663394,3.972792,-2.490260,-2.053934,3.298637,-5.780184,-7.813841,7.571090,-7.095827,4.303695,-8.114207,-4.880915,-3.438377,-0.082266,-9.800128,-3.242991,3.024845,8.857912,6.954280,5.882655,0.383938,-2.675589,-7.113293,-8.250375,-5.105248,4.699329,7.246409,7.033289,-5.370835,4.054872,8.076465,5.761343,9.978885,9.061366,-9.895674,0.038590,-4.968732,4.844272,1.667322,7.944859,7.495014,-1.134167,-5.417553,8.345627,3.038474,-9.700190,-6.979451,0.312958,-4.316645,-8.648628,-3.338119,-8.436611,7.133347,4.288286,-2.973569,-2.430437,9.330645,-1.106174,-4.730838,-7.630979,-3.412513,2.052238,-9.141396,-3.812874,3.682773,8.697928,-3.931531,-6.901816,-0.440238,-3.963123,-9.220919,-0.809601,5.353109,-5.911969,-5.371692,4.773498,3.454412,8.928038,2.514020,-9.409310,-1.583420,-0.215667,-1.971873,-4.505185,-8.276388,9.586273,5.338306,-0.179984,-8.770708,2.475436,-0.116770,2.201836,1.672368,7.568624,-9.872742,8.653258,-8.502920,3.203159,-4.556027,5.761287,-3.614935,5.593702,-6.809879,-4.221234,-0.567002,-5.143587,-3.755694,-4.781540,-1.118418,-1.279001,-3.970767,-9.851878,-9.015126,3.228090,9.023663,3.379267,9.498256,-5.329688,1.667452,-0.249079,-2.749660,-7.757694,-4.411340,-5.074370,-9.068845,7.991569,-8.772319,8.665967,7.032343,6.722367,5.353466,-3.418289,3.767638,9.336093,3.338764,3.212020,-7.532951,-8.786668,-1.332562,2.170284,5.118637,0.694080,-8.593218,-7.801254,9.698230,1.092603,9.959837,2.314757,-3.186341,8.647202,-0.693068,2.171962,-1.564064,9.144051,-2.631323,3.293807,4.094882,9.491895,-9.252986,5.114767,0.210933,-0.859398,-2.204261,5.692271,-2.299309,-8.391345,4.088758,8.402579,2.731400,8.601570,-8.549335,-8.410231,0.657725,5.045687,5.096810,-1.673851,9.058181,9.969489,-2.991861,-4.939327,2.029893,-7.665112,-0.632718,-9.397815,-6.910232,4.021717,7.082724,1.401066,9.724695,-2.419566,0.182879,7.429024,6.314981,5.634388,-3.059767,1.267510,-0.228387,-0.060851,1.283632,3.608839,-6.073160,-9.585772,-7.190218,2.710691,0.253994,-1.971086,-8.863987,9.985206,4.893823,6.090286,1.254287,9.792917,-4.828382,-1.703169,0.416581,-0.785477,2.076356,4.597325,-0.763413,4.216663,-0.338840,-7.804641,-2.447717,-1.152886,-8.706772,4.099441,-4.934389,-0.230924,-8.364690,5.395341,-7.294552,-2.106498,-3.878155,7.549814,-2.425293,-1.228929,-2.492140,8.917177,3.606994,-9.469159,7.071709,5.535658,2.010117,2.120544,-1.614253,6.192177,-7.099489,-5.810367,5.098239,6.198357,3.133183,-9.572774,-0.801196,-7.409382,4.042875,-4.856663,-1.771542,6.319725,6.112662,1.034334,8.658671,-9.947170,-2.692375,-3.839342,-3.373662,1.137994,-9.410948,6.726260,5.330491,-2.643025,4.578281,-4.390745,-0.789046,1.457666,-7.703340,0.332316,8.552634,3.692481,0.063826,5.573381,2.747710,9.579110,-8.868768,-0.831329,-3.739048,-0.802512,8.045985,1.986970,-5.948399,2.816716,1.578827,-9.010569,-3.879777,6.216910,-1.179806,5.868471,0.645960,1.304766,-9.967100,-8.745835,-3.950701,-4.264358,0.128198,4.792154,-8.407967,-1.295747,8.092960,-6.052836,-0.648492,4.920697,-3.869702,-6.944556,1.739730,7.526996,3.607994], dtype = "float64")#candidate|10171|(1456,)|const|float64
var_10172 = relay.var("var_10172", dtype = "int32", shape = (1056,))#candidate|10172|(1056,)|var|int32
var_10173 = relay.var("var_10173", dtype = "float64", shape = (7, 5))#candidate|10173|(7, 5)|var|float64
call_10170 = relay.TupleGetItem(func_4945_call(relay.reshape(const_10171.astype('float64'), [1456,]), relay.reshape(var_10172.astype('int32'), [528, 2]), relay.reshape(var_10173.astype('float64'), [35,]), ), 5)
call_10174 = relay.TupleGetItem(func_4949_call(relay.reshape(const_10171.astype('float64'), [1456,]), relay.reshape(var_10172.astype('int32'), [528, 2]), relay.reshape(var_10173.astype('float64'), [35,]), ), 5)
func_7157_call = mod.get_global_var('func_7157')
func_7158_call = mutated_mod.get_global_var('func_7158')
call_10177 = relay.TupleGetItem(func_7157_call(), 0)
call_10178 = relay.TupleGetItem(func_7158_call(), 0)
func_9118_call = mod.get_global_var('func_9118')
func_9121_call = mutated_mod.get_global_var('func_9121')
var_10221 = relay.var("var_10221", dtype = "float32", shape = (364,))#candidate|10221|(364,)|var|float32
call_10220 = relay.TupleGetItem(func_9118_call(relay.reshape(var_10221.astype('float32'), [13, 2, 14]), relay.reshape(var_10221.astype('float32'), [13, 2, 14]), ), 0)
call_10222 = relay.TupleGetItem(func_9121_call(relay.reshape(var_10221.astype('float32'), [13, 2, 14]), relay.reshape(var_10221.astype('float32'), [13, 2, 14]), ), 0)
output = relay.Tuple([call_10103,call_10107,const_10108,var_10109,call_10125,call_10167,call_10170,const_10171,var_10172,var_10173,call_10177,call_10220,var_10221,])
output2 = relay.Tuple([call_10104,call_10110,const_10108,var_10109,call_10126,call_10168,call_10174,const_10171,var_10172,var_10173,call_10178,call_10222,var_10221,])
func_10233 = relay.Function([var_10109,var_10172,var_10173,var_10221,], output)
mod['func_10233'] = func_10233
mod = relay.transform.InferType()(mod)
mutated_mod['func_10233'] = func_10233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10233_call = mutated_mod.get_global_var('func_10233')
var_10235 = relay.var("var_10235", dtype = "uint32", shape = ())#candidate|10235|()|var|uint32
var_10236 = relay.var("var_10236", dtype = "int32", shape = (1056,))#candidate|10236|(1056,)|var|int32
var_10237 = relay.var("var_10237", dtype = "float64", shape = (7, 5))#candidate|10237|(7, 5)|var|float64
var_10238 = relay.var("var_10238", dtype = "float32", shape = (364,))#candidate|10238|(364,)|var|float32
call_10234 = func_10233_call(var_10235,var_10236,var_10237,var_10238,)
output = call_10234
func_10239 = relay.Function([var_10235,var_10236,var_10237,var_10238,], output)
mutated_mod['func_10239'] = func_10239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7566_call = mod.get_global_var('func_7566')
func_7568_call = mutated_mod.get_global_var('func_7568')
call_10310 = relay.TupleGetItem(func_7566_call(), 0)
call_10311 = relay.TupleGetItem(func_7568_call(), 0)
func_8852_call = mod.get_global_var('func_8852')
func_8856_call = mutated_mod.get_global_var('func_8856')
var_10322 = relay.var("var_10322", dtype = "uint64", shape = ())#candidate|10322|()|var|uint64
const_10323 = relay.const([5,2,-2,9,-4,3,-5,-5,3,9,-3,3,-6,2,3,-2,-9,-2,-7,-1,4,-8,-5,9,-4,-5,-7,-5,-3,2,-10,-2,-7,10,-5,-6,4,-7,-8,-6,7,1,8,-6,-5,-6,-1,6,3,3,-4,7,4,9,-2,-8,6,2,-5,6,-7,7,-1,7,8,1,2,1,2,9,5,-3,-7,9,-5,4,-7,9,5,-5,-9,-4,-4,6,5,2,-3,2,-1,-3,-6,-8,9,5,5,-4,4,-5,3,8,7,7,-6,1,2,4,1,2,-9,-4,5,-9,8,-1,5,10,-7,1,7,-3,-6,-6,-8,6,3,6,-10,9,8,10,7,-5,-8,-10,-8,4,9,-10,-8,8,8,1,8,-9,-10,-2,-10,5,-5,1,-7,1,6,-7,-10,6,-1,-8,-9,-9,-8,7,-10,-6,-7,-2,3,-4,-5,-3,-8,-2,6,-9,-9,-3,1,-4,2,8,8,-6,5,10,-1,-4,-2,9,8,-2,-8,3,4,-2,7,6,2,-6,9,7,-7,-10,-9,6,9,-4,2,8,-3,4,10,5,1,-9,5,2,-8,2,3,5,-5,-1,-4,-5,-9,7,1,1,3,-2,-7,2,-1,1,2,8,-2,-8,-9,-3,4,-8,-4,-4,-1,5,5,1,2,9,-9,3,5,-8,-6,3,-5,-2,-1,3,-7,10,-6,9,5,1,-5,5,-10,2,-8,-6,7,-1,6,-10,2,6,-3,3,-3,3,-3,-5,5,-6,4,7,10,10,2,3,-2,-2,-4,-4,-1,4,-9,-6,-8,-9,-6,6,4,6,-7,-10,7,-3,-6,9,-8,-3,2,3,-4,6,1,-10,9,-1,-2,-5,-2,10,-9,-5,-2,6,-8,7,3,3,-7,-9,8,3,10,9,-8,7,-9,-6,1,-6,1,2,-9,6,-10,2,-6,6,-5,-7,5,10,-8,-5,-8,-9,-6,-3,-6,1,-5,-1,-8,-6,-3,5,8,-2,-4,5,-1,3,5,-4,-4,-6,10,9,-8,2,-9,-9,-4,3,-1,-2,-5,10,10,3,-1,-4,-8,-8,9,8,-6,-2,10,-10,6,-3,-8,10,-7,3,-2,8,1,8], dtype = "uint64")#candidate|10323|(416,)|const|uint64
call_10321 = relay.TupleGetItem(func_8852_call(relay.reshape(var_10322.astype('uint64'), []), relay.reshape(const_10323.astype('uint64'), [4, 13, 8]), ), 0)
call_10324 = relay.TupleGetItem(func_8856_call(relay.reshape(var_10322.astype('uint64'), []), relay.reshape(const_10323.astype('uint64'), [4, 13, 8]), ), 0)
func_3630_call = mod.get_global_var('func_3630')
func_3633_call = mutated_mod.get_global_var('func_3633')
call_10328 = relay.TupleGetItem(func_3630_call(relay.reshape(var_10322.astype('bool'), [])), 0)
call_10329 = relay.TupleGetItem(func_3633_call(relay.reshape(var_10322.astype('bool'), [])), 0)
output = relay.Tuple([call_10310,call_10321,var_10322,const_10323,call_10328,])
output2 = relay.Tuple([call_10311,call_10324,var_10322,const_10323,call_10329,])
func_10336 = relay.Function([var_10322,], output)
mod['func_10336'] = func_10336
mod = relay.transform.InferType()(mod)
var_10337 = relay.var("var_10337", dtype = "uint64", shape = ())#candidate|10337|()|var|uint64
output = func_10336(var_10337)
func_10338 = relay.Function([var_10337], output)
mutated_mod['func_10338'] = func_10338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_10381 = func_4666_call()
call_10382 = func_4666_call()
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_10423 = func_4460_call()
call_10424 = func_4460_call()
output = relay.Tuple([call_10381,call_10423,])
output2 = relay.Tuple([call_10382,call_10424,])
func_10432 = relay.Function([], output)
mod['func_10432'] = func_10432
mod = relay.transform.InferType()(mod)
output = func_10432()
func_10433 = relay.Function([], output)
mutated_mod['func_10433'] = func_10433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7163_call = mod.get_global_var('func_7163')
func_7165_call = mutated_mod.get_global_var('func_7165')
call_10475 = func_7163_call()
call_10476 = func_7163_call()
output = relay.Tuple([call_10475,])
output2 = relay.Tuple([call_10476,])
func_10481 = relay.Function([], output)
mod['func_10481'] = func_10481
mod = relay.transform.InferType()(mod)
mutated_mod['func_10481'] = func_10481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10481_call = mutated_mod.get_global_var('func_10481')
call_10482 = func_10481_call()
output = call_10482
func_10483 = relay.Function([], output)
mutated_mod['func_10483'] = func_10483
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10497 = relay.var("var_10497", dtype = "float32", shape = (8, 7, 15))#candidate|10497|(8, 7, 15)|var|float32
uop_10498 = relay.atanh(var_10497.astype('float32')) # shape=(8, 7, 15)
func_5622_call = mod.get_global_var('func_5622')
func_5623_call = mutated_mod.get_global_var('func_5623')
call_10510 = relay.TupleGetItem(func_5622_call(), 1)
call_10511 = relay.TupleGetItem(func_5623_call(), 1)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_10517 = relay.TupleGetItem(func_4849_call(), 0)
call_10518 = relay.TupleGetItem(func_4850_call(), 0)
var_10519 = relay.var("var_10519", dtype = "float32", shape = (8, 7, 15))#candidate|10519|(8, 7, 15)|var|float32
bop_10520 = relay.logical_or(var_10497.astype('bool'), relay.reshape(var_10519.astype('bool'), relay.shape_of(var_10497))) # shape=(8, 7, 15)
func_7775_call = mod.get_global_var('func_7775')
func_7776_call = mutated_mod.get_global_var('func_7776')
call_10523 = relay.TupleGetItem(func_7775_call(), 0)
call_10524 = relay.TupleGetItem(func_7776_call(), 0)
output = relay.Tuple([uop_10498,call_10510,call_10517,bop_10520,call_10523,])
output2 = relay.Tuple([uop_10498,call_10511,call_10518,bop_10520,call_10524,])
func_10532 = relay.Function([var_10497,var_10519,], output)
mod['func_10532'] = func_10532
mod = relay.transform.InferType()(mod)
var_10533 = relay.var("var_10533", dtype = "float32", shape = (8, 7, 15))#candidate|10533|(8, 7, 15)|var|float32
var_10534 = relay.var("var_10534", dtype = "float32", shape = (8, 7, 15))#candidate|10534|(8, 7, 15)|var|float32
output = func_10532(var_10533,var_10534,)
func_10535 = relay.Function([var_10533,var_10534,], output)
mutated_mod['func_10535'] = func_10535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6491_call = mod.get_global_var('func_6491')
func_6492_call = mutated_mod.get_global_var('func_6492')
call_10555 = func_6491_call()
call_10556 = func_6491_call()
func_7526_call = mod.get_global_var('func_7526')
func_7530_call = mutated_mod.get_global_var('func_7530')
var_10558 = relay.var("var_10558", dtype = "uint32", shape = ())#candidate|10558|()|var|uint32
var_10559 = relay.var("var_10559", dtype = "uint32", shape = (4, 1))#candidate|10559|(4, 1)|var|uint32
call_10557 = relay.TupleGetItem(func_7526_call(relay.reshape(var_10558.astype('uint32'), []), relay.reshape(var_10559.astype('uint32'), [4,]), ), 0)
call_10560 = relay.TupleGetItem(func_7530_call(relay.reshape(var_10558.astype('uint32'), []), relay.reshape(var_10559.astype('uint32'), [4,]), ), 0)
func_6956_call = mod.get_global_var('func_6956')
func_6957_call = mutated_mod.get_global_var('func_6957')
call_10564 = relay.TupleGetItem(func_6956_call(), 0)
call_10565 = relay.TupleGetItem(func_6957_call(), 0)
output = relay.Tuple([call_10555,call_10557,var_10558,var_10559,call_10564,])
output2 = relay.Tuple([call_10556,call_10560,var_10558,var_10559,call_10565,])
func_10585 = relay.Function([var_10558,var_10559,], output)
mod['func_10585'] = func_10585
mod = relay.transform.InferType()(mod)
var_10586 = relay.var("var_10586", dtype = "uint32", shape = ())#candidate|10586|()|var|uint32
var_10587 = relay.var("var_10587", dtype = "uint32", shape = (4, 1))#candidate|10587|(4, 1)|var|uint32
output = func_10585(var_10586,var_10587,)
func_10588 = relay.Function([var_10586,var_10587,], output)
mutated_mod['func_10588'] = func_10588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_10593 = relay.TupleGetItem(func_5203_call(), 0)
call_10594 = relay.TupleGetItem(func_5205_call(), 0)
func_7566_call = mod.get_global_var('func_7566')
func_7568_call = mutated_mod.get_global_var('func_7568')
call_10595 = relay.TupleGetItem(func_7566_call(), 0)
call_10596 = relay.TupleGetItem(func_7568_call(), 0)
output = relay.Tuple([call_10593,call_10595,])
output2 = relay.Tuple([call_10594,call_10596,])
func_10615 = relay.Function([], output)
mod['func_10615'] = func_10615
mod = relay.transform.InferType()(mod)
output = func_10615()
func_10616 = relay.Function([], output)
mutated_mod['func_10616'] = func_10616
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10681 = relay.var("var_10681", dtype = "float32", shape = (10, 6, 10))#candidate|10681|(10, 6, 10)|var|float32
uop_10682 = relay.cos(var_10681.astype('float32')) # shape=(10, 6, 10)
output = uop_10682
output2 = uop_10682
func_10684 = relay.Function([var_10681,], output)
mod['func_10684'] = func_10684
mod = relay.transform.InferType()(mod)
var_10685 = relay.var("var_10685", dtype = "float32", shape = (10, 6, 10))#candidate|10685|(10, 6, 10)|var|float32
output = func_10684(var_10685)
func_10686 = relay.Function([var_10685], output)
mutated_mod['func_10686'] = func_10686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6150_call = mod.get_global_var('func_6150')
func_6151_call = mutated_mod.get_global_var('func_6151')
call_10769 = relay.TupleGetItem(func_6150_call(), 0)
call_10770 = relay.TupleGetItem(func_6151_call(), 0)
output = call_10769
output2 = call_10770
func_10787 = relay.Function([], output)
mod['func_10787'] = func_10787
mod = relay.transform.InferType()(mod)
output = func_10787()
func_10788 = relay.Function([], output)
mutated_mod['func_10788'] = func_10788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9644_call = mod.get_global_var('func_9644')
func_9645_call = mutated_mod.get_global_var('func_9645')
call_10796 = func_9644_call()
call_10797 = func_9644_call()
func_10481_call = mod.get_global_var('func_10481')
func_10483_call = mutated_mod.get_global_var('func_10483')
call_10800 = relay.TupleGetItem(func_10481_call(), 0)
call_10801 = relay.TupleGetItem(func_10483_call(), 0)
func_10684_call = mod.get_global_var('func_10684')
func_10686_call = mutated_mod.get_global_var('func_10686')
const_10813 = relay.const([-9.960919,-1.580336,0.198659,-4.606432,7.567428,-0.509754,6.531624,-9.477962,6.566547,9.054477,3.476576,3.799454,0.129183,2.771274,7.801786,4.469966,1.074166,8.621609,2.088374,-5.449751,5.159122,5.741073,5.097402,-4.785489,7.707441,4.176759,-3.749278,9.872077,-6.823419,-8.425075,7.656475,4.843889,-5.364433,8.420177,-6.211705,-5.757411,-5.135663,-4.598096,8.601472,8.212735,-3.149716,0.011153,8.972008,-8.167568,-4.767588,6.650324,-4.003220,-4.198857,7.072622,-2.251595,0.992529,-5.128514,-3.973584,2.113247,3.451983,-4.262070,2.145148,-6.035674,-9.479499,-2.595134,-9.297666,1.490690,-4.546067,2.101289,3.841190,5.839864,-8.902692,4.214525,-8.133406,-0.709530,1.178021,5.130529,5.432941,9.305160,-5.362638,-0.581024,9.724089,2.387885,8.837623,7.987897,6.979307,2.452546,-0.712156,-8.203440,9.080354,6.157416,-0.592725,4.347890,-3.956399,3.142341,5.892052,5.468833,8.123287,-3.155917,6.951276,-7.498766,2.935270,-1.928898,-6.279345,-5.432428,-9.078649,-1.428720,9.323923,-9.276328,-5.007226,-4.904176,9.052042,-8.463412,4.899166,6.795283,-9.754021,0.185775,8.082293,-7.337218,-9.567512,2.393577,-7.401768,1.329545,4.789466,0.944852,-5.436026,1.582545,-1.101378,-2.021476,7.737455,-7.073526,5.455799,2.832325,-2.633435,-9.753702,-0.450616,3.460483,3.108948,-5.528731,-7.479750,-3.399618,-4.526026,-4.397386,2.745321,-7.345527,-8.597520,8.715963,-7.094817,-4.984786,-4.597844,5.508768,-2.509892,4.316298,-4.960287,-8.687251,0.702568,4.794704,5.288575,-4.147773,-3.399001,8.181519,-7.915481,6.616181,5.230084,9.012648,-2.021745,-6.571415,8.086022,2.637708,-2.057931,-6.291743,-8.190059,7.772723,6.515972,3.211577,-2.493656,-5.101809,0.267776,6.038568,3.807421,-3.598822,3.484082,-2.240611,-0.580170,-1.260066,4.760662,-6.782171,-3.736952,0.419907,-3.908240,-7.159989,2.340224,4.534242,-5.484664,4.277395,5.302722,0.096928,4.064233,6.525190,9.105833,-5.573761,-2.574932,1.787236,-3.326807,-1.049178,6.665052,8.531042,8.357624,1.173976,2.075536,3.707736,-7.023054,9.132190,-6.053151,0.322867,6.624492,-6.107926,-9.727618,-0.619580,3.152034,3.649311,0.165869,3.994102,8.163347,-2.915811,-2.802599,0.632601,2.780664,-6.492651,4.713940,2.401661,5.928916,-2.031162,3.597873,-8.791826,2.837886,5.997281,-5.289621,3.820273,7.512890,-4.177210,4.806208,-7.373170,-7.714143,-3.211841,-1.986878,-9.106910,-3.168968,-3.574928,-8.832163,-8.334514,-4.381859,-2.193907,-3.471009,0.697399,-9.941117,1.629407,3.780718,-7.611636,-6.305195,-0.726426,-4.456232,-8.209841,2.769062,4.349471,0.625264,-2.284122,9.064707,-1.214173,-7.375641,-3.499605,5.027948,0.249433,3.680903,8.980765,-5.695064,8.918480,-2.426058,3.582666,-5.358003,8.150309,-0.721007,8.878716,1.220079,-7.407196,4.852040,-6.141955,-4.238082,-6.778556,3.236707,-6.887735,6.857191,-3.120313,7.960160,4.927681,-1.830667,-1.287355,-6.253346,2.785158,6.030188,-1.533149,-3.021494,-0.315097,-1.770042,-0.697339,-3.041030,9.567790,-6.693589,4.270676,-1.717722,3.585761,-5.607202,2.425949,-8.367851,-3.266772,-3.207407,-7.803787,2.649438,-1.115776,2.706372,0.698289,0.320050,2.893469,-0.391720,7.600354,-4.136980,-5.643415,-9.663120,1.267866,-9.129697,5.788472,-9.297483,0.278790,-7.605512,0.315843,-6.280703,1.585706,-1.218563,-6.315134,8.340213,6.896675,-1.563425,-7.199856,7.545094,0.652010,3.422826,4.180267,2.725984,0.142762,-7.453815,7.746349,4.509587,-5.053280,-4.454316,3.867388,-5.383706,6.790600,-8.076737,-6.125269,9.683387,1.885566,-6.767757,9.170998,9.046953,7.424295,4.818487,-8.625995,6.805008,-8.943012,6.606828,7.194278,-0.038024,8.477122,5.320911,6.666216,3.887334,9.286977,0.571778,4.021591,-1.857365,-9.861008,-5.902978,-4.226098,2.279501,6.289762,-1.438185,-2.132628,3.053865,9.838906,6.511465,0.778461,2.027108,-1.949806,1.923549,6.921603,-7.593744,-7.149980,5.089179,-7.781609,8.408883,9.816609,5.482282,5.518841,8.855299,0.833300,6.713338,-7.756618,9.339752,9.241853,-2.330978,-8.850038,-0.079892,3.728032,-1.882920,-1.775800,4.859723,3.963599,2.967929,8.245800,-3.921279,-9.520458,-9.639901,-9.935929,7.762422,-6.414124,9.194731,7.880766,3.782349,7.079759,-2.974212,-2.432418,9.865847,-1.089067,-5.183613,-0.519540,-1.244240,-2.969559,5.750452,9.166352,-6.899400,-2.506157,-8.036451,9.486120,4.190792,9.975041,-9.873825,3.057751,-0.581739,-7.522217,-3.258798,6.618313,0.586334,3.906191,-6.292159,-2.682125,-2.490500,-2.021680,-3.060971,9.192109,-9.614457,9.689560,-4.236447,3.676290,2.044404,7.415848,-0.916575,-5.324132,-7.892485,-4.827198,-0.701311,6.360839,9.986704,-4.352953,2.040034,4.787695,-7.260825,-9.471018,-7.705284,9.024578,3.646271,9.432952,3.389289,-3.319489,3.401992,6.987454,3.381502,-1.438942,-0.531240,-9.040722,-8.875450,-5.245104,-8.989869,7.441554,-8.326046,-2.817152,1.281085,0.367161,-6.265870,-6.201555,-5.319972,8.290819,-0.819134,-9.493828,-1.790684,-3.348797,7.105749,-1.069620,1.989267,-1.638629,-9.165871,-0.136005,-1.133954,3.758228,4.882092,-2.285903,2.573660,8.119090,7.490035,-4.916766,-7.796806,2.973791,0.315941,2.633244,6.963657,-6.306312,7.871125,-3.489537,-6.339425,-2.015954,8.917646,4.574826,-1.595672,3.691382,7.829196,-2.499100,-1.159470,8.171531,9.134779,8.798998,-7.145674,-0.783131,-0.659679,0.551526,-4.856652,-5.192094,-6.112903,-8.463769,-1.304181,-3.660960,-4.807540,8.161893,-5.991101,-9.630233,5.095389,9.230786,-8.022212,6.616464,-9.523738,1.892937,-9.385102,-1.828502,-6.460289,-6.376830,-0.290943,-4.707330,8.983010,-8.787135,-1.148021,4.107855,-4.181557,3.739949,-0.809979,2.676731,3.951939,-9.433946,-7.570132,-7.725107,7.954944,2.195796,4.816697,-0.130903,6.509449,3.685389,-8.642836,8.381106,4.801829,8.658559,-6.488399,-3.926373,2.888573,0.456650,4.383680,-2.579296,-2.128432,5.629065,1.093188,-0.705109,-9.940259,-2.402984,-5.537079,6.385441,-2.808692,-6.261373,3.616563,-4.769429], dtype = "float32")#candidate|10813|(600,)|const|float32
call_10812 = func_10684_call(relay.reshape(const_10813.astype('float32'), [10, 6, 10]))
call_10814 = func_10684_call(relay.reshape(const_10813.astype('float32'), [10, 6, 10]))
bop_10815 = relay.equal(const_10813.astype('bool'), relay.reshape(call_10812.astype('bool'), relay.shape_of(const_10813))) # shape=(600,)
bop_10818 = relay.equal(const_10813.astype('bool'), relay.reshape(call_10814.astype('bool'), relay.shape_of(const_10813))) # shape=(600,)
output = relay.Tuple([call_10796,call_10800,bop_10815,])
output2 = relay.Tuple([call_10797,call_10801,bop_10818,])
func_10821 = relay.Function([], output)
mod['func_10821'] = func_10821
mod = relay.transform.InferType()(mod)
output = func_10821()
func_10822 = relay.Function([], output)
mutated_mod['func_10822'] = func_10822
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10869 = relay.var("var_10869", dtype = "uint64", shape = (12, 13, 15))#candidate|10869|(12, 13, 15)|var|uint64
const_10870 = relay.const([[[-4,9,6,-3,6,-9,-8,2,-1,7,-2,-4,3,-1,3],[8,-4,-5,-9,-7,-2,9,1,-5,4,10,-3,4,4,8],[-3,-7,5,7,-2,-1,5,6,5,-8,-1,7,-5,-2,8],[-8,-8,8,-9,-7,3,5,8,-6,3,2,-4,-10,1,10],[3,10,7,5,5,6,10,10,5,2,1,1,-6,6,4],[5,-8,-1,3,10,9,-9,-9,8,-4,9,-8,-1,-1,10],[-3,-3,9,5,-1,1,-10,7,-9,3,-9,7,3,2,4],[-1,8,-9,9,1,8,-8,-4,10,-3,-7,5,10,1,-4],[-5,-2,-3,1,5,-2,4,3,-8,-1,4,-3,-1,9,-8],[-5,-9,5,-7,4,8,7,7,-2,-1,-5,-3,3,5,4],[-6,6,7,9,-10,8,-10,-2,2,-1,-8,-7,-9,3,-6],[-7,9,8,-5,-1,-2,2,3,9,9,10,10,-10,-2,3],[1,10,1,5,-7,-10,-7,-10,-10,8,3,-9,-9,-2,-2]],[[-9,-2,3,7,1,6,2,8,4,3,7,1,-6,3,-9],[10,-7,5,8,-10,5,-10,9,-10,-4,-4,6,-7,4,-10],[-6,-3,5,-5,-9,1,4,2,1,-6,-5,-8,-6,5,6],[2,-8,-4,-2,-7,7,8,1,-5,-4,-7,-9,-9,-9,-4],[-10,6,-3,2,-1,-8,-6,10,-8,10,-5,-10,4,-9,2],[10,2,-9,-8,10,-9,-10,5,-4,6,-5,-3,-5,-2,3],[-8,7,1,-4,-8,-10,3,4,1,-10,-2,-8,-8,5,7],[-8,-3,4,-3,-2,-3,10,2,3,-1,-2,8,1,1,7],[-4,-3,-10,-10,9,7,-4,-7,2,2,3,-8,4,-8,-5],[-2,-10,7,-6,-4,-9,-5,8,1,-4,-3,9,-9,-3,9],[-1,-9,8,10,3,6,-3,-4,7,-10,10,-9,7,3,4],[-9,5,-6,6,-6,8,-2,5,1,-3,2,-4,-6,8,2],[3,8,1,-8,10,7,-6,-8,-7,2,9,5,6,6,-1]],[[7,-2,-10,1,-2,-4,8,10,-2,4,-6,1,-10,-1,10],[-5,-3,-5,9,-1,-6,2,6,9,-8,5,8,3,10,4],[-5,-8,-7,-1,9,-9,-8,7,2,3,9,-2,-1,-4,-1],[2,9,-2,5,5,7,8,-5,-9,-1,5,-10,8,5,6],[-2,10,10,-8,-7,-8,-6,-10,-1,6,-3,3,-1,7,-5],[-2,3,8,5,-10,-10,-5,-7,5,-3,-2,-3,10,-8,-10],[1,-1,3,10,7,8,-8,-4,-9,-5,-10,-9,-3,-9,-9],[5,-2,-6,6,-10,-4,10,5,-9,3,-7,8,-7,6,-4],[-4,6,-3,-10,-6,4,1,6,-10,-10,-6,5,4,6,8],[6,-7,8,5,-1,-10,-3,-10,9,-1,-4,-8,4,1,-4],[10,-2,4,-10,-10,10,-7,1,1,9,10,10,2,-2,3],[-3,7,1,5,-8,2,5,10,-7,5,-2,9,5,-7,-4],[2,-3,-3,10,-6,5,8,-7,5,9,4,-6,-7,-4,-7]],[[-5,8,-8,4,10,-10,-10,-4,-9,5,-10,-3,-1,7,-5],[8,3,-9,10,3,-7,-5,-3,8,-10,2,-1,6,5,1],[-10,-1,-6,4,-8,-6,-9,-4,1,-6,4,-1,-3,10,2],[10,-2,-5,-3,-4,9,8,2,2,-5,-4,-4,-7,-4,5],[-8,-10,-7,-9,-7,3,-7,-3,6,-2,-4,1,1,-5,7],[-3,-6,-5,9,3,-1,1,1,6,-9,-8,5,1,1,3],[7,-3,8,-5,-6,-4,-7,4,8,5,8,-10,-7,9,6],[-4,-7,-5,-6,5,-9,8,1,-5,-2,8,-8,-3,7,2],[3,6,4,-8,-4,-10,-9,10,-2,2,-7,-4,-7,9,8],[-9,7,2,9,-10,2,-7,-10,-4,3,-6,4,-7,-6,7],[6,-6,3,4,9,-6,-6,3,-9,-10,-3,-5,8,-10,-8],[10,-4,9,-4,3,7,-6,4,10,-6,-8,-9,-10,4,-1],[8,6,-10,3,-6,-9,8,7,-3,-5,-9,10,5,5,9]],[[-2,1,-2,3,-5,2,3,7,1,-10,1,-1,-9,10,-10],[4,-9,-9,4,-4,10,-10,7,-6,-7,7,8,-8,8,3],[-10,-9,-1,-8,8,-3,10,-3,3,5,8,10,2,2,-8],[6,-1,-7,-3,9,-8,2,-8,-3,6,2,10,9,2,9],[-6,9,2,-2,-2,-6,5,-6,-7,-5,9,-9,1,-8,-9],[2,4,5,-9,10,-9,-2,8,-9,-9,10,-4,-4,6,8],[10,1,3,-9,4,-4,6,7,-5,9,-3,-3,-7,-1,-10],[-8,-9,2,4,6,1,-3,7,-2,-8,-6,9,7,-6,-9],[-9,7,-6,2,2,-10,-8,-1,2,-5,6,1,-3,-1,9],[7,7,-6,5,-4,5,-2,-6,-6,-6,-1,6,-8,-4,-8],[-1,1,-1,2,6,-4,8,4,1,-4,-4,-1,-9,-9,-10],[-6,-2,-10,5,-10,7,-3,-2,-1,-10,-9,-2,-5,1,-3],[-1,-3,-5,7,-6,4,2,8,-6,-6,4,3,8,-4,-3]],[[10,-6,-10,-8,3,-5,7,4,-3,2,1,9,-1,-3,7],[-2,4,2,10,-1,5,-10,5,-6,6,-10,-4,-10,-7,10],[1,-1,-3,-6,-4,-6,3,1,-9,8,5,-2,-8,-5,-7],[9,10,-2,-2,6,7,4,7,2,2,-3,10,7,-10,-5],[9,7,-5,-10,1,-4,7,2,5,2,-4,4,4,3,6],[-3,3,2,-10,4,10,2,8,-1,-6,10,-10,3,10,10],[-4,-10,-2,3,-7,-5,-7,-4,9,-9,8,4,-8,4,2],[5,-6,1,7,1,-2,-3,-3,7,-4,-6,8,2,6,-3],[9,-2,-2,2,8,-7,10,-3,-9,-5,-5,-5,1,-8,-3],[-5,10,5,2,-3,-1,-5,10,-5,6,-2,-1,5,-6,8],[7,-2,-3,-1,4,-7,4,-9,-10,5,-4,-9,6,6,-9],[1,-10,-3,10,7,-7,1,6,8,-4,-2,-2,3,4,-9],[-6,1,1,-8,-7,5,7,5,-7,9,-8,10,-1,7,4]],[[10,-6,3,-6,-10,-6,-9,4,8,9,-3,-8,4,-7,7],[-8,-9,-10,4,5,-1,1,-6,3,6,-1,8,3,-9,4],[-2,-4,9,-7,-2,-6,-5,-2,-4,5,9,-9,5,1,-4],[1,9,9,1,-10,-10,3,-5,-8,-10,-9,1,7,3,2],[-5,5,8,4,2,10,2,1,10,8,-4,-10,6,1,-5],[7,5,4,6,3,-1,1,-10,-1,-2,2,-6,3,8,-3],[6,-3,-2,8,-4,-5,6,8,-10,8,-10,10,-3,-9,-6],[5,10,4,-4,9,3,-5,-2,9,-4,6,9,1,6,4],[10,-3,-7,4,1,-1,9,-7,1,-5,-3,10,-6,4,10],[-3,7,-3,-2,8,-2,10,-9,6,-1,6,1,-5,-6,8],[-7,6,-4,-10,8,2,9,3,8,-7,-8,4,8,6,-10],[-7,5,3,-2,8,1,10,-1,-7,10,-10,4,10,5,5],[2,4,-7,7,-10,-1,-6,-10,-4,7,-8,4,1,5,4]],[[1,5,-3,2,4,-6,10,6,8,6,3,2,-7,3,-1],[5,-3,7,1,-8,1,9,-8,3,2,1,5,-5,8,-6],[5,1,2,-5,-7,-9,9,-2,-1,-2,6,10,-7,-6,3],[4,-5,-5,2,9,3,10,6,-8,8,-1,1,6,8,-5],[-3,-10,-3,-5,-5,6,2,1,-7,6,6,10,1,-9,7],[4,4,-8,9,4,6,3,6,-8,2,10,3,7,-5,5],[-2,-2,4,-3,-1,-8,-9,-7,-6,9,10,6,-1,-7,3],[10,2,-2,-2,-9,4,-2,-10,-7,5,-4,9,-8,7,9],[-7,5,-3,-4,-2,9,-10,-8,-9,7,-2,1,-3,2,-2],[9,-3,7,-1,-10,3,8,10,6,-2,-5,5,6,3,-9],[-2,-4,-5,1,-1,-9,-2,-10,5,-2,-10,-3,-1,5,10],[8,-4,-7,3,-5,10,-1,-2,-3,-6,6,-1,10,-10,7],[3,-2,-8,-8,-8,5,8,10,-8,1,-1,-9,7,-4,8]],[[-7,-7,-8,9,-5,-10,6,-8,-9,3,-10,6,5,-1,-2],[-2,-2,7,3,-7,-4,-3,-6,-9,9,5,-4,-1,4,-10],[2,5,-3,3,10,-6,-8,7,2,-7,5,10,-2,-10,4],[-5,4,-10,4,-2,-5,1,9,-5,3,10,3,9,3,-6],[-1,-3,10,-1,7,1,4,-5,-1,4,4,1,-5,5,-10],[-3,1,-6,-9,7,2,10,-9,9,-7,5,-8,-1,9,-1],[8,-9,-1,-9,-4,8,4,2,-5,5,-5,-5,7,5,1],[-4,-1,-9,-10,5,-7,-9,-3,6,1,1,-4,-8,4,8],[1,-6,8,7,4,-1,-4,-1,1,-6,3,-8,-8,9,-2],[-7,8,5,7,-4,-3,1,5,-6,-1,9,-2,10,-5,-9],[-5,-10,-10,-1,-7,7,9,-7,1,-3,6,8,-10,7,9],[-2,4,7,7,8,-2,3,-4,10,-2,2,6,5,10,1],[9,4,-3,5,9,-3,-2,-2,7,-4,4,6,-7,6,-6]],[[-9,-8,8,3,3,-9,-3,-3,7,-7,-6,8,3,-6,5],[5,6,-8,-7,8,-3,4,-7,-10,-4,5,2,-5,-1,3],[2,-1,-3,3,-9,8,5,7,9,-6,8,5,5,4,-3],[-1,7,3,10,-10,4,-1,9,3,-9,3,2,-5,9,2],[-8,-7,4,5,-6,3,2,-3,5,-1,6,-10,-1,5,6],[-4,-10,-9,10,8,-10,6,-6,5,6,4,7,8,10,-9],[-1,-1,3,3,6,9,-4,-10,-5,-2,10,-3,-3,-6,-4],[-9,10,-6,-10,6,2,-5,-2,9,-1,-8,-10,-7,-2,5],[-8,3,-4,2,-9,1,-6,2,-3,-5,1,-3,-4,3,3],[-4,-2,-10,-9,2,1,-1,-2,-4,3,9,-3,-6,-5,3],[-9,-1,-7,7,3,3,-5,-10,-7,-1,-2,-6,-5,1,3],[7,2,-3,9,4,1,6,2,-10,10,1,2,-8,2,-6],[-5,7,5,6,-1,-5,-8,8,-9,-10,10,1,-1,-10,8]],[[7,2,-1,-3,-10,7,-7,-8,-6,-3,-6,-8,-6,7,3],[3,9,6,-2,-8,3,8,2,-7,5,-3,-3,-9,1,7],[1,5,-5,1,10,-10,5,-7,5,5,1,2,-10,-7,7],[6,3,-2,-10,8,2,-7,5,6,-5,10,1,-2,-3,4],[2,-1,-9,5,-6,3,10,-7,-1,5,-5,4,8,-9,-4],[2,10,2,8,3,10,-4,-4,-5,7,1,-8,-8,-10,9],[9,-1,-9,-10,-10,-1,-9,-1,7,7,8,5,-4,4,1],[9,7,9,-5,-10,-4,-3,7,5,2,7,-2,7,5,-2],[-5,6,-3,7,-8,2,10,-4,-1,-1,10,2,10,6,1],[4,10,-7,9,-10,-2,8,8,-1,10,2,1,10,5,9],[-7,-1,4,-10,1,9,-2,7,10,1,-1,-10,10,6,-9],[9,-9,-2,8,6,-2,7,6,8,-4,-6,3,-9,-9,8],[9,3,-10,1,-7,-1,5,-4,2,5,-10,-2,10,-8,6]],[[6,-5,-3,3,3,4,8,-2,8,-2,-1,-7,-7,-6,-3],[-9,8,-7,-9,9,-10,-5,-10,-1,-10,-3,-7,-6,5,-9],[4,7,-2,-7,7,-4,-6,-5,8,7,1,1,-8,4,8],[-4,-1,-4,-7,5,-6,-1,10,9,4,-7,5,4,-6,-9],[-2,-7,-5,-6,-4,8,-4,10,-7,-3,6,7,-10,5,9],[-2,-6,-4,2,7,4,3,6,-1,4,-5,6,10,-5,3],[8,5,-6,6,10,3,-1,-2,-2,10,-7,-6,9,8,-2],[7,8,-5,10,2,7,6,2,4,8,-9,1,9,-3,3],[10,7,-10,4,-8,-4,2,4,5,-5,4,-10,-9,-6,-8],[10,-6,5,1,-10,6,3,-1,1,7,-10,9,-7,-1,-3],[-9,-4,-1,-3,-10,1,-6,-3,3,2,1,-10,-4,-1,9],[1,-10,-5,5,3,-10,3,-1,4,2,6,9,-4,-5,5],[2,2,-10,2,4,3,10,-1,-2,-6,10,-8,10,-10,-8]]], dtype = "uint64")#candidate|10870|(12, 13, 15)|const|uint64
bop_10871 = relay.add(var_10869.astype('uint64'), relay.reshape(const_10870.astype('uint64'), relay.shape_of(var_10869))) # shape=(12, 13, 15)
func_6956_call = mod.get_global_var('func_6956')
func_6957_call = mutated_mod.get_global_var('func_6957')
call_10877 = relay.TupleGetItem(func_6956_call(), 0)
call_10878 = relay.TupleGetItem(func_6957_call(), 0)
func_5773_call = mod.get_global_var('func_5773')
func_5778_call = mutated_mod.get_global_var('func_5778')
const_10890 = relay.const([-0.691444,-3.953918,8.469180,8.310245,-1.123395,-6.079417,-9.188052,-2.807720,-4.295348,2.149120,5.488307,-4.335286,-6.536506,-5.129451,-2.617745,9.112763,5.689278,4.421412,9.054416,-6.687412,6.079153,-4.833725,-1.506316,-1.756809,-3.527279,3.958480,9.133928,-0.274265,-9.854580,9.149313,7.649844,-1.658339,6.050825,7.897313,-6.366682,-4.049932,-0.944301,-1.854777,6.622256,-8.870835,-1.407625,4.281450,7.927906,8.355464,-4.374167,-6.271802,8.370064,7.194085,-1.999637,7.452921,-0.517137,-3.122241,3.241583,2.037996,-7.335484,-5.441642,-8.615681,-9.244840,9.768319,1.873365,4.224204,2.936998,-5.383385,7.140398,1.069157,-4.644157,-0.316708,-0.884306,6.089058,-3.198107,6.153341,-6.389425,6.573552,4.779005,-3.567555,-0.886485,4.786826,-8.831607,-3.890835,-1.768697,-2.192237,-4.408291,-0.591946,-9.543460,-9.058610,6.972644,1.312216,5.532618,-3.324184,9.651748,-2.737410,-9.815095,3.692386,2.472021,-8.694851,9.422215,-5.852308,9.932768,8.252861,-1.589804,1.210847,1.288376,0.794764,0.463127,-4.991263,-7.644036,-4.651234,-7.827978,9.258144,-6.237445,9.251209,0.155951,0.652082,-1.453280,-3.239156,-2.184165,-7.696989,2.459490,5.752672,-4.061002], dtype = "float64")#candidate|10890|(120,)|const|float64
const_10891 = relay.const([-3,2,-8,-7,3,-3,-3,9,-3,10,-4,5,-3,3,-3,-6,-5,-6,-7,6,-5,2,7,9,-6,9,5,-1,-9,2,-9,8,9,8,9,5,2,-1,-1,-2,9,-6,-5,5,-1,6,5,3,10,-9,-5,2,-2,-10,-5,-9,-2,-1,1,-3,-2,2,4,1,-7,4,5,-1,3,1,2,4,-4,-2,-2,-7,3,2,-7,3,3,5,-5,6,-8,6,6,7,-7,-5,4,-3,-3,8,10,-3,-9,1,-7,-4,4,8,-9,10,-3,-5,10,6,5,-5,-5,7,9,2,7,-4,5,2,4,-2,-8,-6,4,-2,-7,-5,-7,8,4,-3,-5,1,6,6,5,1,-4,2,10,-1,2,9,10,-5,-9,-5,-5,8,2,-5,3,-2,10,7,9,7,3,1,5,-8,-4,1,-9,-3,3,8,2,3,4,-4,-7,4,-6,5,-1,-4,-4,-6,-3,6,5,-2,-5,-8,4,-4,2,-2,5,8,8,2,-8,-9,-7,7,-10,-8,-5,-6,10,-1,-1,9,-8,-3,10,2,-6,-8,-5,-3,-5,2,9,8,-1,2,-2,8,-7,-8,-6,2,1,-5,7,1,-10,2,2,-9,-1,-5,-1,4,-1,4,3,1,7,10,3,4,6,-5,7,1,6,-2,-6,4,9,7,3,5,4,-4,7,-2,-5,1,-4,2,8,-4,2,-6,-5,4,10,10,5,3,-1,4,6,9,-8,8,7,-2,2,-10,10,-7,-3,6,-10,-9,6,8,-7,-9,-10,-2,-9,-5,-2,-7,1,5,-10,4,-2,10,6,-7,5,-9,5,1,4,4,-3,10,-5,-9,-10,5,-4,9,3,3,3,2,-3,-1,-8,-5,-8,-4,4,9,6,3,1,2,-9,3,-8,10,-5,-8,-8,4,10,10,-3,7,5,1,-3,3,9,1,-10,-9,-2,9,-10,5,-3,5,3,7,-1,7,3,-3,5,-10,-7,-3,-5,-8,-7,6,-7,8,-10,-2,-5,-4,-7,9,-3,9,7,8,4,9,-10,-3,-4,8,8,-7,-9,1,8,-9,10,-10,10,1,5,-9,-4,3,-3,-4,-3,6,-1,-9,9,-1,-6,6,-2,-3,-6,3,5,8,1,1,-4,-7,3,6,-3,-1,-10,6,5,-1,4,-2,2,-6,-3,-8,-3,-2,10,-8,-6,4,5,10,-1,-2,-4,1,6,8,4,6,10,4,7,5,-1,1,-8,8,1,6,6,-1,7,-10,7,8,6,-1,4,-6,4,-2,10,6,10,7,9,8,9,-7,-6,6,-7,-4,-3,-7,-10,3,-9,-1,9,6,-10,-4,-4,7,-5,9,2,-6,-6,3,-4,-7,-5,3,-8,4,5,7,8,-9,-9,-9,-4,7,10,5,8,6,-2,-9,-9,-8,-8,4,-9,3,3,-10,-8,6,-10,-1,-5,-4,-5,-7,4,1,-8,-10,-7,-8,6,7,6,-2,-6,-7,-8,-8,-1,-9,8,-9,-4,7,3,-4,-5,2,6,-10,-7,-5,-7,9,-10,3,8,-8,10,-6,3,1,-10,-1,-9,3,9,10,-3,-6,-9,10,-2,2,4,-6,-5,-4,1,5,8,5,-6,-7,-8,-9,-3,-4,7,-8,3,5], dtype = "int64")#candidate|10891|(616,)|const|int64
var_10892 = relay.var("var_10892", dtype = "float64", shape = (39,))#candidate|10892|(39,)|var|float64
call_10889 = relay.TupleGetItem(func_5773_call(relay.reshape(const_10890.astype('float64'), [120,]), relay.reshape(const_10891.astype('int64'), [616,]), relay.reshape(var_10892.astype('float64'), [39,]), ), 8)
call_10893 = relay.TupleGetItem(func_5778_call(relay.reshape(const_10890.astype('float64'), [120,]), relay.reshape(const_10891.astype('int64'), [616,]), relay.reshape(var_10892.astype('float64'), [39,]), ), 8)
func_7852_call = mod.get_global_var('func_7852')
func_7854_call = mutated_mod.get_global_var('func_7854')
call_10902 = relay.TupleGetItem(func_7852_call(), 0)
call_10903 = relay.TupleGetItem(func_7854_call(), 0)
const_10904 = relay.const([-8.028636,-9.633391,4.468172,6.627383,9.008756,-0.281397,-7.804701,-3.942199,1.501179,-2.535844,7.937924,0.222866,-4.275621,-7.470538,-7.928908,-5.315441,-6.903476,0.524069,-6.014587,0.033187,-3.035222,-6.040937,-0.974023,-0.373527,9.189401,6.101565,7.299882,8.269525,4.285811,2.631957,9.044417,-3.815604,9.982970,0.688790,-9.025278,5.654199,5.927668,3.446331,0.839191], dtype = "float64")#candidate|10904|(39,)|const|float64
bop_10905 = relay.multiply(var_10892.astype('uint16'), relay.reshape(const_10904.astype('uint16'), relay.shape_of(var_10892))) # shape=(39,)
output = relay.Tuple([bop_10871,call_10877,call_10889,const_10890,const_10891,call_10902,bop_10905,])
output2 = relay.Tuple([bop_10871,call_10878,call_10893,const_10890,const_10891,call_10903,bop_10905,])
func_10913 = relay.Function([var_10869,var_10892,], output)
mod['func_10913'] = func_10913
mod = relay.transform.InferType()(mod)
var_10914 = relay.var("var_10914", dtype = "uint64", shape = (12, 13, 15))#candidate|10914|(12, 13, 15)|var|uint64
var_10915 = relay.var("var_10915", dtype = "float64", shape = (39,))#candidate|10915|(39,)|var|float64
output = func_10913(var_10914,var_10915,)
func_10916 = relay.Function([var_10914,var_10915,], output)
mutated_mod['func_10916'] = func_10916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_10928 = relay.TupleGetItem(func_5146_call(), 0)
call_10929 = relay.TupleGetItem(func_5148_call(), 0)
func_10481_call = mod.get_global_var('func_10481')
func_10483_call = mutated_mod.get_global_var('func_10483')
call_10930 = relay.TupleGetItem(func_10481_call(), 0)
call_10931 = relay.TupleGetItem(func_10483_call(), 0)
func_7502_call = mod.get_global_var('func_7502')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_10933 = relay.TupleGetItem(func_7502_call(), 5)
call_10934 = relay.TupleGetItem(func_7503_call(), 5)
func_9833_call = mod.get_global_var('func_9833')
func_9835_call = mutated_mod.get_global_var('func_9835')
var_10938 = relay.var("var_10938", dtype = "uint32", shape = (2, 2))#candidate|10938|(2, 2)|var|uint32
call_10937 = relay.TupleGetItem(func_9833_call(relay.reshape(var_10938.astype('uint32'), [4,])), 0)
call_10939 = relay.TupleGetItem(func_9835_call(relay.reshape(var_10938.astype('uint32'), [4,])), 0)
func_7502_call = mod.get_global_var('func_7502')
func_7503_call = mutated_mod.get_global_var('func_7503')
call_10940 = relay.TupleGetItem(func_7502_call(), 3)
call_10941 = relay.TupleGetItem(func_7503_call(), 3)
output = relay.Tuple([call_10928,call_10930,call_10933,call_10937,var_10938,call_10940,])
output2 = relay.Tuple([call_10929,call_10931,call_10934,call_10939,var_10938,call_10941,])
func_10942 = relay.Function([var_10938,], output)
mod['func_10942'] = func_10942
mod = relay.transform.InferType()(mod)
mutated_mod['func_10942'] = func_10942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10943 = relay.var("var_10943", dtype = "uint32", shape = (2, 2))#candidate|10943|(2, 2)|var|uint32
func_10942_call = mutated_mod.get_global_var('func_10942')
call_10944 = func_10942_call(var_10943)
output = call_10944
func_10945 = relay.Function([var_10943], output)
mutated_mod['func_10945'] = func_10945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8367_call = mod.get_global_var('func_8367')
func_8368_call = mutated_mod.get_global_var('func_8368')
call_10956 = func_8367_call()
call_10957 = func_8367_call()
func_4580_call = mod.get_global_var('func_4580')
func_4581_call = mutated_mod.get_global_var('func_4581')
call_10968 = func_4580_call()
call_10969 = func_4580_call()
output = relay.Tuple([call_10956,call_10968,])
output2 = relay.Tuple([call_10957,call_10969,])
func_10988 = relay.Function([], output)
mod['func_10988'] = func_10988
mod = relay.transform.InferType()(mod)
output = func_10988()
func_10989 = relay.Function([], output)
mutated_mod['func_10989'] = func_10989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_11004 = relay.TupleGetItem(func_4410_call(), 0)
call_11005 = relay.TupleGetItem(func_4412_call(), 0)
func_7526_call = mod.get_global_var('func_7526')
func_7530_call = mutated_mod.get_global_var('func_7530')
const_11045 = relay.const(-3, dtype = "uint32")#candidate|11045|()|const|uint32
var_11046 = relay.var("var_11046", dtype = "uint32", shape = (1, 4))#candidate|11046|(1, 4)|var|uint32
call_11044 = relay.TupleGetItem(func_7526_call(relay.reshape(const_11045.astype('uint32'), []), relay.reshape(var_11046.astype('uint32'), [4,]), ), 3)
call_11047 = relay.TupleGetItem(func_7530_call(relay.reshape(const_11045.astype('uint32'), []), relay.reshape(var_11046.astype('uint32'), [4,]), ), 3)
output = relay.Tuple([call_11004,call_11044,const_11045,var_11046,])
output2 = relay.Tuple([call_11005,call_11047,const_11045,var_11046,])
func_11059 = relay.Function([var_11046,], output)
mod['func_11059'] = func_11059
mod = relay.transform.InferType()(mod)
var_11060 = relay.var("var_11060", dtype = "uint32", shape = (1, 4))#candidate|11060|(1, 4)|var|uint32
output = func_11059(var_11060)
func_11061 = relay.Function([var_11060], output)
mutated_mod['func_11061'] = func_11061
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11084 = relay.var("var_11084", dtype = "float64", shape = (5, 5, 5))#candidate|11084|(5, 5, 5)|var|float64
uop_11085 = relay.sigmoid(var_11084.astype('float64')) # shape=(5, 5, 5)
output = relay.Tuple([uop_11085,])
output2 = relay.Tuple([uop_11085,])
func_11094 = relay.Function([var_11084,], output)
mod['func_11094'] = func_11094
mod = relay.transform.InferType()(mod)
mutated_mod['func_11094'] = func_11094
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11095 = relay.var("var_11095", dtype = "float64", shape = (5, 5, 5))#candidate|11095|(5, 5, 5)|var|float64
func_11094_call = mutated_mod.get_global_var('func_11094')
call_11096 = func_11094_call(var_11095)
output = call_11096
func_11097 = relay.Function([var_11095], output)
mutated_mod['func_11097'] = func_11097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_11141 = relay.TupleGetItem(func_4849_call(), 0)
call_11142 = relay.TupleGetItem(func_4850_call(), 0)
output = relay.Tuple([call_11141,])
output2 = relay.Tuple([call_11142,])
func_11147 = relay.Function([], output)
mod['func_11147'] = func_11147
mod = relay.transform.InferType()(mod)
mutated_mod['func_11147'] = func_11147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11147_call = mutated_mod.get_global_var('func_11147')
call_11148 = func_11147_call()
output = call_11148
func_11149 = relay.Function([], output)
mutated_mod['func_11149'] = func_11149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9878_call = mod.get_global_var('func_9878')
func_9880_call = mutated_mod.get_global_var('func_9880')
call_11185 = relay.TupleGetItem(func_9878_call(), 0)
call_11186 = relay.TupleGetItem(func_9880_call(), 0)
output = call_11185
output2 = call_11186
func_11217 = relay.Function([], output)
mod['func_11217'] = func_11217
mod = relay.transform.InferType()(mod)
mutated_mod['func_11217'] = func_11217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11217_call = mutated_mod.get_global_var('func_11217')
call_11218 = func_11217_call()
output = call_11218
func_11219 = relay.Function([], output)
mutated_mod['func_11219'] = func_11219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_11235 = func_4460_call()
call_11236 = func_4460_call()
func_3087_call = mod.get_global_var('func_3087')
func_3089_call = mutated_mod.get_global_var('func_3089')
var_11249 = relay.var("var_11249", dtype = "float64", shape = (450,))#candidate|11249|(450,)|var|float64
call_11248 = func_3087_call(relay.reshape(var_11249.astype('float64'), [15, 3, 10]))
call_11250 = func_3087_call(relay.reshape(var_11249.astype('float64'), [15, 3, 10]))
output = relay.Tuple([call_11235,call_11248,var_11249,])
output2 = relay.Tuple([call_11236,call_11250,var_11249,])
func_11257 = relay.Function([var_11249,], output)
mod['func_11257'] = func_11257
mod = relay.transform.InferType()(mod)
var_11258 = relay.var("var_11258", dtype = "float64", shape = (450,))#candidate|11258|(450,)|var|float64
output = func_11257(var_11258)
func_11259 = relay.Function([var_11258], output)
mutated_mod['func_11259'] = func_11259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10094_call = mod.get_global_var('func_10094')
func_10096_call = mutated_mod.get_global_var('func_10096')
call_11286 = relay.TupleGetItem(func_10094_call(), 0)
call_11287 = relay.TupleGetItem(func_10096_call(), 0)
func_9531_call = mod.get_global_var('func_9531')
func_9533_call = mutated_mod.get_global_var('func_9533')
call_11291 = relay.TupleGetItem(func_9531_call(), 1)
call_11292 = relay.TupleGetItem(func_9533_call(), 1)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_11297 = relay.TupleGetItem(func_4849_call(), 0)
call_11298 = relay.TupleGetItem(func_4850_call(), 0)
output = relay.Tuple([call_11286,call_11291,call_11297,])
output2 = relay.Tuple([call_11287,call_11292,call_11298,])
func_11299 = relay.Function([], output)
mod['func_11299'] = func_11299
mod = relay.transform.InferType()(mod)
mutated_mod['func_11299'] = func_11299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11299_call = mutated_mod.get_global_var('func_11299')
call_11300 = func_11299_call()
output = call_11300
func_11301 = relay.Function([], output)
mutated_mod['func_11301'] = func_11301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_11441 = relay.TupleGetItem(func_7885_call(), 2)
call_11442 = relay.TupleGetItem(func_7886_call(), 2)
output = relay.Tuple([call_11441,])
output2 = relay.Tuple([call_11442,])
func_11445 = relay.Function([], output)
mod['func_11445'] = func_11445
mod = relay.transform.InferType()(mod)
mutated_mod['func_11445'] = func_11445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11445_call = mutated_mod.get_global_var('func_11445')
call_11446 = func_11445_call()
output = call_11446
func_11447 = relay.Function([], output)
mutated_mod['func_11447'] = func_11447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9644_call = mod.get_global_var('func_9644')
func_9645_call = mutated_mod.get_global_var('func_9645')
call_11477 = func_9644_call()
call_11478 = func_9644_call()
output = relay.Tuple([call_11477,])
output2 = relay.Tuple([call_11478,])
func_11503 = relay.Function([], output)
mod['func_11503'] = func_11503
mod = relay.transform.InferType()(mod)
output = func_11503()
func_11504 = relay.Function([], output)
mutated_mod['func_11504'] = func_11504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8534_call = mutated_mod.get_global_var('func_8534')
call_11511 = relay.TupleGetItem(func_8532_call(), 0)
call_11512 = relay.TupleGetItem(func_8534_call(), 0)
uop_11520 = relay.acos(call_11511.astype('float32')) # shape=(14, 5, 13)
uop_11522 = relay.acos(call_11512.astype('float32')) # shape=(14, 5, 13)
func_7381_call = mod.get_global_var('func_7381')
func_7383_call = mutated_mod.get_global_var('func_7383')
call_11528 = relay.TupleGetItem(func_7381_call(), 0)
call_11529 = relay.TupleGetItem(func_7383_call(), 0)
func_10913_call = mod.get_global_var('func_10913')
func_10916_call = mutated_mod.get_global_var('func_10916')
const_11534 = relay.const([-6,2,3,7,-8,-6,-1,-8,8,-6,-1,-5,-10,-3,7,-2,-10,-10,10,6,4,-9,-2,-9,2,-5,8,7,8,-10,-3,-10,9,-7,9,-6,-7,8,-3,2,-4,10,7,-10,7,-4,4,-5,-5,-1,6,-5,-4,4,2,5,-3,10,4,8,9,4,-5,-6,1,-3,7,-10,3,-10,-2,-2,2,6,1,-1,-8,-4,4,-3,7,2,6,-7,-7,-5,-4,5,-9,3,-7,-8,1,-5,-4,-10,4,7,5,10,-10,3,10,-1,-9,6,-1,10,-10,7,-5,5,8,-1,5,-6,-4,9,7,4,-4,-1,-7,-7,9,-9,10,6,-5,2,10,-4,-5,10,-3,-7,5,2,-2,-10,-10,5,-4,-7,-10,8,-6,-6,-5,2,-1,5,-8,1,-5,-1,10,6,-5,-5,-3,-4,-7,-10,7,2,-3,-7,5,3,8,6,7,4,-6,-8,-1,-8,5,1,-3,3,10,-9,7,-7,-5,5,-9,-6,5,4,10,-2,-3,8,-6,2,-2,-4,-2,-4,-6,-10,7,9,-2,7,6,-9,-2,5,-10,7,7,-1,-10,7,-5,10,5,-3,2,-10,-9,9,6,1,-2,-7,10,7,6,-8,5,2,-7,8,3,2,-9,-3,-7,-2,-5,-8,-1,-4,1,6,10,-7,-3,8,2,-9,-3,7,-1,8,10,-10,3,5,-6,1,1,4,-2,3,4,-7,8,-6,-3,-4,2,-1,8,10,-7,9,-8,3,7,4,-9,8,-4,-8,-1,-7,6,10,4,-7,9,-2,-1,7,-2,-7,1,-10,-2,-10,-1,-5,-7,-1,3,5,-8,-10,-1,-6,7,5,1,-3,-6,-3,1,3,5,10,-6,1,-9,2,8,-4,1,5,7,-4,-10,-9,7,3,-10,9,8,-9,-2,9,-8,7,4,-1,9,-5,2,-1,8,10,-7,-5,10,-1,6,2,-3,-5,-10,-8,-2,9,-7,-5,-6,-6,-6,5,-6,10,-6,-9,-3,8,1,-4,8,-8,-4,3,-2,3,9,-5,6,-10,10,-3,-2,-6,-6,-7,-4,3,-10,7,5,-9,8,1,9,-6,1,-2,2,-7,10,5,8,3,-4,7,10,4,-2,-2,6,-2,1,1,3,4,-9,7,-8,-5,-1,-2,10,1,-10,-3,-4,5,-10,-9,-2,6,3,-1,4,-1,-8,-7,8,-8,-2,-5,9,-2,-4,-10,5,2,-9,-8,6,-9,-4,-3,-6,-9,4,-5,-3,2,9,6,7,-3,-10,1,-2,-10,-9,-9,4,3,3,2,4,-5,-7,-8,-10,3,4,6,6,-10,-9,-10,-8,-2,3,-7,10,-2,3,-1,3,-1,-10,10,-4,-3,-1,7,-9,8,-5,-9,-5,1,-10,-10,-10,9,9,8,-2,-6,7,2,-2,-8,-5,1,-7,-9,7,-2,-10,7,-10,1,-9,5,-10,-1,-7,-7,-5,2,1,1,-3,-4,-3,2,-9,5,2,3,-5,2,3,-2,-8,-2,-10,-6,7,-3,3,4,-10,10,-7,4,7,-3,5,-3,-2,1,-10,-4,-9,7,-4,-5,-10,-6,6,-10,-6,-5,8,4,-5,-3,-4,-3,-4,6,-3,-2,-4,1,-8,4,4,3,-1,4,-1,-10,2,9,-4,-3,6,10,-4,1,-4,6,-8,1,-5,5,2,3,7,-1,7,-7,-1,-4,-2,7,-3,7,1,1,5,-5,1,2,-2,-8,8,3,-6,4,-5,5,5,9,10,-5,-8,-1,-10,7,-7,-2,-4,-6,-5,8,3,-8,-3,-8,9,-7,4,7,10,-8,3,-2,7,5,10,2,7,4,6,-5,5,-3,-10,3,-6,-7,-2,-4,-8,-1,-6,-2,10,5,7,-3,5,-1,8,-7,6,-5,-4,7,2,10,10,1,9,-8,-9,9,10,-9,4,5,9,-8,1,-6,-3,8,-10,5,-6,-6,-5,7,4,6,-1,10,10,-6,5,-1,10,-4,-8,-10,4,-9,10,6,1,4,10,-5,-3,-1,-3,-9,-4,3,-1,-8,8,6,5,-4,2,10,3,6,6,-6,-2,2,-7,-1,6,3,-9,2,1,-10,-5,8,-8,3,2,3,-4,1,7,-10,-1,9,-4,-4,8,-9,-4,10,-1,-6,-4,-8,-1,2,3,5,8,4,6,10,-1,8,8,-7,-2,-2,1,7,-1,2,-4,7,-2,6,10,1,-5,-9,6,9,-9,4,-3,4,1,-5,4,7,-5,-3,6,-6,-2,3,-1,5,5,1,-10,9,2,6,-8,-1,5,7,7,-4,8,-6,2,-2,1,-5,8,-4,-10,6,5,-10,-1,-6,10,-9,9,-1,9,8,-5,-2,-8,3,1,7,-7,8,4,6,4,-6,1,6,1,9,-8,10,9,8,-3,8,4,7,10,3,9,8,7,9,9,-5,-8,7,-8,-9,-9,-2,3,-2,5,8,7,1,2,-3,7,-10,-2,-6,9,3,4,-5,-7,9,-4,-5,5,-6,-5,7,-8,-10,-1,3,2,2,-1,3,3,1,1,8,-1,10,-5,9,4,-6,-6,7,-2,3,3,5,-10,-3,2,6,6,-9,-4,6,10,3,10,-5,6,-8,-6,6,1,6,9,-5,9,-7,4,1,5,1,5,-10,4,1,-2,5,-4,-5,4,-9,-5,5,10,-5,-3,2,4,8,-9,7,6,5,2,3,1,8,8,5,-3,-7,-1,-2,-1,3,7,-3,2,3,9,2,9,6,-7,-7,5,5,-3,1,7,-7,-5,-9,10,3,-9,-1,-8,6,-10,-6,-7,1,9,-5,9,1,4,-1,2,-6,-2,9,-4,7,-10,-10,-3,-8,-6,-9,6,-7,1,-5,-3,-6,-7,-4,10,8,-4,8,1,2,-8,10,-10,-2,-6,-6,9,-5,4,1,1,-7,-8,-4,8,4,-6,10,5,9,-9,2,4,4,9,6,-5,-6,-6,1,8,-10,2,-2,-1,10,-5,-10,2,-1,-9,2,9,-6,10,-1,-3,-1,-10,-3,6,-3,-6,2,-6,8,9,1,7,3,5,4,-6,4,-9,-8,-10,6,3,3,-10,-5,2,4,-3,7,-2,7,-9,3,10,5,-2,6,-8,3,2,4,5,-3,9,-10,2,-9,10,9,5,8,4,1,2,9,-5,8,-4,-10,-3,-4,-8,6,-8,6,8,1,9,-5,9,7,-10,3,7,7,-2,3,-7,-7,-5,-8,-6,-6,-2,-6,-8,4,9,3,1,-6,-2,-2,-9,4,2,6,3,-5,-6,8,5,3,7,9,-6,10,5,9,-3,-5,-6,-2,-6,6,9,5,5,-7,-4,10,-1,-9,6,-10,10,-3,8,-7,-4,6,8,7,-1,-6,3,8,8,-2,-5,5,-8,4,-6,2,-6,3,-2,-5,-7,2,7,-5,7,-3,-8,10,7,-5,4,2,8,2,-10,-6,8,-6,-8,-3,-8,9,-5,3,-10,-4,8,2,3,-7,-3,-9,-9,-7,6,3,-8,-2,-1,2,5,-6,2,-10,-4,-8,-10,-7,4,7,5,5,-4,6,-2,-7,-6,4,10,5,-1,-10,-9,-9,2,4,5,1,-6,5,5,9,-2,9,4,-8,6,5,7,-10,-7,-8,-6,4,-8,-10,-8,6,1,-3,-9,10,-3,5,-9,10,-1,-10,1,-7,-2,2,7,1,-3,-2,9,2,-9,1,1,-3,4,-9,9,2,4,-5,-1,-10,-3,9,-6,-6,-7,2,10,10,1,7,-5,5,-4,-2,-7,1,3,-3,-10,-4,6,5,-3,10,-2,4,-7,-7,-9,5,-9,5,-6,-5,-9,-3,6,5,-3,-1,-3,2,-6,-2,-8,-1,3,3,8,8,-6,4,-1,1,-3,8,-1,-9,-9,-4,-8,-6,-2,-2,8,8,3,7,-1,7,-3,4,-5,-1,-4,3,-9,-2,-9,-9,-6,-2,1,6,-8,-9,-10,-4,-6,1,-1,9,-5,-9,9,3,7,6,-5,-1,5,-3,-3,-2,-4,-8,-7,-3,9,-9,3,4,5,9,4,2,-2,-6,2,3,-9,10,-7,10,-8,4,9,1,-10,6,2,5,3,-8,-7,2,1,4,9,-6,1,6,10,5,-10,5,-9,8,2,-8,9,5,-3,2,10,-9,-7,-2,4,8,8,-8,6,8,3,4,-7,-6,7,4,-3,10,-8,9,-8,8,4,3,-5,7,7,2,2,4,-5,7,-9,-9,9,-1,-9,-3,8,-3,6,-10,1,5,-9,1,5,-3,-8,3,2,-4,-4,4,-4,-4,-4,1,6,7,5,9,-9,-4,5,-2,-3,8,5,1,6,10,-8,3,9,1,-9,1,3,5,-5,6,5,-7,-5,-2,4,1,4,-9,-6,-4,9,5,3,1,-8,9,-1,6,7,-5,1,-6,-1,-6,3,4,-5,5,8,9,-5,1,-5,1,6,-4,3,-10,2,3,-7,-9,-5,-2,2,-1,10,-4,1,-6,1,-4,9,-9,1,8,9,2,-2,9,6,3,-3,10,2,1,-7,8,-8,-8,-10,-6,-2,3,3,-9,3,6,9,-2,-3,4,7,-7,-10,-3,-1,-9,9,8,7,4,1,8,7,3,-2,-1,9,-3,3,9,-6,7,-2,9,4,9,-3,-7,6,10,7,6,-9,6,4,-6,-6,8,-9,7,-10,1,5,4,6,-1,5,-10,8,-8,9,-3,-8,3,7,3,10,3,-9,-9,2,1,-1,2,5,2,-4,1,7,1,7,5,7,-3,6,-5,-1,-6,5,2,7,-6,-2,-5,2,-4,10,-4,-9,5,-8,2,5,4,5,10,1,-7,2,1,-9,-10,-6,8,-1,1,-3,9,-10,-8,8,-10,-5,-1,8,2,8,-6,8,2,-9,9,5,-10,2,3,-7,10,-8,10,6,3,3,10,7,3,4,-6,3,-5,3,6,1,-3,-8,4,4,-9,1,10,-3,2,6,-8,3,3,-1,5,4,10,-2,7,-6,-6,-8,-6,1,10,-7,6,2,-5,8,-7,-9,-6,5,-8,-4,7,1,4,-1,-9,1,-8,5,-7,5,-5,1,5,9,-7,8,-4,9,-8,10,-9,-3,5,-2,8,6,-2,-9,3,2,8,5,-8,-1,5,4,-4,2,-4,10,2,7,3,4,-3,-7,8,-4,8,-5,-7,-8,-7,-8,7,-2,6,-6,7,-6,-8,-1,8,-5,1,9,10,-8,-8,-7,-6,3,-10,2,8,-10,-4,-5,8,-7,1,-8,-3,-7,5,-5,2,-5,-8,-2,7,-5,2,-3,1,1,8,-2,-6,-2,-2,1,7,-6,5,3,1,4,9,6,-9,-3,-4,6,5,-8,4,-1,-5,6,-7,1,7,1,-3,8,-4,9,-8,-8,10,10,-7,-5,-7,2,1,4,-1,4,4,7,4,5,-8,3,-1,4,-5,8,-1,8,6,-10,8,2,-7,-9,-3,-1,7,1,-8,-6,5,4,6,7,-5,10,2,-5,-1,10,-9,6,-6,6,1,8,7,1,-6,-7,7,4,1,10,6,-7,2,4,10,3,-3,-9,-5,-4,-1,3,10,9,9,-7,-1,9,-10,1,-3,3,-7,6,3,2,3,-5,-5,8,6,-8,-10,8,9,9,-4,-10,3,3,-8,-1,2,-7,2,10,1,-5,-4,2,-2,9,-3,1,7,-5,10,-7,4,1,9,4,-9,4,1,9,7,3,9,10,-7,2,-1,-2,-4,8,4,5,2,9,5,9,7,4,6,-3,-6,-4,3,1,1,-3,3,10,-7,-9,8,6,9,-5,-3,2,3,-6,2,-6,-7,9,6,5,8,-8,9,-6,-4,-7,-9,-6,-3,-1,-2,-9,5,-8,7,8,7,-6,10,7,2,2,-1,4,-5,-2,-3,3,-8,10,-6,5,-4,10,-10,9,10,-3,-2,-6,1,3,10,-1,8,-6,-10,10,9,-10,-6,2,2,7,-10,2,-5,-5,-2,-3,-10,7,-9,5,-6,10,-6,7,8,4,1,9,-3,-8,3,-7,2,2,-10,1,4,7,-4,7,-2,-9,-9,8,-7,6,10,2,7,3,-4,3,-6,7,-9,-3,5,4,2,-5,8,8,3,8,-5,7,-5,-7,-5,4,-9,4,9,-8,-2,2,4,-8,2,-7,8,8,6,-6,-8,-6,-7,10,10,1,-1,-2,2,2,-7,-3,-4], dtype = "uint64")#candidate|11534|(2340,)|const|uint64
var_11535 = relay.var("var_11535", dtype = "float64", shape = (13, 3))#candidate|11535|(13, 3)|var|float64
call_11533 = relay.TupleGetItem(func_10913_call(relay.reshape(const_11534.astype('uint64'), [12, 13, 15]), relay.reshape(var_11535.astype('float64'), [39,]), ), 2)
call_11536 = relay.TupleGetItem(func_10916_call(relay.reshape(const_11534.astype('uint64'), [12, 13, 15]), relay.reshape(var_11535.astype('float64'), [39,]), ), 2)
func_10021_call = mod.get_global_var('func_10021')
func_10022_call = mutated_mod.get_global_var('func_10022')
call_11546 = relay.TupleGetItem(func_10021_call(), 1)
call_11547 = relay.TupleGetItem(func_10022_call(), 1)
func_6068_call = mod.get_global_var('func_6068')
func_6070_call = mutated_mod.get_global_var('func_6070')
const_11570 = relay.const([[8.714586,-4.897103,-9.684324,-4.299755,7.577339,5.643059,7.521115,8.781399,8.887422,-1.524407],[-4.733817,6.349664,-5.785468,-3.270133,5.238334,1.314543,-8.727837,-7.466077,0.471839,6.421994],[0.833398,4.263769,-2.790441,-3.203037,2.856855,-9.095694,8.359172,-8.522267,-0.866885,-9.606705],[4.251106,-2.347870,7.445476,-2.415552,5.494289,5.086019,9.287507,2.351712,8.971463,8.887396],[3.547639,9.379157,-9.431167,-7.478614,-0.230301,-0.054743,-2.755860,5.333414,4.738852,-6.078270],[-6.726792,-5.781275,5.855668,8.360828,4.040799,0.643169,-7.906102,-2.880159,-7.888574,-8.376353],[7.924396,-2.874161,7.273225,-0.832605,0.603710,-1.029369,-2.592564,6.182421,-3.469883,6.264917],[-6.250135,-5.587152,5.525701,1.930543,-4.419704,-5.218830,-0.456095,7.244836,8.310551,-1.979906],[5.809847,-2.160507,8.652350,4.897562,-5.428903,-1.078211,2.648433,-7.994886,7.490773,-0.287618],[5.277811,1.640592,2.019979,3.259646,-4.612773,8.659962,-2.765166,-0.547539,-7.157828,-7.151224],[-7.913002,1.718107,8.388948,-8.956803,1.178636,-4.311152,4.222405,-4.034473,8.847331,2.322935],[8.309120,9.174197,-3.828455,-3.279023,5.068805,-1.636815,5.782426,9.442361,8.450107,5.851581],[-0.687731,6.156086,3.117651,-3.447667,1.639499,7.407623,-2.786295,3.975267,-3.150517,9.110996],[-9.453092,5.224202,3.400041,-1.816204,-4.024901,1.093779,-5.441611,-1.689277,-0.390974,-8.423299],[7.567170,5.753738,-5.168034,-4.910286,-8.275296,-9.221137,3.512201,-9.180915,-0.409533,1.462329],[-3.234137,8.942623,1.273688,-1.920482,-0.834331,-9.570076,-7.189579,9.730102,-6.367583,3.163062],[-4.852370,4.459535,8.070505,-3.167832,-7.184116,-4.015673,9.251786,0.421290,-0.070533,-4.817502],[-5.728611,-8.865773,-2.453977,9.575993,0.630239,4.443664,-0.209065,-9.763844,-6.747885,1.476275],[-3.097998,7.685210,5.727729,9.905534,4.874760,-0.322895,-8.207148,-1.623256,1.622593,0.937609],[3.421687,-9.736912,5.859363,6.704784,8.145814,-5.997165,2.751140,2.909300,4.183694,-8.537539],[0.615161,-5.596295,9.658540,-7.750633,3.453680,2.939554,9.725864,-3.132719,-6.516420,-1.529948],[3.467474,-6.471160,8.638726,0.268738,-4.545904,1.450210,0.990074,7.893966,-3.544138,8.884560],[8.052599,-2.937936,-1.568125,9.761575,4.577644,-5.785820,-7.567111,4.112880,7.308026,-1.462611],[-3.455869,9.621879,-4.711064,-1.590417,-6.189020,-5.587855,-1.770487,-9.017141,2.111817,-0.801312],[-7.623756,7.003015,5.971312,-4.641049,-2.679749,-6.842246,-9.375207,-6.040849,-0.764964,1.616968],[-9.558429,-5.369657,7.835239,5.433622,-7.049264,0.919064,-5.745224,0.776530,0.571220,-9.836695],[8.269572,-3.233734,-8.069890,-5.083735,8.687547,-6.581351,5.837842,-0.335895,7.237631,2.027118],[0.845829,-9.403477,-0.090251,4.275753,4.840157,0.673192,-4.916268,-1.027421,-8.910343,9.273860],[8.229183,6.073178,-6.337882,7.904259,2.381398,0.215770,0.601843,-4.299437,-0.504018,2.579223],[-7.913801,-2.813717,-5.686703,2.966605,0.176330,-7.204101,-7.965374,9.928833,4.751430,3.663887],[8.242671,-4.401266,-9.807054,-4.529169,-7.379432,6.473569,-5.614352,-5.056915,-6.492747,7.066315],[-2.151125,-7.352379,2.091741,-6.597688,-5.840240,1.807635,-7.276850,-2.973326,7.924103,3.431059],[-4.424969,-2.240079,-9.434798,7.708261,-2.582852,-4.296724,-1.815321,-6.347689,-6.094654,2.628885],[-8.281332,7.274526,-5.705772,9.683869,-4.867394,6.389217,3.257204,-9.319958,-0.850358,4.318970],[-8.546833,-7.147712,-5.149833,6.873202,7.535159,-0.979898,0.175202,-6.436742,0.231130,0.093066],[2.251306,7.240802,-6.715943,-2.659026,3.336844,-8.667896,-8.145844,8.064220,0.388727,2.847981],[1.229965,-3.999263,8.976586,-6.998023,-2.850068,8.804254,-6.623455,0.830449,-0.511389,-4.047563],[3.705209,4.819153,2.282237,-8.687104,1.013281,8.306592,0.753788,-5.616609,-4.340557,-7.282172],[-4.162226,-6.825216,-7.751656,-0.693855,-5.347751,-7.541237,7.702126,3.880679,-6.681631,7.197368],[5.935571,-1.907323,-9.973816,-3.505849,4.771127,1.648632,-0.928246,3.763928,1.821283,5.418151]], dtype = "float32")#candidate|11570|(40, 10)|const|float32
call_11569 = relay.TupleGetItem(func_6068_call(relay.reshape(const_11570.astype('float32'), [400,])), 1)
call_11571 = relay.TupleGetItem(func_6070_call(relay.reshape(const_11570.astype('float32'), [400,])), 1)
func_8417_call = mod.get_global_var('func_8417')
func_8420_call = mutated_mod.get_global_var('func_8420')
const_11575 = relay.const([2.883328,9.387298,-3.198542,-7.555024,4.612591,-9.181740,-7.881187,-9.682580,2.467694,-8.814067,1.244516,-0.868180,-5.688496,9.533537,-0.443457,0.807771,-6.053769,5.199809,-7.240620,-0.650490,-4.279336,2.126179,-5.430777,-2.063989,-1.393336,-7.130474,4.966893,-8.408204,-4.188226,-1.718934,1.917028,-1.574036,-5.511340,-6.920996,-9.441382,1.490933,7.943560,6.581836,-6.441647,-3.860561,-9.487753,-2.759239,0.494621,-8.977311,6.214815,3.804836,-9.988241,-2.263583,7.831131,-4.147225,6.984070,-3.872528,-9.365076,-5.778915,8.148763,1.594340,9.086885,3.774580,-0.843654,6.184605,-0.512420,-1.190731,-8.408042,-0.612347,9.354300,9.550757,-5.657914,-1.968400,3.968516,1.680802,1.957419,0.930628,6.849375,1.930979,-5.356083,0.032986,8.985309,7.815098,-4.502177,0.951887,-4.193942,-8.322955,-3.711511,-1.990847,4.140319,-2.219560,-8.263620,-5.587304,4.252537,-4.066818,-3.636326,-7.809642,3.207697,7.251560,9.917370,-3.130152,-7.117060,-9.827558,5.853782,-0.626666,1.070998,5.901137,-2.867324,0.032731,7.428247,1.922242,6.093684,-9.535674,-2.523997,-1.132601,-9.492640,3.424729,4.659802,-7.992478,-1.920908,1.985598,1.088447,-7.858080,-4.193473,4.449895], dtype = "float64")#candidate|11575|(120,)|const|float64
call_11574 = relay.TupleGetItem(func_8417_call(relay.reshape(const_11575.astype('float64'), [120,])), 2)
call_11576 = relay.TupleGetItem(func_8420_call(relay.reshape(const_11575.astype('float64'), [120,])), 2)
func_9905_call = mod.get_global_var('func_9905')
func_9907_call = mutated_mod.get_global_var('func_9907')
call_11593 = relay.TupleGetItem(func_9905_call(), 0)
call_11594 = relay.TupleGetItem(func_9907_call(), 0)
output = relay.Tuple([uop_11520,call_11528,call_11533,const_11534,var_11535,call_11546,call_11569,const_11570,call_11574,const_11575,call_11593,])
output2 = relay.Tuple([uop_11522,call_11529,call_11536,const_11534,var_11535,call_11547,call_11571,const_11570,call_11576,const_11575,call_11594,])
func_11617 = relay.Function([var_11535,], output)
mod['func_11617'] = func_11617
mod = relay.transform.InferType()(mod)
mutated_mod['func_11617'] = func_11617
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11618 = relay.var("var_11618", dtype = "float64", shape = (13, 3))#candidate|11618|(13, 3)|var|float64
func_11617_call = mutated_mod.get_global_var('func_11617')
call_11619 = func_11617_call(var_11618)
output = call_11619
func_11620 = relay.Function([var_11618], output)
mutated_mod['func_11620'] = func_11620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_11673 = relay.TupleGetItem(func_7885_call(), 2)
call_11674 = relay.TupleGetItem(func_7886_call(), 2)
output = relay.Tuple([call_11673,])
output2 = relay.Tuple([call_11674,])
func_11697 = relay.Function([], output)
mod['func_11697'] = func_11697
mod = relay.transform.InferType()(mod)
output = func_11697()
func_11698 = relay.Function([], output)
mutated_mod['func_11698'] = func_11698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4893_call = mod.get_global_var('func_4893')
func_4894_call = mutated_mod.get_global_var('func_4894')
call_11699 = relay.TupleGetItem(func_4893_call(), 3)
call_11700 = relay.TupleGetItem(func_4894_call(), 3)
output = call_11699
output2 = call_11700
func_11725 = relay.Function([], output)
mod['func_11725'] = func_11725
mod = relay.transform.InferType()(mod)
mutated_mod['func_11725'] = func_11725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11725_call = mutated_mod.get_global_var('func_11725')
call_11726 = func_11725_call()
output = call_11726
func_11727 = relay.Function([], output)
mutated_mod['func_11727'] = func_11727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5383_call = mod.get_global_var('func_5383')
func_5385_call = mutated_mod.get_global_var('func_5385')
call_11773 = relay.TupleGetItem(func_5383_call(), 1)
call_11774 = relay.TupleGetItem(func_5385_call(), 1)
func_6997_call = mod.get_global_var('func_6997')
func_6999_call = mutated_mod.get_global_var('func_6999')
call_11787 = func_6997_call()
call_11788 = func_6997_call()
func_9905_call = mod.get_global_var('func_9905')
func_9907_call = mutated_mod.get_global_var('func_9907')
call_11789 = relay.TupleGetItem(func_9905_call(), 0)
call_11790 = relay.TupleGetItem(func_9907_call(), 0)
func_10233_call = mod.get_global_var('func_10233')
func_10239_call = mutated_mod.get_global_var('func_10239')
const_11804 = relay.const(5, dtype = "uint32")#candidate|11804|()|const|uint32
var_11805 = relay.var("var_11805", dtype = "int32", shape = (1056,))#candidate|11805|(1056,)|var|int32
var_11806 = relay.var("var_11806", dtype = "float64", shape = (35,))#candidate|11806|(35,)|var|float64
var_11807 = relay.var("var_11807", dtype = "float32", shape = (364,))#candidate|11807|(364,)|var|float32
call_11803 = relay.TupleGetItem(func_10233_call(relay.reshape(const_11804.astype('uint32'), []), relay.reshape(var_11805.astype('int32'), [1056,]), relay.reshape(var_11806.astype('float64'), [7, 5]), relay.reshape(var_11807.astype('float32'), [364,]), ), 7)
call_11808 = relay.TupleGetItem(func_10239_call(relay.reshape(const_11804.astype('uint32'), []), relay.reshape(var_11805.astype('int32'), [1056,]), relay.reshape(var_11806.astype('float64'), [7, 5]), relay.reshape(var_11807.astype('float32'), [364,]), ), 7)
uop_11810 = relay.acos(call_11773.astype('float32')) # shape=(15, 3, 10)
uop_11812 = relay.acos(call_11774.astype('float32')) # shape=(15, 3, 10)
func_9177_call = mod.get_global_var('func_9177')
func_9180_call = mutated_mod.get_global_var('func_9180')
var_11815 = relay.var("var_11815", dtype = "float64", shape = (1820,))#candidate|11815|(1820,)|var|float64
call_11814 = func_9177_call(relay.reshape(var_11815.astype('float64'), [14, 13, 10]))
call_11816 = func_9177_call(relay.reshape(var_11815.astype('float64'), [14, 13, 10]))
output = relay.Tuple([call_11787,call_11789,call_11803,const_11804,var_11805,var_11806,var_11807,uop_11810,call_11814,var_11815,])
output2 = relay.Tuple([call_11788,call_11790,call_11808,const_11804,var_11805,var_11806,var_11807,uop_11812,call_11816,var_11815,])
func_11818 = relay.Function([var_11805,var_11806,var_11807,var_11815,], output)
mod['func_11818'] = func_11818
mod = relay.transform.InferType()(mod)
var_11819 = relay.var("var_11819", dtype = "int32", shape = (1056,))#candidate|11819|(1056,)|var|int32
var_11820 = relay.var("var_11820", dtype = "float64", shape = (35,))#candidate|11820|(35,)|var|float64
var_11821 = relay.var("var_11821", dtype = "float32", shape = (364,))#candidate|11821|(364,)|var|float32
var_11822 = relay.var("var_11822", dtype = "float64", shape = (1820,))#candidate|11822|(1820,)|var|float64
output = func_11818(var_11819,var_11820,var_11821,var_11822,)
func_11823 = relay.Function([var_11819,var_11820,var_11821,var_11822,], output)
mutated_mod['func_11823'] = func_11823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10988_call = mod.get_global_var('func_10988')
func_10989_call = mutated_mod.get_global_var('func_10989')
call_11943 = relay.TupleGetItem(func_10988_call(), 1)
call_11944 = relay.TupleGetItem(func_10989_call(), 1)
func_6130_call = mod.get_global_var('func_6130')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_11956 = func_6130_call()
call_11957 = func_6130_call()
output = relay.Tuple([call_11943,call_11956,])
output2 = relay.Tuple([call_11944,call_11957,])
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
func_11217_call = mod.get_global_var('func_11217')
func_11219_call = mutated_mod.get_global_var('func_11219')
call_12025 = func_11217_call()
call_12026 = func_11217_call()
output = call_12025
output2 = call_12026
func_12027 = relay.Function([], output)
mod['func_12027'] = func_12027
mod = relay.transform.InferType()(mod)
output = func_12027()
func_12028 = relay.Function([], output)
mutated_mod['func_12028'] = func_12028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5831_call = mod.get_global_var('func_5831')
func_5833_call = mutated_mod.get_global_var('func_5833')
call_12053 = relay.TupleGetItem(func_5831_call(), 0)
call_12054 = relay.TupleGetItem(func_5833_call(), 0)
func_10021_call = mod.get_global_var('func_10021')
func_10022_call = mutated_mod.get_global_var('func_10022')
call_12080 = relay.TupleGetItem(func_10021_call(), 0)
call_12081 = relay.TupleGetItem(func_10022_call(), 0)
func_11503_call = mod.get_global_var('func_11503')
func_11504_call = mutated_mod.get_global_var('func_11504')
call_12090 = relay.TupleGetItem(func_11503_call(), 0)
call_12091 = relay.TupleGetItem(func_11504_call(), 0)
func_10432_call = mod.get_global_var('func_10432')
func_10433_call = mutated_mod.get_global_var('func_10433')
call_12096 = relay.TupleGetItem(func_10432_call(), 0)
call_12097 = relay.TupleGetItem(func_10433_call(), 0)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_12099 = relay.TupleGetItem(func_7885_call(), 1)
call_12100 = relay.TupleGetItem(func_7886_call(), 1)
uop_12111 = relay.log10(call_12099.astype('float64')) # shape=(9, 6, 16)
uop_12113 = relay.log10(call_12100.astype('float64')) # shape=(9, 6, 16)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_12117 = relay.TupleGetItem(func_5900_call(), 0)
call_12118 = relay.TupleGetItem(func_5901_call(), 0)
uop_12131 = relay.erf(uop_12111.astype('float32')) # shape=(9, 6, 16)
uop_12133 = relay.erf(uop_12113.astype('float32')) # shape=(9, 6, 16)
func_8278_call = mod.get_global_var('func_8278')
func_8280_call = mutated_mod.get_global_var('func_8280')
call_12138 = func_8278_call()
call_12139 = func_8278_call()
output = relay.Tuple([call_12053,call_12080,call_12090,call_12096,call_12117,uop_12131,call_12138,])
output2 = relay.Tuple([call_12054,call_12081,call_12091,call_12097,call_12118,uop_12133,call_12139,])
func_12147 = relay.Function([], output)
mod['func_12147'] = func_12147
mod = relay.transform.InferType()(mod)
mutated_mod['func_12147'] = func_12147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12147_call = mutated_mod.get_global_var('func_12147')
call_12148 = func_12147_call()
output = call_12148
func_12149 = relay.Function([], output)
mutated_mod['func_12149'] = func_12149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8534_call = mutated_mod.get_global_var('func_8534')
call_12150 = relay.TupleGetItem(func_8532_call(), 0)
call_12151 = relay.TupleGetItem(func_8534_call(), 0)
output = call_12150
output2 = call_12151
func_12183 = relay.Function([], output)
mod['func_12183'] = func_12183
mod = relay.transform.InferType()(mod)
output = func_12183()
func_12184 = relay.Function([], output)
mutated_mod['func_12184'] = func_12184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6997_call = mod.get_global_var('func_6997')
func_6999_call = mutated_mod.get_global_var('func_6999')
call_12204 = func_6997_call()
call_12205 = func_6997_call()
output = relay.Tuple([call_12204,])
output2 = relay.Tuple([call_12205,])
func_12207 = relay.Function([], output)
mod['func_12207'] = func_12207
mod = relay.transform.InferType()(mod)
mutated_mod['func_12207'] = func_12207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12207_call = mutated_mod.get_global_var('func_12207')
call_12208 = func_12207_call()
output = call_12208
func_12209 = relay.Function([], output)
mutated_mod['func_12209'] = func_12209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7852_call = mod.get_global_var('func_7852')
func_7854_call = mutated_mod.get_global_var('func_7854')
call_12283 = relay.TupleGetItem(func_7852_call(), 0)
call_12284 = relay.TupleGetItem(func_7854_call(), 0)
func_4743_call = mod.get_global_var('func_4743')
func_4747_call = mutated_mod.get_global_var('func_4747')
const_12294 = relay.const(10, dtype = "uint32")#candidate|12294|()|const|uint32
var_12295 = relay.var("var_12295", dtype = "uint32", shape = (4,))#candidate|12295|(4,)|var|uint32
call_12293 = relay.TupleGetItem(func_4743_call(relay.reshape(const_12294.astype('uint32'), []), relay.reshape(var_12295.astype('uint32'), [4,]), ), 1)
call_12296 = relay.TupleGetItem(func_4747_call(relay.reshape(const_12294.astype('uint32'), []), relay.reshape(var_12295.astype('uint32'), [4,]), ), 1)
func_5006_call = mod.get_global_var('func_5006')
func_5011_call = mutated_mod.get_global_var('func_5011')
var_12313 = relay.var("var_12313", dtype = "uint64", shape = (1344, 1))#candidate|12313|(1344, 1)|var|uint64
call_12312 = relay.TupleGetItem(func_5006_call(relay.reshape(const_12294.astype('uint32'), []), relay.reshape(var_12295.astype('uint32'), [4,]), relay.reshape(var_12313.astype('uint64'), [1344, 1]), ), 5)
call_12314 = relay.TupleGetItem(func_5011_call(relay.reshape(const_12294.astype('uint32'), []), relay.reshape(var_12295.astype('uint32'), [4,]), relay.reshape(var_12313.astype('uint64'), [1344, 1]), ), 5)
uop_12327 = relay.tan(call_12312.astype('float32')) # shape=(1344, 1)
uop_12329 = relay.tan(call_12314.astype('float32')) # shape=(1344, 1)
uop_12335 = relay.atanh(uop_12327.astype('float64')) # shape=(1344, 1)
uop_12337 = relay.atanh(uop_12329.astype('float64')) # shape=(1344, 1)
var_12339 = relay.var("var_12339", dtype = "float64", shape = (1344, 8))#candidate|12339|(1344, 8)|var|float64
bop_12340 = relay.power(uop_12335.astype('float32'), var_12339.astype('float32')) # shape=(1344, 8)
bop_12343 = relay.power(uop_12337.astype('float32'), var_12339.astype('float32')) # shape=(1344, 8)
func_6130_call = mod.get_global_var('func_6130')
func_6132_call = mutated_mod.get_global_var('func_6132')
call_12350 = func_6130_call()
call_12351 = func_6130_call()
func_8272_call = mod.get_global_var('func_8272')
func_8273_call = mutated_mod.get_global_var('func_8273')
call_12354 = func_8272_call()
call_12355 = func_8272_call()
output = relay.Tuple([call_12283,call_12293,const_12294,var_12295,var_12313,bop_12340,call_12350,call_12354,])
output2 = relay.Tuple([call_12284,call_12296,const_12294,var_12295,var_12313,bop_12343,call_12351,call_12355,])
func_12359 = relay.Function([var_12295,var_12313,var_12339,], output)
mod['func_12359'] = func_12359
mod = relay.transform.InferType()(mod)
var_12360 = relay.var("var_12360", dtype = "uint32", shape = (4,))#candidate|12360|(4,)|var|uint32
var_12361 = relay.var("var_12361", dtype = "uint64", shape = (1344, 1))#candidate|12361|(1344, 1)|var|uint64
var_12362 = relay.var("var_12362", dtype = "float64", shape = (1344, 8))#candidate|12362|(1344, 8)|var|float64
output = func_12359(var_12360,var_12361,var_12362,)
func_12363 = relay.Function([var_12360,var_12361,var_12362,], output)
mutated_mod['func_12363'] = func_12363
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5146_call = mod.get_global_var('func_5146')
func_5148_call = mutated_mod.get_global_var('func_5148')
call_12418 = relay.TupleGetItem(func_5146_call(), 0)
call_12419 = relay.TupleGetItem(func_5148_call(), 0)
func_11217_call = mod.get_global_var('func_11217')
func_11219_call = mutated_mod.get_global_var('func_11219')
call_12420 = func_11217_call()
call_12421 = func_11217_call()
output = relay.Tuple([call_12418,call_12420,])
output2 = relay.Tuple([call_12419,call_12421,])
func_12443 = relay.Function([], output)
mod['func_12443'] = func_12443
mod = relay.transform.InferType()(mod)
output = func_12443()
func_12444 = relay.Function([], output)
mutated_mod['func_12444'] = func_12444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8272_call = mod.get_global_var('func_8272')
func_8273_call = mutated_mod.get_global_var('func_8273')
call_12448 = func_8272_call()
call_12449 = func_8272_call()
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
call_12483 = relay.TupleGetItem(func_11147_call(), 0)
call_12484 = relay.TupleGetItem(func_11149_call(), 0)
output = relay.Tuple([call_12448,call_12483,])
output2 = relay.Tuple([call_12449,call_12484,])
func_12493 = relay.Function([], output)
mod['func_12493'] = func_12493
mod = relay.transform.InferType()(mod)
mutated_mod['func_12493'] = func_12493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12493_call = mutated_mod.get_global_var('func_12493')
call_12494 = func_12493_call()
output = call_12494
func_12495 = relay.Function([], output)
mutated_mod['func_12495'] = func_12495
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12522 = relay.var("var_12522", dtype = "float64", shape = (14, 6, 4))#candidate|12522|(14, 6, 4)|var|float64
uop_12523 = relay.asin(var_12522.astype('float64')) # shape=(14, 6, 4)
output = uop_12523
output2 = uop_12523
func_12525 = relay.Function([var_12522,], output)
mod['func_12525'] = func_12525
mod = relay.transform.InferType()(mod)
mutated_mod['func_12525'] = func_12525
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12526 = relay.var("var_12526", dtype = "float64", shape = (14, 6, 4))#candidate|12526|(14, 6, 4)|var|float64
func_12525_call = mutated_mod.get_global_var('func_12525')
call_12527 = func_12525_call(var_12526)
output = call_12527
func_12528 = relay.Function([var_12526], output)
mutated_mod['func_12528'] = func_12528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10021_call = mod.get_global_var('func_10021')
func_10022_call = mutated_mod.get_global_var('func_10022')
call_12549 = relay.TupleGetItem(func_10021_call(), 1)
call_12550 = relay.TupleGetItem(func_10022_call(), 1)
func_12525_call = mod.get_global_var('func_12525')
func_12528_call = mutated_mod.get_global_var('func_12528')
var_12571 = relay.var("var_12571", dtype = "float64", shape = (336,))#candidate|12571|(336,)|var|float64
call_12570 = func_12525_call(relay.reshape(var_12571.astype('float64'), [14, 6, 4]))
call_12572 = func_12525_call(relay.reshape(var_12571.astype('float64'), [14, 6, 4]))
uop_12573 = relay.cosh(call_12570.astype('float32')) # shape=(14, 6, 4)
uop_12575 = relay.cosh(call_12572.astype('float32')) # shape=(14, 6, 4)
output = relay.Tuple([call_12549,var_12571,uop_12573,])
output2 = relay.Tuple([call_12550,var_12571,uop_12575,])
func_12585 = relay.Function([var_12571,], output)
mod['func_12585'] = func_12585
mod = relay.transform.InferType()(mod)
mutated_mod['func_12585'] = func_12585
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12586 = relay.var("var_12586", dtype = "float64", shape = (336,))#candidate|12586|(336,)|var|float64
func_12585_call = mutated_mod.get_global_var('func_12585')
call_12587 = func_12585_call(var_12586)
output = call_12587
func_12588 = relay.Function([var_12586], output)
mutated_mod['func_12588'] = func_12588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7381_call = mod.get_global_var('func_7381')
func_7383_call = mutated_mod.get_global_var('func_7383')
call_12628 = relay.TupleGetItem(func_7381_call(), 0)
call_12629 = relay.TupleGetItem(func_7383_call(), 0)
func_10336_call = mod.get_global_var('func_10336')
func_10338_call = mutated_mod.get_global_var('func_10338')
var_12644 = relay.var("var_12644", dtype = "uint64", shape = ())#candidate|12644|()|var|uint64
call_12643 = relay.TupleGetItem(func_10336_call(relay.reshape(var_12644.astype('uint64'), [])), 2)
call_12645 = relay.TupleGetItem(func_10338_call(relay.reshape(var_12644.astype('uint64'), [])), 2)
func_7242_call = mod.get_global_var('func_7242')
func_7243_call = mutated_mod.get_global_var('func_7243')
call_12649 = relay.TupleGetItem(func_7242_call(), 0)
call_12650 = relay.TupleGetItem(func_7243_call(), 0)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_12656 = relay.TupleGetItem(func_4849_call(), 0)
call_12657 = relay.TupleGetItem(func_4850_call(), 0)
func_9933_call = mod.get_global_var('func_9933')
func_9934_call = mutated_mod.get_global_var('func_9934')
call_12669 = func_9933_call()
call_12670 = func_9933_call()
func_7163_call = mod.get_global_var('func_7163')
func_7165_call = mutated_mod.get_global_var('func_7165')
call_12671 = func_7163_call()
call_12672 = func_7163_call()
output = relay.Tuple([call_12628,call_12643,var_12644,call_12649,call_12656,call_12669,call_12671,])
output2 = relay.Tuple([call_12629,call_12645,var_12644,call_12650,call_12657,call_12670,call_12672,])
func_12682 = relay.Function([var_12644,], output)
mod['func_12682'] = func_12682
mod = relay.transform.InferType()(mod)
mutated_mod['func_12682'] = func_12682
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12683 = relay.var("var_12683", dtype = "uint64", shape = ())#candidate|12683|()|var|uint64
func_12682_call = mutated_mod.get_global_var('func_12682')
call_12684 = func_12682_call(var_12683)
output = call_12684
func_12685 = relay.Function([var_12683], output)
mutated_mod['func_12685'] = func_12685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10988_call = mod.get_global_var('func_10988')
func_10989_call = mutated_mod.get_global_var('func_10989')
call_12714 = relay.TupleGetItem(func_10988_call(), 1)
call_12715 = relay.TupleGetItem(func_10989_call(), 1)
output = call_12714
output2 = call_12715
func_12719 = relay.Function([], output)
mod['func_12719'] = func_12719
mod = relay.transform.InferType()(mod)
output = func_12719()
func_12720 = relay.Function([], output)
mutated_mod['func_12720'] = func_12720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_12754 = relay.TupleGetItem(func_5203_call(), 2)
call_12755 = relay.TupleGetItem(func_5205_call(), 2)
func_4410_call = mod.get_global_var('func_4410')
func_4412_call = mutated_mod.get_global_var('func_4412')
call_12756 = relay.TupleGetItem(func_4410_call(), 0)
call_12757 = relay.TupleGetItem(func_4412_call(), 0)
output = relay.Tuple([call_12754,call_12756,])
output2 = relay.Tuple([call_12755,call_12757,])
func_12760 = relay.Function([], output)
mod['func_12760'] = func_12760
mod = relay.transform.InferType()(mod)
output = func_12760()
func_12761 = relay.Function([], output)
mutated_mod['func_12761'] = func_12761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9917_call = mod.get_global_var('func_9917')
func_9918_call = mutated_mod.get_global_var('func_9918')
call_12816 = func_9917_call()
call_12817 = func_9917_call()
func_11445_call = mod.get_global_var('func_11445')
func_11447_call = mutated_mod.get_global_var('func_11447')
call_12831 = relay.TupleGetItem(func_11445_call(), 0)
call_12832 = relay.TupleGetItem(func_11447_call(), 0)
output = relay.Tuple([call_12816,call_12831,])
output2 = relay.Tuple([call_12817,call_12832,])
func_12841 = relay.Function([], output)
mod['func_12841'] = func_12841
mod = relay.transform.InferType()(mod)
output = func_12841()
func_12842 = relay.Function([], output)
mutated_mod['func_12842'] = func_12842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8804_call = mod.get_global_var('func_8804')
func_8806_call = mutated_mod.get_global_var('func_8806')
call_12857 = relay.TupleGetItem(func_8804_call(), 4)
call_12858 = relay.TupleGetItem(func_8806_call(), 4)
output = call_12857
output2 = call_12858
func_12866 = relay.Function([], output)
mod['func_12866'] = func_12866
mod = relay.transform.InferType()(mod)
mutated_mod['func_12866'] = func_12866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12866_call = mutated_mod.get_global_var('func_12866')
call_12867 = func_12866_call()
output = call_12867
func_12868 = relay.Function([], output)
mutated_mod['func_12868'] = func_12868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_12901 = func_4460_call()
call_12902 = func_4460_call()
func_6997_call = mod.get_global_var('func_6997')
func_6999_call = mutated_mod.get_global_var('func_6999')
call_12908 = func_6997_call()
call_12909 = func_6997_call()
func_12841_call = mod.get_global_var('func_12841')
func_12842_call = mutated_mod.get_global_var('func_12842')
call_12947 = relay.TupleGetItem(func_12841_call(), 0)
call_12948 = relay.TupleGetItem(func_12842_call(), 0)
output = relay.Tuple([call_12901,call_12908,call_12947,])
output2 = relay.Tuple([call_12902,call_12909,call_12948,])
func_12969 = relay.Function([], output)
mod['func_12969'] = func_12969
mod = relay.transform.InferType()(mod)
output = func_12969()
func_12970 = relay.Function([], output)
mutated_mod['func_12970'] = func_12970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8804_call = mod.get_global_var('func_8804')
func_8806_call = mutated_mod.get_global_var('func_8806')
call_12993 = relay.TupleGetItem(func_8804_call(), 5)
call_12994 = relay.TupleGetItem(func_8806_call(), 5)
func_5567_call = mod.get_global_var('func_5567')
func_5569_call = mutated_mod.get_global_var('func_5569')
call_12996 = relay.TupleGetItem(func_5567_call(relay.reshape(call_12993.astype('int16'), [216, 4])), 0)
call_12997 = relay.TupleGetItem(func_5569_call(relay.reshape(call_12993.astype('int16'), [216, 4])), 0)
func_6631_call = mod.get_global_var('func_6631')
func_6634_call = mutated_mod.get_global_var('func_6634')
call_13001 = relay.TupleGetItem(func_6631_call(relay.reshape(call_12996.astype('float32'), [14, 5, 13])), 1)
call_13002 = relay.TupleGetItem(func_6634_call(relay.reshape(call_12996.astype('float32'), [14, 5, 13])), 1)
func_10094_call = mod.get_global_var('func_10094')
func_10096_call = mutated_mod.get_global_var('func_10096')
call_13005 = relay.TupleGetItem(func_10094_call(), 0)
call_13006 = relay.TupleGetItem(func_10096_call(), 0)
func_8804_call = mod.get_global_var('func_8804')
func_8806_call = mutated_mod.get_global_var('func_8806')
call_13007 = relay.TupleGetItem(func_8804_call(), 1)
call_13008 = relay.TupleGetItem(func_8806_call(), 1)
output = relay.Tuple([call_12993,call_12996,call_13001,call_13005,call_13007,])
output2 = relay.Tuple([call_12994,call_12997,call_13002,call_13006,call_13008,])
func_13014 = relay.Function([], output)
mod['func_13014'] = func_13014
mod = relay.transform.InferType()(mod)
mutated_mod['func_13014'] = func_13014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13014_call = mutated_mod.get_global_var('func_13014')
call_13015 = func_13014_call()
output = call_13015
func_13016 = relay.Function([], output)
mutated_mod['func_13016'] = func_13016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8489_call = mod.get_global_var('func_8489')
func_8491_call = mutated_mod.get_global_var('func_8491')
call_13109 = func_8489_call()
call_13110 = func_8489_call()
output = relay.Tuple([call_13109,])
output2 = relay.Tuple([call_13110,])
func_13113 = relay.Function([], output)
mod['func_13113'] = func_13113
mod = relay.transform.InferType()(mod)
output = func_13113()
func_13114 = relay.Function([], output)
mutated_mod['func_13114'] = func_13114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_13117 = relay.TupleGetItem(func_5900_call(), 0)
call_13118 = relay.TupleGetItem(func_5901_call(), 0)
func_5024_call = mod.get_global_var('func_5024')
func_5026_call = mutated_mod.get_global_var('func_5026')
call_13122 = func_5024_call()
call_13123 = func_5024_call()
func_9878_call = mod.get_global_var('func_9878')
func_9880_call = mutated_mod.get_global_var('func_9880')
call_13130 = relay.TupleGetItem(func_9878_call(), 0)
call_13131 = relay.TupleGetItem(func_9880_call(), 0)
output = relay.Tuple([call_13117,call_13122,call_13130,])
output2 = relay.Tuple([call_13118,call_13123,call_13131,])
func_13132 = relay.Function([], output)
mod['func_13132'] = func_13132
mod = relay.transform.InferType()(mod)
output = func_13132()
func_13133 = relay.Function([], output)
mutated_mod['func_13133'] = func_13133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7775_call = mod.get_global_var('func_7775')
func_7776_call = mutated_mod.get_global_var('func_7776')
call_13166 = relay.TupleGetItem(func_7775_call(), 0)
call_13167 = relay.TupleGetItem(func_7776_call(), 0)
func_6686_call = mod.get_global_var('func_6686')
func_6691_call = mutated_mod.get_global_var('func_6691')
const_13169 = relay.const([3,5,-7,-4,6,10,-4,1,4,-5,-2,7,-7,8,-4,-10,-7,6,-7,-6,-4,3,5,-9,-9,-9,1,2,7,-5,-1,9,10,-3,8,2,-8,-9,-10,-3,7,10,9,5,-4,-6,5,-2,-1,-4,6,10,-2,8,-9,2,4,5,-6,9,1,2,1,3,-10,-2,4,2,-2,1,-3,9,-5,-1,5,10,7,3,9,-1,-6,7,4,-7,10,-10,-1,10,-3,8,3,3,-3,8,-6,-10,2,2,7,-4,7,1,3,5,-4,-4,-2,-7,-5,6,-5,-2,6,-7,-3,-3,5,10,7,3,-8,-8,-6,-7,9,-2,4,3,10,-6,-1,5,2,3,1,-1,-5,-9,-2,-1,2,7,-1,-7,-2,-6,-9,-10,-6,-2,-1,4,-10,6,-1,-6,2,10,-6,2,9,3,-9,-1,-6,-2,6,2,10,9,-4,-8,-8,8,7,-4,-10,-6,-7,-3,-2,1,-10,-3,10,-4,6,-1,-10,10,10,4,10,6,7,-4,4,-6,-6,-5,-2,3,10,-4,-2,8,10,-10,1,10,7,6,9,8,-10,4,-1,-2,10,1,-10,-1,-10,3,-9,9,8,9,-9,5,-9,3,-5,-3,1,-6,-5,-3,8,-8,8,-4,5,6,-10,5,-7,1,3,8,10,-5,8,1,2,6,-7,8,4,5,-2,-5,-7,4,10,2,-3,6,4,9,5,8,6,3,10,7,-8,-5,-9,-5,-1,3,-5,-5,-6,-7,-4,4,-10,1,7,-6,-2,-8,-1,2,-3,6,-3,6,-7,-10,-7,2,-3,9,-3,-3,-7,-6,5,8,2,-5,-5,6,-6,-5,-3,2,10,-4,-6,7,-9,2,10,1,6,-9,-10,6,-1,1,-8,10,4,-2,-10,-6,2,2,-9,-6,-10,7,1,-8,-4,8,1,1,-1,-6,4,7,-1,7,-1,-5,7,-3,-5,3,-9,1,-7,5,-7,-9,4,-6,7,7,6,1,3,-4,-4,-8,-7,2,3,-2,-8,-3,8,-9,5,-3,9,-6,7,-1,-8,5,-7,-9,-6,-1,3,9,5,6,-6,-1,-2,-7,9,-3,8,10,7,-8,-2,7,4,9,-6,7,4,8,7,7,5,2,-8,-1,-6,7,-7,-5,2,8,1,-1,5,2,-5,7,1,-3,6,3,2,-9,-4,-10,10,-6,5,-5,9,2,8,-5,-3,-7,4,-10,-2,5,-3,4,-3,4,2,-10,-9,-6,-6,-6,-1,7,-5,-2,-5,-2,-2,-4,9,-4,-9,3,-7,-5,-9,-1,3,8,4,-4,-4,1,-5,10,-3,6,-9,10,-7,8,-5,10,8,6,5,4,8,-5,10,-8,2,-7,-4,-6,1,1,-6,3,-9,7,-1,-3,-4,-4,8,7,10,10,8,-9,3,-4,10,-2,-10,-5,7,2,8,6,-9,-5,-7,-5,2,-6,3,-3,-9,4,-3,-2,6,-4,1,-4,2,-1,6,-4,1,5,-1,-9,-7,-2,3,-1,-8,-7,4,9,-1,-3,-8,7,-6,-3,3,9,-6,-10,-3,-10,-7,-9,-6,-5,1,-4,-6,6,3,10,3,6,10,-8,9,5,-5,-7,5,8,3,-2,-2,2,10,-1,-3,4,-7,10,10,-1,10,-6,3,10,7,-4,2,6,2,-5,-6,-10,-1,8,6,8,1,-2,9,8,-1,7,-10,5,2,-7,-1,3,7,-5,3,10,9,-8,-1,-8,-1,-8,-10,5,5,10,2,9,-7,4,-2,-5,4,1,2,-10,4,5,10,-6,5,4,1,9,-10,9,-5,2,8,5,-1,-2,-2,9,-1,9,-2,3,6,3,-3,7,7,-7,3,4,6,10,-2,-10,-7,9,1,3,4,-3,-8,-6,10,-9,-5,8,6,-1,-1,3,9,-7,4,8,-8,4,1,-1,3,-5,-3,-4,-5,9,-8,-3,-4,9,-10,5,-6,-4,-9,10,-4,-2,10,-6,-1,-8,-7,5,-1,9,-9,-1,-3,4,9,4,8,10,10,-10,1,9,1,9,-6,7,-3,2,1,-6,1,4,5,-7,10,-5,9,10,8,6,-10,-1,9,-6,1,-3,-1,-4,-2,3,-10,4,-2,1,-6,6,-8,-6,10,9,6,-4,8,-5,-10,-2,-7,-10,-1,-1,-10,2,3,6,1,-5,-7,4,-8,8,5,8,6,-3,3,-5,-10,-10,6,6,-3,-4,1,-8,5,9,-5,4,-7,2,10,2,6,-4,-9,-10,1,-7,-2,-5,2,-10,3,10,-2,9,-2,3,2,-2,6,-7,8,3,-8,8,4,-7,-4,4,-3,-8,-3,-5,-6,8,-3,-3,7,-4,6,-5,1,-5,2,9,-4,10,-7,2,4,-9,5,9,-8,8,-4,-4,8,-10,-1,-4,7,2,-9,-9,-6,-1,10,6,-2,4,1,10,1,8,10,-9,-5,1,7,6,-8,-8,-6,6,1,5,2,-1,-7,5,10,4,-4,9,5,-9,-4,-1,3,2,9,-6,-3,4,-6,7,2,1,-6,-9,10,4,-7,8,-4,4,6,-6,8,10,6,10,-1,-4,-5,-8,5,1,-8,-1,-7,-8,6,-5,2,8,5,6,1,2,6,-1,5,2,10,6,8,-2,5,-9,-5,7,-7,5,-2,5,1,9,-9,9,-4,-9,-8,9,8,-2,-6,-2,-1,-10,6,-3,1,-2,2,-10,-8,-9,9,4,7,-2,-7,4,1,-3,9,-5,9,-3,-1,-7,3,7,-5,1,7,3,-10,-9,2,10,-9,4,-4,-7,1,4,-2,-7,-10,-7,4,8,-6,4,1,9,-9,-6,-1,8,8,7,-2,5,3,-6,9,-10,5,2,8,-5,-4,1,-5,9,-10,-3,1,4,-9,4,8,-4,-7,-6,8,3,-2,1,-5,1,7,10,2,-5,-6,-9,-10,-5,1,-4,-3,-3,3,-2,-4,-4,7,-10,-9,9,3,-8,-1,2,4,-1,4,4,9,6,1,4,-5,8,-9,-7,-5,5,-8,9,4,-1,-7,-4,4,-8,9,4,8,7,-1,10,-9,-3,4,1,4,-6,10,7,-1,9,-9,-5,-5,2,7,1,9,-5,7,-2,-1,-4,-2,2,-6,-5,-4,-9,5,6,-5,9,2,-10,-1,2,3,-2,-6,8,5,-4,6,-9,-7,2,-1,-10,7,4,2,-2,1,-10,8,7,-3,-4,6,-9,-8,9,-4,-4,8,-8,3,5,-4,1,3,5,10,-3,5,-1,5,-2,-8,-9,-6,7,7,-3,7,2,1,3,9,8,-8,-4,-1,-1,7,-7,6,-2,8,-3,1,-2,-3,4,1,-5,-2,-3,9,2,-3,-9,-5,-4,-10,5,-2,-4,3,6,-1,-2,-10,-6,10,-5,8,-4,6,-5,4,-8,10,1,1,5,8,4,4,-9,9,9,-9,-10,10,-3,-9,9,4,-1,7,8,-3,5,4,4,-7,9,-4,3,8,8,-7,-5,7,6,9,-1,-6,-4,10,4,-10,5,3,10,4,-7,5,1,-7,5,-3,-10,3,-1,-1,10,9,-7,-3,-4,-5,9,-4,-1,9,8,-4,-5,2,10,3,9,7,-4,3,1,-2,9,1,8,-7,6,-5,-10,8,-4,-2,-3,-9,3,-7,-1,5,7,-9,7,-3,9,3,7,-1,-2,-4,-6,-4,-4,-3,1,4,-1,-7,10,1,-8,-9,6,5,-5,-5,-3,-9,-9,3,-10,2,-1,2,-6,1,7,-10,9,3,8,6,6,-6,8,8,6,9,-6,-9,2,-10,-9,4,-8,4,6,5,5,-10,3,-9,8,8,-7,-10,-4,-1,-1,-3,-1,-6,6,10,5,2,-8,10,-9], dtype = "uint8")#candidate|13169|(1456,)|const|uint8
const_13170 = relay.const([5,6,-10,-4,-2,-1,-3,2,10,-1,-2,4,-6,-3,3,2,3,-7,6,5,6,3,-5,-1,6,2,8,5,10,-8,2,-9,9,10,-5,3,3,5,10,-4,9,-2,2,1,-7,-5,1,6,9,-5,-4,-10,-6,-6,-10,-3,-6,7,4,10,-9,2,8,-1,-7,3,-7,-8,-7,-1,5,-7,-1,-1,-10,-6,-5,-10,8,1,-8,-7,-7,-1,-9,3,-6,-5,3,-2,6,-4,8,-5,5,-2,-2,1,-3,-6,-5,-4,-7,6,6,7,-5,6,-6,10,7,-6,10,-8,10,-5,3,5,-10,-2,-10,10,-9,-1,-7,6,-2,5,-2,6,9,6,-1,-1,-4,1,3,1,8,-9,-10,3,9,-7,2,-2,7,2,1,-2,8,10,5,-3,1,9,9,7,-1,9,-10,-2,-1,6,8,8,1,7,-9,-8,4,-6,-1,-1,9,-4,10,-7,-2,6,3,8,-4,-10,9,7,-7,-8,-6,-1,-8,-4,-4,-3,6,-8,3,-4,3,2,-2,-5,2,7,2,-4,4,-1,1,-7,-1,-7,-1,3,-3,-3,-6,3,-4,7,-2,-4,-1,7,7,8,-6,-4,7,8,2,6,2,5,2,1,3,10,-2,-5,-10,-9,-1,3,10,-6,5,-10,3,-4,-9,9,-2,-5,10,3,4,-6,5,-1,-1,9,2,6,7,10,-4,-8,-2,1,5,-9,4,-6,-7,5,-7,-5,-4,-2,-10,6,3,-2,-1,6,7,-6,3,1,2,-7,8,8,4,4,-6,9,8,-4,-6,-4,-6,-1,4,-10,-8,7,-10,2,7,-7,8,-2,-9,3,7,-6,10,5,-1,-2,1,-7,-4,-2,-4,-4,6,9,4,-1,-1,-7,6,5,-4,-8,-6,-5,-3,1,-7,2,-5,-7,4,2,-4,-8,-9,-10,2,10,-3,8,2,-5,-8,-2,-9,2,6,-3,-2,-3,-6,6,10,-5,8,1,7,-1,-3,8,2,7,5,-10,-1,-10,7,4,-9,-10,-6,-1,7,8,4,3,-9,4,2,-2,9,9,-5,3,4,3,4,-3,-5,-2,6,-3,-8,8,4,-3,2,-9,5,-1,5,10,-9,2,-1,-10,-2,3,-3,1,3,-10,-8,-1,3,3,-7,9,6,-9,8,8,-6,1,4,-7,-8,3,8,-10,-10,-10,7,-5,3,-10,3,2,-8,9,4,2,-4,7,-3,-4,-1,-9,6,-9,-8,-1,-8,-2,-5,-10,-8,-3,9,6,-9,4,5,-6,7,-1,6,-6,6,-9,-9,-1,3,-9,4,-6,-6,-2,-2,-1,4,4,5,-2,-5,3,4,-3,8,1,9,-6,8,5,8,10,1,2,1,-8,-9,-4,-7,-1,-9,8,2,3,3,1,-8,-5,-5,5,-3,6,-6,-4,-5,7,-9,-4,-10,-10,-6,6,2,-1,8,-4,-10,2,1,8,-3,2,1,-1,-2,8,4,10,-7,4,6,8,-10,-4,8,-7,-9,1,4,3,-4,1,-6,5,-1,-1,-9,-5,-9,10,-8,-6,-5,-7,2,-2,-2,6,4,-1,10,-2,-1,6,3,-7,2,-10,-4,-5,-8,3,-1,-7,-10,-10,2,-9,-8,-3,2,5,-5,10,-3,-4,-5,-2,5,1,-2,6,-4,7,2,4,1,-8,8,8,7,4,-10,-8,10,2,2,-5,5,-8,-5,-10,6,5,-8,-5,6,6,-8,2,-4,9,4,-2,-8,-7,7,-9,7,-6,8,1,1,-9,2,8,-8,3,2,1,6,-3,5,-5,-8,7,-2,-10,-6,3,-2,3,9,10,-1,-1,10,1,8,10,-9,-1,-5,-4,-10,10,-2,-2,9,2,4,9,9,-3,-8,-10,10,-5,-2,8,10,6,1,2,-9,-3,10,-10,2,4,6,6,-9,3,-2,5,-10,-3,-8,-4,9,-1,9,-8,7,-10,9,-9,7,-8,-6,4,-6,1,-1,-1,2,1,-5,2,-10,5,8,-6,9,-7,-8,2,-7,-8,-10,1,2,1,1,-1,6,10,1,9,1,6,-7,5,-3,-2,-1,3,5,3,9,-6,-10,-9,2,1,-5,5,5,-4,3,1,1,9,2,-1,-8,6,-1,8,-2,-9,6,-9,-3,1,-2,-2,-8,6,-3,-1,-4,-8,1,-10,-7,-1,2,5,-4,-1,-1,-9,4,-1,2,9,-8,-3,-4,-3,2,3,-6,7,-7,8,1,-8,-3,-3,2,1,8,-10,-6,1,-9,-10,-5,4,-7,-9,-10,-5,-8,7,10,-2,3,9,7,7,-6,-2,6,-10,-10,3,-8,2,7,-9,-7,-5,5,10,-6,9,-4,1,-6,-4,4,6,-8,-1,8,-3,-9,5,-10,7,4,8,-8,9,-3,-2,-2,10,-7,-6,9,9,-6,3,1,-4,7,-2,-2,-10,-4,4,9,6,5,2,-1,-3,7,-3,-9,5,10,10,8,8,2,-10,6,-8,9,-6,-1,7,6,-6,8,10,9,-1,1,1,-1,-4,-8,-1,-2,-5,-5,-9,-2,-5,-6,-8,6,2,-9,1,-5,-1,9,9,-7,2,-7,-5,8,1,5,-9,-1,8,-5,3,6,-2,-4,-4,-5,6,-9,-5,1,9,9,8,-8,-1,-7,-2,8,8,4,6,-10,3,1,6,-6,-9,4,5,4,-6,2,-6,1,6,-7,7,5,7,-8,10,-10,8,-6,8,1,-5,-2,-5,4,-10,-4,-8,-5,-4,10,8,3,-5,-9,3,7,-2,6,3,1,-2,-8,-3,-5,-7,-3,4,1,6,-10,-9,-4,7,-10,-1,2,5,4,-5,7,4,9,5,-5,7,10,4,8,-6,-2,9,-2,7,4,-7,-6,-10,-6,4,-4,9,-8,7,-6,4,2,3,-2,2,-4,7,-7,-6,2,8,-2,9,2,4,3,-8,-3,-8,3,1,8,-9,6,2,3,3,7,-5,-2,-8,9,9,-9,7,9,-1,-9,-4,4,-3,5,4,10,10,-8,-4,-4,-1,1,5,7,7,-6,10,-6,-9,-7,-3,-10,-8,1,7,6,-6,-7,5,9,-9,4,7,2,-2,-6,-7,-8,-7,6,2,-2,-9,1,5,7,-7,5,10,9,-6,9,-3,8,-5,6,8,-8,-8,-2,-1,7,7,-3,9,1,6,1,-6,-1,-7,10,8,-2,-7,9,3,-9,8,-1,1,-4,-1,-10,4,-10,10,-6,-8,-5,5,6,-10,10,4,-6,-3,-3,5,-5,-7,-10,5,-7,6,-9,-6,1,-7,-7,-4,7,3,-4,-5,7,-6,-1,5,-5,10,4,-8,-5,5,5,4,7,-1,-6,-3,-8,-2,-1,7,-5,-9,-4,-3,-9,10,8,-5,-1,-9,3,-2,1,4,-8,-6,-9,-4,-2,-3,-5,-7,6,1,10,-8,2,-6,3,-4,10,-8,7,-3,8,1,8,10,10,5,1,-3,-3,-7,10,9,-1,10,-8,-8,10,2,7,-3,-1,-7,10,-7,-10,1,-4,-1,-9,7,-5,-6,4,2,-7,-8,-1,-5,4,6,-4,3,7,-7,4,-6,8,-3,-9,6], dtype = "uint64")#candidate|13170|(1344,)|const|uint64
var_13171 = relay.var("var_13171", dtype = "float64", shape = (140,))#candidate|13171|(140,)|var|float64
call_13168 = relay.TupleGetItem(func_6686_call(relay.reshape(const_13169.astype('uint8'), [8, 182]), relay.reshape(const_13170.astype('uint64'), [1344,]), relay.reshape(var_13171.astype('float64'), [140, 1]), ), 3)
call_13172 = relay.TupleGetItem(func_6691_call(relay.reshape(const_13169.astype('uint8'), [8, 182]), relay.reshape(const_13170.astype('uint64'), [1344,]), relay.reshape(var_13171.astype('float64'), [140, 1]), ), 3)
output = relay.Tuple([call_13166,call_13168,const_13169,const_13170,var_13171,])
output2 = relay.Tuple([call_13167,call_13172,const_13169,const_13170,var_13171,])
func_13213 = relay.Function([var_13171,], output)
mod['func_13213'] = func_13213
mod = relay.transform.InferType()(mod)
var_13214 = relay.var("var_13214", dtype = "float64", shape = (140,))#candidate|13214|(140,)|var|float64
output = func_13213(var_13214)
func_13215 = relay.Function([var_13214], output)
mutated_mod['func_13215'] = func_13215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12443_call = mod.get_global_var('func_12443')
func_12444_call = mutated_mod.get_global_var('func_12444')
call_13220 = relay.TupleGetItem(func_12443_call(), 1)
call_13221 = relay.TupleGetItem(func_12444_call(), 1)
output = relay.Tuple([call_13220,])
output2 = relay.Tuple([call_13221,])
func_13253 = relay.Function([], output)
mod['func_13253'] = func_13253
mod = relay.transform.InferType()(mod)
output = func_13253()
func_13254 = relay.Function([], output)
mutated_mod['func_13254'] = func_13254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7242_call = mod.get_global_var('func_7242')
func_7243_call = mutated_mod.get_global_var('func_7243')
call_13522 = relay.TupleGetItem(func_7242_call(), 0)
call_13523 = relay.TupleGetItem(func_7243_call(), 0)
output = call_13522
output2 = call_13523
func_13581 = relay.Function([], output)
mod['func_13581'] = func_13581
mod = relay.transform.InferType()(mod)
mutated_mod['func_13581'] = func_13581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13581_call = mutated_mod.get_global_var('func_13581')
call_13582 = func_13581_call()
output = call_13582
func_13583 = relay.Function([], output)
mutated_mod['func_13583'] = func_13583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_13610 = relay.TupleGetItem(func_5900_call(), 0)
call_13611 = relay.TupleGetItem(func_5901_call(), 0)
output = call_13610
output2 = call_13611
func_13614 = relay.Function([], output)
mod['func_13614'] = func_13614
mod = relay.transform.InferType()(mod)
mutated_mod['func_13614'] = func_13614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13614_call = mutated_mod.get_global_var('func_13614')
call_13615 = func_13614_call()
output = call_13615
func_13616 = relay.Function([], output)
mutated_mod['func_13616'] = func_13616
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11725_call = mod.get_global_var('func_11725')
func_11727_call = mutated_mod.get_global_var('func_11727')
call_13632 = func_11725_call()
call_13633 = func_11725_call()
func_5987_call = mod.get_global_var('func_5987')
func_5990_call = mutated_mod.get_global_var('func_5990')
var_13662 = relay.var("var_13662", dtype = "bool", shape = ())#candidate|13662|()|var|bool
call_13661 = relay.TupleGetItem(func_5987_call(relay.reshape(var_13662.astype('bool'), [])), 0)
call_13663 = relay.TupleGetItem(func_5990_call(relay.reshape(var_13662.astype('bool'), [])), 0)
func_12760_call = mod.get_global_var('func_12760')
func_12761_call = mutated_mod.get_global_var('func_12761')
call_13666 = relay.TupleGetItem(func_12760_call(), 1)
call_13667 = relay.TupleGetItem(func_12761_call(), 1)
output = relay.Tuple([call_13632,call_13661,var_13662,call_13666,])
output2 = relay.Tuple([call_13633,call_13663,var_13662,call_13667,])
func_13682 = relay.Function([var_13662,], output)
mod['func_13682'] = func_13682
mod = relay.transform.InferType()(mod)
var_13683 = relay.var("var_13683", dtype = "bool", shape = ())#candidate|13683|()|var|bool
output = func_13682(var_13683)
func_13684 = relay.Function([var_13683], output)
mutated_mod['func_13684'] = func_13684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9508_call = mod.get_global_var('func_9508')
func_9510_call = mutated_mod.get_global_var('func_9510')
call_13748 = relay.TupleGetItem(func_9508_call(), 0)
call_13749 = relay.TupleGetItem(func_9510_call(), 0)
func_5269_call = mod.get_global_var('func_5269')
func_5271_call = mutated_mod.get_global_var('func_5271')
call_13761 = relay.TupleGetItem(func_5269_call(), 0)
call_13762 = relay.TupleGetItem(func_5271_call(), 0)
output = relay.Tuple([call_13748,call_13761,])
output2 = relay.Tuple([call_13749,call_13762,])
func_13763 = relay.Function([], output)
mod['func_13763'] = func_13763
mod = relay.transform.InferType()(mod)
mutated_mod['func_13763'] = func_13763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13763_call = mutated_mod.get_global_var('func_13763')
call_13764 = func_13763_call()
output = call_13764
func_13765 = relay.Function([], output)
mutated_mod['func_13765'] = func_13765
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6956_call = mod.get_global_var('func_6956')
func_6957_call = mutated_mod.get_global_var('func_6957')
call_13785 = relay.TupleGetItem(func_6956_call(), 0)
call_13786 = relay.TupleGetItem(func_6957_call(), 0)
func_4564_call = mod.get_global_var('func_4564')
func_4566_call = mutated_mod.get_global_var('func_4566')
var_13803 = relay.var("var_13803", dtype = "bool", shape = ())#candidate|13803|()|var|bool
call_13802 = relay.TupleGetItem(func_4564_call(relay.reshape(var_13803.astype('bool'), [])), 4)
call_13804 = relay.TupleGetItem(func_4566_call(relay.reshape(var_13803.astype('bool'), [])), 4)
output = relay.Tuple([call_13785,call_13802,var_13803,])
output2 = relay.Tuple([call_13786,call_13804,var_13803,])
func_13814 = relay.Function([var_13803,], output)
mod['func_13814'] = func_13814
mod = relay.transform.InferType()(mod)
mutated_mod['func_13814'] = func_13814
mutated_mod = relay.transform.InferType()(mutated_mod)
var_13815 = relay.var("var_13815", dtype = "bool", shape = ())#candidate|13815|()|var|bool
func_13814_call = mutated_mod.get_global_var('func_13814')
call_13816 = func_13814_call(var_13815)
output = call_13816
func_13817 = relay.Function([var_13815], output)
mutated_mod['func_13817'] = func_13817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_13953 = relay.TupleGetItem(func_4849_call(), 0)
call_13954 = relay.TupleGetItem(func_4850_call(), 0)
output = relay.Tuple([call_13953,])
output2 = relay.Tuple([call_13954,])
func_13972 = relay.Function([], output)
mod['func_13972'] = func_13972
mod = relay.transform.InferType()(mod)
mutated_mod['func_13972'] = func_13972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13972_call = mutated_mod.get_global_var('func_13972')
call_13973 = func_13972_call()
output = call_13973
func_13974 = relay.Function([], output)
mutated_mod['func_13974'] = func_13974
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8278_call = mod.get_global_var('func_8278')
func_8280_call = mutated_mod.get_global_var('func_8280')
call_13987 = func_8278_call()
call_13988 = func_8278_call()
func_9118_call = mod.get_global_var('func_9118')
func_9121_call = mutated_mod.get_global_var('func_9121')
const_13995 = relay.const([9.542090,-0.560421,-4.622226,5.300325,5.087281,4.256438,-7.615443,9.548658,-7.231362,-0.670065,4.858263,-0.351272,-9.281883,0.589823,8.640974,6.477157,-2.582246,-4.222590,-2.463712,2.296882,6.529529,-7.033219,9.786598,-7.771754,3.405473,3.756310,0.702385,-4.430449,2.694942,-8.069398,1.114302,6.256874,6.513746,-4.938315,2.533816,1.755471,-1.913114,-7.729153,-7.009698,2.254093,-4.714535,-6.378070,-5.044535,7.699938,-9.868940,-0.920691,2.061195,0.956605,6.157025,-9.267376,-2.942172,7.759526,8.831335,-3.684881,7.176769,5.589905,-0.992394,1.918334,3.554198,0.498534,-1.948677,2.643779,1.994823,9.275283,-9.531687,-3.640756,7.807078,3.197521,5.997637,-4.213937,9.651166,-3.330000,-8.808978,-4.543421,-0.296130,9.740276,4.100860,3.622993,-6.518975,9.470566,-4.464220,2.567388,9.597949,1.091137,-5.972607,5.148521,2.541576,-9.437824,-7.373577,8.456062,-3.442249,2.474901,1.827302,-1.685739,6.534495,-4.803208,0.270725,-8.483918,-8.668069,-1.016221,8.703945,-0.181264,9.792362,-5.495883,9.477417,5.328069,0.288449,0.504810,2.161396,-2.331818,5.361114,-2.825487,-0.938870,-3.614091,-5.023919,6.552620,-3.890848,0.136459,-4.511175,1.469484,9.091616,6.598711,-6.010527,-4.898215,1.493525,-5.386127,1.767349,0.454134,0.252791,6.862805,-8.813700,-5.092793,-9.223193,5.659924,9.360649,3.914166,7.760880,8.396017,7.872965,6.769123,-3.624165,-5.254114,-5.275445,5.254405,8.137651,-1.924964,-5.369368,-0.837255,-4.346226,9.510757,8.314092,-5.844686,-3.239890,-9.460556,6.756050,-0.078349,1.905194,-0.855637,-3.197996,-5.687240,-9.211030,-2.544128,0.378186,8.777952,-2.091741,5.169585,2.334480,-7.703532,-6.271253,-0.890688,-9.228763,9.688364,2.780163,3.658163,-6.861253,8.844749,-6.316488,1.684704,-5.005143,1.728266,8.997504,-3.643283,1.768324,-1.921851,1.849978,9.087265,6.482027,-3.031256,-6.257052,7.082309,1.343613,0.124044,-7.710732,8.368189,-9.412637,1.380026,4.199677,-0.986625,-3.763624,-8.938932,0.913643,9.221904,4.917169,0.256489,7.556149,-4.057643,0.084504,3.382950,-3.804498,7.219058,4.339075,-3.722454,-8.212386,7.551681,-9.705437,4.341037,-0.083056,-5.354041,-5.477805,4.601967,-6.873550,-5.385599,-0.100044,3.963912,-5.532287,6.046799,6.923444,-2.266993,-9.007370,-3.944388,-6.360212,7.971610,-2.609368,-7.026311,7.854487,8.915212,7.237764,-6.814654,4.089301,-7.884443,-8.897056,8.661181,0.935369,2.476914,-3.605542,-2.726698,1.975788,3.467614,-7.441447,-4.648757,1.165587,6.723533,1.442307,-5.382757,-6.264953,-4.588494,-9.170127,-0.952370,-0.357641,-8.041144,-9.191418,5.310479,-3.874167,9.499066,-7.923640,-0.791642,5.603421,-9.794470,4.388443,2.153348,7.031912,-7.571365,-2.106532,9.288222,1.611291,1.565469,8.525841,0.859248,5.689694,-7.604600,9.012685,8.621216,-3.044789,7.017411,5.759999,7.139323,6.180358,-9.548620,8.782833,-3.198686,5.650567,-0.857977,-8.176146,-2.225933,-7.516065,5.070696,-3.726927,6.180315,-5.386903,-5.833346,0.897841,-3.311694,-2.666657,-6.932279,-6.733248,-7.907347,-8.095754,-6.744996,-4.587910,-0.548454,5.740664,-5.817463,8.568695,2.791954,8.767867,1.270663,8.753660,8.456984,-8.457799,4.302058,-7.520785,6.707438,-2.176664,9.494318,-2.113483,-8.610619,3.252961,5.011120,-5.536393,-5.097666,3.799968,-0.510418,1.286675,-2.097734,-8.616311,-5.780524,6.541904,0.776266,-1.501773,-1.758187,1.247418,-0.105039,-6.416862,6.734239,-1.990949,-2.947378,7.587507,0.430435,-3.650388,-6.358085,6.491170,7.734844,-6.229264,8.367990,6.160572,-1.269623,-8.231610,3.564973,-8.665280,0.983795,-1.530488,-9.470708,-0.250645,-7.232531], dtype = "float32")#candidate|13995|(364,)|const|float32
call_13994 = relay.TupleGetItem(func_9118_call(relay.reshape(const_13995.astype('float32'), [13, 2, 14]), relay.reshape(const_13995.astype('float32'), [13, 2, 14]), ), 0)
call_13996 = relay.TupleGetItem(func_9121_call(relay.reshape(const_13995.astype('float32'), [13, 2, 14]), relay.reshape(const_13995.astype('float32'), [13, 2, 14]), ), 0)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_14006 = relay.TupleGetItem(func_5900_call(), 0)
call_14007 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_13987,call_13994,const_13995,call_14006,])
output2 = relay.Tuple([call_13988,call_13996,const_13995,call_14007,])
func_14011 = relay.Function([], output)
mod['func_14011'] = func_14011
mod = relay.transform.InferType()(mod)
mutated_mod['func_14011'] = func_14011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14011_call = mutated_mod.get_global_var('func_14011')
call_14012 = func_14011_call()
output = call_14012
func_14013 = relay.Function([], output)
mutated_mod['func_14013'] = func_14013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8804_call = mod.get_global_var('func_8804')
func_8806_call = mutated_mod.get_global_var('func_8806')
call_14025 = relay.TupleGetItem(func_8804_call(), 4)
call_14026 = relay.TupleGetItem(func_8806_call(), 4)
func_12682_call = mod.get_global_var('func_12682')
func_12685_call = mutated_mod.get_global_var('func_12685')
const_14033 = relay.const(-1, dtype = "uint64")#candidate|14033|()|const|uint64
call_14032 = relay.TupleGetItem(func_12682_call(relay.reshape(const_14033.astype('uint64'), [])), 5)
call_14034 = relay.TupleGetItem(func_12685_call(relay.reshape(const_14033.astype('uint64'), [])), 5)
output = relay.Tuple([call_14025,call_14032,const_14033,])
output2 = relay.Tuple([call_14026,call_14034,const_14033,])
func_14048 = relay.Function([], output)
mod['func_14048'] = func_14048
mod = relay.transform.InferType()(mod)
output = func_14048()
func_14049 = relay.Function([], output)
mutated_mod['func_14049'] = func_14049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11503_call = mod.get_global_var('func_11503')
func_11504_call = mutated_mod.get_global_var('func_11504')
call_14057 = relay.TupleGetItem(func_11503_call(), 0)
call_14058 = relay.TupleGetItem(func_11504_call(), 0)
func_7049_call = mod.get_global_var('func_7049')
func_7050_call = mutated_mod.get_global_var('func_7050')
call_14077 = relay.TupleGetItem(func_7049_call(), 0)
call_14078 = relay.TupleGetItem(func_7050_call(), 0)
func_1811_call = mod.get_global_var('func_1811')
func_1815_call = mutated_mod.get_global_var('func_1815')
var_14090 = relay.var("var_14090", dtype = "int64", shape = (1815,))#candidate|14090|(1815,)|var|int64
call_14089 = func_1811_call(relay.reshape(var_14090.astype('int64'), [15, 11, 11]), relay.reshape(var_14090.astype('int64'), [15, 11, 11]), )
call_14091 = func_1811_call(relay.reshape(var_14090.astype('int64'), [15, 11, 11]), relay.reshape(var_14090.astype('int64'), [15, 11, 11]), )
func_11257_call = mod.get_global_var('func_11257')
func_11259_call = mutated_mod.get_global_var('func_11259')
var_14094 = relay.var("var_14094", dtype = "float64", shape = (450,))#candidate|14094|(450,)|var|float64
call_14093 = relay.TupleGetItem(func_11257_call(relay.reshape(var_14094.astype('float64'), [450,])), 0)
call_14095 = relay.TupleGetItem(func_11259_call(relay.reshape(var_14094.astype('float64'), [450,])), 0)
func_7238_call = mod.get_global_var('func_7238')
func_7239_call = mutated_mod.get_global_var('func_7239')
call_14103 = relay.TupleGetItem(func_7238_call(), 0)
call_14104 = relay.TupleGetItem(func_7239_call(), 0)
output = relay.Tuple([call_14057,call_14077,call_14089,var_14090,call_14093,var_14094,call_14103,])
output2 = relay.Tuple([call_14058,call_14078,call_14091,var_14090,call_14095,var_14094,call_14104,])
func_14126 = relay.Function([var_14090,var_14094,], output)
mod['func_14126'] = func_14126
mod = relay.transform.InferType()(mod)
mutated_mod['func_14126'] = func_14126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14126_call = mutated_mod.get_global_var('func_14126')
var_14128 = relay.var("var_14128", dtype = "int64", shape = (1815,))#candidate|14128|(1815,)|var|int64
var_14129 = relay.var("var_14129", dtype = "float64", shape = (450,))#candidate|14129|(450,)|var|float64
call_14127 = func_14126_call(var_14128,var_14129,)
output = call_14127
func_14130 = relay.Function([var_14128,var_14129,], output)
mutated_mod['func_14130'] = func_14130
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12841_call = mod.get_global_var('func_12841')
func_12842_call = mutated_mod.get_global_var('func_12842')
call_14157 = relay.TupleGetItem(func_12841_call(), 0)
call_14158 = relay.TupleGetItem(func_12842_call(), 0)
func_3981_call = mod.get_global_var('func_3981')
func_3984_call = mutated_mod.get_global_var('func_3984')
var_14165 = relay.var("var_14165", dtype = "float32", shape = (400,))#candidate|14165|(400,)|var|float32
call_14164 = relay.TupleGetItem(func_3981_call(relay.reshape(var_14165.astype('float32'), [5, 10, 8])), 0)
call_14166 = relay.TupleGetItem(func_3984_call(relay.reshape(var_14165.astype('float32'), [5, 10, 8])), 0)
output = relay.Tuple([call_14157,call_14164,var_14165,])
output2 = relay.Tuple([call_14158,call_14166,var_14165,])
func_14167 = relay.Function([var_14165,], output)
mod['func_14167'] = func_14167
mod = relay.transform.InferType()(mod)
mutated_mod['func_14167'] = func_14167
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14168 = relay.var("var_14168", dtype = "float32", shape = (400,))#candidate|14168|(400,)|var|float32
func_14167_call = mutated_mod.get_global_var('func_14167')
call_14169 = func_14167_call(var_14168)
output = call_14169
func_14170 = relay.Function([var_14168], output)
mutated_mod['func_14170'] = func_14170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13763_call = mod.get_global_var('func_13763')
func_13765_call = mutated_mod.get_global_var('func_13765')
call_14238 = relay.TupleGetItem(func_13763_call(), 1)
call_14239 = relay.TupleGetItem(func_13765_call(), 1)
output = call_14238
output2 = call_14239
func_14243 = relay.Function([], output)
mod['func_14243'] = func_14243
mod = relay.transform.InferType()(mod)
mutated_mod['func_14243'] = func_14243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14243_call = mutated_mod.get_global_var('func_14243')
call_14244 = func_14243_call()
output = call_14244
func_14245 = relay.Function([], output)
mutated_mod['func_14245'] = func_14245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6491_call = mod.get_global_var('func_6491')
func_6492_call = mutated_mod.get_global_var('func_6492')
call_14314 = func_6491_call()
call_14315 = func_6491_call()
func_10615_call = mod.get_global_var('func_10615')
func_10616_call = mutated_mod.get_global_var('func_10616')
call_14325 = relay.TupleGetItem(func_10615_call(), 1)
call_14326 = relay.TupleGetItem(func_10616_call(), 1)
output = relay.Tuple([call_14314,call_14325,])
output2 = relay.Tuple([call_14315,call_14326,])
func_14332 = relay.Function([], output)
mod['func_14332'] = func_14332
mod = relay.transform.InferType()(mod)
output = func_14332()
func_14333 = relay.Function([], output)
mutated_mod['func_14333'] = func_14333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14357 = relay.var("var_14357", dtype = "float32", shape = ())#candidate|14357|()|var|float32
var_14358 = relay.var("var_14358", dtype = "float32", shape = (5, 12, 15))#candidate|14358|(5, 12, 15)|var|float32
bop_14359 = relay.less(var_14357.astype('bool'), var_14358.astype('bool')) # shape=(5, 12, 15)
uop_14373 = relay.exp(var_14358.astype('float32')) # shape=(5, 12, 15)
output = relay.Tuple([bop_14359,uop_14373,])
output2 = relay.Tuple([bop_14359,uop_14373,])
func_14385 = relay.Function([var_14357,var_14358,], output)
mod['func_14385'] = func_14385
mod = relay.transform.InferType()(mod)
mutated_mod['func_14385'] = func_14385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14385_call = mutated_mod.get_global_var('func_14385')
var_14387 = relay.var("var_14387", dtype = "float32", shape = ())#candidate|14387|()|var|float32
var_14388 = relay.var("var_14388", dtype = "float32", shape = (5, 12, 15))#candidate|14388|(5, 12, 15)|var|float32
call_14386 = func_14385_call(var_14387,var_14388,)
output = call_14386
func_14389 = relay.Function([var_14387,var_14388,], output)
mutated_mod['func_14389'] = func_14389
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14423 = relay.const([[[2,-2,-10,-1,-9,-10,-4],[-4,4,-5,-10,-8,-5,8],[-4,9,-5,-3,5,9,-6],[1,-9,3,6,-4,5,5],[-9,-5,10,-8,-3,1,4],[-6,-2,-2,-1,4,3,4],[-10,-9,-4,1,-8,-10,-10],[1,-2,6,-5,4,-3,3],[-4,5,-6,2,-9,-5,-2],[8,-5,-7,7,10,2,-7],[-10,-3,7,-2,-2,-2,-7],[-10,1,4,8,-4,7,-6],[-8,5,3,-6,-6,3,3],[1,-4,1,-8,3,6,-2]],[[1,-1,-2,9,-4,8,-3],[6,-8,-8,-7,-10,-3,2],[10,2,3,-2,-10,2,8],[-2,3,-9,-6,-5,-3,9],[-8,7,4,-3,3,-3,8],[8,7,9,1,-1,4,-9],[1,-4,8,8,1,2,9],[-8,3,5,8,-10,-3,-6],[-6,-5,-5,-5,10,-9,-7],[6,6,-10,-4,1,-10,-10],[1,-9,5,4,-3,-4,-2],[-6,4,2,-10,3,9,5],[-4,-2,3,1,-7,9,-2],[5,-6,3,-4,3,9,-7]]], dtype = "int64")#candidate|14423|(2, 14, 7)|const|int64
var_14424 = relay.var("var_14424", dtype = "int64", shape = (2, 14, 7))#candidate|14424|(2, 14, 7)|var|int64
bop_14425 = relay.bitwise_and(const_14423.astype('int64'), relay.reshape(var_14424.astype('int64'), relay.shape_of(const_14423))) # shape=(2, 14, 7)
output = relay.Tuple([bop_14425,])
output2 = relay.Tuple([bop_14425,])
func_14428 = relay.Function([var_14424,], output)
mod['func_14428'] = func_14428
mod = relay.transform.InferType()(mod)
mutated_mod['func_14428'] = func_14428
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14429 = relay.var("var_14429", dtype = "int64", shape = (2, 14, 7))#candidate|14429|(2, 14, 7)|var|int64
func_14428_call = mutated_mod.get_global_var('func_14428')
call_14430 = func_14428_call(var_14429)
output = call_14430
func_14431 = relay.Function([var_14429], output)
mutated_mod['func_14431'] = func_14431
mutated_mod = relay.transform.InferType()(mutated_mod)
const_14439 = relay.const(9, dtype = "int8")#candidate|14439|()|const|int8
var_14440 = relay.var("var_14440", dtype = "int8", shape = (10, 1, 3))#candidate|14440|(10, 1, 3)|var|int8
bop_14441 = relay.maximum(const_14439.astype('int8'), var_14440.astype('int8')) # shape=(10, 1, 3)
func_4485_call = mod.get_global_var('func_4485')
func_4489_call = mutated_mod.get_global_var('func_4489')
var_14447 = relay.var("var_14447", dtype = "int64", shape = (7, 88))#candidate|14447|(7, 88)|var|int64
call_14446 = relay.TupleGetItem(func_4485_call(relay.reshape(var_14447.astype('int64'), [14, 4, 11]), relay.reshape(var_14447.astype('int64'), [14, 4, 11]), ), 0)
call_14448 = relay.TupleGetItem(func_4489_call(relay.reshape(var_14447.astype('int64'), [14, 4, 11]), relay.reshape(var_14447.astype('int64'), [14, 4, 11]), ), 0)
output = relay.Tuple([bop_14441,call_14446,var_14447,])
output2 = relay.Tuple([bop_14441,call_14448,var_14447,])
func_14450 = relay.Function([var_14440,var_14447,], output)
mod['func_14450'] = func_14450
mod = relay.transform.InferType()(mod)
var_14451 = relay.var("var_14451", dtype = "int8", shape = (10, 1, 3))#candidate|14451|(10, 1, 3)|var|int8
var_14452 = relay.var("var_14452", dtype = "int64", shape = (7, 88))#candidate|14452|(7, 88)|var|int64
output = func_14450(var_14451,var_14452,)
func_14453 = relay.Function([var_14451,var_14452,], output)
mutated_mod['func_14453'] = func_14453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_14468 = func_4460_call()
call_14469 = func_4460_call()
output = call_14468
output2 = call_14469
func_14478 = relay.Function([], output)
mod['func_14478'] = func_14478
mod = relay.transform.InferType()(mod)
output = func_14478()
func_14479 = relay.Function([], output)
mutated_mod['func_14479'] = func_14479
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14604 = relay.var("var_14604", dtype = "float64", shape = (1, 9, 15))#candidate|14604|(1, 9, 15)|var|float64
uop_14605 = relay.exp(var_14604.astype('float64')) # shape=(1, 9, 15)
func_10615_call = mod.get_global_var('func_10615')
func_10616_call = mutated_mod.get_global_var('func_10616')
call_14608 = relay.TupleGetItem(func_10615_call(), 1)
call_14609 = relay.TupleGetItem(func_10616_call(), 1)
bop_14610 = relay.bitwise_and(var_14604.astype('uint32'), relay.reshape(uop_14605.astype('uint32'), relay.shape_of(var_14604))) # shape=(1, 9, 15)
uop_14616 = relay.erf(bop_14610.astype('float32')) # shape=(1, 9, 15)
uop_14620 = relay.atan(uop_14616.astype('float32')) # shape=(1, 9, 15)
func_2431_call = mod.get_global_var('func_2431')
func_2434_call = mutated_mod.get_global_var('func_2434')
const_14627 = relay.const([[9.456413,5.764662,4.003536,-7.610316,-8.685098],[6.762983,-2.505063,-3.486373,-2.910240,-1.662059],[-7.080892,-4.000926,0.890955,-4.001069,-8.014942],[3.120103,-2.726265,-4.718578,-5.868059,7.891995],[-5.604145,5.179709,-0.322775,5.035171,0.100020],[9.087061,5.736463,-2.038770,5.955846,1.675626],[-9.276915,9.398739,1.311657,6.769744,-8.201339]], dtype = "float64")#candidate|14627|(7, 5)|const|float64
call_14626 = relay.TupleGetItem(func_2431_call(relay.reshape(const_14627.astype('float64'), [7, 5, 1])), 0)
call_14628 = relay.TupleGetItem(func_2434_call(relay.reshape(const_14627.astype('float64'), [7, 5, 1])), 0)
bop_14639 = relay.greater(bop_14610.astype('bool'), relay.reshape(uop_14620.astype('bool'), relay.shape_of(bop_14610))) # shape=(1, 9, 15)
bop_14648 = relay.floor_mod(bop_14639.astype('float64'), relay.reshape(var_14604.astype('float64'), relay.shape_of(bop_14639))) # shape=(1, 9, 15)
func_9118_call = mod.get_global_var('func_9118')
func_9121_call = mutated_mod.get_global_var('func_9121')
var_14664 = relay.var("var_14664", dtype = "float32", shape = (364,))#candidate|14664|(364,)|var|float32
call_14663 = relay.TupleGetItem(func_9118_call(relay.reshape(var_14664.astype('float32'), [13, 2, 14]), relay.reshape(var_14664.astype('float32'), [13, 2, 14]), ), 0)
call_14665 = relay.TupleGetItem(func_9121_call(relay.reshape(var_14664.astype('float32'), [13, 2, 14]), relay.reshape(var_14664.astype('float32'), [13, 2, 14]), ), 0)
output = relay.Tuple([call_14608,call_14626,const_14627,bop_14648,call_14663,var_14664,])
output2 = relay.Tuple([call_14609,call_14628,const_14627,bop_14648,call_14665,var_14664,])
func_14672 = relay.Function([var_14604,var_14664,], output)
mod['func_14672'] = func_14672
mod = relay.transform.InferType()(mod)
mutated_mod['func_14672'] = func_14672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14672_call = mutated_mod.get_global_var('func_14672')
var_14674 = relay.var("var_14674", dtype = "float64", shape = (1, 9, 15))#candidate|14674|(1, 9, 15)|var|float64
var_14675 = relay.var("var_14675", dtype = "float32", shape = (364,))#candidate|14675|(364,)|var|float32
call_14673 = func_14672_call(var_14674,var_14675,)
output = call_14673
func_14676 = relay.Function([var_14674,var_14675,], output)
mutated_mod['func_14676'] = func_14676
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14680 = relay.var("var_14680", dtype = "int64", shape = (6, 5, 16))#candidate|14680|(6, 5, 16)|var|int64
var_14681 = relay.var("var_14681", dtype = "int64", shape = (6, 5, 16))#candidate|14681|(6, 5, 16)|var|int64
bop_14682 = relay.less_equal(var_14680.astype('bool'), relay.reshape(var_14681.astype('bool'), relay.shape_of(var_14680))) # shape=(6, 5, 16)
uop_14695 = relay.log2(var_14681.astype('float32')) # shape=(6, 5, 16)
func_10233_call = mod.get_global_var('func_10233')
func_10239_call = mutated_mod.get_global_var('func_10239')
var_14700 = relay.var("var_14700", dtype = "uint32", shape = ())#candidate|14700|()|var|uint32
var_14701 = relay.var("var_14701", dtype = "int32", shape = (1056,))#candidate|14701|(1056,)|var|int32
const_14702 = relay.const([-6.019710,-2.435696,-5.648752,-4.258731,3.278485,6.462661,3.469542,5.887840,-6.629504,6.269374,-8.320583,3.821488,-3.276104,-2.968172,2.282570,-5.367656,-3.300722,3.465899,-7.533379,-2.588408,-2.001308,8.889484,-2.352512,0.957540,-7.952366,-6.201926,8.006095,9.113340,-3.053540,9.037569,3.479978,-0.433401,-0.771310,-2.348124,9.117565], dtype = "float64")#candidate|14702|(35,)|const|float64
var_14703 = relay.var("var_14703", dtype = "float32", shape = (182, 2))#candidate|14703|(182, 2)|var|float32
call_14699 = relay.TupleGetItem(func_10233_call(relay.reshape(var_14700.astype('uint32'), []), relay.reshape(var_14701.astype('int32'), [1056,]), relay.reshape(const_14702.astype('float64'), [7, 5]), relay.reshape(var_14703.astype('float32'), [364,]), ), 10)
call_14704 = relay.TupleGetItem(func_10239_call(relay.reshape(var_14700.astype('uint32'), []), relay.reshape(var_14701.astype('int32'), [1056,]), relay.reshape(const_14702.astype('float64'), [7, 5]), relay.reshape(var_14703.astype('float32'), [364,]), ), 10)
func_11986_call = mod.get_global_var('func_11986')
func_11988_call = mutated_mod.get_global_var('func_11988')
call_14705 = relay.TupleGetItem(func_11986_call(), 0)
call_14706 = relay.TupleGetItem(func_11988_call(), 0)
func_11818_call = mod.get_global_var('func_11818')
func_11823_call = mutated_mod.get_global_var('func_11823')
var_14709 = relay.var("var_14709", dtype = "float64", shape = (910, 2))#candidate|14709|(910, 2)|var|float64
call_14708 = relay.TupleGetItem(func_11818_call(relay.reshape(var_14701.astype('int32'), [1056,]), relay.reshape(const_14702.astype('float64'), [35,]), relay.reshape(var_14703.astype('float32'), [364,]), relay.reshape(var_14709.astype('float64'), [1820,]), ), 2)
call_14710 = relay.TupleGetItem(func_11823_call(relay.reshape(var_14701.astype('int32'), [1056,]), relay.reshape(const_14702.astype('float64'), [35,]), relay.reshape(var_14703.astype('float32'), [364,]), relay.reshape(var_14709.astype('float64'), [1820,]), ), 2)
func_4666_call = mod.get_global_var('func_4666')
func_4668_call = mutated_mod.get_global_var('func_4668')
call_14714 = func_4666_call()
call_14715 = func_4666_call()
bop_14749 = relay.minimum(var_14709.astype('uint8'), var_14700.astype('uint8')) # shape=(910, 2)
output = relay.Tuple([bop_14682,uop_14695,call_14699,var_14701,const_14702,var_14703,call_14705,call_14708,call_14714,bop_14749,])
output2 = relay.Tuple([bop_14682,uop_14695,call_14704,var_14701,const_14702,var_14703,call_14706,call_14710,call_14715,bop_14749,])
func_14769 = relay.Function([var_14680,var_14681,var_14700,var_14701,var_14703,var_14709,], output)
mod['func_14769'] = func_14769
mod = relay.transform.InferType()(mod)
var_14770 = relay.var("var_14770", dtype = "int64", shape = (6, 5, 16))#candidate|14770|(6, 5, 16)|var|int64
var_14771 = relay.var("var_14771", dtype = "int64", shape = (6, 5, 16))#candidate|14771|(6, 5, 16)|var|int64
var_14772 = relay.var("var_14772", dtype = "uint32", shape = ())#candidate|14772|()|var|uint32
var_14773 = relay.var("var_14773", dtype = "int32", shape = (1056,))#candidate|14773|(1056,)|var|int32
var_14774 = relay.var("var_14774", dtype = "float32", shape = (182, 2))#candidate|14774|(182, 2)|var|float32
var_14775 = relay.var("var_14775", dtype = "float64", shape = (910, 2))#candidate|14775|(910, 2)|var|float64
output = func_14769(var_14770,var_14771,var_14772,var_14773,var_14774,var_14775,)
func_14776 = relay.Function([var_14770,var_14771,var_14772,var_14773,var_14774,var_14775,], output)
mutated_mod['func_14776'] = func_14776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_14802 = func_4460_call()
call_14803 = func_4460_call()
func_11725_call = mod.get_global_var('func_11725')
func_11727_call = mutated_mod.get_global_var('func_11727')
call_14821 = func_11725_call()
call_14822 = func_11725_call()
output = relay.Tuple([call_14802,call_14821,])
output2 = relay.Tuple([call_14803,call_14822,])
func_14836 = relay.Function([], output)
mod['func_14836'] = func_14836
mod = relay.transform.InferType()(mod)
mutated_mod['func_14836'] = func_14836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14836_call = mutated_mod.get_global_var('func_14836')
call_14837 = func_14836_call()
output = call_14837
func_14838 = relay.Function([], output)
mutated_mod['func_14838'] = func_14838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14876 = relay.var("var_14876", dtype = "uint64", shape = ())#candidate|14876|()|var|uint64
const_14877 = relay.const([[[2,6,-4,-6,-1,-7],[-5,5,1,6,-6,9],[4,4,1,-9,-5,4],[1,-10,-1,3,2,-9]],[[1,-8,2,6,-7,2],[-2,1,-6,-9,-7,9],[10,5,9,-4,9,-7],[1,-7,-6,4,-9,-5]],[[2,-10,-7,-6,-1,10],[4,10,7,-4,-3,-7],[-1,-8,8,3,-9,8],[4,-6,4,6,-1,-3]],[[6,-7,10,1,-4,10],[-2,1,-8,1,2,10],[3,-8,-2,1,8,-10],[-1,-10,10,9,4,5]],[[-9,-7,-4,-1,-3,-9],[7,5,-9,4,8,7],[3,-9,-5,1,3,-9],[5,1,-6,-2,-2,10]],[[6,3,9,1,7,-1],[8,-8,-1,5,-6,3],[7,-9,-4,2,5,3],[9,-6,-6,1,-8,-3]],[[8,5,4,-8,-3,2],[5,7,-1,-4,2,7],[4,2,-8,2,-2,-10],[5,7,-8,-7,-5,3]],[[-3,-8,-6,5,-4,-3],[-3,-8,2,-1,-9,-4],[9,10,-6,-2,1,-5],[5,-4,-8,-1,1,-4]],[[-9,-9,5,-3,-5,-8],[7,9,10,-2,4,5],[-2,3,-6,-6,3,-3],[-9,3,-9,-6,-3,-4]],[[-10,9,2,-6,-8,8],[7,1,9,8,-10,1],[-4,-8,3,9,6,-7],[-9,3,-3,5,6,8]]], dtype = "uint64")#candidate|14877|(10, 4, 6)|const|uint64
bop_14878 = relay.logical_xor(var_14876.astype('uint64'), const_14877.astype('uint64')) # shape=(10, 4, 6)
output = bop_14878
output2 = bop_14878
func_14881 = relay.Function([var_14876,], output)
mod['func_14881'] = func_14881
mod = relay.transform.InferType()(mod)
mutated_mod['func_14881'] = func_14881
mutated_mod = relay.transform.InferType()(mutated_mod)
var_14882 = relay.var("var_14882", dtype = "uint64", shape = ())#candidate|14882|()|var|uint64
func_14881_call = mutated_mod.get_global_var('func_14881')
call_14883 = func_14881_call(var_14882)
output = call_14883
func_14884 = relay.Function([var_14882], output)
mutated_mod['func_14884'] = func_14884
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_14886 = relay.TupleGetItem(func_7885_call(), 0)
call_14887 = relay.TupleGetItem(func_7886_call(), 0)
output = call_14886
output2 = call_14887
func_14901 = relay.Function([], output)
mod['func_14901'] = func_14901
mod = relay.transform.InferType()(mod)
mutated_mod['func_14901'] = func_14901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14901_call = mutated_mod.get_global_var('func_14901')
call_14902 = func_14901_call()
output = call_14902
func_14903 = relay.Function([], output)
mutated_mod['func_14903'] = func_14903
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14836_call = mod.get_global_var('func_14836')
func_14838_call = mutated_mod.get_global_var('func_14838')
call_14972 = relay.TupleGetItem(func_14836_call(), 0)
call_14973 = relay.TupleGetItem(func_14838_call(), 0)
func_1748_call = mod.get_global_var('func_1748')
func_1753_call = mutated_mod.get_global_var('func_1753')
const_14976 = relay.const([[-2.863705],[8.127516],[4.368907],[3.736097],[-5.149044],[5.551306],[9.429567],[4.545869],[5.847258],[5.267494],[5.643583],[-6.792957],[-6.132420],[8.200502],[-7.487030],[-5.684952],[-3.572616],[-8.394057],[0.010173],[7.933360],[-2.282461],[-8.013677],[-4.982161],[-0.103840],[8.022510],[-2.848326],[9.411123],[8.324026],[5.655086],[-8.533154],[-0.563671],[-4.941572],[-6.637282],[-9.802645],[3.091121],[-3.333823],[-2.683791],[8.905149],[-4.723157],[-8.474403],[-4.862205],[-2.690560],[0.475812],[1.754206],[6.284873],[6.432445],[-2.331683],[-8.691904],[-9.169409],[9.568163],[-0.890474],[4.334219],[-3.495589],[-8.012353],[-7.020060],[-4.966609],[8.744567],[-4.328755],[5.146931],[7.226775],[-8.295212],[-1.633709],[5.009253],[5.651366],[6.629557],[2.373032],[-6.229922],[2.966722],[1.294329],[-9.414042],[-1.923748],[-5.258735],[2.810607],[9.600938],[5.638582],[4.841579],[4.680265],[-3.774936],[-2.603397],[-0.825662],[-6.076525],[-7.591180],[-2.888518],[-8.787313],[2.413331],[-3.203139],[6.273597],[4.392648],[0.238241],[3.629355],[-5.498755],[-1.618644],[-2.374829],[-2.318366],[3.323482],[5.536026],[-8.525688],[-7.134567],[3.082718],[-9.945778],[9.427054],[-5.348583],[-9.692134],[-8.978091],[-9.560614],[-3.537189],[-1.757128],[-4.478011],[0.959388],[-2.614035],[0.441595],[9.374706],[0.260291],[9.825785],[-9.456135],[0.976657],[-2.564566],[-2.346508],[1.739111],[-8.947386],[4.193206],[-1.082197],[-6.269356],[-5.426427],[7.979017],[-5.639849],[-8.372558],[-4.117728],[2.829849],[-6.136362],[-1.114246],[-1.161168],[-1.690347],[2.130454],[4.935017],[8.735310],[-6.372929],[-6.228684],[6.386722],[-2.147376],[1.397571],[3.413086],[-9.493776],[8.846423],[0.507327],[3.882653],[6.951544],[-9.668710],[6.787960],[-8.054360],[-2.383874],[0.827295],[0.836789],[9.283483],[-6.924663],[-3.498926],[-2.712678],[-6.353449],[3.779681],[-1.750747],[0.473895],[-1.287613],[4.847674],[-8.744435],[-1.126868],[8.351716],[4.449484],[5.439034],[3.924602],[4.945411],[7.604225],[0.853577],[0.576700],[-3.000164],[-0.823844],[-6.957795],[8.133471],[-0.067419],[8.710482],[2.139859],[0.777989],[-6.991191],[2.250115],[-6.602467],[-5.705199],[-9.007662],[2.460048],[8.451906],[1.421777],[0.312769],[1.485484],[-5.356658],[2.489906],[4.727618],[6.954365],[-0.877903],[-9.565086],[1.739463],[0.913642],[-8.569577],[9.724356],[8.002912],[-2.885674],[-5.149856],[-4.577616],[7.916837],[5.371736],[-8.018038],[7.539160],[5.624314],[-1.982499],[2.894397],[5.521351],[-1.565686],[-5.819106],[-6.461379],[-8.534219],[-1.507556],[7.526055],[-2.531653],[8.331356],[3.773973],[3.517923],[5.701249],[4.008349],[-5.223657],[-3.233955],[-6.854481],[-1.027178],[-3.246191],[1.091179],[4.874382],[-8.832822],[1.612961],[-1.299466],[-9.389704],[1.481275],[-8.197569],[3.101283],[2.349668],[-9.180811],[5.609797],[-5.223256],[-3.546146],[-1.846916],[3.179979],[-2.294042],[7.882592],[9.450521],[-0.149064],[9.825157],[5.161747],[-8.793281],[3.745183],[4.702402],[-0.550850],[-8.817165],[-8.538142],[-0.612572],[-5.845169],[-6.956020],[-0.820599],[-5.165341],[0.674977],[-3.601801],[0.356114],[-2.204616],[2.609428],[-9.917184],[0.167388],[9.976616],[2.193310],[4.897845],[-3.898882],[4.246444],[-6.846398],[4.981050],[-8.812035],[1.872278],[4.893607],[9.333663],[7.829808],[1.206974],[-5.458042],[7.537655],[7.943169],[6.726164],[0.571958],[-6.279828],[-5.329390],[-1.831290],[6.417470],[-7.447675],[7.755413],[-5.552985],[1.731076],[0.114784],[7.390860],[4.905576],[-9.064837],[8.581016],[-7.478978],[-7.097148],[9.030364],[9.190715],[-9.129840],[8.517344],[8.784151],[6.524923],[2.760797],[5.924170],[4.388206],[0.371688],[6.725425],[-1.668438],[7.866930],[7.729757],[5.364095],[2.061013],[6.368561],[-8.703504],[-1.098590],[9.520378],[8.756992],[-6.094165],[-1.392017],[-8.633300],[-3.981587],[4.707525],[-7.088936],[4.943280],[6.662684],[8.506333],[1.305099],[-6.446600],[-1.465249],[-6.976129],[-3.474002],[-5.971751],[3.903560],[-8.769658],[1.699663],[7.679758],[-5.959038],[5.662664],[3.674174],[-8.961831],[-1.191792],[0.243321],[9.633242],[-0.162428],[-6.639775],[-7.337580],[-2.821357],[0.453180],[-5.546350],[-7.837518],[-5.854297],[0.961933],[-2.093307],[0.596471],[-4.950240],[-7.647736],[-1.944672],[-1.613738],[9.315346],[7.386752],[7.558144],[-1.901488],[-1.807548],[1.078682],[3.366923],[-4.418831],[-3.834100],[-8.849618],[3.817083],[-0.464663],[-5.718648],[-4.599116],[-0.347581],[-2.189070],[3.840748],[2.862886],[1.624519],[-6.394922],[6.385765],[-1.420796],[0.433237],[-9.343713],[7.876190],[-2.443051],[7.832447],[-4.599342],[-2.799031],[-9.333834],[1.903456],[-0.127526],[-1.179330],[5.268495],[-3.296506],[7.731417],[-2.300930],[-0.172690],[4.385733],[8.607620],[-6.257053],[8.063357],[-7.757711],[0.777363],[-2.965405],[9.380288],[-3.629118],[-4.086519],[7.954159],[-3.739727],[1.045284],[-1.392151],[-7.791648],[-0.607998],[6.766575],[-5.648336],[0.499074],[1.668737],[5.252971],[-6.563872],[-7.370660],[1.483569],[-1.084267],[5.633467],[3.985237],[0.379086],[-4.013243],[-6.260304],[-4.594726],[-2.813999],[-7.890684],[6.639765],[-1.495330],[3.281517],[8.998393],[7.919463],[4.847830],[-5.416609],[-0.880662],[-8.944188],[-3.592807],[-3.147141],[6.564614],[5.705580],[7.518891],[8.676145],[-5.727816],[-5.388988],[-4.131408],[-0.562524],[5.544592],[6.703188],[-0.587393],[-2.972008],[-1.360365],[-1.733660],[-7.908927],[0.202045],[-6.970898],[-6.283064],[-7.301404],[6.595608],[-3.337503],[3.482496],[-7.542687],[1.737770],[3.791557],[-8.602053],[-2.642843],[-4.926116],[8.623877],[3.366545],[9.036021],[6.722595],[1.274439],[-1.409889],[-1.360015],[-2.463495],[1.562839],[8.406321],[0.524836],[9.410809],[6.005639],[-0.911857],[3.406264],[-3.251134],[-5.689450],[-7.136103],[-4.940241],[6.400176],[1.360212],[4.900307],[9.019113],[3.195166],[6.459352],[-8.267469],[6.406470],[6.488876],[-1.354894],[-1.276629],[-5.805313],[-0.326585],[3.508157],[4.951005],[7.470875],[9.951432],[-4.591499],[-6.092844],[4.803361],[-2.070336],[-8.990391],[9.556559],[-3.406450],[-8.643273],[0.430209],[-8.278614],[-6.631225],[-5.773202],[-6.941811],[0.770493],[-8.592145],[-6.164301],[-1.488140],[-4.637517],[-3.948689],[-7.248315],[-3.197274],[-3.185457],[3.953069],[4.026460],[-5.321600],[-3.656212],[-8.296458],[-3.646792],[-5.064124],[-2.791551],[-9.370450],[0.567155],[8.947324],[-7.868361],[-3.600425],[-4.174809],[3.847241],[-1.273523],[-1.633025],[6.926391],[8.763626],[9.764571],[-9.756328],[-1.094029],[3.995331],[7.847328],[-0.544689],[-3.821030],[-2.055016],[4.100390],[-3.419307],[0.372288],[5.079287],[-6.242949],[3.396457],[-9.900535],[6.899156],[5.415221],[8.014254],[7.409043],[-4.600415],[-7.113381],[6.608769],[6.621955],[-6.369225],[3.612384],[-9.747134],[-6.087893],[-1.098956],[7.977442],[-3.692389],[-2.131303],[5.673875],[3.571182],[-3.407157],[-9.368786],[1.124626],[5.720078],[7.205792],[-2.033314],[4.995003],[-5.732356],[7.725551],[0.253185],[5.806928],[4.545247],[-0.165433],[-1.480229],[4.776338],[-7.043805],[-5.006962],[6.312583],[-4.610812],[-1.728092],[6.723614],[6.714242],[-0.115530],[-9.366750],[-2.620350],[6.032563],[3.813896],[3.092095],[5.427066],[5.840933],[9.671997],[-4.698691],[-6.925205],[0.711367],[-6.519916],[5.151871],[-5.147115],[-6.207417],[-6.085708],[-7.154047],[1.773957],[0.781363],[5.713663],[-7.394367],[-5.635606],[7.449657],[-2.666124],[4.860210],[5.276977],[8.823806],[-9.137078],[1.516150],[7.162311],[-5.143345],[3.965265],[-4.314124],[-9.166039],[9.436154],[-7.648231],[-6.677816],[4.407405],[-4.848367],[9.142859],[9.592107],[-5.117455],[-6.116301],[3.023342],[7.714634],[-8.513528],[-2.840175],[4.268555],[-5.005712],[-9.208225],[3.436123],[7.430677],[9.050975],[1.550732],[-7.419038],[6.999549],[-1.875467],[-0.450245],[9.415075],[-7.986239],[-7.606244],[-4.397186],[-1.441983],[4.264554],[8.278548],[-9.315959],[-5.136510],[0.633889],[0.404169],[4.725201],[6.337400],[8.478929],[-3.278910],[7.280098],[9.752476],[9.158682],[-7.480013],[-0.841029],[5.756822],[2.618728],[-3.748445],[8.119040],[1.939272],[-0.601230],[6.781145],[5.270174],[2.651754],[-5.841443],[-5.652178],[9.458270],[-8.728455],[-8.574878],[-7.023224],[7.006576],[-9.379406],[-3.520451],[4.672189],[-7.312806],[-1.291856],[6.584582],[-6.444072],[3.160938],[6.716946],[-6.741723],[9.749088],[7.954141],[-0.951670],[-1.657130],[-2.930690],[-8.898923],[-2.274136],[9.796218],[-4.639836],[-2.052715],[2.231451],[-4.271413],[-5.288052],[7.026557],[-2.740696],[-9.805837],[1.063985],[4.662509],[1.978414],[-2.275719],[5.332260],[-1.276655],[6.301833],[5.923535],[4.184853],[4.089351],[2.163106],[2.020121],[9.119473],[2.383366],[-4.369516],[5.015708],[6.615785],[3.464688],[-7.110333],[0.799109],[-1.416716],[2.447612],[6.100964],[3.560149],[-8.687982],[7.213641],[-6.894280],[-0.963114],[4.204202],[0.595976],[9.260238],[4.822375],[6.972695],[7.819751],[-9.592035],[-8.384917],[-1.718597],[9.498460],[-6.090145],[0.161807],[2.476883],[9.317191],[6.855768],[4.736670],[7.917639],[-3.792851],[4.094051],[-0.923741],[-3.486568],[-0.822881],[-5.961874],[6.749210],[-0.309914],[-2.056197],[2.255572],[0.048368],[8.531041],[-8.163597],[-4.352925],[2.751277],[9.567331],[-2.420300],[-2.311374],[1.161742],[-6.716677],[3.705955],[-0.818666],[-5.152550],[2.077866],[-7.530497],[-4.196479],[6.583704],[-2.608636],[-0.029565],[2.178843],[-6.662006],[7.889962],[0.795910],[1.817812],[-7.896095],[-5.800829],[-8.655295],[-2.045470],[3.618725],[-5.908816],[-9.910115],[-5.506386],[-9.826947],[6.312501],[0.720995],[-9.731937],[5.220503],[0.917308],[5.127837],[-0.967464],[-3.790714],[-8.833487],[1.278900],[8.005977],[-2.389086],[-6.609247],[-7.290165],[9.050606],[9.741865],[4.848452],[2.650104],[7.649965],[6.929501],[-0.467993],[8.453914],[-0.445248],[4.142044],[1.724876],[6.264295],[-8.895377],[-3.117652],[-4.493779],[0.827507],[1.800655],[1.549006],[7.402256],[-3.755083],[9.962871],[7.038325],[4.881855],[-7.929798],[7.701549],[-9.301286],[9.031337],[2.713794],[5.887654],[-0.082900],[7.008714],[8.460294],[6.911933],[9.074429],[-2.285958],[7.315669],[-7.466849],[3.292780],[2.203900],[4.643181],[2.425182],[9.491111],[-5.636310],[-6.971297],[-4.796020],[4.010487],[-0.075263],[-0.876615],[4.033215],[8.013709],[-4.316999],[-7.142136],[0.819549],[-0.161688],[5.759966],[0.077126],[9.335288],[0.045857],[-2.810707],[7.126528],[8.103399],[-5.448594],[-1.024744],[6.533661],[-9.106951],[8.215350],[9.876271],[9.436852],[1.313331],[7.579914],[-3.150781],[6.267523],[-0.869539],[3.385287],[3.013739],[5.324507],[3.196922],[-3.282123],[2.349359],[-7.845349],[-2.183600],[-4.811994],[0.174683],[7.222416],[0.350019],[3.787084],[3.974165],[9.507771],[-9.421058],[-4.511701],[3.939195],[-9.051828],[0.248636],[-7.009165],[-5.699926],[9.292665],[-5.147075],[-5.472144],[1.268226],[-9.333763],[-9.235017],[-4.066058],[2.694961],[1.608499],[-6.489061],[9.348011],[-3.687415],[9.122349],[-6.470361],[-0.991751],[-7.797432],[-0.334908],[0.714501],[-7.048028],[-5.795306],[7.215613],[-5.527729],[-5.319299],[5.117361],[5.855598],[-4.921869],[4.703115],[-9.301612],[-2.419217],[2.989291],[4.201427],[-0.176836],[-3.611045],[-4.218301],[1.103735],[-9.727239],[-0.815681],[-7.806813],[-2.822363],[-8.740190],[-8.690559],[-9.501110],[2.342479],[-5.779037],[4.816434],[-4.542303],[6.825192],[-6.711057],[-9.123614],[-3.722829],[9.398719],[-8.917525],[6.220446],[7.015826],[-6.944248],[-6.871011],[-1.484967],[8.623655],[9.128703],[1.663046],[6.265431],[-5.605566],[6.653989],[-2.345118],[6.160200],[3.049871],[4.808567],[-2.375277],[-1.290939],[-2.559156],[-1.237995],[7.205829],[9.624214],[-2.583441],[-7.373326],[-7.983288],[-3.248526],[-6.134219],[2.402331],[6.291867],[5.557542],[-2.712290],[4.299854],[-0.584535],[-6.746168],[-4.214513],[2.093210],[2.416906],[-0.496662],[1.548744],[4.787681],[-2.549771],[-4.113315],[8.248144],[-4.384243],[7.744224],[5.334385],[-3.618899],[-1.764508],[6.280183],[-6.839578],[4.981878],[1.709863],[-8.169745],[9.123501],[0.064940],[0.710894],[-9.209453],[-3.553150],[-1.855322],[-0.415218],[0.422206],[7.400662],[-4.783141],[-0.937387],[-5.200685],[-9.332819],[-2.574137],[-1.653290],[5.998262],[-4.202139],[-3.059685],[6.435370],[-8.760622],[5.988136],[-4.357206],[-4.359556],[2.599780],[7.123613],[2.387111],[5.582518],[-2.677942],[-0.363870],[-5.602514],[-8.991195],[-7.873790],[-1.258177],[-6.566798],[0.350311],[6.245641],[1.571079],[-3.334471],[6.855234],[1.704075],[-8.542493],[-0.519723],[-0.111935],[1.158767],[2.611298],[3.451319],[9.205543],[3.748162],[8.780196],[3.971548],[-9.771723],[1.231245],[-5.017379],[7.183123],[8.582347],[5.662785],[7.380551],[-3.598271],[-6.218281],[-8.370079],[8.208926],[2.450869],[9.701585],[-8.583577],[1.152047],[1.968852],[-2.365809],[9.666486],[0.423378],[8.784482],[-2.746189],[-4.446285],[-6.314798],[5.667600],[-6.304069],[9.213762],[-1.574420],[-3.632373],[0.322240],[-0.081766],[7.397100],[-8.149534],[-4.632353],[-1.570219],[-4.785862],[-6.042048],[-0.060216],[-3.331269],[9.939843],[-3.722998],[-2.431796],[5.321609],[-0.682874],[-9.846842],[-3.911483],[-8.522092],[3.903801],[-8.431281],[1.874008],[7.627328],[-5.281420],[-9.167933],[-7.659111],[3.347964],[-1.715437],[1.333625],[7.483708],[2.915562],[-8.366136],[1.761033],[-3.362415],[-5.493916],[-6.812664],[3.680791],[-2.270372],[3.634036],[3.471926],[0.117096],[0.901418],[2.933687],[-7.013140],[-8.768180],[-0.080233],[-5.559237],[5.528743],[0.936452],[8.862017],[4.855873],[-9.516745],[0.666494],[8.543227],[8.641032],[-3.567365],[-3.837128],[-3.588118],[-9.895312],[-1.565992],[-5.711969],[-3.425797],[-6.013708],[4.913743],[-6.681091],[4.689203],[-0.519988],[-6.289235],[-8.401240],[7.426612],[-7.999826],[5.082826],[4.611961],[9.817289],[-6.235487],[-3.835339],[-3.791945],[4.319917],[-0.197987],[-2.309187],[-6.604347],[1.979717],[-9.986583],[-9.598949],[7.688280],[-2.987047],[-5.694979],[8.450553],[5.952590],[2.534860],[-7.951629],[7.772263],[-4.389580],[8.328771],[6.828572],[3.368464],[-0.174791],[-0.218560],[3.896335],[3.271433],[-2.873344],[-1.794378],[1.371862],[-3.067574],[-0.227592],[5.869824],[0.750841],[5.126021],[5.849702],[8.119488],[3.078465],[-6.830116],[3.559278],[-8.667134],[-0.455567],[2.412260],[4.360278],[4.155880],[2.898570],[-6.573989],[8.716566],[4.457510],[-5.781650],[-9.000710],[9.478972],[-2.703605],[5.939185],[-8.748108],[6.681664],[0.603724],[2.795074],[5.353659],[-8.585472],[7.598378],[-1.689953],[-4.436684],[5.326589],[4.454855],[-4.964891],[-4.609312],[2.239495],[-2.218675],[2.989713],[2.137999],[2.428276],[-8.369480],[9.706828],[-2.149751],[-3.074634],[-9.355714],[4.612088],[-0.999567],[-5.322722],[-7.053401],[-6.363012],[-6.277173],[7.878867],[-3.678425],[-9.140625],[0.249335],[-1.126746],[-8.341665],[2.853126],[6.302442],[-8.266404],[4.474368],[-0.493910],[5.835504],[0.829809],[-7.252603],[-1.546279],[8.120024],[9.296942],[-2.291415],[0.896155],[-7.209144],[-5.858176],[4.517367],[0.645010],[2.994599],[-1.697158],[9.914116],[7.920351],[9.325311],[-5.233811],[-5.468959],[4.458514],[-2.570781],[3.334979],[-5.825869],[-7.699473],[-3.539501],[2.574899],[7.156032],[-7.208398],[-8.040818],[3.106536],[-4.161967],[-2.941579],[3.793157],[7.092477],[5.088207],[2.894212],[0.797655],[5.272163],[8.677071],[-1.803017],[-9.518791],[6.797845],[-7.753805],[-1.550861],[4.488359],[-8.613519],[-5.077470],[2.456332],[3.435220],[8.446256],[9.218262],[-5.242320],[3.174831],[-1.080739],[-6.405854],[-9.722350],[-6.190955],[-7.876845],[-0.068001],[-7.139008],[-0.538850],[9.929293],[8.363843],[-2.001879],[8.462701],[-5.021419],[-9.299335],[8.295981],[-2.998692],[-8.203653],[3.207129],[8.512906],[-7.342301],[-1.150915],[-6.604839],[-3.958083],[-5.118821],[-1.988591],[8.208008],[-9.584627],[-2.718960],[8.303878],[-5.723568],[9.182832],[9.725079],[3.989996],[-3.855587],[-1.708035],[-0.700823],[8.060445],[4.896116],[7.277255],[7.076208],[-1.474719],[-9.199716],[6.420299],[8.016182],[5.336637],[-0.780360],[-7.167301],[-7.351293],[-6.238321],[-8.016695],[8.897870],[0.577453],[8.140313],[5.700044],[-9.356753],[-0.359981],[0.471292],[-2.599142],[-4.489271],[9.351144],[1.887018],[-6.495403],[4.042940],[4.791627],[2.281831],[7.388945],[-9.917503],[-1.936642],[0.160562],[-4.916866],[-9.547183],[-9.331686],[5.701236],[0.684585],[-5.293608],[6.260656],[-0.358131],[3.538758],[-5.806480],[0.786716],[-0.681698],[-3.874757],[2.941003],[8.967449],[-3.774764],[3.075478],[-7.752546],[-0.861041],[-7.195969],[2.883341],[6.455445],[-8.734390],[-7.077526],[1.406664],[-3.972286],[5.615193],[4.126644],[8.768051],[-1.914625],[-7.138181],[-2.753856],[2.898663],[0.067673],[-5.612294],[1.873783],[8.617444],[-3.459966],[-3.288054],[9.186357],[6.669221],[-9.845884],[5.203123],[-3.868211],[0.012272],[2.984166],[-0.699328],[8.584195],[-4.937621],[8.475668],[-5.491040],[8.717492],[5.281675],[8.573966],[-1.684341],[-6.855760],[-0.495072],[-0.076250],[-5.513090],[-9.206282],[1.728254]], dtype = "float64")#candidate|14976|(1456, 1)|const|float64
const_14977 = relay.const([-10,-10,6,-10,1,-2,-5,3,-6,-2,-6,1,1,-9,3,-4,4,4,7,7,-3,-7,8,8,-2,-8,-3,-8,-2,9,9,-6,9,-5,7,-6,-10,9,-3,-3,-7,-1,8,9,8,-5,1,-2,-5,-9,-8,3,10,-8,-8,7,-4,10,-10,3,-6,5,-2,-10,-3,-7,5,-8,9,9,-9,-5,-5,-4,-3], dtype = "uint32")#candidate|14977|(75,)|const|uint32
var_14978 = relay.var("var_14978", dtype = "uint32", shape = ())#candidate|14978|()|var|uint32
call_14975 = relay.TupleGetItem(func_1748_call(relay.reshape(const_14976.astype('float64'), [13, 16, 7]), relay.reshape(const_14977.astype('uint32'), [75,]), relay.reshape(var_14978.astype('uint32'), []), ), 0)
call_14979 = relay.TupleGetItem(func_1753_call(relay.reshape(const_14976.astype('float64'), [13, 16, 7]), relay.reshape(const_14977.astype('uint32'), [75,]), relay.reshape(var_14978.astype('uint32'), []), ), 0)
output = relay.Tuple([call_14972,call_14975,const_14976,const_14977,var_14978,])
output2 = relay.Tuple([call_14973,call_14979,const_14976,const_14977,var_14978,])
func_14982 = relay.Function([var_14978,], output)
mod['func_14982'] = func_14982
mod = relay.transform.InferType()(mod)
var_14983 = relay.var("var_14983", dtype = "uint32", shape = ())#candidate|14983|()|var|uint32
output = func_14982(var_14983)
func_14984 = relay.Function([var_14983], output)
mutated_mod['func_14984'] = func_14984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4637_call = mod.get_global_var('func_4637')
func_4639_call = mutated_mod.get_global_var('func_4639')
call_15054 = relay.TupleGetItem(func_4637_call(), 0)
call_15055 = relay.TupleGetItem(func_4639_call(), 0)
func_14769_call = mod.get_global_var('func_14769')
func_14776_call = mutated_mod.get_global_var('func_14776')
const_15057 = relay.const([[1,-4,1,-3,-6,-8,-7,5,8,7,-1,-1,4,-4,5,-8,9,7,7,-7,-8,-5,-4,5,6,-10,-2,8,5,4,4,-4,-5,5,2,-5,6,3,10,10,1,-5,-10,-8,6,3,-5,5,2,2,-1,-4,8,-5,-7,-6,-4,9,5,9,9,-3,2,6,7,8,6,-3,3,-5,-4,1,4,-3,9,-2,5,5,-1,-1,-1,-6,-5,3,8,10,-1,-1,-1,5,6,8,-1,9,6,-10,-1,3,-5,3,4,-7,-4,-9,-1,-5,-2,-8,-8,6,-9,8,-5,5,7,5,-3,6,1,4],[-10,10,-4,4,7,5,-8,-3,3,-3,10,-2,10,-2,-3,-4,-7,-4,5,4,-10,6,-1,-9,1,-7,-9,3,6,10,-6,-2,-1,6,8,7,-7,6,-4,-6,-8,-3,3,6,-5,-9,-3,4,1,9,7,5,-9,-6,7,-5,5,2,5,-7,4,-9,-1,2,-2,1,-9,5,-9,-10,-3,1,-4,-5,-1,-9,-10,-4,3,5,9,7,2,5,-5,10,-1,-5,4,-5,-2,-9,-7,7,1,9,6,7,8,-1,-8,-10,-10,7,4,-10,-8,-3,4,-7,10,4,-2,5,-2,4,7,-10,-8,2],[8,-8,-1,-3,1,-1,-6,8,-5,-9,-1,-8,6,7,4,3,3,10,6,-10,-3,-9,-5,6,-2,-8,7,-3,-3,-4,2,-1,-3,-1,-2,6,-2,-4,-2,9,-9,-8,3,9,4,5,5,2,-4,-6,4,4,7,-4,-10,4,8,-6,-5,-6,-10,-6,-4,-2,-9,-7,-10,-8,-8,-9,-3,-10,7,3,10,-3,-10,-5,5,-5,6,7,2,7,8,-10,9,6,-5,7,8,-8,-7,7,10,8,5,-6,-3,-8,-8,-3,-8,10,8,9,-7,8,-9,8,6,-9,-1,9,7,6,6,2,-10,7],[4,-6,2,5,-9,-5,8,8,-1,3,4,5,1,-6,-2,9,-7,-6,-10,-2,-3,6,3,1,10,-1,-5,6,4,7,3,1,-4,2,-8,-5,-3,4,-4,7,-1,10,-3,-2,-8,-2,-6,4,-1,-5,9,4,10,8,-3,8,1,9,-4,-2,1,-5,8,8,4,-2,3,6,2,-9,-7,8,-5,-6,10,-9,-4,10,4,3,3,-10,1,-2,-8,-9,-6,-4,8,9,-8,8,3,-5,-8,-4,4,-7,-7,-10,-8,1,8,6,-7,-3,-3,8,1,-4,10,7,-9,-10,3,-5,-9,-8,2,-2]], dtype = "int64")#candidate|15057|(4, 120)|const|int64
var_15058 = relay.var("var_15058", dtype = "uint32", shape = ())#candidate|15058|()|var|uint32
var_15059 = relay.var("var_15059", dtype = "int32", shape = (1056,))#candidate|15059|(1056,)|var|int32
const_15060 = relay.const([-4.913491,2.707891,0.785035,6.602319,-3.700783,-1.093059,-2.799533,9.525529,-8.315133,-3.577756,-0.599101,-7.685030,2.843321,-7.167280,-9.498325,-0.156511,-2.249300,-9.244488,9.079244,0.086588,4.150467,-9.925799,-5.879286,-0.123246,4.636572,-3.044919,8.357854,-2.471043,-4.566371,-1.690089,6.361122,0.726851,-6.816678,9.821713,-2.654668,-0.713588,7.849478,1.923333,-3.136146,-5.706615,-3.189471,5.743990,0.076754,6.635267,-2.938235,1.714827,-4.322424,8.200472,-6.979126,-1.660852,-4.047295,8.982326,0.309648,4.994242,-0.406209,5.467149,-6.360584,2.532014,1.981075,6.467213,-7.276219,9.533985,-4.006135,3.105852,0.779422,1.393521,-1.522387,7.759968,1.975408,2.721815,1.192330,-5.432912,8.288167,4.020434,-7.382683,5.194460,7.087756,7.420087,8.069847,3.556205,-9.122067,-9.755487,6.153678,-4.342130,-3.714973,-8.322642,9.691769,3.911220,-0.807598,4.909033,-4.626541,8.725494,6.329435,5.596486,-7.474063,5.852668,6.954344,0.948287,-3.974343,1.305462,-8.380996,-4.108491,-2.600447,-9.701425,-4.136936,-1.422386,-6.935844,4.268096,-9.368318,9.537771,9.182295,-1.442910,-6.320675,8.722122,0.809556,-1.546311,-5.937182,5.154502,-4.008200,-4.741500,4.135630,5.167475,-5.207894,2.513005,3.715653,3.121589,-3.225832,8.345550,-5.142872,9.451983,8.846578,7.302645,-5.464203,5.733758,-2.290338,4.548632,-4.977572,-5.594779,7.148672,6.420455,-3.172587,2.833107,-9.105284,6.799585,0.226759,5.368275,-3.567942,2.342930,3.715548,-5.517620,-0.055387,-0.293867,-0.253510,5.053166,-4.006074,3.469555,-6.699801,6.615058,3.891990,7.441426,6.619198,-9.316145,4.558010,-7.385802,-2.021930,-6.056962,3.254217,5.871638,6.930406,0.800166,5.675807,-0.515786,-1.747179,2.483957,3.095292,-3.932584,2.164940,-1.608359,-7.951116,2.194538,1.250733,2.789082,-3.545606,9.300362,-0.998173,-8.424224,9.612333,4.834161,-7.034721,2.779164,0.466097,6.787148,-5.416421,3.354570,-1.759759,3.836726,-7.436501,-1.957384,0.653253,9.083211,9.247524,-5.258397,-4.454164,-1.261426,-9.337091,-4.812879,8.154199,-8.031923,-1.160511,7.419628,-9.118768,-5.424523,4.581613,-9.635625,-2.491750,-4.409767,0.677006,-8.296460,-4.592228,-0.939488,7.907604,-1.370704,-3.834590,-3.544287,-0.534626,-3.175930,6.198877,-0.069692,9.371038,6.328381,-5.581529,9.995655,-2.216603,9.344818,-7.025184,8.201339,9.730984,4.499933,-7.697294,-1.330585,0.859474,-3.913129,8.705373,4.132124,5.589296,7.383108,4.256166,1.111918,-7.167715,-7.214170,-9.910383,-4.014311,-6.816798,-7.707097,-6.177185,2.863794,6.147461,-7.773661,-3.934607,5.826022,-9.017048,9.037804,-9.143386,-5.869026,-6.973405,7.253458,-4.790075,-7.237123,6.690881,-9.645937,1.370075,0.612821,4.340750,5.142214,-8.617437,6.420332,8.942571,-2.622750,2.182671,3.393983,3.493017,-5.278457,-5.003851,-4.220312,0.313875,5.408936,3.513954,1.055247,-1.047642,-6.402949,-0.487446,-2.280627,7.952639,6.965050,3.434109,-7.255794,0.976568,-4.362201,8.550453,-6.347990,8.164534,4.163540,-2.826982,3.149789,3.899818,6.249060,6.883896,-9.235787,-4.834157,0.843600,-1.171002,2.398733,3.360293,1.414371,-3.270437,8.696760,-9.240094,-2.844126,-2.981850,9.917420,-3.699878,9.135309,-6.661228,-3.436468,2.333146,-0.483190,7.243918,0.951006,-1.089958,8.964124,-4.914248,-4.281796,5.473264,-4.335007,3.437460,8.409932,-0.603099,0.177831,-4.227930,-5.856808,-6.711497,7.636472,-8.492101,-0.957146,-4.970699,2.892102,-2.529357,1.082107,7.504708,8.157762,3.210879,-2.968250,8.988807,8.404965,3.092682,7.392292,-0.406917,8.770436,-5.858492,0.937108,0.940977,2.613589,5.206248,7.699755], dtype = "float32")#candidate|15060|(364,)|const|float32
var_15061 = relay.var("var_15061", dtype = "float64", shape = (1820,))#candidate|15061|(1820,)|var|float64
call_15056 = relay.TupleGetItem(func_14769_call(relay.reshape(const_15057.astype('int64'), [6, 5, 16]), relay.reshape(const_15057.astype('int64'), [6, 5, 16]), relay.reshape(var_15058.astype('uint32'), []), relay.reshape(var_15059.astype('int32'), [1056,]), relay.reshape(const_15060.astype('float32'), [182, 2]), relay.reshape(var_15061.astype('float64'), [910, 2]), ), 4)
call_15062 = relay.TupleGetItem(func_14776_call(relay.reshape(const_15057.astype('int64'), [6, 5, 16]), relay.reshape(const_15057.astype('int64'), [6, 5, 16]), relay.reshape(var_15058.astype('uint32'), []), relay.reshape(var_15059.astype('int32'), [1056,]), relay.reshape(const_15060.astype('float32'), [182, 2]), relay.reshape(var_15061.astype('float64'), [910, 2]), ), 4)
output = relay.Tuple([call_15054,call_15056,const_15057,var_15058,var_15059,const_15060,var_15061,])
output2 = relay.Tuple([call_15055,call_15062,const_15057,var_15058,var_15059,const_15060,var_15061,])
func_15063 = relay.Function([var_15058,var_15059,var_15061,], output)
mod['func_15063'] = func_15063
mod = relay.transform.InferType()(mod)
var_15064 = relay.var("var_15064", dtype = "uint32", shape = ())#candidate|15064|()|var|uint32
var_15065 = relay.var("var_15065", dtype = "int32", shape = (1056,))#candidate|15065|(1056,)|var|int32
var_15066 = relay.var("var_15066", dtype = "float64", shape = (1820,))#candidate|15066|(1820,)|var|float64
output = func_15063(var_15064,var_15065,var_15066,)
func_15067 = relay.Function([var_15064,var_15065,var_15066,], output)
mutated_mod['func_15067'] = func_15067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6927_call = mod.get_global_var('func_6927')
func_6929_call = mutated_mod.get_global_var('func_6929')
call_15069 = relay.TupleGetItem(func_6927_call(), 0)
call_15070 = relay.TupleGetItem(func_6929_call(), 0)
output = call_15069
output2 = call_15070
func_15071 = relay.Function([], output)
mod['func_15071'] = func_15071
mod = relay.transform.InferType()(mod)
output = func_15071()
func_15072 = relay.Function([], output)
mutated_mod['func_15072'] = func_15072
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15120 = relay.var("var_15120", dtype = "float64", shape = (14, 12, 6))#candidate|15120|(14, 12, 6)|var|float64
var_15121 = relay.var("var_15121", dtype = "float64", shape = (14, 12, 6))#candidate|15121|(14, 12, 6)|var|float64
bop_15122 = relay.floor_mod(var_15120.astype('float64'), relay.reshape(var_15121.astype('float64'), relay.shape_of(var_15120))) # shape=(14, 12, 6)
uop_15133 = relay.acosh(var_15120.astype('float32')) # shape=(14, 12, 6)
output = relay.Tuple([bop_15122,uop_15133,])
output2 = relay.Tuple([bop_15122,uop_15133,])
func_15135 = relay.Function([var_15120,var_15121,], output)
mod['func_15135'] = func_15135
mod = relay.transform.InferType()(mod)
mutated_mod['func_15135'] = func_15135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15135_call = mutated_mod.get_global_var('func_15135')
var_15137 = relay.var("var_15137", dtype = "float64", shape = (14, 12, 6))#candidate|15137|(14, 12, 6)|var|float64
var_15138 = relay.var("var_15138", dtype = "float64", shape = (14, 12, 6))#candidate|15138|(14, 12, 6)|var|float64
call_15136 = func_15135_call(var_15137,var_15138,)
output = call_15136
func_15139 = relay.Function([var_15137,var_15138,], output)
mutated_mod['func_15139'] = func_15139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_15203 = relay.var("var_15203", dtype = "float32", shape = (16, 15, 15))#candidate|15203|(16, 15, 15)|var|float32
uop_15204 = relay.sinh(var_15203.astype('float32')) # shape=(16, 15, 15)
output = relay.Tuple([uop_15204,])
output2 = relay.Tuple([uop_15204,])
func_15213 = relay.Function([var_15203,], output)
mod['func_15213'] = func_15213
mod = relay.transform.InferType()(mod)
var_15214 = relay.var("var_15214", dtype = "float32", shape = (16, 15, 15))#candidate|15214|(16, 15, 15)|var|float32
output = func_15213(var_15214)
func_15215 = relay.Function([var_15214], output)
mutated_mod['func_15215'] = func_15215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6956_call = mod.get_global_var('func_6956')
func_6957_call = mutated_mod.get_global_var('func_6957')
call_15219 = relay.TupleGetItem(func_6956_call(), 0)
call_15220 = relay.TupleGetItem(func_6957_call(), 0)
output = call_15219
output2 = call_15220
func_15227 = relay.Function([], output)
mod['func_15227'] = func_15227
mod = relay.transform.InferType()(mod)
mutated_mod['func_15227'] = func_15227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15227_call = mutated_mod.get_global_var('func_15227')
call_15228 = func_15227_call()
output = call_15228
func_15229 = relay.Function([], output)
mutated_mod['func_15229'] = func_15229
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4849_call = mod.get_global_var('func_4849')
func_4850_call = mutated_mod.get_global_var('func_4850')
call_15307 = relay.TupleGetItem(func_4849_call(), 0)
call_15308 = relay.TupleGetItem(func_4850_call(), 0)
output = call_15307
output2 = call_15308
func_15319 = relay.Function([], output)
mod['func_15319'] = func_15319
mod = relay.transform.InferType()(mod)
mutated_mod['func_15319'] = func_15319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15319_call = mutated_mod.get_global_var('func_15319')
call_15320 = func_15319_call()
output = call_15320
func_15321 = relay.Function([], output)
mutated_mod['func_15321'] = func_15321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
call_15382 = relay.TupleGetItem(func_11147_call(), 0)
call_15383 = relay.TupleGetItem(func_11149_call(), 0)
func_8337_call = mod.get_global_var('func_8337')
func_8340_call = mutated_mod.get_global_var('func_8340')
var_15412 = relay.var("var_15412", dtype = "bool", shape = (11, 195))#candidate|15412|(11, 195)|var|bool
call_15411 = func_8337_call(relay.reshape(var_15412.astype('bool'), [11, 13, 15]), relay.reshape(var_15412.astype('bool'), [11, 13, 15]), )
call_15413 = func_8337_call(relay.reshape(var_15412.astype('bool'), [11, 13, 15]), relay.reshape(var_15412.astype('bool'), [11, 13, 15]), )
func_8272_call = mod.get_global_var('func_8272')
func_8273_call = mutated_mod.get_global_var('func_8273')
call_15422 = func_8272_call()
call_15423 = func_8272_call()
func_7108_call = mod.get_global_var('func_7108')
func_7111_call = mutated_mod.get_global_var('func_7111')
const_15435 = relay.const([-3.676985,-7.567000,2.788581,9.430999,3.884617,-0.084443,-9.584597,-6.357808,-6.581947,6.072488,-6.359832,7.722818,-5.208432,7.227276,9.090596,-9.344177,0.420960,1.719855,-5.647371,-6.088419,1.098802,3.804671,-9.378902,0.289813,5.969620,-9.585500,1.240737,-7.250592,-7.439318,-1.581631,-3.040624,2.931875,7.263494,7.319807,9.123233,-8.989418,-1.424224,-3.165416,9.428518], dtype = "float64")#candidate|15435|(39,)|const|float64
call_15434 = relay.TupleGetItem(func_7108_call(relay.reshape(const_15435.astype('float64'), [39,]), relay.reshape(const_15435.astype('float64'), [39,]), ), 2)
call_15436 = relay.TupleGetItem(func_7111_call(relay.reshape(const_15435.astype('float64'), [39,]), relay.reshape(const_15435.astype('float64'), [39,]), ), 2)
output = relay.Tuple([call_15382,call_15411,var_15412,call_15422,call_15434,const_15435,])
output2 = relay.Tuple([call_15383,call_15413,var_15412,call_15423,call_15436,const_15435,])
func_15451 = relay.Function([var_15412,], output)
mod['func_15451'] = func_15451
mod = relay.transform.InferType()(mod)
var_15452 = relay.var("var_15452", dtype = "bool", shape = (11, 195))#candidate|15452|(11, 195)|var|bool
output = func_15451(var_15452)
func_15453 = relay.Function([var_15452], output)
mutated_mod['func_15453'] = func_15453
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12027_call = mod.get_global_var('func_12027')
func_12028_call = mutated_mod.get_global_var('func_12028')
call_15477 = func_12027_call()
call_15478 = func_12027_call()
func_5059_call = mod.get_global_var('func_5059')
func_5062_call = mutated_mod.get_global_var('func_5062')
var_15491 = relay.var("var_15491", dtype = "bool", shape = ())#candidate|15491|()|var|bool
call_15490 = relay.TupleGetItem(func_5059_call(relay.reshape(var_15491.astype('bool'), [])), 0)
call_15492 = relay.TupleGetItem(func_5062_call(relay.reshape(var_15491.astype('bool'), [])), 0)
output = relay.Tuple([call_15477,call_15490,var_15491,])
output2 = relay.Tuple([call_15478,call_15492,var_15491,])
func_15501 = relay.Function([var_15491,], output)
mod['func_15501'] = func_15501
mod = relay.transform.InferType()(mod)
var_15502 = relay.var("var_15502", dtype = "bool", shape = ())#candidate|15502|()|var|bool
output = func_15501(var_15502)
func_15503 = relay.Function([var_15502], output)
mutated_mod['func_15503'] = func_15503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5257_call = mod.get_global_var('func_5257')
func_5259_call = mutated_mod.get_global_var('func_5259')
call_15507 = relay.TupleGetItem(func_5257_call(), 0)
call_15508 = relay.TupleGetItem(func_5259_call(), 0)
output = call_15507
output2 = call_15508
func_15511 = relay.Function([], output)
mod['func_15511'] = func_15511
mod = relay.transform.InferType()(mod)
mutated_mod['func_15511'] = func_15511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15511_call = mutated_mod.get_global_var('func_15511')
call_15512 = func_15511_call()
output = call_15512
func_15513 = relay.Function([], output)
mutated_mod['func_15513'] = func_15513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7885_call = mod.get_global_var('func_7885')
func_7886_call = mutated_mod.get_global_var('func_7886')
call_15530 = relay.TupleGetItem(func_7885_call(), 0)
call_15531 = relay.TupleGetItem(func_7886_call(), 0)
func_9644_call = mod.get_global_var('func_9644')
func_9645_call = mutated_mod.get_global_var('func_9645')
call_15532 = func_9644_call()
call_15533 = func_9644_call()
output = relay.Tuple([call_15530,call_15532,])
output2 = relay.Tuple([call_15531,call_15533,])
func_15551 = relay.Function([], output)
mod['func_15551'] = func_15551
mod = relay.transform.InferType()(mod)
output = func_15551()
func_15552 = relay.Function([], output)
mutated_mod['func_15552'] = func_15552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13763_call = mod.get_global_var('func_13763')
func_13765_call = mutated_mod.get_global_var('func_13765')
call_15684 = relay.TupleGetItem(func_13763_call(), 1)
call_15685 = relay.TupleGetItem(func_13765_call(), 1)
output = relay.Tuple([call_15684,])
output2 = relay.Tuple([call_15685,])
func_15691 = relay.Function([], output)
mod['func_15691'] = func_15691
mod = relay.transform.InferType()(mod)
output = func_15691()
func_15692 = relay.Function([], output)
mutated_mod['func_15692'] = func_15692
mutated_mod = relay.transform.InferType()(mutated_mod)
const_15699 = relay.const([[[4.364834,-8.078572,-5.530105],[8.018654,-1.639405,-5.460430],[-7.432682,-0.939689,5.784992],[3.365554,-9.327346,5.330487],[1.623186,-7.833802,-0.799081],[-6.851994,-2.565541,-8.823670],[2.593340,3.328831,0.492247],[-0.502148,-5.710753,-5.838874]],[[-0.244686,4.991784,1.879126],[-3.787603,-4.087908,0.325891],[7.637877,-6.874765,4.534027],[-9.646073,5.886182,-7.880416],[9.688127,-5.394698,1.681676],[-0.210729,-9.093465,-7.487137],[-8.366945,2.963378,9.608656],[2.949100,-7.259649,1.415289]],[[-8.755652,4.896989,0.255627],[-5.826456,-1.841571,-4.360578],[0.842557,-0.658452,-4.174388],[-1.771287,7.127873,4.300548],[-2.174323,7.570108,2.122978],[-2.202176,-2.689515,0.798660],[-4.304042,3.712183,-0.792655],[-7.246318,-0.521222,-8.743724]],[[-5.514505,6.798022,-2.340704],[-9.229901,1.209914,1.342595],[-8.660536,-9.759627,4.054881],[-5.810055,9.434119,5.026443],[4.481824,0.675029,-6.097418],[-4.362544,-7.898409,-6.220918],[3.907150,-1.767471,8.675733],[9.215971,3.277192,-9.306460]],[[4.578507,-6.531407,-6.121404],[-0.076789,-5.502366,5.515593],[2.993924,8.058208,5.740357],[-5.910139,-1.349658,3.148695],[5.271622,-3.508788,-9.186500],[0.984524,1.456204,-0.383071],[7.255463,-4.536355,4.410245],[-6.030991,0.020124,-6.225266]]], dtype = "float32")#candidate|15699|(5, 8, 3)|const|float32
var_15700 = relay.var("var_15700", dtype = "float32", shape = (5, 8, 3))#candidate|15700|(5, 8, 3)|var|float32
bop_15701 = relay.subtract(const_15699.astype('float32'), relay.reshape(var_15700.astype('float32'), relay.shape_of(const_15699))) # shape=(5, 8, 3)
func_14901_call = mod.get_global_var('func_14901')
func_14903_call = mutated_mod.get_global_var('func_14903')
call_15729 = func_14901_call()
call_15730 = func_14901_call()
func_14167_call = mod.get_global_var('func_14167')
func_14170_call = mutated_mod.get_global_var('func_14170')
var_15733 = relay.var("var_15733", dtype = "float32", shape = (400, 1))#candidate|15733|(400, 1)|var|float32
call_15732 = relay.TupleGetItem(func_14167_call(relay.reshape(var_15733.astype('float32'), [400,])), 1)
call_15734 = relay.TupleGetItem(func_14170_call(relay.reshape(var_15733.astype('float32'), [400,])), 1)
func_3372_call = mod.get_global_var('func_3372')
func_3374_call = mutated_mod.get_global_var('func_3374')
call_15757 = relay.TupleGetItem(func_3372_call(relay.reshape(bop_15701.astype('float64'), [1, 15, 8])), 0)
call_15758 = relay.TupleGetItem(func_3374_call(relay.reshape(bop_15701.astype('float64'), [1, 15, 8])), 0)
output = relay.Tuple([bop_15701,call_15729,call_15732,var_15733,call_15757,])
output2 = relay.Tuple([bop_15701,call_15730,call_15734,var_15733,call_15758,])
func_15759 = relay.Function([var_15700,var_15733,], output)
mod['func_15759'] = func_15759
mod = relay.transform.InferType()(mod)
var_15760 = relay.var("var_15760", dtype = "float32", shape = (5, 8, 3))#candidate|15760|(5, 8, 3)|var|float32
var_15761 = relay.var("var_15761", dtype = "float32", shape = (400, 1))#candidate|15761|(400, 1)|var|float32
output = func_15759(var_15760,var_15761,)
func_15762 = relay.Function([var_15760,var_15761,], output)
mutated_mod['func_15762'] = func_15762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13614_call = mod.get_global_var('func_13614')
func_13616_call = mutated_mod.get_global_var('func_13616')
call_15804 = func_13614_call()
call_15805 = func_13614_call()
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_15816 = relay.TupleGetItem(func_5203_call(), 0)
call_15817 = relay.TupleGetItem(func_5205_call(), 0)
func_13614_call = mod.get_global_var('func_13614')
func_13616_call = mutated_mod.get_global_var('func_13616')
call_15829 = func_13614_call()
call_15830 = func_13614_call()
func_4445_call = mod.get_global_var('func_4445')
func_4448_call = mutated_mod.get_global_var('func_4448')
const_15874 = relay.const([[5.849371],[-7.098569],[-7.616170],[1.787328],[-0.123017],[8.367153],[6.203403],[-6.673583],[0.498382],[4.829726],[-8.951317],[-5.979993],[-6.273469],[8.423500],[-3.720160],[9.805554],[8.457242],[-6.302022],[-0.145939],[8.373597],[6.571641],[9.673353],[4.080074],[0.428227],[-6.977239],[6.017513],[-9.345985],[-8.394688],[2.325424],[-7.120371],[-5.510288],[3.972044],[3.473027],[4.145038],[9.090194],[-0.827276],[-4.280347],[-1.178896],[8.404997],[-6.636421],[-9.013850],[-2.402643],[6.918731],[5.747192],[-9.635119],[2.259556],[-0.998559],[-2.649830],[-6.426610],[6.858881],[-9.757553],[-7.667373],[0.275319],[6.081298],[0.151773],[-0.388404],[5.149213],[-6.837051],[-4.877258],[1.430221],[4.499569],[8.566462],[-5.218628],[3.116923],[1.542057],[-3.703893],[-0.559180],[-1.793688],[9.758112],[-6.092800],[-2.943531],[1.839687],[0.186355],[-0.246658],[1.931716],[-4.467683],[-0.312029],[-7.713689],[-8.197744],[-6.927598],[-1.663263],[9.773329],[9.009854],[-8.217946],[1.896729],[1.409426],[-0.206590],[3.937954],[9.226305],[0.428536],[-9.482154],[9.202278],[9.158175],[5.865046],[-0.111002],[8.856243],[-1.007889],[8.611465],[7.965374],[6.747862],[1.087401],[-0.391456],[0.664874],[9.617233],[3.644194],[4.871716],[8.106341],[2.695754],[3.563557],[-4.597897],[-0.446520],[-9.633175],[-6.889375],[-9.708741],[-8.517303],[1.371920],[0.169982],[9.004109],[2.921618],[6.356926],[5.088204],[-0.975176],[0.481324],[1.664829],[-0.908085],[-2.358597],[8.853173],[-8.929098],[8.421916],[5.251393],[-3.040615],[5.455193],[-2.549382],[-4.518935],[0.003028],[6.504868],[-4.363836],[4.512659],[6.056280],[-2.626616],[-1.052306],[-2.421391],[-8.588732],[-4.811390],[2.655104],[4.764961],[-8.907666],[2.525000],[6.239947],[-8.466551],[0.415116],[1.546580],[-5.109948],[-0.151996],[4.756200],[6.585412],[6.561977],[8.970347],[-6.665305],[5.839752],[-3.555377],[7.987997],[5.194504],[1.694657],[-1.725684],[-2.355599],[5.533522],[-8.389347],[-6.902056],[4.332398],[6.030362],[-1.994336],[-3.155488],[-5.434133],[0.074312],[2.269761],[-3.965604],[-0.768889],[7.844297],[-9.665304],[6.813698],[-2.081120],[-0.099048],[-5.455668],[8.243984],[-4.599965],[3.578147],[7.027959],[3.931099],[-4.513711],[-8.938929],[-8.472197],[5.633725],[-9.496446],[-2.475294],[-1.581685],[6.577652],[7.666355],[3.880727],[8.862422],[4.959844],[-7.797757],[-5.960597],[1.397202],[0.851030],[-4.363464],[0.406012],[4.054485],[6.936989],[7.630543],[-9.177306],[8.182897],[-1.796047],[-8.465331],[5.127848],[-9.535528],[6.363178],[2.067236],[6.403989],[6.384663],[-7.034963],[-0.913912],[-1.253398],[-4.391142],[9.790385],[-8.888085],[-9.017216],[-0.753739],[-2.092087],[-8.486837],[-6.316505],[-9.191293],[8.476414],[0.005378],[-9.999676],[-9.718236],[-5.779811],[-5.275204],[-8.909509],[-5.260743],[9.498198],[1.714407],[-6.296509],[-6.234238],[-8.663785],[-9.294438],[-4.213195],[9.547747],[-8.168795],[-2.254758],[2.259849],[-6.926768],[1.709981],[6.240712],[8.395064],[0.900935],[-7.371885],[-9.382053],[-2.874027],[9.699884],[-7.363869],[2.363238],[-4.063078],[-3.554931],[0.723782],[-7.207335],[0.577621],[-8.482889],[7.026179],[-5.940470],[9.138380],[7.317660],[7.129062],[7.109602],[3.940269],[-9.478792],[-0.319178],[-7.701875],[-7.276075],[-4.916946],[1.381590],[8.060058],[5.204475],[5.691856],[7.445968],[9.282288],[0.985382],[-4.543086],[2.888587],[8.318491],[-6.538088],[-5.448861],[7.228554],[6.298570],[3.980026],[-5.747013],[-6.248788],[-6.987860],[4.658183],[6.792099],[0.245624],[-1.677410],[0.123650],[3.054435],[-1.013397],[6.565233],[4.748072],[6.990517],[-0.867317],[-8.816920],[-1.618612],[-9.068740],[-1.127825],[-8.323580],[-0.739715],[-2.986733],[6.031549],[0.226066],[4.811540],[1.596272],[5.289911],[-5.947505],[-1.112907],[2.350913],[3.890924],[-6.085883],[-4.968704],[-9.865920],[1.676923],[2.515966],[-9.209066],[-4.976989],[-1.447287],[1.106415],[-4.495701],[6.851473],[5.218067],[-6.925450],[9.734452],[6.779917],[-2.686281],[2.355718],[-4.656913],[2.670008],[-8.823487],[-1.919482],[5.368812],[-9.835405],[-0.478421],[4.361822],[-2.166261],[-9.560846],[9.270141],[4.661520],[-3.008764],[3.503939],[0.155057],[-7.017115],[-5.344297],[6.542932],[-6.164790],[-0.847052],[-5.941001],[0.746664],[-3.573037],[-6.685447],[7.069246],[-1.526357],[9.434764],[7.595865],[-4.406079],[-7.134824],[4.476163],[-6.884972],[7.117932],[6.234344],[5.565739],[2.105786],[-4.880406],[-3.016481],[1.518471],[-2.828939],[7.547026],[4.667411],[-2.446056],[-5.018608],[8.242623],[-2.776299],[4.301782],[4.025848],[9.889362],[-2.049336],[-1.351968],[-6.667567],[-3.695810],[5.240423],[8.733119],[-6.051348],[-8.414702],[-9.431977],[5.559219],[-9.358557],[3.092125],[3.259258],[2.178804],[2.949017],[4.607395],[9.845809],[6.074752],[1.223932],[-0.051602],[-7.122322],[-2.835026],[-2.402776],[-4.003772],[3.300113],[2.572256],[0.728421],[0.479175],[-4.973566],[9.557402],[6.389275],[2.379329],[-6.688341],[-7.970012],[7.005774],[-1.502542],[0.635209],[-2.407360],[8.516158],[-0.581080],[-6.385251],[-8.957182],[-7.057784],[5.016518],[-0.939008],[7.483212],[2.941699],[-5.154675],[2.269405],[3.788562],[4.850193],[-0.396783],[-7.397309],[-5.919547],[-5.469160],[0.816510],[4.671032],[-3.671680],[8.473021]], dtype = "float64")#candidate|15874|(450, 1)|const|float64
call_15873 = relay.TupleGetItem(func_4445_call(relay.reshape(const_15874.astype('float64'), [450,])), 2)
call_15875 = relay.TupleGetItem(func_4448_call(relay.reshape(const_15874.astype('float64'), [450,])), 2)
func_5269_call = mod.get_global_var('func_5269')
func_5271_call = mutated_mod.get_global_var('func_5271')
call_15877 = relay.TupleGetItem(func_5269_call(), 0)
call_15878 = relay.TupleGetItem(func_5271_call(), 0)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
call_15881 = relay.TupleGetItem(func_11147_call(), 0)
call_15882 = relay.TupleGetItem(func_11149_call(), 0)
uop_15884 = relay.exp(const_15874.astype('float64')) # shape=(450, 1)
bop_15886 = relay.greater(uop_15884.astype('bool'), relay.reshape(const_15874.astype('bool'), relay.shape_of(uop_15884))) # shape=(450, 1)
bop_15913 = relay.logical_and(uop_15884.astype('bool'), relay.reshape(bop_15886.astype('bool'), relay.shape_of(uop_15884))) # shape=(450, 1)
output = relay.Tuple([call_15804,call_15816,call_15829,call_15873,call_15877,call_15881,bop_15913,])
output2 = relay.Tuple([call_15805,call_15817,call_15830,call_15875,call_15878,call_15882,bop_15913,])
func_15921 = relay.Function([], output)
mod['func_15921'] = func_15921
mod = relay.transform.InferType()(mod)
output = func_15921()
func_15922 = relay.Function([], output)
mutated_mod['func_15922'] = func_15922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13132_call = mod.get_global_var('func_13132')
func_13133_call = mutated_mod.get_global_var('func_13133')
call_15933 = relay.TupleGetItem(func_13132_call(), 1)
call_15934 = relay.TupleGetItem(func_13133_call(), 1)
output = call_15933
output2 = call_15934
func_15943 = relay.Function([], output)
mod['func_15943'] = func_15943
mod = relay.transform.InferType()(mod)
mutated_mod['func_15943'] = func_15943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_15943_call = mutated_mod.get_global_var('func_15943')
call_15944 = func_15943_call()
output = call_15944
func_15945 = relay.Function([], output)
mutated_mod['func_15945'] = func_15945
mutated_mod = relay.transform.InferType()(mutated_mod)
const_15959 = relay.const([[[-7,3,4,-8],[-5,-8,5,-9],[2,-9,-4,9],[8,-8,10,2],[-7,-5,8,-5],[2,-8,-5,-3],[-9,-5,3,-4],[-7,-7,-6,-6],[2,3,-5,-5],[-4,-6,-9,5],[1,3,-5,7],[9,10,-1,-8]],[[8,-4,-2,9],[-1,-6,-4,-8],[-4,-9,10,-2],[9,6,-10,4],[-6,8,9,-5],[-4,1,-3,-1],[2,7,-7,10],[-2,-6,1,-10],[-10,8,-8,2],[-5,8,-1,-6],[-2,-4,-3,-2],[3,9,10,4]],[[10,1,-6,-9],[-5,-10,7,-1],[10,-7,4,-1],[-9,-2,2,1],[9,-9,7,3],[-7,8,10,5],[7,-4,-1,-7],[-5,-9,6,-8],[-4,-7,7,2],[-4,9,2,-5],[-6,-9,1,-9],[-6,5,10,6]],[[-2,-4,-6,4],[1,-5,9,-1],[8,-6,-7,-7],[-5,6,8,1],[6,1,-4,-3],[10,7,7,-6],[1,5,-7,2],[7,-7,-9,-6],[-6,8,-2,4],[-8,-3,2,-1],[9,10,10,-8],[-9,1,5,-6]],[[4,10,4,10],[-6,10,-2,10],[6,-9,-1,3],[-4,-1,-2,10],[10,4,6,7],[-6,-2,7,2],[-2,-10,-10,5],[9,-4,3,-7],[-6,7,6,5],[-1,2,9,-1],[-7,-3,6,-4],[4,-4,-2,9]],[[5,-1,2,-2],[-3,10,10,-10],[-2,7,-1,-3],[-9,-1,9,10],[-10,4,6,-4],[2,-10,7,3],[-5,7,9,10],[-6,-10,2,10],[10,-3,-10,7],[3,6,1,9],[-8,-1,-8,-7],[-3,1,7,-9]],[[-5,-7,-1,9],[-6,-4,-2,3],[1,9,5,6],[-4,-7,-10,10],[-9,2,-3,-6],[4,6,-4,8],[-2,-7,-4,7],[9,1,-10,-7],[-9,-9,-8,3],[-4,9,-7,5],[5,-6,-4,7],[7,-5,10,-6]],[[-8,3,-9,-1],[-5,-2,7,-2],[9,1,1,9],[7,-2,7,-8],[-2,-3,9,-5],[4,9,-5,4],[-8,-9,3,6],[-3,9,-8,-5],[9,-3,-3,7],[8,-9,-8,8],[7,5,-5,-4],[-1,10,-1,10]],[[-4,10,-3,-3],[6,5,4,-10],[-3,5,-7,-8],[-1,6,3,1],[10,3,10,-8],[9,-10,9,5],[6,9,8,-2],[6,-8,5,-6],[-1,-2,-6,-7],[4,-9,-7,4],[-6,-7,-2,3],[10,-9,-3,1]],[[4,4,4,7],[9,2,10,-9],[8,-1,6,8],[-7,2,2,3],[9,-7,1,2],[10,3,-1,-8],[-8,-1,5,2],[-6,2,-10,-7],[-4,-1,-10,4],[10,-10,2,9],[-9,6,-10,5],[-5,-8,-4,1]],[[9,5,-8,9],[-8,6,-9,10],[7,-1,6,-5],[-5,-3,9,-8],[-9,-8,-4,2],[8,-10,5,6],[-5,1,2,-2],[10,-5,3,-7],[-8,7,4,2],[1,10,3,8],[-2,1,4,1],[3,2,1,6]],[[4,1,-7,1],[-6,-4,6,9],[2,4,-3,1],[-2,2,2,-5],[5,6,1,-10],[8,-6,-7,-4],[4,4,-2,-3],[-7,10,-5,10],[2,-2,3,10],[7,6,10,2],[8,1,-10,-8],[1,8,4,-8]],[[4,-9,-3,8],[4,3,-6,8],[-10,7,5,-6],[-5,4,4,8],[-3,5,-6,5],[1,-4,2,4],[-2,9,6,4],[4,3,-2,-4],[-7,-3,5,3],[-6,4,10,10],[-9,-7,-8,8],[-1,-8,1,-9]],[[4,-3,8,7],[-2,3,-1,2],[-2,6,-2,-2],[7,-5,1,-9],[4,3,8,9],[3,2,5,-3],[-2,8,3,-4],[-7,1,5,-4],[3,-2,-7,1],[-2,-3,6,3],[3,10,9,-8],[-7,6,-10,10]]], dtype = "int32")#candidate|15959|(14, 12, 4)|const|int32
var_15960 = relay.var("var_15960", dtype = "int32", shape = (14, 12, 4))#candidate|15960|(14, 12, 4)|var|int32
bop_15961 = relay.bitwise_or(const_15959.astype('int32'), relay.reshape(var_15960.astype('int32'), relay.shape_of(const_15959))) # shape=(14, 12, 4)
uop_15973 = relay.log(bop_15961.astype('float32')) # shape=(14, 12, 4)
uop_16001 = relay.sin(uop_15973.astype('float32')) # shape=(14, 12, 4)
bop_16005 = relay.subtract(uop_15973.astype('int32'), relay.reshape(const_15959.astype('int32'), relay.shape_of(uop_15973))) # shape=(14, 12, 4)
func_8278_call = mod.get_global_var('func_8278')
func_8280_call = mutated_mod.get_global_var('func_8280')
call_16025 = func_8278_call()
call_16026 = func_8278_call()
func_12682_call = mod.get_global_var('func_12682')
func_12685_call = mutated_mod.get_global_var('func_12685')
const_16029 = relay.const(-3, dtype = "uint64")#candidate|16029|()|const|uint64
call_16028 = relay.TupleGetItem(func_12682_call(relay.reshape(const_16029.astype('uint64'), [])), 0)
call_16030 = relay.TupleGetItem(func_12685_call(relay.reshape(const_16029.astype('uint64'), [])), 0)
func_9332_call = mod.get_global_var('func_9332')
func_9336_call = mutated_mod.get_global_var('func_9336')
var_16035 = relay.var("var_16035", dtype = "float32", shape = (154,))#candidate|16035|(154,)|var|float32
var_16036 = relay.var("var_16036", dtype = "int64", shape = (616,))#candidate|16036|(616,)|var|int64
call_16034 = relay.TupleGetItem(func_9332_call(relay.reshape(var_16035.astype('float32'), [1, 11, 14]), relay.reshape(var_16036.astype('int64'), [616,]), ), 1)
call_16037 = relay.TupleGetItem(func_9336_call(relay.reshape(var_16035.astype('float32'), [1, 11, 14]), relay.reshape(var_16036.astype('int64'), [616,]), ), 1)
output = relay.Tuple([uop_16001,bop_16005,call_16025,call_16028,const_16029,call_16034,var_16035,var_16036,])
output2 = relay.Tuple([uop_16001,bop_16005,call_16026,call_16030,const_16029,call_16037,var_16035,var_16036,])
func_16056 = relay.Function([var_15960,var_16035,var_16036,], output)
mod['func_16056'] = func_16056
mod = relay.transform.InferType()(mod)
var_16057 = relay.var("var_16057", dtype = "int32", shape = (14, 12, 4))#candidate|16057|(14, 12, 4)|var|int32
var_16058 = relay.var("var_16058", dtype = "float32", shape = (154,))#candidate|16058|(154,)|var|float32
var_16059 = relay.var("var_16059", dtype = "int64", shape = (616,))#candidate|16059|(616,)|var|int64
output = func_16056(var_16057,var_16058,var_16059,)
func_16060 = relay.Function([var_16057,var_16058,var_16059,], output)
mutated_mod['func_16060'] = func_16060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12719_call = mod.get_global_var('func_12719')
func_12720_call = mutated_mod.get_global_var('func_12720')
call_16125 = func_12719_call()
call_16126 = func_12719_call()
func_1748_call = mod.get_global_var('func_1748')
func_1753_call = mutated_mod.get_global_var('func_1753')
const_16152 = relay.const([-1.294465,-5.821998,7.709019,-1.236645,5.400258,-3.264056,-4.989670,-1.342916,-2.893376,-4.682042,-7.030532,7.761418,-4.359066,1.120740,0.567596,-3.444882,4.726896,-4.151533,-1.567550,-7.705825,-8.942533,2.458095,-6.643022,1.681148,0.053662,-0.530797,1.824464,-9.548948,2.572928,0.990523,-7.729765,-4.168130,0.129290,5.624627,5.198227,2.895063,-5.123101,4.099452,-0.632366,9.769639,-4.417737,-5.267960,-0.810738,4.385804,-1.877424,-1.596239,3.207079,-1.841165,3.480054,-3.652339,9.824446,7.660883,-5.937117,-7.344363,7.215532,-8.775584,9.969443,9.284957,7.146967,9.664730,0.874380,4.728556,-4.680171,7.227176,2.307893,7.855305,-2.736194,-5.317123,0.937087,1.149494,-9.560211,-5.453646,-1.895653,3.287732,3.715075,0.706943,-0.246192,6.726239,-9.640549,1.866306,-5.809499,-9.629561,7.372176,4.495000,8.313170,7.646118,-6.002912,-7.675180,1.678628,-9.378383,-0.508153,1.571081,-9.382207,-7.436332,-5.927862,-3.257324,-5.633648,4.457604,4.920196,-6.832190,9.603674,3.227049,9.141979,9.391704,7.214980,0.615230,5.661192,5.342116,9.327816,3.450521,9.368750,-1.998480,-1.052129,7.017430,-0.415025,6.342061,1.126337,8.506912,-4.560294,2.032343,9.811627,6.135581,6.299765,-0.649080,-9.039829,-7.127902,-2.239004,6.598253,-6.973762,-0.554840,-5.187472,0.481136,-3.630720,6.958648,2.211154,2.861513,8.971687,3.959107,2.819667,-9.142369,1.926391,3.650969,5.034542,5.258414,5.200327,8.018618,9.261040,3.528722,1.707893,-0.782223,4.080239,2.293461,-3.529390,0.464186,4.748842,-2.928850,5.200522,-4.258766,-9.825125,-7.477626,8.950767,-8.954125,-2.258670,9.089477,-1.574761,-5.556964,4.877358,-0.359210,6.768550,0.319090,9.911877,6.352621,5.964645,-2.280250,1.325516,0.435621,-1.903038,5.492838,8.768071,-4.206808,-6.724536,3.039864,5.853064,-2.516863,8.018630,2.619200,6.182085,8.294084,-0.962410,-8.268566,8.534978,-2.952905,6.211316,-9.080555,-2.092088,-4.459162,-3.092999,-3.589576,-8.104182,-2.424192,-5.421278,-2.721728,-1.838408,-7.479117,9.702371,5.665066,-0.127292,-1.408943,3.845544,-4.453908,-4.085443,5.121584,-7.753588,-7.256611,-8.554288,7.708056,-5.624232,-4.572671,3.516378,3.992477,8.553893,1.235351,-0.484760,-0.244651,1.973109,-0.036884,5.143550,-2.538572,0.837410,-1.125151,7.526360,2.171295,-0.021327,-8.654797,-8.232136,-0.737563,-9.396180,-2.185804,-4.371442,2.458827,5.240089,7.997743,9.483219,9.321727,-1.548919,-3.113518,8.117353,2.961609,0.238472,8.598212,2.574077,3.862536,-1.082557,-9.041300,-2.973452,-5.471499,3.180746,4.336091,9.142154,-6.383838,-3.384217,3.313390,-8.574507,7.324329,-2.974131,3.915659,0.193796,-9.726430,-6.358581,-6.978860,-7.794020,5.602381,-7.120962,-0.777217,2.657051,0.649231,5.581869,9.206137,6.550266,6.765789,2.895179,2.798465,1.179603,-9.805780,-4.454867,2.019498,0.179197,3.218400,3.862071,8.929357,-9.462790,-7.678176,8.347753,1.729428,0.655313,9.046612,9.779430,9.206133,-2.866883,4.568362,-5.968944,6.515963,5.369961,4.783752,-4.856223,5.151465,7.498154,-0.979486,0.393453,2.021268,-4.780155,6.244105,0.992632,-2.823719,6.191751,-9.502921,-8.791920,3.724453,-3.352782,-0.946467,-1.040591,4.475261,-3.910649,-5.527208,9.530363,-3.481726,-9.452567,-4.261767,-9.432105,8.070254,-0.559206,3.357976,9.559165,-7.633340,4.193304,-8.271655,-6.602178,8.745418,2.450532,-5.703174,3.960192,-4.869105,-6.033199,0.229289,-2.317127,-6.071399,-4.773605,6.826745,1.766328,-9.583450,5.805490,-9.612541,-6.741448,-2.439417,2.421590,1.442172,1.648916,3.686840,-6.227288,-9.553178,3.940078,5.290290,-0.452268,-5.362983,-1.153772,-5.983807,9.556933,0.755185,-1.162041,-6.063457,-0.916485,-5.954954,5.475580,4.234107,-1.455447,-4.352942,8.481124,7.855985,2.816066,2.903593,-9.314999,3.799035,-9.575110,-3.084516,-0.598782,-3.411402,-7.333327,-4.677667,-0.927488,9.093861,8.377219,4.419404,4.687846,-1.845739,-8.130123,-1.525610,1.396895,-1.965851,-7.917069,-7.039069,8.468524,5.126098,4.447782,-2.364495,8.034736,-6.711731,5.574309,0.400886,-5.954498,1.572751,1.675355,-9.274167,1.447826,-7.680354,1.768083,-8.546617,-0.812504,-7.998585,1.304720,1.830209,-1.844044,4.876771,3.008307,-4.457856,-1.914891,-7.665915,8.608792,-9.565882,-8.905896,-5.749065,8.080707,-2.406098,-4.727453,8.695505,1.997607,-4.363583,-1.983264,-2.477925,5.965081,-1.850025,-0.887694,5.685022,6.655021,1.438598,3.868799,2.793803,-5.783614,-7.645191,-8.679516,3.175934,-3.575079,8.158270,7.776274,1.654254,-5.620009,2.283286,-0.824773,-1.510114,-7.917815,6.413456,6.859797,9.138666,7.155788,-8.157221,5.880421,9.548410,6.959231,0.377020,-1.672335,0.108247,-2.368451,-6.652496,-0.562832,-6.653638,-6.719378,-5.028452,-3.536140,7.962559,7.521890,9.328298,8.198952,-0.199780,7.605810,-8.351997,-7.502646,-9.368108,-5.697233,-8.081290,1.876601,2.173002,-2.922606,3.778412,0.148680,-2.438436,-8.397358,-0.783554,4.979544,-4.690702,-0.770071,-1.980471,3.155690,7.684566,8.360134,-5.163891,-9.805847,-4.840616,8.286342,1.899245,6.865007,4.212066,0.206269,6.213954,-3.905494,5.531320,-4.745459,-4.310789,-1.947791,4.937470,8.798553,-3.828054,-8.937103,-9.840686,-0.231336,-8.686691,-0.258859,5.612860,0.565253,-7.612691,-2.324015,-5.502388,5.715411,-8.565830,-1.100078,-3.543634,2.414448,3.858825,0.088449,8.097755,2.542579,3.653269,4.873470,1.773926,-7.465233,8.818366,0.712013,9.510997,-5.707726,-1.160864,-7.306337,-5.440772,5.322924,3.472583,9.526042,-8.781486,-8.761797,-2.760000,-0.557392,3.748944,3.895656,-9.891486,-9.886989,-2.458229,7.350898,-9.546826,1.746749,-8.854471,-2.084659,6.485643,-7.562270,0.470046,-0.340193,0.834640,4.273164,4.564383,3.504610,-5.928813,3.167978,-4.510982,2.700736,-2.516130,3.079770,-2.800488,-1.227339,5.822599,7.157052,-9.146476,9.026123,8.150602,-2.596417,9.808194,-9.123995,2.689011,-8.403541,-4.974161,-9.028167,-0.460600,4.755161,-2.194049,7.487245,2.149826,-2.167075,-2.168482,5.010528,-0.376605,-9.943918,6.106607,4.609322,-3.144050,-9.270575,-2.691182,-3.926140,-6.961393,6.298216,9.986963,-6.023991,7.924196,-9.158617,-0.989546,8.764828,6.844274,5.189354,-0.110953,-4.399538,-4.555163,-6.751660,7.687414,-0.507279,-2.923871,-1.996180,-8.012507,-2.385647,2.569912,4.966003,-6.587394,9.315900,-4.468868,-1.886533,6.485816,9.037747,5.097992,-3.428058,-1.725659,-0.825520,-2.416125,2.232053,-7.947332,0.330093,-9.982842,8.752526,0.908827,4.348120,8.293100,5.830857,-4.819402,9.568384,-9.836715,-9.989109,-2.235895,1.173380,-6.687322,0.009007,8.636011,-9.829886,1.148565,-9.041247,-9.289498,-3.825375,-4.861446,9.098783,-3.747128,-3.582800,-7.755154,-6.725155,-9.312487,-3.712301,-7.034544,2.386647,-5.428176,8.583096,3.279322,-5.251197,7.017686,-3.840721,-7.745598,-4.479648,-3.728336,0.347540,-9.090247,7.142216,-4.913406,0.951540,6.846473,-7.702496,-1.556487,5.666859,6.320248,-5.616577,-1.757619,-2.437538,-8.534468,9.296230,-4.576088,8.864491,-0.142168,0.969891,-3.879232,4.864915,5.304826,4.691201,-7.089675,7.217518,3.445005,-9.456295,-7.763976,-1.697999,-1.589723,6.048044,4.485542,8.297027,5.840076,-3.832808,4.779057,3.613972,3.186691,-2.312960,2.969558,4.596933,4.056921,-7.938154,4.407832,-3.582179,6.617520,-6.087198,5.045169,-1.054065,-5.021307,-4.582974,2.575848,-9.442543,8.933781,-7.123493,-0.358726,1.874007,1.588166,-8.491730,-8.466668,-2.741881,-7.440774,-5.314816,-9.060558,2.073742,9.423874,-7.804793,6.004900,6.139694,-6.148480,-4.965390,-3.742069,-5.294980,5.232185,-8.053479,-9.415616,8.152256,1.156794,-5.831675,0.041379,-1.128369,9.384229,7.074695,4.788620,4.959990,-4.759023,-9.835275,4.764943,-0.084159,4.151529,1.462880,-3.072695,1.280815,-6.763632,1.288237,7.470979,6.120907,0.265730,4.590363,9.678586,-1.378496,-3.671876,-0.947232,9.298537,9.308384,1.535952,-4.746599,8.033708,3.717783,7.436526,4.264537,-9.528697,-8.067548,0.270225,-8.487793,-4.616037,-3.178290,-8.553733,8.480744,-6.161462,-8.458410,6.323805,1.496849,-3.323091,-0.138042,5.030326,-9.036723,-5.558525,7.016531,5.804543,0.873216,-3.150320,-1.499816,-3.982078,8.815231,-4.282167,7.494475,-8.687877,9.172542,0.549384,6.738352,4.802293,0.152438,-4.981950,-1.805673,-1.353538,5.093252,7.881916,7.339626,4.024689,-3.595426,0.119701,7.073747,-5.264011,-5.923351,0.241143,2.746645,-8.380615,-0.091240,8.958638,-7.871396,-5.364117,3.682313,8.980509,-2.923636,0.175115,9.991701,-2.705977,-0.541367,2.247010,-2.080073,-8.940262,7.216663,-2.411908,3.434968,-1.448087,-1.756343,-1.274774,4.320301,-0.675808,-1.054927,-0.501380,-2.043734,0.181809,-3.986137,-6.880933,2.697035,-6.233509,0.394506,-5.549343,-3.268757,-6.833904,-0.095423,-4.701555,-9.250913,3.600143,-7.430719,-4.531962,-9.468802,-2.218497,-8.891177,4.061319,8.024795,1.374400,0.180459,-1.152801,-2.577317,-5.214720,8.055091,-9.962877,3.339148,-9.854197,-7.357692,7.014410,-7.760164,0.971768,-8.066531,-9.771741,-7.093261,-0.860461,-4.468543,0.641594,5.089274,2.728539,2.721720,-8.163187,8.031440,-4.276383,-6.091738,-7.751154,7.014881,1.090584,-6.699645,-8.099688,0.907069,-9.620075,2.694667,9.051486,7.054200,9.851797,-5.926670,-1.887936,-9.572227,6.665727,-8.760114,-8.180130,4.915989,2.437584,5.470335,-1.384817,-7.966729,-9.274936,3.615515,-8.743170,-4.868052,5.998717,4.397231,-8.496981,-5.548301,-3.630232,8.047380,3.366603,0.183044,6.387703,-8.052211,1.703256,-3.517658,-1.666903,5.253920,0.870954,-4.738618,1.725722,-9.838690,1.547413,9.940232,2.337437,-2.347547,-8.311755,7.443316,9.252562,0.339360,-3.218533,-7.327121,6.499561,0.760161,-3.635921,9.910926,2.618634,1.645827,6.166978,5.216261,-4.129308,7.525314,6.843868,-7.650817,-2.392166,5.431247,8.839377,8.854378,-6.978603,9.120931,-2.507445,-6.081022,-4.204788,-5.838492,-4.255113,-6.428735,-9.491466,9.171750,-1.975184,-2.568329,-8.487523,2.307066,2.781206,-3.018632,4.541556,-4.007391,1.523573,-1.442064,2.324344,8.564960,-3.518338,-0.170302,7.185373,-2.161283,2.021566,-2.219927,-3.721966,6.629353,-0.948684,0.837042,-0.183069,5.385204,-2.894340,3.326131,-7.415141,-8.623985,6.506556,6.241466,-0.135212,-3.099177,-5.850619,5.215181,4.483605,2.799591,5.642540,8.609463,-6.702363,8.313423,-1.844086,-0.774759,3.025397,6.322019,2.563194,6.631409,-2.724497,5.446001,-2.796617,-1.356270,-2.928962,8.759930,-6.856686,0.329654,0.214850,-0.845536,4.439130,-0.458580,5.313004,9.518431,5.541941,-2.476783,6.838336,-9.018096,9.079982,1.081919,-3.225462,1.204027,1.570355,-9.415136,1.513279,3.013206,4.530283,0.809995,8.171917,-4.974076,5.949568,9.521967,-1.886154,-0.358804,-4.596163,4.901324,-2.815704,8.922492,4.761190,-6.714531,-5.485048,-1.158030,0.783765,-1.097729,-9.220672,3.882509,-2.031038,-0.590544,0.658050,-1.645908,-5.373244,-6.896203,-9.358401,0.018011,1.840851,-2.902937,9.002493,-0.388478,-3.019880,9.819919,0.621978,-2.449463,5.274428,-5.620362,4.795105,-8.580895,9.557016,-6.091237,9.844231,1.922731,6.413493,-0.591502,-7.920413,2.656853,-8.305281,-2.722024,-2.834090,2.970533,8.590988,-3.157527,-0.607490,1.253369,5.322347,9.239784,6.844520,-9.503591,-2.719021,7.332737,2.196214,4.313875,8.499531,5.948420,-4.411749,-2.426918,-6.835429,-4.441618,9.072488,-1.952532,2.397698,8.643465,0.847166,6.838551,5.333701,-4.539750,0.809657,-5.101737,5.976971,-8.201905,-7.140117,-9.725533,3.714231,9.947659,-6.891535,-1.280249,2.683234,-6.008888,9.778703,-9.503751,-1.290652,4.131461,-7.961108,-0.421439,3.403571,3.264098,6.895404,-5.108974,-1.637288,-9.888720,-4.754627,-5.158928,-6.037373,-7.915010,-7.178213,-9.218131,0.297033,-1.386425,6.238162,-4.135792,-5.462533,-0.153037,6.696478,-6.354994,-6.072361,-2.061136,8.946541,-7.382909,4.939951,2.324817,4.501114,-0.541560,5.198783,-4.175701,9.236327,9.618914,-4.945152,-5.082563,9.635880,2.627166,2.765219,-4.758641,-3.344239,-6.978557,2.624786,9.246609,-8.598250,7.611222,6.715140,-4.352522,-7.878320,-3.076764,-6.092981,-4.149137,5.312792,3.114062,2.569196,-4.405443,3.567234,0.473788,-6.176197,6.403610,-9.051337,5.825187,5.660873,2.281697,5.565393,-1.886833,-9.787956,7.284185,0.317416,-2.304833,-8.006332,-3.117756,5.537079,-1.245459,4.160976,-4.170437,2.157062,9.127899,-2.939116,-5.730192,-1.156749,7.575651,-4.948777,-6.975821,7.722098,-1.139519,6.668947,0.998276,1.526256,0.894824,-9.925470,-4.316091,3.027305,-4.732382,-0.335424,6.892598,7.656394,4.742779,-6.817824,1.604911,-9.545103,3.378612,2.240591,5.491715,9.587564,6.336703,-8.888456,6.081605,3.529598,2.662256,-9.263096,-7.290673,1.810109,0.932073,7.967823,-2.606259,3.952970,-9.276106,-1.690787,0.683445,-6.588139,6.548895,-3.294357,-6.831068,-5.228717,-4.413917,-4.970480,9.257716,-8.589258,1.592536,1.574706,-0.791148,-3.863806,1.211854,-9.683411,-7.710361,2.533058,7.215339,-8.772412,4.328499,-3.740842,6.687608,-9.868884,-3.275551,-6.614199,8.628811,4.895304,-2.919192,-0.727541,1.401474,-5.492940,4.967512,5.242462,8.165560,-2.049283,5.027433,-8.296924,5.767600,2.785831,-0.032910,-3.200970,1.302131,1.345153,4.835896,-0.009537,-9.007094,-7.510682,-8.422741,-3.692027,2.900542,3.612613,7.448727,5.817445,-1.232521,4.429838,-3.333362,-8.130595,2.506813,0.389366,6.605861,4.625712,-1.070213,2.375672,-8.044555,3.942787,-9.891558,-0.908725,-4.717161,2.957717,-6.946259,6.856095,-1.142701,-5.381795,9.256364,-1.749120,2.966749,-5.188610,5.405103,9.738416,-3.152293,8.219470,0.586794,-8.174177,1.553538,-4.869423,-9.819485,3.457807,-7.054617,9.779573,6.900973,-9.822325,3.571642,4.699160,2.646806,-2.127296,7.854022,-2.304901,4.667883,-4.729540,-2.610496,-9.549263,1.764255,9.341671,-1.191833,0.634548,-3.043582,-1.816241,4.796349,-9.648982,-4.145126,-5.261442,-7.268909,-0.640564,3.608938,0.823041,-0.731268,9.843394,9.927763,0.145000,8.609524,3.848516,-8.988153,9.565940,6.185320,-4.410420,5.515536,5.498271,-1.059108,1.481088,1.465164,0.864507,3.594804,0.589346,-9.563699,-4.791671,5.000138,2.455101,3.606713,3.277577,9.553812,1.521929,-7.435861,-4.650714,-4.261830,5.634221,-0.118452,2.535500,3.873762,-5.452165,1.383436,6.039630,4.482118,3.201544,8.873244,7.463004,-7.246060,3.368091,-3.787616,6.556338,-6.633274,-5.094207,-1.823577,-6.301963,-8.070667,0.624306,4.231403,-4.879235,9.434122,9.841181,1.587551,5.474177,2.485838,-4.783668,8.577440,6.335046], dtype = "float64")#candidate|16152|(1456,)|const|float64
var_16153 = relay.var("var_16153", dtype = "uint32", shape = (1, 75))#candidate|16153|(1, 75)|var|uint32
var_16154 = relay.var("var_16154", dtype = "uint32", shape = ())#candidate|16154|()|var|uint32
call_16151 = relay.TupleGetItem(func_1748_call(relay.reshape(const_16152.astype('float64'), [13, 16, 7]), relay.reshape(var_16153.astype('uint32'), [75,]), relay.reshape(var_16154.astype('uint32'), []), ), 0)
call_16155 = relay.TupleGetItem(func_1753_call(relay.reshape(const_16152.astype('float64'), [13, 16, 7]), relay.reshape(var_16153.astype('uint32'), [75,]), relay.reshape(var_16154.astype('uint32'), []), ), 0)
output = relay.Tuple([call_16125,call_16151,const_16152,var_16153,var_16154,])
output2 = relay.Tuple([call_16126,call_16155,const_16152,var_16153,var_16154,])
func_16166 = relay.Function([var_16153,var_16154,], output)
mod['func_16166'] = func_16166
mod = relay.transform.InferType()(mod)
mutated_mod['func_16166'] = func_16166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16166_call = mutated_mod.get_global_var('func_16166')
var_16168 = relay.var("var_16168", dtype = "uint32", shape = (1, 75))#candidate|16168|(1, 75)|var|uint32
var_16169 = relay.var("var_16169", dtype = "uint32", shape = ())#candidate|16169|()|var|uint32
call_16167 = func_16166_call(var_16168,var_16169,)
output = call_16167
func_16170 = relay.Function([var_16168,var_16169,], output)
mutated_mod['func_16170'] = func_16170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12969_call = mod.get_global_var('func_12969')
func_12970_call = mutated_mod.get_global_var('func_12970')
call_16209 = relay.TupleGetItem(func_12969_call(), 2)
call_16210 = relay.TupleGetItem(func_12970_call(), 2)
output = call_16209
output2 = call_16210
func_16218 = relay.Function([], output)
mod['func_16218'] = func_16218
mod = relay.transform.InferType()(mod)
mutated_mod['func_16218'] = func_16218
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16218_call = mutated_mod.get_global_var('func_16218')
call_16219 = func_16218_call()
output = call_16219
func_16220 = relay.Function([], output)
mutated_mod['func_16220'] = func_16220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6997_call = mod.get_global_var('func_6997')
func_6999_call = mutated_mod.get_global_var('func_6999')
call_16227 = func_6997_call()
call_16228 = func_6997_call()
output = relay.Tuple([call_16227,])
output2 = relay.Tuple([call_16228,])
func_16244 = relay.Function([], output)
mod['func_16244'] = func_16244
mod = relay.transform.InferType()(mod)
output = func_16244()
func_16245 = relay.Function([], output)
mutated_mod['func_16245'] = func_16245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mod.get_global_var('func_4814')
func_4816_call = mutated_mod.get_global_var('func_4816')
call_16275 = relay.TupleGetItem(func_4814_call(), 0)
call_16276 = relay.TupleGetItem(func_4816_call(), 0)
output = relay.Tuple([call_16275,])
output2 = relay.Tuple([call_16276,])
func_16288 = relay.Function([], output)
mod['func_16288'] = func_16288
mod = relay.transform.InferType()(mod)
mutated_mod['func_16288'] = func_16288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16288_call = mutated_mod.get_global_var('func_16288')
call_16289 = func_16288_call()
output = call_16289
func_16290 = relay.Function([], output)
mutated_mod['func_16290'] = func_16290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_16353 = relay.TupleGetItem(func_5203_call(), 0)
call_16354 = relay.TupleGetItem(func_5205_call(), 0)
output = call_16353
output2 = call_16354
func_16360 = relay.Function([], output)
mod['func_16360'] = func_16360
mod = relay.transform.InferType()(mod)
output = func_16360()
func_16361 = relay.Function([], output)
mutated_mod['func_16361'] = func_16361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11147_call = mod.get_global_var('func_11147')
func_11149_call = mutated_mod.get_global_var('func_11149')
call_16405 = relay.TupleGetItem(func_11147_call(), 0)
call_16406 = relay.TupleGetItem(func_11149_call(), 0)
func_7852_call = mod.get_global_var('func_7852')
func_7854_call = mutated_mod.get_global_var('func_7854')
call_16407 = relay.TupleGetItem(func_7852_call(), 0)
call_16408 = relay.TupleGetItem(func_7854_call(), 0)
func_10787_call = mod.get_global_var('func_10787')
func_10788_call = mutated_mod.get_global_var('func_10788')
call_16409 = func_10787_call()
call_16410 = func_10787_call()
output = relay.Tuple([call_16405,call_16407,call_16409,])
output2 = relay.Tuple([call_16406,call_16408,call_16410,])
func_16413 = relay.Function([], output)
mod['func_16413'] = func_16413
mod = relay.transform.InferType()(mod)
output = func_16413()
func_16414 = relay.Function([], output)
mutated_mod['func_16414'] = func_16414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4814_call = mod.get_global_var('func_4814')
func_4816_call = mutated_mod.get_global_var('func_4816')
call_16464 = relay.TupleGetItem(func_4814_call(), 0)
call_16465 = relay.TupleGetItem(func_4816_call(), 0)
output = relay.Tuple([call_16464,])
output2 = relay.Tuple([call_16465,])
func_16481 = relay.Function([], output)
mod['func_16481'] = func_16481
mod = relay.transform.InferType()(mod)
mutated_mod['func_16481'] = func_16481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16481_call = mutated_mod.get_global_var('func_16481')
call_16482 = func_16481_call()
output = call_16482
func_16483 = relay.Function([], output)
mutated_mod['func_16483'] = func_16483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8226_call = mod.get_global_var('func_8226')
func_8228_call = mutated_mod.get_global_var('func_8228')
call_16517 = relay.TupleGetItem(func_8226_call(), 0)
call_16518 = relay.TupleGetItem(func_8228_call(), 0)
output = call_16517
output2 = call_16518
func_16534 = relay.Function([], output)
mod['func_16534'] = func_16534
mod = relay.transform.InferType()(mod)
mutated_mod['func_16534'] = func_16534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16534_call = mutated_mod.get_global_var('func_16534')
call_16535 = func_16534_call()
output = call_16535
func_16536 = relay.Function([], output)
mutated_mod['func_16536'] = func_16536
mutated_mod = relay.transform.InferType()(mutated_mod)
const_16568 = relay.const([[[4.183153,-3.148457,9.525497,1.137978,-2.265938,-1.326601,4.928026,1.968162,3.972761,-9.307839,-3.914634,-4.344160,-8.157544,0.889736],[5.792724,-8.736633,-7.217413,-2.076984,-3.007758,-1.995917,-1.986207,6.979188,-7.038515,6.512577,2.725073,2.976567,-0.244114,-8.585488],[2.596569,-8.207195,-5.348967,6.890059,5.514342,-7.075698,0.024946,0.237169,6.840086,5.189184,9.558664,-0.510452,9.018485,-1.414174],[7.944340,-7.808573,-8.016914,6.675169,8.586399,1.698334,-9.246678,-6.431344,-4.470734,6.529250,-3.187211,-6.840628,0.518796,-9.211032],[-5.466490,6.125308,1.263868,-0.062368,-6.844365,3.754535,-9.992656,-5.182067,-8.676945,0.451975,-4.213918,1.901247,2.041005,-7.714740],[-3.037363,4.295329,5.493874,-0.246553,-5.612502,-5.991010,-2.732157,6.328804,-0.907147,-0.187950,-7.011828,-0.750897,-6.781025,-0.785902],[6.024686,4.858041,4.447503,-1.819658,7.989865,-7.173531,-8.872353,-1.964689,-7.555886,5.615367,6.145695,5.781805,1.611194,0.911845],[6.126317,-0.683299,-3.166521,-4.488349,-1.721121,9.926747,8.811250,-4.450565,-5.689229,3.587961,-3.085615,-0.705647,-6.032313,4.396681],[3.773892,5.832046,-2.740898,6.660479,8.498989,0.342607,-1.203577,1.719833,-5.172352,3.694449,-3.609214,2.335690,-0.692862,0.992321],[5.157045,-1.344200,8.810248,-8.061813,3.806559,-5.810824,3.142863,0.637573,-1.155713,-6.537200,-3.794867,-6.495216,-8.432620,9.096045],[6.843620,9.747077,3.174028,7.186017,5.767841,0.453001,5.201889,-8.724952,2.491265,-4.300486,-1.063177,-9.980838,6.899264,-9.992769],[-4.691661,-1.737160,-4.509535,-9.963410,0.805824,-6.984041,2.963096,-4.005853,8.562329,-3.402586,-5.908729,3.292283,8.155361,0.077285],[-3.246295,-0.262791,0.846720,-3.694789,-9.059537,2.346544,-5.478878,-4.306627,2.230153,-7.311981,0.166031,0.589422,2.673655,9.418081],[-7.498547,1.734491,-5.743293,6.214734,-4.714814,6.355846,2.135239,8.725599,-8.989925,7.013665,-8.662773,-3.369491,-6.356442,9.864660]],[[-2.530760,-3.109635,0.764463,7.378470,4.497718,3.639998,-9.530869,-7.302962,7.756513,7.613357,-7.008802,-1.409880,-0.082223,-7.978541],[-1.181943,4.102663,-0.512023,-9.981704,8.227672,4.662728,-0.044405,4.795887,5.259269,-3.535009,1.012926,-1.069331,8.561239,-1.093587],[-5.066823,-1.026334,-3.410949,3.078432,-9.224463,-4.846081,-4.255670,-6.718392,-0.506351,4.647688,-3.550775,-3.136419,-6.234999,1.039667],[5.059987,2.101831,-9.691767,1.304425,6.980630,-0.704296,-3.907737,-7.426549,-2.217398,3.470554,-4.766866,2.345189,9.110127,-4.920981],[-8.975023,1.286007,2.625540,1.084795,-1.629429,-3.912086,-4.081976,7.289646,6.862383,7.476824,1.325157,-5.651377,4.867551,-5.562017],[2.093176,-8.556502,-5.141277,-5.586144,1.810662,7.167319,-8.246661,3.172326,-3.530111,6.897211,-8.276117,-1.890935,0.306410,8.968669],[-5.871896,0.840082,-7.461480,9.237234,1.014304,-8.350931,-6.408342,2.604396,5.856285,3.172238,5.541219,5.598711,2.728858,6.778939],[-6.953072,3.021237,-9.782256,9.730421,2.140461,3.953202,-8.143547,1.289812,-0.104355,4.118932,4.741026,6.033724,4.783352,2.701795],[-5.584225,7.310586,3.528901,8.236268,-8.272183,8.335715,-3.846768,-4.203093,-1.829989,2.691072,-0.403572,6.150600,4.091160,6.063431],[0.178964,2.767094,6.490738,3.572687,2.759794,4.139300,0.617600,2.747205,9.570336,-5.590627,9.954114,-9.492700,-2.543479,-4.579148],[9.469953,-1.243533,-3.795519,-9.024674,-1.329662,-1.850104,8.975284,5.075250,-7.253042,-9.561195,4.285651,-8.909570,-8.939588,-0.273587],[-2.796727,-1.763093,-0.945131,-2.361024,-8.319011,8.966658,-9.105454,-9.830790,6.326958,-4.852243,6.421584,3.167960,9.098155,7.521095],[6.280032,-5.797235,-2.845183,2.394869,5.162236,4.289726,-7.343451,5.882897,0.009731,-2.813254,8.407954,-0.673524,7.657010,6.803312],[9.775710,-4.760894,2.827485,-7.782937,4.325520,-3.386861,-4.851514,-8.987253,-0.107331,8.422713,-4.268141,-9.473634,8.826168,-1.608903]]], dtype = "float32")#candidate|16568|(2, 14, 14)|const|float32
var_16569 = relay.var("var_16569", dtype = "float32", shape = (2, 14, 14))#candidate|16569|(2, 14, 14)|var|float32
bop_16570 = relay.divide(const_16568.astype('float32'), relay.reshape(var_16569.astype('float32'), relay.shape_of(const_16568))) # shape=(2, 14, 14)
func_15759_call = mod.get_global_var('func_15759')
func_15762_call = mutated_mod.get_global_var('func_15762')
const_16610 = relay.const([-9.183381,3.025522,-4.145484,4.825669,-7.907586,5.170474,-7.981301,3.841952,-0.536424,-9.806352,4.235275,8.981194,-5.687086,-0.185559,-9.852604,-9.451964,-5.138627,3.067719,-3.428253,-7.704980,7.890256,8.571831,-8.793276,-4.474747,-0.926872,-6.910236,5.552219,-2.953456,7.847214,3.656458,-2.178112,-2.273815,7.728311,1.295082,-8.101744,-0.540742,0.749202,-9.136891,-9.013603,9.290787,9.501320,-3.127870,1.027862,1.195618,-2.876056,-9.155198,-2.698853,8.499559,5.356911,5.090352,9.702546,0.590034,3.217383,-3.036909,2.177844,-9.522747,8.017828,7.894097,1.085846,-7.204858,9.843711,-6.754029,7.945429,1.759119,9.030519,4.237164,-8.285696,7.309506,-4.312652,-8.000463,2.944326,-5.626697,8.953807,-6.623536,-1.338411,-1.094408,4.343084,0.563693,7.768968,1.834093,1.915932,4.253835,-1.170097,3.705379,-9.260445,-8.520252,-5.574001,-5.862315,-7.873796,-3.149651,9.446572,-8.236159,-0.715059,-1.685204,-1.540889,-2.951095,-2.814158,8.778599,-7.691501,5.439976,-3.326543,7.641053,-3.792392,4.730696,-6.077944,-2.564697,-3.266420,-5.773458,-3.612820,-8.753345,5.985586,3.566789,-0.796125,-3.365470,7.864041,2.549485,4.771855,1.198384,1.447669,-4.841603], dtype = "float32")#candidate|16610|(120,)|const|float32
var_16611 = relay.var("var_16611", dtype = "float32", shape = (400,))#candidate|16611|(400,)|var|float32
call_16609 = relay.TupleGetItem(func_15759_call(relay.reshape(const_16610.astype('float32'), [5, 8, 3]), relay.reshape(var_16611.astype('float32'), [400, 1]), ), 3)
call_16612 = relay.TupleGetItem(func_15762_call(relay.reshape(const_16610.astype('float32'), [5, 8, 3]), relay.reshape(var_16611.astype('float32'), [400, 1]), ), 3)
output = relay.Tuple([bop_16570,call_16609,const_16610,var_16611,])
output2 = relay.Tuple([bop_16570,call_16612,const_16610,var_16611,])
func_16618 = relay.Function([var_16569,var_16611,], output)
mod['func_16618'] = func_16618
mod = relay.transform.InferType()(mod)
mutated_mod['func_16618'] = func_16618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16618_call = mutated_mod.get_global_var('func_16618')
var_16620 = relay.var("var_16620", dtype = "float32", shape = (2, 14, 14))#candidate|16620|(2, 14, 14)|var|float32
var_16621 = relay.var("var_16621", dtype = "float32", shape = (400,))#candidate|16621|(400,)|var|float32
call_16619 = func_16618_call(var_16620,var_16621,)
output = call_16619
func_16622 = relay.Function([var_16620,var_16621,], output)
mutated_mod['func_16622'] = func_16622
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16624 = relay.var("var_16624", dtype = "float64", shape = (1, 13, 12))#candidate|16624|(1, 13, 12)|var|float64
uop_16625 = relay.sqrt(var_16624.astype('float64')) # shape=(1, 13, 12)
output = uop_16625
output2 = uop_16625
func_16635 = relay.Function([var_16624,], output)
mod['func_16635'] = func_16635
mod = relay.transform.InferType()(mod)
var_16636 = relay.var("var_16636", dtype = "float64", shape = (1, 13, 12))#candidate|16636|(1, 13, 12)|var|float64
output = func_16635(var_16636)
func_16637 = relay.Function([var_16636], output)
mutated_mod['func_16637'] = func_16637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9385_call = mod.get_global_var('func_9385')
func_9386_call = mutated_mod.get_global_var('func_9386')
call_16642 = func_9385_call()
call_16643 = func_9385_call()
func_10942_call = mod.get_global_var('func_10942')
func_10945_call = mutated_mod.get_global_var('func_10945')
var_16646 = relay.var("var_16646", dtype = "uint32", shape = (4,))#candidate|16646|(4,)|var|uint32
call_16645 = relay.TupleGetItem(func_10942_call(relay.reshape(var_16646.astype('uint32'), [2, 2])), 4)
call_16647 = relay.TupleGetItem(func_10945_call(relay.reshape(var_16646.astype('uint32'), [2, 2])), 4)
func_9612_call = mod.get_global_var('func_9612')
func_9613_call = mutated_mod.get_global_var('func_9613')
call_16648 = relay.TupleGetItem(func_9612_call(), 2)
call_16649 = relay.TupleGetItem(func_9613_call(), 2)
output = relay.Tuple([call_16642,call_16645,var_16646,call_16648,])
output2 = relay.Tuple([call_16643,call_16647,var_16646,call_16649,])
func_16658 = relay.Function([var_16646,], output)
mod['func_16658'] = func_16658
mod = relay.transform.InferType()(mod)
mutated_mod['func_16658'] = func_16658
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16659 = relay.var("var_16659", dtype = "uint32", shape = (4,))#candidate|16659|(4,)|var|uint32
func_16658_call = mutated_mod.get_global_var('func_16658')
call_16660 = func_16658_call(var_16659)
output = call_16660
func_16661 = relay.Function([var_16659], output)
mutated_mod['func_16661'] = func_16661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10432_call = mod.get_global_var('func_10432')
func_10433_call = mutated_mod.get_global_var('func_10433')
call_16680 = relay.TupleGetItem(func_10432_call(), 1)
call_16681 = relay.TupleGetItem(func_10433_call(), 1)
output = relay.Tuple([call_16680,])
output2 = relay.Tuple([call_16681,])
func_16682 = relay.Function([], output)
mod['func_16682'] = func_16682
mod = relay.transform.InferType()(mod)
output = func_16682()
func_16683 = relay.Function([], output)
mutated_mod['func_16683'] = func_16683
mutated_mod = relay.transform.InferType()(mutated_mod)
var_16706 = relay.var("var_16706", dtype = "float32", shape = (15, 4, 3))#candidate|16706|(15, 4, 3)|var|float32
uop_16707 = relay.cos(var_16706.astype('float32')) # shape=(15, 4, 3)
output = uop_16707
output2 = uop_16707
func_16709 = relay.Function([var_16706,], output)
mod['func_16709'] = func_16709
mod = relay.transform.InferType()(mod)
var_16710 = relay.var("var_16710", dtype = "float32", shape = (15, 4, 3))#candidate|16710|(15, 4, 3)|var|float32
output = func_16709(var_16710)
func_16711 = relay.Function([var_16710], output)
mutated_mod['func_16711'] = func_16711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10094_call = mod.get_global_var('func_10094')
func_10096_call = mutated_mod.get_global_var('func_10096')
call_16748 = relay.TupleGetItem(func_10094_call(), 1)
call_16749 = relay.TupleGetItem(func_10096_call(), 1)
func_8417_call = mod.get_global_var('func_8417')
func_8420_call = mutated_mod.get_global_var('func_8420')
const_16778 = relay.const([-3.093284,-8.134058,-1.134022,1.669734,0.732061,7.398115,2.770855,0.343967,2.789439,5.885795,-3.176523,5.134502,9.490407,2.880048,2.852959,7.739248,1.503703,4.480777,4.530417,7.286650,-3.076790,-5.675223,-3.882593,-4.347968,0.440021,2.882044,-8.964621,6.257101,0.102139,-7.345029,-0.869390,-4.767055,-0.730765,2.759419,-5.877578,-3.034714,7.634756,6.868304,-1.114163,3.755293,4.719794,4.503405,8.328798,0.835937,9.275760,5.082752,6.322509,-2.185123,6.143616,8.744993,-4.990264,-8.398321,-0.867859,2.507316,5.556695,0.441384,-2.181872,-5.263903,9.787430,-8.739755,-4.192231,-1.629261,-1.863666,4.731662,-4.644824,4.546524,-9.576664,-5.918549,0.469738,7.680936,1.492002,1.212687,1.902578,9.135520,-8.206634,5.645179,-3.541326,-3.209847,-6.854095,-2.157285,6.204539,-3.161467,-4.447224,-4.070539,-7.442078,-1.217773,-8.102895,4.608520,-6.604186,-3.367733,8.752103,2.567976,0.470879,-7.099730,7.321653,-1.739621,-3.077909,-9.711845,-4.809946,1.055787,-0.455638,-8.814960,4.183609,-0.007403,-3.731627,-4.987434,-3.215089,6.981645,-0.342411,-2.596947,6.068708,-1.205740,5.611542,-9.914101,4.894915,-8.568715,8.655394,1.944440,1.120411,-6.137782], dtype = "float64")#candidate|16778|(120,)|const|float64
call_16777 = relay.TupleGetItem(func_8417_call(relay.reshape(const_16778.astype('float64'), [120,])), 0)
call_16779 = relay.TupleGetItem(func_8420_call(relay.reshape(const_16778.astype('float64'), [120,])), 0)
output = relay.Tuple([call_16748,call_16777,const_16778,])
output2 = relay.Tuple([call_16749,call_16779,const_16778,])
func_16783 = relay.Function([], output)
mod['func_16783'] = func_16783
mod = relay.transform.InferType()(mod)
mutated_mod['func_16783'] = func_16783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16783_call = mutated_mod.get_global_var('func_16783')
call_16784 = func_16783_call()
output = call_16784
func_16785 = relay.Function([], output)
mutated_mod['func_16785'] = func_16785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7157_call = mod.get_global_var('func_7157')
func_7158_call = mutated_mod.get_global_var('func_7158')
call_16812 = relay.TupleGetItem(func_7157_call(), 0)
call_16813 = relay.TupleGetItem(func_7158_call(), 0)
output = call_16812
output2 = call_16813
func_16823 = relay.Function([], output)
mod['func_16823'] = func_16823
mod = relay.transform.InferType()(mod)
mutated_mod['func_16823'] = func_16823
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16823_call = mutated_mod.get_global_var('func_16823')
call_16824 = func_16823_call()
output = call_16824
func_16825 = relay.Function([], output)
mutated_mod['func_16825'] = func_16825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9612_call = mod.get_global_var('func_9612')
func_9613_call = mutated_mod.get_global_var('func_9613')
call_16828 = relay.TupleGetItem(func_9612_call(), 0)
call_16829 = relay.TupleGetItem(func_9613_call(), 0)
func_14769_call = mod.get_global_var('func_14769')
func_14776_call = mutated_mod.get_global_var('func_14776')
var_16858 = relay.var("var_16858", dtype = "int64", shape = (480,))#candidate|16858|(480,)|var|int64
var_16859 = relay.var("var_16859", dtype = "uint32", shape = ())#candidate|16859|()|var|uint32
var_16860 = relay.var("var_16860", dtype = "int32", shape = (4, 264))#candidate|16860|(4, 264)|var|int32
var_16861 = relay.var("var_16861", dtype = "float32", shape = (364,))#candidate|16861|(364,)|var|float32
const_16862 = relay.const([-0.859057,-8.603811,-4.583769,-1.378788,1.501797,-1.242453,-4.148352,-7.840908,-1.353899,5.674216,2.905039,2.629259,3.024896,-1.008183,4.345434,0.097937,1.432386,6.457047,0.531502,7.489237,-5.138040,4.549363,2.677818,8.685424,-6.188444,-3.786136,3.392277,-9.665852,9.962754,7.563304,-1.211934,1.484346,-9.303182,3.176331,-8.165424,2.050633,-4.385539,4.700053,-2.309041,-6.218193,5.471043,3.049174,-7.874511,-4.844430,-8.365257,-9.164508,-1.738704,-2.358346,-2.253339,-6.578921,8.432938,5.869106,-5.700071,5.597394,1.923927,-1.038945,-6.477459,2.055041,3.259595,6.824433,-1.222860,-2.930914,8.614831,9.843483,-6.629873,-4.615507,2.740989,6.425142,-1.517167,1.680520,-4.627243,-7.667162,9.084951,5.372589,8.375884,-1.886736,-4.485033,2.919866,1.864226,3.500058,-3.018173,1.106475,6.272548,-3.783507,9.822334,8.084101,0.945316,4.415348,-6.580935,4.147227,2.297953,5.690466,-5.746080,3.337511,8.603807,4.050165,-8.924742,-5.982998,7.246018,6.716157,-3.925570,0.683784,-3.822550,-3.911553,0.799464,4.977830,4.105938,7.058808,4.017827,4.871617,9.469002,-2.703426,-3.959743,-8.515239,6.152190,-9.465862,-0.637047,4.677173,-1.423199,1.878552,9.061876,-7.827131,6.215519,-9.431672,-2.842285,-7.463391,-2.539988,0.029557,0.288040,8.741577,1.192073,-4.994630,4.473917,3.607813,2.764993,5.867952,1.644074,5.051792,9.367692,7.682651,6.789593,-2.618724,-6.645620,-0.093423,6.579445,1.165318,-7.961948,-7.925660,5.783489,5.326305,5.764981,-0.681911,2.366213,0.797376,1.236275,-3.044464,-1.003235,3.419693,5.707732,-7.700758,6.927286,4.500341,4.788673,3.038485,1.785899,3.561708,1.323003,8.817203,7.684347,-6.128774,8.986804,-7.165868,9.777094,5.414645,9.148530,0.706455,9.137625,-6.668413,-3.539501,2.943861,8.290863,-7.252925,-1.881097,2.212409,4.829588,2.505991,-5.573245,-3.162322,0.302950,-1.168900,-1.788145,7.718270,8.118104,-6.665868,5.396504,3.207075,1.199824,3.835267,-7.019414,6.792463,-0.542691,-1.591153,-1.482572,-4.487603,-5.195727,8.991854,-2.643934,-7.307552,-3.050203,-0.969469,2.173204,-8.656256,8.565441,-5.057521,-4.272121,9.961930,-6.049027,-0.084772,7.152007,-0.237265,4.816212,-1.491601,-6.555359,8.285309,9.268435,-1.140358,-6.559302,6.225306,3.400823,8.356656,-7.491435,-2.795320,-7.678355,7.233952,-2.703107,-3.467668,0.167046,0.365855,6.291944,0.528414,-8.824338,0.988759,-8.636502,2.082713,6.497829,-4.384264,8.035577,-4.981719,4.595191,5.896280,-7.278054,4.461899,-0.090292,0.166530,-1.287559,6.120911,7.614446,4.205904,8.497832,3.421133,5.849818,-7.873714,-8.937497,-9.455319,8.661807,4.756472,0.670694,5.349938,-4.842058,-8.745816,9.116773,1.145829,-7.239152,6.585189,9.245020,-3.825882,-5.627655,-5.103434,-1.728973,-2.937284,-6.126558,3.532274,-4.843327,-9.152640,0.543000,4.451458,-8.550318,1.091998,1.655291,-3.976641,7.114992,4.621962,-7.620679,8.009889,9.363157,-9.346554,3.518962,9.881354,-6.065656,-6.170243,-8.506828,8.388348,7.179416,-4.157320,9.139321,6.527112,4.190274,-5.710522,-3.786450,-7.521210,2.770087,-0.720277,-2.367144,-2.317228,5.424397,7.718823,6.718264,-0.753421,8.281065,2.027657,0.963207,-2.795457,-7.731736,-3.939625,-8.671125,-1.234269,9.863628,-9.686391,-3.352051,5.800736,-5.591053,-2.157716,3.931588,-7.681291,7.640560,9.421581,-2.905391,5.058495,-9.372126,-2.017951,0.744840,-5.699029,0.567412,-2.282356,6.400716,0.925959,-6.675430,1.638164,-8.570526,4.276448,-0.299473,-4.373033,-0.455875,0.630170,-1.884007,4.287126,-0.403778,-1.561660,-6.247904,4.799857,-1.122843,9.640250,-3.303939,-7.590803,-2.830491,-6.873705,-1.733588,-6.354923,7.086449,1.561899,0.046687,7.191474,-7.008726,9.053174,-6.790157,9.364172,1.733732,-2.840053,6.835074,-9.951371,-4.159540,-5.069351,5.961715,5.648051,-4.482412,-2.630910,7.699693,9.699604,-9.891425,-2.804524,-0.043241,3.331144,5.385250,2.310222,2.553602,-1.444557,3.353894,-0.732472,3.415334,9.947225,9.088699,4.456212,9.647437,-1.749620,9.052443,-3.640639,-5.365519,0.084478,1.627611,2.479176,-4.852729,-1.404042,-0.542046,9.275115,-3.596243,-2.653556,-6.934869,-8.183037,-5.356807,9.780731,-9.729952,1.702586,-9.377423,-5.728841,-4.602134,-8.900453,3.323697,-5.616813,4.944399,-4.107874,-3.257132,6.380984,-4.285475,-2.880412,6.446321,8.007629,4.543242,-8.003380,7.890516,-9.981333,-0.423392,9.755727,8.161753,-0.728683,8.174052,6.568807,2.307892,-7.154723,-9.642384,-6.944188,5.187477,8.663781,9.530775,-1.628461,-2.282194,-2.074482,8.200642,0.191380,8.185629,1.955802,-5.653706,-2.363266,-1.171513,8.237801,7.481841,-5.837173,1.235722,3.399266,6.826475,-1.121091,-4.088812,3.602785,-7.902835,9.636606,-9.514322,-1.780461,5.469864,-6.823275,3.329702,-9.641456,0.659515,8.443536,3.874280,8.281385,-9.647725,-6.354476,-1.609529,-1.569107,-9.240146,-1.654760,5.442722,5.265744,1.413940,-9.746799,-4.985858,1.034225,7.230263,-8.119292,-8.391169,0.601429,0.597228,8.445552,5.368368,-3.939841,0.390883,-9.826368,3.669485,2.564589,6.131755,-7.084132,7.666650,-2.012833,-3.890034,2.867092,-6.465866,-7.242712,-6.645906,-3.941755,1.896179,-6.646765,7.240013,9.103057,-8.039599,-4.595543,-7.654731,6.492725,-1.452215,-7.654068,5.985612,0.067728,2.204935,3.543372,-8.229329,5.030133,3.612671,-9.196267,3.168286,7.428824,7.849149,8.804574,-5.317863,6.363438,-7.752601,-9.062772,5.078302,-9.800605,3.781030,-6.992920,4.083688,0.658732,3.774136,7.837652,-1.293687,0.289415,-1.839215,7.623287,2.574291,-2.838007,2.476325,2.357242,-3.628729,2.656761,-0.231035,5.328180,4.994864,-3.019287,1.796894,9.497144,-0.631514,2.594198,-1.600399,-7.837822,1.916425,2.395212,2.152974,6.694509,-4.451738,9.178856,-2.642274,-8.911545,0.188145,0.913849,1.190386,-0.319049,9.731522,-1.581588,9.392672,9.892009,3.114286,4.556596,-8.401213,5.291300,9.520923,8.805398,9.117434,1.538156,-4.442385,5.850165,-9.011708,4.845395,8.027400,8.657793,-1.154840,7.691232,6.835762,-9.059221,0.100170,0.414099,-6.349909,4.387257,-3.914573,1.432485,7.617863,-9.326927,-2.585354,7.357367,-2.082668,-9.417277,1.571256,-2.557392,-1.188661,-0.080502,-0.043801,-2.086047,-0.689740,2.775085,5.408864,6.764893,9.610942,-8.751941,-7.992761,-2.917283,-3.079596,7.304922,-3.347982,-4.209997,3.323834,6.188021,-0.213052,-7.283336,1.434048,-9.560262,-5.961202,5.480312,9.622875,-1.956486,7.547242,-8.977501,0.222115,5.208200,-5.527224,2.021931,3.437418,9.149505,-2.998288,-9.343388,2.378181,-5.413583,0.336090,-3.092319,6.143762,-0.398039,9.137198,-4.110490,-1.654246,-1.012857,-8.593456,-8.287689,-6.939466,3.189665,-4.324187,-3.823640,-4.778909,1.292392,-6.655041,5.911860,-4.401868,-0.881967,-6.547433,6.896749,3.723775,9.384504,6.211452,7.002053,-7.706532,-4.961099,-2.837448,-4.248008,-7.096109,-4.852095,9.230018,-1.397962,6.504341,9.291537,-7.580026,2.438007,6.768704,7.614109,-8.585024,-5.047111,8.865914,4.859941,-7.971705,5.935171,-9.863436,5.194821,6.115435,4.175007,3.221749,-8.405198,8.665749,1.784649,6.734847,1.679771,6.295264,-4.385324,0.101008,-6.862585,2.495929,-9.378649,-4.958383,-8.803377,1.310723,-6.043495,-1.672448,-1.666741,-5.755243,-9.372090,-8.669537,-6.598298,-1.668393,4.633395,-9.564283,0.697029,7.262580,0.647050,3.723826,5.393113,-1.330080,0.447179,-7.341082,-5.323082,7.613398,-6.317216,5.505122,5.340931,3.998565,4.984851,4.797753,-2.765806,-5.570374,-5.525022,3.901106,-6.660099,9.847811,-7.083898,-6.847472,0.186333,-1.262752,2.726989,-0.373753,8.487720,0.476008,0.593482,5.906723,1.899103,-5.482946,1.610787,2.660990,9.699422,-1.842589,8.279701,-7.803238,-1.203877,-6.425818,-2.376397,5.080940,9.551618,-8.491309,4.454413,-5.516439,3.176619,-5.139380,-4.506928,1.205938,-4.145332,0.891537,-5.484677,-9.762346,-4.996110,-2.905524,8.375918,-8.730828,0.138904,-1.500154,-4.723067,1.368649,0.731627,7.738932,-8.487861,3.409801,-2.987253,-3.837914,-3.924459,0.921171,0.986418,-9.136223,0.248979,3.783220,1.183115,5.595968,-1.915134,-6.433067,-3.515094,9.908088,-3.369701,-9.111890,-2.657406,9.838270,0.493837,6.446186,-8.204967,-0.238139,5.360267,-6.049878,2.488855,-9.701788,5.629515,2.336428,-2.095386,-6.620687,6.960290,9.567603,6.118702,-3.652594,-3.856689,2.043594,9.258384,-4.812334,-8.544014,-9.249979,7.973313,3.833032,3.699072,-0.788377,-3.955812,-2.515038,5.774941,6.181094,-2.832649,-6.194703,9.087066,2.007344,1.284518,1.683434,1.338171,7.568222,6.703704,4.440258,0.315628,-9.420441,-8.933407,2.694693,4.268926,-5.434718,-1.743578,-5.006430,-3.702960,4.999810,8.563185,4.613746,-7.083526,4.622774,-6.848619,-9.451585,7.975552,5.807472,5.867450,1.978627,5.946753,-1.713324,-0.630135,9.108327,-4.481554,-7.453321,-2.836216,-6.454841,-9.886574,-8.616849,-7.489736,-9.829270,5.623850,6.173910,-2.384816,9.864416,-1.425852,-0.693412,-2.361952,-4.070750,-2.827870,5.335992,-5.115868,2.894759,6.840195,3.056490,-5.507317,7.256741,5.179707,-3.516956,-7.086766,1.376579,0.974151,2.969506,-9.420699,-6.205264,0.736121,8.929080,-9.684720,-3.039937,-3.792737,3.606627,-3.088632,-7.461753,-4.905675,5.257872,1.399741,7.794636,-0.562579,-2.385343,-5.197738,5.350906,-5.830185,-2.058000,9.676669,5.660450,-4.046496,-9.690602,2.558776,7.003434,5.657750,-6.531629,9.341174,6.725663,8.770583,-2.556040,6.211154,7.406158,-6.639774,-3.535759,-5.209406,6.783241,-0.312039,8.714235,0.514502,0.030410,-3.055796,2.805602,-8.357338,1.186668,-2.713268,6.987973,-7.685594,-6.948987,-4.691336,-3.475346,-2.422932,-2.759446,-6.994757,-5.740492,-6.958224,-4.996225,-4.251534,-9.490748,6.534218,-1.462190,-6.541893,6.159260,-3.652545,6.646771,-7.339375,6.329090,-8.577485,5.689111,-6.801268,-0.886012,-2.466858,1.346564,-6.749070,9.404246,4.146119,1.022804,7.101739,-3.972548,-8.856994,2.112621,-1.414019,1.827050,-0.008301,4.668723,7.734717,4.146133,-9.029464,-2.155623,-1.574749,-2.473401,6.654591,2.414387,-1.119829,-7.870121,-9.841192,2.321734,-2.607194,7.669075,-2.838362,8.496417,-5.196392,0.912366,3.402545,7.907694,3.963889,-1.891141,7.861366,1.897593,0.677200,2.297279,1.324312,-2.354609,3.365688,-1.364074,-9.445521,7.618896,-5.013404,-9.218959,-3.286283,-4.872478,9.782554,-7.287729,-6.915130,8.473361,3.891461,7.790772,7.999707,8.947063,4.448520,-2.159794,6.235501,-3.456126,-5.661877,-4.869140,-0.205416,-7.820717,8.186113,3.602882,3.554536,3.892235,4.371574,0.150002,2.993400,3.907604,7.302847,-0.329224,-7.464486,-6.798864,9.385438,4.069666,2.950055,-9.307293,0.348348,9.562504,-4.299187,3.609486,7.104027,-3.348485,8.481174,-9.535688,-8.298758,-7.809034,6.944180,4.113793,7.613258,2.645629,5.035545,1.831382,5.443490,7.706889,7.989998,1.424606,6.910080,5.447894,2.852843,7.379606,1.227337,-2.924683,5.587774,7.459694,0.808180,3.960268,-0.872397,6.144484,4.074523,8.803757,1.218554,-6.857839,5.322865,-7.290203,3.873214,-6.127187,6.682609,8.283660,-7.470481,1.565537,8.707773,-3.261279,4.945450,8.728388,-5.505901,6.050850,2.806732,9.283261,-2.085411,-0.995091,1.416550,-5.032128,0.746075,5.765544,-8.173395,1.988190,-8.144941,-8.521995,8.089501,-3.089698,-2.779351,-6.221146,1.406922,-3.913984,5.509601,5.416056,8.098816,6.203919,-3.739128,9.407241,7.994975,-2.979701,-2.408875,2.263085,5.620234,-2.766505,7.469150,3.482190,-1.015161,-8.243554,-0.220125,-5.153699,7.887435,0.228341,0.744686,2.974196,9.958092,-7.994313,-6.898108,-1.113353,3.098465,6.110337,8.356860,-1.805072,1.033057,4.258533,-3.676834,0.799135,5.794401,3.970285,0.240024,2.327957,5.006265,7.265570,1.843699,3.199348,-2.278066,8.919717,1.937714,1.402457,4.489694,0.365191,-9.118844,7.779210,9.524575,-0.455409,9.717887,2.251854,8.695217,-3.095689,-0.873488,-1.081593,4.261281,-2.356592,5.815487,8.272891,-3.293941,-5.353659,9.149493,-3.493648,9.999056,-8.184536,-5.506583,3.298280,-3.869229,-5.890360,8.328004,1.774402,0.400523,6.641491,2.884841,3.793310,4.077627,-1.455672,1.633915,1.602294,-0.355904,-9.140878,-9.462498,-9.969174,9.132855,9.307974,2.306210,0.934530,0.138789,9.642169,5.284930,-6.494668,7.155230,-6.830133,-8.359665,8.723197,8.506414,1.000238,9.586411,-4.059991,6.992936,0.638781,-0.039489,4.650630,6.490168,-1.044408,5.184043,-7.476947,7.843714,6.164763,-6.501799,-6.996072,-9.161973,7.154934,-3.906481,3.915847,-8.256139,-6.046681,2.127733,-6.834033,1.629040,-0.670530,9.746913,1.833089,9.454672,-0.732393,3.731609,8.114458,9.684462,5.319070,-5.498805,5.624579,3.369386,8.593692,8.074125,6.188075,-5.222587,1.661212,-8.496179,-5.688099,2.126214,-9.202123,-7.037198,6.002275,-2.180458,6.284020,4.955027,3.933318,-2.312066,5.577258,-4.252962,-8.581073,-5.726036,0.321143,-7.110602,-5.689477,-0.557917,-5.243467,-2.744310,-4.647028,-6.619174,4.096034,-5.225379,-4.380078,8.788558,-2.467766,2.594433,-6.196263,-3.361746,-0.830647,-5.536914,4.114535,0.500228,4.063087,6.947313,1.566044,0.601538,5.274211,2.199387,-8.663251,5.945646,2.571868,-4.566786,9.968845,1.852185,6.160023,-8.626592,-5.290675,8.647829,-5.603108,-7.700547,-7.057075,-7.615883,2.160115,-5.689779,6.629854,0.672459,-4.113450,-0.839485,-7.707245,6.026462,4.570739,-8.750537,-0.840983,0.241172,-0.828208,-4.413445,4.310265,-2.484264,-1.221143,2.765969,4.385090,-0.424978,-2.533997,0.987987,-4.096544,-1.361269,-4.773270,-0.602395,-4.706855,9.025524,3.405653,-5.704354,4.945810,0.065855,6.661181,7.748903,6.330990,-4.681538,-1.837421,6.184708,-3.858727,9.072622,-2.376361,2.034646,3.563536,-7.804161,-8.015398,-3.917785,1.063018,-3.006261,-0.556889,2.138320,3.979411,1.515290,0.166323,6.601719,-3.669435,5.027981,-0.041138,-8.833271,0.142979,-1.697077,1.299709,2.898085,-0.568317,1.363124,2.222201,1.940171,-1.270003,5.715927,8.601365,5.284790,8.369743,-8.925147,-8.836530,0.110834,5.916786,2.602786,-1.635523,-0.068263,-5.719529,2.269705,-2.543371,9.704753,4.536503,8.136688,7.122148,6.541480,3.273064,-5.227554,-9.014575,9.620333,8.390059,-9.317879,-3.586007,-6.243469,-5.378244,-4.680620,-6.232964,9.487070,-3.812257,-3.716494,7.984106,-9.595820,-3.208224,-5.230011,4.295166,-0.419025,9.150736,-9.679142,0.973432,-0.250772,4.168763,3.340311,-1.509810,1.769983,0.899931,-2.874464,1.584580,3.516050,5.125926,-9.512108,8.668266,5.340846,0.754332,-6.442714,6.267684,-6.396192,-4.403081,-9.503388,-8.659832,0.678036,-1.806815,1.510418,9.660869,5.111674,-4.508984,7.069433,-5.402433,-0.544135,-4.936226,9.629452,-1.757073,-2.738993,2.017132,8.353426,3.207962,6.563725,1.923932,5.060310,9.840511,5.292685,4.849480,1.673703,-1.025600,6.537785,3.674077,-8.837769,3.743057,-5.374802,4.545843,-0.102658,-5.716252,-1.796443,-7.880687,-8.785612,-6.437654,-5.345909,-8.386882,-2.046243,6.789544,-5.431861,-6.633739,-1.278187,4.666096,-5.601560,2.748007,1.898113,-4.104776,9.068834,-8.604216,-1.983735,5.024872,-7.310851,-2.004853,-7.156225,-2.137378,-7.180420,8.236227,-5.306147,5.791385,-8.968536,-0.283701,4.759512,9.255162,4.595177,-5.333842,9.071514,-0.511023,-8.602687,-4.766828,6.968860,7.626494,7.693939,-8.884210,9.480025,-4.385302,-0.536831,-4.250367,9.131494,-1.833034,6.477765,-0.039190,6.836445,-4.907383,9.265482,-3.860092,3.022178,6.413583,4.349238,3.586686,2.419121,-9.554301,-6.491768,4.712095,-5.800697,-5.616885,6.540057,-1.462304,-9.565532,-7.225895,5.441776,-1.137862,-7.125726,4.452207,1.725256,-5.536637,-8.735759,5.152001,6.867268,-4.166252,-2.281186,7.881958,0.289290,-7.653751,-1.982092,-1.037126,-3.114708,3.479207,-7.306674,-7.790785,2.744254,-1.512322,0.425559,-5.550571,3.415119,-8.779504,3.984396,7.925614,-8.959313,-5.666854,-8.533274,-7.271010,7.039453,5.005151,0.658543,-0.808433,-1.161529,-2.697736,-0.697478,5.952974,-9.934529,0.162142,4.776259,-1.956819,9.365495,7.120965,0.788344,-0.660488,8.802425,-7.347004,5.110561,2.289709,-2.045961,8.197136,-8.931924,-5.725857,-5.216137,-3.729027,-9.009289,1.660693,-3.015341,0.528696,8.896135,-2.709553,9.459631,3.568455,0.096455,-6.819927,-0.718784,-4.965823,-4.217010,2.738364,6.403485,7.666348,9.453667,9.454113,6.915087,2.733852,-2.661210,9.976831,9.682866,-4.885428,9.455288,-7.213680,-5.330298,-9.242488,5.171372,4.614579,1.068783,-2.060611,-7.575194,-3.672392,-8.260124,-6.462919,-9.595039,-7.489751,-4.915451,-3.612024,4.867115,5.720567,-3.743376,3.658396,-7.289457,-6.527171,6.199035,-9.737438,-5.954456,9.352766,-9.421623,2.777308,9.664833,-3.548628,-3.943517,1.797235,2.588200,0.310784,-9.291646,2.325539,8.598353,-3.479690,-9.230206,-3.395472,-1.194344,0.492475,3.790789,2.291279,-4.082299,-7.800716,-5.706646,4.120205,5.235960,2.751766,4.439885,-8.113620,-6.163326,0.017393,7.034830,6.715642,4.611475,-8.620784,1.908864,4.156132,-5.895628,-8.592356,3.311727,-2.203064,-0.067136,-6.766995,3.095825,4.318730,9.074463,-2.239240,-9.650050,-0.022856,5.529484,0.588347,-2.593602,-2.853079,-4.354082,-2.996003,-2.986710,-9.414038,-1.222888,-3.035287,5.077437,-7.008569,-2.490450,8.268825,-7.034098,-3.024049,4.839137,7.842880,-0.586866,-2.720092,-5.583086,-2.576456,3.450502,-9.039603,6.097725,8.797670,-0.311449,-9.210518,8.941397,1.653184,0.546005,0.747418,6.031963,1.348910,-8.332483,9.628339,-3.377974,-7.653723,-7.369169,1.645623,5.922543,5.369563,-8.954128,8.466779,9.630111,-1.476425,-2.677329,9.331733,-8.327666,-3.708297,-8.518513,8.772519,5.276587,9.992628,-0.271376,-3.350545,2.944503,0.928294,8.023249,5.020009,-9.081539,4.077761,3.983195,-7.601826,1.659940,7.214217,-0.944760,-5.871865,-6.185906,-1.831812,2.242929,-5.565254,-8.487986,-5.957080,-2.067927,-1.427637,0.665618,-3.926035,8.377657,-4.647057,2.539909,-1.281808,9.069475,9.050214,-8.581241,-5.429689,-2.676976,6.749125,3.491792,-6.812765,1.934188,-1.972946,5.259375,-5.500351,6.328723,0.859278,-5.570898,9.728116,4.716747,5.427593,-6.651812,9.341436,-0.156168,6.323459,-8.370395,-0.526727,-6.860647], dtype = "float64")#candidate|16862|(1820,)|const|float64
call_16857 = relay.TupleGetItem(func_14769_call(relay.reshape(var_16858.astype('int64'), [6, 5, 16]), relay.reshape(var_16858.astype('int64'), [6, 5, 16]), relay.reshape(var_16859.astype('uint32'), []), relay.reshape(var_16860.astype('int32'), [1056,]), relay.reshape(var_16861.astype('float32'), [182, 2]), relay.reshape(const_16862.astype('float64'), [910, 2]), ), 2)
call_16863 = relay.TupleGetItem(func_14776_call(relay.reshape(var_16858.astype('int64'), [6, 5, 16]), relay.reshape(var_16858.astype('int64'), [6, 5, 16]), relay.reshape(var_16859.astype('uint32'), []), relay.reshape(var_16860.astype('int32'), [1056,]), relay.reshape(var_16861.astype('float32'), [182, 2]), relay.reshape(const_16862.astype('float64'), [910, 2]), ), 2)
output = relay.Tuple([call_16828,call_16857,var_16858,var_16859,var_16860,var_16861,const_16862,])
output2 = relay.Tuple([call_16829,call_16863,var_16858,var_16859,var_16860,var_16861,const_16862,])
func_16869 = relay.Function([var_16858,var_16859,var_16860,var_16861,], output)
mod['func_16869'] = func_16869
mod = relay.transform.InferType()(mod)
mutated_mod['func_16869'] = func_16869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_16869_call = mutated_mod.get_global_var('func_16869')
var_16871 = relay.var("var_16871", dtype = "int64", shape = (480,))#candidate|16871|(480,)|var|int64
var_16872 = relay.var("var_16872", dtype = "uint32", shape = ())#candidate|16872|()|var|uint32
var_16873 = relay.var("var_16873", dtype = "int32", shape = (4, 264))#candidate|16873|(4, 264)|var|int32
var_16874 = relay.var("var_16874", dtype = "float32", shape = (364,))#candidate|16874|(364,)|var|float32
call_16870 = func_16869_call(var_16871,var_16872,var_16873,var_16874,)
output = call_16870
func_16875 = relay.Function([var_16871,var_16872,var_16873,var_16874,], output)
mutated_mod['func_16875'] = func_16875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12443_call = mod.get_global_var('func_12443')
func_12444_call = mutated_mod.get_global_var('func_12444')
call_16955 = relay.TupleGetItem(func_12443_call(), 0)
call_16956 = relay.TupleGetItem(func_12444_call(), 0)
output = call_16955
output2 = call_16956
func_16958 = relay.Function([], output)
mod['func_16958'] = func_16958
mod = relay.transform.InferType()(mod)
output = func_16958()
func_16959 = relay.Function([], output)
mutated_mod['func_16959'] = func_16959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13581_call = mod.get_global_var('func_13581')
func_13583_call = mutated_mod.get_global_var('func_13583')
call_17016 = func_13581_call()
call_17017 = func_13581_call()
output = call_17016
output2 = call_17017
func_17063 = relay.Function([], output)
mod['func_17063'] = func_17063
mod = relay.transform.InferType()(mod)
mutated_mod['func_17063'] = func_17063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17063_call = mutated_mod.get_global_var('func_17063')
call_17064 = func_17063_call()
output = call_17064
func_17065 = relay.Function([], output)
mutated_mod['func_17065'] = func_17065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12760_call = mod.get_global_var('func_12760')
func_12761_call = mutated_mod.get_global_var('func_12761')
call_17112 = relay.TupleGetItem(func_12760_call(), 0)
call_17113 = relay.TupleGetItem(func_12761_call(), 0)
output = call_17112
output2 = call_17113
func_17115 = relay.Function([], output)
mod['func_17115'] = func_17115
mod = relay.transform.InferType()(mod)
mutated_mod['func_17115'] = func_17115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17115_call = mutated_mod.get_global_var('func_17115')
call_17116 = func_17115_call()
output = call_17116
func_17117 = relay.Function([], output)
mutated_mod['func_17117'] = func_17117
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10787_call = mod.get_global_var('func_10787')
func_10788_call = mutated_mod.get_global_var('func_10788')
call_17118 = func_10787_call()
call_17119 = func_10787_call()
output = call_17118
output2 = call_17119
func_17120 = relay.Function([], output)
mod['func_17120'] = func_17120
mod = relay.transform.InferType()(mod)
output = func_17120()
func_17121 = relay.Function([], output)
mutated_mod['func_17121'] = func_17121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13972_call = mod.get_global_var('func_13972')
func_13974_call = mutated_mod.get_global_var('func_13974')
call_17143 = relay.TupleGetItem(func_13972_call(), 0)
call_17144 = relay.TupleGetItem(func_13974_call(), 0)
output = relay.Tuple([call_17143,])
output2 = relay.Tuple([call_17144,])
func_17149 = relay.Function([], output)
mod['func_17149'] = func_17149
mod = relay.transform.InferType()(mod)
mutated_mod['func_17149'] = func_17149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17149_call = mutated_mod.get_global_var('func_17149')
call_17150 = func_17149_call()
output = call_17150
func_17151 = relay.Function([], output)
mutated_mod['func_17151'] = func_17151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13132_call = mod.get_global_var('func_13132')
func_13133_call = mutated_mod.get_global_var('func_13133')
call_17204 = relay.TupleGetItem(func_13132_call(), 1)
call_17205 = relay.TupleGetItem(func_13133_call(), 1)
output = relay.Tuple([call_17204,])
output2 = relay.Tuple([call_17205,])
func_17208 = relay.Function([], output)
mod['func_17208'] = func_17208
mod = relay.transform.InferType()(mod)
mutated_mod['func_17208'] = func_17208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17208_call = mutated_mod.get_global_var('func_17208')
call_17209 = func_17208_call()
output = call_17209
func_17210 = relay.Function([], output)
mutated_mod['func_17210'] = func_17210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5900_call = mod.get_global_var('func_5900')
func_5901_call = mutated_mod.get_global_var('func_5901')
call_17224 = relay.TupleGetItem(func_5900_call(), 0)
call_17225 = relay.TupleGetItem(func_5901_call(), 0)
output = relay.Tuple([call_17224,])
output2 = relay.Tuple([call_17225,])
func_17248 = relay.Function([], output)
mod['func_17248'] = func_17248
mod = relay.transform.InferType()(mod)
output = func_17248()
func_17249 = relay.Function([], output)
mutated_mod['func_17249'] = func_17249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12719_call = mod.get_global_var('func_12719')
func_12720_call = mutated_mod.get_global_var('func_12720')
call_17277 = func_12719_call()
call_17278 = func_12719_call()
output = relay.Tuple([call_17277,])
output2 = relay.Tuple([call_17278,])
func_17281 = relay.Function([], output)
mod['func_17281'] = func_17281
mod = relay.transform.InferType()(mod)
output = func_17281()
func_17282 = relay.Function([], output)
mutated_mod['func_17282'] = func_17282
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17283 = relay.var("var_17283", dtype = "int32", shape = (4, 5, 10))#candidate|17283|(4, 5, 10)|var|int32
var_17284 = relay.var("var_17284", dtype = "int32", shape = (4, 5, 10))#candidate|17284|(4, 5, 10)|var|int32
bop_17285 = relay.less_equal(var_17283.astype('bool'), relay.reshape(var_17284.astype('bool'), relay.shape_of(var_17283))) # shape=(4, 5, 10)
output = relay.Tuple([bop_17285,])
output2 = relay.Tuple([bop_17285,])
func_17289 = relay.Function([var_17283,var_17284,], output)
mod['func_17289'] = func_17289
mod = relay.transform.InferType()(mod)
var_17290 = relay.var("var_17290", dtype = "int32", shape = (4, 5, 10))#candidate|17290|(4, 5, 10)|var|int32
var_17291 = relay.var("var_17291", dtype = "int32", shape = (4, 5, 10))#candidate|17291|(4, 5, 10)|var|int32
output = func_17289(var_17290,var_17291,)
func_17292 = relay.Function([var_17290,var_17291,], output)
mutated_mod['func_17292'] = func_17292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8532_call = mod.get_global_var('func_8532')
func_8534_call = mutated_mod.get_global_var('func_8534')
call_17369 = relay.TupleGetItem(func_8532_call(), 0)
call_17370 = relay.TupleGetItem(func_8534_call(), 0)
output = relay.Tuple([call_17369,])
output2 = relay.Tuple([call_17370,])
func_17377 = relay.Function([], output)
mod['func_17377'] = func_17377
mod = relay.transform.InferType()(mod)
output = func_17377()
func_17378 = relay.Function([], output)
mutated_mod['func_17378'] = func_17378
mutated_mod = relay.transform.InferType()(mutated_mod)
const_17382 = relay.const([[[-1,-2,5,3,-1,-1,5,-9,5],[-10,-8,4,4,10,-8,-8,8,-3],[-3,6,5,-2,-5,7,-10,4,9],[-4,7,-7,-5,-5,-6,-7,7,6],[3,2,-10,7,5,-10,3,-5,5],[5,-10,6,1,8,9,9,3,-1],[10,3,-1,-8,-6,-5,9,-5,-2],[-5,-4,-2,7,6,-5,-5,7,10],[2,4,-3,2,-1,-8,-8,8,8],[-7,-3,6,-2,-3,-8,8,-1,9],[1,5,-8,5,-8,10,-2,2,3],[-5,9,-5,3,9,4,-9,9,7],[8,5,-4,3,-3,-3,-3,3,-8],[-2,-10,8,-1,10,-2,-9,-8,6],[9,-8,-4,-9,9,2,-8,2,-3],[5,7,4,-2,-8,7,-2,5,9]],[[1,10,-9,1,5,7,-4,-4,10],[10,2,4,-4,-4,-6,-10,-10,-1],[3,6,5,-7,-8,10,10,-1,8],[2,2,2,-10,7,5,8,-7,-5],[10,1,-3,-7,9,-7,-1,-10,4],[1,6,-5,5,8,-10,6,7,9],[8,-4,3,-3,-10,-7,5,-10,9],[4,7,-8,9,8,-3,7,-2,-6],[4,-9,-4,-9,-8,2,2,-3,-1],[7,-7,5,1,-9,5,-10,-7,-3],[9,2,3,-7,1,6,-1,4,-10],[-7,-3,6,4,-8,4,1,-7,1],[8,-5,-5,3,-7,-5,-5,8,9],[-5,7,-3,7,4,-9,-4,-10,6],[-1,5,-3,5,-3,6,-4,-4,-6],[-3,2,-9,-10,-6,3,10,-8,-3]],[[7,8,8,3,-7,-6,5,6,-5],[-6,7,9,-3,-3,6,-3,2,3],[7,6,3,7,-1,5,5,3,3],[-1,3,-9,-9,-1,6,-5,-10,-9],[4,10,6,-1,7,4,-10,-10,8],[-1,2,2,-8,4,-7,-10,6,6],[7,4,5,-6,4,5,5,-1,-10],[8,-9,5,-5,8,-4,5,4,-7],[-9,2,-1,7,5,-7,-2,-2,-7],[-8,-1,-4,-5,-8,10,7,-2,-5],[10,-1,10,1,-2,5,-1,10,3],[8,-4,-6,4,4,-4,9,10,8],[-7,-4,-3,8,3,-5,3,2,-2],[2,2,1,4,2,1,6,9,9],[-8,-6,-5,7,6,5,-10,3,-4],[1,-6,2,1,7,7,-3,-3,9]],[[-4,7,-10,8,-1,3,5,3,-7],[1,4,-9,6,-9,-5,-6,-5,-8],[7,-4,-7,4,-2,-3,4,6,-2],[1,1,6,6,-6,4,5,-10,-10],[7,8,10,8,-5,-2,-1,4,2],[-9,-1,1,-9,-9,-7,-7,-4,6],[4,10,8,6,-4,1,-10,6,5],[1,6,-2,-10,9,-2,9,-9,-7],[10,6,6,2,8,-9,3,-7,-1],[-2,-8,6,8,-9,-6,-3,10,10],[9,-3,-10,-1,2,4,7,-6,-8],[8,-10,2,3,-2,-7,10,6,4],[-6,9,-5,3,10,8,4,4,4],[1,3,10,-6,7,-4,8,-8,-7],[-1,-6,4,8,1,-3,8,-2,-7],[-3,5,-7,-3,-8,-3,5,-9,-6]],[[4,-8,-4,1,7,6,-6,-9,9],[9,-2,-2,-3,-10,7,-5,9,-9],[6,-6,-1,-7,1,9,3,-1,-6],[1,-1,4,-6,-10,-2,-10,9,3],[8,9,7,9,-6,4,-5,-3,-7],[-4,-6,10,5,8,3,6,-3,-3],[2,10,-10,4,-1,-2,6,1,-4],[1,10,5,-3,7,7,6,-9,9],[-5,7,-10,4,6,-7,8,-2,-9],[2,-10,-10,6,-6,4,-8,-8,5],[-3,3,4,-2,8,-1,-2,1,-9],[-9,-6,-3,10,-9,6,8,3,-1],[-1,-1,8,8,-2,-4,-7,-9,-7],[5,-4,10,8,-9,7,-8,-2,7],[-1,-10,1,6,-6,-3,9,-4,2],[-1,10,-1,-10,5,-8,-2,7,-3]],[[-7,-10,-6,-9,3,-6,-7,-5,-8],[4,-7,-10,3,-5,-5,9,-7,-6],[-2,-8,8,9,-2,2,3,8,7],[5,9,10,-6,5,-8,6,5,6],[-9,-1,-1,1,-9,2,-6,-5,6],[-6,-4,8,3,3,-10,-3,6,-10],[-7,1,-1,-1,1,-9,-1,9,-9],[7,-3,-9,-1,-1,-8,-6,-1,10],[-1,8,-9,10,3,5,-8,-3,-5],[3,-9,-5,-5,-2,9,8,-5,3],[-3,-3,-4,-10,1,3,-8,-3,9],[3,-8,-10,-7,6,-5,5,4,8],[-8,-8,2,4,8,-4,-5,2,-2],[-8,-1,2,-5,-7,6,-5,-4,3],[6,5,-7,2,-7,-5,7,7,-10],[-7,7,2,-9,-10,-1,10,-2,-1]],[[5,-3,8,-1,-3,-2,-9,-10,2],[4,10,-6,-8,-10,3,-1,7,-1],[4,-9,-10,4,1,-10,5,-6,-7],[-7,1,7,-9,2,-4,10,-5,-7],[-9,8,4,-2,-1,3,3,5,7],[7,2,-9,-6,-6,-7,8,3,-7],[4,-7,10,-3,10,-8,-9,3,6],[-8,1,3,-7,6,-9,-9,2,5],[6,6,5,-4,-9,-6,9,9,-7],[7,-3,4,-4,4,10,2,7,-1],[2,-9,-2,-7,-8,-10,9,9,-10],[6,9,-4,9,-5,3,-1,3,7],[-6,6,-1,10,-8,1,-5,4,5],[3,3,2,-3,-3,4,2,4,-3],[8,4,4,4,2,-5,5,3,-3],[-7,8,5,-2,2,-6,-3,-10,-10]],[[2,-8,-1,3,9,5,-1,-10,-4],[2,1,2,-9,-4,1,7,-6,-8],[-6,-5,5,8,-2,-6,5,-2,2],[-6,10,1,-1,-5,-3,-6,-1,3],[10,-3,-2,-9,-9,-5,-7,-1,10],[10,-2,10,5,-4,6,-6,1,-1],[10,-1,-2,-7,7,8,2,9,-3],[7,5,-6,-9,9,4,4,-9,3],[3,-2,10,8,-8,-5,-7,10,-4],[-5,1,-6,4,-8,-4,4,-5,-8],[8,8,-6,-6,-5,-5,5,5,-5],[-10,8,-2,1,2,2,-2,9,-6],[-10,5,1,8,1,-1,-4,-5,-8],[-7,-3,-4,10,-7,5,3,10,-3],[-10,-6,-4,-9,-5,-3,1,2,10],[3,4,-10,-3,-4,-10,3,-8,3]],[[7,2,-8,5,-6,5,4,7,-8],[-7,-9,4,-8,9,8,-9,6,7],[8,-3,-2,8,6,6,-2,5,-1],[-1,5,-6,2,8,-7,-1,-8,9],[1,-5,-5,-1,1,-8,-4,-3,9],[-2,5,10,-6,8,3,3,7,1],[9,6,-7,-6,3,9,-9,2,4],[9,-1,3,4,-8,-6,-2,-2,-4],[-5,1,2,-10,3,-6,-6,-7,3],[2,8,10,-10,6,1,4,-2,5],[-5,6,1,-4,-8,5,-1,-9,-7],[-2,1,3,-9,9,-2,-7,1,6],[5,10,-3,5,10,-4,2,7,3],[7,-9,-3,-3,9,-4,-8,8,-4],[-1,-6,4,-1,5,2,-8,-10,-5],[9,3,-2,4,6,7,5,-1,-2]],[[-3,3,-3,-6,4,-9,8,7,-5],[-8,10,-2,-6,-7,-8,-1,-4,-8],[9,-7,1,4,-1,3,-9,-6,7],[-5,5,-1,3,-3,-6,1,9,2],[3,1,6,-1,-9,3,-4,-10,-2],[-1,2,-1,5,8,1,3,-6,9],[2,-7,6,-6,10,-7,-6,-1,-2],[-7,-6,2,4,3,-2,10,-4,-5],[-8,-1,7,-5,8,-1,8,-9,4],[-4,-9,-6,3,4,-4,-8,-10,-3],[10,-1,-1,1,2,-4,3,3,-8],[2,-7,-9,-7,-3,7,-5,-3,-7],[1,-6,10,-7,1,-7,-1,8,-7],[-8,3,5,-9,-9,9,9,-6,2],[6,-10,-1,3,8,-9,8,3,-9],[1,9,10,-8,7,-3,-1,-8,5]],[[-10,1,-10,4,8,-9,-6,-4,-2],[4,-5,-5,9,7,-9,-7,1,-8],[8,8,1,-2,-8,3,-3,2,-5],[-6,3,2,-8,-10,8,-9,-1,-2],[-2,1,-3,4,9,-3,4,-1,-7],[-10,3,-3,7,-9,8,-3,6,-2],[6,4,-3,2,-8,-6,-5,9,4],[2,3,4,-3,-2,8,-9,-4,-2],[3,4,-6,-8,7,-10,1,-6,3],[6,6,-8,-5,-1,-3,-6,6,8],[2,-4,3,-2,7,-9,-8,8,-4],[-8,-5,-10,3,-3,-9,2,6,2],[9,-4,-2,7,-7,-3,3,-3,-2],[9,10,4,-4,1,-2,9,-7,-8],[-5,10,-1,-6,6,-7,2,-4,7],[-2,-4,-10,3,8,2,10,10,-1]],[[5,-7,7,-9,-9,1,-1,-6,-3],[-3,-6,10,-6,5,-2,-9,4,-8],[-2,-9,-2,-7,-3,-9,-1,-7,-5],[5,9,7,6,8,4,10,7,-6],[-10,-1,10,-1,4,6,-7,1,8],[-7,8,4,-3,9,-4,8,-10,8],[3,-10,1,6,-4,-4,-7,-1,-6],[6,-1,-1,9,-10,-10,-10,-2,-10],[6,-1,-5,5,5,6,2,5,6],[-8,-7,8,1,-10,8,-3,8,-5],[10,6,7,-9,5,-2,-9,-7,-1],[4,5,-4,-6,5,3,-8,1,8],[-5,7,-8,10,-1,2,4,-3,-9],[-1,-4,-10,8,9,3,9,4,-7],[-7,10,8,10,-9,2,-2,5,-9],[4,-5,9,2,-6,-6,-9,-2,10]],[[10,-1,-5,-8,-5,-2,10,-4,-8],[-2,2,7,3,-10,-4,6,-10,-4],[1,1,-5,-2,8,-9,-10,-9,1],[2,-1,-10,5,-10,2,-2,-7,8],[-6,6,-6,-10,-6,-1,-4,-4,9],[9,-9,-3,-4,3,-7,-3,1,7],[-4,6,-6,8,3,-5,5,8,-5],[-4,-5,-10,10,-5,3,-10,9,-7],[-4,6,-7,10,5,6,9,10,-9],[-4,6,-1,3,5,7,6,-9,9],[-3,9,-6,-9,7,7,-10,4,-4],[6,-6,7,5,7,8,-3,2,1],[7,3,7,-9,-2,-4,9,2,-1],[3,4,1,3,-5,5,4,-3,-7],[6,-9,10,5,-1,9,7,9,9],[5,3,-10,3,-4,1,-7,9,5]],[[1,-1,8,6,1,9,5,-5,-4],[-9,-8,-5,4,6,-10,-3,3,-3],[5,10,-3,7,5,-6,-4,7,-8],[1,-4,3,9,5,1,5,-7,1],[4,-10,9,-7,1,-7,4,-10,4],[-4,-9,-5,7,6,6,4,7,-8],[-9,1,9,-8,-5,-3,2,-4,-4],[-1,2,5,-7,8,2,-10,1,1],[-9,-2,9,-7,-5,-4,-1,-10,-4],[-1,-3,-7,-2,-5,10,2,-7,8],[-4,-7,-8,-5,-5,4,-1,2,-1],[-8,10,8,9,1,-6,2,-6,6],[9,4,10,5,10,-5,8,6,7],[10,-3,2,2,7,2,-3,-7,-6],[5,-8,1,-10,7,9,-9,1,-9],[-9,-6,2,-2,-10,-2,-7,8,-5]]], dtype = "uint64")#candidate|17382|(14, 16, 9)|const|uint64
var_17383 = relay.var("var_17383", dtype = "uint64", shape = (14, 16, 9))#candidate|17383|(14, 16, 9)|var|uint64
bop_17384 = relay.add(const_17382.astype('uint64'), relay.reshape(var_17383.astype('uint64'), relay.shape_of(const_17382))) # shape=(14, 16, 9)
func_11445_call = mod.get_global_var('func_11445')
func_11447_call = mutated_mod.get_global_var('func_11447')
call_17408 = relay.TupleGetItem(func_11445_call(), 0)
call_17409 = relay.TupleGetItem(func_11447_call(), 0)
func_13253_call = mod.get_global_var('func_13253')
func_13254_call = mutated_mod.get_global_var('func_13254')
call_17412 = relay.TupleGetItem(func_13253_call(), 0)
call_17413 = relay.TupleGetItem(func_13254_call(), 0)
func_16288_call = mod.get_global_var('func_16288')
func_16290_call = mutated_mod.get_global_var('func_16290')
call_17415 = relay.TupleGetItem(func_16288_call(), 0)
call_17416 = relay.TupleGetItem(func_16290_call(), 0)
func_4460_call = mod.get_global_var('func_4460')
func_4462_call = mutated_mod.get_global_var('func_4462')
call_17423 = func_4460_call()
call_17424 = func_4460_call()
func_17149_call = mod.get_global_var('func_17149')
func_17151_call = mutated_mod.get_global_var('func_17151')
call_17437 = relay.TupleGetItem(func_17149_call(), 0)
call_17438 = relay.TupleGetItem(func_17151_call(), 0)
func_10913_call = mod.get_global_var('func_10913')
func_10916_call = mutated_mod.get_global_var('func_10916')
var_17444 = relay.var("var_17444", dtype = "uint64", shape = (2340,))#candidate|17444|(2340,)|var|uint64
var_17445 = relay.var("var_17445", dtype = "float64", shape = (39,))#candidate|17445|(39,)|var|float64
call_17443 = relay.TupleGetItem(func_10913_call(relay.reshape(var_17444.astype('uint64'), [12, 13, 15]), relay.reshape(var_17445.astype('float64'), [39,]), ), 1)
call_17446 = relay.TupleGetItem(func_10916_call(relay.reshape(var_17444.astype('uint64'), [12, 13, 15]), relay.reshape(var_17445.astype('float64'), [39,]), ), 1)
func_11503_call = mod.get_global_var('func_11503')
func_11504_call = mutated_mod.get_global_var('func_11504')
call_17447 = relay.TupleGetItem(func_11503_call(), 0)
call_17448 = relay.TupleGetItem(func_11504_call(), 0)
output = relay.Tuple([bop_17384,call_17408,call_17412,call_17415,call_17423,call_17437,call_17443,var_17444,var_17445,call_17447,])
output2 = relay.Tuple([bop_17384,call_17409,call_17413,call_17416,call_17424,call_17438,call_17446,var_17444,var_17445,call_17448,])
func_17456 = relay.Function([var_17383,var_17444,var_17445,], output)
mod['func_17456'] = func_17456
mod = relay.transform.InferType()(mod)
var_17457 = relay.var("var_17457", dtype = "uint64", shape = (14, 16, 9))#candidate|17457|(14, 16, 9)|var|uint64
var_17458 = relay.var("var_17458", dtype = "uint64", shape = (2340,))#candidate|17458|(2340,)|var|uint64
var_17459 = relay.var("var_17459", dtype = "float64", shape = (39,))#candidate|17459|(39,)|var|float64
output = func_17456(var_17457,var_17458,var_17459,)
func_17460 = relay.Function([var_17457,var_17458,var_17459,], output)
mutated_mod['func_17460'] = func_17460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8662_call = mod.get_global_var('func_8662')
func_8664_call = mutated_mod.get_global_var('func_8664')
call_17513 = relay.TupleGetItem(func_8662_call(), 0)
call_17514 = relay.TupleGetItem(func_8664_call(), 0)
func_16413_call = mod.get_global_var('func_16413')
func_16414_call = mutated_mod.get_global_var('func_16414')
call_17521 = relay.TupleGetItem(func_16413_call(), 1)
call_17522 = relay.TupleGetItem(func_16414_call(), 1)
output = relay.Tuple([call_17513,call_17521,])
output2 = relay.Tuple([call_17514,call_17522,])
func_17527 = relay.Function([], output)
mod['func_17527'] = func_17527
mod = relay.transform.InferType()(mod)
mutated_mod['func_17527'] = func_17527
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17527_call = mutated_mod.get_global_var('func_17527')
call_17528 = func_17527_call()
output = call_17528
func_17529 = relay.Function([], output)
mutated_mod['func_17529'] = func_17529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8804_call = mod.get_global_var('func_8804')
func_8806_call = mutated_mod.get_global_var('func_8806')
call_17530 = relay.TupleGetItem(func_8804_call(), 0)
call_17531 = relay.TupleGetItem(func_8806_call(), 0)
func_9118_call = mod.get_global_var('func_9118')
func_9121_call = mutated_mod.get_global_var('func_9121')
var_17562 = relay.var("var_17562", dtype = "float32", shape = (91, 4))#candidate|17562|(91, 4)|var|float32
call_17561 = relay.TupleGetItem(func_9118_call(relay.reshape(var_17562.astype('float32'), [13, 2, 14]), relay.reshape(var_17562.astype('float32'), [13, 2, 14]), ), 0)
call_17563 = relay.TupleGetItem(func_9121_call(relay.reshape(var_17562.astype('float32'), [13, 2, 14]), relay.reshape(var_17562.astype('float32'), [13, 2, 14]), ), 0)
func_4743_call = mod.get_global_var('func_4743')
func_4747_call = mutated_mod.get_global_var('func_4747')
const_17582 = relay.const(6, dtype = "uint32")#candidate|17582|()|const|uint32
const_17583 = relay.const([[1,-9,-6,-2]], dtype = "uint32")#candidate|17583|(1, 4)|const|uint32
call_17581 = relay.TupleGetItem(func_4743_call(relay.reshape(const_17582.astype('uint32'), []), relay.reshape(const_17583.astype('uint32'), [4,]), ), 5)
call_17584 = relay.TupleGetItem(func_4747_call(relay.reshape(const_17582.astype('uint32'), []), relay.reshape(const_17583.astype('uint32'), [4,]), ), 5)
func_11617_call = mod.get_global_var('func_11617')
func_11620_call = mutated_mod.get_global_var('func_11620')
const_17600 = relay.const([[4.260489,5.972562,-5.108530],[7.218053,-6.783254,-5.133440],[-1.971047,-5.893223,-0.703853],[-4.710702,5.785499,8.822434],[9.834816,-2.746027,-8.946094],[8.247330,-8.372521,7.394781],[4.196262,-6.194961,-5.552026],[9.710406,-2.357669,-0.058831],[0.589965,-8.668315,-0.545694],[0.530618,-3.665836,2.627361],[-5.369499,-7.505284,-4.097906],[-3.411516,-0.630791,6.061268],[3.202322,-8.860558,-2.088527]], dtype = "float64")#candidate|17600|(13, 3)|const|float64
call_17599 = relay.TupleGetItem(func_11617_call(relay.reshape(const_17600.astype('float64'), [13, 3])), 0)
call_17601 = relay.TupleGetItem(func_11620_call(relay.reshape(const_17600.astype('float64'), [13, 3])), 0)
func_11697_call = mod.get_global_var('func_11697')
func_11698_call = mutated_mod.get_global_var('func_11698')
call_17614 = relay.TupleGetItem(func_11697_call(), 0)
call_17615 = relay.TupleGetItem(func_11698_call(), 0)
func_6631_call = mod.get_global_var('func_6631')
func_6634_call = mutated_mod.get_global_var('func_6634')
call_17622 = relay.TupleGetItem(func_6631_call(relay.reshape(call_17530.astype('float32'), [14, 5, 13])), 0)
call_17623 = relay.TupleGetItem(func_6634_call(relay.reshape(call_17530.astype('float32'), [14, 5, 13])), 0)
func_12682_call = mod.get_global_var('func_12682')
func_12685_call = mutated_mod.get_global_var('func_12685')
call_17629 = relay.TupleGetItem(func_12682_call(relay.reshape(call_17581.astype('uint64'), [])), 1)
call_17630 = relay.TupleGetItem(func_12685_call(relay.reshape(call_17581.astype('uint64'), [])), 1)
bop_17632 = relay.logical_or(call_17581.astype('bool'), call_17614.astype('bool')) # shape=(864,)
bop_17635 = relay.logical_or(call_17584.astype('bool'), call_17615.astype('bool')) # shape=(864,)
func_6997_call = mod.get_global_var('func_6997')
func_6999_call = mutated_mod.get_global_var('func_6999')
call_17642 = func_6997_call()
call_17643 = func_6997_call()
output = relay.Tuple([call_17530,call_17561,var_17562,const_17582,const_17583,call_17599,const_17600,call_17622,call_17629,bop_17632,call_17642,])
output2 = relay.Tuple([call_17531,call_17563,var_17562,const_17582,const_17583,call_17601,const_17600,call_17623,call_17630,bop_17635,call_17643,])
func_17649 = relay.Function([var_17562,], output)
mod['func_17649'] = func_17649
mod = relay.transform.InferType()(mod)
mutated_mod['func_17649'] = func_17649
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17650 = relay.var("var_17650", dtype = "float32", shape = (91, 4))#candidate|17650|(91, 4)|var|float32
func_17649_call = mutated_mod.get_global_var('func_17649')
call_17651 = func_17649_call(var_17650)
output = call_17651
func_17652 = relay.Function([var_17650], output)
mutated_mod['func_17652'] = func_17652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4612_call = mod.get_global_var('func_4612')
func_4614_call = mutated_mod.get_global_var('func_4614')
call_17661 = relay.TupleGetItem(func_4612_call(), 0)
call_17662 = relay.TupleGetItem(func_4614_call(), 0)
func_17377_call = mod.get_global_var('func_17377')
func_17378_call = mutated_mod.get_global_var('func_17378')
call_17690 = relay.TupleGetItem(func_17377_call(), 0)
call_17691 = relay.TupleGetItem(func_17378_call(), 0)
func_12719_call = mod.get_global_var('func_12719')
func_12720_call = mutated_mod.get_global_var('func_12720')
call_17700 = func_12719_call()
call_17701 = func_12719_call()
output = relay.Tuple([call_17661,call_17690,call_17700,])
output2 = relay.Tuple([call_17662,call_17691,call_17701,])
func_17702 = relay.Function([], output)
mod['func_17702'] = func_17702
mod = relay.transform.InferType()(mod)
output = func_17702()
func_17703 = relay.Function([], output)
mutated_mod['func_17703'] = func_17703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_14836_call = mod.get_global_var('func_14836')
func_14838_call = mutated_mod.get_global_var('func_14838')
call_17719 = relay.TupleGetItem(func_14836_call(), 0)
call_17720 = relay.TupleGetItem(func_14838_call(), 0)
func_12682_call = mod.get_global_var('func_12682')
func_12685_call = mutated_mod.get_global_var('func_12685')
var_17746 = relay.var("var_17746", dtype = "uint64", shape = ())#candidate|17746|()|var|uint64
call_17745 = relay.TupleGetItem(func_12682_call(relay.reshape(var_17746.astype('uint64'), [])), 5)
call_17747 = relay.TupleGetItem(func_12685_call(relay.reshape(var_17746.astype('uint64'), [])), 5)
output = relay.Tuple([call_17719,call_17745,var_17746,])
output2 = relay.Tuple([call_17720,call_17747,var_17746,])
func_17750 = relay.Function([var_17746,], output)
mod['func_17750'] = func_17750
mod = relay.transform.InferType()(mod)
mutated_mod['func_17750'] = func_17750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17751 = relay.var("var_17751", dtype = "uint64", shape = ())#candidate|17751|()|var|uint64
func_17750_call = mutated_mod.get_global_var('func_17750')
call_17752 = func_17750_call(var_17751)
output = call_17752
func_17753 = relay.Function([var_17751], output)
mutated_mod['func_17753'] = func_17753
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7157_call = mod.get_global_var('func_7157')
func_7158_call = mutated_mod.get_global_var('func_7158')
call_17760 = relay.TupleGetItem(func_7157_call(), 0)
call_17761 = relay.TupleGetItem(func_7158_call(), 0)
output = relay.Tuple([call_17760,])
output2 = relay.Tuple([call_17761,])
func_17762 = relay.Function([], output)
mod['func_17762'] = func_17762
mod = relay.transform.InferType()(mod)
output = func_17762()
func_17763 = relay.Function([], output)
mutated_mod['func_17763'] = func_17763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17208_call = mod.get_global_var('func_17208')
func_17210_call = mutated_mod.get_global_var('func_17210')
call_17828 = relay.TupleGetItem(func_17208_call(), 0)
call_17829 = relay.TupleGetItem(func_17210_call(), 0)
output = call_17828
output2 = call_17829
func_17839 = relay.Function([], output)
mod['func_17839'] = func_17839
mod = relay.transform.InferType()(mod)
mutated_mod['func_17839'] = func_17839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_17839_call = mutated_mod.get_global_var('func_17839')
call_17840 = func_17839_call()
output = call_17840
func_17841 = relay.Function([], output)
mutated_mod['func_17841'] = func_17841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12183_call = mod.get_global_var('func_12183')
func_12184_call = mutated_mod.get_global_var('func_12184')
call_17852 = func_12183_call()
call_17853 = func_12183_call()
output = relay.Tuple([call_17852,])
output2 = relay.Tuple([call_17853,])
func_17870 = relay.Function([], output)
mod['func_17870'] = func_17870
mod = relay.transform.InferType()(mod)
output = func_17870()
func_17871 = relay.Function([], output)
mutated_mod['func_17871'] = func_17871
mutated_mod = relay.transform.InferType()(mutated_mod)
var_17872 = relay.var("var_17872", dtype = "float64", shape = (14, 1, 11))#candidate|17872|(14, 1, 11)|var|float64
uop_17873 = relay.log(var_17872.astype('float64')) # shape=(14, 1, 11)
output = uop_17873
output2 = uop_17873
F = relay.Function([var_17872,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_17872,], output2)
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
