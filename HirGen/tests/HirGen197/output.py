import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_262 = relay.const([[[2.744728,-2.886885,-2.479954,2.993672,1.502437,-7.749576,9.708599,0.427715,9.681861],[-4.497308,-6.029197,5.590765,0.915780,0.986078,1.959747,8.236287,2.033218,9.342723],[5.305628,-5.970610,4.250125,1.184121,-2.880319,-1.703263,-3.983559,-8.205376,3.738460],[1.402935,4.373480,-4.815880,6.937745,1.070328,5.037848,6.357893,4.284289,-1.425939],[-2.202561,-5.123054,-8.707615,-0.840743,9.601496,4.039790,2.746653,8.837498,-6.469031],[0.497635,2.661393,-8.936553,2.748763,4.116358,8.268338,1.948212,5.082797,-3.377559],[9.624141,0.600467,6.789242,4.447934,5.862955,2.060845,-6.898660,-4.811556,8.385038],[8.126574,-4.388246,-0.286547,-7.829639,3.143422,0.895187,7.161852,0.746922,4.920240],[-9.168867,0.249425,1.651492,0.138751,1.478985,9.450619,-6.355402,-0.556499,1.002548],[-0.751099,-1.888508,8.867131,-4.557320,-8.945168,1.636604,-1.481353,4.526168,-7.288846],[3.650977,-7.426066,5.968145,2.881098,-8.555191,-1.713362,-5.411064,7.732721,-2.382530],[-9.788335,-6.221935,-9.030237,-4.955162,8.314280,-0.830086,-1.569684,0.191630,6.829972],[-5.184795,-8.842827,-8.139937,-8.334161,5.062584,4.881621,2.719361,-7.007779,4.952759],[1.382829,-4.138353,6.934241,-8.945427,-5.895159,-0.829837,-8.343075,-9.116099,-8.045517],[7.015539,-1.387276,-6.560125,2.736494,7.963982,8.468289,-7.087446,7.942520,0.910104],[-4.634645,-1.266882,2.944808,-0.142072,-5.074696,-7.884032,0.801735,0.918222,2.819848]],[[4.566211,0.458380,-5.542068,2.906528,-9.218149,7.828225,6.948419,3.322415,-5.981151],[3.332363,4.365449,-0.881711,-7.369253,2.818150,5.270218,9.711738,2.566026,1.922922],[-9.648988,7.168176,7.515924,-3.033870,-5.457195,4.585730,2.881596,4.459781,-5.082451],[-2.488277,5.182652,-0.211853,-8.328589,1.978474,0.193564,-6.099240,-1.635076,-3.169358],[-3.362809,-8.007920,-6.634866,-9.646946,-1.205988,-6.491750,0.482094,7.289012,7.596382],[7.137376,-7.660210,6.282426,1.818654,7.415084,9.410988,-9.231949,-6.970740,-7.221357],[-6.967194,-4.027155,-1.003703,4.961405,-4.605818,-5.487391,-3.468261,4.068602,7.228079],[-0.801211,-1.590898,-9.874977,1.056522,-9.957349,5.484457,4.106243,7.862446,4.872669],[-1.796805,2.774767,6.830421,-4.551346,0.703550,-7.146872,6.202152,7.747533,-2.826408],[9.707529,-1.048349,-2.796363,8.333207,1.735364,5.579888,-0.336744,1.285559,-6.141609],[-0.111682,6.253900,3.526946,-8.248964,-4.657595,-8.658765,1.801526,4.378814,6.173968],[4.743819,8.571060,7.440547,2.303177,-1.231069,6.939020,-3.846114,-4.695415,5.192708],[5.461928,-1.275374,-1.833769,2.625196,-9.116525,3.059277,-0.968768,-5.874595,-0.110998],[-2.270682,-5.956526,-5.875477,-4.221790,1.982450,-0.875111,-4.321070,-2.302048,-8.170164],[0.039731,-7.311182,-9.939417,-9.742420,-5.117659,-8.788704,-1.840285,7.072572,4.300378],[8.808313,-1.505216,-0.359743,5.620166,-5.985338,3.184445,-6.654316,-1.263585,8.557584]]], dtype = "float64")#candidate|262|(2, 16, 9)|const|float64
uop_263 = relay.acos(const_262.astype('float64')) # shape=(2, 16, 9)
output = uop_263
output2 = uop_263
func_270 = relay.Function([], output)
mod['func_270'] = func_270
mod = relay.transform.InferType()(mod)
output = func_270()
func_271 = relay.Function([], output)
mutated_mod['func_271'] = func_271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_289 = func_270_call()
call_290 = func_270_call()
output = relay.Tuple([call_289,])
output2 = relay.Tuple([call_290,])
func_292 = relay.Function([], output)
mod['func_292'] = func_292
mod = relay.transform.InferType()(mod)
output = func_292()
func_293 = relay.Function([], output)
mutated_mod['func_293'] = func_293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_332 = func_270_call()
call_333 = func_270_call()
uop_336 = relay.tan(call_332.astype('float64')) # shape=(2, 16, 9)
uop_338 = relay.tan(call_333.astype('float64')) # shape=(2, 16, 9)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_339 = relay.TupleGetItem(func_292_call(), 0)
call_340 = relay.TupleGetItem(func_293_call(), 0)
uop_353 = relay.sigmoid(call_332.astype('float64')) # shape=(2, 16, 9)
uop_355 = relay.sigmoid(call_333.astype('float64')) # shape=(2, 16, 9)
uop_359 = relay.asin(uop_336.astype('float32')) # shape=(2, 16, 9)
uop_361 = relay.asin(uop_338.astype('float32')) # shape=(2, 16, 9)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_377 = relay.TupleGetItem(func_292_call(), 0)
call_378 = relay.TupleGetItem(func_293_call(), 0)
bop_385 = relay.bitwise_xor(uop_359.astype('int8'), relay.reshape(call_377.astype('int8'), relay.shape_of(uop_359))) # shape=(2, 16, 9)
bop_388 = relay.bitwise_xor(uop_361.astype('int8'), relay.reshape(call_378.astype('int8'), relay.shape_of(uop_361))) # shape=(2, 16, 9)
uop_394 = relay.sin(uop_359.astype('float32')) # shape=(2, 16, 9)
uop_396 = relay.sin(uop_361.astype('float32')) # shape=(2, 16, 9)
output = relay.Tuple([call_339,uop_353,bop_385,uop_394,])
output2 = relay.Tuple([call_340,uop_355,bop_388,uop_396,])
func_402 = relay.Function([], output)
mod['func_402'] = func_402
mod = relay.transform.InferType()(mod)
mutated_mod['func_402'] = func_402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_402_call = mutated_mod.get_global_var('func_402')
call_403 = func_402_call()
output = call_403
func_404 = relay.Function([], output)
mutated_mod['func_404'] = func_404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_423 = relay.var("var_423", dtype = "int32", shape = (3, 9, 4))#candidate|423|(3, 9, 4)|var|int32
var_424 = relay.var("var_424", dtype = "int32", shape = (3, 9, 4))#candidate|424|(3, 9, 4)|var|int32
bop_425 = relay.not_equal(var_423.astype('bool'), relay.reshape(var_424.astype('bool'), relay.shape_of(var_423))) # shape=(3, 9, 4)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_428 = relay.TupleGetItem(func_402_call(), 0)
call_429 = relay.TupleGetItem(func_404_call(), 0)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_446 = relay.TupleGetItem(func_402_call(), 0)
call_447 = relay.TupleGetItem(func_404_call(), 0)
output = relay.Tuple([bop_425,call_428,call_446,])
output2 = relay.Tuple([bop_425,call_429,call_447,])
func_456 = relay.Function([var_423,var_424,], output)
mod['func_456'] = func_456
mod = relay.transform.InferType()(mod)
mutated_mod['func_456'] = func_456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_456_call = mutated_mod.get_global_var('func_456')
var_458 = relay.var("var_458", dtype = "int32", shape = (3, 9, 4))#candidate|458|(3, 9, 4)|var|int32
var_459 = relay.var("var_459", dtype = "int32", shape = (3, 9, 4))#candidate|459|(3, 9, 4)|var|int32
call_457 = func_456_call(var_458,var_459,)
output = call_457
func_460 = relay.Function([var_458,var_459,], output)
mutated_mod['func_460'] = func_460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_498 = relay.TupleGetItem(func_402_call(), 0)
call_499 = relay.TupleGetItem(func_404_call(), 0)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_502 = relay.TupleGetItem(func_402_call(), 3)
call_503 = relay.TupleGetItem(func_404_call(), 3)
output = relay.Tuple([call_498,call_502,])
output2 = relay.Tuple([call_499,call_503,])
func_509 = relay.Function([], output)
mod['func_509'] = func_509
mod = relay.transform.InferType()(mod)
output = func_509()
func_510 = relay.Function([], output)
mutated_mod['func_510'] = func_510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_575 = relay.TupleGetItem(func_292_call(), 0)
call_576 = relay.TupleGetItem(func_293_call(), 0)
output = relay.Tuple([call_575,])
output2 = relay.Tuple([call_576,])
func_580 = relay.Function([], output)
mod['func_580'] = func_580
mod = relay.transform.InferType()(mod)
output = func_580()
func_581 = relay.Function([], output)
mutated_mod['func_581'] = func_581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_586 = func_270_call()
call_587 = func_270_call()
output = call_586
output2 = call_587
func_609 = relay.Function([], output)
mod['func_609'] = func_609
mod = relay.transform.InferType()(mod)
output = func_609()
func_610 = relay.Function([], output)
mutated_mod['func_610'] = func_610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_613 = relay.TupleGetItem(func_292_call(), 0)
call_614 = relay.TupleGetItem(func_293_call(), 0)
output = relay.Tuple([call_613,])
output2 = relay.Tuple([call_614,])
func_617 = relay.Function([], output)
mod['func_617'] = func_617
mod = relay.transform.InferType()(mod)
output = func_617()
func_618 = relay.Function([], output)
mutated_mod['func_618'] = func_618
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_640 = func_609_call()
call_641 = func_609_call()
uop_648 = relay.rsqrt(call_640.astype('float64')) # shape=(2, 16, 9)
uop_650 = relay.rsqrt(call_641.astype('float64')) # shape=(2, 16, 9)
output = relay.Tuple([uop_648,])
output2 = relay.Tuple([uop_650,])
func_653 = relay.Function([], output)
mod['func_653'] = func_653
mod = relay.transform.InferType()(mod)
output = func_653()
func_654 = relay.Function([], output)
mutated_mod['func_654'] = func_654
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_671 = relay.TupleGetItem(func_292_call(), 0)
call_672 = relay.TupleGetItem(func_293_call(), 0)
output = call_671
output2 = call_672
func_681 = relay.Function([], output)
mod['func_681'] = func_681
mod = relay.transform.InferType()(mod)
mutated_mod['func_681'] = func_681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mutated_mod.get_global_var('func_681')
call_682 = func_681_call()
output = call_682
func_683 = relay.Function([], output)
mutated_mod['func_683'] = func_683
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_786 = func_681_call()
call_787 = func_681_call()
output = call_786
output2 = call_787
func_788 = relay.Function([], output)
mod['func_788'] = func_788
mod = relay.transform.InferType()(mod)
output = func_788()
func_789 = relay.Function([], output)
mutated_mod['func_789'] = func_789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_952 = relay.TupleGetItem(func_653_call(), 0)
call_953 = relay.TupleGetItem(func_654_call(), 0)
output = relay.Tuple([call_952,])
output2 = relay.Tuple([call_953,])
func_957 = relay.Function([], output)
mod['func_957'] = func_957
mod = relay.transform.InferType()(mod)
output = func_957()
func_958 = relay.Function([], output)
mutated_mod['func_958'] = func_958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_1039 = func_681_call()
call_1040 = func_681_call()
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1043 = relay.TupleGetItem(func_957_call(), 0)
call_1044 = relay.TupleGetItem(func_958_call(), 0)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_1051 = relay.TupleGetItem(func_653_call(), 0)
call_1052 = relay.TupleGetItem(func_654_call(), 0)
output = relay.Tuple([call_1039,call_1043,call_1051,])
output2 = relay.Tuple([call_1040,call_1044,call_1052,])
func_1053 = relay.Function([], output)
mod['func_1053'] = func_1053
mod = relay.transform.InferType()(mod)
output = func_1053()
func_1054 = relay.Function([], output)
mutated_mod['func_1054'] = func_1054
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1090 = relay.var("var_1090", dtype = "uint64", shape = ())#candidate|1090|()|var|uint64
var_1091 = relay.var("var_1091", dtype = "uint64", shape = (16, 14, 14))#candidate|1091|(16, 14, 14)|var|uint64
bop_1092 = relay.not_equal(var_1090.astype('bool'), var_1091.astype('bool')) # shape=(16, 14, 14)
output = bop_1092
output2 = bop_1092
func_1107 = relay.Function([var_1090,var_1091,], output)
mod['func_1107'] = func_1107
mod = relay.transform.InferType()(mod)
var_1108 = relay.var("var_1108", dtype = "uint64", shape = ())#candidate|1108|()|var|uint64
var_1109 = relay.var("var_1109", dtype = "uint64", shape = (16, 14, 14))#candidate|1109|(16, 14, 14)|var|uint64
output = func_1107(var_1108,var_1109,)
func_1110 = relay.Function([var_1108,var_1109,], output)
mutated_mod['func_1110'] = func_1110
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_1131 = func_681_call()
call_1132 = func_681_call()
var_1146 = relay.var("var_1146", dtype = "float64", shape = (2, 16, 9))#candidate|1146|(2, 16, 9)|var|float64
bop_1147 = relay.divide(call_1131.astype('float32'), relay.reshape(var_1146.astype('float32'), relay.shape_of(call_1131))) # shape=(2, 16, 9)
bop_1150 = relay.divide(call_1132.astype('float32'), relay.reshape(var_1146.astype('float32'), relay.shape_of(call_1132))) # shape=(2, 16, 9)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_1152 = relay.TupleGetItem(func_402_call(), 3)
call_1153 = relay.TupleGetItem(func_404_call(), 3)
uop_1157 = relay.log(call_1152.astype('float32')) # shape=(2, 16, 9)
uop_1159 = relay.log(call_1153.astype('float32')) # shape=(2, 16, 9)
output = relay.Tuple([bop_1147,uop_1157,])
output2 = relay.Tuple([bop_1150,uop_1159,])
func_1160 = relay.Function([var_1146,], output)
mod['func_1160'] = func_1160
mod = relay.transform.InferType()(mod)
mutated_mod['func_1160'] = func_1160
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1161 = relay.var("var_1161", dtype = "float64", shape = (2, 16, 9))#candidate|1161|(2, 16, 9)|var|float64
func_1160_call = mutated_mod.get_global_var('func_1160')
call_1162 = func_1160_call(var_1161)
output = call_1162
func_1163 = relay.Function([var_1161], output)
mutated_mod['func_1163'] = func_1163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1177 = relay.TupleGetItem(func_957_call(), 0)
call_1178 = relay.TupleGetItem(func_958_call(), 0)
output = call_1177
output2 = call_1178
func_1210 = relay.Function([], output)
mod['func_1210'] = func_1210
mod = relay.transform.InferType()(mod)
mutated_mod['func_1210'] = func_1210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1210_call = mutated_mod.get_global_var('func_1210')
call_1211 = func_1210_call()
output = call_1211
func_1212 = relay.Function([], output)
mutated_mod['func_1212'] = func_1212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_1213 = relay.TupleGetItem(func_292_call(), 0)
call_1214 = relay.TupleGetItem(func_293_call(), 0)
var_1220 = relay.var("var_1220", dtype = "float64", shape = (2, 16, 9))#candidate|1220|(2, 16, 9)|var|float64
bop_1221 = relay.multiply(call_1213.astype('int32'), relay.reshape(var_1220.astype('int32'), relay.shape_of(call_1213))) # shape=(2, 16, 9)
bop_1224 = relay.multiply(call_1214.astype('int32'), relay.reshape(var_1220.astype('int32'), relay.shape_of(call_1214))) # shape=(2, 16, 9)
func_1107_call = mod.get_global_var('func_1107')
func_1110_call = mutated_mod.get_global_var('func_1110')
var_1241 = relay.var("var_1241", dtype = "uint64", shape = ())#candidate|1241|()|var|uint64
var_1242 = relay.var("var_1242", dtype = "uint64", shape = (196, 16))#candidate|1242|(196, 16)|var|uint64
call_1240 = func_1107_call(relay.reshape(var_1241.astype('uint64'), []), relay.reshape(var_1242.astype('uint64'), [16, 14, 14]), )
call_1243 = func_1107_call(relay.reshape(var_1241.astype('uint64'), []), relay.reshape(var_1242.astype('uint64'), [16, 14, 14]), )
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_1248 = relay.TupleGetItem(func_402_call(), 3)
call_1249 = relay.TupleGetItem(func_404_call(), 3)
uop_1250 = relay.sinh(var_1242.astype('float32')) # shape=(196, 16)
func_1160_call = mod.get_global_var('func_1160')
func_1163_call = mutated_mod.get_global_var('func_1163')
call_1254 = relay.TupleGetItem(func_1160_call(relay.reshape(bop_1221.astype('float64'), [2, 16, 9])), 0)
call_1255 = relay.TupleGetItem(func_1163_call(relay.reshape(bop_1221.astype('float64'), [2, 16, 9])), 0)
bop_1259 = relay.maximum(uop_1250.astype('int64'), var_1241.astype('int64')) # shape=(196, 16)
var_1262 = relay.var("var_1262", dtype = "uint64", shape = (196, 16))#candidate|1262|(196, 16)|var|uint64
bop_1263 = relay.not_equal(var_1242.astype('bool'), relay.reshape(var_1262.astype('bool'), relay.shape_of(var_1242))) # shape=(196, 16)
uop_1271 = relay.sigmoid(uop_1250.astype('float64')) # shape=(196, 16)
uop_1275 = relay.asinh(call_1213.astype('float64')) # shape=(2, 16, 9)
uop_1277 = relay.asinh(call_1214.astype('float64')) # shape=(2, 16, 9)
output = relay.Tuple([bop_1221,call_1240,call_1248,call_1254,bop_1259,bop_1263,uop_1271,uop_1275,])
output2 = relay.Tuple([bop_1224,call_1243,call_1249,call_1255,bop_1259,bop_1263,uop_1271,uop_1277,])
func_1278 = relay.Function([var_1220,var_1241,var_1242,var_1262,], output)
mod['func_1278'] = func_1278
mod = relay.transform.InferType()(mod)
mutated_mod['func_1278'] = func_1278
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1278_call = mutated_mod.get_global_var('func_1278')
var_1280 = relay.var("var_1280", dtype = "float64", shape = (2, 16, 9))#candidate|1280|(2, 16, 9)|var|float64
var_1281 = relay.var("var_1281", dtype = "uint64", shape = ())#candidate|1281|()|var|uint64
var_1282 = relay.var("var_1282", dtype = "uint64", shape = (196, 16))#candidate|1282|(196, 16)|var|uint64
var_1283 = relay.var("var_1283", dtype = "uint64", shape = (196, 16))#candidate|1283|(196, 16)|var|uint64
call_1279 = func_1278_call(var_1280,var_1281,var_1282,var_1283,)
output = call_1279
func_1284 = relay.Function([var_1280,var_1281,var_1282,var_1283,], output)
mutated_mod['func_1284'] = func_1284
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_1341 = func_681_call()
call_1342 = func_681_call()
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_1378 = func_681_call()
call_1379 = func_681_call()
output = relay.Tuple([call_1341,call_1378,])
output2 = relay.Tuple([call_1342,call_1379,])
func_1380 = relay.Function([], output)
mod['func_1380'] = func_1380
mod = relay.transform.InferType()(mod)
mutated_mod['func_1380'] = func_1380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1380_call = mutated_mod.get_global_var('func_1380')
call_1381 = func_1380_call()
output = call_1381
func_1382 = relay.Function([], output)
mutated_mod['func_1382'] = func_1382
mutated_mod = relay.transform.InferType()(mutated_mod)
func_788_call = mod.get_global_var('func_788')
func_789_call = mutated_mod.get_global_var('func_789')
call_1431 = func_788_call()
call_1432 = func_788_call()
output = relay.Tuple([call_1431,])
output2 = relay.Tuple([call_1432,])
func_1433 = relay.Function([], output)
mod['func_1433'] = func_1433
mod = relay.transform.InferType()(mod)
mutated_mod['func_1433'] = func_1433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mutated_mod.get_global_var('func_1433')
call_1434 = func_1433_call()
output = call_1434
func_1435 = relay.Function([], output)
mutated_mod['func_1435'] = func_1435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_788_call = mod.get_global_var('func_788')
func_789_call = mutated_mod.get_global_var('func_789')
call_1482 = func_788_call()
call_1483 = func_788_call()
func_1160_call = mod.get_global_var('func_1160')
func_1163_call = mutated_mod.get_global_var('func_1163')
call_1485 = relay.TupleGetItem(func_1160_call(relay.reshape(call_1482.astype('float64'), [2, 16, 9])), 1)
call_1486 = relay.TupleGetItem(func_1163_call(relay.reshape(call_1482.astype('float64'), [2, 16, 9])), 1)
var_1496 = relay.var("var_1496", dtype = "float32", shape = (2, 16, 9))#candidate|1496|(2, 16, 9)|var|float32
bop_1497 = relay.equal(call_1485.astype('bool'), relay.reshape(var_1496.astype('bool'), relay.shape_of(call_1485))) # shape=(2, 16, 9)
bop_1500 = relay.equal(call_1486.astype('bool'), relay.reshape(var_1496.astype('bool'), relay.shape_of(call_1486))) # shape=(2, 16, 9)
uop_1513 = relay.cos(call_1482.astype('float64')) # shape=(2, 16, 9)
uop_1515 = relay.cos(call_1483.astype('float64')) # shape=(2, 16, 9)
func_617_call = mod.get_global_var('func_617')
func_618_call = mutated_mod.get_global_var('func_618')
call_1526 = relay.TupleGetItem(func_617_call(), 0)
call_1527 = relay.TupleGetItem(func_618_call(), 0)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_1528 = func_270_call()
call_1529 = func_270_call()
output = relay.Tuple([bop_1497,uop_1513,call_1526,call_1528,])
output2 = relay.Tuple([bop_1500,uop_1515,call_1527,call_1529,])
func_1536 = relay.Function([var_1496,], output)
mod['func_1536'] = func_1536
mod = relay.transform.InferType()(mod)
var_1537 = relay.var("var_1537", dtype = "float32", shape = (2, 16, 9))#candidate|1537|(2, 16, 9)|var|float32
output = func_1536(var_1537)
func_1538 = relay.Function([var_1537], output)
mutated_mod['func_1538'] = func_1538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_617_call = mod.get_global_var('func_617')
func_618_call = mutated_mod.get_global_var('func_618')
call_1540 = relay.TupleGetItem(func_617_call(), 0)
call_1541 = relay.TupleGetItem(func_618_call(), 0)
output = relay.Tuple([call_1540,])
output2 = relay.Tuple([call_1541,])
func_1544 = relay.Function([], output)
mod['func_1544'] = func_1544
mod = relay.transform.InferType()(mod)
output = func_1544()
func_1545 = relay.Function([], output)
mutated_mod['func_1545'] = func_1545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_1586 = func_681_call()
call_1587 = func_681_call()
output = relay.Tuple([call_1586,])
output2 = relay.Tuple([call_1587,])
func_1600 = relay.Function([], output)
mod['func_1600'] = func_1600
mod = relay.transform.InferType()(mod)
mutated_mod['func_1600'] = func_1600
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1600_call = mutated_mod.get_global_var('func_1600')
call_1601 = func_1600_call()
output = call_1601
func_1602 = relay.Function([], output)
mutated_mod['func_1602'] = func_1602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1622 = relay.TupleGetItem(func_957_call(), 0)
call_1623 = relay.TupleGetItem(func_958_call(), 0)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_1633 = func_609_call()
call_1634 = func_609_call()
func_509_call = mod.get_global_var('func_509')
func_510_call = mutated_mod.get_global_var('func_510')
call_1647 = relay.TupleGetItem(func_509_call(), 0)
call_1648 = relay.TupleGetItem(func_510_call(), 0)
output = relay.Tuple([call_1622,call_1633,call_1647,])
output2 = relay.Tuple([call_1623,call_1634,call_1648,])
func_1652 = relay.Function([], output)
mod['func_1652'] = func_1652
mod = relay.transform.InferType()(mod)
mutated_mod['func_1652'] = func_1652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1652_call = mutated_mod.get_global_var('func_1652')
call_1653 = func_1652_call()
output = call_1653
func_1654 = relay.Function([], output)
mutated_mod['func_1654'] = func_1654
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1684 = relay.var("var_1684", dtype = "float64", shape = (15, 2, 7))#candidate|1684|(15, 2, 7)|var|float64
uop_1685 = relay.exp(var_1684.astype('float64')) # shape=(15, 2, 7)
func_1536_call = mod.get_global_var('func_1536')
func_1538_call = mutated_mod.get_global_var('func_1538')
const_1690 = relay.const([8.365962,7.275815,-7.233639,-9.840597,-7.730131,6.090007,-6.760507,-8.178379,1.899989,2.166316,-4.383672,-1.690461,8.712422,-3.214382,0.653303,9.743490,3.216113,8.733770,-8.768142,-4.600430,4.983745,-6.641247,-1.490694,-2.958555,3.716627,0.694294,3.012213,-0.839223,-2.713304,6.960191,6.716612,-0.089757,-8.123578,-6.253626,-7.690835,1.530888,3.684148,4.297634,-1.449620,9.827050,2.841725,-5.291799,3.537549,4.197431,1.378599,1.987477,1.520073,-5.083797,-4.387539,9.526446,8.217081,-4.577756,-2.229064,-4.037424,-5.250161,-8.714568,-3.402759,-5.016982,6.410955,5.432540,-1.018052,2.144347,4.975619,2.699413,6.358911,-3.862406,-2.211991,7.268552,-6.524301,8.063767,3.166776,-9.066052,-4.347020,0.426060,-7.665452,1.985985,-4.852639,6.537671,-6.916757,7.158234,3.277829,-7.177279,-2.184136,-8.162727,-5.563558,5.567377,8.409006,3.388808,-4.628915,-4.260957,-2.625394,-8.485106,-1.091354,-7.278319,-4.307344,-4.777501,6.974746,8.944518,-4.739540,-7.165515,-8.611442,8.968952,7.877220,5.996963,0.561079,-5.385103,7.444787,-0.187800,-3.215155,-7.492998,-2.342183,-3.549228,-4.668003,-4.439181,2.603895,4.662289,-0.037332,-8.606931,3.741652,-1.399782,3.072452,-6.662263,6.440466,-4.074213,4.476122,-3.666596,-9.021089,1.814933,6.097244,1.637601,-8.634146,-2.957917,5.485288,-0.045018,-8.024744,-9.772514,-6.260097,5.315663,3.807822,9.984264,-5.562811,1.927345,2.407204,6.038479,-2.429058,5.426599,6.718020,4.585686,-9.792962,-7.972327,-2.345585,-7.955266,8.943085,-0.572202,-7.416709,-9.248996,-3.023808,2.323028,-1.953834,-3.292490,1.423424,-2.896281,7.370519,-8.680547,6.800439,-5.473495,5.830581,-0.383841,-5.826453,6.525853,2.585619,-3.518943,5.588718,1.647257,-7.752287,-3.815953,5.617321,9.117929,9.252055,3.759680,-3.939199,-4.429307,-9.667462,-4.349994,-3.273850,8.463867,3.896018,0.107039,9.476028,4.502436,-7.102870,-3.647210,-2.763685,-2.416017,7.798238,-4.026803,7.364115,1.329849,-0.904433,2.646532,8.384709,-3.901989,-7.224367,-5.393025,-9.138127,1.394068,4.208858,-4.969335,6.686171,4.472613,-6.190239,-3.091435,0.260620,-8.536522,-5.484273,-6.096157,-7.241419,-6.362846,-7.493486,6.242208,-4.527071,9.230211,-2.776896,5.897697,-8.596663,-0.263352,5.926937,-7.149217,-9.033022,-8.225445,-1.374820,-6.862443,4.019687,3.867498,2.515825,-5.734731,-7.426781,-8.416977,5.143923,-8.841509,-1.521182,9.729075,-2.983155,-4.953954,-1.404319,3.647895,9.167649,8.220501,-8.665569,-1.749102,4.114257,-4.041498,-3.641817,-6.375848,-6.730800,1.136143,3.361233,-3.046480,2.898111,-4.380135,1.095616,-7.751591,-2.984634,0.404761,0.487258,-1.778964,-1.260343,-4.413653,7.478171,5.495077,9.757902,2.437211,7.585366,-3.471622,-4.490439,-8.932954,-1.219769,8.867804,-7.209112,-4.303025,-2.800870,4.798306,6.034066,-9.314596,-4.893602,-9.702880,-9.196930,4.366236], dtype = "float32")#candidate|1690|(288,)|const|float32
call_1689 = relay.TupleGetItem(func_1536_call(relay.reshape(const_1690.astype('float32'), [2, 16, 9])), 3)
call_1691 = relay.TupleGetItem(func_1538_call(relay.reshape(const_1690.astype('float32'), [2, 16, 9])), 3)
uop_1696 = relay.sqrt(call_1689.astype('float64')) # shape=(2, 16, 9)
uop_1698 = relay.sqrt(call_1691.astype('float64')) # shape=(2, 16, 9)
uop_1707 = relay.cos(uop_1685.astype('float64')) # shape=(15, 2, 7)
bop_1711 = relay.logical_xor(uop_1685.astype('uint64'), relay.reshape(var_1684.astype('uint64'), relay.shape_of(uop_1685))) # shape=(15, 2, 7)
bop_1721 = relay.bitwise_or(bop_1711.astype('uint64'), relay.reshape(uop_1685.astype('uint64'), relay.shape_of(bop_1711))) # shape=(15, 2, 7)
output = relay.Tuple([const_1690,uop_1696,uop_1707,bop_1721,])
output2 = relay.Tuple([const_1690,uop_1698,uop_1707,bop_1721,])
func_1724 = relay.Function([var_1684,], output)
mod['func_1724'] = func_1724
mod = relay.transform.InferType()(mod)
mutated_mod['func_1724'] = func_1724
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1725 = relay.var("var_1725", dtype = "float64", shape = (15, 2, 7))#candidate|1725|(15, 2, 7)|var|float64
func_1724_call = mutated_mod.get_global_var('func_1724')
call_1726 = func_1724_call(var_1725)
output = call_1726
func_1727 = relay.Function([var_1725], output)
mutated_mod['func_1727'] = func_1727
mutated_mod = relay.transform.InferType()(mutated_mod)
func_617_call = mod.get_global_var('func_617')
func_618_call = mutated_mod.get_global_var('func_618')
call_1729 = relay.TupleGetItem(func_617_call(), 0)
call_1730 = relay.TupleGetItem(func_618_call(), 0)
output = relay.Tuple([call_1729,])
output2 = relay.Tuple([call_1730,])
func_1733 = relay.Function([], output)
mod['func_1733'] = func_1733
mod = relay.transform.InferType()(mod)
mutated_mod['func_1733'] = func_1733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mutated_mod.get_global_var('func_1733')
call_1734 = func_1733_call()
output = call_1734
func_1735 = relay.Function([], output)
mutated_mod['func_1735'] = func_1735
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1757 = relay.var("var_1757", dtype = "int8", shape = (6, 12, 2))#candidate|1757|(6, 12, 2)|var|int8
var_1758 = relay.var("var_1758", dtype = "int8", shape = (6, 12, 2))#candidate|1758|(6, 12, 2)|var|int8
bop_1759 = relay.equal(var_1757.astype('bool'), relay.reshape(var_1758.astype('bool'), relay.shape_of(var_1757))) # shape=(6, 12, 2)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_1762 = relay.TupleGetItem(func_957_call(), 0)
call_1763 = relay.TupleGetItem(func_958_call(), 0)
output = relay.Tuple([bop_1759,call_1762,])
output2 = relay.Tuple([bop_1759,call_1763,])
func_1771 = relay.Function([var_1757,var_1758,], output)
mod['func_1771'] = func_1771
mod = relay.transform.InferType()(mod)
mutated_mod['func_1771'] = func_1771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1771_call = mutated_mod.get_global_var('func_1771')
var_1773 = relay.var("var_1773", dtype = "int8", shape = (6, 12, 2))#candidate|1773|(6, 12, 2)|var|int8
var_1774 = relay.var("var_1774", dtype = "int8", shape = (6, 12, 2))#candidate|1774|(6, 12, 2)|var|int8
call_1772 = func_1771_call(var_1773,var_1774,)
output = call_1772
func_1775 = relay.Function([var_1773,var_1774,], output)
mutated_mod['func_1775'] = func_1775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_1837 = relay.TupleGetItem(func_1733_call(), 0)
call_1838 = relay.TupleGetItem(func_1735_call(), 0)
func_1536_call = mod.get_global_var('func_1536')
func_1538_call = mutated_mod.get_global_var('func_1538')
call_1849 = relay.TupleGetItem(func_1536_call(relay.reshape(call_1837.astype('float32'), [2, 16, 9])), 0)
call_1850 = relay.TupleGetItem(func_1538_call(relay.reshape(call_1837.astype('float32'), [2, 16, 9])), 0)
output = relay.Tuple([call_1837,call_1849,])
output2 = relay.Tuple([call_1838,call_1850,])
func_1860 = relay.Function([], output)
mod['func_1860'] = func_1860
mod = relay.transform.InferType()(mod)
output = func_1860()
func_1861 = relay.Function([], output)
mutated_mod['func_1861'] = func_1861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1600_call = mod.get_global_var('func_1600')
func_1602_call = mutated_mod.get_global_var('func_1602')
call_1868 = relay.TupleGetItem(func_1600_call(), 0)
call_1869 = relay.TupleGetItem(func_1602_call(), 0)
output = relay.Tuple([call_1868,])
output2 = relay.Tuple([call_1869,])
func_1872 = relay.Function([], output)
mod['func_1872'] = func_1872
mod = relay.transform.InferType()(mod)
mutated_mod['func_1872'] = func_1872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1872_call = mutated_mod.get_global_var('func_1872')
call_1873 = func_1872_call()
output = call_1873
func_1874 = relay.Function([], output)
mutated_mod['func_1874'] = func_1874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_1932 = relay.TupleGetItem(func_1544_call(), 0)
call_1933 = relay.TupleGetItem(func_1545_call(), 0)
output = call_1932
output2 = call_1933
func_1940 = relay.Function([], output)
mod['func_1940'] = func_1940
mod = relay.transform.InferType()(mod)
mutated_mod['func_1940'] = func_1940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mutated_mod.get_global_var('func_1940')
call_1941 = func_1940_call()
output = call_1941
func_1942 = relay.Function([], output)
mutated_mod['func_1942'] = func_1942
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2015 = relay.var("var_2015", dtype = "float32", shape = (14, 9, 10))#candidate|2015|(14, 9, 10)|var|float32
var_2016 = relay.var("var_2016", dtype = "float32", shape = (14, 9, 10))#candidate|2016|(14, 9, 10)|var|float32
bop_2017 = relay.maximum(var_2015.astype('float32'), relay.reshape(var_2016.astype('float32'), relay.shape_of(var_2015))) # shape=(14, 9, 10)
bop_2026 = relay.bitwise_and(var_2015.astype('uint64'), relay.reshape(bop_2017.astype('uint64'), relay.shape_of(var_2015))) # shape=(14, 9, 10)
func_1278_call = mod.get_global_var('func_1278')
func_1284_call = mutated_mod.get_global_var('func_1284')
var_2035 = relay.var("var_2035", dtype = "float64", shape = (288,))#candidate|2035|(288,)|var|float64
var_2036 = relay.var("var_2036", dtype = "uint64", shape = ())#candidate|2036|()|var|uint64
var_2037 = relay.var("var_2037", dtype = "uint64", shape = (3136,))#candidate|2037|(3136,)|var|uint64
call_2034 = relay.TupleGetItem(func_1278_call(relay.reshape(var_2035.astype('float64'), [2, 16, 9]), relay.reshape(var_2036.astype('uint64'), []), relay.reshape(var_2037.astype('uint64'), [196, 16]), relay.reshape(var_2037.astype('uint64'), [196, 16]), ), 6)
call_2038 = relay.TupleGetItem(func_1284_call(relay.reshape(var_2035.astype('float64'), [2, 16, 9]), relay.reshape(var_2036.astype('uint64'), []), relay.reshape(var_2037.astype('uint64'), [196, 16]), relay.reshape(var_2037.astype('uint64'), [196, 16]), ), 6)
output = relay.Tuple([bop_2026,call_2034,var_2035,var_2036,var_2037,])
output2 = relay.Tuple([bop_2026,call_2038,var_2035,var_2036,var_2037,])
func_2040 = relay.Function([var_2015,var_2016,var_2035,var_2036,var_2037,], output)
mod['func_2040'] = func_2040
mod = relay.transform.InferType()(mod)
mutated_mod['func_2040'] = func_2040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2040_call = mutated_mod.get_global_var('func_2040')
var_2042 = relay.var("var_2042", dtype = "float32", shape = (14, 9, 10))#candidate|2042|(14, 9, 10)|var|float32
var_2043 = relay.var("var_2043", dtype = "float32", shape = (14, 9, 10))#candidate|2043|(14, 9, 10)|var|float32
var_2044 = relay.var("var_2044", dtype = "float64", shape = (288,))#candidate|2044|(288,)|var|float64
var_2045 = relay.var("var_2045", dtype = "uint64", shape = ())#candidate|2045|()|var|uint64
var_2046 = relay.var("var_2046", dtype = "uint64", shape = (3136,))#candidate|2046|(3136,)|var|uint64
call_2041 = func_2040_call(var_2042,var_2043,var_2044,var_2045,var_2046,)
output = call_2041
func_2047 = relay.Function([var_2042,var_2043,var_2044,var_2045,var_2046,], output)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2055 = relay.const([[[4,8,-7,3,3,-5,4,-4],[-2,6,-8,-2,4,-5,-2,-8],[2,-2,-8,3,8,-6,5,5],[-8,5,9,2,-1,8,-10,2],[2,-1,8,4,3,8,-9,-5],[-4,-5,-8,-8,-2,4,3,-3],[7,-5,-9,1,-8,-2,-2,8],[-9,-2,-7,-8,9,2,6,-6]],[[1,-10,-10,-2,1,-9,-3,2],[-7,-9,-5,7,6,3,-7,9],[-10,-8,-1,1,6,-7,-7,9],[3,10,2,1,9,4,-5,-3],[1,5,2,5,8,-7,3,8],[-3,-4,-8,-4,9,2,-10,-6],[6,2,9,-6,-1,1,8,-10],[10,7,-6,-6,9,-6,-2,-10]],[[8,-6,9,-4,-4,6,4,4],[-1,1,-2,-2,-4,-1,-5,-7],[-3,9,-5,-4,-8,3,-10,6],[-6,9,-6,8,-3,8,-10,-10],[6,-6,-4,9,3,-6,9,-4],[-2,2,6,-8,8,7,-1,-2],[-8,-9,9,4,2,-6,-3,3],[-3,-3,-4,10,-7,4,5,4]],[[-2,-6,10,2,-2,-2,-9,2],[9,-5,-6,-7,-1,10,4,-9],[-8,-7,7,-2,-10,-7,7,-2],[-5,-1,1,4,10,-10,-10,3],[6,-8,-1,-3,3,9,7,8],[10,3,-9,5,-10,4,-6,10],[6,4,-8,-10,6,3,-3,-7],[2,8,6,-1,-10,10,1,-7]],[[-8,6,-9,7,8,-1,2,-5],[8,6,-9,-2,-1,7,2,10],[-5,6,-5,-9,4,3,8,10],[3,1,10,-3,8,4,-3,2],[3,4,-2,10,-5,-1,2,10],[-5,9,6,10,-3,-6,9,8],[3,-9,-5,10,-1,-4,2,8],[4,-7,-1,-6,1,3,-9,1]]], dtype = "uint8")#candidate|2055|(5, 8, 8)|const|uint8
var_2056 = relay.var("var_2056", dtype = "uint8", shape = (5, 8, 8))#candidate|2056|(5, 8, 8)|var|uint8
bop_2057 = relay.left_shift(const_2055.astype('uint8'), relay.reshape(var_2056.astype('uint8'), relay.shape_of(const_2055))) # shape=(5, 8, 8)
output = bop_2057
output2 = bop_2057
func_2062 = relay.Function([var_2056,], output)
mod['func_2062'] = func_2062
mod = relay.transform.InferType()(mod)
mutated_mod['func_2062'] = func_2062
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2063 = relay.var("var_2063", dtype = "uint8", shape = (5, 8, 8))#candidate|2063|(5, 8, 8)|var|uint8
func_2062_call = mutated_mod.get_global_var('func_2062')
call_2064 = func_2062_call(var_2063)
output = call_2064
func_2065 = relay.Function([var_2063], output)
mutated_mod['func_2065'] = func_2065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_509_call = mod.get_global_var('func_509')
func_510_call = mutated_mod.get_global_var('func_510')
call_2156 = relay.TupleGetItem(func_509_call(), 0)
call_2157 = relay.TupleGetItem(func_510_call(), 0)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_2174 = relay.TupleGetItem(func_653_call(), 0)
call_2175 = relay.TupleGetItem(func_654_call(), 0)
func_2040_call = mod.get_global_var('func_2040')
func_2047_call = mutated_mod.get_global_var('func_2047')
const_2183 = relay.const([9.451741,1.493262,-2.085414,6.947268,3.532936,3.747646,4.142964,0.199419,3.838182,-2.556546,1.785540,-2.073072,-2.831763,-1.090411,3.777268,-8.311871,0.012642,-4.262841,-9.557373,5.320172,2.330273,8.468950,-8.890955,3.422432,7.416912,3.780811,4.451340,8.610645,8.387586,9.039811,-0.811830,7.221094,9.789255,0.930074,4.039723,-4.071939,6.851656,-1.750910,-2.095184,2.331214,1.576144,-5.027675,-1.619241,-4.542880,5.099495,9.313894,7.712582,-3.333508,-9.768531,-2.209261,-0.769513,-7.860922,-3.244965,5.349239,-9.955245,-7.146568,0.396746,-1.308566,7.533099,4.330744,6.903537,-3.623212,1.808649,3.281539,-7.948268,-9.284054,-6.884164,-6.123453,3.227641,-3.247174,-0.381316,4.532343,2.225714,0.989972,-4.433960,-9.909317,3.183462,-3.169593,0.095364,-5.814117,7.487076,-9.966946,-0.391182,4.046073,-9.197026,2.437804,-9.707007,-2.520536,1.585964,-8.213294,-1.473862,6.761739,1.467698,-6.653228,7.137131,-7.926202,5.346402,0.566156,3.542837,1.922253,-0.200772,-5.857490,5.174823,-3.276448,2.942427,-1.744975,7.300699,6.859872,9.345801,5.089993,2.276036,-6.933114,-4.743188,-1.017747,-2.761847,5.640539,-3.021355,5.453126,-0.714316,-8.425483,1.924400,0.902716,-4.601606,7.939385,2.805116,3.080767,9.406541,3.442817,0.047935,3.827999,-8.385408,-1.698441,4.879543,-4.128912,6.340335,5.164495,-0.945207,-2.127845,5.500450,-2.547744,-5.966790,7.790796,4.894138,-1.148848,-1.777318,-8.455354,-4.644250,-5.125641,8.604156,-6.428348,4.792837,3.924009,-0.104230,0.080012,0.985188,-4.287001,1.363397,9.113593,7.349965,9.165127,-4.221904,-7.615045,-3.006222,-8.125206,7.050443,-1.130694,-4.505404,-4.430843,9.890849,-9.763396,-0.435566,6.283298,6.406225,-4.300462,-0.729751,-4.204318,-2.171643,0.396541,6.376699,-4.537673,-8.080992,-4.368038,-0.233282,-5.137672,-9.887719,-0.932787,7.342616,-0.632780,9.947773,7.620058,-9.784037,-8.683395,-5.337844,5.855286,9.415308,1.954350,-9.811312,-9.260377,-5.010984,7.470286,3.463968,6.502924,9.339570,8.790986,4.261856,-5.710101,7.570988,-3.930901,-7.690033,0.982099,5.137755,-9.289283,-5.862787,-4.151365,7.441238,9.469475,6.281177,6.633988,-6.989808,4.654980,-0.791019,1.838433,-4.572674,7.024298,1.598939,-9.933922,2.716035,3.370447,9.716094,1.142376,0.655922,-7.871165,9.417748,6.944635,-3.671638,0.792959,-0.214683,-5.132255,-2.771664,9.183097,4.129060,-7.460063,-8.727018,-3.866203,0.813697,-5.675030,6.674056,-4.996315,1.712141,-1.806102,-9.516902,-8.594804,7.744252,-6.743323,-6.085126,4.409454,3.443800,9.299698,1.372477,-1.235504,1.211898,3.518294,5.354441,4.184856,8.648001,-9.860868,-8.461603,-6.454601,-8.082158,4.207602,5.917279,-0.527865,0.457508,-1.612283,2.286535,9.513770,-9.038143,3.348286,-7.432332,-7.972207,5.308288,-1.963428,9.288747,4.150786,9.586766,-0.310596,0.841551,2.017751,-6.081254,-6.699628,-7.734588,-9.649979,-7.328482,-3.990293,3.936499,0.453125,-0.696242,-0.017438,-8.589224,4.305200,-7.545792,-6.014008,-1.479451,-4.595776,-5.613765,-5.960549,7.073969,6.639935,7.266530,-6.840476,-3.841361,0.040782,6.384910,-8.911357,7.176525,1.408673,5.567409,7.273167,-8.033762,3.809390,-3.316000,2.237607,-6.343084,-0.889182,6.227583,-9.516321,-9.969244,-6.339006,1.640324,0.235988,-6.041105,3.016296,4.514077,7.350199,-2.187918,-7.873997,-9.519266,-8.097712,-7.142157,-5.414226,-1.984768,9.786720,-5.403781,-8.021334,-5.782891,-5.400196,4.818757,-9.443972,7.999586,-2.535336,-8.363910,-6.066682,-2.286326,-7.391652,6.708766,-6.989703,4.815278,-2.054008,4.591142,-6.069172,3.706747,-0.704364,-9.431744,3.491196,-1.571182,2.078858,-0.307026,-6.896551,2.247472,5.133721,4.642159,-6.233651,4.030681,6.743205,6.232131,-9.682277,-7.549551,3.207649,0.597067,-6.230435,-4.279099,1.716716,-1.450888,-8.688241,-9.989878,-3.979746,9.579426,-3.190165,-2.564983,-0.458829,8.753030,-6.475329,0.997869,-2.663358,-9.129089,2.999087,9.426717,1.498274,-4.431824,1.605128,6.438205,-8.301457,-0.333032,0.337871,-1.000584,-8.294813,-9.015195,-9.727869,2.423779,-5.297124,5.658863,-4.760044,-7.831190,-4.190581,4.041998,6.819023,-8.521036,-0.344155,0.968225,8.766178,7.576932,6.243650,-1.061568,3.211354,4.602346,0.113275,5.152869,8.649870,3.350275,-3.874507,8.811820,4.938869,-1.883994,-6.960710,1.325252,8.885083,9.025199,-5.885610,-6.852299,5.800108,3.616877,0.389469,1.617142,4.067781,-1.136043,2.247860,0.878924,6.593805,-0.103731,4.685674,2.169842,-5.071001,-4.017569,-0.060837,8.199996,-2.992649,-9.121305,8.083392,-7.924522,-9.906515,1.103004,-4.640338,-1.304181,-4.727103,4.416015,-3.788802,-5.685362,2.690793,6.281782,-8.475016,-5.591453,-8.470266,-6.938699,-6.732901,-0.249750,7.540468,-9.522454,-7.884012,-8.055282,-1.965703,7.147429,-2.870225,8.893317,-7.232322,-2.921113,6.818881,1.177884,8.985603,-8.220009,-4.437867,0.736936,-7.804805,5.265161,-6.855063,1.172080,6.945784,-1.754251,-9.207480,0.237926,-6.391477,6.096693,-3.208835,8.659936,-1.217290,5.513596,-7.276224,2.341309,5.691128,-4.130168,-7.937992,-7.377518,-9.938047,0.800861,-3.438720,5.659198,-5.252769,7.814043,7.883937,3.771340,-2.145872,-0.006760,8.574027,3.247031,-6.345901,-0.264005,9.335954,-8.905946,6.929951,-1.214631,-3.298866,7.450591,6.181783,-6.837732,9.618793,-3.574429,-7.053479,5.607550,-3.651057,-2.983398,-7.285709,7.121782,2.615722,1.752766,-0.160081,0.447927,8.251522,6.806852,8.691215,2.517294,3.656459,-9.466614,-9.935265,7.809244,-8.326861,0.489065,2.553226,-9.369634,-4.583442,9.427784,3.821551,1.517445,8.691916,3.884330,-7.988837,-4.132218,4.928713,-4.348044,-9.025232,-0.739530,3.637719,3.097909,8.211418,-7.252910,8.822148,-0.029908,-4.420095,2.425947,-0.988569,-0.375975,7.209043,6.485064,9.011454,-2.318707,2.580402,-5.441429,-8.246984,4.904658,6.278764,3.271181,-5.078663,2.479073,4.754606,-1.205749,-1.609340,6.005563,2.702845,-3.193086,-3.234799,-3.802694,8.901551,-1.614705,-5.754659,0.199941,7.546546,-2.758166,-5.982861,-3.866751,-4.220265,-9.326116,1.725241,-2.565271,-9.339764,7.280355,7.885156,-7.032673,-0.692438,-1.843347,7.377922,-3.350112,-3.964618,-4.519764,4.778380,3.137286,5.465887,-1.185998,0.794325,-6.921446,9.927610,-3.842254,0.731617,9.719614,0.321097,5.287820,-4.980120,-7.097921,-6.484134,7.011372,4.238679,-0.123401,-1.384795,-6.008892,5.085509,8.014658,-4.862751,-6.690703,5.507007,-8.091571,9.172130,2.843101,0.400713,1.846321,-4.191043,9.514548,9.768697,-4.288788,-7.467752,9.336797,7.205194,-2.153849,-1.773725,-9.067422,9.609885,-9.235444,-2.653722,-5.129279,0.193206,2.215535,-8.204052,-8.295146,-5.770934,-6.518290,4.261089,8.401806,-8.373809,-9.659513,-5.772637,-5.551683,8.866505,-5.734466,-8.485627,-6.363200,-1.284764,5.175380,-1.239247,-0.440517,0.142223,-8.479594,-7.416783,6.558579,9.028617,9.565465,-8.905720,8.317566,2.657523,6.949686,-9.531381,4.946905,-2.883463,-4.735580,-3.636534,9.003459,2.258816,-4.357365,1.930595,-4.882630,-0.372698,-9.255046,-3.694150,-0.347712,-2.864502,4.168068,0.679069,7.619641,-8.027331,7.802058,0.582487,-3.059053,-8.372323,-0.040922,-3.797640,-5.782992,6.451606,-0.128769,3.526849,6.696134,-6.651241,-7.665470,2.761106,6.090577,4.480244,9.385011,-5.537021,5.582606,-3.835386,-2.153630,7.557062,6.315185,-6.039979,-8.620989,9.723304,2.917681,-8.206805,2.613263,6.494956,0.341034,5.411445,9.407391,-2.172476,-5.320201,6.744166,-2.413782,-3.091991,0.059145,5.196157,-6.538146,6.882680,-9.321860,8.775503,4.104771,0.186938,-1.834123,1.033354,-4.298359,-2.396662,1.003953,6.560638,-2.108938,0.402594,-1.548974,4.929873,0.630415,-6.935216,3.388927,-6.316977,2.828719,3.792222,-5.881199,6.395913,5.027705,-1.598719,6.314918,-8.999785,2.423241,7.425933,-0.913265,-3.384908,2.748585,1.589162,-8.511562,-5.680677,6.283380,3.556801,-8.392891,-3.977573,2.767245,-3.691431,0.551786,-6.108230,7.823907,-9.311782,4.446232,3.297766,-9.444469,7.644575,-7.626094,-7.324113,2.475700,-5.402101,-3.190862,6.075595,0.964385,8.847607,-1.857129,8.525568,2.045316,8.836055,-8.144249,-7.522380,-9.704983,4.216471,0.815026,-6.417962,-6.525342,-9.633910,-4.244313,-4.628775,-2.554296,-2.956703,5.347213,-8.451546,1.934129,4.167770,-9.192681,-7.296735,7.555180,-7.210466,1.328607,-1.349126,4.691803,4.324143,-0.874929,1.052347,4.159285,-0.261774,7.996122,1.696010,-9.043769,-2.168658,-7.704856,4.007567,-1.906646,-5.373799,4.067848,6.918862,-6.170185,-0.315741,-3.118059,8.595649,5.976761,7.051535,-4.782084,7.603209,5.026746,3.294705,2.618406,-9.236753,-6.812341,9.588090,2.579356,-6.498380,1.620554,-1.341110,-8.753727,1.545409,0.389702,-3.458732,-9.116500,5.684274,8.679809,4.025667,9.051445,0.416390,8.913848,7.234381,2.755717,-0.876936,-2.282971,5.793984,-9.451760,-7.697394,2.378293,4.390098,3.524454,7.239334,2.061190,3.983370,-5.121893,0.274758,3.208448,-7.786959,-9.196600,-8.238215,-5.172723,-8.691570,-0.565447,-8.715062,8.355484,8.307774,-6.010963,-1.543571,-5.187076,4.511761,-0.280934,-3.056581,1.323792,-7.679097,3.025070,8.859249,-9.077243,-1.548618,-5.850046,-0.584120,-3.984738,-4.227863,3.428363,-1.898099,-5.074447,-6.155848,-8.871393,8.367838,-6.752632,-4.259330,-5.421552,4.902841,5.685450,4.184535,-5.619922,3.587037,-3.383510,-9.400163,-8.441484,1.338209,-5.786551,8.738380,-0.709552,-5.242105,0.111334,-5.947139,-8.382991,-9.464216,1.735569,-5.717690,-4.806684,-4.602397,5.070618,-3.587524,0.543541,9.871517,7.962861,3.440787,4.703897,-5.545131,-6.903308,-8.663199,-4.349419,-1.170049,-5.197972,-5.538446,-3.026660,7.161709,7.541048,-0.191182,0.050995,-2.596787,-3.016177,-2.801315,0.250846,-3.750728,8.499706,1.564761,-2.720766,4.402295,-6.085472,9.988314,-1.496628,-1.354054,-4.498331,8.594813,-7.337141,-4.693874,4.663703,-0.906426,-5.564913,-3.702761,6.383952,0.346022,0.610193,9.585526,-9.729484,-2.433185,9.393989,-9.035229,1.997227,-1.112029,6.585835,2.340618,8.666034,-7.339534,-2.918370,-7.361415,-5.670440,1.570099,-5.792536,6.083784,3.141674,-7.359530,-0.964858,-5.359468,-6.139773,-1.606366,-8.673434,-5.373049,1.354982,6.889359,5.447273,-5.946910,8.345810,8.564678,-5.791952,4.576112,-6.576163,-2.860469,-6.770414,1.545164,1.036971,7.618072,3.853227,-5.673163,-0.577411,-2.037701,8.292097,9.969207,7.972460,-0.415528,4.160710,5.421582,2.630685,-2.969036,3.219314,-6.784830,9.328015,-5.950921,1.542522,-4.810469,-2.656975,7.523728,0.205261,-0.933246,8.765076,-5.488525,-0.380293,1.219117,1.667198,-3.289800,5.667380,-3.885505,-4.548581,8.340578,0.536148,0.315169,-6.396032,9.785549,0.136575,-3.765567,-1.174604,0.838170,9.538781,7.313660,-2.617406,0.224667,-4.632025,6.799164,-6.861778,4.696474,-8.386776,3.016581,6.123483,-7.640706,-7.033374,-9.610645,2.231664,-2.526695,-6.775255,5.820514,0.418928,-2.737018,-4.369904,-6.451084,-3.081085,-5.589820,-0.980198,8.476418,-7.800683,-9.525367,4.882836,-3.239922,-1.566272,4.910021,-5.587223,8.910124,2.141313,0.560748,5.492980,-6.030552,9.626308,-1.299817,-3.644675,-2.761442,9.558060,0.183364,9.756835,7.259123,-9.586432,-9.899216,-1.821526,-6.044020,0.002352,9.591647,1.968141,-5.631713,7.654661,-6.359523,-8.659796,-3.458688,9.839630,-8.263643,2.000762,-7.962495,-1.556865,-0.051787,1.231462,-6.400877,6.289075,6.579751,1.578187,7.299479,1.375438,-8.660360,-3.319969,3.986523,3.565431,-1.830865,-6.327265,-4.587943,3.155483,5.588831,-0.595044,9.271104,5.579818,-3.441544,-0.978658,1.941100,-5.075276,-2.333734,6.432991,-3.034171,7.299100,5.440814,-8.061445,1.030663,3.773770,-8.316846,-6.154511,2.031034,-4.256670,5.692822,1.074961,-7.597800,-1.493201,4.807294,4.185360,-6.405482,-5.259990,-6.368293,-7.728524,8.856306,-4.906831,1.117787,5.560793,-6.051945,-6.851683,0.119201,1.325116,8.845722,-9.152655,9.914864,8.033266,-5.371886,1.816880,-3.917608,-1.557961,3.342379,0.437317,-5.531031,6.022207,-0.212836,-5.032868,-2.253018,-7.255445,3.705322,-8.167278,-9.940055,3.110779,3.072047,4.031842,-9.955917,0.014512,-7.460144,-3.139056,-7.417356,0.424002,5.501443,-2.056004,8.889926,-8.038855,1.268037,9.817854,-5.212190,-6.409134,-9.970141,7.012549,-3.008729,-4.469832,6.808700,0.864125,9.716720,-0.348674,-8.921127,-3.775376,1.640684,-9.237072,2.523749,-2.067413,-8.768916,3.657902,-0.619568,6.540269,-4.031025,6.932606,-7.084209,2.694922,-0.003888,8.140843,-6.168225,-7.668420,-5.474765,-3.460384,0.050928,3.693859,5.570026], dtype = "float32")#candidate|2183|(1260,)|const|float32
var_2184 = relay.var("var_2184", dtype = "uint64", shape = ())#candidate|2184|()|var|uint64
const_2185 = relay.const([4,6,10,-9,-2,-9,-7,-2,6,10,3,6,-7,6,-10,9,1,-8,-3,-10,-7,9,7,-1,-5,4,5,3,-2,2,-10,-6,6,-1,-10,-4,-9,3,4,10,8,-7,-3,3,-1,-7,-7,3,-6,4,5,-5,1,-2,-3,-4,6,2,-4,-5,3,8,-5,-3,7,-9,5,9,-1,1,-1,6,8,7,4,-9,-3,7,9,-1,9,-9,3,10,-8,9,-6,7,5,-8,-5,6,-5,6,-4,10,-6,-8,10,-4,-9,-8,-9,10,8,-3,-6,-8,5,-7,-10,4,8,6,10,-6,6,3,-8,1,5,-6,-4,-2,-10,-8,5,-6,-4,3,-6,-10,-3,-10,-9,5,-3,-5,-7,6,5,8,5,-5,8,-10,6,-7,-4,10,-7,5,7,-7,-6,-4,6,-3,7,8,9,-2,-8,6,7,5,-10,-6,-2,-5,-5,-1,2,1,-3,9,-9,-9,-1,8,8,3,-6,6,1,6,2,-10,3,-6,-2,-10,-5,7,1,-5,1,-8,-9,4,-8,10,10,-2,1,1,2,-2,10,2,-5,10,-7,2,5,-7,-10,10,-5,5,2,-9,9,1,1,1,-10,-3,-1,2,2,-8,-4,-2,-3,-7,5,1,-7,1,6,7,3,3,-4,-10,4,-9,-6,-1,10,-6,-4,-6,1,-3,9,5,8,8,2,-8,-5,7,10,10,4,2,5,2,-5,-5,5,-10,5,-6,-5,-3,3,-2,6,2,2,-1,-2,-4,-8,-5,6,-5,-1,-10,-7,-7,-5,-5,2,2,-1,-2,-5,-2,-3,5,10,2,3,10,-5,2,7,-2,5,5,-8,-9,-1,-6,-9,6,3,3,-8,-5,9,4,7,6,-9,-7,8,-1,-8,7,-10,-7,9,-8,-2,-3,-2,-8,4,-10,7,-1,5,5,-9,-1,5,1,-9,-2,-3,3,-3,-6,-4,-9,6,-5,-10,-4,-5,9,6,-6,8,-5,5,10,-8,-3,5,-3,-2,1,1,2,-4,-7,-8,5,-1,10,-8,-3,9,9,8,6,-10,-1,-4,-8,3,-9,10,-8,6,-6,10,-1,5,-6,1,4,-9,-4,-7,3,10,10,8,1,-10,8,-8,1,-10,8,-9,5,-7,-2,3,-6,-9,-3,6,9,-2,-8,-6,4,7,7,6,3,1,10,1,9,2,-7,7,-6,10,9,-4,2,-7,-5,-1,8,6,-5,4,8,-7,8,-10,-1,10,-8,3,6,-7,4,-1,-9,2,3,10,-6,6,-1,8,-7,-1,3,-5,5,9,-1,4,5,-5,-4,2,4,-3,4,-4,-10,-8,-9,9,6,-5,-8,6,-7,-4,8,10,-5,4,4,2,2,-6,-4,7,5,-8,1,8,5,-10,9,-4,2,-6,5,-10,-2,8,-3,8,6,-1,-10,-4,3,9,-3,10,10,-4,6,1,-2,5,-5,3,9,-8,-5,5,8,3,8,9,-9,-4,-10,-4,6,-10,-2,-4,-9,1,9,-5,1,-8,-1,-8,3,7,7,-8,1,-5,2,-4,-6,-6,-1,1,1,1,-8,4,1,5,-5,10,-10,8,6,5,-5,6,4,-7,9,-6,-9,10,-4,-5,-9,-6,9,3,6,-9,8,8,-3,6,-5,8,-7,-3,5,-1,-2,-5,10,8,5,8,3,7,3,9,-8,-1,7,-5,1,-7,4,5,10,-2,1,8,10,-1,9,-2,-8,1,8,-8,-3,-1,6,2,9,9,-6,5,2,-8,7,7,4,3,-3,8,-5,-2,-4,5,8,5,-2,-1,-8,5,-10,3,10,3,-4,-1,3,9,6,3,1,10,-8,-10,-10,2,-9,4,-8,7,2,-2,-9,-2,-9,1,-3,-3,-1,-7,-10,-3,-3,-10,-5,-4,3,10,9,1,9,9,-4,-2,7,-8,-6,6,7,10,-3,7,-2,-9,10,-2,3,-10,-4,-2,2,6,10,-7,9,8,-6,9,-3,1,-10,2,-4,8,7,-7,-9,-6,4,-5,3,-5,8,6,-2,-5,-2,6,3,2,-4,-6,-3,-4,-6,-1,2,-7,-10,2,-10,6,7,-7,-6,10,-9,2,9,-8,5,-3,5,-9,-2,1,-9,-5,-9,-9,-3,-4,5,6,-2,-8,-6,-5,-2,-10,-5,-8,7,3,8,-10,10,5,10,9,8,10,-2,-6,9,-9,-6,1,10,1,7,-9,5,-2,7,-8,1,-8,-3,7,10,-8,-3,-2,-2,-3,2,6,5,-4,-1,7,8,-7,10,5,-2,-8,10,9,1,-3,-3,-2,-8,1,7,-3,3,-8,-8,5,-5,-4,-3,9,5,8,-2,6,-7,9,-7,10,6,5,2,1,-4,-4,-10,-2,-6,4,-1,6,-9,1,-1,8,-1,-9,-6,2,-9,-9,-1,5,1,3,-4,-7,6,-1,-1,4,3,-8,-8,-8,-9,8,-6,-7,-4,9,3,-1,4,-8,10,-8,7,-1,-6,-2,4,7,4,-8,-8,6,-1,-10,8,3,-2,-2,-6,-4,10,1,7,-5,-4,9,8,-3,2,-7,3,-2,-10,2,5,-2,3,10,-1,-10,8,9,5,-6,-5,-1,2,1,-6,-9,10,-10,5,4,-3,-5,4,-6,3,-9,-4,7,4,7,3,-2,5,8,2,-8,-6,5,-6,-10,4,9,2,3,6,-5,-5,-3,-9,-2,1,-5,2,7,-4,9,10,5,4,5,9,2,-9,4,-6,-8,-6,-5,4,8,-1,-5,5,-3,1,2,10,-1,6,4,2,10,6,10,-9,7,7,1,3,2,3,-3,7,9,-1,-7,6,3,-5,1,3,-4,-9,2,-10,-7,10,6,-4,-1,10,8,-7,10,-3,-4,9,7,-2,2,-5,4,9,-3,5,-5,-3,-10,3,-10,1,3,1,-9,-10,4,-2,-3,8,-3,1,5,3,2,-7,2,-8,9,-6,-4,-1,-2,-7,-3,10,-8,-4,-4,-10,2,-3,-7,-1,10,-7,2,3,1,8,4,10,10,5,-2,2,-4,10,4,8,-9,-8,-10,-4,10,-7,-1,-8,-2,2,-10,7,9,-3,-7,1,-5,6,10,8,-3,6,-9,-2,9,-4,10,5,7,6,-9,1,-6,9,6,-5,2,2,10,-4,-9,10,-8,-3,-2,-10,-6,7,7,-7,5,3,-7,-1,-8,-6,1,-8,-10,7,-8,7,7,5,3,-8,-5,-6,-5,-7,-1,-2,10,3,-1,-4,-7,-4,-6,-10,-2,-5,-1,-7,-9,-1,-7,3,5,7,-4,6,3,-6,8,6,-4,6,4,-2,-10,-5,8,-6,2,10,6,7,-5,-6,9,-4,3,-10,3,-1,-5,-2,4,9,-1,4,-2,-5,-8,-9,-1,1,2,2,-3,10,1,2,-10,-1,-9,-6,-10,7,2,-6,-10,-8,8,2,4,9,6,1,4,6,-9,-4,5,-8,9,1,-10,-4,2,-10,-9,-2,-2,-10,-4,-2,9,5,-9,-1,6,-10,5,-5,-1,3,-3,5,-7,4,9,8,1,-4,-6,-3,-10,-9,8,-2,-8,-10,-2,-6,8,-2,-3,-9,-6,9,7,-6,-4,2,10,4,10,7,-7,-3,-3,3,7,-2,-2,-5,-10,10,6,7,-7,-4,-5,1,5,6,-8,4,1,-6,-5,-6,2,1,7,5,-1,10,-9,-7,-4,-2,1,6,2,-7,-5,-3,6,-4,-6,-6,8,-2,-7,-3,1,3,-3,-6,-1,1,-5,-2,10,3,-6,2,2,-3,4,-2,-3,-1,-4,-1,-9,10,9,-4,-7,-5,-3,-7,5,-8,9,-8,-4,1,5,2,4,-7,-3,4,-7,3,9,4,3,5,-3,4,-9,5,7,-7,9,-6,6,-4,-10,-10,8,-1,8,-3,-8,-8,4,-2,-1,3,-4,6,-10,10,7,7,5,-10,-5,-4,2,1,-7,6,-1,-10,10,4,6,10,-3,3,-8,-3,-6,7,10,3,-10,-5,-1,-7,-3,-3,-4,-6,-1,-6,-2,1,5,7,5,-3,2,-7,7,4,-4,10,-1,6,7,-10,-1,8,-10,-1,6,9,6,-1,-9,-2,3,10,10,7,-7,6,-9,-4,-9,3,3,-5,5,9,-2,-6,4,-10,-3,2,5,8,4,2,-6,-1,6,-7,2,6,8,-9,-9,9,-6,-4,2,-5,-3,-10,-4,10,-8,3,-5,-6,-3,9,3,-6,10,-8,-1,9,-1,-6,1,-5,3,3,-8,-2,3,7,-9,7,-4,-2,-9,10,9,5,2,-2,-9,-4,3,10,-7,-6,-9,-6,7,9,-6,-5,6,6,9,2,3,5,-2,-4,3,3,-10,-6,-6,4,-5,-8,1,7,-2,-8,-7,-10,9,7,-1,-3,-1,1,-3,9,6,-6,-1,-4,4,-7,4,-1,1,-2,-10,7,-3,9,3,-3,7,-3,4,3,-1,10,-8,-10,-9,-3,-9,-10,-9,10,9,9,5,-6,3,-7,-10,2,8,-8,6,3,4,-10,4,-2,-5,1,-7,9,6,2,4,3,8,6,5,-9,-7,-1,-1,6,-8,-6,-5,2,-4,7,-10,8,2,-2,-5,7,10,-3,-2,6,7,4,-8,3,-3,-10,1,-1,-3,-3,3,-2,-9,-3,7,3,-3,8,-5,5,-3,1,4,8,-4,-8,10,-8,-9,2,-2,10,1,-7,10,4,-7,-7,4,8,6,-5,-10,-5,-5,4,1,-1,3,1,-9,5,8,7,-7,2,-5,-2,-1,3,-6,-3,1,1,3,-7,7,-10,-6,-8,6,-8,6,-3,9,-3,2,-1,-10,-1,6,-7,2,7,6,4,-3,10,-4,-6,-10,-9,-5,-9,5,-7,-8,4,-4,1,-4,2,9,9,-7,-8,4,-1,-8,-3,10,3,-6,9,8,10,5,3,3,7,9,-7,3,-1,8,-3,5,6,5,-1,-3,8,4,2,-3,7,6,-4,-4,1,8,10,-4,-5,2,-5,-1,-5,-4,2,7,9,5,-6,10,-3,-3,-2,-9,-7,4,-8,-5,-10,7,8,1,-9,3,-9,3,1,-5,5,9,7,-4,-8,5,7,10,-9,-3,1,-4,-8,2,-4,-2,3,1,-7,-4,-5,5,-4,-7,7,-1,-5,9,-3,5,-8,-8,-8,-10,5,2,-4,2,-1,10,9,6,-6,9,4,9,-1,-2,6,-6,5,-1,-4,-8,1,2,-7,6,-3,-5,1,10,10,4,3,9,9,-8,4,-9,4,-5,-2,-8,-7,4,6,-1,6,-2,-5,-9,-10,9,-5,-9,10,3,4,-6,2,-1,6,5,-9,-2,-6,1,10,-10,-6,5,10,7,9,8,-5,-2,-3,2,-1,-6,-7,-3,-7,-3,9,-9,8,-6,9,-10,3,7,8,7,6,-6,-2,-10,-1,2,-1,-10,6,7,10,-2,-1,10,-8,1,-2,-7,-8,-1,-9,1,-3,10,9,-7,-7,5,-9,7,1,3,7,-6,-4,5,2,-5,9,6,-3,10,-3,-9,-9,2,-6,-3,-3,-5,-8,2,6,-4,-3,4,3,-7,8,-9,-2,-9,3,1,-1,-5,-9,-8,4,-2,2,4,-2,10,-5,-9,9,7,-9,8,-5,8,9,8,8,2,-6,5,-7,9,5,1,7,-6,6,-6,-6,-6,-2,2,-4,2,-3,7,-4,-2,-6,5,-2,-10,4,3,10,-8,-4,2,5,8,-3,-7,-3,9,3,3,-4,8,-8,-1,10,1,-10,-2,9,4,-4,2,-10,-7,5,-10,2,1,9,-8,-1,-3,-2,-5,-2,6,8,3,6,-10,-1,-2,-8,-5,-4,6,-2,4,3,-8,8,2,9,-5,9,-8,6,5,2,1,-5,-9,7,2,5,-4,1,3,3,-8,5,-3,5,-7,10,-5,6,-1,-1,10,10,-1,1,-4,1,-7,8,-7,7,-4,-1,-1,2,7,-4,9,2,6,5,-8,-2,3,4,-4,4,-10,-4,-2,-3,-2,-8,3,-5,3,-1,-6,-5,-2,9,-10,4,9,-10,-8,10,2,-5,7,-3,9,1,-6,4,-3,-6,7,-2,-9,7,-5,-9,4,9,-1,-2,-6,-6,7,-10,5,5,5,-8,10,-2,-2,-4,-3,8,5,6,2,4,4,-2,-10,-10,-4,9,-4,1,-2,-4,9,-10,-3,8,10,5,-5,-2,-5,10,-1,-5,10,4,-2,8,2,6,6,-1,5,10,-4,-3,-5,8,1,-2,1,4,2,-5,-2,2,-4,-6,-8,8,-9,10,-5,-9,-2,-7,4,-8,-5,-3,-3,-5,-7,-7,9,8,8,1,6,10,-10,-3,-10,1,4,-2,-10,-8,-10,-3,-2,-7,8,-6,8,6,-6,-2,-2,2,8,2,3,-4,-7,-1,7,1,-6,4,4,-3,9,-7,-10,-6,4,-8,-10,-1,-9,-5,-2,4,3,3,-7,6,-2,8,1,-10,-4,4,-1,10,-9,8,9,-9,-9,-10,9,-4,-6,-2,-8,3,-1,5,-2,-1,8,-10,1,-1,-4,-7,-6,7,-5,10,3,5,-8,5,-3,-9,-6,-10,-2,5,2,10,-7,2,6,-5,-5,3,1,3,4,7,-5,-5,9,-3,-6,-1,-2,4,4,6,-2,-5,7,-8,-2,-9,3,-3,7,-3,1,-5,6,-10,1,-2,-5,7,-4,10,-4,-4,6,9,-7,6,8,-10,3,7,-8,-8,-7,-2,3,-9,-5,-4,-4,4,-5,9,4,-10,-1,-10,7,1,-4,-4,-9,4,8,6,-10,3,-3,-9,-4,-3,-7,6,-4,7,-10,-6,4,2,7,5,-8,-3,3,-9,2,-5,-6,2,-8,7,9,-8,3,-6,9,10,-4,-10,8,7,9,10,3,-5,-8,-8,6,-2,5,3,-1,-1,7,-3,9,6,2,-5,-5,-3,-3,-2,6,-1,-1,-6,7,-9,-9,1,2,7,-3,-8,-5,3,-1,-8,-10,1,3,-6,-5,7,7,5,5,-5,6,-9,4,8,9,-4,7,10,5,10,-1,5,7,9,-1,2,-8,8,-5,7,4,-4,-1,3,-2,-5,2,-3,9,2,-10,9,7,10,-6,7,2,-3,8,6,-10,5,10,-2,-3,1,9,1,-9,-8,-10,5,6,3,-5,-4,-2,7,-8,-3,1,4,7,-8,6,9,2,-8,-3,2,1,-3,6,5,6,7,-5,9,-6,-6,4,-6,3,-7,-6,4,-9,-10,-4,-1,6,-10,-8,-3,-8,5,-6,10,-7,-6,8,-10,-7,-1,7,3,-9,4,-2,2,-6,3,9,3,-10,9,-1,4,1,-10,7,-2,6,4,5,-9,-4,-4,6,9,8,-8,8,6,-7,-8,8,3,-7,4,-4,4,-5,-8,-8,1,-6,-5,-10,4,5,-4,-3,9,-3,-6,7,-4,8,7,1,-2,-6,-1,-7,-6,8,-7,4,-5,-2,5,-10,-4,-10,-4,1,-6,-4,7,-4,4,-2,5,9,-4,-2,10,7,8,-7,6,2,-8,1,-8,8,-8,-4,-6,-4,4,1,-8,10,-6,10,-6,6,-9,-1,5,-2,10,8,1,-8,10,8,8,3,6,5,-6,-8,-9,3,-10,7,-2,-6,8,5,5,-5,-3,4,4,1,-10,6,-8,5,5,-8,10,-8,-1,-6,10,7,4,1,1,-9,-1,-4,5,8,3,8,1,-2,3,-9,3,-4,-9,2,-7,3,-5,10,8,3,6,-7,-7,1,8,1,-6,-8,-2,-7,3,-8,8,-10,5,-10,-5,8,-5,-2,-9,-4,-1,-1,3,1,-7,4,-8,2,10,-4,8,-6,3,7,2,10,-6,-6,9,6,-8,-3,-7,-10,8,9,-8,-10,3,-4,1,-10,-4,-7,-4,1,5,6,9,-8,-10,5,-4,-8,4,-3,5,-5,8,2,-7,1,4,-4,5,-2,-1,-10,3,1,9,4,5,-1,-1,4,3,-10,7,2,5,5,-10,-10,-3,10,-5,6,-6,-5,-9,7,-6,-10,10,-3,5,-3,-4,-8,4,-9,-6,10,-1,1,4,3,-2,1,5,8,-3,-7,-4,4,-4,-8,9,2,-3,-1,10,6,-6,-5,2,-3,2,4,6,5,-10,-2,-3,8,-7,2,2,9,-7,-1,8,8,5,-8,-7,-10,-6,-7,-7,6,3,-1,-7,4,-7,-7,-10,-4,6,-5,5,-1,8,-1,-10,-8,6,-9,-2,-9,10,5,-10,7,1,8,-7,-8,-4,7,5,-10,-7,-3,3,-9,7,-5,10,-2,5,-8,8,5,-4,-9,-10,-1,-7,-5,6,7,7,-10,-5,-10,2,-3,4,2,2,1,8,8,-6,-10,-6,-8,1,10,10,-6,-9,-1,-7,-3,4], dtype = "uint64")#candidate|2185|(3136,)|const|uint64
call_2182 = relay.TupleGetItem(func_2040_call(relay.reshape(const_2183.astype('float32'), [14, 9, 10]), relay.reshape(const_2183.astype('float32'), [14, 9, 10]), relay.reshape(call_2156.astype('float64'), [288,]), relay.reshape(var_2184.astype('uint64'), []), relay.reshape(const_2185.astype('uint64'), [3136,]), ), 4)
call_2186 = relay.TupleGetItem(func_2047_call(relay.reshape(const_2183.astype('float32'), [14, 9, 10]), relay.reshape(const_2183.astype('float32'), [14, 9, 10]), relay.reshape(call_2156.astype('float64'), [288,]), relay.reshape(var_2184.astype('uint64'), []), relay.reshape(const_2185.astype('uint64'), [3136,]), ), 4)
uop_2187 = relay.erf(call_2174.astype('float32')) # shape=(2, 16, 9)
uop_2189 = relay.erf(call_2175.astype('float32')) # shape=(2, 16, 9)
output = relay.Tuple([call_2156,call_2182,const_2183,var_2184,const_2185,uop_2187,])
output2 = relay.Tuple([call_2157,call_2186,const_2183,var_2184,const_2185,uop_2189,])
func_2208 = relay.Function([var_2184,], output)
mod['func_2208'] = func_2208
mod = relay.transform.InferType()(mod)
var_2209 = relay.var("var_2209", dtype = "uint64", shape = ())#candidate|2209|()|var|uint64
output = func_2208(var_2209)
func_2210 = relay.Function([var_2209], output)
mutated_mod['func_2210'] = func_2210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_2212 = relay.TupleGetItem(func_1872_call(), 0)
call_2213 = relay.TupleGetItem(func_1874_call(), 0)
output = call_2212
output2 = call_2213
func_2239 = relay.Function([], output)
mod['func_2239'] = func_2239
mod = relay.transform.InferType()(mod)
mutated_mod['func_2239'] = func_2239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2239_call = mutated_mod.get_global_var('func_2239')
call_2240 = func_2239_call()
output = call_2240
func_2241 = relay.Function([], output)
mutated_mod['func_2241'] = func_2241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_2275 = relay.TupleGetItem(func_292_call(), 0)
call_2276 = relay.TupleGetItem(func_293_call(), 0)
output = call_2275
output2 = call_2276
func_2321 = relay.Function([], output)
mod['func_2321'] = func_2321
mod = relay.transform.InferType()(mod)
mutated_mod['func_2321'] = func_2321
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2321_call = mutated_mod.get_global_var('func_2321')
call_2322 = func_2321_call()
output = call_2322
func_2323 = relay.Function([], output)
mutated_mod['func_2323'] = func_2323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2338 = relay.var("var_2338", dtype = "int8", shape = (8, 1, 13))#candidate|2338|(8, 1, 13)|var|int8
const_2339 = relay.const([[[7,7,5,-10,-1,9,7,3,-10,9,1,7,-2],[-6,5,2,-1,-3,-4,9,9,7,1,-1,-8,9],[4,3,-2,-3,-6,10,-2,4,-7,-5,3,6,2],[5,10,1,-7,-9,5,10,5,-9,-5,2,7,10],[-9,-4,-6,3,2,-7,10,9,-6,-5,9,7,-6],[-5,8,3,-4,10,-5,-3,9,-5,5,-2,-3,3],[10,3,3,-3,5,-10,-2,-6,-5,5,10,1,-5],[8,10,7,3,10,-10,-7,-8,4,7,-8,-1,-4]],[[-4,-6,-8,5,6,-1,-6,5,3,-2,8,2,6],[-8,4,5,9,-5,6,8,-5,-2,-10,-6,-10,-4],[2,6,8,4,7,10,-3,-4,6,-10,1,-2,1],[-3,-4,-9,-5,-6,-8,4,4,-3,8,5,-1,7],[-8,-4,6,-10,-4,-9,-4,1,9,-9,-9,7,2],[-3,6,-7,-10,-3,-8,-7,2,3,-2,7,-2,-4],[9,-8,3,5,3,4,-3,-10,-10,5,-4,7,7],[-9,10,-7,5,9,-9,9,-8,-5,-2,4,-1,-5]],[[1,3,5,4,7,4,9,2,-10,9,-4,1,-9],[-7,7,-5,3,4,-2,-5,4,-1,-7,-10,-3,-6],[-3,-2,-3,-3,2,-9,-8,5,5,-10,-3,1,-5],[-8,-2,-5,3,-7,8,-9,10,7,2,7,-4,-4],[8,-7,-10,1,-9,-7,6,9,8,6,5,-3,5],[-2,-8,6,-6,9,7,-8,-8,7,2,10,5,5],[7,-6,-9,3,-9,-3,1,-10,6,3,4,-10,9],[4,5,-5,-9,-7,3,8,-9,8,-7,-8,-8,-8]],[[2,-9,-7,-6,-6,7,4,-6,5,9,-4,-4,7],[3,3,-10,-9,-6,5,1,3,-7,-5,3,6,6],[9,1,1,3,-7,-1,-1,-5,10,-8,-5,9,-7],[-1,-6,-2,-6,3,9,3,9,4,-10,-6,4,-3],[-8,-8,7,-7,6,-8,-2,-10,-6,-9,-5,-5,-2],[3,-7,-5,-1,10,-2,-8,6,-1,-8,-3,3,1],[5,-5,9,2,-4,-2,10,2,-1,-10,-8,-7,-3],[-3,2,-6,-2,-5,9,-8,4,10,2,-6,2,-7]],[[-9,1,5,-10,-9,-6,-9,3,-10,-3,-9,-8,4],[-1,2,-1,6,-6,-7,10,5,7,8,-4,-1,5],[-9,-8,-9,-3,10,-3,-5,7,-5,8,-2,-6,6],[-1,8,-4,8,-1,-4,-9,8,9,1,5,-3,-10],[9,7,7,-10,-3,1,8,-10,8,-7,1,10,-3],[10,8,-1,5,10,-6,-6,-7,-2,-10,-1,4,-5],[-5,-9,-7,-4,-8,-2,3,-4,4,-1,6,10,-8],[6,-9,8,-3,-10,-3,-7,-1,3,-3,-4,6,10]],[[9,-2,10,-10,7,1,-3,10,9,-9,6,-4,-1],[-6,4,-1,-5,-1,-10,-4,-8,-5,-9,-1,4,-7],[-1,7,-9,-1,8,-7,4,8,10,-1,8,-1,2],[-5,1,-7,3,6,-9,-5,8,10,2,8,-1,-2],[6,7,-5,-6,-2,-1,-9,9,6,4,7,-8,1],[3,-8,2,8,3,2,2,-6,-1,1,-2,-3,3],[-10,1,8,5,8,-9,9,-2,5,6,-6,-6,-8],[-6,-5,-1,1,-6,5,-6,-3,9,-8,4,4,5]],[[-9,-9,-9,8,-5,1,-2,-4,10,-1,-4,6,1],[7,2,-7,5,7,-4,-10,-3,-4,7,3,-7,-4],[-5,5,2,3,-6,-6,8,-6,8,1,6,10,3],[-5,-6,-1,9,6,8,7,2,4,9,-4,6,2],[-1,7,4,4,1,10,1,-5,-7,-4,8,-1,-8],[3,10,-7,-8,5,-8,-1,-4,3,8,8,-2,4],[-2,6,10,5,-7,-9,9,-6,-2,-8,-1,-6,8],[-4,-8,-10,-5,-10,6,-3,10,-7,-7,-7,-3,9]],[[-5,2,-1,-6,7,9,4,7,9,-4,-5,7,5],[2,9,1,6,-1,-2,-8,-7,-2,-8,-1,-10,-5],[6,-6,-6,-3,8,2,9,-5,-2,-9,9,8,-8],[-4,3,-3,1,-4,-6,3,10,1,9,-8,8,10],[7,-5,-8,-5,-8,4,10,6,4,3,5,3,10],[4,1,7,3,-6,1,-6,2,8,-7,-7,2,-6],[3,-10,3,3,8,-3,-2,-4,10,3,9,3,4],[8,9,-2,5,7,5,-3,10,6,7,-6,-1,9]]], dtype = "int8")#candidate|2339|(8, 8, 13)|const|int8
bop_2340 = relay.minimum(var_2338.astype('int8'), const_2339.astype('int8')) # shape=(8, 8, 13)
output = bop_2340
output2 = bop_2340
func_2347 = relay.Function([var_2338,], output)
mod['func_2347'] = func_2347
mod = relay.transform.InferType()(mod)
mutated_mod['func_2347'] = func_2347
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2348 = relay.var("var_2348", dtype = "int8", shape = (8, 1, 13))#candidate|2348|(8, 1, 13)|var|int8
func_2347_call = mutated_mod.get_global_var('func_2347')
call_2349 = func_2347_call(var_2348)
output = call_2349
func_2350 = relay.Function([var_2348], output)
mutated_mod['func_2350'] = func_2350
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2359 = relay.var("var_2359", dtype = "int8", shape = (9, 14, 11))#candidate|2359|(9, 14, 11)|var|int8
var_2360 = relay.var("var_2360", dtype = "int8", shape = (9, 14, 11))#candidate|2360|(9, 14, 11)|var|int8
bop_2361 = relay.multiply(var_2359.astype('int8'), relay.reshape(var_2360.astype('int8'), relay.shape_of(var_2359))) # shape=(9, 14, 11)
output = relay.Tuple([bop_2361,])
output2 = relay.Tuple([bop_2361,])
func_2370 = relay.Function([var_2359,var_2360,], output)
mod['func_2370'] = func_2370
mod = relay.transform.InferType()(mod)
mutated_mod['func_2370'] = func_2370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2370_call = mutated_mod.get_global_var('func_2370')
var_2372 = relay.var("var_2372", dtype = "int8", shape = (9, 14, 11))#candidate|2372|(9, 14, 11)|var|int8
var_2373 = relay.var("var_2373", dtype = "int8", shape = (9, 14, 11))#candidate|2373|(9, 14, 11)|var|int8
call_2371 = func_2370_call(var_2372,var_2373,)
output = call_2371
func_2374 = relay.Function([var_2372,var_2373,], output)
mutated_mod['func_2374'] = func_2374
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2379 = relay.const([[[-8,-6,9,-6,-1,7,-8],[-2,-6,-6,-1,-2,2,9],[5,8,6,-8,1,3,-5],[-4,1,6,10,2,9,-2],[-3,-5,-7,-2,8,-10,-3],[3,-1,-3,-2,-2,10,-4],[8,-2,-6,-1,-3,-8,2],[1,8,3,2,-4,2,-7],[-7,-3,-6,10,-3,7,-4],[8,10,1,-5,7,-8,-2],[-6,5,9,-10,5,6,-1],[-6,5,-10,3,-3,4,6],[3,-4,-4,-4,-9,7,-6],[-1,-6,-1,1,8,-3,-2],[4,-10,-3,-8,5,1,6]],[[-9,-3,-1,-7,1,-6,-4],[3,7,-4,-4,3,-6,-4],[6,7,4,6,-10,-8,3],[-2,-2,-2,4,-7,-3,-2],[3,-7,6,2,5,-3,-1],[8,4,2,6,-4,10,-9],[-6,-1,7,-5,6,-2,5],[8,6,-3,-7,-6,-9,-5],[6,9,7,8,-1,-6,10],[10,5,5,-5,4,3,6],[2,10,-5,7,-2,5,-8],[10,1,7,-7,9,-3,3],[5,-10,9,5,1,-6,-7],[-6,-4,-6,6,2,8,-5],[-8,-10,8,-8,-10,-2,4]],[[-5,1,-9,6,1,-9,-5],[-6,-9,-9,-5,-9,-3,-7],[3,5,6,7,-10,-1,5],[5,8,-2,-6,-7,7,6],[-8,-7,8,-7,7,-2,-9],[1,4,5,5,-2,-8,4],[9,-7,4,-8,-5,1,-10],[-2,-5,-4,7,4,9,-3],[-6,-4,6,10,3,-6,-4],[10,-9,3,-5,4,8,-2],[-3,6,3,-2,9,-2,-1],[-1,-5,-9,5,-10,-8,-10],[4,5,-10,-7,-1,3,3],[2,-6,-9,8,-5,9,-3],[2,5,-9,3,1,4,9]],[[2,7,-9,1,-1,-7,1],[-4,5,2,-1,-2,2,-4],[-7,-8,-6,7,5,5,-6],[-6,8,-3,-7,-3,-8,3],[-10,10,10,8,-2,-3,-10],[7,-9,-3,3,10,-3,-10],[-9,4,-10,7,-4,-7,-10],[5,7,8,-5,4,10,-9],[6,5,4,5,6,5,-8],[8,5,2,5,9,-4,7],[-5,-7,8,8,-3,-8,-8],[-1,-7,6,2,3,9,-7],[-5,7,1,-2,-5,-2,7],[1,3,2,1,-10,-10,-10],[5,2,-2,-9,-2,-3,-5]],[[-9,-5,6,2,-7,-9,-8],[2,-8,5,-8,-8,1,9],[-8,1,7,-8,3,2,-3],[-9,-8,8,7,-5,-10,1],[4,7,6,-9,-3,5,-7],[8,-8,10,7,9,1,10],[-8,5,2,-3,-10,-1,-1],[1,-5,-7,-7,6,-5,9],[-10,9,9,-1,-6,1,-9],[2,-3,8,-3,9,-4,-1],[2,6,8,-4,-9,-10,-9],[4,-5,8,9,-6,-4,2],[3,-8,-3,9,-10,-8,7],[-8,9,4,8,6,1,2],[8,-1,7,-6,-4,4,9]],[[4,10,-2,-4,6,10,3],[-5,-5,1,4,7,-10,8],[-6,-6,2,-2,6,3,-2],[-4,-4,-2,-2,9,10,-7],[-7,-4,1,-3,5,-9,3],[-3,-7,-10,7,-2,-4,6],[-6,-4,-7,8,-8,3,6],[4,-6,-4,5,-5,-5,-1],[7,3,-10,8,5,7,9],[-7,-6,4,-10,-6,-2,9],[-10,-6,-8,2,-8,-9,-8],[-8,-8,2,8,7,-6,-4],[6,6,4,10,-3,-1,-3],[-5,9,-8,10,3,5,7],[5,-10,5,-4,1,10,-8]],[[-4,5,2,5,-3,7,5],[7,5,-3,2,2,6,10],[7,1,9,-3,10,-10,-2],[-8,-2,9,9,-4,-2,5],[-2,-6,-4,-2,-10,5,-2],[-2,3,3,7,3,-4,4],[-3,-3,-5,2,5,2,1],[-5,2,9,-7,9,4,7],[8,3,-10,4,7,-5,-2],[-6,-6,-5,-10,4,-9,-1],[-6,1,10,3,2,7,3],[-10,1,-7,-10,-5,-9,6],[-3,-10,-5,-3,7,-7,5],[-8,6,-3,-7,3,-5,8],[1,-1,-10,5,4,-2,-6]],[[-9,3,-1,-9,-5,7,4],[10,7,5,-6,-10,4,-1],[-4,7,9,-5,6,-7,10],[1,-7,7,2,1,-1,-9],[7,-3,-8,-4,-8,-9,3],[-7,9,9,9,-9,10,-7],[3,7,-9,-8,-1,-5,-3],[3,-10,9,8,-5,-7,-6],[-4,-9,-2,-4,-7,7,9],[6,8,-8,-2,8,-8,-7],[-7,2,-7,-8,-9,1,7],[5,1,9,-5,-6,7,-8],[-6,10,7,5,-4,6,-5],[9,-4,9,-8,-5,-7,-9],[-6,7,-2,-7,10,-5,-5]],[[6,-8,2,-1,-9,1,-1],[6,1,7,-6,-7,-7,5],[1,-3,-9,-4,-4,4,-2],[-5,1,3,3,-2,-8,-2],[-7,-7,6,-7,-2,6,6],[9,-2,2,-6,-7,-6,10],[1,-9,10,1,7,-2,9],[-4,9,4,8,7,1,-6],[7,9,9,-8,-3,8,-5],[8,10,10,5,-1,7,8],[-3,5,10,8,3,8,-3],[7,-7,-5,-6,6,-6,-4],[-4,3,7,-7,-3,6,-1],[3,1,3,2,6,-2,9],[9,2,-6,-3,4,-7,5]],[[2,-8,-1,2,10,3,-4],[-10,4,8,5,3,-6,9],[2,9,-1,1,-9,-7,9],[-6,-4,7,8,-6,-9,10],[-3,-1,5,3,8,-8,-6],[-5,-7,-7,-7,-1,-2,-7],[-3,8,-8,-3,8,8,9],[-2,-5,8,-10,-2,-3,-2],[-7,6,8,10,-3,-10,8],[-9,-8,-1,-10,2,6,-6],[7,4,9,-8,5,4,10],[1,5,-6,-2,5,-4,1],[3,10,7,5,-3,-2,10],[6,-3,-7,-6,-9,-8,10],[1,5,-9,3,-7,2,1]]], dtype = "uint32")#candidate|2379|(10, 15, 7)|const|uint32
var_2380 = relay.var("var_2380", dtype = "uint32", shape = (10, 15, 7))#candidate|2380|(10, 15, 7)|var|uint32
bop_2381 = relay.right_shift(const_2379.astype('uint32'), relay.reshape(var_2380.astype('uint32'), relay.shape_of(const_2379))) # shape=(10, 15, 7)
bop_2384 = relay.add(const_2379.astype('float32'), relay.reshape(bop_2381.astype('float32'), relay.shape_of(const_2379))) # shape=(10, 15, 7)
output = relay.Tuple([bop_2384,])
output2 = relay.Tuple([bop_2384,])
func_2401 = relay.Function([var_2380,], output)
mod['func_2401'] = func_2401
mod = relay.transform.InferType()(mod)
var_2402 = relay.var("var_2402", dtype = "uint32", shape = (10, 15, 7))#candidate|2402|(10, 15, 7)|var|uint32
output = func_2401(var_2402)
func_2403 = relay.Function([var_2402], output)
mutated_mod['func_2403'] = func_2403
mutated_mod = relay.transform.InferType()(mutated_mod)
func_788_call = mod.get_global_var('func_788')
func_789_call = mutated_mod.get_global_var('func_789')
call_2422 = func_788_call()
call_2423 = func_788_call()
output = relay.Tuple([call_2422,])
output2 = relay.Tuple([call_2423,])
func_2426 = relay.Function([], output)
mod['func_2426'] = func_2426
mod = relay.transform.InferType()(mod)
mutated_mod['func_2426'] = func_2426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2426_call = mutated_mod.get_global_var('func_2426')
call_2427 = func_2426_call()
output = call_2427
func_2428 = relay.Function([], output)
mutated_mod['func_2428'] = func_2428
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_581_call = mutated_mod.get_global_var('func_581')
call_2453 = relay.TupleGetItem(func_580_call(), 0)
call_2454 = relay.TupleGetItem(func_581_call(), 0)
func_2239_call = mod.get_global_var('func_2239')
func_2241_call = mutated_mod.get_global_var('func_2241')
call_2460 = func_2239_call()
call_2461 = func_2239_call()
output = relay.Tuple([call_2453,call_2460,])
output2 = relay.Tuple([call_2454,call_2461,])
func_2467 = relay.Function([], output)
mod['func_2467'] = func_2467
mod = relay.transform.InferType()(mod)
output = func_2467()
func_2468 = relay.Function([], output)
mutated_mod['func_2468'] = func_2468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_2543 = relay.TupleGetItem(func_957_call(), 0)
call_2544 = relay.TupleGetItem(func_958_call(), 0)
output = relay.Tuple([call_2543,])
output2 = relay.Tuple([call_2544,])
func_2546 = relay.Function([], output)
mod['func_2546'] = func_2546
mod = relay.transform.InferType()(mod)
output = func_2546()
func_2547 = relay.Function([], output)
mutated_mod['func_2547'] = func_2547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2321_call = mod.get_global_var('func_2321')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_2580 = func_2321_call()
call_2581 = func_2321_call()
output = relay.Tuple([call_2580,])
output2 = relay.Tuple([call_2581,])
func_2583 = relay.Function([], output)
mod['func_2583'] = func_2583
mod = relay.transform.InferType()(mod)
mutated_mod['func_2583'] = func_2583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2583_call = mutated_mod.get_global_var('func_2583')
call_2584 = func_2583_call()
output = call_2584
func_2585 = relay.Function([], output)
mutated_mod['func_2585'] = func_2585
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2586 = relay.var("var_2586", dtype = "float64", shape = (3, 9, 16))#candidate|2586|(3, 9, 16)|var|float64
uop_2587 = relay.rsqrt(var_2586.astype('float64')) # shape=(3, 9, 16)
func_1600_call = mod.get_global_var('func_1600')
func_1602_call = mutated_mod.get_global_var('func_1602')
call_2599 = relay.TupleGetItem(func_1600_call(), 0)
call_2600 = relay.TupleGetItem(func_1602_call(), 0)
bop_2605 = relay.bitwise_or(var_2586.astype('uint64'), relay.reshape(uop_2587.astype('uint64'), relay.shape_of(var_2586))) # shape=(3, 9, 16)
output = relay.Tuple([call_2599,bop_2605,])
output2 = relay.Tuple([call_2600,bop_2605,])
func_2610 = relay.Function([var_2586,], output)
mod['func_2610'] = func_2610
mod = relay.transform.InferType()(mod)
var_2611 = relay.var("var_2611", dtype = "float64", shape = (3, 9, 16))#candidate|2611|(3, 9, 16)|var|float64
output = func_2610(var_2611)
func_2612 = relay.Function([var_2611], output)
mutated_mod['func_2612'] = func_2612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2583_call = mod.get_global_var('func_2583')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_2683 = relay.TupleGetItem(func_2583_call(), 0)
call_2684 = relay.TupleGetItem(func_2585_call(), 0)
var_2685 = relay.var("var_2685", dtype = "float64", shape = (2, 16, 9))#candidate|2685|(2, 16, 9)|var|float64
bop_2686 = relay.bitwise_and(call_2683.astype('uint64'), relay.reshape(var_2685.astype('uint64'), relay.shape_of(call_2683))) # shape=(2, 16, 9)
bop_2689 = relay.bitwise_and(call_2684.astype('uint64'), relay.reshape(var_2685.astype('uint64'), relay.shape_of(call_2684))) # shape=(2, 16, 9)
output = relay.Tuple([bop_2686,])
output2 = relay.Tuple([bop_2689,])
func_2694 = relay.Function([var_2685,], output)
mod['func_2694'] = func_2694
mod = relay.transform.InferType()(mod)
var_2695 = relay.var("var_2695", dtype = "float64", shape = (2, 16, 9))#candidate|2695|(2, 16, 9)|var|float64
output = func_2694(var_2695)
func_2696 = relay.Function([var_2695], output)
mutated_mod['func_2696'] = func_2696
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2730 = relay.var("var_2730", dtype = "float32", shape = (9, 7, 9))#candidate|2730|(9, 7, 9)|var|float32
uop_2731 = relay.cosh(var_2730.astype('float32')) # shape=(9, 7, 9)
func_456_call = mod.get_global_var('func_456')
func_460_call = mutated_mod.get_global_var('func_460')
const_2743 = relay.const([[-2,3,4,6,-2,-7],[-7,-6,-9,9,-2,-2],[-1,3,-6,6,6,9],[-3,-7,4,-5,-3,9],[9,-7,10,2,-6,9],[-5,-9,-4,8,5,-4],[3,10,-8,10,-7,-10],[6,8,-10,3,-2,4],[-5,3,2,-9,-5,-3],[-9,4,-1,3,-8,-9],[-8,4,7,5,-2,9],[6,-9,10,5,4,-5],[4,2,1,-2,4,-8],[-2,2,-3,-10,-1,-9],[-10,10,4,8,-3,1],[4,2,7,-8,5,5],[-2,-5,3,-6,10,6],[9,-1,-6,4,-4,-7]], dtype = "int32")#candidate|2743|(18, 6)|const|int32
call_2742 = relay.TupleGetItem(func_456_call(relay.reshape(const_2743.astype('int32'), [3, 9, 4]), relay.reshape(const_2743.astype('int32'), [3, 9, 4]), ), 2)
call_2744 = relay.TupleGetItem(func_460_call(relay.reshape(const_2743.astype('int32'), [3, 9, 4]), relay.reshape(const_2743.astype('int32'), [3, 9, 4]), ), 2)
var_2747 = relay.var("var_2747", dtype = "float32", shape = (9, 7, 9))#candidate|2747|(9, 7, 9)|var|float32
bop_2748 = relay.add(var_2730.astype('int8'), relay.reshape(var_2747.astype('int8'), relay.shape_of(var_2730))) # shape=(9, 7, 9)
uop_2755 = relay.acos(uop_2731.astype('float64')) # shape=(9, 7, 9)
bop_2771 = relay.logical_and(uop_2755.astype('bool'), relay.reshape(uop_2731.astype('bool'), relay.shape_of(uop_2755))) # shape=(9, 7, 9)
bop_2776 = relay.mod(uop_2731.astype('float64'), relay.reshape(bop_2748.astype('float64'), relay.shape_of(uop_2731))) # shape=(9, 7, 9)
output = relay.Tuple([call_2742,const_2743,bop_2771,bop_2776,])
output2 = relay.Tuple([call_2744,const_2743,bop_2771,bop_2776,])
func_2787 = relay.Function([var_2730,var_2747,], output)
mod['func_2787'] = func_2787
mod = relay.transform.InferType()(mod)
var_2788 = relay.var("var_2788", dtype = "float32", shape = (9, 7, 9))#candidate|2788|(9, 7, 9)|var|float32
var_2789 = relay.var("var_2789", dtype = "float32", shape = (9, 7, 9))#candidate|2789|(9, 7, 9)|var|float32
output = func_2787(var_2788,var_2789,)
func_2790 = relay.Function([var_2788,var_2789,], output)
mutated_mod['func_2790'] = func_2790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_2792 = relay.TupleGetItem(func_957_call(), 0)
call_2793 = relay.TupleGetItem(func_958_call(), 0)
uop_2809 = relay.log2(call_2792.astype('float64')) # shape=(2, 16, 9)
uop_2811 = relay.log2(call_2793.astype('float64')) # shape=(2, 16, 9)
output = uop_2809
output2 = uop_2811
func_2813 = relay.Function([], output)
mod['func_2813'] = func_2813
mod = relay.transform.InferType()(mod)
output = func_2813()
func_2814 = relay.Function([], output)
mutated_mod['func_2814'] = func_2814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_2820 = relay.TupleGetItem(func_292_call(), 0)
call_2821 = relay.TupleGetItem(func_293_call(), 0)
output = relay.Tuple([call_2820,])
output2 = relay.Tuple([call_2821,])
func_2825 = relay.Function([], output)
mod['func_2825'] = func_2825
mod = relay.transform.InferType()(mod)
mutated_mod['func_2825'] = func_2825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2825_call = mutated_mod.get_global_var('func_2825')
call_2826 = func_2825_call()
output = call_2826
func_2827 = relay.Function([], output)
mutated_mod['func_2827'] = func_2827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_2837 = relay.TupleGetItem(func_1872_call(), 0)
call_2838 = relay.TupleGetItem(func_1874_call(), 0)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_2856 = relay.TupleGetItem(func_402_call(), 3)
call_2857 = relay.TupleGetItem(func_404_call(), 3)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
const_2868 = relay.const([-1,-10,5,-7,-2,-9,2,-4,-3,-9,-1,3,5,1,-3,3,-3,-4,-6,3,6,4,-7,10,1,4,2,-2,-7,10,-3,-3,-7,7,8,1,3,1,4,-9,-3,-6,10,9,-3,9,-2,-4,-1,-2,2,-4,7,-4,-9,7,-8,6,-3,7,-3,-1,1,4,8,-3,-9,5,2,-8,-4,2,10,-10,-2,8,-5,2,6,-8,-4,-5,9,1,-9,2,-6,5,-2,-6,2,-2,2,-3,-2,3,3,10,-7,-3,10,10,-2,1,-2,10,2,2,-8,4,-7,7,-4,2,-8,6,2,5,4,8,4,9,2,1,6,9,10,-3,-2,6,2,7,9,-8,7,-9,3,-8,1,4,-5,-3,10,-1,-3,-2,8,-10,3,-2,-5,-3,8,5,3,9,4,-4,7,9,-2,-6,-2,7,-8,6,-9,4,-2,-9,8,-4,-9,9,4,6,8,-4,10,-4,10,2,10,-9,4,-9,5,9,2,9,-3,-9,7,-9,-5,-5,-4,-6,-4,-9,4,-5,3,-2,9,8,6,-4,1,2,-8,-4,-6,9,7,8,-7,-10,-4,-5,6,6,-1,7,-6,1,-7,-8,-5,-1,-6,2,10,4,-4,9,-2,-4,-7,-6,-1,9,-2,-9,6,7,-8,5,-1,-6,-8,7,-3,-5,-3,5,8,1,1,-6,1,8,2,-1,-2,10,-3,-2,-7,7,9,-3,8,-6,-8,-5,-6,2,6,-3,-2,2,9,2,-2,7,4,8,-5,-8,-9,-2,8,4,-7,4,-1,5,-10,-5,9,-4,1,-3,-8,-9,-6,3,7,7,8,3,8,9,-6,-10,6,8,-8,6,-3,-7,8,-4,9,8,5,-7,9,10,-10,-2,8,8,10,4,-8,4,-10,2,-4,-9,2,-1,-1,8,-5,2,10,-1,-1,-8,7,9,-2,9,1,-4,-5,4,10,-9,-4,-8,10,-7,-6,2,-6,-1,1,-6,-9,7,-7,-1,-5,-2,1,1,9,2,4,-1,6,1,-3,2,-9,-7,10,-3,-6,1,-7,9,-4,-3,7,-9,5,2,6,9,3,-4,-4,9,4,-9,4,-6,1,5,3,-2,-5,-6,8,-8,3,-5,1,-9,4,5,-6,-6,-2,6,6,-6,2,-2,1,-3,-4,-3,2,9,8,4,8,-4,3,-8,9,10,9,-4,-3,-7,3,1,10,1,-5,5,-5,6,10,-4,9,2,7,-10,-1,5,-5,-1,-8,4,-7,7,-9,-9,6,-7,9,-4,-5,7,9,2,-10,-10,7,-10,-2,-6,9,-9,-1,1,-8,-8,-7,-9,-7,-10,-5,-5,-4,-7,-3,9,-10,-6,-7,-1,-10,-7,4,-3,8,9,-4,6,-7,-4,5,2,-2,-6,-7,-3,8,6,-8,4,-2,1,-5,-2,1,-5,-9,-10,7,-9,5,-1,-4,4,6,1,-10,2,3,-8,-1,-9,-9,-1,-6,-1,4,3,-9,-1,-6,-10,7,10,7,-2,-10,-9,1,7,2,-10,10,-4,4,-3,-10,-5,-7,8,-4,4,-3,-6,7,-6,1,-5,1,9,7,-6,-5,5,-7,-7,5,-6,8,-7,-5,-4,-10,9,-8,-7,-10,-1,3,10,1,2,1,-8,-1,-4,9,5,6,-3,2,-7,-4,-9,6,-8,7,7,-9,8,2,-8,-1,10,-7,-2,-4,3,-9,4,2,-4,-3,8,6,4,2,-8,-7,10,3,4,1,5,2,5,3,-4,2,10,1,-7,8,-6,6,-10,10,-10,5,-2,5,10,9,-6,-5,-9,10,9,-1,-2,3,-10,10,-5,-5,10,4,-10,4,-4,-2,-5,-8,8,-9,8,6,4,-10,-9,-6,5,-10,5,-10,-3,1,-3,-4,10,-5,5,8,5,2,1,6,-10,-10,10,-3,2,-5,-4,-10,-2,3,-6,9,-9,7,9,-7,-10,5,8,-7,5,-7,-8,-3,2,10,-9,9,-1,9,10,10,-2,1,4,-10,9,8,-4,8,1,6,-8,-9,1,-9,-1,-2,6,2,-3,-1,-8,10,3,10,7,-3,10,3,9,4,-3,-4,-2,-10,-7,-7,-9,-8,4,-6,3,5,-3,-5,-8,-4,-5,-1,7,2,-10,8,6,4,6,-1,9,-4,-2,-7,-10,-3,-1,2,6,1,-4,7,-7,-2,-1,3,8,-2,-6,5,10,-1,-4,9,10,6,-9,6,4,-10,-2,4,-8,-2,-5,-2,-7,-6,-7,-1,-4,-3,-1,-10,6,9,1,-9,2,-7,10,-2,2,8,-4,8,-5,3,-7,-1,3,2,5,-4,5,-4,1,-10,5,-4,-6,-10,-1,-6,-8,-5,9,4,1,3,-1,8,4,-5,-7,-9,-1,-5,4,3,10,-2,7,5,5,-1,4,8,-9,-6,-4,-1,-5,-9,10,2,2,-3,9,-7,5,-3,-1,-6,4,9,8,-4,8,4,9,-2,-10,-2,-10,-5,8,3,-9,-10,-10,2,10,-2,3,-10,2,5,-6,2,5,2,-7,3,-5,-10,5,-4,-10,-5,2,5,-7,7,7,-1,9,6,-8,2,5,8,-4,4,9,-8,9,7,6,-1,-3,5,-4,10,1,5,5,-5,6,-4,-3,3,8,7,-4,-6,9,-3,-2,4,4,-1,-3,-10,8,-1,4,10,-6,5,5,8,-3,-4,-3,-10,8,-8,10,9,9,8,3,-7,-4,8,-2,-3,5,-9,8,5,-3,-8,-10,8,4,-3,3,-8,2,8,10,8,9,-6,-9,2,6,4,6,5,7,8,10], dtype = "uint32")#candidate|2868|(1050,)|const|uint32
call_2867 = relay.TupleGetItem(func_2401_call(relay.reshape(const_2868.astype('uint32'), [10, 15, 7])), 0)
call_2869 = relay.TupleGetItem(func_2403_call(relay.reshape(const_2868.astype('uint32'), [10, 15, 7])), 0)
uop_2877 = relay.atanh(call_2856.astype('float64')) # shape=(2, 16, 9)
uop_2879 = relay.atanh(call_2857.astype('float64')) # shape=(2, 16, 9)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_2901 = relay.TupleGetItem(func_1433_call(), 0)
call_2902 = relay.TupleGetItem(func_1435_call(), 0)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_2912 = relay.TupleGetItem(func_1544_call(), 0)
call_2913 = relay.TupleGetItem(func_1545_call(), 0)
output = relay.Tuple([call_2837,call_2867,const_2868,uop_2877,call_2901,call_2912,])
output2 = relay.Tuple([call_2838,call_2869,const_2868,uop_2879,call_2902,call_2913,])
func_2927 = relay.Function([], output)
mod['func_2927'] = func_2927
mod = relay.transform.InferType()(mod)
mutated_mod['func_2927'] = func_2927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2927_call = mutated_mod.get_global_var('func_2927')
call_2928 = func_2927_call()
output = call_2928
func_2929 = relay.Function([], output)
mutated_mod['func_2929'] = func_2929
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2945 = relay.var("var_2945", dtype = "float64", shape = (3, 12, 13))#candidate|2945|(3, 12, 13)|var|float64
uop_2946 = relay.log(var_2945.astype('float64')) # shape=(3, 12, 13)
output = uop_2946
output2 = uop_2946
func_2948 = relay.Function([var_2945,], output)
mod['func_2948'] = func_2948
mod = relay.transform.InferType()(mod)
var_2949 = relay.var("var_2949", dtype = "float64", shape = (3, 12, 13))#candidate|2949|(3, 12, 13)|var|float64
output = func_2948(var_2949)
func_2950 = relay.Function([var_2949], output)
mutated_mod['func_2950'] = func_2950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_2991 = func_2813_call()
call_2992 = func_2813_call()
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_3000 = relay.TupleGetItem(func_1053_call(), 0)
call_3001 = relay.TupleGetItem(func_1054_call(), 0)
output = relay.Tuple([call_2991,call_3000,])
output2 = relay.Tuple([call_2992,call_3001,])
func_3004 = relay.Function([], output)
mod['func_3004'] = func_3004
mod = relay.transform.InferType()(mod)
mutated_mod['func_3004'] = func_3004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mutated_mod.get_global_var('func_3004')
call_3005 = func_3004_call()
output = call_3005
func_3006 = relay.Function([], output)
mutated_mod['func_3006'] = func_3006
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1210_call = mod.get_global_var('func_1210')
func_1212_call = mutated_mod.get_global_var('func_1212')
call_3069 = func_1210_call()
call_3070 = func_1210_call()
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_3074 = relay.TupleGetItem(func_2927_call(), 4)
call_3075 = relay.TupleGetItem(func_2929_call(), 4)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_3078 = relay.TupleGetItem(func_2825_call(), 0)
call_3079 = relay.TupleGetItem(func_2827_call(), 0)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_3081 = relay.TupleGetItem(func_957_call(), 0)
call_3082 = relay.TupleGetItem(func_958_call(), 0)
func_2370_call = mod.get_global_var('func_2370')
func_2374_call = mutated_mod.get_global_var('func_2374')
const_3088 = relay.const([-1,-1,-5,6,5,-3,7,-7,-3,-9,-5,-7,2,-10,-8,-5,3,7,-6,-7,3,1,-3,-2,-7,7,8,5,-7,-9,7,3,-9,7,7,10,5,10,10,-4,-5,-10,-5,2,-9,7,4,7,2,3,-9,9,-4,4,1,4,-9,8,1,-5,3,-8,4,2,-9,-5,-10,6,3,2,8,-1,-10,10,-3,2,9,-4,-3,-8,3,-5,-8,-9,-9,-9,6,-3,-1,8,9,1,-7,-10,-3,-5,2,1,8,-2,-2,-3,1,5,-8,7,10,-7,2,7,4,4,-1,7,-7,-6,10,-7,5,4,-4,1,8,1,5,-7,-2,-6,-4,-4,-4,9,-2,-6,8,-10,-2,6,-1,1,-9,-7,-7,-5,8,3,-10,3,-9,-8,-10,9,9,1,4,-6,-2,3,-5,-2,8,2,-10,-1,-5,-5,-5,-6,-10,6,3,-7,4,4,-8,4,-4,3,3,-2,-1,5,3,-4,-2,-9,2,-8,5,8,10,7,-8,7,-4,-2,-8,-5,-2,-4,-9,9,-8,-8,1,-6,5,5,8,5,-1,-9,5,9,-2,4,-7,-3,-10,-8,8,-1,1,-8,-8,-1,1,-9,1,-6,1,6,-2,3,-1,-2,8,2,9,-6,-5,5,6,-4,2,-2,9,10,-7,3,5,7,-9,3,-8,-5,8,9,-6,3,-3,10,2,-3,-5,9,10,-5,4,6,-7,-7,1,-8,-8,-4,5,3,5,8,-2,4,-2,2,-5,10,-9,8,2,6,9,1,5,-3,1,2,10,-5,3,8,6,-3,-4,7,-6,-8,-5,9,6,-10,-7,8,8,-10,3,-2,-8,5,3,2,5,4,-2,9,9,2,-4,1,-8,-5,-1,-1,2,-4,6,-6,-7,-2,-5,4,-2,8,-9,-10,-2,-7,1,-5,-1,-8,5,1,-4,9,-4,3,-1,4,2,6,-8,-8,-8,2,1,10,5,6,-4,1,9,-6,7,-10,-3,-4,7,9,-6,-9,-2,3,-10,-7,5,2,3,6,-9,10,1,2,9,-7,4,-2,-5,-4,-5,1,8,-5,3,-1,-8,-2,-7,8,8,9,-3,6,7,5,10,1,9,-9,7,-3,-2,-5,1,-3,1,1,-4,-2,-9,-2,-2,9,8,4,-9,-2,3,-10,-1,5,4,3,-5,10,1,4,-4,5,-2,-9,5,4,9,2,6,3,5,9,-3,3,2,7,10,-9,-10,-5,-2,-3,-2,2,-4,9,10,-9,-8,7,10,5,-6,4,5,-1,10,-7,-8,-2,3,-2,-1,6,-3,-9,-6,3,-1,10,-8,-2,-4,5,-9,6,8,4,7,9,2,-3,4,-2,4,-10,2,5,2,-10,6,-2,-2,-6,-8,-10,-2,-1,-8,-1,5,-7,7,5,-1,-10,-2,3,-1,-4,-5,9,7,6,-5,10,-2,8,-10,-7,-1,9,-9,7,1,-9,10,-6,2,-4,10,-6,10,10,-9,10,3,-3,-2,-4,-6,1,-5,-2,-8,-3,-8,-9,-4,-10,-5,5,10,4,-10,6,3,9,6,-6,-6,3,7,4,-10,-6,-5,-4,-9,-10,7,3,5,2,5,-6,-5,7,-10,7,5,6,4,-8,8,-2,-4,-9,-8,10,6,-4,-4,7,4,-5,-7,1,-1,-4,7,-8,-2,-9,7,-6,5,8,-5,-5,-8,7,1,7,-7,3,-9,-2,-9,5,-10,10,5,7,2,-6,-4,4,-1,7,1,1,-2,-3,5,6,-9,3,4,-3,-3,7,-1,3,1,7,2,4,-2,7,-4,-3,1,8,-7,2,-9,-9,9,10,4,5,-7,1,7,7,1,8,-5,7,-9,-3,-9,9,-6,1,-10,7,-5,-7,6,-6,3,1,10,1,1,8,-8,-10,-7,2,7,-7,8,7,-7,5,4,-9,7,4,3,8,8,-6,8,4,-7,-10,-4,-3,7,-2,-5,7,-2,2,2,9,-9,-7,-2,4,10,6,-10,-7,-8,-8,-2,7,-6,1,10,-8,-2,-5,3,-6,3,9,3,-10,6,6,-5,-4,-3,-8,5,-1,8,1,-5,-6,-9,4,2,-4,2,-6,2,-9,-5,7,1,-6,4,-2,-4,-9,-3,6,-5,-4,10,-7,2,-7,-10,-4,4,2,7,9,10,8,-1,1,-5,-6,-6,7,-6,2,3,-9,-8,-5,2,-10,-3,10,-3,9,-7,-2,7,-1,-6,-1,1,-5,10,7,5,-8,4,-10,8,-4,4,10,-5,-4,-3,9,-4,6,6,8,9,-8,4,9,-9,9,-8,5,-9,8,6,8,4,6,7,9,-1,-8,-9,1,9,1,10,-5,-9,-10,10,4,2,-2,-7,-5,-2,-5,10,-6,7,-8,-7,5,4,8,-3,-8,4,6,-2,10,-3,-2,-3,2,10,-9,3,-3,-9,-2,5,9,-1,1,-3,-7,7,9,-2,2,-3,8,-2,6,2,-4,-10,-6,-8,-6,7,-7,-7,-4,9,10,6,-1,-1,-2,5,-9,8,7,2,7,9,4,2,4,6,5,-5,2,3,10,9,4,7,-3,9,8,6,5,-2,1,-4,-9,5,7,-5,-8,8,-2,-5,2,5,-1,2,10,4,1,10,-1,3,-2,6,-3,-2,-9,-9,1,1,-6,-10,8,-10,4,-2,4,4,4,-4,4,3,4,-4,-8,9,-9,-4,4,9,1,-4,7,-1,-6,7,2,3,1,-3,2,7,-2,10,3,4,1,1,4,6,-8,1,-4,-7,10,6,-3,-3,1,9,-3,8,-2,9,-10,7,-9,-9,3,-7,-6,-4,5,-4,-1,2,7,-7,10,5,2,-9,2,-5,4,7,7,10,1,10,-6,-7,4,-2,-3,-4,8,-7,1,-5,-5,6,-6,-6,8,-10,-10,-7,-2,-9,-5,9,6,6,-7,2,-5,-6,5,-9,-9,7,-7,-6,-5,-3,5,4,9,9,-2,10,9,10,7,7,10,7,-10,8,7,-4,5,-6,-1,-2,5,-10,-7,10,-2,2,-1,-9,4,-6,9,5,-1,10,-5,-5,-4,9,-5,-7,-6,-9,10,9,5,6,9,-10,4,2,-4,-2,-10,-2,-9,-4,-10,3,-10,7,-2,-1,-6,-9,3,-10,6,9,-2,-3,-2,8,-9,-5,5,-4,6,-8,-8,-3,-10,-10,-4,4,-10,8,5,7,7,5,-3,-1,-4,-3,5,3,-8,4,2,1,9,7,5,10,-5,4,-3,6,3,10,-5,5,-8,9,-9,3,10,-1,-5,7,-7,-7,-5,8,2,5,-10,5,1,7,6,5,-3,1,9,-5,6,-5,-5,-10,-2,8,-7,-10,-9,-6,1,1,10,-10,-9,-5,7,7,-4,10,-1,-8,1,7,-6,-5,8,9,-7,7,5,2,-4,5,5,4,4,-6,-9,-7,8,10,-7,4,-1,1,-4,8,-1,6,8,1,1,7,10,4,5,6,4,-9,2,3,-4,-6,3,10,-3,5,8,-3,-5,8,1,-5,5,-2,-5,-5,-5,3,-4,-1,-6,2,-10,6,-3,7,-10,3,-6,4,-1,10,1,-5,-10,5,-5,-2,3,-10,2,-2,-2,10,9,9,3,5,-7,-1,9,3,-3,8,-4,-4,-8,1,-9,-7,-4,-6,8,-3,2,-1,1,4,10,-4,2,1,2], dtype = "int8")#candidate|3088|(1386,)|const|int8
call_3087 = relay.TupleGetItem(func_2370_call(relay.reshape(const_3088.astype('int8'), [9, 14, 11]), relay.reshape(const_3088.astype('int8'), [9, 14, 11]), ), 0)
call_3089 = relay.TupleGetItem(func_2374_call(relay.reshape(const_3088.astype('int8'), [9, 14, 11]), relay.reshape(const_3088.astype('int8'), [9, 14, 11]), ), 0)
output = relay.Tuple([call_3069,call_3074,call_3078,call_3081,call_3087,const_3088,])
output2 = relay.Tuple([call_3070,call_3075,call_3079,call_3082,call_3089,const_3088,])
func_3102 = relay.Function([], output)
mod['func_3102'] = func_3102
mod = relay.transform.InferType()(mod)
output = func_3102()
func_3103 = relay.Function([], output)
mutated_mod['func_3103'] = func_3103
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3192 = relay.const(10, dtype = "uint64")#candidate|3192|()|const|uint64
var_3193 = relay.var("var_3193", dtype = "uint64", shape = (10, 12, 5))#candidate|3193|(10, 12, 5)|var|uint64
bop_3194 = relay.bitwise_or(const_3192.astype('uint64'), var_3193.astype('uint64')) # shape=(10, 12, 5)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_3197 = func_1940_call()
call_3198 = func_1940_call()
output = relay.Tuple([bop_3194,call_3197,])
output2 = relay.Tuple([bop_3194,call_3198,])
func_3202 = relay.Function([var_3193,], output)
mod['func_3202'] = func_3202
mod = relay.transform.InferType()(mod)
var_3203 = relay.var("var_3203", dtype = "uint64", shape = (10, 12, 5))#candidate|3203|(10, 12, 5)|var|uint64
output = func_3202(var_3203)
func_3204 = relay.Function([var_3203], output)
mutated_mod['func_3204'] = func_3204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2321_call = mod.get_global_var('func_2321')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_3206 = func_2321_call()
call_3207 = func_2321_call()
output = relay.Tuple([call_3206,])
output2 = relay.Tuple([call_3207,])
func_3214 = relay.Function([], output)
mod['func_3214'] = func_3214
mod = relay.transform.InferType()(mod)
output = func_3214()
func_3215 = relay.Function([], output)
mutated_mod['func_3215'] = func_3215
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2321_call = mod.get_global_var('func_2321')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_3277 = func_2321_call()
call_3278 = func_2321_call()
output = relay.Tuple([call_3277,])
output2 = relay.Tuple([call_3278,])
func_3289 = relay.Function([], output)
mod['func_3289'] = func_3289
mod = relay.transform.InferType()(mod)
output = func_3289()
func_3290 = relay.Function([], output)
mutated_mod['func_3290'] = func_3290
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_3346 = relay.TupleGetItem(func_1872_call(), 0)
call_3347 = relay.TupleGetItem(func_1874_call(), 0)
output = call_3346
output2 = call_3347
func_3356 = relay.Function([], output)
mod['func_3356'] = func_3356
mod = relay.transform.InferType()(mod)
output = func_3356()
func_3357 = relay.Function([], output)
mutated_mod['func_3357'] = func_3357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_3379 = func_1940_call()
call_3380 = func_1940_call()
output = relay.Tuple([call_3379,])
output2 = relay.Tuple([call_3380,])
func_3389 = relay.Function([], output)
mod['func_3389'] = func_3389
mod = relay.transform.InferType()(mod)
output = func_3389()
func_3390 = relay.Function([], output)
mutated_mod['func_3390'] = func_3390
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_3430 = relay.TupleGetItem(func_1544_call(), 0)
call_3431 = relay.TupleGetItem(func_1545_call(), 0)
func_3202_call = mod.get_global_var('func_3202')
func_3204_call = mutated_mod.get_global_var('func_3204')
const_3449 = relay.const([3,4,10,6,3,4,-9,7,7,8,-4,2,5,-1,10,10,6,1,-10,-7,9,4,-2,-3,10,-9,-6,-6,-6,-1,1,-10,-5,-6,-5,9,6,-5,-4,-7,2,1,-6,-7,3,1,-9,-2,1,9,-3,-2,-2,9,-7,-2,-2,-7,7,-5,1,-6,-6,-5,8,-4,4,2,-5,4,7,1,7,2,-1,6,-2,2,-3,-6,1,-2,6,-3,-4,2,-10,-1,-10,-3,-9,-3,-3,8,4,-5,-1,-1,2,7,8,-7,2,-7,10,-5,1,9,-5,-8,-10,3,3,-10,8,10,7,-6,3,5,-3,2,8,-8,8,-1,10,-2,10,7,-9,3,2,7,3,1,-2,-2,6,-5,-7,-5,-2,1,10,7,-4,-5,2,-4,-6,2,1,10,3,6,-2,6,-9,-6,-4,-6,5,-5,-5,-1,5,1,-7,-5,-4,10,-1,2,3,9,-10,4,-8,2,9,6,-1,9,-8,8,-5,-2,3,6,-9,-3,-10,4,-7,3,4,-9,-10,2,-5,2,7,6,-5,7,-7,-2,-9,-9,5,-4,3,3,-6,-1,-5,10,-8,-3,-1,6,-5,9,7,2,-9,-10,-2,8,-7,-8,4,4,6,-5,-10,-5,1,10,-1,9,-1,-2,1,-2,9,-1,-7,6,-4,10,-4,-10,-10,-3,3,9,-1,8,3,10,-9,6,10,9,3,-10,6,-1,10,-7,4,-8,1,6,-5,5,-1,-10,-2,-5,-10,-3,-4,-5,8,9,10,-8,-1,-2,-3,10,9,-5,9,-8,-4,5,5,2,2,5,7,2,8,-6,-2,-6,-4,-1,-10,2,-10,-10,7,-8,3,2,7,-10,7,-5,-10,-9,2,9,-1,-6,10,-7,9,-5,-7,10,10,-8,-6,7,3,-2,7,7,-4,10,8,-10,-1,9,3,-3,-1,-9,1,3,-3,-9,8,-10,-8,6,-8,-4,1,-8,-5,7,-9,1,4,7,8,-10,3,-9,-2,8,-1,-8,8,-9,6,-8,-6,-8,4,-10,1,-1,1,5,6,3,10,4,-9,2,10,-2,-1,-9,-6,-7,10,-3,-9,6,6,5,-1,5,-1,-5,6,-9,8,4,-8,2,1,3,-6,5,6,-7,10,-7,6,6,-9,-3,-5,-2,-5,5,10,6,-4,-7,5,-1,3,-8,10,-4,-8,-8,1,-8,-4,4,10,1,3,8,1,10,7,-4,-1,8,3,-4,5,1,-6,3,-5,10,2,3,-5,-7,3,1,-8,-7,4,5,5,7,1,7,-6,-3,5,2,-2,-4,10,3,4,-1,1,-6,-2,-10,-4,-2,-4,-9,-2,2,-1,1,2,9,1,-6,6,1,-6,-4,7,-3,10,1,2,-7,10,4,9,-9,5,-5,9,2,6,-6,-9,-4,-10,2,8,6,-5,-1,-8,-7,8,-6,9,-10,2,-7,-6,2,8,1,1,-6,-10,3,9,-10,5,2,4,8,-2,8,8,8,-4,-3,-8,1,4,-7,5,10,3,-3,-5,-2,-8,9,-10,3,5,9,3,-3,-6,-1,-8,-1,2,8,7,-8,-2,-10,-1,-6,-8,-2,-5,-7], dtype = "uint64")#candidate|3449|(600,)|const|uint64
call_3448 = relay.TupleGetItem(func_3202_call(relay.reshape(const_3449.astype('uint64'), [10, 12, 5])), 1)
call_3450 = relay.TupleGetItem(func_3204_call(relay.reshape(const_3449.astype('uint64'), [10, 12, 5])), 1)
func_580_call = mod.get_global_var('func_580')
func_581_call = mutated_mod.get_global_var('func_581')
call_3469 = relay.TupleGetItem(func_580_call(), 0)
call_3470 = relay.TupleGetItem(func_581_call(), 0)
func_2948_call = mod.get_global_var('func_2948')
func_2950_call = mutated_mod.get_global_var('func_2950')
var_3472 = relay.var("var_3472", dtype = "float64", shape = (468, 1))#candidate|3472|(468, 1)|var|float64
call_3471 = func_2948_call(relay.reshape(var_3472.astype('float64'), [3, 12, 13]))
call_3473 = func_2948_call(relay.reshape(var_3472.astype('float64'), [3, 12, 13]))
func_1652_call = mod.get_global_var('func_1652')
func_1654_call = mutated_mod.get_global_var('func_1654')
call_3475 = relay.TupleGetItem(func_1652_call(), 1)
call_3476 = relay.TupleGetItem(func_1654_call(), 1)
uop_3483 = relay.sigmoid(const_3449.astype('float32')) # shape=(600,)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_3485 = relay.TupleGetItem(func_1872_call(), 0)
call_3486 = relay.TupleGetItem(func_1874_call(), 0)
output = relay.Tuple([call_3430,call_3448,call_3469,call_3471,var_3472,call_3475,uop_3483,call_3485,])
output2 = relay.Tuple([call_3431,call_3450,call_3470,call_3473,var_3472,call_3476,uop_3483,call_3486,])
func_3488 = relay.Function([var_3472,], output)
mod['func_3488'] = func_3488
mod = relay.transform.InferType()(mod)
mutated_mod['func_3488'] = func_3488
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3489 = relay.var("var_3489", dtype = "float64", shape = (468, 1))#candidate|3489|(468, 1)|var|float64
func_3488_call = mutated_mod.get_global_var('func_3488')
call_3490 = func_3488_call(var_3489)
output = call_3490
func_3491 = relay.Function([var_3489], output)
mutated_mod['func_3491'] = func_3491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_581_call = mutated_mod.get_global_var('func_581')
call_3524 = relay.TupleGetItem(func_580_call(), 0)
call_3525 = relay.TupleGetItem(func_581_call(), 0)
output = call_3524
output2 = call_3525
func_3541 = relay.Function([], output)
mod['func_3541'] = func_3541
mod = relay.transform.InferType()(mod)
output = func_3541()
func_3542 = relay.Function([], output)
mutated_mod['func_3542'] = func_3542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_3552 = relay.TupleGetItem(func_1733_call(), 0)
call_3553 = relay.TupleGetItem(func_1735_call(), 0)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_3595 = func_270_call()
call_3596 = func_270_call()
func_1278_call = mod.get_global_var('func_1278')
func_1284_call = mutated_mod.get_global_var('func_1284')
var_3624 = relay.var("var_3624", dtype = "uint64", shape = ())#candidate|3624|()|var|uint64
const_3625 = relay.const([-3,9,-8,7,-2,2,-8,5,5,10,-10,3,10,1,-8,2,-5,9,7,-3,-6,10,-7,-3,-8,6,-2,4,-7,-7,-7,-6,-1,6,-10,7,-3,7,-4,2,-3,-10,7,6,-8,1,-3,10,10,4,-4,-6,-1,-8,-3,-7,-1,1,2,4,-2,7,-9,-1,-2,9,-9,-4,-7,-3,7,7,8,5,-5,10,-3,-3,4,1,1,2,6,8,8,-6,-3,2,10,9,-8,3,8,4,-1,5,-7,-2,3,-10,3,-8,8,-8,-9,4,-8,7,-4,-7,5,9,-9,9,-2,4,5,-2,4,-9,-8,8,-1,-3,7,-2,-4,-6,-3,-6,4,-10,4,1,-3,10,-5,-9,-7,-3,-4,5,-7,10,6,3,-8,8,-7,1,-1,-3,-1,-3,7,-1,5,7,-8,10,-5,-5,-9,8,-2,-8,-1,-9,3,1,2,-1,1,-6,6,-3,2,5,-1,-7,-1,-7,-6,-5,10,1,9,6,-1,-8,-10,-8,-9,4,-10,-4,-8,5,7,4,-7,9,8,-5,8,6,4,-2,10,4,7,-1,1,10,6,-7,-1,-9,2,10,7,9,1,-8,-5,3,4,-8,9,-5,2,-8,-8,5,-2,1,-2,-3,-10,-6,-5,9,-2,-4,-5,-8,1,-3,4,3,5,-7,2,2,3,7,8,7,4,-2,10,-7,7,-4,-10,-9,8,-1,-6,-4,-2,6,8,-9,5,-1,-1,-6,10,9,6,4,4,6,-10,-8,3,10,7,4,-1,5,-7,10,2,9,9,-1,1,-2,10,-1,4,-4,3,1,5,5,8,9,-5,7,2,-9,-7,-1,-3,-10,6,-7,2,-10,-5,-8,10,-4,-6,1,1,10,-2,-9,-3,-3,-2,7,-10,4,-4,10,-2,9,5,5,-3,-8,-5,-10,-5,-9,-3,3,-5,-9,-9,-3,3,-10,-5,8,1,-10,10,-7,5,2,-4,3,3,-10,-1,5,6,-6,-10,6,-8,-8,-10,-5,-10,-3,3,-6,8,-9,7,-6,-9,4,7,-1,-8,-5,-3,-3,1,-9,-2,1,9,2,7,-10,10,-6,-4,2,-5,10,1,-2,9,-7,4,-4,1,10,-4,4,6,9,-6,-4,1,-10,-7,-5,4,1,9,3,-1,-7,5,7,1,1,-10,-10,-9,1,3,-4,7,4,-1,7,-2,-5,8,-8,9,-8,-6,-7,-1,3,-6,2,2,-9,-5,-3,3,-3,1,3,5,-8,-2,-8,-5,6,7,5,5,4,-2,-6,6,-7,-5,4,2,10,7,6,8,3,1,7,-2,8,8,9,5,9,-8,9,7,3,-5,5,-2,-9,6,1,-6,2,-2,8,-8,-9,-1,6,6,-3,-10,-4,-9,-7,6,-5,-6,-6,9,-10,-10,3,7,-1,-1,-4,3,3,-1,-10,-10,-1,3,7,-1,9,7,-5,3,7,-10,-7,1,8,-2,-10,1,-9,1,6,-6,-5,1,7,-8,10,-7,3,-6,-9,7,-1,3,7,-9,-5,-10,-7,-2,6,7,8,-4,-2,-1,-1,4,-1,3,2,10,6,-10,2,-7,10,6,-10,8,-3,6,-9,5,7,7,1,-7,-7,1,-6,10,4,5,-8,-7,2,-4,-2,-3,8,-8,-7,-7,-1,6,9,-5,-3,7,3,-4,-5,-10,-1,8,2,10,5,6,8,-5,-9,7,3,7,6,-5,-2,-10,7,-4,-7,10,2,8,-9,6,-5,2,-7,-6,-2,7,-5,9,-6,2,-5,-5,-10,8,8,-9,-9,1,-2,10,-9,8,-6,7,-9,-7,-3,3,7,-3,7,8,-7,-1,-7,2,8,9,8,7,-4,2,-7,9,8,9,-7,3,-7,2,-5,-7,6,-8,1,-2,10,-2,-10,-2,-6,8,-9,7,5,-7,6,5,1,8,1,-9,-3,7,-4,6,2,-3,-2,5,10,8,-10,-9,10,-5,7,-1,4,8,7,-8,-7,-9,1,-8,10,8,1,-10,-7,2,-8,-6,1,2,7,8,-1,3,-3,-5,-7,2,2,-8,9,-5,-3,1,5,1,-3,4,-3,8,-7,10,7,1,4,-10,-1,9,-6,-7,6,-10,4,5,-2,5,7,3,-7,-3,6,-5,-8,3,7,-4,-6,3,10,-9,-2,-2,-2,-3,1,-2,-3,6,-3,5,6,4,4,4,-7,8,9,-8,-7,10,1,5,-2,3,-9,-7,10,9,-1,9,5,-7,7,5,-8,-10,-8,-1,7,6,-6,10,-6,-1,-3,-7,6,-3,1,5,-3,-10,-3,3,-9,-5,-4,1,6,-9,2,7,3,-1,10,-6,4,-5,-1,4,-7,-4,-5,-3,9,-2,-9,9,1,-8,7,-3,2,-7,-8,4,9,8,-5,7,-4,-6,-7,7,-6,-8,-9,-5,1,-3,-2,-4,-4,-7,5,6,-2,-2,-9,9,-4,-2,8,-3,7,5,2,2,-6,-9,-4,8,-9,-7,9,-6,2,3,5,-8,1,-4,5,-3,5,-9,6,5,10,-4,9,-2,-9,-1,-3,7,-4,-1,6,-9,-5,-2,-10,8,10,-8,3,-1,9,7,3,-9,4,6,-5,5,-7,-3,-3,-4,-5,5,4,-2,-10,-6,2,1,-7,-8,-4,-2,-9,6,8,-6,-4,-4,-6,3,3,10,7,3,-10,6,-5,5,-5,-5,-10,-7,9,5,8,-3,9,8,7,-10,4,9,6,3,-4,4,9,-10,-5,-4,-3,3,2,-8,5,-4,-5,10,6,1,-2,-5,8,-1,-10,-3,-4,5,-10,-3,-2,-3,9,-6,-7,-8,-4,1,-8,-7,7,-3,8,7,2,10,6,-9,-7,3,-6,2,-3,3,5,-2,-2,5,3,-6,1,-7,1,3,4,1,-6,9,-8,-1,-4,7,-7,6,4,3,9,-6,7,-10,7,1,8,3,4,-1,8,-6,2,-3,5,-4,7,7,-9,-6,-2,-2,-7,-6,-10,3,7,-2,-1,-5,-2,-1,9,4,-6,-4,7,9,-10,7,6,-9,7,-1,-8,-5,5,3,5,-2,8,-1,2,1,9,-6,-5,-7,8,-5,2,1,7,1,-1,-6,9,-6,-1,6,4,-4,-7,-3,9,-3,9,8,8,-9,2,-10,5,5,2,6,3,4,1,7,5,-2,-6,10,2,4,5,7,7,-5,-3,-4,-1,6,-4,-3,-5,-3,5,-6,3,3,2,-9,1,-10,5,1,-10,9,4,-7,4,1,-5,8,-6,7,10,9,-2,-8,-4,-2,-7,-2,-2,9,9,9,6,-2,-6,-10,-9,-8,9,7,-6,-8,1,-6,-7,10,5,-9,-7,-3,4,-9,-2,1,6,3,-8,-5,-10,-1,-7,4,2,-3,6,2,-9,2,-2,3,10,8,-8,6,-5,7,-2,4,-4,-3,-4,2,-9,-7,5,9,-7,-5,1,2,-10,9,-2,6,-1,8,-5,3,5,5,1,9,-10,-2,6,8,-5,-8,2,-4,-4,-10,-5,2,-2,-1,-10,10,5,-10,8,-8,7,-1,-1,-1,9,3,4,-5,-4,-1,7,4,-3,-2,4,-5,6,-9,-1,2,-2,6,-4,-4,7,5,-9,5,-5,5,5,-10,6,-7,-10,8,8,7,5,2,-9,8,-6,-1,10,-2,-6,7,2,10,7,-3,10,-6,-5,8,5,-3,-1,-2,10,7,6,9,-1,1,7,-2,-6,-3,-7,7,9,3,-4,-10,-8,-2,2,-6,2,-1,-1,-5,1,2,-9,2,-6,-7,-1,-5,-5,-5,10,-9,9,1,-3,9,-6,-4,7,-4,-10,-3,7,9,-5,-8,6,-9,-7,4,-9,-4,5,10,3,-7,5,3,10,-4,8,1,-9,-8,-9,6,5,-2,7,4,-8,-2,-3,-4,9,-7,2,-1,-8,-7,1,-6,-3,-9,-2,10,-4,-4,-9,9,8,7,5,3,6,10,-5,-4,-7,-7,-5,-1,-1,-7,3,10,-5,-3,6,-4,6,-10,2,-7,6,-8,-5,2,-1,-6,-7,6,-5,2,5,-4,2,1,-7,-1,-4,-5,-9,5,-8,-4,9,-8,-1,6,8,6,-3,2,-5,4,-3,10,-8,3,6,-2,9,9,-2,-5,-6,-8,6,-10,4,-2,-3,-10,5,-6,1,8,-9,10,-6,2,6,3,-10,2,-7,5,-7,10,8,-7,-3,9,-1,-3,-5,-9,5,-2,-4,-10,-1,2,10,1,7,7,2,4,-8,-2,-2,-4,4,-3,-10,-1,10,10,3,-7,1,2,3,-9,-3,-4,2,3,3,4,8,8,-9,9,-2,-4,-2,10,-2,-8,10,1,1,-1,7,2,3,7,-8,3,1,-7,-6,10,-6,5,2,1,8,-8,7,4,9,1,-6,-9,4,3,3,-9,4,6,-10,7,-8,4,-4,5,-2,3,1,-6,-8,-6,-4,1,-9,-2,-3,-6,4,6,10,3,6,-9,-8,1,-6,8,-9,6,5,6,6,8,-4,2,-6,8,-3,-8,-4,8,3,1,-6,-4,6,-10,2,4,2,1,-3,9,-6,6,5,1,1,-4,9,-7,-7,-7,4,-6,9,6,4,5,-4,1,4,-7,-6,-1,6,1,-6,-2,-2,-1,-6,1,4,-2,-9,-6,-7,-10,-4,7,1,-5,6,9,6,7,7,-1,-7,9,-8,-1,-10,5,1,3,-9,1,6,3,8,-3,1,-7,-1,-4,-1,-3,7,-4,1,2,-8,7,-1,-7,2,7,7,4,10,6,-5,2,-6,-10,-8,7,3,1,4,-4,-9,2,3,-4,3,4,-7,-8,7,-10,-8,10,-10,-5,8,-1,-10,-2,6,-8,6,-7,-2,-7,-2,-3,-3,2,-3,-8,-8,-7,3,-5,-5,-9,7,-5,-10,-8,-7,-1,-4,-6,1,10,-4,-2,-8,7,8,-6,2,3,-2,-4,-2,1,-9,-4,2,4,1,-4,-10,2,-9,-4,10,4,-10,2,5,-9,10,-9,-7,8,-8,5,-3,8,7,-4,-1,8,-7,7,-4,6,-10,-6,-7,-5,7,3,-8,4,4,10,-6,-1,9,-3,-2,6,-6,-9,9,10,-3,-7,-5,-6,-9,-6,-7,6,-3,-10,1,-9,8,-2,3,4,4,-8,-2,-7,3,6,10,-7,-4,-10,-2,-4,8,-9,9,-8,5,-3,10,-10,3,4,-9,-6,9,9,-4,4,-2,-2,8,-3,6,10,6,-3,-5,2,-10,-8,-6,-2,2,2,-3,-5,4,4,4,10,-3,10,-9,-3,-3,-2,9,-9,2,-5,8,5,-7,-4,2,-2,-4,-4,-7,6,1,-10,1,-1,3,-9,-3,-2,3,3,9,-2,-10,-10,5,-8,3,7,9,9,2,-4,-2,7,-2,1,-6,6,9,-4,1,3,1,-10,-5,-4,-6,-4,-5,-6,-3,-2,-1,-4,6,9,9,-1,-9,1,-9,5,-3,8,1,-9,-4,-3,9,7,7,-3,7,9,7,4,-6,5,-7,9,8,4,9,9,9,5,2,-4,-4,-7,-4,-8,7,10,-8,-5,1,2,-9,9,-9,-3,2,1,2,-8,-6,-7,-2,8,7,10,-5,9,-3,1,3,-2,3,1,-1,4,-5,-10,-9,1,-6,-6,-3,-4,-1,8,-10,9,6,-1,-10,4,-7,4,-7,-3,-6,-1,-4,-7,9,-9,8,4,-9,-2,-1,6,-3,3,-5,-2,-5,-2,-9,4,-4,8,-4,-7,7,-3,6,-6,10,-8,8,-8,2,-4,6,-8,4,4,8,2,-3,-4,4,7,-1,-9,-6,4,6,8,7,-4,-3,10,2,-7,-6,-3,2,4,-8,2,1,-9,-3,9,-4,-2,1,-10,-1,7,9,10,3,-3,-7,2,-1,5,9,-6,6,2,8,-2,9,8,3,-9,2,-5,7,8,-8,3,-6,-2,7,-4,6,-5,7,-2,1,-5,5,1,9,1,-2,-7,-5,1,-3,-8,10,5,-7,10,-10,1,6,7,-1,3,5,10,-10,-4,7,-3,7,6,7,-2,-2,-2,6,4,-10,-9,-8,6,3,3,6,-8,-6,-7,-10,-7,3,-1,-9,-4,-3,-5,-5,10,-5,-7,1,-1,10,9,6,-4,-7,6,1,6,-5,6,-2,-8,-1,5,10,10,-6,2,5,3,-3,10,10,-8,5,-7,-10,3,9,5,7,-3,-2,-7,3,1,-8,7,-4,-5,9,-7,6,-2,1,-6,3,-1,6,-6,-7,-2,7,-5,6,-2,-1,-6,1,3,7,10,1,-7,-9,-4,7,5,7,6,1,10,1,10,6,-3,5,5,5,10,2,-4,2,-4,9,-6,-10,-4,-4,2,-10,-5,10,-8,9,-3,-4,1,-6,6,-6,8,9,-8,8,3,7,-2,9,4,-10,10,-3,9,-7,-5,-5,9,-4,-7,7,2,-9,10,6,7,-2,7,7,5,9,6,-2,8,-2,-2,-4,-2,9,-10,-8,1,3,5,4,-5,-9,-8,8,1,-2,8,7,8,3,-1,6,-3,9,-2,-6,-7,8,8,-1,5,-9,-9,4,-2,-9,10,-6,6,-10,8,5,-3,-1,8,-9,7,-5,-4,-6,-8,1,2,-10,3,-7,4,-8,-7,-7,3,8,-3,8,4,8,-1,-9,-8,-3,6,4,4,-8,-3,5,-10,9,8,3,-3,5,1,9,10,10,2,6,10,-6,-9,-2,-4,4,-8,5,9,-7,1,-8,8,8,6,5,-8,-8,9,-7,8,-6,-10,8,-10,-8,1,-3,5,-8,-5,-4,3,1,-3,9,-2,10,6,1,-4,-9,4,3,-3,-10,-5,3,-10,4,-7,-5,-7,-10,2,9,10,-1,9,-8,7,3,4,-2,4,-6,-8,-9,5,-6,-1,-2,-4,-9,-7,7,5,-7,-10,3,-4,3,1,7,-1,4,-9,-5,9,5,-1,1,-4,4,9,8,-8,7,4,7,6,-7,8,-7,-8,-5,5,-4,4,5,-5,9,5,-5,8,4,3,-1,5,-8,-10,-1,-8,-8,-3,8,-5,1,10,8,-8,-4,-4,-2,2,-4,-2,9,-10,-2,9,10,6,-5,9,-4,8,10,2,-2,3,-7,1,-6,-5,5,-10,-10,-8,3,-2,8,5,-1,1,9,9,10,-4,-10,-7,-4,10,5,3,-9,3,5,5,-4,9,-2,-1,-8,-3,5,3,-8,7,3,1,5,9,-1,3,-3,-1,1,-1,9,7,-3,7,-3,5,2,-10,-10,-4,7,10,-2,-7,3,1,-10,-7,-7,6,-7,-10,9,-6,2,1,9,-9,2,-3,-4,8,1,10,-10,-1,-7,9,-10,-6,7,2,-9,-9,9,-8,8,-10,1,-10,4,1,-10,-9,5,5,-3,10,-9,4,4,-10,6,-1,8,10,-3,-7,-9,-5,2,-8,8,8,8,-5,4,5,5,-8,7,9,9,5,2,4,-2,8,2,-9,-8,5,4,-1,-7,-4,-7,6,-10,-5,3,-6,-4,6,10,10,-4,7,6,6,7,2,4,-1,9,7,-7,-6,7,1,-1,-5,-8,2,-2,-9,-8,-4,-1,9,3,1,-8,3,2,5,4,8,-4,-8,-7,-7,10,-1,8,-10,-7,3,1,-3,1,-6,-1,9,-3,4,-5,-8,4,-5,-1,-5,9,4,-7,3,-6,-5,3,2,10,-9,7,-2,-7,5,-6,-6,2,5,6,7,6,7,-5,-7,-5,2,4,-4,2,10,-2,1,6,-1,-3,-2,-10,8,10,-10,2,6,5,8,9,-3,4,-3,1,3,-2,-3,-6,6,8,10,8,-7,-7,-8,3,-7,7,-7,6,2,-5,-10,8,8,4,10,-7,4,-2,-2,6,-1,-1,-1,8,-7,-10,7,-7,-6,4,-2,4,7,-10,10,10,7,2,2,-1,5,8,-9,-7,-5,-4,-4,-4,-4,-3,8,-8,7,-5,1,8,9,-6,-10,-7,5,-1,-10,1,-9,10,10,-6,-9,-7,-9,4,2,8,4,6,-7,-8,2,-10,-6,10,-8,2,-9,8,4,8,6,8,3,9,1,-8,-9,-7,9,-8,6,-4,10,3,-8,2,8,1,-5,3,10,-2,10,-1,-7,-5,2,5,3,-6,10,-4,9,10,-8,10,4,6,-1,2,7,-10,1,10,5,5,-5,2,6,8,4,-1,-1,-4,-3,10,-8,-10,-8,-2,-10,8,8,9,-3,8,-4,8,6,-8,10,1,-8,4,-5,9,-3,-1,7,5,-5,-7,-3,-4,7,-8,-10,5,-1,-6,-7,-10,-9,3,8,-4,-2,6,6,-4,4,9,2,3,-5,8,3,-2,8,8,3,3,-5,-3,-8,1], dtype = "uint64")#candidate|3625|(3136,)|const|uint64
call_3623 = relay.TupleGetItem(func_1278_call(relay.reshape(call_3595.astype('float64'), [2, 16, 9]), relay.reshape(var_3624.astype('uint64'), []), relay.reshape(const_3625.astype('uint64'), [196, 16]), relay.reshape(const_3625.astype('uint64'), [196, 16]), ), 2)
call_3626 = relay.TupleGetItem(func_1284_call(relay.reshape(call_3595.astype('float64'), [2, 16, 9]), relay.reshape(var_3624.astype('uint64'), []), relay.reshape(const_3625.astype('uint64'), [196, 16]), relay.reshape(const_3625.astype('uint64'), [196, 16]), ), 2)
func_3102_call = mod.get_global_var('func_3102')
func_3103_call = mutated_mod.get_global_var('func_3103')
call_3643 = relay.TupleGetItem(func_3102_call(), 3)
call_3644 = relay.TupleGetItem(func_3103_call(), 3)
output = relay.Tuple([call_3552,call_3595,call_3623,var_3624,const_3625,call_3643,])
output2 = relay.Tuple([call_3553,call_3596,call_3626,var_3624,const_3625,call_3644,])
func_3647 = relay.Function([var_3624,], output)
mod['func_3647'] = func_3647
mod = relay.transform.InferType()(mod)
mutated_mod['func_3647'] = func_3647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3648 = relay.var("var_3648", dtype = "uint64", shape = ())#candidate|3648|()|var|uint64
func_3647_call = mutated_mod.get_global_var('func_3647')
call_3649 = func_3647_call(var_3648)
output = call_3649
func_3650 = relay.Function([var_3648], output)
mutated_mod['func_3650'] = func_3650
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3661 = relay.var("var_3661", dtype = "float32", shape = (10, 8, 4))#candidate|3661|(10, 8, 4)|var|float32
uop_3662 = relay.asinh(var_3661.astype('float32')) # shape=(10, 8, 4)
bop_3670 = relay.bitwise_and(uop_3662.astype('int8'), relay.reshape(var_3661.astype('int8'), relay.shape_of(uop_3662))) # shape=(10, 8, 4)
output = relay.Tuple([bop_3670,])
output2 = relay.Tuple([bop_3670,])
func_3674 = relay.Function([var_3661,], output)
mod['func_3674'] = func_3674
mod = relay.transform.InferType()(mod)
var_3675 = relay.var("var_3675", dtype = "float32", shape = (10, 8, 4))#candidate|3675|(10, 8, 4)|var|float32
output = func_3674(var_3675)
func_3676 = relay.Function([var_3675], output)
mutated_mod['func_3676'] = func_3676
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_3783 = relay.TupleGetItem(func_1053_call(), 0)
call_3784 = relay.TupleGetItem(func_1054_call(), 0)
output = relay.Tuple([call_3783,])
output2 = relay.Tuple([call_3784,])
func_3786 = relay.Function([], output)
mod['func_3786'] = func_3786
mod = relay.transform.InferType()(mod)
mutated_mod['func_3786'] = func_3786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3786_call = mutated_mod.get_global_var('func_3786')
call_3787 = func_3786_call()
output = call_3787
func_3788 = relay.Function([], output)
mutated_mod['func_3788'] = func_3788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_3789 = func_609_call()
call_3790 = func_609_call()
func_1536_call = mod.get_global_var('func_1536')
func_1538_call = mutated_mod.get_global_var('func_1538')
call_3801 = relay.TupleGetItem(func_1536_call(relay.reshape(call_3789.astype('float32'), [2, 16, 9])), 2)
call_3802 = relay.TupleGetItem(func_1538_call(relay.reshape(call_3789.astype('float32'), [2, 16, 9])), 2)
output = relay.Tuple([call_3789,call_3801,])
output2 = relay.Tuple([call_3790,call_3802,])
func_3803 = relay.Function([], output)
mod['func_3803'] = func_3803
mod = relay.transform.InferType()(mod)
output = func_3803()
func_3804 = relay.Function([], output)
mutated_mod['func_3804'] = func_3804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3541_call = mod.get_global_var('func_3541')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_3821 = func_3541_call()
call_3822 = func_3541_call()
output = relay.Tuple([call_3821,])
output2 = relay.Tuple([call_3822,])
func_3833 = relay.Function([], output)
mod['func_3833'] = func_3833
mod = relay.transform.InferType()(mod)
mutated_mod['func_3833'] = func_3833
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mutated_mod.get_global_var('func_3833')
call_3834 = func_3833_call()
output = call_3834
func_3835 = relay.Function([], output)
mutated_mod['func_3835'] = func_3835
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1652_call = mod.get_global_var('func_1652')
func_1654_call = mutated_mod.get_global_var('func_1654')
call_3876 = relay.TupleGetItem(func_1652_call(), 1)
call_3877 = relay.TupleGetItem(func_1654_call(), 1)
var_3892 = relay.var("var_3892", dtype = "float64", shape = (2, 16, 9))#candidate|3892|(2, 16, 9)|var|float64
bop_3893 = relay.floor_mod(call_3876.astype('float32'), relay.reshape(var_3892.astype('float32'), relay.shape_of(call_3876))) # shape=(2, 16, 9)
bop_3896 = relay.floor_mod(call_3877.astype('float32'), relay.reshape(var_3892.astype('float32'), relay.shape_of(call_3877))) # shape=(2, 16, 9)
bop_3905 = relay.greater_equal(call_3876.astype('bool'), relay.reshape(var_3892.astype('bool'), relay.shape_of(call_3876))) # shape=(2, 16, 9)
bop_3908 = relay.greater_equal(call_3877.astype('bool'), relay.reshape(var_3892.astype('bool'), relay.shape_of(call_3877))) # shape=(2, 16, 9)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_3914 = relay.TupleGetItem(func_2546_call(), 0)
call_3915 = relay.TupleGetItem(func_2547_call(), 0)
output = relay.Tuple([bop_3893,bop_3905,call_3914,])
output2 = relay.Tuple([bop_3896,bop_3908,call_3915,])
func_3927 = relay.Function([var_3892,], output)
mod['func_3927'] = func_3927
mod = relay.transform.InferType()(mod)
mutated_mod['func_3927'] = func_3927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3928 = relay.var("var_3928", dtype = "float64", shape = (2, 16, 9))#candidate|3928|(2, 16, 9)|var|float64
func_3927_call = mutated_mod.get_global_var('func_3927')
call_3929 = func_3927_call(var_3928)
output = call_3929
func_3930 = relay.Function([var_3928], output)
mutated_mod['func_3930'] = func_3930
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1860_call = mod.get_global_var('func_1860')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_3946 = relay.TupleGetItem(func_1860_call(), 1)
call_3947 = relay.TupleGetItem(func_1861_call(), 1)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_3951 = relay.TupleGetItem(func_957_call(), 0)
call_3952 = relay.TupleGetItem(func_958_call(), 0)
output = relay.Tuple([call_3946,call_3951,])
output2 = relay.Tuple([call_3947,call_3952,])
func_3958 = relay.Function([], output)
mod['func_3958'] = func_3958
mod = relay.transform.InferType()(mod)
mutated_mod['func_3958'] = func_3958
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3958_call = mutated_mod.get_global_var('func_3958')
call_3959 = func_3958_call()
output = call_3959
func_3960 = relay.Function([], output)
mutated_mod['func_3960'] = func_3960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3389_call = mod.get_global_var('func_3389')
func_3390_call = mutated_mod.get_global_var('func_3390')
call_3966 = relay.TupleGetItem(func_3389_call(), 0)
call_3967 = relay.TupleGetItem(func_3390_call(), 0)
uop_3979 = relay.sinh(call_3966.astype('float64')) # shape=(2, 16, 9)
uop_3981 = relay.sinh(call_3967.astype('float64')) # shape=(2, 16, 9)
output = uop_3979
output2 = uop_3981
func_3988 = relay.Function([], output)
mod['func_3988'] = func_3988
mod = relay.transform.InferType()(mod)
output = func_3988()
func_3989 = relay.Function([], output)
mutated_mod['func_3989'] = func_3989
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_4015 = func_681_call()
call_4016 = func_681_call()
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_4019 = relay.TupleGetItem(func_1733_call(), 0)
call_4020 = relay.TupleGetItem(func_1735_call(), 0)
bop_4031 = relay.logical_or(call_4015.astype('bool'), relay.reshape(call_4019.astype('bool'), relay.shape_of(call_4015))) # shape=(2, 16, 9)
bop_4034 = relay.logical_or(call_4016.astype('bool'), relay.reshape(call_4020.astype('bool'), relay.shape_of(call_4016))) # shape=(2, 16, 9)
func_3541_call = mod.get_global_var('func_3541')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_4038 = func_3541_call()
call_4039 = func_3541_call()
output = relay.Tuple([bop_4031,call_4038,])
output2 = relay.Tuple([bop_4034,call_4039,])
func_4062 = relay.Function([], output)
mod['func_4062'] = func_4062
mod = relay.transform.InferType()(mod)
mutated_mod['func_4062'] = func_4062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4062_call = mutated_mod.get_global_var('func_4062')
call_4063 = func_4062_call()
output = call_4063
func_4064 = relay.Function([], output)
mutated_mod['func_4064'] = func_4064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4062_call = mod.get_global_var('func_4062')
func_4064_call = mutated_mod.get_global_var('func_4064')
call_4067 = relay.TupleGetItem(func_4062_call(), 1)
call_4068 = relay.TupleGetItem(func_4064_call(), 1)
func_3389_call = mod.get_global_var('func_3389')
func_3390_call = mutated_mod.get_global_var('func_3390')
call_4084 = relay.TupleGetItem(func_3389_call(), 0)
call_4085 = relay.TupleGetItem(func_3390_call(), 0)
output = relay.Tuple([call_4067,call_4084,])
output2 = relay.Tuple([call_4068,call_4085,])
func_4087 = relay.Function([], output)
mod['func_4087'] = func_4087
mod = relay.transform.InferType()(mod)
mutated_mod['func_4087'] = func_4087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4087_call = mutated_mod.get_global_var('func_4087')
call_4088 = func_4087_call()
output = call_4088
func_4089 = relay.Function([], output)
mutated_mod['func_4089'] = func_4089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4114 = relay.var("var_4114", dtype = "float32", shape = (7, 12, 16))#candidate|4114|(7, 12, 16)|var|float32
uop_4115 = relay.cos(var_4114.astype('float32')) # shape=(7, 12, 16)
output = relay.Tuple([uop_4115,])
output2 = relay.Tuple([uop_4115,])
func_4122 = relay.Function([var_4114,], output)
mod['func_4122'] = func_4122
mod = relay.transform.InferType()(mod)
var_4123 = relay.var("var_4123", dtype = "float32", shape = (7, 12, 16))#candidate|4123|(7, 12, 16)|var|float32
output = func_4122(var_4123)
func_4124 = relay.Function([var_4123], output)
mutated_mod['func_4124'] = func_4124
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2583_call = mod.get_global_var('func_2583')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_4126 = relay.TupleGetItem(func_2583_call(), 0)
call_4127 = relay.TupleGetItem(func_2585_call(), 0)
output = call_4126
output2 = call_4127
func_4137 = relay.Function([], output)
mod['func_4137'] = func_4137
mod = relay.transform.InferType()(mod)
output = func_4137()
func_4138 = relay.Function([], output)
mutated_mod['func_4138'] = func_4138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_4184 = relay.TupleGetItem(func_1872_call(), 0)
call_4185 = relay.TupleGetItem(func_1874_call(), 0)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
const_4196 = relay.const([-8,-2,-7,-8,-5,-5,-3,-5,-6,-2,3,-10,-4,-4,-3,-7,-7,-6,9,1,5,9,6,7,-3,2,-6,10,-5,5,3,-7,-2,5,8,-5,5,-5,8,-2,10,8,6,-7,2,9,5,6,-10,9,8,-3,10,3,-7,-10,8,-4,-7,7,5,5,-1,-7,5,-1,4,7,1,1,-4,6,10,-8,10,-8,-1,-5,5,3,2,2,-7,7,8,7,-2,6,2,-10,-1,-9,1,-7,8,8,-4,-3,9,9,1,-1,-9,-4,5,7,-2,10,-10,2,7,-9,10,1,5,1,8,-8,1,1,-6,1,3,-3,-8,-5,5,-5,-8,-6,-8,1,-9,4,1,-5,2,-6,9,1,4,-2,2,6,4,4,-1,10,4,-1,1,-1,-3,-9,-6,-10,8,9,-9,-9,9,7,-10,9,2,6,-5,6,4,10,8,10,2,-6,-6,-6,-2,-2,-1,-4,-10,-6,-9,-3,-10,3,-5,-3,-4,-9,-8,3,7,10,-6,-1,-7,3,9,-7,1,6,4,-2,-10,7,6,-8,7,3,4,-2,-2,5,3,10,-5,-1,-8,7,3,-8,6,-6,-5,6,4,10,-3,9,8,-1,6,2,-4,-3,-5,-10,6,1,4,1,-5,7,-6,5,6,9,-7,-7,1,10,1,-6,3,-10,-7,8,-10,4,-9,-9,7,8,-10,7,-5,9,6,-2,-5,7,-3,-5,-9,-6,10,-5,5,2,-8,-9,5,-8,-1,1,5,9,-4,1,-5,-4,-4,3,4,-7,4,5,1,-2,6,-10,1,10,-4,-9,-8,4,-3,3,10,-10,-3,-6,10,7,-3,-8,-6,2], dtype = "uint8")#candidate|4196|(320,)|const|uint8
call_4195 = func_2062_call(relay.reshape(const_4196.astype('uint8'), [5, 8, 8]))
call_4197 = func_2062_call(relay.reshape(const_4196.astype('uint8'), [5, 8, 8]))
output = relay.Tuple([call_4184,call_4195,const_4196,])
output2 = relay.Tuple([call_4185,call_4197,const_4196,])
func_4210 = relay.Function([], output)
mod['func_4210'] = func_4210
mod = relay.transform.InferType()(mod)
mutated_mod['func_4210'] = func_4210
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4210_call = mutated_mod.get_global_var('func_4210')
call_4211 = func_4210_call()
output = call_4211
func_4212 = relay.Function([], output)
mutated_mod['func_4212'] = func_4212
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1652_call = mod.get_global_var('func_1652')
func_1654_call = mutated_mod.get_global_var('func_1654')
call_4221 = relay.TupleGetItem(func_1652_call(), 1)
call_4222 = relay.TupleGetItem(func_1654_call(), 1)
func_2370_call = mod.get_global_var('func_2370')
func_2374_call = mutated_mod.get_global_var('func_2374')
const_4254 = relay.const([-4,-7,8,-6,-10,-5,9,4,8,5,8,-8,7,2,-8,-4,-7,-5,-2,-7,2,-3,5,-8,9,3,-3,-8,10,4,10,-10,9,-1,-6,3,-2,3,-4,-8,-4,2,3,-8,1,-1,-1,7,-6,-1,7,-2,-10,6,-4,7,-7,-5,-1,3,4,3,5,-7,8,-5,4,6,2,8,-6,6,-5,4,-4,8,-3,5,-8,-2,10,3,-5,-8,1,-3,-2,-10,9,-3,-3,3,9,-7,-10,-5,-6,-4,7,8,-9,-3,-1,6,-9,5,7,1,5,4,6,-6,8,-3,-4,-3,3,2,10,-6,-6,-2,-8,-2,2,-8,5,-3,6,10,-9,2,10,8,3,-1,-4,5,-8,2,-3,8,-4,3,-9,9,7,-9,-7,-8,-10,1,-4,5,3,1,10,4,-2,-6,-1,8,8,6,6,-8,-3,-2,5,-10,-7,-4,2,-10,8,-7,3,-8,5,-8,8,-9,5,9,-9,8,-9,10,2,-8,-8,-9,2,-1,3,-10,-5,3,10,-10,10,2,10,-3,-4,3,7,2,-1,-8,4,5,-9,-9,-2,-8,9,-4,-4,3,9,1,-10,-7,7,7,-5,1,3,-5,-1,7,-2,10,5,3,9,-2,-8,2,-4,5,3,5,7,1,2,-9,7,10,3,8,9,3,-8,-1,5,-4,-3,4,-1,-2,-3,7,10,-3,-3,5,2,-7,2,-3,-5,5,7,2,4,-3,4,-8,7,7,4,-2,-7,-5,9,6,-6,-4,10,-3,1,-3,5,-9,-3,-2,6,3,3,6,7,-5,-3,-6,-6,-9,-4,-2,-4,-3,5,3,-1,9,-4,7,-7,4,3,6,8,6,8,5,7,6,-5,-7,5,2,3,3,-2,-1,-9,-4,-2,1,8,-1,-3,-1,8,-7,-6,-4,-8,8,-6,-7,-7,3,3,1,-1,-8,-1,-3,7,-4,8,-9,-7,-8,-7,9,6,-5,-8,-10,-1,3,9,1,-7,6,-2,-4,3,5,7,-6,-10,1,9,4,4,-10,-5,-7,-5,-10,2,-10,-5,7,-3,-2,5,-8,9,-2,3,-3,4,-1,-5,-8,4,-1,4,-9,-2,9,-8,-2,1,7,-6,2,-10,-9,-5,-9,-6,8,-10,-7,1,2,3,6,7,-7,4,3,2,7,10,8,10,-5,6,5,-8,-7,-10,-6,-6,10,-2,-4,-4,4,8,-9,10,9,6,3,10,6,5,-6,6,-3,-8,5,-7,-7,2,3,10,6,-7,-1,-1,6,-10,8,-8,-6,-5,8,1,9,1,-3,-6,-6,-8,-2,5,-4,2,-3,-3,7,-2,-2,-2,4,4,6,-8,5,-1,-6,6,-3,2,-1,5,-2,4,-9,6,-2,1,-10,-10,7,-3,8,-3,-10,-7,1,-8,10,-9,-10,10,-5,2,2,-2,5,-1,7,-6,-10,-7,-4,4,-10,-2,-7,-4,5,-10,10,-5,-9,10,10,-4,-6,1,-7,5,-7,-10,9,-7,-2,1,-10,8,5,-5,1,-7,-2,10,-1,-9,-2,-5,4,7,-10,1,7,7,-7,-6,4,9,2,-5,4,3,2,-9,1,-4,4,-1,5,2,-2,2,2,2,-1,-8,1,-5,9,-1,1,1,3,6,-10,1,9,-10,7,6,8,-6,-3,-6,-4,3,4,-1,-4,6,7,7,-5,6,8,-3,-4,-7,-8,1,10,5,8,3,-3,9,10,-6,1,-8,-4,7,-8,8,5,-7,-3,-1,10,-6,-4,-5,-9,9,4,10,6,7,2,-1,-5,4,-3,-3,-10,10,-4,-8,7,-4,3,-9,3,-5,3,4,4,-8,-4,4,9,-7,10,-5,-3,9,5,4,-6,-5,-7,-7,-8,2,7,7,1,-9,1,9,5,9,6,9,4,-8,-4,2,9,5,9,2,-6,-10,-6,-9,6,10,1,1,7,6,6,5,-1,3,-2,9,-5,5,7,2,-3,-5,-6,-2,8,4,6,-9,-10,9,5,-8,-9,4,8,-1,-2,5,-3,-1,-5,-2,4,9,4,-6,8,-3,-8,4,5,-6,4,-5,8,-7,-10,-3,-4,8,10,9,9,-6,-1,4,-8,2,-2,8,-2,-3,7,7,-8,-9,1,8,-10,-9,-5,-6,3,-4,7,-7,10,-9,7,10,3,6,7,-3,8,-9,-7,7,-3,9,6,8,7,5,-3,9,-4,9,-1,-10,8,-4,-4,-7,4,8,-9,6,-6,-1,-5,7,7,1,-10,-7,-2,-3,3,-7,3,5,-4,9,-1,8,-1,3,1,-6,-7,-1,-5,7,-2,3,10,9,-10,-1,-9,6,4,-9,-5,7,-9,3,3,-2,-2,2,6,3,2,-6,5,-2,-3,-5,6,-4,-2,-9,-7,-2,7,-1,7,-8,8,-1,-7,-1,4,3,-7,2,-4,-4,3,7,2,-4,2,8,-7,-4,-2,9,10,-3,-8,8,-8,-10,10,3,-5,-1,-9,10,7,-10,-8,4,-10,-7,-4,8,-9,2,-8,-1,2,-2,10,4,-6,6,-5,4,-7,-2,7,-2,-10,8,-1,-1,-3,-1,4,2,-2,-6,1,10,2,-9,-4,7,-7,-2,-6,-1,-5,-1,8,3,-4,-4,-8,4,-8,8,6,-6,10,3,-10,-4,7,-5,1,-6,6,1,-6,-3,10,6,9,-10,1,-7,-10,-5,-8,-5,-8,-7,10,-6,5,-1,-3,10,1,10,-5,-3,8,3,8,-7,6,-1,-2,-3,8,-1,-4,-2,-2,9,1,-2,1,7,1,6,-7,-6,-5,5,4,2,-8,-5,9,6,5,9,3,-5,-1,4,9,-9,8,6,2,1,6,-8,9,5,2,-10,-1,9,-8,-9,2,1,-2,3,-9,-1,4,10,-3,-7,-8,-10,-6,2,-10,2,9,-2,-4,-4,-3,6,6,1,10,4,9,-8,3,-10,10,-6,7,1,-7,2,2,9,5,-9,10,-4,9,5,-3,6,-6,2,10,-5,-8,7,7,2,-6,9,-4,6,-7,7,5,-1,4,4,-9,-1,8,-9,-1,-8,-1,4,10,-1,8,-6,9,-4,3,7,9,-8,-5,1,-9,-5,-6,8,-7,-2,8,10,5,2,-1,9,8,-4,-8,9,4,2,2,-5,-10,4,6,7,7,1,-10,-8,10,9,9,-9,-1,2,-10,2,5,-10,-9,2,6,-6,4,3,7,3,-2,-10,1,6,-10,-1,-6,6,8,3,-1,-10,-2,8,5,-9,4,-9,3,6,6,10,10,7,-4,-10,9,10,3,3,9,-6,-1,-8,4,2,3,2,-8,1,-1,-6,3,2,-4,-5,-4,6,9,4,7,-3,-7,-6,-8,-6,-10,-9,-10,8,-3,5,-5,7,-4,-7,-6,-3,-7,-8,8,4,-10,-8,4,-4,-10,-8,-9,-8,5,-6,-4,-4,2,8,9,7,-4,10,2,5,-3,6,8,-7,-7,-4,3,-4,3,4,-3,-1,-5,-5,7,8,4,1,8,-5,-2,8,10,-10,-5,4,3,-4,-10,-7,10,-4,9,-6,-5,2,1,-5,-3,3,9,-5,-5,-3,10,2,5,-4,-3,-1,-1,-8,-4,-5,-7,-4,-8,-9,8,9,-1,-9,7,1,2,-2,7,-7,-2,8,3,-8,-1,-5,10,-10,-7,7,10,7,4,-7,9,3,-8], dtype = "int8")#candidate|4254|(1386,)|const|int8
call_4253 = relay.TupleGetItem(func_2370_call(relay.reshape(const_4254.astype('int8'), [9, 14, 11]), relay.reshape(const_4254.astype('int8'), [9, 14, 11]), ), 0)
call_4255 = relay.TupleGetItem(func_2374_call(relay.reshape(const_4254.astype('int8'), [9, 14, 11]), relay.reshape(const_4254.astype('int8'), [9, 14, 11]), ), 0)
uop_4256 = relay.rsqrt(call_4253.astype('float64')) # shape=(9, 14, 11)
uop_4258 = relay.rsqrt(call_4255.astype('float64')) # shape=(9, 14, 11)
bop_4260 = relay.greater_equal(uop_4256.astype('bool'), relay.reshape(call_4253.astype('bool'), relay.shape_of(uop_4256))) # shape=(9, 14, 11)
bop_4263 = relay.greater_equal(uop_4258.astype('bool'), relay.reshape(call_4255.astype('bool'), relay.shape_of(uop_4258))) # shape=(9, 14, 11)
output = relay.Tuple([call_4221,const_4254,bop_4260,])
output2 = relay.Tuple([call_4222,const_4254,bop_4263,])
func_4265 = relay.Function([], output)
mod['func_4265'] = func_4265
mod = relay.transform.InferType()(mod)
mutated_mod['func_4265'] = func_4265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4265_call = mutated_mod.get_global_var('func_4265')
call_4266 = func_4265_call()
output = call_4266
func_4267 = relay.Function([], output)
mutated_mod['func_4267'] = func_4267
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_4297 = relay.TupleGetItem(func_3004_call(), 1)
call_4298 = relay.TupleGetItem(func_3006_call(), 1)
output = call_4297
output2 = call_4298
func_4301 = relay.Function([], output)
mod['func_4301'] = func_4301
mod = relay.transform.InferType()(mod)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4301_call = mutated_mod.get_global_var('func_4301')
call_4302 = func_4301_call()
output = call_4302
func_4303 = relay.Function([], output)
mutated_mod['func_4303'] = func_4303
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1652_call = mod.get_global_var('func_1652')
func_1654_call = mutated_mod.get_global_var('func_1654')
call_4307 = relay.TupleGetItem(func_1652_call(), 2)
call_4308 = relay.TupleGetItem(func_1654_call(), 2)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_4309 = relay.TupleGetItem(func_2825_call(), 0)
call_4310 = relay.TupleGetItem(func_2827_call(), 0)
output = relay.Tuple([call_4307,call_4309,])
output2 = relay.Tuple([call_4308,call_4310,])
func_4318 = relay.Function([], output)
mod['func_4318'] = func_4318
mod = relay.transform.InferType()(mod)
output = func_4318()
func_4319 = relay.Function([], output)
mutated_mod['func_4319'] = func_4319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4318_call = mod.get_global_var('func_4318')
func_4319_call = mutated_mod.get_global_var('func_4319')
call_4320 = relay.TupleGetItem(func_4318_call(), 0)
call_4321 = relay.TupleGetItem(func_4319_call(), 0)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_4340 = relay.TupleGetItem(func_1544_call(), 0)
call_4341 = relay.TupleGetItem(func_1545_call(), 0)
output = relay.Tuple([call_4320,call_4340,])
output2 = relay.Tuple([call_4321,call_4341,])
func_4343 = relay.Function([], output)
mod['func_4343'] = func_4343
mod = relay.transform.InferType()(mod)
mutated_mod['func_4343'] = func_4343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4343_call = mutated_mod.get_global_var('func_4343')
call_4344 = func_4343_call()
output = call_4344
func_4345 = relay.Function([], output)
mutated_mod['func_4345'] = func_4345
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1940_call = mod.get_global_var('func_1940')
func_1942_call = mutated_mod.get_global_var('func_1942')
call_4372 = func_1940_call()
call_4373 = func_1940_call()
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_4385 = relay.TupleGetItem(func_1380_call(), 0)
call_4386 = relay.TupleGetItem(func_1382_call(), 0)
func_1160_call = mod.get_global_var('func_1160')
func_1163_call = mutated_mod.get_global_var('func_1163')
call_4390 = relay.TupleGetItem(func_1160_call(relay.reshape(call_4372.astype('float64'), [2, 16, 9])), 1)
call_4391 = relay.TupleGetItem(func_1163_call(relay.reshape(call_4372.astype('float64'), [2, 16, 9])), 1)
func_3647_call = mod.get_global_var('func_3647')
func_3650_call = mutated_mod.get_global_var('func_3650')
const_4393 = relay.const(-5, dtype = "uint64")#candidate|4393|()|const|uint64
call_4392 = relay.TupleGetItem(func_3647_call(relay.reshape(const_4393.astype('uint64'), [])), 0)
call_4394 = relay.TupleGetItem(func_3650_call(relay.reshape(const_4393.astype('uint64'), [])), 0)
output = relay.Tuple([call_4372,call_4385,call_4390,call_4392,const_4393,])
output2 = relay.Tuple([call_4373,call_4386,call_4391,call_4394,const_4393,])
func_4398 = relay.Function([], output)
mod['func_4398'] = func_4398
mod = relay.transform.InferType()(mod)
output = func_4398()
func_4399 = relay.Function([], output)
mutated_mod['func_4399'] = func_4399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2321_call = mod.get_global_var('func_2321')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_4411 = func_2321_call()
call_4412 = func_2321_call()
output = relay.Tuple([call_4411,])
output2 = relay.Tuple([call_4412,])
func_4413 = relay.Function([], output)
mod['func_4413'] = func_4413
mod = relay.transform.InferType()(mod)
mutated_mod['func_4413'] = func_4413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4413_call = mutated_mod.get_global_var('func_4413')
call_4414 = func_4413_call()
output = call_4414
func_4415 = relay.Function([], output)
mutated_mod['func_4415'] = func_4415
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4487 = relay.const(-1, dtype = "int64")#candidate|4487|()|const|int64
var_4488 = relay.var("var_4488", dtype = "int64", shape = (13, 3, 10))#candidate|4488|(13, 3, 10)|var|int64
bop_4489 = relay.minimum(const_4487.astype('int64'), var_4488.astype('int64')) # shape=(13, 3, 10)
output = bop_4489
output2 = bop_4489
func_4500 = relay.Function([var_4488,], output)
mod['func_4500'] = func_4500
mod = relay.transform.InferType()(mod)
var_4501 = relay.var("var_4501", dtype = "int64", shape = (13, 3, 10))#candidate|4501|(13, 3, 10)|var|int64
output = func_4500(var_4501)
func_4502 = relay.Function([var_4501], output)
mutated_mod['func_4502'] = func_4502
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1600_call = mod.get_global_var('func_1600')
func_1602_call = mutated_mod.get_global_var('func_1602')
call_4509 = relay.TupleGetItem(func_1600_call(), 0)
call_4510 = relay.TupleGetItem(func_1602_call(), 0)
output = relay.Tuple([call_4509,])
output2 = relay.Tuple([call_4510,])
func_4540 = relay.Function([], output)
mod['func_4540'] = func_4540
mod = relay.transform.InferType()(mod)
mutated_mod['func_4540'] = func_4540
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4540_call = mutated_mod.get_global_var('func_4540')
call_4541 = func_4540_call()
output = call_4541
func_4542 = relay.Function([], output)
mutated_mod['func_4542'] = func_4542
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_4573 = relay.TupleGetItem(func_1544_call(), 0)
call_4574 = relay.TupleGetItem(func_1545_call(), 0)
output = relay.Tuple([call_4573,])
output2 = relay.Tuple([call_4574,])
func_4596 = relay.Function([], output)
mod['func_4596'] = func_4596
mod = relay.transform.InferType()(mod)
mutated_mod['func_4596'] = func_4596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mutated_mod.get_global_var('func_4596')
call_4597 = func_4596_call()
output = call_4597
func_4598 = relay.Function([], output)
mutated_mod['func_4598'] = func_4598
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4675 = relay.var("var_4675", dtype = "float64", shape = (4, 14, 1))#candidate|4675|(4, 14, 1)|var|float64
var_4676 = relay.var("var_4676", dtype = "float64", shape = (4, 14, 11))#candidate|4676|(4, 14, 11)|var|float64
bop_4677 = relay.floor_divide(var_4675.astype('float64'), var_4676.astype('float64')) # shape=(4, 14, 11)
output = relay.Tuple([bop_4677,])
output2 = relay.Tuple([bop_4677,])
func_4680 = relay.Function([var_4675,var_4676,], output)
mod['func_4680'] = func_4680
mod = relay.transform.InferType()(mod)
mutated_mod['func_4680'] = func_4680
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4680_call = mutated_mod.get_global_var('func_4680')
var_4682 = relay.var("var_4682", dtype = "float64", shape = (4, 14, 1))#candidate|4682|(4, 14, 1)|var|float64
var_4683 = relay.var("var_4683", dtype = "float64", shape = (4, 14, 11))#candidate|4683|(4, 14, 11)|var|float64
call_4681 = func_4680_call(var_4682,var_4683,)
output = call_4681
func_4684 = relay.Function([var_4682,var_4683,], output)
mutated_mod['func_4684'] = func_4684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_617_call = mod.get_global_var('func_617')
func_618_call = mutated_mod.get_global_var('func_618')
call_4717 = relay.TupleGetItem(func_617_call(), 0)
call_4718 = relay.TupleGetItem(func_618_call(), 0)
output = relay.Tuple([call_4717,])
output2 = relay.Tuple([call_4718,])
func_4719 = relay.Function([], output)
mod['func_4719'] = func_4719
mod = relay.transform.InferType()(mod)
mutated_mod['func_4719'] = func_4719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4719_call = mutated_mod.get_global_var('func_4719')
call_4720 = func_4719_call()
output = call_4720
func_4721 = relay.Function([], output)
mutated_mod['func_4721'] = func_4721
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4734 = relay.var("var_4734", dtype = "uint8", shape = (6, 8, 4))#candidate|4734|(6, 8, 4)|var|uint8
const_4735 = relay.const([[[-2,10,-10,9],[6,-6,9,6],[7,-10,-3,4],[-9,-2,3,9],[-4,-5,8,4],[-8,-6,4,8],[3,-2,-6,2],[5,10,-8,3]],[[-8,8,-4,9],[3,-9,-7,-8],[-7,-9,-9,8],[-4,1,-7,-6],[5,-10,6,-1],[5,6,8,-6],[-4,-10,5,8],[8,3,-6,-10]],[[-3,-9,2,-8],[9,2,-7,4],[3,-8,-2,10],[-8,5,4,-4],[-10,7,-3,10],[10,1,2,1],[-9,-6,7,-3],[10,8,5,-10]],[[5,8,2,-1],[-2,2,-8,-7],[-3,-10,-10,-7],[10,2,-9,2],[-2,3,-8,8],[7,-2,-4,1],[-4,10,-3,4],[-4,1,-3,-9]],[[-5,10,-9,3],[-10,-8,-8,2],[10,-7,8,-6],[-10,-6,-4,-7],[-9,2,5,3],[-2,10,2,1],[-3,-4,-10,3],[-1,-2,-6,-2]],[[5,-1,9,8],[5,-1,-1,8],[1,-6,4,10],[10,10,2,-1],[6,-9,-7,8],[6,-10,2,-2],[-2,3,-2,1],[6,8,-3,-4]]], dtype = "uint8")#candidate|4735|(6, 8, 4)|const|uint8
bop_4736 = relay.add(var_4734.astype('uint8'), relay.reshape(const_4735.astype('uint8'), relay.shape_of(var_4734))) # shape=(6, 8, 4)
bop_4749 = relay.greater_equal(const_4735.astype('bool'), relay.reshape(var_4734.astype('bool'), relay.shape_of(const_4735))) # shape=(6, 8, 4)
func_2583_call = mod.get_global_var('func_2583')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_4755 = relay.TupleGetItem(func_2583_call(), 0)
call_4756 = relay.TupleGetItem(func_2585_call(), 0)
output = relay.Tuple([bop_4736,bop_4749,call_4755,])
output2 = relay.Tuple([bop_4736,bop_4749,call_4756,])
func_4778 = relay.Function([var_4734,], output)
mod['func_4778'] = func_4778
mod = relay.transform.InferType()(mod)
mutated_mod['func_4778'] = func_4778
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4779 = relay.var("var_4779", dtype = "uint8", shape = (6, 8, 4))#candidate|4779|(6, 8, 4)|var|uint8
func_4778_call = mutated_mod.get_global_var('func_4778')
call_4780 = func_4778_call(var_4779)
output = call_4780
func_4781 = relay.Function([var_4779], output)
mutated_mod['func_4781'] = func_4781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1210_call = mod.get_global_var('func_1210')
func_1212_call = mutated_mod.get_global_var('func_1212')
call_4807 = func_1210_call()
call_4808 = func_1210_call()
func_456_call = mod.get_global_var('func_456')
func_460_call = mutated_mod.get_global_var('func_460')
var_4816 = relay.var("var_4816", dtype = "int32", shape = (108,))#candidate|4816|(108,)|var|int32
call_4815 = relay.TupleGetItem(func_456_call(relay.reshape(var_4816.astype('int32'), [3, 9, 4]), relay.reshape(var_4816.astype('int32'), [3, 9, 4]), ), 1)
call_4817 = relay.TupleGetItem(func_460_call(relay.reshape(var_4816.astype('int32'), [3, 9, 4]), relay.reshape(var_4816.astype('int32'), [3, 9, 4]), ), 1)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_4820 = func_270_call()
call_4821 = func_270_call()
output = relay.Tuple([call_4807,call_4815,var_4816,call_4820,])
output2 = relay.Tuple([call_4808,call_4817,var_4816,call_4821,])
func_4835 = relay.Function([var_4816,], output)
mod['func_4835'] = func_4835
mod = relay.transform.InferType()(mod)
mutated_mod['func_4835'] = func_4835
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4836 = relay.var("var_4836", dtype = "int32", shape = (108,))#candidate|4836|(108,)|var|int32
func_4835_call = mutated_mod.get_global_var('func_4835')
call_4837 = func_4835_call(var_4836)
output = call_4837
func_4838 = relay.Function([var_4836], output)
mutated_mod['func_4838'] = func_4838
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4892 = relay.var("var_4892", dtype = "float64", shape = (16, 12, 1))#candidate|4892|(16, 12, 1)|var|float64
uop_4893 = relay.erf(var_4892.astype('float64')) # shape=(16, 12, 1)
uop_4908 = relay.sinh(var_4892.astype('float32')) # shape=(16, 12, 1)
output = relay.Tuple([uop_4893,uop_4908,])
output2 = relay.Tuple([uop_4893,uop_4908,])
func_4910 = relay.Function([var_4892,], output)
mod['func_4910'] = func_4910
mod = relay.transform.InferType()(mod)
var_4911 = relay.var("var_4911", dtype = "float64", shape = (16, 12, 1))#candidate|4911|(16, 12, 1)|var|float64
output = func_4910(var_4911)
func_4912 = relay.Function([var_4911], output)
mutated_mod['func_4912'] = func_4912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_4941 = func_681_call()
call_4942 = func_681_call()
output = relay.Tuple([call_4941,])
output2 = relay.Tuple([call_4942,])
func_4943 = relay.Function([], output)
mod['func_4943'] = func_4943
mod = relay.transform.InferType()(mod)
mutated_mod['func_4943'] = func_4943
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4943_call = mutated_mod.get_global_var('func_4943')
call_4944 = func_4943_call()
output = call_4944
func_4945 = relay.Function([], output)
mutated_mod['func_4945'] = func_4945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5111 = relay.var("var_5111", dtype = "int64", shape = (10, 12, 16))#candidate|5111|(10, 12, 16)|var|int64
const_5112 = relay.const([[[-5,-5,-5,5,-3,1,-4,-8,-4,4,-3,-6,-8,10,5,9],[-1,6,-3,1,-8,8,1,6,5,9,10,1,-6,-8,-8,-10],[3,7,6,6,2,7,9,3,3,2,-1,-3,-3,-7,-8,-2],[-2,-7,-8,-4,6,-8,-5,7,-4,5,-3,2,7,-6,8,-6],[-8,-1,-7,-9,-6,-7,7,-1,4,-8,-2,2,-2,6,8,-10],[-6,-3,6,7,-6,-1,10,-5,7,1,6,1,-6,5,9,-10],[-6,10,-4,2,-1,6,6,-6,-7,-4,-2,8,-2,-2,10,-7],[-7,-10,6,-5,-6,8,2,-7,-3,-9,-6,3,-4,10,-8,-2],[-6,8,-4,-8,-3,4,-4,-4,2,2,-2,5,-1,-2,1,-6],[4,-8,-8,-1,-5,-6,-6,6,4,5,4,-4,6,-5,-7,4],[6,2,-8,-5,-7,-2,9,-10,-7,-9,-6,7,6,-9,-3,-8],[4,-3,4,5,-6,6,-6,-8,-3,5,1,-3,4,-4,4,-5]],[[2,1,3,9,3,-7,-4,-4,-6,-8,1,-6,3,1,9,-8],[-4,-9,2,-10,-5,-8,4,6,2,-4,5,-5,9,-10,4,1],[4,8,-10,-5,-5,-2,6,6,-1,-1,2,9,-4,10,-6,7],[-1,-9,3,-3,-8,7,2,2,-6,2,-8,9,-9,-1,10,-4],[-3,1,7,-4,1,-9,-7,-6,3,-10,8,-5,6,1,-4,-8],[-8,-2,-3,9,10,-8,-10,-9,-4,-6,-8,-1,-8,2,-7,-8],[-9,9,-1,-7,6,-7,10,1,-4,-8,7,7,-2,-9,9,-4],[-10,-10,1,1,1,-6,-5,-6,-4,-1,4,8,9,4,7,-4],[-1,7,2,-1,-9,7,-6,2,7,-2,-3,6,-10,-10,8,-3],[10,1,9,6,-1,-1,-6,-6,8,6,10,3,-4,-4,-9,-3],[6,-1,-8,-4,-2,7,-10,2,10,-9,-10,8,-7,10,1,5],[9,-4,-4,7,3,-3,6,-1,3,-9,-6,9,-1,-9,2,10]],[[1,8,10,3,-1,8,-2,-6,-1,-8,-1,-10,5,7,-5,-7],[-10,-4,-2,6,5,-1,-3,2,9,10,-6,-6,-10,-8,-9,3],[-2,10,6,-5,9,8,2,-7,9,-3,-6,5,10,-2,10,8],[4,6,-5,-3,-7,-8,10,-10,-1,-3,3,-4,3,2,9,5],[-10,-5,4,-9,8,1,-3,6,-5,-10,9,1,-7,-5,-5,-4],[-5,-7,-7,-9,-4,-3,-1,-8,8,-5,3,8,9,10,8,-8],[-3,10,-1,-6,-1,-9,-10,9,8,-6,7,3,-9,-1,-5,8],[6,-9,-8,4,-6,2,-2,5,-4,-1,4,1,6,-10,3,-10],[-7,7,-4,7,-4,5,1,-7,10,7,3,7,10,-10,-5,-1],[9,-8,-7,-2,-3,8,-8,8,-7,10,-5,-7,4,9,8,-10],[7,10,2,-6,3,-8,3,9,-2,-7,-5,3,4,9,-1,-8],[6,4,-4,-2,6,-7,5,-8,4,6,-2,9,3,7,-6,2]],[[-5,-7,-7,-5,8,-4,6,1,-9,-9,8,-6,-5,-4,-8,-2],[-3,1,7,-4,5,-9,-10,-1,9,-10,10,-9,9,-8,10,-9],[9,2,5,3,4,3,6,2,7,-4,8,-4,7,-5,1,1],[-5,8,-8,1,6,-5,9,-8,1,-3,-7,7,8,2,-7,9],[-5,1,-7,7,-6,4,2,-2,-5,-4,-2,6,-3,7,-3,-2],[-3,-4,-7,4,3,-1,-3,8,7,-10,-2,-9,7,7,-2,8],[3,-6,1,4,-1,9,-9,9,8,5,6,-9,9,2,-6,-9],[-4,-9,-6,-1,9,10,-6,4,-10,5,4,-10,-9,-6,-5,-4],[-9,-4,-6,-3,-2,5,-4,1,7,-10,10,-5,2,-4,6,4],[10,2,2,3,8,1,6,-4,9,-5,5,10,9,4,3,-1],[-7,-1,8,-2,-3,-6,6,1,7,-6,3,-10,1,10,-4,-9],[3,10,5,8,5,-6,-6,-6,-4,-5,-10,1,-1,-7,1,-5]],[[-5,8,7,7,-1,-2,-1,-10,-3,-4,-2,-6,6,-7,1,-5],[-9,8,8,1,-10,6,3,6,3,-1,-5,-7,2,9,-7,10],[7,5,5,7,-7,7,-1,8,-5,10,-5,10,-2,-1,-5,-7],[10,2,-6,-1,1,4,2,-7,-2,4,5,-7,7,6,-10,6],[4,5,6,4,-3,1,-2,-2,-9,-4,-4,-1,-8,3,-9,7],[-5,-3,8,8,6,9,-2,-2,9,3,-6,2,-1,-9,-4,-6],[-1,-9,8,2,-9,-4,4,-9,-4,6,-9,2,-5,-2,1,7],[-9,-1,-6,-3,-6,7,4,4,-10,-6,1,1,-2,5,1,3],[8,8,-7,-10,-7,4,5,-9,-6,-6,-6,-3,7,2,-9,9],[9,3,10,10,10,-9,9,2,5,-4,-2,-9,-6,9,6,-1],[5,2,9,3,7,6,3,3,3,-9,8,-4,-9,-8,-10,1],[-4,1,4,-3,-9,6,5,10,-1,-3,-6,-3,-9,-1,1,4]],[[-2,1,10,-8,-2,-1,-8,-7,1,-9,-6,-4,-5,-1,5,-4],[-10,-7,-8,1,3,-9,4,-3,-3,-2,7,3,10,-10,7,4],[-10,10,-9,-10,-3,-5,-4,-10,1,5,7,-1,1,-2,9,8],[10,-7,-6,-3,-5,-6,5,5,7,5,9,-10,9,-9,-1,-8],[-4,2,-4,-9,-1,10,-10,-3,7,10,6,-8,-4,-1,-3,-8],[6,7,4,10,2,5,-5,8,8,9,9,-9,4,10,1,-6],[-1,-4,10,2,4,-3,-6,2,-8,6,-10,-2,4,-4,3,1],[-5,-7,-1,-7,6,3,-9,-4,7,4,-6,2,10,7,7,5],[5,7,3,-8,-3,1,-7,9,-6,1,-3,5,2,7,10,-3],[6,-10,3,-9,10,-8,-6,10,4,-5,-6,-8,-2,8,-9,-8],[1,5,7,-2,-6,3,1,-6,-7,-10,1,3,-5,7,2,-10],[-5,-10,-10,9,-5,10,8,-1,-8,1,-10,-5,3,-10,7,-9]],[[4,-5,2,-2,6,2,-9,2,5,7,6,-2,-3,-6,-6,-5],[6,7,-1,6,-3,5,3,-1,1,-4,7,-7,-2,-3,10,9],[5,6,6,-7,-2,3,10,-4,2,-7,5,1,7,-6,-9,4],[2,4,-2,7,1,-9,-5,-1,2,6,-10,-5,-1,3,-7,-8],[9,-4,-2,6,4,4,10,-6,3,-10,-9,9,7,3,-1,2],[2,-10,1,-8,1,2,-9,-4,10,-5,-8,-2,8,-8,6,-8],[7,1,-2,-3,-2,4,5,4,-1,-6,-3,3,-4,8,-2,6],[-4,9,7,1,-7,3,-5,9,3,-5,4,8,9,-5,2,-2],[10,4,-1,9,2,-4,-8,-2,-6,9,-3,5,-3,-4,-2,3],[6,-3,2,9,-5,-10,-3,6,-9,9,-2,-5,7,-1,-6,2],[4,10,-7,-2,3,-5,-6,8,-6,7,-3,4,-4,10,-1,-1],[-8,-3,-2,-7,-6,-3,-3,-8,-8,-8,9,-3,-9,2,-5,-5]],[[6,10,-2,4,1,-2,6,5,7,9,7,9,-4,6,-4,2],[2,9,-1,3,8,-8,5,2,-9,10,-2,-4,1,-6,2,6],[-2,-7,8,4,-5,-2,-6,-4,5,2,4,2,7,-2,-5,-2],[-3,-9,1,7,-4,6,-3,-6,6,-4,6,-6,3,2,6,7],[5,2,-7,-1,8,-2,2,1,-10,8,2,-10,2,7,8,-9],[7,-10,-10,7,2,3,9,-2,1,-6,-2,2,-10,3,-10,-2],[4,3,-7,-6,-10,-3,-2,-10,4,8,2,-1,-8,10,-5,-6],[8,-6,10,4,-10,-10,3,-7,-4,3,6,8,-8,-3,3,-3],[1,-6,1,10,8,-4,-10,9,6,9,6,6,-8,-7,8,-9],[-1,-9,-6,2,1,-6,8,4,-7,-6,4,9,2,-10,9,-9],[-6,-3,-9,6,-2,10,8,-4,9,-2,-5,-3,-6,-7,-4,-5],[5,3,-2,2,3,-4,8,-8,9,9,10,8,9,-10,2,-5]],[[3,10,9,9,-6,5,-10,-2,-4,10,-5,9,-6,8,6,4],[1,5,8,2,-9,-9,-1,-6,3,8,-6,3,9,9,-5,5],[9,-6,5,2,-6,-3,-3,3,-6,-6,-9,2,10,-3,4,-1],[-1,-9,-6,2,-5,2,-3,6,7,2,2,-5,-5,9,10,4],[6,8,6,7,-5,9,-5,7,-6,-1,-5,3,7,-1,2,8],[9,-2,-8,-6,2,-10,10,-1,8,-9,10,-5,1,-4,1,1],[-10,9,-5,-8,2,-4,-9,3,8,-10,-1,5,-1,5,3,-6],[-2,-8,9,6,5,-4,-6,2,6,-2,7,10,-8,-1,-4,1],[-1,-5,-4,2,10,4,4,9,5,8,9,-1,-5,-6,-1,-7],[6,5,-10,1,-4,5,8,9,-5,9,-6,-1,-5,10,-5,-10],[-8,3,3,-9,9,-6,-9,-4,1,8,-4,-8,7,-6,-6,5],[3,-5,4,-5,9,-1,6,3,-9,-7,-2,-3,-5,-3,-9,-9]],[[6,1,8,-2,7,5,7,5,3,-8,-6,-5,-1,-6,-7,-5],[8,3,-1,-3,6,-4,-8,-10,10,5,2,9,-8,-6,-9,-8],[-6,-3,5,7,-3,-8,-9,-1,8,-7,6,4,10,-1,-10,7],[1,2,5,-9,10,9,-6,10,-4,6,4,6,-1,-4,7,8],[-1,-5,-10,5,4,1,2,-5,10,-6,1,-8,-10,-5,6,-6],[4,3,8,5,-10,1,10,8,-7,-6,-6,-3,9,-3,1,-9],[-3,-10,10,2,-4,2,10,5,6,-10,-6,-9,2,7,3,10],[-2,-6,8,4,2,-3,8,2,9,-6,-4,9,1,9,6,10],[2,10,-4,1,2,10,3,-4,3,-7,-7,5,6,3,-5,-10],[9,-8,-4,-2,-2,8,4,8,-4,-6,-5,10,-7,1,-6,-1],[-1,-1,-10,3,3,7,-3,-9,-2,-7,-8,-6,10,6,-10,-10],[-10,8,-3,-1,-2,6,-5,-2,9,-4,6,1,9,1,-8,2]]], dtype = "int64")#candidate|5112|(10, 12, 16)|const|int64
bop_5113 = relay.left_shift(var_5111.astype('int64'), relay.reshape(const_5112.astype('int64'), relay.shape_of(var_5111))) # shape=(10, 12, 16)
func_1536_call = mod.get_global_var('func_1536')
func_1538_call = mutated_mod.get_global_var('func_1538')
var_5125 = relay.var("var_5125", dtype = "float32", shape = (288,))#candidate|5125|(288,)|var|float32
call_5124 = relay.TupleGetItem(func_1536_call(relay.reshape(var_5125.astype('float32'), [2, 16, 9])), 0)
call_5126 = relay.TupleGetItem(func_1538_call(relay.reshape(var_5125.astype('float32'), [2, 16, 9])), 0)
uop_5133 = relay.sin(bop_5113.astype('float32')) # shape=(10, 12, 16)
func_1278_call = mod.get_global_var('func_1278')
func_1284_call = mutated_mod.get_global_var('func_1284')
const_5153 = relay.const(-4, dtype = "uint64")#candidate|5153|()|const|uint64
var_5154 = relay.var("var_5154", dtype = "uint64", shape = (3136,))#candidate|5154|(3136,)|var|uint64
call_5152 = relay.TupleGetItem(func_1278_call(relay.reshape(var_5125.astype('float64'), [2, 16, 9]), relay.reshape(const_5153.astype('uint64'), []), relay.reshape(var_5154.astype('uint64'), [196, 16]), relay.reshape(var_5154.astype('uint64'), [196, 16]), ), 7)
call_5155 = relay.TupleGetItem(func_1284_call(relay.reshape(var_5125.astype('float64'), [2, 16, 9]), relay.reshape(const_5153.astype('uint64'), []), relay.reshape(var_5154.astype('uint64'), [196, 16]), relay.reshape(var_5154.astype('uint64'), [196, 16]), ), 7)
output = relay.Tuple([call_5124,var_5125,uop_5133,call_5152,const_5153,var_5154,])
output2 = relay.Tuple([call_5126,var_5125,uop_5133,call_5155,const_5153,var_5154,])
func_5164 = relay.Function([var_5111,var_5125,var_5154,], output)
mod['func_5164'] = func_5164
mod = relay.transform.InferType()(mod)
mutated_mod['func_5164'] = func_5164
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5164_call = mutated_mod.get_global_var('func_5164')
var_5166 = relay.var("var_5166", dtype = "int64", shape = (10, 12, 16))#candidate|5166|(10, 12, 16)|var|int64
var_5167 = relay.var("var_5167", dtype = "float32", shape = (288,))#candidate|5167|(288,)|var|float32
var_5168 = relay.var("var_5168", dtype = "uint64", shape = (3136,))#candidate|5168|(3136,)|var|uint64
call_5165 = func_5164_call(var_5166,var_5167,var_5168,)
output = call_5165
func_5169 = relay.Function([var_5166,var_5167,var_5168,], output)
mutated_mod['func_5169'] = func_5169
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5178 = relay.const([[[-4.350570,-0.752539,-1.925997,4.293147,7.980107],[-0.120765,2.924839,9.540851,1.229224,-1.433907]],[[-4.341570,-6.710856,-6.502062,9.493479,-8.271132],[-6.647748,-4.128094,9.394057,9.227828,8.524786]],[[4.989489,-4.614459,5.887146,-5.292436,5.376376],[-9.988153,3.929348,-9.755306,5.830399,3.804351]],[[-9.108780,-7.751268,-4.416481,6.047800,-9.821143],[6.052223,-1.511456,-2.751848,2.433212,-0.342021]],[[5.743439,-4.503762,-8.848426,-9.465990,-0.455035],[1.068171,-4.066880,2.456135,9.367083,-0.192557]],[[2.675220,3.820837,6.323247,-8.257258,-0.779772],[4.708471,9.145725,-9.659748,-0.103441,1.215535]],[[-7.107249,3.370730,-3.892387,-4.032429,1.947158],[6.159642,-7.930740,-8.980441,7.673944,-3.421253]],[[-9.506748,3.330922,1.460861,0.354661,4.604558],[-8.615725,2.774136,-0.271747,-0.951270,5.989751]]], dtype = "float64")#candidate|5178|(8, 2, 5)|const|float64
uop_5179 = relay.asinh(const_5178.astype('float64')) # shape=(8, 2, 5)
output = uop_5179
output2 = uop_5179
func_5187 = relay.Function([], output)
mod['func_5187'] = func_5187
mod = relay.transform.InferType()(mod)
mutated_mod['func_5187'] = func_5187
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5187_call = mutated_mod.get_global_var('func_5187')
call_5188 = func_5187_call()
output = call_5188
func_5189 = relay.Function([], output)
mutated_mod['func_5189'] = func_5189
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1860_call = mod.get_global_var('func_1860')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_5253 = relay.TupleGetItem(func_1860_call(), 0)
call_5254 = relay.TupleGetItem(func_1861_call(), 0)
output = relay.Tuple([call_5253,])
output2 = relay.Tuple([call_5254,])
func_5258 = relay.Function([], output)
mod['func_5258'] = func_5258
mod = relay.transform.InferType()(mod)
mutated_mod['func_5258'] = func_5258
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5258_call = mutated_mod.get_global_var('func_5258')
call_5259 = func_5258_call()
output = call_5259
func_5260 = relay.Function([], output)
mutated_mod['func_5260'] = func_5260
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_5277 = relay.TupleGetItem(func_3833_call(), 0)
call_5278 = relay.TupleGetItem(func_3835_call(), 0)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_5280 = relay.TupleGetItem(func_1544_call(), 0)
call_5281 = relay.TupleGetItem(func_1545_call(), 0)
func_2401_call = mod.get_global_var('func_2401')
func_2403_call = mutated_mod.get_global_var('func_2403')
const_5283 = relay.const([[-5],[2],[-6],[7],[-3],[-9],[-1],[-9],[7],[8],[-3],[7],[-8],[-8],[2],[-3],[-10],[-7],[8],[-8],[10],[-2],[-4],[-1],[1],[5],[8],[1],[-6],[2],[-9],[-7],[8],[7],[9],[-10],[7],[-2],[-5],[3],[4],[7],[2],[6],[7],[8],[-3],[-6],[8],[-8],[1],[7],[-10],[-8],[-2],[8],[-1],[-6],[4],[-2],[3],[8],[-2],[8],[8],[-8],[4],[8],[2],[6],[8],[-2],[2],[3],[3],[7],[-5],[2],[9],[-9],[4],[9],[-1],[-1],[-4],[-1],[-2],[1],[-10],[-9],[10],[-6],[5],[2],[8],[3],[9],[1],[9],[-4],[-8],[5],[-7],[-5],[3],[-9],[4],[-9],[5],[-2],[-5],[4],[-7],[3],[-6],[10],[4],[-5],[4],[-6],[-6],[3],[10],[8],[5],[8],[-5],[5],[9],[9],[-7],[-9],[-6],[9],[-6],[8],[-2],[3],[-5],[7],[3],[2],[-10],[-1],[5],[6],[8],[-2],[-2],[6],[-8],[2],[-7],[1],[-8],[-2],[6],[8],[-2],[-6],[-10],[8],[8],[4],[-3],[-9],[-5],[2],[-8],[4],[1],[-6],[1],[-4],[-4],[10],[1],[-3],[10],[-8],[-6],[-5],[-8],[2],[9],[-9],[-3],[9],[10],[9],[-2],[-9],[8],[1],[-9],[-4],[-5],[-7],[5],[-6],[-7],[-7],[3],[-6],[-7],[-8],[-7],[1],[9],[5],[2],[3],[8],[10],[-9],[-8],[-5],[-7],[-8],[1],[2],[-6],[6],[-4],[1],[5],[9],[-1],[-7],[-10],[9],[-5],[4],[-3],[8],[10],[5],[9],[-3],[-8],[-4],[-6],[-10],[10],[7],[-6],[-2],[3],[4],[10],[9],[-2],[-6],[-6],[5],[3],[-7],[-2],[7],[-4],[4],[5],[2],[3],[1],[8],[1],[-4],[2],[-8],[-4],[-6],[-4],[-7],[2],[9],[1],[3],[-9],[9],[-8],[-2],[8],[10],[6],[9],[-10],[2],[-3],[7],[8],[1],[-10],[-5],[1],[-1],[-5],[-9],[-10],[5],[8],[-7],[-6],[4],[-6],[5],[9],[-5],[2],[-9],[8],[-3],[-6],[-5],[3],[2],[3],[10],[8],[1],[7],[10],[-5],[6],[-7],[-2],[7],[-7],[10],[-9],[4],[-6],[3],[-6],[-4],[-5],[-6],[6],[1],[9],[-6],[-4],[-6],[8],[-5],[-3],[-10],[-5],[7],[-2],[-10],[-1],[-5],[8],[-6],[6],[7],[5],[-5],[1],[9],[8],[-3],[10],[6],[-2],[-2],[-5],[-7],[-3],[-9],[4],[-2],[-9],[-9],[-8],[4],[-8],[1],[-6],[2],[5],[10],[-3],[4],[-9],[8],[1],[10],[9],[-10],[-10],[3],[9],[7],[-10],[5],[5],[7],[2],[5],[-4],[-5],[-2],[-5],[-6],[6],[-9],[-5],[-4],[8],[-3],[1],[-8],[-7],[10],[2],[-2],[-1],[3],[5],[-2],[9],[-1],[-2],[9],[9],[10],[-2],[-8],[9],[-1],[-4],[-1],[7],[-2],[5],[-3],[-5],[-1],[7],[4],[-3],[-6],[5],[6],[-4],[6],[-9],[-4],[10],[9],[9],[-2],[-8],[1],[4],[-3],[-2],[-4],[5],[-10],[6],[-8],[2],[3],[9],[9],[-6],[4],[5],[-9],[-3],[-10],[1],[9],[-5],[-6],[4],[7],[-7],[9],[-2],[6],[1],[-10],[-7],[7],[-1],[-4],[-2],[-8],[-1],[-7],[-8],[2],[5],[-3],[-10],[-5],[-9],[7],[-5],[-8],[3],[9],[-7],[4],[3],[7],[-8],[-9],[8],[9],[9],[7],[8],[7],[-2],[10],[-9],[3],[-7],[-7],[8],[4],[-1],[-8],[2],[-7],[1],[2],[1],[3],[-6],[-1],[3],[4],[10],[-10],[5],[4],[-6],[-7],[10],[-9],[9],[2],[-1],[-3],[7],[4],[7],[10],[7],[-6],[6],[10],[-4],[8],[2],[-7],[-1],[1],[4],[-10],[8],[-3],[-2],[-10],[2],[3],[8],[10],[2],[-6],[-7],[5],[1],[-1],[10],[8],[-7],[-10],[-1],[-8],[-8],[3],[-6],[-6],[10],[1],[6],[-5],[-2],[2],[10],[-7],[-8],[-6],[1],[5],[6],[-5],[-2],[-9],[4],[10],[-7],[-7],[-3],[-10],[-8],[2],[6],[-8],[-3],[-6],[1],[-9],[4],[-5],[-1],[-10],[-2],[-7],[7],[-2],[4],[2],[1],[7],[-1],[10],[6],[-6],[1],[-1],[-8],[9],[10],[-9],[-1],[2],[4],[-5],[2],[-8],[7],[-6],[9],[-3],[5],[3],[9],[-7],[7],[-3],[-6],[6],[-9],[-4],[5],[5],[-10],[-4],[6],[1],[5],[7],[7],[-10],[2],[5],[-10],[-10],[3],[1],[6],[9],[10],[-8],[3],[8],[-5],[-10],[10],[9],[5],[4],[6],[-8],[7],[-9],[7],[10],[-3],[4],[8],[-4],[6],[7],[3],[-2],[9],[-6],[9],[8],[-5],[-9],[-6],[2],[5],[-7],[-7],[-8],[-2],[2],[1],[6],[9],[7],[-7],[-4],[-1],[-7],[-1],[-8],[4],[-3],[-6],[-5],[-6],[-6],[1],[6],[-7],[2],[5],[8],[-10],[-3],[-1],[-1],[-8],[-7],[5],[-3],[-9],[9],[2],[-3],[-8],[2],[-10],[9],[5],[-3],[7],[-3],[-8],[7],[2],[-6],[10],[2],[9],[-2],[-8],[-10],[7],[8],[-3],[10],[5],[-5],[4],[6],[-4],[9],[-6],[-10],[6],[-3],[8],[-5],[-5],[9],[-6],[-8],[-2],[3],[6],[4],[-2],[6],[3],[6],[-7],[4],[-2],[-10],[-3],[-7],[-8],[9],[-9],[-10],[4],[3],[-6],[-7],[-4],[-8],[1],[6],[-2],[2],[-7],[-4],[3],[7],[-8],[5],[10],[9],[8],[4],[-6],[-4],[-8],[-2],[-7],[6],[1],[-9],[5],[-6],[-10],[4],[-2],[5],[-10],[3],[5],[5],[-8],[-2],[9],[-6],[-9],[-7],[-10],[7],[8],[1],[6],[-10],[-9],[4],[-10],[5],[-4],[-2],[-6],[7],[5],[2],[-9],[-9],[-10],[-6],[8],[-5],[-1],[-9],[8],[1],[-3],[-6],[3],[-6],[7],[8],[-7],[-4],[-7],[5],[8],[-4],[-1],[-10],[-9],[2],[5],[-2],[-9],[-9],[-6],[-2],[-3],[-10],[-9],[-8],[9],[4],[7],[10],[6],[-7],[-7],[-1],[7],[5],[-6],[6],[5],[2],[3],[9],[-3],[1],[-8],[5],[4],[-6],[3],[9],[5],[5],[1],[3],[-9],[10],[-8],[-3],[3],[-1],[6],[6],[2],[-1],[9],[-6],[4],[-10],[-7],[2],[9],[-8],[-4],[-7],[7],[-9],[-8],[3],[9],[6],[7],[-4],[5],[7],[6],[-8],[5],[3],[-6],[-6],[10],[6],[-2],[-9],[-6],[-3],[-7],[4],[-1],[-6],[2],[6],[-9],[-5],[-9],[8],[8],[-9],[-4],[5],[3],[2],[3],[4],[7],[-4],[3],[4],[-7],[6],[2],[7],[-9],[-2],[5],[2],[-3],[10],[2],[-1],[3],[8],[5],[7],[-3],[-8],[-7],[6],[-3],[9],[-4],[-8],[7],[5],[1],[8],[3],[-7],[8],[-10],[6],[-7],[-5],[9],[9],[-6],[8],[2],[-1],[5],[-4],[5],[7],[-6],[5],[-7],[6],[-4],[-4],[8],[8],[8]], dtype = "uint32")#candidate|5283|(1050, 1)|const|uint32
call_5282 = relay.TupleGetItem(func_2401_call(relay.reshape(const_5283.astype('uint32'), [10, 15, 7])), 0)
call_5284 = relay.TupleGetItem(func_2403_call(relay.reshape(const_5283.astype('uint32'), [10, 15, 7])), 0)
output = relay.Tuple([call_5277,call_5280,call_5282,const_5283,])
output2 = relay.Tuple([call_5278,call_5281,call_5284,const_5283,])
func_5285 = relay.Function([], output)
mod['func_5285'] = func_5285
mod = relay.transform.InferType()(mod)
mutated_mod['func_5285'] = func_5285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5285_call = mutated_mod.get_global_var('func_5285')
call_5286 = func_5285_call()
output = call_5286
func_5287 = relay.Function([], output)
mutated_mod['func_5287'] = func_5287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_957_call = mod.get_global_var('func_957')
func_958_call = mutated_mod.get_global_var('func_958')
call_5314 = relay.TupleGetItem(func_957_call(), 0)
call_5315 = relay.TupleGetItem(func_958_call(), 0)
output = call_5314
output2 = call_5315
func_5318 = relay.Function([], output)
mod['func_5318'] = func_5318
mod = relay.transform.InferType()(mod)
mutated_mod['func_5318'] = func_5318
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5318_call = mutated_mod.get_global_var('func_5318')
call_5319 = func_5318_call()
output = call_5319
func_5320 = relay.Function([], output)
mutated_mod['func_5320'] = func_5320
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5334 = relay.var("var_5334", dtype = "int8", shape = (6, 10, 16))#candidate|5334|(6, 10, 16)|var|int8
const_5335 = relay.const([[[4,-8,6,-1,9,-4,-10,8,4,-6,-2,-3,7,-8,4,10],[-3,5,6,-10,9,-3,1,-4,9,-1,-9,6,4,2,-3,7],[1,-9,-7,4,-3,6,10,2,-2,-2,7,-6,1,10,10,-2],[-9,-8,8,-4,-10,-8,2,2,2,4,2,-10,-8,5,-8,-9],[-5,-3,10,7,-8,10,4,-4,6,6,8,10,-6,5,3,-1],[2,3,-3,-2,5,1,-6,8,2,1,-9,7,-8,-1,6,-9],[-8,-10,5,2,-4,1,-9,-3,2,1,4,9,10,-1,2,7],[-4,-10,7,-1,4,-2,-3,-4,-6,8,-4,-10,-5,-1,10,-6],[4,-3,8,3,-8,-3,-9,-5,3,-5,-10,-1,7,-1,-1,3],[-5,-8,2,2,-6,10,3,2,-1,-5,3,6,-8,-9,6,-6]],[[-10,-1,-4,2,-2,-9,10,-3,8,1,-3,-1,6,2,2,2],[-10,6,-7,-8,-3,-4,-6,-5,4,-6,-5,-8,7,-2,7,10],[-6,-3,-5,10,6,2,-10,8,2,-10,1,9,-7,-6,4,2],[-2,-3,-4,6,8,5,4,-3,-7,7,-1,3,-9,10,5,-5],[7,-8,2,4,-4,7,2,6,3,7,-10,-1,1,4,5,5],[-7,2,8,7,-5,-2,8,-6,3,-6,6,-4,1,3,5,-8],[4,2,-6,-6,5,7,7,-6,-9,-3,-10,-1,5,8,3,-4],[6,1,-5,4,-4,-7,8,-1,-6,1,-3,8,8,2,10,10],[-2,-9,-7,-10,5,2,-1,-10,9,-4,8,4,7,-9,2,4],[-2,4,7,-2,1,6,9,8,1,-2,-3,-5,10,7,7,7]],[[-6,9,-5,8,5,8,1,-1,8,-1,10,1,-10,-4,-4,6],[-2,-5,-6,-2,8,6,-8,4,-10,8,9,-2,10,5,6,3],[-8,6,-1,6,8,1,-9,-3,9,1,-1,-8,8,4,-7,-4],[5,-9,-10,-8,-7,6,3,4,-1,10,5,-4,3,9,-4,5],[4,-10,10,-5,-8,-10,-10,-2,7,-2,2,-7,3,7,10,-9],[-5,-1,6,2,4,-6,6,5,2,8,-3,-10,-3,-4,-10,-9],[1,-2,3,2,5,4,-5,-7,-4,2,-1,4,1,7,10,-8],[4,-9,-1,-6,10,-8,-9,-4,9,2,10,2,-3,-5,-4,3],[1,7,-4,8,5,1,-10,-6,-10,-7,-2,6,-9,-8,5,1],[5,10,2,-5,6,8,-10,-7,1,-5,-4,-10,-3,5,2,-4]],[[3,10,5,-10,-1,9,3,4,-1,-8,-9,9,9,-9,-8,-1],[10,8,-7,8,-7,1,-4,-3,-3,1,1,5,-2,4,9,2],[-5,7,-9,9,-2,7,5,-1,2,4,2,5,4,-5,-3,6],[-9,1,6,5,10,3,1,8,8,7,1,-3,1,10,6,3],[9,-3,-4,2,-10,3,-1,-5,1,10,-3,-9,-2,8,4,-5],[-5,-7,-7,-5,6,-6,-7,5,-2,1,9,-10,8,-8,9,-7],[-2,-3,5,-5,4,-9,4,-10,-10,-4,3,-7,1,-5,-1,-5],[9,3,4,7,3,10,10,6,2,-9,3,8,-3,4,-5,8],[-5,-2,-3,6,4,3,-7,-6,-8,-6,10,5,-6,9,6,-7],[-2,-9,-7,9,10,-7,-3,-5,-7,2,-4,-5,3,-4,-5,9]],[[10,-10,-2,2,3,8,4,4,6,-1,2,1,-1,-6,5,-2],[3,6,3,7,7,1,-1,-3,3,-7,1,2,-4,8,2,-6],[4,-10,8,-2,-5,6,-9,4,6,-9,-1,1,-9,-5,-9,-8],[1,-9,-7,5,5,9,2,-8,-5,7,9,-1,7,9,-7,10],[-5,6,-1,4,-2,-1,-8,-3,7,-1,8,-5,10,-2,1,4],[10,-7,-10,-8,-6,9,10,-7,3,-5,1,-7,-2,-7,-10,8],[-10,-2,8,5,1,-7,7,9,-1,-3,2,3,-9,-8,9,3],[-3,-2,-7,4,-10,-8,-5,6,-9,10,9,7,2,-8,-3,4],[6,-6,2,10,1,8,-6,3,3,9,7,-9,3,-1,8,10],[-1,8,6,-5,7,4,10,-1,1,5,7,-6,-5,7,-4,9]],[[5,9,7,-8,-9,-8,-10,-2,-10,-8,2,7,2,-3,3,2],[-9,-9,4,1,-10,2,9,-2,8,-7,-3,-10,-10,-1,-4,1],[3,2,-9,-3,-3,10,7,-4,-3,9,-7,3,1,2,-7,1],[-5,9,5,5,-7,3,-1,10,7,-10,-6,4,6,-5,1,5],[8,-1,6,-2,-3,6,1,7,-5,2,1,1,2,-2,-9,-10],[-1,-1,-9,9,-9,7,2,7,1,9,5,-1,3,9,-10,-10],[-10,-7,5,4,-2,-3,2,-10,-9,-9,8,-1,-3,4,9,-2],[8,-9,-5,6,-3,2,10,2,-2,6,-9,2,7,-5,1,-7],[-7,1,-1,-1,-9,-2,6,10,3,7,-7,5,-4,-2,8,-3],[8,-8,2,-5,-2,-10,1,6,10,-7,4,-10,-4,5,-4,8]]], dtype = "int8")#candidate|5335|(6, 10, 16)|const|int8
bop_5336 = relay.bitwise_or(var_5334.astype('int8'), relay.reshape(const_5335.astype('int8'), relay.shape_of(var_5334))) # shape=(6, 10, 16)
output = bop_5336
output2 = bop_5336
func_5371 = relay.Function([var_5334,], output)
mod['func_5371'] = func_5371
mod = relay.transform.InferType()(mod)
var_5372 = relay.var("var_5372", dtype = "int8", shape = (6, 10, 16))#candidate|5372|(6, 10, 16)|var|int8
output = func_5371(var_5372)
func_5373 = relay.Function([var_5372], output)
mutated_mod['func_5373'] = func_5373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2546_call = mod.get_global_var('func_2546')
func_2547_call = mutated_mod.get_global_var('func_2547')
call_5387 = relay.TupleGetItem(func_2546_call(), 0)
call_5388 = relay.TupleGetItem(func_2547_call(), 0)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_5405 = relay.TupleGetItem(func_1872_call(), 0)
call_5406 = relay.TupleGetItem(func_1874_call(), 0)
output = relay.Tuple([call_5387,call_5405,])
output2 = relay.Tuple([call_5388,call_5406,])
func_5409 = relay.Function([], output)
mod['func_5409'] = func_5409
mod = relay.transform.InferType()(mod)
output = func_5409()
func_5410 = relay.Function([], output)
mutated_mod['func_5410'] = func_5410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1210_call = mod.get_global_var('func_1210')
func_1212_call = mutated_mod.get_global_var('func_1212')
call_5418 = func_1210_call()
call_5419 = func_1210_call()
output = relay.Tuple([call_5418,])
output2 = relay.Tuple([call_5419,])
func_5432 = relay.Function([], output)
mod['func_5432'] = func_5432
mod = relay.transform.InferType()(mod)
output = func_5432()
func_5433 = relay.Function([], output)
mutated_mod['func_5433'] = func_5433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_5434 = relay.TupleGetItem(func_402_call(), 2)
call_5435 = relay.TupleGetItem(func_404_call(), 2)
func_4087_call = mod.get_global_var('func_4087')
func_4089_call = mutated_mod.get_global_var('func_4089')
call_5460 = relay.TupleGetItem(func_4087_call(), 0)
call_5461 = relay.TupleGetItem(func_4089_call(), 0)
func_4398_call = mod.get_global_var('func_4398')
func_4399_call = mutated_mod.get_global_var('func_4399')
call_5473 = relay.TupleGetItem(func_4398_call(), 3)
call_5474 = relay.TupleGetItem(func_4399_call(), 3)
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
var_5508 = relay.var("var_5508", dtype = "uint8", shape = (320, 1))#candidate|5508|(320, 1)|var|uint8
call_5507 = func_2062_call(relay.reshape(var_5508.astype('uint8'), [5, 8, 8]))
call_5509 = func_2062_call(relay.reshape(var_5508.astype('uint8'), [5, 8, 8]))
func_2062_call = mod.get_global_var('func_2062')
func_2065_call = mutated_mod.get_global_var('func_2065')
call_5514 = func_2062_call(relay.reshape(call_5507.astype('uint8'), [5, 8, 8]))
call_5515 = func_2062_call(relay.reshape(call_5507.astype('uint8'), [5, 8, 8]))
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_5523 = relay.TupleGetItem(func_1380_call(), 0)
call_5524 = relay.TupleGetItem(func_1382_call(), 0)
bop_5525 = relay.bitwise_or(call_5514.astype('int64'), relay.reshape(call_5507.astype('int64'), relay.shape_of(call_5514))) # shape=(5, 8, 8)
bop_5528 = relay.bitwise_or(call_5515.astype('int64'), relay.reshape(call_5509.astype('int64'), relay.shape_of(call_5515))) # shape=(5, 8, 8)
func_609_call = mod.get_global_var('func_609')
func_610_call = mutated_mod.get_global_var('func_610')
call_5535 = func_609_call()
call_5536 = func_609_call()
output = relay.Tuple([call_5434,call_5460,call_5473,var_5508,call_5523,bop_5525,call_5535,])
output2 = relay.Tuple([call_5435,call_5461,call_5474,var_5508,call_5524,bop_5528,call_5536,])
func_5541 = relay.Function([var_5508,], output)
mod['func_5541'] = func_5541
mod = relay.transform.InferType()(mod)
var_5542 = relay.var("var_5542", dtype = "uint8", shape = (320, 1))#candidate|5542|(320, 1)|var|uint8
output = func_5541(var_5542)
func_5543 = relay.Function([var_5542], output)
mutated_mod['func_5543'] = func_5543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4087_call = mod.get_global_var('func_4087')
func_4089_call = mutated_mod.get_global_var('func_4089')
call_5559 = relay.TupleGetItem(func_4087_call(), 1)
call_5560 = relay.TupleGetItem(func_4089_call(), 1)
output = relay.Tuple([call_5559,])
output2 = relay.Tuple([call_5560,])
func_5566 = relay.Function([], output)
mod['func_5566'] = func_5566
mod = relay.transform.InferType()(mod)
output = func_5566()
func_5567 = relay.Function([], output)
mutated_mod['func_5567'] = func_5567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_5568 = relay.TupleGetItem(func_1433_call(), 0)
call_5569 = relay.TupleGetItem(func_1435_call(), 0)
func_270_call = mod.get_global_var('func_270')
func_271_call = mutated_mod.get_global_var('func_271')
call_5574 = func_270_call()
call_5575 = func_270_call()
output = relay.Tuple([call_5568,call_5574,])
output2 = relay.Tuple([call_5569,call_5575,])
func_5576 = relay.Function([], output)
mod['func_5576'] = func_5576
mod = relay.transform.InferType()(mod)
output = func_5576()
func_5577 = relay.Function([], output)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5583 = relay.var("var_5583", dtype = "bool", shape = ())#candidate|5583|()|var|bool
var_5584 = relay.var("var_5584", dtype = "bool", shape = (1, 10, 3))#candidate|5584|(1, 10, 3)|var|bool
bop_5585 = relay.logical_and(var_5583.astype('bool'), var_5584.astype('bool')) # shape=(1, 10, 3)
output = relay.Tuple([bop_5585,])
output2 = relay.Tuple([bop_5585,])
func_5602 = relay.Function([var_5583,var_5584,], output)
mod['func_5602'] = func_5602
mod = relay.transform.InferType()(mod)
var_5603 = relay.var("var_5603", dtype = "bool", shape = ())#candidate|5603|()|var|bool
var_5604 = relay.var("var_5604", dtype = "bool", shape = (1, 10, 3))#candidate|5604|(1, 10, 3)|var|bool
output = func_5602(var_5603,var_5604,)
func_5605 = relay.Function([var_5603,var_5604,], output)
mutated_mod['func_5605'] = func_5605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4318_call = mod.get_global_var('func_4318')
func_4319_call = mutated_mod.get_global_var('func_4319')
call_5607 = relay.TupleGetItem(func_4318_call(), 1)
call_5608 = relay.TupleGetItem(func_4319_call(), 1)
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_5609 = relay.TupleGetItem(func_2927_call(), 2)
call_5610 = relay.TupleGetItem(func_2929_call(), 2)
output = relay.Tuple([call_5607,call_5609,])
output2 = relay.Tuple([call_5608,call_5610,])
func_5615 = relay.Function([], output)
mod['func_5615'] = func_5615
mod = relay.transform.InferType()(mod)
mutated_mod['func_5615'] = func_5615
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mutated_mod.get_global_var('func_5615')
call_5616 = func_5615_call()
output = call_5616
func_5617 = relay.Function([], output)
mutated_mod['func_5617'] = func_5617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_5711 = relay.TupleGetItem(func_653_call(), 0)
call_5712 = relay.TupleGetItem(func_654_call(), 0)
output = call_5711
output2 = call_5712
func_5717 = relay.Function([], output)
mod['func_5717'] = func_5717
mod = relay.transform.InferType()(mod)
output = func_5717()
func_5718 = relay.Function([], output)
mutated_mod['func_5718'] = func_5718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_788_call = mod.get_global_var('func_788')
func_789_call = mutated_mod.get_global_var('func_789')
call_5737 = func_788_call()
call_5738 = func_788_call()
func_2583_call = mod.get_global_var('func_2583')
func_2585_call = mutated_mod.get_global_var('func_2585')
call_5754 = relay.TupleGetItem(func_2583_call(), 0)
call_5755 = relay.TupleGetItem(func_2585_call(), 0)
output = relay.Tuple([call_5737,call_5754,])
output2 = relay.Tuple([call_5738,call_5755,])
func_5758 = relay.Function([], output)
mod['func_5758'] = func_5758
mod = relay.transform.InferType()(mod)
mutated_mod['func_5758'] = func_5758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5758_call = mutated_mod.get_global_var('func_5758')
call_5759 = func_5758_call()
output = call_5759
func_5760 = relay.Function([], output)
mutated_mod['func_5760'] = func_5760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_5806 = relay.TupleGetItem(func_3004_call(), 1)
call_5807 = relay.TupleGetItem(func_3006_call(), 1)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_5818 = relay.TupleGetItem(func_292_call(), 0)
call_5819 = relay.TupleGetItem(func_293_call(), 0)
output = relay.Tuple([call_5806,call_5818,])
output2 = relay.Tuple([call_5807,call_5819,])
func_5826 = relay.Function([], output)
mod['func_5826'] = func_5826
mod = relay.transform.InferType()(mod)
mutated_mod['func_5826'] = func_5826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5826_call = mutated_mod.get_global_var('func_5826')
call_5827 = func_5826_call()
output = call_5827
func_5828 = relay.Function([], output)
mutated_mod['func_5828'] = func_5828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5839 = relay.var("var_5839", dtype = "uint64", shape = ())#candidate|5839|()|var|uint64
var_5840 = relay.var("var_5840", dtype = "uint64", shape = (6, 14, 1))#candidate|5840|(6, 14, 1)|var|uint64
bop_5841 = relay.left_shift(var_5839.astype('uint64'), var_5840.astype('uint64')) # shape=(6, 14, 1)
output = bop_5841
output2 = bop_5841
func_5846 = relay.Function([var_5839,var_5840,], output)
mod['func_5846'] = func_5846
mod = relay.transform.InferType()(mod)
var_5847 = relay.var("var_5847", dtype = "uint64", shape = ())#candidate|5847|()|var|uint64
var_5848 = relay.var("var_5848", dtype = "uint64", shape = (6, 14, 1))#candidate|5848|(6, 14, 1)|var|uint64
output = func_5846(var_5847,var_5848,)
func_5849 = relay.Function([var_5847,var_5848,], output)
mutated_mod['func_5849'] = func_5849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5855 = relay.var("var_5855", dtype = "uint32", shape = (16, 16, 16))#candidate|5855|(16, 16, 16)|var|uint32
var_5856 = relay.var("var_5856", dtype = "uint32", shape = (16, 16, 16))#candidate|5856|(16, 16, 16)|var|uint32
bop_5857 = relay.greater_equal(var_5855.astype('bool'), relay.reshape(var_5856.astype('bool'), relay.shape_of(var_5855))) # shape=(16, 16, 16)
uop_5861 = relay.atan(var_5856.astype('float64')) # shape=(16, 16, 16)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_5869 = relay.TupleGetItem(func_3958_call(), 0)
call_5870 = relay.TupleGetItem(func_3960_call(), 0)
output = relay.Tuple([bop_5857,uop_5861,call_5869,])
output2 = relay.Tuple([bop_5857,uop_5861,call_5870,])
func_5872 = relay.Function([var_5855,var_5856,], output)
mod['func_5872'] = func_5872
mod = relay.transform.InferType()(mod)
mutated_mod['func_5872'] = func_5872
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5872_call = mutated_mod.get_global_var('func_5872')
var_5874 = relay.var("var_5874", dtype = "uint32", shape = (16, 16, 16))#candidate|5874|(16, 16, 16)|var|uint32
var_5875 = relay.var("var_5875", dtype = "uint32", shape = (16, 16, 16))#candidate|5875|(16, 16, 16)|var|uint32
call_5873 = func_5872_call(var_5874,var_5875,)
output = call_5873
func_5876 = relay.Function([var_5874,var_5875,], output)
mutated_mod['func_5876'] = func_5876
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5992 = relay.var("var_5992", dtype = "float64", shape = (3, 6, 1))#candidate|5992|(3, 6, 1)|var|float64
uop_5993 = relay.cosh(var_5992.astype('float64')) # shape=(3, 6, 1)
bop_6006 = relay.multiply(uop_5993.astype('int8'), relay.reshape(var_5992.astype('int8'), relay.shape_of(uop_5993))) # shape=(3, 6, 1)
uop_6010 = relay.acosh(uop_5993.astype('float64')) # shape=(3, 6, 1)
func_2321_call = mod.get_global_var('func_2321')
func_2323_call = mutated_mod.get_global_var('func_2323')
call_6012 = func_2321_call()
call_6013 = func_2321_call()
bop_6014 = relay.bitwise_and(uop_6010.astype('int16'), relay.reshape(uop_5993.astype('int16'), relay.shape_of(uop_6010))) # shape=(3, 6, 1)
output = relay.Tuple([bop_6006,call_6012,bop_6014,])
output2 = relay.Tuple([bop_6006,call_6013,bop_6014,])
func_6026 = relay.Function([var_5992,], output)
mod['func_6026'] = func_6026
mod = relay.transform.InferType()(mod)
mutated_mod['func_6026'] = func_6026
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6027 = relay.var("var_6027", dtype = "float64", shape = (3, 6, 1))#candidate|6027|(3, 6, 1)|var|float64
func_6026_call = mutated_mod.get_global_var('func_6026')
call_6028 = func_6026_call(var_6027)
output = call_6028
func_6029 = relay.Function([var_6027], output)
mutated_mod['func_6029'] = func_6029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_6053 = relay.TupleGetItem(func_3803_call(), 0)
call_6054 = relay.TupleGetItem(func_3804_call(), 0)
const_6057 = relay.const([[[-7.926702,-9.196689,-7.828331,-1.691391,-9.676635,8.354723,6.481735,-6.102441,5.963485],[-4.403558,-3.667908,-4.633856,-8.513861,2.820079,-5.893415,-9.415712,7.310924,-9.793132],[-4.975160,-7.242410,-0.668428,-0.933090,-2.684517,9.612062,7.085579,2.295933,-2.180715],[-2.316670,-6.085374,3.596585,2.375609,2.999399,8.009705,-0.134113,-8.961728,-9.917897],[-1.189942,-8.880415,2.575566,-6.733911,3.498820,-3.888997,9.039856,-8.263757,7.700626],[-3.505531,-8.526786,4.325392,-9.933550,9.441065,5.777297,7.419570,1.498342,-4.036141],[-7.668867,8.411579,-2.674112,8.460662,9.259353,5.205590,3.961719,4.559208,9.594555],[9.499236,-9.458932,8.855104,1.259793,2.955145,-4.009140,8.458649,-8.259051,5.484022],[7.588487,-9.634784,-7.388329,1.717898,-9.780625,4.689767,4.027495,1.695458,-8.103892],[7.092690,6.164827,-9.170759,-8.768235,-1.507506,-4.720397,9.777846,-9.781363,-4.954007],[6.405168,0.417908,-4.353599,-0.097789,5.411331,0.562397,-0.300847,3.195076,8.741725],[3.295760,-0.201791,-4.312408,5.033717,-2.105984,-2.125107,8.154897,-4.038338,6.864838],[7.858629,-3.910266,8.144514,-2.051030,6.227960,5.161237,7.611939,-6.014428,3.988702],[3.903383,4.624479,-4.047902,-3.482412,6.616798,-1.918704,-6.215316,-5.320952,9.506013],[-5.729317,3.050973,6.491381,5.026059,-1.480288,-3.012949,-9.476820,-0.241750,9.570846],[8.264665,-5.737256,-0.488137,2.378587,9.021227,-9.366098,3.957133,-7.190730,-5.638066]],[[-6.057702,7.461213,8.885142,-9.130260,9.790855,8.165524,2.280136,-7.317251,-6.000668],[2.555974,3.483293,9.137611,7.251544,1.148797,-4.810808,6.204702,4.255345,2.526344],[2.030111,-0.273385,-1.866847,3.901087,5.214998,-1.280029,7.902583,0.620395,-3.362071],[-4.077244,-9.559983,8.313513,8.763146,8.172407,8.993846,5.128068,-5.328368,3.136916],[-1.904501,-1.139485,9.850835,8.534453,-6.881525,1.243103,1.893126,-4.491706,3.290146],[-2.795510,7.180378,8.796377,-2.288182,8.645269,9.583996,-8.877721,3.482967,3.388141],[4.959166,6.527261,0.298794,-0.326986,-6.049886,-9.137001,-6.773755,-1.411904,-6.021634],[8.492719,6.609238,5.861214,3.263711,-2.754411,9.926333,4.911037,-1.522995,-8.081969],[-2.804305,-4.232232,-7.880692,-8.112675,-8.655809,-7.506521,4.030246,2.508538,-5.454347],[4.644613,-5.051359,-5.416612,9.462098,-1.887798,7.808788,7.859696,7.183924,-8.636492],[6.990042,8.169867,-6.403659,-0.800715,9.222474,-4.731934,5.076149,7.704009,8.454756],[3.339685,-0.347159,-2.956761,-6.662350,1.901282,2.873343,5.606169,-7.276929,-0.639717],[-4.495947,-5.840710,7.655300,4.257656,-2.293032,-1.152645,0.058727,-0.201654,-5.102781],[2.132265,6.541429,-9.094834,-0.046934,7.584598,-4.893348,6.916716,-1.049374,-2.732744],[-9.988689,-6.120424,4.516126,-1.935132,-0.115563,-5.041188,0.986753,-0.500118,-5.443163],[-3.789253,-8.028999,3.282540,4.488084,-2.558885,5.878707,5.885381,-5.416810,-7.707798]]], dtype = "float64")#candidate|6057|(2, 16, 9)|const|float64
bop_6058 = relay.power(call_6053.astype('float64'), relay.reshape(const_6057.astype('float64'), relay.shape_of(call_6053))) # shape=(2, 16, 9)
bop_6061 = relay.power(call_6054.astype('float64'), relay.reshape(const_6057.astype('float64'), relay.shape_of(call_6054))) # shape=(2, 16, 9)
func_4343_call = mod.get_global_var('func_4343')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_6071 = relay.TupleGetItem(func_4343_call(), 1)
call_6072 = relay.TupleGetItem(func_4345_call(), 1)
func_1860_call = mod.get_global_var('func_1860')
func_1861_call = mutated_mod.get_global_var('func_1861')
call_6078 = relay.TupleGetItem(func_1860_call(), 0)
call_6079 = relay.TupleGetItem(func_1861_call(), 0)
func_456_call = mod.get_global_var('func_456')
func_460_call = mutated_mod.get_global_var('func_460')
const_6082 = relay.const([9,8,6,-1,-5,-7,-1,8,-1,5,10,10,3,-2,-3,1,-7,-3,6,-5,-7,4,3,7,6,6,9,4,1,7,1,5,10,2,3,7,-2,-7,4,-8,9,10,3,2,-10,-9,8,10,3,-5,1,-6,2,-7,1,-9,-3,-8,1,-2,8,5,-7,-7,-6,9,-4,-10,10,3,5,2,8,-4,-10,3,10,-8,-2,-9,5,4,5,-6,-3,8,10,6,8,1,6,7,-4,3,8,-2,2,-4,2,-3,8,3,-1,-8,-8,-6,4,2], dtype = "int32")#candidate|6082|(108,)|const|int32
call_6081 = relay.TupleGetItem(func_456_call(relay.reshape(const_6082.astype('int32'), [3, 9, 4]), relay.reshape(const_6082.astype('int32'), [3, 9, 4]), ), 0)
call_6083 = relay.TupleGetItem(func_460_call(relay.reshape(const_6082.astype('int32'), [3, 9, 4]), relay.reshape(const_6082.astype('int32'), [3, 9, 4]), ), 0)
func_617_call = mod.get_global_var('func_617')
func_618_call = mutated_mod.get_global_var('func_618')
call_6088 = relay.TupleGetItem(func_617_call(), 0)
call_6089 = relay.TupleGetItem(func_618_call(), 0)
output = relay.Tuple([bop_6058,call_6071,call_6078,call_6081,const_6082,call_6088,])
output2 = relay.Tuple([bop_6061,call_6072,call_6079,call_6083,const_6082,call_6089,])
func_6097 = relay.Function([], output)
mod['func_6097'] = func_6097
mod = relay.transform.InferType()(mod)
mutated_mod['func_6097'] = func_6097
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6097_call = mutated_mod.get_global_var('func_6097')
call_6098 = func_6097_call()
output = call_6098
func_6099 = relay.Function([], output)
mutated_mod['func_6099'] = func_6099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_6125 = relay.TupleGetItem(func_292_call(), 0)
call_6126 = relay.TupleGetItem(func_293_call(), 0)
output = call_6125
output2 = call_6126
func_6134 = relay.Function([], output)
mod['func_6134'] = func_6134
mod = relay.transform.InferType()(mod)
mutated_mod['func_6134'] = func_6134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mutated_mod.get_global_var('func_6134')
call_6135 = func_6134_call()
output = call_6135
func_6136 = relay.Function([], output)
mutated_mod['func_6136'] = func_6136
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_6208 = func_3356_call()
call_6209 = func_3356_call()
output = call_6208
output2 = call_6209
func_6240 = relay.Function([], output)
mod['func_6240'] = func_6240
mod = relay.transform.InferType()(mod)
output = func_6240()
func_6241 = relay.Function([], output)
mutated_mod['func_6241'] = func_6241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3541_call = mod.get_global_var('func_3541')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_6250 = func_3541_call()
call_6251 = func_3541_call()
func_6026_call = mod.get_global_var('func_6026')
func_6029_call = mutated_mod.get_global_var('func_6029')
var_6253 = relay.var("var_6253", dtype = "float64", shape = (18,))#candidate|6253|(18,)|var|float64
call_6252 = relay.TupleGetItem(func_6026_call(relay.reshape(var_6253.astype('float64'), [3, 6, 1])), 2)
call_6254 = relay.TupleGetItem(func_6029_call(relay.reshape(var_6253.astype('float64'), [3, 6, 1])), 2)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_6272 = relay.TupleGetItem(func_1544_call(), 0)
call_6273 = relay.TupleGetItem(func_1545_call(), 0)
uop_6285 = relay.sqrt(call_6252.astype('float64')) # shape=(3, 6, 1)
uop_6287 = relay.sqrt(call_6254.astype('float64')) # shape=(3, 6, 1)
uop_6296 = relay.exp(uop_6285.astype('float32')) # shape=(3, 6, 1)
uop_6298 = relay.exp(uop_6287.astype('float32')) # shape=(3, 6, 1)
var_6304 = relay.var("var_6304", dtype = "float32", shape = (3, 6, 11))#candidate|6304|(3, 6, 11)|var|float32
bop_6305 = relay.bitwise_or(uop_6296.astype('uint16'), var_6304.astype('uint16')) # shape=(3, 6, 11)
bop_6308 = relay.bitwise_or(uop_6298.astype('uint16'), var_6304.astype('uint16')) # shape=(3, 6, 11)
output = relay.Tuple([call_6250,var_6253,call_6272,bop_6305,])
output2 = relay.Tuple([call_6251,var_6253,call_6273,bop_6308,])
func_6321 = relay.Function([var_6253,var_6304,], output)
mod['func_6321'] = func_6321
mod = relay.transform.InferType()(mod)
var_6322 = relay.var("var_6322", dtype = "float64", shape = (18,))#candidate|6322|(18,)|var|float64
var_6323 = relay.var("var_6323", dtype = "float32", shape = (3, 6, 11))#candidate|6323|(3, 6, 11)|var|float32
output = func_6321(var_6322,var_6323,)
func_6324 = relay.Function([var_6322,var_6323,], output)
mutated_mod['func_6324'] = func_6324
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6331 = relay.var("var_6331", dtype = "float64", shape = (14, 15, 16))#candidate|6331|(14, 15, 16)|var|float64
const_6332 = relay.const([[[6.930820,5.906530,1.946189,7.280601,2.774561,0.109810,-7.185904,4.153964,0.221837,6.886675,8.296764,8.615272,-3.635036,-3.605980,7.471458,-3.042373],[-9.577076,4.619116,-4.946676,7.362255,9.698970,3.980737,-8.235201,-0.245086,-5.143607,0.962307,-5.462520,-2.736679,-3.991051,-4.794505,5.584422,-4.173395],[-4.762264,6.866599,-8.747310,-0.692959,7.063755,-4.265026,-5.891340,8.742665,-2.842252,-6.664108,9.723567,5.922569,0.351759,7.728881,-0.848387,-1.565466],[7.637357,-8.489421,-5.904223,-0.969999,-2.605113,7.408487,6.827482,7.386867,-6.754463,-8.665887,2.969525,7.850322,9.888182,8.967016,4.779107,-8.048356],[4.840702,-2.828002,1.931263,7.538768,2.025113,-1.325176,2.062675,8.585811,2.748474,4.038088,7.208370,5.519950,4.756310,6.567677,-7.602005,-0.411188],[-2.587236,-4.353754,6.992856,1.053672,-2.544046,9.667724,-8.954625,3.254740,9.656787,-4.735824,-4.605760,9.207852,-8.242237,-0.400508,6.772548,-9.493896],[4.586545,7.574912,-3.774334,-8.728880,1.786394,-2.356760,-5.251751,6.029515,-6.465372,-4.372952,-3.061833,-9.018250,-2.896447,2.838255,7.278301,6.465507],[-9.836599,9.007172,-3.649137,-6.662791,-7.772412,2.016207,-4.643564,-5.364535,-0.719416,5.136720,-5.052833,4.287033,-9.973057,-1.901288,-8.576238,0.928716],[4.766838,1.982850,-4.351210,9.931534,-9.614275,7.593001,9.124308,8.601071,-5.588854,-5.664347,-9.292312,-0.151464,2.278950,7.757597,-2.043750,-3.902562],[0.501114,8.511400,6.366441,-5.178845,5.044123,0.224079,1.323290,-5.161123,4.873370,0.662224,-1.958443,7.683389,-6.312895,7.577210,0.918420,-3.489407],[2.419035,-2.409956,-1.712745,-2.402874,-2.037202,9.426388,-4.383724,5.076546,-0.538283,-0.792106,-8.359139,-5.050749,-7.805325,-9.598670,-2.796522,-7.339251],[-7.326541,-9.107069,-9.939611,1.206156,-2.898176,-0.255835,-1.437524,8.075240,-7.791993,-8.852651,1.468878,-7.044190,-2.595153,3.719493,8.303617,3.254036],[-3.983396,6.670946,-9.169312,0.958927,6.663521,-5.034182,0.307370,-5.663636,1.701406,9.024196,-7.524233,-6.304836,-5.922647,2.309856,7.273729,5.524338],[-2.170730,-1.826088,5.712840,-5.372822,-8.751838,8.126274,-8.899656,3.070798,-6.095374,-6.780118,-2.938823,5.060923,-9.547090,5.378360,4.250496,9.600587],[5.117111,1.950939,6.318490,2.086783,-8.959975,5.357334,-8.663494,-8.598737,4.703291,5.480819,3.794292,-3.881365,5.562324,5.314651,8.452694,6.186447]],[[5.356975,7.519418,-6.483117,-1.298643,3.893937,4.189676,-7.808848,-1.677660,-7.396586,-5.644855,5.242352,3.895736,-6.950143,3.812553,2.195652,-7.181156],[0.010264,5.278718,-8.961122,-3.156272,9.995182,1.592997,8.624622,-9.869311,-0.214665,1.086411,5.854261,-2.162299,-7.408486,1.872822,-6.004837,-9.440680],[-4.424388,1.924129,9.156000,-3.180504,8.408664,-4.625068,-2.188327,-4.976610,9.337499,-9.129798,-8.041650,-4.455698,-0.741264,-1.531430,1.712152,1.402813],[-2.454069,-4.182180,-2.230656,2.079282,8.181973,2.850728,-8.789057,-1.253886,6.424910,-3.027346,7.542813,-4.786735,1.277691,0.978575,4.941354,-7.023282],[2.822128,8.701648,1.231588,-5.546074,4.474160,-1.603307,6.837416,9.009240,4.084030,3.543513,2.668992,5.833169,-0.508499,5.920729,6.021919,-9.340174],[6.855878,-0.070123,-3.660681,1.219499,-3.645540,7.697696,-6.541521,4.672011,-4.962391,-7.629422,-0.477886,-3.217288,-9.428388,5.857926,3.628569,8.689733],[0.193322,-2.039678,-8.907108,1.906815,8.960021,-1.326310,-3.877348,-5.544813,-0.370020,-8.891301,-1.329449,-9.940439,-5.083104,-5.660112,0.135503,-5.216386],[4.155140,-0.219214,-8.237095,1.194023,-0.090090,0.137560,3.660242,8.554659,6.548004,-5.675464,1.011056,-9.111291,-4.393846,4.513289,-8.191123,5.329010],[-2.385318,6.423291,6.983584,5.126814,0.011194,-0.870155,-7.006676,-7.815719,1.095282,2.070822,2.265977,4.969430,-9.809842,8.945181,-1.023182,-0.608353],[-7.121036,-7.393213,-4.594008,6.372138,-1.490278,-1.560113,-1.863446,-3.379445,-9.942448,-4.745838,-9.321771,5.106375,-3.413653,5.588897,9.679758,-8.461867],[-9.737371,-3.622949,-8.081561,-9.103889,9.434554,1.958606,9.245719,-6.665621,2.278388,-8.429440,-2.712195,-3.112024,-6.240554,3.408513,9.476809,-4.704768],[-2.755465,3.769765,-3.980466,-7.597760,-6.095877,1.535713,2.908968,1.516973,-0.715175,-0.277650,-9.971733,-7.911735,3.370837,-3.205381,0.906794,-5.933937],[5.091972,-4.542029,6.513405,-3.872660,-1.976730,7.885088,3.354116,-2.015414,-3.665047,-5.249317,6.237257,-7.202734,-9.371529,2.146213,2.913436,-1.222858],[6.648686,-5.080106,8.618740,3.524667,0.412291,4.338438,1.909800,-8.322761,0.892020,-4.426015,8.112166,8.430138,-3.979241,3.334006,-3.546210,-4.946894],[-7.147326,-4.600044,3.799189,1.842444,-9.515996,8.138749,-7.475369,-4.563258,-9.960711,-8.260477,5.722417,-4.380322,9.339559,8.765813,9.766968,5.964415]],[[-4.560661,0.065749,7.292137,-4.005872,7.866740,-5.619586,-9.124767,9.573419,5.938496,-5.771852,8.803727,-0.591151,8.086333,-8.777708,-8.317016,-3.875446],[3.040715,-2.085051,9.345567,2.904719,2.486358,-3.379748,-7.896386,-0.033415,-7.886084,-6.780176,9.776568,-7.487401,-7.820883,4.544272,-9.272873,1.692390],[1.699599,1.137265,7.292344,-8.943377,-1.161027,-2.334160,-7.399848,-7.302904,8.816071,1.722653,-8.993759,9.311116,-2.279507,1.555122,4.480694,2.865826],[-6.391891,3.782779,0.990677,-2.509003,-0.497607,-9.195371,-0.191367,4.587645,0.710669,-1.210396,-4.533541,-3.605420,7.304823,-7.965750,-5.616286,2.518074],[-8.471542,-3.075301,-7.799940,4.453756,4.028984,-2.727864,-8.965792,-3.601162,-1.213724,4.726932,-5.938846,6.054096,6.379748,-1.737305,0.633777,3.925118],[-6.562793,0.401338,-6.261454,-8.894832,-4.969790,4.503188,-5.633612,-0.914046,5.134794,-5.913291,3.069669,2.545416,0.671623,5.004018,6.577774,-2.237799],[-7.004560,7.198860,-6.245694,8.499299,-0.642877,9.736088,-3.993819,2.675017,-9.637924,3.595574,5.496392,-5.969008,7.806387,-6.180334,-5.541226,-6.957576],[-7.125364,-7.223368,2.467421,-9.427458,-5.709970,8.804763,3.723929,-4.049002,-5.797735,-1.621610,-3.311997,-7.871841,-9.578390,4.611851,0.340113,4.128209],[7.506832,-5.204768,4.125564,-9.430142,-1.786997,-5.863781,-3.068318,2.959139,3.902730,-7.633723,2.991243,5.903589,5.312440,-8.511834,-9.493078,0.029213],[4.453898,3.398875,-2.584213,4.690748,2.956700,-0.729490,-6.712907,-3.738295,8.016853,-1.160881,2.108006,-0.096185,-1.602862,8.117932,8.798519,-1.715306],[-1.926870,1.803548,6.786932,1.784074,2.218316,-4.899264,-8.260412,8.998818,7.361899,-5.612721,6.027769,-1.991606,6.181386,-1.201428,-0.453203,-9.721806],[-7.745614,8.622244,-4.808201,-7.716876,-8.628934,5.868552,4.164338,7.579836,-2.669970,5.182973,-7.756146,9.514229,7.027510,-3.839806,-1.715986,-3.964167],[9.694359,-5.894735,2.636957,9.325609,7.303618,-4.325328,0.368930,-3.860083,2.034106,3.619495,5.314892,9.179080,-3.332254,-6.106368,-0.768609,-6.212597],[-4.526118,4.488924,3.052870,3.039191,-3.581556,-6.508660,6.663860,9.784851,-5.515579,3.916629,-9.244390,4.669611,-0.549427,0.276126,-1.029761,-9.952992],[8.137877,-7.415033,-0.382491,8.712360,9.022984,-3.560224,-7.062625,7.058099,-5.774736,-0.003433,-3.155612,-8.033005,8.611282,1.093945,5.127697,-0.642932]],[[-3.936883,6.595178,4.226222,1.478763,-5.842475,3.485978,6.038987,-8.421802,0.909016,-5.763027,-0.341844,0.967425,3.608808,0.472771,-8.616890,5.170256],[1.081666,-8.013019,3.679398,3.721812,7.635144,8.757855,-6.913178,9.298302,-4.294917,4.078596,-4.765706,7.374501,9.955298,-8.440821,-1.545089,-4.043659],[-1.190199,-3.414281,-1.711045,-4.698494,9.436348,5.070440,0.981726,4.261828,-6.741518,-4.942247,9.638006,-8.797875,-1.761793,1.162631,-8.100382,-0.405159],[-2.191822,7.661814,1.975163,-5.190533,0.094678,-9.595480,-5.128326,-6.808621,-2.039540,4.659688,-1.102273,-3.471627,-3.253975,-3.810070,-8.224713,-0.679801],[9.216029,7.585262,0.936815,4.141140,0.031358,7.286431,-9.288850,0.330758,-8.275792,-3.737550,-1.657994,2.118226,-3.076283,-3.236901,0.276982,7.639709],[-9.908306,2.980149,7.091642,-2.468637,-5.631524,-9.014921,2.603309,2.956133,7.044390,6.544556,-0.831001,-1.447377,-2.172025,7.159704,8.458775,-1.280501],[-4.366991,0.713199,8.259903,-6.165316,8.595646,-3.400254,-1.885429,-9.719629,1.763243,-8.378417,6.745215,8.133741,8.199297,4.234490,7.761103,-8.630214],[1.787781,8.759114,3.082475,-7.529074,6.285196,8.241067,-7.055783,9.353397,3.772142,2.713912,-1.472145,-0.184692,-7.969826,4.961630,-7.706965,4.914498],[7.320356,-3.880503,-0.658789,-9.969894,0.456795,-2.911341,7.166063,5.436200,7.494299,1.315465,8.988611,6.077683,2.402673,-7.530031,-4.056368,1.457863],[-0.540576,-0.334913,-6.754209,-9.859314,-4.704329,7.484202,-5.490653,7.966776,-8.412881,-5.382425,-4.630771,3.612272,-7.071625,4.844099,2.775798,-7.252855],[-4.326081,-3.406757,9.735779,-6.881741,3.799248,-3.124613,1.154864,0.168729,-4.825585,7.884052,7.699308,7.679938,-6.729503,-4.899323,8.707430,-2.791703],[1.213581,5.899897,7.742522,5.273056,1.329294,2.153425,0.267890,-4.398012,-5.505171,-8.492388,-4.806718,8.227907,3.994136,-3.766479,-4.571287,-8.138077],[-3.001322,9.118895,-2.550244,-6.950174,-5.406431,-4.828867,4.463846,5.391226,-3.766553,1.240295,5.005466,-6.356383,8.942340,-4.608936,4.976455,7.599355],[-6.690613,8.550686,7.141162,-0.498834,7.506584,4.353845,-7.923268,-2.148120,9.359089,3.244047,-3.257054,5.281150,9.021456,-5.219642,-3.234315,-4.166232],[-0.421530,6.185815,4.949892,7.579673,-5.266738,6.689047,9.830579,-6.555832,-3.073481,-3.262355,3.242568,-4.401399,5.976034,9.124208,-5.731015,-6.061320]],[[9.718676,0.334399,9.293344,-6.412284,5.151903,-3.757313,4.882295,4.848793,2.324810,9.916589,0.474992,9.961601,-8.181545,7.859849,-4.071012,1.610402],[2.631935,-8.356176,5.092088,3.758095,2.780683,3.630007,-3.196905,-1.296580,-2.940114,-6.451719,0.787501,-0.545732,-2.415508,-4.837971,2.615069,-4.171522],[-3.545976,-2.768363,5.711344,2.143319,7.274603,-9.310140,0.102143,2.723001,-7.066345,-5.233228,4.488578,5.181772,-1.420218,-2.135294,5.491579,-3.588325],[-7.165786,3.720402,-9.341646,-8.661770,4.652952,6.159111,6.544709,1.781245,-5.711044,3.689397,-0.501476,5.385997,-7.215830,3.475842,4.641315,-7.419858],[-0.001381,9.334717,-6.979026,-0.136962,-3.446822,-5.744831,0.806613,8.956282,8.760122,4.596332,9.771058,-0.509475,9.074324,6.180930,-4.889480,-5.504548],[6.049154,9.254204,2.162056,-7.753793,-1.730635,2.937842,-7.601617,0.502421,3.813669,7.075870,-1.175503,-5.640630,0.395472,-1.265312,3.647802,-3.322748],[-5.957871,-0.312584,-0.050642,-1.510433,-3.091509,-4.570513,-1.652676,-8.244089,-7.337163,1.257274,-0.986369,-9.987388,2.390259,4.146027,8.025119,-6.179045],[2.347118,3.013502,4.267420,-8.267552,5.577899,-9.117168,6.622441,7.212098,-0.062248,-2.072446,1.626901,4.832516,3.495441,7.869934,-1.852085,-2.520831],[9.343854,3.169976,8.434450,-0.407523,-3.721908,8.961552,1.226317,-0.188896,5.302424,-2.896938,4.427314,3.213852,-0.652031,-5.287104,-4.198310,6.823049],[-0.080342,-0.002277,-5.847165,0.566734,4.801928,-0.867409,7.826075,3.166914,5.933677,2.275612,6.591173,5.775577,-1.959370,-3.931424,3.015474,-4.043394],[6.948676,5.283712,0.924120,-2.836997,3.311555,4.229205,6.458577,2.122831,9.819273,-1.494204,-5.614357,-1.897569,3.927583,0.233818,-5.737385,-2.066908],[3.928294,-8.813461,-9.153943,8.595732,3.037308,3.268111,0.812918,-6.661192,6.557552,1.840214,-2.360735,-0.869623,1.494474,-2.613816,0.928671,2.709315],[7.954008,3.123849,-6.050829,8.904236,-5.886856,6.189702,-6.530885,-9.101148,-3.362531,7.889676,4.972507,-3.381534,9.936398,2.697337,6.795387,8.397900],[-1.297660,8.135097,-5.156378,-7.073297,2.281283,-4.890764,1.961813,5.679062,7.347326,0.846196,0.373468,5.773615,-6.386565,9.961125,6.441410,-2.347673],[-1.672083,-7.753691,2.353553,1.502615,-1.972493,-3.647099,-4.004070,8.228739,-4.823165,-4.256857,-8.472417,-9.394583,-3.238834,4.141298,3.474073,8.709231]],[[8.851489,-2.626162,4.501166,4.843684,4.244619,0.062350,6.957293,3.114189,7.585011,3.316217,5.791185,6.359500,-4.436767,6.469717,-0.330832,4.968949],[5.355395,-2.561269,2.689876,-7.914238,2.230456,-5.836537,7.893520,-2.099264,4.753303,-9.648310,-8.602739,1.085331,-9.279493,-0.300155,9.097825,-4.634590],[9.097952,2.860185,-6.696434,9.323384,-6.673177,5.078803,-7.543577,-9.122823,5.857796,-2.772669,-6.430404,-9.082642,1.093225,-2.217830,-4.364723,4.439764],[2.991646,-8.474190,-4.857635,-4.944934,5.874816,-1.422027,2.947904,-9.916966,-6.173783,-6.711432,-0.856537,3.409000,9.052663,-1.051237,4.265569,1.525686],[2.666776,-8.154834,-9.636026,-5.249818,-5.135855,9.135795,1.774576,0.090076,-9.199958,8.064708,-8.362337,-4.686736,-6.279767,-8.110335,-2.721352,-8.118354],[8.817434,-5.566362,2.314437,-6.300576,8.789515,-8.711901,7.247540,-3.586024,9.290912,-0.880379,1.383978,-1.217700,3.388177,6.911580,-8.576523,4.184151],[-6.363744,2.097384,-1.635855,-6.537436,3.011437,3.482039,-2.363634,5.240921,0.327834,4.485121,-3.317166,-2.445657,-6.395668,-5.121157,4.432821,8.197454],[9.141041,-8.629366,-5.252630,6.049507,6.425067,-6.923090,9.715972,0.712849,1.909071,0.910790,-3.904028,0.417491,5.595006,-5.777584,-9.694268,-7.287254],[-0.342814,6.426468,3.339527,9.427797,2.717162,-0.017230,8.679934,3.258234,7.125944,-8.009371,-5.572626,-1.817861,1.079589,0.470393,-7.479204,5.507528],[-0.585035,4.128409,-5.465106,-8.879025,-3.565559,-3.528911,-4.759218,-8.745286,-1.931238,-4.927221,8.441497,-5.686542,5.194299,-3.974888,2.496805,-4.724674],[-8.421291,-3.812730,-7.037244,2.212876,2.735656,-7.785058,7.080297,8.733565,-8.400804,5.543386,2.853288,-2.008556,0.242144,-3.828232,6.652975,-6.764439],[1.610947,-8.672886,7.939125,-3.805938,7.842965,-6.886839,-8.279374,-3.252051,9.863983,-0.993374,2.152385,3.162336,5.492255,3.825855,0.527627,-3.910966],[-6.517182,-0.923508,-1.422739,5.940257,-8.746769,2.647681,8.070501,0.313860,3.280150,2.496114,-0.141505,2.482678,1.386555,-1.401782,-9.788319,7.390020],[2.201364,-3.688451,-4.373253,5.907470,6.347748,6.777828,-7.063025,-9.289933,-8.557054,-8.634083,-0.329663,-3.315458,9.931217,-1.102800,-6.402729,-8.430315],[-8.093565,4.667364,-8.859980,9.335206,7.861087,5.362275,5.378012,1.918197,1.317562,-0.064703,7.915470,2.742435,-6.137686,-9.525948,1.478109,-4.268051]],[[8.822608,1.382429,0.148880,-3.429212,2.701488,-4.165118,0.137275,5.111644,-6.954278,-9.553781,-2.341416,-4.825394,-6.174840,0.732497,7.654925,1.891938],[-8.243076,4.633553,5.724492,-6.428397,7.316848,3.165446,4.641470,3.280383,-8.256296,2.753258,-3.363603,5.125565,7.794080,-2.921819,7.361737,6.112954],[-2.817777,9.258757,-9.474415,3.688695,-0.184633,-2.500777,6.318497,6.887611,-3.879528,-9.677021,-6.762207,7.924091,4.987745,0.325523,3.179551,-7.382618],[6.549318,0.135259,7.032119,6.421612,4.375620,0.688144,2.964972,-5.187739,-4.441198,-3.865815,4.076285,-0.511848,-0.053789,5.116712,-1.490293,3.980673],[3.515578,-9.090887,8.243382,-0.298470,3.348784,2.759524,7.714418,-1.000542,6.893506,-0.201139,-9.444165,9.350642,-6.634984,-8.394680,-5.936302,-2.576578],[-5.944014,-4.421734,-8.126457,-2.106235,5.020555,5.949126,-2.659642,-7.059022,-0.351651,-6.969733,6.479403,3.191933,-4.473290,-5.892705,-0.814652,-4.975144],[0.496422,-0.125765,2.876192,-7.339421,8.093818,9.074313,1.180188,5.399037,6.704413,3.869372,2.922787,-8.011625,-8.736179,-1.504276,-3.772900,-7.893085],[3.261298,1.011509,9.090125,9.768471,0.270997,-2.284883,-4.924985,2.251302,6.702015,-2.543568,9.609934,-3.984687,-2.257092,-6.428793,8.229885,-2.535226],[-7.699063,-9.939170,2.659180,-6.741833,-9.455247,-9.902086,-8.196224,-4.031178,-9.192571,-8.214204,-8.438553,8.760976,2.759362,2.509466,-7.773584,6.078191],[9.507522,9.330501,-5.307945,-5.187592,-5.090440,4.474723,-0.317085,9.099593,9.489338,-3.992758,-8.018353,-7.033723,-5.039593,7.939714,5.652531,0.732397],[-6.350548,-7.789942,-3.157161,7.697090,2.303263,4.615298,1.402087,-5.192641,-4.493117,-8.621745,-3.833873,-3.067652,-2.571686,-4.647534,-7.695439,-7.642000],[-0.355072,7.701660,0.884083,6.541004,-3.720408,-2.349881,3.474131,-7.573641,-3.130579,1.866203,8.600724,0.400895,4.845075,7.098015,9.706779,-3.630140],[-1.270188,-0.254885,-0.275915,-0.827071,-0.212403,-6.367147,8.321988,7.622571,5.901979,7.644297,-8.306163,-0.570862,-3.070424,7.835669,-8.421072,2.451339],[-9.850258,-2.763124,8.169378,5.333928,-5.898839,-8.653448,-6.594402,0.796420,-1.650082,-2.270612,2.962218,-8.922309,-8.161653,3.957932,0.718142,-8.850102],[-7.307531,-7.610519,5.665989,8.651588,-3.770994,-0.916861,4.841781,-4.329997,-9.209662,-9.426570,-0.199576,7.394499,-6.761256,5.926907,1.670648,1.257999]],[[-6.656320,3.115493,0.652719,9.566382,-8.241226,-4.353246,7.684690,2.446689,6.697208,2.432463,-1.088564,4.101276,5.355698,-0.972925,-7.458194,-4.025491],[-1.255705,-8.101787,-8.776950,6.127449,3.126785,-1.642313,-0.895787,-9.798559,6.224301,1.801686,-3.692500,9.567416,0.154341,-6.706285,0.393012,3.477487],[9.483354,-1.394762,3.086891,-8.508288,6.370904,-0.012161,6.432872,-2.780443,-8.038132,-9.609350,-9.682548,1.231928,-9.654812,7.788804,-6.696636,2.152250],[-0.969822,-1.021405,4.824946,2.063258,9.787018,-7.033947,-3.343867,-0.618902,3.589860,-2.330568,-8.171657,5.961903,5.503991,-0.043286,5.023305,9.687596],[6.083478,-1.842605,7.946294,-3.612202,8.190273,3.515451,1.796530,-0.117385,-1.429932,-5.428946,-1.150874,7.662173,-3.195802,-5.367896,5.316334,6.842582],[7.578635,6.919198,9.892790,5.285045,4.728335,5.186232,-8.581066,7.684785,-3.547529,6.393396,0.690821,-0.104480,7.568405,-6.276931,0.388481,7.356036],[0.074480,3.719757,-8.457028,4.570885,0.399931,-5.290924,-6.418077,-4.120296,7.683048,-9.239515,2.741193,-3.988343,7.424182,4.132971,5.017839,0.555244],[-0.882274,1.733994,6.681445,-0.542526,5.088530,2.961253,-5.436811,-2.481595,3.601671,-4.802632,-6.024856,8.984782,8.910914,-6.041257,-4.899160,7.552732],[-3.573173,7.716724,2.256217,-1.249980,2.984722,2.517600,2.566657,6.855548,-4.735571,5.896682,5.968907,-4.627986,-4.007171,3.643055,-0.033163,1.953161],[2.895933,-6.925966,-5.512050,-5.728406,-5.392042,4.307132,0.922659,8.182460,-3.334860,-1.977400,6.732087,0.470680,0.306090,-7.457378,6.154342,-3.380300],[0.529860,-1.566549,8.699108,2.059462,-5.646627,-1.280306,7.365577,9.114908,-0.099311,1.975949,-2.625791,0.838282,6.230923,4.764636,7.756677,-1.128518],[-7.730873,-6.235480,9.574694,-6.238749,-7.085808,2.102506,-1.857280,-7.306677,2.771850,-7.364761,-6.038120,2.409195,-8.362864,-9.722722,4.840051,-3.489089],[7.581958,0.937465,-6.903872,-6.332653,-7.467611,-9.100687,-0.651833,-0.192757,7.750511,0.930539,-5.906636,7.272790,8.791261,0.424171,-0.059642,5.538513],[-9.708768,-1.855120,-7.582096,-8.629034,5.592646,7.296691,5.958392,7.554459,-7.934595,-6.753526,9.622604,8.865674,0.009066,4.158289,-6.333233,-5.771715],[-5.945520,1.238459,0.366608,0.310379,4.602525,9.396460,-7.335743,8.859796,9.825187,-0.514798,7.714643,-6.498986,-0.651708,6.001156,-7.004965,4.506757]],[[-4.786525,1.600744,-1.578179,-8.136207,7.381326,-4.797563,-3.727941,-9.846821,7.198766,6.699855,4.784089,-7.757535,8.043946,-0.610357,9.950141,-7.856956],[6.369483,5.324866,1.550103,3.486794,2.578402,-9.986816,1.898039,-7.869815,5.100274,2.019074,3.004932,-7.950703,8.524767,-9.362514,1.647320,4.428224],[-1.964831,-8.776104,-7.363264,-9.349363,-1.887798,-5.376016,7.107619,-5.043224,-1.258750,0.079697,1.355900,-0.391209,5.398782,1.308905,-0.832508,8.478605],[-5.493887,-5.327340,3.335013,-6.109757,5.067459,8.819002,6.916316,-1.838009,8.182360,3.830173,2.255989,-5.007745,-0.689936,8.967957,-9.230101,9.658746],[2.938931,2.733739,-6.976447,-3.252655,-9.657641,6.100226,8.904946,7.719279,7.057774,-8.846454,4.265174,6.289995,-7.493117,-6.963955,8.521901,0.301543],[2.751671,5.104456,9.558604,7.330894,1.291797,3.817908,-5.837411,-5.344488,-2.755314,0.418231,4.523904,7.331669,2.803578,-4.366235,-7.096382,8.977424],[-8.165148,1.128312,-5.619681,-7.139349,8.440920,3.278613,-3.173779,-6.398437,-3.287441,-5.462715,-1.741796,2.982068,7.578045,6.731864,-9.296723,7.401583],[7.545723,-8.067123,-7.502546,-7.631097,-4.799526,1.408977,8.723651,2.399592,3.326542,7.483137,-4.132168,-3.534901,-8.150836,4.188328,-0.528143,7.994645],[9.811450,-1.167425,-1.081092,-4.084896,-3.431581,-1.829416,6.798696,7.367873,6.186960,-6.900235,7.764471,-8.632719,-0.308874,-6.505957,-8.986543,3.120623],[2.752960,6.287863,-5.506878,2.179509,-0.358050,-5.468728,5.388924,-4.375999,-0.834537,-4.238993,5.363663,4.115666,-1.183173,8.678664,2.184205,9.981420],[-9.899666,5.535296,-8.186777,8.152718,-1.039018,-1.743493,7.755251,-2.275376,9.331741,9.095675,5.958145,3.688191,6.097866,1.742402,5.010481,1.314360],[1.394195,-1.975859,2.366832,-1.975584,8.101336,-2.598479,-8.737244,-3.287941,3.702044,-8.641087,-8.596417,0.101455,-5.661362,-1.429103,3.200886,7.966519],[-3.131340,-3.660302,2.337538,3.975622,9.349660,5.921449,4.042612,8.185258,-1.056902,4.657765,7.996593,-3.364142,8.241994,1.131617,-0.482598,-5.463576],[-5.918412,0.498589,4.803307,-7.901255,-1.514959,-1.016848,1.118277,-1.230322,-6.796816,-5.549791,-3.030197,6.256262,-5.637759,-2.429960,-4.643987,3.496600],[9.269957,-0.058782,-9.803669,0.149136,8.142169,-2.399518,-6.195708,-3.752513,-3.457504,-6.205276,3.319466,5.193191,1.534295,-7.742475,-8.306457,-7.375633]],[[-7.469737,-7.314494,-1.711153,4.255761,-0.581991,-1.062750,4.642566,7.869569,-4.219991,-7.657442,2.536256,1.751773,-7.615614,-4.140454,0.174998,-0.780648],[-2.675327,-3.276463,1.174452,-7.257619,6.718619,-2.298095,5.398685,9.159863,6.078099,2.376185,0.990489,6.264401,-4.566493,-5.649905,8.770592,-5.988598],[3.813759,-2.552429,-3.115657,-6.379658,5.180596,-1.955064,-5.461501,-5.478554,-0.531521,0.908914,-1.861973,6.382457,-8.953161,9.438118,-8.899114,4.725155],[-2.616200,-5.085159,-3.160162,2.474027,3.242429,-7.044775,1.391375,-3.442703,-6.140581,2.322693,-9.517708,-9.321738,-9.817927,-3.811990,2.543309,-6.698892],[3.480236,-5.184167,-1.822878,-5.788187,-7.647173,4.898949,1.734746,5.150956,7.268713,8.682825,1.967380,3.168438,6.461747,-3.894051,3.053283,-8.429798],[-2.614507,1.462179,-4.203040,-4.909276,-8.291445,-6.479070,8.920122,-8.245928,-3.793711,7.220420,6.207317,0.701160,-3.875921,0.280866,9.272469,4.620402],[-9.076378,-4.079957,-6.050449,9.500613,-9.043553,-4.993314,7.293527,8.218353,-1.794883,8.065162,9.651982,-3.408378,4.202141,6.496599,-7.176648,-3.539716],[6.469449,1.293438,7.678473,5.879922,8.173310,-0.576212,-7.884760,-0.910879,-1.580767,-4.120390,0.008193,0.638737,-1.348180,8.545164,7.955514,7.908121],[-6.108414,-2.508957,-4.266278,5.506876,-5.326987,-0.167208,5.259100,8.603407,9.630769,0.280091,7.690610,2.499112,-7.860620,-4.033590,-1.836893,-8.637872],[-8.024725,-0.508139,-4.614072,-6.884200,8.871547,8.865002,-7.262289,-3.377247,-5.799009,-1.293089,8.916710,8.183577,-7.220428,5.832666,-2.441998,7.637293],[3.064267,4.137181,7.472387,-5.896214,-7.893107,-0.640787,-8.112983,-9.893318,-0.697045,-1.406978,-7.900336,9.682127,3.920235,5.426694,3.638488,5.816736],[1.310125,-9.724688,-1.024803,5.691823,1.415106,2.543315,0.943468,-4.407826,-6.920955,4.749105,3.311799,4.747930,6.505233,-2.676392,2.237711,1.590988],[-0.341629,-0.596501,-3.957351,3.662995,5.076567,-6.130421,3.182983,-1.021910,4.863428,-3.035574,3.626971,-2.946999,9.364412,2.166850,-5.033909,2.422078],[-7.939047,8.358759,3.806562,-1.340645,-6.090752,5.034162,-2.253250,6.997873,1.606182,-1.155488,-1.019670,-3.501782,0.807922,-9.241724,-4.042315,-0.691956],[3.027635,-6.484806,-6.379823,4.956071,3.007847,-3.068435,3.783040,1.450503,-0.666064,2.557179,-9.703570,-7.853766,9.483386,1.492747,-9.367559,-3.588643]],[[-0.932688,-0.502634,-0.886269,0.037638,6.853447,0.965469,4.409788,3.192371,-5.290752,-1.126986,-1.226968,-1.186764,-1.159674,-6.654146,9.948890,-8.447415],[4.610605,-1.012455,2.236064,6.982504,-0.605551,3.587606,9.672317,4.816425,5.395428,7.876182,-5.941078,5.292142,0.034286,7.679308,-4.875791,-3.046510],[-6.609587,1.778072,-4.517362,-7.414013,2.200026,9.497586,6.815044,-9.771895,-9.263024,-1.803690,2.155339,3.934500,5.055614,9.525984,2.627572,5.241274],[2.144145,5.300869,6.972576,-7.464395,2.299479,-3.875796,-5.219987,3.368683,-1.410099,0.999942,1.226252,-0.076045,5.796429,-0.212295,-8.696250,-5.751677],[8.471886,9.899326,-8.389419,6.375885,3.662941,-7.702673,8.535306,2.287413,9.808053,4.289790,2.786749,-7.624203,-0.019201,5.541271,-7.355783,-5.138856],[1.431556,4.359559,7.525660,8.247143,-3.387877,-0.289577,1.885309,1.733115,-9.124010,1.617992,-2.767150,-7.610852,3.864516,4.073223,7.688617,5.566087],[-8.921030,-5.845309,8.503269,-0.113773,3.914696,5.275727,-3.206431,-3.131788,-3.088403,3.719716,3.793863,6.719764,7.716156,-7.193914,-3.579047,-5.212848],[-1.428420,-0.759561,-4.990208,1.124083,0.446397,4.554089,3.845586,-1.751261,4.290887,1.608640,4.586101,1.873763,6.806255,8.974156,4.518654,-1.791238],[9.116051,-3.330278,-9.347105,4.782844,-9.719815,7.044910,-2.818373,7.663788,2.049959,-3.617615,3.224478,-3.485602,-8.078051,-2.761616,1.304936,1.347362],[5.481534,-7.781665,-7.927453,6.711082,-1.464678,-8.458734,-5.340595,7.315716,-4.254301,-0.809286,4.464011,0.470119,1.769759,-8.258102,-9.707215,9.585670],[5.355079,6.225156,0.561216,-8.174493,-4.516639,4.642406,0.544647,-4.447700,-1.962755,9.553450,2.945327,1.749290,6.039825,3.221016,-1.727815,7.808730],[4.959402,8.704633,-2.491792,-1.417490,-8.618919,3.586228,-1.615505,-1.254413,3.179596,8.449969,-7.564217,9.206604,-4.989653,7.786915,1.628936,-7.891378],[-6.136065,9.141542,1.650604,2.444542,8.679922,1.429879,-4.206466,0.440097,-4.434333,9.762940,3.617295,-4.794615,3.735305,-8.532055,-0.507611,5.162949],[-1.470289,7.065689,8.633624,-7.356013,-9.966604,-2.466400,5.927901,-8.657709,-4.348135,-4.329848,-3.354232,9.614406,-9.212114,-2.584465,-7.100146,3.258739],[-6.668246,0.501200,8.029902,7.771079,3.933813,5.052348,1.760033,-0.241347,6.098435,6.378592,2.415109,8.756347,6.455236,9.658113,-6.148494,-9.640856]],[[7.051421,-8.292602,8.470487,-2.083375,3.276077,3.030975,4.427966,6.981179,-4.280645,-4.357204,8.288398,-4.635089,4.298389,6.980348,-2.049662,7.536415],[0.997750,2.560085,9.482691,6.538317,9.339516,4.439169,0.497614,8.586772,1.377891,3.134610,6.021907,2.116496,1.795538,-6.929389,8.236244,-2.333249],[0.860835,6.578638,0.459054,-1.585855,-8.026176,-7.438627,-5.557078,7.069689,7.648761,-3.011043,-7.015299,-4.416724,-0.094137,-4.916002,-9.192980,-0.697780],[-0.420229,-5.896721,6.558111,-8.744411,-9.675881,8.637487,-8.341907,-6.577592,6.260548,-4.581641,5.913320,-7.062716,-8.649264,6.629240,8.579402,-8.306849],[6.450678,6.914072,2.536139,-2.158004,-9.547789,-6.192779,8.621833,0.863022,-2.864715,-6.101339,-1.718507,1.575590,2.481728,5.978660,0.722806,-5.770542],[-9.392498,3.587340,7.569520,1.567195,7.316949,-3.661835,-5.873159,1.274323,-2.858052,-0.541380,-0.362773,7.739017,-5.722923,-4.470886,-3.571475,7.162141],[5.345260,4.194234,-8.175366,-6.118232,-4.948912,-9.675709,-6.846840,0.015073,-1.160617,6.215600,-5.107243,-0.006649,6.997851,-8.030140,-3.692542,-0.735624],[-3.685013,-4.002376,-6.588405,-6.907628,-3.921248,-8.794484,-1.064700,7.537498,0.388600,-7.057390,2.034596,4.991456,8.885197,-9.239385,1.591152,5.535653],[-6.760014,-1.040725,0.502126,-8.249194,-2.755315,-9.693851,-5.345155,9.412196,2.390755,2.150016,-2.755016,8.793843,-0.900626,5.101937,7.668992,2.332880],[1.295723,-8.911503,-3.734281,-1.742761,2.625466,-7.567772,-2.253625,-5.287401,2.195637,-3.664166,-7.415614,4.002538,9.642625,-4.675607,-9.061292,0.019164],[3.557266,-8.443041,-2.661986,-0.615907,0.923124,3.345307,-2.800003,5.217961,-8.120004,-9.438729,-9.982703,9.749151,-6.837532,-0.947415,-4.479678,-2.494489],[1.945781,9.736531,1.498734,-9.272135,-9.479338,-3.458481,9.364558,-4.299250,6.870023,-9.126835,5.482653,-5.216671,5.518854,-5.983724,-4.228260,1.379778],[2.061972,8.891985,8.692408,1.179931,9.374267,-1.246890,-6.317828,-7.494618,6.638581,8.077978,6.650991,4.327879,-3.290462,-4.845055,-2.122080,-0.763748],[-5.597235,5.846463,6.474592,-9.015654,-9.592796,7.748964,9.068776,2.611242,-3.916751,4.989125,-6.524977,-9.336517,-6.170638,2.253202,7.092846,-5.840886],[7.773419,3.173447,2.234895,7.156427,-7.427475,-9.516505,2.145167,9.072113,-6.712964,8.322822,2.852716,0.764877,-5.174357,-0.154931,-5.764741,0.117858]],[[-7.837513,7.972838,-0.901738,-7.821094,2.781520,4.093948,-9.599006,2.804408,3.983976,7.933918,-9.172005,2.650550,7.130014,-0.953937,-5.060710,7.484429],[-3.888263,-9.591950,5.790041,-6.856186,7.572773,6.932963,-5.378664,-3.094018,1.984664,-9.555061,-8.294170,-3.589261,6.207004,-8.378146,9.371295,1.037868],[-7.903760,-1.160312,-2.309588,-8.388583,-4.369324,4.422724,-8.586672,8.767717,9.491996,-7.312185,0.014106,7.902017,5.107017,-5.164112,7.333365,6.657631],[-3.360984,0.771258,-2.831914,-0.153474,-2.116852,2.632566,-2.063657,-7.718376,-7.153109,0.988253,-3.060921,-7.059220,-1.131521,-8.294603,-5.450896,4.241164],[6.980391,4.806169,6.309670,8.578169,7.383054,-9.242396,6.372760,3.192759,3.425043,7.902779,4.983387,-1.124969,-6.471006,6.765759,-6.194682,8.995661],[-8.484934,5.782319,1.516560,6.920792,7.061786,-9.442016,-1.241258,-3.384111,-3.945318,3.833980,7.556200,-6.703215,-3.459636,5.268851,-3.731815,6.926058],[7.744885,-2.820225,6.624955,-7.707007,-1.961176,7.175349,-5.324172,-7.453656,9.057897,5.576432,9.234494,-5.802231,3.554088,-4.279730,0.942164,-1.029325],[-3.499472,9.768745,-5.808039,-1.466954,-9.146879,-1.019251,3.259344,6.091706,-8.551921,-0.553503,-6.211778,-9.897314,-7.349696,-2.922945,-9.893341,-7.391038],[2.351838,-2.802637,5.946961,-7.129050,-9.606230,7.367165,-3.327413,-1.361732,6.600775,-7.573716,9.108273,0.529159,-4.358579,0.648766,4.094348,6.630868],[7.688973,-6.216749,1.693350,-1.947038,5.804174,7.219182,0.653927,9.648838,-5.374556,-9.342665,-0.146969,9.554713,1.344166,5.438429,0.974407,-9.747203],[-9.703184,9.268761,9.660954,5.583488,3.636626,-8.422251,-6.023212,8.336598,-7.411737,-7.732473,-3.577387,4.588374,6.557601,-9.847048,5.920106,4.266479],[5.977486,4.225927,5.363952,-5.262766,-7.391524,5.720571,-5.651959,5.692292,-5.656476,7.045436,-1.488050,0.662443,4.627924,-0.091144,-4.048570,-1.050349],[-4.195366,-1.089772,-1.282828,5.818413,-0.308365,5.778772,1.980695,1.004111,-9.649997,-2.497393,1.789845,-9.401780,3.498433,0.487780,2.161082,-0.111010],[-9.420607,9.578649,4.568542,5.214672,1.837017,-4.648149,4.577982,-7.288866,-6.790749,-8.601973,-2.494029,-0.417872,8.251528,2.645252,2.334636,3.840716],[4.433184,-4.549572,0.653223,-9.706356,-7.912164,6.349364,-6.826236,2.104198,9.980175,-5.752737,1.708355,0.965113,-3.384070,4.133781,-7.688086,3.395746]],[[9.138299,-4.138188,2.802056,7.253845,7.041362,-6.724622,-3.409727,-9.641274,8.008474,-9.280288,5.939283,-3.717729,-3.682957,4.030564,-7.151737,-9.435366],[-3.170349,-7.101208,8.763066,7.641952,-9.334837,-9.219572,-5.423411,-7.243459,1.615090,-1.514296,0.082774,0.114008,-6.586620,-0.303836,7.933513,-8.879015],[-8.284106,-8.012600,-2.468726,-7.413739,3.806298,3.975930,-7.343196,9.669638,-4.037849,-7.513239,-2.292675,-6.910006,6.091730,4.301730,0.749553,-7.349981],[-9.851397,-4.991893,3.447247,-1.411323,9.984731,-8.124961,6.592715,-8.234561,4.740959,6.028180,-5.905227,-5.979936,2.128243,-6.331901,2.383598,-0.115222],[6.309456,-9.499781,0.328032,4.712991,-0.977836,-9.257503,-1.964981,-8.210618,-0.806603,8.788300,7.283016,-9.415396,-0.197950,0.657197,5.381984,2.186544],[-7.067527,5.847297,-8.082461,8.249473,-5.806362,4.761373,-7.578937,-3.403938,0.926289,6.338184,1.242436,2.556324,-5.572392,3.521946,-1.084014,5.451324],[-2.606294,7.076165,7.265859,-0.909757,-0.485668,-0.015556,0.325010,3.544947,4.222027,7.071477,-8.758545,-0.431474,2.051290,6.216937,-5.421326,0.976423],[4.768042,-1.992106,7.547210,3.052621,-6.030405,-2.737729,-6.095617,-2.675930,-8.789334,2.441320,6.057119,7.083634,1.988237,-2.965562,0.556636,6.960501],[-3.560588,-4.746431,-6.508042,-0.860050,6.517957,-6.683739,-9.424537,1.533933,-7.164225,-2.727590,-0.382865,-1.044655,-6.727684,-4.674656,-7.973042,-9.344233],[0.411277,-0.678725,-2.548682,-6.992212,2.282051,-8.343425,4.313024,-3.375758,-0.203111,7.707498,5.131144,-7.114509,0.288237,7.632247,-1.727058,-9.528741],[-7.685653,3.195658,4.195878,5.990155,-1.799388,3.883215,6.556447,8.075257,-2.355341,6.881908,4.417581,8.541752,-9.807485,-0.790742,-0.618241,-0.420884],[-7.876488,-4.443868,3.318243,-7.476308,5.461131,0.254580,-6.876023,-0.855377,-9.703549,-6.411809,0.312353,-6.841766,-9.082946,1.832683,4.631392,-0.777926],[8.625595,-3.572983,-9.853103,7.832580,-2.519175,-8.352067,9.550622,8.258579,-0.595466,7.823970,1.357912,5.835915,6.899858,-7.602893,-5.745693,-8.745695],[9.876190,-7.408121,8.841251,6.313696,9.967622,-6.319138,-2.429919,-5.443725,6.430411,7.878993,8.043039,7.703274,3.051902,0.296223,-4.708139,4.868049],[-1.263582,4.551417,9.871590,6.139330,-8.359452,-7.877884,9.991358,-9.509804,-5.669283,2.205183,-6.742280,-4.431629,2.522842,-6.638236,1.192733,2.291980]]], dtype = "float64")#candidate|6332|(14, 15, 16)|const|float64
bop_6333 = relay.add(var_6331.astype('float64'), relay.reshape(const_6332.astype('float64'), relay.shape_of(var_6331))) # shape=(14, 15, 16)
output = relay.Tuple([bop_6333,])
output2 = relay.Tuple([bop_6333,])
func_6358 = relay.Function([var_6331,], output)
mod['func_6358'] = func_6358
mod = relay.transform.InferType()(mod)
mutated_mod['func_6358'] = func_6358
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6359 = relay.var("var_6359", dtype = "float64", shape = (14, 15, 16))#candidate|6359|(14, 15, 16)|var|float64
func_6358_call = mutated_mod.get_global_var('func_6358')
call_6360 = func_6358_call(var_6359)
output = call_6360
func_6361 = relay.Function([var_6359], output)
mutated_mod['func_6361'] = func_6361
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_6385 = relay.TupleGetItem(func_1433_call(), 0)
call_6386 = relay.TupleGetItem(func_1435_call(), 0)
func_5541_call = mod.get_global_var('func_5541')
func_5543_call = mutated_mod.get_global_var('func_5543')
const_6404 = relay.const([[6,-2,8,-10,-4,-3,-9,-8,-8,3,6,-7,-1,8,-8,10,8,-4,7,-5,6,-4,2,7,-4,-8,-2,-5,10,6,4,2,7,-8,-10,5,-10,9,10,-2,6,3,4,4,1,-2,3,-7,-7,-5,8,1,9,-8,7,1,9,-3,4,-7,-7,-10,-2,-1,1,-6,-5,5,-10,-1,4,-10,8,7,3,6,4,8,-4,7,-4,2,-3,-1,3,-7,6,3,-3,5,-8,-3,9,-10,-2,-8,-1,6,-9,-4,1,-3,-1,10,-7,-7,9,7,1,1,-4,10,9,-9,4,-3,7,3,-2,-1,1,-6,-7,-6,-2,-2,6,-2,-7,-3,6,-10,-4,10,-8,-7,-8,9,5,4,4,4,7,5,8,-6,8,9,9,-7,2,-7,-6,6,2,9,-7,6,-10,7],[-10,4,1,9,-3,-8,-2,-5,-1,-2,-2,-1,-5,-2,-9,-2,-4,-7,10,-6,4,-7,-10,7,-5,6,-9,8,-3,6,9,-1,6,9,-5,8,10,-8,-10,-4,3,4,-9,3,-3,4,-10,-7,2,-4,-1,-8,10,3,-10,-6,-9,4,-5,9,-7,1,7,-6,4,-8,4,7,-2,5,1,5,-6,-9,-6,-2,-3,-4,3,-9,-2,3,3,-2,-4,6,-10,5,-2,8,3,4,-5,6,8,4,-4,-8,10,-1,6,-10,-10,2,-9,9,2,-10,10,4,3,2,6,-4,7,-3,-3,-9,7,-5,4,2,5,-5,-2,-7,-7,-4,-6,-1,4,-5,-6,9,8,2,8,-1,10,2,-5,6,-7,-4,9,-7,9,9,8,9,-4,9,-8,6,6,-9,6,-10,-6,-7]], dtype = "uint8")#candidate|6404|(2, 160)|const|uint8
call_6403 = relay.TupleGetItem(func_5541_call(relay.reshape(const_6404.astype('uint8'), [320, 1])), 3)
call_6405 = relay.TupleGetItem(func_5543_call(relay.reshape(const_6404.astype('uint8'), [320, 1])), 3)
output = relay.Tuple([call_6385,call_6403,const_6404,])
output2 = relay.Tuple([call_6386,call_6405,const_6404,])
func_6411 = relay.Function([], output)
mod['func_6411'] = func_6411
mod = relay.transform.InferType()(mod)
output = func_6411()
func_6412 = relay.Function([], output)
mutated_mod['func_6412'] = func_6412
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6422 = relay.var("var_6422", dtype = "float32", shape = (1, 16, 4))#candidate|6422|(1, 16, 4)|var|float32
uop_6423 = relay.asin(var_6422.astype('float32')) # shape=(1, 16, 4)
func_2239_call = mod.get_global_var('func_2239')
func_2241_call = mutated_mod.get_global_var('func_2241')
call_6430 = func_2239_call()
call_6431 = func_2239_call()
output = relay.Tuple([uop_6423,call_6430,])
output2 = relay.Tuple([uop_6423,call_6431,])
func_6439 = relay.Function([var_6422,], output)
mod['func_6439'] = func_6439
mod = relay.transform.InferType()(mod)
var_6440 = relay.var("var_6440", dtype = "float32", shape = (1, 16, 4))#candidate|6440|(1, 16, 4)|var|float32
output = func_6439(var_6440)
func_6441 = relay.Function([var_6440], output)
mutated_mod['func_6441'] = func_6441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_6445 = relay.TupleGetItem(func_3833_call(), 0)
call_6446 = relay.TupleGetItem(func_3835_call(), 0)
output = call_6445
output2 = call_6446
func_6460 = relay.Function([], output)
mod['func_6460'] = func_6460
mod = relay.transform.InferType()(mod)
output = func_6460()
func_6461 = relay.Function([], output)
mutated_mod['func_6461'] = func_6461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3289_call = mod.get_global_var('func_3289')
func_3290_call = mutated_mod.get_global_var('func_3290')
call_6474 = relay.TupleGetItem(func_3289_call(), 0)
call_6475 = relay.TupleGetItem(func_3290_call(), 0)
func_5164_call = mod.get_global_var('func_5164')
func_5169_call = mutated_mod.get_global_var('func_5169')
const_6493 = relay.const([[4,-9,1,2,2,-6,2,-7,7,9,-2,-9,2,-5,1,-4,-3,6,6,-7,10,9,3,6,-1,-9,3,-1,-3,-7,-8,-9,-3,2,-5,-10,-4,8,4,-9,-8,-9,-10,3,9,-6,-10,-7,-2,-4,1,1,-2,3,2,10,4,-8,-10,-8,2,7,10,4,-4,-6,-10,-10,-5,-8,-9,-4,10,7,-6,10,-8,-7,2,10,-10,2,-3,-2,-5,5,1,-7,5,10,9,-7,-8,5,6,5,-2,-5,9,-3,-10,-10,-2,-1,-1,6,2,6,8,9,5,-9,10,1,-3,-6,7,-5,3,3,8,5,-5,-9,2,-8,-1,5,-2,3,-5,8,6,-10,-1,4,-4,-1,-10,3,-10,1,7,5,4,-5,-8,8,8,3,-3,-1,8,6,-4,-1,10,-8,-8,4,-2,1,-4,5,9,1,9,-8,6,4,-3,-6,7,-9,8,8,-4,3,-10,-10,-8,-2,5,-3,-4,-2,-2,-1,6,-3,-5,4,2,9,-8,4,10,-5,3,-5,-5,-5,9,3,6,-8,8,4,3,-5,-10,7,2,2,-9,4,8,-10,-3,-10,2,-4,4,-2,1,6,-6,-1,4,-6,2,9,-7,-5,-4,1,-5,-6,-3,3,-8,5,-1,-2,10,2,-8,-2,-1,-7,-5,3,-3,8,9,-2,-10,9,-3,-10,1,-5,-4,5,-7,2,-1,2,4,-4,1,8,-2,5,-9,6,-9,-10,9,8,-8,-8,5,-4,9,-10,3,2,-6,-9,-5,7,-8,-7,-4,5,-7,-2,-2,-9,-4,1,-6,3,1,-7,6,10,-2,-1,4,-10,-8,3,-1,-2,1,4,-6,9,8,-4,3,8,-1,-4,6,5,-8,-5,1,6,1,-9,-9,-4,6,3,2,-7,-2,-7,6,-4,2,-5,-7,3,3,4,-2,-10,6,10,-5,-10,-7,-7,1,-7,-1,6,-3,5,-2,-7,9,5,-1,3,9,2,2,-8,9,6,6,-7,2,5,2,8,-9,9,7,5,7,3,7,2,7,-7,9,-1,9,-5,-10,-4,-8,-9,5,3,3,9,7,7,9,-6,1,9,5,-1,-7,-4,-6,-9,8,10,10,-1,-3,1,-6,10,8,5,3,8,9,-6,4,-5,-9,-4,-8,-6,-7,1,-7,9,10,9,-10,-5,9,-5,9,7,-6,-9,-8,-5,3,6,-9,-5,9,-4,1,9,3,2,3,-1,10,5,-4,-1,-6,-9,4,-4,10,-3,9,2,5,5,-3,8,6,-1,2,9,1,-5,-6,7,8,8,1,1,-3,-5,-1,-8,-6,7,-1,8,-8,4,-1,-9,-10,-8,8,6,-6,-6,3,3,-4,-7,-1,-8,7,1,4,1,-9,-4,8,8,2,10,9,7,6,-8,-1,5,8,-8,-6,-6,-7,3,2,-9,5,-4,-5,-8,4,-7,2,-3,-8,5,-1,2,-3,5,-4,4,6,-4,6,3,7,5,1,-4,-2,-4,1,-2,1,-4,4,6,5,-10,-1,-2,-2,-8,8,6,10,-2,-8,-9,-4,5,2,-7,-1,-9,1,-9,-10,-9,-8,8,-5,-10,7,-1,2,-8,-5,-1,-3,9,4,8,-6,2,-2,-3,-3,7,4,-8,3,-3,10,-5,6,8,3,-4,2,4,-8,-10,-1,10,6,6,-3,-8,-4,-7,-8,-10,2,-1,-2,8,-3,1,-7,3,-9,1,-7,7,1,-4,1,-1,10,7,6,-3,6,-4,5,4,-6,7,3,7,-10,-2,-4,5,-4,7,-2,2,-2,-8,-4,10,9,-3,1,-4,-10,-5,-1,10,5,-9,8,2,8,7,-4,3,-6,6,8,-10,8,5,-6,-7,4,7,-7,-2,-10,-6,7,10,6,3,-5,4,-10,5,6,6,-9,-2,1,1,2,-6,9,-4,-1,10,-4,1,3,-8,9,-1,-7,5,6,9,-7,8,-2,-10,-1,-9,7,9,-8,-1,2,-7,4,9,10,-9,-5,-3,-9,-10,-5,7,10,2,-2,-7,6,5,6,1,2,-2,-6,3,-8,-8,-1,5,-1,-9,1,-9,-10,6,-8,3,-6,8,2,7,-4,2,-2,-7,5,5,-2,10,9,-9,4,1,-10,4,-10,-1,8,10,-2,2,-2,3,3,9,9,3,1,5,-2,-3,-2,9,-2,9,-5,-1,-9,-5,8,-6,-2,-2,10,-6,8,7,6,9,4,-1,-8,7,9,-10,6,7,5,-2,-9,-9,8,9,9,-3,6,1,-10,-3,-2,7,-9,5,4,-8,4,1,3,-9,8,5,-5,1,-7,-4,7,7,8,1,9,-6,-9,8,-9,-4,6,4,-8,-9,-9,-5,8,4,6,-7,-7,10,2,-9,5,-9,-5,-4,-5,-7,8,1,-6,2,-2,-6,2,8,4,-4,-3,9,5,10,-8,6,-8,4,4,5,2,7,-7,-7,-2,-7,-3,2,10,8,8,-6,3,-2,5,-2,-9,1,4,5,1,3,-10,2,7,-10,5,3,5,2,-5,6,-5,-1,7,9,10,1,-8,-10,2,2,-5,3,2,-9,-2,-2,2,-8,-1,-8,-8,1,-10,1,-8,-1,-9,2,-4,10,-5,-4,8,-7,-8,10,-4,2,-1,-7,-5,3,-5,-7,7,4,2,3,10,10,7,-4,2,-4,-8,-3,3,6,2,-6,3,-3,10,6,7,7,-10,4,6,5,3,6,-6,4,6,-9,2,3,-9,1,6,2,9,-8,-4,-7,-2,2,5,-8,-8,1,2,-3,6,-8,3,10,4,7,2,-6,8,4,4,8,2,1,7,4,-9,8,2,4,-6,5,-8,2,-7,-1,2,-2,-3,8,-6,-3,-5,-4,9,-3,10,2,-9,6,-5,-6,8,-1,10,1,10,-10,7,1,4,10,4,-4,8,-6,6,-8,-1,-7,8,6,4,-2,1,-8,9,-1,-1,3,-4,10,4,-4,9,-3,-9,-5,-6,7,-2,4,-4,4,9,-5,-8,-5,-5,7,-10,2,-1,6,4,7,-8,-9,6,-8,-1,-10,-7,3,-3,7,1,7,-6,3,8,-8,-9,-1,-2,-1,-9,4,-7,-10,-7,8,-6,-2,-9,4,5,6,-1,-10,-5,6,6,-1,-6,5,-8,3,-9,-8,-10,-8,6,-10,10,-2,4,8,-9,-3,10,8,1,3,6,8,4,4,7,-9,-5,1,-10,-7,10,1,6,-7,3,-6,-3,-9,-8,9,5,4,8,9,-6,6,-6,5,8,-10,-4,-2,-9,-4,-1,6,-8,8,-8,5,-3,10,-7,3,7,-8,10,-7,-2,7,1,-3,-4,6,-8,-5,-3,-2,2,-8,9,-1,10,7,7,5,-7,-9,-9,-2,8,-10,6,3,-7,6,-9,-4,-5,8,5,1,4,-5,-7,-2,6,-7,-5,-10,-1,10,-5,6,-5,5,-2,4,-8,-10,5,1,-5,-6,9,3,-6,8,7,-3,-10,2,5,-7,4,8,-9,-3,-7,5,6,-6,2,4,-9,4,5,1,-4,3,-6,-7,9,-9,8,-10,3,7,-9,-7,-9,-10,-8,8,-1,-10,-1,-4,-7,-5,-1,9,3,9,10,2,6,-6,3,6,5,5,-3,6,-3,4,8,-8,-3,2,-3,-3,-6,-3,2,-5,5,3,-8,-7,10,7,-7,8,1,3,6,-5,2,-1,9,-1,7,-2,3,-8,-3,2,9,9,-1,6,-8,-10,-8,7,1,2,2,-3,-5,7,-9,7,-8,-9,-1,-6,5,9,9,3,-4,7,8,10,-2,-1,-3,-8,5,9,4,2,3,5,1,-1,-2,2,8,-5,-6,-3,3,1,-1,-3,-8,-6,-10,5,8,6,-4,-2,-10,-7,3,7,-3,5,9,-9,-5,-9,6,6,-10,6,3,-8,-4,9,-5,5,-3,2,-10,-10,-7,-10,3,-9,-2,-6,-10,10,-1,3,-5,6,9,-1,-2,-4,10,-4,-3,5,-5,-10,7,-10,9,8,2,-6,-5,-1,-10,6,10,2,-2,-9,-9,-3,-1,7,-8,7,-3,2,10,7,-8,-9,-4,4,-9,2,-3,4,-9,7,-10,-9,5,-2,-3,-4,-1,-1,-5,10,7,-2,8,8,1,-7,10,-3,-5,2,4,-1,1,10,7,2,2,6,-1,7,10,4,-2,-6,4,7,6,-2,9,4,2,2,9,-3,-2,4,-6,1,5,-7,7,-6,-1,9,2,8,9,-5,-7,3,-1,-1,-7,-5,2,-3,5,2,-8,7,-6,4,-4,8,-9,1,9,-7,4,9,3,5,-1,-5,9,1,-7,-5,-3,-4,-5,2,-7,-10,-10,-9,3,10,-2,-5,7,8,-10,-6,-5,7,7,4,8,-5,5,9,9,-1,6,-1,1,-6,-2,8,-5,9,-4,-6,-7,1,6,-9,1,3,6,-8,-3,10,9,7,4,-3,-9,1,9,-9,3,-9,9,-2,6,-4,6,-6,-3,-6,9,5,10,7,9,-4,7,7,-5,-1,-8,-4,8,-9,5,5,-7,-5,6,6,-9,8,-6,-1,3,-6,4,5,-9,4,10,-7,2,3,3,5,-4,9,-7,2,10,-1,7,-10,-2,10,4,10,1,-5,-5,-8,3,-8,6,2,-10,-2,-1,-1,7,-5,-1,8,-10,-4,-1,-3,-10,5,-5,-1,10,-9,-8,-3,4,-7,-3,-4,-5,-8,-3,-3,6,-8,-6,5,6,8,6,10,-9,4,-9,-7,-9,3,9,-6,5,-5,6,-7,-4,6,-8,10,1,-1,2,-9,4,4,9,8,5,4,-3,-4,8,5,-6,3,-8,-2,-4,-3,2,-4,9,-4,5,-6,9,-5,9,10,6,-3,-10,7,5,-4,9,-7,-10,-3,-6,-7,-8,-1,4,-2,-7,-9,9,2,-7,-10,-4,5,5,3,8,8,2,-2,-3,1,9,-8,7,2,-6,-10,-7,-6,-6,6,9,-1,5,1,8,-9,-1,7,9,-2,2,-7,1,-3,-4,-1,5,8,-5,-8,-1,2,-8,-2,10,3,-7,3,6,5,7,7,-9,-1,-1,9,-8,4,2,2,-1,4,-5,-8,-2,-3,10,-8,4,-3]], dtype = "int64")#candidate|6493|(1, 1920)|const|int64
var_6494 = relay.var("var_6494", dtype = "uint64", shape = (3136,))#candidate|6494|(3136,)|var|uint64
call_6492 = relay.TupleGetItem(func_5164_call(relay.reshape(const_6493.astype('int64'), [10, 12, 16]), relay.reshape(call_6474.astype('float32'), [288,]), relay.reshape(var_6494.astype('uint64'), [3136,]), ), 4)
call_6495 = relay.TupleGetItem(func_5169_call(relay.reshape(const_6493.astype('int64'), [10, 12, 16]), relay.reshape(call_6474.astype('float32'), [288,]), relay.reshape(var_6494.astype('uint64'), [3136,]), ), 4)
func_3803_call = mod.get_global_var('func_3803')
func_3804_call = mutated_mod.get_global_var('func_3804')
call_6509 = relay.TupleGetItem(func_3803_call(), 0)
call_6510 = relay.TupleGetItem(func_3804_call(), 0)
output = relay.Tuple([call_6474,call_6492,const_6493,var_6494,call_6509,])
output2 = relay.Tuple([call_6475,call_6495,const_6493,var_6494,call_6510,])
func_6518 = relay.Function([var_6494,], output)
mod['func_6518'] = func_6518
mod = relay.transform.InferType()(mod)
mutated_mod['func_6518'] = func_6518
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6519 = relay.var("var_6519", dtype = "uint64", shape = (3136,))#candidate|6519|(3136,)|var|uint64
func_6518_call = mutated_mod.get_global_var('func_6518')
call_6520 = func_6518_call(var_6519)
output = call_6520
func_6521 = relay.Function([var_6519], output)
mutated_mod['func_6521'] = func_6521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6523 = relay.TupleGetItem(func_5615_call(), 0)
call_6524 = relay.TupleGetItem(func_5617_call(), 0)
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_6529 = relay.TupleGetItem(func_2927_call(), 4)
call_6530 = relay.TupleGetItem(func_2929_call(), 4)
var_6537 = relay.var("var_6537", dtype = "float64", shape = (2, 16, 9))#candidate|6537|(2, 16, 9)|var|float64
bop_6538 = relay.bitwise_or(call_6529.astype('uint8'), relay.reshape(var_6537.astype('uint8'), relay.shape_of(call_6529))) # shape=(2, 16, 9)
bop_6541 = relay.bitwise_or(call_6530.astype('uint8'), relay.reshape(var_6537.astype('uint8'), relay.shape_of(call_6530))) # shape=(2, 16, 9)
func_2825_call = mod.get_global_var('func_2825')
func_2827_call = mutated_mod.get_global_var('func_2827')
call_6542 = relay.TupleGetItem(func_2825_call(), 0)
call_6543 = relay.TupleGetItem(func_2827_call(), 0)
output = relay.Tuple([call_6523,bop_6538,call_6542,])
output2 = relay.Tuple([call_6524,bop_6541,call_6543,])
func_6544 = relay.Function([var_6537,], output)
mod['func_6544'] = func_6544
mod = relay.transform.InferType()(mod)
var_6545 = relay.var("var_6545", dtype = "float64", shape = (2, 16, 9))#candidate|6545|(2, 16, 9)|var|float64
output = func_6544(var_6545)
func_6546 = relay.Function([var_6545], output)
mutated_mod['func_6546'] = func_6546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_580_call = mod.get_global_var('func_580')
func_581_call = mutated_mod.get_global_var('func_581')
call_6562 = relay.TupleGetItem(func_580_call(), 0)
call_6563 = relay.TupleGetItem(func_581_call(), 0)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_6568 = relay.TupleGetItem(func_1053_call(), 2)
call_6569 = relay.TupleGetItem(func_1054_call(), 2)
output = relay.Tuple([call_6562,call_6568,])
output2 = relay.Tuple([call_6563,call_6569,])
func_6591 = relay.Function([], output)
mod['func_6591'] = func_6591
mod = relay.transform.InferType()(mod)
mutated_mod['func_6591'] = func_6591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6591_call = mutated_mod.get_global_var('func_6591')
call_6592 = func_6591_call()
output = call_6592
func_6593 = relay.Function([], output)
mutated_mod['func_6593'] = func_6593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_6596 = relay.TupleGetItem(func_653_call(), 0)
call_6597 = relay.TupleGetItem(func_654_call(), 0)
output = call_6596
output2 = call_6597
func_6602 = relay.Function([], output)
mod['func_6602'] = func_6602
mod = relay.transform.InferType()(mod)
mutated_mod['func_6602'] = func_6602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6602_call = mutated_mod.get_global_var('func_6602')
call_6603 = func_6602_call()
output = call_6603
func_6604 = relay.Function([], output)
mutated_mod['func_6604'] = func_6604
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6682 = relay.const([[[1,1,-10,6,-2,6,9],[5,10,5,-1,8,6,-4],[-5,3,2,2,2,9,10],[-7,1,-9,7,-2,8,6],[2,-6,-6,-4,4,10,6],[7,5,5,7,-8,7,-7],[-10,2,4,10,9,-8,-10],[7,8,-1,10,-8,7,5],[7,-2,4,2,4,-10,6],[5,8,1,8,8,6,-4],[5,-1,-1,1,7,-5,-3],[-3,5,-6,-10,1,-9,-5],[-7,1,8,4,3,7,7],[2,-9,3,-2,8,-6,-1]],[[8,-3,5,-6,-4,-6,-6],[-8,7,6,-4,1,-8,8],[-8,10,-5,10,4,6,-8],[6,5,10,-3,-9,5,-1],[-9,-8,9,2,10,-7,9],[2,-4,-3,2,3,10,-10],[-10,-10,3,-5,-6,10,8],[-8,-1,-4,1,-5,9,-8],[-8,3,-3,-8,-1,-1,-7],[-10,-8,-1,3,3,-1,8],[-6,8,-7,3,-6,-6,-1],[5,-8,4,5,3,9,3],[6,-9,-8,-6,1,-4,-8],[5,7,-1,5,1,9,2]],[[-1,7,6,10,4,-2,-5],[4,-9,7,9,1,1,5],[-7,9,2,7,-1,-6,5],[2,4,-5,4,-9,10,-6],[3,3,8,1,-6,-10,7],[6,1,4,-5,-8,-3,-2],[6,-5,1,2,8,9,-4],[-4,2,7,-9,9,-9,3],[-4,6,4,3,-7,-5,10],[2,-5,-9,8,2,-6,-3],[10,9,-2,-5,6,4,-5],[-10,-4,-1,3,-8,7,-10],[1,-7,9,6,-1,-8,9],[2,-10,10,-7,5,-2,-10]],[[-10,-1,-2,-3,-4,-2,2],[-4,3,-6,10,-9,7,-6],[-4,10,-9,-9,9,3,3],[-10,7,-5,-2,3,6,-9],[-3,-4,3,5,4,4,7],[7,-3,6,-5,-10,3,8],[-5,-4,4,-9,3,1,-9],[-1,10,-8,-8,-5,-7,-9],[10,10,4,6,-4,-5,1],[4,-10,-6,-6,-5,1,7],[-7,-8,2,2,4,6,-5],[2,-8,3,3,8,6,-2],[-3,6,-5,-7,-4,5,-9],[7,3,-9,8,-6,-3,-10]],[[8,-7,1,1,10,5,8],[-4,-2,-2,-10,3,-5,9],[-3,-9,1,2,-1,-9,2],[5,-3,-9,-1,9,2,-9],[9,6,-7,5,-3,1,1],[-3,4,-4,-10,-4,-4,2],[3,2,1,5,3,5,6],[-9,4,9,3,-6,6,4],[3,5,-7,-9,5,6,4],[7,5,-9,10,-10,-3,6],[6,-9,-3,-6,-1,1,-9],[-7,6,6,-10,4,-5,2],[1,-9,-7,-8,3,3,9],[4,-10,-2,7,-2,1,8]],[[10,-5,-10,-2,1,9,3],[1,-7,9,-8,-6,7,1],[-3,5,10,6,4,-1,7],[-10,4,-4,6,10,6,-8],[-3,-2,-1,2,1,-3,6],[-10,6,7,3,2,-7,-5],[2,8,4,4,1,7,1],[-6,6,2,-8,-1,-2,-2],[9,4,3,-7,-5,2,-4],[-7,1,-4,9,-8,-6,-2],[1,-9,-3,2,-6,3,-9],[-7,-4,-9,-8,-3,-10,-6],[9,7,1,-2,9,-10,-2],[-6,10,3,-8,10,-5,2]],[[3,4,-5,-1,6,-3,-5],[10,8,8,9,-3,-2,-10],[-5,4,2,9,8,-4,-3],[-9,-1,-8,5,8,-5,-1],[-3,8,3,7,10,3,-6],[-4,5,7,-2,-7,-9,1],[4,-5,-2,5,4,3,8],[4,4,-2,1,4,-4,-10],[-6,1,2,-6,-8,2,-5],[-6,10,6,9,-2,7,6],[7,-6,-9,-4,10,7,-3],[10,3,-8,7,4,1,-8],[2,-10,2,-3,-1,-1,-8],[-1,-7,-6,6,-3,9,-10]],[[-3,-9,-2,7,4,-4,8],[-8,-6,-7,7,-3,-9,-7],[-6,-1,5,6,-8,1,5],[-7,-3,-9,-1,1,-10,-4],[-3,-7,7,-7,-9,-10,-6],[-9,6,-3,-10,-7,-7,-10],[3,5,-4,-4,-2,3,-2],[6,-6,8,-10,1,1,10],[6,-4,3,-6,2,8,-9],[-3,6,10,6,-3,8,8],[-4,7,8,1,-3,-10,7],[8,1,-8,5,-8,-5,-9],[7,-2,8,2,-3,9,2],[-10,9,6,1,6,1,9]],[[7,8,-7,-4,10,-3,9],[-8,3,-1,-5,-2,-2,-4],[-6,-8,1,4,6,3,4],[-8,9,-5,5,-7,-2,9],[-9,6,4,-6,-3,2,-10],[7,4,8,-3,-8,-8,9],[1,-5,-8,8,8,6,-6],[-1,7,2,-3,-5,-5,3],[7,5,-7,-10,3,7,-2],[1,3,-8,-7,-4,-3,5],[3,3,-1,7,1,2,-7],[-3,4,-9,-5,-1,-7,3],[5,10,-7,7,-3,5,-4],[-6,-8,10,-5,10,5,-2]],[[-6,4,4,-9,-7,10,-3],[-4,4,7,-10,-5,-5,-3],[-6,-3,-2,4,-1,9,-1],[9,-4,8,2,-3,2,5],[2,-6,-5,-3,-3,2,-9],[-1,-8,2,-3,3,8,8],[-1,-5,-5,3,9,-6,2],[8,7,-2,2,-10,-8,2],[8,-6,-5,3,-4,-9,-2],[-7,10,-6,7,-3,-5,5],[5,-9,-9,1,-6,3,1],[-2,6,-9,-7,7,-6,2],[-5,-5,4,3,-9,-7,-9],[6,4,-6,9,1,2,-9]],[[-10,8,-10,6,-6,-9,-3],[1,-9,-5,7,5,7,-2],[-6,5,-4,1,-7,1,-6],[-8,7,3,8,-10,9,9],[-3,-5,3,-5,5,4,3],[-5,4,-9,7,-8,10,-8],[-5,-5,9,9,9,3,-2],[-8,-2,5,10,-8,4,10],[4,-2,-6,-7,-4,8,-10],[9,-8,8,-4,6,5,-1],[-2,4,10,4,1,-10,8],[10,9,-2,10,6,1,8],[-10,6,9,-7,-5,4,2],[5,-3,8,6,-10,-7,10]],[[10,5,-4,-1,2,1,-9],[-7,10,1,-7,-5,8,-1],[2,7,1,4,-5,-10,3],[6,8,-4,-5,2,-3,-7],[10,10,-9,-4,6,-6,4],[-10,7,10,-9,-4,7,-6],[-2,-3,-1,4,7,2,7],[8,4,-8,-4,-8,3,9],[9,2,10,-4,10,3,-8],[-5,-3,-6,-9,-9,3,7],[-3,-7,4,4,7,-5,7],[-6,-10,-10,2,-1,-10,-5],[10,-8,8,5,-5,4,-8],[8,-6,8,5,-1,4,9]],[[2,7,-6,5,10,-4,9],[-6,-8,2,-1,3,10,3],[6,8,-6,10,-9,3,-6],[-4,-8,4,7,1,-8,-3],[6,4,10,2,6,7,10],[5,-1,-1,-9,5,10,-3],[-10,-7,-6,10,3,-3,5],[-6,-2,-1,10,-1,6,5],[2,4,-8,-10,-4,-10,2],[9,3,-4,-6,7,-6,5],[6,8,9,2,7,-2,2],[-9,5,-4,3,3,-5,-5],[3,-5,-9,-9,-6,-6,4],[-3,7,-1,-10,-1,6,-4]]], dtype = "uint32")#candidate|6682|(13, 14, 7)|const|uint32
var_6683 = relay.var("var_6683", dtype = "uint32", shape = (13, 14, 7))#candidate|6683|(13, 14, 7)|var|uint32
bop_6684 = relay.logical_xor(const_6682.astype('uint32'), relay.reshape(var_6683.astype('uint32'), relay.shape_of(const_6682))) # shape=(13, 14, 7)
output = bop_6684
output2 = bop_6684
func_6703 = relay.Function([var_6683,], output)
mod['func_6703'] = func_6703
mod = relay.transform.InferType()(mod)
var_6704 = relay.var("var_6704", dtype = "uint32", shape = (13, 14, 7))#candidate|6704|(13, 14, 7)|var|uint32
output = func_6703(var_6704)
func_6705 = relay.Function([var_6704], output)
mutated_mod['func_6705'] = func_6705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1380_call = mod.get_global_var('func_1380')
func_1382_call = mutated_mod.get_global_var('func_1382')
call_6723 = relay.TupleGetItem(func_1380_call(), 0)
call_6724 = relay.TupleGetItem(func_1382_call(), 0)
func_4062_call = mod.get_global_var('func_4062')
func_4064_call = mutated_mod.get_global_var('func_4064')
call_6732 = relay.TupleGetItem(func_4062_call(), 0)
call_6733 = relay.TupleGetItem(func_4064_call(), 0)
output = relay.Tuple([call_6723,call_6732,])
output2 = relay.Tuple([call_6724,call_6733,])
func_6741 = relay.Function([], output)
mod['func_6741'] = func_6741
mod = relay.transform.InferType()(mod)
output = func_6741()
func_6742 = relay.Function([], output)
mutated_mod['func_6742'] = func_6742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5258_call = mod.get_global_var('func_5258')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_6756 = relay.TupleGetItem(func_5258_call(), 0)
call_6757 = relay.TupleGetItem(func_5260_call(), 0)
output = relay.Tuple([call_6756,])
output2 = relay.Tuple([call_6757,])
func_6763 = relay.Function([], output)
mod['func_6763'] = func_6763
mod = relay.transform.InferType()(mod)
output = func_6763()
func_6764 = relay.Function([], output)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4343_call = mod.get_global_var('func_4343')
func_4345_call = mutated_mod.get_global_var('func_4345')
call_6771 = relay.TupleGetItem(func_4343_call(), 1)
call_6772 = relay.TupleGetItem(func_4345_call(), 1)
output = call_6771
output2 = call_6772
func_6773 = relay.Function([], output)
mod['func_6773'] = func_6773
mod = relay.transform.InferType()(mod)
output = func_6773()
func_6774 = relay.Function([], output)
mutated_mod['func_6774'] = func_6774
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6460_call = mod.get_global_var('func_6460')
func_6461_call = mutated_mod.get_global_var('func_6461')
call_6804 = func_6460_call()
call_6805 = func_6460_call()
output = call_6804
output2 = call_6805
func_6808 = relay.Function([], output)
mod['func_6808'] = func_6808
mod = relay.transform.InferType()(mod)
mutated_mod['func_6808'] = func_6808
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6808_call = mutated_mod.get_global_var('func_6808')
call_6809 = func_6808_call()
output = call_6809
func_6810 = relay.Function([], output)
mutated_mod['func_6810'] = func_6810
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_6831 = relay.TupleGetItem(func_3004_call(), 0)
call_6832 = relay.TupleGetItem(func_3006_call(), 0)
func_5187_call = mod.get_global_var('func_5187')
func_5189_call = mutated_mod.get_global_var('func_5189')
call_6843 = func_5187_call()
call_6844 = func_5187_call()
output = relay.Tuple([call_6831,call_6843,])
output2 = relay.Tuple([call_6832,call_6844,])
func_6849 = relay.Function([], output)
mod['func_6849'] = func_6849
mod = relay.transform.InferType()(mod)
mutated_mod['func_6849'] = func_6849
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6849_call = mutated_mod.get_global_var('func_6849')
call_6850 = func_6849_call()
output = call_6850
func_6851 = relay.Function([], output)
mutated_mod['func_6851'] = func_6851
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6882 = relay.const([[[5.455591,9.009337,-8.209016,6.467097,-4.283087,4.827577,-2.838453,-6.132462,0.599439,6.709886,3.505392,-9.730346,-0.591763,-4.873352,9.515211],[4.991978,-3.438327,5.794870,7.995364,-6.988280,1.366134,-0.329898,1.597769,-8.386000,7.182834,0.703803,2.145116,7.228444,-4.933880,3.247674],[2.461140,5.421671,6.893204,-4.885716,9.677848,2.765244,-2.130876,-3.808494,-3.523271,-9.638893,5.489225,-6.634238,-7.201621,-1.860310,8.598561],[-4.920013,-5.481816,-2.100072,-7.063008,-2.018978,5.690005,-2.881516,8.569974,2.524470,8.726946,7.264301,-6.204064,3.422971,6.569999,3.884181]],[[6.221748,-6.799592,6.369846,-6.760423,7.466004,6.483159,-5.866755,7.876143,4.262885,7.794571,-8.353013,4.979553,-4.019028,8.141954,-5.253863],[-8.947678,-3.542092,7.027912,9.296672,-3.900234,-4.686106,0.975099,7.830016,-9.930586,-8.746286,-9.941845,0.609890,6.430365,-4.776195,5.281396],[7.395800,2.958945,-1.059342,-8.184908,-5.850056,3.594619,-8.076972,2.638425,1.361025,-6.240450,8.072492,-9.764904,-6.678203,-3.983346,1.770505],[0.505213,7.839719,-1.591186,6.913638,6.047088,4.645698,-9.423369,8.651301,-7.963521,-4.085113,-8.399000,4.445040,-7.310555,-7.375020,-6.684864]],[[-2.508630,2.341956,-9.087021,-4.190230,-8.845444,8.275245,-0.076166,4.109605,1.147862,-5.864625,4.196036,5.304427,0.237467,-5.662552,-6.442742],[9.012000,2.292176,-9.304507,5.592690,7.059399,-8.112703,3.275993,9.811120,6.506520,-4.223942,-0.231084,-3.932987,-1.798520,7.259772,-4.730864],[-9.741707,-2.237525,-6.865056,1.668287,9.542425,5.483154,-8.077092,-1.435050,6.533841,-2.930873,3.993643,6.549446,5.973041,-2.972135,7.976094],[-1.227147,-1.396812,9.981286,-3.021208,-2.494753,8.148414,2.841269,6.447781,0.281092,6.703770,-5.587874,-5.106048,7.558596,-8.228658,-6.082930]],[[-0.208553,1.748083,-4.680924,1.866687,5.464858,-9.796676,4.513695,-4.789310,-9.480853,6.149226,-4.046216,-6.718094,-9.100559,-5.257557,0.979912],[-9.765060,6.981783,6.757638,-7.338961,-3.334884,-8.446390,-6.328759,4.893269,-9.652969,1.755936,2.928530,-4.867987,-7.082772,2.142265,9.519883],[-1.133512,-4.993855,6.852977,1.029911,-0.893780,4.441714,-6.198443,-1.688219,1.290902,9.871665,3.520754,-0.524463,4.995777,-4.138982,0.858870],[6.958206,8.124702,9.431881,5.209752,-6.316258,7.629057,7.783983,2.260386,7.431950,-6.806134,0.876292,1.829113,0.548390,1.939111,-2.633574]],[[6.707852,-8.903956,4.427381,6.087450,-1.462351,1.757304,-6.497767,2.174982,-7.562653,-1.750087,-9.349999,-2.868903,8.528109,-8.960727,3.593497],[5.603784,-3.186998,8.093124,6.614970,8.613811,-6.676041,0.938987,5.059467,3.441116,2.114457,-6.526417,4.564577,-0.476446,7.256467,6.099574],[7.925082,4.990432,-2.615008,7.019277,-0.954127,3.875074,2.252233,8.882453,-1.011596,7.303906,-9.273324,3.305241,-7.779133,-2.315421,-5.045044],[5.943343,-8.655966,9.954905,1.368193,-4.324405,8.448815,2.472207,0.884726,4.031293,7.662570,8.130044,0.686910,9.063882,-0.446714,8.023976]],[[-5.725700,-6.024098,0.799176,2.198343,4.663848,-6.435756,-0.594055,0.702686,-0.610911,8.620335,8.713301,4.885226,8.668249,1.081346,-9.376019],[-4.251567,9.649984,3.495690,-5.122928,4.952994,6.783183,9.207191,0.292963,3.937145,0.868350,6.908536,1.847238,5.355538,-1.718122,0.129043],[5.240181,6.727706,-3.887589,-8.494805,6.632790,-2.628711,9.066432,-6.982741,2.978432,1.593931,-6.325190,4.477204,0.787400,-9.485976,3.611772],[4.549247,3.246687,3.009220,2.919529,2.217396,-0.810343,0.992895,1.937283,-0.927128,8.960077,9.288990,7.855935,-1.369025,-7.672721,-2.982543]],[[-0.988470,-4.627224,-2.820494,1.545396,2.886432,-9.218381,5.885261,-5.681463,-5.511982,1.298440,-7.874627,9.213252,9.567287,-5.226310,0.222754],[-6.349289,-0.023157,0.082875,-0.158104,2.796640,8.812745,2.331957,6.940573,3.189076,5.426008,-7.007735,-8.700279,0.253545,5.035312,0.156635],[-5.422045,-5.760078,-2.762467,2.749619,-2.449477,2.357261,-3.738649,-4.309085,-1.604647,4.386734,-9.044250,6.387571,-5.920898,0.194878,-2.289646],[-3.706588,-5.951195,-1.730312,-1.741587,8.697238,-5.617562,2.869321,-6.699553,-1.250217,5.044828,-1.941308,9.340338,-9.708601,-5.328890,3.767941]],[[-9.430630,2.439977,-1.213336,-9.021395,7.934906,-3.458513,-3.006722,-1.762179,0.519078,2.064337,8.963532,6.963491,4.365097,-4.858270,2.171442],[-5.200341,4.165593,-1.495446,7.167377,-5.907451,-7.130248,-1.663470,-0.883010,1.382956,-1.421634,9.407225,-9.549382,-9.349803,-5.082216,6.775394],[4.801280,-2.337780,8.259185,-8.514396,8.212019,6.684225,6.110570,-8.542207,0.815650,-0.443187,-5.533600,3.294232,-2.326949,-5.141162,-6.782637],[-2.789906,5.062641,-9.566925,2.721256,-4.039854,8.960732,-5.603937,1.057326,3.643681,7.747752,-8.744785,1.527025,-4.544205,-6.443417,-3.507795]],[[6.437093,-0.487282,9.366666,7.280867,1.095835,3.286266,-9.720864,-6.016358,-2.346544,-1.676699,3.104526,8.892388,-9.656001,-0.980681,-1.874287],[5.455498,5.257743,8.915106,-5.482859,8.729542,-3.282824,-3.887163,-8.825548,-1.186063,-5.028578,-0.743072,-6.416188,-2.773156,-4.149354,3.783153],[-8.621722,-4.403828,-3.928488,-1.886881,-8.881578,-9.757746,9.483598,3.673051,1.391590,-4.689302,-2.438344,7.470372,8.351870,8.900519,-5.072330],[-1.882669,4.009161,-0.998506,-6.843369,-1.105874,-9.960307,1.616556,-4.864999,-3.385769,2.392184,1.098127,6.054938,-1.387252,2.616553,-3.230533]],[[-7.823669,-6.351041,4.807727,1.881472,1.887495,6.315475,-0.888042,8.136642,8.535669,2.147854,9.818865,8.436316,1.796551,9.468831,1.586279],[7.745502,-2.529443,-1.401161,-3.083521,-6.687181,3.508476,-0.761026,-3.987657,-2.448929,0.455289,-4.875514,4.454668,1.904309,7.023962,4.758959],[4.749305,-3.100449,-3.729835,7.517188,-7.626525,-2.183141,9.833073,-8.481920,3.892119,-8.463958,-5.521273,8.070911,-2.823296,-9.740602,6.990964],[-7.071557,-4.415133,-4.491473,6.322300,-0.697150,8.018355,-0.148793,5.672144,2.747132,4.575592,5.581778,-1.560353,5.387350,7.665985,8.188969]],[[0.367098,5.080614,-9.000026,-7.567359,-6.803608,-5.193439,-2.858356,-1.434094,0.121503,-1.988178,3.854406,-5.790681,-2.905072,-8.522557,0.264655],[-4.895979,-9.013705,3.018962,2.279810,-0.408923,-7.593517,-1.846757,6.514601,-4.251575,-8.053459,-3.523212,-9.222892,7.519757,-9.027720,-6.735061],[5.165155,5.218729,1.993013,8.968911,-6.934934,-3.682331,-0.421385,6.721079,9.442498,-6.041354,-8.757661,-9.061809,1.273563,2.327004,1.325587],[7.576662,-2.048791,-6.587266,9.107206,1.385802,-2.800514,-8.160492,-8.444058,-1.279863,7.418232,0.237849,4.840536,-0.933444,0.247192,7.468196]],[[-2.546652,-7.408548,3.816298,-2.521270,-3.595008,-4.076727,7.674419,2.567946,2.945973,8.882106,-8.860921,-8.142784,-3.651291,-2.231164,2.261594],[9.890023,-1.047134,-5.448481,-4.382715,9.972850,-7.241171,7.816800,-0.783185,8.203823,2.642578,3.141207,7.472861,4.295476,-1.230844,-8.459827],[6.409632,3.122719,2.652725,9.585731,-0.239265,-6.124760,9.815115,-7.180782,-0.069444,3.843278,7.333042,4.583895,-0.958737,-1.343807,-3.974234],[-1.758951,-3.863386,1.300936,-2.487465,-8.815376,8.199147,0.884675,-4.925556,0.870381,-6.383274,-1.975595,3.050879,-5.629897,5.389462,-8.384643]],[[2.493748,4.004702,8.082642,9.106918,-0.546753,-4.306968,-3.062962,-3.248474,-6.481415,0.470815,-9.226568,-5.681140,9.332666,8.252192,0.539517],[-8.096572,7.413633,4.046288,2.367520,-3.353641,-7.354648,2.505354,-4.323846,5.709489,0.980776,4.942916,7.515103,9.662781,6.761330,3.907827],[1.122832,7.338003,6.933220,7.182170,-3.397599,-6.931251,-5.571745,7.514342,8.963118,4.306763,-0.041166,-1.021543,-5.163362,-4.701574,2.532320],[0.276431,-4.029568,5.161456,2.130155,-8.475770,-2.539535,-9.315015,-4.279155,0.886753,-0.196635,8.828104,-7.108792,-8.674250,6.799128,-7.934382]]], dtype = "float64")#candidate|6882|(13, 4, 15)|const|float64
uop_6883 = relay.rsqrt(const_6882.astype('float64')) # shape=(13, 4, 15)
uop_6887 = relay.sinh(uop_6883.astype('float64')) # shape=(13, 4, 15)
func_6544_call = mod.get_global_var('func_6544')
func_6546_call = mutated_mod.get_global_var('func_6546')
const_6896 = relay.const([-5.770991,-5.784550,8.996102,-7.254953,0.824402,-3.526508,-7.686208,-8.616038,4.893455,0.601094,4.499423,-7.785882,2.564488,-3.866443,-4.029036,9.835455,-7.663965,9.704587,5.658594,-9.872278,2.618789,-2.551799,-3.496468,-1.466627,3.051890,6.605977,-5.940216,-9.586763,-0.576091,-1.638605,4.220700,0.691920,-3.682555,1.715101,-8.237826,-8.529537,-1.164247,4.442831,5.844570,-9.470144,1.969581,-1.467783,7.327002,4.854541,9.100070,-7.611158,-4.327425,-2.765331,-2.644540,-2.951174,9.075316,4.658652,1.271568,8.995072,-5.482186,-0.227566,0.106959,-3.686537,6.775733,-3.726783,3.394552,8.984452,-5.115536,-5.192254,8.646783,4.153524,6.623243,7.261625,8.466565,-2.695297,-8.127981,1.783951,2.037501,5.852353,6.690476,8.590425,-5.291761,-1.923617,8.827114,-2.953278,0.844810,1.625319,-5.331311,-1.194676,3.540822,1.468935,5.115726,7.512640,-9.577485,5.422501,-8.275030,5.612978,-6.029555,0.198162,-1.293591,-9.958706,4.037218,9.395561,-3.541354,1.444702,-4.197702,-9.645097,3.536290,-1.722651,-1.615816,-5.511077,-1.426080,2.331803,6.968321,-1.132575,-6.689796,-2.581215,6.639583,0.148337,8.439729,9.337422,-0.755068,6.070182,-4.945913,6.950815,5.682228,8.727075,4.026294,-8.539581,-5.406362,3.626238,-1.147767,-4.800664,4.008164,4.974350,5.370445,-2.130169,-0.896729,6.986783,7.767690,9.641991,-8.701125,-7.379638,-5.306698,4.708423,-4.911123,8.109242,-8.384511,-6.401298,-5.566728,-3.916141,-5.300240,3.310680,-0.376135,2.572974,6.471161,-8.832696,-0.631601,-4.735055,-3.705950,6.460682,-3.514700,0.835274,-2.569500,-7.801340,2.924062,-1.680810,8.666379,8.823648,8.534418,6.365022,8.925726,-5.495994,-5.264081,-1.065954,-3.578046,2.712971,7.217161,1.873399,-8.015426,-6.105476,-9.553718,-3.801709,-3.741203,8.538201,-7.085728,-2.027561,6.190591,8.792346,1.313371,-4.163628,2.555389,-9.855879,-5.451550,4.937327,8.989190,-7.196053,-8.931201,4.317123,-7.913762,-5.217810,9.824077,5.241398,-3.472241,2.671423,-0.640424,6.265490,0.009410,-2.563017,-5.218327,9.420865,7.309184,9.270896,-8.376867,-4.332857,-7.338084,8.379622,-0.412441,-6.139057,-7.007024,-6.439960,0.134617,-4.367517,-6.063030,-7.178986,-4.234007,-9.051763,4.255301,-4.289912,1.483932,6.547408,3.189563,0.856117,2.431654,-8.006406,6.124731,-2.695941,1.086443,-7.155131,-3.774139,-4.602221,-4.506165,-8.923130,-1.900623,6.840512,-8.363972,5.238496,3.853435,0.550018,-2.834266,-2.700396,-2.564422,-2.200731,-1.262092,7.330889,4.674126,2.531468,6.533950,-0.448375,-8.122604,0.585119,-0.396150,7.166779,5.703360,-1.779162,-5.449217,-1.716047,2.092473,-5.946233,3.886064,-7.693367,0.211651,-1.409739,-3.633695,0.580687,-6.232760,3.765792,2.805254,-5.370944,6.581967,4.451425,-1.152820,-3.655859,-5.462018,2.452055,2.683137,0.087683,8.047169,5.502847,-2.594201,6.225657,5.237001,6.495999], dtype = "float64")#candidate|6896|(288,)|const|float64
call_6895 = relay.TupleGetItem(func_6544_call(relay.reshape(const_6896.astype('float64'), [2, 16, 9])), 0)
call_6897 = relay.TupleGetItem(func_6546_call(relay.reshape(const_6896.astype('float64'), [2, 16, 9])), 0)
func_6591_call = mod.get_global_var('func_6591')
func_6593_call = mutated_mod.get_global_var('func_6593')
call_6898 = relay.TupleGetItem(func_6591_call(), 1)
call_6899 = relay.TupleGetItem(func_6593_call(), 1)
func_5615_call = mod.get_global_var('func_5615')
func_5617_call = mutated_mod.get_global_var('func_5617')
call_6909 = relay.TupleGetItem(func_5615_call(), 0)
call_6910 = relay.TupleGetItem(func_5617_call(), 0)
func_5566_call = mod.get_global_var('func_5566')
func_5567_call = mutated_mod.get_global_var('func_5567')
call_6915 = relay.TupleGetItem(func_5566_call(), 0)
call_6916 = relay.TupleGetItem(func_5567_call(), 0)
output = relay.Tuple([uop_6887,call_6895,const_6896,call_6898,call_6909,call_6915,])
output2 = relay.Tuple([uop_6887,call_6897,const_6896,call_6899,call_6910,call_6916,])
func_6938 = relay.Function([], output)
mod['func_6938'] = func_6938
mod = relay.transform.InferType()(mod)
mutated_mod['func_6938'] = func_6938
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6938_call = mutated_mod.get_global_var('func_6938')
call_6939 = func_6938_call()
output = call_6939
func_6940 = relay.Function([], output)
mutated_mod['func_6940'] = func_6940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_6989 = relay.TupleGetItem(func_1733_call(), 0)
call_6990 = relay.TupleGetItem(func_1735_call(), 0)
output = call_6989
output2 = call_6990
func_7023 = relay.Function([], output)
mod['func_7023'] = func_7023
mod = relay.transform.InferType()(mod)
mutated_mod['func_7023'] = func_7023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7023_call = mutated_mod.get_global_var('func_7023')
call_7024 = func_7023_call()
output = call_7024
func_7025 = relay.Function([], output)
mutated_mod['func_7025'] = func_7025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4062_call = mod.get_global_var('func_4062')
func_4064_call = mutated_mod.get_global_var('func_4064')
call_7034 = relay.TupleGetItem(func_4062_call(), 1)
call_7035 = relay.TupleGetItem(func_4064_call(), 1)
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_7070 = func_3356_call()
call_7071 = func_3356_call()
func_3356_call = mod.get_global_var('func_3356')
func_3357_call = mutated_mod.get_global_var('func_3357')
call_7111 = func_3356_call()
call_7112 = func_3356_call()
output = relay.Tuple([call_7034,call_7070,call_7111,])
output2 = relay.Tuple([call_7035,call_7071,call_7112,])
func_7113 = relay.Function([], output)
mod['func_7113'] = func_7113
mod = relay.transform.InferType()(mod)
output = func_7113()
func_7114 = relay.Function([], output)
mutated_mod['func_7114'] = func_7114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3541_call = mod.get_global_var('func_3541')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_7135 = func_3541_call()
call_7136 = func_3541_call()
func_1433_call = mod.get_global_var('func_1433')
func_1435_call = mutated_mod.get_global_var('func_1435')
call_7149 = relay.TupleGetItem(func_1433_call(), 0)
call_7150 = relay.TupleGetItem(func_1435_call(), 0)
func_5576_call = mod.get_global_var('func_5576')
func_5577_call = mutated_mod.get_global_var('func_5577')
call_7164 = relay.TupleGetItem(func_5576_call(), 0)
call_7165 = relay.TupleGetItem(func_5577_call(), 0)
output = relay.Tuple([call_7135,call_7149,call_7164,])
output2 = relay.Tuple([call_7136,call_7150,call_7165,])
func_7182 = relay.Function([], output)
mod['func_7182'] = func_7182
mod = relay.transform.InferType()(mod)
output = func_7182()
func_7183 = relay.Function([], output)
mutated_mod['func_7183'] = func_7183
mutated_mod = relay.transform.InferType()(mutated_mod)
func_681_call = mod.get_global_var('func_681')
func_683_call = mutated_mod.get_global_var('func_683')
call_7199 = func_681_call()
call_7200 = func_681_call()
output = call_7199
output2 = call_7200
func_7207 = relay.Function([], output)
mod['func_7207'] = func_7207
mod = relay.transform.InferType()(mod)
output = func_7207()
func_7208 = relay.Function([], output)
mutated_mod['func_7208'] = func_7208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7286 = relay.var("var_7286", dtype = "bool", shape = (7, 8, 3))#candidate|7286|(7, 8, 3)|var|bool
var_7287 = relay.var("var_7287", dtype = "bool", shape = (7, 8, 3))#candidate|7287|(7, 8, 3)|var|bool
bop_7288 = relay.logical_or(var_7286.astype('bool'), relay.reshape(var_7287.astype('bool'), relay.shape_of(var_7286))) # shape=(7, 8, 3)
func_1652_call = mod.get_global_var('func_1652')
func_1654_call = mutated_mod.get_global_var('func_1654')
call_7291 = relay.TupleGetItem(func_1652_call(), 2)
call_7292 = relay.TupleGetItem(func_1654_call(), 2)
bop_7303 = relay.bitwise_and(var_7286.astype('uint32'), relay.reshape(var_7287.astype('uint32'), relay.shape_of(var_7286))) # shape=(7, 8, 3)
output = relay.Tuple([bop_7288,call_7291,bop_7303,])
output2 = relay.Tuple([bop_7288,call_7292,bop_7303,])
func_7317 = relay.Function([var_7286,var_7287,], output)
mod['func_7317'] = func_7317
mod = relay.transform.InferType()(mod)
var_7318 = relay.var("var_7318", dtype = "bool", shape = (7, 8, 3))#candidate|7318|(7, 8, 3)|var|bool
var_7319 = relay.var("var_7319", dtype = "bool", shape = (7, 8, 3))#candidate|7319|(7, 8, 3)|var|bool
output = func_7317(var_7318,var_7319,)
func_7320 = relay.Function([var_7318,var_7319,], output)
mutated_mod['func_7320'] = func_7320
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_7363 = relay.TupleGetItem(func_1053_call(), 2)
call_7364 = relay.TupleGetItem(func_1054_call(), 2)
output = relay.Tuple([call_7363,])
output2 = relay.Tuple([call_7364,])
func_7372 = relay.Function([], output)
mod['func_7372'] = func_7372
mod = relay.transform.InferType()(mod)
output = func_7372()
func_7373 = relay.Function([], output)
mutated_mod['func_7373'] = func_7373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_292_call = mod.get_global_var('func_292')
func_293_call = mutated_mod.get_global_var('func_293')
call_7374 = relay.TupleGetItem(func_292_call(), 0)
call_7375 = relay.TupleGetItem(func_293_call(), 0)
output = call_7374
output2 = call_7375
func_7393 = relay.Function([], output)
mod['func_7393'] = func_7393
mod = relay.transform.InferType()(mod)
output = func_7393()
func_7394 = relay.Function([], output)
mutated_mod['func_7394'] = func_7394
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7419 = relay.var("var_7419", dtype = "int8", shape = (13, 11, 13))#candidate|7419|(13, 11, 13)|var|int8
var_7420 = relay.var("var_7420", dtype = "int8", shape = (13, 11, 13))#candidate|7420|(13, 11, 13)|var|int8
bop_7421 = relay.maximum(var_7419.astype('int8'), relay.reshape(var_7420.astype('int8'), relay.shape_of(var_7419))) # shape=(13, 11, 13)
bop_7445 = relay.mod(var_7419.astype('float32'), relay.reshape(bop_7421.astype('float32'), relay.shape_of(var_7419))) # shape=(13, 11, 13)
func_1872_call = mod.get_global_var('func_1872')
func_1874_call = mutated_mod.get_global_var('func_1874')
call_7449 = relay.TupleGetItem(func_1872_call(), 0)
call_7450 = relay.TupleGetItem(func_1874_call(), 0)
func_7023_call = mod.get_global_var('func_7023')
func_7025_call = mutated_mod.get_global_var('func_7025')
call_7456 = func_7023_call()
call_7457 = func_7023_call()
var_7466 = relay.var("var_7466", dtype = "int8", shape = (13, 11, 13))#candidate|7466|(13, 11, 13)|var|int8
bop_7467 = relay.minimum(bop_7421.astype('float32'), relay.reshape(var_7466.astype('float32'), relay.shape_of(bop_7421))) # shape=(13, 11, 13)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_7501 = relay.TupleGetItem(func_3833_call(), 0)
call_7502 = relay.TupleGetItem(func_3835_call(), 0)
uop_7506 = relay.sigmoid(var_7419.astype('float64')) # shape=(13, 11, 13)
output = relay.Tuple([bop_7445,call_7449,call_7456,bop_7467,call_7501,uop_7506,])
output2 = relay.Tuple([bop_7445,call_7450,call_7457,bop_7467,call_7502,uop_7506,])
func_7515 = relay.Function([var_7419,var_7420,var_7466,], output)
mod['func_7515'] = func_7515
mod = relay.transform.InferType()(mod)
mutated_mod['func_7515'] = func_7515
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7515_call = mutated_mod.get_global_var('func_7515')
var_7517 = relay.var("var_7517", dtype = "int8", shape = (13, 11, 13))#candidate|7517|(13, 11, 13)|var|int8
var_7518 = relay.var("var_7518", dtype = "int8", shape = (13, 11, 13))#candidate|7518|(13, 11, 13)|var|int8
var_7519 = relay.var("var_7519", dtype = "int8", shape = (13, 11, 13))#candidate|7519|(13, 11, 13)|var|int8
call_7516 = func_7515_call(var_7517,var_7518,var_7519,)
output = call_7516
func_7520 = relay.Function([var_7517,var_7518,var_7519,], output)
mutated_mod['func_7520'] = func_7520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4062_call = mod.get_global_var('func_4062')
func_4064_call = mutated_mod.get_global_var('func_4064')
call_7561 = relay.TupleGetItem(func_4062_call(), 1)
call_7562 = relay.TupleGetItem(func_4064_call(), 1)
func_7317_call = mod.get_global_var('func_7317')
func_7320_call = mutated_mod.get_global_var('func_7320')
const_7564 = relay.const([[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True]], dtype = "bool")#candidate|7564|(168, 1)|const|bool
call_7563 = relay.TupleGetItem(func_7317_call(relay.reshape(const_7564.astype('bool'), [7, 8, 3]), relay.reshape(const_7564.astype('bool'), [7, 8, 3]), ), 1)
call_7565 = relay.TupleGetItem(func_7320_call(relay.reshape(const_7564.astype('bool'), [7, 8, 3]), relay.reshape(const_7564.astype('bool'), [7, 8, 3]), ), 1)
const_7575 = relay.const([[False,False,True],[False,True,False],[True,True,False],[True,True,True],[True,False,True],[False,False,True],[False,True,False],[True,False,False],[True,False,False],[False,False,False],[False,False,True],[True,False,False],[True,True,False],[True,False,True],[False,True,True],[True,True,True],[False,True,False],[True,False,True],[True,True,True],[True,True,True],[False,True,True],[True,False,True],[True,True,False],[True,False,False],[False,False,True],[True,False,False],[False,False,False],[True,True,False],[False,True,False],[True,False,True],[True,False,True],[False,True,True],[False,True,True],[False,False,True],[True,True,False],[False,False,False],[True,True,False],[True,False,False],[True,False,True],[True,True,True],[True,False,False],[False,True,True],[True,True,False],[False,True,True],[False,False,False],[False,True,False],[False,False,True],[False,True,True],[False,False,True],[True,False,True],[True,True,True],[True,True,False],[False,False,True],[True,True,True],[False,True,True],[False,True,False],[False,True,False],[False,True,True],[True,False,False],[True,True,False],[False,False,True],[True,True,False],[False,False,False],[True,True,True],[False,True,False],[False,True,True],[False,True,False],[True,True,False],[False,True,False],[False,False,True],[False,False,False],[True,True,True],[True,True,True],[False,True,False],[True,True,True],[False,True,False],[True,False,False],[False,True,True],[False,True,False],[False,False,False],[True,False,False],[True,False,False],[True,True,True],[False,True,False],[True,True,False],[False,True,True],[True,False,True],[True,False,False],[False,False,False],[True,False,False],[True,False,False],[False,True,False],[False,False,False],[True,True,True],[False,False,False],[False,False,True],[True,True,False],[True,False,False],[True,True,True],[True,False,True],[True,True,True],[False,True,True],[False,True,True],[False,True,False],[False,True,False],[False,True,True],[False,False,False],[False,True,True],[False,True,False],[True,False,False],[True,False,True],[False,False,True],[True,False,False],[True,True,True],[True,True,False],[False,True,True],[True,True,False],[True,True,True],[False,False,False],[False,True,True],[False,False,True],[False,True,True],[True,False,True],[True,True,False],[True,True,True],[True,True,True],[True,False,False],[True,True,False],[False,False,False],[True,False,True],[False,True,False],[True,True,True],[False,False,True],[True,True,True],[False,False,False],[True,False,True],[False,True,True],[True,False,False],[True,False,False],[True,True,True],[False,True,False],[False,False,True],[True,False,True],[True,False,False],[False,False,True],[False,True,True],[True,False,False],[False,True,False],[False,False,False],[True,True,False],[False,True,True],[False,False,False],[True,True,False],[False,False,False],[False,False,False],[True,False,False],[False,True,False],[False,True,True],[False,False,True],[True,True,False],[True,True,True],[False,True,True],[False,False,True],[True,False,True],[True,False,False],[False,False,False],[False,False,False],[False,True,True]], dtype = "bool")#candidate|7575|(168, 3)|const|bool
bop_7576 = relay.add(const_7564.astype('int64'), const_7575.astype('int64')) # shape=(168, 3)
func_5566_call = mod.get_global_var('func_5566')
func_5567_call = mutated_mod.get_global_var('func_5567')
call_7585 = relay.TupleGetItem(func_5566_call(), 0)
call_7586 = relay.TupleGetItem(func_5567_call(), 0)
output = relay.Tuple([call_7561,call_7563,bop_7576,call_7585,])
output2 = relay.Tuple([call_7562,call_7565,bop_7576,call_7586,])
func_7590 = relay.Function([], output)
mod['func_7590'] = func_7590
mod = relay.transform.InferType()(mod)
output = func_7590()
func_7591 = relay.Function([], output)
mutated_mod['func_7591'] = func_7591
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5826_call = mod.get_global_var('func_5826')
func_5828_call = mutated_mod.get_global_var('func_5828')
call_7595 = relay.TupleGetItem(func_5826_call(), 1)
call_7596 = relay.TupleGetItem(func_5828_call(), 1)
func_6518_call = mod.get_global_var('func_6518')
func_6521_call = mutated_mod.get_global_var('func_6521')
const_7604 = relay.const([-5,10,-4,2,-6,-1,-9,-6,-1,1,6,-7,6,7,5,-3,4,6,4,-7,7,5,7,3,4,1,5,10,-7,-7,10,-5,-3,2,1,8,-7,7,6,1,6,-3,1,-2,-2,-3,9,7,-10,-1,-8,10,2,1,-7,-10,-6,4,6,-8,-5,1,10,5,-6,-1,-5,-10,-8,7,-5,10,9,1,-8,-2,-1,-8,-10,8,-1,-10,10,5,3,5,10,9,7,-5,-8,-9,-9,-7,10,-4,-6,9,-4,-4,-8,-5,2,10,-2,8,1,9,6,10,3,9,8,-5,-2,-9,8,1,-8,1,5,9,9,-5,-6,-1,6,-10,7,9,4,2,-2,2,-5,9,2,-3,8,6,-10,2,-8,-2,-8,6,9,-4,2,-10,-8,-6,-6,1,-6,5,5,-4,2,8,7,9,-4,8,8,-3,-6,7,8,6,-7,10,10,5,-1,1,-6,5,-3,6,-10,10,-7,-8,6,-9,-6,-7,4,-10,2,3,2,-8,3,-8,4,-9,-6,-6,-10,7,5,-4,-3,-3,6,5,-6,-4,-10,9,2,-4,4,1,6,-4,2,-7,-4,4,-6,9,5,-10,8,8,9,8,-4,1,-9,-9,3,-7,-8,-9,1,8,-1,-2,10,-9,-2,4,6,-5,10,-5,4,4,-5,8,-8,4,9,-8,-6,9,2,5,9,-2,-6,6,8,-1,2,1,-8,-1,10,5,6,5,7,7,-10,7,-5,5,2,8,-5,-3,-5,1,4,3,-10,-8,-8,5,4,-1,6,4,-2,-3,3,-2,-10,4,-1,-6,5,7,10,9,-5,-5,-8,8,-3,-7,-7,-5,-3,3,-7,-2,4,4,-5,-8,-3,9,3,-1,10,-5,8,6,-2,-3,9,-9,-9,4,4,-2,6,10,3,-8,-1,10,6,1,6,-4,1,7,-6,4,5,-1,-9,10,4,5,-4,7,10,7,3,-10,-7,-6,7,5,8,-1,-8,-9,3,-10,-6,7,4,-1,-7,3,7,9,9,-6,-1,-4,-1,1,-6,1,7,-9,3,-8,-2,-6,-10,2,10,-6,6,2,-10,1,4,-7,1,-2,7,-7,-2,-7,2,2,9,5,-8,3,7,-4,-6,-2,9,1,7,-3,5,-3,-1,-8,-5,-6,-7,-10,4,9,-7,7,6,-9,10,-4,-4,-1,-4,-7,-2,-1,-3,5,-5,7,5,7,6,6,2,10,-7,-2,7,-9,2,8,-8,-3,9,-6,-6,10,3,-7,-6,-10,7,5,1,3,-1,-9,7,-4,5,-3,-7,4,-8,4,7,8,-7,-10,-6,-4,-5,8,6,-10,-3,4,5,9,-9,9,8,2,2,-6,4,-5,-4,2,-6,2,7,-1,-2,-8,-5,6,6,-3,-7,-5,10,1,5,-3,-8,-10,9,-9,-2,-1,-6,4,-5,8,-5,-3,5,6,-9,-10,-4,-2,-2,3,10,2,-10,-7,3,-7,2,-1,5,-8,-8,1,-9,-4,-8,4,2,-5,4,7,9,6,-7,-8,-8,-9,5,8,-5,-2,1,2,-5,4,-8,9,-9,9,-5,10,-5,10,9,3,-2,6,4,5,-4,1,3,1,6,-10,1,6,7,8,-8,1,-8,3,6,9,8,3,-9,-3,-6,-8,3,5,-2,7,5,-9,-4,3,10,-9,4,-10,-6,-2,8,-1,5,-10,-10,8,4,8,-8,7,5,-6,7,5,-9,-8,-6,7,-9,-8,-5,-4,-4,6,-3,1,10,-10,1,10,10,-6,-1,8,9,8,-4,2,5,1,-2,8,8,-9,-1,1,-9,10,2,-9,-7,7,-1,1,-1,-4,3,-5,7,-3,4,-4,5,-4,-3,9,4,-3,-7,9,-7,10,-4,-2,-10,-1,-1,9,10,-2,-10,5,7,7,10,-1,-8,8,6,4,7,2,2,-5,-7,-5,7,9,6,7,3,-5,-9,-4,3,10,-3,9,4,-8,-2,-7,1,-5,3,4,-2,-8,2,-5,-10,-8,-9,-10,2,5,-9,2,-10,8,1,-9,1,-1,9,-1,-2,2,7,-6,8,-2,4,8,3,7,-7,4,-6,-2,-2,4,1,5,5,-6,3,-1,-4,-10,6,8,8,3,8,8,10,1,-5,-1,8,-5,-5,-9,-7,5,-8,7,6,9,7,3,-7,-1,5,-5,9,-5,8,5,-2,-9,5,6,7,-7,-3,6,-9,4,-10,6,-1,-6,-2,4,-5,-6,-10,4,-8,-4,5,10,-8,7,-5,7,-3,-3,-8,-1,-10,3,-7,-7,-2,-5,4,1,2,-8,-1,1,10,1,2,10,6,4,-2,10,6,1,3,-10,1,9,6,8,-7,3,8,3,-7,-1,10,3,9,3,-5,4,-4,-10,7,6,4,3,-3,9,-5,-10,-2,-10,4,-2,8,-7,-10,-1,-4,1,6,-3,4,10,-2,4,-3,6,8,10,-3,8,-3,-2,-8,6,-1,-5,-1,-4,-7,-9,-5,-10,1,10,-7,1,9,-9,-8,-1,4,-6,10,9,10,-8,1,7,9,5,-6,-8,-2,2,-1,-1,-8,1,-6,-5,-6,-9,-4,8,4,9,-2,6,3,-3,2,3,-10,-10,-7,-1,10,2,8,7,-5,-3,3,-10,9,5,7,3,-4,-4,-8,4,4,-3,-5,-6,7,7,9,10,-3,3,-5,-9,-1,-10,7,8,1,6,2,-8,9,10,-5,10,-5,9,-1,-9,-3,-1,6,-4,1,-4,-9,-1,-8,-10,1,-2,-5,6,-1,-6,5,-7,-7,7,8,-2,-4,7,3,-6,9,1,-8,10,4,-8,-5,2,-3,-3,-10,9,-7,-7,-6,-7,8,-9,-6,10,6,1,-2,-5,-3,7,1,-9,-2,1,9,3,7,-8,10,7,5,-7,-2,-3,9,8,3,10,-4,-5,8,-2,7,-10,-7,3,4,10,-10,-10,-10,1,-6,1,4,2,-4,-9,-4,8,-7,-3,10,-8,6,-1,4,10,-3,-9,8,8,-8,1,-7,3,-1,-6,2,1,-2,2,4,-8,-4,-3,8,4,-2,8,-5,5,7,-9,5,-7,-2,-3,-3,-5,-7,1,4,1,-10,5,-10,-3,2,-8,-2,4,-3,2,9,3,10,1,-9,7,-3,-5,3,-10,10,1,-2,-9,3,1,1,-8,-9,-2,-3,-8,-5,7,-10,2,6,5,-8,5,6,-3,-1,7,-10,-8,1,-7,-8,-2,-3,10,10,9,8,1,-9,10,-3,-10,7,6,-4,4,-7,-2,-3,-4,-10,2,7,3,-8,-8,1,4,7,-7,2,7,-8,-2,3,-5,-8,-10,-10,5,-5,9,-2,-5,-2,4,-4,3,-9,-4,-2,-3,5,7,6,3,4,9,-4,7,-7,-10,-1,4,10,10,6,-2,9,-8,1,6,3,1,10,-3,-6,-9,-10,7,-10,1,2,-8,-5,4,8,-1,-3,-8,8,-9,6,1,10,5,-5,-5,4,-8,2,4,1,-4,-6,7,-6,10,6,-8,-1,4,3,-3,-7,-5,2,-2,5,-9,-8,6,-5,-6,10,-5,10,7,3,2,2,10,7,8,7,6,4,-7,-10,9,-8,-1,8,-4,9,-10,3,6,3,3,-1,-5,-3,-5,-7,3,1,-6,5,9,-5,-4,2,-8,3,-4,10,-9,-4,-6,-9,8,6,-10,-5,-4,9,-7,-7,7,-6,-4,10,1,-8,-5,-9,-8,7,5,-8,-2,-8,-9,4,7,-4,-10,6,8,-10,4,6,-6,1,-4,-4,-5,5,-7,7,1,-7,-8,2,-1,-9,-4,7,7,-5,7,9,-10,-4,-5,3,4,9,-4,-10,-5,-8,-5,1,4,-6,3,-1,-2,-2,-9,5,4,7,-4,1,-7,10,-7,-5,7,2,-7,-5,-1,5,9,-3,-5,10,-9,-1,-1,10,4,-9,-9,2,-7,6,-5,7,-3,8,-3,7,9,-8,-1,-8,-8,-7,-1,2,10,-5,-8,-9,-3,9,5,-7,6,-5,-6,1,4,-10,10,5,1,-3,2,-2,-10,10,6,10,-3,-8,-1,-4,10,-2,-7,8,-4,-8,4,-1,2,-10,9,2,-6,-2,1,2,1,2,8,9,-3,-10,9,-3,-5,9,4,7,-2,-5,-8,-6,10,10,-10,-3,5,3,-9,5,9,9,7,-3,8,4,6,6,2,5,-4,-6,-4,-3,5,-6,-5,-10,-2,1,-9,-7,-7,-1,8,2,4,10,-8,10,2,10,2,8,-10,-3,6,-6,-2,3,-4,-9,4,8,-2,-7,-6,-2,6,-10,10,9,-5,8,-5,7,-5,-10,6,1,8,-4,5,-3,-7,1,-8,3,7,-3,2,10,6,6,-9,10,3,2,-10,-10,9,4,2,-3,9,-9,-5,8,-2,1,-1,9,-5,-3,7,1,5,-5,3,5,-3,-2,-7,10,-5,1,4,-10,-2,-5,8,-6,1,9,-9,-5,3,3,-8,-1,5,-8,1,-9,1,-5,10,-2,-3,5,9,6,-5,-2,-3,-5,5,9,-1,3,10,3,-9,1,7,-6,3,-8,5,3,-5,6,2,-9,4,7,10,-6,-6,-3,-2,-1,2,-5,-1,5,-7,-9,-6,1,8,6,9,-9,8,10,-10,6,10,9,2,-9,-4,-5,7,-2,8,-5,1,-2,5,-10,-2,-8,-2,4,-10,-10,-3,7,-4,5,9,7,-3,1,-2,2,9,-6,7,-4,5,1,8,-10,-9,4,-6,-9,1,-6,3,7,-9,5,-3,3,1,-9,-6,-3,5,-4,-10,9,-7,4,-4,3,4,-9,7,8,-10,10,8,-10,3,-2,-10,-2,-8,6,9,-5,-5,3,-10,9,10,7,-3,8,4,-8,-3,-9,9,4,5,5,8,2,-9,-10,-2,-4,6,2,-6,-2,1,1,-9,9,4,1,-2,-2,6,9,-8,5,-6,2,7,2,-7,7,-8,7,-2,6,3,-4,-7,-1,7,7,-2,7,4,7,-10,5,-3,-10,3,1,-1,7,8,-4,-3,-10,1,4,7,-7,6,-5,-4,-5,2,-5,1,-2,9,3,7,8,-1,3,4,4,-2,10,-5,-5,3,9,-1,4,-5,3,-2,-9,-3,-10,-2,6,5,-10,-3,9,-2,-1,-9,4,-1,7,-7,-6,-1,-9,5,7,-3,2,9,-3,8,-5,-8,3,5,1,-8,-6,5,2,-1,10,5,10,-3,-6,-9,-10,-1,4,-4,-1,4,-3,-1,1,-3,7,-4,3,-2,-10,1,5,4,-7,-6,3,6,-1,1,10,-4,4,-4,7,6,-6,-9,9,2,-2,-4,8,-10,-6,2,5,-3,-8,-5,-2,2,8,-10,-5,-2,-9,-1,-6,-8,10,-10,-6,5,9,-8,-3,-8,-4,-7,-1,5,7,8,6,8,4,2,-1,7,-9,1,-7,-4,-7,1,1,-9,3,6,1,-5,3,8,-6,-4,-10,-8,3,-2,-4,8,1,6,5,1,-7,5,-4,4,8,5,-10,-8,5,-5,3,4,3,5,-1,5,3,-8,3,-6,-9,-10,4,-3,-8,-5,2,-2,-9,-2,-3,10,7,4,-1,10,3,-10,9,-5,-2,5,-2,-8,6,-3,8,-7,-5,-2,3,-6,-3,-3,-10,7,-1,-7,-1,-3,-6,6,-4,-9,-5,-5,7,7,10,2,2,-3,6,-5,-4,4,7,-5,6,-9,-9,1,8,5,2,7,1,-7,7,-3,-10,-2,-10,7,-3,9,1,-9,10,6,-3,5,10,-10,4,7,-2,-3,7,8,-6,-3,7,-7,-6,-10,-5,-3,-1,-1,6,-8,-8,9,-1,-5,-4,-6,-8,9,-8,-3,7,8,-8,-2,-7,-1,3,10,8,1,-4,4,-3,-6,-3,-4,4,8,-10,-6,-3,4,6,-10,-1,-8,-9,7,-5,-5,-3,-1,-2,8,-1,3,-1,10,2,6,10,-8,-4,10,-9,8,-5,-10,-7,-1,5,2,10,7,-9,-5,7,-7,2,2,4,5,8,8,-6,-6,10,8,10,-2,-10,-10,-4,-8,6,-8,-10,2,10,5,-9,-8,-7,-9,-4,7,-9,1,-4,8,8,2,2,-4,-6,-10,-10,-1,7,-5,10,4,-1,-1,-3,6,-8,7,-6,2,-2,6,1,10,-9,10,8,-9,1,5,2,5,-2,9,5,-2,4,-10,5,-6,6,-4,-9,5,-4,4,-2,5,1,-3,-5,-7,3,7,-9,10,6,10,-6,5,-5,-3,6,-2,2,-5,-2,-6,-10,-3,-4,4,7,-7,-1,3,9,-5,-6,4,-4,-2,1,-1,3,-10,9,8,10,-8,-8,-6,-9,-2,8,2,4,10,6,-6,7,7,-10,1,2,10,2,-7,-7,-7,-6,8,-5,-7,2,-9,1,-5,10,-10,7,10,-8,-2,5,-1,-8,-3,7,-3,3,-8,-5,5,8,8,7,-7,-5,9,8,-3,9,3,-7,-5,-8,5,3,-1,-7,-8,-6,-1,-4,3,10,-2,5,5,2,2,-2,-3,9,7,10,-2,2,9,6,10,1,7,7,-6,1,-9,7,9,6,1,3,4,1,-1,-7,-2,-5,4,2,-3,10,-7,5,-10,-2,-9,-8,-10,8,5,4,-6,10,-3,2,5,-7,8,10,3,2,-7,-4,-1,-10,-10,6,5,5,-8,3,8,8,4,-5,10,-10,8,-5,8,5,-2,-3,-7,-7,7,8,2,5,-4,2,6,10,-7,2,2,3,-8,-3,9,10,9,-5,-4,6,9,-3,-1,-10,9,4,-3,7,7,8,1,-4,-6,1,7,9,7,-2,4,-9,-8,-6,1,-2,-5,-6,8,7,9,5,7,-2,5,-5,10,4,6,-8,-3,-7,1,-7,5,3,3,-8,2,-5,7,-6,1,-4,-9,-5,-3,3,8,-2,-3,7,-3,-6,-6,-9,-10,-8,6,9,-4,-8,-1,-10,-2,-1,7,10,-2,2,9,1,-10,-2,2,-2,8,-3,2,7,6,-8,8,3,-6,10,-8,-7,-9,-5,-2,9,-6,8,-6,3,-7,-6,-10,-4,4,4,-2,-2,-1,6,-3,-5,7,-8,-10,-6,-1,1,1,-10,7,9,-6,-4,8,-2,5,10,3,-5,-1,10,-3,-5,-4,7,10,5,-7,-5,-1,5,-6,-7,5,2,3,1,-2,-8,3,10,-3,9,5,4,3,-1,-4,-8,10,-8,1,-9,-6,-9,-6,2,5,-1,9,8,7,-3,-8,2,8,-1,9,-1,-6,-6,9,-2,-1,-5,-8,-2,-2,8,3,-8,-9,-1,-8,5,-1,6,9,2,-1,-8,-2,6,3,-6,3,9,-4,2,3,5,10,-3,7,9,-6,9,-9,-4,6,-1,5,-2,-2,-8,-6,10,4,7,3,-9,4,9,-2,8,-2,-8,-10,-3,-7,-1,3,8,-7,1,10,-10,-8,10,9,-10,8,5,10,-2,8,9,5,1,2,-1,-1,-9,-10,-3,-8,10,-2,-3,3,-1,-7,6,-8,3,10,2,-6,2,-3,-7,-9,6,1,6,-5,7,-5,-5,2,3,-5,-3,10,-9,10,4,10,-3,-1,5,5,-1,4,3,3,8,-5,-9,6,-7,-3,-8,-3,3,9,2,-1,4,9,3,-7,2,-10,4,10,-4,4,-5,2,-3,-8,-5,-9,6,10,4,10,9,8,8,7,-2,-2,10,-6,7,9,3,-2,-8,10,-2,-7,-2,6,-4,2,4,2,9,6,-2,-7,4,5,4,5,6,6,-8,8,5,-9,-5,4,9,-8,-8,-7,4,6,7,-5,5,3,-6,-9,-2,-4,7,8,10,8,-1,-2,-7,5,2,-9,1,-4,4,10,10,-2,1,-5,-8,-1,-8,-3,1,-8,-8,-2,10,10,7,-1,-5,4,-3,-9,3,-9,2,3,2,8,2,-10,8,-6,9,2,10,-10,-8,-5,10,10,-8,7,8,-1,-9,-1,-1,2,6,-6,3,-1,-6,9,-2,9,-4,3,4,-2,-5,10,2,5,-5,4,8,8,-4,9,-10,10,-5,-7,5,3,-2,5,2,-2,3,-8,1,-5,7,-3,-2,-2,-5,7,-8,-1,1,4,8,-4,-2,-3,10,-10,-2,3,-9,1,2,6,-8,10,-5,-5,-10,5,3,9,-6,10,3,1,6,5,-10,8,8,-9,4,-5,5,8,-9,-1,5,4,5,-1,-9,-9,-9,-9,6,-9,2,-7,-7,-6,2,-3,9,9,7,4,-8,7,1,2,3,-8,-7,-1,9,-3,5,2,-5,9,-10,-8,-8,-4,10,-6,1,-6,-10,5,6,-2,3,-6,-4,-8,8,3,-10,4], dtype = "uint64")#candidate|7604|(3136,)|const|uint64
call_7603 = relay.TupleGetItem(func_6518_call(relay.reshape(const_7604.astype('uint64'), [3136,])), 4)
call_7605 = relay.TupleGetItem(func_6521_call(relay.reshape(const_7604.astype('uint64'), [3136,])), 4)
output = relay.Tuple([call_7595,call_7603,const_7604,])
output2 = relay.Tuple([call_7596,call_7605,const_7604,])
func_7612 = relay.Function([], output)
mod['func_7612'] = func_7612
mod = relay.transform.InferType()(mod)
output = func_7612()
func_7613 = relay.Function([], output)
mutated_mod['func_7613'] = func_7613
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7372_call = mod.get_global_var('func_7372')
func_7373_call = mutated_mod.get_global_var('func_7373')
call_7624 = relay.TupleGetItem(func_7372_call(), 0)
call_7625 = relay.TupleGetItem(func_7373_call(), 0)
output = call_7624
output2 = call_7625
func_7651 = relay.Function([], output)
mod['func_7651'] = func_7651
mod = relay.transform.InferType()(mod)
output = func_7651()
func_7652 = relay.Function([], output)
mutated_mod['func_7652'] = func_7652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6763_call = mod.get_global_var('func_6763')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_7653 = relay.TupleGetItem(func_6763_call(), 0)
call_7654 = relay.TupleGetItem(func_6764_call(), 0)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_7655 = relay.TupleGetItem(func_3004_call(), 1)
call_7656 = relay.TupleGetItem(func_3006_call(), 1)
func_5566_call = mod.get_global_var('func_5566')
func_5567_call = mutated_mod.get_global_var('func_5567')
call_7663 = relay.TupleGetItem(func_5566_call(), 0)
call_7664 = relay.TupleGetItem(func_5567_call(), 0)
output = relay.Tuple([call_7653,call_7655,call_7663,])
output2 = relay.Tuple([call_7654,call_7656,call_7664,])
func_7677 = relay.Function([], output)
mod['func_7677'] = func_7677
mod = relay.transform.InferType()(mod)
output = func_7677()
func_7678 = relay.Function([], output)
mutated_mod['func_7678'] = func_7678
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1544_call = mod.get_global_var('func_1544')
func_1545_call = mutated_mod.get_global_var('func_1545')
call_7706 = relay.TupleGetItem(func_1544_call(), 0)
call_7707 = relay.TupleGetItem(func_1545_call(), 0)
func_2208_call = mod.get_global_var('func_2208')
func_2210_call = mutated_mod.get_global_var('func_2210')
const_7732 = relay.const(-1, dtype = "uint64")#candidate|7732|()|const|uint64
call_7731 = relay.TupleGetItem(func_2208_call(relay.reshape(const_7732.astype('uint64'), [])), 2)
call_7733 = relay.TupleGetItem(func_2210_call(relay.reshape(const_7732.astype('uint64'), [])), 2)
output = relay.Tuple([call_7706,call_7731,const_7732,])
output2 = relay.Tuple([call_7707,call_7733,const_7732,])
func_7742 = relay.Function([], output)
mod['func_7742'] = func_7742
mod = relay.transform.InferType()(mod)
mutated_mod['func_7742'] = func_7742
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7742_call = mutated_mod.get_global_var('func_7742')
call_7743 = func_7742_call()
output = call_7743
func_7744 = relay.Function([], output)
mutated_mod['func_7744'] = func_7744
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7798 = relay.const([[[1,5],[-10,6],[-7,4],[7,-6],[-10,-5],[-1,-2],[-3,9],[-1,5],[5,-3],[-3,10],[-1,-3],[-2,-1]],[[-9,-3],[-1,1],[-7,7],[-3,9],[2,-5],[-4,5],[1,2],[-7,8],[-1,6],[7,7],[-8,-1],[7,-9]],[[5,-4],[-8,2],[6,-5],[-9,7],[-7,2],[-2,9],[3,9],[1,9],[-9,-2],[-1,-6],[-10,-8],[-7,7]],[[-9,9],[9,-9],[7,4],[-5,3],[5,1],[-2,3],[-2,-9],[5,3],[8,-5],[-2,-1],[2,9],[8,1]],[[9,-1],[1,-3],[6,-1],[1,-7],[10,5],[-6,-2],[-2,8],[-3,5],[-3,5],[2,-6],[-1,9],[3,-10]]], dtype = "int8")#candidate|7798|(5, 12, 2)|const|int8
var_7799 = relay.var("var_7799", dtype = "int8", shape = (5, 12, 2))#candidate|7799|(5, 12, 2)|var|int8
bop_7800 = relay.equal(const_7798.astype('bool'), relay.reshape(var_7799.astype('bool'), relay.shape_of(const_7798))) # shape=(5, 12, 2)
output = bop_7800
output2 = bop_7800
func_7824 = relay.Function([var_7799,], output)
mod['func_7824'] = func_7824
mod = relay.transform.InferType()(mod)
var_7825 = relay.var("var_7825", dtype = "int8", shape = (5, 12, 2))#candidate|7825|(5, 12, 2)|var|int8
output = func_7824(var_7825)
func_7826 = relay.Function([var_7825], output)
mutated_mod['func_7826'] = func_7826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4087_call = mod.get_global_var('func_4087')
func_4089_call = mutated_mod.get_global_var('func_4089')
call_7831 = relay.TupleGetItem(func_4087_call(), 1)
call_7832 = relay.TupleGetItem(func_4089_call(), 1)
output = call_7831
output2 = call_7832
func_7847 = relay.Function([], output)
mod['func_7847'] = func_7847
mod = relay.transform.InferType()(mod)
output = func_7847()
func_7848 = relay.Function([], output)
mutated_mod['func_7848'] = func_7848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4596_call = mod.get_global_var('func_4596')
func_4598_call = mutated_mod.get_global_var('func_4598')
call_7862 = relay.TupleGetItem(func_4596_call(), 0)
call_7863 = relay.TupleGetItem(func_4598_call(), 0)
output = call_7862
output2 = call_7863
func_7864 = relay.Function([], output)
mod['func_7864'] = func_7864
mod = relay.transform.InferType()(mod)
output = func_7864()
func_7865 = relay.Function([], output)
mutated_mod['func_7865'] = func_7865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_509_call = mod.get_global_var('func_509')
func_510_call = mutated_mod.get_global_var('func_510')
call_8003 = relay.TupleGetItem(func_509_call(), 0)
call_8004 = relay.TupleGetItem(func_510_call(), 0)
output = relay.Tuple([call_8003,])
output2 = relay.Tuple([call_8004,])
func_8024 = relay.Function([], output)
mod['func_8024'] = func_8024
mod = relay.transform.InferType()(mod)
output = func_8024()
func_8025 = relay.Function([], output)
mutated_mod['func_8025'] = func_8025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7023_call = mod.get_global_var('func_7023')
func_7025_call = mutated_mod.get_global_var('func_7025')
call_8045 = func_7023_call()
call_8046 = func_7023_call()
output = call_8045
output2 = call_8046
func_8050 = relay.Function([], output)
mod['func_8050'] = func_8050
mod = relay.transform.InferType()(mod)
output = func_8050()
func_8051 = relay.Function([], output)
mutated_mod['func_8051'] = func_8051
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8072 = relay.var("var_8072", dtype = "uint64", shape = (6, 14, 13))#candidate|8072|(6, 14, 13)|var|uint64
var_8073 = relay.var("var_8073", dtype = "uint64", shape = (6, 14, 13))#candidate|8073|(6, 14, 13)|var|uint64
bop_8074 = relay.equal(var_8072.astype('bool'), relay.reshape(var_8073.astype('bool'), relay.shape_of(var_8072))) # shape=(6, 14, 13)
output = bop_8074
output2 = bop_8074
func_8085 = relay.Function([var_8072,var_8073,], output)
mod['func_8085'] = func_8085
mod = relay.transform.InferType()(mod)
mutated_mod['func_8085'] = func_8085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8085_call = mutated_mod.get_global_var('func_8085')
var_8087 = relay.var("var_8087", dtype = "uint64", shape = (6, 14, 13))#candidate|8087|(6, 14, 13)|var|uint64
var_8088 = relay.var("var_8088", dtype = "uint64", shape = (6, 14, 13))#candidate|8088|(6, 14, 13)|var|uint64
call_8086 = func_8085_call(var_8087,var_8088,)
output = call_8086
func_8089 = relay.Function([var_8087,var_8088,], output)
mutated_mod['func_8089'] = func_8089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4062_call = mod.get_global_var('func_4062')
func_4064_call = mutated_mod.get_global_var('func_4064')
call_8091 = relay.TupleGetItem(func_4062_call(), 0)
call_8092 = relay.TupleGetItem(func_4064_call(), 0)
output = relay.Tuple([call_8091,])
output2 = relay.Tuple([call_8092,])
func_8118 = relay.Function([], output)
mod['func_8118'] = func_8118
mod = relay.transform.InferType()(mod)
output = func_8118()
func_8119 = relay.Function([], output)
mutated_mod['func_8119'] = func_8119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5566_call = mod.get_global_var('func_5566')
func_5567_call = mutated_mod.get_global_var('func_5567')
call_8137 = relay.TupleGetItem(func_5566_call(), 0)
call_8138 = relay.TupleGetItem(func_5567_call(), 0)
func_7677_call = mod.get_global_var('func_7677')
func_7678_call = mutated_mod.get_global_var('func_7678')
call_8157 = relay.TupleGetItem(func_7677_call(), 1)
call_8158 = relay.TupleGetItem(func_7678_call(), 1)
output = relay.Tuple([call_8137,call_8157,])
output2 = relay.Tuple([call_8138,call_8158,])
func_8169 = relay.Function([], output)
mod['func_8169'] = func_8169
mod = relay.transform.InferType()(mod)
mutated_mod['func_8169'] = func_8169
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8169_call = mutated_mod.get_global_var('func_8169')
call_8170 = func_8169_call()
output = call_8170
func_8171 = relay.Function([], output)
mutated_mod['func_8171'] = func_8171
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6411_call = mod.get_global_var('func_6411')
func_6412_call = mutated_mod.get_global_var('func_6412')
call_8179 = relay.TupleGetItem(func_6411_call(), 2)
call_8180 = relay.TupleGetItem(func_6412_call(), 2)
output = relay.Tuple([call_8179,])
output2 = relay.Tuple([call_8180,])
func_8181 = relay.Function([], output)
mod['func_8181'] = func_8181
mod = relay.transform.InferType()(mod)
output = func_8181()
func_8182 = relay.Function([], output)
mutated_mod['func_8182'] = func_8182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_8227 = relay.TupleGetItem(func_2467_call(), 1)
call_8228 = relay.TupleGetItem(func_2468_call(), 1)
func_1053_call = mod.get_global_var('func_1053')
func_1054_call = mutated_mod.get_global_var('func_1054')
call_8233 = relay.TupleGetItem(func_1053_call(), 1)
call_8234 = relay.TupleGetItem(func_1054_call(), 1)
output = relay.Tuple([call_8227,call_8233,])
output2 = relay.Tuple([call_8228,call_8234,])
func_8241 = relay.Function([], output)
mod['func_8241'] = func_8241
mod = relay.transform.InferType()(mod)
output = func_8241()
func_8242 = relay.Function([], output)
mutated_mod['func_8242'] = func_8242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7651_call = mod.get_global_var('func_7651')
func_7652_call = mutated_mod.get_global_var('func_7652')
call_8270 = func_7651_call()
call_8271 = func_7651_call()
output = relay.Tuple([call_8270,])
output2 = relay.Tuple([call_8271,])
func_8293 = relay.Function([], output)
mod['func_8293'] = func_8293
mod = relay.transform.InferType()(mod)
output = func_8293()
func_8294 = relay.Function([], output)
mutated_mod['func_8294'] = func_8294
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5318_call = mod.get_global_var('func_5318')
func_5320_call = mutated_mod.get_global_var('func_5320')
call_8302 = func_5318_call()
call_8303 = func_5318_call()
output = relay.Tuple([call_8302,])
output2 = relay.Tuple([call_8303,])
func_8313 = relay.Function([], output)
mod['func_8313'] = func_8313
mod = relay.transform.InferType()(mod)
mutated_mod['func_8313'] = func_8313
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8313_call = mutated_mod.get_global_var('func_8313')
call_8314 = func_8313_call()
output = call_8314
func_8315 = relay.Function([], output)
mutated_mod['func_8315'] = func_8315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7651_call = mod.get_global_var('func_7651')
func_7652_call = mutated_mod.get_global_var('func_7652')
call_8334 = func_7651_call()
call_8335 = func_7651_call()
output = call_8334
output2 = call_8335
func_8348 = relay.Function([], output)
mod['func_8348'] = func_8348
mod = relay.transform.InferType()(mod)
mutated_mod['func_8348'] = func_8348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8348_call = mutated_mod.get_global_var('func_8348')
call_8349 = func_8348_call()
output = call_8349
func_8350 = relay.Function([], output)
mutated_mod['func_8350'] = func_8350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5409_call = mod.get_global_var('func_5409')
func_5410_call = mutated_mod.get_global_var('func_5410')
call_8351 = relay.TupleGetItem(func_5409_call(), 1)
call_8352 = relay.TupleGetItem(func_5410_call(), 1)
func_4719_call = mod.get_global_var('func_4719')
func_4721_call = mutated_mod.get_global_var('func_4721')
call_8358 = relay.TupleGetItem(func_4719_call(), 0)
call_8359 = relay.TupleGetItem(func_4721_call(), 0)
output = relay.Tuple([call_8351,call_8358,])
output2 = relay.Tuple([call_8352,call_8359,])
func_8375 = relay.Function([], output)
mod['func_8375'] = func_8375
mod = relay.transform.InferType()(mod)
output = func_8375()
func_8376 = relay.Function([], output)
mutated_mod['func_8376'] = func_8376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4210_call = mod.get_global_var('func_4210')
func_4212_call = mutated_mod.get_global_var('func_4212')
call_8384 = relay.TupleGetItem(func_4210_call(), 2)
call_8385 = relay.TupleGetItem(func_4212_call(), 2)
func_2694_call = mod.get_global_var('func_2694')
func_2696_call = mutated_mod.get_global_var('func_2696')
var_8393 = relay.var("var_8393", dtype = "float64", shape = (288,))#candidate|8393|(288,)|var|float64
call_8392 = relay.TupleGetItem(func_2694_call(relay.reshape(var_8393.astype('float64'), [2, 16, 9])), 0)
call_8394 = relay.TupleGetItem(func_2696_call(relay.reshape(var_8393.astype('float64'), [2, 16, 9])), 0)
output = relay.Tuple([call_8384,call_8392,var_8393,])
output2 = relay.Tuple([call_8385,call_8394,var_8393,])
func_8395 = relay.Function([var_8393,], output)
mod['func_8395'] = func_8395
mod = relay.transform.InferType()(mod)
mutated_mod['func_8395'] = func_8395
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8396 = relay.var("var_8396", dtype = "float64", shape = (288,))#candidate|8396|(288,)|var|float64
func_8395_call = mutated_mod.get_global_var('func_8395')
call_8397 = func_8395_call(var_8396)
output = call_8397
func_8398 = relay.Function([var_8396], output)
mutated_mod['func_8398'] = func_8398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8469 = relay.var("var_8469", dtype = "float32", shape = (2, 7, 11))#candidate|8469|(2, 7, 11)|var|float32
uop_8470 = relay.sqrt(var_8469.astype('float32')) # shape=(2, 7, 11)
func_2787_call = mod.get_global_var('func_2787')
func_2790_call = mutated_mod.get_global_var('func_2790')
const_8474 = relay.const([3.800554,-9.712690,-9.414221,8.766820,6.610041,8.422540,2.855987,-5.363050,-4.193650,-6.186272,8.399779,0.364180,0.497758,-4.163688,-8.683372,-0.628329,7.314385,7.111487,-3.974108,-4.753198,1.217094,-3.351851,-8.722016,-6.257773,6.226973,-7.681098,0.377165,4.240196,6.220597,6.349848,7.675126,8.580469,9.417423,-4.922806,3.479163,0.226955,-1.964873,9.462837,-1.165973,-7.735129,-2.313779,0.170507,-3.170025,-7.747447,-6.428443,2.324596,5.457100,-6.882811,9.418173,-2.015978,-4.761353,2.544991,3.225832,1.124110,-1.009037,2.757466,-8.313903,-4.708937,-8.271127,-5.439471,6.367252,-2.484056,-8.789245,0.134862,-9.758063,-1.955460,3.663271,3.218893,-3.524807,9.834899,-9.966783,7.430307,9.129686,3.014720,-8.294509,-7.951184,-0.343185,-4.678734,8.116673,-0.445175,-4.213783,-8.575412,1.326529,-4.140643,-0.827528,-4.311126,6.255076,-9.457542,-0.032426,-6.691776,5.445140,-2.365539,9.094072,4.696208,-1.084344,-4.414838,-9.119517,-9.182776,4.867939,-5.049804,-7.064773,-1.249605,-0.244983,-1.954896,6.047764,-2.474999,0.216351,-7.902496,5.710221,-1.556575,5.140971,-7.791761,3.718978,7.043372,-7.355474,8.936456,7.670459,-2.347396,-5.940101,-5.778993,2.278034,-6.394497,9.103719,7.861094,-4.557275,-6.058506,1.501134,-9.080977,8.522292,0.594752,9.538906,9.092111,-5.342759,-7.585253,-1.954871,-1.041587,9.573935,7.654754,5.922730,-3.283019,-5.549230,-1.266998,0.590319,-5.404834,-0.460824,-5.802019,-2.008386,-2.854909,5.079549,2.330660,0.372783,7.899849,8.458909,9.152330,-8.611763,-6.021174,-2.245757,-1.438932,8.591641,1.186992,-9.181253,1.938896,4.629875,0.923242,8.105156,-3.726355,5.417969,1.884300,-9.444487,2.097030,-4.832721,2.817899,-9.503140,4.147448,4.740594,-8.513728,-4.067121,-7.836769,9.099205,8.503378,7.355579,-4.892225,1.495354,4.481862,-3.331855,-4.824998,-3.173920,-7.111206,9.247396,6.721717,-2.156813,-5.841929,2.011972,-8.304901,0.900334,1.712942,9.268349,5.323439,-0.902680,5.980367,7.813936,5.434730,8.752246,2.861809,6.871528,9.139516,-1.920361,2.697530,3.890705,-3.829287,3.898566,5.843705,7.291062,9.823238,7.132265,0.826773,1.044856,-3.701154,-9.584076,1.205063,-4.104036,9.162585,8.345101,2.371889,-8.621631,0.465932,1.392425,-7.310822,0.970260,-4.231475,-0.368511,1.018466,5.689373,3.256242,0.979146,5.050198,7.158076,-4.581683,3.889196,2.053319,-1.979148,7.663362,4.499693,-3.964928,-9.248314,8.518295,-3.013890,-2.945217,6.214351,8.914562,-1.512083,-0.606962,6.348178,-0.256102,-5.854184,-8.311301,-3.944331,6.305726,-8.201316,-2.917100,-8.618409,5.273083,3.508577,-2.169393,0.312816,5.475921,2.896056,-0.090735,5.513379,1.452666,-3.662226,-8.335044,-1.493538,1.103651,2.434039,5.482891,7.410944,7.299474,-0.139356,8.325773,4.032989,0.078252,8.018694,-5.135447,8.168753,-2.881086,1.104398,-8.941930,-1.765235,-4.450436,-2.721721,-6.605896,1.813054,-2.770336,1.542875,8.521141,-9.659468,7.498258,-9.976875,-6.828968,-4.556224,-5.601185,5.087894,7.412632,-5.853286,-2.402323,6.339098,-3.154522,-6.085723,-2.872282,2.033415,-7.408394,-6.511912,4.643152,2.339549,-5.514020,-5.288928,-6.514210,-8.173331,-2.579628,7.896222,3.158280,1.865237,5.726787,-3.184019,1.323295,-1.586046,1.029083,-2.318818,6.716753,1.478875,4.717172,-4.672853,9.033644,4.301367,8.663626,-5.401525,1.030680,6.257323,1.767651,-4.219957,7.498059,8.425077,1.880295,5.198251,7.517013,2.048827,-8.290863,-7.433500,-6.096036,0.252053,9.800566,-3.536095,8.857907,7.374288,7.958039,-8.312621,-3.085777,2.223020,0.553778,2.207655,1.575837,2.268299,-3.279270,-7.103590,4.264299,0.751554,6.925295,6.118387,1.245092,-7.591312,-6.575526,4.655171,-0.025447,-1.615990,2.480630,-6.604933,-9.771694,-1.369340,-3.553633,7.077914,4.578380,-5.320103,-2.224194,9.319639,-4.579152,-1.036369,-6.707947,-0.445658,9.150699,-0.733350,-7.178352,7.681250,-6.875208,9.251626,-6.965777,-2.151936,9.042221,5.913957,-7.360032,6.965854,-1.273911,0.593794,0.635430,5.188218,9.733181,0.942374,-1.124641,-2.991179,1.874824,5.540815,8.126435,8.981406,-7.904327,-8.265662,4.550829,-9.961693,-5.695389,2.399889,0.175237,-5.069477,-5.441304,-4.351677,-7.511109,-4.867010,-5.776106,-9.935337,8.480377,7.613869,-7.303882,3.064646,1.721594,4.929557,7.433327,-0.798954,4.251447,8.779755,-7.533611,-3.489956,0.169420,-1.994891,8.773882,9.565120,-8.627708,-8.933763,-9.068115,1.259200,0.233798,0.537985,9.203171,1.660827,-0.087102,-2.671904,-4.364972,-5.889878,0.505821,-1.634942,4.829759,-1.567179,-8.766721,-5.951053,-9.392954,-6.838896,-5.245380,-1.516506,9.532689,-2.015538,7.148433,8.697549,6.302309,9.173969,-2.077278,1.149930,7.448590,-8.734867,0.851526,-2.406270,-6.452055,2.872238,5.819490,-0.047022,-1.160520,-7.921820,5.692077,3.483509,4.910537,-7.848833,-3.450103,0.596292,9.877904,3.552741,-0.225818,-6.904176,7.973418,6.337252,9.057508,6.509564,-2.253011,2.545545,8.279737,6.846992,9.212352,3.233612,0.518280,1.307984,-0.774541,8.369459,3.478600,7.361962,-6.407263,4.481001,-3.731492,2.402228,-8.848895,-1.150298,1.544086,6.314456,4.603505,0.523005,9.053297,8.463451,7.355818,4.379865,-4.418730,1.650420,1.141226,8.569948,-7.551159,5.163413,9.234290,-6.637871,2.239177,-4.520509,-3.227897,1.772121,-5.171131,5.684103,-6.484479,-6.978001,0.642844,1.940074,-3.592474,-7.052329,2.860844,-8.374446,-8.474742,8.914999,-3.464655,-3.794367,9.789679,-0.621721,4.117880,-0.743270,-6.722345,-4.365931,-1.022833,8.402408,-2.101111,6.377468,3.984536,2.457291,7.231110,2.496938,-1.370284,-1.046663,5.349628,4.762393], dtype = "float32")#candidate|8474|(567,)|const|float32
call_8473 = relay.TupleGetItem(func_2787_call(relay.reshape(const_8474.astype('float32'), [9, 7, 9]), relay.reshape(const_8474.astype('float32'), [9, 7, 9]), ), 2)
call_8475 = relay.TupleGetItem(func_2790_call(relay.reshape(const_8474.astype('float32'), [9, 7, 9]), relay.reshape(const_8474.astype('float32'), [9, 7, 9]), ), 2)
const_8481 = relay.const([-5.818663,-7.189420,7.833344,3.637194,-7.069486,-3.835764,-7.109421,4.237611,-6.866733,8.251325,-3.976190,2.895854,-7.056831,-5.451695,-7.947640,6.624062,-4.000394,2.681571,2.394674,-1.573765,3.071463,-1.291600,0.997426,-5.566150,-8.809630,-0.026406,7.542005,9.982204,5.290675,-0.629175,-6.282718,-1.981071,-0.352791,-1.384545,-0.828627,6.854763,5.074222,3.544225,-1.878289,6.517563,-6.543882,5.563908,6.458947,3.190206,-5.298502,-0.378580,3.118822,-1.341228,0.228798,-2.296593,7.025420,8.236018,7.003629,9.105068,-5.875637,-2.845989,-1.681353,1.529457,3.317371,-5.914008,-7.938719,-9.900443,9.451797,9.310255,4.401346,0.891511,-9.981978,0.254911,4.427808,4.338228,2.849031,-6.900092,1.696588,8.995713,3.512920,-7.133071,9.605907,3.077812,7.586555,2.325632,-5.174808,3.008914,9.607154,-2.508845,-7.337958,-5.778844,-1.578333,6.184142,-7.734020,-2.191217,3.255089,-9.040885,6.866340,8.093479,-3.029651,7.436468,3.551601,3.498045,6.863284,-0.404646,3.975272,-1.812703,5.666724,5.055174,-1.877449,0.099326,1.706106,-4.537108,-5.801179,1.829159,-1.108018,7.069926,-1.915593,-3.501173,5.878343,9.416458,-7.860983,-5.789342,3.313649,5.443453,8.845438,0.289615,-8.033784,3.320615,-9.806666,-8.283800,2.127140,-2.506019,-9.193805,1.011860,7.350190,2.237083,-6.602246,-5.949919,9.522803,-5.784274,-0.293014,1.875317,5.841187,2.072879,-0.975709,2.870224,-4.880009,0.223159,-8.494354,-6.384360,4.367028,1.472943,2.153531,2.287411,-4.830507,7.706789,-4.799242,1.487517,8.630151,6.551625,-3.135963,6.085473,-5.645416,-9.224541,7.930434,5.095499,-5.621377,9.385891,-1.665068,-4.548311,-7.218659,5.678702,1.752204,-6.564374,-1.111707,-1.829581,-8.899769,7.154803,-2.686239,-0.069748,-1.530844,-4.407186,-2.506958,-5.617665,-7.656515,7.472542,-6.452646,9.083504,-4.395873,-5.994969,4.398740,9.548429,-9.082776,7.622964,-4.675478,-7.709906,3.584153,7.315879,-8.068445,-1.289407,5.671467,1.704516,-0.896637,1.630615,3.518485,9.484158,-0.997187,-0.653793,3.975877,5.897852,2.334291,-4.365195,-8.977125,9.140128,5.073913,9.574105,8.646102,-3.051235,-7.610680,-8.363827,1.986062,-7.940974,1.187419,-8.388271,-5.909142,-7.334948,-6.610099,-0.112416,4.146940,1.675457,6.489385,9.835929,-5.670166,1.824387,9.578736,-9.745173,5.440014,-3.977554,7.532767,-3.287799,-1.411675,-0.684265,2.616821,8.599989,-2.075289,-6.483150,7.720085,-6.788335,8.163385,-6.595646,-5.719907,-6.737096,-9.212054,-3.266622,0.836665,4.779340,9.651925,-3.336910,8.470340,9.391203,2.093115,0.320676,9.991254,-2.791631,4.770754,3.769113,0.709025,-0.674062,-7.876750,9.738078,6.742594,6.701076,-9.946570,2.732540,0.714934,8.206106,-8.220311,-2.651200,7.290405,9.596408,1.556583,-9.738606,-5.493854,-1.340004,8.233232,-9.060984,8.275833,8.368273,-9.015577,9.377514,-0.736882,-7.457331,7.021935,-5.254656,3.615007,-7.395459,5.276327,2.220955,8.270632,-2.606594,1.578964,6.370261,6.098338,9.283942,6.895186,0.575203,9.822235,7.243582,-3.766757,8.195685,6.450284,0.125150,-9.076646,-2.905878,-0.209864,-8.890262,8.853878,-3.529531,7.357635,-4.605910,-4.523999,-6.547556,4.522465,4.697722,0.484390,0.918153,-2.165303,9.848180,6.417953,-9.670806,0.504122,-1.578646,-4.976269,2.913126,-0.722076,-0.229524,1.639647,-7.480034,-1.898366,7.522566,7.391581,-7.817721,4.028247,-4.872689,0.187583,-7.389772,-3.046529,-9.228605,-8.321752,-7.664578,5.559779,2.066163,0.148077,-9.357013,8.715838,9.530784,-9.253762,-9.751530,-6.188791,3.078772,4.919949,-8.999222,-3.875049,-7.489438,-6.894340,2.132320,-0.083923,-5.759000,-0.918637,3.139189,-6.748288,-7.100658,2.846910,-0.681328,-4.743966,3.394515,-4.107215,0.277132,-0.542656,0.401957,-5.895927,0.775668,5.560995,-2.058541,-1.014548,-4.242900,-9.973964,4.833640,4.849733,7.552207,7.123508,-2.107601,-1.329413,-0.584010,5.949665,9.686107,-6.958818,-9.671085,3.324510,-8.068176,5.322605,-5.594805,4.815541,6.250886,-0.912820,-8.491550,5.764314,7.566543,-0.201564,4.264817,6.039473,1.798467,1.085322,1.367654,-4.987373,-0.356145,-6.049093,-0.681092,-1.064452,2.079668,-0.782380,6.597358,-2.104028,-6.621723,-5.916367,-4.636811,-8.912358,-3.320831,-2.474276,-4.941406,1.798800,-3.449427,-0.399904,5.246094,-2.969193,2.435107,2.950961,-8.074617,7.402375,-0.761717,-9.821640,5.224004,2.589598,-7.668400,9.264501,-3.000093,6.618699,2.895106,7.322073,4.863030,2.836731,8.737584,2.137236,-9.081085,-2.679854,-3.737701,0.336861,2.178000,8.827954,-6.576170,4.917852,8.113954,9.640360,-5.849194,-2.304076,-7.425376,-0.373332,-9.117200,-0.625494,-2.401857,1.370661,0.820296,-8.821124,7.146275,0.053147,-7.495123,8.173396,9.495043,-3.396644,8.207352,4.807434,-5.407634,2.307358,0.072937,5.202373,-5.213034,8.100006,-3.300402,1.444661,9.637577,2.803300,3.945459,-4.642312,-7.873521,-4.232942,6.275911,4.804703,6.793684,-0.432666,-8.264035,-2.613205,-7.175975,0.366608,9.983314,1.514800,4.150316,-8.010323,8.029760,6.589320,-1.944503,4.485346,-7.670735,4.684912,-0.623599,-5.379051,-4.116462,5.935567,-2.579195,2.767080,2.533612,1.948991,8.676947,8.958246,-4.676956,-2.821386,-4.987710,-9.367660,4.286955,-4.371116,9.876329,-9.750294,9.940896,-0.858367,-4.512174,3.270848,-3.630143,-2.202625,6.015705,-7.225166,4.569771,-4.240096,2.437977,-7.219483,-2.253474,-2.643032,4.285533,0.241038,-9.879942,6.846436,8.225562,7.135938,8.241401,-0.618712,5.889152,-0.260335,4.919511,4.021673,9.629061,7.845947,-7.448533,2.897086,1.292334,3.498293,-3.947382,-4.148005,8.824080,-3.014614,-5.963448,2.697215,9.557308,-5.835497], dtype = "float32")#candidate|8481|(567,)|const|float32
bop_8482 = relay.subtract(const_8474.astype('uint64'), relay.reshape(const_8481.astype('uint64'), relay.shape_of(const_8474))) # shape=(567,)
output = relay.Tuple([uop_8470,call_8473,bop_8482,])
output2 = relay.Tuple([uop_8470,call_8475,bop_8482,])
func_8491 = relay.Function([var_8469,], output)
mod['func_8491'] = func_8491
mod = relay.transform.InferType()(mod)
var_8492 = relay.var("var_8492", dtype = "float32", shape = (2, 7, 11))#candidate|8492|(2, 7, 11)|var|float32
output = func_8491(var_8492)
func_8493 = relay.Function([var_8492], output)
mutated_mod['func_8493'] = func_8493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3541_call = mod.get_global_var('func_3541')
func_3542_call = mutated_mod.get_global_var('func_3542')
call_8517 = func_3541_call()
call_8518 = func_3541_call()
output = relay.Tuple([call_8517,])
output2 = relay.Tuple([call_8518,])
func_8520 = relay.Function([], output)
mod['func_8520'] = func_8520
mod = relay.transform.InferType()(mod)
mutated_mod['func_8520'] = func_8520
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8520_call = mutated_mod.get_global_var('func_8520')
call_8521 = func_8520_call()
output = call_8521
func_8522 = relay.Function([], output)
mutated_mod['func_8522'] = func_8522
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8527 = relay.var("var_8527", dtype = "int64", shape = (5, 12, 8))#candidate|8527|(5, 12, 8)|var|int64
const_8528 = relay.const([[[-3,-1,10,-10,1,-7,3,8],[-2,2,-2,-1,-10,2,-3,1],[-5,8,4,-6,-1,-1,-9,-2],[10,10,-7,-4,-3,9,7,1],[4,9,-7,-10,6,-3,-10,7],[6,-1,8,10,-4,-9,-10,-2],[10,-2,-4,5,4,6,2,-6],[-3,-3,-4,4,3,8,-4,8],[2,2,2,10,5,4,1,8],[-8,-5,-8,-2,-4,4,3,-3],[4,2,3,4,8,-7,-9,-1],[10,1,6,-8,-6,-8,6,3]],[[-9,8,5,-9,-9,1,5,-6],[9,10,-1,-6,3,-5,7,1],[-2,-5,-10,-1,-5,8,6,3],[-1,3,-3,10,-4,5,2,-5],[-2,1,-9,2,5,-3,3,-10],[-3,8,-3,2,-3,1,2,10],[-10,-7,-5,2,10,-3,-3,7],[6,-2,4,-8,-2,2,7,-1],[5,4,8,10,-3,-8,5,-2],[1,-2,1,-1,9,8,-7,2],[8,2,4,-1,4,-3,9,10],[1,-4,-1,5,8,7,4,-7]],[[-5,-6,10,4,-1,1,-4,9],[-4,-8,-7,7,8,-3,5,-5],[-1,-9,-10,-3,2,10,-8,1],[-1,-6,-4,8,-1,6,-2,-6],[10,2,-8,1,-10,8,-2,-7],[-10,3,-8,-7,9,4,-2,2],[6,4,-8,6,7,-5,4,2],[-7,-9,-4,-5,-10,6,-9,-6],[4,-1,-6,-2,2,4,1,10],[-10,2,-5,-9,-6,-9,-7,2],[-6,6,1,-6,7,-6,5,4],[-5,9,5,-9,7,10,4,5]],[[-4,-5,-1,7,-3,6,-9,3],[-1,7,4,-9,-3,-5,10,10],[-5,10,-8,-5,9,8,6,-3],[-6,2,-6,3,9,-10,-9,6],[7,-9,-2,3,6,9,-3,-8],[5,-10,-1,4,-10,3,-7,3],[-5,-7,7,-8,3,4,10,-4],[-1,7,5,6,-8,-5,5,10],[-10,-7,-9,9,-2,6,4,8],[4,9,-1,-7,3,-5,-1,10],[-2,-6,2,10,8,-6,8,8],[-1,5,4,-10,-5,-5,10,6]],[[2,2,7,8,10,8,9,-3],[-6,4,-2,7,1,-4,9,2],[3,-7,-8,8,10,7,5,-10],[8,-1,10,8,1,-4,-3,4],[-2,10,6,7,5,5,-4,3],[1,-4,5,4,-5,8,5,-8],[3,-7,6,-6,8,5,8,-5],[5,10,3,-5,2,-8,5,8],[-4,8,-8,4,-8,9,-8,-3],[-4,-10,8,-5,9,1,-9,-2],[3,6,-6,7,-9,8,-1,-10],[-7,-9,-6,-7,-8,-10,7,-4]]], dtype = "int64")#candidate|8528|(5, 12, 8)|const|int64
bop_8529 = relay.bitwise_or(var_8527.astype('int64'), relay.reshape(const_8528.astype('int64'), relay.shape_of(var_8527))) # shape=(5, 12, 8)
output = bop_8529
output2 = bop_8529
func_8534 = relay.Function([var_8527,], output)
mod['func_8534'] = func_8534
mod = relay.transform.InferType()(mod)
mutated_mod['func_8534'] = func_8534
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8535 = relay.var("var_8535", dtype = "int64", shape = (5, 12, 8))#candidate|8535|(5, 12, 8)|var|int64
func_8534_call = mutated_mod.get_global_var('func_8534')
call_8536 = func_8534_call(var_8535)
output = call_8536
func_8537 = relay.Function([var_8535], output)
mutated_mod['func_8537'] = func_8537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4087_call = mod.get_global_var('func_4087')
func_4089_call = mutated_mod.get_global_var('func_4089')
call_8550 = relay.TupleGetItem(func_4087_call(), 0)
call_8551 = relay.TupleGetItem(func_4089_call(), 0)
func_1600_call = mod.get_global_var('func_1600')
func_1602_call = mutated_mod.get_global_var('func_1602')
call_8573 = relay.TupleGetItem(func_1600_call(), 0)
call_8574 = relay.TupleGetItem(func_1602_call(), 0)
func_6703_call = mod.get_global_var('func_6703')
func_6705_call = mutated_mod.get_global_var('func_6705')
var_8582 = relay.var("var_8582", dtype = "uint32", shape = (1274,))#candidate|8582|(1274,)|var|uint32
call_8581 = func_6703_call(relay.reshape(var_8582.astype('uint32'), [13, 14, 7]))
call_8583 = func_6703_call(relay.reshape(var_8582.astype('uint32'), [13, 14, 7]))
func_8118_call = mod.get_global_var('func_8118')
func_8119_call = mutated_mod.get_global_var('func_8119')
call_8588 = relay.TupleGetItem(func_8118_call(), 0)
call_8589 = relay.TupleGetItem(func_8119_call(), 0)
func_8313_call = mod.get_global_var('func_8313')
func_8315_call = mutated_mod.get_global_var('func_8315')
call_8592 = relay.TupleGetItem(func_8313_call(), 0)
call_8593 = relay.TupleGetItem(func_8315_call(), 0)
func_7023_call = mod.get_global_var('func_7023')
func_7025_call = mutated_mod.get_global_var('func_7025')
call_8600 = func_7023_call()
call_8601 = func_7023_call()
func_7651_call = mod.get_global_var('func_7651')
func_7652_call = mutated_mod.get_global_var('func_7652')
call_8603 = func_7651_call()
call_8604 = func_7651_call()
output = relay.Tuple([call_8550,call_8573,call_8581,var_8582,call_8588,call_8592,call_8600,call_8603,])
output2 = relay.Tuple([call_8551,call_8574,call_8583,var_8582,call_8589,call_8593,call_8601,call_8604,])
func_8620 = relay.Function([var_8582,], output)
mod['func_8620'] = func_8620
mod = relay.transform.InferType()(mod)
mutated_mod['func_8620'] = func_8620
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8621 = relay.var("var_8621", dtype = "uint32", shape = (1274,))#candidate|8621|(1274,)|var|uint32
func_8620_call = mutated_mod.get_global_var('func_8620')
call_8622 = func_8620_call(var_8621)
output = call_8622
func_8623 = relay.Function([var_8621], output)
mutated_mod['func_8623'] = func_8623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5258_call = mod.get_global_var('func_5258')
func_5260_call = mutated_mod.get_global_var('func_5260')
call_8671 = relay.TupleGetItem(func_5258_call(), 0)
call_8672 = relay.TupleGetItem(func_5260_call(), 0)
func_2927_call = mod.get_global_var('func_2927')
func_2929_call = mutated_mod.get_global_var('func_2929')
call_8687 = relay.TupleGetItem(func_2927_call(), 0)
call_8688 = relay.TupleGetItem(func_2929_call(), 0)
output = relay.Tuple([call_8671,call_8687,])
output2 = relay.Tuple([call_8672,call_8688,])
func_8692 = relay.Function([], output)
mod['func_8692'] = func_8692
mod = relay.transform.InferType()(mod)
output = func_8692()
func_8693 = relay.Function([], output)
mutated_mod['func_8693'] = func_8693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_653_call = mod.get_global_var('func_653')
func_654_call = mutated_mod.get_global_var('func_654')
call_8711 = relay.TupleGetItem(func_653_call(), 0)
call_8712 = relay.TupleGetItem(func_654_call(), 0)
output = call_8711
output2 = call_8712
func_8718 = relay.Function([], output)
mod['func_8718'] = func_8718
mod = relay.transform.InferType()(mod)
mutated_mod['func_8718'] = func_8718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8718_call = mutated_mod.get_global_var('func_8718')
call_8719 = func_8718_call()
output = call_8719
func_8720 = relay.Function([], output)
mutated_mod['func_8720'] = func_8720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8024_call = mod.get_global_var('func_8024')
func_8025_call = mutated_mod.get_global_var('func_8025')
call_8732 = relay.TupleGetItem(func_8024_call(), 0)
call_8733 = relay.TupleGetItem(func_8025_call(), 0)
output = call_8732
output2 = call_8733
func_8734 = relay.Function([], output)
mod['func_8734'] = func_8734
mod = relay.transform.InferType()(mod)
output = func_8734()
func_8735 = relay.Function([], output)
mutated_mod['func_8735'] = func_8735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6763_call = mod.get_global_var('func_6763')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_8751 = relay.TupleGetItem(func_6763_call(), 0)
call_8752 = relay.TupleGetItem(func_6764_call(), 0)
output = relay.Tuple([call_8751,])
output2 = relay.Tuple([call_8752,])
func_8761 = relay.Function([], output)
mod['func_8761'] = func_8761
mod = relay.transform.InferType()(mod)
mutated_mod['func_8761'] = func_8761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8761_call = mutated_mod.get_global_var('func_8761')
call_8762 = func_8761_call()
output = call_8762
func_8763 = relay.Function([], output)
mutated_mod['func_8763'] = func_8763
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_8770 = relay.TupleGetItem(func_3004_call(), 0)
call_8771 = relay.TupleGetItem(func_3006_call(), 0)
output = call_8770
output2 = call_8771
func_8773 = relay.Function([], output)
mod['func_8773'] = func_8773
mod = relay.transform.InferType()(mod)
mutated_mod['func_8773'] = func_8773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8773_call = mutated_mod.get_global_var('func_8773')
call_8774 = func_8773_call()
output = call_8774
func_8775 = relay.Function([], output)
mutated_mod['func_8775'] = func_8775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2813_call = mod.get_global_var('func_2813')
func_2814_call = mutated_mod.get_global_var('func_2814')
call_8791 = func_2813_call()
call_8792 = func_2813_call()
func_7651_call = mod.get_global_var('func_7651')
func_7652_call = mutated_mod.get_global_var('func_7652')
call_8814 = func_7651_call()
call_8815 = func_7651_call()
func_4835_call = mod.get_global_var('func_4835')
func_4838_call = mutated_mod.get_global_var('func_4838')
var_8821 = relay.var("var_8821", dtype = "int32", shape = (108,))#candidate|8821|(108,)|var|int32
call_8820 = relay.TupleGetItem(func_4835_call(relay.reshape(var_8821.astype('int32'), [108,])), 3)
call_8822 = relay.TupleGetItem(func_4838_call(relay.reshape(var_8821.astype('int32'), [108,])), 3)
output = relay.Tuple([call_8791,call_8814,call_8820,var_8821,])
output2 = relay.Tuple([call_8792,call_8815,call_8822,var_8821,])
func_8823 = relay.Function([var_8821,], output)
mod['func_8823'] = func_8823
mod = relay.transform.InferType()(mod)
mutated_mod['func_8823'] = func_8823
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8824 = relay.var("var_8824", dtype = "int32", shape = (108,))#candidate|8824|(108,)|var|int32
func_8823_call = mutated_mod.get_global_var('func_8823')
call_8825 = func_8823_call(var_8824)
output = call_8825
func_8826 = relay.Function([var_8824], output)
mutated_mod['func_8826'] = func_8826
mutated_mod = relay.transform.InferType()(mutated_mod)
func_402_call = mod.get_global_var('func_402')
func_404_call = mutated_mod.get_global_var('func_404')
call_8850 = relay.TupleGetItem(func_402_call(), 2)
call_8851 = relay.TupleGetItem(func_404_call(), 2)
output = call_8850
output2 = call_8851
func_8855 = relay.Function([], output)
mod['func_8855'] = func_8855
mod = relay.transform.InferType()(mod)
mutated_mod['func_8855'] = func_8855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8855_call = mutated_mod.get_global_var('func_8855')
call_8856 = func_8855_call()
output = call_8856
func_8857 = relay.Function([], output)
mutated_mod['func_8857'] = func_8857
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6134_call = mod.get_global_var('func_6134')
func_6136_call = mutated_mod.get_global_var('func_6136')
call_8907 = func_6134_call()
call_8908 = func_6134_call()
output = call_8907
output2 = call_8908
func_8912 = relay.Function([], output)
mod['func_8912'] = func_8912
mod = relay.transform.InferType()(mod)
output = func_8912()
func_8913 = relay.Function([], output)
mutated_mod['func_8913'] = func_8913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5826_call = mod.get_global_var('func_5826')
func_5828_call = mutated_mod.get_global_var('func_5828')
call_8961 = relay.TupleGetItem(func_5826_call(), 0)
call_8962 = relay.TupleGetItem(func_5828_call(), 0)
uop_8987 = relay.acosh(call_8961.astype('float64')) # shape=(2, 16, 9)
uop_8989 = relay.acosh(call_8962.astype('float64')) # shape=(2, 16, 9)
output = uop_8987
output2 = uop_8989
func_8995 = relay.Function([], output)
mod['func_8995'] = func_8995
mod = relay.transform.InferType()(mod)
mutated_mod['func_8995'] = func_8995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8995_call = mutated_mod.get_global_var('func_8995')
call_8996 = func_8995_call()
output = call_8996
func_8997 = relay.Function([], output)
mutated_mod['func_8997'] = func_8997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1733_call = mod.get_global_var('func_1733')
func_1735_call = mutated_mod.get_global_var('func_1735')
call_9013 = relay.TupleGetItem(func_1733_call(), 0)
call_9014 = relay.TupleGetItem(func_1735_call(), 0)
output = call_9013
output2 = call_9014
func_9029 = relay.Function([], output)
mod['func_9029'] = func_9029
mod = relay.transform.InferType()(mod)
output = func_9029()
func_9030 = relay.Function([], output)
mutated_mod['func_9030'] = func_9030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9050 = relay.var("var_9050", dtype = "uint32", shape = ())#candidate|9050|()|var|uint32
var_9051 = relay.var("var_9051", dtype = "uint32", shape = (13, 9, 14))#candidate|9051|(13, 9, 14)|var|uint32
bop_9052 = relay.bitwise_and(var_9050.astype('uint32'), var_9051.astype('uint32')) # shape=(13, 9, 14)
output = bop_9052
output2 = bop_9052
func_9055 = relay.Function([var_9050,var_9051,], output)
mod['func_9055'] = func_9055
mod = relay.transform.InferType()(mod)
mutated_mod['func_9055'] = func_9055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9055_call = mutated_mod.get_global_var('func_9055')
var_9057 = relay.var("var_9057", dtype = "uint32", shape = ())#candidate|9057|()|var|uint32
var_9058 = relay.var("var_9058", dtype = "uint32", shape = (13, 9, 14))#candidate|9058|(13, 9, 14)|var|uint32
call_9056 = func_9055_call(var_9057,var_9058,)
output = call_9056
func_9059 = relay.Function([var_9057,var_9058,], output)
mutated_mod['func_9059'] = func_9059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6763_call = mod.get_global_var('func_6763')
func_6764_call = mutated_mod.get_global_var('func_6764')
call_9100 = relay.TupleGetItem(func_6763_call(), 0)
call_9101 = relay.TupleGetItem(func_6764_call(), 0)
output = call_9100
output2 = call_9101
func_9115 = relay.Function([], output)
mod['func_9115'] = func_9115
mod = relay.transform.InferType()(mod)
output = func_9115()
func_9116 = relay.Function([], output)
mutated_mod['func_9116'] = func_9116
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9148 = relay.var("var_9148", dtype = "uint8", shape = (4, 1, 9))#candidate|9148|(4, 1, 9)|var|uint8
var_9149 = relay.var("var_9149", dtype = "uint8", shape = (4, 2, 9))#candidate|9149|(4, 2, 9)|var|uint8
bop_9150 = relay.multiply(var_9148.astype('uint8'), var_9149.astype('uint8')) # shape=(4, 2, 9)
func_5318_call = mod.get_global_var('func_5318')
func_5320_call = mutated_mod.get_global_var('func_5320')
call_9165 = func_5318_call()
call_9166 = func_5318_call()
output = relay.Tuple([bop_9150,call_9165,])
output2 = relay.Tuple([bop_9150,call_9166,])
func_9170 = relay.Function([var_9148,var_9149,], output)
mod['func_9170'] = func_9170
mod = relay.transform.InferType()(mod)
mutated_mod['func_9170'] = func_9170
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9170_call = mutated_mod.get_global_var('func_9170')
var_9172 = relay.var("var_9172", dtype = "uint8", shape = (4, 1, 9))#candidate|9172|(4, 1, 9)|var|uint8
var_9173 = relay.var("var_9173", dtype = "uint8", shape = (4, 2, 9))#candidate|9173|(4, 2, 9)|var|uint8
call_9171 = func_9170_call(var_9172,var_9173,)
output = call_9171
func_9174 = relay.Function([var_9172,var_9173,], output)
mutated_mod['func_9174'] = func_9174
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2426_call = mod.get_global_var('func_2426')
func_2428_call = mutated_mod.get_global_var('func_2428')
call_9186 = relay.TupleGetItem(func_2426_call(), 0)
call_9187 = relay.TupleGetItem(func_2428_call(), 0)
output = call_9186
output2 = call_9187
func_9201 = relay.Function([], output)
mod['func_9201'] = func_9201
mod = relay.transform.InferType()(mod)
output = func_9201()
func_9202 = relay.Function([], output)
mutated_mod['func_9202'] = func_9202
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9236 = relay.var("var_9236", dtype = "float32", shape = ())#candidate|9236|()|var|float32
const_9237 = relay.const([[[5.440368,-8.133559,-0.087626,8.812483,-1.094683,4.689454,-3.997982,-0.848229,3.507327,6.750471,-4.759533,-1.155381],[2.847196,0.123739,0.189854,-1.909930,2.392092,-1.093399,-3.021480,2.649300,-7.199643,1.786179,-1.385420,-0.875709],[5.045699,1.226027,4.300674,0.781518,2.915727,-0.277478,8.748529,4.582370,2.345165,3.500339,5.843948,-6.756159],[6.608864,9.768626,-5.746229,-5.819824,8.170912,0.408301,3.501153,-3.144703,3.105829,5.122978,0.901644,-5.330657],[5.902480,-1.626888,-0.228142,-2.832044,-6.229942,-1.697554,8.062338,2.857932,-5.769338,2.318791,9.647124,-3.093707]],[[7.526992,4.486726,-6.242943,6.625326,8.636556,-2.543084,7.885902,-0.182656,-9.993625,-5.899216,1.565118,9.386726],[-4.274234,1.107103,-4.853256,-8.328543,-8.576313,-8.459769,5.264819,-3.466895,-4.693953,4.546065,6.043950,4.627640],[-5.807002,-9.517433,8.150199,2.817853,-6.393564,6.141560,-4.111619,-8.787239,-9.697025,3.939579,9.778072,-5.592239],[-1.734539,5.082057,4.120613,-9.108083,-2.486540,0.438783,-7.265416,1.645556,-0.238203,5.418800,-6.222901,7.267591],[-6.623212,6.860769,-6.227173,2.755112,6.180960,-8.081016,-2.964991,-5.157726,7.499184,-1.403959,-3.902111,9.326008]],[[3.131064,5.903458,-3.158000,-2.683809,0.685783,-2.635723,8.371909,-0.888030,-5.221152,-7.835006,8.417363,8.966302],[-0.195995,-4.102337,6.904520,9.164061,-3.512979,0.542166,2.733132,-5.303591,4.379430,-1.154448,-1.618288,2.913896],[-5.500793,8.330634,-2.028151,-6.004216,7.075056,9.090130,-3.816775,8.439693,2.494298,-8.172879,-4.920783,1.033574],[2.143750,-4.434704,-8.529009,6.495074,9.963825,1.623213,5.121830,9.370184,-2.083563,-8.580194,8.418737,-9.713113],[-1.394775,-3.249982,8.468279,-9.089445,7.075236,-2.399297,-2.197571,-3.754460,8.845385,5.961167,-3.209063,3.991456]],[[5.022858,2.513768,3.916793,9.463581,-3.940727,-0.950287,1.928591,0.428214,7.277471,-0.334125,0.997151,-0.595843],[-3.793624,2.165546,-7.517870,-5.369289,-7.704646,-8.964415,0.186933,7.875140,6.666457,0.315842,-9.052601,-1.454517],[-0.354809,3.675212,7.492215,-6.836930,1.107712,-1.135651,-4.080693,7.371400,1.753914,-5.231537,8.535160,-2.147713],[1.857550,6.829416,-2.027426,-7.096869,8.694564,-0.155763,3.421564,-5.099134,7.773933,-9.576704,2.823649,-4.665196],[6.349969,4.492842,8.986196,-5.947995,5.835707,-1.535473,7.475124,1.717650,2.539609,0.073787,-5.430672,9.725737]],[[2.699325,-5.629122,-1.841658,8.921815,7.028646,-0.556523,-0.228447,-3.841930,1.770035,-2.879905,3.274571,6.650355],[8.356373,4.034599,-7.141848,5.815577,-2.319355,5.380396,6.110710,-8.784189,9.238145,2.109555,8.297702,-8.109150],[-8.212206,4.716885,-1.395430,-8.199690,-3.405325,0.786852,0.317908,-0.451461,-0.673741,-5.145101,-8.725552,1.124727],[0.334014,9.381237,-8.936496,9.470262,-8.253026,-3.243878,3.791545,7.582207,-8.203131,1.422353,9.214078,0.771811],[5.825931,6.668419,-3.983081,2.236559,8.980899,1.567917,-6.827565,7.962456,6.094369,9.182330,-4.960418,-5.568162]],[[-5.449933,-3.335686,5.729307,9.318263,1.247709,-4.208852,9.631201,-0.867857,4.704341,-5.416212,-6.818450,-9.167248],[6.712896,6.544225,-6.716519,-6.951397,7.160743,0.500199,-9.392392,1.841843,2.936310,-6.418403,8.973042,-2.454645],[-8.944029,3.767109,-0.001088,-6.769825,6.882061,8.782353,-8.997380,-7.946440,5.607019,-5.730354,0.112803,3.264324],[-7.615537,7.485485,-3.799427,-8.619602,5.344050,-9.263623,4.635221,3.602687,-7.937550,1.616203,3.870853,-1.160220],[5.638756,-1.568484,-9.140690,0.830547,6.899864,-9.541555,-1.203914,-7.453268,-9.417550,0.157177,-1.151684,3.220819]],[[-3.233538,7.345507,-5.434938,-0.980757,-8.184373,-5.807063,-2.029076,3.260544,6.438309,-1.409143,-1.556296,1.423449],[3.313031,4.568862,2.933899,-0.292138,1.526063,4.592356,3.704203,5.513703,0.521915,-7.475754,8.242285,3.822494],[9.691160,0.012139,0.864834,3.696965,5.696990,-6.262615,9.967590,-1.010897,-6.377603,-5.842281,6.053117,9.952478],[-1.674621,6.325645,-5.597830,-4.865356,-1.064630,7.573500,-3.476950,-8.073303,6.113087,-2.068241,8.507530,7.775709],[6.541384,8.828373,0.586567,5.209662,-3.757890,-1.449383,7.517378,-9.356482,-0.613878,1.897635,-1.154975,-8.586282]],[[-7.753926,-9.657628,-3.873897,0.947846,-6.808525,-7.608795,-5.491149,3.641438,-2.227154,3.916642,-6.166417,2.965843],[9.778089,5.114340,-5.978353,-9.290565,-6.932071,-1.162426,-9.039323,-5.863173,-5.411565,3.463311,-5.450002,1.561098],[-3.070198,3.776808,3.336097,1.079998,1.306499,-7.983509,-2.421999,3.461985,-5.686970,9.080627,3.440442,8.811756],[1.272899,-2.324360,8.139630,-8.586691,-0.695812,-8.347019,2.808332,4.603774,-8.558559,-9.098776,-1.809492,8.563850],[-1.626075,2.398106,8.053632,4.859130,9.101634,-8.915901,-7.983047,-2.249825,-6.542375,-3.271118,-1.979057,5.290997]],[[2.804701,-8.982502,7.660183,-8.133376,-0.047553,0.537706,-7.570854,-4.656493,4.577962,-5.536880,-5.531766,-6.260665],[3.454981,-8.258668,-3.446132,-2.774304,1.330765,3.787867,0.246800,-5.147267,-1.584753,3.170669,1.504681,-4.567192],[-3.852360,-6.720277,-7.510048,-0.347051,1.818244,6.875698,-3.273105,6.208069,-8.292375,-7.702328,7.692811,-9.649991],[-0.022270,-3.554102,7.304799,-3.410428,-3.175846,-8.817579,-8.703937,-2.161749,4.184263,4.138219,-3.050246,-3.703460],[-6.069827,-3.772184,9.154551,8.653612,-8.835143,7.186016,-2.070116,8.228658,-0.215789,7.610131,-0.634646,-4.471192]],[[-0.236857,5.920908,5.700991,9.927571,-1.436779,3.871393,-6.249174,-0.232644,-2.653328,5.599628,8.384632,6.884982],[-1.381051,-5.375104,6.226859,8.834873,5.676981,-3.547459,-5.151938,-9.887234,1.505631,-7.341390,-7.752649,-0.248198],[2.183837,8.617162,-3.909009,-5.941837,-4.785951,-4.810604,-9.163090,9.588678,-4.615935,-4.434228,1.581479,-5.611186],[-2.718422,1.130169,8.135366,6.324329,7.164388,6.043466,-2.983099,-5.387963,1.087455,-2.804630,-0.927042,5.836195],[3.574208,2.410006,-0.054115,9.343447,4.818281,3.686347,-0.106289,5.082341,4.376626,4.165000,-8.904989,-4.558919]],[[-9.467476,3.505354,-6.755260,-4.696596,-1.968263,4.834467,4.812555,5.209170,2.873364,6.413247,-7.797616,5.452906],[3.850523,7.038554,-3.666230,9.662063,-4.608808,-0.891033,3.688560,-3.926904,-3.920988,-2.327882,-7.928634,-0.853212],[-9.713168,5.032253,-6.243407,5.163160,8.363415,-6.952346,-5.141218,6.984217,-3.787216,-5.271037,-7.240489,-3.026224],[-4.266506,-3.891104,-1.734431,-7.454528,-4.048292,7.390620,-0.263249,-1.397269,2.874621,4.863737,0.768410,-1.561028],[-4.799354,4.278617,9.041039,-3.659194,8.389274,-0.059462,6.504125,-7.771534,-8.685034,9.825449,-2.603647,4.865709]],[[-6.734864,-0.418210,6.420084,3.736033,7.819934,-3.520402,-2.327517,-3.096480,9.178158,-2.409769,4.086343,-9.323688],[-8.992069,-1.265423,0.229636,8.865916,-7.231758,2.331338,-1.829441,-6.283539,-7.447567,6.873151,2.607467,-6.784660],[-1.914672,4.613835,3.336088,-8.317231,0.552279,4.893621,-8.161971,-2.298109,-5.500967,-3.113532,2.579113,-3.984989],[2.428220,-3.903901,1.847746,6.764324,6.031514,1.098539,-3.697786,1.791184,-5.644653,-4.965220,7.199937,9.458380],[5.744258,-1.867990,-4.779532,-9.609897,-6.097757,-0.119484,1.766556,-7.033686,8.551916,6.119186,5.872119,9.492144]],[[7.033180,-7.283303,3.861530,-3.448711,3.486332,8.489033,9.283924,1.289202,-2.691614,9.371109,4.903873,2.069759],[2.378036,-5.309303,5.069703,-0.895860,9.538531,9.886589,7.033314,8.402383,-1.042707,-9.405389,-0.406606,-5.822050],[-5.175163,-1.860510,0.182702,-8.269572,2.660957,8.044485,-4.853264,2.109859,-1.805251,-6.664773,2.284274,-8.991625],[-0.304563,5.676202,-1.170115,-0.568490,-2.652314,-9.298169,-6.611781,-1.385597,4.660887,-0.860620,-1.968200,6.713382],[-9.441545,-9.265724,-1.883647,5.685522,0.896097,4.252309,-7.497747,-8.316711,4.720032,-6.457682,8.501963,9.178476]],[[-7.359763,5.298642,3.915628,1.946691,-1.186837,1.981682,-8.430875,-6.538441,-7.772989,3.527923,5.611426,6.500199],[-2.695548,-7.107266,-0.195540,-9.719970,9.952872,1.691547,2.301576,-8.240058,-4.501355,-4.473984,-5.801093,6.264687],[-8.177969,-3.874077,-8.052850,-7.534087,7.515328,8.642638,-0.213608,4.621497,7.489333,4.250734,6.142742,-0.529979],[3.539106,3.143421,3.560748,-4.110502,7.628052,6.832145,-2.357808,6.945573,-8.745544,-9.952422,-9.006419,-0.319272],[-9.221590,-0.550841,9.147763,-5.886740,9.808283,6.843236,-7.996649,9.335477,-9.900868,1.763470,-5.345549,-3.477296]],[[0.805744,-1.566390,-8.498044,2.244832,-7.827733,6.098862,4.991870,-5.245290,6.069208,7.617191,-1.092297,4.113295],[-4.775683,5.721000,6.653265,6.658770,-8.571329,8.396771,0.141630,-3.682673,-6.549757,4.240420,1.475618,0.239650],[1.629927,-1.446312,1.470175,-1.295522,-7.068420,-6.599127,-2.301535,0.881885,9.513773,5.537260,4.904511,-4.263490],[3.397693,3.987037,-2.053662,5.278037,-3.887074,1.997619,-5.093036,6.688911,1.474517,-4.917280,3.393055,2.444998],[-5.293976,4.103030,-1.706532,-6.408494,-7.046405,-3.691171,-2.252836,-5.230408,6.246285,-6.690933,-5.138114,-8.167243]],[[7.122289,8.805687,-5.557302,-0.681093,9.391273,4.228344,3.322373,-7.310613,2.655481,-3.045051,-8.614280,-8.815410],[-9.479891,0.462204,-4.648309,7.197948,0.955331,4.301383,0.425859,-0.059924,9.533202,-6.792162,9.401975,-9.369472],[0.073113,-7.603171,-4.610146,7.858882,8.168311,4.532017,-8.452777,-5.102468,2.221857,-7.910309,7.124543,5.873700],[-0.341737,8.603176,-5.601773,-3.287786,3.163967,-1.453667,-1.115812,-1.403848,-6.186429,6.265057,-2.675659,-4.435945],[9.980905,-8.647016,-3.319583,-0.802205,4.999105,-8.398552,8.951455,0.427290,-5.541348,-4.849042,2.132013,-1.084178]]], dtype = "float32")#candidate|9237|(16, 5, 12)|const|float32
bop_9238 = relay.divide(var_9236.astype('float32'), const_9237.astype('float32')) # shape=(16, 5, 12)
output = bop_9238
output2 = bop_9238
F = relay.Function([var_9236,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9236,], output2)
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
