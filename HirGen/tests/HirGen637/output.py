import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_148 = relay.var("var_148", dtype = "int16", shape = (15, 4, 8))#candidate|148|(15, 4, 8)|var|int16
var_149 = relay.var("var_149", dtype = "int16", shape = (15, 4, 8))#candidate|149|(15, 4, 8)|var|int16
bop_150 = relay.bitwise_or(var_148.astype('int16'), relay.reshape(var_149.astype('int16'), relay.shape_of(var_148))) # shape=(15, 4, 8)
output = bop_150
output2 = bop_150
func_180 = relay.Function([var_148,var_149,], output)
mod['func_180'] = func_180
mod = relay.transform.InferType()(mod)
var_181 = relay.var("var_181", dtype = "int16", shape = (15, 4, 8))#candidate|181|(15, 4, 8)|var|int16
var_182 = relay.var("var_182", dtype = "int16", shape = (15, 4, 8))#candidate|182|(15, 4, 8)|var|int16
output = func_180(var_181,var_182,)
func_183 = relay.Function([var_181,var_182,], output)
mutated_mod['func_183'] = func_183
mutated_mod = relay.transform.InferType()(mutated_mod)
var_322 = relay.var("var_322", dtype = "float32", shape = (7, 6, 4))#candidate|322|(7, 6, 4)|var|float32
var_323 = relay.var("var_323", dtype = "float32", shape = (7, 6, 4))#candidate|323|(7, 6, 4)|var|float32
bop_324 = relay.maximum(var_322.astype('float32'), relay.reshape(var_323.astype('float32'), relay.shape_of(var_322))) # shape=(7, 6, 4)
output = relay.Tuple([bop_324,])
output2 = relay.Tuple([bop_324,])
func_343 = relay.Function([var_322,var_323,], output)
mod['func_343'] = func_343
mod = relay.transform.InferType()(mod)
var_344 = relay.var("var_344", dtype = "float32", shape = (7, 6, 4))#candidate|344|(7, 6, 4)|var|float32
var_345 = relay.var("var_345", dtype = "float32", shape = (7, 6, 4))#candidate|345|(7, 6, 4)|var|float32
output = func_343(var_344,var_345,)
func_346 = relay.Function([var_344,var_345,], output)
mutated_mod['func_346'] = func_346
mutated_mod = relay.transform.InferType()(mutated_mod)
var_439 = relay.var("var_439", dtype = "float64", shape = (1, 10, 12))#candidate|439|(1, 10, 12)|var|float64
uop_440 = relay.log(var_439.astype('float64')) # shape=(1, 10, 12)
output = uop_440
output2 = uop_440
func_460 = relay.Function([var_439,], output)
mod['func_460'] = func_460
mod = relay.transform.InferType()(mod)
var_461 = relay.var("var_461", dtype = "float64", shape = (1, 10, 12))#candidate|461|(1, 10, 12)|var|float64
output = func_460(var_461)
func_462 = relay.Function([var_461], output)
mutated_mod['func_462'] = func_462
mutated_mod = relay.transform.InferType()(mutated_mod)
var_518 = relay.var("var_518", dtype = "uint32", shape = ())#candidate|518|()|var|uint32
var_519 = relay.var("var_519", dtype = "uint32", shape = (16, 11, 8))#candidate|519|(16, 11, 8)|var|uint32
bop_520 = relay.bitwise_and(var_518.astype('uint32'), var_519.astype('uint32')) # shape=(16, 11, 8)
func_460_call = mod.get_global_var('func_460')
func_462_call = mutated_mod.get_global_var('func_462')
const_532 = relay.const([-8.496358,0.232660,-8.693865,-9.290540,-0.916799,0.095473,-1.603172,-6.155274,-7.867450,7.302930,-2.860936,8.175630,6.269943,-7.726187,-2.359370,-2.512084,-4.306306,-1.317084,-0.454189,4.778821,0.411590,7.598423,-3.242280,-3.730879,-0.855843,1.959072,4.352857,-0.972419,-6.010705,-5.360935,-4.527464,4.721527,-0.050992,-7.846567,-0.294679,-4.308857,-9.265405,-2.419464,4.059974,-7.986502,-0.530404,-5.908462,-0.621183,-6.743853,-3.891595,3.313405,-1.283162,7.944916,-5.822757,1.153925,0.213436,-7.475132,8.968029,-9.551749,1.919787,0.035294,-6.223975,-8.696770,-3.587373,0.892429,2.340588,-5.574940,7.569648,-6.550884,6.921970,7.531011,5.123934,-5.437261,-1.957794,8.308058,9.564435,2.581672,3.137907,-6.644238,6.460632,-4.990014,-1.654553,-0.903430,-2.510965,1.574104,-7.012857,-5.914579,-8.862044,-5.407426,8.886845,5.355283,-4.190032,-4.958870,-1.135957,-8.386005,5.483918,-7.708167,9.865569,5.088254,2.931670,4.485081,9.873550,-3.201307,-8.340111,-6.078364,-8.326584,0.122514,6.992682,-2.473566,-5.893959,7.215598,7.531797,-3.519556,-5.845791,-4.423384,-7.415697,8.948796,3.015677,-2.278660,-3.170480,8.343789,-2.596429,-3.055261,5.042591,5.413238], dtype = "float64")#candidate|532|(120,)|const|float64
call_531 = func_460_call(relay.reshape(const_532.astype('float64'), [1, 10, 12]))
call_533 = func_460_call(relay.reshape(const_532.astype('float64'), [1, 10, 12]))
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
const_536 = relay.const([-3,7,2,-10,5,-7,-8,2,-1,-1,7,6,1,-5,1,5,2,-3,4,-7,5,-8,10,2,2,-4,-1,-2,-2,-9,6,-5,5,-5,3,10,5,-3,-9,4,-10,2,-9,-2,-3,2,-2,-10,-8,8,4,-9,7,3,9,-7,8,-10,8,-7,-2,2,9,1,-6,9,6,-10,2,-8,3,-9,9,-9,1,7,7,7,3,1,8,3,8,6,-9,2,-10,-2,-2,5,6,-7,3,-7,2,10,-8,4,6,-7,-4,6,1,4,-10,-7,1,9,5,-4,6,9,-9,-3,4,-10,10,-4,-6,4,-5,4,2,4,1,-8,-2,-4,-1,5,-6,4,5,-9,-6,8,-4,1,-6,-7,3,-6,2,7,7,-1,-9,1,4,-4,4,4,-4,8,-10,-1,-10,-7,6,-8,-7,6,-3,-9,-8,7,-7,-4,6,5,6,-10,-10,1,-2,-7,-5,5,1,-4,7,2,2,6,-7,5,-4,2,-3,-2,-1,2,-3,3,-10,-2,8,-2,-10,-10,9,2,2,1,-6,-8,1,2,-6,-7,-2,5,5,-10,-6,-1,6,10,9,3,2,2,-3,9,-1,-6,-9,3,-8,6,3,-9,-3,7,10,-7,1,-8,-6,-4,7,-10,-2,-8,-5,-4,-4,-7,4,10,6,-6,7,-3,-3,9,-8,-6,-1,-3,-1,-3,2,3,-6,9,10,-8,9,3,-8,-2,1,-9,2,-9,10,1,1,-9,-9,-8,-4,-8,-10,5,-3,-6,-4,-9,6,-3,-9,8,8,-9,-6,8,5,-2,-6,5,-5,8,-4,8,-4,-6,-5,4,-2,2,2,-5,-5,4,-6,-5,-7,-10,7,-1,-1,5,-9,-3,4,8,-7,-4,2,8,-4,8,-3,2,-8,-2,-8,-7,9,-10,7,-10,-3,-1,-10,-2,9,8,8,-3,-3,-5,3,1,-4,-5,-9,9,7,8,6,-6,9,8,-3,6,-5,8,5,-10,-10,-3,-9,-2,2,-8,1,-5,7,10,2,6,8,-5,-5,3,-1,-8,-1,-9,-2,1,-10,-6,10,6,3,-1,-8,-6,-3,-2,-7,5,1,-1,2,8,10,6,9,4,-4,3,-5,-8,-7,-5,9,2,-5,-4,-5,-8,6,5,-5,-5,7,-2,-4,3,1,8,9,1,-3,10,9,2,-1,9,9,-5,-4,9,7,1,-1,7,9,3,-5,9,-2,-1,10,-8,-6,5,2,-7,-9,7,7,9,4,-9,6,4,1,-10,-7,-9,-3,-2,2,4], dtype = "int16")#candidate|536|(480,)|const|int16
call_535 = func_180_call(relay.reshape(const_536.astype('int16'), [15, 4, 8]), relay.reshape(const_536.astype('int16'), [15, 4, 8]), )
call_537 = func_180_call(relay.reshape(const_536.astype('int16'), [15, 4, 8]), relay.reshape(const_536.astype('int16'), [15, 4, 8]), )
output = relay.Tuple([bop_520,call_531,const_532,call_535,const_536,])
output2 = relay.Tuple([bop_520,call_533,const_532,call_537,const_536,])
func_544 = relay.Function([var_518,var_519,], output)
mod['func_544'] = func_544
mod = relay.transform.InferType()(mod)
mutated_mod['func_544'] = func_544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_544_call = mutated_mod.get_global_var('func_544')
var_546 = relay.var("var_546", dtype = "uint32", shape = ())#candidate|546|()|var|uint32
var_547 = relay.var("var_547", dtype = "uint32", shape = (16, 11, 8))#candidate|547|(16, 11, 8)|var|uint32
call_545 = func_544_call(var_546,var_547,)
output = call_545
func_548 = relay.Function([var_546,var_547,], output)
mutated_mod['func_548'] = func_548
mutated_mod = relay.transform.InferType()(mutated_mod)
var_826 = relay.var("var_826", dtype = "int16", shape = (7, 2, 6))#candidate|826|(7, 2, 6)|var|int16
var_827 = relay.var("var_827", dtype = "int16", shape = (7, 2, 6))#candidate|827|(7, 2, 6)|var|int16
bop_828 = relay.right_shift(var_826.astype('int16'), relay.reshape(var_827.astype('int16'), relay.shape_of(var_826))) # shape=(7, 2, 6)
bop_835 = relay.bitwise_or(bop_828.astype('int8'), relay.reshape(var_826.astype('int8'), relay.shape_of(bop_828))) # shape=(7, 2, 6)
const_845 = relay.const([[[-9,-6,6,2,7,1],[-5,4,-1,4,-4,-5]],[[-4,-8,5,7,-4,-8],[10,-6,-3,4,3,-10]],[[6,2,-4,1,-9,3],[1,-7,-4,5,6,-10]],[[6,6,1,-4,9,-10],[-6,-1,10,-8,-5,-5]],[[-3,-2,10,7,-7,7],[-1,6,8,5,7,-8]],[[9,9,4,-10,2,5],[5,2,-9,9,-10,1]],[[10,-2,1,5,8,1],[-8,9,4,-4,8,-10]]], dtype = "int8")#candidate|845|(7, 2, 6)|const|int8
bop_846 = relay.maximum(bop_835.astype('int16'), relay.reshape(const_845.astype('int16'), relay.shape_of(bop_835))) # shape=(7, 2, 6)
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
var_851 = relay.var("var_851", dtype = "int16", shape = (480,))#candidate|851|(480,)|var|int16
call_850 = func_180_call(relay.reshape(var_851.astype('int16'), [15, 4, 8]), relay.reshape(var_851.astype('int16'), [15, 4, 8]), )
call_852 = func_180_call(relay.reshape(var_851.astype('int16'), [15, 4, 8]), relay.reshape(var_851.astype('int16'), [15, 4, 8]), )
var_857 = relay.var("var_857", dtype = "int8", shape = (7, 2, 6))#candidate|857|(7, 2, 6)|var|int8
bop_858 = relay.left_shift(bop_835.astype('uint32'), relay.reshape(var_857.astype('uint32'), relay.shape_of(bop_835))) # shape=(7, 2, 6)
output = relay.Tuple([bop_846,call_850,var_851,bop_858,])
output2 = relay.Tuple([bop_846,call_852,var_851,bop_858,])
func_867 = relay.Function([var_826,var_827,var_851,var_857,], output)
mod['func_867'] = func_867
mod = relay.transform.InferType()(mod)
var_868 = relay.var("var_868", dtype = "int16", shape = (7, 2, 6))#candidate|868|(7, 2, 6)|var|int16
var_869 = relay.var("var_869", dtype = "int16", shape = (7, 2, 6))#candidate|869|(7, 2, 6)|var|int16
var_870 = relay.var("var_870", dtype = "int16", shape = (480,))#candidate|870|(480,)|var|int16
var_871 = relay.var("var_871", dtype = "int8", shape = (7, 2, 6))#candidate|871|(7, 2, 6)|var|int8
output = func_867(var_868,var_869,var_870,var_871,)
func_872 = relay.Function([var_868,var_869,var_870,var_871,], output)
mutated_mod['func_872'] = func_872
mutated_mod = relay.transform.InferType()(mutated_mod)
const_883 = relay.const([[[1.075796,-6.898724,7.269347],[-8.332474,8.875013,-8.400362],[3.074214,-4.806606,3.016195],[9.948190,-2.585366,9.837261]],[[-4.119038,-9.346683,-2.208863],[-7.645867,2.283940,9.243184],[-5.519474,-3.473467,0.817740],[2.106520,-7.822730,0.844489]],[[-9.296126,6.330921,-3.371941],[8.766210,-6.616890,6.402413],[8.481031,0.425793,-4.386049],[-2.014694,-5.729778,-8.394570]]], dtype = "float64")#candidate|883|(3, 4, 3)|const|float64
uop_884 = relay.acos(const_883.astype('float64')) # shape=(3, 4, 3)
output = uop_884
output2 = uop_884
func_886 = relay.Function([], output)
mod['func_886'] = func_886
mod = relay.transform.InferType()(mod)
mutated_mod['func_886'] = func_886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mutated_mod.get_global_var('func_886')
call_887 = func_886_call()
output = call_887
func_888 = relay.Function([], output)
mutated_mod['func_888'] = func_888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_891 = func_886_call()
call_892 = func_886_call()
output = relay.Tuple([call_891,])
output2 = relay.Tuple([call_892,])
func_893 = relay.Function([], output)
mod['func_893'] = func_893
mod = relay.transform.InferType()(mod)
output = func_893()
func_894 = relay.Function([], output)
mutated_mod['func_894'] = func_894
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_898 = func_886_call()
call_899 = func_886_call()
output = relay.Tuple([call_898,])
output2 = relay.Tuple([call_899,])
func_904 = relay.Function([], output)
mod['func_904'] = func_904
mod = relay.transform.InferType()(mod)
mutated_mod['func_904'] = func_904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mutated_mod.get_global_var('func_904')
call_905 = func_904_call()
output = call_905
func_906 = relay.Function([], output)
mutated_mod['func_906'] = func_906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_943 = relay.TupleGetItem(func_904_call(), 0)
call_944 = relay.TupleGetItem(func_906_call(), 0)
output = call_943
output2 = call_944
func_946 = relay.Function([], output)
mod['func_946'] = func_946
mod = relay.transform.InferType()(mod)
output = func_946()
func_947 = relay.Function([], output)
mutated_mod['func_947'] = func_947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_1032 = relay.TupleGetItem(func_893_call(), 0)
call_1033 = relay.TupleGetItem(func_894_call(), 0)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_1039 = relay.TupleGetItem(func_893_call(), 0)
call_1040 = relay.TupleGetItem(func_894_call(), 0)
output = relay.Tuple([call_1032,call_1039,])
output2 = relay.Tuple([call_1033,call_1040,])
func_1044 = relay.Function([], output)
mod['func_1044'] = func_1044
mod = relay.transform.InferType()(mod)
mutated_mod['func_1044'] = func_1044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mutated_mod.get_global_var('func_1044')
call_1045 = func_1044_call()
output = call_1045
func_1046 = relay.Function([], output)
mutated_mod['func_1046'] = func_1046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1066 = func_886_call()
call_1067 = func_886_call()
uop_1072 = relay.asinh(call_1066.astype('float64')) # shape=(3, 4, 3)
uop_1074 = relay.asinh(call_1067.astype('float64')) # shape=(3, 4, 3)
bop_1091 = relay.bitwise_or(uop_1072.astype('int16'), relay.reshape(call_1066.astype('int16'), relay.shape_of(uop_1072))) # shape=(3, 4, 3)
bop_1094 = relay.bitwise_or(uop_1074.astype('int16'), relay.reshape(call_1067.astype('int16'), relay.shape_of(uop_1074))) # shape=(3, 4, 3)
output = bop_1091
output2 = bop_1094
func_1095 = relay.Function([], output)
mod['func_1095'] = func_1095
mod = relay.transform.InferType()(mod)
output = func_1095()
func_1096 = relay.Function([], output)
mutated_mod['func_1096'] = func_1096
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1130 = func_886_call()
call_1131 = func_886_call()
uop_1134 = relay.exp(call_1130.astype('float64')) # shape=(3, 4, 3)
uop_1136 = relay.exp(call_1131.astype('float64')) # shape=(3, 4, 3)
output = uop_1134
output2 = uop_1136
func_1140 = relay.Function([], output)
mod['func_1140'] = func_1140
mod = relay.transform.InferType()(mod)
output = func_1140()
func_1141 = relay.Function([], output)
mutated_mod['func_1141'] = func_1141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1200 = func_886_call()
call_1201 = func_886_call()
var_1206 = relay.var("var_1206", dtype = "float64", shape = (3, 4, 3))#candidate|1206|(3, 4, 3)|var|float64
bop_1207 = relay.subtract(call_1200.astype('uint16'), relay.reshape(var_1206.astype('uint16'), relay.shape_of(call_1200))) # shape=(3, 4, 3)
bop_1210 = relay.subtract(call_1201.astype('uint16'), relay.reshape(var_1206.astype('uint16'), relay.shape_of(call_1201))) # shape=(3, 4, 3)
uop_1211 = relay.cosh(call_1200.astype('float32')) # shape=(3, 4, 3)
uop_1213 = relay.cosh(call_1201.astype('float32')) # shape=(3, 4, 3)
uop_1220 = relay.log10(call_1200.astype('float32')) # shape=(3, 4, 3)
uop_1222 = relay.log10(call_1201.astype('float32')) # shape=(3, 4, 3)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_1224 = func_1095_call()
call_1225 = func_1095_call()
bop_1226 = relay.less(uop_1211.astype('bool'), relay.reshape(call_1200.astype('bool'), relay.shape_of(uop_1211))) # shape=(3, 4, 3)
bop_1229 = relay.less(uop_1213.astype('bool'), relay.reshape(call_1201.astype('bool'), relay.shape_of(uop_1213))) # shape=(3, 4, 3)
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
var_1249 = relay.var("var_1249", dtype = "int16", shape = (480,))#candidate|1249|(480,)|var|int16
call_1248 = func_180_call(relay.reshape(var_1249.astype('int16'), [15, 4, 8]), relay.reshape(var_1249.astype('int16'), [15, 4, 8]), )
call_1250 = func_180_call(relay.reshape(var_1249.astype('int16'), [15, 4, 8]), relay.reshape(var_1249.astype('int16'), [15, 4, 8]), )
output = relay.Tuple([bop_1207,uop_1220,call_1224,bop_1226,call_1248,var_1249,])
output2 = relay.Tuple([bop_1210,uop_1222,call_1225,bop_1229,call_1250,var_1249,])
func_1253 = relay.Function([var_1206,var_1249,], output)
mod['func_1253'] = func_1253
mod = relay.transform.InferType()(mod)
var_1254 = relay.var("var_1254", dtype = "float64", shape = (3, 4, 3))#candidate|1254|(3, 4, 3)|var|float64
var_1255 = relay.var("var_1255", dtype = "int16", shape = (480,))#candidate|1255|(480,)|var|int16
output = func_1253(var_1254,var_1255,)
func_1256 = relay.Function([var_1254,var_1255,], output)
mutated_mod['func_1256'] = func_1256
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1273 = relay.var("var_1273", dtype = "float32", shape = (7, 9, 9))#candidate|1273|(7, 9, 9)|var|float32
var_1274 = relay.var("var_1274", dtype = "float32", shape = (7, 9, 9))#candidate|1274|(7, 9, 9)|var|float32
bop_1275 = relay.floor_divide(var_1273.astype('float32'), relay.reshape(var_1274.astype('float32'), relay.shape_of(var_1273))) # shape=(7, 9, 9)
output = bop_1275
output2 = bop_1275
func_1281 = relay.Function([var_1273,var_1274,], output)
mod['func_1281'] = func_1281
mod = relay.transform.InferType()(mod)
mutated_mod['func_1281'] = func_1281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1281_call = mutated_mod.get_global_var('func_1281')
var_1283 = relay.var("var_1283", dtype = "float32", shape = (7, 9, 9))#candidate|1283|(7, 9, 9)|var|float32
var_1284 = relay.var("var_1284", dtype = "float32", shape = (7, 9, 9))#candidate|1284|(7, 9, 9)|var|float32
call_1282 = func_1281_call(var_1283,var_1284,)
output = call_1282
func_1285 = relay.Function([var_1283,var_1284,], output)
mutated_mod['func_1285'] = func_1285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1046_call = mutated_mod.get_global_var('func_1046')
call_1352 = relay.TupleGetItem(func_1044_call(), 1)
call_1353 = relay.TupleGetItem(func_1046_call(), 1)
var_1373 = relay.var("var_1373", dtype = "float64", shape = (3, 4, 3))#candidate|1373|(3, 4, 3)|var|float64
bop_1374 = relay.logical_or(call_1352.astype('bool'), relay.reshape(var_1373.astype('bool'), relay.shape_of(call_1352))) # shape=(3, 4, 3)
bop_1377 = relay.logical_or(call_1353.astype('bool'), relay.reshape(var_1373.astype('bool'), relay.shape_of(call_1353))) # shape=(3, 4, 3)
output = relay.Tuple([bop_1374,])
output2 = relay.Tuple([bop_1377,])
func_1383 = relay.Function([var_1373,], output)
mod['func_1383'] = func_1383
mod = relay.transform.InferType()(mod)
var_1384 = relay.var("var_1384", dtype = "float64", shape = (3, 4, 3))#candidate|1384|(3, 4, 3)|var|float64
output = func_1383(var_1384)
func_1385 = relay.Function([var_1384], output)
mutated_mod['func_1385'] = func_1385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1393 = func_886_call()
call_1394 = func_886_call()
output = relay.Tuple([call_1393,])
output2 = relay.Tuple([call_1394,])
func_1409 = relay.Function([], output)
mod['func_1409'] = func_1409
mod = relay.transform.InferType()(mod)
output = func_1409()
func_1410 = relay.Function([], output)
mutated_mod['func_1410'] = func_1410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1443 = relay.var("var_1443", dtype = "uint16", shape = (1, 15, 14))#candidate|1443|(1, 15, 14)|var|uint16
var_1444 = relay.var("var_1444", dtype = "uint16", shape = (1, 15, 14))#candidate|1444|(1, 15, 14)|var|uint16
bop_1445 = relay.left_shift(var_1443.astype('uint16'), relay.reshape(var_1444.astype('uint16'), relay.shape_of(var_1443))) # shape=(1, 15, 14)
bop_1452 = relay.subtract(var_1444.astype('uint16'), relay.reshape(bop_1445.astype('uint16'), relay.shape_of(var_1444))) # shape=(1, 15, 14)
output = relay.Tuple([bop_1452,])
output2 = relay.Tuple([bop_1452,])
func_1469 = relay.Function([var_1443,var_1444,], output)
mod['func_1469'] = func_1469
mod = relay.transform.InferType()(mod)
mutated_mod['func_1469'] = func_1469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1469_call = mutated_mod.get_global_var('func_1469')
var_1471 = relay.var("var_1471", dtype = "uint16", shape = (1, 15, 14))#candidate|1471|(1, 15, 14)|var|uint16
var_1472 = relay.var("var_1472", dtype = "uint16", shape = (1, 15, 14))#candidate|1472|(1, 15, 14)|var|uint16
call_1470 = func_1469_call(var_1471,var_1472,)
output = call_1470
func_1473 = relay.Function([var_1471,var_1472,], output)
mutated_mod['func_1473'] = func_1473
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1475 = func_886_call()
call_1476 = func_886_call()
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_1501 = relay.TupleGetItem(func_893_call(), 0)
call_1502 = relay.TupleGetItem(func_894_call(), 0)
uop_1514 = relay.erf(call_1501.astype('float32')) # shape=(3, 4, 3)
uop_1516 = relay.erf(call_1502.astype('float32')) # shape=(3, 4, 3)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1531 = func_886_call()
call_1532 = func_886_call()
func_1469_call = mod.get_global_var('func_1469')
func_1473_call = mutated_mod.get_global_var('func_1473')
const_1538 = relay.const([-5,-10,5,10,-6,6,-4,-8,-5,-8,-5,-8,1,5,10,-9,-3,2,2,10,1,-3,-10,-9,-6,-3,-5,1,-4,1,6,-2,2,9,-6,-1,-6,1,5,-8,-8,-2,-3,-9,1,10,2,6,-6,8,-5,-10,-1,-6,10,7,-8,-10,-4,-7,-9,-4,-1,-6,7,-10,3,3,8,2,5,7,-10,4,8,-3,-8,-1,-9,-5,-1,9,4,7,5,-3,9,-6,9,-5,1,7,4,10,4,-10,-10,-8,4,8,7,10,1,6,-5,-8,-10,-6,2,-10,1,3,10,10,9,1,-9,-1,-6,2,-10,10,7,6,3,-8,-7,-8,2,-3,5,-4,-7,-7,-2,6,3,-3,1,-2,7,-9,-10,-3,6,-3,10,-7,4,1,7,9,-3,-10,4,-9,3,7,-6,8,-8,4,8,-6,9,10,5,6,4,2,-10,-8,2,8,10,1,5,-6,9,7,9,6,9,-2,9,-10,9,-2,5,-1,6,-1,-9,5,-10,8,2,-1,-5,3,-9,3,-10,8,-6,10,-1,2,9,8], dtype = "uint16")#candidate|1538|(210,)|const|uint16
call_1537 = relay.TupleGetItem(func_1469_call(relay.reshape(const_1538.astype('uint16'), [1, 15, 14]), relay.reshape(const_1538.astype('uint16'), [1, 15, 14]), ), 0)
call_1539 = relay.TupleGetItem(func_1473_call(relay.reshape(const_1538.astype('uint16'), [1, 15, 14]), relay.reshape(const_1538.astype('uint16'), [1, 15, 14]), ), 0)
uop_1543 = relay.cos(uop_1514.astype('float32')) # shape=(3, 4, 3)
uop_1545 = relay.cos(uop_1516.astype('float32')) # shape=(3, 4, 3)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_1549 = func_886_call()
call_1550 = func_886_call()
func_544_call = mod.get_global_var('func_544')
func_548_call = mutated_mod.get_global_var('func_548')
const_1554 = relay.const(-4, dtype = "uint32")#candidate|1554|()|const|uint32
const_1555 = relay.const([-1,-2,-1,-2,6,2,7,-9,1,-6,1,-3,5,-8,-6,3,-8,-4,8,4,5,-8,-1,5,-5,3,4,-8,6,8,-8,1,-9,-5,-3,3,-6,-2,1,9,10,-9,-9,-3,-2,-7,5,-8,-7,3,1,-7,6,6,-9,-3,-8,-3,-1,2,-9,-6,10,-9,9,6,6,7,-5,1,-7,-10,9,3,-10,-3,-5,1,5,2,-2,3,2,-1,-4,-10,9,7,-3,-7,-5,-2,-1,6,5,-9,-6,4,-2,-8,1,9,-8,-9,-7,6,9,4,10,-6,-10,1,-5,8,2,-6,-4,5,1,2,2,-2,5,1,-10,10,1,-7,-6,8,3,-5,10,8,5,1,-10,-2,-3,-8,-1,-2,-2,1,-6,-8,-4,5,-4,-7,-4,10,-5,7,-5,-8,5,-1,9,-5,-10,5,9,-9,-4,3,7,2,-6,-8,5,-9,6,-7,1,-1,8,-6,5,-9,-2,-6,6,8,6,4,2,2,-1,-2,-5,-3,8,-2,-5,-1,-3,-5,-5,-4,-1,-2,2,-2,7,7,-8,6,10,-8,-9,3,5,5,-2,-1,-7,-9,-1,2,-6,1,-9,-1,-5,7,7,-5,7,2,-7,4,10,-3,-4,-8,-3,-6,3,5,-4,1,-10,6,6,-1,-3,-9,10,-3,-6,-7,-7,3,-8,-10,-1,-8,7,10,-1,6,-6,6,-6,10,-7,3,10,8,6,-4,8,8,3,-7,-9,-8,-10,10,-3,-10,-9,-8,10,-7,-3,3,-1,5,1,10,-8,6,3,6,8,6,-8,6,-8,4,4,-3,8,-10,-3,-8,9,9,-10,5,10,7,6,5,6,7,7,-6,-9,6,9,3,8,7,8,9,-5,-5,8,7,9,6,6,-3,-10,-9,4,4,-5,-1,-5,10,-5,-3,4,10,5,-1,8,8,-4,-5,-10,-10,4,-5,-10,-10,-9,-1,-4,8,7,-2,3,2,-8,4,8,10,-5,-2,1,1,5,-5,-5,8,-2,4,2,-3,-5,-8,-2,6,7,-2,7,10,-9,3,-10,3,-3,7,5,10,6,-2,8,6,5,6,3,-6,-5,-4,9,-6,4,-2,1,8,9,8,9,5,-1,-6,10,-7,-2,-9,10,-7,-9,5,8,9,-3,-5,10,6,4,6,-5,-9,5,10,-7,2,-6,6,-8,1,4,6,7,-7,-4,-5,7,-8,5,-10,6,6,6,-6,-1,-8,5,10,3,-3,10,8,1,2,7,-8,-1,-7,-10,-1,-1,7,2,8,-5,-4,8,-4,1,4,-7,3,9,-7,4,-10,-9,-3,-4,-6,-9,-6,4,5,-6,-3,5,3,7,-3,-7,8,-1,5,-1,4,3,8,-10,1,5,-10,-10,-4,-2,8,1,-5,6,-6,3,8,10,3,10,-7,-8,3,8,4,4,9,-9,-6,4,-3,-3,-3,8,4,-2,1,8,9,-1,5,-7,1,-9,-3,2,-2,-9,-10,10,5,7,-1,9,-10,-5,6,-1,9,5,-5,-10,-1,-1,-7,7,3,5,-6,8,-5,-2,4,-9,3,5,-2,-2,-3,6,-4,-2,-4,4,3,7,-2,10,-10,9,6,1,8,-3,-6,2,9,-8,-3,6,-4,-6,1,2,-9,-5,4,3,1,2,-4,-9,10,-7,-2,9,-5,2,-4,-9,7,8,-2,-5,8,2,4,4,-1,-7,5,8,-4,7,-7,9,-10,7,-9,-7,-2,6,2,-9,2,-7,3,-8,-8,-5,1,10,10,-5,2,5,-3,-1,10,10,-8,-8,2,10,-2,4,-6,7,4,8,-6,-1,3,-5,-3,-4,10,2,9,-2,4,4,-10,9,-5,-1,7,1,5,-2,9,-7,-9,10,2,8,-8,7,3,4,-2,-8,-9,10,3,2,9,2,2,-5,6,10,4,-3,-5,5,-4,-8,-10,-8,-2,4,4,9,-9,-10,-8,8,8,-10,-8,10,-8,6,-9,-10,9,-2,1,8,-6,3,-1,-7,-4,-3,10,6,-2,-5,-9,1,10,-10,5,-10,-8,-4,-6,9,-7,-2,-4,6,-1,8,-5,-7,-2,-5,4,-9,-10,3,-3,-4,3,-9,4,-4,6,4,-2,-8,9,3,-1,-8,-5,-5,-1,1,6,-2,5,5,9,3,-2,8,-4,-5,-1,-6,-3,-5,1,-10,-7,-5,-10,4,-10,3,-9,3,9,-10,2,7,6,-2,1,4,-8,-10,9,-10,-2,3,1,7,-6,2,-5,-3,-4,-10,1,-1,-2,5,-7,-2,-7,2,-1,-10,8,-2,3,-5,-2,-10,-8,-10,-1,4,2,-7,-1,7,-10,8,10,-2,-7,8,2,2,10,-10,1,-9,10,-1,8,2,6,-7,-1,-9,-8,10,6,9,8,-7,5,-1,5,-7,-2,1,10,6,7,-2,4,-6,-5,-6,-8,1,10,-10,4,6,-8,-5,4,-4,7,-7,-7,1,10,5,10,-1,8,5,-1,-1,9,9,-7,6,8,-5,8,9,5,6,-1,-8,-8,-4,-8,-8,-1,10,-10,4,-10,3,6,4,5,7,-8,-7,-9,-7,-6,-4,4,4,8,1,6,-6,7,6,-1,-10,-7,5,-7,-5,-7,-7,2,-6,9,10,3,-2,7,2,10,-7,8,4,-4,6,7,4,-7,10,8,-3,-8,-3,2,3,7,8,-3,1,-1,-1,-4,-10,7,-7,1,-10,-7,-2,-8,9,-6,-1,9,-6,-2,-1,-6,-7,10,-10,8,-8,2,-1,6,6,-7,8,-10,8,-3,-8,9,-4,3,-10,5,-3,-7,-7,-6,-4,9,-9,-8,3,-6,-2,8,4,9,2,1,3,2,2,3,1,1,1,8,3,-6,-1,-3,8,8,-8,-5,-8,8,-5,7,3,5,-7,9,-9,7,1,-4,3,-9,4,1,3,3,2,-3,7,-10,-10,-6,-6,-8,4,8,-5,-8,4,-10,-9,-4,-2,6,4,-6,7,-5,5,-9,-5,-6,-5,1,2,-6,-4,-1,-7,6,5,8,-3,4,-6,9,-2,-6,-9,-8,-8,-3,-5,9,-5,3,-6,-1,-6,9,10,5,-2,8,-6,4,1,6,-4,-7,-9,-9,3,-4,-5,-3,8,6,7,-3,10,-8,-5,-6,7,-7,6,-1,-8,-10,-5,-7,-8,-5,6,-9,5,7,2,-10,7,-7,-5,-1,-1,-5,3,1,4,-8,6,-7,7,-1,-9,9,-10,10,3,8,4,4,5,9,-3,-10,-6,-10,-4,9,-3,1,5,9,-3,-3,2,4,-3,7,-10,5,-7,-7,7,2,6,-3,5,8,1,-4,-9,10,-9,-9,5,5,8,-1,-1,3,8,-8,-2,-2,-10,-5,3,2,-4,5,3,-1,3,6,-9,-1,6,2,6,10,10,-4,5,-7,6,-10,3,10,5,9,-6,3,-8,10,10,-9,-9,3,8,3,-3,5,-4,9,-2,5,7,-7,-4,-10,-9,5,1,-4,-8,-4,-9,5,3,-5,4,-10,10,7,-6,-10,-5,7,-3,-6,-7,1,7,-1,2,5,8,7,3,-3,3,8,-8,-4,3,1,-8,7,-10,8,-4,8,-6,-9,-2,-2,6,3,-4,-3,6,-6,-6,-2,1,8,2,-9,-2,-1,-3,-9,2,2,-8,-2,9,-1,-3,3,4,1,-9,4,1,8,-8,-2,7,-6,-9,1,6,-6,4,3,1,4,6,-3,-7,8,6,-6,6,-1,-8,-6,2,-3], dtype = "uint32")#candidate|1555|(1408,)|const|uint32
call_1553 = relay.TupleGetItem(func_544_call(relay.reshape(const_1554.astype('uint32'), []), relay.reshape(const_1555.astype('uint32'), [16, 11, 8]), ), 4)
call_1556 = relay.TupleGetItem(func_548_call(relay.reshape(const_1554.astype('uint32'), []), relay.reshape(const_1555.astype('uint32'), [16, 11, 8]), ), 4)
output = relay.Tuple([call_1475,call_1531,call_1537,const_1538,uop_1543,call_1549,call_1553,const_1554,const_1555,])
output2 = relay.Tuple([call_1476,call_1532,call_1539,const_1538,uop_1545,call_1550,call_1556,const_1554,const_1555,])
func_1561 = relay.Function([], output)
mod['func_1561'] = func_1561
mod = relay.transform.InferType()(mod)
output = func_1561()
func_1562 = relay.Function([], output)
mutated_mod['func_1562'] = func_1562
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_1592 = func_1140_call()
call_1593 = func_1140_call()
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
var_1615 = relay.var("var_1615", dtype = "int16", shape = (480,))#candidate|1615|(480,)|var|int16
call_1614 = func_180_call(relay.reshape(var_1615.astype('int16'), [15, 4, 8]), relay.reshape(var_1615.astype('int16'), [15, 4, 8]), )
call_1616 = func_180_call(relay.reshape(var_1615.astype('int16'), [15, 4, 8]), relay.reshape(var_1615.astype('int16'), [15, 4, 8]), )
output = relay.Tuple([call_1592,call_1614,var_1615,])
output2 = relay.Tuple([call_1593,call_1616,var_1615,])
func_1618 = relay.Function([var_1615,], output)
mod['func_1618'] = func_1618
mod = relay.transform.InferType()(mod)
var_1619 = relay.var("var_1619", dtype = "int16", shape = (480,))#candidate|1619|(480,)|var|int16
output = func_1618(var_1619)
func_1620 = relay.Function([var_1619], output)
mutated_mod['func_1620'] = func_1620
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1628 = relay.var("var_1628", dtype = "float64", shape = (4, 1, 5))#candidate|1628|(4, 1, 5)|var|float64
uop_1629 = relay.sqrt(var_1628.astype('float64')) # shape=(4, 1, 5)
bop_1631 = relay.subtract(uop_1629.astype('uint32'), relay.reshape(var_1628.astype('uint32'), relay.shape_of(uop_1629))) # shape=(4, 1, 5)
output = relay.Tuple([bop_1631,])
output2 = relay.Tuple([bop_1631,])
func_1650 = relay.Function([var_1628,], output)
mod['func_1650'] = func_1650
mod = relay.transform.InferType()(mod)
var_1651 = relay.var("var_1651", dtype = "float64", shape = (4, 1, 5))#candidate|1651|(4, 1, 5)|var|float64
output = func_1650(var_1651)
func_1652 = relay.Function([var_1651], output)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_1706 = relay.TupleGetItem(func_904_call(), 0)
call_1707 = relay.TupleGetItem(func_906_call(), 0)
uop_1716 = relay.log2(call_1706.astype('float32')) # shape=(3, 4, 3)
uop_1718 = relay.log2(call_1707.astype('float32')) # shape=(3, 4, 3)
output = uop_1716
output2 = uop_1718
func_1727 = relay.Function([], output)
mod['func_1727'] = func_1727
mod = relay.transform.InferType()(mod)
output = func_1727()
func_1728 = relay.Function([], output)
mutated_mod['func_1728'] = func_1728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_1763 = func_1095_call()
call_1764 = func_1095_call()
output = call_1763
output2 = call_1764
func_1779 = relay.Function([], output)
mod['func_1779'] = func_1779
mod = relay.transform.InferType()(mod)
mutated_mod['func_1779'] = func_1779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1779_call = mutated_mod.get_global_var('func_1779')
call_1780 = func_1779_call()
output = call_1780
func_1781 = relay.Function([], output)
mutated_mod['func_1781'] = func_1781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_1806 = relay.TupleGetItem(func_904_call(), 0)
call_1807 = relay.TupleGetItem(func_906_call(), 0)
func_1253_call = mod.get_global_var('func_1253')
func_1256_call = mutated_mod.get_global_var('func_1256')
var_1820 = relay.var("var_1820", dtype = "int16", shape = (480,))#candidate|1820|(480,)|var|int16
call_1819 = relay.TupleGetItem(func_1253_call(relay.reshape(call_1806.astype('float64'), [3, 4, 3]), relay.reshape(var_1820.astype('int16'), [480,]), ), 0)
call_1821 = relay.TupleGetItem(func_1256_call(relay.reshape(call_1806.astype('float64'), [3, 4, 3]), relay.reshape(var_1820.astype('int16'), [480,]), ), 0)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_1833 = relay.TupleGetItem(func_904_call(), 0)
call_1834 = relay.TupleGetItem(func_906_call(), 0)
func_544_call = mod.get_global_var('func_544')
func_548_call = mutated_mod.get_global_var('func_548')
const_1842 = relay.const(-2, dtype = "uint32")#candidate|1842|()|const|uint32
const_1843 = relay.const([[6,-10,-8,-8],[4,1,6,-4],[-5,4,10,-7],[9,-1,-7,10],[5,-10,2,-9],[8,2,-7,8],[-5,5,8,-6],[-7,-8,4,-10],[7,1,7,-10],[3,-10,-6,4],[1,-1,-3,-7],[-5,-9,-2,7],[8,-1,-1,-10],[2,-5,-8,-4],[-10,1,-1,8],[-3,7,3,-7],[4,-5,-10,9],[7,-2,3,-6],[-8,-8,7,-7],[2,-8,-7,-7],[-4,8,-9,5],[9,3,-1,6],[-7,-10,-2,-5],[-10,1,-9,-10],[1,8,-5,8],[-10,7,-1,3],[-7,2,-10,6],[-1,9,5,4],[7,8,3,-5],[8,-4,-5,6],[-2,3,-7,-1],[-6,-8,-2,-7],[-4,-3,2,2],[2,-10,5,-10],[6,8,-6,2],[1,-3,4,-2],[-8,7,-4,1],[-5,2,-8,-6],[10,8,2,8],[-9,6,4,2],[-4,-1,8,-4],[-4,4,3,-6],[3,-8,3,-8],[-8,8,2,-5],[10,5,-9,-2],[7,5,-3,2],[-5,1,-8,-2],[3,2,1,4],[-3,-9,9,-5],[7,-6,-9,6],[-1,-3,8,-9],[5,-6,7,8],[-10,2,10,4],[7,10,10,-1],[-5,-2,-10,-3],[10,-3,-1,9],[-10,9,-10,9],[-4,-5,-5,5],[-3,-2,-6,7],[-4,7,1,-7],[8,-5,8,8],[-3,6,9,9],[-8,4,5,4],[-2,-5,8,8],[-7,-4,6,-8],[-5,8,-8,6],[7,-2,3,-4],[-6,10,10,-9],[8,5,-7,5],[-9,-8,10,-5],[-5,-1,-4,3],[-3,-3,10,3],[9,-4,-3,10],[9,-1,5,-8],[-4,1,4,-7],[9,-4,-3,-9],[-5,1,-9,9],[9,1,-7,-4],[-7,-8,-9,2],[6,6,-2,-4],[-5,4,3,6],[-3,-8,3,1],[7,5,-4,-5],[-4,2,6,-3],[-10,-7,-8,7],[-9,4,-8,-5],[6,-2,-8,1],[-10,6,-8,6],[-5,10,-9,7],[-3,1,-7,8],[-6,-4,-9,-6],[9,-4,-2,6],[7,-1,5,4],[2,-9,10,2],[8,-2,-2,-8],[4,-9,-4,4],[-1,8,4,3],[-5,-4,-10,5],[-4,-8,9,9],[-8,8,3,3],[-8,9,-1,9],[-5,-5,9,4],[8,2,-8,9],[-9,-5,-10,6],[9,1,6,-10],[-2,5,-4,7],[-2,7,9,-3],[-4,1,-9,5],[10,10,5,8],[-2,1,3,7],[-8,-5,-4,-5],[9,4,1,-7],[-5,-9,-6,10],[-2,-5,-2,2],[1,-6,8,-3],[5,8,-9,9],[2,4,6,8],[-8,7,-9,9],[8,7,5,4],[9,8,-7,-2],[4,8,4,8],[-1,10,-3,2],[-4,-9,8,3],[-5,7,-5,-10],[-5,-8,4,-10],[2,7,-1,-9],[9,-6,-1,-6],[9,8,-10,-4],[7,-5,10,8],[-5,9,5,1],[-6,-10,-7,3],[10,1,-2,-7],[6,9,-7,-10],[-1,10,-9,-9],[9,3,-6,3],[10,3,8,-8],[-4,-4,4,-5],[5,1,6,8],[-9,-5,-7,-8],[4,-8,3,-1],[-5,-10,-9,5],[10,-9,-8,-6],[-7,-2,9,3],[3,-8,-1,5],[-3,6,10,7],[1,-8,2,8],[3,8,-1,-7],[-4,1,3,-1],[3,-8,1,4],[-1,3,-4,-5],[-10,-1,3,5],[7,3,6,-8],[-1,1,-2,-4],[-7,8,-7,-10],[-3,-9,-3,4],[-2,9,8,4],[-4,3,-4,-10],[-5,4,-1,-10],[9,3,-6,1],[-3,-4,10,2],[7,-1,-2,1],[9,-1,2,-7],[3,-3,6,-6],[6,9,10,-9],[7,-5,1,8],[3,-2,-3,4],[-8,4,10,-2],[10,2,3,6],[-1,8,-8,4],[6,-6,7,-6],[8,-1,-9,-7],[-4,-8,10,4],[-4,-1,-1,-4],[3,7,-10,4],[-2,-8,-8,2],[2,7,-6,1],[-5,4,9,4],[-8,1,3,-7],[2,10,8,2],[-3,-4,-1,-9],[-9,-4,-1,-2],[9,-10,-1,-1],[-2,-5,-2,4],[5,4,-3,4],[-8,-4,-7,1],[-2,-10,9,7],[4,-4,8,-2],[6,-9,-3,-4],[-1,1,5,-4],[4,-1,9,4],[2,8,8,3],[9,6,6,2],[-6,-7,-6,9],[7,3,-10,7],[-7,-1,8,10],[9,9,5,5],[6,-2,5,2],[-1,-9,-4,-2],[3,5,-9,-9],[2,-6,-9,6],[-4,-6,2,-2],[5,-2,8,-9],[7,-4,-10,7],[-1,6,-5,-3],[-3,-2,1,7],[-5,-6,-5,6],[8,10,-3,9],[-1,3,-7,9],[-7,6,4,5],[-2,-4,5,-9],[-10,-2,-8,-10],[-4,-7,1,-5],[-6,8,4,-9],[4,5,3,-2],[-5,-9,-5,-3],[2,-2,-7,-3],[7,3,5,-10],[-7,-8,-1,7],[-7,10,-5,-1],[-3,4,-1,3],[6,-1,-9,-10],[8,-9,8,-4],[2,7,4,-8],[10,-9,9,-8],[9,8,2,6],[-5,8,1,-8],[-5,2,-2,8],[-4,-2,-10,-8],[2,7,-3,4],[6,-1,4,-1],[4,-10,-8,10],[-7,3,-3,-4],[-6,-8,2,6],[6,8,-7,-10],[-4,9,9,2],[-2,-3,7,-9],[-8,1,-1,-1],[-2,-8,8,4],[-8,-2,4,5],[10,-10,-7,9],[8,-9,-6,-7],[-7,-9,-2,-5],[-8,1,4,6],[6,-10,-7,-10],[8,5,8,-2],[8,2,-6,4],[5,-6,1,-2],[9,10,2,2],[-1,-3,10,6],[1,-10,4,-3],[-7,-9,-2,-5],[-4,9,-9,5],[8,9,-7,6],[4,7,9,-8],[-10,7,9,-4],[-9,8,-2,7],[2,7,-4,9],[8,7,-9,-4],[-3,10,-4,-2],[7,-2,2,-10],[9,6,-8,-3],[-3,4,7,-1],[-10,10,-7,-9],[-4,-5,2,1],[-1,-5,3,7],[-8,8,-10,6],[9,-4,-10,-3],[3,9,3,7],[10,-7,1,9],[-5,-5,-5,5],[-6,-2,-1,9],[7,9,1,-6],[-7,-1,6,-8],[-8,-8,-3,-7],[-1,3,8,-5],[-9,4,10,10],[4,-8,3,5],[-10,-2,-7,9],[-2,1,-4,6],[3,-5,2,2],[7,8,7,-1],[8,7,-4,3],[-1,-7,-1,8],[3,-8,-9,2],[-2,7,-4,8],[2,7,-4,-4],[-5,7,6,-1],[-3,5,-9,9],[7,-3,-4,5],[6,4,2,-4],[2,2,-1,8],[-10,-5,8,-2],[-1,8,-8,3],[-4,-6,8,-3],[3,8,-6,5],[9,-7,-5,-4],[8,2,-6,1],[-6,6,7,6],[-3,-4,-1,7],[1,9,-4,2],[4,7,-1,-1],[5,2,-7,4],[3,10,-8,-5],[10,-5,-6,6],[1,1,-4,-10],[8,-3,-10,-6],[6,8,3,-3],[7,9,2,-3],[-1,-6,5,-3],[10,1,-2,5],[-10,-10,-6,8],[-10,5,2,-7],[-2,-7,-3,-3],[4,-2,-8,-4],[10,3,-8,9],[10,2,-4,7],[5,5,4,-8],[-2,7,-9,-10],[9,-7,8,5],[-2,10,-7,1],[2,-10,4,7],[10,5,8,-2],[-3,-2,-5,-9],[-5,10,-7,-5],[-7,-5,5,-6],[-7,6,-10,-10],[7,4,-2,-8],[3,10,1,8],[2,-8,7,-2],[6,-10,8,9],[-4,9,7,3],[-9,1,10,-9],[-5,1,-2,-6],[3,-5,6,10],[9,5,9,8],[-1,-8,-10,-7],[-4,9,-1,4],[-3,-7,-3,10],[-6,-9,-3,3],[-6,8,5,-5],[2,-5,-10,-7],[8,-3,-2,-2],[-8,-3,8,6],[6,1,7,-2],[-9,2,-6,4],[6,6,2,6],[10,2,7,3],[-10,-7,-10,6],[8,1,-10,9],[-4,-3,2,6],[-1,10,-4,1],[9,3,-7,-1]], dtype = "uint32")#candidate|1843|(352, 4)|const|uint32
call_1841 = relay.TupleGetItem(func_544_call(relay.reshape(const_1842.astype('uint32'), []), relay.reshape(const_1843.astype('uint32'), [16, 11, 8]), ), 2)
call_1844 = relay.TupleGetItem(func_548_call(relay.reshape(const_1842.astype('uint32'), []), relay.reshape(const_1843.astype('uint32'), [16, 11, 8]), ), 2)
func_1253_call = mod.get_global_var('func_1253')
func_1256_call = mutated_mod.get_global_var('func_1256')
call_1845 = relay.TupleGetItem(func_1253_call(relay.reshape(call_1819.astype('float64'), [3, 4, 3]), relay.reshape(var_1820.astype('int16'), [480,]), ), 5)
call_1846 = relay.TupleGetItem(func_1256_call(relay.reshape(call_1819.astype('float64'), [3, 4, 3]), relay.reshape(var_1820.astype('int16'), [480,]), ), 5)
output = relay.Tuple([call_1806,call_1819,var_1820,call_1833,call_1841,const_1842,const_1843,call_1845,])
output2 = relay.Tuple([call_1807,call_1821,var_1820,call_1834,call_1844,const_1842,const_1843,call_1846,])
func_1847 = relay.Function([var_1820,], output)
mod['func_1847'] = func_1847
mod = relay.transform.InferType()(mod)
mutated_mod['func_1847'] = func_1847
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1848 = relay.var("var_1848", dtype = "int16", shape = (480,))#candidate|1848|(480,)|var|int16
func_1847_call = mutated_mod.get_global_var('func_1847')
call_1849 = func_1847_call(var_1848)
output = call_1849
func_1850 = relay.Function([var_1848], output)
mutated_mod['func_1850'] = func_1850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_1878 = relay.TupleGetItem(func_1561_call(), 2)
call_1879 = relay.TupleGetItem(func_1562_call(), 2)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_1880 = relay.TupleGetItem(func_904_call(), 0)
call_1881 = relay.TupleGetItem(func_906_call(), 0)
output = relay.Tuple([call_1878,call_1880,])
output2 = relay.Tuple([call_1879,call_1881,])
func_1898 = relay.Function([], output)
mod['func_1898'] = func_1898
mod = relay.transform.InferType()(mod)
output = func_1898()
func_1899 = relay.Function([], output)
mutated_mod['func_1899'] = func_1899
mutated_mod = relay.transform.InferType()(mutated_mod)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_1910 = relay.TupleGetItem(func_893_call(), 0)
call_1911 = relay.TupleGetItem(func_894_call(), 0)
uop_1912 = relay.sigmoid(call_1910.astype('float64')) # shape=(3, 4, 3)
uop_1914 = relay.sigmoid(call_1911.astype('float64')) # shape=(3, 4, 3)
func_1281_call = mod.get_global_var('func_1281')
func_1285_call = mutated_mod.get_global_var('func_1285')
const_1918 = relay.const([-3.009483,-7.879519,2.928797,-0.637320,9.792831,6.942686,-6.273844,0.807680,-5.347698,-0.397369,7.346987,7.238776,-2.136390,-8.123455,-4.874515,3.525329,-0.341704,-5.362676,1.323874,-1.245450,-7.586741,-8.432211,-6.537541,7.269698,-9.381299,-7.602461,-8.200460,6.966446,-2.819294,-5.600986,4.150790,9.994947,-9.443737,8.761370,-0.910798,-1.537675,-2.545135,-2.699991,-9.882931,5.486335,9.414278,9.691067,9.915017,-5.914735,-2.252085,4.151228,-5.118768,9.137575,-4.465055,6.783240,8.490293,3.557142,-8.184608,-0.898459,-9.490025,2.089804,-2.595975,1.526000,6.636822,4.810558,-6.767767,9.168757,0.399786,6.863743,-3.547435,7.780657,4.630163,0.237349,-6.629100,-8.394916,0.052606,-5.554617,-2.801554,1.775327,9.633901,0.188346,6.899508,-8.746039,-2.044043,-6.666700,-4.435106,-1.311785,8.777874,-8.461734,1.960214,-4.954858,-0.090250,-8.622208,-7.773117,0.442020,-8.877336,2.170076,3.926038,9.837417,-5.785029,-5.863781,8.852786,-2.754671,-3.763150,-6.218421,1.355536,-3.472217,4.595517,6.896836,1.160808,5.224018,9.925953,2.343680,-7.322699,-3.256293,2.274640,-4.649490,5.052672,3.359086,3.364474,-8.237507,-2.540098,-4.256663,7.991854,5.913914,-8.475040,6.631838,1.239618,5.953038,5.184048,-7.128367,-8.002887,0.644886,5.724176,-9.779611,-5.921471,-7.704049,9.830364,-7.148563,-6.970981,9.531415,-1.448021,-7.130473,-6.157319,3.151145,-1.625440,-7.538588,-8.688019,-0.803315,-5.744435,-8.846949,3.069987,8.030112,-5.604244,-4.354836,1.992579,3.445531,-3.321704,0.004948,3.767255,-0.865239,5.480158,9.121309,-4.882007,4.415660,-1.577840,7.708888,-9.385331,-8.398703,-1.195167,0.870192,4.331364,1.697434,4.253515,-8.746143,7.691630,-2.913756,5.513983,0.336035,4.164182,-9.406334,-4.757650,-3.258980,-3.954376,2.027381,5.256283,-2.265407,-6.255076,-0.191343,-0.191400,-2.473133,7.533848,-4.273064,-3.681534,-6.271168,5.544414,1.129114,-2.790050,-3.642774,9.429491,7.635488,3.049487,4.137683,2.170497,5.746692,-1.908472,2.240304,-8.548520,-6.717269,1.167399,-2.288684,4.584920,4.348834,4.129470,-6.420808,2.051390,8.128855,6.986813,-5.232142,-7.767409,-7.833730,-0.529375,-1.120784,-1.672896,8.247383,2.455948,-2.304084,-0.578976,-6.772049,2.747800,-0.810815,-4.805635,5.606039,-8.780298,-5.586304,4.524797,0.492874,1.274316,-8.403341,-3.798120,5.181658,-2.662540,-8.945043,5.414167,-2.953065,6.157652,-2.158488,8.072116,7.280628,1.335468,-4.872376,-6.861310,-1.416393,-6.311131,4.636991,1.611343,-9.418278,-5.331645,-9.168353,-1.646990,2.152220,5.912817,2.226040,3.807422,-3.604755,5.312783,-4.970537,-5.913862,6.487489,4.988864,9.715972,8.816131,-0.202506,-8.424615,-7.490940,-3.978497,-9.570390,4.824760,-3.094461,-9.094899,1.689713,1.389487,7.160550,3.730034,-1.858041,-2.483582,8.859745,-6.315434,8.946085,-2.304523,7.692209,6.034146,-8.498637,9.457123,-7.243245,1.764737,9.208978,0.981835,-8.186515,7.773595,7.465781,-7.990051,-0.812362,2.754936,2.415103,2.983519,-6.929752,-0.712097,9.243180,1.008778,6.681725,9.293499,3.493297,1.102208,0.351153,0.487012,-2.113363,6.971690,-8.015523,1.235640,-7.860826,-2.931215,2.348252,0.296515,-1.785533,-7.310503,1.259745,0.659248,-4.147374,-6.505252,5.410829,6.907910,6.857007,-7.036273,2.096395,7.967105,-4.199171,-0.283900,-0.181001,-2.385434,-5.841737,-8.242493,8.052534,-6.140076,5.540200,3.379139,-1.054965,-1.725947,-9.982115,1.806045,-8.028326,3.683499,-4.485565,4.257161,-7.745192,-8.057272,-4.292200,-4.595190,-1.076453,-6.697880,-1.582096,-9.461701,-9.796424,-3.970765,-4.984513,-4.214515,5.967443,3.000163,5.405044,-9.827216,2.099391,-4.965684,-1.106897,0.990024,9.387081,-2.743352,9.033758,7.173064,3.082829,-9.305116,0.525574,1.162969,1.483911,1.011746,4.082147,-7.532609,-8.116567,-3.377422,0.030900,0.603424,0.566947,-3.845852,-3.388747,-2.756811,-6.693437,6.030530,1.589289,-3.969176,-9.069319,4.945419,4.927815,-7.482288,-3.214165,-8.110292,-1.859241,6.595833,5.458184,-3.551995,9.822339,-2.239125,-0.222730,2.229246,-4.311643,-0.935588,6.742472,-9.739330,9.642534,-8.074966,1.031957,3.561959,-7.007248,-3.754017,7.148168,-0.562115,5.148336,-8.779881,-4.840163,-2.102799,4.008692,1.628291,-2.314049,4.831668,-3.075711,-6.960859,9.225565,8.356061,-3.461436,5.083346,1.039355,-5.861998,-1.058081,-2.048117,-6.307816,1.632844,8.798549,2.214687,-9.245404,5.596424,-3.531910,9.360823,5.731151,-4.591296,-0.655157,6.715765,5.756768,-7.382952,-2.324864,-3.176929,6.369286,-1.416252,2.172847,8.191633,9.223874,-2.354534,-8.997729,4.942032,8.980719,8.742669,0.925318,4.449788,-5.967011,7.859243,-0.278605,5.805760,0.274048,-0.321797,2.457054,2.516038,-7.704532,0.540829,6.706099,-5.691662,-9.928149,-3.778581,2.357603,-5.263963,2.420465,-5.040563,3.595278,-5.194451,-9.966621,5.038473,-3.141671,-4.977410,0.481015,7.589129,-3.378845,8.348092,3.498511,-0.713600,5.648138,-8.021945,-9.292641,-9.297318,-8.272226,8.547327,8.399185,3.336013,5.865779,-2.869328,7.850091,5.014100,1.528094,-1.868517,-7.576886,7.791339,3.434493,-7.570076,0.619307,2.639406,0.120190,-6.724226,-8.457591,-3.328645,2.638935,-8.333490,-2.525124,-0.682317,-5.316761,-8.558141,0.737696,-1.093705,2.099766,5.809890,6.408693,3.894935,9.908443,1.871405,1.646773,6.017904,-7.375499,9.066141,9.491229,-9.788218,-6.917013,-0.317114,5.959345,-7.141908,2.974168,9.833957,-7.440965,-3.863880,-3.673183,9.860015,6.547225,-0.253163,-6.133006,4.127076,1.233212,5.738601,-6.738388,6.419447,-2.224863,6.123801,8.637683,-5.510356,0.552755,3.537282,-5.593890,9.664735,3.764717,5.953130], dtype = "float32")#candidate|1918|(567,)|const|float32
call_1917 = func_1281_call(relay.reshape(const_1918.astype('float32'), [7, 9, 9]), relay.reshape(const_1918.astype('float32'), [7, 9, 9]), )
call_1919 = func_1281_call(relay.reshape(const_1918.astype('float32'), [7, 9, 9]), relay.reshape(const_1918.astype('float32'), [7, 9, 9]), )
output = relay.Tuple([uop_1912,call_1917,const_1918,])
output2 = relay.Tuple([uop_1914,call_1919,const_1918,])
func_1931 = relay.Function([], output)
mod['func_1931'] = func_1931
mod = relay.transform.InferType()(mod)
output = func_1931()
func_1932 = relay.Function([], output)
mutated_mod['func_1932'] = func_1932
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1947 = relay.const([[[3.772802,-8.126663,4.224297,3.927234,6.731046],[7.735053,-4.666736,-1.003622,0.014474,-8.819270],[-3.154309,5.698188,2.785619,-9.248975,1.042466],[3.890669,0.627991,-9.867199,5.991465,-5.664513],[-0.297244,-1.265878,-5.671081,-4.503658,8.019506],[9.269793,5.150400,3.806521,5.122456,0.963476],[1.620842,5.019535,-2.596201,8.866694,-1.542781],[-2.395548,5.857677,1.411103,4.746842,3.207884],[0.153790,-1.153016,2.273040,4.882359,3.818575],[-8.306217,3.654075,3.862757,9.705394,3.140708],[-9.512725,8.383927,-8.147252,9.615173,-7.845331],[-7.314555,8.474928,-9.818996,-4.606652,4.429892],[-2.564530,-9.240536,-8.190917,-1.257977,-2.209378],[9.389038,2.325150,-8.000832,2.646939,-2.151710],[-8.859442,2.467310,0.409478,-2.023653,7.991814]]], dtype = "float32")#candidate|1947|(1, 15, 5)|const|float32
uop_1948 = relay.asin(const_1947.astype('float32')) # shape=(1, 15, 5)
output = uop_1948
output2 = uop_1948
func_1950 = relay.Function([], output)
mod['func_1950'] = func_1950
mod = relay.transform.InferType()(mod)
output = func_1950()
func_1951 = relay.Function([], output)
mutated_mod['func_1951'] = func_1951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_1981 = func_1779_call()
call_1982 = func_1779_call()
func_1898_call = mod.get_global_var('func_1898')
func_1899_call = mutated_mod.get_global_var('func_1899')
call_1992 = relay.TupleGetItem(func_1898_call(), 0)
call_1993 = relay.TupleGetItem(func_1899_call(), 0)
uop_1994 = relay.acos(call_1992.astype('float32')) # shape=(1, 15, 14)
uop_1996 = relay.acos(call_1993.astype('float32')) # shape=(1, 15, 14)
uop_2003 = relay.log2(uop_1994.astype('float64')) # shape=(1, 15, 14)
uop_2005 = relay.log2(uop_1996.astype('float64')) # shape=(1, 15, 14)
func_1727_call = mod.get_global_var('func_1727')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_2008 = func_1727_call()
call_2009 = func_1727_call()
func_1847_call = mod.get_global_var('func_1847')
func_1850_call = mutated_mod.get_global_var('func_1850')
var_2016 = relay.var("var_2016", dtype = "int16", shape = (4, 120))#candidate|2016|(4, 120)|var|int16
call_2015 = relay.TupleGetItem(func_1847_call(relay.reshape(var_2016.astype('int16'), [480,])), 7)
call_2017 = relay.TupleGetItem(func_1850_call(relay.reshape(var_2016.astype('int16'), [480,])), 7)
bop_2026 = relay.greater(uop_2003.astype('bool'), relay.reshape(call_1992.astype('bool'), relay.shape_of(uop_2003))) # shape=(1, 15, 14)
bop_2029 = relay.greater(uop_2005.astype('bool'), relay.reshape(call_1993.astype('bool'), relay.shape_of(uop_2005))) # shape=(1, 15, 14)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_2033 = func_1779_call()
call_2034 = func_1779_call()
var_2038 = relay.var("var_2038", dtype = "int16", shape = (4, 120))#candidate|2038|(4, 120)|var|int16
bop_2039 = relay.floor_divide(var_2016.astype('float64'), relay.reshape(var_2038.astype('float64'), relay.shape_of(var_2016))) # shape=(4, 120)
output = relay.Tuple([call_1981,call_2008,call_2015,bop_2026,call_2033,bop_2039,])
output2 = relay.Tuple([call_1982,call_2009,call_2017,bop_2029,call_2034,bop_2039,])
func_2043 = relay.Function([var_2016,var_2038,], output)
mod['func_2043'] = func_2043
mod = relay.transform.InferType()(mod)
var_2044 = relay.var("var_2044", dtype = "int16", shape = (4, 120))#candidate|2044|(4, 120)|var|int16
var_2045 = relay.var("var_2045", dtype = "int16", shape = (4, 120))#candidate|2045|(4, 120)|var|int16
output = func_2043(var_2044,var_2045,)
func_2046 = relay.Function([var_2044,var_2045,], output)
mutated_mod['func_2046'] = func_2046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1950_call = mod.get_global_var('func_1950')
func_1951_call = mutated_mod.get_global_var('func_1951')
call_2169 = func_1950_call()
call_2170 = func_1950_call()
output = relay.Tuple([call_2169,])
output2 = relay.Tuple([call_2170,])
func_2171 = relay.Function([], output)
mod['func_2171'] = func_2171
mod = relay.transform.InferType()(mod)
mutated_mod['func_2171'] = func_2171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mutated_mod.get_global_var('func_2171')
call_2172 = func_2171_call()
output = call_2172
func_2173 = relay.Function([], output)
mutated_mod['func_2173'] = func_2173
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_2183 = relay.TupleGetItem(func_1561_call(), 4)
call_2184 = relay.TupleGetItem(func_1562_call(), 4)
output = call_2183
output2 = call_2184
func_2187 = relay.Function([], output)
mod['func_2187'] = func_2187
mod = relay.transform.InferType()(mod)
mutated_mod['func_2187'] = func_2187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mutated_mod.get_global_var('func_2187')
call_2188 = func_2187_call()
output = call_2188
func_2189 = relay.Function([], output)
mutated_mod['func_2189'] = func_2189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_2240 = func_1095_call()
call_2241 = func_1095_call()
func_1383_call = mod.get_global_var('func_1383')
func_1385_call = mutated_mod.get_global_var('func_1385')
call_2256 = relay.TupleGetItem(func_1383_call(relay.reshape(call_2240.astype('float64'), [3, 4, 3])), 0)
call_2257 = relay.TupleGetItem(func_1385_call(relay.reshape(call_2240.astype('float64'), [3, 4, 3])), 0)
output = relay.Tuple([call_2240,call_2256,])
output2 = relay.Tuple([call_2241,call_2257,])
func_2259 = relay.Function([], output)
mod['func_2259'] = func_2259
mod = relay.transform.InferType()(mod)
mutated_mod['func_2259'] = func_2259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mutated_mod.get_global_var('func_2259')
call_2260 = func_2259_call()
output = call_2260
func_2261 = relay.Function([], output)
mutated_mod['func_2261'] = func_2261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_2327 = relay.TupleGetItem(func_1561_call(), 8)
call_2328 = relay.TupleGetItem(func_1562_call(), 8)
uop_2338 = relay.acos(call_2327.astype('float64')) # shape=(1408,)
uop_2340 = relay.acos(call_2328.astype('float64')) # shape=(1408,)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_2349 = relay.TupleGetItem(func_893_call(), 0)
call_2350 = relay.TupleGetItem(func_894_call(), 0)
output = relay.Tuple([uop_2338,call_2349,])
output2 = relay.Tuple([uop_2340,call_2350,])
func_2357 = relay.Function([], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
output = func_2357()
func_2358 = relay.Function([], output)
mutated_mod['func_2358'] = func_2358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_2419 = relay.TupleGetItem(func_904_call(), 0)
call_2420 = relay.TupleGetItem(func_906_call(), 0)
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
var_2431 = relay.var("var_2431", dtype = "int16", shape = (480,))#candidate|2431|(480,)|var|int16
call_2430 = func_180_call(relay.reshape(var_2431.astype('int16'), [15, 4, 8]), relay.reshape(var_2431.astype('int16'), [15, 4, 8]), )
call_2432 = func_180_call(relay.reshape(var_2431.astype('int16'), [15, 4, 8]), relay.reshape(var_2431.astype('int16'), [15, 4, 8]), )
func_460_call = mod.get_global_var('func_460')
func_462_call = mutated_mod.get_global_var('func_462')
var_2442 = relay.var("var_2442", dtype = "float64", shape = (120,))#candidate|2442|(120,)|var|float64
call_2441 = func_460_call(relay.reshape(var_2442.astype('float64'), [1, 10, 12]))
call_2443 = func_460_call(relay.reshape(var_2442.astype('float64'), [1, 10, 12]))
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
call_2452 = func_180_call(relay.reshape(var_2431.astype('int16'), [15, 4, 8]), relay.reshape(call_2430.astype('int16'), [15, 4, 8]), )
call_2453 = func_180_call(relay.reshape(var_2431.astype('int16'), [15, 4, 8]), relay.reshape(call_2430.astype('int16'), [15, 4, 8]), )
bop_2454 = relay.less(call_2452.astype('bool'), relay.reshape(var_2431.astype('bool'), relay.shape_of(call_2452))) # shape=(15, 4, 8)
bop_2457 = relay.less(call_2453.astype('bool'), relay.reshape(var_2431.astype('bool'), relay.shape_of(call_2453))) # shape=(15, 4, 8)
output = relay.Tuple([call_2419,call_2430,call_2441,var_2442,bop_2454,])
output2 = relay.Tuple([call_2420,call_2432,call_2443,var_2442,bop_2457,])
func_2462 = relay.Function([var_2431,var_2442,], output)
mod['func_2462'] = func_2462
mod = relay.transform.InferType()(mod)
mutated_mod['func_2462'] = func_2462
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2462_call = mutated_mod.get_global_var('func_2462')
var_2464 = relay.var("var_2464", dtype = "int16", shape = (480,))#candidate|2464|(480,)|var|int16
var_2465 = relay.var("var_2465", dtype = "float64", shape = (120,))#candidate|2465|(120,)|var|float64
call_2463 = func_2462_call(var_2464,var_2465,)
output = call_2463
func_2466 = relay.Function([var_2464,var_2465,], output)
mutated_mod['func_2466'] = func_2466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1561_call = mod.get_global_var('func_1561')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_2497 = relay.TupleGetItem(func_1561_call(), 3)
call_2498 = relay.TupleGetItem(func_1562_call(), 3)
output = call_2497
output2 = call_2498
func_2508 = relay.Function([], output)
mod['func_2508'] = func_2508
mod = relay.transform.InferType()(mod)
mutated_mod['func_2508'] = func_2508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2508_call = mutated_mod.get_global_var('func_2508')
call_2509 = func_2508_call()
output = call_2509
func_2510 = relay.Function([], output)
mutated_mod['func_2510'] = func_2510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2357_call = mod.get_global_var('func_2357')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_2559 = relay.TupleGetItem(func_2357_call(), 0)
call_2560 = relay.TupleGetItem(func_2358_call(), 0)
func_1281_call = mod.get_global_var('func_1281')
func_1285_call = mutated_mod.get_global_var('func_1285')
var_2569 = relay.var("var_2569", dtype = "float32", shape = (567,))#candidate|2569|(567,)|var|float32
call_2568 = func_1281_call(relay.reshape(var_2569.astype('float32'), [7, 9, 9]), relay.reshape(var_2569.astype('float32'), [7, 9, 9]), )
call_2570 = func_1281_call(relay.reshape(var_2569.astype('float32'), [7, 9, 9]), relay.reshape(var_2569.astype('float32'), [7, 9, 9]), )
func_2043_call = mod.get_global_var('func_2043')
func_2046_call = mutated_mod.get_global_var('func_2046')
const_2582 = relay.const([6,4,-8,-1,-8,7,-10,-10,-5,2,-10,-6,5,6,-9,-4,8,-7,7,-1,3,-4,8,-9,1,-5,-8,-7,-6,10,7,2,-4,-4,-9,5,-5,-6,-2,-6,-6,2,-5,-6,-2,-8,-2,6,9,8,-5,1,-3,4,2,6,2,-4,9,-8,8,-3,6,6,-9,5,-7,-7,3,-6,9,3,-4,-8,6,-7,4,5,-9,-5,-5,-4,7,5,-3,3,4,5,2,10,-1,-2,-7,5,8,-6,-2,-7,4,-1,2,-8,1,-4,-7,8,-3,7,7,-6,3,8,-2,8,-5,-10,-2,-3,2,-3,4,-10,-4,-7,-8,6,4,-1,-6,-2,-6,10,-3,-1,4,5,-7,-7,2,4,8,5,3,-10,-5,-4,9,8,-8,-6,-3,10,-7,-5,-10,1,8,-2,4,-1,-6,-9,-8,-6,6,-9,-4,2,-6,10,-3,-6,9,-3,-9,1,9,10,-6,6,-8,-2,-3,-4,9,-7,-9,5,-10,-10,-5,6,-10,3,-5,-8,1,-7,-4,5,7,10,-2,3,-5,1,-5,-4,-5,8,4,-3,6,1,-3,3,-8,-5,8,-2,-2,-3,-2,-9,-3,-5,3,-4,-9,6,3,1,4,2,5,-7,9,-1,8,-7,7,8,1,-6,10,4,5,5,-3,-5,4,-3,-3,-3,-4,-10,4,8,3,-10,8,-6,-1,-4,9,1,1,-6,10,-5,-4,3,4,-7,-7,-8,1,10,7,6,-5,-1,3,-3,1,-7,-3,-2,2,-4,6,-6,9,1,-1,-4,-6,-5,6,-1,-5,9,9,-7,-3,-1,-4,-8,-2,9,-3,-2,-9,7,-4,-2,9,9,5,8,-6,8,6,4,-2,3,-7,-6,1,-4,4,-4,-7,10,8,1,6,5,-3,10,-2,-3,-8,-5,-2,4,5,10,10,4,-7,1,4,7,-4,3,10,3,4,-6,9,4,-7,-3,-2,6,-6,5,4,-7,9,-2,-7,8,7,10,4,-7,8,-10,1,-2,-3,-6,8,-5,5,-5,-4,-6,7,-6,-9,3,-5,8,9,2,4,8,1,-9,1,-9,-9,8,10,-10,-9,6,6,-1,-1,-6,2,9,7,10,-5,7,-5,-1,-10,-3,6,2,-1,-6,5,9,7,-1,-7,-4,-1,6,7,10,-10,4,-10,7,-9,-6,-6,2,-3,10,7,4,-7,3,-10,9,5,8,-10,-7,-10,3,-7,9,-9,2,5,3,6,3,-10,6,8,1,10,6,2,-6,-4,9,-6,-1], dtype = "int16")#candidate|2582|(480,)|const|int16
call_2581 = relay.TupleGetItem(func_2043_call(relay.reshape(const_2582.astype('int16'), [4, 120]), relay.reshape(const_2582.astype('int16'), [4, 120]), ), 2)
call_2583 = relay.TupleGetItem(func_2046_call(relay.reshape(const_2582.astype('int16'), [4, 120]), relay.reshape(const_2582.astype('int16'), [4, 120]), ), 2)
output = relay.Tuple([call_2559,call_2568,var_2569,call_2581,const_2582,])
output2 = relay.Tuple([call_2560,call_2570,var_2569,call_2583,const_2582,])
func_2584 = relay.Function([var_2569,], output)
mod['func_2584'] = func_2584
mod = relay.transform.InferType()(mod)
var_2585 = relay.var("var_2585", dtype = "float32", shape = (567,))#candidate|2585|(567,)|var|float32
output = func_2584(var_2585)
func_2586 = relay.Function([var_2585], output)
mutated_mod['func_2586'] = func_2586
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1727_call = mod.get_global_var('func_1727')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_2605 = func_1727_call()
call_2606 = func_1727_call()
output = relay.Tuple([call_2605,])
output2 = relay.Tuple([call_2606,])
func_2622 = relay.Function([], output)
mod['func_2622'] = func_2622
mod = relay.transform.InferType()(mod)
output = func_2622()
func_2623 = relay.Function([], output)
mutated_mod['func_2623'] = func_2623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mod.get_global_var('func_2187')
func_2189_call = mutated_mod.get_global_var('func_2189')
call_2648 = func_2187_call()
call_2649 = func_2187_call()
output = call_2648
output2 = call_2649
func_2654 = relay.Function([], output)
mod['func_2654'] = func_2654
mod = relay.transform.InferType()(mod)
mutated_mod['func_2654'] = func_2654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2654_call = mutated_mod.get_global_var('func_2654')
call_2655 = func_2654_call()
output = call_2655
func_2656 = relay.Function([], output)
mutated_mod['func_2656'] = func_2656
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1046_call = mutated_mod.get_global_var('func_1046')
call_2684 = relay.TupleGetItem(func_1044_call(), 1)
call_2685 = relay.TupleGetItem(func_1046_call(), 1)
var_2686 = relay.var("var_2686", dtype = "float64", shape = (3, 4, 3))#candidate|2686|(3, 4, 3)|var|float64
bop_2687 = relay.bitwise_xor(call_2684.astype('int64'), relay.reshape(var_2686.astype('int64'), relay.shape_of(call_2684))) # shape=(3, 4, 3)
bop_2690 = relay.bitwise_xor(call_2685.astype('int64'), relay.reshape(var_2686.astype('int64'), relay.shape_of(call_2685))) # shape=(3, 4, 3)
output = bop_2687
output2 = bop_2690
func_2708 = relay.Function([var_2686,], output)
mod['func_2708'] = func_2708
mod = relay.transform.InferType()(mod)
mutated_mod['func_2708'] = func_2708
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2709 = relay.var("var_2709", dtype = "float64", shape = (3, 4, 3))#candidate|2709|(3, 4, 3)|var|float64
func_2708_call = mutated_mod.get_global_var('func_2708')
call_2710 = func_2708_call(var_2709)
output = call_2710
func_2711 = relay.Function([var_2709], output)
mutated_mod['func_2711'] = func_2711
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2715 = relay.const([[[-4.287948,-3.675391,-4.898637,2.251795,6.249035,0.625906,2.001898,-7.569522,-2.226586,-9.935453,8.726616],[-5.608901,-2.581459,6.982596,-8.524191,-7.769237,4.465962,-1.858928,-3.180730,5.346974,-1.382642,-4.642136],[9.673253,6.725235,5.861113,1.495703,6.418679,-7.352661,1.675639,5.342442,-7.930284,-0.332437,8.182682]],[[4.792082,-4.389169,0.524521,5.042003,-1.243608,8.720609,-3.991774,4.834490,7.990928,-0.466663,8.355166],[-5.054347,8.316907,-5.546610,-6.754824,-3.615232,4.456881,-0.267202,3.848567,8.384892,-2.024994,8.102342],[0.094371,-3.036992,3.788044,-4.610098,-3.502323,-6.103426,4.678262,3.557051,-8.774319,-6.547606,4.140376]]], dtype = "float64")#candidate|2715|(2, 3, 11)|const|float64
uop_2716 = relay.log(const_2715.astype('float64')) # shape=(2, 3, 11)
func_2043_call = mod.get_global_var('func_2043')
func_2046_call = mutated_mod.get_global_var('func_2046')
const_2739 = relay.const([[3,2,5,9],[-2,-8,4,8],[-1,8,-10,-6],[-6,9,-8,-2],[3,6,-6,9],[-9,-2,1,5],[-10,9,-9,-5],[4,10,7,5],[-6,7,6,-9],[-2,-6,-10,6],[-3,9,2,9],[-8,-9,9,-6],[-5,-6,-8,3],[-5,-3,-1,6],[-6,8,-3,-5],[3,7,-8,-8],[5,-3,10,-2],[-5,3,-4,2],[8,-7,4,-9],[5,-1,-8,-7],[3,-5,-6,-10],[-2,8,4,5],[7,-10,-5,8],[-4,5,7,6],[-10,5,-7,-8],[7,-4,-6,-2],[2,-6,10,9],[4,-7,-3,-3],[5,-10,2,-3],[6,2,8,-8],[6,1,9,-10],[-1,-6,-2,-9],[6,9,-9,-8],[10,10,-4,2],[2,5,-1,-6],[6,9,10,4],[9,-1,6,3],[1,-5,2,6],[1,7,8,4],[-5,1,3,9],[-1,-10,2,-4],[-7,-8,8,-4],[5,1,-3,7],[-8,-3,-6,-2],[-3,-3,-6,-7],[-5,3,-9,2],[-8,-7,-8,9],[7,-8,4,-9],[2,1,-8,-2],[-3,8,-2,6],[-1,-1,1,4],[3,10,-2,6],[2,2,6,-7],[-9,-1,-5,-2],[-9,-5,4,8],[-3,-7,-9,1],[-2,5,6,-7],[5,7,6,-8],[2,-5,5,6],[-4,-5,7,6],[8,7,3,9],[3,-10,5,4],[-1,4,6,6],[-6,-5,-8,4],[2,9,7,-5],[-6,-9,-3,8],[4,2,3,-10],[-10,4,7,5],[9,-7,4,9],[9,2,-3,-7],[-2,8,8,6],[2,9,8,-9],[8,5,9,3],[-2,-9,-5,1],[-7,5,-7,-5],[-1,-10,-8,7],[-8,7,10,3],[-5,6,-9,9],[8,-3,-3,7],[5,-4,-8,-7],[7,2,-6,-9],[9,2,4,6],[-5,8,7,1],[-3,-5,8,-7],[-7,-10,8,-5],[5,-7,-1,1],[-1,-2,-4,-2],[-10,8,-8,2],[-8,10,4,-2],[-3,7,1,-9],[-1,-1,-6,2],[10,5,-6,5],[1,-9,1,3],[-10,9,2,-2],[-9,-6,5,-2],[-9,-5,3,-1],[7,9,-9,3],[3,-1,-2,-8],[5,5,-3,7],[3,6,-3,-10],[7,8,2,-7],[7,-9,-8,-9],[10,-5,10,-4],[-3,7,-9,6],[-6,2,-8,-2],[7,-4,-10,-8],[-7,-3,4,-8],[-10,-2,-3,5],[-3,-9,7,7],[-5,-9,-4,-5],[-1,-7,-8,1],[-1,-8,-1,6],[-1,-6,6,-10],[-6,6,-7,10],[9,-2,-2,4],[-8,-10,5,-3],[-10,-3,-4,-9],[-6,-8,-6,-1],[-6,2,8,1],[-8,2,-6,-10]], dtype = "int16")#candidate|2739|(120, 4)|const|int16
call_2738 = relay.TupleGetItem(func_2043_call(relay.reshape(const_2739.astype('int16'), [4, 120]), relay.reshape(const_2739.astype('int16'), [4, 120]), ), 1)
call_2740 = relay.TupleGetItem(func_2046_call(relay.reshape(const_2739.astype('int16'), [4, 120]), relay.reshape(const_2739.astype('int16'), [4, 120]), ), 1)
output = relay.Tuple([uop_2716,call_2738,const_2739,])
output2 = relay.Tuple([uop_2716,call_2740,const_2739,])
func_2743 = relay.Function([], output)
mod['func_2743'] = func_2743
mod = relay.transform.InferType()(mod)
mutated_mod['func_2743'] = func_2743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2743_call = mutated_mod.get_global_var('func_2743')
call_2744 = func_2743_call()
output = call_2744
func_2745 = relay.Function([], output)
mutated_mod['func_2745'] = func_2745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_2793 = func_886_call()
call_2794 = func_886_call()
func_2357_call = mod.get_global_var('func_2357')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_2797 = relay.TupleGetItem(func_2357_call(), 0)
call_2798 = relay.TupleGetItem(func_2358_call(), 0)
const_2799 = relay.const([[[-3.738576,-4.832597,7.412463],[6.525211,-8.650936,-3.320070],[-5.927410,9.998243,-6.345103],[-0.847185,5.072852,9.648351]],[[4.365652,8.181591,7.668010],[-5.214718,3.501433,7.861340],[-8.456637,2.248676,5.645361],[-1.456469,-6.246615,3.319011]],[[-4.387018,-3.803976,9.920640],[6.942698,6.164398,0.269476],[1.957487,-5.449342,-5.579451],[3.183088,9.775769,9.013556]]], dtype = "float64")#candidate|2799|(3, 4, 3)|const|float64
bop_2800 = relay.minimum(call_2793.astype('uint32'), relay.reshape(const_2799.astype('uint32'), relay.shape_of(call_2793))) # shape=(3, 4, 3)
bop_2803 = relay.minimum(call_2794.astype('uint32'), relay.reshape(const_2799.astype('uint32'), relay.shape_of(call_2794))) # shape=(3, 4, 3)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_2820 = func_886_call()
call_2821 = func_886_call()
output = relay.Tuple([call_2797,bop_2800,call_2820,])
output2 = relay.Tuple([call_2798,bop_2803,call_2821,])
func_2824 = relay.Function([], output)
mod['func_2824'] = func_2824
mod = relay.transform.InferType()(mod)
mutated_mod['func_2824'] = func_2824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mutated_mod.get_global_var('func_2824')
call_2825 = func_2824_call()
output = call_2825
func_2826 = relay.Function([], output)
mutated_mod['func_2826'] = func_2826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1046_call = mutated_mod.get_global_var('func_1046')
call_2858 = relay.TupleGetItem(func_1044_call(), 0)
call_2859 = relay.TupleGetItem(func_1046_call(), 0)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_2861 = func_1095_call()
call_2862 = func_1095_call()
output = relay.Tuple([call_2858,call_2861,])
output2 = relay.Tuple([call_2859,call_2862,])
func_2867 = relay.Function([], output)
mod['func_2867'] = func_2867
mod = relay.transform.InferType()(mod)
mutated_mod['func_2867'] = func_2867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2867_call = mutated_mod.get_global_var('func_2867')
call_2868 = func_2867_call()
output = call_2868
func_2869 = relay.Function([], output)
mutated_mod['func_2869'] = func_2869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mod.get_global_var('func_2187')
func_2189_call = mutated_mod.get_global_var('func_2189')
call_2905 = func_2187_call()
call_2906 = func_2187_call()
func_1847_call = mod.get_global_var('func_1847')
func_1850_call = mutated_mod.get_global_var('func_1850')
const_2921 = relay.const([3,-3,6,4,10,5,-5,4,3,-4,10,9,-4,-6,8,-6,-5,5,-2,-7,-10,-4,5,4,6,7,7,3,1,-10,9,9,-6,-5,-3,1,-5,8,-3,-2,-2,6,-4,-3,-8,-5,-3,-3,9,7,2,-5,5,9,-8,8,9,-1,4,-2,-9,1,1,10,2,4,-7,1,4,1,-2,-2,-2,-7,-9,1,4,-1,-6,7,-8,3,9,9,-5,-5,-7,1,-2,-6,-7,-8,-8,8,-9,3,-5,5,10,7,-4,6,3,-1,-6,-3,-5,-4,1,-1,6,-8,-10,-6,6,-10,8,-2,-3,-6,-1,4,2,-2,-1,-3,-7,-9,-5,9,-10,6,5,1,-2,-9,-7,-10,2,-4,-5,3,2,-8,6,-10,6,-6,-3,-9,3,-9,-2,9,-3,10,-2,9,-4,10,-6,-8,-8,1,1,-8,9,-5,6,-8,7,-8,-8,2,6,2,4,-2,2,4,7,-8,-7,9,6,-4,-3,5,-9,-3,-9,-7,-5,-5,-6,2,9,10,-2,-3,8,5,-10,-5,7,8,-3,9,5,6,-3,5,-8,-1,-5,3,2,5,8,4,9,3,6,1,8,-5,6,6,-6,-4,-1,-4,-5,-6,-10,10,4,-1,-9,-4,-10,9,-10,9,2,-6,-10,-6,1,10,4,-1,7,-1,-6,3,-5,-1,-7,-8,4,2,4,1,-1,7,4,4,-9,8,-1,1,-3,-8,5,-1,-9,4,-2,9,7,9,-1,3,-9,7,-1,-5,-1,9,8,-6,5,-2,-5,10,-4,-3,3,9,6,3,2,-2,-10,10,10,-7,-6,-2,8,2,1,9,1,8,-3,5,-9,-10,-9,-7,6,6,10,2,-9,2,-2,-6,10,-2,-6,-8,-5,4,-9,-5,-4,9,-10,-4,7,-1,-6,4,2,6,-5,3,-3,6,-5,-8,-3,-2,10,-5,1,-10,4,2,-1,6,-5,6,3,1,-4,-8,6,1,8,-6,4,8,9,-4,10,-6,8,-4,-3,-2,2,5,3,-5,-4,2,7,5,-9,4,-10,6,-2,10,3,-4,3,-4,-7,-5,-2,-8,6,4,-2,-5,-1,-10,-1,-10,-2,1,4,-10,-8,2,6,8,-3,7,1,8,5,4,-10,-2,9,-8,1,-3,-6,9,-7,4,-7,7,-7,9,3,-9,6,-5,-7,7,4,-6,-7,4,2,-5,-3,7,7,1,9,-3,5,9,5,-1,8,-3,2,8,-7,3,5,-7,5,-4,-2,-9,-7,9,4,2], dtype = "int16")#candidate|2921|(480,)|const|int16
call_2920 = relay.TupleGetItem(func_1847_call(relay.reshape(const_2921.astype('int16'), [480,])), 5)
call_2922 = relay.TupleGetItem(func_1850_call(relay.reshape(const_2921.astype('int16'), [480,])), 5)
output = relay.Tuple([call_2905,call_2920,const_2921,])
output2 = relay.Tuple([call_2906,call_2922,const_2921,])
func_2929 = relay.Function([], output)
mod['func_2929'] = func_2929
mod = relay.transform.InferType()(mod)
output = func_2929()
func_2930 = relay.Function([], output)
mutated_mod['func_2930'] = func_2930
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2935 = relay.const([[[2.619999,8.232369,-2.491670,8.477153,7.601396,-6.035387],[8.214673,-1.555864,8.347578,-0.003306,7.439047,4.546046],[9.664509,-4.372919,5.767842,-3.048312,-5.311962,1.835076],[-3.646120,-6.794525,7.061407,6.372358,-5.990459,2.552692],[3.596092,1.050228,-2.646592,6.257559,4.847609,1.033964],[8.590192,1.051645,1.222517,-3.853206,-9.626446,3.334246],[-3.881617,-4.925085,-0.273160,-0.987303,5.565273,-3.542879],[-0.078395,3.896101,-8.244850,-2.695675,4.983723,8.435095],[-6.856555,-2.243205,-7.763538,-0.807521,-9.779328,9.716119]],[[-8.810794,6.317470,-0.495765,2.046868,5.102216,-6.175536],[6.977206,0.316356,4.443167,6.676855,0.368772,-2.488549],[-3.082799,-8.430513,6.265113,7.741280,8.682147,8.434789],[6.658873,-5.541632,9.037334,-9.003896,5.615819,6.042622],[-0.982440,-1.851505,-7.452134,5.777240,9.733036,-7.778112],[6.151705,9.745648,-2.679544,-8.159278,3.468352,-0.058697],[-5.289380,-8.456883,-7.248143,-0.922631,-4.209984,-0.724823],[7.389764,4.827460,9.932431,0.375575,-2.995047,0.941831],[2.398095,-4.719374,-7.017277,2.025966,2.292682,-5.973047]],[[-6.242682,-7.810469,9.645935,0.901304,-8.661691,-8.610912],[-2.251302,-0.746679,-4.029623,4.173125,-1.673856,-0.934821],[-4.310019,8.392326,3.939812,-8.713763,-6.203572,6.843250],[1.046346,-8.982759,8.639080,-1.238343,-8.814954,-5.038956],[-2.450149,-0.122476,1.760347,-2.881704,-5.529537,4.594077],[2.206754,3.575782,-9.051591,-0.620190,-6.722211,1.091379],[7.522858,5.116431,2.056170,-0.046932,-0.382547,-1.492597],[2.861878,8.695559,-6.404976,-1.995696,-3.289925,2.954553],[-8.804396,5.644025,-2.128269,-4.419893,-7.223475,5.785652]],[[-1.518019,7.612231,-4.812550,-4.956248,-9.510638,6.845284],[2.133977,5.783139,-3.360643,-0.440818,-9.380251,7.534594],[9.751519,-6.378322,2.272086,2.202795,6.767198,-6.195094],[-0.477954,2.336808,5.334879,3.748298,-2.464690,-1.186048],[2.975670,0.395130,-9.443019,-5.653850,2.760217,9.125867],[-7.009664,-1.821388,-3.446591,2.338543,1.969899,3.622296],[4.697152,8.804362,6.660716,-5.296104,2.614411,-1.425708],[-0.231443,2.036425,0.758438,2.993067,6.566716,4.186756],[-2.540250,-8.119789,-2.433579,-3.432121,-5.367138,4.367998]],[[-0.739539,-1.085363,-2.648705,9.771463,4.648537,-7.858248],[-8.811734,-0.741081,0.604375,7.493487,-6.475289,1.011986],[1.873418,-4.618613,-5.505700,-4.624109,-7.874691,-4.852010],[1.926608,6.343815,-2.072366,-1.826638,3.209686,-5.188768],[-1.648675,6.691920,7.135607,1.032438,-1.065906,-8.977997],[-6.120735,9.395903,3.009313,7.031472,-6.634105,6.990699],[-1.975492,6.090357,-9.904535,-9.469793,0.279188,8.700507],[-0.505099,5.774909,-7.590142,2.987909,-6.702429,8.860559],[-8.566280,5.756270,-2.684744,1.812463,-1.869669,-3.081496]],[[-5.016983,6.949685,-4.406078,-4.973333,-3.115642,-8.748677],[1.075320,3.547100,-6.201610,3.140522,6.398188,9.956333],[3.246231,-2.480655,6.398361,-4.951231,3.220294,4.992702],[-9.371137,-3.255864,-6.490387,-2.723985,6.657800,9.777592],[-8.479557,-3.571663,9.832270,3.965595,5.578039,-0.508935],[6.045597,-9.868351,5.818014,-1.933702,-6.182685,-4.890827],[6.050500,-5.831774,-9.751447,2.185517,6.595928,-6.170826],[3.303339,6.069060,7.522748,-9.331476,3.195850,3.489541],[-4.027287,-5.421529,-5.284837,1.932078,8.870294,-9.402756]],[[-6.921205,7.108933,-7.469296,-7.299308,7.153273,-7.740586],[-0.202212,0.681845,5.272679,-7.226107,7.012733,-4.823171],[7.900692,9.348136,-8.894526,-4.218364,6.408548,-5.258950],[1.744598,-4.307268,-0.473477,6.146510,5.145960,-0.041054],[0.198682,-2.506844,-4.156181,-6.896858,9.951561,-3.653095],[-9.531868,-2.550483,-3.313215,3.915530,0.696349,5.138042],[-6.189384,-9.213876,4.116079,-2.172063,6.420358,2.545028],[-2.825405,5.941264,-7.785988,4.818958,-7.943633,-4.924111],[-9.579909,-7.325308,2.266658,1.682769,-1.834642,6.999697]],[[6.717128,-6.630490,6.788420,-6.420452,-7.787717,1.074811],[2.256682,7.738208,-8.958683,0.766304,3.186497,-8.998480],[7.396976,-3.890650,-4.719676,1.812120,4.808771,-8.122096],[-8.938366,-5.752997,4.144543,6.354765,-0.533336,-5.835973],[-2.317485,5.002756,-8.244728,2.728659,-8.865895,9.259700],[2.936917,-2.195313,8.673601,8.850243,8.008786,-3.124976],[5.117039,3.533216,-8.741370,-6.276024,5.985694,-5.579531],[-1.957243,5.827602,3.104855,2.909867,-9.955310,4.810866],[-4.767458,4.560794,2.886746,-1.430337,8.020928,-7.017658]],[[-8.949834,-1.764705,0.122098,6.931919,-2.308519,-9.028337],[1.551324,1.098843,5.343502,3.971518,2.040131,1.345545],[-8.377414,-0.103637,9.577270,9.228428,3.684479,-6.023211],[-4.671334,-4.710862,-7.292560,-0.737256,-4.166122,0.887862],[0.074375,-7.582337,4.176551,5.902379,3.734830,6.336717],[-4.457873,-1.571654,6.848995,-7.190997,-3.383678,-4.686022],[3.618872,3.403161,-0.014055,2.104634,7.552671,5.714632],[6.938643,5.123308,-7.711980,-6.394532,9.664316,-3.317659],[6.329990,3.413589,-9.439441,-9.429016,-1.455431,1.949054]],[[1.069748,-8.690860,-9.471844,6.088046,-5.234752,8.586738],[-0.897937,-0.408332,-3.215018,-8.482862,0.972039,-8.922906],[2.888284,-8.630756,-0.533625,4.244358,-1.002738,-8.180042],[7.885362,6.279940,-6.084344,-4.077865,-1.107799,2.224058],[9.658434,-2.899753,9.287620,-7.017458,6.718777,-6.608295],[2.630469,2.951193,-1.156622,-2.364850,-4.813635,3.141034],[-2.131629,0.056527,-0.503044,-1.599444,-2.018850,8.364920],[7.443901,-2.491853,-3.774419,-0.497993,-6.123670,8.503011],[5.173304,-9.312118,3.560027,0.674726,7.535848,-5.795768]],[[2.401601,-5.427988,6.148855,0.547338,5.468374,-4.976771],[-8.962705,9.467299,-4.558247,9.962677,0.944551,1.556666],[-1.155397,-8.991123,4.346008,4.993150,6.038399,-3.160998],[5.410043,7.384483,-0.413984,-2.524886,-0.288996,8.893858],[6.844828,3.290104,0.757058,4.018994,4.001622,7.371568],[8.211444,8.461775,-4.839157,2.963485,7.441796,9.464697],[-8.407392,-0.097540,6.763456,-0.179603,6.286956,5.323119],[-8.532416,-5.565239,1.036972,0.491614,-5.804676,7.607522],[-3.385897,9.501967,-9.956540,9.810837,-2.350614,2.894502]],[[-6.581002,-5.949576,0.562536,-7.328077,1.441599,8.494796],[-6.298965,9.002513,9.044913,-1.568952,8.116372,3.802728],[-5.011712,8.337044,4.499264,-4.636616,-7.568317,0.576451],[0.755218,8.608073,-1.530287,6.781374,1.427572,6.289416],[2.198291,8.812586,9.521767,-1.853629,4.893834,2.611578],[3.032582,-2.885560,-0.719629,9.041217,4.792206,-1.739097],[-5.911346,2.033121,-7.402925,-1.668868,-8.852628,3.876055],[3.335919,6.072660,6.205996,6.724552,-7.930757,-3.001998],[2.613809,-8.357708,-4.390069,-2.293939,-4.008513,7.252564]],[[-3.989545,3.822172,3.078354,9.304777,-5.516424,7.273556],[3.993721,-1.579672,4.206784,-9.775413,0.436916,7.108090],[-7.780391,-5.864997,1.363621,5.702170,9.869417,-8.674313],[4.578197,2.130859,-9.541881,4.538316,4.307224,-3.010743],[-3.042213,1.263402,1.145879,-9.578343,-8.375963,7.509989],[-9.196748,-6.753764,5.377225,-1.364912,-8.913958,-0.999799],[-1.980163,-5.541707,-9.159712,-7.300056,4.551931,-2.522353],[3.037322,-9.039008,1.671576,6.464353,1.119794,7.279749],[2.377880,2.703440,-6.053364,-6.288450,-0.392924,-5.082623]],[[0.776831,2.275766,8.827528,-3.530586,-9.448821,-6.634075],[-4.009076,5.816011,0.941630,-0.972846,-8.236911,-7.400250],[4.955252,-7.360779,4.731804,-7.310627,2.655330,-4.022707],[3.761361,4.023200,9.545597,4.740962,-7.107650,8.548021],[-9.619988,-6.709726,-7.603325,2.540186,7.915828,8.512275],[-8.274282,-5.051392,9.462542,-3.868372,0.738292,7.853908],[-7.095183,-7.543035,4.306460,-8.511737,2.698902,1.478691],[-8.367688,7.818225,-0.218392,-2.588547,3.609950,-6.250022],[7.056433,0.133692,5.990610,-5.090879,-7.370036,-6.104357]],[[-0.471672,4.356210,3.057236,9.826171,6.592875,5.161080],[2.927598,-3.020570,-3.273590,-2.783944,-3.498174,-9.602251],[-4.348569,8.014597,4.549548,-7.656174,-9.436113,9.234504],[-2.418659,5.901886,-7.163422,9.281336,1.292944,-2.047524],[8.022191,6.859409,-5.515115,5.235527,-7.928006,3.655419],[-0.399209,-1.276912,9.384343,-9.380366,-5.123255,0.765697],[-4.265843,6.825208,4.031089,-3.949184,-8.855007,-2.952334],[4.303252,1.392707,-6.259575,-8.071253,-4.493399,8.148713],[-9.677343,-9.183300,-4.647030,5.193049,-7.158521,-5.316186]],[[-3.195904,-8.246075,-3.379018,-1.433353,-6.041113,-8.819215],[-3.146862,3.414846,0.172529,7.630754,-5.589387,-8.889753],[8.210279,-2.562139,-5.480766,5.953523,2.734259,5.910887],[-9.358063,0.258685,8.110682,5.124026,-8.070587,0.803721],[-1.168950,-4.659961,-7.315127,0.932829,-9.619472,7.772656],[-1.545456,-0.843052,4.929879,9.239512,1.775039,-2.294115],[-8.585205,-1.465724,7.299371,-0.067832,-9.404032,-5.358681],[-1.586284,3.571768,2.211909,0.843993,0.661823,6.143091],[-8.339098,9.287277,-5.502496,-6.391939,1.726540,9.820058]]], dtype = "float32")#candidate|2935|(16, 9, 6)|const|float32
uop_2936 = relay.asin(const_2935.astype('float32')) # shape=(16, 9, 6)
func_2708_call = mod.get_global_var('func_2708')
func_2711_call = mutated_mod.get_global_var('func_2711')
const_2939 = relay.const([-2.138348,-6.114416,4.893718,5.855563,-6.462949,-1.754597,1.455118,2.126358,7.303706,-1.100508,0.718161,6.413101,-9.909090,5.590875,-4.198963,-7.319586,4.174342,-8.056454,-5.319203,-3.228722,8.174539,-5.843416,3.485047,3.772535,1.795252,7.389352,-1.040105,-0.516925,6.882220,9.184101,-3.264297,-5.054289,-9.932557,-5.188988,-1.781205,9.531643], dtype = "float64")#candidate|2939|(36,)|const|float64
call_2938 = func_2708_call(relay.reshape(const_2939.astype('float64'), [3, 4, 3]))
call_2940 = func_2708_call(relay.reshape(const_2939.astype('float64'), [3, 4, 3]))
output = relay.Tuple([uop_2936,call_2938,const_2939,])
output2 = relay.Tuple([uop_2936,call_2940,const_2939,])
func_2942 = relay.Function([], output)
mod['func_2942'] = func_2942
mod = relay.transform.InferType()(mod)
output = func_2942()
func_2943 = relay.Function([], output)
mutated_mod['func_2943'] = func_2943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3177 = relay.TupleGetItem(func_2259_call(), 1)
call_3178 = relay.TupleGetItem(func_2261_call(), 1)
output = call_3177
output2 = call_3178
func_3179 = relay.Function([], output)
mod['func_3179'] = func_3179
mod = relay.transform.InferType()(mod)
mutated_mod['func_3179'] = func_3179
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3179_call = mutated_mod.get_global_var('func_3179')
call_3180 = func_3179_call()
output = call_3180
func_3181 = relay.Function([], output)
mutated_mod['func_3181'] = func_3181
mutated_mod = relay.transform.InferType()(mutated_mod)
func_946_call = mod.get_global_var('func_946')
func_947_call = mutated_mod.get_global_var('func_947')
call_3215 = func_946_call()
call_3216 = func_946_call()
func_2867_call = mod.get_global_var('func_2867')
func_2869_call = mutated_mod.get_global_var('func_2869')
call_3220 = relay.TupleGetItem(func_2867_call(), 0)
call_3221 = relay.TupleGetItem(func_2869_call(), 0)
func_1950_call = mod.get_global_var('func_1950')
func_1951_call = mutated_mod.get_global_var('func_1951')
call_3227 = func_1950_call()
call_3228 = func_1950_call()
output = relay.Tuple([call_3215,call_3220,call_3227,])
output2 = relay.Tuple([call_3216,call_3221,call_3228,])
func_3246 = relay.Function([], output)
mod['func_3246'] = func_3246
mod = relay.transform.InferType()(mod)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3246_call = mutated_mod.get_global_var('func_3246')
call_3247 = func_3246_call()
output = call_3247
func_3248 = relay.Function([], output)
mutated_mod['func_3248'] = func_3248
mutated_mod = relay.transform.InferType()(mutated_mod)
func_946_call = mod.get_global_var('func_946')
func_947_call = mutated_mod.get_global_var('func_947')
call_3249 = func_946_call()
call_3250 = func_946_call()
output = relay.Tuple([call_3249,])
output2 = relay.Tuple([call_3250,])
func_3267 = relay.Function([], output)
mod['func_3267'] = func_3267
mod = relay.transform.InferType()(mod)
output = func_3267()
func_3268 = relay.Function([], output)
mutated_mod['func_3268'] = func_3268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1932_call = mutated_mod.get_global_var('func_1932')
call_3300 = relay.TupleGetItem(func_1931_call(), 0)
call_3301 = relay.TupleGetItem(func_1932_call(), 0)
output = call_3300
output2 = call_3301
func_3305 = relay.Function([], output)
mod['func_3305'] = func_3305
mod = relay.transform.InferType()(mod)
output = func_3305()
func_3306 = relay.Function([], output)
mutated_mod['func_3306'] = func_3306
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2743_call = mod.get_global_var('func_2743')
func_2745_call = mutated_mod.get_global_var('func_2745')
call_3310 = relay.TupleGetItem(func_2743_call(), 0)
call_3311 = relay.TupleGetItem(func_2745_call(), 0)
func_2867_call = mod.get_global_var('func_2867')
func_2869_call = mutated_mod.get_global_var('func_2869')
call_3353 = relay.TupleGetItem(func_2867_call(), 1)
call_3354 = relay.TupleGetItem(func_2869_call(), 1)
output = relay.Tuple([call_3310,call_3353,])
output2 = relay.Tuple([call_3311,call_3354,])
func_3355 = relay.Function([], output)
mod['func_3355'] = func_3355
mod = relay.transform.InferType()(mod)
mutated_mod['func_3355'] = func_3355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3355_call = mutated_mod.get_global_var('func_3355')
call_3356 = func_3355_call()
output = call_3356
func_3357 = relay.Function([], output)
mutated_mod['func_3357'] = func_3357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3246_call = mod.get_global_var('func_3246')
func_3248_call = mutated_mod.get_global_var('func_3248')
call_3401 = relay.TupleGetItem(func_3246_call(), 2)
call_3402 = relay.TupleGetItem(func_3248_call(), 2)
func_2929_call = mod.get_global_var('func_2929')
func_2930_call = mutated_mod.get_global_var('func_2930')
call_3411 = relay.TupleGetItem(func_2929_call(), 1)
call_3412 = relay.TupleGetItem(func_2930_call(), 1)
output = relay.Tuple([call_3401,call_3411,])
output2 = relay.Tuple([call_3402,call_3412,])
func_3414 = relay.Function([], output)
mod['func_3414'] = func_3414
mod = relay.transform.InferType()(mod)
output = func_3414()
func_3415 = relay.Function([], output)
mutated_mod['func_3415'] = func_3415
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3414_call = mod.get_global_var('func_3414')
func_3415_call = mutated_mod.get_global_var('func_3415')
call_3444 = relay.TupleGetItem(func_3414_call(), 0)
call_3445 = relay.TupleGetItem(func_3415_call(), 0)
uop_3453 = relay.asinh(call_3444.astype('float32')) # shape=(1, 15, 5)
uop_3455 = relay.asinh(call_3445.astype('float32')) # shape=(1, 15, 5)
bop_3470 = relay.logical_and(call_3444.astype('bool'), relay.reshape(uop_3453.astype('bool'), relay.shape_of(call_3444))) # shape=(1, 15, 5)
bop_3473 = relay.logical_and(call_3445.astype('bool'), relay.reshape(uop_3455.astype('bool'), relay.shape_of(call_3445))) # shape=(1, 15, 5)
func_3179_call = mod.get_global_var('func_3179')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_3481 = func_3179_call()
call_3482 = func_3179_call()
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_3483 = func_1140_call()
call_3484 = func_1140_call()
output = relay.Tuple([bop_3470,call_3481,call_3483,])
output2 = relay.Tuple([bop_3473,call_3482,call_3484,])
func_3488 = relay.Function([], output)
mod['func_3488'] = func_3488
mod = relay.transform.InferType()(mod)
output = func_3488()
func_3489 = relay.Function([], output)
mutated_mod['func_3489'] = func_3489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_3493 = relay.TupleGetItem(func_2171_call(), 0)
call_3494 = relay.TupleGetItem(func_2173_call(), 0)
output = relay.Tuple([call_3493,])
output2 = relay.Tuple([call_3494,])
func_3507 = relay.Function([], output)
mod['func_3507'] = func_3507
mod = relay.transform.InferType()(mod)
output = func_3507()
func_3508 = relay.Function([], output)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3519 = relay.var("var_3519", dtype = "float64", shape = (13, 14, 3))#candidate|3519|(13, 14, 3)|var|float64
uop_3520 = relay.sin(var_3519.astype('float64')) # shape=(13, 14, 3)
var_3523 = relay.var("var_3523", dtype = "float64", shape = (13, 14, 3))#candidate|3523|(13, 14, 3)|var|float64
bop_3524 = relay.multiply(uop_3520.astype('int8'), relay.reshape(var_3523.astype('int8'), relay.shape_of(uop_3520))) # shape=(13, 14, 3)
output = bop_3524
output2 = bop_3524
func_3528 = relay.Function([var_3519,var_3523,], output)
mod['func_3528'] = func_3528
mod = relay.transform.InferType()(mod)
var_3529 = relay.var("var_3529", dtype = "float64", shape = (13, 14, 3))#candidate|3529|(13, 14, 3)|var|float64
var_3530 = relay.var("var_3530", dtype = "float64", shape = (13, 14, 3))#candidate|3530|(13, 14, 3)|var|float64
output = func_3528(var_3529,var_3530,)
func_3531 = relay.Function([var_3529,var_3530,], output)
mutated_mod['func_3531'] = func_3531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_3589 = func_1779_call()
call_3590 = func_1779_call()
func_2043_call = mod.get_global_var('func_2043')
func_2046_call = mutated_mod.get_global_var('func_2046')
var_3617 = relay.var("var_3617", dtype = "int16", shape = (480,))#candidate|3617|(480,)|var|int16
call_3616 = relay.TupleGetItem(func_2043_call(relay.reshape(var_3617.astype('int16'), [4, 120]), relay.reshape(var_3617.astype('int16'), [4, 120]), ), 2)
call_3618 = relay.TupleGetItem(func_2046_call(relay.reshape(var_3617.astype('int16'), [4, 120]), relay.reshape(var_3617.astype('int16'), [4, 120]), ), 2)
output = relay.Tuple([call_3589,call_3616,var_3617,])
output2 = relay.Tuple([call_3590,call_3618,var_3617,])
func_3637 = relay.Function([var_3617,], output)
mod['func_3637'] = func_3637
mod = relay.transform.InferType()(mod)
var_3638 = relay.var("var_3638", dtype = "int16", shape = (480,))#candidate|3638|(480,)|var|int16
output = func_3637(var_3638)
func_3639 = relay.Function([var_3638], output)
mutated_mod['func_3639'] = func_3639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1932_call = mutated_mod.get_global_var('func_1932')
call_3648 = relay.TupleGetItem(func_1931_call(), 2)
call_3649 = relay.TupleGetItem(func_1932_call(), 2)
var_3652 = relay.var("var_3652", dtype = "float32", shape = (567,))#candidate|3652|(567,)|var|float32
bop_3653 = relay.greater(call_3648.astype('bool'), relay.reshape(var_3652.astype('bool'), relay.shape_of(call_3648))) # shape=(567,)
bop_3656 = relay.greater(call_3649.astype('bool'), relay.reshape(var_3652.astype('bool'), relay.shape_of(call_3649))) # shape=(567,)
var_3657 = relay.var("var_3657", dtype = "bool", shape = (567,))#candidate|3657|(567,)|var|bool
bop_3658 = relay.minimum(bop_3653.astype('uint32'), relay.reshape(var_3657.astype('uint32'), relay.shape_of(bop_3653))) # shape=(567,)
bop_3661 = relay.minimum(bop_3656.astype('uint32'), relay.reshape(var_3657.astype('uint32'), relay.shape_of(bop_3656))) # shape=(567,)
bop_3668 = relay.left_shift(call_3648.astype('uint16'), relay.reshape(var_3652.astype('uint16'), relay.shape_of(call_3648))) # shape=(567,)
bop_3671 = relay.left_shift(call_3649.astype('uint16'), relay.reshape(var_3652.astype('uint16'), relay.shape_of(call_3649))) # shape=(567,)
uop_3672 = relay.rsqrt(var_3657.astype('float32')) # shape=(567,)
output = relay.Tuple([bop_3658,bop_3668,uop_3672,])
output2 = relay.Tuple([bop_3661,bop_3671,uop_3672,])
func_3687 = relay.Function([var_3652,var_3657,], output)
mod['func_3687'] = func_3687
mod = relay.transform.InferType()(mod)
var_3688 = relay.var("var_3688", dtype = "float32", shape = (567,))#candidate|3688|(567,)|var|float32
var_3689 = relay.var("var_3689", dtype = "bool", shape = (567,))#candidate|3689|(567,)|var|bool
output = func_3687(var_3688,var_3689,)
func_3690 = relay.Function([var_3688,var_3689,], output)
mutated_mod['func_3690'] = func_3690
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1044_call = mod.get_global_var('func_1044')
func_1046_call = mutated_mod.get_global_var('func_1046')
call_3702 = relay.TupleGetItem(func_1044_call(), 0)
call_3703 = relay.TupleGetItem(func_1046_call(), 0)
func_2043_call = mod.get_global_var('func_2043')
func_2046_call = mutated_mod.get_global_var('func_2046')
const_3722 = relay.const([[-7,-1,5,1,-8,4,2,-9,2,9,-6,6,9,-4,8,-7,6,-4,-1,-8,-5,1,2,2,-7,-1,4,-6,9,-5,3,-2,9,8,10,-1,2,4,-3,9,-9,-2,2,-5,-8,-8,4,10,7,-3,5,3,9,3,-4,-3,-7,-8,-3,-9,-5,3,-6,-3,10,7,-2,-5,8,3,2,-8,1,7,-1,4,-1,5,8,8,4,3,8,6,-6,1,-7,7,5,9,-10,1,-1,-9,-2,7,4,1,10,9,8,-5,9,10,-6,9,3,-7,6,-3,3,-6,4,9,7,-1,10,-8,8,2],[-9,9,-2,-8,2,-1,-5,-2,-6,-4,-10,8,1,-6,5,2,-10,-10,5,1,3,-2,8,-7,4,-7,-8,-4,-10,7,-10,-3,-10,-3,3,4,-7,-2,10,-1,-3,-1,-3,2,-5,1,10,8,-7,6,-4,-3,7,-5,-9,3,5,4,9,3,5,-1,-10,-4,7,-8,-10,-1,-8,-4,-5,10,-1,7,-10,-3,-6,1,-3,-4,5,-3,-3,-2,3,2,4,-7,6,-4,6,-5,-4,-10,-3,7,-6,-5,-7,2,4,9,5,5,-1,10,-8,10,1,-7,4,-2,-8,-9,-5,-4,-4,1,8,1],[-4,-7,-3,-4,-6,-9,-9,-9,10,-10,9,-6,-9,-4,-2,6,-5,-10,-9,3,7,8,-4,1,-6,-1,-6,-10,5,-2,9,4,-1,10,-9,7,-6,-10,-3,4,-3,-4,1,2,6,-2,-1,8,-1,4,-3,7,-6,-8,9,6,-7,9,-4,4,6,-6,-2,-9,-3,4,5,-5,-8,10,9,7,8,-3,-8,6,-3,-1,7,8,4,-7,-3,10,9,9,7,3,-4,10,1,4,-8,-9,-4,6,10,6,10,-7,3,-9,5,-8,8,1,-3,5,9,-6,-2,-2,8,8,-2,-8,-4,-7,-9,-8],[-4,6,3,9,-3,8,1,-8,7,-8,-2,6,-3,4,10,7,-10,-3,2,6,1,3,-3,-1,-8,9,-7,-7,-10,2,-3,-7,-2,6,2,-3,4,-5,6,7,-6,5,3,-4,3,4,5,-8,2,2,4,7,9,4,7,-3,-10,-8,10,-6,8,-8,-3,-1,-8,9,6,1,5,5,9,-8,-6,-1,-8,9,9,8,-6,7,2,8,-9,5,4,-9,-8,3,-3,10,3,7,9,-4,-6,10,6,-6,-5,-2,-1,-4,-9,-10,-1,-2,-10,-6,6,-5,-2,8,3,6,5,10,10,2,1,10]], dtype = "int16")#candidate|3722|(4, 120)|const|int16
call_3721 = relay.TupleGetItem(func_2043_call(relay.reshape(const_3722.astype('int16'), [4, 120]), relay.reshape(const_3722.astype('int16'), [4, 120]), ), 3)
call_3723 = relay.TupleGetItem(func_2046_call(relay.reshape(const_3722.astype('int16'), [4, 120]), relay.reshape(const_3722.astype('int16'), [4, 120]), ), 3)
func_2708_call = mod.get_global_var('func_2708')
func_2711_call = mutated_mod.get_global_var('func_2711')
call_3730 = func_2708_call(relay.reshape(call_3702.astype('float64'), [3, 4, 3]))
call_3731 = func_2708_call(relay.reshape(call_3702.astype('float64'), [3, 4, 3]))
output = relay.Tuple([call_3702,call_3721,const_3722,call_3730,])
output2 = relay.Tuple([call_3703,call_3723,const_3722,call_3731,])
func_3733 = relay.Function([], output)
mod['func_3733'] = func_3733
mod = relay.transform.InferType()(mod)
mutated_mod['func_3733'] = func_3733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3733_call = mutated_mod.get_global_var('func_3733')
call_3734 = func_3733_call()
output = call_3734
func_3735 = relay.Function([], output)
mutated_mod['func_3735'] = func_3735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2824_call = mod.get_global_var('func_2824')
func_2826_call = mutated_mod.get_global_var('func_2826')
call_3744 = relay.TupleGetItem(func_2824_call(), 2)
call_3745 = relay.TupleGetItem(func_2826_call(), 2)
output = call_3744
output2 = call_3745
func_3774 = relay.Function([], output)
mod['func_3774'] = func_3774
mod = relay.transform.InferType()(mod)
mutated_mod['func_3774'] = func_3774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3774_call = mutated_mod.get_global_var('func_3774')
call_3775 = func_3774_call()
output = call_3775
func_3776 = relay.Function([], output)
mutated_mod['func_3776'] = func_3776
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3821 = relay.var("var_3821", dtype = "int16", shape = ())#candidate|3821|()|var|int16
var_3822 = relay.var("var_3822", dtype = "int16", shape = (12, 10, 12))#candidate|3822|(12, 10, 12)|var|int16
bop_3823 = relay.equal(var_3821.astype('bool'), var_3822.astype('bool')) # shape=(12, 10, 12)
output = bop_3823
output2 = bop_3823
func_3826 = relay.Function([var_3821,var_3822,], output)
mod['func_3826'] = func_3826
mod = relay.transform.InferType()(mod)
mutated_mod['func_3826'] = func_3826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3826_call = mutated_mod.get_global_var('func_3826')
var_3828 = relay.var("var_3828", dtype = "int16", shape = ())#candidate|3828|()|var|int16
var_3829 = relay.var("var_3829", dtype = "int16", shape = (12, 10, 12))#candidate|3829|(12, 10, 12)|var|int16
call_3827 = func_3826_call(var_3828,var_3829,)
output = call_3827
func_3830 = relay.Function([var_3828,var_3829,], output)
mutated_mod['func_3830'] = func_3830
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3878 = relay.var("var_3878", dtype = "float32", shape = (1, 8, 2))#candidate|3878|(1, 8, 2)|var|float32
var_3879 = relay.var("var_3879", dtype = "float32", shape = (15, 8, 2))#candidate|3879|(15, 8, 2)|var|float32
bop_3880 = relay.equal(var_3878.astype('bool'), var_3879.astype('bool')) # shape=(15, 8, 2)
func_2508_call = mod.get_global_var('func_2508')
func_2510_call = mutated_mod.get_global_var('func_2510')
call_3885 = func_2508_call()
call_3886 = func_2508_call()
output = relay.Tuple([bop_3880,call_3885,])
output2 = relay.Tuple([bop_3880,call_3886,])
func_3890 = relay.Function([var_3878,var_3879,], output)
mod['func_3890'] = func_3890
mod = relay.transform.InferType()(mod)
var_3891 = relay.var("var_3891", dtype = "float32", shape = (1, 8, 2))#candidate|3891|(1, 8, 2)|var|float32
var_3892 = relay.var("var_3892", dtype = "float32", shape = (15, 8, 2))#candidate|3892|(15, 8, 2)|var|float32
output = func_3890(var_3891,var_3892,)
func_3893 = relay.Function([var_3891,var_3892,], output)
mutated_mod['func_3893'] = func_3893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_3901 = func_1095_call()
call_3902 = func_1095_call()
func_2708_call = mod.get_global_var('func_2708')
func_2711_call = mutated_mod.get_global_var('func_2711')
call_3921 = func_2708_call(relay.reshape(call_3901.astype('float64'), [3, 4, 3]))
call_3922 = func_2708_call(relay.reshape(call_3901.astype('float64'), [3, 4, 3]))
output = relay.Tuple([call_3901,call_3921,])
output2 = relay.Tuple([call_3902,call_3922,])
func_3930 = relay.Function([], output)
mod['func_3930'] = func_3930
mod = relay.transform.InferType()(mod)
output = func_3930()
func_3931 = relay.Function([], output)
mutated_mod['func_3931'] = func_3931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mod.get_global_var('func_2187')
func_2189_call = mutated_mod.get_global_var('func_2189')
call_3932 = func_2187_call()
call_3933 = func_2187_call()
func_1618_call = mod.get_global_var('func_1618')
func_1620_call = mutated_mod.get_global_var('func_1620')
var_3938 = relay.var("var_3938", dtype = "int16", shape = (8, 60))#candidate|3938|(8, 60)|var|int16
call_3937 = relay.TupleGetItem(func_1618_call(relay.reshape(var_3938.astype('int16'), [480,])), 2)
call_3939 = relay.TupleGetItem(func_1620_call(relay.reshape(var_3938.astype('int16'), [480,])), 2)
var_3940 = relay.var("var_3940", dtype = "int16", shape = (8, 60))#candidate|3940|(8, 60)|var|int16
bop_3941 = relay.logical_and(var_3938.astype('bool'), relay.reshape(var_3940.astype('bool'), relay.shape_of(var_3938))) # shape=(8, 60)
func_2654_call = mod.get_global_var('func_2654')
func_2656_call = mutated_mod.get_global_var('func_2656')
call_3944 = func_2654_call()
call_3945 = func_2654_call()
output = relay.Tuple([call_3932,call_3937,bop_3941,call_3944,])
output2 = relay.Tuple([call_3933,call_3939,bop_3941,call_3945,])
func_3947 = relay.Function([var_3938,var_3940,], output)
mod['func_3947'] = func_3947
mod = relay.transform.InferType()(mod)
var_3948 = relay.var("var_3948", dtype = "int16", shape = (8, 60))#candidate|3948|(8, 60)|var|int16
var_3949 = relay.var("var_3949", dtype = "int16", shape = (8, 60))#candidate|3949|(8, 60)|var|int16
output = func_3947(var_3948,var_3949,)
func_3950 = relay.Function([var_3948,var_3949,], output)
mutated_mod['func_3950'] = func_3950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_3966 = relay.TupleGetItem(func_2259_call(), 0)
call_3967 = relay.TupleGetItem(func_2261_call(), 0)
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
const_3975 = relay.const([3.743272,-2.811811,7.316412,7.890064,-2.837064,-8.615903,-5.769629,-2.998655,-8.076539,-5.768851,3.908832,-2.628043,5.751115,-7.242952,2.739863,8.580703,2.734746,-0.688327,1.979953,0.493842], dtype = "float64")#candidate|3975|(20,)|const|float64
call_3974 = relay.TupleGetItem(func_1650_call(relay.reshape(const_3975.astype('float64'), [4, 1, 5])), 0)
call_3976 = relay.TupleGetItem(func_1652_call(relay.reshape(const_3975.astype('float64'), [4, 1, 5])), 0)
func_1281_call = mod.get_global_var('func_1281')
func_1285_call = mutated_mod.get_global_var('func_1285')
const_3980 = relay.const([-1.479920,-7.391280,-2.971330,-5.385436,-2.154811,1.874675,-4.977035,2.432510,-4.534255,8.779971,4.043355,-8.521770,-5.750375,-4.901001,-3.531286,1.112196,-9.347909,-7.347532,1.726528,3.560518,9.807232,9.017170,1.721081,2.997216,-3.020977,-7.526381,-8.635447,2.000178,-1.096907,-6.009257,-5.561372,-6.734821,1.477164,2.788337,2.342542,-3.506672,-0.195832,-1.951409,-0.791400,1.654133,-2.460114,-8.147509,-3.717633,-5.427704,6.526015,5.728573,-8.107970,-0.513152,-4.155463,-3.228675,-1.960965,8.662886,-5.190736,3.298552,6.699689,8.117676,-0.656466,-5.037583,4.308589,6.136120,3.619253,-0.639727,-3.431280,9.510813,4.946444,8.701656,-6.554587,-6.032042,-7.049986,8.970560,-3.165437,-1.277309,-4.198926,1.435753,5.202220,2.479068,1.579540,-8.749280,-1.419162,3.369118,2.923744,-8.736027,8.061710,-2.361375,-4.491965,5.556183,8.608247,2.039990,8.743567,2.854043,1.245447,6.747040,0.368779,1.739048,-9.690236,0.563750,4.839495,0.250064,-4.097259,-5.194156,-1.415528,6.769184,3.577513,8.159851,7.849146,9.452423,7.683135,0.314572,-2.259975,2.527697,7.646329,-1.328593,-6.583837,4.234519,-9.348728,0.529754,-6.750390,-5.274801,2.891054,-8.569133,-6.558525,3.812946,-0.545465,-3.226523,2.644603,3.730382,-7.207211,5.533031,-4.236543,9.343833,2.681582,2.392150,7.643936,8.155252,0.513089,2.764726,-8.309879,-3.167708,-6.773642,6.985516,-9.299573,-7.019597,8.725698,2.104827,1.529152,-2.527922,3.069849,-7.115584,9.360085,5.467722,2.872396,-8.911154,3.984854,-3.341127,-3.601840,-8.190952,6.976784,1.644272,-9.285786,-9.287393,-0.017909,-6.463558,-9.339453,-1.946814,3.360879,-5.852549,8.937058,-6.218543,3.860788,-1.503002,-2.462766,-9.895483,6.061319,-2.669701,-5.762620,4.001105,5.728660,-1.858341,-6.214430,7.986315,-0.730457,-0.546098,2.831752,4.390372,-8.388654,-9.546100,-6.882652,-8.817432,-4.056316,1.594322,0.297744,2.559660,7.225780,-5.613436,9.139764,6.672786,0.316779,3.167959,-9.866154,-2.768203,-3.452906,1.542731,3.796249,-3.049806,0.371336,6.755645,7.180222,4.579692,-4.529509,-2.089856,-7.099119,-2.342570,-2.593175,-1.730719,-5.335127,9.368574,2.313706,8.360225,-9.121447,-1.574053,4.350316,-4.622156,9.527471,7.387985,3.336291,3.502421,1.516231,3.835462,3.016916,-9.398945,-5.708876,-1.670857,6.662977,6.690680,4.758741,0.265013,8.495057,0.124087,9.764608,-3.757538,4.750039,-9.306701,6.003540,-3.280848,3.743304,-6.841456,-9.930357,7.299184,-5.354317,9.305261,5.893083,3.134702,-2.071314,2.933479,2.087951,-4.070714,1.996787,-2.319209,-8.373030,5.383025,1.015634,-7.512420,-6.671117,1.845483,-9.329027,-2.346602,1.502304,-5.699513,5.846982,-2.344155,6.171109,8.030545,5.296277,-5.533548,-6.767458,-0.732487,6.705246,7.072984,-9.072269,4.511425,2.925042,-4.175349,5.721480,-9.739412,-8.410381,5.641813,7.521127,-3.492428,-0.636464,-6.219097,-7.641788,4.994709,9.509328,7.035531,1.033711,-3.523994,7.691341,-1.136525,6.402533,2.020705,6.827435,-1.376315,7.027370,3.762505,9.216211,-4.678069,-6.997972,5.986466,-5.037269,-0.754000,5.520591,-6.437154,3.712307,4.088449,3.289473,4.956697,-7.838110,1.790031,-2.626761,4.420745,-7.218605,-5.286432,5.907760,7.765025,-8.822675,-5.601009,-6.657132,-0.599755,7.095038,7.930376,-5.068462,9.545073,-8.955841,-3.771591,5.872919,-8.726473,8.590887,7.755859,-9.375631,-2.330402,-6.081251,1.700577,6.208081,-9.500272,0.036760,3.001717,-3.986605,-4.978113,2.041209,-7.289481,2.330366,2.789811,2.643968,2.765148,2.522509,-6.809355,-1.518904,-3.163758,-3.124282,-4.198291,-6.717812,1.012183,-7.165261,0.783254,6.432874,0.982196,-0.274000,4.319349,9.474038,-9.005570,2.438254,-1.492030,-1.970572,8.067917,5.352774,-5.329130,-2.835046,5.146875,-2.277151,-5.736601,-5.828071,-3.356517,-8.596675,-4.118513,-2.952841,-3.529329,4.351318,-1.651785,-1.140639,-2.896872,8.833780,0.791292,2.801682,5.098574,-9.151325,8.183844,1.378742,9.149554,9.699157,0.563636,-1.970035,7.292593,-8.385629,0.194402,-3.207195,-5.784424,2.970466,1.400060,-5.572573,-8.412154,-8.378000,2.120910,5.295562,-5.336746,-2.773664,-0.127844,2.199819,1.451499,7.257027,-3.884068,-5.310268,-0.885931,7.671550,-8.825340,-9.468521,-4.371357,-8.978553,-3.736647,-5.192216,9.644323,-1.276667,-7.330831,3.013878,3.321324,-8.741617,-7.047598,-6.970350,-5.144434,-8.155754,-3.234436,4.726999,-6.295107,-0.970940,7.338472,4.076924,-0.473908,8.639712,3.148877,-1.276473,8.388580,2.125478,1.358586,-1.099781,1.047429,2.087758,4.185024,-7.525369,-1.165207,-6.756596,0.240632,-7.519936,4.415071,-1.874403,3.153540,2.078961,-2.819503,-4.526148,5.801360,7.366281,-2.847705,-1.278157,-7.556916,2.771347,8.561008,-6.506253,1.239362,-7.500388,-2.945613,1.954516,5.257804,2.741320,9.003173,-8.749191,-1.846571,8.045057,-8.431803,8.044492,-6.216421,8.846448,-0.245766,3.835158,8.872375,6.915878,-1.051875,8.386752,9.156864,5.393236,-5.124171,3.879816,-6.286101,0.067213,-6.774015,3.196037,0.639426,7.888608,-8.237366,2.432886,-0.417799,-2.831768,-1.058076,1.899973,-7.315281,-2.102934,-6.555537,9.150387,4.258078,2.916088,1.258855,-7.788911,1.312048,6.748707,-6.363920,8.739209,9.766100,-9.926213,6.121410,2.826748,-8.397178,3.518564,-8.850753,0.162861,5.561058,3.718709,4.008162,-7.202340,7.850913,9.573335,-4.014505,6.191604,-4.610717,9.974710,2.077954,6.153756,2.851342,-2.253050,5.850347,1.768047,-0.995882,-2.228493,-7.012993,-6.102386,-6.610418,-8.282454,6.049844,-9.401126,5.301254,7.113370,-4.306293,-2.998547,0.582773,5.152599,4.030064,-2.599622,-4.551224,7.132067,1.829278,-5.799335], dtype = "float32")#candidate|3980|(567,)|const|float32
call_3979 = func_1281_call(relay.reshape(const_3980.astype('float32'), [7, 9, 9]), relay.reshape(const_3980.astype('float32'), [7, 9, 9]), )
call_3981 = func_1281_call(relay.reshape(const_3980.astype('float32'), [7, 9, 9]), relay.reshape(const_3980.astype('float32'), [7, 9, 9]), )
uop_3988 = relay.sqrt(const_3980.astype('float64')) # shape=(567,)
var_3995 = relay.var("var_3995", dtype = "float64", shape = (567,))#candidate|3995|(567,)|var|float64
bop_3996 = relay.bitwise_or(uop_3988.astype('int8'), relay.reshape(var_3995.astype('int8'), relay.shape_of(uop_3988))) # shape=(567,)
const_3999 = relay.const([6,9,-6,-9,-10,6,1,-3,6,-9,2,2,-5,-2,-7,-8,-10,2,5,4,2,-7,1,-8,-1,9,4,-1,4,-5,-8,4,9,-6,9,10,-10,-6,8,-8,-10,2,10,2,-7,-5,-1,-2,4,5,-8,7,-3,-10,7,-9,5,-1,-3,9,2,-6,2,3,8,1,4,-5,-3,7,-3,6,-8,-4,-2,2,6,8,7,-8,-1,10,-1,2,10,-1,-6,10,6,4,7,-1,-5,5,-10,7,-3,7,-4,5,8,4,5,-7,-9,8,-8,-1,7,5,10,-9,10,7,8,-5,-2,-2,6,9,-2,-3,3,3,1,-7,9,6,-5,3,-6,10,9,6,-3,3,9,6,-10,-4,-9,2,1,7,-2,1,-9,6,5,5,7,3,-4,10,10,-4,8,-6,5,-7,4,-3,-9,2,2,-1,-7,-5,-5,-2,-2,3,2,9,3,-2,-5,1,-7,7,-2,8,-5,10,-9,-5,9,-1,9,8,-9,2,-9,-8,-6,6,5,9,7,10,-2,-7,6,1,1,9,4,-3,-4,1,-6,-10,-9,1,-8,3,7,-10,9,10,3,-1,-1,-1,-5,-9,-9,2,-9,5,-3,5,10,4,-7,1,-4,-10,-7,1,3,-3,-8,2,7,5,8,1,-7,7,-7,-5,-3,5,-6,-3,6,-5,2,-2,-7,-8,-6,4,2,-7,-2,-10,-9,-6,-1,8,-7,-2,10,-8,10,5,7,-9,-1,-7,-1,9,-4,-7,-7,4,7,5,-9,-8,10,-5,1,5,-2,-6,-3,-5,1,4,8,-4,-2,-4,-3,-10,-4,-2,-8,-8,3,-5,10,-5,-1,-10,5,-4,4,-1,-10,2,5,8,4,6,-1,-4,-1,1,8,-3,-7,1,4,-8,3,8,-5,5,-4,7,-2,-6,1,-6,-9,1,5,7,6,-6,7,-10,2,-4,-8,2,5,4,-5,5,7,-2,-2,4,6,10,3,8,5,2,4,-3,1,-4,-8,-2,7,-9,-5,-8,4,4,7,-5,-3,-8,-4,-5,10,3,8,-5,1,3,-9,-7,-8,4,-3,8,7,-3,6,-6,-7,4,-4,10,3,1,4,-6,-9,8,9,-7,1,-7,-8,-3,2,8,-6,-3,-2,10,-4,-10,5,4,3,10,3,-1,10,6,3,2,-2,6,-1,4,3,8,-2,-3,6,-9,3,-10,7,-7,-9,8,3,-9,-2,-10,7,-6,2,5,5,9,-5,-2,-4,-3,-9,-6,6,-7,-8,-5,6,-5,-3,10,-4,7,-9,-2,-10,-8,5,-1,9,9,-8,-4,8,-5,-8,10,-6,-1,-7,-8,7,8,-9,-3,9,-8,8,1,9,-8,3,-9,4,3,-3,10,8,2,-7,6,8,-2,5,-2,-9,3,8,-2,2,-6,6,-4,2,-2,2,-4,3,5,-9,-4,9,2,-1,-10,10,7,1,-2,1,3,-3,4,-5,8,7,-4,-1,-4,3,-5,-9,10,-6,-7,6], dtype = "int8")#candidate|3999|(567,)|const|int8
bop_4000 = relay.less(bop_3996.astype('bool'), relay.reshape(const_3999.astype('bool'), relay.shape_of(bop_3996))) # shape=(567,)
output = relay.Tuple([call_3966,call_3974,const_3975,call_3979,bop_4000,])
output2 = relay.Tuple([call_3967,call_3976,const_3975,call_3981,bop_4000,])
func_4010 = relay.Function([var_3995,], output)
mod['func_4010'] = func_4010
mod = relay.transform.InferType()(mod)
var_4011 = relay.var("var_4011", dtype = "float64", shape = (567,))#candidate|4011|(567,)|var|float64
output = func_4010(var_4011)
func_4012 = relay.Function([var_4011], output)
mutated_mod['func_4012'] = func_4012
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3246_call = mod.get_global_var('func_3246')
func_3248_call = mutated_mod.get_global_var('func_3248')
call_4035 = relay.TupleGetItem(func_3246_call(), 2)
call_4036 = relay.TupleGetItem(func_3248_call(), 2)
output = relay.Tuple([call_4035,])
output2 = relay.Tuple([call_4036,])
func_4071 = relay.Function([], output)
mod['func_4071'] = func_4071
mod = relay.transform.InferType()(mod)
output = func_4071()
func_4072 = relay.Function([], output)
mutated_mod['func_4072'] = func_4072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2259_call = mod.get_global_var('func_2259')
func_2261_call = mutated_mod.get_global_var('func_2261')
call_4101 = relay.TupleGetItem(func_2259_call(), 0)
call_4102 = relay.TupleGetItem(func_2261_call(), 0)
func_1561_call = mod.get_global_var('func_1561')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_4110 = relay.TupleGetItem(func_1561_call(), 4)
call_4111 = relay.TupleGetItem(func_1562_call(), 4)
output = relay.Tuple([call_4101,call_4110,])
output2 = relay.Tuple([call_4102,call_4111,])
func_4114 = relay.Function([], output)
mod['func_4114'] = func_4114
mod = relay.transform.InferType()(mod)
mutated_mod['func_4114'] = func_4114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4114_call = mutated_mod.get_global_var('func_4114')
call_4115 = func_4114_call()
output = call_4115
func_4116 = relay.Function([], output)
mutated_mod['func_4116'] = func_4116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4123 = relay.var("var_4123", dtype = "int16", shape = (2, 10, 7))#candidate|4123|(2, 10, 7)|var|int16
const_4124 = relay.const([[[10,1,-5,-6,-8,-5,7],[-8,5,-2,8,-2,-3,9],[8,1,7,-4,4,7,4],[-1,-10,-4,5,-4,2,-2],[-4,2,-10,2,7,-10,-7],[-3,8,4,4,-5,-3,-4],[6,-2,6,-4,7,2,3],[6,-8,1,-4,-8,-4,-9],[-3,-4,10,-1,9,1,-1],[-1,6,4,-8,-3,-3,-3]],[[3,6,7,-7,5,3,3],[-2,-8,1,-10,-1,-4,-1],[3,-6,7,2,-3,3,7],[3,-10,8,-10,6,-6,8],[-9,-8,4,1,-7,7,2],[-9,-6,2,-9,-5,-9,-9],[-8,-4,-8,9,8,3,-3],[-5,-10,7,-7,1,-7,-5],[9,-1,10,4,-10,10,-5],[1,-5,6,-1,1,-1,-5]]], dtype = "int16")#candidate|4124|(2, 10, 7)|const|int16
bop_4125 = relay.minimum(var_4123.astype('int16'), relay.reshape(const_4124.astype('int16'), relay.shape_of(var_4123))) # shape=(2, 10, 7)
output = bop_4125
output2 = bop_4125
func_4134 = relay.Function([var_4123,], output)
mod['func_4134'] = func_4134
mod = relay.transform.InferType()(mod)
mutated_mod['func_4134'] = func_4134
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4135 = relay.var("var_4135", dtype = "int16", shape = (2, 10, 7))#candidate|4135|(2, 10, 7)|var|int16
func_4134_call = mutated_mod.get_global_var('func_4134')
call_4136 = func_4134_call(var_4135)
output = call_4136
func_4137 = relay.Function([var_4135], output)
mutated_mod['func_4137'] = func_4137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1950_call = mod.get_global_var('func_1950')
func_1951_call = mutated_mod.get_global_var('func_1951')
call_4173 = func_1950_call()
call_4174 = func_1950_call()
uop_4176 = relay.cos(call_4173.astype('float64')) # shape=(1, 15, 5)
uop_4178 = relay.cos(call_4174.astype('float64')) # shape=(1, 15, 5)
output = uop_4176
output2 = uop_4178
func_4179 = relay.Function([], output)
mod['func_4179'] = func_4179
mod = relay.transform.InferType()(mod)
output = func_4179()
func_4180 = relay.Function([], output)
mutated_mod['func_4180'] = func_4180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_4210 = relay.TupleGetItem(func_893_call(), 0)
call_4211 = relay.TupleGetItem(func_894_call(), 0)
output = relay.Tuple([call_4210,])
output2 = relay.Tuple([call_4211,])
func_4213 = relay.Function([], output)
mod['func_4213'] = func_4213
mod = relay.transform.InferType()(mod)
mutated_mod['func_4213'] = func_4213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mutated_mod.get_global_var('func_4213')
call_4214 = func_4213_call()
output = call_4214
func_4215 = relay.Function([], output)
mutated_mod['func_4215'] = func_4215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_886_call = mod.get_global_var('func_886')
func_888_call = mutated_mod.get_global_var('func_888')
call_4224 = func_886_call()
call_4225 = func_886_call()
func_1561_call = mod.get_global_var('func_1561')
func_1562_call = mutated_mod.get_global_var('func_1562')
call_4233 = relay.TupleGetItem(func_1561_call(), 6)
call_4234 = relay.TupleGetItem(func_1562_call(), 6)
output = relay.Tuple([call_4224,call_4233,])
output2 = relay.Tuple([call_4225,call_4234,])
func_4250 = relay.Function([], output)
mod['func_4250'] = func_4250
mod = relay.transform.InferType()(mod)
mutated_mod['func_4250'] = func_4250
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4250_call = mutated_mod.get_global_var('func_4250')
call_4251 = func_4250_call()
output = call_4251
func_4252 = relay.Function([], output)
mutated_mod['func_4252'] = func_4252
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1727_call = mod.get_global_var('func_1727')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_4281 = func_1727_call()
call_4282 = func_1727_call()
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
const_4286 = relay.const([-9.040503,2.759448,-0.334001,3.696692,1.891720,-3.976841,-0.472637,-8.544737,-3.996936,-3.831351,7.061590,-5.843547,-5.047372,8.021588,2.818778,6.482769,-6.656926,-5.920569,9.933096,3.362069], dtype = "float64")#candidate|4286|(20,)|const|float64
call_4285 = relay.TupleGetItem(func_1650_call(relay.reshape(const_4286.astype('float64'), [4, 1, 5])), 0)
call_4287 = relay.TupleGetItem(func_1652_call(relay.reshape(const_4286.astype('float64'), [4, 1, 5])), 0)
output = relay.Tuple([call_4281,call_4285,const_4286,])
output2 = relay.Tuple([call_4282,call_4287,const_4286,])
func_4291 = relay.Function([], output)
mod['func_4291'] = func_4291
mod = relay.transform.InferType()(mod)
output = func_4291()
func_4292 = relay.Function([], output)
mutated_mod['func_4292'] = func_4292
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3414_call = mod.get_global_var('func_3414')
func_3415_call = mutated_mod.get_global_var('func_3415')
call_4366 = relay.TupleGetItem(func_3414_call(), 0)
call_4367 = relay.TupleGetItem(func_3415_call(), 0)
func_3890_call = mod.get_global_var('func_3890')
func_3893_call = mutated_mod.get_global_var('func_3893')
var_4381 = relay.var("var_4381", dtype = "float32", shape = (16,))#candidate|4381|(16,)|var|float32
const_4382 = relay.const([-5.581472,-5.565147,3.989412,3.897325,8.957308,8.173094,-3.962363,-1.469436,-1.015175,-5.378750,-5.556299,9.550965,9.512176,-5.995942,3.060964,2.466896,-7.124743,-5.694375,2.881085,8.343591,6.298442,-0.580063,0.851428,8.244619,-3.695773,0.920342,1.682247,4.831573,-4.034125,-1.932041,-7.966287,-6.813227,5.500236,-5.573554,-2.518831,3.334854,-1.501049,-1.273216,7.778747,-4.669237,3.008192,-0.561391,-6.750736,-8.278394,0.519935,-3.581583,-2.767508,-0.868473,0.884345,-1.286541,-2.532352,5.301948,9.368559,8.185987,-7.988321,-3.615606,9.638128,-8.623733,-0.915352,4.691111,5.194206,2.961728,-3.884912,3.753437,-9.832398,1.013389,-2.041680,-0.200592,-1.314277,-0.667718,0.412490,5.430743,7.414919,-6.264743,-9.648053,-6.043993,4.148285,6.189852,6.043398,-4.439551,-2.404098,1.725475,-3.074316,-1.074347,2.471772,2.755385,8.718984,6.048718,7.755075,-0.760077,9.118208,7.295985,-7.511642,-4.891732,-0.490549,7.435734,3.827028,2.268792,-8.765486,-7.756475,-6.562408,-7.869628,-1.527474,-1.904220,8.487310,7.986199,5.565331,-7.324894,8.915889,-2.414566,5.944853,-7.921844,-3.457701,-3.370127,0.252940,-6.675381,2.882138,4.839819,-0.126311,1.646006,-5.966433,3.153242,4.020454,8.554421,-7.150058,-2.862377,-3.703313,-8.352356,-2.254484,3.772099,-7.876954,4.589341,9.136598,8.336445,1.777443,1.504621,-0.852201,6.896904,-9.487583,-3.123658,-1.253788,-8.846440,-3.547006,0.192628,-8.866670,-9.744888,-3.881817,-0.338440,4.541019,-5.132829,-8.994513,-4.880663,-4.550294,-7.441898,3.472766,3.627240,-2.832619,-8.567416,3.760678,0.801470,-9.140294,-5.624259,-1.525317,-9.141471,-2.445462,-7.649771,2.233029,1.107345,-4.096634,-4.258669,6.432121,-4.765335,-2.014054,-1.333830,-3.686635,9.620818,9.648899,-3.358783,-0.718894,4.501478,6.211427,1.543830,4.579672,-2.821793,-4.359510,5.382828,-7.027910,6.521486,-0.197527,-3.282356,-7.383931,9.742811,4.712151,7.337013,2.918914,3.876844,-2.094927,9.459753,4.081410,0.325012,-0.009152,2.345890,-8.376131,3.022176,-7.942359,-2.128150,0.847738,5.766797,3.496726,-7.090064,6.325985,5.809723,-6.536139,3.625680,-1.677227,-2.377170,5.819296,3.005880,-4.550153,-2.939917,0.086382,1.506482,1.504542,7.970150,4.928677,3.818224,3.694941,-3.134455,8.962591,-8.161238,3.470544,-3.717366,-1.459780,-5.403340,8.666814,-3.316625,2.141514,2.721122,-5.908599,5.853180], dtype = "float32")#candidate|4382|(240,)|const|float32
call_4380 = relay.TupleGetItem(func_3890_call(relay.reshape(var_4381.astype('float32'), [1, 8, 2]), relay.reshape(const_4382.astype('float32'), [15, 8, 2]), ), 0)
call_4383 = relay.TupleGetItem(func_3893_call(relay.reshape(var_4381.astype('float32'), [1, 8, 2]), relay.reshape(const_4382.astype('float32'), [15, 8, 2]), ), 0)
output = relay.Tuple([call_4366,call_4380,var_4381,const_4382,])
output2 = relay.Tuple([call_4367,call_4383,var_4381,const_4382,])
func_4385 = relay.Function([var_4381,], output)
mod['func_4385'] = func_4385
mod = relay.transform.InferType()(mod)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4386 = relay.var("var_4386", dtype = "float32", shape = (16,))#candidate|4386|(16,)|var|float32
func_4385_call = mutated_mod.get_global_var('func_4385')
call_4387 = func_4385_call(var_4386)
output = call_4387
func_4388 = relay.Function([var_4386], output)
mutated_mod['func_4388'] = func_4388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1932_call = mutated_mod.get_global_var('func_1932')
call_4390 = relay.TupleGetItem(func_1931_call(), 1)
call_4391 = relay.TupleGetItem(func_1932_call(), 1)
output = relay.Tuple([call_4390,])
output2 = relay.Tuple([call_4391,])
func_4398 = relay.Function([], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
output = func_4398()
func_4399 = relay.Function([], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4431 = relay.var("var_4431", dtype = "float64", shape = (10, 3, 10))#candidate|4431|(10, 3, 10)|var|float64
uop_4432 = relay.log10(var_4431.astype('float64')) # shape=(10, 3, 10)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_4439 = relay.TupleGetItem(func_904_call(), 0)
call_4440 = relay.TupleGetItem(func_906_call(), 0)
var_4454 = relay.var("var_4454", dtype = "float64", shape = (10, 3, 10))#candidate|4454|(10, 3, 10)|var|float64
bop_4455 = relay.mod(uop_4432.astype('float64'), relay.reshape(var_4454.astype('float64'), relay.shape_of(uop_4432))) # shape=(10, 3, 10)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_4459 = func_1779_call()
call_4460 = func_1779_call()
bop_4462 = relay.less_equal(var_4454.astype('bool'), relay.reshape(uop_4432.astype('bool'), relay.shape_of(var_4454))) # shape=(10, 3, 10)
func_2867_call = mod.get_global_var('func_2867')
func_2869_call = mutated_mod.get_global_var('func_2869')
call_4466 = relay.TupleGetItem(func_2867_call(), 1)
call_4467 = relay.TupleGetItem(func_2869_call(), 1)
output = relay.Tuple([call_4439,bop_4455,call_4459,bop_4462,call_4466,])
output2 = relay.Tuple([call_4440,bop_4455,call_4460,bop_4462,call_4467,])
func_4474 = relay.Function([var_4431,var_4454,], output)
mod['func_4474'] = func_4474
mod = relay.transform.InferType()(mod)
mutated_mod['func_4474'] = func_4474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4474_call = mutated_mod.get_global_var('func_4474')
var_4476 = relay.var("var_4476", dtype = "float64", shape = (10, 3, 10))#candidate|4476|(10, 3, 10)|var|float64
var_4477 = relay.var("var_4477", dtype = "float64", shape = (10, 3, 10))#candidate|4477|(10, 3, 10)|var|float64
call_4475 = func_4474_call(var_4476,var_4477,)
output = call_4475
func_4478 = relay.Function([var_4476,var_4477,], output)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
call_4503 = relay.TupleGetItem(func_904_call(), 0)
call_4504 = relay.TupleGetItem(func_906_call(), 0)
func_3528_call = mod.get_global_var('func_3528')
func_3531_call = mutated_mod.get_global_var('func_3531')
const_4545 = relay.const([-3.943730,0.861533,-8.679465,-2.312009,-4.740501,2.868037,-5.781293,9.268433,-0.731768,-5.081903,-2.577352,4.026070,9.207545,-6.931839,-7.199297,-1.906571,5.616885,-4.900034,-8.963073,-9.089164,-4.784436,0.376133,4.474866,2.290702,-5.813334,1.812253,6.768034,-8.620297,9.706446,8.705951,-2.110965,5.028747,7.460026,-9.126797,-8.285338,-2.785924,-9.912154,0.135057,-1.208600,-3.595235,-3.657248,-5.981064,-5.364497,-3.499620,6.450275,1.309779,-3.892603,0.596994,-3.214281,0.548746,-8.554463,3.474771,6.698771,4.283439,0.121436,7.289401,6.035544,9.086341,-7.064627,-5.158066,-2.011644,4.815803,-6.965787,-7.687974,-1.841088,9.651976,-2.803763,-5.606087,0.264696,6.137244,2.448612,-3.968154,-1.854750,-0.616347,2.927757,-1.046594,-6.661628,-9.186907,-7.939034,7.310745,4.235481,-2.061846,-5.153554,0.232707,-4.668139,-0.588093,8.946083,-5.026360,4.766024,-1.031733,7.712190,-8.653649,7.590033,-7.249042,5.832497,-0.978995,-6.252070,-1.148778,7.258007,-9.862175,7.640624,8.928412,3.168166,-0.368642,-6.199048,-6.331369,-9.925971,4.315616,0.343347,0.512264,-0.697415,3.044470,-7.796965,4.741959,-2.257857,0.425886,-3.685978,-6.019224,8.022405,-6.838507,-3.855864,5.053469,0.987286,-9.667498,8.720917,-4.198077,1.843541,-7.126628,4.099545,-4.801125,-2.458541,5.097301,-3.445296,-7.583276,0.752660,-5.507889,6.898375,-9.770501,-5.364794,-7.381139,-2.489065,6.886527,-3.070038,-7.901842,2.723677,9.302251,-3.751582,3.515797,6.763951,-7.459474,-4.383829,-5.752153,6.504557,6.070159,3.161754,5.351484,-8.692114,6.418609,-5.532930,-8.723159,-8.571635,4.532005,8.673751,-0.364905,5.439261,9.171192,3.313088,8.374811,-7.033506,-9.162631,-1.941613,1.754744,1.178788,-2.726992,-4.975665,3.715770,-5.072815,-1.923938,4.728734,-6.223351,0.443809,8.455964,9.909325,7.081162,3.012444,2.577480,0.922746,-0.208657,-7.021472,7.901919,1.768754,9.042504,8.924241,2.191852,-4.929251,4.051651,3.657235,-3.758594,-9.571850,-3.799989,-5.663458,6.514820,8.456812,-4.979538,-5.176859,-6.514847,-3.377977,-5.094004,1.148498,5.260824,3.639401,-9.874326,0.570700,-5.068444,-4.864755,3.829766,-6.955914,3.277374,-7.614256,6.325586,5.165726,-0.190919,-3.057553,6.397152,8.333484,0.248838,-1.500973,0.237287,2.723844,9.780403,8.429057,-9.130113,0.768860,0.160358,3.507369,5.032718,-5.121890,-5.370800,-7.191382,3.813102,-4.166718,-6.665885,-2.767170,-9.473129,0.812695,7.771046,-2.497844,3.846718,2.600013,9.667656,2.935140,8.264922,7.787397,-1.642837,-0.406700,8.129599,6.689316,9.358655,2.671345,5.918176,1.652707,8.522959,-1.503077,1.534501,0.545690,-8.145826,2.379365,9.534707,2.195448,-7.845936,0.887696,4.651316,-0.657330,-0.050110,-0.321051,-5.610643,-5.619787,-4.778975,-6.359102,0.366630,-4.893745,7.695869,3.211481,-9.131128,-7.587450,-0.168790,-4.944725,-1.765844,-1.530725,3.252937,-6.602278,-0.839436,1.224091,6.930317,5.378270,-9.461118,-7.943697,9.593305,-2.088519,7.438030,9.774932,-6.271705,6.280846,-4.550666,3.154430,-7.657232,7.693296,-5.967098,8.412635,7.050374,-7.604966,0.493872,1.026975,1.368262,-6.228912,-9.026795,-8.013786,-2.020580,-4.239479,-4.093899,-1.180750,6.381663,6.368197,-6.288938,-5.249600,5.336088,8.324331,2.937329,-3.080692,-3.004823,5.282139,-2.645194,8.022539,7.709522,7.902781,9.115400,7.126473,5.723788,9.974992,2.237195,4.479327,-5.958783,9.578796,3.490063,-0.737157,8.042764,0.143740,-2.295545,-1.796043,-6.282851,9.225314,2.197922,-6.442696,6.596923,-4.953684,0.459138,-6.981485,0.910259,-3.054592,8.819792,-3.786967,-7.353627,-7.259081,7.813336,7.571719,-5.324895,6.100838,1.051409,-5.665131,6.837483,0.306640,0.548013,2.122687,-7.929557,1.850516,-8.818448,-1.039596,3.440591,0.271617,0.870532,-5.196509,9.215816,1.545463,-6.043989,-1.350965,-0.369236,-0.596386,3.097629,-8.223083,2.395241,4.637818,-6.505532,8.600743,-9.933857,-5.226304,1.844907,8.131233,-7.069880,6.793815,-8.211315,8.902284,6.428067,-5.547105,1.803000,-4.020925,1.158064,-0.409361,0.382131,8.513346,3.641749,1.128190,5.827385,4.727520,0.797686,-7.034625,-5.803173,5.641259,4.022195,-8.930310,-2.783649,-4.372038,-1.758008,6.950470,-5.672777,6.205491,-7.915699,-2.883159,5.446413,-2.883731,-2.114679,4.514017,-3.481145,-5.184478,-4.198250,-2.490440,-7.154795,-9.609838,2.458541,-2.347863,0.154178,9.242433,3.569212,9.219491,-6.380229,7.571099,-6.500143,4.829567,1.732912,-8.003001,8.169340,1.096387,0.739759,-5.312349,9.564285,-2.152690,3.259455,4.203863,2.188608,2.987662,-9.287837,-8.746790,4.688371,6.246913,-2.354927,4.047201,-3.505328,3.438878,-8.589048,-4.511961,-8.283564,-4.687551,3.326919,-3.899723,-3.171504,-7.564250,1.975734,5.114834,-0.416263,1.152487,2.445540,-6.742565,6.071451,0.612424,-4.893805,-5.920877,7.597951,-7.242734,-4.493286,6.764296,-9.263382,1.689153,6.212837,3.170800,1.658870,-4.847087,0.836169,-6.160967,-9.590585,-8.220921,3.210151,4.814720,-2.685441,6.210618,4.184201,3.866520,-6.185139,9.103962,-8.098157,-4.521109,4.818750,-4.843618,9.264961,-6.895999,-0.897454,-9.449309,2.419299,-3.815070,7.344705,-7.177080,6.557720,7.073112,-6.641727,2.352664,7.349133,-4.931274,-9.904520,3.542870,5.665291,3.285683,-2.495419,8.947069,0.428393,9.427330,-7.909477,9.127646,-9.849846,2.059557,8.181855,6.734100,-5.360545,-5.411287,-4.481991,2.421212,2.831557,3.391461,-8.025639], dtype = "float64")#candidate|4545|(546,)|const|float64
call_4544 = func_3528_call(relay.reshape(const_4545.astype('float64'), [13, 14, 3]), relay.reshape(const_4545.astype('float64'), [13, 14, 3]), )
call_4546 = func_3528_call(relay.reshape(const_4545.astype('float64'), [13, 14, 3]), relay.reshape(const_4545.astype('float64'), [13, 14, 3]), )
output = relay.Tuple([call_4503,call_4544,const_4545,])
output2 = relay.Tuple([call_4504,call_4546,const_4545,])
func_4554 = relay.Function([], output)
mod['func_4554'] = func_4554
mod = relay.transform.InferType()(mod)
output = func_4554()
func_4555 = relay.Function([], output)
mutated_mod['func_4555'] = func_4555
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4605 = relay.var("var_4605", dtype = "float32", shape = (16, 8, 7))#candidate|4605|(16, 8, 7)|var|float32
uop_4606 = relay.exp(var_4605.astype('float32')) # shape=(16, 8, 7)
uop_4612 = relay.log2(uop_4606.astype('float64')) # shape=(16, 8, 7)
output = relay.Tuple([uop_4612,])
output2 = relay.Tuple([uop_4612,])
func_4621 = relay.Function([var_4605,], output)
mod['func_4621'] = func_4621
mod = relay.transform.InferType()(mod)
mutated_mod['func_4621'] = func_4621
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4622 = relay.var("var_4622", dtype = "float32", shape = (16, 8, 7))#candidate|4622|(16, 8, 7)|var|float32
func_4621_call = mutated_mod.get_global_var('func_4621')
call_4623 = func_4621_call(var_4622)
output = call_4623
func_4624 = relay.Function([var_4622], output)
mutated_mod['func_4624'] = func_4624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1950_call = mod.get_global_var('func_1950')
func_1951_call = mutated_mod.get_global_var('func_1951')
call_4626 = func_1950_call()
call_4627 = func_1950_call()
output = relay.Tuple([call_4626,])
output2 = relay.Tuple([call_4627,])
func_4634 = relay.Function([], output)
mod['func_4634'] = func_4634
mod = relay.transform.InferType()(mod)
output = func_4634()
func_4635 = relay.Function([], output)
mutated_mod['func_4635'] = func_4635
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4717 = relay.var("var_4717", dtype = "float64", shape = ())#candidate|4717|()|var|float64
var_4718 = relay.var("var_4718", dtype = "float64", shape = (5, 15, 15))#candidate|4718|(5, 15, 15)|var|float64
bop_4719 = relay.floor_mod(var_4717.astype('float64'), var_4718.astype('float64')) # shape=(5, 15, 15)
output = relay.Tuple([bop_4719,])
output2 = relay.Tuple([bop_4719,])
func_4723 = relay.Function([var_4717,var_4718,], output)
mod['func_4723'] = func_4723
mod = relay.transform.InferType()(mod)
mutated_mod['func_4723'] = func_4723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4723_call = mutated_mod.get_global_var('func_4723')
var_4725 = relay.var("var_4725", dtype = "float64", shape = ())#candidate|4725|()|var|float64
var_4726 = relay.var("var_4726", dtype = "float64", shape = (5, 15, 15))#candidate|4726|(5, 15, 15)|var|float64
call_4724 = func_4723_call(var_4725,var_4726,)
output = call_4724
func_4727 = relay.Function([var_4725,var_4726,], output)
mutated_mod['func_4727'] = func_4727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4554_call = mod.get_global_var('func_4554')
func_4555_call = mutated_mod.get_global_var('func_4555')
call_4737 = relay.TupleGetItem(func_4554_call(), 1)
call_4738 = relay.TupleGetItem(func_4555_call(), 1)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_4741 = relay.TupleGetItem(func_3733_call(), 0)
call_4742 = relay.TupleGetItem(func_3735_call(), 0)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_4747 = relay.TupleGetItem(func_893_call(), 0)
call_4748 = relay.TupleGetItem(func_894_call(), 0)
output = relay.Tuple([call_4737,call_4741,call_4747,])
output2 = relay.Tuple([call_4738,call_4742,call_4748,])
func_4761 = relay.Function([], output)
mod['func_4761'] = func_4761
mod = relay.transform.InferType()(mod)
output = func_4761()
func_4762 = relay.Function([], output)
mutated_mod['func_4762'] = func_4762
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4772 = relay.var("var_4772", dtype = "float64", shape = (7, 14, 11))#candidate|4772|(7, 14, 11)|var|float64
uop_4773 = relay.rsqrt(var_4772.astype('float64')) # shape=(7, 14, 11)
func_3305_call = mod.get_global_var('func_3305')
func_3306_call = mutated_mod.get_global_var('func_3306')
call_4790 = func_3305_call()
call_4791 = func_3305_call()
output = relay.Tuple([uop_4773,call_4790,])
output2 = relay.Tuple([uop_4773,call_4791,])
func_4805 = relay.Function([var_4772,], output)
mod['func_4805'] = func_4805
mod = relay.transform.InferType()(mod)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4806 = relay.var("var_4806", dtype = "float64", shape = (7, 14, 11))#candidate|4806|(7, 14, 11)|var|float64
func_4805_call = mutated_mod.get_global_var('func_4805')
call_4807 = func_4805_call(var_4806)
output = call_4807
func_4808 = relay.Function([var_4806], output)
mutated_mod['func_4808'] = func_4808
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4810 = relay.var("var_4810", dtype = "float32", shape = (7, 8, 2))#candidate|4810|(7, 8, 2)|var|float32
uop_4811 = relay.rsqrt(var_4810.astype('float32')) # shape=(7, 8, 2)
bop_4813 = relay.mod(var_4810.astype('float64'), relay.reshape(uop_4811.astype('float64'), relay.shape_of(var_4810))) # shape=(7, 8, 2)
uop_4826 = relay.acos(uop_4811.astype('float64')) # shape=(7, 8, 2)
uop_4828 = relay.atanh(uop_4826.astype('float64')) # shape=(7, 8, 2)
func_2654_call = mod.get_global_var('func_2654')
func_2656_call = mutated_mod.get_global_var('func_2656')
call_4848 = func_2654_call()
call_4849 = func_2654_call()
bop_4857 = relay.greater(uop_4826.astype('bool'), relay.reshape(bop_4813.astype('bool'), relay.shape_of(uop_4826))) # shape=(7, 8, 2)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_4863 = relay.TupleGetItem(func_3733_call(), 1)
call_4864 = relay.TupleGetItem(func_3735_call(), 1)
output = relay.Tuple([uop_4828,call_4848,bop_4857,call_4863,])
output2 = relay.Tuple([uop_4828,call_4849,bop_4857,call_4864,])
func_4870 = relay.Function([var_4810,], output)
mod['func_4870'] = func_4870
mod = relay.transform.InferType()(mod)
mutated_mod['func_4870'] = func_4870
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4871 = relay.var("var_4871", dtype = "float32", shape = (7, 8, 2))#candidate|4871|(7, 8, 2)|var|float32
func_4870_call = mutated_mod.get_global_var('func_4870')
call_4872 = func_4870_call(var_4871)
output = call_4872
func_4873 = relay.Function([var_4871], output)
mutated_mod['func_4873'] = func_4873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4179_call = mod.get_global_var('func_4179')
func_4180_call = mutated_mod.get_global_var('func_4180')
call_4886 = func_4179_call()
call_4887 = func_4179_call()
output = call_4886
output2 = call_4887
func_4890 = relay.Function([], output)
mod['func_4890'] = func_4890
mod = relay.transform.InferType()(mod)
mutated_mod['func_4890'] = func_4890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4890_call = mutated_mod.get_global_var('func_4890')
call_4891 = func_4890_call()
output = call_4891
func_4892 = relay.Function([], output)
mutated_mod['func_4892'] = func_4892
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_4901 = relay.TupleGetItem(func_3507_call(), 0)
call_4902 = relay.TupleGetItem(func_3508_call(), 0)
func_1898_call = mod.get_global_var('func_1898')
func_1899_call = mutated_mod.get_global_var('func_1899')
call_4908 = relay.TupleGetItem(func_1898_call(), 1)
call_4909 = relay.TupleGetItem(func_1899_call(), 1)
func_2654_call = mod.get_global_var('func_2654')
func_2656_call = mutated_mod.get_global_var('func_2656')
call_4916 = func_2654_call()
call_4917 = func_2654_call()
output = relay.Tuple([call_4901,call_4908,call_4916,])
output2 = relay.Tuple([call_4902,call_4909,call_4917,])
func_4946 = relay.Function([], output)
mod['func_4946'] = func_4946
mod = relay.transform.InferType()(mod)
output = func_4946()
func_4947 = relay.Function([], output)
mutated_mod['func_4947'] = func_4947
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4991 = relay.var("var_4991", dtype = "uint16", shape = (10, 6, 9))#candidate|4991|(10, 6, 9)|var|uint16
var_4992 = relay.var("var_4992", dtype = "uint16", shape = (10, 6, 9))#candidate|4992|(10, 6, 9)|var|uint16
bop_4993 = relay.add(var_4991.astype('uint16'), relay.reshape(var_4992.astype('uint16'), relay.shape_of(var_4991))) # shape=(10, 6, 9)
output = relay.Tuple([bop_4993,])
output2 = relay.Tuple([bop_4993,])
func_5000 = relay.Function([var_4991,var_4992,], output)
mod['func_5000'] = func_5000
mod = relay.transform.InferType()(mod)
var_5001 = relay.var("var_5001", dtype = "uint16", shape = (10, 6, 9))#candidate|5001|(10, 6, 9)|var|uint16
var_5002 = relay.var("var_5002", dtype = "uint16", shape = (10, 6, 9))#candidate|5002|(10, 6, 9)|var|uint16
output = func_5000(var_5001,var_5002,)
func_5003 = relay.Function([var_5001,var_5002,], output)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2357_call = mod.get_global_var('func_2357')
func_2358_call = mutated_mod.get_global_var('func_2358')
call_5028 = relay.TupleGetItem(func_2357_call(), 1)
call_5029 = relay.TupleGetItem(func_2358_call(), 1)
func_1931_call = mod.get_global_var('func_1931')
func_1932_call = mutated_mod.get_global_var('func_1932')
call_5084 = relay.TupleGetItem(func_1931_call(), 2)
call_5085 = relay.TupleGetItem(func_1932_call(), 2)
output = relay.Tuple([call_5028,call_5084,])
output2 = relay.Tuple([call_5029,call_5085,])
func_5089 = relay.Function([], output)
mod['func_5089'] = func_5089
mod = relay.transform.InferType()(mod)
mutated_mod['func_5089'] = func_5089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5089_call = mutated_mod.get_global_var('func_5089')
call_5090 = func_5089_call()
output = call_5090
func_5091 = relay.Function([], output)
mutated_mod['func_5091'] = func_5091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_5187 = func_1095_call()
call_5188 = func_1095_call()
output = relay.Tuple([call_5187,])
output2 = relay.Tuple([call_5188,])
func_5200 = relay.Function([], output)
mod['func_5200'] = func_5200
mod = relay.transform.InferType()(mod)
mutated_mod['func_5200'] = func_5200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5200_call = mutated_mod.get_global_var('func_5200')
call_5201 = func_5200_call()
output = call_5201
func_5202 = relay.Function([], output)
mutated_mod['func_5202'] = func_5202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5206 = relay.var("var_5206", dtype = "uint32", shape = (5, 6, 14))#candidate|5206|(5, 6, 14)|var|uint32
var_5207 = relay.var("var_5207", dtype = "uint32", shape = (5, 6, 14))#candidate|5207|(5, 6, 14)|var|uint32
bop_5208 = relay.logical_xor(var_5206.astype('uint32'), relay.reshape(var_5207.astype('uint32'), relay.shape_of(var_5206))) # shape=(5, 6, 14)
output = bop_5208
output2 = bop_5208
func_5217 = relay.Function([var_5206,var_5207,], output)
mod['func_5217'] = func_5217
mod = relay.transform.InferType()(mod)
mutated_mod['func_5217'] = func_5217
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5217_call = mutated_mod.get_global_var('func_5217')
var_5219 = relay.var("var_5219", dtype = "uint32", shape = (5, 6, 14))#candidate|5219|(5, 6, 14)|var|uint32
var_5220 = relay.var("var_5220", dtype = "uint32", shape = (5, 6, 14))#candidate|5220|(5, 6, 14)|var|uint32
call_5218 = func_5217_call(var_5219,var_5220,)
output = call_5218
func_5221 = relay.Function([var_5219,var_5220,], output)
mutated_mod['func_5221'] = func_5221
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5273 = relay.var("var_5273", dtype = "float64", shape = (3, 1, 2))#candidate|5273|(3, 1, 2)|var|float64
uop_5274 = relay.sin(var_5273.astype('float64')) # shape=(3, 1, 2)
func_2942_call = mod.get_global_var('func_2942')
func_2943_call = mutated_mod.get_global_var('func_2943')
call_5280 = relay.TupleGetItem(func_2942_call(), 2)
call_5281 = relay.TupleGetItem(func_2943_call(), 2)
func_2584_call = mod.get_global_var('func_2584')
func_2586_call = mutated_mod.get_global_var('func_2586')
var_5295 = relay.var("var_5295", dtype = "float32", shape = (567,))#candidate|5295|(567,)|var|float32
call_5294 = relay.TupleGetItem(func_2584_call(relay.reshape(var_5295.astype('float32'), [567,])), 1)
call_5296 = relay.TupleGetItem(func_2586_call(relay.reshape(var_5295.astype('float32'), [567,])), 1)
output = relay.Tuple([uop_5274,call_5280,call_5294,var_5295,])
output2 = relay.Tuple([uop_5274,call_5281,call_5296,var_5295,])
func_5301 = relay.Function([var_5273,var_5295,], output)
mod['func_5301'] = func_5301
mod = relay.transform.InferType()(mod)
var_5302 = relay.var("var_5302", dtype = "float64", shape = (3, 1, 2))#candidate|5302|(3, 1, 2)|var|float64
var_5303 = relay.var("var_5303", dtype = "float32", shape = (567,))#candidate|5303|(567,)|var|float32
output = func_5301(var_5302,var_5303,)
func_5304 = relay.Function([var_5302,var_5303,], output)
mutated_mod['func_5304'] = func_5304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_5320 = relay.TupleGetItem(func_4761_call(), 0)
call_5321 = relay.TupleGetItem(func_4762_call(), 0)
func_5089_call = mod.get_global_var('func_5089')
func_5091_call = mutated_mod.get_global_var('func_5091')
call_5342 = relay.TupleGetItem(func_5089_call(), 0)
call_5343 = relay.TupleGetItem(func_5091_call(), 0)
func_1281_call = mod.get_global_var('func_1281')
func_1285_call = mutated_mod.get_global_var('func_1285')
const_5349 = relay.const([[9.376471,-4.352867,-0.507649],[6.387553,1.166752,-8.611089],[-2.766778,-8.684520,-3.341851],[-8.871203,6.374582,-8.956230],[-4.241663,5.901127,-3.896514],[-3.897154,-7.858390,2.428760],[6.453285,1.236472,4.598437],[-7.163751,-3.855615,8.546075],[-5.901352,8.417079,8.337259],[-2.284172,6.233905,1.779209],[-4.646121,1.214835,-3.649430],[-1.388883,7.620791,-2.371255],[9.969205,-4.784679,3.297172],[-1.259550,6.051245,-7.402529],[5.517819,-7.771138,-9.420376],[-8.224894,6.565512,6.604657],[-5.368769,7.990614,-7.820305],[2.166964,9.569638,5.592706],[4.286497,-1.395226,9.294225],[2.775691,0.158081,1.199061],[5.287215,0.661506,2.113729],[-4.260334,-2.992342,4.054435],[-3.051378,-2.280831,-1.913483],[-5.092401,5.095413,-4.588080],[2.399270,7.882416,9.189403],[-7.259016,-4.147157,6.273603],[3.108996,4.894144,7.420157],[-1.844541,9.208089,1.709140],[-2.827714,5.141148,1.910918],[-8.539784,-6.648398,6.991651],[-7.771455,-6.810876,9.402812],[-1.154035,-0.961359,-3.965267],[-6.069834,5.428952,7.040074],[5.621911,-3.661298,3.357658],[-9.465613,1.425960,1.711445],[-0.368785,-9.809722,-0.768919],[-8.488821,-4.709256,5.420299],[-8.253752,8.155370,7.660109],[2.267564,-1.608033,-9.183633],[4.562119,2.500052,7.318882],[7.154713,-6.364591,-5.644784],[-4.400806,1.656112,6.623088],[1.866396,-7.365626,7.119290],[-5.090326,-4.798416,7.422533],[-1.301369,1.703395,4.309633],[6.809689,-6.629045,-5.473229],[-5.092762,3.475065,-7.739466],[-7.982207,8.826887,-6.209507],[0.535920,9.101868,-4.292496],[-1.366934,9.091465,-3.830560],[-2.078502,6.152664,-6.454208],[1.987010,-3.447814,-7.700524],[-7.360082,0.091926,-4.822403],[-4.615445,-3.909973,5.678116],[-4.528343,0.664690,-8.194923],[-4.861456,2.443448,5.914281],[-3.063739,6.326083,-4.449933],[6.139554,-1.727970,-4.540826],[-0.406520,-2.106609,-7.467645],[8.954737,8.828286,-1.320424],[6.593450,-3.095579,-5.047557],[-9.367168,6.737925,-4.228607],[2.712239,-9.133953,-7.858467],[-3.344267,0.469870,3.088332],[0.215922,3.965270,7.398408],[-5.969302,-0.451888,-8.744228],[-0.091977,3.932622,-1.030904],[3.034198,0.304620,0.466711],[-2.868743,6.900473,9.637627],[5.933066,9.203479,8.634194],[-4.628436,1.731086,1.574355],[-6.097251,-3.492095,0.797514],[9.821207,8.798579,-0.770475],[-5.565614,-0.379755,-5.689130],[-1.190273,-6.182341,-4.255828],[-2.552691,8.760044,-6.261755],[8.973961,8.193632,-1.236585],[-2.269947,2.673945,4.978560],[8.351524,1.724467,5.396699],[8.069615,6.490911,8.735981],[9.607923,2.272391,-8.155771],[9.592007,-3.988337,6.650929],[8.015414,-8.373294,7.278964],[-4.160666,7.208768,7.033425],[-7.024551,-8.621736,-2.671187],[1.154666,1.386980,2.414557],[-7.963833,-2.332964,7.448523],[-4.112397,1.841210,8.212686],[-4.565381,3.733191,5.682179],[-8.450740,7.261852,-7.151961],[-2.197514,-3.791452,-9.979426],[3.679763,-1.991191,0.124131],[-8.873062,1.397437,-6.097574],[-0.868383,-9.076852,-6.176619],[-4.359157,7.033318,3.818880],[-4.018403,-5.485730,3.095909],[-1.588248,3.775958,-7.770039],[-6.644947,-5.610309,6.258767],[-4.782227,9.155807,9.877060],[5.945283,-3.749228,-0.014515],[-5.539139,-4.276798,5.346139],[3.846640,-6.903578,-4.739268],[3.239790,2.038494,-7.671310],[-0.808055,6.408909,-9.842048],[9.666436,-3.292193,-7.334338],[3.304670,0.678708,1.395439],[6.048840,-4.437928,-8.111469],[6.453121,0.684493,6.687607],[7.886659,7.863038,-1.130420],[4.502476,6.663154,2.907469],[-8.506434,-3.037838,-3.606233],[-9.875520,-9.618361,-6.419119],[-3.633580,-7.105383,-6.588989],[3.745143,1.212132,-5.569266],[-4.648126,1.042756,-8.328581],[-1.123966,2.774427,-0.447761],[-3.234304,4.524906,-6.942561],[2.240834,5.370958,-4.104498],[-2.237692,2.912439,-9.365650],[4.276490,-6.102701,-0.673524],[6.227321,2.145216,0.871264],[9.763526,6.391191,-8.500957],[-5.518335,-9.288680,1.367136],[9.379992,-1.038266,0.174220],[3.563436,-1.930148,9.427213],[-5.806396,2.453745,9.516804],[8.753822,-4.429732,-1.162388],[-5.817858,2.457345,-5.236957],[-3.432463,-1.766527,0.794914],[8.373453,-5.784766,-9.116297],[2.695296,-6.902439,-1.611520],[7.629632,-8.766225,-7.804438],[3.636578,2.818800,5.531518],[3.505253,-7.374260,9.658563],[-4.836741,-7.775762,-7.839550],[-1.465325,5.702847,-4.226797],[4.603564,8.990656,7.893247],[-3.689573,8.158904,7.829618],[7.882092,-0.715248,-8.185502],[7.682678,-8.614998,7.763205],[-6.573549,-4.977230,3.013712],[-3.194326,4.005410,-6.319497],[2.025130,2.936310,2.573066],[-8.023413,9.579090,-9.842953],[-2.107778,-9.042020,7.784902],[2.769426,-3.903150,9.324669],[-6.832167,-5.712821,8.442055],[-2.712864,8.626275,3.011369],[0.633786,4.546111,-4.256223],[-9.491691,-3.358575,-4.427600],[3.466440,5.424298,7.497527],[1.449877,-7.965466,4.263355],[-3.259756,1.819869,3.814033],[-8.340509,-5.518481,-0.400559],[5.180808,9.284084,8.616568],[5.542568,7.943598,-6.204576],[5.935003,-3.845942,5.053097],[-6.405656,6.513122,8.985918],[-6.990497,9.695322,-4.683423],[-6.949458,3.522098,3.061290],[4.817466,4.728945,0.595890],[0.860144,5.621445,7.702942],[-7.289702,-6.548661,8.830966],[-5.308970,-7.919571,-7.657218],[3.357042,-0.855052,-2.490888],[-2.873281,4.721863,-3.829504],[8.692334,8.843079,5.189133],[-9.925421,-9.669056,4.919570],[-3.531983,-5.165001,-0.703450],[1.676420,2.381786,-0.009941],[1.266503,4.292936,-3.126647],[-5.804746,7.676647,-3.755269],[-7.026625,-1.248955,0.176572],[-0.549984,-1.192466,-1.427936],[9.948136,-4.203031,-2.280999],[-2.783194,8.611176,-9.706273],[5.369578,-2.955585,-0.433431],[2.982744,0.400561,-2.080627],[0.179867,-6.746213,3.524504],[-7.163810,0.172079,5.743033],[4.803530,5.117286,6.227980],[-8.281247,-4.401746,5.215042],[8.214045,1.090678,8.732700],[-7.351029,-0.017560,-1.776064],[0.637958,-4.682254,8.937859],[-4.278710,9.745375,-3.562227],[4.453084,0.532492,0.899032],[3.486557,0.347330,6.592601],[-6.670770,-9.225286,-3.431637]], dtype = "float32")#candidate|5349|(189, 3)|const|float32
call_5348 = func_1281_call(relay.reshape(const_5349.astype('float32'), [7, 9, 9]), relay.reshape(const_5349.astype('float32'), [7, 9, 9]), )
call_5350 = func_1281_call(relay.reshape(const_5349.astype('float32'), [7, 9, 9]), relay.reshape(const_5349.astype('float32'), [7, 9, 9]), )
func_1383_call = mod.get_global_var('func_1383')
func_1385_call = mutated_mod.get_global_var('func_1385')
call_5372 = relay.TupleGetItem(func_1383_call(relay.reshape(call_5342.astype('float64'), [3, 4, 3])), 0)
call_5373 = relay.TupleGetItem(func_1385_call(relay.reshape(call_5342.astype('float64'), [3, 4, 3])), 0)
func_1044_call = mod.get_global_var('func_1044')
func_1046_call = mutated_mod.get_global_var('func_1046')
call_5376 = relay.TupleGetItem(func_1044_call(), 1)
call_5377 = relay.TupleGetItem(func_1046_call(), 1)
func_3267_call = mod.get_global_var('func_3267')
func_3268_call = mutated_mod.get_global_var('func_3268')
call_5381 = relay.TupleGetItem(func_3267_call(), 0)
call_5382 = relay.TupleGetItem(func_3268_call(), 0)
output = relay.Tuple([call_5320,call_5342,call_5348,const_5349,call_5372,call_5376,call_5381,])
output2 = relay.Tuple([call_5321,call_5343,call_5350,const_5349,call_5373,call_5377,call_5382,])
func_5387 = relay.Function([], output)
mod['func_5387'] = func_5387
mod = relay.transform.InferType()(mod)
output = func_5387()
func_5388 = relay.Function([], output)
mutated_mod['func_5388'] = func_5388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_5412 = func_1095_call()
call_5413 = func_1095_call()
output = call_5412
output2 = call_5413
func_5417 = relay.Function([], output)
mod['func_5417'] = func_5417
mod = relay.transform.InferType()(mod)
mutated_mod['func_5417'] = func_5417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5417_call = mutated_mod.get_global_var('func_5417')
call_5418 = func_5417_call()
output = call_5418
func_5419 = relay.Function([], output)
mutated_mod['func_5419'] = func_5419
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5470 = relay.const([[[4,7,-7,-9,8,-2,6,2,-2,-10,-5,1,5,-1,-9,-7],[2,-4,6,-5,-3,-9,1,-5,-4,-2,-10,-10,-8,-7,1,9],[8,4,7,10,8,-3,1,-2,2,5,-8,8,6,-10,-1,-2]],[[-4,-5,-6,3,2,-3,-3,-9,8,9,-9,-1,-4,3,1,4],[-2,6,-2,1,6,-1,8,6,-6,-3,3,9,8,5,-7,-7],[-8,4,4,5,9,1,-6,5,-1,6,-4,-3,6,2,-7,-10]],[[-1,-6,-2,-7,7,-10,2,-6,4,8,8,10,9,7,8,2],[6,6,-9,10,-10,10,6,6,-9,-7,6,-10,9,3,-9,-9],[-3,4,10,7,-4,2,4,-1,-2,9,-8,-5,8,-6,-4,-1]],[[-10,6,-9,-9,-1,-7,9,-7,8,1,7,-5,-5,-2,-6,6],[10,-7,5,3,7,3,8,10,-8,-4,-8,-9,-9,-4,6,4],[-1,2,-9,4,-5,-3,-6,6,6,6,8,9,-6,6,-2,-5]],[[-1,9,-4,-5,7,-1,-3,-5,-9,-2,-6,-8,-1,-4,3,6],[-10,4,-5,4,-9,4,-2,-2,10,9,3,10,-2,-9,-6,10],[9,10,5,5,-9,-7,-10,3,2,-7,1,-1,4,9,4,-5]],[[-3,6,-1,1,1,-10,-8,-2,6,5,9,-10,3,-6,-9,9],[-8,-10,-5,-8,1,-9,10,9,-1,3,8,6,3,10,2,1],[-4,10,4,-10,-5,-5,-10,-1,9,-4,7,2,-1,9,-2,5]],[[3,-9,-5,-3,-6,5,3,9,-10,-10,-1,7,5,-7,-8,4],[2,-10,10,7,-2,-4,-8,8,5,5,10,-10,-7,3,3,-9],[-1,-10,-2,1,-9,8,9,5,6,10,1,-3,10,4,-3,6]],[[1,9,5,9,6,-1,-5,-8,6,7,1,4,5,-3,-2,-4],[-7,8,4,5,-7,4,-3,-5,2,6,1,3,9,-6,-6,-4],[5,2,9,9,4,-10,-6,5,6,-1,1,-6,-3,1,-5,10]]], dtype = "int32")#candidate|5470|(8, 3, 16)|const|int32
const_5471 = relay.const([[[4,-5,-2,-7,-3,-1,8,-5,-2,-1,-9,-1,2,-6,10,2],[-1,-6,-9,7,5,10,-10,2,-7,-2,-5,7,2,-4,5,8],[-4,9,7,-7,6,8,4,9,-3,8,-4,7,-10,-10,-8,-1]],[[3,8,-5,-6,6,-6,-4,-10,6,6,2,-5,4,-7,2,-7],[-7,-6,-3,1,6,8,2,6,-7,-7,-6,3,-8,4,-10,6],[7,-10,-4,-10,8,-10,-9,2,9,-8,2,4,-6,9,-1,-3]],[[-6,-1,-4,3,-10,-6,-1,8,6,4,-7,-9,9,9,2,10],[-5,-10,-3,-2,-8,-3,-5,-9,-7,10,-3,9,6,6,1,5],[7,4,-8,5,3,5,1,2,8,3,10,5,-1,-3,7,6]],[[-5,5,7,1,8,-1,-1,8,-4,1,3,1,7,6,-3,-7],[5,4,-2,5,3,10,8,3,8,-7,2,-7,-5,2,-7,8],[8,7,7,1,-9,-3,-8,-10,-4,9,6,-4,1,9,-4,-2]],[[-9,4,3,5,6,-9,-8,-3,8,8,-10,-5,10,-8,2,-9],[-1,6,-10,-7,9,-3,7,-9,9,-10,-4,9,10,-10,-9,1],[2,7,-8,-10,-10,-6,-10,1,4,10,6,-2,9,9,1,-2]],[[-9,6,-1,6,1,8,9,-3,-3,-3,-6,-5,4,-5,-6,-9],[3,-2,-2,-8,2,-6,-7,6,-4,9,3,-5,10,4,-6,-10],[-8,5,-3,-3,-1,8,8,8,-2,-1,4,3,-5,-9,10,2]],[[-2,-8,-2,-9,-9,-10,2,10,8,-10,9,-6,10,7,-5,-10],[8,1,10,-4,7,-8,6,5,-9,-6,-8,-3,8,-2,9,-7],[9,-8,7,8,7,-5,3,-7,-4,-1,5,-3,-3,5,5,10]],[[9,-3,-3,-2,-8,-5,4,-3,7,1,7,-7,6,-4,-4,-7],[6,9,4,10,-6,-10,7,1,7,-7,5,-7,-4,4,-7,10],[2,3,-1,-7,-7,9,2,9,-1,6,-10,7,-3,-1,3,-6]]], dtype = "int32")#candidate|5471|(8, 3, 16)|const|int32
bop_5472 = relay.bitwise_xor(const_5470.astype('int32'), relay.reshape(const_5471.astype('int32'), relay.shape_of(const_5470))) # shape=(8, 3, 16)
output = bop_5472
output2 = bop_5472
func_5477 = relay.Function([], output)
mod['func_5477'] = func_5477
mod = relay.transform.InferType()(mod)
output = func_5477()
func_5478 = relay.Function([], output)
mutated_mod['func_5478'] = func_5478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1095_call = mod.get_global_var('func_1095')
func_1096_call = mutated_mod.get_global_var('func_1096')
call_5482 = func_1095_call()
call_5483 = func_1095_call()
func_3687_call = mod.get_global_var('func_3687')
func_3690_call = mutated_mod.get_global_var('func_3690')
var_5485 = relay.var("var_5485", dtype = "float32", shape = (9, 63))#candidate|5485|(9, 63)|var|float32
call_5484 = relay.TupleGetItem(func_3687_call(relay.reshape(var_5485.astype('float32'), [567,]), relay.reshape(var_5485.astype('bool'), [567,]), ), 1)
call_5486 = relay.TupleGetItem(func_3690_call(relay.reshape(var_5485.astype('float32'), [567,]), relay.reshape(var_5485.astype('bool'), [567,]), ), 1)
output = relay.Tuple([call_5482,call_5484,var_5485,])
output2 = relay.Tuple([call_5483,call_5486,var_5485,])
func_5492 = relay.Function([var_5485,], output)
mod['func_5492'] = func_5492
mod = relay.transform.InferType()(mod)
var_5493 = relay.var("var_5493", dtype = "float32", shape = (9, 63))#candidate|5493|(9, 63)|var|float32
output = func_5492(var_5493)
func_5494 = relay.Function([var_5493], output)
mutated_mod['func_5494'] = func_5494
mutated_mod = relay.transform.InferType()(mutated_mod)
func_946_call = mod.get_global_var('func_946')
func_947_call = mutated_mod.get_global_var('func_947')
call_5513 = func_946_call()
call_5514 = func_946_call()
output = relay.Tuple([call_5513,])
output2 = relay.Tuple([call_5514,])
func_5515 = relay.Function([], output)
mod['func_5515'] = func_5515
mod = relay.transform.InferType()(mod)
output = func_5515()
func_5516 = relay.Function([], output)
mutated_mod['func_5516'] = func_5516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5515_call = mod.get_global_var('func_5515')
func_5516_call = mutated_mod.get_global_var('func_5516')
call_5533 = relay.TupleGetItem(func_5515_call(), 0)
call_5534 = relay.TupleGetItem(func_5516_call(), 0)
func_4805_call = mod.get_global_var('func_4805')
func_4808_call = mutated_mod.get_global_var('func_4808')
const_5547 = relay.const([-6.774227,6.866683,-4.934254,-0.263150,-8.683416,-1.596310,1.847677,-1.755035,5.339808,1.050900,-4.077247,0.844592,-8.668784,-9.889441,-9.716503,-2.218478,2.477969,2.756403,9.769617,0.462766,-4.507058,-8.766913,3.584788,-9.508864,-4.194275,3.495772,8.111929,-3.757740,-0.176833,1.823695,-2.357809,8.605272,3.726846,8.499571,-4.209864,-2.630068,3.500510,2.301931,-2.637995,1.546092,2.747892,5.366047,1.642654,-3.303860,-7.516142,1.282098,7.282142,-6.896525,8.229438,7.983948,3.870968,7.418678,3.655479,7.513414,-2.760145,-7.508049,5.891934,0.228233,2.943826,-8.326442,7.653979,-6.228696,-7.578775,-2.750489,9.376069,7.108377,2.796411,6.203120,4.422170,-0.705417,0.583754,1.894082,-2.768634,9.120738,3.107632,-7.681607,3.078980,8.695318,5.812281,-3.593334,-9.102433,3.530297,-8.413254,-5.897197,5.195567,3.882157,1.110472,3.840528,3.879255,-3.933201,-4.270988,-0.840023,4.567326,9.026225,5.639196,4.776809,-9.607192,8.947339,0.330021,-4.314740,2.526420,4.286512,9.616529,-9.136398,-8.915796,4.952918,9.339928,-0.459518,2.210972,-6.253927,0.716092,-2.708670,-5.615080,-6.942131,8.483157,8.741730,3.948809,-8.535208,8.215029,7.192228,3.453260,9.822653,-4.242414,9.056751,0.787767,-8.084425,-6.793166,-8.666909,0.999827,-8.930932,-1.838784,3.679661,5.820601,-7.717113,-8.145408,-5.330507,-3.307263,2.094139,4.834274,-6.275834,-4.306304,-5.484034,-9.207415,9.609457,5.350875,-9.045917,2.941516,8.473785,0.803545,-4.900222,-3.612112,1.632002,-1.016717,2.771986,-0.228433,-2.896111,9.544308,2.563420,-6.303750,3.082001,-0.805386,7.937186,2.071668,-8.822336,-0.408053,-6.533274,7.183039,6.753208,-5.383966,-0.726409,-6.077354,1.335447,7.139531,7.178732,-1.750271,4.475263,0.853458,-9.949425,-2.274550,4.553853,6.212896,9.763255,-9.896952,-9.452988,3.006844,7.675275,-4.340128,8.431859,8.427134,4.854064,1.778406,-9.954234,8.786289,5.502509,-4.166701,-2.075176,7.689465,-7.189563,-3.236304,-1.388902,8.799756,6.002996,0.524287,5.540696,-8.596033,-1.204158,-5.559641,-5.469484,2.551160,2.253047,-7.067910,-1.021169,8.514967,5.331806,9.826437,1.984652,4.732179,-9.968634,-8.496528,5.620573,-7.683203,-8.447999,6.499050,-3.646562,2.904253,-9.140997,1.634749,0.080049,0.315456,-8.351698,-4.815076,-8.140123,1.302265,-3.006719,-3.839466,-0.628930,8.737074,1.545125,2.281790,-5.097133,8.114376,-2.777174,7.812074,8.689495,8.762921,7.012965,-6.925760,2.886843,7.077578,1.060923,-3.489129,-9.402843,-8.086808,-7.847219,-6.928244,-8.315791,4.207859,-9.716723,-9.119623,9.557996,-1.744379,-7.326642,-4.856199,-7.522823,8.570246,-3.176351,7.418461,-6.341121,-3.696363,7.574496,7.479045,8.610823,-6.446686,5.418001,1.970855,-6.922937,1.824046,-0.428213,9.218030,6.100254,-5.545265,-8.398652,2.620578,-6.024383,7.498316,-2.980421,7.872162,1.873671,3.037204,9.043412,4.345006,-7.320864,-6.227918,3.928059,8.996209,-1.530132,-9.056954,6.993224,2.536098,6.329901,1.528179,4.725202,7.484487,5.840073,7.719906,-5.999375,-2.783420,-2.270778,7.247095,-4.537321,-8.514811,9.664121,5.407903,-4.639537,-1.741338,4.620643,1.045206,-8.431934,1.334761,-0.439562,-9.267991,-6.102394,2.120110,1.166230,-6.212268,-0.192198,7.996584,8.445538,-9.219299,7.492484,5.852396,3.384169,-3.432308,-9.320040,7.936927,-3.365977,0.102037,-7.641066,7.153212,6.859585,-3.216655,3.616959,8.579446,-7.654989,-9.514525,-4.124274,4.804259,7.019588,-0.666661,1.529658,-8.657109,9.207914,-3.365980,-3.397797,-4.562118,5.694898,6.799624,-7.288346,0.064520,2.367517,-3.046120,-5.656447,8.725223,7.101235,6.472756,5.664399,0.514918,5.320880,-5.486375,0.920249,6.268237,8.380304,4.373602,-8.958254,4.592250,8.913466,4.577997,0.940757,0.560979,-4.310369,0.363018,-8.449329,7.433900,6.901146,6.447549,-8.597219,4.470127,-3.036197,1.957300,-1.567320,-1.314115,-9.515110,8.658249,-9.444387,7.234184,6.290650,-6.890488,8.048713,3.521057,0.587470,1.961344,8.734363,-5.906943,-8.464983,-7.392542,-4.177938,-1.040079,7.568759,-7.301401,-3.788623,-0.481463,-2.338612,8.966800,-0.567969,-3.993571,6.119306,1.791965,2.608374,-7.949592,5.651483,-1.263427,5.513728,2.022181,-5.047380,-2.157415,7.104090,-8.216671,3.277917,7.063237,-2.885590,-8.739031,2.187962,-0.018947,2.706938,-4.642130,-6.405597,-6.816066,2.592590,-9.319097,7.235360,-4.321759,9.017847,-0.655757,-6.503159,5.982991,-9.092830,1.920526,4.511920,-4.999231,-7.739136,-9.477813,1.249206,7.445155,-7.868347,-3.734438,-7.404072,-7.585039,2.284614,0.572387,-0.360255,-5.509456,-4.657749,-9.770792,3.910547,-8.023029,-1.844968,-0.832492,4.055048,-6.291152,4.826955,0.554226,-3.681235,-2.160124,-7.465222,1.929275,-7.631593,6.036184,1.694370,-8.483392,-9.367070,5.970489,8.160841,-5.511103,2.909354,-3.485893,7.047242,-3.254280,8.140485,1.128906,-3.308876,-9.440906,-7.439492,6.846940,-4.019677,3.631140,-1.631691,5.192684,-5.834333,-8.313476,-2.400340,3.150950,-3.224436,9.484240,-2.096130,-1.338351,-0.500449,5.601278,-4.933350,-3.313846,-9.455797,-7.904088,-8.208075,8.525318,5.168979,-2.074865,-6.417857,-4.446227,-1.106581,8.969801,-2.922504,9.652046,-8.861645,-4.399665,-5.082900,1.187643,-8.747013,3.339281,7.810549,5.780705,9.804105,7.223751,4.128724,-9.825368,3.310054,-8.778509,5.277733,-6.020212,-8.118972,8.151525,-3.441525,-9.274270,-0.340650,1.497898,-3.313959,-3.040595,5.190016,4.182676,2.748441,-5.107746,2.110158,7.833606,-4.053185,2.813223,-9.227644,8.954244,2.865781,6.396464,-8.744287,-4.807099,5.220796,-4.393222,-8.800711,-8.778510,0.173124,-5.020392,6.942594,-8.151989,-0.828043,7.106695,-0.256515,2.409594,-2.316183,3.836111,1.387186,3.794940,-9.051458,5.392282,4.200691,4.305421,-0.539723,-0.646575,4.824413,-5.557775,-4.267612,-5.864078,-2.023292,-6.109034,-6.400225,0.690666,0.060464,-8.225592,-8.809056,-8.151549,1.327486,1.076899,-2.635550,-5.821897,-7.961432,0.870407,-8.335816,0.100396,6.877216,4.818012,3.220034,2.337952,9.866484,-4.856321,-9.877878,6.811888,-5.636736,5.978905,-1.563019,-5.165072,-7.625571,6.007883,4.598327,-5.825106,1.046401,-4.940759,-0.948557,6.284603,-7.379022,-3.203989,1.109870,-5.816153,-0.169134,-9.127327,0.792656,5.993541,-7.178426,-6.663402,5.871743,-9.648245,-6.047830,4.953913,-9.870037,-2.163592,-5.451967,0.811605,3.411550,-9.002487,-7.435734,-4.092394,4.578783,8.894681,9.232132,-5.650246,-5.048324,8.275467,9.779397,-6.176073,0.244116,-2.516892,0.571109,6.082264,-0.854726,-3.336453,-1.483939,-2.797530,-8.143549,7.293222,-2.701475,-6.305331,-7.545361,2.670168,-8.927622,-1.842125,1.523802,7.215900,-7.467738,8.333805,-8.702812,6.441870,-8.179195,8.043548,-2.107533,-2.399480,-7.193272,1.957605,-0.203528,-9.762364,-6.329008,0.086027,-5.854989,-6.267445,4.623261,7.034667,1.220166,9.249304,-5.648207,-1.197058,8.581801,4.577079,8.419942,1.552258,-5.954033,-8.659071,-6.289216,-2.161796,9.508484,7.174382,-7.146761,-2.421740,-5.335340,3.531385,-3.374599,5.902758,4.845092,3.666187,7.259010,-2.653808,4.723461,9.427405,-7.338535,-1.157464,-1.764694,5.052128,-8.165140,4.762806,7.211996,9.336546,-4.008102,0.375048,-3.371505,0.257715,9.692758,1.478991,-7.229396,-8.510747,-8.352913,-6.082726,8.473878,1.395492,-8.235942,-8.735313,7.413427,2.684511,-7.952632,4.558865,-4.887463,-0.242904,2.523551,-2.525151,-4.945817,-4.423268,4.243883,-4.018111,-0.996921,-7.679699,-6.766128,-0.402085,-7.191351,4.742539,6.869456,4.101637,5.725110,7.176230,9.258947,7.408132,9.958110,-2.616031,-8.646381,5.558151,-8.626695,1.349120,-0.663833,4.963766,-2.290059,1.905979,7.972312,0.258258,-0.350984,8.155828,-2.298935,-5.589064,1.577705,-2.685970,5.758651,-9.242910,8.402908,-8.970141,-7.156473,-3.407924,-7.928728,-6.511862,4.159775,4.037634,-8.824031,6.278428,6.314417,-4.407594,3.979153,-9.454592,-5.018564,-8.325802,8.966578,2.327450,-7.123329,-6.834464,4.951866,2.190327,-5.371541,3.714967,2.161826,8.858110,-0.500143,9.167583,-3.259788,-2.770975,5.422230,-6.238473,6.531296,-9.404687,0.355512,-1.973160,7.593081,7.225020,-5.563865,-1.762761,-9.692326,-5.461338,-5.503475,-8.764498,-8.506994,5.024659,0.099912,-0.719180,-5.602531,0.217032,9.180855,-8.583090,1.585609,-7.562793,-9.746960,1.151800,-3.379058,0.848889,-1.617753,1.930054,-8.656310,-2.372112,-1.244454,-5.218004,3.400719,-7.910579,-6.453995,9.152476,1.540782,6.209553,-1.385394,-9.071175,0.094937,2.197219,2.680769,-7.972043,-4.215030,5.921668,0.293322,0.356219,8.494629,2.954976,-3.416372,6.841186,-0.851136,-5.297865,-0.407593,6.597894,-0.253254,5.151408,3.406791,-2.621463,-2.205649,-2.243623,3.547674,-8.108125,2.993749,-6.284334,-8.556799,3.682481,8.600065,1.268112,-4.168819,1.222367,-5.630684,-5.749505,-1.061747,7.868235,1.984723,-2.582841,0.269173,4.955428,-4.088334,-7.250965,-2.197812,2.565854,0.068896,5.632516,1.909253,0.393887,8.855960,5.860714,-4.862979,-0.299576,-0.146770,-5.374910,9.937856,-4.797393,-2.322941,-9.497530,4.778512,-9.727668,-7.037666,-4.878910,-3.400703,0.327677,-9.132094,9.850753,0.754206,-8.973250,-1.664936,2.266516,-2.021449,0.163251,0.510460,0.886602,6.549673,0.776854,6.619895,3.108515,7.729195,6.686175,7.263511,-8.672108,-5.235525,-0.344169,-8.325671,-0.800264,6.372783,4.908113,9.309761,1.586836,-6.275225,9.744705,6.768606,7.811094,6.631650,-8.548333,8.931047,-4.386141,2.784901,-4.242993,-8.156997,-9.855232,-6.156379,-3.128905,7.924956,-6.471509,0.009489,3.600424,-4.378851,9.671383,-8.614646,-2.086234,1.526411,0.874600,4.504498,-2.731746,6.374067,3.191329,-5.419694,1.511962,-5.499341,7.440551,2.291118,-7.990785,6.721534,-4.378523,8.597763,8.322765,1.306711,0.549926,-5.477016,-6.700215,-8.793839,4.140525,-7.855779,-5.178094,-8.036457,-5.449036,3.317741,5.272834,-6.537910,-3.790133,-2.265885,-8.744727,-5.415086,-6.955916,3.603808,-7.562488,-2.286548,-4.292893,1.141696,9.953971,-8.499659,5.408501,-0.615505,-5.811756,-9.793847,-5.320552,-2.813191,-2.067646,-9.460211,0.060567,-9.384880,-3.612781,7.790894,6.312738,1.411943,-0.005933,-1.330148,7.806350,-5.747175,4.533067,-3.479101,0.849941,6.180122,-5.127885,-6.687214,2.483465,4.023268,-8.063331,5.729922,2.010755,-4.426012,-0.602700,-9.787094,-8.292907,-2.238560,4.349686,0.742914,8.021165,5.334563,6.165746,-3.506101,-0.928969,-8.472863,-4.335441,-9.526657,-1.753264,-4.603379,1.071729,8.981392,7.435756,2.287174,-1.335533,-4.612551,6.566614,0.542876,8.604073,-0.531506,-6.575780,-1.006116,-2.506329,-4.730265,-3.802604,7.483985,7.195180,9.510159,-0.297667,-0.099766,7.880230,3.755783,-5.202308,9.982908,-7.177132,5.447240,-2.279683,9.003431], dtype = "float64")#candidate|5547|(1078,)|const|float64
call_5546 = relay.TupleGetItem(func_4805_call(relay.reshape(const_5547.astype('float64'), [7, 14, 11])), 1)
call_5548 = relay.TupleGetItem(func_4808_call(relay.reshape(const_5547.astype('float64'), [7, 14, 11])), 1)
func_4634_call = mod.get_global_var('func_4634')
func_4635_call = mutated_mod.get_global_var('func_4635')
call_5549 = relay.TupleGetItem(func_4634_call(), 0)
call_5550 = relay.TupleGetItem(func_4635_call(), 0)
uop_5559 = relay.atanh(const_5547.astype('float64')) # shape=(1078,)
func_2171_call = mod.get_global_var('func_2171')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_5571 = relay.TupleGetItem(func_2171_call(), 0)
call_5572 = relay.TupleGetItem(func_2173_call(), 0)
uop_5574 = relay.log(const_5547.astype('float64')) # shape=(1078,)
func_5089_call = mod.get_global_var('func_5089')
func_5091_call = mutated_mod.get_global_var('func_5091')
call_5577 = relay.TupleGetItem(func_5089_call(), 0)
call_5578 = relay.TupleGetItem(func_5091_call(), 0)
bop_5584 = relay.power(uop_5574.astype('float32'), relay.reshape(const_5547.astype('float32'), relay.shape_of(uop_5574))) # shape=(1078,)
uop_5595 = relay.tan(uop_5574.astype('float64')) # shape=(1078,)
func_4134_call = mod.get_global_var('func_4134')
func_4137_call = mutated_mod.get_global_var('func_4137')
const_5603 = relay.const([8,-4,-6,-5,8,5,-6,2,-9,-10,-10,-6,8,-1,8,9,-6,4,-1,-9,7,-6,-8,-6,7,-4,3,-9,-9,-9,10,3,-10,6,-10,-2,-2,-9,-7,1,-10,-10,7,5,-2,5,2,-6,6,6,10,4,-6,-4,9,8,-2,-4,10,5,6,3,-9,-4,10,3,-10,4,2,-1,-5,2,-1,-6,-8,2,2,-3,4,-6,-7,-6,7,-5,10,-10,6,2,-8,8,-1,1,-8,6,2,-6,-10,8,-4,6,10,1,-8,5,3,-4,-6,10,9,-3,8,4,6,7,6,4,-1,-3,-7,-5,-2,7,-5,-9,2,7,-3,-10,-2,9,-2,3,-9,2,-3,-8,-7,-2,-1,7], dtype = "int16")#candidate|5603|(140,)|const|int16
call_5602 = func_4134_call(relay.reshape(const_5603.astype('int16'), [2, 10, 7]))
call_5604 = func_4134_call(relay.reshape(const_5603.astype('int16'), [2, 10, 7]))
func_4385_call = mod.get_global_var('func_4385')
func_4388_call = mutated_mod.get_global_var('func_4388')
var_5607 = relay.var("var_5607", dtype = "float32", shape = (16,))#candidate|5607|(16,)|var|float32
call_5606 = relay.TupleGetItem(func_4385_call(relay.reshape(var_5607.astype('float32'), [16,])), 3)
call_5608 = relay.TupleGetItem(func_4388_call(relay.reshape(var_5607.astype('float32'), [16,])), 3)
uop_5612 = relay.rsqrt(uop_5574.astype('float32')) # shape=(1078,)
func_5515_call = mod.get_global_var('func_5515')
func_5516_call = mutated_mod.get_global_var('func_5516')
call_5615 = relay.TupleGetItem(func_5515_call(), 0)
call_5616 = relay.TupleGetItem(func_5516_call(), 0)
var_5620 = relay.var("var_5620", dtype = "float32", shape = (1078,))#candidate|5620|(1078,)|var|float32
bop_5621 = relay.floor_divide(bop_5584.astype('float32'), relay.reshape(var_5620.astype('float32'), relay.shape_of(bop_5584))) # shape=(1078,)
bop_5639 = relay.divide(uop_5612.astype('float64'), relay.reshape(uop_5559.astype('float64'), relay.shape_of(uop_5612))) # shape=(1078,)
output = relay.Tuple([call_5533,call_5546,call_5549,call_5571,call_5577,uop_5595,call_5602,const_5603,call_5606,var_5607,call_5615,bop_5621,bop_5639,])
output2 = relay.Tuple([call_5534,call_5548,call_5550,call_5572,call_5578,uop_5595,call_5604,const_5603,call_5608,var_5607,call_5616,bop_5621,bop_5639,])
func_5655 = relay.Function([var_5607,var_5620,], output)
mod['func_5655'] = func_5655
mod = relay.transform.InferType()(mod)
mutated_mod['func_5655'] = func_5655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5655_call = mutated_mod.get_global_var('func_5655')
var_5657 = relay.var("var_5657", dtype = "float32", shape = (16,))#candidate|5657|(16,)|var|float32
var_5658 = relay.var("var_5658", dtype = "float32", shape = (1078,))#candidate|5658|(1078,)|var|float32
call_5656 = func_5655_call(var_5657,var_5658,)
output = call_5656
func_5659 = relay.Function([var_5657,var_5658,], output)
mutated_mod['func_5659'] = func_5659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2929_call = mod.get_global_var('func_2929')
func_2930_call = mutated_mod.get_global_var('func_2930')
call_5678 = relay.TupleGetItem(func_2929_call(), 2)
call_5679 = relay.TupleGetItem(func_2930_call(), 2)
func_4385_call = mod.get_global_var('func_4385')
func_4388_call = mutated_mod.get_global_var('func_4388')
var_5696 = relay.var("var_5696", dtype = "float32", shape = (16,))#candidate|5696|(16,)|var|float32
call_5695 = relay.TupleGetItem(func_4385_call(relay.reshape(var_5696.astype('float32'), [16,])), 1)
call_5697 = relay.TupleGetItem(func_4388_call(relay.reshape(var_5696.astype('float32'), [16,])), 1)
output = relay.Tuple([call_5678,call_5695,var_5696,])
output2 = relay.Tuple([call_5679,call_5697,var_5696,])
func_5711 = relay.Function([var_5696,], output)
mod['func_5711'] = func_5711
mod = relay.transform.InferType()(mod)
mutated_mod['func_5711'] = func_5711
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5712 = relay.var("var_5712", dtype = "float32", shape = (16,))#candidate|5712|(16,)|var|float32
func_5711_call = mutated_mod.get_global_var('func_5711')
call_5713 = func_5711_call(var_5712)
output = call_5713
func_5714 = relay.Function([var_5712], output)
mutated_mod['func_5714'] = func_5714
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2929_call = mod.get_global_var('func_2929')
func_2930_call = mutated_mod.get_global_var('func_2930')
call_5754 = relay.TupleGetItem(func_2929_call(), 1)
call_5755 = relay.TupleGetItem(func_2930_call(), 1)
func_2171_call = mod.get_global_var('func_2171')
func_2173_call = mutated_mod.get_global_var('func_2173')
call_5756 = relay.TupleGetItem(func_2171_call(), 0)
call_5757 = relay.TupleGetItem(func_2173_call(), 0)
bop_5777 = relay.greater_equal(call_5754.astype('bool'), call_5756.astype('bool')) # shape=(1, 15, 5)
bop_5780 = relay.greater_equal(call_5755.astype('bool'), call_5757.astype('bool')) # shape=(1, 15, 5)
func_5711_call = mod.get_global_var('func_5711')
func_5714_call = mutated_mod.get_global_var('func_5714')
var_5783 = relay.var("var_5783", dtype = "float32", shape = (4, 4))#candidate|5783|(4, 4)|var|float32
call_5782 = relay.TupleGetItem(func_5711_call(relay.reshape(var_5783.astype('float32'), [16,])), 0)
call_5784 = relay.TupleGetItem(func_5714_call(relay.reshape(var_5783.astype('float32'), [16,])), 0)
func_4114_call = mod.get_global_var('func_4114')
func_4116_call = mutated_mod.get_global_var('func_4116')
call_5789 = relay.TupleGetItem(func_4114_call(), 1)
call_5790 = relay.TupleGetItem(func_4116_call(), 1)
output = relay.Tuple([bop_5777,call_5782,var_5783,call_5789,])
output2 = relay.Tuple([bop_5780,call_5784,var_5783,call_5790,])
func_5791 = relay.Function([var_5783,], output)
mod['func_5791'] = func_5791
mod = relay.transform.InferType()(mod)
mutated_mod['func_5791'] = func_5791
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5792 = relay.var("var_5792", dtype = "float32", shape = (4, 4))#candidate|5792|(4, 4)|var|float32
func_5791_call = mutated_mod.get_global_var('func_5791')
call_5793 = func_5791_call(var_5792)
output = call_5793
func_5794 = relay.Function([var_5792], output)
mutated_mod['func_5794'] = func_5794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5515_call = mod.get_global_var('func_5515')
func_5516_call = mutated_mod.get_global_var('func_5516')
call_5935 = relay.TupleGetItem(func_5515_call(), 0)
call_5936 = relay.TupleGetItem(func_5516_call(), 0)
output = call_5935
output2 = call_5936
func_5951 = relay.Function([], output)
mod['func_5951'] = func_5951
mod = relay.transform.InferType()(mod)
mutated_mod['func_5951'] = func_5951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5951_call = mutated_mod.get_global_var('func_5951')
call_5952 = func_5951_call()
output = call_5952
func_5953 = relay.Function([], output)
mutated_mod['func_5953'] = func_5953
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1931_call = mod.get_global_var('func_1931')
func_1932_call = mutated_mod.get_global_var('func_1932')
call_5954 = relay.TupleGetItem(func_1931_call(), 2)
call_5955 = relay.TupleGetItem(func_1932_call(), 2)
var_5956 = relay.var("var_5956", dtype = "float32", shape = (567,))#candidate|5956|(567,)|var|float32
bop_5957 = relay.mod(call_5954.astype('float32'), relay.reshape(var_5956.astype('float32'), relay.shape_of(call_5954))) # shape=(567,)
bop_5960 = relay.mod(call_5955.astype('float32'), relay.reshape(var_5956.astype('float32'), relay.shape_of(call_5955))) # shape=(567,)
output = relay.Tuple([bop_5957,])
output2 = relay.Tuple([bop_5960,])
func_5964 = relay.Function([var_5956,], output)
mod['func_5964'] = func_5964
mod = relay.transform.InferType()(mod)
var_5965 = relay.var("var_5965", dtype = "float32", shape = (567,))#candidate|5965|(567,)|var|float32
output = func_5964(var_5965)
func_5966 = relay.Function([var_5965], output)
mutated_mod['func_5966'] = func_5966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_5971 = relay.TupleGetItem(func_4761_call(), 2)
call_5972 = relay.TupleGetItem(func_4762_call(), 2)
func_4554_call = mod.get_global_var('func_4554')
func_4555_call = mutated_mod.get_global_var('func_4555')
call_5973 = relay.TupleGetItem(func_4554_call(), 2)
call_5974 = relay.TupleGetItem(func_4555_call(), 2)
output = relay.Tuple([call_5971,call_5973,])
output2 = relay.Tuple([call_5972,call_5974,])
func_5986 = relay.Function([], output)
mod['func_5986'] = func_5986
mod = relay.transform.InferType()(mod)
output = func_5986()
func_5987 = relay.Function([], output)
mutated_mod['func_5987'] = func_5987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_6002 = relay.TupleGetItem(func_4398_call(), 0)
call_6003 = relay.TupleGetItem(func_4399_call(), 0)
func_5000_call = mod.get_global_var('func_5000')
func_5003_call = mutated_mod.get_global_var('func_5003')
const_6016 = relay.const([-8,-1,3,-7,-4,5,-10,-2,-4,9,-8,6,-6,7,2,5,7,2,-1,10,-5,-5,-2,9,-5,8,1,-1,2,2,-4,-5,-2,-2,-9,-10,-9,-7,-2,-7,-9,2,8,6,1,-5,4,7,8,-2,-4,-1,-7,-6,-7,6,5,-5,-9,-2,-8,5,-6,9,-4,10,3,-2,10,-7,-10,-2,-9,7,-7,-10,5,-6,-2,4,-5,-3,-8,7,5,-4,7,10,-4,-5,6,-5,-5,-2,5,10,-2,6,-9,5,-7,9,-6,1,7,-10,-3,6,5,2,5,10,6,5,-1,1,3,3,10,1,7,-2,8,8,-5,-7,-4,-8,-3,8,-7,-3,1,-2,-7,10,-6,-6,-10,2,-7,-6,6,-3,-8,4,-2,-8,2,-5,2,-4,-8,5,-7,5,-5,-4,6,-1,-10,2,1,-4,9,-1,5,-1,8,-2,4,8,8,-2,1,1,-8,1,2,-4,7,3,-3,-6,2,-5,-7,8,6,10,-5,7,3,-5,-5,7,6,-5,-4,-9,1,3,-10,-3,-4,4,-3,7,2,2,-10,-1,-1,-5,-7,1,2,-8,-8,-9,-4,-4,-5,-7,-2,4,10,-10,10,-5,-2,7,-10,-6,-3,-1,-5,6,-5,-7,-3,-10,-4,3,-6,3,5,-1,4,-5,10,6,2,-7,6,-5,5,-2,-4,3,5,7,5,-7,5,5,-10,3,4,9,6,-1,-9,-9,9,-2,-9,4,-7,10,3,-9,8,-4,-6,4,-9,2,-7,-1,-5,1,-2,-8,8,-2,5,5,-5,-6,4,-2,5,10,-7,8,-4,7,-8,6,3,8,-1,-1,-3,-7,9,1,5,5,2,5,-6,3,-5,1,-9,8,-3,-8,8,-5,-7,2,-8,6,-4,-8,-3,-6,4,-8,8,4,-5,-10,-8,-3,-1,-6,3,1,-3,8,3,-6,-1,9,2,-1,-6,3,5,-6,10,7,4,-9,-10,6,-2,10,9,-1,3,-2,-4,-2,1,-5,-1,-2,-2,-3,9,6,2,-5,5,5,-9,-6,2,-1,-5,-3,1,-1,-8,5,-6,1,7,2,-3,10,4,4,-6,-10,-3,9,-10,-7,7,-8,-5,2,6,-3,-10,10,3,-3,-10,1,-8,7,9,8,10,-8,6,8,-3,-10,6,-7,3,9,3,-9,8,-10,-2,4,6,-6,1,6,-6,7,4,2,-5,3,9,-10,-7,-4,1,-10,2,-1,1,9,2,1,1,5,6,-6,1,-2,8,-9,7,-6,-7,-2,-2,8,-6,-2,-4,-4,9,5,-6,8,6,3,-7,10,5,4,2,5,-5,-6,-6,-1,-10,2,-5,2,-8,-7,-3,10,-1,-7,-8,-1,-9,-4,-7,7,1,-3,-2,10,-9,8,5,10,-4,-9,1,-7,-8,5,-4,-3,6,1,-1,9,-9,-2], dtype = "uint16")#candidate|6016|(540,)|const|uint16
call_6015 = relay.TupleGetItem(func_5000_call(relay.reshape(const_6016.astype('uint16'), [10, 6, 9]), relay.reshape(const_6016.astype('uint16'), [10, 6, 9]), ), 0)
call_6017 = relay.TupleGetItem(func_5003_call(relay.reshape(const_6016.astype('uint16'), [10, 6, 9]), relay.reshape(const_6016.astype('uint16'), [10, 6, 9]), ), 0)
output = relay.Tuple([call_6002,call_6015,const_6016,])
output2 = relay.Tuple([call_6003,call_6017,const_6016,])
func_6023 = relay.Function([], output)
mod['func_6023'] = func_6023
mod = relay.transform.InferType()(mod)
output = func_6023()
func_6024 = relay.Function([], output)
mutated_mod['func_6024'] = func_6024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3305_call = mod.get_global_var('func_3305')
func_3306_call = mutated_mod.get_global_var('func_3306')
call_6141 = func_3305_call()
call_6142 = func_3305_call()
func_3414_call = mod.get_global_var('func_3414')
func_3415_call = mutated_mod.get_global_var('func_3415')
call_6153 = relay.TupleGetItem(func_3414_call(), 0)
call_6154 = relay.TupleGetItem(func_3415_call(), 0)
func_5951_call = mod.get_global_var('func_5951')
func_5953_call = mutated_mod.get_global_var('func_5953')
call_6163 = func_5951_call()
call_6164 = func_5951_call()
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_6165 = func_1140_call()
call_6166 = func_1140_call()
output = relay.Tuple([call_6141,call_6153,call_6163,call_6165,])
output2 = relay.Tuple([call_6142,call_6154,call_6164,call_6166,])
func_6175 = relay.Function([], output)
mod['func_6175'] = func_6175
mod = relay.transform.InferType()(mod)
mutated_mod['func_6175'] = func_6175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6175_call = mutated_mod.get_global_var('func_6175')
call_6176 = func_6175_call()
output = call_6176
func_6177 = relay.Function([], output)
mutated_mod['func_6177'] = func_6177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5986_call = mod.get_global_var('func_5986')
func_5987_call = mutated_mod.get_global_var('func_5987')
call_6235 = relay.TupleGetItem(func_5986_call(), 0)
call_6236 = relay.TupleGetItem(func_5987_call(), 0)
func_1650_call = mod.get_global_var('func_1650')
func_1652_call = mutated_mod.get_global_var('func_1652')
var_6247 = relay.var("var_6247", dtype = "float64", shape = (20,))#candidate|6247|(20,)|var|float64
call_6246 = relay.TupleGetItem(func_1650_call(relay.reshape(var_6247.astype('float64'), [4, 1, 5])), 0)
call_6248 = relay.TupleGetItem(func_1652_call(relay.reshape(var_6247.astype('float64'), [4, 1, 5])), 0)
output = relay.Tuple([call_6235,call_6246,var_6247,])
output2 = relay.Tuple([call_6236,call_6248,var_6247,])
func_6249 = relay.Function([var_6247,], output)
mod['func_6249'] = func_6249
mod = relay.transform.InferType()(mod)
var_6250 = relay.var("var_6250", dtype = "float64", shape = (20,))#candidate|6250|(20,)|var|float64
output = func_6249(var_6250)
func_6251 = relay.Function([var_6250], output)
mutated_mod['func_6251'] = func_6251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3267_call = mod.get_global_var('func_3267')
func_3268_call = mutated_mod.get_global_var('func_3268')
call_6280 = relay.TupleGetItem(func_3267_call(), 0)
call_6281 = relay.TupleGetItem(func_3268_call(), 0)
output = call_6280
output2 = call_6281
func_6287 = relay.Function([], output)
mod['func_6287'] = func_6287
mod = relay.transform.InferType()(mod)
mutated_mod['func_6287'] = func_6287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6287_call = mutated_mod.get_global_var('func_6287')
call_6288 = func_6287_call()
output = call_6288
func_6289 = relay.Function([], output)
mutated_mod['func_6289'] = func_6289
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3246_call = mod.get_global_var('func_3246')
func_3248_call = mutated_mod.get_global_var('func_3248')
call_6324 = relay.TupleGetItem(func_3246_call(), 2)
call_6325 = relay.TupleGetItem(func_3248_call(), 2)
output = call_6324
output2 = call_6325
func_6326 = relay.Function([], output)
mod['func_6326'] = func_6326
mod = relay.transform.InferType()(mod)
output = func_6326()
func_6327 = relay.Function([], output)
mutated_mod['func_6327'] = func_6327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3507_call = mod.get_global_var('func_3507')
func_3508_call = mutated_mod.get_global_var('func_3508')
call_6347 = relay.TupleGetItem(func_3507_call(), 0)
call_6348 = relay.TupleGetItem(func_3508_call(), 0)
output = call_6347
output2 = call_6348
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
var_6443 = relay.var("var_6443", dtype = "float64", shape = (4, 5, 2))#candidate|6443|(4, 5, 2)|var|float64
var_6444 = relay.var("var_6444", dtype = "float64", shape = (4, 5, 2))#candidate|6444|(4, 5, 2)|var|float64
bop_6445 = relay.power(var_6443.astype('float64'), relay.reshape(var_6444.astype('float64'), relay.shape_of(var_6443))) # shape=(4, 5, 2)
func_5655_call = mod.get_global_var('func_5655')
func_5659_call = mutated_mod.get_global_var('func_5659')
const_6450 = relay.const([2.965671,5.208207,0.038990,-9.637880,-5.666460,-3.865563,3.261959,1.550631,4.332876,8.085179,-9.584409,-0.043758,1.983093,-2.394553,6.921673,-3.836653], dtype = "float32")#candidate|6450|(16,)|const|float32
const_6451 = relay.const([9.299401,2.518167,3.364078,1.124784,5.508832,0.412484,-0.220645,-2.746578,7.509740,7.992138,-0.218451,-1.566745,8.318097,-6.796563,-8.631112,8.195657,2.783016,4.300707,-9.848134,9.614518,3.511093,-9.140006,9.212688,-5.257391,-1.167518,-9.784986,3.973750,-5.164750,3.158975,9.771087,-5.996264,-9.894181,-6.564397,-1.888231,-6.674485,-9.826509,-4.972232,8.451906,4.343548,-4.173270,8.533346,-4.241610,3.682245,9.480380,3.856199,-4.115936,1.169291,7.580692,-3.271353,-4.081644,-5.361626,6.771536,-0.899087,-5.736000,-0.338807,9.643076,5.254118,6.382782,-7.609284,-9.585021,6.525910,4.577608,0.594577,-1.011345,-4.875437,-8.434773,7.623612,7.160694,8.388118,5.225457,-0.434810,0.989491,-9.952864,0.586515,-8.500431,-2.794154,-0.346488,-7.940182,4.171015,-8.478065,-7.415765,-9.098045,-0.784968,5.205637,6.372703,4.533273,8.125520,-4.174596,9.081574,-8.379251,4.534742,-1.150666,-0.080540,6.589289,5.237820,5.889410,-8.179598,-0.935897,5.844893,-4.210293,-4.229124,-4.215239,5.710438,-9.845079,-2.381333,-7.563209,0.084029,-3.452901,1.024324,2.558419,3.747209,-1.514676,-2.600283,-1.566788,-3.245015,3.094498,-3.329493,-3.526475,-2.583687,2.652442,1.521652,-6.378690,-6.263984,-6.332255,-5.401479,-1.390929,-0.524383,8.248919,2.902838,-5.004194,7.573521,3.851272,-5.453308,1.908120,-2.352448,8.913625,-1.321634,-2.944011,-2.934036,-7.866224,9.899498,-0.908171,-9.805674,-0.818188,3.968922,9.005170,-3.086281,2.584517,2.615704,3.218168,8.485708,3.845477,-1.109311,-2.756256,7.246869,0.559434,7.702071,-9.080864,-5.737483,-3.441962,-1.938053,-2.942223,-5.093613,2.110947,-6.053663,2.609336,9.530150,6.138112,-7.118908,7.717678,-9.452647,-0.901555,-6.353182,0.528489,-0.784103,4.567907,-3.704284,7.934821,6.252722,-5.787298,-7.574033,6.823377,-8.373486,7.508269,-5.472885,-5.078016,-9.233566,-3.670430,-8.845916,3.146150,5.133849,4.446206,-9.763234,-4.076208,0.828418,0.118945,-4.115655,4.248646,4.163661,-9.474304,5.377093,-4.132037,1.434560,7.102196,3.146307,-6.159766,8.998906,-3.130393,4.407721,5.219177,7.299917,-4.235986,7.182124,-6.522382,-9.565059,-7.055625,-2.216648,4.658386,8.413351,6.032195,0.744607,-3.265873,4.818883,-4.101545,2.077104,3.652427,-5.109245,1.225768,3.336540,-1.635791,-2.133806,-5.131590,-2.655624,-0.776537,-3.830182,-6.655720,-3.526347,-4.421658,1.164162,-2.784061,-7.602051,5.171709,4.085701,-9.574014,-7.981594,-8.618608,5.549512,7.921581,9.571387,9.936700,0.938810,6.693811,-6.620928,8.867748,7.548024,5.695845,7.162435,-5.682882,3.958107,-0.666898,-5.048115,-5.033971,6.788762,7.978230,5.106483,-9.547444,-8.987292,-8.392788,4.338431,-7.872714,3.744959,-9.435344,-8.142954,1.047005,3.903303,5.738755,2.854580,8.483503,-7.517264,4.383315,8.562751,-0.691740,3.197890,2.878590,0.225985,2.303350,1.394009,5.022579,2.063824,1.598706,-5.363443,-1.368120,-9.451228,-8.419395,-8.808062,-1.540587,3.130049,3.998477,-9.788866,8.411702,-1.028434,-6.238918,-4.649589,9.645230,6.804487,-2.565193,1.452652,9.583649,-5.970596,-5.595953,8.088654,9.607040,-5.812079,1.910924,9.545001,-9.539857,-0.865090,5.740909,-8.205601,-9.463195,2.854398,-5.258159,6.000939,-4.173170,3.337079,-8.750087,8.909529,-4.244719,-6.171906,-6.202001,-8.970077,8.860243,-3.349367,-5.015075,3.093802,-6.590549,7.185604,0.279274,-6.164626,9.388156,6.711988,-4.569635,8.523903,-6.438504,-4.829453,3.809856,4.856415,0.195317,9.106092,-6.376700,-1.589573,6.286155,5.851302,-0.598275,-1.695890,-7.211729,4.868120,-4.761184,0.327107,-6.919368,-5.290937,-3.160633,-8.229588,4.951503,7.155039,-3.552817,-4.311033,-9.292403,7.334810,7.609751,-5.948521,3.259931,-9.484635,-0.896449,-1.264320,2.255666,-6.801887,-3.724692,-8.779865,-3.988371,2.750621,3.695434,-2.070775,-1.232139,2.416224,8.854848,2.218213,6.335596,-3.078027,4.483349,0.632196,9.540579,-6.895642,-5.359788,2.688753,3.466582,-9.322903,-4.211457,-0.909996,-8.530017,-8.831300,7.802374,-4.525775,9.223179,-3.866326,8.434927,-2.175245,1.858215,-6.704992,4.276753,-6.025329,-9.763119,7.915441,8.399280,2.331033,3.627305,2.166959,7.550118,-8.454517,-6.627718,7.346692,-6.590682,0.772008,7.919695,7.733820,3.855539,4.215213,-0.339483,4.547725,-2.557039,8.049686,-9.466708,-4.659296,-9.570111,4.344377,5.855210,-0.527976,-8.305929,3.275600,7.443123,-4.575254,-6.435605,1.911251,-6.929828,-3.985056,5.249487,5.099685,-4.883379,-5.997799,-3.394962,6.257678,-9.325546,5.637645,3.934772,-0.281951,7.809534,-7.766743,-9.586917,8.024302,-0.699410,4.583730,7.043941,6.769900,-5.362152,7.662384,2.040933,-4.292548,-7.215715,-8.828728,-3.043911,7.251334,8.138696,7.029233,6.151064,5.370104,-9.216692,0.079266,6.554386,1.110912,-7.734211,-5.033828,-6.081767,-3.547143,-6.887597,-8.570375,8.828514,-3.066746,5.835437,8.479201,-6.443864,-8.103119,3.878212,1.435583,5.263918,6.714298,0.928712,5.397124,-8.566155,-6.807276,6.683196,-1.958447,-2.641754,0.894980,-4.601741,-8.769426,9.462284,-3.434894,0.395295,9.548177,-3.550670,-4.972518,-3.463791,8.148728,8.870448,0.495210,3.325858,-8.250281,3.528592,6.319984,-0.321575,-6.017397,0.273142,-4.841022,-9.291893,2.612968,-9.481553,-8.188529,8.856333,-3.830377,-8.083402,7.344495,7.697603,9.761496,-0.094735,-3.232346,3.079712,-5.218363,6.108835,0.996419,4.356573,2.988695,-0.240005,-9.307309,3.501405,0.759531,4.107366,0.695073,-9.658426,4.207459,-8.660221,3.059214,-3.678705,-8.133098,-7.244884,-5.416096,-6.858469,-0.477687,4.556572,-7.588026,5.295454,-6.289086,5.590536,4.421014,3.045735,-8.497567,-1.303480,3.617665,5.727238,3.887831,9.216194,8.378595,3.896859,-4.812248,2.939602,6.737001,-8.000452,0.916948,-1.990663,1.807942,2.867244,8.194099,7.584481,-3.178597,-6.585088,2.460773,7.853989,9.669012,-9.075235,-7.584194,-9.889636,-5.803904,9.816937,-6.301504,-4.676609,8.682493,1.097045,0.887409,1.699472,-2.212720,6.339784,2.168637,-6.680440,1.115728,9.824416,-4.167148,-3.856624,-5.198198,-7.006314,2.802251,7.521646,-1.830363,9.974896,6.878307,-4.366510,-2.267761,0.664951,-9.273380,-5.372413,-6.989696,3.579594,4.020895,6.862678,-0.486539,8.115798,-1.756701,-9.809767,0.154222,7.548192,8.267893,-4.184070,7.091837,4.918738,-7.113778,-8.692293,6.454580,1.105088,4.938462,7.399382,2.029340,6.601726,9.607821,-0.007311,8.014476,6.221640,0.207416,-3.893950,-4.700508,9.822873,8.781832,4.355886,3.594028,0.258493,-9.183350,-3.985898,7.687956,7.921720,-7.133103,-0.523580,8.597595,-4.278243,1.098415,-9.727344,-5.221051,-6.903305,7.132776,8.128313,5.115379,2.118581,9.059283,1.189336,7.747192,3.156850,-2.757025,1.044451,5.363147,4.560491,-5.192504,-2.768623,9.170092,-2.063274,2.773504,9.024448,-2.130087,-7.079118,2.977143,6.479502,-8.823557,-6.357075,-9.127124,4.541608,2.161525,-0.723210,-3.742104,-3.164261,-6.014929,-8.008245,-5.680771,-5.256681,-8.766319,-6.254448,-8.176699,-7.818795,-8.980813,5.508030,-2.693880,6.406627,9.628314,7.354625,-7.514272,7.990988,-7.759228,-1.018755,-8.346691,6.054243,5.831884,-3.598184,2.778167,7.981811,2.930408,-2.600337,5.591606,3.956663,-2.428386,-2.642791,-8.219719,0.129322,5.023516,-5.849460,-4.446825,-8.638776,5.382375,2.290175,9.597499,5.301491,2.919331,-7.077908,5.684815,-2.746819,-7.048511,-0.093510,-2.210109,7.450390,-5.849503,3.642100,2.826455,-2.717747,-8.513639,-9.100555,-5.733346,-5.735133,3.943302,-7.033136,-8.983707,-3.943857,8.172274,-5.784386,-3.726098,3.716682,8.977023,2.738160,-0.057252,8.189747,1.337002,-1.369401,3.184434,-0.925912,4.931374,4.930878,3.975822,-1.786043,5.082194,-5.317795,-8.171853,-5.965492,3.837954,0.794572,3.701004,-3.449656,-6.299616,4.125328,-3.585483,-9.976992,-6.411740,1.104110,-1.532274,0.711028,-2.405778,6.817948,8.779610,-4.096396,-0.393771,1.620297,3.614255,-5.749816,-3.603443,2.236780,7.565312,3.012973,-8.170654,6.874442,-2.182673,-2.807815,8.534563,-7.211473,4.712252,6.160473,-8.299851,2.313130,-3.798144,4.529492,0.892155,9.151765,-9.379490,3.060493,-8.285931,5.926018,1.406947,9.532417,-5.527994,7.069079,7.943178,8.047544,5.467882,8.294898,-9.292102,5.967834,5.267277,6.507437,2.423621,-4.655068,3.250549,-2.169980,2.933470,4.181610,4.439310,6.471021,8.081662,-3.053258,-9.395693,6.522309,-7.363909,-7.660134,2.225325,-0.843768,-8.551481,-1.113840,-2.524680,-1.757693,6.189602,9.296115,6.199445,1.288542,5.917104,8.194416,0.582500,4.828986,3.597085,4.169743,2.779881,1.670083,0.842131,8.152762,9.481504,6.208594,-5.556335,0.702157,-7.568001,-8.909633,6.470475,5.385072,-1.401274,-2.571752,-3.815000,7.484947,9.716556,-0.239036,-0.533490,7.458902,6.023498,-0.421964,2.891010,5.094493,-6.359474,-7.360309,-9.249731,-3.210332,-5.719170,-5.023857,0.898103,-2.864209,0.732956,0.159980,-8.563038,7.824810,6.192359,6.678140,9.312633,-8.890529,9.328215,7.675591,-2.731094,-9.404961,9.927651,-4.786518,-3.661067,5.990516,4.395439,-5.464029,8.526673,3.703648,2.083206,-0.059905,-8.364008,1.626071,8.826711,6.931028,-6.017631,-6.960817,-9.475394,-8.622671,6.554166,-1.748862,-0.668816,-8.597849,-3.734031,2.360304,4.374942,0.655460,-9.846401,2.042130,7.624302,-8.730454,-4.966456,5.466968,3.107566,-4.071079,-4.612147,9.449612,0.836463,-8.372694,9.615399,2.273727,0.076781,-7.736588,1.539160,4.641110,-1.151765,5.095613,-7.961307,-7.638530,-0.112952,-8.950212,0.765219,-1.308167,-7.627607,0.705264,-7.095131,-1.311677,6.620645,6.579567,-1.074346,1.035841,-6.927994,5.450969,-5.003460,-3.277526,-9.646411,4.855246,-2.085413,-0.157490,-3.610275,1.065337,7.860268,5.797862,-3.600257,1.328013,3.147955,-3.609987,8.591153,7.813354,4.933501,4.089248,-9.089726,4.988835,-6.463251,0.967975,8.637270,4.869409,-3.489658,8.383723,0.025617,7.747045,-6.666067,6.129988,-2.839128,9.364597,-3.828383,2.901971,7.619021,-7.926972,3.361575,-9.969222,-3.424637,8.934204,-6.744205,1.634411,9.894385,5.907710,-7.547277,-3.487874,5.185362,-2.872215,-9.158715,-8.611457,3.275297,0.390966,7.427329,8.607575,5.404875,-6.680769,-7.894680,0.334357,1.236899,4.351516,0.285863,-2.729712,4.749622,8.115392,-5.079698,4.649008,-4.878166,-9.644597,-3.173530,3.018520,-4.114371,-4.564407,8.331498,6.424291,-2.945446,0.752230,-3.230982,-4.263633,-5.179256,5.216734,9.097031,-4.857401,8.688030,3.560771,0.528208,5.740578,5.027282,-4.459549,9.524373,9.933258,-3.898908,-8.307785,-9.429059,-8.653105,-7.311097,0.283003,-3.519528,0.215407,6.081196,3.341000,0.719819,-4.761656,-3.235406,3.633878,-6.575846,0.955149,0.170297,7.422510,-8.303814,6.547248,7.817030,8.501724,-2.967562,0.724712], dtype = "float32")#candidate|6451|(1078,)|const|float32
call_6449 = relay.TupleGetItem(func_5655_call(relay.reshape(const_6450.astype('float32'), [16,]), relay.reshape(const_6451.astype('float32'), [1078,]), ), 5)
call_6452 = relay.TupleGetItem(func_5659_call(relay.reshape(const_6450.astype('float32'), [16,]), relay.reshape(const_6451.astype('float32'), [1078,]), ), 5)
output = relay.Tuple([bop_6445,call_6449,const_6450,const_6451,])
output2 = relay.Tuple([bop_6445,call_6452,const_6450,const_6451,])
func_6457 = relay.Function([var_6443,var_6444,], output)
mod['func_6457'] = func_6457
mod = relay.transform.InferType()(mod)
var_6458 = relay.var("var_6458", dtype = "float64", shape = (4, 5, 2))#candidate|6458|(4, 5, 2)|var|float64
var_6459 = relay.var("var_6459", dtype = "float64", shape = (4, 5, 2))#candidate|6459|(4, 5, 2)|var|float64
output = func_6457(var_6458,var_6459,)
func_6460 = relay.Function([var_6458,var_6459,], output)
mutated_mod['func_6460'] = func_6460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_6478 = relay.TupleGetItem(func_4761_call(), 1)
call_6479 = relay.TupleGetItem(func_4762_call(), 1)
output = call_6478
output2 = call_6479
func_6484 = relay.Function([], output)
mod['func_6484'] = func_6484
mod = relay.transform.InferType()(mod)
mutated_mod['func_6484'] = func_6484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6484_call = mutated_mod.get_global_var('func_6484')
call_6485 = func_6484_call()
output = call_6485
func_6486 = relay.Function([], output)
mutated_mod['func_6486'] = func_6486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5200_call = mod.get_global_var('func_5200')
func_5202_call = mutated_mod.get_global_var('func_5202')
call_6519 = relay.TupleGetItem(func_5200_call(), 0)
call_6520 = relay.TupleGetItem(func_5202_call(), 0)
output = call_6519
output2 = call_6520
func_6528 = relay.Function([], output)
mod['func_6528'] = func_6528
mod = relay.transform.InferType()(mod)
output = func_6528()
func_6529 = relay.Function([], output)
mutated_mod['func_6529'] = func_6529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1140_call = mod.get_global_var('func_1140')
func_1141_call = mutated_mod.get_global_var('func_1141')
call_6538 = func_1140_call()
call_6539 = func_1140_call()
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_6553 = relay.TupleGetItem(func_4250_call(), 1)
call_6554 = relay.TupleGetItem(func_4252_call(), 1)
output = relay.Tuple([call_6538,call_6553,])
output2 = relay.Tuple([call_6539,call_6554,])
func_6562 = relay.Function([], output)
mod['func_6562'] = func_6562
mod = relay.transform.InferType()(mod)
output = func_6562()
func_6563 = relay.Function([], output)
mutated_mod['func_6563'] = func_6563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_893_call = mod.get_global_var('func_893')
func_894_call = mutated_mod.get_global_var('func_894')
call_6638 = relay.TupleGetItem(func_893_call(), 0)
call_6639 = relay.TupleGetItem(func_894_call(), 0)
func_2929_call = mod.get_global_var('func_2929')
func_2930_call = mutated_mod.get_global_var('func_2930')
call_6657 = relay.TupleGetItem(func_2929_call(), 1)
call_6658 = relay.TupleGetItem(func_2930_call(), 1)
func_4385_call = mod.get_global_var('func_4385')
func_4388_call = mutated_mod.get_global_var('func_4388')
const_6668 = relay.const([[-4.084693,6.969936,4.621427,-9.559861,2.441805,6.701345,2.513819,-9.509663],[4.704629,8.919269,-9.148668,9.236117,7.369966,-7.582723,-6.657356,3.068115]], dtype = "float32")#candidate|6668|(2, 8)|const|float32
call_6667 = relay.TupleGetItem(func_4385_call(relay.reshape(const_6668.astype('float32'), [16,])), 2)
call_6669 = relay.TupleGetItem(func_4388_call(relay.reshape(const_6668.astype('float32'), [16,])), 2)
output = relay.Tuple([call_6638,call_6657,call_6667,const_6668,])
output2 = relay.Tuple([call_6639,call_6658,call_6669,const_6668,])
func_6672 = relay.Function([], output)
mod['func_6672'] = func_6672
mod = relay.transform.InferType()(mod)
mutated_mod['func_6672'] = func_6672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6672_call = mutated_mod.get_global_var('func_6672')
call_6673 = func_6672_call()
output = call_6673
func_6674 = relay.Function([], output)
mutated_mod['func_6674'] = func_6674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_6707 = relay.TupleGetItem(func_4761_call(), 2)
call_6708 = relay.TupleGetItem(func_4762_call(), 2)
func_5492_call = mod.get_global_var('func_5492')
func_5494_call = mutated_mod.get_global_var('func_5494')
var_6716 = relay.var("var_6716", dtype = "float32", shape = (567,))#candidate|6716|(567,)|var|float32
call_6715 = relay.TupleGetItem(func_5492_call(relay.reshape(var_6716.astype('float32'), [9, 63])), 0)
call_6717 = relay.TupleGetItem(func_5494_call(relay.reshape(var_6716.astype('float32'), [9, 63])), 0)
output = relay.Tuple([call_6707,call_6715,var_6716,])
output2 = relay.Tuple([call_6708,call_6717,var_6716,])
func_6726 = relay.Function([var_6716,], output)
mod['func_6726'] = func_6726
mod = relay.transform.InferType()(mod)
var_6727 = relay.var("var_6727", dtype = "float32", shape = (567,))#candidate|6727|(567,)|var|float32
output = func_6726(var_6727)
func_6728 = relay.Function([var_6727], output)
mutated_mod['func_6728'] = func_6728
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6732 = relay.var("var_6732", dtype = "float32", shape = (13, 8, 14))#candidate|6732|(13, 8, 14)|var|float32
uop_6733 = relay.cos(var_6732.astype('float32')) # shape=(13, 8, 14)
output = relay.Tuple([uop_6733,])
output2 = relay.Tuple([uop_6733,])
func_6736 = relay.Function([var_6732,], output)
mod['func_6736'] = func_6736
mod = relay.transform.InferType()(mod)
mutated_mod['func_6736'] = func_6736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6737 = relay.var("var_6737", dtype = "float32", shape = (13, 8, 14))#candidate|6737|(13, 8, 14)|var|float32
func_6736_call = mutated_mod.get_global_var('func_6736')
call_6738 = func_6736_call(var_6737)
output = call_6738
func_6739 = relay.Function([var_6737], output)
mutated_mod['func_6739'] = func_6739
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6795 = relay.var("var_6795", dtype = "bool", shape = (11, 14, 15))#candidate|6795|(11, 14, 15)|var|bool
var_6796 = relay.var("var_6796", dtype = "bool", shape = (11, 14, 15))#candidate|6796|(11, 14, 15)|var|bool
bop_6797 = relay.logical_and(var_6795.astype('bool'), relay.reshape(var_6796.astype('bool'), relay.shape_of(var_6795))) # shape=(11, 14, 15)
uop_6800 = relay.acos(var_6796.astype('float32')) # shape=(11, 14, 15)
uop_6806 = relay.erf(uop_6800.astype('float64')) # shape=(11, 14, 15)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_6814 = func_1779_call()
call_6815 = func_1779_call()
var_6832 = relay.var("var_6832", dtype = "bool", shape = (11, 14, 15))#candidate|6832|(11, 14, 15)|var|bool
bop_6833 = relay.minimum(bop_6797.astype('int64'), relay.reshape(var_6832.astype('int64'), relay.shape_of(bop_6797))) # shape=(11, 14, 15)
bop_6837 = relay.less_equal(uop_6806.astype('bool'), relay.reshape(bop_6833.astype('bool'), relay.shape_of(uop_6806))) # shape=(11, 14, 15)
bop_6849 = relay.logical_or(uop_6800.astype('bool'), relay.reshape(bop_6797.astype('bool'), relay.shape_of(uop_6800))) # shape=(11, 14, 15)
output = relay.Tuple([call_6814,bop_6837,bop_6849,])
output2 = relay.Tuple([call_6815,bop_6837,bop_6849,])
func_6855 = relay.Function([var_6795,var_6796,var_6832,], output)
mod['func_6855'] = func_6855
mod = relay.transform.InferType()(mod)
mutated_mod['func_6855'] = func_6855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6855_call = mutated_mod.get_global_var('func_6855')
var_6857 = relay.var("var_6857", dtype = "bool", shape = (11, 14, 15))#candidate|6857|(11, 14, 15)|var|bool
var_6858 = relay.var("var_6858", dtype = "bool", shape = (11, 14, 15))#candidate|6858|(11, 14, 15)|var|bool
var_6859 = relay.var("var_6859", dtype = "bool", shape = (11, 14, 15))#candidate|6859|(11, 14, 15)|var|bool
call_6856 = func_6855_call(var_6857,var_6858,var_6859,)
output = call_6856
func_6860 = relay.Function([var_6857,var_6858,var_6859,], output)
mutated_mod['func_6860'] = func_6860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6866 = relay.var("var_6866", dtype = "float64", shape = (15, 4, 12))#candidate|6866|(15, 4, 12)|var|float64
uop_6867 = relay.cosh(var_6866.astype('float64')) # shape=(15, 4, 12)
output = relay.Tuple([uop_6867,])
output2 = relay.Tuple([uop_6867,])
func_6896 = relay.Function([var_6866,], output)
mod['func_6896'] = func_6896
mod = relay.transform.InferType()(mod)
var_6897 = relay.var("var_6897", dtype = "float64", shape = (15, 4, 12))#candidate|6897|(15, 4, 12)|var|float64
output = func_6896(var_6897)
func_6898 = relay.Function([var_6897], output)
mutated_mod['func_6898'] = func_6898
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6917 = relay.var("var_6917", dtype = "float64", shape = (3, 5, 2))#candidate|6917|(3, 5, 2)|var|float64
var_6918 = relay.var("var_6918", dtype = "float64", shape = (3, 5, 2))#candidate|6918|(3, 5, 2)|var|float64
bop_6919 = relay.multiply(var_6917.astype('float64'), relay.reshape(var_6918.astype('float64'), relay.shape_of(var_6917))) # shape=(3, 5, 2)
func_5301_call = mod.get_global_var('func_5301')
func_5304_call = mutated_mod.get_global_var('func_5304')
var_6923 = relay.var("var_6923", dtype = "float64", shape = (6,))#candidate|6923|(6,)|var|float64
var_6924 = relay.var("var_6924", dtype = "float32", shape = (567,))#candidate|6924|(567,)|var|float32
call_6922 = relay.TupleGetItem(func_5301_call(relay.reshape(var_6923.astype('float64'), [3, 1, 2]), relay.reshape(var_6924.astype('float32'), [567,]), ), 2)
call_6925 = relay.TupleGetItem(func_5304_call(relay.reshape(var_6923.astype('float64'), [3, 1, 2]), relay.reshape(var_6924.astype('float32'), [567,]), ), 2)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_6933 = relay.TupleGetItem(func_3733_call(), 0)
call_6934 = relay.TupleGetItem(func_3735_call(), 0)
func_3733_call = mod.get_global_var('func_3733')
func_3735_call = mutated_mod.get_global_var('func_3735')
call_6936 = relay.TupleGetItem(func_3733_call(), 1)
call_6937 = relay.TupleGetItem(func_3735_call(), 1)
uop_6946 = relay.sinh(bop_6919.astype('float64')) # shape=(3, 5, 2)
bop_6954 = relay.bitwise_xor(uop_6946.astype('int16'), relay.reshape(bop_6919.astype('int16'), relay.shape_of(uop_6946))) # shape=(3, 5, 2)
uop_6957 = relay.asinh(var_6918.astype('float64')) # shape=(3, 5, 2)
bop_6969 = relay.logical_or(bop_6954.astype('bool'), relay.reshape(uop_6946.astype('bool'), relay.shape_of(bop_6954))) # shape=(3, 5, 2)
var_6987 = relay.var("var_6987", dtype = "bool", shape = (10, 15, 14))#candidate|6987|(10, 15, 14)|var|bool
bop_6988 = relay.left_shift(call_6936.astype('uint8'), var_6987.astype('uint8')) # shape=(10, 15, 14)
bop_6991 = relay.left_shift(call_6937.astype('uint8'), var_6987.astype('uint8')) # shape=(10, 15, 14)
output = relay.Tuple([call_6922,var_6923,var_6924,call_6933,uop_6957,bop_6969,bop_6988,])
output2 = relay.Tuple([call_6925,var_6923,var_6924,call_6934,uop_6957,bop_6969,bop_6991,])
func_6995 = relay.Function([var_6917,var_6918,var_6923,var_6924,var_6987,], output)
mod['func_6995'] = func_6995
mod = relay.transform.InferType()(mod)
var_6996 = relay.var("var_6996", dtype = "float64", shape = (3, 5, 2))#candidate|6996|(3, 5, 2)|var|float64
var_6997 = relay.var("var_6997", dtype = "float64", shape = (3, 5, 2))#candidate|6997|(3, 5, 2)|var|float64
var_6998 = relay.var("var_6998", dtype = "float64", shape = (6,))#candidate|6998|(6,)|var|float64
var_6999 = relay.var("var_6999", dtype = "float32", shape = (567,))#candidate|6999|(567,)|var|float32
var_7000 = relay.var("var_7000", dtype = "bool", shape = (10, 15, 14))#candidate|7000|(10, 15, 14)|var|bool
output = func_6995(var_6996,var_6997,var_6998,var_6999,var_7000,)
func_7001 = relay.Function([var_6996,var_6997,var_6998,var_6999,var_7000,], output)
mutated_mod['func_7001'] = func_7001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6287_call = mod.get_global_var('func_6287')
func_6289_call = mutated_mod.get_global_var('func_6289')
call_7017 = func_6287_call()
call_7018 = func_6287_call()
func_1898_call = mod.get_global_var('func_1898')
func_1899_call = mutated_mod.get_global_var('func_1899')
call_7019 = relay.TupleGetItem(func_1898_call(), 1)
call_7020 = relay.TupleGetItem(func_1899_call(), 1)
output = relay.Tuple([call_7017,call_7019,])
output2 = relay.Tuple([call_7018,call_7020,])
func_7042 = relay.Function([], output)
mod['func_7042'] = func_7042
mod = relay.transform.InferType()(mod)
output = func_7042()
func_7043 = relay.Function([], output)
mutated_mod['func_7043'] = func_7043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5951_call = mod.get_global_var('func_5951')
func_5953_call = mutated_mod.get_global_var('func_5953')
call_7082 = func_5951_call()
call_7083 = func_5951_call()
func_4250_call = mod.get_global_var('func_4250')
func_4252_call = mutated_mod.get_global_var('func_4252')
call_7095 = relay.TupleGetItem(func_4250_call(), 1)
call_7096 = relay.TupleGetItem(func_4252_call(), 1)
uop_7099 = relay.sin(call_7082.astype('float64')) # shape=(3, 4, 3)
uop_7101 = relay.sin(call_7083.astype('float64')) # shape=(3, 4, 3)
func_6484_call = mod.get_global_var('func_6484')
func_6486_call = mutated_mod.get_global_var('func_6486')
call_7115 = func_6484_call()
call_7116 = func_6484_call()
output = relay.Tuple([call_7095,uop_7099,call_7115,])
output2 = relay.Tuple([call_7096,uop_7101,call_7116,])
func_7126 = relay.Function([], output)
mod['func_7126'] = func_7126
mod = relay.transform.InferType()(mod)
mutated_mod['func_7126'] = func_7126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7126_call = mutated_mod.get_global_var('func_7126')
call_7127 = func_7126_call()
output = call_7127
func_7128 = relay.Function([], output)
mutated_mod['func_7128'] = func_7128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4946_call = mod.get_global_var('func_4946')
func_4947_call = mutated_mod.get_global_var('func_4947')
call_7132 = relay.TupleGetItem(func_4946_call(), 0)
call_7133 = relay.TupleGetItem(func_4947_call(), 0)
var_7143 = relay.var("var_7143", dtype = "float32", shape = (2, 15, 5))#candidate|7143|(2, 15, 5)|var|float32
bop_7144 = relay.add(call_7132.astype('uint32'), var_7143.astype('uint32')) # shape=(2, 15, 5)
bop_7147 = relay.add(call_7133.astype('uint32'), var_7143.astype('uint32')) # shape=(2, 15, 5)
output = bop_7144
output2 = bop_7147
func_7148 = relay.Function([var_7143,], output)
mod['func_7148'] = func_7148
mod = relay.transform.InferType()(mod)
var_7149 = relay.var("var_7149", dtype = "float32", shape = (2, 15, 5))#candidate|7149|(2, 15, 5)|var|float32
output = func_7148(var_7149)
func_7150 = relay.Function([var_7149], output)
mutated_mod['func_7150'] = func_7150
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6672_call = mod.get_global_var('func_6672')
func_6674_call = mutated_mod.get_global_var('func_6674')
call_7170 = relay.TupleGetItem(func_6672_call(), 3)
call_7171 = relay.TupleGetItem(func_6674_call(), 3)
func_5200_call = mod.get_global_var('func_5200')
func_5202_call = mutated_mod.get_global_var('func_5202')
call_7183 = relay.TupleGetItem(func_5200_call(), 0)
call_7184 = relay.TupleGetItem(func_5202_call(), 0)
output = relay.Tuple([call_7170,call_7183,])
output2 = relay.Tuple([call_7171,call_7184,])
func_7187 = relay.Function([], output)
mod['func_7187'] = func_7187
mod = relay.transform.InferType()(mod)
mutated_mod['func_7187'] = func_7187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7187_call = mutated_mod.get_global_var('func_7187')
call_7188 = func_7187_call()
output = call_7188
func_7189 = relay.Function([], output)
mutated_mod['func_7189'] = func_7189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6287_call = mod.get_global_var('func_6287')
func_6289_call = mutated_mod.get_global_var('func_6289')
call_7237 = func_6287_call()
call_7238 = func_6287_call()
output = relay.Tuple([call_7237,])
output2 = relay.Tuple([call_7238,])
func_7246 = relay.Function([], output)
mod['func_7246'] = func_7246
mod = relay.transform.InferType()(mod)
output = func_7246()
func_7247 = relay.Function([], output)
mutated_mod['func_7247'] = func_7247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1727_call = mod.get_global_var('func_1727')
func_1728_call = mutated_mod.get_global_var('func_1728')
call_7251 = func_1727_call()
call_7252 = func_1727_call()
func_3414_call = mod.get_global_var('func_3414')
func_3415_call = mutated_mod.get_global_var('func_3415')
call_7258 = relay.TupleGetItem(func_3414_call(), 0)
call_7259 = relay.TupleGetItem(func_3415_call(), 0)
output = relay.Tuple([call_7251,call_7258,])
output2 = relay.Tuple([call_7252,call_7259,])
func_7277 = relay.Function([], output)
mod['func_7277'] = func_7277
mod = relay.transform.InferType()(mod)
mutated_mod['func_7277'] = func_7277
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7277_call = mutated_mod.get_global_var('func_7277')
call_7278 = func_7277_call()
output = call_7278
func_7279 = relay.Function([], output)
mutated_mod['func_7279'] = func_7279
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5089_call = mod.get_global_var('func_5089')
func_5091_call = mutated_mod.get_global_var('func_5091')
call_7300 = relay.TupleGetItem(func_5089_call(), 0)
call_7301 = relay.TupleGetItem(func_5091_call(), 0)
output = relay.Tuple([call_7300,])
output2 = relay.Tuple([call_7301,])
func_7302 = relay.Function([], output)
mod['func_7302'] = func_7302
mod = relay.transform.InferType()(mod)
mutated_mod['func_7302'] = func_7302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7302_call = mutated_mod.get_global_var('func_7302')
call_7303 = func_7302_call()
output = call_7303
func_7304 = relay.Function([], output)
mutated_mod['func_7304'] = func_7304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3930_call = mod.get_global_var('func_3930')
func_3931_call = mutated_mod.get_global_var('func_3931')
call_7313 = relay.TupleGetItem(func_3930_call(), 0)
call_7314 = relay.TupleGetItem(func_3931_call(), 0)
output = relay.Tuple([call_7313,])
output2 = relay.Tuple([call_7314,])
func_7320 = relay.Function([], output)
mod['func_7320'] = func_7320
mod = relay.transform.InferType()(mod)
mutated_mod['func_7320'] = func_7320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7320_call = mutated_mod.get_global_var('func_7320')
call_7321 = func_7320_call()
output = call_7321
func_7322 = relay.Function([], output)
mutated_mod['func_7322'] = func_7322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2867_call = mod.get_global_var('func_2867')
func_2869_call = mutated_mod.get_global_var('func_2869')
call_7331 = relay.TupleGetItem(func_2867_call(), 1)
call_7332 = relay.TupleGetItem(func_2869_call(), 1)
output = call_7331
output2 = call_7332
func_7352 = relay.Function([], output)
mod['func_7352'] = func_7352
mod = relay.transform.InferType()(mod)
output = func_7352()
func_7353 = relay.Function([], output)
mutated_mod['func_7353'] = func_7353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1898_call = mod.get_global_var('func_1898')
func_1899_call = mutated_mod.get_global_var('func_1899')
call_7362 = relay.TupleGetItem(func_1898_call(), 1)
call_7363 = relay.TupleGetItem(func_1899_call(), 1)
output = relay.Tuple([call_7362,])
output2 = relay.Tuple([call_7363,])
func_7386 = relay.Function([], output)
mod['func_7386'] = func_7386
mod = relay.transform.InferType()(mod)
mutated_mod['func_7386'] = func_7386
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7386_call = mutated_mod.get_global_var('func_7386')
call_7387 = func_7386_call()
output = call_7387
func_7388 = relay.Function([], output)
mutated_mod['func_7388'] = func_7388
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4554_call = mod.get_global_var('func_4554')
func_4555_call = mutated_mod.get_global_var('func_4555')
call_7413 = relay.TupleGetItem(func_4554_call(), 1)
call_7414 = relay.TupleGetItem(func_4555_call(), 1)
output = relay.Tuple([call_7413,])
output2 = relay.Tuple([call_7414,])
func_7415 = relay.Function([], output)
mod['func_7415'] = func_7415
mod = relay.transform.InferType()(mod)
output = func_7415()
func_7416 = relay.Function([], output)
mutated_mod['func_7416'] = func_7416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2622_call = mod.get_global_var('func_2622')
func_2623_call = mutated_mod.get_global_var('func_2623')
call_7429 = relay.TupleGetItem(func_2622_call(), 0)
call_7430 = relay.TupleGetItem(func_2623_call(), 0)
func_5217_call = mod.get_global_var('func_5217')
func_5221_call = mutated_mod.get_global_var('func_5221')
var_7442 = relay.var("var_7442", dtype = "uint32", shape = (1, 420))#candidate|7442|(1, 420)|var|uint32
call_7441 = func_5217_call(relay.reshape(var_7442.astype('uint32'), [5, 6, 14]), relay.reshape(var_7442.astype('uint32'), [5, 6, 14]), )
call_7443 = func_5217_call(relay.reshape(var_7442.astype('uint32'), [5, 6, 14]), relay.reshape(var_7442.astype('uint32'), [5, 6, 14]), )
output = relay.Tuple([call_7429,call_7441,var_7442,])
output2 = relay.Tuple([call_7430,call_7443,var_7442,])
func_7463 = relay.Function([var_7442,], output)
mod['func_7463'] = func_7463
mod = relay.transform.InferType()(mod)
mutated_mod['func_7463'] = func_7463
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7464 = relay.var("var_7464", dtype = "uint32", shape = (1, 420))#candidate|7464|(1, 420)|var|uint32
func_7463_call = mutated_mod.get_global_var('func_7463')
call_7465 = func_7463_call(var_7464)
output = call_7465
func_7466 = relay.Function([var_7464], output)
mutated_mod['func_7466'] = func_7466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4213_call = mod.get_global_var('func_4213')
func_4215_call = mutated_mod.get_global_var('func_4215')
call_7498 = relay.TupleGetItem(func_4213_call(), 0)
call_7499 = relay.TupleGetItem(func_4215_call(), 0)
func_180_call = mod.get_global_var('func_180')
func_183_call = mutated_mod.get_global_var('func_183')
var_7503 = relay.var("var_7503", dtype = "int16", shape = (480,))#candidate|7503|(480,)|var|int16
call_7502 = func_180_call(relay.reshape(var_7503.astype('int16'), [15, 4, 8]), relay.reshape(var_7503.astype('int16'), [15, 4, 8]), )
call_7504 = func_180_call(relay.reshape(var_7503.astype('int16'), [15, 4, 8]), relay.reshape(var_7503.astype('int16'), [15, 4, 8]), )
output = relay.Tuple([call_7498,call_7502,var_7503,])
output2 = relay.Tuple([call_7499,call_7504,var_7503,])
func_7505 = relay.Function([var_7503,], output)
mod['func_7505'] = func_7505
mod = relay.transform.InferType()(mod)
mutated_mod['func_7505'] = func_7505
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7506 = relay.var("var_7506", dtype = "int16", shape = (480,))#candidate|7506|(480,)|var|int16
func_7505_call = mutated_mod.get_global_var('func_7505')
call_7507 = func_7505_call(var_7506)
output = call_7507
func_7508 = relay.Function([var_7506], output)
mutated_mod['func_7508'] = func_7508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1779_call = mod.get_global_var('func_1779')
func_1781_call = mutated_mod.get_global_var('func_1781')
call_7521 = func_1779_call()
call_7522 = func_1779_call()
func_1253_call = mod.get_global_var('func_1253')
func_1256_call = mutated_mod.get_global_var('func_1256')
var_7555 = relay.var("var_7555", dtype = "int16", shape = (480,))#candidate|7555|(480,)|var|int16
call_7554 = relay.TupleGetItem(func_1253_call(relay.reshape(call_7521.astype('float64'), [3, 4, 3]), relay.reshape(var_7555.astype('int16'), [480,]), ), 4)
call_7556 = relay.TupleGetItem(func_1256_call(relay.reshape(call_7521.astype('float64'), [3, 4, 3]), relay.reshape(var_7555.astype('int16'), [480,]), ), 4)
output = relay.Tuple([call_7521,call_7554,var_7555,])
output2 = relay.Tuple([call_7522,call_7556,var_7555,])
func_7565 = relay.Function([var_7555,], output)
mod['func_7565'] = func_7565
mod = relay.transform.InferType()(mod)
var_7566 = relay.var("var_7566", dtype = "int16", shape = (480,))#candidate|7566|(480,)|var|int16
output = func_7565(var_7566)
func_7567 = relay.Function([var_7566], output)
mutated_mod['func_7567'] = func_7567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7386_call = mod.get_global_var('func_7386')
func_7388_call = mutated_mod.get_global_var('func_7388')
call_7626 = relay.TupleGetItem(func_7386_call(), 0)
call_7627 = relay.TupleGetItem(func_7388_call(), 0)
var_7628 = relay.var("var_7628", dtype = "float64", shape = (3, 4, 3))#candidate|7628|(3, 4, 3)|var|float64
bop_7629 = relay.mod(call_7626.astype('float64'), relay.reshape(var_7628.astype('float64'), relay.shape_of(call_7626))) # shape=(3, 4, 3)
bop_7632 = relay.mod(call_7627.astype('float64'), relay.reshape(var_7628.astype('float64'), relay.shape_of(call_7627))) # shape=(3, 4, 3)
func_4870_call = mod.get_global_var('func_4870')
func_4873_call = mutated_mod.get_global_var('func_4873')
var_7639 = relay.var("var_7639", dtype = "float32", shape = (2, 56))#candidate|7639|(2, 56)|var|float32
call_7638 = relay.TupleGetItem(func_4870_call(relay.reshape(var_7639.astype('float32'), [7, 8, 2])), 1)
call_7640 = relay.TupleGetItem(func_4873_call(relay.reshape(var_7639.astype('float32'), [7, 8, 2])), 1)
func_544_call = mod.get_global_var('func_544')
func_548_call = mutated_mod.get_global_var('func_548')
const_7663 = relay.const(-3, dtype = "uint32")#candidate|7663|()|const|uint32
var_7664 = relay.var("var_7664", dtype = "uint32", shape = (1, 1408))#candidate|7664|(1, 1408)|var|uint32
call_7662 = relay.TupleGetItem(func_544_call(relay.reshape(const_7663.astype('uint32'), []), relay.reshape(var_7664.astype('uint32'), [16, 11, 8]), ), 1)
call_7665 = relay.TupleGetItem(func_548_call(relay.reshape(const_7663.astype('uint32'), []), relay.reshape(var_7664.astype('uint32'), [16, 11, 8]), ), 1)
output = relay.Tuple([bop_7629,call_7638,var_7639,call_7662,const_7663,var_7664,])
output2 = relay.Tuple([bop_7632,call_7640,var_7639,call_7665,const_7663,var_7664,])
func_7670 = relay.Function([var_7628,var_7639,var_7664,], output)
mod['func_7670'] = func_7670
mod = relay.transform.InferType()(mod)
var_7671 = relay.var("var_7671", dtype = "float64", shape = (3, 4, 3))#candidate|7671|(3, 4, 3)|var|float64
var_7672 = relay.var("var_7672", dtype = "float32", shape = (2, 56))#candidate|7672|(2, 56)|var|float32
var_7673 = relay.var("var_7673", dtype = "uint32", shape = (1, 1408))#candidate|7673|(1, 1408)|var|uint32
output = func_7670(var_7671,var_7672,var_7673,)
func_7674 = relay.Function([var_7671,var_7672,var_7673,], output)
mutated_mod['func_7674'] = func_7674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1898_call = mod.get_global_var('func_1898')
func_1899_call = mutated_mod.get_global_var('func_1899')
call_7735 = relay.TupleGetItem(func_1898_call(), 1)
call_7736 = relay.TupleGetItem(func_1899_call(), 1)
func_7148_call = mod.get_global_var('func_7148')
func_7150_call = mutated_mod.get_global_var('func_7150')
var_7739 = relay.var("var_7739", dtype = "float32", shape = (150,))#candidate|7739|(150,)|var|float32
call_7738 = func_7148_call(relay.reshape(var_7739.astype('float32'), [2, 15, 5]))
call_7740 = func_7148_call(relay.reshape(var_7739.astype('float32'), [2, 15, 5]))
output = relay.Tuple([call_7735,call_7738,var_7739,])
output2 = relay.Tuple([call_7736,call_7740,var_7739,])
func_7741 = relay.Function([var_7739,], output)
mod['func_7741'] = func_7741
mod = relay.transform.InferType()(mod)
var_7742 = relay.var("var_7742", dtype = "float32", shape = (150,))#candidate|7742|(150,)|var|float32
output = func_7741(var_7742)
func_7743 = relay.Function([var_7742], output)
mutated_mod['func_7743'] = func_7743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2187_call = mod.get_global_var('func_2187')
func_2189_call = mutated_mod.get_global_var('func_2189')
call_7771 = func_2187_call()
call_7772 = func_2187_call()
func_2942_call = mod.get_global_var('func_2942')
func_2943_call = mutated_mod.get_global_var('func_2943')
call_7781 = relay.TupleGetItem(func_2942_call(), 2)
call_7782 = relay.TupleGetItem(func_2943_call(), 2)
func_3179_call = mod.get_global_var('func_3179')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_7789 = func_3179_call()
call_7790 = func_3179_call()
uop_7792 = relay.asin(call_7789.astype('float64')) # shape=(3, 4, 3)
uop_7794 = relay.asin(call_7790.astype('float64')) # shape=(3, 4, 3)
output = relay.Tuple([call_7771,call_7781,uop_7792,])
output2 = relay.Tuple([call_7772,call_7782,uop_7794,])
func_7795 = relay.Function([], output)
mod['func_7795'] = func_7795
mod = relay.transform.InferType()(mod)
mutated_mod['func_7795'] = func_7795
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7795_call = mutated_mod.get_global_var('func_7795')
call_7796 = func_7795_call()
output = call_7796
func_7797 = relay.Function([], output)
mutated_mod['func_7797'] = func_7797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7246_call = mod.get_global_var('func_7246')
func_7247_call = mutated_mod.get_global_var('func_7247')
call_7839 = relay.TupleGetItem(func_7246_call(), 0)
call_7840 = relay.TupleGetItem(func_7247_call(), 0)
var_7848 = relay.var("var_7848", dtype = "float64", shape = (3, 4, 3))#candidate|7848|(3, 4, 3)|var|float64
bop_7849 = relay.divide(call_7839.astype('float64'), relay.reshape(var_7848.astype('float64'), relay.shape_of(call_7839))) # shape=(3, 4, 3)
bop_7852 = relay.divide(call_7840.astype('float64'), relay.reshape(var_7848.astype('float64'), relay.shape_of(call_7840))) # shape=(3, 4, 3)
func_6023_call = mod.get_global_var('func_6023')
func_6024_call = mutated_mod.get_global_var('func_6024')
call_7853 = relay.TupleGetItem(func_6023_call(), 1)
call_7854 = relay.TupleGetItem(func_6024_call(), 1)
output = relay.Tuple([bop_7849,call_7853,])
output2 = relay.Tuple([bop_7852,call_7854,])
func_7856 = relay.Function([var_7848,], output)
mod['func_7856'] = func_7856
mod = relay.transform.InferType()(mod)
mutated_mod['func_7856'] = func_7856
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7857 = relay.var("var_7857", dtype = "float64", shape = (3, 4, 3))#candidate|7857|(3, 4, 3)|var|float64
func_7856_call = mutated_mod.get_global_var('func_7856')
call_7858 = func_7856_call(var_7857)
output = call_7858
func_7859 = relay.Function([var_7857], output)
mutated_mod['func_7859'] = func_7859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3179_call = mod.get_global_var('func_3179')
func_3181_call = mutated_mod.get_global_var('func_3181')
call_7883 = func_3179_call()
call_7884 = func_3179_call()
func_2187_call = mod.get_global_var('func_2187')
func_2189_call = mutated_mod.get_global_var('func_2189')
call_7888 = func_2187_call()
call_7889 = func_2187_call()
output = relay.Tuple([call_7883,call_7888,])
output2 = relay.Tuple([call_7884,call_7889,])
func_7896 = relay.Function([], output)
mod['func_7896'] = func_7896
mod = relay.transform.InferType()(mod)
output = func_7896()
func_7897 = relay.Function([], output)
mutated_mod['func_7897'] = func_7897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7187_call = mod.get_global_var('func_7187')
func_7189_call = mutated_mod.get_global_var('func_7189')
call_7909 = relay.TupleGetItem(func_7187_call(), 0)
call_7910 = relay.TupleGetItem(func_7189_call(), 0)
func_3687_call = mod.get_global_var('func_3687')
func_3690_call = mutated_mod.get_global_var('func_3690')
var_7926 = relay.var("var_7926", dtype = "float32", shape = (567,))#candidate|7926|(567,)|var|float32
call_7925 = relay.TupleGetItem(func_3687_call(relay.reshape(var_7926.astype('float32'), [567,]), relay.reshape(var_7926.astype('bool'), [567,]), ), 1)
call_7927 = relay.TupleGetItem(func_3690_call(relay.reshape(var_7926.astype('float32'), [567,]), relay.reshape(var_7926.astype('bool'), [567,]), ), 1)
func_6287_call = mod.get_global_var('func_6287')
func_6289_call = mutated_mod.get_global_var('func_6289')
call_7945 = func_6287_call()
call_7946 = func_6287_call()
bop_7958 = relay.logical_xor(var_7926.astype('uint8'), relay.reshape(call_7925.astype('uint8'), relay.shape_of(var_7926))) # shape=(567,)
bop_7961 = relay.logical_xor(var_7926.astype('uint8'), relay.reshape(call_7927.astype('uint8'), relay.shape_of(var_7926))) # shape=(567,)
func_5791_call = mod.get_global_var('func_5791')
func_5794_call = mutated_mod.get_global_var('func_5794')
call_7965 = relay.TupleGetItem(func_5791_call(relay.reshape(call_7909.astype('float32'), [4, 4])), 0)
call_7966 = relay.TupleGetItem(func_5794_call(relay.reshape(call_7909.astype('float32'), [4, 4])), 0)
var_7971 = relay.var("var_7971", dtype = "float32", shape = (567,))#candidate|7971|(567,)|var|float32
bop_7972 = relay.power(var_7926.astype('float32'), relay.reshape(var_7971.astype('float32'), relay.shape_of(var_7926))) # shape=(567,)
output = relay.Tuple([call_7909,call_7945,bop_7958,call_7965,bop_7972,])
output2 = relay.Tuple([call_7910,call_7946,bop_7961,call_7966,bop_7972,])
F = relay.Function([var_7926,var_7971,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_7926,var_7971,], output2)
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
