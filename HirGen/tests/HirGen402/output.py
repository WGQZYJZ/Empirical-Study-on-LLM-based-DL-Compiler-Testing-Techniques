import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_188 = relay.var("var_188", dtype = "uint16", shape = (1, 2, 12))#candidate|188|(1, 2, 12)|var|uint16
var_189 = relay.var("var_189", dtype = "uint16", shape = (10, 2, 12))#candidate|189|(10, 2, 12)|var|uint16
bop_190 = relay.minimum(var_188.astype('uint16'), var_189.astype('uint16')) # shape=(10, 2, 12)
output = bop_190
output2 = bop_190
func_193 = relay.Function([var_188,var_189,], output)
mod['func_193'] = func_193
mod = relay.transform.InferType()(mod)
var_194 = relay.var("var_194", dtype = "uint16", shape = (1, 2, 12))#candidate|194|(1, 2, 12)|var|uint16
var_195 = relay.var("var_195", dtype = "uint16", shape = (10, 2, 12))#candidate|195|(10, 2, 12)|var|uint16
output = func_193(var_194,var_195,)
func_196 = relay.Function([var_194,var_195,], output)
mutated_mod['func_196'] = func_196
mutated_mod = relay.transform.InferType()(mutated_mod)
var_272 = relay.var("var_272", dtype = "float64", shape = (8, 12, 11))#candidate|272|(8, 12, 11)|var|float64
uop_273 = relay.sinh(var_272.astype('float64')) # shape=(8, 12, 11)
output = relay.Tuple([uop_273,])
output2 = relay.Tuple([uop_273,])
func_276 = relay.Function([var_272,], output)
mod['func_276'] = func_276
mod = relay.transform.InferType()(mod)
mutated_mod['func_276'] = func_276
mutated_mod = relay.transform.InferType()(mutated_mod)
var_277 = relay.var("var_277", dtype = "float64", shape = (8, 12, 11))#candidate|277|(8, 12, 11)|var|float64
func_276_call = mutated_mod.get_global_var('func_276')
call_278 = func_276_call(var_277)
output = call_278
func_279 = relay.Function([var_277], output)
mutated_mod['func_279'] = func_279
mutated_mod = relay.transform.InferType()(mutated_mod)
var_331 = relay.var("var_331", dtype = "float32", shape = ())#candidate|331|()|var|float32
var_332 = relay.var("var_332", dtype = "float32", shape = (11, 9, 11))#candidate|332|(11, 9, 11)|var|float32
bop_333 = relay.less_equal(var_331.astype('bool'), var_332.astype('bool')) # shape=(11, 9, 11)
bop_341 = relay.equal(var_331.astype('bool'), var_332.astype('bool')) # shape=(11, 9, 11)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
var_347 = relay.var("var_347", dtype = "float64", shape = (1056,))#candidate|347|(1056,)|var|float64
call_346 = relay.TupleGetItem(func_276_call(relay.reshape(var_347.astype('float64'), [8, 12, 11])), 0)
call_348 = relay.TupleGetItem(func_279_call(relay.reshape(var_347.astype('float64'), [8, 12, 11])), 0)
output = relay.Tuple([bop_333,bop_341,call_346,var_347,])
output2 = relay.Tuple([bop_333,bop_341,call_348,var_347,])
func_351 = relay.Function([var_331,var_332,var_347,], output)
mod['func_351'] = func_351
mod = relay.transform.InferType()(mod)
mutated_mod['func_351'] = func_351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_351_call = mutated_mod.get_global_var('func_351')
var_353 = relay.var("var_353", dtype = "float32", shape = ())#candidate|353|()|var|float32
var_354 = relay.var("var_354", dtype = "float32", shape = (11, 9, 11))#candidate|354|(11, 9, 11)|var|float32
var_355 = relay.var("var_355", dtype = "float64", shape = (1056,))#candidate|355|(1056,)|var|float64
call_352 = func_351_call(var_353,var_354,var_355,)
output = call_352
func_356 = relay.Function([var_353,var_354,var_355,], output)
mutated_mod['func_356'] = func_356
mutated_mod = relay.transform.InferType()(mutated_mod)
var_405 = relay.var("var_405", dtype = "float32", shape = (16, 11, 9))#candidate|405|(16, 11, 9)|var|float32
var_406 = relay.var("var_406", dtype = "float32", shape = (16, 11, 9))#candidate|406|(16, 11, 9)|var|float32
bop_407 = relay.equal(var_405.astype('bool'), relay.reshape(var_406.astype('bool'), relay.shape_of(var_405))) # shape=(16, 11, 9)
bop_417 = relay.bitwise_or(var_406.astype('int16'), relay.reshape(var_405.astype('int16'), relay.shape_of(var_406))) # shape=(16, 11, 9)
output = relay.Tuple([bop_407,bop_417,])
output2 = relay.Tuple([bop_407,bop_417,])
func_423 = relay.Function([var_405,var_406,], output)
mod['func_423'] = func_423
mod = relay.transform.InferType()(mod)
var_424 = relay.var("var_424", dtype = "float32", shape = (16, 11, 9))#candidate|424|(16, 11, 9)|var|float32
var_425 = relay.var("var_425", dtype = "float32", shape = (16, 11, 9))#candidate|425|(16, 11, 9)|var|float32
output = func_423(var_424,var_425,)
func_426 = relay.Function([var_424,var_425,], output)
mutated_mod['func_426'] = func_426
mutated_mod = relay.transform.InferType()(mutated_mod)
var_444 = relay.var("var_444", dtype = "float64", shape = (1, 7, 5))#candidate|444|(1, 7, 5)|var|float64
uop_445 = relay.asinh(var_444.astype('float64')) # shape=(1, 7, 5)
output = relay.Tuple([uop_445,])
output2 = relay.Tuple([uop_445,])
func_459 = relay.Function([var_444,], output)
mod['func_459'] = func_459
mod = relay.transform.InferType()(mod)
mutated_mod['func_459'] = func_459
mutated_mod = relay.transform.InferType()(mutated_mod)
var_460 = relay.var("var_460", dtype = "float64", shape = (1, 7, 5))#candidate|460|(1, 7, 5)|var|float64
func_459_call = mutated_mod.get_global_var('func_459')
call_461 = func_459_call(var_460)
output = call_461
func_462 = relay.Function([var_460], output)
mutated_mod['func_462'] = func_462
mutated_mod = relay.transform.InferType()(mutated_mod)
var_897 = relay.var("var_897", dtype = "uint32", shape = (14, 5, 6))#candidate|897|(14, 5, 6)|var|uint32
const_898 = relay.const([[[-2,3,-8,10,8,-6],[6,-1,-3,-8,-2,9],[-2,10,-10,1,4,3],[-5,-2,1,-7,2,-7],[-9,-7,2,4,-10,7]],[[-9,-1,-4,-7,-9,1],[-6,8,-6,-10,-8,7],[4,-7,-8,-4,5,-4],[-4,-10,-9,-5,-9,1],[-8,10,10,9,3,-10]],[[-2,-9,-4,8,3,10],[-10,5,2,3,-8,7],[4,-4,3,7,-8,4],[9,-9,1,4,-8,1],[4,-9,8,-10,3,-1]],[[-8,4,7,8,-10,-10],[-8,-4,-1,6,8,-8],[1,-1,2,3,-2,-5],[-4,7,-2,7,-9,-8],[-6,8,10,-10,-5,-7]],[[5,-8,8,-6,-8,8],[-7,-4,6,9,-6,5],[2,-9,8,-4,8,2],[5,8,-2,-7,-1,-7],[1,-10,10,5,3,-9]],[[-9,-6,4,5,-5,-5],[9,-5,-1,7,8,-10],[-5,2,-8,8,3,8],[-1,1,6,-2,7,5],[-10,3,2,-6,-10,-4]],[[9,-10,6,-4,-1,-5],[-10,-1,-4,9,9,-2],[7,7,-8,8,4,2],[5,9,10,10,8,-8],[-8,-8,7,9,10,1]],[[-6,5,-6,2,-4,7],[2,3,1,-4,-6,-7],[4,9,1,-4,-1,-8],[8,8,8,4,-3,4],[8,-4,-2,-9,6,-2]],[[10,-5,-5,-9,5,-4],[3,5,-7,-1,-8,-9],[-5,-9,-6,9,7,8],[8,-6,5,6,-10,-7],[1,-3,-4,-9,1,-1]],[[9,5,-3,-9,-10,-6],[6,4,-4,-4,8,5],[-10,-10,-4,-9,10,-10],[-9,-6,5,6,3,-7],[9,-3,1,-9,-2,-1]],[[10,9,6,-3,-10,5],[-10,-5,1,9,7,8],[-9,8,-8,8,-9,-7],[8,-9,10,2,-5,2],[-10,5,-4,5,10,5]],[[-2,-5,9,5,4,6],[10,-4,8,10,-1,-7],[-9,-8,-6,6,-5,-9],[5,-4,10,2,1,-6],[4,-6,4,-9,4,2]],[[2,9,1,4,4,2],[1,5,-2,8,10,10],[-7,-6,8,-2,6,-10],[9,-2,3,8,-9,-5],[-5,-6,6,8,-5,-4]],[[-2,5,-8,-6,10,-2],[1,-6,-3,9,5,5],[-1,5,-9,1,7,-1],[3,-6,5,-6,7,9],[7,8,-5,-3,7,-4]]], dtype = "uint32")#candidate|898|(14, 5, 6)|const|uint32
bop_899 = relay.less(var_897.astype('bool'), relay.reshape(const_898.astype('bool'), relay.shape_of(var_897))) # shape=(14, 5, 6)
output = relay.Tuple([bop_899,])
output2 = relay.Tuple([bop_899,])
func_904 = relay.Function([var_897,], output)
mod['func_904'] = func_904
mod = relay.transform.InferType()(mod)
var_905 = relay.var("var_905", dtype = "uint32", shape = (14, 5, 6))#candidate|905|(14, 5, 6)|var|uint32
output = func_904(var_905)
func_906 = relay.Function([var_905], output)
mutated_mod['func_906'] = func_906
mutated_mod = relay.transform.InferType()(mutated_mod)
const_961 = relay.const([[[7,4,-4,-2],[-8,4,-2,-8],[-5,-7,-3,3],[-6,-3,-1,4],[-6,-7,-5,-3],[-10,7,-8,-2],[5,2,-4,-9],[1,7,-7,-3],[1,-5,-9,-7],[3,-2,-8,-4],[4,2,2,-10]],[[-5,9,8,-7],[2,-5,-10,1],[-8,-6,7,-3],[7,-1,-9,6],[-8,6,-8,6],[4,-2,-4,8],[6,-2,4,-6],[-1,4,5,-3],[-6,8,-1,4],[6,10,9,-5],[3,-9,-3,2]],[[1,-3,5,-9],[5,4,4,3],[-6,-1,2,1],[1,4,7,7],[9,4,6,-4],[-5,-8,8,8],[-6,-8,-4,4],[1,1,-4,-5],[8,9,-7,6],[-3,10,8,3],[6,4,10,-5]],[[-8,10,7,-6],[-7,1,-8,-5],[-5,-2,2,9],[-9,-9,-1,-2],[3,10,7,4],[-9,-9,4,-9],[8,4,-9,7],[-3,6,1,10],[10,-3,-6,-5],[2,3,8,4],[3,6,-10,9]],[[1,5,3,-7],[7,-4,-5,-7],[2,4,2,-4],[8,9,4,9],[-3,-7,-2,-1],[-4,-2,-3,7],[-9,-3,-1,-7],[8,-4,4,-6],[-2,3,-7,4],[1,-2,5,10],[-10,-6,-2,9]],[[1,-2,9,-1],[-5,4,3,5],[2,-8,7,-2],[3,-8,-2,-6],[-10,-7,-10,-9],[-7,7,9,-1],[9,9,-7,3],[-8,6,-7,3],[3,-6,2,-6],[-8,-8,4,7],[1,7,6,8]],[[2,6,-6,-9],[-10,-10,2,-3],[10,5,-1,7],[-10,-1,-6,-4],[3,-8,-10,-8],[3,5,5,-4],[-9,8,3,3],[-10,4,3,4],[8,7,-10,10],[-6,-7,-5,7],[-1,-6,-2,10]],[[3,-8,1,-4],[-6,9,-7,-9],[8,-5,8,6],[9,-4,1,1],[-9,10,-4,3],[5,-8,-2,7],[-5,-2,-6,-10],[10,-4,-9,3],[-7,-10,-7,-1],[-4,9,7,6],[10,-3,-6,-9]],[[-9,7,7,8],[5,5,10,6],[-6,-9,-1,-5],[5,-7,-4,-9],[-9,-3,-6,-2],[-8,3,-4,1],[4,-3,7,7],[-7,-4,1,6],[-10,8,-9,-7],[7,4,-8,9],[4,-8,1,2]],[[-2,-1,-10,4],[-5,5,3,10],[1,9,-8,1],[2,3,-7,-5],[1,-3,-4,-2],[1,2,1,-2],[-7,-2,-1,9],[4,-1,6,1],[2,10,-5,5],[-2,-8,1,5],[-4,5,10,1]],[[5,-7,5,-8],[-6,-3,9,-4],[6,-3,-5,7],[3,-3,7,9],[5,2,-3,-7],[7,9,9,-6],[-7,-4,-7,-10],[-4,-3,8,-2],[7,-10,-2,-1],[-8,-4,4,-6],[9,1,-10,6]],[[5,-4,3,-3],[9,3,2,-8],[-4,1,-4,-9],[4,1,-1,1],[-10,7,10,6],[-5,1,-4,-10],[-3,8,-6,2],[-5,8,-2,1],[4,5,-10,-5],[9,4,7,4],[3,-9,7,2]]], dtype = "uint64")#candidate|961|(12, 11, 4)|const|uint64
var_962 = relay.var("var_962", dtype = "uint64", shape = (12, 11, 4))#candidate|962|(12, 11, 4)|var|uint64
bop_963 = relay.bitwise_or(const_961.astype('uint64'), relay.reshape(var_962.astype('uint64'), relay.shape_of(const_961))) # shape=(12, 11, 4)
uop_972 = relay.rsqrt(var_962.astype('float64')) # shape=(12, 11, 4)
var_974 = relay.var("var_974", dtype = "float64", shape = (12, 11, 4))#candidate|974|(12, 11, 4)|var|float64
bop_975 = relay.maximum(uop_972.astype('uint32'), relay.reshape(var_974.astype('uint32'), relay.shape_of(uop_972))) # shape=(12, 11, 4)
uop_980 = relay.atan(uop_972.astype('float64')) # shape=(12, 11, 4)
func_193_call = mod.get_global_var('func_193')
func_196_call = mutated_mod.get_global_var('func_196')
var_988 = relay.var("var_988", dtype = "uint16", shape = (24,))#candidate|988|(24,)|var|uint16
const_989 = relay.const([[8,-4],[-1,-3],[-8,10],[8,4],[-9,-9],[-7,7],[7,-6],[-5,-2],[8,-4],[-6,-7],[-8,10],[-6,5],[-3,8],[-9,8],[9,8],[-10,-1],[-8,-9],[-3,-1],[-5,9],[5,-9],[-8,2],[5,3],[4,10],[-4,2],[5,6],[-8,-1],[10,-6],[-3,5],[5,-1],[7,-4],[7,-3],[-4,-3],[-6,9],[8,7],[-9,2],[10,-7],[5,5],[2,-3],[3,8],[-10,-8],[-9,-10],[-6,-2],[-2,1],[2,-8],[4,8],[-3,2],[6,-5],[10,3],[-10,-8],[-10,3],[5,-5],[-2,3],[-4,-1],[-2,3],[5,-4],[-1,6],[-10,10],[-5,3],[7,-6],[-10,-4],[-1,-3],[7,1],[-6,-9],[-4,10],[9,5],[1,5],[-7,-8],[1,-3],[-6,-7],[4,7],[5,-9],[-10,4],[-7,5],[-8,-7],[-1,-5],[-6,7],[7,-6],[-2,-1],[10,-5],[-8,-2],[-9,-2],[-9,-3],[5,-5],[6,-6],[-5,-6],[-7,5],[6,10],[10,-9],[-10,5],[2,-10],[-8,2],[8,-9],[-10,2],[-1,-7],[-9,-2],[-10,8],[-2,1],[-3,-4],[7,-4],[-2,8],[9,1],[8,-6],[-4,6],[9,-6],[-6,-6],[-10,-9],[6,2],[8,10],[-1,-7],[9,-6],[4,-9],[-5,-6],[1,-10],[-2,-8],[4,-6],[1,10],[-7,10],[2,10],[-7,9],[-1,-3]], dtype = "uint16")#candidate|989|(120, 2)|const|uint16
call_987 = func_193_call(relay.reshape(var_988.astype('uint16'), [1, 2, 12]), relay.reshape(const_989.astype('uint16'), [10, 2, 12]), )
call_990 = func_193_call(relay.reshape(var_988.astype('uint16'), [1, 2, 12]), relay.reshape(const_989.astype('uint16'), [10, 2, 12]), )
func_459_call = mod.get_global_var('func_459')
func_462_call = mutated_mod.get_global_var('func_462')
const_997 = relay.const([6.193778,3.743934,-8.878533,-7.753452,-5.956248,8.015051,1.300630,-3.681517,4.925902,2.620828,9.333927,-7.551682,-0.283928,3.331174,-4.218177,-7.950509,4.957328,3.115499,6.434255,7.920072,-9.837552,-9.646953,0.583992,-2.109686,-6.046509,-5.095550,1.928006,7.786096,8.297564,-4.201136,7.868203,-1.595859,-4.075971,1.085522,0.832909], dtype = "float64")#candidate|997|(35,)|const|float64
call_996 = relay.TupleGetItem(func_459_call(relay.reshape(const_997.astype('float64'), [1, 7, 5])), 0)
call_998 = relay.TupleGetItem(func_462_call(relay.reshape(const_997.astype('float64'), [1, 7, 5])), 0)
output = relay.Tuple([bop_963,bop_975,uop_980,call_987,var_988,const_989,call_996,const_997,])
output2 = relay.Tuple([bop_963,bop_975,uop_980,call_990,var_988,const_989,call_998,const_997,])
func_1014 = relay.Function([var_962,var_974,var_988,], output)
mod['func_1014'] = func_1014
mod = relay.transform.InferType()(mod)
var_1015 = relay.var("var_1015", dtype = "uint64", shape = (12, 11, 4))#candidate|1015|(12, 11, 4)|var|uint64
var_1016 = relay.var("var_1016", dtype = "float64", shape = (12, 11, 4))#candidate|1016|(12, 11, 4)|var|float64
var_1017 = relay.var("var_1017", dtype = "uint16", shape = (24,))#candidate|1017|(24,)|var|uint16
output = func_1014(var_1015,var_1016,var_1017,)
func_1018 = relay.Function([var_1015,var_1016,var_1017,], output)
mutated_mod['func_1018'] = func_1018
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1206 = relay.const([[[-3.010511,9.597118,9.445500],[7.875857,-7.263974,-3.141391],[-3.238233,-3.528461,5.268570],[-3.142862,-3.732718,-5.854093],[4.054076,5.981440,4.858384],[0.962011,-7.315234,-4.808990],[7.111815,8.091251,-1.293122],[7.981821,-1.974978,-8.591544]],[[4.497470,9.361185,6.184932],[-4.795457,2.830926,-7.970801],[1.456519,-6.545181,-1.534632],[4.092241,-9.168766,9.670512],[1.616387,4.140166,9.142193],[6.569840,0.667936,-4.880063],[-1.542883,8.490070,-9.376002],[0.225416,8.940722,-9.188405]],[[-7.148982,-5.276356,-6.913786],[-7.767081,-3.859708,-1.024369],[7.570674,4.060561,-0.068011],[7.578057,-4.626378,-6.552303],[-8.544872,-1.299811,5.315414],[6.850859,8.085821,5.186400],[-6.755388,7.333614,9.864328],[-9.503300,5.285941,3.993646]],[[7.962467,9.134634,-3.310066],[5.164533,8.038143,-6.619915],[-2.932794,-2.763364,4.961084],[0.220725,0.957499,4.938454],[-9.333164,4.684782,7.054194],[-1.203466,-7.629052,-9.830966],[0.202080,3.037846,-3.459243],[-1.242255,-1.493109,-8.043764]],[[-8.894365,3.749446,-1.252702],[-0.846428,-0.284377,-8.481787],[3.813553,-9.168667,-2.330380],[-8.745822,-7.855994,-1.275621],[5.754810,8.679061,-2.162064],[-6.193889,-3.297520,-5.812909],[-4.202735,4.559954,1.205823],[-7.236678,-7.456860,-0.015223]],[[1.807189,2.481273,-5.012013],[-9.220148,-8.145428,4.649564],[3.438955,9.105591,8.828789],[-4.722309,-9.263076,-3.496197],[-4.646636,-2.993266,-0.167058],[3.245140,7.926154,2.960470],[4.421085,-3.247207,-7.791050],[-7.925891,0.891413,8.223440]],[[8.254842,-4.265962,1.045775],[9.716477,8.485453,9.436821],[-5.152618,2.475463,9.847442],[-4.117183,7.889217,-1.656316],[-1.903290,4.214018,-0.450851],[3.561325,7.234997,3.027870],[-8.294364,-5.733443,0.655665],[5.526002,-7.159142,0.358314]],[[-9.787325,-5.171346,-3.473222],[0.644037,2.774289,-5.055600],[2.786846,-1.401986,7.914702],[0.560715,-1.929499,1.228132],[4.320426,-6.964553,-8.049537],[9.626265,2.720678,-1.165473],[-1.657756,-7.078490,-6.878952],[1.920426,-7.742799,-8.300056]],[[-6.983948,-8.796771,6.986552],[-2.406397,-6.526620,3.727929],[-7.060923,3.092308,-7.173032],[-0.619035,3.532867,4.386429],[1.334798,0.313287,-5.021894],[-2.562542,-2.249587,3.917250],[-4.215887,-5.339875,-8.971147],[9.942577,1.313343,-4.618969]],[[-6.957572,-3.855192,-5.796312],[-4.502204,4.680527,2.469454],[4.594523,-9.258897,-2.996050],[-8.804816,3.592956,-3.232018],[-8.366149,-8.428881,-5.702105],[7.365380,0.964254,7.558491],[5.392583,-1.654450,6.689481],[-1.868007,2.389757,-0.070020]]], dtype = "float32")#candidate|1206|(10, 8, 3)|const|float32
var_1207 = relay.var("var_1207", dtype = "float32", shape = (10, 8, 3))#candidate|1207|(10, 8, 3)|var|float32
bop_1208 = relay.floor_mod(const_1206.astype('float32'), relay.reshape(var_1207.astype('float32'), relay.shape_of(const_1206))) # shape=(10, 8, 3)
func_423_call = mod.get_global_var('func_423')
func_426_call = mutated_mod.get_global_var('func_426')
var_1212 = relay.var("var_1212", dtype = "float32", shape = (1584,))#candidate|1212|(1584,)|var|float32
call_1211 = relay.TupleGetItem(func_423_call(relay.reshape(var_1212.astype('float32'), [16, 11, 9]), relay.reshape(var_1212.astype('float32'), [16, 11, 9]), ), 0)
call_1213 = relay.TupleGetItem(func_426_call(relay.reshape(var_1212.astype('float32'), [16, 11, 9]), relay.reshape(var_1212.astype('float32'), [16, 11, 9]), ), 0)
output = relay.Tuple([bop_1208,call_1211,var_1212,])
output2 = relay.Tuple([bop_1208,call_1213,var_1212,])
func_1233 = relay.Function([var_1207,var_1212,], output)
mod['func_1233'] = func_1233
mod = relay.transform.InferType()(mod)
var_1234 = relay.var("var_1234", dtype = "float32", shape = (10, 8, 3))#candidate|1234|(10, 8, 3)|var|float32
var_1235 = relay.var("var_1235", dtype = "float32", shape = (1584,))#candidate|1235|(1584,)|var|float32
output = func_1233(var_1234,var_1235,)
func_1236 = relay.Function([var_1234,var_1235,], output)
mutated_mod['func_1236'] = func_1236
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1283 = relay.var("var_1283", dtype = "float64", shape = (1, 8, 13))#candidate|1283|(1, 8, 13)|var|float64
uop_1284 = relay.atanh(var_1283.astype('float64')) # shape=(1, 8, 13)
output = uop_1284
output2 = uop_1284
func_1302 = relay.Function([var_1283,], output)
mod['func_1302'] = func_1302
mod = relay.transform.InferType()(mod)
mutated_mod['func_1302'] = func_1302
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1303 = relay.var("var_1303", dtype = "float64", shape = (1, 8, 13))#candidate|1303|(1, 8, 13)|var|float64
func_1302_call = mutated_mod.get_global_var('func_1302')
call_1304 = func_1302_call(var_1303)
output = call_1304
func_1305 = relay.Function([var_1303], output)
mutated_mod['func_1305'] = func_1305
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1634 = relay.const([[[-1.377608,-0.251096,-7.344312,-3.000751,7.096315,-8.400355,4.894944,-9.708436,2.671435,-8.645217,-3.565199],[-0.268475,-3.695108,-1.358010,-3.843615,-4.787925,1.446260,3.491521,-2.497924,-7.708639,-6.587852,7.009324],[7.545931,-1.879659,3.956134,-5.500494,2.972068,-9.047626,7.810742,3.779541,7.771952,-4.778624,-7.651375],[-5.677557,-5.595481,1.668884,9.031931,-8.806466,-7.077055,-8.731181,9.239576,3.760376,4.214084,1.683359],[-4.808997,-2.343793,-3.924606,1.845753,2.710945,1.960616,-4.477607,-9.190234,0.009228,-1.311390,3.642757],[-8.219904,8.185163,-5.084790,1.251749,-1.859994,-3.591504,5.708905,3.740676,-7.645317,-8.563445,-7.243339],[-2.076282,9.787257,-6.054431,4.128988,-2.488536,-3.951427,8.972852,-1.010852,-6.160961,-2.524715,2.385490],[-2.545601,-9.452420,0.212126,-4.748880,9.951272,-9.830443,2.719697,-3.623408,5.509481,-1.586849,5.931810],[-8.829214,-3.902040,-9.534778,3.449154,5.256573,-9.057435,-9.181876,-9.309932,-2.247194,9.486171,-4.495608],[9.668005,4.512089,2.007195,-8.481460,9.500661,-6.844223,-0.145591,6.199795,9.926828,1.576836,-6.270621],[8.538201,-8.634691,3.907344,1.437687,-2.963967,-6.610898,0.682695,0.024989,-8.097816,-9.349120,7.441826],[4.823990,-8.586689,9.407656,6.913540,-7.081209,-0.345718,-0.170741,-5.425255,-3.367432,-7.589229,4.786350],[-6.179829,9.122018,1.381581,-1.697000,-8.497619,9.058467,-7.883591,-8.893677,3.158654,-4.805436,-6.286561],[5.542732,-4.997299,1.532491,-4.773485,-1.719537,-4.132173,-9.224183,1.290999,-2.538050,-7.647986,9.488899],[-1.012817,-8.633357,-7.633425,0.037878,7.357469,8.780509,-1.576891,-1.885318,4.395146,-3.819862,8.362176],[-1.597504,4.714323,-2.306344,-6.271086,-6.156321,-8.888865,-9.232229,1.539269,3.572144,-9.719961,3.238958]],[[5.904439,-8.383587,-3.717248,-0.140728,2.359216,4.759941,7.098208,-9.004766,4.917785,-5.457259,-5.400313],[-8.303042,3.780514,-3.408004,-8.721823,-9.401782,-8.044532,8.290336,2.966186,-7.460474,-5.661665,5.745164],[5.014144,2.808288,-6.710053,-6.363989,9.745790,3.572705,-9.127711,-0.938434,1.690042,4.390772,2.404381],[-5.616684,-7.295377,9.966417,-1.673727,9.988127,2.496771,-1.534495,-3.190455,-4.131388,7.474827,-4.435396],[9.409409,7.971998,-9.267504,-8.342334,6.148927,-8.807683,5.693042,-4.505280,9.380973,-7.936657,-7.442377],[-1.449704,3.156431,-8.739996,-6.360258,2.921091,-7.991691,-5.115118,8.120144,-1.191003,-1.472688,-9.478981],[8.653364,8.448966,-1.679662,6.697391,9.880083,-5.523440,-2.466639,1.256276,6.108127,-6.227925,0.639251],[-7.367719,-9.269936,0.198962,-2.798790,-9.198117,-2.811072,-9.866078,3.301193,-8.263153,4.534298,-4.090110],[5.960041,4.111332,-5.928038,-0.979241,-2.290414,-1.809538,-2.571081,4.582965,5.098574,-1.193376,-5.418659],[6.469507,-6.601362,-2.326569,-4.401841,5.630286,-5.630315,-6.596376,-5.835296,7.310607,-7.731536,4.459319],[0.618474,9.382870,5.222059,7.871881,-5.164616,8.854526,-3.279089,-1.234440,-2.132277,-4.671973,-5.490633],[0.058978,-4.340020,-2.971922,-7.772885,6.094405,-2.157420,6.655231,-3.951998,3.289498,9.273738,1.165954],[-2.378959,-2.987755,1.371637,-1.857591,0.037218,-5.667651,-5.656549,-5.765350,1.924360,-6.405498,-2.814622],[7.400081,-2.338329,9.709044,4.200362,8.580071,1.353073,9.090936,2.652318,-1.957463,4.573119,-6.563657],[9.193037,3.321370,-9.078087,8.535638,6.223264,6.017673,4.477827,8.119874,2.457499,3.301117,-0.922414],[9.342479,-4.339985,-6.060480,-1.200888,2.118533,-5.575347,-0.999347,-4.673626,0.651493,-6.830516,-7.383355]],[[-5.483700,6.572021,-4.638416,-2.227146,2.659031,-0.225314,8.396550,1.145291,3.288431,-8.239637,0.818621],[-3.836425,-1.269507,5.034081,-3.503268,-3.861496,5.621398,-0.940342,-5.013445,-5.309824,-2.829358,7.267248],[-5.163886,-3.012727,2.701971,6.061773,7.386970,8.266985,3.946519,0.360124,-0.222998,-6.705645,7.285384],[0.247057,5.887282,5.055090,2.137117,-5.287455,2.812726,6.739695,5.837920,-1.446295,8.666859,-5.327616],[-0.986764,-9.675957,8.077467,9.300536,-3.857729,0.143969,-7.543633,1.706844,1.005376,3.766741,-8.255845],[-9.232745,0.197524,3.455929,-8.687500,-0.803940,6.668473,5.591310,0.501536,9.064420,8.497986,-5.236968],[3.426885,8.607935,7.761569,2.047027,-2.976617,2.202857,-1.425964,-4.847998,-6.135032,-0.464790,4.776926],[-4.347719,-6.713876,-9.751073,-7.353115,0.174015,3.068288,3.076820,-3.897173,-1.382484,-3.146591,-3.357893],[-3.014513,0.722055,5.343135,-0.239918,6.642717,-4.974792,-7.226526,9.890161,3.769467,-6.366716,-3.660666],[9.494475,6.264234,9.450765,4.606291,-9.125136,-2.737765,-3.964242,9.307477,-8.690965,7.259243,-4.334010],[-8.177684,9.963625,8.887574,-3.978735,3.762348,-2.856321,1.062148,-8.312120,3.891291,1.165698,-2.856476],[-9.419373,-9.153580,-5.247075,3.711473,-2.994432,-3.715056,2.341132,1.281901,0.156555,6.696444,5.797638],[3.845664,4.556317,6.284610,-8.551212,-1.052641,6.693713,-8.029687,-6.577370,9.777725,4.599407,-2.929759],[0.118999,-4.035805,-3.620872,-9.744297,-7.022717,2.505230,-2.288976,-0.646106,-9.158791,5.027804,-5.879365],[3.964050,6.276302,8.700259,3.072334,8.937593,1.351380,8.876015,3.196800,-7.718518,-0.514587,2.730506],[-9.431253,7.916612,-2.162908,-8.062056,-6.930319,-5.063231,-5.864520,-4.774672,3.893570,-0.723737,1.582647]],[[7.538949,7.527110,3.347126,5.255526,6.082807,-5.650344,3.387027,5.558518,7.385736,4.382671,-2.059795],[6.877873,7.592843,-5.377091,-3.569044,-8.004891,3.296404,5.864503,0.600161,5.572457,-2.872026,0.709524],[9.783565,6.224932,1.536000,-2.341187,0.102903,-7.199851,-0.637855,-8.956548,2.397810,-3.152136,8.437173],[4.916268,3.926145,6.607641,-4.379676,1.689570,1.855010,3.634178,6.033111,-1.341935,1.895713,-3.197275],[-9.325757,-8.301700,9.755472,-0.206601,-3.427271,4.171338,-9.465584,9.534464,9.249515,-2.242806,-6.233536],[8.270464,9.420507,-1.525196,2.842086,9.661256,9.452424,5.836186,-2.798450,7.344693,8.061896,-9.624596],[8.131922,-2.687973,-1.697064,-9.587220,-0.530633,1.701171,1.745982,8.076811,-6.626748,-3.408967,-5.745960],[-0.608112,0.099470,-8.446412,-6.780462,1.287361,-4.989716,-5.406863,-0.003025,4.511155,5.600391,3.287876],[-1.254341,1.194118,4.172333,6.576529,8.412187,-5.927965,1.392500,6.996729,-2.701324,-2.807212,-5.181533],[6.899402,2.528998,-4.446790,3.384382,7.429755,-8.949081,-5.493429,0.458417,7.116675,5.240599,7.652623],[-6.536066,-9.194500,5.440963,-2.754803,-4.103411,6.914981,-3.285970,-0.256755,3.108292,-3.605982,-2.787288],[0.076057,-2.644410,-8.551327,-9.243514,-3.515525,-6.872252,1.076763,9.317801,7.269844,-8.066823,8.707292],[-3.388655,-9.532930,-6.302638,2.675052,-2.554615,-3.530951,-8.378870,-7.084634,-4.294278,3.620498,-6.561995],[7.022479,-4.597429,2.663343,1.118728,-8.853708,-5.769730,2.590435,5.399381,8.790097,1.358529,-7.922431],[-2.408576,-1.807013,8.745160,1.346028,7.585082,-5.320153,6.807265,-2.423984,-5.798889,8.151014,4.926054],[1.351626,7.299423,-0.047599,-7.172344,-0.122946,-8.770422,-1.748763,6.569492,6.054264,-8.439565,-7.473372]],[[1.902359,-0.957299,5.460229,-2.479852,-7.396163,0.796427,-0.210130,-7.658935,-3.531738,7.592456,3.522218],[2.127506,1.753494,5.400881,-9.373392,9.259564,-4.903987,0.903549,7.786887,7.855829,-8.635508,-4.300059],[-3.340150,5.190095,0.011765,3.944919,-2.050335,3.173524,4.116763,3.659232,5.120616,5.532898,-6.202750],[9.219731,-9.332487,4.537566,-7.910018,7.970973,-7.402343,9.745401,1.697289,9.784838,8.415089,9.816766],[0.652274,-1.809271,-1.481223,0.128127,4.482727,-9.428040,1.250604,-9.560586,5.593877,-9.861363,-4.390347],[-3.200839,9.615173,-2.239841,-3.081958,7.507239,-2.708667,-7.632431,-9.480874,-5.890338,9.103820,0.281474],[-4.175173,-9.524060,-5.757771,-6.679160,-7.133130,-5.510357,-2.526734,8.659857,1.548059,-7.265387,-4.862817],[-6.131914,-9.614832,-1.316441,1.784992,-7.361078,2.568756,-9.928191,-6.869474,0.657442,2.045454,-0.284921],[-8.789453,-1.172145,-9.211427,0.242298,-5.710742,0.953339,-6.597458,-2.601003,-6.033797,-9.727615,3.158297],[6.831756,5.735365,-4.292686,-4.889219,-6.176796,-3.781383,-7.067809,3.663891,-0.989308,1.444573,4.433624],[5.304024,-5.998128,-6.212553,-9.868760,1.487625,6.762036,-3.077851,9.295809,-9.192442,5.078539,-5.517608],[-9.785433,2.336077,9.690709,-0.527621,7.077827,-2.892927,6.095052,-2.924865,-3.219894,8.595900,-6.778414],[-2.955385,4.472834,9.933652,5.286411,-9.601020,5.605770,-6.344504,4.308078,5.451796,1.974143,-2.367601],[8.637473,-9.133826,-6.996649,2.185348,7.226361,-9.475255,0.355064,5.467899,0.718939,-4.635387,1.829087],[-3.072922,1.451339,8.334772,5.087203,-7.813464,-9.718833,9.510489,-6.673216,2.082198,-4.368362,-9.595924],[2.169335,-0.961691,-7.611872,-6.113233,-6.909017,-2.387714,-8.852948,-3.497509,5.154471,-8.307472,8.170286]],[[-4.623648,6.095215,6.005346,1.162630,6.773508,7.470878,6.910619,-0.394057,8.332707,-6.836572,-4.662792],[-7.307682,7.078334,0.338814,3.140421,4.205898,5.042562,-3.103566,-0.492658,-6.474674,-2.420783,3.410316],[0.272438,1.810371,-5.111452,-0.927182,4.753569,1.673027,-2.954917,-3.051095,1.330888,5.547155,-0.341849],[3.471961,9.289979,-9.955346,6.209334,-6.898402,4.994891,-2.653157,5.268886,0.714633,5.546398,7.978113],[8.974147,5.800845,9.464675,3.776665,-1.862768,-3.228713,8.246575,-7.309168,0.251573,4.599735,-4.697174],[-1.997002,4.673405,-9.684473,1.486844,-1.708171,-0.564268,3.124634,6.832416,2.833085,-9.329702,5.548343],[2.884514,-5.430466,-4.383072,5.527899,2.153712,3.069257,7.366409,7.876737,7.410757,-5.642587,-9.860913],[-0.544957,-5.414412,3.056435,3.867391,-3.857451,-4.407812,1.514294,1.939852,-3.529949,6.324413,1.080276],[5.414602,4.042055,-4.039296,-9.710727,2.287282,-3.341129,4.229530,-4.890947,5.936074,8.096409,-7.308923],[-4.155736,8.124855,-9.903554,-1.369515,-5.440933,8.312604,0.981914,6.620762,-8.686239,-5.945626,-1.744465],[-5.340932,-7.931442,-4.403509,-3.215873,8.662424,-1.388745,0.937446,0.471601,-3.928275,7.286494,9.527623],[8.592940,0.547967,4.902674,0.331266,6.772982,2.098346,6.146777,9.755807,-6.176260,-5.980089,1.541606],[0.361246,-4.715776,-3.158042,5.778854,-5.966468,-1.024171,-9.949015,6.476947,-2.727489,-2.144912,-4.784546],[5.206306,6.946665,-7.393014,-8.480144,1.542541,-0.170929,0.680080,0.332367,-9.701525,9.338915,2.269508],[0.442458,2.569557,9.755009,5.840207,5.469538,4.249682,-3.834890,5.595717,-1.158940,-5.129327,-6.812458],[7.152262,7.282484,8.391234,1.463189,-8.726617,6.997851,-2.052658,1.584572,-4.532082,-8.828357,9.198623]]], dtype = "float32")#candidate|1634|(6, 16, 11)|const|float32
uop_1635 = relay.cosh(const_1634.astype('float32')) # shape=(6, 16, 11)
output = relay.Tuple([uop_1635,])
output2 = relay.Tuple([uop_1635,])
func_1643 = relay.Function([], output)
mod['func_1643'] = func_1643
mod = relay.transform.InferType()(mod)
output = func_1643()
func_1644 = relay.Function([], output)
mutated_mod['func_1644'] = func_1644
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_1656 = relay.TupleGetItem(func_1643_call(), 0)
call_1657 = relay.TupleGetItem(func_1644_call(), 0)
uop_1664 = relay.asinh(call_1656.astype('float32')) # shape=(6, 16, 11)
uop_1666 = relay.asinh(call_1657.astype('float32')) # shape=(6, 16, 11)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
const_1671 = relay.const([4,9,5,10,-7,-7,8,6,10,-1,-3,4,-6,6,-6,10,10,1,-3,9,7,1,-5,-3,3,3,-8,7,-6,8,4,2,-7,9,8,-2,-4,-10,-9,4,-6,8,-6,10,8,3,-5,-5,-10,6,4,2,-2,9,-5,3,-1,-5,-6,6,10,5,4,10,6,-1,4,8,-6,-7,-9,-2,3,-7,2,-10,-3,-10,5,-3,7,-1,9,-9,6,6,8,6,-7,8,-6,-6,5,10,-7,3,8,5,3,2,9,5,-8,-1,-3,8,9,-10,7,4,-10,-8,-1,6,8,-5,8,6,-10,2,-6,-3,-2,9,1,-7,-2,-1,-9,-9,7,-4,4,10,5,-5,4,-5,-9,10,-8,2,2,-3,10,-6,5,-1,-9,1,5,-6,4,-7,-4,4,2,9,9,4,5,-8,1,-9,2,-6,-8,6,-2,6,10,7,7,-5,-10,-8,1,3,-7,2,-4,6,1,-5,-7,-10,-2,8,-4,6,3,7,1,-6,6,-6,8,-2,4,-3,-8,-7,-9,10,9,7,9,6,8,6,1,4,-6,8,2,10,-4,10,3,9,5,5,-2,4,4,3,6,5,-4,1,-6,-5,9,8,-7,-5,4,6,1,-7,-2,10,-10,7,2,9,8,-10,1,-8,-4,-9,-10,-4,7,-8,4,6,-7,-7,10,6,-9,-6,4,-9,6,7,-4,-9,-4,9,-6,-1,7,-9,3,-6,2,5,5,-4,-3,-9,2,8,-4,4,-2,-3,5,6,9,-2,-4,-7,-2,-10,-2,4,6,9,-8,3,10,-9,-10,-6,-8,2,-9,3,-9,-6,3,-4,3,10,-6,3,9,-4,-8,-9,-1,10,-9,-1,7,9,9,-8,5,-4,-1,1,-9,-8,-5,5,6,-8,-8,3,-6,5,4,-8,1,3,10,-1,-9,10,-4,2,10,-6,8,-6,-2,2,6,6,-5,-1,-3,6,9,-7,-10,-6,-10,-9,-2,3,-7,9,-6,-3,7,5,-6,3,-6,-2,-9,5,1,-8,-10,-6,-5,-2,-3,9,1,-10,-5,-4,-1,-7,3,2,9,-6,10,-8,8,-5,9,10,9,6,-1,7,7,4,10,-3], dtype = "uint32")#candidate|1671|(420,)|const|uint32
call_1670 = relay.TupleGetItem(func_904_call(relay.reshape(const_1671.astype('uint32'), [14, 5, 6])), 0)
call_1672 = relay.TupleGetItem(func_906_call(relay.reshape(const_1671.astype('uint32'), [14, 5, 6])), 0)
output = relay.Tuple([uop_1664,call_1670,const_1671,])
output2 = relay.Tuple([uop_1666,call_1672,const_1671,])
func_1678 = relay.Function([], output)
mod['func_1678'] = func_1678
mod = relay.transform.InferType()(mod)
output = func_1678()
func_1679 = relay.Function([], output)
mutated_mod['func_1679'] = func_1679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_1693 = relay.TupleGetItem(func_1678_call(), 0)
call_1694 = relay.TupleGetItem(func_1679_call(), 0)
output = relay.Tuple([call_1693,])
output2 = relay.Tuple([call_1694,])
func_1705 = relay.Function([], output)
mod['func_1705'] = func_1705
mod = relay.transform.InferType()(mod)
mutated_mod['func_1705'] = func_1705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mutated_mod.get_global_var('func_1705')
call_1706 = func_1705_call()
output = call_1706
func_1707 = relay.Function([], output)
mutated_mod['func_1707'] = func_1707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_1779 = relay.TupleGetItem(func_1678_call(), 2)
call_1780 = relay.TupleGetItem(func_1679_call(), 2)
func_459_call = mod.get_global_var('func_459')
func_462_call = mutated_mod.get_global_var('func_462')
var_1808 = relay.var("var_1808", dtype = "float64", shape = (7, 5))#candidate|1808|(7, 5)|var|float64
call_1807 = relay.TupleGetItem(func_459_call(relay.reshape(var_1808.astype('float64'), [1, 7, 5])), 0)
call_1809 = relay.TupleGetItem(func_462_call(relay.reshape(var_1808.astype('float64'), [1, 7, 5])), 0)
output = relay.Tuple([call_1779,call_1807,var_1808,])
output2 = relay.Tuple([call_1780,call_1809,var_1808,])
func_1813 = relay.Function([var_1808,], output)
mod['func_1813'] = func_1813
mod = relay.transform.InferType()(mod)
mutated_mod['func_1813'] = func_1813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1814 = relay.var("var_1814", dtype = "float64", shape = (7, 5))#candidate|1814|(7, 5)|var|float64
func_1813_call = mutated_mod.get_global_var('func_1813')
call_1815 = func_1813_call(var_1814)
output = call_1815
func_1816 = relay.Function([var_1814], output)
mutated_mod['func_1816'] = func_1816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_1821 = relay.TupleGetItem(func_1643_call(), 0)
call_1822 = relay.TupleGetItem(func_1644_call(), 0)
uop_1839 = relay.tan(call_1821.astype('float64')) # shape=(6, 16, 11)
uop_1841 = relay.tan(call_1822.astype('float64')) # shape=(6, 16, 11)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
var_1847 = relay.var("var_1847", dtype = "uint32", shape = (420,))#candidate|1847|(420,)|var|uint32
call_1846 = relay.TupleGetItem(func_904_call(relay.reshape(var_1847.astype('uint32'), [14, 5, 6])), 0)
call_1848 = relay.TupleGetItem(func_906_call(relay.reshape(var_1847.astype('uint32'), [14, 5, 6])), 0)
output = relay.Tuple([uop_1839,call_1846,var_1847,])
output2 = relay.Tuple([uop_1841,call_1848,var_1847,])
func_1857 = relay.Function([var_1847,], output)
mod['func_1857'] = func_1857
mod = relay.transform.InferType()(mod)
var_1858 = relay.var("var_1858", dtype = "uint32", shape = (420,))#candidate|1858|(420,)|var|uint32
output = func_1857(var_1858)
func_1859 = relay.Function([var_1858], output)
mutated_mod['func_1859'] = func_1859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_1874 = relay.TupleGetItem(func_1643_call(), 0)
call_1875 = relay.TupleGetItem(func_1644_call(), 0)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_1883 = relay.TupleGetItem(func_1678_call(), 1)
call_1884 = relay.TupleGetItem(func_1679_call(), 1)
func_351_call = mod.get_global_var('func_351')
func_356_call = mutated_mod.get_global_var('func_356')
var_1903 = relay.var("var_1903", dtype = "float32", shape = ())#candidate|1903|()|var|float32
var_1904 = relay.var("var_1904", dtype = "float32", shape = (1089,))#candidate|1904|(1089,)|var|float32
call_1902 = relay.TupleGetItem(func_351_call(relay.reshape(var_1903.astype('float32'), []), relay.reshape(var_1904.astype('float32'), [11, 9, 11]), relay.reshape(call_1874.astype('float64'), [1056,]), ), 3)
call_1905 = relay.TupleGetItem(func_356_call(relay.reshape(var_1903.astype('float32'), []), relay.reshape(var_1904.astype('float32'), [11, 9, 11]), relay.reshape(call_1874.astype('float64'), [1056,]), ), 3)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_1906 = relay.TupleGetItem(func_1705_call(), 0)
call_1907 = relay.TupleGetItem(func_1707_call(), 0)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_1908 = relay.TupleGetItem(func_1678_call(), 1)
call_1909 = relay.TupleGetItem(func_1679_call(), 1)
output = relay.Tuple([call_1874,call_1883,call_1902,var_1903,var_1904,call_1906,call_1908,])
output2 = relay.Tuple([call_1875,call_1884,call_1905,var_1903,var_1904,call_1907,call_1909,])
func_1933 = relay.Function([var_1903,var_1904,], output)
mod['func_1933'] = func_1933
mod = relay.transform.InferType()(mod)
mutated_mod['func_1933'] = func_1933
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1933_call = mutated_mod.get_global_var('func_1933')
var_1935 = relay.var("var_1935", dtype = "float32", shape = ())#candidate|1935|()|var|float32
var_1936 = relay.var("var_1936", dtype = "float32", shape = (1089,))#candidate|1936|(1089,)|var|float32
call_1934 = func_1933_call(var_1935,var_1936,)
output = call_1934
func_1937 = relay.Function([var_1935,var_1936,], output)
mutated_mod['func_1937'] = func_1937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_1965 = relay.TupleGetItem(func_1643_call(), 0)
call_1966 = relay.TupleGetItem(func_1644_call(), 0)
func_1302_call = mod.get_global_var('func_1302')
func_1305_call = mutated_mod.get_global_var('func_1305')
var_1981 = relay.var("var_1981", dtype = "float64", shape = (104,))#candidate|1981|(104,)|var|float64
call_1980 = func_1302_call(relay.reshape(var_1981.astype('float64'), [1, 8, 13]))
call_1982 = func_1302_call(relay.reshape(var_1981.astype('float64'), [1, 8, 13]))
func_423_call = mod.get_global_var('func_423')
func_426_call = mutated_mod.get_global_var('func_426')
var_1984 = relay.var("var_1984", dtype = "float32", shape = (2, 792))#candidate|1984|(2, 792)|var|float32
call_1983 = relay.TupleGetItem(func_423_call(relay.reshape(var_1984.astype('float32'), [16, 11, 9]), relay.reshape(var_1984.astype('float32'), [16, 11, 9]), ), 0)
call_1985 = relay.TupleGetItem(func_426_call(relay.reshape(var_1984.astype('float32'), [16, 11, 9]), relay.reshape(var_1984.astype('float32'), [16, 11, 9]), ), 0)
output = relay.Tuple([call_1965,call_1980,var_1981,call_1983,var_1984,])
output2 = relay.Tuple([call_1966,call_1982,var_1981,call_1985,var_1984,])
func_2004 = relay.Function([var_1981,var_1984,], output)
mod['func_2004'] = func_2004
mod = relay.transform.InferType()(mod)
mutated_mod['func_2004'] = func_2004
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2004_call = mutated_mod.get_global_var('func_2004')
var_2006 = relay.var("var_2006", dtype = "float64", shape = (104,))#candidate|2006|(104,)|var|float64
var_2007 = relay.var("var_2007", dtype = "float32", shape = (2, 792))#candidate|2007|(2, 792)|var|float32
call_2005 = func_2004_call(var_2006,var_2007,)
output = call_2005
func_2008 = relay.Function([var_2006,var_2007,], output)
mutated_mod['func_2008'] = func_2008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_2089 = relay.TupleGetItem(func_1643_call(), 0)
call_2090 = relay.TupleGetItem(func_1644_call(), 0)
uop_2101 = relay.sin(call_2089.astype('float64')) # shape=(6, 16, 11)
uop_2103 = relay.sin(call_2090.astype('float64')) # shape=(6, 16, 11)
output = uop_2101
output2 = uop_2103
func_2138 = relay.Function([], output)
mod['func_2138'] = func_2138
mod = relay.transform.InferType()(mod)
mutated_mod['func_2138'] = func_2138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mutated_mod.get_global_var('func_2138')
call_2139 = func_2138_call()
output = call_2139
func_2140 = relay.Function([], output)
mutated_mod['func_2140'] = func_2140
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_2177 = relay.TupleGetItem(func_1705_call(), 0)
call_2178 = relay.TupleGetItem(func_1707_call(), 0)
var_2188 = relay.var("var_2188", dtype = "float32", shape = (6, 16, 11))#candidate|2188|(6, 16, 11)|var|float32
bop_2189 = relay.less(call_2177.astype('bool'), relay.reshape(var_2188.astype('bool'), relay.shape_of(call_2177))) # shape=(6, 16, 11)
bop_2192 = relay.less(call_2178.astype('bool'), relay.reshape(var_2188.astype('bool'), relay.shape_of(call_2178))) # shape=(6, 16, 11)
func_1933_call = mod.get_global_var('func_1933')
func_1937_call = mutated_mod.get_global_var('func_1937')
var_2198 = relay.var("var_2198", dtype = "float32", shape = ())#candidate|2198|()|var|float32
var_2199 = relay.var("var_2199", dtype = "float32", shape = (1089,))#candidate|2199|(1089,)|var|float32
call_2197 = relay.TupleGetItem(func_1933_call(relay.reshape(var_2198.astype('float32'), []), relay.reshape(var_2199.astype('float32'), [1089,]), ), 6)
call_2200 = relay.TupleGetItem(func_1937_call(relay.reshape(var_2198.astype('float32'), []), relay.reshape(var_2199.astype('float32'), [1089,]), ), 6)
func_1233_call = mod.get_global_var('func_1233')
func_1236_call = mutated_mod.get_global_var('func_1236')
const_2207 = relay.const([[-0.396727,1.732769,-5.552789,8.445195,7.522441,2.260944,-2.935990,4.721831,2.038760,-0.843489],[1.856659,-8.978853,4.723721,-5.323870,-4.937057,-2.365893,-4.404222,-5.309416,1.298991,-9.379254],[8.759092,-5.491061,0.020199,-2.503614,4.771299,3.079334,6.846994,8.340158,4.375455,-1.662055],[-4.896184,-3.975123,-1.100585,6.257296,-7.509321,7.160375,1.711309,7.554573,9.678024,-0.328367],[2.885062,4.421722,0.447923,9.573547,-1.895938,-0.635355,-1.565822,-9.396571,1.190148,-1.261305],[0.950073,-6.637896,8.798645,-1.289792,8.149586,4.779607,-2.648074,1.105049,1.781037,-0.760773],[4.008849,-7.609373,0.619161,-2.180614,-3.880170,8.881962,-4.444697,2.754320,8.584048,-7.814476],[-8.266782,8.578894,-8.076287,-8.960318,6.377466,-8.751389,2.280675,-3.682237,6.049005,3.636484],[4.644425,8.207175,-3.279308,3.266287,-3.119249,0.594865,-3.229400,3.362792,5.760643,-7.193071],[-7.733375,6.756692,-3.449394,0.229765,8.454191,3.854904,5.782102,-2.575586,6.794201,4.925371],[-1.719766,-4.936929,-0.277902,5.995132,0.211740,-5.667877,-9.959501,9.123103,-4.618925,-6.149466],[-5.966467,-1.988146,0.604373,9.009112,1.419376,-2.432128,1.573350,-5.123593,2.270042,-2.650371],[5.253322,-8.590091,-0.301855,-9.185747,-7.110233,-4.289338,5.220926,-7.682345,-1.207345,0.107255],[9.743265,0.537746,3.423187,-6.060554,1.434088,5.973156,7.033461,2.486846,-0.133664,-0.558129],[-9.710491,3.179836,-9.183945,-7.795262,1.818177,-4.024394,-7.364299,-2.923447,6.672239,-6.610807],[1.609087,2.881057,7.559066,-5.565829,8.993240,7.396816,-9.801691,1.205188,-4.772612,7.378854],[5.764870,-0.129943,4.363755,2.514907,1.784139,4.724956,-5.449752,-6.401906,3.801418,8.881566],[3.730155,1.073419,9.817035,-9.847896,-2.325010,9.534445,5.491616,6.374907,-2.576543,6.279438],[-9.908712,-2.330467,-7.263020,8.993078,-6.282596,-0.128952,5.759556,4.740919,-8.335955,-5.366067],[5.794335,-5.925736,-6.783856,7.866655,3.462181,-1.079119,0.029144,-2.120057,8.188385,-6.960228],[-8.213515,-6.701953,-5.061709,-6.761065,4.571207,0.526020,-0.364419,-6.765598,-9.007140,-9.379352],[-1.594747,5.082261,3.629298,4.885634,0.653869,-2.831995,-6.918186,6.934467,-6.671667,0.417927],[7.082187,-4.062164,5.530990,-1.131283,-1.672405,8.229706,5.639050,3.334997,-7.254322,-7.283176],[-5.949269,5.677185,7.276949,7.973416,-1.576957,8.963180,1.592253,8.485936,-7.728546,-7.461852]], dtype = "float32")#candidate|2207|(24, 10)|const|float32
var_2208 = relay.var("var_2208", dtype = "float32", shape = (132, 12))#candidate|2208|(132, 12)|var|float32
call_2206 = relay.TupleGetItem(func_1233_call(relay.reshape(const_2207.astype('float32'), [10, 8, 3]), relay.reshape(var_2208.astype('float32'), [1584,]), ), 1)
call_2209 = relay.TupleGetItem(func_1236_call(relay.reshape(const_2207.astype('float32'), [10, 8, 3]), relay.reshape(var_2208.astype('float32'), [1584,]), ), 1)
uop_2210 = relay.erf(bop_2189.astype('float32')) # shape=(6, 16, 11)
uop_2212 = relay.erf(bop_2192.astype('float32')) # shape=(6, 16, 11)
func_1857_call = mod.get_global_var('func_1857')
func_1859_call = mutated_mod.get_global_var('func_1859')
call_2221 = relay.TupleGetItem(func_1857_call(relay.reshape(call_2197.astype('uint32'), [420,])), 1)
call_2222 = relay.TupleGetItem(func_1859_call(relay.reshape(call_2197.astype('uint32'), [420,])), 1)
output = relay.Tuple([call_2197,var_2198,var_2199,call_2206,const_2207,var_2208,uop_2210,call_2221,])
output2 = relay.Tuple([call_2200,var_2198,var_2199,call_2209,const_2207,var_2208,uop_2212,call_2222,])
func_2225 = relay.Function([var_2188,var_2198,var_2199,var_2208,], output)
mod['func_2225'] = func_2225
mod = relay.transform.InferType()(mod)
mutated_mod['func_2225'] = func_2225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2225_call = mutated_mod.get_global_var('func_2225')
var_2227 = relay.var("var_2227", dtype = "float32", shape = (6, 16, 11))#candidate|2227|(6, 16, 11)|var|float32
var_2228 = relay.var("var_2228", dtype = "float32", shape = ())#candidate|2228|()|var|float32
var_2229 = relay.var("var_2229", dtype = "float32", shape = (1089,))#candidate|2229|(1089,)|var|float32
var_2230 = relay.var("var_2230", dtype = "float32", shape = (132, 12))#candidate|2230|(132, 12)|var|float32
call_2226 = func_2225_call(var_2227,var_2228,var_2229,var_2230,)
output = call_2226
func_2231 = relay.Function([var_2227,var_2228,var_2229,var_2230,], output)
mutated_mod['func_2231'] = func_2231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_2246 = relay.TupleGetItem(func_1705_call(), 0)
call_2247 = relay.TupleGetItem(func_1707_call(), 0)
var_2278 = relay.var("var_2278", dtype = "float32", shape = (6, 16, 11))#candidate|2278|(6, 16, 11)|var|float32
bop_2279 = relay.logical_xor(call_2246.astype('int32'), relay.reshape(var_2278.astype('int32'), relay.shape_of(call_2246))) # shape=(6, 16, 11)
bop_2282 = relay.logical_xor(call_2247.astype('int32'), relay.reshape(var_2278.astype('int32'), relay.shape_of(call_2247))) # shape=(6, 16, 11)
output = relay.Tuple([bop_2279,])
output2 = relay.Tuple([bop_2282,])
func_2292 = relay.Function([var_2278,], output)
mod['func_2292'] = func_2292
mod = relay.transform.InferType()(mod)
mutated_mod['func_2292'] = func_2292
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2293 = relay.var("var_2293", dtype = "float32", shape = (6, 16, 11))#candidate|2293|(6, 16, 11)|var|float32
func_2292_call = mutated_mod.get_global_var('func_2292')
call_2294 = func_2292_call(var_2293)
output = call_2294
func_2295 = relay.Function([var_2293], output)
mutated_mod['func_2295'] = func_2295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2322 = relay.var("var_2322", dtype = "float32", shape = (5, 3, 9))#candidate|2322|(5, 3, 9)|var|float32
var_2323 = relay.var("var_2323", dtype = "float32", shape = (5, 3, 9))#candidate|2323|(5, 3, 9)|var|float32
bop_2324 = relay.power(var_2322.astype('float32'), relay.reshape(var_2323.astype('float32'), relay.shape_of(var_2322))) # shape=(5, 3, 9)
output = bop_2324
output2 = bop_2324
func_2330 = relay.Function([var_2322,var_2323,], output)
mod['func_2330'] = func_2330
mod = relay.transform.InferType()(mod)
var_2331 = relay.var("var_2331", dtype = "float32", shape = (5, 3, 9))#candidate|2331|(5, 3, 9)|var|float32
var_2332 = relay.var("var_2332", dtype = "float32", shape = (5, 3, 9))#candidate|2332|(5, 3, 9)|var|float32
output = func_2330(var_2331,var_2332,)
func_2333 = relay.Function([var_2331,var_2332,], output)
mutated_mod['func_2333'] = func_2333
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_2343 = relay.TupleGetItem(func_1643_call(), 0)
call_2344 = relay.TupleGetItem(func_1644_call(), 0)
func_2330_call = mod.get_global_var('func_2330')
func_2333_call = mutated_mod.get_global_var('func_2333')
var_2356 = relay.var("var_2356", dtype = "float32", shape = (135,))#candidate|2356|(135,)|var|float32
call_2355 = func_2330_call(relay.reshape(var_2356.astype('float32'), [5, 3, 9]), relay.reshape(var_2356.astype('float32'), [5, 3, 9]), )
call_2357 = func_2330_call(relay.reshape(var_2356.astype('float32'), [5, 3, 9]), relay.reshape(var_2356.astype('float32'), [5, 3, 9]), )
func_1302_call = mod.get_global_var('func_1302')
func_1305_call = mutated_mod.get_global_var('func_1305')
const_2367 = relay.const([[2.142082,-4.069978,-3.271594,-1.679480,0.220963,-8.707244,0.405460,5.246278,-3.018008,5.800225,8.668881,-7.718343,-9.823768,-4.465904,-5.596180,-0.800411,-1.687937,-7.714161,4.266581,4.931475,-8.988767,-7.894493,5.537357,-1.537856,-8.882769,-0.649321,3.814760,-0.371069,8.565080,-8.232613,-4.743118,3.840008,2.138778,8.657122,-4.174850,7.812245,1.855702,-5.069819,-8.591277,-9.970470,-1.817950,-4.834734,1.291720,-2.566365,4.047229,8.681188,7.473555,-6.599694,-1.730184,-7.286236,-2.884080,7.485007,1.551848,-8.712680,-5.418322,-9.793391,-0.097171,-9.140640,4.026073,-4.071913,0.236676,7.954252,-5.189957,2.200140,0.459424,3.853263,9.472861,0.612157,-0.213618,-8.175274,2.013518,-8.900256,1.648506,6.102513,1.662199,3.986517,8.222925,5.471419,-2.639392,-4.044938,-5.688769,-6.615082,-7.413974,-4.321322,1.936238,2.284670,9.403035,-6.564204,-8.679139,-7.430967,0.681576,-6.493639,-7.676995,-3.231490,-2.167720,-2.031182,-2.803283,9.354885,8.996598,-4.573033,-7.595791,6.883967,5.636972,5.469284]], dtype = "float64")#candidate|2367|(1, 104)|const|float64
call_2366 = func_1302_call(relay.reshape(const_2367.astype('float64'), [1, 8, 13]))
call_2368 = func_1302_call(relay.reshape(const_2367.astype('float64'), [1, 8, 13]))
func_351_call = mod.get_global_var('func_351')
func_356_call = mutated_mod.get_global_var('func_356')
const_2372 = relay.const(-3.419768, dtype = "float32")#candidate|2372|()|const|float32
var_2373 = relay.var("var_2373", dtype = "float32", shape = (1089,))#candidate|2373|(1089,)|var|float32
call_2371 = relay.TupleGetItem(func_351_call(relay.reshape(const_2372.astype('float32'), []), relay.reshape(var_2373.astype('float32'), [11, 9, 11]), relay.reshape(call_2343.astype('float64'), [1056,]), ), 3)
call_2374 = relay.TupleGetItem(func_356_call(relay.reshape(const_2372.astype('float32'), []), relay.reshape(var_2373.astype('float32'), [11, 9, 11]), relay.reshape(call_2343.astype('float64'), [1056,]), ), 3)
bop_2375 = relay.logical_xor(var_2373.astype('uint32'), const_2372.astype('uint32')) # shape=(1089,)
func_2330_call = mod.get_global_var('func_2330')
func_2333_call = mutated_mod.get_global_var('func_2333')
call_2388 = func_2330_call(relay.reshape(call_2355.astype('float32'), [5, 3, 9]), relay.reshape(var_2356.astype('float32'), [5, 3, 9]), )
call_2389 = func_2330_call(relay.reshape(call_2355.astype('float32'), [5, 3, 9]), relay.reshape(var_2356.astype('float32'), [5, 3, 9]), )
output = relay.Tuple([call_2343,call_2355,var_2356,call_2366,const_2367,call_2371,bop_2375,call_2388,])
output2 = relay.Tuple([call_2344,call_2357,var_2356,call_2368,const_2367,call_2374,bop_2375,call_2389,])
func_2390 = relay.Function([var_2356,var_2373,], output)
mod['func_2390'] = func_2390
mod = relay.transform.InferType()(mod)
var_2391 = relay.var("var_2391", dtype = "float32", shape = (135,))#candidate|2391|(135,)|var|float32
var_2392 = relay.var("var_2392", dtype = "float32", shape = (1089,))#candidate|2392|(1089,)|var|float32
output = func_2390(var_2391,var_2392,)
func_2393 = relay.Function([var_2391,var_2392,], output)
mutated_mod['func_2393'] = func_2393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_2428 = relay.TupleGetItem(func_1705_call(), 0)
call_2429 = relay.TupleGetItem(func_1707_call(), 0)
var_2449 = relay.var("var_2449", dtype = "float32", shape = (6, 16, 11))#candidate|2449|(6, 16, 11)|var|float32
bop_2450 = relay.power(call_2428.astype('float32'), relay.reshape(var_2449.astype('float32'), relay.shape_of(call_2428))) # shape=(6, 16, 11)
bop_2453 = relay.power(call_2429.astype('float32'), relay.reshape(var_2449.astype('float32'), relay.shape_of(call_2429))) # shape=(6, 16, 11)
func_2390_call = mod.get_global_var('func_2390')
func_2393_call = mutated_mod.get_global_var('func_2393')
var_2455 = relay.var("var_2455", dtype = "float32", shape = (135,))#candidate|2455|(135,)|var|float32
var_2456 = relay.var("var_2456", dtype = "float32", shape = (1089,))#candidate|2456|(1089,)|var|float32
call_2454 = relay.TupleGetItem(func_2390_call(relay.reshape(var_2455.astype('float32'), [135,]), relay.reshape(var_2456.astype('float32'), [1089,]), ), 4)
call_2457 = relay.TupleGetItem(func_2393_call(relay.reshape(var_2455.astype('float32'), [135,]), relay.reshape(var_2456.astype('float32'), [1089,]), ), 4)
output = relay.Tuple([bop_2450,call_2454,var_2455,var_2456,])
output2 = relay.Tuple([bop_2453,call_2457,var_2455,var_2456,])
func_2458 = relay.Function([var_2449,var_2455,var_2456,], output)
mod['func_2458'] = func_2458
mod = relay.transform.InferType()(mod)
mutated_mod['func_2458'] = func_2458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mutated_mod.get_global_var('func_2458')
var_2460 = relay.var("var_2460", dtype = "float32", shape = (6, 16, 11))#candidate|2460|(6, 16, 11)|var|float32
var_2461 = relay.var("var_2461", dtype = "float32", shape = (135,))#candidate|2461|(135,)|var|float32
var_2462 = relay.var("var_2462", dtype = "float32", shape = (1089,))#candidate|2462|(1089,)|var|float32
call_2459 = func_2458_call(var_2460,var_2461,var_2462,)
output = call_2459
func_2463 = relay.Function([var_2460,var_2461,var_2462,], output)
mutated_mod['func_2463'] = func_2463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_2465 = relay.TupleGetItem(func_1643_call(), 0)
call_2466 = relay.TupleGetItem(func_1644_call(), 0)
var_2471 = relay.var("var_2471", dtype = "float32", shape = (6, 16, 11))#candidate|2471|(6, 16, 11)|var|float32
bop_2472 = relay.mod(call_2465.astype('float32'), relay.reshape(var_2471.astype('float32'), relay.shape_of(call_2465))) # shape=(6, 16, 11)
bop_2475 = relay.mod(call_2466.astype('float32'), relay.reshape(var_2471.astype('float32'), relay.shape_of(call_2466))) # shape=(6, 16, 11)
output = bop_2472
output2 = bop_2475
func_2481 = relay.Function([var_2471,], output)
mod['func_2481'] = func_2481
mod = relay.transform.InferType()(mod)
var_2482 = relay.var("var_2482", dtype = "float32", shape = (6, 16, 11))#candidate|2482|(6, 16, 11)|var|float32
output = func_2481(var_2482)
func_2483 = relay.Function([var_2482], output)
mutated_mod['func_2483'] = func_2483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_2492 = func_2138_call()
call_2493 = func_2138_call()
output = relay.Tuple([call_2492,])
output2 = relay.Tuple([call_2493,])
func_2507 = relay.Function([], output)
mod['func_2507'] = func_2507
mod = relay.transform.InferType()(mod)
mutated_mod['func_2507'] = func_2507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2507_call = mutated_mod.get_global_var('func_2507')
call_2508 = func_2507_call()
output = call_2508
func_2509 = relay.Function([], output)
mutated_mod['func_2509'] = func_2509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_2560 = relay.TupleGetItem(func_1643_call(), 0)
call_2561 = relay.TupleGetItem(func_1644_call(), 0)
output = relay.Tuple([call_2560,])
output2 = relay.Tuple([call_2561,])
func_2562 = relay.Function([], output)
mod['func_2562'] = func_2562
mod = relay.transform.InferType()(mod)
output = func_2562()
func_2563 = relay.Function([], output)
mutated_mod['func_2563'] = func_2563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_2592 = relay.TupleGetItem(func_2562_call(), 0)
call_2593 = relay.TupleGetItem(func_2563_call(), 0)
func_1302_call = mod.get_global_var('func_1302')
func_1305_call = mutated_mod.get_global_var('func_1305')
var_2600 = relay.var("var_2600", dtype = "float64", shape = (52, 2))#candidate|2600|(52, 2)|var|float64
call_2599 = func_1302_call(relay.reshape(var_2600.astype('float64'), [1, 8, 13]))
call_2601 = func_1302_call(relay.reshape(var_2600.astype('float64'), [1, 8, 13]))
bop_2622 = relay.greater_equal(var_2600.astype('bool'), relay.reshape(call_2599.astype('bool'), relay.shape_of(var_2600))) # shape=(52, 2)
bop_2625 = relay.greater_equal(var_2600.astype('bool'), relay.reshape(call_2601.astype('bool'), relay.shape_of(var_2600))) # shape=(52, 2)
output = relay.Tuple([call_2592,bop_2622,])
output2 = relay.Tuple([call_2593,bop_2625,])
func_2627 = relay.Function([var_2600,], output)
mod['func_2627'] = func_2627
mod = relay.transform.InferType()(mod)
mutated_mod['func_2627'] = func_2627
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2628 = relay.var("var_2628", dtype = "float64", shape = (52, 2))#candidate|2628|(52, 2)|var|float64
func_2627_call = mutated_mod.get_global_var('func_2627')
call_2629 = func_2627_call(var_2628)
output = call_2629
func_2630 = relay.Function([var_2628], output)
mutated_mod['func_2630'] = func_2630
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_2667 = relay.TupleGetItem(func_1705_call(), 0)
call_2668 = relay.TupleGetItem(func_1707_call(), 0)
uop_2679 = relay.sqrt(call_2667.astype('float32')) # shape=(6, 16, 11)
uop_2681 = relay.sqrt(call_2668.astype('float32')) # shape=(6, 16, 11)
output = relay.Tuple([uop_2679,])
output2 = relay.Tuple([uop_2681,])
func_2686 = relay.Function([], output)
mod['func_2686'] = func_2686
mod = relay.transform.InferType()(mod)
output = func_2686()
func_2687 = relay.Function([], output)
mutated_mod['func_2687'] = func_2687
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_2698 = relay.TupleGetItem(func_1643_call(), 0)
call_2699 = relay.TupleGetItem(func_1644_call(), 0)
output = call_2698
output2 = call_2699
func_2701 = relay.Function([], output)
mod['func_2701'] = func_2701
mod = relay.transform.InferType()(mod)
output = func_2701()
func_2702 = relay.Function([], output)
mutated_mod['func_2702'] = func_2702
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2766 = relay.var("var_2766", dtype = "bool", shape = ())#candidate|2766|()|var|bool
var_2767 = relay.var("var_2767", dtype = "bool", shape = (2, 11, 12))#candidate|2767|(2, 11, 12)|var|bool
bop_2768 = relay.logical_or(var_2766.astype('bool'), var_2767.astype('bool')) # shape=(2, 11, 12)
output = relay.Tuple([bop_2768,])
output2 = relay.Tuple([bop_2768,])
func_2771 = relay.Function([var_2766,var_2767,], output)
mod['func_2771'] = func_2771
mod = relay.transform.InferType()(mod)
mutated_mod['func_2771'] = func_2771
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2771_call = mutated_mod.get_global_var('func_2771')
var_2773 = relay.var("var_2773", dtype = "bool", shape = ())#candidate|2773|()|var|bool
var_2774 = relay.var("var_2774", dtype = "bool", shape = (2, 11, 12))#candidate|2774|(2, 11, 12)|var|bool
call_2772 = func_2771_call(var_2773,var_2774,)
output = call_2772
func_2775 = relay.Function([var_2773,var_2774,], output)
mutated_mod['func_2775'] = func_2775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_2798 = relay.TupleGetItem(func_2562_call(), 0)
call_2799 = relay.TupleGetItem(func_2563_call(), 0)
const_2800 = relay.const([[[4.350294,-1.949589,-9.897919,8.002930,-0.132832,-5.140165,-3.170945,-7.751536,-4.496703,2.355360,1.210218],[-8.243658,2.806096,-5.901276,5.154648,-9.207833,-6.754692,0.887809,-2.758619,-3.865280,-0.740300,-9.659753],[-0.072955,9.703339,2.277858,8.017882,-8.450350,0.769529,-5.201448,-3.645629,7.304414,4.030805,7.638541],[-4.480581,6.815360,-8.541537,1.223022,2.471999,3.886007,8.597074,4.900917,3.996756,-5.892730,7.526435],[-2.224996,-8.495474,-2.687395,-9.410287,7.609519,-4.805950,6.281686,-5.046154,9.348651,3.478775,9.679310],[5.070731,4.597139,-6.533693,4.966958,-5.169970,-9.198967,-7.393549,-0.581624,-2.016518,8.573850,8.052208],[-2.465820,-5.082419,4.626490,-8.418900,-2.739310,7.550410,9.866953,9.233717,-7.929061,-2.172676,1.877872],[6.920809,5.226830,9.680780,-9.158954,-0.698971,-4.772915,9.252599,-0.241821,-8.883604,3.794055,-7.323540],[-9.320317,-0.620415,9.844523,9.917827,6.249218,5.250417,-4.357653,7.794047,2.318065,2.634556,-2.643279],[3.933465,1.075923,9.786805,6.801410,4.783353,-4.277365,-0.733319,-9.335128,-2.787418,9.007820,0.553527],[-5.482762,-3.303859,-4.340289,0.270407,-6.996097,0.348461,6.922416,7.893266,-0.667428,-7.082971,-1.932597],[-4.324497,-0.773653,-1.030200,-0.076209,4.845072,-1.891385,-7.750892,-4.815155,-7.758222,-8.392749,-4.963157],[-9.850827,0.866417,-4.722612,7.692854,-7.407767,2.156073,-2.704710,-9.809837,1.793148,2.307460,-7.342731],[-7.026517,-6.875063,5.527921,-4.112759,-9.501738,3.364212,9.340148,5.524263,-5.191378,1.970426,-1.149868],[6.084704,-8.001356,-6.365048,6.941483,-9.866624,4.683307,-0.794503,9.285672,-1.866770,3.497558,8.013877],[7.176664,-2.625707,7.091620,-1.062329,7.015893,-4.785368,-9.106337,-7.385117,1.529532,-7.579448,6.643693]],[[-4.329093,6.742052,-3.926992,-4.336614,-9.993247,-8.988128,-2.175120,-1.260476,3.300981,-6.788862,1.970342],[-6.474260,-0.604465,-5.090028,4.051511,0.088929,5.420548,-2.953632,-2.387473,2.252229,4.236649,7.005981],[3.227296,-0.783640,5.869997,6.186957,9.891907,-9.519525,8.249010,-8.785893,-6.070682,-1.718895,7.427468],[9.170108,-7.467454,-6.905911,-6.135987,3.944814,8.247349,-5.889747,-8.770545,8.666993,-5.783801,-0.566353],[1.448085,-4.997303,-1.839875,5.480731,0.885199,2.055520,1.137183,6.533439,9.171898,-7.500765,-6.805759],[-7.603507,-4.550909,0.300676,5.582827,-3.797073,-6.765623,8.600692,-6.209029,-7.091259,5.341172,1.502960],[9.060781,6.408676,4.169549,8.741808,-2.259891,-3.994400,-9.962238,3.435552,8.195478,-3.482399,-3.139055],[0.440508,-0.530106,5.662966,3.681882,-6.823435,5.491512,-5.190918,3.438524,1.012571,4.629270,-9.258191],[0.992726,6.080145,-2.259508,-0.397727,1.686900,0.534872,-3.741251,-9.787588,5.747527,-3.699594,-9.591890],[0.033001,9.648083,6.281355,-5.344725,-6.709846,-9.441153,8.964263,3.286200,2.854932,6.383329,-7.303759],[6.638454,8.084271,5.233277,-5.817720,-0.817173,-0.760161,-0.356119,-3.498705,5.927023,-7.815485,7.599470],[-1.779694,6.401482,5.929573,-4.500224,-1.630577,-1.602672,-1.314180,-7.354160,9.967420,-3.234330,-2.949935],[-7.358455,-2.428696,9.432209,7.348374,-9.438152,6.887408,4.768848,-8.250096,-3.522616,-2.641646,-7.338171],[-9.192556,5.298984,-0.314052,9.147475,-7.545441,1.487517,-7.007610,3.812062,0.877010,0.428789,1.491822],[-6.368156,1.452731,8.987351,3.378808,-1.645507,-5.840634,-3.527808,-2.831589,7.533056,3.547988,7.625151],[6.838367,1.292197,-2.585302,3.079540,3.520875,0.868185,-5.679106,-5.260390,-5.311260,8.535845,-3.212480]],[[5.167464,-1.069353,9.682002,-2.196402,2.823653,5.007126,-8.149729,6.658061,-1.738056,3.455675,9.802014],[-3.404187,-6.074690,2.126627,4.165176,9.119934,-1.523081,7.842013,7.755183,-3.314509,3.187004,8.853553],[2.468527,3.791104,2.597606,2.955557,-1.846969,3.737816,-5.975658,-0.521360,-6.506691,7.030449,1.582043],[7.001188,-8.106009,0.738248,3.301518,0.485817,-5.864784,-8.618524,-1.674877,-7.118346,4.900276,3.113413],[-0.326274,1.097990,5.649178,6.899570,3.871783,7.949401,-5.933137,1.454471,9.530598,-6.979595,4.917148],[4.212834,-4.299105,-5.472310,7.873993,-2.814346,-8.677892,1.435856,-0.126082,-5.096200,9.186844,4.849873],[6.324466,4.567625,4.852518,-4.064976,6.554569,-8.981330,3.271973,3.988816,-2.951124,2.513934,-4.243454],[-7.772101,1.638926,-9.367912,-5.775678,3.869951,1.724243,-6.519110,-8.895552,9.488835,4.700360,-5.435006],[4.421322,1.284915,3.806457,-3.360043,9.509906,-1.532479,5.002444,9.870234,-7.076105,3.711610,-2.021306],[-6.622996,-0.208792,-9.294962,-0.602390,1.190349,-1.180322,9.108865,6.654277,1.534584,8.131141,1.292818],[1.717727,-2.579812,4.251252,9.872515,-2.881500,7.592291,9.696084,-4.108886,-1.911615,0.331525,-3.418545],[-4.119294,-9.175521,2.849259,0.744133,6.358675,6.504570,-6.556867,2.788261,-1.790488,9.921197,6.737870],[5.626379,-1.752910,6.967141,0.328779,0.489028,7.704723,4.292777,4.508742,2.453207,2.898475,-2.069760],[-5.783071,0.796683,0.793323,-2.235002,-4.390391,-0.083390,8.248814,-0.123746,-7.373895,-0.964435,-9.583274],[-6.588090,-5.384324,-6.110921,-1.425822,9.823136,-0.883283,-1.604861,0.760418,-2.740604,-3.086773,0.479817],[-0.334306,-0.246572,4.767222,-9.304294,2.581966,9.871957,3.876182,3.711264,-1.709523,-3.843776,-2.303521]],[[8.888494,7.223690,6.104621,-9.206329,4.072501,-3.547361,6.138122,-0.679385,4.497482,-7.842003,4.825271],[-3.680133,-0.692025,7.336017,-4.144734,0.080623,9.944053,9.883395,-9.263162,1.935588,8.676393,-6.814027],[8.286114,-7.692246,-1.149279,1.369849,-3.971126,-1.690804,4.609220,1.871508,1.082911,3.477396,3.510636],[0.407353,-5.870876,5.708170,1.037077,7.686369,-5.242229,4.356701,-7.221404,-6.007323,9.940447,6.891593],[-2.115978,-5.204455,0.654661,3.982636,-3.916177,4.339153,2.318555,-5.390207,-0.179575,-2.904464,-1.508232],[8.405285,-2.825481,8.837604,-9.392736,-7.132799,-7.034955,4.016503,-5.123142,-0.089226,4.915773,-6.962218],[6.501542,2.153135,-0.931675,-9.971233,-6.739908,4.684784,-3.501039,-2.003192,-9.507105,9.419038,1.978939],[-2.854874,4.404673,-3.977812,-5.791102,-6.001777,-3.795210,3.490383,6.467767,9.453366,3.657951,-2.074876],[5.377366,3.821487,-5.546741,-4.628846,9.211021,4.759784,-0.175586,3.746237,-9.854411,-6.074110,-3.402671],[9.454632,2.662467,6.208822,-0.591889,-2.274326,-9.062495,6.205112,6.788313,-5.560699,-7.789259,1.345878],[2.625029,-2.276429,-3.190392,-4.789013,-7.666248,-1.079027,-3.563891,1.756408,-2.189074,9.866792,6.413367],[1.446124,-1.616917,8.612259,7.505601,1.656595,5.282753,7.289793,-3.647540,-2.669896,3.445271,3.953356],[-6.117060,-7.505063,-3.708959,9.007157,-1.867054,-1.949517,-4.763669,-0.978344,7.633915,2.775909,6.342123],[-4.246667,-6.305251,-3.762399,-0.277816,-0.988181,-9.368940,4.386412,-6.997546,-3.394904,5.908424,8.022887],[-1.213732,7.329343,-1.024879,6.030310,4.320874,2.643306,-0.817643,-1.662248,6.514294,-4.164735,2.336780],[1.807859,-8.584161,9.851070,-6.954089,-4.411032,-9.859699,-5.474279,-4.650007,-9.728506,-2.764768,6.672972]],[[0.981555,3.801633,-8.351571,2.255351,5.126523,2.119758,-5.140693,7.370314,-0.933333,-5.175163,1.367752],[7.544444,-9.558175,-9.744392,9.490707,1.710824,3.932276,-7.585315,-6.626307,9.181793,-1.284275,-6.772233],[3.331087,5.223133,2.922456,-7.740541,1.251025,-8.753967,6.906528,-3.625102,-0.341582,-4.817853,-0.712692],[-3.313478,-9.712993,-7.213611,-7.827576,4.588006,-2.294651,3.989686,-0.633595,-8.584854,8.042404,4.694681],[7.869537,-5.897523,-5.544571,0.701881,4.781460,2.071911,-2.992528,-9.609000,-0.022632,-1.968965,-7.445477],[-7.476325,-8.380897,-1.149426,3.310247,-3.337036,2.633623,9.538206,7.232724,-4.098562,-6.890562,-1.807360],[1.881346,0.766755,1.051350,-7.472398,-8.434697,-1.493956,-2.148280,-6.229949,1.199461,-1.870377,5.116565],[-9.074822,2.271530,8.481985,-7.545262,-4.115898,-6.753359,-4.324780,3.763288,-3.184355,9.632239,-9.060273],[2.475706,-3.097730,-8.951469,-8.165983,-1.887295,-2.591762,6.032417,4.499284,-9.360465,-0.422040,2.673244],[-6.109363,8.383430,-3.463498,8.418390,-8.268096,-3.519762,6.185009,-6.528339,-7.592305,-8.187529,-3.751616],[8.594127,-8.015311,8.203110,-1.322058,0.674842,2.974591,4.108482,9.501468,0.672590,-6.761073,-5.602961],[-5.302309,2.228366,1.359554,2.890618,4.990950,8.925262,-6.851449,-3.078472,-6.376612,5.114857,1.305365],[8.446398,-5.370158,-8.814239,-1.955027,-9.167682,9.793202,-9.459241,-2.972123,-3.117334,-1.073936,4.833987],[-8.628496,5.234037,0.339263,5.291793,-8.538398,1.021230,1.687504,0.281002,5.772929,-2.054260,3.142311],[6.282162,-7.685442,4.520547,-0.283709,-3.092904,2.451778,7.172150,-9.939357,7.595922,0.596463,7.298847],[-6.837946,7.553711,7.307657,4.876441,-1.975151,-2.045014,-3.841849,8.921376,-9.177093,-2.658388,9.983256]],[[-3.143352,-6.653997,-7.468475,-5.466703,-3.708890,-4.361291,-4.636002,9.897932,-5.681613,2.091107,-4.959821],[5.847971,-5.856774,7.951476,9.634302,-1.899410,9.286586,3.049576,-6.970898,7.533127,-0.296314,-9.590549],[1.492095,-7.351088,1.363444,-6.187057,-4.105758,3.635251,6.072732,1.335279,-5.913930,-0.395121,-9.875541],[3.739287,-0.210125,5.708634,3.334992,6.559143,6.150838,-1.566170,7.759074,-6.315383,-1.833369,-4.889939],[0.987419,-9.276890,4.770005,2.103877,-8.412844,0.796228,7.809166,-9.475258,-0.202370,-2.343886,0.223917],[1.363060,1.860778,-7.485966,3.108607,-2.997470,-7.969633,-0.765407,5.639878,0.133060,3.961997,-2.522135],[7.963957,1.159086,9.841775,4.687033,-9.251995,3.038321,0.033517,-5.447832,0.054623,5.609360,0.775813],[1.700042,6.191163,2.854356,6.872526,7.179139,-6.188432,2.335082,-1.278293,-2.946622,1.693409,7.881117],[-6.224961,2.182540,-4.677637,4.797910,1.825103,-0.807658,-4.406561,3.226220,-5.734727,-4.003246,5.209482],[-8.935692,3.833738,-5.518975,-4.903905,0.462123,8.041723,-2.018776,0.310051,-9.286099,2.096730,4.359719],[-6.901569,7.947454,3.708955,9.665251,0.646252,1.662107,-3.021884,5.073876,0.168323,5.415103,-0.573743],[-6.840634,-6.805771,-6.814952,7.817435,0.582735,-9.111291,-3.436260,-1.520709,-2.494172,8.294507,-7.587257],[8.362086,2.880752,-7.235696,-0.367021,-2.863347,-2.677888,2.169438,-2.064405,-2.239259,-8.616989,6.015104],[6.423895,-3.951692,3.552043,1.877567,1.434307,-4.977096,7.045060,-2.421046,7.647760,-7.147189,0.576322],[-8.518915,-2.384688,3.555876,3.681627,-2.528426,-7.218893,-3.540279,-8.714084,-2.981451,-4.498705,-6.804556],[8.656151,1.948834,-8.212772,7.634724,0.157020,1.384910,-7.438337,-7.238780,1.830574,-5.765830,6.928715]]], dtype = "float32")#candidate|2800|(6, 16, 11)|const|float32
bop_2801 = relay.greater_equal(call_2798.astype('bool'), relay.reshape(const_2800.astype('bool'), relay.shape_of(call_2798))) # shape=(6, 16, 11)
bop_2804 = relay.greater_equal(call_2799.astype('bool'), relay.reshape(const_2800.astype('bool'), relay.shape_of(call_2799))) # shape=(6, 16, 11)
func_2771_call = mod.get_global_var('func_2771')
func_2775_call = mutated_mod.get_global_var('func_2775')
var_2806 = relay.var("var_2806", dtype = "bool", shape = ())#candidate|2806|()|var|bool
const_2807 = relay.const([False,False,True,False,False,True,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,True,False], dtype = "bool")#candidate|2807|(264,)|const|bool
call_2805 = relay.TupleGetItem(func_2771_call(relay.reshape(var_2806.astype('bool'), []), relay.reshape(const_2807.astype('bool'), [2, 11, 12]), ), 0)
call_2808 = relay.TupleGetItem(func_2775_call(relay.reshape(var_2806.astype('bool'), []), relay.reshape(const_2807.astype('bool'), [2, 11, 12]), ), 0)
output = relay.Tuple([bop_2801,call_2805,var_2806,const_2807,])
output2 = relay.Tuple([bop_2804,call_2808,var_2806,const_2807,])
func_2813 = relay.Function([var_2806,], output)
mod['func_2813'] = func_2813
mod = relay.transform.InferType()(mod)
var_2814 = relay.var("var_2814", dtype = "bool", shape = ())#candidate|2814|()|var|bool
output = func_2813(var_2814)
func_2815 = relay.Function([var_2814], output)
mutated_mod['func_2815'] = func_2815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_2847 = relay.TupleGetItem(func_1705_call(), 0)
call_2848 = relay.TupleGetItem(func_1707_call(), 0)
output = call_2847
output2 = call_2848
func_2871 = relay.Function([], output)
mod['func_2871'] = func_2871
mod = relay.transform.InferType()(mod)
mutated_mod['func_2871'] = func_2871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2871_call = mutated_mod.get_global_var('func_2871')
call_2872 = func_2871_call()
output = call_2872
func_2873 = relay.Function([], output)
mutated_mod['func_2873'] = func_2873
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2871_call = mod.get_global_var('func_2871')
func_2873_call = mutated_mod.get_global_var('func_2873')
call_2874 = func_2871_call()
call_2875 = func_2871_call()
func_1933_call = mod.get_global_var('func_1933')
func_1937_call = mutated_mod.get_global_var('func_1937')
var_2915 = relay.var("var_2915", dtype = "float32", shape = ())#candidate|2915|()|var|float32
var_2916 = relay.var("var_2916", dtype = "float32", shape = (1089,))#candidate|2916|(1089,)|var|float32
call_2914 = relay.TupleGetItem(func_1933_call(relay.reshape(var_2915.astype('float32'), []), relay.reshape(var_2916.astype('float32'), [1089,]), ), 2)
call_2917 = relay.TupleGetItem(func_1937_call(relay.reshape(var_2915.astype('float32'), []), relay.reshape(var_2916.astype('float32'), [1089,]), ), 2)
func_2771_call = mod.get_global_var('func_2771')
func_2775_call = mutated_mod.get_global_var('func_2775')
const_2930 = relay.const([False,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|2930|(264,)|const|bool
call_2929 = relay.TupleGetItem(func_2771_call(relay.reshape(var_2915.astype('bool'), []), relay.reshape(const_2930.astype('bool'), [2, 11, 12]), ), 0)
call_2931 = relay.TupleGetItem(func_2775_call(relay.reshape(var_2915.astype('bool'), []), relay.reshape(const_2930.astype('bool'), [2, 11, 12]), ), 0)
uop_2945 = relay.atanh(call_2874.astype('float32')) # shape=(6, 16, 11)
uop_2947 = relay.atanh(call_2875.astype('float32')) # shape=(6, 16, 11)
output = relay.Tuple([call_2914,var_2915,var_2916,call_2929,const_2930,uop_2945,])
output2 = relay.Tuple([call_2917,var_2915,var_2916,call_2931,const_2930,uop_2947,])
func_2951 = relay.Function([var_2915,var_2916,], output)
mod['func_2951'] = func_2951
mod = relay.transform.InferType()(mod)
var_2952 = relay.var("var_2952", dtype = "float32", shape = ())#candidate|2952|()|var|float32
var_2953 = relay.var("var_2953", dtype = "float32", shape = (1089,))#candidate|2953|(1089,)|var|float32
output = func_2951(var_2952,var_2953,)
func_2954 = relay.Function([var_2952,var_2953,], output)
mutated_mod['func_2954'] = func_2954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_2964 = relay.TupleGetItem(func_1705_call(), 0)
call_2965 = relay.TupleGetItem(func_1707_call(), 0)
func_2701_call = mod.get_global_var('func_2701')
func_2702_call = mutated_mod.get_global_var('func_2702')
call_2976 = func_2701_call()
call_2977 = func_2701_call()
output = relay.Tuple([call_2964,call_2976,])
output2 = relay.Tuple([call_2965,call_2977,])
func_2978 = relay.Function([], output)
mod['func_2978'] = func_2978
mod = relay.transform.InferType()(mod)
mutated_mod['func_2978'] = func_2978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mutated_mod.get_global_var('func_2978')
call_2979 = func_2978_call()
output = call_2979
func_2980 = relay.Function([], output)
mutated_mod['func_2980'] = func_2980
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2686_call = mod.get_global_var('func_2686')
func_2687_call = mutated_mod.get_global_var('func_2687')
call_2997 = relay.TupleGetItem(func_2686_call(), 0)
call_2998 = relay.TupleGetItem(func_2687_call(), 0)
func_2330_call = mod.get_global_var('func_2330')
func_2333_call = mutated_mod.get_global_var('func_2333')
const_3003 = relay.const([-4.791968,1.511273,-7.976562,5.300760,0.834244,-6.667658,-1.194025,0.345849,-5.487397,-8.618079,-6.504312,9.000610,1.603800,-0.420805,-6.619999,7.000371,-3.067787,9.841299,-8.464804,-9.613674,-8.444988,-6.595393,-1.024733,7.161847,-6.409807,-9.898366,-7.934906,-7.970123,0.687543,-3.439000,-3.430249,-2.489856,6.375965,0.231544,5.329988,9.646359,-5.642025,-6.362885,2.009697,3.298713,1.685953,-3.134428,1.672070,2.367961,9.303556,-8.285301,-5.873661,0.289196,2.798634,1.273538,-4.306667,-0.989442,-3.541788,-3.616449,-9.589423,-2.568503,5.420919,6.801521,3.696754,6.835007,-9.135809,-5.732424,3.478734,-9.009160,-4.973423,1.439493,8.676637,-5.136730,-2.672239,4.552566,-4.407808,-4.634544,0.903476,7.764031,-3.485104,9.035894,-7.373565,1.464148,8.344771,-5.902289,-9.997772,6.499389,2.736696,0.501096,-8.262510,-2.665996,-4.083341,-6.385359,-7.152082,-8.035997,1.988022,-0.739552,0.034649,0.967756,9.188219,5.161812,5.063085,9.821535,-1.049578,-8.821035,-8.172858,4.433217,8.879715,-8.340411,7.681384,-7.905031,-4.159556,9.552828,3.942688,0.283928,-4.514312,-3.909364,3.616133,3.021573,-1.011234,-6.364218,-5.108197,-7.672728,4.244455,-1.671203,1.512378,3.916333,7.396388,-3.706023,6.602930,0.631371,-6.452998,4.953771,-1.750106,6.973879,-2.693137,3.872662,8.707311,-3.988267,-6.714345], dtype = "float32")#candidate|3003|(135,)|const|float32
call_3002 = func_2330_call(relay.reshape(const_3003.astype('float32'), [5, 3, 9]), relay.reshape(const_3003.astype('float32'), [5, 3, 9]), )
call_3004 = func_2330_call(relay.reshape(const_3003.astype('float32'), [5, 3, 9]), relay.reshape(const_3003.astype('float32'), [5, 3, 9]), )
func_1233_call = mod.get_global_var('func_1233')
func_1236_call = mutated_mod.get_global_var('func_1236')
var_3021 = relay.var("var_3021", dtype = "float32", shape = (24, 10))#candidate|3021|(24, 10)|var|float32
const_3022 = relay.const([-9.731433,9.669076,4.075994,6.640160,-3.115013,1.388434,-2.161008,-8.934737,-1.331742,-0.480549,5.169033,-2.196189,5.462896,5.991895,-5.558349,6.972796,-2.907894,2.338336,-2.469135,-4.106570,3.989562,-8.765377,7.898100,5.160094,8.415827,3.680540,2.213890,-9.758377,-1.016362,1.377371,7.810112,8.989880,4.302964,5.530121,0.273638,-5.394430,-3.579783,-9.531529,8.765961,5.746801,9.915518,2.289039,-2.419036,-7.212070,-4.572669,4.928686,-6.095001,4.604350,2.631269,-6.272740,-9.920313,3.264216,8.690697,-8.696754,-6.848234,-4.612200,4.722853,-6.200365,0.014261,-4.397823,-6.318634,-3.604341,-4.311911,-0.991601,-7.592502,9.465725,9.285446,4.336153,-0.100163,9.692637,5.755824,1.178165,-8.496035,-3.731622,-3.610581,0.387184,7.424694,4.926525,7.940640,3.565103,-8.060822,4.128750,-1.534379,8.690372,-5.832826,7.447958,-5.009781,-2.967511,-3.152935,-6.083929,6.684826,4.398285,0.528379,1.868935,-9.022246,7.776383,6.022566,-4.750213,5.986225,-3.069848,-1.045863,-7.440211,-0.621656,6.159372,1.188313,4.881582,3.977951,5.671114,-5.917666,-0.277938,-3.565152,7.557084,-7.591590,8.274578,5.213113,3.715899,6.840562,-3.492834,4.532692,-2.151412,-0.484306,2.731913,-2.148352,-5.926517,8.301852,8.204751,-9.749868,5.338714,-8.177866,1.673892,2.058071,7.713447,-1.280996,-9.882206,-5.079335,-9.298648,7.203675,-0.201565,3.673410,-6.295628,8.143111,-5.878541,-3.386404,-8.023350,-3.857429,9.692009,0.858677,-9.215680,-3.642502,4.554443,0.527226,8.149839,1.002617,-4.647759,1.157605,-5.451710,-5.987037,-6.498328,-3.354921,5.641042,-9.851668,-6.721845,8.451316,3.123262,-5.312096,-8.291471,2.945248,-4.882054,-6.745829,6.595947,5.963653,-0.670537,-6.555550,-7.879156,-5.881600,3.968808,-5.655547,-5.344008,-8.141012,-6.194734,-1.674650,-1.483816,-0.269762,-9.641961,1.402641,-9.970481,6.099866,-0.849504,-1.931893,3.348050,-4.071234,9.956975,-9.596339,-1.807352,-2.054255,9.493002,-1.881438,-3.668372,-8.740813,5.717932,-0.708106,-3.766707,-3.287049,6.365246,-6.111133,5.714979,0.648074,9.300594,-0.026882,-0.770959,-3.758181,2.992283,4.428228,-7.764616,3.343470,4.700811,5.650638,0.241428,-6.964946,-1.947097,2.832720,4.972954,1.544332,9.645755,-7.287419,-6.405645,6.927056,5.370481,2.459100,4.149188,9.425394,-9.065671,-2.069411,2.157984,-2.809647,5.050756,0.392004,-7.922813,-7.981267,7.857092,6.051632,2.180046,5.722849,1.139637,-1.976401,1.051532,4.583622,4.409023,-6.110951,-3.728880,-3.970744,-3.076450,-1.855367,-6.791982,-2.579623,9.159767,6.445101,8.768595,-4.935763,1.730598,0.040295,-5.627807,-0.920575,-0.963055,-6.095187,7.827472,1.282644,9.858587,-6.458295,-1.900972,0.931665,-8.287731,-5.422006,1.216754,-1.089485,-1.667045,-5.942015,-2.604768,-1.118737,9.465092,2.743814,0.224616,-1.771805,-3.558365,0.056621,-0.933126,1.601560,3.205689,-9.156563,-9.530403,-6.778084,-0.439936,6.720111,2.367996,5.825794,9.125933,-2.032960,0.027011,0.867114,6.709540,-6.539008,9.314339,5.431391,-5.363026,8.385906,-7.361565,7.235824,-9.184237,-0.538613,-0.450330,-2.603457,-2.290549,-6.079827,-5.702054,-1.994004,-0.701137,5.503958,-7.643507,3.975108,-4.907607,6.712538,-1.214380,9.297516,2.705823,-5.472782,8.723914,4.297035,9.390967,-1.965292,6.302144,-6.220244,0.190227,5.304049,-0.425233,-5.015460,-3.365911,3.409184,-9.249155,0.883938,-1.482960,0.337561,6.484992,-2.284271,6.532320,-2.350286,6.645618,-6.238758,-5.819039,-9.836085,-7.033853,4.814600,-2.275173,6.061460,8.840309,-2.371413,5.915476,4.115491,1.808023,0.396248,-7.662260,3.133723,-7.224680,1.653813,-4.902238,8.012518,-9.298021,6.158199,-1.718190,-8.276982,4.213556,9.595621,-3.412876,2.665926,-7.232174,-3.680353,-1.776831,-3.192354,-0.203110,7.487608,5.697981,3.994090,6.864720,-8.363066,-8.914367,8.210133,-3.246257,-4.739533,-5.758380,-2.164283,-5.954024,2.105993,-1.328186,-3.066490,6.626501,2.066768,-2.002698,3.703303,4.411858,6.528807,-9.971694,-5.674238,-4.040857,7.140495,-0.924231,5.536442,5.040050,-5.171202,2.172044,-5.768360,-1.976673,9.229118,-8.093265,1.369611,5.634268,6.925420,1.803829,-7.682211,-4.978064,-1.456115,4.657895,-3.269834,6.995323,-1.895437,1.375920,1.810439,2.357246,-5.251123,8.298121,7.096802,2.646593,-3.803322,-2.805420,-9.271523,6.697195,-5.937994,-0.794066,2.791861,7.415905,-8.505712,-8.165627,-3.472126,8.180237,8.315038,-0.678249,0.188317,-6.940135,9.721131,-5.425776,1.020387,-9.696502,-3.052665,-0.900629,-5.815237,8.842941,-4.126853,2.656087,5.185528,-8.075098,5.413241,-2.561520,-2.493206,4.444768,0.535272,1.157226,6.684999,-8.277409,-5.862132,7.820744,-7.007256,-6.591316,-9.942563,-5.582513,-2.101753,-8.321111,7.381124,-7.571991,8.345448,5.243561,6.962459,-8.776534,8.150792,-7.036091,6.451286,-6.724019,-9.534021,1.845932,-6.480492,2.000004,-4.773591,0.040808,-2.250930,4.776762,8.855235,-0.721833,7.697998,5.245782,-8.296908,-0.852439,6.311854,3.222199,5.025444,-0.098034,-3.655972,-5.712766,2.230150,3.011699,0.511586,-2.668744,5.462884,3.925086,8.437972,3.528199,-7.563943,4.360732,7.315100,-0.587303,4.359707,-6.764861,-0.311054,-2.819178,-8.321316,9.855294,-0.572073,-6.368338,-0.725300,-5.280280,-7.137342,1.529236,-8.887819,-3.593972,-9.103376,-2.842619,1.067947,9.330481,-5.700294,-4.419762,4.190159,-9.380824,6.116968,-8.861575,3.530234,3.285662,-1.440110,-4.263025,6.904850,-0.813405,4.148225,-9.405495,-1.818008,-8.030642,9.158751,2.775780,-9.310375,7.097235,3.585752,-6.920733,-4.455429,-3.677754,-9.912992,1.123826,-2.528776,4.209730,1.549413,-5.723628,-5.036235,-9.212552,2.651184,-3.275798,0.510942,5.525977,1.314519,5.352836,2.522444,3.878737,6.003638,-4.732247,-6.550967,6.221093,1.086346,3.988180,7.566545,0.052117,-9.896973,-4.751168,4.974842,-7.161915,9.103174,2.165770,5.344797,1.712045,6.811910,-1.607239,9.862680,8.329556,-3.431024,-7.196296,-6.518675,-0.291160,-6.812779,6.555983,5.505169,-2.923415,4.833930,3.523369,-2.961226,9.503700,-1.780401,-2.361525,-2.776173,-5.552402,-3.858140,-8.773819,7.523278,9.805722,3.317511,3.670213,-5.981250,-1.757224,0.994700,9.735449,-8.453310,-8.665720,-1.849614,-2.100826,-9.361247,0.074323,-0.035723,-1.808023,9.843742,8.050183,-8.600989,0.455713,-6.142698,-6.769645,7.503216,-7.350458,5.608178,7.429401,9.706143,-3.663098,-1.190213,-3.243480,0.665634,-8.534021,7.311949,6.186722,7.501040,-7.466894,-4.181670,9.047087,-7.390758,9.031938,-0.493479,-7.536751,4.194219,-5.113173,-5.693228,-1.722806,7.818915,-1.764154,-4.139224,-4.371472,-1.276673,6.285101,9.281036,9.482107,-1.282489,8.038354,1.530808,-7.939961,-0.067062,-2.556533,-6.114409,-7.814901,-7.913935,-0.505538,9.929372,-7.507777,0.657680,-3.095023,-0.718511,1.177515,8.250141,-3.832790,-1.332617,2.664160,3.016848,1.186928,-4.618100,9.734993,5.854573,4.861667,-3.504108,-9.767319,8.225709,-3.213706,-5.145068,2.471761,8.497038,-8.647474,-5.914944,-7.332004,-2.159529,5.792474,-2.282957,8.920643,-7.121557,-1.770740,-0.216088,0.099306,0.186666,6.394450,0.821752,5.376952,-1.511581,-8.517743,2.710143,-3.142076,-2.842361,-2.995986,-8.340718,-5.279772,-3.252207,2.896374,-2.348241,1.605676,0.750542,4.919093,0.770098,2.355803,2.630465,-5.132551,-7.607608,-0.238207,0.680208,0.486601,-1.599509,-7.875546,-5.045378,2.925831,-2.931752,8.132775,0.349734,-2.536698,1.054828,4.477285,4.374176,-1.208469,-8.675874,2.417218,9.969314,-3.811787,-2.586944,9.668780,-2.534976,9.701517,3.332900,-6.421528,-5.490631,0.213549,-6.912537,-7.524642,-0.830509,-7.355816,4.761725,-1.603247,-5.771769,-4.550910,-1.535811,-3.893447,-8.543994,1.980874,-1.356829,-9.129635,9.480520,-8.327509,-5.127035,4.737015,6.928685,-5.451670,9.799763,-9.976679,6.052946,9.877479,-6.505509,-6.193690,4.216065,-3.747701,-0.184165,-0.802892,-5.986980,4.605664,6.562313,2.408681,-9.982026,7.771125,5.434812,-1.350765,-1.130195,-7.204148,7.470508,3.255534,-2.706612,-6.906954,4.184795,-4.764382,8.910663,-0.703755,3.807897,-2.339121,3.947093,6.271380,5.301633,0.198939,5.569543,-7.276208,1.805048,-5.184622,1.226097,-3.194525,5.666618,-4.792766,-6.225558,-2.282120,-4.376792,-5.970314,-2.073162,-7.693665,2.619148,-9.415429,6.768745,4.212968,-4.578645,5.866850,-5.735394,-5.245959,-1.377883,-8.705161,-2.940165,-5.892136,8.012587,-3.743217,9.845447,7.076870,8.214643,5.259439,-6.622414,6.406652,-6.798066,-0.142814,-6.915750,7.405311,7.633318,2.278964,-3.826774,9.635714,-0.374972,4.757614,-4.873276,-6.488731,-2.819057,1.631349,-2.553955,-0.151745,2.734190,3.410280,1.253253,-0.186432,0.038581,-0.835124,-6.053204,7.414440,-0.848899,-1.520495,-1.312865,-3.108004,-9.584293,8.785197,-4.914466,-2.444358,9.574665,3.210197,-9.832061,3.420602,9.390980,2.785744,2.751962,9.795228,7.797447,4.019594,-0.384664,2.360825,4.276153,-6.974916,-2.590094,9.201283,-0.843008,-1.740623,-3.097329,-5.952824,-8.206489,7.450416,5.647929,0.331007,-1.417441,-0.200639,-1.638475,-9.980034,-8.310166,1.354456,3.616597,-4.986153,9.094346,-9.842106,7.421324,7.458333,-1.864512,0.359883,6.311184,-7.208516,3.359195,9.190364,-0.833458,8.708169,-9.507099,8.432771,0.899024,0.931995,8.608100,2.671394,6.208059,-8.870279,3.719723,0.953470,-5.541659,8.998931,-4.078777,4.087914,-7.041758,8.705813,1.173762,-6.155759,2.109726,1.249801,3.772986,8.928892,7.918313,-2.168604,9.320319,-1.032645,8.199438,-6.366153,-5.380018,1.315734,-4.139592,9.233315,5.624777,1.211690,3.208774,3.928935,8.048997,1.855741,-0.488675,6.410267,4.826574,3.583006,6.250281,-8.160702,0.460702,-4.432277,8.766120,4.922025,9.526518,5.844106,5.702020,5.257122,1.326045,-8.456296,-8.585566,9.231077,6.927560,4.539410,-6.470749,-2.989001,8.127829,-3.667224,-0.667087,3.572737,-2.561349,-5.433590,-0.677320,-8.118687,7.962650,3.991827,-7.088896,9.317264,-3.223732,4.631355,6.546150,-8.000334,-2.901299,3.240107,6.621697,5.788654,7.588572,2.170318,3.097353,5.212558,-7.916356,9.018677,4.266559,-2.035177,3.082073,3.440551,1.066355,0.224310,-9.267753,-5.256874,8.922721,2.304234,-6.969683,-3.156668,-2.003451,-5.532270,2.261194,8.294770,-8.364931,-7.770473,9.161237,-6.638174,9.037153,5.653294,-6.556482,9.597195,9.459063,-8.718094,-5.370697,4.245948,-6.290725,5.567378,2.177991,2.090343,7.178739,3.687201,9.104589,1.674251,0.062795,-4.274654,1.544796,-4.945134,-5.344415,-2.213525,8.886456,2.261819,2.851275,1.588529,5.265609,-5.229046,-5.991101,-8.590014,-0.666464,7.475972,-3.888688,0.456305,9.319050,-9.221991,7.854264,-7.598952,-5.500337,-2.445572,9.629131,1.568796,-0.012938,2.535474,7.205944,-6.084262,6.997617,-1.412550,4.090762,8.505183,0.056832,-6.380754,-8.079105,9.311439,-8.211021,-3.674938,-0.083471,4.120971,-7.970267,5.297640,-6.901448,2.242594,4.441071,7.704779,9.040992,-0.562789,-2.984184,8.847320,7.772295,0.466546,4.661726,4.288432,0.544125,-1.251843,1.592841,-3.034624,-7.889692,-2.722342,1.168350,-4.414758,-5.681661,9.121100,-2.075285,-3.585125,2.947774,5.204933,0.294257,-8.387939,8.380695,-8.951937,4.602588,-8.576914,-0.050803,0.805884,-6.933706,3.691111,-8.893252,7.181248,6.335438,5.997837,-7.800557,7.484333,3.848399,-1.944740,9.167429,-2.645126,2.966160,-1.537713,6.152585,2.674906,9.018603,-0.151543,8.635447,-1.701470,1.154346,-3.768634,7.131054,-2.340549,9.375932,9.013979,5.063799,6.705695,4.656634,9.248111,-8.019730,-8.105481,2.363405,2.419162,9.088668,9.242320,6.701524,-8.564472,-7.222292,-2.389745,2.735367,-8.306545,4.108357,-9.151639,7.076848,4.535004,-0.380357,9.935367,-0.205147,4.099922,0.770982,5.232516,-8.392181,1.073306,-3.729773,-6.547332,9.286898,-3.688049,4.954391,2.396862,-6.470813,-0.214747,5.884083,-7.450824,-9.022664,5.991515,8.025935,6.811646,-4.307985,-2.668873,-4.336665,-1.707830,1.407206,-1.646398,5.041648,7.029920,-2.110879,3.868624,6.043908,6.232324,8.430583,5.707468,8.052565,-2.852002,1.307047,-9.542474,2.175338,-1.827640,-3.696577,8.989361,-0.470454,4.837225,-6.157351,-5.512696,6.288001,-0.671359,-4.519772,8.747918,-4.737156,3.652842,-4.085874,5.160692,3.133412,-8.022509,-0.839469,6.066830,-9.798466,3.956248,5.428600,-5.205245,4.791567,4.377039,2.262557,-8.551553,-8.113467,1.151193,5.508539,5.353872,-9.886929,-3.201178,6.655904,-7.375104,3.571359,7.188395,2.660043,8.520154,-5.436656,6.902494,5.316560,2.720182,2.251993,-0.665995,7.500275,8.511580,5.582500,-6.002014,-4.329655,-7.458546,-9.329155,-7.973746,7.839555,-8.869234,7.484204,8.246486,9.068168,-5.417477,-0.367460,-6.072707,-9.657434,3.135890,8.042069,9.415253,-3.352874,1.949682,2.228573,5.236292,9.666989,-7.118357,2.468691,2.106661,-8.208907,7.816660,-2.923580,-5.576448,-4.084312,-9.303825,7.214065,3.259240,6.223116,-1.366549,-4.921694,-9.523220,7.751204,-4.391955,-3.721293,-9.148011,-0.957625,2.952594,1.818014,1.559004,-6.353691,4.168843,0.332472,1.343145,-1.047709,1.624065,0.230500,-5.600613,-2.203609,6.201763,7.121898,3.842584,-2.760548,-7.483663,-3.015490,7.398292,-7.092558,-1.265184,9.331153,-1.087984,9.585766,-6.916787,5.044551,-6.238516,-7.728481,5.249353,3.397657,4.396459,1.069100,1.193201,5.609996,-7.742083,0.583640,-9.233877,9.901082,-0.695799,-8.233126,9.214943,-2.943580,-0.293836,-8.738241,-6.527651,-0.745996,4.829275,9.259635,-1.760727,4.658083,-1.276028,6.237726,5.215433,-3.808902,-6.964146,-6.202168,-6.746245,8.817797,7.274785,-5.981654,5.411296,9.185985,0.473550,4.901304,-2.673743,-8.636251,8.474751,3.722756,-0.120644,9.377627,-4.856292,4.788686,-6.804338,4.717722,-1.417502,7.210994,7.693486,-6.361718,4.933122,-3.090983,-1.021245,1.134076,-0.205166,-6.596484,-6.815705,5.560828,5.484303,6.193371,2.238615,-3.186624,3.439739,1.353226,-7.349591,7.251188,0.151258,1.656371,-3.059507,-4.124483,2.987047,-1.431282,-1.729607,3.554602,-5.367861,4.702283,1.585210,2.843743,1.257918,7.167135,-7.079277,5.802009,-5.205050,9.710440,5.060871,-9.891877,-7.727512,-5.726352,-7.497446,-6.432007,0.889427,7.419147,8.856440,3.255961,9.079925,9.127325,0.006458,-5.428421,4.738055,-5.940456,6.773535,-4.390706,0.478391,-5.181996,-8.652239,-2.539148,-4.246214,-8.178662,-0.966350,-3.765726,1.907275,1.032646,-1.563602,-1.203864,2.912781,3.611530,8.900678,-4.867515,-1.902378,9.341740,-2.527953,-9.812074,5.285885,-2.078245,-6.653799,0.182179,-7.749508,-0.718021,-0.686448,9.468987,-2.143031,-0.177087,-3.381623,-9.330556,0.942488,7.969707,-9.373586,-1.310826,-6.292432,7.536797,2.980709,-2.788471,-5.610007,2.336251,-7.159218,-8.818187,9.401228,-8.261282,-6.880524,-8.661897,-2.515351,8.646629,-6.484215,-5.908806,-8.978174,0.004681,5.065023,-7.757439,6.960312,-9.764902,-0.962160,-6.423966,-1.548483,1.594185,7.240500,-0.864553,3.994918,-5.555515,-1.235480,-7.710719,2.163044,-3.036255,-8.846969,-6.261867,-7.293461,4.679278,0.995562,-2.922223,-3.534413,-0.606247,-0.511833,-6.471403,-3.102229,4.214927,9.806831,-8.257789,9.381798,7.901373,2.173702,6.099677,6.722491,-0.128761,-5.841164,-2.342988,-9.164779,8.115113,1.721253,-2.299335,-4.089714,-7.431156,3.875170,-9.353090,-8.274474,-8.372217,6.733166,5.898614,-2.700181,-1.648989,3.816187,-9.987649,0.494010,-2.367517,6.050306,1.608774,-3.909683,5.001411,-5.859876,-2.790787,-5.195553,-1.696819,4.294227,-4.697744,3.868488,-3.831595,7.018449,-4.002450,-5.813853,6.235444,6.222705,-6.453649,6.314702,4.423853,3.632824,-6.211740,6.013682,-7.367125,-2.675977,-7.018894,3.878696,-7.011258,0.065864,4.881870,8.291354,8.959728,6.979777,-4.460465,-3.821622,-9.235916,-0.477975,1.890539,9.614397,-3.379082,-2.356866,6.980886,6.638735], dtype = "float32")#candidate|3022|(1584,)|const|float32
call_3020 = relay.TupleGetItem(func_1233_call(relay.reshape(var_3021.astype('float32'), [10, 8, 3]), relay.reshape(const_3022.astype('float32'), [1584,]), ), 1)
call_3023 = relay.TupleGetItem(func_1236_call(relay.reshape(var_3021.astype('float32'), [10, 8, 3]), relay.reshape(const_3022.astype('float32'), [1584,]), ), 1)
output = relay.Tuple([call_2997,call_3002,const_3003,call_3020,var_3021,const_3022,])
output2 = relay.Tuple([call_2998,call_3004,const_3003,call_3023,var_3021,const_3022,])
func_3035 = relay.Function([var_3021,], output)
mod['func_3035'] = func_3035
mod = relay.transform.InferType()(mod)
mutated_mod['func_3035'] = func_3035
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3036 = relay.var("var_3036", dtype = "float32", shape = (24, 10))#candidate|3036|(24, 10)|var|float32
func_3035_call = mutated_mod.get_global_var('func_3035')
call_3037 = func_3035_call(var_3036)
output = call_3037
func_3038 = relay.Function([var_3036], output)
mutated_mod['func_3038'] = func_3038
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_3070 = func_2138_call()
call_3071 = func_2138_call()
func_2458_call = mod.get_global_var('func_2458')
func_2463_call = mutated_mod.get_global_var('func_2463')
var_3091 = relay.var("var_3091", dtype = "float32", shape = (135,))#candidate|3091|(135,)|var|float32
var_3092 = relay.var("var_3092", dtype = "float32", shape = (1089,))#candidate|3092|(1089,)|var|float32
call_3090 = relay.TupleGetItem(func_2458_call(relay.reshape(call_3070.astype('float32'), [6, 16, 11]), relay.reshape(var_3091.astype('float32'), [135,]), relay.reshape(var_3092.astype('float32'), [1089,]), ), 0)
call_3093 = relay.TupleGetItem(func_2463_call(relay.reshape(call_3070.astype('float32'), [6, 16, 11]), relay.reshape(var_3091.astype('float32'), [135,]), relay.reshape(var_3092.astype('float32'), [1089,]), ), 0)
func_459_call = mod.get_global_var('func_459')
func_462_call = mutated_mod.get_global_var('func_462')
const_3095 = relay.const([0.345468,-5.331637,2.802013,2.850692,-1.473470,3.442745,8.683198,3.075668,-5.205052,0.181747,9.575418,-8.086311,9.638844,-4.466860,0.976389,7.050706,0.552694,-1.769203,2.856680,-6.769444,-1.374105,-6.180044,0.343228,-1.511511,4.295575,4.047724,0.049562,-8.334434,9.336073,2.300632,-8.765480,2.257524,-3.502892,-9.426256,1.261616], dtype = "float64")#candidate|3095|(35,)|const|float64
call_3094 = relay.TupleGetItem(func_459_call(relay.reshape(const_3095.astype('float64'), [1, 7, 5])), 0)
call_3096 = relay.TupleGetItem(func_462_call(relay.reshape(const_3095.astype('float64'), [1, 7, 5])), 0)
output = relay.Tuple([call_3070,call_3090,var_3091,var_3092,call_3094,const_3095,])
output2 = relay.Tuple([call_3071,call_3093,var_3091,var_3092,call_3096,const_3095,])
func_3106 = relay.Function([var_3091,var_3092,], output)
mod['func_3106'] = func_3106
mod = relay.transform.InferType()(mod)
var_3107 = relay.var("var_3107", dtype = "float32", shape = (135,))#candidate|3107|(135,)|var|float32
var_3108 = relay.var("var_3108", dtype = "float32", shape = (1089,))#candidate|3108|(1089,)|var|float32
output = func_3106(var_3107,var_3108,)
func_3109 = relay.Function([var_3107,var_3108,], output)
mutated_mod['func_3109'] = func_3109
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2701_call = mod.get_global_var('func_2701')
func_2702_call = mutated_mod.get_global_var('func_2702')
call_3116 = func_2701_call()
call_3117 = func_2701_call()
output = relay.Tuple([call_3116,])
output2 = relay.Tuple([call_3117,])
func_3118 = relay.Function([], output)
mod['func_3118'] = func_3118
mod = relay.transform.InferType()(mod)
output = func_3118()
func_3119 = relay.Function([], output)
mutated_mod['func_3119'] = func_3119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_3146 = relay.TupleGetItem(func_2978_call(), 1)
call_3147 = relay.TupleGetItem(func_2980_call(), 1)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_3155 = relay.TupleGetItem(func_2978_call(), 1)
call_3156 = relay.TupleGetItem(func_2980_call(), 1)
bop_3180 = relay.add(call_3146.astype('float64'), relay.reshape(call_3155.astype('float64'), relay.shape_of(call_3146))) # shape=(6, 16, 11)
bop_3183 = relay.add(call_3147.astype('float64'), relay.reshape(call_3156.astype('float64'), relay.shape_of(call_3147))) # shape=(6, 16, 11)
bop_3184 = relay.bitwise_xor(call_3155.astype('int8'), relay.reshape(bop_3180.astype('int8'), relay.shape_of(call_3155))) # shape=(6, 16, 11)
bop_3187 = relay.bitwise_xor(call_3156.astype('int8'), relay.reshape(bop_3183.astype('int8'), relay.shape_of(call_3156))) # shape=(6, 16, 11)
output = bop_3184
output2 = bop_3187
func_3191 = relay.Function([], output)
mod['func_3191'] = func_3191
mod = relay.transform.InferType()(mod)
mutated_mod['func_3191'] = func_3191
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mutated_mod.get_global_var('func_3191')
call_3192 = func_3191_call()
output = call_3192
func_3193 = relay.Function([], output)
mutated_mod['func_3193'] = func_3193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_3210 = relay.TupleGetItem(func_2978_call(), 0)
call_3211 = relay.TupleGetItem(func_2980_call(), 0)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_3224 = relay.TupleGetItem(func_276_call(relay.reshape(call_3210.astype('float64'), [8, 12, 11])), 0)
call_3225 = relay.TupleGetItem(func_279_call(relay.reshape(call_3210.astype('float64'), [8, 12, 11])), 0)
output = relay.Tuple([call_3210,call_3224,])
output2 = relay.Tuple([call_3211,call_3225,])
func_3226 = relay.Function([], output)
mod['func_3226'] = func_3226
mod = relay.transform.InferType()(mod)
output = func_3226()
func_3227 = relay.Function([], output)
mutated_mod['func_3227'] = func_3227
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_3316 = func_2138_call()
call_3317 = func_2138_call()
func_2507_call = mod.get_global_var('func_2507')
func_2509_call = mutated_mod.get_global_var('func_2509')
call_3318 = relay.TupleGetItem(func_2507_call(), 0)
call_3319 = relay.TupleGetItem(func_2509_call(), 0)
func_2771_call = mod.get_global_var('func_2771')
func_2775_call = mutated_mod.get_global_var('func_2775')
const_3340 = relay.const(False, dtype = "bool")#candidate|3340|()|const|bool
var_3341 = relay.var("var_3341", dtype = "bool", shape = (1, 264))#candidate|3341|(1, 264)|var|bool
call_3339 = relay.TupleGetItem(func_2771_call(relay.reshape(const_3340.astype('bool'), []), relay.reshape(var_3341.astype('bool'), [2, 11, 12]), ), 0)
call_3342 = relay.TupleGetItem(func_2775_call(relay.reshape(const_3340.astype('bool'), []), relay.reshape(var_3341.astype('bool'), [2, 11, 12]), ), 0)
output = relay.Tuple([call_3316,call_3318,call_3339,const_3340,var_3341,])
output2 = relay.Tuple([call_3317,call_3319,call_3342,const_3340,var_3341,])
func_3349 = relay.Function([var_3341,], output)
mod['func_3349'] = func_3349
mod = relay.transform.InferType()(mod)
var_3350 = relay.var("var_3350", dtype = "bool", shape = (1, 264))#candidate|3350|(1, 264)|var|bool
output = func_3349(var_3350)
func_3351 = relay.Function([var_3350], output)
mutated_mod['func_3351'] = func_3351
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_3411 = relay.TupleGetItem(func_2978_call(), 1)
call_3412 = relay.TupleGetItem(func_2980_call(), 1)
func_276_call = mod.get_global_var('func_276')
func_279_call = mutated_mod.get_global_var('func_279')
call_3428 = relay.TupleGetItem(func_276_call(relay.reshape(call_3411.astype('float64'), [8, 12, 11])), 0)
call_3429 = relay.TupleGetItem(func_279_call(relay.reshape(call_3411.astype('float64'), [8, 12, 11])), 0)
output = relay.Tuple([call_3411,call_3428,])
output2 = relay.Tuple([call_3412,call_3429,])
func_3439 = relay.Function([], output)
mod['func_3439'] = func_3439
mod = relay.transform.InferType()(mod)
output = func_3439()
func_3440 = relay.Function([], output)
mutated_mod['func_3440'] = func_3440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mod.get_global_var('func_3191')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_3456 = func_3191_call()
call_3457 = func_3191_call()
func_1933_call = mod.get_global_var('func_1933')
func_1937_call = mutated_mod.get_global_var('func_1937')
const_3483 = relay.const(-5.987036, dtype = "float32")#candidate|3483|()|const|float32
const_3484 = relay.const([-8.625171,-3.694650,-2.773745,1.680070,-5.551200,-1.321214,0.836757,4.358600,7.554789,4.759052,-2.213212,9.324530,4.763306,-8.390306,-1.826691,-8.206833,8.609475,-0.831901,-8.621737,-7.294252,9.660158,-7.350480,8.045157,-8.167789,1.194416,-3.888696,0.056518,4.337402,0.048871,6.136129,-7.195215,2.799392,-5.487421,8.248557,6.177735,-1.687557,-6.722531,9.550943,-6.425879,2.697880,7.917524,-6.145127,8.064153,2.219899,7.088118,-3.637045,0.909699,3.739164,8.804614,-0.595475,5.168213,7.295320,7.065780,9.600158,-8.048526,-4.415556,-8.042564,-9.737240,-9.532961,7.807877,-5.738173,7.495573,5.339883,-7.071099,-7.111397,9.204850,2.926427,8.681983,3.711149,-8.346674,3.920856,-1.668328,9.898135,-0.722712,-2.734104,3.491793,8.366071,-5.832362,-0.809806,-5.818764,8.059738,-9.295308,-5.310758,-5.147497,-9.222032,-5.394357,0.072757,-0.847912,7.174909,-4.182695,-7.133479,9.835580,3.257942,-5.491133,-1.481414,-9.643594,-4.554832,-2.537354,-7.055591,-7.734489,6.109232,2.052981,4.927202,-6.510193,-7.025686,9.482704,-3.453993,-8.893960,-3.302138,5.802017,3.622008,1.398543,-3.151788,2.083536,-5.267593,-2.941547,-0.828676,-1.734288,4.947184,-4.646460,9.025852,-6.266078,-7.437539,5.661652,3.597219,5.617443,-7.022954,-3.766731,-8.216604,-5.162800,0.840146,1.790048,-5.330527,-2.443459,-5.244453,6.873222,-3.849820,9.295571,-4.554489,7.058641,-9.794448,9.721657,7.267474,0.178885,0.173473,-9.919311,-1.816532,-8.729917,3.165150,-6.749040,1.420062,-6.916105,5.782759,2.024527,-2.543048,1.375166,6.210820,-8.883271,-9.488687,1.984450,0.241084,3.905308,3.268817,-3.974451,-8.032447,-5.825650,-2.581991,8.589886,-6.958717,0.526567,8.628430,2.460088,8.778578,-5.005391,-3.297021,6.945432,5.505571,8.001255,-9.080873,-6.477435,0.529145,1.337188,6.096581,3.875132,8.168633,-4.462053,-1.092813,7.230453,8.432973,7.303832,8.262032,9.044982,4.058686,9.930358,-2.938807,-1.085641,-3.005029,2.162180,-0.150888,-6.875835,-5.227162,7.600973,-3.208150,-1.686222,-0.141783,8.361298,4.120652,-5.503646,-4.195795,-3.308461,1.062689,-4.650632,-5.675465,8.328209,-8.168401,-9.794842,9.262304,0.520284,0.307062,3.081823,-8.631136,1.271594,-4.894036,-7.033848,-3.029559,2.146275,-4.981464,7.832321,-4.952032,0.353810,-5.965001,6.086211,0.937399,-9.845793,-7.187211,-7.225125,-2.360967,-1.756882,-3.986282,6.251595,-1.740550,-8.817709,-4.766096,8.965193,2.991370,-9.166809,4.277421,8.503639,-3.636485,7.272669,6.368666,6.314936,9.181502,-7.233196,4.115776,-4.759704,3.426926,-4.600795,9.082671,-2.698817,-0.023350,-5.407834,-1.250928,7.439299,2.851738,2.785683,-2.467196,6.798714,2.000763,3.286172,2.261173,-0.330170,8.533591,0.373095,-7.479956,2.803774,-8.263536,-9.285430,9.804609,8.124344,-9.937508,1.757308,-4.428966,3.730720,2.329425,-5.566696,-3.501425,6.363542,0.674723,-0.435014,-9.346216,-0.631994,-4.198188,8.724490,-5.898430,-5.127651,4.821856,-5.458703,-8.559847,2.245963,-6.114473,6.819350,-7.977616,-1.640696,7.692807,-0.133868,-9.356823,-5.133081,5.178360,-6.097589,-0.438441,9.189340,4.958490,0.203380,8.658700,4.166548,-0.446417,-8.859432,4.648907,-3.069855,-9.579563,-2.107171,-8.246041,6.524242,-7.097029,8.931258,-6.042475,-1.262859,-5.505425,-8.771370,0.446389,-0.391039,-3.348054,-0.027901,2.728602,-4.764382,5.442067,3.623570,4.006330,-5.189205,-7.218612,-7.306440,-1.326230,-2.119929,8.631506,-8.993983,-3.110861,-2.372410,1.555776,-3.402114,-3.404405,-2.455803,4.536708,1.564225,-8.568804,-8.284170,9.986119,-0.402985,-3.433246,4.610466,1.733251,-2.100198,-2.698404,-8.278345,7.170558,-1.794974,6.642652,-6.922973,-6.367494,7.462036,5.524046,-4.212226,-2.691363,-5.264572,1.845760,-1.768754,3.572343,5.475218,-5.051321,3.471190,-6.069033,6.694939,6.659188,7.627343,7.995132,-5.486877,-5.652183,0.749813,5.880043,8.623821,0.949628,2.026367,-7.034782,-3.277567,-3.055418,5.437031,-1.447592,-7.520013,-7.509117,6.275804,-3.529394,-9.892306,-2.256556,-0.394433,7.419322,7.423105,2.269519,5.948707,1.552165,-5.181506,8.469871,-5.641769,-7.536117,7.080080,-6.212937,-9.158206,3.352178,-4.299367,3.426728,2.457845,-2.283454,6.794451,-9.109201,-7.685595,9.923387,0.391206,-8.612436,-3.686324,2.896536,4.938663,-5.934830,-5.669605,-6.241582,-6.334409,4.808801,-7.718551,-2.730142,-3.607247,-2.188182,-9.598272,4.890386,-8.296696,1.129477,6.706202,8.153233,9.029132,-9.392695,3.117513,-2.252019,-7.182686,1.596264,4.511868,8.321209,-8.756682,-2.835267,8.506868,7.044539,3.900562,-8.906134,1.392163,1.999989,6.099309,-6.830123,-8.140866,-2.288429,1.378336,8.372514,3.517065,-8.215406,-6.559486,-3.525604,-8.716783,-2.353600,6.847097,-2.575930,-4.212196,3.272712,-0.448534,-7.649854,-5.219405,2.055497,-8.052957,-8.280947,5.594583,-5.482246,-3.893476,6.198549,-7.040550,-3.959573,-2.632912,-3.862853,2.957573,2.192939,7.978068,-6.673310,-5.331794,4.209749,2.761970,7.520465,-4.084929,-7.925344,-7.027844,-7.350158,2.289340,-4.399349,3.777435,-0.043691,-0.840501,-7.106952,1.502205,4.848265,1.373729,1.478301,0.357949,8.685710,-2.165337,-4.492545,-4.395990,4.658145,7.008285,5.748313,-2.880538,1.022141,3.919398,-0.956893,1.205550,9.035692,4.715481,1.064797,6.855929,-1.165065,-6.036486,-3.477772,7.821882,2.573743,-9.257445,-9.523577,-5.238443,8.971142,1.186345,9.997036,-6.057134,4.682617,3.486632,-3.695331,-7.523416,-2.726065,0.627894,4.812562,-5.028978,1.519994,0.277167,3.861315,-1.379937,-9.090558,-7.391718,-4.528812,-4.104329,-5.296532,-5.202143,-0.403974,-9.129055,4.940431,9.897700,-9.295375,6.974393,-5.300907,4.706853,5.576519,4.748530,-9.489163,2.051683,-0.007516,-8.722243,5.204916,4.765196,2.795880,-0.686930,1.057359,6.836857,3.582488,2.368373,-3.872935,2.589858,-7.423455,2.822443,-5.853406,7.185053,-4.175991,-7.174306,-5.473894,8.452312,4.429420,6.328918,5.601693,-0.930840,9.814020,0.686561,6.135971,6.663806,9.619609,-5.406304,3.838413,-7.810302,9.989763,0.772868,-4.757980,-1.473357,-1.287315,-7.323532,-7.029292,-1.661544,-8.949272,5.894047,-3.108770,-7.624844,9.927109,-7.611628,-9.034192,-5.641222,9.103387,-3.927499,-4.174153,0.951527,-9.302418,0.803673,-3.904503,-4.378624,3.171426,-2.691079,7.942080,6.339714,8.707635,8.502533,-3.231328,-9.765451,-0.010464,1.320261,2.750488,1.509076,-1.136336,-7.598440,8.563801,0.629702,6.135825,-7.278410,-9.287258,3.319132,1.272493,-6.874677,2.053637,6.129774,1.757044,-0.269719,5.162397,-2.545897,-6.474217,7.274527,8.210756,-5.489791,-6.272792,0.207976,-5.530740,2.631131,-2.198925,5.256555,-4.409123,1.662643,0.126848,-9.789909,2.893942,-7.984205,8.934211,6.321854,3.494343,4.718505,5.106823,-8.989437,-5.508715,2.843406,5.304249,-0.348383,-8.542903,8.032906,6.454038,-5.592414,-3.270616,0.588647,-7.289380,8.995478,-9.923804,-6.181422,2.576093,-9.033399,-0.356233,-3.283153,-7.025440,1.310775,-6.946782,1.835690,-3.387121,9.980444,-8.250351,-8.876575,3.916350,-7.090893,2.124899,8.752673,-4.381242,-7.400618,-8.428483,-8.501536,3.721124,4.155417,7.495255,0.171084,-8.258801,-9.470316,8.952047,-8.136643,-1.694231,8.281967,9.326725,7.830163,-4.543994,-7.170786,-9.778922,9.441824,-8.764528,-9.701612,0.953285,2.842204,-1.344804,5.853593,-3.646946,-4.376033,-3.276028,-1.253538,9.154274,1.281544,0.267182,-7.088047,1.756052,4.235745,-7.823439,2.192023,-8.820288,6.473548,-0.758142,-1.839831,-3.608993,-5.722705,-7.274849,-0.778637,-2.720803,4.063314,7.546763,2.794751,-9.928735,-8.809286,-4.995769,-4.656509,-4.238078,5.836758,-6.962350,-4.245377,2.928204,-0.649856,3.486017,0.669280,-4.446293,-8.219413,-6.960833,-7.700453,-9.981657,3.627276,-4.089611,2.439548,7.573116,-4.237781,4.483997,3.352289,3.247422,-0.740209,-0.110325,-4.185366,0.996474,7.627343,-8.813726,-6.024323,-8.202146,-6.503541,3.336767,-5.898519,-1.325842,8.441396,8.238538,-8.282507,-1.055381,3.197789,-1.549316,5.657821,-2.218835,2.786888,7.096454,-2.837418,8.887876,-4.284306,-0.856728,-7.455057,5.355449,-8.277185,-6.269365,2.790735,-6.808741,1.938631,-8.229188,-9.325027,7.203272,-6.103826,1.493784,4.444294,7.622498,2.182977,-7.499425,-9.040559,6.460471,-0.972145,-7.289073,-2.038045,-5.230928,8.751870,8.866765,-0.674606,-2.575951,1.034043,4.454459,-7.144920,-0.941741,-8.881117,0.097970,8.135757,-3.358210,-4.017853,4.560895,4.348408,9.615526,1.493148,-6.992339,6.517939,-3.715932,-4.954860,3.630083,-8.250002,-7.517079,-2.855350,5.411182,8.142554,4.612024,-6.565335,-3.167266,8.642937,0.729618,-7.125512,-6.118649,-5.683306,-3.038585,-0.236523,8.351777,-5.423746,3.403058,-1.843552,-1.967429,-7.649049,4.204521,-1.038857,-2.475829,1.042665,-2.585628,1.351664,-8.702464,6.758144,-9.663675,-1.975720,-9.038867,-4.188142,-5.604838,4.650832,-7.754346,-5.631269,-3.958314,2.339242,-7.602992,-7.824710,5.833326,2.817795,4.625713,-1.432083,-7.465509,-1.305353,5.335754,1.975711,7.825842,-1.592612,-5.603248,4.947234,-3.100382,-1.949237,-1.939391,4.181909,-4.404655,9.306622,-3.987190,-8.248513,-6.913845,1.827626,7.674910,2.386560,6.446171,-8.834477,6.352190,8.523010,-4.079867,-1.029878,-6.006207,-0.228530,9.222882,1.744175,-0.124543,-5.737486,-3.318581,-8.108634,-8.632527,-1.293737,-4.464965,-5.861236,-3.167957,2.393696,0.581705,4.893669,0.518355,-5.297293,9.148497,-4.222614,3.873713,5.739882,1.962406,3.586193,4.295983,0.457489,-5.916476,9.949053,0.847087,-1.422004,5.360393,2.577380,2.836829,8.652540,7.977605,-9.307635,-7.725091,-5.885328,-9.249647,-2.589638,6.130383,9.122069,6.798700,-3.395495,6.422265,8.826167,1.339035,1.224940,-6.015383,7.894359,8.046405,4.528372,3.168877,4.775484,2.047863,-0.824182,8.066218,5.722940,-2.821884,-6.673698,-0.640541,-4.201302,-7.870383,-4.276892,-1.671344,-7.099985,-7.353934,-9.583220,8.385795,8.073171,9.133195,3.456606,4.493508,1.784949,-1.801072,9.153279,9.458700,-1.236869,7.067987,-3.910261,3.610848,0.547742,-6.401511,1.645608,7.711841,8.322628,-3.777084,-9.068200,4.598318,-3.498312,2.597995,-0.847544,2.183924,-1.811084,0.371879,2.591749,0.901435,-9.455925,-3.133234,0.842907,-9.118668,-3.802519,6.159783,-8.465606,-4.735745,-5.753085,-4.319078,-0.439115,-9.746776,8.607453,9.794187,-9.266496,6.945852,3.337942,-6.134547,-2.807316,9.158563,-9.287939,0.058513,5.621589,8.468350,0.538662,-5.495328,4.033853,-4.938094,-7.465847,6.647439,-4.900642,-6.215105,-9.908329,-4.356510,1.383715,6.347057,-9.276414,1.885519,-7.324132,3.906886,-8.764257,1.288937,-9.952289,-6.008930,-2.925839,5.412195,2.176829,-4.044476,4.588904,-1.318456,-7.571658,-8.032598,-3.339337,-2.302650,-1.655610,-2.867785,0.241844,-3.295902,0.025495,-0.555492,3.656237,-5.061195,4.043403,-4.315881,2.994535,-6.354968,1.276570,-2.540884], dtype = "float32")#candidate|3484|(1089,)|const|float32
call_3482 = relay.TupleGetItem(func_1933_call(relay.reshape(const_3483.astype('float32'), []), relay.reshape(const_3484.astype('float32'), [1089,]), ), 6)
call_3485 = relay.TupleGetItem(func_1937_call(relay.reshape(const_3483.astype('float32'), []), relay.reshape(const_3484.astype('float32'), [1089,]), ), 6)
func_2871_call = mod.get_global_var('func_2871')
func_2873_call = mutated_mod.get_global_var('func_2873')
call_3512 = func_2871_call()
call_3513 = func_2871_call()
bop_3525 = relay.right_shift(const_3483.astype('int8'), call_3456.astype('int8')) # shape=(6, 16, 11)
bop_3528 = relay.right_shift(const_3483.astype('int8'), call_3457.astype('int8')) # shape=(6, 16, 11)
func_1302_call = mod.get_global_var('func_1302')
func_1305_call = mutated_mod.get_global_var('func_1305')
const_3547 = relay.const([-6.978107,4.328075,7.671329,7.877700,8.563515,-2.218510,-3.851111,4.063572,2.566822,-5.516698,7.133418,8.865382,2.473290,-9.678400,-3.031393,-9.236282,7.393789,-0.946360,-9.779338,6.404341,6.275190,5.295572,-7.221309,-8.728877,5.074317,-7.797451,2.750958,-3.819295,1.321005,-6.312642,-4.681329,-4.243614,-9.342399,-7.371814,-4.448669,-1.297264,2.420708,-4.704738,-8.575373,1.341043,8.897647,-4.369788,-6.170966,7.793141,2.318973,5.994371,-9.036624,7.491769,-7.203105,0.992430,8.827174,-3.975348,8.888283,6.755292,4.247164,8.634370,-1.416296,-1.204272,-5.984067,-4.244001,1.797134,3.557455,-0.115671,-9.021350,-8.886059,7.687815,6.586123,3.164882,-1.319386,-6.858712,3.344714,-1.241873,-2.125592,-6.217939,2.798270,-6.406549,3.161657,-9.173203,8.431551,-0.387371,4.822279,2.908486,-8.975744,5.394373,7.943004,-3.008725,-5.032893,8.969979,8.198161,2.799291,-3.358312,9.762991,-6.193593,4.362798,-5.932017,9.177001,-4.434373,-4.027213,1.323013,8.406040,-2.754645,-9.330710,5.837745,3.017028], dtype = "float64")#candidate|3547|(104,)|const|float64
call_3546 = func_1302_call(relay.reshape(const_3547.astype('float64'), [1, 8, 13]))
call_3548 = func_1302_call(relay.reshape(const_3547.astype('float64'), [1, 8, 13]))
output = relay.Tuple([call_3482,const_3484,call_3512,bop_3525,call_3546,const_3547,])
output2 = relay.Tuple([call_3485,const_3484,call_3513,bop_3528,call_3548,const_3547,])
func_3567 = relay.Function([], output)
mod['func_3567'] = func_3567
mod = relay.transform.InferType()(mod)
mutated_mod['func_3567'] = func_3567
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mutated_mod.get_global_var('func_3567')
call_3568 = func_3567_call()
output = call_3568
func_3569 = relay.Function([], output)
mutated_mod['func_3569'] = func_3569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_3572 = relay.TupleGetItem(func_1643_call(), 0)
call_3573 = relay.TupleGetItem(func_1644_call(), 0)
var_3585 = relay.var("var_3585", dtype = "float32", shape = (6, 16, 11))#candidate|3585|(6, 16, 11)|var|float32
bop_3586 = relay.equal(call_3572.astype('bool'), relay.reshape(var_3585.astype('bool'), relay.shape_of(call_3572))) # shape=(6, 16, 11)
bop_3589 = relay.equal(call_3573.astype('bool'), relay.reshape(var_3585.astype('bool'), relay.shape_of(call_3573))) # shape=(6, 16, 11)
func_2951_call = mod.get_global_var('func_2951')
func_2954_call = mutated_mod.get_global_var('func_2954')
var_3607 = relay.var("var_3607", dtype = "float32", shape = ())#candidate|3607|()|var|float32
var_3608 = relay.var("var_3608", dtype = "float32", shape = (1089, 1))#candidate|3608|(1089, 1)|var|float32
call_3606 = relay.TupleGetItem(func_2951_call(relay.reshape(var_3607.astype('float32'), []), relay.reshape(var_3608.astype('float32'), [1089,]), ), 2)
call_3609 = relay.TupleGetItem(func_2954_call(relay.reshape(var_3607.astype('float32'), []), relay.reshape(var_3608.astype('float32'), [1089,]), ), 2)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_3610 = relay.TupleGetItem(func_2978_call(), 1)
call_3611 = relay.TupleGetItem(func_2980_call(), 1)
output = relay.Tuple([bop_3586,call_3606,var_3607,var_3608,call_3610,])
output2 = relay.Tuple([bop_3589,call_3609,var_3607,var_3608,call_3611,])
func_3619 = relay.Function([var_3585,var_3607,var_3608,], output)
mod['func_3619'] = func_3619
mod = relay.transform.InferType()(mod)
mutated_mod['func_3619'] = func_3619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3619_call = mutated_mod.get_global_var('func_3619')
var_3621 = relay.var("var_3621", dtype = "float32", shape = (6, 16, 11))#candidate|3621|(6, 16, 11)|var|float32
var_3622 = relay.var("var_3622", dtype = "float32", shape = ())#candidate|3622|()|var|float32
var_3623 = relay.var("var_3623", dtype = "float32", shape = (1089, 1))#candidate|3623|(1089, 1)|var|float32
call_3620 = func_3619_call(var_3621,var_3622,var_3623,)
output = call_3620
func_3624 = relay.Function([var_3621,var_3622,var_3623,], output)
mutated_mod['func_3624'] = func_3624
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3721 = relay.var("var_3721", dtype = "float32", shape = (5, 13, 13))#candidate|3721|(5, 13, 13)|var|float32
var_3722 = relay.var("var_3722", dtype = "float32", shape = (5, 13, 13))#candidate|3722|(5, 13, 13)|var|float32
bop_3723 = relay.divide(var_3721.astype('float32'), relay.reshape(var_3722.astype('float32'), relay.shape_of(var_3721))) # shape=(5, 13, 13)
output = bop_3723
output2 = bop_3723
func_3732 = relay.Function([var_3721,var_3722,], output)
mod['func_3732'] = func_3732
mod = relay.transform.InferType()(mod)
mutated_mod['func_3732'] = func_3732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3732_call = mutated_mod.get_global_var('func_3732')
var_3734 = relay.var("var_3734", dtype = "float32", shape = (5, 13, 13))#candidate|3734|(5, 13, 13)|var|float32
var_3735 = relay.var("var_3735", dtype = "float32", shape = (5, 13, 13))#candidate|3735|(5, 13, 13)|var|float32
call_3733 = func_3732_call(var_3734,var_3735,)
output = call_3733
func_3736 = relay.Function([var_3734,var_3735,], output)
mutated_mod['func_3736'] = func_3736
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_3826 = func_2138_call()
call_3827 = func_2138_call()
output = call_3826
output2 = call_3827
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
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_3879 = func_3833_call()
call_3880 = func_3833_call()
func_1014_call = mod.get_global_var('func_1014')
func_1018_call = mutated_mod.get_global_var('func_1018')
const_3903 = relay.const([[-3],[2],[-10],[6],[-5],[7],[-6],[-7],[-10],[9],[-6],[-6],[9],[-6],[4],[-4],[8],[5],[-2],[-1],[4],[1],[2],[-2],[2],[2],[10],[-4],[-10],[9],[-2],[-8],[-8],[-10],[6],[9],[1],[1],[-7],[-8],[4],[8],[-8],[5],[3],[-1],[-7],[-7],[2],[7],[-9],[9],[6],[3],[-2],[-4],[-1],[-2],[-5],[8],[-3],[4],[5],[-8],[7],[6],[-2],[5],[-4],[-3],[9],[3],[-2],[-10],[4],[-4],[6],[8],[9],[10],[-1],[-3],[-1],[3],[7],[2],[-5],[-8],[1],[-1],[-8],[3],[-5],[5],[5],[2],[-4],[-9],[1],[10],[7],[-4],[8],[7],[-1],[-6],[5],[3],[10],[-6],[5],[-1],[2],[4],[1],[1],[-6],[8],[8],[3],[6],[-6],[-9],[-1],[-7],[4],[-6],[3],[-4],[-1],[-8],[2],[-9],[8],[-8],[7],[-2],[-4],[-4],[-10],[3],[-4],[-10],[5],[1],[8],[10],[5],[-2],[9],[6],[3],[8],[9],[-2],[4],[-6],[4],[-5],[-7],[-5],[-8],[-6],[-4],[-8],[10],[8],[-1],[1],[-10],[-2],[10],[-3],[1],[3],[6],[4],[-5],[-9],[-1],[-2],[10],[-6],[-8],[-3],[-2],[3],[1],[8],[7],[10],[1],[9],[8],[-7],[-4],[2],[2],[-5],[7],[-9],[2],[-2],[-1],[5],[-2],[-1],[-2],[-3],[8],[-9],[-2],[6],[-1],[2],[-8],[-6],[6],[-3],[6],[5],[4],[-5],[8],[-7],[9],[-9],[-9],[2],[-8],[5],[-9],[6],[6],[-2],[-9],[4],[-5],[-2],[-8],[-9],[4],[-7],[3],[-2],[-6],[-6],[-7],[8],[-6],[-10],[9],[10],[5],[-7],[8],[-10],[-4],[-5],[8],[7],[-4],[7],[-9],[-7],[-9],[-2],[2],[-2],[-2],[10],[7],[-4],[8],[-7],[7],[-10],[-10],[4],[-4],[-6],[9],[1],[8],[8],[4],[-1],[9],[1],[7],[6],[3],[6],[-3],[-3],[-1],[-9],[-5],[-2],[6],[4],[-8],[-3],[2],[-6],[4],[-4],[-6],[-10],[-9],[7],[10],[-10],[6],[9],[-4],[6],[-1],[10],[-4],[4],[-10],[5],[-7],[6],[-8],[7],[7],[-4],[-1],[-9],[-7],[8],[-5],[-1],[5],[-7],[4],[-3],[-6],[6],[-10],[-3],[-2],[3],[1],[10],[-8],[-6],[-5],[10],[-4],[6],[-8],[8],[8],[2],[-9],[-6],[-4],[-6],[-1],[-3],[-3],[10],[9],[1],[-8],[1],[8],[3],[-3],[3],[-10],[5],[-7],[8],[-7],[7],[-1],[-1],[10],[4],[-1],[-5],[4],[4],[-3],[-1],[5],[6],[7],[10],[-5],[6],[-7],[-6],[9],[6],[-5],[-10],[8],[-8],[10],[-3],[-5],[4],[3],[8],[2],[-3],[10],[-7],[-1],[10],[1],[7],[-3],[-2],[4],[5],[6],[-3],[-5],[6],[4],[-8],[1],[5],[8],[2],[-5],[-1],[-3],[1],[-10],[-9],[8],[-7],[3],[-2],[-5],[5],[-10],[1],[-8],[-9],[1],[-1],[-5],[-4],[-9],[-3],[-4],[-1],[6],[-6],[-8],[10],[-1],[-5],[-4],[-4],[-6],[-9],[-7],[6],[-3],[4],[1],[-6],[1],[-7],[-5],[6],[-6],[5],[-5],[4],[3],[-2],[4],[10],[-9],[7],[-2],[-5],[7],[1],[-9],[-7],[9],[-4],[2],[8],[1],[10],[10],[-5],[6],[8],[-8],[-10],[-7],[8],[9],[-10],[9],[7],[-3],[-1],[-4],[10],[-2],[-2],[-10],[6],[-5],[3],[-9],[-7],[-6],[9],[4],[1],[10],[2],[4]], dtype = "uint64")#candidate|3903|(528, 1)|const|uint64
const_3904 = relay.const([[4,-4,5,7,1,-9,-4,-7,2,-10,9,-4,6,4,6,5,3,2,-9,6,-5,-10,1,6]], dtype = "uint16")#candidate|3904|(1, 24)|const|uint16
call_3902 = relay.TupleGetItem(func_1014_call(relay.reshape(const_3903.astype('uint64'), [12, 11, 4]), relay.reshape(const_3903.astype('float64'), [12, 11, 4]), relay.reshape(const_3904.astype('uint16'), [24,]), ), 4)
call_3905 = relay.TupleGetItem(func_1018_call(relay.reshape(const_3903.astype('uint64'), [12, 11, 4]), relay.reshape(const_3903.astype('float64'), [12, 11, 4]), relay.reshape(const_3904.astype('uint16'), [24,]), ), 4)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_3912 = relay.TupleGetItem(func_2562_call(), 0)
call_3913 = relay.TupleGetItem(func_2563_call(), 0)
var_3929 = relay.var("var_3929", dtype = "float32", shape = (6, 16, 11))#candidate|3929|(6, 16, 11)|var|float32
bop_3930 = relay.floor_divide(call_3912.astype('float32'), relay.reshape(var_3929.astype('float32'), relay.shape_of(call_3912))) # shape=(6, 16, 11)
bop_3933 = relay.floor_divide(call_3913.astype('float32'), relay.reshape(var_3929.astype('float32'), relay.shape_of(call_3913))) # shape=(6, 16, 11)
func_2458_call = mod.get_global_var('func_2458')
func_2463_call = mutated_mod.get_global_var('func_2463')
var_3942 = relay.var("var_3942", dtype = "float32", shape = (135,))#candidate|3942|(135,)|var|float32
const_3943 = relay.const([7.259590,-4.578385,-5.909121,-1.912713,-6.239338,-3.885477,-7.729385,-6.259581,3.233526,4.997704,-5.630961,3.192034,-3.383899,-7.672233,-7.675513,-1.798456,5.722583,-8.298442,-7.573058,0.228043,-6.658735,8.500070,-1.754729,1.896111,-0.077473,5.136016,-8.850040,7.132369,-9.282468,-7.718934,-3.385307,-2.452478,8.835945,8.945043,-0.976116,-5.815053,9.348437,1.666371,-2.773873,9.032696,1.464245,3.679809,8.933965,-0.335489,-5.805631,7.907348,3.245654,2.077646,-4.310899,-3.325401,4.081106,4.728007,6.277974,-6.438616,3.394733,-8.755180,9.142744,-8.180562,8.321839,-5.767284,8.082730,-8.713616,-6.700368,6.709012,-3.075387,2.607976,3.950793,-4.632121,8.662574,-2.031402,6.132241,7.541274,-9.612032,5.581230,-0.981001,9.577447,3.266345,-5.001851,2.841172,-9.388781,-2.891349,8.757199,-4.761577,-6.364675,2.600023,9.187516,5.951973,7.159197,-8.366932,7.411680,-5.742639,9.955537,-2.478973,1.865782,4.542170,-3.283242,9.708771,4.481554,3.250839,8.318954,-4.089415,4.988607,6.791135,9.287296,-3.426020,-7.269840,-0.451361,-5.647854,-0.260950,-7.669917,-0.720412,0.876448,1.480662,8.289691,-6.803234,0.500969,1.592818,-6.218981,4.770353,1.352568,3.096608,-9.919436,2.106417,-5.890853,1.901049,0.930684,8.531639,5.824674,-1.995540,-9.121560,-7.085934,1.337332,-0.322681,-2.920113,-0.095269,9.185406,-1.683006,8.302691,7.942599,2.506968,-2.591426,-7.854661,9.365102,-0.440073,-0.375215,-1.825283,-0.683776,2.896724,9.285754,-7.225168,4.445144,3.868351,-7.014983,8.897389,7.017567,-6.846236,4.145793,9.517353,-7.661743,-0.850802,-2.255071,4.699350,6.022957,-1.179640,5.834294,-2.061952,-8.372316,-7.629374,-9.676684,-5.641652,-3.168661,5.016437,2.100209,-1.472286,1.227678,7.799108,2.230231,-8.832049,7.397010,5.424660,-7.555585,1.740901,-4.428395,9.397267,9.354001,-8.544566,-2.946341,6.301545,-9.081799,0.874376,1.866488,-9.555036,-1.023518,4.160055,0.929349,-9.984226,-0.326902,-8.576122,0.514489,2.148772,-5.974314,-8.030790,1.941655,-7.101169,8.073579,5.339089,-3.203384,2.160219,3.037342,-8.953033,4.247944,-6.394112,-3.787203,-3.554638,-1.642340,-1.302400,8.639843,1.111751,5.675898,6.430812,8.964035,3.070528,-1.348395,-4.400682,0.683050,-0.442576,2.320777,-3.253394,2.185787,1.438233,-5.713533,-6.629569,-3.974114,-9.228726,-7.971361,-1.439320,3.609025,1.247846,-1.914843,7.864757,0.905463,4.075688,-4.152441,-9.114808,-1.107107,9.482745,-6.989123,4.372199,2.562559,-6.430926,1.979040,5.552708,-1.254709,-3.811088,2.197585,-0.115739,2.545418,2.713280,1.134077,8.962846,-8.037363,-9.659853,1.726758,8.324088,0.520232,-4.576965,0.949094,8.173900,-2.871780,-6.942574,8.073169,-0.482237,-1.279784,-2.220919,-0.490703,-6.113265,-2.252467,9.155616,-3.238963,-0.030758,-1.892397,-9.272576,9.974186,5.346184,8.954517,5.652664,-3.707047,9.695920,8.038453,-4.830479,0.769893,-1.698650,7.054966,4.427597,8.197482,2.287856,-2.627541,1.250453,-1.447061,-7.108515,-9.900949,-9.239859,6.510160,-8.884305,-0.583618,-4.819726,3.147436,0.872487,-3.026821,-5.765861,9.860413,6.233761,1.530812,7.975829,4.318440,2.299480,2.951954,-5.737514,4.947974,2.829034,2.505271,6.222425,2.534470,8.575070,-4.503575,4.277101,-9.780987,7.679530,8.436800,8.632397,-9.888562,-3.102978,-5.682761,2.162275,7.740287,1.098699,-9.775983,5.586105,-0.134391,-8.653453,-2.279142,-3.841071,-1.426081,-1.410390,-5.763807,8.349887,-1.668335,-0.135379,-9.239067,-3.817576,-5.989666,3.369700,8.838714,-1.951343,0.420669,-8.128442,-7.504452,-0.988248,-3.070166,-7.119666,-8.515004,-2.887854,-4.009427,-8.931583,-3.028023,-9.445699,-6.392518,4.466057,1.772796,5.592056,-7.887552,-7.115032,-0.311805,-5.853266,-3.413313,7.308585,-9.395026,1.102321,-5.403468,0.433431,2.122447,-8.941190,9.409493,2.256416,7.839253,-8.786302,-7.815332,0.303632,2.929795,9.866615,-9.275023,5.765194,-4.212603,7.270754,-4.642661,5.764621,6.362853,0.952895,-1.676721,1.114618,-4.976967,6.715121,-3.684439,1.931847,-1.044268,7.509827,-0.710213,0.604586,-1.784093,7.936001,-3.892283,-6.246982,-7.917825,-5.821671,-9.436123,1.141002,6.669269,0.031627,6.789045,-3.007921,6.853668,-7.617119,-2.651274,0.332782,6.432083,2.392862,7.128611,3.575361,2.231002,-4.374074,6.603515,-1.994189,8.433813,-0.938126,7.872826,-7.685637,3.345692,-5.600614,9.406241,-1.429051,-9.078490,-9.081376,2.546923,-6.746541,8.059758,-7.327942,-5.149894,-1.398665,-9.533328,-0.454440,3.216357,-0.060417,3.532756,-2.081995,-4.522158,2.392204,-4.762424,5.625343,3.412937,-4.635352,-7.311485,9.660244,-2.988896,-3.622803,7.477561,-8.447210,-5.479845,2.841706,7.750792,-5.720171,-7.703461,-4.917509,6.893370,-7.876889,4.346496,2.617990,5.939096,-2.810564,-9.035258,-5.070523,6.129131,-2.076008,6.646329,-3.194745,8.212602,6.496631,-2.323674,-3.241731,1.368025,5.715885,-8.451473,-5.679465,0.565318,0.330311,-1.268248,4.501855,-9.315239,9.428014,6.475443,-4.318586,-8.271460,-5.936561,3.040368,-4.933393,4.802920,-2.732034,-4.874942,2.904593,2.863802,-5.152771,-6.645686,-7.426927,1.411694,3.785338,5.696558,-2.370783,8.866522,-9.618171,0.678503,7.781205,-0.120537,-1.460991,-4.368792,0.694397,-6.460331,9.995819,2.823126,5.549843,8.143697,-7.539380,-6.383631,-7.292497,6.803400,7.639342,9.714043,-2.346169,-9.458167,9.267846,-2.575194,-4.152933,-4.993714,-9.701497,1.226004,-8.818047,-4.175167,8.174730,5.938289,-1.009068,9.647903,-0.042019,-6.521681,-6.038173,5.304333,0.934502,-9.151854,6.693894,-9.591026,0.596868,2.011057,-8.394314,-1.289469,7.388310,-6.876249,-5.473446,0.927454,-2.283581,1.100596,-7.389276,-7.053701,4.780945,9.681453,8.895934,-3.496571,-2.247117,1.118109,0.449405,-1.732463,6.353834,-0.121824,-0.792494,-7.773564,9.815311,-9.285644,4.428353,7.210128,6.942616,2.427099,-0.403241,4.448238,7.016685,-5.418827,-3.214729,9.769395,9.172711,-3.547695,8.731014,-3.553737,-2.187661,-1.980734,-4.670920,-5.113096,9.757666,-4.852936,0.652973,-3.446381,-4.233378,0.225113,5.931053,8.806308,-1.124580,8.368683,-4.271233,-9.282873,-6.409025,-9.259295,1.595177,-5.266540,-6.365916,-3.784807,1.808989,9.123464,3.044396,-7.165435,2.483774,1.728619,9.674194,-1.887890,3.401312,1.942745,9.272161,-9.726738,-0.763501,8.061219,6.421611,5.565903,-2.068281,9.493360,5.924680,3.333898,2.923254,7.199178,5.226251,-9.420674,-1.294899,-7.372684,-0.559555,-2.060223,9.832979,1.658105,-8.680954,6.341131,9.661232,-8.506587,9.547552,-5.506834,3.163363,6.047464,6.875685,1.720691,3.244912,1.048187,-1.408498,3.592574,-4.655274,-6.661254,2.722866,3.327042,-6.157418,7.525225,1.210552,-1.738640,9.893442,8.900082,-6.582670,2.377432,-0.621432,8.499326,-8.650597,3.191148,2.153178,3.153492,4.286144,-7.344396,8.855982,8.282801,2.092637,9.673574,-5.869240,9.213856,6.182663,-0.552725,0.338408,-2.708319,-7.234128,-1.697143,8.909589,-3.953333,5.156695,2.624800,3.979804,2.927204,-4.984026,2.993913,-1.859219,5.045207,7.366750,0.921647,9.670074,3.710615,0.626926,-6.801408,4.819231,-8.474515,3.469775,7.752692,-2.098865,7.700596,6.694746,2.730891,1.857059,6.105470,2.168345,7.429842,-3.873203,-2.519027,9.369974,9.857685,-8.976753,0.958528,2.107187,-0.297350,8.359079,-4.411134,-4.377475,-4.425855,6.281767,9.812379,3.253905,7.787095,9.168982,9.302900,-4.423253,9.261222,-7.077171,-9.710457,-1.013984,-0.228544,-1.133759,-8.666255,-9.217766,-5.138595,0.607065,-0.092821,0.149497,-3.114801,-3.947338,4.341007,-7.133402,4.580754,4.049629,-3.903611,-4.862437,0.882330,-8.235442,1.781651,2.013505,-7.109804,4.795688,1.299561,-4.223139,0.272231,5.600560,-8.688228,-1.075349,9.999668,7.823491,0.532895,-8.425680,1.593225,-6.706524,5.189709,-0.321639,-3.486153,8.533567,-7.986996,-5.830839,-8.861266,-5.652549,0.812793,-9.234883,-4.894064,5.934903,1.618488,9.046220,-5.065431,9.777724,8.753690,9.932949,-6.384926,7.998131,-6.394608,-3.414959,9.711575,1.018201,5.674884,5.535105,-0.870242,6.098265,-5.038154,-3.526591,3.445353,6.454021,3.062620,-9.199345,3.100972,4.786156,5.124529,-5.231956,-7.957181,-9.895786,1.188265,-3.048067,-9.309700,7.613184,-4.463571,9.598842,8.959971,-3.329743,8.611889,-2.026789,-1.796544,-2.157638,-6.585596,-0.939752,1.114464,-9.452779,1.580487,-7.435424,1.141814,-9.755741,4.092364,8.580369,-5.711822,6.706150,-7.519434,-2.536268,4.711918,8.909045,3.604801,7.605676,-1.283177,5.895536,-0.042554,8.023419,1.765504,1.582007,0.439450,-0.881851,-4.057203,9.155305,7.443223,0.751588,-2.672209,-6.446545,-7.198376,-3.637259,-6.242735,-9.562769,0.086199,-9.380276,-1.555349,5.510104,-7.333562,2.358220,-8.026761,6.363204,5.789328,-9.503165,5.059129,0.909549,-1.939961,-2.579956,-7.866200,3.512029,-7.935307,-6.892592,7.200735,-6.203957,5.561259,-8.673650,-1.083031,-0.355099,-3.589384,-5.620256,2.065550,-1.300757,9.783316,-3.313489,4.540634,-3.907423,3.832022,-9.989444,-4.008698,-0.853034,8.807345,3.383689,4.491742,5.837433,7.096721,8.244087,6.185783,-1.824251,2.023973,-0.429360,3.952596,-4.228266,-7.300763,3.005054,-4.201306,-9.345668,7.642465,0.242836,9.119367,-1.103163,-9.186764,-1.061189,4.862526,3.048681,4.062946,-8.720664,-5.273896,-1.221186,4.490142,7.616485,1.917264,7.644396,-0.203795,6.151834,7.750540,-0.304784,-7.706241,-8.211191,7.907286,-1.606823,4.172450,0.560643,3.377606,-1.931905,-4.133538,-6.362454,-6.622304,-0.133368,0.136713,-0.917045,1.708722,-4.799643,4.593541,-3.006982,-8.423891,-7.599166,7.343386,9.744928,6.329183,8.288584,-6.351689,2.265725,-8.758405,4.117709,-5.510116,-3.381378,-7.252991,4.282285,2.461987,-5.559654,-8.404511,-4.355305,5.242459,-6.194803,4.270834,-2.996500,-6.582048,-5.046384,9.108635,-6.911577,-6.723302,6.256753,4.677902,-1.988084,-5.843961,5.004875,5.870926,-9.791413,2.730715,9.446673,2.809953,-2.812142,-5.759959,-2.995311,-4.233008,9.146065,4.485716,3.418838,6.335333,-3.388644,4.651885,-9.798580,3.264800,4.204361,8.541327,2.220316,-5.952511,-1.218675,2.782448,-4.533632,6.027449,-1.989628,-5.061998,-8.149308,4.186225,-0.832197,-4.970034,-6.478283,5.053835,-0.163306,-2.635360,8.582382,-0.591448,7.730296,-6.120797,5.930207,6.259417,8.668389,-3.441440,5.893177,-1.035051,-0.361800,-5.911386,-5.716449,-2.317545,8.935198,-8.739018,0.697314,-6.052368,-5.976640,-0.851545,5.411976,4.525285,5.025697,-4.561435,-0.304562,-8.674101,9.032729,1.362537,4.931612,-8.595205,-8.496100,7.574437,2.757747,0.174841,6.812734,-1.245791,7.211106,5.571245,2.463791,-2.153840,-1.691619,-6.307228,1.760883,5.732017,6.272975,6.965937,-8.740398,1.642585,1.006881,-6.259442,-9.803818,9.548988,-6.266847,-4.797093,-4.363728,8.586130,-2.330024,-7.160229,4.130350,-3.835497,3.895176,3.850785,-7.004011,-4.567157], dtype = "float32")#candidate|3943|(1089,)|const|float32
call_3941 = relay.TupleGetItem(func_2458_call(relay.reshape(var_3929.astype('float32'), [6, 16, 11]), relay.reshape(var_3942.astype('float32'), [135,]), relay.reshape(const_3943.astype('float32'), [1089,]), ), 1)
call_3944 = relay.TupleGetItem(func_2463_call(relay.reshape(var_3929.astype('float32'), [6, 16, 11]), relay.reshape(var_3942.astype('float32'), [135,]), relay.reshape(const_3943.astype('float32'), [1089,]), ), 1)
bop_3968 = relay.logical_xor(call_3941.astype('int16'), const_3903.astype('int16')) # shape=(528, 104)
bop_3971 = relay.logical_xor(call_3944.astype('int16'), const_3903.astype('int16')) # shape=(528, 104)
output = relay.Tuple([call_3879,call_3902,const_3904,bop_3930,var_3942,const_3943,bop_3968,])
output2 = relay.Tuple([call_3880,call_3905,const_3904,bop_3933,var_3942,const_3943,bop_3971,])
func_3975 = relay.Function([var_3929,var_3942,], output)
mod['func_3975'] = func_3975
mod = relay.transform.InferType()(mod)
var_3976 = relay.var("var_3976", dtype = "float32", shape = (6, 16, 11))#candidate|3976|(6, 16, 11)|var|float32
var_3977 = relay.var("var_3977", dtype = "float32", shape = (135,))#candidate|3977|(135,)|var|float32
output = func_3975(var_3976,var_3977,)
func_3978 = relay.Function([var_3976,var_3977,], output)
mutated_mod['func_3978'] = func_3978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_4008 = func_3833_call()
call_4009 = func_3833_call()
output = relay.Tuple([call_4008,])
output2 = relay.Tuple([call_4009,])
func_4013 = relay.Function([], output)
mod['func_4013'] = func_4013
mod = relay.transform.InferType()(mod)
mutated_mod['func_4013'] = func_4013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4013_call = mutated_mod.get_global_var('func_4013')
call_4014 = func_4013_call()
output = call_4014
func_4015 = relay.Function([], output)
mutated_mod['func_4015'] = func_4015
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4024 = relay.var("var_4024", dtype = "float32", shape = (8, 1, 8))#candidate|4024|(8, 1, 8)|var|float32
uop_4025 = relay.exp(var_4024.astype('float32')) # shape=(8, 1, 8)
func_4013_call = mod.get_global_var('func_4013')
func_4015_call = mutated_mod.get_global_var('func_4015')
call_4031 = relay.TupleGetItem(func_4013_call(), 0)
call_4032 = relay.TupleGetItem(func_4015_call(), 0)
func_2481_call = mod.get_global_var('func_2481')
func_2483_call = mutated_mod.get_global_var('func_2483')
call_4033 = func_2481_call(relay.reshape(call_4031.astype('float32'), [6, 16, 11]))
call_4034 = func_2481_call(relay.reshape(call_4031.astype('float32'), [6, 16, 11]))
func_1813_call = mod.get_global_var('func_1813')
func_1816_call = mutated_mod.get_global_var('func_1816')
var_4051 = relay.var("var_4051", dtype = "float64", shape = (35,))#candidate|4051|(35,)|var|float64
call_4050 = relay.TupleGetItem(func_1813_call(relay.reshape(var_4051.astype('float64'), [7, 5])), 2)
call_4052 = relay.TupleGetItem(func_1816_call(relay.reshape(var_4051.astype('float64'), [7, 5])), 2)
func_2330_call = mod.get_global_var('func_2330')
func_2333_call = mutated_mod.get_global_var('func_2333')
var_4062 = relay.var("var_4062", dtype = "float32", shape = (135,))#candidate|4062|(135,)|var|float32
call_4061 = func_2330_call(relay.reshape(var_4062.astype('float32'), [5, 3, 9]), relay.reshape(var_4062.astype('float32'), [5, 3, 9]), )
call_4063 = func_2330_call(relay.reshape(var_4062.astype('float32'), [5, 3, 9]), relay.reshape(var_4062.astype('float32'), [5, 3, 9]), )
uop_4068 = relay.sinh(var_4024.astype('float64')) # shape=(8, 1, 8)
output = relay.Tuple([uop_4025,call_4031,call_4033,call_4050,var_4051,call_4061,var_4062,uop_4068,])
output2 = relay.Tuple([uop_4025,call_4032,call_4034,call_4052,var_4051,call_4063,var_4062,uop_4068,])
func_4070 = relay.Function([var_4024,var_4051,var_4062,], output)
mod['func_4070'] = func_4070
mod = relay.transform.InferType()(mod)
var_4071 = relay.var("var_4071", dtype = "float32", shape = (8, 1, 8))#candidate|4071|(8, 1, 8)|var|float32
var_4072 = relay.var("var_4072", dtype = "float64", shape = (35,))#candidate|4072|(35,)|var|float64
var_4073 = relay.var("var_4073", dtype = "float32", shape = (135,))#candidate|4073|(135,)|var|float32
output = func_4070(var_4071,var_4072,var_4073,)
func_4074 = relay.Function([var_4071,var_4072,var_4073,], output)
mutated_mod['func_4074'] = func_4074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mod.get_global_var('func_3191')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_4133 = func_3191_call()
call_4134 = func_3191_call()
output = relay.Tuple([call_4133,])
output2 = relay.Tuple([call_4134,])
func_4136 = relay.Function([], output)
mod['func_4136'] = func_4136
mod = relay.transform.InferType()(mod)
output = func_4136()
func_4137 = relay.Function([], output)
mutated_mod['func_4137'] = func_4137
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4210 = relay.const([[[-2.277774,6.972404,7.997813,5.497168,7.666133,-3.461769,-5.397544,-0.988392,9.166760,-8.944203,5.188710,-0.473935,0.718171,5.844928],[-6.067522,-6.036565,9.407322,7.899482,4.662045,9.856960,-1.547778,-9.990124,-5.963736,2.545201,2.763824,-1.366452,-4.227354,8.500016],[5.664219,7.083443,9.397436,-7.753340,6.557920,-9.517409,-3.992821,-9.093599,7.374726,0.046039,8.009193,5.813900,-0.899745,2.665192],[-9.146788,5.019389,4.813657,2.531017,-3.019235,-5.885179,0.154119,5.615138,-7.073733,8.966539,-3.620950,0.080304,7.182229,-2.913408],[4.504996,-5.317553,-4.975552,0.259805,-4.056582,-4.511209,-7.195054,8.574633,5.343889,-9.403563,-7.985871,6.114092,-3.806026,-1.046013],[0.673968,-2.514798,-2.041570,-5.097668,-8.841291,6.838332,-7.744121,9.629416,-4.061660,6.021183,4.199902,5.855164,5.803182,-0.932425],[7.401665,9.790975,8.401809,5.298110,-8.293351,-7.033295,8.270611,0.028761,-6.455734,9.122457,1.923764,-0.274577,-0.232903,-5.413367],[7.600557,4.704926,2.134209,7.481073,-3.603157,4.729637,0.535917,2.381663,5.627914,-7.430415,-9.941192,-6.987512,-9.790838,-1.078681],[-9.403363,-4.484280,-2.905998,-3.718707,-2.506531,-1.307316,5.911676,8.092159,-6.629098,5.832708,-8.584722,7.727991,7.831028,-5.991086],[-9.600270,-1.901083,-0.387354,-7.762990,2.476288,-3.748909,5.647695,-4.125676,-8.115009,0.055394,4.522089,-1.729665,-0.018580,-3.370571],[2.596088,-2.954482,7.132083,-1.414509,2.394858,-2.035321,-1.463947,3.304343,-6.588759,-4.991321,6.560110,3.234179,-4.810415,-6.880878]],[[4.412520,9.811602,-4.409598,-6.874030,-0.617396,0.052770,-8.458368,-5.005331,-8.086251,-3.845584,-5.373673,-6.632042,-0.675825,-9.247112],[5.805231,3.932998,9.430768,-1.821467,-3.547203,5.112818,4.079306,1.749926,9.023764,-8.681777,8.405250,-2.195578,8.061719,5.972781],[-0.563160,7.260665,6.230013,-1.254706,0.557405,-6.094165,8.418689,-4.176926,-4.474810,-1.899058,-4.323383,4.082660,6.883892,0.915265],[-3.170275,-1.862290,-3.586437,2.200266,9.836153,-6.818806,-1.326760,-2.138438,-5.820392,-3.051330,-8.656609,-8.411925,-5.481932,-1.019217],[6.691420,-3.283424,5.658944,-8.912013,-1.360012,2.288588,9.442107,-5.255695,-8.105160,-3.980754,-6.342825,9.874786,3.951181,5.118493],[4.515776,-6.167381,1.353876,5.311479,3.924755,-8.914793,0.343096,7.857731,3.339289,-2.372738,7.468626,-3.466774,2.989804,-9.215612],[-2.761917,-9.910621,-2.184606,-5.772471,-9.274731,-9.533434,-2.021928,3.240584,-7.624595,-4.176066,4.962295,3.595959,1.012989,-3.364058],[7.581406,-5.244299,-1.365832,1.000363,5.304084,-8.929045,9.431377,5.028767,3.747205,8.476633,-0.365442,1.132615,-1.243356,-2.560019],[-8.763971,4.102357,4.539247,4.010340,-0.091711,-6.122839,6.438863,3.984379,1.081484,-1.260491,-9.989015,-0.345438,6.763941,-2.502198],[-1.708994,-4.968239,2.111609,-3.524216,9.461455,-7.511970,1.455571,6.179235,4.953925,8.359116,0.826887,4.587593,-6.528633,-6.203073],[8.841423,6.999115,1.065018,-1.465237,6.318037,-9.854506,6.208459,0.336023,7.944071,2.624369,7.664325,-2.167171,-6.274539,-8.560110]],[[5.241290,-2.240033,2.290123,9.191422,1.507032,6.576199,-0.612063,5.989271,-8.557599,-0.273404,5.632249,-7.789150,5.086838,-0.230014],[-1.064756,-6.628636,6.444001,-4.158947,-5.826429,-3.125475,-8.269115,8.525954,6.027517,-3.969311,5.538999,0.512560,-7.331793,9.781633],[-0.904277,2.507629,1.132632,2.322659,-6.109486,1.024996,2.106468,1.447864,-2.707394,-5.022333,0.956093,9.557252,-4.395616,-2.588972],[1.847969,-8.306077,9.203418,-2.863448,5.156461,9.080886,-4.394642,-4.420294,-7.985361,3.743498,-0.331033,-5.500453,-4.806443,-2.440286],[5.024543,7.385403,4.710055,-2.180089,2.429994,3.074946,-7.237096,-7.032044,5.451171,-9.255410,-8.863600,-7.062344,-6.251209,2.335426],[2.525533,4.123424,-5.468088,2.208726,-3.752301,-2.293445,-3.963289,-2.513076,-9.173858,4.691300,9.799939,-2.355088,3.245872,7.697880],[6.063010,-8.754500,-5.844734,3.881104,-6.148557,-4.628355,4.763731,-9.808635,-9.164471,-1.200785,-9.824184,2.291242,-9.684996,3.577044],[-2.307957,3.975335,5.485266,-1.023130,9.657392,-1.050154,-4.039602,-2.150111,7.379286,-8.839087,0.047034,9.343625,-1.748165,4.739885],[-8.668704,3.526114,9.268774,-4.490108,-0.718227,1.433822,8.613607,-8.616617,-0.130958,1.556744,4.060673,-1.514272,-0.848146,-3.658359],[-9.931651,0.629105,3.432769,4.049615,5.631427,1.249055,7.651685,1.230976,5.068964,-9.187247,-1.407948,6.359646,8.430373,-8.603164],[8.455440,3.929298,3.368762,-8.033232,4.747300,1.118923,-0.425494,-6.256782,2.493118,-0.865801,9.171163,8.797822,-3.666090,-2.352168]],[[-7.325034,5.377771,6.856113,0.958048,-1.710587,0.100094,1.608740,-5.340002,-2.768071,4.729543,8.655712,-1.071843,2.798887,-4.335171],[-6.759869,5.169540,-2.817379,7.009704,0.770529,-1.347176,-9.973066,8.688853,-1.193616,7.754181,0.817166,7.814671,-3.981521,5.921585],[0.424609,5.198595,-8.941385,-9.191037,-3.081619,3.111838,-4.666517,0.112557,0.631190,-9.767950,-6.590727,-6.797691,0.954417,-0.830176],[8.569983,3.459830,-2.542242,5.653069,5.271500,4.690778,7.251702,-6.235793,-0.495511,-6.800366,-8.560190,5.882592,0.806624,-4.163717],[1.923606,-3.295577,0.549523,1.239891,5.248780,-0.302091,-7.532920,-5.473919,-8.184351,8.025172,-0.495366,4.593296,5.161894,3.836664],[-9.097987,5.171107,8.276983,6.985969,3.751712,-7.611140,8.276922,8.123805,-7.153670,2.674376,-2.510479,2.524482,-4.220647,-9.735447],[8.153236,-6.616784,5.580899,-9.129756,-5.148408,7.563680,-9.750854,-1.217805,2.651903,-9.433559,1.521820,-3.678410,-3.620874,-4.625951],[-6.263383,-5.062745,-8.039493,-1.827615,-0.196978,-7.099492,-3.173233,-3.140297,3.121817,-0.866013,4.778087,-0.365865,-3.849785,-7.709307],[-2.439319,9.277253,0.562850,6.176448,5.527693,-0.290911,-0.734622,-0.624251,-5.187965,7.172917,0.116054,-4.336142,-7.100849,7.455538],[-0.049333,-0.097526,-3.779923,0.403643,1.864561,8.733985,-1.510283,8.480670,6.118439,6.919348,-2.113660,9.885110,-7.323387,-9.147345],[2.463211,9.671460,-0.503768,-3.789441,-6.100258,-4.083952,-0.323016,-3.959604,9.735846,9.956552,8.703050,3.945206,-9.657250,3.797143]],[[-5.088764,9.659729,1.597948,1.582059,-8.477586,-3.456278,-9.125441,0.205160,-6.367282,2.592043,2.048109,-5.562956,-3.433327,-1.131680],[3.085804,8.176805,-9.512561,0.100178,-6.303790,5.145401,-1.986086,0.788682,-2.306713,-1.015934,-5.500077,7.761752,-0.149084,-9.618921],[7.208693,4.529182,-5.851907,-7.133684,-1.265996,-2.661765,0.061157,4.746107,4.928115,-3.553042,9.542009,-4.316547,-7.631455,1.236395],[-0.214293,2.935082,5.614288,-1.950323,-7.608136,-6.572216,-9.387811,6.694339,-6.788886,5.123549,6.361872,0.357103,-4.861565,-5.125009],[0.641100,-3.008521,8.635137,4.322955,-7.226806,-3.169060,7.001293,3.117620,2.641034,4.351165,-5.063756,4.757941,-6.836879,-8.843305],[-5.506716,4.628164,2.861804,7.247903,-8.100283,0.607429,-6.362333,8.830248,-7.488375,9.787704,7.487570,8.983713,-2.373179,2.169042],[3.729037,6.873958,-7.588347,-9.442210,-4.353974,-3.091452,-2.276789,-0.893191,2.137435,-5.560124,-4.925280,5.570485,-1.339802,0.264377],[6.367889,7.629900,3.369294,-2.380225,-3.060008,7.098607,1.245674,5.023275,3.949117,-5.879092,4.931784,-5.855214,1.226595,9.854647],[-4.237748,-3.607968,3.457231,-1.662560,-4.438084,-2.872447,6.144576,-4.849344,8.155093,8.057085,6.585422,6.430589,-2.738057,-0.684827],[0.839279,-7.935665,1.051014,4.116839,-9.153826,6.888764,-9.491139,2.647176,6.720845,-2.577247,2.818988,8.266989,-7.805529,3.264020],[-6.250770,-3.958185,7.982100,2.020710,1.858961,5.699622,-9.588695,-3.160145,-4.510175,8.405816,3.341924,-8.108480,4.631719,0.512608]],[[-9.401658,-4.189397,3.870346,-5.062118,9.765285,2.670488,-2.758107,6.283766,4.181461,-1.333696,7.966868,4.448726,3.340126,-7.486665],[2.945430,-5.316656,-6.906536,-2.356903,6.408335,7.918875,-7.456436,7.917573,9.016594,9.348072,2.438598,1.883405,8.545580,4.333544],[-2.158922,2.598587,-4.449068,-0.024032,8.913077,-9.794767,0.243463,8.782823,-0.297617,7.363224,2.758856,-9.596284,-2.279869,-5.237553],[-7.290772,-5.590354,2.925504,-3.108937,-4.548849,-1.174820,7.771215,-4.048553,-3.800419,-5.031866,0.981871,4.632614,-7.844757,3.458971],[6.771133,1.040083,3.032689,-3.147800,1.759328,-3.611168,4.748610,6.353232,6.880647,-6.661703,-4.626352,-8.397500,-6.742221,-2.272680],[4.438236,6.080918,0.180745,-8.647224,-8.040407,4.228762,5.044359,9.325889,2.189426,7.840558,7.168237,-1.238800,-0.070117,7.966380],[-7.243959,-3.886932,7.115463,-0.492467,-6.654955,7.109680,-0.023724,-2.776906,3.202761,-6.154186,6.293726,5.595497,8.917719,-1.998590],[9.352540,-8.836524,4.532767,8.677243,-2.955781,-0.150670,3.660005,-5.028122,-6.110650,7.403465,-6.165393,-7.828250,-6.297212,-3.160043],[-3.154641,9.444764,-2.929051,5.650195,-6.917902,-3.655957,1.356158,3.378266,4.413060,-8.553803,3.600309,5.901207,1.821837,9.262293],[3.680571,-8.055507,-8.413663,0.724944,7.497851,-4.525519,-4.303605,1.795860,4.525421,-6.318950,-1.023974,4.734073,-8.234558,7.880951],[-1.799856,4.469851,4.847205,2.537207,-2.788463,-0.367905,-1.959328,5.872419,-2.484555,-5.809822,-2.367967,-8.627956,1.754625,-4.826904]],[[-5.529024,7.699998,-0.454248,-9.436014,-1.662983,3.079048,7.369177,5.693961,-1.626805,-0.634240,5.004225,5.312367,1.628710,-8.863750],[5.351038,-7.849834,-9.055673,-0.106288,7.148866,-8.960407,1.519631,-8.077156,-4.409241,-7.058009,-2.756553,7.818806,5.158519,9.168316],[-7.713607,5.804993,-7.960451,4.282445,9.061985,9.142043,-3.123672,5.296701,6.197331,-2.821744,7.064996,3.415956,8.200727,7.311508],[5.849676,4.943702,-9.273194,0.361648,7.983297,1.310220,-3.005993,4.715038,4.523914,-6.281507,-5.058049,-9.486411,5.110754,7.775866],[-8.305055,0.007746,-7.413286,2.173987,4.925975,4.947466,5.104517,-7.003665,-9.449269,-3.301999,-8.828930,-8.759958,-9.477371,-2.375248],[-5.524705,-5.648442,-9.027830,-0.782547,9.232226,1.899299,-8.152696,3.371649,0.226934,-1.981818,7.273379,5.017704,2.748281,-0.754671],[-5.286019,-8.710034,-0.747748,6.215257,-4.300210,9.400636,4.871553,4.921418,-3.570283,6.354351,-8.740999,6.192816,0.815210,7.116362],[-4.602506,-2.827176,-3.303002,-2.674091,1.427302,8.559211,9.633044,4.933843,4.240296,6.971727,9.552512,6.180459,-1.434012,7.192119],[-6.388717,-1.935933,-3.967958,7.684793,7.010087,-1.722144,-6.963168,9.510931,-9.212743,-4.128248,2.551739,8.378202,5.083303,-1.313099],[5.152094,7.712635,-0.097941,9.701690,-3.373611,3.801927,-2.965621,-2.124441,7.842622,-0.020564,7.871663,3.003302,-0.022008,0.851498],[5.826877,0.954385,-1.561334,-0.619494,1.075760,3.879662,5.952935,7.030391,-8.046876,-6.098130,5.107661,-0.053973,2.158771,7.115327]],[[-7.956047,1.902011,-0.599711,6.966160,6.890230,9.057743,7.234333,-1.976903,1.753678,-1.748928,-0.455280,0.476249,1.754542,-6.778492],[6.740174,4.110727,-4.977804,-8.859403,0.827894,9.305072,8.503689,2.716185,-6.436763,0.627907,-1.078820,1.955880,-5.392130,-4.891985],[-5.307983,5.352754,4.755502,-2.841167,0.917475,-3.495597,-6.204656,-1.941494,3.558781,-3.352452,0.332884,8.549834,0.095017,-4.989282],[-5.409579,1.618793,6.296971,-7.372213,2.057272,5.103860,2.828364,-6.126332,8.097503,-5.285796,-1.230096,-6.788964,-1.180019,8.890960],[0.525009,-2.959959,5.473745,-0.849319,-4.383005,9.974301,2.517165,-7.980559,-1.868015,-5.760652,2.156299,-9.097106,2.573986,-0.116140],[2.534586,7.683173,4.730063,-6.345953,-6.729794,-1.560217,7.584125,-9.520550,-4.342106,-8.087659,3.418514,-0.915147,1.290813,6.482262],[-8.660229,-5.484594,0.609481,-0.710470,4.849604,4.219060,7.301774,-8.849229,0.696269,-8.449886,-0.190630,3.553215,1.698390,-9.955514],[-0.196644,-6.781599,3.947964,-5.984962,-0.848144,-3.090628,2.649863,6.955812,2.580915,-7.793853,8.328416,-1.349947,3.960194,3.894225],[5.411638,1.315923,5.395280,-8.745918,-2.075140,-7.054250,1.245675,2.285080,-5.958613,-8.331992,-2.202333,1.558260,3.432777,2.997951],[4.792969,9.278236,4.425545,-5.347977,-6.817183,5.435991,-6.798577,-9.738842,-6.700620,-5.457626,-1.933294,-3.282636,3.383500,-3.085272],[1.582185,5.907043,0.381657,-0.402434,7.136566,1.925196,9.437935,4.048316,-0.572902,-3.386353,2.895726,-1.779082,0.791434,-9.104546]],[[-7.804700,7.741540,2.716117,-1.345498,9.214847,6.568475,3.601586,9.594928,9.863152,-9.496166,-5.813901,4.839243,-2.443129,7.935778],[-0.977810,-7.812741,4.046735,7.201082,0.141262,9.393362,-9.887189,8.040223,7.658930,-1.934660,5.333359,8.934765,2.075401,0.376295],[-7.370349,9.643635,5.342718,7.828854,7.949303,9.213374,-3.020354,-6.441325,5.141156,-7.597324,-6.385666,4.154114,-9.955933,9.295982],[8.076926,2.207476,5.275078,4.986594,-2.095225,1.548705,6.493959,-1.011484,3.193973,-8.123417,6.698373,-4.758109,0.047606,6.546024],[-6.645865,-0.011049,-2.519808,0.304102,-2.888743,-9.486515,7.575942,4.291465,-1.320645,-0.349437,-7.603285,-3.292819,5.138439,9.456295],[-8.482730,-4.849122,3.845268,4.478339,-6.941996,5.442515,4.571127,-4.935188,-9.146017,0.666179,7.457158,-6.129461,-5.614430,4.599091],[6.168446,-4.879691,-2.037950,-5.817387,0.688835,7.085446,-2.303611,6.907625,-2.742011,-6.546041,4.887036,5.315753,4.258693,-2.571776],[-0.088209,-9.202004,-4.276301,4.212200,2.661179,-1.929532,5.787003,7.538736,-9.310476,8.438308,-1.693508,7.314862,0.037048,-0.404595],[6.036776,-6.261019,0.959490,4.984820,-6.359037,-8.233696,7.560789,-3.103358,-5.429181,-0.861848,-5.736289,3.819038,-6.260024,-9.395525],[9.652838,-5.425463,5.901229,-7.855637,9.412830,-9.140938,-1.269668,-7.925857,9.868353,5.823163,-4.318987,6.240867,4.896826,1.833796],[0.676491,-5.330792,-9.428148,7.992480,2.675050,-6.839280,-1.409104,-3.844639,2.559544,-2.122920,-7.513246,-8.594577,6.977347,2.291434]],[[-6.274908,-1.423628,6.415053,-6.813855,-9.632432,0.947239,1.787799,-2.808678,5.337627,6.141555,1.811694,2.687116,3.372097,-0.338157],[4.654043,4.097766,-0.429264,-9.619161,-1.657789,-1.181187,-5.064861,3.985014,2.531525,2.742410,-8.928355,-3.100586,-0.988993,2.187876],[2.241372,4.225919,-2.545344,6.378615,-4.704163,-2.896174,-8.904223,3.375666,-5.875164,4.218767,4.491999,-0.099294,0.368689,3.323194],[3.358923,1.407778,6.366571,7.873967,0.216544,-7.330192,-9.960527,0.080678,3.287056,-3.295053,3.689451,-1.371582,-1.776025,-1.475700],[1.578950,-5.997070,1.799564,6.398551,-9.613733,-1.127047,7.120037,3.668889,0.207866,0.574648,-6.114256,-9.691591,0.217990,-7.789527],[-1.506120,3.796219,-8.231399,-0.417472,6.573144,-9.442422,-3.408763,5.267333,-3.676898,-5.659822,2.718733,-3.121927,2.134659,9.368957],[3.990287,-2.785528,7.377229,4.882377,8.696131,1.894780,-1.376077,-5.530538,-5.784336,-6.167767,7.669927,-5.134680,-8.342937,-2.084417],[8.866005,-9.547692,0.860582,-7.465912,-1.867381,-9.124380,9.133107,-3.911913,-1.061504,0.290917,6.917146,6.246375,-3.258902,2.810851],[-4.867426,-5.497594,-9.156479,6.030429,0.644318,-5.759067,9.304385,-7.031943,-3.256361,-3.669376,8.791073,1.354777,-7.466768,8.892322],[-0.849518,7.210721,-0.014384,-9.022849,6.536315,-3.457279,-7.394829,-9.099053,-5.651101,-6.868763,-8.981060,8.893618,-0.466136,-6.118581],[4.878846,9.394472,-6.435058,-7.266449,-1.564532,5.482520,-2.311941,2.511014,-2.444784,1.902835,-9.649045,6.259319,-8.341720,-2.673754]],[[4.391815,2.525678,5.657636,-7.082460,-8.545614,-2.444269,-0.269353,-6.242805,-4.352900,5.353441,1.893271,6.931800,-0.711482,-3.065962],[1.154877,-7.754519,7.327993,3.038077,-5.306298,7.184763,-9.483709,-2.542533,8.061262,-6.107766,-7.541524,0.817544,-0.074892,8.654401],[4.408249,3.723543,-0.855419,-3.725165,-7.897989,-4.816313,5.794984,8.652426,-3.587128,-8.490787,-8.383105,9.158482,-8.208458,-9.895414],[9.398488,-2.593454,-1.189186,3.807517,4.290586,-3.574693,3.898041,-4.310343,-1.970950,-7.088003,6.033909,1.078976,5.771159,-8.612692],[0.732513,-1.926584,-6.213653,7.012900,8.456933,-2.150492,-1.657075,-6.845054,4.745274,7.096978,-7.676637,-3.828833,-0.591923,6.742367],[-5.108309,-7.057342,-2.024994,-6.691678,6.031076,3.932110,-5.464652,9.101670,6.425397,-9.182470,-4.097047,-5.971606,-8.398992,5.851029],[-1.017880,-5.060404,-4.710078,-1.684243,-4.304131,-0.153976,7.023751,-0.886735,2.745972,-1.754183,7.870234,9.404530,-5.758657,-6.072719],[6.699104,-2.045811,-4.419899,-9.091187,5.246306,3.669862,-0.975561,9.274907,-9.683250,3.967738,8.085329,-1.522333,5.965718,-8.063777],[7.983671,-4.952664,-3.495287,4.785297,4.256168,-7.463542,-0.780526,-3.045014,9.151817,-9.009376,3.239887,3.363968,-1.474592,2.739480],[0.156136,6.274634,-2.595787,4.655232,-4.491196,2.413879,5.460798,-7.123868,-2.594419,-2.738078,-2.509134,3.726274,-0.361806,-2.936521],[-8.192528,-4.421102,-6.585218,-9.758700,2.498730,5.649221,-8.157492,-6.882773,-4.495330,-2.472168,7.455731,-4.481538,4.079246,-9.668551]],[[-4.574684,-5.968006,-4.279992,9.459157,2.854757,-9.819523,1.000297,-2.138663,-6.066388,4.570982,-1.184448,7.381096,-8.895599,9.441671],[8.977245,-7.647721,4.524946,-9.853473,3.113777,-9.260521,-3.123070,-7.029032,-2.463503,1.349840,0.698449,-2.575553,-2.049854,0.656288],[6.989865,3.758965,-7.451467,9.112794,-8.056192,-8.470076,2.936537,-2.610243,3.711514,7.085510,-5.316878,-2.091832,-4.264402,6.370517],[6.622206,8.220620,7.790738,6.446503,-9.517280,1.906530,3.269689,3.182371,-4.682740,-7.063014,-5.266156,-5.320290,-3.358578,-8.123247],[9.840680,-0.509868,-6.819855,4.643938,-5.708747,-8.627613,3.415740,3.389109,6.374638,1.491139,6.545303,3.215361,-6.379369,-2.121340],[-2.339558,1.875140,-7.377285,-5.018524,1.052489,-9.723551,0.864275,3.342158,2.482010,6.725988,5.526085,-1.590548,-4.937921,-1.467350],[1.361692,3.425850,7.380376,0.319717,-2.995640,-2.082069,-2.586784,3.574647,6.820004,-2.840284,-4.970022,8.800659,1.715202,-7.758230],[0.254089,-2.968049,9.279608,6.271994,-5.113490,-0.574716,-7.925769,-8.696451,6.993228,-0.695550,-0.587919,6.285252,-2.987313,-5.361994],[1.232142,6.989024,7.629189,9.459180,-6.730649,5.363009,-7.919997,8.972414,1.617195,0.239537,-2.085853,8.958675,-7.482302,2.340365],[-2.063153,-1.342045,-2.331450,-7.418768,1.029296,-8.813632,-4.683122,-2.821615,9.384796,-1.175734,-2.265182,8.825994,0.881481,1.348153],[-6.927390,8.242891,4.782646,-4.562962,7.698637,3.445670,-9.140836,-0.525628,-6.186174,3.576303,6.814793,-7.673578,3.288359,-1.626373]],[[-3.220629,4.213473,-4.219347,2.449846,-2.960460,0.017462,8.303746,9.578357,-9.283437,-9.706967,-0.376778,-7.703842,6.512669,0.632811],[-5.312409,-5.016751,-8.799344,8.324432,-3.505736,-2.176743,-6.060695,-9.502310,-1.149333,-5.758274,-0.345784,2.370551,-4.457027,-2.053123],[-6.079824,3.332224,9.537528,-7.564837,5.456769,-3.459334,-6.072414,-1.346833,-3.539337,-4.725301,-3.639589,8.566206,-1.606887,-7.616498],[-9.126742,-2.283410,-1.014502,9.624293,0.377597,5.252481,-7.870769,-5.722029,-6.846689,1.952902,-6.095458,-1.868187,-6.789341,8.138390],[-2.810269,-1.286540,-5.767317,-4.459193,-2.454858,-8.471570,3.454165,-4.591951,3.861352,-9.734388,3.282785,-6.504484,-1.157614,8.968780],[-4.691506,0.518626,-7.585551,7.137900,-3.478527,8.341613,9.067064,3.543799,-9.197445,-2.568130,-9.303507,2.153965,2.232026,6.441016],[-4.509815,-3.322006,8.300624,-4.989583,7.693378,-8.332167,2.857893,-0.599112,3.504379,3.944754,2.603243,7.556626,-9.735568,-6.401142],[-9.932056,2.083640,-0.364758,7.634515,7.008846,3.492857,4.657529,7.651387,8.682713,-2.955561,2.937735,-4.402932,8.161790,-9.855254],[0.578227,4.495068,6.236530,-0.707538,4.596322,0.483601,3.473626,4.956494,3.001155,5.327818,5.802164,4.622585,6.195579,9.710834],[-6.044264,3.649375,-8.867015,2.216708,4.586677,7.163271,-0.043603,-2.631887,8.075070,-0.953233,-2.570526,-3.460850,6.521410,-8.973630],[5.491460,-2.666614,1.152808,2.156715,-1.638462,2.691030,4.739457,-9.599039,-6.272101,2.893695,2.981337,-7.564210,-1.262511,4.143375]],[[-7.322479,-7.566029,8.267444,6.562415,-9.041709,9.545374,-5.083862,5.142423,8.840261,2.832625,-8.516802,-6.420822,-4.204334,0.474006],[0.254850,3.754604,-9.428743,4.672387,-3.190800,-2.749543,-1.176019,4.282203,9.324182,-4.179972,4.305420,-4.935749,-8.838614,4.963431],[6.559928,6.282862,0.155134,-9.268085,1.178933,5.432260,5.409807,-2.895000,2.907855,-8.139858,-1.673123,-5.348786,-7.513675,6.691499],[7.919318,2.169886,0.543345,8.868891,2.063143,-0.316082,2.544661,-6.106121,-0.006119,-3.470810,8.075004,-3.178972,0.230023,8.367370],[9.716464,8.703523,8.202919,6.370441,9.046955,2.538097,-7.305997,2.576506,3.526959,-8.538764,3.827238,-3.758385,1.738325,-0.801438],[2.559666,-8.560711,7.620890,8.778913,4.949898,6.849101,8.502772,4.726082,6.548649,6.561009,9.215387,-6.323987,4.194242,9.760394],[2.173717,2.320790,4.111161,0.692014,7.967427,3.497316,6.714086,-1.776193,1.885886,-0.602314,-1.351532,4.608952,-8.540930,-2.813082],[-5.698869,-1.865839,-5.644250,-7.078094,-0.799254,-0.895773,-9.879125,-9.148936,-5.749496,-9.576893,-6.647516,-8.683554,0.531297,-9.485266],[3.471546,5.307312,-4.808927,7.953454,7.941052,-7.585407,4.783049,-9.730569,-6.983592,6.792088,9.158189,-8.321843,2.479910,-7.017112],[8.638950,-2.592349,-1.337880,-0.038596,5.878667,9.312800,-2.453226,-3.453459,-1.282296,2.021604,3.140184,9.886788,1.628659,6.819939],[1.288004,7.801115,-1.828909,0.678550,7.287274,-9.305120,-4.380438,9.424781,3.131600,-2.581692,-2.968378,6.117309,0.755051,-4.863066]],[[-8.813902,5.594271,-7.932230,-7.392646,-9.809092,2.329650,-8.486142,-3.870104,4.796832,3.759434,-9.543650,-9.659933,9.305298,-8.733078],[-3.383832,8.142409,-5.537980,-0.884552,9.162868,-1.194117,5.282572,1.811827,5.007008,-0.466564,-2.225952,3.356350,2.083402,5.239678],[7.688567,7.312689,2.141638,8.639111,5.892825,-7.374285,-1.436415,-3.513937,-5.400051,5.914007,-3.847244,-2.646434,1.522976,5.967756],[4.169755,-9.513157,-8.101091,-3.429741,-2.948101,-3.416269,-8.652216,4.492787,5.215392,-0.846179,9.466066,9.445233,1.007998,-0.560973],[8.226543,3.602453,0.891632,-2.759233,-4.684207,2.049732,-5.225053,-3.418969,-2.557789,5.404587,-6.692572,6.985080,-7.666199,7.380039],[-2.339599,-1.938823,0.107962,-7.828836,8.495611,-8.630641,2.300649,7.468864,5.787630,-3.511123,5.218355,1.846595,5.827652,6.222892],[1.119669,9.921138,4.514401,-5.533189,-7.090522,6.927502,4.001179,9.860977,4.558335,-4.771037,-0.478056,-1.205732,-5.734537,2.151590],[-4.865424,0.612946,0.054481,8.172199,0.294817,0.875344,-8.451358,0.381568,5.876451,-2.133660,0.126763,4.535037,-0.662460,5.586872],[-6.749770,-4.067689,-4.582859,-1.056059,2.824820,-0.879771,6.395700,-6.506933,-0.841747,5.364952,-3.630218,-0.374047,-9.606159,6.346422],[9.372307,-5.455281,-6.598230,-2.783929,-8.273768,-5.213127,-1.715926,-7.550430,4.646165,4.008046,0.080158,4.274282,-9.100900,0.465728],[6.425391,9.036981,-8.964275,-6.827626,5.174719,9.872179,-9.352232,8.139628,-1.348106,-4.481020,-6.983836,9.067729,5.584854,9.475175]]], dtype = "float64")#candidate|4210|(15, 11, 14)|const|float64
uop_4211 = relay.acosh(const_4210.astype('float64')) # shape=(15, 11, 14)
output = uop_4211
output2 = uop_4211
func_4227 = relay.Function([], output)
mod['func_4227'] = func_4227
mod = relay.transform.InferType()(mod)
output = func_4227()
func_4228 = relay.Function([], output)
mutated_mod['func_4228'] = func_4228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_4267 = func_2138_call()
call_4268 = func_2138_call()
func_2771_call = mod.get_global_var('func_2771')
func_2775_call = mutated_mod.get_global_var('func_2775')
const_4279 = relay.const(False, dtype = "bool")#candidate|4279|()|const|bool
const_4280 = relay.const([True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,True,True,False,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,True,True,True,False,True,True], dtype = "bool")#candidate|4280|(264,)|const|bool
call_4278 = relay.TupleGetItem(func_2771_call(relay.reshape(const_4279.astype('bool'), []), relay.reshape(const_4280.astype('bool'), [2, 11, 12]), ), 0)
call_4281 = relay.TupleGetItem(func_2775_call(relay.reshape(const_4279.astype('bool'), []), relay.reshape(const_4280.astype('bool'), [2, 11, 12]), ), 0)
uop_4292 = relay.atan(call_4278.astype('float64')) # shape=(2, 11, 12)
uop_4294 = relay.atan(call_4281.astype('float64')) # shape=(2, 11, 12)
output = relay.Tuple([call_4267,const_4279,const_4280,uop_4292,])
output2 = relay.Tuple([call_4268,const_4279,const_4280,uop_4294,])
func_4299 = relay.Function([], output)
mod['func_4299'] = func_4299
mod = relay.transform.InferType()(mod)
output = func_4299()
func_4300 = relay.Function([], output)
mutated_mod['func_4300'] = func_4300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3118_call = mod.get_global_var('func_3118')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_4318 = relay.TupleGetItem(func_3118_call(), 0)
call_4319 = relay.TupleGetItem(func_3119_call(), 0)
output = relay.Tuple([call_4318,])
output2 = relay.Tuple([call_4319,])
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
var_4396 = relay.var("var_4396", dtype = "int32", shape = ())#candidate|4396|()|var|int32
var_4397 = relay.var("var_4397", dtype = "int32", shape = (15, 12, 7))#candidate|4397|(15, 12, 7)|var|int32
bop_4398 = relay.bitwise_or(var_4396.astype('int32'), var_4397.astype('int32')) # shape=(15, 12, 7)
func_2813_call = mod.get_global_var('func_2813')
func_2815_call = mutated_mod.get_global_var('func_2815')
call_4402 = relay.TupleGetItem(func_2813_call(relay.reshape(var_4396.astype('bool'), [])), 2)
call_4403 = relay.TupleGetItem(func_2815_call(relay.reshape(var_4396.astype('bool'), [])), 2)
output = relay.Tuple([bop_4398,call_4402,])
output2 = relay.Tuple([bop_4398,call_4403,])
func_4407 = relay.Function([var_4396,var_4397,], output)
mod['func_4407'] = func_4407
mod = relay.transform.InferType()(mod)
var_4408 = relay.var("var_4408", dtype = "int32", shape = ())#candidate|4408|()|var|int32
var_4409 = relay.var("var_4409", dtype = "int32", shape = (15, 12, 7))#candidate|4409|(15, 12, 7)|var|int32
output = func_4407(var_4408,var_4409,)
func_4410 = relay.Function([var_4408,var_4409,], output)
mutated_mod['func_4410'] = func_4410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4442 = relay.var("var_4442", dtype = "int32", shape = (8, 7, 4))#candidate|4442|(8, 7, 4)|var|int32
var_4443 = relay.var("var_4443", dtype = "int32", shape = (8, 7, 4))#candidate|4443|(8, 7, 4)|var|int32
bop_4444 = relay.bitwise_xor(var_4442.astype('int32'), relay.reshape(var_4443.astype('int32'), relay.shape_of(var_4442))) # shape=(8, 7, 4)
output = relay.Tuple([bop_4444,])
output2 = relay.Tuple([bop_4444,])
func_4449 = relay.Function([var_4442,var_4443,], output)
mod['func_4449'] = func_4449
mod = relay.transform.InferType()(mod)
var_4450 = relay.var("var_4450", dtype = "int32", shape = (8, 7, 4))#candidate|4450|(8, 7, 4)|var|int32
var_4451 = relay.var("var_4451", dtype = "int32", shape = (8, 7, 4))#candidate|4451|(8, 7, 4)|var|int32
output = func_4449(var_4450,var_4451,)
func_4452 = relay.Function([var_4450,var_4451,], output)
mutated_mod['func_4452'] = func_4452
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4456 = relay.var("var_4456", dtype = "float32", shape = (16, 8, 7))#candidate|4456|(16, 8, 7)|var|float32
uop_4457 = relay.log10(var_4456.astype('float32')) # shape=(16, 8, 7)
func_2004_call = mod.get_global_var('func_2004')
func_2008_call = mutated_mod.get_global_var('func_2008')
var_4461 = relay.var("var_4461", dtype = "float64", shape = (104,))#candidate|4461|(104,)|var|float64
var_4462 = relay.var("var_4462", dtype = "float32", shape = (1584,))#candidate|4462|(1584,)|var|float32
call_4460 = relay.TupleGetItem(func_2004_call(relay.reshape(var_4461.astype('float64'), [104,]), relay.reshape(var_4462.astype('float32'), [2, 792]), ), 4)
call_4463 = relay.TupleGetItem(func_2008_call(relay.reshape(var_4461.astype('float64'), [104,]), relay.reshape(var_4462.astype('float32'), [2, 792]), ), 4)
output = relay.Tuple([uop_4457,call_4460,var_4461,var_4462,])
output2 = relay.Tuple([uop_4457,call_4463,var_4461,var_4462,])
func_4469 = relay.Function([var_4456,var_4461,var_4462,], output)
mod['func_4469'] = func_4469
mod = relay.transform.InferType()(mod)
mutated_mod['func_4469'] = func_4469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4469_call = mutated_mod.get_global_var('func_4469')
var_4471 = relay.var("var_4471", dtype = "float32", shape = (16, 8, 7))#candidate|4471|(16, 8, 7)|var|float32
var_4472 = relay.var("var_4472", dtype = "float64", shape = (104,))#candidate|4472|(104,)|var|float64
var_4473 = relay.var("var_4473", dtype = "float32", shape = (1584,))#candidate|4473|(1584,)|var|float32
call_4470 = func_4469_call(var_4471,var_4472,var_4473,)
output = call_4470
func_4474 = relay.Function([var_4471,var_4472,var_4473,], output)
mutated_mod['func_4474'] = func_4474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_4555 = relay.TupleGetItem(func_2562_call(), 0)
call_4556 = relay.TupleGetItem(func_2563_call(), 0)
uop_4571 = relay.sigmoid(call_4555.astype('float32')) # shape=(6, 16, 11)
uop_4573 = relay.sigmoid(call_4556.astype('float32')) # shape=(6, 16, 11)
output = relay.Tuple([uop_4571,])
output2 = relay.Tuple([uop_4573,])
func_4574 = relay.Function([], output)
mod['func_4574'] = func_4574
mod = relay.transform.InferType()(mod)
mutated_mod['func_4574'] = func_4574
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mutated_mod.get_global_var('func_4574')
call_4575 = func_4574_call()
output = call_4575
func_4576 = relay.Function([], output)
mutated_mod['func_4576'] = func_4576
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_4711 = func_2138_call()
call_4712 = func_2138_call()
func_459_call = mod.get_global_var('func_459')
func_462_call = mutated_mod.get_global_var('func_462')
var_4717 = relay.var("var_4717", dtype = "float64", shape = (1, 35))#candidate|4717|(1, 35)|var|float64
call_4716 = relay.TupleGetItem(func_459_call(relay.reshape(var_4717.astype('float64'), [1, 7, 5])), 0)
call_4718 = relay.TupleGetItem(func_462_call(relay.reshape(var_4717.astype('float64'), [1, 7, 5])), 0)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_4723 = func_4227_call()
call_4724 = func_4227_call()
uop_4725 = relay.rsqrt(var_4717.astype('float32')) # shape=(1, 35)
uop_4734 = relay.sigmoid(var_4717.astype('float64')) # shape=(1, 35)
func_423_call = mod.get_global_var('func_423')
func_426_call = mutated_mod.get_global_var('func_426')
const_4737 = relay.const([-3.221334,-7.504646,-7.080026,-9.379683,-3.403665,1.224293,6.597917,4.790247,-9.660550,-4.150536,9.129920,-6.993728,-0.404104,7.216894,-9.585810,9.970894,6.049172,2.283568,-5.548784,3.375468,-8.284230,4.306529,6.020342,4.236037,-9.711339,-1.129515,-8.162323,-3.507609,0.893312,1.231996,-1.932215,-8.626054,-6.814823,-6.909910,9.552745,2.531475,-9.334929,-8.637530,3.074150,-2.770354,4.324015,5.359082,0.008239,3.460650,-1.979912,-2.390774,3.401831,-8.486624,8.853894,-0.705495,-3.806736,-2.309659,-3.838374,-2.361582,-0.041300,-0.534085,4.722304,-7.673559,1.877049,9.703665,-3.724014,-0.666361,-7.597118,3.935756,6.259094,5.824564,4.611834,9.198526,-4.021930,-7.912841,-9.135031,-7.591519,-1.214714,-1.488499,-5.837305,3.622607,4.720289,-9.028718,-7.858516,8.117284,0.338005,2.014387,9.608568,1.412654,8.160936,-0.604221,-0.548272,3.191294,5.714104,-4.350565,-4.060230,-1.876159,8.654370,1.346069,-1.850138,-4.636111,2.501969,4.368323,-4.231010,-1.939699,-9.760322,7.325775,-3.420952,2.076675,-1.370357,8.247795,-2.783148,-9.214074,4.560254,9.176286,8.937609,2.065087,-2.736339,5.395673,8.446268,-4.929568,-2.102231,-7.736352,-9.001020,5.260702,8.490301,8.708037,-1.828402,-1.461155,-1.755023,-5.764236,8.896280,-4.573915,-7.369509,-3.735687,-3.456973,0.730635,-6.500987,5.558451,3.313969,1.446776,3.518163,-4.627003,-6.782926,8.004630,5.177079,-9.629487,-2.955276,-6.977136,-5.117763,-0.852737,7.159449,-5.393532,-2.422447,-0.355750,-2.634273,-0.299287,0.416516,2.363531,9.333500,-0.652593,-7.590068,5.148831,7.767256,2.078107,-3.582680,-6.175642,4.127004,8.034363,-6.754923,-0.071740,6.584022,3.272116,4.731743,0.621671,9.705132,3.404402,-4.328311,-6.943640,-4.024861,-8.812183,-1.158226,-4.909216,7.176110,6.629234,-6.596650,-8.543177,-3.533198,-8.657231,-7.298237,0.298300,7.816924,-0.779961,6.880975,8.431549,-1.181182,6.535972,5.043768,6.130096,4.328401,-1.956600,-2.918976,-8.501220,-5.081847,-5.801619,-1.425384,7.653269,1.026981,2.815296,-4.896119,-9.032876,-9.392509,7.505912,-6.678792,-8.715224,9.174487,8.943511,8.499590,2.742415,-2.751741,2.112982,9.229641,-6.562715,-6.955601,0.401402,-2.084830,4.208681,5.279947,-1.965764,8.875489,-3.768292,-2.323362,-0.458531,8.942152,0.355112,-6.649117,-5.469089,6.789870,-9.004393,-2.451859,4.995929,5.344582,-8.360265,1.689609,-3.111799,5.103902,-1.038093,-3.171529,-0.810976,-0.882462,1.244456,-5.687361,-1.954718,-5.657180,4.668201,-6.819898,-2.961033,1.103755,0.859072,3.558947,-8.262711,-7.662616,-6.079396,6.052121,-7.167405,4.390417,-1.517509,8.432901,4.590866,2.510039,-5.923277,4.794767,-8.540716,7.170159,-8.444028,4.409346,-9.814683,3.773189,5.639572,1.267316,-7.184228,6.975254,-1.418663,3.855847,1.629556,-8.026788,-9.160782,-5.638362,-3.753923,-7.364461,-3.126200,2.702869,3.171384,-5.110079,-9.905851,-5.275360,-0.150846,4.246863,-2.663600,-8.506692,-7.194588,-9.944658,4.615655,7.081884,-6.271959,-6.406387,4.464659,6.111713,-1.974624,4.634206,2.971960,3.760906,-0.961141,-4.510126,7.533710,-8.126260,3.909686,-7.141552,4.968306,5.601998,-8.313013,-5.121803,2.101485,-0.724491,1.073979,-5.107152,-2.438170,-5.235751,9.306585,8.967265,-1.776803,-5.161482,-5.520079,-3.606134,-3.363671,-0.150668,3.786994,-4.715375,-0.676851,-6.914300,0.878583,6.731543,-3.965652,-6.429919,-0.954216,-0.508253,4.324607,8.087552,1.692265,9.873653,8.502290,-9.143851,-1.070685,1.346727,-6.061064,0.952761,9.000924,6.606890,-3.359548,1.709746,1.528258,3.569946,-7.040610,5.615584,-7.175747,7.472123,-7.907271,-6.667486,-4.753995,3.916383,6.883038,-7.917817,8.902384,-6.776261,6.743854,6.762555,3.451689,2.317326,1.738375,-7.226366,3.229702,4.700745,1.924391,2.542116,5.077783,-8.783713,8.719858,1.818351,-6.049898,-1.969964,1.810316,2.642873,5.748387,-1.270366,9.877584,-4.797378,-6.505402,-9.759233,-2.592541,-7.989425,-6.940833,-0.113991,6.088911,6.473860,-4.244207,-5.722782,1.303849,-7.174662,-5.939073,3.822106,0.813409,4.566364,3.362090,-8.362120,5.343446,3.520219,3.477049,6.596171,-7.726165,0.889669,-8.492176,-7.883589,9.358146,-5.905198,-1.366107,0.216345,-3.783705,0.557771,-5.627847,5.278033,-6.969594,5.581963,-7.711163,5.924259,3.101915,2.096046,-5.497978,8.634606,4.644355,5.332869,0.919405,3.469246,5.310182,5.545615,-3.742313,7.802911,-1.042072,4.571749,5.762981,3.521677,4.836570,7.520248,-0.116036,6.963577,-0.392358,5.564086,7.788040,5.046618,-0.805812,-1.305753,8.336200,1.301649,-1.337156,4.155198,9.140850,2.583701,6.253809,-3.962184,3.044459,1.936063,4.759620,-9.715386,-5.147981,0.130406,-7.328262,0.325808,-5.920816,9.390625,6.531656,-9.025322,6.434137,2.268668,-0.007550,6.046950,3.213982,-5.375751,9.421229,1.621743,-7.612048,-1.517648,-3.264579,1.030788,3.665854,-5.145693,5.894112,5.324637,-3.071685,3.752691,7.777058,-3.650620,-7.218257,9.068862,9.764227,1.827626,5.932714,6.281698,6.840747,-7.297062,0.315039,-1.654945,-4.739607,-6.810483,-8.428156,4.422241,-1.504041,1.692269,-7.806132,-6.348140,4.506612,-1.517223,-7.027979,8.908534,-3.954824,-6.673803,-8.125019,-8.113483,-4.647634,5.364033,-4.842901,-8.344657,-6.790664,4.342593,-4.491505,1.022855,3.190636,5.037630,2.403685,-5.174662,-7.857561,5.930510,6.201821,3.997733,-3.545692,-6.540901,-0.902106,0.159605,-5.965140,1.909296,1.985635,1.062479,-3.998751,-2.756488,6.533063,2.184536,1.403479,-7.181247,-7.333151,-0.276647,-9.094903,-0.628430,-0.943814,1.646316,-7.814072,1.964217,0.818655,0.023880,7.042769,4.561894,-6.277649,3.934967,-4.756698,-5.272153,2.206119,1.018716,3.255875,-6.140243,-3.818353,1.996480,7.656923,-2.649256,7.851011,-4.518279,2.944414,7.742791,3.727236,8.023916,-5.763520,-3.205955,-8.678687,7.814408,8.759125,5.556171,6.625801,2.878294,-8.047980,-5.868149,3.359425,-0.775558,-0.740604,-0.501110,-4.431017,0.396618,1.802402,5.274002,-6.504305,6.145416,-0.657780,9.464001,6.947411,-6.807940,-1.238540,6.433525,-6.908746,-2.556386,4.603782,-6.954782,-8.139689,-3.221940,9.377413,8.594757,-5.083897,-8.994400,-5.859709,7.927020,-6.310797,4.935344,-1.685205,-0.021181,-4.377085,0.136690,4.197828,-2.489732,-0.234744,8.911035,-4.854804,0.536123,4.460906,7.120494,2.159074,-6.925264,3.909785,-5.759070,-6.907206,-0.624506,2.959168,9.292969,6.881926,-1.365336,-3.946831,0.205376,-8.530075,-2.120808,-3.708544,7.747685,-5.515205,7.487201,4.760804,2.737281,-0.364363,2.210855,7.139795,-6.388350,-8.015339,-4.074670,-0.297567,8.651706,-4.279806,1.882452,6.905932,-1.947981,-8.210189,7.187773,5.445618,9.605399,-1.633134,0.797073,7.139592,-1.992562,-7.814505,9.656756,3.917067,-5.014560,-9.297484,-4.657275,-9.616686,1.649188,0.208225,9.152343,7.582583,-8.644510,7.750085,2.876586,-0.887825,-0.238849,3.648794,9.529788,-2.223433,-1.660692,5.893452,-0.887559,-8.438069,-0.632227,2.372124,-4.389605,4.298403,-5.023356,3.187864,5.661631,-8.088757,-8.961471,2.588636,-2.973330,5.363539,-3.477624,5.133356,9.976613,-6.176983,5.731376,5.977370,-1.889160,8.036690,9.444111,5.034186,-2.594341,-6.365948,9.557900,-3.606305,6.264743,-3.816248,7.934786,-7.270176,9.383431,-6.426599,-4.342607,4.828899,-0.646977,-0.129683,8.812038,9.738180,2.469814,-8.974050,9.953258,-2.382722,8.579905,2.416315,-2.806917,8.364581,-7.565245,4.039545,7.698364,-4.208884,5.082424,7.158455,-0.907226,-3.163679,-8.454725,-1.296363,5.346364,-5.984932,8.677112,6.441337,8.124493,-8.367264,9.119498,9.438927,-2.756932,-9.297771,-0.210731,-1.953712,-5.595745,-8.552983,5.792167,3.757614,3.139643,6.243671,0.579191,-2.783118,4.411938,-4.928646,-7.001984,0.700451,1.545884,-5.837380,7.466031,-1.357831,5.274428,-6.395690,2.214745,-3.154399,4.557245,-5.121845,-7.597444,-5.505639,1.747140,-1.793350,-9.593414,-3.235996,-3.923317,5.681485,2.380251,9.586239,-0.097338,2.769892,4.121862,-1.454015,-5.069436,8.083945,7.450294,-0.017000,2.279311,0.887073,4.371129,1.590416,-0.047466,8.859361,6.127284,6.771817,3.495868,9.092558,-0.900862,2.741468,-4.772832,9.053359,-0.915398,-5.459738,4.364415,2.998058,1.025279,-6.012850,9.470842,4.326948,-5.867706,-2.832070,-4.469793,6.818773,3.271602,8.603575,0.372672,-3.948392,-6.654655,8.992620,-8.255690,-1.952038,-8.914959,0.114484,8.250655,-9.352974,3.859842,8.179488,-3.936876,-0.404003,8.767600,-2.643303,6.805437,4.549663,1.411989,0.521450,9.717610,-3.745810,-8.312145,-7.899265,-0.978662,1.567370,4.736960,1.278477,5.211337,-3.060980,9.579295,-9.813799,9.394371,6.348555,-9.982225,-4.048697,-6.477361,3.997169,-9.635320,-8.577435,-6.180227,5.415445,-0.330841,-3.768644,-8.758388,8.981590,8.006167,-1.728775,9.633609,9.566696,-3.541731,5.269547,-3.224634,8.592193,-8.548933,-6.693211,-8.592552,3.375553,-0.758392,-3.554923,-6.119304,3.678642,0.742776,-5.790969,8.331393,4.889958,8.555348,-9.047798,8.441353,-0.738729,-6.780650,9.458419,-6.551513,4.689703,-8.028389,-4.256772,3.862089,-5.521217,9.331873,5.424720,-8.633568,6.133933,-1.090670,-3.375004,6.815172,7.272675,5.549790,-1.484468,9.987677,-3.473168,-7.287500,-4.265650,-6.381836,-9.987357,1.385976,-6.583553,-3.413374,5.071399,-4.960940,4.896240,5.611763,3.728445,6.127039,-1.983659,0.879103,-4.823736,1.912447,-4.535963,6.553865,-6.318272,-0.580830,-9.293978,-3.315748,6.443120,7.522641,-4.058505,-9.282722,6.178620,-7.887598,-6.616263,6.992866,4.720196,-6.437101,-6.172443,-3.811748,-2.979019,-4.075158,-8.150796,9.002234,5.038221,-2.937891,4.867311,0.841333,-3.179308,-3.091101,6.520426,7.762645,4.015298,-9.796481,7.806939,-5.765734,-0.773950,-5.991392,8.234033,-1.269300,0.128424,-9.575087,3.296270,2.250825,2.469690,4.063876,2.069547,8.795495,-7.415642,7.421128,9.882121,5.190030,-1.971178,-5.964917,1.390085,-7.842008,5.977564,8.751151,-1.836688,-8.003823,0.706907,-4.534886,-1.503211,5.877702,-3.107966,-2.450974,-8.568108,3.673631,2.662240,-2.180035,-4.069066,9.218860,8.065901,3.667379,-3.452632,-0.358916,0.902503,-2.090002,-5.498341,-1.383635,-4.479612,-4.428676,-9.669488,8.638076,2.065686,1.150253,-5.466529,1.958245,4.098001,8.816200,-7.111908,1.140631,1.941800,0.408076,9.233536,-2.851760,-9.631509,-6.996512,-1.814319,2.548752,3.675708,0.791187,3.326506,-2.357756,1.182014,-4.354305,9.163507,4.816940,-7.909346,-8.053701,-2.428924,1.071850,-1.975263,-4.856358,-6.320707,-7.749914,-7.296016,8.558495,4.218444,-7.137858,-8.963207,-1.481107,3.119475,-8.344788,4.128557,1.870306,4.632838,-7.317940,5.432369,-6.919323,-4.733472,4.276733,-0.676787,5.926425,-1.726025,3.496609,-0.750394,-5.884716,5.221358,4.733608,-8.788731,5.518737,-2.546250,7.036582,-9.460219,9.407288,-8.849600,9.908326,0.846752,-6.644655,-4.929292,-4.331803,-4.429589,-2.232445,8.770598,-3.740525,1.523140,0.965570,5.442620,4.854034,-7.610228,9.734419,8.093494,-2.579950,7.289407,7.107350,-8.167839,-2.518945,-5.961140,-6.618850,6.574070,8.620349,-0.925466,-9.967521,7.268813,4.222990,-6.018251,1.743817,6.007640,-4.467269,-8.688339,0.824072,-9.834294,8.145094,-9.057520,-8.550997,-7.007361,-2.982209,8.818126,8.807295,-2.976909,-8.640227,7.184743,3.593713,5.879866,2.039009,1.064935,-5.994924,-4.776694,-7.280304,-1.241202,-1.005725,5.200879,2.851404,2.720234,4.541392,-7.904125,-9.082835,2.518574,-4.979019,-9.245624,8.632348,-3.422240,7.669654,3.842726,-1.216637,-2.487933,3.965913,7.361947,-3.340038,2.727157,2.820616,-1.998714,9.669557,5.045598,-5.951829,5.325010,5.345504,-5.311753,-7.148810,-8.702397,7.753151,-0.224017,-3.300410,9.624684,-3.239469,9.555320,-1.708286,-1.162561,0.251694,-3.911716,4.833782,9.845784,9.667165,2.938872,-7.177989,-8.808884,-5.936060,-3.006995,7.446467,-0.150257,-8.881362,8.944591,0.847859,-7.636286,9.985027,-0.982907,-8.400239,3.742248,1.955819,1.252322,-1.750669,1.592231,-5.503168,-7.070176,-7.457707,-2.278854,-0.959912,7.185377,4.612268,-9.803365,-3.839548,6.809469,8.580629,1.804130,0.140836,-3.263084,-2.594398,-4.001994,6.314238,-0.267812,0.294749,-0.626840,-4.841393,2.381202,4.776644,-5.481721,8.843768,-0.777631,-7.420769,4.929785,-0.225483,-9.099068,-8.117635,-3.907937,1.826571,3.557289,3.551800,-0.368345,1.138072,9.784464,8.808939,9.340994,6.698203,3.186736,6.390925,5.224920,-6.045730,-3.956047,-5.979267,-1.913283,-1.242379,2.795177,2.434986,9.686208,3.302279,5.504995,2.399798,7.403472,-5.057728,-8.775967,-3.600708,-9.784207,3.387805,0.975613,3.667903,8.723693,6.632189,1.874391,-7.529448,9.828390,5.641406,1.846453,3.076784,6.448676,8.100695,3.126072,1.435634,2.131942,8.913869,-5.714738,-9.470413,-2.681844,-0.328531,6.642768,-8.454484,5.835104,5.316944,-2.816349,7.891724,8.352983,-4.475507,-1.203244,-3.385475,-7.967492,-2.458119,-9.942126,2.357701,-0.824125,-3.019256,-9.368998,5.743393,-1.619581,-2.857869,8.447576,-8.976633,3.686439,-3.937499,-6.408275,2.457688,-3.645403,9.916314,-3.567956,8.861539,5.742958,-2.760561,-7.844189,5.659999,8.468409,-5.241863,8.700897,9.911640,2.301352,1.203741,-3.978898,-3.217468,-8.028983,6.627428,-4.276439,-9.269456,-5.251345,-9.715185,-1.167815,0.539327,8.128652,-5.421636,-9.394788,8.740622,9.478078,7.513982,5.678153,-8.384499,4.802274,5.620517,-4.244871,6.926333,-9.247613,-7.497182,4.191723,-8.560790,7.920927,-8.283486,-3.010183,7.843219,-3.685872,7.820307,-3.505064,4.809044,0.461089,-0.213697,-2.300771,-3.350835,3.402906,1.860253,-2.590787,8.781928,2.321088,4.035000,-6.795502,4.114739,1.808875,-9.193626,4.359575,-9.798029,-1.140587,-8.647664,-9.398935,-5.314329,1.306946,2.150771,6.871705,2.202228,-4.429846,5.234762,8.974147,8.209161,9.817960,6.348786,4.510447,-3.576105,-4.206654,9.768056,6.708897,-3.445882,6.316121,2.085638,-6.407057,6.142781,7.252916,0.486365,-7.452089,-2.900828,1.692569,-5.781309,8.011551,-6.770920,0.388567,-4.753373,5.687914,-8.316724,-2.570994,-6.421524,-9.253263,1.667524,-3.012702,9.586015,9.165780,-7.509637,7.617440,-9.785612,8.362784,-8.717488,-3.010764,-5.348872,7.804533,-2.242797,-2.720751,-1.407837,6.310944,-5.825555,9.173973,-7.269043,0.833935,9.573967,0.592252,6.684866,-5.605745,8.403078,8.312024,1.379169,-6.640707,-8.974314,-6.843458,-7.407021,0.627935,3.536614,-1.139982,4.423234,-0.629251,-2.119571,-2.954734,5.903477,5.137595,2.698428,-1.296457,5.291991,6.416952,4.692310,-5.306911,9.661721,-6.524763,-8.204489,-6.005311,1.188306,-4.868926,-2.284581,3.874273,-0.604881,-8.419177,6.127669,-1.292324,-8.598141,7.184182,6.074152,0.494972,9.232416,7.826934,-6.291087,4.996014,-6.429561,1.526214,4.649734,-6.508416,4.682543,7.453981,0.361442,6.047098,7.235296,1.698547,-5.662716,7.056573,9.261568,-1.691530,-7.083350,0.595036,3.611424,5.788707,2.460339,-2.326203,2.345043,-4.795206,7.165572,-4.307483,-1.757697,6.010130,-8.108233,-8.085012,5.984777,5.631674,-5.298544,7.617361,3.733768,-8.573691,-2.332341,2.155886,7.208906,1.460400,8.910090,5.859625,0.207045,-9.913579,-2.530522,7.169646,8.914621,2.816425,7.718856,-5.349855,-1.766460,-7.850643,0.175901,-2.306722,0.031182,-9.939991,2.568728,-0.843599,-5.139717,-3.175451,1.329583,7.652176,-5.522665,-6.208133,4.116313,-7.641093,-2.970876,-4.342289,-9.014103,-6.726001,-9.575995,-0.168239,-7.405152,8.530620,4.750366,1.026678,2.077057,-8.197447,-7.625811,-4.575858,0.202742,2.287697,1.989438,3.801307,-9.228362,1.848656,-7.197468,-2.999494,-6.579840,-0.234696,9.318024,-6.766793,-7.125942,-7.406727,3.417265,-9.685805,7.762141,-3.738429,6.731522,-1.021309,6.215239,3.692068,7.715100,3.349461,7.596123,8.106094,1.005907,7.990040,-2.194739,-5.940637], dtype = "float32")#candidate|4737|(1584,)|const|float32
call_4736 = relay.TupleGetItem(func_423_call(relay.reshape(const_4737.astype('float32'), [16, 11, 9]), relay.reshape(const_4737.astype('float32'), [16, 11, 9]), ), 1)
call_4738 = relay.TupleGetItem(func_426_call(relay.reshape(const_4737.astype('float32'), [16, 11, 9]), relay.reshape(const_4737.astype('float32'), [16, 11, 9]), ), 1)
output = relay.Tuple([call_4711,call_4716,call_4723,uop_4725,uop_4734,call_4736,const_4737,])
output2 = relay.Tuple([call_4712,call_4718,call_4724,uop_4725,uop_4734,call_4738,const_4737,])
func_4739 = relay.Function([var_4717,], output)
mod['func_4739'] = func_4739
mod = relay.transform.InferType()(mod)
var_4740 = relay.var("var_4740", dtype = "float64", shape = (1, 35))#candidate|4740|(1, 35)|var|float64
output = func_4739(var_4740)
func_4741 = relay.Function([var_4740], output)
mutated_mod['func_4741'] = func_4741
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_4779 = func_2138_call()
call_4780 = func_2138_call()
func_2458_call = mod.get_global_var('func_2458')
func_2463_call = mutated_mod.get_global_var('func_2463')
const_4812 = relay.const([4.242322,-1.585198,-3.713337,-6.206563,0.742929,4.838726,6.041921,3.854833,-2.174716,3.249132,8.761557,6.833660,6.353080,3.823095,7.913212,8.584136,2.973168,-6.577248,8.779323,-3.132226,0.474199,-2.020973,1.192274,-3.619698,-1.678437,-5.524847,-4.671747,1.172963,2.883429,-9.671909,4.243218,9.737564,0.662242,-9.093299,-8.597162,7.152622,0.554613,8.573473,-5.698254,-6.412313,7.505801,-7.605609,5.040232,-8.520589,-5.505850,3.203235,-6.058538,9.687215,-1.023114,-0.708256,-8.442491,0.969067,8.614049,-3.058135,-2.489123,-4.400302,-8.571314,2.988791,3.283844,-0.353380,-8.407838,0.008463,-3.483384,-7.590781,2.891592,5.888462,6.177675,6.876516,7.426098,-1.539917,-7.006142,-0.129117,5.108916,-6.652903,8.773394,-1.742975,-6.539774,-3.492436,-9.333635,-1.331760,2.314626,-2.958702,-4.719692,3.775079,3.453559,0.649108,-2.761106,-3.316869,-8.235053,-1.878883,8.924310,9.873620,4.604646,-6.669625,5.133064,3.556725,1.091389,9.872129,1.839439,9.699172,-8.045536,-0.100052,-8.483986,-0.812428,-3.213584,-3.954789,4.925119,8.485076,3.732698,0.463508,-5.287702,9.490877,-3.669564,0.060641,8.775873,-3.098688,-8.379096,7.367241,-4.091219,9.063660,-9.293767,-9.144691,5.873850,-3.510787,-1.426108,1.677584,-6.812548,-6.772808,8.429705,-3.772635,-9.334297,-6.610551,-1.886419,-0.424966,2.074297], dtype = "float32")#candidate|4812|(135,)|const|float32
const_4813 = relay.const([-8.071757,3.422644,-0.705437,-6.803886,2.202548,-0.554958,3.934870,4.907541,5.857763,-8.192515,-7.359870,0.936306,3.220570,-2.965778,-7.101774,0.112850,1.005816,-7.396564,-4.892249,3.359107,6.277128,0.123907,-9.047249,8.987078,-0.286808,2.784244,-5.120425,0.359983,-0.812982,-8.015041,-0.799473,9.851660,-7.029191,0.692414,-1.521313,-1.094900,-8.188335,-8.897846,6.543889,-0.364435,2.668905,-6.656339,-8.419740,-8.494639,-4.279997,-2.558465,-9.907220,-2.729233,8.797296,2.122241,-6.932118,6.216346,4.980505,4.331457,9.311091,-4.492387,-0.592753,-6.766274,1.100311,0.169261,9.166737,-1.539101,5.945259,2.941276,-9.986887,-3.705783,-3.490953,1.222952,8.415755,-1.444696,1.165409,4.753206,-6.208911,-5.339842,-2.596610,6.272762,4.149511,7.015201,-5.917053,8.235493,9.438756,8.796261,-7.353310,3.332657,-2.426383,-5.173599,6.643021,9.577437,-9.419210,8.925333,1.045782,-0.354970,-4.736101,8.353304,-2.452711,6.046729,-0.022169,-4.784587,9.818406,-3.881331,2.939952,7.541103,-2.727121,-0.625431,3.221647,-2.484212,-0.910098,2.211448,-8.252781,2.527320,-7.093736,1.828445,-0.375612,7.388430,7.236293,5.880193,-7.923460,4.105142,9.336058,1.269787,2.748270,9.538821,0.668629,-2.646989,8.959446,-7.968310,-7.084001,-9.192072,4.008229,3.307789,5.853151,-0.175097,2.000588,-2.958480,1.437748,8.402807,2.876534,1.693952,-8.211887,7.514334,1.368745,5.850114,5.221044,-2.145675,4.894581,4.689001,-5.195328,-6.918524,-3.001533,-7.036489,4.718987,-4.548888,-6.427337,4.442681,-4.224779,-1.989941,-8.844196,2.694374,4.091006,4.935053,6.815913,7.985945,-2.282338,-6.576597,3.307391,-8.146757,-2.102714,3.981318,-5.392305,3.419910,7.781122,9.672530,5.767150,6.027869,-1.652240,3.079531,-3.131257,-8.268723,6.127077,7.953048,0.629843,4.448452,-7.875161,3.974546,9.770537,5.771234,-0.527861,-1.353001,-3.980733,3.427249,-6.744902,-1.648495,2.444795,6.500756,9.055833,1.674547,4.606356,3.356103,-6.933097,-2.486618,7.450533,-6.562462,-2.405068,-1.594669,9.936276,-9.043830,-6.995768,-2.616694,4.608690,-8.926045,-4.819174,6.776100,-4.243933,7.888313,6.609449,-4.001857,-9.443100,0.935662,-4.494531,6.942747,5.362844,2.780638,-4.109886,6.151551,-2.036138,6.720015,-5.722079,-7.584178,3.666070,4.872209,1.096226,5.570846,-8.848146,8.568213,-1.574243,-2.574525,-7.427572,-1.223005,3.812733,-1.276276,7.105917,-1.802469,-8.107957,3.338702,8.210996,2.530121,-9.628017,-9.369397,5.616963,2.082785,-5.889961,6.134725,-8.119320,1.400230,1.467437,3.148552,7.112605,-0.902604,-8.121808,3.602997,-7.357878,-9.720334,-6.273615,-3.650194,-1.483096,4.659907,2.996770,8.051289,-1.640182,-8.918985,-0.968211,2.652743,5.224908,-9.488087,9.043232,5.571919,-1.335813,-5.237270,-5.440464,-3.421203,4.722490,5.985744,-8.825202,-1.631741,-3.412591,-5.123546,-4.502510,-1.016492,-7.700945,7.860300,4.966420,0.138941,-6.791310,-8.055522,-1.338055,-0.849922,-0.237395,9.710240,-3.837381,-9.222954,-6.168506,-8.864494,-6.738245,-8.000401,2.697313,-9.723313,9.223574,-0.142376,4.383593,-3.798959,0.663005,9.215276,2.016749,-8.692470,-0.858378,-2.087151,7.077782,9.241198,8.962881,-7.831517,4.247771,4.286971,0.009567,5.943634,-5.839377,-6.667911,-3.423546,-6.232407,-7.327257,0.970830,4.658548,7.367470,-6.675388,-9.971484,1.509235,-6.952303,8.378247,8.877722,4.077274,6.904292,-8.119857,5.178909,-1.136901,-2.313896,-3.851285,0.894722,1.270316,4.089357,-7.855479,-1.776470,-4.815932,-9.503514,-8.602670,-3.431223,-4.004339,-9.554751,-4.460319,4.443989,0.186824,4.676152,-2.462360,9.395736,-7.356288,1.932468,-1.237228,-4.198702,7.898578,-6.483909,-0.082762,7.001672,-8.672712,4.733711,-7.552175,7.995351,8.593177,6.897223,-5.153128,3.302890,2.199585,3.447373,-6.035661,4.994528,-7.947025,-6.196864,-7.900601,-1.928744,6.721418,9.233298,-7.063558,4.310823,-9.287626,9.200183,9.500018,9.141250,-0.542367,-6.394109,-6.896193,-8.657419,4.739089,1.234305,-8.216474,-5.228776,6.203388,7.041964,0.635926,0.857987,-5.399947,-1.624492,-0.319056,-3.851800,-7.333520,6.739636,-7.626799,9.682116,-0.211328,-3.267622,-0.883533,-4.513041,-4.341242,-3.752126,-1.619320,0.817496,-6.487955,-1.750533,9.569934,2.783432,6.991618,-6.348407,-8.442634,5.482626,-4.785485,-3.058046,2.392553,1.589512,-5.279182,0.098675,3.248918,3.361687,-6.872782,-1.107207,6.354352,4.833621,3.820148,-0.440300,9.568650,-1.554690,5.801854,4.871630,-6.519500,6.515769,-8.548790,2.580740,9.432419,5.506033,8.720878,-2.680748,-1.238602,6.847182,1.993332,8.495027,-6.494947,8.994506,-5.228746,-7.759215,5.292904,-8.212986,-9.983260,0.053473,-3.405846,7.857062,9.394000,-0.329628,4.248229,2.447123,-4.636318,9.169454,-7.378898,-0.044722,6.891771,5.006425,-8.858281,-1.651811,-0.325948,8.664107,1.756874,-5.638438,-0.298513,-5.196942,-0.336834,-5.571625,-3.888596,0.995031,-7.482328,-0.938732,-3.275894,-1.254965,8.274886,3.866381,5.050179,-1.358352,9.541769,8.830216,-3.120410,1.557585,9.508681,2.680424,-4.272285,-1.343923,-0.704880,-0.388290,6.312652,-9.485237,-5.524566,-1.664739,-6.226287,-2.234830,9.653176,7.432143,0.672932,-2.564533,-6.942152,-3.491217,9.107681,-3.668188,5.076768,-4.298815,8.814194,5.124435,0.767949,9.603178,7.828746,6.589978,7.459716,-2.774511,-8.076466,7.441611,-4.220761,5.146966,6.773017,0.073142,-8.687950,3.522200,-2.148234,9.846104,-0.167238,7.759323,-0.326097,-0.098953,8.512478,-7.963154,4.765345,1.986178,-6.684879,3.985078,-7.408475,-3.936127,6.029938,-2.260551,0.753848,2.948345,5.538767,3.101585,4.233842,1.727443,-9.493128,-9.122428,-1.743568,7.910012,-5.522777,-4.201996,1.022799,-1.226547,-8.643120,8.794568,-1.766713,7.615689,5.075177,-1.823286,-2.639838,-8.331436,0.693712,-3.900893,-4.334350,-7.921921,4.717230,9.343310,-6.143261,8.746215,-2.539584,-0.777751,9.513216,-8.590208,-8.173039,2.616108,8.064125,2.887593,1.241346,-0.534653,3.590938,-9.335376,6.049539,0.017571,2.304427,-2.751651,3.074772,5.577070,-4.314658,-9.875068,-7.555325,5.890974,9.649464,-8.360243,-9.473913,-8.288952,-2.885067,-9.673102,-7.590176,8.187099,-1.053088,0.816498,-4.661081,-4.334045,4.834241,1.660407,1.255878,4.118815,3.677360,2.311983,-3.545779,0.760000,-3.672777,-2.532465,2.736962,6.674720,5.228123,-7.793169,2.914807,-9.641921,5.297204,-4.294173,-7.331258,9.738563,4.715615,7.517243,-5.873539,-9.492534,2.223530,0.902691,-1.199166,-9.618007,7.501692,6.272839,-0.706324,9.074733,5.059352,-8.252665,1.953106,4.151103,-4.814559,-1.768788,0.098807,0.012076,5.929054,-9.331336,7.488861,5.553036,6.604264,5.263521,-6.569120,4.725036,-3.544357,5.498100,2.959039,2.344082,-6.423127,-2.483812,-5.544500,-5.838716,-9.457863,-1.195028,4.119660,-0.089201,-3.140452,-8.138263,6.324084,0.725999,5.546050,0.283605,8.086478,-0.436321,3.794753,-4.927061,7.020051,5.297352,6.454704,7.756879,-7.225420,7.494781,-5.624878,5.421026,5.175630,0.775176,-0.652196,9.026556,5.850719,7.320037,-3.514110,4.740237,-1.252875,3.874551,-7.867381,-2.836923,-8.086789,7.942873,-4.071140,-4.413316,2.062845,-0.728072,7.270343,-6.068902,-4.963914,4.332651,0.242440,-7.332670,8.280524,0.162452,-0.749391,-1.472248,3.142559,6.377411,8.553245,6.724264,-9.952071,-4.683451,6.058040,-3.628377,-7.142627,-3.066689,-0.916825,9.686727,-8.871381,8.431580,-3.047184,8.201355,-6.238452,8.087490,2.753133,-2.595120,3.495165,6.038568,0.108861,-9.366861,3.876121,9.887276,7.190820,3.748637,3.048585,-2.549305,2.065456,6.030689,6.388618,5.886090,7.128858,-4.632862,-5.072229,9.583123,8.412676,0.657921,-6.046355,1.590583,6.294328,4.969412,0.826645,-1.045738,-5.774388,-5.976665,5.928262,-8.846948,-9.870769,4.623471,-7.937272,-5.373302,-6.479791,-0.811062,4.449049,-5.091911,-5.093506,5.420807,8.247061,-7.858495,-2.347812,7.940344,-9.321717,-8.800094,-7.027251,0.175810,8.652648,6.085558,7.285681,-2.194925,9.465839,0.896212,6.413642,8.564259,8.127778,-8.419889,4.918741,4.261652,4.766873,-0.131104,2.042429,-6.230987,7.348261,-6.049926,0.036088,8.593396,3.186055,-2.329166,-1.247815,6.170823,-2.117179,3.636614,-3.781567,3.808990,-5.247787,7.397858,-6.909105,-9.478189,1.286654,-5.207938,-4.917440,4.920662,3.544724,-4.537827,-3.390924,0.406656,5.356785,-4.550047,8.062407,8.834413,1.513023,8.428241,-1.732422,1.327624,-1.358367,-1.736333,-0.290002,-7.262659,1.362292,9.660567,-0.079229,-7.912364,1.091384,2.372550,8.105648,-1.670589,-6.166962,-8.827599,-2.712040,-9.380959,9.155138,5.616837,6.047217,1.229264,-5.407392,-2.566463,6.008897,-4.826977,9.971414,1.885566,-5.111285,9.967780,0.982501,4.100133,9.107091,-0.855463,-9.312534,-6.284431,7.567236,-0.113868,-7.692983,7.509435,-1.005228,-9.099633,0.148814,-5.374937,-2.746997,-9.087917,1.672381,2.619292,-5.792574,5.817090,8.646191,-2.332927,-9.975815,-9.270963,8.677659,-7.321811,4.790059,5.179963,5.082835,-1.012842,4.085101,5.431702,-2.030942,1.000510,5.088030,8.146881,2.620182,2.027002,-2.149101,-8.331040,6.701988,6.153699,-2.710922,-2.989146,-9.296985,4.130972,8.090572,-6.099856,9.761334,-7.694827,6.096004,5.901583,7.102822,-7.693440,-4.588631,4.838799,0.733623,-3.293856,0.172502,1.755378,8.084804,8.878243,-4.189636,-1.809495,-1.646324,-2.381570,-8.830290,-5.135914,-3.735982,0.138756,6.834867,3.863658,-8.057083,-2.084137,-1.353630,9.490201,-5.297898,-9.136327,4.414556,-0.050546,-5.306452,4.084961,-1.111380,-2.030781,-2.441003,7.717049,0.527501,-3.743210,-7.559292,7.363588,9.116018,-3.908752,-9.494265,-6.375647,9.693078,9.317678,0.552751,-5.508719,-9.739073,-7.414155,3.586726,-1.473906,-6.622964,-9.098239,-2.739751,5.995946,-6.908228,8.043599,9.737879,-4.501408,2.091336,-7.945166,-2.268523,-6.828296,5.267416,4.571226,4.219051,3.449576,2.293457,-1.294485,-7.647822,0.106028,-1.690091,9.623214,-6.537451,-8.942485,6.405422,-7.283142,-5.924915,-8.111232,4.816495,-4.585211,2.733030,4.060733,6.582482,-5.106576,1.740589,-9.909440,0.372026,6.013321,-1.188918,1.644678,-7.725817,4.961728,-6.314512,9.854227,-6.725651,-1.301714,6.234029,-1.582882,-2.268090,-3.758176,-4.308096,6.163185,-4.763877,0.078126,-2.630866,-2.192240,-7.801204,4.606368,1.876427,-4.565629,-4.147263,-7.525839,-9.386122,-4.906643,5.745916,6.697359,-9.927742,8.736267,9.450676,5.135841,8.937293,7.873694,5.109060,8.264782,2.672019,-8.551316,-2.788012,8.501191,9.378427,8.599627,7.350239,-9.873499,7.200750,-6.741003,-0.891589,2.877185,-3.977247,8.011564,3.426351,-6.789350,6.808611,8.765439,1.077751,-5.313711,-6.026736,-2.207470,-1.499159,7.679857,-3.664594,7.021240,1.082270,5.651513,9.985536,-1.148891,6.946979,8.405437,9.658335,-9.611725,8.507561,-0.672508,5.965967,8.665016,0.011720,4.021262,8.462420], dtype = "float32")#candidate|4813|(1089,)|const|float32
call_4811 = relay.TupleGetItem(func_2458_call(relay.reshape(call_4779.astype('float32'), [6, 16, 11]), relay.reshape(const_4812.astype('float32'), [135,]), relay.reshape(const_4813.astype('float32'), [1089,]), ), 1)
call_4814 = relay.TupleGetItem(func_2463_call(relay.reshape(call_4779.astype('float32'), [6, 16, 11]), relay.reshape(const_4812.astype('float32'), [135,]), relay.reshape(const_4813.astype('float32'), [1089,]), ), 1)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_4816 = relay.TupleGetItem(func_1678_call(), 2)
call_4817 = relay.TupleGetItem(func_1679_call(), 2)
output = relay.Tuple([call_4779,call_4811,const_4812,const_4813,call_4816,])
output2 = relay.Tuple([call_4780,call_4814,const_4812,const_4813,call_4817,])
func_4833 = relay.Function([], output)
mod['func_4833'] = func_4833
mod = relay.transform.InferType()(mod)
output = func_4833()
func_4834 = relay.Function([], output)
mutated_mod['func_4834'] = func_4834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mod.get_global_var('func_4574')
func_4576_call = mutated_mod.get_global_var('func_4576')
call_4851 = relay.TupleGetItem(func_4574_call(), 0)
call_4852 = relay.TupleGetItem(func_4576_call(), 0)
func_4136_call = mod.get_global_var('func_4136')
func_4137_call = mutated_mod.get_global_var('func_4137')
call_4855 = relay.TupleGetItem(func_4136_call(), 0)
call_4856 = relay.TupleGetItem(func_4137_call(), 0)
output = relay.Tuple([call_4851,call_4855,])
output2 = relay.Tuple([call_4852,call_4856,])
func_4859 = relay.Function([], output)
mod['func_4859'] = func_4859
mod = relay.transform.InferType()(mod)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4859_call = mutated_mod.get_global_var('func_4859')
call_4860 = func_4859_call()
output = call_4860
func_4861 = relay.Function([], output)
mutated_mod['func_4861'] = func_4861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4299_call = mod.get_global_var('func_4299')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_4862 = relay.TupleGetItem(func_4299_call(), 2)
call_4863 = relay.TupleGetItem(func_4300_call(), 2)
var_4876 = relay.var("var_4876", dtype = "bool", shape = (264,))#candidate|4876|(264,)|var|bool
bop_4877 = relay.equal(call_4862.astype('bool'), relay.reshape(var_4876.astype('bool'), relay.shape_of(call_4862))) # shape=(264,)
bop_4880 = relay.equal(call_4863.astype('bool'), relay.reshape(var_4876.astype('bool'), relay.shape_of(call_4863))) # shape=(264,)
func_2951_call = mod.get_global_var('func_2951')
func_2954_call = mutated_mod.get_global_var('func_2954')
var_4889 = relay.var("var_4889", dtype = "float32", shape = ())#candidate|4889|()|var|float32
var_4890 = relay.var("var_4890", dtype = "float32", shape = (11, 99))#candidate|4890|(11, 99)|var|float32
call_4888 = relay.TupleGetItem(func_2951_call(relay.reshape(var_4889.astype('float32'), []), relay.reshape(var_4890.astype('float32'), [1089,]), ), 1)
call_4891 = relay.TupleGetItem(func_2954_call(relay.reshape(var_4889.astype('float32'), []), relay.reshape(var_4890.astype('float32'), [1089,]), ), 1)
func_1813_call = mod.get_global_var('func_1813')
func_1816_call = mutated_mod.get_global_var('func_1816')
var_4896 = relay.var("var_4896", dtype = "float64", shape = (35,))#candidate|4896|(35,)|var|float64
call_4895 = relay.TupleGetItem(func_1813_call(relay.reshape(var_4896.astype('float64'), [7, 5])), 2)
call_4897 = relay.TupleGetItem(func_1816_call(relay.reshape(var_4896.astype('float64'), [7, 5])), 2)
output = relay.Tuple([bop_4877,call_4888,var_4889,var_4890,call_4895,var_4896,])
output2 = relay.Tuple([bop_4880,call_4891,var_4889,var_4890,call_4897,var_4896,])
func_4901 = relay.Function([var_4876,var_4889,var_4890,var_4896,], output)
mod['func_4901'] = func_4901
mod = relay.transform.InferType()(mod)
mutated_mod['func_4901'] = func_4901
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4901_call = mutated_mod.get_global_var('func_4901')
var_4903 = relay.var("var_4903", dtype = "bool", shape = (264,))#candidate|4903|(264,)|var|bool
var_4904 = relay.var("var_4904", dtype = "float32", shape = ())#candidate|4904|()|var|float32
var_4905 = relay.var("var_4905", dtype = "float32", shape = (11, 99))#candidate|4905|(11, 99)|var|float32
var_4906 = relay.var("var_4906", dtype = "float64", shape = (35,))#candidate|4906|(35,)|var|float64
call_4902 = func_4901_call(var_4903,var_4904,var_4905,var_4906,)
output = call_4902
func_4907 = relay.Function([var_4903,var_4904,var_4905,var_4906,], output)
mutated_mod['func_4907'] = func_4907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4833_call = mod.get_global_var('func_4833')
func_4834_call = mutated_mod.get_global_var('func_4834')
call_4927 = relay.TupleGetItem(func_4833_call(), 0)
call_4928 = relay.TupleGetItem(func_4834_call(), 0)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
var_4930 = relay.var("var_4930", dtype = "uint32", shape = (420,))#candidate|4930|(420,)|var|uint32
call_4929 = relay.TupleGetItem(func_904_call(relay.reshape(var_4930.astype('uint32'), [14, 5, 6])), 0)
call_4931 = relay.TupleGetItem(func_906_call(relay.reshape(var_4930.astype('uint32'), [14, 5, 6])), 0)
func_4833_call = mod.get_global_var('func_4833')
func_4834_call = mutated_mod.get_global_var('func_4834')
call_4947 = relay.TupleGetItem(func_4833_call(), 0)
call_4948 = relay.TupleGetItem(func_4834_call(), 0)
output = relay.Tuple([call_4927,call_4929,var_4930,call_4947,])
output2 = relay.Tuple([call_4928,call_4931,var_4930,call_4948,])
func_4952 = relay.Function([var_4930,], output)
mod['func_4952'] = func_4952
mod = relay.transform.InferType()(mod)
var_4953 = relay.var("var_4953", dtype = "uint32", shape = (420,))#candidate|4953|(420,)|var|uint32
output = func_4952(var_4953)
func_4954 = relay.Function([var_4953], output)
mutated_mod['func_4954'] = func_4954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3439_call = mod.get_global_var('func_3439')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_5000 = relay.TupleGetItem(func_3439_call(), 0)
call_5001 = relay.TupleGetItem(func_3440_call(), 0)
func_3349_call = mod.get_global_var('func_3349')
func_3351_call = mutated_mod.get_global_var('func_3351')
const_5008 = relay.const([False,False,False,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,True,False,True,True,False,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,True,False,True], dtype = "bool")#candidate|5008|(264,)|const|bool
call_5007 = relay.TupleGetItem(func_3349_call(relay.reshape(const_5008.astype('bool'), [1, 264])), 1)
call_5009 = relay.TupleGetItem(func_3351_call(relay.reshape(const_5008.astype('bool'), [1, 264])), 1)
output = relay.Tuple([call_5000,call_5007,const_5008,])
output2 = relay.Tuple([call_5001,call_5009,const_5008,])
func_5010 = relay.Function([], output)
mod['func_5010'] = func_5010
mod = relay.transform.InferType()(mod)
output = func_5010()
func_5011 = relay.Function([], output)
mutated_mod['func_5011'] = func_5011
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5015 = relay.var("var_5015", dtype = "uint16", shape = (13, 10, 16))#candidate|5015|(13, 10, 16)|var|uint16
const_5016 = relay.const([[[-8,7,-9,-10,-9,-9,-8,-2,-7,-10,-4,7,-5,-4,-1,-4],[-1,10,5,4,-2,-1,-6,-5,-3,-9,3,3,-6,-4,1,7],[-8,-3,6,9,10,10,-4,8,-7,4,-4,7,-5,8,-10,9],[-3,-5,10,9,-5,-8,2,-8,-5,-1,1,-9,-3,-2,4,-5],[4,8,-5,7,-5,-10,-3,8,-3,6,-8,-10,-2,4,-4,2],[8,-5,4,4,7,6,4,-5,-4,-1,-4,3,-3,-1,-7,-6],[-1,-9,-3,6,-7,-7,8,-8,-2,5,9,-3,7,9,7,1],[6,-4,-3,6,-5,-2,4,-7,10,2,10,-2,-9,10,-6,-3],[1,1,10,-7,-10,-9,-1,-9,-8,10,6,6,-5,-1,-9,3],[-4,7,2,10,-3,6,-7,6,-6,5,10,-1,-2,-4,-9,-3]],[[3,-10,4,-7,-10,2,8,3,4,-9,-1,-9,-3,6,-2,-8],[10,2,-5,-2,1,-2,-2,4,7,2,4,-3,-6,10,7,-5],[-3,3,-5,6,-1,-7,-5,10,-4,2,-4,6,3,8,-3,8],[-9,7,8,-1,2,-9,-9,-1,-1,-3,-5,5,-5,9,-7,8],[-10,1,8,4,-10,-7,3,-1,10,-9,3,4,-8,-7,-9,-2],[-10,6,5,-8,-2,3,2,10,-10,-6,5,-10,-2,-10,4,2],[5,3,-6,6,-7,-5,-4,2,8,-4,9,-7,-3,-4,9,2],[-1,-3,-8,-9,7,-4,3,-5,-4,-5,5,4,9,6,3,9],[4,3,10,-5,-9,1,4,2,-7,1,-7,3,-2,-3,8,8],[-3,-4,-4,3,9,-5,10,-3,2,-2,-10,6,-1,-6,10,-10]],[[7,-7,2,-6,4,4,-7,-4,10,2,8,-1,-7,-9,-10,-10],[-5,-10,9,-10,5,8,2,5,-7,-3,6,-3,10,2,2,-1],[-10,-6,4,9,-9,-5,10,-2,-6,-9,8,7,-5,1,10,-6],[2,-9,-5,8,-7,4,3,-2,2,3,-7,-9,-9,2,4,-2],[-10,-3,-9,-9,-3,4,3,-7,9,-5,2,9,-6,-3,-8,7],[5,-3,2,-1,-8,-1,2,4,-9,8,-4,-3,9,-3,2,-7],[3,-1,3,-9,8,-2,9,-4,6,10,-10,-2,-2,7,8,-10],[3,5,-7,9,-6,8,8,8,3,-5,2,3,4,-7,-4,-5],[-10,5,5,-3,-4,10,2,-7,5,-9,9,2,-3,-8,-6,6],[-3,3,6,1,-8,1,9,6,-9,-3,-8,2,2,2,4,5]],[[-10,7,6,-5,1,4,-3,-3,7,1,-1,-1,-6,2,-1,-7],[-3,7,2,-4,8,-2,10,5,3,5,10,8,6,-6,-5,8],[-7,9,-8,4,-3,-9,6,-10,-10,5,-8,-8,1,3,-6,5],[-9,7,-7,1,9,-3,-4,6,-8,3,-3,4,4,-1,-10,6],[-1,5,3,-10,-6,9,-7,-3,3,-3,-7,-10,4,-1,-10,-2],[-9,-2,4,7,6,9,1,6,-8,-10,-6,5,-4,4,3,-8],[4,-9,2,8,3,9,9,-6,6,1,-8,2,3,7,-2,2],[-3,-4,-6,2,10,-3,-7,-8,-5,-5,-7,7,2,10,9,10],[3,-8,6,8,1,7,-10,-3,7,-10,-6,6,10,-2,8,-2],[5,9,10,-7,1,-9,10,8,9,-2,4,2,6,5,-7,-4]],[[-7,-4,-4,-5,5,-6,7,4,1,-10,-6,2,-8,7,-6,-8],[5,9,2,-4,10,-4,3,3,-4,10,-9,1,9,-3,-8,-7],[2,4,-2,3,-6,10,-6,3,10,-9,6,-6,-9,-2,-1,-2],[7,-9,4,-2,10,2,-7,-8,-10,5,9,5,-2,7,-7,10],[-6,-4,4,5,-10,-2,3,5,6,-3,1,3,4,1,-10,9],[2,8,-1,-10,9,-9,9,-10,-4,-10,-1,-10,-2,8,2,9],[1,9,-10,5,10,-4,8,4,6,-8,-6,4,9,-1,1,6],[5,6,-4,-5,-4,3,-4,5,10,7,-10,-3,4,2,2,-7],[-5,4,-3,6,-9,-9,-8,3,8,4,-10,8,1,-7,-10,-3],[7,-4,6,8,-3,-8,-3,-8,10,6,-3,4,-6,8,-7,-9]],[[-8,-7,-7,10,1,-8,9,-3,2,-9,-6,8,5,-8,-8,-9],[1,1,-10,-5,-8,-5,-3,-8,-2,9,-1,1,-4,8,-5,-8],[-4,4,9,5,4,-6,10,3,10,-1,-8,7,-9,-6,4,1],[-3,2,-6,-3,6,-9,-3,8,4,-6,-10,-6,10,5,6,-3],[-3,-2,9,1,-7,2,3,-5,9,-1,6,10,-9,-1,-3,3],[9,-4,3,6,8,-1,-9,-9,-10,9,-8,-4,-8,-2,-9,-6],[2,-7,-7,-6,2,-7,-6,1,-9,-5,-3,-3,-4,-9,-10,3],[7,9,-4,1,4,7,6,-7,-10,1,-1,-4,7,-10,-10,-1],[3,-3,4,-3,1,10,9,2,10,-3,-8,-6,2,-4,-6,-1],[4,6,-7,-8,-8,-8,6,6,-5,-6,10,8,5,6,6,2]],[[1,-7,4,1,-2,1,-10,3,-10,8,1,1,7,-9,3,4],[9,6,-7,-7,7,8,-7,-3,-9,4,-7,6,-10,-9,-6,1],[-4,-1,6,-1,-6,-10,-7,-9,-6,-6,7,8,-9,-4,-2,10],[-2,9,9,-10,-7,7,5,-2,-8,-3,2,-2,-8,6,1,-8],[-7,2,-6,-10,-3,9,-4,9,9,6,-3,2,5,3,-2,-1],[-9,6,5,8,-4,6,-8,-7,-6,10,-1,1,8,4,-7,10],[9,-1,1,-2,8,2,-4,-5,-2,-10,-7,3,-4,-7,3,9],[3,-6,-1,1,8,-7,2,3,-9,9,3,-1,-10,-10,-6,-6],[-10,5,-1,-3,10,1,6,-6,-6,-10,8,8,2,2,6,8],[10,-9,2,2,-2,1,-7,-2,3,-4,5,-10,9,-4,-2,2]],[[8,3,-1,-1,9,2,1,1,-6,-7,-4,-10,1,-7,-8,2],[-10,5,1,-6,-10,-6,-2,8,-1,-1,-2,-5,4,-5,-3,-8],[6,-4,-1,-7,7,-5,2,7,8,6,10,4,-7,8,-8,1],[-2,-10,3,8,-3,-1,6,-8,-7,-6,-10,-2,-1,-7,9,-2],[-2,7,-2,-9,10,1,9,2,-8,4,-1,4,-7,1,-8,-6],[-5,-8,-8,1,-7,3,4,2,6,-9,-2,-8,-4,6,2,-4],[7,-4,-1,4,-9,-3,-4,4,-3,-6,-4,8,3,-9,6,-2],[7,9,-2,3,-9,4,-5,3,1,-5,-6,-4,6,4,9,6],[-5,-2,-5,-10,-3,-10,-5,8,-4,3,-5,1,-2,-3,4,-7],[-4,5,3,-6,10,-7,-10,-2,-8,-8,-2,4,3,-5,9,-3]],[[-10,-2,6,1,5,2,5,-4,7,-7,9,4,-1,9,10,2],[-2,3,6,3,-6,-9,-9,3,6,-6,1,9,9,-3,1,7],[4,1,-5,-1,9,1,4,-5,-6,-5,3,1,1,-10,-1,-6],[-8,5,1,-8,8,10,5,-2,10,-10,-3,-4,-4,7,-3,10],[-1,-9,-1,-5,-6,10,-2,-4,10,-5,4,-9,8,-4,10,4],[-1,4,-10,10,3,9,2,10,-7,7,6,10,2,5,-9,3],[-4,1,-5,-1,-3,-6,6,-9,8,-6,1,-8,-1,-7,4,8],[9,1,2,-2,6,10,-1,7,-4,-6,1,10,-1,-2,-8,-2],[-2,9,-8,-7,-9,6,-5,-1,-8,-5,-3,2,-1,8,7,-4],[-4,2,-6,-6,-7,4,5,-10,10,-1,2,8,8,-3,-7,-5]],[[-2,5,-8,-2,3,-7,-9,1,-4,-6,-8,8,-10,4,-1,-10],[-5,-10,6,-6,-10,-9,-9,10,-5,-8,1,-2,10,-2,-2,-4],[7,-10,8,4,-8,-6,-3,10,5,4,5,-10,-1,-6,3,2],[3,-5,-7,-8,-1,-1,3,6,-9,-5,-6,1,-7,4,4,2],[-7,8,-5,10,3,4,-5,5,1,-10,6,8,-8,-3,-8,10],[3,1,6,-6,5,4,-2,-5,10,-2,9,-10,-2,-9,-10,-8],[-9,-3,-2,-4,10,-8,9,-5,-1,7,-7,-6,2,1,-6,-6],[-8,2,7,9,-5,10,-10,-5,4,-10,-9,-1,-4,2,1,-7],[-7,1,4,-5,-6,-3,2,9,9,6,-8,8,9,-3,10,-1],[8,4,1,1,4,4,-3,1,-4,2,4,-7,-2,5,-10,-10]],[[8,8,-3,5,-2,-5,-3,9,-1,-1,-2,10,-9,-5,-9,5],[1,5,2,-3,-10,-3,3,2,2,-1,-4,-8,3,-1,-2,-2],[-10,9,8,10,10,-2,-3,9,10,2,10,-6,-7,7,-1,-2],[-7,-7,-3,-4,-8,6,-1,-1,-4,4,4,6,6,1,-4,10],[-6,-6,-4,1,-9,5,9,-2,8,-6,-7,-6,-8,2,-1,-3],[9,-5,-4,-5,3,-2,4,7,3,4,6,2,-8,7,-7,8],[2,9,2,-8,3,-7,-5,9,-8,7,-7,-9,3,4,-6,6],[-8,3,-8,-4,2,-10,-6,4,-3,7,10,-5,-9,3,-3,-5],[-3,-2,-1,3,-8,10,-1,-5,5,-6,-7,8,-4,-3,-7,10],[1,4,-10,7,10,-1,4,-9,9,4,8,4,-10,-1,-7,10]],[[4,-10,-10,2,6,1,1,-9,-7,6,4,9,7,4,10,-2],[5,-9,-10,-5,4,6,-7,-6,7,-2,-4,-4,9,-6,9,3],[9,1,1,-8,5,10,7,8,2,5,-9,6,7,8,10,-2],[-3,10,2,-3,-2,-8,-1,-4,-4,-8,8,-2,-7,-10,4,-6],[8,5,6,6,-10,-6,1,-3,-9,-10,6,9,-4,10,5,-7],[4,3,-9,-7,-3,2,-4,-9,-6,9,2,-7,1,8,-3,-6],[-8,-8,-8,-8,1,5,4,10,4,4,-9,6,-6,3,1,8],[-8,6,5,-9,3,2,7,-7,-1,-10,-2,8,1,1,1,-1],[8,-7,3,-9,-9,6,-3,10,4,2,-6,-7,-2,-9,8,3],[9,-10,5,3,-10,-1,-1,-9,-1,-2,3,-4,-8,7,-4,1]],[[-10,10,-10,-1,-1,5,5,7,-5,3,-8,3,9,-1,10,-10],[5,-10,-2,-7,-5,-3,6,-6,-8,-9,5,4,1,9,-9,4],[9,-9,4,6,-6,-10,10,3,5,8,-3,-4,-8,-6,3,9],[5,-5,-3,8,1,-2,-6,-10,-7,2,9,-4,10,3,1,7],[9,-5,-2,-2,3,-5,10,-1,-2,-9,-1,-9,3,6,4,-10],[-5,7,-7,2,4,-8,-3,-3,4,-9,5,9,1,-5,-1,10],[-1,-5,8,8,-7,6,9,-8,-3,9,-6,-7,-8,-2,7,-4],[10,7,-9,10,5,-9,-7,-7,-3,-8,7,-5,-8,-3,-10,-5],[6,-8,9,4,-6,-6,7,3,2,-10,9,-3,4,-3,-2,-5],[-2,-7,3,-7,-2,3,-8,3,10,-8,-1,-7,6,-9,10,-1]]], dtype = "uint16")#candidate|5016|(13, 10, 16)|const|uint16
bop_5017 = relay.less_equal(var_5015.astype('bool'), relay.reshape(const_5016.astype('bool'), relay.shape_of(var_5015))) # shape=(13, 10, 16)
bop_5020 = relay.minimum(const_5016.astype('uint32'), relay.reshape(bop_5017.astype('uint32'), relay.shape_of(const_5016))) # shape=(13, 10, 16)
uop_5023 = relay.acos(const_5016.astype('float32')) # shape=(13, 10, 16)
bop_5026 = relay.left_shift(uop_5023.astype('int16'), relay.reshape(bop_5020.astype('int16'), relay.shape_of(uop_5023))) # shape=(13, 10, 16)
uop_5050 = relay.sigmoid(uop_5023.astype('float64')) # shape=(13, 10, 16)
bop_5055 = relay.logical_xor(uop_5050.astype('int32'), relay.reshape(bop_5026.astype('int32'), relay.shape_of(uop_5050))) # shape=(13, 10, 16)
func_2871_call = mod.get_global_var('func_2871')
func_2873_call = mutated_mod.get_global_var('func_2873')
call_5058 = func_2871_call()
call_5059 = func_2871_call()
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_5062 = relay.TupleGetItem(func_2978_call(), 0)
call_5063 = relay.TupleGetItem(func_2980_call(), 0)
bop_5065 = relay.greater_equal(bop_5055.astype('bool'), relay.reshape(uop_5023.astype('bool'), relay.shape_of(bop_5055))) # shape=(13, 10, 16)
uop_5068 = relay.log2(bop_5020.astype('float64')) # shape=(13, 10, 16)
output = relay.Tuple([call_5058,call_5062,bop_5065,uop_5068,])
output2 = relay.Tuple([call_5059,call_5063,bop_5065,uop_5068,])
func_5070 = relay.Function([var_5015,], output)
mod['func_5070'] = func_5070
mod = relay.transform.InferType()(mod)
var_5071 = relay.var("var_5071", dtype = "uint16", shape = (13, 10, 16))#candidate|5071|(13, 10, 16)|var|uint16
output = func_5070(var_5071)
func_5072 = relay.Function([var_5071], output)
mutated_mod['func_5072'] = func_5072
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5010_call = mod.get_global_var('func_5010')
func_5011_call = mutated_mod.get_global_var('func_5011')
call_5127 = relay.TupleGetItem(func_5010_call(), 2)
call_5128 = relay.TupleGetItem(func_5011_call(), 2)
output = call_5127
output2 = call_5128
func_5133 = relay.Function([], output)
mod['func_5133'] = func_5133
mod = relay.transform.InferType()(mod)
mutated_mod['func_5133'] = func_5133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5133_call = mutated_mod.get_global_var('func_5133')
call_5134 = func_5133_call()
output = call_5134
func_5135 = relay.Function([], output)
mutated_mod['func_5135'] = func_5135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4136_call = mod.get_global_var('func_4136')
func_4137_call = mutated_mod.get_global_var('func_4137')
call_5136 = relay.TupleGetItem(func_4136_call(), 0)
call_5137 = relay.TupleGetItem(func_4137_call(), 0)
func_2701_call = mod.get_global_var('func_2701')
func_2702_call = mutated_mod.get_global_var('func_2702')
call_5149 = func_2701_call()
call_5150 = func_2701_call()
output = relay.Tuple([call_5136,call_5149,])
output2 = relay.Tuple([call_5137,call_5150,])
func_5152 = relay.Function([], output)
mod['func_5152'] = func_5152
mod = relay.transform.InferType()(mod)
output = func_5152()
func_5153 = relay.Function([], output)
mutated_mod['func_5153'] = func_5153
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5179 = relay.var("var_5179", dtype = "float64", shape = (2, 1, 1))#candidate|5179|(2, 1, 1)|var|float64
const_5180 = relay.const([[[3.158346,6.843925,-2.107638,-3.132844,-9.087326,8.488612,-8.614633,3.816404,-6.455828,2.110409,6.037903,-2.307622],[3.369679,-0.309586,3.984193,6.533543,-7.480597,9.731424,-5.158730,6.849883,-2.139747,-9.854692,9.021715,5.627305],[-5.911316,4.792275,9.898350,-5.778254,-3.005993,2.165066,-0.191143,2.907144,9.522532,0.363809,-3.071165,-8.665316],[6.628880,-0.887067,-5.036874,6.052881,-6.374404,-9.874970,-1.782039,-9.565810,3.909390,-2.605246,-2.555076,8.095225],[5.760026,-2.070675,9.736407,-5.141262,3.864101,-6.735582,2.489651,-7.206909,-4.830049,8.818955,0.687289,-4.257925],[3.135972,9.090830,-5.626821,4.101686,3.506811,0.083405,-1.390713,-6.652760,-6.507683,9.513628,-2.267325,-4.393662],[2.919360,4.311857,4.663051,5.439046,-8.304796,6.298353,1.471758,-7.110312,-9.069907,-4.937659,-7.176907,-1.763875],[6.815926,-1.850013,-1.825063,-5.624144,-2.374664,-5.705334,6.560169,0.564162,-6.861176,-5.958594,5.032451,9.763583]],[[1.054940,2.129245,-3.296260,-8.900681,8.760463,2.215223,5.006145,4.319199,5.774279,-3.260558,-1.382199,-3.215841],[-5.103944,-7.689352,-9.091034,6.904543,1.384565,4.082495,-8.273325,2.877032,-7.903567,3.202093,4.351517,7.671671],[1.891148,2.902887,4.587055,-9.453801,8.654652,-5.449286,-5.469347,4.843523,-0.926829,0.675172,-4.152676,-2.101424],[6.159009,3.578269,7.435055,1.000146,-3.667628,-9.711900,5.496101,8.192062,2.043323,-9.834881,3.539608,-6.102534],[-0.076642,-0.055612,-6.019667,2.769246,4.051892,-7.935873,7.972380,4.068384,9.217927,-8.328486,-2.118243,5.759168],[3.745134,-6.329015,9.794900,-4.993142,-9.231125,-2.381601,9.407396,6.507380,-1.402479,8.289491,1.896774,8.195974],[-8.736576,3.328729,8.917987,5.465387,-5.129884,4.525547,-9.424446,2.187071,3.349387,1.123184,5.863726,6.712364],[5.458410,-0.912721,7.446743,9.003189,5.665409,-2.670603,2.606426,2.701546,5.906350,2.128874,-5.986314,9.101058]]], dtype = "float64")#candidate|5180|(2, 8, 12)|const|float64
bop_5181 = relay.mod(var_5179.astype('float64'), const_5180.astype('float64')) # shape=(2, 8, 12)
output = relay.Tuple([bop_5181,])
output2 = relay.Tuple([bop_5181,])
func_5191 = relay.Function([var_5179,], output)
mod['func_5191'] = func_5191
mod = relay.transform.InferType()(mod)
var_5192 = relay.var("var_5192", dtype = "float64", shape = (2, 1, 1))#candidate|5192|(2, 1, 1)|var|float64
output = func_5191(var_5192)
func_5193 = relay.Function([var_5192], output)
mutated_mod['func_5193'] = func_5193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_5198 = relay.TupleGetItem(func_1643_call(), 0)
call_5199 = relay.TupleGetItem(func_1644_call(), 0)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_5201 = relay.TupleGetItem(func_1643_call(), 0)
call_5202 = relay.TupleGetItem(func_1644_call(), 0)
func_423_call = mod.get_global_var('func_423')
func_426_call = mutated_mod.get_global_var('func_426')
const_5206 = relay.const([9.914912,-0.047806,8.797582,0.496678,-7.426639,-0.850483,6.402268,9.517608,-0.088898,-7.394207,-6.013134,-5.710673,0.435074,2.925641,-6.587071,-5.409165,0.124005,8.272003,0.163232,7.629412,-4.837175,-7.570012,4.552718,-0.671556,4.238953,5.034363,-2.175657,5.687928,-6.917256,-3.732510,9.452539,-4.002326,-9.231928,8.455490,4.570765,6.932538,8.182498,0.487225,6.569512,-5.327809,-7.950896,6.781951,6.739834,8.632355,1.936413,-1.963806,-5.871974,4.160418,9.056339,-1.886854,5.600844,-3.837368,2.078281,-1.869887,9.009467,-5.918247,-0.259615,-0.015645,-4.073055,-3.658736,-9.614470,-9.185990,4.256665,9.097279,0.228134,0.589455,6.884654,6.400416,-2.711562,-4.595228,-3.450768,9.927910,-2.462497,-4.885431,4.155865,-9.062566,5.799458,-0.041047,8.006574,0.923716,-5.547835,0.606636,9.385313,-5.539312,-0.213254,9.008547,4.894079,-3.021545,1.425061,1.485438,0.228091,-6.257010,-9.567385,3.581512,-3.994369,-9.588825,-4.606455,-1.110049,-1.772919,9.497216,4.958775,2.715096,1.060423,-5.133189,-0.896977,-2.905340,-5.532147,5.998969,6.733377,-2.802601,2.080359,-9.711453,-3.900834,6.146283,-9.263695,-3.572507,-2.564786,-8.017573,1.314470,-1.534759,-2.817484,1.282646,2.926270,-0.453159,8.890117,-6.342807,2.218432,-1.918765,7.206008,4.777529,-2.640433,-5.028562,0.208362,7.572742,0.139671,8.099441,-3.517853,-9.271308,3.085203,-0.562213,0.943492,2.292742,-0.964610,9.426469,-3.652454,6.482705,-8.401707,9.062174,-3.525222,-6.335545,-6.136362,-0.639683,-8.811872,-0.824489,0.389093,-3.731278,5.942792,7.228594,-3.919779,7.524374,5.164167,8.967228,-2.951887,-5.680622,4.034577,7.300808,-1.493134,-4.004403,-1.929577,-3.941418,-0.326487,1.724569,-4.221694,8.379390,3.231662,2.376205,8.126101,-9.230100,9.027752,-8.660345,4.357483,-5.814669,6.396189,-0.565008,3.718052,9.920830,8.336282,8.442222,-4.735934,-1.904860,-1.208615,-0.770207,0.355843,6.418474,7.623536,7.203608,4.124591,-3.055528,6.541201,5.540478,7.082775,-9.021019,5.043472,4.507856,-5.936752,0.623336,3.825589,-6.016040,-1.906362,-8.900138,0.898458,-3.217172,9.035402,-3.039936,1.795121,-3.982367,-5.249890,4.624562,-8.927367,3.999083,0.187665,6.416435,7.158102,6.936810,-3.203464,3.124878,6.779350,-6.005367,8.223978,4.902801,-3.868955,4.895232,-8.120617,-0.402657,6.161651,0.965571,-2.233701,-2.312207,-9.079886,3.154770,2.978933,5.682574,-4.721497,2.789661,-6.646014,-6.705256,-6.230518,5.160540,1.586132,-2.952681,-4.157607,6.798751,-4.025663,-1.041760,0.972415,7.348633,-9.900274,0.986624,4.738549,-0.735055,-2.828498,-7.654108,3.666847,7.516154,-9.134554,4.989356,-7.449114,3.724264,-3.490221,6.794542,-9.541465,-2.064558,3.348066,9.362743,7.397293,-7.718470,9.664922,-3.878877,6.274477,5.645238,9.990966,-3.352883,3.366838,3.594283,5.789996,6.596462,0.430158,-9.281259,0.920262,1.309569,-5.004938,-5.169485,4.129181,-4.721572,3.589328,-1.338616,-0.582741,-8.588481,-6.441618,-7.531465,-5.506954,2.142651,4.394050,7.088823,-8.350507,0.851741,-4.235794,-1.776730,0.954404,-7.989443,-0.294125,9.145464,8.363078,-9.986505,2.695491,3.365808,-6.150844,-6.327884,9.781199,-4.779876,-5.538676,-6.478256,-9.066612,-6.903348,0.315889,-3.938593,4.220218,-2.808829,9.775200,7.269532,2.332312,-7.265222,0.828084,-5.011126,-1.136149,-4.575430,-4.371463,-4.373822,2.771243,-5.083363,8.878695,-8.932958,7.032968,-3.644624,9.968704,8.566950,-7.399275,-1.325928,-6.332980,-8.016773,-3.745217,-8.183080,0.887544,5.202516,9.797930,3.884167,-3.750434,-8.442842,1.370149,-7.906712,-6.814879,7.463681,0.069931,-8.775605,-1.582096,9.727530,-8.983179,-8.816069,-1.874778,-4.150161,4.362557,-4.398817,-2.960960,7.398749,5.403063,-0.551462,-7.841892,8.171304,-4.184632,4.230351,-8.952942,9.802993,-8.428814,1.715983,9.498300,2.012358,6.517745,-6.356626,-6.472230,2.020510,6.788807,0.494194,-1.552538,1.609122,-0.816954,8.728010,6.361827,6.228465,-4.572708,-3.103202,9.975802,2.379576,-5.913560,-5.314707,9.554311,-7.597400,2.085796,-0.443808,-7.441644,-3.982274,7.807843,-4.119601,-7.586857,-4.221685,-2.573713,-5.340536,-1.203782,-6.064563,1.872008,2.238239,3.616127,9.738556,0.552212,-1.694283,-7.117555,8.047459,-5.427084,-9.257278,8.430463,-1.893153,-7.820021,3.117110,-4.791373,4.063454,-7.542119,-8.769144,-8.776943,6.141050,-8.220431,-3.280561,-4.648284,-3.417480,3.008634,-8.704228,5.810952,-8.404417,4.796085,1.490428,0.808080,-2.116860,1.116079,3.943550,-2.122546,-8.542679,-1.255481,9.770922,-0.713077,-6.812080,9.426795,-0.730031,9.460581,-6.231752,2.712373,-0.904994,-0.206833,-2.440207,5.502007,1.823806,-1.810825,-1.704167,-9.038993,-3.198129,8.934746,-3.710802,3.725683,-7.581315,2.787723,0.283579,-2.370966,-6.469548,-5.768524,-3.523616,-9.056220,-5.591469,7.468102,-9.546608,-4.424466,-1.779253,6.406219,-8.188439,-2.852801,1.117678,4.150154,-5.295102,-3.380860,-9.060997,4.551502,-8.553210,6.409017,6.731339,-4.357198,-9.637882,-4.606245,-6.868201,-9.185464,-0.558694,9.106727,-8.667539,-5.862162,-1.107312,9.017199,-5.609699,-5.262601,5.778143,4.351068,-6.541659,-7.841906,-2.690414,-8.329488,-2.408369,-7.181835,5.765573,-4.220893,-7.794807,-7.986507,1.909506,-3.146436,-1.826103,-5.156427,-8.018842,-0.273303,5.500510,4.894100,1.987100,0.292496,-2.222656,-5.200032,0.090912,-1.524139,-5.825593,3.809477,-2.384876,7.391034,-6.817763,-3.297751,4.839953,4.794066,6.672830,-6.068503,-0.309168,-2.285054,6.575769,-0.879112,3.842901,6.468864,0.885775,9.114308,-0.431880,2.690487,9.799046,9.432277,-6.099956,8.960276,5.502573,1.990967,0.015496,7.566294,-2.965604,-7.101040,-2.081691,7.033273,-0.097187,4.008400,5.354961,4.270478,2.263252,8.621091,9.600710,4.117894,1.030380,9.274058,9.131258,3.642511,-3.329262,8.389668,3.035989,4.265290,-7.044826,-9.479637,3.168233,-4.738133,-5.607007,-8.140825,-2.568489,0.982502,-4.755937,6.305033,6.840180,-2.732687,-6.169158,-6.444969,-9.236328,6.524021,-5.355584,4.659312,4.645318,-8.399321,5.472613,6.695775,2.400793,8.869281,4.337360,6.997776,-4.760057,6.486667,9.544382,-4.232367,6.511735,-3.866025,-2.880235,2.366967,5.037331,1.945458,-3.546236,1.876789,0.615285,-4.402934,4.093647,6.412316,8.840214,-0.622457,-1.310313,-1.760713,-4.479366,-0.186513,-8.858408,-9.344462,4.467087,8.370322,-0.269685,0.406392,6.409327,7.106467,9.235172,-4.386495,0.380695,-0.952251,-6.215092,7.419794,9.585417,3.308089,3.936553,-9.413555,9.106119,-4.141673,-2.827055,-1.465230,3.106705,-7.355347,-0.924433,2.350102,2.349153,-6.937368,5.244412,-0.619135,2.418501,-2.373143,1.339976,5.797524,-0.909817,-7.400014,-0.920540,3.118077,-7.829921,-1.573289,-7.495891,-5.187325,2.924270,2.353410,-7.049435,-0.216237,6.152952,-5.684843,6.588804,-3.325463,-4.013473,-9.123836,3.641149,-8.198041,8.999478,-7.302039,8.766190,0.549961,7.416916,1.445962,-2.404394,8.357633,-8.993397,-9.863590,-0.425399,-9.714372,8.234654,5.175584,-8.920645,4.045497,-7.214413,7.106732,-5.249122,5.642222,-5.016974,-0.201757,-3.554730,-0.906483,4.089028,-4.033970,4.905245,-5.843549,5.965513,8.238532,-6.449671,3.446242,2.560065,-7.884150,3.957228,1.654959,-4.150622,-8.128472,-1.276952,9.531609,8.926791,8.900466,-6.744716,1.479600,4.794381,8.569611,7.872737,-2.640889,-0.756433,3.010819,-3.074236,0.266733,-7.046776,0.890343,-1.681660,-5.449802,-2.320764,3.742566,-0.954784,-7.462700,1.246302,2.572068,-1.049174,6.910647,-6.912522,-7.393754,-8.158134,0.990597,6.598625,4.349054,6.172652,4.912710,0.198466,7.476540,-6.423764,2.140633,1.367639,-8.944287,-8.943078,-7.537459,-6.090623,-8.182343,-0.223918,7.120667,-1.411306,-8.529263,5.045115,-2.253299,-1.790487,-6.573557,2.541232,-4.623653,-2.884829,1.904983,0.807449,3.735009,-7.232643,-7.444757,6.064308,0.621508,-5.070168,5.154393,2.492589,-3.508959,8.607836,-2.356581,-3.190124,-8.454318,-9.411183,7.839208,1.326339,3.518728,-1.405390,4.019170,-6.448821,-9.533337,-0.107774,-2.116446,4.470386,3.967889,4.793220,3.968497,-4.098068,-5.038414,0.334003,-0.691304,-7.261227,4.431604,3.386352,-1.293592,9.506962,-0.917702,-8.125653,8.436200,6.011062,5.516463,9.933904,-3.078017,-6.840056,-9.719072,4.530940,-6.036177,-4.715713,-7.371194,-1.246448,1.194532,9.594096,8.116584,-9.269667,8.744651,9.510702,-8.224773,-9.634696,8.501303,8.333415,-6.820623,-4.254840,-9.541714,-7.698867,3.992023,0.107425,-9.375894,-1.497048,9.218050,5.592813,1.975204,5.838673,2.272938,-5.066304,-9.281536,-0.080376,-3.865920,4.288013,8.836422,-9.230835,1.978645,-2.040134,-8.865996,6.910542,8.903664,3.015661,-0.560693,4.172867,-7.686684,-4.815039,8.541042,2.531662,1.328772,2.601767,5.051094,6.012738,3.664910,-5.400552,5.442858,9.429560,-1.542312,2.246009,5.296007,-0.719371,-0.255222,-3.808242,4.297942,-0.131550,6.411743,-4.126409,3.586772,9.144772,0.595269,-5.110730,0.796610,2.072634,-3.858957,-5.173140,5.924442,1.669692,6.417776,-1.205479,-6.073591,-9.146789,-4.058535,-2.895834,-4.932273,-8.764296,8.046628,-1.421932,9.184402,4.947178,-0.018039,8.216251,-9.552511,-9.432328,4.727024,1.427196,7.275358,2.827413,-7.139993,3.243407,8.746394,-7.432749,-4.248484,6.376042,-6.324851,-4.301090,8.892603,5.896544,-3.418132,6.045329,-2.545245,9.131266,-2.957386,0.233421,-2.650205,-0.989495,-9.820096,6.470121,8.234117,-2.382014,2.904647,5.604241,5.891611,-4.760001,-1.381938,3.835208,-2.247100,-6.237983,7.946999,1.389033,-1.227915,5.463974,-6.125018,6.741302,7.500641,-5.403927,-4.377675,2.449327,-9.012033,-9.349650,-9.060289,2.827854,-8.717407,7.449408,2.104257,-2.339382,-6.266388,-6.643514,-0.888987,0.290232,-4.889092,-8.001275,2.765508,-3.596774,5.096992,-5.138538,-6.717711,3.798258,7.119544,-4.528763,2.241098,-2.230199,-0.991498,8.642081,-4.438591,-6.278097,-8.211219,-1.345236,2.040866,4.172465,3.401356,-8.962879,5.171685,-3.313388,-9.454047,7.284927,1.846112,-8.482779,-8.009901,-8.690311,-8.003442,7.736893,0.030433,-4.438683,-2.984640,-0.289126,6.903193,8.777112,-4.558645,9.645390,-8.393272,-9.759385,-5.614374,5.317660,-0.456575,0.931715,9.219679,6.276851,-1.853160,9.230876,2.244459,-7.494315,-7.979333,2.145426,-3.443778,2.871134,1.119241,-2.082386,-4.535965,1.744544,-4.965078,3.793654,3.289812,-8.697992,-2.753346,7.141906,7.404741,-9.557593,5.282522,-2.653698,-4.552431,6.483733,-0.796149,5.519296,0.383234,2.357307,-2.625890,0.420168,-4.507487,1.473599,6.186873,-4.046565,3.349261,-6.038085,6.738627,-7.264446,8.463204,2.355387,5.615855,-3.187472,3.117759,-7.176832,6.512509,-3.508499,-2.199574,-2.784688,-5.151218,-8.816409,-7.169241,-3.297403,-9.367412,8.257755,-3.852736,5.740268,-9.249537,1.196335,7.540547,3.995419,9.265441,-0.601797,4.264359,-4.339336,-4.703186,6.772380,2.867916,-2.020506,-6.564881,7.859810,-3.020479,6.682276,7.152163,9.407870,-2.904309,8.302374,-8.422325,0.208465,-8.346108,7.745411,0.008278,5.429420,-0.507025,-1.167555,-6.956605,-9.458703,-2.569767,9.768344,-9.106889,-9.165083,6.468347,-6.937311,-8.907103,4.390688,5.882996,5.720897,-8.645758,-1.066256,-0.302739,1.359228,-1.354931,7.119195,0.078140,-8.686142,3.895212,8.670581,-7.449869,-2.517226,2.294849,-2.412906,-3.087337,8.942522,-3.071751,-9.925087,-8.974956,3.121065,6.323781,3.181800,3.538297,-6.473754,3.470365,5.657568,2.799851,-5.120497,-1.539182,-6.833928,-8.021325,6.473109,7.739910,9.566414,9.039217,-1.658476,9.709981,-0.363332,-9.191925,-4.243148,-9.876856,0.669794,1.630492,-7.489595,-8.292040,9.882584,4.240164,-8.834195,-3.129489,-0.422507,-0.915668,-5.896363,9.836140,3.164691,9.210733,9.179897,6.596180,4.019229,-9.716157,-4.386524,-6.228619,4.959060,-9.891599,-5.321984,0.916396,1.792691,-7.096975,7.066414,-0.436047,2.576442,-5.217081,3.187554,6.248193,5.242067,-0.043659,6.765650,6.860796,-0.060610,-5.083305,-2.752224,-7.347624,2.109904,2.663445,-0.974338,0.310131,7.319109,-6.926280,-3.266500,2.061307,8.862936,7.375815,4.852514,5.588885,1.676644,-8.747190,6.842811,8.857154,9.306448,0.435989,-9.663773,4.366363,7.177286,-4.398926,-4.476055,1.183888,6.086684,-8.359815,6.226321,7.069954,5.547899,-9.889347,-9.194721,3.311233,-6.656020,0.591493,-5.301746,-9.451657,-8.309542,2.856454,-7.501984,-5.837847,3.714582,-3.123159,-2.953993,8.056973,-9.545196,-2.040857,5.075291,-1.486739,-8.790232,-9.749264,9.525180,-4.701615,2.303292,-5.947184,-1.968480,-4.458949,6.103128,-7.852905,-7.808594,1.641670,8.223743,7.070932,1.650360,-0.848535,8.780636,-7.621175,0.851120,-0.942905,-7.859918,5.839498,3.775224,5.545492,-6.362796,-0.578384,4.847164,4.852911,6.519155,-6.431378,0.642522,-2.614722,0.500468,4.535334,-5.326465,-8.027907,-6.655449,1.533411,3.429795,-7.948862,7.081127,-5.998955,-4.254086,3.185161,-2.736448,-6.047341,0.067183,-6.307123,-3.316826,4.770741,9.609997,1.605133,0.225392,5.481898,1.510501,3.856666,-9.698580,-7.882372,2.501688,-1.408132,3.595461,7.459301,6.226983,8.151576,5.796266,-4.329325,-9.266605,-3.248404,3.641387,-9.854851,2.039242,6.012937,0.976626,-0.930358,2.858414,-2.137492,-9.218452,1.000673,7.581780,9.039186,-5.961836,0.479555,7.575391,-5.935106,7.280260,-1.879929,-1.226615,-1.723251,2.075321,7.468503,7.670019,6.503449,9.709647,-3.708739,7.366420,-2.373308,7.792039,2.073198,8.718224,5.508179,-5.776156,-7.221640,0.444664,7.299930,7.817293,-9.317050,-7.520439,-7.377046,-4.005345,3.933888,-0.201533,1.252717,4.402177,0.089517,7.918831,-0.154690,-9.844784,-7.824717,2.521561,-1.069762,-5.428110,-6.123482,-6.021754,5.437275,1.878689,-8.160847,-0.365957,1.264108,-1.119154,-1.624680,-6.825951,-7.680910,3.718048,-8.614804,-3.531246,-8.889527,5.598103,1.082474,5.794860,3.724179,7.458913,1.719057,5.738025,-9.314456,5.558867,5.090228,4.208673,-1.829432,9.462289,6.655964,6.229120,-9.342911,-1.510274,-8.997817,-9.188089,-0.689739,8.666899,3.179964,0.077441,2.430706,8.153517,-5.028041,-5.992115,7.002185,3.204402,3.933637,-3.690193,-9.265961,0.888321,1.454371,-3.251683,-6.692107,3.826523,-5.647730,2.816291,2.400352,5.588703,2.319035,-9.666654,3.398281,1.697018,-3.841766,-5.028385,9.483780,8.120406,-6.120868,-4.683524,1.940889,-7.493771,-1.919766,5.772164,-8.929376,7.107682,-1.749611,1.498756,-4.438663,-8.507631,-4.123169,1.195001,4.981633,-4.392079,-1.120201,-8.201912,-3.883912,1.497800,-4.824975,-2.385678,7.531730,-9.750224,8.146097,1.641270,-3.698243,-5.249318,2.610566,-1.691430,-6.423181,-9.434811,-7.281766,8.703304,0.660911,4.270707,2.110948,5.778619,-6.929081,9.304176,1.727489,2.710712,-7.772825,-0.555435,8.511059,-6.192384,-4.670573,-4.294214,1.684319,3.694568,-2.726648,-5.586843,4.625345,3.675772,4.354171,2.011659,7.607313,5.282866,9.766822,4.861324,-3.982686,-1.095124,-0.099689,4.788503,-6.543424,1.598245,-1.705369,1.436681,6.357248,3.683213,3.292691,7.829984,9.926164,-3.951742,-6.306598,7.936192,-5.009201,3.327622,-0.920768,-6.336608,-3.027599,5.428748,-1.503080,-0.790730,4.056304,-7.201888,-1.547331,-0.188315,-2.769442,-5.024165,-1.289997,-4.966423,-6.426649,-6.835217,-1.970913,2.286309,-7.784432,1.321702,5.363784,-1.771135,7.065397,4.330641,-4.428628,7.157355,7.000899,6.836563,7.153203,-3.664166,-4.517587,-6.469187,7.041053,8.504305,0.090179,-7.272781,-8.201506,1.877712,-5.828959,7.472274,-8.210468,0.443528,5.566812,-8.536257,-2.397536,-1.507819,4.182718,-5.667905,-1.939194,-8.652755,-6.251620,8.630670,7.813407,3.833900,0.126867,-3.647445,2.190509,1.680399,-6.451884,-4.254782,-7.217672,3.354162,5.433030,6.223547,1.676867,4.613988,-5.065981,-2.035566,-4.790029,6.574805,3.523253,2.746311], dtype = "float32")#candidate|5206|(1584,)|const|float32
call_5205 = relay.TupleGetItem(func_423_call(relay.reshape(const_5206.astype('float32'), [16, 11, 9]), relay.reshape(const_5206.astype('float32'), [16, 11, 9]), ), 1)
call_5207 = relay.TupleGetItem(func_426_call(relay.reshape(const_5206.astype('float32'), [16, 11, 9]), relay.reshape(const_5206.astype('float32'), [16, 11, 9]), ), 1)
func_2686_call = mod.get_global_var('func_2686')
func_2687_call = mutated_mod.get_global_var('func_2687')
call_5209 = relay.TupleGetItem(func_2686_call(), 0)
call_5210 = relay.TupleGetItem(func_2687_call(), 0)
func_4739_call = mod.get_global_var('func_4739')
func_4741_call = mutated_mod.get_global_var('func_4741')
var_5216 = relay.var("var_5216", dtype = "float64", shape = (35,))#candidate|5216|(35,)|var|float64
call_5215 = relay.TupleGetItem(func_4739_call(relay.reshape(var_5216.astype('float64'), [1, 35])), 6)
call_5217 = relay.TupleGetItem(func_4741_call(relay.reshape(var_5216.astype('float64'), [1, 35])), 6)
output = relay.Tuple([call_5198,call_5201,call_5205,const_5206,call_5209,call_5215,var_5216,])
output2 = relay.Tuple([call_5199,call_5202,call_5207,const_5206,call_5210,call_5217,var_5216,])
func_5222 = relay.Function([var_5216,], output)
mod['func_5222'] = func_5222
mod = relay.transform.InferType()(mod)
mutated_mod['func_5222'] = func_5222
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5223 = relay.var("var_5223", dtype = "float64", shape = (35,))#candidate|5223|(35,)|var|float64
func_5222_call = mutated_mod.get_global_var('func_5222')
call_5224 = func_5222_call(var_5223)
output = call_5224
func_5225 = relay.Function([var_5223], output)
mutated_mod['func_5225'] = func_5225
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5152_call = mod.get_global_var('func_5152')
func_5153_call = mutated_mod.get_global_var('func_5153')
call_5296 = relay.TupleGetItem(func_5152_call(), 1)
call_5297 = relay.TupleGetItem(func_5153_call(), 1)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_5298 = func_3833_call()
call_5299 = func_3833_call()
func_2390_call = mod.get_global_var('func_2390')
func_2393_call = mutated_mod.get_global_var('func_2393')
var_5304 = relay.var("var_5304", dtype = "float32", shape = (135,))#candidate|5304|(135,)|var|float32
const_5305 = relay.const([[6.549303,-9.350741,3.525796,-6.723491,3.664995,-6.085137,0.811786,5.799324,-6.873279],[-6.016389,9.430164,2.711356,-8.926548,6.493096,2.529342,5.105760,8.428802,-0.336845],[2.012829,8.517777,-2.193845,-0.417360,-3.532564,-1.203408,-4.653065,4.389550,5.928211],[2.904635,8.182136,5.466745,-5.015022,-5.944854,-5.953135,7.067924,9.813199,-7.446672],[-0.920410,6.331308,-9.127731,6.500562,9.218280,-4.442361,1.748303,-3.967814,-5.905934],[-3.983556,-2.548229,-3.369442,1.171500,-2.827030,-5.290774,-5.413017,4.466967,-4.507090],[6.714329,-6.588010,-0.516512,-8.477661,7.181382,5.197323,-1.504884,-4.103757,-4.656187],[5.983110,-3.621177,-8.496330,-2.109421,-4.514949,-9.921922,6.316678,-2.031425,-1.502474],[-9.741715,2.568054,6.127549,2.453673,-6.430786,-0.557847,1.982220,-7.508610,-2.480220],[-5.851534,-5.301439,-0.273453,6.759149,-5.541217,-6.118122,5.502210,9.976207,-3.923607],[7.684103,-6.373753,5.988822,-4.860496,-1.245135,7.515215,6.667921,7.176979,-0.200324],[-5.108145,2.472016,7.767820,-2.219657,-4.238157,7.500007,-7.754607,1.749947,-0.154953],[-0.699408,4.582057,-2.458676,3.916136,-8.534155,8.641103,-8.585886,3.807626,-5.930187],[7.645080,9.571727,7.349779,-8.635955,4.643420,-4.200186,7.758462,-5.962648,-6.881352],[3.885674,-8.272134,-9.863353,-6.864325,4.451782,6.185080,-7.386045,-3.590765,-8.298654],[6.240807,-4.795151,-1.919212,-7.960206,6.055808,-3.302059,9.974230,5.287954,-9.003977],[4.789372,-9.864190,-1.784186,7.888976,3.690489,-6.930637,0.835704,-8.889954,-5.985602],[-9.570487,-8.105547,9.919531,8.677392,-9.366868,-9.670059,6.325197,1.955341,-1.806646],[4.579515,6.465619,-7.526319,-8.241930,3.418145,3.331702,-5.038198,-7.974191,0.209178],[5.794454,7.519271,3.111905,-2.694043,9.200802,-4.663589,1.307008,7.702528,-6.496142],[-7.529269,4.312946,-9.601136,7.096366,7.357887,1.537160,0.696935,2.695214,5.357912],[-8.261321,2.285759,7.915959,-1.043425,6.115579,0.756365,6.518756,8.262921,8.495757],[3.361737,-2.980792,8.980584,1.230259,-2.789160,6.534204,2.690734,-5.768650,3.214487],[-6.886927,-0.073083,-7.196540,-1.822436,-3.164074,-4.544482,4.106128,-0.447674,-7.627875],[1.394259,0.665719,3.662698,8.841180,-2.862784,6.251060,-5.986884,8.832963,-7.949680],[-0.815986,8.177589,-5.004063,9.576854,2.515204,1.037697,7.599581,6.868678,-2.395845],[7.233370,1.659020,7.250193,7.520466,9.892005,7.296791,-6.501707,-1.247029,-1.008159],[-4.118110,-2.990469,5.166354,5.166933,-4.745522,8.151460,9.224487,4.451450,3.156901],[-5.494949,-9.470011,5.541872,8.383975,4.400527,-9.742985,-2.477930,7.715642,-7.496817],[-5.729643,4.310509,4.222361,4.716952,0.056734,1.743558,-0.271302,-6.288132,0.292779],[-5.250620,7.718577,-5.980300,9.717478,-8.183195,3.864253,4.589577,5.986402,4.162069],[-5.416732,6.855041,4.459330,-3.433346,-0.942511,-2.511191,-7.251336,-6.470384,-8.703413],[7.883229,5.438345,6.850074,0.274742,-3.820838,1.829112,6.034455,3.842270,-8.456732],[6.927509,-6.778382,8.676540,-5.323766,4.200620,9.745098,1.497389,0.773478,4.990421],[-2.675795,2.900430,3.825474,-2.607183,-6.953542,3.498858,-3.501758,3.994652,0.203488],[8.118808,8.211713,-2.303774,-9.037411,0.754345,8.748669,-5.362142,3.740315,-0.828794],[9.988484,4.172553,-3.095815,-8.503449,-4.900789,7.643762,-7.813974,1.901018,7.654687],[-9.663415,9.731928,7.196885,-0.378970,-0.553341,-1.177861,-5.048600,8.561858,9.362843],[4.922749,-7.778007,-9.363175,2.931528,-8.240912,-6.994266,-0.302040,-0.200847,-7.973849],[-1.742813,3.369380,3.714409,-4.877000,0.629775,5.345359,4.337894,-0.275629,-2.267746],[-1.373060,1.249694,-2.606457,-7.403730,7.777590,3.653841,5.157152,-0.991338,-5.530129],[-5.036789,-9.232246,6.725576,-2.157988,-9.862208,-4.873657,6.148882,-1.419445,-2.592859],[-8.166339,9.293865,5.452470,-2.747122,5.044797,7.733674,-5.223789,-0.605332,-4.652195],[-7.572029,-6.742181,7.444487,-3.715765,2.176445,-2.085031,4.774706,8.971696,-3.109046],[2.822150,4.486740,1.406832,7.858175,-5.022605,-2.060910,9.668335,1.337412,9.969570],[-6.538964,-2.859266,-0.564613,2.650232,6.723963,4.152770,2.749142,-7.040590,2.479111],[-0.808659,2.229458,-8.459764,8.847532,1.975112,6.599181,9.065287,-7.470737,-7.727143],[-0.925293,-5.088657,-1.604674,6.634189,7.957490,-4.938802,-6.767347,7.601577,4.841285],[3.339424,2.208344,2.527744,-8.722312,-8.911856,-5.886927,6.712301,3.529510,0.441694],[4.752270,4.128058,-6.956243,2.324966,-6.390130,5.913606,-6.647129,-6.223298,1.398976],[5.427130,3.314343,-2.906888,-1.463720,-5.852424,4.736092,9.028799,7.682243,7.181065],[-4.128282,-9.127422,6.219977,-0.282305,-2.679808,8.485745,-0.529170,3.034940,1.956381],[-0.985296,-6.947726,3.730748,-9.020752,-7.684654,3.707926,3.369928,0.729990,7.206482],[5.695559,-3.893340,-2.121983,0.077389,-6.399714,-6.407669,-2.755064,1.817404,-2.028288],[9.480465,1.032400,-0.975219,4.025055,-4.124865,3.418738,-4.278370,1.708670,-8.577185],[-8.182910,5.766293,0.306549,-1.731133,-3.363917,-2.097185,-1.557123,8.910761,0.051665],[8.176817,8.609724,0.518751,3.019376,-6.234998,0.715327,-1.882173,-3.403863,-3.884064],[-6.347334,-4.176230,2.949977,3.061074,-1.817125,5.169489,-2.394544,-6.235432,3.540978],[-0.509942,6.424639,3.076957,5.629542,3.596435,9.839534,3.112234,-2.714613,-3.718967],[-5.671543,-0.130613,-2.578627,0.788840,-0.722465,1.652112,3.771910,-4.163004,-6.320964],[2.228459,2.938170,5.419476,2.115578,-2.845252,-3.210774,0.994950,-4.717210,5.752773],[1.843400,7.877861,7.824463,6.989350,-7.408957,7.247806,-2.342183,9.165223,1.792918],[-2.663280,6.157455,7.176439,-5.480713,8.635738,-9.014999,3.064356,7.245238,8.603685],[7.416719,6.674336,-6.069106,-2.217764,-7.780844,-4.078898,2.717952,-4.623090,-5.942144],[-3.914650,-5.756848,4.835134,8.663267,-4.811959,-2.193096,9.996074,6.106550,1.863165],[4.711882,-5.154689,6.403327,-9.291026,0.502921,-3.247949,-3.741707,-0.901364,-2.397409],[2.466388,0.290912,-1.106763,4.449376,9.345692,-0.576453,-9.144136,1.600320,9.802750],[5.275735,0.416769,-7.466523,-5.549582,-6.135361,9.671697,9.052655,-5.868100,2.394741],[-1.682747,-8.220762,9.676283,-3.938672,8.179279,-1.097026,8.517029,-2.526008,-1.795826],[-4.212872,2.330143,-0.175121,6.399556,2.608050,-4.375237,-9.737234,1.197126,-9.113307],[8.595634,-3.354798,-1.154543,-4.158357,-0.085951,-8.111764,4.984415,-7.826093,-6.751194],[-8.616268,-3.790168,7.367311,-9.774034,3.560747,3.043845,-7.979077,-9.235762,0.731626],[9.903701,-3.918425,-5.967407,-3.151092,6.586334,-4.048090,5.814553,6.690579,-8.475793],[-0.613388,-6.211120,-3.712667,-7.868970,5.493982,3.761596,0.762198,-3.466495,-9.003433],[2.853883,-2.853395,7.866317,-4.036917,8.756170,-4.010739,-9.589132,-4.007035,-0.236770],[-8.351066,0.481858,-5.144935,-6.424880,3.556921,3.709744,6.668888,0.751418,-2.155419],[-2.954966,3.067341,-6.626828,7.391361,6.052749,-5.656102,-4.829638,-0.211415,-3.643118],[-2.037867,-2.829121,5.149889,-2.376506,-0.960611,-5.054475,-2.699760,7.278406,6.465757],[-7.689539,7.606579,-3.311801,4.852163,-8.643961,4.665934,-0.413991,-9.158317,8.370236],[2.187987,-6.749776,0.583654,-9.081708,-4.704215,-1.128369,0.284910,-1.785678,-8.680333],[-5.427271,-6.315694,3.456929,4.044587,4.967899,-7.009837,1.650322,-5.098902,-3.070031],[1.774688,-6.348844,-5.973766,2.242675,6.541559,-9.074701,-0.538521,1.294999,-3.705279],[-6.318823,3.447612,5.626456,9.709007,2.135118,-9.068176,7.803084,-1.806716,7.398203],[-4.950551,-1.911647,2.849073,1.826855,-5.192794,-0.109542,0.990872,-6.650487,-2.975668],[5.723180,8.034834,-9.485850,-8.897399,9.926075,3.424773,8.120693,4.038325,4.133089],[6.507861,-9.526082,0.630297,-9.265026,-5.508036,2.903141,-1.537988,-6.433748,1.006518],[8.668637,-9.444293,-7.510382,-5.601575,-5.459382,-5.319702,-8.912211,-9.395945,3.769854],[5.421546,3.565815,-2.818228,-9.602430,5.651026,-1.211347,1.493886,-6.168603,-4.730975],[3.342813,-1.234762,-8.834983,8.068854,-3.575765,-4.708672,-6.759252,8.628963,0.249754],[-5.078259,-2.514177,-9.677303,3.156590,4.522619,2.001241,-7.614607,-4.382295,-9.720232],[8.457187,2.095202,-2.024389,4.449351,2.460091,-5.658507,1.759332,-2.837177,-8.359972],[-1.379431,5.974735,8.531009,-4.375529,4.117939,-8.230982,8.351396,-2.191429,-6.077281],[-6.759076,2.431439,-6.909159,-6.173874,-8.542272,-2.698955,7.976496,-9.917644,-6.441063],[-2.376514,-6.282310,0.411969,5.467012,-1.839072,8.110507,-3.747247,8.957430,2.867281],[3.506206,7.157514,-1.190517,-6.274589,-5.284352,-9.848422,-2.440747,7.752044,6.360876],[-3.561294,-6.042475,-1.144623,3.827940,6.316519,-9.222395,-8.883029,5.797903,8.358977],[2.326156,6.092296,0.597473,-9.268999,-5.437243,-0.645393,-3.148384,8.150324,8.403699],[-3.886453,-5.056332,8.301140,-6.837709,3.737778,9.008353,-7.257788,-5.013463,8.339083],[9.052292,-5.007642,1.048451,1.703255,3.666929,-2.548390,-4.161782,9.703843,6.119433],[3.497722,-3.612553,1.267715,-5.410966,6.390615,5.344117,-0.684840,-3.120547,2.807421],[2.943300,-5.295832,9.739550,1.050179,1.275929,-3.651280,-9.585604,9.302250,-0.442229],[-0.256478,-2.338389,-1.956522,-1.037057,-6.021385,5.455757,9.652645,5.154648,2.771709],[-1.314598,-1.404142,0.560061,-4.413249,6.274398,-2.625764,-8.718577,-9.027943,-8.257527],[9.190981,6.063113,-3.727279,7.739576,7.511494,7.948433,1.504236,8.900560,9.290890],[-9.594252,-6.976734,0.873362,-6.273702,-5.508048,-2.409634,8.187380,2.475905,-3.070552],[2.907102,2.241407,-1.765534,7.523233,3.460651,9.326541,7.019796,-5.846057,2.733050],[-9.052413,-7.350865,-5.737037,-4.581253,-0.097796,-5.782949,5.954655,-1.733824,-7.124900],[7.705155,-8.113272,2.502342,6.009179,8.880601,-8.914125,-1.139930,-3.677022,0.573707],[3.663711,-9.527055,-6.855529,-1.194141,-7.714607,-1.784435,4.185198,-6.465693,-2.714225],[-3.691954,-4.700348,-5.349338,-3.082143,-4.799583,2.207232,-7.678616,1.821369,-5.168788],[2.858944,2.321325,7.976603,0.556746,6.641242,-8.668192,1.096943,6.460117,-2.573192],[-0.740676,-6.521230,-7.846188,5.949849,7.765034,9.127544,-9.664971,-2.460936,5.480611],[7.471089,4.471788,-3.586485,7.926616,-7.758684,-3.579254,-6.246158,8.330086,4.404450],[-1.392194,-5.384622,1.892273,2.939487,8.711923,5.834557,2.905936,3.543827,5.734342],[-0.532488,6.110036,1.437004,5.587508,-6.839702,3.486781,-9.273586,-9.611152,0.812307],[5.952220,7.050615,-4.659437,2.378328,-5.416568,-2.927523,-9.948649,-1.576453,0.329612],[5.228837,8.013477,-6.753309,1.985481,-0.358688,5.824927,5.710072,-5.528980,1.218099],[1.588602,-6.128468,6.767264,1.525566,6.907345,1.108090,-0.830254,6.604474,9.282424],[-3.105869,3.234094,-7.975682,-5.518370,0.464900,8.680433,6.653746,8.701586,-6.868536],[7.054086,-9.514175,2.725737,2.365985,7.291077,7.883680,-8.010836,9.044418,-3.181492],[5.990728,-1.752886,9.945879,7.243235,-8.642572,-6.592121,-4.744085,8.871069,-9.665409]], dtype = "float32")#candidate|5305|(121, 9)|const|float32
call_5303 = relay.TupleGetItem(func_2390_call(relay.reshape(var_5304.astype('float32'), [135,]), relay.reshape(const_5305.astype('float32'), [1089,]), ), 7)
call_5306 = relay.TupleGetItem(func_2393_call(relay.reshape(var_5304.astype('float32'), [135,]), relay.reshape(const_5305.astype('float32'), [1089,]), ), 7)
func_4469_call = mod.get_global_var('func_4469')
func_4474_call = mutated_mod.get_global_var('func_4474')
var_5315 = relay.var("var_5315", dtype = "float32", shape = (896,))#candidate|5315|(896,)|var|float32
const_5316 = relay.const([[-0.829603,4.842221],[-8.646787,7.380440],[-1.868035,-8.758745],[2.661560,-9.538955],[2.577740,8.591064],[-0.343094,-9.291457],[4.748612,2.068955],[2.762124,-9.443651],[2.024673,-6.722711],[5.124695,0.480920],[-0.296444,6.098412],[-6.309533,-2.853970],[-3.311259,-6.909683],[0.608409,-6.802401],[-2.572812,-1.715833],[-6.271618,2.952328],[-6.879118,-4.138845],[1.466748,5.034086],[3.776119,1.143573],[-4.231969,2.140259],[0.938913,7.296355],[-1.182805,5.180621],[-3.686423,-4.187558],[-9.941363,-0.979268],[7.955661,-6.090170],[-6.611643,-8.288541],[-6.615321,9.757656],[9.051613,8.712007],[-1.825393,9.370320],[3.913078,-4.846878],[-2.342215,-7.973171],[-7.811729,6.493513],[5.366817,3.526915],[-8.397421,7.598287],[7.870623,3.816498],[6.943260,-5.162529],[-6.863701,-4.018196],[-9.504613,1.055336],[-6.267627,-8.679423],[-4.868722,-9.069790],[2.148768,6.247529],[-1.731176,7.166683],[3.495174,-1.159069],[8.688943,-8.329207],[6.184193,8.813226],[0.435668,-3.256564],[3.534218,8.103526],[7.858437,9.764392],[0.547646,-1.530596],[-9.009096,5.891576],[-5.462123,-8.801503],[-6.504161,7.855849]], dtype = "float64")#candidate|5316|(52, 2)|const|float64
var_5317 = relay.var("var_5317", dtype = "float32", shape = (132, 12))#candidate|5317|(132, 12)|var|float32
call_5314 = relay.TupleGetItem(func_4469_call(relay.reshape(var_5315.astype('float32'), [16, 8, 7]), relay.reshape(const_5316.astype('float64'), [104,]), relay.reshape(var_5317.astype('float32'), [1584,]), ), 0)
call_5318 = relay.TupleGetItem(func_4474_call(relay.reshape(var_5315.astype('float32'), [16, 8, 7]), relay.reshape(const_5316.astype('float64'), [104,]), relay.reshape(var_5317.astype('float32'), [1584,]), ), 0)
output = relay.Tuple([call_5296,call_5298,call_5303,var_5304,const_5305,call_5314,var_5315,const_5316,var_5317,])
output2 = relay.Tuple([call_5297,call_5299,call_5306,var_5304,const_5305,call_5318,var_5315,const_5316,var_5317,])
func_5319 = relay.Function([var_5304,var_5315,var_5317,], output)
mod['func_5319'] = func_5319
mod = relay.transform.InferType()(mod)
mutated_mod['func_5319'] = func_5319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5319_call = mutated_mod.get_global_var('func_5319')
var_5321 = relay.var("var_5321", dtype = "float32", shape = (135,))#candidate|5321|(135,)|var|float32
var_5322 = relay.var("var_5322", dtype = "float32", shape = (896,))#candidate|5322|(896,)|var|float32
var_5323 = relay.var("var_5323", dtype = "float32", shape = (132, 12))#candidate|5323|(132, 12)|var|float32
call_5320 = func_5319_call(var_5321,var_5322,var_5323,)
output = call_5320
func_5324 = relay.Function([var_5321,var_5322,var_5323,], output)
mutated_mod['func_5324'] = func_5324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_5344 = relay.TupleGetItem(func_2978_call(), 1)
call_5345 = relay.TupleGetItem(func_2980_call(), 1)
func_1813_call = mod.get_global_var('func_1813')
func_1816_call = mutated_mod.get_global_var('func_1816')
const_5368 = relay.const([3.124348,5.602207,0.358029,3.504688,-4.634240,6.285238,4.037402,-3.054313,-4.782675,-5.221857,-9.700710,-5.312391,-9.077270,2.782584,-9.635823,-1.297985,-8.213356,6.995810,1.135202,-9.633669,2.710968,-1.873400,2.618058,6.804673,-8.343959,-8.955640,-3.835337,-1.099815,4.735909,-8.383563,-4.139151,1.138833,-7.932137,-2.325497,7.249600], dtype = "float64")#candidate|5368|(35,)|const|float64
call_5367 = relay.TupleGetItem(func_1813_call(relay.reshape(const_5368.astype('float64'), [7, 5])), 2)
call_5369 = relay.TupleGetItem(func_1816_call(relay.reshape(const_5368.astype('float64'), [7, 5])), 2)
output = relay.Tuple([call_5344,call_5367,const_5368,])
output2 = relay.Tuple([call_5345,call_5369,const_5368,])
func_5376 = relay.Function([], output)
mod['func_5376'] = func_5376
mod = relay.transform.InferType()(mod)
mutated_mod['func_5376'] = func_5376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5376_call = mutated_mod.get_global_var('func_5376')
call_5377 = func_5376_call()
output = call_5377
func_5378 = relay.Function([], output)
mutated_mod['func_5378'] = func_5378
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3833_call = mod.get_global_var('func_3833')
func_3835_call = mutated_mod.get_global_var('func_3835')
call_5406 = func_3833_call()
call_5407 = func_3833_call()
output = call_5406
output2 = call_5407
func_5412 = relay.Function([], output)
mod['func_5412'] = func_5412
mod = relay.transform.InferType()(mod)
output = func_5412()
func_5413 = relay.Function([], output)
mutated_mod['func_5413'] = func_5413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_5430 = func_4227_call()
call_5431 = func_4227_call()
output = relay.Tuple([call_5430,])
output2 = relay.Tuple([call_5431,])
func_5435 = relay.Function([], output)
mod['func_5435'] = func_5435
mod = relay.transform.InferType()(mod)
mutated_mod['func_5435'] = func_5435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5435_call = mutated_mod.get_global_var('func_5435')
call_5436 = func_5435_call()
output = call_5436
func_5437 = relay.Function([], output)
mutated_mod['func_5437'] = func_5437
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4013_call = mod.get_global_var('func_4013')
func_4015_call = mutated_mod.get_global_var('func_4015')
call_5438 = relay.TupleGetItem(func_4013_call(), 0)
call_5439 = relay.TupleGetItem(func_4015_call(), 0)
func_3106_call = mod.get_global_var('func_3106')
func_3109_call = mutated_mod.get_global_var('func_3109')
var_5445 = relay.var("var_5445", dtype = "float32", shape = (3, 45))#candidate|5445|(3, 45)|var|float32
var_5446 = relay.var("var_5446", dtype = "float32", shape = (1089,))#candidate|5446|(1089,)|var|float32
call_5444 = relay.TupleGetItem(func_3106_call(relay.reshape(var_5445.astype('float32'), [135,]), relay.reshape(var_5446.astype('float32'), [1089,]), ), 1)
call_5447 = relay.TupleGetItem(func_3109_call(relay.reshape(var_5445.astype('float32'), [135,]), relay.reshape(var_5446.astype('float32'), [1089,]), ), 1)
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
const_5464 = relay.const([[-10,10,7,1,-6,-7,2,-5,-3,-6,-2,8,-7,8,-9,-6,7,-3,10,2,2,10,-7,2,1,-2,-6,5,-9,9,-1,-7,3,-3,-3,-8,6,2,2,-1,1,-5],[6,-2,5,5,8,-4,-3,5,-2,4,2,1,-9,8,8,6,-5,8,-10,6,6,-3,7,-6,3,-8,5,1,-2,1,4,5,-6,9,-8,5,7,3,-6,-4,9,5],[3,-6,-5,-6,-6,6,4,7,-4,-3,2,4,5,6,2,-5,-7,10,2,9,-7,-10,-4,-10,-1,9,1,1,5,-9,1,2,9,-10,-7,8,3,4,7,6,-1,3],[-2,9,6,-2,3,4,7,-2,-2,10,-10,-5,-8,-7,7,2,-6,5,-8,6,-3,3,6,-6,-10,4,-1,-7,9,10,3,7,1,-1,1,10,10,5,1,-4,8,-8],[-4,-7,-10,3,9,5,2,-6,-5,-10,-10,-3,-6,1,-3,-2,6,4,-6,-3,6,4,-6,-2,9,-8,-7,-9,7,9,-8,1,-10,-2,-1,-3,3,-5,-10,-1,-1,5],[1,-10,-5,-10,-10,9,-7,10,7,5,1,-10,10,-9,10,8,-9,10,7,-6,-5,1,-7,-10,-4,-4,-8,7,6,7,-9,9,-3,-1,1,9,2,7,-1,-4,3,-10],[-4,7,3,10,-8,2,-6,-2,-2,-4,-3,6,6,-8,9,10,-9,7,-10,5,-4,9,-2,8,4,-10,2,2,7,-9,-10,-2,-3,-10,-6,10,4,1,-10,1,10,10],[9,-2,-4,5,-7,2,7,-2,8,2,-9,7,-1,-3,2,-5,-7,-7,5,4,10,1,-9,10,-6,9,-3,-7,7,-7,3,-1,-8,-1,2,-6,-1,-10,1,8,-2,3],[7,2,-9,-4,1,-5,4,2,3,-8,7,7,-8,5,3,-5,-9,-6,-6,-3,6,5,-7,-5,7,7,3,-1,-10,-1,6,5,3,-6,-10,3,10,-5,5,7,5,-5],[5,-9,2,-8,-6,-6,4,5,4,9,7,8,6,-5,9,-7,-4,9,-6,6,2,10,-3,-10,-4,10,-5,-5,-6,-9,-10,9,-5,-2,7,-3,-10,-7,-10,2,7,7]], dtype = "uint32")#candidate|5464|(10, 42)|const|uint32
call_5463 = relay.TupleGetItem(func_904_call(relay.reshape(const_5464.astype('uint32'), [14, 5, 6])), 0)
call_5465 = relay.TupleGetItem(func_906_call(relay.reshape(const_5464.astype('uint32'), [14, 5, 6])), 0)
func_1813_call = mod.get_global_var('func_1813')
func_1816_call = mutated_mod.get_global_var('func_1816')
var_5468 = relay.var("var_5468", dtype = "float64", shape = (7, 5))#candidate|5468|(7, 5)|var|float64
call_5467 = relay.TupleGetItem(func_1813_call(relay.reshape(var_5468.astype('float64'), [7, 5])), 0)
call_5469 = relay.TupleGetItem(func_1816_call(relay.reshape(var_5468.astype('float64'), [7, 5])), 0)
output = relay.Tuple([call_5438,call_5444,var_5445,var_5446,call_5463,const_5464,call_5467,var_5468,])
output2 = relay.Tuple([call_5439,call_5447,var_5445,var_5446,call_5465,const_5464,call_5469,var_5468,])
func_5479 = relay.Function([var_5445,var_5446,var_5468,], output)
mod['func_5479'] = func_5479
mod = relay.transform.InferType()(mod)
var_5480 = relay.var("var_5480", dtype = "float32", shape = (3, 45))#candidate|5480|(3, 45)|var|float32
var_5481 = relay.var("var_5481", dtype = "float32", shape = (1089,))#candidate|5481|(1089,)|var|float32
var_5482 = relay.var("var_5482", dtype = "float64", shape = (7, 5))#candidate|5482|(7, 5)|var|float64
output = func_5479(var_5480,var_5481,var_5482,)
func_5483 = relay.Function([var_5480,var_5481,var_5482,], output)
mutated_mod['func_5483'] = func_5483
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4299_call = mod.get_global_var('func_4299')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_5527 = relay.TupleGetItem(func_4299_call(), 3)
call_5528 = relay.TupleGetItem(func_4300_call(), 3)
output = relay.Tuple([call_5527,])
output2 = relay.Tuple([call_5528,])
func_5536 = relay.Function([], output)
mod['func_5536'] = func_5536
mod = relay.transform.InferType()(mod)
mutated_mod['func_5536'] = func_5536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5536_call = mutated_mod.get_global_var('func_5536')
call_5537 = func_5536_call()
output = call_5537
func_5538 = relay.Function([], output)
mutated_mod['func_5538'] = func_5538
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2686_call = mod.get_global_var('func_2686')
func_2687_call = mutated_mod.get_global_var('func_2687')
call_5608 = relay.TupleGetItem(func_2686_call(), 0)
call_5609 = relay.TupleGetItem(func_2687_call(), 0)
func_4070_call = mod.get_global_var('func_4070')
func_4074_call = mutated_mod.get_global_var('func_4074')
const_5613 = relay.const([9.938053,-8.725178,2.819716,9.972940,-8.377416,9.382129,-0.242674,-4.572019,9.620717,-8.399351,-4.991728,-1.582728,4.520719,-8.722828,-0.364052,2.791830,3.245319,-7.671223,-6.399022,1.742074,-0.469423,7.250337,-6.464243,-4.278409,-9.527089,-0.112434,-1.944210,2.664820,6.357670,-9.452586,8.766888,3.792436,7.391548,5.628504,-0.809718,-4.688740,9.772409,3.584560,-5.805269,-6.911942,-5.340101,2.292440,0.107919,-6.403121,-2.591012,-4.219933,0.159374,-8.459749,-2.695290,-3.530158,-8.272143,8.861392,-3.862462,-9.139619,8.052466,-2.588257,4.237786,-9.334673,-6.484602,0.604833,9.583108,-5.469275,-2.428030,1.837763], dtype = "float32")#candidate|5613|(64,)|const|float32
const_5614 = relay.const([-0.393890,6.842762,9.486763,2.198775,-4.515600,-1.830607,1.421679,0.048776,3.784934,-4.448866,-7.819365,6.149003,0.573641,3.532349,2.873960,6.200288,-7.025497,-5.208979,-0.257113,-0.053519,1.530601,-8.036796,3.402599,-7.800269,5.247708,9.499134,-7.460498,-3.235243,8.049600,-3.020438,-2.158478,-2.709179,-6.081349,-3.644058,6.550821], dtype = "float64")#candidate|5614|(35,)|const|float64
var_5615 = relay.var("var_5615", dtype = "float32", shape = (135,))#candidate|5615|(135,)|var|float32
call_5612 = relay.TupleGetItem(func_4070_call(relay.reshape(const_5613.astype('float32'), [8, 1, 8]), relay.reshape(const_5614.astype('float64'), [35,]), relay.reshape(var_5615.astype('float32'), [135,]), ), 6)
call_5616 = relay.TupleGetItem(func_4074_call(relay.reshape(const_5613.astype('float32'), [8, 1, 8]), relay.reshape(const_5614.astype('float64'), [35,]), relay.reshape(var_5615.astype('float32'), [135,]), ), 6)
uop_5620 = relay.rsqrt(call_5612.astype('float64')) # shape=(135,)
uop_5622 = relay.rsqrt(call_5616.astype('float64')) # shape=(135,)
func_3118_call = mod.get_global_var('func_3118')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_5630 = relay.TupleGetItem(func_3118_call(), 0)
call_5631 = relay.TupleGetItem(func_3119_call(), 0)
output = relay.Tuple([call_5608,const_5613,const_5614,var_5615,uop_5620,call_5630,])
output2 = relay.Tuple([call_5609,const_5613,const_5614,var_5615,uop_5622,call_5631,])
func_5635 = relay.Function([var_5615,], output)
mod['func_5635'] = func_5635
mod = relay.transform.InferType()(mod)
var_5636 = relay.var("var_5636", dtype = "float32", shape = (135,))#candidate|5636|(135,)|var|float32
output = func_5635(var_5636)
func_5637 = relay.Function([var_5636], output)
mutated_mod['func_5637'] = func_5637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_5639 = relay.TupleGetItem(func_1643_call(), 0)
call_5640 = relay.TupleGetItem(func_1644_call(), 0)
output = relay.Tuple([call_5639,])
output2 = relay.Tuple([call_5640,])
func_5660 = relay.Function([], output)
mod['func_5660'] = func_5660
mod = relay.transform.InferType()(mod)
mutated_mod['func_5660'] = func_5660
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5660_call = mutated_mod.get_global_var('func_5660')
call_5661 = func_5660_call()
output = call_5661
func_5662 = relay.Function([], output)
mutated_mod['func_5662'] = func_5662
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3118_call = mod.get_global_var('func_3118')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_5683 = relay.TupleGetItem(func_3118_call(), 0)
call_5684 = relay.TupleGetItem(func_3119_call(), 0)
func_5635_call = mod.get_global_var('func_5635')
func_5637_call = mutated_mod.get_global_var('func_5637')
var_5699 = relay.var("var_5699", dtype = "float32", shape = (1, 135))#candidate|5699|(1, 135)|var|float32
call_5698 = relay.TupleGetItem(func_5635_call(relay.reshape(var_5699.astype('float32'), [135,])), 1)
call_5700 = relay.TupleGetItem(func_5637_call(relay.reshape(var_5699.astype('float32'), [135,])), 1)
func_5222_call = mod.get_global_var('func_5222')
func_5225_call = mutated_mod.get_global_var('func_5225')
const_5706 = relay.const([-0.045695,1.118045,-8.758605,-3.944521,2.941952,-0.473524,0.538774,-4.838386,5.128904,-7.287697,7.547990,2.796079,2.355343,-6.854526,-0.898965,2.064893,-5.477142,5.914826,-6.847799,7.621541,5.942100,-8.611474,0.754260,3.504990,-1.179893,-5.497839,-7.285859,3.414742,7.400126,-0.049664,-9.164038,-3.326940,-3.452381,-7.635623,-2.781811], dtype = "float64")#candidate|5706|(35,)|const|float64
call_5705 = relay.TupleGetItem(func_5222_call(relay.reshape(const_5706.astype('float64'), [35,])), 3)
call_5707 = relay.TupleGetItem(func_5225_call(relay.reshape(const_5706.astype('float64'), [35,])), 3)
func_4013_call = mod.get_global_var('func_4013')
func_4015_call = mutated_mod.get_global_var('func_4015')
call_5713 = relay.TupleGetItem(func_4013_call(), 0)
call_5714 = relay.TupleGetItem(func_4015_call(), 0)
output = relay.Tuple([call_5683,call_5698,var_5699,call_5705,const_5706,call_5713,])
output2 = relay.Tuple([call_5684,call_5700,var_5699,call_5707,const_5706,call_5714,])
func_5717 = relay.Function([var_5699,], output)
mod['func_5717'] = func_5717
mod = relay.transform.InferType()(mod)
mutated_mod['func_5717'] = func_5717
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5718 = relay.var("var_5718", dtype = "float32", shape = (1, 135))#candidate|5718|(1, 135)|var|float32
func_5717_call = mutated_mod.get_global_var('func_5717')
call_5719 = func_5717_call(var_5718)
output = call_5719
func_5720 = relay.Function([var_5718], output)
mutated_mod['func_5720'] = func_5720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3439_call = mod.get_global_var('func_3439')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_5776 = relay.TupleGetItem(func_3439_call(), 0)
call_5777 = relay.TupleGetItem(func_3440_call(), 0)
output = relay.Tuple([call_5776,])
output2 = relay.Tuple([call_5777,])
func_5778 = relay.Function([], output)
mod['func_5778'] = func_5778
mod = relay.transform.InferType()(mod)
output = func_5778()
func_5779 = relay.Function([], output)
mutated_mod['func_5779'] = func_5779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mod.get_global_var('func_4574')
func_4576_call = mutated_mod.get_global_var('func_4576')
call_5792 = relay.TupleGetItem(func_4574_call(), 0)
call_5793 = relay.TupleGetItem(func_4576_call(), 0)
output = call_5792
output2 = call_5793
func_5802 = relay.Function([], output)
mod['func_5802'] = func_5802
mod = relay.transform.InferType()(mod)
output = func_5802()
func_5803 = relay.Function([], output)
mutated_mod['func_5803'] = func_5803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_5849 = relay.TupleGetItem(func_1705_call(), 0)
call_5850 = relay.TupleGetItem(func_1707_call(), 0)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_5868 = func_2138_call()
call_5869 = func_2138_call()
func_3439_call = mod.get_global_var('func_3439')
func_3440_call = mutated_mod.get_global_var('func_3440')
call_5871 = relay.TupleGetItem(func_3439_call(), 1)
call_5872 = relay.TupleGetItem(func_3440_call(), 1)
uop_5874 = relay.log(call_5871.astype('float32')) # shape=(8, 12, 11)
uop_5876 = relay.log(call_5872.astype('float32')) # shape=(8, 12, 11)
func_2458_call = mod.get_global_var('func_2458')
func_2463_call = mutated_mod.get_global_var('func_2463')
const_5878 = relay.const([-8.474424,4.814674,2.704609,9.391699,0.643966,7.005920,8.389482,8.987815,-9.394759,-1.941085,4.198206,-3.061595,-6.986282,-2.609319,-6.496150,6.899752,-4.353601,-3.042857,-3.482933,3.081477,-3.110470,-0.357787,-0.122992,-5.526348,2.298545,-7.012448,3.189819,4.390413,6.716303,-7.319783,8.459380,-7.700064,-6.573254,1.575220,-4.557005,-9.258664,-3.778991,0.947306,-8.161563,8.948509,-1.472320,-2.780885,-4.913547,0.959103,4.193590,-9.349940,9.818149,4.574421,2.404318,-6.540747,1.224950,-9.248100,1.294296,-8.657946,3.968402,-2.460986,4.175993,-6.439977,-1.015217,3.140954,1.786773,-8.291968,-5.750593,-7.548646,3.506793,-2.334818,4.105213,-1.611275,-1.491947,-6.088710,-4.402046,6.953137,-1.585812,-9.035396,6.503173,-9.517722,0.699409,0.601901,-1.814980,3.277217,-9.067514,2.882923,8.015491,5.890169,-2.591111,6.535373,-4.380410,3.366552,-6.319343,8.609318,2.243412,-4.713483,5.555525,9.209305,1.069910,7.432259,-9.942922,6.824377,-5.215538,2.306771,3.064317,3.970410,8.050096,-9.063101,-9.573044,7.745596,2.012519,-8.339294,2.455011,6.558432,2.861776,-6.293469,2.999114,3.747365,-5.700689,-0.443835,6.838794,8.832570,-4.458646,4.636910,-5.146702,0.950726,-5.842152,-5.986731,2.798534,5.047485,-8.312453,-7.222582,3.957810,4.887432,-6.452302,8.054513,2.560386,-5.961577,-4.799934], dtype = "float32")#candidate|5878|(135,)|const|float32
const_5879 = relay.const([[-0.267125,-2.679695,1.618930,-6.104003,0.860797,3.075860,-2.989293,2.330886,-4.917627,7.766283,3.181824,-2.739278,8.940967,-1.376015,-1.028270,-0.551711,2.564690,-7.073706,-1.826915,-4.116075,5.751802,7.456467,-8.339658,-7.819403,6.205050,4.323214,9.204355,8.770103,6.886784,-8.331610,6.743317,-6.573227,7.926240,1.403538,-5.314650,2.288601,0.157396,7.826177,4.225001,-4.735624,9.016895,-8.304932,0.982629,3.572765,2.784917,-7.819916,1.141286,-2.475433,8.436351,-7.963341,5.496341,0.566602,-3.766867,7.261486,-7.769118,1.102172,5.856181,-5.702982,2.700317,9.733391,0.433798,0.393176,-6.332497,7.249503,8.083525,2.043563,-9.575568,2.122260,-8.412087,-3.860151,-0.232955,-4.547700,1.961034,2.420928,4.168952,-3.571838,-3.391762,7.379359,1.735908,3.808703,-2.754427,3.020796,5.688774,-8.203508,1.660665,2.168019,-5.990556,2.166729,-8.112542,-2.929964,1.997108,0.188956,-8.912154,1.474320,6.116746,-8.521286,3.298433,-3.393650,-2.156946],[-5.178558,-6.370936,1.199711,-8.795452,-2.743028,9.167895,-4.616956,6.558306,3.674610,-2.843392,4.073580,0.472938,9.385190,-1.817784,7.247107,-3.904955,-9.346302,7.451008,4.427039,7.687626,2.456458,-5.422166,7.421681,7.643101,4.864733,6.984944,1.109952,-5.221121,-8.944163,1.568983,9.452115,0.635431,-3.868807,-3.007121,-2.643825,4.425365,-0.814905,4.449961,-2.629082,-0.404458,-5.906787,-0.482869,-9.709292,6.469616,8.678170,3.869666,-4.215149,0.330775,8.134254,1.315138,8.680299,2.300213,-7.632310,8.629955,6.320663,6.210541,-3.772869,-6.414226,-3.198456,2.183066,-3.480511,8.148405,8.489947,1.976462,-7.533805,5.953729,1.749801,4.013952,6.239895,-3.545732,8.587783,9.649646,-5.111303,-3.821319,0.142215,-2.235840,-8.563266,-4.015288,-3.112689,3.414970,-1.461853,-3.719180,7.861583,-3.982677,7.010453,-1.984061,-6.367949,-2.711694,6.324143,8.760716,-0.065914,-7.935358,7.682476,-4.828713,-6.064003,-9.809881,-5.329535,-5.474773,0.675716],[2.598696,-1.816749,8.816278,4.065264,1.371538,-8.703833,5.631821,-6.169970,-3.507962,-0.701285,-2.272581,-5.478545,-6.009524,7.921792,-1.816764,0.705652,6.480571,8.935952,-4.373764,-8.551870,8.955766,-0.911724,2.263243,-6.382122,7.866834,7.774954,2.880692,-0.872530,-7.442798,6.703648,-2.103823,-5.552108,-2.248024,-7.083714,-7.921868,-1.935322,-0.097248,-9.169259,5.545487,0.381098,-3.258562,-2.764345,-7.983587,4.584898,6.529644,1.275897,6.354345,3.972542,-7.808293,-6.534537,4.842520,-4.504473,9.176844,4.661533,-0.315457,8.832803,7.153625,-9.691346,8.019857,1.680244,-7.348772,-5.268767,-6.596917,0.147208,-8.641297,-9.020788,-6.279657,2.355172,0.460290,3.476097,9.526022,-3.943161,-5.612895,-4.758180,-7.936430,-9.813750,-6.141664,-0.376601,9.519631,9.027321,1.324180,9.708336,6.550865,-3.169376,6.208631,-5.633958,-9.799441,-0.608506,7.211546,-1.946074,-9.024523,8.123883,-6.761138,7.691710,9.595055,9.219967,-4.500794,8.269569,8.844694],[9.466923,5.141620,0.800804,-6.545941,-8.624859,-9.567087,-5.510371,-0.122138,2.387519,3.545576,-2.154017,-8.765986,-6.007498,-9.388649,-0.011672,1.529005,-3.155772,4.135922,-3.398075,2.806577,2.243774,-9.143148,-9.121776,8.819315,8.577594,5.422750,-8.270298,8.359193,-0.299240,-7.954941,4.465976,-2.873561,-9.764494,7.739921,-5.388190,2.892529,-7.621178,9.796826,-0.655661,-0.614512,3.954011,5.149065,5.527481,-8.320387,-3.880683,-0.842508,-4.255606,-8.322040,-9.317960,-1.637833,-1.144587,3.115672,1.971903,-6.030661,8.294227,0.474648,-9.562264,-7.149538,3.508302,6.984631,1.729755,4.929140,2.004340,-9.112302,8.633648,-5.053896,5.484001,-8.661910,-3.460477,-3.946177,6.953557,-2.602412,4.691257,-9.491469,-2.854071,-6.029718,0.723530,2.161917,7.879176,1.455061,-5.499610,8.590222,6.129333,-7.888499,-4.050971,0.662790,-6.351521,5.692608,9.646323,-4.576509,4.700251,7.880474,-1.165811,8.919712,3.910957,-7.084584,-8.576804,7.503844,1.556348],[0.826488,-5.962517,-5.386729,7.297334,-5.675209,7.076929,-1.706088,-0.128909,2.592216,-3.587051,-2.796180,0.729298,-6.967441,-7.497656,6.761807,8.421313,5.638150,-8.086428,6.734256,1.818502,-3.840864,-2.348392,-4.682858,-5.219775,-3.846483,-4.632553,-6.459083,4.312375,-5.618075,-8.732363,-6.218066,-9.287828,-6.815482,7.375600,-0.749948,0.101978,1.417061,6.065866,-7.199429,8.074198,5.068925,-3.438740,-2.620474,-7.342622,4.655742,-8.444049,-2.781278,-8.894153,8.200709,-3.167792,-5.189651,-6.495991,-7.095281,5.281826,-9.511997,5.659872,5.510555,7.358153,9.717284,-3.437499,2.450089,-2.230432,4.186072,-3.864401,-1.114380,3.206816,-3.865243,-8.966025,8.038321,-0.249654,3.083284,0.714042,3.770888,-6.117983,-1.831884,1.895443,8.980920,-1.827246,-5.218058,-1.850229,7.326662,-9.036015,5.344290,-8.931312,-3.267111,-8.239572,-6.358087,-7.694020,3.876432,8.788570,9.111233,2.504266,-4.448023,-9.818039,-2.261977,-8.904075,-9.843576,2.953112,4.185171],[-0.320063,-2.060196,8.634789,7.798469,-2.165177,-8.421234,-4.414465,3.810715,4.090628,7.205362,-0.140865,-3.733496,-5.748703,6.519586,-1.033743,9.417950,9.058878,-0.363079,0.317657,-2.533151,-5.391167,9.358184,8.514032,-4.446822,-2.894442,-9.251642,6.860498,3.785138,2.124042,3.509381,-4.861821,-9.449271,6.068579,-6.195001,-5.969984,-2.038916,-0.795664,-7.610839,-1.034908,-7.511392,-4.595332,-4.871579,2.688244,8.617284,-6.457736,-5.923042,-1.278061,-4.179043,4.371929,-4.469154,-6.385412,-2.481617,-8.218608,-1.704292,6.016177,8.922396,1.902294,9.375849,-6.055517,0.439456,-7.630395,6.572035,-8.275802,-1.518077,-1.213390,-4.761513,6.535425,3.528761,4.601381,1.509574,-8.901469,-3.176961,-9.315335,-2.881682,8.915994,9.350598,-3.520079,-7.141448,2.641982,-1.448750,5.602131,-5.895862,-9.841194,-2.301635,1.839566,-9.155497,-6.036599,0.913911,5.390517,2.999653,0.276706,-2.470972,0.648933,-3.613237,0.984755,3.949126,8.502526,0.132923,7.363605],[3.540222,4.622246,8.504621,3.143592,-4.616055,-7.337379,3.717676,4.089089,7.163411,-3.605609,9.659074,4.703781,-5.608604,-6.975301,-8.736247,7.916964,-3.337402,1.239830,-5.342132,-4.035829,8.340605,7.655668,-5.270875,-0.958678,7.227289,4.666159,-4.241139,4.925541,-6.907288,3.928227,-4.601279,-4.006707,7.952188,-0.306352,-9.469879,8.322292,3.857300,-3.264815,8.739735,-5.317722,5.549962,5.174970,-7.301393,-5.389395,-2.922764,0.847086,-6.715808,1.476566,9.518334,-7.042371,-3.734966,-2.061655,-1.452185,1.078750,5.252207,-5.353192,8.482235,4.735506,1.562265,-2.871945,3.765177,-4.944179,-9.648749,4.790711,0.708853,8.632459,2.442333,3.759398,2.915896,5.277498,-2.043577,9.743657,0.355977,2.541790,5.190561,-8.689518,5.365516,-2.404826,-9.033065,-0.726278,8.897738,4.219248,0.383933,-3.741192,4.861576,8.142798,-0.636557,-1.647388,2.900900,-3.693711,4.267276,2.681933,1.691015,-2.438418,-7.317949,5.675572,4.194051,-9.556076,4.778960],[7.328171,3.640930,0.793951,5.609235,1.993823,8.303377,4.181508,5.049243,-3.824816,3.592650,-0.774885,1.947609,6.141099,3.875792,8.661500,9.871686,4.316931,1.697161,-3.253286,-1.634965,-2.246728,6.943948,7.750697,-7.375175,8.656081,-6.882125,8.127912,6.196314,-1.361977,1.221332,9.231239,-8.452096,0.486118,8.445068,6.336381,7.424364,-7.789505,9.158547,6.977718,6.736884,1.307419,4.303102,5.276515,-4.685846,8.236460,6.617979,-7.229415,3.789571,3.106879,7.899462,4.335274,-3.704236,0.221095,8.430918,-8.073379,2.555399,-1.094427,-1.143170,3.799713,-2.194269,-0.222747,1.550800,6.758025,-2.770020,-7.016018,6.271925,1.808994,0.297331,-7.621998,3.674207,2.801193,-3.060802,7.117864,1.115337,8.583174,8.256890,8.433019,-4.868094,-5.210112,3.348364,-2.981003,-6.992282,5.157432,-1.206574,-3.508358,-1.112884,-6.842750,0.923130,4.368115,-5.201566,-6.615230,1.198705,5.828837,0.039417,-2.856651,-1.808548,3.211435,-2.253679,-7.809841],[-1.771375,4.226366,-4.414379,-6.427329,5.834542,-6.550193,-9.502152,-6.565880,-1.450574,-7.530367,9.875699,-8.703464,9.006668,-0.237407,-8.153682,0.824616,4.835109,4.799067,-6.139383,9.277334,-9.090881,-4.262137,8.406185,-9.526742,-6.598321,4.724555,8.361179,5.383262,8.812097,3.656394,-5.848424,8.069259,6.145475,7.043439,-3.430880,7.789682,-7.688932,3.870529,-2.533969,8.502780,-3.429150,-0.064262,-5.390034,5.431827,3.962377,-1.344797,8.747182,4.972864,-7.987271,-9.135825,-1.493408,6.178519,1.345181,-8.686108,-9.939347,-8.545992,-8.142270,6.221456,-9.830407,-6.865944,8.989632,9.477219,-9.490634,1.539533,8.314070,2.953153,5.302189,-3.277195,-6.256029,5.969719,-3.891526,1.972050,-6.121993,-0.608056,1.051869,9.291663,6.340305,7.489955,8.224120,-8.515614,5.960791,-6.279139,1.887647,9.805544,5.661123,-1.511548,4.403518,-4.876730,-5.017547,-5.517725,-4.800251,-7.252571,3.456135,4.372927,-2.055093,2.486660,-0.600849,6.205782,2.046329],[9.167137,8.827212,-0.935981,0.891531,-5.160550,3.319204,-6.888714,-0.340249,4.725797,-1.295832,7.366744,1.652256,-4.101037,-2.554642,5.766739,2.212310,8.592791,-0.949421,2.506400,-9.703389,-4.201093,-8.708645,0.661693,8.880451,-1.109731,-4.730432,2.722132,9.780198,9.339940,2.708871,6.367910,4.881852,9.348481,-3.319108,0.028948,-5.384001,0.157652,-3.736706,-5.062124,1.096586,-2.851027,-2.115017,2.825557,6.647991,1.163502,6.165701,6.894273,1.879282,9.517429,0.057634,2.877166,-7.290008,4.698436,9.974572,-1.852710,-2.815111,-0.079343,-4.634425,-0.631688,-9.543130,-8.868562,-6.803664,-3.800337,-0.506395,-8.059829,2.698914,-6.211773,-7.087006,-9.889002,8.112117,-9.917322,6.850895,-6.155743,9.938263,-3.545091,-3.431240,0.191726,-0.873783,4.928453,4.212578,7.120617,1.788123,-7.668168,7.557683,1.274460,-1.987162,-6.468604,0.858301,8.452107,-3.814808,-5.153701,3.228915,6.494988,-7.188958,-6.203258,-5.935991,-8.415798,8.970425,9.039805],[2.769517,7.840881,4.591397,-3.281232,-1.725011,5.349730,7.893100,-4.326667,8.233501,-5.825735,-1.401328,-8.399848,-2.572871,-7.122097,1.233601,-6.662970,-9.270518,-3.568736,-6.428891,-8.359833,3.998502,0.780049,-3.930437,2.624973,2.948023,3.635065,-4.657093,5.622879,-3.124024,9.509369,2.519722,-6.579855,1.389977,8.046523,0.407407,6.431812,0.739846,1.329874,-0.389899,-8.856292,9.175893,7.624809,8.838650,-6.321362,-8.150070,9.475271,-0.100928,2.121237,6.730666,0.442868,8.248462,8.810172,5.631437,-8.296275,3.344225,9.718316,-6.684674,-6.955721,7.886879,4.854639,-5.659130,-2.344636,-6.877756,7.498251,-3.866159,1.834460,1.656925,9.554512,4.340588,-7.250145,-4.992741,0.462071,-5.805482,-3.727178,0.187751,0.570504,-0.774053,-3.721923,0.693091,-0.882933,-9.554224,4.727463,-9.736324,-3.912459,-3.225316,-8.772867,-4.430203,4.345467,-2.818813,2.801648,6.968580,7.467208,-8.689792,2.716773,1.540100,2.024137,7.801226,6.473271,2.520645]], dtype = "float32")#candidate|5879|(11, 99)|const|float32
call_5877 = relay.TupleGetItem(func_2458_call(relay.reshape(call_5868.astype('float32'), [6, 16, 11]), relay.reshape(const_5878.astype('float32'), [135,]), relay.reshape(const_5879.astype('float32'), [1089,]), ), 0)
call_5880 = relay.TupleGetItem(func_2463_call(relay.reshape(call_5868.astype('float32'), [6, 16, 11]), relay.reshape(const_5878.astype('float32'), [135,]), relay.reshape(const_5879.astype('float32'), [1089,]), ), 0)
output = relay.Tuple([call_5849,call_5868,uop_5874,call_5877,const_5878,const_5879,])
output2 = relay.Tuple([call_5850,call_5869,uop_5876,call_5880,const_5878,const_5879,])
func_5883 = relay.Function([], output)
mod['func_5883'] = func_5883
mod = relay.transform.InferType()(mod)
output = func_5883()
func_5884 = relay.Function([], output)
mutated_mod['func_5884'] = func_5884
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5937 = relay.var("var_5937", dtype = "float32", shape = (1, 7, 1))#candidate|5937|(1, 7, 1)|var|float32
uop_5938 = relay.cosh(var_5937.astype('float32')) # shape=(1, 7, 1)
func_5191_call = mod.get_global_var('func_5191')
func_5193_call = mutated_mod.get_global_var('func_5193')
var_5946 = relay.var("var_5946", dtype = "float64", shape = (1, 2))#candidate|5946|(1, 2)|var|float64
call_5945 = relay.TupleGetItem(func_5191_call(relay.reshape(var_5946.astype('float64'), [2, 1, 1])), 0)
call_5947 = relay.TupleGetItem(func_5193_call(relay.reshape(var_5946.astype('float64'), [2, 1, 1])), 0)
output = relay.Tuple([uop_5938,call_5945,var_5946,])
output2 = relay.Tuple([uop_5938,call_5947,var_5946,])
func_5950 = relay.Function([var_5937,var_5946,], output)
mod['func_5950'] = func_5950
mod = relay.transform.InferType()(mod)
mutated_mod['func_5950'] = func_5950
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5950_call = mutated_mod.get_global_var('func_5950')
var_5952 = relay.var("var_5952", dtype = "float32", shape = (1, 7, 1))#candidate|5952|(1, 7, 1)|var|float32
var_5953 = relay.var("var_5953", dtype = "float64", shape = (1, 2))#candidate|5953|(1, 2)|var|float64
call_5951 = func_5950_call(var_5952,var_5953,)
output = call_5951
func_5954 = relay.Function([var_5952,var_5953,], output)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5536_call = mod.get_global_var('func_5536')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_5958 = relay.TupleGetItem(func_5536_call(), 0)
call_5959 = relay.TupleGetItem(func_5538_call(), 0)
uop_5960 = relay.sinh(call_5958.astype('float64')) # shape=(2, 11, 12)
uop_5962 = relay.sinh(call_5959.astype('float64')) # shape=(2, 11, 12)
output = relay.Tuple([uop_5960,])
output2 = relay.Tuple([uop_5962,])
func_5970 = relay.Function([], output)
mod['func_5970'] = func_5970
mod = relay.transform.InferType()(mod)
mutated_mod['func_5970'] = func_5970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5970_call = mutated_mod.get_global_var('func_5970')
call_5971 = func_5970_call()
output = call_5971
func_5972 = relay.Function([], output)
mutated_mod['func_5972'] = func_5972
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_5976 = relay.TupleGetItem(func_2978_call(), 0)
call_5977 = relay.TupleGetItem(func_2980_call(), 0)
output = relay.Tuple([call_5976,])
output2 = relay.Tuple([call_5977,])
func_5990 = relay.Function([], output)
mod['func_5990'] = func_5990
mod = relay.transform.InferType()(mod)
mutated_mod['func_5990'] = func_5990
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mutated_mod.get_global_var('func_5990')
call_5991 = func_5990_call()
output = call_5991
func_5992 = relay.Function([], output)
mutated_mod['func_5992'] = func_5992
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3118_call = mod.get_global_var('func_3118')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_6050 = relay.TupleGetItem(func_3118_call(), 0)
call_6051 = relay.TupleGetItem(func_3119_call(), 0)
func_2225_call = mod.get_global_var('func_2225')
func_2231_call = mutated_mod.get_global_var('func_2231')
const_6085 = relay.const(-5.959453, dtype = "float32")#candidate|6085|()|const|float32
const_6086 = relay.const([-7.818036,-2.235013,9.756890,-9.206147,1.010699,3.056287,6.056895,7.003823,-6.031257,3.625906,-4.760403,-6.667430,6.368416,-4.617647,-4.634543,-5.033077,-1.696527,7.763886,2.887615,-1.091708,-9.286721,9.655279,-0.242703,1.027535,-4.107130,8.960076,6.637241,6.347280,-7.900384,-1.998556,-6.180852,-5.860736,4.339337,-1.330755,8.064436,8.506923,-7.599366,7.566271,6.907606,-3.654735,-7.812561,6.118585,6.617785,-4.909317,-3.968706,-7.789443,3.839326,2.705859,-8.272951,-2.538826,-2.864881,-1.427735,-0.085766,6.309715,-6.475294,-6.862419,6.499047,7.915093,-7.679350,4.772909,-4.770269,4.429420,-1.636065,-7.570185,5.451940,-7.203507,-7.302503,-8.451552,8.043459,0.859517,9.948473,-0.254480,4.570247,1.609749,6.992724,-4.844291,-5.313300,-3.997809,-5.246011,-5.871294,9.878849,-1.992961,6.589434,-6.687410,-6.357299,-5.512719,4.102305,6.592356,-3.356576,-8.794310,2.459033,0.832848,1.256778,-3.423958,-0.328299,6.304551,9.817702,-3.164594,-7.097835,3.120786,-2.829812,3.645146,-4.711766,-4.112203,8.689519,3.299182,9.146523,2.882035,-7.315612,-9.931953,-7.523210,-7.658941,9.263737,-7.738618,7.600753,8.976692,0.458574,-9.185157,4.735401,0.833472,2.571667,7.608940,9.292468,7.861387,-3.393887,8.581212,3.981193,-7.755503,-3.594607,2.042615,5.219345,3.304453,6.151677,-1.763757,-2.212302,9.574965,-0.801817,-3.593822,8.082457,8.532428,4.945035,-3.764665,-2.927859,-5.022891,5.847099,4.237288,-6.312733,-8.801624,-0.924577,-1.428181,-2.850539,-3.944396,-2.915297,-6.798937,2.015161,9.166929,-3.240500,3.508349,-3.103293,3.903855,7.906168,-4.955025,7.775303,4.931287,-6.246042,-1.262944,-9.403334,0.544155,9.203768,-7.742580,-2.587246,-6.239726,-1.214037,1.035347,7.942800,-5.062966,7.504444,-3.763120,5.962550,-4.142986,0.498062,-0.615605,-6.604784,-2.440401,-3.875333,-5.924652,-0.832342,1.889327,-7.780002,7.529836,-3.672139,1.123619,0.154036,-6.187835,7.901110,-0.942293,-9.945513,-9.164911,-9.332488,-3.259583,-6.412339,5.634818,3.180612,1.626983,-4.523210,8.766884,-1.902010,-4.073339,-0.249552,8.157259,-3.760350,-1.078764,-0.071438,2.323579,0.888005,7.008901,-7.602035,-8.537137,-0.323761,9.583805,4.311950,8.441397,4.650304,0.258844,-6.838101,-4.944340,-1.843849,5.488840,7.183042,0.230848,6.739863,-3.327167,-3.851219,8.991692,-3.074911,8.851823,-3.726976,-3.910460,-2.945173,3.035913,-7.779094,6.207324,7.182830,1.462735,8.896005,8.846019,-8.878680,-9.595282,7.622853,2.075637,8.728540,7.654801,3.269413,4.065128,4.883923,-0.791380,-2.410231,-8.975043,5.150416,7.089786,-9.803192,4.860108,-8.689068,9.557245,5.724458,-4.055425,2.979646,-2.745416,0.402386,5.623184,6.851161,-0.583343,9.823006,3.057938,-0.133133,-1.107988,9.940950,2.351797,6.914000,0.916483,4.844304,4.017165,7.659608,0.890095,-3.563167,1.491128,5.891930,6.125783,-0.202861,2.967276,1.856918,-2.978158,4.380839,7.942423,-5.995374,9.328287,-9.213911,1.515292,2.731541,-8.056558,1.721719,2.585000,2.124167,5.332071,1.260635,-2.008418,-0.312106,7.128365,8.986124,4.894323,-0.458789,0.726992,5.701453,-3.578334,-9.699756,-4.332332,9.029822,-4.949300,5.860682,-7.799631,-7.275408,2.028491,7.465599,-1.560093,1.323859,5.780052,-0.192929,-2.161483,1.824394,-7.407235,3.491594,0.577156,-1.545737,6.407802,6.335600,-7.989421,6.709207,8.723889,4.594753,9.010902,3.024222,-9.086457,9.842538,1.324909,0.792674,-2.941228,8.769776,4.920633,8.408030,0.109878,5.486634,-0.718614,6.560538,7.734255,0.544590,-4.576738,5.228182,9.687022,8.232137,2.572788,-1.423382,-2.112954,9.339145,-3.300947,-9.849358,-3.237173,4.216913,-5.870084,-3.333898,3.193832,-4.623534,-0.459881,-1.746646,0.610577,-1.952178,1.386598,-1.882417,-2.970200,0.189316,8.203077,-0.694984,7.656939,-6.736162,1.201893,-1.596609,6.587897,-6.421024,-8.739551,9.272722,-5.033412,0.545328,-4.606402,7.226951,0.533153,2.250615,0.597009,-7.383025,-3.547589,-8.123803,6.154107,-0.733127,-7.712908,-1.490855,-9.098655,-0.427554,-8.748255,-2.587017,3.650505,6.197415,-0.713660,8.348112,6.244391,2.000576,4.132528,0.721984,-0.638958,1.849485,-9.636267,6.549309,0.276539,0.565778,1.682345,-8.199767,-7.868642,-9.075629,2.569773,-4.305640,4.122377,-5.721551,9.591099,-0.401649,1.383720,-3.879040,7.076623,-5.464255,6.877960,-7.880968,5.385714,-1.212847,4.779970,2.384973,-9.782383,9.119055,3.575469,-9.752582,7.091269,-5.185703,-1.408963,-9.371894,-3.341554,-7.410140,-6.954802,9.963988,-5.889842,6.817214,-5.630513,-4.863167,-4.356937,-6.518572,4.600171,4.140669,7.529679,8.232151,-9.172171,-8.122119,4.002551,3.429168,2.155618,4.107389,-5.491571,3.374148,7.803758,2.377464,4.949024,2.365371,1.148937,8.364372,-3.502419,-2.517748,-1.024203,-5.825949,-9.311882,-8.728049,-7.075252,0.795099,-5.895499,6.778055,-0.188721,-5.916105,-8.676923,-9.596907,-0.060811,9.772073,-1.820682,6.258534,-4.448153,-0.837792,7.652162,-1.301210,6.967734,-9.640670,5.909903,7.445469,4.404067,4.415203,-7.121553,5.455543,-6.810076,4.828460,-6.579516,5.509465,-1.490165,2.187821,-9.730071,8.032405,5.474347,-8.980574,6.431235,-0.170963,6.017913,9.168153,2.235168,-4.790455,3.205659,0.007481,-8.736861,-9.376951,-5.446539,6.074328,9.158942,-8.601870,-4.496379,0.950977,6.859513,-0.691062,-4.675483,-2.994826,-4.519439,3.303441,-9.608057,-8.997513,0.966283,-4.305482,-7.659836,2.777476,-2.017128,1.655749,-9.537431,7.363069,-7.696195,-0.975081,1.100533,7.250483,6.032806,2.701382,5.424763,-6.678818,-9.311591,-9.497604,-7.009012,-0.680872,-3.849305,-3.656515,7.944192,-7.480561,0.134830,-8.513195,9.453035,1.237789,-0.252790,-5.589419,-0.192917,-3.814021,4.372433,0.434873,-0.022248,1.791596,0.759084,8.795973,7.010116,8.706275,-7.354189,8.861657,9.922929,-7.307977,3.232528,7.640439,-4.437592,-6.639839,-6.624628,4.209165,6.945952,4.244377,-3.819887,6.131449,-3.877205,6.733852,-7.344295,-1.803705,2.630715,9.235904,-6.134527,-1.610253,5.713714,-6.687972,-3.996005,-4.371350,-0.365434,3.172624,2.695259,-1.632757,7.848118,-1.308141,-0.491687,1.636589,-4.064610,-8.107578,7.805704,5.962578,0.857972,-7.042261,2.824659,-6.868228,8.153971,0.165370,-4.994561,-1.217355,6.838548,-5.658633,-6.095780,4.766327,-0.699833,6.511897,-7.678198,-8.331712,-9.042726,0.875441,-6.105885,-2.794307,4.664935,-7.581810,9.853596,1.446732,3.961855,6.553837,0.110920,-0.392721,-7.083279,1.632325,-9.426199,1.371957,5.628452,6.227918,-3.221116,0.756241,8.124738,5.665234,-3.274906,2.603084,-2.508037,3.280584,8.031304,-0.864257,9.175216,-1.330419,4.252851,1.096385,-6.180775,-8.143888,-8.150994,4.033472,1.557518,-7.896833,5.392556,-8.714925,-9.676591,-6.173092,1.996809,-3.064999,-5.652307,1.286274,-6.669847,-0.091437,3.744721,2.249905,-5.164208,5.741471,4.498637,-7.629775,4.247006,9.045238,-1.155648,3.156039,-2.002254,1.482152,-3.629736,-7.856205,1.054599,6.456408,-1.816420,-3.738751,8.637520,-7.545860,2.762951,-7.736684,8.655125,4.855306,0.427115,-1.190006,-5.482148,-8.115927,-9.654838,5.001513,-8.365891,-4.523478,5.502743,1.627799,-1.343264,0.367652,-2.281881,-4.719985,4.782246,-5.246830,-7.534686,-6.385610,-1.136001,1.174485,-8.474593,-4.089110,3.909436,3.921480,1.497228,-7.439019,-9.224210,9.459216,8.010974,5.965505,1.733364,2.765301,-8.942901,-2.341928,-9.017332,2.403601,-1.082226,3.480365,-5.536304,-9.167861,-1.015080,1.909074,7.709471,5.704023,-3.111266,0.507181,-0.728106,2.647336,1.342067,0.929213,4.622170,-7.684474,-9.155940,9.247845,-3.204544,-6.129926,-7.301045,6.127845,6.192444,-0.332498,8.828650,3.543317,-7.159812,-4.198953,7.848300,-3.655602,-9.168905,-1.194922,-2.792513,1.569515,-4.471928,4.275835,4.700395,-1.101183,-5.615127,-5.333074,-3.711303,2.272811,-0.850175,-9.632989,-9.326588,-7.258980,0.069892,6.548724,2.406037,-4.203268,2.186145,-9.897500,2.869593,3.545356,-4.830217,3.287359,9.438003,9.216481,0.273160,3.716285,-3.586304,-5.941683,4.217862,-1.585724,9.603401,-2.082269,-8.937894,4.929593,2.697477,5.296435,9.031980,-5.296013,-1.976275,-7.424681,-4.684108,7.722727,-2.716734,-3.788041,1.182459,-1.448520,-6.578588,2.820252,5.539876,-2.042787,9.155860,-6.546867,-2.725138,-2.536282,2.686076,-0.883585,-0.936882,-3.125308,-3.023122,-1.743930,0.869070,-1.382969,5.761590,8.842009,-4.215838,1.251202,2.472271,-6.758840,6.832177,-3.270813,-8.049750,-7.072190,-9.667698,4.133249,1.421938,5.070770,-7.357935,-0.856327,8.037460,-8.414284,9.342114,-5.353234,-1.668793,7.147109,6.646881,-1.313974,-1.046486,-2.724667,3.559667,5.478154,-1.446938,-8.111154,-7.381780,-7.504164,-7.250101,-4.422430,0.494952,-6.752569,1.722695,2.517756,-9.095190,-2.276581,-8.191196,6.345098,-5.445369,-8.396344,9.339409,5.209441,-3.242780,-7.770308,4.855695,-5.629017,9.000266,-5.144724,-0.318444,5.622470,8.459823,-0.287972,-3.033782,3.076032,-0.853165,9.353048,-4.159597,-1.374830,5.093188,8.490533,7.895926,1.532754,7.985760,2.641249,6.627945,-8.680876,2.700599,-0.237628,-8.325658,-5.356520,8.000602,2.070407,8.378702,-7.873551,-4.837412,8.887349,-3.140816,-6.712398,-6.335163,7.752087,-4.354711,-1.567086,-4.742876,1.023866,-6.196207,-5.092334,-2.863115,-5.044018,4.546924,-4.717611,-9.103240,5.072508,-0.270742,-0.785105,9.119501,-7.426048,7.121713,3.718104,4.012733,5.605060,2.724551,9.996234,6.894663,7.491691,2.607338,-5.499552,1.013139,-0.964567,9.874110,-1.701590,-1.306117,-7.306332,6.987668,-2.167414,-6.928987,-9.549611,9.908813,1.062561,5.118201,0.101465,-6.745446,3.672382,8.041987,0.425094,-5.301104,5.072084,-7.036825,3.833595,-1.054676,-3.599061,7.111654,-9.809131,1.063681,1.085940,-4.874506,1.568433,-0.359504,-7.387547,-0.914350,-9.474387,4.955179,8.487816,8.625317,1.463589,-4.148498,-0.174126,-7.456693,-0.900265,1.202478,9.906964,-4.406419,-4.364424,6.344239,-3.832510,6.806966,-0.265069,2.264117,-8.877578,-5.280144,-3.246196,-4.296269,-8.325236,5.521233,-9.603122,-0.804313,-5.748881,-5.733222,9.406286,5.130918,8.079751,-1.612226,0.923675,2.682715,-6.989111,4.275440,4.509056,-6.591025,-1.305926,-8.008225,-8.638466,-5.533762,-3.138540,6.508339,-4.057094,5.705910,3.651404,-2.831698,0.548928,6.745395,0.620563,-7.070649,-4.872124,0.500950,-5.424601,7.818869,-8.968636,3.316079,-7.551938,5.666520,9.443159,-5.686176,-9.444697,3.795203,-5.094766,-5.066348,6.793093,-0.172239,4.779444,2.340054,-3.513623,-6.148000,-7.173687,8.367539,-5.782430,-6.776819,8.929368,6.980332,6.791383,-0.558164,9.331043,7.608385,2.708062,-4.100854,3.414808,4.462558,-0.967950,8.211954,9.450913,5.478944,3.210157,-2.387865,-9.480948,-3.862873,-7.049082,2.587059,9.108311,6.404334,3.113247,4.548255,9.342334,-6.505909,-9.757848,-2.783686,-0.215210,-3.005445,8.948692], dtype = "float32")#candidate|6086|(1089,)|const|float32
var_6087 = relay.var("var_6087", dtype = "float32", shape = (132, 12))#candidate|6087|(132, 12)|var|float32
call_6084 = relay.TupleGetItem(func_2225_call(relay.reshape(call_6050.astype('float32'), [6, 16, 11]), relay.reshape(const_6085.astype('float32'), []), relay.reshape(const_6086.astype('float32'), [1089,]), relay.reshape(var_6087.astype('float32'), [132, 12]), ), 7)
call_6088 = relay.TupleGetItem(func_2231_call(relay.reshape(call_6050.astype('float32'), [6, 16, 11]), relay.reshape(const_6085.astype('float32'), []), relay.reshape(const_6086.astype('float32'), [1089,]), relay.reshape(var_6087.astype('float32'), [132, 12]), ), 7)
func_5536_call = mod.get_global_var('func_5536')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_6094 = relay.TupleGetItem(func_5536_call(), 0)
call_6095 = relay.TupleGetItem(func_5538_call(), 0)
output = relay.Tuple([call_6050,call_6084,const_6085,const_6086,var_6087,call_6094,])
output2 = relay.Tuple([call_6051,call_6088,const_6085,const_6086,var_6087,call_6095,])
func_6099 = relay.Function([var_6087,], output)
mod['func_6099'] = func_6099
mod = relay.transform.InferType()(mod)
mutated_mod['func_6099'] = func_6099
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6100 = relay.var("var_6100", dtype = "float32", shape = (132, 12))#candidate|6100|(132, 12)|var|float32
func_6099_call = mutated_mod.get_global_var('func_6099')
call_6101 = func_6099_call(var_6100)
output = call_6101
func_6102 = relay.Function([var_6100], output)
mutated_mod['func_6102'] = func_6102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5778_call = mod.get_global_var('func_5778')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_6129 = relay.TupleGetItem(func_5778_call(), 0)
call_6130 = relay.TupleGetItem(func_5779_call(), 0)
func_3619_call = mod.get_global_var('func_3619')
func_3624_call = mutated_mod.get_global_var('func_3624')
const_6142 = relay.const(9.202210, dtype = "float32")#candidate|6142|()|const|float32
const_6143 = relay.const([3.044149,9.795277,-3.900091,-7.753393,-2.498526,6.055562,2.610247,4.282962,8.358422,-5.350934,-9.249327,-2.409621,-0.464824,3.932432,-4.603456,-3.166594,-1.541641,-6.502850,5.303467,-3.928176,-3.282848,-0.420559,1.891369,4.920486,1.656298,-7.170928,-7.335434,-0.742431,3.648552,-1.032567,7.032034,2.650929,4.518327,-8.201999,-9.357050,-5.203647,-0.765690,3.253365,-9.680099,-1.370067,-8.876141,2.341779,-5.190234,-0.566453,9.266873,6.761276,4.114978,2.919455,-8.058514,8.860168,-6.739648,6.580552,-4.590637,-5.896766,-6.570716,1.352317,4.556120,0.509018,-6.441977,3.961007,-5.077484,-3.357045,-4.764286,-3.920556,3.585806,3.985277,6.776746,-2.449627,7.007922,-7.078484,5.113518,0.504663,6.585867,-0.385868,-8.691934,3.668178,9.341756,-2.690709,0.391506,-2.896010,-3.671526,-9.883735,6.275218,4.859283,7.359231,-0.548361,2.782442,-2.192046,-4.016389,-8.797065,-8.686275,3.819738,1.229175,9.428007,9.330686,7.014088,-3.625353,4.879362,-1.993566,-4.384326,4.391882,6.474580,-2.478067,1.380132,-0.255199,3.703521,0.056931,-3.991792,-3.417872,-5.063102,-0.704896,4.230872,4.719065,-5.231993,-4.167454,-8.264532,7.883536,-3.346895,2.873601,-3.193479,-0.936660,-1.192175,-6.408076,-4.327389,1.993213,-0.530243,7.868951,-6.563093,9.464292,-7.608309,3.702211,3.837009,-0.470354,9.566955,8.297198,-6.942270,7.166041,2.752052,5.366707,9.501093,-2.891152,-4.650688,8.531278,5.941503,6.151918,-9.036701,-8.953448,5.657570,-5.362937,-9.788761,-3.039085,4.669271,5.821364,-0.649097,-0.037737,8.250662,5.881765,-5.149453,-1.396966,8.114653,-5.657625,1.184439,5.599700,6.524199,2.924507,8.702138,-5.256415,0.014012,-9.728377,6.408875,0.591011,4.070575,-0.332679,-0.546260,0.125340,2.593634,7.540396,-8.501257,2.019385,-0.500469,5.273141,4.692031,-8.408626,-6.089711,-9.371476,-6.733033,-0.872242,-0.907615,6.447232,-0.326110,8.809437,-4.706168,-7.528730,8.590329,3.507032,-0.095626,-2.375561,-9.604373,-5.851566,9.603085,-6.994687,7.759560,3.148100,-0.580297,-4.903988,-7.986988,-6.514875,-8.578960,8.766089,-8.522088,-1.274636,-4.087278,-9.290759,8.002271,2.938565,6.246000,-6.242698,-5.071905,5.778353,5.879108,8.778102,2.090210,-1.679671,-0.956613,9.690929,-2.379137,1.940203,-7.407624,-3.707886,6.928716,-9.542012,2.463162,9.824916,9.175432,-4.165613,-4.013652,-1.669576,1.032712,0.088664,-5.126903,2.997847,-2.945634,8.277319,-5.638712,3.438810,7.056249,3.386859,-5.599404,7.990748,1.327820,-5.657803,9.888255,0.307005,-9.060812,2.060043,2.312913,7.655408,1.363476,4.716455,-1.494077,9.225020,-8.848485,7.136386,5.028713,-2.954494,-5.567938,-0.154509,2.275344,9.881534,0.436451,7.792858,5.445488,-9.403452,9.289644,-5.186685,-1.954460,-3.594752,-1.128387,-5.239165,-2.403378,-2.733200,4.909988,-4.361333,-6.669999,-5.401652,-6.664881,8.159017,1.054255,1.092027,3.068267,-7.206405,5.707883,-0.840049,-9.353229,-5.235952,-3.303557,-9.600301,9.393110,-6.941639,-5.164922,9.903330,-9.081338,-2.905072,7.582019,8.545611,9.309973,-5.346149,-6.822739,2.487767,5.871730,5.179757,-4.499625,-1.656043,-1.965651,-2.641672,6.013016,-6.132284,-7.451824,5.774853,-6.170565,-4.391670,5.759256,-6.593116,2.826400,-2.054457,7.792416,-6.446291,8.876080,-5.757721,-1.783464,-3.356841,-1.439619,4.353201,1.932634,-0.898023,1.950548,-8.836373,-3.663237,-9.352835,-9.346075,-7.583085,-3.980929,3.956428,4.721560,-0.659981,-0.046098,-9.451233,6.406278,0.369681,-9.615252,-0.317055,-1.197922,-5.641519,8.002013,9.272838,-3.192361,-6.316974,-0.163632,-5.696364,0.365581,2.008563,-8.654755,-1.329094,-3.525786,-7.788279,-9.121856,-7.217459,2.849670,2.626201,-2.623622,-0.171701,-6.492157,4.188495,8.985263,2.015536,-4.098684,-9.590406,-6.828905,-0.934882,8.279176,1.564720,5.456800,-4.647346,3.003855,-1.541234,-9.492200,-8.113149,4.250079,-0.894594,0.675921,8.780689,-7.906476,-9.988920,-7.530986,7.660802,-9.415163,7.509869,7.283020,-6.748014,1.890588,-8.966895,-6.827511,4.313808,-8.137408,-3.277056,4.276794,-0.805129,7.105870,-5.536640,4.559316,9.205770,-9.573370,-4.315492,4.315445,-0.184448,4.150819,-8.796579,9.188924,0.813747,3.419264,-6.540451,3.576195,4.364048,4.528566,-8.402734,1.623219,-6.446967,9.527129,6.455874,-7.874714,8.311489,-8.850667,2.602902,9.058916,-3.280511,-2.548715,5.095156,3.943136,-5.151582,-1.838285,9.476327,9.740476,-7.141353,-3.264376,2.616401,1.891998,-6.611259,-0.075430,-8.656369,-5.840205,0.844551,3.472144,-2.168068,9.968022,6.179068,-7.347062,5.779024,4.944483,-5.594410,-8.946478,-2.246619,-1.416084,6.115246,-4.542058,5.594076,-7.525733,2.193857,1.867747,-9.135470,-0.279962,5.246765,6.887304,-3.435065,-3.425660,-1.038699,-4.078889,-9.216298,-0.567819,-9.374537,5.094133,9.656184,-3.416930,4.114973,4.110944,-0.877812,-4.526792,-0.622441,-0.412516,-7.959233,5.502973,0.817740,0.935682,-7.498402,-0.324271,-2.113304,-2.959438,3.586455,-6.212081,6.601610,7.790644,7.064122,8.293699,2.367311,7.831512,-0.695160,-1.512957,-9.626688,1.351082,6.520384,7.197442,-8.862497,-9.815166,-6.097243,-4.985999,-9.743032,0.891281,0.764600,5.533873,0.660043,-2.488705,3.278350,6.480756,-5.860832,-9.958278,-1.774476,2.612482,-7.639373,3.990861,-5.092554,-6.052261,6.874360,9.164457,-3.932129,8.071211,8.044595,8.047407,-4.867349,-2.419621,9.015908,0.980782,7.962113,-7.895846,-5.095667,-1.445897,-8.267126,0.943157,0.288593,-6.330740,5.502948,1.297017,-3.746755,7.133312,8.444232,6.805084,-9.361318,4.718269,-8.010714,3.997778,2.782044,5.762720,-4.697167,7.831414,6.125685,7.906746,7.661147,6.746072,3.679410,-5.028528,2.754721,-4.628969,-7.424787,8.055331,9.258493,4.972466,-2.365986,-5.080317,5.815181,-2.922801,-0.043310,8.567456,-9.220716,1.524303,9.458268,0.255592,1.194730,5.986500,3.535084,-2.683800,7.501215,3.522430,0.116951,6.966363,1.580770,0.548882,5.826824,3.387103,-8.170659,-1.078846,-6.412546,-5.808815,2.274226,-0.217695,-7.115844,8.734414,-1.703030,3.514638,2.027948,1.884616,2.659048,-7.642589,3.049933,-6.730065,-6.783688,-5.965043,-5.390588,-6.113284,-5.899605,-2.462435,-1.811635,-4.558647,-0.619732,-6.869380,-8.862513,-1.617986,-9.220417,1.700926,-7.118607,3.981415,-3.340049,-2.993449,-4.409312,-2.459516,6.715769,4.347831,-9.905871,-0.204880,-1.591522,-3.443347,-2.834223,-6.390698,1.734415,9.412352,2.199663,-7.056728,-6.323829,8.216426,-1.181009,5.424503,-9.730959,7.818493,-6.547036,-8.522408,-6.586375,-6.219383,8.448209,6.029709,-2.685186,7.490429,-6.938976,1.433289,-9.813276,2.079500,-4.861066,-6.879184,-2.247661,8.952488,9.515477,4.530296,7.755197,1.187827,-9.332573,5.405633,9.325600,-0.161044,0.451316,-3.253270,-5.042768,-8.194295,-4.669014,-1.961279,-7.546647,2.126816,6.862022,7.041001,-3.934458,5.032825,9.715532,9.140087,5.379414,-9.916820,0.293132,-2.049373,8.300866,-9.568615,8.725383,-6.155950,4.795263,-8.455503,-4.264841,5.059780,-4.884503,2.743382,2.616809,-2.120753,-3.800713,0.042158,8.847285,-2.387719,-5.554349,-3.698677,4.737429,4.769757,-1.075393,0.873804,6.355991,-5.884297,4.268144,-7.029889,-1.424031,-4.023791,2.543270,8.439970,9.855552,2.053405,-5.848270,-6.553319,-1.265436,-7.772851,7.509704,3.620325,-4.496284,-1.078726,0.467842,5.545177,4.620299,8.170107,2.601624,0.584899,-8.254017,4.868968,-1.224959,-3.573922,2.893629,4.179231,-0.637184,-9.790896,-8.469924,-5.598783,8.465991,-0.104916,7.460373,2.151115,-8.183149,-7.085614,-5.742613,1.388987,2.885060,0.437272,4.410284,8.428718,-4.719931,-3.032907,-7.006354,-3.579170,-7.076511,-1.431265,-7.615120,8.817806,-6.235172,4.670659,6.633915,0.149722,-0.442970,5.509252,7.951497,9.217156,-2.078950,3.859244,0.088363,-8.320503,-2.315698,1.864550,4.945887,7.941096,-1.833324,-0.860719,3.600127,-4.351490,-1.656459,0.590133,-7.089982,6.141316,5.043663,8.840910,4.493443,-9.654782,-2.915588,-1.034276,-0.155353,1.688596,1.223870,-1.248153,4.804936,-7.722456,0.814144,-9.674395,5.231862,-2.825913,-8.087338,7.634177,-5.953484,8.114614,2.599256,-4.759188,3.498075,6.283400,3.777079,5.209470,-5.020830,-9.301000,-3.068958,-7.534263,5.927764,-1.703580,-3.381560,6.214064,2.847657,-4.467675,-2.337971,7.307876,-3.043016,-5.351438,-2.612090,6.668789,-6.605308,-8.840359,-0.052195,-4.103093,-9.007293,4.881047,-6.330495,8.230197,6.936315,-7.746098,-2.989061,0.610448,-3.104606,-9.215987,1.910100,-2.791004,1.963924,-8.998592,7.531432,3.743547,9.389111,-0.550868,5.593622,-5.071121,7.425589,1.896022,-5.624023,3.282609,-7.708676,1.258930,4.914980,6.637334,1.254763,-1.815491,-7.931327,-0.398995,-4.373717,7.109559,-9.911063,-7.719068,7.110043,4.379702,-6.023908,-2.228031,-6.817322,-2.071745,7.440315,-6.132782,-0.286071,2.481915,1.191710,-0.762017,1.565598,5.110312,0.679493,3.487245,4.928538,-0.853670,1.270753,0.700123,3.012002,2.451831,2.822332,9.806914,-7.090459,3.816146,-5.067762,3.674257,5.380626,7.494442,-6.194498,2.777704,5.913912,5.390468,0.634432,-2.127551,3.574526,6.154968,2.925665,-2.025363,-0.706671,0.776005,9.676712,-1.778825,-4.572893,-3.299283,-1.366595,-6.189747,4.101319,1.149383,-5.775323,9.051423,2.564013,8.542526,8.267516,7.037021,1.089282,-1.681362,6.193012,0.052442,-2.590410,4.955881,-9.752873,-5.268727,9.099931,-7.345304,2.580287,9.854850,-1.285718,-4.804222,-3.769309,9.682323,-4.522155,1.022920,-1.725870,2.357976,-8.542103,-2.448339,7.475647,-5.929106,-9.356436,-3.555638,5.613157,-9.511584,-0.300438,9.300786,-4.931768,-7.662852,6.593613,4.701866,5.138171,-5.294560,1.613383,-3.626022,-1.225259,0.576322,6.177500,-5.476805,-7.023413,-0.851778,8.905344,2.980575,9.586442,8.359635,4.798109,-1.463047,9.166032,-0.568502,5.771952,8.096391,-2.702879,-5.599561,5.174076,-9.236880,-1.433113,-7.154570,-0.058818,9.743220,-2.542709,-7.427492,4.060963,-4.846795,-9.771741,4.440723,8.740274,9.119580,-4.385953,6.694253,-7.595667,8.285374,-4.565617,2.565100,6.125625,-7.449882,5.357626,-5.378195,-0.871021,1.983396,2.277005,-1.348788,-5.608532,-9.176949,-3.301256,-5.953558,4.708789,3.662946,2.009193,0.855066,0.867239,-5.511217,-3.283875,-6.245852,0.430555,7.327598,-3.011791,2.846895,1.215434,3.714396,0.029164,8.950892,3.911808,1.825388,4.122710,-6.574611,-1.697316,4.571321,4.139802,8.745339,2.435301,1.595743,9.057374,-9.374015,0.973447,-4.743100,2.173535,7.233622,-6.258563,-6.933425,5.325059,-2.972282,7.947513,3.226095,7.476596,-5.346875,2.083220,9.034947,-4.919981,-2.723624,6.207660,3.173302,-4.135174,-3.353041,2.198837,-9.218294,4.348753,-0.932179,-4.324893,5.642555,7.382998,-0.345216,7.556051,0.591974,-7.132921,1.619274,-9.655865,-7.780190,-0.038238,4.289133,2.599581,-7.013424,-5.243589,-1.082958,-7.321333,1.899254,9.940717], dtype = "float32")#candidate|6143|(1089,)|const|float32
call_6141 = relay.TupleGetItem(func_3619_call(relay.reshape(call_6129.astype('float32'), [6, 16, 11]), relay.reshape(const_6142.astype('float32'), []), relay.reshape(const_6143.astype('float32'), [1089, 1]), ), 2)
call_6144 = relay.TupleGetItem(func_3624_call(relay.reshape(call_6129.astype('float32'), [6, 16, 11]), relay.reshape(const_6142.astype('float32'), []), relay.reshape(const_6143.astype('float32'), [1089, 1]), ), 2)
output = relay.Tuple([call_6129,call_6141,const_6142,const_6143,])
output2 = relay.Tuple([call_6130,call_6144,const_6142,const_6143,])
func_6150 = relay.Function([], output)
mod['func_6150'] = func_6150
mod = relay.transform.InferType()(mod)
output = func_6150()
func_6151 = relay.Function([], output)
mutated_mod['func_6151'] = func_6151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6150_call = mod.get_global_var('func_6150')
func_6151_call = mutated_mod.get_global_var('func_6151')
call_6161 = relay.TupleGetItem(func_6150_call(), 0)
call_6162 = relay.TupleGetItem(func_6151_call(), 0)
func_1302_call = mod.get_global_var('func_1302')
func_1305_call = mutated_mod.get_global_var('func_1305')
const_6164 = relay.const([[7.058296,7.337285,-1.545218,-9.099747,1.570709,-1.328749,8.005880,6.695695,3.952405,-4.807116,-9.669762,9.747408,4.685827,-5.126589,4.718634,2.789388,1.280743,-4.405142,8.631852,-1.728802,2.757162,6.234846,6.101146,-2.660251,3.648853,-8.333060,-3.205807,5.927233,-4.615714,-8.782906,-4.415328,-1.934300,-9.629064,2.162285,-0.054480,-0.130605,1.710047,-3.712211,8.191113,8.878369,6.677056,-3.148878,2.512587,-6.599851,-6.103761,7.959200,-8.954019,-8.758203,0.704338,-1.698729,5.537169,5.181184,1.543747,-8.021705,-7.724985,4.070514,1.897078,5.661972,9.812748,-4.660544,-0.230773,-6.298886,5.132158,7.460611,-5.140708,-6.446042,2.192669,-5.574799,8.264677,8.223260,1.279985,-0.818452,-2.856412,8.607165,9.801671,5.513041,-5.310207,-7.448446,-6.465305,-3.454573,-9.768286,0.111619,-6.521123,-4.971848,-4.052801,2.352007,-4.523511,-6.100336,0.839235,-2.376174,2.614258,9.874750,2.520642,6.803156,1.401440,-2.942762,8.038857,3.830626,-7.585968,9.810197,7.618953,-1.572187,-8.187776,7.420920]], dtype = "float64")#candidate|6164|(1, 104)|const|float64
call_6163 = func_1302_call(relay.reshape(const_6164.astype('float64'), [1, 8, 13]))
call_6165 = func_1302_call(relay.reshape(const_6164.astype('float64'), [1, 8, 13]))
bop_6171 = relay.add(const_6164.astype('uint32'), relay.reshape(call_6163.astype('uint32'), relay.shape_of(const_6164))) # shape=(1, 104)
bop_6174 = relay.add(const_6164.astype('uint32'), relay.reshape(call_6165.astype('uint32'), relay.shape_of(const_6164))) # shape=(1, 104)
var_6178 = relay.var("var_6178", dtype = "float32", shape = (6, 16, 11))#candidate|6178|(6, 16, 11)|var|float32
bop_6179 = relay.subtract(call_6161.astype('int64'), relay.reshape(var_6178.astype('int64'), relay.shape_of(call_6161))) # shape=(6, 16, 11)
bop_6182 = relay.subtract(call_6162.astype('int64'), relay.reshape(var_6178.astype('int64'), relay.shape_of(call_6162))) # shape=(6, 16, 11)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_6201 = relay.TupleGetItem(func_1643_call(), 0)
call_6202 = relay.TupleGetItem(func_1644_call(), 0)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
call_6210 = relay.TupleGetItem(func_5376_call(), 2)
call_6211 = relay.TupleGetItem(func_5378_call(), 2)
output = relay.Tuple([bop_6171,bop_6179,call_6201,call_6210,])
output2 = relay.Tuple([bop_6174,bop_6182,call_6202,call_6211,])
func_6216 = relay.Function([var_6178,], output)
mod['func_6216'] = func_6216
mod = relay.transform.InferType()(mod)
mutated_mod['func_6216'] = func_6216
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6217 = relay.var("var_6217", dtype = "float32", shape = (6, 16, 11))#candidate|6217|(6, 16, 11)|var|float32
func_6216_call = mutated_mod.get_global_var('func_6216')
call_6218 = func_6216_call(var_6217)
output = call_6218
func_6219 = relay.Function([var_6217], output)
mutated_mod['func_6219'] = func_6219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_6295 = relay.TupleGetItem(func_1678_call(), 0)
call_6296 = relay.TupleGetItem(func_1679_call(), 0)
output = relay.Tuple([call_6295,])
output2 = relay.Tuple([call_6296,])
func_6302 = relay.Function([], output)
mod['func_6302'] = func_6302
mod = relay.transform.InferType()(mod)
mutated_mod['func_6302'] = func_6302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6302_call = mutated_mod.get_global_var('func_6302')
call_6303 = func_6302_call()
output = call_6303
func_6304 = relay.Function([], output)
mutated_mod['func_6304'] = func_6304
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5883_call = mod.get_global_var('func_5883')
func_5884_call = mutated_mod.get_global_var('func_5884')
call_6400 = relay.TupleGetItem(func_5883_call(), 5)
call_6401 = relay.TupleGetItem(func_5884_call(), 5)
uop_6402 = relay.log(call_6400.astype('float32')) # shape=(11, 99)
uop_6404 = relay.log(call_6401.astype('float32')) # shape=(11, 99)
bop_6409 = relay.logical_xor(uop_6402.astype('uint8'), relay.reshape(call_6400.astype('uint8'), relay.shape_of(uop_6402))) # shape=(11, 99)
bop_6412 = relay.logical_xor(uop_6404.astype('uint8'), relay.reshape(call_6401.astype('uint8'), relay.shape_of(uop_6404))) # shape=(11, 99)
uop_6413 = relay.acosh(uop_6402.astype('float64')) # shape=(11, 99)
uop_6415 = relay.acosh(uop_6404.astype('float64')) # shape=(11, 99)
uop_6421 = relay.tan(uop_6413.astype('float32')) # shape=(11, 99)
uop_6423 = relay.tan(uop_6415.astype('float32')) # shape=(11, 99)
uop_6428 = relay.sqrt(bop_6409.astype('float64')) # shape=(11, 99)
uop_6430 = relay.sqrt(bop_6412.astype('float64')) # shape=(11, 99)
func_5010_call = mod.get_global_var('func_5010')
func_5011_call = mutated_mod.get_global_var('func_5011')
call_6435 = relay.TupleGetItem(func_5010_call(), 1)
call_6436 = relay.TupleGetItem(func_5011_call(), 1)
uop_6441 = relay.acos(uop_6421.astype('float32')) # shape=(11, 99)
uop_6443 = relay.acos(uop_6423.astype('float32')) # shape=(11, 99)
bop_6448 = relay.bitwise_or(uop_6441.astype('int64'), relay.reshape(uop_6413.astype('int64'), relay.shape_of(uop_6441))) # shape=(11, 99)
bop_6451 = relay.bitwise_or(uop_6443.astype('int64'), relay.reshape(uop_6415.astype('int64'), relay.shape_of(uop_6443))) # shape=(11, 99)
bop_6455 = relay.greater_equal(bop_6448.astype('bool'), relay.reshape(uop_6402.astype('bool'), relay.shape_of(bop_6448))) # shape=(11, 99)
bop_6458 = relay.greater_equal(bop_6451.astype('bool'), relay.reshape(uop_6404.astype('bool'), relay.shape_of(bop_6451))) # shape=(11, 99)
bop_6468 = relay.less_equal(uop_6402.astype('bool'), relay.reshape(bop_6448.astype('bool'), relay.shape_of(uop_6402))) # shape=(11, 99)
bop_6471 = relay.less_equal(uop_6404.astype('bool'), relay.reshape(bop_6451.astype('bool'), relay.shape_of(uop_6404))) # shape=(11, 99)
output = relay.Tuple([uop_6428,call_6435,bop_6455,bop_6468,])
output2 = relay.Tuple([uop_6430,call_6436,bop_6458,bop_6471,])
func_6481 = relay.Function([], output)
mod['func_6481'] = func_6481
mod = relay.transform.InferType()(mod)
output = func_6481()
func_6482 = relay.Function([], output)
mutated_mod['func_6482'] = func_6482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3567_call = mod.get_global_var('func_3567')
func_3569_call = mutated_mod.get_global_var('func_3569')
call_6503 = relay.TupleGetItem(func_3567_call(), 4)
call_6504 = relay.TupleGetItem(func_3569_call(), 4)
func_2330_call = mod.get_global_var('func_2330')
func_2333_call = mutated_mod.get_global_var('func_2333')
var_6510 = relay.var("var_6510", dtype = "float32", shape = (135,))#candidate|6510|(135,)|var|float32
call_6509 = func_2330_call(relay.reshape(var_6510.astype('float32'), [5, 3, 9]), relay.reshape(var_6510.astype('float32'), [5, 3, 9]), )
call_6511 = func_2330_call(relay.reshape(var_6510.astype('float32'), [5, 3, 9]), relay.reshape(var_6510.astype('float32'), [5, 3, 9]), )
output = relay.Tuple([call_6503,call_6509,var_6510,])
output2 = relay.Tuple([call_6504,call_6511,var_6510,])
func_6528 = relay.Function([var_6510,], output)
mod['func_6528'] = func_6528
mod = relay.transform.InferType()(mod)
mutated_mod['func_6528'] = func_6528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6529 = relay.var("var_6529", dtype = "float32", shape = (135,))#candidate|6529|(135,)|var|float32
func_6528_call = mutated_mod.get_global_var('func_6528')
call_6530 = func_6528_call(var_6529)
output = call_6530
func_6531 = relay.Function([var_6529], output)
mutated_mod['func_6531'] = func_6531
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4859_call = mod.get_global_var('func_4859')
func_4861_call = mutated_mod.get_global_var('func_4861')
call_6620 = relay.TupleGetItem(func_4859_call(), 0)
call_6621 = relay.TupleGetItem(func_4861_call(), 0)
func_3349_call = mod.get_global_var('func_3349')
func_3351_call = mutated_mod.get_global_var('func_3351')
var_6631 = relay.var("var_6631", dtype = "bool", shape = (264,))#candidate|6631|(264,)|var|bool
call_6630 = relay.TupleGetItem(func_3349_call(relay.reshape(var_6631.astype('bool'), [1, 264])), 4)
call_6632 = relay.TupleGetItem(func_3351_call(relay.reshape(var_6631.astype('bool'), [1, 264])), 4)
uop_6648 = relay.acosh(var_6631.astype('float64')) # shape=(264,)
output = relay.Tuple([call_6620,call_6630,uop_6648,])
output2 = relay.Tuple([call_6621,call_6632,uop_6648,])
func_6650 = relay.Function([var_6631,], output)
mod['func_6650'] = func_6650
mod = relay.transform.InferType()(mod)
var_6651 = relay.var("var_6651", dtype = "bool", shape = (264,))#candidate|6651|(264,)|var|bool
output = func_6650(var_6651)
func_6652 = relay.Function([var_6651], output)
mutated_mod['func_6652'] = func_6652
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4320_call = mod.get_global_var('func_4320')
func_4322_call = mutated_mod.get_global_var('func_4322')
call_6664 = relay.TupleGetItem(func_4320_call(), 0)
call_6665 = relay.TupleGetItem(func_4322_call(), 0)
output = relay.Tuple([call_6664,])
output2 = relay.Tuple([call_6665,])
func_6673 = relay.Function([], output)
mod['func_6673'] = func_6673
mod = relay.transform.InferType()(mod)
output = func_6673()
func_6674 = relay.Function([], output)
mutated_mod['func_6674'] = func_6674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4320_call = mod.get_global_var('func_4320')
func_4322_call = mutated_mod.get_global_var('func_4322')
call_6675 = relay.TupleGetItem(func_4320_call(), 0)
call_6676 = relay.TupleGetItem(func_4322_call(), 0)
output = call_6675
output2 = call_6676
func_6677 = relay.Function([], output)
mod['func_6677'] = func_6677
mod = relay.transform.InferType()(mod)
output = func_6677()
func_6678 = relay.Function([], output)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6715 = relay.var("var_6715", dtype = "float64", shape = (14, 15, 7))#candidate|6715|(14, 15, 7)|var|float64
uop_6716 = relay.log2(var_6715.astype('float64')) # shape=(14, 15, 7)
output = relay.Tuple([uop_6716,])
output2 = relay.Tuple([uop_6716,])
func_6719 = relay.Function([var_6715,], output)
mod['func_6719'] = func_6719
mod = relay.transform.InferType()(mod)
var_6720 = relay.var("var_6720", dtype = "float64", shape = (14, 15, 7))#candidate|6720|(14, 15, 7)|var|float64
output = func_6719(var_6720)
func_6721 = relay.Function([var_6720], output)
mutated_mod['func_6721'] = func_6721
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1678_call = mod.get_global_var('func_1678')
func_1679_call = mutated_mod.get_global_var('func_1679')
call_6726 = relay.TupleGetItem(func_1678_call(), 2)
call_6727 = relay.TupleGetItem(func_1679_call(), 2)
output = relay.Tuple([call_6726,])
output2 = relay.Tuple([call_6727,])
func_6754 = relay.Function([], output)
mod['func_6754'] = func_6754
mod = relay.transform.InferType()(mod)
output = func_6754()
func_6755 = relay.Function([], output)
mutated_mod['func_6755'] = func_6755
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6784 = relay.var("var_6784", dtype = "float32", shape = ())#candidate|6784|()|var|float32
const_6785 = relay.const([[[-2.404381,-9.762623,0.197977,7.727057,9.015278,8.234011,4.279163,-2.677543,-5.360140,-1.556894],[3.127775,8.074431,8.977217,1.213807,-3.809573,-9.793847,2.423205,-9.436806,-5.672902,2.310533]],[[6.936850,0.106873,-3.155862,9.812197,8.423733,-3.728296,-3.291347,0.728836,9.085854,2.282497],[9.782600,0.575493,-6.585662,2.609192,0.810256,9.798569,5.563257,-4.697789,-1.167227,2.146740]],[[6.893999,-5.263699,1.327697,6.526972,-5.415779,-6.461946,-8.538825,-2.873230,2.969694,3.018962],[-3.986106,5.306346,9.656848,-5.614505,0.378781,3.321581,4.602234,0.479859,3.165271,4.532691]],[[2.627779,8.444687,6.901131,2.226530,-9.929177,-3.883899,9.177436,-3.265112,9.544026,-5.581423],[-7.857525,8.101516,5.168876,-6.948228,4.239691,-8.397164,8.935265,0.807234,0.201018,1.662363]],[[4.598461,1.328628,-8.728924,-4.160116,-6.428968,-3.379430,-7.597795,-8.925209,-9.733838,9.603584],[-7.682706,8.147458,9.537167,0.375531,3.334676,-8.966167,-2.217799,5.660480,-5.294608,-0.545992]],[[-7.482517,6.043862,-2.613254,-5.197097,5.424976,-8.632832,5.217218,3.113320,-3.134271,8.488011],[-2.129827,4.900775,8.267846,1.644994,-6.488513,-7.493455,-6.338613,7.758915,6.256785,-1.658698]],[[7.808160,3.551339,-8.131293,-9.608940,6.141415,-7.215139,0.270963,-1.281500,-2.379910,-4.486438],[4.537745,2.975926,4.967566,-1.991776,-6.146215,0.084322,9.391943,-0.354092,4.457277,5.416884]],[[-5.021246,-9.920666,9.708018,6.162327,-3.908893,-5.970453,-2.022482,-0.086687,-2.938107,0.798684],[5.116057,8.538882,9.781060,-1.593587,-2.148282,2.644344,0.271894,-9.175181,-2.823833,-9.438411]],[[-2.731080,-2.141088,-2.114711,-1.493169,3.422791,5.176332,-7.975437,5.328601,-7.457024,-6.103623],[4.997513,4.575379,-4.258051,1.201099,8.972364,7.743341,-0.792070,5.673038,-3.824519,-5.763975]],[[5.144310,-4.096318,-7.066666,6.666046,4.191278,3.577485,2.433927,8.364647,-2.964142,-7.456028],[-4.021372,9.079256,2.444193,6.849625,-4.830147,9.099702,3.959562,1.508299,0.851418,-5.359332]],[[4.863856,-4.442480,1.482441,-7.352556,-2.589394,9.626642,-5.334633,-1.840279,2.389834,-9.325068],[4.359617,0.269182,6.696809,-2.562928,2.050410,-6.518858,-5.700617,6.211902,-5.781382,7.927106]],[[-6.089273,-5.572649,-4.698342,-3.174243,-8.309979,0.188624,-7.164297,4.151965,-1.895077,0.388017],[-4.922972,-2.787063,-6.639131,-4.045595,1.080313,9.323007,2.075337,-3.472568,-7.980355,3.343616]],[[0.819378,-4.608952,-3.954723,-2.448669,1.742617,-1.090345,9.832176,-7.181193,2.464245,-1.486189],[0.600363,-5.483218,3.290834,-3.543396,-7.449669,9.553827,-2.117348,1.288077,5.906023,9.860331]],[[8.207615,-8.021683,-4.433170,-8.656706,-8.876236,-3.710604,3.068966,-2.279181,-4.895750,-3.430564],[-8.600606,-1.334172,-5.571468,3.945605,2.048557,-7.000663,7.492570,3.075992,-1.803565,6.473097]],[[5.920612,-3.333733,-8.936812,3.708947,2.583413,3.484208,1.609003,-2.799761,-2.653309,1.756422],[7.769715,-0.245978,2.447395,-3.147694,-5.538378,-7.595298,-4.323737,-8.980461,0.943194,0.453353]]], dtype = "float32")#candidate|6785|(15, 2, 10)|const|float32
bop_6786 = relay.mod(var_6784.astype('float32'), const_6785.astype('float32')) # shape=(15, 2, 10)
uop_6790 = relay.asinh(bop_6786.astype('float32')) # shape=(15, 2, 10)
func_2813_call = mod.get_global_var('func_2813')
func_2815_call = mutated_mod.get_global_var('func_2815')
call_6803 = relay.TupleGetItem(func_2813_call(relay.reshape(var_6784.astype('bool'), [])), 0)
call_6804 = relay.TupleGetItem(func_2815_call(relay.reshape(var_6784.astype('bool'), [])), 0)
uop_6806 = relay.cos(uop_6790.astype('float64')) # shape=(15, 2, 10)
func_2292_call = mod.get_global_var('func_2292')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_6809 = relay.TupleGetItem(func_2292_call(relay.reshape(call_6803.astype('float32'), [6, 16, 11])), 0)
call_6810 = relay.TupleGetItem(func_2295_call(relay.reshape(call_6803.astype('float32'), [6, 16, 11])), 0)
func_6650_call = mod.get_global_var('func_6650')
func_6652_call = mutated_mod.get_global_var('func_6652')
const_6812 = relay.const([True,True,True,True,False,True,True,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,False,True], dtype = "bool")#candidate|6812|(264,)|const|bool
call_6811 = relay.TupleGetItem(func_6650_call(relay.reshape(const_6812.astype('bool'), [264,])), 2)
call_6813 = relay.TupleGetItem(func_6652_call(relay.reshape(const_6812.astype('bool'), [264,])), 2)
output = relay.Tuple([call_6803,uop_6806,call_6809,call_6811,const_6812,])
output2 = relay.Tuple([call_6804,uop_6806,call_6810,call_6813,const_6812,])
func_6815 = relay.Function([var_6784,], output)
mod['func_6815'] = func_6815
mod = relay.transform.InferType()(mod)
mutated_mod['func_6815'] = func_6815
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6816 = relay.var("var_6816", dtype = "float32", shape = ())#candidate|6816|()|var|float32
func_6815_call = mutated_mod.get_global_var('func_6815')
call_6817 = func_6815_call(var_6816)
output = call_6817
func_6818 = relay.Function([var_6816], output)
mutated_mod['func_6818'] = func_6818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4859_call = mod.get_global_var('func_4859')
func_4861_call = mutated_mod.get_global_var('func_4861')
call_6820 = relay.TupleGetItem(func_4859_call(), 0)
call_6821 = relay.TupleGetItem(func_4861_call(), 0)
var_6823 = relay.var("var_6823", dtype = "float32", shape = (6, 16, 11))#candidate|6823|(6, 16, 11)|var|float32
bop_6824 = relay.bitwise_and(call_6820.astype('int32'), relay.reshape(var_6823.astype('int32'), relay.shape_of(call_6820))) # shape=(6, 16, 11)
bop_6827 = relay.bitwise_and(call_6821.astype('int32'), relay.reshape(var_6823.astype('int32'), relay.shape_of(call_6821))) # shape=(6, 16, 11)
func_5435_call = mod.get_global_var('func_5435')
func_5437_call = mutated_mod.get_global_var('func_5437')
call_6842 = relay.TupleGetItem(func_5435_call(), 0)
call_6843 = relay.TupleGetItem(func_5437_call(), 0)
output = relay.Tuple([bop_6824,call_6842,])
output2 = relay.Tuple([bop_6827,call_6843,])
func_6851 = relay.Function([var_6823,], output)
mod['func_6851'] = func_6851
mod = relay.transform.InferType()(mod)
mutated_mod['func_6851'] = func_6851
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6852 = relay.var("var_6852", dtype = "float32", shape = (6, 16, 11))#candidate|6852|(6, 16, 11)|var|float32
func_6851_call = mutated_mod.get_global_var('func_6851')
call_6853 = func_6851_call(var_6852)
output = call_6853
func_6854 = relay.Function([var_6852], output)
mutated_mod['func_6854'] = func_6854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5536_call = mod.get_global_var('func_5536')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_6897 = relay.TupleGetItem(func_5536_call(), 0)
call_6898 = relay.TupleGetItem(func_5538_call(), 0)
func_6677_call = mod.get_global_var('func_6677')
func_6678_call = mutated_mod.get_global_var('func_6678')
call_6920 = func_6677_call()
call_6921 = func_6677_call()
uop_6938 = relay.sqrt(call_6897.astype('float32')) # shape=(2, 11, 12)
uop_6940 = relay.sqrt(call_6898.astype('float32')) # shape=(2, 11, 12)
func_6150_call = mod.get_global_var('func_6150')
func_6151_call = mutated_mod.get_global_var('func_6151')
call_6943 = relay.TupleGetItem(func_6150_call(), 2)
call_6944 = relay.TupleGetItem(func_6151_call(), 2)
output = relay.Tuple([call_6920,uop_6938,call_6943,])
output2 = relay.Tuple([call_6921,uop_6940,call_6944,])
func_6949 = relay.Function([], output)
mod['func_6949'] = func_6949
mod = relay.transform.InferType()(mod)
mutated_mod['func_6949'] = func_6949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6949_call = mutated_mod.get_global_var('func_6949')
call_6950 = func_6949_call()
output = call_6950
func_6951 = relay.Function([], output)
mutated_mod['func_6951'] = func_6951
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4574_call = mod.get_global_var('func_4574')
func_4576_call = mutated_mod.get_global_var('func_4576')
call_6961 = relay.TupleGetItem(func_4574_call(), 0)
call_6962 = relay.TupleGetItem(func_4576_call(), 0)
func_1813_call = mod.get_global_var('func_1813')
func_1816_call = mutated_mod.get_global_var('func_1816')
const_6976 = relay.const([-9.976043,-6.702805,0.835310,9.770908,9.237723,9.751077,-8.841184,-6.514237,1.699620,4.639950,-2.534203,-9.161450,-5.095585,0.161632,8.606305,-2.134384,8.161356,2.872334,2.348375,-7.866255,-7.022564,3.411184,-4.726313,-1.224583,5.180821,8.378148,8.099555,6.738235,-8.709660,2.796996,3.602779,9.807699,9.206217,3.422801,-6.814986], dtype = "float64")#candidate|6976|(35,)|const|float64
call_6975 = relay.TupleGetItem(func_1813_call(relay.reshape(const_6976.astype('float64'), [7, 5])), 0)
call_6977 = relay.TupleGetItem(func_1816_call(relay.reshape(const_6976.astype('float64'), [7, 5])), 0)
output = relay.Tuple([call_6961,call_6975,const_6976,])
output2 = relay.Tuple([call_6962,call_6977,const_6976,])
func_6984 = relay.Function([], output)
mod['func_6984'] = func_6984
mod = relay.transform.InferType()(mod)
output = func_6984()
func_6985 = relay.Function([], output)
mutated_mod['func_6985'] = func_6985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4227_call = mod.get_global_var('func_4227')
func_4228_call = mutated_mod.get_global_var('func_4228')
call_7001 = func_4227_call()
call_7002 = func_4227_call()
func_5152_call = mod.get_global_var('func_5152')
func_5153_call = mutated_mod.get_global_var('func_5153')
call_7003 = relay.TupleGetItem(func_5152_call(), 0)
call_7004 = relay.TupleGetItem(func_5153_call(), 0)
output = relay.Tuple([call_7001,call_7003,])
output2 = relay.Tuple([call_7002,call_7004,])
func_7014 = relay.Function([], output)
mod['func_7014'] = func_7014
mod = relay.transform.InferType()(mod)
output = func_7014()
func_7015 = relay.Function([], output)
mutated_mod['func_7015'] = func_7015
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4833_call = mod.get_global_var('func_4833')
func_4834_call = mutated_mod.get_global_var('func_4834')
call_7018 = relay.TupleGetItem(func_4833_call(), 2)
call_7019 = relay.TupleGetItem(func_4834_call(), 2)
func_5376_call = mod.get_global_var('func_5376')
func_5378_call = mutated_mod.get_global_var('func_5378')
call_7026 = relay.TupleGetItem(func_5376_call(), 2)
call_7027 = relay.TupleGetItem(func_5378_call(), 2)
output = relay.Tuple([call_7018,call_7026,])
output2 = relay.Tuple([call_7019,call_7027,])
func_7030 = relay.Function([], output)
mod['func_7030'] = func_7030
mod = relay.transform.InferType()(mod)
mutated_mod['func_7030'] = func_7030
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7030_call = mutated_mod.get_global_var('func_7030')
call_7031 = func_7030_call()
output = call_7031
func_7032 = relay.Function([], output)
mutated_mod['func_7032'] = func_7032
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2686_call = mod.get_global_var('func_2686')
func_2687_call = mutated_mod.get_global_var('func_2687')
call_7033 = relay.TupleGetItem(func_2686_call(), 0)
call_7034 = relay.TupleGetItem(func_2687_call(), 0)
output = relay.Tuple([call_7033,])
output2 = relay.Tuple([call_7034,])
func_7050 = relay.Function([], output)
mod['func_7050'] = func_7050
mod = relay.transform.InferType()(mod)
output = func_7050()
func_7051 = relay.Function([], output)
mutated_mod['func_7051'] = func_7051
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mod.get_global_var('func_5990')
func_5992_call = mutated_mod.get_global_var('func_5992')
call_7181 = relay.TupleGetItem(func_5990_call(), 0)
call_7182 = relay.TupleGetItem(func_5992_call(), 0)
output = call_7181
output2 = call_7182
func_7187 = relay.Function([], output)
mod['func_7187'] = func_7187
mod = relay.transform.InferType()(mod)
output = func_7187()
func_7188 = relay.Function([], output)
mutated_mod['func_7188'] = func_7188
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7290 = relay.const([[[7.983139,-9.300815,2.747551,2.998304,1.047323,3.897515,-9.986879,1.598913,-7.046478,7.369936,-6.189495,5.857537,2.563010,-8.902320,-3.852235,8.197114],[4.900569,4.454300,-3.883448,7.341812,5.211472,-5.434410,1.930296,8.194458,-2.585745,-7.096383,-9.346681,4.144357,-5.256514,2.947324,7.539582,7.675227],[-2.199031,-7.081347,6.402557,-5.246325,-6.983488,-8.592552,5.827241,6.047789,-6.412038,-6.396343,1.627756,5.886026,3.922403,-4.462177,6.682627,-7.586330],[0.409047,-8.682359,-5.515120,1.961186,9.851435,-9.200147,5.880248,-8.357840,4.636469,1.881574,2.143362,3.729255,5.875672,9.054907,7.719215,2.499558],[-6.076229,1.366463,-3.879880,8.089595,9.254651,-9.169615,4.336300,-4.968392,-9.882317,6.816589,-1.357461,-6.135892,3.550981,-7.911290,1.411380,5.665474],[-3.107368,-8.316466,5.556401,-9.715086,9.835217,-1.095558,-6.207735,-9.902559,-3.507185,-4.516634,-2.465050,-1.102042,-9.182129,-5.495010,-3.642322,-4.082283],[-2.686211,-1.573868,-3.189980,-7.995493,9.656041,6.162515,-2.654472,-2.604438,2.576070,3.729786,-4.801547,0.501581,9.520585,-8.756715,0.513929,-5.256536],[-0.667155,-3.488246,0.176024,-3.609035,4.526924,-3.931978,8.815050,-9.348036,5.726706,-3.917102,4.677639,1.159481,7.690563,9.263842,-2.469451,6.901893],[-1.826777,9.831624,-0.531048,-9.709071,5.100699,9.355635,-7.213013,-1.032784,-8.529866,0.555704,-2.574416,-7.287961,-4.144587,4.678175,2.488310,0.074924],[-1.669763,0.059073,3.264590,-9.724604,0.716161,9.751996,1.382452,1.369810,0.116547,6.486278,5.091745,5.673668,1.009408,-0.854114,2.324001,-4.598874],[8.759580,1.759263,-0.883249,4.565826,2.975936,8.047670,-4.998358,-5.279808,8.446336,-5.377036,3.297867,-3.715484,-8.734373,6.487233,6.671000,8.004569]],[[-5.729230,6.952635,-1.693551,-6.027773,6.998776,-3.107935,-4.667398,8.492712,-1.689012,9.182498,-5.131649,1.146733,-1.198908,-3.563122,-1.642649,-3.281139],[-0.345624,2.313537,3.482839,6.467702,4.018913,-9.090441,-3.639646,4.886343,8.631126,4.692594,4.246764,-7.538044,3.197044,8.156115,-2.880896,-8.741780],[4.617699,6.675404,5.427051,4.878928,-8.465149,7.528543,-4.947531,-1.801513,3.367281,1.698993,-6.053694,-1.040711,-8.053223,8.295071,-5.771619,-3.147165],[-3.290732,-6.582842,-8.170649,-2.816793,8.934565,2.209506,9.980860,-7.189647,3.281355,1.286574,4.072922,-8.136052,9.027245,9.103906,7.400596,1.198212],[7.671164,-9.522094,9.036252,6.622398,-0.161274,-9.901390,-3.194990,-6.613682,-3.560850,6.028289,5.765587,-1.159673,2.373436,-1.995511,2.354986,-2.250214],[4.137783,-2.240741,-1.930648,-8.050612,-0.759163,-6.360450,1.946606,1.753981,-1.071355,9.961261,-9.539077,-4.697081,1.895719,-2.411964,-4.827135,-8.587814],[3.227539,-8.520865,-8.556618,-2.206706,-0.361386,4.392649,7.396029,3.564613,7.631168,-0.294241,-8.071411,3.245236,6.399335,-8.408348,8.478275,-0.921635],[0.715221,-1.106158,1.136588,4.003630,4.605453,1.955466,1.297182,-3.175360,3.676631,-8.652322,4.217513,-3.730052,4.996110,-0.349124,6.768584,-9.613526],[6.691373,-5.130507,6.498448,-0.780559,-0.028158,-3.244297,8.048356,-5.869777,1.002725,-1.802165,-3.876038,9.904923,-0.779783,-0.277738,-6.469160,-5.383540],[2.604112,-5.560300,-0.754214,4.423347,-8.857177,-3.793222,-0.444678,5.823566,7.411773,-3.510893,-4.917028,-1.514404,8.256919,-8.416721,1.670559,-7.731561],[5.579787,5.929950,7.872807,-2.351931,-6.423108,6.618080,0.017783,-2.880528,1.812585,-9.699814,8.370697,-2.803294,-3.763565,-1.829339,1.715847,-9.328002]],[[-4.479218,9.803499,7.816359,5.779205,-5.682533,-7.796448,0.917894,9.048209,-5.943346,-1.133850,-7.419913,-0.224573,2.722989,-1.648081,4.543600,0.015632],[-1.006520,-4.399078,-0.727008,-0.833265,-3.338848,-3.551664,6.776667,-8.623597,-7.668333,2.429397,4.023740,3.056036,3.455955,-0.946973,-6.175972,-7.622494],[-0.275072,-4.915315,-7.902020,5.037059,-0.351894,0.419316,6.969860,4.897651,-4.366114,-5.523474,-8.067735,8.696745,2.737927,8.015395,4.639821,3.920485],[-5.595297,2.335583,-0.467410,2.590266,-2.909338,-6.756449,0.359503,0.773640,6.201090,4.789028,4.906801,2.414349,-0.105429,0.879947,-0.032372,3.819332],[-6.471925,8.982955,-7.776589,7.948899,6.397372,-6.710492,5.920856,9.554652,-1.984692,9.929429,0.332893,-3.619919,9.438612,5.930564,-5.661573,-0.417880],[7.553732,6.391405,-2.668211,2.433322,5.669437,-4.121279,9.058588,4.656368,6.961741,-6.372330,0.744816,-4.307497,-5.846432,-8.422333,5.658931,9.932642],[-8.344220,-1.999317,-5.863953,5.210628,3.953413,-3.798843,8.084471,-2.212146,-4.718635,0.080041,-1.809936,-8.969849,4.318454,2.474407,5.126665,-4.176120],[-3.436908,6.434640,-7.553971,-2.236332,-4.159483,-0.254776,-8.245540,-0.304789,5.323158,-0.113030,-1.156188,-6.945596,2.459769,-1.295347,1.148137,-6.268655],[3.610005,-7.573691,-0.270554,1.928786,5.370267,-9.700739,1.144335,3.071867,-5.327743,-3.963990,-2.610212,3.507654,-9.974720,5.611755,-5.746806,6.371871],[6.831643,0.434900,-6.355029,-0.373198,-4.375023,4.161654,-7.457410,3.901616,-2.605356,5.005827,-7.668215,-1.919718,-1.481084,-5.737979,-0.795550,-4.475331],[3.140269,1.492664,-8.194425,-3.345847,4.536621,-9.418510,-1.187457,-1.842330,2.047199,4.802904,-3.594295,8.944225,2.048051,1.695135,4.882837,0.254938]],[[0.492786,7.124531,1.317453,9.709518,8.968918,-5.054214,4.319655,9.472485,-2.928147,-4.133262,-8.936663,8.997466,-1.558457,9.889524,-0.170152,-3.356444],[-0.758340,9.924254,2.997917,-9.978453,7.706408,-9.485195,1.164321,6.673268,6.577347,9.794238,5.326901,1.387460,7.339446,-3.819899,-0.295403,-3.818987],[-7.351057,-3.330391,-8.914242,-2.047713,3.567325,-5.032663,-3.648209,-2.878665,0.709651,-0.658757,-1.825228,-8.372901,-3.838675,4.745002,-4.434178,1.133206],[5.652453,-8.205175,-7.232989,7.707012,-0.055772,3.367795,-5.462551,-4.732087,4.573553,-3.032824,-4.923570,9.563540,1.712735,6.714544,-1.148403,-1.420001],[-9.444964,4.007022,-3.103433,-4.982303,-1.305590,9.388534,1.573349,4.989951,-0.681697,-0.914383,-9.606210,-5.483437,-4.126359,1.923755,-1.400913,8.638547],[0.282310,-1.934023,5.081537,-0.352195,-8.766914,-0.612610,6.188500,-7.731299,-3.009975,-9.906627,-0.898195,-5.345673,4.997585,-5.387517,-9.939455,-0.460686],[-4.274830,6.403981,-4.359211,-6.505321,2.075015,-4.563701,-9.173218,9.463460,-4.835241,5.635758,-2.060005,2.647269,-0.874863,4.680967,7.154275,-7.119882],[-7.517394,-4.833007,2.868342,3.384002,7.059823,7.248410,-9.877947,-1.945492,-1.315349,-9.719026,-5.263020,-5.800766,7.734887,1.202221,-6.589955,-2.044739],[4.214242,1.994412,0.541432,1.631908,-8.637501,-5.740953,0.473768,1.475716,0.093506,-0.260477,-3.376606,-3.032732,2.609966,-6.335704,0.174037,-7.693702],[4.795109,9.229388,0.092365,-0.826095,8.501642,-4.497097,3.553112,-8.701442,7.163903,-0.836931,-4.258839,3.365400,-9.142278,7.246582,0.096537,-1.099239],[7.194555,7.793220,9.098330,-3.510600,6.785563,0.434755,9.962660,7.788509,8.172888,-7.169168,-7.699045,8.971745,6.524837,-8.589579,-1.926806,-7.494520]],[[-0.952546,-5.274299,9.250298,-9.499107,-2.985881,1.446830,2.465602,-1.702489,4.260834,-5.270963,0.727875,-8.642711,-0.348143,0.024240,-5.757184,-4.912383],[3.816910,-7.615011,-2.575100,5.963704,-3.143934,-1.698158,1.262261,-1.933271,5.786938,-8.052496,-0.066204,7.446389,5.854262,-6.445389,-2.948832,-8.247906],[5.861281,-4.827056,0.851067,-4.010883,6.904757,-8.610333,-7.721305,5.836001,2.005778,-2.627520,-7.457229,0.019308,-3.616845,2.177456,-8.787034,-9.749445],[-2.946410,4.239221,6.407177,-2.676220,-1.755363,5.208369,9.675858,-2.245995,2.428811,8.554157,3.455825,5.869905,-7.996997,-2.808622,7.260630,-5.040056],[-5.110146,9.801294,-2.820675,-0.021008,-5.418459,5.418222,-4.731397,7.990666,-7.478967,3.965646,3.794966,7.098068,-8.697437,-3.741078,-5.057173,1.684128],[8.500155,-9.377881,-4.129552,-0.811698,2.478392,3.171220,-3.764780,4.770927,9.257596,-0.172229,3.995778,-2.175711,8.253346,2.553574,5.000469,-7.721761],[-4.264763,-5.422740,6.097089,1.563388,-4.264426,-1.801438,1.178908,1.946744,8.782947,7.058539,8.826399,-9.811613,4.745289,3.490208,-6.801372,2.143965],[-9.771711,-9.779182,-9.526583,-5.361906,-5.592575,4.262394,-9.282980,-1.482768,-4.768648,2.030956,2.804624,1.862597,4.744235,4.282690,-4.120854,-0.584245],[0.543917,7.365385,5.072095,-0.541221,-1.595083,2.353226,8.538897,-8.091576,-4.427639,6.429836,9.431756,-2.650363,7.886657,7.938038,-4.930436,2.807994],[-2.364450,7.548021,-8.350334,4.588536,-2.356196,-6.599115,-8.762353,1.394117,-1.830300,-4.672212,5.177693,-4.122501,-6.845719,4.484492,-9.334647,-5.849198],[3.216521,-6.160898,-8.162498,-0.838830,-8.583101,-1.226662,-0.574484,9.828412,-1.712043,-0.966296,-8.840514,3.559185,-1.674542,5.354414,4.822498,1.760138]],[[-7.791666,-3.701985,4.360465,7.040380,8.632164,-9.332831,6.953322,-1.993056,1.915090,-6.039579,-2.761745,6.179381,-9.613292,5.003963,-4.594650,-9.801326],[-8.120618,2.464713,3.866672,5.233021,-5.100616,-2.236074,-2.157554,-3.716246,-3.913350,0.337353,-6.440154,0.370791,-1.483151,-1.466096,-3.897299,8.790183],[7.388897,-9.539744,7.553488,-1.949240,-2.415214,7.620544,8.627487,-1.497128,-0.498788,-1.139309,-0.814481,2.181327,-7.250854,-3.138044,-8.945330,0.495075],[-8.621249,3.768826,-7.322883,-1.089339,-6.393159,8.138888,6.738127,4.272024,8.214563,-8.724889,-5.329406,-0.741592,5.440439,5.581610,-4.675220,9.780700],[-1.557914,-9.286348,-8.401810,3.293769,8.524507,9.268101,7.323399,-3.615137,-3.258999,-1.536639,9.514737,-9.450898,6.988404,-1.730910,-3.834278,0.402796],[-6.052424,3.486152,-8.315436,-9.160018,7.938389,-3.341219,-0.924148,-7.466447,4.849255,0.217316,7.077769,0.942716,8.469268,8.002530,1.307463,2.530065],[-6.353429,6.387525,9.518809,-8.663440,4.074469,7.075888,-5.206383,-4.963991,2.979033,-5.301639,1.824533,8.383932,5.466166,6.244700,2.624625,9.609949],[0.094833,-6.167655,-4.566513,-8.699963,2.177499,8.823818,3.953674,2.740771,-1.639315,8.605613,0.072973,-6.666699,2.352884,-7.628150,-2.511230,1.040597],[-7.967658,1.982152,-6.715846,-4.713924,0.551456,2.796341,8.964278,7.831262,-2.220485,-7.871314,-6.407376,3.693519,-6.116682,-6.150656,0.639993,-6.520109],[-1.275554,-2.978238,9.844529,-0.963644,-3.640880,6.045240,5.760787,3.828711,-2.285845,3.128944,9.526784,-0.620758,-4.478398,-1.079283,-0.913742,4.071537],[-9.940187,-7.583447,-4.416058,6.228654,-8.419770,6.676029,8.839934,-3.318584,-1.137434,-1.453814,-1.450961,0.899809,-0.781995,-6.816012,-9.490791,1.710626]],[[9.267939,3.410648,-2.435124,-8.526743,0.621318,-2.816426,9.739214,-1.050692,4.603584,2.274614,-8.836668,-8.598656,-4.125320,2.849394,5.355233,-1.735649],[-5.706161,-9.363668,-7.906567,-6.966045,-2.241439,-9.575949,5.111731,8.003424,-9.994353,-6.840008,1.190203,1.613951,0.284948,7.812360,3.527656,5.412068],[5.137891,-8.925809,-1.688728,4.179976,-9.620513,-9.772120,4.530700,-5.100766,-8.614293,-7.140837,1.623191,-7.236934,-8.334786,5.959521,2.713619,-5.100127],[7.567085,-6.305134,5.596112,-9.191264,9.637187,3.455013,8.042650,-4.418984,-0.105846,6.677103,-8.966625,-0.196339,4.916556,-1.286925,-9.350480,4.117473],[-6.979929,9.406580,-2.918312,0.072200,6.361239,-2.849373,-8.558489,-2.084611,2.149851,-8.234443,0.070941,-8.054959,1.035721,6.474414,8.763231,8.648544],[-3.015462,6.690519,-0.574056,0.753798,0.311151,-6.691287,-0.306823,-9.180092,3.451138,-4.289627,3.908091,6.547261,1.174330,-1.195048,-2.852298,-0.760844],[6.554493,2.052211,-5.056339,1.657346,-8.845856,6.806548,-5.667202,-3.514357,8.379361,6.038980,3.311120,9.929965,5.226387,-5.602907,0.166585,3.788256],[-0.063036,-9.058871,3.491900,1.741800,-6.132155,-1.771274,-7.184212,-7.779975,6.658193,2.173063,-2.088262,-6.088247,-2.954738,6.480009,3.765585,-6.268056],[7.845267,0.053094,-2.298499,-7.202380,3.268654,-9.448314,4.195936,3.266075,-2.533237,-2.241402,8.365317,-6.918900,8.479813,8.212200,-5.222749,-1.589078],[9.472300,-0.282225,-4.758246,-4.839185,-7.827894,-9.629839,9.105084,-5.625666,-4.272965,-1.784883,5.794786,7.095156,2.109978,-5.604153,9.805927,8.588654],[-6.018820,-6.274356,0.648186,-4.236025,9.032712,5.369473,4.228604,-0.890205,-6.591881,5.916589,-3.797285,-9.254531,-8.741253,9.083316,-9.220328,-4.731927]],[[3.123002,3.479563,3.674334,-9.423488,-6.608607,7.742665,4.197371,5.652821,-8.947244,-1.096186,-7.835742,-1.667350,4.428484,-9.080317,1.774648,-2.631306],[2.695503,2.610247,9.326215,-0.296953,6.436459,9.504721,5.637678,4.295334,-5.742779,-2.463748,-4.597698,0.284568,1.955537,4.864792,-8.055068,3.384445],[-6.617860,-1.914421,-5.638964,4.209502,-8.577713,-5.715518,-2.241029,9.103139,4.767239,8.018911,4.561448,2.400039,-4.164488,1.740575,-8.813432,-3.872478],[0.240732,9.933254,2.402049,3.175673,7.033083,-8.892404,8.976956,-4.441124,5.604440,0.798645,-0.530114,1.951630,0.340643,2.469065,3.314672,-2.415335],[-1.579893,-3.502956,1.987741,4.268608,-3.184493,-7.992685,-8.424705,-8.900789,-0.151981,-9.959552,0.433831,3.108376,-5.769114,-9.633941,-3.149715,-6.208709],[-8.683026,9.584694,-7.988350,7.769832,-8.195080,4.441704,-7.027253,-1.208425,9.996724,-3.662009,5.397695,8.020218,-2.985470,1.311839,9.577203,-3.935190],[7.979947,4.622616,-9.574352,-8.423348,-1.815824,6.249456,8.299406,5.907101,-2.325322,8.321772,1.765552,4.080233,2.904734,-1.575509,-7.925470,-1.249169],[-3.470520,-4.933043,-3.133362,9.370989,-4.252078,-7.789491,9.891270,-9.242697,7.646550,6.573361,-3.029208,-8.114625,8.828223,-8.923298,3.573188,7.134788],[-0.378829,4.501806,-3.275391,3.083997,7.462916,7.676087,1.571455,4.086137,6.331459,6.985996,1.460560,5.270164,1.888114,7.082452,0.239098,-1.300435],[-1.664813,-7.712726,5.219860,8.197482,2.327939,7.501731,-6.843322,8.057724,9.245660,6.471352,6.369786,2.357610,2.717820,9.737291,-3.487232,-6.730026],[5.546499,3.380571,9.471814,-1.770765,0.048572,6.433826,-7.845013,-8.131732,-8.794983,-1.797942,-0.789503,-5.122545,-2.380110,-6.000530,7.401053,0.820082]],[[-7.495335,5.789048,2.306805,-1.018331,7.045700,-1.928775,3.815900,9.396147,4.792632,5.829765,-2.745267,9.070846,6.704415,7.895659,-0.649956,-2.126762],[4.185522,-2.436957,2.048877,-7.603900,6.826301,-5.832516,2.887335,-6.443394,2.195634,-3.531867,3.784535,1.283098,-5.062289,1.323396,9.070697,1.428355],[-2.732331,-7.785167,-0.770466,-1.593481,9.704082,-7.685616,6.847478,2.493240,-2.140115,-6.380186,7.528095,0.634243,-3.895703,8.085915,-7.680053,-5.190807],[-6.837762,-4.633494,0.074494,-9.144751,9.134640,8.721381,3.343087,8.881249,0.119838,6.591345,0.725203,-0.228245,-9.067543,-4.208455,-8.244367,9.554357],[4.178254,8.852294,-9.514019,8.787646,0.879289,-7.206391,-5.704804,-1.750340,4.362709,-7.655243,-9.549683,-2.369208,-4.692943,3.303986,-2.915997,-1.847468],[-6.424516,-4.840139,6.430413,-7.830588,9.438589,-8.603014,0.373713,4.900725,-1.566125,5.809747,-7.596560,2.140631,-4.493829,6.294337,0.652780,-1.463814],[2.156604,1.711384,4.097927,2.804594,-7.569531,-8.053734,4.820107,1.624914,5.256158,-7.957977,-8.437651,5.725956,1.464449,5.434299,-5.884198,-7.368725],[9.231018,-3.720606,-0.981098,0.182639,2.771860,-1.408238,8.484805,7.514640,-8.940898,-3.246112,4.701645,-0.628003,-6.577283,-8.467550,6.910117,-9.253859],[-9.124317,4.420375,1.710982,6.369983,-3.769595,9.981202,0.878712,0.171517,-8.640098,0.621783,2.977943,-5.590437,5.590456,-9.054553,-2.065287,8.757043],[6.190304,7.260987,2.457664,-1.558563,-9.210301,8.891775,-4.201345,9.003103,-1.431323,-9.973436,-6.871870,5.033960,5.399228,6.254683,3.298342,-2.194719],[7.814968,3.695347,1.891602,0.923959,1.220853,9.962859,7.225778,-1.904336,9.733860,3.646909,-9.791507,-4.532740,-4.712999,6.832179,-3.456016,-5.707212]],[[6.162562,3.333255,6.001421,-1.242247,4.531743,-2.573092,-3.411637,5.442280,-9.372209,-6.103539,6.232123,-7.094499,-3.266323,3.612333,-4.220244,-2.656134],[1.888430,-7.811746,-3.143891,6.086785,-0.293746,-6.906859,6.011095,7.418643,-3.327064,-2.786443,-6.048179,8.482445,-6.010161,3.303318,3.573572,-4.036465],[3.159098,5.761274,3.650129,-1.992266,5.702069,-8.838160,-3.723228,-1.454631,5.999550,-6.413837,8.356218,-2.673598,4.973431,-5.733252,-8.988527,3.853394],[2.291791,1.625739,-5.341629,5.456560,2.483763,-5.883199,8.348337,-5.143392,7.934521,-5.305993,4.580283,-2.571821,-4.070035,2.201483,0.860150,9.458301],[4.159401,9.170587,-0.703450,5.083033,-7.198291,3.014997,-6.172011,6.545478,-0.069340,1.843903,-5.887072,-2.244401,-8.237307,6.999330,9.128754,9.763628],[-0.206859,-8.371657,9.486071,-5.510539,8.998910,3.004079,5.185587,4.149642,-8.279293,5.881814,-8.270885,8.272353,7.762342,-8.356374,3.568214,-0.562152],[-3.789412,-2.763467,-3.969272,1.441791,-8.362446,-8.863554,1.905594,-2.559092,-9.049274,0.980752,0.764914,5.663054,4.776897,5.849587,8.024653,-1.930558],[-3.983707,8.154774,4.706439,-9.166633,1.539180,-0.703546,-4.351228,-7.037352,-5.606740,2.459329,4.808772,8.066164,-4.916321,4.184452,-7.266310,4.712772],[5.902481,5.216521,-4.009712,-7.981477,-7.869503,-0.422770,4.059355,5.202055,-0.613043,-3.632450,-4.100290,6.187528,-8.993086,-4.659724,-0.618185,-7.830619],[6.249901,1.794329,3.643630,5.426555,-6.466584,1.020839,9.217822,3.058059,6.299147,0.449754,2.794156,9.493088,4.594123,-8.338978,4.020161,4.319940],[9.503211,-9.380902,5.615561,-6.404415,-0.554191,6.798516,2.166006,2.553433,-5.158842,-1.402582,7.601624,-6.325584,4.008683,5.216596,4.782595,7.126433]],[[9.843556,5.768974,-2.907465,-7.174687,7.152561,-2.186397,-8.326436,-5.318138,-3.453159,1.655679,-0.291076,-8.321380,-3.026620,-8.688572,0.711522,-1.648159],[-4.266812,2.258203,-4.194370,8.552314,9.369029,-4.240340,7.781493,2.655942,1.834067,-5.134186,-3.855434,9.677371,-9.072168,-2.734709,-1.470657,-1.573500],[-1.344362,4.874124,7.182136,0.680596,-7.040248,-7.214161,-5.643756,9.923178,-4.799861,0.200801,-7.753177,-2.882610,-9.699753,-2.245362,6.562865,5.836015],[-4.230508,-5.094427,2.242355,9.404052,8.090073,-6.128049,4.565039,4.263714,4.426240,-3.540381,-7.785493,-6.218666,1.411592,3.945285,6.947548,-9.423329],[5.109024,0.015405,-3.883423,-3.215527,-0.793415,8.312682,-7.712558,-3.227713,6.068033,2.284186,6.881167,1.275461,6.917085,3.493931,7.062594,-1.079473],[1.229959,-4.942351,-1.334485,3.184863,7.884605,-0.319108,-8.628047,1.600369,3.773056,0.232211,-4.373375,5.341598,8.035113,-8.929410,2.573582,5.367279],[-1.595985,-2.521163,-3.670801,7.492615,6.674890,0.692695,-5.970246,1.395765,6.417361,-1.012314,9.836314,0.006996,6.448779,-8.849266,4.272428,0.698301],[0.276669,-9.249108,0.266020,0.239153,-1.869948,-2.212962,1.282794,-6.691213,-4.668866,-8.094612,7.311420,-1.017483,1.614831,5.722118,-6.940495,-7.857474],[-9.827345,8.727408,-6.884160,-4.240708,1.968049,-8.403842,4.197082,-8.509798,0.982126,7.891493,-4.367747,5.592180,-6.888349,-8.311380,5.209974,-7.191109],[-0.500528,-1.723969,-5.800245,4.471373,1.011866,-2.207209,-2.109677,3.308538,4.964353,-4.570831,-3.516820,0.420899,-7.034544,-4.814367,-1.311395,-4.557004],[-0.507928,-1.189071,3.298593,7.095870,5.760102,1.017231,-4.675293,8.864343,-9.065444,5.004722,-0.258839,8.410064,5.407880,-6.423862,0.200361,-8.792873]],[[7.158220,-0.706197,-5.677546,-6.600134,-1.732136,9.520245,-6.906108,-8.615659,8.354165,5.885336,4.979003,-9.402602,-1.862190,-4.915160,8.823624,-1.877172],[7.805578,-4.807794,-9.464790,0.018919,-2.897138,7.778549,-0.867690,6.238845,4.698645,4.582938,-7.780551,8.881330,-1.944105,-7.080210,-8.839584,8.591383],[1.881471,1.677734,-1.669522,-4.879842,-5.442057,0.536597,-2.066462,-4.821360,1.238264,-9.487258,4.952863,8.388641,8.204905,-7.054583,-3.954005,-9.732849],[3.703451,2.834151,-6.465696,-1.177690,3.009258,1.879088,6.569719,8.905413,2.616316,-6.651296,-6.038364,5.704839,1.018182,9.740365,4.363414,8.237381],[-1.500006,-1.623919,9.234473,8.688661,-7.574462,-1.593562,-3.814174,-5.126032,7.901869,-8.383724,-4.293939,8.236496,3.897029,8.060971,-1.323657,2.713045],[6.641403,-7.897882,6.399989,9.505266,-7.836307,6.415835,-6.541500,9.742523,-1.383192,3.191678,4.058485,-3.834560,9.528145,8.428085,-5.237183,-8.000606],[-9.765586,-6.108986,-6.172729,8.204277,8.665121,9.739800,-3.820614,5.474248,7.148343,-1.700221,-0.626303,3.517728,-6.462981,4.045257,-9.368312,1.017540],[-9.532483,-7.910991,1.029177,-2.749919,-7.340440,-7.762949,-1.492768,0.579533,-7.708064,-1.769691,-4.301544,5.149210,-3.162441,0.249437,-7.764159,3.518782],[5.422370,-1.030518,4.051307,7.751532,-5.789860,-1.795962,-7.225906,-4.359594,2.967740,2.974797,5.487290,4.485394,4.474865,-4.738268,6.573980,9.480109],[1.413510,8.060121,-3.212688,-2.468982,5.570506,9.926650,-6.290414,-6.626061,-1.154795,7.260187,-0.486489,5.967728,2.357088,-6.615837,8.822977,5.560505],[3.171592,1.379733,-0.058886,-0.638138,-5.775046,7.955756,-5.372264,3.341004,0.840081,-8.763169,5.620533,4.353611,0.046264,3.928792,0.608175,4.505051]],[[7.524808,-4.951973,-9.559922,7.597357,-7.254691,2.327011,4.204314,6.005074,0.945511,-2.723803,3.830189,5.197650,6.389078,8.407935,-4.867129,8.687043],[0.249334,9.360592,8.840472,6.871486,3.499849,-0.655196,7.184167,6.171590,8.990041,4.422417,6.526358,9.815654,1.275702,-8.267083,4.286779,5.009039],[8.703329,-0.718895,-7.941882,1.394515,-4.181843,-4.392653,8.567512,-5.218554,8.275180,-9.714202,-0.261351,-7.512423,-7.540210,1.858285,-9.245353,7.335576],[8.746548,-1.560803,5.681361,2.820665,9.597776,3.196966,4.733757,9.887564,8.342582,-1.837031,7.071887,8.433060,3.570067,1.834127,4.190783,8.729555],[-5.936521,-9.603405,7.257390,5.352850,5.089078,-8.918144,-6.622524,-8.183203,1.560520,-1.697022,8.616070,-7.949813,-2.733712,-9.039252,-7.622631,4.615166],[-8.710513,-2.386151,1.821326,-1.649842,-1.670398,-8.773365,5.528172,-7.572952,4.364214,2.239477,-6.728242,9.709329,-4.654329,1.312483,8.986050,3.538954],[-1.258098,-2.278556,-8.167377,2.570857,7.070981,8.675254,-1.023194,4.791303,-4.286596,-3.336182,-9.269529,-6.456873,5.126682,-4.869384,-9.792171,-3.144421],[4.074685,-4.793375,-1.642393,5.565132,0.929086,-3.659850,-5.728234,6.468082,-7.517623,-4.236704,8.973153,5.901157,-7.209965,-7.636067,-4.513850,1.558757],[8.510237,9.774160,5.923459,1.032098,0.542369,-3.773772,7.113137,8.921510,9.757846,-0.578887,-2.659422,-7.908921,3.499253,3.511733,2.628719,-4.791981],[-4.846333,-4.428865,-1.680746,1.069147,2.173550,5.683245,3.561473,1.689470,-1.574119,-3.805032,1.219341,6.135467,5.712168,-3.971454,-7.716576,9.583800],[-7.463856,-9.471419,8.898721,0.708591,-1.327318,6.793747,2.666083,-1.078633,-6.056765,-6.742298,3.289857,1.201724,-2.469729,-5.370002,-7.182952,1.571852]],[[4.809293,2.069664,6.547020,-7.291662,4.956756,-3.089355,-1.683344,8.816365,1.470252,-1.051233,5.478061,0.652013,-4.988796,-3.535152,5.361653,2.397543],[-7.907790,7.836983,4.595062,5.365796,7.981305,1.158675,-3.339138,-4.256263,-8.515140,6.681800,-0.667251,1.487315,-3.017286,3.916102,-6.948790,-9.388547],[5.327812,-1.086264,2.477244,-9.205340,9.015176,-2.224195,-7.785962,5.100733,-9.782693,-3.630408,6.507811,7.703370,-0.879926,4.175048,4.921137,8.623564],[7.698595,-0.016760,7.718020,6.144476,-1.431876,-4.612976,9.299146,-5.830745,-5.331774,-9.408518,-3.625141,4.988728,6.333220,8.580902,3.470093,9.834541],[7.418743,4.037976,-2.444464,4.120593,3.944426,3.609854,-6.688344,-1.124499,9.231613,-0.896168,-1.112598,-0.258309,4.599636,-8.073048,-4.521409,7.678906],[7.572190,-0.716497,-9.638379,7.593639,5.241261,-3.622634,-8.646582,9.524098,5.406504,0.975992,2.691156,5.135508,-2.903535,5.413254,-8.679604,-1.055746],[-1.661410,6.682540,-6.387892,-2.795223,-6.881483,7.161218,3.013713,-6.619989,0.455414,-7.905645,7.207161,4.015252,8.319933,-0.934894,8.015487,-7.308687],[6.053373,-9.312526,-3.319357,6.897179,8.344365,4.074995,8.834118,-2.644166,3.285992,-3.947886,-1.106611,-2.124356,-9.775757,2.478006,4.355962,6.438578],[-3.466108,2.634134,-0.419846,9.555722,4.983239,-9.189480,-1.164887,6.573138,9.698189,-5.657794,3.897270,-2.992094,2.170924,-9.467101,1.370966,7.539050],[0.215873,-6.847944,6.441402,-6.969764,-1.367201,-8.199333,5.548084,-8.089301,6.644053,-3.627686,-5.452828,-8.907676,8.136466,-5.804867,2.318398,-1.516704],[-8.935284,-5.944423,-3.403116,4.111603,-5.912820,7.927166,1.217177,-4.909636,-8.215081,-1.775755,2.996600,-5.561358,0.583129,2.661211,-7.887195,7.959286]],[[-8.001186,-4.223133,-8.506449,9.563128,3.118018,-1.163446,6.343102,9.543388,-7.676372,-2.075678,0.671853,-1.540012,0.017296,7.904268,4.736578,2.604247],[-6.198222,-9.354782,1.185472,2.329019,-1.071284,2.511567,2.139678,6.060730,-4.259725,0.244638,-7.285931,-5.011910,-0.330334,2.826914,1.370068,7.358469],[-3.524602,-9.124063,-0.897000,3.142142,-7.151874,-8.126338,1.803546,1.072515,9.335360,7.392864,-3.054614,3.494585,8.408893,-6.446760,9.625592,3.513657],[5.993536,5.967538,6.486211,-5.294649,-4.979674,8.881021,-1.782278,8.986003,-4.701377,1.465478,9.511607,9.473758,8.166594,7.326314,1.734296,-0.079237],[-2.805567,-0.023676,-5.912021,5.829477,4.495863,8.069034,6.020287,9.375796,9.251091,-0.695466,-8.599814,-6.248329,3.156327,-9.051125,-9.449154,8.847457],[1.550559,-4.972759,-3.551227,-8.095907,7.214395,8.991737,-4.168683,-7.340284,7.724152,-8.445120,-7.874499,2.661498,-7.689890,-0.912878,8.688093,-7.956090],[-7.981293,-6.757954,-1.524144,-1.589661,-2.514822,0.381714,3.222588,6.736624,-5.367436,-9.430887,-2.418601,0.750170,2.990913,1.865379,3.839154,0.538658],[-8.045820,8.193221,-6.020175,-7.257672,1.698085,-3.012623,4.713695,-0.627005,8.829396,-4.239839,-1.558837,3.959708,-1.115599,-4.996589,-2.935714,8.443758],[-4.778406,6.297500,-9.148727,1.990465,3.183754,-9.512131,2.153567,3.247067,6.889526,-7.657932,4.487800,-9.706876,-4.464000,5.833258,-9.795886,-7.156446],[5.808197,-9.734909,0.243188,-2.692292,5.678048,-3.671870,6.790983,7.780801,3.448994,-1.354056,9.378160,-2.929293,-7.063570,-6.065630,-6.941565,9.656492],[9.199135,-4.052537,9.535285,6.740684,8.737242,-4.713223,5.489861,-1.243898,1.379581,5.432990,8.688345,5.123636,-0.657923,-9.455306,-8.909886,-5.433561]],[[6.434540,-7.222129,6.622951,7.913971,5.602156,7.143796,-6.926275,-0.747544,9.058502,-6.745230,8.139477,-5.728672,-1.529634,2.298386,-0.050789,-9.712297],[-6.299893,-1.882849,-9.663208,-1.633691,3.246732,2.406956,7.332237,-9.570443,9.621589,6.781877,-0.774918,-6.454361,2.459223,3.880740,-2.124699,3.106002],[-5.956750,-9.933431,-1.642863,1.462502,6.715293,4.532740,-5.561796,0.370845,-9.970005,-0.194588,-1.761689,9.007406,-0.702083,8.948498,-1.943317,5.892246],[-0.723461,-7.938476,7.785806,6.698369,-8.540350,8.929808,-7.682514,-5.990786,-8.122116,2.013746,-4.572589,-8.215445,4.121147,3.440848,-0.683312,-8.576289],[-7.970059,0.422789,-9.639320,-9.355547,7.341499,1.713136,-8.232597,9.039938,1.394961,9.081740,2.592954,-3.873147,2.190029,8.990639,0.666029,3.062902],[-6.901971,8.180001,2.882081,4.597579,3.684021,-3.002779,-9.750293,-3.101546,-0.116395,6.822133,1.115864,-9.897012,8.619593,0.096531,7.110876,2.182966],[5.743407,2.266265,-4.927979,-5.455366,8.629202,-2.221939,-9.282568,1.099456,-2.575449,-4.287546,8.376532,5.372702,-4.010480,4.484060,6.548854,8.313092],[3.977648,9.598705,8.023184,1.869237,-7.021428,4.264438,2.067486,9.660229,2.686067,9.666389,-4.429177,-1.792868,9.628303,-0.588998,-0.138398,-8.153975],[-1.609530,6.365569,1.850210,6.722457,-5.932977,-6.516296,8.471166,-1.098208,6.343378,8.963638,-2.173880,9.777379,7.654915,-5.222131,8.670840,5.603015],[-9.167173,-6.209181,-5.781772,9.610074,-5.756396,-1.381706,7.923038,-6.642065,-5.592048,-0.964386,0.799385,5.090224,4.154849,-3.945643,-7.349079,0.090957],[7.228417,-3.207767,1.100461,-1.681087,1.618663,7.895407,3.463133,0.298675,-8.698167,-4.710210,1.794466,-1.904426,4.410631,-9.043271,4.528161,-6.010681]]], dtype = "float32")#candidate|7290|(16, 11, 16)|const|float32
uop_7291 = relay.atan(const_7290.astype('float32')) # shape=(16, 11, 16)
func_5802_call = mod.get_global_var('func_5802')
func_5803_call = mutated_mod.get_global_var('func_5803')
call_7325 = func_5802_call()
call_7326 = func_5802_call()
const_7346 = relay.const([[[3.403108,-5.464981,-0.197928,1.743222,3.071292,-0.785062,-9.865973,7.495485,3.255325,-4.093899,3.207281,-5.780693,-5.676940,7.044332,-4.419787,5.525826],[-6.064848,-3.051670,-5.950401,0.960831,8.214039,5.623355,9.860514,-5.101826,0.940057,4.990066,-9.857412,-0.825669,2.503867,-2.322745,-0.191393,5.239724],[3.488472,-8.190033,4.018884,-5.719059,7.500395,-8.195241,-8.486626,4.531411,2.904835,-7.472717,-2.304985,-5.239185,1.227258,-1.330994,-5.409779,-6.512414],[6.866773,-6.181245,-2.730944,3.182300,-9.667070,8.425063,-2.499571,4.375315,0.897937,4.977548,-3.636151,7.299491,-4.326993,-4.749485,0.947193,4.738976],[8.203990,1.010822,-6.851905,4.750140,-7.279952,6.173207,5.056587,-6.487257,-0.796362,0.978098,7.289357,-4.156454,-5.983060,5.173971,5.630322,-7.974689],[-1.570104,3.744685,-8.190173,2.173112,2.273425,3.564134,5.966695,6.019290,5.168493,4.221986,-4.331296,4.829234,-7.325379,-1.260854,1.450330,-0.770574],[7.938705,-6.064952,-1.460558,-8.302996,-5.560101,-5.677080,-8.952091,4.919232,-1.182632,-5.795972,6.520596,4.648767,-7.209092,5.009633,-7.715427,5.320292],[4.649202,9.206718,-6.240905,1.664844,1.092657,-3.389996,-3.616452,-2.645295,-2.604011,5.542125,-9.387440,5.394329,-3.838504,-1.641416,-5.389880,-5.561537],[2.126630,4.595511,-9.410899,-0.694720,6.030123,6.312253,-8.457439,-2.820572,-7.626361,-7.938212,5.006296,-2.029805,1.735450,-2.381511,-1.639240,5.035089],[5.825813,5.812422,-2.802464,7.555355,3.703915,1.109216,-6.417039,-0.939659,2.417841,5.771742,8.949388,-5.015305,-3.157709,-5.576164,-8.796459,-0.778583],[8.684594,3.387366,5.287997,1.312758,9.889448,1.491328,-6.371616,-0.253791,-1.244058,-1.868520,0.594086,-5.651210,-4.320845,5.895767,8.063631,-6.854836]],[[7.676606,-1.537387,-4.565901,4.851397,-0.285028,-8.671027,6.792278,-2.536696,-1.664955,1.483521,7.786241,-2.590977,-6.037224,-5.566415,9.122218,-6.995967],[-6.922957,-9.939461,-0.175334,-0.591516,-8.559928,-2.186251,-0.045778,9.702677,4.981165,-6.579910,2.340289,-7.254972,-9.710954,9.935593,5.011115,1.647015],[-0.331461,5.159662,2.054715,1.157822,-7.402076,7.858810,-3.849290,8.423262,0.731940,-4.866674,-8.246236,3.897863,-3.546629,3.459593,-2.885564,8.792933],[-7.444858,-9.411289,3.020458,1.203657,8.385718,-4.652713,6.497194,1.919379,7.143437,4.574437,4.734395,9.077348,9.331927,1.333816,2.379158,-0.078805],[5.610684,1.510679,-4.326203,-5.895775,-9.897181,0.770336,9.820457,-8.369086,5.788972,-9.199310,-1.771470,-6.484723,-9.567246,-1.659084,-6.983456,6.172335],[8.186106,-2.990619,8.698598,8.847429,9.334287,-0.371454,2.808983,-4.704808,-5.769719,9.656058,-1.683576,7.385482,-1.793619,-6.516600,-5.927009,-7.834772],[-1.509271,-3.962888,-1.604793,2.366567,-5.923636,-5.315971,9.116471,-1.553266,3.314462,-1.497213,7.749778,9.179385,9.043257,6.760438,5.805776,0.286663],[-9.192848,-3.538218,5.190887,5.412706,2.158228,-4.457967,-8.246384,-4.152760,-2.973306,0.991922,-4.150409,7.463173,-4.520585,-1.813222,1.718886,9.945985],[5.441304,-3.038866,-2.979888,-4.545005,2.127760,-9.893352,-1.975383,1.027683,2.349005,-3.806284,4.537661,-4.725167,-7.041427,-0.379320,-0.063261,-2.722380],[2.993327,6.065896,-9.086548,3.926246,-4.644028,3.013728,-6.756215,9.487855,6.285255,-0.157955,-5.469439,-3.182367,8.808881,-5.106072,-8.321535,7.797590],[6.028535,0.958166,-5.523433,8.013011,-9.845423,8.462833,1.289865,5.276882,2.304293,-1.519203,-8.857464,-2.035424,5.306630,0.019472,1.749156,9.756072]],[[1.276315,-6.909414,1.584686,-1.004850,-3.514984,-1.238295,6.957702,-0.363857,1.240750,-3.218110,2.794621,5.654621,0.679987,3.996506,6.727373,3.898223],[3.840277,2.386230,1.466010,4.529655,6.592781,1.697615,4.674877,9.898167,-8.440333,-2.332166,8.219925,-9.351430,-0.331982,1.620554,-5.144994,2.376180],[3.820524,-7.075483,-7.802733,-3.465464,-6.775329,-8.431951,-0.135657,-2.779756,1.595609,-6.119920,8.939921,3.753226,-8.792572,3.722315,8.919718,7.512798],[2.301278,1.646048,5.442036,-8.839005,-3.909896,4.730237,-6.426972,7.947750,-0.174913,-5.411472,7.073082,5.139977,8.373144,-8.526144,9.655352,4.135775],[-1.465889,6.435909,-9.708527,1.759704,-0.952441,3.337846,-1.741858,5.510052,0.942594,-5.505007,6.383782,-9.903393,5.429835,-1.175999,-9.759074,8.047105],[-0.615142,-3.651682,-3.597355,8.154688,-6.256934,-4.332239,-3.180303,4.500985,5.908458,-2.627056,-1.229518,5.985707,3.921761,-5.846542,0.036165,-1.192157],[-3.658873,8.393989,-1.742153,-4.006701,1.273991,-7.790016,-9.722063,3.198152,6.337780,-3.528557,5.097171,2.007204,8.564054,-3.379563,-9.301972,9.358485],[-8.927741,3.774962,2.379971,8.561203,-7.003444,-4.665895,-5.941044,9.052335,7.300226,0.395896,6.285214,-3.389058,-3.488267,-1.235276,9.288895,-4.048816],[-0.193543,7.699612,5.220168,-2.161550,-0.039829,-7.319432,9.804024,-4.053720,2.330472,8.690136,5.263190,-9.120468,-5.525631,-3.685594,-3.158249,0.953706],[-5.145235,-9.707635,-7.062715,-7.094912,-0.335383,1.971263,-8.651882,-0.889654,9.620202,-7.979826,4.432887,-0.051786,1.805422,-6.806234,6.215592,-9.103002],[-9.959805,1.603726,-9.767566,5.247885,-3.642787,-3.138851,-5.848919,7.770765,-7.895650,-9.089013,-4.915386,5.999184,4.243513,8.424252,-4.492660,3.706579]],[[-4.371149,0.494380,-3.830431,9.482056,0.367635,8.603103,2.945366,1.728154,-8.453461,7.294542,-6.044340,0.010331,-8.663938,0.151585,-9.162930,4.078966],[2.610294,4.506618,8.537418,2.775917,-3.455499,9.219974,6.245245,3.088061,-8.752512,-1.863625,-2.231802,1.179004,-9.250173,1.510925,9.659384,6.158521],[6.177451,-0.104904,-6.297738,5.429249,-3.858490,-7.303889,0.869081,6.411847,-5.006431,-8.534314,0.093091,-1.073986,-3.897592,7.741621,-3.561083,1.479287],[9.575213,2.335755,3.805471,2.977269,8.657425,1.017895,2.895715,-9.859474,-3.977381,-1.886406,-3.084486,8.900600,-8.605732,-9.395184,6.591023,-4.002236],[6.652799,-3.435461,-9.950737,-5.799455,5.248821,-1.267358,2.965136,7.114837,-5.156237,9.001693,-1.531500,2.529549,4.613357,0.499450,5.513227,-0.026899],[7.099216,0.697399,-9.782911,8.891386,7.472869,-7.804434,8.170761,-9.518717,-8.000315,-6.509596,-2.422258,6.580408,-6.543164,1.049026,9.963447,-6.956721],[-4.118259,-9.734445,-5.335654,9.940127,-4.709473,-5.888266,6.393745,8.542522,-7.693247,-5.254623,3.543858,2.994749,-6.496863,-9.768915,-7.797184,9.678534],[-4.387520,7.334715,7.004680,8.330483,-8.212196,7.321000,-0.690243,6.220853,6.717328,-2.481270,-6.654949,-1.157291,-7.622652,-9.295021,5.358021,8.865226],[6.454254,-6.137202,5.324031,-8.339039,2.270579,0.720496,-0.515761,2.794705,-1.053655,3.366014,4.884059,-3.665614,-0.971622,-4.965434,-6.600082,3.698680],[-7.769372,-4.482026,3.246407,6.738153,1.684060,0.328698,-5.489084,1.605903,-8.188656,9.694938,-5.216192,6.475908,-6.349929,-7.398868,5.906544,-1.541453],[-2.339556,-2.139330,-5.683628,-1.891191,-5.198201,2.614974,-6.310515,-4.190494,7.569822,-6.189038,5.317566,-9.645161,8.754324,-1.334249,1.661903,-4.488981]],[[9.388136,7.002733,4.320435,2.845095,3.312254,-9.747884,8.999836,-7.181135,-2.085298,-4.711583,-3.108537,3.949577,-9.211881,6.835956,-0.409054,0.187860],[-3.626054,6.694516,-8.515940,1.317696,-3.551386,-2.431512,-0.326661,-8.299371,5.194949,-1.078069,-6.191872,-3.432813,8.854345,-3.196808,6.128943,-3.903934],[-6.925761,1.801217,-7.549510,0.027035,-2.414207,1.829812,-0.601686,5.207164,-6.433332,-3.842275,9.046296,5.086324,-3.095043,5.819998,8.287057,0.161253],[3.559486,2.420658,8.537255,-1.747134,-1.081051,3.903807,-0.784024,-2.760422,-8.437057,5.842423,9.270827,9.579635,-9.291827,-0.384527,-1.366358,0.936801],[-4.702436,5.481026,4.026998,-6.277960,6.301319,5.522882,-7.637639,9.982469,-0.904315,7.129371,0.873485,9.047904,8.754679,-8.030597,6.485325,1.845548],[-7.056203,2.682379,8.426035,5.664858,0.996058,-2.583489,-4.457417,4.543181,-1.465246,0.752156,6.729550,4.048708,-1.757003,-4.898683,1.758343,0.568532],[-5.745085,-8.180302,-4.960205,0.091570,-0.679286,-2.420130,1.904523,3.245769,-3.519896,9.780277,9.147173,-9.668105,-5.759240,1.221562,-3.426752,1.324865],[8.807985,-4.398091,5.562867,-5.280890,6.878234,8.006540,-1.758613,-1.979664,7.301283,-3.196752,-1.256531,-6.415882,6.333531,8.430071,-6.649229,-7.888799],[-2.108343,-7.538973,-9.114475,1.883059,5.488445,-4.953818,0.332354,-4.974203,0.985682,4.264573,4.127519,-4.256825,2.032815,-0.067921,4.204538,9.490690],[-9.088163,6.255350,-0.015092,-4.967996,6.773460,7.058044,-0.556025,1.990812,-8.154317,8.735984,-0.597385,-2.182370,0.706616,-8.790595,-0.835573,-2.655996],[4.407901,3.870889,-4.558598,7.197743,2.805865,-5.709263,-2.794124,0.756495,-8.491200,-7.158158,-3.592925,-9.887683,0.068392,-1.525351,0.152418,-1.445109]],[[7.765744,-4.003709,-2.004374,3.410254,9.844188,5.857715,-7.461636,-8.586222,7.938898,6.002681,-7.492748,-5.546741,-2.667169,0.541305,8.740485,-7.428555],[9.956556,2.827541,-3.774890,5.870640,-4.729253,9.832020,3.737091,-4.570125,-9.386215,5.815786,9.683454,6.037745,-1.576924,9.866277,-6.202903,-1.853148],[8.976029,9.075697,0.304126,4.702417,6.710328,-7.275958,-2.065224,-3.508248,-7.235475,1.349447,5.320896,-6.697623,9.586657,9.815052,3.868256,-4.708731],[7.074097,6.722085,-4.852570,4.922011,7.724444,4.645344,-8.701042,2.430222,4.751827,-8.904200,3.180866,-1.041866,2.797293,-5.335777,-9.951797,7.353396],[2.425341,-2.325839,5.032717,8.816615,7.652647,-9.683767,-6.811157,-6.729127,6.996612,-0.542936,5.992823,9.018928,5.112089,-1.668560,-2.564781,3.253171],[-7.521842,-8.864576,7.070877,-6.958724,-1.719196,-3.751996,-3.678916,-5.834875,-5.272135,-0.535927,2.081311,-1.038105,-9.007122,-8.218362,-9.264727,-7.373848],[0.470059,-6.848498,-9.046944,4.571150,6.485026,-8.856889,0.425694,1.448224,0.574326,7.578575,-7.562911,3.437295,-5.776858,2.646384,-6.907079,0.814424],[-5.562882,-3.995742,9.397570,3.467354,-7.628609,-9.692072,-1.909458,4.988402,-4.245295,3.211027,-3.579904,6.352055,-5.361472,8.571204,-9.457993,6.471435],[-3.582382,4.044876,6.198046,-5.578352,-3.517257,2.155992,4.297171,1.527490,-6.332684,-6.832270,3.225166,8.524772,-2.465150,-0.096859,-6.547069,-8.268481],[-0.579042,-3.337331,-7.826557,3.611771,0.810646,-4.028297,9.692958,-9.184470,-7.866561,-3.077179,-9.214125,9.431678,-2.495429,3.109808,2.672632,6.764566],[-7.238244,-3.835032,-4.455581,9.115266,-6.854963,-3.232752,1.067087,0.420092,0.669124,-1.452438,-3.035988,3.607456,9.210260,0.740905,-6.582126,-8.218530]],[[-6.330512,5.843223,-7.136984,-7.889302,-9.975579,-9.728287,-2.595402,1.001726,5.050860,5.564175,-4.391914,-9.524167,-6.686228,-2.233712,-0.645711,2.407793],[6.264672,-6.026726,0.413770,8.959537,9.722148,-4.893357,9.118358,-9.725649,4.037182,-8.157160,-3.052069,2.455982,-2.026126,1.110928,6.876476,0.391286],[7.262293,-2.415707,5.726729,2.027727,-8.079203,-5.547097,3.780248,-7.680148,-0.912591,-9.891848,-1.440716,2.052609,-7.499962,1.885087,2.675982,-9.848106],[-0.167698,-9.737814,-1.733564,2.945389,9.654536,8.879948,-9.234715,2.263182,-7.683375,0.847849,3.849346,-7.031808,5.265577,1.552304,-8.400535,2.452865],[9.033155,-1.694435,7.274932,-0.034181,4.618466,-5.472801,8.852183,1.200167,1.565290,-6.153156,0.645499,-8.967110,0.432117,-1.079519,-2.530209,-5.752507],[9.870060,5.883017,-3.504940,3.003675,8.503900,2.470714,8.250976,7.836797,0.737203,1.654727,-2.990110,7.903396,-0.583302,6.601913,-3.095394,-7.408955],[2.282090,-3.163212,7.786062,8.885132,2.468461,5.796464,2.012898,-9.339511,6.589497,-8.564504,6.507180,8.461983,0.170526,-8.302359,-6.102030,6.797493],[2.044783,-3.712353,2.474306,0.331541,-9.905398,7.094952,0.809744,2.319655,5.406715,-0.250021,7.192069,-9.756890,4.144330,-2.277153,8.811951,3.850101],[-7.348176,6.342144,0.530376,-7.273770,-6.820940,-8.636264,6.781345,-2.317575,2.974979,-1.647575,-0.789186,6.774738,2.385572,7.318628,2.053531,5.353433],[-3.620056,0.825818,-7.590732,-9.689501,4.440054,-5.413612,-0.833322,0.055882,-6.066754,-1.159585,4.651997,-8.811138,-6.564488,1.615887,-4.842051,6.528403],[-8.726423,-2.373301,-4.178691,2.533522,5.526285,8.039459,-2.365415,4.453240,-5.113910,0.966450,8.961943,-4.751113,3.573441,3.025034,9.256033,9.987463]],[[1.217780,-4.255625,-1.993658,9.218139,7.890304,4.720335,-4.766857,-3.067172,-5.218795,-5.394759,6.579188,7.685160,-7.361417,-2.287371,9.995989,2.016726],[-4.740780,9.575764,3.350928,-6.333564,1.305973,-7.871117,7.199380,-8.098807,-5.047942,0.336236,7.088153,0.875150,-1.866874,7.207021,4.677504,-7.257007],[-5.645474,-7.732085,2.120200,1.991019,-8.511930,-1.334787,-4.739025,7.314992,8.977155,0.465882,-1.396956,-9.804244,-1.272626,-8.913171,5.476143,7.610236],[-3.099863,5.622419,8.165061,-3.757018,6.907071,5.833450,1.370086,-5.549239,8.458062,-2.664006,-4.505499,-4.417068,-7.941381,-4.165960,-2.190105,-0.213829],[7.241203,-3.527986,-3.057179,-8.586090,5.557059,6.041724,7.449427,4.204234,8.500730,-6.844124,-8.107008,1.841253,4.493539,-0.089552,4.674985,3.966147],[9.245779,5.779470,-4.327761,6.173177,2.170508,3.395980,-5.729660,-8.510929,-2.019103,-6.818031,9.721327,0.801684,3.111887,-4.818486,-3.139629,-1.477860],[4.318942,3.283086,9.266616,5.607751,-9.126976,2.120697,5.171184,-0.396427,-0.251557,1.673623,-0.167016,0.009961,-3.610247,8.995789,3.103054,-7.089588],[7.856524,-0.688609,-6.248494,-0.211302,-7.877611,-9.971859,8.062159,0.722292,7.750091,5.387286,-4.235090,5.572845,9.311988,4.485428,-3.553631,4.367126],[-7.172109,8.036505,-3.610298,7.476078,0.464725,-1.058935,-8.046500,8.906142,-8.206145,-0.466747,8.240811,-9.729628,-6.334222,0.020425,6.474804,-0.823257],[-3.947136,6.639593,1.312667,-4.832396,-8.986474,0.016262,-2.898028,-3.537401,-8.691321,1.318677,-6.992332,-0.054546,-3.944276,-0.376050,-5.217864,4.079840],[-6.096781,1.733126,4.946832,-4.133948,3.985535,-4.436088,-3.200642,-6.940056,8.004815,-3.054925,0.291226,-0.081544,-1.573618,-4.908619,-0.500635,-9.226230]],[[-8.192548,-1.427964,9.759840,4.404775,7.508826,-6.569588,-4.067397,-5.322454,5.298226,9.276181,6.849618,-0.634136,-2.370187,-0.636539,-0.303400,9.938400],[3.357870,-8.491049,1.181077,0.563933,6.023691,-5.146243,-4.213941,-4.380004,-6.593065,6.379838,6.297219,5.610011,-1.986663,-1.883542,-5.190166,7.382326],[-6.406062,-2.263708,6.380905,-3.913606,-7.660429,-5.461209,2.771940,-9.812418,-2.151990,3.355978,2.906340,-3.222239,-1.424403,-4.221070,-0.932748,-7.106979],[4.776514,-9.851362,-3.965345,6.510083,-9.268232,-5.913302,-4.542220,9.688834,-2.085915,8.957321,1.559248,2.647855,-0.523280,0.394119,7.633993,2.345358],[-3.990254,6.514379,-7.008467,1.300370,-8.320539,-8.104925,-1.881191,8.789925,-6.994852,-0.369250,-7.075107,-7.998478,5.495201,-9.141562,6.088412,9.889791],[2.432733,1.798228,-3.842516,-7.334637,-2.087380,9.907586,-5.780994,6.114552,7.083996,0.166542,2.960403,2.691809,7.533694,1.005483,6.848063,-8.066141],[5.013879,2.376722,2.419604,-4.938672,-0.173295,-7.013804,-1.912494,-9.629926,-9.304762,-9.415975,3.589045,-2.722285,6.869432,1.758307,0.531387,1.618429],[8.655189,-6.244272,9.140171,-1.502450,-3.966675,-2.195116,-1.687877,8.998691,-2.486387,-0.171786,9.205629,-3.954671,-2.944273,8.750410,-3.193678,-2.817329],[5.838338,-3.705382,7.200285,5.058332,3.977328,2.608221,-5.887650,-8.659057,-1.040253,-7.358781,-5.544096,-3.844020,-1.281332,-1.848101,-2.899090,5.156153],[6.731993,-4.514141,-2.185735,-0.786568,-1.734675,-0.457807,-1.358991,1.826557,1.853019,-4.904106,3.636776,2.336105,7.876425,-6.995236,-3.047201,6.754163],[2.715793,2.873421,9.534864,3.104598,6.455751,-0.903143,5.627773,-1.674432,1.525830,-0.284559,8.420529,7.915219,5.582664,-2.981279,6.820714,9.995675]],[[-8.507717,-8.142849,-3.670863,6.647526,3.064577,-4.863066,4.559754,-8.880930,4.314590,7.867747,-8.580572,7.421471,-4.263586,2.817436,-7.056766,-7.282152],[0.805871,-8.346700,1.023799,7.367895,-2.352341,0.011888,-4.129404,-2.721686,-3.761737,-0.517043,-8.972225,-6.839360,-7.887527,-1.537132,-0.609131,0.004522],[-1.836533,4.631474,2.558406,-6.007748,-5.965071,7.962483,2.095914,1.694503,-6.516666,-8.807864,7.715634,8.151671,7.456097,-1.062533,4.245337,4.353811],[-2.715407,5.442732,-9.906701,2.245020,5.588501,3.446342,-2.394203,-8.520470,2.762994,-8.866935,5.994039,-8.362049,9.687843,-9.481461,-3.022141,-9.622844],[-1.440350,-4.448150,-4.370168,-6.183203,-0.937873,-4.366256,-0.225586,6.078598,-4.567858,-5.730549,-4.114186,-2.543159,-1.778508,-2.316657,-8.306458,3.389803],[-4.606127,6.663532,9.121500,-7.883012,-7.287296,-3.721036,5.562477,-2.743874,6.549370,5.433553,2.533150,-7.380871,-6.151499,-8.759936,7.314516,4.757376],[7.168057,-4.173675,-8.000353,-2.167917,-4.115927,7.928985,3.148592,2.764289,1.800017,-1.209931,-0.610589,-0.339116,5.517259,6.371997,-8.598759,-6.323753],[-3.266499,-9.330624,1.728798,8.369213,2.456652,0.217671,-4.502500,-6.377927,7.910006,-1.794001,4.409080,-0.546394,7.611678,4.097030,-2.711870,9.708012],[7.700139,-0.122924,-6.965660,-9.548080,-1.185728,-3.694771,-0.043603,-2.083972,2.924799,7.500068,0.661149,4.270952,7.187610,-2.677887,-0.387612,-3.862722],[8.749377,-4.847652,-2.196674,-8.851524,-6.328412,5.732354,5.052093,-3.680230,-0.419416,1.973362,3.683256,-6.927511,1.333891,4.263655,-6.346105,5.153661],[-3.573391,-8.112791,-9.850500,2.703363,6.172181,6.178594,5.657303,-9.558347,4.873811,7.907368,-7.330734,-6.483043,8.997918,-9.825379,7.074897,9.057895]],[[6.916769,2.511823,-3.339905,0.010646,6.141680,-1.404876,-8.330594,1.162950,-2.002098,6.764049,-1.101080,7.215525,8.647789,-0.285428,0.202197,-4.413248],[1.816496,9.078676,-7.412567,9.675648,7.401077,-3.099240,-3.812705,-9.902080,8.311901,-5.431881,9.242742,7.252390,1.807291,6.614201,9.230115,8.121121],[6.576922,1.329737,1.664030,-3.630700,-6.224002,0.393238,-9.996125,-2.494569,6.664578,3.449577,-1.515666,5.916916,-1.707041,-9.418276,-3.810869,-4.545253],[-5.271325,9.648605,1.840784,3.934630,9.441444,-4.575110,-7.974692,7.700998,0.297622,-7.554334,5.685498,8.363661,-5.796708,1.670066,-2.614756,7.107239],[3.617586,-7.107023,-2.608953,0.943300,-1.809387,1.603489,-2.113156,-3.531469,9.610633,4.401560,-4.334954,0.993925,-0.479794,0.101204,-7.756758,-5.183764],[-4.452860,-8.118652,-6.798984,-4.081253,-1.535302,7.414088,-8.970462,-1.538342,-8.128908,-0.124713,7.113355,8.723441,-5.748904,-8.063090,9.279647,9.851536],[2.838420,-7.081258,7.180182,6.200704,-5.890707,-2.470270,-8.558660,8.830984,-7.225460,-3.433871,1.640667,4.049518,-0.348261,-9.088767,-1.565541,0.628850],[-4.010814,0.826804,-0.906016,2.575442,8.984802,4.400552,-7.342981,-5.806459,-6.360406,-4.902622,6.673873,-3.807284,6.503322,3.664355,-8.162858,-5.444001],[0.365369,-7.320413,-1.339442,-3.031501,7.028070,2.782542,-0.612070,-5.270205,-7.398089,-3.995803,-1.824463,-5.716078,-4.807744,-1.794170,-5.658501,8.205905],[-4.455418,-9.220020,4.774665,4.875755,-8.014608,-4.402709,-8.205372,-6.410590,-0.110681,-1.782377,3.614303,-5.358934,2.489556,-5.592217,4.327390,9.819441],[2.057714,-3.794528,-0.412811,2.693212,3.914981,-0.604268,-3.996841,-4.419870,1.297362,7.948831,1.533431,-2.939741,-3.425638,5.865904,-8.126270,-1.328019]],[[-4.404447,-9.149481,-3.224453,5.523222,-0.554983,7.069118,-0.161159,0.234732,8.344452,-5.855841,-1.270619,6.981650,4.145940,8.562226,6.409502,1.493950],[-6.719926,-8.566956,2.497046,-8.488030,0.821079,-6.902753,-9.155070,-1.874371,5.315558,-5.570311,5.969246,-1.754634,-5.920482,6.844196,3.781360,6.958724],[-4.842070,-5.148868,-2.916089,4.639384,7.860910,0.443388,3.534981,6.957709,3.547649,8.313723,5.188015,4.012440,9.616765,6.480629,-1.776184,-1.211553],[-0.545051,-5.517269,-2.979944,4.042411,-9.055803,6.287870,-4.643961,-0.515851,-0.876391,-2.384407,2.532470,-2.888236,-1.948138,-9.761241,-6.745162,-0.768866],[2.081269,5.999301,-3.420676,9.409410,-5.643695,9.198281,2.061499,-4.448672,8.462098,2.381957,-0.798700,2.096698,7.731717,4.458228,-2.964744,3.638444],[4.552069,1.326748,4.847049,-0.985684,0.428532,-3.187826,1.141230,8.629966,7.523025,3.386864,-9.112118,2.039746,-0.635196,2.755857,-7.742562,2.030269],[-7.318269,9.468284,6.501204,8.754582,5.057396,-6.593096,-4.122226,7.703708,-5.298285,9.248627,3.550822,1.789357,-7.441169,5.267213,9.293852,-6.588150],[6.138668,2.768761,4.555279,-0.417024,-9.271659,5.912648,-3.147830,-0.629518,4.814449,7.102386,-8.138961,3.194743,1.307863,1.663786,7.979566,-0.518332],[-1.732616,4.136020,-9.708932,-7.960934,-4.435234,9.282155,2.791360,-3.339248,-9.904757,2.991791,-5.021135,4.396651,5.832751,-0.517422,-2.464303,-8.055516],[-2.649536,-6.624814,0.249089,8.647955,-2.797519,-2.095284,-2.797258,-3.551736,-0.505716,-9.008448,-6.214798,-6.904257,-4.130556,-0.259079,-0.354173,3.357875],[1.586648,3.185328,1.691537,-6.421659,-8.074728,4.071212,0.717014,1.039374,1.377811,-5.406967,1.751253,-1.335480,7.782088,-1.048558,6.670976,-6.921422]],[[0.947722,8.465574,-4.119405,-4.431745,-0.023613,-1.394782,7.346977,2.872148,8.064405,8.381053,-8.333081,-6.263925,-0.747835,5.445455,6.383756,-0.522953],[-2.856021,9.620174,-5.830052,7.597749,2.355901,-4.437914,8.562034,5.547006,-7.127371,4.079092,-3.854826,-5.476110,-9.798456,-9.859067,-8.005473,-5.168917],[-8.334814,3.852207,8.589389,6.750522,-0.968736,7.337526,9.186307,-1.706337,0.988590,3.495673,-5.685250,7.615940,5.431543,-4.187220,-2.536568,-4.315458],[-0.410999,9.828619,-2.264264,-8.488223,6.722039,-3.818506,-5.826396,-9.276392,-4.795123,-7.385095,1.634902,5.015364,0.016577,-6.412191,-1.955991,6.516200],[7.712561,-9.518155,3.812431,-1.420396,7.721232,-4.131914,-4.210887,8.717278,-2.772724,1.526661,6.866235,-4.690887,-6.919237,7.252172,-6.830300,8.353164],[3.111430,4.210123,-3.455129,5.291909,7.279310,8.957192,-7.117553,-4.937400,-2.318017,4.985960,2.032544,6.735957,-6.873712,-9.987632,5.729550,-5.059253],[-9.682337,5.529456,-7.117312,-3.044925,-8.044293,7.794718,-7.530397,2.109263,9.829799,4.385647,5.481821,-9.795760,3.529669,-0.347882,-3.803456,7.153470],[-3.292778,8.397333,-5.095673,-9.783756,9.741092,2.120780,-3.924286,9.791588,9.907758,-9.141858,4.110541,8.474942,6.209161,6.340144,-1.412924,-1.265812],[6.562944,7.696661,5.491056,6.987043,6.344687,9.276750,8.235676,1.605596,9.225735,8.324163,-7.159610,3.492689,-4.903168,5.211051,6.163531,-2.173745],[5.624869,-9.648872,6.164293,-4.244759,1.324638,-5.868317,-7.852263,4.170434,5.258837,-4.404396,0.023175,-6.693729,-1.550376,1.584800,3.924880,-8.181930],[4.502822,-8.460974,-3.303151,-8.373382,-3.064695,9.773584,-8.504078,-6.613501,8.649612,-5.851607,-4.250483,8.693923,-7.558812,-4.902147,-7.597245,5.640614]],[[-0.787175,-5.789401,-3.516234,-7.167465,-6.043879,5.855998,-5.836645,-4.301575,-2.909954,5.456623,6.996770,2.142589,7.581909,-4.493754,-7.280771,7.166419],[2.941237,-1.471154,-9.249485,-6.586474,-8.780451,-1.295551,9.136100,-2.145738,1.431496,-0.278581,-9.888614,-1.582500,9.893092,7.710657,-9.167496,-8.014509],[8.041559,7.270275,6.967075,-5.600439,5.434915,4.677781,4.010249,-7.107328,7.958635,-8.435317,-4.524706,3.511935,6.027546,-9.728340,8.055892,8.570141],[6.700988,3.799947,-7.296167,-8.661686,-9.229318,-0.849350,2.792782,-1.382009,8.402398,0.395220,3.083145,0.505623,4.518660,9.248282,5.397782,3.057173],[1.516255,6.547622,-1.067964,-5.644116,3.419865,5.328840,4.629195,6.617851,-0.482387,2.555018,8.435403,-8.546116,-0.406306,-2.486571,-2.078488,-7.424021],[-2.496235,8.967585,1.970285,1.254226,-6.379681,7.253219,-4.068077,-9.699586,1.708319,-2.657562,-4.373707,-6.790692,-0.915717,-5.955367,-5.161698,4.235655],[0.810222,-5.670328,-5.962874,6.883560,-9.532364,-1.491578,-7.020326,6.484431,-9.097648,-1.575535,-7.881143,6.852664,6.341666,1.862836,-2.443143,-7.873733],[5.993486,-2.148554,-9.481396,-9.545517,5.965168,7.833859,5.575909,5.440683,2.989156,-4.038340,-2.431657,-6.821075,-1.298813,-0.485388,-8.784592,-4.191371],[3.058964,5.724125,-1.297404,-3.618330,0.975739,9.794886,-0.714654,-5.030426,9.743109,6.118791,2.680707,2.414567,6.593935,-2.916191,3.674205,7.080616],[-8.433968,-3.759380,-0.742091,-2.614519,1.691078,-6.357446,-6.667295,0.464380,9.378143,-0.503919,-8.094020,-9.182547,6.281824,-4.019339,1.252105,4.228455],[-8.318702,6.754262,-1.614749,-6.470139,9.314895,5.621585,-9.258060,1.096908,1.121579,-1.693384,-6.356926,3.913404,1.962484,-0.047342,8.156373,-4.433882]],[[3.289928,-9.704284,2.904859,5.402113,4.590520,0.069809,2.985413,6.725018,-0.650005,8.687898,5.733394,-4.389597,-8.036356,4.289269,-5.952713,7.646080],[9.985456,6.084963,2.936393,-9.853604,2.250677,-6.624358,-9.353298,5.479161,8.414902,9.035306,9.533121,6.865254,-0.359842,2.980521,8.450478,6.505514],[-5.976248,6.773411,8.525030,-1.816112,9.726323,-5.442587,-4.937261,-3.537297,-6.840861,-1.998410,8.102891,5.479858,7.580758,-3.536360,0.754397,8.604479],[-7.422828,2.293860,-9.115960,-9.817011,-1.047220,-8.437751,-1.638451,-1.088955,-2.193908,-4.169657,5.204162,-7.796441,-7.727512,3.258473,-2.135112,9.015019],[8.076975,-2.831342,-7.776595,-6.878911,2.270721,-3.558404,8.877135,-6.610852,3.853403,-1.064302,-4.624061,3.072788,7.407160,7.535149,-3.026895,0.202503],[1.004030,6.296240,-0.448735,4.897359,-8.425373,-6.629089,-7.444874,-6.606985,0.639241,-7.057479,6.611461,5.620048,-1.663619,-2.341861,7.362005,9.168952],[4.284158,6.193514,-3.306462,-3.239469,-8.196328,-3.504693,6.808874,-0.183452,9.142141,5.383580,5.381761,-9.742747,7.715055,-9.010175,-1.616899,2.289797],[-1.066432,3.288765,9.501932,-8.258676,-1.146354,9.291209,3.005055,8.824091,-6.406385,4.172974,5.173325,-2.826726,-7.083546,9.378306,-4.419440,-6.927860],[8.364753,2.368998,8.093965,-5.824363,-7.124016,-0.857934,-4.722655,4.077495,-4.214618,-0.356507,-3.882179,-0.703589,5.208941,9.125843,-0.778712,-5.409235],[2.627189,9.017795,0.316921,1.379486,7.690092,3.379736,4.727142,-2.492832,0.120252,9.637225,0.613887,-3.232911,2.097877,-7.080960,-5.378444,-6.248125],[-3.677872,-5.529217,3.885151,-6.978032,3.710137,-4.409412,-7.261283,-0.896940,2.926505,0.169748,1.559996,5.382495,0.794781,2.664603,5.150663,3.608447]],[[1.222866,9.146733,5.437523,4.554469,-9.153839,1.154205,-5.269718,-1.854861,2.051400,3.023921,-5.766208,-2.861227,-2.296547,2.041502,0.880340,-8.124095],[-7.685440,1.045391,7.640986,2.012969,8.783009,-3.515651,-2.200246,9.337299,-3.398451,5.993056,-2.290189,-3.153402,8.250209,-7.274742,-6.031399,2.189095],[-7.620565,5.506109,3.557533,0.495653,7.214451,-6.181860,7.323763,-2.082357,-9.446391,-2.199002,2.477648,-4.478302,-5.234945,7.320850,3.801547,8.599396],[1.970559,1.388994,7.415664,7.373032,-3.960988,3.524498,-9.890028,8.534257,0.529862,3.954799,-4.418071,7.460855,-4.691827,6.181999,9.805526,4.619755],[9.744024,4.675004,-7.382842,-8.448975,-2.128704,-9.999609,4.397255,-8.018524,6.396797,2.109329,3.697871,-2.539289,1.789488,4.758498,-8.395941,6.139204],[4.878529,0.683291,-2.883783,-0.935262,5.519747,9.450293,-9.574964,5.709570,9.914317,0.560002,5.594514,-8.061814,4.914218,0.988786,-1.510554,-8.434087],[7.021280,8.271399,1.071772,-2.887871,-1.045747,9.669163,8.955632,-0.461992,5.698455,8.393881,4.741359,1.494820,5.065661,1.532417,7.309572,0.926537],[4.511085,-4.469517,-7.930905,0.972764,-3.789579,5.418447,7.434874,-4.132386,2.344233,3.461810,5.512116,-0.940684,3.214727,1.375056,7.299968,0.469500],[6.489892,1.351534,-4.590443,5.044685,5.395942,1.797919,-7.741431,6.606086,0.740262,7.005933,0.971695,-7.178690,3.878344,8.958804,-5.618595,1.894614],[2.867538,-8.769474,5.281108,-1.767669,-7.501291,4.673566,-1.430768,8.187856,5.291995,-5.813267,-6.122806,4.979761,-8.434322,-5.909515,4.636952,4.632555],[-1.241734,-3.455967,6.472746,-8.617019,-5.375326,-2.471389,-2.476123,4.258952,-6.043632,-5.557999,-4.427746,-5.760080,-4.519200,6.630468,-7.524462,-7.539128]]], dtype = "float32")#candidate|7346|(16, 11, 16)|const|float32
bop_7347 = relay.minimum(uop_7291.astype('uint32'), relay.reshape(const_7346.astype('uint32'), relay.shape_of(uop_7291))) # shape=(16, 11, 16)
func_7187_call = mod.get_global_var('func_7187')
func_7188_call = mutated_mod.get_global_var('func_7188')
call_7351 = func_7187_call()
call_7352 = func_7187_call()
output = relay.Tuple([call_7325,bop_7347,call_7351,])
output2 = relay.Tuple([call_7326,bop_7347,call_7352,])
func_7359 = relay.Function([], output)
mod['func_7359'] = func_7359
mod = relay.transform.InferType()(mod)
output = func_7359()
func_7360 = relay.Function([], output)
mutated_mod['func_7360'] = func_7360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1643_call = mod.get_global_var('func_1643')
func_1644_call = mutated_mod.get_global_var('func_1644')
call_7409 = relay.TupleGetItem(func_1643_call(), 0)
call_7410 = relay.TupleGetItem(func_1644_call(), 0)
func_5883_call = mod.get_global_var('func_5883')
func_5884_call = mutated_mod.get_global_var('func_5884')
call_7441 = relay.TupleGetItem(func_5883_call(), 5)
call_7442 = relay.TupleGetItem(func_5884_call(), 5)
output = relay.Tuple([call_7409,call_7441,])
output2 = relay.Tuple([call_7410,call_7442,])
func_7444 = relay.Function([], output)
mod['func_7444'] = func_7444
mod = relay.transform.InferType()(mod)
output = func_7444()
func_7445 = relay.Function([], output)
mutated_mod['func_7445'] = func_7445
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6302_call = mod.get_global_var('func_6302')
func_6304_call = mutated_mod.get_global_var('func_6304')
call_7457 = relay.TupleGetItem(func_6302_call(), 0)
call_7458 = relay.TupleGetItem(func_6304_call(), 0)
output = relay.Tuple([call_7457,])
output2 = relay.Tuple([call_7458,])
func_7467 = relay.Function([], output)
mod['func_7467'] = func_7467
mod = relay.transform.InferType()(mod)
mutated_mod['func_7467'] = func_7467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7467_call = mutated_mod.get_global_var('func_7467')
call_7468 = func_7467_call()
output = call_7468
func_7469 = relay.Function([], output)
mutated_mod['func_7469'] = func_7469
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4833_call = mod.get_global_var('func_4833')
func_4834_call = mutated_mod.get_global_var('func_4834')
call_7470 = relay.TupleGetItem(func_4833_call(), 2)
call_7471 = relay.TupleGetItem(func_4834_call(), 2)
output = call_7470
output2 = call_7471
func_7474 = relay.Function([], output)
mod['func_7474'] = func_7474
mod = relay.transform.InferType()(mod)
mutated_mod['func_7474'] = func_7474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7474_call = mutated_mod.get_global_var('func_7474')
call_7475 = func_7474_call()
output = call_7475
func_7476 = relay.Function([], output)
mutated_mod['func_7476'] = func_7476
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2562_call = mod.get_global_var('func_2562')
func_2563_call = mutated_mod.get_global_var('func_2563')
call_7496 = relay.TupleGetItem(func_2562_call(), 0)
call_7497 = relay.TupleGetItem(func_2563_call(), 0)
output = call_7496
output2 = call_7497
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
func_5133_call = mod.get_global_var('func_5133')
func_5135_call = mutated_mod.get_global_var('func_5135')
call_7541 = func_5133_call()
call_7542 = func_5133_call()
func_4013_call = mod.get_global_var('func_4013')
func_4015_call = mutated_mod.get_global_var('func_4015')
call_7551 = relay.TupleGetItem(func_4013_call(), 0)
call_7552 = relay.TupleGetItem(func_4015_call(), 0)
output = relay.Tuple([call_7541,call_7551,])
output2 = relay.Tuple([call_7542,call_7552,])
func_7556 = relay.Function([], output)
mod['func_7556'] = func_7556
mod = relay.transform.InferType()(mod)
mutated_mod['func_7556'] = func_7556
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7556_call = mutated_mod.get_global_var('func_7556')
call_7557 = func_7556_call()
output = call_7557
func_7558 = relay.Function([], output)
mutated_mod['func_7558'] = func_7558
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7525_call = mod.get_global_var('func_7525')
func_7527_call = mutated_mod.get_global_var('func_7527')
call_7559 = func_7525_call()
call_7560 = func_7525_call()
func_5970_call = mod.get_global_var('func_5970')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_7564 = relay.TupleGetItem(func_5970_call(), 0)
call_7565 = relay.TupleGetItem(func_5972_call(), 0)
func_3035_call = mod.get_global_var('func_3035')
func_3038_call = mutated_mod.get_global_var('func_3038')
var_7567 = relay.var("var_7567", dtype = "float32", shape = (24, 10))#candidate|7567|(24, 10)|var|float32
call_7566 = relay.TupleGetItem(func_3035_call(relay.reshape(var_7567.astype('float32'), [24, 10])), 3)
call_7568 = relay.TupleGetItem(func_3038_call(relay.reshape(var_7567.astype('float32'), [24, 10])), 3)
uop_7571 = relay.log2(var_7567.astype('float32')) # shape=(24, 10)
output = relay.Tuple([call_7559,call_7564,call_7566,uop_7571,])
output2 = relay.Tuple([call_7560,call_7565,call_7568,uop_7571,])
func_7598 = relay.Function([var_7567,], output)
mod['func_7598'] = func_7598
mod = relay.transform.InferType()(mod)
mutated_mod['func_7598'] = func_7598
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7599 = relay.var("var_7599", dtype = "float32", shape = (24, 10))#candidate|7599|(24, 10)|var|float32
func_7598_call = mutated_mod.get_global_var('func_7598')
call_7600 = func_7598_call(var_7599)
output = call_7600
func_7601 = relay.Function([var_7599], output)
mutated_mod['func_7601'] = func_7601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7474_call = mod.get_global_var('func_7474')
func_7476_call = mutated_mod.get_global_var('func_7476')
call_7603 = func_7474_call()
call_7604 = func_7474_call()
uop_7605 = relay.log2(call_7603.astype('float64')) # shape=(135,)
uop_7607 = relay.log2(call_7604.astype('float64')) # shape=(135,)
output = uop_7605
output2 = uop_7607
func_7609 = relay.Function([], output)
mod['func_7609'] = func_7609
mod = relay.transform.InferType()(mod)
mutated_mod['func_7609'] = func_7609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7609_call = mutated_mod.get_global_var('func_7609')
call_7610 = func_7609_call()
output = call_7610
func_7611 = relay.Function([], output)
mutated_mod['func_7611'] = func_7611
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_7652 = relay.TupleGetItem(func_2978_call(), 1)
call_7653 = relay.TupleGetItem(func_2980_call(), 1)
func_6984_call = mod.get_global_var('func_6984')
func_6985_call = mutated_mod.get_global_var('func_6985')
call_7694 = relay.TupleGetItem(func_6984_call(), 2)
call_7695 = relay.TupleGetItem(func_6985_call(), 2)
func_5536_call = mod.get_global_var('func_5536')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_7696 = relay.TupleGetItem(func_5536_call(), 0)
call_7697 = relay.TupleGetItem(func_5538_call(), 0)
func_7187_call = mod.get_global_var('func_7187')
func_7188_call = mutated_mod.get_global_var('func_7188')
call_7703 = func_7187_call()
call_7704 = func_7187_call()
var_7721 = relay.var("var_7721", dtype = "float64", shape = (2, 11, 12))#candidate|7721|(2, 11, 12)|var|float64
bop_7722 = relay.equal(call_7696.astype('bool'), relay.reshape(var_7721.astype('bool'), relay.shape_of(call_7696))) # shape=(2, 11, 12)
bop_7725 = relay.equal(call_7697.astype('bool'), relay.reshape(var_7721.astype('bool'), relay.shape_of(call_7697))) # shape=(2, 11, 12)
output = relay.Tuple([call_7652,call_7694,call_7703,bop_7722,])
output2 = relay.Tuple([call_7653,call_7695,call_7704,bop_7725,])
func_7729 = relay.Function([var_7721,], output)
mod['func_7729'] = func_7729
mod = relay.transform.InferType()(mod)
mutated_mod['func_7729'] = func_7729
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7730 = relay.var("var_7730", dtype = "float64", shape = (2, 11, 12))#candidate|7730|(2, 11, 12)|var|float64
func_7729_call = mutated_mod.get_global_var('func_7729')
call_7731 = func_7729_call(var_7730)
output = call_7731
func_7732 = relay.Function([var_7730], output)
mutated_mod['func_7732'] = func_7732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5010_call = mod.get_global_var('func_5010')
func_5011_call = mutated_mod.get_global_var('func_5011')
call_7739 = relay.TupleGetItem(func_5010_call(), 0)
call_7740 = relay.TupleGetItem(func_5011_call(), 0)
func_6099_call = mod.get_global_var('func_6099')
func_6102_call = mutated_mod.get_global_var('func_6102')
var_7744 = relay.var("var_7744", dtype = "float32", shape = (1584,))#candidate|7744|(1584,)|var|float32
call_7743 = relay.TupleGetItem(func_6099_call(relay.reshape(var_7744.astype('float32'), [132, 12])), 4)
call_7745 = relay.TupleGetItem(func_6102_call(relay.reshape(var_7744.astype('float32'), [132, 12])), 4)
output = relay.Tuple([call_7739,call_7743,var_7744,])
output2 = relay.Tuple([call_7740,call_7745,var_7744,])
func_7750 = relay.Function([var_7744,], output)
mod['func_7750'] = func_7750
mod = relay.transform.InferType()(mod)
var_7751 = relay.var("var_7751", dtype = "float32", shape = (1584,))#candidate|7751|(1584,)|var|float32
output = func_7750(var_7751)
func_7752 = relay.Function([var_7751], output)
mutated_mod['func_7752'] = func_7752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2871_call = mod.get_global_var('func_2871')
func_2873_call = mutated_mod.get_global_var('func_2873')
call_7843 = func_2871_call()
call_7844 = func_2871_call()
func_904_call = mod.get_global_var('func_904')
func_906_call = mutated_mod.get_global_var('func_906')
const_7853 = relay.const([10,-2,8,-2,-3,-6,9,-10,-4,-1,4,-8,5,-6,-7,-3,-4,-3,-4,3,-1,6,-4,10,-9,7,-7,6,4,-5,10,7,2,-6,4,4,10,-7,10,4,-8,-3,-4,9,2,1,3,-5,8,9,-3,-7,-7,-7,2,4,-2,7,7,-8,-9,10,6,4,7,6,-10,-2,1,-2,3,-3,5,3,-5,1,-9,-7,-6,-9,-6,-2,-1,-3,-4,-5,3,1,9,9,4,-9,5,-8,-7,-4,3,1,-8,4,1,10,9,-9,-5,2,2,-2,5,8,8,-7,7,5,-2,9,10,5,-1,8,7,-7,1,-8,1,10,-7,10,-5,-1,-6,10,2,-7,-2,-2,5,1,-1,2,-4,-3,9,7,10,1,-10,4,-8,8,-6,-2,2,-4,-10,-6,3,7,5,-8,-4,5,-1,8,9,-1,8,5,5,-2,-10,-1,-8,-4,2,9,2,10,4,3,5,8,7,1,5,-9,2,7,-8,-4,-3,-6,9,-8,-5,-8,-7,4,-2,-8,-10,1,6,-3,-8,-7,-2,-6,9,5,5,4,10,7,-7,-8,-9,9,6,2,-1,-5,-1,3,4,-6,1,-4,10,-10,4,3,6,1,-6,-6,-1,9,3,-4,1,-8,9,-3,1,5,-3,1,10,3,-6,-2,-1,10,4,1,-3,-8,-10,1,-4,9,5,-9,3,-3,-1,7,-6,6,-1,5,-5,-4,4,8,-4,-7,8,-3,10,-1,1,-4,5,8,6,-9,6,6,3,-10,-3,-3,5,-4,-2,-5,-5,1,-9,-7,2,-6,1,10,7,8,-7,1,-9,-6,-1,5,9,5,6,-3,-8,-9,-10,-5,-9,5,6,-9,-4,-5,7,1,7,-4,-10,3,5,-8,-3,1,8,9,3,-8,-2,-2,-4,-6,10,7,-8,-7,4,-7,-2,8,-4,3,-4,4,5,-6,-8,-3,-2,-6,1,-3,-3,-10,1,-5,5,-4,-9,5,-4,-5,3,9,-6,-6,-2,-2,3,10,-9,3,-2,-3,7,7,10,4,-9,9,-9,4,7,-6,5,-6,-10,-8,-8,-3,10,-4,1,-2,-10,8,7,1,-6,-6,-1,-7,3,-3,-8,-4], dtype = "uint32")#candidate|7853|(420,)|const|uint32
call_7852 = relay.TupleGetItem(func_904_call(relay.reshape(const_7853.astype('uint32'), [14, 5, 6])), 0)
call_7854 = relay.TupleGetItem(func_906_call(relay.reshape(const_7853.astype('uint32'), [14, 5, 6])), 0)
func_6949_call = mod.get_global_var('func_6949')
func_6951_call = mutated_mod.get_global_var('func_6951')
call_7857 = relay.TupleGetItem(func_6949_call(), 1)
call_7858 = relay.TupleGetItem(func_6951_call(), 1)
func_2627_call = mod.get_global_var('func_2627')
func_2630_call = mutated_mod.get_global_var('func_2630')
const_7863 = relay.const([5.126322,6.076896,0.402532,-4.140544,-8.548174,-3.924324,6.210434,-5.551430,-6.457213,6.013871,-5.585729,0.876181,-0.052592,-1.964090,-8.572893,-1.089026,-4.289635,3.077332,-3.390044,7.838797,8.786511,0.790537,6.391027,-6.411944,4.463241,-4.756158,4.894835,-9.885748,-3.423657,0.215777,6.472369,-9.376043,6.400205,8.736226,-9.000834,-5.104918,0.375518,-2.700232,2.227775,-4.834523,-4.308552,-0.437380,-2.358158,8.721298,-5.732408,-4.530007,-6.597294,9.304050,-1.733720,7.812392,-7.483599,-3.291325,-0.184743,-3.607326,-1.756715,-6.316271,9.174867,-4.735442,-1.049271,-3.492592,0.438342,-7.089202,2.166886,4.902350,-7.989076,-9.921744,1.415275,-5.515747,1.403823,9.065952,-3.503419,0.946858,8.923576,7.713770,5.742145,-7.884592,-3.961428,1.987588,-5.544506,-2.607262,4.457302,4.491766,9.813946,-6.310414,-1.434247,-7.454509,-5.307668,-1.057974,-1.179441,7.381971,1.765664,-5.978452,-8.284311,-6.189333,-4.872841,9.032356,7.107311,-8.390912,5.637101,-7.753411,0.672793,-1.029229,-3.705999,5.665774], dtype = "float64")#candidate|7863|(104,)|const|float64
call_7862 = relay.TupleGetItem(func_2627_call(relay.reshape(const_7863.astype('float64'), [52, 2])), 0)
call_7864 = relay.TupleGetItem(func_2630_call(relay.reshape(const_7863.astype('float64'), [52, 2])), 0)
func_4574_call = mod.get_global_var('func_4574')
func_4576_call = mutated_mod.get_global_var('func_4576')
call_7867 = relay.TupleGetItem(func_4574_call(), 0)
call_7868 = relay.TupleGetItem(func_4576_call(), 0)
output = relay.Tuple([call_7843,call_7852,const_7853,call_7857,call_7862,const_7863,call_7867,])
output2 = relay.Tuple([call_7844,call_7854,const_7853,call_7858,call_7864,const_7863,call_7868,])
func_7877 = relay.Function([], output)
mod['func_7877'] = func_7877
mod = relay.transform.InferType()(mod)
output = func_7877()
func_7878 = relay.Function([], output)
mutated_mod['func_7878'] = func_7878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4013_call = mod.get_global_var('func_4013')
func_4015_call = mutated_mod.get_global_var('func_4015')
call_7890 = relay.TupleGetItem(func_4013_call(), 0)
call_7891 = relay.TupleGetItem(func_4015_call(), 0)
func_2330_call = mod.get_global_var('func_2330')
func_2333_call = mutated_mod.get_global_var('func_2333')
const_7951 = relay.const([3.497120,-2.094400,3.813325,-9.591560,7.670489,-7.262391,-1.698058,-3.744476,6.281201,5.167746,2.306303,6.631968,-5.648074,0.443191,4.710369,-1.547496,7.952862,7.632411,5.759924,9.631421,4.773636,1.356931,-4.702109,3.157855,4.223177,-0.466308,-8.169417,2.021984,-5.804762,-7.975778,7.912642,5.930892,-9.263846,6.357040,-4.693586,-8.501980,-7.460488,0.715316,7.583818,3.583196,2.313344,6.420374,2.896276,8.292339,0.177186,2.172439,-3.924444,-0.885487,4.336780,-9.048011,-6.330237,0.247002,8.123091,4.495900,0.521807,8.231586,-8.077978,8.791439,8.454508,4.442045,-5.734078,-1.346918,7.851522,7.658434,-3.410678,-9.756942,2.664111,-8.929581,-9.029991,8.975588,-1.076368,2.592311,-3.892243,-6.565905,7.207833,-8.745300,-6.318510,-0.567716,2.666000,-3.533103,5.208432,-0.678235,-6.141604,9.725349,-8.639891,-9.685712,-1.272357,6.174475,-6.886264,-0.908928,-1.442997,-8.506714,0.378962,-1.532051,-0.544182,4.174829,-3.940540,-2.996866,-8.646584,5.597242,8.351662,5.039215,0.258547,-5.813044,-1.993264,2.955390,6.968673,9.590301,-1.771902,-1.817532,-0.941188,2.886899,6.344589,8.037158,3.458473,5.170956,-3.071609,-7.951753,1.392970,-4.986601,-5.003771,-2.985975,0.296872,-1.197495,-7.972449,-0.651791,-7.220021,7.200801,-4.018491,2.755738,4.954611,-8.865275,9.495847,-1.267313,7.894988], dtype = "float32")#candidate|7951|(135,)|const|float32
call_7950 = func_2330_call(relay.reshape(const_7951.astype('float32'), [5, 3, 9]), relay.reshape(const_7951.astype('float32'), [5, 3, 9]), )
call_7952 = func_2330_call(relay.reshape(const_7951.astype('float32'), [5, 3, 9]), relay.reshape(const_7951.astype('float32'), [5, 3, 9]), )
func_2390_call = mod.get_global_var('func_2390')
func_2393_call = mutated_mod.get_global_var('func_2393')
var_7962 = relay.var("var_7962", dtype = "float32", shape = (1089, 1))#candidate|7962|(1089, 1)|var|float32
call_7961 = relay.TupleGetItem(func_2390_call(relay.reshape(const_7951.astype('float32'), [135,]), relay.reshape(var_7962.astype('float32'), [1089,]), ), 3)
call_7963 = relay.TupleGetItem(func_2393_call(relay.reshape(const_7951.astype('float32'), [135,]), relay.reshape(var_7962.astype('float32'), [1089,]), ), 3)
func_193_call = mod.get_global_var('func_193')
func_196_call = mutated_mod.get_global_var('func_196')
var_7980 = relay.var("var_7980", dtype = "uint16", shape = (1, 24))#candidate|7980|(1, 24)|var|uint16
var_7981 = relay.var("var_7981", dtype = "uint16", shape = (8, 30))#candidate|7981|(8, 30)|var|uint16
call_7979 = func_193_call(relay.reshape(var_7980.astype('uint16'), [1, 2, 12]), relay.reshape(var_7981.astype('uint16'), [10, 2, 12]), )
call_7982 = func_193_call(relay.reshape(var_7980.astype('uint16'), [1, 2, 12]), relay.reshape(var_7981.astype('uint16'), [10, 2, 12]), )
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_7983 = relay.TupleGetItem(func_2978_call(), 0)
call_7984 = relay.TupleGetItem(func_2980_call(), 0)
bop_7993 = relay.right_shift(call_7950.astype('uint32'), relay.reshape(const_7951.astype('uint32'), relay.shape_of(call_7950))) # shape=(5, 3, 9)
bop_7996 = relay.right_shift(call_7952.astype('uint32'), relay.reshape(const_7951.astype('uint32'), relay.shape_of(call_7952))) # shape=(5, 3, 9)
uop_7999 = relay.log10(var_7981.astype('float32')) # shape=(8, 30)
output = relay.Tuple([call_7890,call_7961,var_7962,call_7979,var_7980,call_7983,bop_7993,uop_7999,])
output2 = relay.Tuple([call_7891,call_7963,var_7962,call_7982,var_7980,call_7984,bop_7996,uop_7999,])
func_8013 = relay.Function([var_7962,var_7980,var_7981,], output)
mod['func_8013'] = func_8013
mod = relay.transform.InferType()(mod)
mutated_mod['func_8013'] = func_8013
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8013_call = mutated_mod.get_global_var('func_8013')
var_8015 = relay.var("var_8015", dtype = "float32", shape = (1089, 1))#candidate|8015|(1089, 1)|var|float32
var_8016 = relay.var("var_8016", dtype = "uint16", shape = (1, 24))#candidate|8016|(1, 24)|var|uint16
var_8017 = relay.var("var_8017", dtype = "uint16", shape = (8, 30))#candidate|8017|(8, 30)|var|uint16
call_8014 = func_8013_call(var_8015,var_8016,var_8017,)
output = call_8014
func_8018 = relay.Function([var_8015,var_8016,var_8017,], output)
mutated_mod['func_8018'] = func_8018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_8026 = relay.TupleGetItem(func_2978_call(), 1)
call_8027 = relay.TupleGetItem(func_2980_call(), 1)
func_4299_call = mod.get_global_var('func_4299')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_8028 = relay.TupleGetItem(func_4299_call(), 0)
call_8029 = relay.TupleGetItem(func_4300_call(), 0)
output = relay.Tuple([call_8026,call_8028,])
output2 = relay.Tuple([call_8027,call_8029,])
func_8059 = relay.Function([], output)
mod['func_8059'] = func_8059
mod = relay.transform.InferType()(mod)
output = func_8059()
func_8060 = relay.Function([], output)
mutated_mod['func_8060'] = func_8060
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5412_call = mod.get_global_var('func_5412')
func_5413_call = mutated_mod.get_global_var('func_5413')
call_8066 = func_5412_call()
call_8067 = func_5412_call()
output = call_8066
output2 = call_8067
func_8068 = relay.Function([], output)
mod['func_8068'] = func_8068
mod = relay.transform.InferType()(mod)
output = func_8068()
func_8069 = relay.Function([], output)
mutated_mod['func_8069'] = func_8069
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7444_call = mod.get_global_var('func_7444')
func_7445_call = mutated_mod.get_global_var('func_7445')
call_8093 = relay.TupleGetItem(func_7444_call(), 1)
call_8094 = relay.TupleGetItem(func_7445_call(), 1)
const_8101 = relay.const([[1.854158,-1.109959,-2.024616,-0.785714,-1.766868,9.989284,7.641508,-5.997317,-1.528451,-9.102705,6.134135,7.512804,-8.963683,0.996569,0.839351,3.407050,4.819500,-4.438233,8.448924,-9.134789,3.778764,8.224254,9.136565,-5.857211,7.703310,-2.179602,4.363295,-2.914384,5.243679,-5.742321,6.368541,7.723663,7.987942,-6.375401,-5.393295,6.313624,3.206728,-9.986905,-9.380082,-8.325777,6.408714,-0.492108,-5.449601,-1.771946,-8.436333,-5.269041,-9.215422,-8.410712,5.256767,-4.092206,9.757971,2.960006,2.600472,7.923252,-4.083409,6.418606,-1.423277,-9.871324,-4.692487,-6.384692,9.012700,-7.974612,-8.043574,-8.855412,-7.663010,4.578908,-7.342508,-3.784029,-8.207022,9.807562,2.705557,4.987509,-6.992663,-5.142931,-6.352979,3.306328,0.248930,-2.503472,-8.065784,7.738480,5.148666,-8.233252,8.053499,5.990770,-1.538608,-4.408872,7.462711,-9.704301,5.936505,5.184491,4.061738,-8.982964,-1.389162,0.110177,9.016084,6.749935,1.863518,-5.702882,-9.786401],[2.102525,-2.833717,-0.261876,8.297811,5.458262,7.292600,-9.136246,8.384195,3.180240,3.915202,-1.797333,3.988804,-6.717034,4.311715,4.170619,-9.006390,-0.073962,-0.913723,1.798100,6.404249,6.241571,6.783691,-0.955459,-4.025922,-2.398077,-3.207129,-5.727543,2.659120,-1.224104,4.147113,-9.729581,-7.626673,-1.785809,-7.479767,-1.884138,-0.339284,-2.980950,-2.594663,-5.014680,1.361594,-7.209668,9.535352,9.265215,0.218891,1.521019,-3.373866,2.041444,-0.700368,7.255554,6.841633,6.749827,8.459364,4.295145,-7.558032,-8.467368,-9.954339,9.377002,0.070622,-5.655979,-5.007092,3.501855,-9.172014,-3.007780,-8.177104,3.366757,3.685637,1.540193,-5.310251,-6.554061,-4.274800,-4.570722,-8.491635,-0.193038,3.526347,-2.656070,-1.946178,-2.529325,-5.767472,-0.186597,-2.171097,-2.461195,-8.301217,8.926655,-1.123076,6.169518,-9.843423,-4.680437,9.339062,6.162482,5.711146,-4.799562,8.448052,-3.953052,1.499519,2.145435,-9.984459,-1.531191,1.490905,-1.454038],[4.448249,6.271487,0.792629,-0.351681,-9.237241,3.279436,-9.314436,-5.214564,-8.097252,1.432191,2.782874,-5.206093,9.236863,-9.045813,-2.200646,-2.451803,-3.675763,8.380389,9.645546,-2.481386,5.794494,-8.166766,9.119066,-1.045990,0.765291,-2.706209,-6.308699,7.343208,2.329078,-0.842887,-4.870537,9.856609,-5.535987,-7.644476,8.386592,-3.647172,1.839055,-0.871079,2.076817,-8.084774,-1.771356,7.638936,0.137379,-7.069465,-4.233474,-3.962224,-9.912013,8.305141,0.606481,-7.193928,-4.605040,0.206172,7.553053,-2.391403,-2.471393,-8.804867,4.891753,9.485727,-4.031154,9.518707,5.506280,1.656225,-4.267701,-4.392871,-8.908380,-5.017046,7.628528,-1.236683,2.095666,6.891661,-2.395608,-8.066488,5.143454,-8.390288,-7.003743,-5.530366,-1.156835,2.080418,-9.257774,-8.517684,-0.844634,1.721752,-2.556036,5.849633,8.397790,-4.380330,-2.233963,2.372621,-0.929697,9.873521,-8.853376,-9.034134,8.789991,5.314066,-5.713287,-8.004062,-6.748301,-4.639930,-7.340914],[-5.787217,1.953650,3.562717,2.050822,0.459154,-0.866764,-7.452731,2.174078,0.799581,-9.592093,-0.313436,-0.705595,-8.771790,2.327312,-2.306383,-9.258576,1.500222,3.924675,9.721759,9.270467,-4.959307,8.716303,-7.208467,-4.590768,0.305659,-6.458001,0.004205,-5.658476,9.605807,-6.594260,3.650009,-3.592914,-1.815418,5.612398,8.332027,5.302380,8.718947,-0.740640,1.443621,2.685360,-3.673769,-6.990337,7.951040,5.902033,-3.220633,-2.862252,-5.166926,-4.705465,-9.438374,-2.891350,4.633173,9.907673,-2.051918,-8.035887,-2.676238,-7.516923,-0.007767,-7.384755,4.616343,-7.555153,-9.819146,-6.864166,-8.330109,7.189148,-6.794443,-1.176006,0.455131,-8.525658,0.445464,4.341507,1.051729,-0.956248,2.033218,9.429537,-3.093040,-5.886312,-8.218874,4.633367,-7.382897,8.769358,-2.103923,-2.516677,0.619350,0.883905,2.412209,4.023830,-8.167122,-8.219763,-7.073238,7.961092,-0.178705,6.708365,-0.040506,3.481373,-3.015368,6.677503,-6.237618,-8.500507,7.859735],[-7.863624,3.640168,3.523650,-2.405144,9.924502,1.986722,7.317316,-0.069345,-0.273399,-2.942844,3.197596,-7.413945,4.061900,-0.845923,-5.874644,-9.036421,6.001673,-9.618080,1.889506,-7.458301,-1.055155,6.835024,0.637934,-7.526334,-4.300708,1.284407,0.992896,1.359103,-6.774951,9.889981,0.227457,-5.948816,5.869391,0.651853,2.616635,0.072038,1.647990,4.049654,-3.357714,-5.052463,-8.228759,6.602332,4.504350,6.960923,-0.645046,-8.927542,-3.293079,-8.938914,-7.357025,-9.139748,-3.680534,3.188989,0.604662,-7.892796,-1.192280,-1.744423,8.894049,5.436126,-9.066528,-4.939085,5.383040,-6.517777,4.659666,2.309866,-9.338912,8.811004,5.715491,-4.568329,-1.550430,-7.920189,3.002216,6.554357,-3.758685,6.459665,1.018012,-7.738838,6.847722,-1.979449,5.145936,-9.240765,-6.660609,-8.980885,-7.566215,-5.038678,-7.636011,8.475216,8.015514,-0.811672,9.023756,1.709933,9.981290,5.939560,-0.134600,-6.042657,8.482347,-3.906328,-5.366004,6.437721,6.192338],[7.188334,1.201933,-4.828573,-4.203138,-4.101526,-2.187445,-8.461245,2.470494,-9.761093,-5.402741,-7.125560,9.936532,2.023927,5.704692,-0.198880,-2.861171,-2.337910,9.283982,-9.565784,5.049973,8.648939,-9.545951,-1.507656,-8.087637,-3.730548,5.028020,-6.352178,6.531499,-8.707585,2.169768,5.308162,6.912171,6.736494,-0.862861,-3.030187,-2.085361,-7.788822,7.734425,8.900654,6.384554,-6.302220,-6.514440,-3.887420,-0.935256,-5.310381,4.244094,2.922298,-2.688770,6.756088,8.975450,-4.611490,-3.098212,-0.365153,3.692959,0.993048,6.464034,5.279381,-8.254150,7.364160,0.979036,-6.810130,-8.535881,3.286490,-4.564612,6.985647,-8.919048,-5.479746,-2.662005,-2.945264,-6.810478,5.414657,-8.223700,8.279115,-1.535189,3.164446,-8.272692,-7.328440,-7.409669,3.609604,9.631592,-4.566162,6.180544,-8.146126,4.046072,3.362406,-0.055441,-9.146061,-9.977144,5.850333,-7.209651,-7.547418,5.084572,3.149057,-2.599596,-3.729058,-3.285858,8.566408,9.082901,0.259401],[-6.138954,-6.567979,6.512926,2.687936,-4.606770,-9.410550,-0.945652,-6.786077,-4.588060,3.544672,-2.664391,-9.040866,-4.631942,-7.830460,7.060285,-8.213894,7.534126,-8.311760,0.992725,-1.882346,-3.215660,0.575163,9.611480,-3.811866,0.027361,-2.334916,-1.279999,-0.154139,-5.584296,-2.972600,3.314795,6.290231,-1.576324,2.316743,-2.171908,1.346787,3.198822,6.281847,-9.553985,-4.770658,5.933018,-2.992744,5.354585,-2.169461,5.436391,0.025688,9.960638,3.869693,-9.635976,-0.362874,-1.675077,2.405229,-0.220879,-2.605690,7.530204,-7.246186,6.444385,-9.928120,-6.411544,-0.246171,8.789178,-6.674010,0.080328,-1.888403,-4.724892,-0.504776,7.796576,-0.641846,-1.498468,-6.128393,7.689709,-2.958085,8.547926,0.686714,1.338656,-1.471884,8.352789,7.017531,-8.103521,-1.995671,-6.700993,-8.767656,8.959516,9.423707,5.757147,3.925387,1.028577,-7.436200,-9.851401,-7.382740,0.609599,-1.596897,7.518665,4.688743,-4.288530,-4.694185,-5.547615,-6.428973,-0.909266],[0.847938,5.883219,-3.802377,-0.906142,-3.613112,4.974152,-7.784363,5.887920,9.521477,4.952249,-8.861216,5.549822,-8.939496,1.116210,3.974044,4.531947,-7.785559,5.284939,3.367999,1.277549,-7.124351,-0.955299,7.154755,5.893133,-5.467297,-2.962279,-2.655273,8.821941,3.285514,9.315027,-7.631401,-1.042834,-1.258548,-9.939240,4.197072,7.443456,-4.253405,0.640549,3.132871,-0.295544,6.140576,-4.578579,-3.501049,-1.616787,5.625065,-8.653898,-8.481547,-1.067872,-6.051053,-5.546395,-2.720822,0.285265,9.369190,-9.708006,-3.557432,-1.687351,6.794556,8.007965,1.047582,-6.417166,-5.183319,-0.532767,8.198990,8.450985,6.616261,8.674365,6.265684,-3.675816,9.960475,9.913648,-7.968751,4.643573,-7.862672,3.525935,6.851532,-3.798442,7.329040,-3.140176,8.102260,-2.755039,-4.584701,-5.029226,3.440039,-6.015838,-5.830694,-9.294709,-2.757842,-5.345239,-3.822153,-3.375882,9.866351,4.501430,5.936607,6.350429,3.445825,-8.881305,-2.955998,2.987882,7.568814],[-9.766448,8.846008,-9.370914,0.449692,7.478544,5.290583,6.280973,-8.403850,2.917578,-3.679419,8.352087,-5.213995,1.960239,-1.100753,-1.176281,5.856014,8.228891,6.395925,-6.622092,7.627743,0.471061,6.012997,7.478232,2.622163,1.424684,-3.941853,-6.109804,-0.431586,2.313187,-8.357802,0.630813,-2.015380,1.563577,-8.571008,-0.342919,3.918469,-0.947221,-3.674698,-0.619408,-4.419193,-0.804369,-5.799550,-6.800939,-5.785954,-6.023656,7.674055,-4.782874,-9.822529,-3.251017,8.532488,-5.459354,-1.099526,1.847811,2.441651,-5.482553,-8.936783,-0.859770,0.790456,1.222071,-5.417177,4.766247,9.421043,9.426738,6.267414,8.519725,1.583295,9.955346,-5.315148,-3.120716,-2.030518,-9.706152,7.768075,-5.311968,4.922492,0.223954,1.614835,0.943238,-5.473808,-1.888415,-4.585048,8.462611,-5.713791,5.117363,3.332504,-1.021536,6.210251,-9.516414,2.194120,8.408271,9.223660,-1.370008,1.564039,4.405603,-2.109020,3.306078,3.551329,-3.564543,8.560500,6.104330],[-0.590504,2.383949,-8.787030,-3.669100,-1.409222,-6.266221,-8.048536,-6.133368,-6.900916,-8.496415,5.929657,-8.167971,-8.103456,-3.966264,-0.883391,-1.977175,5.894372,-8.193260,-2.285795,8.998345,3.272046,-5.762481,-3.312853,2.755559,-0.635570,-3.236199,-8.074477,5.349307,4.291540,-6.905025,8.330097,-9.506008,-1.693990,-0.254379,-3.329609,8.475154,1.563576,0.099212,-0.374462,-4.787598,-9.515546,1.288322,7.562801,7.378129,-3.592302,7.183521,9.657930,3.405016,-6.666586,-5.567053,1.804760,-7.303451,8.941845,7.147903,0.732554,-3.701061,-7.564081,-7.402816,-4.519599,-3.908472,1.748454,-4.510269,-6.725164,7.775511,3.511998,3.830170,0.698396,3.321760,4.786567,4.871489,3.831173,2.560805,3.873412,3.261714,7.469965,-8.191541,6.709780,4.482393,-1.364772,1.113262,-5.551869,0.566139,-9.418473,-8.025553,9.772436,-1.436500,-8.298172,-2.934651,6.800877,9.388964,9.209130,-5.907185,2.516173,-3.406549,-8.772922,8.140492,-9.999438,-6.760326,-9.229391],[2.640859,-7.043699,-9.824608,6.496895,-7.313426,-8.981343,3.012905,-7.045930,8.242195,-4.652337,1.321142,3.733263,3.386966,9.674236,-1.109743,6.726786,8.514425,-8.163661,-2.083437,-7.288665,-2.872954,-7.144492,0.531323,0.885574,-2.321062,-7.185415,-0.483942,1.268151,-7.682552,-9.845717,-9.951681,-1.945584,9.613142,4.279121,-9.342008,3.372661,-1.613584,-6.526932,-2.378003,-7.801070,9.957559,-9.407458,-2.208096,-3.639409,3.679113,-8.755130,-4.036541,8.255922,9.254298,4.688401,4.237120,-7.156179,-8.619906,4.733362,3.052170,-3.429602,-8.859891,-4.574859,-1.399439,0.913890,0.973335,5.492341,-2.105604,-5.266283,2.962802,0.422440,-5.310021,-1.448349,1.776890,9.022191,-0.228431,8.858444,-9.873081,6.407044,-7.250403,-7.626669,-8.922951,6.727434,3.938358,-4.391890,9.014244,1.257753,-2.606259,3.829933,3.868553,-1.387488,-0.502404,-4.699654,0.522575,4.465058,8.416321,-3.713829,2.603522,-0.266824,9.800621,5.298967,2.403078,-5.452897,-9.445706]], dtype = "float32")#candidate|8101|(11, 99)|const|float32
bop_8102 = relay.greater(call_8093.astype('bool'), relay.reshape(const_8101.astype('bool'), relay.shape_of(call_8093))) # shape=(11, 99)
bop_8105 = relay.greater(call_8094.astype('bool'), relay.reshape(const_8101.astype('bool'), relay.shape_of(call_8094))) # shape=(11, 99)
var_8113 = relay.var("var_8113", dtype = "float32", shape = (11, 99))#candidate|8113|(11, 99)|var|float32
bop_8114 = relay.multiply(call_8093.astype('int8'), relay.reshape(var_8113.astype('int8'), relay.shape_of(call_8093))) # shape=(11, 99)
bop_8117 = relay.multiply(call_8094.astype('int8'), relay.reshape(var_8113.astype('int8'), relay.shape_of(call_8094))) # shape=(11, 99)
output = relay.Tuple([bop_8102,bop_8114,])
output2 = relay.Tuple([bop_8105,bop_8117,])
func_8121 = relay.Function([var_8113,], output)
mod['func_8121'] = func_8121
mod = relay.transform.InferType()(mod)
var_8122 = relay.var("var_8122", dtype = "float32", shape = (11, 99))#candidate|8122|(11, 99)|var|float32
output = func_8121(var_8122)
func_8123 = relay.Function([var_8122], output)
mutated_mod['func_8123'] = func_8123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2507_call = mod.get_global_var('func_2507')
func_2509_call = mutated_mod.get_global_var('func_2509')
call_8230 = relay.TupleGetItem(func_2507_call(), 0)
call_8231 = relay.TupleGetItem(func_2509_call(), 0)
func_6216_call = mod.get_global_var('func_6216')
func_6219_call = mutated_mod.get_global_var('func_6219')
call_8240 = relay.TupleGetItem(func_6216_call(relay.reshape(call_8230.astype('float32'), [6, 16, 11])), 3)
call_8241 = relay.TupleGetItem(func_6219_call(relay.reshape(call_8230.astype('float32'), [6, 16, 11])), 3)
output = relay.Tuple([call_8230,call_8240,])
output2 = relay.Tuple([call_8231,call_8241,])
func_8249 = relay.Function([], output)
mod['func_8249'] = func_8249
mod = relay.transform.InferType()(mod)
mutated_mod['func_8249'] = func_8249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8249_call = mutated_mod.get_global_var('func_8249')
call_8250 = func_8249_call()
output = call_8250
func_8251 = relay.Function([], output)
mutated_mod['func_8251'] = func_8251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5970_call = mod.get_global_var('func_5970')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_8285 = relay.TupleGetItem(func_5970_call(), 0)
call_8286 = relay.TupleGetItem(func_5972_call(), 0)
var_8298 = relay.var("var_8298", dtype = "float64", shape = (2, 11, 12))#candidate|8298|(2, 11, 12)|var|float64
bop_8299 = relay.subtract(call_8285.astype('uint64'), relay.reshape(var_8298.astype('uint64'), relay.shape_of(call_8285))) # shape=(2, 11, 12)
bop_8302 = relay.subtract(call_8286.astype('uint64'), relay.reshape(var_8298.astype('uint64'), relay.shape_of(call_8286))) # shape=(2, 11, 12)
func_2978_call = mod.get_global_var('func_2978')
func_2980_call = mutated_mod.get_global_var('func_2980')
call_8304 = relay.TupleGetItem(func_2978_call(), 0)
call_8305 = relay.TupleGetItem(func_2980_call(), 0)
func_7030_call = mod.get_global_var('func_7030')
func_7032_call = mutated_mod.get_global_var('func_7032')
call_8306 = relay.TupleGetItem(func_7030_call(), 1)
call_8307 = relay.TupleGetItem(func_7032_call(), 1)
uop_8309 = relay.erf(call_8285.astype('float32')) # shape=(2, 11, 12)
uop_8311 = relay.erf(call_8286.astype('float32')) # shape=(2, 11, 12)
uop_8312 = relay.log10(uop_8309.astype('float64')) # shape=(2, 11, 12)
uop_8314 = relay.log10(uop_8311.astype('float64')) # shape=(2, 11, 12)
func_1705_call = mod.get_global_var('func_1705')
func_1707_call = mutated_mod.get_global_var('func_1707')
call_8318 = relay.TupleGetItem(func_1705_call(), 0)
call_8319 = relay.TupleGetItem(func_1707_call(), 0)
output = relay.Tuple([bop_8299,call_8304,call_8306,uop_8312,call_8318,])
output2 = relay.Tuple([bop_8302,call_8305,call_8307,uop_8314,call_8319,])
func_8320 = relay.Function([var_8298,], output)
mod['func_8320'] = func_8320
mod = relay.transform.InferType()(mod)
mutated_mod['func_8320'] = func_8320
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8321 = relay.var("var_8321", dtype = "float64", shape = (2, 11, 12))#candidate|8321|(2, 11, 12)|var|float64
func_8320_call = mutated_mod.get_global_var('func_8320')
call_8322 = func_8320_call(var_8321)
output = call_8322
func_8323 = relay.Function([var_8321], output)
mutated_mod['func_8323'] = func_8323
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8411 = relay.var("var_8411", dtype = "int32", shape = (3, 6, 11))#candidate|8411|(3, 6, 11)|var|int32
const_8412 = relay.const([[[-6,-10,9,-5,-7,5,2,1,10,7,9],[-4,5,-10,6,7,-7,10,6,-8,2,5],[7,-3,9,4,-6,-9,-2,8,-5,10,3],[-9,-5,-1,2,10,-5,-4,-3,-2,-7,-1],[-2,-7,-3,10,-8,4,5,10,-3,-7,-5],[5,-9,8,10,7,8,8,2,7,6,-3]],[[9,6,-6,-2,-6,-9,-4,3,8,-5,-5],[-8,-2,8,8,-8,-7,-1,-9,-5,2,10],[-3,-1,6,-7,-10,9,-2,1,-10,-7,3],[-9,-2,7,-8,-9,1,-2,-5,-7,4,8],[-5,-5,8,-10,-1,3,-5,7,-7,-6,8],[5,-9,-10,-10,-10,-7,-10,9,6,-2,3]],[[-9,-1,-1,-5,7,2,-4,-10,3,1,-4],[-5,-2,-3,9,-2,-8,-5,1,8,1,5],[-4,-2,-6,-7,4,1,4,-8,10,3,2],[9,-9,-3,-8,-6,5,9,10,2,-9,-10],[9,-10,-10,8,-3,7,-5,4,1,6,-9],[9,-3,3,-6,-7,-1,-5,-9,2,4,-4]]], dtype = "int32")#candidate|8412|(3, 6, 11)|const|int32
bop_8413 = relay.right_shift(var_8411.astype('int32'), relay.reshape(const_8412.astype('int32'), relay.shape_of(var_8411))) # shape=(3, 6, 11)
output = relay.Tuple([bop_8413,])
output2 = relay.Tuple([bop_8413,])
func_8416 = relay.Function([var_8411,], output)
mod['func_8416'] = func_8416
mod = relay.transform.InferType()(mod)
var_8417 = relay.var("var_8417", dtype = "int32", shape = (3, 6, 11))#candidate|8417|(3, 6, 11)|var|int32
output = func_8416(var_8417)
func_8418 = relay.Function([var_8417], output)
mutated_mod['func_8418'] = func_8418
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4299_call = mod.get_global_var('func_4299')
func_4300_call = mutated_mod.get_global_var('func_4300')
call_8441 = relay.TupleGetItem(func_4299_call(), 2)
call_8442 = relay.TupleGetItem(func_4300_call(), 2)
output = call_8441
output2 = call_8442
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
func_7556_call = mod.get_global_var('func_7556')
func_7558_call = mutated_mod.get_global_var('func_7558')
call_8456 = relay.TupleGetItem(func_7556_call(), 1)
call_8457 = relay.TupleGetItem(func_7558_call(), 1)
func_5152_call = mod.get_global_var('func_5152')
func_5153_call = mutated_mod.get_global_var('func_5153')
call_8458 = relay.TupleGetItem(func_5152_call(), 0)
call_8459 = relay.TupleGetItem(func_5153_call(), 0)
output = relay.Tuple([call_8456,call_8458,])
output2 = relay.Tuple([call_8457,call_8459,])
func_8465 = relay.Function([], output)
mod['func_8465'] = func_8465
mod = relay.transform.InferType()(mod)
mutated_mod['func_8465'] = func_8465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8465_call = mutated_mod.get_global_var('func_8465')
call_8466 = func_8465_call()
output = call_8466
func_8467 = relay.Function([], output)
mutated_mod['func_8467'] = func_8467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mod.get_global_var('func_3191')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_8477 = func_3191_call()
call_8478 = func_3191_call()
output = relay.Tuple([call_8477,])
output2 = relay.Tuple([call_8478,])
func_8505 = relay.Function([], output)
mod['func_8505'] = func_8505
mod = relay.transform.InferType()(mod)
output = func_8505()
func_8506 = relay.Function([], output)
mutated_mod['func_8506'] = func_8506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_8507 = func_2138_call()
call_8508 = func_2138_call()
func_2951_call = mod.get_global_var('func_2951')
func_2954_call = mutated_mod.get_global_var('func_2954')
const_8519 = relay.const(3.801444, dtype = "float32")#candidate|8519|()|const|float32
var_8520 = relay.var("var_8520", dtype = "float32", shape = (121, 9))#candidate|8520|(121, 9)|var|float32
call_8518 = relay.TupleGetItem(func_2951_call(relay.reshape(const_8519.astype('float32'), []), relay.reshape(var_8520.astype('float32'), [1089,]), ), 3)
call_8521 = relay.TupleGetItem(func_2954_call(relay.reshape(const_8519.astype('float32'), []), relay.reshape(var_8520.astype('float32'), [1089,]), ), 3)
func_5950_call = mod.get_global_var('func_5950')
func_5954_call = mutated_mod.get_global_var('func_5954')
var_8525 = relay.var("var_8525", dtype = "float32", shape = (7, 1))#candidate|8525|(7, 1)|var|float32
var_8526 = relay.var("var_8526", dtype = "float64", shape = (2, 1))#candidate|8526|(2, 1)|var|float64
call_8524 = relay.TupleGetItem(func_5950_call(relay.reshape(var_8525.astype('float32'), [1, 7, 1]), relay.reshape(var_8526.astype('float64'), [1, 2]), ), 0)
call_8527 = relay.TupleGetItem(func_5954_call(relay.reshape(var_8525.astype('float32'), [1, 7, 1]), relay.reshape(var_8526.astype('float64'), [1, 2]), ), 0)
func_5070_call = mod.get_global_var('func_5070')
func_5072_call = mutated_mod.get_global_var('func_5072')
var_8537 = relay.var("var_8537", dtype = "uint16", shape = (2080,))#candidate|8537|(2080,)|var|uint16
call_8536 = relay.TupleGetItem(func_5070_call(relay.reshape(var_8537.astype('uint16'), [13, 10, 16])), 1)
call_8538 = relay.TupleGetItem(func_5072_call(relay.reshape(var_8537.astype('uint16'), [13, 10, 16])), 1)
func_2871_call = mod.get_global_var('func_2871')
func_2873_call = mutated_mod.get_global_var('func_2873')
call_8552 = func_2871_call()
call_8553 = func_2871_call()
bop_8561 = relay.minimum(var_8537.astype('float32'), const_8519.astype('float32')) # shape=(2080,)
func_5536_call = mod.get_global_var('func_5536')
func_5538_call = mutated_mod.get_global_var('func_5538')
call_8569 = relay.TupleGetItem(func_5536_call(), 0)
call_8570 = relay.TupleGetItem(func_5538_call(), 0)
output = relay.Tuple([call_8507,call_8518,var_8520,call_8524,var_8525,var_8526,call_8536,call_8552,bop_8561,call_8569,])
output2 = relay.Tuple([call_8508,call_8521,var_8520,call_8527,var_8525,var_8526,call_8538,call_8553,bop_8561,call_8570,])
func_8577 = relay.Function([var_8520,var_8525,var_8526,var_8537,], output)
mod['func_8577'] = func_8577
mod = relay.transform.InferType()(mod)
var_8578 = relay.var("var_8578", dtype = "float32", shape = (121, 9))#candidate|8578|(121, 9)|var|float32
var_8579 = relay.var("var_8579", dtype = "float32", shape = (7, 1))#candidate|8579|(7, 1)|var|float32
var_8580 = relay.var("var_8580", dtype = "float64", shape = (2, 1))#candidate|8580|(2, 1)|var|float64
var_8581 = relay.var("var_8581", dtype = "uint16", shape = (2080,))#candidate|8581|(2080,)|var|uint16
output = func_8577(var_8578,var_8579,var_8580,var_8581,)
func_8582 = relay.Function([var_8578,var_8579,var_8580,var_8581,], output)
mutated_mod['func_8582'] = func_8582
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3191_call = mod.get_global_var('func_3191')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_8614 = func_3191_call()
call_8615 = func_3191_call()
output = call_8614
output2 = call_8615
func_8637 = relay.Function([], output)
mod['func_8637'] = func_8637
mod = relay.transform.InferType()(mod)
mutated_mod['func_8637'] = func_8637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8637_call = mutated_mod.get_global_var('func_8637')
call_8638 = func_8637_call()
output = call_8638
func_8639 = relay.Function([], output)
mutated_mod['func_8639'] = func_8639
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5883_call = mod.get_global_var('func_5883')
func_5884_call = mutated_mod.get_global_var('func_5884')
call_8650 = relay.TupleGetItem(func_5883_call(), 3)
call_8651 = relay.TupleGetItem(func_5884_call(), 3)
func_8013_call = mod.get_global_var('func_8013')
func_8018_call = mutated_mod.get_global_var('func_8018')
const_8657 = relay.const([-9.429138,2.129852,-2.100990,4.984850,-0.821732,-4.378868,5.459562,-3.160877,5.494083,5.894607,-7.200889,-5.065372,-8.680069,8.444776,-1.723097,-6.493951,-6.735013,0.336777,-7.351287,1.466681,-3.234322,-5.922068,-2.349810,-9.707197,-5.792398,3.285541,-0.419351,-2.380379,-1.639284,-2.062692,-5.017563,5.448683,-2.036931,5.063504,8.711217,-2.636696,-7.385413,6.882900,0.105852,-8.367940,-9.989682,-2.986684,1.115685,1.298546,-0.403792,2.117397,-0.856203,-5.750772,4.840326,-0.799401,-4.708016,-5.623174,4.744500,2.042452,-5.029153,1.671926,-3.716609,6.922775,-1.612980,8.148534,-5.381840,7.580793,-4.593160,1.293432,5.156144,-0.587401,-2.335057,8.226287,1.069432,-9.972381,-9.541190,-2.000094,-0.846944,3.524168,-0.398644,4.519130,9.064680,7.746925,-7.066653,9.152187,-4.484354,6.238912,-5.997376,6.843412,-3.400148,7.740358,6.845293,7.381177,7.920236,-2.775818,4.224971,-6.726372,-2.696418,-2.152476,4.439614,-0.424755,-9.255079,-9.342430,-4.403451,-5.245457,-8.285295,-1.553573,2.264956,8.250652,-9.461782,-8.052541,5.301899,-8.238765,-3.803858,3.240098,-8.569706,-3.226546,2.784954,4.362887,-5.415485,-2.789609,-5.902732,-0.649869,-4.330649,-5.087519,6.241319,4.548745,-8.446813,-5.419041,-9.575778,-7.711950,0.163315,9.572410,7.524791,7.704468,-8.513194,-9.752763,-3.032575,-8.447791,-2.455766,0.785417,8.229194,0.587373,-2.811922,2.629219,9.880815,7.227476,-5.968893,7.943306,2.690764,1.761892,1.333222,-5.367872,-4.458115,-1.030514,-4.763781,-4.531104,-7.110105,9.204335,8.453984,-7.268104,-2.595510,2.627593,-1.402974,-3.617895,6.827921,-7.814386,-1.706911,-2.913606,3.062080,4.660335,-6.616666,-9.491956,5.912356,7.174192,-3.585464,9.564609,6.596199,9.460957,-2.996982,-1.741258,1.107686,-8.748193,7.299740,-4.568016,6.917273,-3.711973,9.610365,2.719802,-9.550918,7.301589,-0.236939,1.855137,3.269746,4.433270,9.960793,-3.749376,-9.852880,-7.319846,7.938880,1.370975,-7.393902,2.420503,-5.442483,5.364289,6.250466,7.301032,9.320523,-8.322134,1.228186,-8.340366,8.506764,0.884522,3.529532,9.683267,-0.399470,-9.054371,7.635218,-7.168194,-1.480332,-4.210581,-8.230592,5.095307,9.364748,-2.970023,4.789137,0.490051,0.074642,6.468285,-1.888743,-9.572975,3.238150,7.819100,-9.828606,-0.587282,7.331008,-2.005321,-6.430061,-5.084297,6.006099,-5.613918,7.738935,5.663592,-9.070576,-8.382428,-4.065097,4.775245,0.700787,-2.981538,-4.968574,-0.414296,0.227707,2.607637,-0.185849,5.368869,-3.974253,-6.038945,5.141248,2.119787,-2.676621,-7.288273,-3.428113,-4.962579,8.561180,2.329992,4.661299,9.236900,-6.559547,-8.727090,-4.340673,1.608072,8.210520,0.728372,6.235875,-8.806213,-6.791140,-9.384205,-7.061536,-9.366818,8.030728,8.568648,3.857084,-1.952943,6.622845,-3.149610,-6.726129,7.986780,0.301121,6.886051,3.730165,6.419246,-0.299679,-0.341609,-2.870675,-6.928765,-5.187443,0.767930,2.498211,3.953438,-1.682244,-2.353617,7.214154,6.541414,-3.189235,-3.469558,-2.997357,7.880152,9.966853,-1.839514,-0.127068,-0.836938,-0.529730,-7.190542,9.632076,9.313452,1.017581,-9.141574,9.794797,-0.255621,-4.587664,0.819010,-3.473830,-0.843394,-7.078688,0.015551,9.604433,3.587674,4.455582,5.874690,8.528374,5.758428,1.193988,-6.057627,7.967063,-9.913192,4.802756,-8.782456,4.709652,7.751195,1.252801,-7.891953,-5.761938,7.456217,-6.597514,-1.001443,7.115764,-1.145402,-2.507007,9.296440,0.396533,4.503782,9.622591,-8.318069,-5.172049,-8.333347,0.657179,1.915025,-5.983384,2.683512,4.833615,-7.657127,0.497083,3.456183,0.635435,5.778369,4.480216,5.582960,1.234935,5.297807,-9.330639,5.783954,-8.911910,8.089714,4.895394,6.208194,5.558872,0.105185,7.573395,-2.313663,9.173447,8.877272,-0.734095,4.644599,2.690522,-5.294701,-5.876864,3.833188,-6.551805,2.544831,2.907887,-0.835294,2.618155,-3.154654,3.435447,4.433907,-9.603262,4.065148,-5.601950,-2.365351,6.866562,0.011745,0.942590,-3.719553,1.993928,8.346130,0.406690,6.555452,-7.896282,9.402610,-1.930394,-0.695630,4.194469,-2.371140,6.574596,4.394249,1.643374,-4.261521,8.052322,-9.656195,7.904788,-0.005505,2.574702,4.885954,2.592275,5.640439,1.259215,-0.554237,6.724605,-9.278059,-4.994947,6.900403,-5.435202,-4.566270,3.970184,6.491427,-6.879889,7.283330,8.480068,8.984211,5.656185,1.092663,8.904136,7.228469,-1.528403,6.319066,-2.768577,-9.535528,-7.002621,-5.170570,7.505898,-0.066409,6.810452,4.999368,-4.933385,9.402189,-2.001148,9.441808,6.222803,-5.153656,-8.333213,-6.687600,4.066324,-9.546273,9.022409,2.350755,-9.820601,-6.683861,0.685480,-2.458760,4.807420,5.660195,-9.703633,3.685072,0.452733,3.622970,0.359150,-7.905268,-4.634568,-7.011407,-5.586822,-9.640088,-7.236089,-9.225343,9.615558,9.816050,1.937805,-6.263977,1.784072,5.521377,9.410410,8.816020,-6.149692,3.241420,-3.984261,-6.250985,5.236166,3.238491,4.833898,6.579111,-8.868652,7.829832,4.825291,-2.130444,3.231663,-6.800457,-0.155293,4.454860,7.354544,-9.255218,3.108023,-5.391724,0.930780,-4.756188,-6.187430,7.845657,-5.457982,-1.187720,-3.714716,5.826152,-6.818782,7.412409,4.409409,3.384309,5.832137,-9.823947,-7.839108,-5.578624,-0.850221,-8.049226,-9.321403,6.253537,9.122225,4.855340,-0.788707,5.526630,-7.940746,-9.148969,-1.416207,-2.162508,0.404512,-5.773095,-3.162925,5.648180,3.124725,7.792469,-7.466780,-4.863019,-7.434736,4.214929,-6.659798,0.521522,6.118570,-7.052666,5.251508,-1.825413,4.536263,-7.278801,8.411822,-6.332030,0.881678,-7.777813,1.662092,9.939411,-8.587590,-4.907794,-5.442349,9.682534,8.768205,3.767042,9.634874,3.130678,-5.747936,-5.915535,-3.581815,-3.005934,-1.608922,9.023162,5.526540,0.018410,7.573247,6.714802,0.932503,-2.131389,-3.543151,2.672089,7.949121,0.617448,-7.454113,7.825436,-2.034382,-4.513657,-7.786639,-3.478298,0.708958,-1.426254,-2.812873,-2.555903,-0.582726,-2.406527,-1.217931,-5.513462,4.514824,2.407081,2.841303,-4.253637,-2.573861,-5.759898,-6.108148,-4.123939,-7.686791,-1.408078,-1.616514,-9.935911,7.194877,-1.150861,-1.723257,6.076135,-4.026300,9.573172,2.801058,0.857256,5.508056,0.407909,3.967738,1.735432,-6.271912,-6.388053,-7.802953,7.087999,0.111911,6.606505,3.248876,1.026052,4.591196,6.659325,-9.971118,-5.546264,2.161282,6.775723,7.951133,-1.206058,4.457482,6.696812,-7.937356,6.646617,-2.764855,7.222889,-0.538568,1.022286,-0.089573,-9.123267,0.560241,-2.627112,-5.285136,7.829838,-4.007626,0.932170,-3.426232,4.228333,-2.706984,3.174558,7.590070,-9.142214,6.519509,2.201714,-8.477261,8.532455,-3.608447,-2.237952,6.750854,-1.375774,-3.711535,3.277081,-3.328217,5.839351,-7.793499,4.482673,8.094438,9.780634,9.201078,-2.802499,-5.850596,-3.169214,9.556348,-1.130624,-1.168919,-6.152664,-2.930050,-4.642008,-4.995418,3.130117,-8.397797,-4.136029,-2.991532,-2.303003,-1.083503,-2.187238,-1.843395,2.287349,9.378279,6.547092,5.501272,-6.577681,7.668383,-5.458937,-4.432787,-8.401526,8.052707,9.107486,-3.340476,9.339561,-8.767349,-3.403323,-3.099384,8.494070,6.198905,-1.982455,-3.189827,-2.924379,8.610711,-7.790058,0.996134,-3.433662,2.141400,-8.566896,7.259949,0.909203,4.996072,0.307467,8.588622,-9.584407,8.203772,6.703048,5.731909,3.320382,8.393324,1.356073,7.469345,2.814264,7.299825,-2.602343,4.567766,-2.855486,5.193289,0.029421,-0.071195,5.611349,-8.888715,-7.210742,3.327537,-9.858758,3.960429,8.504624,0.997819,9.252250,-7.579123,3.455623,6.921045,0.050287,5.900384,-8.813257,-3.578949,2.332769,-1.052536,-4.539530,-7.662023,-7.152134,-7.741655,-8.111874,-3.952996,-7.815732,6.463412,7.062225,-7.219341,-2.784129,7.161751,3.907594,-3.554916,-6.126968,-9.894469,-4.093424,8.952875,-6.755519,-0.489351,7.108905,1.046531,-1.709799,0.401745,1.308487,-3.781377,-6.315771,-9.251323,9.374102,-0.818325,-6.274432,-1.713809,0.719683,4.360674,-7.966962,-5.289876,7.816810,8.904267,9.531109,8.240300,-7.962259,-0.521547,5.415481,5.439441,5.631599,-5.962267,-3.761890,9.453978,-0.456956,-9.451808,-1.158296,-5.648346,-2.775063,6.074944,-7.010510,-7.166912,-9.704914,7.684954,-9.122135,-3.097229,4.824465,4.587542,-1.218617,2.486055,1.942671,9.596754,8.003522,7.785326,2.918105,2.466392,1.016628,4.202735,-6.360405,7.993055,4.502865,-3.165562,-7.405723,-6.723152,-1.488582,0.298186,7.317559,-7.098429,-6.030885,-5.191746,-3.411478,-9.998250,-0.886641,-7.719159,-3.826873,8.017189,6.708828,-8.729745,8.463310,-0.118934,1.509205,6.241243,-2.710942,7.095145,-2.745735,7.859252,7.769541,-3.302992,4.015754,-4.365651,8.576656,5.788119,7.434595,-4.993152,-3.040917,4.862544,6.931469,1.863628,-8.347694,-7.701052,-3.621543,1.732575,8.468802,9.429800,-1.818157,8.731851,4.234183,8.823029,-2.961702,0.008769,-6.340462,-5.204984,-0.830309,-7.410730,-8.962795,2.864974,-3.486545,-0.506132,-3.804711,-8.612445,9.925871,-2.811396,-9.628687,-0.801672,-3.463942,1.573282,-4.012352,-8.920735,9.968149,9.977089,3.422981,0.447480,6.190288,-9.827924,9.852153,3.664480,-7.190548,-5.051384,2.899938,7.664114,-8.528438,-2.386501,9.340316,5.780836,7.554335,-5.020088,6.420533,-4.043625,-0.677186,5.144250,1.217330,-9.307186,-2.460957,-7.440079,8.275065,4.567839,8.020016,-5.106457,-3.638262,8.308650,-1.366063,3.915615,9.738353,2.502768,-6.822672,-4.551511,1.958437,3.309113,9.586794,0.969814,4.619709,-1.348183,-9.211014,7.176916,5.712070,8.693447,6.522879,1.595187,-8.904561,-0.208651,1.213862,9.205244,8.095442,1.254056,-8.167232,-3.581593,0.736013,-3.363450,6.665919,1.360622,4.393301,7.930500,3.293103,0.127161,4.871639,-3.385986,-0.888796,4.500181,-4.937162,-8.385376,6.811297,-8.454799,-1.385020,-5.879242,3.721873,-3.969220,-1.735757,8.736728,-8.459625,-2.676885,-4.541733,9.189469,-7.266159,-9.466310,8.620487,5.806671,9.447054,0.629040,2.022635,-1.788159,1.711085,5.849881,-4.984649,7.659215,1.724614,-6.687075,-4.721306,7.887993,-5.256545,8.648459,-8.588563,-8.242200,5.162114,3.737008,7.973943,6.139746,-7.748573,8.283785,2.738107,-5.630258,-8.627802,-7.576579,-6.735193,4.317611,9.093493,-3.007179,2.901925,-4.716214,-3.847938,9.797709,3.804850,9.197161,6.799647,-3.992776,5.990565,-2.604101,6.042174,3.374577,-0.063670,-1.239880,2.003434,7.368544,8.089658,8.653674,-1.932864,9.357789,1.610022,7.133293,7.223119,3.774408,-0.830205,-8.495369,-0.256029,9.723502,-9.455120,4.055013,-7.207982,1.271075,-1.613465,-6.213600,0.551739,-5.873473,-1.738857,-4.629372,7.196324,-0.103838,0.843321,2.993587,-6.671814,-6.428164,-2.878864,0.958403,-0.180048,-2.543057,6.993509,8.945264,-0.653334,-7.424712,-4.135457,5.528468,-7.913411,1.963117,-6.982419,-1.005528,-9.616459,-8.228403,-8.729044,4.240125,-2.260705,3.113916,-5.713353,-5.990725,-7.526400,4.254578,9.936886,-4.719254], dtype = "float32")#candidate|8657|(1089,)|const|float32
const_8658 = relay.const([-4,4,-10,2,2,10,1,2,8,4,7,9,-6,7,7,-1,7,-6,2,10,6,-8,2,10], dtype = "uint16")#candidate|8658|(24,)|const|uint16
const_8659 = relay.const([4,-9,7,-4,-5,8,-2,3,-4,10,1,-4,2,-6,-7,-6,10,8,3,2,2,5,-5,-6,3,10,1,-10,1,-7,6,-1,-9,2,10,-9,3,6,10,4,-7,7,10,1,3,4,-1,6,6,1,1,8,-2,2,8,7,-10,-3,2,-6,4,-4,4,5,7,6,6,4,10,-3,-3,6,-5,-6,7,-1,1,-5,5,-3,-8,4,4,-5,5,-5,-8,-2,3,9,-1,10,6,-4,-9,-7,7,2,-9,-8,-5,-5,-5,8,-6,-8,7,-10,5,-8,-3,1,4,3,-10,-2,-5,8,3,-10,2,9,-7,-6,2,-5,9,-7,9,8,1,4,6,-10,9,9,9,3,-6,-6,-3,3,5,6,-10,-3,6,-10,1,-1,-7,2,-10,-10,3,5,7,9,10,7,-2,2,8,-10,10,-9,-6,3,-7,-4,-10,-10,9,-2,7,-8,10,6,-9,-8,2,8,-10,3,5,-10,6,-6,9,3,-7,-4,-2,6,-1,-2,6,10,-10,-5,-10,-4,5,3,-5,-10,9,1,8,-3,-2,1,-5,-5,-2,2,3,8,3,2,8,-2,7,8,-1,-4,6,-2,-6,3,-5,-2,10,-8,3,-3,-5,-10,8,-10], dtype = "uint16")#candidate|8659|(240,)|const|uint16
call_8656 = relay.TupleGetItem(func_8013_call(relay.reshape(const_8657.astype('float32'), [1089, 1]), relay.reshape(const_8658.astype('uint16'), [1, 24]), relay.reshape(const_8659.astype('uint16'), [8, 30]), ), 1)
call_8660 = relay.TupleGetItem(func_8018_call(relay.reshape(const_8657.astype('float32'), [1089, 1]), relay.reshape(const_8658.astype('uint16'), [1, 24]), relay.reshape(const_8659.astype('uint16'), [8, 30]), ), 1)
uop_8662 = relay.atan(const_8657.astype('float32')) # shape=(1089,)
output = relay.Tuple([call_8650,call_8656,const_8658,const_8659,uop_8662,])
output2 = relay.Tuple([call_8651,call_8660,const_8658,const_8659,uop_8662,])
func_8667 = relay.Function([], output)
mod['func_8667'] = func_8667
mod = relay.transform.InferType()(mod)
mutated_mod['func_8667'] = func_8667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8667_call = mutated_mod.get_global_var('func_8667')
call_8668 = func_8667_call()
output = call_8668
func_8669 = relay.Function([], output)
mutated_mod['func_8669'] = func_8669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3118_call = mod.get_global_var('func_3118')
func_3119_call = mutated_mod.get_global_var('func_3119')
call_8710 = relay.TupleGetItem(func_3118_call(), 0)
call_8711 = relay.TupleGetItem(func_3119_call(), 0)
output = call_8710
output2 = call_8711
func_8720 = relay.Function([], output)
mod['func_8720'] = func_8720
mod = relay.transform.InferType()(mod)
output = func_8720()
func_8721 = relay.Function([], output)
mutated_mod['func_8721'] = func_8721
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8837 = relay.var("var_8837", dtype = "float64", shape = (1, 9, 16))#candidate|8837|(1, 9, 16)|var|float64
uop_8838 = relay.sqrt(var_8837.astype('float64')) # shape=(1, 9, 16)
output = uop_8838
output2 = uop_8838
func_8843 = relay.Function([var_8837,], output)
mod['func_8843'] = func_8843
mod = relay.transform.InferType()(mod)
var_8844 = relay.var("var_8844", dtype = "float64", shape = (1, 9, 16))#candidate|8844|(1, 9, 16)|var|float64
output = func_8843(var_8844)
func_8845 = relay.Function([var_8844], output)
mutated_mod['func_8845'] = func_8845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6754_call = mod.get_global_var('func_6754')
func_6755_call = mutated_mod.get_global_var('func_6755')
call_8903 = relay.TupleGetItem(func_6754_call(), 0)
call_8904 = relay.TupleGetItem(func_6755_call(), 0)
output = relay.Tuple([call_8903,])
output2 = relay.Tuple([call_8904,])
func_8921 = relay.Function([], output)
mod['func_8921'] = func_8921
mod = relay.transform.InferType()(mod)
mutated_mod['func_8921'] = func_8921
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8921_call = mutated_mod.get_global_var('func_8921')
call_8922 = func_8921_call()
output = call_8922
func_8923 = relay.Function([], output)
mutated_mod['func_8923'] = func_8923
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8932 = relay.const([[[-3,10,9,6,10],[-4,2,7,10,3],[4,5,-6,4,-6],[-1,-7,2,8,6],[2,6,-1,9,3],[-7,-8,1,-1,-9],[8,-7,-2,-3,-9],[-10,-2,2,-9,5],[5,-9,6,6,-6],[6,4,3,4,-8]],[[-6,1,-5,1,6],[-6,-2,3,-6,7],[1,-10,-7,-4,-8],[4,-1,9,-10,9],[-8,8,-9,-10,-9],[9,-2,-8,1,-10],[4,-10,-8,10,1],[7,-2,3,-7,6],[-2,5,-5,3,-5],[-2,6,2,3,6]],[[-1,5,-10,-5,-1],[-3,8,-7,3,7],[-2,4,3,1,-10],[-9,-10,6,-5,6],[-4,1,9,4,-7],[-9,-2,-6,-1,-2],[-6,5,9,5,-10],[2,-2,-5,10,-10],[-2,7,-1,2,9],[-6,5,2,-1,-8]],[[10,7,2,2,3],[2,-10,-3,1,7],[-7,7,-4,-8,6],[10,-5,-7,-10,10],[2,1,8,-4,-7],[-10,-6,8,6,7],[-1,9,1,-2,4],[6,-3,-9,-1,1],[6,4,-8,1,10],[5,2,-7,9,-6]],[[3,-10,-1,7,-2],[1,10,9,2,2],[-8,3,-3,7,-4],[-9,-6,-3,-10,10],[1,-9,9,-8,1],[-2,1,1,8,7],[10,8,7,-3,-4],[-8,-4,-5,-6,-5],[5,6,-5,-9,4],[6,4,-9,7,-5]],[[-5,-7,9,-4,-7],[1,-6,-9,5,-7],[-3,-2,9,7,5],[1,4,-1,-10,-9],[-3,10,-9,-4,6],[-3,4,-8,-1,1],[7,-8,-9,-4,-3],[7,-3,-7,7,-7],[3,-2,7,2,-4],[-4,6,-2,10,-6]]], dtype = "int32")#candidate|8932|(6, 10, 5)|const|int32
var_8933 = relay.var("var_8933", dtype = "int32", shape = (6, 10, 5))#candidate|8933|(6, 10, 5)|var|int32
bop_8934 = relay.multiply(const_8932.astype('int32'), relay.reshape(var_8933.astype('int32'), relay.shape_of(const_8932))) # shape=(6, 10, 5)
uop_8938 = relay.sinh(bop_8934.astype('float32')) # shape=(6, 10, 5)
func_7609_call = mod.get_global_var('func_7609')
func_7611_call = mutated_mod.get_global_var('func_7611')
call_8947 = func_7609_call()
call_8948 = func_7609_call()
bop_8958 = relay.logical_xor(uop_8938.astype('uint8'), relay.reshape(bop_8934.astype('uint8'), relay.shape_of(uop_8938))) # shape=(6, 10, 5)
func_3035_call = mod.get_global_var('func_3035')
func_3038_call = mutated_mod.get_global_var('func_3038')
var_8962 = relay.var("var_8962", dtype = "float32", shape = (240,))#candidate|8962|(240,)|var|float32
call_8961 = relay.TupleGetItem(func_3035_call(relay.reshape(var_8962.astype('float32'), [24, 10])), 3)
call_8963 = relay.TupleGetItem(func_3038_call(relay.reshape(var_8962.astype('float32'), [24, 10])), 3)
output = relay.Tuple([call_8947,bop_8958,call_8961,var_8962,])
output2 = relay.Tuple([call_8948,bop_8958,call_8963,var_8962,])
func_8966 = relay.Function([var_8933,var_8962,], output)
mod['func_8966'] = func_8966
mod = relay.transform.InferType()(mod)
mutated_mod['func_8966'] = func_8966
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8966_call = mutated_mod.get_global_var('func_8966')
var_8968 = relay.var("var_8968", dtype = "int32", shape = (6, 10, 5))#candidate|8968|(6, 10, 5)|var|int32
var_8969 = relay.var("var_8969", dtype = "float32", shape = (240,))#candidate|8969|(240,)|var|float32
call_8967 = func_8966_call(var_8968,var_8969,)
output = call_8967
func_8970 = relay.Function([var_8968,var_8969,], output)
mutated_mod['func_8970'] = func_8970
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5990_call = mod.get_global_var('func_5990')
func_5992_call = mutated_mod.get_global_var('func_5992')
call_9015 = relay.TupleGetItem(func_5990_call(), 0)
call_9016 = relay.TupleGetItem(func_5992_call(), 0)
output = relay.Tuple([call_9015,])
output2 = relay.Tuple([call_9016,])
func_9025 = relay.Function([], output)
mod['func_9025'] = func_9025
mod = relay.transform.InferType()(mod)
output = func_9025()
func_9026 = relay.Function([], output)
mutated_mod['func_9026'] = func_9026
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9062 = relay.const([[[-7,-8,3,3,-8,2,-6,10,-4,2,9,-8,-1,-5,1],[8,2,-9,6,4,10,5,-7,-10,6,-8,5,1,6,-3],[-4,7,9,-3,-7,-10,5,10,10,4,9,1,5,4,-8],[10,-9,9,10,-4,-1,3,10,9,-3,-6,-2,-10,8,10],[-10,7,-7,7,8,-6,8,4,-3,7,-3,-8,-9,6,2],[-5,-6,2,-9,-1,-2,8,4,-7,-5,3,-7,-7,-1,6],[-8,-6,5,8,-6,-3,-5,6,2,-8,-10,-9,6,-5,-6],[2,4,-8,5,5,6,10,10,3,-1,-1,6,8,-5,-8],[-6,6,-6,8,-2,-3,-2,10,-8,6,-5,-10,8,-2,-1],[-7,-9,-6,9,8,-9,-8,3,5,-2,-3,-7,-8,1,9],[10,-10,8,6,1,7,-5,5,4,1,8,-2,9,1,4],[3,-5,-3,-8,-10,-4,-1,3,-9,5,-4,-6,-9,8,4]],[[-1,6,-7,-8,-1,-3,7,-4,-9,9,4,8,-2,4,6],[-4,2,-2,-10,-3,-1,5,-2,10,1,7,5,-5,2,-6],[5,7,9,-8,4,-1,-10,2,-5,-3,-4,-2,-8,5,-8],[10,1,3,-9,-1,2,7,-8,4,-3,-10,9,-5,2,-7],[-9,4,-4,-1,7,5,4,3,-1,5,-4,-1,8,-10,-4],[-9,-1,4,-1,8,9,-9,-3,4,9,-8,-4,-6,4,3],[2,-2,6,-8,-3,4,2,-4,6,-1,-7,6,7,-6,-9],[-1,-10,3,1,10,2,7,-7,-8,-10,6,7,1,-7,5],[3,-6,-10,-8,4,8,-3,-9,7,3,-4,7,4,-5,2],[-6,7,1,-3,-10,-8,-3,5,-3,-7,10,-7,5,4,10],[-2,-4,-8,-8,-3,-8,-9,1,-2,6,1,5,4,9,1],[-5,-6,2,1,7,-10,-4,7,-1,-2,-2,-5,-2,6,7]],[[1,-10,1,2,-4,8,5,3,1,-3,-10,-7,2,4,-9],[5,10,-6,9,-5,-7,9,4,6,-5,-8,1,-2,3,3],[6,1,-5,-9,4,-9,6,5,-9,5,7,1,-1,3,8],[7,5,-9,4,5,1,-1,10,-7,4,-3,7,10,-6,3],[10,9,7,-4,-6,-1,2,4,-5,-3,4,1,-9,-9,-8],[2,-2,1,-8,2,-5,1,-2,-1,5,-9,9,10,3,-4],[4,8,6,-7,8,8,-2,-3,3,3,-6,-7,-4,-5,-8],[9,5,-10,-9,-5,6,-2,-4,3,7,-7,2,-9,3,-5],[-3,5,-4,-2,3,1,3,-10,-6,-4,10,-9,-5,9,2],[-1,10,6,-4,-8,6,-8,3,-5,2,-4,-1,7,1,4],[-1,2,-4,7,7,-4,-5,1,2,-8,5,9,7,2,3],[5,2,7,-6,-1,-10,-3,9,4,1,-6,-6,-2,2,-2]],[[1,-8,3,-8,-10,1,6,-4,9,8,9,-6,-10,5,4],[6,-5,8,-2,8,-7,-1,-2,-10,2,-10,-4,6,-7,-6],[10,-6,-6,4,3,9,10,5,-6,4,-4,1,-3,2,1],[2,-9,8,-5,5,-4,-7,6,-10,-8,-10,-1,8,9,-5],[-7,-2,9,4,-4,-1,-5,5,-2,-2,9,3,-5,5,3],[6,9,8,10,2,-3,2,-5,7,-4,-10,-3,5,5,3],[10,-10,9,-4,2,-3,-1,2,2,3,-10,-10,-5,-10,3],[-8,5,9,-8,3,1,4,10,7,-7,7,3,-8,-2,-1],[-6,-7,9,-4,-1,6,2,-5,7,-4,4,2,9,-8,-2],[6,-7,6,-1,2,7,5,9,-10,5,3,-5,7,-6,-7],[-5,4,-7,10,3,9,2,-7,-7,-7,1,2,-4,-10,-5],[1,-9,3,-7,4,-7,-8,-9,7,-4,-6,6,-8,6,-3]],[[6,-2,8,1,-10,-5,-7,5,-2,2,9,-10,8,7,8],[7,-5,9,8,-1,4,-5,-1,-7,-5,8,8,10,5,-10],[-7,-7,7,6,-5,-4,-2,-1,1,7,-8,-1,4,10,9],[2,-8,8,2,-1,-2,-5,-5,-9,-4,-4,3,9,-7,5],[-1,-3,6,4,-7,7,1,-4,-8,-5,-1,-7,4,-10,-6],[-10,5,-6,5,1,7,1,-9,4,-10,-4,-8,3,-8,7],[-1,-1,-8,-7,6,-5,5,-1,-1,-6,6,1,-2,5,1],[-1,9,-7,8,-10,-2,-9,2,-3,-7,-5,-6,6,-3,7],[-7,6,-2,-2,9,-7,10,-7,-8,-5,-9,9,-7,5,-7],[3,1,-9,4,-5,7,3,-8,8,-1,2,-5,5,-5,3],[-3,6,-8,8,8,3,7,-3,-6,-2,5,-7,2,-2,4],[-1,-4,2,-3,3,8,-9,4,2,2,-9,8,9,9,9]],[[9,-2,-8,-4,-7,-4,-3,-9,-4,8,-5,-5,2,2,-5],[7,-10,6,5,9,-7,8,6,8,8,-6,-1,-3,6,4],[-6,-7,2,-2,-1,9,-4,7,-4,-7,-1,5,-5,4,-6],[3,9,-8,-3,-8,-1,-4,5,4,8,-4,-6,8,-9,-3],[1,9,-5,-3,-7,-5,-1,5,10,-7,-3,-5,2,-8,-8],[-8,-8,10,-3,-4,-5,3,5,2,-9,4,-2,9,-4,4],[10,10,-8,1,-3,-4,-3,-4,4,6,5,-7,8,-10,5],[-2,-6,2,3,5,-10,2,-5,4,2,-7,9,-5,-10,-9],[9,-9,-6,-6,6,-2,-2,2,1,-9,7,2,-9,-2,2],[-1,5,-3,-3,-7,-4,-7,-3,6,-6,-9,-2,-8,-7,-8],[-4,-1,1,7,7,-2,2,7,-2,-1,7,-3,10,8,4],[10,6,-6,-5,10,-8,3,4,9,-1,6,10,-7,-3,-10]],[[10,6,1,-3,-8,8,-7,-7,-1,9,-7,-1,4,-7,-2],[3,-7,10,-2,4,-7,-5,-5,5,1,9,-9,-2,10,-10],[-8,-6,4,3,-2,6,-1,-4,-7,2,3,3,6,2,9],[-8,-5,-2,-2,-6,1,-4,5,7,-6,-10,-4,8,-2,-4],[2,-6,8,-5,2,-7,-3,3,8,2,1,-3,-6,-5,-1],[9,-10,-10,2,1,9,5,6,4,10,-9,1,-7,3,7],[-8,-9,1,9,9,7,5,-1,-2,8,-4,-4,-9,2,-1],[-7,-3,-1,8,-8,-9,4,-9,-8,2,4,3,1,-8,-7],[9,-2,-2,9,-3,6,1,8,7,-2,2,-6,-3,8,-7],[-2,8,-3,7,10,-8,-3,-8,-1,-7,-5,7,3,-6,3],[3,-2,-9,3,6,7,-2,4,-1,5,8,-6,-1,6,9],[1,-5,7,7,-2,-3,-6,9,-7,5,-10,-3,-7,-7,-2]],[[-4,-10,-5,5,-5,6,7,-5,3,9,-5,10,-5,-10,4],[9,-4,-7,4,-2,8,-10,-1,-1,8,-2,-9,9,-1,-4],[-3,-3,2,8,9,-8,10,-3,-3,-7,6,-4,-4,-7,-5],[2,-6,5,-2,-5,-2,9,10,-7,8,-6,3,-7,4,-4],[9,-7,10,2,-4,4,-1,-2,-4,-4,10,7,1,-2,10],[-5,1,-3,-3,-4,3,5,-10,-2,3,-9,9,10,-9,-6],[10,5,3,-4,-2,-5,4,-6,-6,-1,8,6,3,9,8],[-9,9,10,2,10,10,-9,-7,9,5,4,9,1,4,5],[5,8,10,6,2,5,3,-6,-1,4,6,-9,8,8,2],[-3,7,-1,-1,-8,4,5,-9,10,10,6,-1,-3,-9,-10],[2,7,7,6,-6,-1,2,-10,6,3,-3,2,-5,5,-5],[4,10,-9,-1,5,1,-10,1,-6,-1,5,-7,9,1,6]],[[9,-3,3,-6,-9,4,8,-5,-5,7,7,9,8,-5,-2],[-5,5,9,-2,-2,7,-2,-9,5,-5,1,6,-7,-10,3],[5,2,-10,8,8,-4,8,-4,-1,5,3,10,-6,2,-9],[-7,-7,-6,1,-8,8,8,7,6,-10,4,7,-1,-10,8],[-1,8,3,4,10,5,-5,-7,-4,8,6,-5,5,5,-10],[5,-7,7,6,5,5,-7,2,1,-9,-8,-1,5,1,-1],[2,-10,10,-8,-1,4,3,-4,-7,1,-6,-8,-5,2,4],[7,-3,4,6,-10,5,3,-9,-4,-4,2,-7,-6,3,8],[-3,-3,2,10,9,7,7,-3,6,3,-4,9,-5,-4,3],[8,-9,-4,10,10,-5,-5,-6,-9,8,4,8,5,-8,-4],[3,9,-4,-4,9,4,-1,-6,-1,-3,10,-3,3,-2,1],[4,-7,-7,-7,3,-4,-10,8,-4,-5,-10,-6,-3,-2,-2]],[[2,-6,-2,-10,-1,7,-2,10,4,-10,3,-6,-10,-10,8],[5,9,-9,-2,1,1,-1,-4,-2,-7,1,-2,-10,8,7],[1,5,1,10,2,9,9,6,-10,-4,-3,-6,-2,7,4],[7,4,-7,8,10,-9,1,6,-1,-6,-3,10,3,-4,3],[4,7,-3,-3,-2,-9,2,10,9,-4,8,5,-5,-1,9],[-10,3,-1,2,7,6,4,8,-6,7,4,-7,5,-7,4],[-10,9,2,10,-5,-7,-3,-9,-6,7,-6,1,2,-5,2],[-7,4,6,5,1,2,-2,-10,7,-7,9,7,-7,6,8],[-1,-10,10,-4,-3,6,2,2,9,8,-4,-9,7,-10,8],[-2,-2,8,10,8,7,-9,-1,1,-10,6,-7,5,-1,-8],[-2,9,-5,-5,-1,10,-6,-6,-2,7,-7,-6,-7,8,-5],[-8,7,2,-6,-8,-1,-4,-7,-3,9,-9,-4,1,-5,1]]], dtype = "uint8")#candidate|9062|(10, 12, 15)|const|uint8
var_9063 = relay.var("var_9063", dtype = "uint8", shape = (10, 12, 15))#candidate|9063|(10, 12, 15)|var|uint8
bop_9064 = relay.bitwise_and(const_9062.astype('uint8'), relay.reshape(var_9063.astype('uint8'), relay.shape_of(const_9062))) # shape=(10, 12, 15)
output = bop_9064
output2 = bop_9064
func_9084 = relay.Function([var_9063,], output)
mod['func_9084'] = func_9084
mod = relay.transform.InferType()(mod)
mutated_mod['func_9084'] = func_9084
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9085 = relay.var("var_9085", dtype = "uint8", shape = (10, 12, 15))#candidate|9085|(10, 12, 15)|var|uint8
func_9084_call = mutated_mod.get_global_var('func_9084')
call_9086 = func_9084_call(var_9085)
output = call_9086
func_9087 = relay.Function([var_9085], output)
mutated_mod['func_9087'] = func_9087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8450_call = mod.get_global_var('func_8450')
func_8452_call = mutated_mod.get_global_var('func_8452')
call_9123 = func_8450_call()
call_9124 = func_8450_call()
func_2138_call = mod.get_global_var('func_2138')
func_2140_call = mutated_mod.get_global_var('func_2140')
call_9160 = func_2138_call()
call_9161 = func_2138_call()
output = relay.Tuple([call_9123,call_9160,])
output2 = relay.Tuple([call_9124,call_9161,])
func_9167 = relay.Function([], output)
mod['func_9167'] = func_9167
mod = relay.transform.InferType()(mod)
output = func_9167()
func_9168 = relay.Function([], output)
mutated_mod['func_9168'] = func_9168
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8450_call = mod.get_global_var('func_8450')
func_8452_call = mutated_mod.get_global_var('func_8452')
call_9193 = func_8450_call()
call_9194 = func_8450_call()
output = call_9193
output2 = call_9194
func_9198 = relay.Function([], output)
mod['func_9198'] = func_9198
mod = relay.transform.InferType()(mod)
mutated_mod['func_9198'] = func_9198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9198_call = mutated_mod.get_global_var('func_9198')
call_9199 = func_9198_call()
output = call_9199
func_9200 = relay.Function([], output)
mutated_mod['func_9200'] = func_9200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7877_call = mod.get_global_var('func_7877')
func_7878_call = mutated_mod.get_global_var('func_7878')
call_9206 = relay.TupleGetItem(func_7877_call(), 5)
call_9207 = relay.TupleGetItem(func_7878_call(), 5)
uop_9220 = relay.sigmoid(call_9206.astype('float32')) # shape=(104,)
uop_9222 = relay.sigmoid(call_9207.astype('float32')) # shape=(104,)
output = relay.Tuple([uop_9220,])
output2 = relay.Tuple([uop_9222,])
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
