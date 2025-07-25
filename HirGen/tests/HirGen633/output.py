import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_50 = relay.var("var_50", dtype = "float32", shape = (8, 5, 16))#candidate|50|(8, 5, 16)|var|float32
uop_51 = relay.atan(var_50.astype('float32')) # shape=(8, 5, 16)
var_53 = relay.var("var_53", dtype = "float32", shape = (8, 5, 16))#candidate|53|(8, 5, 16)|var|float32
bop_54 = relay.right_shift(var_50.astype('uint8'), relay.reshape(var_53.astype('uint8'), relay.shape_of(var_50))) # shape=(8, 5, 16)
uop_58 = relay.sinh(uop_51.astype('float32')) # shape=(8, 5, 16)
bop_92 = relay.divide(uop_58.astype('float64'), relay.reshape(bop_54.astype('float64'), relay.shape_of(uop_58))) # shape=(8, 5, 16)
output = bop_92
output2 = bop_92
func_113 = relay.Function([var_50,var_53,], output)
mod['func_113'] = func_113
mod = relay.transform.InferType()(mod)
var_114 = relay.var("var_114", dtype = "float32", shape = (8, 5, 16))#candidate|114|(8, 5, 16)|var|float32
var_115 = relay.var("var_115", dtype = "float32", shape = (8, 5, 16))#candidate|115|(8, 5, 16)|var|float32
output = func_113(var_114,var_115,)
func_116 = relay.Function([var_114,var_115,], output)
mutated_mod['func_116'] = func_116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_330 = relay.var("var_330", dtype = "float64", shape = ())#candidate|330|()|var|float64
var_331 = relay.var("var_331", dtype = "float64", shape = (10, 9, 1))#candidate|331|(10, 9, 1)|var|float64
bop_332 = relay.power(var_330.astype('float64'), var_331.astype('float64')) # shape=(10, 9, 1)
uop_337 = relay.sinh(bop_332.astype('float32')) # shape=(10, 9, 1)
bop_341 = relay.add(uop_337.astype('uint64'), relay.reshape(bop_332.astype('uint64'), relay.shape_of(uop_337))) # shape=(10, 9, 1)
bop_344 = relay.bitwise_or(uop_337.astype('int64'), relay.reshape(bop_332.astype('int64'), relay.shape_of(uop_337))) # shape=(10, 9, 1)
output = relay.Tuple([bop_341,bop_344,])
output2 = relay.Tuple([bop_341,bop_344,])
func_364 = relay.Function([var_330,var_331,], output)
mod['func_364'] = func_364
mod = relay.transform.InferType()(mod)
var_365 = relay.var("var_365", dtype = "float64", shape = ())#candidate|365|()|var|float64
var_366 = relay.var("var_366", dtype = "float64", shape = (10, 9, 1))#candidate|366|(10, 9, 1)|var|float64
output = func_364(var_365,var_366,)
func_367 = relay.Function([var_365,var_366,], output)
mutated_mod['func_367'] = func_367
mutated_mod = relay.transform.InferType()(mutated_mod)
const_831 = relay.const([[[10,-9,7,-3,-2,1,10,7,-3,-9,7],[1,9,6,-7,-5,-6,-2,-6,1,-5,9],[8,-7,8,5,3,-5,-1,-4,-7,-5,-1],[-5,-1,-6,-9,-4,-10,-7,10,6,-8,-8],[5,9,-10,4,-1,-8,-7,1,-9,2,-9],[-10,3,-2,10,-1,-1,6,5,3,-10,10],[-7,-3,9,8,6,-5,-7,-1,-7,9,-3],[9,6,7,3,3,-10,6,4,5,3,1],[7,6,-4,-3,-9,-8,6,-1,3,-1,-10],[2,3,6,-9,6,8,-3,-7,1,1,-3],[7,6,-7,2,-3,1,-4,-2,3,3,1],[4,-2,-8,-8,-8,4,-4,-10,-8,3,-9],[-6,1,2,-1,-10,3,-3,3,-1,-6,-4],[3,7,6,-1,-8,-7,-8,-5,-4,-5,-4],[-7,2,9,-2,-6,-8,-8,-4,1,-8,1]],[[9,-5,10,9,10,3,3,-8,5,-10,9],[-9,-7,-5,1,10,-1,-3,5,-6,-8,-5],[-9,6,10,-8,5,4,-8,-8,-4,-8,-1],[7,-3,-1,10,-1,-10,6,6,9,-1,-7],[1,-9,4,-1,10,-3,8,1,-9,-10,3],[8,-10,-3,7,4,-3,-2,-2,-2,-10,-5],[-8,-10,-1,7,-6,3,10,-1,-6,-7,-9],[6,4,4,-4,4,-5,10,-5,-2,-1,-9],[3,-10,-6,-9,-7,-8,4,7,-3,3,-5],[8,1,-1,6,-1,-3,-7,-9,-5,1,9],[7,7,-7,10,5,-2,-7,-7,6,-2,-1],[7,5,-8,5,-4,-3,4,3,-10,3,3],[6,3,-9,10,-5,-2,8,9,-7,-8,5],[-10,8,-5,3,-1,7,10,10,-8,4,-5],[1,-8,6,9,-9,-8,-9,8,-2,-9,-2]]], dtype = "uint32")#candidate|831|(2, 15, 11)|const|uint32
var_832 = relay.var("var_832", dtype = "uint32", shape = (2, 15, 11))#candidate|832|(2, 15, 11)|var|uint32
bop_833 = relay.not_equal(const_831.astype('bool'), relay.reshape(var_832.astype('bool'), relay.shape_of(const_831))) # shape=(2, 15, 11)
output = bop_833
output2 = bop_833
func_839 = relay.Function([var_832,], output)
mod['func_839'] = func_839
mod = relay.transform.InferType()(mod)
var_840 = relay.var("var_840", dtype = "uint32", shape = (2, 15, 11))#candidate|840|(2, 15, 11)|var|uint32
output = func_839(var_840)
func_841 = relay.Function([var_840], output)
mutated_mod['func_841'] = func_841
mutated_mod = relay.transform.InferType()(mutated_mod)
var_969 = relay.var("var_969", dtype = "float64", shape = (11, 16, 5))#candidate|969|(11, 16, 5)|var|float64
uop_970 = relay.log2(var_969.astype('float64')) # shape=(11, 16, 5)
uop_976 = relay.sin(uop_970.astype('float32')) # shape=(11, 16, 5)
var_978 = relay.var("var_978", dtype = "float32", shape = (11, 16, 5))#candidate|978|(11, 16, 5)|var|float32
bop_979 = relay.equal(uop_976.astype('bool'), relay.reshape(var_978.astype('bool'), relay.shape_of(uop_976))) # shape=(11, 16, 5)
uop_982 = relay.atan(bop_979.astype('float32')) # shape=(11, 16, 5)
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
var_988 = relay.var("var_988", dtype = "float32", shape = (10, 64))#candidate|988|(10, 64)|var|float32
call_987 = func_113_call(relay.reshape(var_988.astype('float32'), [8, 5, 16]), relay.reshape(var_988.astype('float32'), [8, 5, 16]), )
call_989 = func_113_call(relay.reshape(var_988.astype('float32'), [8, 5, 16]), relay.reshape(var_988.astype('float32'), [8, 5, 16]), )
output = relay.Tuple([uop_982,call_987,var_988,])
output2 = relay.Tuple([uop_982,call_989,var_988,])
func_993 = relay.Function([var_969,var_978,var_988,], output)
mod['func_993'] = func_993
mod = relay.transform.InferType()(mod)
var_994 = relay.var("var_994", dtype = "float64", shape = (11, 16, 5))#candidate|994|(11, 16, 5)|var|float64
var_995 = relay.var("var_995", dtype = "float32", shape = (11, 16, 5))#candidate|995|(11, 16, 5)|var|float32
var_996 = relay.var("var_996", dtype = "float32", shape = (10, 64))#candidate|996|(10, 64)|var|float32
output = func_993(var_994,var_995,var_996,)
func_997 = relay.Function([var_994,var_995,var_996,], output)
mutated_mod['func_997'] = func_997
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1226 = relay.var("var_1226", dtype = "float32", shape = (15, 1, 3))#candidate|1226|(15, 1, 3)|var|float32
uop_1227 = relay.acosh(var_1226.astype('float32')) # shape=(15, 1, 3)
output = uop_1227
output2 = uop_1227
func_1230 = relay.Function([var_1226,], output)
mod['func_1230'] = func_1230
mod = relay.transform.InferType()(mod)
var_1231 = relay.var("var_1231", dtype = "float32", shape = (15, 1, 3))#candidate|1231|(15, 1, 3)|var|float32
output = func_1230(var_1231)
func_1232 = relay.Function([var_1231], output)
mutated_mod['func_1232'] = func_1232
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1273 = relay.var("var_1273", dtype = "int64", shape = (7, 12, 2))#candidate|1273|(7, 12, 2)|var|int64
var_1274 = relay.var("var_1274", dtype = "int64", shape = (7, 12, 2))#candidate|1274|(7, 12, 2)|var|int64
bop_1275 = relay.subtract(var_1273.astype('int64'), relay.reshape(var_1274.astype('int64'), relay.shape_of(var_1273))) # shape=(7, 12, 2)
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
var_1282 = relay.var("var_1282", dtype = "float32", shape = (640,))#candidate|1282|(640,)|var|float32
call_1281 = func_113_call(relay.reshape(var_1282.astype('float32'), [8, 5, 16]), relay.reshape(var_1282.astype('float32'), [8, 5, 16]), )
call_1283 = func_113_call(relay.reshape(var_1282.astype('float32'), [8, 5, 16]), relay.reshape(var_1282.astype('float32'), [8, 5, 16]), )
uop_1292 = relay.tan(bop_1275.astype('float64')) # shape=(7, 12, 2)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
const_1295 = relay.const([6,10,-3,7,8,-7,3,-8,1,-8,6,-10,9,-1,-4,-1,-8,-10,10,10,-1,2,5,8,10,3,-8,-2,10,5,-10,6,-7,-2,-6,-2,7,10,6,8,-8,5,-3,-4,10,8,-6,-9,1,-10,2,-3,-8,3,-2,3,3,5,2,-10,1,-4,10,-9,-5,-7,1,-7,4,-2,-2,-8,2,2,5,6,-10,2,-4,-3,10,-7,2,9,-6,2,-5,-5,-4,-10,-9,-4,9,-8,-6,3,1,-6,-5,-6,-5,1,1,-6,-10,-5,-5,7,6,6,-4,-8,10,-5,7,6,-2,-2,2,9,4,-3,2,2,3,9,-8,2,9,3,-1,-9,-7,-7,9,-2,-9,-4,3,6,-8,5,2,-4,-7,8,-5,4,-6,-10,6,-9,-7,3,-3,-7,-5,-4,2,-9,-4,-10,4,2,4,6,-6,-4,-10,-4,-9,3,-5,-1,7,-7,-7,-10,8,10,6,1,-10,4,3,4,-8,6,-6,-2,6,-3,-6,-3,-5,-8,8,-2,6,2,-3,-9,-5,-6,-1,3,-10,2,9,10,-8,-4,10,5,-3,3,-3,-9,-9,-1,-5,-2,9,9,-1,2,9,-6,-4,-5,7,-3,4,3,6,6,6,-6,-3,-5,-6,-4,4,6,-10,-5,10,-9,9,-8,6,8,-3,9,1,-10,10,4,1,-2,-10,8,-4,-2,1,-9,3,10,-2,-4,2,10,8,-8,3,-10,6,2,-8,-4,-4,7,10,7,-8,-7,-5,-6,2,-1,-3,-7,-10,-2,5,7,-1,-1,6,5,9,6,-10,6,-4,6,-8,10,-3,-8,8,-8,-2,10,-6,-1,10,6,8,1,-9,-3,3,6,-6,4,2,5,-2,-3], dtype = "uint32")#candidate|1295|(330,)|const|uint32
call_1294 = func_839_call(relay.reshape(const_1295.astype('uint32'), [2, 15, 11]))
call_1296 = func_839_call(relay.reshape(const_1295.astype('uint32'), [2, 15, 11]))
bop_1304 = relay.greater_equal(uop_1292.astype('bool'), relay.reshape(bop_1275.astype('bool'), relay.shape_of(uop_1292))) # shape=(7, 12, 2)
uop_1308 = relay.cosh(uop_1292.astype('float64')) # shape=(7, 12, 2)
output = relay.Tuple([call_1281,var_1282,call_1294,const_1295,bop_1304,uop_1308,])
output2 = relay.Tuple([call_1283,var_1282,call_1296,const_1295,bop_1304,uop_1308,])
func_1315 = relay.Function([var_1273,var_1274,var_1282,], output)
mod['func_1315'] = func_1315
mod = relay.transform.InferType()(mod)
mutated_mod['func_1315'] = func_1315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1315_call = mutated_mod.get_global_var('func_1315')
var_1317 = relay.var("var_1317", dtype = "int64", shape = (7, 12, 2))#candidate|1317|(7, 12, 2)|var|int64
var_1318 = relay.var("var_1318", dtype = "int64", shape = (7, 12, 2))#candidate|1318|(7, 12, 2)|var|int64
var_1319 = relay.var("var_1319", dtype = "float32", shape = (640,))#candidate|1319|(640,)|var|float32
call_1316 = func_1315_call(var_1317,var_1318,var_1319,)
output = call_1316
func_1320 = relay.Function([var_1317,var_1318,var_1319,], output)
mutated_mod['func_1320'] = func_1320
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1847 = relay.const([[[9,-9,8,1,8,-5,1,1,-10,8,3,9,-3,3,-3,7],[-10,-4,-6,6,-9,4,9,-5,-2,-7,6,7,6,1,-6,-1],[7,-5,-10,-10,3,10,9,-3,8,-8,-7,6,-4,1,7,6],[-9,6,3,-10,-10,-8,-6,2,10,8,2,9,3,7,3,-4],[6,2,6,8,10,4,9,-10,5,-6,-4,-4,8,6,5,-4],[10,4,7,1,-10,-5,-1,9,7,-3,-2,-9,-8,-4,7,-6],[3,4,-2,1,-9,10,-5,6,-4,-2,-5,1,-8,-6,10,-1],[-2,6,9,3,-8,-10,1,3,-6,-4,-6,4,-9,-8,-4,5],[-3,7,10,1,-4,1,6,3,-8,3,-3,7,-9,10,-5,9],[-5,1,-8,-5,5,8,-1,3,9,5,-3,1,-9,-7,-5,2]],[[5,-9,-10,-5,-2,6,5,3,5,3,10,4,-6,-4,7,5],[1,-5,10,-6,5,6,-1,-4,-4,-6,3,-4,9,4,-3,-8],[-2,-7,-2,-3,-5,9,-7,-2,-1,7,-8,-5,-8,5,-7,-6],[-5,-9,6,-6,-2,-6,-7,2,-7,-4,-10,4,-9,9,-3,2],[8,6,7,4,8,-10,6,-5,-1,-10,9,8,6,-1,-2,8],[6,5,-8,3,-7,-3,7,10,6,-10,7,-2,-7,1,-5,1],[-2,7,3,8,-4,-7,-10,10,6,-2,10,-5,6,-6,2,4],[-2,-6,10,-9,6,7,10,3,-7,-10,-8,2,10,4,-5,-5],[-9,6,-6,6,-8,1,10,7,-8,4,1,-7,6,-2,-10,-10],[10,8,8,2,-7,-7,7,-4,-10,-1,4,3,-1,-1,-3,-10]],[[6,3,-4,-3,7,9,1,-9,4,3,9,-8,-10,-3,-1,-8],[-3,-4,-5,9,4,-6,-3,-5,6,-5,-3,-5,-3,5,-3,2],[3,4,-2,8,3,10,-10,3,4,-10,10,-9,4,-8,7,5],[-7,-6,6,-4,9,-4,-2,2,2,10,-7,-6,2,-2,-5,7],[-7,-2,8,-1,3,-5,-4,-8,10,10,-6,-10,10,7,8,9],[8,10,9,-4,-9,-5,5,9,1,3,-8,8,-5,-5,-1,-10],[-8,-7,-2,-9,-10,-5,-10,-10,-6,10,8,-1,-5,9,3,-4],[-10,7,-2,6,-3,-6,-7,-5,1,-6,5,3,-6,-3,2,9],[10,7,-4,-1,3,-1,-4,-3,4,-6,-7,-7,1,-3,9,6],[-7,1,-7,-8,2,1,8,2,3,8,-7,4,-7,1,-8,5]],[[-4,-7,-1,-1,6,8,6,-5,6,-1,-10,-10,-4,5,2,5],[8,-6,7,-1,-9,-7,7,-4,-7,7,-1,-4,-2,5,1,-9],[-2,-10,-2,3,8,-4,4,-1,4,8,-8,8,-3,3,3,-5],[-7,-5,3,-8,-10,7,4,-4,-7,4,5,5,-7,2,-10,-6],[-1,6,10,7,8,-5,2,-1,-6,-4,8,-10,8,6,8,-5],[-4,-5,4,-8,5,-7,5,-8,4,1,-1,-9,-3,-7,7,-4],[-2,7,10,-10,-9,2,6,6,-1,-4,-9,1,7,7,-9,-5],[9,-9,-7,1,-6,1,-2,4,5,-6,-10,-8,-7,1,3,9],[7,-10,8,2,6,-8,10,2,9,-2,6,-5,3,1,1,-10],[9,-3,-3,1,-6,-6,10,-4,7,-7,5,6,-8,-4,6,-5]],[[5,-1,3,-6,10,9,-1,8,-10,10,7,-1,-10,3,-10,2],[8,-4,7,10,-3,7,4,1,-10,-7,-7,-1,-5,5,-3,-3],[-2,2,6,-7,2,4,-1,8,-7,8,5,-3,4,-10,-6,-9],[-1,-8,-4,-7,-10,4,5,3,-9,4,-10,6,6,4,8,-10],[6,-5,2,-9,-2,-6,-7,7,-9,1,9,-5,3,6,-3,-10],[4,-1,9,1,-5,8,-5,1,7,3,-9,-2,-8,-4,3,-1],[-3,-5,4,-4,4,-2,-7,3,5,2,4,8,10,-4,8,-4],[-8,5,-7,-3,-1,2,-10,-5,-8,-8,-1,-4,-8,8,4,9],[10,-5,3,10,5,-5,4,9,-7,4,-5,10,9,-3,7,4],[-6,-6,9,6,-7,-8,-10,-5,-7,-4,-9,8,-2,10,5,-7]]], dtype = "int16")#candidate|1847|(5, 10, 16)|const|int16
var_1848 = relay.var("var_1848", dtype = "int16", shape = (5, 10, 16))#candidate|1848|(5, 10, 16)|var|int16
bop_1849 = relay.equal(const_1847.astype('bool'), relay.reshape(var_1848.astype('bool'), relay.shape_of(const_1847))) # shape=(5, 10, 16)
bop_1854 = relay.logical_or(const_1847.astype('bool'), relay.reshape(bop_1849.astype('bool'), relay.shape_of(const_1847))) # shape=(5, 10, 16)
bop_1857 = relay.right_shift(bop_1854.astype('int64'), relay.reshape(var_1848.astype('int64'), relay.shape_of(bop_1854))) # shape=(5, 10, 16)
output = bop_1857
output2 = bop_1857
func_1876 = relay.Function([var_1848,], output)
mod['func_1876'] = func_1876
mod = relay.transform.InferType()(mod)
var_1877 = relay.var("var_1877", dtype = "int16", shape = (5, 10, 16))#candidate|1877|(5, 10, 16)|var|int16
output = func_1876(var_1877)
func_1878 = relay.Function([var_1877], output)
mutated_mod['func_1878'] = func_1878
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1880 = relay.const([[[True,False,False,True,True,True,False,False,True,True,True,False],[True,True,False,True,False,False,True,True,True,True,False,True]],[[False,True,True,False,True,False,False,False,False,True,False,True],[False,False,True,True,True,True,True,True,False,True,False,False]],[[True,False,True,False,True,True,False,True,True,True,True,False],[True,False,False,True,True,False,False,True,False,True,False,False]]], dtype = "bool")#candidate|1880|(3, 2, 12)|const|bool
const_1881 = relay.const([[[False,True,False,True,True,False,True,True,True,True,False,True],[True,True,False,False,True,False,True,True,False,False,False,True]],[[False,True,True,False,True,True,False,True,False,True,True,False],[True,False,True,True,True,False,False,True,True,False,True,False]],[[False,True,True,False,True,True,True,False,False,True,False,False],[False,False,True,True,True,False,True,True,False,False,False,False]]], dtype = "bool")#candidate|1881|(3, 2, 12)|const|bool
bop_1882 = relay.logical_and(const_1880.astype('bool'), relay.reshape(const_1881.astype('bool'), relay.shape_of(const_1880))) # shape=(3, 2, 12)
uop_1885 = relay.erf(bop_1882.astype('float32')) # shape=(3, 2, 12)
uop_1891 = relay.cos(uop_1885.astype('float32')) # shape=(3, 2, 12)
output = uop_1891
output2 = uop_1891
func_1893 = relay.Function([], output)
mod['func_1893'] = func_1893
mod = relay.transform.InferType()(mod)
mutated_mod['func_1893'] = func_1893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mutated_mod.get_global_var('func_1893')
call_1894 = func_1893_call()
output = call_1894
func_1895 = relay.Function([], output)
mutated_mod['func_1895'] = func_1895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_1921 = func_1893_call()
call_1922 = func_1893_call()
var_1924 = relay.var("var_1924", dtype = "float32", shape = (3, 2, 12))#candidate|1924|(3, 2, 12)|var|float32
bop_1925 = relay.greater(call_1921.astype('bool'), relay.reshape(var_1924.astype('bool'), relay.shape_of(call_1921))) # shape=(3, 2, 12)
bop_1928 = relay.greater(call_1922.astype('bool'), relay.reshape(var_1924.astype('bool'), relay.shape_of(call_1922))) # shape=(3, 2, 12)
output = bop_1925
output2 = bop_1928
func_1929 = relay.Function([var_1924,], output)
mod['func_1929'] = func_1929
mod = relay.transform.InferType()(mod)
var_1930 = relay.var("var_1930", dtype = "float32", shape = (3, 2, 12))#candidate|1930|(3, 2, 12)|var|float32
output = func_1929(var_1930)
func_1931 = relay.Function([var_1930], output)
mutated_mod['func_1931'] = func_1931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_1970 = func_1893_call()
call_1971 = func_1893_call()
func_1876_call = mod.get_global_var('func_1876')
func_1878_call = mutated_mod.get_global_var('func_1878')
var_1973 = relay.var("var_1973", dtype = "int16", shape = (800,))#candidate|1973|(800,)|var|int16
call_1972 = func_1876_call(relay.reshape(var_1973.astype('int16'), [5, 10, 16]))
call_1974 = func_1876_call(relay.reshape(var_1973.astype('int16'), [5, 10, 16]))
func_1929_call = mod.get_global_var('func_1929')
func_1931_call = mutated_mod.get_global_var('func_1931')
call_1975 = func_1929_call(relay.reshape(call_1970.astype('float32'), [3, 2, 12]))
call_1976 = func_1929_call(relay.reshape(call_1970.astype('float32'), [3, 2, 12]))
output = relay.Tuple([call_1970,call_1972,var_1973,call_1975,])
output2 = relay.Tuple([call_1971,call_1974,var_1973,call_1976,])
func_1979 = relay.Function([var_1973,], output)
mod['func_1979'] = func_1979
mod = relay.transform.InferType()(mod)
mutated_mod['func_1979'] = func_1979
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1980 = relay.var("var_1980", dtype = "int16", shape = (800,))#candidate|1980|(800,)|var|int16
func_1979_call = mutated_mod.get_global_var('func_1979')
call_1981 = func_1979_call(var_1980)
output = call_1981
func_1982 = relay.Function([var_1980], output)
mutated_mod['func_1982'] = func_1982
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2034 = relay.var("var_2034", dtype = "float64", shape = (2, 9, 2))#candidate|2034|(2, 9, 2)|var|float64
var_2035 = relay.var("var_2035", dtype = "float64", shape = (2, 9, 2))#candidate|2035|(2, 9, 2)|var|float64
bop_2036 = relay.divide(var_2034.astype('float64'), relay.reshape(var_2035.astype('float64'), relay.shape_of(var_2034))) # shape=(2, 9, 2)
uop_2044 = relay.acos(var_2035.astype('float64')) # shape=(2, 9, 2)
output = relay.Tuple([bop_2036,uop_2044,])
output2 = relay.Tuple([bop_2036,uop_2044,])
func_2061 = relay.Function([var_2034,var_2035,], output)
mod['func_2061'] = func_2061
mod = relay.transform.InferType()(mod)
mutated_mod['func_2061'] = func_2061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2061_call = mutated_mod.get_global_var('func_2061')
var_2063 = relay.var("var_2063", dtype = "float64", shape = (2, 9, 2))#candidate|2063|(2, 9, 2)|var|float64
var_2064 = relay.var("var_2064", dtype = "float64", shape = (2, 9, 2))#candidate|2064|(2, 9, 2)|var|float64
call_2062 = func_2061_call(var_2063,var_2064,)
output = call_2062
func_2065 = relay.Function([var_2063,var_2064,], output)
mutated_mod['func_2065'] = func_2065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_2150 = func_1893_call()
call_2151 = func_1893_call()
func_1230_call = mod.get_global_var('func_1230')
func_1232_call = mutated_mod.get_global_var('func_1232')
const_2169 = relay.const([2.571733,5.283495,5.210577,-9.854173,1.123774,-9.503190,3.457645,-9.805125,7.880929,-3.882822,-2.248932,8.727770,-6.852631,4.432450,8.274362,3.389523,-5.062198,-1.327715,-7.291369,1.628002,-2.722199,-9.550577,0.558291,2.296933,-5.224860,1.334570,2.868867,-3.014348,5.329394,8.643816,-7.180886,-3.656702,-7.318228,6.900919,6.484418,-9.782307,-8.270524,3.944221,-8.012967,-1.580687,-7.769647,4.713101,-9.379821,5.712923,-2.015835], dtype = "float32")#candidate|2169|(45,)|const|float32
call_2168 = func_1230_call(relay.reshape(const_2169.astype('float32'), [15, 1, 3]))
call_2170 = func_1230_call(relay.reshape(const_2169.astype('float32'), [15, 1, 3]))
func_2061_call = mod.get_global_var('func_2061')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_2173 = relay.const([2.637044,1.258504,5.176589,-1.875362,-1.917166,1.329186,-0.247720,2.256030,-6.373149,-2.531676,5.491075,-2.256623,0.587670,8.534321,8.253612,-9.583936,6.621314,7.546408,8.438834,8.494598,-4.558093,-5.323814,-7.669699,4.502397,-4.449319,3.473789,3.489186,7.888616,-0.529026,-8.837009,9.770599,-8.176196,-6.634357,1.694545,8.505570,3.781446], dtype = "float64")#candidate|2173|(36,)|const|float64
call_2172 = relay.TupleGetItem(func_2061_call(relay.reshape(const_2173.astype('float64'), [2, 9, 2]), relay.reshape(const_2173.astype('float64'), [2, 9, 2]), ), 0)
call_2174 = relay.TupleGetItem(func_2065_call(relay.reshape(const_2173.astype('float64'), [2, 9, 2]), relay.reshape(const_2173.astype('float64'), [2, 9, 2]), ), 0)
output = relay.Tuple([call_2150,call_2168,const_2169,call_2172,const_2173,])
output2 = relay.Tuple([call_2151,call_2170,const_2169,call_2174,const_2173,])
func_2183 = relay.Function([], output)
mod['func_2183'] = func_2183
mod = relay.transform.InferType()(mod)
mutated_mod['func_2183'] = func_2183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mutated_mod.get_global_var('func_2183')
call_2184 = func_2183_call()
output = call_2184
func_2185 = relay.Function([], output)
mutated_mod['func_2185'] = func_2185
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2196 = relay.TupleGetItem(func_2183_call(), 1)
call_2197 = relay.TupleGetItem(func_2185_call(), 1)
func_1979_call = mod.get_global_var('func_1979')
func_1982_call = mutated_mod.get_global_var('func_1982')
var_2200 = relay.var("var_2200", dtype = "int16", shape = (2, 400))#candidate|2200|(2, 400)|var|int16
call_2199 = relay.TupleGetItem(func_1979_call(relay.reshape(var_2200.astype('int16'), [800,])), 2)
call_2201 = relay.TupleGetItem(func_1982_call(relay.reshape(var_2200.astype('int16'), [800,])), 2)
bop_2202 = relay.left_shift(var_2200.astype('int8'), relay.reshape(call_2199.astype('int8'), relay.shape_of(var_2200))) # shape=(2, 400)
bop_2205 = relay.left_shift(var_2200.astype('int8'), relay.reshape(call_2201.astype('int8'), relay.shape_of(var_2200))) # shape=(2, 400)
func_1979_call = mod.get_global_var('func_1979')
func_1982_call = mutated_mod.get_global_var('func_1982')
call_2207 = relay.TupleGetItem(func_1979_call(relay.reshape(var_2200.astype('int16'), [800,])), 3)
call_2208 = relay.TupleGetItem(func_1982_call(relay.reshape(var_2200.astype('int16'), [800,])), 3)
bop_2211 = relay.minimum(bop_2202.astype('float32'), relay.reshape(var_2200.astype('float32'), relay.shape_of(bop_2202))) # shape=(2, 400)
bop_2214 = relay.minimum(bop_2205.astype('float32'), relay.reshape(var_2200.astype('float32'), relay.shape_of(bop_2205))) # shape=(2, 400)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
var_2223 = relay.var("var_2223", dtype = "uint32", shape = (330,))#candidate|2223|(330,)|var|uint32
call_2222 = func_839_call(relay.reshape(var_2223.astype('uint32'), [2, 15, 11]))
call_2224 = func_839_call(relay.reshape(var_2223.astype('uint32'), [2, 15, 11]))
uop_2234 = relay.erf(call_2222.astype('float64')) # shape=(2, 15, 11)
uop_2236 = relay.erf(call_2224.astype('float64')) # shape=(2, 15, 11)
output = relay.Tuple([call_2196,call_2207,bop_2211,var_2223,uop_2234,])
output2 = relay.Tuple([call_2197,call_2208,bop_2214,var_2223,uop_2236,])
func_2240 = relay.Function([var_2200,var_2223,], output)
mod['func_2240'] = func_2240
mod = relay.transform.InferType()(mod)
mutated_mod['func_2240'] = func_2240
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2240_call = mutated_mod.get_global_var('func_2240')
var_2242 = relay.var("var_2242", dtype = "int16", shape = (2, 400))#candidate|2242|(2, 400)|var|int16
var_2243 = relay.var("var_2243", dtype = "uint32", shape = (330,))#candidate|2243|(330,)|var|uint32
call_2241 = func_2240_call(var_2242,var_2243,)
output = call_2241
func_2244 = relay.Function([var_2242,var_2243,], output)
mutated_mod['func_2244'] = func_2244
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2246 = relay.var("var_2246", dtype = "float64", shape = (13, 2, 1))#candidate|2246|(13, 2, 1)|var|float64
uop_2247 = relay.cosh(var_2246.astype('float64')) # shape=(13, 2, 1)
func_2061_call = mod.get_global_var('func_2061')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_2252 = relay.const([-8.930872,3.499237,2.004856,-1.901324,8.071216,5.993792,-1.269489,-9.450588,3.240657,-0.497374,3.474175,3.550597,9.428468,9.584564,7.148881,-2.665966,-2.171028,7.429471,8.414409,-5.555543,-9.138850,2.323024,0.601357,7.403789,-2.979271,-1.443252,-0.482810,-9.078090,0.937026,-1.011406,-2.457064,0.912166,-3.184488,-6.659171,-4.193332,8.098426], dtype = "float64")#candidate|2252|(36,)|const|float64
call_2251 = relay.TupleGetItem(func_2061_call(relay.reshape(const_2252.astype('float64'), [2, 9, 2]), relay.reshape(const_2252.astype('float64'), [2, 9, 2]), ), 1)
call_2253 = relay.TupleGetItem(func_2065_call(relay.reshape(const_2252.astype('float64'), [2, 9, 2]), relay.reshape(const_2252.astype('float64'), [2, 9, 2]), ), 1)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
var_2256 = relay.var("var_2256", dtype = "uint32", shape = (330,))#candidate|2256|(330,)|var|uint32
call_2255 = func_839_call(relay.reshape(var_2256.astype('uint32'), [2, 15, 11]))
call_2257 = func_839_call(relay.reshape(var_2256.astype('uint32'), [2, 15, 11]))
bop_2269 = relay.power(uop_2247.astype('float64'), var_2256.astype('float64')) # shape=(13, 2, 330)
output = relay.Tuple([call_2251,const_2252,call_2255,bop_2269,])
output2 = relay.Tuple([call_2253,const_2252,call_2257,bop_2269,])
func_2278 = relay.Function([var_2246,var_2256,], output)
mod['func_2278'] = func_2278
mod = relay.transform.InferType()(mod)
mutated_mod['func_2278'] = func_2278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2278_call = mutated_mod.get_global_var('func_2278')
var_2280 = relay.var("var_2280", dtype = "float64", shape = (13, 2, 1))#candidate|2280|(13, 2, 1)|var|float64
var_2281 = relay.var("var_2281", dtype = "uint32", shape = (330,))#candidate|2281|(330,)|var|uint32
call_2279 = func_2278_call(var_2280,var_2281,)
output = call_2279
func_2282 = relay.Function([var_2280,var_2281,], output)
mutated_mod['func_2282'] = func_2282
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2353 = relay.var("var_2353", dtype = "float32", shape = (6, 4, 7))#candidate|2353|(6, 4, 7)|var|float32
uop_2354 = relay.cosh(var_2353.astype('float32')) # shape=(6, 4, 7)
output = relay.Tuple([uop_2354,])
output2 = relay.Tuple([uop_2354,])
func_2358 = relay.Function([var_2353,], output)
mod['func_2358'] = func_2358
mod = relay.transform.InferType()(mod)
var_2359 = relay.var("var_2359", dtype = "float32", shape = (6, 4, 7))#candidate|2359|(6, 4, 7)|var|float32
output = func_2358(var_2359)
func_2360 = relay.Function([var_2359], output)
mutated_mod['func_2360'] = func_2360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2408 = relay.TupleGetItem(func_2183_call(), 1)
call_2409 = relay.TupleGetItem(func_2185_call(), 1)
output = call_2408
output2 = call_2409
func_2444 = relay.Function([], output)
mod['func_2444'] = func_2444
mod = relay.transform.InferType()(mod)
output = func_2444()
func_2445 = relay.Function([], output)
mutated_mod['func_2445'] = func_2445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_2531 = func_2444_call()
call_2532 = func_2444_call()
func_1230_call = mod.get_global_var('func_1230')
func_1232_call = mutated_mod.get_global_var('func_1232')
call_2567 = func_1230_call(relay.reshape(call_2531.astype('float32'), [15, 1, 3]))
call_2568 = func_1230_call(relay.reshape(call_2531.astype('float32'), [15, 1, 3]))
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
const_2571 = relay.const([[-4.064907,-1.965103,9.998812,-8.081610,1.016313,-1.704425,5.641047,9.363260,4.320887,-4.782448,9.430050,-2.533321,-9.144710,6.978627,-1.406431,-9.922268,-0.232356,3.758699,-4.924288,8.892292,0.626495,3.718943,-2.527251,8.482743,-4.528725,7.670546,0.817784,-8.628729,3.853969,8.173624,0.008045,-1.080436,-9.638849,9.515094,2.387317,-6.149310,-8.432111,9.076199,-4.679584,9.991188,2.626362,-9.170416,-7.629171,-5.745315,0.327968,-1.844963,-6.835287,-9.779872,-1.520477,1.278429,-6.860027,5.891401,5.187813,4.118475,7.099342,-6.093528,2.775195,-0.901683,-3.015943,7.504868,-8.911021,-5.964693,-0.040605,2.210568],[-1.839593,7.388549,-7.335815,8.740602,2.828672,5.194578,1.066682,8.227670,7.321350,6.241762,2.153756,9.187131,-7.340172,-3.010507,-4.884318,0.966616,-4.148681,-2.815625,1.191021,-3.585283,-9.003441,-3.835001,-1.667460,7.615095,5.667618,4.133644,9.049552,-9.985605,-2.949140,3.171973,-5.337446,3.259252,5.264460,2.907056,9.421842,2.537117,8.767747,-3.987476,-5.547549,2.605890,-6.093342,-3.068706,7.086575,2.785944,4.493998,3.628642,1.217221,-1.343064,-7.699791,-3.428407,1.121452,5.179399,0.225907,-0.656449,3.677589,8.736368,-4.144413,-0.468624,-3.726149,3.276868,-5.371621,0.893201,2.215005,-1.659690],[4.656351,-3.472252,-3.870890,4.735316,5.222677,2.962669,-7.044880,-6.294105,-4.726560,-9.321648,-3.770167,-5.286345,-7.215249,-2.812222,8.414249,3.569688,5.812262,-1.324155,-6.843163,6.215721,1.727185,-6.342213,6.653948,6.566804,1.875617,-3.823729,2.246754,-4.522547,-2.132777,-4.002182,1.941163,-0.031247,3.996223,9.874955,1.866783,8.541395,1.351782,-9.779372,-7.038774,8.395983,1.893685,5.246832,-7.812996,2.189706,-6.097044,3.183798,8.120069,7.071113,-1.840998,-9.852148,1.911317,-0.746688,-0.260826,-8.219524,-7.565436,-6.462970,6.263066,0.774492,-8.952095,8.623309,-1.157034,-2.868769,-9.953021,-5.048951],[-6.348309,-6.113090,-9.769156,2.499592,5.936317,7.259921,1.810318,-6.579245,7.966033,-8.634086,-9.969498,-8.081348,-8.575631,-0.522945,-4.221691,3.277898,-6.431353,8.090327,2.585641,9.598917,-6.157025,-5.273524,-8.276576,-3.422317,-2.568805,2.646352,-8.689790,2.941757,2.766372,-7.628928,-9.603903,-8.918139,9.089452,5.254042,-1.660607,-4.709478,5.096445,-3.298382,9.931659,2.688496,-0.067924,-7.660936,3.983314,2.565565,7.146288,-6.131625,-8.084074,-1.042125,-0.328165,-4.933027,-4.556621,9.792076,3.749067,-9.327610,0.571265,5.299603,-8.253931,-3.123097,0.617981,-3.279880,1.789600,5.768531,-2.367854,-9.573808],[6.551540,3.881611,6.335746,-4.153967,4.278009,7.419238,-0.461274,-6.596503,-7.170698,-3.207266,-2.313200,-8.753220,-2.998215,5.015746,-1.172414,7.235958,-1.261247,2.904947,-4.773030,7.214313,-9.589657,-8.108031,5.075815,-1.058546,5.624443,5.482367,7.107745,-2.976112,3.099963,-7.463510,3.156596,-0.204287,7.358866,3.882059,3.603829,7.488369,9.651375,-7.288886,-4.269137,-0.171714,-3.018524,3.811543,1.665774,1.847799,-8.495658,-9.604321,5.245387,3.070845,7.535776,-8.158863,7.481649,-8.347341,1.943042,9.939362,1.202494,-4.378311,-5.946082,-0.765623,7.681996,-6.215151,7.294418,4.374263,0.936002,6.220789],[9.593273,4.331172,5.533723,7.798018,4.494232,-4.661170,-0.629026,-3.897773,7.519477,-4.683348,-2.757024,-0.127907,-4.975646,-7.368957,-4.524406,-9.294389,-2.514093,7.766264,9.290020,-2.729079,0.215417,-6.040950,3.579955,-4.239300,3.159605,8.999002,-5.989168,5.054196,0.140238,-3.469894,-1.917437,7.984019,4.469293,-9.768015,7.509335,2.741504,-0.305214,-4.174297,-9.521009,-6.651517,-0.781179,7.637662,6.539564,7.901821,-7.212154,-4.611075,-8.181475,8.262162,-8.966647,-4.056072,8.444132,6.290975,6.067792,8.281553,-0.048730,1.709891,-0.218557,7.211921,-1.355362,-5.525988,8.941043,4.352080,1.135659,1.105811],[-6.507572,1.066543,0.005079,0.426625,3.191375,-6.426852,-4.678919,-5.404392,-0.099650,-3.611249,-7.319292,5.009442,-8.495467,4.830817,-0.865033,9.724870,-4.115088,-2.223502,4.871278,5.841765,-9.708569,8.971829,5.857930,4.296044,8.520429,-5.286773,5.795934,9.776583,-3.548339,2.871247,2.326667,-0.214088,4.604752,8.053810,-3.873237,7.974973,-9.357112,-0.332268,-5.901850,6.908395,1.532671,5.147861,-0.275980,-5.565311,8.723120,0.584702,8.659450,0.129354,-6.352464,6.261265,4.133780,0.788377,2.162823,4.327308,-6.586654,-9.822229,3.444227,-0.675097,-1.635887,-9.222866,-2.816298,5.058907,3.708111,-0.958844],[1.376096,3.006982,4.221085,2.695993,-8.888239,-2.984636,1.489504,-3.861080,5.877149,-9.812304,-2.527375,3.798059,-9.823393,-1.804752,6.754240,0.881985,-4.663058,2.227005,-4.667035,9.216770,-5.111898,8.105018,-4.828343,-8.550315,-7.435102,7.352992,4.976475,7.814130,3.285274,-1.223365,-0.759153,-0.264205,-1.574488,-3.149129,-7.322077,3.496036,-7.840740,-4.370512,-6.865521,-3.658650,-2.409059,9.800237,-3.490031,4.273961,-7.831427,1.453320,-4.058772,-7.710236,8.160269,1.648660,-6.878995,-0.033925,5.614624,0.626457,6.337214,-9.973603,4.781717,-4.332133,-0.447115,-6.770069,3.331630,3.703676,3.349130,-7.014145],[6.150689,-2.748023,-5.024506,-4.740226,7.081131,9.998725,8.654716,-3.334385,-5.127886,-1.293356,5.055195,6.455296,-2.641408,-9.076029,-7.207382,1.873105,-3.553514,1.643086,-9.864089,-9.959209,4.016077,1.010888,2.170020,-8.748640,-6.983952,-3.988759,7.153001,-7.794554,-8.115647,5.774943,4.062749,-1.142325,-0.222146,-5.099786,9.575613,-8.511287,-1.519168,6.686334,-6.794806,3.243152,7.441475,-5.116028,-8.783245,-5.482565,6.015718,8.652647,-2.640775,-5.569976,-1.105167,-1.541190,1.893819,-7.568520,-6.059775,6.564615,7.347012,5.926190,-2.991968,8.276981,-2.797590,9.367688,5.800062,-9.599739,4.151324,-9.425493],[4.013508,5.568467,-4.296483,-9.290625,-5.006059,0.228974,1.678215,-0.697708,-9.693402,-2.873165,2.057679,-8.944174,-2.593825,3.667866,1.862673,9.644261,-7.393404,3.922863,5.022447,8.772584,2.337435,7.478895,8.259520,-4.007230,-6.375696,-1.388734,-4.735659,-8.010064,7.582928,-9.148232,-7.760135,6.708107,5.170020,6.787178,-6.345767,-1.897280,5.170962,-4.776365,8.053074,-6.573811,2.262353,8.673007,6.450276,7.240715,8.416303,0.037967,8.452474,-3.769588,0.147941,0.995437,-9.421095,1.471635,-8.421186,-9.800124,-2.051726,2.354441,8.636076,8.154205,-7.627794,8.229710,0.962693,5.503083,5.183385,7.680167]], dtype = "float32")#candidate|2571|(10, 64)|const|float32
call_2570 = func_113_call(relay.reshape(const_2571.astype('float32'), [8, 5, 16]), relay.reshape(const_2571.astype('float32'), [8, 5, 16]), )
call_2572 = func_113_call(relay.reshape(const_2571.astype('float32'), [8, 5, 16]), relay.reshape(const_2571.astype('float32'), [8, 5, 16]), )
uop_2577 = relay.sin(const_2571.astype('float64')) # shape=(10, 64)
uop_2590 = relay.exp(uop_2577.astype('float64')) # shape=(10, 64)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2592 = relay.TupleGetItem(func_2183_call(), 0)
call_2593 = relay.TupleGetItem(func_2185_call(), 0)
func_2240_call = mod.get_global_var('func_2240')
func_2244_call = mutated_mod.get_global_var('func_2244')
const_2598 = relay.const([6,-10,7,5,-4,7,10,4,8,-10,-4,-9,6,-9,7,-5,-5,3,3,-7,-9,-3,-8,4,4,-5,6,3,9,8,-5,-8,6,-4,9,5,8,6,-5,-1,6,-7,-1,-4,-2,8,-5,-8,8,-9,-3,-7,-2,-6,5,6,-3,-2,3,5,-10,1,-9,-6,10,4,-2,6,-3,-1,-8,-10,9,-5,9,8,-3,5,-9,-7,-8,4,-1,6,-3,-4,1,1,-5,-2,6,-2,-8,-1,7,8,8,-7,-4,-2,-9,7,-8,2,7,-8,4,4,-6,-1,-10,2,2,-6,2,3,-4,-1,-1,8,7,-4,5,-4,-2,7,5,1,-9,-2,-7,-2,5,7,-8,-7,10,-7,9,7,-8,5,-4,-9,-5,1,5,-7,9,-8,9,-4,-7,6,-2,-7,-7,-4,-1,1,-3,2,-10,-10,-10,-5,-4,-8,10,4,6,2,8,-4,8,-6,10,9,-6,-8,-7,-5,-4,9,8,-5,9,-10,3,7,-9,-2,-3,-8,10,-5,-9,-8,-7,6,-4,-2,6,1,3,-1,-1,3,4,2,5,2,10,-8,1,-4,5,-10,-7,-2,-9,5,6,5,-7,-5,-4,10,-1,3,-2,-8,3,8,9,2,-5,-9,5,2,-8,-6,-5,10,-3,-7,2,-4,3,4,-3,1,3,8,1,10,6,4,10,-7,-9,-2,2,-5,-7,9,7,-6,10,-8,4,10,2,9,-2,-9,-1,-1,4,-7,6,10,6,4,2,6,-10,3,-4,7,9,4,-6,4,-2,-2,-9,-2,10,2,9,-5,-6,-2,3,4,-3,5,-5,1,1,6,6,6,3,8,-6,3,-3,10,-2,9,7,5,4,9,-9,-7,2,-1,-1,-9,3,-9,-4,-4,5,4,-9,4,-6,1,8,10,-9,-7,1,-7,7,-3,-7,9,-2,4,3,5,10,5,-3,-10,-8,-5,2,-5,10,-1,-5,-8,3,-8,-9,4,-8,9,-5,-6,-5,-2,-4,3,-5,10,-5,6,-10,4,9,3,8,1,-1,6,7,-3,7,5,-10,-3,-5,5,-5,-7,9,-2,-3,10,-9,10,-4,-4,-10,-4,-6,-7,10,-6,-3,9,-4,8,-3,1,-7,-5,5,4,2,8,-9,-9,-7,3,-10,1,-1,-1,-9,6,7,-9,-5,-10,4,-5,10,-1,-6,8,-5,10,-10,-2,-5,-7,10,-5,-2,9,2,9,7,1,-4,-1,-10,5,-4,-8,-5,-1,4,9,-2,10,-4,6,-10,-5,7,-3,7,-4,-7,1,-9,7,10,-9,-6,-6,9,2,-10,2,-2,-2,-3,3,-1,1,7,-5,-4,1,3,-2,1,2,10,-7,-10,-5,-5,4,3,6,-3,-8,5,-9,-1,1,-5,-1,8,9,-9,1,-5,10,10,7,-6,2,-8,-10,-10,-9,5,-1,-2,-10,-7,4,10,9,9,3,2,-1,-6,9,3,2,2,10,4,-2,5,-2,-10,-4,6,8,-5,-10,9,7,-9,-9,-2,4,3,6,4,4,8,4,-5,2,1,-1,3,-4,6,-5,4,-6,-7,-6,10,-4,-6,-2,3,3,8,-6,-1,-5,-4,9,2,-7,-8,10,1,-8,-4,-1,6,1,-7,5,9,-7,2,1,1,-5,-10,-9,-10,-9,-9,1,4,9,1,9,6,3,2,-4,-3,-2,-3,-4,-9,-7,-3,6,-2,-9,3,-3,4,8,1,8,10,-4,2,6,-1,2,1,1,2,-6,-10,5,4,-1,-5,8,-1,-8,10,-4,7,7,3,9,10,2,4,-5,9,3,6,-1,4,10,3,7,10,-8,-5,-8,-2,-6,-6,-3,6,-2,9,-7,-3,7,1,-8,1,1,2,-1,-10,1,6,2,1,-4,7,3,10,-8,5,1,-1,-10,-4,7,7,-9,-3,-7,-4,5,4,-9,-10,-7,-2,-1,-3,-6,-3,10,-3,5,9,-10,-4,-2,3,-5,10,-7,2,-7,-2,-1,-10,-7,9,8,-3,-9,-3,5,4,-8,4,9,5,3,1,-4,-5,3,-2,-2,-9,-10,-1,8,-7,-2,-4,-6,-8,-8,-3,9,1,3,-3,8,5,-4,-5,4,3,-2,8,7,7,5,8,-9], dtype = "int16")#candidate|2598|(800,)|const|int16
var_2599 = relay.var("var_2599", dtype = "uint32", shape = (330,))#candidate|2599|(330,)|var|uint32
call_2597 = relay.TupleGetItem(func_2240_call(relay.reshape(const_2598.astype('int16'), [2, 400]), relay.reshape(var_2599.astype('uint32'), [330,]), ), 4)
call_2600 = relay.TupleGetItem(func_2244_call(relay.reshape(const_2598.astype('int16'), [2, 400]), relay.reshape(var_2599.astype('uint32'), [330,]), ), 4)
var_2609 = relay.var("var_2609", dtype = "float64", shape = (10, 64))#candidate|2609|(10, 64)|var|float64
bop_2610 = relay.minimum(uop_2590.astype('float32'), relay.reshape(var_2609.astype('float32'), relay.shape_of(uop_2590))) # shape=(10, 64)
bop_2616 = relay.bitwise_and(bop_2610.astype('int8'), relay.reshape(uop_2590.astype('int8'), relay.shape_of(bop_2610))) # shape=(10, 64)
func_1230_call = mod.get_global_var('func_1230')
func_1232_call = mutated_mod.get_global_var('func_1232')
call_2623 = func_1230_call(relay.reshape(call_2567.astype('float32'), [15, 1, 3]))
call_2624 = func_1230_call(relay.reshape(call_2567.astype('float32'), [15, 1, 3]))
var_2625 = relay.var("var_2625", dtype = "float64", shape = (10, 64))#candidate|2625|(10, 64)|var|float64
bop_2626 = relay.floor_mod(uop_2577.astype('float32'), relay.reshape(var_2625.astype('float32'), relay.shape_of(uop_2577))) # shape=(10, 64)
output = relay.Tuple([call_2531,call_2567,call_2570,call_2592,call_2597,const_2598,var_2599,bop_2616,call_2623,bop_2626,])
output2 = relay.Tuple([call_2532,call_2568,call_2572,call_2593,call_2600,const_2598,var_2599,bop_2616,call_2624,bop_2626,])
func_2649 = relay.Function([var_2599,var_2609,var_2625,], output)
mod['func_2649'] = func_2649
mod = relay.transform.InferType()(mod)
var_2650 = relay.var("var_2650", dtype = "uint32", shape = (330,))#candidate|2650|(330,)|var|uint32
var_2651 = relay.var("var_2651", dtype = "float64", shape = (10, 64))#candidate|2651|(10, 64)|var|float64
var_2652 = relay.var("var_2652", dtype = "float64", shape = (10, 64))#candidate|2652|(10, 64)|var|float64
output = func_2649(var_2650,var_2651,var_2652,)
func_2653 = relay.Function([var_2650,var_2651,var_2652,], output)
mutated_mod['func_2653'] = func_2653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_2662 = func_1893_call()
call_2663 = func_1893_call()
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2672 = relay.TupleGetItem(func_2183_call(), 2)
call_2673 = relay.TupleGetItem(func_2185_call(), 2)
func_2649_call = mod.get_global_var('func_2649')
func_2653_call = mutated_mod.get_global_var('func_2653')
var_2676 = relay.var("var_2676", dtype = "uint32", shape = (330,))#candidate|2676|(330,)|var|uint32
const_2677 = relay.const([-4.122206,-6.984925,-4.060024,0.097872,5.284869,8.677456,-4.295938,1.882286,8.480473,9.719921,-9.226208,-0.763014,-2.828266,8.385573,0.819323,3.031918,-8.568074,-8.878079,2.386651,-2.018708,-3.093917,-4.597424,-9.827031,3.725040,-9.359721,-1.314864,-5.530408,-4.446121,7.052457,-6.779755,-1.335508,-0.266716,9.645732,1.369046,1.666597,-9.234906,-9.551606,-3.185007,-2.987953,-6.680205,-7.293222,0.190991,1.322626,8.471310,8.616221,2.267693,2.989430,-5.753013,-6.632158,9.260159,5.897180,2.999954,-6.612229,-7.797697,1.530714,-1.020334,-7.833665,-4.455218,4.546982,-0.675218,4.783034,-1.637548,9.074389,1.047904,-5.381248,4.653000,-2.440533,6.815896,-7.937432,8.029727,-2.777409,-4.536535,-4.207140,-2.123221,-9.085377,-9.712835,-4.447111,0.807797,-4.742200,3.157374,7.866281,-5.882410,9.886234,3.664538,-4.176935,6.288281,-6.202654,8.375418,-8.843082,-7.392889,-8.951306,-4.337676,5.525059,-4.430802,3.422056,-1.956319,0.143185,-8.671901,8.558628,-7.607119,7.998858,-2.540537,3.794176,-8.775133,-4.876357,1.599176,7.429567,3.931267,1.099810,-2.906094,-3.530683,7.515213,-3.716535,-1.698054,2.299269,7.619963,4.886078,-2.374760,9.532154,-6.085726,9.994460,-8.957967,-0.101287,7.892001,7.364908,-3.460441,9.201930,2.565309,7.904451,0.959035,6.866683,4.535015,-3.682147,2.268445,-9.399836,6.293736,8.253680,1.767058,-3.652623,1.595156,-2.553916,8.113826,-5.732752,5.705275,-6.709694,-6.481372,2.805613,-9.062738,-7.287409,7.769977,-4.210929,-2.651012,-4.893205,4.159391,3.371463,9.195720,-0.459775,7.595358,8.421255,-4.308385,2.218115,4.798694,7.592445,-7.541509,-9.230716,-9.930870,9.032502,-5.368842,-2.848093,-7.496695,4.847674,-4.815879,-3.819097,-2.855615,-2.468063,4.589282,6.020356,6.949508,6.619284,-2.800666,6.963231,-8.107215,-2.342251,4.686680,-0.535047,-5.619322,6.514718,5.835530,-2.056880,2.742308,-1.548265,-4.923788,-1.852991,-3.280321,9.076433,1.694261,-1.381747,3.270447,-0.424746,6.115822,-8.941247,-3.342597,-6.142629,8.146238,0.602014,-7.584723,-5.509401,-3.763905,-5.138429,-9.091444,2.368315,-4.498773,9.549790,-6.252460,-5.530213,-8.342834,3.650351,-4.199193,-7.862935,-1.569160,5.453201,8.898528,6.597187,-4.443421,7.893742,-4.604234,-8.265235,-7.280598,-0.646328,9.065192,-8.289759,-3.828325,7.357956,-0.084456,-4.046459,8.496620,7.444421,3.282204,-5.657350,-1.559444,-4.427199,2.192837,9.205357,-4.131058,-8.071277,3.086406,1.646920,6.464327,-7.641010,-0.924134,-7.524104,-3.388369,5.641160,2.566999,7.343071,1.189452,-8.948336,-6.053750,-0.205022,6.464661,6.010230,0.100719,-1.716180,3.165829,-9.305515,-1.207067,1.568129,-5.397342,-6.706505,9.047537,0.319715,-5.369386,6.806557,-8.613429,4.239398,-5.460137,-2.715343,-8.636420,-8.534506,0.126049,4.546178,-7.714121,9.546719,1.453440,-1.098520,9.803074,6.261005,0.577008,6.644284,-4.002348,4.547051,3.212764,2.014599,6.133786,7.003246,-6.303920,-8.598645,3.585634,-3.103720,5.143897,7.626887,-5.282464,-4.701259,1.720730,2.843240,4.853573,9.258282,-9.863491,-8.225784,-5.940618,3.644937,-0.859855,2.506760,6.538013,4.004502,-3.693966,1.562778,2.769692,-4.169494,0.797343,2.733578,6.140625,4.647978,3.258594,6.471616,5.963831,-0.636577,-1.404152,-9.684919,3.168295,-9.623614,-4.392468,2.897970,-1.811401,3.663037,3.446730,-5.742154,0.223286,8.220663,6.021291,-9.108852,6.760375,-3.091796,6.616840,5.189395,-3.558692,-2.287525,6.367392,2.522958,-7.907225,-4.806911,1.886041,-7.614989,-3.179628,3.178491,-1.907733,5.620064,-9.254061,3.439082,-2.874872,3.751840,-2.536163,9.667680,9.991247,6.928092,5.061452,9.418499,-5.752149,7.523208,3.434182,-5.375381,8.471860,0.584719,-2.545479,1.534287,3.611476,2.304193,-3.594194,-7.550993,2.720979,1.979192,3.427149,0.936247,-5.546878,-9.511557,6.031354,4.219374,-4.696617,7.497062,1.302829,5.085388,1.019566,9.796175,-3.085332,2.464008,0.976634,-4.531220,4.792996,0.202356,5.727155,-8.428864,-5.598984,8.771138,-2.642735,1.594779,8.954795,3.062449,-6.979571,-2.922610,-7.868328,-4.791638,7.570789,-1.984129,2.274372,-4.215539,9.166562,5.705738,3.074550,0.760579,4.759998,5.145690,5.433993,7.701877,3.782551,-3.193420,3.395615,-0.343903,-0.404921,-6.339393,-1.865120,-7.720704,7.071424,1.953657,-2.840111,-2.759939,-4.305444,-1.383408,-8.103849,2.480579,1.416027,5.893941,-0.779082,1.995739,-9.642779,-9.533668,2.794403,5.259656,7.567370,2.887282,8.979751,7.174379,9.376721,5.347138,-9.188597,-1.410028,0.887637,-4.396502,0.903019,-8.539803,1.778159,-8.840486,5.217171,5.021572,-5.280929,-5.115931,4.507959,2.656217,0.944046,-4.098906,2.254951,5.968026,0.804432,7.952989,-2.198973,-0.142751,-4.111914,-5.695808,-2.774893,-2.859554,-6.121336,-7.095164,6.390126,-5.385956,2.328437,-8.223364,9.241101,5.268137,8.184428,3.104627,-8.091743,-4.976590,-8.022185,-0.847530,-4.043979,-4.322194,0.255950,-3.275748,-3.520803,4.713277,-8.503439,3.240083,2.513247,-7.382880,8.573543,-6.777932,4.118061,-7.438769,8.367644,9.993354,-6.419111,-4.746930,-1.275781,-6.384909,-0.531480,-3.017910,0.526797,-8.283233,-4.852918,1.225303,6.015493,5.380123,-3.508352,-4.033786,-5.232777,-5.066300,7.363815,-7.644765,9.192021,0.240229,-3.044016,-4.332891,4.426469,1.831732,0.025411,1.222312,-3.459058,-1.516861,-7.900592,8.466937,-8.401106,3.137370,-0.397925,5.124046,-3.423598,9.782979,1.406607,-1.376884,0.005540,-4.848859,9.810281,7.100255,6.800037,-5.029114,-0.123590,-9.476619,2.299459,3.296855,-6.498878,-5.037592,0.970226,4.069224,5.726815,7.509727,4.080122,-0.795003,5.253322,1.813837,3.339338,-3.076346,6.575823,-3.809110,0.183633,-5.908887,-2.706709,-8.906285,6.277519,-9.202154,-0.409082,0.271382,-6.697578,-0.307865,6.945043,-9.155661,8.268667,-4.361187,1.433373,-2.657730,-8.124603,-8.984316,5.895828,-3.332263,3.865292,2.685282,-2.940596,6.671698,-3.156907,-4.400957,4.242580,-1.837769,-5.562021,4.058366,9.789749,-0.211022,2.823460,4.673130,5.855098,7.224868,-3.835741,-4.730366,5.712752,5.189618,6.145815,7.754264,-5.173949,-7.703364,-8.066695,7.411711,7.312459,-8.951911,-5.354232,0.790457,7.357624,-8.826230,6.686748,9.910796,8.360391,1.469908,-4.889268,5.229146,-3.421967,0.168720,-3.377057,0.501065,-2.810476,-0.503745,3.256927,1.700586,-4.141160,-4.531782,-0.065290], dtype = "float64")#candidate|2677|(640,)|const|float64
call_2675 = relay.TupleGetItem(func_2649_call(relay.reshape(var_2676.astype('uint32'), [330,]), relay.reshape(const_2677.astype('float64'), [10, 64]), relay.reshape(const_2677.astype('float64'), [10, 64]), ), 3)
call_2678 = relay.TupleGetItem(func_2653_call(relay.reshape(var_2676.astype('uint32'), [330,]), relay.reshape(const_2677.astype('float64'), [10, 64]), relay.reshape(const_2677.astype('float64'), [10, 64]), ), 3)
output = relay.Tuple([call_2662,call_2672,call_2675,var_2676,const_2677,])
output2 = relay.Tuple([call_2663,call_2673,call_2678,var_2676,const_2677,])
func_2706 = relay.Function([var_2676,], output)
mod['func_2706'] = func_2706
mod = relay.transform.InferType()(mod)
var_2707 = relay.var("var_2707", dtype = "uint32", shape = (330,))#candidate|2707|(330,)|var|uint32
output = func_2706(var_2707)
func_2708 = relay.Function([var_2707], output)
mutated_mod['func_2708'] = func_2708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2728 = relay.var("var_2728", dtype = "float32", shape = ())#candidate|2728|()|var|float32
var_2729 = relay.var("var_2729", dtype = "float32", shape = (11, 11, 7))#candidate|2729|(11, 11, 7)|var|float32
bop_2730 = relay.floor_mod(var_2728.astype('float32'), var_2729.astype('float32')) # shape=(11, 11, 7)
output = relay.Tuple([bop_2730,])
output2 = relay.Tuple([bop_2730,])
func_2735 = relay.Function([var_2728,var_2729,], output)
mod['func_2735'] = func_2735
mod = relay.transform.InferType()(mod)
mutated_mod['func_2735'] = func_2735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2735_call = mutated_mod.get_global_var('func_2735')
var_2737 = relay.var("var_2737", dtype = "float32", shape = ())#candidate|2737|()|var|float32
var_2738 = relay.var("var_2738", dtype = "float32", shape = (11, 11, 7))#candidate|2738|(11, 11, 7)|var|float32
call_2736 = func_2735_call(var_2737,var_2738,)
output = call_2736
func_2739 = relay.Function([var_2737,var_2738,], output)
mutated_mod['func_2739'] = func_2739
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_2758 = func_1893_call()
call_2759 = func_1893_call()
uop_2773 = relay.atanh(call_2758.astype('float32')) # shape=(3, 2, 12)
uop_2775 = relay.atanh(call_2759.astype('float32')) # shape=(3, 2, 12)
func_2649_call = mod.get_global_var('func_2649')
func_2653_call = mutated_mod.get_global_var('func_2653')
const_2796 = relay.const([-9,-7,3,3,-1,-4,8,10,7,10,10,5,8,-3,-3,-3,-5,5,6,-5,-10,-9,1,8,1,8,-5,-1,2,10,-6,-10,-3,-8,-2,4,-4,-10,4,4,5,7,7,-3,-3,6,5,-2,-10,5,-7,-6,4,7,6,-1,3,1,5,-3,-8,-10,7,-1,-6,3,-7,-4,6,9,3,3,8,-10,-9,-5,-3,9,-9,-9,9,8,-10,9,4,-6,-7,-4,2,-2,-6,7,2,-1,10,-5,9,-5,6,5,-3,6,1,-7,-4,5,5,-1,-1,7,-2,8,-8,2,-10,-3,-1,3,8,6,-8,-4,-4,10,-9,5,-1,-7,-10,2,-8,-1,1,3,-3,-3,-2,5,-6,-3,6,-8,-3,-6,4,2,-3,4,-6,-5,-8,3,-7,-9,-5,-8,10,-8,1,-5,3,10,8,-2,-1,-7,-7,-2,-9,7,-1,7,-3,4,10,-10,5,-9,-3,1,-9,-4,7,1,7,1,7,1,2,5,-5,5,6,-4,4,-3,-4,-9,3,8,-10,-9,-7,-6,-6,-3,9,-10,1,-3,1,-9,-5,7,-10,9,4,-8,8,1,6,-4,1,9,-10,-10,10,-6,-10,4,-8,10,3,-2,-4,9,-7,7,7,-10,8,-7,-9,-5,6,7,-4,-5,-8,2,-9,2,-1,2,4,-6,3,-3,4,9,7,5,6,-10,6,6,2,1,-8,-5,8,7,3,-2,-7,-9,1,-8,4,3,2,7,-7,9,-3,8,-6,-3,-4,-5,9,7,-8,9,5,-3,-9,-2,9,2,10,5,4,2,-4,10,3,-5,4,-4,-6,-9,7,3,-7,-8,-6,10,3,-9,2,-2,9,-7,-3,-4,-10,-4,-6,-3], dtype = "uint32")#candidate|2796|(330,)|const|uint32
var_2797 = relay.var("var_2797", dtype = "float64", shape = (640,))#candidate|2797|(640,)|var|float64
call_2795 = relay.TupleGetItem(func_2649_call(relay.reshape(const_2796.astype('uint32'), [330,]), relay.reshape(var_2797.astype('float64'), [10, 64]), relay.reshape(var_2797.astype('float64'), [10, 64]), ), 2)
call_2798 = relay.TupleGetItem(func_2653_call(relay.reshape(const_2796.astype('uint32'), [330,]), relay.reshape(var_2797.astype('float64'), [10, 64]), relay.reshape(var_2797.astype('float64'), [10, 64]), ), 2)
output = relay.Tuple([uop_2773,call_2795,const_2796,var_2797,])
output2 = relay.Tuple([uop_2775,call_2798,const_2796,var_2797,])
func_2804 = relay.Function([var_2797,], output)
mod['func_2804'] = func_2804
mod = relay.transform.InferType()(mod)
var_2805 = relay.var("var_2805", dtype = "float64", shape = (640,))#candidate|2805|(640,)|var|float64
output = func_2804(var_2805)
func_2806 = relay.Function([var_2805], output)
mutated_mod['func_2806'] = func_2806
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2824 = relay.TupleGetItem(func_2183_call(), 4)
call_2825 = relay.TupleGetItem(func_2185_call(), 4)
func_2358_call = mod.get_global_var('func_2358')
func_2360_call = mutated_mod.get_global_var('func_2360')
var_2827 = relay.var("var_2827", dtype = "float32", shape = (168,))#candidate|2827|(168,)|var|float32
call_2826 = relay.TupleGetItem(func_2358_call(relay.reshape(var_2827.astype('float32'), [6, 4, 7])), 0)
call_2828 = relay.TupleGetItem(func_2360_call(relay.reshape(var_2827.astype('float32'), [6, 4, 7])), 0)
output = relay.Tuple([call_2824,call_2826,var_2827,])
output2 = relay.Tuple([call_2825,call_2828,var_2827,])
func_2832 = relay.Function([var_2827,], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
var_2833 = relay.var("var_2833", dtype = "float32", shape = (168,))#candidate|2833|(168,)|var|float32
output = func_2832(var_2833)
func_2834 = relay.Function([var_2833], output)
mutated_mod['func_2834'] = func_2834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_2903 = func_1893_call()
call_2904 = func_1893_call()
func_2735_call = mod.get_global_var('func_2735')
func_2739_call = mutated_mod.get_global_var('func_2739')
const_2909 = relay.const(0.894142, dtype = "float32")#candidate|2909|()|const|float32
const_2910 = relay.const([[-3.814746],[2.241677],[-3.953799],[9.674872],[6.907119],[6.483419],[2.244267],[9.928630],[8.156557],[1.947157],[-9.396167],[3.770152],[-8.350708],[-6.892408],[-8.435564],[0.431313],[-0.666094],[-8.964430],[-7.073601],[9.263626],[-9.193403],[-7.936367],[2.049815],[0.201006],[-7.245603],[6.185314],[3.663509],[-0.902958],[3.476431],[-3.162036],[7.471433],[9.506777],[-0.627476],[-3.628116],[4.482828],[-1.702641],[-0.518591],[4.273021],[-1.705477],[-6.560442],[-0.230507],[4.952464],[-3.046300],[7.373588],[7.721847],[-8.756872],[4.213341],[-4.935985],[4.519276],[7.459595],[6.349520],[7.836913],[-4.069428],[9.936132],[3.788646],[-0.794120],[5.127108],[0.526856],[4.506482],[-9.801877],[-7.777913],[-6.786375],[-1.752037],[0.342847],[5.168249],[-6.260532],[-4.763619],[6.502989],[-8.953505],[6.768601],[-1.755304],[5.262361],[5.865172],[-1.156740],[3.732454],[8.423283],[4.883319],[-9.019468],[5.865712],[5.681945],[-7.183560],[7.184029],[8.538185],[9.100609],[8.145165],[4.151712],[-1.655327],[-1.360531],[7.373194],[4.809230],[3.467369],[-8.371356],[-8.271679],[-9.228001],[-2.272801],[-4.153177],[7.887692],[7.588919],[-2.703004],[-9.167341],[0.672858],[-7.073746],[3.381515],[-1.562122],[4.224454],[1.394295],[-9.482590],[7.427080],[-3.127834],[-1.729346],[3.820697],[8.570935],[-4.478738],[-5.768507],[-0.695508],[5.768040],[-1.896377],[8.532187],[-7.569356],[8.489568],[3.935620],[-0.444606],[-7.524600],[-3.144937],[3.569799],[-7.597343],[-1.116363],[8.875197],[-4.051408],[7.788201],[-4.683374],[2.747521],[-9.510478],[-9.694924],[-6.215924],[-1.770705],[2.762080],[1.306989],[-9.738494],[-5.546695],[7.578485],[5.920053],[0.532998],[-6.397158],[-5.875800],[-8.140143],[-8.901668],[4.005424],[-4.113606],[0.020880],[0.221145],[6.606729],[-3.108263],[3.698321],[-5.280213],[-9.059233],[-9.779308],[5.106163],[-5.627605],[3.392095],[-8.998515],[-0.819591],[4.322909],[8.331289],[1.343672],[-4.431546],[9.232317],[4.625405],[2.546472],[-2.411560],[0.307420],[7.692746],[-8.049402],[7.575386],[-2.709944],[2.221454],[-2.388848],[-4.777705],[-5.731414],[0.530408],[-1.363589],[-1.409803],[4.031792],[-2.691779],[-4.328305],[4.989909],[3.314709],[1.764106],[0.517599],[5.638971],[-7.084146],[-6.501214],[-8.928309],[-6.177576],[0.419349],[-0.888760],[-5.879794],[3.316560],[1.468130],[-9.298277],[-4.763593],[2.317027],[-7.324544],[-4.694778],[7.999703],[3.062815],[-4.468980],[-7.611461],[-5.198012],[9.340340],[-9.583658],[-0.880021],[0.864192],[2.550958],[8.182370],[-5.352143],[6.518339],[9.798560],[7.208140],[3.801790],[2.448112],[-2.870479],[6.687215],[-4.484266],[6.736779],[6.310854],[-3.964030],[-4.831001],[4.516769],[-1.082038],[7.369037],[-9.946301],[-8.688219],[-0.940679],[0.770492],[-0.458928],[1.576175],[0.733189],[0.618028],[-8.287852],[7.283845],[-6.936779],[8.728417],[5.591366],[-0.291751],[8.008161],[1.590713],[-8.155257],[-4.260044],[6.759331],[8.505507],[-1.834375],[-7.991149],[9.664247],[-5.855659],[-1.133010],[7.770432],[2.559505],[-2.942657],[2.872952],[-9.435448],[-1.707253],[-3.391398],[2.730481],[-9.736219],[1.632819],[-9.623088],[-8.006912],[6.494698],[-7.372183],[6.775804],[9.029479],[8.138705],[-7.416483],[-4.080456],[8.010960],[-9.929107],[-4.844230],[-3.283050],[7.506894],[-1.803443],[-7.692831],[3.573431],[8.592954],[-6.569180],[-7.297693],[-7.890699],[-4.973904],[-1.436179],[2.109928],[-8.575923],[9.928814],[3.056486],[-5.614338],[5.303718],[-8.429555],[-8.834723],[-8.947494],[8.692625],[-7.337665],[0.632776],[5.822046],[-3.017577],[3.052194],[-9.837138],[3.435321],[1.305207],[-6.432351],[-5.629865],[9.164037],[-8.942620],[6.542592],[-5.715939],[-1.248006],[2.539688],[-3.017565],[1.360027],[5.728383],[3.664245],[-1.527592],[8.261004],[7.599268],[-7.324275],[1.919126],[-2.110356],[-1.656374],[-5.888356],[7.625558],[6.802860],[-8.885722],[-0.705099],[1.842290],[2.563853],[4.111663],[-0.350719],[-5.578492],[-9.542437],[-9.633647],[4.763585],[6.178608],[-7.860084],[5.467007],[-8.222150],[-0.860760],[-0.908396],[-9.366940],[1.644692],[2.440548],[-7.066733],[3.107751],[-7.209245],[2.861533],[4.161192],[-5.759742],[3.594141],[-8.605287],[2.256981],[0.025780],[-4.193358],[-2.421233],[-7.312504],[9.365520],[-3.184205],[-9.638603],[-3.626464],[7.236736],[-7.753392],[3.315179],[7.057653],[-6.502467],[2.501827],[-9.493864],[-6.261752],[-3.629603],[9.446016],[-0.074065],[-5.760281],[4.673498],[-7.953149],[7.708763],[-9.027930],[8.640648],[7.804917],[-6.808606],[-2.501604],[-7.832299],[-1.388130],[2.750412],[-2.311939],[2.425820],[-2.465210],[0.201468],[-6.102994],[1.441700],[9.744676],[9.519497],[-2.431955],[-3.891339],[1.543185],[-2.823840],[5.750647],[0.040518],[5.768296],[0.868622],[2.578936],[-8.599749],[-2.236879],[-9.173412],[-5.526836],[1.104160],[-8.080080],[6.614992],[6.170841],[1.752314],[4.024804],[4.654025],[-5.276097],[-9.504113],[1.885131],[4.368980],[-1.679445],[-4.613653],[0.745826],[5.425612],[-8.923950],[8.190068],[6.515898],[6.546022],[-0.863992],[1.827826],[-8.408244],[1.443458],[-5.526579],[2.491430],[7.659692],[-8.050273],[-2.886661],[-1.664012],[5.885586],[1.480396],[-9.784738],[-7.422468],[-2.455264],[-9.068372],[-7.793758],[-5.920174],[-0.937575],[9.010772],[8.169282],[-2.574243],[2.619092],[-6.958636],[2.401608],[-1.837602],[5.140237],[1.499013],[-2.891739],[1.555732],[8.277475],[-6.616118],[-1.080428],[3.000518],[-1.237336],[3.379457],[8.127621],[-5.750980],[-9.645096],[-2.308232],[3.230684],[-8.649018],[-5.606878],[-9.221342],[0.897516],[8.819452],[3.364059],[6.413235],[-6.992450],[1.255373],[2.872389],[-4.619531],[-8.341405],[-0.769395],[-5.509368],[8.427908],[2.189666],[-9.533780],[9.576418],[-8.906026],[-5.872136],[5.752558],[3.055230],[3.612646],[1.641120],[-2.565277],[9.553366],[1.971448],[9.905030],[-8.421182],[-6.861822],[6.951514],[0.380609],[-5.005521],[-9.414467],[-4.776863],[-5.114288],[9.563935],[-5.970243],[-7.505930],[0.803791],[-6.706885],[0.160090],[-1.405171],[2.535805],[-8.396702],[-1.439334],[2.447555],[2.423942],[-6.504940],[8.387162],[2.729598],[2.219427],[1.234477],[1.932040],[7.120084],[0.395786],[-4.764173],[-4.846639],[4.717853],[3.505764],[5.265025],[-7.702159],[-6.896459],[-5.912751],[9.779300],[4.728449],[-5.858374],[5.455178],[-2.658384],[6.745976],[6.035750],[4.778670],[4.200333],[8.143858],[-1.581297],[5.238051],[-9.149163],[-2.224720],[7.624898],[-8.222955],[-0.542653],[1.204830],[-1.298103],[1.043276],[-0.756583],[-0.142061],[0.840535],[1.508462],[7.924227],[5.329697],[9.109942],[-0.443619],[-7.373861],[-9.988797],[8.645148],[2.372643],[-1.581694],[-7.413210],[7.901550],[0.923141],[-0.525886],[-6.916569],[-3.672097],[4.535845],[-3.824532],[7.378405],[3.668441],[1.180320],[-2.792544],[3.016081],[-7.428604],[-2.035270],[-2.744654],[6.866897],[-3.379173],[3.712870],[9.328130],[-2.594359],[2.362544],[1.726835],[-3.758353],[3.310437],[-0.006904],[-6.387135],[2.481234],[0.227755],[-0.535701],[-6.043277],[-4.551824],[-2.136260],[5.882474],[-2.682766],[0.845469],[-5.907983],[-9.793756],[-4.534731],[-2.539960],[-2.551626],[3.479937],[4.402674],[-3.245452],[-9.676986],[-0.535101],[9.349898],[2.138005],[1.508891],[7.070614],[2.185963],[-4.688852],[5.033239],[4.143084],[-0.519246],[-7.710325],[6.604169],[1.992462],[-6.859067],[3.758199],[-2.708953],[8.867409],[-0.986589],[8.232228],[2.527571],[3.450802],[-3.401582],[-7.892864],[-7.517400],[5.157117],[4.115670],[9.370998],[7.806686],[-8.809050],[5.728929],[6.486115],[1.228027],[4.593049],[6.111065],[-3.510337],[-0.832630],[2.816902],[2.530872],[-8.056947],[9.424357],[-5.795192],[8.026963],[3.256867],[-5.394703],[-2.942285],[8.125677],[8.285696],[1.860797],[0.390874],[-7.812982],[9.287578],[4.838089],[0.183034],[8.812269],[8.770087],[4.088155],[0.788745],[9.152432],[-7.175772],[-6.260833],[8.940073],[-4.408168],[4.988323],[-3.037437],[-2.149040],[-2.871131],[1.113855],[-3.988885],[-6.929481],[-2.751964],[-2.183096],[-5.360542],[9.482548],[5.159834],[9.073327],[-3.712003],[2.849543],[-8.171606],[-3.307945],[1.243227],[7.266565],[0.024458],[-2.540078],[5.209937],[8.557899],[-4.676685],[1.194022],[3.870566],[-7.468186],[-8.316982],[6.102303],[0.020799],[9.512543],[2.239104],[-1.057717],[-4.669294],[-8.301694],[-2.480957],[7.609260],[8.838367],[6.761106],[5.960252],[-7.778477],[8.983342],[8.989617],[9.712625],[0.309426],[6.968086],[-4.993699],[-8.568793],[-1.360607],[-0.860058],[-2.408387],[1.697620],[-2.144886],[-1.224337],[-9.889533],[-1.087136],[8.949476],[9.735541],[-9.791508],[2.612562],[9.033217],[-7.401856],[2.361126],[-2.373591],[-4.886726],[-4.748423],[3.876555],[-8.024635],[-0.305294],[-6.301916],[-9.702329],[-4.600024],[-8.105612],[-4.844970],[-6.675007],[-3.874789],[1.555160],[7.381476],[-0.975658],[-1.756852],[-8.924617],[0.062664],[-2.051831],[6.599486],[6.800256],[3.207589],[-5.908060],[5.690601],[3.186641],[4.782826],[8.909740],[-5.799553],[6.132650],[8.920517],[3.249460],[-3.282363],[-7.404043],[-9.824800],[4.206893],[7.218800],[8.906971],[4.696288],[-3.248853],[-0.330168],[-6.994216],[1.899033],[-9.259059],[-5.525682],[3.323536],[2.969097],[7.314637],[-7.685982],[1.168219],[-9.614622],[-1.561690],[5.967630],[-8.033590],[-2.196346],[1.002266],[1.350258],[-6.790695],[2.672190],[-0.063029],[-3.007708],[9.905190],[-1.136093],[1.243855],[-1.244143],[6.541797],[-6.470117],[8.331181],[6.118343],[-5.706730],[-0.208523],[2.115641],[8.249082],[4.833796],[-2.674880],[8.792714],[8.787044],[-6.317537],[6.177243],[7.415781],[-2.186077],[1.642421],[-1.062123],[2.859669],[-7.260430],[0.033319],[8.624433],[-5.611211],[5.771838],[-9.621102],[6.412624],[-6.194413],[-9.291701],[5.167669],[3.962347],[-1.331814],[7.773990],[-7.548254],[-5.869633],[-3.348937],[1.394956],[0.701813],[-2.923971],[8.384339],[4.667837],[2.932458],[5.263402],[-7.415011],[-9.768411],[-8.379925],[-6.096784]], dtype = "float32")#candidate|2910|(847, 1)|const|float32
call_2908 = relay.TupleGetItem(func_2735_call(relay.reshape(const_2909.astype('float32'), []), relay.reshape(const_2910.astype('float32'), [11, 11, 7]), ), 0)
call_2911 = relay.TupleGetItem(func_2739_call(relay.reshape(const_2909.astype('float32'), []), relay.reshape(const_2910.astype('float32'), [11, 11, 7]), ), 0)
output = relay.Tuple([call_2903,call_2908,const_2909,const_2910,])
output2 = relay.Tuple([call_2904,call_2911,const_2909,const_2910,])
func_2912 = relay.Function([], output)
mod['func_2912'] = func_2912
mod = relay.transform.InferType()(mod)
output = func_2912()
func_2913 = relay.Function([], output)
mutated_mod['func_2913'] = func_2913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_2947 = relay.TupleGetItem(func_2912_call(), 1)
call_2948 = relay.TupleGetItem(func_2913_call(), 1)
output = call_2947
output2 = call_2948
func_2949 = relay.Function([], output)
mod['func_2949'] = func_2949
mod = relay.transform.InferType()(mod)
output = func_2949()
func_2950 = relay.Function([], output)
mutated_mod['func_2950'] = func_2950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_2965 = relay.TupleGetItem(func_2183_call(), 4)
call_2966 = relay.TupleGetItem(func_2185_call(), 4)
func_2358_call = mod.get_global_var('func_2358')
func_2360_call = mutated_mod.get_global_var('func_2360')
const_2968 = relay.const([-5.592642,7.669850,2.802710,-0.873455,-1.419920,6.430484,-6.630002,-3.480763,9.847770,0.629875,-9.977920,-8.276413,1.524462,-7.463392,8.182437,-2.845485,9.564484,-0.808671,-0.772627,6.531896,2.608649,-6.130637,-7.663933,8.283680,3.609333,2.109498,5.179865,-0.798972,2.646679,7.360980,8.950793,-9.302460,7.401693,-2.695319,4.220056,-5.499929,-0.145807,-1.259052,-0.647410,1.257640,5.870685,5.798907,-7.121103,8.196831,-6.495700,-2.328474,-7.946609,3.780766,-2.978653,-0.071347,0.173776,-1.730728,5.585752,-5.058238,-0.755001,4.004966,-9.647340,-9.681772,6.012458,-3.833092,-8.147178,3.570858,-5.804474,3.797755,-3.950575,-1.633409,-1.791937,-1.638908,-2.187428,1.324488,-4.319880,-0.459507,0.484721,3.319693,-3.382913,1.284214,0.639748,1.342117,8.769250,-1.966351,-5.337955,7.730053,3.190566,6.441029,-8.903035,-6.683563,7.761665,-9.537655,3.617961,4.812878,8.480198,-1.371022,-0.366039,-9.745352,-2.831296,1.788468,-5.330595,-8.029048,-1.895471,9.997870,-0.321545,2.467392,-0.182441,8.559027,-0.137013,1.777447,8.473806,-9.545077,3.106283,0.615095,8.055888,5.412339,3.259230,0.893441,3.213837,-3.221589,-4.822198,2.780104,8.785576,-9.483682,-0.417772,-3.046284,3.462938,2.340808,3.883245,9.603993,7.217966,-4.408843,-1.392935,1.086025,-1.663047,6.460142,5.132886,2.222303,4.445575,-3.592169,5.822220,9.938542,9.908585,-3.324589,8.453891,6.665032,-4.877447,9.772150,7.365252,-5.947186,2.176148,-3.907484,-5.884331,4.723478,5.080055,3.944727,-5.154445,-0.113053,1.504532,5.613975,-5.324513,-9.701182,-8.879992,1.889750,-8.961570,-7.452173,9.981286,-3.086358,-1.899864,-7.629296,-4.122029,0.579990], dtype = "float32")#candidate|2968|(168,)|const|float32
call_2967 = relay.TupleGetItem(func_2358_call(relay.reshape(const_2968.astype('float32'), [6, 4, 7])), 0)
call_2969 = relay.TupleGetItem(func_2360_call(relay.reshape(const_2968.astype('float32'), [6, 4, 7])), 0)
output = relay.Tuple([call_2965,call_2967,const_2968,])
output2 = relay.Tuple([call_2966,call_2969,const_2968,])
func_2975 = relay.Function([], output)
mod['func_2975'] = func_2975
mod = relay.transform.InferType()(mod)
mutated_mod['func_2975'] = func_2975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2975_call = mutated_mod.get_global_var('func_2975')
call_2976 = func_2975_call()
output = call_2976
func_2977 = relay.Function([], output)
mutated_mod['func_2977'] = func_2977
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2999 = relay.var("var_2999", dtype = "uint64", shape = (13, 11, 8))#candidate|2999|(13, 11, 8)|var|uint64
const_3000 = relay.const([[[-2,-4,7,-5,-10,-9,6,-8],[8,6,-1,-8,5,3,-6,9],[-9,5,4,2,2,3,-1,8],[-6,-1,-9,7,9,-4,-2,-5],[6,8,-1,-6,-10,-2,-3,-2],[-7,7,2,-7,-6,9,6,9],[-5,3,-7,-8,-1,10,3,2],[-5,-5,5,-1,5,-8,-2,-4],[-4,-3,-8,-8,3,1,-9,7],[4,-4,-4,-9,-3,-9,-4,3],[9,-8,9,6,-5,-10,-1,-10]],[[-7,-7,9,9,3,-10,2,-4],[9,10,10,-10,2,-9,6,-2],[-4,-3,5,9,-9,-2,10,4],[9,-9,-9,-4,-8,-5,-2,7],[-6,-1,2,6,8,-4,5,10],[-3,5,-8,2,9,8,4,9],[6,10,9,3,5,6,7,-6],[-4,10,-7,6,10,9,-3,-6],[8,9,4,-7,-9,-9,-10,7],[-7,4,1,-1,-7,-7,-9,-1],[10,6,-2,-3,5,-7,8,-9]],[[-3,8,-4,-5,1,3,-6,7],[-4,10,-6,-7,4,6,-10,-8],[7,-6,-6,5,-4,9,5,-8],[1,-5,2,7,-9,-9,-9,1],[2,10,8,-5,-6,-4,2,-9],[9,-9,-7,-6,-1,-7,-1,-8],[-8,9,4,10,-10,-2,-4,3],[-5,6,-9,10,7,-2,-6,1],[9,-9,6,4,2,8,6,-3],[6,-5,-2,-6,-4,9,-9,3],[-10,10,2,4,9,-3,-5,-6]],[[-4,7,7,6,6,-1,-4,2],[9,-2,7,8,-7,-10,7,-5],[-6,8,-8,5,8,8,2,-7],[-5,3,-4,9,-2,-4,-5,-2],[3,-4,-4,6,9,-5,-7,2],[-1,3,6,7,-1,8,1,-6],[-2,9,3,8,-1,-3,-7,-8],[1,-4,-5,6,-3,3,6,2],[4,-4,5,9,4,4,-6,-10],[6,-6,6,-1,8,-4,-5,-4],[6,-6,-9,8,-6,7,-5,-10]],[[2,3,10,6,10,-4,-6,4],[8,4,-4,3,5,5,-8,2],[-1,-7,-1,-10,-2,-5,-3,-2],[-6,8,-1,1,2,7,-1,9],[5,6,10,-6,8,-3,-10,-4],[5,8,7,-3,7,9,10,3],[-6,3,3,-10,-3,-6,10,-1],[3,1,1,9,6,6,-7,-1],[-8,-1,-6,-3,-4,1,-8,8],[-2,-1,5,-10,9,-6,7,-3],[4,5,7,-8,-7,-6,3,-6]],[[5,7,7,-8,5,5,1,-6],[-2,-6,1,1,-5,10,-10,-5],[4,-4,1,-9,6,-6,-2,4],[5,6,-6,-1,3,-10,-10,8],[7,4,4,4,-9,-6,5,8],[2,6,-8,-10,2,4,7,3],[3,-3,3,6,-8,-3,-6,4],[3,-7,-9,-4,9,3,9,1],[5,1,-9,-10,-1,1,5,7],[-3,3,-3,5,2,-9,3,-2],[-2,-6,2,-10,-2,2,4,7]],[[6,-1,4,3,3,-6,-10,5],[-3,-4,1,-10,3,-10,1,-4],[9,8,-3,-9,10,3,8,-3],[10,-8,1,6,9,-1,-5,-1],[-2,8,-7,4,-4,1,-6,3],[-2,-9,-10,-7,10,1,-4,-8],[1,-2,2,-10,-2,8,-5,-3],[3,-2,-4,-2,-8,10,7,-6],[5,-9,-5,-5,7,-6,4,1],[-3,2,3,-4,1,1,-3,6],[-9,4,3,-3,-3,-3,2,6]],[[-9,3,-4,-1,2,-5,-10,-10],[6,-5,3,9,8,-3,-8,-6],[-9,6,-7,-10,-10,-3,-6,3],[6,10,5,5,3,-6,9,5],[2,-1,10,-9,4,5,4,1],[6,-1,-3,6,6,-7,5,-1],[5,7,3,8,-7,-9,-2,5],[4,-9,-4,-2,-7,5,3,7],[10,-3,-2,-2,7,2,-2,5],[2,-2,7,7,5,5,8,5],[-8,2,-3,-8,8,8,-8,-5]],[[-9,5,10,-9,3,-4,8,8],[-10,-5,-5,-5,-7,-2,-8,-3],[3,-2,-1,-10,6,5,3,-1],[4,-10,-1,3,-8,10,1,2],[3,-6,8,1,10,-10,-9,-8],[7,3,2,5,-8,-7,-8,2],[-4,8,-4,6,4,9,-6,-8],[6,10,-5,10,-10,2,-6,1],[-3,-2,9,3,5,-9,-2,4],[6,7,-1,-5,-2,10,1,5],[-4,3,6,-9,1,-2,4,-8]],[[-3,4,-2,4,-7,-9,8,4],[-3,-5,4,-10,1,5,-9,8],[10,6,2,-5,4,7,7,2],[-8,-1,-1,9,-2,-9,-9,-4],[10,2,-8,9,10,4,7,9],[4,-10,-10,7,5,-4,-3,-5],[6,5,6,-8,1,-4,-1,-6],[3,-8,-6,5,-10,-8,-7,8],[-2,-9,-10,-5,-2,-1,-3,6],[6,-1,10,6,4,7,-8,-5],[9,-1,5,-1,-8,-8,1,9]],[[1,-4,5,-2,-5,-2,-1,5],[3,10,3,-4,4,-4,-7,4],[4,-8,-7,9,9,-7,8,-2],[-8,-10,-2,4,6,2,-2,3],[4,4,-4,-5,4,-5,4,3],[10,6,8,9,-9,-9,-7,8],[8,5,7,-6,4,3,-9,-1],[-2,4,-9,3,-3,-1,-7,-2],[-5,8,6,4,7,9,6,6],[7,5,2,5,10,-6,7,5],[-6,5,-9,4,-6,4,3,9]],[[2,7,2,1,-10,-3,6,10],[-1,6,3,7,-2,-3,-3,-6],[-6,8,7,-4,-8,-3,-4,-6],[7,8,1,1,-8,-10,-9,-5],[1,7,-5,-4,-7,-7,9,6],[5,-8,-9,2,5,10,8,1],[1,5,8,-10,6,3,-3,3],[-5,6,10,-3,8,3,1,5],[-1,-9,-10,1,10,-3,-7,3],[-5,-9,-7,-4,-8,-2,10,-10],[-10,9,1,7,-7,4,-7,7]],[[-8,-1,-1,-1,-1,-5,-2,3],[3,1,-5,5,9,8,-8,9],[3,10,-4,-10,-8,9,9,2],[-5,8,-1,4,4,-7,-8,8],[-6,-5,3,-5,-2,1,-6,5],[-3,-3,-8,8,2,-6,-2,4],[-5,8,6,-9,10,10,-10,-9],[-2,9,3,3,3,-6,4,-2],[-6,-6,-6,1,-4,1,-9,-9],[5,2,7,3,-3,-4,-6,-5],[-9,-7,8,8,-2,-8,-9,4]]], dtype = "uint64")#candidate|3000|(13, 11, 8)|const|uint64
bop_3001 = relay.equal(var_2999.astype('bool'), relay.reshape(const_3000.astype('bool'), relay.shape_of(var_2999))) # shape=(13, 11, 8)
output = relay.Tuple([bop_3001,])
output2 = relay.Tuple([bop_3001,])
func_3004 = relay.Function([var_2999,], output)
mod['func_3004'] = func_3004
mod = relay.transform.InferType()(mod)
mutated_mod['func_3004'] = func_3004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3005 = relay.var("var_3005", dtype = "uint64", shape = (13, 11, 8))#candidate|3005|(13, 11, 8)|var|uint64
func_3004_call = mutated_mod.get_global_var('func_3004')
call_3006 = func_3004_call(var_3005)
output = call_3006
func_3007 = relay.Function([var_3005], output)
mutated_mod['func_3007'] = func_3007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3076 = func_2949_call()
call_3077 = func_2949_call()
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_3081 = relay.TupleGetItem(func_2183_call(), 0)
call_3082 = relay.TupleGetItem(func_2185_call(), 0)
output = relay.Tuple([call_3076,call_3081,])
output2 = relay.Tuple([call_3077,call_3082,])
func_3090 = relay.Function([], output)
mod['func_3090'] = func_3090
mod = relay.transform.InferType()(mod)
output = func_3090()
func_3091 = relay.Function([], output)
mutated_mod['func_3091'] = func_3091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3130 = func_2949_call()
call_3131 = func_2949_call()
output = relay.Tuple([call_3130,])
output2 = relay.Tuple([call_3131,])
func_3149 = relay.Function([], output)
mod['func_3149'] = func_3149
mod = relay.transform.InferType()(mod)
mutated_mod['func_3149'] = func_3149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3149_call = mutated_mod.get_global_var('func_3149')
call_3150 = func_3149_call()
output = call_3150
func_3151 = relay.Function([], output)
mutated_mod['func_3151'] = func_3151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3211 = func_2949_call()
call_3212 = func_2949_call()
func_2358_call = mod.get_global_var('func_2358')
func_2360_call = mutated_mod.get_global_var('func_2360')
const_3221 = relay.const([8.720681,-7.474317,0.779039,-5.051790,-8.816081,5.663834,-1.648630,5.661511,4.833714,2.363620,8.398821,6.452638,5.863438,1.283958,7.591553,3.792735,-8.069788,-7.184445,-0.671449,6.835806,-0.592458,3.067022,6.285992,-7.978501,-2.644378,-1.960367,9.363771,-6.861526,-3.381900,1.444262,-7.861034,-7.486122,3.244218,-0.249119,-8.555559,-1.849250,-8.869474,3.614501,-7.069156,-5.959609,6.607280,-4.308232,-6.885714,-6.776506,-2.642249,-2.629120,-5.583941,1.718325,-2.604469,7.954311,-0.506271,0.747684,-6.458874,-1.778319,-0.252495,7.408046,6.696413,7.274364,1.119293,6.405369,8.665780,-6.399766,-3.346760,0.600649,-9.892727,0.339364,-8.169616,3.440978,-9.836125,1.705001,0.704193,-4.236315,9.602959,-4.775219,7.788623,-1.430611,-8.577797,1.501956,3.602192,9.289186,3.357009,-1.112381,4.039959,-0.006349,3.952874,-1.849511,3.760667,-8.625097,-4.262162,3.328883,-1.834132,3.593320,-6.094842,1.577224,7.485552,3.172053,-1.269228,3.883017,-3.562210,2.008879,6.156541,-2.221728,-5.739702,0.978709,6.958830,8.845704,3.319385,-7.344774,5.866334,4.346739,-8.215718,1.278712,-9.436324,-8.541718,9.983370,-6.034191,-7.430367,7.800906,1.061000,4.625668,1.624488,-3.594901,2.310286,-1.163138,9.596884,-6.633381,4.195133,-9.087926,-2.401797,-9.367944,-5.493759,-3.073535,4.189443,2.780243,2.446581,1.300273,4.011133,7.778936,8.475163,9.668591,2.290675,-2.449907,-4.636027,-2.462596,-3.322142,-4.996478,9.552680,2.245938,-8.750570,-9.025795,6.407349,-1.181958,4.189630,-3.011286,6.215329,4.532713,1.356746,7.684470,-8.033721,-4.928686,-0.238420,5.393446,6.182888,-1.523605,-5.750261,4.438621,7.154628,-6.617697], dtype = "float32")#candidate|3221|(168,)|const|float32
call_3220 = relay.TupleGetItem(func_2358_call(relay.reshape(const_3221.astype('float32'), [6, 4, 7])), 0)
call_3222 = relay.TupleGetItem(func_2360_call(relay.reshape(const_3221.astype('float32'), [6, 4, 7])), 0)
uop_3227 = relay.asinh(call_3220.astype('float32')) # shape=(6, 4, 7)
uop_3229 = relay.asinh(call_3222.astype('float32')) # shape=(6, 4, 7)
output = relay.Tuple([call_3211,const_3221,uop_3227,])
output2 = relay.Tuple([call_3212,const_3221,uop_3229,])
func_3230 = relay.Function([], output)
mod['func_3230'] = func_3230
mod = relay.transform.InferType()(mod)
output = func_3230()
func_3231 = relay.Function([], output)
mutated_mod['func_3231'] = func_3231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2975_call = mod.get_global_var('func_2975')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_3246 = relay.TupleGetItem(func_2975_call(), 0)
call_3247 = relay.TupleGetItem(func_2977_call(), 0)
output = call_3246
output2 = call_3247
func_3252 = relay.Function([], output)
mod['func_3252'] = func_3252
mod = relay.transform.InferType()(mod)
mutated_mod['func_3252'] = func_3252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3252_call = mutated_mod.get_global_var('func_3252')
call_3253 = func_3252_call()
output = call_3253
func_3254 = relay.Function([], output)
mutated_mod['func_3254'] = func_3254
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_3272 = func_2949_call()
call_3273 = func_2949_call()
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_3276 = relay.TupleGetItem(func_2183_call(), 2)
call_3277 = relay.TupleGetItem(func_2185_call(), 2)
func_1230_call = mod.get_global_var('func_1230')
func_1232_call = mutated_mod.get_global_var('func_1232')
call_3290 = func_1230_call(relay.reshape(call_3276.astype('float32'), [15, 1, 3]))
call_3291 = func_1230_call(relay.reshape(call_3276.astype('float32'), [15, 1, 3]))
output = relay.Tuple([call_3272,call_3276,call_3290,])
output2 = relay.Tuple([call_3273,call_3277,call_3291,])
func_3318 = relay.Function([], output)
mod['func_3318'] = func_3318
mod = relay.transform.InferType()(mod)
mutated_mod['func_3318'] = func_3318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3318_call = mutated_mod.get_global_var('func_3318')
call_3319 = func_3318_call()
output = call_3319
func_3320 = relay.Function([], output)
mutated_mod['func_3320'] = func_3320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_3323 = func_3252_call()
call_3324 = func_3252_call()
output = call_3323
output2 = call_3324
func_3331 = relay.Function([], output)
mod['func_3331'] = func_3331
mod = relay.transform.InferType()(mod)
mutated_mod['func_3331'] = func_3331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mutated_mod.get_global_var('func_3331')
call_3332 = func_3331_call()
output = call_3332
func_3333 = relay.Function([], output)
mutated_mod['func_3333'] = func_3333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3351 = relay.var("var_3351", dtype = "uint64", shape = (14, 14, 4))#candidate|3351|(14, 14, 4)|var|uint64
const_3352 = relay.const([[[-10,-4,3,-8],[-9,-2,-7,-9],[-8,5,-7,1],[1,6,8,1],[3,7,-5,3],[-5,-4,3,-5],[-4,-9,5,-2],[5,8,-6,-3],[4,-4,-7,5],[-2,-6,4,-8],[-4,-9,8,5],[-1,-9,2,5],[2,-7,6,2],[-2,-3,-2,7]],[[9,-4,9,-2],[-2,9,-3,-2],[-6,3,-4,8],[-3,-4,-3,10],[-7,10,-6,6],[5,4,10,4],[-6,7,-2,-5],[5,10,10,-9],[6,1,-4,-10],[4,9,-1,-1],[-10,8,-3,-8],[4,-8,8,9],[9,-6,1,-3],[1,9,5,-10]],[[8,6,10,-2],[2,9,7,5],[-10,-8,6,-3],[3,8,6,10],[5,7,-10,2],[-9,3,6,2],[7,-6,1,-10],[3,-4,-6,-3],[2,8,9,3],[8,-3,-2,-2],[-5,3,-8,-2],[-1,-10,-1,-7],[2,-5,3,10],[4,8,8,-8]],[[-8,9,-4,-9],[-5,9,1,-9],[9,-6,3,-4],[7,4,3,6],[-3,-9,6,-1],[4,-9,5,-8],[3,7,-9,-5],[-4,-2,3,8],[5,-4,-3,1],[2,-2,9,1],[5,-8,-10,1],[-3,9,-10,-3],[-4,5,-9,-7],[-6,10,-1,9]],[[-9,-2,-1,-3],[3,10,10,-10],[8,4,-2,10],[9,7,-9,8],[3,-8,-1,9],[-4,-1,10,-1],[-7,-6,3,10],[6,-4,2,-6],[1,9,5,-8],[-7,-3,2,-7],[-8,-9,1,-3],[-9,-3,-8,-7],[-10,-3,-6,-4],[-1,10,-3,-2]],[[2,-2,-3,9],[1,-2,-8,9],[7,5,-2,6],[7,5,-5,-1],[-10,-9,7,6],[7,-8,-9,4],[-9,-9,7,-2],[-3,8,-8,4],[-1,3,-10,-7],[-9,1,2,-3],[-4,1,8,-10],[2,9,-7,10],[-8,6,-3,5],[8,9,-3,10]],[[-5,-1,-4,-1],[8,-8,5,-1],[-2,10,-9,-9],[-1,6,3,1],[7,-8,-4,-9],[1,5,7,10],[4,7,3,2],[-6,-9,-4,-6],[4,-2,-3,1],[8,1,-4,7],[10,-3,1,8],[4,8,-8,7],[-8,-2,-9,8],[-9,-5,9,10]],[[7,4,-9,-9],[8,10,-4,1],[7,-5,-4,-8],[-2,-5,6,-2],[-1,2,9,-4],[1,-4,-1,6],[-8,-6,4,7],[-6,6,-8,-6],[-7,10,2,-2],[5,7,-10,-8],[6,3,8,5],[-2,10,3,10],[6,3,-1,-10],[-10,-6,4,1]],[[8,9,3,1],[-6,7,7,-7],[-5,-9,-5,5],[-8,8,-3,-1],[2,-6,-3,-4],[8,-8,7,5],[8,-10,-7,-8],[6,-6,-4,1],[-8,-5,-5,-1],[8,-9,-7,-1],[-2,-7,6,3],[-3,4,-7,-5],[5,7,-9,-5],[10,-6,-10,-1]],[[7,-1,-7,-6],[3,-8,-6,-7],[-5,1,3,-2],[1,9,2,6],[-1,-2,-1,-9],[-10,-7,1,9],[8,-9,9,-5],[9,6,5,-1],[-8,7,5,8],[-2,-4,-8,-1],[5,1,-3,-6],[2,6,-3,6],[-1,-3,-8,2],[5,-4,-10,-3]],[[-7,1,-1,-4],[9,10,6,5],[8,6,8,-5],[5,-10,-6,-2],[-7,5,-1,1],[-9,-4,-1,-4],[7,-5,7,2],[3,9,-2,4],[-5,9,8,-8],[3,3,2,-2],[-9,-6,1,10],[-7,-3,9,10],[6,10,9,10],[1,-5,5,2]],[[6,-10,-5,9],[9,-2,-9,4],[2,-9,3,3],[7,9,-7,3],[8,-8,-8,-8],[1,7,4,7],[-5,-9,8,-2],[-3,-6,-1,-2],[4,5,-9,9],[3,-3,-7,-7],[9,-1,-9,3],[-4,-10,9,6],[-4,-7,4,-6],[-4,-5,1,3]],[[9,8,-7,-10],[9,-5,-4,4],[-2,2,7,-2],[-6,9,-1,7],[6,-8,6,3],[-9,-6,1,-10],[8,-8,9,5],[-9,3,9,-1],[-3,10,-8,7],[-1,-10,-2,5],[6,7,3,1],[8,-5,-3,-4],[9,8,-4,5],[-7,-10,-9,10]],[[-6,1,9,-3],[-7,6,7,10],[1,-3,4,-4],[7,1,7,-1],[8,-4,5,6],[8,-4,9,10],[4,8,-3,9],[6,-6,-9,6],[1,6,9,-8],[1,3,5,-1],[9,7,2,4],[3,-1,-8,-2],[8,5,-10,-6],[4,-1,3,10]]], dtype = "uint64")#candidate|3352|(14, 14, 4)|const|uint64
bop_3353 = relay.bitwise_or(var_3351.astype('uint64'), relay.reshape(const_3352.astype('uint64'), relay.shape_of(var_3351))) # shape=(14, 14, 4)
output = relay.Tuple([bop_3353,])
output2 = relay.Tuple([bop_3353,])
func_3359 = relay.Function([var_3351,], output)
mod['func_3359'] = func_3359
mod = relay.transform.InferType()(mod)
mutated_mod['func_3359'] = func_3359
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3360 = relay.var("var_3360", dtype = "uint64", shape = (14, 14, 4))#candidate|3360|(14, 14, 4)|var|uint64
func_3359_call = mutated_mod.get_global_var('func_3359')
call_3361 = func_3359_call(var_3360)
output = call_3361
func_3362 = relay.Function([var_3360], output)
mutated_mod['func_3362'] = func_3362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3149_call = mod.get_global_var('func_3149')
func_3151_call = mutated_mod.get_global_var('func_3151')
call_3384 = relay.TupleGetItem(func_3149_call(), 0)
call_3385 = relay.TupleGetItem(func_3151_call(), 0)
var_3400 = relay.var("var_3400", dtype = "float32", shape = (11, 11, 7))#candidate|3400|(11, 11, 7)|var|float32
bop_3401 = relay.floor_divide(call_3384.astype('float32'), relay.reshape(var_3400.astype('float32'), relay.shape_of(call_3384))) # shape=(11, 11, 7)
bop_3404 = relay.floor_divide(call_3385.astype('float32'), relay.reshape(var_3400.astype('float32'), relay.shape_of(call_3385))) # shape=(11, 11, 7)
output = bop_3401
output2 = bop_3404
func_3436 = relay.Function([var_3400,], output)
mod['func_3436'] = func_3436
mod = relay.transform.InferType()(mod)
var_3437 = relay.var("var_3437", dtype = "float32", shape = (11, 11, 7))#candidate|3437|(11, 11, 7)|var|float32
output = func_3436(var_3437)
func_3438 = relay.Function([var_3437], output)
mutated_mod['func_3438'] = func_3438
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_3537 = relay.TupleGetItem(func_2912_call(), 0)
call_3538 = relay.TupleGetItem(func_2913_call(), 0)
output = call_3537
output2 = call_3538
func_3550 = relay.Function([], output)
mod['func_3550'] = func_3550
mod = relay.transform.InferType()(mod)
output = func_3550()
func_3551 = relay.Function([], output)
mutated_mod['func_3551'] = func_3551
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3588 = relay.var("var_3588", dtype = "uint32", shape = (4, 7, 14))#candidate|3588|(4, 7, 14)|var|uint32
var_3589 = relay.var("var_3589", dtype = "uint32", shape = (4, 7, 14))#candidate|3589|(4, 7, 14)|var|uint32
bop_3590 = relay.maximum(var_3588.astype('uint32'), relay.reshape(var_3589.astype('uint32'), relay.shape_of(var_3588))) # shape=(4, 7, 14)
uop_3598 = relay.asin(var_3589.astype('float32')) # shape=(4, 7, 14)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_3604 = relay.TupleGetItem(func_2183_call(), 3)
call_3605 = relay.TupleGetItem(func_2185_call(), 3)
output = relay.Tuple([bop_3590,uop_3598,call_3604,])
output2 = relay.Tuple([bop_3590,uop_3598,call_3605,])
func_3611 = relay.Function([var_3588,var_3589,], output)
mod['func_3611'] = func_3611
mod = relay.transform.InferType()(mod)
var_3612 = relay.var("var_3612", dtype = "uint32", shape = (4, 7, 14))#candidate|3612|(4, 7, 14)|var|uint32
var_3613 = relay.var("var_3613", dtype = "uint32", shape = (4, 7, 14))#candidate|3613|(4, 7, 14)|var|uint32
output = func_3611(var_3612,var_3613,)
func_3614 = relay.Function([var_3612,var_3613,], output)
mutated_mod['func_3614'] = func_3614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3090_call = mod.get_global_var('func_3090')
func_3091_call = mutated_mod.get_global_var('func_3091')
call_3668 = relay.TupleGetItem(func_3090_call(), 0)
call_3669 = relay.TupleGetItem(func_3091_call(), 0)
func_2278_call = mod.get_global_var('func_2278')
func_2282_call = mutated_mod.get_global_var('func_2282')
var_3677 = relay.var("var_3677", dtype = "float64", shape = (26, 1))#candidate|3677|(26, 1)|var|float64
var_3678 = relay.var("var_3678", dtype = "uint32", shape = (330,))#candidate|3678|(330,)|var|uint32
call_3676 = relay.TupleGetItem(func_2278_call(relay.reshape(var_3677.astype('float64'), [13, 2, 1]), relay.reshape(var_3678.astype('uint32'), [330,]), ), 2)
call_3679 = relay.TupleGetItem(func_2282_call(relay.reshape(var_3677.astype('float64'), [13, 2, 1]), relay.reshape(var_3678.astype('uint32'), [330,]), ), 2)
bop_3695 = relay.bitwise_and(var_3677.astype('int8'), var_3678.astype('int8')) # shape=(26, 330)
func_3149_call = mod.get_global_var('func_3149')
func_3151_call = mutated_mod.get_global_var('func_3151')
call_3698 = relay.TupleGetItem(func_3149_call(), 0)
call_3699 = relay.TupleGetItem(func_3151_call(), 0)
output = relay.Tuple([call_3668,call_3676,bop_3695,call_3698,])
output2 = relay.Tuple([call_3669,call_3679,bop_3695,call_3699,])
func_3710 = relay.Function([var_3677,var_3678,], output)
mod['func_3710'] = func_3710
mod = relay.transform.InferType()(mod)
mutated_mod['func_3710'] = func_3710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3710_call = mutated_mod.get_global_var('func_3710')
var_3712 = relay.var("var_3712", dtype = "float64", shape = (26, 1))#candidate|3712|(26, 1)|var|float64
var_3713 = relay.var("var_3713", dtype = "uint32", shape = (330,))#candidate|3713|(330,)|var|uint32
call_3711 = func_3710_call(var_3712,var_3713,)
output = call_3711
func_3714 = relay.Function([var_3712,var_3713,], output)
mutated_mod['func_3714'] = func_3714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_3749 = relay.TupleGetItem(func_2183_call(), 4)
call_3750 = relay.TupleGetItem(func_2185_call(), 4)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
const_3769 = relay.const([[5],[5],[-8],[-2],[1],[-10],[-5],[-8],[1],[6],[8],[-2],[1],[-3],[7],[-9],[1],[-2],[-4],[-9],[4],[-10],[10],[-5],[7],[-6],[-1],[-3],[10],[1],[3],[10],[6],[10],[8],[5],[-1],[-1],[4],[-4],[7],[-9],[10],[-1],[5],[-10],[3],[-2],[-1],[1],[4],[-3],[2],[5],[-8],[-8],[-9],[-5],[6],[-1],[-9],[-1],[8],[3],[8],[1],[9],[-6],[-8],[8],[10],[-2],[2],[9],[-3],[-1],[9],[5],[7],[-9],[2],[-8],[5],[-4],[5],[-8],[-8],[5],[8],[-8],[-2],[3],[2],[1],[6],[6],[-1],[8],[8],[-1],[-4],[9],[1],[-1],[-8],[2],[-1],[3],[1],[-5],[-5],[4],[7],[4],[-6],[10],[5],[-3],[5],[-7],[-7],[5],[2],[-1],[6],[-1],[-9],[9],[-8],[1],[9],[5],[1],[2],[6],[-9],[8],[10],[5],[-4],[-1],[2],[-9],[8],[-3],[1],[-10],[-7],[6],[9],[9],[-6],[-3],[9],[-2],[-9],[-8],[-3],[-1],[4],[9],[7],[4],[2],[-3],[4],[10],[-9],[6],[3],[10],[1],[6],[-5],[-6],[-2],[-6],[6],[-2],[10],[1],[7],[3],[6],[-3],[7],[4],[3],[3],[-6],[9],[-4],[6],[-5],[-10],[2],[-10],[-5],[-7],[2],[2],[3],[-9],[-4],[4],[-1],[-8],[10],[-5],[-2],[1],[-6],[-5],[5],[2],[1],[-1],[9],[-3],[-2],[5],[-2],[8],[-6],[-6],[-8],[4],[-9],[5],[-10],[3],[10],[-6],[-4],[2],[-5],[-9],[1],[-8],[10],[7],[2],[-2],[-2],[-5],[3],[-2],[2],[3],[-8],[-1],[-3],[2],[10],[3],[6],[8],[3],[7],[6],[-6],[1],[-3],[9],[-10],[3],[1],[-4],[2],[-5],[-3],[-6],[6],[-10],[5],[-6],[6],[-2],[-10],[-7],[9],[2],[7],[-5],[1],[5],[8],[7],[-3],[9],[-3],[-2],[2],[-10],[-6],[-5],[-6],[-6],[-6],[-2],[-10],[2],[-2],[-6],[-6],[-4],[9],[9],[-3],[-6],[-3],[-5],[1],[-2],[4],[-1],[-4],[-4],[2],[1],[4],[8],[-3],[-7],[-6],[-5],[-5],[10],[4],[10]], dtype = "uint32")#candidate|3769|(330, 1)|const|uint32
call_3768 = func_839_call(relay.reshape(const_3769.astype('uint32'), [2, 15, 11]))
call_3770 = func_839_call(relay.reshape(const_3769.astype('uint32'), [2, 15, 11]))
bop_3775 = relay.bitwise_xor(call_3749.astype('int32'), const_3769.astype('int32')) # shape=(330, 36)
bop_3778 = relay.bitwise_xor(call_3750.astype('int32'), const_3769.astype('int32')) # shape=(330, 36)
uop_3781 = relay.cosh(bop_3775.astype('float32')) # shape=(330, 36)
uop_3783 = relay.cosh(bop_3778.astype('float32')) # shape=(330, 36)
var_3785 = relay.var("var_3785", dtype = "uint32", shape = (330, 1))#candidate|3785|(330, 1)|var|uint32
bop_3786 = relay.maximum(const_3769.astype('uint32'), relay.reshape(var_3785.astype('uint32'), relay.shape_of(const_3769))) # shape=(330, 1)
func_3611_call = mod.get_global_var('func_3611')
func_3614_call = mutated_mod.get_global_var('func_3614')
var_3790 = relay.var("var_3790", dtype = "uint32", shape = (392,))#candidate|3790|(392,)|var|uint32
call_3789 = relay.TupleGetItem(func_3611_call(relay.reshape(var_3790.astype('uint32'), [4, 7, 14]), relay.reshape(var_3790.astype('uint32'), [4, 7, 14]), ), 0)
call_3791 = relay.TupleGetItem(func_3614_call(relay.reshape(var_3790.astype('uint32'), [4, 7, 14]), relay.reshape(var_3790.astype('uint32'), [4, 7, 14]), ), 0)
uop_3801 = relay.atanh(uop_3781.astype('float64')) # shape=(330, 36)
uop_3803 = relay.atanh(uop_3783.astype('float64')) # shape=(330, 36)
func_2061_call = mod.get_global_var('func_2061')
func_2065_call = mutated_mod.get_global_var('func_2065')
call_3806 = relay.TupleGetItem(func_2061_call(relay.reshape(call_3749.astype('float64'), [2, 9, 2]), relay.reshape(call_3749.astype('float64'), [2, 9, 2]), ), 1)
call_3807 = relay.TupleGetItem(func_2065_call(relay.reshape(call_3749.astype('float64'), [2, 9, 2]), relay.reshape(call_3749.astype('float64'), [2, 9, 2]), ), 1)
bop_3811 = relay.floor_mod(uop_3801.astype('float64'), var_3785.astype('float64')) # shape=(330, 36)
bop_3814 = relay.floor_mod(uop_3803.astype('float64'), var_3785.astype('float64')) # shape=(330, 36)
func_3149_call = mod.get_global_var('func_3149')
func_3151_call = mutated_mod.get_global_var('func_3151')
call_3816 = relay.TupleGetItem(func_3149_call(), 0)
call_3817 = relay.TupleGetItem(func_3151_call(), 0)
func_3611_call = mod.get_global_var('func_3611')
func_3614_call = mutated_mod.get_global_var('func_3614')
call_3822 = relay.TupleGetItem(func_3611_call(relay.reshape(call_3789.astype('uint32'), [4, 7, 14]), relay.reshape(var_3790.astype('uint32'), [4, 7, 14]), ), 1)
call_3823 = relay.TupleGetItem(func_3614_call(relay.reshape(call_3789.astype('uint32'), [4, 7, 14]), relay.reshape(var_3790.astype('uint32'), [4, 7, 14]), ), 1)
func_1929_call = mod.get_global_var('func_1929')
func_1931_call = mutated_mod.get_global_var('func_1931')
const_3831 = relay.const([-7.037395,-3.869613,-3.572700,7.992138,2.842777,5.822404,5.723156,9.756944,-8.286920,-7.344507,2.986864,-3.322726,4.316413,9.115633,-3.941627,-9.876880,1.553691,8.700866,-0.863628,3.714354,4.493192,-9.576826,-0.583053,-0.592113,-4.508824,4.256787,8.181523,8.072547,6.516399,0.868564,2.628129,5.067772,-2.319250,-0.437190,1.577570,-4.905927,0.980826,2.199620,-4.247028,-7.109399,-0.974220,7.674477,5.209910,-7.773632,9.445583,-8.216967,5.298142,-5.055232,-0.611371,-7.659850,-8.479057,3.892633,5.390739,-9.577388,-5.337892,3.846624,-7.116110,-6.780042,3.311065,4.987653,-5.296788,5.678777,1.864493,1.099804,4.154915,6.309396,-4.607984,0.245349,6.660554,-3.451387,-0.667443,-0.141630], dtype = "float32")#candidate|3831|(72,)|const|float32
call_3830 = func_1929_call(relay.reshape(const_3831.astype('float32'), [3, 2, 12]))
call_3832 = func_1929_call(relay.reshape(const_3831.astype('float32'), [3, 2, 12]))
output = relay.Tuple([call_3768,bop_3786,call_3789,var_3790,call_3806,bop_3811,call_3816,call_3822,call_3830,const_3831,])
output2 = relay.Tuple([call_3770,bop_3786,call_3791,var_3790,call_3807,bop_3814,call_3817,call_3823,call_3832,const_3831,])
func_3833 = relay.Function([var_3785,var_3790,], output)
mod['func_3833'] = func_3833
mod = relay.transform.InferType()(mod)
var_3834 = relay.var("var_3834", dtype = "uint32", shape = (330, 1))#candidate|3834|(330, 1)|var|uint32
var_3835 = relay.var("var_3835", dtype = "uint32", shape = (392,))#candidate|3835|(392,)|var|uint32
output = func_3833(var_3834,var_3835,)
func_3836 = relay.Function([var_3834,var_3835,], output)
mutated_mod['func_3836'] = func_3836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_3840 = relay.TupleGetItem(func_2183_call(), 4)
call_3841 = relay.TupleGetItem(func_2185_call(), 4)
func_3611_call = mod.get_global_var('func_3611')
func_3614_call = mutated_mod.get_global_var('func_3614')
var_3861 = relay.var("var_3861", dtype = "uint32", shape = (392,))#candidate|3861|(392,)|var|uint32
call_3860 = relay.TupleGetItem(func_3611_call(relay.reshape(var_3861.astype('uint32'), [4, 7, 14]), relay.reshape(var_3861.astype('uint32'), [4, 7, 14]), ), 2)
call_3862 = relay.TupleGetItem(func_3614_call(relay.reshape(var_3861.astype('uint32'), [4, 7, 14]), relay.reshape(var_3861.astype('uint32'), [4, 7, 14]), ), 2)
func_3090_call = mod.get_global_var('func_3090')
func_3091_call = mutated_mod.get_global_var('func_3091')
call_3867 = relay.TupleGetItem(func_3090_call(), 0)
call_3868 = relay.TupleGetItem(func_3091_call(), 0)
uop_3873 = relay.rsqrt(call_3867.astype('float32')) # shape=(11, 11, 7)
uop_3875 = relay.rsqrt(call_3868.astype('float32')) # shape=(11, 11, 7)
output = relay.Tuple([call_3840,call_3860,var_3861,uop_3873,])
output2 = relay.Tuple([call_3841,call_3862,var_3861,uop_3875,])
func_3894 = relay.Function([var_3861,], output)
mod['func_3894'] = func_3894
mod = relay.transform.InferType()(mod)
mutated_mod['func_3894'] = func_3894
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3895 = relay.var("var_3895", dtype = "uint32", shape = (392,))#candidate|3895|(392,)|var|uint32
func_3894_call = mutated_mod.get_global_var('func_3894')
call_3896 = func_3894_call(var_3895)
output = call_3896
func_3897 = relay.Function([var_3895], output)
mutated_mod['func_3897'] = func_3897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2975_call = mod.get_global_var('func_2975')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_3903 = relay.TupleGetItem(func_2975_call(), 2)
call_3904 = relay.TupleGetItem(func_2977_call(), 2)
output = call_3903
output2 = call_3904
func_3908 = relay.Function([], output)
mod['func_3908'] = func_3908
mod = relay.transform.InferType()(mod)
output = func_3908()
func_3909 = relay.Function([], output)
mutated_mod['func_3909'] = func_3909
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3149_call = mod.get_global_var('func_3149')
func_3151_call = mutated_mod.get_global_var('func_3151')
call_3934 = relay.TupleGetItem(func_3149_call(), 0)
call_3935 = relay.TupleGetItem(func_3151_call(), 0)
func_3550_call = mod.get_global_var('func_3550')
func_3551_call = mutated_mod.get_global_var('func_3551')
call_3941 = func_3550_call()
call_3942 = func_3550_call()
output = relay.Tuple([call_3934,call_3941,])
output2 = relay.Tuple([call_3935,call_3942,])
func_3950 = relay.Function([], output)
mod['func_3950'] = func_3950
mod = relay.transform.InferType()(mod)
output = func_3950()
func_3951 = relay.Function([], output)
mutated_mod['func_3951'] = func_3951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3318_call = mod.get_global_var('func_3318')
func_3320_call = mutated_mod.get_global_var('func_3320')
call_3955 = relay.TupleGetItem(func_3318_call(), 1)
call_3956 = relay.TupleGetItem(func_3320_call(), 1)
output = relay.Tuple([call_3955,])
output2 = relay.Tuple([call_3956,])
func_3968 = relay.Function([], output)
mod['func_3968'] = func_3968
mod = relay.transform.InferType()(mod)
output = func_3968()
func_3969 = relay.Function([], output)
mutated_mod['func_3969'] = func_3969
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4055 = relay.var("var_4055", dtype = "uint8", shape = (3, 14, 9))#candidate|4055|(3, 14, 9)|var|uint8
var_4056 = relay.var("var_4056", dtype = "uint8", shape = (3, 14, 9))#candidate|4056|(3, 14, 9)|var|uint8
bop_4057 = relay.subtract(var_4055.astype('uint8'), relay.reshape(var_4056.astype('uint8'), relay.shape_of(var_4055))) # shape=(3, 14, 9)
func_1315_call = mod.get_global_var('func_1315')
func_1320_call = mutated_mod.get_global_var('func_1320')
const_4064 = relay.const([5,3,8,-10,-5,-2,1,-7,-3,-9,-10,-10,-1,-2,-9,-5,8,8,-10,-6,1,-7,2,-3,10,7,-10,-4,2,-10,-1,-7,3,-7,-6,-7,1,-7,9,-7,1,10,5,-4,10,-9,-9,9,2,6,-7,4,8,-2,-1,-9,-4,-6,4,7,-4,-4,1,-6,7,10,2,3,-5,-10,-5,1,-7,-8,6,5,-2,-4,2,5,-9,-5,-10,4,3,-4,-2,-10,3,-2,-5,-1,-5,9,5,9,10,-5,-2,6,3,-6,6,-4,3,-9,2,-5,-5,6,-6,-3,9,-7,-7,8,4,2,1,-8,-1,-3,7,10,10,-1,3,7,2,-2,-8,8,6,1,-8,-4,-5,2,4,-5,9,3,2,1,3,-2,6,4,-1,-3,-3,8,1,4,-1,2,-7,-10,-4,-2,6,9,-5,8,-7,7,-6,-1], dtype = "int64")#candidate|4064|(168,)|const|int64
var_4065 = relay.var("var_4065", dtype = "float32", shape = (640,))#candidate|4065|(640,)|var|float32
call_4063 = relay.TupleGetItem(func_1315_call(relay.reshape(const_4064.astype('int64'), [7, 12, 2]), relay.reshape(const_4064.astype('int64'), [7, 12, 2]), relay.reshape(var_4065.astype('float32'), [640,]), ), 5)
call_4066 = relay.TupleGetItem(func_1320_call(relay.reshape(const_4064.astype('int64'), [7, 12, 2]), relay.reshape(const_4064.astype('int64'), [7, 12, 2]), relay.reshape(var_4065.astype('float32'), [640,]), ), 5)
func_3436_call = mod.get_global_var('func_3436')
func_3438_call = mutated_mod.get_global_var('func_3438')
var_4082 = relay.var("var_4082", dtype = "float32", shape = (1, 847))#candidate|4082|(1, 847)|var|float32
call_4081 = func_3436_call(relay.reshape(var_4082.astype('float32'), [11, 11, 7]))
call_4083 = func_3436_call(relay.reshape(var_4082.astype('float32'), [11, 11, 7]))
bop_4090 = relay.bitwise_or(var_4056.astype('uint32'), relay.reshape(var_4055.astype('uint32'), relay.shape_of(var_4056))) # shape=(3, 14, 9)
output = relay.Tuple([bop_4057,call_4063,const_4064,var_4065,call_4081,var_4082,bop_4090,])
output2 = relay.Tuple([bop_4057,call_4066,const_4064,var_4065,call_4083,var_4082,bop_4090,])
func_4099 = relay.Function([var_4055,var_4056,var_4065,var_4082,], output)
mod['func_4099'] = func_4099
mod = relay.transform.InferType()(mod)
mutated_mod['func_4099'] = func_4099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4099_call = mutated_mod.get_global_var('func_4099')
var_4101 = relay.var("var_4101", dtype = "uint8", shape = (3, 14, 9))#candidate|4101|(3, 14, 9)|var|uint8
var_4102 = relay.var("var_4102", dtype = "uint8", shape = (3, 14, 9))#candidate|4102|(3, 14, 9)|var|uint8
var_4103 = relay.var("var_4103", dtype = "float32", shape = (640,))#candidate|4103|(640,)|var|float32
var_4104 = relay.var("var_4104", dtype = "float32", shape = (1, 847))#candidate|4104|(1, 847)|var|float32
call_4100 = func_4099_call(var_4101,var_4102,var_4103,var_4104,)
output = call_4100
func_4105 = relay.Function([var_4101,var_4102,var_4103,var_4104,], output)
mutated_mod['func_4105'] = func_4105
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4190 = relay.var("var_4190", dtype = "float32", shape = (12, 1, 4))#candidate|4190|(12, 1, 4)|var|float32
uop_4191 = relay.sinh(var_4190.astype('float32')) # shape=(12, 1, 4)
output = uop_4191
output2 = uop_4191
func_4210 = relay.Function([var_4190,], output)
mod['func_4210'] = func_4210
mod = relay.transform.InferType()(mod)
var_4211 = relay.var("var_4211", dtype = "float32", shape = (12, 1, 4))#candidate|4211|(12, 1, 4)|var|float32
output = func_4210(var_4211)
func_4212 = relay.Function([var_4211], output)
mutated_mod['func_4212'] = func_4212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3149_call = mod.get_global_var('func_3149')
func_3151_call = mutated_mod.get_global_var('func_3151')
call_4257 = relay.TupleGetItem(func_3149_call(), 0)
call_4258 = relay.TupleGetItem(func_3151_call(), 0)
func_3908_call = mod.get_global_var('func_3908')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_4280 = func_3908_call()
call_4281 = func_3908_call()
func_3950_call = mod.get_global_var('func_3950')
func_3951_call = mutated_mod.get_global_var('func_3951')
call_4284 = relay.TupleGetItem(func_3950_call(), 1)
call_4285 = relay.TupleGetItem(func_3951_call(), 1)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_4286 = func_3252_call()
call_4287 = func_3252_call()
output = relay.Tuple([call_4257,call_4280,call_4284,call_4286,])
output2 = relay.Tuple([call_4258,call_4281,call_4285,call_4287,])
func_4306 = relay.Function([], output)
mod['func_4306'] = func_4306
mod = relay.transform.InferType()(mod)
output = func_4306()
func_4307 = relay.Function([], output)
mutated_mod['func_4307'] = func_4307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_4331 = func_3331_call()
call_4332 = func_3331_call()
output = relay.Tuple([call_4331,])
output2 = relay.Tuple([call_4332,])
func_4358 = relay.Function([], output)
mod['func_4358'] = func_4358
mod = relay.transform.InferType()(mod)
mutated_mod['func_4358'] = func_4358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4358_call = mutated_mod.get_global_var('func_4358')
call_4359 = func_4358_call()
output = call_4359
func_4360 = relay.Function([], output)
mutated_mod['func_4360'] = func_4360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_4369 = func_3331_call()
call_4370 = func_3331_call()
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_4373 = func_1893_call()
call_4374 = func_1893_call()
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_4377 = relay.TupleGetItem(func_2183_call(), 2)
call_4378 = relay.TupleGetItem(func_2185_call(), 2)
func_2358_call = mod.get_global_var('func_2358')
func_2360_call = mutated_mod.get_global_var('func_2360')
const_4387 = relay.const([-8.277386,8.336362,-2.714357,8.546676,-8.266911,-2.375139,1.772745,-9.724636,-1.424060,-4.276334,-5.023585,0.085328,7.005257,2.308332,9.834156,2.654014,-9.678866,-5.210852,-9.853083,4.645468,2.665004,-9.606382,-4.896924,8.877593,-2.183249,3.009542,-0.760184,-7.922577,-8.570421,-9.088768,-0.268342,3.095471,5.746675,9.633983,3.539222,-3.876088,8.350562,-6.763780,7.145999,-1.555925,7.301022,-4.204081,-4.812068,3.459737,-7.492572,-0.406704,8.657549,1.826526,-5.270325,-5.610635,5.769710,-7.327076,0.383396,1.711674,2.145104,-2.032931,9.576645,-9.286846,-3.086709,-4.482232,-7.547337,4.345244,5.183373,-4.279693,7.584444,0.451493,5.317842,9.097486,-3.921511,4.989336,-8.341754,1.088629,-3.891341,0.197194,8.651080,5.735060,4.801331,-2.051855,7.190354,-7.271062,2.332600,-6.013886,8.950268,-9.474239,-2.093030,1.667953,1.056531,-5.930637,2.762944,-6.151027,5.634582,-6.966567,-6.282138,8.189146,0.849399,0.812953,-5.592087,1.162653,0.780228,9.479755,4.558391,8.556204,0.782464,-7.023575,6.067993,-9.086216,-8.428076,9.878162,9.130241,-6.923460,-4.606229,1.525327,2.994666,9.198190,-9.190766,-9.022125,5.717821,3.493112,6.532704,8.920595,-7.714080,-3.624146,-5.336045,-0.541945,-3.894278,-0.497191,-2.514305,3.027243,-8.876834,-2.938442,-8.730871,-9.009275,-0.475720,-1.801633,6.854207,5.284924,3.035776,-7.695746,8.969358,6.754190,-4.125703,5.498936,-0.293660,-0.273326,2.865449,0.045175,-6.162394,1.887749,2.202843,-6.596819,-3.689998,4.914733,1.864369,6.833242,-4.587528,4.546468,3.399508,4.732877,9.443183,-0.809451,-8.906711,-1.740056,-8.089129,-1.179835,-1.698650,-3.456663,-4.214718,-3.680748], dtype = "float32")#candidate|4387|(168,)|const|float32
call_4386 = relay.TupleGetItem(func_2358_call(relay.reshape(const_4387.astype('float32'), [6, 4, 7])), 0)
call_4388 = relay.TupleGetItem(func_2360_call(relay.reshape(const_4387.astype('float32'), [6, 4, 7])), 0)
func_2061_call = mod.get_global_var('func_2061')
func_2065_call = mutated_mod.get_global_var('func_2065')
call_4389 = relay.TupleGetItem(func_2061_call(relay.reshape(call_4369.astype('float64'), [2, 9, 2]), relay.reshape(call_4369.astype('float64'), [2, 9, 2]), ), 0)
call_4390 = relay.TupleGetItem(func_2065_call(relay.reshape(call_4369.astype('float64'), [2, 9, 2]), relay.reshape(call_4369.astype('float64'), [2, 9, 2]), ), 0)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_4394 = func_3252_call()
call_4395 = func_3252_call()
output = relay.Tuple([call_4369,call_4373,call_4377,call_4386,const_4387,call_4389,call_4394,])
output2 = relay.Tuple([call_4370,call_4374,call_4378,call_4388,const_4387,call_4390,call_4395,])
func_4398 = relay.Function([], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
output = func_4398()
func_4399 = relay.Function([], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3090_call = mod.get_global_var('func_3090')
func_3091_call = mutated_mod.get_global_var('func_3091')
call_4429 = relay.TupleGetItem(func_3090_call(), 0)
call_4430 = relay.TupleGetItem(func_3091_call(), 0)
output = relay.Tuple([call_4429,])
output2 = relay.Tuple([call_4430,])
func_4431 = relay.Function([], output)
mod['func_4431'] = func_4431
mod = relay.transform.InferType()(mod)
output = func_4431()
func_4432 = relay.Function([], output)
mutated_mod['func_4432'] = func_4432
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2975_call = mod.get_global_var('func_2975')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_4489 = relay.TupleGetItem(func_2975_call(), 0)
call_4490 = relay.TupleGetItem(func_2977_call(), 0)
output = call_4489
output2 = call_4490
func_4496 = relay.Function([], output)
mod['func_4496'] = func_4496
mod = relay.transform.InferType()(mod)
mutated_mod['func_4496'] = func_4496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4496_call = mutated_mod.get_global_var('func_4496')
call_4497 = func_4496_call()
output = call_4497
func_4498 = relay.Function([], output)
mutated_mod['func_4498'] = func_4498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_4525 = func_1893_call()
call_4526 = func_1893_call()
var_4534 = relay.var("var_4534", dtype = "float32", shape = (3, 2, 12))#candidate|4534|(3, 2, 12)|var|float32
bop_4535 = relay.left_shift(call_4525.astype('uint8'), relay.reshape(var_4534.astype('uint8'), relay.shape_of(call_4525))) # shape=(3, 2, 12)
bop_4538 = relay.left_shift(call_4526.astype('uint8'), relay.reshape(var_4534.astype('uint8'), relay.shape_of(call_4526))) # shape=(3, 2, 12)
output = bop_4535
output2 = bop_4538
func_4546 = relay.Function([var_4534,], output)
mod['func_4546'] = func_4546
mod = relay.transform.InferType()(mod)
var_4547 = relay.var("var_4547", dtype = "float32", shape = (3, 2, 12))#candidate|4547|(3, 2, 12)|var|float32
output = func_4546(var_4547)
func_4548 = relay.Function([var_4547], output)
mutated_mod['func_4548'] = func_4548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_4564 = relay.TupleGetItem(func_4398_call(), 6)
call_4565 = relay.TupleGetItem(func_4399_call(), 6)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
const_4613 = relay.const([[5],[8],[-5],[-8],[-4],[5],[-2],[-9],[-9],[5],[-6],[-1],[-10],[4],[-9],[9],[-8],[-5],[9],[5],[-2],[-9],[-3],[9],[3],[7],[2],[8],[5],[7],[10],[7],[-4],[4],[6],[7],[10],[-4],[-2],[5],[6],[7],[-2],[-3],[6],[-10],[-7],[6],[-9],[-5],[10],[3],[-7],[2],[-10],[9],[7],[-6],[-10],[5],[-9],[2],[-3],[-7],[9],[-7],[3],[-6],[7],[-4],[-5],[2],[8],[2],[-7],[1],[5],[1],[-2],[-10],[10],[7],[-7],[4],[2],[-10],[-10],[10],[10],[-3],[8],[-2],[9],[-1],[-2],[1],[10],[5],[-2],[-3],[8],[1],[6],[5],[3],[3],[-4],[-4],[-8],[4],[-8],[2],[-3],[-9],[-8],[9],[-6],[4],[-4],[-9],[9],[-10],[-5],[-5],[-1],[-5],[-4],[-1],[5],[-1],[-10],[9],[-5],[-9],[-3],[7],[10],[-4],[4],[-10],[-10],[6],[-1],[10],[4],[-9],[6],[-4],[2],[-1],[4],[9],[-7],[-1],[-6],[-6],[5],[10],[-8],[3],[4],[8],[-1],[-2],[-8],[10],[-2],[5],[5],[8],[6],[-6],[5],[-6],[6],[7],[-1],[-9],[-9],[-5],[-3],[8],[7],[-5],[-9],[2],[7],[6],[-5],[5],[4],[-1],[-6],[9],[-3],[-2],[-3],[-4],[-4],[-3],[-1],[10],[-4],[-2],[-3],[-10],[8],[3],[-6],[-1],[7],[7],[-4],[10],[-1],[-2],[-9],[-2],[1],[2],[10],[10],[-7],[-6],[-5],[2],[-10],[4],[2],[-3],[7],[3],[8],[-9],[-9],[2],[6],[9],[-4],[6],[2],[3],[-7],[-8],[-1],[9],[-4],[3],[10],[-10],[4],[-10],[3],[4],[4],[9],[6],[-10],[9],[3],[6],[-9],[6],[4],[-6],[7],[-8],[8],[6],[-1],[2],[8],[1],[2],[-5],[1],[6],[-6],[2],[10],[-6],[-7],[6],[6],[-9],[-6],[-6],[-10],[4],[9],[6],[-5],[-10],[7],[-10],[-1],[8],[3],[-5],[-7],[7],[-5],[8],[1],[7],[1],[10],[8],[-6],[-3],[3],[-7],[1],[-4],[10],[-1],[5],[-9],[9],[-4],[10],[10],[1],[7],[4],[-6],[-3],[10],[2],[10]], dtype = "uint32")#candidate|4613|(330, 1)|const|uint32
call_4612 = func_839_call(relay.reshape(const_4613.astype('uint32'), [2, 15, 11]))
call_4614 = func_839_call(relay.reshape(const_4613.astype('uint32'), [2, 15, 11]))
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_4619 = relay.TupleGetItem(func_2912_call(), 2)
call_4620 = relay.TupleGetItem(func_2913_call(), 2)
func_1315_call = mod.get_global_var('func_1315')
func_1320_call = mutated_mod.get_global_var('func_1320')
var_4634 = relay.var("var_4634", dtype = "int64", shape = (168,))#candidate|4634|(168,)|var|int64
var_4635 = relay.var("var_4635", dtype = "float32", shape = (320, 2))#candidate|4635|(320, 2)|var|float32
call_4633 = relay.TupleGetItem(func_1315_call(relay.reshape(var_4634.astype('int64'), [7, 12, 2]), relay.reshape(var_4634.astype('int64'), [7, 12, 2]), relay.reshape(var_4635.astype('float32'), [640,]), ), 4)
call_4636 = relay.TupleGetItem(func_1320_call(relay.reshape(var_4634.astype('int64'), [7, 12, 2]), relay.reshape(var_4634.astype('int64'), [7, 12, 2]), relay.reshape(var_4635.astype('float32'), [640,]), ), 4)
func_364_call = mod.get_global_var('func_364')
func_367_call = mutated_mod.get_global_var('func_367')
const_4644 = relay.const([[5.015016,-0.282673,0.772034,3.771187,-8.693367,-3.500824],[-1.078611,5.041221,-6.528546,7.657482,-0.104637,-0.103349],[9.493441,0.203779,4.115172,-0.513606,1.073015,6.840974],[-0.280505,-1.927932,7.486757,-5.915038,-8.892804,9.699522],[-8.039457,-3.332679,9.622954,-4.834865,-9.578064,-8.788555],[-7.392320,6.242073,3.826928,9.681331,6.852264,0.950559],[-2.925719,-0.370552,7.290258,-8.113611,-7.986001,-6.888918],[5.517059,-3.530899,-4.990494,6.037197,-7.219350,-8.706495],[-7.360388,3.517888,-8.194981,-4.553331,9.822433,5.900056],[-3.661397,-1.612419,-5.352232,-2.715065,-5.028795,-3.539757],[4.600464,4.885715,-1.123585,-9.555581,8.944132,-9.149428],[-9.495578,5.429754,4.410178,-5.891743,-7.430203,-2.473066],[0.671352,-9.577035,-6.772623,9.430536,4.691446,7.771901],[-7.213417,-5.692316,5.955035,6.167140,6.360652,3.174049],[4.612020,8.478269,3.607552,0.689226,-8.488644,-8.073107]], dtype = "float64")#candidate|4644|(15, 6)|const|float64
call_4643 = relay.TupleGetItem(func_364_call(relay.reshape(call_4619.astype('float64'), []), relay.reshape(const_4644.astype('float64'), [10, 9, 1]), ), 0)
call_4645 = relay.TupleGetItem(func_367_call(relay.reshape(call_4619.astype('float64'), []), relay.reshape(const_4644.astype('float64'), [10, 9, 1]), ), 0)
func_3436_call = mod.get_global_var('func_3436')
func_3438_call = mutated_mod.get_global_var('func_3438')
const_4659 = relay.const([1.481640,-0.781539,9.828740,2.595176,-5.951218,8.321097,-7.029663,-5.832775,6.566244,-6.354846,-1.197868,9.407006,-0.061465,4.731905,-0.727828,7.801605,-9.463117,5.232631,-9.268991,-2.563000,8.969676,0.468448,1.697881,5.492144,8.048868,-7.395296,-5.770618,6.967908,8.408552,-5.971579,-7.106401,-3.237432,-3.691010,3.603399,-9.808399,7.885642,6.289193,4.797176,-4.436868,-7.012815,1.852531,6.922881,-7.121636,-2.310858,0.556617,7.638646,-7.488171,-7.312049,0.770274,7.831957,5.891526,-5.181488,6.027635,1.452257,-4.628288,2.440159,-0.206982,5.502941,1.450706,5.667134,-9.949370,6.969750,-1.360255,7.067447,3.355205,0.129676,8.868467,2.146118,-8.993050,-5.447328,-5.608232,-5.152576,-8.184438,2.662296,8.016626,-4.716093,-7.789411,-4.389478,0.508706,-6.129660,-5.867605,8.236680,3.193538,-6.250435,2.850500,-6.465234,-5.980546,3.574813,-5.479898,-7.522102,3.184357,-5.655991,-3.318391,-2.523627,-1.048882,-0.864769,-2.842458,6.264721,7.632769,9.830864,-2.424480,-9.597242,-9.069830,-7.926743,4.865630,-1.007343,5.659611,-9.537120,3.407557,-4.526114,8.726567,-7.844391,-5.843564,-6.973658,9.507062,7.725153,6.040494,-5.858272,3.226148,4.508241,-9.973223,8.029738,-6.059896,4.391009,-3.841466,2.482068,0.792046,0.710457,9.901614,8.833444,-4.300299,7.763152,-7.938950,6.941265,-7.527825,-1.378149,8.189760,-9.073433,2.235440,6.319573,0.400769,-8.965263,7.463358,0.087162,3.736651,0.483321,2.253508,0.563720,8.947364,9.320713,3.932757,-7.356509,2.371116,-1.586409,-1.029957,-9.330232,5.325400,-3.769669,-0.552617,8.135423,-3.623090,2.175660,3.563213,-6.927895,-2.644940,-3.738367,2.191210,-9.381069,-7.766327,-3.365099,-3.823622,-2.643132,4.754314,-1.145579,-6.755216,5.387720,5.638951,-4.418054,9.740239,9.625967,-9.916063,-2.495749,-9.248363,-8.015569,7.638691,2.278417,0.235519,0.028335,2.512770,5.974369,-0.032763,-8.683325,2.192228,-9.270015,6.496679,-4.588755,-0.945338,-1.169593,4.761022,6.415423,6.964789,1.040414,-6.680615,3.679543,-1.356891,-2.296030,2.660607,-8.962066,4.471133,6.995122,-7.086670,9.242187,-5.799959,2.623282,-3.160388,3.822640,-0.858813,3.236822,7.065567,-9.938561,3.090488,-5.985078,1.238484,1.756010,-7.916860,-5.148841,1.622358,7.975678,9.186206,1.935323,3.633794,2.071350,2.902371,-4.287164,4.144703,6.897042,4.744542,5.153954,-5.037836,-5.797402,0.447660,-1.988667,-4.700029,1.145855,-1.423910,8.732310,1.797502,3.136955,4.969746,6.605027,-1.233389,1.796321,8.996842,0.169903,-2.687957,-8.486360,-2.593655,-3.392163,-1.948882,-6.619679,-6.356982,-0.617012,-8.253008,9.351388,9.373512,-5.843756,3.835864,-1.136016,-2.182608,-3.276504,4.917926,-6.271661,6.756951,-6.188243,-1.433776,5.717654,-1.049515,-2.299176,9.407697,8.837580,3.399410,6.405238,6.944681,1.583673,7.850660,-5.888031,-5.000907,-2.218295,8.756736,7.527656,8.044982,8.480321,-6.626557,-0.025847,4.739827,-1.961521,8.374281,9.696508,4.350442,-0.585538,-8.059244,0.757534,8.833256,2.338738,-5.043902,0.965992,9.402787,-3.145003,-6.038156,3.714518,-6.191808,-3.301710,7.892253,-9.109711,-9.994202,0.162460,-8.094445,6.595574,-8.001359,-8.548760,6.721258,-1.804932,-2.888679,-9.672541,2.105383,-0.861067,-2.646618,2.481727,-9.740774,-3.545606,-2.766176,-6.822102,5.661929,6.063509,-6.821097,-7.660640,3.816549,-1.919701,2.301121,-3.737271,-0.977147,-5.817768,-1.050409,4.842193,-2.030914,6.864742,5.240219,0.926254,-5.485715,4.025967,-9.418917,-2.569659,-3.017860,-6.711205,-2.639890,0.464662,3.376016,8.412270,4.155521,5.223308,-4.090478,3.494213,-2.825158,-9.250854,5.118160,8.041379,-4.714362,2.291095,-2.150224,-8.664144,-4.643359,6.175985,-3.746718,4.226482,2.517423,5.630342,-0.910867,-3.962624,8.479741,0.057112,-5.762495,-4.973844,-9.005773,3.776906,8.642570,4.127248,4.182039,-6.627442,8.013489,-4.414289,-5.978897,8.398415,-0.979306,8.368652,-5.943219,-7.922997,7.465574,8.669082,-9.450041,-8.111419,1.134921,3.159018,-2.388475,-1.277747,-7.031567,4.267750,-1.262006,4.410437,-7.016573,-1.438221,2.842481,3.553795,5.662940,-1.314682,2.302483,-0.690118,2.710917,-6.549165,4.398484,9.781711,8.990955,-5.675059,8.211870,-7.292858,-5.801653,5.482571,4.059887,-5.355763,3.737004,-7.709205,5.737947,8.626370,-7.485890,-5.594408,-1.290654,7.134447,-2.611399,1.204658,4.600981,9.902356,-6.392753,6.400962,4.456157,8.708843,7.772130,-9.584504,-1.734217,1.755699,6.537609,-6.428754,6.844364,5.115970,5.328520,-7.195936,-6.034111,-8.363185,-6.239320,-0.475841,4.931440,-4.399872,3.691775,6.780356,8.908848,-0.883538,-3.581169,-5.762420,3.240794,-0.986746,9.167423,1.489262,-8.144174,-5.034501,-3.411729,1.790786,-9.531389,-9.909683,-1.299653,1.895358,-1.572112,-4.161048,-1.408697,-1.352002,-9.468869,-5.152527,9.922264,3.786620,3.123704,-3.937867,-9.829403,6.495254,-8.101699,-6.031127,7.859775,-6.219843,3.184591,1.760905,7.679788,9.059174,-7.900090,4.845044,-9.706405,4.877744,8.507569,9.857969,5.804162,-5.663585,-4.914227,-0.726678,1.031796,2.654542,7.761589,-9.894103,-3.161722,-2.684064,-2.969064,5.019010,-5.134431,-3.830327,-1.605029,8.411704,8.420241,2.107064,-2.973422,2.087288,-7.748706,3.411822,6.830291,0.329525,5.916023,-5.820575,7.452177,-3.578721,4.773485,0.868956,-6.209467,6.629137,2.914782,2.095597,9.903142,6.596165,1.191708,6.775961,-5.574527,3.161892,4.716578,7.402557,2.837826,-7.643872,2.411087,-4.694439,1.661766,2.893469,8.929337,-8.195123,2.194293,-2.504525,-3.797708,-2.645197,-1.428270,3.462513,5.160078,1.228832,-9.592840,2.092896,5.563220,-1.434393,-3.965264,4.530767,-3.143049,-8.895269,9.560866,2.573200,-3.951534,5.885751,1.368746,-9.505132,5.186934,8.206103,-7.584921,6.514090,-3.999183,-0.110428,7.889818,-5.760509,4.622753,-0.258338,-0.898373,2.129900,6.041453,2.046846,1.444302,1.491327,2.611787,-5.005237,-3.804732,-2.764353,9.662837,1.251622,-2.526096,9.458685,-1.134890,5.809125,1.529599,1.169022,6.622155,2.282990,6.195500,6.489416,5.161039,-8.109269,-6.552210,-7.743676,5.713784,-9.152546,-7.033289,3.241743,9.373885,1.765917,1.338216,3.372421,0.034810,8.729036,-4.151009,-3.324415,0.239340,0.930716,1.860675,6.699021,0.147685,-4.773958,0.289601,-0.532780,-4.684374,4.537016,-8.436696,-4.160736,3.829875,-2.431476,5.947780,6.092406,5.299021,-8.146169,2.101984,1.750362,7.846349,-0.888407,-0.382849,-8.771973,-7.607579,-9.826203,-4.669729,-2.185479,9.395697,1.808341,5.013053,7.010819,9.469898,8.376575,3.952833,2.286780,3.520726,-6.524653,-6.659407,-2.262600,-3.898294,-6.238433,-2.708737,0.339749,9.282384,-1.527629,8.434528,-3.147564,6.189560,0.317235,-6.762821,0.952638,-8.763465,8.040009,-1.303286,2.783081,3.117081,-5.533775,6.922783,4.922117,-7.236054,7.580235,7.786407,8.500984,-4.672048,6.415833,6.127490,-8.542146,-4.705362,0.387691,4.687181,-3.788841,-0.349746,-1.031841,-1.738891,-7.567997,0.982009,-2.211315,1.168393,1.119679,1.618147,1.242979,-9.108799,-8.273381,3.021123,2.922897,5.706276,6.971829,-8.506078,4.315626,1.487029,-0.991612,6.805884,6.472453,-4.836055,-5.493208,-9.215644,-4.639183,3.759305,8.755833,-1.755449,-6.436428,-4.057183,9.773470,6.480642,2.148381,2.948361,-2.233044,0.988868,3.880590,-5.850467,9.248907,3.592208,1.935393,-7.020941,-3.078725,-2.286733,-7.386233,-9.276271,5.965879,-0.621030,7.790750,-3.697434,8.700893,8.845418,2.054056,-0.376227,-1.336500,3.488131,4.894889,1.518107,-0.092421,-9.961390,-2.087519,8.533907,-9.280559,6.750864,3.215157,1.500590,7.080989,7.931283,0.713672,0.757576,-2.342250,7.201528,-2.413599,4.122858,-9.641402,-6.383326,-6.656173,2.923007,4.718836,-2.579333,-0.590634,7.267760,7.985494,3.702110,5.991113,-0.828792,0.827418,0.876172,-7.412305,-2.337230,-8.857024,-8.088118,-3.820677,2.980540,-9.700240,-5.064919,-5.512092,-5.268950,7.637457,-5.368216,-1.031513,-8.027021,-0.430622,2.849739,-6.688592,-5.059850,-7.386070,9.064131,-5.732122,3.742215,8.394299,3.381914,3.726457,0.032309,4.100391,1.536393,-3.627250,1.804459,8.045411,-6.219433,5.567042,-0.854910,9.472947,-1.796654,8.120769,-8.260845,-6.070103,-3.389725,0.118174,-2.466927,9.578838,-5.130370,0.886779,-1.951758,-4.763385,-2.560500,2.177703,-0.024658,-6.921759,-7.613268,-0.225353,-4.933879,5.933611,-5.087063,-6.775312,8.464975,3.437827,-8.713060,-3.647514,1.736395], dtype = "float32")#candidate|4659|(847,)|const|float32
call_4658 = func_3436_call(relay.reshape(const_4659.astype('float32'), [11, 11, 7]))
call_4660 = func_3436_call(relay.reshape(const_4659.astype('float32'), [11, 11, 7]))
output = relay.Tuple([call_4564,call_4612,const_4613,call_4619,call_4633,var_4634,var_4635,call_4643,const_4644,call_4658,const_4659,])
output2 = relay.Tuple([call_4565,call_4614,const_4613,call_4620,call_4636,var_4634,var_4635,call_4645,const_4644,call_4660,const_4659,])
func_4674 = relay.Function([var_4634,var_4635,], output)
mod['func_4674'] = func_4674
mod = relay.transform.InferType()(mod)
mutated_mod['func_4674'] = func_4674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4674_call = mutated_mod.get_global_var('func_4674')
var_4676 = relay.var("var_4676", dtype = "int64", shape = (168,))#candidate|4676|(168,)|var|int64
var_4677 = relay.var("var_4677", dtype = "float32", shape = (320, 2))#candidate|4677|(320, 2)|var|float32
call_4675 = func_4674_call(var_4676,var_4677,)
output = call_4675
func_4678 = relay.Function([var_4676,var_4677,], output)
mutated_mod['func_4678'] = func_4678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_4701 = func_2949_call()
call_4702 = func_2949_call()
uop_4717 = relay.sigmoid(call_4701.astype('float32')) # shape=(11, 11, 7)
uop_4719 = relay.sigmoid(call_4702.astype('float32')) # shape=(11, 11, 7)
output = uop_4717
output2 = uop_4719
func_4736 = relay.Function([], output)
mod['func_4736'] = func_4736
mod = relay.transform.InferType()(mod)
output = func_4736()
func_4737 = relay.Function([], output)
mutated_mod['func_4737'] = func_4737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4736_call = mod.get_global_var('func_4736')
func_4737_call = mutated_mod.get_global_var('func_4737')
call_4745 = func_4736_call()
call_4746 = func_4736_call()
output = call_4745
output2 = call_4746
func_4753 = relay.Function([], output)
mod['func_4753'] = func_4753
mod = relay.transform.InferType()(mod)
output = func_4753()
func_4754 = relay.Function([], output)
mutated_mod['func_4754'] = func_4754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4431_call = mod.get_global_var('func_4431')
func_4432_call = mutated_mod.get_global_var('func_4432')
call_4781 = relay.TupleGetItem(func_4431_call(), 0)
call_4782 = relay.TupleGetItem(func_4432_call(), 0)
func_2649_call = mod.get_global_var('func_2649')
func_2653_call = mutated_mod.get_global_var('func_2653')
var_4786 = relay.var("var_4786", dtype = "uint32", shape = (165, 2))#candidate|4786|(165, 2)|var|uint32
var_4787 = relay.var("var_4787", dtype = "float64", shape = (640,))#candidate|4787|(640,)|var|float64
call_4785 = relay.TupleGetItem(func_2649_call(relay.reshape(var_4786.astype('uint32'), [330,]), relay.reshape(var_4787.astype('float64'), [10, 64]), relay.reshape(var_4787.astype('float64'), [10, 64]), ), 0)
call_4788 = relay.TupleGetItem(func_2653_call(relay.reshape(var_4786.astype('uint32'), [330,]), relay.reshape(var_4787.astype('float64'), [10, 64]), relay.reshape(var_4787.astype('float64'), [10, 64]), ), 0)
output = relay.Tuple([call_4781,call_4785,var_4786,var_4787,])
output2 = relay.Tuple([call_4782,call_4788,var_4786,var_4787,])
func_4790 = relay.Function([var_4786,var_4787,], output)
mod['func_4790'] = func_4790
mod = relay.transform.InferType()(mod)
var_4791 = relay.var("var_4791", dtype = "uint32", shape = (165, 2))#candidate|4791|(165, 2)|var|uint32
var_4792 = relay.var("var_4792", dtype = "float64", shape = (640,))#candidate|4792|(640,)|var|float64
output = func_4790(var_4791,var_4792,)
func_4793 = relay.Function([var_4791,var_4792,], output)
mutated_mod['func_4793'] = func_4793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_4840 = func_2949_call()
call_4841 = func_2949_call()
func_4306_call = mod.get_global_var('func_4306')
func_4307_call = mutated_mod.get_global_var('func_4307')
call_4862 = relay.TupleGetItem(func_4306_call(), 3)
call_4863 = relay.TupleGetItem(func_4307_call(), 3)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_4867 = func_2949_call()
call_4868 = func_2949_call()
output = relay.Tuple([call_4840,call_4862,call_4867,])
output2 = relay.Tuple([call_4841,call_4863,call_4868,])
func_4871 = relay.Function([], output)
mod['func_4871'] = func_4871
mod = relay.transform.InferType()(mod)
output = func_4871()
func_4872 = relay.Function([], output)
mutated_mod['func_4872'] = func_4872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4753_call = mod.get_global_var('func_4753')
func_4754_call = mutated_mod.get_global_var('func_4754')
call_4888 = func_4753_call()
call_4889 = func_4753_call()
output = call_4888
output2 = call_4889
func_4911 = relay.Function([], output)
mod['func_4911'] = func_4911
mod = relay.transform.InferType()(mod)
output = func_4911()
func_4912 = relay.Function([], output)
mutated_mod['func_4912'] = func_4912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2975_call = mod.get_global_var('func_2975')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_4927 = relay.TupleGetItem(func_2975_call(), 0)
call_4928 = relay.TupleGetItem(func_2977_call(), 0)
func_1979_call = mod.get_global_var('func_1979')
func_1982_call = mutated_mod.get_global_var('func_1982')
const_4945 = relay.const([10,-8,6,-3,4,2,6,-4,7,-2,6,4,9,-7,3,-4,3,-9,-3,-1,-4,-1,-4,-7,2,10,1,9,5,10,5,10,8,-8,-10,10,-1,6,7,6,5,5,-2,-7,-2,5,-10,5,4,1,-4,8,1,1,-9,7,-7,-9,9,-5,2,-6,7,-10,-7,-3,-1,6,-6,2,-6,-9,-1,1,6,-1,-8,-3,-10,-3,4,-8,8,-9,-1,-10,-1,-9,1,2,-7,-8,-2,9,-3,-1,-10,-6,-4,-3,-7,1,5,-10,-3,-6,7,-5,-4,-3,7,-8,6,5,8,-5,10,10,-8,-2,5,1,-9,-5,3,1,-3,-8,2,6,-9,2,-7,-7,-5,7,-4,-5,7,9,7,1,-1,-8,-10,1,-7,3,7,2,8,5,-10,-6,-8,8,-4,-7,7,6,-4,-1,1,-7,-3,-10,10,2,6,8,2,1,-6,3,-6,3,7,10,-5,6,-8,8,4,10,7,-3,-6,6,-5,-7,9,8,1,4,5,-5,-6,10,2,-9,-10,1,9,9,-8,4,4,5,-9,3,-9,-8,-3,7,10,6,10,-5,-7,-4,1,-2,1,-2,6,-6,-4,-2,-7,-2,-4,-7,8,-7,8,-7,1,-4,7,-3,-1,-8,5,10,8,9,2,8,7,2,7,4,3,10,-4,-2,2,-10,1,-1,3,3,-5,5,6,-7,1,3,-1,-3,-4,10,7,6,-9,9,6,-7,-2,-3,2,-3,3,-4,-9,-9,-1,2,6,-6,-5,-9,6,10,-8,6,2,10,7,10,-8,2,8,7,-2,-1,9,-7,-5,1,-9,1,10,9,-5,5,7,-5,3,-9,7,3,-9,1,9,-7,-10,-10,-2,-8,-9,2,-4,1,9,4,9,1,10,-1,-5,7,-9,-6,7,7,10,-2,-8,-2,2,-4,5,-8,-1,-4,-9,2,10,-8,3,-3,-7,-7,-7,-6,5,9,-9,-5,-5,-5,-9,-2,-4,-6,-6,-1,-3,9,-7,10,-5,2,-3,2,-3,4,-5,-1,-9,-7,-3,7,9,9,-3,8,5,1,4,-7,2,8,-2,-6,5,5,4,-5,9,10,10,-9,-7,-4,6,7,7,-5,6,9,7,-9,-5,7,-8,-8,-3,5,7,-1,3,1,5,8,-9,3,10,-10,-8,-10,2,-7,3,6,-1,5,5,3,-3,-3,7,-2,-10,9,9,-4,-5,7,1,2,-8,-8,-4,-5,2,-3,4,4,-8,-1,4,10,-4,-1,-8,-1,-9,-1,9,-10,-4,10,8,5,8,-5,-1,6,-9,2,-10,-6,-9,-2,5,-9,-6,-10,-4,-2,-8,7,-9,-5,-9,-8,10,-6,10,-7,-9,-5,-7,9,7,6,-8,7,5,6,8,1,-7,-7,6,-4,-2,1,-6,-3,-4,10,-1,9,-10,-9,10,-6,-8,6,9,-10,2,2,-2,1,-3,7,-10,9,-3,8,-10,-10,9,4,-9,9,-6,7,8,-3,9,-7,8,8,-8,-3,-3,9,-1,10,-7,-9,-1,-2,-6,-2,-7,-5,8,-6,-2,-5,4,-8,6,2,6,8,-10,8,5,1,2,-7,-1,-7,4,9,5,-10,5,6,-5,-1,-7,1,1,-4,-9,-3,5,-3,-1,6,2,-9,-10,-10,-1,2,-10,-10,6,-5,-8,-5,-8,4,3,-5,6,3,9,10,4,8,2,6,5,-3,10,7,-6,-7,-1,-7,-4,-2,4,3,-2,6,2,-6,-5,-9,6,-3,7,3,-2,-6,1,-9,1,-6,4,9,-4,-2,-3,-4,-7,3,-6,-5,-9,3,10,-6,4,4,-4,6,9,6,7,2,6,-9,4,-9,4,2,5,-4,3,-9,-2,-4,-2,-4,-10,-4,-2,9,6,8,1,5,1,7,9,1,-10,4,-9,1,-5,-8,-8,4,4,-6,-3,8,-2,9,2,3,-9,4,-5,7,-1,-8,1,-5,-5,7,3,5,-2,-5,6,-6,4,1,8,9,5,2,-1,-9,9,-6,5,10,-6,2,4,5,2,7,-5,1,4,-6,-10,1,2,4,9,-5,-10,6,-8,9,-6,2,-3,-3,-6,-3,-3,8,4,-5,7,-7,-8,8,-4,8,5,3], dtype = "int16")#candidate|4945|(800,)|const|int16
call_4944 = relay.TupleGetItem(func_1979_call(relay.reshape(const_4945.astype('int16'), [800,])), 0)
call_4946 = relay.TupleGetItem(func_1982_call(relay.reshape(const_4945.astype('int16'), [800,])), 0)
uop_4957 = relay.asinh(call_4944.astype('float32')) # shape=(3, 2, 12)
uop_4959 = relay.asinh(call_4946.astype('float32')) # shape=(3, 2, 12)
func_4753_call = mod.get_global_var('func_4753')
func_4754_call = mutated_mod.get_global_var('func_4754')
call_4960 = func_4753_call()
call_4961 = func_4753_call()
output = relay.Tuple([call_4927,const_4945,uop_4957,call_4960,])
output2 = relay.Tuple([call_4928,const_4945,uop_4959,call_4961,])
func_4963 = relay.Function([], output)
mod['func_4963'] = func_4963
mod = relay.transform.InferType()(mod)
output = func_4963()
func_4964 = relay.Function([], output)
mutated_mod['func_4964'] = func_4964
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4965 = relay.const([[[-2.855995,8.803005,9.661482,2.306814],[-6.246351,-0.651206,2.678074,-6.783525],[-1.266016,-5.393196,9.685982,-1.640350],[-8.419828,8.356089,-8.571725,-3.424887],[0.247981,-5.492658,-7.989798,3.375919],[-9.105489,8.488678,2.277361,-3.254894],[0.607003,1.768055,3.634033,1.064888]],[[6.416135,-8.999765,5.237426,0.922860],[-5.283520,-3.097684,0.814573,-6.019373],[8.794594,1.437296,6.156558,2.370495],[-5.634413,2.732293,-2.011955,-1.231282],[3.078818,9.166255,7.711654,-4.877514],[-9.513482,-4.338892,-5.221659,-6.872081],[4.747717,-9.896582,0.254858,6.019959]],[[-2.700704,2.981476,7.309496,3.131029],[-7.852250,8.329755,8.022668,-4.202269],[-0.730464,7.574691,7.205307,0.049568],[0.290541,3.757059,7.341260,3.439936],[8.363058,-3.209793,-2.187020,1.266211],[-8.903514,-3.259391,-5.722201,8.093942],[-7.435429,-2.155021,-2.404825,-2.340188]],[[2.286712,-4.452844,-6.828573,1.987546],[-9.244154,-5.764232,4.128936,-0.892619],[-3.694578,6.819844,5.475659,-7.044865],[3.826015,9.276245,-4.640792,8.710203],[5.176840,-9.556544,9.535705,1.767818],[8.902473,-9.406497,5.735558,-2.539244],[-3.931311,2.859547,-2.738269,7.213764]],[[-9.594003,-8.809041,-8.556955,-3.912385],[3.030986,0.360266,-7.537171,8.588743],[-5.982883,-4.287894,-1.457028,6.571126],[-4.140869,-6.944961,-4.949110,-9.571906],[-5.000381,5.927896,0.803629,-1.947516],[-8.694285,5.611296,-3.886196,-2.088985],[6.431566,-0.855583,9.036768,-6.500685]],[[-3.705390,1.052457,-5.826119,4.542315],[-7.191611,8.661017,3.719174,-7.578804],[2.734273,-5.727677,-2.025394,-0.673059],[-5.578413,1.155111,-8.461609,1.123185],[-6.486750,-3.605719,9.017593,1.487588],[-3.607444,7.862556,-9.624441,-6.163084],[7.200757,4.166375,6.592973,3.508031]],[[4.887973,-0.446622,-1.291062,-2.307857],[-1.823957,2.580804,7.960498,6.608644],[3.038374,3.805736,-1.837847,5.872888],[-4.799884,-5.539483,-9.991414,7.242667],[-1.957459,-3.120094,-0.793286,-2.450400],[0.152589,-3.961975,-5.443276,-5.038993],[-5.945229,-2.936316,4.463816,-4.624254]],[[-6.696439,-6.893275,7.050141,-2.495638],[0.262518,-4.177814,-6.263434,-1.774854],[1.818922,-2.142180,-2.725397,8.898409],[-2.068715,1.429034,-5.689611,0.175608],[-9.947525,7.099100,-0.046764,-1.601826],[-4.261848,6.494218,6.460005,-7.401766],[-2.916793,-9.325166,-7.539476,4.377716]],[[3.293409,-5.620470,-9.766398,2.946578],[4.840412,-5.392856,-2.515359,8.243450],[-7.688739,0.317364,-0.729896,-8.135538],[-5.947609,6.376861,-8.266979,7.528765],[-8.019960,2.651871,-3.781848,6.979076],[-2.361941,2.345821,-0.239727,2.507375],[5.910255,-8.910570,0.884642,-4.402109]],[[-7.576808,-6.729675,-6.804539,-6.872296],[5.633047,0.363453,-7.844949,-8.377338],[2.217089,-7.530272,-7.255533,-9.295393],[-6.001358,-3.527973,8.460622,-1.886777],[-8.917668,-2.873661,-3.579581,6.631320],[2.929029,6.265420,-0.433146,-8.016060],[6.445760,9.936876,-8.861377,3.708778]],[[8.034340,-4.883881,-0.743444,-5.269937],[6.013813,8.143773,5.618789,-7.545787],[-5.982409,7.414735,3.958550,-5.646833],[-2.648445,-7.432684,0.062142,2.482786],[1.481100,5.922262,-9.103047,8.731661],[-7.404302,-7.602675,3.178364,-6.580280],[-2.913662,-2.365610,8.920398,3.642139]],[[3.319945,7.714754,1.149653,6.621100],[-1.974927,8.588515,-2.587822,8.868370],[8.608120,-9.419601,-0.798307,-5.661675],[-3.296322,-1.581366,6.159889,6.607084],[6.523016,8.793466,-2.449076,-0.311220],[2.139522,5.785983,-4.148260,2.575625],[-2.708508,-7.810315,-5.920721,-4.966027]],[[-7.364696,7.307147,-5.573863,-1.975744],[5.445941,-8.445731,-2.885317,-7.705570],[-8.274469,9.989639,-5.287264,8.820691],[-2.588151,4.210985,-3.150107,-1.436262],[-8.343619,1.489505,-2.884559,2.483706],[7.113570,7.779994,-9.600642,-2.805489],[-5.069230,1.339640,-9.237007,5.759380]]], dtype = "float64")#candidate|4965|(13, 7, 4)|const|float64
uop_4966 = relay.log(const_4965.astype('float64')) # shape=(13, 7, 4)
uop_4995 = relay.atan(uop_4966.astype('float64')) # shape=(13, 7, 4)
bop_4999 = relay.multiply(uop_4966.astype('float64'), relay.reshape(uop_4995.astype('float64'), relay.shape_of(uop_4966))) # shape=(13, 7, 4)
output = bop_4999
output2 = bop_4999
func_5008 = relay.Function([], output)
mod['func_5008'] = func_5008
mod = relay.transform.InferType()(mod)
output = func_5008()
func_5009 = relay.Function([], output)
mutated_mod['func_5009'] = func_5009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_5010 = func_1893_call()
call_5011 = func_1893_call()
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_5013 = relay.TupleGetItem(func_2183_call(), 0)
call_5014 = relay.TupleGetItem(func_2185_call(), 0)
func_3950_call = mod.get_global_var('func_3950')
func_3951_call = mutated_mod.get_global_var('func_3951')
call_5023 = relay.TupleGetItem(func_3950_call(), 1)
call_5024 = relay.TupleGetItem(func_3951_call(), 1)
output = relay.Tuple([call_5010,call_5013,call_5023,])
output2 = relay.Tuple([call_5011,call_5014,call_5024,])
func_5035 = relay.Function([], output)
mod['func_5035'] = func_5035
mod = relay.transform.InferType()(mod)
output = func_5035()
func_5036 = relay.Function([], output)
mutated_mod['func_5036'] = func_5036
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5043 = relay.const([[[3,-7,-5,5,3,10,7,5,-5,9,-4,-5],[9,5,-10,-7,8,-7,-3,5,-6,-3,6,-5],[6,-10,-4,-9,6,8,1,-7,9,2,-10,7],[3,-9,7,9,-7,6,-4,6,-8,-4,-10,-10],[6,-1,8,-2,-10,-1,4,2,8,5,-2,-2],[7,-1,-6,6,-2,10,-6,4,-3,5,-4,-1],[5,-4,8,9,-1,-10,1,1,-6,-7,3,-10],[-6,-6,-4,-3,-4,7,-5,5,5,3,3,3],[-6,2,2,8,7,-10,-2,9,2,-5,-10,-2],[-8,-5,2,-10,8,10,4,-8,3,-3,1,-10],[-7,1,-5,-4,-8,4,5,-10,6,5,-9,4],[-10,-6,6,-7,1,10,-1,-9,-3,10,-4,3],[10,3,-10,1,1,-3,5,10,8,-2,-6,7],[-1,-7,5,9,5,-7,7,5,7,-7,-9,-8],[8,-5,8,-2,-9,6,-9,3,6,-1,8,-3],[7,7,6,3,3,8,2,-2,1,6,2,-5]],[[9,-3,3,2,-3,-6,-4,3,-10,1,-3,4],[-3,-5,2,-5,-8,-6,2,3,-6,-6,-1,-8],[-2,-3,-3,10,-7,-3,6,10,6,-9,5,-6],[2,-1,-1,-3,9,-7,-5,8,-3,-1,-9,-3],[6,-5,-3,-1,-3,9,3,-6,-10,-7,-1,6],[-8,-2,-9,-3,-8,-7,-1,7,3,5,-10,10],[-5,6,6,1,9,2,-10,-3,5,-1,-10,-10],[6,9,-8,9,-10,1,-7,9,-6,5,5,-6],[8,9,-8,1,4,-2,-2,6,-6,-7,9,-8],[-4,5,-1,-2,-8,8,-9,10,2,-8,2,6],[10,2,7,8,-5,3,-2,6,7,6,7,-3],[-7,-3,2,-9,-1,6,1,1,5,-1,-10,-8],[4,-7,9,10,-9,-5,10,-7,-2,-3,7,8],[-10,10,7,9,2,-4,7,5,7,-9,3,-2],[-1,10,6,9,-9,6,-6,9,2,-9,7,7],[3,3,-3,2,7,-1,10,-1,-10,-4,3,-4]],[[-9,5,8,-10,-9,-8,-7,6,10,8,-9,8],[-7,6,10,-8,7,-4,7,-8,8,-7,-6,-10],[-4,8,-9,-3,-1,-6,-2,-9,-10,-4,9,-1],[7,2,3,-10,8,10,-4,-4,3,9,6,4],[3,3,9,-6,2,-10,8,3,9,5,-6,2],[1,-7,-9,3,9,1,7,-6,7,-5,-7,-3],[2,10,7,9,1,-4,-7,2,2,7,3,2],[9,-5,6,3,-5,5,-4,9,10,-6,2,-6],[3,8,5,6,-7,-2,-8,-10,7,5,2,7],[-1,1,-4,10,10,-3,-7,-1,-1,-5,10,-4],[-3,-8,-6,6,-1,3,-6,3,2,-3,7,1],[-10,9,-6,-7,-3,-3,-2,-6,-8,6,-1,-1],[5,2,-1,3,1,-9,6,-5,1,-10,7,-3],[5,10,-8,-1,-7,8,5,-9,-3,5,-4,-8],[8,-7,-4,-9,-2,6,-10,-5,-9,-4,2,1],[2,5,-4,-1,1,-7,-10,5,-5,-2,-10,-3]]], dtype = "int16")#candidate|5043|(3, 16, 12)|const|int16
var_5044 = relay.var("var_5044", dtype = "int16", shape = (3, 16, 12))#candidate|5044|(3, 16, 12)|var|int16
bop_5045 = relay.add(const_5043.astype('int16'), relay.reshape(var_5044.astype('int16'), relay.shape_of(const_5043))) # shape=(3, 16, 12)
output = relay.Tuple([bop_5045,])
output2 = relay.Tuple([bop_5045,])
func_5052 = relay.Function([var_5044,], output)
mod['func_5052'] = func_5052
mod = relay.transform.InferType()(mod)
mutated_mod['func_5052'] = func_5052
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5053 = relay.var("var_5053", dtype = "int16", shape = (3, 16, 12))#candidate|5053|(3, 16, 12)|var|int16
func_5052_call = mutated_mod.get_global_var('func_5052')
call_5054 = func_5052_call(var_5053)
output = call_5054
func_5055 = relay.Function([var_5053], output)
mutated_mod['func_5055'] = func_5055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4496_call = mod.get_global_var('func_4496')
func_4498_call = mutated_mod.get_global_var('func_4498')
call_5075 = func_4496_call()
call_5076 = func_4496_call()
output = call_5075
output2 = call_5076
func_5084 = relay.Function([], output)
mod['func_5084'] = func_5084
mod = relay.transform.InferType()(mod)
output = func_5084()
func_5085 = relay.Function([], output)
mutated_mod['func_5085'] = func_5085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_5121 = func_3331_call()
call_5122 = func_3331_call()
output = call_5121
output2 = call_5122
func_5123 = relay.Function([], output)
mod['func_5123'] = func_5123
mod = relay.transform.InferType()(mod)
output = func_5123()
func_5124 = relay.Function([], output)
mutated_mod['func_5124'] = func_5124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3090_call = mod.get_global_var('func_3090')
func_3091_call = mutated_mod.get_global_var('func_3091')
call_5132 = relay.TupleGetItem(func_3090_call(), 0)
call_5133 = relay.TupleGetItem(func_3091_call(), 0)
output = call_5132
output2 = call_5133
func_5153 = relay.Function([], output)
mod['func_5153'] = func_5153
mod = relay.transform.InferType()(mod)
mutated_mod['func_5153'] = func_5153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5153_call = mutated_mod.get_global_var('func_5153')
call_5154 = func_5153_call()
output = call_5154
func_5155 = relay.Function([], output)
mutated_mod['func_5155'] = func_5155
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5253 = relay.var("var_5253", dtype = "float32", shape = (11, 11, 12))#candidate|5253|(11, 11, 12)|var|float32
uop_5254 = relay.atan(var_5253.astype('float32')) # shape=(11, 11, 12)
bop_5257 = relay.right_shift(var_5253.astype('int32'), relay.reshape(uop_5254.astype('int32'), relay.shape_of(var_5253))) # shape=(11, 11, 12)
output = bop_5257
output2 = bop_5257
func_5265 = relay.Function([var_5253,], output)
mod['func_5265'] = func_5265
mod = relay.transform.InferType()(mod)
mutated_mod['func_5265'] = func_5265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5266 = relay.var("var_5266", dtype = "float32", shape = (11, 11, 12))#candidate|5266|(11, 11, 12)|var|float32
func_5265_call = mutated_mod.get_global_var('func_5265')
call_5267 = func_5265_call(var_5266)
output = call_5267
func_5268 = relay.Function([var_5266], output)
mutated_mod['func_5268'] = func_5268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5084_call = mod.get_global_var('func_5084')
func_5085_call = mutated_mod.get_global_var('func_5085')
call_5280 = func_5084_call()
call_5281 = func_5084_call()
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_5286 = func_1893_call()
call_5287 = func_1893_call()
output = relay.Tuple([call_5280,call_5286,])
output2 = relay.Tuple([call_5281,call_5287,])
func_5300 = relay.Function([], output)
mod['func_5300'] = func_5300
mod = relay.transform.InferType()(mod)
output = func_5300()
func_5301 = relay.Function([], output)
mutated_mod['func_5301'] = func_5301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3550_call = mod.get_global_var('func_3550')
func_3551_call = mutated_mod.get_global_var('func_3551')
call_5311 = func_3550_call()
call_5312 = func_3550_call()
output = call_5311
output2 = call_5312
func_5314 = relay.Function([], output)
mod['func_5314'] = func_5314
mod = relay.transform.InferType()(mod)
mutated_mod['func_5314'] = func_5314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5314_call = mutated_mod.get_global_var('func_5314')
call_5315 = func_5314_call()
output = call_5315
func_5316 = relay.Function([], output)
mutated_mod['func_5316'] = func_5316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5345 = relay.var("var_5345", dtype = "uint32", shape = ())#candidate|5345|()|var|uint32
var_5346 = relay.var("var_5346", dtype = "uint32", shape = (1, 9, 5))#candidate|5346|(1, 9, 5)|var|uint32
bop_5347 = relay.not_equal(var_5345.astype('bool'), var_5346.astype('bool')) # shape=(1, 9, 5)
func_3894_call = mod.get_global_var('func_3894')
func_3897_call = mutated_mod.get_global_var('func_3897')
const_5351 = relay.const([[10,-10,-6,6,-3,4,10,-10,-5,10,8,3,-9,-1,-4,-2,4,7,8,-3,-2,10,8,-10,4,6,-5,1,8,10,2,6,5,-7,9,-5,-8,10,4,8,-9,-3,5,-8,-3,-5,-10,10,-2,-8,8,1,-8,-1,8,2,4,-2,7,-2,-6,-5,5,2,6,-10,3,10,10,-6,1,-8,1,-5,-7,1,1,-4,5,6,7,-6,7,4,9,8,5,-6,5,7,6,7,-3,-6,6,10,9,-4,1,-6,7,2,-1,8,-10,7,-2,5,-5,4,6,7,-9,4,10,-2,-5,8,-1,-1,3,8,2,1,-8,-3,8,-10,2,8,-5,2,3,5,8,6,3,7,9,5,2,2,7,-8,5,4,6,-1,5,4,3,7,6,-1,3,-2,1,6,5,8,1,1,5,-6,-9,6,-2,6,-10,-3,-3,9,-1,2,10,-8,-2,-10,-3,9,-9,-2,9,-1,6,-1,10,-5,-4,7,-8,7,-7,7,3,2,1,5,3,-9,9,-2,-8,10,-5,-8,-5,3,1,-10,3,8,-7,4,-6,-10,10,4,10,-2,10,-8,-8,-6,8,-5,9,5,-8,-5,1,-9,-9,1,-6,4,4,2,-10,10,6,1,1,-9,-6,-3,-2,-7,7,10,-10,3,4,-7,6,6,-5,7,-6,4,3,-8,4,-5,3,6,8,7,-7,-10,-2,-4,5,4,8,-3,9,-5,7,4,3,-3,-9,5,-7,-10,-1,-7,-8,8,-10,8,-2,-2,2,1,4,-8,-6,-1,-8,-3,7,-7,-2,-2,6,2,2,-9,8,10,5,8,-1,-4,2,-1,-7,4,3,-2,6,9,7,-2,9,8,-10,-3,7,-1,5,8,2,9,-7,-4,-4,1,-10,-6,-3,-3,3,5,3,9,-9,10,-8,-7,-2,8,-4,7,1,5,2,-6,-3,-6,-8,4,1,-9,5,-4,6,2,10,-6,-5,-5,-10,-3,-4,9,6,-9,7,4,5,8,-9,-1,-2,-1,1,-5,7,-2]], dtype = "uint32")#candidate|5351|(1, 392)|const|uint32
call_5350 = relay.TupleGetItem(func_3894_call(relay.reshape(const_5351.astype('uint32'), [392,])), 1)
call_5352 = relay.TupleGetItem(func_3897_call(relay.reshape(const_5351.astype('uint32'), [392,])), 1)
uop_5366 = relay.sqrt(const_5351.astype('float32')) # shape=(1, 392)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_5373 = func_3331_call()
call_5374 = func_3331_call()
func_2706_call = mod.get_global_var('func_2706')
func_2708_call = mutated_mod.get_global_var('func_2708')
var_5379 = relay.var("var_5379", dtype = "uint32", shape = (330,))#candidate|5379|(330,)|var|uint32
call_5378 = relay.TupleGetItem(func_2706_call(relay.reshape(var_5379.astype('uint32'), [330,])), 3)
call_5380 = relay.TupleGetItem(func_2708_call(relay.reshape(var_5379.astype('uint32'), [330,])), 3)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_5392 = func_3252_call()
call_5393 = func_3252_call()
output = relay.Tuple([bop_5347,call_5350,uop_5366,call_5373,call_5378,var_5379,call_5392,])
output2 = relay.Tuple([bop_5347,call_5352,uop_5366,call_5374,call_5380,var_5379,call_5393,])
func_5395 = relay.Function([var_5345,var_5346,var_5379,], output)
mod['func_5395'] = func_5395
mod = relay.transform.InferType()(mod)
mutated_mod['func_5395'] = func_5395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5395_call = mutated_mod.get_global_var('func_5395')
var_5397 = relay.var("var_5397", dtype = "uint32", shape = ())#candidate|5397|()|var|uint32
var_5398 = relay.var("var_5398", dtype = "uint32", shape = (1, 9, 5))#candidate|5398|(1, 9, 5)|var|uint32
var_5399 = relay.var("var_5399", dtype = "uint32", shape = (330,))#candidate|5399|(330,)|var|uint32
call_5396 = func_5395_call(var_5397,var_5398,var_5399,)
output = call_5396
func_5400 = relay.Function([var_5397,var_5398,var_5399,], output)
mutated_mod['func_5400'] = func_5400
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4911_call = mod.get_global_var('func_4911')
func_4912_call = mutated_mod.get_global_var('func_4912')
call_5415 = func_4911_call()
call_5416 = func_4911_call()
output = call_5415
output2 = call_5416
func_5429 = relay.Function([], output)
mod['func_5429'] = func_5429
mod = relay.transform.InferType()(mod)
mutated_mod['func_5429'] = func_5429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mutated_mod.get_global_var('func_5429')
call_5430 = func_5429_call()
output = call_5430
func_5431 = relay.Function([], output)
mutated_mod['func_5431'] = func_5431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3230_call = mod.get_global_var('func_3230')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_5473 = relay.TupleGetItem(func_3230_call(), 2)
call_5474 = relay.TupleGetItem(func_3231_call(), 2)
output = call_5473
output2 = call_5474
func_5479 = relay.Function([], output)
mod['func_5479'] = func_5479
mod = relay.transform.InferType()(mod)
output = func_5479()
func_5480 = relay.Function([], output)
mutated_mod['func_5480'] = func_5480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_5492 = func_3331_call()
call_5493 = func_3331_call()
output = call_5492
output2 = call_5493
func_5502 = relay.Function([], output)
mod['func_5502'] = func_5502
mod = relay.transform.InferType()(mod)
mutated_mod['func_5502'] = func_5502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5502_call = mutated_mod.get_global_var('func_5502')
call_5503 = func_5502_call()
output = call_5503
func_5504 = relay.Function([], output)
mutated_mod['func_5504'] = func_5504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5502_call = mod.get_global_var('func_5502')
func_5504_call = mutated_mod.get_global_var('func_5504')
call_5523 = func_5502_call()
call_5524 = func_5502_call()
output = relay.Tuple([call_5523,])
output2 = relay.Tuple([call_5524,])
func_5528 = relay.Function([], output)
mod['func_5528'] = func_5528
mod = relay.transform.InferType()(mod)
mutated_mod['func_5528'] = func_5528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5528_call = mutated_mod.get_global_var('func_5528')
call_5529 = func_5528_call()
output = call_5529
func_5530 = relay.Function([], output)
mutated_mod['func_5530'] = func_5530
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5561 = relay.var("var_5561", dtype = "int64", shape = ())#candidate|5561|()|var|int64
var_5562 = relay.var("var_5562", dtype = "int64", shape = (11, 4, 1))#candidate|5562|(11, 4, 1)|var|int64
bop_5563 = relay.greater_equal(var_5561.astype('bool'), var_5562.astype('bool')) # shape=(11, 4, 1)
output = relay.Tuple([bop_5563,])
output2 = relay.Tuple([bop_5563,])
func_5568 = relay.Function([var_5561,var_5562,], output)
mod['func_5568'] = func_5568
mod = relay.transform.InferType()(mod)
mutated_mod['func_5568'] = func_5568
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5568_call = mutated_mod.get_global_var('func_5568')
var_5570 = relay.var("var_5570", dtype = "int64", shape = ())#candidate|5570|()|var|int64
var_5571 = relay.var("var_5571", dtype = "int64", shape = (11, 4, 1))#candidate|5571|(11, 4, 1)|var|int64
call_5569 = func_5568_call(var_5570,var_5571,)
output = call_5569
func_5572 = relay.Function([var_5570,var_5571,], output)
mutated_mod['func_5572'] = func_5572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3950_call = mod.get_global_var('func_3950')
func_3951_call = mutated_mod.get_global_var('func_3951')
call_5597 = relay.TupleGetItem(func_3950_call(), 0)
call_5598 = relay.TupleGetItem(func_3951_call(), 0)
output = call_5597
output2 = call_5598
func_5601 = relay.Function([], output)
mod['func_5601'] = func_5601
mod = relay.transform.InferType()(mod)
mutated_mod['func_5601'] = func_5601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5601_call = mutated_mod.get_global_var('func_5601')
call_5602 = func_5601_call()
output = call_5602
func_5603 = relay.Function([], output)
mutated_mod['func_5603'] = func_5603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_5606 = relay.TupleGetItem(func_5035_call(), 2)
call_5607 = relay.TupleGetItem(func_5036_call(), 2)
output = relay.Tuple([call_5606,])
output2 = relay.Tuple([call_5607,])
func_5619 = relay.Function([], output)
mod['func_5619'] = func_5619
mod = relay.transform.InferType()(mod)
output = func_5619()
func_5620 = relay.Function([], output)
mutated_mod['func_5620'] = func_5620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4911_call = mod.get_global_var('func_4911')
func_4912_call = mutated_mod.get_global_var('func_4912')
call_5634 = func_4911_call()
call_5635 = func_4911_call()
func_4546_call = mod.get_global_var('func_4546')
func_4548_call = mutated_mod.get_global_var('func_4548')
const_5645 = relay.const([3.769876,9.075692,-1.801872,4.305228,1.113987,7.085245,-4.839078,-5.312793,-3.266950,4.827982,1.203557,0.512935,-0.790754,4.206404,6.133358,1.961870,3.437135,7.041809,-5.778306,-3.478691,-8.940321,-9.832080,-9.096452,-4.664397,6.809749,2.006568,0.346218,-5.168918,8.644710,1.342823,-7.073031,6.651846,2.070954,-9.095622,3.118111,1.564242,-4.106047,-7.636321,5.775804,4.474607,4.780805,9.952992,-2.740506,-0.528305,-9.749444,-4.685592,-0.540573,-4.150216,8.756420,0.697427,4.198758,-9.340586,-7.216013,-6.997935,0.551487,-9.481233,-0.898129,7.822055,7.493637,-2.027806,6.531172,0.739324,-8.191886,-6.490345,-1.326482,-1.660369,-4.472713,3.798968,-4.429924,-4.495371,3.026368,-1.726609], dtype = "float32")#candidate|5645|(72,)|const|float32
call_5644 = func_4546_call(relay.reshape(const_5645.astype('float32'), [3, 2, 12]))
call_5646 = func_4546_call(relay.reshape(const_5645.astype('float32'), [3, 2, 12]))
bop_5657 = relay.right_shift(call_5644.astype('uint16'), relay.reshape(const_5645.astype('uint16'), relay.shape_of(call_5644))) # shape=(3, 2, 12)
bop_5660 = relay.right_shift(call_5646.astype('uint16'), relay.reshape(const_5645.astype('uint16'), relay.shape_of(call_5646))) # shape=(3, 2, 12)
func_3359_call = mod.get_global_var('func_3359')
func_3362_call = mutated_mod.get_global_var('func_3362')
var_5668 = relay.var("var_5668", dtype = "uint64", shape = (784,))#candidate|5668|(784,)|var|uint64
call_5667 = relay.TupleGetItem(func_3359_call(relay.reshape(var_5668.astype('uint64'), [14, 14, 4])), 0)
call_5669 = relay.TupleGetItem(func_3362_call(relay.reshape(var_5668.astype('uint64'), [14, 14, 4])), 0)
bop_5687 = relay.power(call_5667.astype('float64'), relay.reshape(var_5668.astype('float64'), relay.shape_of(call_5667))) # shape=(14, 14, 4)
bop_5690 = relay.power(call_5669.astype('float64'), relay.reshape(var_5668.astype('float64'), relay.shape_of(call_5669))) # shape=(14, 14, 4)
func_4431_call = mod.get_global_var('func_4431')
func_4432_call = mutated_mod.get_global_var('func_4432')
call_5691 = relay.TupleGetItem(func_4431_call(), 0)
call_5692 = relay.TupleGetItem(func_4432_call(), 0)
output = relay.Tuple([call_5634,bop_5657,bop_5687,call_5691,])
output2 = relay.Tuple([call_5635,bop_5660,bop_5690,call_5692,])
func_5697 = relay.Function([var_5668,], output)
mod['func_5697'] = func_5697
mod = relay.transform.InferType()(mod)
mutated_mod['func_5697'] = func_5697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5698 = relay.var("var_5698", dtype = "uint64", shape = (784,))#candidate|5698|(784,)|var|uint64
func_5697_call = mutated_mod.get_global_var('func_5697')
call_5699 = func_5697_call(var_5698)
output = call_5699
func_5700 = relay.Function([var_5698], output)
mutated_mod['func_5700'] = func_5700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_5706 = relay.TupleGetItem(func_2912_call(), 3)
call_5707 = relay.TupleGetItem(func_2913_call(), 3)
var_5710 = relay.var("var_5710", dtype = "float32", shape = (847, 11))#candidate|5710|(847, 11)|var|float32
bop_5711 = relay.add(call_5706.astype('int64'), var_5710.astype('int64')) # shape=(847, 11)
bop_5714 = relay.add(call_5707.astype('int64'), var_5710.astype('int64')) # shape=(847, 11)
output = bop_5711
output2 = bop_5714
func_5715 = relay.Function([var_5710,], output)
mod['func_5715'] = func_5715
mod = relay.transform.InferType()(mod)
mutated_mod['func_5715'] = func_5715
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5716 = relay.var("var_5716", dtype = "float32", shape = (847, 11))#candidate|5716|(847, 11)|var|float32
func_5715_call = mutated_mod.get_global_var('func_5715')
call_5717 = func_5715_call(var_5716)
output = call_5717
func_5718 = relay.Function([var_5716], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5765 = relay.const([[[-5.664505,-3.934363,-4.531458]],[[-3.659669,8.344431,2.151056]],[[-2.807270,4.544224,-4.694809]]], dtype = "float64")#candidate|5765|(3, 1, 3)|const|float64
uop_5766 = relay.atan(const_5765.astype('float64')) # shape=(3, 1, 3)
func_2278_call = mod.get_global_var('func_2278')
func_2282_call = mutated_mod.get_global_var('func_2282')
var_5775 = relay.var("var_5775", dtype = "float64", shape = (26,))#candidate|5775|(26,)|var|float64
const_5776 = relay.const([7,3,6,8,-2,3,-2,-6,4,-2,2,-3,3,-1,-3,9,4,2,9,5,10,-1,-2,3,-8,9,3,4,4,-6,-6,5,-8,-8,-8,10,-3,-2,1,-5,10,-1,-3,-10,2,2,-10,8,5,-7,-10,-10,-2,-2,-8,2,-8,-1,-9,8,7,-9,-6,-7,4,-5,-2,1,-7,-5,-9,-3,9,8,6,-1,-3,-2,-9,3,2,2,-2,6,-6,-6,-7,2,4,-7,-3,5,-9,8,-3,-3,-8,9,-8,1,5,8,8,-9,9,5,4,-1,-7,1,1,-7,9,-1,8,-10,9,6,-10,-10,-2,-5,6,-7,9,5,10,-1,7,-7,-3,-9,-6,10,9,-9,6,5,-1,7,10,10,-3,10,-4,-4,-3,1,-5,7,4,4,9,-4,-4,2,10,-4,4,2,9,7,8,-3,-3,-8,6,7,-1,-8,9,-9,-4,3,-6,-10,-8,9,6,-10,10,-6,-9,-4,1,5,3,-10,-6,-9,-5,-7,5,-10,8,10,7,6,8,-6,3,-10,7,5,2,-8,-2,-1,-3,-8,2,-10,-3,-6,-6,9,-6,-8,-8,10,7,-8,-3,6,1,-6,3,3,-2,-8,-3,-10,7,-4,10,-6,2,-8,2,-10,7,7,3,5,-8,6,1,2,1,-2,10,10,1,-6,1,5,5,9,1,-5,-8,-2,-4,-4,8,8,5,1,-5,8,-6,-7,2,-1,9,-1,7,-3,-6,6,4,-6,-1,4,6,5,4,3,5,8,-9,2,-4,7,-3,-6,6,-7,-8,6,-4,6,-10,-3,-2,-2,1,7,8,-5,-6,1,4,-2,10,8,6,1,2,4,4,-5,9,-10,7,-9,8,-6,9,-7], dtype = "uint32")#candidate|5776|(330,)|const|uint32
call_5774 = relay.TupleGetItem(func_2278_call(relay.reshape(var_5775.astype('float64'), [13, 2, 1]), relay.reshape(const_5776.astype('uint32'), [330,]), ), 1)
call_5777 = relay.TupleGetItem(func_2282_call(relay.reshape(var_5775.astype('float64'), [13, 2, 1]), relay.reshape(const_5776.astype('uint32'), [330,]), ), 1)
uop_5779 = relay.acos(uop_5766.astype('float32')) # shape=(3, 1, 3)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_5790 = func_2949_call()
call_5791 = func_2949_call()
output = relay.Tuple([call_5774,var_5775,const_5776,uop_5779,call_5790,])
output2 = relay.Tuple([call_5777,var_5775,const_5776,uop_5779,call_5791,])
func_5795 = relay.Function([var_5775,], output)
mod['func_5795'] = func_5795
mod = relay.transform.InferType()(mod)
mutated_mod['func_5795'] = func_5795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5796 = relay.var("var_5796", dtype = "float64", shape = (26,))#candidate|5796|(26,)|var|float64
func_5795_call = mutated_mod.get_global_var('func_5795')
call_5797 = func_5795_call(var_5796)
output = call_5797
func_5798 = relay.Function([var_5796], output)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5479_call = mod.get_global_var('func_5479')
func_5480_call = mutated_mod.get_global_var('func_5480')
call_5932 = func_5479_call()
call_5933 = func_5479_call()
func_3318_call = mod.get_global_var('func_3318')
func_3320_call = mutated_mod.get_global_var('func_3320')
call_5951 = relay.TupleGetItem(func_3318_call(), 2)
call_5952 = relay.TupleGetItem(func_3320_call(), 2)
output = relay.Tuple([call_5932,call_5951,])
output2 = relay.Tuple([call_5933,call_5952,])
func_5955 = relay.Function([], output)
mod['func_5955'] = func_5955
mod = relay.transform.InferType()(mod)
output = func_5955()
func_5956 = relay.Function([], output)
mutated_mod['func_5956'] = func_5956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5300_call = mod.get_global_var('func_5300')
func_5301_call = mutated_mod.get_global_var('func_5301')
call_6008 = relay.TupleGetItem(func_5300_call(), 0)
call_6009 = relay.TupleGetItem(func_5301_call(), 0)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_6027 = func_3252_call()
call_6028 = func_3252_call()
output = relay.Tuple([call_6008,call_6027,])
output2 = relay.Tuple([call_6009,call_6028,])
func_6034 = relay.Function([], output)
mod['func_6034'] = func_6034
mod = relay.transform.InferType()(mod)
output = func_6034()
func_6035 = relay.Function([], output)
mutated_mod['func_6035'] = func_6035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4753_call = mod.get_global_var('func_4753')
func_4754_call = mutated_mod.get_global_var('func_4754')
call_6062 = func_4753_call()
call_6063 = func_4753_call()
output = relay.Tuple([call_6062,])
output2 = relay.Tuple([call_6063,])
func_6067 = relay.Function([], output)
mod['func_6067'] = func_6067
mod = relay.transform.InferType()(mod)
output = func_6067()
func_6068 = relay.Function([], output)
mutated_mod['func_6068'] = func_6068
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6069 = relay.var("var_6069", dtype = "float64", shape = (13, 11, 14))#candidate|6069|(13, 11, 14)|var|float64
uop_6070 = relay.sin(var_6069.astype('float64')) # shape=(13, 11, 14)
func_5528_call = mod.get_global_var('func_5528')
func_5530_call = mutated_mod.get_global_var('func_5530')
call_6072 = relay.TupleGetItem(func_5528_call(), 0)
call_6073 = relay.TupleGetItem(func_5530_call(), 0)
output = relay.Tuple([uop_6070,call_6072,])
output2 = relay.Tuple([uop_6070,call_6073,])
func_6079 = relay.Function([var_6069,], output)
mod['func_6079'] = func_6079
mod = relay.transform.InferType()(mod)
var_6080 = relay.var("var_6080", dtype = "float64", shape = (13, 11, 14))#candidate|6080|(13, 11, 14)|var|float64
output = func_6079(var_6080)
func_6081 = relay.Function([var_6080], output)
mutated_mod['func_6081'] = func_6081
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_6089 = relay.TupleGetItem(func_4398_call(), 2)
call_6090 = relay.TupleGetItem(func_4399_call(), 2)
output = relay.Tuple([call_6089,])
output2 = relay.Tuple([call_6090,])
func_6094 = relay.Function([], output)
mod['func_6094'] = func_6094
mod = relay.transform.InferType()(mod)
mutated_mod['func_6094'] = func_6094
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6094_call = mutated_mod.get_global_var('func_6094')
call_6095 = func_6094_call()
output = call_6095
func_6096 = relay.Function([], output)
mutated_mod['func_6096'] = func_6096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_6146 = func_2444_call()
call_6147 = func_2444_call()
var_6187 = relay.var("var_6187", dtype = "float32", shape = (15, 1, 3))#candidate|6187|(15, 1, 3)|var|float32
bop_6188 = relay.right_shift(call_6146.astype('int64'), relay.reshape(var_6187.astype('int64'), relay.shape_of(call_6146))) # shape=(15, 1, 3)
bop_6191 = relay.right_shift(call_6147.astype('int64'), relay.reshape(var_6187.astype('int64'), relay.shape_of(call_6147))) # shape=(15, 1, 3)
func_5429_call = mod.get_global_var('func_5429')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_6192 = func_5429_call()
call_6193 = func_5429_call()
func_5395_call = mod.get_global_var('func_5395')
func_5400_call = mutated_mod.get_global_var('func_5400')
const_6220 = relay.const(1, dtype = "uint32")#candidate|6220|()|const|uint32
var_6221 = relay.var("var_6221", dtype = "uint32", shape = (330,))#candidate|6221|(330,)|var|uint32
call_6219 = relay.TupleGetItem(func_5395_call(relay.reshape(const_6220.astype('uint32'), []), relay.reshape(call_6146.astype('uint32'), [1, 9, 5]), relay.reshape(var_6221.astype('uint32'), [330,]), ), 1)
call_6222 = relay.TupleGetItem(func_5400_call(relay.reshape(const_6220.astype('uint32'), []), relay.reshape(call_6146.astype('uint32'), [1, 9, 5]), relay.reshape(var_6221.astype('uint32'), [330,]), ), 1)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_6223 = func_3331_call()
call_6224 = func_3331_call()
func_4674_call = mod.get_global_var('func_4674')
func_4678_call = mutated_mod.get_global_var('func_4678')
const_6230 = relay.const([6,-6,-5,4,8,-3,-10,1,-5,-7,4,-9,-2,3,6,-2,2,-3,-10,-10,-7,-7,3,8,8,-5,1,9,10,9,-3,-8,8,-2,2,-9,3,3,5,8,-1,10,-6,5,2,-3,4,-8,5,-3,1,6,-9,2,2,-1,-4,5,9,-7,4,6,3,10,-5,5,-6,-10,1,1,3,-8,-3,6,-5,-3,-4,8,-2,-3,3,10,2,4,-3,9,-9,2,2,-1,2,-7,-10,2,-5,-8,-7,-8,8,4,-1,9,10,9,1,10,-4,2,1,-8,2,-5,-4,-10,6,-6,-5,-4,-8,8,5,-5,-4,-2,2,3,6,5,-2,-4,6,-5,5,-9,-4,-2,-4,7,5,-5,1,-1,6,7,-10,4,1,9,3,-8,-5,-8,-9,-7,6,9,7,-4,-5,-1,-4,-1,6,-2,9,8,2,5], dtype = "int64")#candidate|6230|(168,)|const|int64
var_6231 = relay.var("var_6231", dtype = "float32", shape = (640,))#candidate|6231|(640,)|var|float32
call_6229 = relay.TupleGetItem(func_4674_call(relay.reshape(const_6230.astype('int64'), [168,]), relay.reshape(var_6231.astype('float32'), [320, 2]), ), 1)
call_6232 = relay.TupleGetItem(func_4678_call(relay.reshape(const_6230.astype('int64'), [168,]), relay.reshape(var_6231.astype('float32'), [320, 2]), ), 1)
output = relay.Tuple([bop_6188,call_6192,call_6219,const_6220,var_6221,call_6223,call_6229,const_6230,var_6231,])
output2 = relay.Tuple([bop_6191,call_6193,call_6222,const_6220,var_6221,call_6224,call_6232,const_6230,var_6231,])
func_6239 = relay.Function([var_6187,var_6221,var_6231,], output)
mod['func_6239'] = func_6239
mod = relay.transform.InferType()(mod)
var_6240 = relay.var("var_6240", dtype = "float32", shape = (15, 1, 3))#candidate|6240|(15, 1, 3)|var|float32
var_6241 = relay.var("var_6241", dtype = "uint32", shape = (330,))#candidate|6241|(330,)|var|uint32
var_6242 = relay.var("var_6242", dtype = "float32", shape = (640,))#candidate|6242|(640,)|var|float32
output = func_6239(var_6240,var_6241,var_6242,)
func_6243 = relay.Function([var_6240,var_6241,var_6242,], output)
mutated_mod['func_6243'] = func_6243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_6245 = relay.TupleGetItem(func_2183_call(), 1)
call_6246 = relay.TupleGetItem(func_2185_call(), 1)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_6247 = func_2949_call()
call_6248 = func_2949_call()
output = relay.Tuple([call_6245,call_6247,])
output2 = relay.Tuple([call_6246,call_6248,])
func_6264 = relay.Function([], output)
mod['func_6264'] = func_6264
mod = relay.transform.InferType()(mod)
output = func_6264()
func_6265 = relay.Function([], output)
mutated_mod['func_6265'] = func_6265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4358_call = mod.get_global_var('func_4358')
func_4360_call = mutated_mod.get_global_var('func_4360')
call_6270 = relay.TupleGetItem(func_4358_call(), 0)
call_6271 = relay.TupleGetItem(func_4360_call(), 0)
func_4358_call = mod.get_global_var('func_4358')
func_4360_call = mutated_mod.get_global_var('func_4360')
call_6275 = relay.TupleGetItem(func_4358_call(), 0)
call_6276 = relay.TupleGetItem(func_4360_call(), 0)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_6280 = relay.TupleGetItem(func_2183_call(), 0)
call_6281 = relay.TupleGetItem(func_2185_call(), 0)
output = relay.Tuple([call_6270,call_6275,call_6280,])
output2 = relay.Tuple([call_6271,call_6276,call_6281,])
func_6292 = relay.Function([], output)
mod['func_6292'] = func_6292
mod = relay.transform.InferType()(mod)
output = func_6292()
func_6293 = relay.Function([], output)
mutated_mod['func_6293'] = func_6293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6299 = relay.var("var_6299", dtype = "bool", shape = ())#candidate|6299|()|var|bool
const_6300 = relay.const([[[False,False,True,True,False,True,False,False],[False,True,True,False,True,False,False,False],[False,True,False,False,True,True,False,False],[False,True,True,True,True,False,True,True],[True,False,False,True,True,True,False,False],[False,True,False,True,True,True,False,True],[False,False,True,False,True,False,False,True],[True,True,True,False,False,False,False,True],[True,False,False,False,True,False,False,True],[False,True,True,True,False,True,True,False],[True,False,False,False,False,False,False,True],[False,True,False,False,True,False,True,False],[False,True,True,False,False,True,True,False]],[[False,False,True,False,True,False,True,False],[True,True,True,True,False,True,True,False],[False,True,False,True,True,True,False,True],[False,True,True,False,False,True,False,True],[True,False,True,True,False,False,True,True],[False,False,True,False,True,False,False,True],[True,False,True,False,True,True,True,True],[False,True,False,False,False,False,True,True],[False,True,False,True,True,False,False,True],[False,True,True,False,True,True,True,False],[True,False,False,False,True,False,False,True],[True,False,False,True,False,True,False,True],[False,True,False,False,True,False,True,True]],[[False,True,True,True,False,True,False,False],[True,False,False,True,False,False,False,True],[False,False,False,True,False,True,False,False],[False,False,False,True,False,False,False,False],[True,False,False,True,True,False,True,False],[False,False,True,True,False,False,False,True],[False,True,False,False,False,False,True,False],[False,True,True,False,True,True,True,False],[True,True,False,False,True,True,True,True],[True,False,False,False,False,True,True,True],[False,True,True,False,True,False,False,True],[False,True,True,True,False,False,False,False],[True,False,False,False,True,True,False,True]],[[False,False,True,False,True,False,True,True],[True,True,True,False,True,True,True,True],[False,False,True,True,True,True,True,False],[True,True,True,False,True,True,True,True],[True,False,True,True,False,True,False,True],[False,False,True,True,True,False,True,False],[True,False,True,False,True,False,False,False],[True,True,False,False,False,False,True,False],[False,True,True,True,False,True,False,False],[True,False,True,True,False,False,True,True],[False,False,True,True,False,False,True,True],[True,False,False,False,False,True,False,False],[False,True,True,False,False,False,False,False]],[[False,False,True,False,False,False,False,True],[False,True,False,False,True,False,True,True],[False,True,True,False,True,True,False,True],[False,False,False,False,False,False,False,False],[False,True,False,True,True,False,False,True],[False,False,True,True,False,True,False,False],[False,True,False,True,False,True,True,False],[True,True,True,True,True,True,True,False],[True,True,True,False,False,True,False,False],[True,True,True,False,False,False,False,True],[True,True,False,False,False,True,False,True],[False,True,False,False,True,True,False,False],[False,True,False,False,False,False,False,True]],[[False,False,True,False,False,False,True,True],[True,False,True,True,True,False,False,False],[True,False,False,False,True,False,False,True],[True,True,False,True,True,False,False,True],[False,False,False,False,False,True,False,True],[True,True,False,True,True,False,True,True],[False,True,True,True,True,False,False,False],[True,False,True,False,True,True,False,True],[True,False,False,True,True,False,False,True],[True,False,False,True,False,True,False,False],[False,True,True,True,True,False,True,False],[False,False,True,True,True,True,True,True],[True,True,False,False,True,True,True,False]]], dtype = "bool")#candidate|6300|(6, 13, 8)|const|bool
bop_6301 = relay.logical_and(var_6299.astype('bool'), const_6300.astype('bool')) # shape=(6, 13, 8)
output = relay.Tuple([bop_6301,])
output2 = relay.Tuple([bop_6301,])
func_6307 = relay.Function([var_6299,], output)
mod['func_6307'] = func_6307
mod = relay.transform.InferType()(mod)
mutated_mod['func_6307'] = func_6307
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6308 = relay.var("var_6308", dtype = "bool", shape = ())#candidate|6308|()|var|bool
func_6307_call = mutated_mod.get_global_var('func_6307')
call_6309 = func_6307_call(var_6308)
output = call_6309
func_6310 = relay.Function([var_6308], output)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4753_call = mod.get_global_var('func_4753')
func_4754_call = mutated_mod.get_global_var('func_4754')
call_6384 = func_4753_call()
call_6385 = func_4753_call()
output = call_6384
output2 = call_6385
func_6388 = relay.Function([], output)
mod['func_6388'] = func_6388
mod = relay.transform.InferType()(mod)
output = func_6388()
func_6389 = relay.Function([], output)
mutated_mod['func_6389'] = func_6389
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_6393 = relay.TupleGetItem(func_2183_call(), 4)
call_6394 = relay.TupleGetItem(func_2185_call(), 4)
const_6397 = relay.const([-8.891102,-1.266564,-1.652013,-2.942443,6.533980,-5.607745,-4.463888,3.316123,-0.518507,-9.554229,-0.162648,4.839137,2.786221,-9.364786,-4.747142,-6.928508,0.652359,-3.780009,3.135254,5.829303,8.587917,-8.026152,4.107508,-3.433191,0.639518,-8.804179,8.178914,9.374499,-4.231527,4.016093,-1.775612,5.318403,9.569293,4.301387,4.156675,4.195840], dtype = "float64")#candidate|6397|(36,)|const|float64
bop_6398 = relay.greater_equal(call_6393.astype('bool'), relay.reshape(const_6397.astype('bool'), relay.shape_of(call_6393))) # shape=(36,)
bop_6401 = relay.greater_equal(call_6394.astype('bool'), relay.reshape(const_6397.astype('bool'), relay.shape_of(call_6394))) # shape=(36,)
output = bop_6398
output2 = bop_6401
func_6402 = relay.Function([], output)
mod['func_6402'] = func_6402
mod = relay.transform.InferType()(mod)
output = func_6402()
func_6403 = relay.Function([], output)
mutated_mod['func_6403'] = func_6403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5479_call = mod.get_global_var('func_5479')
func_5480_call = mutated_mod.get_global_var('func_5480')
call_6420 = func_5479_call()
call_6421 = func_5479_call()
func_2444_call = mod.get_global_var('func_2444')
func_2445_call = mutated_mod.get_global_var('func_2445')
call_6426 = func_2444_call()
call_6427 = func_2444_call()
func_5697_call = mod.get_global_var('func_5697')
func_5700_call = mutated_mod.get_global_var('func_5700')
const_6435 = relay.const([-9,-3,7,-4,-7,-2,-6,-9,-10,7,5,-2,-8,-9,5,4,-8,7,-1,2,1,-10,-3,-1,9,2,1,-2,-2,-9,-9,-1,10,-4,-10,-8,10,-7,7,7,-5,2,3,-4,-7,2,-8,2,-2,10,5,-4,-7,8,-8,-4,2,-10,1,9,-8,1,5,-7,-2,-10,6,1,-4,9,-4,8,10,4,-1,7,-6,-9,-4,10,3,4,-4,3,6,4,9,-9,-2,-8,5,-4,6,2,10,-7,-3,-2,-7,-9,-1,6,-6,6,-7,-1,-2,5,-8,7,10,1,-6,-2,-10,-8,3,10,9,7,2,10,3,-1,4,-1,3,-8,6,2,1,6,5,5,-2,2,10,-8,-9,6,-9,10,10,1,-9,4,4,-6,-8,5,-1,3,-2,4,2,-7,-6,2,-4,-2,7,-3,-7,-2,-7,-4,7,-10,10,10,-4,2,-3,-6,7,-10,-5,7,-9,7,-9,6,10,-5,-2,2,-2,-7,-7,2,10,-10,4,-9,8,10,-6,-3,4,7,-3,-3,-3,1,-3,6,6,10,-5,4,-4,-3,3,-9,4,-7,6,5,10,9,-1,-7,-3,9,-6,3,1,2,-4,5,10,-6,-1,4,-6,-3,8,-6,-8,10,1,-6,9,-6,-1,-10,2,5,-6,-3,2,9,-9,-2,1,-1,-5,-7,-4,-7,6,6,-5,9,2,2,-9,7,-8,-5,10,3,10,10,-3,-9,-6,6,5,-3,-9,-2,-7,-8,-7,6,-6,1,-1,2,-7,4,5,7,5,-7,-4,-3,-10,-8,4,2,-6,-10,5,-4,10,-8,-8,-4,-2,9,2,10,5,-8,-5,10,7,-10,-9,-3,-2,5,5,-3,2,4,6,-7,2,-7,-8,-8,-7,5,3,-7,10,-5,9,1,-1,-7,-9,-5,10,9,1,2,6,-3,9,3,10,-6,5,-2,4,-1,-2,5,-10,-1,-2,6,4,6,-7,-5,-7,8,8,-6,9,-7,-6,4,-9,-5,-10,10,10,7,6,-8,1,-3,-8,-1,-8,10,1,10,-1,-2,5,2,7,-7,-1,4,-3,-1,7,9,-2,-9,-5,4,3,-4,5,8,-7,-7,-9,8,-7,2,3,-1,-10,-8,1,-10,8,-7,-2,-9,9,7,4,-10,6,-8,5,4,2,-2,-5,-9,8,8,-8,-9,2,5,-3,8,10,8,5,-5,-5,-10,-1,5,-5,-9,1,-2,-6,-8,5,-6,-2,-2,-8,4,4,-6,-2,-4,6,-2,1,-2,2,-6,6,3,6,-4,2,10,1,1,-6,4,8,3,-1,-6,4,1,-4,7,8,6,9,-8,-3,6,3,3,8,-1,-10,-2,-1,-4,7,-8,-3,7,-2,6,3,5,4,7,8,8,9,4,-5,6,10,-7,10,-8,-8,-8,-6,6,2,9,3,8,9,1,-10,6,-3,-4,-6,5,-7,-2,5,3,1,-9,-3,-6,1,-6,4,-3,-4,10,-1,1,-6,-1,1,10,7,-6,-8,-3,-8,2,-3,-1,-1,-5,5,-8,-9,2,4,3,3,2,-10,2,5,3,8,5,6,10,7,10,1,-7,-8,-8,8,6,-6,9,2,-1,8,10,7,-3,9,10,9,-7,-8,10,5,-5,4,-4,7,-9,-1,-9,8,-1,-7,-9,10,5,-10,-3,3,-6,3,-7,7,-5,4,7,8,-9,10,-3,-5,-8,7,10,9,-1,7,-5,4,3,6,8,-9,-8,8,-1,2,-5,-1,9,2,4,-7,-6,-1,-7,-10,-10,5,-1,-1,-3,2,-10,-7,-2,-10,-10,5,6,-6,2,1,6,10,-8,-10,2,2,-4,4,8,2,8,4,5,10,-8,7,-8,1,-8,10,-4,3,-1,-4,10,7,-7,-4,2,8,-7,-4,-4,3,-6,1,5,-8,2,5,1,-9,-6,-1,-1,8,7,-2,-7,-2,-8,-4,8,9,-5,-9,-10,-7,5,5,-8,-3,7,6,2,8,1,-3,4,-7,10,-7,6,5,1,-9,-4,-4,8,2,5,10,-2,5,6,-6,7,7,9,-7,1,-9,-8,4,2,6,8], dtype = "uint64")#candidate|6435|(784,)|const|uint64
call_6434 = relay.TupleGetItem(func_5697_call(relay.reshape(const_6435.astype('uint64'), [784,])), 1)
call_6436 = relay.TupleGetItem(func_5700_call(relay.reshape(const_6435.astype('uint64'), [784,])), 1)
output = relay.Tuple([call_6420,call_6426,call_6434,const_6435,])
output2 = relay.Tuple([call_6421,call_6427,call_6436,const_6435,])
func_6456 = relay.Function([], output)
mod['func_6456'] = func_6456
mod = relay.transform.InferType()(mod)
output = func_6456()
func_6457 = relay.Function([], output)
mutated_mod['func_6457'] = func_6457
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6461 = relay.var("var_6461", dtype = "int16", shape = (15, 9, 14))#candidate|6461|(15, 9, 14)|var|int16
const_6462 = relay.const([[[8,7,-6,-2,-2,5,-7,-10,9,6,-1,-4,10,-2],[-10,8,-8,8,3,10,7,9,-6,-10,-3,8,9,-2],[1,-3,-6,-10,8,-8,-10,-8,4,10,-6,-6,1,2],[5,8,-8,8,3,-8,-6,2,7,-4,5,10,6,-2],[-9,6,8,1,-8,2,6,10,8,-9,-2,-5,-9,-10],[-10,-4,7,-4,-8,3,-5,5,4,-3,-9,-7,-7,10],[7,3,-2,-6,-6,6,-7,-10,-3,-2,-2,1,-1,-2],[1,4,-2,3,3,3,-2,-5,-7,1,-10,8,2,-3],[8,-1,7,-4,4,1,1,-1,2,-1,-3,-8,7,-6]],[[7,-2,-7,3,8,-3,7,2,-9,-10,-10,-9,-5,-9],[4,3,-7,6,6,9,9,8,7,3,-4,-8,-5,-1],[-3,7,6,-9,-3,-8,-6,-4,-9,10,-4,-6,7,-7],[9,7,8,1,3,8,7,-6,-1,8,5,-7,-1,9],[7,2,-6,9,-2,10,2,-1,2,-2,10,-4,-5,5],[-6,-4,2,8,-5,-2,9,2,7,-10,3,-3,-1,-9],[8,4,8,-6,6,-8,10,7,1,-9,-3,9,-3,8],[-9,-10,-10,-10,4,1,-9,10,1,9,5,10,8,-3],[-4,-5,-9,-10,1,9,8,-5,1,6,-1,3,2,-3]],[[5,-3,8,-1,-3,5,-5,-9,-6,-1,10,-8,4,-6],[-5,9,6,8,-10,-10,-2,-6,1,1,10,6,-1,10],[6,-2,-6,10,4,5,-10,6,-9,-10,-8,8,3,9],[-8,9,-6,4,3,3,5,1,2,-7,10,1,-6,-9],[5,-3,8,9,-5,7,9,7,-7,-7,-8,9,-10,9],[1,7,7,-1,3,10,-2,-8,-6,-5,7,-1,8,6],[-10,6,-4,-9,4,-7,-9,7,-5,-4,-1,-5,3,-5],[6,1,-6,-9,-1,-1,-8,3,7,-9,-4,5,-2,-4],[-6,7,10,-10,-4,-7,7,1,-8,3,4,-10,-4,4]],[[5,2,6,-5,-7,3,4,-10,5,6,-8,9,-10,-10],[5,-2,-1,4,-8,-4,-2,8,-4,-6,-2,4,-1,1],[3,-8,5,-1,-6,6,3,-9,-6,2,-9,-2,-1,10],[1,-3,-3,7,1,-6,4,-3,1,-6,2,8,-6,-10],[-9,9,4,-6,-3,4,-2,2,-10,5,-8,-8,-6,-10],[1,9,2,9,10,-2,-10,-6,7,-8,-5,-10,-3,3],[-9,4,-5,-7,1,-5,-5,3,-3,10,10,-9,-3,8],[-9,5,-4,-7,2,-9,2,-5,1,4,10,6,-4,-3],[-5,-2,3,-2,8,7,-3,-4,-10,-4,6,3,-4,6]],[[-3,6,1,2,-7,1,4,-5,6,-4,8,-7,7,-2],[8,-10,6,-1,-4,-3,7,-6,5,2,1,-8,-5,3],[5,-5,-3,8,-1,-8,-1,-5,6,3,-3,3,-8,-2],[5,5,1,5,-4,-5,1,1,-6,-2,8,-2,-8,-6],[5,9,5,2,-7,2,-9,8,2,-1,6,1,-7,-8],[9,1,-3,-5,-8,6,3,7,-7,-1,-4,7,6,-5],[-10,-9,-6,4,5,-8,4,10,-4,-9,-4,1,-5,-8],[-6,-5,6,7,8,-9,-9,-8,3,-10,7,-9,2,-8],[8,-7,9,-3,7,6,1,10,6,-3,-6,-7,6,1]],[[-6,2,-7,10,-2,2,3,7,-5,4,-5,-10,3,3],[5,-7,4,-7,-10,-6,10,-4,-8,-8,9,4,-10,4],[-4,-5,10,-2,-1,3,7,-4,9,-1,10,-10,3,3],[-10,9,2,5,-3,-6,7,6,3,3,9,-9,-5,-7],[2,-2,-7,-8,-6,-2,-1,5,-2,-4,-10,-6,-2,7],[-5,6,4,-10,10,1,1,6,4,2,10,-2,4,9],[-5,3,-9,-7,-8,6,-5,3,2,9,-1,-5,-6,1],[-5,4,-7,9,-6,10,3,4,-5,-5,-6,-7,3,8],[-7,7,-1,1,10,3,6,9,-1,9,-10,7,9,5]],[[-3,1,-5,-1,9,-4,4,4,3,1,-8,2,-5,8],[-2,-5,-7,5,5,8,-10,3,-10,-3,-2,-8,7,10],[8,7,10,-5,8,-3,-5,-7,3,-6,8,-7,8,-3],[-5,8,-1,-5,6,-10,-9,-7,3,-7,5,3,-7,-6],[-6,-9,-9,6,1,-3,-1,-1,-7,5,4,8,9,3],[-2,10,-5,10,-7,8,-10,-3,5,1,4,-1,10,-8],[-3,-5,-9,4,6,-9,-2,1,7,3,9,3,-4,2],[6,-2,-10,-5,-6,2,-4,-6,-10,-10,-10,9,9,-5],[-6,6,8,2,-9,-6,7,6,10,2,7,-7,5,8]],[[-7,6,1,-5,1,4,4,4,9,7,-2,-9,10,-7],[1,-8,10,2,-7,-8,-4,-10,-4,4,-4,3,9,-4],[8,-4,9,-9,-6,-8,-10,3,1,-4,8,8,-10,-8],[3,-8,5,3,-3,-3,-5,-6,-9,1,-4,7,-5,-6],[8,-2,7,-3,3,6,-10,9,-10,-10,-3,3,6,-1],[-6,3,-2,6,-8,-2,7,-9,7,-2,-2,-7,3,-4],[9,1,-4,-9,1,6,4,-10,-5,8,6,8,4,5],[-5,-8,8,-2,-4,-9,-6,-4,-4,-3,-5,1,-3,-1],[6,4,-7,-8,2,7,2,-10,-2,1,1,7,9,7]],[[-8,-8,-4,-8,5,-6,-7,-4,1,-9,8,-1,8,-5],[9,-6,2,-1,-6,-9,-6,-9,-10,-4,-7,-3,5,-6],[-3,7,-4,-9,6,-5,3,-5,-9,-4,9,9,10,-5],[-8,-7,3,-5,6,-5,7,7,2,-9,-10,1,10,7],[3,-5,2,-2,-6,4,-2,-6,-7,-7,7,-1,8,8],[3,7,7,5,-6,6,5,-5,7,5,6,-2,-7,-2],[6,-4,7,-2,-5,-6,5,4,10,-6,1,-10,3,-10],[6,7,1,-8,3,3,-9,9,-8,4,2,-6,3,-10],[7,-9,1,4,7,2,-6,-8,-3,8,3,1,6,-10]],[[3,-5,9,5,10,-4,5,-7,-1,5,5,5,-7,-3],[4,-10,-1,-9,-9,-2,6,-3,2,-2,-6,-6,10,9],[8,10,3,-10,7,7,-8,2,-7,-6,7,-3,-3,-4],[-2,10,-4,3,2,-4,-7,-2,3,10,9,10,-4,-8],[4,1,6,-6,-6,8,4,-7,-6,-7,-3,9,-3,-7],[-4,5,9,-3,-1,-5,-10,5,6,7,10,-1,1,4],[-10,2,-8,-3,-4,9,-7,-2,-7,3,8,-7,5,9],[9,9,-4,5,-9,8,5,1,-2,-9,2,4,3,6],[1,-4,-9,-4,-6,-7,-7,10,-4,6,-6,7,-8,-5]],[[4,8,7,10,7,-2,-2,7,6,1,-8,6,-3,-9],[-5,1,6,-7,-3,2,10,10,5,-1,-5,-2,9,-7],[2,3,-10,7,8,-10,2,9,-6,-3,-8,-3,-7,8],[-7,-10,2,-6,-2,10,-10,8,-4,3,-8,2,-1,1],[-4,-7,5,-9,3,-9,10,-4,4,2,1,-10,2,-8],[-9,-4,-9,3,8,-1,7,5,-1,-6,3,3,-3,-4],[4,-9,-1,7,2,4,-10,-1,6,4,5,4,-8,-1],[-9,6,-6,-8,10,7,-3,-3,5,-2,10,-10,-6,4],[-3,-6,9,-8,9,-2,-9,-2,-9,7,-7,-6,-7,-5]],[[-3,8,3,10,8,-8,2,-5,-8,-5,-9,10,-5,6],[-3,6,9,3,10,5,9,-6,-5,4,-7,2,-5,-6],[9,4,-3,9,6,4,-3,-5,-6,5,-1,9,-10,-6],[3,5,1,3,10,6,4,-4,-2,-9,-2,-2,-3,-1],[-1,-10,-8,-6,6,5,-3,-4,2,4,-10,6,9,-5],[8,7,-2,6,2,8,-3,-6,5,-3,-9,-3,-4,-1],[7,-7,-1,-8,1,-4,6,-3,-7,5,-8,-1,7,-3],[2,-4,-9,8,5,-6,10,9,4,-2,10,2,-6,-2],[6,-6,1,-1,-2,4,-5,-4,-8,10,7,-2,-1,-3]],[[-9,2,4,6,-9,-8,8,-8,2,-7,-7,4,-10,10],[-1,8,2,7,-9,1,-2,9,-3,-2,-1,7,5,-1],[-6,-4,-6,10,4,1,-10,9,5,9,-5,3,9,3],[1,-1,-4,7,9,7,-3,-5,5,5,4,-8,-7,6],[-2,2,-2,2,7,-8,-7,10,-7,2,-10,2,3,4],[10,7,-6,7,1,-4,9,5,-8,5,-1,-7,-6,-5],[-8,8,-9,-2,-6,-3,-6,-5,10,10,-6,-5,-4,10],[-1,8,5,7,-2,7,8,5,8,1,-2,7,-10,7],[-5,3,-3,7,-6,2,-5,-8,-2,9,2,7,4,2]],[[-6,-5,9,1,8,1,-4,6,5,-4,-4,4,-4,-8],[5,-10,2,-6,-5,2,-4,-9,-8,-10,6,8,7,-6],[5,7,5,-2,3,7,-4,-1,-3,-7,-5,4,10,-3],[-5,6,-2,-9,8,-5,9,1,2,2,-4,8,5,-3],[3,-2,7,-8,10,-8,-9,1,5,-1,-6,2,-3,3],[2,5,-4,-6,4,9,-3,2,8,-10,-9,-9,6,-7],[4,7,6,3,-8,10,-5,5,4,10,5,6,-2,7],[10,7,3,-10,-7,-8,2,-6,-7,-2,10,-4,3,9],[8,-3,1,2,5,3,-5,-6,1,3,-7,-8,7,4]],[[-5,-7,-8,-3,2,2,-1,1,10,-2,-1,6,10,-7],[-9,8,1,-8,6,9,-9,7,-8,6,8,-6,3,-9],[9,1,-4,-1,-4,5,2,-10,-6,3,-7,-1,-6,-4],[-2,-3,8,8,-3,-8,-10,7,-8,5,3,-8,-6,3],[-8,5,1,-1,-4,-2,10,5,6,5,8,10,7,-2],[-8,7,6,-8,-1,-8,9,-3,-4,10,10,-6,5,-10],[5,-7,8,9,-7,-1,-5,3,-10,3,-3,-4,10,1],[-5,10,-4,-2,-3,6,-7,8,9,6,-8,-3,-5,3],[-4,-3,-7,8,-9,4,3,-2,1,2,1,-9,-10,9]]], dtype = "int16")#candidate|6462|(15, 9, 14)|const|int16
bop_6463 = relay.bitwise_and(var_6461.astype('int16'), relay.reshape(const_6462.astype('int16'), relay.shape_of(var_6461))) # shape=(15, 9, 14)
var_6469 = relay.var("var_6469", dtype = "int16", shape = (15, 9, 14))#candidate|6469|(15, 9, 14)|var|int16
bop_6470 = relay.equal(var_6461.astype('bool'), relay.reshape(var_6469.astype('bool'), relay.shape_of(var_6461))) # shape=(15, 9, 14)
func_6307_call = mod.get_global_var('func_6307')
func_6310_call = mutated_mod.get_global_var('func_6310')
const_6479 = relay.const(True, dtype = "bool")#candidate|6479|()|const|bool
call_6478 = relay.TupleGetItem(func_6307_call(relay.reshape(const_6479.astype('bool'), [])), 0)
call_6480 = relay.TupleGetItem(func_6310_call(relay.reshape(const_6479.astype('bool'), [])), 0)
output = relay.Tuple([bop_6463,bop_6470,call_6478,const_6479,])
output2 = relay.Tuple([bop_6463,bop_6470,call_6480,const_6479,])
func_6485 = relay.Function([var_6461,var_6469,], output)
mod['func_6485'] = func_6485
mod = relay.transform.InferType()(mod)
var_6486 = relay.var("var_6486", dtype = "int16", shape = (15, 9, 14))#candidate|6486|(15, 9, 14)|var|int16
var_6487 = relay.var("var_6487", dtype = "int16", shape = (15, 9, 14))#candidate|6487|(15, 9, 14)|var|int16
output = func_6485(var_6486,var_6487,)
func_6488 = relay.Function([var_6486,var_6487,], output)
mutated_mod['func_6488'] = func_6488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5429_call = mod.get_global_var('func_5429')
func_5431_call = mutated_mod.get_global_var('func_5431')
call_6495 = func_5429_call()
call_6496 = func_5429_call()
func_5123_call = mod.get_global_var('func_5123')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_6499 = func_5123_call()
call_6500 = func_5123_call()
func_4963_call = mod.get_global_var('func_4963')
func_4964_call = mutated_mod.get_global_var('func_4964')
call_6510 = relay.TupleGetItem(func_4963_call(), 0)
call_6511 = relay.TupleGetItem(func_4964_call(), 0)
output = relay.Tuple([call_6495,call_6499,call_6510,])
output2 = relay.Tuple([call_6496,call_6500,call_6511,])
func_6512 = relay.Function([], output)
mod['func_6512'] = func_6512
mod = relay.transform.InferType()(mod)
mutated_mod['func_6512'] = func_6512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6512_call = mutated_mod.get_global_var('func_6512')
call_6513 = func_6512_call()
output = call_6513
func_6514 = relay.Function([], output)
mutated_mod['func_6514'] = func_6514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6264_call = mod.get_global_var('func_6264')
func_6265_call = mutated_mod.get_global_var('func_6265')
call_6631 = relay.TupleGetItem(func_6264_call(), 1)
call_6632 = relay.TupleGetItem(func_6265_call(), 1)
func_3908_call = mod.get_global_var('func_3908')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_6637 = func_3908_call()
call_6638 = func_3908_call()
output = relay.Tuple([call_6631,call_6637,])
output2 = relay.Tuple([call_6632,call_6638,])
func_6644 = relay.Function([], output)
mod['func_6644'] = func_6644
mod = relay.transform.InferType()(mod)
output = func_6644()
func_6645 = relay.Function([], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6671 = relay.var("var_6671", dtype = "bool", shape = (14, 3, 3))#candidate|6671|(14, 3, 3)|var|bool
var_6672 = relay.var("var_6672", dtype = "bool", shape = (14, 3, 3))#candidate|6672|(14, 3, 3)|var|bool
bop_6673 = relay.logical_and(var_6671.astype('bool'), relay.reshape(var_6672.astype('bool'), relay.shape_of(var_6671))) # shape=(14, 3, 3)
output = bop_6673
output2 = bop_6673
func_6686 = relay.Function([var_6671,var_6672,], output)
mod['func_6686'] = func_6686
mod = relay.transform.InferType()(mod)
mutated_mod['func_6686'] = func_6686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6686_call = mutated_mod.get_global_var('func_6686')
var_6688 = relay.var("var_6688", dtype = "bool", shape = (14, 3, 3))#candidate|6688|(14, 3, 3)|var|bool
var_6689 = relay.var("var_6689", dtype = "bool", shape = (14, 3, 3))#candidate|6689|(14, 3, 3)|var|bool
call_6687 = func_6686_call(var_6688,var_6689,)
output = call_6687
func_6690 = relay.Function([var_6688,var_6689,], output)
mutated_mod['func_6690'] = func_6690
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6717 = relay.var("var_6717", dtype = "float64", shape = (10, 15, 6))#candidate|6717|(10, 15, 6)|var|float64
uop_6718 = relay.log(var_6717.astype('float64')) # shape=(10, 15, 6)
bop_6755 = relay.floor_divide(uop_6718.astype('float64'), relay.reshape(var_6717.astype('float64'), relay.shape_of(uop_6718))) # shape=(10, 15, 6)
output = bop_6755
output2 = bop_6755
func_6764 = relay.Function([var_6717,], output)
mod['func_6764'] = func_6764
mod = relay.transform.InferType()(mod)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6765 = relay.var("var_6765", dtype = "float64", shape = (10, 15, 6))#candidate|6765|(10, 15, 6)|var|float64
func_6764_call = mutated_mod.get_global_var('func_6764')
call_6766 = func_6764_call(var_6765)
output = call_6766
func_6767 = relay.Function([var_6765], output)
mutated_mod['func_6767'] = func_6767
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2949_call = mod.get_global_var('func_2949')
func_2950_call = mutated_mod.get_global_var('func_2950')
call_6775 = func_2949_call()
call_6776 = func_2949_call()
output = relay.Tuple([call_6775,])
output2 = relay.Tuple([call_6776,])
func_6782 = relay.Function([], output)
mod['func_6782'] = func_6782
mod = relay.transform.InferType()(mod)
output = func_6782()
func_6783 = relay.Function([], output)
mutated_mod['func_6783'] = func_6783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5153_call = mod.get_global_var('func_5153')
func_5155_call = mutated_mod.get_global_var('func_5155')
call_6784 = func_5153_call()
call_6785 = func_5153_call()
output = call_6784
output2 = call_6785
func_6792 = relay.Function([], output)
mod['func_6792'] = func_6792
mod = relay.transform.InferType()(mod)
mutated_mod['func_6792'] = func_6792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6792_call = mutated_mod.get_global_var('func_6792')
call_6793 = func_6792_call()
output = call_6793
func_6794 = relay.Function([], output)
mutated_mod['func_6794'] = func_6794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6456_call = mod.get_global_var('func_6456')
func_6457_call = mutated_mod.get_global_var('func_6457')
call_6865 = relay.TupleGetItem(func_6456_call(), 2)
call_6866 = relay.TupleGetItem(func_6457_call(), 2)
uop_6871 = relay.acosh(call_6865.astype('float32')) # shape=(3, 2, 12)
uop_6873 = relay.acosh(call_6866.astype('float32')) # shape=(3, 2, 12)
func_3611_call = mod.get_global_var('func_3611')
func_3614_call = mutated_mod.get_global_var('func_3614')
var_6880 = relay.var("var_6880", dtype = "uint32", shape = (7, 56))#candidate|6880|(7, 56)|var|uint32
call_6879 = relay.TupleGetItem(func_3611_call(relay.reshape(var_6880.astype('uint32'), [4, 7, 14]), relay.reshape(var_6880.astype('uint32'), [4, 7, 14]), ), 1)
call_6881 = relay.TupleGetItem(func_3614_call(relay.reshape(var_6880.astype('uint32'), [4, 7, 14]), relay.reshape(var_6880.astype('uint32'), [4, 7, 14]), ), 1)
func_1315_call = mod.get_global_var('func_1315')
func_1320_call = mutated_mod.get_global_var('func_1320')
const_6884 = relay.const([[-1,-6,-2,-4,-3,-3,10,-2,2,10,-4,10,-1,-7,-3,8,6,10,10,-10,-5,-1,2,8,9,-7,4,10,-8,-2,4,4,-3,-9,-10,-6,-3,-2,2,8,-7,-4,-4,-6,-1,-5,8,8,-6,4,5,3,-9,-4,2,-10],[-9,-1,3,5,-6,1,-2,5,6,-5,1,1,-2,1,-9,4,9,10,3,-6,-8,2,5,-5,1,4,-8,4,-1,4,7,-7,3,8,5,-4,-10,10,-6,-6,6,8,6,4,8,7,-7,-2,4,-4,-2,1,-5,-7,7,-7],[-5,9,-9,-9,4,-2,2,1,4,4,-4,-9,-7,1,2,-9,4,-6,-4,10,3,-6,6,1,-3,-5,2,-7,10,3,5,-9,-1,-10,2,-10,1,-9,5,4,-7,-6,-5,-5,10,-7,9,4,2,4,3,8,2,-1,-9,5]], dtype = "int64")#candidate|6884|(3, 56)|const|int64
var_6885 = relay.var("var_6885", dtype = "float32", shape = (640,))#candidate|6885|(640,)|var|float32
call_6883 = relay.TupleGetItem(func_1315_call(relay.reshape(const_6884.astype('int64'), [7, 12, 2]), relay.reshape(const_6884.astype('int64'), [7, 12, 2]), relay.reshape(var_6885.astype('float32'), [640,]), ), 5)
call_6886 = relay.TupleGetItem(func_1320_call(relay.reshape(const_6884.astype('int64'), [7, 12, 2]), relay.reshape(const_6884.astype('int64'), [7, 12, 2]), relay.reshape(var_6885.astype('float32'), [640,]), ), 5)
output = relay.Tuple([uop_6871,call_6879,var_6880,call_6883,const_6884,var_6885,])
output2 = relay.Tuple([uop_6873,call_6881,var_6880,call_6886,const_6884,var_6885,])
func_6887 = relay.Function([var_6880,var_6885,], output)
mod['func_6887'] = func_6887
mod = relay.transform.InferType()(mod)
var_6888 = relay.var("var_6888", dtype = "uint32", shape = (7, 56))#candidate|6888|(7, 56)|var|uint32
var_6889 = relay.var("var_6889", dtype = "float32", shape = (640,))#candidate|6889|(640,)|var|float32
output = func_6887(var_6888,var_6889,)
func_6890 = relay.Function([var_6888,var_6889,], output)
mutated_mod['func_6890'] = func_6890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2975_call = mod.get_global_var('func_2975')
func_2977_call = mutated_mod.get_global_var('func_2977')
call_6914 = relay.TupleGetItem(func_2975_call(), 0)
call_6915 = relay.TupleGetItem(func_2977_call(), 0)
output = call_6914
output2 = call_6915
func_6922 = relay.Function([], output)
mod['func_6922'] = func_6922
mod = relay.transform.InferType()(mod)
mutated_mod['func_6922'] = func_6922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mutated_mod.get_global_var('func_6922')
call_6923 = func_6922_call()
output = call_6923
func_6924 = relay.Function([], output)
mutated_mod['func_6924'] = func_6924
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3968_call = mod.get_global_var('func_3968')
func_3969_call = mutated_mod.get_global_var('func_3969')
call_6937 = relay.TupleGetItem(func_3968_call(), 0)
call_6938 = relay.TupleGetItem(func_3969_call(), 0)
func_4496_call = mod.get_global_var('func_4496')
func_4498_call = mutated_mod.get_global_var('func_4498')
call_6943 = func_4496_call()
call_6944 = func_4496_call()
output = relay.Tuple([call_6937,call_6943,])
output2 = relay.Tuple([call_6938,call_6944,])
func_6955 = relay.Function([], output)
mod['func_6955'] = func_6955
mod = relay.transform.InferType()(mod)
mutated_mod['func_6955'] = func_6955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6955_call = mutated_mod.get_global_var('func_6955')
call_6956 = func_6955_call()
output = call_6956
func_6957 = relay.Function([], output)
mutated_mod['func_6957'] = func_6957
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5123_call = mod.get_global_var('func_5123')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_6986 = func_5123_call()
call_6987 = func_5123_call()
func_5479_call = mod.get_global_var('func_5479')
func_5480_call = mutated_mod.get_global_var('func_5480')
call_7008 = func_5479_call()
call_7009 = func_5479_call()
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_7034 = relay.TupleGetItem(func_5035_call(), 1)
call_7035 = relay.TupleGetItem(func_5036_call(), 1)
output = relay.Tuple([call_6986,call_7008,call_7034,])
output2 = relay.Tuple([call_6987,call_7009,call_7035,])
func_7040 = relay.Function([], output)
mod['func_7040'] = func_7040
mod = relay.transform.InferType()(mod)
output = func_7040()
func_7041 = relay.Function([], output)
mutated_mod['func_7041'] = func_7041
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3908_call = mod.get_global_var('func_3908')
func_3909_call = mutated_mod.get_global_var('func_3909')
call_7045 = func_3908_call()
call_7046 = func_3908_call()
output = relay.Tuple([call_7045,])
output2 = relay.Tuple([call_7046,])
func_7063 = relay.Function([], output)
mod['func_7063'] = func_7063
mod = relay.transform.InferType()(mod)
output = func_7063()
func_7064 = relay.Function([], output)
mutated_mod['func_7064'] = func_7064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6922_call = mod.get_global_var('func_6922')
func_6924_call = mutated_mod.get_global_var('func_6924')
call_7079 = func_6922_call()
call_7080 = func_6922_call()
output = call_7079
output2 = call_7080
func_7085 = relay.Function([], output)
mod['func_7085'] = func_7085
mod = relay.transform.InferType()(mod)
output = func_7085()
func_7086 = relay.Function([], output)
mutated_mod['func_7086'] = func_7086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7040_call = mod.get_global_var('func_7040')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_7107 = relay.TupleGetItem(func_7040_call(), 0)
call_7108 = relay.TupleGetItem(func_7041_call(), 0)
output = relay.Tuple([call_7107,])
output2 = relay.Tuple([call_7108,])
func_7113 = relay.Function([], output)
mod['func_7113'] = func_7113
mod = relay.transform.InferType()(mod)
mutated_mod['func_7113'] = func_7113
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7113_call = mutated_mod.get_global_var('func_7113')
call_7114 = func_7113_call()
output = call_7114
func_7115 = relay.Function([], output)
mutated_mod['func_7115'] = func_7115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_7126 = relay.TupleGetItem(func_2912_call(), 2)
call_7127 = relay.TupleGetItem(func_2913_call(), 2)
func_5955_call = mod.get_global_var('func_5955')
func_5956_call = mutated_mod.get_global_var('func_5956')
call_7145 = relay.TupleGetItem(func_5955_call(), 1)
call_7146 = relay.TupleGetItem(func_5956_call(), 1)
bop_7166 = relay.less_equal(call_7145.astype('bool'), call_7126.astype('bool')) # shape=(15, 1, 3)
bop_7169 = relay.less_equal(call_7146.astype('bool'), call_7127.astype('bool')) # shape=(15, 1, 3)
func_4753_call = mod.get_global_var('func_4753')
func_4754_call = mutated_mod.get_global_var('func_4754')
call_7189 = func_4753_call()
call_7190 = func_4753_call()
bop_7230 = relay.add(call_7145.astype('float32'), relay.reshape(bop_7166.astype('float32'), relay.shape_of(call_7145))) # shape=(15, 1, 3)
bop_7233 = relay.add(call_7146.astype('float32'), relay.reshape(bop_7169.astype('float32'), relay.shape_of(call_7146))) # shape=(15, 1, 3)
bop_7244 = relay.logical_or(bop_7166.astype('bool'), relay.reshape(call_7145.astype('bool'), relay.shape_of(bop_7166))) # shape=(15, 1, 3)
bop_7247 = relay.logical_or(bop_7169.astype('bool'), relay.reshape(call_7146.astype('bool'), relay.shape_of(bop_7169))) # shape=(15, 1, 3)
func_3894_call = mod.get_global_var('func_3894')
func_3897_call = mutated_mod.get_global_var('func_3897')
var_7251 = relay.var("var_7251", dtype = "uint32", shape = (392,))#candidate|7251|(392,)|var|uint32
call_7250 = relay.TupleGetItem(func_3894_call(relay.reshape(var_7251.astype('uint32'), [392,])), 0)
call_7252 = relay.TupleGetItem(func_3897_call(relay.reshape(var_7251.astype('uint32'), [392,])), 0)
func_2735_call = mod.get_global_var('func_2735')
func_2739_call = mutated_mod.get_global_var('func_2739')
call_7269 = relay.TupleGetItem(func_2735_call(relay.reshape(call_7126.astype('float32'), []), relay.reshape(call_7189.astype('float32'), [11, 11, 7]), ), 0)
call_7270 = relay.TupleGetItem(func_2739_call(relay.reshape(call_7126.astype('float32'), []), relay.reshape(call_7189.astype('float32'), [11, 11, 7]), ), 0)
func_2912_call = mod.get_global_var('func_2912')
func_2913_call = mutated_mod.get_global_var('func_2913')
call_7290 = relay.TupleGetItem(func_2912_call(), 0)
call_7291 = relay.TupleGetItem(func_2913_call(), 0)
func_6402_call = mod.get_global_var('func_6402')
func_6403_call = mutated_mod.get_global_var('func_6403')
call_7297 = func_6402_call()
call_7298 = func_6402_call()
output = relay.Tuple([call_7189,bop_7230,bop_7244,call_7250,var_7251,call_7269,call_7290,call_7297,])
output2 = relay.Tuple([call_7190,bop_7233,bop_7247,call_7252,var_7251,call_7270,call_7291,call_7298,])
func_7304 = relay.Function([var_7251,], output)
mod['func_7304'] = func_7304
mod = relay.transform.InferType()(mod)
var_7305 = relay.var("var_7305", dtype = "uint32", shape = (392,))#candidate|7305|(392,)|var|uint32
output = func_7304(var_7305)
func_7306 = relay.Function([var_7305], output)
mutated_mod['func_7306'] = func_7306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1893_call = mod.get_global_var('func_1893')
func_1895_call = mutated_mod.get_global_var('func_1895')
call_7373 = func_1893_call()
call_7374 = func_1893_call()
output = relay.Tuple([call_7373,])
output2 = relay.Tuple([call_7374,])
func_7378 = relay.Function([], output)
mod['func_7378'] = func_7378
mod = relay.transform.InferType()(mod)
output = func_7378()
func_7379 = relay.Function([], output)
mutated_mod['func_7379'] = func_7379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6067_call = mod.get_global_var('func_6067')
func_6068_call = mutated_mod.get_global_var('func_6068')
call_7380 = relay.TupleGetItem(func_6067_call(), 0)
call_7381 = relay.TupleGetItem(func_6068_call(), 0)
output = call_7380
output2 = call_7381
func_7384 = relay.Function([], output)
mod['func_7384'] = func_7384
mod = relay.transform.InferType()(mod)
output = func_7384()
func_7385 = relay.Function([], output)
mutated_mod['func_7385'] = func_7385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7063_call = mod.get_global_var('func_7063')
func_7064_call = mutated_mod.get_global_var('func_7064')
call_7468 = relay.TupleGetItem(func_7063_call(), 0)
call_7469 = relay.TupleGetItem(func_7064_call(), 0)
func_5955_call = mod.get_global_var('func_5955')
func_5956_call = mutated_mod.get_global_var('func_5956')
call_7470 = relay.TupleGetItem(func_5955_call(), 1)
call_7471 = relay.TupleGetItem(func_5956_call(), 1)
output = relay.Tuple([call_7468,call_7470,])
output2 = relay.Tuple([call_7469,call_7471,])
func_7485 = relay.Function([], output)
mod['func_7485'] = func_7485
mod = relay.transform.InferType()(mod)
output = func_7485()
func_7486 = relay.Function([], output)
mutated_mod['func_7486'] = func_7486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6792_call = mod.get_global_var('func_6792')
func_6794_call = mutated_mod.get_global_var('func_6794')
call_7507 = func_6792_call()
call_7508 = func_6792_call()
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_7523 = relay.TupleGetItem(func_2183_call(), 4)
call_7524 = relay.TupleGetItem(func_2185_call(), 4)
output = relay.Tuple([call_7507,call_7523,])
output2 = relay.Tuple([call_7508,call_7524,])
func_7525 = relay.Function([], output)
mod['func_7525'] = func_7525
mod = relay.transform.InferType()(mod)
mutated_mod['func_7525'] = func_7525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7525_call = mutated_mod.get_global_var('func_7525')
call_7526 = func_7525_call()
output = call_7526
func_7527 = relay.Function([], output)
mutated_mod['func_7527'] = func_7527
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7528 = relay.var("var_7528", dtype = "int8", shape = (9, 5, 14))#candidate|7528|(9, 5, 14)|var|int8
var_7529 = relay.var("var_7529", dtype = "int8", shape = (9, 5, 14))#candidate|7529|(9, 5, 14)|var|int8
bop_7530 = relay.bitwise_or(var_7528.astype('int8'), relay.reshape(var_7529.astype('int8'), relay.shape_of(var_7528))) # shape=(9, 5, 14)
output = relay.Tuple([bop_7530,])
output2 = relay.Tuple([bop_7530,])
func_7534 = relay.Function([var_7528,var_7529,], output)
mod['func_7534'] = func_7534
mod = relay.transform.InferType()(mod)
mutated_mod['func_7534'] = func_7534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7534_call = mutated_mod.get_global_var('func_7534')
var_7536 = relay.var("var_7536", dtype = "int8", shape = (9, 5, 14))#candidate|7536|(9, 5, 14)|var|int8
var_7537 = relay.var("var_7537", dtype = "int8", shape = (9, 5, 14))#candidate|7537|(9, 5, 14)|var|int8
call_7535 = func_7534_call(var_7536,var_7537,)
output = call_7535
func_7538 = relay.Function([var_7536,var_7537,], output)
mutated_mod['func_7538'] = func_7538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5502_call = mod.get_global_var('func_5502')
func_5504_call = mutated_mod.get_global_var('func_5504')
call_7546 = func_5502_call()
call_7547 = func_5502_call()
output = relay.Tuple([call_7546,])
output2 = relay.Tuple([call_7547,])
func_7558 = relay.Function([], output)
mod['func_7558'] = func_7558
mod = relay.transform.InferType()(mod)
output = func_7558()
func_7559 = relay.Function([], output)
mutated_mod['func_7559'] = func_7559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_7635 = relay.TupleGetItem(func_5035_call(), 1)
call_7636 = relay.TupleGetItem(func_5036_call(), 1)
output = call_7635
output2 = call_7636
func_7647 = relay.Function([], output)
mod['func_7647'] = func_7647
mod = relay.transform.InferType()(mod)
output = func_7647()
func_7648 = relay.Function([], output)
mutated_mod['func_7648'] = func_7648
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7485_call = mod.get_global_var('func_7485')
func_7486_call = mutated_mod.get_global_var('func_7486')
call_7654 = relay.TupleGetItem(func_7485_call(), 1)
call_7655 = relay.TupleGetItem(func_7486_call(), 1)
output = relay.Tuple([call_7654,])
output2 = relay.Tuple([call_7655,])
func_7682 = relay.Function([], output)
mod['func_7682'] = func_7682
mod = relay.transform.InferType()(mod)
output = func_7682()
func_7683 = relay.Function([], output)
mutated_mod['func_7683'] = func_7683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6264_call = mod.get_global_var('func_6264')
func_6265_call = mutated_mod.get_global_var('func_6265')
call_7686 = relay.TupleGetItem(func_6264_call(), 1)
call_7687 = relay.TupleGetItem(func_6265_call(), 1)
output = relay.Tuple([call_7686,])
output2 = relay.Tuple([call_7687,])
func_7698 = relay.Function([], output)
mod['func_7698'] = func_7698
mod = relay.transform.InferType()(mod)
mutated_mod['func_7698'] = func_7698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7698_call = mutated_mod.get_global_var('func_7698')
call_7699 = func_7698_call()
output = call_7699
func_7700 = relay.Function([], output)
mutated_mod['func_7700'] = func_7700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6067_call = mod.get_global_var('func_6067')
func_6068_call = mutated_mod.get_global_var('func_6068')
call_7782 = relay.TupleGetItem(func_6067_call(), 0)
call_7783 = relay.TupleGetItem(func_6068_call(), 0)
output = call_7782
output2 = call_7783
func_7790 = relay.Function([], output)
mod['func_7790'] = func_7790
mod = relay.transform.InferType()(mod)
output = func_7790()
func_7791 = relay.Function([], output)
mutated_mod['func_7791'] = func_7791
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_7803 = relay.TupleGetItem(func_4398_call(), 2)
call_7804 = relay.TupleGetItem(func_4399_call(), 2)
output = relay.Tuple([call_7803,])
output2 = relay.Tuple([call_7804,])
func_7837 = relay.Function([], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
output = func_7837()
func_7838 = relay.Function([], output)
mutated_mod['func_7838'] = func_7838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7063_call = mod.get_global_var('func_7063')
func_7064_call = mutated_mod.get_global_var('func_7064')
call_7861 = relay.TupleGetItem(func_7063_call(), 0)
call_7862 = relay.TupleGetItem(func_7064_call(), 0)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
const_7881 = relay.const([-3,8,10,-8,-8,8,8,7,2,6,10,-10,-5,-6,-10,-10,5,4,5,-10,5,-10,-7,-10,-3,-5,-2,-10,10,2,1,5,-1,1,1,8,1,-2,4,-1,10,-2,1,-9,-9,2,-4,-6,-8,-10,8,6,5,2,-7,8,9,10,-3,-10,2,2,1,-1,-5,-7,-1,6,8,-5,9,4,5,-9,-5,-1,-10,-2,-1,9,6,-2,-6,2,6,-9,-5,4,-9,8,-1,10,2,-4,9,-2,9,3,-2,-9,4,-5,3,9,-10,5,-6,5,-8,-2,2,1,9,7,9,-2,-4,-2,-4,-8,-9,-8,-5,-4,1,10,-1,-5,5,2,5,-8,10,-5,-2,1,-3,6,-9,3,-6,3,3,6,9,-1,3,-3,-9,7,1,-3,-6,-4,-7,7,9,-1,-10,-8,6,-3,-1,3,-5,3,10,-2,-5,3,3,-7,2,5,-6,10,4,-2,8,-7,8,10,-6,-6,9,4,9,-6,-9,2,-6,7,6,7,7,-8,3,-4,-10,-9,2,-5,-5,4,4,1,-8,3,10,-9,-3,-3,-5,-5,-7,-8,-6,-10,3,-6,9,8,6,3,-1,-4,-9,1,1,-3,-10,9,-1,8,-2,1,-4,3,10,7,-10,6,-5,5,4,-6,8,-10,-4,-3,7,-2,-4,-10,-2,-8,5,4,-2,7,9,-10,-9,-4,-3,3,-2,8,9,2,4,-4,5,-10,-8,-3,-10,-2,3,6,-4,5,-4,-1,8,6,5,-2,9,7,7,-4,1,8,3,-2,-10,4,10,9,-1,2,7,6,4,-3,1,7,-5,-10,8,-7,10,4,-7,8,10,-3,3,-2,1,7,-5,6,3,8,9,-2,7,9], dtype = "uint32")#candidate|7881|(330,)|const|uint32
call_7880 = func_839_call(relay.reshape(const_7881.astype('uint32'), [2, 15, 11]))
call_7882 = func_839_call(relay.reshape(const_7881.astype('uint32'), [2, 15, 11]))
output = relay.Tuple([call_7861,call_7880,const_7881,])
output2 = relay.Tuple([call_7862,call_7882,const_7881,])
func_7896 = relay.Function([], output)
mod['func_7896'] = func_7896
mod = relay.transform.InferType()(mod)
mutated_mod['func_7896'] = func_7896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7896_call = mutated_mod.get_global_var('func_7896')
call_7897 = func_7896_call()
output = call_7897
func_7898 = relay.Function([], output)
mutated_mod['func_7898'] = func_7898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5035_call = mod.get_global_var('func_5035')
func_5036_call = mutated_mod.get_global_var('func_5036')
call_7959 = relay.TupleGetItem(func_5035_call(), 0)
call_7960 = relay.TupleGetItem(func_5036_call(), 0)
func_3833_call = mod.get_global_var('func_3833')
func_3836_call = mutated_mod.get_global_var('func_3836')
const_7974 = relay.const([-9,-8,-2,-10,-10,-10,-2,7,1,-8,2,-3,-6,-5,7,2,8,2,-4,-1,-3,1,1,9,5,-3,3,-5,4,1,-1,-9,2,1,4,-10,-2,-4,10,9,1,2,7,2,-7,-5,5,-7,7,-4,-9,-10,7,8,-7,3,-6,-1,-2,8,-5,8,-9,10,-3,5,-9,5,-8,3,7,-5,-1,-9,1,-2,10,-10,-7,5,3,1,6,9,-8,-1,-10,-9,-5,6,6,4,-2,-7,5,8,-1,-1,7,-10,4,-2,-10,-5,-1,-2,-1,-3,3,1,-1,7,9,8,9,3,-1,-8,-5,-7,6,-3,8,-9,7,2,-8,-7,-8,-3,5,10,10,-7,1,-3,-3,-3,4,5,-1,-7,-3,-5,1,8,5,-2,-8,-4,-2,7,5,8,3,1,10,4,-4,6,9,3,-4,3,-3,2,-5,-3,-10,-10,-6,-8,8,-10,2,-10,-2,9,8,-9,-8,-8,-1,-3,-2,5,-1,4,6,4,2,3,8,1,3,-9,-2,-3,-10,5,9,-9,6,4,7,-1,1,-4,-5,7,4,10,6,10,-2,-7,-6,3,-10,-5,-4,-10,2,6,-7,-7,2,7,-1,-4,-2,3,-7,-2,-5,6,5,6,7,5,8,7,9,8,2,2,2,4,4,-6,4,8,-7,-5,6,-2,-3,-4,4,-2,-3,10,2,3,-1,4,-3,5,7,-8,-3,7,9,8,-3,-10,9,-2,-8,-6,5,6,-2,-8,2,-2,-6,9,-10,9,-1,10,2,10,8,-1,-8,9,-8,1,-2,-3,1,4,-2,7,-5,-3,8,9,1,-8,-4,9,5,2,-2,-8,8,6,-8,-3,-9,-9,2,-4,-7,2,-9,-5], dtype = "uint32")#candidate|7974|(330,)|const|uint32
var_7975 = relay.var("var_7975", dtype = "uint32", shape = (392,))#candidate|7975|(392,)|var|uint32
call_7973 = relay.TupleGetItem(func_3833_call(relay.reshape(const_7974.astype('uint32'), [330, 1]), relay.reshape(var_7975.astype('uint32'), [392,]), ), 9)
call_7976 = relay.TupleGetItem(func_3836_call(relay.reshape(const_7974.astype('uint32'), [330, 1]), relay.reshape(var_7975.astype('uint32'), [392,]), ), 9)
output = relay.Tuple([call_7959,call_7973,const_7974,var_7975,])
output2 = relay.Tuple([call_7960,call_7976,const_7974,var_7975,])
func_7978 = relay.Function([var_7975,], output)
mod['func_7978'] = func_7978
mod = relay.transform.InferType()(mod)
var_7979 = relay.var("var_7979", dtype = "uint32", shape = (392,))#candidate|7979|(392,)|var|uint32
output = func_7978(var_7979)
func_7980 = relay.Function([var_7979], output)
mutated_mod['func_7980'] = func_7980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4496_call = mod.get_global_var('func_4496')
func_4498_call = mutated_mod.get_global_var('func_4498')
call_8013 = func_4496_call()
call_8014 = func_4496_call()
output = call_8013
output2 = call_8014
func_8038 = relay.Function([], output)
mod['func_8038'] = func_8038
mod = relay.transform.InferType()(mod)
mutated_mod['func_8038'] = func_8038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8038_call = mutated_mod.get_global_var('func_8038')
call_8039 = func_8038_call()
output = call_8039
func_8040 = relay.Function([], output)
mutated_mod['func_8040'] = func_8040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2183_call = mod.get_global_var('func_2183')
func_2185_call = mutated_mod.get_global_var('func_2185')
call_8057 = relay.TupleGetItem(func_2183_call(), 0)
call_8058 = relay.TupleGetItem(func_2185_call(), 0)
uop_8063 = relay.exp(call_8057.astype('float64')) # shape=(3, 2, 12)
uop_8065 = relay.exp(call_8058.astype('float64')) # shape=(3, 2, 12)
func_113_call = mod.get_global_var('func_113')
func_116_call = mutated_mod.get_global_var('func_116')
var_8076 = relay.var("var_8076", dtype = "float32", shape = (20, 32))#candidate|8076|(20, 32)|var|float32
call_8075 = func_113_call(relay.reshape(var_8076.astype('float32'), [8, 5, 16]), relay.reshape(var_8076.astype('float32'), [8, 5, 16]), )
call_8077 = func_113_call(relay.reshape(var_8076.astype('float32'), [8, 5, 16]), relay.reshape(var_8076.astype('float32'), [8, 5, 16]), )
output = relay.Tuple([uop_8063,call_8075,var_8076,])
output2 = relay.Tuple([uop_8065,call_8077,var_8076,])
func_8078 = relay.Function([var_8076,], output)
mod['func_8078'] = func_8078
mod = relay.transform.InferType()(mod)
var_8079 = relay.var("var_8079", dtype = "float32", shape = (20, 32))#candidate|8079|(20, 32)|var|float32
output = func_8078(var_8079)
func_8080 = relay.Function([var_8079], output)
mutated_mod['func_8080'] = func_8080
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8155 = relay.var("var_8155", dtype = "uint16", shape = ())#candidate|8155|()|var|uint16
var_8156 = relay.var("var_8156", dtype = "uint16", shape = (11, 9, 16))#candidate|8156|(11, 9, 16)|var|uint16
bop_8157 = relay.greater_equal(var_8155.astype('bool'), var_8156.astype('bool')) # shape=(11, 9, 16)
func_4871_call = mod.get_global_var('func_4871')
func_4872_call = mutated_mod.get_global_var('func_4872')
call_8174 = relay.TupleGetItem(func_4871_call(), 2)
call_8175 = relay.TupleGetItem(func_4872_call(), 2)
func_2358_call = mod.get_global_var('func_2358')
func_2360_call = mutated_mod.get_global_var('func_2360')
const_8188 = relay.const([[-8.983993],[9.919029],[3.856880],[6.158768],[6.069107],[-6.913314],[9.774077],[1.079081],[-7.065118],[1.668595],[-1.298232],[8.451880],[-3.069414],[0.802048],[-5.973416],[-4.302374],[-6.824811],[-6.064989],[4.486953],[-7.231100],[9.610713],[-2.220892],[-7.738902],[-0.048364],[-1.424296],[6.265243],[-1.218173],[6.799507],[-5.811209],[7.384779],[-2.504522],[4.734116],[5.941978],[-0.359611],[9.151092],[0.445398],[-8.442214],[9.710242],[6.205126],[7.550377],[-9.037246],[-6.079264],[-6.075641],[9.508813],[-8.036173],[2.221415],[-6.845893],[0.822276],[-4.758008],[-0.218673],[-5.145232],[-6.790678],[-2.942100],[6.316280],[5.421299],[8.066259],[4.975918],[-8.744424],[9.890334],[-3.513197],[-4.703490],[-0.060723],[8.442753],[-7.121245],[-0.817842],[7.468344],[-3.084667],[4.243759],[-7.859209],[-1.192917],[1.217400],[2.966494],[5.977423],[-2.205158],[6.100567],[-6.562894],[-5.599168],[-1.565447],[-4.155116],[-5.490891],[6.451867],[4.036115],[9.788393],[-7.313304],[1.640028],[-5.676004],[-8.252320],[-4.169954],[4.003831],[-1.757813],[9.189507],[6.973942],[-7.213588],[3.885522],[-0.814354],[1.911983],[-4.105778],[-7.579503],[2.214582],[5.721435],[4.513276],[1.117819],[9.161346],[-3.399505],[0.967465],[6.676045],[9.289509],[-2.417672],[-6.353501],[5.083135],[3.957449],[-3.933411],[9.450271],[-8.130419],[-6.274607],[-6.325694],[4.878550],[9.314467],[3.714396],[7.859115],[2.960836],[0.148799],[1.507771],[-2.596463],[-6.183333],[7.461827],[-6.166670],[8.072961],[-5.697283],[-5.000891],[0.870139],[-2.174847],[-0.469220],[7.676428],[4.477259],[-7.354923],[2.904996],[-2.120723],[-2.206696],[-9.753529],[-0.997654],[-4.457282],[1.704288],[-5.547094],[1.487537],[-3.978618],[1.132240],[4.322985],[5.106967],[6.593488],[-7.298900],[6.263166],[-2.938135],[-8.782506],[-8.679645],[2.364161],[-5.422878],[7.410543],[9.604707],[2.115631],[-6.171808],[2.521233],[5.686928],[9.103142],[4.866124],[9.786374],[7.685845],[9.335113]], dtype = "float32")#candidate|8188|(168, 1)|const|float32
call_8187 = relay.TupleGetItem(func_2358_call(relay.reshape(const_8188.astype('float32'), [6, 4, 7])), 0)
call_8189 = relay.TupleGetItem(func_2360_call(relay.reshape(const_8188.astype('float32'), [6, 4, 7])), 0)
func_3230_call = mod.get_global_var('func_3230')
func_3231_call = mutated_mod.get_global_var('func_3231')
call_8190 = relay.TupleGetItem(func_3230_call(), 2)
call_8191 = relay.TupleGetItem(func_3231_call(), 2)
func_7485_call = mod.get_global_var('func_7485')
func_7486_call = mutated_mod.get_global_var('func_7486')
call_8214 = relay.TupleGetItem(func_7485_call(), 0)
call_8215 = relay.TupleGetItem(func_7486_call(), 0)
func_4871_call = mod.get_global_var('func_4871')
func_4872_call = mutated_mod.get_global_var('func_4872')
call_8221 = relay.TupleGetItem(func_4871_call(), 1)
call_8222 = relay.TupleGetItem(func_4872_call(), 1)
func_3359_call = mod.get_global_var('func_3359')
func_3362_call = mutated_mod.get_global_var('func_3362')
const_8248 = relay.const([1,5,-5,3,-4,8,9,1,3,6,-2,-6,-2,2,-4,-5,3,4,5,-1,-4,-6,2,-8,-1,-3,-5,-5,3,3,10,-4,-10,-10,-8,1,10,5,-7,9,9,-1,2,-1,3,2,-2,8,-3,-6,-9,-2,-6,-3,2,-3,5,-3,-1,-1,8,10,8,-3,-8,1,-6,8,-2,5,4,-2,1,7,-2,8,2,2,-8,2,-2,1,7,-9,2,-2,-1,9,-2,6,7,-3,-2,10,8,3,-6,-1,6,4,4,-6,2,9,-4,-5,-8,1,-3,-9,-4,4,-9,-6,5,-4,-8,5,10,4,-10,-6,-9,-6,9,-5,10,-4,2,-5,-2,5,-3,-1,-6,-6,6,-3,-8,-7,-8,9,-10,6,-5,-1,2,-8,-8,-8,6,1,6,6,6,-9,4,2,-3,7,9,-4,4,8,2,8,-9,-9,4,-9,7,-5,-7,8,-5,-9,-5,-7,-6,-2,-10,6,9,6,-1,2,-4,10,3,-3,-2,-5,5,5,7,-10,8,-8,-1,8,1,1,-8,7,10,-10,-4,1,-6,-1,-6,2,6,10,-6,3,-10,-3,9,2,3,4,-8,7,3,-9,-10,2,-4,-5,-3,-8,-5,3,-2,-3,-8,10,-2,-10,-6,4,1,-2,-2,-5,-7,10,-3,-6,-8,10,6,10,9,-4,10,-1,-8,5,-1,-3,-5,-10,5,-5,-5,-9,-5,10,10,8,-4,10,-1,-9,7,-1,-6,1,9,6,-9,6,5,-9,-1,-6,6,-6,3,1,1,10,-5,1,-5,7,-2,-9,10,-4,4,6,6,-7,9,-6,-10,-10,-5,10,-7,-5,1,-6,1,9,-7,-3,9,9,10,10,2,-6,8,9,2,-4,8,-3,7,-4,9,7,-1,-5,4,2,5,4,-5,-9,-9,-1,3,7,6,-6,3,2,-4,5,-2,5,-7,1,6,-9,4,-3,4,9,-3,4,8,10,-2,-1,3,2,-7,-4,-4,7,2,5,9,-5,-8,-10,6,-10,8,5,-7,3,-1,-6,-9,4,-4,9,-2,-8,7,7,-10,2,-8,1,-5,9,3,-2,10,-6,-3,-8,3,-5,5,-2,7,-5,10,-10,2,2,7,-8,7,3,-2,7,8,6,2,-2,-3,-7,5,-9,-7,2,4,-2,5,3,8,-5,-3,-2,10,-7,-1,7,10,-2,-6,4,6,2,-1,1,6,6,8,4,3,10,-6,1,10,4,10,7,-3,-9,6,6,7,-1,3,2,9,-2,-6,10,8,3,1,6,-1,-2,7,8,1,1,-7,10,3,-10,6,-7,5,4,2,-1,7,7,-3,-1,6,-10,5,8,3,6,-9,4,5,-1,-10,-7,8,-2,-10,-7,5,7,9,-7,-7,-2,8,-2,5,-9,6,1,-1,-6,8,-5,-9,4,-2,-10,7,-7,9,-9,1,-9,-3,2,5,-5,9,7,-6,8,5,-7,4,-1,-3,7,-8,4,7,7,4,-7,4,3,-9,8,-2,8,10,1,8,9,6,-1,-7,-7,2,6,-7,6,3,-10,8,1,7,-1,-1,3,4,-10,-4,-4,10,10,8,-5,-9,-5,3,7,9,-7,8,8,5,5,-3,-4,6,2,2,-6,-2,-10,-1,7,6,-10,5,8,-6,-9,-9,-3,9,-10,1,-3,-9,10,-1,9,2,-4,9,-6,5,5,-8,-1,-4,-9,-9,9,-5,-7,7,-6,7,-5,1,3,-7,-2,-5,-2,-5,3,3,-3,3,7,-8,-7,2,-3,-3,1,-5,5,-5,10,-7,-4,-6,-1,7,-7,10,1,-7,-6,-3,8,-9,9,-9,-4,3,-1,6,-8,-9,-9,-10,-4,9,7,7,1,8,2,10,-8,-7,-1,-10,-8,-3,-9,-9,10,-10,-9,4,-7,-1,-2,8,-3,-8,7,-3,-6,-2,-9,-5,-9,8,6,-10,-6,3,-10,-9,-5,7,-6,7,-9,6,-9,9,-10,8,10,-10,-6,6,3,1,4,-1,10,-4,-4,9,5,-1,-6,10,6,-4,-2,-10,-8,6,1,-4,-3,10,-3,3,6,3,-5,-1,3,-3,8], dtype = "uint64")#candidate|8248|(784,)|const|uint64
call_8247 = relay.TupleGetItem(func_3359_call(relay.reshape(const_8248.astype('uint64'), [14, 14, 4])), 0)
call_8249 = relay.TupleGetItem(func_3362_call(relay.reshape(const_8248.astype('uint64'), [14, 14, 4])), 0)
output = relay.Tuple([bop_8157,call_8174,call_8187,const_8188,call_8190,call_8214,call_8221,call_8247,const_8248,])
output2 = relay.Tuple([bop_8157,call_8175,call_8189,const_8188,call_8191,call_8215,call_8222,call_8249,const_8248,])
func_8254 = relay.Function([var_8155,var_8156,], output)
mod['func_8254'] = func_8254
mod = relay.transform.InferType()(mod)
var_8255 = relay.var("var_8255", dtype = "uint16", shape = ())#candidate|8255|()|var|uint16
var_8256 = relay.var("var_8256", dtype = "uint16", shape = (11, 9, 16))#candidate|8256|(11, 9, 16)|var|uint16
output = func_8254(var_8255,var_8256,)
func_8257 = relay.Function([var_8255,var_8256,], output)
mutated_mod['func_8257'] = func_8257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5601_call = mod.get_global_var('func_5601')
func_5603_call = mutated_mod.get_global_var('func_5603')
call_8266 = func_5601_call()
call_8267 = func_5601_call()
output = relay.Tuple([call_8266,])
output2 = relay.Tuple([call_8267,])
func_8288 = relay.Function([], output)
mod['func_8288'] = func_8288
mod = relay.transform.InferType()(mod)
mutated_mod['func_8288'] = func_8288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8288_call = mutated_mod.get_global_var('func_8288')
call_8289 = func_8288_call()
output = call_8289
func_8290 = relay.Function([], output)
mutated_mod['func_8290'] = func_8290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5123_call = mod.get_global_var('func_5123')
func_5124_call = mutated_mod.get_global_var('func_5124')
call_8320 = func_5123_call()
call_8321 = func_5123_call()
func_8038_call = mod.get_global_var('func_8038')
func_8040_call = mutated_mod.get_global_var('func_8040')
call_8348 = func_8038_call()
call_8349 = func_8038_call()
func_7896_call = mod.get_global_var('func_7896')
func_7898_call = mutated_mod.get_global_var('func_7898')
call_8354 = relay.TupleGetItem(func_7896_call(), 2)
call_8355 = relay.TupleGetItem(func_7898_call(), 2)
output = relay.Tuple([call_8320,call_8348,call_8354,])
output2 = relay.Tuple([call_8321,call_8349,call_8355,])
func_8382 = relay.Function([], output)
mod['func_8382'] = func_8382
mod = relay.transform.InferType()(mod)
output = func_8382()
func_8383 = relay.Function([], output)
mutated_mod['func_8383'] = func_8383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5008_call = mod.get_global_var('func_5008')
func_5009_call = mutated_mod.get_global_var('func_5009')
call_8386 = func_5008_call()
call_8387 = func_5008_call()
output = relay.Tuple([call_8386,])
output2 = relay.Tuple([call_8387,])
func_8394 = relay.Function([], output)
mod['func_8394'] = func_8394
mod = relay.transform.InferType()(mod)
mutated_mod['func_8394'] = func_8394
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8394_call = mutated_mod.get_global_var('func_8394')
call_8395 = func_8394_call()
output = call_8395
func_8396 = relay.Function([], output)
mutated_mod['func_8396'] = func_8396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7063_call = mod.get_global_var('func_7063')
func_7064_call = mutated_mod.get_global_var('func_7064')
call_8429 = relay.TupleGetItem(func_7063_call(), 0)
call_8430 = relay.TupleGetItem(func_7064_call(), 0)
output = relay.Tuple([call_8429,])
output2 = relay.Tuple([call_8430,])
func_8435 = relay.Function([], output)
mod['func_8435'] = func_8435
mod = relay.transform.InferType()(mod)
output = func_8435()
func_8436 = relay.Function([], output)
mutated_mod['func_8436'] = func_8436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6792_call = mod.get_global_var('func_6792')
func_6794_call = mutated_mod.get_global_var('func_6794')
call_8441 = func_6792_call()
call_8442 = func_6792_call()
output = relay.Tuple([call_8441,])
output2 = relay.Tuple([call_8442,])
func_8451 = relay.Function([], output)
mod['func_8451'] = func_8451
mod = relay.transform.InferType()(mod)
output = func_8451()
func_8452 = relay.Function([], output)
mutated_mod['func_8452'] = func_8452
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mod.get_global_var('func_7837')
func_7838_call = mutated_mod.get_global_var('func_7838')
call_8489 = relay.TupleGetItem(func_7837_call(), 0)
call_8490 = relay.TupleGetItem(func_7838_call(), 0)
output = relay.Tuple([call_8489,])
output2 = relay.Tuple([call_8490,])
func_8491 = relay.Function([], output)
mod['func_8491'] = func_8491
mod = relay.transform.InferType()(mod)
mutated_mod['func_8491'] = func_8491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8491_call = mutated_mod.get_global_var('func_8491')
call_8492 = func_8491_call()
output = call_8492
func_8493 = relay.Function([], output)
mutated_mod['func_8493'] = func_8493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7063_call = mod.get_global_var('func_7063')
func_7064_call = mutated_mod.get_global_var('func_7064')
call_8500 = relay.TupleGetItem(func_7063_call(), 0)
call_8501 = relay.TupleGetItem(func_7064_call(), 0)
func_2358_call = mod.get_global_var('func_2358')
func_2360_call = mutated_mod.get_global_var('func_2360')
call_8502 = relay.TupleGetItem(func_2358_call(relay.reshape(call_8500.astype('float32'), [6, 4, 7])), 0)
call_8503 = relay.TupleGetItem(func_2360_call(relay.reshape(call_8500.astype('float32'), [6, 4, 7])), 0)
func_6239_call = mod.get_global_var('func_6239')
func_6243_call = mutated_mod.get_global_var('func_6243')
var_8505 = relay.var("var_8505", dtype = "float32", shape = (45,))#candidate|8505|(45,)|var|float32
var_8506 = relay.var("var_8506", dtype = "uint32", shape = (330,))#candidate|8506|(330,)|var|uint32
const_8507 = relay.const([-1.580695,1.704003,3.299901,-1.701885,-7.606454,-2.120042,9.881964,3.696726,2.411234,-1.214629,-4.455707,7.512021,-0.895623,4.852929,3.433496,7.331766,-4.306570,-7.963748,2.453246,-6.929843,-9.956690,6.011881,-9.999326,-0.332320,6.363413,2.944134,-6.413885,-4.781191,-8.115089,-8.139071,8.780471,6.318853,-3.332259,3.963121,-2.045251,-5.950251,-2.134261,0.271024,-2.068321,-1.142692,-1.193461,-6.043818,-2.210195,2.357232,-1.107410,-9.883905,6.686501,-7.186517,-2.220891,5.694663,2.780292,3.065258,-3.842342,6.768988,-4.299207,-8.221062,5.943446,5.986343,-4.049647,2.946232,-4.653105,-4.836499,1.741958,-7.584505,-1.406558,7.014695,6.670422,4.506033,8.831018,-9.368343,9.798875,-0.488427,2.634329,-8.351653,-4.183020,7.153327,-4.171870,-6.372684,-5.528659,0.136667,-6.644158,-1.683994,3.712659,6.603258,-3.786986,-8.195336,3.062810,4.658345,-8.626394,-0.506013,9.834266,6.797393,2.960570,4.789137,-0.527636,-2.225976,8.972614,-4.374109,-1.622041,0.847494,-8.440483,-5.175268,-2.318911,-1.578094,-0.755820,8.884098,-2.643771,5.622408,-5.791985,6.974179,0.082564,-6.477743,9.036887,2.693121,-5.960640,-5.864314,-2.214432,-8.964607,-8.424991,2.772327,2.557357,-4.340321,2.911171,7.373613,6.503589,8.094900,-3.888344,3.986677,-8.670261,-7.529596,-9.348329,5.631750,5.338440,4.438289,6.134095,-9.589886,-1.145846,-3.502848,-8.318053,1.920236,2.535918,-0.495781,-6.568748,7.539868,-8.840565,-4.763667,-0.796301,6.917414,9.045748,-0.613028,7.558740,-9.169546,8.012856,-7.624099,-1.167848,6.994292,-9.376337,-6.953692,-2.376841,9.543238,7.418426,2.276911,-1.452713,8.699692,2.044149,-3.712115,6.518542,-9.974699,5.918260,-2.017781,8.329185,1.377621,-8.990366,-3.195824,4.966224,6.898504,0.989131,8.891643,-2.874090,-6.408766,-4.442720,-4.511024,9.536966,-2.324527,8.777413,-3.912902,6.723519,-2.355289,9.039909,-3.375930,0.047273,1.584873,-0.191344,-6.402488,-9.337537,-1.705412,5.942521,-7.903274,-1.185973,1.165987,6.145608,-9.715722,-5.754997,-9.474942,9.998161,-3.248958,8.807052,-6.200640,-1.755912,-5.664038,2.972593,0.485726,3.435461,8.190211,9.654250,-0.991924,-7.220622,3.507342,6.025742,1.609420,-9.470603,7.792784,1.230071,0.789498,-3.888067,-2.115962,-5.880484,-9.926258,7.168377,3.996670,5.297150,-2.135422,-1.956983,-9.315968,3.579100,5.567426,0.213090,4.815965,-2.808998,3.826199,-0.229409,-9.105567,4.817161,4.517586,-2.836873,7.807037,-8.994169,9.180426,1.292772,-4.818109,2.131668,-8.796017,5.502097,-0.719134,-9.081275,-5.506981,9.330641,-3.915098,-9.872362,-4.982233,-6.615052,-7.696935,6.614569,-6.470707,4.154630,1.960910,-3.538363,9.403596,-6.271257,2.309343,6.552459,2.286879,-5.132556,-3.100854,3.689740,2.130129,-4.289627,-8.296012,3.809856,2.137027,-4.911051,-7.536419,-2.323015,-8.287047,0.393366,-9.876368,5.375454,8.748655,5.591597,-4.952687,-8.126192,-6.777212,9.147202,-2.076314,4.630605,4.486312,7.496649,-7.811542,-0.357049,-4.911465,-8.482912,-4.973347,-7.716954,4.538234,8.626838,3.568411,4.573699,3.281988,-1.720453,-8.965345,1.683506,2.306450,6.442388,-9.594299,-7.716670,9.479326,8.927680,8.406335,0.987650,1.272180,-8.775717,9.203028,9.775598,3.163002,-8.628198,9.222440,9.629826,-5.783155,2.016939,-3.998767,2.481372,-3.207509,-4.641458,3.617131,4.127426,-4.999680,7.119360,0.017808,-3.774563,-9.883957,-2.510683,-7.429733,7.180439,-2.896976,-3.837336,-8.270952,-1.298440,-2.574540,-8.199850,4.252199,0.896752,-9.989931,7.559222,2.999742,-3.456926,-7.916501,3.982731,-9.193984,-7.318929,2.041461,-7.357288,-3.536911,3.656929,0.192420,-1.609305,9.337728,-9.646298,-3.157810,8.121098,-8.294443,-9.223590,8.042483,5.386999,-8.276234,-5.015719,-3.851705,9.601138,-1.722673,-6.856823,4.006593,-2.454024,-8.349437,-9.375203,-7.408260,-5.831644,2.966722,5.471947,-2.993128,-0.167339,-3.211263,1.788705,8.223035,-6.654144,4.657811,1.682515,0.017842,4.650304,5.803539,5.869236,0.036757,-4.341799,-9.286008,7.839718,-3.123335,3.503223,8.963585,-9.629521,2.437315,-2.202580,2.939825,1.297466,5.067331,-5.061620,-4.151179,-8.964404,3.648621,-1.493832,-4.872357,-2.916699,-5.272407,-2.241970,-6.050307,-0.997792,0.461913,-0.401606,6.362220,0.737877,-7.342560,0.302619,0.467211,8.767933,-9.947102,-8.013445,0.675630,9.562461,-8.150851,5.241307,-4.669002,0.980111,-7.432260,-8.281331,0.791276,-5.661522,7.821782,2.336148,2.824831,8.551917,-4.027091,6.863731,1.422753,6.123894,-7.968327,-7.074630,6.109169,-6.542801,-1.368446,3.388719,-2.152114,1.770898,0.771561,5.598271,0.245748,-7.685883,-2.957999,-3.251542,-5.122227,-1.283465,-7.831135,-5.487092,-8.135982,-8.545680,8.757690,-7.746321,8.042588,-9.515468,-4.410364,-3.415527,-1.792064,-8.708660,-3.348396,-5.129542,-3.798816,7.316247,-7.759888,-2.303406,-1.024737,5.608441,-5.996601,1.863289,6.798097,-9.576923,9.285667,-5.456965,5.664980,1.248801,7.066926,4.809533,-7.396635,-1.471345,-0.523427,2.435022,1.551333,-5.570468,-3.229553,-2.053332,5.514737,-9.175639,7.220380,2.019604,9.937406,-1.431345,-6.918654,-4.777600,-8.613781,9.718453,-9.149634,4.773073,0.028449,2.316066,3.293026,-5.065062,1.097304,-7.830014,6.978084,6.545905,-6.916781,7.516962,1.611640,3.974748,-0.848626,-3.301782,2.483330,6.950795,-4.997475,-9.850743,-2.363352,-0.786177,2.815874,-1.023031,-8.939610,5.998664,2.709909,-3.319935,6.985880,-9.965777,-1.153102,-6.255853,-3.398098,4.315468,-2.750206,-4.601940,-1.461467,-7.142589,0.251105,-7.079599,4.812008,-1.827332,-7.499648,6.254465,-0.283902,1.461259,5.899317,-8.554528,2.421172,-9.906857,-0.088666,-7.411137,5.068201,-1.652958,1.430766,7.226089,6.386304,4.289228,-5.982071,5.363329,-0.398351,0.159682,-6.393366,7.155002,0.515780,8.322136,0.255980,-9.783595,8.744326,0.642019,3.503640,1.775799,9.021454,-7.654356,7.353773,-6.977520,3.703093,4.349309,-7.700860,3.038595,-6.969525,9.132477,7.241610,2.697906,-4.787471,1.192543,8.334223,-1.092077,-4.778150,-3.850337,-0.939434,7.821891,-3.600068,2.460781,-2.479089,4.549744,-7.617550,-9.712450,-1.424541,-1.217633,-1.673168,0.597854,-0.328529,-5.871382,-1.299553,-7.401592,-3.488496,-2.151445,4.809116,1.201057,1.379586,-3.922633,7.385233,5.982467,-4.151833,-7.145626,2.608206,-2.697673,-6.078394,-9.223740,8.794371,5.568357,7.049819,9.001944,-9.488010], dtype = "float32")#candidate|8507|(640,)|const|float32
call_8504 = relay.TupleGetItem(func_6239_call(relay.reshape(var_8505.astype('float32'), [15, 1, 3]), relay.reshape(var_8506.astype('uint32'), [330,]), relay.reshape(const_8507.astype('float32'), [640,]), ), 5)
call_8508 = relay.TupleGetItem(func_6243_call(relay.reshape(var_8505.astype('float32'), [15, 1, 3]), relay.reshape(var_8506.astype('uint32'), [330,]), relay.reshape(const_8507.astype('float32'), [640,]), ), 5)
output = relay.Tuple([call_8500,call_8502,call_8504,var_8505,var_8506,const_8507,])
output2 = relay.Tuple([call_8501,call_8503,call_8508,var_8505,var_8506,const_8507,])
func_8520 = relay.Function([var_8505,var_8506,], output)
mod['func_8520'] = func_8520
mod = relay.transform.InferType()(mod)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8520_call = mutated_mod.get_global_var('func_8520')
var_8522 = relay.var("var_8522", dtype = "float32", shape = (45,))#candidate|8522|(45,)|var|float32
var_8523 = relay.var("var_8523", dtype = "uint32", shape = (330,))#candidate|8523|(330,)|var|uint32
call_8521 = func_8520_call(var_8522,var_8523,)
output = call_8521
func_8524 = relay.Function([var_8522,var_8523,], output)
mutated_mod['func_8524'] = func_8524
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8547 = relay.var("var_8547", dtype = "float32", shape = (16, 4, 14))#candidate|8547|(16, 4, 14)|var|float32
uop_8548 = relay.tan(var_8547.astype('float32')) # shape=(16, 4, 14)
func_7534_call = mod.get_global_var('func_7534')
func_7538_call = mutated_mod.get_global_var('func_7538')
const_8563 = relay.const([-9,-5,-1,2,-6,-8,5,10,7,8,8,-7,2,-8,6,-9,10,-1,-6,2,-7,-5,-8,2,3,-9,5,4,6,4,-9,-8,-6,7,1,-6,-2,3,-5,7,-4,-9,-2,8,6,1,-4,2,9,-2,3,-1,8,-2,8,1,6,10,-4,6,-10,-3,8,-6,9,7,5,-4,1,-6,-7,-10,-8,1,-1,-1,-7,-7,2,-2,-9,-2,9,9,-5,-1,-3,-7,3,10,8,5,6,8,3,-10,1,1,1,9,7,8,3,9,-5,8,-2,7,-4,7,-7,2,-2,-7,2,-9,-8,-9,4,6,10,-3,8,-2,6,-2,8,-10,-4,3,3,-7,1,-1,-5,-2,-3,-7,4,-3,-1,-3,8,1,-10,-2,-8,-5,4,-2,5,3,-1,-8,10,-7,-8,-1,-6,10,9,-1,10,6,4,-2,5,6,6,3,7,8,-2,4,3,8,-8,9,-6,2,4,-8,9,-5,8,-10,9,2,7,1,-10,2,-9,5,-7,-5,9,9,7,-3,-1,-10,1,2,-8,9,-4,-5,3,8,5,10,7,3,3,-9,-9,5,-2,1,1,-7,3,8,2,-4,7,2,-3,-8,-1,1,7,-9,2,-9,9,6,10,8,9,-10,7,-2,6,-7,6,-6,-3,-4,-4,7,-10,5,-6,3,-6,4,6,-4,-6,9,8,-7,-10,-7,5,-8,-7,-9,6,10,7,-3,-10,5,-9,-1,10,9,10,-2,8,-2,-3,-9,4,-10,3,-4,-2,10,3,-8,9,1,-3,-6,3,9,-8,-4,6,-3,-1,4,6,-5,-7,-10,-2,8,3,10,2,1,-8,4,3,4,4,5,4,-9,-7,-9,-9,6,-3,-8,-8,4,-6,-9,-6,10,3,-2,-9,9,-7,5,-7,7,-1,-4,-6,4,-9,-10,8,-6,9,-7,8,-4,-6,2,2,-3,4,2,8,-3,-1,-1,-5,9,7,-2,-3,10,5,-3,1,2,5,-9,-1,7,5,10,-7,4,4,8,10,7,2,-2,7,-2,9,-3,-4,-2,-10,-9,-1,2,-6,-3,2,2,1,9,-10,-8,2,9,6,5,6,-5,-4,2,-1,6,6,-7,2,3,-9,-2,6,9,5,-8,-5,-5,1,-8,-4,-6,-2,7,1,9,5,-2,-3,3,-4,-6,-3,9,10,-8,4,7,9,4,-8,-1,-2,-3,6,2,6,-3,9,-5,-1,-5,7,3,-8,5,9,8,-10,8,-9,-10,-8,-4,-2,8,-1,10,-7,-3,1,-10,5,4,2,-3,-2,-6,3,9,-10,-3,-4,-1,8,-5,-2,-9,-6,4,7,-9,-10,1,-6,3,1,-10,-8,3,5,-5,4,5,9,6,-9,-6,1,-4,-2,-4,2,-8,-5,6,-1,-8,-9,5,-4,-5,-7,2,8,4,3,-3,-1,5,1,5,-4,-9,8,10,-6,-7,-6,2,6,-6,-3,4,-1,8,-4,-4,-8,3,8,9,10,8,6,-4,5,1,-10,-1,-6,10,4,10,8,5,7,-9,-2,5,-6,-8,8,8,4,6,8,2,4,3,5,10,-4,1,6,1,4,3,-9,-7,-10,-7,-10,2,2,6,3,-1,4,10,7,-4,-1,10,-9,4,-1,2,1,3,-9,-1,6,-9,4,-2,3,4], dtype = "int8")#candidate|8563|(630,)|const|int8
call_8562 = relay.TupleGetItem(func_7534_call(relay.reshape(const_8563.astype('int8'), [9, 5, 14]), relay.reshape(const_8563.astype('int8'), [9, 5, 14]), ), 0)
call_8564 = relay.TupleGetItem(func_7538_call(relay.reshape(const_8563.astype('int8'), [9, 5, 14]), relay.reshape(const_8563.astype('int8'), [9, 5, 14]), ), 0)
bop_8566 = relay.equal(uop_8548.astype('bool'), relay.reshape(var_8547.astype('bool'), relay.shape_of(uop_8548))) # shape=(16, 4, 14)
output = relay.Tuple([call_8562,const_8563,bop_8566,])
output2 = relay.Tuple([call_8564,const_8563,bop_8566,])
func_8569 = relay.Function([var_8547,], output)
mod['func_8569'] = func_8569
mod = relay.transform.InferType()(mod)
mutated_mod['func_8569'] = func_8569
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8570 = relay.var("var_8570", dtype = "float32", shape = (16, 4, 14))#candidate|8570|(16, 4, 14)|var|float32
func_8569_call = mutated_mod.get_global_var('func_8569')
call_8571 = func_8569_call(var_8570)
output = call_8571
func_8572 = relay.Function([var_8570], output)
mutated_mod['func_8572'] = func_8572
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7485_call = mod.get_global_var('func_7485')
func_7486_call = mutated_mod.get_global_var('func_7486')
call_8597 = relay.TupleGetItem(func_7485_call(), 1)
call_8598 = relay.TupleGetItem(func_7486_call(), 1)
output = relay.Tuple([call_8597,])
output2 = relay.Tuple([call_8598,])
func_8601 = relay.Function([], output)
mod['func_8601'] = func_8601
mod = relay.transform.InferType()(mod)
mutated_mod['func_8601'] = func_8601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8601_call = mutated_mod.get_global_var('func_8601')
call_8602 = func_8601_call()
output = call_8602
func_8603 = relay.Function([], output)
mutated_mod['func_8603'] = func_8603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5300_call = mod.get_global_var('func_5300')
func_5301_call = mutated_mod.get_global_var('func_5301')
call_8617 = relay.TupleGetItem(func_5300_call(), 1)
call_8618 = relay.TupleGetItem(func_5301_call(), 1)
func_6264_call = mod.get_global_var('func_6264')
func_6265_call = mutated_mod.get_global_var('func_6265')
call_8631 = relay.TupleGetItem(func_6264_call(), 1)
call_8632 = relay.TupleGetItem(func_6265_call(), 1)
output = relay.Tuple([call_8617,call_8631,])
output2 = relay.Tuple([call_8618,call_8632,])
func_8645 = relay.Function([], output)
mod['func_8645'] = func_8645
mod = relay.transform.InferType()(mod)
mutated_mod['func_8645'] = func_8645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8645_call = mutated_mod.get_global_var('func_8645')
call_8646 = func_8645_call()
output = call_8646
func_8647 = relay.Function([], output)
mutated_mod['func_8647'] = func_8647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8653 = relay.var("var_8653", dtype = "float64", shape = (14, 12, 4))#candidate|8653|(14, 12, 4)|var|float64
uop_8654 = relay.cosh(var_8653.astype('float64')) # shape=(14, 12, 4)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
const_8669 = relay.const([-9,3,2,5,10,5,4,10,-7,6,-10,8,7,1,7,-4,-3,-8,-4,10,-2,-7,5,6,-2,8,7,4,-7,-4,10,-9,-6,-10,9,4,7,10,9,-5,-8,4,10,9,-2,-10,-10,-7,-5,7,-9,7,-10,-9,3,-1,1,-6,3,8,8,-8,-8,-5,4,-1,10,-8,-7,1,-2,-2,-8,-4,4,6,2,10,-1,-5,6,-7,-5,1,3,-1,4,8,2,5,-5,-9,9,7,4,-6,-1,9,7,6,-1,4,10,9,3,-9,-7,5,8,7,-7,4,-3,4,2,9,-6,-1,5,8,6,-8,6,10,-7,-7,7,4,6,-1,7,4,-10,-2,4,3,-7,-4,4,6,8,-10,5,-6,-4,-9,-6,-6,7,1,8,-3,5,-10,1,4,1,8,-10,9,1,4,-3,4,-8,3,-9,3,-6,-6,-2,10,-4,9,3,7,6,-1,-4,8,2,-10,-10,8,9,-4,-4,-2,5,2,1,-1,-3,-7,9,-10,7,-3,-6,-4,5,-4,6,-5,1,-6,9,9,-2,-10,2,-4,-2,7,-8,-1,-10,-9,-4,5,4,-6,-1,-6,1,-5,-7,-1,6,5,10,-8,-4,9,3,-1,-7,1,-2,-10,4,6,-4,10,-9,-5,-2,1,10,-2,-4,-2,-2,9,-4,8,4,-9,3,8,6,-10,6,4,1,-9,-1,-6,-5,-6,5,7,8,-8,7,4,1,2,7,-3,6,-1,-2,9,-1,-6,-8,6,1,10,3,-1,-8,-2,-1,-1,-7,-3,1,-10,-8,1,-9,6,2,-8,-10,9,-4,-2,6,-3,10,-5,9,-3,2,-4,10,3,-6,7,1,-3,-7,-1,10,7,1,1], dtype = "uint32")#candidate|8669|(330,)|const|uint32
call_8668 = func_839_call(relay.reshape(const_8669.astype('uint32'), [2, 15, 11]))
call_8670 = func_839_call(relay.reshape(const_8669.astype('uint32'), [2, 15, 11]))
func_7040_call = mod.get_global_var('func_7040')
func_7041_call = mutated_mod.get_global_var('func_7041')
call_8689 = relay.TupleGetItem(func_7040_call(), 2)
call_8690 = relay.TupleGetItem(func_7041_call(), 2)
bop_8694 = relay.floor_mod(uop_8654.astype('float64'), relay.reshape(var_8653.astype('float64'), relay.shape_of(uop_8654))) # shape=(14, 12, 4)
output = relay.Tuple([call_8668,const_8669,call_8689,bop_8694,])
output2 = relay.Tuple([call_8670,const_8669,call_8690,bop_8694,])
func_8699 = relay.Function([var_8653,], output)
mod['func_8699'] = func_8699
mod = relay.transform.InferType()(mod)
mutated_mod['func_8699'] = func_8699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8700 = relay.var("var_8700", dtype = "float64", shape = (14, 12, 4))#candidate|8700|(14, 12, 4)|var|float64
func_8699_call = mutated_mod.get_global_var('func_8699')
call_8701 = func_8699_call(var_8700)
output = call_8701
func_8702 = relay.Function([var_8700], output)
mutated_mod['func_8702'] = func_8702
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8724 = relay.var("var_8724", dtype = "float32", shape = (8, 5, 10))#candidate|8724|(8, 5, 10)|var|float32
uop_8725 = relay.cosh(var_8724.astype('float32')) # shape=(8, 5, 10)
func_7384_call = mod.get_global_var('func_7384')
func_7385_call = mutated_mod.get_global_var('func_7385')
call_8727 = func_7384_call()
call_8728 = func_7384_call()
output = relay.Tuple([uop_8725,call_8727,])
output2 = relay.Tuple([uop_8725,call_8728,])
func_8732 = relay.Function([var_8724,], output)
mod['func_8732'] = func_8732
mod = relay.transform.InferType()(mod)
mutated_mod['func_8732'] = func_8732
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8733 = relay.var("var_8733", dtype = "float32", shape = (8, 5, 10))#candidate|8733|(8, 5, 10)|var|float32
func_8732_call = mutated_mod.get_global_var('func_8732')
call_8734 = func_8732_call(var_8733)
output = call_8734
func_8735 = relay.Function([var_8733], output)
mutated_mod['func_8735'] = func_8735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5601_call = mod.get_global_var('func_5601')
func_5603_call = mutated_mod.get_global_var('func_5603')
call_8761 = func_5601_call()
call_8762 = func_5601_call()
output = relay.Tuple([call_8761,])
output2 = relay.Tuple([call_8762,])
func_8765 = relay.Function([], output)
mod['func_8765'] = func_8765
mod = relay.transform.InferType()(mod)
output = func_8765()
func_8766 = relay.Function([], output)
mutated_mod['func_8766'] = func_8766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5502_call = mod.get_global_var('func_5502')
func_5504_call = mutated_mod.get_global_var('func_5504')
call_8771 = func_5502_call()
call_8772 = func_5502_call()
func_2832_call = mod.get_global_var('func_2832')
func_2834_call = mutated_mod.get_global_var('func_2834')
const_8776 = relay.const([-4.334565,-2.866180,-0.251047,9.300700,8.444260,-5.161463,-7.034711,5.187309,-9.138114,-8.749378,-9.591346,6.470865,8.742913,-0.623987,0.793027,5.000623,-4.966033,-6.216238,4.388413,-5.918173,2.912113,0.235313,5.513814,-3.275875,-1.771007,9.983443,8.275277,-6.289290,9.160996,-5.480194,-1.790232,0.746949,4.610862,7.548006,6.253613,3.892095,2.836616,0.357507,9.460982,-8.502227,-0.793353,-3.026386,-3.148156,-1.865353,7.462423,-1.219183,-0.681106,-0.532448,1.359174,-1.334145,-6.880299,1.932811,-9.481786,-8.471928,-9.837655,0.854205,-0.327201,1.589008,-8.619791,9.449181,-2.781006,-2.877968,7.531712,-3.081764,-8.024634,9.455795,-3.187552,-6.568131,3.046964,-8.137070,-5.686312,-0.638293,6.755681,9.956311,2.095023,5.250595,5.374353,-6.534216,-6.157354,7.880419,-0.684951,7.650297,-8.469008,9.860786,-6.103091,7.165952,-5.687139,-2.708859,1.995384,5.177564,-4.562675,-4.717918,-7.600184,-8.151447,6.413980,-3.198554,-6.535815,-9.078176,3.311674,1.657740,6.259169,-9.583426,-2.846541,2.891495,8.574805,5.578105,8.559280,9.000396,-6.468217,8.142428,6.723829,3.960927,6.288178,-5.206903,-1.779566,9.761246,2.840344,3.607100,-2.888756,6.548043,7.453287,5.133901,6.525533,9.996722,-1.445896,1.981228,-0.833902,0.108390,8.195456,-6.871211,5.327331,4.946645,-8.565718,5.658881,-6.078667,-3.295105,2.857709,-4.069283,-4.319241,-3.061930,-9.478541,-1.513457,9.844377,8.562230,-0.283533,-4.703783,9.345117,-9.875869,-3.912289,-6.754855,-6.992216,-3.828801,-4.557304,-9.609345,-0.531090,0.892495,6.635569,7.343930,6.747187,0.511832,1.622633,-1.013084,1.728906,-4.392756,-1.167184,-2.585316,6.313840,-1.914060], dtype = "float32")#candidate|8776|(168,)|const|float32
call_8775 = relay.TupleGetItem(func_2832_call(relay.reshape(const_8776.astype('float32'), [168,])), 2)
call_8777 = relay.TupleGetItem(func_2834_call(relay.reshape(const_8776.astype('float32'), [168,])), 2)
output = relay.Tuple([call_8771,call_8775,const_8776,])
output2 = relay.Tuple([call_8772,call_8777,const_8776,])
func_8778 = relay.Function([], output)
mod['func_8778'] = func_8778
mod = relay.transform.InferType()(mod)
output = func_8778()
func_8779 = relay.Function([], output)
mutated_mod['func_8779'] = func_8779
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8799 = relay.const([[[-5.250922,-0.745873,6.098415,5.925440,-8.139529,-3.041409],[2.549246,-1.118438,9.589267,-2.670687,-4.303045,-0.593301],[-5.113588,-5.570337,-7.642175,6.289607,-2.732553,2.574472],[-4.922102,-6.244165,1.992593,0.295304,9.999128,-2.860204],[7.780554,9.288690,8.128650,-4.950289,5.755055,-4.644396],[-0.298132,2.372176,8.982583,8.974671,0.838000,7.608746],[-4.080073,6.250808,-2.780244,-5.844846,-6.395955,-9.633598],[8.492125,3.423234,8.291881,-7.369345,1.312114,-6.766706],[3.202874,-0.107605,3.812537,0.940882,-4.221754,-6.669949],[-9.596335,-3.380702,-1.420565,-9.558522,-8.270354,-1.844613],[1.821327,2.697223,-3.203149,-9.908585,1.349733,-4.058895]],[[-4.814044,1.565035,-8.064478,9.037389,-4.391487,2.397936],[-1.473414,8.107185,0.055794,8.395017,-1.809551,-8.985947],[-2.990678,-7.952828,2.980454,8.673172,-4.998000,3.514393],[-1.896206,7.478251,-5.552378,9.433756,-0.300622,3.657201],[-6.364961,2.409732,-6.674520,-8.185491,-8.816011,-4.011934],[0.623495,3.128376,-7.668686,0.200613,4.145049,-7.274721],[1.002926,8.268934,-3.106768,-3.855542,6.408246,0.976767],[0.603431,-7.330610,3.618671,5.457173,-3.101533,-4.277166],[7.161130,8.626394,8.964817,2.749529,1.914619,-8.552816],[2.244344,2.566294,-0.485178,-4.668307,-7.043768,5.153669],[-2.740815,-1.347987,6.862933,7.788832,-3.037398,-0.266212]],[[-9.885315,4.401792,-5.229721,6.338737,-4.112565,-0.283992],[-7.247813,-7.784265,0.443100,-2.641864,-5.546244,4.668694],[6.574359,6.297003,6.285979,0.588290,8.071383,-5.820604],[9.086230,2.338100,-0.221027,-1.024251,3.960212,2.717382],[2.737691,-6.654822,-9.730550,8.564388,-2.379004,-5.631092],[-7.001696,-8.316991,-4.288504,3.049320,-4.450317,4.076578],[-7.485110,5.770173,-9.297067,5.228766,-8.607699,2.517979],[9.129441,2.019124,8.965439,6.803338,5.398973,7.231381],[-0.616507,6.425681,-1.854158,5.572924,5.685797,-9.807007],[3.124156,1.629685,7.593372,1.622351,4.484297,-0.371999],[-8.162169,6.666476,5.790836,4.756804,4.134886,6.698481]],[[0.819120,6.281698,2.731547,-6.055911,1.865624,2.393106],[-0.642281,7.418443,8.361092,3.938228,7.990171,7.121183],[9.186209,9.590864,-2.012703,-9.734655,8.912328,-9.001692],[0.999702,-6.737756,-3.799002,4.206449,-8.489003,-9.040071],[3.979781,6.494624,-3.964892,4.375971,5.060690,9.559259],[8.387940,0.875751,4.790354,-0.748954,-6.177776,0.582782],[-1.365650,1.126145,8.834886,-4.801337,9.420024,1.457076],[-4.415342,-6.601435,2.299963,2.255900,5.831690,-7.820937],[-7.423509,-0.054875,8.792742,1.427559,-8.391574,-5.610916],[3.142761,-7.356021,-1.710948,-8.168833,4.303536,-4.018602],[-3.933159,2.304136,-0.326044,-8.262418,-4.937369,3.926208]],[[-1.471207,3.352684,5.218663,-3.283105,-1.380293,-8.991333],[0.142488,-0.464192,2.593884,2.639381,-8.117573,7.466897],[-9.003734,-8.211187,-7.392037,-6.874849,-6.081281,-2.195598],[2.929080,-1.254472,9.774028,-1.697810,-7.790602,9.620406],[2.750105,1.923385,-2.415254,-3.317805,5.098928,0.983053],[-5.145484,-1.677805,-0.239341,3.580897,-2.948728,5.587076],[-0.972685,-1.094082,-2.906736,-0.792564,-5.274978,-0.851821],[-7.326923,-7.951136,8.593257,-2.330996,9.577362,-5.417173],[2.985425,-8.870681,-6.698614,0.037382,2.344059,7.004524],[-7.818035,-6.909380,0.811623,0.023401,5.510610,1.844444],[8.266017,3.202428,1.572764,-8.765927,7.620795,-1.275240]],[[6.963535,-7.185172,8.081278,-8.445829,2.871655,-6.292796],[8.341027,-5.830760,7.104267,4.885677,6.487527,-7.791601],[4.967962,1.365203,8.763149,-7.722916,-6.748567,8.983083],[-1.158219,4.775169,-1.563297,-7.398862,8.906979,0.433892],[8.323115,3.359290,1.462026,4.690191,5.152586,7.644319],[-0.331538,9.108029,-5.200425,-7.991481,-9.186503,-5.310240],[5.160670,6.084272,2.902852,-5.123502,1.025152,-7.247106],[8.239520,4.906432,-0.243570,5.606343,-0.516149,1.319964],[5.311595,3.355410,6.041830,0.605861,3.251219,6.539096],[7.057451,2.266980,-6.556801,6.657299,4.816357,-0.945770],[8.925636,-3.219729,-3.201684,-6.467333,1.906792,8.317778]],[[1.459686,9.962411,5.631979,5.701924,-9.406834,-0.528056],[-5.267199,-4.262498,-4.081475,-6.907264,-8.161946,-4.439045],[-6.542376,4.919481,-1.174331,0.466551,1.076039,-1.476457],[0.473541,4.741822,-8.982787,-0.008246,0.680695,-5.336120],[6.600273,4.450438,8.648886,-2.360624,-3.018782,2.581768],[6.192153,-9.268685,-9.165304,8.227103,-1.654493,3.666923],[-8.519707,-1.032461,6.033390,-9.462072,4.868701,-2.419024],[7.502935,-1.065752,-9.214182,-1.038590,-4.044666,-5.597455],[-9.497025,4.056886,-3.304994,5.419004,-0.223740,-4.685616],[6.892395,4.816398,-1.216518,6.115850,-4.548934,6.623529],[-1.206299,-6.021740,-5.656886,1.802357,8.263064,-3.083860]],[[0.355579,-9.188696,0.347447,6.981305,1.188236,3.069411],[9.217273,0.380186,-6.544078,-7.265216,9.739505,-2.517385],[-1.612409,-4.025272,-9.116370,0.683103,-7.203465,2.567487],[5.069274,-7.827775,4.108479,-0.760473,7.339148,7.817558],[4.140419,-1.554193,-0.918770,-6.630104,-5.860121,-1.125779],[2.912215,-7.350505,-9.567405,0.885020,2.301808,-6.360583],[4.364684,2.076234,5.450248,0.418737,-1.846400,5.184931],[-7.765816,2.298390,-7.576533,4.649855,-1.143153,7.943696],[3.178995,-6.451408,3.192963,-9.520544,3.475322,0.154587],[-3.199507,3.737620,-4.624529,5.095516,2.291423,0.363227],[3.618961,1.358151,-7.882781,-6.908987,-2.158114,-7.491829]],[[7.784344,-7.089730,-2.356471,6.168367,-5.137612,-7.712477],[6.270829,7.586403,-1.036223,-5.887002,8.403311,7.470743],[4.915794,-7.590619,-2.294753,5.948181,8.786720,1.250954],[0.861030,-6.610687,8.550968,-8.716862,-9.093295,2.405208],[-2.297551,-8.792991,-0.937287,0.949241,6.150513,7.069525],[7.019187,-0.748429,-5.037998,-7.248526,-4.383232,-7.981223],[3.142095,1.968490,-3.487049,9.862997,-3.224746,9.176139],[9.374294,-6.262929,-0.563354,8.574840,-8.856295,-2.369294],[7.755950,-9.021963,1.134125,2.108292,8.105052,-1.456055],[-1.552518,-2.634679,-6.255297,4.257329,6.255373,-3.308683],[6.596228,7.013467,3.479684,-3.664131,-3.825652,3.675606]],[[5.538992,2.258048,2.745468,2.924803,5.663601,-5.579518],[6.837440,5.442929,-7.559392,-8.319460,6.219440,3.780552],[2.358937,6.126204,6.579947,3.075873,-9.753207,5.486974],[-3.322909,7.817199,3.862150,5.646507,7.354572,9.337728],[0.496478,4.804683,6.389973,9.283000,-5.732413,-4.076393],[6.256264,5.709265,-3.990894,7.325499,1.234066,-5.010023],[1.822464,2.359584,8.540560,-2.483950,-3.166337,1.572409],[-1.479272,-2.690237,-5.971121,-3.174442,-8.631942,4.397164],[9.411531,5.042038,6.723919,5.223333,-0.296998,6.993311],[4.925018,-0.660818,4.255830,4.499107,-2.623387,-8.169395],[-3.593680,6.531211,-1.256390,-5.264814,9.104208,-7.342349]],[[0.749269,3.652510,-0.381467,3.675748,-0.907250,5.828990],[-6.143202,-9.814312,-4.088719,3.301637,4.029596,5.765582],[1.385027,4.472558,-5.273602,0.573632,2.097233,5.696341],[0.727146,6.339393,-3.405862,7.711067,9.192727,6.267544],[-7.891623,8.042339,0.095549,-2.997801,-2.875898,-2.359654],[8.333246,-3.142911,-7.503754,6.174487,1.873264,-5.295591],[0.366885,-7.309224,0.629015,2.873506,-8.264152,9.193411],[3.689398,-5.233177,-7.161046,-6.375974,-7.155207,-9.485543],[-5.358728,-4.041588,5.958657,8.697718,-5.713600,6.988313],[-7.841162,9.365653,8.228945,-1.246869,-9.300636,-2.500729],[9.500295,9.374614,-2.030756,8.175214,9.899513,-9.688066]],[[-2.717466,4.636163,5.220846,-3.814412,2.819231,-2.810250],[-8.940289,-3.641731,1.333558,4.065851,2.399095,-5.932806],[0.947798,2.721330,6.222301,7.366736,4.646405,-6.680279],[9.539859,-9.110420,-0.923258,-5.248366,-6.478437,-4.204667],[1.541597,-5.275383,-0.387080,-6.061283,-8.203517,-9.633823],[5.624851,0.831970,-0.140902,9.756419,-5.707303,5.212921],[-3.624043,-5.315114,-2.835805,-0.089727,-4.212302,-8.082152],[3.041486,-4.467911,-5.956019,5.714657,-8.685472,0.322736],[-2.377593,7.381420,-7.806026,-4.761562,-0.627955,6.089653],[0.181356,-7.368577,1.619791,-4.478216,-9.780437,-8.956229],[3.364934,-1.674016,1.754840,-7.479628,3.454027,-5.496430]],[[-0.757389,-8.004242,8.810825,4.563726,-1.707639,7.827625],[9.754314,-7.559499,-7.558493,-5.133855,0.864028,-2.453623],[-6.002970,-4.549747,-6.400481,-5.697458,0.124925,6.999324],[-6.231630,5.882302,-0.474262,-9.173012,-3.660490,7.746859],[-5.268310,-3.678378,0.903329,-5.890284,-2.437555,0.681371],[4.630832,1.396491,-9.868916,-1.080310,-1.349921,8.059552],[-2.554067,-2.495468,4.134537,6.618036,0.354131,8.518591],[-9.437081,5.024130,-0.901763,4.801415,-4.479400,4.526289],[5.415075,3.549900,3.772354,8.594656,1.091545,5.823701],[0.900387,-2.311086,-2.411161,0.705328,5.639854,2.047138],[6.927131,8.717990,-1.591569,5.381440,-9.261217,1.122852]],[[5.740057,6.534144,-8.938168,8.900653,-9.345558,-5.425282],[0.430821,2.075563,-1.378892,7.037180,-3.081505,4.882508],[4.377728,-1.425471,-5.163960,9.082118,-8.068395,-3.649712],[3.344103,8.000625,0.780069,5.208305,4.290237,7.938774],[7.183079,-5.665659,3.043049,-8.713414,-4.433198,1.537889],[-2.853115,-3.847266,4.625844,9.570992,1.167911,-9.873172],[7.224949,8.495636,3.957591,-1.493846,7.517818,-7.778063],[2.685488,6.156805,7.687286,-3.399584,-6.106421,8.178104],[5.733726,-5.611194,5.455511,4.013977,-9.977390,1.627255],[3.908576,6.944181,-1.786530,0.558496,-8.430889,6.694885],[6.870165,-7.963607,7.157530,-7.431137,-0.240581,9.509876]],[[0.723025,-0.590098,7.807958,3.532754,-1.644497,-7.940606],[-3.624489,-5.391655,-6.945657,7.181704,4.280988,8.151716],[1.831731,4.255033,9.108981,8.260975,9.412380,-4.632329],[5.908992,6.612588,-1.760684,5.117993,5.894932,-6.259434],[8.766056,-0.987062,1.727966,3.455841,3.869604,-9.002001],[2.671639,1.096866,-5.319791,-2.849943,-6.173633,5.907584],[5.335313,1.943578,-1.057224,-6.649373,9.089074,-0.650772],[6.730887,3.211707,-9.652713,0.562762,3.450712,-4.478868],[-7.317873,-7.585792,-8.436097,-0.437092,-5.952744,-7.494573],[4.918793,-5.208290,7.574822,1.174862,8.839246,8.074385],[-8.403852,6.034452,-7.559890,7.316014,-7.113761,1.893317]],[[3.587586,-9.800213,6.374788,-4.507274,-5.541003,-0.711195],[3.716902,-2.312404,-0.489406,-5.571644,-0.730205,5.901626],[9.788112,3.684187,-4.849690,-6.849739,-6.801521,4.741397],[-4.038602,-6.797638,-6.394865,-6.675940,-9.038939,-5.814216],[6.649191,-7.907290,4.819980,-6.682312,-2.715529,-5.222895],[-5.110020,2.642782,-8.539794,-3.839610,-2.335480,3.111797],[5.766195,0.028274,-4.316527,6.202643,-5.091625,9.797180],[0.088911,1.791725,1.453316,-0.262191,-1.535443,5.904427],[-9.479045,1.430385,-5.237615,9.425375,2.963812,-3.776281],[8.120265,1.086691,0.055356,2.153199,-7.532200,-7.367735],[-2.848862,4.966309,-3.422401,2.690694,-1.887462,-5.781269]]], dtype = "float32")#candidate|8799|(16, 11, 6)|const|float32
uop_8800 = relay.cosh(const_8799.astype('float32')) # shape=(16, 11, 6)
func_3331_call = mod.get_global_var('func_3331')
func_3333_call = mutated_mod.get_global_var('func_3333')
call_8804 = func_3331_call()
call_8805 = func_3331_call()
const_8815 = relay.const([[[8.066022,-8.656539,-2.905182,0.219950,-0.329117,6.105408],[2.335898,-6.051340,-6.207582,8.506151,-4.633333,-1.996982],[-6.843745,-1.209431,-7.325690,3.441294,-1.942026,-0.026847],[-1.081712,-7.755784,3.846834,-1.520220,-1.218768,2.657122],[-8.322825,9.936044,-8.380012,6.675041,4.676236,-9.488195],[8.484982,1.237057,9.588130,-6.754126,0.158163,5.874673],[-1.329198,3.345234,-7.553468,5.464558,-3.971180,-1.896496],[-9.187506,9.816176,5.336727,8.956655,5.703682,-3.638235],[-3.533728,-8.383484,5.889691,9.506701,-0.969224,5.455682],[2.053154,6.045502,4.788336,-3.165444,2.655193,2.544844],[-3.186801,1.821184,3.205480,-1.531539,-9.161040,-5.670529]],[[-0.974432,5.929375,-1.360073,-7.238292,5.250752,3.478081],[8.616532,-0.699711,1.024593,0.446081,-5.289859,9.495227],[4.086152,9.544705,6.128387,9.641075,6.112161,-2.532455],[3.339314,9.483200,-5.491062,8.719203,7.397442,-1.678015],[6.624186,-4.363403,-5.005950,-5.327566,2.261695,6.607344],[9.778032,2.485488,8.561441,-9.626656,-6.746179,7.343769],[0.112772,-5.405643,-8.807042,7.052561,-2.381056,8.156647],[-5.353874,-6.804835,5.207970,-4.085180,9.114555,-4.808083],[9.331334,5.454839,-0.265907,-6.974447,-3.030352,-4.201967],[5.201970,-6.921675,7.131099,-7.433261,6.459334,-4.182749],[-0.267062,8.114640,-0.732869,-9.354223,7.462514,7.379862]],[[-4.421917,7.271186,-7.360711,5.968475,8.343858,4.033676],[6.361421,-4.326046,0.482010,6.390750,1.051532,3.169624],[-2.305020,1.031487,8.939553,-6.330138,-8.150070,-4.538167],[0.089902,-6.873775,-7.402463,-5.052839,8.459112,-3.134091],[1.826497,-2.036087,9.612579,-6.544977,3.233891,2.226469],[-3.126072,-3.542812,6.025859,0.394835,-2.803319,7.971925],[8.370149,-5.628872,9.511368,2.224688,8.729286,3.163333],[1.854093,-6.638931,-0.590013,-8.905894,1.372858,3.278736],[9.152466,-8.759263,3.230892,-5.309113,6.147700,3.391868],[-0.909193,5.210772,7.255600,-0.677222,-5.162774,0.213693],[-6.408453,4.354370,2.813062,-6.302534,1.744511,-1.024723]],[[-8.149549,6.886313,-3.292550,-7.921371,-7.685186,-2.651973],[5.442131,-5.748339,2.830518,-5.070912,9.188507,-8.997623],[-6.783332,-9.747528,9.997881,-1.800593,2.287415,7.625575],[0.516411,-7.491282,3.277628,1.259685,5.845933,-6.796401],[1.924506,-4.474638,-5.582994,2.716094,7.592814,-9.989960],[3.227853,4.398622,-9.367377,-8.658228,-3.295220,3.328640],[2.336842,-7.137216,8.426806,7.105169,5.872716,8.681889],[-3.381370,3.293839,-8.663225,-7.395811,-3.805928,2.496020],[-7.737421,-8.351045,-8.511484,-8.469522,-0.539445,9.151934],[0.548082,5.166884,-9.413339,-6.602319,0.205778,7.610854],[1.280333,7.136765,4.135118,4.909025,-8.807075,-3.503755]],[[0.806679,-7.006308,-8.686964,1.938994,4.795609,-0.334308],[-0.346950,-9.266830,-2.195544,1.932087,-3.902665,-1.586929],[5.717378,1.993831,9.353232,8.549120,3.094526,2.782449],[6.752391,2.605918,5.313348,-7.693965,1.985499,4.949602],[-6.683260,8.177241,-3.993011,-4.248678,5.891535,4.728977],[-7.305112,-5.323587,1.525195,5.456355,-6.204100,1.876157],[-0.445140,6.030265,-5.667890,-3.771887,-7.642543,0.772652],[6.094524,-3.468834,-2.506825,8.802493,-7.519312,-6.263425],[2.368083,-7.396860,-3.488359,9.839738,-5.763471,-6.949978],[-6.354699,7.364086,7.280636,5.869036,0.883837,2.120675],[2.967439,-8.779131,-8.988763,4.096559,-0.595147,-7.941749]],[[6.024127,1.973657,-7.677071,3.602781,-5.019834,6.971630],[5.824677,-0.471958,4.923456,-1.942248,8.756545,-8.169940],[0.996931,2.072410,-2.650188,4.698207,-2.533925,4.858936],[-6.413519,3.164708,7.415240,-6.159236,2.466625,7.528051],[8.122057,7.530362,-6.835334,-2.980397,-0.261835,5.013957],[3.581335,-8.027153,-8.748506,6.036622,-7.514200,4.737441],[3.560325,4.165379,2.161502,0.253425,-3.239739,7.309895],[1.078921,4.520732,6.467119,-9.662299,3.565594,-0.452141],[-4.643344,-9.207507,-0.189619,-5.966783,-7.294721,-3.792452],[7.089255,-2.012670,0.132525,-3.691218,8.280704,-9.925898],[2.368344,-2.861398,8.335690,-4.744496,-4.639449,0.610142]],[[-3.126198,-8.082294,1.559347,-1.617582,2.296728,-2.456836],[-2.640245,3.142068,-7.554225,2.765762,-8.851697,-9.667986],[-2.224402,1.863394,-8.697908,-8.058822,-4.838214,2.659849],[7.476913,-6.747072,-4.832759,9.103703,-7.045017,-3.613384],[-4.809161,-0.946553,5.081582,6.648322,2.722913,-1.804974],[4.924177,-2.179427,-0.352039,8.259561,-2.089557,-6.867852],[-3.043930,9.416946,-1.860929,-5.024341,0.797110,7.537460],[0.273306,8.339584,4.583163,-8.757360,-4.508710,-9.437645],[-1.904290,-9.041022,-6.151121,8.058893,6.107748,4.183796],[8.443622,-3.892359,-2.813654,5.110687,-6.887708,-7.706036],[8.655626,-4.759045,7.529470,-3.991502,-1.738484,-3.703841]],[[0.786587,-0.403679,9.798908,-0.922068,1.196903,7.671361],[-2.669775,9.320257,7.005539,-7.798782,1.870690,-4.757527],[0.683483,-1.670394,-8.921076,-2.290118,7.331768,-6.751362],[-6.841749,1.922074,9.866210,0.430083,3.647737,0.582304],[-4.937227,5.029830,-9.444800,9.191421,-3.977517,-4.580578],[-5.069743,-1.447789,7.504667,-0.793433,0.496553,7.380202],[7.286995,-2.677175,0.009788,8.985124,5.288096,5.045016],[1.969759,-6.699201,0.200850,-8.422886,0.555545,3.746426],[4.583939,2.134518,5.317610,2.201086,0.359870,6.740507],[7.598301,9.215873,-1.989802,3.563615,2.960489,6.601907],[-9.678957,-7.416054,7.056036,-0.827054,-0.472550,5.050798]],[[-9.505718,-2.328315,7.025615,-1.515740,-7.162884,7.305185],[8.557740,-8.904174,-2.894639,5.081497,0.754214,8.886299],[2.288185,5.875941,8.000235,8.146077,-1.380762,2.572096],[0.747181,-2.149547,1.877089,-4.891114,-9.648980,6.733909],[8.076800,7.794880,5.464278,5.685038,-8.520487,-5.097380],[1.713780,8.453077,8.843889,5.956782,3.670803,-2.677224],[-8.120770,3.524479,-6.544957,4.598700,0.106031,-9.443559],[9.283986,7.923938,4.573622,7.481508,9.245302,-3.773610],[-4.351061,5.937417,8.802028,-2.670369,5.976405,5.010370],[4.213111,4.853948,8.125682,7.217876,3.038366,3.474151],[-4.940797,8.950155,4.473118,-6.523667,-8.694543,3.297259]],[[9.942390,3.445537,9.445078,-1.661650,0.578773,9.772504],[-0.504757,-6.477987,2.071845,-0.856010,-7.355150,8.030301],[3.314886,2.290275,-2.890740,8.994865,5.911578,-4.703525],[6.968734,7.908885,-3.031090,-7.652296,1.636318,-4.845172],[-7.102622,-6.921567,-3.476306,-7.801295,7.994522,8.831617],[7.832068,6.752862,1.969458,7.864736,6.379061,-0.445193],[-6.707384,-3.498791,2.130114,-8.558116,7.457456,-6.942841],[8.448210,1.060224,6.665394,-1.886475,1.705031,0.566806],[0.102960,-6.931082,4.015401,-0.783369,5.318788,8.393626],[2.938810,-9.248945,-6.537975,-4.392253,8.963149,-2.058552],[9.150216,5.581719,-7.099308,1.328784,-1.911630,-0.458850]],[[-9.734863,9.596525,2.835797,-7.235167,-5.794167,4.861866],[-3.488807,-3.312426,1.959191,-4.067180,0.899770,-4.829291],[-5.245617,1.630898,0.249020,-7.808579,-6.219952,8.145755],[-2.914087,-5.777383,-0.717438,7.324602,-0.637165,-9.128648],[-1.943916,-0.541664,9.325513,3.249922,-3.071163,-9.941804],[5.146029,-7.804121,-4.984301,0.243826,5.699446,4.758954],[-2.487818,-8.995493,5.461456,-4.580877,3.811069,0.966806],[3.022679,-0.105093,-8.649243,9.420534,0.979298,7.607546],[4.861573,-2.920613,4.646692,-4.807966,-7.007497,-3.072681],[-4.266222,4.483042,0.455246,-3.589661,-4.444917,-1.404785],[3.632118,-6.578414,6.284458,-4.962799,-3.438617,-7.571653]],[[-4.856851,8.163257,0.694318,-3.919116,8.117755,-2.895366],[3.853658,9.102164,0.052085,-9.702549,-6.916395,-2.875618],[-3.632629,-4.765883,2.813897,-2.405209,-8.260365,0.981566],[6.335275,2.557365,6.380209,2.740137,-6.080319,-2.908142],[1.659619,-6.943981,4.678933,5.490878,4.648629,3.797021],[-2.739999,-5.943162,2.943276,5.090156,-4.334449,7.001143],[-5.495997,-8.185501,-0.650350,-3.433713,6.378550,0.481446],[3.446779,-0.355285,-1.499095,-0.795074,-3.092830,7.863552],[-4.540675,-9.260530,5.940951,-2.116437,5.492173,-6.670227],[-6.461978,5.643737,4.042125,-2.885997,8.250348,8.540658],[-8.637926,4.079995,1.936234,1.277730,0.943063,-0.757781]],[[1.232591,-9.107222,3.382451,-3.114599,5.158252,5.660280],[-9.498954,-3.656454,-7.073134,-9.292281,7.291114,5.494399],[-0.705830,-4.365496,7.058408,1.411929,5.767537,8.952631],[-6.865088,-7.942938,6.326987,1.059210,-6.054011,9.229186],[2.376283,3.110203,5.494614,1.798864,9.692414,6.610779],[-1.285309,-3.551589,-9.502057,-7.442144,9.328005,1.627330],[-1.683455,7.789016,-8.063439,-2.999794,-9.282437,-1.443653],[-7.754922,9.743925,3.619806,-2.904046,6.068411,9.396661],[-4.733656,3.057467,6.764766,-7.470822,5.843337,-8.111112],[9.310644,2.350686,-9.240478,1.563219,-4.919744,1.907813],[-7.275307,3.045145,-2.073472,0.086914,8.966096,-5.130525]],[[2.646503,-9.703859,-7.018391,-1.119954,0.453631,9.062225],[3.806594,4.863499,-1.974635,5.319293,-9.726446,-5.252429],[-3.030619,-1.196249,-8.579543,-2.427402,3.555281,-0.239443],[8.387915,0.024299,8.014776,-8.182931,-4.418795,-7.978254],[-1.593382,4.812888,-1.944189,9.821422,6.824519,-7.879495],[9.579017,-1.311647,-7.395707,-2.454296,8.526993,-5.359382],[9.665209,-7.291657,-9.549612,-8.532942,-8.734928,-4.683101],[7.925490,4.022755,2.381481,9.432575,-3.698655,4.451053],[-3.604976,-6.092009,-7.917617,-9.706957,-5.416789,0.749205],[7.726401,7.316023,3.580229,9.557559,-1.942147,5.031827],[-7.439711,-5.237945,-5.072689,7.483809,4.860075,2.787146]],[[6.410716,7.312520,-1.686546,-4.734434,-7.347992,8.932006],[2.895777,7.966897,-1.671872,3.977440,3.851115,7.527721],[-0.775111,-4.688609,3.323189,6.173071,-7.532638,-1.365946],[5.418512,-0.029786,-4.105960,2.011938,-8.814224,6.110371],[9.452781,-3.212655,-5.862075,9.456820,-1.182413,7.740148],[2.810172,-3.587310,0.841692,-6.516567,-6.783065,4.406158],[-9.627506,-6.772611,8.776183,8.362202,0.190120,8.098435],[-9.500756,-2.257861,-2.556032,-5.116645,-4.345639,2.520987],[7.573022,-2.777024,8.929311,-9.464363,-3.522863,-4.759338],[3.142119,-7.653432,0.265698,-1.036020,-5.088941,3.497069],[-5.432749,-6.743561,-2.893662,9.413130,5.172642,8.927883]],[[8.895923,8.483302,5.762666,7.860321,7.078356,3.338426],[3.426236,-1.388164,-6.714400,-5.541416,0.017900,1.798161],[2.434473,4.257534,-4.971827,9.023106,4.160181,8.233275],[-4.092473,0.122681,-2.615818,2.275508,-5.785157,-5.908818],[8.424532,-6.238253,2.586906,-4.656116,-4.070779,-0.567609],[6.569386,-6.227896,-1.063504,8.976853,-4.913348,-3.143085],[5.026287,-6.281590,-2.817950,-2.794987,9.570165,-5.670644],[-6.497872,0.630614,7.306689,4.963883,7.124356,6.828051],[1.301458,0.908887,9.621568,-7.025835,7.972883,-9.627103],[8.183549,5.977807,2.520354,-6.766997,-7.409323,-8.422436],[5.001433,-5.932048,6.951298,-4.009941,-5.981095,-1.099181]]], dtype = "float32")#candidate|8815|(16, 11, 6)|const|float32
bop_8816 = relay.left_shift(uop_8800.astype('uint8'), relay.reshape(const_8815.astype('uint8'), relay.shape_of(uop_8800))) # shape=(16, 11, 6)
func_8382_call = mod.get_global_var('func_8382')
func_8383_call = mutated_mod.get_global_var('func_8383')
call_8829 = relay.TupleGetItem(func_8382_call(), 1)
call_8830 = relay.TupleGetItem(func_8383_call(), 1)
func_6094_call = mod.get_global_var('func_6094')
func_6096_call = mutated_mod.get_global_var('func_6096')
call_8837 = relay.TupleGetItem(func_6094_call(), 0)
call_8838 = relay.TupleGetItem(func_6096_call(), 0)
uop_8839 = relay.asin(uop_8800.astype('float32')) # shape=(16, 11, 6)
output = relay.Tuple([call_8804,bop_8816,call_8829,call_8837,uop_8839,])
output2 = relay.Tuple([call_8805,bop_8816,call_8830,call_8838,uop_8839,])
func_8858 = relay.Function([], output)
mod['func_8858'] = func_8858
mod = relay.transform.InferType()(mod)
mutated_mod['func_8858'] = func_8858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8858_call = mutated_mod.get_global_var('func_8858')
call_8859 = func_8858_call()
output = call_8859
func_8860 = relay.Function([], output)
mutated_mod['func_8860'] = func_8860
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7485_call = mod.get_global_var('func_7485')
func_7486_call = mutated_mod.get_global_var('func_7486')
call_8880 = relay.TupleGetItem(func_7485_call(), 1)
call_8881 = relay.TupleGetItem(func_7486_call(), 1)
func_6887_call = mod.get_global_var('func_6887')
func_6890_call = mutated_mod.get_global_var('func_6890')
var_8883 = relay.var("var_8883", dtype = "uint32", shape = (392,))#candidate|8883|(392,)|var|uint32
const_8884 = relay.const([6.008726,9.342624,6.755798,-4.789799,4.474834,6.557707,-4.851227,0.094518,7.614359,8.669541,-0.570761,-4.700323,9.471059,-0.376066,-1.898235,-8.650280,-0.838336,8.919526,-0.235022,-1.052066,-3.828411,-1.531732,-4.985111,0.467345,8.980792,-4.864156,-5.053142,-6.106248,2.205118,1.004163,-9.544785,5.494605,4.328857,-9.554820,-3.984318,2.074064,-1.688994,6.239127,-6.415340,-6.801743,-5.095577,3.609701,-4.624616,-5.735890,-3.573133,2.810598,-8.179541,1.019587,8.152085,5.784941,-2.613189,-2.715849,-5.248258,0.172455,6.596211,-1.354200,-7.914294,-9.922511,-8.141025,-6.626950,-3.870271,5.518961,6.647705,-1.491980,-2.163362,-7.648094,1.756169,1.637762,2.144516,-3.660062,4.500481,-1.147927,-9.679047,-4.552809,7.482057,5.297620,-6.393629,-4.583378,3.277385,8.964634,7.560307,-9.566405,-2.522599,-6.802220,-0.219207,-5.676533,-2.630911,-9.219956,-4.750495,7.328943,3.432625,3.905646,3.200089,1.345953,9.611289,-3.852474,8.067525,0.214249,-0.144736,5.288015,-3.232523,-4.867549,-4.426301,0.783677,7.204955,-4.824179,9.806914,0.302890,-4.710783,3.108914,7.412710,-9.205290,-6.515888,-4.200398,2.409319,7.751496,-7.969360,-4.383968,-0.484178,6.972187,-3.198186,5.926000,0.107915,-0.617515,5.659855,9.631830,0.564060,3.549801,4.589502,0.156199,6.547596,-7.195064,-3.808942,-1.314212,-6.811055,9.065708,-6.211281,-1.201882,9.755719,6.041214,-1.156725,5.463363,-9.703250,4.260549,-8.457034,-7.587731,-4.788160,5.887062,-1.697531,0.902712,5.903543,9.351771,0.794270,-2.559708,6.817315,-8.068822,-7.338304,5.897298,-6.237423,4.939113,0.090819,2.046496,-2.942368,8.284227,-3.533288,-5.975582,7.460012,0.749659,7.299306,1.004015,0.707663,0.771697,0.300950,-3.326105,4.879669,-9.707639,-5.864943,-1.603777,1.567775,1.726279,5.095670,2.973429,7.803895,0.270014,-5.136246,1.417889,-6.112406,-9.308639,-5.882666,-2.359754,-1.335162,-8.766173,-6.831646,9.925893,-1.968455,6.184541,-7.001687,-3.788586,-4.114296,2.734177,-4.666237,-9.817165,5.053986,-5.833966,-4.454953,5.115564,-5.259890,3.204566,8.700786,-8.834591,9.899993,8.171222,-5.772961,1.181396,6.468632,-4.215546,-5.008321,5.864723,9.584561,3.123617,-8.029701,-0.508145,-5.057630,1.944946,-1.844566,-5.835387,7.262819,-7.574914,6.682844,-5.211425,-8.671536,6.114102,-9.467173,-0.797688,-9.942206,8.115318,-2.255670,1.755931,0.810449,-4.031349,-7.234998,4.405139,-1.658584,-5.025574,4.568881,1.522692,2.849699,-8.994329,5.323056,4.856026,-6.419409,-3.831777,-4.025752,-6.035841,-8.637012,8.389001,1.416678,-8.661498,-0.767505,5.951466,-3.410037,4.775683,3.368512,1.791221,-9.713748,1.988879,7.176893,-1.098706,3.865092,2.776803,3.271491,9.722832,2.243267,0.104007,-0.556344,2.353137,7.458611,-7.892352,2.738344,8.655113,-3.885330,-1.619405,-2.279591,5.828241,5.555137,8.411310,5.571791,5.512148,-4.980744,5.702326,-1.857881,2.887312,8.294371,-7.954414,3.778749,9.844500,-7.195035,6.590066,-3.946516,5.199107,3.188774,-2.362948,9.310604,9.285822,-8.561097,-9.026282,-2.981181,-6.097056,7.532426,-6.252470,-1.009919,-7.435946,0.322732,1.364936,-7.969959,-4.829504,7.397172,-5.962872,-9.958920,9.623106,-2.014416,7.666322,0.009480,1.975711,8.525335,-5.539723,2.352169,-2.698924,-6.593961,-2.631030,-5.903646,6.737597,6.575216,-8.236362,5.511826,2.295550,0.304079,-1.602085,-2.699669,6.933858,0.151242,-3.258291,-6.362996,-0.530489,-8.531757,9.599679,5.856439,6.994422,8.634170,-1.650314,7.789119,-6.460987,4.273818,5.119961,-1.156458,6.357852,-8.476243,-0.471823,-0.443393,-5.851476,6.735941,-5.867215,-7.164217,-2.770835,1.844124,-6.962789,-6.408406,-8.632696,-2.543668,0.879294,-4.013129,-6.186619,-7.246311,-7.771800,1.970845,-6.601801,-1.731294,9.558155,-8.441856,-7.122497,2.649437,-8.480806,-0.022616,2.146687,-7.107659,7.381884,8.497805,-6.285743,2.115795,-1.155506,4.353199,0.425124,1.700849,-1.742029,-2.319375,-1.599222,6.717905,5.081732,7.665921,-7.381641,-1.243131,-2.872119,-5.751724,1.577373,6.562574,-6.100835,-6.658756,2.749353,5.599686,4.629280,-5.868209,1.780658,-2.505080,5.561650,7.107060,-2.071347,-8.202661,1.062410,0.938027,-2.297177,-7.151740,9.895417,-8.419567,4.906555,-9.414756,-5.247003,-8.595413,-1.411644,-9.478683,-6.824290,-3.241934,4.338779,8.102022,8.701362,-5.998677,-4.789644,-5.193790,3.975174,-9.996375,-1.679412,-2.089308,4.207978,-0.204156,6.668593,-3.145541,-4.100749,-7.438710,0.792827,-4.579041,-7.728778,-0.733308,-5.544933,-9.725738,7.962400,-5.683358,5.995465,-8.193096,0.340160,4.591299,-3.261273,-3.987538,-9.514054,-1.957000,-1.793006,-4.699874,6.317856,4.666725,7.664304,-9.009707,-0.207706,6.783499,7.418664,5.927300,-0.343760,9.946992,-8.250256,-5.170056,5.123931,-4.569529,3.037860,-3.978617,8.164868,-5.920715,-9.206138,4.170165,2.318166,-7.051160,4.407683,9.817798,-6.755311,-4.165525,-6.706556,6.450179,1.990020,-6.350949,-2.550562,-9.722561,-7.318525,3.788798,4.959002,-9.894554,3.453776,8.653985,-3.238074,-7.926523,9.552877,3.311514,0.934218,0.690104,-0.209791,-4.432298,8.562447,-5.583090,3.007367,-8.681850,-1.636355,-0.438866,0.972732,-0.681468,-7.829521,9.602531,7.693414,-6.195883,8.746595,-7.694983,5.565951,5.109409,0.343455,-8.152975,4.378223,7.626751,8.557797,8.453717,9.880158,-4.868414,-9.474872,9.834007,-9.008125,7.726603,-8.442616,3.882639,-7.424646,-1.210041,-3.617035,-0.933981,1.224694,-9.196190,4.603355,2.688261,4.927401,3.415060,7.486249,-3.310601,-4.993527,-5.415714,3.488728,-6.736998,-4.799611,5.174024,0.042513,-6.695067,7.472395,-8.701202,-3.341695,1.159422,6.117737,2.133239,8.190187,6.409551,0.164560,-3.256585,8.220504,-1.664329,1.554172,0.873159,-6.480691,2.369733,-3.330192,-1.125429,-8.383608,-4.131591,-3.869888,-5.853929,9.856792,3.565111,1.596001,1.723622,-2.334880,-0.168139,1.404057,4.047591,9.321325,9.253686,-5.119696,-1.520625,1.397801,-5.620900,2.292912,-2.953615,-1.695844,5.749844,5.692853,0.756561,4.175025,-1.678133,0.717014,-7.471553,-0.546114,-0.961216,1.710088,5.349792,0.438545,3.500145,4.710144,-1.470892,7.850503,5.654449,-5.025871,6.514795,6.636327,3.991789,5.309393,0.148583,5.786654,-6.766659,3.957676,-8.222654,0.659440,2.128102,9.206053,0.821261,3.959064,7.370947,1.869131,2.953747,-0.770346,4.769035,-5.430223,-9.476725,-7.908833], dtype = "float32")#candidate|8884|(640,)|const|float32
call_8882 = relay.TupleGetItem(func_6887_call(relay.reshape(var_8883.astype('uint32'), [7, 56]), relay.reshape(const_8884.astype('float32'), [640,]), ), 1)
call_8885 = relay.TupleGetItem(func_6890_call(relay.reshape(var_8883.astype('uint32'), [7, 56]), relay.reshape(const_8884.astype('float32'), [640,]), ), 1)
output = relay.Tuple([call_8880,call_8882,var_8883,const_8884,])
output2 = relay.Tuple([call_8881,call_8885,var_8883,const_8884,])
func_8887 = relay.Function([var_8883,], output)
mod['func_8887'] = func_8887
mod = relay.transform.InferType()(mod)
mutated_mod['func_8887'] = func_8887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8888 = relay.var("var_8888", dtype = "uint32", shape = (392,))#candidate|8888|(392,)|var|uint32
func_8887_call = mutated_mod.get_global_var('func_8887')
call_8889 = func_8887_call(var_8888)
output = call_8889
func_8890 = relay.Function([var_8888], output)
mutated_mod['func_8890'] = func_8890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7647_call = mod.get_global_var('func_7647')
func_7648_call = mutated_mod.get_global_var('func_7648')
call_8897 = func_7647_call()
call_8898 = func_7647_call()
output = call_8897
output2 = call_8898
func_8903 = relay.Function([], output)
mod['func_8903'] = func_8903
mod = relay.transform.InferType()(mod)
output = func_8903()
func_8904 = relay.Function([], output)
mutated_mod['func_8904'] = func_8904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4306_call = mod.get_global_var('func_4306')
func_4307_call = mutated_mod.get_global_var('func_4307')
call_8919 = relay.TupleGetItem(func_4306_call(), 0)
call_8920 = relay.TupleGetItem(func_4307_call(), 0)
func_6887_call = mod.get_global_var('func_6887')
func_6890_call = mutated_mod.get_global_var('func_6890')
var_8928 = relay.var("var_8928", dtype = "uint32", shape = (392, 1))#candidate|8928|(392, 1)|var|uint32
const_8929 = relay.const([6.448854,-4.802817,3.219658,-2.548529,-2.393778,-4.485257,0.128134,0.859747,4.820880,6.750557,1.507882,-4.171814,-0.424911,-9.832501,0.872877,-7.951904,7.013151,-1.981895,0.675965,-3.169010,7.785712,-9.829392,-0.397710,5.355296,4.515603,5.950021,-2.918176,1.654374,-5.567176,-5.395638,6.745319,-4.495588,6.326999,9.607235,-1.030020,-7.029944,3.609726,-7.131932,-4.256295,2.383994,-1.959550,-1.205652,-6.702911,-9.734592,-8.517650,-3.163963,5.504755,-9.220335,-6.872351,8.423061,0.738213,-0.769036,-6.027591,-4.672605,-6.261032,0.449723,-9.952254,4.052082,8.658417,-9.978301,-2.453045,4.787736,1.983882,-3.750013,7.412419,-8.045344,3.350421,8.756504,7.959796,-1.088799,6.224383,2.280286,-1.221526,2.832735,-7.635696,7.585966,-4.212340,-3.095757,-6.041196,5.568432,2.899094,8.604193,5.459296,-6.921792,-7.660520,-9.307198,-6.089940,-7.243402,8.599145,-8.125671,4.875821,-1.819586,-0.274756,8.462863,-4.836583,1.061714,4.302898,-6.217259,0.603171,5.560712,-6.329180,-1.777635,9.878539,9.943088,-4.502980,-3.363396,4.476861,0.353016,-5.681480,-1.067759,-9.562923,-9.894979,-4.106019,-8.759223,8.820767,-0.747655,3.127473,7.064385,1.754924,0.488406,-3.398026,3.315985,9.842581,-5.312412,1.232573,-1.406790,-1.261947,5.487055,3.032939,-8.302147,-0.539435,-2.479124,6.377083,-0.955771,-3.546904,-8.995773,-9.414355,-3.240925,3.462325,9.990180,-6.240408,-5.480668,-4.220390,1.113063,0.738429,-1.064883,-7.425134,8.337899,-1.308013,-0.985807,-1.059869,-6.645733,-6.254520,-5.184277,3.910613,7.705445,4.818954,-2.842147,1.696603,5.269306,5.347321,-5.617976,7.026051,-6.871119,-1.272743,-4.854484,4.306229,3.436205,-1.189343,7.352720,8.091325,0.987001,-2.982891,-8.923007,0.422579,-3.723510,3.605242,2.908170,8.248299,8.607016,-8.219598,-3.913672,-2.833239,-4.977960,0.415153,-3.402245,-3.721403,3.785235,3.597481,-5.077116,3.745094,3.704206,-5.323223,2.299989,-8.263565,4.311363,9.997134,2.716622,1.422313,-3.545782,6.196948,8.483738,-6.444365,2.917771,-9.161826,-3.364283,-9.773512,-0.940556,-9.653632,-8.055116,-2.318377,-7.318437,5.272314,9.714557,7.150112,8.638658,-4.735230,-4.636219,1.640408,-9.123732,3.954098,-2.844842,9.682519,-2.135203,-1.065758,-0.098921,-4.911102,-1.391654,-9.385139,-7.633062,3.440130,6.282470,-6.424441,-6.993185,4.008749,2.163704,-8.695931,-4.678279,3.740097,0.179345,-9.643130,-3.678469,-1.766860,-1.711651,0.388772,-2.439592,9.708143,-8.057110,6.286376,6.397004,-5.500878,-8.662903,-2.735792,-4.005498,7.557548,-3.108322,0.320377,4.431546,6.624312,3.484452,-7.561004,-7.623754,9.719275,-9.221472,7.565809,3.725894,-4.633560,-4.354300,-5.432073,-5.254118,6.277122,3.884873,-2.508433,-7.119799,5.874474,-4.184341,-4.709907,4.849741,2.209915,-1.769534,9.283281,-1.707848,0.428648,9.158378,4.127772,-2.411372,-2.916443,-0.447449,-5.019376,-0.186065,-5.218361,8.568651,4.960416,-2.970743,-5.980943,-1.086927,-2.624305,-0.262347,6.173355,9.298102,2.790610,5.890710,-2.694462,-9.309018,4.754505,-7.163013,3.997044,-5.816844,-7.699353,-1.585992,0.473941,-7.978667,9.649180,-0.303618,-3.932782,-7.755330,1.601346,5.234233,5.969596,-7.505758,9.581778,-7.889871,-8.471865,9.090869,0.820963,-1.573707,-8.814047,-6.295869,6.745778,9.579723,-2.588548,2.631547,3.258719,8.290581,6.311403,2.323368,-1.770894,6.869206,-2.011988,4.119211,-2.914042,7.869364,9.607658,4.647066,-2.375343,-1.312494,-8.362558,-3.990001,2.888112,-2.839342,6.424224,0.606782,8.047504,-7.439943,2.596980,2.283834,0.061036,8.275762,-5.515955,5.252470,3.275400,1.570467,-0.215081,1.243022,-6.608647,-1.554123,-4.389744,1.447631,-6.673769,3.446626,-1.539220,-9.759626,0.185727,-5.935853,-3.432680,-9.425609,1.348692,6.608360,9.326046,8.468286,-9.688212,7.471717,7.466938,-1.685856,1.739734,-5.460660,-0.155360,2.099253,-3.160098,4.080432,-3.443776,-4.224799,1.909006,9.745403,-5.893994,-1.267603,-1.316330,5.388290,4.366614,9.589605,-3.313778,-5.952130,-3.610949,-8.697756,2.008282,5.390159,-6.312172,9.412321,0.119140,-1.233876,-4.668983,-3.380003,7.208525,-9.765401,6.476254,7.149716,6.356509,-1.236935,8.786373,-3.906394,-5.886650,-9.736478,6.620353,2.124064,-6.148514,4.466762,-7.763050,0.192141,3.427529,-9.403728,-5.823429,-8.143567,9.177415,9.420532,-3.547108,2.418636,-1.363026,7.994174,-8.454105,-6.898829,-4.690979,9.451475,-9.464822,-8.579946,-6.510910,-3.589639,-9.939902,0.344088,-8.809717,8.531903,-8.096542,2.084427,-6.949257,3.081958,9.655066,-8.140555,4.982067,9.182055,-2.755836,0.242946,-0.775448,4.871491,1.120725,0.356384,-2.927479,-2.018393,1.435006,9.392860,-5.576573,-5.981757,-8.020965,8.909415,-9.729899,9.345197,5.783872,-1.405028,9.507734,-7.303811,-5.823826,-8.052691,-4.389527,3.691815,-6.378207,-2.422113,9.388249,3.512794,6.785821,4.790356,2.116477,-3.124993,-5.608948,-1.730970,1.645951,-7.968219,-8.988101,-1.663012,7.877901,9.054491,-6.833836,-3.433370,-8.349075,4.858486,-0.616017,-9.566671,-4.233846,-3.739677,3.066556,-8.091354,-3.318781,-4.889460,5.212306,0.358764,-1.367961,-9.278674,-5.089789,6.830979,-5.382513,-4.779068,0.444689,-5.088060,-1.342376,-6.690867,-8.984236,-1.558034,4.000894,4.796588,9.966814,1.179162,5.514163,-4.397328,-4.138083,7.519697,-2.086044,-6.688843,-9.044716,7.675652,0.022008,-4.368971,-3.880174,-7.532961,8.732053,-4.945108,9.015442,-8.054993,-6.900870,-0.544303,-4.506137,5.148557,-3.954634,1.046184,5.675927,9.742770,-4.452528,-4.583941,-4.888350,2.067802,-7.820664,-3.254215,6.039447,5.679554,3.119111,0.407411,1.591297,-8.996060,-1.532155,-4.620403,5.040935,-6.840119,0.418197,-7.379579,-3.935239,1.630384,-6.757274,-3.065969,-1.804673,1.056213,2.689487,-6.643036,1.530664,-4.690563,-6.212035,9.218964,-5.820889,2.644909,-7.317840,0.488221,6.884067,-1.809904,-8.328143,-7.140325,-7.174682,-7.625780,-8.979038,-3.864943,-7.100856,0.135438,1.975744,-9.668820,-2.547417,4.066543,0.638160,6.535396,5.636326,-9.037346,-5.614270,-9.407927,-0.390709,6.322391,7.349186,4.116847,-8.986273,-9.366907,1.080610,-2.510144,6.331771,5.151610,-1.049473,2.740779,-2.859928,-0.412367,-7.726783,0.083387,7.464288,2.928454,-1.863577,-9.815802,8.161311,-2.037578,9.711038,8.213943,-2.500170,-1.918135,5.856489,-3.281057,3.407171,3.302061,4.818920,0.401245,6.433040,-4.041389], dtype = "float32")#candidate|8929|(640,)|const|float32
call_8927 = relay.TupleGetItem(func_6887_call(relay.reshape(var_8928.astype('uint32'), [7, 56]), relay.reshape(const_8929.astype('float32'), [640,]), ), 5)
call_8930 = relay.TupleGetItem(func_6890_call(relay.reshape(var_8928.astype('uint32'), [7, 56]), relay.reshape(const_8929.astype('float32'), [640,]), ), 5)
func_839_call = mod.get_global_var('func_839')
func_841_call = mutated_mod.get_global_var('func_841')
var_8955 = relay.var("var_8955", dtype = "uint32", shape = (330,))#candidate|8955|(330,)|var|uint32
call_8954 = func_839_call(relay.reshape(var_8955.astype('uint32'), [2, 15, 11]))
call_8956 = func_839_call(relay.reshape(var_8955.astype('uint32'), [2, 15, 11]))
func_2832_call = mod.get_global_var('func_2832')
func_2834_call = mutated_mod.get_global_var('func_2834')
const_8965 = relay.const([4.517867,-9.750495,8.855329,3.628426,-0.433349,-2.890463,4.700776,-1.648787,-7.415625,7.680158,5.990045,2.703048,-7.239707,-2.056973,-0.550155,6.745960,-3.862830,5.341392,6.924777,-2.039713,6.587716,1.120857,4.527199,9.372881,-8.569795,7.572827,8.344978,-3.982584,-2.316581,-5.812753,5.448437,-1.834584,7.189687,4.182245,-2.583838,9.847703,6.769100,4.244733,-7.772346,-0.090923,6.981160,2.923330,-9.298739,-4.228410,-3.576694,-6.844628,6.769160,3.908704,-3.427744,2.680623,0.817094,-8.640380,8.424179,0.708581,-1.423295,6.932910,9.279181,6.627108,-9.440555,-5.861278,-2.201060,-1.856691,7.376320,-8.546033,1.388085,3.677127,-5.037574,3.442951,5.352989,-1.426240,-4.135130,8.590489,-7.019650,-2.576937,8.484342,4.684835,2.398596,3.097950,-5.556603,-8.521866,4.963949,-1.354381,3.275213,-2.579427,-5.951897,7.504510,-0.162807,-0.352878,6.769730,2.081618,7.691247,-8.111320,3.307024,7.633870,6.170255,5.475197,1.057120,7.445041,2.704417,8.887601,-9.890035,-6.825006,-3.100588,9.696241,1.710590,-6.008583,1.697670,2.739453,-6.006305,-7.658598,-2.393728,-6.448219,9.914515,9.201113,7.549131,-9.063618,8.855195,-2.912019,1.465227,9.782626,8.890762,6.881644,-6.089580,6.713349,-8.880849,-7.322651,7.740458,-8.994593,-6.500412,3.412657,3.537094,9.451090,-2.673611,-4.935526,4.726874,1.253724,7.441505,-3.534659,1.266038,-6.290450,6.691153,0.618446,6.707921,-7.926444,9.494267,-1.147709,5.062678,0.528298,9.409124,-6.113229,0.118506,5.794436,-3.749772,-7.779458,1.252919,7.190280,6.205167,1.921362,9.398360,3.602547,9.207592,4.774794,6.896209,4.937845,-2.666362,-3.850292,4.439796,-7.464094], dtype = "float32")#candidate|8965|(168,)|const|float32
call_8964 = relay.TupleGetItem(func_2832_call(relay.reshape(const_8965.astype('float32'), [168,])), 2)
call_8966 = relay.TupleGetItem(func_2834_call(relay.reshape(const_8965.astype('float32'), [168,])), 2)
var_8971 = relay.var("var_8971", dtype = "uint32", shape = (392, 2))#candidate|8971|(392, 2)|var|uint32
bop_8972 = relay.maximum(var_8928.astype('int32'), var_8971.astype('int32')) # shape=(392, 2)
uop_8978 = relay.asinh(call_8919.astype('float64')) # shape=(11, 11, 7)
uop_8980 = relay.asinh(call_8920.astype('float64')) # shape=(11, 11, 7)
uop_8996 = relay.cos(bop_8972.astype('float32')) # shape=(392, 2)
output = relay.Tuple([call_8927,const_8929,call_8954,var_8955,call_8964,const_8965,uop_8978,uop_8996,])
output2 = relay.Tuple([call_8930,const_8929,call_8956,var_8955,call_8966,const_8965,uop_8980,uop_8996,])
F = relay.Function([var_8928,var_8955,var_8971,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8928,var_8955,var_8971,], output2)
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
