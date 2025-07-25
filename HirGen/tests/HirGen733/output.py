import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_210 = relay.var("var_210", dtype = "float32", shape = (2, 15, 13))#candidate|210|(2, 15, 13)|var|float32
var_211 = relay.var("var_211", dtype = "float32", shape = (2, 15, 13))#candidate|211|(2, 15, 13)|var|float32
bop_212 = relay.floor_divide(var_210.astype('float32'), relay.reshape(var_211.astype('float32'), relay.shape_of(var_210))) # shape=(2, 15, 13)
output = relay.Tuple([bop_212,])
output2 = relay.Tuple([bop_212,])
func_220 = relay.Function([var_210,var_211,], output)
mod['func_220'] = func_220
mod = relay.transform.InferType()(mod)
mutated_mod['func_220'] = func_220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_220_call = mutated_mod.get_global_var('func_220')
var_222 = relay.var("var_222", dtype = "float32", shape = (2, 15, 13))#candidate|222|(2, 15, 13)|var|float32
var_223 = relay.var("var_223", dtype = "float32", shape = (2, 15, 13))#candidate|223|(2, 15, 13)|var|float32
call_221 = func_220_call(var_222,var_223,)
output = call_221
func_224 = relay.Function([var_222,var_223,], output)
mutated_mod['func_224'] = func_224
mutated_mod = relay.transform.InferType()(mutated_mod)
var_270 = relay.var("var_270", dtype = "float64", shape = (10, 8, 1))#candidate|270|(10, 8, 1)|var|float64
uop_271 = relay.log10(var_270.astype('float64')) # shape=(10, 8, 1)
output = relay.Tuple([uop_271,])
output2 = relay.Tuple([uop_271,])
func_299 = relay.Function([var_270,], output)
mod['func_299'] = func_299
mod = relay.transform.InferType()(mod)
var_300 = relay.var("var_300", dtype = "float64", shape = (10, 8, 1))#candidate|300|(10, 8, 1)|var|float64
output = func_299(var_300)
func_301 = relay.Function([var_300], output)
mutated_mod['func_301'] = func_301
mutated_mod = relay.transform.InferType()(mutated_mod)
var_833 = relay.var("var_833", dtype = "float64", shape = (15, 6, 2))#candidate|833|(15, 6, 2)|var|float64
uop_834 = relay.cosh(var_833.astype('float64')) # shape=(15, 6, 2)
func_220_call = mod.get_global_var('func_220')
func_224_call = mutated_mod.get_global_var('func_224')
var_852 = relay.var("var_852", dtype = "float32", shape = (390,))#candidate|852|(390,)|var|float32
call_851 = relay.TupleGetItem(func_220_call(relay.reshape(var_852.astype('float32'), [2, 15, 13]), relay.reshape(var_852.astype('float32'), [2, 15, 13]), ), 0)
call_853 = relay.TupleGetItem(func_224_call(relay.reshape(var_852.astype('float32'), [2, 15, 13]), relay.reshape(var_852.astype('float32'), [2, 15, 13]), ), 0)
uop_854 = relay.sigmoid(var_833.astype('float32')) # shape=(15, 6, 2)
func_299_call = mod.get_global_var('func_299')
func_301_call = mutated_mod.get_global_var('func_301')
var_857 = relay.var("var_857", dtype = "float64", shape = (20, 4))#candidate|857|(20, 4)|var|float64
call_856 = relay.TupleGetItem(func_299_call(relay.reshape(var_857.astype('float64'), [10, 8, 1])), 0)
call_858 = relay.TupleGetItem(func_301_call(relay.reshape(var_857.astype('float64'), [10, 8, 1])), 0)
uop_864 = relay.cosh(call_856.astype('float64')) # shape=(10, 8, 1)
uop_866 = relay.cosh(call_858.astype('float64')) # shape=(10, 8, 1)
bop_881 = relay.maximum(uop_854.astype('uint16'), relay.reshape(uop_834.astype('uint16'), relay.shape_of(uop_854))) # shape=(15, 6, 2)
func_299_call = mod.get_global_var('func_299')
func_301_call = mutated_mod.get_global_var('func_301')
call_885 = relay.TupleGetItem(func_299_call(relay.reshape(call_856.astype('float64'), [10, 8, 1])), 0)
call_886 = relay.TupleGetItem(func_301_call(relay.reshape(call_856.astype('float64'), [10, 8, 1])), 0)
output = relay.Tuple([call_851,var_852,var_857,uop_864,bop_881,call_885,])
output2 = relay.Tuple([call_853,var_852,var_857,uop_866,bop_881,call_886,])
func_894 = relay.Function([var_833,var_852,var_857,], output)
mod['func_894'] = func_894
mod = relay.transform.InferType()(mod)
var_895 = relay.var("var_895", dtype = "float64", shape = (15, 6, 2))#candidate|895|(15, 6, 2)|var|float64
var_896 = relay.var("var_896", dtype = "float32", shape = (390,))#candidate|896|(390,)|var|float32
var_897 = relay.var("var_897", dtype = "float64", shape = (20, 4))#candidate|897|(20, 4)|var|float64
output = func_894(var_895,var_896,var_897,)
func_898 = relay.Function([var_895,var_896,var_897,], output)
mutated_mod['func_898'] = func_898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_974 = relay.var("var_974", dtype = "int16", shape = (14, 12, 1))#candidate|974|(14, 12, 1)|var|int16
var_975 = relay.var("var_975", dtype = "int16", shape = (14, 12, 1))#candidate|975|(14, 12, 1)|var|int16
bop_976 = relay.bitwise_and(var_974.astype('int16'), relay.reshape(var_975.astype('int16'), relay.shape_of(var_974))) # shape=(14, 12, 1)
bop_992 = relay.logical_or(bop_976.astype('bool'), relay.reshape(var_975.astype('bool'), relay.shape_of(bop_976))) # shape=(14, 12, 1)
func_220_call = mod.get_global_var('func_220')
func_224_call = mutated_mod.get_global_var('func_224')
var_1005 = relay.var("var_1005", dtype = "float32", shape = (390, 1))#candidate|1005|(390, 1)|var|float32
call_1004 = relay.TupleGetItem(func_220_call(relay.reshape(var_1005.astype('float32'), [2, 15, 13]), relay.reshape(var_1005.astype('float32'), [2, 15, 13]), ), 0)
call_1006 = relay.TupleGetItem(func_224_call(relay.reshape(var_1005.astype('float32'), [2, 15, 13]), relay.reshape(var_1005.astype('float32'), [2, 15, 13]), ), 0)
func_894_call = mod.get_global_var('func_894')
func_898_call = mutated_mod.get_global_var('func_898')
var_1011 = relay.var("var_1011", dtype = "float64", shape = (180,))#candidate|1011|(180,)|var|float64
const_1012 = relay.const([3.304116,-8.835699,1.128469,-1.872425,9.754731,0.219701,8.504097,7.117917,-5.436182,7.347234,3.452764,9.296452,-0.281607,-4.022451,0.953318,6.236503,6.150369,6.380543,-0.062004,-0.238329,-8.643876,2.978739,0.071156,1.701821,-1.058005,1.695657,-8.936710,-2.234354,8.817703,2.172797,0.402867,0.348156,-2.468274,8.640108,-6.849122,-0.068270,-4.886195,-9.720246,-8.898399,2.243593,-3.988393,-6.761943,1.254867,5.370479,-4.568505,3.748661,7.384022,-0.960148,-8.347995,-7.352482,3.896875,4.591838,-5.597117,-2.190964,-8.886380,7.728646,-4.563969,1.766285,9.154466,-8.519794,8.382235,4.245265,-3.736228,-8.194098,-5.591340,8.884115,2.656333,3.920793,-1.526355,-6.518866,4.355124,6.360187,-5.305850,6.021116,4.174504,3.395370,1.089472,9.114570,-1.785946,-2.216108], dtype = "float64")#candidate|1012|(80,)|const|float64
call_1010 = relay.TupleGetItem(func_894_call(relay.reshape(var_1011.astype('float64'), [15, 6, 2]), relay.reshape(var_1005.astype('float32'), [390,]), relay.reshape(const_1012.astype('float64'), [20, 4]), ), 3)
call_1013 = relay.TupleGetItem(func_898_call(relay.reshape(var_1011.astype('float64'), [15, 6, 2]), relay.reshape(var_1005.astype('float32'), [390,]), relay.reshape(const_1012.astype('float64'), [20, 4]), ), 3)
bop_1020 = relay.divide(var_1011.astype('float64'), var_1005.astype('float64')) # shape=(390, 180)
output = relay.Tuple([bop_992,call_1004,call_1010,const_1012,bop_1020,])
output2 = relay.Tuple([bop_992,call_1006,call_1013,const_1012,bop_1020,])
func_1033 = relay.Function([var_974,var_975,var_1005,var_1011,], output)
mod['func_1033'] = func_1033
mod = relay.transform.InferType()(mod)
var_1034 = relay.var("var_1034", dtype = "int16", shape = (14, 12, 1))#candidate|1034|(14, 12, 1)|var|int16
var_1035 = relay.var("var_1035", dtype = "int16", shape = (14, 12, 1))#candidate|1035|(14, 12, 1)|var|int16
var_1036 = relay.var("var_1036", dtype = "float32", shape = (390, 1))#candidate|1036|(390, 1)|var|float32
var_1037 = relay.var("var_1037", dtype = "float64", shape = (180,))#candidate|1037|(180,)|var|float64
output = func_1033(var_1034,var_1035,var_1036,var_1037,)
func_1038 = relay.Function([var_1034,var_1035,var_1036,var_1037,], output)
mutated_mod['func_1038'] = func_1038
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1059 = relay.var("var_1059", dtype = "int32", shape = (15, 4, 11))#candidate|1059|(15, 4, 11)|var|int32
const_1060 = relay.const([[[10,2,10,9,2,-7,3,-9,-8,10,-3],[10,-2,9,6,5,-8,10,-10,-3,3,1],[2,4,-9,7,-1,-5,5,10,10,7,-2],[-7,-10,-7,8,8,7,9,4,9,5,8]],[[-10,3,-4,9,1,-8,-6,-5,-2,4,5],[-7,-1,4,-2,8,-1,-1,3,-10,-6,7],[-3,6,-5,7,6,-7,-2,-5,-5,6,5],[-10,-9,-5,9,9,-4,7,7,-7,8,2]],[[-9,4,-1,10,8,-8,-8,-4,-7,-9,7],[-2,10,9,-5,7,9,8,2,8,5,6],[3,2,-4,2,-7,-8,-6,-4,-8,-5,-2],[9,-8,-3,4,-8,-3,6,-1,9,-5,-4]],[[3,-9,1,-10,-8,9,5,-1,-3,-6,1],[-4,-2,-10,-1,5,-4,-5,-2,-10,-3,6],[-10,6,10,-2,4,3,10,-3,10,4,-4],[-7,-5,7,-5,-3,4,10,1,-6,9,-5]],[[5,-9,5,6,-2,8,-9,5,-9,-9,-10],[-8,-3,10,-4,-3,10,-1,-5,8,10,-5],[2,3,10,6,-2,-1,-9,-9,3,-1,5],[-1,8,10,-7,7,6,-3,-3,-4,-5,2]],[[-7,8,-6,-6,8,-1,-7,4,-5,3,2],[-6,7,10,9,8,4,8,5,-10,9,9],[2,10,-6,-9,-1,1,-8,-3,-4,5,-9],[9,6,6,3,-3,-1,-2,-8,-3,-7,8]],[[-9,2,-2,-3,-9,2,4,-1,3,3,7],[-1,8,3,-10,3,-1,-5,2,-1,-2,6],[-3,6,3,10,-5,-6,-4,-8,-1,6,-6],[5,10,-10,-3,2,-5,1,-6,-9,-3,1]],[[5,4,10,10,-2,3,2,-4,-2,-10,5],[-7,2,9,3,5,-1,6,10,9,-10,3],[6,7,-6,-6,-8,-1,1,8,-1,-1,-9],[-8,-4,2,-9,-6,-4,4,-1,10,-3,10]],[[2,7,-8,-8,9,7,-2,7,-3,8,-7],[-9,3,6,10,-10,-3,-8,9,-9,3,-10],[-4,-8,-10,-6,9,5,-5,-7,-6,-9,-8],[-1,2,-3,-5,-2,10,8,6,-8,9,6]],[[4,-1,2,1,-7,-7,2,6,5,-4,7],[6,6,-6,-7,1,6,6,-3,10,-9,1],[-8,-9,-4,-9,-5,-2,-1,7,1,-1,-9],[-6,4,-4,-4,-6,-3,-7,-8,-8,3,7]],[[10,-4,-2,-9,4,5,3,4,-6,4,-5],[-6,9,-7,4,8,8,7,9,-2,3,-2],[1,-8,6,4,-2,4,4,4,3,-4,-4],[-10,-6,7,-4,-8,4,-9,7,-10,6,8]],[[5,-10,4,9,4,10,-6,1,-5,-2,-6],[-7,-8,2,3,6,2,6,1,-1,-9,-8],[7,4,10,-10,8,-1,-4,-2,3,-5,-5],[8,-10,-4,-1,5,-2,1,-4,-10,8,-1]],[[-4,-1,1,1,-1,-4,9,2,-8,1,6],[6,3,-6,-9,5,-8,-2,4,-4,2,6],[6,3,-6,8,6,-4,9,-10,-5,-4,3],[5,-9,2,9,-3,7,10,10,-5,-9,-5]],[[-9,9,-4,-10,-8,2,-3,9,2,6,-9],[3,2,8,-7,2,-2,1,-3,-10,-3,8],[-9,-8,10,2,-10,-9,-3,6,1,-7,10],[-6,-8,-5,1,8,2,-2,-10,2,-9,4]],[[9,5,1,-3,-9,-5,-7,7,8,9,1],[-2,6,-3,-4,-9,9,3,6,-1,6,2],[-10,1,-4,6,2,6,-2,2,-6,-1,7],[-2,-1,-7,-1,-8,8,9,-10,5,2,9]]], dtype = "int32")#candidate|1060|(15, 4, 11)|const|int32
bop_1061 = relay.multiply(var_1059.astype('int32'), relay.reshape(const_1060.astype('int32'), relay.shape_of(var_1059))) # shape=(15, 4, 11)
output = bop_1061
output2 = bop_1061
func_1070 = relay.Function([var_1059,], output)
mod['func_1070'] = func_1070
mod = relay.transform.InferType()(mod)
mutated_mod['func_1070'] = func_1070
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1071 = relay.var("var_1071", dtype = "int32", shape = (15, 4, 11))#candidate|1071|(15, 4, 11)|var|int32
func_1070_call = mutated_mod.get_global_var('func_1070')
call_1072 = func_1070_call(var_1071)
output = call_1072
func_1073 = relay.Function([var_1071], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1333 = relay.var("var_1333", dtype = "float32", shape = (6, 11, 7))#candidate|1333|(6, 11, 7)|var|float32
uop_1334 = relay.rsqrt(var_1333.astype('float32')) # shape=(6, 11, 7)
var_1339 = relay.var("var_1339", dtype = "float32", shape = (6, 11, 7))#candidate|1339|(6, 11, 7)|var|float32
bop_1340 = relay.greater(uop_1334.astype('bool'), relay.reshape(var_1339.astype('bool'), relay.shape_of(uop_1334))) # shape=(6, 11, 7)
uop_1343 = relay.acos(bop_1340.astype('float64')) # shape=(6, 11, 7)
output = uop_1343
output2 = uop_1343
func_1356 = relay.Function([var_1333,var_1339,], output)
mod['func_1356'] = func_1356
mod = relay.transform.InferType()(mod)
var_1357 = relay.var("var_1357", dtype = "float32", shape = (6, 11, 7))#candidate|1357|(6, 11, 7)|var|float32
var_1358 = relay.var("var_1358", dtype = "float32", shape = (6, 11, 7))#candidate|1358|(6, 11, 7)|var|float32
output = func_1356(var_1357,var_1358,)
func_1359 = relay.Function([var_1357,var_1358,], output)
mutated_mod['func_1359'] = func_1359
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1477 = relay.const(9, dtype = "uint8")#candidate|1477|()|const|uint8
var_1478 = relay.var("var_1478", dtype = "uint8", shape = (4, 10, 5))#candidate|1478|(4, 10, 5)|var|uint8
bop_1479 = relay.minimum(const_1477.astype('uint8'), var_1478.astype('uint8')) # shape=(4, 10, 5)
output = relay.Tuple([bop_1479,])
output2 = relay.Tuple([bop_1479,])
func_1492 = relay.Function([var_1478,], output)
mod['func_1492'] = func_1492
mod = relay.transform.InferType()(mod)
mutated_mod['func_1492'] = func_1492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1493 = relay.var("var_1493", dtype = "uint8", shape = (4, 10, 5))#candidate|1493|(4, 10, 5)|var|uint8
func_1492_call = mutated_mod.get_global_var('func_1492')
call_1494 = func_1492_call(var_1493)
output = call_1494
func_1495 = relay.Function([var_1493], output)
mutated_mod['func_1495'] = func_1495
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2077 = relay.var("var_2077", dtype = "int8", shape = ())#candidate|2077|()|var|int8
var_2078 = relay.var("var_2078", dtype = "int8", shape = (4, 5, 2))#candidate|2078|(4, 5, 2)|var|int8
bop_2079 = relay.less(var_2077.astype('bool'), var_2078.astype('bool')) # shape=(4, 5, 2)
output = bop_2079
output2 = bop_2079
func_2085 = relay.Function([var_2077,var_2078,], output)
mod['func_2085'] = func_2085
mod = relay.transform.InferType()(mod)
mutated_mod['func_2085'] = func_2085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2085_call = mutated_mod.get_global_var('func_2085')
var_2087 = relay.var("var_2087", dtype = "int8", shape = ())#candidate|2087|()|var|int8
var_2088 = relay.var("var_2088", dtype = "int8", shape = (4, 5, 2))#candidate|2088|(4, 5, 2)|var|int8
call_2086 = func_2085_call(var_2087,var_2088,)
output = call_2086
func_2089 = relay.Function([var_2087,var_2088,], output)
mutated_mod['func_2089'] = func_2089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2652 = relay.var("var_2652", dtype = "float32", shape = (1, 10, 12))#candidate|2652|(1, 10, 12)|var|float32
var_2653 = relay.var("var_2653", dtype = "float32", shape = (15, 10, 12))#candidate|2653|(15, 10, 12)|var|float32
bop_2654 = relay.not_equal(var_2652.astype('bool'), var_2653.astype('bool')) # shape=(15, 10, 12)
func_1033_call = mod.get_global_var('func_1033')
func_1038_call = mutated_mod.get_global_var('func_1038')
const_2661 = relay.const([8,-4,4,2,6,9,8,2,9,-7,-3,6,-10,3,8,1,-3,-10,-5,-3,6,8,6,-6,-5,-1,-3,-8,-7,-7,6,-10,-5,7,3,-10,-2,5,-8,4,-5,2,2,-2,-10,4,9,6,-4,-3,-3,-10,-1,4,7,5,-2,9,-6,3,-10,-1,-10,-2,-9,5,-7,-6,1,10,-9,9,1,-3,1,-2,-2,-9,-9,9,5,10,1,2,10,-10,-4,-8,9,1,-7,10,-7,2,-9,6,6,-7,5,-1,-1,4,1,2,3,-9,-10,2,7,5,-6,3,-8,3,2,-8,4,-10,-4,-5,8,9,-3,5,-4,10,-3,6,-5,-7,-10,10,9,-8,-4,1,-7,8,-1,3,-5,-7,-6,-10,-1,-8,3,4,-9,6,5,5,-8,-3,-6,-6,1,-9,-8,8,7,-10,-7,2,-9,9,-6,6], dtype = "int16")#candidate|2661|(168,)|const|int16
var_2662 = relay.var("var_2662", dtype = "float32", shape = (195, 2))#candidate|2662|(195, 2)|var|float32
const_2663 = relay.const([-2.325955,-7.808790,-8.959223,-7.991818,9.469217,5.701836,-1.484950,-0.382568,0.655124,-4.291704,-3.296799,4.688645,5.795138,-8.741172,-1.096648,5.895063,5.978461,-8.864814,-3.505892,2.984401,-3.019794,4.291303,-4.522889,6.592446,1.515691,2.249590,2.192035,-2.172363,-3.959545,7.237721,0.739174,7.903322,-5.130818,-3.740618,7.203025,9.719232,6.515315,-0.730724,-0.107156,0.746595,4.969214,-2.673430,2.495764,-0.436329,3.533234,-1.084615,-8.932836,6.094562,4.314538,5.307311,-8.031988,0.311572,5.606000,8.247474,2.604061,5.315311,0.041924,1.377769,-1.818673,3.316718,-2.943271,0.427201,9.480721,9.557458,-7.102157,3.470309,3.172164,-5.979560,-2.633851,9.525082,6.134308,6.469172,-7.318338,4.375626,-4.713693,-4.667471,4.115261,7.750793,2.529872,0.711207,3.231371,-2.960666,6.059226,7.095157,-5.892308,-8.840228,8.831612,0.852756,-8.011210,-5.786560,5.182381,6.780678,-2.451507,7.080368,-7.951400,-8.531088,-1.383416,-3.356774,3.323774,1.251089,-8.873212,6.836269,3.435010,9.782756,-1.914179,-0.889619,2.088653,-2.786616,-9.675457,5.480535,-9.734784,-5.897708,-2.149015,8.103065,-2.374057,1.961315,-2.749200,-6.239365,4.834391,2.308499,-4.381248,6.956834,-7.944045,1.549896,-8.529853,9.734820,-7.800502,3.246414,-3.801885,4.077210,5.381761,-1.349370,3.896215,-4.599297,-9.119267,-9.758716,8.914350,-7.814672,2.947191,8.397970,-3.443291,9.167240,-9.545365,9.534373,5.312779,-1.763980,-0.875637,-2.575672,8.081197,-8.324376,-2.813507,-4.995988,7.306366,8.145059,5.129975,-2.333526,5.546800,-6.086691,-6.710397,0.286927,-2.105084,-1.025075,-8.232038,1.748977,5.247777,7.350218,-7.955433,-7.212730,2.556122,1.493156,-0.046801,-8.668575,2.050939,1.212553,3.890049,1.443257,-3.205482,-5.933551,-4.049926,5.375155], dtype = "float64")#candidate|2663|(180,)|const|float64
call_2660 = relay.TupleGetItem(func_1033_call(relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(var_2662.astype('float32'), [390, 1]), relay.reshape(const_2663.astype('float64'), [180,]), ), 1)
call_2664 = relay.TupleGetItem(func_1038_call(relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(var_2662.astype('float32'), [390, 1]), relay.reshape(const_2663.astype('float64'), [180,]), ), 1)
func_1033_call = mod.get_global_var('func_1033')
func_1038_call = mutated_mod.get_global_var('func_1038')
call_2667 = relay.TupleGetItem(func_1033_call(relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(var_2662.astype('float32'), [390, 1]), relay.reshape(const_2663.astype('float64'), [180,]), ), 1)
call_2668 = relay.TupleGetItem(func_1038_call(relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(const_2661.astype('int16'), [14, 12, 1]), relay.reshape(var_2662.astype('float32'), [390, 1]), relay.reshape(const_2663.astype('float64'), [180,]), ), 1)
output = relay.Tuple([bop_2654,call_2660,const_2661,var_2662,const_2663,call_2667,])
output2 = relay.Tuple([bop_2654,call_2664,const_2661,var_2662,const_2663,call_2668,])
func_2669 = relay.Function([var_2652,var_2653,var_2662,], output)
mod['func_2669'] = func_2669
mod = relay.transform.InferType()(mod)
mutated_mod['func_2669'] = func_2669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2669_call = mutated_mod.get_global_var('func_2669')
var_2671 = relay.var("var_2671", dtype = "float32", shape = (1, 10, 12))#candidate|2671|(1, 10, 12)|var|float32
var_2672 = relay.var("var_2672", dtype = "float32", shape = (15, 10, 12))#candidate|2672|(15, 10, 12)|var|float32
var_2673 = relay.var("var_2673", dtype = "float32", shape = (195, 2))#candidate|2673|(195, 2)|var|float32
call_2670 = func_2669_call(var_2671,var_2672,var_2673,)
output = call_2670
func_2674 = relay.Function([var_2671,var_2672,var_2673,], output)
mutated_mod['func_2674'] = func_2674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2784 = relay.var("var_2784", dtype = "float32", shape = (11, 13, 16))#candidate|2784|(11, 13, 16)|var|float32
uop_2785 = relay.erf(var_2784.astype('float32')) # shape=(11, 13, 16)
func_1492_call = mod.get_global_var('func_1492')
func_1495_call = mutated_mod.get_global_var('func_1495')
const_2793 = relay.const([-4,-5,7,-4,-8,-2,10,-6,-10,8,-8,10,-9,10,-3,-4,-1,8,10,6,10,10,9,-10,-10,2,-7,-7,-9,-2,9,9,-4,7,-8,-1,-2,10,-6,2,-3,5,9,8,-10,-2,8,-8,-10,-4,7,9,-6,-3,-1,2,1,6,9,10,6,-10,-3,5,-3,-10,-6,-4,-7,-7,-3,-4,4,6,6,3,-6,-6,-1,-10,2,7,-10,2,-9,10,10,6,-6,9,8,5,7,3,-4,4,-7,-6,1,6,9,-2,10,2,2,-1,5,4,-9,10,4,-1,-5,7,7,8,9,-4,9,6,-9,-2,3,6,5,-5,-8,-9,3,10,9,-5,-9,-7,5,10,2,-10,-7,7,10,2,-10,4,-5,3,-4,2,7,2,5,-8,1,2,-4,-2,2,-4,-3,8,-3,-3,1,-10,3,2,3,4,10,4,6,-8,-9,3,-3,3,-3,-4,-10,-3,-8,2,7,-5,-4,10,-4,10,-3,7,-5,-3,-5,-3,3,7,-2,-3,6,5], dtype = "uint8")#candidate|2793|(200,)|const|uint8
call_2792 = relay.TupleGetItem(func_1492_call(relay.reshape(const_2793.astype('uint8'), [4, 10, 5])), 0)
call_2794 = relay.TupleGetItem(func_1495_call(relay.reshape(const_2793.astype('uint8'), [4, 10, 5])), 0)
output = relay.Tuple([uop_2785,call_2792,const_2793,])
output2 = relay.Tuple([uop_2785,call_2794,const_2793,])
func_2795 = relay.Function([var_2784,], output)
mod['func_2795'] = func_2795
mod = relay.transform.InferType()(mod)
mutated_mod['func_2795'] = func_2795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2796 = relay.var("var_2796", dtype = "float32", shape = (11, 13, 16))#candidate|2796|(11, 13, 16)|var|float32
func_2795_call = mutated_mod.get_global_var('func_2795')
call_2797 = func_2795_call(var_2796)
output = call_2797
func_2798 = relay.Function([var_2796], output)
mutated_mod['func_2798'] = func_2798
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2819 = relay.var("var_2819", dtype = "float32", shape = (1, 10, 16))#candidate|2819|(1, 10, 16)|var|float32
uop_2820 = relay.sigmoid(var_2819.astype('float32')) # shape=(1, 10, 16)
bop_2823 = relay.logical_or(uop_2820.astype('bool'), relay.reshape(var_2819.astype('bool'), relay.shape_of(uop_2820))) # shape=(1, 10, 16)
output = relay.Tuple([bop_2823,])
output2 = relay.Tuple([bop_2823,])
func_2828 = relay.Function([var_2819,], output)
mod['func_2828'] = func_2828
mod = relay.transform.InferType()(mod)
mutated_mod['func_2828'] = func_2828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2829 = relay.var("var_2829", dtype = "float32", shape = (1, 10, 16))#candidate|2829|(1, 10, 16)|var|float32
func_2828_call = mutated_mod.get_global_var('func_2828')
call_2830 = func_2828_call(var_2829)
output = call_2830
func_2831 = relay.Function([var_2829], output)
mutated_mod['func_2831'] = func_2831
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3453 = relay.var("var_3453", dtype = "float32", shape = (7, 1, 5))#candidate|3453|(7, 1, 5)|var|float32
uop_3454 = relay.sigmoid(var_3453.astype('float32')) # shape=(7, 1, 5)
output = uop_3454
output2 = uop_3454
func_3456 = relay.Function([var_3453,], output)
mod['func_3456'] = func_3456
mod = relay.transform.InferType()(mod)
var_3457 = relay.var("var_3457", dtype = "float32", shape = (7, 1, 5))#candidate|3457|(7, 1, 5)|var|float32
output = func_3456(var_3457)
func_3458 = relay.Function([var_3457], output)
mutated_mod['func_3458'] = func_3458
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3777 = relay.var("var_3777", dtype = "float32", shape = (13, 7, 3))#candidate|3777|(13, 7, 3)|var|float32
uop_3778 = relay.sigmoid(var_3777.astype('float32')) # shape=(13, 7, 3)
bop_3789 = relay.not_equal(var_3777.astype('bool'), relay.reshape(uop_3778.astype('bool'), relay.shape_of(var_3777))) # shape=(13, 7, 3)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
var_3808 = relay.var("var_3808", dtype = "float32", shape = (1, 462))#candidate|3808|(1, 462)|var|float32
call_3807 = func_1356_call(relay.reshape(var_3808.astype('float32'), [6, 11, 7]), relay.reshape(var_3808.astype('float32'), [6, 11, 7]), )
call_3809 = func_1356_call(relay.reshape(var_3808.astype('float32'), [6, 11, 7]), relay.reshape(var_3808.astype('float32'), [6, 11, 7]), )
func_220_call = mod.get_global_var('func_220')
func_224_call = mutated_mod.get_global_var('func_224')
const_3811 = relay.const([[0.621834,-1.756403,8.547681,7.777504,5.721792,4.483538,-8.430312,-6.309703,7.780281,-6.728107,1.392923,4.643360,-5.610391,-1.106613,-3.545685,4.474328,-5.134592,9.897815,4.176686,-5.090399,-3.018799,-5.165774,8.043292,1.380816,9.165446,-7.835410,8.192744,6.745600,-6.799797,-1.218667,-2.299242,2.051061,5.558041,3.627585,5.421324,-7.496163,1.806624,-0.408492,9.939967,2.840585,0.008195,6.807966,7.500716,-8.398907,-8.915919,1.957119,9.375959,7.586141,9.989319,9.641689,9.449910,-4.450236,0.570474,1.734326,-3.242492,9.368615,-3.965660,-9.634208,-4.777835,-7.612961,8.242131,2.784941,-9.045131,2.526933,7.225822,-3.627872,-6.851407,5.867342,-7.308432,-7.382731,-7.881519,-0.744546,3.080489,-0.411363,-1.524526,-6.519643,-5.335215,-3.841624],[4.043352,-1.631215,-1.802858,0.177038,1.732940,-9.433919,4.339972,-9.472378,5.577555,2.445459,6.193012,-5.556812,-5.714302,9.862704,-7.459084,0.043585,-3.624650,9.966392,-7.186760,3.786712,0.516785,2.697669,0.959935,-4.704080,1.919201,9.778334,-0.463190,-6.966680,-8.062491,6.101345,9.480485,-5.467974,0.016585,-4.008298,-1.465478,1.433582,-2.900750,6.897903,0.049553,-9.126195,0.565953,5.065186,7.078080,-9.921433,-1.694255,-8.563958,-5.886018,2.317198,-0.834266,2.734231,6.971684,9.698770,-6.280779,1.252313,-7.640100,-9.050974,2.611613,1.739598,7.446774,2.042995,-4.643509,8.416544,-1.624353,-7.623166,-9.276451,-8.182427,-4.482162,9.266647,-5.936854,-0.529462,-9.169423,-7.091637,4.329448,-8.811272,3.850873,-3.449049,-7.860538,-8.690572],[-1.403434,4.947533,-9.531562,-7.847634,6.155670,3.112158,4.749057,2.063942,-8.581260,5.732438,2.880984,-8.044449,4.527294,-1.949720,-9.708099,1.821328,0.652117,-3.201896,-9.499775,4.934058,-4.814349,6.682100,-7.590367,-5.098915,-5.842007,-5.723569,7.186033,-4.758773,7.418363,-0.633152,0.145405,-5.290194,8.512610,-7.005795,-3.672672,8.603413,5.257864,-5.614743,5.765672,-1.766511,-2.292342,-9.956627,-9.398006,7.918664,6.440884,7.131730,1.284560,-5.056758,-2.738871,-9.065451,-3.140648,-1.095203,-9.471949,5.634850,8.415962,1.887596,8.789078,9.379286,-1.472890,6.382817,6.241872,-9.409786,2.227253,9.853786,0.592479,-1.454475,1.291375,4.267806,3.846596,-3.261113,7.775678,-0.543636,3.428178,-7.907706,-9.850150,8.393786,-5.379872,-8.321765],[-5.167818,-1.438260,9.644042,9.752573,4.852562,-9.182423,-8.650153,0.753798,-9.937549,-9.412749,8.892612,9.279859,-7.359271,3.639811,-6.603978,-5.145140,4.379917,2.761828,3.159391,-9.851638,3.686139,1.353361,1.899572,5.308608,7.835443,1.819000,-3.386149,-8.689804,1.862926,-8.006934,-4.084910,5.644581,1.280738,-2.652479,8.553628,9.913539,-2.712286,-7.562668,9.736702,8.811237,4.984614,2.989091,-7.369700,8.654625,-5.342887,1.879194,-8.254800,-6.601635,2.210130,1.792260,1.131400,-1.330635,8.141418,4.621723,-3.734179,3.004849,2.574515,-7.999603,1.895417,-1.520444,5.571274,-5.497971,-7.465732,0.737983,6.971363,-6.085834,2.059997,-7.938137,-6.827383,0.908330,3.851265,-5.202799,2.349481,-0.326686,-2.003773,-7.819286,-1.011195,-9.538713],[-5.805901,6.631692,-3.377414,-5.843202,-9.594690,-4.313566,2.710525,0.452927,2.439266,2.929779,-2.832948,2.546933,-9.595659,-6.825856,-2.261828,9.175501,-1.143372,-1.078378,1.956908,-9.837397,-2.292393,-7.710083,-4.703746,-2.782300,7.812265,7.632122,8.371266,1.591380,-8.866311,-6.107486,-8.016488,6.430942,-6.096880,5.239805,9.646988,1.099298,-4.639597,0.129275,-7.223267,-1.271537,0.651940,3.766846,-3.099759,2.008659,8.397532,1.044159,0.429662,-2.617167,7.995186,7.459391,-3.718013,-2.116500,-2.556436,9.489835,6.984898,8.726901,6.209336,1.552152,8.896805,7.987212,-8.010811,-5.498357,9.492002,-0.867833,-5.588698,6.930801,-8.219421,2.386183,2.021114,4.355493,3.104413,-8.880552,-2.986519,-0.841293,-0.740818,-2.185480,4.946441,-2.018564]], dtype = "float32")#candidate|3811|(5, 78)|const|float32
call_3810 = relay.TupleGetItem(func_220_call(relay.reshape(const_3811.astype('float32'), [2, 15, 13]), relay.reshape(const_3811.astype('float32'), [2, 15, 13]), ), 0)
call_3812 = relay.TupleGetItem(func_224_call(relay.reshape(const_3811.astype('float32'), [2, 15, 13]), relay.reshape(const_3811.astype('float32'), [2, 15, 13]), ), 0)
func_894_call = mod.get_global_var('func_894')
func_898_call = mutated_mod.get_global_var('func_898')
var_3816 = relay.var("var_3816", dtype = "float64", shape = (180,))#candidate|3816|(180,)|var|float64
var_3817 = relay.var("var_3817", dtype = "float64", shape = (80,))#candidate|3817|(80,)|var|float64
call_3815 = relay.TupleGetItem(func_894_call(relay.reshape(var_3816.astype('float64'), [15, 6, 2]), relay.reshape(call_3810.astype('float32'), [390,]), relay.reshape(var_3817.astype('float64'), [20, 4]), ), 3)
call_3818 = relay.TupleGetItem(func_898_call(relay.reshape(var_3816.astype('float64'), [15, 6, 2]), relay.reshape(call_3810.astype('float32'), [390,]), relay.reshape(var_3817.astype('float64'), [20, 4]), ), 3)
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
var_3822 = relay.var("var_3822", dtype = "float32", shape = (35,))#candidate|3822|(35,)|var|float32
call_3821 = func_3456_call(relay.reshape(var_3822.astype('float32'), [7, 1, 5]))
call_3823 = func_3456_call(relay.reshape(var_3822.astype('float32'), [7, 1, 5]))
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
var_3825 = relay.var("var_3825", dtype = "float32", shape = (2288,))#candidate|3825|(2288,)|var|float32
call_3824 = relay.TupleGetItem(func_2795_call(relay.reshape(var_3825.astype('float32'), [11, 13, 16])), 0)
call_3826 = relay.TupleGetItem(func_2798_call(relay.reshape(var_3825.astype('float32'), [11, 13, 16])), 0)
output = relay.Tuple([bop_3789,call_3807,var_3808,call_3810,const_3811,call_3815,var_3816,var_3817,call_3821,var_3822,call_3824,var_3825,])
output2 = relay.Tuple([bop_3789,call_3809,var_3808,call_3812,const_3811,call_3818,var_3816,var_3817,call_3823,var_3822,call_3826,var_3825,])
func_3852 = relay.Function([var_3777,var_3808,var_3816,var_3817,var_3822,var_3825,], output)
mod['func_3852'] = func_3852
mod = relay.transform.InferType()(mod)
mutated_mod['func_3852'] = func_3852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3852_call = mutated_mod.get_global_var('func_3852')
var_3854 = relay.var("var_3854", dtype = "float32", shape = (13, 7, 3))#candidate|3854|(13, 7, 3)|var|float32
var_3855 = relay.var("var_3855", dtype = "float32", shape = (1, 462))#candidate|3855|(1, 462)|var|float32
var_3856 = relay.var("var_3856", dtype = "float64", shape = (180,))#candidate|3856|(180,)|var|float64
var_3857 = relay.var("var_3857", dtype = "float64", shape = (80,))#candidate|3857|(80,)|var|float64
var_3858 = relay.var("var_3858", dtype = "float32", shape = (35,))#candidate|3858|(35,)|var|float32
var_3859 = relay.var("var_3859", dtype = "float32", shape = (2288,))#candidate|3859|(2288,)|var|float32
call_3853 = func_3852_call(var_3854,var_3855,var_3856,var_3857,var_3858,var_3859,)
output = call_3853
func_3860 = relay.Function([var_3854,var_3855,var_3856,var_3857,var_3858,var_3859,], output)
mutated_mod['func_3860'] = func_3860
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3978 = relay.const([[[-1,7,-1,-10,-2],[-2,-6,10,7,-10],[7,6,-1,-8,-9],[2,-6,-2,9,3],[9,-10,-6,-2,2],[-9,6,-6,-6,3],[-3,-5,-5,8,-1],[5,10,-6,6,9],[-2,10,-6,8,-9],[5,-5,5,-9,3],[-5,9,-4,2,-3],[-1,-1,-6,5,7],[4,-10,-4,8,-7],[1,-1,-7,-3,6]],[[-2,-4,8,-10,-3],[-9,-10,-3,-3,6],[-4,-1,-7,-10,9],[-10,-5,-6,2,7],[2,10,6,-4,6],[8,7,5,-8,-6],[-2,-8,9,-1,-7],[-6,-4,-10,-2,9],[6,-2,-5,-1,-3],[-9,-5,4,-8,-7],[-1,7,1,-6,-4],[5,-2,-7,3,9],[-4,10,5,3,9],[2,3,7,-9,-9]],[[10,4,-10,-9,8],[-8,8,2,-4,-9],[-7,2,2,-5,4],[3,9,-4,-8,-1],[-2,-1,-7,-4,-9],[5,-5,5,-8,-8],[6,6,7,-4,2],[-3,4,-5,-6,3],[3,1,-5,-5,7],[-5,3,8,-1,6],[8,10,-5,3,5],[7,4,-5,-4,-1],[-4,-6,8,-8,8],[6,5,-8,-2,-2]],[[-6,4,4,-8,8],[9,-8,8,1,-6],[-9,-5,-2,-7,-3],[-3,5,-9,-5,-9],[-8,6,5,3,1],[3,4,6,-10,-10],[1,9,1,7,9],[-2,4,5,3,5],[7,-3,5,-7,-2],[5,-2,-9,6,-10],[2,4,-9,7,-6],[5,-10,4,-8,10],[10,3,-2,5,-8],[5,-7,8,-9,-10]]], dtype = "int64")#candidate|3978|(4, 14, 5)|const|int64
const_3979 = relay.const([[[-4,7,4,10,2],[-6,7,-9,-7,-10],[-4,8,9,1,-6],[1,4,2,1,5],[7,-10,1,3,-10],[10,-4,-7,6,8],[4,1,-9,-7,-7],[2,4,-8,3,-4],[4,8,-4,3,-4],[-9,-10,8,3,10],[8,6,7,-10,7],[5,7,1,8,-1],[-5,-3,-1,6,8],[8,9,-9,-9,-7]],[[2,8,-5,3,1],[10,-4,-2,-3,1],[-4,9,-2,-2,-7],[5,-2,3,2,-5],[-9,10,5,10,-8],[-1,-7,-8,9,10],[-8,7,8,7,5],[-4,4,-10,3,1],[9,6,4,-7,-1],[-1,3,-6,8,-2],[5,9,-7,-10,-7],[4,5,-3,1,2],[-8,10,10,2,-9],[-3,10,6,3,2]],[[7,7,5,10,2],[9,-2,-3,4,2],[-2,10,9,1,-1],[1,8,-1,9,-10],[-3,5,9,10,3],[-1,-7,7,6,-5],[1,-7,7,4,9],[-1,5,10,1,-7],[9,1,8,1,6],[-1,3,7,-5,-8],[-5,7,-2,-3,-6],[-9,-10,-3,8,2],[-10,-4,2,5,-4],[-2,-9,-10,5,-5]],[[-6,5,5,-4,-10],[9,-3,4,-4,-3],[-1,9,1,10,3],[-4,-2,-4,-7,-1],[7,10,3,-5,3],[7,-10,-4,6,-6],[1,-7,-1,9,-1],[8,10,-10,-1,2],[-3,-8,5,-6,7],[-7,6,-3,-5,6],[5,-4,1,8,8],[-6,8,6,7,4],[7,-4,5,9,-2],[-6,10,-1,-3,-3]]], dtype = "int64")#candidate|3979|(4, 14, 5)|const|int64
bop_3980 = relay.right_shift(const_3978.astype('int64'), relay.reshape(const_3979.astype('int64'), relay.shape_of(const_3978))) # shape=(4, 14, 5)
func_220_call = mod.get_global_var('func_220')
func_224_call = mutated_mod.get_global_var('func_224')
var_3984 = relay.var("var_3984", dtype = "float32", shape = (390,))#candidate|3984|(390,)|var|float32
call_3983 = relay.TupleGetItem(func_220_call(relay.reshape(var_3984.astype('float32'), [2, 15, 13]), relay.reshape(var_3984.astype('float32'), [2, 15, 13]), ), 0)
call_3985 = relay.TupleGetItem(func_224_call(relay.reshape(var_3984.astype('float32'), [2, 15, 13]), relay.reshape(var_3984.astype('float32'), [2, 15, 13]), ), 0)
output = relay.Tuple([bop_3980,call_3983,var_3984,])
output2 = relay.Tuple([bop_3980,call_3985,var_3984,])
func_3988 = relay.Function([var_3984,], output)
mod['func_3988'] = func_3988
mod = relay.transform.InferType()(mod)
var_3989 = relay.var("var_3989", dtype = "float32", shape = (390,))#candidate|3989|(390,)|var|float32
output = func_3988(var_3989)
func_3990 = relay.Function([var_3989], output)
mutated_mod['func_3990'] = func_3990
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4076 = relay.var("var_4076", dtype = "float32", shape = (2, 6, 16))#candidate|4076|(2, 6, 16)|var|float32
var_4077 = relay.var("var_4077", dtype = "float32", shape = (2, 6, 16))#candidate|4077|(2, 6, 16)|var|float32
bop_4078 = relay.mod(var_4076.astype('float32'), relay.reshape(var_4077.astype('float32'), relay.shape_of(var_4076))) # shape=(2, 6, 16)
bop_4081 = relay.less_equal(var_4076.astype('bool'), relay.reshape(bop_4078.astype('bool'), relay.shape_of(var_4076))) # shape=(2, 6, 16)
output = relay.Tuple([bop_4081,])
output2 = relay.Tuple([bop_4081,])
func_4087 = relay.Function([var_4076,var_4077,], output)
mod['func_4087'] = func_4087
mod = relay.transform.InferType()(mod)
var_4088 = relay.var("var_4088", dtype = "float32", shape = (2, 6, 16))#candidate|4088|(2, 6, 16)|var|float32
var_4089 = relay.var("var_4089", dtype = "float32", shape = (2, 6, 16))#candidate|4089|(2, 6, 16)|var|float32
output = func_4087(var_4088,var_4089,)
func_4090 = relay.Function([var_4088,var_4089,], output)
mutated_mod['func_4090'] = func_4090
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4104 = relay.var("var_4104", dtype = "float64", shape = (4, 9, 13))#candidate|4104|(4, 9, 13)|var|float64
uop_4105 = relay.log(var_4104.astype('float64')) # shape=(4, 9, 13)
func_220_call = mod.get_global_var('func_220')
func_224_call = mutated_mod.get_global_var('func_224')
var_4115 = relay.var("var_4115", dtype = "float32", shape = (195, 2))#candidate|4115|(195, 2)|var|float32
call_4114 = relay.TupleGetItem(func_220_call(relay.reshape(var_4115.astype('float32'), [2, 15, 13]), relay.reshape(var_4115.astype('float32'), [2, 15, 13]), ), 0)
call_4116 = relay.TupleGetItem(func_224_call(relay.reshape(var_4115.astype('float32'), [2, 15, 13]), relay.reshape(var_4115.astype('float32'), [2, 15, 13]), ), 0)
func_1033_call = mod.get_global_var('func_1033')
func_1038_call = mutated_mod.get_global_var('func_1038')
const_4125 = relay.const([[-10],[-3],[2],[-8],[4],[9],[-9],[-4],[1],[10],[-6],[-4],[10],[-6],[-7],[3],[7],[-8],[-8],[9],[-2],[1],[9],[-8],[-9],[-10],[7],[-6],[9],[-7],[10],[8],[4],[10],[2],[-3],[-10],[-8],[2],[-1],[4],[7],[-7],[-10],[7],[-7],[-5],[-6],[-8],[-2],[4],[7],[-10],[2],[10],[-4],[-7],[8],[4],[-4],[-3],[-7],[5],[1],[8],[6],[-9],[-7],[-7],[-2],[4],[-3],[-6],[9],[-9],[10],[4],[-2],[1],[-2],[7],[2],[-2],[-6],[7],[8],[-5],[-4],[-2],[-1],[-6],[4],[-10],[-10],[-2],[-1],[-2],[-6],[9],[-3],[-1],[8],[2],[6],[-7],[-6],[2],[4],[8],[5],[8],[-8],[7],[5],[9],[4],[1],[-5],[6],[-6],[10],[5],[-1],[6],[-2],[-9],[6],[-3],[3],[-1],[-7],[2],[9],[-10],[3],[-5],[7],[-7],[-8],[8],[-3],[-2],[-6],[4],[-4],[4],[1],[9],[5],[2],[-5],[-3],[6],[5],[-2],[-4],[1],[3],[-1],[-7],[-1],[-6],[8],[2],[-5],[3],[1],[6]], dtype = "int16")#candidate|4125|(168, 1)|const|int16
const_4126 = relay.const([[-6.507528,8.265314],[-5.849852,2.179255],[-8.636866,-5.050535],[0.957696,1.355876],[-3.142272,-1.991645],[-2.825647,1.703656],[-2.672980,8.322415],[-0.689220,-8.930294],[-4.219012,-5.054042],[-4.790085,0.740130],[7.544413,-5.184979],[-4.718838,1.295512],[-9.028542,-3.979411],[-6.160899,3.260484],[-1.404832,0.027819],[-8.079309,-2.471038],[-7.806712,8.760812],[-1.539172,9.149982],[-8.377617,-5.101171],[3.125178,3.135601],[0.275140,-2.966971],[8.876324,-4.576983],[-7.603476,-7.046328],[6.890852,-9.635259],[-4.202093,-7.210519],[-8.938170,-2.906959],[-3.733389,4.361739],[-7.473249,6.433835],[-6.964734,5.191313],[4.689476,-9.982081],[-9.857366,-5.876189],[6.881985,8.313042],[-7.979096,-9.142957],[6.403182,1.330852],[9.822782,3.295510],[5.621697,2.478026],[5.154455,5.483849],[8.992645,-4.980377],[2.522309,8.640097],[7.631165,-2.352678],[1.866420,2.955272],[2.497236,-3.132307],[3.261155,-5.553915],[-1.153101,0.285870],[3.585485,-9.175335],[-6.094746,-6.621640],[-4.536966,-3.806122],[-7.673678,5.473986],[7.293657,-7.774989],[-1.772216,4.858165],[-0.225109,-7.092349],[1.335665,-2.057500],[2.610658,1.999257],[-7.624883,6.363595],[-3.125420,-7.411822],[-7.224404,-3.223740],[-5.397313,-0.951932],[8.961656,2.442867],[1.333126,-3.619189],[4.394530,9.155296],[3.809368,-1.131194],[-7.618757,-9.517428],[8.078570,2.310002],[6.421967,3.400333],[-6.228209,-9.638664],[1.368978,-7.381220],[5.483711,2.216405],[2.645994,7.163638],[-7.466601,-3.198059],[9.446169,8.295056],[-8.023701,-0.002286],[-6.374593,4.545216],[9.384047,-2.266704],[2.413444,-4.965181],[9.082663,7.975044],[-0.888857,6.051438],[-1.860220,-4.631996],[6.147738,-5.446477],[-7.254130,4.114126],[-9.750171,-9.766087],[-5.076389,-4.854434],[8.237925,-3.229525],[2.428466,3.651699],[5.715171,-4.485909],[1.538208,3.543653],[-4.518983,-3.350116],[1.034619,4.336037],[-9.837199,1.053708],[-6.232429,5.208201],[-8.045620,-6.407199]], dtype = "float64")#candidate|4126|(90, 2)|const|float64
call_4124 = relay.TupleGetItem(func_1033_call(relay.reshape(const_4125.astype('int16'), [14, 12, 1]), relay.reshape(const_4125.astype('int16'), [14, 12, 1]), relay.reshape(call_4114.astype('float32'), [390, 1]), relay.reshape(const_4126.astype('float64'), [180,]), ), 3)
call_4127 = relay.TupleGetItem(func_1038_call(relay.reshape(const_4125.astype('int16'), [14, 12, 1]), relay.reshape(const_4125.astype('int16'), [14, 12, 1]), relay.reshape(call_4114.astype('float32'), [390, 1]), relay.reshape(const_4126.astype('float64'), [180,]), ), 3)
uop_4130 = relay.asin(uop_4105.astype('float64')) # shape=(4, 9, 13)
output = relay.Tuple([call_4114,var_4115,call_4124,const_4125,const_4126,uop_4130,])
output2 = relay.Tuple([call_4116,var_4115,call_4127,const_4125,const_4126,uop_4130,])
func_4134 = relay.Function([var_4104,var_4115,], output)
mod['func_4134'] = func_4134
mod = relay.transform.InferType()(mod)
mutated_mod['func_4134'] = func_4134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4134_call = mutated_mod.get_global_var('func_4134')
var_4136 = relay.var("var_4136", dtype = "float64", shape = (4, 9, 13))#candidate|4136|(4, 9, 13)|var|float64
var_4137 = relay.var("var_4137", dtype = "float32", shape = (195, 2))#candidate|4137|(195, 2)|var|float32
call_4135 = func_4134_call(var_4136,var_4137,)
output = call_4135
func_4138 = relay.Function([var_4136,var_4137,], output)
mutated_mod['func_4138'] = func_4138
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4563 = relay.var("var_4563", dtype = "int64", shape = (8, 13, 6))#candidate|4563|(8, 13, 6)|var|int64
var_4564 = relay.var("var_4564", dtype = "int64", shape = (8, 13, 6))#candidate|4564|(8, 13, 6)|var|int64
bop_4565 = relay.bitwise_and(var_4563.astype('int64'), relay.reshape(var_4564.astype('int64'), relay.shape_of(var_4563))) # shape=(8, 13, 6)
output = bop_4565
output2 = bop_4565
func_4571 = relay.Function([var_4563,var_4564,], output)
mod['func_4571'] = func_4571
mod = relay.transform.InferType()(mod)
mutated_mod['func_4571'] = func_4571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mutated_mod.get_global_var('func_4571')
var_4573 = relay.var("var_4573", dtype = "int64", shape = (8, 13, 6))#candidate|4573|(8, 13, 6)|var|int64
var_4574 = relay.var("var_4574", dtype = "int64", shape = (8, 13, 6))#candidate|4574|(8, 13, 6)|var|int64
call_4572 = func_4571_call(var_4573,var_4574,)
output = call_4572
func_4575 = relay.Function([var_4573,var_4574,], output)
mutated_mod['func_4575'] = func_4575
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4594 = relay.const([[[6,5],[-5,-1]],[[3,-6],[2,-10]],[[1,5],[-6,4]],[[1,3],[-10,6]],[[-6,-9],[5,10]],[[7,-6],[3,-5]],[[-3,-6],[5,3]],[[5,-10],[6,2]],[[-8,-4],[10,-10]],[[-1,-5],[-4,1]],[[-3,6],[-7,6]],[[6,7],[-3,-5]],[[8,3],[-5,-3]]], dtype = "int32")#candidate|4594|(13, 2, 2)|const|int32
const_4595 = relay.const([[[9,-5],[7,-10]],[[8,-10],[6,-5]],[[-7,-4],[2,-1]],[[-9,-1],[-4,-3]],[[2,-2],[1,-3]],[[3,-9],[-3,9]],[[-1,-4],[10,-10]],[[-6,4],[-9,-2]],[[6,-1],[8,-7]],[[-5,10],[-1,7]],[[4,8],[7,-3]],[[-6,-4],[5,-5]],[[10,9],[8,-10]]], dtype = "int32")#candidate|4595|(13, 2, 2)|const|int32
bop_4596 = relay.maximum(const_4594.astype('int32'), relay.reshape(const_4595.astype('int32'), relay.shape_of(const_4594))) # shape=(13, 2, 2)
output = relay.Tuple([bop_4596,])
output2 = relay.Tuple([bop_4596,])
func_4610 = relay.Function([], output)
mod['func_4610'] = func_4610
mod = relay.transform.InferType()(mod)
output = func_4610()
func_4611 = relay.Function([], output)
mutated_mod['func_4611'] = func_4611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4639 = relay.var("var_4639", dtype = "float64", shape = (16, 13, 5))#candidate|4639|(16, 13, 5)|var|float64
var_4640 = relay.var("var_4640", dtype = "float64", shape = (16, 13, 5))#candidate|4640|(16, 13, 5)|var|float64
bop_4641 = relay.power(var_4639.astype('float64'), relay.reshape(var_4640.astype('float64'), relay.shape_of(var_4639))) # shape=(16, 13, 5)
output = relay.Tuple([bop_4641,])
output2 = relay.Tuple([bop_4641,])
func_4649 = relay.Function([var_4639,var_4640,], output)
mod['func_4649'] = func_4649
mod = relay.transform.InferType()(mod)
mutated_mod['func_4649'] = func_4649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4649_call = mutated_mod.get_global_var('func_4649')
var_4651 = relay.var("var_4651", dtype = "float64", shape = (16, 13, 5))#candidate|4651|(16, 13, 5)|var|float64
var_4652 = relay.var("var_4652", dtype = "float64", shape = (16, 13, 5))#candidate|4652|(16, 13, 5)|var|float64
call_4650 = func_4649_call(var_4651,var_4652,)
output = call_4650
func_4653 = relay.Function([var_4651,var_4652,], output)
mutated_mod['func_4653'] = func_4653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_4680 = relay.TupleGetItem(func_4610_call(), 0)
call_4681 = relay.TupleGetItem(func_4611_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
var_4688 = relay.var("var_4688", dtype = "int32", shape = (660,))#candidate|4688|(660,)|var|int32
call_4687 = func_1070_call(relay.reshape(var_4688.astype('int32'), [15, 4, 11]))
call_4689 = func_1070_call(relay.reshape(var_4688.astype('int32'), [15, 4, 11]))
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_4699 = func_1070_call(relay.reshape(call_4687.astype('int32'), [15, 4, 11]))
call_4700 = func_1070_call(relay.reshape(call_4687.astype('int32'), [15, 4, 11]))
output = relay.Tuple([call_4680,call_4687,var_4688,call_4699,])
output2 = relay.Tuple([call_4681,call_4689,var_4688,call_4700,])
func_4707 = relay.Function([var_4688,], output)
mod['func_4707'] = func_4707
mod = relay.transform.InferType()(mod)
mutated_mod['func_4707'] = func_4707
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4708 = relay.var("var_4708", dtype = "int32", shape = (660,))#candidate|4708|(660,)|var|int32
func_4707_call = mutated_mod.get_global_var('func_4707')
call_4709 = func_4707_call(var_4708)
output = call_4709
func_4710 = relay.Function([var_4708], output)
mutated_mod['func_4710'] = func_4710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_4754 = relay.TupleGetItem(func_4610_call(), 0)
call_4755 = relay.TupleGetItem(func_4611_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
const_4761 = relay.const([-9,-4,5,-6,-6,-8,1,-8,-7,-3,3,-4,-8,4,-9,5,-6,-1,-6,-10,7,9,-1,-7,7,-3,3,1,10,-9,6,7,2,-5,-4,-1,2,10,-6,2,-8,6,-4,-5,10,-3,9,-10,-9,-1,9,5,3,5,-4,-5,-3,4,-5,2,-4,-4,7,3,-9,9,6,9,9,1,4,4,4,-5,-6,4,3,2,-2,-6,-1,8,6,9,3,9,-3,-5,2,5,10,-7,-9,-3,-3,-3,3,-4,-1,6,-10,-1,9,-1,7,-8,-7,-10,-5,-7,-3,5,-2,-6,-9,-6,9,-3,5,-9,9,-1,-4,3,7,8,-2,7,1,8,-10,-2,-4,-9,-8,-5,-8,3,1,-1,-8,10,5,6,3,-7,-8,1,-3,-3,9,-8,-6,10,1,-6,4,10,3,3,-8,8,9,-8,-10,-1,-8,-7,-2,-2,8,-1,-3,-10,-7,-4,-5,-10,4,7,10,-2,-9,-5,-5,5,4,-8,8,-5,2,1,4,4,-1,1,-10,-2,-3,1,1,-3,-1,3,-8,-6,2,10,1,3,6,5,-6,-7,1,8,4,-10,10,-6,-6,9,-2,-3,4,4,9,-7,6,5,-4,3,2,-2,-9,-1,5,-2,-10,1,-10,-5,6,-5,8,4,-2,-9,-2,-9,3,5,-9,-4,-1,-2,-10,1,10,10,5,9,1,-4,-1,2,-2,-2,6,-1,-3,-8,-1,-10,-5,1,4,-9,-10,-6,7,-4,6,3,4,-9,-8,-9,-7,2,-9,4,-6,8,8,-8,-3,6,-10,3,5,-10,-10,4,10,-1,-10,4,-8,4,8,2,4,-5,9,10,-2,6,1,-9,-5,-2,5,-3,-10,-10,-8,-2,-10,-1,-6,10,-1,-8,-6,3,-9,-8,-3,-9,1,5,-2,4,-5,1,-5,-7,-9,1,6,-9,-1,1,-10,-10,10,10,2,3,10,7,7,4,-1,-3,8,-1,-9,-4,-3,-1,10,4,-7,9,1,5,-2,-5,-5,-1,8,-4,6,-7,-2,1,-10,-6,-2,-6,-3,-2,-1,1,5,9,-3,10,10,-10,6,6,6,2,-9,4,9,-8,-3,8,-8,-1,9,2,-1,-4,4,2,4,-2,2,2,2,-4,8,4,9,10,-1,7,-5,-8,1,-10,3,5,-8,9,-10,6,4,-5,-7,3,7,1,-1,2,-10,6,-6,9,1,-3,-2,8,-1,1,7,-8,-3,6,-10,9,-3,-3,7,3,1,-10,7,9,8,9,-5,10,6,4,-6,-5,-8,-8,-10,5,-8,-4,-3,-6,4,-8,2,7,-6,5,-3,-1,-9,-8,-1,-2,-9,8,1,3,-1,4,-9,-3,-3,-6,-1,7,-7,10,-9,-1,-9,10,-4,5,4,-9,2,5,-2,-2,-8,-2,-6,-5,3,5,4,1,-8,3,8,2,-6,5,-10,3,-6,4,-7,8,2,3,-7,-6,-5,-5,-3,-2,8,8,-4,9,-8,-1,2,7,3,2,6,-4,-6,-3,8,9,5,-5,10,1,6,1,3,2,9,5,1,-8,8,6,-9,1,4,-2,-1,10,-5,5,-10,4,-10,-7,-6,-10,4,-10,10,-6,-9,-9,-1,8,-10,6,10,1,8,-3,-3,-1,-8,2,2,4,-6,2,10,7,-2,3,-4,-2,-4,-1,7,-4,2,-4,-1,6,1,-9,9,-2,9,-3,-2,9,1,1,-1,4,10,-6,6,10,-1,8,-5,10,-8,8,7,5], dtype = "int32")#candidate|4761|(660,)|const|int32
call_4760 = func_1070_call(relay.reshape(const_4761.astype('int32'), [15, 4, 11]))
call_4762 = func_1070_call(relay.reshape(const_4761.astype('int32'), [15, 4, 11]))
func_299_call = mod.get_global_var('func_299')
func_301_call = mutated_mod.get_global_var('func_301')
const_4767 = relay.const([6.841931,-1.141619,-7.822328,-6.379170,-1.653456,7.719518,-0.194049,-8.813579,1.544204,-2.651238,1.694814,-9.249433,5.722271,7.304650,5.375190,-2.783146,8.759137,-0.026775,8.789043,2.849082,-9.807440,6.832392,-1.194223,-3.653174,-1.758505,-3.320684,-4.856612,4.296612,8.064391,-7.821665,-1.221757,1.061042,6.755955,2.415777,-0.650273,-1.288461,-4.537329,2.231998,-4.754035,-9.279035,-6.979765,-9.135299,9.466215,-5.511891,-4.831332,8.212905,-2.450579,-2.554832,-5.921617,-0.313487,-5.312010,0.688386,-7.319888,-8.533885,-7.755269,2.169412,1.924955,1.404503,-0.665492,0.258803,-0.681510,6.728493,0.290079,4.448295,-5.292338,-5.555800,-9.519441,9.020218,-3.824306,9.092478,-3.868536,7.348771,-2.015220,5.266608,2.046485,-4.173234,9.682270,-3.661646,4.229594,8.780811], dtype = "float64")#candidate|4767|(80,)|const|float64
call_4766 = relay.TupleGetItem(func_299_call(relay.reshape(const_4767.astype('float64'), [10, 8, 1])), 0)
call_4768 = relay.TupleGetItem(func_301_call(relay.reshape(const_4767.astype('float64'), [10, 8, 1])), 0)
output = relay.Tuple([call_4754,call_4760,const_4761,call_4766,const_4767,])
output2 = relay.Tuple([call_4755,call_4762,const_4761,call_4768,const_4767,])
func_4770 = relay.Function([], output)
mod['func_4770'] = func_4770
mod = relay.transform.InferType()(mod)
mutated_mod['func_4770'] = func_4770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mutated_mod.get_global_var('func_4770')
call_4771 = func_4770_call()
output = call_4771
func_4772 = relay.Function([], output)
mutated_mod['func_4772'] = func_4772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_4776 = relay.TupleGetItem(func_4770_call(), 1)
call_4777 = relay.TupleGetItem(func_4772_call(), 1)
const_4781 = relay.const([[[-3,8,3,-2,7,3,-5,4,4,10,2],[-1,9,10,2,-7,3,2,9,4,-4,-1],[-10,3,-7,-5,-1,9,2,3,-5,8,6],[-2,5,-2,-7,-10,-5,10,9,5,4,2]],[[-5,-7,-5,-6,6,-7,-8,-2,1,-1,-8],[-10,-10,7,-9,9,3,-4,-2,9,-2,1],[-5,-4,-6,3,-10,8,-8,-4,-1,-2,-7],[-3,9,-7,10,1,-10,2,-4,7,-7,-3]],[[-10,-5,8,-7,6,-5,6,7,1,-1,-5],[-6,-9,-2,-2,5,-10,4,8,2,-5,-10],[-9,7,7,1,-3,2,4,2,6,7,-6],[3,-6,9,-2,-2,-7,2,-9,7,-4,5]],[[10,-1,5,-4,10,-4,-2,8,3,6,-3],[4,-3,-5,8,4,-9,6,-4,-2,8,3],[-2,-4,4,-3,-10,8,-7,-2,-3,5,-5],[4,1,-6,-6,9,-1,-3,4,-2,4,-10]],[[1,8,-2,5,-5,-7,-9,-7,3,2,-8],[-8,10,9,-8,-5,-2,-4,-5,2,-10,-8],[1,3,-1,7,-10,4,-5,-6,-3,-3,-5],[1,-5,-1,9,3,5,3,1,-5,-5,4]],[[1,4,-4,-1,3,10,3,5,1,4,-4],[-1,-7,9,-7,-3,-5,-4,-3,6,7,7],[7,3,-2,5,-4,-2,-7,4,-3,4,-3],[5,-3,3,8,1,-4,5,-3,-1,-1,1]],[[-1,1,1,2,-4,-9,1,-9,4,4,6],[3,4,-10,4,-2,-6,10,10,1,-2,-1],[4,2,9,7,7,-9,-1,-5,-10,-3,4],[4,-7,6,-5,2,8,-9,-2,-4,-4,2]],[[-2,2,8,8,9,3,-5,7,7,-1,-7],[-4,7,-10,3,-8,-2,6,-6,-1,-6,-4],[5,-3,3,9,-6,-1,-3,4,4,10,2],[8,-10,-4,-5,-9,10,-7,8,4,-9,7]],[[-5,-5,-10,-7,-2,-2,-5,-1,7,-3,4],[1,-5,5,10,-5,2,-8,-6,-7,-9,1],[7,6,-1,-10,-6,6,6,5,-5,4,2],[-2,-6,-7,9,-1,-9,2,-4,5,-3,-3]],[[-6,6,-1,-1,-10,-3,1,1,7,10,-9],[-8,-5,4,7,7,-8,-5,3,1,-6,-2],[-4,10,-7,9,-1,8,3,-3,1,-2,-3],[9,-2,1,-7,-6,6,-4,4,-8,2,2]],[[1,-6,3,3,-6,4,-3,5,-8,10,-6],[-8,8,7,3,7,-3,6,10,4,2,-3],[2,4,8,-5,-6,7,8,-4,-3,7,-2],[4,4,10,-7,-10,3,-9,6,5,7,-6]],[[6,-8,-10,5,-1,6,8,-1,10,-3,5],[-4,-8,-5,-1,-9,-10,3,5,-2,10,2],[-5,-2,6,10,9,-4,-2,-1,-9,-7,-9],[-9,-10,-1,-8,-8,-5,9,-8,-3,-2,-6]],[[-6,-5,-9,-6,-3,-3,3,-3,4,-7,4],[10,-7,-10,2,3,-5,4,1,10,-4,-10],[6,1,5,-1,-4,-2,8,9,-10,-9,-1],[6,-5,-9,-1,8,-2,-1,7,-7,-5,-1]],[[1,-2,-2,-3,-5,6,-7,-9,-4,10,-7],[3,3,4,-1,10,5,-2,-4,-2,7,-9],[5,-5,-6,-4,-5,7,-9,7,-6,-3,-10],[7,-3,3,9,4,-9,-10,5,-9,3,10]],[[5,-3,6,-1,2,-10,-7,2,-4,-9,-7],[-9,-4,-5,-4,-10,-4,-9,10,9,-8,-6],[-4,2,-7,1,9,-8,-10,-2,2,3,-7],[-8,-10,9,-8,4,3,9,6,-4,2,10]]], dtype = "int32")#candidate|4781|(15, 4, 11)|const|int32
bop_4782 = relay.less(call_4776.astype('bool'), relay.reshape(const_4781.astype('bool'), relay.shape_of(call_4776))) # shape=(15, 4, 11)
bop_4785 = relay.less(call_4777.astype('bool'), relay.reshape(const_4781.astype('bool'), relay.shape_of(call_4777))) # shape=(15, 4, 11)
bop_4787 = relay.bitwise_and(call_4776.astype('int64'), relay.reshape(const_4781.astype('int64'), relay.shape_of(call_4776))) # shape=(15, 4, 11)
bop_4790 = relay.bitwise_and(call_4777.astype('int64'), relay.reshape(const_4781.astype('int64'), relay.shape_of(call_4777))) # shape=(15, 4, 11)
output = relay.Tuple([bop_4782,bop_4787,])
output2 = relay.Tuple([bop_4785,bop_4790,])
func_4821 = relay.Function([], output)
mod['func_4821'] = func_4821
mod = relay.transform.InferType()(mod)
output = func_4821()
func_4822 = relay.Function([], output)
mutated_mod['func_4822'] = func_4822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_4837 = relay.TupleGetItem(func_4610_call(), 0)
call_4838 = relay.TupleGetItem(func_4611_call(), 0)
output = call_4837
output2 = call_4838
func_4843 = relay.Function([], output)
mod['func_4843'] = func_4843
mod = relay.transform.InferType()(mod)
output = func_4843()
func_4844 = relay.Function([], output)
mutated_mod['func_4844'] = func_4844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_4861 = relay.TupleGetItem(func_4770_call(), 1)
call_4862 = relay.TupleGetItem(func_4772_call(), 1)
func_4571_call = mod.get_global_var('func_4571')
func_4575_call = mutated_mod.get_global_var('func_4575')
var_4868 = relay.var("var_4868", dtype = "int64", shape = (24, 26))#candidate|4868|(24, 26)|var|int64
call_4867 = func_4571_call(relay.reshape(var_4868.astype('int64'), [8, 13, 6]), relay.reshape(var_4868.astype('int64'), [8, 13, 6]), )
call_4869 = func_4571_call(relay.reshape(var_4868.astype('int64'), [8, 13, 6]), relay.reshape(var_4868.astype('int64'), [8, 13, 6]), )
bop_4870 = relay.less(var_4868.astype('bool'), relay.reshape(call_4867.astype('bool'), relay.shape_of(var_4868))) # shape=(24, 26)
bop_4873 = relay.less(var_4868.astype('bool'), relay.reshape(call_4869.astype('bool'), relay.shape_of(var_4868))) # shape=(24, 26)
output = relay.Tuple([call_4861,bop_4870,])
output2 = relay.Tuple([call_4862,bop_4873,])
func_4874 = relay.Function([var_4868,], output)
mod['func_4874'] = func_4874
mod = relay.transform.InferType()(mod)
mutated_mod['func_4874'] = func_4874
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4875 = relay.var("var_4875", dtype = "int64", shape = (24, 26))#candidate|4875|(24, 26)|var|int64
func_4874_call = mutated_mod.get_global_var('func_4874')
call_4876 = func_4874_call(var_4875)
output = call_4876
func_4877 = relay.Function([var_4875], output)
mutated_mod['func_4877'] = func_4877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_4996 = relay.TupleGetItem(func_4821_call(), 0)
call_4997 = relay.TupleGetItem(func_4822_call(), 0)
func_2085_call = mod.get_global_var('func_2085')
func_2089_call = mutated_mod.get_global_var('func_2089')
const_4999 = relay.const(7, dtype = "int8")#candidate|4999|()|const|int8
var_5000 = relay.var("var_5000", dtype = "int8", shape = (40,))#candidate|5000|(40,)|var|int8
call_4998 = func_2085_call(relay.reshape(const_4999.astype('int8'), []), relay.reshape(var_5000.astype('int8'), [4, 5, 2]), )
call_5001 = func_2085_call(relay.reshape(const_4999.astype('int8'), []), relay.reshape(var_5000.astype('int8'), [4, 5, 2]), )
func_4843_call = mod.get_global_var('func_4843')
func_4844_call = mutated_mod.get_global_var('func_4844')
call_5009 = func_4843_call()
call_5010 = func_4843_call()
output = relay.Tuple([call_4996,call_4998,const_4999,var_5000,call_5009,])
output2 = relay.Tuple([call_4997,call_5001,const_4999,var_5000,call_5010,])
func_5015 = relay.Function([var_5000,], output)
mod['func_5015'] = func_5015
mod = relay.transform.InferType()(mod)
var_5016 = relay.var("var_5016", dtype = "int8", shape = (40,))#candidate|5016|(40,)|var|int8
output = func_5015(var_5016)
func_5017 = relay.Function([var_5016], output)
mutated_mod['func_5017'] = func_5017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4843_call = mod.get_global_var('func_4843')
func_4844_call = mutated_mod.get_global_var('func_4844')
call_5028 = func_4843_call()
call_5029 = func_4843_call()
output = relay.Tuple([call_5028,])
output2 = relay.Tuple([call_5029,])
func_5036 = relay.Function([], output)
mod['func_5036'] = func_5036
mod = relay.transform.InferType()(mod)
output = func_5036()
func_5037 = relay.Function([], output)
mutated_mod['func_5037'] = func_5037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_5050 = relay.TupleGetItem(func_4821_call(), 1)
call_5051 = relay.TupleGetItem(func_4822_call(), 1)
func_3852_call = mod.get_global_var('func_3852')
func_3860_call = mutated_mod.get_global_var('func_3860')
const_5058 = relay.const([[4.696658,0.211587,-1.425027,-3.347767,-3.395756,2.788387,8.658653,7.988011,-0.136314,1.257185,6.395828,-7.191005,-1.205773,7.678902,-6.831833,-5.509285,-7.511335,-7.632029,6.104663,-5.186606,-7.997139,4.144435,4.930190,7.979836,6.737802,3.941047,3.705334,-6.534028,1.068294,-0.741480,-2.454660,-7.249519,-7.043878,0.697193,2.391122,-0.974935,9.988834,7.425049,-3.849132,-9.559312,-3.401212,1.620223,-2.416268,5.905672,4.558048,8.335596,0.542000,-5.936081,-9.741034,6.796014,-9.966373,-1.974433,1.398417,-4.812305,-1.341755,-5.901544,-9.456538,-3.276772,8.948948,1.447180,-6.652801,-1.601722,-0.471621,9.336248,-5.167773,-5.916048,-4.019165,-5.609803,4.082304,-8.746075,-5.903169,-8.145245,-0.502129,9.681721,-9.373988,-8.163102,1.111752,-0.318221,4.727278,-5.415116,1.029151,-9.789738,0.868862,4.015543,-0.279106,-6.764306,-8.509902,5.834161,-2.822993,-0.901102,8.672270,6.117184,5.566187,-9.553102,4.081657,-2.683761,-4.595347,7.362281,-1.989675,-4.160051,-3.683247,0.746466,6.747620,8.439669,0.499968,-4.119094,-6.345191,2.429920,-7.846818,-8.531141,-0.591531,-3.414863,-9.185895,2.204447,-2.953530,7.994607,-6.650378,-2.653282,2.215005,2.027356,0.301911,-7.628164,9.130131,-1.788201,4.618688,-5.274882,8.966036,-7.604489,-8.046015,-5.679005,3.863597,0.312116,-4.044702,0.894834,6.899590,-2.457136,5.773517,-0.196631,-6.642090,-4.410713,4.510867,-3.290310,4.725506,-4.919637,-5.953102,-3.590791,-7.022875,4.543963,7.926970,1.637939,-8.626459,-7.450925,-4.317033,-1.155360,5.965655,-9.345166,4.817021,5.826180,-3.118391,-1.421254,4.748652,-5.312418,-7.734436,-5.754459,5.653293,-9.461743,-3.938246,8.649623,8.522284,9.391627,-5.316697,-8.080430,-6.115059,-4.409610,2.471456,6.132238,3.958845,8.660832,-3.487915,-8.917121,3.880024,6.976522,7.714590,-6.464028,-6.653206,1.844173,6.552275,7.602243,8.035460,-4.114355,-6.628207,6.568749,-4.204404,-0.862162,6.219531,-4.610555,3.577863,-1.126277,-0.548353,-0.703078,-1.516697,7.894257,3.033237,-4.712436,-3.024037,7.059575,-8.332237,-0.311631,2.116864,1.664330,3.233288,8.109869,1.889555,7.065744,-3.087645,2.397736,3.622303,4.389713,7.084807,-8.679910,-1.108388,-0.540734,-2.742955,6.521188,6.199532,-3.069993,-4.532816,-2.040380,4.212880,8.941042,9.519590,1.791176,1.244388,4.383604,-8.914359,-3.089834,0.147372,7.049980,-9.064707,-6.934345,-0.274161,-8.715904,-5.646965,-1.692236,0.104498,-4.302018,-6.174184,7.024112,-9.471940,-6.431184,-1.365460,1.496205,-5.251846,-1.260610,-1.558676,-5.999463,7.795439,9.642986,1.955355,-5.092118,-9.005251,2.830889,-9.915342,-3.374516,8.621315,5.947811,-9.438686,-6.488342,4.708272,5.586652,6.249242,-4.354653,-7.137775]], dtype = "float32")#candidate|5058|(1, 273)|const|float32
var_5059 = relay.var("var_5059", dtype = "float32", shape = (462,))#candidate|5059|(462,)|var|float32
var_5060 = relay.var("var_5060", dtype = "float64", shape = (180,))#candidate|5060|(180,)|var|float64
const_5061 = relay.const([-2.052755,5.979883,-3.856127,9.581242,-3.912254,6.790575,-7.246045,8.027469,-8.697641,-7.354310,-9.509769,5.784765,6.913052,-0.896040,-0.431130,3.955760,4.389722,-7.298113,-3.518954,-9.735090,-4.602104,-5.614561,-3.571926,-6.208039,7.258370,4.587472,1.945616,7.190714,-0.443860,5.257971,4.335656,8.316944,5.457750,-0.467522,4.815968,-3.617499,8.854522,-5.363423,1.096105,-9.305469,-8.314953,-9.330035,-7.922597,-0.543196,4.607393,6.841821,-4.620588,2.488353,-0.600731,5.033670,-3.409815,6.841489,-3.366012,8.609653,-9.071195,1.104866,-7.269626,-5.759998,5.629820,9.402422,5.475711,6.516405,6.851935,4.085409,-7.245864,-0.743823,2.713714,-3.943866,2.801992,3.846509,5.643145,-9.948072,-4.342396,-8.071429,-4.234351,-1.575907,-5.943704,2.105882,4.930861,8.980750], dtype = "float64")#candidate|5061|(80,)|const|float64
var_5062 = relay.var("var_5062", dtype = "float32", shape = (35, 1))#candidate|5062|(35, 1)|var|float32
const_5063 = relay.const([3.004447,3.194822,-9.765887,2.913032,8.924247,-9.755127,7.471242,5.347242,-8.522670,6.551987,6.949328,8.262834,5.989798,-3.977699,-3.234211,3.334143,2.971006,2.653461,-7.561014,-9.020937,-3.257315,-8.187603,-9.904685,3.438667,-5.376713,-2.863342,-5.897474,6.328177,5.263911,-3.481950,9.399594,-8.848643,9.741910,-9.889575,-6.694011,5.835835,2.331173,-6.997278,-4.669553,2.741326,-3.969003,-2.036366,8.768273,6.870369,5.046019,-6.280202,3.602865,1.896945,9.270704,6.013442,0.108257,-1.622319,-4.899919,-9.097840,-9.368746,9.331099,4.750870,2.688464,7.185807,-7.974179,3.712921,-8.941919,8.185756,7.028175,7.485753,-6.797941,6.773918,-0.553736,6.328291,-2.178752,-6.122366,-5.379014,7.943190,-1.372324,-3.697487,-8.043607,-8.368637,0.713584,-0.881217,-8.673226,0.358984,-7.348951,9.481946,-0.474490,9.397600,1.109928,-6.004112,-9.647572,0.570983,-9.923696,9.762035,1.330082,1.282028,1.451289,4.615186,-8.612972,-5.250623,-1.694926,6.735589,-1.003889,9.200337,-7.075520,8.096089,-3.841912,8.754210,0.148844,1.254158,-2.818260,8.635565,-4.844816,8.740641,4.048888,-8.803985,-3.862456,-7.652852,-5.202284,-3.690840,5.441914,5.137475,-6.817607,-1.061177,8.445375,3.243187,4.790158,0.803021,3.894865,-8.303953,-3.492519,-8.703336,-0.409583,0.286346,7.871900,1.435567,-9.744567,-5.068227,4.846307,-0.063775,-6.395181,6.921355,-4.947619,1.311688,2.075221,-5.653007,-2.803309,-6.696328,7.013134,-9.555230,7.413509,5.984864,-9.448596,5.687025,-5.338281,2.545491,3.693184,-0.938299,0.918743,1.785973,9.781573,9.747507,2.515120,-8.435046,1.339878,2.439322,-2.738843,-6.806263,-2.885838,7.872523,2.876598,1.753219,2.485761,-9.038851,0.998144,1.829773,0.583336,2.161642,4.263959,7.782771,-4.345558,0.082032,0.526222,2.942852,0.242023,5.362611,3.643448,2.097608,-5.796673,-6.201366,-0.866110,2.573650,-8.968804,-4.010921,-6.698779,-8.082336,-7.823509,-0.749691,-4.600006,5.027227,-2.374137,-2.350693,0.690811,-0.942288,-0.104000,3.432872,-1.858411,-3.609131,2.177672,-2.052034,6.403120,-7.768349,4.488836,0.790545,3.160814,6.808601,9.267935,3.068536,-7.940897,6.931770,-2.801554,6.825664,7.870620,5.737524,-3.238470,-4.591721,4.077702,3.569756,4.479485,-7.004042,6.378958,-9.473260,8.977173,0.573046,8.865766,-2.645701,2.221043,9.814140,-9.636979,-2.281548,-4.444411,-7.667571,3.547052,-3.183909,-0.726640,6.658681,3.452311,6.541039,-2.372521,-5.562781,8.183189,9.485491,-2.117343,3.466794,-8.549700,8.240280,-3.690540,-0.183497,1.745955,1.604806,0.776032,3.391491,-7.635489,1.217048,2.930503,1.678632,3.803647,0.415679,0.558197,-3.583701,-6.518262,-9.028152,5.513746,7.016152,-9.031521,-2.736317,0.886456,-1.622983,-1.894342,-4.362465,6.401496,-4.124568,1.636456,-2.503493,-7.306767,-1.057051,-6.771926,-7.807737,9.017254,-7.737888,-3.662071,2.094196,-5.931603,0.961291,5.343789,-1.477381,4.680339,4.291659,-4.263147,5.274321,-8.291479,-5.747780,4.920742,-8.227678,-6.258022,-8.107417,-8.692308,-9.725331,3.828814,2.439082,-2.822354,8.417058,9.962860,-2.009416,-1.563590,-1.631903,0.369418,9.339708,0.364775,1.403774,-0.589419,-4.270966,0.275363,7.572762,1.634990,4.339649,-5.420335,7.898566,-5.081448,1.814957,-8.165115,4.214567,-1.949651,-9.513911,0.282297,4.432311,9.517704,-1.745454,1.304006,9.792495,-9.106862,-0.076046,3.437640,-0.756728,2.071422,-0.336280,-1.579950,9.485013,-3.064281,-4.931626,0.586587,1.725254,-3.720366,2.371757,3.526889,-7.277006,6.259680,-8.300375,-6.211338,-4.147666,-6.293176,6.779275,9.885038,-8.584023,-8.514176,3.250601,-9.838179,-1.573312,-4.327077,-6.672024,-6.866977,3.209748,8.483321,-9.940090,6.171716,3.459909,2.363803,-8.023358,9.583261,-5.893345,0.856599,2.171027,-9.483298,-7.403582,1.055562,-1.729783,4.890886,-0.187983,1.255948,1.791794,6.333326,4.335292,2.070363,1.204286,-3.833690,2.424079,3.908557,2.881317,-2.654336,-9.224135,6.858926,-3.394506,7.662177,8.839930,5.696419,1.462050,-9.406418,-6.402310,-4.308694,-0.869792,3.253213,-8.663835,6.635937,6.683062,-3.055342,5.025770,-1.326056,-7.943253,-6.129236,9.714841,-4.103421,9.937580,9.781838,8.932234,4.824845,-2.358528,5.082247,-6.062655,-8.333238,-6.496518,3.884376,-4.992618,7.478930,0.406622,1.932172,-8.159207,0.775990,-2.805200,8.016361,-6.972104,4.082043,9.906023,-8.666859,6.017373,7.164002,9.575352,-0.802929,7.285089,-2.229672,2.384203,0.063938,-9.371662,8.361475,0.805840,-0.797245,-2.321877,-9.084036,-1.311777,5.065886,8.441671,1.215882,6.279399,8.592603,-9.675100,-2.733696,4.821538,7.484545,-3.124623,-2.119772,7.739033,-2.187616,-9.817578,0.384047,9.266811,5.537723,-1.621687,8.365092,-0.408226,-0.668936,-2.858208,-2.547829,-1.578283,2.034439,4.061826,-6.248735,-6.864982,-6.530296,3.432219,6.924917,-7.473366,4.234257,-3.971449,-6.748856,7.005672,1.918393,1.573491,6.738680,1.671094,9.550889,-0.583820,1.759351,-1.428260,-3.768909,7.087211,-1.525687,-6.016165,-1.282590,-9.509142,0.817513,1.205842,2.806673,-7.103639,-1.209314,-9.481376,-5.923781,4.285190,1.318252,9.200185,7.412144,-4.314485,-1.871507,-6.149357,0.693458,-9.982581,-6.712623,5.816418,-7.388213,9.861457,6.981797,-9.843956,-3.576660,7.483762,3.908847,9.285311,4.059275,-6.789493,-8.366904,9.397029,4.879138,-0.041273,2.260536,-5.508690,-2.431312,7.069057,8.561093,4.845458,5.535766,1.620618,-4.873381,-0.804425,-3.891850,6.286218,5.897504,-8.199747,-0.494437,-6.954489,-2.971806,-6.446043,-8.100454,-5.299647,6.918625,-3.656206,-1.898785,-5.781871,-8.078641,0.439074,7.429187,-0.548197,1.992105,-0.867801,7.693804,7.615854,2.475456,-5.485912,8.254829,2.057915,1.876602,-1.745034,9.399588,-7.723407,0.802456,8.435295,-1.773479,1.253486,-5.859465,-0.215618,-7.862178,-6.531325,1.357333,-5.243910,1.323358,4.684764,1.205180,9.756659,-8.442053,-8.341038,7.091748,1.274820,3.111559,3.399780,-5.744848,-2.239348,7.238438,-8.453713,5.076577,-8.692167,-9.013230,8.966150,1.764892,-9.137783,-2.257073,3.344928,-7.041756,-2.408176,6.233279,-9.368018,5.266679,-6.750110,6.276463,7.175042,7.602442,6.167266,9.991794,6.074750,0.508799,7.959625,8.193277,5.164377,6.021338,3.443262,8.401689,-4.891940,-4.172461,-4.282402,1.696197,8.600404,1.017638,-8.155202,4.011809,6.506125,6.240947,7.356095,1.760345,2.998192,-0.449873,6.154368,-2.735165,-6.521181,-9.166211,-8.591713,-4.144009,5.747068,-1.220884,-3.748274,1.006756,8.207698,-4.224994,4.602212,2.119160,-2.814897,-5.270438,-6.913882,8.112793,7.084593,0.488551,3.578875,9.420807,6.264654,-0.529414,-5.328876,9.244860,4.336150,-0.486869,1.500974,0.974549,4.756337,5.428357,-2.038336,-1.443397,-7.915378,8.507809,3.575184,-0.513096,-9.933530,-4.053002,1.637960,-5.571539,-1.824634,2.867524,1.284071,0.467167,-7.128785,-6.089492,-4.625429,0.738592,-5.271888,-5.545585,4.641756,-9.908812,-8.054367,-8.744070,-8.268853,-3.715402,5.488004,-4.633270,-6.876359,9.470689,-2.858972,5.546376,-5.400511,2.856456,4.107586,-5.990674,0.800769,-2.765122,-2.954609,0.697334,-0.655450,9.167363,1.834026,-2.075656,3.888017,0.283444,7.776090,-3.572017,5.939179,-0.162460,-5.554642,8.090266,0.593863,5.844235,1.879454,-4.585664,-9.439797,7.288537,9.999810,6.203884,-8.903416,-5.537577,9.128667,9.995161,-2.276382,3.145468,5.764994,-0.537093,-3.603639,-9.598277,-4.194195,9.396219,-7.816334,5.954465,-7.049741,-6.767429,4.830364,-7.267575,-3.387736,3.143684,2.233085,1.361648,0.560806,4.498215,6.269778,6.226218,-2.686657,-6.376400,-7.915088,-2.619172,-4.836850,8.969050,6.435841,-4.594695,0.848738,9.111818,-5.490631,0.161845,-1.429997,5.330845,-7.056341,-1.500195,-6.590394,7.124550,-5.118130,6.338107,2.397520,-2.404958,6.539695,-7.399562,-7.810492,7.353276,-1.966764,-5.238374,-8.376790,-3.955488,9.733712,9.029582,2.882820,-4.475893,0.827733,-2.345863,-4.712718,1.311237,7.803018,-3.466414,2.457452,-0.924298,4.369148,0.670414,-5.996423,-2.494283,-2.730040,7.554234,4.522214,0.747651,-9.248658,2.030141,-9.117703,-8.308221,-0.691195,9.042285,-2.731025,3.021604,-2.635912,8.705670,-1.359797,-3.815261,-6.340044,-4.196935,7.657182,-4.852024,7.680793,-8.714801,-1.164196,1.946695,-9.470722,8.988868,-0.678079,-1.745005,2.820664,5.825795,9.420357,-2.132859,-3.463399,2.223878,-4.501921,6.579320,8.988481,5.553376,-9.658532,-8.011166,7.304402,8.676734,-5.406956,-6.236668,-7.672812,9.870087,-9.238283,8.870214,-5.844574,-6.535768,-4.653765,-4.977376,-6.824340,1.333675,-7.401160,8.840651,7.253369,9.677263,-1.478995,3.667149,-7.094883,-4.034531,-8.480132,4.804256,4.011200,2.438785,8.818095,0.335131,6.743993,-4.948640,8.056717,5.736818,-1.426148,-9.519049,2.242136,9.598325,6.462017,-5.525026,0.926998,-6.210389,6.694366,-4.630729,-2.760601,-7.336600,0.933116,3.027134,-2.733616,5.134115,-0.527411,2.166721,-0.813742,8.875492,1.037855,3.067726,0.405251,4.145342,-0.579724,8.918561,5.919230,-4.053385,-3.749626,8.171973,5.086421,7.505877,3.184215,5.150814,-0.796208,5.853462,-0.632247,-4.632280,-9.586618,-0.467963,-5.301265,8.354215,-7.543398,-1.878514,-8.270333,4.878087,-0.040245,1.770265,-2.220878,5.313659,2.409347,-1.640190,-0.241581,0.203328,-7.607816,5.621545,8.587063,-2.777807,-5.679030,-4.075712,1.303261,-4.202228,-3.018034,5.369575,-9.201061,0.485030,7.533451,0.304020,9.729060,-6.267934,3.197010,-1.275783,5.228478,-4.241939,0.305832,-2.093221,-9.377372,-4.258184,-4.109018,4.893729,6.369805,-2.060255,-6.239152,-1.212493,-4.456278,7.547661,-0.529397,-3.388282,0.362831,1.492037,9.162232,1.539000,6.590591,-5.484822,9.943466,-9.370210,5.025833,7.402921,5.060449,0.332298,-9.954694,5.802538,-0.376186,-9.573551,-1.572181,-1.278942,3.961247,8.581544,0.320111,-4.221382,-6.178501,4.203364,6.777435,6.169195,-9.704018,-3.705080,-8.046021,3.236454,8.773679,-2.101313,-5.290327,6.039834,-4.906455,-7.008978,2.507284,-5.600209,9.215764,7.359334,-8.269722,8.957028,8.262742,3.009097,7.576802,-7.327864,5.422301,-6.455821,8.323542,1.175708,1.777767,5.944560,8.153020,-0.572645,-2.582290,6.720148,-9.578065,3.458572,9.255093,9.648067,-3.949526,3.169736,-2.481958,0.792689,-2.076703,5.667473,-7.528625,-1.785107,-6.868094,-9.672306,-0.296770,8.221651,9.164321,-5.394821,-0.008120,7.766371,3.045601,-2.436092,3.342707,9.971267,-3.066493,8.944782,0.272146,-1.288250,-5.325096,-7.753911,5.527062,7.551961,8.818836,5.114990,-7.895819,-1.428055,9.956943,0.134224,-0.327637,-4.898045,-8.307216,9.795071,6.193655,4.706638,-7.055435,-6.469194,-5.717812,-3.630527,5.515225,8.019782,6.069860,4.259800,-3.236568,7.415280,2.877798,6.606326,6.183512,-6.219535,3.909284,-3.966581,0.554947,0.954793,-0.612856,1.898634,6.989530,7.861108,-1.685848,1.748748,-2.092130,4.692055,5.519402,5.379935,4.193977,4.516533,6.530362,1.262576,0.367342,-7.641755,-5.763378,1.590388,-3.941640,-2.045134,-0.203571,1.547808,-1.650319,-6.678738,-4.795590,-0.925863,8.311926,-0.559108,1.224669,-4.928000,-9.427476,3.985096,-3.818900,-5.528975,4.751912,-7.060410,-1.493424,-8.339159,-4.274323,-6.954090,-1.529906,2.579985,9.621680,9.228802,9.256632,5.320646,-5.559710,-8.973869,8.770068,-9.450508,-0.330603,-8.155517,-2.538797,1.535516,-1.522261,3.920745,8.128496,-2.517706,-1.394949,6.803153,1.633425,4.989605,0.967147,1.531111,-1.036256,-0.474785,-4.676272,-2.075106,0.085821,6.305510,8.023854,4.944976,7.568594,4.366296,8.418852,5.637247,9.259651,-2.475906,0.512944,-1.345707,3.452582,-3.398603,7.385954,3.480703,-1.554653,-1.294346,8.684181,-5.170297,-4.147677,6.331362,6.098881,-7.631244,2.550332,8.290155,-8.139595,6.964869,-9.563838,0.833535,-5.126083,2.116830,-5.033078,-5.046971,6.319640,-4.137297,3.885819,3.486636,1.930473,5.488875,-6.060277,5.522114,-3.239719,6.064356,-3.974838,4.101297,1.873232,1.809001,-7.387906,9.080773,7.740588,7.869052,9.877216,4.873545,1.363597,-7.005984,3.062754,-1.096454,-3.679497,0.656049,0.319546,2.165422,7.773390,-0.966984,-8.286260,7.580699,5.983481,-4.965628,3.901500,3.325588,1.989208,-5.005874,8.545533,-0.457304,-2.675023,-8.988203,-5.023937,-2.035157,8.532610,-1.760963,4.519255,2.170308,-2.020606,6.284150,4.698166,-8.095869,-7.878184,1.682983,-2.420490,4.916306,5.133940,-7.892258,8.625515,8.954407,4.638235,4.058595,7.379890,2.475436,-2.738162,4.958872,-2.795908,-2.357903,1.484011,-6.192001,-2.142146,-4.528196,-4.823040,6.431958,-3.398100,-3.417292,-7.168262,-9.988166,-5.801783,-7.063944,-9.059306,-9.407801,5.447577,-9.030870,-6.647555,-9.984310,-1.896864,8.135775,9.372317,0.318114,1.372910,8.499337,9.855935,-3.423927,-3.661748,-7.870997,-2.910680,5.564406,-7.602810,-9.602540,-7.879235,8.844037,-6.663212,1.237096,5.825351,6.328789,-3.109469,7.039574,-4.237869,6.380507,-6.356225,8.162690,-6.014564,-0.379675,-0.898257,-9.114870,-2.977659,-3.357757,-3.953939,-6.208777,-1.240262,-6.323850,3.965555,-4.298920,7.356102,-3.951097,2.291150,7.389973,-4.515489,-7.774176,-0.821616,7.936801,-3.447673,0.204064,-9.528438,8.697743,8.623731,5.012319,1.245788,-2.471080,-3.024996,-0.906838,3.427634,1.078398,1.770864,-3.793059,-0.516630,-4.511875,6.267286,8.151987,-9.912627,-1.369395,7.736442,-6.732555,2.038661,3.116202,4.518320,-1.905317,8.085110,-2.882879,5.001618,1.341556,-0.329173,3.458209,3.735669,6.656301,7.167541,-9.705994,-3.625870,3.371909,5.606457,0.067359,-2.390645,8.998681,5.349766,-9.436721,6.210458,9.723992,-5.629571,6.272893,5.534198,4.232088,3.357380,9.084999,-8.001331,1.492536,-5.544785,-8.726591,-0.467674,-8.257763,1.413002,1.563126,-5.167271,-3.247166,1.193903,9.333021,4.709157,3.190272,-0.399288,-5.205381,1.833795,-4.873582,-2.628621,-5.821528,4.250030,-9.144360,2.145341,9.703036,-0.685955,-4.985482,4.761652,0.844752,-6.427838,6.394673,8.647543,4.477877,-0.176535,-8.485899,-3.055310,0.744957,-9.297349,-3.098747,5.497937,2.784147,-3.932615,0.338717,8.525628,-9.059572,1.349412,-1.551913,1.304990,6.142250,-5.357858,-8.719251,-0.088789,-4.609014,1.340924,5.667234,-8.727418,0.995468,-3.075790,-6.489901,6.357548,-9.214459,6.933586,9.367436,-6.652929,-1.116900,8.856224,-2.307210,-7.927332,-8.055688,8.954089,2.172948,-5.299187,-7.562864,6.599817,1.386346,0.828575,-0.114956,-2.616840,9.038832,-1.579999,2.625373,-2.795930,-8.054599,-4.811598,4.495826,-2.275572,2.530169,6.584519,4.544726,0.275476,0.155273,-5.405644,7.024268,0.657767,-5.210967,-1.646948,8.073833,3.510664,3.657026,-4.469289,0.906862,9.112638,-3.345783,4.622220,-1.451150,-6.038242,4.882643,1.097356,7.499406,-8.642254,-8.143786,-9.060009,3.313916,6.731613,6.983205,4.216892,-6.572482,-7.315731,2.459218,0.701982,-3.668984,3.320745,-7.683756,-8.096884,-0.557344,8.550012,0.338554,-8.277194,7.048677,8.678458,-8.679198,-1.815883,-4.064778,1.129576,-1.489089,2.647137,-4.242223,-0.578464,8.724649,-8.559334,2.694610,-5.773558,5.416954,-4.041313,6.128551,-4.213780,-6.215121,-1.879021,9.358058,0.781746,-9.644027,-2.679723,6.386964,-0.630416,1.240417,-6.753092,-5.261253,7.338286,-2.266069,6.086951,7.434923,5.884004,-7.005778,-9.634259,3.578658,4.171469,-7.543830,-9.018897,-9.898016,-6.738860,9.777908,1.336277,-4.895179,-7.758189,-7.507035,-2.704581,6.467322,0.036613,5.896322,0.858649,6.787452,7.571627,-9.400240,-0.373107,-6.462185,-3.843991,8.627066,9.992911,-1.132668,-8.418487,0.332404,-0.650456,-9.518013,-2.966205,-3.188541,-0.822397,-0.476995,2.509523,6.975710,-0.484281,9.674443,-1.701490,-3.359850,-7.969832,6.339852,1.866320,1.686987,8.154343,7.561319,8.329149,3.265410,-9.188699,8.594286,-8.099796,9.959603,-6.206481,0.260458,3.818303,5.177743,-3.773575,5.647071,4.339328,8.331631,-3.411561,8.730415,-0.680202,-5.930889,-9.596580,3.967009,-5.897792,8.387425,3.847406,0.366227,-6.071805,-1.944596,3.362014,-2.573173,-2.409645,6.736018,1.163793,-4.571760,1.007533,-7.312512,6.738442,-3.395678,-6.613216,-3.972918,-3.049327,-7.016498,-2.315855,5.621312,-8.824311,7.479385,-1.590182,-4.441772,2.895448,0.436042,9.664312,-6.472058,4.214709,-6.496927,5.328732,8.301583,3.774216,-5.437837,-2.692219,5.240666,-8.531651,4.864547,-5.012844,-1.143691,8.041891,-7.317538,0.371491,3.349949,-0.560123,-8.843854,-8.462663,3.660721,9.458475,-9.347451,-3.885826,7.777425,-0.513221,2.081663,-6.677137,-6.285125,9.179754,-3.826091,0.076248,-2.626173,5.566617,9.146757,-5.160373,7.063872,8.100552,-4.178673,-0.718166,-8.525318,-2.884578,0.920243,0.878188,-2.309847,-6.615701,1.987559,-0.715649,5.065564,-3.935498,-7.438524,-9.846171,-3.920907,5.146532,1.689078,-3.944569,-1.919785,0.022062,7.554816,5.954221,1.695446,-6.336132,1.499104,-0.607290,5.250524,-3.117545,-0.037931,5.380052,-3.230560,8.087888,-0.731955,1.452393,-7.968361,-7.223655,9.989572,-1.421953,-4.843628,8.109964,4.975272,-5.186041,-7.887355,-8.827963,2.889933,0.391538,-1.534941,7.692849,3.134642,5.339932,3.918647,8.211719,5.596703,-3.815364,1.557424,-9.085749,4.364693,3.713629,5.612278,-2.597988,6.884621,-3.464498,-0.617151,0.027665,-3.144199,-6.677153,-5.170126,-3.210790,3.583762,6.687683,-2.820988,3.904912,5.595263,9.104081,4.004089,5.566956,6.997850,-8.449954,-4.897819,1.266976,4.203637,-1.983108,-8.104624,4.110554,7.910181,-4.336029,-2.805067,-5.925985,-8.877580,-2.697611,4.057940,-2.928473,8.764095,8.456896,-8.475169,-9.515805,-3.332939,-9.756637,0.955094,-5.412590,-2.195956,-5.325634,-4.703304,-3.057618,-4.820992,-3.550872,2.921718,4.032762,-3.839010,-5.330222,8.594563,-2.306218,0.974907,-4.836895,-4.319877,-9.021074,5.281243,-5.090444,7.576841,-7.232271,8.336412,4.108328,-9.207342,-7.364548,6.245916,0.478781,2.686280,-7.651772,-6.799988,-3.040797,6.939677,-8.630526,8.391214,7.455406,9.972510,2.558941,-1.592217,2.720409,3.125362,8.417809,-1.939292,6.539452,-1.130857,4.898302,1.903662,-8.452761,-4.735017,1.380284,8.313141,-2.467833,3.866099,5.175768,-3.639338,-0.285770,-8.787104,0.249675,-9.836236,7.809280,-4.405597,-8.911558,-7.129312,4.121428,0.626889,-7.939197,7.370921,2.017252,-3.902312,-4.894367,-4.551113,-7.714349,5.883402,5.785620,5.168851,-0.691182,4.384764,8.100349,2.814569,-6.564422,7.320584,9.106792,7.934736,1.155462,-0.062546,2.759940,-8.340794,0.089657,9.427359,-8.251602,0.766509,-6.657871,2.221455,-7.476788,-1.427531,7.487232,-2.469440,-4.897563,6.447310,3.679045,-5.848838,-2.157493,7.318146,-2.139191,0.781635,7.661876,1.210222,9.503534,5.399611,-1.950764,3.168268,5.530801,-8.988916,9.860138,-2.956090,9.846731,7.435063,3.532966,-7.382024,9.942406,-6.115687,-4.982634,7.649099,-3.002974,-5.155002,-8.006815,-7.810207,9.031797,-6.797507,5.275134,6.907439,0.926130,-8.911233,7.605581,-3.786448,-8.525715,8.774996,-1.651905,6.306595,0.109710,0.696739,1.734181,-4.735110,8.096445,3.524901,4.816507,6.003212,-2.328329,8.106407,-3.181712,-2.628006,7.516702,-8.473768,-6.166213,-1.022292,6.940946,-6.169736,-1.972526,8.210183,3.513276,-3.559983,8.535624,6.233980,3.630900,-2.717437,-3.679358,7.881632,-6.428175,9.510896,1.097349,9.197361,-5.249958,3.459446,-9.811799,-2.328313,3.011119,-2.425808,-0.190221,-3.824308,-4.951434,-9.056025,-4.636873,-6.059303,7.070368,3.891880,-4.846794,7.472266,-9.963135,7.133133,5.540779,-0.165024,-7.018014,2.862439,-7.285900,-3.262562,-1.390919,9.151439,-0.283005,-3.488224,-0.719415,-5.326795,-4.547312,2.289326,-7.685800,0.479723,-9.955504,9.010632,-4.848472,4.923375,-6.427860,0.603963,-1.433878,3.111346,3.944860,-7.263577,-2.598518,-9.427331,-8.091244,5.147630,-5.985026,-2.652033,9.229201,2.921085,2.668666,-7.437830,-6.881070,-9.383041,9.476897,-5.027146,2.892592,-3.640073,3.374291,-5.315617,-9.404373,2.053585,-7.415740,9.847199,3.770827,5.442229,0.605732,-2.954966,-3.294599,8.948038,4.629495,-9.734055,-6.859573,-9.849543,1.754285,-1.309067,-6.736041,-8.193560,3.718510,-6.307225,-0.665285,0.013347,-3.394174,1.820246,7.316499,-6.338827,-5.401669,0.139191,1.967142,7.104672,6.616674,-1.700777,5.110101,-4.924227,-3.455271,1.619916,2.490398,-4.194151,-6.651437,-1.385331,-8.662825,-4.732668,9.975071,-3.350294,7.538558,8.605933,6.603133,4.890794,-3.313750,0.137387,-2.101569,1.822205,-9.620735,0.119285,7.136215,-2.941088,-3.896903,5.372770,-4.097088,-9.695783,3.169846,-1.314022,3.380646,2.262545,-0.009473,-1.929625,6.384737,-8.332358,-1.404468,-9.114744,2.713157,1.587521,-8.752093,3.850916,-6.104511,-1.619178,4.745045,-8.258567,-1.047051,-9.928936,8.156268,-6.800842,-3.764202,-3.760265,-3.993399,-1.879605,5.892661,-1.750877,-3.211495,-3.669668,8.748447,-0.354436,-1.570069,-3.783646,-2.638780,6.692955,1.721180,-4.128999,-3.262013,-1.743878,-0.742662,-2.921644,1.482440,8.062417,-4.483384,-8.526107,-4.160204,-8.960186,-8.343639,-9.566684,0.806206,-3.794863,1.139306,-4.718168,1.078801,-9.551493,3.371514,9.679524,8.897667,7.959848,-9.558434,-8.447399,-2.855282,3.904162,2.729509,-9.489426,7.957317,2.865970,0.356334,-9.296476,9.616736,-0.953639,5.783929,6.345163,-7.613127,-9.225358,-1.759751,-4.579553,7.646383,9.589940,7.321192,5.059672,-6.676415,7.779201,-7.257902,-0.698901,-8.104216,7.624131,-6.212662,9.155413,6.137498,-2.889681,-4.681693,-7.059368,-3.662452,-9.172032,0.722638,1.380543,-8.108086,-0.531362,-1.756951,-4.619455,0.117317,2.099946,-1.979635,0.130902,-1.512654,-5.896597,-9.758877,2.200954,-0.284537,-4.635459,5.614430,-0.052988,-8.532931,1.694612,9.012609,3.553662,5.681024,8.780066,7.812411,5.711404,-5.655402,-6.858739,-6.614533,2.442318,4.785953,4.013786,4.021684,1.306331,-8.108021,7.879117,-8.880912,-5.605578,1.659641,-2.264508,-7.516034,-1.926822,6.450359,5.724710,-5.997945,-6.657901,-0.589577,9.790266,5.959329,7.614820,9.647360,-3.359321,-1.348906,2.301833,-9.469673,-3.089196,3.848002,1.023201,-1.054852,-4.552530,5.915763,-8.154241,-6.190617,-7.014806,-7.266740,9.588673,-3.089855,-5.463950,7.657846,-8.118648,6.597611,-5.451294,2.702787,4.340949,0.073892,8.591992,-4.490461,-3.933378,9.059107,5.565929,1.000972,5.414287,-6.238238,-9.244448,8.496009,7.704419,3.091915,0.089861,6.797316,-9.887930,-1.498435,4.200501,-5.719505,-3.809831,-5.816281,6.031554,-1.163411,0.770239,-5.555316,-6.203000,-9.884001,-1.122811,-8.192194,3.334402,-3.131745,-2.176731,2.141685,-7.667395,5.102636,8.788703,-5.023416,0.096653,1.033118,2.047285,-8.771450,8.939419,8.976129,6.450331,0.083387,4.606296,-3.267453,-1.465890,1.547984,9.260010,5.877528,7.891874,-9.836181,2.318516,2.518964,4.767176,-4.494738,4.496869,4.697984,4.840790,3.275950,-6.419470], dtype = "float32")#candidate|5063|(2288,)|const|float32
call_5057 = relay.TupleGetItem(func_3852_call(relay.reshape(const_5058.astype('float32'), [13, 7, 3]), relay.reshape(var_5059.astype('float32'), [1, 462]), relay.reshape(var_5060.astype('float64'), [180,]), relay.reshape(const_5061.astype('float64'), [80,]), relay.reshape(var_5062.astype('float32'), [35,]), relay.reshape(const_5063.astype('float32'), [2288,]), ), 10)
call_5064 = relay.TupleGetItem(func_3860_call(relay.reshape(const_5058.astype('float32'), [13, 7, 3]), relay.reshape(var_5059.astype('float32'), [1, 462]), relay.reshape(var_5060.astype('float64'), [180,]), relay.reshape(const_5061.astype('float64'), [80,]), relay.reshape(var_5062.astype('float32'), [35,]), relay.reshape(const_5063.astype('float32'), [2288,]), ), 10)
output = relay.Tuple([call_5050,call_5057,const_5058,var_5059,var_5060,const_5061,var_5062,const_5063,])
output2 = relay.Tuple([call_5051,call_5064,const_5058,var_5059,var_5060,const_5061,var_5062,const_5063,])
func_5067 = relay.Function([var_5059,var_5060,var_5062,], output)
mod['func_5067'] = func_5067
mod = relay.transform.InferType()(mod)
mutated_mod['func_5067'] = func_5067
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5067_call = mutated_mod.get_global_var('func_5067')
var_5069 = relay.var("var_5069", dtype = "float32", shape = (462,))#candidate|5069|(462,)|var|float32
var_5070 = relay.var("var_5070", dtype = "float64", shape = (180,))#candidate|5070|(180,)|var|float64
var_5071 = relay.var("var_5071", dtype = "float32", shape = (35, 1))#candidate|5071|(35, 1)|var|float32
call_5068 = func_5067_call(var_5069,var_5070,var_5071,)
output = call_5068
func_5072 = relay.Function([var_5069,var_5070,var_5071,], output)
mutated_mod['func_5072'] = func_5072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_5145 = relay.TupleGetItem(func_4610_call(), 0)
call_5146 = relay.TupleGetItem(func_4611_call(), 0)
output = relay.Tuple([call_5145,])
output2 = relay.Tuple([call_5146,])
func_5147 = relay.Function([], output)
mod['func_5147'] = func_5147
mod = relay.transform.InferType()(mod)
mutated_mod['func_5147'] = func_5147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5147_call = mutated_mod.get_global_var('func_5147')
call_5148 = func_5147_call()
output = call_5148
func_5149 = relay.Function([], output)
mutated_mod['func_5149'] = func_5149
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_5207 = relay.TupleGetItem(func_5147_call(), 0)
call_5208 = relay.TupleGetItem(func_5149_call(), 0)
func_4874_call = mod.get_global_var('func_4874')
func_4877_call = mutated_mod.get_global_var('func_4877')
const_5219 = relay.const([4,-6,1,8,1,-8,-9,-2,-8,-8,-5,-8,9,6,-10,2,8,8,-3,-3,-6,-7,5,10,8,-4,-4,2,2,5,-8,6,2,5,2,4,-10,3,-8,-9,-2,9,-5,-7,2,9,-10,-8,-2,-10,1,-2,-2,-6,-1,-9,10,-9,3,-2,-2,5,-7,-2,3,3,7,5,-2,2,-8,6,-10,-4,5,-6,-6,-6,-3,4,-4,2,-4,-9,-9,-10,3,-4,-3,8,4,-4,6,-7,-10,-6,10,6,-6,10,7,2,-6,-4,7,-8,5,-5,-3,1,5,-10,9,7,-10,-1,-7,-8,3,3,-4,-5,4,-2,-2,10,2,2,-5,-7,6,-1,-2,5,1,-7,8,5,-2,8,-10,3,8,3,2,8,9,8,-10,-9,10,7,-8,1,9,-5,-10,3,2,3,8,-4,3,-8,-7,-6,-3,-7,7,-2,-1,-7,3,-1,8,1,-7,4,-8,-5,-1,2,-7,-6,10,1,3,2,-8,3,7,3,-10,4,-1,-3,-3,8,-7,-4,-10,-8,-3,-9,3,8,-7,-2,1,-6,-6,-7,-7,8,-7,3,-7,2,-1,-2,4,-4,4,1,3,-8,-8,9,9,-1,10,-6,7,9,-1,-4,-3,-6,-4,2,4,-8,6,2,-5,-4,9,3,7,3,5,3,-6,6,-7,9,10,-6,5,2,10,-4,-5,4,1,10,-9,-5,-3,6,9,3,-5,6,8,-9,-1,9,1,7,-3,9,1,8,5,6,-1,5,-8,5,8,-6,6,4,9,3,-10,5,-6,-7,-6,9,2,3,-7,-9,2,-4,1,8,-9,5,3,3,4,4,-3,-9,-9,8,-1,-2,2,-3,-6,-2,-2,-4,-6,8,-7,10,-7,8,3,5,2,-7,3,-7,1,-4,6,-1,7,4,4,-7,-5,9,10,2,-1,-8,8,-3,-5,-5,-7,5,8,9,3,2,-10,6,7,3,6,4,9,5,4,-4,6,6,-9,7,10,2,2,-9,-5,-7,-8,-2,-8,-10,7,-7,5,1,6,-8,5,6,7,8,-10,2,8,4,1,10,7,-4,-9,-8,1,3,5,7,7,-5,-10,4,1,4,1,3,-1,2,-2,-7,6,2,1,5,-3,-4,7,9,-5,1,6,8,1,-9,10,-7,-8,-10,-6,-5,-7,-2,-7,6,5,-10,1,10,7,6,-7,-6,10,4,-2,5,-7,6,9,8,9,-4,-7,2,-6,-3,-1,-8,4,-9,10,-6,2,-3,-5,-2,10,-5,-4,4,7,-3,-6,-1,10,9,-3,-6,-8,-3,-9,-7,3,-9,3,7,1,-10,10,1,9,-1,-4,7,-6,-5,7,6,-6,-9,10,-10,-7,-10,-2,-10,-3,-5,-5,-9,5,8,7,-4,-8,-3,10,-1,-6,5,-4,-8,5,1,6,-3,-5,-2,2,7,-6,10,4,2,-4,7,-3,2,8,8,-7,-4,-9,-5,10,-4,-2,2,-8,5,5,-10,7,-6,7,-9,-6,-7,7,7,3,6,10,1,-4,9,-8,-8,1,2,-10,4,-3,-1,2,10,1,-1,3,10,8,-9,-8,-3,-2,9,-5,-8,-6,9,-8,3,2,-2,-6,4,-2,10,1,1,8,5,-4,2,-3,10,-9,-3,-9,-7], dtype = "int64")#candidate|5219|(624,)|const|int64
call_5218 = relay.TupleGetItem(func_4874_call(relay.reshape(const_5219.astype('int64'), [24, 26])), 1)
call_5220 = relay.TupleGetItem(func_4877_call(relay.reshape(const_5219.astype('int64'), [24, 26])), 1)
func_1033_call = mod.get_global_var('func_1033')
func_1038_call = mutated_mod.get_global_var('func_1038')
var_5236 = relay.var("var_5236", dtype = "int16", shape = (168,))#candidate|5236|(168,)|var|int16
const_5237 = relay.const([-6.873066,-1.227360,-6.428593,-8.574246,-2.599368,4.714084,-1.299749,5.688311,-8.098335,5.382441,1.095732,-1.688478,-2.874058,-8.488450,-3.648416,-5.235370,-6.396388,5.089718,-4.356693,-6.545070,-4.718072,2.076838,1.797881,3.193268,-3.181903,2.797137,6.112887,-7.588443,0.200221,0.392082,-3.228275,-7.677269,-3.508224,0.564241,3.919858,0.568925,-5.655789,-6.358338,4.298220,5.715778,1.339613,2.584924,0.995611,-6.449246,-5.480108,-5.503896,-8.017874,9.321825,-0.851622,1.739391,-5.082506,8.296635,-5.919930,-5.013904,-5.518445,6.443113,-0.149414,-7.912060,8.306062,-9.916829,-6.593294,-5.436691,-9.021895,3.105177,2.021199,-1.112629,3.243833,-0.459948,-7.002896,9.852501,-0.234966,-9.631189,9.999613,-5.390529,2.702851,-1.592856,1.416845,-3.109418,5.706945,-0.073752,4.260760,-2.166679,6.590762,-3.557964,-5.529172,-3.579881,-7.021676,6.047766,3.465937,-1.844539,4.054014,-0.448163,-2.597548,-1.460285,-1.024427,-8.118679,9.278726,-1.038529,1.802837,-4.375015,-5.418695,-8.997280,7.721959,-4.275385,-1.895271,-0.567753,2.791906,-4.858037,2.181694,3.026062,-9.464104,3.634698,7.318867,-4.981638,-2.320942,-6.073201,5.476942,-1.860414,-8.809568,5.983456,7.572242,-5.743547,-7.150591,-8.694552,3.831446,5.731165,3.279197,-1.257859,-6.648076,9.082524,2.721870,0.928531,8.242959,-6.457982,-9.387744,-6.396026,6.101974,-2.874890,2.423339,2.525831,0.374580,-8.944216,-8.987348,0.105942,8.946554,5.165845,-2.373447,6.894408,-5.254863,5.149884,9.545913,2.714060,4.004154,-3.413266,-6.710251,8.188752,-9.408546,7.452342,-7.320729,8.726322,3.369808,3.123777,7.295589,5.134906,-7.061486,-2.455905,-8.663229,-7.764235,-7.096233,9.605049,-7.561730,-2.467697,-6.301066,8.455625,-2.851780,1.861668,-9.831066,4.559877,9.483372,3.653222,7.715561,-6.946517,3.058729,7.144407,0.703237,9.081628,-3.148191,3.019776,2.476519,9.877489,0.930026,8.945788,7.866669,-9.117315,-3.348455,-1.997473,1.373385,5.325996,9.196541,-4.315736,6.616270,3.305987,2.343702,0.767606,4.729043,-6.495430,4.489467,-6.943393,-2.377744,7.073834,9.240518,5.971728,-5.924829,9.720480,6.178951,0.335255,1.034604,-8.873392,2.403866,6.301588,2.957614,1.667912,-4.013035,0.579370,-5.618663,7.945162,7.999236,7.004003,4.808133,3.810983,-1.469870,-3.235096,6.410096,5.595305,-2.951176,-2.030627,-9.439225,-7.459766,2.179327,-2.486093,-2.224844,8.340683,-2.777828,-0.522601,-9.852621,-7.035345,-0.885894,-4.554575,-0.077834,-4.442471,6.864727,-5.246533,-4.328260,-0.490066,-6.848994,-1.559002,-0.114751,-9.656207,-5.701691,-6.525543,7.428110,8.740721,0.082657,0.392846,4.892427,-7.057978,-9.949971,1.425045,1.332325,2.257994,-8.892499,6.300506,2.559842,9.441078,-3.626186,-4.324170,-5.491731,4.898505,-2.347414,6.446837,-3.968479,-4.548557,-9.816930,6.426741,1.652062,-3.135727,-1.639610,-9.413173,0.365886,6.611294,9.759582,4.542239,-2.123631,-0.519835,-9.673658,-4.075343,7.546412,1.293171,-9.692507,-5.281259,8.816385,8.662522,-1.135781,-9.296851,4.058277,5.931905,9.374290,4.105825,3.790850,-7.501700,9.459648,-9.956712,2.804691,0.970299,-9.918035,8.840824,-7.666739,-4.672765,-6.080605,-3.475785,-7.758938,6.703750,4.451972,5.353151,-2.522013,-8.472618,2.911351,-4.196403,-5.142049,-1.942077,0.097329,6.028694,7.095509,-7.935502,-1.438082,9.746548,-6.167147,-7.684700,9.504156,-4.676440,-3.643788,-4.461539,4.473611,-1.452602,-6.017553,3.760113,1.544778,4.099537,-0.797323,-2.409690,-6.536919,1.861786,-0.616456,-5.272020,-7.527405,8.289056,9.977830,-2.748784,0.922951,1.716559,0.819647,4.904048,6.815157,2.067063,9.364881,-1.987518,-6.767016,-0.214067,5.528384,-2.214659,-7.438452,-3.447383,0.957781,-7.505647,-0.022315,-4.517154,-8.434509,-5.780146,-0.341662,4.079617,1.820186,-5.652672,-3.564357,9.067678,1.203687,9.050730,4.590529,-8.045483,-9.794389,7.900112], dtype = "float32")#candidate|5237|(390,)|const|float32
var_5238 = relay.var("var_5238", dtype = "float64", shape = (3, 60))#candidate|5238|(3, 60)|var|float64
call_5235 = relay.TupleGetItem(func_1033_call(relay.reshape(var_5236.astype('int16'), [14, 12, 1]), relay.reshape(var_5236.astype('int16'), [14, 12, 1]), relay.reshape(const_5237.astype('float32'), [390, 1]), relay.reshape(var_5238.astype('float64'), [180,]), ), 0)
call_5239 = relay.TupleGetItem(func_1038_call(relay.reshape(var_5236.astype('int16'), [14, 12, 1]), relay.reshape(var_5236.astype('int16'), [14, 12, 1]), relay.reshape(const_5237.astype('float32'), [390, 1]), relay.reshape(var_5238.astype('float64'), [180,]), ), 0)
bop_5241 = relay.power(const_5219.astype('float64'), call_5235.astype('float64')) # shape=(14, 12, 624)
bop_5244 = relay.power(const_5219.astype('float64'), call_5239.astype('float64')) # shape=(14, 12, 624)
output = relay.Tuple([call_5207,call_5218,var_5236,const_5237,var_5238,bop_5241,])
output2 = relay.Tuple([call_5208,call_5220,var_5236,const_5237,var_5238,bop_5244,])
func_5245 = relay.Function([var_5236,var_5238,], output)
mod['func_5245'] = func_5245
mod = relay.transform.InferType()(mod)
mutated_mod['func_5245'] = func_5245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5245_call = mutated_mod.get_global_var('func_5245')
var_5247 = relay.var("var_5247", dtype = "int16", shape = (168,))#candidate|5247|(168,)|var|int16
var_5248 = relay.var("var_5248", dtype = "float64", shape = (3, 60))#candidate|5248|(3, 60)|var|float64
call_5246 = func_5245_call(var_5247,var_5248,)
output = call_5246
func_5249 = relay.Function([var_5247,var_5248,], output)
mutated_mod['func_5249'] = func_5249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_5299 = relay.TupleGetItem(func_5147_call(), 0)
call_5300 = relay.TupleGetItem(func_5149_call(), 0)
output = relay.Tuple([call_5299,])
output2 = relay.Tuple([call_5300,])
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
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_5327 = relay.TupleGetItem(func_4610_call(), 0)
call_5328 = relay.TupleGetItem(func_4611_call(), 0)
output = relay.Tuple([call_5327,])
output2 = relay.Tuple([call_5328,])
func_5333 = relay.Function([], output)
mod['func_5333'] = func_5333
mod = relay.transform.InferType()(mod)
output = func_5333()
func_5334 = relay.Function([], output)
mutated_mod['func_5334'] = func_5334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_5347 = relay.TupleGetItem(func_5036_call(), 0)
call_5348 = relay.TupleGetItem(func_5037_call(), 0)
output = relay.Tuple([call_5347,])
output2 = relay.Tuple([call_5348,])
func_5351 = relay.Function([], output)
mod['func_5351'] = func_5351
mod = relay.transform.InferType()(mod)
output = func_5351()
func_5352 = relay.Function([], output)
mutated_mod['func_5352'] = func_5352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_5364 = relay.TupleGetItem(func_4610_call(), 0)
call_5365 = relay.TupleGetItem(func_4611_call(), 0)
output = relay.Tuple([call_5364,])
output2 = relay.Tuple([call_5365,])
func_5366 = relay.Function([], output)
mod['func_5366'] = func_5366
mod = relay.transform.InferType()(mod)
output = func_5366()
func_5367 = relay.Function([], output)
mutated_mod['func_5367'] = func_5367
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_5395 = relay.TupleGetItem(func_4770_call(), 2)
call_5396 = relay.TupleGetItem(func_4772_call(), 2)
output = relay.Tuple([call_5395,])
output2 = relay.Tuple([call_5396,])
func_5410 = relay.Function([], output)
mod['func_5410'] = func_5410
mod = relay.transform.InferType()(mod)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5410_call = mutated_mod.get_global_var('func_5410')
call_5411 = func_5410_call()
output = call_5411
func_5412 = relay.Function([], output)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_5416 = relay.TupleGetItem(func_5333_call(), 0)
call_5417 = relay.TupleGetItem(func_5334_call(), 0)
func_3852_call = mod.get_global_var('func_3852')
func_3860_call = mutated_mod.get_global_var('func_3860')
var_5445 = relay.var("var_5445", dtype = "float32", shape = (273,))#candidate|5445|(273,)|var|float32
const_5446 = relay.const([1.055572,4.338793,-8.634658,-8.049117,-2.997778,-9.775082,4.483407,-0.548361,-8.758692,0.871194,-5.158092,-5.370641,-7.838036,-1.301299,5.350258,2.614433,8.361216,-1.581940,2.618511,8.530647,8.944737,0.747604,6.737869,9.607977,8.963432,4.833773,-1.356870,4.812195,1.115321,-7.723480,-0.872865,9.014494,6.449990,5.028600,6.544131,-8.615047,-2.682330,9.376961,-5.718117,6.167118,6.899552,7.941317,-9.604622,-1.122127,-6.286443,0.524190,-9.418975,-1.156386,-0.135949,-5.593356,-6.894197,-3.606683,5.723060,2.350309,-1.991102,1.151579,3.107109,2.971132,0.467296,-7.201515,3.028582,-1.228323,-8.266330,3.603416,-2.682381,-3.816685,-0.638860,9.670453,-7.423591,0.017281,-5.001120,-3.199211,0.346080,1.973203,9.753863,-7.557156,2.725016,-3.180931,2.369256,-0.911774,-2.716807,2.343547,-6.864346,-2.238241,9.210066,4.802883,-2.875851,1.144805,-2.767336,7.243180,-6.181539,-0.421939,-9.545864,-3.043449,-2.343562,-2.584534,2.560940,6.550806,-7.942965,4.018184,-2.724704,4.874145,-4.996242,-7.619028,-9.127017,5.407586,-0.472210,-5.648462,-6.714432,-3.020498,-3.083215,7.768459,-0.097538,2.604698,-3.173440,-0.568788,8.215158,-9.870213,7.622633,-3.882310,-3.634989,-7.446177,6.799413,3.268035,8.542566,-6.214416,-2.689754,-3.805963,0.546648,-9.685990,-6.835855,-6.804441,-7.509891,6.946669,1.721051,8.514520,3.347723,-9.186397,3.440698,7.495319,-2.038423,-5.451416,8.278263,3.132050,-4.729016,6.442181,0.314485,-5.487716,-6.938668,2.339362,-7.349451,0.432896,-0.833992,-4.294444,9.253318,8.170773,-4.981558,3.377340,-3.212925,-7.813233,-1.748664,4.193061,9.404063,2.853233,3.469341,8.440012,-3.791144,-1.191679,5.971795,-7.453287,-7.265904,-4.505769,2.086177,-6.168238,-3.994169,-5.471485,-5.804855,-5.018178,9.889763,5.480275,-6.083545,-7.629069,1.814030,-6.485518,-3.390513,-7.792714,-1.123706,6.484887,-5.793957,7.436326,-1.681273,0.835040,3.352199,-2.386286,8.657776,4.858199,-4.132303,-6.023676,-1.403181,-7.547857,8.666695,1.141263,9.224458,0.876466,3.653646,9.459613,-8.438892,-6.202811,-2.003004,1.560171,4.456436,-9.325552,-3.985182,1.765013,3.020809,3.801418,-3.676354,-9.453811,2.926298,3.449087,-2.985816,-4.670206,9.379857,-3.615706,2.487856,-3.928331,-1.053960,5.114235,1.169010,-1.257304,-2.912504,-5.289597,-1.703462,3.565700,-9.565346,-3.435362,0.204801,-6.865177,-2.726723,-4.156773,-7.931781,-2.184957,1.913665,0.717966,-9.927824,0.641452,-4.245040,-8.067005,-5.585107,-6.339784,-4.625012,7.932605,-9.181065,5.262004,-4.363914,-6.664067,-2.817610,-6.786778,-7.362603,-5.309101,5.346357,-7.847844,9.063938,-0.953497,-2.777750,0.150105,-4.160218,-0.542833,-4.729952,4.844070,6.129628,6.765178,-1.081767,-5.814019,8.748277,6.898856,-9.786195,-4.332807,-9.062470,-4.229806,-7.143635,-0.427410,-2.138615,3.390975,-7.994969,-3.802026,-4.676884,9.155800,1.513310,-1.134822,-2.022244,6.745621,3.702313,9.863329,-2.717607,-1.042002,5.228852,1.400797,3.052969,-1.865203,9.276154,3.680882,-2.093830,-9.250831,-9.261099,-6.462044,8.315072,-9.789069,-7.820324,-4.827445,4.252745,1.234326,9.795470,-2.111801,6.098079,-7.669172,4.948334,-0.259559,-0.609098,6.700273,2.679230,-4.027433,1.918472,3.725582,-5.864065,8.999166,-9.041667,-6.150984,0.323426,-6.921814,7.836514,-6.988755,9.948629,-5.458308,0.432592,-5.363985,2.318455,7.385330,0.638090,-8.135630,3.526488,0.830227,-0.829006,4.833299,4.634038,-3.049460,0.350868,7.627410,-8.392684,-3.924411,-9.878106,-1.951706,7.789434,-2.255686,9.110348,-1.306554,-7.173216,-4.210521,9.013792,5.378367,-8.609100,7.747544,-1.030917,-0.837362,-0.214158,-2.806415,8.534705,8.506832,0.803861,-8.730117,-0.280729,3.840024,-1.733946,-8.358698,4.795490,-1.798945,9.668279,2.118466,2.450099,-7.909601,4.455646,-4.161192,-8.222941,5.237520,3.693360,-3.845970,3.621598,9.020015,1.195531,0.455500,7.433928,-6.547472,-6.068786,-5.152952,9.446187,8.401250,2.535191,-8.079237,5.442392,1.680533,3.537780,5.091009,4.396464,-9.752305,-0.859406,-2.808226,-8.737817,-8.275187,-8.472826,-5.390342,-4.021727,-1.862351,0.275838,2.927511,7.636539,9.791388,-2.333307,9.291523,9.596990,-0.076424,7.191740,2.229306,-8.693284,-1.304595,-5.464107,-4.971063,1.052741,8.830295,3.458451,7.997055,5.911833,8.607320,4.006094,-9.660522,6.870775,-0.126763,3.919386,-2.506308,-1.670345,-8.132509,4.313303,4.829358,-8.675727,1.921900,5.899821,-5.937367,9.303585,-8.169246,-5.228077,-5.816872,6.076847,-7.814652,-4.007865,-9.424822,-9.306712,-0.508634,-1.188386,-9.376806,-6.628897,-8.754964,-8.583229,-2.078991], dtype = "float32")#candidate|5446|(462,)|const|float32
const_5447 = relay.const([9.926477,4.759677,-8.703766,2.774326,-8.802678,3.578028,6.289293,-5.822234,3.711305,-1.382576,-7.716612,6.387220,0.249200,-7.467272,-5.294489,-6.970249,4.648402,1.468850,7.376669,1.928223,-5.216719,-0.210197,-1.348454,8.519480,2.989843,1.924776,5.779544,2.727341,-2.931599,6.340473,3.439890,6.566884,4.950889,-7.583815,5.876380,-8.342204,4.297223,0.632367,9.840274,4.379674,-1.736948,-8.550094,-2.815043,-3.291736,2.024952,5.517274,9.103650,-3.070245,7.544010,-7.688339,-3.880400,5.923388,9.807023,7.022856,7.573166,-8.575704,7.616105,4.508167,-4.379396,-8.685963,0.347535,-1.721560,-1.550187,8.582535,8.830486,1.205994,-6.095084,9.268091,2.319689,-3.655248,-2.308760,8.494981,3.861533,8.840187,-1.763505,-0.575294,1.131950,2.208129,0.223787,-6.749281,-7.020372,-3.228180,-6.540962,-4.647887,-4.583032,-9.044192,0.696933,-9.062741,4.365737,-7.588747,3.555343,8.076003,5.576373,7.891004,-5.178470,-3.578046,9.614955,2.240118,-3.414542,1.764494,8.722617,9.126850,9.768678,0.348101,7.772572,1.568763,-5.010987,-3.509175,5.281457,-4.206775,2.602493,-1.405449,6.198029,-3.247058,9.116350,-0.278230,8.460699,-4.958940,1.324676,3.818723,7.509241,-3.990710,-3.328981,-0.249661,-5.416964,6.122873,8.188067,-5.694221,5.837074,-9.390317,-9.815132,7.452918,4.368990,6.047876,-4.453579,2.962338,1.643138,7.327766,-6.382863,6.671446,1.811917,-6.524478,-6.494636,8.395343,8.559250,-3.878076,9.204322,-4.065530,7.373402,4.535621,-1.088952,-2.287733,-2.735400,5.041130,2.837458,9.178139,7.810658,2.816065,-3.708473,-2.730822,-9.902453,-1.406570,-6.871377,-1.724144,-7.976114,2.241783,0.436843,-8.914053,-0.172647,-1.143777,-2.578316,-4.219976,-5.985694,0.082510,-2.384596,-4.634264,-6.567275,-5.447555,6.886626,9.558991], dtype = "float64")#candidate|5447|(180,)|const|float64
const_5448 = relay.const([-1.243761,-2.116347,9.564970,-6.426179,0.607414,-0.264464,-2.681177,-2.119439,2.665370,1.955978,9.937673,-2.803919,2.316954,-2.349271,2.126785,7.411172,8.636287,-6.049287,-7.300043,-8.404105,9.555860,3.366563,-0.173288,-0.374850,0.447257,-0.240515,-7.043536,3.104704,-2.730236,-5.111258,1.864283,9.866217,1.896071,-2.255441,-9.971431,1.714552,5.577339,1.482268,5.755805,5.271222,8.613868,2.721764,-8.650073,8.075054,0.312301,-6.403144,8.240245,5.830383,4.129977,2.207122,3.114505,9.022963,4.643341,-6.829111,0.135179,5.655349,9.080995,-1.651875,-3.799071,-4.797419,3.571935,-0.306409,-5.733946,7.604127,5.540981,2.586318,-1.656664,4.861233,3.870522,-8.323991,5.839516,-4.076742,-0.013714,6.154630,-4.309661,-2.880933,-6.198202,6.021282,1.749539,9.784999], dtype = "float64")#candidate|5448|(80,)|const|float64
const_5449 = relay.const([6.823181,3.653068,-2.339053,4.656736,-1.640645,9.418603,-6.689944,6.608385,-8.303417,-6.483753,-1.793254,-4.907550,1.072621,3.377095,-3.431702,-7.727191,4.619372,0.472544,8.462391,-0.355454,-2.820573,-4.622147,-6.451274,3.699896,-5.083046,9.749292,2.606256,-6.080537,1.717265,8.029698,-4.987635,-1.595408,-4.332857,0.611306,-7.547125], dtype = "float32")#candidate|5449|(35,)|const|float32
const_5450 = relay.const([-2.066344,6.146016,4.144037,7.651821,-5.273402,-4.103775,0.526777,-7.234082,1.043869,-1.214863,4.912549,9.290722,-9.702496,-7.692128,-3.215996,-8.531745,1.851792,4.470736,0.791348,7.323016,2.641514,-1.624603,-2.443209,-2.090531,6.090616,7.185677,3.380874,8.834006,-6.586988,5.897156,-4.094760,6.792186,8.828513,-0.809039,-7.338947,-6.135187,2.389170,-2.811516,-1.102334,2.585916,-3.708100,-3.770967,-5.466219,4.959104,4.344007,1.332034,-5.707854,3.918234,4.094208,-3.399144,6.838505,-0.067908,0.693668,-1.002156,9.978690,2.285280,-7.550669,7.387683,-0.712184,-1.745454,6.929552,6.440716,-2.922518,8.459351,-8.175485,2.939241,-5.515341,-6.522034,9.640319,8.294616,-8.474029,-1.489368,-8.178376,1.535874,-9.470332,-0.246891,-8.918267,-3.437798,-7.412035,-1.913361,9.204320,4.001478,6.447937,-7.836134,-4.142749,3.102093,-5.527076,-1.930695,4.303216,5.886395,0.129469,3.121786,9.072709,-6.923852,9.243465,-2.064087,3.997117,1.082407,8.173143,8.032975,8.127282,9.669961,-4.744420,9.549927,7.866146,1.345476,-3.173856,-6.011530,-8.712431,-4.875531,-1.046395,6.404688,-2.907807,-4.328592,-6.182834,5.061058,9.798318,4.236469,-4.064104,1.676592,-6.685360,-1.137631,-4.751171,-5.709519,-1.753173,-4.190502,-9.109635,-9.918337,-2.780141,-6.042716,-4.512894,3.050255,-8.905441,5.254087,2.119182,9.845254,4.138810,-5.126112,-5.265981,6.190081,4.589787,0.991026,7.045202,-5.144337,0.636927,-5.018006,0.675266,2.660147,-9.129838,-2.892294,7.591240,1.497811,-1.408580,-1.903601,5.666484,4.498225,-2.849048,-9.047124,-7.107504,5.623907,7.025577,9.449561,4.467306,6.788278,3.757199,9.947349,2.682201,4.349788,5.082511,-9.293101,8.101038,8.647253,3.804089,9.394791,6.166516,9.933093,-9.105251,4.172880,3.691323,-9.131058,-2.661878,9.931801,-4.009712,1.404536,3.981259,-1.561257,1.812351,-7.257573,9.160185,-7.888591,-7.462696,-3.784371,-5.299102,0.570837,-1.527328,-5.916387,6.572977,-4.549763,7.158359,8.519218,3.446333,9.034670,-7.083697,3.948354,-9.474358,-0.616661,1.560090,8.341780,-8.454269,5.534281,-7.372920,8.917961,-8.085692,-0.268550,-3.586700,-7.222584,2.131505,-0.262011,2.294292,-2.102786,-8.277953,-0.834384,8.134336,1.045766,-8.262579,-6.818386,1.161367,7.785104,7.793591,7.050322,6.142915,8.773387,1.732129,-0.184957,-2.739754,-5.412176,2.250538,-0.033843,5.365523,-1.192093,2.470673,-6.230649,1.229456,-5.074403,4.009643,-3.058144,3.248202,-7.397150,1.958411,5.778153,9.780123,-9.888643,-2.458504,5.555796,4.656725,-9.956056,-3.520105,3.770522,-5.812646,-5.802400,8.007555,-9.551693,-3.508730,1.206372,-4.559197,8.166483,2.770950,-3.539997,8.420741,8.655559,-4.462739,0.217713,-0.850120,-7.440797,-1.670893,8.994369,9.375128,-2.881237,-3.710382,0.524813,-6.411332,-7.095946,7.274798,7.756935,-8.473651,4.324279,-1.756156,8.506068,0.560334,8.420481,-9.377516,9.548878,6.506237,4.177400,4.848210,-6.832646,-8.819370,8.713665,8.747738,-6.360584,5.705413,-3.804349,-9.146417,6.605104,9.076115,5.125398,2.017429,7.087188,-7.319915,-2.419559,-8.129209,7.821217,9.853534,-9.699285,9.391068,-2.045512,-8.060177,4.465605,-6.837249,-1.093941,5.007802,2.466730,-4.882747,0.875382,3.906352,-1.369777,-5.812021,-6.918542,4.073555,0.917863,7.816298,5.534256,-6.715558,-2.769036,0.797629,5.867342,-8.286572,8.724407,6.899795,5.209681,-6.399184,-7.677185,4.073570,-7.014296,7.817570,-0.641067,3.837840,-3.682017,-2.295586,-4.590607,8.018393,-9.826486,-5.839896,-7.013116,4.271196,4.067278,-2.010041,-2.241133,-9.696473,-4.929483,-2.097536,1.922424,-3.987331,-4.515299,-3.219659,0.119265,-7.421841,-2.342975,0.124625,-1.448152,-6.384684,5.626691,-2.171365,5.311837,-2.411322,-0.157540,-9.402935,6.559057,-7.035691,3.817660,-1.345516,-2.698782,-5.259597,-5.018136,-2.073367,-5.219816,-6.583146,4.280718,-3.889197,1.098041,-7.919790,2.685300,5.122879,2.088206,-3.595861,5.288413,7.908963,2.192416,-2.316356,-7.758286,2.165888,3.934396,-7.736996,-7.176168,3.852264,3.757396,4.189017,-7.329606,7.645599,-7.760834,-8.307548,3.504118,-2.102390,-0.239648,-5.981695,1.185169,7.541923,3.707191,2.405921,-3.394215,9.635076,-0.672674,2.123496,-7.939506,-9.680075,-0.917744,-9.339338,2.598821,6.829732,1.838469,-5.376740,6.541578,1.774869,2.764474,-7.422027,-4.382284,9.047990,-4.635506,3.846257,-6.210804,-7.509552,8.891909,-2.917034,1.927334,-2.507135,1.858125,8.172030,-2.061683,2.296200,9.044194,-1.243830,2.607869,-1.663327,-7.436317,-6.226324,2.119407,9.408437,4.315229,8.760767,6.146755,4.344377,-9.917290,0.641479,-2.302419,-2.203424,-1.964023,6.590580,5.245433,-4.417265,8.421723,-3.131196,0.499474,6.516705,4.113824,5.601821,-4.639362,8.992373,3.252049,-4.387025,5.979485,8.922759,8.030659,6.326987,-7.852574,-9.101080,2.354046,-2.359307,-4.453601,7.838367,5.248537,0.824801,-8.176499,-3.968680,0.602645,7.997556,-7.624472,2.716064,5.031521,-6.936121,-1.449184,2.653749,4.621451,-3.690806,-5.805883,2.440362,-1.678769,8.293936,6.068545,-0.226830,-8.634971,3.224239,-3.415212,-7.125748,4.278678,4.245908,2.688293,1.863912,-9.794772,2.767828,-8.440846,-6.460160,3.229724,8.619177,-9.301695,9.977288,0.690342,1.789311,1.861949,9.828243,-4.784934,-8.844086,1.554697,-8.075797,8.327305,-2.480542,-3.153156,-0.915066,1.786388,-6.896760,7.760510,-3.410908,-7.740436,-9.076084,-5.235560,-9.915530,-9.159079,-1.169194,0.960232,-7.981169,-6.011989,-5.992362,2.000246,-3.858492,-6.420960,-0.199034,3.310222,-5.456658,-1.202453,1.487757,-3.587394,1.798901,7.263791,-1.932567,-1.315039,8.784458,-1.903522,8.491363,3.475436,-4.930074,-5.508328,4.232874,3.047942,6.789358,6.090609,-8.996262,2.048803,-1.586943,-3.962798,0.261640,4.003088,9.672120,-2.957798,-0.338694,4.770136,5.715834,4.226830,8.956061,-8.357884,2.752401,0.515003,8.521308,5.303065,1.190467,-8.934835,5.608486,-0.876028,1.663067,7.330274,-3.033477,-9.770412,8.395054,-1.444495,7.152282,4.153368,-5.263623,-5.680422,8.227048,-7.963920,8.660497,0.142792,-7.782528,-9.634491,-2.283217,3.270534,-4.107186,-8.895090,-3.822539,-0.494134,1.650039,-2.600420,-2.713832,6.193289,-2.827545,2.037187,5.487028,-0.238520,-1.581046,6.677467,0.736771,1.018343,0.830737,0.290467,-0.228400,5.724225,6.795673,-3.088481,-3.601199,-1.166771,9.540751,4.638225,-2.240925,-3.788370,-5.596786,-1.024504,9.080084,0.601964,9.468252,-1.026024,-2.826931,-2.760290,4.929469,4.851646,-3.739701,-8.242173,7.135167,-4.566094,-5.551048,-5.094558,7.451926,-9.206156,-3.893092,2.496436,-6.585193,-9.088415,0.837376,-3.149584,1.102989,-4.783951,7.368552,9.214881,-1.944190,3.158025,-7.550339,0.136302,-2.433616,-8.455142,7.363735,-8.143449,8.116097,-6.823140,8.965450,2.989743,2.061016,5.596212,7.451148,3.398237,-9.974253,-8.428611,4.772502,-8.970538,5.844466,-3.975977,-0.382382,-4.650435,2.944539,-6.938871,2.136073,4.845717,-7.829693,-7.310872,9.198425,3.601686,-2.616920,2.777510,-5.593001,7.304218,-6.483559,-7.685017,-7.645478,5.892827,-7.795186,9.377144,0.138245,-5.807323,4.137017,2.162101,-5.640426,-9.560091,-9.215302,-8.200443,-9.927728,-1.461029,-0.619319,5.906745,5.025691,-3.252261,5.852280,-8.041935,0.389303,-1.595623,1.798530,4.844670,-4.753256,-3.168500,5.376680,2.855488,-2.045101,1.505163,9.140136,7.076280,8.639902,-0.259188,8.004498,9.134859,7.694892,8.861807,-7.309524,-3.645523,1.186682,7.781777,-5.042723,-3.261025,1.435970,4.895904,-1.005484,7.881206,-0.824874,-3.062006,-3.950240,-9.923470,4.939758,-0.251406,7.226806,6.499308,6.228498,3.382736,2.815671,-3.808366,1.424250,7.404589,2.635854,9.329494,-3.701213,4.251671,-1.737223,-6.533090,-9.853017,7.268082,-0.195477,-8.896468,4.926002,0.269515,5.864960,0.390258,1.454038,-6.619988,-3.137274,-4.039554,-6.610454,4.593026,-6.287977,-7.419550,3.370195,-2.756979,-0.033274,7.691952,-8.783397,5.818991,2.686791,5.870009,0.622756,3.719981,5.876279,2.385310,3.074609,-8.891374,-5.063833,-2.099492,-0.262806,8.695520,1.422475,5.448653,9.391722,6.100547,8.226993,5.795896,6.220658,-8.138325,2.009971,-2.676990,6.687474,-1.472976,9.441271,9.639619,3.898939,4.927455,7.585232,-5.894442,2.799920,0.448357,-2.991773,0.071848,4.134323,6.136932,9.980168,-9.203592,-4.737535,8.465428,8.700549,-3.639703,9.824072,-0.167146,-9.463007,-7.698721,-1.434076,-9.258786,-5.402551,-2.325148,-1.044285,-1.566130,5.222276,-9.553258,7.994082,-9.092727,-3.977950,6.773689,-7.912312,-7.429327,4.845123,-9.568197,5.317883,-7.235529,-2.420207,2.969098,-8.040247,0.450931,-8.357054,-0.661320,2.587419,9.184098,5.093544,2.207491,-4.327084,-2.526277,-8.857895,9.061942,0.534216,-4.191359,0.513337,-3.256835,9.967791,3.124729,4.497358,-7.171127,-3.563706,-4.059944,-0.532556,8.523085,-8.664886,-7.769363,-4.851080,-2.224808,-7.515544,-3.795084,-4.565067,4.436349,-1.905471,-8.136594,-1.255293,-4.124817,-6.009801,-4.198151,-8.519765,0.761467,0.981310,-9.404870,7.058579,-5.407625,5.301079,4.466331,4.044201,8.316509,-0.279382,-0.379230,-7.826552,7.529003,2.020483,-6.066644,-0.762846,-5.998385,5.227079,4.928703,9.214398,-4.567296,-1.024384,7.936089,2.567745,2.028600,-1.496259,-0.843031,-5.306767,5.179331,-4.865182,-1.430089,7.685311,-2.251590,5.583945,8.141814,3.316048,2.263348,-3.128279,-6.145611,5.511168,6.858438,4.320126,1.227184,3.958811,8.789522,-0.629916,-0.982706,6.359145,-4.811238,6.294816,8.723754,-1.446229,-7.378133,9.400157,-9.696602,9.634801,-0.016405,7.392409,-8.097503,-7.172922,-8.509950,5.855028,-2.843334,-9.587710,0.365339,4.068051,-0.289296,7.046843,-3.593257,5.555448,-2.549646,-9.257715,7.145964,-8.554217,-3.636165,-4.064528,9.912699,-2.409712,-5.575156,-3.738327,-1.033468,-5.873945,9.068024,7.500635,7.460507,-1.416001,0.266762,-3.401380,7.385698,6.784522,-2.401665,-6.286500,1.902646,7.117084,0.186469,-2.637640,5.934903,3.464936,-9.245561,-4.178578,4.176285,5.229789,3.148054,-1.344139,-2.409795,8.967917,6.235422,-3.314522,-9.855084,-9.260310,-6.659380,0.028100,8.396084,-0.271476,1.916822,8.871219,-7.270518,-1.775426,3.596240,-6.344414,-2.454174,-8.841721,9.982433,-4.316485,-3.962556,-4.214152,2.562290,6.629752,-1.079313,1.988917,-9.782194,-2.967158,5.079288,9.244438,0.712706,0.433007,4.717600,7.249449,-9.876086,-6.069170,-2.070090,8.888552,-8.076909,9.598273,2.261089,-2.836340,2.759893,-7.473910,4.604427,9.195680,7.676430,-6.989774,-2.643064,0.235630,-1.960483,-7.386426,-3.266080,-9.233547,-5.294086,4.654679,-2.872645,3.845444,6.571421,5.624047,1.601193,6.624334,9.653841,5.460974,-5.330320,-5.828743,-4.773803,9.030573,9.487631,7.502113,0.225562,6.583209,2.847877,-9.433783,-7.369212,3.085616,-3.071862,-6.038530,2.589275,-5.985755,-0.972670,-5.781558,3.590605,-6.463274,2.764570,-6.949160,-4.901459,3.863340,-6.457484,-2.889892,9.437019,4.811146,5.173573,3.424195,9.372159,-1.878282,-0.162735,4.417446,-7.730370,-4.751001,9.781537,8.610058,-3.151865,7.541374,-0.473858,3.742601,-2.396013,9.446447,-3.515952,-0.789970,-4.891135,-7.555867,8.845172,-2.881153,2.323559,8.396687,8.160701,-1.711238,7.402087,9.560990,-5.820584,5.722452,0.582943,-5.443231,7.689961,2.779668,7.595904,1.193984,2.557858,-3.313460,-3.514532,-0.460125,-0.517513,-4.436562,-0.254026,4.391307,-2.708815,7.561217,-0.300884,-9.088096,-9.687929,5.727741,6.926891,-8.272410,4.687104,3.052444,3.395825,2.759596,-6.350977,2.183905,1.339725,6.884200,-0.142822,5.992154,-4.455601,-7.451702,-1.416229,-6.257105,-5.017345,-4.310116,-6.190124,-8.428001,0.150360,6.650518,5.076747,8.962373,-9.352415,-7.923294,4.671317,0.293891,2.906354,0.611621,6.703168,4.930750,-7.109826,9.003790,7.135800,-9.630191,-6.401363,6.439926,3.247829,-7.295585,2.564421,-9.039914,7.067744,2.712091,5.112499,-7.517562,-9.163911,9.306712,6.080158,5.195261,-4.919683,-2.619939,-0.486378,-2.261658,-0.431559,9.985808,2.698119,-7.132205,3.200409,-8.036503,-5.102878,2.579750,-8.732142,-7.156155,-7.183228,6.909670,5.430395,8.839383,3.786155,3.110371,-1.885490,5.589354,-8.804294,-4.625633,4.356306,2.821477,6.108092,0.554111,3.601455,-4.291102,6.325407,-5.829938,0.439959,-3.929164,4.631443,-5.045097,-1.210764,1.947976,5.561563,-3.974368,-6.364215,8.448701,0.253664,-8.192968,-7.122931,-7.338898,-1.146205,-0.218709,-7.447967,-5.827891,8.510028,0.523903,-9.564639,-1.855911,8.533290,3.022848,-8.569232,1.254121,0.260114,-2.424668,-4.865218,8.336333,5.228529,-1.781908,9.184698,2.592748,9.540484,-7.946039,-6.801895,-0.166236,-6.289901,7.778900,-0.134013,-4.258504,-3.782428,4.409203,1.429057,1.819233,-4.620274,-8.422338,-8.622633,-3.538387,-2.495657,-2.552128,-4.234858,-6.599213,-1.255472,1.307396,6.541207,-6.984166,6.713845,-8.145497,-2.901107,7.997816,-1.207288,-0.120305,-0.997779,-0.869576,-1.189273,6.343230,3.454133,8.664543,8.326806,-5.779794,-5.257390,2.669802,-9.916264,-8.537785,8.924005,-1.196360,8.259641,8.662788,2.659322,-8.543147,-2.858994,-3.431908,-8.679924,4.356352,7.899794,-8.381514,-0.014839,3.988177,4.051542,4.245650,0.487125,-1.679181,1.706795,-3.146683,-4.253895,-7.078399,-6.200446,-0.598910,-0.781155,2.340007,-0.441406,8.576182,9.901646,4.506484,-9.305100,7.256222,-5.042827,-5.465975,4.674355,9.934169,4.632536,-4.041663,-5.490310,-7.855768,-8.846161,-8.335044,0.912286,2.355192,-9.701660,-3.975879,-3.059059,9.016961,1.570147,-8.536115,-6.982284,-9.151062,3.987931,-1.187809,-7.287878,-2.108486,-9.656634,8.976963,-2.857257,-8.316765,1.892097,4.469231,-2.847922,5.735835,-2.363288,2.024786,3.209329,-2.727210,-1.079588,-5.877623,-9.022886,-7.193494,-3.400505,-8.783428,-2.166619,8.423583,7.748213,1.132650,7.471557,-1.562624,-0.395168,2.097654,7.853825,-0.882509,-4.257870,-1.993217,8.361963,6.618142,-3.557397,-8.725908,-2.217002,7.305431,-3.755366,6.280425,4.193876,7.291582,6.368444,7.811050,9.056255,4.596114,-5.089433,-8.879512,-3.589451,2.523984,1.907514,7.460486,-6.662063,-7.870201,-9.297369,-4.245650,3.478936,6.141753,-4.205220,0.629875,5.543026,3.887490,6.291842,7.474598,9.470123,-7.483220,7.658869,-0.893310,-7.352139,-1.030473,4.153799,-8.446018,0.058612,1.920145,-4.547121,8.257707,7.501220,-6.918866,-3.281602,-3.968952,-9.942555,-9.986636,5.075255,7.440892,2.156120,-0.759294,8.246489,0.900109,-5.881721,-8.294268,-9.786012,-6.338586,6.814969,-3.010566,9.389964,2.969949,4.705114,7.846109,1.150125,8.961329,-2.245155,4.442063,-3.750761,-4.124976,9.735676,-1.717974,-4.040684,-0.577249,2.486809,8.485778,8.816509,-6.026808,9.909684,1.398688,6.967236,5.066679,-6.527041,1.967147,-9.682896,-5.708059,-3.537181,2.022692,9.757239,-3.926773,-5.161316,8.663828,4.429089,-5.747571,9.694570,9.156510,-1.781379,8.428697,7.675292,-2.991672,-4.201875,0.666629,2.725507,-3.031377,-7.833791,0.725676,-8.592344,0.963353,-3.983937,-1.509958,7.557484,-1.713176,7.853241,0.614879,-2.490812,-4.088438,-2.844805,-5.163367,-8.361205,-5.133530,5.948251,7.964957,9.696928,6.589777,-6.322659,0.372005,6.246556,-5.841363,5.020044,5.446454,9.634342,1.724409,-4.757028,4.459314,-3.668213,7.298598,7.316584,0.953385,3.179574,-5.455050,5.966172,-1.314138,-1.898652,5.551485,-1.747270,2.716982,-4.258759,5.310276,-7.260679,9.561080,-6.672659,5.031685,1.112674,-6.419112,6.628569,-9.853746,7.518090,-9.599152,2.554905,6.135421,-8.377312,9.077391,5.402432,5.159982,8.097921,-9.633190,-2.904954,9.353650,8.547938,-5.965794,8.779517,0.895215,5.966571,-8.522471,7.201672,-4.314860,-6.965051,-6.547878,-7.596170,-5.460906,-4.187330,-9.872933,-9.839488,-6.458593,7.122054,-4.613245,3.513735,0.175166,7.896974,-2.007777,-6.069135,1.162397,-5.012515,-6.192618,3.986787,1.036754,-7.986011,-1.396920,8.328520,-9.676535,-1.895675,1.182242,-6.848883,-1.902520,-1.456276,-9.214896,-9.437988,-4.239263,4.395890,2.962967,3.766661,-0.566269,-8.413607,-6.031980,7.877171,7.830802,2.223944,5.817762,5.325505,-8.156100,-2.206528,-3.070584,-4.774523,-1.480867,-2.319441,-5.059499,-7.972586,1.666715,-7.920217,-6.744863,-9.784108,0.340861,1.631101,2.727244,-2.956338,-6.556524,-0.868777,1.500607,6.144424,-7.200323,-5.311865,3.316764,0.907005,4.289641,-2.696082,3.477362,1.014265,1.502812,4.132058,-3.883622,-5.396512,5.254808,1.663533,0.988940,-0.986172,-2.536925,-7.301719,0.177269,-0.051705,7.639463,-5.510873,7.645796,2.215060,-8.201354,2.641199,8.796657,-5.931223,-2.387166,6.292951,-9.119532,1.904981,-1.053281,6.959890,4.642057,3.649137,-6.976856,2.683536,7.022902,-7.448036,-3.047765,-1.663633,6.702595,-5.385616,4.008035,8.917725,6.197656,-4.279278,1.322983,2.355147,-0.160383,9.847217,-0.549439,-2.849218,-9.307610,-5.980219,4.789472,-3.919932,7.343845,-7.092108,-8.049651,-9.080282,3.343727,-4.588460,-6.062700,9.798997,-4.783989,-4.029439,-9.777444,-9.640628,7.428329,1.986932,-8.027305,-5.800655,-4.991394,-0.300151,-0.366505,-8.424525,9.323391,-3.449190,-6.902780,-8.373183,4.398068,0.824625,-3.128921,-1.855602,-0.047916,-8.765582,8.885215,-2.005296,5.904814,-0.543704,-3.142823,3.762054,8.244679,3.748522,-2.625186,-4.829713,-2.952081,6.509624,-9.125340,8.571782,6.006514,5.716610,-1.083224,-8.461927,-1.363972,4.855340,7.047780,-6.767574,9.841550,-8.177162,-0.283401,6.370586,-2.209113,8.309275,-6.106178,-3.290692,-2.221325,-3.950603,3.560086,-4.316863,1.957179,-5.983491,5.486865,-5.669246,2.914926,-7.155299,2.927391,-1.153109,-8.142822,-3.129558,-0.370988,-8.533929,-6.309394,8.567581,3.606592,4.900790,-8.744808,7.024556,4.355322,-6.923799,-3.096683,-3.204794,-4.354363,9.993822,-2.086727,2.212023,-3.727100,9.843728,-1.179937,0.243999,-3.032510,-9.763494,-0.351197,-1.637135,9.463542,-7.954866,3.503310,-5.604929,-4.921543,-2.912688,4.482885,4.247101,7.973824,3.951756,-5.823484,5.668295,1.935153,5.386134,0.394944,9.085183,-6.139448,-2.735145,-0.557407,4.228561,7.123983,1.523367,2.835833,-7.509842,3.576939,-5.510992,-5.942578,3.205118,3.081954,-2.698473,-8.885622,-2.803192,1.703196,3.947985,9.746094,-4.475822,-0.402952,1.429303,2.434507,9.669814,2.764379,-6.160593,2.446309,-6.251576,-3.315633,-2.326116,-8.953950,0.189993,7.450557,-3.875794,2.487752,1.780605,-6.162117,2.781390,5.394824,0.589552,-4.113700,-0.039572,7.796025,-7.684276,6.569629,-6.878164,1.654416,-1.962210,-8.277838,7.506279,6.383141,-4.366381,-2.574413,5.344722,-6.808834,-1.606378,-1.138779,-2.329295,6.701707,8.159317,7.860474,2.757946,3.423737,-3.129828,-4.370705,1.951889,-4.842357,5.117360,5.142048,-5.139618,6.159760,-4.729106,-6.478888,6.840410,-5.918139,-3.902083,2.812343,-6.618018,7.353517,-6.896133,3.420538,-4.538313,2.438376,-5.877780,-9.625139,-4.937567,4.862950,-9.249380,-7.832462,-0.963140,-7.743207,-7.099343,-9.142647,4.629427,9.718532,6.867642,1.181307,5.249001,3.771648,-8.097426,-0.211226,-6.835732,2.173243,4.517758,-9.111039,-8.679496,7.127095,-4.773959,-0.272888,5.172784,-7.803470,-8.841376,-0.275888,-1.488929,0.715640,-4.020350,-9.993698,1.699679,2.399123,7.996285,-2.487374,-1.269028,-9.850954,5.663058,-2.206245,8.583995,1.164508,2.176383,3.802356,-0.084543,-2.371895,-1.335694,6.740042,-4.838327,3.470534,-6.714827,-0.691212,3.091300,-0.626021,3.659527,6.975069,4.151703,-9.387072,3.404087,-8.247547,-2.463623,-1.454591,7.037345,-6.772828,-4.196327,7.098994,-0.266806,2.585853,1.002170,-6.114851,4.088953,2.474529,9.393138,3.918364,1.827889,-6.943371,-9.866938,-1.738655,-9.323703,5.055405,-1.583088,7.711601,-8.030302,-9.730125,-7.482977,-4.471682,9.369386,-6.058605,2.214254,4.020470,-8.567388,-0.297816,-7.458175,-2.475893,-7.647984,3.268573,7.418337,6.736967,6.188357,6.711599,-2.115250,7.222820,1.844750,-9.167078,8.040245,3.111011,5.140144,-4.720394,-2.642927,-4.821769,9.470167,-1.829984,3.309881,-0.043810,9.264481,-9.032448,-7.017223,2.863324,-3.414192,-0.158654,5.387289,2.508304,-5.323526,-8.847628,-9.718447,0.096569,-3.612711,-9.113128,0.934956,1.236991,-2.984659,-8.617587,8.200687,-2.356046,-3.171566,-7.853519,-3.151732,-2.768666,6.335708,-8.521616,-0.636902,9.179326,4.482956,-3.848116,8.901320,3.093239,0.524625,-6.842378,-2.046683,-4.156885,4.695169,-4.241409,-9.477362,-2.434085,-9.977978,-4.803509,-4.028427,0.916429,8.287493,-6.794256,8.505312,4.734266,-3.469934,-3.678376,-8.134364,6.345832,7.808491,-8.556913,-6.898012,6.289625,4.641786,4.679355,-2.800321,6.280763,-2.439577,-3.403039,1.665608,8.891517,2.713001,-5.380822,-7.953209,4.587624,-2.395868,-5.045962,5.477580,8.192633,4.158436,-6.609177,0.448980,8.932553,-6.594904,-9.343995,0.884582,7.273629,6.483054,4.401296,6.579565,3.198485,-5.396370,-1.281808,8.249849,-6.840634,2.516343,-9.887195,-8.238543,-0.429430,3.097497,-0.239036,-3.724564,4.946488,-4.775433,-1.333502,-6.561699,6.575947,6.865505,-1.626203,0.030569,3.705598,6.411674,2.072992,1.177763,-2.629768,-3.656666,-5.466206,-4.079554,-3.835897,-1.303394,-5.739490,-6.566334,5.484106,-1.898951,6.044306,-1.476523,-4.136234,-1.181565,2.482171,5.981279,2.198405,-3.897543,3.744029,1.546251,4.532777,-0.755556,-5.515368,3.397047,-2.512531,2.569814,6.879078,-6.138780,-0.064812,-1.699293,-4.157526,5.169403,5.742079,7.745050,7.529388,1.958316,-2.307889,-3.162266,-6.431304,-8.019273,8.092730,-2.576266,6.997005,-0.985995,-6.764783,3.936051,0.079892,-6.821416,2.355589,0.042359,-7.991705,4.136415,-8.169401,-6.074887,-1.720204,0.189035,-8.648408,-2.516277,-1.629298,2.629355,4.594849,5.097086,-0.536047,-7.493582,-0.419307,-3.830879,-4.763621,6.110849,2.151647,5.876155,2.352774,-3.105491,8.043544,0.394004,1.837740,-1.387724,-4.178210,8.892264,9.315465,-6.536806,8.626411,-3.831135,-5.052461,-5.745644,6.575869,1.902615,-5.564381,0.633048,4.621537,9.353106,2.068821,9.285056,-1.380660,-8.014045,-3.488964,9.682429,7.660085,1.430578,4.392669,-7.707392,-3.616432,9.795123,3.879218,-6.715626,-1.640741,0.906566,7.286121,9.144643,-8.819083,6.872184,-3.323321,-0.449942,-7.025350,1.738427,-6.191625,9.805329,-6.207450,9.693117,9.986759,-6.894052,-2.606116,2.518764,-7.724731,0.605023,9.312727,-8.703615,0.482427,6.208258,-4.341824,4.593039,-6.811905,0.824631,-9.480887,-1.086643,-8.591397,1.071502,5.639278,-8.363729,4.962524,-2.245283,-9.262646,-2.414077,9.895251,-0.747737,-3.521570,-7.224686,-0.007904,8.286329,2.105535,-2.523164,-0.103356,-3.970679,-7.707766,-5.560532,-8.330599,-0.412045,3.020244,-4.161242,7.538517,-1.162204,-3.609125,-0.865038,9.825027,5.935505,-4.515866,-9.954214,6.274391,-1.321680,-7.136155,0.750930,4.314165,9.892920,-8.931734,5.670872,-4.536907,-2.570037], dtype = "float32")#candidate|5450|(2288,)|const|float32
call_5444 = relay.TupleGetItem(func_3852_call(relay.reshape(var_5445.astype('float32'), [13, 7, 3]), relay.reshape(const_5446.astype('float32'), [1, 462]), relay.reshape(const_5447.astype('float64'), [180,]), relay.reshape(const_5448.astype('float64'), [80,]), relay.reshape(const_5449.astype('float32'), [35,]), relay.reshape(const_5450.astype('float32'), [2288,]), ), 1)
call_5451 = relay.TupleGetItem(func_3860_call(relay.reshape(var_5445.astype('float32'), [13, 7, 3]), relay.reshape(const_5446.astype('float32'), [1, 462]), relay.reshape(const_5447.astype('float64'), [180,]), relay.reshape(const_5448.astype('float64'), [80,]), relay.reshape(const_5449.astype('float32'), [35,]), relay.reshape(const_5450.astype('float32'), [2288,]), ), 1)
func_4707_call = mod.get_global_var('func_4707')
func_4710_call = mutated_mod.get_global_var('func_4710')
const_5469 = relay.const([10,-8,-2,3,6,-5,1,3,-5,3,9,-3,-7,9,6,6,1,-3,4,9,7,6,9,3,4,-1,-9,-3,9,-6,7,-3,5,-3,5,2,-7,9,8,2,-9,4,-7,-6,8,-5,1,5,-5,6,-2,9,5,-7,-9,4,2,-8,4,9,-4,-10,10,3,-6,5,-5,9,-2,4,7,-1,-5,-8,-3,-4,-9,3,10,9,5,5,-8,-2,3,6,-2,-9,-6,-10,3,-7,8,6,-6,-5,-6,-10,5,9,-6,7,1,-8,2,7,10,10,6,8,-8,4,3,2,-6,7,-5,-3,-10,-7,-7,-8,10,6,3,-7,-7,6,-5,-8,-9,-6,-9,3,7,4,6,-10,-1,2,2,-6,2,-9,-10,9,-3,-6,-3,-2,10,-2,-7,3,-3,-3,-4,-6,-8,-5,-3,10,1,-8,6,3,-5,2,-1,3,10,9,-2,-2,9,1,-2,-9,6,7,7,-9,5,8,8,10,-5,4,3,10,-3,-5,1,-8,-1,-10,-5,3,-4,-7,-2,10,7,7,-10,-3,5,8,4,-4,2,-3,4,-8,7,-1,-4,8,-7,-3,-9,1,-6,9,-6,-5,8,-7,6,-3,3,-1,6,-2,4,1,-2,7,-1,10,-1,6,-4,4,-10,-2,2,2,5,-3,9,-10,6,1,-6,-7,-5,-6,7,7,-8,10,4,-8,-8,-8,4,-8,-7,-10,-9,8,9,2,-6,1,10,4,5,-5,-2,10,2,6,8,-2,2,-10,6,7,3,-7,-1,-10,-2,7,-9,2,4,5,-6,8,7,-1,4,-6,-5,-1,-4,3,8,-2,7,-2,-3,-5,-4,-9,5,-5,-5,5,5,-8,-8,7,-1,7,-4,-2,-6,8,-4,-2,-6,-7,7,2,-9,-3,1,5,10,9,10,2,10,7,-8,2,-5,6,-2,-6,-9,8,-8,10,-6,3,-4,-6,-7,-8,-2,-1,-9,9,-5,2,3,-4,6,6,-6,-2,3,5,-10,9,5,-9,8,8,2,-7,-2,3,-6,-2,9,3,9,-6,-2,1,4,2,7,-5,-9,-1,5,9,-6,-6,-4,-8,8,5,8,7,-5,4,-8,10,-5,-8,-8,4,9,-6,-10,9,-8,-7,-10,8,3,9,5,9,-2,-10,6,-2,-3,-8,-5,-10,1,9,4,-7,3,10,-5,6,6,10,10,-6,2,-6,3,2,-5,-3,10,8,6,-9,-7,-10,3,-6,2,5,-8,-3,-7,6,3,1,-1,-7,6,-8,3,9,-8,8,-7,-3,4,-7,-8,2,-2,7,1,10,9,2,8,7,-6,-3,8,9,2,2,9,-1,7,6,-1,-5,4,2,9,-7,4,8,-8,3,-5,9,-9,6,-8,5,-9,-2,10,-7,1,5,-4,7,-2,-1,5,10,10,-3,-8,-10,9,-10,-3,-7,8,2,-5,-3,9,-3,-4,2,8,-4,2,-1,-5,-9,5,7,-7,7,-7,-10,-6,1,-5,6,8,2,-4,-10,-4,-1,6,4,4,7,6,8,-10,4,1,1,-9,-9,5,-4,-10,-10,3,-2,-7,-10,6,-5,-6,2,-8,-9,5,2,1,9,-2,-10,4,2,10,-4,-10,3,-9,-7,9,4,8,-1,3,-2,8,-10,3,4,5,-10,-9,3,9,5,-8,9,8,-4,-2,5,-8,2,6,5,-8,-6,-9,4,-3,-5,1,-8,5,-9,-8,-9,-9,8,-9,-9,-9,3,-6,-7,10,-1], dtype = "int32")#candidate|5469|(660,)|const|int32
call_5468 = relay.TupleGetItem(func_4707_call(relay.reshape(const_5469.astype('int32'), [660,])), 3)
call_5470 = relay.TupleGetItem(func_4710_call(relay.reshape(const_5469.astype('int32'), [660,])), 3)
output = relay.Tuple([call_5416,call_5444,var_5445,const_5446,const_5447,const_5448,const_5449,const_5450,call_5468,const_5469,])
output2 = relay.Tuple([call_5417,call_5451,var_5445,const_5446,const_5447,const_5448,const_5449,const_5450,call_5470,const_5469,])
func_5487 = relay.Function([var_5445,], output)
mod['func_5487'] = func_5487
mod = relay.transform.InferType()(mod)
mutated_mod['func_5487'] = func_5487
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5488 = relay.var("var_5488", dtype = "float32", shape = (273,))#candidate|5488|(273,)|var|float32
func_5487_call = mutated_mod.get_global_var('func_5487')
call_5489 = func_5487_call(var_5488)
output = call_5489
func_5490 = relay.Function([var_5488], output)
mutated_mod['func_5490'] = func_5490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4843_call = mod.get_global_var('func_4843')
func_4844_call = mutated_mod.get_global_var('func_4844')
call_5565 = func_4843_call()
call_5566 = func_4843_call()
output = call_5565
output2 = call_5566
func_5580 = relay.Function([], output)
mod['func_5580'] = func_5580
mod = relay.transform.InferType()(mod)
output = func_5580()
func_5581 = relay.Function([], output)
mutated_mod['func_5581'] = func_5581
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5587 = relay.var("var_5587", dtype = "uint64", shape = (1, 2, 7))#candidate|5587|(1, 2, 7)|var|uint64
var_5588 = relay.var("var_5588", dtype = "uint64", shape = (8, 2, 7))#candidate|5588|(8, 2, 7)|var|uint64
bop_5589 = relay.maximum(var_5587.astype('uint64'), var_5588.astype('uint64')) # shape=(8, 2, 7)
func_2085_call = mod.get_global_var('func_2085')
func_2089_call = mutated_mod.get_global_var('func_2089')
const_5600 = relay.const(7, dtype = "int8")#candidate|5600|()|const|int8
const_5601 = relay.const([5,8,-5,-5,10,-2,6,6,10,-5,9,-2,-3,4,8,-8,-1,5,3,-6,5,-9,-10,5,5,7,-3,-4,9,-8,-5,2,-3,9,10,-10,3,-3,4,-3], dtype = "int8")#candidate|5601|(40,)|const|int8
call_5599 = func_2085_call(relay.reshape(const_5600.astype('int8'), []), relay.reshape(const_5601.astype('int8'), [4, 5, 2]), )
call_5602 = func_2085_call(relay.reshape(const_5600.astype('int8'), []), relay.reshape(const_5601.astype('int8'), [4, 5, 2]), )
output = relay.Tuple([bop_5589,call_5599,const_5600,const_5601,])
output2 = relay.Tuple([bop_5589,call_5602,const_5600,const_5601,])
func_5605 = relay.Function([var_5587,var_5588,], output)
mod['func_5605'] = func_5605
mod = relay.transform.InferType()(mod)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5605_call = mutated_mod.get_global_var('func_5605')
var_5607 = relay.var("var_5607", dtype = "uint64", shape = (1, 2, 7))#candidate|5607|(1, 2, 7)|var|uint64
var_5608 = relay.var("var_5608", dtype = "uint64", shape = (8, 2, 7))#candidate|5608|(8, 2, 7)|var|uint64
call_5606 = func_5605_call(var_5607,var_5608,)
output = call_5606
func_5609 = relay.Function([var_5607,var_5608,], output)
mutated_mod['func_5609'] = func_5609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_5652 = relay.TupleGetItem(func_4770_call(), 1)
call_5653 = relay.TupleGetItem(func_4772_call(), 1)
const_5673 = relay.const([[[-1,-9,3,-9,3,-5,3,7,3,4,-9],[-7,3,-3,-10,-5,2,-5,7,9,9,-3],[5,4,-6,-2,-1,-6,-2,9,3,-10,-10],[-9,-9,5,4,2,-7,-7,-7,10,7,-2]],[[4,-8,5,-4,-5,2,-3,1,6,-9,2],[-8,3,8,-5,-9,-2,-7,-7,2,6,-5],[2,8,-3,-10,3,5,7,7,4,10,5],[2,10,5,9,-7,-7,-6,-4,-7,-4,2]],[[-8,3,5,7,-3,-1,5,9,5,5,-2],[2,7,2,4,3,1,3,9,5,10,-5],[1,9,1,-7,4,1,-1,-3,5,6,-1],[-3,10,2,-5,7,10,-1,9,-6,-9,4]],[[-7,6,2,9,10,4,3,2,-1,-3,4],[-2,6,-7,4,-7,-10,-3,5,-6,8,-7],[-3,9,5,-7,-10,3,8,10,-3,2,-10],[-6,9,-9,1,7,2,-10,-10,7,5,-3]],[[-4,-4,10,2,1,4,-1,8,-7,-6,1],[-10,-2,-10,-1,-1,-7,-1,2,-8,3,-4],[3,6,5,2,7,-8,1,5,2,-4,-2],[-8,8,7,8,-8,1,2,6,-3,-8,-2]],[[-8,8,3,-3,-8,-9,-8,8,6,-6,9],[-3,6,8,7,-2,8,-7,1,-6,-2,5],[-1,-6,10,4,-4,6,2,-3,-5,4,-4],[-4,2,3,-7,5,-3,5,-5,-5,-3,-8]],[[-5,4,5,-3,10,3,9,7,6,4,-3],[5,5,6,2,-2,4,-9,3,-7,9,-6],[-5,4,3,3,4,-3,-9,-8,-2,8,-8],[6,-8,6,-2,-8,3,10,-10,3,10,-5]],[[-6,10,5,5,-6,5,-3,-3,-1,-4,3],[-4,7,-8,-5,6,6,-9,-3,-4,-5,-4],[10,-5,-8,-7,3,5,9,8,6,7,-9],[3,-1,10,-6,4,2,6,8,-5,5,10]],[[-3,1,-2,3,5,3,5,-9,10,6,3],[-5,7,2,10,-9,-2,-4,9,6,-3,7],[4,8,1,7,-8,-7,-2,9,2,-5,-10],[-7,-4,10,-1,5,5,1,-9,-4,-3,-4]],[[-1,-7,4,-5,10,-3,6,2,-2,-7,4],[5,-10,-2,1,10,-2,-4,8,1,5,2],[7,1,3,-6,-7,2,-1,2,2,-3,8],[3,9,2,7,-5,10,-4,5,-1,3,2]],[[8,8,-6,6,-10,-10,2,1,7,-4,4],[-9,-9,5,-4,8,3,-5,6,-4,10,-3],[5,-4,4,9,-7,8,9,-10,2,-6,-1],[-3,2,-3,-1,-7,-4,9,10,-5,6,-4]],[[9,-7,-1,6,-6,1,6,4,-2,-4,-3],[-4,2,-1,5,3,-1,-4,7,-6,-9,-3],[-3,-2,8,-1,2,-4,-7,3,10,7,-8],[6,9,8,-1,2,-6,10,4,-4,9,1]],[[3,-7,9,6,4,-3,-6,-10,-2,2,1],[-3,-3,3,7,5,7,-4,-7,6,-2,2],[-1,-4,9,10,-8,-6,2,-1,3,-8,10],[-1,-2,-6,-7,2,-5,1,-2,5,-4,1]],[[10,6,7,-8,-5,4,7,10,10,-1,10],[-8,-3,-2,-4,4,4,1,-3,8,9,5],[-2,9,-7,-5,-4,-1,8,5,-8,-9,-10],[-4,9,-3,2,4,3,5,6,8,5,-9]],[[3,-6,-5,-1,-3,-10,-7,-3,-10,-4,-8],[4,-9,6,-2,-6,6,-5,-4,10,3,2],[-4,10,1,9,-3,5,-7,-5,-3,3,-2],[4,7,5,-3,-10,3,-1,4,-4,-4,8]]], dtype = "int32")#candidate|5673|(15, 4, 11)|const|int32
bop_5674 = relay.equal(call_5652.astype('bool'), relay.reshape(const_5673.astype('bool'), relay.shape_of(call_5652))) # shape=(15, 4, 11)
bop_5677 = relay.equal(call_5653.astype('bool'), relay.reshape(const_5673.astype('bool'), relay.shape_of(call_5653))) # shape=(15, 4, 11)
bop_5689 = relay.logical_or(bop_5674.astype('bool'), relay.reshape(const_5673.astype('bool'), relay.shape_of(bop_5674))) # shape=(15, 4, 11)
bop_5692 = relay.logical_or(bop_5677.astype('bool'), relay.reshape(const_5673.astype('bool'), relay.shape_of(bop_5677))) # shape=(15, 4, 11)
func_5605_call = mod.get_global_var('func_5605')
func_5609_call = mutated_mod.get_global_var('func_5609')
var_5694 = relay.var("var_5694", dtype = "uint64", shape = (14,))#candidate|5694|(14,)|var|uint64
const_5695 = relay.const([-2,5,-6,-1,5,10,-8,3,-3,-8,-1,-4,-10,-5,-7,-2,-9,-5,5,3,5,7,6,-7,3,2,8,-10,10,-9,-10,-8,-1,3,-6,6,-10,7,5,7,-3,1,6,10,-9,-5,-1,7,5,-7,-6,4,-8,-2,-7,10,-9,-1,-4,-2,-9,1,1,3,-8,7,-5,-10,4,-5,-2,-2,8,7,-2,5,8,-1,-4,5,7,5,-4,7,8,2,-9,-10,-8,2,-10,1,-5,-8,-9,2,-4,-9,2,10,-10,-10,5,-7,-9,-2,6,-8,8,-1,-9,-6], dtype = "uint64")#candidate|5695|(112,)|const|uint64
call_5693 = relay.TupleGetItem(func_5605_call(relay.reshape(var_5694.astype('uint64'), [1, 2, 7]), relay.reshape(const_5695.astype('uint64'), [8, 2, 7]), ), 1)
call_5696 = relay.TupleGetItem(func_5609_call(relay.reshape(var_5694.astype('uint64'), [1, 2, 7]), relay.reshape(const_5695.astype('uint64'), [8, 2, 7]), ), 1)
output = relay.Tuple([bop_5689,call_5693,var_5694,const_5695,])
output2 = relay.Tuple([bop_5692,call_5696,var_5694,const_5695,])
func_5697 = relay.Function([var_5694,], output)
mod['func_5697'] = func_5697
mod = relay.transform.InferType()(mod)
var_5698 = relay.var("var_5698", dtype = "uint64", shape = (14,))#candidate|5698|(14,)|var|uint64
output = func_5697(var_5698)
func_5699 = relay.Function([var_5698], output)
mutated_mod['func_5699'] = func_5699
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_5731 = relay.TupleGetItem(func_4821_call(), 0)
call_5732 = relay.TupleGetItem(func_4822_call(), 0)
uop_5733 = relay.acosh(call_5731.astype('float32')) # shape=(15, 4, 11)
uop_5735 = relay.acosh(call_5732.astype('float32')) # shape=(15, 4, 11)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_5746 = func_1070_call(relay.reshape(uop_5733.astype('int32'), [15, 4, 11]))
call_5747 = func_1070_call(relay.reshape(uop_5733.astype('int32'), [15, 4, 11]))
output = relay.Tuple([uop_5733,call_5746,])
output2 = relay.Tuple([uop_5735,call_5747,])
func_5750 = relay.Function([], output)
mod['func_5750'] = func_5750
mod = relay.transform.InferType()(mod)
output = func_5750()
func_5751 = relay.Function([], output)
mutated_mod['func_5751'] = func_5751
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5752 = relay.var("var_5752", dtype = "bool", shape = (11, 16, 15))#candidate|5752|(11, 16, 15)|var|bool
const_5753 = relay.const([[[True,False,False,True,True,False,True,True,True,True,False,False,True,True,False],[True,True,False,False,True,True,True,True,False,True,False,False,False,False,False],[False,True,False,False,False,False,False,False,True,False,True,False,False,False,True],[True,False,False,True,False,True,False,False,False,False,True,True,True,False,True],[True,False,True,True,True,True,True,True,True,True,True,True,True,False,True],[False,True,True,False,False,False,False,True,False,False,True,True,True,False,True],[True,True,False,False,True,True,True,False,False,True,True,False,False,False,False],[True,False,True,True,True,True,True,True,False,True,True,False,False,True,False],[False,False,False,False,False,True,True,True,True,True,False,True,True,False,True],[True,False,False,False,True,True,False,False,False,False,True,True,False,True,False],[True,True,False,True,True,False,False,False,False,True,False,False,False,True,True],[False,True,True,False,True,False,True,True,False,True,False,True,False,False,False],[True,True,False,True,False,True,False,False,False,False,False,False,False,False,True],[True,False,False,False,False,False,False,True,True,False,False,True,True,True,False],[False,False,True,False,True,False,True,True,False,True,True,False,True,False,True],[True,True,True,True,False,False,True,False,True,True,True,False,False,False,True]],[[False,False,True,False,False,False,False,False,False,False,True,True,True,True,True],[False,False,True,True,True,True,True,True,True,True,False,False,True,False,True],[False,True,True,True,True,False,True,True,False,True,True,True,True,False,False],[False,False,False,True,False,False,False,True,True,False,False,True,False,True,True],[True,True,False,True,False,True,True,False,False,True,True,False,False,False,False],[True,True,True,True,False,True,True,True,False,False,True,True,True,True,False],[True,True,False,True,False,False,True,True,False,True,False,False,True,False,False],[False,True,True,True,True,False,False,False,True,False,True,False,True,False,True],[False,True,False,False,True,False,False,False,True,True,True,True,True,True,False],[True,True,True,True,False,False,True,False,True,False,False,False,False,False,False],[True,False,False,False,False,True,False,False,True,False,True,False,True,False,True],[True,False,False,True,True,False,True,False,False,False,False,True,False,False,True],[True,True,True,True,True,True,False,False,True,True,False,True,True,True,True],[True,True,True,True,False,False,False,True,False,False,False,False,True,False,False],[False,True,False,True,False,True,False,False,True,False,True,True,True,True,True],[False,False,False,False,True,False,False,True,True,True,False,True,True,True,False]],[[False,False,True,False,True,False,True,False,False,True,False,False,False,True,True],[True,True,True,True,True,False,True,False,False,True,True,False,False,False,True],[False,False,True,False,False,True,False,False,True,False,True,True,False,True,False],[True,True,True,False,False,True,True,False,True,True,True,False,True,True,False],[False,False,True,False,False,True,True,False,True,False,False,False,True,True,False],[True,False,True,False,True,True,True,False,True,False,True,False,False,False,False],[True,False,False,False,False,False,True,True,False,True,True,False,True,False,True],[True,True,False,False,False,True,False,True,True,True,False,False,False,False,False],[False,True,False,False,True,True,False,True,False,False,False,False,False,True,False],[False,True,False,False,True,False,True,True,True,False,True,True,False,True,False],[False,True,True,False,True,True,True,True,False,False,True,False,False,True,True],[False,True,False,False,True,False,False,False,True,False,False,False,True,False,True],[True,False,False,True,True,True,False,False,False,False,False,True,False,False,True],[True,True,False,False,True,False,False,False,False,True,False,True,False,True,True],[True,True,False,False,False,True,True,False,True,False,False,False,True,False,False],[False,True,True,True,True,True,True,True,True,True,True,True,False,True,False]],[[False,False,True,False,False,True,True,False,True,False,False,True,False,True,True],[True,False,True,False,True,False,True,False,False,False,True,True,True,False,False],[False,False,False,True,False,True,True,True,True,False,True,True,False,False,False],[True,True,False,False,True,True,True,True,True,True,True,True,False,True,True],[False,True,True,False,False,True,True,True,False,False,False,True,True,False,True],[False,True,False,False,False,False,False,True,True,True,False,False,False,False,True],[True,False,False,False,False,True,True,False,False,True,False,False,True,False,False],[False,False,False,True,False,False,True,False,True,False,False,True,False,False,True],[False,False,True,False,False,True,True,False,True,False,True,False,False,False,False],[True,True,False,True,False,False,True,True,True,False,True,True,True,True,True],[False,True,True,True,False,False,False,True,False,False,True,True,False,False,False],[False,True,True,False,False,True,False,True,False,True,True,True,False,False,False],[False,False,False,True,True,False,True,True,True,True,True,True,True,True,True],[True,True,False,False,True,False,True,False,True,True,True,False,False,False,False],[False,False,False,False,True,True,False,True,False,False,False,False,True,True,True],[False,False,True,False,False,False,False,True,False,True,False,False,True,False,False]],[[True,True,False,True,True,True,False,False,False,False,False,True,False,True,False],[False,True,True,True,True,True,True,True,True,False,False,True,False,True,False],[False,False,True,False,True,False,True,True,False,False,True,False,True,False,True],[True,False,False,False,True,True,False,False,False,True,False,False,False,False,True],[False,False,True,True,False,False,False,False,True,False,False,True,True,True,True],[False,False,True,True,True,False,False,True,False,True,False,True,True,False,True],[True,True,False,False,False,False,True,False,False,False,True,False,True,False,True],[False,False,False,True,True,True,True,False,False,False,True,False,True,False,False],[False,True,True,False,False,False,True,True,False,True,True,True,False,True,True],[True,True,False,True,True,True,False,False,True,False,False,False,False,True,True],[True,False,False,False,False,False,False,True,True,True,True,True,False,True,False],[False,False,True,False,False,False,True,False,True,True,True,True,True,True,True],[False,False,True,True,True,True,True,True,True,True,False,False,False,True,True],[False,True,True,True,True,True,False,False,False,True,True,True,False,True,False],[True,True,True,False,False,False,False,False,True,True,True,False,True,True,True],[False,True,False,True,False,True,True,False,True,True,True,True,False,False,False]],[[False,True,True,True,False,False,True,False,False,True,True,True,True,False,False],[False,False,True,False,True,True,True,False,False,False,True,True,True,True,True],[True,False,True,True,True,True,True,True,True,True,False,False,False,True,False],[False,True,False,True,True,True,False,False,False,False,False,True,False,False,True],[True,True,True,False,False,False,True,True,True,False,False,True,False,False,False],[False,False,True,False,True,False,False,False,False,False,False,True,True,False,True],[False,False,False,True,False,True,False,False,False,True,False,True,True,True,True],[True,True,False,True,False,True,True,False,True,False,False,False,True,True,False],[False,False,False,False,True,True,True,True,True,False,True,True,True,False,False],[False,True,False,False,False,False,False,False,False,True,False,False,True,True,True],[False,True,True,False,True,True,True,True,False,False,True,True,False,False,True],[False,False,True,False,True,True,False,True,True,False,False,True,False,False,False],[False,False,True,True,False,True,False,False,False,True,False,True,False,False,True],[False,True,True,True,True,False,False,False,True,False,False,False,True,True,False],[False,True,False,True,False,False,False,True,False,False,False,True,True,False,True],[False,False,False,False,True,False,False,False,False,False,False,False,False,True,True]],[[False,True,False,False,True,True,False,True,False,True,False,False,False,True,False],[True,False,True,False,False,False,False,False,False,False,False,False,False,False,False],[False,False,True,False,False,False,True,True,False,True,False,False,True,False,True],[False,True,True,True,True,True,True,True,False,False,True,False,False,False,True],[False,False,True,False,False,False,False,False,True,False,True,True,False,True,True],[False,True,False,True,False,False,True,True,True,True,True,True,True,False,True],[False,False,True,False,False,True,False,True,True,True,True,True,False,False,False],[True,False,True,True,True,True,True,False,False,True,True,False,False,True,False],[True,True,False,False,True,True,True,True,False,True,False,True,False,False,True],[False,True,True,True,True,True,False,False,True,False,True,True,False,True,False],[False,False,True,True,False,True,False,False,False,False,True,True,True,True,True],[True,True,True,False,False,False,True,False,False,True,False,False,False,True,True],[False,True,False,True,False,False,False,False,False,True,False,True,False,False,False],[True,True,True,False,True,True,False,True,True,True,False,False,True,False,True],[False,False,False,False,True,True,True,False,True,True,True,False,True,True,False],[True,False,True,True,True,False,False,True,True,False,False,True,False,True,True]],[[True,False,True,True,False,True,False,True,True,False,True,False,False,False,True],[False,True,True,True,False,False,True,True,False,True,True,False,False,True,False],[False,False,False,True,True,False,False,False,False,True,False,True,True,False,True],[False,False,False,False,True,True,False,False,False,False,True,True,True,False,False],[True,False,False,True,True,True,True,False,True,True,True,True,False,True,True],[True,True,True,False,True,False,True,False,True,True,False,False,False,True,False],[False,False,False,False,True,False,True,True,False,True,False,True,False,True,False],[False,False,False,True,False,True,False,True,True,True,False,False,True,False,True],[False,False,False,False,False,True,False,False,False,False,True,True,False,True,False],[False,True,False,False,True,True,False,True,False,True,False,True,True,True,True],[True,True,False,True,False,False,False,False,False,True,True,True,False,True,True],[False,True,False,False,False,True,True,False,False,False,True,False,True,True,False],[False,False,True,False,True,True,True,True,False,True,False,True,True,False,False],[False,False,True,False,True,True,False,False,True,False,False,True,True,True,False],[True,False,False,False,False,True,False,True,False,False,True,True,True,False,True],[True,False,False,False,False,True,False,False,True,True,True,False,False,False,True]],[[False,True,True,False,True,False,True,True,True,False,True,False,True,False,False],[False,True,False,False,False,True,True,False,True,True,True,False,True,False,False],[False,False,True,False,True,True,False,False,False,True,False,False,False,True,False],[False,False,False,True,False,False,False,False,False,True,True,True,False,False,True],[False,False,False,False,False,True,True,False,True,True,False,False,True,False,True],[False,False,True,False,True,False,False,True,False,False,True,True,True,True,True],[True,True,True,True,True,False,False,False,False,True,False,False,True,True,False],[True,True,True,False,True,False,False,True,False,False,True,True,True,True,False],[False,False,True,False,True,True,False,True,True,False,False,True,True,False,True],[True,True,False,False,True,False,True,False,True,True,False,True,False,False,False],[False,False,False,True,False,True,False,False,False,False,True,False,True,False,False],[False,True,True,True,False,True,True,True,True,False,False,True,True,False,True],[True,False,False,True,True,False,False,False,True,False,False,False,True,True,False],[True,False,True,True,True,True,False,False,False,True,False,False,False,False,False],[False,True,False,False,True,False,False,True,False,True,False,False,True,True,True],[True,False,True,True,True,False,False,True,False,True,False,True,True,True,True]],[[False,True,False,False,True,True,False,True,True,False,True,True,False,False,False],[False,False,False,True,True,False,False,True,True,False,False,False,True,False,True],[False,False,False,True,False,True,False,True,False,True,True,True,False,False,False],[False,False,False,True,True,True,True,True,False,False,False,True,False,True,True],[True,False,True,True,True,True,False,True,False,True,True,False,False,True,False],[False,False,False,False,True,True,True,False,True,False,False,True,True,True,False],[False,False,False,True,False,True,False,False,True,True,True,False,True,False,True],[True,False,True,True,True,False,False,False,False,True,False,True,False,True,False],[True,True,False,True,False,False,True,True,True,False,False,False,False,True,False],[True,False,True,True,True,False,True,True,False,False,True,True,True,True,False],[True,False,False,True,False,False,False,True,True,True,True,True,True,True,False],[False,False,False,True,True,True,True,True,True,True,True,False,False,False,True],[True,True,False,True,False,False,True,False,True,True,True,False,False,True,True],[True,True,True,True,False,True,True,True,False,False,False,True,False,True,True],[True,False,False,True,True,False,True,False,True,False,True,False,False,False,True],[True,True,False,True,False,False,False,True,True,False,True,False,True,True,True]],[[False,True,True,False,False,False,False,False,False,True,False,False,False,True,False],[True,False,True,False,True,True,False,True,True,False,True,False,False,False,False],[True,False,True,False,False,True,False,True,True,False,False,False,False,False,True],[False,False,True,True,False,True,True,False,False,False,False,False,False,False,False],[False,True,True,True,True,True,True,True,False,False,False,True,False,False,True],[True,True,True,True,False,True,False,True,False,False,True,False,False,False,True],[True,False,False,False,False,False,True,True,True,False,True,True,True,False,False],[False,True,True,False,False,True,True,False,True,True,True,False,False,True,False],[True,False,True,True,False,True,True,False,False,True,False,True,False,True,True],[False,True,True,True,True,True,True,True,False,False,False,True,False,False,False],[True,True,True,False,True,True,True,False,True,True,True,True,False,False,False],[False,False,False,True,False,True,False,True,False,False,True,True,True,True,True],[False,False,True,True,False,False,False,True,False,False,False,False,True,True,False],[False,True,False,False,False,False,True,False,True,False,True,False,True,False,False],[False,False,False,True,True,True,True,False,False,False,False,True,False,True,False],[False,True,True,False,True,True,True,True,True,False,True,False,True,False,True]]], dtype = "bool")#candidate|5753|(11, 16, 15)|const|bool
bop_5754 = relay.logical_and(var_5752.astype('bool'), relay.reshape(const_5753.astype('bool'), relay.shape_of(var_5752))) # shape=(11, 16, 15)
output = relay.Tuple([bop_5754,])
output2 = relay.Tuple([bop_5754,])
func_5759 = relay.Function([var_5752,], output)
mod['func_5759'] = func_5759
mod = relay.transform.InferType()(mod)
var_5760 = relay.var("var_5760", dtype = "bool", shape = (11, 16, 15))#candidate|5760|(11, 16, 15)|var|bool
output = func_5759(var_5760)
func_5761 = relay.Function([var_5760], output)
mutated_mod['func_5761'] = func_5761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5410_call = mod.get_global_var('func_5410')
func_5412_call = mutated_mod.get_global_var('func_5412')
call_5915 = relay.TupleGetItem(func_5410_call(), 0)
call_5916 = relay.TupleGetItem(func_5412_call(), 0)
output = relay.Tuple([call_5915,])
output2 = relay.Tuple([call_5916,])
func_5936 = relay.Function([], output)
mod['func_5936'] = func_5936
mod = relay.transform.InferType()(mod)
mutated_mod['func_5936'] = func_5936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5936_call = mutated_mod.get_global_var('func_5936')
call_5937 = func_5936_call()
output = call_5937
func_5938 = relay.Function([], output)
mutated_mod['func_5938'] = func_5938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_6020 = relay.TupleGetItem(func_5333_call(), 0)
call_6021 = relay.TupleGetItem(func_5334_call(), 0)
output = relay.Tuple([call_6020,])
output2 = relay.Tuple([call_6021,])
func_6035 = relay.Function([], output)
mod['func_6035'] = func_6035
mod = relay.transform.InferType()(mod)
output = func_6035()
func_6036 = relay.Function([], output)
mutated_mod['func_6036'] = func_6036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_6043 = relay.TupleGetItem(func_4770_call(), 3)
call_6044 = relay.TupleGetItem(func_4772_call(), 3)
uop_6045 = relay.sigmoid(call_6043.astype('float64')) # shape=(10, 8, 1)
uop_6047 = relay.sigmoid(call_6044.astype('float64')) # shape=(10, 8, 1)
uop_6054 = relay.atan(uop_6045.astype('float32')) # shape=(10, 8, 1)
uop_6056 = relay.atan(uop_6047.astype('float32')) # shape=(10, 8, 1)
output = relay.Tuple([uop_6054,])
output2 = relay.Tuple([uop_6056,])
func_6072 = relay.Function([], output)
mod['func_6072'] = func_6072
mod = relay.transform.InferType()(mod)
mutated_mod['func_6072'] = func_6072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6072_call = mutated_mod.get_global_var('func_6072')
call_6073 = func_6072_call()
output = call_6073
func_6074 = relay.Function([], output)
mutated_mod['func_6074'] = func_6074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_6212 = relay.TupleGetItem(func_5147_call(), 0)
call_6213 = relay.TupleGetItem(func_5149_call(), 0)
output = call_6212
output2 = call_6213
func_6219 = relay.Function([], output)
mod['func_6219'] = func_6219
mod = relay.transform.InferType()(mod)
output = func_6219()
func_6220 = relay.Function([], output)
mutated_mod['func_6220'] = func_6220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_6242 = relay.TupleGetItem(func_4610_call(), 0)
call_6243 = relay.TupleGetItem(func_4611_call(), 0)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_6260 = relay.TupleGetItem(func_5036_call(), 0)
call_6261 = relay.TupleGetItem(func_5037_call(), 0)
output = relay.Tuple([call_6242,call_6260,])
output2 = relay.Tuple([call_6243,call_6261,])
func_6266 = relay.Function([], output)
mod['func_6266'] = func_6266
mod = relay.transform.InferType()(mod)
mutated_mod['func_6266'] = func_6266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6266_call = mutated_mod.get_global_var('func_6266')
call_6267 = func_6266_call()
output = call_6267
func_6268 = relay.Function([], output)
mutated_mod['func_6268'] = func_6268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_6316 = relay.TupleGetItem(func_5036_call(), 0)
call_6317 = relay.TupleGetItem(func_5037_call(), 0)
output = call_6316
output2 = call_6317
func_6322 = relay.Function([], output)
mod['func_6322'] = func_6322
mod = relay.transform.InferType()(mod)
mutated_mod['func_6322'] = func_6322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6322_call = mutated_mod.get_global_var('func_6322')
call_6323 = func_6322_call()
output = call_6323
func_6324 = relay.Function([], output)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6322_call = mod.get_global_var('func_6322')
func_6324_call = mutated_mod.get_global_var('func_6324')
call_6370 = func_6322_call()
call_6371 = func_6322_call()
func_299_call = mod.get_global_var('func_299')
func_301_call = mutated_mod.get_global_var('func_301')
const_6373 = relay.const([9.056565,0.709969,-2.018878,7.835655,-3.811962,7.877070,-5.283795,1.717729,8.613672,-8.855929,-9.736994,-9.755311,-7.063036,6.741512,1.212254,2.077926,-7.595040,2.937176,0.709792,4.489287,9.999775,5.332987,5.312421,-1.140738,6.144060,-4.092775,0.319414,-2.389179,6.393747,7.467260,-1.650113,7.906956,-4.075998,-5.291414,7.784958,3.912699,-7.901209,-1.349224,8.742297,-5.549269,8.948683,-8.164235,0.539219,2.305411,-1.104571,6.598912,7.877174,-1.720925,1.203353,4.996340,-3.936392,8.030151,7.467485,1.470653,2.795108,6.320640,-2.139794,8.124808,8.478838,-1.609966,-2.709068,-4.474094,-6.118023,8.129287,3.160731,-9.497572,0.941005,-5.652025,6.039193,6.622798,1.469066,-4.647919,-7.656446,-7.774771,-6.869024,2.989070,-0.660242,-5.291138,-6.029332,7.712988], dtype = "float64")#candidate|6373|(80,)|const|float64
call_6372 = relay.TupleGetItem(func_299_call(relay.reshape(const_6373.astype('float64'), [10, 8, 1])), 0)
call_6374 = relay.TupleGetItem(func_301_call(relay.reshape(const_6373.astype('float64'), [10, 8, 1])), 0)
output = relay.Tuple([call_6370,call_6372,const_6373,])
output2 = relay.Tuple([call_6371,call_6374,const_6373,])
func_6385 = relay.Function([], output)
mod['func_6385'] = func_6385
mod = relay.transform.InferType()(mod)
mutated_mod['func_6385'] = func_6385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6385_call = mutated_mod.get_global_var('func_6385')
call_6386 = func_6385_call()
output = call_6386
func_6387 = relay.Function([], output)
mutated_mod['func_6387'] = func_6387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_6394 = relay.TupleGetItem(func_4770_call(), 4)
call_6395 = relay.TupleGetItem(func_4772_call(), 4)
func_5351_call = mod.get_global_var('func_5351')
func_5352_call = mutated_mod.get_global_var('func_5352')
call_6396 = relay.TupleGetItem(func_5351_call(), 0)
call_6397 = relay.TupleGetItem(func_5352_call(), 0)
output = relay.Tuple([call_6394,call_6396,])
output2 = relay.Tuple([call_6395,call_6397,])
func_6399 = relay.Function([], output)
mod['func_6399'] = func_6399
mod = relay.transform.InferType()(mod)
mutated_mod['func_6399'] = func_6399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6399_call = mutated_mod.get_global_var('func_6399')
call_6400 = func_6399_call()
output = call_6400
func_6401 = relay.Function([], output)
mutated_mod['func_6401'] = func_6401
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_6489 = relay.TupleGetItem(func_5036_call(), 0)
call_6490 = relay.TupleGetItem(func_5037_call(), 0)
func_6035_call = mod.get_global_var('func_6035')
func_6036_call = mutated_mod.get_global_var('func_6036')
call_6497 = relay.TupleGetItem(func_6035_call(), 0)
call_6498 = relay.TupleGetItem(func_6036_call(), 0)
var_6502 = relay.var("var_6502", dtype = "int32", shape = (13, 2, 2))#candidate|6502|(13, 2, 2)|var|int32
bop_6503 = relay.add(call_6497.astype('int32'), relay.reshape(var_6502.astype('int32'), relay.shape_of(call_6497))) # shape=(13, 2, 2)
bop_6506 = relay.add(call_6498.astype('int32'), relay.reshape(var_6502.astype('int32'), relay.shape_of(call_6498))) # shape=(13, 2, 2)
func_894_call = mod.get_global_var('func_894')
func_898_call = mutated_mod.get_global_var('func_898')
var_6519 = relay.var("var_6519", dtype = "float64", shape = (180,))#candidate|6519|(180,)|var|float64
const_6520 = relay.const([[-3.990437],[2.816306],[-6.734890],[4.987508],[1.359310],[-0.092292],[-1.471128],[-9.266247],[1.950193],[-5.829232],[-1.718618],[8.394184],[-5.514891],[-6.256879],[-5.021398],[8.032493],[-3.599742],[-4.094356],[8.317495],[-3.747788],[-6.981408],[-1.559868],[5.573403],[2.754686],[-7.608551],[4.833455],[-3.189493],[-2.034406],[3.782431],[-1.500748],[7.306368],[-0.452860],[-8.176987],[-0.712429],[7.186500],[-2.862331],[-6.392620],[-6.450271],[3.035156],[-4.316484],[-7.644982],[-6.416393],[-2.535919],[7.675087],[-3.878056],[8.402161],[-4.701132],[9.450983],[8.266966],[-2.540414],[4.950637],[-4.262623],[7.682267],[5.726634],[-3.026103],[3.045038],[7.111242],[0.055752],[-7.114758],[0.134470],[-3.091404],[-6.385374],[7.041506],[7.451950],[9.075194],[7.266379],[-0.448888],[-9.059902],[-6.745036],[8.633876],[2.415394],[0.556152],[-7.882225],[7.960984],[-3.137504],[6.349272],[3.645308],[0.163848],[-3.664275],[9.591629],[-6.805149],[-8.370230],[-1.159896],[-6.831564],[-7.246025],[8.467108],[-3.322214],[0.493060],[-7.239818],[7.683508],[0.148508],[5.224642],[-8.336889],[9.456958],[-3.121537],[6.951671],[5.385641],[8.928442],[-1.229260],[6.294456],[4.101313],[7.394014],[2.160366],[0.543938],[1.909366],[-1.146029],[7.578009],[3.294040],[-6.773232],[-8.974986],[-5.508088],[7.923198],[6.131054],[1.769439],[8.569346],[1.763063],[-4.877019],[-9.923346],[6.896275],[4.864549],[1.781394],[9.392715],[3.345809],[-0.223060],[-4.803629],[-9.435470],[-5.453451],[-0.472926],[5.139791],[-7.947362],[-0.156771],[4.070459],[-9.473537],[6.377864],[0.967765],[-9.850286],[-7.486207],[-7.850709],[-9.571870],[-2.590172],[5.637593],[3.562558],[-1.674786],[-2.820207],[-0.979065],[-7.182319],[-6.449059],[8.504241],[-9.294044],[-4.945830],[0.980988],[-1.586460],[-2.680658],[1.650583],[9.442565],[5.058697],[0.604707],[6.522790],[4.705531],[9.513993],[-1.226068],[-5.759360],[6.225269],[4.523855],[-7.857436],[-7.832909],[-0.725144],[-9.007193],[8.527873],[3.069943],[1.976386],[1.427300],[-8.503122],[-7.177167],[-6.488449],[8.634482],[-5.223264],[8.654130],[5.099610],[5.090387],[-1.908621],[5.745173],[-8.753946],[-3.150746],[1.319159],[-5.642018],[-6.562029],[8.673059],[-6.603921],[-7.790602],[4.015142],[9.782140],[-6.506962],[-8.917746],[0.748257],[7.011931],[4.749490],[-7.823195],[-7.567508],[7.395641],[6.576153],[-9.261921],[7.347428],[-6.216033],[-4.730356],[5.426666],[-6.189829],[2.580737],[8.227273],[-9.174944],[1.910053],[7.674309],[-0.342251],[-4.212839],[-1.237156],[-4.029777],[3.373057],[4.055809],[6.482675],[3.202928],[1.637946],[0.092488],[0.072423],[-6.711505],[-9.652436],[-5.039821],[-9.992398],[-5.127331],[1.447533],[-9.598097],[-2.135136],[1.549429],[1.986878],[7.181362],[-2.725053],[-0.056872],[1.237233],[9.698635],[-0.110428],[6.308845],[-2.021750],[-2.321523],[0.053391],[9.718168],[0.593680],[-8.631929],[2.155549],[-1.137024],[5.525300],[5.764902],[-4.030262],[5.191474],[4.612873],[-4.715162],[-1.271007],[5.339393],[8.588984],[7.124729],[-3.155086],[-0.424445],[-6.244977],[-1.656181],[-1.583122],[4.851525],[-7.055507],[-9.796082],[-8.500508],[-2.622523],[-4.700157],[-7.730454],[-4.164839],[-6.946087],[2.586311],[2.478761],[-6.355893],[-5.221515],[-5.145260],[-0.386167],[4.207771],[-4.106845],[-1.157531],[-4.119709],[-9.294474],[7.219269],[0.723663],[4.388309],[4.846730],[-2.098211],[-4.538953],[-7.992755],[8.371693],[9.221469],[6.611998],[-0.742455],[2.343236],[-5.159858],[4.657531],[3.167788],[9.921501],[3.813342],[-4.216460],[0.418450],[-7.094809],[-5.955587],[0.455408],[1.416992],[8.142654],[-7.265854],[4.691363],[6.139981],[-3.223795],[-4.758598],[-1.876541],[5.353893],[-2.654126],[6.425983],[-8.787811],[-0.317553],[-6.483455],[8.873121],[-6.524209],[-0.006683],[0.662868],[-7.796186],[2.800707],[-4.761328],[-3.246350],[-5.562662],[-6.283547],[-0.411424],[-5.774520],[8.125223],[-7.403991],[3.373444],[-5.790358],[-4.810157],[1.442417],[7.600851],[-0.235003],[5.947929],[6.070614],[0.696552],[7.681476],[5.244012],[4.029814],[-7.850082],[9.781118],[-4.316337],[-5.255026],[-0.248068],[-3.387988],[0.680442],[8.630466],[0.274516],[-1.049736],[7.736624],[-3.030294],[5.285366],[-0.574337],[6.622466],[0.884855],[7.133026],[6.770063],[-0.167919],[7.227493],[-3.031506],[-7.159504],[-2.930395],[-2.372823],[8.721020],[-2.578155],[9.116083],[3.222924],[-5.682054],[6.895501],[3.182886],[-3.155766],[3.178689],[4.147791],[4.195592],[-8.096329],[-0.743611],[5.571484],[-6.262617],[-1.129443],[-3.617192],[-5.006790],[4.010653],[3.676810],[-7.380107]], dtype = "float32")#candidate|6520|(390, 1)|const|float32
const_6521 = relay.const([-4.507559,0.132744,-3.287063,4.384132,3.296558,7.931137,-4.942673,-6.295910,2.398212,0.925550,-9.812264,7.788170,8.414819,-6.462758,-0.876847,-1.773919,-1.213331,-1.836784,-2.790654,4.494318,3.622081,-2.599104,-6.029057,1.013707,8.191781,-9.033574,7.291250,9.936755,3.365023,-4.915890,0.345171,-1.662492,-9.380768,8.896988,-5.866767,-2.902797,5.611568,5.935032,-0.254030,-0.793412,-5.862659,3.724883,-1.170486,-4.382873,2.989112,6.658319,3.948436,-1.119228,-6.185863,-3.599147,9.542503,0.179652,3.333521,-2.648694,8.704008,2.562540,6.589127,3.495538,-7.501317,0.985563,-6.029583,-2.985376,1.383759,-6.213830,-4.517034,-2.141206,8.134902,6.479665,2.014442,-4.608388,-3.599897,-9.146920,7.808642,1.235934,1.594189,6.984190,-3.564600,3.481434,-5.348823,0.269283], dtype = "float64")#candidate|6521|(80,)|const|float64
call_6518 = relay.TupleGetItem(func_894_call(relay.reshape(var_6519.astype('float64'), [15, 6, 2]), relay.reshape(const_6520.astype('float32'), [390,]), relay.reshape(const_6521.astype('float64'), [20, 4]), ), 5)
call_6522 = relay.TupleGetItem(func_898_call(relay.reshape(var_6519.astype('float64'), [15, 6, 2]), relay.reshape(const_6520.astype('float32'), [390,]), relay.reshape(const_6521.astype('float64'), [20, 4]), ), 5)
func_2669_call = mod.get_global_var('func_2669')
func_2674_call = mutated_mod.get_global_var('func_2674')
var_6531 = relay.var("var_6531", dtype = "float32", shape = (6, 20))#candidate|6531|(6, 20)|var|float32
var_6532 = relay.var("var_6532", dtype = "float32", shape = (1800,))#candidate|6532|(1800,)|var|float32
call_6530 = relay.TupleGetItem(func_2669_call(relay.reshape(var_6531.astype('float32'), [1, 10, 12]), relay.reshape(var_6532.astype('float32'), [15, 10, 12]), relay.reshape(const_6520.astype('float32'), [195, 2]), ), 4)
call_6533 = relay.TupleGetItem(func_2674_call(relay.reshape(var_6531.astype('float32'), [1, 10, 12]), relay.reshape(var_6532.astype('float32'), [15, 10, 12]), relay.reshape(const_6520.astype('float32'), [195, 2]), ), 4)
output = relay.Tuple([call_6489,bop_6503,call_6518,var_6519,const_6520,const_6521,call_6530,var_6531,var_6532,])
output2 = relay.Tuple([call_6490,bop_6506,call_6522,var_6519,const_6520,const_6521,call_6533,var_6531,var_6532,])
func_6536 = relay.Function([var_6502,var_6519,var_6531,var_6532,], output)
mod['func_6536'] = func_6536
mod = relay.transform.InferType()(mod)
var_6537 = relay.var("var_6537", dtype = "int32", shape = (13, 2, 2))#candidate|6537|(13, 2, 2)|var|int32
var_6538 = relay.var("var_6538", dtype = "float64", shape = (180,))#candidate|6538|(180,)|var|float64
var_6539 = relay.var("var_6539", dtype = "float32", shape = (6, 20))#candidate|6539|(6, 20)|var|float32
var_6540 = relay.var("var_6540", dtype = "float32", shape = (1800,))#candidate|6540|(1800,)|var|float32
output = func_6536(var_6537,var_6538,var_6539,var_6540,)
func_6541 = relay.Function([var_6537,var_6538,var_6539,var_6540,], output)
mutated_mod['func_6541'] = func_6541
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_6578 = relay.TupleGetItem(func_5147_call(), 0)
call_6579 = relay.TupleGetItem(func_5149_call(), 0)
output = relay.Tuple([call_6578,])
output2 = relay.Tuple([call_6579,])
func_6580 = relay.Function([], output)
mod['func_6580'] = func_6580
mod = relay.transform.InferType()(mod)
output = func_6580()
func_6581 = relay.Function([], output)
mutated_mod['func_6581'] = func_6581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6072_call = mod.get_global_var('func_6072')
func_6074_call = mutated_mod.get_global_var('func_6074')
call_6667 = relay.TupleGetItem(func_6072_call(), 0)
call_6668 = relay.TupleGetItem(func_6074_call(), 0)
output = call_6667
output2 = call_6668
func_6669 = relay.Function([], output)
mod['func_6669'] = func_6669
mod = relay.transform.InferType()(mod)
mutated_mod['func_6669'] = func_6669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6669_call = mutated_mod.get_global_var('func_6669')
call_6670 = func_6669_call()
output = call_6670
func_6671 = relay.Function([], output)
mutated_mod['func_6671'] = func_6671
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6219_call = mod.get_global_var('func_6219')
func_6220_call = mutated_mod.get_global_var('func_6220')
call_6700 = func_6219_call()
call_6701 = func_6219_call()
output = call_6700
output2 = call_6701
func_6712 = relay.Function([], output)
mod['func_6712'] = func_6712
mod = relay.transform.InferType()(mod)
output = func_6712()
func_6713 = relay.Function([], output)
mutated_mod['func_6713'] = func_6713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6322_call = mod.get_global_var('func_6322')
func_6324_call = mutated_mod.get_global_var('func_6324')
call_6714 = func_6322_call()
call_6715 = func_6322_call()
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
const_6717 = relay.const([-1.120140,1.326117,-0.247582,0.707762,3.699029,-9.210914,5.776315,4.302955,-9.379036,-9.172354,-6.918633,6.224965,-8.172597,2.081170,3.095120,-0.106455,7.857205,-2.810035,-2.622191,-9.530590,-3.003430,-5.042309,-9.420314,-6.327240,-9.217148,6.015674,-8.356346,-8.340600,6.836459,5.220678,-4.705726,-3.562012,6.360539,2.972400,-6.146791], dtype = "float32")#candidate|6717|(35,)|const|float32
call_6716 = func_3456_call(relay.reshape(const_6717.astype('float32'), [7, 1, 5]))
call_6718 = func_3456_call(relay.reshape(const_6717.astype('float32'), [7, 1, 5]))
output = relay.Tuple([call_6714,call_6716,const_6717,])
output2 = relay.Tuple([call_6715,call_6718,const_6717,])
func_6728 = relay.Function([], output)
mod['func_6728'] = func_6728
mod = relay.transform.InferType()(mod)
mutated_mod['func_6728'] = func_6728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6728_call = mutated_mod.get_global_var('func_6728')
call_6729 = func_6728_call()
output = call_6729
func_6730 = relay.Function([], output)
mutated_mod['func_6730'] = func_6730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_6755 = relay.TupleGetItem(func_4821_call(), 0)
call_6756 = relay.TupleGetItem(func_4822_call(), 0)
const_6765 = relay.const([[[False,True,True,True,True,False,True,True,False,False,True],[True,False,False,True,False,True,False,True,False,False,True],[False,True,True,True,True,True,False,True,True,False,False],[False,False,False,True,True,True,True,False,False,True,False]],[[False,False,True,True,True,False,True,True,False,True,False],[True,False,False,False,False,True,True,True,False,False,True],[False,True,False,True,False,False,True,True,True,False,False],[False,True,True,False,True,False,False,False,True,True,True]],[[True,True,True,False,True,False,False,True,True,False,False],[False,True,False,False,True,False,True,True,False,True,False],[True,False,True,True,False,False,False,False,True,True,True],[False,False,False,True,False,True,False,True,True,False,False]],[[False,True,True,False,False,False,False,False,True,True,False],[False,False,False,False,True,False,True,False,False,False,False],[False,True,True,False,True,False,True,False,False,True,True],[False,True,True,False,True,True,True,False,True,False,True]],[[False,False,False,False,False,False,False,False,True,True,True],[False,True,False,False,False,False,False,False,True,False,True],[True,True,True,False,False,True,False,False,False,False,True],[False,False,True,True,True,True,False,False,False,False,True]],[[False,False,True,True,False,True,False,True,True,True,False],[False,False,False,True,False,True,False,False,False,False,False],[True,True,True,False,True,True,False,True,False,False,True],[False,True,False,True,False,True,False,True,True,False,True]],[[True,False,True,False,False,True,False,False,False,True,False],[True,True,True,True,True,True,True,False,False,True,True],[False,True,True,True,True,True,False,False,False,False,False],[False,False,False,True,True,False,True,False,False,True,False]],[[False,False,True,True,True,True,True,True,True,False,False],[False,True,True,True,False,True,False,False,True,False,False],[True,True,True,False,True,False,False,False,False,False,False],[True,True,True,True,True,False,False,True,False,False,False]],[[False,False,False,True,False,False,True,False,True,False,True],[False,False,False,False,True,False,False,True,False,False,True],[False,True,False,False,True,True,True,True,True,True,True],[False,False,True,False,True,True,True,False,True,False,False]],[[True,False,True,False,True,True,False,True,False,False,False],[False,True,True,True,False,False,False,True,False,False,True],[True,True,True,True,False,True,False,False,True,True,True],[True,True,False,False,False,True,False,False,True,False,True]],[[False,True,True,False,True,False,False,False,False,False,True],[True,True,True,False,True,False,True,False,True,False,False],[True,False,False,False,False,False,True,False,False,True,True],[True,True,True,False,False,True,False,False,False,True,True]],[[True,True,False,True,False,False,False,True,False,True,True],[False,True,False,True,False,False,True,True,False,False,True],[True,False,True,False,False,True,False,True,False,True,False],[False,True,True,False,True,False,True,True,True,True,False]],[[True,False,True,False,True,False,False,False,True,True,False],[False,True,True,True,True,False,True,False,True,True,True],[False,False,True,False,True,False,True,False,False,True,True],[True,True,False,False,True,False,True,False,True,False,True]],[[False,True,False,False,True,False,True,False,False,True,False],[True,True,True,True,True,False,True,False,True,True,True],[True,True,False,False,False,False,True,False,True,True,False],[True,True,True,True,True,True,True,False,False,False,False]],[[True,True,True,True,True,True,False,False,False,False,True],[False,False,True,False,True,False,True,False,False,False,True],[True,True,False,False,True,True,False,True,True,False,True],[False,True,False,True,False,False,True,False,True,True,False]]], dtype = "bool")#candidate|6765|(15, 4, 11)|const|bool
bop_6766 = relay.add(call_6755.astype('uint32'), relay.reshape(const_6765.astype('uint32'), relay.shape_of(call_6755))) # shape=(15, 4, 11)
bop_6769 = relay.add(call_6756.astype('uint32'), relay.reshape(const_6765.astype('uint32'), relay.shape_of(call_6756))) # shape=(15, 4, 11)
output = bop_6766
output2 = bop_6769
func_6773 = relay.Function([], output)
mod['func_6773'] = func_6773
mod = relay.transform.InferType()(mod)
mutated_mod['func_6773'] = func_6773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6773_call = mutated_mod.get_global_var('func_6773')
call_6774 = func_6773_call()
output = call_6774
func_6775 = relay.Function([], output)
mutated_mod['func_6775'] = func_6775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_6877 = relay.TupleGetItem(func_4610_call(), 0)
call_6878 = relay.TupleGetItem(func_4611_call(), 0)
var_6887 = relay.var("var_6887", dtype = "int32", shape = (13, 2, 2))#candidate|6887|(13, 2, 2)|var|int32
bop_6888 = relay.less_equal(call_6877.astype('bool'), relay.reshape(var_6887.astype('bool'), relay.shape_of(call_6877))) # shape=(13, 2, 2)
bop_6891 = relay.less_equal(call_6878.astype('bool'), relay.reshape(var_6887.astype('bool'), relay.shape_of(call_6878))) # shape=(13, 2, 2)
func_5750_call = mod.get_global_var('func_5750')
func_5751_call = mutated_mod.get_global_var('func_5751')
call_6906 = relay.TupleGetItem(func_5750_call(), 1)
call_6907 = relay.TupleGetItem(func_5751_call(), 1)
output = relay.Tuple([bop_6888,call_6906,])
output2 = relay.Tuple([bop_6891,call_6907,])
func_6914 = relay.Function([var_6887,], output)
mod['func_6914'] = func_6914
mod = relay.transform.InferType()(mod)
var_6915 = relay.var("var_6915", dtype = "int32", shape = (13, 2, 2))#candidate|6915|(13, 2, 2)|var|int32
output = func_6914(var_6915)
func_6916 = relay.Function([var_6915], output)
mutated_mod['func_6916'] = func_6916
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6773_call = mod.get_global_var('func_6773')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_6927 = func_6773_call()
call_6928 = func_6773_call()
uop_6935 = relay.atan(call_6927.astype('float32')) # shape=(15, 4, 11)
uop_6937 = relay.atan(call_6928.astype('float32')) # shape=(15, 4, 11)
func_1033_call = mod.get_global_var('func_1033')
func_1038_call = mutated_mod.get_global_var('func_1038')
var_6940 = relay.var("var_6940", dtype = "int16", shape = (6, 28))#candidate|6940|(6, 28)|var|int16
var_6941 = relay.var("var_6941", dtype = "float32", shape = (390,))#candidate|6941|(390,)|var|float32
const_6942 = relay.const([[8.937864,6.112028,4.816987,-7.118857,-3.227237,3.688030,6.849770,-0.958790,5.995653,5.748146,3.282586,-5.144264,-5.248154,-0.453110,4.794039,3.822033,2.088637,-2.702581,6.887623,-4.949435,-8.422780,-0.217170,5.073302,4.768223,-7.673754,-7.357419,-3.576448,9.692278,-5.186960,9.846493,9.026809,-0.573583,5.635885,8.671005,5.612435,-2.092111,1.631985,-2.832281,5.455876,7.908831,-1.201190,-4.534660,3.094748,9.059317,7.630510,4.088319,2.809971,5.194375,-8.145757,0.729089,-5.003717,4.070464,-2.777523,-7.645183,5.056319,-1.891708,6.530285,-5.602487,-0.834725,9.514616,-3.287704,-6.232472,-3.209436,0.892081,-3.790228,6.065151,-0.446751,-5.898295,-3.889514,9.123510,3.252608,6.126142,-4.823094,1.640753,7.498029,-7.660851,1.132482,5.789650,-2.420774,-6.028932,8.518812,0.367042,6.359590,-7.835989,-0.267300,1.396157,9.365095,8.853656,8.422530,-5.874911,5.133339,-1.030260,0.288059,-7.968934,-3.436746,-6.476860,-4.041219,-8.215710,-9.520403,7.756558,-6.142998,-6.685260,3.485855,6.019599,-3.849056,3.227433,-6.683223,-5.322073,8.263619,3.517866,0.474585,8.541707,0.571522,8.738661,8.875415,-2.561680,-6.734204,3.352261,-1.098475,-7.765869,2.240429,-5.568993,6.148089,5.250666,-5.968544,8.623010,8.030042,8.365309,-8.367525,-4.089232,-8.358186,2.738665,4.526136,-6.377175,6.142460,-7.625339,0.472377,-0.632172,7.704176,6.407608,-1.863537,8.803932,-6.575766,-8.127419,-5.136130,-7.692657,8.772374,8.116607,-2.495867,0.759540,-0.541827,-9.464617,-0.233324,-5.360323,5.872397,5.412638,-0.068050,6.254869,-8.203901,8.982750,-3.065475,6.384145,4.567191,-8.260370,-8.922159,2.243179,8.039769,-2.258702,-2.082042,7.498090,1.069034,3.877089,6.067456,-8.778855,-4.611024,-5.739741,8.065928,7.047707,-6.801286,-0.885088]], dtype = "float64")#candidate|6942|(1, 180)|const|float64
call_6939 = relay.TupleGetItem(func_1033_call(relay.reshape(var_6940.astype('int16'), [14, 12, 1]), relay.reshape(var_6940.astype('int16'), [14, 12, 1]), relay.reshape(var_6941.astype('float32'), [390, 1]), relay.reshape(const_6942.astype('float64'), [180,]), ), 4)
call_6943 = relay.TupleGetItem(func_1038_call(relay.reshape(var_6940.astype('int16'), [14, 12, 1]), relay.reshape(var_6940.astype('int16'), [14, 12, 1]), relay.reshape(var_6941.astype('float32'), [390, 1]), relay.reshape(const_6942.astype('float64'), [180,]), ), 4)
uop_6944 = relay.cosh(uop_6935.astype('float64')) # shape=(15, 4, 11)
uop_6946 = relay.cosh(uop_6937.astype('float64')) # shape=(15, 4, 11)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_6950 = relay.TupleGetItem(func_5303_call(), 0)
call_6951 = relay.TupleGetItem(func_5305_call(), 0)
func_6728_call = mod.get_global_var('func_6728')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_6961 = relay.TupleGetItem(func_6728_call(), 1)
call_6962 = relay.TupleGetItem(func_6730_call(), 1)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
var_6964 = relay.var("var_6964", dtype = "float32", shape = (462,))#candidate|6964|(462,)|var|float32
call_6963 = func_1356_call(relay.reshape(var_6964.astype('float32'), [6, 11, 7]), relay.reshape(var_6964.astype('float32'), [6, 11, 7]), )
call_6965 = func_1356_call(relay.reshape(var_6964.astype('float32'), [6, 11, 7]), relay.reshape(var_6964.astype('float32'), [6, 11, 7]), )
func_6072_call = mod.get_global_var('func_6072')
func_6074_call = mutated_mod.get_global_var('func_6074')
call_6972 = relay.TupleGetItem(func_6072_call(), 0)
call_6973 = relay.TupleGetItem(func_6074_call(), 0)
func_1492_call = mod.get_global_var('func_1492')
func_1495_call = mutated_mod.get_global_var('func_1495')
var_6975 = relay.var("var_6975", dtype = "uint8", shape = (200,))#candidate|6975|(200,)|var|uint8
call_6974 = relay.TupleGetItem(func_1492_call(relay.reshape(var_6975.astype('uint8'), [4, 10, 5])), 0)
call_6976 = relay.TupleGetItem(func_1495_call(relay.reshape(var_6975.astype('uint8'), [4, 10, 5])), 0)
func_5487_call = mod.get_global_var('func_5487')
func_5490_call = mutated_mod.get_global_var('func_5490')
const_6982 = relay.const([2.972473,5.968481,7.980091,-5.697829,-1.766738,2.035600,3.276194,5.572268,-7.149121,0.436657,-2.902040,-4.907167,-5.303033,9.120989,0.500829,4.278277,-1.815942,4.781197,-4.948045,4.486248,-5.326744,-7.082980,5.322662,1.341864,-4.648488,3.626620,-1.342717,-5.143944,-0.293230,-6.109083,-9.582666,-4.029617,1.367528,-5.471862,3.183508,-7.667556,7.159807,-0.795455,6.028685,-3.992613,-5.131707,-6.677353,-4.179039,3.786046,-7.328035,-1.686321,3.800502,2.526526,-1.401864,1.812882,9.986157,-4.991090,-5.972896,-7.005125,-9.740405,4.150086,-9.142188,0.196600,7.062899,7.804349,6.876688,-8.425279,-2.217388,9.211927,-6.243843,1.758768,-8.350352,-7.591987,-7.846438,-3.396450,7.211707,3.040327,8.841095,-1.763191,5.046446,-1.987739,2.278145,-5.742382,-0.192806,8.219008,-8.375730,2.321587,-9.496872,3.019584,-2.389991,7.441246,-3.954929,9.018859,5.352712,-0.198650,-1.318455,7.389672,7.466694,0.175269,7.793429,-5.202315,9.091103,4.571898,6.629094,-4.247015,-5.467526,-4.534678,-4.088398,3.367278,3.188638,4.057552,-4.342266,-0.800678,-2.968635,-3.011129,-8.191666,5.335637,-7.446868,4.319629,3.107201,7.646576,8.486416,-4.638492,8.795477,7.520390,6.709402,-1.753540,-3.064445,-8.974811,1.437863,-7.772107,3.515613,4.068551,-9.775184,-7.937134,1.541958,-6.245056,7.951333,-8.982348,-3.143925,8.475541,-2.838625,2.812834,-2.154885,1.085310,-6.921091,7.944280,4.864302,5.199846,7.872831,-8.785305,6.346395,0.641866,1.100963,-4.316036,-0.018635,-1.682156,3.525278,1.823385,4.143159,3.628234,-9.510524,1.035460,-3.398019,-3.372509,-2.959597,-8.156853,7.410852,-1.853568,7.772867,-6.343878,8.536846,1.927753,-0.026918,-1.346553,8.665866,-8.805805,7.823588,-6.021768,-5.448128,7.264524,1.195843,4.576095,-9.511783,5.955015,-1.297657,6.228222,-4.924440,-7.452684,7.248895,-9.015039,1.138899,-7.076912,7.592910,-0.142447,9.876051,-3.943790,5.273288,4.946660,-5.102338,4.486348,-5.371195,-8.560585,0.364562,-9.651806,1.858441,-9.726089,5.795066,0.110012,6.658246,-9.297963,-2.653019,0.524100,-5.860287,1.932334,1.876667,0.851384,7.953877,0.740837,6.887830,1.498008,-7.619716,3.346897,-0.419991,-7.350023,-7.242223,6.920163,-4.889629,-3.496836,8.165288,2.847988,-1.077912,5.455607,-4.119762,1.184215,-3.124890,-2.249393,-3.070124,-2.303398,8.925130,-5.726655,9.679527,-3.703159,-8.684611,7.950766,-9.717747,-2.886559,7.088848,-0.316839,-6.264964,1.508765,-8.226119,-8.593901,1.658862,0.488230,4.032533,-7.572863,7.447362,-5.197198,3.193726,-9.496003,-9.949973,5.047466,-6.091094,6.932948,4.661914,1.857220,8.435238,-0.777479,-5.553619,5.695869,5.604626,-7.350741,-8.985695,-0.672151,-0.305890,1.790755,1.420402], dtype = "float32")#candidate|6982|(273,)|const|float32
call_6981 = relay.TupleGetItem(func_5487_call(relay.reshape(const_6982.astype('float32'), [273,])), 8)
call_6983 = relay.TupleGetItem(func_5490_call(relay.reshape(const_6982.astype('float32'), [273,])), 8)
output = relay.Tuple([call_6939,var_6940,var_6941,const_6942,uop_6944,call_6950,call_6961,call_6963,var_6964,call_6972,call_6974,var_6975,call_6981,const_6982,])
output2 = relay.Tuple([call_6943,var_6940,var_6941,const_6942,uop_6946,call_6951,call_6962,call_6965,var_6964,call_6973,call_6976,var_6975,call_6983,const_6982,])
func_7002 = relay.Function([var_6940,var_6941,var_6964,var_6975,], output)
mod['func_7002'] = func_7002
mod = relay.transform.InferType()(mod)
var_7003 = relay.var("var_7003", dtype = "int16", shape = (6, 28))#candidate|7003|(6, 28)|var|int16
var_7004 = relay.var("var_7004", dtype = "float32", shape = (390,))#candidate|7004|(390,)|var|float32
var_7005 = relay.var("var_7005", dtype = "float32", shape = (462,))#candidate|7005|(462,)|var|float32
var_7006 = relay.var("var_7006", dtype = "uint8", shape = (200,))#candidate|7006|(200,)|var|uint8
output = func_7002(var_7003,var_7004,var_7005,var_7006,)
func_7007 = relay.Function([var_7003,var_7004,var_7005,var_7006,], output)
mutated_mod['func_7007'] = func_7007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_7034 = relay.TupleGetItem(func_4610_call(), 0)
call_7035 = relay.TupleGetItem(func_4611_call(), 0)
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
const_7037 = relay.const([-9.421196,5.381882,-5.355411,-0.967111,-5.978073,-4.271990,-4.026992,3.838086,-4.205593,8.168608,-7.556985,-8.573736,-9.195500,1.483990,6.452960,-7.311684,8.368717,1.644824,-3.135218,6.220342,1.031447,-1.138857,6.803313,-6.396417,2.121854,-2.347421,-7.770162,-9.675456,-2.024162,-0.316425,1.183962,9.494063,7.721162,2.912201,-9.625297,-2.088770,-1.665220,7.501497,-5.540397,7.480919,1.504545,7.902774,5.504090,-2.561048,-7.033756,2.522524,-5.833997,-5.464149,8.603048,2.084427,2.763600,-8.423458,1.482108,4.833405,2.967169,9.135612,-2.884326,-3.260352,-2.143683,8.633153,-1.911781,4.401265,0.283017,-4.173279,8.238096,9.992483,5.494728,-7.029271,4.345526,-0.314173,-9.618420,-7.165815,-3.063990,-1.381217,0.209643,4.146085,4.763543,-9.778828,3.934956,8.316304,6.900623,9.790084,-2.169522,5.712006,2.240658,1.000057,9.567324,-3.781610,-0.490003,-9.605920,-7.175166,0.932176,-6.150104,-9.669015,-6.697991,-2.366517,-8.660992,-3.977407,9.094625,0.913165,4.073070,0.037272,-5.780171,4.157377,-4.209537,-8.363221,4.769721,-7.740813,-2.693344,2.881614,5.784415,-1.447399,3.798070,-8.144274,-8.581282,3.011337,-7.998724,-0.459040,-9.454104,-3.599551,4.729174,0.177894,-6.567558,9.506595,6.945265,-8.326450,-6.890921,-2.794252,9.761386,7.802001,-1.115778,-5.597662,0.742592,4.650025,-5.539343,-3.159513,5.280569,-5.395880,-4.701541,-2.148114,7.643767,-1.654856,8.062003,4.234776,8.358934,-3.397343,-8.871731,4.520293,5.884599,7.043384,-7.675670,2.023036,-4.532509,3.417831,4.436634,-9.705268,-8.542140,5.513198,8.252692,4.120426,3.558899,6.727520,-9.707442,5.956037,5.276245,7.286252,-2.788675,2.332939,-5.976424,3.224910,-0.019578,-4.139487,-6.414123,-3.656966,9.501021,7.436543,9.132478,-5.029183,1.270645,1.660623,-5.509437,-7.510948,-7.428638,2.189018,-7.523628,-9.248188,-7.311395,-4.107270,-7.925974,3.247514,-7.285349,-5.034603,6.690159,6.877101,-4.725156,2.454220,1.090663,-2.740990,-3.567752,-0.601925,-9.021198,0.441856,-5.387017,-1.090551,1.538810,-8.584494,-1.182552,2.302988,8.940277,-6.259543,-4.145347,-8.799639,8.814775,3.053963,6.097790,-4.684182,-1.973838,-4.947372,3.106614,-9.366505,-3.591858,-1.341232,4.140910,-9.704179,-4.241152,0.591725,0.622246,-6.186231,-5.574350,-0.515186,-1.218402,7.537669,-7.662480,1.853449,-0.854475,-5.509678,-2.006696,5.435067,0.839326,-8.549190,-3.436414,-1.719580,6.497785,-5.096828,-6.780949,0.403043,-2.277461,2.065052,5.968155,-9.947197,-4.209213,-6.861630,-7.274527,4.761951,-2.852640,0.845792,7.139723,-6.636981,3.369195,-9.841657,1.702417,-6.763017,-6.642963,-3.312530,-8.265665,-6.884592,-9.545883,6.737744,-2.218933,-1.832067,-4.813166,-9.942759,7.259871,-6.140038,5.991631,-5.137135,8.470592,-7.292782,-2.832655,7.337993,-5.535874,-1.020004,-5.253973,7.549924,-7.539516,0.769339,7.663365,-6.730626,-8.316698,7.142728,5.577654,-7.738534,-9.680556,-7.768567,-2.631115,1.980529,9.317130,3.068304,8.876662,6.170084,-1.677008,-5.926181,-0.884431,-2.866154,-7.842068,-4.196897,6.650692,-6.033264,-3.495551,-1.370239,-1.575840,1.394017,6.424114,6.603801,3.310677,-6.370267,-2.982180,1.100999,8.048502,1.584878,-3.173915,7.543205,9.728825,3.961257,5.357298,-3.312477,-2.948576,6.753301,-9.716638,-9.431300,6.636513,3.422480,-3.107116,-6.932368,-8.460601,7.213191,-6.246340,-1.793738,-9.981307,8.228246,5.144973,0.096414,2.497592,-1.090239,5.895739,8.427474,6.456770,-4.565225,9.479398,-8.201939,4.027119,-7.897088,-8.105966,8.418979,4.026033,-9.829565,-9.499020,-2.094652,4.884987,5.672535,5.575131,0.681767,2.071061,-8.866027,7.035303,-0.147302,-9.166704,-5.944524,1.413640,6.633122,-6.215756,4.363037,6.859341,-1.755231,-7.534397,-8.657516,-5.987174,2.947536,8.448941,-1.707333,-0.534031,5.414558,-8.028485,6.419901,9.472083,-9.458786,5.877965,-0.465755,5.126983,5.248184,-6.760265,4.863191,1.057615,-6.118685,5.748869,0.694706,1.761135,-8.779636,-5.305092,1.358415,6.445537,4.046668,-1.781115,9.554723,-9.545379,2.660226,-8.234294,6.336156,2.768636,5.510242,8.454453,-7.697041,0.468506,-8.553186,9.353958,-3.816983,8.861532,1.504334,8.285866,3.037305,4.235785,7.273573,6.194473,6.976614,-7.036007,7.101312,-4.140305,1.134215,4.780957,3.240970,6.170536,3.619052,-5.581381,-7.095336,9.328305,3.530910,6.919633,1.327959,-7.828555,4.313856,9.969088,-1.689490,9.241977,9.257908,1.735754,7.234296,-7.536655,1.529929,3.410284,0.980466,4.469369,8.893201,2.489877,6.536254,1.258864,-5.312468,-2.803882,-2.021855,-2.183542,-5.996438,3.879371,8.646613,-2.871748,-3.718492,-0.384211,-3.470678,-3.125513,-6.841834,-5.378358,5.854884,6.826413,-0.420022,-9.087888,1.664438,5.877493,-7.065502,5.179650,-4.433903,-8.910947,5.583497,-1.643270,-4.797554,5.997719,-7.702367,0.495743,8.343499,-1.600924,-9.249808,4.767068,7.118003,5.787745,8.996217,1.886220,-8.250567,-2.291323,3.820014,9.330122,8.337407,-0.744431,6.284739,-3.159394,-4.030038,-1.202094,6.937145,-2.753169,-9.578231,4.390563,-6.658628,-8.280541,-3.250019,-0.779210,4.573724,-5.971624,-2.919284,6.957732,-1.291501,4.416874,-2.144562,8.879692,7.141656,-6.166985,9.156215,3.968209,1.932788,-1.046396,-9.233520,8.437813,-7.675980,-8.742502,-3.144799,-4.608680,2.930564,-8.799231,-8.862914,-7.709998,5.701634,0.120906,-9.706477,2.557846,-9.217829,0.830104,-6.086454,7.110159,-9.745365,-9.873515,7.299549,3.387287,-8.564733,-7.269837,4.886031,-4.384076,3.000392,4.699966,-9.416289,5.937160,-2.517135,1.249523,4.930830,-3.718038,-1.578658,5.492885,6.639394,1.749892,-6.812106,-5.045032,-4.832375,-6.853039,5.691731,1.913287,-4.856454,-7.154372,1.280295,-2.673309,-9.337138,6.776843,7.502481,-3.781431,5.710889,-3.841770,2.232650,-6.432076,4.653171,-0.658099,-0.352099,-1.788258,-4.106188,-5.721534,-4.438277,2.696335,8.191098,3.861630,0.610756,4.284185,8.948001,-0.865850,8.703837,-8.242188,4.779407,2.249439,-1.796929,3.756098,-9.625969,8.976754,-5.719537,-5.064087,0.090873,-9.147586,5.701408,3.350472,5.860186,-4.001550,-2.928781,3.744026,6.694012,-0.038973,-8.313919,-6.996701,9.566512,7.366655,-5.499596,3.109230,9.062568,-5.162221,1.289492,-8.576476,6.543504,4.271625,6.118321,-4.916812,4.297591,7.580685,-2.344494,5.822910,9.232378,9.319809,-8.423558,1.378984,-0.039918,-1.903265,6.127255,-5.298907,1.183743,8.438711,-6.935406,6.363000,-2.111436,4.808620,9.871008,-6.540357,5.784668,-6.622215,-9.821716,7.020857,-3.879667,-6.109132,-8.238716,-8.216023,6.158091,1.198730,2.740977,6.665238,2.046537,-8.102485,9.753244,7.896158,-2.784007,-6.697756,2.091717,7.264016,-9.347053,6.701245,-3.506764,-8.899855,7.391680,4.717979,9.569758,-0.452852,0.656069,7.071748,0.587694,7.864642,-9.027913,-3.786510,-7.381455,4.004413,-7.528112,2.490797,2.685342,-2.467947,8.280924,0.039077,-2.862736,0.807414,2.449401,9.604566,4.780451,-2.803638,-4.581312,9.778521,2.432496,4.177328,-3.792741,-0.489079,7.050148,-5.486724,5.490863,4.110195,-5.240906,0.477544,6.984546,-3.354690,-2.189370,-9.570158,-5.847188,8.836573,9.504761,4.388272,8.587615,2.761187,-3.612301,-1.369493,8.684349,0.625322,-5.497756,0.464973,4.619234,1.894998,6.492306,3.591083,8.758760,9.905796,3.797333,-5.008072,-1.454830,4.896647,-1.892008,-2.195625,3.238384,7.343322,9.139266,4.874724,-1.163636,-9.588777,4.161717,4.255000,-8.850598,0.382259,1.965590,-9.209391,0.228156,-6.995498,4.507419,4.617036,1.122179,8.948286,-3.059724,1.622687,6.944256,-8.639920,8.728078,4.880508,-7.637057,-2.729232,1.374715,7.598845,-4.360904,-1.417642,2.454946,4.663913,-5.043208,4.226750,6.330273,0.382128,-5.488884,6.236106,-7.057422,6.676538,8.761207,-7.686023,-5.865920,3.598143,-9.506387,2.242230,-7.735708,-0.436997,4.209814,5.507728,-6.991008,3.050782,-3.066373,9.657532,3.936127,2.055717,-9.395333,5.242521,4.692522,8.045408,-9.272279,5.213877,0.164560,5.060978,9.473911,-3.384510,-1.106414,-0.292730,-5.837214,1.228152,-4.770006,1.662325,-0.029383,-9.252067,9.623604,6.384341,-3.635468,-7.132357,-3.151698,-4.973324,-7.404930,-7.782096,-8.945790,6.301551,-0.478946,-2.908008,9.356220,7.734451,8.719940,-6.288755,6.234240,-4.815914,-0.166623,-6.928082,6.663228,5.749263,0.172990,-5.543922,-9.303835,-1.959453,-9.038800,-5.891194,-4.981361,7.794358,0.927430,2.474228,-7.429654,-6.541459,-2.206524,4.332172,5.841444,-6.342923,-8.519798,-1.099879,-9.055908,1.770019,3.916677,1.393729,0.857486,5.354683,-9.472221,-3.013474,7.928910,9.219039,8.610860,9.729070,5.447124,0.309084,-7.265196,8.980122,-8.217425,6.846162,-2.435697,-6.174378,6.035827,-6.328568,-8.969996,-5.055480,0.172394,1.932960,3.590631,4.872517,-1.448016,-6.924238,-3.003897,-6.539246,3.738090,-5.568296,-1.815383,3.937242,2.425544,6.438126,-1.264820,4.624105,4.412509,-4.193436,9.841518,-2.620710,-3.049576,-3.186269,-0.456123,-5.900202,-1.475146,2.914991,8.509889,-4.182622,-7.484544,-5.929874,-4.422222,-4.396963,-4.470132,-1.462148,-4.671767,-8.081950,6.731589,2.043594,0.203869,7.900324,-8.609287,-8.701915,-4.772703,-4.620285,-2.291403,4.132079,-7.499394,-8.895659,1.589384,-6.481473,6.269011,-5.435320,7.026745,-2.589928,1.717359,-1.524489,-7.743805,8.859405,-3.613634,8.852548,-8.044483,3.720099,-5.363766,-0.905317,-3.279651,0.692722,3.521133,-2.901790,2.569151,6.530343,2.501372,1.495347,-2.244217,-1.083433,-5.493376,3.395289,-6.154209,-3.423306,-7.937573,-1.596875,3.263053,0.711258,-5.121855,-6.093305,-5.466261,-7.755118,3.074966,-9.688049,3.097383,-7.204585,-8.715063,-7.401466,-2.139728,-9.445727,4.877621,8.811617,-2.081754,4.741344,1.881791,2.369369,3.953869,8.209401,5.540928,-2.716017,-4.154536,-7.390163,-5.044071,3.202523,5.186096,-9.565659,4.668074,-6.412361,-8.072662,-8.224793,9.972055,6.395705,8.483368,1.729569,-5.747756,9.741149,7.738139,-0.311575,1.575804,-5.740716,3.838743,8.965512,2.160297,-3.900668,-5.295835,5.388520,-6.055212,-4.427930,1.083423,-8.562199,-0.661408,-9.470065,-7.483774,5.579138,-6.990841,-4.307792,-6.867275,-1.458804,1.439078,8.906431,6.348406,6.867119,-8.532017,-5.580188,-0.902585,0.383542,-2.904912,-3.254758,-0.247687,-7.840165,0.033670,-1.623090,9.952516,1.517717,-0.039295,-6.779321,5.105038,7.445018,6.493620,8.532392,3.834849,-1.127020,-8.090800,-8.890288,1.799891,-1.936275,1.478899,-0.238365,8.548394,-2.975753,9.636361,-7.493122,-1.365678,-7.247224,9.202697,8.516982,-0.789741,-9.346401,-4.875974,-1.451168,-6.190349,4.529721,4.628140,-6.151180,2.730707,-5.601240,2.129471,-7.914173,5.343073,4.668570,-6.546265,0.122236,5.814229,-9.801694,-3.519604,3.474731,5.146234,-8.358487,-7.604518,1.572739,6.073821,-2.350515,-1.430698,5.097547,9.838633,-0.602894,4.644344,3.994626,-3.957040,5.317559,-6.051485,4.220215,4.802588,-8.486728,-3.074018,0.971163,-2.922243,-2.937489,-4.857218,-6.615542,-3.240799,-8.767003,-1.326763,-9.118822,8.233599,1.977051,-2.929579,7.159822,-4.627570,-3.423250,4.022579,2.641686,9.216317,7.849019,1.514193,-8.630610,-0.083380,7.224654,-7.033456,6.033445,2.991191,3.118443,0.762267,4.209076,-4.227913,-6.275289,-7.211486,1.800667,8.315369,6.779905,-5.888704,9.041921,-1.527797,7.925748,-2.465921,-9.572107,9.054541,-1.048045,-6.976420,8.440595,9.333685,3.276415,8.382279,5.532635,9.785377,1.560076,-5.988928,-4.385952,2.002937,7.182882,3.531738,-4.216905,9.188516,3.662335,-2.428880,5.388338,3.322054,2.633541,7.913304,3.556743,-2.256718,4.944733,3.649303,8.945050,9.394465,1.803917,8.242221,-5.539098,-9.136300,-4.715302,-1.928382,-9.726231,-7.980635,-7.468270,-0.217295,-8.428778,-3.515354,-9.642686,-5.058491,-8.834718,-4.538211,-3.837674,5.852048,9.940485,-6.898179,9.021310,8.208369,-8.699272,1.803780,2.141159,2.506199,-1.752481,0.501562,1.332780,4.702443,-8.414539,8.285088,5.911474,7.419450,-0.543191,-2.092195,-3.131402,6.157952,-7.775341,4.986880,6.237887,9.755474,-8.253869,-4.958249,-7.844424,9.269997,1.089888,3.508189,-4.051163,4.688286,6.769445,-9.089917,4.932704,-9.598168,-2.209784,-1.516074,-2.700839,-0.118788,-8.248845,3.061074,-1.172469,7.286989,8.705143,-1.102561,9.849911,5.678341,1.836213,-7.076782,4.104022,-6.750197,-2.999040,4.505424,4.349140,6.730507,-8.137376,-9.558293,-5.859122,1.771185,0.675033,3.261040,5.254621,0.101260,-0.065606,-1.151200,-0.614264,2.353953,4.468751,-5.860548,-1.782598,-4.721322,-9.157872,0.736920,9.179250,-2.064415,-9.878014,5.936389,-8.015501,3.001909,3.105942,2.009656,-6.975225,-2.049592,8.861011,-5.873669,8.984507,6.401933,-4.766886,-9.507009,9.866008,-0.732966,-3.263829,1.598153,-4.243161,8.943531,-1.765522,8.567352,1.864929,-8.215699,-3.585844,0.138588,-5.782883,2.370493,6.789173,-9.572370,8.521571,0.675112,-8.768015,-4.136852,3.843731,-4.303099,-5.463269,-2.577014,-2.404664,2.500663,-5.147702,-7.518230,7.876484,4.874845,4.358766,9.711710,-2.188711,-4.151431,0.132865,5.134428,-8.764901,0.952036,7.382949,-0.030254,-1.762299,2.187368,-5.833679,5.943891,8.036016,8.542215,-2.310604,8.905176,7.349921,-7.446136,2.333038,5.862196,3.074406,-2.907761,-3.919789,-0.140382,-3.930224,4.485375,5.424104,-2.166731,6.980155,7.436854,-6.535422,-4.703227,-2.388872,1.462511,-9.562471,3.718592,6.262463,7.197705,5.034144,-4.059939,3.619561,-4.469105,6.373052,0.402839,-9.593888,-9.402355,-3.970630,-4.830544,2.518898,-7.356564,-3.722267,-7.178192,3.497989,-2.890245,5.034741,2.401168,-4.507208,-4.266420,-5.807391,5.185167,-6.822078,-9.294637,-5.185112,-9.827222,-3.652016,-6.591018,-4.596978,-6.665568,-4.456731,-3.780606,2.650695,-1.701104,-5.467246,8.931328,-4.166490,8.332951,5.538602,7.865509,3.221837,2.342772,-0.859173,-8.428781,-9.122636,7.325697,7.953110,8.888790,7.626275,6.417065,-0.150824,-9.332139,4.491378,5.818912,8.562512,-5.758983,-8.025163,-5.702389,5.132548,-9.269328,1.801805,-0.463906,0.281247,-5.992948,7.613061,-8.880587,-3.050560,8.280145,9.539232,-5.050731,2.004330,8.442875,4.915707,0.166488,-9.773434,-0.780544,1.541769,0.826844,-0.017976,6.509897,4.609064,5.176459,-8.965194,2.962190,-8.972032,9.657444,-2.700566,8.261622,-8.070471,8.643090,-2.749726,7.832150,-9.813067,6.324386,-5.298710,2.092188,-8.510106,3.621948,1.123258,-6.222293,2.452492,3.570679,-7.743447,4.275746,8.003193,-1.877930,-8.308526,3.014963,-3.117771,-2.695790,9.845823,-8.700907,-3.904780,4.270179,-4.084137,5.763358,7.874918,2.113906,-4.774284,-9.637939,0.902240,2.037907,-9.994286,7.793855,5.874818,1.545699,5.319794,4.121074,-1.170411,4.691233,-2.728807,-0.862382,3.793101,-7.709255,-8.777768,-5.933030,9.228555,0.013025,-4.940752,-9.187346,-3.518810,5.303179,7.659881,-0.355405,6.734924,-6.156019,-8.124723,9.140094,-2.723460,2.812256,-8.429938,3.618504,-2.163835,-0.803526,1.815846,-4.414530,-0.551038,4.839627,-9.143513,3.680696,8.581030,-4.191931,-9.545339,3.361218,7.729656,7.956196,-4.433202,9.960835,-8.480660,-0.921775,-9.798408,6.806448,-9.466152,-9.403948,-2.961091,-5.512504,9.438768,-6.050741,-5.280860,-4.841453,-9.092131,0.553130,-9.269151,9.156888,-0.762362,-2.130501,3.266606,-9.768987,-0.423087,-9.357484,-4.446928,-6.688679,6.809342,-0.210265,3.422483,9.755145,-7.544177,-3.660313,8.001264,9.604396,7.970249,-9.644869,-1.092089,-5.071580,2.009244,5.473634,6.813820,1.664729,-2.859112,-1.822893,5.673580,-9.343559,9.426473,-2.299830,-5.449367,-2.272266,-5.717538,-9.740303,9.338347,0.061787,-5.125478,3.428434,9.928518,-7.066000,-6.188928,7.309067,5.032574,9.470202,-3.070041,7.184249,-6.044253,8.836120,6.796120,4.985457,-5.681329,4.924100,8.974201,4.318124,-5.927850,8.190863,-4.564815,-8.903438,-1.021457,-9.735414,8.366754,5.396926,-3.939997,-2.165930,1.415364,-6.622386,0.067166,-5.478950,-1.097550,2.473151,7.306654,5.255235,8.683580,3.553448,-7.209424,-7.612645,-7.660526,3.908146,-9.965900,-3.888303,3.157253,-0.398718,-9.099853,9.157941,-9.002062,1.997952,9.644199,0.955846,-8.537688,-6.698091,1.152717,1.486079,8.290829,-6.738310,-7.920922,6.925111,8.409659,-7.282807,-1.254302,5.270814,-4.768014,-2.996263,5.147608,-9.058411,9.959355,-1.588373,-7.190916,-6.837410,-5.773064,4.801701,0.955773,-5.374232,-6.068874,-1.800780,7.287690,4.521200,1.473744,2.537530,-6.303221,-1.996502,2.304654,-9.868372,-2.287359,6.697256,6.547564,-9.570141,4.080528,7.801048,3.595427,-0.811394,7.909707,3.613527,6.298717,-3.570816,-3.218949,9.485113,9.529186,2.074988,-5.666792,1.164663,-2.461561,-3.309457,-0.436451,2.762732,-4.744138,-1.892987,-3.848087,-4.878084,8.546509,4.197687,8.251474,5.756609,-0.005879,2.138710,1.850215,-8.158999,-3.373601,6.341094,-4.886061,-2.719128,-1.041992,5.036653,-6.246246,-7.709666,-0.302193,-3.728975,1.611143,-5.713755,-5.172027,-2.893558,-8.142321,7.024484,-4.006458,-3.122693,-8.655086,7.942089,6.163177,2.070628,-1.705312,8.644553,0.086917,-3.188339,1.785643,-5.893823,-4.411874,5.073136,7.245282,6.249567,6.852130,-2.333619,7.195678,-4.042292,-6.318953,-0.493034,-6.390762,6.383373,0.996075,-3.788889,8.677917,1.765840,3.014719,-2.469216,6.654721,-9.719757,4.146767,-0.283326,-5.831937,-5.190077,-1.322062,0.629162,-4.877992,-4.329758,2.506459,5.301300,5.053000,-3.662875,7.489744,8.796564,3.935172,-5.801509,8.014451,5.698445,6.202654,-2.058736,-2.751630,-9.285714,1.814199,6.688513,3.026811,1.412268,1.625757,-9.532800,-6.335594,5.763421,8.497862,1.822904,9.124420,2.499227,-8.451938,-7.854648,1.856914,1.633359,-2.540639,2.240408,7.844047,-0.356251,7.172918,-7.877740,4.771399,3.905408,8.466790,8.153399,1.344892,3.091520,-8.534974,-1.971526,3.090600,-2.036477,-5.255896,7.128404,-4.480713,-1.686304,-5.556839,-5.762284,7.064288,5.185103,-0.736070,3.156491,5.560699,0.805086,-2.645900,8.259753,6.370953,7.832771,-2.675584,-0.697902,5.946719,-8.814182,2.849277,7.916920,-9.661697,3.377583,7.881010,-8.197956,0.260116,-6.936807,8.911522,0.433065,-9.382343,8.174098,-6.279622,5.559623,-5.030461,9.806878,-5.748162,-3.196854,3.467603,7.722318,-3.169041,3.369075,4.976947,-4.234542,-9.018879,-4.892571,-1.484127,3.265302,4.781110,-0.449393,-6.279433,3.136813,-5.701523,7.786753,3.862863,-2.610170,-8.796918,0.541028,-5.165863,-7.789642,-9.464162,6.126368,-5.772856,4.904506,4.368317,-4.985244,9.162567,1.197871,0.963450,-2.194993,0.720876,3.161589,-2.596753,-4.201097,-5.034886,0.592041,4.167251,5.352918,0.292534,0.785002,9.630033,-5.287171,9.339427,-6.101131,-2.335090,4.047419,-9.435006,0.225636,1.121334,1.639155,7.488451,-7.758330,7.777681,-6.648559,-2.089200,7.613834,0.318476,7.762307,1.301376,-2.919467,-8.619416,-6.772940,-0.437561,9.372921,9.290609,8.644719,-8.975365,8.023845,7.589926,-2.200873,9.421327,8.038826,-7.403531,8.543968,9.805304,3.195421,3.098832,-9.278619,-7.248075,8.144766,-5.020791,-9.409749,0.957981,-1.845102,5.956677,-8.968710,-1.374707,-8.989060,-3.609237,7.820965,9.644709,0.948418,-8.204641,-6.902789,-3.918856,-5.344785,-9.557753,9.566270,-6.509992,-4.775953,-4.358191,-0.629194,6.785041,2.920436,-9.825167,8.256410,-2.160541,-8.051304,-6.202545,8.234186,-3.052092,0.955840,-5.140446,-2.554453,-7.420720,-8.824818,-3.322671,4.951347,5.569183,5.508535,6.919483,1.247482,-2.873396,-9.750512,-5.668401,4.866966,5.908331,1.356741,3.286240,-1.245080,1.144631,-7.152093,9.079795,1.459654,3.975349,-2.798480,2.211255,-0.240690,9.367339,-6.429891,-9.077908,9.024180,-3.382922,1.935355,-9.825641,2.764847,-6.859491,4.291968,1.596464,1.686125,-3.835654,-2.673343,7.856626,7.510669,7.293551,3.711219,1.269620,-2.320234,1.559637,9.899648,9.365762,0.044197,-7.651274,-9.410712,0.406531,-6.003778,8.366624,2.544117,7.174710,-3.020090,-3.127192,-0.193429,-0.598290,3.909616,-7.023032,5.093749,5.822998,-8.348708,-1.175041,-3.434167,-0.027606,6.429376,0.227530,-4.874411,4.736002,2.591976,-1.860492,0.161349,-9.252061,2.091338,6.755904,5.914625,4.589777,-0.932293,-0.421180,-2.877621,-2.068777,-8.976708,-8.333806,-8.989785,0.119913,-0.890557,-4.232266,-9.104926,-2.850055,7.217988,2.908328,5.223351,-7.964949,-7.708349,-8.319666,7.676903,-2.554249,-4.701403,1.187649,-0.619449,-4.878971,-1.775798,-3.780357,-6.700459,-9.610639,-7.078437,-4.800269,9.914037,4.204648,3.237116,-9.854799,-5.365265,-5.589520,9.466229,-7.003299,6.202773,-0.383198,3.883426,-0.384447,-8.682607,3.833061,-6.664515,-3.386553,6.852756,3.512285,0.278929,6.741015,-1.483945,-5.391900,5.674410,7.878843,0.818507,7.869688,-8.728358,-0.055099,-5.990026,0.404138,4.656761,-4.198564,-5.328771,8.612388,1.657994,8.350446,2.987681,-8.105685,-8.971519,2.080183,8.128249,-8.425077,-2.539244,-0.662300,0.330104,-3.377845,5.972908,9.386473,-9.115621,6.653856,1.575230,-2.845838,-1.626054,-3.157054,-3.815141,4.573300,-7.816949,-0.769328,-6.842292,5.047029,-9.640198,2.274024,5.264650,6.816880,8.107904,5.226802,-7.881808,9.507888,-9.096285,8.585893,7.692554,7.222269,3.391311,1.590255,-9.276689,7.188793,-8.688626,9.986033,7.955649,0.380308,5.995808,4.525795,-7.869963,7.670005,-8.468285,-4.049771,1.846889,9.065776,5.920306,-4.854342,-5.763634,-7.801873,-6.780479,-1.502327,5.456135,7.954754,-8.407936,-5.120255,7.782209,-6.619033,-6.546768,-8.731488,-3.970130,-0.040657,-1.737888,1.872910,-8.998965,7.870016,4.833673,-0.444873,4.651997,-3.759945,9.619952,0.655605,-9.343380,-6.234952,-7.845669,-5.465812,9.220580,-5.837646,8.190013,-2.674380,5.999551,5.490106,0.453370,1.355063,6.953245,-1.831635,-0.317179,3.312238,1.139800,-5.478205,-8.967033,-7.468689,7.909925,7.366436,5.620946,6.373785,8.055124,1.212044,-1.431445,-7.563005,-5.174346,-3.054296,-3.968100,8.945742,-4.556472,6.016701,-2.744957,-3.073321,-2.841259,5.238245,3.138439,-2.809541,0.296063,7.956112,8.942745,0.966276,-1.459379,-3.128921,7.766341,0.532307,3.906807,5.422157,-4.538794,-1.092778,4.375361,-0.801157,-2.427352,-6.746819,6.149413,6.056504,7.285752,-6.351136,5.003216,-5.641773,1.968442,-7.027462,-9.741520,-6.114380,8.952628,2.882024,-9.079964,3.131093,-3.916021,-5.651044,0.816859,-5.650097,-2.403402,-6.431243,-7.013335,7.300372,-7.782107,-7.198477,5.031405,-1.730538,5.430134,9.950929,3.210539,-0.689499,-3.761245,4.419643,7.069378,-4.061160,8.669516,5.223022,7.218895,3.887555,-3.951765,-3.671630,-2.982632,-7.812197,-7.656945,-1.833784,-4.073316,-2.474009,3.362513,-1.748441,8.045688,1.980678,0.246988,-3.258577,4.468715,8.535937,-9.482349,6.213705,-5.607151,-0.421618,8.097006,-0.210097,-6.509519,6.381445,8.424096,-2.383610,-5.965710,0.376415,-8.962595,2.386515,6.229968,1.067646,-2.628791], dtype = "float32")#candidate|7037|(2288,)|const|float32
call_7036 = relay.TupleGetItem(func_2795_call(relay.reshape(const_7037.astype('float32'), [11, 13, 16])), 1)
call_7038 = relay.TupleGetItem(func_2798_call(relay.reshape(const_7037.astype('float32'), [11, 13, 16])), 1)
output = relay.Tuple([call_7034,call_7036,const_7037,])
output2 = relay.Tuple([call_7035,call_7038,const_7037,])
func_7062 = relay.Function([], output)
mod['func_7062'] = func_7062
mod = relay.transform.InferType()(mod)
output = func_7062()
func_7063 = relay.Function([], output)
mutated_mod['func_7063'] = func_7063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6266_call = mod.get_global_var('func_6266')
func_6268_call = mutated_mod.get_global_var('func_6268')
call_7079 = relay.TupleGetItem(func_6266_call(), 0)
call_7080 = relay.TupleGetItem(func_6268_call(), 0)
func_5351_call = mod.get_global_var('func_5351')
func_5352_call = mutated_mod.get_global_var('func_5352')
call_7083 = relay.TupleGetItem(func_5351_call(), 0)
call_7084 = relay.TupleGetItem(func_5352_call(), 0)
output = relay.Tuple([call_7079,call_7083,])
output2 = relay.Tuple([call_7080,call_7084,])
func_7085 = relay.Function([], output)
mod['func_7085'] = func_7085
mod = relay.transform.InferType()(mod)
mutated_mod['func_7085'] = func_7085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7085_call = mutated_mod.get_global_var('func_7085')
call_7086 = func_7085_call()
output = call_7086
func_7087 = relay.Function([], output)
mutated_mod['func_7087'] = func_7087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6072_call = mod.get_global_var('func_6072')
func_6074_call = mutated_mod.get_global_var('func_6074')
call_7096 = relay.TupleGetItem(func_6072_call(), 0)
call_7097 = relay.TupleGetItem(func_6074_call(), 0)
var_7101 = relay.var("var_7101", dtype = "float32", shape = (10, 8, 1))#candidate|7101|(10, 8, 1)|var|float32
bop_7102 = relay.subtract(call_7096.astype('uint16'), relay.reshape(var_7101.astype('uint16'), relay.shape_of(call_7096))) # shape=(10, 8, 1)
bop_7105 = relay.subtract(call_7097.astype('uint16'), relay.reshape(var_7101.astype('uint16'), relay.shape_of(call_7097))) # shape=(10, 8, 1)
func_6536_call = mod.get_global_var('func_6536')
func_6541_call = mutated_mod.get_global_var('func_6541')
const_7111 = relay.const([[3,-9,7,1],[-9,-6,-4,-10],[1,10,-5,2],[7,-4,9,7],[5,6,9,3],[8,-6,-4,7],[4,9,8,3],[-9,8,-6,9],[4,-5,-7,-2],[6,9,-6,-5],[-4,2,-6,-9],[-4,4,-3,-9],[-10,-1,-3,-4]], dtype = "int32")#candidate|7111|(13, 4)|const|int32
const_7112 = relay.const([-0.472791,-2.303284,8.991077,7.319435,0.747170,-4.222359,-5.582121,-1.944683,6.061468,3.334788,-8.091439,9.714099,-3.353410,8.253390,8.909629,2.961225,7.387168,2.800249,-3.540399,-9.935690,3.074737,-1.251107,1.404944,5.948544,3.507489,1.187372,5.493572,-3.607321,-5.725584,8.017696,-0.360636,0.403924,-3.497337,-6.228502,6.340709,2.712989,-5.559131,-9.157360,-4.194448,-2.040254,-9.639922,3.531303,-7.006677,5.105211,5.610173,-8.764656,3.399456,-3.978646,7.535028,0.596917,0.279787,1.318718,-6.252217,0.968982,6.968165,-5.517069,7.906211,2.183870,-5.198217,-2.843922,0.453731,5.089063,-5.225675,6.406207,-1.070095,3.907436,6.043157,5.616930,-9.762801,-8.384788,-7.950761,-8.481790,6.617127,-7.405785,-0.961314,6.269930,5.770139,8.805503,-0.889539,2.754597,8.864069,-4.928087,7.996357,-6.474820,-6.686644,-8.439693,3.795072,-1.559034,-8.865019,-8.857067,9.206450,7.543991,-5.162335,4.165705,2.174774,-7.939119,3.092137,1.186083,-6.503056,-3.103464,-7.445099,-1.899966,4.812707,-7.428756,8.614615,2.483284,6.145583,8.808842,8.878316,-2.535467,-7.419361,8.630734,-9.696556,-7.242808,-0.075283,7.555572,8.614517,-0.097107,4.594747,7.513630,-7.310368,4.558773,5.281188,7.407265,1.137640,2.596552,-9.410367,7.407149,3.537859,-0.766751,9.607818,-7.444407,5.840334,5.781179,-5.143864,5.451063,3.204096,-2.848921,8.813734,8.434820,2.175072,-8.587584,6.501295,-0.907880,-0.173591,-9.390317,9.822646,-0.089943,-7.989424,4.115078,-3.174973,0.451624,9.567739,-3.429100,1.774385,-5.018843,-7.457666,3.713325,-7.984593,-6.285580,-1.869335,-9.131839,-4.077063,-6.007442,1.546772,2.416717,-8.168366,7.010362,-1.568115,-8.675182,-1.239685,-4.628933,-4.599573,-9.186792,-9.959171,5.764783,-2.705449,-9.539989,-2.286205,0.036891], dtype = "float64")#candidate|7112|(180,)|const|float64
var_7113 = relay.var("var_7113", dtype = "float32", shape = (120,))#candidate|7113|(120,)|var|float32
const_7114 = relay.const([3.303766,6.887420,4.837912,4.014309,3.466760,9.865454,-2.114590,-1.993208,-9.210267,0.409262,0.209242,-4.272785,9.065513,-5.551711,6.535407,-5.085246,-5.877297,-6.606694,-2.285842,4.893725,9.360264,5.499491,2.707365,-5.198189,-6.054672,-7.056871,-0.071029,7.661203,0.326266,-6.534371,-3.200015,-8.761224,2.071685,3.349759,-5.288376,2.611218,7.706124,9.491957,0.577687,-8.941518,-4.563176,9.443293,-4.231252,-0.170506,8.919041,-9.103049,-6.250369,-9.727723,9.069327,6.967915,-4.549673,4.220047,8.737560,-3.426906,0.937103,-0.813631,3.005032,-1.999111,-5.029964,-4.072008,-9.148822,4.527236,2.573273,-9.621267,4.938585,-8.157789,-1.780679,6.698919,-9.402854,-5.732753,8.335590,5.526012,4.134609,-5.566267,5.735328,1.229216,8.691004,-3.294896,-5.936904,6.005695,-1.384130,8.510795,9.607658,-0.786369,-5.228745,4.500389,9.061905,-7.748293,8.727068,-2.823400,2.843143,-4.260371,-9.329355,0.761619,4.567628,8.342245,-5.464628,-4.914748,0.232480,-8.984346,-8.378722,9.659569,-4.736068,-6.577463,-6.480500,-5.004096,-9.907384,-5.690773,6.047833,0.160346,-1.305172,-7.712839,0.597320,0.166043,1.917846,-2.988191,1.359152,0.841971,4.060974,0.645245,-8.010860,-5.081180,-6.266324,-0.022212,-3.213551,-4.456596,-8.478517,-6.156939,-9.256983,-5.535286,0.144391,5.037458,5.289926,-7.664665,-4.074955,-0.198921,-5.873754,6.604180,-7.571638,-0.294275,4.380506,5.198603,-7.294325,9.698231,2.457895,-8.422778,-5.311255,-7.598499,9.483172,-5.438277,-2.570757,-4.921274,9.112132,-0.952442,4.873404,3.708418,3.857089,-2.238552,-9.226686,-0.765999,-6.302787,-3.476086,-9.277317,-6.166385,5.880430,6.959737,3.335265,-5.747760,4.937645,-7.161171,-5.286373,3.068887,8.510075,7.125535,7.054531,0.100530,-9.312157,-2.889607,-7.501824,-6.639892,-8.594550,-6.791079,-0.202080,-5.100855,4.631949,-7.061374,-8.794468,9.089464,-4.432546,5.277607,1.066521,7.119960,-3.832617,-1.727608,-8.486710,7.456231,6.466678,-4.697112,-4.678184,8.586920,-3.626493,9.955220,-8.346456,-6.750285,7.635270,-1.744012,-7.335507,7.077831,-8.980118,-5.985877,-0.152974,4.809073,3.208941,7.223103,-4.984250,5.643104,5.803380,-8.307664,8.531744,-4.326945,-0.254183,3.281529,-6.968101,-7.828720,6.281001,0.599599,-6.478762,0.975260,-3.169687,2.211555,9.518180,1.096107,-9.336269,-8.838815,-9.382651,-5.866033,-7.268753,-0.722645,-0.441704,3.131706,7.799418,-5.793660,4.296149,9.984078,-8.824840,-2.942530,7.998674,-2.625379,1.502442,6.395326,5.076313,8.509171,-6.078819,-9.167050,-4.140904,-4.767525,-9.803466,7.229571,-9.196937,-3.569288,9.496282,-9.344779,-4.930051,-4.335523,-9.302113,-8.422069,-6.729747,0.454666,4.139366,9.162867,9.522742,2.223408,-2.798201,9.673773,1.548123,-4.784904,-8.467297,8.587634,9.968849,3.075761,2.628155,-1.304618,2.325254,-8.400979,0.954890,-2.326914,7.009608,8.827634,-5.322432,-2.640912,-5.707299,-3.037412,-7.426571,3.051061,-8.564587,1.087913,-3.488152,8.538532,7.004424,-2.870642,5.629113,9.203504,-6.290419,7.117929,0.442226,-1.992545,-6.220505,-9.270558,-7.571982,-7.584328,-0.012373,0.414674,7.622497,-8.064841,-7.491807,-6.880995,8.604546,9.104245,-1.487407,-6.084298,-4.785254,0.381918,-3.823799,0.100331,7.744898,3.015504,2.767778,1.612187,1.710444,1.266181,-8.575233,4.942479,1.131380,-8.617515,4.201073,1.002633,1.669949,-3.752655,4.378905,3.262827,-4.525818,-2.141478,4.647592,-3.326221,-3.045460,-1.283931,4.996608,-8.071798,-1.691419,-6.846441,-0.874203,-4.884488,-2.823466,8.733773,-5.617440,5.273354,6.117966,4.200807,3.338082,7.961006,5.665264,-8.531302,4.414063,-2.466696,3.009425,-8.320973,-6.188593,-2.613328,4.241545,-4.800670,-6.052232,-3.645141,-4.471454,-0.593019,-5.280239,2.208106,1.441015,-7.045275,-3.665490,7.104638,-2.673919,2.535300,-9.122264,0.249757,4.334328,8.456379,9.166037,6.959742,1.959840,4.154488,8.401267,-0.680368,7.861986,-6.087943,3.903511,2.403231,2.861713,-3.439633,-2.807841,8.071837,-0.334881,9.913258,6.521619,6.213358,-6.802739,-2.653503,2.586211,5.804998,6.809935,-9.739861,3.582920,-7.946139,1.390222,-3.480607,5.022702,6.610333,-0.873065,0.694622,-5.148516,7.316953,-7.141622,-0.205664,-1.230213,-3.419119,4.711359,-6.622987,-2.414655,6.016223,1.097541,-4.248559,-7.308462,-4.178987,-4.877832,-4.194927,-0.317060,-8.887615,1.384616,-0.874454,-2.869843,7.451663,-3.739202,-2.273508,1.037026,-8.349370,6.461513,9.722908,-5.036421,-4.443840,9.027995,8.344846,-5.462729,-6.181027,2.696212,6.100368,9.213625,7.430085,-1.311739,8.248481,-6.259651,3.629307,-5.978040,0.277328,-0.588260,3.712396,-0.609720,-8.918388,-7.157332,-6.457260,8.798015,7.930200,-4.286852,-5.875198,-7.908565,-6.059398,1.988931,-4.070525,-2.639142,1.162349,-8.329090,5.399409,8.739716,2.755525,-1.121710,1.427003,-4.456443,0.057522,-6.545002,4.552813,0.340719,4.783870,4.853139,-0.614846,5.979351,4.736779,-3.645757,-7.976544,-0.730565,-6.669472,3.121224,-1.746744,-5.089368,-7.716219,-3.178266,-6.064972,-0.343887,-3.475928,4.708164,3.941175,-1.095554,-6.589047,5.402751,5.785533,4.357505,6.806653,4.405658,-2.790397,0.132382,-3.440363,-2.868079,0.300366,-7.458622,9.522032,-7.270765,-0.078763,3.557944,9.481806,1.219981,-4.170939,-7.130521,5.758804,3.255724,-2.180008,0.283131,-8.214886,6.024533,-9.334345,-3.431909,8.918632,-5.584708,9.857881,2.136921,7.619029,6.180767,5.229019,1.701803,-7.700886,-3.976699,3.266051,9.539628,8.279661,5.798495,4.791729,4.884532,-7.740572,-5.229257,5.487454,-9.813652,9.924311,-4.541894,-2.261774,7.134688,5.622575,5.432379,2.269443,-5.719322,3.029425,-7.828608,5.068044,3.168776,-9.354701,-8.335888,9.801624,-5.211300,-8.763700,9.440057,-6.498470,2.010268,-4.204530,-7.182948,-8.267803,1.837009,-9.052968,-3.728757,7.758151,3.357135,8.396195,-0.056350,-1.118874,0.738604,8.872210,4.171258,-5.259066,2.106057,1.505012,-0.839987,9.243271,1.674479,-0.041892,1.853392,-5.573105,1.837393,-3.718632,-0.195879,-9.885791,-1.399398,5.846549,0.028493,-0.718034,-0.575986,-5.021088,6.692379,-6.377397,0.127675,-2.307231,1.459615,2.091824,5.928754,-0.541590,-5.027541,7.157834,-8.607050,6.067218,-8.750776,5.803777,4.288882,-8.314044,1.054523,-4.835805,2.449545,6.817490,5.478363,4.269161,7.013520,-9.923536,-4.076932,-4.137292,-3.903315,-0.397085,2.675591,-2.960257,5.473702,-2.565515,8.478421,3.930028,0.814725,8.823747,4.346855,3.279857,-2.310295,-4.144886,-1.014691,-6.157839,-1.119399,2.336723,-0.357610,3.810813,-0.831348,-1.582744,-4.371940,-3.414295,-0.847626,-9.589942,-0.265747,-4.718596,5.245209,4.730504,4.373119,5.371693,-2.558221,-5.667658,-2.742126,-5.925766,7.813203,-8.949847,-8.727628,1.760167,2.027506,-8.236682,-1.109134,-0.841776,-2.871725,8.342687,0.829742,6.025225,7.428238,-8.203201,2.355865,6.430778,7.411206,-9.085054,-1.655406,8.000950,8.331930,-4.162228,-9.399563,-2.651690,-9.549604,7.632205,-2.418485,-0.955857,-7.458013,4.935966,7.441951,-1.031770,-0.861155,0.323008,-3.539179,-9.860313,-8.862225,5.537348,-3.454431,1.614791,9.635893,-2.460475,-0.673048,-1.918290,-6.427463,-6.423397,-7.007893,-6.883657,-1.524901,5.062048,-2.366324,-9.390075,-9.317840,-5.534434,6.622659,-5.023950,-7.555158,-3.619283,3.642961,7.340004,-4.295132,3.070091,-4.307598,-4.059496,1.701698,1.476962,3.815522,2.151034,-7.234349,-7.200562,0.290624,-4.058176,-6.060475,-2.807630,1.967507,1.407617,-4.336178,-5.913862,-9.336037,8.559210,2.838061,-8.921420,-2.393527,-3.513010,6.703917,7.858881,2.353005,-4.582309,-0.395552,4.523779,-5.093123,-5.248532,-9.792197,6.044583,6.039632,-5.877263,6.625239,2.851886,-2.472223,-4.770263,4.145994,7.204661,-9.112830,-0.519147,-4.039798,-2.000762,-1.778136,9.717042,-4.910717,1.168675,2.425322,-8.896406,-1.125636,4.563005,9.246716,-1.692563,2.990685,-7.401498,8.559448,-3.069550,-8.495860,-5.282510,8.026437,0.129240,-9.472141,5.137294,8.832515,9.001332,-0.873505,-2.515193,-9.190556,-6.952774,-2.160393,1.474666,3.939849,-0.923613,2.628875,-5.002226,-1.143841,-2.643924,-9.410263,7.177274,9.968207,-4.838943,9.860860,9.430876,0.590783,2.180396,-4.350384,-6.656846,-8.642934,-8.757290,4.339342,9.135146,-9.792207,5.754200,2.868579,-2.435575,5.530118,-1.225349,-1.401077,-4.598241,3.599056,9.280423,7.378787,4.107688,-1.410305,4.715411,-1.607206,-5.934107,-5.056012,-8.043970,-3.029039,-1.911500,3.437196,-8.180879,-1.994671,3.510930,-5.674376,-3.345927,-1.328720,9.841389,7.735126,6.613308,8.878454,-4.296150,6.920095,-9.340270,-0.616046,9.711446,2.588937,4.919520,-2.940674,-5.704855,9.227196,-6.157682,-5.101358,4.882948,-3.338633,-5.134342,-7.758919,2.883747,6.850738,5.780488,-6.294343,5.777019,-8.108974,-5.328556,6.094383,4.653298,0.364027,6.292394,8.418275,8.145545,1.819546,-1.712805,-4.787865,1.471192,0.343219,1.882806,6.230257,0.137945,5.325020,-4.478107,-0.921301,-3.959957,-5.101224,-8.830158,-2.630367,7.544417,8.849485,5.851093,-4.270052,9.612088,3.809441,6.461569,8.126919,-7.283189,-8.305277,5.672765,-3.430218,-5.941177,6.859606,-1.464337,-5.118325,6.514160,6.664194,-9.053724,3.713974,8.762924,-5.741054,0.248050,-3.533508,6.944037,6.874659,0.302137,-6.828773,-2.478328,-4.134542,5.784376,-3.563116,-6.395876,2.696101,3.601347,-9.079138,1.371427,-8.451913,-1.535477,-5.350186,6.207602,0.843000,3.481179,4.385588,3.369471,-3.709466,-4.547253,-5.421834,0.146995,0.143264,-7.652329,0.952267,6.915490,1.688432,-6.121066,8.955135,3.484021,5.064551,-2.484182,-4.565875,-5.668329,-4.666371,8.321552,-9.856906,-6.315932,-4.033865,5.313257,-3.698410,2.135150,0.251545,8.594510,0.289655,3.510564,2.844118,0.280075,0.599799,-0.928154,8.088523,-8.218414,-1.684224,3.379695,-1.927747,3.456613,4.459249,-9.435599,-6.059712,4.048124,-9.142740,-0.552481,-5.877976,7.173919,-1.358211,6.436949,2.138519,5.701493,-6.090954,-4.159585,0.281407,8.554966,-1.414060,4.334251,2.999080,3.840695,8.705899,1.696120,0.232784,-4.118731,6.310512,9.803471,9.480063,-8.209996,-8.436069,-6.547598,-5.259450,-1.481843,9.614585,-3.987533,3.593295,-2.204108,4.464155,-3.203775,-8.509591,-0.829476,2.039260,6.148124,-6.425134,-9.179544,-4.809919,6.540680,2.309059,-3.286442,7.125452,4.163595,-8.990919,-2.196392,-0.215251,-4.622969,3.329162,-0.931521,9.549938,0.123115,8.425320,-2.998624,1.210699,4.497332,8.384334,8.558100,-8.818816,2.729009,4.568640,-6.105293,4.023504,-5.280049,-6.399992,1.089000,-7.801682,3.596528,-3.412659,-3.678368,3.564300,-3.078500,0.073787,-5.796697,9.691345,-3.515241,8.920478,-2.679391,5.981159,0.057835,3.226815,0.098462,7.233751,5.190230,-7.879981,2.812255,6.823719,3.924440,-5.391910,-7.295623,1.949307,-6.428673,-0.401086,2.312807,1.468703,7.453607,7.605013,1.056005,7.583948,6.542148,-3.671562,-9.453332,-6.365351,-7.048394,3.416571,-1.633131,0.436951,2.012570,5.456488,7.136386,9.181612,0.972954,-2.230902,1.515386,-9.238128,0.098537,-0.119462,-6.731847,3.169621,1.294384,-4.577910,-3.861647,-0.975007,9.421786,-3.696869,-6.994401,7.946360,3.069675,-5.521097,9.754858,4.443006,9.785383,-3.807576,-3.563657,-0.741848,-8.578743,-2.179215,-5.471031,-7.091070,-2.971002,3.997023,-2.493225,1.043783,-5.537206,8.077287,-0.093540,-6.808776,-6.354717,3.188004,5.301701,-1.409201,-6.809673,-1.790964,0.535320,-1.118273,2.748392,-7.518625,-6.933673,3.490679,-9.367276,9.867387,7.589724,-6.352865,-7.143129,0.638038,-5.115096,-0.747636,-7.958190,7.083128,1.616170,6.498240,3.349217,0.768291,7.731811,-5.845784,7.077405,-4.922571,-0.737817,-5.217939,5.252843,-1.303660,3.711574,-9.578972,0.768844,3.228530,-3.706902,8.842136,-9.973658,7.329203,-3.023636,0.156931,4.604772,-2.371596,6.917247,3.800410,-5.178495,-8.326640,-0.603792,5.068874,-5.945677,-2.771711,-3.095827,9.462694,-5.786607,-8.397905,-9.870453,-3.829282,-1.123718,5.240178,5.663791,-2.412890,-3.794949,9.991421,9.669952,-2.894742,4.561105,-6.955663,9.855281,7.710937,8.938771,-1.498240,2.348525,2.336161,6.344172,1.902233,6.524001,8.370795,-4.924337,-5.211642,4.030193,-5.104373,-3.192972,-2.573525,-8.301083,4.068563,-3.490234,0.334420,7.149851,1.882373,-4.920263,1.200637,-7.447403,4.930997,-4.741411,-3.550060,2.707898,-1.219454,-2.614824,9.397716,-6.878445,-7.807946,-7.244913,4.056694,-9.393275,-7.800208,2.264942,9.257869,-2.779640,3.884997,-4.049558,9.108058,-8.496035,8.536035,-0.582124,9.910370,-0.847247,3.152495,5.566507,-9.274561,1.726043,-3.007352,-5.368641,-2.279810,8.948665,0.354811,-2.199233,6.696075,0.721791,5.550963,6.168150,-4.152329,-4.716917,-7.876826,-4.325923,4.361337,4.471560,5.529368,3.304850,3.190128,6.658233,3.236254,6.271584,-9.181604,3.814464,-0.940629,-3.148126,-6.795276,3.558807,-1.511202,7.367755,6.252217,-9.532036,4.875002,7.336067,-8.650740,8.847066,-8.898462,-8.259003,6.578234,-6.506863,-2.921341,5.181475,1.534513,5.161987,-7.930375,2.509600,7.937119,-4.801810,-9.794222,9.684715,-2.913251,-1.063595,3.993458,2.162727,-2.398674,1.666772,-3.990118,-8.063205,2.700135,-5.494793,-2.500756,0.949728,0.767446,-3.879500,7.615966,-8.669979,8.733211,-8.314349,1.749731,0.011083,9.811136,-3.774650,8.581731,4.492595,-6.323296,6.485033,-0.639799,-0.894918,-1.069558,9.195060,6.451670,-4.034631,-3.829838,6.617158,-5.160750,1.082879,9.276410,-4.788051,-6.999981,0.306109,9.226646,-4.835954,-6.449562,6.993748,4.205618,-3.352396,-8.871496,3.794414,-0.205502,-3.111632,-3.591609,-4.164155,7.910973,-5.750838,3.419899,-3.581979,-3.003434,-5.068427,0.385844,-0.559735,-4.716655,3.546179,3.879226,0.289982,-8.017903,-6.099288,6.888388,-1.298738,6.328966,0.033863,4.615327,7.090346,-4.166449,-9.540808,9.577117,-9.130482,5.612880,-2.057232,0.192401,-6.255530,6.827244,-5.503661,-3.074826,9.753747,8.425692,-1.348568,-9.249305,7.566499,3.671584,4.738305,-1.456758,-7.998381,6.967761,-4.725480,-6.223555,-4.360109,0.634847,-4.381884,-6.511766,-8.457115,-3.064635,-3.343813,-8.968949,7.795820,7.915398,0.297322,8.683110,1.248902,-1.793153,7.048325,5.035611,2.950641,-2.499504,-6.133738,0.676135,-6.808238,3.599701,0.646851,-2.334714,7.827966,8.152992,3.077054,-8.822371,5.508978,-2.301055,7.945106,4.060839,7.714831,-8.057723,-9.599307,-9.221790,-0.719938,6.909126,8.841591,-6.055569,9.642834,4.053041,-5.806812,7.565307,5.657084,-2.830662,4.717430,6.356077,6.412695,-4.024670,4.714868,5.392048,-4.257038,6.773609,-7.257267,-3.446308,1.334281,3.763870,9.913691,-1.156700,-0.927344,6.652734,-1.371273,-6.277950,9.522924,2.239531,1.155058,-5.833517,9.634722,-1.470376,9.158193,5.521600,-9.617194,9.302274,5.855402,-7.586760,-6.319725,-8.246357,-0.852075,3.242144,9.798760,7.959789,7.502015,2.772733,2.167411,-3.271304,-7.961788,-0.907400,-5.188364,3.526260,7.931050,-1.285498,2.365451,-2.130958,3.229971,1.416014,-1.194216,-0.373838,-8.520643,-1.067195,6.565413,0.532120,-7.331282,-1.855167,4.094067,-0.793316,-7.514816,-4.888952,9.675399,2.702080,-9.842009,-4.173510,4.932966,-2.434283,-0.860960,-2.877356,-7.041069,0.720673,8.967476,8.824035,5.496595,7.529864,-0.063662,-5.168659,-2.965735,9.310797,-5.358630,3.365053,-8.585276,-7.750869,-2.988535,-0.400817,-6.330307,6.141750,4.529017,-6.159729,-9.516216,-1.192525,0.976960,1.654642,2.681431,3.749509,-8.023535,0.817798,-1.523302,7.996037,-4.794068,5.063819,5.947836,-4.417699,-9.613145,-3.062331,-9.323369,6.610961,3.605105,2.267254,8.154263,-4.880367,6.841063,-9.530492,6.616653,-7.869183,9.185238,-8.673795,-5.414826,-9.872539,4.039460,-9.577244,4.142399,-2.368887,-9.140448,9.567252,-7.525622,9.557190,-6.218110,7.141171,2.651938,8.023939,-0.675664,1.617440,9.273412,8.384780,-8.916877,-2.571369,3.194474,-0.659764,1.955676,-5.420728,-6.384586,8.637529,8.673231,-2.853574,6.801012,-1.286887,-5.332332,-1.694280,9.591989,-4.490758,6.320520,5.606453,0.883999,-9.816261,-7.133280,-4.947508,-8.037271,1.058126,2.965892,-6.971728,3.051700,-4.193777,7.494507,5.270593,-8.148286,-6.400466,6.460982,-5.934906,-9.314226,4.679195,9.786028,4.092471,2.960723,-2.611948,-4.518815,1.654126,3.609453,0.319876,0.206289,5.626567,2.190007,1.665564,6.597175,1.141744,9.804489,-6.180132,4.441146,-2.802844,-6.873006,5.528402,-7.171760,0.777373,-4.382282,-1.035363,4.963034,8.307705,3.893893,9.235571,-0.720152,-8.162473,3.316116,9.526810,-9.643660,-5.436410,-7.904967,-1.604678,-0.226472,-6.354526,-2.735655,-9.711387,-6.041509,-1.159972,9.689069,-8.477200,7.243448,4.941493,-7.198837,1.091896,-3.228200,3.649981,5.421614,2.824535,0.022336,-0.822680,-7.987187,-6.187724,-4.972370,9.742044,-4.173512,2.177568,-5.384002,0.539972,7.758802,-1.955760,-4.548213,-2.035061,7.923197,8.075649,4.771300,-1.797308,3.630810,-2.985202,-1.351223,0.615571,-1.720599,-7.845051,8.712212,6.277550,-8.943064,-3.018045,6.350446,-2.392291,8.596099,-5.799474,6.493850,-0.888318,3.954833,-5.144514,-2.586642,-5.102272,-2.607234,-2.592368,-9.359466,8.527031,1.262061,6.860080,-9.252093,1.423006,-3.230367,6.593041,-1.820728,-7.614966,-9.855717,0.095648,-3.681965,6.744840,-1.137384,-0.786810,0.380457,0.008466,6.370303,-2.237011,-2.868811,1.334995,9.581556,-5.030320,7.396699,6.910922,6.988304,-1.135746,-0.524534,6.876925,6.677429,-5.108807,4.487247,9.540270,-8.599613,-3.524559,9.247465,8.920205,-9.216009,3.002769,-8.997957,-8.842046,8.698754,7.557738,-9.610821,5.269406,-4.669143,9.726306,4.200097,4.075274,-9.772514,6.963424,7.753071,-8.281137,-0.472369,3.853154,-8.930849,9.767845,7.486768,8.658861,8.214907,1.616946,-1.910107,0.013622,-3.488250,-1.282746,-8.354938,-3.228214,-7.343166,-5.960172,-8.192742,-1.166305,0.929246,9.610374,-0.112905,-5.620269,5.933674,-1.499747,-8.144981,1.629907,-1.874831,5.566929,3.843271,-1.071519,-7.790394], dtype = "float32")#candidate|7114|(1800,)|const|float32
call_7110 = relay.TupleGetItem(func_6536_call(relay.reshape(const_7111.astype('int32'), [13, 2, 2]), relay.reshape(const_7112.astype('float64'), [180,]), relay.reshape(var_7113.astype('float32'), [6, 20]), relay.reshape(const_7114.astype('float32'), [1800,]), ), 1)
call_7115 = relay.TupleGetItem(func_6541_call(relay.reshape(const_7111.astype('int32'), [13, 2, 2]), relay.reshape(const_7112.astype('float64'), [180,]), relay.reshape(var_7113.astype('float32'), [6, 20]), relay.reshape(const_7114.astype('float32'), [1800,]), ), 1)
func_6266_call = mod.get_global_var('func_6266')
func_6268_call = mutated_mod.get_global_var('func_6268')
call_7116 = relay.TupleGetItem(func_6266_call(), 0)
call_7117 = relay.TupleGetItem(func_6268_call(), 0)
func_2669_call = mod.get_global_var('func_2669')
func_2674_call = mutated_mod.get_global_var('func_2674')
const_7121 = relay.const([3.539465,7.090391,3.551876,-0.161447,-8.531016,-1.143767,1.280627,-4.269359,-9.803363,-7.155023,-2.466615,-8.419266,5.808371,-2.731052,-2.485435,-5.627960,-1.078284,-4.595991,-3.967862,-1.725051,-8.064313,-4.774757,-8.740887,3.759086,7.854637,-4.145885,3.066185,8.064175,1.895730,-3.218172,-0.520447,3.994816,-3.262456,0.971047,-3.553138,8.901318,-4.469764,-2.220572,1.659079,9.825612,-1.352827,-7.479244,-6.324297,-3.228159,-0.629763,7.900829,5.267250,6.964196,8.464813,-0.007713,7.931346,-2.062390,8.752132,-3.706276,-7.571182,6.719309,1.354962,-4.423615,9.283892,6.789444,3.761807,7.079369,9.125524,4.356116,2.763105,1.610696,0.052876,-7.204224,-7.483259,8.793451,9.102569,4.525963,9.871040,-1.613223,-7.902431,-3.416582,2.063235,-8.331481,-9.078265,4.444644,-6.076700,-9.485744,-0.763848,-5.081722,8.039623,5.210088,7.683132,-2.019577,-9.800914,9.292912,-3.962007,8.186742,5.237752,5.206239,8.575759,2.850504,3.420930,4.847388,5.473561,-6.358574,-1.705313,0.159649,3.264530,-3.753476,-6.114853,-8.418614,6.709470,-3.890478,-5.590907,-0.978257,-5.448167,6.591560,-6.999168,2.144806,-9.493415,-6.270179,9.077604,-1.073620,2.447186,2.254340,4.798765,4.878585,2.890615,6.435212,4.304104,6.238935,-8.398685,8.565957,1.214181,-7.141506,-2.562166,-9.988041,-5.900483,-2.431549,2.168308,8.038374,-7.943522,4.924967,8.236500,7.474039,1.412945,-1.556979,2.474859,-5.450916,3.038621,-4.721307,8.908147,9.367276,-3.850620,-6.309914,1.260409,-1.648616,-9.539016,4.833380,-3.252131,-5.159390,4.832420,1.814745,-0.896801,-8.264858,-5.159136,5.998003,7.551251,4.193357,0.563341,-1.937730,-0.610352,-5.241702,-8.412958,-7.124374,-3.226813,-1.128594,4.533895,-4.001047,5.571759,9.643301,8.384931,-8.774224,-8.742066,-8.561857,2.910454,-9.989871,6.168876,-5.956955,2.076088,1.509551,9.947998,9.723566,5.367728,-9.838040,-2.330276,5.981277,-0.320443,9.802092,4.273976,-0.716904,-4.197987,-3.627307,9.061904,8.681277,8.388994,-3.076503,4.303502,-8.560598,5.773485,6.386522,-4.582553,-9.553901,-5.222829,1.041689,7.228657,-4.926940,1.076586,-6.070700,0.483759,1.616068,-0.721185,4.173979,6.868018,-3.395682,-2.889665,4.181121,-4.858243,-8.200499,0.934124,2.966724,1.584668,-7.046529,-0.239339,-0.176579,-4.414492,6.037557,4.531727,-1.198820,-1.574790,-9.633368,2.889060,1.507652,5.337884,-1.280293,-4.484238,5.481484,-3.471889,-6.487140,-5.538577,-0.187830,-0.256628,2.831275,0.838420,-1.012355,5.644439,-9.658511,-8.292307,-7.833366,5.788646,-5.158169,-5.177347,-2.018752,4.072907,-2.443444,2.199685,4.271524,-1.239275,6.356344,-9.035214,2.317488,-1.189353,-9.035607,1.129042,-9.719698,-0.729583,-3.705951,0.580950,6.131650,8.546447,-6.862110,-7.302583,-7.119116,7.128134,-3.465515,-9.811711,8.209912,-4.530179,8.369247,-6.189601,-6.828681,9.313662,-8.866043,6.650229,7.467748,2.161931,7.330239,1.146542,-2.013719,-5.523345,4.243538,-4.496409,1.236947,-9.052467,-3.855489,7.739576,5.063839,-5.996580,9.645462,0.904676,-9.616500,-1.993101,3.722393,-3.723001,-1.393020,-1.711816,5.023780,-6.904794,4.641548,4.410584,-7.531802,9.838511,5.319276,0.220522,4.337264,-0.470570,8.829892,-5.250808,-3.379910,-0.484746,5.426717,-3.953829,1.504005,3.096956,-6.324059,-2.992473,3.797348,-8.624505,9.010721,4.840298,1.697145,0.206172,4.701552,7.344560,-6.240498,-0.044951,-5.832481,-6.050928,-5.755582,3.932225,-5.621517,2.687875,6.552388,9.161924,9.604751,1.209194,-1.293115,0.355770,-3.514745,4.083389,-1.349409,-3.448706,6.630795,-6.576496,2.119379,-7.114236,7.445610,7.763993,5.076879,-1.800631,-2.034675,2.219147,-2.204634,-7.999067,7.223791,8.556390,4.364966,9.214028,-9.271198,-8.467221,9.632076,7.481191,-7.112220,3.713795,4.956316,-1.084632,1.467839,-5.282389,-7.274579,2.797850,0.307649,4.240074,-4.954066,9.478181,-2.217968], dtype = "float32")#candidate|7121|(390,)|const|float32
call_7120 = relay.TupleGetItem(func_2669_call(relay.reshape(var_7113.astype('float32'), [1, 10, 12]), relay.reshape(const_7114.astype('float32'), [15, 10, 12]), relay.reshape(const_7121.astype('float32'), [195, 2]), ), 0)
call_7122 = relay.TupleGetItem(func_2674_call(relay.reshape(var_7113.astype('float32'), [1, 10, 12]), relay.reshape(const_7114.astype('float32'), [15, 10, 12]), relay.reshape(const_7121.astype('float32'), [195, 2]), ), 0)
output = relay.Tuple([bop_7102,call_7110,const_7111,const_7112,var_7113,const_7114,call_7116,call_7120,const_7121,])
output2 = relay.Tuple([bop_7105,call_7115,const_7111,const_7112,var_7113,const_7114,call_7117,call_7122,const_7121,])
func_7133 = relay.Function([var_7101,var_7113,], output)
mod['func_7133'] = func_7133
mod = relay.transform.InferType()(mod)
mutated_mod['func_7133'] = func_7133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7133_call = mutated_mod.get_global_var('func_7133')
var_7135 = relay.var("var_7135", dtype = "float32", shape = (10, 8, 1))#candidate|7135|(10, 8, 1)|var|float32
var_7136 = relay.var("var_7136", dtype = "float32", shape = (120,))#candidate|7136|(120,)|var|float32
call_7134 = func_7133_call(var_7135,var_7136,)
output = call_7134
func_7137 = relay.Function([var_7135,var_7136,], output)
mutated_mod['func_7137'] = func_7137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_7215 = relay.TupleGetItem(func_4770_call(), 1)
call_7216 = relay.TupleGetItem(func_4772_call(), 1)
output = call_7215
output2 = call_7216
func_7241 = relay.Function([], output)
mod['func_7241'] = func_7241
mod = relay.transform.InferType()(mod)
mutated_mod['func_7241'] = func_7241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7241_call = mutated_mod.get_global_var('func_7241')
call_7242 = func_7241_call()
output = call_7242
func_7243 = relay.Function([], output)
mutated_mod['func_7243'] = func_7243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7295 = relay.var("var_7295", dtype = "float32", shape = (4, 1, 14))#candidate|7295|(4, 1, 14)|var|float32
uop_7296 = relay.log2(var_7295.astype('float32')) # shape=(4, 1, 14)
func_3988_call = mod.get_global_var('func_3988')
func_3990_call = mutated_mod.get_global_var('func_3990')
var_7307 = relay.var("var_7307", dtype = "float32", shape = (390,))#candidate|7307|(390,)|var|float32
call_7306 = relay.TupleGetItem(func_3988_call(relay.reshape(var_7307.astype('float32'), [390,])), 2)
call_7308 = relay.TupleGetItem(func_3990_call(relay.reshape(var_7307.astype('float32'), [390,])), 2)
func_5067_call = mod.get_global_var('func_5067')
func_5072_call = mutated_mod.get_global_var('func_5072')
const_7314 = relay.const([-9.921082,-3.495641,-0.297314,-8.034315,0.801653,1.345956,4.505208,0.805006,1.529384,-0.725293,1.934793,-7.391252,-9.020135,7.172739,-5.053043,0.049103,3.581894,-8.332877,-8.904345,0.734121,-2.184887,-0.438990,9.016151,-4.441723,7.025311,-2.121172,1.661706,2.261819,4.882509,9.955596,8.624433,7.448990,-6.570378,1.658772,-3.475642,8.520023,3.510747,-2.172361,0.833232,1.065115,-6.895659,8.287184,-4.396208,9.833407,2.364214,-1.755717,3.964221,4.778936,0.412861,-6.776383,-1.057995,-0.161243,7.179369,-1.179844,1.824209,4.338489,-3.827304,5.156776,2.971300,-6.224479,4.862359,-4.752437,-4.395956,-9.322816,-3.669712,8.670279,-6.624896,-7.889097,2.115831,-3.933822,9.026743,-1.436251,-8.772329,-2.421885,-4.465526,2.080358,4.405969,-1.848636,1.523828,4.391285,-2.471049,-1.848346,-6.448881,-1.007712,-1.906893,-0.040104,8.117647,1.296834,-4.661420,8.373402,-8.399904,-2.997364,-4.465873,-8.258389,-5.086683,3.556789,-2.486941,5.455812,0.229551,-8.127489,3.291484,9.202368,0.870354,-7.773210,-0.015797,-7.836593,-0.719701,3.681041,-7.956816,7.768979,2.826297,9.797236,-2.136629,5.944839,-1.003462,1.597286,-9.071980,-8.610675,8.870631,-4.675209,6.605080,3.891252,7.247574,-4.956699,-9.761452,-1.317881,4.162725,6.153121,5.400355,3.547541,9.162647,5.175963,1.945576,1.667801,-4.709991,-2.448535,9.528400,-0.283969,-2.922156,-1.101023,-1.836125,8.668735,-9.169829,3.701323,2.226069,7.979025,-2.334594,-7.382184,4.371204,-9.331167,7.442756,7.267737,-2.587448,-0.271152,-2.258417,0.853480,6.474247,-3.542261,-8.627538,5.948632,-4.018754,-5.165090,8.238070,-1.699106,-4.412103,9.238443,-2.033019,-9.612546,-6.092743,9.546518,6.682139,0.184135,7.675029,-3.821160,4.155226,6.675600,7.160835,-5.817054,3.284424,7.554082,-7.825125,8.004830,1.547761,3.808533,-8.728359,-1.786086,-0.290705,2.181674,-5.487859,7.531893,1.764547,7.339341,-7.690854,-5.207213,6.534245,7.585091,-4.490101,-6.328573,7.925672,2.800834,-0.332057,0.021399,2.158629,1.420187,3.684642,4.247263,1.571448,4.924325,4.341706,8.073049,7.095905,-4.742119,-2.361998,0.175063,-8.439853,0.539985,-6.673934,3.945952,6.931467,0.880769,6.571540,-7.474196,-8.199009,-6.459375,5.559526,-0.572845,9.122139,-0.549964,5.947005,7.234533,-1.362306,-7.948976,0.456020,-7.831297,-1.482028,4.398269,-5.055572,6.213606,8.244824,-1.472005,0.919340,9.836125,7.024260,-8.213932,2.718074,6.807817,4.614172,5.180175,3.766659,0.351397,0.157413,-7.049586,-7.287520,-3.840579,4.386665,-4.155690,0.542676,4.908203,0.700677,4.553266,4.407414,-0.766190,9.704819,-7.195990,6.049313,-2.832481,-1.539690,5.934970,-9.216235,3.908037,-8.507771,1.750429,0.069592,6.332368,-1.028777,-3.588523,2.518042,-9.130233,-8.811529,5.743762,3.436936,-1.945267,-7.156748,-6.323736,-0.271695,7.979623,-2.981158,-9.370021,8.076608,-7.907325,8.123375,-3.211608,-9.152441,5.698938,7.657969,-3.510632,-3.053448,-9.338975,-8.050080,-3.313729,-9.570137,-7.446738,-0.113821,7.985735,-4.658438,0.884511,-6.873818,-8.299146,0.401311,8.857846,-9.932781,8.140623,-7.602735,-8.641169,-3.870156,1.387613,-3.035718,7.233933,6.357555,-6.298601,4.059069,3.211829,6.046537,-5.698509,0.995549,5.788212,9.477190,-3.024965,7.547697,0.718036,4.680357,-0.743469,-0.584334,-2.976777,-6.675748,7.127406,2.916035,2.108937,-7.593488,9.953750,2.959581,7.700130,0.795308,9.496914,-4.575221,-7.353917,7.097251,7.768561,8.314610,7.436083,4.960960,7.965617,1.854987,5.290035,-0.773594,5.713875,-4.685585,-8.593622,2.000565,-0.536329,-6.678163,9.878005,6.878709,1.294714,9.592151,3.697186,5.994154,6.046264,9.065257,-9.132593,1.428050,-4.571164,3.962293,1.360651,-2.345159,-4.203599,-2.327278,-2.423365,6.263433,-1.585178,2.657889,4.117449,-9.125597,9.568449,4.052044,4.113662,-6.425277,-9.370364,3.755616,-2.222352,1.580345,-1.173321,-2.611033,-1.009778,8.500351,-5.927848,-5.449185,4.800315,-5.521706,-4.189228,9.354377,-8.246525,2.582869,4.488398,-4.171353,-0.280397,-4.785531,-9.089378,-6.055714,-7.067890,9.132403,-2.719686,-4.407129,5.726179,-1.358459,1.788201,6.220282,5.831231,-5.054500,2.089204,-8.123944,6.396741,2.302055,-5.815478,-7.770749,4.543212,7.222842,1.000090,6.728281,6.851079,-5.651319,0.283763,-1.472209,0.876448,5.877795,-6.028888,-5.269643,8.056029,1.232692,9.981183,-4.232929,6.757580,-9.456062,-9.446487,1.944609,-9.586630,-7.257034,-6.543109,-4.174431,4.311748,-7.525144,-6.612757,7.948882,-1.491347,4.697028,-2.235638,-9.823058,4.770494,-4.764306,0.158136,9.723721,-4.961208], dtype = "float32")#candidate|7314|(462,)|const|float32
const_7315 = relay.const([-2.730268,-3.856927,-7.073602,3.592294,-1.887874,-5.621251,-4.710893,8.833419,-0.978488,5.689692,-2.900137,1.400860,-0.890980,5.471454,-4.847459,-4.922027,-4.472714,1.070903,4.009881,-2.041240,1.283649,3.435642,-5.776218,-1.045238,1.753289,2.949335,-8.587564,-0.745042,-8.075739,4.516755,-5.887231,9.796422,-4.220097,7.485346,-2.096768,5.875413,-6.330095,1.124841,0.295149,4.426446,6.096982,8.227566,5.595972,6.876182,9.330177,-8.648727,-2.981975,-5.861920,7.532410,-1.844774,-6.933834,8.758564,-7.733985,7.588464,-6.201045,-6.764510,1.833123,-2.533779,0.065896,6.414705,-5.727856,-1.407993,5.888699,0.762843,-3.262506,-3.616225,2.860318,5.448026,-5.258109,0.021584,-7.134988,3.747138,4.611792,-6.276146,3.384182,-7.924652,-2.398294,-5.378389,6.373084,-0.707516,3.001158,-9.930987,-2.049263,-2.638116,-3.886126,1.834435,8.422475,8.087869,-8.459705,-4.598251,2.033685,1.633335,0.556234,2.145087,1.057257,6.459583,8.639442,8.070239,8.937474,-3.370887,-0.517022,-5.904682,-8.772571,-7.291440,-2.598317,-2.510616,6.011697,0.578106,7.026584,-8.616133,-0.332230,8.244533,6.126934,1.846070,-9.272423,9.343203,5.778507,2.139943,3.444914,3.960382,-2.473342,7.200142,6.896130,-5.223119,8.931829,-9.422352,-4.175756,5.885944,-7.867736,6.502069,1.080052,0.277435,-8.318146,-8.020290,9.863268,6.874055,-0.325123,1.192975,7.964660,-2.066543,-1.744213,-9.990758,6.854804,8.065681,-9.264359,-2.715649,7.775203,3.579479,-2.427391,9.541213,8.817362,9.472949,4.126791,7.779961,9.854634,8.846940,-7.341652,-5.593564,-5.928763,-7.949301,-7.991158,-9.809740,-1.434414,-4.913099,6.879463,-9.776762,-3.473411,-9.942800,4.929585,2.242935,-8.206359,-5.363213,-0.271501,-6.568850,-8.902808,-9.947852,6.830097,-8.146886,-9.894013,9.766160], dtype = "float64")#candidate|7315|(180,)|const|float64
var_7316 = relay.var("var_7316", dtype = "float32", shape = (7, 5))#candidate|7316|(7, 5)|var|float32
call_7313 = relay.TupleGetItem(func_5067_call(relay.reshape(const_7314.astype('float32'), [462,]), relay.reshape(const_7315.astype('float64'), [180,]), relay.reshape(var_7316.astype('float32'), [35, 1]), ), 5)
call_7317 = relay.TupleGetItem(func_5072_call(relay.reshape(const_7314.astype('float32'), [462,]), relay.reshape(const_7315.astype('float64'), [180,]), relay.reshape(var_7316.astype('float32'), [35, 1]), ), 5)
uop_7320 = relay.exp(uop_7296.astype('float32')) # shape=(4, 1, 14)
func_4707_call = mod.get_global_var('func_4707')
func_4710_call = mutated_mod.get_global_var('func_4710')
const_7326 = relay.const([[6,-7,-7,-10,-6,4,4,-4,1,-4,-4,-6,-10,-3,-9,-2,-7,7,1,-1,-6,3,-4,-9,-9,-9,-5,7,6,-2,5,1,5,7,5,-3,5,-3,4,-8,-2,5,4,5,-4,-6,-10,-2,-6,9,7,4,-7,-2,6,-4,-7,-10,-3,-2,1,-5,-8,4,-5,5,4,-5,6,-1,-7,5,-6,-8,9,5,9,-8,6,-1,6,3,7,10,7,-8,-8,10,-7,4,-10,5,-8,8,-9,-7,7,3,-9,-7,-6,-1,-7,8,-9,1,1,1,-3,5,10,-4,-1,-10,10,5,4,10,-6,7,-3,7,6,-5,-8,10,-2,4,-1,-2,-4,7,-2,1,-7,5,9,-6,-1,6,1,7,10,7,-8,4,-7,-1,-10,-8,3,7,-5,-8,3,-6,-2,8,-4,5,5,3,-2,4,7,9,5,-1,-8,-9,-5,-5,-7,10,1,5,-7,-9,-5,1,5,3,5,-2,-4,-3,-7,-7,5,-8,-5,2,3,10,-4,-1,8,-1,-7,5,-6,-2,9,5,-7,8,-8,-5,-2,9,4,7,4,-7,10,4,-10,-9,6,-3,-9,-6,-1,-7,5,-1,6,3,5,-4,-3,3,5,-4,-5,5,-8,-10,3,4,-3,-9,2,-10,-3,5,3,9,9,-10,-10,8,-7,9,-6,-7,7,-8,9,9,2,-8,-10,-2,2,-3,6,-2,-2,2,3,8,5,-2,-6,6,3,-3,-3,-1,-7,-7,8,6,10,1,-9,-5,7,-9,-6,-10,-1,1,-10,-8,9,-9,-7,-8,-7,2,7,10,-5,-6,-6,-2,-1,-10,7,9,-5,2,7,1,-8,8,10,-7,7,-8,2,-1,-4,6,-10,7,5,-9,1,4,3,-5,10,-10,5,-1,7,-2,2,4,4,9,-3,2,10,-3,8,6,10,-4,-3,4,6,2,-5,-3,-8,-10,3,-4,8,4,5,-3,-5,10,3,-9,-1,8,-5,-6,-3,3,10,9,-5,3,4,-5,-4,-8,-10,-7,-5,-8,8,-5,-2,-9,6,-8,10,2,-9,4,3,-10,6,-3,-2,3,-7,-1,7,-9,7,-3,-3,2,2,-5,5,-8,-3,-3,-2,-7,3,7,-9,2,-6,-2,1,-10,9,8,3,8,-6,2,-7,8,8,-1,-2,2,9,-8,9,3,-3,3,-4,-1,2,-10,-4,-1,4,7,5,7,-3,-2,2,2,6,-9,-8,1,-6,1,1,-10,1,2,-9,8,3,6,-7,1,2,4,-2,2,-7,-6,2,-3,5,9,-6,8,10,5,10,1,-7,4,1,7,-6,6,1,10,-7,-2,7,2,-1,7,2,3,-4,-9,10,2,-1,5,10,-7,-6,9,8,3,8,-9,7,-2,-9,-5,-8,-7,7,-10,9,3,-8,-3,2,6,-7,10,6,-6,-2,-6,-9,-1,6,3,-1,-3,7,-7,-5,10,-9,7,-2,-2,3,9,10,-8,1,4,-8,-5,4,-5,-7,10,-5,1,9,6,-1,5,4,2,5,-9,2,9,6,-4,8,8,10,-5,-3,2,-5,-9,-10,-6,6,9,1,-3,-1,1,2,5,9,2,10,-7,-1,-5,7,10,-9,1,-7,9,3,7,7,9,1,-7,-5,7,-3,9,-6,-3,-7,6,-1,2,-5,1,-3,10,-4,-9,1,7,10,4,-4,-2,-3,7,-3,8,-1,2,1,-2,-6,6,-6,-3,-8,2,-6,-4,-1,3,-3,-4]], dtype = "int32")#candidate|7326|(1, 660)|const|int32
call_7325 = relay.TupleGetItem(func_4707_call(relay.reshape(const_7326.astype('int32'), [660,])), 3)
call_7327 = relay.TupleGetItem(func_4710_call(relay.reshape(const_7326.astype('int32'), [660,])), 3)
output = relay.Tuple([call_7306,var_7307,call_7313,const_7314,const_7315,var_7316,uop_7320,call_7325,const_7326,])
output2 = relay.Tuple([call_7308,var_7307,call_7317,const_7314,const_7315,var_7316,uop_7320,call_7327,const_7326,])
func_7329 = relay.Function([var_7295,var_7307,var_7316,], output)
mod['func_7329'] = func_7329
mod = relay.transform.InferType()(mod)
mutated_mod['func_7329'] = func_7329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7329_call = mutated_mod.get_global_var('func_7329')
var_7331 = relay.var("var_7331", dtype = "float32", shape = (4, 1, 14))#candidate|7331|(4, 1, 14)|var|float32
var_7332 = relay.var("var_7332", dtype = "float32", shape = (390,))#candidate|7332|(390,)|var|float32
var_7333 = relay.var("var_7333", dtype = "float32", shape = (7, 5))#candidate|7333|(7, 5)|var|float32
call_7330 = func_7329_call(var_7331,var_7332,var_7333,)
output = call_7330
func_7334 = relay.Function([var_7331,var_7332,var_7333,], output)
mutated_mod['func_7334'] = func_7334
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7398 = relay.var("var_7398", dtype = "float32", shape = (10, 9, 9))#candidate|7398|(10, 9, 9)|var|float32
uop_7399 = relay.exp(var_7398.astype('float32')) # shape=(10, 9, 9)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_7408 = relay.TupleGetItem(func_5036_call(), 0)
call_7409 = relay.TupleGetItem(func_5037_call(), 0)
output = relay.Tuple([uop_7399,call_7408,])
output2 = relay.Tuple([uop_7399,call_7409,])
func_7427 = relay.Function([var_7398,], output)
mod['func_7427'] = func_7427
mod = relay.transform.InferType()(mod)
mutated_mod['func_7427'] = func_7427
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7428 = relay.var("var_7428", dtype = "float32", shape = (10, 9, 9))#candidate|7428|(10, 9, 9)|var|float32
func_7427_call = mutated_mod.get_global_var('func_7427')
call_7429 = func_7427_call(var_7428)
output = call_7429
func_7430 = relay.Function([var_7428], output)
mutated_mod['func_7430'] = func_7430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_7473 = relay.TupleGetItem(func_5333_call(), 0)
call_7474 = relay.TupleGetItem(func_5334_call(), 0)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_7489 = relay.TupleGetItem(func_5036_call(), 0)
call_7490 = relay.TupleGetItem(func_5037_call(), 0)
func_5580_call = mod.get_global_var('func_5580')
func_5581_call = mutated_mod.get_global_var('func_5581')
call_7492 = func_5580_call()
call_7493 = func_5580_call()
output = relay.Tuple([call_7473,call_7489,call_7492,])
output2 = relay.Tuple([call_7474,call_7490,call_7493,])
func_7506 = relay.Function([], output)
mod['func_7506'] = func_7506
mod = relay.transform.InferType()(mod)
output = func_7506()
func_7507 = relay.Function([], output)
mutated_mod['func_7507'] = func_7507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5580_call = mod.get_global_var('func_5580')
func_5581_call = mutated_mod.get_global_var('func_5581')
call_7511 = func_5580_call()
call_7512 = func_5580_call()
func_5580_call = mod.get_global_var('func_5580')
func_5581_call = mutated_mod.get_global_var('func_5581')
call_7513 = func_5580_call()
call_7514 = func_5580_call()
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_7517 = relay.TupleGetItem(func_5303_call(), 0)
call_7518 = relay.TupleGetItem(func_5305_call(), 0)
output = relay.Tuple([call_7511,call_7513,call_7517,])
output2 = relay.Tuple([call_7512,call_7514,call_7518,])
func_7521 = relay.Function([], output)
mod['func_7521'] = func_7521
mod = relay.transform.InferType()(mod)
output = func_7521()
func_7522 = relay.Function([], output)
mutated_mod['func_7522'] = func_7522
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7648 = relay.var("var_7648", dtype = "float64", shape = ())#candidate|7648|()|var|float64
var_7649 = relay.var("var_7649", dtype = "float64", shape = (9, 15, 6))#candidate|7649|(9, 15, 6)|var|float64
bop_7650 = relay.subtract(var_7648.astype('float64'), var_7649.astype('float64')) # shape=(9, 15, 6)
output = relay.Tuple([bop_7650,])
output2 = relay.Tuple([bop_7650,])
func_7658 = relay.Function([var_7648,var_7649,], output)
mod['func_7658'] = func_7658
mod = relay.transform.InferType()(mod)
var_7659 = relay.var("var_7659", dtype = "float64", shape = ())#candidate|7659|()|var|float64
var_7660 = relay.var("var_7660", dtype = "float64", shape = (9, 15, 6))#candidate|7660|(9, 15, 6)|var|float64
output = func_7658(var_7659,var_7660,)
func_7661 = relay.Function([var_7659,var_7660,], output)
mutated_mod['func_7661'] = func_7661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_7709 = relay.TupleGetItem(func_7506_call(), 1)
call_7710 = relay.TupleGetItem(func_7507_call(), 1)
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
const_7718 = relay.const([-8.054917,6.079328,-5.339972,6.099535,3.241836,-5.724159,-3.171274,-0.418379,4.153594,-3.844981,7.142813,-8.049743,2.044165,-5.472828,-9.430950,7.637364,4.239707,-8.852739,-3.837025,-5.474110,6.572982,3.473147,1.734179,-2.750523,1.032414,6.869801,-6.111910,-7.095086,-1.614935,9.715910,-9.876177,2.825842,5.084706,-4.481539,8.230836,4.225937,6.460067,-4.965164,0.546269,6.358623,0.656135,1.796136,-0.814762,6.659262,-8.499939,1.068960,-8.841053,-2.279823,7.634511,1.275226,3.015358,7.871804,7.964599,7.421289,-0.906660,3.125073,3.271310,-4.955832,3.882584,-7.929663,-5.456902,-2.154343,-4.607847,-2.077662,6.455412,-0.056059,-8.773159,4.557510,-5.995559,-8.772676,8.231646,-7.811518,4.684984,-1.182967,3.264870,-3.006636,4.780809,-9.158685,-9.916437,7.199178,-0.306491,-3.681651,0.318409,-9.189247,2.550923,4.008792,-4.094079,0.179362,-3.208667,-2.382278,6.930396,1.954544,-9.386069,-4.965815,-5.941269,-6.776126,-4.837782,2.884465,8.927739,7.328952,6.699141,4.726711,-8.802691,1.147604,4.387479,-1.270764,-5.773638,2.975895,5.101293,1.142060,5.384377,-4.899602,2.016710,2.581388,5.523900,1.420387,2.988332,0.531784,9.331302,-3.643758,-9.901491,5.076198,-5.515403,4.187825,7.765838,6.456571,5.763167,-1.648134,-4.793938,8.965857,-5.929255,-5.982862,2.798035,3.002144,-4.252709,8.336901,8.948118,2.121925,9.832441,0.361301,-6.548134,4.893313,0.557558,-6.808386,-6.270431,0.057646,-3.797008,-3.255472,1.897100,-6.038934,-0.609042,5.416943,9.179072,8.689676,2.800153,7.104826,-1.104365,3.392948,-5.126773,7.323739,7.045363,5.933508,-1.207334,-4.636193,9.351265,3.057147,-9.536162,1.377156,8.571779,3.365948,-4.517694,-6.906793,3.610157,-9.023902,8.217082,-7.434055,-2.382431,-9.888301,-1.528744,0.357905,-5.937890,6.972723,3.138428,-3.684627,0.704651,6.890316,-9.484021,-8.168278,-2.463317,3.337795,-0.405771,-4.867742,0.148720,2.409940,7.546233,0.998837,9.737127,0.882478,-1.138481,-6.373907,9.796986,3.192503,1.319228,5.150238,-5.028739,-6.088325,1.983619,4.850467,3.923899,-6.233311,0.210349,-1.771099,-2.185666,8.346628,7.955218,-9.569895,-6.548881,-7.062274,-1.555291,1.604750,-4.045543,1.005112,-4.186908,-5.294879,-3.343987,9.544821,3.727237,-9.808477,2.006519,-8.364641,3.982479,2.790666,-7.803945,-1.312860,5.173154,3.046991,6.172688,6.709625,4.129609,4.271650,-9.400409,-5.262623,0.937357,4.676635,-3.291822,0.460382,2.504976,1.026561,0.935859,-7.300317,4.684720,-3.126741,-1.561550,2.580169,-9.006375,8.334799,8.146277,-4.515375,4.640578,0.407578,0.977180,5.081893,2.866809,-6.188715,-1.240344,4.112242,-3.135116,-8.878463,-4.003108,-7.504368,7.555989,4.377829,1.829960,6.906616,-7.337445,6.029481,1.238625,-5.945636,0.851745,6.114144,4.558723,-3.195294,0.876896,-3.969046,-1.550269,-6.197153,5.323775,-5.974721,8.964920,8.059722,-2.015144,8.138313,4.390175,-0.578147,-5.016502,1.670768,-2.987838,8.176239,-3.262941,6.784460,-3.675639,-8.509105,-5.779493,9.282195,-9.949070,9.800527,0.514463,5.582935,-7.814357,1.105275,2.302133,-5.972093,-7.115699,4.280959,9.622314,5.813738,-5.702016,3.031908,-1.124576,-5.042785,2.392498,4.605084,-8.709528,-1.516967,-6.939608,6.963119,-9.775709,-3.213092,6.425888,1.303815,-5.448711,0.249985,1.697990,2.560984,4.443898,-0.267828,3.512932,4.572435,-7.227654,-6.533438,4.102866,8.997424,6.935998,2.289325,4.138692,-7.294067,6.119869,6.021896,-0.665480,7.655257,-6.875889,6.200948,3.141371,-7.066292,-2.155657,9.192407,-6.926569,1.649992,-3.652390,6.678042,2.258288,3.454708,1.187318,0.618890,-4.885948,6.407023,9.552749,-4.453061,5.289425,-5.364687,-7.730707,2.357400,-9.764585,-1.809812,0.099087,7.603327,5.757636,-6.754311,8.006364,3.119576,-2.910484,-3.690224,2.324029,-4.383314,2.154535,-8.120285,-0.969179,6.532270,-4.966315,3.523860,2.984972,-9.374631,-1.926976,0.823840,2.390847,8.505933,6.369990,2.729291,-3.797715,7.804516,-7.780001,0.940248,7.688689,-6.383317,4.464092,-9.430465,-0.474368,8.730030,1.205453,-4.382390,6.679494,-0.275160,2.660766,8.770658,6.916710,-9.900927,-3.090122,8.332451,-7.667274,4.920984,7.214986,-2.929990,9.949717,-5.322801,-6.537484,4.901041,-6.935256,-4.082544,5.677975,-3.117818,-2.657591,-7.809261,-7.834291,-4.811603,2.012759,-0.520165,6.417167,-9.473726,1.436788,2.417809,9.282020,4.270831,-2.953286,-0.508640,-1.449096,3.814841,0.495103,4.341574,0.664699,-2.952261,-4.665081,0.856194,4.217621,-1.187301,2.634354,-6.431716,-3.948161,-8.730836,4.732600,-1.651698,8.185574,-8.012842,3.108566,6.337679,3.759461,-9.102540,-8.058058,-1.091706,8.261342,-6.699144,-9.418183,-2.140642,3.797928,-4.951457,3.085446,-4.930901,-2.600063,9.693105,-0.860687,-4.169217,-7.158559,7.173368,-9.548576,-4.441829,-2.646930,-2.181092,5.826216,4.844031,-4.907845,3.445526,-3.773706,-9.045972,-9.214317,5.944641,-9.678696,-9.226511,-9.700304,-7.951736,0.470854,-3.485424,4.121963,7.892420,7.439291,7.475154,-5.549954,3.184720,-9.016883,4.480245,6.026938,-0.364066,-6.194252,-0.198780,-2.214117,5.478846,1.143438,-5.461168,9.177959,7.349485,-8.394135,-7.816169,8.128302,-7.538058,8.182535,-4.501485,-2.254539,3.859734,-4.766671,2.082411,-4.855301,-6.234889,-7.202777,-0.940760,-5.393289,8.342556,1.500730,9.268379,4.058901,-5.672994,0.202351,-7.471854,0.458193,-0.530071,9.007608,6.647290,1.736890,-8.904830,-9.695122,2.004526,-9.553055,9.243171,-4.555645,4.606163,-8.456147,-8.898088,-8.250892,0.360753,-3.251896,2.340115,4.371018,0.761829,9.573545,5.057692,2.104188,-8.524689,8.915028,2.990849,1.574292,3.681495,-9.012798,0.155072,-2.276719,1.583556,2.069461,1.278091,3.680385,1.262178,-2.111453,-8.318699,9.689052,7.518823,-9.495741,-4.311175,9.316033,-8.321126,2.361273,4.001374,-0.821233,0.720632,2.245822,1.002353,7.367116,7.794551,2.232581,3.666761,7.222630,4.544950,1.024629,0.348112,7.451157,1.326255,9.418733,3.610900,8.607111,5.045033,3.746671,4.594340,1.945678,-8.344882,-2.957923,0.567862,-8.758038,9.733683,-3.069707,3.961114,-8.205333,7.052921,9.441781,-9.950788,7.234893,2.157375,-5.916873,6.933852,-6.962379,-9.535372,-1.174567,-1.935203,-5.193282,-9.162394,-9.633019,-0.594997,-2.372427,-1.869068,-4.842805,-9.712542,7.747148,-8.409089,-0.481624,4.933218,7.647463,6.197712,-1.543563,3.296673,-7.136481,1.879104,1.292799,3.220573,4.354234,7.326379,-7.774519,7.316148,8.200167,6.509592,-4.009873,-5.611144,-8.453550,5.038893,9.769102,5.565926,-0.158118,-0.538731,1.148882,-5.387782,-1.812807,-6.788721,7.915548,-9.444631,-8.774723,7.184563,-9.628839,-2.646896,5.223194,5.444804,-3.396519,-3.566842,-4.148334,-2.219495,3.343966,-5.941822,-6.149800,-6.626085,9.693968,0.399404,2.251769,-2.237948,-0.541558,-5.817350,-4.491367,9.380991,8.080871,2.636490,-6.740297,4.036835,-0.484582,5.908082,-9.635302,8.004800,-2.272261,6.100561,8.352670,-5.681680,8.238052,1.265715,-1.606633,-5.993743,4.228837,5.658550,-7.406074,8.528530,0.201277,3.373508,-5.067122,5.048111,0.924768,-2.720714,-3.838484,6.337987,-0.374862,5.935608,6.559478,-4.493043,3.771481,-7.526000,-9.296834,3.820658,4.117918,8.762903,3.925607,-4.587800,-4.073290,8.830765,3.850829,-2.173083,2.908577,0.774984,2.749145,2.430746,6.949291,-0.623947,9.876680,8.812754,1.303941,1.709007,8.824921,6.667388,-7.695371,-5.384570,1.255553,5.197740,-5.028206,8.027370,-8.019098,8.527469,5.391177,0.499800,4.679889,3.240283,-7.990428,7.824652,-2.146894,7.016775,9.794427,2.017656,-3.137182,9.654237,4.248448,-4.765484,-2.610916,2.776781,-0.870402,-1.650939,-4.140549,-5.345863,-3.269108,-1.485543,-1.416739,-2.053150,-6.068699,2.330149,-5.206822,8.535098,3.820528,-6.943508,3.913667,0.184144,-4.347567,7.628104,2.204332,2.073442,6.791969,1.712954,3.205877,6.360077,6.259987,-3.501772,-6.130220,4.875141,-9.213653,8.624386,1.951610,4.672194,-3.782599,-8.210849,-8.062014,-3.941518,-6.377905,4.449674,0.324302,0.384475,4.547298,-6.541040,3.555160,-7.332674,0.923514,-4.659585,-2.363674,3.723479,-9.762691,5.800937,3.995415,9.563636,8.750046,-6.494232,2.219798,4.681938,8.172390,-4.524852,7.475684,-4.431611,-2.826054,8.336481,-2.968867,-7.530354,8.641806,5.047636,1.812529,-7.594806,-2.244623,4.153547,-0.985009,-5.400216,-9.207540,-2.050672,7.063406,8.991784,7.038828,1.641822,2.843377,3.539080,1.961932,3.855488,3.758518,3.230989,-3.620020,1.182726,2.134810,9.424873,7.028580,7.986793,-4.842409,-7.587317,0.978974,-9.433125,4.441342,9.531483,-9.265662,7.708323,-9.528209,9.196478,1.790271,3.435158,9.232732,1.773310,6.034772,6.711544,8.082247,9.251480,4.110106,0.135669,6.224077,8.199384,1.407608,1.181233,8.347290,2.417495,-7.075960,9.970389,0.801444,-6.852648,5.161246,-7.210107,1.686772,-8.176328,9.626273,-7.171311,-5.120613,5.986249,-3.219205,-7.080722,9.894325,5.496827,-0.018424,7.540145,0.549344,-1.933094,-8.722980,5.938157,7.704888,-3.282048,3.493942,2.039011,1.205327,3.963410,-8.269102,0.998733,8.682251,9.651741,-7.220454,8.492055,-6.457635,-2.981732,8.904551,-4.484514,8.213973,5.274846,7.992538,4.083978,6.016304,5.375279,-3.001099,-3.787256,8.123271,9.735171,-7.311198,2.707923,2.216004,0.369943,8.961534,0.653657,2.685477,2.892523,9.785074,2.624008,6.764895,-4.516696,7.240267,-7.217375,-9.528370,-2.426858,-4.683535,7.906555,-6.902143,-1.494701,3.760821,-2.365363,3.631819,0.072395,-4.490983,3.226719,5.389787,1.887162,-5.874185,5.819489,-3.452135,-5.972580,1.062656,-6.940997,-6.517457,2.314408,-8.519754,-0.630796,9.038956,-8.350890,-4.737488,-5.594104,-6.343830,8.195096,8.024306,3.877209,-3.918491,-2.556933,-4.429214,7.560985,-0.098454,-0.272330,2.471141,-2.159465,-1.954766,-5.316840,-4.748494,6.298345,7.683803,-7.337546,6.393705,-2.736894,6.769613,-0.572820,6.638659,-1.836288,-7.238766,-4.195842,-0.386524,3.164047,8.323800,2.946092,-1.100326,-2.927945,2.133161,-3.897634,2.213955,6.174910,3.873114,-3.979192,4.078881,-5.691902,0.577197,8.367308,5.786141,-3.982563,8.051257,7.167192,-8.717216,6.207062,-4.375803,4.801315,-0.383928,-2.437873,-4.082668,-9.490239,9.014315,3.242820,3.869414,-4.333537,9.395662,1.940961,4.636990,-5.194645,0.610662,5.194884,1.065434,6.092148,2.809922,-5.593549,-7.450809,-2.783388,9.924441,-9.681833,-0.495463,-3.837960,9.865543,-0.591698,-6.193269,4.385722,-2.264410,1.093910,3.382330,8.132337,-7.449805,-6.881692,-0.758209,-7.489372,-2.301736,-4.789932,-9.975580,1.914683,9.685638,-5.788355,-8.703797,5.982795,-7.405050,0.583233,7.983030,6.618386,-9.138104,-5.446097,-6.739801,-9.352160,3.499203,9.873886,2.052299,4.062241,9.317486,-4.758055,2.723294,-6.034537,-4.875725,8.744277,0.039688,8.940564,-6.953588,-2.838163,8.907232,-9.790884,-3.752971,-4.386515,-8.608898,-0.548129,5.194760,6.274360,-7.419874,-1.113391,3.406652,-0.684663,-8.910954,-1.567102,7.482682,8.493803,-6.225676,9.432315,-0.381947,-4.486622,9.769957,-6.132122,-8.315061,-1.557016,0.270606,2.390328,-2.475031,2.294693,-8.604292,-9.837785,1.106456,-2.969508,4.239878,-4.793700,4.923778,-1.629959,7.036422,9.095364,-8.792491,-2.367000,-1.864766,2.277125,9.155125,-0.383166,-0.402701,2.517107,-6.110719,4.779317,8.843656,9.353533,0.299262,8.003780,-4.697268,-8.090813,-6.174336,5.565641,-7.470715,-1.241984,2.041540,7.906973,4.207682,8.205764,-1.210227,3.912213,-8.452261,-4.482001,-2.419909,-3.382014,-9.397090,9.165824,2.004559,-3.500577,0.577289,4.917516,7.315140,3.415292,5.541522,-3.422534,1.051198,0.067894,3.691255,0.020901,-1.504359,-5.843830,-2.474394,2.334879,-4.361605,-5.368088,-8.774101,3.064200,-7.241140,-6.787936,6.311847,-4.316088,-8.776678,2.854234,0.837418,6.308957,-5.108342,1.595591,-4.886777,5.028841,-3.677331,-8.669446,6.612060,-6.436378,-2.298498,-4.717884,4.894045,0.732340,-9.405522,6.967578,8.115744,0.872260,1.552593,7.488949,-2.744383,-2.272952,-8.198825,0.791554,-8.732034,3.217006,3.086426,9.179125,-8.265418,-2.272303,8.308485,4.802524,0.038324,-0.485671,0.234624,-2.571915,-8.286899,-7.474992,1.422563,3.605533,9.670370,9.714415,-8.440437,8.016345,2.482260,4.794968,-0.836872,8.039921,-7.799388,-5.345818,8.705787,6.106071,4.908760,-1.273878,1.400045,5.122515,5.463587,5.075774,2.794843,-4.940873,5.603378,2.636740,-1.754450,5.841814,-1.050651,-7.594419,-6.080561,-6.552504,6.010897,-2.612997,-8.194458,0.045378,-7.862250,3.072321,-2.280233,-6.230279,9.449815,5.243603,2.805094,-4.108523,-2.559331,5.311349,-4.843442,-8.887755,4.547741,4.904966,-9.389380,9.704439,6.356208,-0.262631,-4.099678,9.240053,-2.770484,-8.960855,1.502819,-0.237109,0.661207,-1.935523,3.150663,-4.387250,-2.574343,-9.302407,-0.024943,9.527189,-4.295886,9.331073,8.063779,-2.910955,4.291602,3.735035,-6.372702,-2.444230,6.740857,8.802475,-7.628673,4.225256,0.730393,5.002925,8.581128,-0.398196,1.971012,1.967568,-8.714288,-8.869807,-0.392005,1.294352,4.093648,-7.544969,-2.753869,4.388809,0.392228,8.971938,-4.910281,5.940722,-5.527104,7.350851,1.301721,-0.473443,0.977038,-9.843449,-5.869550,-2.866380,9.384963,-6.676082,-9.730163,-1.179906,6.013541,9.130063,0.078721,2.363198,-3.152554,2.598969,8.205882,6.351438,-1.939530,-8.848793,7.803384,5.492469,-6.138974,3.145424,5.901734,-0.659084,6.300807,2.427924,-8.162958,-6.899358,2.971304,4.441572,7.795785,2.298065,-7.800432,-8.527548,-5.094656,-0.881545,-7.617863,-6.407295,-2.203347,-0.512301,-2.346544,-5.089732,-6.527970,5.630955,-4.129547,6.205557,5.873186,3.190799,-7.874560,-2.382347,8.455244,0.439310,-8.528189,-3.826435,2.630622,-1.069759,-5.537786,-9.944641,-7.509488,-3.402817,-1.552372,-0.189231,9.088324,3.027419,-9.322285,-2.442411,3.131086,2.940755,8.409668,-7.801175,-0.122278,-7.933008,2.675195,1.053844,-2.575415,-9.751540,1.033015,4.633863,-3.684752,9.506595,-3.021799,9.944395,3.557890,4.586326,-8.444412,9.813735,-6.998824,2.274666,2.401556,3.180963,-1.934186,-6.504204,9.799787,-6.521705,5.892260,-2.397543,-3.969206,7.982239,-7.074239,-3.387363,-5.667336,4.988270,-0.152922,-7.119073,9.133581,8.619123,6.851747,-4.134776,7.181499,-2.854737,-4.829788,-9.823367,-8.448025,-0.637524,-1.204899,0.685718,7.013773,-6.620040,4.174085,1.143302,-9.254104,7.292542,-8.866259,-3.624203,-2.024040,-9.238830,1.411081,7.721993,-2.415898,-1.374709,9.648707,9.867053,-5.392201,-2.619523,-2.353722,2.008922,-1.703798,-6.415676,-8.099658,3.962314,-9.541817,9.954024,-0.133394,4.744367,-1.470419,-4.982464,-5.143789,-6.210225,1.703624,-4.119869,-2.577970,-6.068264,-2.330862,-3.936306,-8.904660,-9.915567,7.853733,-9.019985,-8.130269,6.557168,-5.534447,-3.797533,6.897342,0.239744,4.088736,4.600761,0.698155,5.772863,-6.370409,-2.652536,0.141650,4.343937,-5.169927,-8.021336,-9.949764,-5.814798,6.164400,2.253209,2.044089,8.897835,-0.966371,2.275785,9.717431,-3.568845,-4.177761,-0.683183,9.754411,-7.428336,7.228309,-0.732772,-0.053717,-5.325253,-4.701023,5.683946,2.944980,-2.618239,3.685188,5.687074,-7.183392,-5.988258,5.750383,-9.962251,2.157686,-2.638309,-9.512580,-0.229062,8.025885,-5.601687,-4.114291,-9.112097,9.067729,7.061072,-9.610527,2.129024,-1.432963,9.441550,-4.389141,-7.227656,-4.107557,-0.693548,-8.596498,-2.565835,-7.351381,7.682598,-9.461566,-9.482492,-3.672940,-3.656393,-0.468741,-5.391441,1.140092,-6.213757,4.112525,8.268524,-9.875849,-4.066361,-5.571047,-4.157681,-1.247694,7.982930,4.821100,-4.557197,-3.347740,-6.647301,-8.482628,4.209513,-1.805367,6.862860,4.436061,-6.994319,-0.238071,-0.736282,8.786985,5.723249,-3.893126,-6.007820,-2.652147,8.110204,1.112352,-9.807670,-1.526853,5.391829,6.151827,2.473839,-5.871115,-4.520640,-9.635472,2.312186,-9.689087,4.604866,-1.035199,-7.737512,-9.892233,1.634688,-6.035359,7.379812,7.701446,7.028196,1.681898,2.449992,-4.029811,0.334609,-6.856679,-8.208427,8.847468,8.197713,9.361090,0.186069,-0.221267,2.166352,-4.869061,9.623475,-4.289231,-0.593374,6.104209,7.095767,-9.673926,7.996817,2.948684,1.439898,9.441471,-5.871192,-0.025205,5.205367,-8.447864,4.429034,6.701152,6.069160,-8.043205,-4.409627,8.269401,1.933748,-4.666118,8.601967,3.944429,-5.048313,7.094721,4.624852,-1.653412,-3.136854,-9.423134,6.571264,1.372014,7.494786,9.981727,5.827043,2.347186,-4.417046,1.415394,5.045322,-8.677684,-5.090808,6.411502,9.246014,-5.277054,-2.447656,-3.363544,-2.449055,-3.501823,2.441234,8.410776,6.542894,4.546126,-1.864611,1.955657,9.348193,-3.422746,5.747632,-0.095383,1.230233,7.864453,0.973399,-4.040364,8.402002,4.731854,-8.829123,4.743216,5.810869,0.963677,-7.098906,1.730697,-7.299363,3.088096,8.576243,-1.629473,-5.529654,3.644691,6.931169,3.446535,-8.032846,8.893018,-5.460554,-3.430994,-4.535139,5.941040,-5.186946,-8.653315,-3.212471,9.839713,9.229842,1.964214,7.106328,8.836025,-9.788982,4.094043,7.562747,7.155414,6.073415,2.175373,2.217860,-5.316552,-8.432323,-3.648257,-4.497102,-3.599403,4.687886,2.898171,-6.833562,-1.463257,-3.911219,-3.120995,-5.570666,5.219756,3.601491,6.699710,8.824715,9.399667,2.404351,0.640321,9.462581,1.254634,2.379731,2.245320,-8.998490,-2.448012,6.381414,-8.036390,-2.712954,7.769971,9.086461,-2.487887,1.522071,-8.378739,4.249399,-5.937718,8.674376,6.674995,3.275920,4.059578,-1.596879,-8.657912,-6.703615,-1.468420,-1.361832,-1.266532,-9.412789,-3.792995,-6.320432,-5.791576,-1.407172,-1.221012,7.690779,-8.383443,-5.115074,-8.457427,7.414859,-5.087024,5.871604,-3.052196,2.479167,7.916783,5.132439,7.334714,-8.638996,8.535278,-2.621707,6.196646,-7.590791,-9.552025,5.329407,0.348488,6.164043,-4.357147,-2.842092,-5.119090,9.078884,-5.545017,-3.883113,8.241588,3.983817,6.537146,-7.063772,8.707166,4.292494,-3.241593,-6.212047,4.920437,1.067799,8.871949,6.514252,2.841123,0.240503,7.231676,6.085097,3.665330,-6.562702,3.661125,1.053903,4.045295,-8.430577,1.168506,0.114198,5.094132,-6.502935,9.465433,-1.588611,-8.251975,-3.422997,0.193914,-2.867768,-9.275291,-4.701645,-5.606708,6.937852,-4.922572,7.501179,-8.732438,-6.782965,3.861449,-5.372339,-3.336887,-7.579150,2.741410,7.155022,-4.933296,6.478525,-5.385879,-5.980765,3.020736,-9.105310,-7.262784,9.994677,-7.964869,-0.804284,-8.588695,-6.237806,4.950343,7.086276,2.369333,-6.480536,3.412530,0.126699,2.945653,-3.515473,4.407328,-4.442631,-8.980873,-2.280113,0.771245,-6.306121,-8.098419,6.059470,1.016341,-7.393736,1.794660,8.370004,-5.880407,-1.497243,-5.178621,-5.275303,2.767698,8.803783,-9.032170,-8.343283,-1.854502,9.654869,-2.360069,2.846513,6.817230,-6.735887,-5.984794,0.195010,-2.885503,-3.221321,-0.684440,-5.558487,8.727928,1.591927,-5.077238,3.668929,6.192294,6.368997,0.111857,4.048399,-8.371263,0.868456,9.361837,4.415457,-1.100113,8.230714,-1.029033,-7.601759,3.956516,7.016561,-4.730767,3.142252,6.099120,8.413284,9.010086,7.891820,-1.955382,-9.411658,-3.687140,-8.253502,3.384937,7.230533,5.105827,1.849655,-2.520117,-2.272735,3.407547,-4.778452,-3.555415,-9.309155,-3.867584,1.374376,-3.432547,1.623820,1.562745,-4.576544,1.979439,-1.155609,0.669981,7.223715,-5.024761,-6.617181,3.299010,-9.678479,-5.366682,3.492893,4.091151,-4.100301,-5.090812,-3.231444,5.584913,-1.598186,-3.922845,6.800321,-1.553643,9.640738,4.592633,8.546984,-4.486645,-7.783869,-9.024826,-6.670098,6.180389,2.746165,-5.882947,1.243705,-5.572635,-0.167699,1.030254,9.427113,-9.073571,-6.062755,-7.096772,6.861347,-0.161597,-3.045122,6.231215,-3.308839,1.869858,7.390559,7.481790,7.722164,-0.900274,-6.825622,1.733174,-9.488613,6.187229,9.881891,-1.725253,-8.767795,4.290014,7.406729,1.375310,0.025354,0.350249,-2.223161,8.135388,1.381773,2.526333,3.499615,8.680331,6.700117,3.072188,-3.813241,0.621328,-2.872169,0.160062,3.384202,2.772911,8.319596,2.441819,4.908540,2.620246,3.560754,-1.410285,-3.831161,-5.162631,-8.704449,-2.924639,1.735860,-5.243461,-4.316954,8.010489,-3.594674,-6.832048,5.076753,-6.915256,4.842635,0.356293,-8.309611,9.808417,1.158924,-2.487865,1.791928,9.198321,-8.565119,-9.897124,8.619444,8.208340,-2.548668,-0.875389,1.428383,-1.281478,-3.528996,3.173529,-4.274785,8.482293,-4.026131,9.916968,3.298346,-8.131733,-8.859455,-4.106016,-9.636552,-7.591287,-2.656449,4.123556,0.457818,-7.091964,5.218304,-7.846456,-8.431260,-8.380384,-3.497109,9.572961,-1.896819,1.080892,-5.385315,-2.026055,1.828296,-6.124928,3.798857,-0.389398,2.720551,1.611421,-6.258920,-7.618975,9.624871,-1.923079,0.857955,8.253933,0.072037,-0.502134,0.901837,6.871269,9.995514,-5.804504,4.190906,4.777599,8.408267,4.505564,4.660958,-3.904574,-9.479980,-5.246078,-4.338854,3.907929,-3.222309,-0.802533,9.583156,1.617691,0.701153,4.797126,-2.492406,2.649439,0.040924,7.718811,5.029033,-3.668174,-1.897897,0.511499,-5.554701,2.145381,-4.545661,-1.182959,1.573266,5.331888,6.526291,9.173597,9.513113,2.987041,4.107618,7.906552,3.662204,6.817203,-9.528176,-5.655775,8.261734,-8.817307,0.844160,4.806274,-9.417913,6.208588,-7.351494,2.492623,-6.536334,-2.011636,8.945158,-8.672516,0.251030,9.579004,-6.943584,6.609728,3.528704,4.370367,-6.155399,1.534439,7.030888,0.024256,8.922976,-9.080235,0.414442,5.224825,-5.138398,3.737293,4.245855,-2.446277,8.667372,-4.179752,3.340335,3.751351,-5.198590,-7.007496,-2.964440,8.969504,-7.971111,4.547103,6.361444,-9.715034,-5.377393,0.544713,-7.480309,5.764581,7.128981,-2.033049,8.083281,7.369324,-9.272987,-1.037201,3.527492,-3.556093,7.561518,3.117731,0.315504,-3.186522,-8.765301,6.142759,9.712815,-6.284690,-1.555075,5.350278,-2.404017,-1.436774,-3.573169,4.084395,-3.157744,1.231004,0.917113,-9.538542,5.763923,-2.694963,0.375859,-1.700438,-3.270978,4.711057,-8.894242,1.733832,9.695333,1.465542,-5.054742,1.417771,0.212634,-9.200664,-9.962284,7.716893,7.620907,2.707305,7.010375,-0.840642,-9.395570,3.979684,-8.430725,8.323974,-1.975664,-4.038075,-0.194178,4.008635,-1.115744,-6.787488,3.867350,-2.311335,-5.002376,2.688001,-2.952776,0.717295,4.660864,5.798615,6.667609,-3.940962,6.332059,-4.316599,-4.001332,5.573009,6.979130,5.850490,1.084984,-7.341392,6.302400,-9.653076,1.517995,-4.566228,-8.095360,-2.246758,2.333111,2.831270,6.200549,-0.774494,2.541114,9.847808,3.961358,4.948029,-8.909983,-7.400038,6.583613,7.253511,2.622048,-3.333682,7.909934,9.042323,3.767786,-5.406653,6.225944,-5.109967,-4.144818,8.565146,2.745594,4.032498,-4.660758,1.952389,-0.939368,-4.640705,9.709929,8.770871,-9.497013,8.494415,2.470697,-2.458990,-7.161120,2.023189,-1.592140], dtype = "float32")#candidate|7718|(2288,)|const|float32
call_7717 = relay.TupleGetItem(func_2795_call(relay.reshape(const_7718.astype('float32'), [11, 13, 16])), 1)
call_7719 = relay.TupleGetItem(func_2798_call(relay.reshape(const_7718.astype('float32'), [11, 13, 16])), 1)
output = relay.Tuple([call_7709,call_7717,const_7718,])
output2 = relay.Tuple([call_7710,call_7719,const_7718,])
func_7728 = relay.Function([], output)
mod['func_7728'] = func_7728
mod = relay.transform.InferType()(mod)
mutated_mod['func_7728'] = func_7728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7728_call = mutated_mod.get_global_var('func_7728')
call_7729 = func_7728_call()
output = call_7729
func_7730 = relay.Function([], output)
mutated_mod['func_7730'] = func_7730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6580_call = mod.get_global_var('func_6580')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_7748 = relay.TupleGetItem(func_6580_call(), 0)
call_7749 = relay.TupleGetItem(func_6581_call(), 0)
func_3988_call = mod.get_global_var('func_3988')
func_3990_call = mutated_mod.get_global_var('func_3990')
const_7753 = relay.const([9.524402,4.273077,-5.844604,4.216240,-6.227203,3.400474,-4.391711,-4.566060,7.687713,-5.840597,1.673223,-1.755581,3.279046,-0.331929,-2.627455,0.296387,1.914977,-2.713868,-5.854325,2.980779,-9.195193,-7.056097,5.352279,-2.163595,2.329740,-2.545215,4.658999,-8.042603,-1.861228,0.125175,1.195142,8.277485,3.750589,-9.014436,4.669703,1.871478,-4.386757,-9.343928,-8.535290,-8.361663,-2.439324,5.159323,-2.272329,-4.636562,-3.665749,7.756488,-8.010317,-0.929939,-3.760345,-4.107394,6.098424,7.866732,1.483043,7.043196,-3.288516,8.237475,-9.818674,-0.685871,-5.380879,4.731195,-2.767757,8.054337,5.176218,2.553963,-3.894127,-0.035425,2.921049,-1.249887,0.431962,-6.649942,6.343453,-5.648186,-5.990265,-1.956475,-6.683157,-6.652636,-4.488658,7.346922,4.573193,-1.902736,-8.716729,8.249924,-3.586158,0.345791,3.740413,-8.782359,3.447378,-1.863982,5.231917,8.901140,8.716114,8.307899,1.059101,4.920635,5.052053,-9.168356,-9.976846,8.753817,9.049662,6.605120,-2.462525,-1.957245,-7.090948,-6.860268,0.468996,5.605779,4.285826,7.685902,-1.301481,4.755617,-8.108429,1.416786,-3.409558,3.387882,1.662415,-0.638124,-3.119543,-6.945027,-6.078340,1.952664,-4.630347,-6.621407,0.314228,-0.408318,-7.643768,7.740691,9.296843,-2.904006,4.116801,-4.041425,-9.229865,-7.390128,6.169866,8.658289,7.906938,4.170239,-9.973666,7.951274,7.279639,1.669499,-8.408837,-9.656431,5.013884,0.617443,0.458402,-0.439686,-5.354496,-8.506908,4.132342,1.384119,-7.384158,-0.773674,-0.658419,-4.549297,4.732235,-5.894465,-1.703826,2.462635,3.723269,-5.006469,-7.302858,-0.530073,-4.920622,-5.024150,-1.057677,-3.485329,8.004335,6.407940,2.949961,5.840500,5.951786,-1.656210,0.746095,-8.367572,-6.568423,2.765255,5.496159,1.075519,-8.616696,9.951821,-2.849792,-9.778443,-6.066221,6.091665,9.581143,-8.367043,-2.514523,3.226790,-8.104011,-3.096575,-1.295788,-4.391185,7.513691,9.322076,3.700061,6.534319,1.204290,4.240587,9.499997,4.274449,-0.944349,-0.403060,-1.704660,-6.146127,9.743128,3.894589,-6.585842,4.908814,9.510956,2.224166,4.328452,-3.453548,-7.209633,-4.747265,0.092848,2.553624,3.503909,-7.948200,7.381686,-5.793834,-6.458245,-6.524002,1.803969,-8.130446,1.858164,-9.492243,-6.751388,6.696487,-5.770157,2.696058,0.080598,1.968212,-8.413381,-0.078063,-2.188749,-3.198336,-4.404912,2.990251,-4.860733,-9.678614,-4.586792,-4.112150,-6.066980,6.766455,2.379415,-4.839994,6.413879,5.517052,1.766448,6.274574,-6.812665,-8.857948,5.131111,7.090054,-8.861556,0.014894,-8.974787,1.510316,9.240987,2.897007,8.832352,0.336347,-1.989993,-6.109117,-7.404543,4.245927,9.776270,2.099014,-3.558986,-4.288892,-9.498949,8.694856,4.376803,1.938508,4.033953,2.749735,-2.855381,-5.756665,5.687693,4.315468,-3.361998,8.917530,-3.247865,-1.615806,1.178148,6.269115,-9.413888,-6.787060,-7.280321,-8.756552,-1.556649,-8.752569,-7.432136,4.372179,-3.607975,8.313085,-8.412369,-8.518095,6.783376,6.125176,-7.791481,3.886140,9.950469,-6.123589,1.555335,9.606232,8.276024,6.286619,-4.788069,2.082580,0.007104,-9.752640,0.861798,-2.868590,4.127468,3.965589,0.752163,5.583726,-7.377784,-4.050110,-1.734729,-2.920260,0.756853,-9.353899,-1.496558,-7.403340,-0.681220,9.697374,-6.840846,1.119959,9.528064,8.570118,0.308892,6.843976,-6.252846,5.374736,-5.342518,-1.684102,4.583839,4.647638,8.656157,8.113492,-6.821136,4.927800,6.672252,3.280304,-1.863005,2.876876,3.427935,7.898628,-4.425300,-7.525231,-9.525020,-7.936885,1.313217,-7.833880,-9.760668,8.566791,-3.324150,8.641507,4.209177,9.405769,5.029751,3.650400,2.607430,-5.629586,7.765439,-7.759670,-1.072488,-7.288966,2.373974,-9.088075,-5.769051,-7.775914,-4.655529,-4.510350,-9.817430,4.325444,-7.662410,-9.640329,-3.802514,2.146165,-1.601370,7.059227,4.928173,-0.605647,-7.620448,-6.863923,-1.268084,-2.392185], dtype = "float32")#candidate|7753|(390,)|const|float32
call_7752 = relay.TupleGetItem(func_3988_call(relay.reshape(const_7753.astype('float32'), [390,])), 2)
call_7754 = relay.TupleGetItem(func_3990_call(relay.reshape(const_7753.astype('float32'), [390,])), 2)
output = relay.Tuple([call_7748,call_7752,const_7753,])
output2 = relay.Tuple([call_7749,call_7754,const_7753,])
func_7757 = relay.Function([], output)
mod['func_7757'] = func_7757
mod = relay.transform.InferType()(mod)
mutated_mod['func_7757'] = func_7757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7757_call = mutated_mod.get_global_var('func_7757')
call_7758 = func_7757_call()
output = call_7758
func_7759 = relay.Function([], output)
mutated_mod['func_7759'] = func_7759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4843_call = mod.get_global_var('func_4843')
func_4844_call = mutated_mod.get_global_var('func_4844')
call_7770 = func_4843_call()
call_7771 = func_4843_call()
output = call_7770
output2 = call_7771
func_7772 = relay.Function([], output)
mod['func_7772'] = func_7772
mod = relay.transform.InferType()(mod)
mutated_mod['func_7772'] = func_7772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7772_call = mutated_mod.get_global_var('func_7772')
call_7773 = func_7772_call()
output = call_7773
func_7774 = relay.Function([], output)
mutated_mod['func_7774'] = func_7774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7241_call = mod.get_global_var('func_7241')
func_7243_call = mutated_mod.get_global_var('func_7243')
call_7800 = func_7241_call()
call_7801 = func_7241_call()
output = relay.Tuple([call_7800,])
output2 = relay.Tuple([call_7801,])
func_7824 = relay.Function([], output)
mod['func_7824'] = func_7824
mod = relay.transform.InferType()(mod)
mutated_mod['func_7824'] = func_7824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7824_call = mutated_mod.get_global_var('func_7824')
call_7825 = func_7824_call()
output = call_7825
func_7826 = relay.Function([], output)
mutated_mod['func_7826'] = func_7826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_7884 = relay.TupleGetItem(func_4610_call(), 0)
call_7885 = relay.TupleGetItem(func_4611_call(), 0)
func_4087_call = mod.get_global_var('func_4087')
func_4090_call = mutated_mod.get_global_var('func_4090')
var_7903 = relay.var("var_7903", dtype = "float32", shape = (1, 192))#candidate|7903|(1, 192)|var|float32
call_7902 = relay.TupleGetItem(func_4087_call(relay.reshape(var_7903.astype('float32'), [2, 6, 16]), relay.reshape(var_7903.astype('float32'), [2, 6, 16]), ), 0)
call_7904 = relay.TupleGetItem(func_4090_call(relay.reshape(var_7903.astype('float32'), [2, 6, 16]), relay.reshape(var_7903.astype('float32'), [2, 6, 16]), ), 0)
const_7912 = relay.const([[3.273641,-4.507770,2.983532,7.252354,4.023303,0.919363,-3.380755,-6.039088,9.624913,-4.137511,-1.358965,4.627861,-1.819711,-4.586054,-7.890108,4.050488,-3.592807,-4.327692,-7.212741,7.796967,-0.428471,3.319302,9.203795,1.040615,2.525534,-9.009909,5.088023,-7.136052,8.237176,-6.968092,0.330076,4.874193,9.888819,9.464581,-0.393002,-8.024630,8.262117,9.054568,8.351049,2.650513,8.919430,-2.132427,-1.133684,-2.725125,7.217423,5.660267,0.454452,-3.704712,-8.020512,-7.351699,-0.545816,8.189562,-4.919982,-3.326213,-4.894182,-2.149375,2.093521,-4.508721,-4.652233,1.323917,-2.313866,-0.593551,3.128122,-5.868284,-3.446118,-2.524825,2.428690,-4.529738,1.753194,6.253286,-3.345858,6.759996,-7.410270,5.448593,-6.815076,-0.808859,4.677831,-5.337904,4.940980,6.960888,-4.580277,-6.887582,6.944083,9.740769,7.441475,-2.158565,9.655938,6.472428,-6.578165,-6.333368,3.616024,6.635558,6.911886,-5.530055,-4.324878,-9.419217,5.358638,3.314986,7.323450,7.313633,4.957030,-8.160481,0.510659,9.092779,5.629065,9.872493,-7.884938,3.847634,-7.006748,5.223177,8.664250,3.337016,-0.026321,-2.840022,-8.387845,5.028126,4.305562,-0.534335,3.914240,-5.762579,4.406297,-0.116076,-6.304535,6.544804,2.321726,-6.292760,-6.242760,9.541541,-7.723928,-2.435263,-7.240942,-7.641373,7.379336,-8.062599,-7.933896,3.608502,-4.539571,-7.702607,-3.935700,-8.396794,-1.586078,-9.581643,-2.254051,7.525251,0.841802,3.625287,4.696542,-7.211627,-5.600808,-5.756225,9.266969,-1.855501,2.252581,1.557352,-1.374736,5.344799,-2.173965,3.282140,1.674043,9.645844,-6.162786,-4.042403,-5.311593,1.766863,-4.146494,-6.207878,9.727356,8.459608,6.576520,-1.093361,-1.422165,-7.872888,-7.471122,-7.262253,-9.765193,-1.613320,-1.069142,2.068529,0.233406,-8.543994,-3.225251,-7.538174,3.958922,-0.980046,-9.458659,9.246884,-9.155823,5.377233,3.963090,-1.639813,8.731095,2.601995],[-8.027379,-7.988478,1.483217,7.936568,7.146236,0.175678,3.091724,0.019555,9.002512,5.657908,-1.805626,-7.685680,-9.149790,-1.945374,8.502862,1.147139,-5.477672,-9.267743,-6.917504,0.092004,7.361999,3.780445,-7.995081,-0.375945,3.382195,4.888884,-9.527557,7.011548,-9.587319,-1.101381,9.545573,3.590071,4.332334,5.660475,6.388517,-6.707035,-7.588405,-2.053100,-9.135614,-5.238726,-3.654540,-9.641782,0.374183,7.665075,2.406506,6.466615,9.265022,-3.446966,-0.405606,1.050345,-0.712438,-9.746643,3.016221,4.410521,8.151404,1.537666,0.810338,-0.252570,8.813857,-9.237320,2.603043,-7.188730,2.027304,-2.570007,-7.379692,1.939092,4.584284,0.950156,-6.413507,-3.108803,-3.043348,0.850529,2.521124,-9.668467,7.538277,3.867035,0.259372,-6.668502,-1.134067,-9.036727,-1.642407,3.389368,-8.705853,-7.001692,4.960527,-5.369978,-8.845085,4.352475,-6.428871,-4.562674,0.847867,-1.154312,2.222712,7.710992,4.949946,8.176430,9.913978,5.717455,7.624883,2.817149,5.668852,6.939211,4.963476,7.911905,-4.519310,-9.221727,-1.380444,-4.849948,2.038139,5.352897,-9.155808,-2.867680,-3.937786,4.338285,1.109806,-2.241091,-5.558845,-2.538281,4.128648,3.833215,4.179596,2.364542,9.748847,-2.870858,9.281649,3.689888,-6.436687,2.154667,-6.102228,-8.368996,8.029217,-1.594263,-6.727602,-9.449991,-9.016913,-6.854886,4.141918,5.167793,0.273021,8.640353,-5.478262,-2.627872,-0.400069,0.384690,-7.024304,-2.068753,-6.808993,-3.476307,9.353658,-6.972626,-3.381878,0.366026,-3.092988,-5.226803,-2.853642,-4.134088,8.167032,9.493329,6.444964,-6.877636,2.518336,0.802383,0.456123,-1.810888,-5.529332,-2.683353,2.683612,-6.317089,6.424482,-0.574061,-3.020405,-7.274124,4.896910,2.997750,-3.902621,4.986615,-0.434773,4.742026,-7.233399,-0.785805,4.018765,8.896787,9.122145,-1.070730,3.897177,-9.123173,-3.092527,9.803806,1.632727,-6.817374,-6.995584,7.791630],[-8.054411,-2.410046,-0.927040,-5.709082,8.664514,9.560866,7.944293,9.023926,-1.992058,2.744788,-1.330022,-4.948468,0.247228,8.140194,-4.068568,2.249319,-1.791486,3.195871,-5.748289,-7.584084,-8.672510,-6.554052,6.042161,-3.808146,-6.170031,-9.977644,-4.936339,-0.801934,4.835345,4.932977,-3.456613,6.708803,-9.307184,4.510478,-9.638159,-2.938891,7.682254,-7.997697,3.498056,-4.331636,-4.794731,-1.761904,-5.942391,9.913974,3.369490,2.821297,6.790305,-7.922488,-2.583885,-9.731358,3.763956,8.671087,-9.529816,3.334269,-9.442659,3.905460,5.083156,6.772224,-0.236082,1.674723,3.550088,9.490036,1.282912,-1.888773,2.413851,-9.213694,0.067573,-7.269730,-7.315300,7.888209,9.073788,0.041536,9.280429,-6.879850,8.313250,1.423268,4.872500,8.541916,-1.048471,-6.160084,6.099578,-6.891968,-7.853837,-0.103648,-8.541957,2.788007,-6.317679,-1.320265,7.340888,5.387657,1.069211,8.943780,4.342996,0.295373,-1.265907,9.278351,7.026935,-8.480913,-6.861429,-0.568072,0.188720,5.705912,-3.249993,6.289285,-7.522409,4.441919,6.907439,-8.662331,6.687060,-8.078102,1.041914,1.426099,2.132363,-8.085616,-0.789083,-0.031383,-3.755938,2.157095,-9.247980,-9.541357,2.432360,-2.492624,-5.252767,1.183953,-6.125444,2.882929,-6.898695,-4.055058,1.931912,9.873926,8.844867,3.589931,9.423390,1.981651,5.897611,9.605266,0.808197,4.924637,-5.068359,3.946487,-2.784014,8.950727,-5.067331,-5.199813,-3.437101,7.221116,6.938164,-1.510803,-7.562639,-0.794808,2.408655,-1.715859,7.854027,0.776322,7.027289,4.135086,0.372710,-3.728505,-5.473391,7.100423,-0.040486,3.311037,1.167620,3.005267,1.329571,8.754168,9.405127,0.274633,0.506654,-8.390803,7.046574,-1.456033,-9.159759,-5.381763,4.743198,-9.171397,8.403478,-6.686957,0.126293,-0.373897,8.259903,9.983632,7.850318,-2.930804,0.587858,7.598096,-7.931018,-8.895763,-1.439702,5.457306,-0.951223,-2.531146],[3.001831,5.722064,-8.457386,9.209245,5.533784,-6.803001,2.782890,-8.468884,8.916744,-5.296321,1.133334,5.640077,6.549542,-3.696503,-7.662459,0.853992,0.095332,-4.626309,-8.555591,7.555237,-0.229553,2.280395,-9.162034,4.123657,8.113656,4.089857,-3.916222,0.499858,-0.251470,3.188246,-9.402373,-2.397597,4.674404,6.919780,1.791150,-6.795229,-7.489184,4.364431,9.467565,-3.301311,-6.287594,0.439222,-7.299512,4.230180,-3.193601,9.314809,9.588589,-5.570821,-1.675623,9.720434,4.682309,-2.886908,9.351318,-9.427496,-1.514113,5.552728,4.915282,5.178887,9.331870,-8.736128,0.949368,-9.113175,0.627256,-4.883320,-9.531442,6.816708,7.151106,7.146194,-9.237466,6.422670,9.224572,5.825830,9.464209,-3.571643,4.371019,9.732210,9.729454,-4.254374,-9.175424,-4.611175,-9.084253,-9.306710,2.852536,-3.856164,-8.883315,-1.356194,-3.911921,-8.662449,-1.946969,5.125379,6.438475,6.950708,-7.205634,9.410977,-1.934939,-6.844756,-3.390986,-0.429631,-6.023453,1.002434,-0.298620,-4.558507,1.175196,-3.699653,-1.350779,-0.177344,-5.095433,-6.935220,3.000964,-8.867085,1.228243,-6.993678,1.676542,-8.607594,6.270943,-6.669709,7.474023,-9.165805,9.333803,4.062725,-8.334004,9.007571,1.906698,-8.205434,-2.783216,-9.510182,7.199878,5.516539,9.119051,-1.894072,9.524278,-1.165503,-1.315041,1.933000,6.505779,3.301489,-2.979117,3.964521,-9.267036,-3.292536,-2.217900,-8.169714,6.749870,-5.787672,4.842843,6.031353,-6.037972,-6.865889,3.740992,-2.617673,-5.440408,-3.050565,1.645986,-6.763713,1.415123,-9.565883,4.243086,1.839105,-8.802939,7.436508,7.788437,-4.255737,-8.918081,-2.733967,-3.859038,-3.684548,-0.585471,-1.316958,-7.552697,5.500471,8.948297,1.047903,-0.762309,-5.784423,4.055119,0.851006,-9.215680,-6.676773,-5.188246,-3.056421,1.790025,2.733827,-7.881415,7.968636,-5.386481,-9.461059,-2.380927,-7.470624,8.174768,9.477731,-3.736510,2.207279],[-6.410548,8.360304,-5.272972,-9.587182,-9.059027,9.032848,6.306606,-5.315916,5.328759,0.349184,-2.041934,-6.132171,-4.392184,-1.818948,-8.688164,-9.983311,8.241459,7.721893,1.883311,-0.743426,5.505395,-1.592194,-3.425912,-2.024027,-1.259026,-5.764149,1.555285,-5.472346,-4.174753,-6.188442,-6.828632,-6.631952,-6.249219,7.320795,3.893367,-5.786632,0.443712,1.143026,5.433420,5.625076,3.039014,-9.496612,-6.138214,5.623437,-5.979185,-9.459275,-0.770251,-3.591835,-1.721055,-9.809282,7.917252,8.789728,-8.314711,6.181971,-2.635947,6.494361,-6.119075,2.729312,-4.277377,2.294590,-0.423018,1.942465,-7.712615,-1.370408,5.313416,-6.160082,6.575976,7.735093,-1.100827,0.409870,7.618372,1.815657,-2.264142,-5.038450,9.832500,1.239417,0.001390,-5.756342,1.789066,0.325791,7.086137,6.081176,5.058810,-5.442225,7.279952,-2.677959,-5.313312,-4.373091,-2.238626,9.614172,7.940112,-3.732781,9.941453,-8.575975,4.347667,1.204238,-4.690435,0.687508,1.050129,1.744842,3.797863,8.583066,9.375700,-6.990481,3.730024,6.546232,0.842366,5.454359,-6.698284,7.939564,6.370654,7.206040,7.037089,3.982872,-7.198702,-9.939481,7.113328,-2.965337,2.569709,-6.758784,-4.091776,7.278246,2.923697,0.359932,9.307253,8.605906,1.167843,-8.730804,0.839387,-1.196580,-2.626142,5.118900,-5.120790,9.304953,1.341934,-1.968915,6.808579,9.922085,8.059682,0.743965,3.921895,2.365125,6.966632,7.501723,-4.866867,-2.853045,-8.492650,-9.947318,2.016568,2.357594,3.543510,2.695989,1.967497,-4.024119,6.875116,8.618920,-6.452892,4.521167,-6.702338,1.781111,-6.316597,-8.624739,5.215562,-2.201836,-0.142222,7.306151,2.139563,-9.854371,8.944058,3.380811,-6.746915,8.558129,-6.761824,-5.295496,-4.149492,8.665974,-1.200839,2.129856,-9.409471,-3.847639,8.893487,-0.500300,-2.851368,-3.409457,4.113321,-8.466033,-1.399896,5.275400,8.036680,-6.666553,0.912029,-5.545755],[5.526392,7.717022,3.230250,-6.462943,-4.784368,-7.360996,7.704779,-4.777570,-0.134238,3.641316,2.263158,9.385768,-9.121416,-0.689959,3.292633,9.355895,-2.366148,-7.769681,0.649217,0.267615,-2.726108,-2.369215,-0.193555,-1.034328,-4.789749,0.931801,-8.250555,-5.652428,-0.064827,-7.382909,3.914216,-6.911897,4.375423,-8.857598,7.235759,-6.888877,6.094519,-7.153732,4.354784,-1.949708,-5.181756,8.580839,5.085925,7.954208,-5.614788,9.707963,-1.283535,-4.747811,4.665190,-9.558581,-8.363687,-2.451802,8.432378,5.023656,1.811937,-2.524927,3.055044,5.262797,7.208444,8.341398,-7.364500,-9.909576,-4.846613,-0.356733,6.547226,7.975516,6.443559,6.608007,-2.995938,-7.110234,-4.568393,5.749373,-6.286521,-7.691357,7.312866,-8.073406,2.494752,-0.161532,5.773760,1.929971,7.293425,-0.058552,-3.968197,-8.111210,-5.388493,-0.628173,9.381349,-9.201089,-3.814141,-5.791236,-3.472642,-9.528253,7.522302,-9.234096,4.347031,0.721786,-6.800908,-9.501010,1.667418,3.706584,5.033303,-1.336336,4.756018,-7.485144,-0.556356,6.167161,8.922502,-3.359949,3.848217,4.607504,-2.295954,8.461451,-3.454892,1.967370,-4.781852,0.527357,-2.683355,3.511727,5.862359,-9.595522,-7.411329,-8.719830,8.106612,-5.127714,5.987708,7.749775,-9.958262,-7.980154,-8.265077,-8.712375,-3.733373,-3.920396,3.030643,-3.898389,-1.308272,-8.068455,5.678336,-9.797069,8.899057,3.627340,4.846769,-6.707420,0.142201,-2.178496,-9.001614,5.475734,3.866700,-7.282335,0.922944,8.526940,3.078959,-7.464968,-0.738280,2.648128,3.606446,7.398630,2.527082,-2.594351,-9.300900,8.020770,4.745231,-3.400171,-3.534635,2.774415,8.085337,8.081803,1.380813,2.475497,3.129053,3.739111,8.460271,9.516831,7.205809,-1.460802,-0.536869,-6.317672,-1.987769,-2.963019,6.836979,-4.847294,-3.970595,3.855326,0.726089,-8.244494,3.499122,9.912932,-8.775109,-7.071067,-2.827176,9.247773,-9.320610,-0.948727],[-1.535023,6.445725,-0.837496,2.820242,-9.594233,-6.343449,1.159868,-3.749845,5.394105,-2.551522,-3.430168,2.085454,2.865101,5.446392,-0.343060,-1.750582,9.727546,6.124413,7.578386,-4.207158,1.050254,4.473243,4.553060,-2.157997,0.784534,-9.024615,8.284003,-7.759366,4.299686,-4.994946,9.511463,-5.992722,-1.465599,-0.470926,-0.937969,1.900046,-0.997212,8.941970,-5.327685,-5.480120,-7.273661,4.651640,-1.185919,-4.040515,-2.567823,1.519366,7.290466,-4.317792,0.253719,7.678181,1.181215,-1.710262,8.554962,-3.673010,6.008726,5.663189,7.897930,0.625250,-2.726611,7.204950,-1.701168,-9.235664,9.498455,5.405660,1.851634,-2.302407,-6.428008,-0.194784,-9.317894,1.516621,4.996062,0.152791,-6.141450,-2.284540,-2.656941,0.330810,6.846587,-9.703652,-4.070121,1.957499,-9.300585,-9.463932,-2.289853,-8.053394,5.065048,-6.401386,-0.077173,-4.492526,-7.223367,9.799310,-2.985201,9.021307,-3.198406,-2.722076,-6.063412,4.321989,-6.163944,2.706793,-7.623523,2.605373,3.850385,8.646793,-8.888190,-5.714056,-2.069770,9.397250,-0.768459,-0.184913,3.987479,2.549513,4.094595,-9.691355,0.552888,-2.660286,-7.742222,9.351786,-8.723593,6.476152,-5.320393,6.071031,-2.006751,-0.815562,-1.922680,4.777347,8.361854,4.537552,0.905965,-4.629331,6.343356,8.347479,3.236954,1.655697,2.234232,-9.700911,8.828823,-8.065800,-7.973439,-2.634738,-5.325240,-0.131713,8.093220,-3.113633,-2.968881,2.645756,5.694932,1.458473,3.252291,-1.071332,1.094614,6.235394,3.631489,-4.850497,-8.876025,-6.124435,1.502935,-8.331744,-6.955211,7.200196,-8.633430,-9.242188,3.326631,-2.024455,-8.805658,9.223041,6.091272,-4.823895,0.688605,-2.856714,-7.923745,-0.307827,-6.354189,-1.545688,7.557669,1.956777,-4.212694,5.641433,4.676923,-7.296909,0.889262,8.564759,-0.271226,9.521556,9.244003,6.140143,-1.567668,4.373199,8.140594,6.983678,0.216753,-6.720896,-6.144605,-5.347003],[4.356355,0.401142,-8.392538,3.387453,6.182325,-9.221296,-4.902893,-1.899752,9.288257,3.774751,5.927117,8.064407,4.006572,-8.462338,-8.838136,4.880943,2.683706,-1.710550,-0.540396,2.633358,-7.698933,-4.441002,0.522029,0.516255,-5.784334,0.265433,4.965202,-7.128823,-1.124890,-6.850759,4.926366,-0.045995,-7.764477,5.040523,-2.205896,-6.581419,-9.241962,-5.621500,2.584692,9.212654,-9.951348,6.260675,7.764960,8.047246,-6.157093,-2.094423,6.803007,2.901371,9.077093,-2.613459,0.005268,-0.264471,5.126342,7.873348,-1.698288,-1.296304,-1.323389,-5.076263,-4.353941,8.632230,6.296018,-7.129049,9.267257,8.493195,-6.638765,-9.637033,-6.391579,-6.286675,2.416554,2.290507,-2.129378,5.055026,1.766632,-6.500089,8.914012,4.914752,-3.450234,8.614580,1.116539,-9.704245,7.905024,9.324296,-7.338690,6.276149,4.195013,8.366259,2.720185,-2.241118,8.465141,-1.882335,6.767201,3.592888,2.221777,0.941995,6.305231,2.425776,-5.349017,8.464690,-2.336573,9.497221,3.139954,9.816994,8.323957,2.999855,-3.205299,5.515442,9.367409,6.120096,0.686033,9.112937,2.544045,5.993710,8.244899,-4.398475,-3.513482,-6.008397,-7.364466,-8.257139,7.438356,-0.004063,5.495827,5.261155,9.210367,2.087774,0.532374,1.103153,8.890196,9.594570,0.620609,-0.159168,9.403560,5.527808,-4.244611,6.722290,-4.501590,-8.400078,8.558832,-0.259785,-4.887175,5.907191,5.507552,-8.766715,-7.028505,6.233417,9.941268,5.656320,-7.117142,5.381510,-4.729785,7.162706,-0.059286,-8.455497,6.984757,-0.947462,-8.496388,-4.855472,0.871387,9.653274,-8.772676,8.060866,-4.209883,-1.899646,-6.094191,-8.843946,-7.855150,1.105448,7.143543,-0.032481,-3.773966,-1.125357,-7.756419,-1.907498,-9.519998,6.016333,8.091031,-3.263259,1.112307,-7.840160,-2.089356,-0.745947,-9.481858,-0.282695,7.009922,1.195116,9.433022,4.662251,-9.762850,9.139603,3.208786,6.992269,-5.775664,-0.610890]], dtype = "float32")#candidate|7912|(8, 192)|const|float32
bop_7913 = relay.multiply(var_7903.astype('uint8'), const_7912.astype('uint8')) # shape=(8, 192)
uop_7921 = relay.log2(bop_7913.astype('float32')) # shape=(8, 192)
output = relay.Tuple([call_7884,call_7902,uop_7921,])
output2 = relay.Tuple([call_7885,call_7904,uop_7921,])
func_7927 = relay.Function([var_7903,], output)
mod['func_7927'] = func_7927
mod = relay.transform.InferType()(mod)
mutated_mod['func_7927'] = func_7927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7928 = relay.var("var_7928", dtype = "float32", shape = (1, 192))#candidate|7928|(1, 192)|var|float32
func_7927_call = mutated_mod.get_global_var('func_7927')
call_7929 = func_7927_call(var_7928)
output = call_7929
func_7930 = relay.Function([var_7928], output)
mutated_mod['func_7930'] = func_7930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_7962 = relay.TupleGetItem(func_7506_call(), 2)
call_7963 = relay.TupleGetItem(func_7507_call(), 2)
var_7965 = relay.var("var_7965", dtype = "int32", shape = (13, 2, 2))#candidate|7965|(13, 2, 2)|var|int32
bop_7966 = relay.less(call_7962.astype('bool'), relay.reshape(var_7965.astype('bool'), relay.shape_of(call_7962))) # shape=(13, 2, 2)
bop_7969 = relay.less(call_7963.astype('bool'), relay.reshape(var_7965.astype('bool'), relay.shape_of(call_7963))) # shape=(13, 2, 2)
func_5605_call = mod.get_global_var('func_5605')
func_5609_call = mutated_mod.get_global_var('func_5609')
const_7979 = relay.const([3,10,-8,-2,7,-8,5,-3,-3,-4,8,-1,-4,-9], dtype = "uint64")#candidate|7979|(14,)|const|uint64
const_7980 = relay.const([10,6,1,-10,-4,8,3,1,-2,6,7,6,4,-6,-4,1,-3,1,-2,1,-10,-1,4,-9,-8,-6,3,-3,-5,-2,-2,-10,-1,-2,-4,10,-2,6,-2,-4,-4,-5,4,3,-7,-6,-9,7,-9,-10,10,8,-10,-7,1,-5,4,1,-6,-7,1,-5,2,-8,-8,4,2,-1,-8,7,2,6,1,-5,-4,-1,6,5,7,6,6,5,-4,10,-5,-1,10,6,-7,-8,3,-5,-7,-6,-6,10,-4,9,1,2,-8,-6,2,-10,3,7,-7,-5,-3,-9,-5,10], dtype = "uint64")#candidate|7980|(112,)|const|uint64
call_7978 = relay.TupleGetItem(func_5605_call(relay.reshape(const_7979.astype('uint64'), [1, 2, 7]), relay.reshape(const_7980.astype('uint64'), [8, 2, 7]), ), 3)
call_7981 = relay.TupleGetItem(func_5609_call(relay.reshape(const_7979.astype('uint64'), [1, 2, 7]), relay.reshape(const_7980.astype('uint64'), [8, 2, 7]), ), 3)
output = relay.Tuple([bop_7966,call_7978,const_7979,const_7980,])
output2 = relay.Tuple([bop_7969,call_7981,const_7979,const_7980,])
func_8010 = relay.Function([var_7965,], output)
mod['func_8010'] = func_8010
mod = relay.transform.InferType()(mod)
var_8011 = relay.var("var_8011", dtype = "int32", shape = (13, 2, 2))#candidate|8011|(13, 2, 2)|var|int32
output = func_8010(var_8011)
func_8012 = relay.Function([var_8011], output)
mutated_mod['func_8012'] = func_8012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6728_call = mod.get_global_var('func_6728')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_8022 = relay.TupleGetItem(func_6728_call(), 2)
call_8023 = relay.TupleGetItem(func_6730_call(), 2)
output = relay.Tuple([call_8022,])
output2 = relay.Tuple([call_8023,])
func_8029 = relay.Function([], output)
mod['func_8029'] = func_8029
mod = relay.transform.InferType()(mod)
output = func_8029()
func_8030 = relay.Function([], output)
mutated_mod['func_8030'] = func_8030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8029_call = mod.get_global_var('func_8029')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_8046 = relay.TupleGetItem(func_8029_call(), 0)
call_8047 = relay.TupleGetItem(func_8030_call(), 0)
func_6773_call = mod.get_global_var('func_6773')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_8074 = func_6773_call()
call_8075 = func_6773_call()
func_7824_call = mod.get_global_var('func_7824')
func_7826_call = mutated_mod.get_global_var('func_7826')
call_8077 = relay.TupleGetItem(func_7824_call(), 0)
call_8078 = relay.TupleGetItem(func_7826_call(), 0)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_8082 = relay.TupleGetItem(func_4770_call(), 0)
call_8083 = relay.TupleGetItem(func_4772_call(), 0)
func_6728_call = mod.get_global_var('func_6728')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_8085 = relay.TupleGetItem(func_6728_call(), 0)
call_8086 = relay.TupleGetItem(func_6730_call(), 0)
bop_8108 = relay.floor_divide(call_8077.astype('float64'), relay.reshape(call_8074.astype('float64'), relay.shape_of(call_8077))) # shape=(15, 4, 11)
bop_8111 = relay.floor_divide(call_8078.astype('float64'), relay.reshape(call_8075.astype('float64'), relay.shape_of(call_8078))) # shape=(15, 4, 11)
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
call_8121 = func_3456_call(relay.reshape(call_8046.astype('float32'), [7, 1, 5]))
call_8122 = func_3456_call(relay.reshape(call_8046.astype('float32'), [7, 1, 5]))
func_6728_call = mod.get_global_var('func_6728')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_8132 = relay.TupleGetItem(func_6728_call(), 0)
call_8133 = relay.TupleGetItem(func_6730_call(), 0)
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
const_8135 = relay.const([5.142696,3.941534,1.665440,-2.974737,5.701438,2.476906,-4.339585,5.292883,5.906825,1.227782,4.591616,4.973455,-4.032712,1.383031,-6.464017,1.290472,5.703899,1.198545,-3.637877,2.308260,1.492019,-4.862137,-7.621883,7.076848,-1.127930,-6.295948,-3.441689,3.387909,6.188403,-7.842925,7.590162,7.050909,-2.358193,0.825301,-3.489468,-7.566054,8.781385,6.605507,-3.422764,-6.678760,-0.539267,-7.768312,-0.535229,0.780301,-4.284062,-2.497651,6.396561,-8.722001,-3.203958,6.838158,-3.465857,-8.021882,-5.345185,-9.805202,-6.490204,8.117619,5.278897,9.412274,-5.686586,-0.255476,-5.732909,-1.723203,-4.321603,9.019237,-6.977103,-0.215086,-9.320823,7.484498,-1.023360,2.397007,-3.526568,2.876430,-7.472774,1.731612,-4.986289,-8.354556,-6.804561,-9.363935,2.966945,2.534428,-5.787239,7.321249,-8.993212,7.163811,-7.150641,5.687034,-8.615922,-6.936334,3.845549,0.519247,0.397723,-0.764535,-2.316719,2.683183,-8.100270,8.277611,-9.900532,0.459376,8.459716,6.446725,1.467829,-8.508917,-5.433109,9.366436,7.033543,0.991641,-6.055890,-8.960057,-1.796070,-8.131008,2.590022,-0.024689,-0.241205,-6.230844,-5.901605,4.957557,3.066491,7.370619,0.639722,2.253690,0.477544,1.256343,7.777968,-3.274070,3.079316,-5.758320,3.511154,-3.318078,8.790942,6.741634,5.624130,5.577027,0.727925,-3.016631,8.737544,9.657108,-7.113040,-9.924313,-0.768232,7.830986,-1.543178,-5.679794,-6.582202,0.904720,-7.463459,-3.922404,-4.775375,-1.325864,-5.670565,-6.501863,-9.532955,5.242858,-0.721302,-9.041892,-0.121062,5.401601,-5.775695,-8.038714,-8.477480,-5.049748,6.435431,-2.792131,-1.554128,7.547714,0.398330,0.324706,8.242324,-4.440166,-8.625678,-5.781440,4.428197,8.566543,-8.954236,-1.797282,-4.512856,3.025679,0.675663,9.659092,-3.735556,6.370191,-1.976117,8.553954,7.760033,7.906760,6.232366,-7.806661,1.935576,-9.726769,-3.963446,4.285222,6.809105,-9.869805,-7.623127,-9.120944,-6.099303,1.506443,-9.918864,-3.873101,-1.633766,-3.817679,3.187472,-2.206970,-7.275249,-2.851850,-4.733534,1.495132,-6.020695,-6.589052,4.101094,9.689615,-5.626513,-8.023096,-1.255004,-2.080897,6.444552,-2.469117,-1.732403,9.375866,2.312654,6.444278,0.376421,7.513395,-3.109679,9.247121,-6.555525,5.102311,9.586765,-7.268036,-0.557886,-5.785089,5.996265,-7.837423,-1.275308,-0.631198,-6.984632,3.451368,2.388668,8.039229,-5.918479,9.002094,-6.753580,-0.101583,3.776605,9.654359,9.105055,9.667687,-3.231817,-9.579187,0.246521,-7.921901,-8.403595,-9.456658,-8.649291,6.764576,-3.561305,3.061448,7.017401,-1.107091,-1.992555,-6.188533,1.062379,-0.177966,-0.035029,-9.963273,-5.428123,5.014557,-8.716144,-8.527343,7.286958,-7.576864,-2.697937,-6.740460,4.063552,-1.920814,-1.230597,8.157372,-8.231030,9.129534,8.637922,1.587445,-9.976069,-3.984823,-2.458018,8.180193,7.894133,3.900692,-0.653290,1.780239,-4.198773,8.294975,4.495993,-3.823214,7.555739,-7.643670,-5.829066,-6.881046,-3.069711,0.467549,5.572918,-0.333671,-2.119218,-9.743978,-3.810606,-9.891952,-0.664846,8.026731,1.605575,7.971653,-9.002345,9.477486,0.842144,7.214764,-0.617294,-7.331321,-2.431479,-1.235313,-6.694149,2.082733,6.998573,7.038162,0.507108,2.165589,0.108445,4.579826,-1.688612,-9.896742,-5.017124,0.595862,-9.275751,-3.403597,-5.785882,-4.396031,-9.230806,5.233425,1.849164,1.907761,-7.983815,3.433299,0.268565,6.384623,8.880909,-3.171483,3.949899,5.701441,7.138927,-2.666811,-7.215401,9.196205,-9.015387,-8.493064,5.960987,7.350413,-1.279860,9.700267,7.147528,0.687251,-6.038549,9.439538,9.275319,-0.369144,-0.353932,2.150635,9.720219,7.562249,5.217113,9.390087,9.270592,-0.363368,-9.218203,-3.680250,-0.458866,-8.043055,3.355735,5.374726,-0.812620,1.729685,-1.372724,-7.144977,9.213976,-6.554925,9.282081,-6.233527,-4.907766,0.953183,-3.177157,-5.448189,9.002615,-9.977841,-4.524375,-4.274893,9.297159,-0.094229,-1.149216,4.140774,-2.681989,-2.068001,6.735831,9.511499,-1.905702,-5.667108,-6.922362,2.728575,-1.280569,-7.538283,3.126606,2.884655,-4.000312,5.912899,-0.467377,8.012917,-5.572630,5.119665,-2.763842,2.033273,0.942885,9.946595,-1.717898,3.202758,-6.395063,-6.315969,-6.296389,-7.594665,4.597262,9.464631,-4.964771,-9.921213,3.126817,3.974754,-4.631443,-2.508741,-1.787026,0.164049,-0.387570,1.903862,-9.694821,7.689030,-6.782498,-9.779359,3.758275,8.571213,-0.715580,-8.124351,0.652430,8.114545,-8.174912,6.388492,8.869145,0.331108,-1.607685,2.986915,-0.603294,4.329143,-7.711688,-3.970586,-3.920391,-8.373355,-8.321170,-6.253639,-0.484748,8.382355,5.696085,3.903586,-5.642924,-9.294512,-1.638553,1.810955,-0.686585,9.590539,-4.911534,-9.737968,8.160904,5.498100,7.007476,-4.686512,1.629758,-1.090274,-3.002648,-0.857417,0.323139,0.557154,-5.760816,-9.302231,-0.133315,6.362976,-1.977629,8.852423,-3.995627,4.374578,-3.017995,4.463860,9.125621,-0.727121,-5.830893,-8.998611,4.811186,9.824335,0.502254,5.395278,5.515074,-4.139548,-7.673682,3.607813,2.136086,7.114815,-1.881559,5.680259,-6.796998,-6.843567,-8.497194,-0.991967,-4.207967,0.470180,-0.748904,3.373926,-2.150484,5.834253,8.245568,3.533223,1.014107,-0.013088,-2.122706,3.329177,7.651233,9.544460,8.269929,-8.799379,9.008351,5.239403,-4.825017,9.490028,-8.263996,0.002620,0.712476,-1.564050,7.790314,2.560952,2.303967,6.580783,-5.972516,-2.162875,-6.906136,7.754533,8.286312,1.105963,-2.833308,-5.769507,7.521922,-3.614061,-4.306865,7.608480,-2.713428,5.006348,-2.023569,-7.075393,0.417252,-2.643431,5.418353,3.256955,-7.719911,-5.347069,5.977507,3.718065,5.445380,-1.204080,4.894267,7.212155,-3.257348,8.485374,5.555356,8.019632,-9.565847,5.079246,1.707831,-8.652075,2.099080,-1.758264,3.038525,-5.322417,-4.686922,2.813737,-8.055853,2.084222,2.277615,1.249785,-9.217980,-3.405584,-6.539844,7.792508,-4.783768,7.541175,-9.863346,2.203997,-3.190862,-3.090310,-6.856326,-9.520759,5.911302,3.618198,-3.923441,6.299880,0.310495,2.271481,6.059636,4.292386,3.124090,-9.865185,1.635332,7.124171,9.389324,-8.214723,4.109533,-8.338923,-6.677836,-3.245623,8.979629,6.913591,9.647138,-5.890220,1.741203,-1.879984,5.788292,3.350280,-2.928601,-6.596846,-0.630353,7.853633,8.136744,-8.466422,8.140884,-2.983882,3.648715,3.900151,-5.643026,6.015041,-6.005090,-1.861940,-7.158934,-4.261236,7.592144,-7.273342,7.080800,8.666753,-7.907203,-8.311331,-3.985563,-5.341311,-2.392545,-4.795672,5.418618,0.430613,-5.344031,8.748277,1.154048,9.197075,-6.013602,-4.314954,-1.181751,-1.750253,-2.341474,-4.654978,7.276568,-2.952454,2.486879,4.536350,-0.328137,-3.869086,-4.587672,-2.948663,6.486879,-4.336477,1.895738,4.663303,8.736298,-9.554494,-6.848168,-5.895273,2.721202,0.478635,-6.794133,-5.379454,1.472725,6.496903,-8.361416,0.482174,9.366685,-0.828013,2.550772,-8.636733,5.655148,-3.716788,-0.347279,-1.732666,5.816027,-4.997397,-7.369572,-9.845739,7.090485,0.218969,5.755702,5.471020,6.985120,-9.901108,7.105121,6.592595,2.312729,-7.564539,-3.799864,-4.989312,-1.883215,5.174770,7.874364,7.535278,2.062822,-6.379113,3.077484,-2.602004,0.291061,9.082493,8.310436,-2.847730,-1.905569,-8.066398,3.530965,-8.925740,6.443647,-5.558140,-6.338732,5.086827,-2.853251,-6.544191,5.931928,-5.806855,1.824916,1.107271,-1.268800,-2.469003,-0.931540,-7.006151,8.524577,-2.093021,-0.545179,9.827275,-4.865237,4.718776,-4.539702,-4.066316,-9.648529,8.811762,4.219818,-8.329910,-3.669855,-5.137473,-6.135965,-2.246028,-0.440367,-1.984273,8.599158,3.729455,1.723464,-4.424303,-4.284683,4.405176,-6.741117,6.659429,-1.025963,4.017825,-9.298782,5.420711,-6.730522,-0.582689,-0.102317,-3.593785,-7.802320,1.174438,-7.405188,6.641195,3.332503,5.044590,9.149926,7.782489,-0.643934,-5.379481,-0.998644,3.757472,4.719745,4.911941,8.762766,3.614099,1.044997,0.325144,0.167758,1.318586,6.703984,-8.184703,7.238945,-8.947106,-8.288386,-9.044969,1.054508,-2.928218,7.813500,-7.875795,4.762729,-1.060692,7.692137,-5.782960,-4.200768,6.764195,-4.136591,0.227078,7.404232,4.682976,-4.315385,-2.422638,-5.844315,0.837009,8.220285,-5.250022,8.881770,1.519155,-9.054539,6.611360,3.551139,-6.335531,-1.488897,9.445838,-1.576543,-8.912460,-5.445381,-4.869294,1.504163,-3.532161,9.239718,2.673493,7.861296,0.428645,-6.177185,7.647323,4.921800,3.343234,9.551476,2.295881,9.503500,-6.391614,3.843229,-6.793089,-4.150766,7.909901,7.239078,2.739962,0.179425,-7.959074,7.561756,-3.486932,-7.929921,6.072223,-2.600284,3.682593,-6.294101,-0.347652,-5.808743,-8.883234,9.344969,-4.170681,-0.756474,-1.362083,2.084407,9.346863,-4.168777,1.334329,8.454002,-4.426327,-0.573899,4.810343,0.797006,-1.430693,4.577384,6.626816,-1.698519,0.601912,6.542853,-9.380374,4.972826,7.319573,0.996683,-4.907767,0.440092,5.231430,-6.850424,-5.150315,-9.074487,6.891716,0.756596,-7.130156,-2.388714,-4.438680,6.267482,-5.284834,-7.569455,-2.628311,4.637716,-1.215240,0.992861,-3.567399,6.040651,-3.414737,8.794329,3.618424,-0.640830,-5.403061,3.612843,-1.646119,5.923959,2.574500,-1.228409,-7.116194,-0.899892,6.966559,-6.304846,4.957120,-6.653793,6.477627,4.674229,9.764639,-1.034065,8.695464,-2.540942,3.869070,-1.599576,-6.038196,-2.742173,-5.356295,3.174247,8.878094,4.765865,8.608305,-8.781768,8.658494,3.717039,1.244275,-7.284859,-4.932955,-2.116180,7.276526,-1.412467,5.523572,-3.418193,-5.654994,3.858972,6.377168,-5.244143,0.669772,4.112707,0.249650,8.275952,-5.963680,1.859117,-3.633538,-4.746957,-9.758722,0.697819,-6.325474,-7.774407,-4.360526,-7.450621,-7.678764,-6.665167,4.479948,2.245858,3.170334,2.523766,-0.872145,-5.523376,-3.095296,-5.672424,2.296167,-6.969926,5.635902,-6.102623,1.417483,3.609743,-6.505544,1.246026,5.883176,-1.763518,3.078882,6.190240,-2.447437,-6.747330,-6.572483,1.517647,0.842171,8.190868,-8.145048,-9.997994,-4.404174,-2.839157,8.812104,-2.004507,-4.520775,3.183282,-7.066525,4.733412,-2.637191,2.527835,1.485429,3.376719,7.589073,5.739841,-8.144241,0.484360,-5.626392,0.989039,6.689932,-8.226211,-5.482986,1.944818,-2.450445,0.050415,-8.673404,-9.065005,-1.565935,-8.342834,-2.434232,5.509756,4.954688,-6.092422,-1.199143,-2.985295,1.181693,6.449461,-6.529058,9.823045,-9.627296,-3.402941,6.146014,-0.239693,-4.222811,0.578929,-4.465203,0.641964,8.548932,7.761212,-0.041141,9.720455,0.014831,7.060966,7.694910,-5.443928,-4.270661,5.528763,2.731301,8.770204,-1.199213,4.083631,9.415464,8.915361,-0.614924,7.519477,-4.166936,-6.484765,6.572767,4.912866,-2.110430,-3.679280,-8.610582,1.478195,0.740318,4.375601,7.738326,7.682573,-4.779576,-5.649147,8.599804,6.306821,-4.471522,3.242641,5.973308,9.888403,0.857945,-2.787303,6.278774,9.627102,-0.710469,-5.397276,1.651684,0.090151,-7.105294,-5.425371,7.463820,3.019655,-4.901791,6.796301,-9.091870,8.971998,6.389668,8.676442,8.848468,3.714044,-7.233866,-3.499917,4.286575,5.592687,6.739252,-2.613803,5.330627,-7.136543,-6.166124,5.654386,-6.899618,-4.893029,6.227284,-8.964881,4.404607,-9.274589,-2.262804,9.630148,-5.050144,0.391399,9.701608,-1.840087,-5.986878,-0.436150,8.295190,3.405010,-2.195829,5.810969,5.249159,5.207962,7.137516,-7.315908,-1.593228,-9.460622,-2.729100,-3.787457,3.453349,-9.434087,7.986047,-7.775225,4.899854,2.990225,-6.339473,4.627334,-6.648153,-7.293343,-7.816987,8.072169,-0.822477,-6.494458,-0.045182,-6.594578,3.729447,9.289115,6.072626,8.837003,3.847217,5.649124,1.362813,8.622911,0.390630,-7.990543,3.589288,-8.476285,7.062727,-2.295881,2.422133,7.894621,-8.402124,4.372790,-4.358378,-7.113081,9.120621,6.026227,-5.094999,3.152984,-2.967044,9.433356,5.566581,-4.236648,-7.705455,-2.219457,0.067470,2.534873,-6.866398,-1.467790,8.613649,-7.928012,-1.214146,-8.215430,2.871693,-9.517201,5.699289,6.624996,1.075952,8.401343,-8.107587,7.161913,1.574095,1.221172,9.194870,-2.609141,-3.500499,-1.845140,4.876923,1.132616,-1.444778,-9.616688,-8.775984,-8.601424,2.730133,4.287245,-2.930684,-0.955682,2.856202,3.745127,9.155722,-0.218794,3.405551,-8.796168,0.682302,5.938179,3.475634,5.740250,5.719185,1.387613,5.981116,-2.151789,5.416011,7.125126,0.947777,4.150338,-6.622370,-8.000772,-2.125972,-4.046670,0.956846,1.605567,-5.545715,-9.898291,1.753203,-7.434716,-6.755172,-9.631374,3.136239,9.899235,-5.757826,0.220839,-6.159232,-3.562252,-5.556455,-2.971843,-7.832187,-9.459467,-3.323252,-8.708046,-4.455552,-9.945628,-0.282647,-0.944644,-5.219763,-0.503455,4.299356,2.152094,5.352853,-1.786883,6.713626,2.161134,7.988361,-5.407837,-0.407084,3.270883,5.884147,-2.526050,-2.126120,-3.835739,-8.641242,9.289029,-6.596033,9.529104,6.170356,-3.961621,-1.725876,-8.710763,9.397150,1.499874,-9.191026,1.158353,-8.256491,5.278155,-1.639711,4.659849,-9.987240,-6.070852,9.999289,-4.993597,-7.102594,8.700990,8.455968,-6.270983,-3.568836,-1.157359,-7.218249,0.336405,5.511659,5.603380,-1.540266,-7.342206,2.616843,4.582544,-8.930883,6.856884,-4.346658,2.111470,9.526614,0.108347,3.805583,-2.115511,5.365295,-4.478046,-6.782269,-0.273526,-9.605784,3.184202,-8.836216,9.886895,-6.026033,3.268093,7.482359,-0.370618,-6.006859,0.489127,-4.305296,0.812067,6.412693,-6.013533,2.249210,-1.307742,-9.754026,5.392780,-6.325386,7.742303,-8.062781,-2.911046,-8.519276,-5.668058,-9.262184,-9.095778,3.759564,-4.241778,-5.731280,-4.648213,3.619818,4.750792,-0.248358,-3.042458,7.658065,7.764991,-0.589058,-9.463133,9.275513,5.027669,-3.190390,-2.710911,8.590218,-8.106033,1.509242,4.046383,3.220365,-8.239332,-3.152312,-6.567843,7.924561,6.343016,9.518272,-6.634468,-4.935957,-2.423285,2.309684,-9.706634,0.764667,-5.074823,6.411291,-7.203430,3.243852,-6.153899,1.026453,9.901256,-5.910110,3.496612,-4.678897,-1.285377,6.964823,8.834665,2.628186,-8.025740,-7.611919,-0.448704,-4.524960,-7.837310,5.785295,8.541226,-3.135387,4.781936,2.913171,-3.473422,-8.384907,-0.545071,-7.782634,0.454279,5.932529,-6.454302,-3.411035,1.191948,5.339926,-7.254295,-0.318981,-3.391662,2.094103,-4.568201,-5.968381,-6.577540,3.075444,-0.751055,5.020007,-6.178197,2.512894,-3.130373,2.544191,6.683176,-0.936924,1.304645,1.287656,1.960824,-7.398685,-0.135994,-1.043270,5.450063,2.393350,7.144432,8.597618,-8.818772,7.032334,0.851646,-3.238526,2.903624,-6.242527,-4.833066,-6.658721,-0.453694,5.781697,7.765073,-7.789315,9.551185,8.480201,-4.128825,-6.322613,3.602429,8.558869,-1.540586,8.121181,-2.054763,2.987801,-2.889603,-1.391771,-8.789141,7.683080,-1.128846,-2.947656,9.860089,-7.309174,6.964869,-0.014546,-6.424272,4.513481,-4.240014,9.509156,-4.596283,9.664174,-9.633412,-4.178303,7.310370,4.003412,8.304899,5.972093,6.034599,-4.558350,1.978914,6.583031,-3.547725,-9.093720,-7.039145,-9.200590,-2.959909,5.010100,4.869150,3.982305,0.142853,-7.409326,3.758247,7.312272,-9.025649,8.385422,8.312869,8.698243,0.099361,-9.925277,7.617819,-6.455739,-5.981348,8.325397,5.193038,-9.619351,2.616862,2.052217,-4.257394,7.053759,-1.149486,-1.051625,9.606146,-5.188599,-5.005175,-2.729597,6.321731,0.004931,-1.277937,5.678491,-6.769942,-5.687647,7.965989,-8.931665,9.342220,-5.474364,-4.442214,4.302908,-8.965462,-5.922733,-4.675210,2.270418,2.010772,8.248985,2.003927,-3.481712,-1.214693,0.015108,-5.052976,9.131086,6.915523,-5.753914,3.764807,1.207833,5.568800,-9.442006,7.037321,0.930644,-3.806716,-7.189564,7.256816,7.755218,-1.714433,5.877488,-2.046254,-3.862355,-5.407802,9.995720,-1.406328,-2.399859,-2.120450,2.639264,-4.630551,6.506095,5.887001,-5.249571,-8.709335,-8.977548,-5.855728,1.357602,-2.178616,-4.793501,-8.654067,-8.197322,-6.389965,-4.316139,9.494979,-0.044747,-0.875581,2.600801,-4.614093,8.195686,8.862977,1.096613,2.511352,1.757830,-5.787764,9.045289,5.277339,2.490613,-3.128267,2.382419,2.904384,2.163585,2.508577,5.216720,-1.083799,-4.488192,-7.063125,4.037745,-4.788072,9.724983,-7.309153,-1.577134,9.658602,4.959381,7.420643,1.074735,5.825520,1.385824,0.949868,-3.700440,6.932181,-8.575632,-1.030218,3.794107,-1.752741,0.791760,2.261842,-7.443696,5.297967,-4.257514,-0.961284,0.333748,-7.274503,-4.628565,0.166740,0.635519,8.940534,-9.271438,7.839914,3.115542,-6.200289,-8.499333,-5.888342,-6.449691,0.544509,-8.382904,0.585234,0.078365,-3.166292,5.433796,-3.092533,-2.081373,-9.920988,0.772614,1.688430,8.577952,0.809836,6.375536,6.498539,2.462993,2.437707,-2.617636,1.750781,-2.075283,-7.275776,7.900693,7.812890,-2.551240,-0.107325,8.992483,-4.646477,1.737014,9.966514,4.738218,8.029450,0.740286,0.400073,9.866989,6.940244,-7.254551,5.437340,-7.118977,-5.949536,6.634793,-2.424236,-8.203692,3.772118,-4.610005,-2.249662,0.403646,-5.302507,-9.857432,1.150171,-2.486625,-0.822791,-3.152720,-4.223903,-3.507681,7.519678,5.715386,-4.787207,2.357135,9.033461,-8.932164,7.844601,1.513112,-9.295512,4.801641,5.202080,-7.052395,0.887582,-6.261786,2.636890,-3.483320,-3.951057,-8.188561,6.428537,-1.042993,6.646306,-7.251333,7.241125,-1.340712,-3.084439,7.736508,0.867952,4.140129,-5.803023,-2.180688,-9.267001,-3.326596,-8.313344,6.237243,-9.436209,9.140593,4.457270,1.524936,2.818293,-0.657357,2.650316,-0.945974,-6.402487,4.816158,5.687470,-7.735846,-6.983065,-4.370600,-5.474049,-3.835633,9.023433,-9.806614,-5.246713,3.358205,-2.694321,6.546826,6.647000,-2.379605,1.934015,-5.357021,-2.732251,-9.447930,-3.993152,9.855532,-6.009365,9.409359,1.042707,-4.052791,1.494671,-9.736406,-4.351271,-7.709486,9.819928,0.962150,-1.990647,4.609453,-8.902081,-6.341719,-5.247001,5.085844,3.419726,-1.385470,0.924829,-0.170933,0.068863,-1.235393,-9.861815,6.588184,1.528147,-3.368294,3.490537,-5.407328,7.994600,-4.100844,8.695716,2.217942,-8.020410,2.134411,-2.823939,4.487396,-8.792966,4.318181,-8.097369,-8.394967,3.289050,2.632667,-0.448899,3.810803,-4.738175,3.565322,9.006236,7.399525,5.853753,1.418622,-4.424941,3.561840,-7.088863,-1.088505,4.895867,5.318511,6.946695,1.997977,-2.271566,-4.165337,-7.957454,-0.507138,-8.374305,-1.940946,6.787542,1.233120,-2.837007,-7.811998,-6.743649,0.238390,-8.526421,-6.910032,5.751670,9.356425,-6.434846,9.702327,-2.554916,1.815608,4.128367,-2.154766,8.662260,-1.773419,-5.230978,7.145124,5.026603,-9.035887,4.792472,-6.514591,1.466585,-2.077534,9.210806,-5.954126,-7.583584,-3.372831,4.777288,-2.431657,-9.580417,-3.829732,7.632314,1.708615,-4.092094,-8.460957,7.535205,7.621434,7.377194,-0.636431,0.368106,-8.246877,-0.923529,8.214706,3.338218,1.720733,-7.328190,-8.424526,4.935571,0.428194,6.163321,2.720308,-7.268771,5.057269,-8.308461,-9.330929,2.627234,2.150471,1.548283,4.342329,-8.501771,-5.687856,1.999344,9.096145,8.447351,-0.160481,-9.422750,2.488506,-8.167555,-5.511411,-1.269630,-6.236778,3.585855,-8.483918,-5.310143,2.249846,-9.944875,-5.622084,-5.741209,-1.743830,-6.587532,2.826338,-4.699621,9.350504,2.230667,2.047067,-9.163797,8.941230,-5.064675,-7.745225,-6.755388,6.916377,0.722738,-7.939015,3.898057,0.782745,0.235715,0.763020,8.268004,7.066693,-3.851386,1.313736,-7.924793,0.178605,-2.004835,-2.706215,5.252150,5.808032,1.544701,3.286724,-9.393880,-6.634543,5.825464,4.994082,-4.836855,0.388009,6.159986,6.070606,-2.022436,-8.895588,-6.278529,3.998872,7.575501,-4.687731,-8.036481,7.046717,7.149921,-9.137869,4.137849,7.937535,-0.433194,9.064503,6.582454,-4.742235,3.575545,-5.697314,2.647231,6.863795,-3.659762,7.436585,2.702940,7.683153,-4.949096,3.496145,0.185594,7.576321,-4.709629,-2.388841,3.327692,1.076884,2.903563,-8.734967,7.764566,0.046953,0.561957,-2.832080,-5.336625,5.819628,4.625620,-8.776229,-7.904006,9.049218,-1.857725,-0.165285,-9.732124,-4.606906,-6.647341,-4.200385,1.562878,2.116116,-3.190304,1.064666,-8.411310,4.345356,-1.023836,-3.360667,3.283430,2.787776,2.374998,9.092713,9.751633,-4.475930,-3.918325,1.588755,-3.671487,-8.506941,-3.108911,0.263036,9.724548,-0.511075,7.486479,-3.146407,-4.149074,-7.157371,5.492167,8.023613,-1.913392,-7.943653,-3.537984,-7.410765,8.119914,4.607071,-5.251613,-8.282806,2.664789,0.439680,7.922765,8.512083,8.611803,-5.048501,7.980290,5.301134,1.769955,-7.647154,9.980620,-7.932849,-6.371877,-1.809639,4.952634,-3.096171,-1.455023,1.858590,7.817364,3.730595,-5.936991,9.601521,-5.401137,0.528564,9.473138,3.051863,-5.919140,1.053716,-3.356238,-8.605632,-2.796394,-1.398803,-8.260156,-6.448653,0.884346,4.277204,4.030889,3.329379,9.204858,1.094999,5.260784,-0.455520,5.584546,-1.057169,0.411775,7.725005,4.662212,-2.799892,8.508796,5.607629,1.211624,-3.969207,6.113154,-1.311498,6.521136,2.610839,-5.815227,-8.037092,9.943557,6.051894,5.006153,-6.775794,0.532868,9.668814,-2.331351,3.075439,7.311122,-0.258539,1.505943,0.346381,8.324193,6.382056,-6.736337,3.061507,-5.115649,7.302633,0.857131,-8.168991,-7.943954,9.147580,-8.633267,-9.934692,-8.793677,1.528401,4.809806,-0.605403,1.809747,5.086771,-0.253306,-5.387570,8.207287,-0.399966,0.555139,4.274271,-2.110076,-7.249583,9.486452,-6.557193,-3.399561,-3.579061,4.642128,-5.776168,-7.234806,-8.959979,-8.117317,-1.518941,-0.373610,-7.094717,4.991706,-0.248494,-5.692216,9.154556,1.351050,8.403428,7.589809,-9.390775,2.439097,3.105398,-6.767050,-8.260861,-9.530932,-9.040723,1.840920,5.695088,2.415069,5.483444,-3.369492,4.642057,-0.567430,4.185614,-3.423638,-5.172630,-6.337126,-1.565131,-2.421230,9.299091,4.194079,0.530829,-3.078609,9.502461,-7.344392,6.322464,3.440736,4.323735,-5.876627,2.117151,-1.977566,-4.757050,-2.705754,5.339457,9.705305,5.452737,-4.997419,7.957220,2.387426,-5.326938,3.250501,4.588057,5.115250,3.552824,8.851758,-4.832582,-2.036397,6.299474,1.743065,8.785413,5.459787,7.597800,-7.463901,9.945267,-3.598937,0.963754,9.995323,-8.562039,8.760484,-6.388216,0.124733,-5.782298,9.516589,-7.397321,-5.344921,7.314035,-5.043054,-0.623998,-7.875841,5.372262,4.919436,-8.376490,0.796609,2.047088,-3.679009,5.117187,7.713669,-0.557346,3.720571,2.701265,-7.607460,-9.131731,-5.704471,8.789090,-2.648882,8.623522,-4.223400,-9.083078,-8.396606,-5.622003,-0.222858,-2.676586,-5.184784,-4.270343,9.938170,0.859716,8.628045,9.503023,-7.563088,-5.239372,8.446410,9.797670,7.178751,2.972557,7.994184,7.878995,4.728640,3.952544,-8.742359,-6.259343,-4.850806,4.858126,4.855354,5.169200,-9.913365,-2.794519,7.033378,9.731962,1.843874,-6.296135,-3.506823,-3.558439,-2.190390,1.769164,-5.654631,-4.846267,-6.204923,-8.087171,-4.061203,9.613583,8.996402,-3.564543,4.394650,7.545336,-6.634446,-2.765068,1.261733,5.313047,-9.442618,-0.908454,-2.205604,7.350157], dtype = "float32")#candidate|8135|(2288,)|const|float32
call_8134 = relay.TupleGetItem(func_2795_call(relay.reshape(const_8135.astype('float32'), [11, 13, 16])), 2)
call_8136 = relay.TupleGetItem(func_2798_call(relay.reshape(const_8135.astype('float32'), [11, 13, 16])), 2)
output = relay.Tuple([call_8046,call_8082,call_8085,bop_8108,call_8121,call_8132,call_8134,const_8135,])
output2 = relay.Tuple([call_8047,call_8083,call_8086,bop_8111,call_8122,call_8133,call_8136,const_8135,])
func_8137 = relay.Function([], output)
mod['func_8137'] = func_8137
mod = relay.transform.InferType()(mod)
output = func_8137()
func_8138 = relay.Function([], output)
mutated_mod['func_8138'] = func_8138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6773_call = mod.get_global_var('func_6773')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_8141 = func_6773_call()
call_8142 = func_6773_call()
output = call_8141
output2 = call_8142
func_8151 = relay.Function([], output)
mod['func_8151'] = func_8151
mod = relay.transform.InferType()(mod)
output = func_8151()
func_8152 = relay.Function([], output)
mutated_mod['func_8152'] = func_8152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7824_call = mod.get_global_var('func_7824')
func_7826_call = mutated_mod.get_global_var('func_7826')
call_8197 = relay.TupleGetItem(func_7824_call(), 0)
call_8198 = relay.TupleGetItem(func_7826_call(), 0)
output = relay.Tuple([call_8197,])
output2 = relay.Tuple([call_8198,])
func_8199 = relay.Function([], output)
mod['func_8199'] = func_8199
mod = relay.transform.InferType()(mod)
mutated_mod['func_8199'] = func_8199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8199_call = mutated_mod.get_global_var('func_8199')
call_8200 = func_8199_call()
output = call_8200
func_8201 = relay.Function([], output)
mutated_mod['func_8201'] = func_8201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6580_call = mod.get_global_var('func_6580')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_8323 = relay.TupleGetItem(func_6580_call(), 0)
call_8324 = relay.TupleGetItem(func_6581_call(), 0)
func_5936_call = mod.get_global_var('func_5936')
func_5938_call = mutated_mod.get_global_var('func_5938')
call_8335 = relay.TupleGetItem(func_5936_call(), 0)
call_8336 = relay.TupleGetItem(func_5938_call(), 0)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
const_8351 = relay.const([7.838779,-0.700006,-8.256384,0.769820,-0.928896,-5.042496,-6.499955,6.436057,7.274071,-5.359294,8.760770,-7.772571,-1.390085,-3.938268,-2.018839,-1.888482,-3.463009,-0.910092,4.558761,-6.434772,-4.232445,-5.664052,1.614074,7.170390,8.095883,5.187742,-2.960428,3.995235,9.989991,0.496045,5.123417,7.014395,-6.867670,-4.381493,2.127143,4.554855,-4.156567,8.833152,-5.025812,-3.196397,-5.686026,-2.614005,-4.887268,8.180519,0.077094,8.582396,-8.388193,-8.964982,9.230995,-0.863531,3.194373,-8.996782,9.853286,-6.118901,-3.150548,4.458279,-3.807775,6.228497,8.291810,-4.123606,1.163035,-7.082945,-1.293384,-1.694815,4.185994,-4.545972,6.715200,-2.813152,-6.833182,-6.899800,-5.818690,-8.164007,4.902901,1.699012,-4.152651,3.492202,6.847300,-7.661930,4.099714,2.552146,6.437767,6.621311,-6.932902,-3.080247,-7.674096,3.634589,-8.007673,3.757004,-4.127139,1.453969,-5.338897,-8.650426,-0.968967,2.927184,-8.033085,-4.278418,4.808318,-1.714913,-8.758357,-2.040247,9.876316,7.883010,4.176428,5.295783,3.908145,9.659642,1.818706,4.948433,-6.889794,1.044962,-8.680556,-3.241967,-4.517609,9.225438,9.798090,1.332793,-3.924732,9.564354,-4.970823,7.790777,7.008421,7.034884,-7.416889,-1.012578,-9.719328,7.104560,5.696660,-2.740291,-1.371836,-9.223104,0.177709,-6.697918,-2.538353,-5.748490,-3.004037,-0.477801,-1.730525,7.225604,7.390150,4.199518,8.408938,-1.052257,-8.825964,-3.641239,-8.258543,4.490044,7.700539,1.921860,4.314214,-1.586352,9.010405,2.576452,-4.128399,0.351026,-0.970104,5.170943,1.504669,-5.083509,-3.231106,8.444670,-6.623047,7.222084,-8.768179,1.261009,-4.716833,-6.211669,5.470759,1.943790,-3.892868,1.335062,0.455706,-4.661387,-0.286607,-8.161080,-8.967223,4.651405,-0.861788,-8.632186,-4.615121,-5.833525,8.483147,-1.807208,-2.389564,-6.567539,-9.850102,6.700870,4.159915,7.983262,6.131661,-8.275690,9.459368,-0.682242,-8.282117,-3.721029,-1.241253,2.563261,1.530370,-4.970744,9.610908,-8.739563,-3.392341,4.681687,-9.907726,5.856703,7.135927,9.660781,-2.960948,-3.249388,-1.870952,9.145745,-7.503550,-3.875364,-3.990447,6.946434,2.221967,-1.171120,-8.407723,2.888103,-2.145009,-0.448095,5.558457,-8.156352,7.218411,-5.466068,8.269840,-6.467956,7.900580,-7.332160,-8.711793,2.516448,3.185055,5.751328,-0.230093,-1.708947,-8.249791,-6.577305,-1.559878,2.804226,9.860385,3.519071,8.433911,-4.706102,-6.610691,-1.665349,6.413965,3.028303,3.512186,-0.360142,7.205865,-9.846604,5.676727,0.416505,4.628084,8.436543,7.443731,-5.180573,-3.335788,6.559142,6.748141,2.176928,4.164454,8.565620,-8.167445,-1.072112,4.490415,7.027467,5.587423,-5.862397,7.862179,-6.764298,7.931571,3.138071,6.874675,-8.148046,-9.957093,6.396650,-0.015297,2.960757,-1.349238,2.595624,-9.506996,-1.187628,5.881386,6.459262,-9.659747,7.503624,-0.979258,-3.540401,7.973540,-3.797190,-6.534480,-8.745177,-6.433400,5.908782,2.681113,-5.389119,9.977202,-6.629012,-6.925133,8.820544,5.363045,-6.012949,3.823150,5.949775,8.764422,7.387463,-0.802898,7.524485,0.605796,4.527148,9.147159,-3.115702,3.868122,6.172737,-8.928880,-1.388829,-4.417726,8.614727,0.203186,-7.854333,-2.030465,7.562286,4.360696,-1.965770,7.587962,-0.576060,8.210586,-4.693107,8.690866,-9.378389,-4.374459,4.789215,6.599306,6.367472,3.355768,-4.987011,8.486204,-2.533426,-9.925737,2.678691,4.549159,-4.296997,-5.585729,5.109729,-1.108941,-3.362655,-1.723823,5.572126,-1.915318,5.597606,5.522087,-0.677047,1.505007,2.385039,1.538900,5.821885,-3.987406,1.149962,-2.775120,-1.870382,5.303696,-4.422305,-0.142625,5.791584,-4.239330,7.881319,-7.701105,-0.862711,-2.191903,6.183974,-0.709882,-3.453882,-7.901296,9.503072,-7.750690,-3.620885,-2.612883,-7.706848,-3.915279,-0.205637,-8.285934,-9.829893,2.736412,-7.449523,6.957164,4.935366,-3.167828,-6.117539,2.173901,-7.650799,-2.129771,8.660593,8.133587,8.398599,-6.670855,-2.242423,9.164589,1.438266,3.130317,4.879323,-8.276468,-2.422198,-6.048486,2.899047,-7.412817,-9.581720,-6.088547,-8.044483,6.055816,-1.156129,3.517881,-9.277140,4.902744,8.432674,8.307646,4.181962,3.353297,-0.217389,9.986408,2.294031,8.798047,-1.608203,-7.392229,4.732245,-7.840298,7.595298,-4.581024,4.217086,1.637185,-5.189605,2.492938,-3.463333,7.083916,-6.474530,1.481490,5.793745,1.351919,-1.483781,-6.983124,2.214233,9.690845,-3.929580,-4.679751,-0.109502,-6.089687,-5.738140,-9.435793,-0.959936,-1.159221,-7.662490,-1.440243,-7.405796,5.268665,0.047848,7.473500,3.893593,1.620934,-2.137816,5.742050,-1.689989,-2.070959,7.374385], dtype = "float32")#candidate|8351|(462,)|const|float32
call_8350 = func_1356_call(relay.reshape(const_8351.astype('float32'), [6, 11, 7]), relay.reshape(const_8351.astype('float32'), [6, 11, 7]), )
call_8352 = func_1356_call(relay.reshape(const_8351.astype('float32'), [6, 11, 7]), relay.reshape(const_8351.astype('float32'), [6, 11, 7]), )
func_299_call = mod.get_global_var('func_299')
func_301_call = mutated_mod.get_global_var('func_301')
var_8357 = relay.var("var_8357", dtype = "float64", shape = (2, 40))#candidate|8357|(2, 40)|var|float64
call_8356 = relay.TupleGetItem(func_299_call(relay.reshape(var_8357.astype('float64'), [10, 8, 1])), 0)
call_8358 = relay.TupleGetItem(func_301_call(relay.reshape(var_8357.astype('float64'), [10, 8, 1])), 0)
func_2669_call = mod.get_global_var('func_2669')
func_2674_call = mutated_mod.get_global_var('func_2674')
const_8360 = relay.const([-7.571350,3.003056,-5.748183,7.704918,-3.941711,-8.275686,-0.976641,9.118912,-4.331070,-5.887765,5.967806,5.821952,7.016023,-5.985075,1.822732,4.082841,0.265989,-6.591801,8.304405,-5.384156,-3.649250,8.692986,2.091138,0.037021,-7.950591,-7.695323,-4.804199,-7.880115,0.485033,-2.747163,9.570751,2.692320,-3.612988,-7.464378,2.447435,4.799448,9.785991,-9.399677,-7.360241,-8.881849,9.729481,-5.131299,9.352186,1.959346,9.542009,5.384172,0.797596,0.970714,-1.944595,-3.039353,7.001809,2.942971,-7.132882,7.522742,-1.166944,4.908452,-4.910464,6.270580,-9.167239,3.770302,-2.861702,1.565210,2.700080,0.823582,-4.047574,1.806881,9.718683,0.788894,-3.920591,-8.409882,-5.358500,-7.962158,1.654223,-0.026760,9.951045,-1.668253,0.646536,9.546114,-3.817631,-0.899216,-6.186057,-8.317635,2.887040,9.211985,-9.158769,-6.308060,1.258321,-3.253399,-0.431633,5.751938,-9.773812,7.959601,5.192554,-1.134842,3.764751,-4.165231,-0.085232,4.802672,-6.431410,7.877799,4.113137,-5.989718,-8.835111,0.331806,3.947883,-5.285805,-3.877110,0.383563,7.141107,-3.043003,8.865962,-4.697969,7.714475,8.449198,5.632118,1.368857,-1.312510,6.205125,-2.880415,6.533799], dtype = "float32")#candidate|8360|(120,)|const|float32
const_8361 = relay.const([9.091232,8.118361,-9.936118,0.404345,4.522702,3.723224,4.762381,-2.056499,6.424809,1.388691,5.021088,-1.387955,-2.017818,-7.049021,-4.368097,6.908712,-5.967618,-4.639134,-6.322067,-6.491985,4.565490,7.002169,-4.855801,2.837491,3.921739,4.009361,-1.346277,-1.519969,7.144502,-7.307990,-3.986425,3.679345,1.108313,8.996664,4.790034,9.223980,2.695409,-5.422666,-4.303535,8.787811,-5.598522,5.297545,-4.864057,1.474783,-5.282098,4.225929,-0.141547,5.600594,-8.833272,9.408952,9.046076,9.433537,2.714657,-3.336509,9.839847,8.838395,0.804785,-0.193959,-8.154810,8.991537,-7.965269,3.979285,-4.059241,-4.117655,9.012867,-8.818347,-4.450476,2.677914,1.995946,0.874110,1.632926,0.004001,9.833452,4.794653,2.982327,-2.627117,5.327084,-2.695545,3.986208,0.876657,2.457353,6.786841,7.234444,6.840611,-7.377052,5.130622,-7.666652,-3.156023,1.037411,2.287122,6.910957,-2.334490,-9.450791,-7.757230,3.679440,-9.436412,8.674395,-2.239209,2.528432,-2.735321,-3.315612,9.336233,-0.741704,9.529862,8.707136,-6.823046,-8.614039,-1.427931,-7.195907,-9.663173,-7.909739,-3.422945,-7.300530,-8.830624,-5.415055,-7.475386,-1.114514,7.088016,4.081007,-1.774942,-4.702018,5.905886,4.357393,0.266636,-7.597816,7.481638,-5.091206,8.654458,-7.471547,-6.125741,-0.011353,-3.614928,1.743064,9.587788,-1.038471,7.464557,-8.711736,2.084912,-9.625746,1.199025,1.202732,6.669106,-8.451819,-2.206731,-8.036368,-0.294927,9.200614,-6.816776,-6.313700,-5.290931,0.613944,0.746241,-7.967751,-2.346683,4.387709,-5.436371,-8.531601,5.899618,-0.349212,-8.241979,-3.436714,9.144370,5.853880,-0.102004,2.484430,-3.119964,8.216779,-4.410819,-7.881382,-0.663287,6.734619,-0.791604,2.883871,-0.518486,-3.700397,-9.379566,8.328105,-9.349770,8.011466,1.531676,2.737204,-7.801071,7.221519,2.151241,2.939774,-9.026124,-6.374149,-6.093072,-4.520170,9.186311,3.925523,0.051472,0.511042,5.383814,7.270626,8.179666,-0.004552,9.784788,-9.536025,-0.720606,-3.972232,-5.686115,1.203815,-3.069878,-9.342755,-7.947185,-5.509936,-3.100542,-1.407447,-7.419431,-2.739772,-2.126373,4.210296,6.601003,-1.888680,5.497832,-7.131404,0.809437,5.841989,1.667201,4.042178,5.912130,2.696740,5.257250,-6.443939,5.539764,3.670942,2.670118,1.213482,8.145932,-2.099165,4.041518,-7.140324,4.653063,-3.568430,6.842282,-4.011421,7.540586,6.721422,2.425336,3.790317,-9.617034,3.178182,4.783089,-4.932318,-5.091669,-5.755078,5.915725,3.699191,-4.614358,7.911485,1.276386,-5.526358,-8.830370,-3.398675,3.715087,-3.901475,-1.644993,-7.533727,2.820852,-2.868802,0.918401,6.573003,-0.641674,1.822628,-6.929681,-9.249562,0.549101,3.417539,-8.579578,9.805642,4.145522,-1.396236,2.900361,3.104626,1.823620,5.313827,-2.664545,-6.096664,1.889634,7.035050,-4.332203,1.745394,0.278444,1.415478,-7.825279,7.147082,8.277518,-8.862534,-7.942573,3.069262,2.809281,6.693811,8.692412,-0.236302,9.198603,-1.122142,-9.278740,5.600716,-5.886808,2.000672,-6.157720,-8.346811,-7.266137,-0.449433,7.783774,4.432005,-5.668511,-7.689584,-2.188405,-7.454257,7.903942,8.853580,2.658098,9.348694,-3.952290,-3.043383,9.523545,-6.552259,8.465848,7.017446,-7.126551,-7.238048,2.272959,-2.587869,7.684475,3.263449,5.195751,-0.982176,-0.190245,2.709354,0.766462,4.295669,-1.716368,-9.969610,-3.150257,-7.300780,-0.040535,-2.013803,-1.720740,9.551003,3.218684,-0.915285,-7.600658,4.129523,-7.607905,3.727443,8.159970,-2.031906,-0.943276,3.378605,-1.276834,0.870639,-1.115572,-3.509297,-7.443577,0.537942,0.224304,-7.065071,-0.001623,-2.385438,-3.144369,-2.863509,-9.257206,-2.349986,-4.773848,7.046926,4.356421,8.906200,-3.919413,-2.966092,-1.606354,9.228862,5.896070,3.769471,0.898330,-5.454679,1.762272,2.452842,-4.639359,-4.094235,-7.057951,0.888578,-9.435857,9.912675,4.146719,7.172575,9.863668,5.373337,-3.702237,1.049852,-2.955075,-9.838549,-8.268308,6.401939,4.609477,5.227862,3.550107,2.513882,-0.042676,5.388102,6.776106,0.587008,1.725697,3.242689,3.066143,2.812615,4.109490,5.358422,-4.686869,-0.964782,-2.323396,2.517308,-2.670742,4.801178,4.637140,-4.603982,6.793114,-1.260698,-0.467066,-0.938402,-3.756138,5.075257,2.750803,5.376225,7.712431,6.106614,-2.793025,-9.184690,-1.279522,3.504948,-9.978673,-7.098594,8.398527,-5.341269,-3.646305,2.610287,-9.966216,-9.178642,1.947237,3.725089,6.701069,-5.376662,0.886448,0.666182,-7.917788,-1.889978,-5.182635,-3.300200,0.263882,-0.042844,2.606696,-4.434275,-3.127748,-0.059697,-9.460876,7.520790,-7.622599,2.742771,-9.235988,3.987901,8.944015,7.248900,-2.403780,1.679802,-2.674164,-2.691213,6.539330,5.047055,4.539772,0.066567,-2.578010,-9.302501,-1.858436,-7.723997,-5.651859,7.640084,4.948253,2.976901,-2.897668,3.672994,-0.880502,4.262638,-9.518823,-0.347505,-5.816058,-3.559188,-4.590419,1.265010,-3.338574,9.743274,-5.740088,8.085075,1.589650,9.541547,1.667072,-7.078859,-8.033574,-6.566780,-3.043819,8.463347,-3.261748,3.167977,-1.221808,-6.417006,7.459336,2.331831,-4.287555,2.143930,7.839652,-1.492852,-2.033915,4.289777,-0.142516,1.160895,-1.154739,0.418899,-7.458486,6.447273,8.408109,-0.601941,9.164304,-5.102098,-3.234562,5.858853,4.613638,-6.843693,-5.426493,-6.617563,4.138379,8.868269,-4.867844,3.769268,-3.435030,2.377595,-8.175863,-3.535981,7.368874,5.619113,-0.040929,-5.184768,-9.583819,8.228169,-8.809488,9.001603,-0.223290,6.217905,2.245435,6.352613,2.272862,-7.951826,-9.679208,8.115405,1.390601,7.438393,6.167465,0.352724,2.478485,-9.761744,1.482429,1.115901,-0.863025,-9.139780,2.405407,4.515565,7.999927,-1.622016,-6.886101,3.966776,1.300414,-7.000415,-5.596776,-6.062293,-0.973701,4.385286,2.370816,0.577374,1.257102,3.418949,-8.114558,8.654599,-6.210728,4.804305,6.452633,6.569633,-8.576780,9.764299,7.989857,-0.258753,-0.265417,0.659594,-3.255498,-8.818233,2.428682,0.445801,-1.542493,8.474019,-7.128446,-0.902234,1.525272,-3.404125,5.569359,8.236112,-8.098430,-6.716670,6.385058,-3.221294,3.693647,-0.294179,-5.974090,-6.741305,-1.405854,-0.246529,-6.935355,8.050921,-3.044721,2.068528,7.519301,-1.256439,-3.959173,3.615510,7.975314,-1.771582,-3.222998,6.739974,-7.468824,2.403093,5.321640,0.547566,-9.011824,7.475166,1.642063,-3.653282,8.854977,-9.205068,-6.248054,-4.352395,7.393627,-7.059436,4.488530,-0.519176,9.831981,-5.524704,9.374865,-1.110779,-9.364962,-7.752297,0.872458,5.107573,-4.513920,-7.124457,3.333710,-6.182956,0.008414,-5.211215,-4.660573,-1.356074,-4.132793,-0.655076,2.545524,-3.513505,-6.515685,6.444681,3.792436,2.754285,-9.377938,-0.333506,-0.428895,-9.090136,7.572604,-5.569782,5.908024,1.809143,9.198994,-1.098601,6.291222,9.853822,6.626707,6.170947,3.544033,-7.526894,-9.111444,2.486385,1.253125,3.252558,-9.674649,-6.792583,-4.669436,3.423540,9.798766,-1.579430,-3.544236,2.207810,-0.595935,9.154380,0.855163,7.176715,-8.839592,-9.544830,-3.671745,0.072325,3.291440,5.854885,0.823585,1.669146,-0.134982,9.182196,8.223566,-3.304142,9.063241,2.702959,-2.100063,3.733129,1.296378,-7.725905,5.962613,-6.960112,-0.613840,-3.452143,6.190858,-9.092584,-7.980663,-4.662001,-0.407843,4.733577,-5.393213,-6.687351,-8.524617,-8.707411,6.204898,4.347331,-3.177950,1.491942,3.892735,-1.526731,-4.195793,-5.265287,2.611138,-6.151666,-9.361468,3.293732,8.172274,5.048371,5.595787,0.384552,-6.962691,8.646106,5.661639,0.379893,3.642625,5.503227,7.932324,-0.791728,-9.999571,-0.377327,-2.866775,-9.961149,-4.633298,2.611865,0.999578,-1.890342,-8.007916,-3.045949,4.543540,-8.711244,8.507658,-7.952383,-2.716473,4.752189,9.210273,3.632431,-9.319961,7.318473,3.928871,-9.034300,-4.697438,-6.099135,0.030614,-9.183531,6.932370,0.976759,-4.003357,1.446376,-5.482281,5.758176,-2.783690,2.023013,-6.174416,6.727918,-8.498150,-2.829834,7.416468,4.608170,6.253287,5.566308,-8.665143,-4.216888,-7.337474,1.263788,-4.249403,-4.082766,2.871813,3.204530,4.790722,0.019116,6.876611,-1.241136,0.692305,0.010377,7.044733,9.682136,1.349214,-3.711890,3.395471,-0.253998,-5.050159,-2.542824,-2.351850,-8.369322,2.678714,7.160814,9.461246,2.915120,9.893832,-5.485102,6.903296,8.202743,9.542196,-5.238765,5.973900,-0.834901,2.048819,-5.412008,1.221924,1.945233,-9.276757,1.708898,-5.131563,-0.859402,1.370755,-8.382270,-6.555075,5.800722,7.794402,-6.381410,-3.503939,7.526737,-9.157410,8.911198,-6.501519,-6.145599,-6.589509,-6.927196,-0.427973,-9.594589,9.382678,-0.974800,-0.974374,1.391285,6.889735,9.876401,5.799603,5.986099,-2.739690,2.503077,-7.626290,4.632315,6.207855,4.416810,7.677895,1.831157,0.943435,-8.113599,7.223399,6.059434,-1.973457,-2.815419,3.299768,1.850000,-8.256715,-1.959685,-1.868673,8.065696,-1.979431,0.234869,4.472277,-9.161996,-9.676208,-4.480755,7.031611,-3.216303,-3.820172,1.257658,-8.975420,8.904398,0.074124,5.047108,-1.224459,0.430914,-8.736698,-7.849076,4.810389,-4.391226,4.210011,8.611190,-5.030356,-6.927711,-6.100037,2.882441,-4.248463,9.365355,-8.814436,3.732014,-8.855594,9.612314,6.908341,-2.900144,8.219042,-0.349272,4.724969,1.292437,6.638308,1.817344,2.953558,1.917631,1.582549,2.936406,0.725824,-7.914409,5.537765,-3.346270,5.035589,1.819371,1.496578,-7.356004,4.818077,6.601151,6.956367,-9.249762,3.861731,3.474744,-7.491143,-6.404106,4.460902,5.755004,8.831063,-1.990447,-1.319568,1.044138,8.335874,9.545884,9.130333,-1.648684,6.986221,9.212434,-7.440422,0.291272,7.530975,-4.520345,1.813601,9.785080,-0.636712,1.027768,9.500465,-7.485623,-1.351045,5.581452,-9.610537,3.759508,-4.877925,-9.306764,3.268127,0.791051,-7.118033,3.241964,-1.380179,-3.133730,-5.602473,0.284393,-1.126783,4.509404,4.864371,-3.227557,-7.756191,7.141858,-3.523768,0.729281,-8.838265,-6.779088,-3.483829,-3.862640,-9.607186,9.786886,-9.711355,-7.912688,5.878646,-3.995521,-2.531914,-3.211844,-9.793028,3.698305,-8.601967,-1.602564,1.846851,9.477347,-8.878290,-3.467720,-0.373826,-9.012493,1.941710,4.801135,-6.530141,5.230308,-4.083199,3.957110,-4.535733,0.601523,8.459636,6.694941,-7.510599,-8.820116,-7.801180,2.238898,5.642651,6.935548,-5.181828,0.952761,-3.959620,6.995656,-0.062607,0.164163,6.767668,3.649357,-5.931480,0.530125,9.550731,-4.369582,4.243075,-2.519865,6.674631,9.204458,-9.124912,-2.719614,0.324207,6.436193,-8.010883,-2.401206,3.798113,-0.409147,-2.947498,-4.818138,9.412140,9.189329,-9.205430,2.634167,-9.997343,5.878503,0.944311,9.935910,6.454032,1.996388,-7.171578,9.134529,6.772997,6.756461,-9.756785,-2.461409,-7.766176,-5.735489,0.449073,-5.170469,-1.840472,1.467781,1.960118,-1.160717,9.356625,-3.913096,-0.981199,-0.219964,0.777041,6.577675,8.900985,-0.307371,-1.032545,2.603337,-5.925072,6.372308,6.780994,9.787741,0.719934,-6.876240,2.545686,-7.115859,-3.430980,2.864117,7.051398,1.606428,-3.542585,-8.112666,-1.086054,4.430441,-3.443391,8.709569,2.268269,-3.001429,5.415663,9.077303,-7.504603,-5.968097,-0.129465,-8.557200,-4.983040,0.665389,5.201260,3.404526,8.412341,6.151934,7.867596,9.665667,3.484482,-1.147477,-0.415085,6.958636,4.850211,-9.122395,1.481706,2.002850,-1.710203,7.874871,4.852515,-6.451132,0.960601,-5.302904,-3.566152,4.212026,7.382499,-8.524254,7.783262,-0.081159,4.830869,6.244006,-4.232345,3.925388,5.844692,-7.189380,5.051212,8.313325,-2.553897,-4.087890,7.384255,-0.217970,5.039705,4.688622,-5.963794,2.805867,-5.338903,8.945626,-1.295950,7.800451,8.453159,-8.942866,-6.730076,6.461013,5.357973,-8.676396,0.377413,3.563448,1.808218,8.511583,8.986765,-7.731328,6.722184,-9.338898,-7.172918,1.198532,3.590845,-6.512089,2.953290,2.667873,5.447978,-7.392271,-0.870544,1.656639,-3.298172,-5.555304,-8.731522,6.823072,-3.436718,8.557413,2.030523,-8.386316,-3.582876,6.188962,-6.093711,-6.332610,-8.263719,-3.711069,-3.128435,-3.856047,-2.340915,-3.966989,6.282521,4.414242,8.199326,-3.624868,8.879811,-0.592877,-0.627114,-7.395184,-7.782952,-6.764496,7.670711,5.570873,1.328243,-8.117262,-1.762516,-3.405544,-4.807107,4.565106,-3.665825,-9.644907,-6.745084,3.818980,-8.489413,4.253055,-3.815686,7.197276,-1.445500,6.996889,3.232358,-6.585949,4.426564,3.069235,-5.585668,1.434125,8.948803,-4.449370,-2.745876,-4.901022,6.974922,7.380623,2.010993,9.311338,-6.259706,5.019056,-7.559395,3.358722,-7.413190,5.195064,-3.566372,6.828392,2.085292,9.351817,1.072180,-9.516029,-2.454883,-0.505932,2.656001,8.949385,5.910496,7.836861,-4.972715,8.411016,6.666904,4.304528,6.773930,5.647356,8.243031,9.940824,-3.861091,8.244019,8.400657,9.645528,-7.897411,-0.931070,8.412754,0.456241,6.070031,3.346347,-4.837318,-7.989041,3.029460,-0.582903,-5.177788,-7.542950,4.180370,5.139027,2.730924,3.254940,-1.743273,3.466826,9.690881,7.516483,3.167802,-7.877597,-3.367177,-4.184790,-4.145303,-5.870919,-1.385145,-2.558841,-7.593894,-9.984943,-8.681804,3.680688,-5.536300,-8.636025,-4.980722,-0.462622,-9.205134,9.414312,0.020864,0.229655,-0.341538,-2.939330,-3.583436,-5.727729,4.398411,-2.775413,2.507857,-3.212891,9.598019,7.423442,-0.854185,7.469392,-6.663213,2.746309,-4.614377,-8.918846,-9.977636,4.305374,7.025816,-6.663122,3.280544,-8.609065,-3.749407,-1.891996,7.483702,3.707117,1.410444,9.368561,7.533666,3.410762,6.867392,-4.774343,-0.636101,-1.437870,-3.178259,-8.279869,6.588573,-7.517779,4.890258,6.692044,-5.226385,1.655331,-2.093679,-7.924964,0.817745,1.280420,0.397025,4.733914,-4.076945,1.633480,-0.380481,-1.185085,-3.064752,7.618356,7.560640,-8.983684,-2.038673,2.757480,-2.193310,-1.443592,8.118885,-3.536509,-3.488186,-8.276650,6.703611,2.237224,-4.219377,-1.670633,-5.774696,-5.060377,-5.597940,6.874972,-5.931730,0.275167,-1.828496,2.524501,-9.696410,-0.976226,4.469456,2.307321,-7.213764,-2.242809,-8.042442,8.526294,-0.900336,-9.118859,8.335869,1.729862,-2.355251,-9.026050,2.343040,-8.942676,-1.404508,-5.523445,4.874830,-5.563986,-9.946069,-8.698361,1.580748,3.902942,-9.839752,1.512537,5.196269,8.822956,7.208130,5.779918,1.361590,-3.436394,-7.623112,9.532136,-3.873790,-0.383093,-3.240755,9.091334,-8.546634,-1.156590,-3.640239,-8.958146,-6.182959,1.628609,-7.919789,-8.809191,-8.951074,6.306016,4.779885,7.314140,-5.833770,-4.420914,-6.099603,7.748685,-3.794978,8.763287,8.120427,9.582244,-1.711746,3.327853,8.839564,-8.050861,7.939093,-5.398145,1.343073,-3.298919,8.679425,-8.159715,8.138991,1.432157,8.370847,-3.030615,-7.769608,3.450621,5.482172,3.484221,-1.895350,-9.943801,9.993671,4.320519,-9.326646,3.779916,-8.147750,-7.493323,8.143713,-3.973506,-7.437589,7.731496,-5.267705,0.369202,1.788672,-1.929290,9.345763,7.213377,6.795362,5.595960,8.823087,-8.021938,-8.390726,3.082965,-9.180174,5.168692,-9.255661,9.785202,0.282232,-8.569594,-2.967469,-3.656751,-0.759634,-2.820028,-5.364333,7.444979,-7.007805,-2.659459,-3.580363,-7.834382,6.368705,-0.448592,-3.109526,-7.253976,-3.711942,9.717653,6.679429,-5.577785,3.081411,4.811952,-9.311577,1.796190,-6.171939,-7.617910,0.646405,3.344846,-0.300857,2.177289,-1.921791,-8.214531,-6.785736,3.417456,3.154470,7.892772,-3.554238,9.887065,-0.720447,-8.292707,-0.753557,2.758494,6.220082,-6.662046,-1.622949,3.312544,9.138821,-7.126933,0.927978,4.010918,2.118279,4.726997,6.220304,5.999243,-9.288547,3.609212,-7.017875,-8.185900,4.180332,6.759634,-3.483402,-9.007821,-7.177989,-6.652280,-0.803404,-9.772369,-7.829643,-3.410184,-7.339746,4.290219,2.594163,1.654797,-7.401396,5.173365,-6.052002,1.662798,1.749844,-1.894398,-1.641466,4.895077,-4.680332,0.806975,-3.644503,8.712204,7.487669,1.136194,4.603900,-9.044813,-0.704662,4.864480,-7.619258,-8.324942,5.208174,3.739511,8.504190,-0.401639,-0.017503,-2.446178,1.554317,-8.026377,4.899647,1.282297,-1.688442,-7.207375,-5.428238,-8.968109,-9.206637,-8.838335,1.297234,-9.665130,3.584412,8.422380,-0.807120,-1.060157,6.117004,-6.623905,-2.679501,6.391852,9.089640,9.844739,6.862230,-1.771932,-0.788566,8.599494,-9.249325,-1.314724,2.117079,2.915050,-4.949252,2.491612,-5.471967,-7.580326,-6.799193,-2.731088,4.798739,9.433597,2.649983,-7.805694,-4.642927,8.870859,3.006388,-8.272858,2.139018,-6.380218,8.665170,6.080704,4.584525,-0.143473,0.010020,1.559905,1.263757,-4.420612,-1.573343,-1.300267,-7.643241,0.499070,-0.591139,-9.916899,-0.534118,4.535169,3.645542,4.962457,-8.817378,-5.032547,-6.590290,-3.466809,-7.150559,-8.883197,5.086942,1.810932,9.785027,-5.965618,2.188993,4.245667,4.482814,2.730676,-3.175515,-0.168501,7.384923,-7.559380,-9.892149,2.508101,9.267913,-1.424079,-7.273815,6.372247,-2.546528,3.946841,-9.649938,6.269577,7.228270,-8.914747,-6.911656,-3.078830,9.138089,1.593298,0.972266,-3.481481,6.751781,-5.229020,1.492144,5.682712,3.212666,8.369880,8.587387,7.274324,2.709390,-0.273830,-4.865868,8.706559,-5.484426,-2.499729,4.662739,-6.811192,9.813477,7.467894,-0.269022,-6.514077,6.335872,-4.690371,3.408098,-9.086289,9.542566,-0.232177,0.939858,-0.223093,-0.134805,-7.527681,5.253118,-8.497598,7.261716,0.973787,-7.307157,8.532534,0.731871,6.295678,9.972559,-4.358275,-1.688185,8.717099,-0.854821,5.718569,-4.081018,8.036851,4.937587,-1.297903,3.018356,-2.674446,7.349437,3.058688,8.991873,6.284836,-6.272082,-1.382055,-8.219213,8.544574,1.557604,-6.375883,-2.181357,6.609321,6.440627,-5.390031,-5.709253,0.883886,-9.438193,-3.101237,0.428701,-8.191552,4.555252,-8.451779,-8.599953,0.273643,4.521728,2.530226,0.999223,9.912339,-7.822887,1.769126,-9.223468,6.390679,2.327356,5.709273,6.734770,7.805907,-4.298450,8.150624,5.989431,-4.275346,-7.584705,-7.269795,-7.573719,-1.372690,3.409672,5.368592,-9.332383,-1.654564,7.360283,-9.722283,5.353187,3.039449,-6.628358,8.386433,4.514173,-3.909728,2.166732,7.099329,-3.944664], dtype = "float32")#candidate|8361|(1800,)|const|float32
const_8362 = relay.const([4.618084,8.233789,-6.007030,3.047103,8.800590,-7.386115,-4.749898,6.539878,-8.765191,6.126836,-6.732141,4.582029,7.639413,-3.838760,3.335861,1.898472,2.943618,-1.057837,6.780288,5.277281,-6.768657,-3.710032,-9.562498,-1.749738,-8.104779,7.336412,6.976334,4.222393,-7.751327,9.654031,7.784666,-7.960742,2.421642,-2.772977,9.565936,9.867505,1.292984,-2.529890,-5.244483,-0.348433,7.782691,2.733680,-2.051158,0.906853,-0.396611,-3.075937,1.694591,1.130488,8.924066,-7.205278,4.379513,9.535938,2.023705,-5.385589,-5.319398,-5.998587,-1.145963,-2.263990,-5.587489,7.279867,-8.772408,8.948683,-1.181436,-5.692832,-1.271278,-6.651861,6.714015,2.322478,-3.012770,-4.876062,-9.111546,-4.341195,-9.126257,-0.388010,-8.442332,-0.429910,1.135732,-4.654067,-1.912516,-3.758040,8.538754,-1.616650,-7.424517,1.782497,9.264336,8.531238,5.009147,-5.094430,4.424730,-1.166185,-3.916676,-7.916369,-1.788907,0.764000,-2.392298,-0.475726,6.059137,-9.790640,-8.970046,-5.674347,0.608316,1.584130,5.768308,-5.618476,-3.492386,-7.918914,5.434701,2.605713,2.232740,-9.201327,-3.289170,-7.866593,0.231952,7.507445,-0.217627,7.443366,1.420683,-4.012856,-5.780390,2.844256,-1.639963,4.313797,3.092131,2.560444,-6.893128,-6.564404,-9.780395,-9.831891,3.572849,4.628920,2.680888,1.280954,-2.929179,9.698781,-6.984965,5.297219,-4.172891,5.275178,4.342516,-3.052230,-3.343566,-7.458266,9.981915,9.489923,-6.893639,7.606401,3.203498,9.479084,-8.093693,8.017832,7.921781,8.233943,0.303990,6.042902,-9.443380,-2.346077,-3.752524,1.201104,3.346054,-9.745095,-1.418524,7.167888,-3.697629,7.777997,3.172977,-4.999921,3.843095,-8.243634,-8.959623,-0.350813,-3.052688,6.113934,1.625730,-2.300872,7.905617,5.869072,-4.176076,-1.110240,1.625629,-3.027063,-4.478354,3.660390,-7.876825,-6.812707,-6.147863,4.723951,-0.764617,9.039941,-0.352457,-2.104408,3.399789,5.067840,3.773662,-7.545880,8.191881,0.983686,6.311024,3.492081,3.813932,-0.924723,-0.711307,-6.290117,1.021830,0.545329,4.117856,7.023454,3.762805,1.294827,-9.690880,7.512527,-4.598218,4.043305,7.259531,6.477716,7.116242,-2.204803,-6.514975,-8.776622,5.183933,4.279901,0.729305,9.270778,8.741428,7.765857,-0.394367,3.031833,-1.368665,2.056668,1.304006,-5.750802,-6.944805,2.043702,5.674456,-8.213434,9.900917,6.414759,7.109432,8.873979,3.618643,-6.805682,0.865039,-3.948595,7.837333,1.528090,6.504221,1.486786,8.124296,-2.052707,-6.324864,3.629748,-4.597012,-8.832444,6.131277,-9.541935,2.320044,-7.052826,-3.423831,-4.564613,-7.364177,-8.270982,1.981247,-2.514231,-7.206972,3.410307,7.446834,-3.488074,0.935947,7.236762,-4.585969,-9.224408,7.865651,-8.985897,9.691162,9.049172,9.895192,5.838582,4.183058,3.579128,-4.691476,-8.382727,1.149834,0.521908,2.588936,7.523336,-7.542559,8.963708,-4.857126,6.172404,-8.709739,-6.621328,2.878937,-2.054826,4.775993,-0.918247,-3.786085,7.868131,-7.138170,9.882261,-3.352838,4.261092,-0.529845,-1.998928,6.230813,-7.430176,-5.827358,9.814316,1.004865,-4.308150,9.897494,-6.021534,4.008273,8.150589,3.761067,7.204017,9.237838,-2.320724,-6.164958,-6.834001,1.669478,9.878175,1.938820,1.327975,6.133519,4.727307,-5.027024,-3.226492,-2.464912,0.728157,-8.660426,2.391819,-2.667818,4.469723,-7.061922,-3.479133,4.650326,0.934620,-8.775529,0.641665,-1.540793,-9.698514,-9.850670,-4.933490,-7.239020,-6.125722,-5.897014,-1.697435,-3.872186,7.360142,8.850358,-7.287274,-0.859777,-1.106631,-8.534983,-8.785077,-3.066390,7.195357,3.138455,2.331968,-6.929318,1.535494,7.524666,0.419831,8.314894,-3.825194,-4.334997,2.654549,-7.922362,5.449480,1.367515,2.373498,-8.932354,8.791158,-5.231018,6.130012,-1.239512,-2.116659,-3.573695,7.380704,-9.525260,-2.223948,-4.556931,0.408402,4.125619,8.524688,-1.592792,3.760644,-5.994992,8.539461,9.800601,0.952996], dtype = "float32")#candidate|8362|(390,)|const|float32
call_8359 = relay.TupleGetItem(func_2669_call(relay.reshape(const_8360.astype('float32'), [1, 10, 12]), relay.reshape(const_8361.astype('float32'), [15, 10, 12]), relay.reshape(const_8362.astype('float32'), [195, 2]), ), 5)
call_8363 = relay.TupleGetItem(func_2674_call(relay.reshape(const_8360.astype('float32'), [1, 10, 12]), relay.reshape(const_8361.astype('float32'), [15, 10, 12]), relay.reshape(const_8362.astype('float32'), [195, 2]), ), 5)
bop_8367 = relay.floor_divide(var_8357.astype('float32'), relay.reshape(call_8356.astype('float32'), relay.shape_of(var_8357))) # shape=(2, 40)
bop_8370 = relay.floor_divide(var_8357.astype('float32'), relay.reshape(call_8358.astype('float32'), relay.shape_of(var_8357))) # shape=(2, 40)
bop_8399 = relay.logical_and(call_8359.astype('bool'), relay.reshape(const_8362.astype('bool'), relay.shape_of(call_8359))) # shape=(2, 15, 13)
bop_8402 = relay.logical_and(call_8363.astype('bool'), relay.reshape(const_8362.astype('bool'), relay.shape_of(call_8363))) # shape=(2, 15, 13)
func_1492_call = mod.get_global_var('func_1492')
func_1495_call = mutated_mod.get_global_var('func_1495')
const_8404 = relay.const([[9,-6],[-3,1],[6,9],[-8,-9],[3,2],[6,7],[5,-3],[-1,-2],[7,9],[6,5],[9,-5],[6,-9],[-7,8],[4,-1],[-7,5],[-9,8],[-4,4],[-8,-1],[-5,-3],[10,4],[2,5],[7,9],[2,4],[3,-5],[-1,-9],[2,-6],[-6,-1],[-1,-6],[-7,3],[6,-2],[7,10],[-9,7],[8,9],[-5,8],[-5,10],[2,-1],[8,6],[5,4],[3,-10],[-1,-2],[-4,-8],[7,-2],[2,6],[-9,-6],[-10,-3],[-8,7],[-1,4],[5,-10],[9,9],[3,-6],[-3,-3],[-1,1],[9,8],[-1,1],[-1,5],[-2,-6],[4,-7],[-9,5],[7,-6],[7,2],[1,5],[5,5],[2,-4],[6,7],[9,8],[7,10],[1,2],[5,-4],[-8,-10],[7,-10],[5,5],[-8,-1],[6,-3],[-5,7],[-2,4],[7,-6],[6,-7],[-1,-4],[-3,-10],[-1,5],[2,-10],[-2,-3],[-10,-2],[4,1],[3,-5],[-4,-3],[-7,-5],[-7,8],[8,-6],[-7,-5],[-7,-3],[4,-3],[1,-3],[8,-10],[-10,3],[-5,7],[-9,6],[-6,-4],[-9,-6],[-2,-9]], dtype = "uint8")#candidate|8404|(100, 2)|const|uint8
call_8403 = relay.TupleGetItem(func_1492_call(relay.reshape(const_8404.astype('uint8'), [4, 10, 5])), 0)
call_8405 = relay.TupleGetItem(func_1495_call(relay.reshape(const_8404.astype('uint8'), [4, 10, 5])), 0)
bop_8407 = relay.bitwise_xor(call_8335.astype('uint32'), call_8356.astype('uint32')) # shape=(10, 8, 660)
bop_8410 = relay.bitwise_xor(call_8336.astype('uint32'), call_8358.astype('uint32')) # shape=(10, 8, 660)
var_8414 = relay.var("var_8414", dtype = "float32", shape = (2, 40))#candidate|8414|(2, 40)|var|float32
bop_8415 = relay.add(bop_8367.astype('int32'), relay.reshape(var_8414.astype('int32'), relay.shape_of(bop_8367))) # shape=(2, 40)
bop_8418 = relay.add(bop_8370.astype('int32'), relay.reshape(var_8414.astype('int32'), relay.shape_of(bop_8370))) # shape=(2, 40)
const_8427 = relay.const([[3.674320,-7.144102,8.289762,9.565323,7.070303,9.179795,-1.703577,6.411293,6.104792,7.231854,-0.896963,8.202871,7.632302,-7.669793,6.840058,-6.761662,-8.076875,9.662663,1.455619,7.374561,3.335589,-9.601307,4.650227,-6.753287,9.674169,-3.447608,-0.769945,0.307112,2.959360,-5.487459,0.581505,2.881018,-6.170291,3.159753,8.160424,-7.618191,0.959706,3.186621,-7.157971,-2.372574],[4.457828,1.566012,-3.147462,5.807267,-6.387125,-9.567716,-7.285810,-3.742625,-4.667761,3.083958,-6.894020,1.571217,-6.396121,-6.409143,-6.123999,1.158845,6.226741,4.910404,6.742297,-8.467620,7.685007,4.666212,-1.252660,-6.291423,9.364015,8.908019,3.031642,1.146032,8.718656,-1.415158,-7.619287,6.547638,0.854824,-6.782009,2.935767,-4.868078,1.697062,6.484284,2.526149,2.721623]], dtype = "float32")#candidate|8427|(2, 40)|const|float32
bop_8428 = relay.mod(bop_8367.astype('float64'), relay.reshape(const_8427.astype('float64'), relay.shape_of(bop_8367))) # shape=(2, 40)
bop_8431 = relay.mod(bop_8370.astype('float64'), relay.reshape(const_8427.astype('float64'), relay.shape_of(bop_8370))) # shape=(2, 40)
const_8466 = relay.const([[2.616636,8.096744,-8.100553,8.726487,-3.220128,1.803620,-5.895586,1.174656,-0.206419,-6.739228,-1.029921,4.977583,1.315512,-7.391889,-5.239873,0.505783,-9.354736,-5.164332,4.192831,-9.243925,8.060082,-1.603174,9.689303,-0.350332,-8.933219,5.059518,0.610947,6.741637,8.093447,-3.470506,2.505686,8.775699,-6.212003,-9.988314,-1.303738,-8.684665,-7.038627,9.933078,-0.403512,9.333920],[9.323866,8.190726,-7.961019,7.044260,-4.054750,9.957808,4.784235,9.259058,1.118216,1.789918,5.265125,9.118768,-7.894665,7.033177,-9.078900,5.543318,9.029225,-8.873590,3.900594,1.378393,-2.835447,9.830331,-2.105048,8.323446,-2.770645,8.377318,-0.740379,-6.284321,4.626933,2.954392,-7.648299,7.723331,7.995453,5.270627,2.467249,-3.479238,-5.366101,7.289125,4.288209,-2.060665]], dtype = "float64")#candidate|8466|(2, 40)|const|float64
bop_8467 = relay.floor_mod(bop_8428.astype('float32'), relay.reshape(const_8466.astype('float32'), relay.shape_of(bop_8428))) # shape=(2, 40)
bop_8470 = relay.floor_mod(bop_8431.astype('float32'), relay.reshape(const_8466.astype('float32'), relay.shape_of(bop_8431))) # shape=(2, 40)
const_8475 = relay.const([[[-3.896814,-7.513805,-5.407418,-6.954316,-6.189427,-0.364073,-9.913595,4.165901,5.846856,-1.982644,-4.455133,4.825290,-8.147349],[6.941652,-0.518746,3.057222,8.516861,-3.542992,0.275826,-8.456676,7.828872,-6.860805,-2.512983,7.096711,3.988377,5.376102],[-6.362001,-3.216467,-4.949496,-8.951294,-4.832857,1.690603,0.126605,-6.716606,-3.466182,-2.644484,6.118677,7.838908,2.023295],[0.152935,-4.416700,-5.110324,0.406245,9.195009,-1.100282,-0.441041,-9.120425,-5.300607,2.742803,-0.974727,-3.152226,-0.160230],[7.998214,0.870226,-4.941629,2.603111,0.693161,-9.719619,4.695276,-3.241028,8.991649,-0.118669,-3.731280,-4.354296,6.955881],[8.133722,7.051590,7.461146,3.425661,8.023254,-3.558536,-4.253921,-7.368140,-9.605165,2.822548,0.691552,-9.858780,-4.035857],[1.069291,-0.203202,9.226861,-6.030540,4.390206,-3.056046,-4.110383,0.025971,-8.832531,-4.917540,-8.570685,-4.705573,7.981593],[-7.549222,-3.785359,-7.147310,8.731933,-2.970922,-8.998651,-1.765055,9.238825,-6.702054,-0.825518,-5.953316,0.235618,-8.556895],[9.946461,4.924511,-7.924192,-8.132629,-2.795916,-6.363886,-1.745580,6.198038,3.720782,-6.406110,-9.395498,-0.569661,-6.858012],[4.234427,1.523569,0.782632,4.349547,0.991466,0.930399,-7.959640,-0.774032,6.517420,5.358758,7.670523,-1.485911,5.542391],[-2.353484,-4.081796,-3.947800,5.766717,3.780565,7.722870,6.801357,-7.663651,-6.503437,1.507005,-4.397904,4.294922,6.622986],[-8.625762,5.282868,-5.355974,-6.801658,-8.965148,-0.132265,-0.051484,1.981147,-0.240967,1.038746,2.688297,8.309113,-6.477022],[7.646815,-6.506641,6.635358,8.887909,-9.207702,-9.132620,-0.794831,-5.395753,-4.103612,-0.496335,-6.779689,2.624974,7.101242],[1.822036,9.480116,-3.879438,-3.510288,1.851841,-6.547139,-9.799406,-2.127748,9.003862,5.335863,6.262495,-4.714902,6.410845],[3.543917,-1.784200,5.687783,6.822870,-8.839205,-1.875913,-2.269429,-1.724215,-6.477105,-6.788164,4.756940,5.934252,4.735306]],[[8.563378,-2.349837,-5.470110,7.279425,-6.871835,-0.880476,3.628954,-2.019961,5.995320,5.996188,1.385217,-2.271442,-3.721506],[1.669532,4.808145,-8.704496,-5.307828,4.259979,-1.586372,-8.382842,-8.216520,9.011014,8.340727,0.017952,-8.154941,-6.587094],[-2.647098,0.299500,-9.502003,-8.967120,8.689666,-0.825617,5.457825,-5.933392,-9.759998,-3.585912,-9.402825,-0.767042,9.468034],[-9.563860,-4.389218,8.441342,-6.187853,1.758190,2.205961,-9.264488,3.889189,1.556517,-7.197352,-2.529245,-4.771138,1.683346],[-0.913673,-8.928097,8.803913,-2.919005,1.704250,-5.710814,-8.458805,-9.531796,1.473424,3.018838,-3.527385,6.256116,-4.777278],[5.296080,9.551267,9.872952,8.246060,2.164561,2.667823,-1.834245,-7.269442,-5.652666,0.527140,-8.307680,2.145528,6.373513],[-0.504403,-2.248964,-5.654887,1.612312,2.499167,-1.487253,-5.411679,9.270372,8.642069,-6.789723,5.118951,-5.393219,-5.044841],[8.950909,-5.393270,0.415626,-0.610710,-8.742565,0.686142,-9.306001,-7.284221,5.727346,-1.170138,-9.711428,4.805452,3.753588],[2.383639,4.263959,0.535114,0.117724,0.787131,-8.173038,7.656380,-6.171249,8.807881,8.922305,0.324836,-2.809362,7.757221],[6.397936,-6.588110,5.191473,7.705971,6.821224,-3.387392,-6.876344,2.230722,3.715987,2.264965,6.737380,-2.034953,7.768062],[-5.092843,1.818378,-7.918544,-4.771002,-5.513579,5.791621,-7.091728,-1.740464,1.104493,-6.355588,3.978734,3.100767,5.401927],[1.444432,8.285299,-9.339966,9.302509,-8.143073,-4.489954,-1.232621,-2.513854,-8.778098,-2.776210,2.068891,-6.040417,-1.336817],[9.442140,-1.484173,-7.209315,-0.765544,-4.408973,5.729973,9.113501,-0.390247,-5.817385,-3.343306,-2.909751,8.575009,5.326809],[-4.816570,-0.880380,9.678757,5.456559,1.721060,-0.978266,7.095504,-8.366107,-7.479406,-7.191284,5.508106,8.771690,-8.960138],[4.351850,-9.958827,-3.606793,-7.766387,6.321594,7.160467,2.992259,-9.758838,-2.733397,3.690435,8.503412,-8.702666,-3.805300]]], dtype = "float32")#candidate|8475|(2, 15, 13)|const|float32
bop_8476 = relay.greater_equal(call_8359.astype('bool'), relay.reshape(const_8475.astype('bool'), relay.shape_of(call_8359))) # shape=(2, 15, 13)
bop_8479 = relay.greater_equal(call_8363.astype('bool'), relay.reshape(const_8475.astype('bool'), relay.shape_of(call_8363))) # shape=(2, 15, 13)
func_4874_call = mod.get_global_var('func_4874')
func_4877_call = mutated_mod.get_global_var('func_4877')
const_8482 = relay.const([-4,-6,-1,3,9,9,-8,-1,-2,-2,-4,-5,-3,3,10,5,-7,2,-1,9,4,6,-3,-9,-2,7,5,8,8,5,-1,1,-1,-6,-5,-6,3,1,9,-2,-10,-8,-3,-4,8,-9,2,-7,-3,7,7,9,5,7,-1,-4,-10,-7,-9,-5,10,7,6,-7,6,8,-5,-3,-10,-4,-9,-1,5,3,-9,-2,-2,3,1,-8,-1,-10,7,1,-4,-8,5,2,-9,3,-3,9,4,-5,1,1,2,-2,-5,-6,-8,-1,-6,-3,10,-3,3,-10,3,1,1,-5,3,3,8,6,8,9,10,10,-9,3,-4,-8,-10,-10,1,5,-3,-4,2,7,5,5,-9,5,8,2,1,-1,-9,2,-6,-5,-9,-8,-9,2,-2,-9,-4,10,2,-5,4,-6,7,-4,-6,10,10,-8,-6,2,9,-10,8,6,4,5,-9,10,8,9,-2,1,8,10,-2,-1,-4,6,10,1,3,-3,-6,8,-6,-8,-5,-2,-10,6,-3,-5,-7,8,-2,3,-5,-8,9,5,-3,4,3,1,-8,-5,4,-9,-2,-8,8,-2,8,-5,7,2,4,8,-4,3,7,-5,10,2,1,-6,3,-3,7,-8,8,4,6,1,4,1,2,4,10,-3,8,-1,7,-4,3,-1,-3,-5,9,-10,8,6,-7,-3,6,9,7,-7,-5,-1,4,-9,8,-6,10,2,7,-9,8,-3,-9,-10,-4,3,9,-10,-7,-10,5,-2,3,-4,-1,7,6,-4,2,-1,1,10,1,3,-10,-3,-10,-9,-10,-3,5,-8,10,6,-8,-2,5,8,-1,4,-3,-8,1,-6,-2,1,9,-10,3,-4,-5,9,8,5,-8,5,-5,4,4,-8,9,6,9,10,4,-5,10,-10,-1,8,-2,-1,-7,5,-3,8,10,-3,-1,-5,6,-3,-3,-3,-8,4,-5,8,-9,1,-4,5,2,5,10,-8,9,1,4,8,8,-3,6,4,4,7,-6,-4,-10,-2,8,-9,1,10,-5,-9,-10,-5,-4,10,-6,-4,9,1,-6,4,-2,4,2,-1,2,-9,2,7,-4,-2,5,-1,5,-6,4,8,2,9,5,10,-10,8,-4,6,3,8,-5,2,10,2,9,-2,-1,4,1,-3,-2,10,5,4,5,4,1,-1,-6,-7,-2,-6,9,9,4,10,-3,4,8,6,9,5,-7,-5,9,8,2,-4,-3,-1,-7,5,-1,7,-6,-5,6,9,4,8,5,-5,-1,-7,4,-3,9,10,-4,1,4,9,6,5,9,5,3,-10,-1,-9,7,7,-8,7,-7,-6,-6,3,2,-2,-3,-4,9,1,4,-8,-1,-8,5,5,-6,3,5,-4,3,-7,-4,-5,8,4,5,3,-8,-7,6,5,2,-4,3,5,3,-6,-4,2,6,-3,10,1,5,-3,9,-1,-5,1,2,-7,9,-3,-6,-4,-3,-7,3,2,-3,8,-4,-6,-5,-8,2,-3,-1,-3,-5,1,-6,-2,-4,4,1,3,1,4,-6,-3,2,-1,-4,9,-3,-7,9,-5,-6,-2,3,4,-5,-9,3,-9,-10,7,7,5,-8,-1,4,2,7,8,-1,3,1,7,6,8,-8,-9,-2,-7,7,-9,-3,2,7,9,10,-4], dtype = "int64")#candidate|8482|(624,)|const|int64
call_8481 = relay.TupleGetItem(func_4874_call(relay.reshape(const_8482.astype('int64'), [24, 26])), 0)
call_8483 = relay.TupleGetItem(func_4877_call(relay.reshape(const_8482.astype('int64'), [24, 26])), 0)
uop_8487 = relay.log(bop_8367.astype('float64')) # shape=(2, 40)
uop_8489 = relay.log(bop_8370.astype('float64')) # shape=(2, 40)
output = relay.Tuple([call_8323,call_8350,const_8351,const_8360,const_8361,bop_8399,call_8403,const_8404,bop_8407,bop_8415,bop_8467,bop_8476,call_8481,const_8482,uop_8487,])
output2 = relay.Tuple([call_8324,call_8352,const_8351,const_8360,const_8361,bop_8402,call_8405,const_8404,bop_8410,bop_8418,bop_8470,bop_8479,call_8483,const_8482,uop_8489,])
func_8496 = relay.Function([var_8357,var_8414,], output)
mod['func_8496'] = func_8496
mod = relay.transform.InferType()(mod)
var_8497 = relay.var("var_8497", dtype = "float64", shape = (2, 40))#candidate|8497|(2, 40)|var|float64
var_8498 = relay.var("var_8498", dtype = "float32", shape = (2, 40))#candidate|8498|(2, 40)|var|float32
output = func_8496(var_8497,var_8498,)
func_8499 = relay.Function([var_8497,var_8498,], output)
mutated_mod['func_8499'] = func_8499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_8516 = relay.TupleGetItem(func_4770_call(), 4)
call_8517 = relay.TupleGetItem(func_4772_call(), 4)
output = call_8516
output2 = call_8517
func_8547 = relay.Function([], output)
mod['func_8547'] = func_8547
mod = relay.transform.InferType()(mod)
output = func_8547()
func_8548 = relay.Function([], output)
mutated_mod['func_8548'] = func_8548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_8592 = relay.TupleGetItem(func_4821_call(), 0)
call_8593 = relay.TupleGetItem(func_4822_call(), 0)
output = relay.Tuple([call_8592,])
output2 = relay.Tuple([call_8593,])
func_8594 = relay.Function([], output)
mod['func_8594'] = func_8594
mod = relay.transform.InferType()(mod)
output = func_8594()
func_8595 = relay.Function([], output)
mutated_mod['func_8595'] = func_8595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8594_call = mod.get_global_var('func_8594')
func_8595_call = mutated_mod.get_global_var('func_8595')
call_8622 = relay.TupleGetItem(func_8594_call(), 0)
call_8623 = relay.TupleGetItem(func_8595_call(), 0)
func_5303_call = mod.get_global_var('func_5303')
func_5305_call = mutated_mod.get_global_var('func_5305')
call_8631 = relay.TupleGetItem(func_5303_call(), 0)
call_8632 = relay.TupleGetItem(func_5305_call(), 0)
func_7824_call = mod.get_global_var('func_7824')
func_7826_call = mutated_mod.get_global_var('func_7826')
call_8636 = relay.TupleGetItem(func_7824_call(), 0)
call_8637 = relay.TupleGetItem(func_7826_call(), 0)
output = relay.Tuple([call_8622,call_8631,call_8636,])
output2 = relay.Tuple([call_8623,call_8632,call_8637,])
func_8650 = relay.Function([], output)
mod['func_8650'] = func_8650
mod = relay.transform.InferType()(mod)
mutated_mod['func_8650'] = func_8650
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8650_call = mutated_mod.get_global_var('func_8650')
call_8651 = func_8650_call()
output = call_8651
func_8652 = relay.Function([], output)
mutated_mod['func_8652'] = func_8652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_8686 = relay.TupleGetItem(func_5333_call(), 0)
call_8687 = relay.TupleGetItem(func_5334_call(), 0)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
const_8734 = relay.const([-9.956424,2.556161,-7.330154,-1.915629,2.545121,7.393081,-2.945844,-3.729924,-4.092916,7.339993,-5.065520,-7.598255,8.513899,3.054753,-4.673184,9.018654,5.653285,-4.905708,8.973891,4.667941,-7.319033,-9.186207,-0.833001,8.742161,-7.897829,-1.376022,-0.050129,-3.670013,-9.605907,-9.792584,-1.602459,-3.925528,-7.138649,2.960552,7.823149,-2.287104,-7.043111,-6.320413,7.647463,0.864021,-1.038932,1.005202,-3.531347,9.149623,0.139102,-9.025008,5.290908,4.636334,0.628272,6.696100,5.391821,-7.326480,-2.006222,-3.238471,6.330770,-3.596305,0.625607,-6.332677,4.342987,8.219806,7.976113,-7.697804,-3.837941,-6.665028,3.970922,-2.067073,7.118543,-3.977279,-9.324818,-9.230386,-9.254835,4.129748,-5.556189,-7.138532,1.239111,-9.721355,9.253879,-6.377951,-6.130647,5.346649,-7.465782,-2.715440,-5.387320,-6.632758,-9.693905,-1.978541,2.361692,-4.237144,6.324135,8.018948,-4.728294,3.637176,5.643329,8.218512,-0.364699,6.130835,6.274961,5.864795,-8.439326,-0.510318,-4.119198,3.494235,-7.817505,7.577176,-0.284263,8.845304,-7.361409,-3.291400,-5.301523,3.012790,-4.934528,0.220448,-3.043562,-4.737009,-3.384429,9.830319,2.484541,-7.731883,6.793146,-3.932011,5.578607,-0.798658,-5.033743,7.011779,2.235128,-9.737185,8.699052,8.893700,-0.221789,-0.527352,-8.511222,6.054685,-0.571780,7.541741,9.470383,-3.804914,0.980289,-4.803288,5.930331,-9.328101,-4.410218,8.324431,9.389589,9.048874,-1.693382,-5.865845,-9.264859,-9.522411,-6.551039,-9.239227,2.309040,-9.569519,0.220082,7.310133,-7.010383,8.910894,-3.275445,-8.423853,9.159151,5.062817,2.319154,-3.209752,5.582903,-9.675157,3.781306,4.849477,0.041739,8.198728,-6.402446,-4.191141,2.290741,1.890663,-1.564840,0.294124,1.071884,1.276792,-8.279243,-4.192019,-0.365030,5.245850,2.379750,5.714175,-4.087836,-3.215715,5.953017,1.262651,-6.508250,-3.543835,-1.147416,7.896004,-3.473200,-0.538847,-8.522848,-7.766898,-8.343502,-1.113099,-6.915735,-7.758576,1.408645,9.150856,9.129790,8.139491,0.938963,-3.811715,1.826875,6.184087,-7.369153,-4.395986,9.452406,-7.532131,0.210257,8.356676,-7.738694,-2.150890,-7.666425,-0.562934,1.465683,-2.841257,2.988738,-2.153126,-5.079420,-2.128412,-6.851022,7.782730,8.261225,3.143097,8.176518,-1.082948,-2.150991,1.863559,-5.414316,9.598123,9.797723,-1.215805,-8.699159,3.492164,-7.918076,-5.029111,-3.795217,-1.624145,8.137824,-3.685988,3.268535,-9.777547,-1.778292,-6.533239,6.715947,-2.235734,9.510244,6.572757,1.051947,-5.667170,-0.553117,-0.265630,0.021119,-7.530722,-7.867402,3.227751,2.410468,-5.889968,3.207597,-7.162330,-7.641811,7.048074,0.989913,2.205279,7.478391,-4.424037,-4.781207,-8.370752,-3.228152,-0.330094,-4.842228,-1.629429,7.582437,5.564551,8.523628,9.910927,-6.985361,-0.424863,3.336091,-7.851675,8.515734,-3.025841,-3.689510,8.348674,3.001468,3.172834,5.802500,3.237530,-2.742238,3.696434,-0.277759,4.676265,1.078560,-8.345742,-4.513043,6.086735,-2.941652,9.199242,4.605296,5.685583,0.521592,-6.361095,-5.142090,1.773637,-6.545800,-2.622766,-5.015569,9.844776,8.989067,-6.825959,-8.265691,-4.895453,-7.988030,3.830618,-4.561973,-5.909194,-9.276855,7.926479,8.396022,6.715662,4.342403,-7.935597,-1.481209,-4.153240,-0.797052,5.758416,-0.990076,9.616623,4.182801,-2.745570,9.543359,8.557921,1.219306,-1.667258,-5.652464,-5.275983,7.498854,9.508279,-8.769506,-9.815787,-1.090936,-6.231401,4.065499,6.696919,-8.544976,-0.084190,5.293097,5.985556,-9.853077,5.299630,-3.083420,7.302076,-1.644037,3.300693,-9.536201,6.120986,3.926624,7.316954,8.318769,4.689847,3.957274,4.024223,-9.692425,9.071793,-8.480129,5.571524,7.693196,2.562912,4.973706,-0.263719,-8.987341,-6.675384,2.625916,-0.065965,9.315348,5.468186,3.148954,1.356133,1.343142,9.459460,7.504706,-4.375099,3.577242,-2.732740,-7.800349,-6.988178,1.068801,-6.639079,-5.475240,1.131589,0.307708,-5.019316,-8.088208,-9.334369,0.937711,9.251104,-2.674821,2.995931,9.029831,-4.269431,-3.457346,-1.243061,0.169124,1.395113,0.648939,3.414267,2.256795,-7.632827,6.203404,4.571509,-9.228111,1.251000,4.713127,-1.916979,7.750689,-4.075921,8.612851,7.864234,-5.535189,-1.221784,7.622720,-9.242374,-2.930059,-0.547284,5.060347,-8.767759,9.164287,-2.041912,-8.511183,7.871841,8.051082,1.056920,8.623289,6.996049,9.246911,4.530452,-4.996702,8.524026,-9.021248,-7.514913,-7.518407,5.942861,3.521902,-5.193221,-5.992609,4.408405,3.205293,-4.962223,7.512811,-9.351508,-3.958480,7.502418,4.493535,0.483163,8.062158,9.122670,-4.432526,8.585136,-4.900485,3.321278], dtype = "float32")#candidate|8734|(462,)|const|float32
call_8733 = func_1356_call(relay.reshape(const_8734.astype('float32'), [6, 11, 7]), relay.reshape(const_8734.astype('float32'), [6, 11, 7]), )
call_8735 = func_1356_call(relay.reshape(const_8734.astype('float32'), [6, 11, 7]), relay.reshape(const_8734.astype('float32'), [6, 11, 7]), )
output = relay.Tuple([call_8686,call_8733,const_8734,])
output2 = relay.Tuple([call_8687,call_8735,const_8734,])
func_8741 = relay.Function([], output)
mod['func_8741'] = func_8741
mod = relay.transform.InferType()(mod)
output = func_8741()
func_8742 = relay.Function([], output)
mutated_mod['func_8742'] = func_8742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8741_call = mod.get_global_var('func_8741')
func_8742_call = mutated_mod.get_global_var('func_8742')
call_8751 = relay.TupleGetItem(func_8741_call(), 1)
call_8752 = relay.TupleGetItem(func_8742_call(), 1)
func_7329_call = mod.get_global_var('func_7329')
func_7334_call = mutated_mod.get_global_var('func_7334')
var_8754 = relay.var("var_8754", dtype = "float32", shape = (56,))#candidate|8754|(56,)|var|float32
var_8755 = relay.var("var_8755", dtype = "float32", shape = (5, 78))#candidate|8755|(5, 78)|var|float32
const_8756 = relay.const([-8.059728,0.925325,-5.372023,1.766521,3.028892,2.281975,-5.622879,-4.749042,-4.875351,3.125847,-7.360951,2.897191,-8.562214,-1.430556,-4.683049,9.831322,-2.467979,2.603510,0.369982,-8.507409,7.905226,-2.094051,-2.774659,-0.402376,8.213983,-7.445690,4.930140,-0.185871,1.602714,-9.066755,2.419346,-3.207388,-0.813717,-1.767171,-7.853154], dtype = "float32")#candidate|8756|(35,)|const|float32
call_8753 = relay.TupleGetItem(func_7329_call(relay.reshape(var_8754.astype('float32'), [4, 1, 14]), relay.reshape(var_8755.astype('float32'), [390,]), relay.reshape(const_8756.astype('float32'), [7, 5]), ), 5)
call_8757 = relay.TupleGetItem(func_7334_call(relay.reshape(var_8754.astype('float32'), [4, 1, 14]), relay.reshape(var_8755.astype('float32'), [390,]), relay.reshape(const_8756.astype('float32'), [7, 5]), ), 5)
func_5067_call = mod.get_global_var('func_5067')
func_5072_call = mutated_mod.get_global_var('func_5072')
const_8773 = relay.const([5.815553,7.532337,-9.634059,-6.498056,-5.980186,-0.272147,3.217237,9.128052,-7.181203,2.142879,7.751022,5.372509,7.127327,7.789186,-0.199424,-7.568776,0.360328,-2.386200,-5.139807,7.947596,0.394147,0.664190,-5.021264,4.604739,2.988438,-3.366056,-0.658876,3.441611,7.488861,-8.850875,4.823693,2.395675,-7.893884,-0.582321,5.450753,3.192233,1.370128,0.265350,-7.441128,-5.455905,-1.530077,-3.252894,2.473626,-2.227183,-8.667440,-8.067207,-3.055019,7.995342,3.238251,2.499095,7.546574,8.284217,3.674815,-6.693245,-8.437581,4.192140,5.091869,7.105838,6.126780,5.581307,-0.939983,5.877741,-2.831421,5.459034,-2.893949,-0.130956,9.558533,-8.826105,-9.228013,-4.252890,9.861228,1.634137,-0.947112,0.784375,7.696826,0.111358,-4.911246,-5.456910,7.874940,-2.591655,-9.210698,2.901851,5.914100,-3.582008,-4.810349,-2.873377,-6.225431,-1.715169,-5.073523,-7.613633,7.221349,2.104532,-5.840005,-7.086119,2.008505,1.874272,1.166108,1.017359,-2.608760,-8.956692,5.086556,-5.974077,1.780550,-3.190405,5.312999,6.339912,-6.867305,-8.330540,-2.541822,1.919600,-1.097681,4.117743,1.664606,-2.071905,-5.977824,1.391364,9.355947,5.914015,-3.888523,-2.736459,-0.492173,-4.074171,-7.990693,6.019765,5.469347,-6.986988,1.834724,6.592385,-8.588330,-8.171560,7.970398,-8.764791,4.785001,1.515416,7.873026,5.171888,3.656182,0.153302,9.655119,-9.100735,3.016230,-5.740750,-3.869994,3.955868,5.337071,8.387015,3.284397,9.862581,6.314241,1.054993,-8.786134,-7.066668,-6.342136,8.727795,-6.849318,4.045074,-5.447879,-3.708683,9.742133,6.167406,1.633199,4.381964,0.382644,9.205497,7.413478,2.083320,-0.074822,2.207021,5.436498,-6.669224,-2.376174,1.839368,5.749270,9.190518,-6.441460,0.021843,8.999204,-3.430276,1.733288,1.288734], dtype = "float64")#candidate|8773|(180,)|const|float64
call_8772 = relay.TupleGetItem(func_5067_call(relay.reshape(call_8751.astype('float32'), [462,]), relay.reshape(const_8773.astype('float64'), [180,]), relay.reshape(call_8753.astype('float32'), [35, 1]), ), 0)
call_8774 = relay.TupleGetItem(func_5072_call(relay.reshape(call_8751.astype('float32'), [462,]), relay.reshape(const_8773.astype('float64'), [180,]), relay.reshape(call_8753.astype('float32'), [35, 1]), ), 0)
uop_8782 = relay.sin(var_8755.astype('float64')) # shape=(5, 78)
output = relay.Tuple([call_8751,call_8753,var_8754,const_8756,call_8772,const_8773,uop_8782,])
output2 = relay.Tuple([call_8752,call_8757,var_8754,const_8756,call_8774,const_8773,uop_8782,])
func_8788 = relay.Function([var_8754,var_8755,], output)
mod['func_8788'] = func_8788
mod = relay.transform.InferType()(mod)
mutated_mod['func_8788'] = func_8788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8788_call = mutated_mod.get_global_var('func_8788')
var_8790 = relay.var("var_8790", dtype = "float32", shape = (56,))#candidate|8790|(56,)|var|float32
var_8791 = relay.var("var_8791", dtype = "float32", shape = (5, 78))#candidate|8791|(5, 78)|var|float32
call_8789 = func_8788_call(var_8790,var_8791,)
output = call_8789
func_8792 = relay.Function([var_8790,var_8791,], output)
mutated_mod['func_8792'] = func_8792
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8854 = relay.const([[[6.173822],[1.290039],[9.762763],[4.811326],[-3.339085],[-6.609957],[-7.118724],[-9.247273],[-6.200842],[0.677076],[2.587162],[3.685217]],[[9.224094],[-5.600067],[5.643076],[3.906766],[-1.670763],[-1.418596],[3.150367],[-6.951122],[6.175048],[-3.231207],[-7.840721],[-2.047063]],[[-0.550347],[-6.980848],[2.633533],[-9.189686],[2.615588],[-8.796253],[-1.688092],[5.794407],[-7.294739],[4.410581],[0.707562],[9.518069]],[[-3.164839],[-7.717046],[-7.599881],[2.896182],[-4.282480],[-4.856324],[9.353691],[4.767193],[-4.220876],[-8.748821],[8.332078],[0.916088]],[[0.753352],[-3.149655],[7.042086],[8.879076],[3.097655],[-1.895161],[-1.133923],[8.373600],[1.462743],[1.940840],[-9.924770],[-4.395405]],[[-8.070651],[0.072354],[-2.278058],[1.875590],[7.995087],[9.972658],[2.943348],[6.557677],[-3.767311],[-7.335012],[6.257282],[-5.482445]]], dtype = "float64")#candidate|8854|(6, 12, 1)|const|float64
uop_8855 = relay.log(const_8854.astype('float64')) # shape=(6, 12, 1)
output = uop_8855
output2 = uop_8855
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
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_8924 = relay.TupleGetItem(func_5036_call(), 0)
call_8925 = relay.TupleGetItem(func_5037_call(), 0)
func_4649_call = mod.get_global_var('func_4649')
func_4653_call = mutated_mod.get_global_var('func_4653')
const_8954 = relay.const([5.137640,-9.300276,-0.509722,-0.107310,2.953362,-0.580660,6.774973,-3.531844,4.760624,8.277409,7.327247,-5.971801,3.608318,-2.098007,6.947833,9.325020,-4.189503,6.988619,7.315790,3.551337,-6.461324,-7.265657,-4.730172,-9.957963,-0.189482,-9.456788,6.702572,-9.041015,-3.821464,-4.557809,6.631416,-5.515731,3.101948,-7.099415,-8.365397,0.417326,-2.328831,-8.089944,-3.154961,-3.665063,0.504517,-2.065156,1.434727,2.862990,-6.147800,-3.421269,0.810422,3.917819,-9.696125,2.946203,5.490796,6.443205,1.831582,-8.726128,-4.499673,-7.770096,5.109036,5.792750,5.785492,-5.462782,-1.731927,2.165541,5.752967,-4.575335,4.695361,-9.657809,-9.343359,-4.327524,-2.787906,0.483531,4.762306,-1.983570,4.182490,3.545682,-1.218676,-5.174366,-3.830957,6.568069,-6.206247,-3.085889,0.717606,-4.604507,-4.473178,0.965079,6.207703,-4.778732,-7.877070,6.671458,-5.123386,9.799136,-4.470018,4.622018,3.605301,-1.213603,-7.983263,0.399999,-7.542838,0.777343,-9.557897,1.142329,7.196067,-5.687909,-2.193285,5.583248,0.058406,7.862811,-0.736795,-3.295066,0.886623,9.846993,7.089704,-7.960273,-1.403098,3.591069,-7.287530,-7.180144,-1.080755,-3.014835,-2.714952,2.404296,-0.614935,6.897159,5.201954,-3.260487,8.607640,-1.057631,0.916144,-4.451343,-7.646660,-4.031284,-6.291903,-0.914626,-0.778581,7.488729,0.470927,-4.772707,4.196071,-9.529343,0.991060,-8.964912,1.742566,-8.112305,3.969503,-3.207046,-9.038223,-3.435961,-2.828817,5.014373,0.607803,0.019976,5.790566,-7.365239,-6.343789,2.862731,-2.347057,-6.118579,-7.108043,-5.354481,0.113761,1.244075,0.205552,-3.632271,-1.578751,-5.695500,-0.038673,-1.865330,9.874092,-2.664550,-4.737857,-2.984851,2.751646,-6.626086,6.495417,9.406889,1.233239,-9.666814,9.841277,-8.555192,-0.915431,7.933539,2.645437,-0.060474,3.739748,-8.704114,-1.301499,-2.010484,3.834097,6.649204,4.257737,3.748501,6.880715,0.185405,-0.807026,-1.662865,0.908654,7.322059,-7.541349,8.256832,-3.019604,9.128604,-7.139048,3.005416,-7.011135,-7.045498,1.229647,-4.111869,8.837567,4.664671,-1.223570,-2.000683,-6.600265,-2.104367,7.738201,-9.860414,7.679095,-2.803366,8.201179,1.488250,-4.260543,5.902086,3.345593,-2.858819,3.962428,-4.802703,-7.973242,6.853800,-4.061880,5.306757,-5.216498,8.633690,9.711066,2.545502,3.262739,-2.086825,8.194605,-7.876954,8.390098,4.919544,-0.181475,-0.618723,9.978741,9.785870,5.301310,5.355952,-0.146430,2.026763,0.731391,-8.151275,0.370141,-2.845669,-0.821876,0.809700,-6.247795,6.177535,-1.712779,5.569757,9.829434,0.929464,3.185543,-1.454525,-6.111054,4.840656,2.059584,-2.625415,-7.663563,0.019378,5.275086,-4.798087,9.003152,3.446411,-1.732076,6.654075,3.176769,-3.408312,-5.211536,4.107700,4.045624,-5.214239,-6.473317,5.320030,8.186175,-6.764579,-4.594497,-7.105090,-9.925012,5.765516,-8.927708,-5.449954,-5.958840,-1.246402,-5.961306,4.112701,-2.477851,-4.089262,-3.659406,6.087860,-8.966497,9.357295,4.603996,-4.739748,0.463579,-5.265584,5.043515,4.528463,1.576516,-6.757583,4.866466,0.522614,1.110919,4.230076,-6.717726,6.888064,-3.167453,9.361467,8.993797,4.843596,4.750454,-7.798737,-1.651082,-5.922804,-4.361372,2.867720,-9.091082,1.621708,-7.055269,-7.983939,-1.693829,5.550198,-8.526096,-6.599984,3.101859,-4.573467,8.353394,4.523306,-3.723775,6.369364,-0.761794,0.601727,-6.932704,-3.775584,4.843107,5.880409,-4.211520,-8.987476,9.134981,-3.640930,-4.496723,8.274273,-0.560099,0.693057,3.140740,5.346856,-7.380738,-6.316250,9.717985,3.670798,6.702063,-8.130632,-4.282979,-1.327585,3.534319,-2.659991,9.319313,2.492728,-8.045499,4.942468,-4.375899,9.762689,5.633380,4.913532,-0.882325,6.346525,2.944866,6.660347,-7.051641,6.364913,7.644946,0.935661,3.718297,-1.923475,7.127537,1.623606,-7.818154,-1.937044,2.943811,-8.822210,2.976834,0.824010,-9.221820,-9.750119,3.683022,-1.265655,9.507762,9.857482,8.265771,-0.024521,9.826854,-5.998880,-9.789035,5.175262,-6.892451,7.224808,7.837348,-9.932675,9.920546,-4.553341,-2.020195,1.577493,-7.687600,-8.688311,-7.879733,7.067424,8.768630,3.106842,-0.411315,1.884538,0.956415,-2.294008,6.815292,-4.417399,5.689403,9.857664,1.002315,4.016344,-7.031937,9.690263,-8.185790,-0.836072,-7.189781,3.067959,7.965526,4.738075,2.234489,5.693094,-7.236322,-3.501672,9.191189,6.008978,-0.386708,-5.177914,3.332605,-4.184600,-5.619905,2.117264,-1.990886,-4.287430,0.160009,-1.945152,9.638484,1.104764,9.623629,-0.290439,-3.175714,-7.149278,-6.494338,9.172378,-5.581708,-8.512258,-3.320605,-4.849517,-9.498539,-2.206640,-7.655797,5.770733,9.415925,-4.105005,-9.316496,2.199464,-2.772808,0.821761,-7.355908,-6.738612,-0.173216,-4.834182,-8.275683,-2.503891,7.419215,-9.309731,2.822480,6.314702,9.991301,-5.988987,-7.088289,-8.906905,1.215730,-1.543065,-1.332923,-3.214104,5.037210,2.983136,9.852847,-7.360412,0.792695,7.635742,-1.829173,0.708144,-8.340032,2.104335,2.567800,9.515869,-9.606192,-7.473655,3.358828,8.934207,2.557577,-4.759043,-2.293258,4.178126,-9.583333,9.745366,-5.399898,-1.385630,-0.749094,6.830664,2.620684,-9.972281,-6.612462,-6.313917,3.207675,-2.942949,-7.589527,-1.420907,-1.996086,-0.429671,-5.223785,7.249590,-9.750971,2.990434,-3.118232,-8.612009,2.857836,3.299570,-4.567483,6.724750,6.241831,-4.777746,9.022624,7.784658,3.935221,-0.763176,2.566250,-5.733803,7.684867,-2.746196,-0.004479,5.260882,2.201472,-5.492595,-4.932750,9.075695,3.572471,8.898896,-3.062549,-3.366028,5.304226,9.683292,4.677744,-1.364063,9.677163,-2.047269,-0.824450,-5.908325,-1.013125,9.878835,-0.349503,-2.358113,-0.974736,-3.726294,-1.945497,-4.035445,3.218337,-4.646025,8.865921,4.601322,5.277261,2.196492,4.604871,9.884836,-2.715395,-7.985447,-1.702106,-1.542580,7.999724,6.691694,-7.961683,7.911522,-6.041648,-5.324363,-6.821910,-6.561264,5.925988,8.400693,5.345764,-8.147851,3.757162,8.514560,3.779423,7.732820,-8.204774,8.497482,-5.003515,9.499862,-7.867986,7.984224,5.306221,0.843159,5.063747,-4.108417,4.650981,-3.668523,8.926119,-5.714637,8.740265,9.095138,6.645724,-4.625955,3.778284,-9.478104,3.774931,0.801790,1.361178,7.139092,0.965485,-5.259166,-8.033586,-3.700871,-9.579774,1.472916,-7.228488,9.771291,6.236245,2.349547,2.013751,-7.702837,2.166019,-1.115779,-8.443054,9.302185,4.947481,1.839820,-8.231163,9.351604,-7.490839,7.205347,-0.728989,-0.424023,-6.504730,-4.606385,5.579107,4.553599,-8.259072,-1.729388,2.757626,3.756074,9.943788,9.879539,-3.153008,-7.808631,2.712115,4.933416,-5.725204,9.217261,1.923218,4.030178,-5.753987,-7.599052,-9.764038,-0.353351,-9.084088,-7.681146,-3.094219,-8.203029,-7.382986,3.490575,-7.914432,6.650512,0.483766,0.047318,7.467123,3.590757,4.302118,-1.644737,-6.823060,-5.985045,-9.265755,-0.882913,-4.479326,5.805510,8.105769,-6.896585,5.510858,8.182728,-9.569489,-3.747919,5.390951,1.397550,7.700270,-9.775148,-6.307618,-7.163653,5.709097,6.593428,1.975606,-6.295011,-3.422019,-9.126880,1.981449,-5.299226,1.948372,6.513044,-1.557740,5.493601,-6.368934,-1.286143,-7.640379,-0.534163,8.276457,3.356272,-0.630598,-5.546185,-0.965901,8.591046,-5.212807,8.534557,-4.877636,-7.117296,-9.762794,-8.174406,0.998736,4.335498,0.539000,9.231815,-6.861045,-3.750425,-0.484794,6.743579,8.383582,-8.484588,-8.248370,1.339696,-3.270051,2.033701,-1.150804,-8.251815,-5.791300,3.258948,8.182620,4.483347,-3.770496,-7.191319,-0.359542,8.967983,-7.030103,2.352998,-9.672441,8.669299,-2.009457,4.176066,-4.239283,-0.296404,1.927825,5.419815,-0.010729,-6.048576,-3.233158,7.910472,-5.253664,-5.943627,5.423416,2.138232,6.926486,-0.374148,-6.488103,-2.121378,7.400239,9.844974,-1.050757,5.432085,0.460525,8.137610,5.951023,-7.716020,-1.400444,-4.500111,-8.603238,4.542358,2.297385,8.632614,2.742677,-6.923435,-2.761670,4.988263,-2.242282,4.789988,0.364980,9.145152,-4.841957,-2.445946,5.499803,-5.921082,4.824946,7.462282,0.611008,-6.671972,-9.963970,-0.693277,-8.392209,2.276889,-2.720846,2.076097,-2.549982,-3.718726,-2.074433,3.079164,-4.587485,-4.783935,8.220802,-0.193130,-3.931258,6.338835,4.173337,-6.946139,2.985112,2.088420,-4.086819,6.456193,8.146188,2.433586,1.906482,1.670708,-0.764218,4.150275,6.220445,0.464843,-1.614851,-1.044454,-8.636820,1.126497,3.513998,7.132526,2.568790,-7.137264,2.128863,9.143555,-3.038920,-7.927764,-7.194949,-7.280548,5.465296,5.504649,-3.532743,1.886405,-9.025385,-3.700897,7.167999,-6.548972,3.757327,-6.247335,-0.147912,6.140748,-5.400654,-9.033839,7.846041,9.319276,-5.499903,-7.100221,-5.231588,5.692640,-6.481667,-4.021213,5.990295,9.514043,2.225639,0.765301,1.552092,-8.616664,-2.464655,-9.533763,7.320011,-0.169023,-9.215588,-1.764308,1.059518,-9.172448,-5.852286,6.446951,3.270096,-7.243677,-0.230610,-3.391751,-8.576158,-9.391120,0.562926,-1.329273,-9.738195,-4.280033,1.207282,5.949128,-4.244570,-5.279596,3.209547,0.857954,-1.292057,2.243586,9.190004,-4.142129,7.533186,4.467488,4.967131,3.161260,-9.922622,6.260959,2.739685,-1.998315,-7.178666,-7.522956,9.788427,-8.983571,7.847214,-9.748388,4.779054,-6.932378,5.517204,-7.052235,1.931129,-5.479492,9.635371,5.296328,6.981213,3.092467,-2.563846,6.227154,0.467613,-9.653172,0.675410,1.060505,2.214886,5.864808,9.625029,-8.519759,-0.130731,1.289631,-4.040500,-7.307558,-6.399270,6.062398,5.210428,-6.759299,-7.580490,7.055001,-9.414762,-5.030260,-7.778201,-6.839449,5.548975,-1.108104,-5.795699,-6.944568,-3.723836,-2.350192,-1.916784,3.951128,-2.829797,-8.232311,-3.267524,-5.808110,-0.553221,4.528981,8.406037,2.329686,-3.885408,-7.166450,5.182051,2.683761,5.567642,-6.718659,6.238248,3.397709,-6.276008,-7.039219,9.506760,0.223696,6.261757,-2.667716,-5.901615,-9.421940,4.478180,4.132047,1.072103,-6.879288,-9.320186,-2.972350,-2.815689,3.532063,9.941406,-4.998846,2.775418,-0.279216,-7.541494,7.694877,-1.173434,1.794230,-4.834436,-0.140348,8.619458,-1.277778,-6.480394,7.028939,-4.582775,4.798818,-6.883236,-2.520690,0.514315,-4.540184,0.045920,-7.896900,3.392513,0.943915,3.059801,8.187755,-1.430778,-0.915734,-6.799239,4.050577,2.878092,-7.537539,-6.834109,6.743844,-9.617245,4.590215,8.483118,9.657984,3.369437,-7.765914,6.543439,8.175716,6.095317,-6.619402,5.976630,-6.046002], dtype = "float64")#candidate|8954|(1040,)|const|float64
call_8953 = relay.TupleGetItem(func_4649_call(relay.reshape(const_8954.astype('float64'), [16, 13, 5]), relay.reshape(const_8954.astype('float64'), [16, 13, 5]), ), 0)
call_8955 = relay.TupleGetItem(func_4653_call(relay.reshape(const_8954.astype('float64'), [16, 13, 5]), relay.reshape(const_8954.astype('float64'), [16, 13, 5]), ), 0)
output = relay.Tuple([call_8924,call_8953,const_8954,])
output2 = relay.Tuple([call_8925,call_8955,const_8954,])
func_9024 = relay.Function([], output)
mod['func_9024'] = func_9024
mod = relay.transform.InferType()(mod)
output = func_9024()
func_9025 = relay.Function([], output)
mutated_mod['func_9025'] = func_9025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_9045 = relay.TupleGetItem(func_4610_call(), 0)
call_9046 = relay.TupleGetItem(func_4611_call(), 0)
output = relay.Tuple([call_9045,])
output2 = relay.Tuple([call_9046,])
func_9048 = relay.Function([], output)
mod['func_9048'] = func_9048
mod = relay.transform.InferType()(mod)
mutated_mod['func_9048'] = func_9048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9048_call = mutated_mod.get_global_var('func_9048')
call_9049 = func_9048_call()
output = call_9049
func_9050 = relay.Function([], output)
mutated_mod['func_9050'] = func_9050
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9079 = relay.var("var_9079", dtype = "float64", shape = (10, 13, 2))#candidate|9079|(10, 13, 2)|var|float64
uop_9080 = relay.rsqrt(var_9079.astype('float64')) # shape=(10, 13, 2)
output = uop_9080
output2 = uop_9080
func_9098 = relay.Function([var_9079,], output)
mod['func_9098'] = func_9098
mod = relay.transform.InferType()(mod)
mutated_mod['func_9098'] = func_9098
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9099 = relay.var("var_9099", dtype = "float64", shape = (10, 13, 2))#candidate|9099|(10, 13, 2)|var|float64
func_9098_call = mutated_mod.get_global_var('func_9098')
call_9100 = func_9098_call(var_9099)
output = call_9100
func_9101 = relay.Function([var_9099], output)
mutated_mod['func_9101'] = func_9101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8151_call = mod.get_global_var('func_8151')
func_8152_call = mutated_mod.get_global_var('func_8152')
call_9129 = func_8151_call()
call_9130 = func_8151_call()
output = relay.Tuple([call_9129,])
output2 = relay.Tuple([call_9130,])
func_9143 = relay.Function([], output)
mod['func_9143'] = func_9143
mod = relay.transform.InferType()(mod)
output = func_9143()
func_9144 = relay.Function([], output)
mutated_mod['func_9144'] = func_9144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6669_call = mod.get_global_var('func_6669')
func_6671_call = mutated_mod.get_global_var('func_6671')
call_9273 = func_6669_call()
call_9274 = func_6669_call()
const_9285 = relay.const([[[6.779467,1.059277],[-0.050296,6.097564],[-9.953096,-6.763984],[-7.006216,0.733032],[3.993039,-8.882204],[-1.369761,2.915168],[8.676428,0.714109],[-9.919235,7.369255]],[[2.143459,-1.729911],[-3.590176,1.041971],[-6.656405,3.015597],[9.892138,3.836315],[-3.506028,1.676913],[6.215197,-2.988255],[7.154871,-1.624782],[-4.375100,-8.331436]],[[-3.480253,-7.733662],[-9.893086,0.099579],[4.303313,9.574260],[6.435502,3.931144],[9.470360,1.531602],[7.810456,0.191792],[5.578134,-8.215017],[8.312287,7.189844]],[[-9.710034,-1.511177],[2.603112,4.058083],[9.912707,-4.814920],[-7.971090,-4.970306],[-3.140977,-5.287089],[8.109733,1.542639],[9.916011,4.413843],[-8.798248,1.843445]],[[-4.241706,8.003349],[7.742900,-7.342530],[-7.184243,-6.555390],[-7.496854,-3.285357],[-5.418117,-3.668025],[-0.124267,-7.153371],[-7.323349,-3.613407],[0.458837,5.529340]],[[3.427311,3.096091],[8.105227,3.663756],[-4.128207,-5.981305],[-5.879152,-5.363342],[3.045883,4.191508],[-6.820743,-4.459385],[6.685766,4.121018],[-2.633336,-6.488369]],[[8.911272,-5.935159],[7.672435,-2.517031],[6.696082,-1.672866],[3.337129,-3.399059],[3.612176,-8.223534],[-6.679412,-5.246031],[5.045093,-1.169707],[-7.529603,-6.935986]],[[-1.279520,2.725006],[-8.553393,-2.534734],[-7.016530,-9.838243],[5.495342,8.276093],[-3.012322,-6.198517],[-2.582334,-8.742242],[-9.903987,3.096161],[4.157100,-6.745927]],[[-0.598333,7.260509],[-9.925109,0.128944],[-4.408323,-6.489851],[-0.895139,-4.399766],[-8.811818,0.727060],[-1.341675,-2.161020],[-2.275947,1.064556],[6.645794,-5.575862]],[[0.642722,9.105848],[2.472600,5.337138],[-2.218390,6.191854],[9.230843,5.127492],[-4.038478,-6.746378],[-1.729984,1.569518],[-3.494205,-7.704290],[-1.136306,5.504594]]], dtype = "float32")#candidate|9285|(10, 8, 2)|const|float32
bop_9286 = relay.multiply(call_9273.astype('int16'), const_9285.astype('int16')) # shape=(10, 8, 2)
bop_9289 = relay.multiply(call_9274.astype('int16'), const_9285.astype('int16')) # shape=(10, 8, 2)
func_299_call = mod.get_global_var('func_299')
func_301_call = mutated_mod.get_global_var('func_301')
call_9300 = relay.TupleGetItem(func_299_call(relay.reshape(call_9273.astype('float64'), [10, 8, 1])), 0)
call_9301 = relay.TupleGetItem(func_301_call(relay.reshape(call_9273.astype('float64'), [10, 8, 1])), 0)
uop_9304 = relay.log2(bop_9286.astype('float64')) # shape=(10, 8, 2)
uop_9306 = relay.log2(bop_9289.astype('float64')) # shape=(10, 8, 2)
func_5750_call = mod.get_global_var('func_5750')
func_5751_call = mutated_mod.get_global_var('func_5751')
call_9313 = relay.TupleGetItem(func_5750_call(), 0)
call_9314 = relay.TupleGetItem(func_5751_call(), 0)
func_6219_call = mod.get_global_var('func_6219')
func_6220_call = mutated_mod.get_global_var('func_6220')
call_9316 = func_6219_call()
call_9317 = func_6219_call()
func_4707_call = mod.get_global_var('func_4707')
func_4710_call = mutated_mod.get_global_var('func_4710')
call_9324 = relay.TupleGetItem(func_4707_call(relay.reshape(call_9313.astype('int32'), [660,])), 3)
call_9325 = relay.TupleGetItem(func_4710_call(relay.reshape(call_9313.astype('int32'), [660,])), 3)
func_2085_call = mod.get_global_var('func_2085')
func_2089_call = mutated_mod.get_global_var('func_2089')
var_9338 = relay.var("var_9338", dtype = "int8", shape = ())#candidate|9338|()|var|int8
const_9339 = relay.const([[-6,-10,-4,-6],[-2,-9,-8,8],[-7,-9,-1,-6],[-1,-3,-7,-5],[6,9,10,2],[-8,5,-9,3],[-3,1,-7,-2],[6,-5,-2,9],[4,9,-3,-6],[-2,-6,3,7]], dtype = "int8")#candidate|9339|(10, 4)|const|int8
call_9337 = func_2085_call(relay.reshape(var_9338.astype('int8'), []), relay.reshape(const_9339.astype('int8'), [4, 5, 2]), )
call_9340 = func_2085_call(relay.reshape(var_9338.astype('int8'), []), relay.reshape(const_9339.astype('int8'), [4, 5, 2]), )
func_5245_call = mod.get_global_var('func_5245')
func_5249_call = mutated_mod.get_global_var('func_5249')
var_9343 = relay.var("var_9343", dtype = "int16", shape = (168,))#candidate|9343|(168,)|var|int16
var_9344 = relay.var("var_9344", dtype = "float64", shape = (180,))#candidate|9344|(180,)|var|float64
call_9342 = relay.TupleGetItem(func_5245_call(relay.reshape(var_9343.astype('int16'), [168,]), relay.reshape(var_9344.astype('float64'), [3, 60]), ), 0)
call_9345 = relay.TupleGetItem(func_5249_call(relay.reshape(var_9343.astype('int16'), [168,]), relay.reshape(var_9344.astype('float64'), [3, 60]), ), 0)
output = relay.Tuple([call_9300,uop_9304,call_9313,call_9316,call_9324,call_9337,var_9338,const_9339,call_9342,var_9343,var_9344,])
output2 = relay.Tuple([call_9301,uop_9306,call_9314,call_9317,call_9325,call_9340,var_9338,const_9339,call_9345,var_9343,var_9344,])
func_9354 = relay.Function([var_9338,var_9343,var_9344,], output)
mod['func_9354'] = func_9354
mod = relay.transform.InferType()(mod)
var_9355 = relay.var("var_9355", dtype = "int8", shape = ())#candidate|9355|()|var|int8
var_9356 = relay.var("var_9356", dtype = "int16", shape = (168,))#candidate|9356|(168,)|var|int16
var_9357 = relay.var("var_9357", dtype = "float64", shape = (180,))#candidate|9357|(180,)|var|float64
output = func_9354(var_9355,var_9356,var_9357,)
func_9358 = relay.Function([var_9355,var_9356,var_9357,], output)
mutated_mod['func_9358'] = func_9358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8199_call = mod.get_global_var('func_8199')
func_8201_call = mutated_mod.get_global_var('func_8201')
call_9420 = relay.TupleGetItem(func_8199_call(), 0)
call_9421 = relay.TupleGetItem(func_8201_call(), 0)
func_9098_call = mod.get_global_var('func_9098')
func_9101_call = mutated_mod.get_global_var('func_9101')
const_9432 = relay.const([-8.897886,3.108462,-9.134160,-1.897553,-8.444768,-5.667539,-8.313913,9.177260,-1.643905,2.690238,0.247866,-5.393262,-3.959836,-7.707856,0.773386,-3.499544,-4.591511,4.851667,-6.724353,-2.873128,-0.032541,8.578212,4.350420,2.387310,-1.315052,0.346485,4.675943,-1.560237,-8.416379,-4.771986,3.841572,7.039134,-1.418314,1.802771,-6.127100,2.133113,-8.086049,-5.869901,-8.367884,2.987287,-1.329312,-4.841247,-1.809317,8.702629,0.669514,-6.503731,-8.762594,-7.206727,-7.298959,8.902585,0.950157,4.404189,3.460147,6.750690,-2.335079,4.278599,-9.423498,-5.921255,-3.488409,7.024646,0.641625,-4.574347,5.204808,-4.110442,-8.304303,-4.609514,3.636819,8.625616,7.411948,-5.910129,7.206348,-0.702475,3.800770,-0.238329,-9.724457,-2.204082,-5.457516,7.352663,4.797786,1.499371,-8.612292,-9.209428,-2.951751,-5.964212,-8.516445,2.491273,-2.732449,5.368515,-6.931675,1.839238,8.015087,2.359982,6.402027,9.870822,-6.162421,-5.632066,2.247733,-4.415121,6.230417,2.846572,1.755962,4.915964,6.856403,-7.183716,2.461964,-3.683814,8.598508,-5.259532,8.754766,5.491804,-5.145770,-6.381923,-6.043275,1.563037,3.886965,-3.166943,0.374241,5.612243,-9.448187,8.865989,9.380171,1.887455,3.798448,0.281745,9.180455,-8.826530,1.795815,6.995063,-8.153695,5.994312,-7.454088,-2.108230,2.574187,-4.879110,3.746535,7.232491,9.612475,6.176889,-5.709289,3.077683,-7.661469,-7.167076,-3.133791,3.806733,-6.718769,9.164536,-0.965905,8.754121,9.366639,-7.500264,6.875218,6.253899,-2.785052,4.070734,-1.414054,-5.930884,-6.016792,-8.358126,5.957440,4.349786,-6.146892,-2.826824,5.133280,-1.493586,8.116594,9.695410,9.054947,9.233878,-6.671940,-6.611762,-8.869457,7.739277,5.718445,6.491149,1.547329,6.300565,1.689083,7.360480,5.825016,3.681878,-4.373110,6.929230,-6.499362,2.224732,2.661583,9.150556,-5.140734,-0.279205,-4.132190,-9.022250,9.418105,1.724270,8.034865,9.955855,-0.730058,7.387221,2.979822,-4.389821,-3.419285,-2.324622,-7.249601,7.152200,-5.041249,-6.744896,9.772930,2.336051,-8.904597,-6.579454,7.207973,-5.972888,-3.699310,-7.449543,-5.920913,9.404800,-5.261901,-6.474277,9.932117,9.167750,-7.469335,-9.563287,1.465361,-6.346557,-5.167322,3.430093,-6.699510,-2.756417,-6.183699,-9.968737,0.799699,2.778167,-2.159520,-4.495872,6.819466,3.445795,-4.275401,0.427182,7.032886,4.053547,-8.706513,4.603151,2.998044,-7.131023,-2.800867,-1.823255,-9.980310,5.590725,-2.265272,7.861551,-2.940840,0.294664,-6.041162,-6.580006,-6.339917,-9.004172,-7.516075,7.862764,5.306577,0.477156,-2.810257,1.587069], dtype = "float64")#candidate|9432|(260,)|const|float64
call_9431 = func_9098_call(relay.reshape(const_9432.astype('float64'), [10, 13, 2]))
call_9433 = func_9098_call(relay.reshape(const_9432.astype('float64'), [10, 13, 2]))
func_6072_call = mod.get_global_var('func_6072')
func_6074_call = mutated_mod.get_global_var('func_6074')
call_9457 = relay.TupleGetItem(func_6072_call(), 0)
call_9458 = relay.TupleGetItem(func_6074_call(), 0)
output = relay.Tuple([call_9420,call_9431,const_9432,call_9457,])
output2 = relay.Tuple([call_9421,call_9433,const_9432,call_9458,])
func_9480 = relay.Function([], output)
mod['func_9480'] = func_9480
mod = relay.transform.InferType()(mod)
output = func_9480()
func_9481 = relay.Function([], output)
mutated_mod['func_9481'] = func_9481
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9489 = relay.var("var_9489", dtype = "float64", shape = (5, 10, 5))#candidate|9489|(5, 10, 5)|var|float64
uop_9490 = relay.sin(var_9489.astype('float64')) # shape=(5, 10, 5)
output = uop_9490
output2 = uop_9490
func_9502 = relay.Function([var_9489,], output)
mod['func_9502'] = func_9502
mod = relay.transform.InferType()(mod)
mutated_mod['func_9502'] = func_9502
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9503 = relay.var("var_9503", dtype = "float64", shape = (5, 10, 5))#candidate|9503|(5, 10, 5)|var|float64
func_9502_call = mutated_mod.get_global_var('func_9502')
call_9504 = func_9502_call(var_9503)
output = call_9504
func_9505 = relay.Function([var_9503], output)
mutated_mod['func_9505'] = func_9505
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9024_call = mod.get_global_var('func_9024')
func_9025_call = mutated_mod.get_global_var('func_9025')
call_9541 = relay.TupleGetItem(func_9024_call(), 0)
call_9542 = relay.TupleGetItem(func_9025_call(), 0)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_9588 = relay.TupleGetItem(func_4610_call(), 0)
call_9589 = relay.TupleGetItem(func_4611_call(), 0)
output = relay.Tuple([call_9541,call_9588,])
output2 = relay.Tuple([call_9542,call_9589,])
func_9592 = relay.Function([], output)
mod['func_9592'] = func_9592
mod = relay.transform.InferType()(mod)
mutated_mod['func_9592'] = func_9592
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9592_call = mutated_mod.get_global_var('func_9592')
call_9593 = func_9592_call()
output = call_9593
func_9594 = relay.Function([], output)
mutated_mod['func_9594'] = func_9594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_9609 = relay.TupleGetItem(func_4821_call(), 1)
call_9610 = relay.TupleGetItem(func_4822_call(), 1)
uop_9619 = relay.rsqrt(call_9609.astype('float64')) # shape=(15, 4, 11)
uop_9621 = relay.rsqrt(call_9610.astype('float64')) # shape=(15, 4, 11)
uop_9638 = relay.tan(uop_9619.astype('float32')) # shape=(15, 4, 11)
uop_9640 = relay.tan(uop_9621.astype('float32')) # shape=(15, 4, 11)
output = relay.Tuple([uop_9638,])
output2 = relay.Tuple([uop_9640,])
func_9661 = relay.Function([], output)
mod['func_9661'] = func_9661
mod = relay.transform.InferType()(mod)
mutated_mod['func_9661'] = func_9661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9661_call = mutated_mod.get_global_var('func_9661')
call_9662 = func_9661_call()
output = call_9662
func_9663 = relay.Function([], output)
mutated_mod['func_9663'] = func_9663
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8137_call = mod.get_global_var('func_8137')
func_8138_call = mutated_mod.get_global_var('func_8138')
call_9680 = relay.TupleGetItem(func_8137_call(), 7)
call_9681 = relay.TupleGetItem(func_8138_call(), 7)
output = call_9680
output2 = call_9681
func_9685 = relay.Function([], output)
mod['func_9685'] = func_9685
mod = relay.transform.InferType()(mod)
mutated_mod['func_9685'] = func_9685
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9685_call = mutated_mod.get_global_var('func_9685')
call_9686 = func_9685_call()
output = call_9686
func_9687 = relay.Function([], output)
mutated_mod['func_9687'] = func_9687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4843_call = mod.get_global_var('func_4843')
func_4844_call = mutated_mod.get_global_var('func_4844')
call_9688 = func_4843_call()
call_9689 = func_4843_call()
output = call_9688
output2 = call_9689
func_9693 = relay.Function([], output)
mod['func_9693'] = func_9693
mod = relay.transform.InferType()(mod)
output = func_9693()
func_9694 = relay.Function([], output)
mutated_mod['func_9694'] = func_9694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9685_call = mod.get_global_var('func_9685')
func_9687_call = mutated_mod.get_global_var('func_9687')
call_9764 = func_9685_call()
call_9765 = func_9685_call()
uop_9766 = relay.asinh(call_9764.astype('float32')) # shape=(2288,)
uop_9768 = relay.asinh(call_9765.astype('float32')) # shape=(2288,)
bop_9771 = relay.less(uop_9766.astype('bool'), relay.reshape(call_9764.astype('bool'), relay.shape_of(uop_9766))) # shape=(2288,)
bop_9774 = relay.less(uop_9768.astype('bool'), relay.reshape(call_9765.astype('bool'), relay.shape_of(uop_9768))) # shape=(2288,)
func_5067_call = mod.get_global_var('func_5067')
func_5072_call = mutated_mod.get_global_var('func_5072')
var_9782 = relay.var("var_9782", dtype = "float32", shape = (462,))#candidate|9782|(462,)|var|float32
const_9783 = relay.const([-7.656651,-2.878204,5.226196,2.815605,1.532173,-1.529581,-9.424933,-7.043057,0.854230,7.745252,-2.813214,4.105173,-8.149200,3.191302,-6.354651,-1.045738,5.535930,-2.170752,-9.685372,-2.885579,-8.760150,-8.563764,4.828389,9.427700,-0.602087,2.865061,-4.748105,-6.332549,5.557606,-1.972172,5.053697,1.807569,-6.551458,7.683269,9.136110,-4.313382,-1.697402,-2.846839,7.723680,-5.595127,-0.645461,-0.517657,-1.628809,-2.524547,9.691088,8.550686,7.915793,2.376449,2.471125,3.956715,-5.026701,-1.008383,-5.247762,-8.403172,-4.376250,-2.281349,-5.332888,-0.682755,6.126993,8.881688,6.747837,0.123866,4.854847,-5.897222,9.006794,0.839517,-7.100280,-0.578748,1.044374,-8.804805,3.107175,-0.026895,-7.380173,-0.015061,5.086072,-0.963497,9.613690,-2.605213,-3.089309,3.182501,-7.418966,-5.593664,-8.347078,2.658904,5.232557,5.459281,-7.724970,2.183668,-5.848769,-0.075408,0.653299,7.134546,-6.391473,6.263489,-0.711076,-1.631606,3.360931,0.736243,7.445390,2.913966,4.125728,6.417853,8.220389,-7.184764,9.586918,0.184750,0.756032,5.154812,-9.582367,-3.620587,5.453110,6.559731,3.721286,-9.244625,-3.426210,-7.995971,-5.980867,3.540354,-7.879730,-9.570691,1.376866,-6.053898,-0.074866,-9.089535,-0.232715,2.990767,-9.548580,-8.208072,-7.719748,-0.538438,4.243002,-1.276878,6.003678,2.575798,5.555896,3.828184,2.043449,4.064465,6.390837,8.820591,-1.782024,8.200362,8.113752,4.205496,-8.274929,-9.574432,-3.611401,5.493611,4.544937,5.975566,-0.523022,6.388324,-3.648269,2.946904,-3.350132,1.533182,-3.111563,3.874286,-6.187603,3.888217,8.356795,-2.178279,-6.392403,8.485942,-1.622966,-5.337660,1.585826,5.865453,-2.252818,5.914951,0.256248,9.631466,2.994637,0.592842,3.778513,-2.242905,8.523991,-9.311505,-9.260431,5.640374], dtype = "float64")#candidate|9783|(180,)|const|float64
var_9784 = relay.var("var_9784", dtype = "float32", shape = (35, 1))#candidate|9784|(35, 1)|var|float32
call_9781 = relay.TupleGetItem(func_5067_call(relay.reshape(var_9782.astype('float32'), [462,]), relay.reshape(const_9783.astype('float64'), [180,]), relay.reshape(var_9784.astype('float32'), [35, 1]), ), 5)
call_9785 = relay.TupleGetItem(func_5072_call(relay.reshape(var_9782.astype('float32'), [462,]), relay.reshape(const_9783.astype('float64'), [180,]), relay.reshape(var_9784.astype('float32'), [35, 1]), ), 5)
func_1356_call = mod.get_global_var('func_1356')
func_1359_call = mutated_mod.get_global_var('func_1359')
call_9786 = func_1356_call(relay.reshape(var_9782.astype('float32'), [6, 11, 7]), relay.reshape(var_9782.astype('float32'), [6, 11, 7]), )
call_9787 = func_1356_call(relay.reshape(var_9782.astype('float32'), [6, 11, 7]), relay.reshape(var_9782.astype('float32'), [6, 11, 7]), )
func_4874_call = mod.get_global_var('func_4874')
func_4877_call = mutated_mod.get_global_var('func_4877')
const_9789 = relay.const([-10,-9,3,-4,-9,1,4,-4,3,-2,-10,-5,4,-10,7,6,-10,4,6,-2,-2,2,7,5,-1,4,-6,4,7,10,5,3,-10,9,-4,4,6,-2,-1,2,3,-3,-3,2,1,3,-7,-1,1,4,3,-3,-3,1,-1,-6,-8,-5,10,-2,1,-8,2,-5,1,10,7,-2,-8,2,7,4,-1,-8,-8,1,-6,6,-10,2,-10,5,8,6,10,5,-10,-5,-10,3,5,-7,-4,-8,-6,4,-3,-5,-6,-6,3,-6,-2,5,5,-10,-3,-1,4,9,-10,-7,-2,3,-5,4,2,-10,-4,6,4,-2,-5,-2,-4,8,-6,8,-9,-5,4,2,-3,8,-9,7,-2,-10,1,5,-5,-1,10,-8,-4,1,6,2,8,-5,6,-10,-10,-5,-6,-8,5,-1,-1,-2,-4,1,-8,7,4,-3,-5,-9,7,8,6,4,5,6,6,9,3,-10,-2,9,3,6,-8,5,-1,-1,-8,8,-2,-9,2,-8,7,-8,-7,7,-2,7,10,-7,4,-7,3,-6,-10,3,3,9,-9,3,5,-7,-4,6,8,-4,1,7,-7,-9,7,10,-3,-2,-5,10,4,8,-4,2,10,-4,-7,3,3,-2,-3,-4,1,-1,-10,8,-8,4,3,-4,9,-1,9,2,-7,-4,-9,9,4,-10,-8,-2,7,10,9,-10,-4,-7,-7,4,-5,6,-7,-8,2,-9,6,-1,-5,-2,7,-5,5,3,-10,7,5,3,-8,-5,7,-3,5,-8,6,-7,4,-3,5,-10,-3,2,10,-2,-4,-9,2,8,7,-10,-5,-8,-8,-7,-9,7,4,9,-5,-10,-7,4,2,-7,-7,4,3,-3,4,-5,7,-4,3,4,-4,9,-7,3,2,-10,6,-2,-9,1,5,8,-9,-4,8,10,-4,5,1,-3,-9,-3,1,5,8,-3,3,-6,4,5,-8,3,-4,-5,8,10,-3,2,6,-1,-5,-9,6,1,3,-3,10,5,6,-9,-10,-2,9,6,-3,-2,-1,-9,6,10,-5,-2,-1,-9,1,-1,-6,-5,-9,10,5,-10,-5,-7,8,-2,-10,-10,-5,10,-8,6,-6,-8,-1,-6,-2,-5,3,10,1,6,6,4,6,7,7,-5,6,9,-2,4,-1,-3,-4,8,2,-9,-10,2,-9,10,-4,-10,-8,8,1,-6,-2,9,-9,-1,10,1,-5,8,10,9,-2,-4,7,2,5,-2,-4,-3,7,4,-6,-9,-6,6,-4,-1,5,9,-9,-9,9,-1,2,6,10,7,4,8,5,-7,-8,-7,8,-4,-7,3,-4,-8,10,6,-3,7,-10,-9,-10,4,-9,-2,7,5,-1,-1,-3,-3,-5,5,3,7,-9,-8,7,9,-3,10,-7,7,3,2,8,-1,4,5,7,1,-10,-7,1,10,4,-7,7,8,-3,-6,-6,6,-2,-7,2,-7,9,1,7,-7,3,4,7,2,2,10,6,8,-8,-6,-5,5,4,-7,7,-4,7,2,7,3,-3,-7,-1,-4,-10,-9,3,2,-10,-10,2,-7,1,-10,-3,-8,-7,5,10,7,2,-8,2,6,-8,6,10,8,5,10,2,-6,2,7,1,-1,-9,-9,8,10,-2,7,-4,-5,-4,8,-2,-5,6,-6,3,1], dtype = "int64")#candidate|9789|(624,)|const|int64
call_9788 = relay.TupleGetItem(func_4874_call(relay.reshape(const_9789.astype('int64'), [24, 26])), 0)
call_9790 = relay.TupleGetItem(func_4877_call(relay.reshape(const_9789.astype('int64'), [24, 26])), 0)
output = relay.Tuple([bop_9771,call_9781,var_9782,const_9783,var_9784,call_9786,call_9788,const_9789,])
output2 = relay.Tuple([bop_9774,call_9785,var_9782,const_9783,var_9784,call_9787,call_9790,const_9789,])
func_9796 = relay.Function([var_9782,var_9784,], output)
mod['func_9796'] = func_9796
mod = relay.transform.InferType()(mod)
mutated_mod['func_9796'] = func_9796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9796_call = mutated_mod.get_global_var('func_9796')
var_9798 = relay.var("var_9798", dtype = "float32", shape = (462,))#candidate|9798|(462,)|var|float32
var_9799 = relay.var("var_9799", dtype = "float32", shape = (35, 1))#candidate|9799|(35, 1)|var|float32
call_9797 = func_9796_call(var_9798,var_9799,)
output = call_9797
func_9800 = relay.Function([var_9798,var_9799,], output)
mutated_mod['func_9800'] = func_9800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6773_call = mod.get_global_var('func_6773')
func_6775_call = mutated_mod.get_global_var('func_6775')
call_9814 = func_6773_call()
call_9815 = func_6773_call()
func_2085_call = mod.get_global_var('func_2085')
func_2089_call = mutated_mod.get_global_var('func_2089')
var_9818 = relay.var("var_9818", dtype = "int8", shape = ())#candidate|9818|()|var|int8
var_9819 = relay.var("var_9819", dtype = "int8", shape = (1, 40))#candidate|9819|(1, 40)|var|int8
call_9817 = func_2085_call(relay.reshape(var_9818.astype('int8'), []), relay.reshape(var_9819.astype('int8'), [4, 5, 2]), )
call_9820 = func_2085_call(relay.reshape(var_9818.astype('int8'), []), relay.reshape(var_9819.astype('int8'), [4, 5, 2]), )
func_6712_call = mod.get_global_var('func_6712')
func_6713_call = mutated_mod.get_global_var('func_6713')
call_9822 = func_6712_call()
call_9823 = func_6712_call()
bop_9824 = relay.bitwise_xor(var_9819.astype('uint64'), var_9818.astype('uint64')) # shape=(1, 40)
func_6728_call = mod.get_global_var('func_6728')
func_6730_call = mutated_mod.get_global_var('func_6730')
call_9829 = relay.TupleGetItem(func_6728_call(), 0)
call_9830 = relay.TupleGetItem(func_6730_call(), 0)
output = relay.Tuple([call_9814,call_9817,call_9822,bop_9824,call_9829,])
output2 = relay.Tuple([call_9815,call_9820,call_9823,bop_9824,call_9830,])
func_9831 = relay.Function([var_9818,var_9819,], output)
mod['func_9831'] = func_9831
mod = relay.transform.InferType()(mod)
var_9832 = relay.var("var_9832", dtype = "int8", shape = ())#candidate|9832|()|var|int8
var_9833 = relay.var("var_9833", dtype = "int8", shape = (1, 40))#candidate|9833|(1, 40)|var|int8
output = func_9831(var_9832,var_9833,)
func_9834 = relay.Function([var_9832,var_9833,], output)
mutated_mod['func_9834'] = func_9834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7062_call = mod.get_global_var('func_7062')
func_7063_call = mutated_mod.get_global_var('func_7063')
call_9866 = relay.TupleGetItem(func_7062_call(), 1)
call_9867 = relay.TupleGetItem(func_7063_call(), 1)
func_8594_call = mod.get_global_var('func_8594')
func_8595_call = mutated_mod.get_global_var('func_8595')
call_9877 = relay.TupleGetItem(func_8594_call(), 0)
call_9878 = relay.TupleGetItem(func_8595_call(), 0)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_9884 = func_1070_call(relay.reshape(call_9877.astype('int32'), [15, 4, 11]))
call_9885 = func_1070_call(relay.reshape(call_9877.astype('int32'), [15, 4, 11]))
func_9480_call = mod.get_global_var('func_9480')
func_9481_call = mutated_mod.get_global_var('func_9481')
call_9889 = relay.TupleGetItem(func_9480_call(), 2)
call_9890 = relay.TupleGetItem(func_9481_call(), 2)
output = relay.Tuple([call_9866,call_9877,call_9884,call_9889,])
output2 = relay.Tuple([call_9867,call_9878,call_9885,call_9890,])
func_9892 = relay.Function([], output)
mod['func_9892'] = func_9892
mod = relay.transform.InferType()(mod)
mutated_mod['func_9892'] = func_9892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9892_call = mutated_mod.get_global_var('func_9892')
call_9893 = func_9892_call()
output = call_9893
func_9894 = relay.Function([], output)
mutated_mod['func_9894'] = func_9894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9892_call = mod.get_global_var('func_9892')
func_9894_call = mutated_mod.get_global_var('func_9894')
call_9927 = relay.TupleGetItem(func_9892_call(), 1)
call_9928 = relay.TupleGetItem(func_9894_call(), 1)
var_9947 = relay.var("var_9947", dtype = "bool", shape = (15, 4, 11))#candidate|9947|(15, 4, 11)|var|bool
bop_9948 = relay.floor_mod(call_9927.astype('float64'), relay.reshape(var_9947.astype('float64'), relay.shape_of(call_9927))) # shape=(15, 4, 11)
bop_9951 = relay.floor_mod(call_9928.astype('float64'), relay.reshape(var_9947.astype('float64'), relay.shape_of(call_9928))) # shape=(15, 4, 11)
output = bop_9948
output2 = bop_9951
func_9953 = relay.Function([var_9947,], output)
mod['func_9953'] = func_9953
mod = relay.transform.InferType()(mod)
mutated_mod['func_9953'] = func_9953
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9954 = relay.var("var_9954", dtype = "bool", shape = (15, 4, 11))#candidate|9954|(15, 4, 11)|var|bool
func_9953_call = mutated_mod.get_global_var('func_9953')
call_9955 = func_9953_call(var_9954)
output = call_9955
func_9956 = relay.Function([var_9954], output)
mutated_mod['func_9956'] = func_9956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5351_call = mod.get_global_var('func_5351')
func_5352_call = mutated_mod.get_global_var('func_5352')
call_9962 = relay.TupleGetItem(func_5351_call(), 0)
call_9963 = relay.TupleGetItem(func_5352_call(), 0)
output = relay.Tuple([call_9962,])
output2 = relay.Tuple([call_9963,])
func_9967 = relay.Function([], output)
mod['func_9967'] = func_9967
mod = relay.transform.InferType()(mod)
mutated_mod['func_9967'] = func_9967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9967_call = mutated_mod.get_global_var('func_9967')
call_9968 = func_9967_call()
output = call_9968
func_9969 = relay.Function([], output)
mutated_mod['func_9969'] = func_9969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6266_call = mod.get_global_var('func_6266')
func_6268_call = mutated_mod.get_global_var('func_6268')
call_10020 = relay.TupleGetItem(func_6266_call(), 0)
call_10021 = relay.TupleGetItem(func_6268_call(), 0)
func_7521_call = mod.get_global_var('func_7521')
func_7522_call = mutated_mod.get_global_var('func_7522')
call_10022 = relay.TupleGetItem(func_7521_call(), 1)
call_10023 = relay.TupleGetItem(func_7522_call(), 1)
func_8496_call = mod.get_global_var('func_8496')
func_8499_call = mutated_mod.get_global_var('func_8499')
const_10027 = relay.const([-9.883732,4.571049,-2.809534,6.488302,6.715808,7.722035,-2.714178,8.140175,6.516805,-9.006297,-3.185341,-5.019118,-0.395326,-7.204050,0.903672,1.702988,-9.384196,-2.452141,-8.657445,-7.677829,2.068646,-3.181367,1.289172,-1.845662,-2.824700,-3.399116,9.418021,0.845580,5.252035,8.392760,0.542469,-5.011929,-7.340389,-2.367277,8.075955,-9.004269,7.493992,-4.168723,4.654844,7.807431,9.221794,-9.194088,-8.171681,4.385330,1.109892,-9.298204,0.663391,-4.776084,-7.544999,-9.259981,8.493434,-8.954990,3.793937,-5.730376,4.031453,0.497211,0.138888,7.815299,5.103738,8.074977,-2.732245,-0.151690,8.123220,6.270013,1.867515,3.511182,-5.455341,4.990902,-7.730180,-6.917028,4.047770,5.633647,3.940628,-3.188367,1.797411,7.041247,-7.886168,6.375166,-8.300382,9.495126], dtype = "float64")#candidate|10027|(80,)|const|float64
call_10026 = relay.TupleGetItem(func_8496_call(relay.reshape(const_10027.astype('float64'), [2, 40]), relay.reshape(const_10027.astype('float32'), [2, 40]), ), 13)
call_10028 = relay.TupleGetItem(func_8499_call(relay.reshape(const_10027.astype('float64'), [2, 40]), relay.reshape(const_10027.astype('float32'), [2, 40]), ), 13)
output = relay.Tuple([call_10020,call_10022,call_10026,const_10027,])
output2 = relay.Tuple([call_10021,call_10023,call_10028,const_10027,])
func_10031 = relay.Function([], output)
mod['func_10031'] = func_10031
mod = relay.transform.InferType()(mod)
output = func_10031()
func_10032 = relay.Function([], output)
mutated_mod['func_10032'] = func_10032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9592_call = mod.get_global_var('func_9592')
func_9594_call = mutated_mod.get_global_var('func_9594')
call_10067 = relay.TupleGetItem(func_9592_call(), 0)
call_10068 = relay.TupleGetItem(func_9594_call(), 0)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_10097 = relay.TupleGetItem(func_5036_call(), 0)
call_10098 = relay.TupleGetItem(func_5037_call(), 0)
output = relay.Tuple([call_10067,call_10097,])
output2 = relay.Tuple([call_10068,call_10098,])
func_10108 = relay.Function([], output)
mod['func_10108'] = func_10108
mod = relay.transform.InferType()(mod)
mutated_mod['func_10108'] = func_10108
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10108_call = mutated_mod.get_global_var('func_10108')
call_10109 = func_10108_call()
output = call_10109
func_10110 = relay.Function([], output)
mutated_mod['func_10110'] = func_10110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6219_call = mod.get_global_var('func_6219')
func_6220_call = mutated_mod.get_global_var('func_6220')
call_10138 = func_6219_call()
call_10139 = func_6219_call()
func_3456_call = mod.get_global_var('func_3456')
func_3458_call = mutated_mod.get_global_var('func_3458')
const_10148 = relay.const([[-1.671395,3.744127,7.577573,6.988083,1.542268],[-5.835274,3.547553,2.708249,-8.166898,-1.317234],[-8.375667,-5.246014,6.442273,4.284024,-0.666600],[0.650313,7.449576,-4.740164,-2.032399,-1.392706],[8.658022,-5.062018,6.764898,0.804653,5.833299],[7.351081,5.938623,-5.041217,-7.088665,-6.696026],[-5.077892,5.535672,-7.065319,-6.054126,7.487969]], dtype = "float32")#candidate|10148|(7, 5)|const|float32
call_10147 = func_3456_call(relay.reshape(const_10148.astype('float32'), [7, 1, 5]))
call_10149 = func_3456_call(relay.reshape(const_10148.astype('float32'), [7, 1, 5]))
func_4087_call = mod.get_global_var('func_4087')
func_4090_call = mutated_mod.get_global_var('func_4090')
const_10151 = relay.const([1.783431,-3.803114,-6.982835,8.804324,-0.596149,4.922197,0.674782,-2.779741,-2.933111,3.937594,-8.542920,8.241136,-0.355118,-0.697093,0.142231,-8.114767,-1.589932,-0.292926,7.277223,3.720590,8.433560,-7.507969,-2.971776,2.777332,8.035980,-2.484314,-5.506501,-5.519357,8.286831,-7.659758,-5.954423,5.048889,2.982761,1.729178,8.156532,-2.966399,0.292055,9.082016,-4.103249,4.092394,8.956805,9.634944,7.877141,-3.550906,-7.939209,7.825518,6.251807,4.091854,-8.069206,5.733761,-9.281025,3.819562,-0.106343,5.464952,2.993442,9.446498,-5.296402,-5.383814,-6.454370,-8.404729,-7.454081,3.846260,-2.124721,-3.731839,7.114862,-6.754539,-7.452161,2.488904,2.796846,2.509849,3.699175,2.377559,2.100167,3.167525,6.863485,-6.504690,-7.636087,3.035720,-0.704584,2.409274,-7.267507,1.016700,1.748526,3.252047,8.403053,2.613284,2.353411,3.576550,1.995100,-0.248341,-4.115548,-0.352975,-4.119020,-6.051851,5.555515,-8.693738,9.320795,-4.665662,0.699431,7.610773,-5.173155,0.329535,-6.730795,-0.617096,-7.193233,-3.674828,8.226449,7.079917,-2.518517,2.063211,5.212788,5.086775,2.386617,-5.815095,-6.659358,-3.398060,-4.644102,-1.443728,-9.910089,-8.504609,-9.219219,2.275703,0.961883,3.180940,-5.901311,-5.552271,8.203389,6.104714,7.512974,8.660846,9.236679,5.952687,3.641809,-5.189072,-7.596704,-8.736863,4.745312,6.723220,-8.867898,3.325677,0.449973,3.864800,5.778924,7.377568,-1.792881,-0.033719,-8.958920,3.479975,-9.598026,1.679219,4.667269,9.417849,-3.516211,4.855631,8.416363,9.238761,-4.552489,2.525386,1.170693,1.800099,9.419130,-6.847889,7.056323,-2.127219,7.490355,-6.490319,4.945697,-7.796305,-2.569311,2.626724,-6.062755,-6.079378,7.322730,-9.839574,2.143245,-2.214073,-8.232515,-2.871204,-4.815604,3.715452,8.351189,-8.843428,5.284094,-0.332431,0.765744,4.142957,-8.363150,-3.251071,-8.854035,4.214635,-7.701548,-2.909645], dtype = "float32")#candidate|10151|(192,)|const|float32
call_10150 = relay.TupleGetItem(func_4087_call(relay.reshape(const_10151.astype('float32'), [2, 6, 16]), relay.reshape(const_10151.astype('float32'), [2, 6, 16]), ), 0)
call_10152 = relay.TupleGetItem(func_4090_call(relay.reshape(const_10151.astype('float32'), [2, 6, 16]), relay.reshape(const_10151.astype('float32'), [2, 6, 16]), ), 0)
output = relay.Tuple([call_10138,call_10147,const_10148,call_10150,const_10151,])
output2 = relay.Tuple([call_10139,call_10149,const_10148,call_10152,const_10151,])
func_10153 = relay.Function([], output)
mod['func_10153'] = func_10153
mod = relay.transform.InferType()(mod)
mutated_mod['func_10153'] = func_10153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10153_call = mutated_mod.get_global_var('func_10153')
call_10154 = func_10153_call()
output = call_10154
func_10155 = relay.Function([], output)
mutated_mod['func_10155'] = func_10155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6322_call = mod.get_global_var('func_6322')
func_6324_call = mutated_mod.get_global_var('func_6324')
call_10203 = func_6322_call()
call_10204 = func_6322_call()
func_6669_call = mod.get_global_var('func_6669')
func_6671_call = mutated_mod.get_global_var('func_6671')
call_10223 = func_6669_call()
call_10224 = func_6669_call()
func_7085_call = mod.get_global_var('func_7085')
func_7087_call = mutated_mod.get_global_var('func_7087')
call_10227 = relay.TupleGetItem(func_7085_call(), 0)
call_10228 = relay.TupleGetItem(func_7087_call(), 0)
output = relay.Tuple([call_10203,call_10223,call_10227,])
output2 = relay.Tuple([call_10204,call_10224,call_10228,])
func_10237 = relay.Function([], output)
mod['func_10237'] = func_10237
mod = relay.transform.InferType()(mod)
mutated_mod['func_10237'] = func_10237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10237_call = mutated_mod.get_global_var('func_10237')
call_10238 = func_10237_call()
output = call_10238
func_10239 = relay.Function([], output)
mutated_mod['func_10239'] = func_10239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5580_call = mod.get_global_var('func_5580')
func_5581_call = mutated_mod.get_global_var('func_5581')
call_10276 = func_5580_call()
call_10277 = func_5580_call()
func_6035_call = mod.get_global_var('func_6035')
func_6036_call = mutated_mod.get_global_var('func_6036')
call_10291 = relay.TupleGetItem(func_6035_call(), 0)
call_10292 = relay.TupleGetItem(func_6036_call(), 0)
output = relay.Tuple([call_10276,call_10291,])
output2 = relay.Tuple([call_10277,call_10292,])
func_10298 = relay.Function([], output)
mod['func_10298'] = func_10298
mod = relay.transform.InferType()(mod)
mutated_mod['func_10298'] = func_10298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10298_call = mutated_mod.get_global_var('func_10298')
call_10299 = func_10298_call()
output = call_10299
func_10300 = relay.Function([], output)
mutated_mod['func_10300'] = func_10300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9661_call = mod.get_global_var('func_9661')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_10323 = relay.TupleGetItem(func_9661_call(), 0)
call_10324 = relay.TupleGetItem(func_9663_call(), 0)
output = call_10323
output2 = call_10324
func_10333 = relay.Function([], output)
mod['func_10333'] = func_10333
mod = relay.transform.InferType()(mod)
output = func_10333()
func_10334 = relay.Function([], output)
mutated_mod['func_10334'] = func_10334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10108_call = mod.get_global_var('func_10108')
func_10110_call = mutated_mod.get_global_var('func_10110')
call_10335 = relay.TupleGetItem(func_10108_call(), 0)
call_10336 = relay.TupleGetItem(func_10110_call(), 0)
output = relay.Tuple([call_10335,])
output2 = relay.Tuple([call_10336,])
func_10339 = relay.Function([], output)
mod['func_10339'] = func_10339
mod = relay.transform.InferType()(mod)
mutated_mod['func_10339'] = func_10339
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10339_call = mutated_mod.get_global_var('func_10339')
call_10340 = func_10339_call()
output = call_10340
func_10341 = relay.Function([], output)
mutated_mod['func_10341'] = func_10341
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9143_call = mod.get_global_var('func_9143')
func_9144_call = mutated_mod.get_global_var('func_9144')
call_10361 = relay.TupleGetItem(func_9143_call(), 0)
call_10362 = relay.TupleGetItem(func_9144_call(), 0)
output = relay.Tuple([call_10361,])
output2 = relay.Tuple([call_10362,])
func_10391 = relay.Function([], output)
mod['func_10391'] = func_10391
mod = relay.transform.InferType()(mod)
output = func_10391()
func_10392 = relay.Function([], output)
mutated_mod['func_10392'] = func_10392
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6266_call = mod.get_global_var('func_6266')
func_6268_call = mutated_mod.get_global_var('func_6268')
call_10415 = relay.TupleGetItem(func_6266_call(), 0)
call_10416 = relay.TupleGetItem(func_6268_call(), 0)
func_6385_call = mod.get_global_var('func_6385')
func_6387_call = mutated_mod.get_global_var('func_6387')
call_10443 = relay.TupleGetItem(func_6385_call(), 2)
call_10444 = relay.TupleGetItem(func_6387_call(), 2)
output = relay.Tuple([call_10415,call_10443,])
output2 = relay.Tuple([call_10416,call_10444,])
func_10455 = relay.Function([], output)
mod['func_10455'] = func_10455
mod = relay.transform.InferType()(mod)
output = func_10455()
func_10456 = relay.Function([], output)
mutated_mod['func_10456'] = func_10456
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10467 = relay.var("var_10467", dtype = "bool", shape = (8, 8, 1))#candidate|10467|(8, 8, 1)|var|bool
const_10468 = relay.const([[[True,False,True,True,True,True],[False,False,True,False,False,True],[True,True,False,False,False,True],[False,True,True,False,False,False],[False,True,True,False,True,False],[False,True,False,True,False,True],[True,True,False,False,True,False],[True,False,True,False,False,False]],[[True,True,True,False,True,True],[False,True,False,True,True,False],[True,False,True,True,True,True],[False,False,False,False,False,False],[False,False,False,False,False,True],[False,True,False,True,True,True],[False,True,True,False,False,False],[False,True,False,True,False,False]],[[True,False,False,True,True,True],[True,True,True,False,True,True],[True,True,False,True,False,True],[False,False,False,True,True,False],[False,True,True,False,True,True],[False,False,True,True,True,False],[False,True,False,True,True,True],[False,False,True,False,True,True]],[[True,True,False,True,True,True],[True,True,False,False,True,True],[True,False,True,False,True,True],[True,True,False,True,False,True],[False,False,True,True,False,False],[True,True,True,True,False,False],[False,True,True,False,True,True],[False,False,True,True,False,False]],[[False,True,True,False,False,True],[True,True,True,False,False,True],[False,True,False,False,False,False],[False,False,True,False,True,False],[True,True,False,False,False,False],[False,True,False,True,True,False],[False,True,True,True,True,False],[False,False,True,False,False,False]],[[False,False,False,True,False,True],[True,True,False,True,True,True],[True,True,False,True,False,True],[False,False,False,True,True,False],[True,True,False,True,True,False],[True,True,False,True,False,True],[True,True,False,True,False,False],[False,False,True,False,True,False]],[[False,True,False,False,True,False],[False,False,True,False,True,True],[False,False,False,True,False,True],[False,True,False,False,False,True],[False,True,True,False,True,False],[False,True,False,False,False,True],[False,False,True,False,True,True],[True,True,True,True,False,True]],[[False,False,False,True,True,True],[False,True,False,True,True,True],[True,True,True,True,False,True],[False,False,True,False,False,False],[True,True,False,False,True,False],[False,True,True,False,False,False],[True,False,True,True,True,True],[True,True,False,False,False,False]]], dtype = "bool")#candidate|10468|(8, 8, 6)|const|bool
bop_10469 = relay.logical_and(var_10467.astype('bool'), const_10468.astype('bool')) # shape=(8, 8, 6)
output = relay.Tuple([bop_10469,])
output2 = relay.Tuple([bop_10469,])
func_10472 = relay.Function([var_10467,], output)
mod['func_10472'] = func_10472
mod = relay.transform.InferType()(mod)
mutated_mod['func_10472'] = func_10472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10473 = relay.var("var_10473", dtype = "bool", shape = (8, 8, 1))#candidate|10473|(8, 8, 1)|var|bool
func_10472_call = mutated_mod.get_global_var('func_10472')
call_10474 = func_10472_call(var_10473)
output = call_10474
func_10475 = relay.Function([var_10473], output)
mutated_mod['func_10475'] = func_10475
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5750_call = mod.get_global_var('func_5750')
func_5751_call = mutated_mod.get_global_var('func_5751')
call_10486 = relay.TupleGetItem(func_5750_call(), 1)
call_10487 = relay.TupleGetItem(func_5751_call(), 1)
output = relay.Tuple([call_10486,])
output2 = relay.Tuple([call_10487,])
func_10506 = relay.Function([], output)
mod['func_10506'] = func_10506
mod = relay.transform.InferType()(mod)
mutated_mod['func_10506'] = func_10506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10506_call = mutated_mod.get_global_var('func_10506')
call_10507 = func_10506_call()
output = call_10507
func_10508 = relay.Function([], output)
mutated_mod['func_10508'] = func_10508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9143_call = mod.get_global_var('func_9143')
func_9144_call = mutated_mod.get_global_var('func_9144')
call_10524 = relay.TupleGetItem(func_9143_call(), 0)
call_10525 = relay.TupleGetItem(func_9144_call(), 0)
uop_10536 = relay.cos(call_10524.astype('float32')) # shape=(15, 4, 11)
uop_10538 = relay.cos(call_10525.astype('float32')) # shape=(15, 4, 11)
func_9953_call = mod.get_global_var('func_9953')
func_9956_call = mutated_mod.get_global_var('func_9956')
call_10542 = func_9953_call(relay.reshape(call_10524.astype('bool'), [15, 4, 11]))
call_10543 = func_9953_call(relay.reshape(call_10524.astype('bool'), [15, 4, 11]))
func_6712_call = mod.get_global_var('func_6712')
func_6713_call = mutated_mod.get_global_var('func_6713')
call_10552 = func_6712_call()
call_10553 = func_6712_call()
func_7772_call = mod.get_global_var('func_7772')
func_7774_call = mutated_mod.get_global_var('func_7774')
call_10554 = func_7772_call()
call_10555 = func_7772_call()
output = relay.Tuple([uop_10536,call_10542,call_10552,call_10554,])
output2 = relay.Tuple([uop_10538,call_10543,call_10553,call_10555,])
func_10583 = relay.Function([], output)
mod['func_10583'] = func_10583
mod = relay.transform.InferType()(mod)
mutated_mod['func_10583'] = func_10583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10583_call = mutated_mod.get_global_var('func_10583')
call_10584 = func_10583_call()
output = call_10584
func_10585 = relay.Function([], output)
mutated_mod['func_10585'] = func_10585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9892_call = mod.get_global_var('func_9892')
func_9894_call = mutated_mod.get_global_var('func_9894')
call_10601 = relay.TupleGetItem(func_9892_call(), 2)
call_10602 = relay.TupleGetItem(func_9894_call(), 2)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_10605 = func_1070_call(relay.reshape(call_10601.astype('int32'), [15, 4, 11]))
call_10606 = func_1070_call(relay.reshape(call_10601.astype('int32'), [15, 4, 11]))
func_5759_call = mod.get_global_var('func_5759')
func_5761_call = mutated_mod.get_global_var('func_5761')
var_10628 = relay.var("var_10628", dtype = "bool", shape = (2640,))#candidate|10628|(2640,)|var|bool
call_10627 = relay.TupleGetItem(func_5759_call(relay.reshape(var_10628.astype('bool'), [11, 16, 15])), 0)
call_10629 = relay.TupleGetItem(func_5761_call(relay.reshape(var_10628.astype('bool'), [11, 16, 15])), 0)
uop_10639 = relay.sqrt(call_10627.astype('float32')) # shape=(11, 16, 15)
uop_10641 = relay.sqrt(call_10629.astype('float32')) # shape=(11, 16, 15)
uop_10651 = relay.asin(uop_10639.astype('float64')) # shape=(11, 16, 15)
uop_10653 = relay.asin(uop_10641.astype('float64')) # shape=(11, 16, 15)
output = relay.Tuple([call_10601,call_10605,var_10628,uop_10651,])
output2 = relay.Tuple([call_10602,call_10606,var_10628,uop_10653,])
func_10658 = relay.Function([var_10628,], output)
mod['func_10658'] = func_10658
mod = relay.transform.InferType()(mod)
mutated_mod['func_10658'] = func_10658
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10659 = relay.var("var_10659", dtype = "bool", shape = (2640,))#candidate|10659|(2640,)|var|bool
func_10658_call = mutated_mod.get_global_var('func_10658')
call_10660 = func_10658_call(var_10659)
output = call_10660
func_10661 = relay.Function([var_10659], output)
mutated_mod['func_10661'] = func_10661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_10738 = relay.TupleGetItem(func_7506_call(), 2)
call_10739 = relay.TupleGetItem(func_7507_call(), 2)
func_9831_call = mod.get_global_var('func_9831')
func_9834_call = mutated_mod.get_global_var('func_9834')
var_10775 = relay.var("var_10775", dtype = "int8", shape = ())#candidate|10775|()|var|int8
var_10776 = relay.var("var_10776", dtype = "int8", shape = (40,))#candidate|10776|(40,)|var|int8
call_10774 = relay.TupleGetItem(func_9831_call(relay.reshape(var_10775.astype('int8'), []), relay.reshape(var_10776.astype('int8'), [1, 40]), ), 4)
call_10777 = relay.TupleGetItem(func_9834_call(relay.reshape(var_10775.astype('int8'), []), relay.reshape(var_10776.astype('int8'), [1, 40]), ), 4)
func_5245_call = mod.get_global_var('func_5245')
func_5249_call = mutated_mod.get_global_var('func_5249')
var_10783 = relay.var("var_10783", dtype = "int16", shape = (168, 1))#candidate|10783|(168, 1)|var|int16
var_10784 = relay.var("var_10784", dtype = "float64", shape = (30, 6))#candidate|10784|(30, 6)|var|float64
call_10782 = relay.TupleGetItem(func_5245_call(relay.reshape(var_10783.astype('int16'), [168,]), relay.reshape(var_10784.astype('float64'), [3, 60]), ), 5)
call_10785 = relay.TupleGetItem(func_5249_call(relay.reshape(var_10783.astype('int16'), [168,]), relay.reshape(var_10784.astype('float64'), [3, 60]), ), 5)
func_7062_call = mod.get_global_var('func_7062')
func_7063_call = mutated_mod.get_global_var('func_7063')
call_10789 = relay.TupleGetItem(func_7062_call(), 1)
call_10790 = relay.TupleGetItem(func_7063_call(), 1)
output = relay.Tuple([call_10738,call_10774,var_10775,var_10776,call_10782,var_10783,var_10784,call_10789,])
output2 = relay.Tuple([call_10739,call_10777,var_10775,var_10776,call_10785,var_10783,var_10784,call_10790,])
func_10793 = relay.Function([var_10775,var_10776,var_10783,var_10784,], output)
mod['func_10793'] = func_10793
mod = relay.transform.InferType()(mod)
var_10794 = relay.var("var_10794", dtype = "int8", shape = ())#candidate|10794|()|var|int8
var_10795 = relay.var("var_10795", dtype = "int8", shape = (40,))#candidate|10795|(40,)|var|int8
var_10796 = relay.var("var_10796", dtype = "int16", shape = (168, 1))#candidate|10796|(168, 1)|var|int16
var_10797 = relay.var("var_10797", dtype = "float64", shape = (30, 6))#candidate|10797|(30, 6)|var|float64
output = func_10793(var_10794,var_10795,var_10796,var_10797,)
func_10798 = relay.Function([var_10794,var_10795,var_10796,var_10797,], output)
mutated_mod['func_10798'] = func_10798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_10812 = relay.TupleGetItem(func_7506_call(), 0)
call_10813 = relay.TupleGetItem(func_7507_call(), 0)
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_10814 = relay.TupleGetItem(func_5333_call(), 0)
call_10815 = relay.TupleGetItem(func_5334_call(), 0)
output = relay.Tuple([call_10812,call_10814,])
output2 = relay.Tuple([call_10813,call_10815,])
func_10817 = relay.Function([], output)
mod['func_10817'] = func_10817
mod = relay.transform.InferType()(mod)
output = func_10817()
func_10818 = relay.Function([], output)
mutated_mod['func_10818'] = func_10818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10817_call = mod.get_global_var('func_10817')
func_10818_call = mutated_mod.get_global_var('func_10818')
call_10834 = relay.TupleGetItem(func_10817_call(), 1)
call_10835 = relay.TupleGetItem(func_10818_call(), 1)
func_9354_call = mod.get_global_var('func_9354')
func_9358_call = mutated_mod.get_global_var('func_9358')
const_10837 = relay.const(-6, dtype = "int8")#candidate|10837|()|const|int8
var_10838 = relay.var("var_10838", dtype = "int16", shape = (168,))#candidate|10838|(168,)|var|int16
const_10839 = relay.const([0.687238,6.566620,-1.467826,-6.959499,-6.500518,0.538344,-7.500548,-9.217229,-2.274783,-6.243520,-1.882128,9.775983,-7.981876,-9.217935,6.405151,-6.300964,4.294762,-9.295893,7.389438,-8.614584,2.342676,0.928360,5.815604,-6.310467,7.779764,-7.092922,-6.430820,4.904181,-9.529010,-8.166753,8.340945,-3.221409,-1.710272,-9.577569,2.644588,3.542068,-5.351337,-8.295694,-4.301182,-5.091200,-2.430282,-9.290010,-4.373946,5.741606,5.313899,1.243590,-7.478860,6.977271,-8.130649,-0.010287,-4.388449,-1.803135,2.122753,-3.705292,1.588424,6.060789,2.433201,-9.314779,8.233602,-4.366280,6.616302,4.136387,1.942949,-3.638678,-0.563118,-1.992960,1.438553,-0.222039,4.423142,-9.313951,0.199694,-3.677086,4.044032,-8.258897,4.018710,9.822602,-3.345609,-6.809100,9.461287,9.370222,-0.916285,3.164845,-2.707065,-5.562776,-6.903278,2.426027,-0.338751,7.292658,-9.407769,1.415545,-2.671341,9.471848,7.481402,3.096584,-4.854626,3.764585,-0.798177,-9.203858,-1.755998,-6.213899,-4.642019,-3.987505,-2.193112,-5.798522,0.722714,-2.230123,4.314016,9.549343,8.415718,6.609914,6.162268,-8.164208,6.774114,6.190152,7.385315,6.292933,5.338492,6.284446,0.785173,-6.074596,0.017072,-6.602881,-8.740846,7.358596,-6.803270,-6.404098,2.815703,2.837997,1.870116,-9.234410,4.265643,-7.041375,5.863438,-4.880923,-3.902955,-9.700090,5.785428,-0.950780,-2.864962,6.253465,-6.966518,-9.024406,7.705148,0.398154,-2.621232,4.249723,9.659633,-9.906001,5.857076,5.766863,-6.570615,6.700565,-9.841384,8.648590,-7.659372,-8.026324,-9.349486,-0.632765,-6.968183,0.255672,-9.332898,-9.972038,-0.247329,-4.548313,0.245970,3.788352,2.334471,3.199802,-6.431239,-4.874596,-5.678239,-7.440323,-2.997993,-6.699140,-3.834815,3.479052,-0.610666,-8.792561,3.731581,6.917814], dtype = "float64")#candidate|10839|(180,)|const|float64
call_10836 = relay.TupleGetItem(func_9354_call(relay.reshape(const_10837.astype('int8'), []), relay.reshape(var_10838.astype('int16'), [168,]), relay.reshape(const_10839.astype('float64'), [180,]), ), 7)
call_10840 = relay.TupleGetItem(func_9358_call(relay.reshape(const_10837.astype('int8'), []), relay.reshape(var_10838.astype('int16'), [168,]), relay.reshape(const_10839.astype('float64'), [180,]), ), 7)
func_9796_call = mod.get_global_var('func_9796')
func_9800_call = mutated_mod.get_global_var('func_9800')
const_10846 = relay.const([4.666100,-4.708812,0.851054,-7.883277,5.552000,-5.566032,-8.143546,-6.935587,-8.206501,-0.793301,4.009884,1.355168,-8.831317,-2.626673,-5.225893,-1.908112,7.746693,4.802225,0.001711,-3.088571,-8.230936,7.404577,2.294688,9.169556,-3.174929,-7.873216,-3.984351,-5.233751,1.210837,-8.328556,-6.068688,-4.763316,-7.529612,-3.772460,2.196080,-6.094554,7.945807,-6.836057,-8.298794,-0.612003,2.459783,-5.730800,-0.089810,1.342929,7.883795,-8.675459,-6.961818,-2.598466,-6.260375,-1.013428,1.576819,-1.921539,-3.851482,8.413561,-2.597493,7.237266,-5.423468,0.540357,8.250198,7.696269,-7.546750,-0.046155,-6.819760,7.864733,4.321234,-5.774001,3.711469,-1.494772,-7.804127,-3.200247,1.054123,-8.651592,6.955085,2.372690,-5.591378,-2.380778,-5.745762,5.082432,6.469413,6.789444,-9.632674,0.214839,-1.317681,0.925279,-8.319762,1.240205,-9.660717,0.389310,1.082416,-0.454251,6.323529,6.068880,7.729181,-4.344715,2.549674,6.845535,-2.692661,1.170681,-2.076589,4.892738,-7.629520,6.190098,-4.635646,7.706329,3.961570,-2.026241,-8.499826,-5.704145,-8.884951,-5.416853,-8.731894,-2.448431,-0.430965,-1.097877,-4.798413,8.364752,-7.591921,6.437743,-7.592535,1.177405,-1.645645,-7.740845,1.019814,-2.724751,-4.186750,2.013376,2.079660,6.719367,-0.464731,-8.912856,4.992279,9.430570,-8.544667,-8.219905,0.179485,-3.422829,7.719409,-7.854145,8.896462,6.549941,9.007826,2.536702,-2.930085,9.829360,-2.482285,8.877011,5.333733,9.399035,-4.843143,-5.619680,6.870288,2.770886,-4.930953,7.071420,8.192443,4.597184,-1.119447,0.519108,6.710003,0.164857,-8.085154,2.418674,3.894564,-7.167709,-6.531692,-5.397348,2.191573,3.278371,3.750833,-4.650512,3.541522,-9.200042,-8.488961,-5.530837,-1.146372,8.652756,-2.107026,-4.693728,2.245780,6.576772,-8.288534,-2.374052,-1.486309,9.005796,-2.476115,-9.343633,9.745788,3.324840,-6.947987,7.908717,4.892562,8.675970,1.520466,-2.350003,-3.811450,-1.919839,2.114207,4.460503,-1.295025,5.951801,-9.599183,-2.420815,-0.650534,9.199240,3.095531,4.370216,6.512037,3.022644,0.211595,0.378204,8.391889,-4.262379,-6.922139,-7.914034,-1.760443,-9.088043,0.147908,-6.872828,-9.027991,-2.600889,-3.810618,6.900302,3.409506,-3.431918,-9.430978,-2.047177,9.863794,-9.356197,-7.987275,0.328563,-6.902801,3.583380,-2.005207,-2.361791,2.622333,4.841206,-1.424978,6.184050,3.670221,-5.964984,-7.782486,6.432167,0.943232,9.646157,0.479864,-3.629748,-5.380565,3.745649,4.925069,-9.051238,3.181318,-7.807212,-9.173564,1.484394,8.901699,9.255341,-8.780293,-8.348398,-2.713635,-3.535665,-0.609659,9.611758,-6.224679,5.062503,-8.725768,5.024831,1.921875,-0.352717,5.595363,2.743254,6.317126,-3.822068,-8.342675,-3.706030,9.228018,-3.409013,4.995164,-7.739629,-0.829049,-1.735637,7.604250,-3.405965,3.945992,-9.355011,-4.840225,-7.390813,-1.047046,-6.481761,5.241386,2.558599,0.792359,-6.427785,-1.415217,-3.239207,-2.241318,5.537153,-6.869735,6.116447,-9.715386,6.753182,1.401220,9.808425,-0.054795,-3.090791,-9.858248,-6.967400,1.850992,-3.370807,-4.516648,9.448359,1.314433,-9.726812,-6.557258,-0.063976,-4.974493,-2.274070,6.927191,5.038516,6.552863,9.306955,-5.987280,7.556449,-5.575962,6.919088,-4.727901,3.702037,7.558126,-5.390109,7.788729,3.962476,-3.702512,-2.268105,1.806557,1.726066,0.374261,-7.749167,3.114118,-1.991854,5.157763,-5.344267,-0.236119,-8.052231,4.302844,7.923116,1.966052,-9.066602,-4.215931,5.909020,2.609556,-1.679670,5.872215,-0.779632,-4.600521,-1.617171,-2.609407,-6.881546,-5.328744,-5.082960,8.502677,6.946712,-7.278882,-1.981004,-3.036010,-2.366655,-2.308526,-9.631778,0.935532,-3.584323,2.908902,-9.569270,9.930461,-5.160667,6.444087,-5.319262,5.975798,8.114248,3.738388,-2.176159,9.364318,8.676914,-3.651521,2.051543,-1.286173,4.053298,-0.562394,0.289251,-1.350432,4.353753,9.590795,-8.470074,3.300164,-6.421035,0.247216,-7.069151,-4.423525,8.578644,-1.173760,-0.176136,-4.187769,-4.477056,0.777637,0.199195,-1.678850,6.493348,-4.304057,-8.829441,3.809275,-0.016880,4.874073,3.687497,9.116820,-1.112600,1.854246,-9.218243,9.501698,-6.942535,5.413468,-7.635893,1.267445,2.013153,-4.293476,4.105435,-9.026049,-4.564787,9.637823,9.430782,-6.531798,-6.257937,7.450372,-8.876635,9.182298,8.991934,-7.503324,-2.607523,-8.031558,5.885533,3.388138,-1.030775,-6.049553,-7.384539,1.702020,-6.955911,7.232365,6.892225,-2.352101,9.062179,9.753652,-5.072973,6.235235,2.477057,-6.294014,-3.177060,9.345618,7.230115,7.539987,5.652293,-6.223919,4.901254,-7.485402,-2.952071,-9.250791,0.788853], dtype = "float32")#candidate|10846|(462,)|const|float32
var_10847 = relay.var("var_10847", dtype = "float32", shape = (35,))#candidate|10847|(35,)|var|float32
call_10845 = relay.TupleGetItem(func_9796_call(relay.reshape(const_10846.astype('float32'), [462,]), relay.reshape(var_10847.astype('float32'), [35, 1]), ), 3)
call_10848 = relay.TupleGetItem(func_9800_call(relay.reshape(const_10846.astype('float32'), [462,]), relay.reshape(var_10847.astype('float32'), [35, 1]), ), 3)
output = relay.Tuple([call_10834,call_10836,const_10837,var_10838,const_10839,call_10845,const_10846,var_10847,])
output2 = relay.Tuple([call_10835,call_10840,const_10837,var_10838,const_10839,call_10848,const_10846,var_10847,])
func_10853 = relay.Function([var_10838,var_10847,], output)
mod['func_10853'] = func_10853
mod = relay.transform.InferType()(mod)
var_10854 = relay.var("var_10854", dtype = "int16", shape = (168,))#candidate|10854|(168,)|var|int16
var_10855 = relay.var("var_10855", dtype = "float32", shape = (35,))#candidate|10855|(35,)|var|float32
output = func_10853(var_10854,var_10855,)
func_10856 = relay.Function([var_10854,var_10855,], output)
mutated_mod['func_10856'] = func_10856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6580_call = mod.get_global_var('func_6580')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_10864 = relay.TupleGetItem(func_6580_call(), 0)
call_10865 = relay.TupleGetItem(func_6581_call(), 0)
output = call_10864
output2 = call_10865
func_10883 = relay.Function([], output)
mod['func_10883'] = func_10883
mod = relay.transform.InferType()(mod)
mutated_mod['func_10883'] = func_10883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10883_call = mutated_mod.get_global_var('func_10883')
call_10884 = func_10883_call()
output = call_10884
func_10885 = relay.Function([], output)
mutated_mod['func_10885'] = func_10885
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11001 = relay.var("var_11001", dtype = "int8", shape = (16, 9, 11))#candidate|11001|(16, 9, 11)|var|int8
const_11002 = relay.const([[[-10,3,1,-1,-2,-5,6,3,4,-8,-2],[-10,-2,-6,6,5,10,1,-7,4,-7,-10],[-6,-10,1,-3,-5,-10,1,-2,-7,-10,4],[8,-4,-3,-1,5,-5,10,-3,9,-7,-4],[6,-3,4,-9,7,-2,-10,-3,5,10,10],[-6,-4,2,-5,-8,-4,-3,6,-9,-9,-5],[3,4,5,9,-6,2,-9,9,-1,-4,-10],[5,9,1,2,-7,-6,-6,6,10,-2,10],[-5,7,6,10,8,-3,9,3,2,10,-2]],[[2,-2,8,3,7,-6,5,-6,7,-10,9],[4,3,-3,-7,7,-2,2,-5,9,4,-6],[7,-1,4,-7,-3,6,-1,8,5,-7,-8],[-9,3,-7,-3,-3,-7,-9,10,-5,-6,-8],[1,5,3,2,-1,6,-1,9,6,-6,-8],[5,10,-10,10,-5,6,-6,4,-2,-1,8],[-9,-5,1,-9,8,-7,-3,-5,5,-3,-2],[1,7,10,2,-9,5,8,-9,4,-1,6],[-8,-9,2,7,3,7,-3,-9,5,6,3]],[[-5,-10,-10,2,7,6,4,-7,10,-8,1],[6,-4,9,-2,-3,7,-7,-4,-2,10,6],[5,-4,-5,-6,4,8,6,10,-2,-6,-6],[-7,-4,3,8,-10,5,2,6,8,-3,-10],[6,6,4,-8,-4,3,5,-4,7,7,-7],[6,8,-5,-2,9,-6,-5,-6,-1,7,10],[1,-4,9,-2,2,-10,-10,3,-10,10,-7],[6,-10,-6,2,9,-4,-2,4,-7,-10,9],[2,3,-6,9,10,9,-4,-6,-2,10,6]],[[7,3,-10,-1,-4,3,-4,-2,2,-10,-3],[5,1,-2,5,2,-2,8,-10,1,1,-3],[2,-9,9,-3,-4,-10,8,-5,-4,5,-3],[-7,1,7,3,10,-5,-8,-10,5,-1,-10],[-8,2,-3,-7,-1,7,4,7,-2,-3,-7],[1,5,-3,2,-5,-8,2,5,6,-6,9],[7,-9,10,7,-6,7,4,-8,-3,5,-2],[-5,-8,5,5,4,-8,2,7,-9,8,2],[6,-6,-3,-2,-2,3,7,-4,4,6,-2]],[[-1,-10,2,6,9,4,-3,-10,3,10,-2],[6,9,7,-3,4,10,6,-1,5,-6,-9],[5,2,1,-8,8,2,-5,3,-8,1,2],[-9,10,6,1,5,-5,8,10,1,-1,7],[2,1,8,9,1,-4,-1,9,4,-10,2],[6,-3,1,-10,9,8,-5,3,-8,-1,7],[3,-4,1,-7,-3,6,10,9,6,3,9],[10,-1,8,1,5,-1,-4,-2,-7,5,-10],[-1,-6,-8,-10,-6,-1,-1,2,6,7,-6]],[[-2,-1,5,4,-1,-8,-3,6,5,6,-3],[-7,-6,-2,-2,5,1,5,-1,3,4,-9],[-10,-2,8,-1,2,8,2,-2,-10,-10,-4],[9,4,9,5,-6,-4,-10,-4,-5,-10,6],[-5,-8,-7,8,-3,-7,10,4,-6,10,9],[-6,10,3,6,-2,10,-6,10,8,-10,10],[-3,-5,7,10,-3,2,10,3,-5,-9,-7],[-1,8,10,-4,-5,-7,5,6,-1,-4,4],[8,-3,2,-7,-4,6,8,9,-6,-1,7]],[[-6,-3,-3,10,2,5,-1,7,8,8,5],[-9,8,-1,10,-4,4,-3,-6,-4,-3,6],[-8,3,6,7,7,-6,-3,7,8,10,-1],[-8,-10,-9,-3,-8,-8,6,-4,7,-3,10],[1,-9,-9,2,-4,8,5,6,10,1,-6],[-6,-4,-4,6,-10,1,8,10,9,10,-9],[-3,-7,10,-5,-6,9,-3,-4,-8,6,6],[1,-3,2,-8,-10,-8,7,4,-8,-4,10],[-1,6,1,-1,5,-4,2,10,9,-4,5]],[[-8,-5,9,3,-7,-4,-6,-3,1,-8,-4],[3,10,-6,-2,6,-1,-6,8,-10,6,8],[-8,-8,8,-5,4,-10,3,-1,-6,7,-7],[8,4,2,1,-1,-10,-7,7,-5,-4,-7],[9,-2,-6,4,1,9,-9,5,-1,-6,-7],[1,9,-5,9,7,-2,6,-7,-1,2,4],[-1,1,7,-2,2,-8,-9,1,-9,-9,9],[-8,6,7,-9,9,-9,-1,8,1,-7,1],[4,-8,-4,5,-10,2,-2,6,-7,3,-5]],[[-2,-8,-3,2,2,9,10,-5,-5,-7,5],[-5,5,5,-9,10,3,2,2,-3,-1,-4],[-4,-5,-8,-7,6,-3,5,6,-8,3,4],[-1,-1,-3,-7,-5,-8,1,7,-8,-9,1],[-8,-7,-5,2,-10,-8,-7,5,-7,-2,-3],[10,10,-10,-10,-4,1,-7,-6,6,9,-6],[4,-10,-2,-8,7,2,8,8,-4,-6,-8],[1,-1,-7,-2,1,-4,9,-3,-2,6,8],[7,-2,10,8,-5,9,8,8,-1,-8,-10]],[[-3,-5,-3,-9,7,-7,-9,-8,-5,3,-9],[-2,-3,-8,9,7,10,7,4,-6,-5,1],[2,-8,2,-8,4,-2,2,7,7,-3,7],[2,-9,-4,1,-6,-7,-7,8,2,7,1],[3,1,2,-8,-8,-4,-9,1,6,-1,4],[1,-7,-5,6,-6,-4,10,-2,6,-9,7],[9,-7,5,-5,8,-10,9,-9,-3,-8,3],[2,-6,-5,9,4,10,-2,-9,-6,4,-4],[-3,-2,10,-3,7,8,6,-10,-7,-4,6]],[[-6,4,4,7,-5,-2,7,6,-7,-7,-6],[-10,9,-1,-8,10,3,-5,-4,-6,-3,3],[-2,-1,-1,4,3,-6,-3,7,5,5,-1],[-7,-3,1,1,7,4,2,8,5,-10,-6],[-7,2,8,9,8,-2,7,6,-9,3,10],[-1,1,-10,6,-2,8,-4,-1,-6,9,9],[-3,-5,-7,8,-4,-8,6,4,5,-6,1],[-9,-2,-5,-3,6,9,-8,10,8,8,8],[5,7,-1,-4,4,-9,6,-9,6,5,-9]],[[-6,1,-4,9,5,8,-7,-7,-3,2,-9],[-4,9,6,-7,-1,5,-6,-2,-4,2,-9],[1,8,8,4,2,6,7,-9,8,-9,1],[3,-10,-8,-9,1,-4,-3,-3,-10,4,8],[9,-8,-7,-9,2,-10,6,-5,9,-4,7],[5,-4,-4,-2,-2,10,-7,8,-5,-5,3],[7,8,-3,6,2,1,8,-6,8,1,-1],[6,2,8,-10,-1,-8,-10,-3,-5,2,3],[-1,-10,1,8,-8,9,-10,9,9,-7,-9]],[[10,-7,-1,8,7,-4,-8,-8,7,5,-6],[-5,4,-5,1,-10,-9,5,-6,-3,4,-9],[6,-1,3,-1,10,6,-9,7,-6,-2,-3],[-3,2,1,-7,8,-10,-6,-4,4,2,2],[-10,3,7,8,-2,1,1,8,4,1,5],[-9,-2,-7,-4,6,-9,9,-4,-7,10,-10],[10,8,4,-2,-7,-1,5,-3,-6,-4,-10],[10,1,-8,-5,-3,6,9,-3,2,3,10],[1,8,4,4,-4,-8,4,-6,-4,-2,-2]],[[-4,-3,6,-10,-3,-10,10,-10,8,1,-8],[1,1,-7,-10,5,6,10,5,8,3,-8],[2,7,3,7,2,7,7,-6,5,-3,-1],[-2,-5,4,-8,10,10,3,7,5,10,-1],[-8,-6,-2,3,-3,10,5,5,6,-5,-3],[10,-8,7,8,7,-9,-10,-3,4,8,-2],[-2,8,2,-6,10,5,2,-6,-4,-10,-7],[5,1,-3,-5,-4,4,5,-3,-3,9,-3],[-3,-5,3,1,-4,-7,8,-8,7,-10,-3]],[[-6,-7,1,8,1,2,-10,1,-4,-2,2],[1,2,1,8,10,10,5,-7,5,6,-2],[-4,-2,10,9,1,-3,7,-9,-7,1,8],[1,10,-1,-5,7,-8,8,-2,-9,9,7],[5,1,5,-1,9,-6,2,-7,10,6,10],[3,3,4,3,7,7,10,-1,5,-7,-9],[8,-5,8,8,7,2,5,-1,-9,-4,6],[10,-9,7,6,4,-2,4,-10,9,-4,-9],[-7,5,9,-2,-7,4,7,-1,-9,-7,-4]],[[10,1,-1,-10,-4,-1,3,-10,6,-9,-3],[-4,-9,9,-6,7,7,7,3,-10,-4,-7],[10,-6,-5,9,-1,-4,5,-6,-6,-7,3],[1,-1,2,-2,6,6,-10,-7,3,-1,-8],[-2,-7,9,1,10,-7,-5,-10,-10,2,-10],[-1,1,-5,-2,-9,1,-1,4,2,8,-8],[-10,1,-7,-8,-5,-6,-2,9,5,-6,-5],[-7,-3,-4,-8,-1,1,8,4,6,4,6],[-2,2,2,-4,-7,8,9,8,-4,-8,2]]], dtype = "int8")#candidate|11002|(16, 9, 11)|const|int8
bop_11003 = relay.left_shift(var_11001.astype('int8'), relay.reshape(const_11002.astype('int8'), relay.shape_of(var_11001))) # shape=(16, 9, 11)
output = relay.Tuple([bop_11003,])
output2 = relay.Tuple([bop_11003,])
func_11009 = relay.Function([var_11001,], output)
mod['func_11009'] = func_11009
mod = relay.transform.InferType()(mod)
mutated_mod['func_11009'] = func_11009
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11010 = relay.var("var_11010", dtype = "int8", shape = (16, 9, 11))#candidate|11010|(16, 9, 11)|var|int8
func_11009_call = mutated_mod.get_global_var('func_11009')
call_11011 = func_11009_call(var_11010)
output = call_11011
func_11012 = relay.Function([var_11010], output)
mutated_mod['func_11012'] = func_11012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4770_call = mod.get_global_var('func_4770')
func_4772_call = mutated_mod.get_global_var('func_4772')
call_11091 = relay.TupleGetItem(func_4770_call(), 0)
call_11092 = relay.TupleGetItem(func_4772_call(), 0)
func_10817_call = mod.get_global_var('func_10817')
func_10818_call = mutated_mod.get_global_var('func_10818')
call_11101 = relay.TupleGetItem(func_10817_call(), 1)
call_11102 = relay.TupleGetItem(func_10818_call(), 1)
func_9892_call = mod.get_global_var('func_9892')
func_9894_call = mutated_mod.get_global_var('func_9894')
call_11107 = relay.TupleGetItem(func_9892_call(), 2)
call_11108 = relay.TupleGetItem(func_9894_call(), 2)
output = relay.Tuple([call_11091,call_11101,call_11107,])
output2 = relay.Tuple([call_11092,call_11102,call_11108,])
func_11111 = relay.Function([], output)
mod['func_11111'] = func_11111
mod = relay.transform.InferType()(mod)
output = func_11111()
func_11112 = relay.Function([], output)
mutated_mod['func_11112'] = func_11112
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11160 = relay.var("var_11160", dtype = "float32", shape = (8, 6, 1))#candidate|11160|(8, 6, 1)|var|float32
uop_11161 = relay.atan(var_11160.astype('float32')) # shape=(8, 6, 1)
uop_11190 = relay.log(var_11160.astype('float64')) # shape=(8, 6, 1)
output = relay.Tuple([uop_11161,uop_11190,])
output2 = relay.Tuple([uop_11161,uop_11190,])
func_11197 = relay.Function([var_11160,], output)
mod['func_11197'] = func_11197
mod = relay.transform.InferType()(mod)
var_11198 = relay.var("var_11198", dtype = "float32", shape = (8, 6, 1))#candidate|11198|(8, 6, 1)|var|float32
output = func_11197(var_11198)
func_11199 = relay.Function([var_11198], output)
mutated_mod['func_11199'] = func_11199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7772_call = mod.get_global_var('func_7772')
func_7774_call = mutated_mod.get_global_var('func_7774')
call_11208 = func_7772_call()
call_11209 = func_7772_call()
output = call_11208
output2 = call_11209
func_11212 = relay.Function([], output)
mod['func_11212'] = func_11212
mod = relay.transform.InferType()(mod)
output = func_11212()
func_11213 = relay.Function([], output)
mutated_mod['func_11213'] = func_11213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7772_call = mod.get_global_var('func_7772')
func_7774_call = mutated_mod.get_global_var('func_7774')
call_11281 = func_7772_call()
call_11282 = func_7772_call()
func_6399_call = mod.get_global_var('func_6399')
func_6401_call = mutated_mod.get_global_var('func_6401')
call_11286 = relay.TupleGetItem(func_6399_call(), 0)
call_11287 = relay.TupleGetItem(func_6401_call(), 0)
func_3988_call = mod.get_global_var('func_3988')
func_3990_call = mutated_mod.get_global_var('func_3990')
var_11307 = relay.var("var_11307", dtype = "float32", shape = (390,))#candidate|11307|(390,)|var|float32
call_11306 = relay.TupleGetItem(func_3988_call(relay.reshape(var_11307.astype('float32'), [390,])), 1)
call_11308 = relay.TupleGetItem(func_3990_call(relay.reshape(var_11307.astype('float32'), [390,])), 1)
func_6669_call = mod.get_global_var('func_6669')
func_6671_call = mutated_mod.get_global_var('func_6671')
call_11309 = func_6669_call()
call_11310 = func_6669_call()
output = relay.Tuple([call_11281,call_11286,call_11306,var_11307,call_11309,])
output2 = relay.Tuple([call_11282,call_11287,call_11308,var_11307,call_11310,])
func_11317 = relay.Function([var_11307,], output)
mod['func_11317'] = func_11317
mod = relay.transform.InferType()(mod)
var_11318 = relay.var("var_11318", dtype = "float32", shape = (390,))#candidate|11318|(390,)|var|float32
output = func_11317(var_11318)
func_11319 = relay.Function([var_11318], output)
mutated_mod['func_11319'] = func_11319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11433 = relay.var("var_11433", dtype = "int8", shape = ())#candidate|11433|()|var|int8
var_11434 = relay.var("var_11434", dtype = "int8", shape = (1, 2, 4))#candidate|11434|(1, 2, 4)|var|int8
bop_11435 = relay.logical_xor(var_11433.astype('int8'), var_11434.astype('int8')) # shape=(1, 2, 4)
uop_11449 = relay.asin(var_11434.astype('float64')) # shape=(1, 2, 4)
func_8029_call = mod.get_global_var('func_8029')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_11452 = relay.TupleGetItem(func_8029_call(), 0)
call_11453 = relay.TupleGetItem(func_8030_call(), 0)
output = relay.Tuple([bop_11435,uop_11449,call_11452,])
output2 = relay.Tuple([bop_11435,uop_11449,call_11453,])
func_11454 = relay.Function([var_11433,var_11434,], output)
mod['func_11454'] = func_11454
mod = relay.transform.InferType()(mod)
mutated_mod['func_11454'] = func_11454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11454_call = mutated_mod.get_global_var('func_11454')
var_11456 = relay.var("var_11456", dtype = "int8", shape = ())#candidate|11456|()|var|int8
var_11457 = relay.var("var_11457", dtype = "int8", shape = (1, 2, 4))#candidate|11457|(1, 2, 4)|var|int8
call_11455 = func_11454_call(var_11456,var_11457,)
output = call_11455
func_11458 = relay.Function([var_11456,var_11457,], output)
mutated_mod['func_11458'] = func_11458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7241_call = mod.get_global_var('func_7241')
func_7243_call = mutated_mod.get_global_var('func_7243')
call_11483 = func_7241_call()
call_11484 = func_7241_call()
output = relay.Tuple([call_11483,])
output2 = relay.Tuple([call_11484,])
func_11492 = relay.Function([], output)
mod['func_11492'] = func_11492
mod = relay.transform.InferType()(mod)
output = func_11492()
func_11493 = relay.Function([], output)
mutated_mod['func_11493'] = func_11493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10333_call = mod.get_global_var('func_10333')
func_10334_call = mutated_mod.get_global_var('func_10334')
call_11497 = func_10333_call()
call_11498 = func_10333_call()
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_11505 = relay.TupleGetItem(func_4821_call(), 1)
call_11506 = relay.TupleGetItem(func_4822_call(), 1)
output = relay.Tuple([call_11497,call_11505,])
output2 = relay.Tuple([call_11498,call_11506,])
func_11507 = relay.Function([], output)
mod['func_11507'] = func_11507
mod = relay.transform.InferType()(mod)
mutated_mod['func_11507'] = func_11507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11507_call = mutated_mod.get_global_var('func_11507')
call_11508 = func_11507_call()
output = call_11508
func_11509 = relay.Function([], output)
mutated_mod['func_11509'] = func_11509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11507_call = mod.get_global_var('func_11507')
func_11509_call = mutated_mod.get_global_var('func_11509')
call_11512 = relay.TupleGetItem(func_11507_call(), 1)
call_11513 = relay.TupleGetItem(func_11509_call(), 1)
uop_11514 = relay.acos(call_11512.astype('float32')) # shape=(15, 4, 11)
uop_11516 = relay.acos(call_11513.astype('float32')) # shape=(15, 4, 11)
output = uop_11514
output2 = uop_11516
func_11542 = relay.Function([], output)
mod['func_11542'] = func_11542
mod = relay.transform.InferType()(mod)
output = func_11542()
func_11543 = relay.Function([], output)
mutated_mod['func_11543'] = func_11543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10883_call = mod.get_global_var('func_10883')
func_10885_call = mutated_mod.get_global_var('func_10885')
call_11573 = func_10883_call()
call_11574 = func_10883_call()
output = call_11573
output2 = call_11574
func_11577 = relay.Function([], output)
mod['func_11577'] = func_11577
mod = relay.transform.InferType()(mod)
mutated_mod['func_11577'] = func_11577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11577_call = mutated_mod.get_global_var('func_11577')
call_11578 = func_11577_call()
output = call_11578
func_11579 = relay.Function([], output)
mutated_mod['func_11579'] = func_11579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9693_call = mod.get_global_var('func_9693')
func_9694_call = mutated_mod.get_global_var('func_9694')
call_11583 = func_9693_call()
call_11584 = func_9693_call()
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_11597 = relay.TupleGetItem(func_5147_call(), 0)
call_11598 = relay.TupleGetItem(func_5149_call(), 0)
output = relay.Tuple([call_11583,call_11597,])
output2 = relay.Tuple([call_11584,call_11598,])
func_11620 = relay.Function([], output)
mod['func_11620'] = func_11620
mod = relay.transform.InferType()(mod)
mutated_mod['func_11620'] = func_11620
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11620_call = mutated_mod.get_global_var('func_11620')
call_11621 = func_11620_call()
output = call_11621
func_11622 = relay.Function([], output)
mutated_mod['func_11622'] = func_11622
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11638 = relay.var("var_11638", dtype = "float64", shape = (13, 11, 4))#candidate|11638|(13, 11, 4)|var|float64
uop_11639 = relay.log2(var_11638.astype('float64')) # shape=(13, 11, 4)
output = relay.Tuple([uop_11639,])
output2 = relay.Tuple([uop_11639,])
func_11650 = relay.Function([var_11638,], output)
mod['func_11650'] = func_11650
mod = relay.transform.InferType()(mod)
var_11651 = relay.var("var_11651", dtype = "float64", shape = (13, 11, 4))#candidate|11651|(13, 11, 4)|var|float64
output = func_11650(var_11651)
func_11652 = relay.Function([var_11651], output)
mutated_mod['func_11652'] = func_11652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11111_call = mod.get_global_var('func_11111')
func_11112_call = mutated_mod.get_global_var('func_11112')
call_11662 = relay.TupleGetItem(func_11111_call(), 1)
call_11663 = relay.TupleGetItem(func_11112_call(), 1)
func_4821_call = mod.get_global_var('func_4821')
func_4822_call = mutated_mod.get_global_var('func_4822')
call_11682 = relay.TupleGetItem(func_4821_call(), 1)
call_11683 = relay.TupleGetItem(func_4822_call(), 1)
func_7085_call = mod.get_global_var('func_7085')
func_7087_call = mutated_mod.get_global_var('func_7087')
call_11689 = relay.TupleGetItem(func_7085_call(), 1)
call_11690 = relay.TupleGetItem(func_7087_call(), 1)
func_8151_call = mod.get_global_var('func_8151')
func_8152_call = mutated_mod.get_global_var('func_8152')
call_11691 = func_8151_call()
call_11692 = func_8151_call()
output = relay.Tuple([call_11662,call_11682,call_11689,call_11691,])
output2 = relay.Tuple([call_11663,call_11683,call_11690,call_11692,])
func_11696 = relay.Function([], output)
mod['func_11696'] = func_11696
mod = relay.transform.InferType()(mod)
output = func_11696()
func_11697 = relay.Function([], output)
mutated_mod['func_11697'] = func_11697
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11746 = relay.var("var_11746", dtype = "float64", shape = (4, 4, 12))#candidate|11746|(4, 4, 12)|var|float64
const_11747 = relay.const([[[-3.680916,-5.266246,6.352649,7.889488,3.931053,9.213377,0.142473,7.771817,-2.014772,-3.209900,-5.529523,-9.529310],[6.211742,4.550917,9.356035,-1.759193,-1.449821,-7.783848,-8.546402,0.329069,9.356359,4.212018,-2.152142,0.784436],[-7.030956,8.254931,7.262411,4.329191,-1.163102,-6.829046,-6.188260,-7.964860,1.643304,-0.862518,-6.253574,-9.430022],[-6.538452,6.611469,-9.366019,4.843254,-0.753157,5.611845,5.252325,-9.592967,4.074495,5.919968,3.707232,1.737500]],[[-1.790161,-7.609015,9.211595,-6.732069,3.204678,-9.662884,3.415207,-2.629857,-8.396450,8.124518,-6.894473,-9.035627],[-7.199995,2.824511,5.535323,-6.506983,4.967426,-9.518196,9.661768,-9.001975,-8.171240,-3.310547,3.889351,2.064186],[-1.196843,4.109232,-8.384192,1.507984,5.097721,3.875291,9.932235,-8.867929,-6.366091,1.282495,0.985536,-8.269619],[-2.470623,8.918503,8.077773,6.339574,7.480265,3.891237,-2.873279,-2.942765,7.441459,-3.792678,-5.137625,6.554344]],[[-0.415812,-9.277959,8.235841,0.707002,-1.220035,0.484429,-5.543550,4.929442,4.200628,9.080434,6.385500,3.565976],[8.447236,5.224743,-0.278721,4.928812,7.869448,-7.902505,-4.702371,-0.014875,0.427504,4.256374,4.420686,4.101159],[2.967066,-7.146806,1.410312,5.166741,-8.398272,-7.322625,-0.923838,9.435968,8.796054,-7.795998,0.302749,-0.192486],[-3.883877,-8.878782,4.933670,-5.009915,6.470766,6.937026,-3.068469,6.209178,-3.549163,4.849172,4.943321,-3.074641]],[[-3.609587,5.568452,-6.991866,-1.139255,7.862801,-9.522784,4.700244,6.800107,7.759772,3.440067,5.634061,-8.968972],[-5.990326,-4.448021,-7.737801,-8.771128,2.126665,1.723348,-1.803662,-0.932728,-7.845250,-0.539567,3.419706,-9.169355],[-0.809564,-1.928207,6.192569,2.706346,-1.387450,1.017845,7.414426,-2.243732,2.587810,-3.256381,9.800468,6.077170],[6.477269,3.133569,9.462717,8.503290,6.860927,-6.033049,0.050685,-2.136756,3.986320,-9.853141,-7.189173,-9.994595]]], dtype = "float64")#candidate|11747|(4, 4, 12)|const|float64
bop_11748 = relay.floor_mod(var_11746.astype('float64'), relay.reshape(const_11747.astype('float64'), relay.shape_of(var_11746))) # shape=(4, 4, 12)
uop_11751 = relay.erf(bop_11748.astype('float64')) # shape=(4, 4, 12)
output = relay.Tuple([uop_11751,])
output2 = relay.Tuple([uop_11751,])
func_11771 = relay.Function([var_11746,], output)
mod['func_11771'] = func_11771
mod = relay.transform.InferType()(mod)
mutated_mod['func_11771'] = func_11771
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11772 = relay.var("var_11772", dtype = "float64", shape = (4, 4, 12))#candidate|11772|(4, 4, 12)|var|float64
func_11771_call = mutated_mod.get_global_var('func_11771')
call_11773 = func_11771_call(var_11772)
output = call_11773
func_11774 = relay.Function([var_11772], output)
mutated_mod['func_11774'] = func_11774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11785 = relay.var("var_11785", dtype = "float64", shape = (3, 6, 16))#candidate|11785|(3, 6, 16)|var|float64
uop_11786 = relay.log(var_11785.astype('float64')) # shape=(3, 6, 16)
output = relay.Tuple([uop_11786,])
output2 = relay.Tuple([uop_11786,])
func_11794 = relay.Function([var_11785,], output)
mod['func_11794'] = func_11794
mod = relay.transform.InferType()(mod)
mutated_mod['func_11794'] = func_11794
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11795 = relay.var("var_11795", dtype = "float64", shape = (3, 6, 16))#candidate|11795|(3, 6, 16)|var|float64
func_11794_call = mutated_mod.get_global_var('func_11794')
call_11796 = func_11794_call(var_11795)
output = call_11796
func_11797 = relay.Function([var_11795], output)
mutated_mod['func_11797'] = func_11797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6580_call = mod.get_global_var('func_6580')
func_6581_call = mutated_mod.get_global_var('func_6581')
call_11820 = relay.TupleGetItem(func_6580_call(), 0)
call_11821 = relay.TupleGetItem(func_6581_call(), 0)
output = call_11820
output2 = call_11821
func_11831 = relay.Function([], output)
mod['func_11831'] = func_11831
mod = relay.transform.InferType()(mod)
output = func_11831()
func_11832 = relay.Function([], output)
mutated_mod['func_11832'] = func_11832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11212_call = mod.get_global_var('func_11212')
func_11213_call = mutated_mod.get_global_var('func_11213')
call_11900 = func_11212_call()
call_11901 = func_11212_call()
output = relay.Tuple([call_11900,])
output2 = relay.Tuple([call_11901,])
func_11902 = relay.Function([], output)
mod['func_11902'] = func_11902
mod = relay.transform.InferType()(mod)
output = func_11902()
func_11903 = relay.Function([], output)
mutated_mod['func_11903'] = func_11903
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11923 = relay.var("var_11923", dtype = "float32", shape = (10, 15, 14))#candidate|11923|(10, 15, 14)|var|float32
var_11924 = relay.var("var_11924", dtype = "float32", shape = (10, 15, 14))#candidate|11924|(10, 15, 14)|var|float32
bop_11925 = relay.floor_divide(var_11923.astype('float32'), relay.reshape(var_11924.astype('float32'), relay.shape_of(var_11923))) # shape=(10, 15, 14)
func_1070_call = mod.get_global_var('func_1070')
func_1073_call = mutated_mod.get_global_var('func_1073')
const_11945 = relay.const([4,5,-7,-5,-2,-1,7,8,5,6,2,-4,3,-3,7,7,5,-7,10,7,-7,4,-8,-5,4,6,9,9,3,-1,7,-6,-1,5,4,-3,2,5,2,2,3,2,-5,-4,-4,-3,-4,-3,1,-8,10,8,-9,-2,4,6,10,-9,-8,7,7,-3,6,-8,6,2,7,9,-4,6,-5,-3,-10,-1,-5,-4,-8,-5,-5,-1,-9,6,-2,2,4,-4,-10,-3,9,-3,-4,-7,4,-7,7,7,-1,-1,-5,-1,-1,-9,3,-3,10,7,1,-6,-9,1,3,1,-10,-10,-7,8,-7,-9,1,-3,6,-4,-7,1,5,10,-1,-3,7,-7,-4,2,-2,-10,-3,-5,-4,-7,1,-4,1,6,9,4,-3,-8,-6,10,3,4,-4,8,-7,-6,-4,-7,-8,-8,6,-1,-3,-8,3,-10,8,4,-10,-10,7,7,10,-6,-9,-5,8,-6,7,1,-1,-4,-4,3,-1,3,2,-7,6,-1,10,1,-2,-1,10,6,-5,-2,-1,5,9,9,-9,-6,-2,9,-2,1,7,2,-4,-7,-1,7,6,-5,9,-8,10,1,-10,-5,-1,4,-8,5,5,10,3,-1,9,-5,9,7,5,1,-10,-8,5,-1,10,-7,-10,-4,-6,1,8,4,-7,-7,8,-10,6,-9,1,8,-6,8,-1,8,-7,3,-4,3,5,-6,7,9,-7,6,8,1,8,9,-4,-9,5,6,-8,-1,-8,5,-6,-1,-5,-10,3,-9,5,-2,-5,9,2,9,4,-2,10,10,-2,-8,-7,9,4,-3,-8,-7,8,4,3,2,7,2,1,-3,2,-7,-2,1,6,2,-8,6,-6,6,6,-7,-1,-8,10,3,-3,-10,-1,-10,6,-1,-2,2,9,-7,5,-8,2,9,9,3,6,-10,6,-6,-3,-9,-5,-5,9,9,-6,2,-7,2,-5,-10,10,-10,10,-1,2,-2,-10,-9,-8,3,-7,4,8,-10,10,-5,-1,-7,8,8,9,-5,6,6,-4,2,7,-7,-3,-7,-10,3,5,4,1,3,1,-7,-6,3,-5,3,-10,-5,9,5,-2,9,-2,3,5,1,6,3,2,-1,-10,9,5,2,-5,3,9,5,7,5,3,-7,6,10,5,-7,8,-4,7,6,7,9,1,9,3,-1,-2,7,8,7,1,-10,-9,1,-2,-10,-6,5,5,9,-8,4,7,-9,3,10,-2,-2,-5,-7,-1,6,-5,7,4,8,6,-5,5,8,2,1,-8,-4,-7,-10,9,-6,-8,6,10,-8,-6,-9,-7,-9,7,-2,5,10,9,10,9,-4,-10,-10,4,7,1,1,5,6,1,8,5,8,1,4,4,6,-8,-6,-6,-2,-1,4,4,7,-7,-3,-5,6,1,-6,10,8,-10,-2,-7,5,9,1,1,-3,5,3,-9,9,-1,-4,9,-10,-6,9,-9,9,-4,-5,2,-3,6,-10,7,4,4,-10,9,6,-4,-7,7,-3,10,-6,-8,9,7,8,9,-3,-9,8,2,-1,6,9,6,4,2,8,3,3,-7,5,4,-8,8,8,7,6,9,-7,-1,-3,-3,4,-8,-5,9,-8,-5,-5,2,4,-5,1,8,-1,8,-4,4,-6,-7,7,8,-9,4,7,9,3,4,8,-3,2,2,2,-6,-10,9,8,-5,-2,3,4,3,-6,3,-10,2,10,8,3,2,6,1,1,-3,6,4,-9,-9,-5,-8,1], dtype = "int32")#candidate|11945|(660,)|const|int32
call_11944 = func_1070_call(relay.reshape(const_11945.astype('int32'), [15, 4, 11]))
call_11946 = func_1070_call(relay.reshape(const_11945.astype('int32'), [15, 4, 11]))
output = relay.Tuple([bop_11925,call_11944,const_11945,])
output2 = relay.Tuple([bop_11925,call_11946,const_11945,])
func_11947 = relay.Function([var_11923,var_11924,], output)
mod['func_11947'] = func_11947
mod = relay.transform.InferType()(mod)
var_11948 = relay.var("var_11948", dtype = "float32", shape = (10, 15, 14))#candidate|11948|(10, 15, 14)|var|float32
var_11949 = relay.var("var_11949", dtype = "float32", shape = (10, 15, 14))#candidate|11949|(10, 15, 14)|var|float32
output = func_11947(var_11948,var_11949,)
func_11950 = relay.Function([var_11948,var_11949,], output)
mutated_mod['func_11950'] = func_11950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8547_call = mod.get_global_var('func_8547')
func_8548_call = mutated_mod.get_global_var('func_8548')
call_11963 = func_8547_call()
call_11964 = func_8547_call()
output = relay.Tuple([call_11963,])
output2 = relay.Tuple([call_11964,])
func_11983 = relay.Function([], output)
mod['func_11983'] = func_11983
mod = relay.transform.InferType()(mod)
output = func_11983()
func_11984 = relay.Function([], output)
mutated_mod['func_11984'] = func_11984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7728_call = mod.get_global_var('func_7728')
func_7730_call = mutated_mod.get_global_var('func_7730')
call_11994 = relay.TupleGetItem(func_7728_call(), 2)
call_11995 = relay.TupleGetItem(func_7730_call(), 2)
func_9661_call = mod.get_global_var('func_9661')
func_9663_call = mutated_mod.get_global_var('func_9663')
call_11997 = relay.TupleGetItem(func_9661_call(), 0)
call_11998 = relay.TupleGetItem(func_9663_call(), 0)
func_7329_call = mod.get_global_var('func_7329')
func_7334_call = mutated_mod.get_global_var('func_7334')
var_12002 = relay.var("var_12002", dtype = "float32", shape = (56,))#candidate|12002|(56,)|var|float32
var_12003 = relay.var("var_12003", dtype = "float32", shape = (390,))#candidate|12003|(390,)|var|float32
var_12004 = relay.var("var_12004", dtype = "float32", shape = (35, 1))#candidate|12004|(35, 1)|var|float32
call_12001 = relay.TupleGetItem(func_7329_call(relay.reshape(var_12002.astype('float32'), [4, 1, 14]), relay.reshape(var_12003.astype('float32'), [390,]), relay.reshape(var_12004.astype('float32'), [7, 5]), ), 2)
call_12005 = relay.TupleGetItem(func_7334_call(relay.reshape(var_12002.astype('float32'), [4, 1, 14]), relay.reshape(var_12003.astype('float32'), [390,]), relay.reshape(var_12004.astype('float32'), [7, 5]), ), 2)
output = relay.Tuple([call_11994,call_11997,call_12001,var_12002,var_12003,var_12004,])
output2 = relay.Tuple([call_11995,call_11998,call_12005,var_12002,var_12003,var_12004,])
func_12012 = relay.Function([var_12002,var_12003,var_12004,], output)
mod['func_12012'] = func_12012
mod = relay.transform.InferType()(mod)
var_12013 = relay.var("var_12013", dtype = "float32", shape = (56,))#candidate|12013|(56,)|var|float32
var_12014 = relay.var("var_12014", dtype = "float32", shape = (390,))#candidate|12014|(390,)|var|float32
var_12015 = relay.var("var_12015", dtype = "float32", shape = (35, 1))#candidate|12015|(35, 1)|var|float32
output = func_12012(var_12013,var_12014,var_12015,)
func_12016 = relay.Function([var_12013,var_12014,var_12015,], output)
mutated_mod['func_12016'] = func_12016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5036_call = mod.get_global_var('func_5036')
func_5037_call = mutated_mod.get_global_var('func_5037')
call_12038 = relay.TupleGetItem(func_5036_call(), 0)
call_12039 = relay.TupleGetItem(func_5037_call(), 0)
func_4707_call = mod.get_global_var('func_4707')
func_4710_call = mutated_mod.get_global_var('func_4710')
const_12050 = relay.const([-3,3,6,1,4,-9,4,-4,6,-3,-4,1,3,-5,6,-4,1,-2,5,8,-3,-10,-4,7,-8,-4,-5,-10,10,7,-1,4,-8,8,-10,-1,-7,2,-7,9,9,-8,2,-3,5,-8,-10,-8,-9,-2,-5,5,-5,-1,-6,-6,8,9,3,-2,-1,5,-3,10,1,4,-6,-10,-6,3,-5,-6,4,3,-1,-6,-7,6,5,-3,-9,-4,6,5,-7,3,-7,7,8,9,-6,2,7,5,-3,8,-7,-8,-8,-4,-3,-9,10,4,-5,-9,-9,6,8,-5,10,-4,8,10,7,3,5,-2,9,4,8,-6,-2,-2,4,5,3,-8,3,8,-4,-10,4,-3,-8,8,-8,-5,-9,-5,6,-4,9,-9,4,4,8,-6,-8,7,7,3,10,-8,-7,-1,-2,4,-10,6,2,-1,-6,5,7,-9,7,-10,2,-7,2,3,-2,-9,-2,6,5,-4,-4,4,-1,6,6,7,5,-10,10,2,10,6,-6,-4,8,3,-7,3,-1,7,4,-9,6,5,3,-1,1,-5,-10,2,-8,-1,-4,-4,1,4,3,-4,3,6,1,8,-5,-10,1,2,-7,-4,-7,-7,8,-6,7,2,3,5,-3,5,8,-2,9,8,-7,8,1,-4,7,3,-2,-3,3,9,2,4,3,-9,-2,-10,-9,4,-6,-2,2,6,-10,-1,8,7,-5,-10,-10,1,-5,-10,-3,-8,-7,-1,-6,3,5,-7,1,3,-8,6,-3,8,10,-4,-6,-2,-5,-10,-10,-6,-4,-10,-8,4,-5,2,7,-5,1,2,4,-10,6,9,-2,3,-6,2,-5,10,5,9,5,1,-5,-5,6,7,5,8,-9,-1,3,10,10,-7,5,8,-9,-8,-9,-3,-6,7,-4,-7,7,9,5,-7,3,-9,1,8,6,4,7,-10,-8,4,-1,7,3,7,9,-3,9,9,-1,2,3,3,-5,-4,-8,-7,1,7,1,-2,-10,-1,8,9,-8,-7,6,10,-2,4,-3,9,4,10,1,-6,-10,10,-8,7,1,-9,-5,8,-5,7,3,4,3,-3,-9,-7,-7,-6,7,2,-9,-7,-2,-10,-9,-5,-3,10,-4,-4,3,3,-10,4,2,7,7,-4,9,5,2,-10,10,3,-4,-8,-8,-4,10,8,-4,-3,-9,1,2,-7,8,1,9,4,1,-10,-3,-9,-2,4,4,-8,-4,-2,-9,-3,8,6,8,-3,-2,-9,-7,9,-7,-9,10,-3,-8,-5,8,3,1,-5,9,-9,-9,7,7,9,-1,-5,6,7,5,-3,1,-8,5,-3,-1,7,-1,8,-4,-3,3,-6,-8,-5,7,5,-3,-10,8,5,6,-9,-10,-4,-2,-9,-7,-4,-2,-7,6,-6,-8,-9,2,6,-8,2,2,2,4,-8,10,7,2,10,-7,7,5,-2,10,4,4,7,3,-9,3,-10,-9,5,-1,9,3,3,-4,6,4,-1,5,4,7,5,-9,3,9,3,-4,8,-10,7,8,5,3,-10,-4,-4,-8,-3,1,-6,5,-2,2,6,1,-6,-9,10,-9,-8,-7,-7,1,-9,-5,7,-6,1,-7,2,2,-8,10,-3,-10,-5,-5,-9,10,1,5,-9,6,-1,-7,-2,8,10,-8,9,5,-5,4,-7,2,-4,-7,-9,1,6,10,8,10,8,-2,5,10,-6,-2,3,-4,-4,-9,3,-5,-9,1,-5,-7,6,-1,-7,-1,-9,9,-10,8,3], dtype = "int32")#candidate|12050|(660,)|const|int32
call_12049 = relay.TupleGetItem(func_4707_call(relay.reshape(const_12050.astype('int32'), [660,])), 3)
call_12051 = relay.TupleGetItem(func_4710_call(relay.reshape(const_12050.astype('int32'), [660,])), 3)
uop_12056 = relay.asinh(call_12049.astype('float32')) # shape=(15, 4, 11)
uop_12058 = relay.asinh(call_12051.astype('float32')) # shape=(15, 4, 11)
func_10391_call = mod.get_global_var('func_10391')
func_10392_call = mutated_mod.get_global_var('func_10392')
call_12067 = relay.TupleGetItem(func_10391_call(), 0)
call_12068 = relay.TupleGetItem(func_10392_call(), 0)
func_7002_call = mod.get_global_var('func_7002')
func_7007_call = mutated_mod.get_global_var('func_7007')
var_12074 = relay.var("var_12074", dtype = "int16", shape = (6, 28))#candidate|12074|(6, 28)|var|int16
const_12075 = relay.const([6.881539,2.039875,-1.247814,5.075679,9.240672,-5.951243,0.780582,1.988625,-9.214423,7.830020,8.563461,-2.012067,4.956239,-0.863693,-1.326568,-6.320424,0.681800,8.848836,-8.536325,-1.835358,6.163568,2.797121,3.794247,9.260218,8.002000,-7.212118,-6.534989,2.683793,7.882322,-8.609243,8.408170,6.605272,-9.725133,6.771889,0.151466,7.400563,-3.858235,7.215678,3.433082,2.894804,7.340826,5.920728,4.195214,-5.490952,6.577900,-5.742208,3.485380,8.232746,-6.582703,-6.919933,-4.575829,0.970662,-4.562559,6.012605,2.234209,6.527854,-1.657612,-6.282072,4.286829,-9.684726,4.258276,5.556612,-9.391802,-1.176725,7.536618,4.059498,-5.334482,1.010935,3.818454,-4.626111,6.451968,-1.814491,0.922035,7.800292,8.555923,2.944746,4.204981,5.741414,5.480806,-9.106438,-1.795941,7.104614,-8.467686,-7.877291,2.449932,-3.650567,-1.018989,-2.443225,8.223535,-6.731524,-6.749610,6.003021,-1.905739,0.275174,3.083556,2.846786,3.929600,-5.455831,0.265124,-2.029854,-6.505240,6.590553,4.890709,-1.699460,-2.492887,2.226007,-9.958802,-2.721669,1.479774,-3.890310,6.603256,-8.111129,-9.759167,8.658043,2.955638,-1.559930,-8.470939,-7.898286,-2.014766,3.330755,6.612543,6.445127,9.248991,5.325146,7.856997,1.608207,8.880258,-5.098757,1.132662,6.689058,5.456854,-8.107962,4.938038,1.602263,8.968960,-9.479218,5.963301,-8.858819,4.263660,6.329679,4.443340,-9.894746,-4.123125,5.621689,-7.601575,6.984269,-1.917915,7.480628,-6.601579,0.105122,8.997581,7.701195,9.149724,-0.694419,3.047338,-8.667948,-0.281430,7.787555,2.277587,-8.273092,7.826356,0.230191,8.755195,1.297247,5.278842,5.613090,7.956229,8.421070,-4.157744,3.476134,0.036149,7.607471,-6.120276,-3.177643,6.069783,4.302930,-9.875783,-2.453966,-4.730106,-9.322396,4.020645,-0.524687,-5.036549,2.768057,5.931733,-8.548845,-7.091341,4.787750,-2.472386,-8.066998,-2.167918,-0.332274,-5.579509,8.221508,-1.128478,-6.993429,3.289369,-0.173507,-7.773146,1.673983,0.453196,-1.468716,2.007316,-2.269577,-3.853523,1.915064,8.858932,6.448632,-1.138070,-3.844800,-5.185918,-8.145620,4.719240,1.093274,5.600082,-6.313489,-4.361527,-8.483957,-8.266840,9.230038,-6.241258,3.750351,-3.645641,2.081046,9.193626,-7.619533,0.699924,-5.111240,5.247435,-7.540644,-7.687005,3.188893,-9.937532,-7.648525,1.068275,4.209936,-7.773788,6.282744,4.331962,3.646146,-6.741662,8.634424,5.947857,-9.595846,7.019791,9.235262,1.929676,5.072824,-5.873114,-5.446963,9.306220,0.555134,9.165320,9.688211,-1.838533,3.369173,-8.211404,-3.309117,-7.439564,-6.149152,7.452394,3.289593,1.143349,-7.283531,-7.237964,2.618284,-5.611431,1.596873,5.171345,5.435468,-2.159534,-8.039165,6.011681,-5.071506,5.121351,9.211478,-4.784433,-7.399099,4.017841,9.805667,5.625408,-6.585078,-0.846220,0.640252,-6.757377,8.064727,-2.373328,6.987472,-0.091714,9.776262,-7.762048,-4.505822,-4.567214,-2.686163,-6.877562,2.661916,-4.845465,7.862906,-4.018874,-3.484896,5.851369,8.463098,0.049947,9.236581,-1.736590,-8.818087,-4.071603,1.777479,3.687116,-4.374424,9.772816,8.570028,0.448179,-8.733914,-2.496356,-0.931967,-5.855315,5.201304,-3.178175,6.422780,0.033061,-4.013339,5.596312,-2.619636,6.006531,-6.360951,3.630744,9.292011,-5.955354,-7.813835,-3.675651,5.355505,-5.817188,3.371667,4.188665,5.538539,-1.325000,-5.173027,9.774281,-8.238106,-5.937904,1.693866,-9.291907,-0.759996,6.579603,9.712120,-0.066984,-2.241826,6.421614,1.138340,1.251933,-6.405676,-7.077909,6.168370,0.525441,5.392268,-7.590273,6.180038,6.281219,4.580993,-2.608305,-4.852810,1.501418,5.176245,-3.546217,-6.502339,8.823625,0.857904,6.491745,6.063947,-1.077935,-1.383498,-9.147133,-9.414681,-8.103680,-2.528803,-2.131919,7.806157,6.635286,8.935083,0.304360,0.772684,-3.485189,1.922658,8.968008,-2.028425,8.603379,-5.166333,0.881659,1.376329], dtype = "float32")#candidate|12075|(390,)|const|float32
const_12076 = relay.const([-9.752250,0.535722,3.065315,-5.110990,-3.912850,3.231686,-8.674566,4.292741,-7.546364,-5.335240,-9.954325,1.537310,0.958829,5.620649,-5.036634,-7.327327,1.768547,-9.890543,-1.173915,-0.289766,1.541602,7.258865,-1.999371,1.114063,3.097818,-7.048939,2.841491,3.617438,-4.089639,9.800660,-0.900544,2.090957,3.743211,-5.639633,-6.248211,4.104048,3.312165,-8.011629,3.706917,-2.587636,0.245234,-3.993119,-5.816362,0.409142,2.167273,7.176132,-2.498308,0.799673,-6.736574,-1.745231,-5.652392,-5.739571,-3.566978,5.876406,9.247503,-7.494697,-3.336058,2.399885,-6.914546,5.866429,8.476080,-6.030651,-5.795856,9.839835,3.635436,8.213676,5.894300,9.562505,-0.939889,3.756235,-0.177934,-7.682146,3.538206,5.559502,-2.926272,2.436216,3.762954,-8.500830,3.261857,8.422171,0.014569,2.152693,-7.641533,-6.977069,6.109028,-0.388416,-1.538843,6.410153,-4.576132,3.668647,6.556496,-4.184661,-3.121392,-8.900884,0.127345,7.577856,1.723850,7.401329,8.957509,-0.511667,-8.880734,2.340241,-4.835370,-2.104762,0.019885,9.065085,-4.965952,-7.057279,-8.639391,-2.045050,-2.338472,-0.626755,-9.781180,9.560682,-5.109086,5.717283,3.188642,6.249053,1.941203,-1.640837,3.524726,8.287470,-4.346382,2.287060,2.916335,-7.912655,0.934034,7.539577,-4.915747,0.801736,-9.596231,3.122698,8.524420,4.555149,-8.833194,-2.342134,-7.341615,7.920844,4.780841,2.054536,8.929143,-5.649418,1.198394,-3.877874,-7.442406,-2.096809,-1.516235,-0.492749,-4.734940,-0.725056,-8.400678,-6.953148,3.349818,9.039020,-4.648405,3.170526,-9.177981,-5.591908,8.747363,0.448678,2.536677,-1.253100,-1.947456,3.475090,3.947291,7.723974,-2.175196,-8.455513,-7.732230,-6.603245,-3.315348,-4.614546,0.259272,-1.216915,1.441261,7.199543,4.075157,1.554130,-7.842925,-7.440001,-3.100135,7.689256,-2.795344,-2.459454,1.588303,6.461788,-4.185415,-6.945414,6.131973,-2.476453,3.270795,1.882055,-9.679503,-1.150049,9.539510,-2.508145,-6.442292,0.652539,9.589393,8.295940,-7.664348,-9.627949,-9.105309,7.221636,-6.433050,4.583782,1.970451,-3.925170,8.524768,-7.320030,-1.151657,-8.660727,0.797366,1.197845,-3.139024,1.325037,3.062916,9.632953,8.416015,4.056909,1.549966,9.149065,3.259249,-4.332226,-0.867391,-7.086527,7.121340,7.439616,-3.013973,2.398245,-8.208477,2.778010,-2.279594,7.968214,3.953313,7.435879,6.021991,8.263036,2.913692,3.019297,0.420793,-8.638158,7.983503,8.095184,-7.683525,-1.187531,3.588231,-7.165250,-4.947784,2.864175,2.745881,-4.407416,9.679907,4.980762,7.041788,-6.138995,-9.591137,4.012578,9.945037,1.830600,7.446664,-3.115671,-5.337418,4.618573,-3.813293,-8.954102,8.664620,5.595497,7.624814,6.134841,8.593389,5.486368,-6.016910,9.273226,2.639971,1.206886,-0.509182,3.337555,9.287135,-7.809982,-3.272372,9.323341,0.848938,-9.500731,7.656759,-4.502630,-8.366551,2.563237,-6.263291,-8.996118,5.441058,5.146211,6.327799,-4.135902,9.434121,-1.154769,-0.210550,4.112883,-0.487574,-1.377103,-5.726902,9.734879,-9.923333,8.780265,9.345192,-2.635958,-9.825015,0.447947,-6.146081,-6.700068,-6.516526,3.073770,-8.017897,-3.475604,3.146935,-1.050139,0.685137,-2.584768,-2.583928,0.577300,5.729864,4.706522,7.315443,4.278427,-1.786056,3.088911,-4.062390,3.580140,2.329200,-4.674867,-3.887059,-9.053372,-9.684102,2.455773,4.358944,-9.187642,-8.511719,-1.697578,-4.004523,-3.149995,2.568353,2.259942,-5.438252,-4.500033,5.531764,-6.680417,3.582327,0.315670,4.333053,1.366368,4.501732,1.713760,1.773675,0.897594,9.278938,-2.643192,3.710048,1.431276,1.297047,-9.361802,-5.428682,-2.874860,7.860873,6.298979,5.660092,1.313963,-1.153787,-4.690280,-8.289797,-2.095851,1.144823,-4.602660,-5.707756,8.518411,3.253894,-2.583047,-5.241948,-6.945169,8.208497,9.428030,-9.265627,0.882288,6.647118,-0.885113,-9.301018,-9.978384,3.951795,-3.747948,-0.692627,8.378621,7.902352,0.840286,9.024254,-5.747305,8.975753,3.884267,-0.970312,-0.151123,-5.446021,-8.663448,4.579075,7.074538,0.145858,8.617528,9.745405,-5.941493,-7.025692,-0.173094,9.874655,-0.919884,-4.415026,-4.253633,9.316448,4.316896,2.508196,-6.144945,-7.278370,2.617759,9.574513,5.482035,-8.439199,-0.306514,4.863265,-7.806181,4.703476,1.809381,-4.405339,-2.565428,-2.758339,6.139180,2.792182,7.636625,3.372837,-8.095335,4.577370,0.479073,2.323857,-6.481151,5.063385,3.426162,-2.533218,-6.255949,-3.098788,-7.088514,-5.777037,-7.995698,7.356434,6.232049,-9.459165,4.113499,2.976754,5.114712,-5.775878,5.213286,-6.245240,-2.802501,3.811525,4.847229,-2.768367,9.962677,-2.627640,-0.419904], dtype = "float32")#candidate|12076|(462,)|const|float32
const_12077 = relay.const([1,3,6,3,-4,-4,-3,2,3,-5,5,-4,9,-6,-10,6,-10,5,-2,4,9,-8,-7,6,-4,-2,10,1,-5,6,7,-9,2,1,-2,2,2,-4,2,6,-4,-7,4,4,5,5,4,9,7,10,6,1,-3,7,-8,5,1,6,10,-5,2,6,-3,1,-4,1,4,8,-8,5,7,-10,2,4,-6,8,8,-5,9,-2,9,-5,-5,2,-5,1,-9,-10,9,-4,2,4,-5,10,-4,-1,6,-6,6,-4,5,2,-10,-6,6,-3,-1,10,-5,4,-5,-2,8,9,6,-6,3,-6,2,-10,-1,9,-10,-1,-1,6,-9,-4,6,2,9,4,6,4,1,8,-9,-7,-8,-5,3,-7,-8,1,6,-8,1,-8,-2,-7,-6,-9,4,5,-4,2,-2,10,-10,5,-4,3,-5,-4,-1,1,8,4,6,5,-2,9,-8,5,2,5,3,3,7,6,-8,9,9,-9,5,-8,1,-2,-8,8,-6,-6,-1,10,6,-9,-5,2,2,-10], dtype = "uint8")#candidate|12077|(200,)|const|uint8
call_12073 = relay.TupleGetItem(func_7002_call(relay.reshape(var_12074.astype('int16'), [6, 28]), relay.reshape(const_12075.astype('float32'), [390,]), relay.reshape(const_12076.astype('float32'), [462,]), relay.reshape(const_12077.astype('uint8'), [200,]), ), 3)
call_12078 = relay.TupleGetItem(func_7007_call(relay.reshape(var_12074.astype('int16'), [6, 28]), relay.reshape(const_12075.astype('float32'), [390,]), relay.reshape(const_12076.astype('float32'), [462,]), relay.reshape(const_12077.astype('uint8'), [200,]), ), 3)
func_7133_call = mod.get_global_var('func_7133')
func_7137_call = mutated_mod.get_global_var('func_7137')
const_12094 = relay.const([2.574130,-0.389406,6.827121,8.344762,5.163575,6.000851,9.534113,9.561977,-9.414538,7.921388,6.632805,8.544330,2.320021,-5.857752,5.685956,-4.323920,0.546316,-2.407790,-8.373902,-5.612580,-9.572200,-4.916013,8.412394,2.567334,-8.830236,-4.550195,-7.077564,-3.029698,5.883052,-4.533628,-5.073716,-6.546269,1.545666,-9.557626,-2.778988,8.366850,1.130950,-7.807720,2.863263,-6.925473,-8.473241,5.418934,-0.999109,0.254464,-9.454762,4.300798,-1.007257,1.111178,-8.942881,6.352219,-0.818013,-8.052589,-5.262534,-3.147496,-0.599451,3.034797,8.650322,1.357191,0.536812,6.845626,-8.748801,-6.303664,-8.223170,-6.939068,-7.336559,-8.830515,-2.763467,-1.677412,6.156831,-0.938094,8.522489,5.873634,-3.495977,-8.690949,1.175453,5.357760,-1.767928,-5.503613,9.070895,-9.625090], dtype = "float32")#candidate|12094|(80,)|const|float32
var_12095 = relay.var("var_12095", dtype = "float32", shape = (120,))#candidate|12095|(120,)|var|float32
call_12093 = relay.TupleGetItem(func_7133_call(relay.reshape(const_12094.astype('float32'), [10, 8, 1]), relay.reshape(var_12095.astype('float32'), [120,]), ), 3)
call_12096 = relay.TupleGetItem(func_7137_call(relay.reshape(const_12094.astype('float32'), [10, 8, 1]), relay.reshape(var_12095.astype('float32'), [120,]), ), 3)
output = relay.Tuple([call_12038,const_12050,uop_12056,call_12067,call_12073,var_12074,const_12075,const_12076,const_12077,call_12093,const_12094,var_12095,])
output2 = relay.Tuple([call_12039,const_12050,uop_12058,call_12068,call_12078,var_12074,const_12075,const_12076,const_12077,call_12096,const_12094,var_12095,])
func_12098 = relay.Function([var_12074,var_12095,], output)
mod['func_12098'] = func_12098
mod = relay.transform.InferType()(mod)
mutated_mod['func_12098'] = func_12098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12098_call = mutated_mod.get_global_var('func_12098')
var_12100 = relay.var("var_12100", dtype = "int16", shape = (6, 28))#candidate|12100|(6, 28)|var|int16
var_12101 = relay.var("var_12101", dtype = "float32", shape = (120,))#candidate|12101|(120,)|var|float32
call_12099 = func_12098_call(var_12100,var_12101,)
output = call_12099
func_12102 = relay.Function([var_12100,var_12101,], output)
mutated_mod['func_12102'] = func_12102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7506_call = mod.get_global_var('func_7506')
func_7507_call = mutated_mod.get_global_var('func_7507')
call_12152 = relay.TupleGetItem(func_7506_call(), 0)
call_12153 = relay.TupleGetItem(func_7507_call(), 0)
output = relay.Tuple([call_12152,])
output2 = relay.Tuple([call_12153,])
func_12185 = relay.Function([], output)
mod['func_12185'] = func_12185
mod = relay.transform.InferType()(mod)
output = func_12185()
func_12186 = relay.Function([], output)
mutated_mod['func_12186'] = func_12186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8858_call = mod.get_global_var('func_8858')
func_8860_call = mutated_mod.get_global_var('func_8860')
call_12239 = func_8858_call()
call_12240 = func_8858_call()
output = call_12239
output2 = call_12240
func_12257 = relay.Function([], output)
mod['func_12257'] = func_12257
mod = relay.transform.InferType()(mod)
mutated_mod['func_12257'] = func_12257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12257_call = mutated_mod.get_global_var('func_12257')
call_12258 = func_12257_call()
output = call_12258
func_12259 = relay.Function([], output)
mutated_mod['func_12259'] = func_12259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11902_call = mod.get_global_var('func_11902')
func_11903_call = mutated_mod.get_global_var('func_11903')
call_12309 = relay.TupleGetItem(func_11902_call(), 0)
call_12310 = relay.TupleGetItem(func_11903_call(), 0)
output = relay.Tuple([call_12309,])
output2 = relay.Tuple([call_12310,])
func_12323 = relay.Function([], output)
mod['func_12323'] = func_12323
mod = relay.transform.InferType()(mod)
mutated_mod['func_12323'] = func_12323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12323_call = mutated_mod.get_global_var('func_12323')
call_12324 = func_12323_call()
output = call_12324
func_12325 = relay.Function([], output)
mutated_mod['func_12325'] = func_12325
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8137_call = mod.get_global_var('func_8137')
func_8138_call = mutated_mod.get_global_var('func_8138')
call_12344 = relay.TupleGetItem(func_8137_call(), 3)
call_12345 = relay.TupleGetItem(func_8138_call(), 3)
output = relay.Tuple([call_12344,])
output2 = relay.Tuple([call_12345,])
func_12374 = relay.Function([], output)
mod['func_12374'] = func_12374
mod = relay.transform.InferType()(mod)
mutated_mod['func_12374'] = func_12374
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12374_call = mutated_mod.get_global_var('func_12374')
call_12375 = func_12374_call()
output = call_12375
func_12376 = relay.Function([], output)
mutated_mod['func_12376'] = func_12376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11902_call = mod.get_global_var('func_11902')
func_11903_call = mutated_mod.get_global_var('func_11903')
call_12393 = relay.TupleGetItem(func_11902_call(), 0)
call_12394 = relay.TupleGetItem(func_11903_call(), 0)
output = call_12393
output2 = call_12394
func_12416 = relay.Function([], output)
mod['func_12416'] = func_12416
mod = relay.transform.InferType()(mod)
mutated_mod['func_12416'] = func_12416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12416_call = mutated_mod.get_global_var('func_12416')
call_12417 = func_12416_call()
output = call_12417
func_12418 = relay.Function([], output)
mutated_mod['func_12418'] = func_12418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6322_call = mod.get_global_var('func_6322')
func_6324_call = mutated_mod.get_global_var('func_6324')
call_12450 = func_6322_call()
call_12451 = func_6322_call()
func_5147_call = mod.get_global_var('func_5147')
func_5149_call = mutated_mod.get_global_var('func_5149')
call_12457 = relay.TupleGetItem(func_5147_call(), 0)
call_12458 = relay.TupleGetItem(func_5149_call(), 0)
func_11197_call = mod.get_global_var('func_11197')
func_11199_call = mutated_mod.get_global_var('func_11199')
var_12461 = relay.var("var_12461", dtype = "float32", shape = (48,))#candidate|12461|(48,)|var|float32
call_12460 = relay.TupleGetItem(func_11197_call(relay.reshape(var_12461.astype('float32'), [8, 6, 1])), 0)
call_12462 = relay.TupleGetItem(func_11199_call(relay.reshape(var_12461.astype('float32'), [8, 6, 1])), 0)
func_7521_call = mod.get_global_var('func_7521')
func_7522_call = mutated_mod.get_global_var('func_7522')
call_12478 = relay.TupleGetItem(func_7521_call(), 1)
call_12479 = relay.TupleGetItem(func_7522_call(), 1)
func_8151_call = mod.get_global_var('func_8151')
func_8152_call = mutated_mod.get_global_var('func_8152')
call_12482 = func_8151_call()
call_12483 = func_8151_call()
func_6072_call = mod.get_global_var('func_6072')
func_6074_call = mutated_mod.get_global_var('func_6074')
call_12494 = relay.TupleGetItem(func_6072_call(), 0)
call_12495 = relay.TupleGetItem(func_6074_call(), 0)
bop_12504 = relay.bitwise_or(var_12461.astype('int8'), call_12494.astype('int8')) # shape=(10, 8, 48)
bop_12507 = relay.bitwise_or(var_12461.astype('int8'), call_12495.astype('int8')) # shape=(10, 8, 48)
output = relay.Tuple([call_12450,call_12457,call_12460,call_12478,call_12482,bop_12504,])
output2 = relay.Tuple([call_12451,call_12458,call_12462,call_12479,call_12483,bop_12507,])
func_12518 = relay.Function([var_12461,], output)
mod['func_12518'] = func_12518
mod = relay.transform.InferType()(mod)
var_12519 = relay.var("var_12519", dtype = "float32", shape = (48,))#candidate|12519|(48,)|var|float32
output = func_12518(var_12519)
func_12520 = relay.Function([var_12519], output)
mutated_mod['func_12520'] = func_12520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9480_call = mod.get_global_var('func_9480')
func_9481_call = mutated_mod.get_global_var('func_9481')
call_12535 = relay.TupleGetItem(func_9480_call(), 1)
call_12536 = relay.TupleGetItem(func_9481_call(), 1)
var_12539 = relay.var("var_12539", dtype = "float64", shape = (10, 13, 2))#candidate|12539|(10, 13, 2)|var|float64
bop_12540 = relay.right_shift(call_12535.astype('uint8'), relay.reshape(var_12539.astype('uint8'), relay.shape_of(call_12535))) # shape=(10, 13, 2)
bop_12543 = relay.right_shift(call_12536.astype('uint8'), relay.reshape(var_12539.astype('uint8'), relay.shape_of(call_12536))) # shape=(10, 13, 2)
func_11507_call = mod.get_global_var('func_11507')
func_11509_call = mutated_mod.get_global_var('func_11509')
call_12546 = relay.TupleGetItem(func_11507_call(), 1)
call_12547 = relay.TupleGetItem(func_11509_call(), 1)
bop_12573 = relay.less_equal(bop_12540.astype('bool'), relay.reshape(call_12535.astype('bool'), relay.shape_of(bop_12540))) # shape=(10, 13, 2)
bop_12576 = relay.less_equal(bop_12543.astype('bool'), relay.reshape(call_12536.astype('bool'), relay.shape_of(bop_12543))) # shape=(10, 13, 2)
output = relay.Tuple([call_12546,bop_12573,])
output2 = relay.Tuple([call_12547,bop_12576,])
func_12577 = relay.Function([var_12539,], output)
mod['func_12577'] = func_12577
mod = relay.transform.InferType()(mod)
var_12578 = relay.var("var_12578", dtype = "float64", shape = (10, 13, 2))#candidate|12578|(10, 13, 2)|var|float64
output = func_12577(var_12578)
func_12579 = relay.Function([var_12578], output)
mutated_mod['func_12579'] = func_12579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5750_call = mod.get_global_var('func_5750')
func_5751_call = mutated_mod.get_global_var('func_5751')
call_12594 = relay.TupleGetItem(func_5750_call(), 0)
call_12595 = relay.TupleGetItem(func_5751_call(), 0)
func_7772_call = mod.get_global_var('func_7772')
func_7774_call = mutated_mod.get_global_var('func_7774')
call_12604 = func_7772_call()
call_12605 = func_7772_call()
output = relay.Tuple([call_12594,call_12604,])
output2 = relay.Tuple([call_12595,call_12605,])
func_12606 = relay.Function([], output)
mod['func_12606'] = func_12606
mod = relay.transform.InferType()(mod)
mutated_mod['func_12606'] = func_12606
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12606_call = mutated_mod.get_global_var('func_12606')
call_12607 = func_12606_call()
output = call_12607
func_12608 = relay.Function([], output)
mutated_mod['func_12608'] = func_12608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8741_call = mod.get_global_var('func_8741')
func_8742_call = mutated_mod.get_global_var('func_8742')
call_12706 = relay.TupleGetItem(func_8741_call(), 2)
call_12707 = relay.TupleGetItem(func_8742_call(), 2)
func_8788_call = mod.get_global_var('func_8788')
func_8792_call = mutated_mod.get_global_var('func_8792')
var_12712 = relay.var("var_12712", dtype = "float32", shape = (56,))#candidate|12712|(56,)|var|float32
const_12713 = relay.const([-5.607291,4.967188,2.928253,-2.760843,-3.060078,4.015459,3.518371,0.599342,3.230931,2.100763,6.927135,-9.390844,3.853406,-8.845317,-3.309756,5.319386,-1.234949,1.832208,-3.222841,-0.281163,4.174068,1.771392,0.510519,1.252421,8.069300,-9.951590,5.756792,-7.273381,9.259740,-5.533138,3.702512,-6.266673,-7.659370,0.120036,9.357223,7.080250,7.067511,1.212668,-7.526980,5.270014,-0.460901,-1.235663,-8.395884,-2.182441,-6.064043,-8.568790,-5.681879,2.274402,-6.667820,5.779431,-0.377695,-4.069227,2.369733,5.100034,-7.339402,4.691126,-3.050375,8.623884,-5.876907,-8.425037,-6.462320,-2.738860,6.430781,0.409088,-4.410388,3.520345,-9.460638,7.967512,-4.168838,8.196689,4.808721,9.980621,-9.735776,6.316534,-1.712752,0.759961,-1.849306,4.521708,-1.074922,9.337464,5.844151,8.098656,4.261169,2.695659,0.324363,-2.454701,-6.662510,-9.970051,-6.187512,6.936878,7.792781,8.068710,2.758385,0.694289,-9.560009,-4.308643,-7.653062,4.579507,-1.130451,5.564124,3.147265,1.016891,5.648072,-7.656640,3.985415,-6.930931,6.280308,-6.469739,-9.588899,-8.705820,-0.300403,-2.584474,-2.170692,-7.738524,-8.787709,0.067784,-7.396421,7.646951,-6.559314,3.450701,-8.557503,5.746707,-6.524181,-3.884999,6.713295,7.628861,3.387408,-1.664029,4.558986,6.496160,-2.343107,7.243041,1.939180,-4.016352,-5.603661,0.514181,0.620690,-4.508296,-7.658010,-9.580830,3.741515,1.714743,2.760946,6.496685,1.226701,5.045532,5.894739,-1.365117,7.093288,-0.100641,-8.590404,-8.625825,-5.682674,1.274578,6.288033,4.462719,1.853354,-4.858433,-3.031377,6.676731,-3.165220,-1.315189,7.140904,-3.356809,1.004226,6.469819,-5.671882,-9.900734,-2.588964,1.472184,2.569446,3.853772,1.503026,-0.840006,1.474954,5.013039,-8.064291,5.612590,-3.860522,-4.485027,-1.962906,-2.598196,-4.942044,-5.799334,-1.746364,-0.512955,-0.578499,6.291085,0.543802,9.432714,4.122671,-6.338746,-8.582763,-4.957356,6.576241,7.993902,-0.050786,-9.320475,-2.601380,4.899660,-9.062247,-7.558080,3.654171,3.243581,2.498206,9.562158,8.483030,-6.017208,5.346916,6.318307,-8.566220,3.569588,-7.894527,5.692599,-7.703761,3.961278,-8.342159,1.964790,7.876859,4.177540,7.099506,-7.808433,-8.432601,4.791284,2.112349,7.085674,9.401396,-8.966951,-1.741843,-7.127500,-8.410641,-1.124665,4.012863,9.403176,-3.991864,-3.916986,2.051829,-5.766449,9.938911,-8.640492,-9.907828,-9.378567,-8.780815,6.313139,-5.293537,6.436322,-9.609800,-4.165265,3.253394,-5.160817,-9.102174,3.908675,5.857263,7.911114,6.561508,3.804652,9.533325,8.881951,-6.437425,7.306812,-6.216148,-2.239320,-9.616974,3.336071,-9.058855,5.626117,-8.411425,-1.441856,-8.374060,-9.912588,4.901447,-8.049726,-8.664057,-5.186024,-1.899594,4.148896,-2.216441,2.735139,-4.082359,-9.728182,6.051127,6.134228,1.460248,5.667752,-8.666139,3.413276,-0.522274,-8.580062,-6.183928,3.533304,-3.455053,7.450612,-8.571564,3.008895,5.969829,2.693461,9.905164,-9.855123,6.743308,2.881570,-7.481128,2.940442,-9.204534,9.177889,4.096157,4.000320,7.211211,-0.556749,-0.860425,9.176062,-7.930000,-9.073385,5.480950,-3.555251,-2.571774,-4.298749,-7.700073,8.765523,-6.121767,5.496503,-4.829013,1.425663,-6.851143,3.117639,-3.232691,-5.990415,-6.360987,-8.653310,-7.973910,-5.244964,-0.001167,5.691471,-7.195142,5.594109,0.667164,-4.897120,-8.917392,2.272175,-9.470331,7.801476,1.962690,1.077346,-0.446370,-3.111083,-7.705328,7.378733,1.938254,0.867065,-8.709270,-2.426330,-2.861954,3.555863,8.839637,7.456520,8.294628,-5.828474,-4.900145,-4.626349,7.192112,1.562019,4.835844,9.817968,7.700114,7.764792,9.177972,0.944503,-0.863606,-6.228027,-7.519173,9.684734,-4.194383,-7.516065,8.562208,9.355082,3.457287,-0.167015,-2.965050,-7.774237,2.161624,8.840101,5.854034,-1.205051,5.037048,0.588703,-5.158733,7.173402,-6.622680,7.719120,4.963190,0.144304], dtype = "float32")#candidate|12713|(390,)|const|float32
call_12711 = relay.TupleGetItem(func_8788_call(relay.reshape(var_12712.astype('float32'), [56,]), relay.reshape(const_12713.astype('float32'), [5, 78]), ), 1)
call_12714 = relay.TupleGetItem(func_8792_call(relay.reshape(var_12712.astype('float32'), [56,]), relay.reshape(const_12713.astype('float32'), [5, 78]), ), 1)
output = relay.Tuple([call_12706,call_12711,var_12712,const_12713,])
output2 = relay.Tuple([call_12707,call_12714,var_12712,const_12713,])
func_12718 = relay.Function([var_12712,], output)
mod['func_12718'] = func_12718
mod = relay.transform.InferType()(mod)
mutated_mod['func_12718'] = func_12718
mutated_mod = relay.transform.InferType()(mutated_mod)
var_12719 = relay.var("var_12719", dtype = "float32", shape = (56,))#candidate|12719|(56,)|var|float32
func_12718_call = mutated_mod.get_global_var('func_12718')
call_12720 = func_12718_call(var_12719)
output = call_12720
func_12721 = relay.Function([var_12719], output)
mutated_mod['func_12721'] = func_12721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7728_call = mod.get_global_var('func_7728')
func_7730_call = mutated_mod.get_global_var('func_7730')
call_12743 = relay.TupleGetItem(func_7728_call(), 2)
call_12744 = relay.TupleGetItem(func_7730_call(), 2)
func_9480_call = mod.get_global_var('func_9480')
func_9481_call = mutated_mod.get_global_var('func_9481')
call_12745 = relay.TupleGetItem(func_9480_call(), 3)
call_12746 = relay.TupleGetItem(func_9481_call(), 3)
output = relay.Tuple([call_12743,call_12745,])
output2 = relay.Tuple([call_12744,call_12746,])
func_12747 = relay.Function([], output)
mod['func_12747'] = func_12747
mod = relay.transform.InferType()(mod)
output = func_12747()
func_12748 = relay.Function([], output)
mutated_mod['func_12748'] = func_12748
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10883_call = mod.get_global_var('func_10883')
func_10885_call = mutated_mod.get_global_var('func_10885')
call_12786 = func_10883_call()
call_12787 = func_10883_call()
output = relay.Tuple([call_12786,])
output2 = relay.Tuple([call_12787,])
func_12793 = relay.Function([], output)
mod['func_12793'] = func_12793
mod = relay.transform.InferType()(mod)
output = func_12793()
func_12794 = relay.Function([], output)
mutated_mod['func_12794'] = func_12794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8547_call = mod.get_global_var('func_8547')
func_8548_call = mutated_mod.get_global_var('func_8548')
call_12806 = func_8547_call()
call_12807 = func_8547_call()
func_11771_call = mod.get_global_var('func_11771')
func_11774_call = mutated_mod.get_global_var('func_11774')
const_12834 = relay.const([-3.513231,-7.912149,-7.446674,-9.600434,1.790703,4.887703,1.309008,-7.439920,-9.776223,4.930131,5.672323,-0.038448,2.710632,-4.321947,-3.751023,-6.584690,5.314931,-2.477411,4.805546,0.234152,-0.438701,8.341990,9.479662,2.255654,-5.379639,2.446816,4.596444,2.761664,7.969679,5.172994,5.091702,-7.382375,7.355561,-2.721789,2.139095,6.497841,-8.518709,7.054187,-3.789108,-4.226987,8.668692,8.713680,9.516292,8.497577,-2.212339,6.799662,-1.600956,-5.006973,-0.160323,-6.776990,-8.574385,-2.382243,2.947106,-7.233459,-7.002114,-2.610540,-8.926034,-1.022305,-3.085425,-3.817143,6.102631,3.103683,4.865691,7.974338,-7.173155,-2.357921,9.291376,-7.769804,-6.108058,-1.533328,8.296056,2.288298,-6.843511,6.119712,4.548506,6.563609,9.624217,4.537300,-3.070638,5.983495,-1.357946,-1.829036,-5.819736,-4.974115,9.153352,9.539987,0.688672,9.564814,8.979013,0.385786,-3.012783,2.296674,6.049000,3.597024,3.332489,-2.140896,-0.871023,4.679839,8.415748,7.617647,-5.562524,4.688419,4.825546,-0.402183,-3.135883,-9.291851,-0.263363,-2.730962,-8.376716,-7.683092,-5.053535,1.494047,8.941480,9.614419,8.430783,8.185294,-9.251118,1.380151,6.992680,-9.339780,2.827871,3.950298,-6.825960,1.137969,7.579737,-0.290136,3.338170,-1.892294,-4.067619,2.430185,-8.247654,3.618406,-1.607845,5.760542,-6.654136,5.389090,-4.786711,-1.835135,-9.437124,1.523340,2.808391,-9.267624,1.505800,0.431080,-7.938494,8.671626,5.302372,2.248544,-6.379106,-6.709195,-9.274700,-8.743636,-3.211569,5.750740,6.962936,-0.338454,-1.051846,2.411603,5.543663,8.092007,5.175049,-2.294039,-0.234910,-5.365428,-4.485679,1.612756,-2.759674,7.253476,-8.071928,-6.077525,7.157778,-5.769222,4.341520,-2.845402,-5.863282,-3.543841,-7.509886,4.831774,7.879310,3.477572,-1.827969,-3.403494,3.142112,4.374450,8.232006,6.225689,-5.636625,-3.973104,7.666864,-3.837628,5.848108,8.521484], dtype = "float64")#candidate|12834|(192,)|const|float64
call_12833 = relay.TupleGetItem(func_11771_call(relay.reshape(const_12834.astype('float64'), [4, 4, 12])), 0)
call_12835 = relay.TupleGetItem(func_11774_call(relay.reshape(const_12834.astype('float64'), [4, 4, 12])), 0)
func_8788_call = mod.get_global_var('func_8788')
func_8792_call = mutated_mod.get_global_var('func_8792')
const_12844 = relay.const([[1.504034],[5.736647],[4.378204],[8.112288],[-0.271590],[-7.097699],[3.114385],[2.950722],[-1.995142],[8.456192],[9.939423],[2.827509],[-4.316559],[9.631027],[8.548340],[3.121146],[3.163254],[3.501319],[5.366278],[0.317711],[-9.343077],[-2.310276],[3.296361],[-6.621730],[1.620225],[-5.672975],[-5.256742],[-5.012157],[-8.896052],[7.733663],[1.460150],[-5.444049],[1.836246],[4.472960],[-8.729745],[-9.048652],[-6.055073],[0.781975],[-5.294282],[-5.919970],[3.818448],[3.080166],[-7.480479],[1.734823],[4.791830],[-9.147060],[7.260096],[1.230998],[-3.995077],[9.831688],[0.475147],[9.825692],[-1.452127],[8.418148],[-0.347846],[8.000814]], dtype = "float32")#candidate|12844|(56, 1)|const|float32
var_12845 = relay.var("var_12845", dtype = "float32", shape = (390,))#candidate|12845|(390,)|var|float32
call_12843 = relay.TupleGetItem(func_8788_call(relay.reshape(const_12844.astype('float32'), [56,]), relay.reshape(var_12845.astype('float32'), [5, 78]), ), 3)
call_12846 = relay.TupleGetItem(func_8792_call(relay.reshape(const_12844.astype('float32'), [56,]), relay.reshape(var_12845.astype('float32'), [5, 78]), ), 3)
bop_12849 = relay.multiply(var_12845.astype('uint32'), const_12844.astype('uint32')) # shape=(56, 390)
var_12873 = relay.var("var_12873", dtype = "float32", shape = (35,))#candidate|12873|(35,)|var|float32
bop_12874 = relay.maximum(call_12843.astype('uint64'), relay.reshape(var_12873.astype('uint64'), relay.shape_of(call_12843))) # shape=(35,)
bop_12877 = relay.maximum(call_12846.astype('uint64'), relay.reshape(var_12873.astype('uint64'), relay.shape_of(call_12846))) # shape=(35,)
bop_12879 = relay.left_shift(bop_12849.astype('uint64'), const_12844.astype('uint64')) # shape=(56, 390)
func_5487_call = mod.get_global_var('func_5487')
func_5490_call = mutated_mod.get_global_var('func_5490')
var_12891 = relay.var("var_12891", dtype = "float32", shape = (273,))#candidate|12891|(273,)|var|float32
call_12890 = relay.TupleGetItem(func_5487_call(relay.reshape(var_12891.astype('float32'), [273,])), 7)
call_12892 = relay.TupleGetItem(func_5490_call(relay.reshape(var_12891.astype('float32'), [273,])), 7)
bop_12896 = relay.bitwise_or(call_12890.astype('int64'), const_12844.astype('int64')) # shape=(56, 2288)
bop_12899 = relay.bitwise_or(call_12892.astype('int64'), const_12844.astype('int64')) # shape=(56, 2288)
output = relay.Tuple([call_12806,call_12833,const_12834,bop_12874,bop_12879,var_12891,bop_12896,])
output2 = relay.Tuple([call_12807,call_12835,const_12834,bop_12877,bop_12879,var_12891,bop_12899,])
func_12907 = relay.Function([var_12845,var_12873,var_12891,], output)
mod['func_12907'] = func_12907
mod = relay.transform.InferType()(mod)
mutated_mod['func_12907'] = func_12907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12907_call = mutated_mod.get_global_var('func_12907')
var_12909 = relay.var("var_12909", dtype = "float32", shape = (390,))#candidate|12909|(390,)|var|float32
var_12910 = relay.var("var_12910", dtype = "float32", shape = (35,))#candidate|12910|(35,)|var|float32
var_12911 = relay.var("var_12911", dtype = "float32", shape = (273,))#candidate|12911|(273,)|var|float32
call_12908 = func_12907_call(var_12909,var_12910,var_12911,)
output = call_12908
func_12912 = relay.Function([var_12909,var_12910,var_12911,], output)
mutated_mod['func_12912'] = func_12912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11983_call = mod.get_global_var('func_11983')
func_11984_call = mutated_mod.get_global_var('func_11984')
call_12937 = relay.TupleGetItem(func_11983_call(), 0)
call_12938 = relay.TupleGetItem(func_11984_call(), 0)
func_12907_call = mod.get_global_var('func_12907')
func_12912_call = mutated_mod.get_global_var('func_12912')
var_12953 = relay.var("var_12953", dtype = "float32", shape = (195, 2))#candidate|12953|(195, 2)|var|float32
var_12954 = relay.var("var_12954", dtype = "float32", shape = (35,))#candidate|12954|(35,)|var|float32
var_12955 = relay.var("var_12955", dtype = "float32", shape = (273,))#candidate|12955|(273,)|var|float32
call_12952 = relay.TupleGetItem(func_12907_call(relay.reshape(var_12953.astype('float32'), [390,]), relay.reshape(var_12954.astype('float32'), [35,]), relay.reshape(var_12955.astype('float32'), [273,]), ), 0)
call_12956 = relay.TupleGetItem(func_12912_call(relay.reshape(var_12953.astype('float32'), [390,]), relay.reshape(var_12954.astype('float32'), [35,]), relay.reshape(var_12955.astype('float32'), [273,]), ), 0)
func_12747_call = mod.get_global_var('func_12747')
func_12748_call = mutated_mod.get_global_var('func_12748')
call_12959 = relay.TupleGetItem(func_12747_call(), 1)
call_12960 = relay.TupleGetItem(func_12748_call(), 1)
bop_12963 = relay.bitwise_xor(var_12955.astype('uint16'), call_12959.astype('uint16')) # shape=(10, 8, 273)
bop_12966 = relay.bitwise_xor(var_12955.astype('uint16'), call_12960.astype('uint16')) # shape=(10, 8, 273)
func_11492_call = mod.get_global_var('func_11492')
func_11493_call = mutated_mod.get_global_var('func_11493')
call_12983 = relay.TupleGetItem(func_11492_call(), 0)
call_12984 = relay.TupleGetItem(func_11493_call(), 0)
output = relay.Tuple([call_12937,call_12952,var_12953,var_12954,bop_12963,call_12983,])
output2 = relay.Tuple([call_12938,call_12956,var_12953,var_12954,bop_12966,call_12984,])
func_12986 = relay.Function([var_12953,var_12954,var_12955,], output)
mod['func_12986'] = func_12986
mod = relay.transform.InferType()(mod)
mutated_mod['func_12986'] = func_12986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_12986_call = mutated_mod.get_global_var('func_12986')
var_12988 = relay.var("var_12988", dtype = "float32", shape = (195, 2))#candidate|12988|(195, 2)|var|float32
var_12989 = relay.var("var_12989", dtype = "float32", shape = (35,))#candidate|12989|(35,)|var|float32
var_12990 = relay.var("var_12990", dtype = "float32", shape = (273,))#candidate|12990|(273,)|var|float32
call_12987 = func_12986_call(var_12988,var_12989,var_12990,)
output = call_12987
func_12991 = relay.Function([var_12988,var_12989,var_12990,], output)
mutated_mod['func_12991'] = func_12991
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4610_call = mod.get_global_var('func_4610')
func_4611_call = mutated_mod.get_global_var('func_4611')
call_13006 = relay.TupleGetItem(func_4610_call(), 0)
call_13007 = relay.TupleGetItem(func_4611_call(), 0)
output = call_13006
output2 = call_13007
func_13008 = relay.Function([], output)
mod['func_13008'] = func_13008
mod = relay.transform.InferType()(mod)
mutated_mod['func_13008'] = func_13008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_13008_call = mutated_mod.get_global_var('func_13008')
call_13009 = func_13008_call()
output = call_13009
func_13010 = relay.Function([], output)
mutated_mod['func_13010'] = func_13010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10883_call = mod.get_global_var('func_10883')
func_10885_call = mutated_mod.get_global_var('func_10885')
call_13016 = func_10883_call()
call_13017 = func_10883_call()
func_5333_call = mod.get_global_var('func_5333')
func_5334_call = mutated_mod.get_global_var('func_5334')
call_13031 = relay.TupleGetItem(func_5333_call(), 0)
call_13032 = relay.TupleGetItem(func_5334_call(), 0)
func_8496_call = mod.get_global_var('func_8496')
func_8499_call = mutated_mod.get_global_var('func_8499')
const_13039 = relay.const([-3.114116,8.736350,0.917584,-5.961968,4.515028,0.669143,-5.918853,2.581209,1.559586,5.119089,0.706153,-9.179389,7.141682,-4.149881,9.477737,-6.837139,5.688573,1.312240,-1.640960,-9.662999,0.937910,-4.508990,-1.904473,-8.708355,-5.761502,4.655812,-5.506235,-0.108810,5.703765,-2.989891,-2.743583,7.325386,-3.247012,-0.210903,-1.289733,-9.612189,-9.874726,4.346912,-5.728000,0.172574,5.424920,-7.329883,-9.712642,9.099341,-1.834092,-9.502088,-6.816723,-8.237105,8.384169,5.127451,-9.373324,1.623815,8.225385,9.999098,-1.782856,-1.835441,-2.288952,2.976207,7.853698,-6.624028,-1.580174,-7.207498,-3.490965,7.450500,-8.895674,7.228364,-0.740494,8.039673,9.575365,-5.994200,9.152998,1.363626,6.537568,6.638369,1.551782,-9.122238,-0.162187,-9.940565,-9.553956,-7.242183], dtype = "float64")#candidate|13039|(80,)|const|float64
call_13038 = relay.TupleGetItem(func_8496_call(relay.reshape(const_13039.astype('float64'), [2, 40]), relay.reshape(const_13039.astype('float32'), [2, 40]), ), 13)
call_13040 = relay.TupleGetItem(func_8499_call(relay.reshape(const_13039.astype('float64'), [2, 40]), relay.reshape(const_13039.astype('float32'), [2, 40]), ), 13)
func_11111_call = mod.get_global_var('func_11111')
func_11112_call = mutated_mod.get_global_var('func_11112')
call_13058 = relay.TupleGetItem(func_11111_call(), 0)
call_13059 = relay.TupleGetItem(func_11112_call(), 0)
func_4087_call = mod.get_global_var('func_4087')
func_4090_call = mutated_mod.get_global_var('func_4090')
var_13062 = relay.var("var_13062", dtype = "float32", shape = (192,))#candidate|13062|(192,)|var|float32
call_13061 = relay.TupleGetItem(func_4087_call(relay.reshape(var_13062.astype('float32'), [2, 6, 16]), relay.reshape(var_13062.astype('float32'), [2, 6, 16]), ), 0)
call_13063 = relay.TupleGetItem(func_4090_call(relay.reshape(var_13062.astype('float32'), [2, 6, 16]), relay.reshape(var_13062.astype('float32'), [2, 6, 16]), ), 0)
func_10391_call = mod.get_global_var('func_10391')
func_10392_call = mutated_mod.get_global_var('func_10392')
call_13087 = relay.TupleGetItem(func_10391_call(), 0)
call_13088 = relay.TupleGetItem(func_10392_call(), 0)
output = relay.Tuple([call_13016,call_13031,call_13038,const_13039,call_13058,call_13061,var_13062,call_13087,])
output2 = relay.Tuple([call_13017,call_13032,call_13040,const_13039,call_13059,call_13063,var_13062,call_13088,])
func_13099 = relay.Function([var_13062,], output)
mod['func_13099'] = func_13099
mod = relay.transform.InferType()(mod)
var_13100 = relay.var("var_13100", dtype = "float32", shape = (192,))#candidate|13100|(192,)|var|float32
output = func_13099(var_13100)
func_13101 = relay.Function([var_13100], output)
mutated_mod['func_13101'] = func_13101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8029_call = mod.get_global_var('func_8029')
func_8030_call = mutated_mod.get_global_var('func_8030')
call_13137 = relay.TupleGetItem(func_8029_call(), 0)
call_13138 = relay.TupleGetItem(func_8030_call(), 0)
func_8858_call = mod.get_global_var('func_8858')
func_8860_call = mutated_mod.get_global_var('func_8860')
call_13175 = func_8858_call()
call_13176 = func_8858_call()
bop_13190 = relay.power(call_13175.astype('float64'), call_13137.astype('float64')) # shape=(6, 12, 35)
bop_13193 = relay.power(call_13176.astype('float64'), call_13138.astype('float64')) # shape=(6, 12, 35)
output = bop_13190
output2 = bop_13193
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
	relay.transform.PartialEvaluate(),
	relay.transform.Legalize(),
	relay.transform.FoldConstant(),
	relay.transform.ToANormalForm(),
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
