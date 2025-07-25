import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_127 = relay.var("var_127", dtype = "float32", shape = (2, 12, 9))#candidate|127|(2, 12, 9)|var|float32
var_128 = relay.var("var_128", dtype = "float32", shape = (2, 12, 9))#candidate|128|(2, 12, 9)|var|float32
bop_129 = relay.not_equal(var_127.astype('bool'), relay.reshape(var_128.astype('bool'), relay.shape_of(var_127))) # shape=(2, 12, 9)
bop_147 = relay.minimum(var_128.astype('float64'), relay.reshape(var_127.astype('float64'), relay.shape_of(var_128))) # shape=(2, 12, 9)
uop_168 = relay.acos(var_128.astype('float32')) # shape=(2, 12, 9)
output = relay.Tuple([bop_129,bop_147,uop_168,])
output2 = relay.Tuple([bop_129,bop_147,uop_168,])
func_179 = relay.Function([var_127,var_128,], output)
mod['func_179'] = func_179
mod = relay.transform.InferType()(mod)
var_180 = relay.var("var_180", dtype = "float32", shape = (2, 12, 9))#candidate|180|(2, 12, 9)|var|float32
var_181 = relay.var("var_181", dtype = "float32", shape = (2, 12, 9))#candidate|181|(2, 12, 9)|var|float32
output = func_179(var_180,var_181,)
func_182 = relay.Function([var_180,var_181,], output)
mutated_mod['func_182'] = func_182
mutated_mod = relay.transform.InferType()(mutated_mod)
const_317 = relay.const(-4, dtype = "uint32")#candidate|317|()|const|uint32
const_318 = relay.const([[[5,-8,10,3,-10,9,8,1,9,-10,1,-8,4,-5],[-4,10,-7,-8,-6,6,2,1,3,9,-10,-2,1,-3]],[[-3,10,7,9,-10,5,-1,-1,-8,-2,8,2,10,-1],[3,-6,2,6,-7,7,3,5,-3,-9,-1,-2,2,-7]],[[10,-3,-1,9,-4,5,1,9,2,-10,-10,-5,-9,2],[-3,-4,-6,-5,-6,2,-1,-1,9,-4,6,5,2,9]]], dtype = "uint32")#candidate|318|(3, 2, 14)|const|uint32
bop_319 = relay.logical_xor(const_317.astype('uint32'), const_318.astype('uint32')) # shape=(3, 2, 14)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
const_325 = relay.const([-2.170832,-9.241909,4.947214,0.679377,-8.343313,-9.025188,-0.804855,2.453678,3.831477,6.123384,8.500620,5.526894,-8.541190,-9.726162,3.651828,-7.888992,-5.137280,-1.528208,-3.161092,-5.396563,-0.150002,2.334145,3.321374,6.500365,-8.875436,-0.572081,-7.101877,8.293355,8.955883,-2.536809,9.303362,-8.472867,2.314625,-4.405389,-4.519640,7.059385,8.369558,1.216258,5.540562,1.068148,2.840601,-2.730202,9.865005,9.311755,1.036273,-4.279977,-0.439260,-7.584618,3.096771,-8.197947,0.748271,9.245111,-4.887252,0.052888,7.320198,1.922224,-3.567568,-9.303731,-9.729694,-1.855774,6.083234,-2.712530,8.456575,-9.623291,8.088811,-6.712550,-2.051722,8.349033,8.531879,-8.672118,3.119033,1.190334,3.779381,-6.624651,2.081363,2.876798,7.893170,7.941127,-7.210824,0.691320,-5.899030,-1.691337,3.380208,0.200402,-4.365575,-0.320087,-3.293003,-3.640365,0.124674,9.879092,4.681588,-3.996147,-2.350568,-0.940980,9.119979,5.185139,6.171648,-3.090707,4.968284,3.784547,1.113341,-4.939171,-4.547138,-4.760276,9.113377,-4.442314,-5.948171,0.581393,-1.375673,-7.816409,1.860616,2.386143,1.983540,-5.578514,-1.979577,0.367174,3.413965,0.575409,-5.111916,1.233053,4.961380,-9.968755,-7.540528,-6.504113,3.783502,-7.025185,-7.603957,-5.925404,8.504483,6.170778,-0.039556,-5.369434,-9.832803,2.527860,2.644752,-0.404933,0.708748,-5.064260,-2.431276,-4.952023,2.344313,-9.609362,8.774366,-3.768716,5.273320,-4.044111,-8.560727,9.308127,-4.327197,0.550033,-4.868293,-0.799291,-6.217178,3.144422,3.439138,5.195187,2.051841,3.395670,-6.056402,8.505577,5.957155,5.471850,-1.185459,-3.492485,-6.552056,-1.545366,4.494745,-5.677873,-8.620762,-1.717897,8.519411,-7.304998,3.310686,3.314731,9.309887,-3.401856,-7.194401,-4.639926,-9.276473,1.728396,-7.426073,3.409429,-1.030253,-7.422188,-9.379468,3.131094,-5.531911,-6.165296,1.619758,0.105424,-0.841467,3.967673,8.274026,-4.054318,-5.582573,-1.647912,8.938355,-1.331144,1.768323,-9.228874,2.772457,-5.610656,-3.229435,9.254664,-9.656173,-5.720583,-6.448354,-1.466103,-5.476032,-0.121472,-8.099573,3.636861,-0.048132,-1.809339,-0.285251,6.462314], dtype = "float32")#candidate|325|(216,)|const|float32
call_324 = relay.TupleGetItem(func_179_call(relay.reshape(const_325.astype('float32'), [2, 12, 9]), relay.reshape(const_325.astype('float32'), [2, 12, 9]), ), 0)
call_326 = relay.TupleGetItem(func_182_call(relay.reshape(const_325.astype('float32'), [2, 12, 9]), relay.reshape(const_325.astype('float32'), [2, 12, 9]), ), 0)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
call_329 = relay.TupleGetItem(func_179_call(relay.reshape(call_324.astype('float32'), [2, 12, 9]), relay.reshape(const_325.astype('float32'), [2, 12, 9]), ), 0)
call_330 = relay.TupleGetItem(func_182_call(relay.reshape(call_324.astype('float32'), [2, 12, 9]), relay.reshape(const_325.astype('float32'), [2, 12, 9]), ), 0)
uop_333 = relay.log10(call_329.astype('float32')) # shape=(2, 12, 9)
uop_335 = relay.log10(call_330.astype('float32')) # shape=(2, 12, 9)
uop_338 = relay.asin(uop_333.astype('float32')) # shape=(2, 12, 9)
uop_340 = relay.asin(uop_335.astype('float32')) # shape=(2, 12, 9)
output = relay.Tuple([bop_319,call_324,const_325,uop_338,])
output2 = relay.Tuple([bop_319,call_326,const_325,uop_340,])
func_342 = relay.Function([], output)
mod['func_342'] = func_342
mod = relay.transform.InferType()(mod)
mutated_mod['func_342'] = func_342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_342_call = mutated_mod.get_global_var('func_342')
call_343 = func_342_call()
output = call_343
func_344 = relay.Function([], output)
mutated_mod['func_344'] = func_344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_342_call = mod.get_global_var('func_342')
func_344_call = mutated_mod.get_global_var('func_344')
call_360 = relay.TupleGetItem(func_342_call(), 1)
call_361 = relay.TupleGetItem(func_344_call(), 1)
output = relay.Tuple([call_360,])
output2 = relay.Tuple([call_361,])
func_365 = relay.Function([], output)
mod['func_365'] = func_365
mod = relay.transform.InferType()(mod)
output = func_365()
func_366 = relay.Function([], output)
mutated_mod['func_366'] = func_366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_342_call = mod.get_global_var('func_342')
func_344_call = mutated_mod.get_global_var('func_344')
call_385 = relay.TupleGetItem(func_342_call(), 1)
call_386 = relay.TupleGetItem(func_344_call(), 1)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
call_391 = relay.TupleGetItem(func_179_call(relay.reshape(call_385.astype('float32'), [2, 12, 9]), relay.reshape(call_385.astype('float32'), [2, 12, 9]), ), 2)
call_392 = relay.TupleGetItem(func_182_call(relay.reshape(call_385.astype('float32'), [2, 12, 9]), relay.reshape(call_385.astype('float32'), [2, 12, 9]), ), 2)
output = relay.Tuple([call_385,call_391,])
output2 = relay.Tuple([call_386,call_392,])
func_393 = relay.Function([], output)
mod['func_393'] = func_393
mod = relay.transform.InferType()(mod)
mutated_mod['func_393'] = func_393
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mutated_mod.get_global_var('func_393')
call_394 = func_393_call()
output = call_394
func_395 = relay.Function([], output)
mutated_mod['func_395'] = func_395
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_417 = relay.TupleGetItem(func_365_call(), 0)
call_418 = relay.TupleGetItem(func_366_call(), 0)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_419 = relay.TupleGetItem(func_365_call(), 0)
call_420 = relay.TupleGetItem(func_366_call(), 0)
var_423 = relay.var("var_423", dtype = "bool", shape = (2, 12, 9))#candidate|423|(2, 12, 9)|var|bool
bop_424 = relay.floor_mod(call_417.astype('float64'), relay.reshape(var_423.astype('float64'), relay.shape_of(call_417))) # shape=(2, 12, 9)
bop_427 = relay.floor_mod(call_418.astype('float64'), relay.reshape(var_423.astype('float64'), relay.shape_of(call_418))) # shape=(2, 12, 9)
output = relay.Tuple([call_419,bop_424,])
output2 = relay.Tuple([call_420,bop_427,])
func_435 = relay.Function([var_423,], output)
mod['func_435'] = func_435
mod = relay.transform.InferType()(mod)
var_436 = relay.var("var_436", dtype = "bool", shape = (2, 12, 9))#candidate|436|(2, 12, 9)|var|bool
output = func_435(var_436)
func_437 = relay.Function([var_436], output)
mutated_mod['func_437'] = func_437
mutated_mod = relay.transform.InferType()(mutated_mod)
var_447 = relay.var("var_447", dtype = "uint8", shape = ())#candidate|447|()|var|uint8
var_448 = relay.var("var_448", dtype = "uint8", shape = (8, 14, 9))#candidate|448|(8, 14, 9)|var|uint8
bop_449 = relay.less_equal(var_447.astype('bool'), var_448.astype('bool')) # shape=(8, 14, 9)
output = bop_449
output2 = bop_449
func_452 = relay.Function([var_447,var_448,], output)
mod['func_452'] = func_452
mod = relay.transform.InferType()(mod)
var_453 = relay.var("var_453", dtype = "uint8", shape = ())#candidate|453|()|var|uint8
var_454 = relay.var("var_454", dtype = "uint8", shape = (8, 14, 9))#candidate|454|(8, 14, 9)|var|uint8
output = func_452(var_453,var_454,)
func_455 = relay.Function([var_453,var_454,], output)
mutated_mod['func_455'] = func_455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_508 = relay.TupleGetItem(func_365_call(), 0)
call_509 = relay.TupleGetItem(func_366_call(), 0)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
call_518 = relay.TupleGetItem(func_179_call(relay.reshape(call_508.astype('float32'), [2, 12, 9]), relay.reshape(call_508.astype('float32'), [2, 12, 9]), ), 1)
call_519 = relay.TupleGetItem(func_182_call(relay.reshape(call_508.astype('float32'), [2, 12, 9]), relay.reshape(call_508.astype('float32'), [2, 12, 9]), ), 1)
uop_539 = relay.log(call_508.astype('float64')) # shape=(2, 12, 9)
uop_541 = relay.log(call_509.astype('float64')) # shape=(2, 12, 9)
output = relay.Tuple([call_518,uop_539,])
output2 = relay.Tuple([call_519,uop_541,])
func_542 = relay.Function([], output)
mod['func_542'] = func_542
mod = relay.transform.InferType()(mod)
output = func_542()
func_543 = relay.Function([], output)
mutated_mod['func_543'] = func_543
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_590 = relay.TupleGetItem(func_542_call(), 1)
call_591 = relay.TupleGetItem(func_543_call(), 1)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
call_592 = relay.TupleGetItem(func_179_call(relay.reshape(call_590.astype('float32'), [2, 12, 9]), relay.reshape(call_590.astype('float32'), [2, 12, 9]), ), 0)
call_593 = relay.TupleGetItem(func_182_call(relay.reshape(call_590.astype('float32'), [2, 12, 9]), relay.reshape(call_590.astype('float32'), [2, 12, 9]), ), 0)
output = relay.Tuple([call_590,call_592,])
output2 = relay.Tuple([call_591,call_593,])
func_595 = relay.Function([], output)
mod['func_595'] = func_595
mod = relay.transform.InferType()(mod)
output = func_595()
func_596 = relay.Function([], output)
mutated_mod['func_596'] = func_596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_616 = relay.TupleGetItem(func_365_call(), 0)
call_617 = relay.TupleGetItem(func_366_call(), 0)
output = call_616
output2 = call_617
func_623 = relay.Function([], output)
mod['func_623'] = func_623
mod = relay.transform.InferType()(mod)
mutated_mod['func_623'] = func_623
mutated_mod = relay.transform.InferType()(mutated_mod)
func_623_call = mutated_mod.get_global_var('func_623')
call_624 = func_623_call()
output = call_624
func_625 = relay.Function([], output)
mutated_mod['func_625'] = func_625
mutated_mod = relay.transform.InferType()(mutated_mod)
var_681 = relay.var("var_681", dtype = "int8", shape = (11, 2, 16))#candidate|681|(11, 2, 16)|var|int8
var_682 = relay.var("var_682", dtype = "int8", shape = (11, 2, 16))#candidate|682|(11, 2, 16)|var|int8
bop_683 = relay.greater(var_681.astype('bool'), relay.reshape(var_682.astype('bool'), relay.shape_of(var_681))) # shape=(11, 2, 16)
var_686 = relay.var("var_686", dtype = "int8", shape = (11, 2, 16))#candidate|686|(11, 2, 16)|var|int8
bop_687 = relay.power(var_681.astype('float32'), relay.reshape(var_686.astype('float32'), relay.shape_of(var_681))) # shape=(11, 2, 16)
bop_690 = relay.divide(var_681.astype('float64'), relay.reshape(var_682.astype('float64'), relay.shape_of(var_681))) # shape=(11, 2, 16)
bop_694 = relay.bitwise_xor(bop_683.astype('int8'), relay.reshape(bop_690.astype('int8'), relay.shape_of(bop_683))) # shape=(11, 2, 16)
output = relay.Tuple([bop_687,bop_694,])
output2 = relay.Tuple([bop_687,bop_694,])
func_710 = relay.Function([var_681,var_682,var_686,], output)
mod['func_710'] = func_710
mod = relay.transform.InferType()(mod)
mutated_mod['func_710'] = func_710
mutated_mod = relay.transform.InferType()(mutated_mod)
func_710_call = mutated_mod.get_global_var('func_710')
var_712 = relay.var("var_712", dtype = "int8", shape = (11, 2, 16))#candidate|712|(11, 2, 16)|var|int8
var_713 = relay.var("var_713", dtype = "int8", shape = (11, 2, 16))#candidate|713|(11, 2, 16)|var|int8
var_714 = relay.var("var_714", dtype = "int8", shape = (11, 2, 16))#candidate|714|(11, 2, 16)|var|int8
call_711 = func_710_call(var_712,var_713,var_714,)
output = call_711
func_715 = relay.Function([var_712,var_713,var_714,], output)
mutated_mod['func_715'] = func_715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_732 = relay.TupleGetItem(func_393_call(), 0)
call_733 = relay.TupleGetItem(func_395_call(), 0)
uop_740 = relay.cos(call_732.astype('float64')) # shape=(2, 12, 9)
uop_742 = relay.cos(call_733.astype('float64')) # shape=(2, 12, 9)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_743 = relay.TupleGetItem(func_595_call(), 0)
call_744 = relay.TupleGetItem(func_596_call(), 0)
output = relay.Tuple([uop_740,call_743,])
output2 = relay.Tuple([uop_742,call_744,])
func_762 = relay.Function([], output)
mod['func_762'] = func_762
mod = relay.transform.InferType()(mod)
mutated_mod['func_762'] = func_762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_762_call = mutated_mod.get_global_var('func_762')
call_763 = func_762_call()
output = call_763
func_764 = relay.Function([], output)
mutated_mod['func_764'] = func_764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_762_call = mod.get_global_var('func_762')
func_764_call = mutated_mod.get_global_var('func_764')
call_832 = relay.TupleGetItem(func_762_call(), 0)
call_833 = relay.TupleGetItem(func_764_call(), 0)
func_342_call = mod.get_global_var('func_342')
func_344_call = mutated_mod.get_global_var('func_344')
call_850 = relay.TupleGetItem(func_342_call(), 2)
call_851 = relay.TupleGetItem(func_344_call(), 2)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_861 = relay.TupleGetItem(func_365_call(), 0)
call_862 = relay.TupleGetItem(func_366_call(), 0)
func_623_call = mod.get_global_var('func_623')
func_625_call = mutated_mod.get_global_var('func_625')
call_866 = func_623_call()
call_867 = func_623_call()
func_435_call = mod.get_global_var('func_435')
func_437_call = mutated_mod.get_global_var('func_437')
call_874 = relay.TupleGetItem(func_435_call(relay.reshape(call_861.astype('bool'), [2, 12, 9])), 1)
call_875 = relay.TupleGetItem(func_437_call(relay.reshape(call_861.astype('bool'), [2, 12, 9])), 1)
bop_877 = relay.bitwise_or(call_866.astype('int16'), relay.reshape(call_874.astype('int16'), relay.shape_of(call_866))) # shape=(2, 12, 9)
bop_880 = relay.bitwise_or(call_867.astype('int16'), relay.reshape(call_875.astype('int16'), relay.shape_of(call_867))) # shape=(2, 12, 9)
func_452_call = mod.get_global_var('func_452')
func_455_call = mutated_mod.get_global_var('func_455')
const_885 = relay.const(-10, dtype = "uint8")#candidate|885|()|const|uint8
var_886 = relay.var("var_886", dtype = "uint8", shape = (1008,))#candidate|886|(1008,)|var|uint8
call_884 = func_452_call(relay.reshape(const_885.astype('uint8'), []), relay.reshape(var_886.astype('uint8'), [8, 14, 9]), )
call_887 = func_452_call(relay.reshape(const_885.astype('uint8'), []), relay.reshape(var_886.astype('uint8'), [8, 14, 9]), )
output = relay.Tuple([call_832,call_850,call_861,bop_877,call_884,const_885,var_886,])
output2 = relay.Tuple([call_833,call_851,call_862,bop_880,call_887,const_885,var_886,])
func_901 = relay.Function([var_886,], output)
mod['func_901'] = func_901
mod = relay.transform.InferType()(mod)
mutated_mod['func_901'] = func_901
mutated_mod = relay.transform.InferType()(mutated_mod)
var_902 = relay.var("var_902", dtype = "uint8", shape = (1008,))#candidate|902|(1008,)|var|uint8
func_901_call = mutated_mod.get_global_var('func_901')
call_903 = func_901_call(var_902)
output = call_903
func_904 = relay.Function([var_902], output)
mutated_mod['func_904'] = func_904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_950 = relay.TupleGetItem(func_595_call(), 0)
call_951 = relay.TupleGetItem(func_596_call(), 0)
output = relay.Tuple([call_950,])
output2 = relay.Tuple([call_951,])
func_952 = relay.Function([], output)
mod['func_952'] = func_952
mod = relay.transform.InferType()(mod)
mutated_mod['func_952'] = func_952
mutated_mod = relay.transform.InferType()(mutated_mod)
func_952_call = mutated_mod.get_global_var('func_952')
call_953 = func_952_call()
output = call_953
func_954 = relay.Function([], output)
mutated_mod['func_954'] = func_954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_342_call = mod.get_global_var('func_342')
func_344_call = mutated_mod.get_global_var('func_344')
call_1007 = relay.TupleGetItem(func_342_call(), 3)
call_1008 = relay.TupleGetItem(func_344_call(), 3)
output = relay.Tuple([call_1007,])
output2 = relay.Tuple([call_1008,])
func_1015 = relay.Function([], output)
mod['func_1015'] = func_1015
mod = relay.transform.InferType()(mod)
output = func_1015()
func_1016 = relay.Function([], output)
mutated_mod['func_1016'] = func_1016
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_1022 = relay.TupleGetItem(func_393_call(), 0)
call_1023 = relay.TupleGetItem(func_395_call(), 0)
output = call_1022
output2 = call_1023
func_1029 = relay.Function([], output)
mod['func_1029'] = func_1029
mod = relay.transform.InferType()(mod)
mutated_mod['func_1029'] = func_1029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mutated_mod.get_global_var('func_1029')
call_1030 = func_1029_call()
output = call_1030
func_1031 = relay.Function([], output)
mutated_mod['func_1031'] = func_1031
mutated_mod = relay.transform.InferType()(mutated_mod)
func_952_call = mod.get_global_var('func_952')
func_954_call = mutated_mod.get_global_var('func_954')
call_1032 = relay.TupleGetItem(func_952_call(), 0)
call_1033 = relay.TupleGetItem(func_954_call(), 0)
output = call_1032
output2 = call_1033
func_1064 = relay.Function([], output)
mod['func_1064'] = func_1064
mod = relay.transform.InferType()(mod)
mutated_mod['func_1064'] = func_1064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mutated_mod.get_global_var('func_1064')
call_1065 = func_1064_call()
output = call_1065
func_1066 = relay.Function([], output)
mutated_mod['func_1066'] = func_1066
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1107 = relay.var("var_1107", dtype = "float32", shape = (8, 14, 4))#candidate|1107|(8, 14, 4)|var|float32
var_1108 = relay.var("var_1108", dtype = "float32", shape = (8, 14, 4))#candidate|1108|(8, 14, 4)|var|float32
bop_1109 = relay.power(var_1107.astype('float32'), relay.reshape(var_1108.astype('float32'), relay.shape_of(var_1107))) # shape=(8, 14, 4)
func_710_call = mod.get_global_var('func_710')
func_715_call = mutated_mod.get_global_var('func_715')
var_1113 = relay.var("var_1113", dtype = "int8", shape = (352,))#candidate|1113|(352,)|var|int8
call_1112 = relay.TupleGetItem(func_710_call(relay.reshape(var_1113.astype('int8'), [11, 2, 16]), relay.reshape(var_1113.astype('int8'), [11, 2, 16]), relay.reshape(var_1113.astype('int8'), [11, 2, 16]), ), 1)
call_1114 = relay.TupleGetItem(func_715_call(relay.reshape(var_1113.astype('int8'), [11, 2, 16]), relay.reshape(var_1113.astype('int8'), [11, 2, 16]), relay.reshape(var_1113.astype('int8'), [11, 2, 16]), ), 1)
output = relay.Tuple([bop_1109,call_1112,var_1113,])
output2 = relay.Tuple([bop_1109,call_1114,var_1113,])
func_1118 = relay.Function([var_1107,var_1108,var_1113,], output)
mod['func_1118'] = func_1118
mod = relay.transform.InferType()(mod)
var_1119 = relay.var("var_1119", dtype = "float32", shape = (8, 14, 4))#candidate|1119|(8, 14, 4)|var|float32
var_1120 = relay.var("var_1120", dtype = "float32", shape = (8, 14, 4))#candidate|1120|(8, 14, 4)|var|float32
var_1121 = relay.var("var_1121", dtype = "int8", shape = (352,))#candidate|1121|(352,)|var|int8
output = func_1118(var_1119,var_1120,var_1121,)
func_1122 = relay.Function([var_1119,var_1120,var_1121,], output)
mutated_mod['func_1122'] = func_1122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_1143 = relay.TupleGetItem(func_595_call(), 0)
call_1144 = relay.TupleGetItem(func_596_call(), 0)
output = relay.Tuple([call_1143,])
output2 = relay.Tuple([call_1144,])
func_1145 = relay.Function([], output)
mod['func_1145'] = func_1145
mod = relay.transform.InferType()(mod)
mutated_mod['func_1145'] = func_1145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1145_call = mutated_mod.get_global_var('func_1145')
call_1146 = func_1145_call()
output = call_1146
func_1147 = relay.Function([], output)
mutated_mod['func_1147'] = func_1147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_1223 = relay.TupleGetItem(func_1015_call(), 0)
call_1224 = relay.TupleGetItem(func_1016_call(), 0)
func_710_call = mod.get_global_var('func_710')
func_715_call = mutated_mod.get_global_var('func_715')
var_1227 = relay.var("var_1227", dtype = "int8", shape = (352,))#candidate|1227|(352,)|var|int8
call_1226 = relay.TupleGetItem(func_710_call(relay.reshape(var_1227.astype('int8'), [11, 2, 16]), relay.reshape(var_1227.astype('int8'), [11, 2, 16]), relay.reshape(var_1227.astype('int8'), [11, 2, 16]), ), 1)
call_1228 = relay.TupleGetItem(func_715_call(relay.reshape(var_1227.astype('int8'), [11, 2, 16]), relay.reshape(var_1227.astype('int8'), [11, 2, 16]), relay.reshape(var_1227.astype('int8'), [11, 2, 16]), ), 1)
uop_1235 = relay.asinh(call_1226.astype('float32')) # shape=(11, 2, 16)
uop_1237 = relay.asinh(call_1228.astype('float32')) # shape=(11, 2, 16)
uop_1250 = relay.cos(var_1227.astype('float32')) # shape=(352,)
output = relay.Tuple([call_1223,uop_1235,uop_1250,])
output2 = relay.Tuple([call_1224,uop_1237,uop_1250,])
func_1259 = relay.Function([var_1227,], output)
mod['func_1259'] = func_1259
mod = relay.transform.InferType()(mod)
mutated_mod['func_1259'] = func_1259
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1260 = relay.var("var_1260", dtype = "int8", shape = (352,))#candidate|1260|(352,)|var|int8
func_1259_call = mutated_mod.get_global_var('func_1259')
call_1261 = func_1259_call(var_1260)
output = call_1261
func_1262 = relay.Function([var_1260], output)
mutated_mod['func_1262'] = func_1262
mutated_mod = relay.transform.InferType()(mutated_mod)
func_952_call = mod.get_global_var('func_952')
func_954_call = mutated_mod.get_global_var('func_954')
call_1300 = relay.TupleGetItem(func_952_call(), 0)
call_1301 = relay.TupleGetItem(func_954_call(), 0)
output = relay.Tuple([call_1300,])
output2 = relay.Tuple([call_1301,])
func_1322 = relay.Function([], output)
mod['func_1322'] = func_1322
mod = relay.transform.InferType()(mod)
output = func_1322()
func_1323 = relay.Function([], output)
mutated_mod['func_1323'] = func_1323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_1335 = relay.TupleGetItem(func_542_call(), 1)
call_1336 = relay.TupleGetItem(func_543_call(), 1)
output = relay.Tuple([call_1335,])
output2 = relay.Tuple([call_1336,])
func_1337 = relay.Function([], output)
mod['func_1337'] = func_1337
mod = relay.transform.InferType()(mod)
output = func_1337()
func_1338 = relay.Function([], output)
mutated_mod['func_1338'] = func_1338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_1362 = relay.TupleGetItem(func_365_call(), 0)
call_1363 = relay.TupleGetItem(func_366_call(), 0)
output = call_1362
output2 = call_1363
func_1374 = relay.Function([], output)
mod['func_1374'] = func_1374
mod = relay.transform.InferType()(mod)
output = func_1374()
func_1375 = relay.Function([], output)
mutated_mod['func_1375'] = func_1375
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_1394 = relay.TupleGetItem(func_542_call(), 0)
call_1395 = relay.TupleGetItem(func_543_call(), 0)
output = call_1394
output2 = call_1395
func_1406 = relay.Function([], output)
mod['func_1406'] = func_1406
mod = relay.transform.InferType()(mod)
mutated_mod['func_1406'] = func_1406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1406_call = mutated_mod.get_global_var('func_1406')
call_1407 = func_1406_call()
output = call_1407
func_1408 = relay.Function([], output)
mutated_mod['func_1408'] = func_1408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_1452 = relay.TupleGetItem(func_542_call(), 0)
call_1453 = relay.TupleGetItem(func_543_call(), 0)
output = relay.Tuple([call_1452,])
output2 = relay.Tuple([call_1453,])
func_1454 = relay.Function([], output)
mod['func_1454'] = func_1454
mod = relay.transform.InferType()(mod)
mutated_mod['func_1454'] = func_1454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mutated_mod.get_global_var('func_1454')
call_1455 = func_1454_call()
output = call_1455
func_1456 = relay.Function([], output)
mutated_mod['func_1456'] = func_1456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_623_call = mod.get_global_var('func_623')
func_625_call = mutated_mod.get_global_var('func_625')
call_1464 = func_623_call()
call_1465 = func_623_call()
func_762_call = mod.get_global_var('func_762')
func_764_call = mutated_mod.get_global_var('func_764')
call_1486 = relay.TupleGetItem(func_762_call(), 0)
call_1487 = relay.TupleGetItem(func_764_call(), 0)
func_1374_call = mod.get_global_var('func_1374')
func_1375_call = mutated_mod.get_global_var('func_1375')
call_1491 = func_1374_call()
call_1492 = func_1374_call()
output = relay.Tuple([call_1464,call_1486,call_1491,])
output2 = relay.Tuple([call_1465,call_1487,call_1492,])
func_1502 = relay.Function([], output)
mod['func_1502'] = func_1502
mod = relay.transform.InferType()(mod)
output = func_1502()
func_1503 = relay.Function([], output)
mutated_mod['func_1503'] = func_1503
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1406_call = mod.get_global_var('func_1406')
func_1408_call = mutated_mod.get_global_var('func_1408')
call_1570 = func_1406_call()
call_1571 = func_1406_call()
output = call_1570
output2 = call_1571
func_1581 = relay.Function([], output)
mod['func_1581'] = func_1581
mod = relay.transform.InferType()(mod)
mutated_mod['func_1581'] = func_1581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mutated_mod.get_global_var('func_1581')
call_1582 = func_1581_call()
output = call_1582
func_1583 = relay.Function([], output)
mutated_mod['func_1583'] = func_1583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_762_call = mod.get_global_var('func_762')
func_764_call = mutated_mod.get_global_var('func_764')
call_1602 = relay.TupleGetItem(func_762_call(), 1)
call_1603 = relay.TupleGetItem(func_764_call(), 1)
output = call_1602
output2 = call_1603
func_1618 = relay.Function([], output)
mod['func_1618'] = func_1618
mod = relay.transform.InferType()(mod)
output = func_1618()
func_1619 = relay.Function([], output)
mutated_mod['func_1619'] = func_1619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_1665 = relay.TupleGetItem(func_1454_call(), 0)
call_1666 = relay.TupleGetItem(func_1456_call(), 0)
var_1674 = relay.var("var_1674", dtype = "float64", shape = (2, 12, 9))#candidate|1674|(2, 12, 9)|var|float64
bop_1675 = relay.bitwise_and(call_1665.astype('uint8'), relay.reshape(var_1674.astype('uint8'), relay.shape_of(call_1665))) # shape=(2, 12, 9)
bop_1678 = relay.bitwise_and(call_1666.astype('uint8'), relay.reshape(var_1674.astype('uint8'), relay.shape_of(call_1666))) # shape=(2, 12, 9)
uop_1683 = relay.atan(bop_1675.astype('float32')) # shape=(2, 12, 9)
uop_1685 = relay.atan(bop_1678.astype('float32')) # shape=(2, 12, 9)
output = relay.Tuple([uop_1683,])
output2 = relay.Tuple([uop_1685,])
func_1689 = relay.Function([var_1674,], output)
mod['func_1689'] = func_1689
mod = relay.transform.InferType()(mod)
mutated_mod['func_1689'] = func_1689
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1690 = relay.var("var_1690", dtype = "float64", shape = (2, 12, 9))#candidate|1690|(2, 12, 9)|var|float64
func_1689_call = mutated_mod.get_global_var('func_1689')
call_1691 = func_1689_call(var_1690)
output = call_1691
func_1692 = relay.Function([var_1690], output)
mutated_mod['func_1692'] = func_1692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_1740 = relay.TupleGetItem(func_595_call(), 1)
call_1741 = relay.TupleGetItem(func_596_call(), 1)
var_1742 = relay.var("var_1742", dtype = "bool", shape = (2, 12, 9))#candidate|1742|(2, 12, 9)|var|bool
bop_1743 = relay.power(call_1740.astype('float32'), relay.reshape(var_1742.astype('float32'), relay.shape_of(call_1740))) # shape=(2, 12, 9)
bop_1746 = relay.power(call_1741.astype('float32'), relay.reshape(var_1742.astype('float32'), relay.shape_of(call_1741))) # shape=(2, 12, 9)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1747 = func_1029_call()
call_1748 = func_1029_call()
func_1322_call = mod.get_global_var('func_1322')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_1756 = relay.TupleGetItem(func_1322_call(), 0)
call_1757 = relay.TupleGetItem(func_1323_call(), 0)
output = relay.Tuple([bop_1743,call_1747,call_1756,])
output2 = relay.Tuple([bop_1746,call_1748,call_1757,])
func_1774 = relay.Function([var_1742,], output)
mod['func_1774'] = func_1774
mod = relay.transform.InferType()(mod)
var_1775 = relay.var("var_1775", dtype = "bool", shape = (2, 12, 9))#candidate|1775|(2, 12, 9)|var|bool
output = func_1774(var_1775)
func_1776 = relay.Function([var_1775], output)
mutated_mod['func_1776'] = func_1776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_1806 = func_1581_call()
call_1807 = func_1581_call()
const_1820 = relay.const([[[4.010449,-3.993540,-1.940513,5.326087,9.261372,-7.120066,4.941451,9.406387,-9.963634],[-7.053590,3.721064,0.177573,-8.714971,2.075771,-1.367247,-4.391200,5.015746,8.008875],[-8.260373,5.958950,-8.567307,1.212455,6.295152,7.051036,-2.182527,2.736457,-5.310020],[0.992206,-1.259915,-6.892609,-8.384075,-7.170955,3.288742,9.545214,-9.856604,1.904852],[-8.468156,4.825436,2.410711,-9.835031,-9.332900,-8.894862,-1.034201,-2.686138,-8.264999],[0.328189,6.171557,3.490264,6.593761,-5.241282,4.218876,4.609976,-4.848200,7.683572],[0.523211,7.089804,-3.921412,0.248921,-4.538420,3.595396,-6.073610,3.522009,-2.760846],[-4.433287,2.278204,4.610418,-5.623850,-2.715901,6.727938,5.018043,8.721784,2.187569],[-7.515168,-4.992545,-8.566751,2.752146,-9.380397,-7.956037,6.177290,9.329950,2.609210],[3.302093,6.531798,7.713569,-5.498965,5.444488,9.413382,0.174947,8.506656,-1.240045],[7.885304,-3.516948,-3.849824,-0.567981,0.354301,-6.567077,-5.257362,5.856660,-1.600633],[2.203993,4.585431,-4.370954,7.921448,-3.655205,-0.221308,-3.707412,-9.879157,8.493281]],[[0.537894,6.874493,0.452871,9.146372,6.221486,9.568898,6.231768,-7.639903,-9.126164],[-2.358544,-7.645831,-8.869375,0.831514,-2.467015,-9.064979,6.678617,7.675257,-2.294285],[-7.435918,7.698468,-2.432472,3.133767,1.436082,-0.469025,5.305001,3.240723,5.660428],[-1.706273,-9.811640,1.455151,-3.346368,-8.900258,7.835085,6.571063,-8.387477,7.063197],[5.246400,7.972329,5.045066,-9.883544,-3.824529,-6.094213,-1.908064,-6.880135,-9.117215],[4.745462,-1.713988,-7.993667,-3.098934,-4.021327,-3.137431,-3.019946,-7.412107,-0.838600],[8.618058,-7.666539,-5.382680,-2.625791,4.040682,6.528816,-2.030296,9.939410,-7.316935],[-6.733400,6.702299,-4.055375,-1.927344,5.813722,-7.372278,-7.531110,2.303995,7.260890],[-3.822477,-1.995360,-3.140500,3.025468,-7.543491,-0.749464,-0.595030,4.688011,6.107312],[-5.824938,-5.009267,-8.648083,6.268423,4.717715,-2.469832,6.826167,-5.327053,-5.889745],[0.554808,7.992660,-8.147300,9.181403,-1.593035,-9.115602,-1.802504,2.193681,8.528982],[4.773496,1.152582,6.192962,4.930737,-0.470698,-3.614960,-3.029793,-5.348362,7.511412]]], dtype = "float64")#candidate|1820|(2, 12, 9)|const|float64
bop_1821 = relay.mod(call_1806.astype('float32'), relay.reshape(const_1820.astype('float32'), relay.shape_of(call_1806))) # shape=(2, 12, 9)
bop_1824 = relay.mod(call_1807.astype('float32'), relay.reshape(const_1820.astype('float32'), relay.shape_of(call_1807))) # shape=(2, 12, 9)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_1838 = relay.TupleGetItem(func_595_call(), 1)
call_1839 = relay.TupleGetItem(func_596_call(), 1)
func_1374_call = mod.get_global_var('func_1374')
func_1375_call = mutated_mod.get_global_var('func_1375')
call_1841 = func_1374_call()
call_1842 = func_1374_call()
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_1856 = func_1029_call()
call_1857 = func_1029_call()
func_1689_call = mod.get_global_var('func_1689')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_1862 = relay.TupleGetItem(func_1689_call(relay.reshape(call_1841.astype('float64'), [2, 12, 9])), 0)
call_1863 = relay.TupleGetItem(func_1692_call(relay.reshape(call_1841.astype('float64'), [2, 12, 9])), 0)
const_1871 = relay.const([[[False,True,False,True,False,False,False,False,False],[True,False,False,True,True,True,False,False,False],[False,True,False,False,True,True,True,False,True],[False,True,True,False,False,False,False,True,False],[False,True,True,True,False,True,True,True,False],[False,True,False,True,False,True,True,False,False],[False,True,False,False,True,False,True,True,False],[False,True,True,False,False,False,True,True,False],[False,False,False,False,True,True,False,False,True],[False,True,True,False,False,False,True,False,True],[True,True,False,True,True,False,False,False,False],[False,True,True,False,False,True,False,False,False]],[[False,True,False,True,True,False,True,True,False],[True,False,False,True,True,True,True,False,True],[True,False,True,True,False,False,False,True,False],[False,True,True,False,True,False,True,True,True],[True,False,False,True,True,True,True,False,False],[False,False,True,True,True,True,False,True,False],[True,True,True,True,True,False,False,False,False],[False,True,True,True,False,True,False,True,False],[True,False,True,True,False,True,False,False,False],[False,False,True,False,True,True,True,True,False],[True,True,False,True,False,True,False,True,True],[True,True,False,False,False,False,True,False,True]]], dtype = "bool")#candidate|1871|(2, 12, 9)|const|bool
bop_1872 = relay.subtract(call_1841.astype('int64'), relay.reshape(const_1871.astype('int64'), relay.shape_of(call_1841))) # shape=(2, 12, 9)
bop_1875 = relay.subtract(call_1842.astype('int64'), relay.reshape(const_1871.astype('int64'), relay.shape_of(call_1842))) # shape=(2, 12, 9)
output = relay.Tuple([bop_1821,call_1838,call_1856,call_1862,bop_1872,])
output2 = relay.Tuple([bop_1824,call_1839,call_1857,call_1863,bop_1875,])
func_1888 = relay.Function([], output)
mod['func_1888'] = func_1888
mod = relay.transform.InferType()(mod)
output = func_1888()
func_1889 = relay.Function([], output)
mutated_mod['func_1889'] = func_1889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_1897 = relay.TupleGetItem(func_365_call(), 0)
call_1898 = relay.TupleGetItem(func_366_call(), 0)
output = call_1897
output2 = call_1898
func_1913 = relay.Function([], output)
mod['func_1913'] = func_1913
mod = relay.transform.InferType()(mod)
mutated_mod['func_1913'] = func_1913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mutated_mod.get_global_var('func_1913')
call_1914 = func_1913_call()
output = call_1914
func_1915 = relay.Function([], output)
mutated_mod['func_1915'] = func_1915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_1957 = relay.TupleGetItem(func_1145_call(), 0)
call_1958 = relay.TupleGetItem(func_1147_call(), 0)
func_1888_call = mod.get_global_var('func_1888')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_1977 = relay.TupleGetItem(func_1888_call(), 1)
call_1978 = relay.TupleGetItem(func_1889_call(), 1)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
call_1990 = relay.TupleGetItem(func_179_call(relay.reshape(call_1957.astype('float32'), [2, 12, 9]), relay.reshape(call_1957.astype('float32'), [2, 12, 9]), ), 1)
call_1991 = relay.TupleGetItem(func_182_call(relay.reshape(call_1957.astype('float32'), [2, 12, 9]), relay.reshape(call_1957.astype('float32'), [2, 12, 9]), ), 1)
output = relay.Tuple([call_1957,call_1977,call_1990,])
output2 = relay.Tuple([call_1958,call_1978,call_1991,])
func_1993 = relay.Function([], output)
mod['func_1993'] = func_1993
mod = relay.transform.InferType()(mod)
output = func_1993()
func_1994 = relay.Function([], output)
mutated_mod['func_1994'] = func_1994
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_2007 = relay.TupleGetItem(func_1322_call(), 0)
call_2008 = relay.TupleGetItem(func_1323_call(), 0)
output = call_2007
output2 = call_2008
func_2024 = relay.Function([], output)
mod['func_2024'] = func_2024
mod = relay.transform.InferType()(mod)
mutated_mod['func_2024'] = func_2024
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2024_call = mutated_mod.get_global_var('func_2024')
call_2025 = func_2024_call()
output = call_2025
func_2026 = relay.Function([], output)
mutated_mod['func_2026'] = func_2026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1374_call = mod.get_global_var('func_1374')
func_1375_call = mutated_mod.get_global_var('func_1375')
call_2031 = func_1374_call()
call_2032 = func_1374_call()
func_1689_call = mod.get_global_var('func_1689')
func_1692_call = mutated_mod.get_global_var('func_1692')
call_2035 = relay.TupleGetItem(func_1689_call(relay.reshape(call_2031.astype('float64'), [2, 12, 9])), 0)
call_2036 = relay.TupleGetItem(func_1692_call(relay.reshape(call_2031.astype('float64'), [2, 12, 9])), 0)
output = relay.Tuple([call_2031,call_2035,])
output2 = relay.Tuple([call_2032,call_2036,])
func_2043 = relay.Function([], output)
mod['func_2043'] = func_2043
mod = relay.transform.InferType()(mod)
output = func_2043()
func_2044 = relay.Function([], output)
mutated_mod['func_2044'] = func_2044
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_2095 = relay.TupleGetItem(func_1015_call(), 0)
call_2096 = relay.TupleGetItem(func_1016_call(), 0)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_2106 = relay.TupleGetItem(func_595_call(), 1)
call_2107 = relay.TupleGetItem(func_596_call(), 1)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2116 = relay.TupleGetItem(func_2043_call(), 1)
call_2117 = relay.TupleGetItem(func_2044_call(), 1)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_2160 = func_1064_call()
call_2161 = func_1064_call()
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_2190 = relay.TupleGetItem(func_1774_call(relay.reshape(call_2106.astype('bool'), [2, 12, 9])), 2)
call_2191 = relay.TupleGetItem(func_1776_call(relay.reshape(call_2106.astype('bool'), [2, 12, 9])), 2)
output = relay.Tuple([call_2095,call_2106,call_2116,call_2160,call_2190,])
output2 = relay.Tuple([call_2096,call_2107,call_2117,call_2161,call_2191,])
func_2207 = relay.Function([], output)
mod['func_2207'] = func_2207
mod = relay.transform.InferType()(mod)
output = func_2207()
func_2208 = relay.Function([], output)
mutated_mod['func_2208'] = func_2208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2213 = func_1913_call()
call_2214 = func_1913_call()
output = call_2213
output2 = call_2214
func_2219 = relay.Function([], output)
mod['func_2219'] = func_2219
mod = relay.transform.InferType()(mod)
mutated_mod['func_2219'] = func_2219
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2219_call = mutated_mod.get_global_var('func_2219')
call_2220 = func_2219_call()
output = call_2220
func_2221 = relay.Function([], output)
mutated_mod['func_2221'] = func_2221
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_2255 = relay.TupleGetItem(func_2043_call(), 0)
call_2256 = relay.TupleGetItem(func_2044_call(), 0)
uop_2261 = relay.sigmoid(call_2255.astype('float64')) # shape=(2, 12, 9)
uop_2263 = relay.sigmoid(call_2256.astype('float64')) # shape=(2, 12, 9)
output = uop_2261
output2 = uop_2263
func_2273 = relay.Function([], output)
mod['func_2273'] = func_2273
mod = relay.transform.InferType()(mod)
mutated_mod['func_2273'] = func_2273
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2273_call = mutated_mod.get_global_var('func_2273')
call_2274 = func_2273_call()
output = call_2274
func_2275 = relay.Function([], output)
mutated_mod['func_2275'] = func_2275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_2449 = relay.TupleGetItem(func_595_call(), 0)
call_2450 = relay.TupleGetItem(func_596_call(), 0)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_2451 = relay.TupleGetItem(func_542_call(), 0)
call_2452 = relay.TupleGetItem(func_543_call(), 0)
output = relay.Tuple([call_2449,call_2451,])
output2 = relay.Tuple([call_2450,call_2452,])
func_2455 = relay.Function([], output)
mod['func_2455'] = func_2455
mod = relay.transform.InferType()(mod)
output = func_2455()
func_2456 = relay.Function([], output)
mutated_mod['func_2456'] = func_2456
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mod.get_global_var('func_2207')
func_2208_call = mutated_mod.get_global_var('func_2208')
call_2463 = relay.TupleGetItem(func_2207_call(), 1)
call_2464 = relay.TupleGetItem(func_2208_call(), 1)
output = relay.Tuple([call_2463,])
output2 = relay.Tuple([call_2464,])
func_2467 = relay.Function([], output)
mod['func_2467'] = func_2467
mod = relay.transform.InferType()(mod)
output = func_2467()
func_2468 = relay.Function([], output)
mutated_mod['func_2468'] = func_2468
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2525 = relay.const([[[-2,6,4,1,-4,-9,-8,9,-9,-4,4,6,-2],[5,8,3,-6,3,4,-8,-8,3,1,3,4,-4],[-7,-10,-1,-9,10,-8,-3,-4,4,-5,-10,8,2],[-3,9,5,-10,-7,2,10,9,6,-7,-1,4,-3]],[[8,-6,-3,9,8,9,10,7,-3,-4,4,-8,-2],[-2,-7,-1,-6,-7,7,2,1,3,9,-5,-8,-9],[-9,-5,-8,-9,4,9,-8,1,-4,3,6,9,8],[10,-3,10,7,-4,2,9,-3,6,-7,-9,1,8]],[[-9,-3,-1,5,-5,5,-10,-9,2,10,8,-9,4],[8,9,3,3,7,10,-7,6,-8,-10,-1,-5,-10],[-9,-8,6,-8,-1,4,-8,7,2,-2,-5,7,7],[10,10,-3,-10,10,8,-2,1,-5,9,-7,-8,-1]],[[1,-10,9,8,-1,-6,3,-6,8,-2,-6,-5,10],[5,-1,3,-8,10,-7,7,-9,-1,-1,-5,-5,-5],[5,5,4,-3,8,-8,-3,4,-7,7,3,10,3],[2,-4,10,-1,-3,2,-1,-6,-7,-7,6,-1,10]],[[1,8,7,3,-9,9,7,-4,-1,-1,3,-5,-10],[-2,6,-7,-4,-2,-6,-2,-9,6,4,4,4,4],[5,6,10,8,-2,2,9,6,-10,-4,-9,2,-10],[-1,-4,-4,2,-2,-9,-10,-5,-6,-8,-4,1,5]],[[8,-5,6,7,-9,-6,-10,-5,1,2,10,2,2],[-8,6,3,3,-4,-4,-8,1,-3,-4,-2,6,3],[-1,5,3,-6,-7,2,-7,-8,7,-3,1,9,-4],[2,-4,5,-2,-9,-4,-5,-4,-10,5,-3,3,1]]], dtype = "uint32")#candidate|2525|(6, 4, 13)|const|uint32
var_2526 = relay.var("var_2526", dtype = "uint32", shape = (6, 4, 13))#candidate|2526|(6, 4, 13)|var|uint32
bop_2527 = relay.subtract(const_2525.astype('uint32'), relay.reshape(var_2526.astype('uint32'), relay.shape_of(const_2525))) # shape=(6, 4, 13)
output = bop_2527
output2 = bop_2527
func_2532 = relay.Function([var_2526,], output)
mod['func_2532'] = func_2532
mod = relay.transform.InferType()(mod)
var_2533 = relay.var("var_2533", dtype = "uint32", shape = (6, 4, 13))#candidate|2533|(6, 4, 13)|var|uint32
output = func_2532(var_2533)
func_2534 = relay.Function([var_2533], output)
mutated_mod['func_2534'] = func_2534
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2549 = relay.var("var_2549", dtype = "float64", shape = (15, 1, 1))#candidate|2549|(15, 1, 1)|var|float64
uop_2550 = relay.atanh(var_2549.astype('float64')) # shape=(15, 1, 1)
func_1118_call = mod.get_global_var('func_1118')
func_1122_call = mutated_mod.get_global_var('func_1122')
const_2560 = relay.const([-5.623245,3.257667,9.904798,5.496554,-1.446150,-8.156897,0.976136,0.442655,0.171612,6.004236,-4.898784,-3.134758,-3.632626,-6.881223,2.330055,0.264254,7.000359,-0.845818,2.264350,-9.295121,6.379611,2.563150,-8.069602,8.017631,2.838751,-6.059720,-8.311500,-6.351801,4.339485,-6.137715,-0.378519,9.483597,-7.406048,-8.269046,3.091395,3.178670,-2.296791,9.885627,-3.495901,-8.610981,9.551716,7.365681,0.643244,-5.843322,-8.561044,8.159313,-8.695445,-6.189841,4.907859,3.158382,-1.801819,1.586257,8.679275,0.746099,1.809997,-6.996942,-6.129231,-2.406367,0.967324,3.796564,4.859000,-7.884911,9.945490,5.522053,2.345000,3.778706,5.983222,-5.930372,8.675875,-5.031403,-1.900890,7.744500,-3.806705,-4.817599,-5.110903,-0.945852,4.076498,-9.950383,8.869053,3.843320,-8.429472,-2.708092,8.414766,-9.892421,-9.606839,-8.303561,4.425952,-1.537723,4.130374,3.749300,-7.583094,-5.278458,-1.235471,-2.463480,-1.591123,2.458747,-6.727677,-1.593690,-4.743508,-8.985608,-3.081359,5.817983,-5.595071,7.939052,2.677564,8.216627,-9.661593,9.648041,-0.243712,4.458039,4.010551,2.754795,-9.082013,5.513805,3.066039,-4.457279,-1.353803,2.595897,6.078802,8.420200,-6.440423,-6.752263,-0.960088,1.839945,9.632297,5.479608,4.787773,-5.279708,-6.407207,8.559935,4.156068,8.041454,6.973064,-5.661893,-4.945791,4.177773,-7.696049,6.856930,5.609424,-7.331080,6.002707,1.343258,-9.171616,9.442330,-2.999638,-4.836481,-9.161691,0.385897,0.862831,-6.668307,8.874257,-2.700641,4.595787,-4.775230,-4.630062,0.032904,-9.086699,3.957071,-4.415116,-1.420604,5.423762,-2.501630,-6.119081,3.070078,7.719470,3.333199,-7.592897,-4.847726,-7.144154,-9.903005,5.137853,-9.027999,5.115323,9.754469,-6.269701,-3.948594,-3.368712,8.993968,-7.868471,-6.117704,-2.720132,9.188497,5.508755,-0.463362,-0.225668,1.747527,-7.313274,-4.436074,8.178414,2.057731,6.043007,8.160902,-5.026596,-3.223135,4.370362,-7.676051,6.797551,-3.466457,-6.897931,-5.142240,-5.126682,-7.991735,6.421894,-1.441296,-2.357169,0.691198,4.204886,-8.267994,1.739191,-2.309753,1.494572,7.981923,-6.121353,-0.554448,-2.978191,-9.159086,-6.852096,-5.329197,4.214110,-6.733106,-9.957989,8.895256,-7.087683,-0.154797,-9.463492,-9.946655,5.171983,-5.845234,-2.067580,-4.503337,3.669775,9.628366,-4.158560,-2.861481,-2.837519,1.574811,-4.769687,-0.337228,-1.435549,-6.769245,0.142110,8.123700,-7.854048,7.229468,-3.870395,-0.064202,-9.596669,4.968983,4.547592,-3.310954,-0.375242,-3.879928,-8.387892,9.182380,4.259517,0.227239,-9.830721,-9.615874,7.511372,1.179075,0.598097,0.675280,2.251548,-1.610283,-7.810334,-7.440540,7.824912,3.374947,2.603490,-4.611711,7.541680,-6.115612,-1.887854,-8.479417,-2.953475,9.817061,0.764492,2.736610,8.829010,1.947817,-4.136929,-9.931958,4.926827,8.906968,-8.213368,7.145729,9.645141,-1.889726,-8.324330,9.147664,-8.284454,2.547838,-5.086431,0.672941,-8.263576,5.193354,-6.608445,-6.329098,-1.286616,9.393814,-2.164123,-8.702053,-0.214657,5.301998,8.072130,0.868117,-9.923024,-2.706411,0.148444,-7.874865,-8.995476,-2.406755,-6.422509,-3.807109,-9.492364,2.745938,9.931229,-8.756288,-6.990643,-2.114593,3.744194,-2.870832,-9.397886,-7.704759,-4.580777,-2.922180,-6.284634,8.370795,1.684718,9.887373,2.686639,-6.518076,-5.652757,-6.863296,0.873318,9.456599,-2.949072,-1.362832,-5.981660,-8.396739,1.075868,3.942564,1.414771,-1.777671,3.559225,-8.728597,2.710465,6.678104,-1.118621,-1.943729,-1.265847,-9.599342,3.617257,-6.117180,9.780163,-5.068420,5.000461,-5.115905,0.264254,5.977556,5.359979,2.669864,8.279858,-2.646582,8.870327,5.479904,-5.192596,-8.744604,-4.117696,3.053378,-1.675440,-9.784054,-1.467694,-8.898235,-1.762217,-9.797560,-8.973947,-5.969613,-6.881334,4.502981,6.655831,3.276673,-4.435840,-7.701731,-8.548664,-6.296366,1.436277,-6.792471,6.707192,7.527743,1.585720,2.890165,-1.421035,1.774952,0.466437,-6.858355,6.839707,-2.223162,6.833336,-3.795913,6.330302,-6.428000,1.151877,-9.131403,-4.100918,-6.225051,6.955800,3.384535,9.620308,-6.042703,6.227461,-5.663979,-7.870530,-0.600254,6.638422,-9.499472,8.316937,4.771219,7.386554,7.701986,-8.124977,2.380071,-3.078880,1.352380,4.636494,-8.988727,-2.561720,4.954346,2.943511,-8.613975,-0.120188,9.269349,-4.119556,9.425797,-5.471907,0.333098,-7.719546,-7.848255,9.986941,6.798744,5.330639,9.177369,-7.770054,2.241383,-3.264190,-5.724280,-3.735583,-8.685099], dtype = "float32")#candidate|2560|(448,)|const|float32
var_2561 = relay.var("var_2561", dtype = "int8", shape = (8, 44))#candidate|2561|(8, 44)|var|int8
call_2559 = relay.TupleGetItem(func_1118_call(relay.reshape(const_2560.astype('float32'), [8, 14, 4]), relay.reshape(const_2560.astype('float32'), [8, 14, 4]), relay.reshape(var_2561.astype('int8'), [352,]), ), 0)
call_2562 = relay.TupleGetItem(func_1122_call(relay.reshape(const_2560.astype('float32'), [8, 14, 4]), relay.reshape(const_2560.astype('float32'), [8, 14, 4]), relay.reshape(var_2561.astype('int8'), [352,]), ), 0)
uop_2566 = relay.cosh(var_2561.astype('float64')) # shape=(8, 44)
bop_2568 = relay.less_equal(uop_2550.astype('bool'), var_2561.astype('bool')) # shape=(15, 8, 44)
bop_2571 = relay.bitwise_and(bop_2568.astype('uint16'), var_2549.astype('uint16')) # shape=(15, 8, 44)
output = relay.Tuple([call_2559,const_2560,uop_2566,bop_2571,])
output2 = relay.Tuple([call_2562,const_2560,uop_2566,bop_2571,])
func_2578 = relay.Function([var_2549,var_2561,], output)
mod['func_2578'] = func_2578
mod = relay.transform.InferType()(mod)
var_2579 = relay.var("var_2579", dtype = "float64", shape = (15, 1, 1))#candidate|2579|(15, 1, 1)|var|float64
var_2580 = relay.var("var_2580", dtype = "int8", shape = (8, 44))#candidate|2580|(8, 44)|var|int8
output = func_2578(var_2579,var_2580,)
func_2581 = relay.Function([var_2579,var_2580,], output)
mutated_mod['func_2581'] = func_2581
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2630 = relay.var("var_2630", dtype = "float32", shape = (9, 15, 6))#candidate|2630|(9, 15, 6)|var|float32
uop_2631 = relay.sqrt(var_2630.astype('float32')) # shape=(9, 15, 6)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_2645 = relay.TupleGetItem(func_1502_call(), 1)
call_2646 = relay.TupleGetItem(func_1503_call(), 1)
bop_2649 = relay.bitwise_or(uop_2631.astype('uint8'), relay.reshape(var_2630.astype('uint8'), relay.shape_of(uop_2631))) # shape=(9, 15, 6)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_2652 = relay.TupleGetItem(func_365_call(), 0)
call_2653 = relay.TupleGetItem(func_366_call(), 0)
bop_2656 = relay.bitwise_xor(var_2630.astype('uint8'), relay.reshape(bop_2649.astype('uint8'), relay.shape_of(var_2630))) # shape=(9, 15, 6)
bop_2660 = relay.less_equal(uop_2631.astype('bool'), relay.reshape(var_2630.astype('bool'), relay.shape_of(uop_2631))) # shape=(9, 15, 6)
output = relay.Tuple([call_2645,call_2652,bop_2656,bop_2660,])
output2 = relay.Tuple([call_2646,call_2653,bop_2656,bop_2660,])
func_2665 = relay.Function([var_2630,], output)
mod['func_2665'] = func_2665
mod = relay.transform.InferType()(mod)
var_2666 = relay.var("var_2666", dtype = "float32", shape = (9, 15, 6))#candidate|2666|(9, 15, 6)|var|float32
output = func_2665(var_2666)
func_2667 = relay.Function([var_2666], output)
mutated_mod['func_2667'] = func_2667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1913_call = mod.get_global_var('func_1913')
func_1915_call = mutated_mod.get_global_var('func_1915')
call_2754 = func_1913_call()
call_2755 = func_1913_call()
output = relay.Tuple([call_2754,])
output2 = relay.Tuple([call_2755,])
func_2776 = relay.Function([], output)
mod['func_2776'] = func_2776
mod = relay.transform.InferType()(mod)
mutated_mod['func_2776'] = func_2776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2776_call = mutated_mod.get_global_var('func_2776')
call_2777 = func_2776_call()
output = call_2777
func_2778 = relay.Function([], output)
mutated_mod['func_2778'] = func_2778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_2795 = relay.TupleGetItem(func_1337_call(), 0)
call_2796 = relay.TupleGetItem(func_1338_call(), 0)
func_435_call = mod.get_global_var('func_435')
func_437_call = mutated_mod.get_global_var('func_437')
call_2822 = relay.TupleGetItem(func_435_call(relay.reshape(call_2795.astype('bool'), [2, 12, 9])), 0)
call_2823 = relay.TupleGetItem(func_437_call(relay.reshape(call_2795.astype('bool'), [2, 12, 9])), 0)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_2839 = relay.TupleGetItem(func_1502_call(), 1)
call_2840 = relay.TupleGetItem(func_1503_call(), 1)
output = relay.Tuple([call_2795,call_2822,call_2839,])
output2 = relay.Tuple([call_2796,call_2823,call_2840,])
func_2863 = relay.Function([], output)
mod['func_2863'] = func_2863
mod = relay.transform.InferType()(mod)
mutated_mod['func_2863'] = func_2863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mutated_mod.get_global_var('func_2863')
call_2864 = func_2863_call()
output = call_2864
func_2865 = relay.Function([], output)
mutated_mod['func_2865'] = func_2865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_2881 = relay.TupleGetItem(func_393_call(), 1)
call_2882 = relay.TupleGetItem(func_395_call(), 1)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_2893 = relay.TupleGetItem(func_542_call(), 0)
call_2894 = relay.TupleGetItem(func_543_call(), 0)
uop_2896 = relay.erf(call_2893.astype('float64')) # shape=(2, 12, 9)
uop_2898 = relay.erf(call_2894.astype('float64')) # shape=(2, 12, 9)
output = relay.Tuple([call_2881,uop_2896,])
output2 = relay.Tuple([call_2882,uop_2898,])
func_2925 = relay.Function([], output)
mod['func_2925'] = func_2925
mod = relay.transform.InferType()(mod)
mutated_mod['func_2925'] = func_2925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mutated_mod.get_global_var('func_2925')
call_2926 = func_2925_call()
output = call_2926
func_2927 = relay.Function([], output)
mutated_mod['func_2927'] = func_2927
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2987 = relay.var("var_2987", dtype = "float32", shape = ())#candidate|2987|()|var|float32
var_2988 = relay.var("var_2988", dtype = "float32", shape = (4, 15, 6))#candidate|2988|(4, 15, 6)|var|float32
bop_2989 = relay.mod(var_2987.astype('float32'), var_2988.astype('float32')) # shape=(4, 15, 6)
output = bop_2989
output2 = bop_2989
func_2995 = relay.Function([var_2987,var_2988,], output)
mod['func_2995'] = func_2995
mod = relay.transform.InferType()(mod)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mutated_mod.get_global_var('func_2995')
var_2997 = relay.var("var_2997", dtype = "float32", shape = ())#candidate|2997|()|var|float32
var_2998 = relay.var("var_2998", dtype = "float32", shape = (4, 15, 6))#candidate|2998|(4, 15, 6)|var|float32
call_2996 = func_2995_call(var_2997,var_2998,)
output = call_2996
func_2999 = relay.Function([var_2997,var_2998,], output)
mutated_mod['func_2999'] = func_2999
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3028 = relay.var("var_3028", dtype = "bool", shape = (8, 8, 13))#candidate|3028|(8, 8, 13)|var|bool
var_3029 = relay.var("var_3029", dtype = "bool", shape = (8, 8, 13))#candidate|3029|(8, 8, 13)|var|bool
bop_3030 = relay.logical_or(var_3028.astype('bool'), relay.reshape(var_3029.astype('bool'), relay.shape_of(var_3028))) # shape=(8, 8, 13)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_3046 = relay.TupleGetItem(func_365_call(), 0)
call_3047 = relay.TupleGetItem(func_366_call(), 0)
output = relay.Tuple([bop_3030,call_3046,])
output2 = relay.Tuple([bop_3030,call_3047,])
func_3055 = relay.Function([var_3028,var_3029,], output)
mod['func_3055'] = func_3055
mod = relay.transform.InferType()(mod)
mutated_mod['func_3055'] = func_3055
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3055_call = mutated_mod.get_global_var('func_3055')
var_3057 = relay.var("var_3057", dtype = "bool", shape = (8, 8, 13))#candidate|3057|(8, 8, 13)|var|bool
var_3058 = relay.var("var_3058", dtype = "bool", shape = (8, 8, 13))#candidate|3058|(8, 8, 13)|var|bool
call_3056 = func_3055_call(var_3057,var_3058,)
output = call_3056
func_3059 = relay.Function([var_3057,var_3058,], output)
mutated_mod['func_3059'] = func_3059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_3211 = func_1029_call()
call_3212 = func_1029_call()
output = relay.Tuple([call_3211,])
output2 = relay.Tuple([call_3212,])
func_3219 = relay.Function([], output)
mod['func_3219'] = func_3219
mod = relay.transform.InferType()(mod)
output = func_3219()
func_3220 = relay.Function([], output)
mutated_mod['func_3220'] = func_3220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2273_call = mod.get_global_var('func_2273')
func_2275_call = mutated_mod.get_global_var('func_2275')
call_3238 = func_2273_call()
call_3239 = func_2273_call()
output = relay.Tuple([call_3238,])
output2 = relay.Tuple([call_3239,])
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
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_3255 = func_1029_call()
call_3256 = func_1029_call()
output = relay.Tuple([call_3255,])
output2 = relay.Tuple([call_3256,])
func_3270 = relay.Function([], output)
mod['func_3270'] = func_3270
mod = relay.transform.InferType()(mod)
output = func_3270()
func_3271 = relay.Function([], output)
mutated_mod['func_3271'] = func_3271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2043_call = mod.get_global_var('func_2043')
func_2044_call = mutated_mod.get_global_var('func_2044')
call_3312 = relay.TupleGetItem(func_2043_call(), 1)
call_3313 = relay.TupleGetItem(func_2044_call(), 1)
output = call_3312
output2 = call_3313
func_3322 = relay.Function([], output)
mod['func_3322'] = func_3322
mod = relay.transform.InferType()(mod)
output = func_3322()
func_3323 = relay.Function([], output)
mutated_mod['func_3323'] = func_3323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_3416 = relay.TupleGetItem(func_1145_call(), 0)
call_3417 = relay.TupleGetItem(func_1147_call(), 0)
output = relay.Tuple([call_3416,])
output2 = relay.Tuple([call_3417,])
func_3420 = relay.Function([], output)
mod['func_3420'] = func_3420
mod = relay.transform.InferType()(mod)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3420_call = mutated_mod.get_global_var('func_3420')
call_3421 = func_3420_call()
output = call_3421
func_3422 = relay.Function([], output)
mutated_mod['func_3422'] = func_3422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2273_call = mod.get_global_var('func_2273')
func_2275_call = mutated_mod.get_global_var('func_2275')
call_3483 = func_2273_call()
call_3484 = func_2273_call()
func_1774_call = mod.get_global_var('func_1774')
func_1776_call = mutated_mod.get_global_var('func_1776')
call_3499 = relay.TupleGetItem(func_1774_call(relay.reshape(call_3483.astype('bool'), [2, 12, 9])), 0)
call_3500 = relay.TupleGetItem(func_1776_call(relay.reshape(call_3483.astype('bool'), [2, 12, 9])), 0)
func_452_call = mod.get_global_var('func_452')
func_455_call = mutated_mod.get_global_var('func_455')
const_3519 = relay.const(-4, dtype = "uint8")#candidate|3519|()|const|uint8
const_3520 = relay.const([8,-5,6,-6,7,6,-6,4,-10,6,1,4,2,7,2,9,9,-3,-8,-10,4,6,-3,-1,-3,-2,8,6,-3,-5,-8,3,8,2,4,10,-8,-9,7,5,-10,6,4,-8,-8,-9,5,6,9,-1,8,10,-8,-6,-10,8,-9,-8,8,-1,8,5,-4,-9,6,4,1,-1,-5,-7,9,7,-10,10,-10,6,-3,-3,1,9,-2,-1,-9,6,-1,-2,-8,6,-5,-8,9,5,5,8,10,3,-10,-8,9,4,-7,-8,-5,-3,-3,7,4,-4,10,7,9,5,-6,-8,-7,7,-1,10,-1,8,3,8,5,-6,-5,-6,-3,-4,2,-6,-6,-6,7,-3,-9,4,6,9,7,-6,-10,-9,-3,-6,6,-5,-4,-7,7,1,3,-7,-1,-2,-6,3,3,1,-4,1,8,2,7,4,1,7,3,5,-2,4,-5,4,-8,2,-3,-2,8,-2,3,-6,-3,2,-9,-2,4,-9,-5,-7,-9,5,-1,-2,10,4,9,-2,5,8,1,-4,-8,-1,5,5,6,-5,-8,-6,10,4,1,4,9,9,4,2,6,6,-1,9,-1,-4,3,7,-3,-5,-10,10,10,9,5,-7,-7,4,6,-7,10,-5,-5,-6,-7,3,-9,5,4,-5,-9,10,7,-6,-9,-7,-6,2,7,2,-9,9,7,7,-2,-10,5,7,-6,-5,5,6,6,-7,-7,7,3,6,-2,3,7,4,-5,-6,-1,-8,4,-2,-5,3,7,10,6,9,-2,3,-6,-3,-8,-2,1,7,-5,4,-9,3,-7,-3,-10,-4,-5,-2,-3,-1,-6,-2,-2,-10,10,-8,1,5,6,-4,2,-9,-4,-7,-7,-10,9,10,10,2,-6,-9,2,6,3,6,-5,-10,7,-7,-6,-9,-6,-10,-1,-8,-3,-3,-2,4,-8,-9,-5,-3,10,9,7,-5,-9,1,7,6,-6,-4,-9,-4,-9,1,5,6,-3,1,3,5,9,3,-5,6,9,2,8,-4,-10,-1,-8,-8,2,-3,5,6,-3,-2,7,2,7,3,-9,-4,-1,-3,2,1,1,6,1,-2,10,-5,-1,2,-8,-5,1,5,4,8,-9,7,-3,6,6,10,-3,4,9,-1,-10,-5,6,10,8,-6,-9,7,-10,7,2,-2,2,8,-2,10,7,-3,-7,-5,-5,10,-7,-7,1,-1,-1,7,-10,5,-3,-6,-2,3,3,2,10,1,10,-2,-2,-5,7,4,-4,1,-6,8,-7,-7,3,-8,5,10,-9,-8,9,-4,5,6,-9,-9,-4,-6,9,1,5,5,-3,7,1,-5,-1,7,-8,-5,7,-5,10,4,-5,1,6,-1,-3,3,8,-2,-6,2,1,-1,9,1,-7,9,10,3,-8,-7,5,-4,-5,-1,-5,-4,-10,7,3,1,3,-2,-1,-10,-9,1,6,-8,-4,-1,2,7,2,-3,2,-7,-5,-1,-3,-9,-8,8,-6,5,7,-8,3,1,9,-2,-10,-7,7,-5,-9,-5,-3,-2,-1,-10,5,7,3,-5,2,5,-6,8,10,-4,-8,-7,1,-1,-8,-1,8,1,6,6,-1,1,-1,1,-2,2,3,10,-1,-6,-1,10,-5,-3,-6,8,-7,-7,7,2,4,-9,3,10,-10,3,-5,5,5,-10,6,-10,-6,1,-6,3,7,6,-9,4,-5,5,1,2,7,-6,-10,5,-3,9,1,1,4,-10,6,-4,-2,-2,10,-8,6,9,-8,3,-1,3,6,2,3,-3,-9,-1,10,3,-9,-7,4,-2,10,-4,-10,5,-2,6,-10,-4,7,-1,3,7,4,9,-1,10,8,4,-2,-4,7,-8,8,-7,1,4,-1,-6,-4,-5,-7,6,-9,-3,-9,-5,-6,5,-7,1,-10,2,5,-6,-4,-5,6,-6,4,-7,-6,-3,-7,8,-1,-2,5,2,-3,-10,1,-5,1,-3,-1,-1,-3,1,3,6,8,4,-3,5,7,10,-5,7,6,-2,-10,-6,-9,5,-6,-5,10,-10,-8,-6,2,-4,-2,-2,1,-7,-9,8,-10,2,-5,-10,8,5,-5,-2,-8,2,9,8,10,-3,-10,8,3,4,7,-2,-2,-3,-9,-1,-3,-6,-9,-4,-4,7,-7,2,5,9,-9,-8,-9,9,-10,-4,-5,7,7,-10,-8,4,2,-9,-1,-10,1,-1,-1,-6,-3,5,-3,2,4,2,1,-9,-10,-9,-9,1,-6,-10,-7,1,-9,7,-1,-3,-1,8,8,4,-8,-1,1,-8,-8,-6,-5,2,5,5,8,-10,-2,10,10,10,-6,-6,4,-6,2,-7,10,2,-1,-1,6,6,4,8,2,3,-10,5,-4,-6,2,5,5,7,-6,-2,2,10,8,7,7,-5,8,1,-2,10,2,-8,-3,-4,-5,-1,8,10,-3,-3,-8,7,10,-10,9,-6,5,10,9,9,2,-1,-5,-4,10,9,6,6,6,-8,-5,-7,-8,-10,-1,-3,9,1,4,2,-3,-2,9,-6,-3,1,9,-8,-3,4,-5,6,10,10,5,10,3,8,9,8,-8,-1,4,-6,8,-2,-6,9,-6,-1,-2,-10,2,-8,3,4,2,-10,5,-3,5,-5,4,10,4,-4,2,-3,3,7,7,9,9,8,-7,-6,-8,7,9,-3,-9,-1,-10,-5,-8,-9], dtype = "uint8")#candidate|3520|(1008,)|const|uint8
call_3518 = func_452_call(relay.reshape(const_3519.astype('uint8'), []), relay.reshape(const_3520.astype('uint8'), [8, 14, 9]), )
call_3521 = func_452_call(relay.reshape(const_3519.astype('uint8'), []), relay.reshape(const_3520.astype('uint8'), [8, 14, 9]), )
output = relay.Tuple([call_3483,call_3499,call_3518,const_3519,const_3520,])
output2 = relay.Tuple([call_3484,call_3500,call_3521,const_3519,const_3520,])
func_3524 = relay.Function([], output)
mod['func_3524'] = func_3524
mod = relay.transform.InferType()(mod)
output = func_3524()
func_3525 = relay.Function([], output)
mutated_mod['func_3525'] = func_3525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_3549 = relay.TupleGetItem(func_542_call(), 0)
call_3550 = relay.TupleGetItem(func_543_call(), 0)
uop_3565 = relay.rsqrt(call_3549.astype('float32')) # shape=(2, 12, 9)
uop_3567 = relay.rsqrt(call_3550.astype('float32')) # shape=(2, 12, 9)
output = relay.Tuple([uop_3565,])
output2 = relay.Tuple([uop_3567,])
func_3573 = relay.Function([], output)
mod['func_3573'] = func_3573
mod = relay.transform.InferType()(mod)
mutated_mod['func_3573'] = func_3573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3573_call = mutated_mod.get_global_var('func_3573')
call_3574 = func_3573_call()
output = call_3574
func_3575 = relay.Function([], output)
mutated_mod['func_3575'] = func_3575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_3623 = func_3322_call()
call_3624 = func_3322_call()
output = call_3623
output2 = call_3624
func_3641 = relay.Function([], output)
mod['func_3641'] = func_3641
mod = relay.transform.InferType()(mod)
mutated_mod['func_3641'] = func_3641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3641_call = mutated_mod.get_global_var('func_3641')
call_3642 = func_3641_call()
output = call_3642
func_3643 = relay.Function([], output)
mutated_mod['func_3643'] = func_3643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mod.get_global_var('func_2207')
func_2208_call = mutated_mod.get_global_var('func_2208')
call_3843 = relay.TupleGetItem(func_2207_call(), 1)
call_3844 = relay.TupleGetItem(func_2208_call(), 1)
func_1259_call = mod.get_global_var('func_1259')
func_1262_call = mutated_mod.get_global_var('func_1262')
var_3853 = relay.var("var_3853", dtype = "int8", shape = (352,))#candidate|3853|(352,)|var|int8
call_3852 = relay.TupleGetItem(func_1259_call(relay.reshape(var_3853.astype('int8'), [352,])), 0)
call_3854 = relay.TupleGetItem(func_1262_call(relay.reshape(var_3853.astype('int8'), [352,])), 0)
output = relay.Tuple([call_3843,call_3852,var_3853,])
output2 = relay.Tuple([call_3844,call_3854,var_3853,])
func_3863 = relay.Function([var_3853,], output)
mod['func_3863'] = func_3863
mod = relay.transform.InferType()(mod)
var_3864 = relay.var("var_3864", dtype = "int8", shape = (352,))#candidate|3864|(352,)|var|int8
output = func_3863(var_3864)
func_3865 = relay.Function([var_3864], output)
mutated_mod['func_3865'] = func_3865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_952_call = mod.get_global_var('func_952')
func_954_call = mutated_mod.get_global_var('func_954')
call_3907 = relay.TupleGetItem(func_952_call(), 0)
call_3908 = relay.TupleGetItem(func_954_call(), 0)
func_952_call = mod.get_global_var('func_952')
func_954_call = mutated_mod.get_global_var('func_954')
call_3945 = relay.TupleGetItem(func_952_call(), 0)
call_3946 = relay.TupleGetItem(func_954_call(), 0)
output = relay.Tuple([call_3907,call_3945,])
output2 = relay.Tuple([call_3908,call_3946,])
func_3953 = relay.Function([], output)
mod['func_3953'] = func_3953
mod = relay.transform.InferType()(mod)
output = func_3953()
func_3954 = relay.Function([], output)
mutated_mod['func_3954'] = func_3954
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3953_call = mod.get_global_var('func_3953')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_3955 = relay.TupleGetItem(func_3953_call(), 0)
call_3956 = relay.TupleGetItem(func_3954_call(), 0)
output = call_3955
output2 = call_3956
func_3961 = relay.Function([], output)
mod['func_3961'] = func_3961
mod = relay.transform.InferType()(mod)
output = func_3961()
func_3962 = relay.Function([], output)
mutated_mod['func_3962'] = func_3962
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3219_call = mod.get_global_var('func_3219')
func_3220_call = mutated_mod.get_global_var('func_3220')
call_4021 = relay.TupleGetItem(func_3219_call(), 0)
call_4022 = relay.TupleGetItem(func_3220_call(), 0)
output = relay.Tuple([call_4021,])
output2 = relay.Tuple([call_4022,])
func_4023 = relay.Function([], output)
mod['func_4023'] = func_4023
mod = relay.transform.InferType()(mod)
mutated_mod['func_4023'] = func_4023
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mutated_mod.get_global_var('func_4023')
call_4024 = func_4023_call()
output = call_4024
func_4025 = relay.Function([], output)
mutated_mod['func_4025'] = func_4025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3573_call = mod.get_global_var('func_3573')
func_3575_call = mutated_mod.get_global_var('func_3575')
call_4031 = relay.TupleGetItem(func_3573_call(), 0)
call_4032 = relay.TupleGetItem(func_3575_call(), 0)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_4048 = relay.TupleGetItem(func_3252_call(), 0)
call_4049 = relay.TupleGetItem(func_3254_call(), 0)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_4051 = relay.TupleGetItem(func_4023_call(), 0)
call_4052 = relay.TupleGetItem(func_4025_call(), 0)
output = relay.Tuple([call_4031,call_4048,call_4051,])
output2 = relay.Tuple([call_4032,call_4049,call_4052,])
func_4057 = relay.Function([], output)
mod['func_4057'] = func_4057
mod = relay.transform.InferType()(mod)
mutated_mod['func_4057'] = func_4057
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mutated_mod.get_global_var('func_4057')
call_4058 = func_4057_call()
output = call_4058
func_4059 = relay.Function([], output)
mutated_mod['func_4059'] = func_4059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_4096 = relay.TupleGetItem(func_2467_call(), 0)
call_4097 = relay.TupleGetItem(func_2468_call(), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_4102 = relay.const([[True,True],[False,False],[False,False],[False,False],[False,False],[True,False],[True,False],[True,True],[False,True],[True,False],[True,True],[False,False],[False,False],[False,False],[False,True],[False,True],[True,False],[False,True],[False,False],[True,True],[False,True],[True,True],[True,False],[False,True],[True,True],[False,False],[True,False],[True,True],[False,True],[True,False],[True,False],[True,False],[False,True],[True,True],[True,True],[False,True],[False,True],[False,True],[True,False],[True,False],[False,True],[False,True],[True,True],[False,True],[True,True],[True,False],[True,False],[False,False],[False,True],[True,True],[False,True],[True,False],[False,True],[False,True],[False,True],[True,False],[False,True],[True,True],[True,True],[False,False],[False,True],[False,False],[True,False],[False,True],[True,True],[True,False],[False,False],[False,False],[True,False],[True,True],[True,False],[True,True],[True,False],[False,False],[True,False],[False,False],[True,False],[False,True],[False,False],[False,False],[True,True],[False,True],[True,False],[True,True],[True,False],[False,False],[False,False],[False,True],[False,False],[False,False],[True,False],[False,False],[True,False],[True,True],[False,False],[True,True],[True,True],[False,True],[False,True],[False,True],[True,False],[True,True],[False,True],[False,True],[False,False],[True,True],[True,True],[True,False],[True,True],[True,True],[True,True],[False,False],[False,False],[True,False],[True,True],[True,False],[False,True],[True,False],[False,True],[True,False],[False,False],[True,True],[True,True],[True,False],[False,False],[True,True],[True,True],[True,False],[True,True],[False,False],[False,False],[False,False],[True,True],[True,True],[True,False],[False,True],[True,True],[False,False],[False,True],[True,False],[True,False],[True,True],[False,True],[True,True],[False,True],[False,False],[True,False],[True,False],[False,False],[False,True],[False,False],[False,True],[True,False],[False,False],[True,True],[False,False],[True,False],[True,True],[True,False],[True,True],[False,True],[True,True],[True,False],[False,True],[False,False],[False,True],[False,False],[False,True],[False,False],[True,True],[True,False],[False,True],[False,True],[False,True],[False,True],[False,False],[False,True],[True,False],[False,True],[True,False],[True,False],[True,True],[False,False],[True,True],[False,False],[False,False],[False,False],[True,False],[False,True],[True,False],[True,True],[False,True],[True,True],[True,True],[True,True],[True,False],[True,True],[False,True],[True,True],[False,True],[True,True],[True,False],[True,False],[False,True],[False,False],[True,True],[True,True],[False,False],[True,False],[True,False],[True,True],[False,False],[False,False],[True,True],[True,False],[False,True],[True,False],[True,False],[False,True],[False,False],[True,True],[True,True],[True,False],[True,False],[False,True],[False,True],[False,False],[True,False],[True,False],[True,False],[False,True],[True,True],[True,False],[False,False],[False,False],[False,True],[True,False],[False,False],[False,False],[False,False],[True,False],[True,True],[True,False],[True,False],[False,False],[False,True],[True,False],[False,True],[False,False],[True,False],[False,True],[False,False],[True,False],[False,True],[False,True],[True,True],[True,False],[False,False],[False,True],[False,True],[True,True],[False,True],[True,False],[False,True],[True,True],[False,True],[False,False],[True,False],[False,False],[True,True],[True,True],[False,False],[True,True],[True,False],[False,True],[True,False],[False,True],[True,True],[True,True],[True,False],[False,True],[False,False],[True,True],[False,True],[True,False],[False,False],[True,True],[True,False],[False,False],[False,False],[True,True],[False,False],[False,True],[True,False],[False,False],[False,False],[True,False],[True,False],[False,True],[False,True],[True,False],[False,False],[True,True],[True,True],[True,True],[False,False],[True,False],[False,True],[False,False],[True,False],[False,False],[True,False],[False,False],[False,False],[True,False],[False,True],[True,False],[True,False],[True,False],[False,False],[False,False],[False,True],[False,True],[False,False],[True,False],[True,True],[False,False],[True,False],[False,False],[True,True],[False,True],[False,True],[True,False],[False,False],[False,False],[False,False],[False,False],[True,False],[True,False],[True,False],[False,False],[False,False],[False,True],[False,False],[True,True],[True,False],[False,False],[True,True],[False,True],[True,False],[True,True],[True,True],[False,False],[False,True],[False,True],[False,False],[True,False],[False,True],[True,True],[True,True],[False,False],[True,True],[False,False],[False,False],[False,False],[True,True],[True,False],[True,True],[False,True],[True,True],[False,True],[True,True],[True,False],[False,False],[True,True],[True,True],[True,False],[False,False],[True,True],[False,True],[True,True],[False,False],[True,True],[False,False],[False,True],[True,False],[False,False],[True,True],[False,True],[True,True],[False,True],[True,False],[True,True],[False,False],[False,False],[True,True],[False,False],[False,True],[True,False],[True,False],[True,False],[False,True],[True,False],[False,True],[True,True],[True,False],[False,False],[False,False],[True,False],[False,False],[False,False],[True,False],[False,True],[False,True],[True,True],[True,False]], dtype = "bool")#candidate|4102|(416, 2)|const|bool
call_4101 = relay.TupleGetItem(func_3055_call(relay.reshape(const_4102.astype('bool'), [8, 8, 13]), relay.reshape(const_4102.astype('bool'), [8, 8, 13]), ), 0)
call_4103 = relay.TupleGetItem(func_3059_call(relay.reshape(const_4102.astype('bool'), [8, 8, 13]), relay.reshape(const_4102.astype('bool'), [8, 8, 13]), ), 0)
uop_4108 = relay.acosh(const_4102.astype('float64')) # shape=(416, 2)
var_4110 = relay.var("var_4110", dtype = "float64", shape = (416, 2))#candidate|4110|(416, 2)|var|float64
bop_4111 = relay.mod(uop_4108.astype('float64'), relay.reshape(var_4110.astype('float64'), relay.shape_of(uop_4108))) # shape=(416, 2)
output = relay.Tuple([call_4096,call_4101,bop_4111,])
output2 = relay.Tuple([call_4097,call_4103,bop_4111,])
func_4132 = relay.Function([var_4110,], output)
mod['func_4132'] = func_4132
mod = relay.transform.InferType()(mod)
var_4133 = relay.var("var_4133", dtype = "float64", shape = (416, 2))#candidate|4133|(416, 2)|var|float64
output = func_4132(var_4133)
func_4134 = relay.Function([var_4133], output)
mutated_mod['func_4134'] = func_4134
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_4136 = relay.TupleGetItem(func_1145_call(), 0)
call_4137 = relay.TupleGetItem(func_1147_call(), 0)
output = relay.Tuple([call_4136,])
output2 = relay.Tuple([call_4137,])
func_4142 = relay.Function([], output)
mod['func_4142'] = func_4142
mod = relay.transform.InferType()(mod)
mutated_mod['func_4142'] = func_4142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4142_call = mutated_mod.get_global_var('func_4142')
call_4143 = func_4142_call()
output = call_4143
func_4144 = relay.Function([], output)
mutated_mod['func_4144'] = func_4144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3270_call = mod.get_global_var('func_3270')
func_3271_call = mutated_mod.get_global_var('func_3271')
call_4184 = relay.TupleGetItem(func_3270_call(), 0)
call_4185 = relay.TupleGetItem(func_3271_call(), 0)
output = relay.Tuple([call_4184,])
output2 = relay.Tuple([call_4185,])
func_4189 = relay.Function([], output)
mod['func_4189'] = func_4189
mod = relay.transform.InferType()(mod)
output = func_4189()
func_4190 = relay.Function([], output)
mutated_mod['func_4190'] = func_4190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_4218 = func_1581_call()
call_4219 = func_1581_call()
output = relay.Tuple([call_4218,])
output2 = relay.Tuple([call_4219,])
func_4222 = relay.Function([], output)
mod['func_4222'] = func_4222
mod = relay.transform.InferType()(mod)
output = func_4222()
func_4223 = relay.Function([], output)
mutated_mod['func_4223'] = func_4223
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_4232 = relay.TupleGetItem(func_1454_call(), 0)
call_4233 = relay.TupleGetItem(func_1456_call(), 0)
output = relay.Tuple([call_4232,])
output2 = relay.Tuple([call_4233,])
func_4240 = relay.Function([], output)
mod['func_4240'] = func_4240
mod = relay.transform.InferType()(mod)
output = func_4240()
func_4241 = relay.Function([], output)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4246 = relay.var("var_4246", dtype = "uint64", shape = (6, 1, 10))#candidate|4246|(6, 1, 10)|var|uint64
var_4247 = relay.var("var_4247", dtype = "uint64", shape = (6, 2, 10))#candidate|4247|(6, 2, 10)|var|uint64
bop_4248 = relay.greater(var_4246.astype('bool'), var_4247.astype('bool')) # shape=(6, 2, 10)
output = relay.Tuple([bop_4248,])
output2 = relay.Tuple([bop_4248,])
func_4263 = relay.Function([var_4246,var_4247,], output)
mod['func_4263'] = func_4263
mod = relay.transform.InferType()(mod)
var_4264 = relay.var("var_4264", dtype = "uint64", shape = (6, 1, 10))#candidate|4264|(6, 1, 10)|var|uint64
var_4265 = relay.var("var_4265", dtype = "uint64", shape = (6, 2, 10))#candidate|4265|(6, 2, 10)|var|uint64
output = func_4263(var_4264,var_4265,)
func_4266 = relay.Function([var_4264,var_4265,], output)
mutated_mod['func_4266'] = func_4266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3420_call = mod.get_global_var('func_3420')
func_3422_call = mutated_mod.get_global_var('func_3422')
call_4299 = relay.TupleGetItem(func_3420_call(), 0)
call_4300 = relay.TupleGetItem(func_3422_call(), 0)
output = call_4299
output2 = call_4300
func_4307 = relay.Function([], output)
mod['func_4307'] = func_4307
mod = relay.transform.InferType()(mod)
mutated_mod['func_4307'] = func_4307
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4307_call = mutated_mod.get_global_var('func_4307')
call_4308 = func_4307_call()
output = call_4308
func_4309 = relay.Function([], output)
mutated_mod['func_4309'] = func_4309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3524_call = mod.get_global_var('func_3524')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_4429 = relay.TupleGetItem(func_3524_call(), 2)
call_4430 = relay.TupleGetItem(func_3525_call(), 2)
func_4132_call = mod.get_global_var('func_4132')
func_4134_call = mutated_mod.get_global_var('func_4134')
const_4439 = relay.const([[-5.904785,4.188159,-1.873987,9.290168,-8.452048,3.832622,9.299734,9.954669,7.779375,8.773059,2.675739,2.353622,4.374451,-0.836812,-1.060124,8.974137,3.243539,2.671976,-9.661055,2.767759,-5.449079,5.835231,2.835728,3.149138,7.136473,-3.250804,4.135635,-2.032317,9.737826,-1.553642,-9.921385,-1.389078,3.859500,3.899023,-0.298321,-5.001834,0.311656,-1.148526,-2.877154,3.836182,0.661638,-9.183368,9.044718,0.119927,-1.068686,2.534499,3.366326,-5.710094,9.716140,-0.676727,9.052039,9.463306,6.267419,3.691822,3.399009,2.121391,-8.832542,2.747390,0.445576,-3.644173,6.395256,-4.092027,8.160284,4.178055,-6.805519,9.762572,-4.134895,-2.066898,-5.840258,5.970040,-3.257359,-6.536170,-3.902144,5.695640,-0.538108,8.466557,4.128395,-2.504765,3.082059,7.406611,-2.577673,0.664473,7.584772,-1.949884,6.727113,3.784349,-3.627502,-0.049732,-1.481934,-1.989909,-8.629468,-8.632271,9.166780,-6.635006,-9.273696,-0.442188,-8.960856,7.977940,9.528977,-6.389478,7.759016,3.313242,4.311491,-5.015499,5.075377,4.943788,4.385379,6.209180,-7.670648,9.573047,0.255491,8.107396,0.203708,-4.355323,-2.414943,7.880646,-3.437867,-7.815225,-2.795555,7.686526,7.504518,1.634275,-4.470298,-1.946067,1.059162,1.894181,8.805316,-0.914109,1.452302,-9.537944,8.253737,7.337372,-8.079400,-0.196146,7.816326,-2.728099,-3.749180,9.350421,-4.470353,2.716783,6.619434,-1.439388,-9.378083,1.638902,9.552828,5.513752,2.416444,2.125630,-9.879113,-5.903626,0.759795,7.897470,7.193506,8.145943,-4.170002,6.584648,9.315881,-7.993665,-6.023714,-1.707878,9.902235,2.124691,-1.249975,-5.826865,-5.183142,-7.324356,4.192073,0.074204,-5.312134,-7.475392,3.594766,-8.718652,-0.368478,-0.014586,-0.626082,-7.575442,8.111846,-0.979991,-0.693068,-4.750407,-4.640308,0.043427,-3.495253,-3.307682,4.703517,5.758771,-9.538361,9.347011,9.219740,0.662906,-6.415926,1.488082,9.508359,-8.486693,2.561814,-1.123229,6.849917,6.957234,-2.725309,8.605293,7.184769,6.524740,-1.630569,-7.426095,-2.003490,-2.435950,3.701471,-4.545463,0.092013,8.850416,-3.012493,-4.883827,8.955227,5.462922,9.295778,1.804152,-0.521765,-9.764657,5.835189,-0.815431,7.769563,9.287003,-9.521361,2.024779,-8.028099,-2.393992,4.557004,-1.818702,3.417658,-6.048848,-4.529274,5.965554,-1.909859,-8.262286,-5.251311,-1.323008,4.270665,-0.518564,8.211788,7.653940,-9.949790,-5.437781,5.236716,-3.844524,8.169085,6.724142,-4.674899,-0.797855,3.476606,0.628711,3.563696,4.516222,2.117727,-2.719509,0.990291,-7.586781,-1.764224,0.825591,7.583298,-7.053360,1.800421,4.333566,-2.730890,-5.113630,-6.460288,1.243570,3.076995,-1.380128,-1.246483,-5.957398,-3.226827,-6.952317,1.849287,-1.577406,0.022215,4.462338,4.569572,7.975254,-6.871214,5.611535,2.779999,-7.486048,1.997839,3.011662,-7.888481,3.251100,-6.788804,0.069639,-2.602808,-6.804533,-1.733235,-4.448394,-2.380814,0.732558,3.873941,0.380220,1.955289,-8.608107,-7.960943,-1.091607,3.851978,-6.326415,8.649704,3.936113,7.125243,-8.409000,-2.645783,7.939720,-0.678913,8.038404,9.679851,-7.492069,8.033198,6.774369,-7.817017,-7.933333,-1.598577,6.997514,-2.062258,4.165901,-1.875011,4.627232,-1.501465,-3.866597,5.760152,-4.842349,-0.833310,5.348613,6.528544,-2.562788,-1.571624,3.008595,5.306788,9.155617,-8.274213,4.250499,-8.534223,4.982221,-2.064205,3.831870,5.368850,-7.135857,-1.282711,7.385115,5.108110,6.551205,-3.386977,-3.939477,5.872564,4.091266,-3.883086,-4.183440,7.363389,0.882663,9.192017,7.288542,-0.040356,2.715210,6.327165,4.347045,-8.981925,9.971998,9.526517,-7.586625,8.090258,-6.111765,-1.172074,-0.442852,-8.630254,1.684211,-0.196391,2.700757,4.832955,1.149750,2.354670,2.360447,9.390855,4.385568,-0.838302,7.685663,6.971703,6.816668,-1.770691,-7.619510,1.044857,1.059001,-8.499608,-6.484092,0.889224,8.408387,-9.296566,-0.588568,6.602351,1.458681,2.763110,8.081099,-8.734808,-5.237114,-5.004549,-2.604256,7.590743,8.619419,-6.110352,6.099302,8.454996,-0.435608,9.218774,8.074922,-1.786412,-9.615371,2.624404,0.984456,-6.166306,-6.755791,-2.328444,-7.127499],[-0.614773,3.158433,5.536788,-3.616721,3.665159,0.077360,6.820794,0.454861,1.503700,4.050666,9.055563,-6.415088,6.816602,-8.724298,4.563145,0.149432,-6.006515,-3.648154,7.285615,-9.788507,-1.369478,5.497710,-4.325157,6.908578,-5.827462,-6.163218,0.131795,4.485331,-2.051836,-9.642882,-1.285118,2.051760,8.563963,-1.150564,9.420449,7.414750,-0.588504,4.355384,-8.265831,-1.362944,-1.260323,-2.226587,-9.418938,-8.105276,-6.302080,-4.378720,-2.733750,7.529435,-8.285043,-4.116193,1.044055,5.547280,-1.669499,-7.919993,1.934065,9.363973,-2.259418,-8.730216,3.330252,2.103040,8.673825,-5.619038,7.812340,2.433038,5.443410,6.656880,-5.471655,9.099804,-9.635411,4.500381,-4.369708,6.628496,-5.552117,7.307496,-3.549493,6.583381,3.386700,7.890853,-5.038281,-9.737472,-5.246574,-0.716479,-5.842384,3.083045,9.375384,-9.436718,2.679525,-2.987443,8.671713,7.672352,-3.020921,-2.582187,-3.993785,8.993448,-9.099112,-6.563586,5.394664,4.190396,-0.557700,-4.541818,9.418783,-7.837046,-9.930680,6.133698,-0.693321,8.573947,3.796553,-7.541552,9.825974,-2.268810,9.697025,-4.141469,9.895191,-1.800666,-2.825501,-1.909859,-4.487016,-0.229193,0.837491,-3.370460,-1.645483,2.973011,3.359066,7.237800,2.989029,4.741521,2.512952,7.782361,1.818052,-5.186005,0.140034,-2.163260,1.890189,-9.698171,-9.765225,3.747887,9.733652,-6.588967,-2.130992,7.137643,-1.286284,1.139253,7.024962,-1.004251,-7.448141,-0.465339,0.650682,0.831048,-5.712246,-1.221063,2.886578,5.651954,-2.025953,2.505303,-1.761391,-2.044940,2.277794,-9.344830,-3.351100,-3.187559,2.336102,-5.909225,2.811693,-7.430640,-2.131577,-0.319911,-6.263575,-9.401979,5.463531,9.935227,-0.805393,-0.011512,1.860699,-2.822764,-1.117443,9.137611,-0.808863,-2.343063,3.427198,2.460818,1.088542,4.727454,0.409007,-2.951490,-0.669255,-8.834129,4.959858,-5.791379,5.104535,8.679512,9.019511,-6.534198,-8.822863,7.525697,5.426624,4.250055,-1.662798,-4.974433,-8.214646,5.915741,-0.982853,-5.621403,-8.415668,5.355946,5.231705,6.709932,1.069925,-0.619788,1.417529,1.011439,-8.240630,1.133676,-7.910382,1.535527,4.334068,6.277974,-5.313392,4.255265,-3.955874,9.249410,5.529102,6.101803,-9.392342,6.206378,7.961909,-8.143910,9.956565,3.570595,7.192207,7.815432,5.246803,-9.882764,-7.617767,-5.880561,-0.234098,-9.570182,8.245960,-3.838014,-8.730975,3.729619,3.505160,2.437912,4.322982,-9.461915,6.433539,6.515947,-7.683079,8.146998,-3.754691,7.623318,9.988460,-2.358600,0.714450,-9.541609,-5.212093,-7.643193,5.486788,5.168085,-9.677628,4.269105,3.746540,-2.151841,-3.216315,-1.646583,6.236252,-3.193954,9.518132,7.703550,6.395945,-6.112913,6.825878,4.019663,5.609832,-2.357302,-6.297509,3.485743,-3.904146,1.200279,4.563731,7.135855,-6.433336,5.874611,1.360158,-8.638844,-1.155981,-5.671641,7.490132,-0.381586,-6.740880,-2.593074,-9.219352,-8.277853,2.691609,-3.647042,5.649889,-5.528381,4.738220,-8.366400,-3.841774,6.414445,8.772709,5.554875,-8.106754,2.306474,-0.870637,7.516038,-1.937103,0.442704,-4.586756,-3.141070,-7.431429,3.351741,1.678108,-0.729555,-8.969593,-3.267186,0.476204,0.083493,-7.358416,9.167248,-6.509362,8.932141,-6.718113,3.416156,-8.154768,0.143210,-7.529326,-2.191315,-0.595073,9.608848,0.706159,-2.414914,4.257088,-3.034704,8.530501,-1.007498,-6.348227,-8.501466,6.054166,6.517437,2.306236,-0.151520,2.605398,2.496914,5.656635,9.427450,1.511171,7.493939,9.281101,-9.675935,9.683320,-7.699712,-9.415969,0.419148,-0.816013,-1.226433,1.227241,5.976422,9.988740,-0.685906,-6.165590,2.105211,4.581048,-8.868366,-2.904682,9.948540,-7.471035,-6.310016,-2.776676,-0.444671,-4.465339,4.787552,9.974305,6.515830,3.243441,7.246378,9.474744,6.195070,2.328474,3.251725,-2.271186,-7.902217,-4.006001,-4.430733,-1.988360,-9.313961,1.854708,-2.969076,-1.230766,1.392800,1.199190,0.880696,-8.500858,8.947086,5.147118,7.149534,-2.249291,-5.622403,-1.745929,6.859542,9.450260,-9.084684,1.646911,0.841619,-7.466772,-9.831295,3.324555,-8.704766,-3.791428,7.748700,-3.238632,-6.031684,-4.840062,4.618663,3.801576,8.749423]], dtype = "float64")#candidate|4439|(2, 416)|const|float64
call_4438 = relay.TupleGetItem(func_4132_call(relay.reshape(const_4439.astype('float64'), [416, 2])), 1)
call_4440 = relay.TupleGetItem(func_4134_call(relay.reshape(const_4439.astype('float64'), [416, 2])), 1)
output = relay.Tuple([call_4429,call_4438,const_4439,])
output2 = relay.Tuple([call_4430,call_4440,const_4439,])
func_4448 = relay.Function([], output)
mod['func_4448'] = func_4448
mod = relay.transform.InferType()(mod)
output = func_4448()
func_4449 = relay.Function([], output)
mutated_mod['func_4449'] = func_4449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_4469 = relay.TupleGetItem(func_1337_call(), 0)
call_4470 = relay.TupleGetItem(func_1338_call(), 0)
var_4488 = relay.var("var_4488", dtype = "float64", shape = (2, 12, 9))#candidate|4488|(2, 12, 9)|var|float64
bop_4489 = relay.floor_divide(call_4469.astype('float64'), relay.reshape(var_4488.astype('float64'), relay.shape_of(call_4469))) # shape=(2, 12, 9)
bop_4492 = relay.floor_divide(call_4470.astype('float64'), relay.reshape(var_4488.astype('float64'), relay.shape_of(call_4470))) # shape=(2, 12, 9)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_4493 = relay.TupleGetItem(func_1454_call(), 0)
call_4494 = relay.TupleGetItem(func_1456_call(), 0)
func_4132_call = mod.get_global_var('func_4132')
func_4134_call = mutated_mod.get_global_var('func_4134')
var_4501 = relay.var("var_4501", dtype = "float64", shape = (208, 4))#candidate|4501|(208, 4)|var|float64
call_4500 = relay.TupleGetItem(func_4132_call(relay.reshape(var_4501.astype('float64'), [416, 2])), 0)
call_4502 = relay.TupleGetItem(func_4134_call(relay.reshape(var_4501.astype('float64'), [416, 2])), 0)
func_4448_call = mod.get_global_var('func_4448')
func_4449_call = mutated_mod.get_global_var('func_4449')
call_4531 = relay.TupleGetItem(func_4448_call(), 2)
call_4532 = relay.TupleGetItem(func_4449_call(), 2)
output = relay.Tuple([bop_4489,call_4493,call_4500,var_4501,call_4531,])
output2 = relay.Tuple([bop_4492,call_4494,call_4502,var_4501,call_4532,])
func_4541 = relay.Function([var_4488,var_4501,], output)
mod['func_4541'] = func_4541
mod = relay.transform.InferType()(mod)
var_4542 = relay.var("var_4542", dtype = "float64", shape = (2, 12, 9))#candidate|4542|(2, 12, 9)|var|float64
var_4543 = relay.var("var_4543", dtype = "float64", shape = (208, 4))#candidate|4543|(208, 4)|var|float64
output = func_4541(var_4542,var_4543,)
func_4544 = relay.Function([var_4542,var_4543,], output)
mutated_mod['func_4544'] = func_4544
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_4584 = relay.TupleGetItem(func_2776_call(), 0)
call_4585 = relay.TupleGetItem(func_2778_call(), 0)
func_342_call = mod.get_global_var('func_342')
func_344_call = mutated_mod.get_global_var('func_344')
call_4597 = relay.TupleGetItem(func_342_call(), 2)
call_4598 = relay.TupleGetItem(func_344_call(), 2)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_4613 = relay.TupleGetItem(func_595_call(), 1)
call_4614 = relay.TupleGetItem(func_596_call(), 1)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_4620 = relay.TupleGetItem(func_1454_call(), 0)
call_4621 = relay.TupleGetItem(func_1456_call(), 0)
output = relay.Tuple([call_4584,call_4597,call_4613,call_4620,])
output2 = relay.Tuple([call_4585,call_4598,call_4614,call_4621,])
func_4638 = relay.Function([], output)
mod['func_4638'] = func_4638
mod = relay.transform.InferType()(mod)
mutated_mod['func_4638'] = func_4638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4638_call = mutated_mod.get_global_var('func_4638')
call_4639 = func_4638_call()
output = call_4639
func_4640 = relay.Function([], output)
mutated_mod['func_4640'] = func_4640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3219_call = mod.get_global_var('func_3219')
func_3220_call = mutated_mod.get_global_var('func_3220')
call_4643 = relay.TupleGetItem(func_3219_call(), 0)
call_4644 = relay.TupleGetItem(func_3220_call(), 0)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
var_4657 = relay.var("var_4657", dtype = "bool", shape = (2, 416))#candidate|4657|(2, 416)|var|bool
call_4656 = relay.TupleGetItem(func_3055_call(relay.reshape(var_4657.astype('bool'), [8, 8, 13]), relay.reshape(var_4657.astype('bool'), [8, 8, 13]), ), 1)
call_4658 = relay.TupleGetItem(func_3059_call(relay.reshape(var_4657.astype('bool'), [8, 8, 13]), relay.reshape(var_4657.astype('bool'), [8, 8, 13]), ), 1)
output = relay.Tuple([call_4643,call_4656,var_4657,])
output2 = relay.Tuple([call_4644,call_4658,var_4657,])
func_4663 = relay.Function([var_4657,], output)
mod['func_4663'] = func_4663
mod = relay.transform.InferType()(mod)
var_4664 = relay.var("var_4664", dtype = "bool", shape = (2, 416))#candidate|4664|(2, 416)|var|bool
output = func_4663(var_4664)
func_4665 = relay.Function([var_4664], output)
mutated_mod['func_4665'] = func_4665
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4696 = relay.const([[[1,-2,-8,-2,8],[10,9,3,-8,6],[1,-4,-4,-4,-9],[3,-2,8,10,10],[-5,-3,-2,-2,3],[2,-7,-7,-1,2],[-5,-2,7,-9,-10],[-4,9,1,-2,-2],[4,-8,-10,2,7],[3,-6,-1,5,-2],[10,1,-3,-1,-7]]], dtype = "int32")#candidate|4696|(1, 11, 5)|const|int32
const_4697 = relay.const([[[8,-2,6,10,-5],[-7,10,-6,1,1],[3,-3,6,5,-8],[7,-6,4,3,7],[-9,-9,-6,5,4],[-9,9,7,-7,-1],[7,-2,-8,-8,2],[-9,2,1,4,5],[1,-8,5,6,-6],[-8,-8,9,-7,-5],[2,4,-3,-10,-1]],[[6,9,10,9,-10],[6,9,8,-8,-7],[-6,8,-1,-4,-7],[-7,5,-6,4,5],[-10,1,3,-9,6],[7,-5,3,7,10],[-10,-8,5,-4,-9],[4,-9,1,6,-6],[-8,-4,9,8,5],[-9,-4,-2,1,1],[-4,-9,2,7,-2]],[[8,-8,-10,10,-3],[7,-9,-1,2,-8],[1,-8,7,2,7],[8,3,-10,3,4],[-6,-9,2,8,1],[-6,10,-7,-7,-2],[5,2,8,-3,-3],[-6,-8,5,-5,3],[-3,-10,-7,1,-8],[-8,4,10,-1,10],[2,4,3,9,6]],[[-3,4,-1,10,5],[-2,-10,-3,8,-7],[-8,6,-10,-3,6],[2,-6,5,-7,9],[5,-5,10,7,-9],[-6,-3,1,3,2],[-1,1,9,7,2],[-8,-7,-2,-10,-5],[-1,-8,-5,-8,2],[8,-2,-1,4,9],[-1,-1,-1,-7,1]],[[-1,-1,1,-9,4],[8,-3,8,5,1],[8,-2,-2,3,3],[-1,10,-5,-10,9],[4,-4,8,-2,-6],[7,-6,-4,-2,-10],[-4,-9,-3,-5,-7],[-6,10,9,-4,2],[-3,-5,-8,9,-9],[-4,10,-5,-8,-5],[-5,-7,1,-4,6]],[[-8,-3,-7,-3,2],[7,-2,9,-9,10],[-1,5,9,-3,-4],[6,-7,-4,-1,-5],[8,9,7,1,-5],[2,-5,4,-4,6],[-8,-9,-3,-1,1],[-7,8,-2,4,-10],[6,4,8,5,9],[-1,6,-3,-4,-3],[-2,5,6,4,-3]],[[-10,-6,-8,6,-8],[9,-1,-3,1,-1],[-4,5,-3,-9,3],[-1,8,-7,4,4],[-6,5,-5,4,-6],[10,-7,9,6,-7],[1,9,-7,-8,10],[5,4,-7,-6,6],[-7,-2,-1,-4,-1],[7,-9,1,-5,-7],[10,4,9,4,-2]],[[7,-9,4,2,-9],[9,4,4,-5,4],[-5,3,-10,-1,-10],[-5,2,6,5,6],[-10,2,6,-1,5],[3,2,7,10,4],[-3,-9,-4,3,-4],[5,-5,-9,-3,9],[6,5,-10,7,2],[-2,-4,-10,-7,-10],[-1,4,-2,-4,-3]],[[-2,-9,-6,1,10],[7,-8,4,-1,-8],[-9,-8,4,8,-6],[3,10,4,2,1],[9,-6,1,5,-1],[5,-4,5,-4,8],[-3,-9,-4,9,10],[-9,-8,-8,-5,2],[-7,-7,1,-1,-6],[8,-1,-10,-2,2],[-9,-5,-6,-7,-7]],[[10,-6,-7,1,-6],[6,-6,-1,-5,-5],[6,-9,-2,-5,7],[-6,8,-6,-2,2],[5,2,-8,-6,-9],[-9,7,-8,-5,8],[7,-1,-7,-9,-5],[7,-10,9,-5,10],[-10,-8,8,-7,-9],[7,8,-10,-4,-6],[-1,-8,5,10,4]],[[1,-10,10,5,3],[2,-9,-7,-7,-1],[3,-9,4,10,-1],[3,-10,-9,4,-10],[7,8,-4,8,-9],[8,10,3,-9,-7],[9,10,-6,2,4],[-7,-5,8,2,-3],[-4,1,6,9,8],[6,7,-1,-9,-3],[6,-6,6,2,-2]]], dtype = "int32")#candidate|4697|(11, 11, 5)|const|int32
bop_4698 = relay.right_shift(const_4696.astype('int32'), const_4697.astype('int32')) # shape=(11, 11, 5)
func_3863_call = mod.get_global_var('func_3863')
func_3865_call = mutated_mod.get_global_var('func_3865')
var_4705 = relay.var("var_4705", dtype = "int8", shape = (352,))#candidate|4705|(352,)|var|int8
call_4704 = relay.TupleGetItem(func_3863_call(relay.reshape(var_4705.astype('int8'), [352,])), 1)
call_4706 = relay.TupleGetItem(func_3865_call(relay.reshape(var_4705.astype('int8'), [352,])), 1)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_4709 = relay.TupleGetItem(func_393_call(), 0)
call_4710 = relay.TupleGetItem(func_395_call(), 0)
func_901_call = mod.get_global_var('func_901')
func_904_call = mutated_mod.get_global_var('func_904')
const_4718 = relay.const([10,7,-2,7,-7,1,6,8,5,2,8,-3,-2,-6,-9,-6,-7,-2,6,-4,-2,2,-3,2,8,7,3,-2,3,3,10,-10,4,7,-3,-5,-8,-3,-9,-8,-10,-2,4,-8,-3,8,4,-2,10,-2,-2,8,-6,-8,7,-2,10,-1,-10,-1,2,8,-7,-8,-10,10,7,-10,8,-8,6,3,3,-2,3,-8,5,2,-4,9,-1,6,6,3,-5,-10,-10,-9,-4,-8,6,-1,1,5,6,-1,-4,4,-2,5,-7,-10,-7,-2,2,8,-5,1,4,1,-1,-6,-9,4,-7,-1,-3,1,-2,2,2,-1,1,-5,1,5,-8,8,1,-1,2,-5,4,6,-1,-9,-8,-10,-6,4,-10,-9,1,-8,-1,3,4,8,-5,4,-3,-9,-5,2,5,-9,6,-5,-9,-1,5,-4,3,-7,-8,-6,-5,-4,7,2,-3,-9,2,7,-1,10,2,3,7,6,10,-8,9,5,-9,8,-1,10,2,-5,-6,7,10,-5,-1,-2,-3,5,-2,9,-1,-3,5,8,-3,-10,-7,-8,8,-3,4,-9,-4,10,9,7,-8,4,6,-1,-2,-7,-8,7,-8,-5,4,9,10,-5,-1,-1,-5,-2,-7,-9,2,10,-2,-5,5,-3,6,10,1,7,2,-1,-2,-7,6,8,5,-9,4,7,6,10,-4,-7,8,9,3,6,-2,4,10,-7,9,1,-10,3,-2,7,5,-1,10,-4,1,-8,-4,3,6,10,4,9,4,9,6,10,-1,-6,-2,-4,4,-5,8,-4,-8,10,-8,7,10,5,-3,7,7,-5,-8,9,-4,-8,-2,7,-9,-1,5,-6,-5,10,8,-2,-3,-4,-7,-10,-9,3,3,1,-4,-6,2,3,4,7,-1,7,-5,2,5,-5,10,-6,-8,4,9,3,3,1,9,9,7,1,-6,6,-5,-6,10,10,8,10,-4,-1,10,2,9,9,-7,8,5,5,-6,7,-2,4,8,7,8,7,-9,-7,-10,4,7,1,5,-2,-10,9,-5,-1,-6,5,6,3,-2,-4,5,10,-10,-5,-10,8,-7,1,9,-5,8,-10,-1,-10,3,5,-1,-1,-9,-8,5,-8,-2,-4,-1,-7,-8,-5,-1,-2,-10,4,6,-4,2,-4,5,-7,1,1,10,-2,6,7,-2,-4,10,4,1,-8,8,-10,-6,-4,-8,-10,3,-7,7,8,5,-10,10,-8,1,-4,10,4,10,-2,10,-7,3,-2,7,8,2,6,3,2,10,3,-1,5,-4,2,-10,-7,-4,-3,-10,5,-10,-3,5,-7,3,-6,-6,8,1,-3,10,3,-2,-6,-7,4,4,-2,-7,5,-8,6,3,5,-5,-4,-2,-10,-1,-7,-9,-8,10,-1,7,-9,-6,-3,9,2,8,-9,-1,5,7,-2,2,-9,-10,-9,6,-5,3,1,6,7,9,6,-7,4,4,-10,8,9,4,4,-8,-2,7,-4,-7,8,-7,6,9,7,7,-8,-1,-10,6,2,-3,6,10,-4,9,4,8,9,1,-1,-3,3,7,-6,-7,9,-7,-1,-3,5,-7,-7,1,4,-1,-2,3,10,-7,5,7,8,-8,-10,-6,-2,-3,9,4,8,10,2,3,5,8,-8,3,8,4,2,-2,4,5,9,-7,-7,-7,2,10,-10,7,-5,3,-2,3,9,-8,3,6,-5,1,2,10,7,-9,-10,6,-7,-9,8,-2,-9,1,6,-6,-2,2,2,-8,-3,6,5,9,3,-2,-1,-9,7,-2,9,3,-4,7,-8,-5,-4,-2,-4,-5,-8,9,1,2,8,-10,-2,8,9,-4,-2,8,3,-7,1,-6,-8,10,1,-5,6,7,2,5,-1,-10,7,1,8,-9,-9,-9,7,4,1,-8,9,-6,1,2,-10,6,-10,9,4,-8,10,10,7,5,7,3,-9,7,-10,-3,-1,10,-6,1,5,-3,-5,4,8,9,3,9,1,-1,5,1,-2,9,-10,-8,-10,-1,3,-8,-5,6,9,9,1,10,5,-4,-4,7,-5,-10,3,1,-7,8,-6,-9,8,-4,1,7,-9,4,-7,-9,3,9,-9,5,1,-7,6,1,-5,4,-3,1,-5,-5,-6,-5,4,-9,6,10,-5,-6,4,-4,-4,-4,-3,-9,1,-9,8,8,-7,4,8,1,-10,6,-4,-2,1,5,2,10,-8,10,2,8,4,-3,6,8,10,-10,4,-5,8,9,-4,3,8,7,-1,1,7,-8,1,8,1,8,-2,10,-10,1,-8,5,-6,-9,-7,2,6,6,-7,-9,-6,4,7,-9,-3,-5,3,-10,-2,7,9,3,9,-5,6,5,-2,-10,-2,-7,9,7,-2,2,6,-5,-9,2,-10,6,-10,9,-9,10,10,-8,1,-3,-2,9,6,-1,-2,7,-10,9,-4,-4,9,-6,-5,-10,-8,9,7,8,-2,10,-3,-8,-10,5,-7,-8,-4,5,-9,-6,-7,-6,5,-10,4,4,9,-10,-9,4,3,2,8,-7,-2,3,9,4,5,4,-5,5,-10,-2,10,-7,-10,10,-6,-3,1,-10,5,-6,-7,10,-9,-6,9,-10,-4,2,5,1,1,2,2,-2,-7,9,-1,5,-5,-8,9,-5,-4,10,-1,3,-7,-1,8,-9,-2,-8,-9,-2,6], dtype = "uint8")#candidate|4718|(1008,)|const|uint8
call_4717 = relay.TupleGetItem(func_901_call(relay.reshape(const_4718.astype('uint8'), [1008,])), 2)
call_4719 = relay.TupleGetItem(func_904_call(relay.reshape(const_4718.astype('uint8'), [1008,])), 2)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_4724 = func_3961_call()
call_4725 = func_3961_call()
bop_4739 = relay.logical_xor(const_4696.astype('uint8'), bop_4698.astype('uint8')) # shape=(11, 11, 5)
output = relay.Tuple([call_4704,var_4705,call_4709,call_4717,const_4718,call_4724,bop_4739,])
output2 = relay.Tuple([call_4706,var_4705,call_4710,call_4719,const_4718,call_4725,bop_4739,])
func_4750 = relay.Function([var_4705,], output)
mod['func_4750'] = func_4750
mod = relay.transform.InferType()(mod)
mutated_mod['func_4750'] = func_4750
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4751 = relay.var("var_4751", dtype = "int8", shape = (352,))#candidate|4751|(352,)|var|int8
func_4750_call = mutated_mod.get_global_var('func_4750')
call_4752 = func_4750_call(var_4751)
output = call_4752
func_4753 = relay.Function([var_4751], output)
mutated_mod['func_4753'] = func_4753
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4760 = relay.var("var_4760", dtype = "float32", shape = (7, 8, 3))#candidate|4760|(7, 8, 3)|var|float32
uop_4761 = relay.log(var_4760.astype('float32')) # shape=(7, 8, 3)
output = uop_4761
output2 = uop_4761
func_4767 = relay.Function([var_4760,], output)
mod['func_4767'] = func_4767
mod = relay.transform.InferType()(mod)
var_4768 = relay.var("var_4768", dtype = "float32", shape = (7, 8, 3))#candidate|4768|(7, 8, 3)|var|float32
output = func_4767(var_4768)
func_4769 = relay.Function([var_4768], output)
mutated_mod['func_4769'] = func_4769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4448_call = mod.get_global_var('func_4448')
func_4449_call = mutated_mod.get_global_var('func_4449')
call_4774 = relay.TupleGetItem(func_4448_call(), 2)
call_4775 = relay.TupleGetItem(func_4449_call(), 2)
output = call_4774
output2 = call_4775
func_4788 = relay.Function([], output)
mod['func_4788'] = func_4788
mod = relay.transform.InferType()(mod)
output = func_4788()
func_4789 = relay.Function([], output)
mutated_mod['func_4789'] = func_4789
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4808 = relay.var("var_4808", dtype = "float64", shape = (7, 13, 6))#candidate|4808|(7, 13, 6)|var|float64
var_4809 = relay.var("var_4809", dtype = "float64", shape = (7, 13, 6))#candidate|4809|(7, 13, 6)|var|float64
bop_4810 = relay.power(var_4808.astype('float64'), relay.reshape(var_4809.astype('float64'), relay.shape_of(var_4808))) # shape=(7, 13, 6)
func_4307_call = mod.get_global_var('func_4307')
func_4309_call = mutated_mod.get_global_var('func_4309')
call_4813 = func_4307_call()
call_4814 = func_4307_call()
output = relay.Tuple([bop_4810,call_4813,])
output2 = relay.Tuple([bop_4810,call_4814,])
func_4815 = relay.Function([var_4808,var_4809,], output)
mod['func_4815'] = func_4815
mod = relay.transform.InferType()(mod)
mutated_mod['func_4815'] = func_4815
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4815_call = mutated_mod.get_global_var('func_4815')
var_4817 = relay.var("var_4817", dtype = "float64", shape = (7, 13, 6))#candidate|4817|(7, 13, 6)|var|float64
var_4818 = relay.var("var_4818", dtype = "float64", shape = (7, 13, 6))#candidate|4818|(7, 13, 6)|var|float64
call_4816 = func_4815_call(var_4817,var_4818,)
output = call_4816
func_4819 = relay.Function([var_4817,var_4818,], output)
mutated_mod['func_4819'] = func_4819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1374_call = mod.get_global_var('func_1374')
func_1375_call = mutated_mod.get_global_var('func_1375')
call_4823 = func_1374_call()
call_4824 = func_1374_call()
output = call_4823
output2 = call_4824
func_4825 = relay.Function([], output)
mod['func_4825'] = func_4825
mod = relay.transform.InferType()(mod)
mutated_mod['func_4825'] = func_4825
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4825_call = mutated_mod.get_global_var('func_4825')
call_4826 = func_4825_call()
output = call_4826
func_4827 = relay.Function([], output)
mutated_mod['func_4827'] = func_4827
mutated_mod = relay.transform.InferType()(mutated_mod)
func_365_call = mod.get_global_var('func_365')
func_366_call = mutated_mod.get_global_var('func_366')
call_4862 = relay.TupleGetItem(func_365_call(), 0)
call_4863 = relay.TupleGetItem(func_366_call(), 0)
func_3953_call = mod.get_global_var('func_3953')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_4878 = relay.TupleGetItem(func_3953_call(), 1)
call_4879 = relay.TupleGetItem(func_3954_call(), 1)
func_4767_call = mod.get_global_var('func_4767')
func_4769_call = mutated_mod.get_global_var('func_4769')
var_4898 = relay.var("var_4898", dtype = "float32", shape = (84, 2))#candidate|4898|(84, 2)|var|float32
call_4897 = func_4767_call(relay.reshape(var_4898.astype('float32'), [7, 8, 3]))
call_4899 = func_4767_call(relay.reshape(var_4898.astype('float32'), [7, 8, 3]))
bop_4906 = relay.right_shift(call_4897.astype('uint64'), relay.reshape(var_4898.astype('uint64'), relay.shape_of(call_4897))) # shape=(7, 8, 3)
bop_4909 = relay.right_shift(call_4899.astype('uint64'), relay.reshape(var_4898.astype('uint64'), relay.shape_of(call_4899))) # shape=(7, 8, 3)
output = relay.Tuple([call_4862,call_4878,bop_4906,])
output2 = relay.Tuple([call_4863,call_4879,bop_4909,])
func_4958 = relay.Function([var_4898,], output)
mod['func_4958'] = func_4958
mod = relay.transform.InferType()(mod)
var_4959 = relay.var("var_4959", dtype = "float32", shape = (84, 2))#candidate|4959|(84, 2)|var|float32
output = func_4958(var_4959)
func_4960 = relay.Function([var_4959], output)
mutated_mod['func_4960'] = func_4960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1015_call = mod.get_global_var('func_1015')
func_1016_call = mutated_mod.get_global_var('func_1016')
call_4972 = relay.TupleGetItem(func_1015_call(), 0)
call_4973 = relay.TupleGetItem(func_1016_call(), 0)
output = call_4972
output2 = call_4973
func_4985 = relay.Function([], output)
mod['func_4985'] = func_4985
mod = relay.transform.InferType()(mod)
mutated_mod['func_4985'] = func_4985
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4985_call = mutated_mod.get_global_var('func_4985')
call_4986 = func_4985_call()
output = call_4986
func_4987 = relay.Function([], output)
mutated_mod['func_4987'] = func_4987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3953_call = mod.get_global_var('func_3953')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_4991 = relay.TupleGetItem(func_3953_call(), 0)
call_4992 = relay.TupleGetItem(func_3954_call(), 0)
func_179_call = mod.get_global_var('func_179')
func_182_call = mutated_mod.get_global_var('func_182')
call_5028 = relay.TupleGetItem(func_179_call(relay.reshape(call_4991.astype('float32'), [2, 12, 9]), relay.reshape(call_4991.astype('float32'), [2, 12, 9]), ), 0)
call_5029 = relay.TupleGetItem(func_182_call(relay.reshape(call_4991.astype('float32'), [2, 12, 9]), relay.reshape(call_4991.astype('float32'), [2, 12, 9]), ), 0)
func_4263_call = mod.get_global_var('func_4263')
func_4266_call = mutated_mod.get_global_var('func_4266')
const_5041 = relay.const([-7,9,7,-1,-2,-1,1,6,4,-2,4,-8,4,6,-9,3,6,-1,9,-9,10,-10,3,-10,3,-4,9,-7,-6,-4,6,2,-1,-2,-2,-1,-2,-5,1,4,7,-3,9,-1,5,-9,-3,10,1,4,6,10,-10,-2,2,5,5,-6,-5,1], dtype = "uint64")#candidate|5041|(60,)|const|uint64
var_5042 = relay.var("var_5042", dtype = "uint64", shape = (120,))#candidate|5042|(120,)|var|uint64
call_5040 = relay.TupleGetItem(func_4263_call(relay.reshape(const_5041.astype('uint64'), [6, 1, 10]), relay.reshape(var_5042.astype('uint64'), [6, 2, 10]), ), 0)
call_5043 = relay.TupleGetItem(func_4266_call(relay.reshape(const_5041.astype('uint64'), [6, 1, 10]), relay.reshape(var_5042.astype('uint64'), [6, 2, 10]), ), 0)
func_3863_call = mod.get_global_var('func_3863')
func_3865_call = mutated_mod.get_global_var('func_3865')
var_5052 = relay.var("var_5052", dtype = "int8", shape = (352,))#candidate|5052|(352,)|var|int8
call_5051 = relay.TupleGetItem(func_3863_call(relay.reshape(var_5052.astype('int8'), [352,])), 0)
call_5053 = relay.TupleGetItem(func_3865_call(relay.reshape(var_5052.astype('int8'), [352,])), 0)
func_1118_call = mod.get_global_var('func_1118')
func_1122_call = mutated_mod.get_global_var('func_1122')
var_5064 = relay.var("var_5064", dtype = "float32", shape = (448, 1))#candidate|5064|(448, 1)|var|float32
call_5063 = relay.TupleGetItem(func_1118_call(relay.reshape(var_5064.astype('float32'), [8, 14, 4]), relay.reshape(var_5064.astype('float32'), [8, 14, 4]), relay.reshape(var_5052.astype('int8'), [352,]), ), 1)
call_5065 = relay.TupleGetItem(func_1122_call(relay.reshape(var_5064.astype('float32'), [8, 14, 4]), relay.reshape(var_5064.astype('float32'), [8, 14, 4]), relay.reshape(var_5052.astype('int8'), [352,]), ), 1)
func_710_call = mod.get_global_var('func_710')
func_715_call = mutated_mod.get_global_var('func_715')
call_5066 = relay.TupleGetItem(func_710_call(relay.reshape(call_5063.astype('int8'), [11, 2, 16]), relay.reshape(var_5052.astype('int8'), [11, 2, 16]), relay.reshape(var_5052.astype('int8'), [11, 2, 16]), ), 1)
call_5067 = relay.TupleGetItem(func_715_call(relay.reshape(call_5063.astype('int8'), [11, 2, 16]), relay.reshape(var_5052.astype('int8'), [11, 2, 16]), relay.reshape(var_5052.astype('int8'), [11, 2, 16]), ), 1)
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_5068 = func_3322_call()
call_5069 = func_3322_call()
output = relay.Tuple([call_4991,call_5028,call_5040,const_5041,var_5042,call_5051,var_5052,call_5063,var_5064,call_5066,call_5068,])
output2 = relay.Tuple([call_4992,call_5029,call_5043,const_5041,var_5042,call_5053,var_5052,call_5065,var_5064,call_5067,call_5069,])
func_5073 = relay.Function([var_5042,var_5052,var_5064,], output)
mod['func_5073'] = func_5073
mod = relay.transform.InferType()(mod)
var_5074 = relay.var("var_5074", dtype = "uint64", shape = (120,))#candidate|5074|(120,)|var|uint64
var_5075 = relay.var("var_5075", dtype = "int8", shape = (352,))#candidate|5075|(352,)|var|int8
var_5076 = relay.var("var_5076", dtype = "float32", shape = (448, 1))#candidate|5076|(448, 1)|var|float32
output = func_5073(var_5074,var_5075,var_5076,)
func_5077 = relay.Function([var_5074,var_5075,var_5076,], output)
mutated_mod['func_5077'] = func_5077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_5097 = relay.TupleGetItem(func_1454_call(), 0)
call_5098 = relay.TupleGetItem(func_1456_call(), 0)
func_1581_call = mod.get_global_var('func_1581')
func_1583_call = mutated_mod.get_global_var('func_1583')
call_5120 = func_1581_call()
call_5121 = func_1581_call()
func_4825_call = mod.get_global_var('func_4825')
func_4827_call = mutated_mod.get_global_var('func_4827')
call_5136 = func_4825_call()
call_5137 = func_4825_call()
func_901_call = mod.get_global_var('func_901')
func_904_call = mutated_mod.get_global_var('func_904')
const_5147 = relay.const([[8,7,-3,8,9,10,-10,8,-2,6,-2,-8,2,-9,-3,-6,-6,-6,7,8,-1,5,-5,-5,2,7,-2,2,-8,-5,-8,3,-3,3,-5,8,-3,-7,-8,5,4,3,-8,7,4,6,-2,-7,8,-7,-3,8,9,-4,8,6,-3,5,4,5,6,1,2,5,8,-2,-6,-8,-6,2,4,-5,1,-8,3,-4,-7,-7,4,9,-3,-6,-1,-5],[-7,-2,-9,7,6,4,9,6,-6,4,-4,-4,4,-9,-4,-4,5,3,-1,-3,-8,-4,-8,2,5,4,9,-10,7,9,-6,-4,7,7,8,6,-9,-2,3,1,-1,9,2,-4,1,-2,-4,-7,2,2,-6,-7,-9,3,4,-1,-8,7,-2,-1,-4,-1,7,-1,2,2,-10,-2,-7,-2,-9,-8,-5,-7,5,1,10,8,-10,8,-2,1,-1,-2],[9,1,-7,5,3,-1,1,-8,6,8,-4,-1,9,8,-8,-10,4,-5,10,7,5,4,1,-6,-5,-6,-3,5,10,3,6,3,5,-5,1,8,9,1,-3,1,-1,9,4,5,-9,-10,-10,-5,4,-9,1,2,-1,-1,1,-2,-7,-4,5,6,8,9,2,2,-5,2,10,5,8,8,8,-10,3,7,-5,-3,1,-10,7,9,-5,-9,5,-8],[4,10,8,-8,-6,-10,-9,4,7,1,6,-10,-8,-7,7,-6,5,-10,6,5,-2,-2,10,-1,10,2,1,-8,-3,2,4,10,5,-2,7,-2,-2,1,10,10,-1,7,-6,-1,-2,10,2,-3,7,8,3,-4,6,-7,-7,-8,9,10,-2,6,-5,-10,-4,6,10,-9,3,6,-9,8,9,-4,-5,4,7,-1,-6,-1,-6,6,-8,9,-8,-3],[-7,5,-10,6,3,-3,2,3,7,-10,1,-10,-1,-2,-3,6,-7,8,9,-3,6,5,1,7,3,10,-5,3,-9,-5,-2,-2,1,8,-6,4,-8,9,8,5,3,-5,8,-2,-3,-9,7,3,3,-10,4,-2,-3,-2,-5,2,4,6,-7,9,7,-6,1,-4,3,-5,8,-1,-8,-3,10,3,-5,6,-1,-4,4,5,-1,2,-5,-5,6,-3],[7,-7,3,2,1,2,4,-10,-7,-4,4,-4,-4,-1,5,3,1,-10,2,-2,2,2,-9,-4,7,-7,-3,1,2,-8,-7,-10,10,3,-5,-4,-9,1,-1,6,-5,1,6,7,-4,-6,3,7,9,5,5,9,6,-3,6,-6,-4,9,7,-9,-1,9,-2,-7,-8,-5,4,8,5,-8,1,-2,-9,5,8,-8,-9,-3,5,2,-4,6,-10,-9],[-8,-5,-1,3,1,7,-4,-8,-1,-3,-3,-10,1,-5,2,5,-3,8,9,-5,1,-10,6,-7,-9,5,-5,-8,-3,-9,-9,7,-5,7,10,6,3,-8,4,-7,-6,-4,7,9,-7,7,3,9,2,-5,7,4,7,-8,-9,-3,-5,-8,-3,4,-7,7,6,-1,-3,1,-10,-7,-8,8,-9,-2,2,-9,-9,4,-6,10,-8,-10,-9,-8,-7,6],[3,1,-6,8,-5,10,2,3,-4,9,6,-2,10,6,8,-3,5,-3,-8,-7,-10,8,3,-9,4,1,-5,7,-7,-5,4,-6,-1,-9,1,-2,5,2,-1,8,-7,7,4,-9,4,3,-9,6,9,-9,-1,1,2,7,2,-3,4,3,4,6,6,-6,10,7,9,-10,-10,10,4,-7,1,-7,10,3,-2,9,-10,-6,-1,2,10,10,-2,-2],[-8,-3,9,-3,10,10,-5,-1,-8,-7,-10,8,-2,-10,1,-9,10,-7,1,-7,-8,-2,-6,9,-2,2,7,3,-10,-2,-4,-7,4,-5,-6,8,7,-6,-5,-8,1,-10,-10,6,6,1,2,6,4,2,4,-5,-2,-8,5,-3,-6,7,-5,-7,4,3,-6,9,-2,1,3,-9,-8,-1,2,1,8,-5,-4,4,-10,1,5,9,3,5,7,-10],[-10,-8,-4,2,1,-4,10,1,4,10,-4,-1,9,4,10,3,-4,2,-1,1,-2,7,5,-5,-1,-10,-2,-3,-7,-10,-10,6,-3,-5,5,-6,-3,10,-10,6,-10,8,9,6,8,-10,-7,6,7,4,-7,10,5,5,4,9,-10,-7,-6,-3,-7,5,-1,5,2,1,-10,-7,-2,-10,-6,2,6,2,-2,-8,-10,-4,4,3,9,-5,-7,-5],[5,-7,6,6,9,-6,3,-2,7,-7,5,8,6,-6,6,-1,-7,-3,-8,-7,-6,-7,-6,-3,-7,5,2,8,7,-2,5,3,2,9,4,6,-8,9,6,-9,4,-4,9,6,-8,-8,-2,7,8,5,-1,-10,-7,-4,-2,-5,1,5,-3,-10,1,-6,-1,-8,-10,-9,-3,-1,-9,-3,-10,-7,8,-4,5,4,2,-9,-6,9,10,-4,-10,-3],[-1,-10,-5,-3,1,3,-9,-3,10,3,-9,-9,-4,-1,-9,-1,-1,1,-8,-8,-2,-4,-2,4,-9,6,-1,6,-10,-8,-3,9,-10,1,-5,-8,4,9,-8,-7,-10,-6,10,4,1,8,3,-2,-10,-2,4,3,1,-3,5,-6,3,-5,6,-2,3,2,1,-8,7,-5,9,10,-8,-1,-2,-7,10,9,-1,-4,-5,10,-10,-5,10,9,-8,1]], dtype = "uint8")#candidate|5147|(12, 84)|const|uint8
call_5146 = relay.TupleGetItem(func_901_call(relay.reshape(const_5147.astype('uint8'), [1008,])), 4)
call_5148 = relay.TupleGetItem(func_904_call(relay.reshape(const_5147.astype('uint8'), [1008,])), 4)
output = relay.Tuple([call_5097,call_5120,call_5136,call_5146,const_5147,])
output2 = relay.Tuple([call_5098,call_5121,call_5137,call_5148,const_5147,])
func_5165 = relay.Function([], output)
mod['func_5165'] = func_5165
mod = relay.transform.InferType()(mod)
output = func_5165()
func_5166 = relay.Function([], output)
mutated_mod['func_5166'] = func_5166
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2455_call = mod.get_global_var('func_2455')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_5177 = relay.TupleGetItem(func_2455_call(), 0)
call_5178 = relay.TupleGetItem(func_2456_call(), 0)
output = call_5177
output2 = call_5178
func_5196 = relay.Function([], output)
mod['func_5196'] = func_5196
mod = relay.transform.InferType()(mod)
output = func_5196()
func_5197 = relay.Function([], output)
mutated_mod['func_5197'] = func_5197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4638_call = mod.get_global_var('func_4638')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_5254 = relay.TupleGetItem(func_4638_call(), 1)
call_5255 = relay.TupleGetItem(func_4640_call(), 1)
func_4638_call = mod.get_global_var('func_4638')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_5258 = relay.TupleGetItem(func_4638_call(), 2)
call_5259 = relay.TupleGetItem(func_4640_call(), 2)
func_2532_call = mod.get_global_var('func_2532')
func_2534_call = mutated_mod.get_global_var('func_2534')
var_5268 = relay.var("var_5268", dtype = "uint32", shape = (312,))#candidate|5268|(312,)|var|uint32
call_5267 = func_2532_call(relay.reshape(var_5268.astype('uint32'), [6, 4, 13]))
call_5269 = func_2532_call(relay.reshape(var_5268.astype('uint32'), [6, 4, 13]))
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_5278 = relay.TupleGetItem(func_2776_call(), 0)
call_5279 = relay.TupleGetItem(func_2778_call(), 0)
output = relay.Tuple([call_5254,call_5258,call_5267,var_5268,call_5278,])
output2 = relay.Tuple([call_5255,call_5259,call_5269,var_5268,call_5279,])
func_5280 = relay.Function([var_5268,], output)
mod['func_5280'] = func_5280
mod = relay.transform.InferType()(mod)
mutated_mod['func_5280'] = func_5280
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5281 = relay.var("var_5281", dtype = "uint32", shape = (312,))#candidate|5281|(312,)|var|uint32
func_5280_call = mutated_mod.get_global_var('func_5280')
call_5282 = func_5280_call(var_5281)
output = call_5282
func_5283 = relay.Function([var_5281], output)
mutated_mod['func_5283'] = func_5283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_5288 = relay.TupleGetItem(func_1502_call(), 2)
call_5289 = relay.TupleGetItem(func_1503_call(), 2)
output = call_5288
output2 = call_5289
func_5292 = relay.Function([], output)
mod['func_5292'] = func_5292
mod = relay.transform.InferType()(mod)
output = func_5292()
func_5293 = relay.Function([], output)
mutated_mod['func_5293'] = func_5293
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5349 = relay.var("var_5349", dtype = "float32", shape = (14, 3, 2))#candidate|5349|(14, 3, 2)|var|float32
uop_5350 = relay.erf(var_5349.astype('float32')) # shape=(14, 3, 2)
func_2219_call = mod.get_global_var('func_2219')
func_2221_call = mutated_mod.get_global_var('func_2221')
call_5365 = func_2219_call()
call_5366 = func_2219_call()
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_5375 = relay.TupleGetItem(func_3252_call(), 0)
call_5376 = relay.TupleGetItem(func_3254_call(), 0)
output = relay.Tuple([uop_5350,call_5365,call_5375,])
output2 = relay.Tuple([uop_5350,call_5366,call_5376,])
func_5377 = relay.Function([var_5349,], output)
mod['func_5377'] = func_5377
mod = relay.transform.InferType()(mod)
var_5378 = relay.var("var_5378", dtype = "float32", shape = (14, 3, 2))#candidate|5378|(14, 3, 2)|var|float32
output = func_5377(var_5378)
func_5379 = relay.Function([var_5378], output)
mutated_mod['func_5379'] = func_5379
mutated_mod = relay.transform.InferType()(mutated_mod)
func_623_call = mod.get_global_var('func_623')
func_625_call = mutated_mod.get_global_var('func_625')
call_5396 = func_623_call()
call_5397 = func_623_call()
func_4132_call = mod.get_global_var('func_4132')
func_4134_call = mutated_mod.get_global_var('func_4134')
var_5420 = relay.var("var_5420", dtype = "float64", shape = (104, 8))#candidate|5420|(104, 8)|var|float64
call_5419 = relay.TupleGetItem(func_4132_call(relay.reshape(var_5420.astype('float64'), [416, 2])), 1)
call_5421 = relay.TupleGetItem(func_4134_call(relay.reshape(var_5420.astype('float64'), [416, 2])), 1)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_5438 = relay.TupleGetItem(func_2925_call(), 0)
call_5439 = relay.TupleGetItem(func_2927_call(), 0)
output = relay.Tuple([call_5396,call_5419,var_5420,call_5438,])
output2 = relay.Tuple([call_5397,call_5421,var_5420,call_5439,])
func_5442 = relay.Function([var_5420,], output)
mod['func_5442'] = func_5442
mod = relay.transform.InferType()(mod)
var_5443 = relay.var("var_5443", dtype = "float64", shape = (104, 8))#candidate|5443|(104, 8)|var|float64
output = func_5442(var_5443)
func_5444 = relay.Function([var_5443], output)
mutated_mod['func_5444'] = func_5444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1374_call = mod.get_global_var('func_1374')
func_1375_call = mutated_mod.get_global_var('func_1375')
call_5481 = func_1374_call()
call_5482 = func_1374_call()
output = call_5481
output2 = call_5482
func_5488 = relay.Function([], output)
mod['func_5488'] = func_5488
mod = relay.transform.InferType()(mod)
mutated_mod['func_5488'] = func_5488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5488_call = mutated_mod.get_global_var('func_5488')
call_5489 = func_5488_call()
output = call_5489
func_5490 = relay.Function([], output)
mutated_mod['func_5490'] = func_5490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_5493 = relay.TupleGetItem(func_1454_call(), 0)
call_5494 = relay.TupleGetItem(func_1456_call(), 0)
output = relay.Tuple([call_5493,])
output2 = relay.Tuple([call_5494,])
func_5499 = relay.Function([], output)
mod['func_5499'] = func_5499
mod = relay.transform.InferType()(mod)
output = func_5499()
func_5500 = relay.Function([], output)
mutated_mod['func_5500'] = func_5500
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mod.get_global_var('func_1322')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_5511 = relay.TupleGetItem(func_1322_call(), 0)
call_5512 = relay.TupleGetItem(func_1323_call(), 0)
output = relay.Tuple([call_5511,])
output2 = relay.Tuple([call_5512,])
func_5516 = relay.Function([], output)
mod['func_5516'] = func_5516
mod = relay.transform.InferType()(mod)
output = func_5516()
func_5517 = relay.Function([], output)
mutated_mod['func_5517'] = func_5517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_5633 = relay.TupleGetItem(func_2863_call(), 2)
call_5634 = relay.TupleGetItem(func_2865_call(), 2)
output = call_5633
output2 = call_5634
func_5638 = relay.Function([], output)
mod['func_5638'] = func_5638
mod = relay.transform.InferType()(mod)
mutated_mod['func_5638'] = func_5638
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5638_call = mutated_mod.get_global_var('func_5638')
call_5639 = func_5638_call()
output = call_5639
func_5640 = relay.Function([], output)
mutated_mod['func_5640'] = func_5640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_5659 = func_1064_call()
call_5660 = func_1064_call()
output = relay.Tuple([call_5659,])
output2 = relay.Tuple([call_5660,])
func_5691 = relay.Function([], output)
mod['func_5691'] = func_5691
mod = relay.transform.InferType()(mod)
mutated_mod['func_5691'] = func_5691
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5691_call = mutated_mod.get_global_var('func_5691')
call_5692 = func_5691_call()
output = call_5692
func_5693 = relay.Function([], output)
mutated_mod['func_5693'] = func_5693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_623_call = mod.get_global_var('func_623')
func_625_call = mutated_mod.get_global_var('func_625')
call_5704 = func_623_call()
call_5705 = func_623_call()
output = relay.Tuple([call_5704,])
output2 = relay.Tuple([call_5705,])
func_5714 = relay.Function([], output)
mod['func_5714'] = func_5714
mod = relay.transform.InferType()(mod)
output = func_5714()
func_5715 = relay.Function([], output)
mutated_mod['func_5715'] = func_5715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4222_call = mod.get_global_var('func_4222')
func_4223_call = mutated_mod.get_global_var('func_4223')
call_5725 = relay.TupleGetItem(func_4222_call(), 0)
call_5726 = relay.TupleGetItem(func_4223_call(), 0)
var_5740 = relay.var("var_5740", dtype = "float64", shape = (2, 12, 9))#candidate|5740|(2, 12, 9)|var|float64
bop_5741 = relay.greater_equal(call_5725.astype('bool'), relay.reshape(var_5740.astype('bool'), relay.shape_of(call_5725))) # shape=(2, 12, 9)
bop_5744 = relay.greater_equal(call_5726.astype('bool'), relay.reshape(var_5740.astype('bool'), relay.shape_of(call_5726))) # shape=(2, 12, 9)
output = relay.Tuple([bop_5741,])
output2 = relay.Tuple([bop_5744,])
func_5747 = relay.Function([var_5740,], output)
mod['func_5747'] = func_5747
mod = relay.transform.InferType()(mod)
mutated_mod['func_5747'] = func_5747
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5748 = relay.var("var_5748", dtype = "float64", shape = (2, 12, 9))#candidate|5748|(2, 12, 9)|var|float64
func_5747_call = mutated_mod.get_global_var('func_5747')
call_5749 = func_5747_call(var_5748)
output = call_5749
func_5750 = relay.Function([var_5748], output)
mutated_mod['func_5750'] = func_5750
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5815 = relay.const([[[-1,5,7,3,4,8,2,-2,-5,8,-6,1],[8,-8,8,-3,10,-10,-8,4,6,-3,-1,-9],[7,-2,-10,5,-10,2,-7,-8,3,-2,1,-4],[-10,-7,-1,-9,-4,1,5,-3,-9,4,10,-2],[10,-7,-4,7,-7,6,1,-6,8,10,-5,8],[-7,-1,4,1,9,-4,8,-8,-8,-3,-10,3]],[[-8,9,5,7,-2,1,2,-2,10,6,9,-3],[8,3,6,-4,-8,-8,-2,9,1,-2,1,-4],[1,-1,5,7,-1,-1,-8,-1,-8,1,2,-8],[9,-8,5,3,3,6,7,3,-4,5,7,-8],[5,-9,-1,-1,-6,-1,2,-6,-6,-5,6,1],[10,1,1,4,-9,4,7,-10,-6,-3,3,-3]],[[10,3,4,5,1,-1,5,10,-6,6,2,8],[7,6,9,-10,-5,-6,-9,3,6,2,-9,7],[-7,-1,-9,6,-8,-5,-2,-7,-9,8,-5,8],[4,5,2,-9,5,9,8,-9,10,5,-10,-10],[5,-7,-8,-2,-4,-6,-8,-7,-4,8,-4,8],[2,7,-6,-1,7,-1,-10,9,-1,2,9,-2]],[[-6,5,-7,5,4,1,10,-1,9,-4,-7,5],[-6,-7,4,10,-10,-3,5,6,1,1,9,-10],[4,-9,5,-10,9,-9,-7,-7,1,-3,8,-8],[-7,2,-1,-6,6,-7,-7,5,-4,-3,3,-9],[-9,-3,-2,-8,9,8,-6,-6,-8,-5,-2,5],[7,9,7,4,-10,3,-5,-4,-4,-6,-5,-3]],[[3,-1,2,-1,3,9,-9,4,-8,-3,1,-9],[10,-5,6,-1,8,6,-8,-9,10,-1,-8,8],[5,1,1,-10,7,-7,3,-4,9,-3,10,10],[-1,-8,-9,7,10,-9,-9,-3,6,9,-5,2],[-6,3,-10,-7,5,2,-4,9,8,-6,-8,-3],[-8,-4,7,8,-5,-1,-5,6,4,5,6,3]],[[-3,10,7,-6,8,-7,-9,2,6,-7,-2,1],[10,5,10,-1,-4,-6,6,5,3,-3,-6,6],[-8,3,7,-7,1,-4,-9,-6,8,5,6,-2],[-1,3,9,1,2,7,-1,-8,-6,3,-1,-8],[3,-5,-3,-9,-1,6,-4,7,-3,7,9,-6],[10,-10,-2,-10,-2,-5,-3,9,-9,-3,-2,-10]],[[5,10,-3,-8,-8,5,-5,-5,3,1,-6,-9],[-7,-9,5,7,5,1,-6,4,-7,5,6,-10],[2,5,4,-5,10,-2,-1,4,-6,5,-6,-7],[-8,5,-2,2,-6,4,-5,-9,-10,10,9,7],[-9,-9,-1,-7,9,-2,-5,-7,-3,9,9,-5],[-2,-10,8,-8,10,-3,-6,-8,10,-7,6,8]],[[-4,-1,8,2,10,-10,-9,-7,-8,10,9,-6],[-9,6,7,-9,10,4,4,7,-7,-2,5,-5],[-8,-4,4,7,-5,1,6,2,7,-5,3,-7],[-9,7,8,7,-9,-4,3,6,-6,-9,-6,2],[9,6,-9,4,-2,4,-5,8,3,6,-3,3],[3,4,5,5,-3,-9,6,2,4,-9,-6,2]],[[-7,5,-5,3,-2,-7,3,4,5,-8,-5,-8],[-6,-8,2,-10,-10,-2,3,1,2,-4,-10,-1],[-10,-5,-9,3,-9,-6,1,-3,2,4,-1,-3],[-4,10,-5,-8,-9,-1,-7,-4,5,9,-9,-7],[-6,-6,-7,-1,-4,-7,-1,-6,-10,-1,-1,-1],[-6,-4,-1,-5,3,7,10,3,1,5,-4,4]],[[-5,-9,1,-5,-2,-1,-10,-1,8,3,8,-2],[-5,-2,-7,5,3,-10,-5,1,-2,10,1,-4],[-1,-6,4,-9,6,-10,-8,-5,-8,-5,-10,8],[-9,3,-2,-8,4,2,-2,7,-2,1,1,-3],[10,1,4,-1,2,2,1,-4,2,2,-7,-3],[5,3,1,6,3,3,-9,-10,-8,-4,2,3]],[[4,-9,-4,3,8,5,9,-1,1,2,6,-10],[4,-5,-1,-10,6,9,-4,9,-8,9,8,-2],[2,8,5,6,3,8,2,3,9,-7,-4,-5],[3,-10,4,9,-5,7,6,-1,-5,-2,-7,6],[-7,-9,1,3,-7,-4,-6,-8,9,-3,9,3],[5,2,2,-7,10,2,-9,-5,10,7,4,7]],[[9,8,5,3,-9,-1,-2,2,6,5,-10,2],[-4,6,-4,-1,4,-4,-3,7,9,-10,6,-7],[5,8,4,5,-10,-4,-5,-1,6,-6,-10,8],[-10,-4,-2,1,-3,-5,8,5,-1,4,5,3],[-1,-10,-3,-2,-9,-1,5,10,-10,5,5,8],[8,-9,9,4,-2,-1,-1,10,-9,-2,-5,-2]],[[-7,3,-6,5,-4,7,-10,-3,3,9,-7,5],[2,-2,-10,-1,1,9,4,-1,10,-2,-9,5],[9,6,-7,-3,8,5,10,-5,10,2,7,4],[1,10,-1,2,2,-9,8,-7,7,-4,-8,2],[4,3,7,-1,-3,10,7,-7,9,6,-8,-4],[5,-6,9,-2,-1,-4,-4,9,-5,3,-9,9]]], dtype = "uint32")#candidate|5815|(13, 6, 12)|const|uint32
var_5816 = relay.var("var_5816", dtype = "uint32", shape = (13, 6, 12))#candidate|5816|(13, 6, 12)|var|uint32
bop_5817 = relay.add(const_5815.astype('uint32'), relay.reshape(var_5816.astype('uint32'), relay.shape_of(const_5815))) # shape=(13, 6, 12)
bop_5823 = relay.greater_equal(var_5816.astype('bool'), relay.reshape(bop_5817.astype('bool'), relay.shape_of(var_5816))) # shape=(13, 6, 12)
var_5831 = relay.var("var_5831", dtype = "uint32", shape = (13, 6, 12))#candidate|5831|(13, 6, 12)|var|uint32
bop_5832 = relay.bitwise_or(var_5816.astype('uint16'), relay.reshape(var_5831.astype('uint16'), relay.shape_of(var_5816))) # shape=(13, 6, 12)
output = relay.Tuple([bop_5823,bop_5832,])
output2 = relay.Tuple([bop_5823,bop_5832,])
func_5840 = relay.Function([var_5816,var_5831,], output)
mod['func_5840'] = func_5840
mod = relay.transform.InferType()(mod)
mutated_mod['func_5840'] = func_5840
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5840_call = mutated_mod.get_global_var('func_5840')
var_5842 = relay.var("var_5842", dtype = "uint32", shape = (13, 6, 12))#candidate|5842|(13, 6, 12)|var|uint32
var_5843 = relay.var("var_5843", dtype = "uint32", shape = (13, 6, 12))#candidate|5843|(13, 6, 12)|var|uint32
call_5841 = func_5840_call(var_5842,var_5843,)
output = call_5841
func_5844 = relay.Function([var_5842,var_5843,], output)
mutated_mod['func_5844'] = func_5844
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5908 = relay.var("var_5908", dtype = "float64", shape = (13, 5, 11))#candidate|5908|(13, 5, 11)|var|float64
uop_5909 = relay.atanh(var_5908.astype('float64')) # shape=(13, 5, 11)
func_762_call = mod.get_global_var('func_762')
func_764_call = mutated_mod.get_global_var('func_764')
call_5913 = relay.TupleGetItem(func_762_call(), 0)
call_5914 = relay.TupleGetItem(func_764_call(), 0)
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_5916 = relay.TupleGetItem(func_4240_call(), 0)
call_5917 = relay.TupleGetItem(func_4241_call(), 0)
uop_5922 = relay.cosh(uop_5909.astype('float32')) # shape=(13, 5, 11)
bop_5924 = relay.logical_and(var_5908.astype('bool'), relay.reshape(uop_5909.astype('bool'), relay.shape_of(var_5908))) # shape=(13, 5, 11)
const_5936 = relay.const([[[-7.069071,-5.789261,9.182509,0.469892,2.783137,1.060874,8.260462,-2.310656,2.104933,2.187751,6.305290],[-9.473701,9.810199,-1.048788,-4.581555,4.780126,3.897025,-3.435779,-6.377278,7.013160,-5.286792,-6.921919],[4.925436,2.033932,0.050782,-4.113349,3.677744,-8.300994,0.900143,2.509704,-0.605097,5.029157,-0.685890],[-1.809143,0.054213,4.656044,7.957141,6.719429,-7.200865,6.647847,-4.988749,-9.094964,-6.425644,-6.985811],[-7.293241,-5.125517,7.232556,-5.906051,3.114744,-5.625869,-8.907835,-9.567402,0.364302,0.885319,0.912197]],[[-4.852771,-7.864186,3.868538,0.543498,-2.722676,5.075959,-3.038674,-4.841855,-2.446830,-3.617844,2.014835],[-9.714755,-1.259778,8.685319,6.169224,-3.898439,-8.041733,8.942542,-6.376983,-0.147334,-9.232329,8.401426],[-1.633930,7.520363,0.873725,8.926232,1.332782,9.286468,6.537380,4.844421,1.456866,-8.508782,-7.059428],[6.790801,-1.706482,4.239494,7.325574,-4.567210,3.977442,-2.363133,0.807128,6.741377,-5.518694,-4.426336],[7.886758,-7.069022,5.999083,9.177804,-1.435771,-8.923425,-9.155193,8.096058,-3.523174,4.019069,-9.464935]],[[3.789071,2.569980,-5.244689,8.007172,0.209629,-5.056420,5.241555,9.071378,6.712499,2.198693,-7.507263],[4.455720,7.135742,3.249406,6.120867,-8.504521,9.434536,7.789986,2.528772,-4.762482,-8.906778,2.952411],[0.667752,-9.937705,-6.793595,-9.708208,5.803132,9.068490,-1.138763,0.361092,-8.808055,-9.147474,3.501222],[5.041435,-4.309847,4.139542,-1.306958,-0.446856,0.352279,-8.942900,-9.902636,6.124170,-5.268147,-3.823407],[0.115114,7.048716,5.443258,-3.663573,9.944473,-7.310030,9.853916,-5.653734,-7.583214,1.285919,6.170177]],[[2.620251,6.682037,1.563551,2.957397,-3.451631,7.873691,-8.862415,4.016106,5.010698,-0.416816,-0.754865],[-2.639836,5.850546,6.027382,-6.842934,-2.964639,-6.531497,-1.142054,-3.773962,4.285460,9.761461,-1.204611],[9.441660,-6.528147,-4.884559,-4.686123,-1.674404,-1.979693,3.017830,5.490286,-3.699003,-7.885930,4.101287],[6.931868,-4.603374,-3.137462,7.042641,-6.433485,-6.803297,-9.470256,6.950461,6.105741,5.144965,-8.671354],[9.552078,-8.142917,9.550954,-0.122659,-6.816580,-1.493478,-4.983426,-6.770417,7.538810,-9.841225,3.103965]],[[9.294120,-5.896653,-8.047038,-3.276576,-1.113426,-8.233075,6.154165,5.037180,-6.976043,1.504159,8.884047],[3.138756,-4.659254,-8.296378,-5.807269,2.860249,-6.062217,-1.613670,5.593172,9.480800,-5.144739,-2.993995],[-4.877803,1.575218,7.151976,8.667479,-7.812416,-3.762847,-2.381652,-1.734376,-0.648611,-1.133248,1.863201],[-3.025448,3.739179,-9.643034,3.430262,6.093209,7.319427,5.287249,-8.861193,4.258625,3.670934,3.602234],[-0.511056,1.260457,1.809872,4.230826,-2.322215,2.830957,-7.955837,-7.912225,-6.356918,2.809839,-2.584307]],[[3.659461,9.224218,-2.000917,-7.943215,-9.649398,4.955752,-6.358162,7.027234,4.543772,6.455518,8.257081],[-4.819406,8.517577,-6.968508,-8.968987,4.694999,2.592282,-1.531477,-1.128091,6.212361,4.714463,-5.709721],[1.196066,-4.612433,6.692861,7.837511,1.164635,-5.316067,-6.089345,2.356561,-9.520133,-2.956567,3.628772],[9.414769,-2.487553,1.690064,4.106474,0.176501,7.369081,9.283864,1.511838,-1.578868,-8.851117,3.807657],[3.701923,-6.978057,-3.118058,7.485872,5.453745,4.941281,3.022857,-3.856150,-0.879205,9.213900,1.546621]],[[-5.134329,0.184636,0.154005,-4.872354,-5.499531,8.362748,7.083107,-3.159779,7.708822,2.336866,9.188056],[3.021096,4.289343,3.382273,-9.015464,6.443571,6.466010,7.918207,-0.647836,2.706659,7.668301,6.699860],[-5.128290,1.620502,-7.596408,-8.108171,9.349630,9.934725,0.682532,2.384420,7.410190,0.259257,2.319636],[9.082401,-3.146070,-3.055505,7.524288,-3.765271,5.051485,1.435644,-7.668792,4.576944,-7.645935,-9.321022],[8.634917,4.838970,-2.718203,5.813073,5.941436,3.593332,-3.470615,0.782129,-1.365471,6.041307,0.092206]],[[7.706291,1.202982,8.760451,0.346476,2.670975,9.306155,4.352490,4.781633,3.785689,3.332274,-9.189917],[-4.115309,7.253209,5.974312,3.522206,5.565883,-0.405854,7.049589,-1.395357,1.506905,-2.755039,-3.028017],[-4.696180,-2.602502,-4.183293,6.564675,5.234800,-5.824158,-3.030013,-8.159646,-1.000317,-7.813845,-1.296974],[-9.110604,-4.121648,-4.941427,-7.087103,-2.612057,0.046144,-8.151530,-2.797537,-0.340408,-7.978771,-6.188672],[2.424905,-7.331895,-1.666068,-0.524538,-2.976878,-4.922584,6.396187,9.363303,8.081184,-0.758904,4.739976]],[[5.390674,-8.551245,3.434175,-2.946633,4.698310,-2.493681,-9.059673,-5.092654,7.039006,5.411799,0.694297],[1.540628,0.325515,-8.422708,1.003443,-0.570622,6.842971,-7.634976,1.258750,-3.812380,-7.409615,-6.048026],[-3.966619,-7.287712,-5.603887,8.202191,-5.052551,-1.086633,4.310184,3.601721,-6.891658,5.611735,7.957071],[8.505581,5.086804,6.779606,-7.602481,-3.476527,2.395693,0.791458,-1.588154,1.237500,8.987585,-0.989494],[5.116147,2.685872,-8.826324,1.454839,-8.431365,-2.787950,0.327500,-2.668531,-9.999619,-1.768513,2.894570]],[[2.738247,-3.528495,-8.630901,-3.192577,-3.864599,-9.595749,-4.837105,3.277360,-3.526942,-7.015246,8.679956],[5.598458,5.300509,-8.373092,2.028628,0.056113,0.060476,6.030590,5.645233,8.048647,3.914149,1.530954],[-3.391932,-6.927456,9.147866,3.204943,-0.690199,-3.294313,-4.181458,7.671235,-5.767062,-8.527844,-9.350177],[4.883133,-6.208539,4.473018,-1.047985,3.754849,5.608565,-8.904631,-8.843050,7.657318,-7.738688,-4.793240],[-9.893703,-6.755658,8.002718,4.468479,-2.147705,0.645660,2.081607,4.932943,-3.460404,-3.147188,-1.861769]],[[-7.797537,-3.480624,8.403784,4.272830,-7.413632,6.778569,-3.070227,5.093521,-3.068637,-6.570237,-1.014687],[-2.637458,9.552995,-3.096454,0.467495,-8.997269,6.808309,1.955870,8.486922,7.675535,3.984321,-3.542658],[8.668506,2.212383,-5.098465,4.108012,4.463500,-9.180936,-5.403092,-6.781736,6.074562,7.991849,9.676073],[2.158348,1.718601,-6.573153,2.033205,-8.450050,2.302609,-3.193456,0.084711,-8.556191,7.964707,-3.845046],[-2.976700,1.317940,7.465290,-3.242247,-9.044294,-0.050185,-1.250296,-9.350124,8.884931,-3.668430,-1.412306]],[[-9.454552,5.469786,-1.540417,1.212455,-7.919184,0.670693,5.794488,9.063550,5.856725,3.383692,8.189673],[7.938736,9.960046,6.034017,7.263721,-3.245665,6.431577,-7.143902,9.977868,-7.924166,8.371692,0.924435],[3.166723,7.689933,-8.574003,-0.257433,-1.553958,5.154452,-2.422191,-3.851008,-9.513990,-8.344021,-0.311790],[6.591343,-8.533282,1.531905,6.737414,3.505498,9.017090,-8.690577,0.300876,-4.154622,-4.438362,-3.893407],[-7.510013,-9.464951,8.779223,-0.687225,7.500114,9.667301,-8.900079,-6.063013,-5.547871,-2.851672,-1.811947]],[[7.865326,6.103680,2.870650,-4.216131,-0.488516,-8.337119,2.472284,1.791841,5.671930,-8.908871,4.757544],[-0.596732,-1.707979,0.161734,-3.103229,7.956678,4.920352,3.294904,-9.160291,-1.725846,-7.508204,9.447199],[8.529041,-1.208422,-2.522003,0.254360,8.522052,8.900186,-3.888925,-7.266038,-4.104333,9.189830,-9.304701],[-7.023693,-5.560805,8.811215,-0.865316,-2.990041,-5.849840,-3.391447,4.460304,-7.461822,1.110369,7.501844],[-1.972652,7.597025,9.399178,-6.993321,5.929868,2.867840,-5.108452,3.020636,1.147827,-3.615938,-2.396899]]], dtype = "float32")#candidate|5936|(13, 5, 11)|const|float32
bop_5937 = relay.divide(uop_5922.astype('float32'), relay.reshape(const_5936.astype('float32'), relay.shape_of(uop_5922))) # shape=(13, 5, 11)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_5951 = relay.TupleGetItem(func_4023_call(), 0)
call_5952 = relay.TupleGetItem(func_4025_call(), 0)
func_2665_call = mod.get_global_var('func_2665')
func_2667_call = mutated_mod.get_global_var('func_2667')
var_5965 = relay.var("var_5965", dtype = "float32", shape = (81, 10))#candidate|5965|(81, 10)|var|float32
call_5964 = relay.TupleGetItem(func_2665_call(relay.reshape(var_5965.astype('float32'), [9, 15, 6])), 3)
call_5966 = relay.TupleGetItem(func_2667_call(relay.reshape(var_5965.astype('float32'), [9, 15, 6])), 3)
output = relay.Tuple([call_5913,call_5916,bop_5924,bop_5937,call_5951,call_5964,var_5965,])
output2 = relay.Tuple([call_5914,call_5917,bop_5924,bop_5937,call_5952,call_5966,var_5965,])
func_5973 = relay.Function([var_5908,var_5965,], output)
mod['func_5973'] = func_5973
mod = relay.transform.InferType()(mod)
var_5974 = relay.var("var_5974", dtype = "float64", shape = (13, 5, 11))#candidate|5974|(13, 5, 11)|var|float64
var_5975 = relay.var("var_5975", dtype = "float32", shape = (81, 10))#candidate|5975|(81, 10)|var|float32
output = func_5973(var_5974,var_5975,)
func_5976 = relay.Function([var_5974,var_5975,], output)
mutated_mod['func_5976'] = func_5976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2273_call = mod.get_global_var('func_2273')
func_2275_call = mutated_mod.get_global_var('func_2275')
call_5978 = func_2273_call()
call_5979 = func_2273_call()
func_435_call = mod.get_global_var('func_435')
func_437_call = mutated_mod.get_global_var('func_437')
call_5998 = relay.TupleGetItem(func_435_call(relay.reshape(call_5978.astype('bool'), [2, 12, 9])), 0)
call_5999 = relay.TupleGetItem(func_437_call(relay.reshape(call_5978.astype('bool'), [2, 12, 9])), 0)
output = relay.Tuple([call_5978,call_5998,])
output2 = relay.Tuple([call_5979,call_5999,])
func_6001 = relay.Function([], output)
mod['func_6001'] = func_6001
mod = relay.transform.InferType()(mod)
mutated_mod['func_6001'] = func_6001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6001_call = mutated_mod.get_global_var('func_6001')
call_6002 = func_6001_call()
output = call_6002
func_6003 = relay.Function([], output)
mutated_mod['func_6003'] = func_6003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mod.get_global_var('func_4057')
func_4059_call = mutated_mod.get_global_var('func_4059')
call_6050 = relay.TupleGetItem(func_4057_call(), 2)
call_6051 = relay.TupleGetItem(func_4059_call(), 2)
output = relay.Tuple([call_6050,])
output2 = relay.Tuple([call_6051,])
func_6059 = relay.Function([], output)
mod['func_6059'] = func_6059
mod = relay.transform.InferType()(mod)
mutated_mod['func_6059'] = func_6059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6059_call = mutated_mod.get_global_var('func_6059')
call_6060 = func_6059_call()
output = call_6060
func_6061 = relay.Function([], output)
mutated_mod['func_6061'] = func_6061
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6130 = relay.const([[[9,-5,-5,3,-9,8,9,-9,-6],[7,-1,-10,-9,-3,-4,-4,10,-9],[8,-8,-8,4,-10,8,-10,-1,-10],[-10,-8,1,9,-3,7,-6,4,9],[2,1,6,9,6,1,-5,-6,3],[-2,-5,3,-9,-4,-5,-4,8,-9],[5,-2,-2,-7,-3,-7,-2,-1,6],[-8,5,7,-7,-4,-8,-1,3,-6],[-6,1,7,8,-8,6,-2,-10,-6],[-4,-8,2,-3,9,-6,-10,-7,4],[8,-3,10,10,-4,7,-7,-5,-1],[-1,9,2,-4,-2,3,6,7,-8],[7,-6,-10,10,-8,-4,-3,-3,6]],[[2,8,-2,-9,4,6,-2,4,3],[-5,-3,2,-1,-2,-9,-10,8,-4],[-10,-7,-10,6,7,2,-4,-4,9],[6,-1,4,7,-3,-3,7,2,8],[8,-6,4,4,-6,-4,-4,-4,-9],[5,4,4,6,1,-5,10,10,10],[-3,-1,3,-3,-6,-2,-7,2,4],[7,7,-8,6,8,3,2,-2,-4],[-10,2,5,-2,10,2,-10,-3,-8],[1,-8,-1,-9,-6,8,6,8,6],[1,-4,2,4,-6,2,10,9,2],[-9,-5,-2,7,-2,7,8,6,6],[1,-1,-8,10,-6,-6,-1,1,-1]],[[10,2,-3,-10,4,7,3,3,5],[-6,-9,-6,-1,9,-2,7,-8,-5],[-8,4,-10,-6,-8,-8,-10,8,7],[4,2,1,6,7,7,-5,-7,-6],[1,-2,9,-2,4,-10,-5,-8,10],[10,-7,9,8,-6,-4,-2,4,-4],[3,4,5,8,-10,4,8,-5,-10],[1,-10,-3,-9,9,-8,-8,6,-8],[-8,10,5,-10,-9,-9,1,7,7],[6,-4,1,6,2,-5,-5,-7,1],[-1,4,-5,-9,3,8,5,-5,-10],[10,10,-10,-2,-8,-9,10,9,10],[-9,2,4,-1,7,7,-4,3,-8]],[[-9,-7,-1,5,8,7,9,6,9],[5,-8,-6,8,-3,6,-4,-2,-1],[9,4,1,7,9,-3,-3,6,9],[-10,6,7,-3,-8,-2,-7,6,-10],[5,6,1,10,-8,-9,10,5,1],[9,-5,-2,-7,-1,2,-9,9,9],[-5,-5,-7,1,6,-5,-9,2,1],[-2,4,-3,-5,3,6,-5,3,3],[8,7,-9,10,7,4,7,8,1],[8,-4,1,3,2,-10,5,-8,-10],[7,6,4,-3,8,-2,5,-7,1],[8,6,9,2,3,-6,-8,5,-8],[6,1,3,2,-5,6,9,-7,1]],[[-2,-10,6,8,-1,-7,-1,10,-6],[-7,-2,1,6,1,6,9,-6,3],[-7,5,-5,8,-5,7,-3,4,-5],[-3,-5,-6,6,-9,6,-4,4,-2],[-2,-4,-9,10,5,9,-9,3,-7],[-4,-4,-7,4,3,1,-6,4,-1],[1,6,5,8,-8,-7,9,9,-4],[-4,-10,-6,-10,5,2,-8,-7,-9],[-8,6,7,10,-3,-9,-7,-5,8],[9,6,6,10,-1,8,9,4,-3],[-9,6,6,-8,6,2,-9,-6,5],[-2,-5,9,-2,3,-4,-8,-1,-4],[8,10,9,2,10,-2,-9,9,-7]],[[1,-9,-7,1,5,-8,1,-2,1],[-2,9,10,-9,6,-5,8,-2,2],[-9,3,-7,4,-6,-6,8,-10,9],[8,1,6,7,-3,1,8,-8,-4],[1,-10,6,6,3,-3,-7,2,5],[3,-4,-2,-2,6,1,-3,-10,3],[-1,10,-6,10,-3,9,-2,1,9],[-2,-4,-10,-8,1,-8,-4,3,4],[-4,-3,7,-7,6,-5,-3,-7,5],[4,-2,1,-9,-10,-6,4,-9,1],[10,-4,-7,-5,-6,-7,-10,4,6],[-4,10,-9,-10,-8,-1,4,-6,2],[-7,-4,-9,-6,10,3,-7,2,2]],[[-2,6,1,1,-1,-4,-2,9,-8],[5,-7,5,-4,8,-8,9,5,3],[5,1,-1,-10,-8,7,5,-7,8],[4,-4,7,-5,3,-2,-5,-8,-2],[1,-2,-8,4,-2,8,5,-3,6],[-1,6,2,10,-2,6,-9,-5,8],[3,-9,-3,8,-10,-8,-1,-9,5],[-5,-1,-5,-3,5,-9,-1,7,9],[8,-9,-8,-7,6,-8,-9,5,-1],[10,7,4,-10,-10,5,-6,-7,-1],[2,4,4,-10,-6,-5,-7,3,-10],[-2,1,9,1,1,2,3,-10,3],[-10,10,-10,-2,-2,5,-3,-4,10]],[[2,-9,-9,7,-5,8,4,3,-3],[9,-3,2,2,-6,-10,10,-8,-7],[9,9,-2,4,-5,7,1,5,6],[-2,5,-5,-4,8,-3,9,10,8],[2,-7,-8,-7,2,-2,1,7,2],[2,-8,-8,-9,4,4,3,-1,-5],[9,-7,5,-9,5,-2,-9,-3,-7],[7,9,-5,-3,-8,-1,3,-6,10],[2,-8,7,-6,-6,-5,-1,1,6],[-10,4,-3,-3,-6,-9,-10,8,-9],[-10,3,-3,3,3,-1,-7,5,-1],[10,-5,10,-3,-4,-10,5,-8,-10],[-5,3,4,-6,-7,4,-1,9,-1]],[[9,-1,4,-8,5,-5,6,-5,-9],[-5,2,8,-7,2,-3,6,8,5],[-1,9,8,1,6,-3,7,-10,9],[6,-4,-1,-1,1,6,-9,10,5],[4,1,3,2,3,10,-9,7,5],[2,-7,-5,-8,2,-4,5,-4,-5],[4,9,-1,-9,-5,6,6,-6,-1],[-8,7,9,8,9,-4,-8,-6,-6],[-8,-9,-3,3,-5,4,9,-6,-3],[-8,-3,-10,-5,-3,-9,-8,-4,-10],[-4,-8,-1,4,6,8,7,8,-5],[4,1,3,-8,5,-7,-1,-9,9],[-3,9,3,9,-5,9,-7,2,-2]],[[-8,-5,2,-9,3,2,-7,5,6],[-5,-5,2,-10,8,-9,-4,-9,-1],[1,4,7,7,2,-1,-7,3,-5],[-7,6,-7,-4,-5,10,-5,-7,4],[-6,-9,1,9,6,-2,-7,-8,-4],[1,3,-2,1,3,-8,-1,8,-5],[9,8,3,8,1,-4,-8,5,-10],[-6,4,-8,-8,7,8,6,-5,3],[-6,-8,5,-2,-7,-6,-3,8,4],[10,-3,-10,10,-8,-2,-2,2,-5],[-2,-1,3,-5,-2,6,9,9,-4],[4,-5,-8,5,-7,-10,3,-1,-2],[-4,3,-2,-5,4,4,5,1,-10]],[[8,8,2,8,-7,-2,5,6,5],[6,8,5,7,9,9,8,-7,-1],[-2,4,7,-10,3,10,-5,-7,-6],[6,2,3,7,7,6,10,-8,-9],[2,9,7,-5,-6,7,7,-5,-1],[10,-8,9,-6,3,-7,1,4,-7],[7,-5,-6,-5,6,-4,8,4,-3],[-3,-3,-3,1,-10,-1,-5,-10,-3],[3,-1,-10,7,-1,6,-5,2,-5],[10,8,10,8,-2,-8,-7,5,-1],[5,2,10,-9,-7,6,-6,8,8],[-7,-5,-7,4,-3,1,3,-3,-3],[3,9,5,-5,-2,6,3,8,-2]],[[1,8,2,-8,-7,-10,-2,-4,-6],[-6,9,4,-10,1,-6,-3,-7,-9],[-10,6,5,-8,10,2,1,6,8],[7,10,-5,1,1,9,-8,8,6],[1,-4,8,-6,-4,8,6,-9,5],[1,2,-7,4,9,1,-7,9,-3],[5,-5,6,10,-1,8,-5,-4,-3],[-7,8,10,9,-2,-9,5,-6,3],[-6,-4,4,-2,1,5,1,-2,7],[-8,7,7,5,-10,-4,5,-9,-6],[-2,-3,6,-8,9,-6,10,-3,4],[-5,-5,1,9,9,6,-1,4,1],[2,-9,-7,-7,8,6,-3,-8,5]]], dtype = "int8")#candidate|6130|(12, 13, 9)|const|int8
var_6131 = relay.var("var_6131", dtype = "int8", shape = (12, 13, 9))#candidate|6131|(12, 13, 9)|var|int8
bop_6132 = relay.left_shift(const_6130.astype('int8'), relay.reshape(var_6131.astype('int8'), relay.shape_of(const_6130))) # shape=(12, 13, 9)
output = relay.Tuple([bop_6132,])
output2 = relay.Tuple([bop_6132,])
func_6135 = relay.Function([var_6131,], output)
mod['func_6135'] = func_6135
mod = relay.transform.InferType()(mod)
mutated_mod['func_6135'] = func_6135
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6136 = relay.var("var_6136", dtype = "int8", shape = (12, 13, 9))#candidate|6136|(12, 13, 9)|var|int8
func_6135_call = mutated_mod.get_global_var('func_6135')
call_6137 = func_6135_call(var_6136)
output = call_6137
func_6138 = relay.Function([var_6136], output)
mutated_mod['func_6138'] = func_6138
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_6215 = relay.TupleGetItem(func_1502_call(), 0)
call_6216 = relay.TupleGetItem(func_1503_call(), 0)
func_4788_call = mod.get_global_var('func_4788')
func_4789_call = mutated_mod.get_global_var('func_4789')
call_6226 = func_4788_call()
call_6227 = func_4788_call()
var_6228 = relay.var("var_6228", dtype = "float64", shape = (2, 416))#candidate|6228|(2, 416)|var|float64
bop_6229 = relay.maximum(call_6226.astype('int8'), relay.reshape(var_6228.astype('int8'), relay.shape_of(call_6226))) # shape=(2, 416)
bop_6232 = relay.maximum(call_6227.astype('int8'), relay.reshape(var_6228.astype('int8'), relay.shape_of(call_6227))) # shape=(2, 416)
func_4985_call = mod.get_global_var('func_4985')
func_4987_call = mutated_mod.get_global_var('func_4987')
call_6237 = func_4985_call()
call_6238 = func_4985_call()
output = relay.Tuple([call_6215,bop_6229,call_6237,])
output2 = relay.Tuple([call_6216,bop_6232,call_6238,])
func_6240 = relay.Function([var_6228,], output)
mod['func_6240'] = func_6240
mod = relay.transform.InferType()(mod)
var_6241 = relay.var("var_6241", dtype = "float64", shape = (2, 416))#candidate|6241|(2, 416)|var|float64
output = func_6240(var_6241)
func_6242 = relay.Function([var_6241], output)
mutated_mod['func_6242'] = func_6242
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_6264 = relay.TupleGetItem(func_2863_call(), 2)
call_6265 = relay.TupleGetItem(func_2865_call(), 2)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_6266 = relay.TupleGetItem(func_542_call(), 0)
call_6267 = relay.TupleGetItem(func_543_call(), 0)
func_5840_call = mod.get_global_var('func_5840')
func_5844_call = mutated_mod.get_global_var('func_5844')
var_6283 = relay.var("var_6283", dtype = "uint32", shape = (6, 156))#candidate|6283|(6, 156)|var|uint32
call_6282 = relay.TupleGetItem(func_5840_call(relay.reshape(var_6283.astype('uint32'), [13, 6, 12]), relay.reshape(var_6283.astype('uint32'), [13, 6, 12]), ), 0)
call_6284 = relay.TupleGetItem(func_5844_call(relay.reshape(var_6283.astype('uint32'), [13, 6, 12]), relay.reshape(var_6283.astype('uint32'), [13, 6, 12]), ), 0)
output = relay.Tuple([call_6264,call_6266,call_6282,var_6283,])
output2 = relay.Tuple([call_6265,call_6267,call_6284,var_6283,])
func_6286 = relay.Function([var_6283,], output)
mod['func_6286'] = func_6286
mod = relay.transform.InferType()(mod)
var_6287 = relay.var("var_6287", dtype = "uint32", shape = (6, 156))#candidate|6287|(6, 156)|var|uint32
output = func_6286(var_6287)
func_6288 = relay.Function([var_6287], output)
mutated_mod['func_6288'] = func_6288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3573_call = mod.get_global_var('func_3573')
func_3575_call = mutated_mod.get_global_var('func_3575')
call_6312 = relay.TupleGetItem(func_3573_call(), 0)
call_6313 = relay.TupleGetItem(func_3575_call(), 0)
uop_6347 = relay.exp(call_6312.astype('float32')) # shape=(2, 12, 9)
uop_6349 = relay.exp(call_6313.astype('float32')) # shape=(2, 12, 9)
output = uop_6347
output2 = uop_6349
func_6350 = relay.Function([], output)
mod['func_6350'] = func_6350
mod = relay.transform.InferType()(mod)
mutated_mod['func_6350'] = func_6350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mutated_mod.get_global_var('func_6350')
call_6351 = func_6350_call()
output = call_6351
func_6352 = relay.Function([], output)
mutated_mod['func_6352'] = func_6352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mod.get_global_var('func_6350')
func_6352_call = mutated_mod.get_global_var('func_6352')
call_6373 = func_6350_call()
call_6374 = func_6350_call()
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_6383 = relay.TupleGetItem(func_4240_call(), 0)
call_6384 = relay.TupleGetItem(func_4241_call(), 0)
func_5638_call = mod.get_global_var('func_5638')
func_5640_call = mutated_mod.get_global_var('func_5640')
call_6387 = func_5638_call()
call_6388 = func_5638_call()
output = relay.Tuple([call_6373,call_6383,call_6387,])
output2 = relay.Tuple([call_6374,call_6384,call_6388,])
func_6401 = relay.Function([], output)
mod['func_6401'] = func_6401
mod = relay.transform.InferType()(mod)
output = func_6401()
func_6402 = relay.Function([], output)
mutated_mod['func_6402'] = func_6402
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1502_call = mod.get_global_var('func_1502')
func_1503_call = mutated_mod.get_global_var('func_1503')
call_6435 = relay.TupleGetItem(func_1502_call(), 2)
call_6436 = relay.TupleGetItem(func_1503_call(), 2)
output = call_6435
output2 = call_6436
func_6447 = relay.Function([], output)
mod['func_6447'] = func_6447
mod = relay.transform.InferType()(mod)
output = func_6447()
func_6448 = relay.Function([], output)
mutated_mod['func_6448'] = func_6448
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4023_call = mod.get_global_var('func_4023')
func_4025_call = mutated_mod.get_global_var('func_4025')
call_6518 = relay.TupleGetItem(func_4023_call(), 0)
call_6519 = relay.TupleGetItem(func_4025_call(), 0)
func_5840_call = mod.get_global_var('func_5840')
func_5844_call = mutated_mod.get_global_var('func_5844')
var_6528 = relay.var("var_6528", dtype = "uint32", shape = (936,))#candidate|6528|(936,)|var|uint32
call_6527 = relay.TupleGetItem(func_5840_call(relay.reshape(var_6528.astype('uint32'), [13, 6, 12]), relay.reshape(var_6528.astype('uint32'), [13, 6, 12]), ), 0)
call_6529 = relay.TupleGetItem(func_5844_call(relay.reshape(var_6528.astype('uint32'), [13, 6, 12]), relay.reshape(var_6528.astype('uint32'), [13, 6, 12]), ), 0)
output = relay.Tuple([call_6518,call_6527,var_6528,])
output2 = relay.Tuple([call_6519,call_6529,var_6528,])
func_6555 = relay.Function([var_6528,], output)
mod['func_6555'] = func_6555
mod = relay.transform.InferType()(mod)
var_6556 = relay.var("var_6556", dtype = "uint32", shape = (936,))#candidate|6556|(936,)|var|uint32
output = func_6555(var_6556)
func_6557 = relay.Function([var_6556], output)
mutated_mod['func_6557'] = func_6557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_542_call = mod.get_global_var('func_542')
func_543_call = mutated_mod.get_global_var('func_543')
call_6657 = relay.TupleGetItem(func_542_call(), 1)
call_6658 = relay.TupleGetItem(func_543_call(), 1)
output = call_6657
output2 = call_6658
func_6679 = relay.Function([], output)
mod['func_6679'] = func_6679
mod = relay.transform.InferType()(mod)
mutated_mod['func_6679'] = func_6679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6679_call = mutated_mod.get_global_var('func_6679')
call_6680 = func_6679_call()
output = call_6680
func_6681 = relay.Function([], output)
mutated_mod['func_6681'] = func_6681
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6685 = relay.const([[[6,-2,4,5,-6,10,9,1,-9,-6,-7,-5,-6],[-9,6,8,-5,-1,8,-10,7,6,-4,-3,-9,4],[-1,4,-7,10,6,-7,10,-10,6,-5,-10,8,-7],[6,10,-4,3,8,1,-5,-6,8,10,6,-5,-8],[1,8,-5,-8,8,-7,1,1,3,-9,-8,-7,-4],[-6,-6,-6,8,-7,-8,-9,-8,-7,2,-1,4,6],[-8,2,-7,-2,1,-2,-2,4,-5,-6,9,-3,3],[-8,3,-1,-6,-4,-1,8,6,3,-10,-10,7,-9],[1,-7,-6,-1,8,2,5,9,-6,-10,-8,2,7],[6,-10,-2,8,5,-4,-5,-10,-8,-4,-3,-7,-5],[-5,6,1,-5,6,-1,-9,-8,-7,-7,1,4,-6],[8,-1,8,-1,7,6,-4,1,9,-4,-3,10,-7],[-7,6,9,5,-8,3,1,3,4,-2,-5,-5,7]],[[-9,7,-8,9,8,-10,8,-9,-9,-3,-8,2,-3],[8,-7,5,-2,3,9,-5,-2,1,3,4,-8,6],[5,-5,-6,-6,8,8,6,-1,7,-1,1,2,-1],[7,3,-7,-3,9,-5,-2,-8,2,-4,-8,-9,2],[10,3,10,5,3,-4,-4,4,9,2,-8,1,7],[5,-10,-5,10,-4,-8,-4,10,-5,-2,-4,7,-10],[2,9,3,-7,-2,3,-2,4,7,9,7,-4,7],[10,3,10,-1,7,4,7,8,-10,9,10,-2,-5],[-5,8,6,5,-7,-7,4,4,-9,6,1,8,9],[-7,-7,10,9,3,5,5,2,2,-5,6,7,1],[-7,9,-5,7,-7,1,6,-1,1,-4,-9,9,-3],[8,-4,-10,-6,-6,-5,10,-1,-10,-6,-7,9,9],[8,-2,2,10,8,8,-9,4,9,-6,8,9,-8]],[[-2,8,7,-1,6,2,3,6,-6,8,-8,6,9],[-1,10,5,-8,-5,-8,7,-2,-9,-9,-6,9,6],[3,1,-8,10,-2,9,-7,-7,3,-6,3,9,10],[8,9,7,4,4,10,9,7,2,-4,-9,-2,-1],[-10,-8,6,-2,-8,7,-8,-5,4,-10,3,5,2],[-6,8,-9,8,3,-3,-8,-5,-2,-7,3,2,2],[-7,5,-10,-4,-8,1,2,9,10,-6,-4,9,-7],[1,-6,-5,10,10,2,-2,-7,-6,6,6,-5,-10],[3,10,-2,9,6,8,-7,7,4,-8,2,-2,1],[4,-10,-5,-4,3,8,3,-10,-9,3,4,5,8],[8,-8,8,7,6,1,8,9,5,-9,5,10,4],[-3,8,8,5,-8,-8,1,6,-8,-5,2,9,5],[-9,-9,-10,4,8,-5,10,6,-8,-3,-8,-1,-8]],[[-4,-4,10,-3,6,3,-3,-6,2,4,5,4,8],[-1,-6,4,7,-9,1,5,-7,-1,-1,-1,-2,-2],[8,-5,9,-7,-6,-7,9,1,1,-9,-6,1,7],[10,-8,6,-8,4,8,6,-10,-8,-2,1,5,-2],[-2,6,-8,9,-1,-3,6,8,-9,-8,9,10,-3],[5,-4,-6,-3,-4,-3,8,-7,-2,-10,-5,-9,8],[8,-1,2,8,-4,-10,9,9,-8,5,-10,8,-1],[9,-7,8,-8,6,-7,-5,1,10,-1,3,8,9],[-6,9,2,-7,-8,4,-6,-5,-7,3,-6,-9,4],[10,-1,-3,6,8,4,6,-2,8,-5,10,5,-1],[8,2,3,7,1,-4,-4,4,8,9,-2,-10,4],[-8,-3,2,10,-5,-3,8,-4,10,7,-5,-6,6],[3,-5,-6,-8,4,2,1,7,-2,10,1,4,-6]],[[4,-5,-1,6,9,-9,-3,-4,-6,-2,1,-10,-2],[2,9,-8,3,-3,4,-8,-3,8,1,1,-9,10],[9,-2,1,8,6,-2,9,-1,5,6,6,4,-9],[5,-7,7,-7,8,3,-7,-2,-5,-2,-6,6,7],[-7,1,7,4,-3,2,8,-7,6,1,2,-8,4],[5,5,4,-4,-10,3,5,-4,7,6,4,-7,-9],[3,-5,-1,-5,-2,-10,3,7,3,3,10,-9,3],[10,10,-3,5,8,-10,-2,-3,1,2,4,-2,5],[7,2,-9,2,-10,-2,4,-2,-4,-7,9,-3,-5],[-8,-3,3,-7,2,7,-5,10,5,9,8,-4,-10],[-2,3,9,-8,-4,-2,6,-7,7,-2,-1,-3,-4],[4,6,2,5,7,9,-6,-8,4,-2,7,-2,8],[-7,4,2,1,1,5,-9,2,8,8,6,-10,-2]],[[-10,9,10,1,-5,-3,8,-10,-2,5,-4,1,1],[-4,8,9,2,9,1,-5,2,5,-6,5,3,-3],[5,8,3,-6,-2,10,2,-6,-9,1,1,-1,2],[-4,-8,-9,2,10,3,-8,-2,9,-10,-8,5,10],[7,2,9,-2,4,-1,-1,2,8,1,10,3,2],[-1,-1,3,-4,5,3,-2,9,3,-6,-5,7,-2],[5,-9,7,4,-10,-3,-3,10,6,-5,7,6,-5],[8,9,8,-7,3,-8,-1,-5,3,-5,-6,-4,5],[-8,-5,-3,4,-4,8,-1,5,-7,8,-3,9,-3],[-8,-7,8,-5,8,-7,10,7,5,8,-7,-8,-4],[-5,6,2,-5,-6,-4,-8,-9,-7,8,-8,3,-5],[-8,5,-2,8,8,-4,7,-6,1,5,8,-10,7],[-9,1,-1,5,-4,8,-6,10,-9,-10,-9,-6,-10]]], dtype = "int64")#candidate|6685|(6, 13, 13)|const|int64
var_6686 = relay.var("var_6686", dtype = "int64", shape = (6, 13, 13))#candidate|6686|(6, 13, 13)|var|int64
bop_6687 = relay.greater(const_6685.astype('bool'), relay.reshape(var_6686.astype('bool'), relay.shape_of(const_6685))) # shape=(6, 13, 13)
output = bop_6687
output2 = bop_6687
func_6694 = relay.Function([var_6686,], output)
mod['func_6694'] = func_6694
mod = relay.transform.InferType()(mod)
var_6695 = relay.var("var_6695", dtype = "int64", shape = (6, 13, 13))#candidate|6695|(6, 13, 13)|var|int64
output = func_6694(var_6695)
func_6696 = relay.Function([var_6695], output)
mutated_mod['func_6696'] = func_6696
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_6713 = relay.TupleGetItem(func_2467_call(), 0)
call_6714 = relay.TupleGetItem(func_2468_call(), 0)
output = call_6713
output2 = call_6714
func_6718 = relay.Function([], output)
mod['func_6718'] = func_6718
mod = relay.transform.InferType()(mod)
mutated_mod['func_6718'] = func_6718
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6718_call = mutated_mod.get_global_var('func_6718')
call_6719 = func_6718_call()
output = call_6719
func_6720 = relay.Function([], output)
mutated_mod['func_6720'] = func_6720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6679_call = mod.get_global_var('func_6679')
func_6681_call = mutated_mod.get_global_var('func_6681')
call_6734 = func_6679_call()
call_6735 = func_6679_call()
func_5073_call = mod.get_global_var('func_5073')
func_5077_call = mutated_mod.get_global_var('func_5077')
var_6743 = relay.var("var_6743", dtype = "uint64", shape = (60, 2))#candidate|6743|(60, 2)|var|uint64
const_6744 = relay.const([-7,7,-2,-5,-4,9,-7,6,1,-3,1,5,-9,-2,-1,2,-5,9,7,10,-2,-5,-5,3,4,-3,7,8,3,4,6,9,-8,7,-2,-5,9,-3,2,8,-2,-10,9,7,-7,-5,9,-2,-4,-10,-7,-3,6,1,-4,3,-2,-4,-10,-2,-2,-8,2,-5,1,3,2,-6,-3,-8,6,2,-4,-10,7,-1,-10,9,-9,8,-4,1,8,6,-4,8,-6,9,-7,6,10,5,6,-2,2,6,3,-2,5,-4,-10,1,5,8,9,-5,1,1,-6,4,-4,-4,10,-2,1,3,10,-1,-6,-6,5,5,3,-5,10,-9,-2,5,-6,-6,-5,-2,3,-2,2,-3,1,-5,6,5,9,-2,4,2,4,-1,-5,8,6,-8,-9,-7,10,7,2,-2,4,2,3,2,-10,-8,5,4,5,-2,-2,5,1,-8,1,-3,-5,-7,-7,-6,9,3,-10,-7,-8,1,8,-3,-7,-3,2,7,1,6,10,-6,-5,-5,5,-4,-9,-4,-1,9,10,8,9,9,-9,1,-8,10,-5,2,5,4,9,2,-5,-9,4,-6,5,5,2,-3,3,6,6,-10,2,-6,2,-2,-10,1,-10,-9,4,-9,7,9,-5,10,10,4,-3,-4,10,-3,1,-6,-3,-6,-6,5,8,5,-8,-9,-4,2,-5,2,6,-8,1,8,9,-1,10,10,2,5,10,-10,-7,2,3,-7,-1,-6,9,6,-7,-2,-5,-8,10,6,-7,4,3,8,-2,-4,2,-7,3,8,2,-8,-4,3,2,-2,10,-3,-4,8,7,-2,2,-9,-5,-5,-9,-4,-1,-5,-8,2,-6,10,7,7,10,3,9,6,-1,2,8,-10,-5,-2,5,3,-10,-9,-1,-10,-6,-2,7,10,3,-5,-10,-9,-4,-9,6,8,7,2], dtype = "int8")#candidate|6744|(352,)|const|int8
var_6745 = relay.var("var_6745", dtype = "float32", shape = (448,))#candidate|6745|(448,)|var|float32
call_6742 = relay.TupleGetItem(func_5073_call(relay.reshape(var_6743.astype('uint64'), [120,]), relay.reshape(const_6744.astype('int8'), [352,]), relay.reshape(var_6745.astype('float32'), [448, 1]), ), 5)
call_6746 = relay.TupleGetItem(func_5077_call(relay.reshape(var_6743.astype('uint64'), [120,]), relay.reshape(const_6744.astype('int8'), [352,]), relay.reshape(var_6745.astype('float32'), [448, 1]), ), 5)
output = relay.Tuple([call_6734,call_6742,var_6743,const_6744,var_6745,])
output2 = relay.Tuple([call_6735,call_6746,var_6743,const_6744,var_6745,])
func_6761 = relay.Function([var_6743,var_6745,], output)
mod['func_6761'] = func_6761
mod = relay.transform.InferType()(mod)
var_6762 = relay.var("var_6762", dtype = "uint64", shape = (60, 2))#candidate|6762|(60, 2)|var|uint64
var_6763 = relay.var("var_6763", dtype = "float32", shape = (448,))#candidate|6763|(448,)|var|float32
output = func_6761(var_6762,var_6763,)
func_6764 = relay.Function([var_6762,var_6763,], output)
mutated_mod['func_6764'] = func_6764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_6771 = relay.TupleGetItem(func_2925_call(), 1)
call_6772 = relay.TupleGetItem(func_2927_call(), 1)
output = relay.Tuple([call_6771,])
output2 = relay.Tuple([call_6772,])
func_6778 = relay.Function([], output)
mod['func_6778'] = func_6778
mod = relay.transform.InferType()(mod)
output = func_6778()
func_6779 = relay.Function([], output)
mutated_mod['func_6779'] = func_6779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1064_call = mod.get_global_var('func_1064')
func_1066_call = mutated_mod.get_global_var('func_1066')
call_6789 = func_1064_call()
call_6790 = func_1064_call()
func_6135_call = mod.get_global_var('func_6135')
func_6138_call = mutated_mod.get_global_var('func_6138')
const_6799 = relay.const([-4,-7,-1,-4,10,-4,10,8,-8,-3,-8,9,-7,8,-1,-7,7,3,-6,8,-1,-3,-8,4,9,-8,-4,-2,9,-7,2,3,-6,9,3,10,-8,7,-1,4,2,10,-9,9,2,-8,7,-4,-10,-7,-8,9,9,4,8,-3,-7,8,-3,6,2,10,7,-4,-4,-10,-9,8,6,9,7,-6,-5,2,1,3,-2,-5,-4,-8,4,-1,-8,3,9,9,4,-2,-2,-6,4,8,-2,-7,-4,5,2,10,-4,-5,5,-3,-1,-7,-1,6,2,-3,5,-3,4,6,5,-7,9,6,-6,-2,-3,-8,1,2,-5,2,-5,-10,4,-7,4,-1,-6,8,3,-6,8,-1,-7,-6,7,4,-2,5,2,8,5,-2,4,2,-9,-4,-2,8,7,2,2,8,-2,-4,4,-2,-9,10,2,1,-10,-8,1,4,10,3,-3,9,-3,-8,5,8,4,-7,9,8,6,-6,2,4,5,5,8,1,-7,8,1,-5,-3,-1,-4,-6,5,-5,9,10,-7,-1,-6,-6,-3,4,10,1,4,8,3,8,5,6,3,9,8,4,-2,9,-5,-1,6,8,6,-8,1,6,9,1,5,-1,10,8,-4,-9,-4,3,4,10,1,-8,5,-10,5,8,1,-4,-5,-5,3,-9,8,-7,-5,-2,-6,-9,-6,7,10,1,5,4,-8,-10,-3,-8,-2,3,3,-4,-8,1,-3,5,-4,-5,-10,10,8,-8,8,3,-10,-7,-4,1,-5,-7,-1,-10,-7,-5,-5,-4,6,5,-8,3,-5,-9,3,-2,-2,-5,-9,9,3,4,10,3,10,9,-8,-5,5,1,-4,8,-10,-9,1,7,-2,4,-9,-6,-6,-10,-9,7,-9,-4,1,-8,-5,4,-5,-10,1,8,10,2,1,2,7,2,8,-8,7,4,5,10,8,-8,3,-1,-2,-10,-5,10,2,7,-9,-10,4,-2,9,-10,1,6,-6,6,-1,8,9,-9,2,-10,4,-1,4,-7,3,-2,7,-8,-6,-8,1,5,8,8,4,2,7,-4,7,4,1,4,-3,-1,-7,7,9,-7,-8,6,2,-9,3,8,7,10,7,7,6,-10,-1,2,-9,-4,3,-8,-9,-6,10,-10,7,6,6,5,-3,7,-1,3,-8,-8,6,8,5,-8,7,4,10,9,7,-7,8,-4,3,-1,-6,-3,-7,10,6,-6,5,-6,-2,-10,10,9,9,9,3,-4,8,-1,-8,-6,-8,7,2,10,-10,-3,6,-8,-9,9,-6,-1,10,-1,5,-5,10,6,-7,8,-7,-8,6,9,3,-5,3,-5,-10,-1,4,7,8,-7,-10,-2,7,9,6,-9,8,-7,-2,3,-1,-6,-10,2,-4,5,-6,-2,-7,-8,-1,-1,1,-9,2,-4,6,-1,-10,-8,-2,2,-10,-2,-9,7,7,10,-7,2,1,-4,5,7,8,4,6,7,2,2,-10,-1,8,5,-2,-5,-3,2,-4,-5,-2,-2,7,-6,-1,-10,7,7,3,-9,7,10,2,-9,-10,-1,-3,3,-4,-9,-5,-7,-10,-8,-6,-10,10,4,9,-10,-8,-1,4,3,3,7,10,-10,8,-3,-2,7,10,-6,3,-8,-7,-1,5,2,-5,3,3,-6,-1,5,-2,7,-4,-3,-1,9,3,10,6,-3,-3,8,4,-8,5,-8,8,10,-10,-10,-5,-10,8,4,4,-5,-8,4,9,6,-9,-8,2,10,1,5,-8,-4,-7,-2,-8,9,-2,-7,-8,2,7,-4,-9,3,4,-8,2,-1,-10,1,2,3,6,-4,3,10,7,9,8,-8,9,-9,7,4,-4,5,-7,-9,-10,-5,-8,-5,9,-1,-7,3,4,-8,1,8,7,1,-2,4,3,7,6,-6,-5,4,-5,-7,-9,10,7,7,-1,-7,-9,9,2,-5,7,5,-10,3,8,-6,4,-8,6,-6,-4,-2,-6,6,6,-8,5,-4,-4,2,-4,10,-4,1,-4,9,-10,10,1,-5,9,9,-7,-9,-9,-3,-9,2,-1,-5,2,2,2,-7,10,-3,7,3,6,-5,10,7,2,5,4,8,-2,7,4,9,8,-3,6,9,7,-5,3,-8,-3,8,-1,-3,-9,-6,-6,9,1,-1,7,6,-5,2,-7,2,-1,9,-7,6,-5,-8,-1,7,10,-6,-7,2,-5,9,-3,2,-1,10,5,3,8,1,2,-9,5,1,10,-5,8,-7,-6,6,1,-5,-2,4,-4,9,-4,-8,6,10,-3,-10,-8,-3,-7,-4,-5,-3,-9,-8,4,1,-8,7,-10,-1,-4,3,10,-8,5,5,1,10,9,-5,5,-2,-4,-8,-8,7,-2,3,8,-10,3,4,5,6,-2,-6,-6,2,7,-6,1,-6,4,8,5,7,-5,-4,7,-6,-10,7,-3,7,1,7,-5,-6,6,-4,-1,-9,-2,-7,-2,7,5,5,3,10,-5,7,-9,2,-6,-6,-5,-5,9,-5,5,10,-6,-10,9,4,-6,-6,5,-2,-2,9,-7,-4,6,-7,1,-5,-6,-9,-6,1,-5,8,-2,-10,3,2,4,6,7,-5,3,-9,-6,4,-3,-5,-9,-8,-7,7,-8,2,9,5,3,6,9,-5,-4,-6,-3,3,8,-4,10,5,-10,-3,4,5,-8,-3,6,2,6,-7,1,-10,-3,-3,4,2,-4,-5,3,-8,-2,-7,-9,-8,-7,2,7,8,-4,1,-9,-6,-10,-5,-2,5,4,-2,-9,7,-7,5,-3,-2,-1,7,-7,-7,3,-1,5,-8,-6,-1,1,2,-9,10,7,8,-4,-10,-7,10,-8,-4,-7,-1,3,9,-2,-3,-7,4,4,1,-7,3,-7,6,5,8,4,-6,-1,-4,7,5,-8,-7,-9,2,-1,-3,-7,-6,1,-4,-3,-6,7,-7,-5,8,9,8,6,-7,-7,9,-9,8,-1,7,-3,8,2,4,-8,-1,-8,9,10,-4,6,3,-10,-7,3,5,-8,-6,8,8,-2,7,9,-7,1,8,-7,-3,1,-10,-6,10,7,2,8,3,8,-2,-5,-8,10,-4,-6,-4,8,3,8,-8,1,-2,2,9,-7,-9,-7,9,-2,4,9,-8,1,-1,-7,4,8,9,3,-10,-8,-1,5,-4,-2,-6,8,9,5,8,10,-10,-10,-8,6,1,8,-10,-3,-1,-5,-7,-1,2,-8,-6,2,9,-6,5,7,-7,-10,-2,-3,2,-10,-1,-7,4,3,6,-9,-9,3,8,-2,7,-2,-6,1,-3,7,9,6,1,-5,-5,3,-9,10,6,-2,3,-3,-9,7,5,-5,-9,-10,-8,-9,-1,-9,-7,-10,8,-10,-6,-9,7,-6,-1,-9,-9,1,5,-2,-2,-7,-1,-4,8,9,-6,8,4,10,-6,6,-7,5,-8,-8,-10,-9,-1,10,-6,-1,9,10,5,9,-6,-7,5,-6,-10,1,-9,-3,-5,10,-3,-6,2,6,-5,-9,1,5,-9,-6,5,-1,10,-5,-6,-8,5,1,-1,7,1,6,-5,7,2,-2,-5,-9,8,1,6,3,3,-1,1,8,-5,4,-5,-3,-6,-2,-10,5,-7,-2,-4,-6,-10,-3,6,-3,-8,-8,-7,10,8,2,4,-5,-2,4,1,6,9,-2,-3,-4,1,-3,-5,-10,4,-10,-9,-1,-10,-8,-5,4,-4,-8,3,-7,6,-1,-3,-5,-2,7,-7,-2,-3,2,5], dtype = "int8")#candidate|6799|(1404,)|const|int8
call_6798 = relay.TupleGetItem(func_6135_call(relay.reshape(const_6799.astype('int8'), [12, 13, 9])), 0)
call_6800 = relay.TupleGetItem(func_6138_call(relay.reshape(const_6799.astype('int8'), [12, 13, 9])), 0)
func_623_call = mod.get_global_var('func_623')
func_625_call = mutated_mod.get_global_var('func_625')
call_6803 = func_623_call()
call_6804 = func_623_call()
output = relay.Tuple([call_6789,call_6798,const_6799,call_6803,])
output2 = relay.Tuple([call_6790,call_6800,const_6799,call_6804,])
func_6806 = relay.Function([], output)
mod['func_6806'] = func_6806
mod = relay.transform.InferType()(mod)
output = func_6806()
func_6807 = relay.Function([], output)
mutated_mod['func_6807'] = func_6807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4189_call = mod.get_global_var('func_4189')
func_4190_call = mutated_mod.get_global_var('func_4190')
call_6830 = relay.TupleGetItem(func_4189_call(), 0)
call_6831 = relay.TupleGetItem(func_4190_call(), 0)
output = call_6830
output2 = call_6831
func_6848 = relay.Function([], output)
mod['func_6848'] = func_6848
mod = relay.transform.InferType()(mod)
mutated_mod['func_6848'] = func_6848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6848_call = mutated_mod.get_global_var('func_6848')
call_6849 = func_6848_call()
output = call_6849
func_6850 = relay.Function([], output)
mutated_mod['func_6850'] = func_6850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5196_call = mod.get_global_var('func_5196')
func_5197_call = mutated_mod.get_global_var('func_5197')
call_6927 = func_5196_call()
call_6928 = func_5196_call()
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_6942 = relay.TupleGetItem(func_1145_call(), 0)
call_6943 = relay.TupleGetItem(func_1147_call(), 0)
func_5714_call = mod.get_global_var('func_5714')
func_5715_call = mutated_mod.get_global_var('func_5715')
call_6946 = relay.TupleGetItem(func_5714_call(), 0)
call_6947 = relay.TupleGetItem(func_5715_call(), 0)
output = relay.Tuple([call_6927,call_6942,call_6946,])
output2 = relay.Tuple([call_6928,call_6943,call_6947,])
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
func_4142_call = mod.get_global_var('func_4142')
func_4144_call = mutated_mod.get_global_var('func_4144')
call_7040 = relay.TupleGetItem(func_4142_call(), 0)
call_7041 = relay.TupleGetItem(func_4144_call(), 0)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_7044 = relay.TupleGetItem(func_1454_call(), 0)
call_7045 = relay.TupleGetItem(func_1456_call(), 0)
func_5165_call = mod.get_global_var('func_5165')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_7048 = relay.TupleGetItem(func_5165_call(), 4)
call_7049 = relay.TupleGetItem(func_5166_call(), 4)
const_7057 = relay.const([[-6,1,10,-10,-4,5,2,-1,10,-9,6,5,-5,7,-8,3,-6,1,-8,10,5,7,7,-8,-3,6,-7,7,5,3,-7,-9,-1,-8,-9,-3,4,-6,2,-9,-3,6,6,-1,7,6,2,-4,-4,-6,-1,-9,-10,7,1,9,-1,-1,10,9,7,1,9,-4,8,-7,-8,-5,1,4,-9,5,10,6,9,-9,-1,6,8,4,-2,8,-7,-10],[-6,-10,7,-5,-1,-1,8,-7,-4,2,6,9,-7,6,1,-4,-2,10,-10,-8,-5,1,1,-4,-4,-9,4,-6,7,7,-10,3,-5,-1,7,6,-2,-9,7,-8,-2,1,4,-7,1,-9,2,3,4,-2,7,6,7,2,1,-6,8,-6,-5,5,6,-9,5,-6,9,-3,8,-6,5,10,2,6,3,6,7,-6,-5,-1,-8,-1,-7,-3,-4,-1],[-9,-4,6,2,-3,9,-10,-1,1,-7,-9,6,-3,-2,-8,-5,-3,-9,-8,-8,9,-1,4,6,-5,6,1,1,-1,-8,-5,5,1,-5,-4,10,-2,-4,4,-4,3,3,4,-6,7,3,1,10,-3,-1,-9,2,-3,-10,6,-5,5,-1,-2,-5,4,-2,7,7,8,5,-10,-1,-3,1,4,-8,-4,8,-7,4,1,6,-8,6,-2,5,9,-6],[-4,2,5,-5,-9,6,5,9,5,-4,10,-1,4,-6,-10,5,-1,2,-9,6,1,5,-1,-4,10,1,1,-4,-10,5,-3,3,-9,10,3,5,-8,-4,5,-5,-7,6,-10,2,-1,9,-9,-7,-9,-8,3,-8,6,-7,-1,7,-9,-7,-5,9,6,-9,-2,5,3,6,9,-6,8,-7,6,-7,8,7,3,-1,-4,5,-9,7,-8,-8,7,-3],[7,-3,5,-1,-4,-10,4,7,4,-4,-6,4,4,-10,-8,-7,4,-10,-10,4,9,2,-5,-1,-4,-1,8,4,-9,-4,-9,4,8,4,4,3,-4,-7,7,8,-3,-2,6,2,4,2,6,9,-9,4,-5,-9,4,-5,-1,2,4,4,4,5,1,-1,5,-3,-7,10,-5,-8,-4,-2,8,1,-2,1,-3,1,-4,-3,4,-3,-4,-2,3,-10],[5,-4,-7,-4,-1,4,9,-8,-10,2,-6,7,-2,-10,7,4,5,-6,4,-3,4,9,-3,-8,7,-8,-9,-4,2,-7,-8,-4,10,7,-9,-9,6,-8,-4,-3,-8,-5,-6,9,-4,10,9,7,1,3,2,2,-9,-8,-9,-3,2,8,-6,-7,-5,-4,-10,-2,-5,-2,9,5,-8,-1,6,6,2,7,10,10,-2,8,5,4,6,-7,3,3],[6,8,9,-9,5,1,-9,-9,-7,-2,8,2,-5,-9,4,-10,7,4,10,-9,9,-10,-2,1,7,-2,1,-7,5,-5,-9,1,2,3,7,9,-5,6,10,-7,-1,10,-4,-8,-4,-10,-9,10,-4,-3,7,9,-1,-1,2,-5,-8,-7,-1,-3,-2,-9,-4,2,4,-1,5,2,6,-6,1,5,6,2,-9,-4,8,9,4,1,5,8,-3,8],[6,-2,-5,8,7,9,-7,-4,-6,-8,-4,-6,-1,3,-7,-3,-6,9,10,-1,7,4,2,-8,2,-9,-5,9,1,7,-4,-8,5,-10,-5,5,-10,4,8,-10,-8,-9,8,-8,-10,7,-9,-4,4,-1,-4,9,-5,8,6,4,-1,-8,2,5,3,8,9,-6,6,10,-6,-8,3,-6,5,5,-2,-2,9,8,1,5,6,3,-1,-3,-3,9],[6,6,-5,7,4,-4,7,8,-6,8,-6,-5,5,5,-1,-5,-2,-10,4,4,7,4,8,3,-6,-7,3,1,-1,5,5,-1,-5,-1,10,-10,5,-10,7,-8,-6,5,-8,7,-7,3,6,-6,-7,-1,-4,4,2,-4,-9,2,-7,5,7,5,6,-3,-4,-5,-8,9,-5,3,7,8,10,-1,9,2,-10,8,-5,-10,4,3,10,-5,-5,4],[-6,9,-2,-2,-8,7,-9,6,9,-6,-1,-4,1,8,10,9,6,-1,-2,-1,7,-10,6,2,-2,-8,-9,6,4,5,7,9,6,4,-4,10,-5,-8,4,8,-2,9,-9,-9,-10,-8,-2,10,8,8,1,3,-8,-8,-3,-8,-3,6,3,-6,2,10,10,6,6,-1,-1,4,7,2,10,-7,-1,4,8,5,-5,-8,6,4,7,8,2,-9],[-8,3,5,1,-2,-9,7,2,10,-7,-5,6,-10,2,-10,3,4,-6,-5,-4,-1,9,7,-10,-3,-3,9,10,6,1,5,-4,1,7,-6,-5,5,3,-7,-1,1,9,-3,-9,-3,7,-8,6,-2,5,7,2,-4,-6,-9,3,10,2,-3,4,-3,3,-3,-1,5,10,-6,3,-1,-2,5,2,7,9,-5,5,6,-9,10,-2,8,6,8,5],[-8,10,2,9,6,-9,-2,8,6,-7,-9,-1,2,-10,-7,-10,2,8,-1,-3,-6,-7,9,-8,-5,1,-5,1,-10,-10,8,3,9,5,-10,-7,3,7,-7,6,2,-6,-10,6,1,-8,-5,10,2,-4,-6,-1,4,10,4,5,-3,-3,-9,-2,7,9,1,-8,7,-7,4,3,-5,9,-8,5,5,-2,-9,5,4,-9,-5,8,-8,6,-5,8]], dtype = "uint8")#candidate|7057|(12, 84)|const|uint8
bop_7058 = relay.mod(call_7048.astype('float32'), relay.reshape(const_7057.astype('float32'), relay.shape_of(call_7048))) # shape=(12, 84)
bop_7061 = relay.mod(call_7049.astype('float32'), relay.reshape(const_7057.astype('float32'), relay.shape_of(call_7049))) # shape=(12, 84)
output = relay.Tuple([call_7040,call_7044,bop_7058,])
output2 = relay.Tuple([call_7041,call_7045,bop_7061,])
func_7072 = relay.Function([], output)
mod['func_7072'] = func_7072
mod = relay.transform.InferType()(mod)
output = func_7072()
func_7073 = relay.Function([], output)
mutated_mod['func_7073'] = func_7073
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7142 = relay.var("var_7142", dtype = "float64", shape = (1, 11, 16))#candidate|7142|(1, 11, 16)|var|float64
uop_7143 = relay.sigmoid(var_7142.astype('float64')) # shape=(1, 11, 16)
func_1029_call = mod.get_global_var('func_1029')
func_1031_call = mutated_mod.get_global_var('func_1031')
call_7151 = func_1029_call()
call_7152 = func_1029_call()
uop_7154 = relay.sqrt(uop_7143.astype('float64')) # shape=(1, 11, 16)
func_3055_call = mod.get_global_var('func_3055')
func_3059_call = mutated_mod.get_global_var('func_3059')
const_7159 = relay.const([False,False,True,False,True,False,False,True,False,False,False,True,False,True,True,False,True,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,True,True,False,True,True,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,False,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,True,False,True,False,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,True,False,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,False,True,True,False,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,True,False,False,True,True,False,False,True,True], dtype = "bool")#candidate|7159|(832,)|const|bool
call_7158 = relay.TupleGetItem(func_3055_call(relay.reshape(const_7159.astype('bool'), [8, 8, 13]), relay.reshape(const_7159.astype('bool'), [8, 8, 13]), ), 1)
call_7160 = relay.TupleGetItem(func_3059_call(relay.reshape(const_7159.astype('bool'), [8, 8, 13]), relay.reshape(const_7159.astype('bool'), [8, 8, 13]), ), 1)
uop_7172 = relay.log10(uop_7154.astype('float64')) # shape=(1, 11, 16)
output = relay.Tuple([call_7151,call_7158,const_7159,uop_7172,])
output2 = relay.Tuple([call_7152,call_7160,const_7159,uop_7172,])
func_7174 = relay.Function([var_7142,], output)
mod['func_7174'] = func_7174
mod = relay.transform.InferType()(mod)
mutated_mod['func_7174'] = func_7174
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7175 = relay.var("var_7175", dtype = "float64", shape = (1, 11, 16))#candidate|7175|(1, 11, 16)|var|float64
func_7174_call = mutated_mod.get_global_var('func_7174')
call_7176 = func_7174_call(var_7175)
output = call_7176
func_7177 = relay.Function([var_7175], output)
mutated_mod['func_7177'] = func_7177
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5714_call = mod.get_global_var('func_5714')
func_5715_call = mutated_mod.get_global_var('func_5715')
call_7235 = relay.TupleGetItem(func_5714_call(), 0)
call_7236 = relay.TupleGetItem(func_5715_call(), 0)
func_5516_call = mod.get_global_var('func_5516')
func_5517_call = mutated_mod.get_global_var('func_5517')
call_7245 = relay.TupleGetItem(func_5516_call(), 0)
call_7246 = relay.TupleGetItem(func_5517_call(), 0)
func_4307_call = mod.get_global_var('func_4307')
func_4309_call = mutated_mod.get_global_var('func_4309')
call_7249 = func_4307_call()
call_7250 = func_4307_call()
output = relay.Tuple([call_7235,call_7245,call_7249,])
output2 = relay.Tuple([call_7236,call_7246,call_7250,])
func_7251 = relay.Function([], output)
mod['func_7251'] = func_7251
mod = relay.transform.InferType()(mod)
mutated_mod['func_7251'] = func_7251
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7251_call = mutated_mod.get_global_var('func_7251')
call_7252 = func_7251_call()
output = call_7252
func_7253 = relay.Function([], output)
mutated_mod['func_7253'] = func_7253
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5488_call = mod.get_global_var('func_5488')
func_5490_call = mutated_mod.get_global_var('func_5490')
call_7254 = func_5488_call()
call_7255 = func_5488_call()
output = call_7254
output2 = call_7255
func_7268 = relay.Function([], output)
mod['func_7268'] = func_7268
mod = relay.transform.InferType()(mod)
output = func_7268()
func_7269 = relay.Function([], output)
mutated_mod['func_7269'] = func_7269
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5292_call = mod.get_global_var('func_5292')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_7299 = func_5292_call()
call_7300 = func_5292_call()
output = relay.Tuple([call_7299,])
output2 = relay.Tuple([call_7300,])
func_7333 = relay.Function([], output)
mod['func_7333'] = func_7333
mod = relay.transform.InferType()(mod)
output = func_7333()
func_7334 = relay.Function([], output)
mutated_mod['func_7334'] = func_7334
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_7351 = relay.TupleGetItem(func_2925_call(), 1)
call_7352 = relay.TupleGetItem(func_2927_call(), 1)
output = call_7351
output2 = call_7352
func_7371 = relay.Function([], output)
mod['func_7371'] = func_7371
mod = relay.transform.InferType()(mod)
mutated_mod['func_7371'] = func_7371
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7371_call = mutated_mod.get_global_var('func_7371')
call_7372 = func_7371_call()
output = call_7372
func_7373 = relay.Function([], output)
mutated_mod['func_7373'] = func_7373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_7447 = relay.TupleGetItem(func_2467_call(), 0)
call_7448 = relay.TupleGetItem(func_2468_call(), 0)
func_4767_call = mod.get_global_var('func_4767')
func_4769_call = mutated_mod.get_global_var('func_4769')
var_7464 = relay.var("var_7464", dtype = "float32", shape = (1, 168))#candidate|7464|(1, 168)|var|float32
call_7463 = func_4767_call(relay.reshape(var_7464.astype('float32'), [7, 8, 3]))
call_7465 = func_4767_call(relay.reshape(var_7464.astype('float32'), [7, 8, 3]))
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_7469 = relay.TupleGetItem(func_1337_call(), 0)
call_7470 = relay.TupleGetItem(func_1338_call(), 0)
output = relay.Tuple([call_7447,call_7463,var_7464,call_7469,])
output2 = relay.Tuple([call_7448,call_7465,var_7464,call_7470,])
func_7479 = relay.Function([var_7464,], output)
mod['func_7479'] = func_7479
mod = relay.transform.InferType()(mod)
var_7480 = relay.var("var_7480", dtype = "float32", shape = (1, 168))#candidate|7480|(1, 168)|var|float32
output = func_7479(var_7480)
func_7481 = relay.Function([var_7480], output)
mutated_mod['func_7481'] = func_7481
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2455_call = mod.get_global_var('func_2455')
func_2456_call = mutated_mod.get_global_var('func_2456')
call_7493 = relay.TupleGetItem(func_2455_call(), 0)
call_7494 = relay.TupleGetItem(func_2456_call(), 0)
func_5840_call = mod.get_global_var('func_5840')
func_5844_call = mutated_mod.get_global_var('func_5844')
const_7500 = relay.const([5,-7,6,-9,-10,3,8,2,-7,-5,-3,10,10,-4,6,-9,9,-9,-3,-2,-7,-9,-5,6,-5,-8,6,6,-4,5,4,-2,7,9,-8,-4,-8,-1,-4,-4,7,-9,9,-1,4,4,-9,4,-6,7,-6,10,-4,6,7,8,3,9,1,-7,-9,4,5,-5,10,6,2,9,-8,-5,4,-3,1,9,5,8,6,1,1,-4,-9,-7,8,-9,1,-5,7,2,-9,9,-6,5,10,-3,3,2,-8,5,4,-4,5,-2,7,-10,6,10,8,-5,-5,-9,-8,10,-9,3,8,2,9,8,7,-4,-7,6,2,-4,-2,5,4,-5,10,-10,-9,2,4,6,9,-6,-4,4,6,5,10,7,5,1,-1,-6,3,8,9,1,-2,4,1,-6,-5,4,-10,3,2,3,-5,2,6,-7,2,2,-5,1,-6,3,-7,1,6,5,10,-9,-6,4,1,-10,7,8,-10,-10,-8,-10,-9,-2,-4,3,4,8,-5,5,-2,-10,7,-5,-6,3,-7,9,-3,1,8,1,5,6,-4,7,-6,-6,-4,-9,-5,6,-7,-8,-6,8,-2,-9,-10,9,6,9,3,-6,-8,7,9,-5,-8,5,-1,-9,-3,2,-3,-7,-8,-10,4,8,-1,3,-8,-6,-1,-2,5,-7,-2,-4,-1,4,9,-8,2,-5,1,-4,-8,7,3,-4,-1,-9,-10,-7,-3,-10,-7,-7,4,-3,-2,4,-7,-1,-10,-9,6,5,-10,-8,-7,9,-7,-4,-6,6,4,-8,-2,-3,4,7,-1,-9,-9,8,-5,10,1,5,-1,-7,-2,9,-6,8,4,1,10,-8,8,4,1,7,8,-1,-4,7,7,-2,8,-2,-7,-8,6,-5,2,-10,-3,-6,1,-9,10,-1,-2,8,2,10,5,-6,6,5,-3,2,4,-7,9,-9,2,4,2,-1,3,6,3,-1,5,8,3,-6,-2,-1,10,10,4,7,-7,10,2,-10,-10,-6,6,-5,-8,3,5,-2,8,9,5,7,4,2,3,-3,-10,8,-6,5,5,3,4,6,-7,-3,9,-4,7,-1,9,-5,-6,5,7,4,-7,-3,4,2,-4,-4,3,8,-6,-2,4,4,-10,1,-10,-1,-4,8,4,9,-7,1,-3,-1,9,-5,-1,-4,-9,-8,10,6,4,1,-7,5,3,5,-6,-6,10,-9,-10,1,8,10,9,-1,1,-10,-2,2,1,-5,4,2,-3,-6,-6,6,-6,-1,10,9,-7,10,2,-7,1,-7,-3,8,2,3,-1,-9,3,4,-5,9,-2,1,2,6,-2,-6,-4,3,10,-1,4,10,3,5,8,9,-2,3,-10,7,2,9,10,9,9,-1,-1,4,-6,1,2,2,-2,-10,-2,6,-2,9,8,-4,-9,2,7,-3,7,-4,5,5,-3,-2,1,10,-3,-5,-8,-10,3,8,-9,10,-6,-5,2,-8,4,-1,-8,-8,9,-3,-10,5,-4,1,3,-1,8,10,7,-7,8,8,9,10,-7,7,8,3,3,7,-7,-5,-6,7,2,4,1,9,-8,-8,-4,4,-4,-3,-3,5,1,-7,4,8,-9,8,-6,10,8,9,-10,1,2,-3,6,-6,-9,-2,8,-10,6,-5,-7,-4,-2,4,-10,7,10,-8,7,5,-7,-8,-9,-2,-6,-7,3,-7,-8,6,-7,9,-3,6,-1,6,10,-4,2,-5,-4,-3,-6,1,-3,-10,-2,-10,8,-4,10,8,6,8,10,8,6,3,4,-5,-3,-9,-6,9,-8,-4,5,-8,-5,-10,-2,1,2,1,7,4,1,-4,-4,-10,8,-3,-7,5,-7,-7,5,-8,-1,2,-5,8,2,2,5,-10,-7,7,2,-5,6,10,1,8,-5,10,9,-5,-1,6,-10,-10,-9,-2,-10,-2,1,10,9,6,8,-5,5,7,8,2,4,-8,1,-6,7,7,-1,9,-5,-8,-2,-2,-5,-3,-6,3,-6,-3,-1,8,-8,-7,2,-2,3,-1,-3,10,-4,10,-7,-10,-6,-2,3,-6,-4,3,-8,-4,3,6,8,1,-8,-4,4,9,-6,-8,8,-1,6,10,-6,-7,-8,4,-8,10,8,2,-7,-3,-10,3,4,2,-7,-3,7,-2,2,2,3,-7,-7,2,-8,6,-5,-9,2,-8,-4,-2,3,-7,-1,7,3,6,3,-4,4,-10,-9,-9,-2,10,2,-8,-5,3,4,-4,4,-6,10,7,-10,-5,7,9,-5,-5,8,-5,8,3,-8,10,-8,8,-8,2,-3,6,4,-9,-2,-9,8,7,10,10,8,-9,-8,-2,1,4,-4,-1,-8,9,-7,-2,2,2,1,9,4,4,4,-8,-4,6,7,-6,10,-4,-6,1,-10,-10,-7,-10,7,-2,-2,8,5,1,3,-6,5,-9,8,8,3,9,-7,8,3,-6,10,-8,-8,-6,8,-4,-4,7,3,10,-3,5,-7,3], dtype = "uint32")#candidate|7500|(936,)|const|uint32
call_7499 = relay.TupleGetItem(func_5840_call(relay.reshape(const_7500.astype('uint32'), [13, 6, 12]), relay.reshape(const_7500.astype('uint32'), [13, 6, 12]), ), 0)
call_7501 = relay.TupleGetItem(func_5844_call(relay.reshape(const_7500.astype('uint32'), [13, 6, 12]), relay.reshape(const_7500.astype('uint32'), [13, 6, 12]), ), 0)
func_1888_call = mod.get_global_var('func_1888')
func_1889_call = mutated_mod.get_global_var('func_1889')
call_7509 = relay.TupleGetItem(func_1888_call(), 0)
call_7510 = relay.TupleGetItem(func_1889_call(), 0)
output = relay.Tuple([call_7493,call_7499,const_7500,call_7509,])
output2 = relay.Tuple([call_7494,call_7501,const_7500,call_7510,])
func_7515 = relay.Function([], output)
mod['func_7515'] = func_7515
mod = relay.transform.InferType()(mod)
output = func_7515()
func_7516 = relay.Function([], output)
mutated_mod['func_7516'] = func_7516
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7521 = relay.var("var_7521", dtype = "float64", shape = (10, 11, 6))#candidate|7521|(10, 11, 6)|var|float64
uop_7522 = relay.cos(var_7521.astype('float64')) # shape=(10, 11, 6)
output = relay.Tuple([uop_7522,])
output2 = relay.Tuple([uop_7522,])
func_7530 = relay.Function([var_7521,], output)
mod['func_7530'] = func_7530
mod = relay.transform.InferType()(mod)
var_7531 = relay.var("var_7531", dtype = "float64", shape = (10, 11, 6))#candidate|7531|(10, 11, 6)|var|float64
output = func_7530(var_7531)
func_7532 = relay.Function([var_7531], output)
mutated_mod['func_7532'] = func_7532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7251_call = mod.get_global_var('func_7251')
func_7253_call = mutated_mod.get_global_var('func_7253')
call_7555 = relay.TupleGetItem(func_7251_call(), 1)
call_7556 = relay.TupleGetItem(func_7253_call(), 1)
func_6350_call = mod.get_global_var('func_6350')
func_6352_call = mutated_mod.get_global_var('func_6352')
call_7562 = func_6350_call()
call_7563 = func_6350_call()
output = relay.Tuple([call_7555,call_7562,])
output2 = relay.Tuple([call_7556,call_7563,])
func_7564 = relay.Function([], output)
mod['func_7564'] = func_7564
mod = relay.transform.InferType()(mod)
output = func_7564()
func_7565 = relay.Function([], output)
mutated_mod['func_7565'] = func_7565
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4057_call = mod.get_global_var('func_4057')
func_4059_call = mutated_mod.get_global_var('func_4059')
call_7566 = relay.TupleGetItem(func_4057_call(), 0)
call_7567 = relay.TupleGetItem(func_4059_call(), 0)
output = relay.Tuple([call_7566,])
output2 = relay.Tuple([call_7567,])
func_7569 = relay.Function([], output)
mod['func_7569'] = func_7569
mod = relay.transform.InferType()(mod)
output = func_7569()
func_7570 = relay.Function([], output)
mutated_mod['func_7570'] = func_7570
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7588 = relay.var("var_7588", dtype = "float32", shape = ())#candidate|7588|()|var|float32
var_7589 = relay.var("var_7589", dtype = "float32", shape = (7, 13, 11))#candidate|7589|(7, 13, 11)|var|float32
bop_7590 = relay.divide(var_7588.astype('float32'), var_7589.astype('float32')) # shape=(7, 13, 11)
func_2273_call = mod.get_global_var('func_2273')
func_2275_call = mutated_mod.get_global_var('func_2275')
call_7599 = func_2273_call()
call_7600 = func_2273_call()
func_7530_call = mod.get_global_var('func_7530')
func_7532_call = mutated_mod.get_global_var('func_7532')
const_7631 = relay.const([-0.663167,-7.102388,6.711093,2.046301,-5.056146,4.267529,8.058478,1.387122,4.953363,-5.399470,-9.748070,9.993770,-2.005329,-1.771148,-3.728165,-7.288595,7.120489,3.754688,0.384298,7.023087,-2.419717,5.234269,0.272623,-0.710180,7.038232,-0.797324,6.939864,-9.022018,3.110949,-4.200723,-6.753900,-3.853789,6.909228,7.982605,-8.469055,-0.876386,8.606231,5.107271,-4.669263,5.856734,-5.877679,8.911276,-6.466695,0.126824,-7.568893,6.729085,-8.113775,-7.386033,5.414822,4.536562,1.808582,9.873120,4.174713,2.991574,-1.767347,7.719955,5.538903,4.743886,-5.624631,8.561941,-5.948995,-1.983608,-9.673084,-9.109141,-9.401883,-9.635198,3.560623,-5.318206,-7.254521,-4.627105,2.349927,7.928263,-5.805222,-5.601201,3.158806,-1.176986,-8.258089,4.275712,1.851579,6.631453,1.575511,4.863986,6.387809,8.619495,-0.912448,-5.248478,2.736370,-2.334147,-7.142918,-3.287560,-7.732291,5.209416,7.849556,7.867199,-6.668550,-8.690993,-8.042291,-3.409314,-8.821276,0.307931,3.439877,-1.239215,6.038791,9.891179,5.521796,-7.418622,-6.521305,-1.380437,-6.974851,-6.372654,-3.886105,-1.520314,1.803012,-3.785514,-9.010435,-5.882035,-2.944312,-2.717434,5.098248,8.000560,7.581446,-7.441718,-0.644214,-7.550765,-4.741901,8.734092,0.500532,-5.070603,4.942715,-0.417592,-1.915422,3.770941,2.529247,1.449611,4.185414,4.436708,-2.732621,-1.839376,7.753100,1.569147,-1.427199,-6.402054,-0.239894,-5.847846,-0.946574,2.230774,9.585181,6.422690,-3.549546,7.905793,7.023173,-4.416503,-0.039544,-1.410010,7.398585,1.321907,5.699728,-1.334000,-4.190614,5.212644,9.712588,-3.255625,5.837029,-2.773188,-7.320036,-6.314238,-6.261141,6.190518,4.120303,-7.996412,5.066150,-9.030670,-6.534794,-7.228981,7.942704,5.498687,-6.172471,6.064639,3.189235,6.886751,2.007681,4.209694,-0.570120,-7.405976,6.795010,5.249475,6.915536,6.007420,-0.766005,-3.944863,3.221803,-3.644945,4.602075,2.125535,7.786418,-2.872936,-3.536094,5.482437,-0.026506,5.750321,-5.779607,-0.791465,-3.725986,9.519065,1.413449,1.382144,7.417648,-2.494616,4.094609,7.598900,-6.681196,-7.206395,-8.207764,-1.140274,0.417077,-5.686886,-5.171226,0.155556,-2.746897,0.782262,5.492931,-7.469233,-3.977500,1.569323,-1.671824,4.830499,1.934066,-0.514348,4.300733,-7.070845,-5.360143,-6.541113,-2.167410,7.402308,5.758449,-2.345006,1.795077,0.321650,-6.404540,-0.848481,-3.103066,9.874142,2.936158,6.400816,-8.337882,7.387424,-1.413169,6.474583,-6.078944,2.566374,4.625401,-9.403493,-0.555540,4.910945,-9.113604,6.761395,0.949214,-1.469318,-9.777544,3.236612,-6.480703,4.112504,-9.686225,6.879570,-6.812255,-0.208893,-4.170411,-3.308982,6.283212,0.566381,8.652146,-3.434837,-3.120517,6.627076,-4.439457,8.363982,-8.232551,6.474261,-9.570649,6.538838,6.953468,-1.921870,-2.711841,-1.425426,-7.063994,1.689072,-4.282382,-0.842592,5.577842,-9.359359,-0.511956,-4.283093,-3.076119,-9.898242,-0.379567,7.373936,8.005377,6.488978,0.066130,4.615714,-5.634092,7.870189,-6.516106,6.017135,-2.971909,0.338601,0.275079,2.081290,5.371655,-6.588662,1.627279,3.202923,-3.773139,-7.994403,-0.022787,2.924153,-3.241986,-8.499655,3.692315,-8.199429,0.913452,-0.777213,7.153943,-9.205598,9.399978,-6.049706,7.495345,-3.693820,6.784249,0.649549,-0.648109,-0.590748,2.151343,-7.575732,-8.640317,-5.527096,-9.934141,-9.437274,-8.612659,4.612645,-7.171631,-9.507348,4.207983,5.482542,8.897013,6.987850,6.356678,5.789368,-5.152474,0.703079,-1.863083,-4.837807,3.770328,6.301428,0.208795,2.263437,-2.008255,1.626645,-8.578827,-9.003620,0.024072,-6.616926,3.524643,-9.732697,9.745728,-0.140985,3.573912,-2.398025,-8.868297,5.363939,-3.658050,0.154831,-9.556030,4.453542,6.088279,0.503774,8.597364,7.672558,9.795351,-1.818016,-2.453998,-0.804842,9.596280,-5.736867,-8.239937,4.370024,-7.235497,-9.659684,-0.451616,-7.951246,2.560608,-1.196183,4.854672,-0.455706,3.492056,5.541833,6.842799,-9.813401,-2.133974,-1.590005,-9.177843,-2.644083,-9.403003,0.651155,-8.204910,-8.188568,2.936570,-6.657218,8.639573,3.622821,1.386987,-8.629674,1.879317,5.471631,2.097790,-1.590779,1.552078,-2.274318,4.888943,-8.194070,6.799709,-0.701952,-5.811029,8.374670,4.374132,-3.178911,2.417135,0.216331,7.858196,3.090581,0.799308,-5.509944,-8.386500,-1.357777,3.728089,1.322671,-5.506440,0.276394,-9.115647,-7.418317,-5.952907,-8.493072,6.323751,-8.099485,-3.294253,3.930264,0.477165,-9.048359,-6.678577,-9.993069,-0.580100,9.181568,0.363854,3.574436,0.403169,3.239999,-3.317178,-8.813543,9.585398,6.056919,-5.672682,3.536936,-2.281791,2.947239,0.308127,-5.886188,2.914409,-1.514974,6.760234,-3.920986,6.371594,-0.798198,3.059262,4.716527,5.481391,-0.281301,5.604710,5.817512,9.889434,-7.750026,-6.288418,-0.319424,-1.788560,-8.288397,-3.107604,2.251197,-2.533256,-8.949667,-5.008079,6.702171,-5.773635,0.968343,9.213749,9.986414,0.668523,3.762570,1.753645,3.724304,-0.594801,4.225793,-2.954623,-2.523061,-9.948395,-0.980661,-1.207114,-6.383665,2.430475,-3.327922,-5.500896,6.460072,-2.088449,-7.982927,5.003985,6.890528,2.193126,-9.147707,5.796184,1.984983,9.386574,-9.585820,7.910032,-2.441773,-8.499990,7.944557,6.100605,-3.991727,-7.620992,0.967944,-7.607243,7.155566,8.420392,1.785252,8.266343,-7.970447,-8.087769,-5.687326,7.878896,-1.711732,-1.670795,-2.949752,5.136716,7.337794,0.453503,3.388931,7.553820,-0.600033,-6.511381,-1.031363,-0.611630,8.067324,3.015178,-3.860263,-6.362210,7.563386,-5.511373,-5.616202,-5.873017,6.857606,-6.625779,-1.681039,-1.431766,-0.121512,-9.233535,-2.290513,2.846873,-8.313855,8.106585,1.250287,7.272471,-2.397833,6.906008,9.650701,-4.854627,0.583361,9.792700,9.949883,-2.340428,5.645295,-6.193942,3.691535,6.452088,-6.413407,-9.322687,-3.786024,-0.064007,-8.715300,-9.148549,-2.238275,-0.775206,2.501786,9.722357,5.346321,1.867836,-6.220189,-0.214022,7.586208,5.527542,8.638215,-5.965089,-8.103787,-4.463214,-0.156065,-0.122499,-8.962054,-4.843954,7.549023,-2.746966,-5.028757,3.150188,2.410368,-0.636856,5.368291,-6.827280,-0.167227,-9.177137,-7.638960,7.079571,8.191585,0.747003,-6.881633,-2.408655,2.863567,5.313970,-6.475131,-8.585922,-9.976298,-1.518587,4.801576,-0.314877,0.632733,-7.378735,-5.016003,-3.246845,9.025904,9.502753,-1.395550,7.006988,-3.469144,2.117153,6.693851,-5.652680,-6.079033,5.751389,9.425570,6.315618,2.530256,-4.463157,4.934760,7.609980,-0.245453,1.084437,-2.924689,-8.390665,7.120017,2.412846,-9.402818,-3.555029,4.296913,-0.510830,-5.650472], dtype = "float64")#candidate|7631|(660,)|const|float64
call_7630 = relay.TupleGetItem(func_7530_call(relay.reshape(const_7631.astype('float64'), [10, 11, 6])), 0)
call_7632 = relay.TupleGetItem(func_7532_call(relay.reshape(const_7631.astype('float64'), [10, 11, 6])), 0)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_7641 = relay.TupleGetItem(func_3252_call(), 0)
call_7642 = relay.TupleGetItem(func_3254_call(), 0)
output = relay.Tuple([bop_7590,call_7599,call_7630,const_7631,call_7641,])
output2 = relay.Tuple([bop_7590,call_7600,call_7632,const_7631,call_7642,])
func_7645 = relay.Function([var_7588,var_7589,], output)
mod['func_7645'] = func_7645
mod = relay.transform.InferType()(mod)
var_7646 = relay.var("var_7646", dtype = "float32", shape = ())#candidate|7646|()|var|float32
var_7647 = relay.var("var_7647", dtype = "float32", shape = (7, 13, 11))#candidate|7647|(7, 13, 11)|var|float32
output = func_7645(var_7646,var_7647,)
func_7648 = relay.Function([var_7646,var_7647,], output)
mutated_mod['func_7648'] = func_7648
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7675 = relay.var("var_7675", dtype = "float32", shape = (8, 8, 7))#candidate|7675|(8, 8, 7)|var|float32
uop_7676 = relay.asin(var_7675.astype('float32')) # shape=(8, 8, 7)
func_952_call = mod.get_global_var('func_952')
func_954_call = mutated_mod.get_global_var('func_954')
call_7690 = relay.TupleGetItem(func_952_call(), 0)
call_7691 = relay.TupleGetItem(func_954_call(), 0)
output = relay.Tuple([uop_7676,call_7690,])
output2 = relay.Tuple([uop_7676,call_7691,])
func_7696 = relay.Function([var_7675,], output)
mod['func_7696'] = func_7696
mod = relay.transform.InferType()(mod)
var_7697 = relay.var("var_7697", dtype = "float32", shape = (8, 8, 7))#candidate|7697|(8, 8, 7)|var|float32
output = func_7696(var_7697)
func_7698 = relay.Function([var_7697], output)
mutated_mod['func_7698'] = func_7698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6350_call = mod.get_global_var('func_6350')
func_6352_call = mutated_mod.get_global_var('func_6352')
call_7748 = func_6350_call()
call_7749 = func_6350_call()
output = relay.Tuple([call_7748,])
output2 = relay.Tuple([call_7749,])
func_7758 = relay.Function([], output)
mod['func_7758'] = func_7758
mod = relay.transform.InferType()(mod)
output = func_7758()
func_7759 = relay.Function([], output)
mutated_mod['func_7759'] = func_7759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4307_call = mod.get_global_var('func_4307')
func_4309_call = mutated_mod.get_global_var('func_4309')
call_7808 = func_4307_call()
call_7809 = func_4307_call()
func_2024_call = mod.get_global_var('func_2024')
func_2026_call = mutated_mod.get_global_var('func_2026')
call_7819 = func_2024_call()
call_7820 = func_2024_call()
func_2578_call = mod.get_global_var('func_2578')
func_2581_call = mutated_mod.get_global_var('func_2581')
var_7825 = relay.var("var_7825", dtype = "float64", shape = (15,))#candidate|7825|(15,)|var|float64
const_7826 = relay.const([-6,9,9,8,8,-6,-1,5,-10,4,7,9,1,2,7,9,8,3,-4,9,1,7,10,1,-9,7,-9,9,6,-3,9,-8,-10,6,4,-7,1,-6,8,-3,10,-6,8,1,9,7,-6,2,-6,3,4,-4,4,7,7,10,2,8,-3,6,-3,-7,7,-8,-10,4,8,2,-10,-5,-1,-6,-3,4,3,6,-2,6,4,6,-2,-9,-10,6,10,-7,-8,-5,-7,-5,-1,-8,-5,4,-8,-3,-1,-3,-3,-1,10,-5,2,9,9,2,6,4,-4,-1,9,3,8,2,-6,-6,2,-5,1,6,8,9,7,7,2,-2,-4,4,2,7,9,-4,-7,7,-3,-8,-2,6,2,1,-3,-8,9,-1,8,-8,-3,9,-9,10,1,4,-6,-3,4,-6,-8,-4,-6,7,-6,10,5,-9,-8,-10,-6,-2,-5,-3,-10,7,-3,4,-9,5,8,-5,7,-9,5,-5,4,-5,4,-1,9,2,-3,3,-9,-7,4,-2,-6,-5,2,3,-7,6,-8,-6,7,1,6,1,-10,4,8,4,-7,-8,1,5,-10,1,-10,-7,7,-4,-9,10,-3,5,2,-9,10,-8,-9,-1,5,-8,-1,9,-2,10,-10,-3,9,-6,7,10,3,10,-10,-2,3,10,-5,-1,-4,8,-5,8,-7,3,-10,-3,10,4,4,-6,5,2,-5,-7,-6,-2,4,-3,4,6,8,6,3,-9,-7,-6,1,2,-1,-6,4,9,9,8,9,-7,1,6,-7,-1,-10,-7,-4,-10,10,5,-3,1,-6,5,-2,2,-10,-9,3,-1,8,-5,-9,-9,-10,-2,-9,-7,1,-8,-6,8,9,3,7,5,4,-8,-7,-1,-3,10,-7,7,-8,-10,-5,10,-6,-4,-9,-8,10,-3,3,2,8,-8,-8,2,9,-2,-10,8], dtype = "int8")#candidate|7826|(352,)|const|int8
call_7824 = relay.TupleGetItem(func_2578_call(relay.reshape(var_7825.astype('float64'), [15, 1, 1]), relay.reshape(const_7826.astype('int8'), [8, 44]), ), 1)
call_7827 = relay.TupleGetItem(func_2581_call(relay.reshape(var_7825.astype('float64'), [15, 1, 1]), relay.reshape(const_7826.astype('int8'), [8, 44]), ), 1)
func_6694_call = mod.get_global_var('func_6694')
func_6696_call = mutated_mod.get_global_var('func_6696')
const_7833 = relay.const([-2,10,3,-8,4,7,-4,10,-9,-7,5,3,-6,-1,-1,8,-9,-7,-2,7,7,-2,10,-2,2,-10,-5,-5,3,-7,6,10,-6,10,-2,-6,10,9,1,-7,-1,1,9,-10,10,5,-3,-3,-1,-8,7,-3,-1,7,4,-6,2,-4,3,-1,1,1,2,4,-5,8,4,1,6,9,3,-6,3,3,-5,-3,10,-10,-5,8,7,-6,-1,-6,6,-6,1,3,3,-3,10,-3,-7,-7,-9,6,2,7,-10,10,-10,-4,-8,6,3,-10,-5,-7,9,-7,-8,-4,-5,-4,4,1,-10,-7,-2,-2,4,9,-6,-2,-8,-1,1,7,-6,1,4,-6,-6,3,-5,4,6,9,-10,6,7,4,-5,-6,-1,1,-8,2,-9,4,1,-5,1,-10,2,-9,-5,9,-4,-1,1,-2,10,-4,8,-4,6,-5,-3,8,-9,8,-9,-4,-3,8,8,4,-4,8,8,1,3,-3,-9,4,7,3,-1,9,-1,-10,8,6,2,-4,-8,-4,-10,-7,-7,8,5,10,-8,9,-9,-10,-3,-1,-2,5,9,-1,8,10,1,9,-9,1,1,9,-1,7,9,10,2,-3,7,-1,-4,-10,7,8,-10,5,10,-9,5,6,-3,-7,-2,-5,-6,5,7,4,3,-2,-2,-4,1,3,9,-1,-6,7,-1,-8,-9,7,-6,-2,3,-4,10,-7,-1,-8,2,5,8,-5,-2,-5,5,9,-1,4,4,6,6,-7,-6,1,4,7,6,2,6,-1,7,4,-2,1,6,1,3,-1,5,-10,-6,3,-8,1,2,6,-5,-9,-7,-2,10,-7,3,5,-9,-9,1,-8,6,-2,3,-2,-8,-5,3,-10,-3,7,4,-6,-6,-10,6,5,-7,-2,7,-9,5,4,3,1,10,6,2,8,6,7,4,-5,3,1,3,6,6,-8,-3,-7,-8,10,-4,8,-6,1,8,-3,5,-2,-6,6,8,2,-2,-8,-1,-8,7,-4,-2,-3,1,3,9,-4,-4,8,-4,-5,9,-5,-4,-3,3,-3,2,-7,-1,-1,-6,7,5,3,-6,-6,-4,3,-7,6,-6,5,7,3,4,10,8,1,-3,-3,-3,-1,-1,4,1,-8,-10,-4,-4,-5,-2,-10,10,-6,-4,-1,-9,5,-7,9,-10,6,7,7,9,-2,6,-3,-3,-1,-7,5,5,7,-8,9,-3,-8,-6,-4,6,6,-9,-8,8,-1,-10,-3,6,-4,-8,2,9,-4,4,10,5,10,6,8,7,-1,8,1,-7,10,-9,9,-2,-3,-10,-6,8,10,-6,-10,-2,10,-6,-3,8,-10,-6,5,9,-6,-10,5,2,3,-8,3,-3,-9,5,-4,5,-10,-1,9,-2,1,7,1,3,-9,7,8,-4,1,-9,10,8,-3,4,3,8,9,9,-5,6,-3,6,6,-8,-9,3,1,9,4,-7,-1,-10,10,-4,4,-1,-4,-8,-6,7,-3,5,2,9,9,-3,-1,-5,-4,10,-9,-5,-9,-3,-9,-10,-1,-6,3,10,-1,4,-8,7,-8,-2,-9,9,-9,-4,-5,1,-3,10,2,8,3,-9,1,-4,2,-3,4,10,-6,-2,-3,6,1,10,6,-9,9,1,-2,6,-1,-9,-3,-10,5,10,6,4,2,1,1,6,-7,-8,3,5,7,1,-4,10,3,-9,-8,6,-4,-9,-6,5,-3,2,-8,-10,-2,-4,-9,8,-6,1,-8,3,4,7,6,-3,4,5,-2,-9,-3,3,-7,6,-5,-7,-3,-5,4,-7,5,-1,5,2,-8,-4,-4,-5,-7,6,7,5,6,7,3,2,5,-8,7,10,3,-8,-2,-9,3,10,-1,-10,-6,-10,-2,-8,6,-9,-8,-10,-6,7,1,-8,-5,4,3,4,-4,10,-7,-5,4,5,5,-10,-2,-9,-7,9,5,-8,9,10,6,-9,8,-5,-8,-2,-6,3,1,2,1,10,7,8,9,9,-10,10,4,10,-8,6,7,1,-5,8,4,-6,5,7,2,1,8,-9,9,-6,-2,-8,-6,-8,1,9,-1,6,-8,10,-1,-1,-4,-1,10,9,-2,2,7,-8,-4,-6,3,1,-5,1,-3,4,3,-10,3,-4,6,2,3,-4,9,2,-1,3,-5,3,5,3,5,10,3,-2,9,4,5,1,-7,-6,-9,6,3,9,-1,5,-8,-5,-10,-9,2,-3,3,-1,-10,-3,-7,-10,-10,-8,3,-8,-2,-1,-1,-1,8,-10,-9,-3,9,5,-5,-6,-6,-8,2,2,-9,6,7,-3,-9,-6,-7,7,-5,3,7,-6,6,4,10,-3,10,10,-5,10,9,4,5,1,-2,-9,-4,4,9,-9,3,-9,-3,2,-4,-4,10,-7,9,-4,-10,2,10,-5,5,9,8,-2,-6,1,-7,-1,2,2,5,4,3,-3,-3,3,2,5,7,-5,2,-3,10,7,-3,3,7,7,-5,-4,-9,-6,6,-3,1,-9,3,-5,7,4,1,10,-7,9,-9,2,-7,-9,10,-9,1,5,10,-6,9,9,-9,9,7,-10,8,-4,-8,1,6,-10,-8,10,2,6,-8,-3,-3,-5,-8,-7,-6,-3,-4,6,-4,7,-1,1,7,-5,4,3,10,-8,-6,-5,7,-9,-2,-3,1,-10,10,-6,-1,-3,-10,-2,8,-7,8], dtype = "int64")#candidate|7833|(1014,)|const|int64
call_7832 = func_6694_call(relay.reshape(const_7833.astype('int64'), [6, 13, 13]))
call_7834 = func_6694_call(relay.reshape(const_7833.astype('int64'), [6, 13, 13]))
output = relay.Tuple([call_7808,call_7819,call_7824,var_7825,const_7826,call_7832,const_7833,])
output2 = relay.Tuple([call_7809,call_7820,call_7827,var_7825,const_7826,call_7834,const_7833,])
func_7850 = relay.Function([var_7825,], output)
mod['func_7850'] = func_7850
mod = relay.transform.InferType()(mod)
var_7851 = relay.var("var_7851", dtype = "float64", shape = (15,))#candidate|7851|(15,)|var|float64
output = func_7850(var_7851)
func_7852 = relay.Function([var_7851], output)
mutated_mod['func_7852'] = func_7852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3252_call = mod.get_global_var('func_3252')
func_3254_call = mutated_mod.get_global_var('func_3254')
call_7857 = relay.TupleGetItem(func_3252_call(), 0)
call_7858 = relay.TupleGetItem(func_3254_call(), 0)
output = relay.Tuple([call_7857,])
output2 = relay.Tuple([call_7858,])
func_7866 = relay.Function([], output)
mod['func_7866'] = func_7866
mod = relay.transform.InferType()(mod)
mutated_mod['func_7866'] = func_7866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7866_call = mutated_mod.get_global_var('func_7866')
call_7867 = func_7866_call()
output = call_7867
func_7868 = relay.Function([], output)
mutated_mod['func_7868'] = func_7868
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4222_call = mod.get_global_var('func_4222')
func_4223_call = mutated_mod.get_global_var('func_4223')
call_7878 = relay.TupleGetItem(func_4222_call(), 0)
call_7879 = relay.TupleGetItem(func_4223_call(), 0)
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_7880 = func_3322_call()
call_7881 = func_3322_call()
func_5747_call = mod.get_global_var('func_5747')
func_5750_call = mutated_mod.get_global_var('func_5750')
call_7890 = relay.TupleGetItem(func_5747_call(relay.reshape(call_7880.astype('float64'), [2, 12, 9])), 0)
call_7891 = relay.TupleGetItem(func_5750_call(relay.reshape(call_7880.astype('float64'), [2, 12, 9])), 0)
output = relay.Tuple([call_7878,call_7880,call_7890,])
output2 = relay.Tuple([call_7879,call_7881,call_7891,])
func_7917 = relay.Function([], output)
mod['func_7917'] = func_7917
mod = relay.transform.InferType()(mod)
mutated_mod['func_7917'] = func_7917
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7917_call = mutated_mod.get_global_var('func_7917')
call_7918 = func_7917_call()
output = call_7918
func_7919 = relay.Function([], output)
mutated_mod['func_7919'] = func_7919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3953_call = mod.get_global_var('func_3953')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_7935 = relay.TupleGetItem(func_3953_call(), 1)
call_7936 = relay.TupleGetItem(func_3954_call(), 1)
func_2665_call = mod.get_global_var('func_2665')
func_2667_call = mutated_mod.get_global_var('func_2667')
const_7954 = relay.const([-4.373463,-3.592573,-0.749623,-1.368075,6.897167,-1.668524,-8.677337,8.195188,4.735731,2.580617,0.289262,-3.402970,3.780198,-8.393386,6.600026,-9.046970,0.348385,-0.683676,-0.465243,0.152621,-7.862747,7.338749,3.613720,8.545340,4.656839,3.580457,6.383500,-5.239592,-9.858242,1.689830,-3.819453,-2.102609,3.605901,-3.494044,9.151703,7.614400,2.761037,-6.241961,9.807765,7.860015,-1.529083,9.666556,-8.998085,-7.987850,1.702630,6.194910,0.850856,0.571767,-2.598617,-2.515461,8.262774,5.417088,-4.824486,-6.424625,1.209038,-8.055779,-2.061789,3.863584,-4.558476,-5.572939,-2.373871,0.008587,9.805929,-0.997418,-6.783148,0.640786,-5.072236,6.309393,-0.446112,-9.528476,8.747100,-1.920746,-1.770304,9.557682,6.600636,-8.878849,5.589131,-8.618529,-8.353339,-9.888933,2.538838,0.026850,-9.033954,9.217637,-5.178193,-6.293086,-4.477852,9.210053,-6.218996,0.125520,-9.728471,8.361033,-6.335117,-9.925407,-2.508546,3.314398,-9.518515,4.748311,0.574253,-7.639912,-7.493124,-0.850790,5.593096,-8.778001,-4.905923,1.126159,8.870406,-5.748934,-5.280090,6.974783,5.052413,1.587515,4.306540,-0.375833,0.275691,-3.559889,4.340029,-4.404137,-7.572074,-0.040751,5.845067,-6.590612,2.017270,-2.368230,5.124586,-3.763967,-9.552675,8.374986,0.606685,8.322041,-0.925003,-9.372490,-1.243382,-4.828194,6.890148,0.210517,-3.627693,-3.748217,-2.738154,-3.666943,-2.740966,-8.402863,-1.500801,-3.011745,7.132373,-0.954815,3.860837,6.122508,1.934897,-3.383283,-8.606165,2.524812,4.130050,-1.768367,-4.654243,-2.805178,-1.239652,-5.689024,-2.498731,-0.838601,-2.683270,5.843260,1.938636,3.265183,-0.889308,-4.480480,4.760091,0.718324,6.287298,-3.699537,-2.449774,-7.054901,9.548052,4.234481,0.339211,8.156068,-4.978803,7.826276,6.559890,1.933433,-6.914186,-3.269494,2.790466,3.828621,-2.585155,9.665031,-0.131671,9.738918,-6.850623,4.486220,-0.055253,4.780687,4.717754,-9.179228,5.193543,-9.237430,6.227785,0.373731,-4.571582,4.917031,-7.213711,-6.425776,-0.356511,-3.670958,-0.414071,-8.315674,-1.517718,-4.449881,-8.549073,-8.320811,-0.933406,-2.541070,3.023735,-5.910305,-7.539248,-7.455099,-6.828462,9.806167,-5.869058,7.299870,3.742486,3.880926,4.055712,1.945997,6.750965,5.856880,-3.103443,0.623374,2.452291,7.673146,-8.284255,-1.902743,-0.625682,8.899420,3.695848,-8.257838,2.811126,-9.870392,3.858586,-6.935082,0.222657,-0.961847,3.149482,-4.964347,6.826298,-7.264185,1.145943,7.807793,-8.122308,0.025082,7.563311,-3.788669,1.595169,-1.832866,-8.793821,2.275251,-3.596130,1.126760,-5.081566,5.549721,-0.685661,8.639424,-2.691201,8.155810,6.787526,6.552288,-3.974062,7.339444,-7.464289,-6.046596,5.343780,1.014254,0.372385,0.651672,-7.651301,-1.011040,2.038541,-7.542697,-3.169994,-1.460031,-7.990602,-1.277936,-8.842883,2.051610,4.762153,9.881021,8.529753,7.852093,-9.925649,-7.210581,5.832864,3.198878,-2.124746,-8.109710,2.829759,5.339498,-8.982536,4.623348,6.237595,-3.307365,-5.287379,3.690892,-4.834658,8.468419,-7.115422,4.342575,-6.350562,-6.167836,-6.514177,8.347928,5.472852,-3.964905,-3.465566,-8.727226,-6.263655,5.181655,4.107968,-4.200566,9.802008,-6.983288,-5.163731,3.533779,-7.471876,1.609868,-3.684206,-6.241050,5.706644,-8.432599,-4.928935,-0.419051,5.403905,-4.735895,-8.064962,-4.564735,-5.913485,1.933930,-3.702409,8.138206,-0.597005,1.407412,4.189655,6.535040,-4.608079,-7.941400,-3.830584,6.629339,-5.148298,-1.199318,9.723997,-3.174114,9.472392,-3.245987,-3.004382,-8.972715,-9.216368,-0.785476,-4.358527,5.620429,6.605042,2.915240,-9.748065,5.647635,-0.978381,0.644581,-9.539302,7.553383,-9.323805,4.319191,2.383971,3.446340,5.440755,6.807245,6.559161,6.885601,5.332926,6.560425,8.698396,-2.191779,-9.201071,5.544068,-1.535347,0.224351,-1.941049,1.342560,-6.420891,-5.549600,-6.293441,9.645000,-3.923651,-6.374594,-4.821755,8.475328,-4.118108,1.619996,1.157230,9.868522,-5.829204,-2.170767,7.798495,-4.520061,1.707617,-9.201836,2.407132,8.249735,-2.619034,7.646181,8.004989,-0.434967,-3.666627,4.178747,7.867951,8.648359,8.256866,-2.662117,-3.552155,-3.662987,9.049150,2.802629,0.345906,-4.182985,1.456859,-6.199061,-6.708216,-2.273523,-1.991609,3.270067,0.743458,5.133218,-1.506201,9.748271,8.455293,-7.271836,-1.941807,3.218465,6.040328,2.175696,1.119586,6.272895,8.238954,-6.852019,2.840816,3.881022,6.663579,3.402256,-8.704326,-6.798417,2.454153,2.737166,-8.502137,8.610308,-0.585313,-9.621290,-8.126441,-8.803942,-6.086148,8.494581,-7.597043,-4.504430,-5.750333,1.857579,-1.174008,-1.853792,1.653988,-4.593828,-6.023650,5.974728,-4.094733,-2.010082,4.477977,-1.354532,2.260895,-1.701179,-2.525870,6.133543,-5.721135,-4.990319,-3.471969,-8.915897,-7.183582,-4.431161,-1.378863,4.884533,8.413297,4.329558,-8.429856,-4.329069,-9.630290,7.855918,8.574838,4.351391,-8.209107,2.177538,-0.113567,-7.674145,-6.896865,7.871042,-2.707808,8.909155,-4.211110,-6.711186,9.703322,-2.648590,8.364476,-2.768394,0.997130,5.895770,3.033874,-2.119945,-5.423687,-6.128806,6.030240,-4.806038,2.283679,-8.317380,-5.697026,-2.225053,9.364833,4.322236,5.782393,-0.920546,8.870459,-9.476974,-2.823576,-7.652377,7.965197,2.875425,-3.503729,-2.410065,7.662033,5.077408,0.402791,2.186059,0.032490,-3.509492,6.116344,4.270834,-9.015844,7.489425,-4.239409,1.176698,9.468291,5.510435,-6.439586,7.372130,-7.200112,-5.955703,-0.572038,-9.062449,-7.946308,-8.844362,5.987663,4.933818,8.709581,-4.009192,-4.427193,6.737370,-3.208681,-6.097142,-4.347866,2.411656,-3.311620,8.534981,1.646473,-3.524774,-5.044008,7.679379,-6.158758,7.736030,-7.792983,-7.548639,7.198575,-4.109297,-5.715484,2.468293,-5.276306,0.515867,-5.543913,6.227758,-6.995131,6.184938,6.064733,9.432915,9.977691,4.779191,-5.713575,6.125585,-4.741903,-8.900654,-4.094858,0.020192,-0.052552,9.863453,3.449798,-9.638723,6.321854,-1.142520,2.273873,-0.831964,-9.509873,-0.516318,3.272584,0.046492,1.613531,-0.111823,7.414116,-0.993675,-1.513814,-5.867536,-7.718927,-2.788355,-0.534716,-4.204075,-7.334411,7.026733,6.584609,9.307955,0.967870,-6.950799,-1.913044,-2.517138,-2.963056,3.528357,-8.304112,7.557777,8.803981,-7.476707,-4.933082,4.558579,-4.574866,-4.856916,-8.502613,-5.514095,-6.151247,-5.763079,-7.597504,-1.457301,2.437352,1.374504,0.500632,-7.604304,-2.212813,-0.908466,-1.281523,0.747698,-2.217651,-6.660478,-7.197948,-8.301620,2.018161,9.352243,2.136977,-1.910620,-0.789923,6.539487,-7.960469,-7.044634,-9.293999,-5.152668,-0.439446,4.021174,4.543733,0.088539,5.158944,-4.203009,-5.567391,-6.510451,7.094632,-9.980400,-0.493527,0.238490,1.846506,-8.884766,-2.515021,-2.670144,-5.121312,-5.192785,5.921256,2.369721,9.330923,3.551365,-6.533004,-1.629123,7.346984,5.935887,-3.906386,-0.306577,-8.996412,6.789799,2.480981,0.270254,-4.297109,7.650642,8.662019,-1.059385,-8.686218,-8.894624,4.861214,-0.706329,4.726637,-0.659138,-7.817129,2.523404,6.901489,-5.898658,8.233885,6.690497,9.812382,4.166207,5.708819,4.882677,-0.882794,-8.101470,-8.532489,-5.964862,-8.918452,4.411653,8.912187,8.993202,-8.052150,-9.908915,8.328835,6.794642,-3.651615,7.290327,-6.397677,-4.003164,-1.585177,-8.289365,9.349295,-4.165981,3.042116,1.514573,5.320348,-7.924888,-0.364797,9.997180,-2.801108,-0.569871,4.705561,-6.866536,-9.325781,-4.543595,-5.806867,-9.654359,6.741492,0.489806,-9.976223,-9.510865,-5.957562,3.894869,7.522610,-3.094307,8.665984,-7.767469,8.694374,-2.242237,7.567573,-0.025841,8.557606,-4.285127,-3.001498,-6.848037,-1.292446,-9.947290,4.930815,3.902709,-7.329080,-8.298806,-5.953712,-7.798310,1.316626,5.750995,-7.508373,-2.444622,-4.248798,-7.608164,4.827558,-8.632111,3.824919,-4.214725,-4.585160,4.937474,8.920108,4.365309,5.548058,4.890071,-2.557388,6.202241,4.204205,1.992949,-2.701608,-8.715734,-7.470676,0.696881,7.531414,-1.511828,1.433523,-3.977464,2.335219,-5.304809,0.062396,2.204823,6.396131,-3.253899,4.277609,-2.505916,-4.112307,7.040419,8.069908,-3.755627], dtype = "float32")#candidate|7954|(810,)|const|float32
call_7953 = relay.TupleGetItem(func_2665_call(relay.reshape(const_7954.astype('float32'), [9, 15, 6])), 3)
call_7955 = relay.TupleGetItem(func_2667_call(relay.reshape(const_7954.astype('float32'), [9, 15, 6])), 3)
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_7963 = relay.TupleGetItem(func_4240_call(), 0)
call_7964 = relay.TupleGetItem(func_4241_call(), 0)
output = relay.Tuple([call_7935,call_7953,const_7954,call_7963,])
output2 = relay.Tuple([call_7936,call_7955,const_7954,call_7964,])
func_7976 = relay.Function([], output)
mod['func_7976'] = func_7976
mod = relay.transform.InferType()(mod)
mutated_mod['func_7976'] = func_7976
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7976_call = mutated_mod.get_global_var('func_7976')
call_7977 = func_7976_call()
output = call_7977
func_7978 = relay.Function([], output)
mutated_mod['func_7978'] = func_7978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7251_call = mod.get_global_var('func_7251')
func_7253_call = mutated_mod.get_global_var('func_7253')
call_8002 = relay.TupleGetItem(func_7251_call(), 1)
call_8003 = relay.TupleGetItem(func_7253_call(), 1)
output = relay.Tuple([call_8002,])
output2 = relay.Tuple([call_8003,])
func_8035 = relay.Function([], output)
mod['func_8035'] = func_8035
mod = relay.transform.InferType()(mod)
output = func_8035()
func_8036 = relay.Function([], output)
mutated_mod['func_8036'] = func_8036
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8049 = relay.var("var_8049", dtype = "int16", shape = (2, 11, 3))#candidate|8049|(2, 11, 3)|var|int16
var_8050 = relay.var("var_8050", dtype = "int16", shape = (2, 11, 3))#candidate|8050|(2, 11, 3)|var|int16
bop_8051 = relay.bitwise_xor(var_8049.astype('int16'), relay.reshape(var_8050.astype('int16'), relay.shape_of(var_8049))) # shape=(2, 11, 3)
output = bop_8051
output2 = bop_8051
func_8061 = relay.Function([var_8049,var_8050,], output)
mod['func_8061'] = func_8061
mod = relay.transform.InferType()(mod)
mutated_mod['func_8061'] = func_8061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8061_call = mutated_mod.get_global_var('func_8061')
var_8063 = relay.var("var_8063", dtype = "int16", shape = (2, 11, 3))#candidate|8063|(2, 11, 3)|var|int16
var_8064 = relay.var("var_8064", dtype = "int16", shape = (2, 11, 3))#candidate|8064|(2, 11, 3)|var|int16
call_8062 = func_8061_call(var_8063,var_8064,)
output = call_8062
func_8065 = relay.Function([var_8063,var_8064,], output)
mutated_mod['func_8065'] = func_8065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1618_call = mod.get_global_var('func_1618')
func_1619_call = mutated_mod.get_global_var('func_1619')
call_8073 = func_1618_call()
call_8074 = func_1618_call()
output = call_8073
output2 = call_8074
func_8083 = relay.Function([], output)
mod['func_8083'] = func_8083
mod = relay.transform.InferType()(mod)
mutated_mod['func_8083'] = func_8083
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8083_call = mutated_mod.get_global_var('func_8083')
call_8084 = func_8083_call()
output = call_8084
func_8085 = relay.Function([], output)
mutated_mod['func_8085'] = func_8085
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_8097 = relay.TupleGetItem(func_2863_call(), 1)
call_8098 = relay.TupleGetItem(func_2865_call(), 1)
output = call_8097
output2 = call_8098
func_8104 = relay.Function([], output)
mod['func_8104'] = func_8104
mod = relay.transform.InferType()(mod)
output = func_8104()
func_8105 = relay.Function([], output)
mutated_mod['func_8105'] = func_8105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4448_call = mod.get_global_var('func_4448')
func_4449_call = mutated_mod.get_global_var('func_4449')
call_8122 = relay.TupleGetItem(func_4448_call(), 0)
call_8123 = relay.TupleGetItem(func_4449_call(), 0)
func_4263_call = mod.get_global_var('func_4263')
func_4266_call = mutated_mod.get_global_var('func_4266')
const_8130 = relay.const([-1,-2,6,-6,-9,-5,-9,-8,4,9,-8,8,-2,-1,6,-9,-7,-9,4,-9,-2,8,3,-8,-9,-6,8,5,2,5,8,-8,4,9,1,-2,4,-6,-5,3,-1,-5,3,-7,3,-7,-7,-7,2,-8,6,8,2,-7,8,5,9,6,-9,8], dtype = "uint64")#candidate|8130|(60,)|const|uint64
var_8131 = relay.var("var_8131", dtype = "uint64", shape = (6, 20))#candidate|8131|(6, 20)|var|uint64
call_8129 = relay.TupleGetItem(func_4263_call(relay.reshape(const_8130.astype('uint64'), [6, 1, 10]), relay.reshape(var_8131.astype('uint64'), [6, 2, 10]), ), 0)
call_8132 = relay.TupleGetItem(func_4266_call(relay.reshape(const_8130.astype('uint64'), [6, 1, 10]), relay.reshape(var_8131.astype('uint64'), [6, 2, 10]), ), 0)
output = relay.Tuple([call_8122,call_8129,const_8130,var_8131,])
output2 = relay.Tuple([call_8123,call_8132,const_8130,var_8131,])
func_8142 = relay.Function([var_8131,], output)
mod['func_8142'] = func_8142
mod = relay.transform.InferType()(mod)
var_8143 = relay.var("var_8143", dtype = "uint64", shape = (6, 20))#candidate|8143|(6, 20)|var|uint64
output = func_8142(var_8143)
func_8144 = relay.Function([var_8143], output)
mutated_mod['func_8144'] = func_8144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5292_call = mod.get_global_var('func_5292')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_8194 = func_5292_call()
call_8195 = func_5292_call()
func_3524_call = mod.get_global_var('func_3524')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_8196 = relay.TupleGetItem(func_3524_call(), 0)
call_8197 = relay.TupleGetItem(func_3525_call(), 0)
func_4263_call = mod.get_global_var('func_4263')
func_4266_call = mutated_mod.get_global_var('func_4266')
var_8212 = relay.var("var_8212", dtype = "uint64", shape = (60,))#candidate|8212|(60,)|var|uint64
const_8213 = relay.const([2,6,-2,10,7,10,6,-9,-1,-2,-3,-1,-10,9,7,-2,6,2,6,-1,-1,-4,1,1,-6,-8,-8,7,-3,-9,2,1,9,7,-5,-8,-1,5,-6,1,9,-1,10,4,6,-4,-5,8,8,9,6,-2,-10,9,3,-7,1,1,8,5,-1,2,-5,9,-6,9,-8,10,-9,-3,1,7,8,5,3,9,2,9,-2,1,9,-1,-4,-4,-2,-7,6,6,2,-1,-3,9,2,1,6,-3,5,-3,-4,5,-3,10,-6,5,-8,-3,9,-6,-7,6,-10,-10,4,7,-10,6,3,-3,10,7], dtype = "uint64")#candidate|8213|(120,)|const|uint64
call_8211 = relay.TupleGetItem(func_4263_call(relay.reshape(var_8212.astype('uint64'), [6, 1, 10]), relay.reshape(const_8213.astype('uint64'), [6, 2, 10]), ), 0)
call_8214 = relay.TupleGetItem(func_4266_call(relay.reshape(var_8212.astype('uint64'), [6, 1, 10]), relay.reshape(const_8213.astype('uint64'), [6, 2, 10]), ), 0)
func_5973_call = mod.get_global_var('func_5973')
func_5976_call = mutated_mod.get_global_var('func_5976')
const_8230 = relay.const([3.243768,6.323108,-5.784062,-4.007686,-7.024948,0.651232,5.036381,0.714290,-6.843573,2.444830,-5.769878,-4.997510,-3.762594,-7.515492,-3.457013,-5.727155,6.973357,-6.088059,8.081654,-1.088472,-3.177399,-0.086607,-1.702270,6.906897,-8.817251,5.933160,4.169578,5.683434,-5.643262,-5.476269,7.908484,-4.432732,-9.421466,-0.055099,0.042761,4.205899,-1.103114,-6.406826,6.301023,6.664959,-9.049672,8.205047,0.052345,1.899379,-8.772115,-2.463463,6.292625,-6.760364,-3.451166,9.664225,3.432096,4.076281,-1.129394,-0.897866,1.368817,8.170633,-4.753521,0.137793,1.327058,4.632535,-9.639249,4.207085,-7.648723,5.422974,-3.555338,1.386073,3.841776,4.689331,-2.435662,-0.677211,-1.613607,5.376471,-7.308639,-8.021313,-7.232975,6.875506,1.603399,-0.932037,-7.275234,-2.909971,-8.905933,-0.356849,-3.232613,-4.007685,1.558992,-7.920802,-9.348446,-5.851316,2.080686,2.648740,2.976139,-5.446217,8.039814,-1.257190,7.799453,0.922536,-0.779533,4.963042,8.002324,6.488801,-8.395204,-0.133234,-3.514028,9.637853,9.875846,7.162637,6.605222,-7.993542,-4.544165,-3.778204,2.414331,9.591247,4.359669,9.520736,-6.591438,5.442726,-0.131677,-1.788984,1.010377,-9.121290,-3.031840,0.330878,-3.493902,-9.419181,-8.084279,-7.231619,-5.519737,-6.887889,-0.734823,7.385287,-0.626817,-9.666864,-6.374526,3.344354,-2.573262,6.368783,8.722464,8.395664,-9.444338,-5.829417,-2.997634,-6.717736,5.670900,5.816381,-4.152765,-8.160738,7.838654,-7.724114,9.773310,8.419009,5.817214,-3.388025,1.123934,-9.563295,-8.695614,9.497797,9.971306,4.261188,-3.991404,2.980800,4.864542,1.746665,-7.301975,0.315717,-6.994788,3.760949,9.643140,-1.260342,4.344201,-3.070533,-9.868684,0.420415,2.503195,-1.616696,2.048486,3.748136,1.959664,1.827974,-8.553657,-0.846404,-0.069235,-1.783415,6.338313,-1.153292,-6.636690,-6.417795,-9.870030,-9.392638,4.594498,8.623061,-5.959205,9.163336,-0.348015,5.658185,2.190557,7.037936,-7.885153,3.140544,-1.522712,-5.227063,-2.305646,3.295381,-7.400964,8.285583,-5.738910,-9.129078,9.873844,9.562746,4.711563,-4.899192,-1.883225,-8.208094,5.182800,-5.285438,2.762893,-9.384202,-5.751025,1.971889,-5.168182,-4.246215,5.749667,9.903254,-4.389501,-2.889675,-2.139399,3.485827,-5.943978,1.751723,1.448612,-2.658616,-3.176269,4.234147,-4.118668,-3.381950,2.680220,-6.664817,3.138914,5.531875,-4.773725,2.758570,-6.391430,1.512356,-1.610213,-4.099429,-9.871853,2.447203,-7.497356,7.465465,0.266487,0.453110,-7.162957,4.725146,0.040932,-0.035538,7.890629,-0.725294,-2.532446,-2.915275,-0.386158,-7.419292,6.137449,-8.232360,-5.895382,9.412790,9.116680,-0.209164,-8.285112,9.369193,-7.536648,1.667358,-4.719061,4.017991,8.113577,6.939397,0.821439,-5.151985,3.635637,-7.480122,2.978406,6.272090,-1.191314,-6.539898,-3.040382,-7.158197,1.468079,-2.504957,-0.874344,-7.950857,2.511896,0.938585,-8.922858,-4.428947,-3.282519,9.212157,-1.334026,-5.295739,2.752456,6.266903,1.668401,-8.919346,6.775674,-4.772674,0.986197,5.089032,-4.751741,3.115843,-9.883046,3.578231,-6.111469,-3.299757,8.508423,4.917484,-6.444931,-8.081744,-0.335093,-2.659816,2.602188,7.911532,-8.770153,-5.655479,-8.547874,4.483508,9.621649,5.338901,9.037158,-6.204798,4.004211,9.899177,-6.843877,8.144800,8.497363,-3.677883,-3.710290,1.689083,-4.866301,3.927588,5.245475,6.722943,0.832546,-3.697438,9.454854,-0.778656,-3.853920,-0.250266,2.325166,7.630528,3.179701,-0.379225,-8.735719,-7.395167,7.904771,4.703641,-2.058962,7.167399,1.664796,6.575032,-2.528891,9.661933,7.798494,3.545467,9.336727,0.399651,-7.679086,-9.602735,6.309862,1.941456,6.400312,9.352984,2.427968,4.604538,-7.700504,2.180914,-6.627800,4.699219,-5.997316,1.502187,-9.854264,3.192887,-3.053389,9.688058,-6.319523,-5.450998,7.716720,-1.326375,-0.233830,3.796582,-2.672559,1.098830,-7.893854,-1.039233,5.651877,-6.645740,1.663621,-7.567060,-9.191874,9.625379,-6.061876,-5.637518,-6.905652,-8.219921,-9.854212,5.312566,2.539398,-9.011923,-1.410477,-9.761361,-1.226582,1.517838,-4.422772,2.526875,1.401715,-4.803229,-1.628989,0.959565,3.086080,9.578170,4.016722,-6.881861,0.685850,-3.976010,4.360314,6.664217,-8.215356,7.411612,-9.513162,1.318225,-2.823388,2.341057,-3.880640,3.091643,-0.465350,7.376797,1.134909,-5.010880,-9.627215,-0.010872,-6.532681,7.871930,-8.660651,5.479733,8.171263,-9.353500,-4.833025,-3.755307,-3.208618,-6.166705,-8.622031,3.168707,1.822563,-4.585631,-9.752003,-6.696270,-4.283684,4.778157,-3.476235,3.252013,1.637994,8.750406,3.766289,-7.122973,1.147177,0.088218,3.279856,-5.041059,-0.887933,-1.911573,7.428293,7.982241,1.009815,5.468792,-2.459505,3.962114,-6.280612,8.809480,3.812016,-2.955624,3.707246,-5.737762,-3.502276,9.737587,-9.667917,0.049471,-9.083812,1.143570,-6.519630,-2.791792,-3.419442,-1.222554,-5.084497,-9.887119,-4.088178,6.391116,-6.343581,-7.427052,-4.074591,-6.630442,6.644912,-3.556765,-7.641901,0.330964,-1.619284,6.934422,-7.791293,-5.876999,-0.015053,-4.978859,4.712036,-3.811645,9.600293,-8.034024,-9.939798,-5.253587,-2.218650,-3.921583,9.204646,4.637831,0.258253,-1.023651,6.741675,-5.613945,5.067579,-8.444077,-4.911973,4.854968,5.992871,2.942705,-7.807450,4.654296,9.408057,9.377260,-9.234342,-3.604146,-4.483371,5.116685,0.187430,4.571637,-9.576504,1.216557,-5.692364,-5.652763,-2.248372,4.897477,-5.308842,-2.672607,-1.048882,-5.927746,-1.522242,-1.594820,9.335946,-3.207756,-5.560873,6.750466,3.615311,5.166697,1.011745,7.493004,-0.759356,-6.412510,-9.275370,-1.744195,1.348891,8.638455,8.853887,-3.033892,4.975735,-0.266792,-2.878224,-5.616996,-3.687147,2.636472,6.143954,-6.506558,4.635533,-8.539832,7.990179,1.560542,1.780970,-2.642999,-8.743817,7.054397,-8.957197,9.711711,-5.595006,-6.624802,-5.442165,-6.019295,3.869223,7.995537,-5.501010,-7.501736,-1.662043,-0.074314,-4.282826,-7.513147,6.355037,-7.697950,5.586329,-9.869070,2.206766,9.329831,-7.083551,9.214169,-8.450789,-1.892245,6.158773,-7.861202,-2.308750,0.791609,0.555844,-0.093474,-8.802615,-0.772450,-1.392888,5.846177,-1.151577,8.094126,-3.410508,-4.513545,7.621044,5.898186,7.157315,-7.393170,-7.897313,-1.945470,-9.681764,-9.325263,4.922320,-2.757807,7.369768,1.763261,-0.173753,-7.718262,7.318713,8.626692,-0.025016,0.076987,-7.240431,4.144561,-9.823318,3.815958,-0.230587,9.128048,-3.865082,-1.488314,2.813666,8.273949,-5.568816,-1.540292,-1.800821,0.964767,2.019353,-2.961905,-7.071682,-1.270171,3.542368,0.158685,-3.760246,9.203312,1.767202,-8.547187,1.889864,-8.883418,-7.152760,-3.754464,6.990252,2.239767,-2.419818,-6.220544,7.681768,2.113314,-8.661195,8.456471,0.840837,-1.751843,-2.142221,2.975435,-0.006203,6.730597,9.313134,-1.569761,8.853518,9.849285,6.004537,9.961224,-4.436296,-1.266666,7.241381,1.274103,-0.797400,3.371031,7.569488,4.110287,0.745070,-6.036834,-3.286010,8.696940,-9.064877,6.228226,-9.299478,-5.344680,-4.275441,-0.300114,-3.089092,-6.789327,1.769317,5.644557,8.645142,-6.864934,-3.078529,4.745206,5.951154,-4.538109,9.729806,-7.095658,-3.558793], dtype = "float64")#candidate|8230|(715,)|const|float64
var_8231 = relay.var("var_8231", dtype = "float32", shape = (810,))#candidate|8231|(810,)|var|float32
call_8229 = relay.TupleGetItem(func_5973_call(relay.reshape(const_8230.astype('float64'), [13, 5, 11]), relay.reshape(var_8231.astype('float32'), [81, 10]), ), 1)
call_8232 = relay.TupleGetItem(func_5976_call(relay.reshape(const_8230.astype('float64'), [13, 5, 11]), relay.reshape(var_8231.astype('float32'), [81, 10]), ), 1)
output = relay.Tuple([call_8194,call_8196,call_8211,var_8212,const_8213,call_8229,const_8230,var_8231,])
output2 = relay.Tuple([call_8195,call_8197,call_8214,var_8212,const_8213,call_8232,const_8230,var_8231,])
func_8239 = relay.Function([var_8212,var_8231,], output)
mod['func_8239'] = func_8239
mod = relay.transform.InferType()(mod)
mutated_mod['func_8239'] = func_8239
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8239_call = mutated_mod.get_global_var('func_8239')
var_8241 = relay.var("var_8241", dtype = "uint64", shape = (60,))#candidate|8241|(60,)|var|uint64
var_8242 = relay.var("var_8242", dtype = "float32", shape = (810,))#candidate|8242|(810,)|var|float32
call_8240 = func_8239_call(var_8241,var_8242,)
output = call_8240
func_8243 = relay.Function([var_8241,var_8242,], output)
mutated_mod['func_8243'] = func_8243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8083_call = mod.get_global_var('func_8083')
func_8085_call = mutated_mod.get_global_var('func_8085')
call_8265 = func_8083_call()
call_8266 = func_8083_call()
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_8275 = relay.TupleGetItem(func_4240_call(), 0)
call_8276 = relay.TupleGetItem(func_4241_call(), 0)
func_8104_call = mod.get_global_var('func_8104')
func_8105_call = mutated_mod.get_global_var('func_8105')
call_8279 = func_8104_call()
call_8280 = func_8104_call()
func_5840_call = mod.get_global_var('func_5840')
func_5844_call = mutated_mod.get_global_var('func_5844')
var_8284 = relay.var("var_8284", dtype = "uint32", shape = (936,))#candidate|8284|(936,)|var|uint32
call_8283 = relay.TupleGetItem(func_5840_call(relay.reshape(var_8284.astype('uint32'), [13, 6, 12]), relay.reshape(var_8284.astype('uint32'), [13, 6, 12]), ), 1)
call_8285 = relay.TupleGetItem(func_5844_call(relay.reshape(var_8284.astype('uint32'), [13, 6, 12]), relay.reshape(var_8284.astype('uint32'), [13, 6, 12]), ), 1)
output = relay.Tuple([call_8265,call_8275,call_8279,call_8283,var_8284,])
output2 = relay.Tuple([call_8266,call_8276,call_8280,call_8285,var_8284,])
func_8288 = relay.Function([var_8284,], output)
mod['func_8288'] = func_8288
mod = relay.transform.InferType()(mod)
mutated_mod['func_8288'] = func_8288
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8289 = relay.var("var_8289", dtype = "uint32", shape = (936,))#candidate|8289|(936,)|var|uint32
func_8288_call = mutated_mod.get_global_var('func_8288')
call_8290 = func_8288_call(var_8289)
output = call_8290
func_8291 = relay.Function([var_8289], output)
mutated_mod['func_8291'] = func_8291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5714_call = mod.get_global_var('func_5714')
func_5715_call = mutated_mod.get_global_var('func_5715')
call_8318 = relay.TupleGetItem(func_5714_call(), 0)
call_8319 = relay.TupleGetItem(func_5715_call(), 0)
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
const_8334 = relay.const([5.245488,-5.661862,-5.928549,1.290893,6.564183,-2.989618,1.143754,9.738920,4.362042,9.812055,8.003064,-0.287372,-8.867933,-5.072988,-1.846732,-1.326155,-5.167495,6.587089,-0.114047,5.451117,1.470905,-1.905093,3.997474,-9.052118,2.317336,9.288897,3.073407,2.046853,-2.406321,8.297624,7.008881,6.181321,6.276973,2.115231,4.674928,5.123681,-7.256854,-5.573708,1.688632,-7.076127,-0.307892,8.594169,-8.955142,8.876767,-5.845829,3.601058,-2.947138,-4.157389,8.725088,2.954609,-5.228786,8.362951,-0.205254,-2.888683,8.871997,-0.526625,-9.890487,2.573011,-0.187769,-4.615712,0.891098,9.673191,-6.284316,9.913333,6.845783,-1.892210,1.631293,-2.936221,3.461723,5.823554,0.629817,0.466670,6.933362,-2.859539,1.841020,2.413831,-4.759197,5.130602,-0.427670,0.861708,8.131150,8.026090,8.869223,6.358864,-8.691814,3.814481,-3.784937,-3.178945,5.730847,-9.430210,6.388273,-2.862090,-9.013796,-1.114434,-7.597279,-6.579333,7.958657,4.594727,4.154656,-0.176761,6.432671,6.360567,-5.297766,-4.173323,9.941852,-6.093108,-4.576741,-0.723451,-6.550715,1.678423,-0.967652,1.461742,1.685858,3.133833,9.150707,-5.509866,8.563008,-5.428021,3.288893,-7.337777,5.360140,7.768342,2.710591,-4.462431,-9.481169,-0.594396,9.699131,0.407128,-4.893579,1.920503,-2.407575,8.452791,-5.756554,2.139554,-1.269317,-7.617339,-9.109179,8.567199,8.662285,-2.983027,3.653935,1.069672,-7.381099,7.370683,7.048255,-5.719254,-1.554054,6.518907,6.489273,6.567538,-1.748669,-5.607636,8.017927,-3.758817,1.283364,1.539241,-2.934881,-9.325672,1.074213,8.358114,-1.748568,-9.656470,3.924233,6.447549,-1.024447,-3.502801,-1.355872,7.546707,-7.391059,5.939959,-9.152623,-6.639549,9.471008,0.957016,-3.079209,1.184925,-7.088572,-2.869115,4.336562,1.937317,-0.448446,3.394696,-3.135927,-0.955003,-6.039751,-1.916699,-2.117251,9.024305,1.137701,-8.987967,-2.276895,8.026803,6.853058,-9.294609,0.718271,-6.880715,-7.821671,4.282688,1.356322,1.668676,3.678653,-6.349672,9.203837,7.597657,0.374323,-7.256898,3.609458,-5.480378,7.636902,2.400212,-6.642005,-5.212901,7.420100,1.873622,-5.307237,7.433287,4.316673,2.008204,1.491356,0.443883,8.336432,-9.651690,1.776974,5.280713,-0.390953,-1.875080,4.771857,6.926930,-3.953242,3.218936,3.843491,-2.548756,-1.949961,1.512306,-0.350477,-2.044627,6.402663,-8.793217,-5.303208,6.267692,-1.993955,3.604087,2.755853,0.958019,-6.670242,-5.378983,6.010528,-7.953820,-4.823349,5.211285,-3.152302,-0.406992,3.431512,5.456961,2.532034,-3.201557,-9.197772,6.864851,-4.350533,3.803400,4.630107,-7.854592,-9.933620,-2.986530,1.174098,2.692625,-6.065939,3.761196,-7.600388,6.575825,3.250092,3.803499,8.426877,1.661151,5.234229,-2.038506,-4.379783,5.421122,7.529886,-3.825750,-9.759825,7.225765,7.154953,-0.733978,1.895295,7.723950,1.712212,-6.595888,0.434264,-3.770356,-4.122433,3.008622,5.728456,9.086807,4.729834,6.713713,8.976448,-8.837216,8.866309,-7.225367,-6.666015,-6.773907,-9.511280,-6.976329,-2.492528,9.137065,-6.332295,-3.186505,0.429422,-7.175381,6.428225,-4.060275,-9.936157,9.957006,9.684817,-9.789019,-3.238933,3.452910,6.528565,-3.829011,-7.911952,-5.494342,3.894948,0.430097,-4.197656,4.679518,4.237647,-2.136827,-8.862029,-4.061868,9.737079,7.282109,4.991334,8.799207,-9.343274,-2.786707,5.012182,4.645104,3.959866,3.289124,3.388045,7.378647,4.466826,-1.225007,-6.128847,2.878771,-6.263125,2.726006,-2.877434,-1.653096,-4.372185,0.112000,-2.861127,-7.292307,4.293691,8.345323,-0.898369,-4.262624,6.161831,2.013722,1.846448,3.605658,4.977080,3.602635,9.669903,3.890895,-2.015691,8.488883,9.746182,2.244487,-4.802920,8.789438,8.728573,-6.933254,3.295443,-3.756665,-5.196335,-6.195515,-9.711935,9.277806,0.710379,-6.421138,-5.737052,-2.773733,6.870885,-6.047180,6.738344,6.506458,7.393588,5.103692,9.293317,4.129307,6.497562,-0.479525,5.748310,-0.970107,-8.926593,0.353406,-0.709683,-6.259072,8.216425,1.739972,2.358280,5.637534,-6.905981,7.976279,2.086508,-6.817491,-5.328767,-7.641087,-7.318112,-5.204330,1.957826,8.192130,-9.690389,-3.853179,3.682290,-8.499154,-0.059528,3.799871,-7.994868,-9.154390,-1.277944,-8.726994,1.957721,-7.761551,4.057335,-1.359552,-1.842975,8.398807,-1.868093,-0.078110,9.536960,-5.303954,6.538370,2.004733,-7.414712,9.495599,-5.044988,9.970051,-2.258901,0.429431,-9.524113,5.390801,-1.907798,4.734455,-3.675563,-1.370960,-9.394137,0.859027,-9.916845,8.090551,-4.676450,3.625966,4.458153,5.443681,8.615614,5.686802,-5.325231,-2.576671,6.369121,3.919452,-8.393229,-9.833198,-3.692479,-1.540328,-7.682549,8.831987,-2.313283,9.091124,2.644248,8.515116,1.823490,9.648703,9.360100,-2.588886,1.723198,-3.892464,6.410106,2.867543,-4.281453,9.385041,3.758919,-0.887100,8.955416,8.760376,-1.869949,2.840229,-9.601312,0.208940,4.867560,-1.494196,-5.946284,-1.864294,2.030229,8.426883,9.428439,-3.261559,-5.540706,-2.119530,-8.096548,-9.430080,-6.994924,9.503067,-8.104404,4.883129,-2.784833,4.692767,-3.264249,8.021248,9.225249,-9.072769,1.455881,8.780482,7.302834,4.193180,-0.707227,-9.072125,-3.755772,5.698676,-5.708944,-4.722379,-9.212507,0.874201,5.226344,7.446385,-4.326286,4.987559,-5.874383,5.615378,-8.156304,-2.204472,-3.825364,7.920333,-0.238837,-5.150686,1.610299,5.073549,-9.487451,2.876477,3.721425,-2.338235,-8.474355,2.997627,-6.997501,-0.518646,-5.908716,1.804933,7.156391,8.507377,9.862346,-0.021677,-4.880803,8.730054,4.838098,-9.576317,7.543975,-6.277635,-7.767387,-7.631833,-9.797804,6.118451,0.658991,1.738488,8.321134,-3.954900,-1.724774,-5.290856,2.541340,2.752443,-0.608020,6.713874,-6.264590,8.735172,-8.984351,-5.300816,-7.650584,2.440272,-5.803152,-5.960818,7.726556,8.955028,4.746847,-7.450972,8.539645,8.681096,3.663053,8.414603,-1.115064,-2.224960,-0.853423,1.337369,-5.241543,1.287351,-4.052220,-3.637898,-4.701636,2.964804,9.785895,-1.937622,-0.498068,-9.890186,2.147828,8.072081,-0.987411,-0.675892,-5.065831,8.708890,-9.028858,-1.121058,-2.473740,-2.426799,-9.948480,2.067415,6.351010,-8.326490,9.400178,8.919269,-8.750874,3.789993,-3.938286,8.559911,4.149728,0.700728,6.721253,-5.765450,-8.198407,7.236581,4.290659,6.657380,-0.808403,-5.064791,-5.066454,-8.401112,-9.824689,-2.562773,4.165771,-2.671985,-1.190933,-3.941441,5.443647,-3.206625,6.052245,-0.987051,-2.643799,7.754476,9.924586,-6.776941,5.499626,-7.790834,-2.586930,-7.337519,-9.521331,8.723735,-9.524596,5.132902,-2.505388,-8.465483,5.345844,-1.400831,-6.333580,-0.383856,5.075430,5.884429,-9.719069,7.134691,-1.611069,-8.671996,-8.673070,-1.316916,-3.101638,-1.935719,7.628362,-5.375880,2.802845,-2.789906,3.618131,9.437386,2.678029,8.871260,-8.028760,9.510651,2.105022,3.001150,4.579718,-6.137203,5.797514,-8.859749,9.681757,5.716801,-6.046575,-3.295318,8.640838,-2.128761,7.428011,-9.983182,-0.244953,-6.020224,6.936050,7.428621,6.109077,-7.325806,-1.673585,1.795571,-5.135261,-5.397193,-3.694337,-3.416207,-4.224739,2.250766,-5.163963,4.149090,1.552149,-3.059282,-6.562997,2.335324,-2.866236,-1.151359,-2.800111,-4.231362,5.057022,4.547821,-6.384482,6.053551,6.980009,-8.733966,-1.473672,-5.596043,8.633835,-2.700502,8.672441,-1.818583,-7.061667,-5.755549,-5.910514,6.565385,-0.632284,-2.690369,-1.927030,1.685558,-6.120082,9.008423,-4.896022,-3.655446,3.642288,0.039656,-1.353853,-9.115437,-1.372462,0.372709,8.998032,-8.599266,-8.056409,-8.956293,-8.548296,-0.100423,0.839249,6.107433,7.893837,-3.001387,1.266174,7.101412,2.289522,-2.780189,2.714811,-3.685506,-8.643233,-5.445461,6.929831,7.586486,-7.790412,-7.660616,6.680988,1.337812,6.619885,6.088047,0.352218,-0.642986,-1.384180,5.394365,3.474285,9.860641,-0.059753,-8.833496,-2.442059,-5.549295,4.848705,3.745173,-4.414943,4.004111,-1.764611,-0.707982,-6.593820,-2.450546,0.490166,-7.753523,8.675649,-4.710360,0.369887,-0.303162,-6.209108,-4.604628,3.255092,7.984162,5.819634,-0.778772,2.295417,5.582288,5.890890,7.827154,5.116473,7.538049,9.530738,7.315302,-7.994318,-1.201818,-5.835051,-5.023721,-5.939760,4.452516,5.173686,4.894980,5.061461,-7.415861,-5.738878,2.914395,9.589128,8.733383,5.983722,2.569732,-7.558283,-7.988443], dtype = "float64")#candidate|8334|(832,)|const|float64
call_8333 = relay.TupleGetItem(func_5442_call(relay.reshape(const_8334.astype('float64'), [104, 8])), 1)
call_8335 = relay.TupleGetItem(func_5444_call(relay.reshape(const_8334.astype('float64'), [104, 8])), 1)
bop_8342 = relay.bitwise_or(call_8333.astype('uint32'), relay.reshape(const_8334.astype('uint32'), relay.shape_of(call_8333))) # shape=(8, 8, 13)
bop_8345 = relay.bitwise_or(call_8335.astype('uint32'), relay.reshape(const_8334.astype('uint32'), relay.shape_of(call_8335))) # shape=(8, 8, 13)
output = relay.Tuple([call_8318,bop_8342,])
output2 = relay.Tuple([call_8319,bop_8345,])
func_8353 = relay.Function([], output)
mod['func_8353'] = func_8353
mod = relay.transform.InferType()(mod)
output = func_8353()
func_8354 = relay.Function([], output)
mutated_mod['func_8354'] = func_8354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6778_call = mod.get_global_var('func_6778')
func_6779_call = mutated_mod.get_global_var('func_6779')
call_8368 = relay.TupleGetItem(func_6778_call(), 0)
call_8369 = relay.TupleGetItem(func_6779_call(), 0)
output = relay.Tuple([call_8368,])
output2 = relay.Tuple([call_8369,])
func_8396 = relay.Function([], output)
mod['func_8396'] = func_8396
mod = relay.transform.InferType()(mod)
mutated_mod['func_8396'] = func_8396
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8396_call = mutated_mod.get_global_var('func_8396')
call_8397 = func_8396_call()
output = call_8397
func_8398 = relay.Function([], output)
mutated_mod['func_8398'] = func_8398
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8407 = relay.var("var_8407", dtype = "float32", shape = (14, 7, 16))#candidate|8407|(14, 7, 16)|var|float32
uop_8408 = relay.erf(var_8407.astype('float32')) # shape=(14, 7, 16)
func_5840_call = mod.get_global_var('func_5840')
func_5844_call = mutated_mod.get_global_var('func_5844')
const_8412 = relay.const([1,-7,4,2,8,4,-8,6,-7,4,-4,-5,-5,9,-5,2,-2,4,10,-9,7,6,2,-3,6,2,4,-7,6,-8,8,8,10,-8,-1,-1,-2,4,-8,4,-6,6,-4,8,8,-3,-5,6,3,8,-1,-2,7,-9,-3,-8,1,-1,-6,-5,3,9,-6,-7,-9,5,-5,4,-1,6,-6,-4,-2,-2,-2,-1,2,6,6,-9,8,6,-10,-5,5,-4,-10,8,3,-10,-6,3,2,-5,3,-5,9,4,4,-10,-5,-10,5,8,-9,-7,9,4,-9,4,-5,3,-2,3,8,-7,-10,-9,8,-4,-6,-3,-1,10,5,10,-5,-6,-9,7,4,2,2,10,-1,-8,-7,3,9,6,9,8,10,-1,4,-8,-1,-4,-6,-4,1,3,6,-4,1,-2,7,-4,-3,7,2,-8,8,7,-8,-8,-6,9,-10,10,-4,-4,2,9,3,-5,-1,-10,-8,-10,2,7,10,-2,10,4,4,-6,-3,2,-1,3,-3,-9,-3,-9,-9,-7,-2,-1,-2,-6,-2,3,-9,3,3,2,-10,6,1,10,-2,3,5,8,-1,-4,-9,8,1,6,7,9,-10,-3,-10,1,2,-8,9,6,10,-1,-6,-5,-10,10,-10,7,4,10,-4,8,6,5,-1,3,1,-8,-3,-4,7,-10,-3,-6,-6,-4,9,8,-7,-1,4,-10,8,-5,-3,5,3,7,-2,-6,9,-1,-10,-4,-2,7,-8,4,-5,8,10,-7,9,-10,5,1,5,-4,3,-4,-4,-4,8,-8,-8,2,-10,-2,1,9,-7,-3,6,-7,-5,5,-4,2,8,-6,6,6,-6,-2,10,4,4,2,-5,9,2,9,-5,-9,-1,-1,4,3,-4,7,-8,3,-8,-4,-6,5,8,-3,7,6,-8,4,-4,9,4,4,-9,-8,2,2,-6,5,10,-9,-1,-4,-3,8,-7,-7,-5,7,-8,2,6,9,10,-9,3,9,4,2,4,-7,8,-6,-5,-10,-7,-4,-8,-6,-6,-1,3,-2,5,-6,-3,-2,7,8,10,-4,10,-7,-10,7,7,4,7,-9,-9,1,-6,-4,10,4,10,4,-3,-8,-5,-8,10,4,-7,10,-8,9,-4,6,5,-4,7,6,-1,2,7,10,-3,7,-7,-7,9,-8,8,-9,-5,9,10,-1,-10,-9,-6,-4,-3,-10,-1,-5,10,-5,7,-1,-8,-4,8,1,2,-4,-7,5,1,-10,2,-5,9,1,6,10,-4,2,2,9,3,2,4,-2,5,-9,9,9,4,4,4,3,10,2,-1,8,6,8,7,5,3,-7,8,10,8,1,10,1,-1,4,6,8,1,-10,-7,8,-8,4,-5,-9,10,4,-4,-2,6,9,-9,3,-2,-6,-9,10,-3,5,-9,-8,4,9,-5,-5,8,-4,-10,4,-10,-2,9,6,4,-10,6,2,-10,-6,-5,-9,-4,9,-1,-7,-5,10,8,-8,7,-7,-5,-3,-1,3,1,-8,-6,8,-2,-8,3,-3,-4,-5,-6,-4,-3,-8,-5,10,-3,-10,5,-6,-4,-6,-2,9,-9,-7,-7,9,-7,4,-8,-9,-5,3,8,9,-4,8,-5,10,-1,2,-7,10,8,9,10,-10,-6,5,2,7,-10,-2,3,-10,10,-4,2,4,-10,9,-10,5,10,1,3,-10,4,-7,-5,-1,10,5,-1,-6,-1,-1,2,6,-5,5,-4,2,-6,-6,7,-7,5,2,10,-9,1,-1,-5,6,-3,-9,-6,6,-9,5,2,-6,8,4,-4,-1,2,-7,-9,8,-3,-1,-7,3,1,-5,-3,-9,7,-9,4,-5,9,5,4,-10,-10,8,-9,-5,-10,-3,-9,2,-6,8,-10,-8,4,9,-7,-5,-1,6,3,-10,2,-5,-6,1,-9,-3,10,2,-5,4,-1,10,-3,3,10,8,-9,-4,-2,-8,-2,4,2,-7,-8,-10,-9,2,-9,-9,-10,-10,2,3,-1,-8,2,6,-9,-1,-4,-5,-5,9,4,4,5,-1,10,-2,5,-3,-2,-10,-3,-8,-4,-2,-2,5,-8,-9,3,-9,-6,-3,1,-7,-6,-5,-8,6,8,4,-8,7,8,-9,8,3,9,4,-3,-2,-7,-5,-2,8,-8,9,1,-4,-1,-7,8,-10,7,6,4,8,7,-6,-4,-8,-7,10,2,-5,6,-2,4,-1,6,1,-7,1,4,-4,2,-3,-8,8,-7,-5,-5,-7,-6,1,8,-4,-3,-3,-2,7,9,-6,-3,9,5,2,8,10,10,8,3,4,-6,-5,2,-4,-10,-9,3,2,1,-10,1,-5,-3,-8,-6,4,-9,-2,-1,-3,-7,3,-8,1,-6,8,-3,8,-7,-2,-1,7,-7,1,5,6,-6,-5,-3,4,7,7,-7,6,3,9,8,4,-2,1,8,-3,-8,1,-3,1,8,-2,4,1,9,1,-5,-1,9,8,1,6,-8,-9,1,-2,9,-6,-3,-10], dtype = "uint32")#candidate|8412|(936,)|const|uint32
call_8411 = relay.TupleGetItem(func_5840_call(relay.reshape(const_8412.astype('uint32'), [13, 6, 12]), relay.reshape(const_8412.astype('uint32'), [13, 6, 12]), ), 0)
call_8413 = relay.TupleGetItem(func_5844_call(relay.reshape(const_8412.astype('uint32'), [13, 6, 12]), relay.reshape(const_8412.astype('uint32'), [13, 6, 12]), ), 0)
output = relay.Tuple([uop_8408,call_8411,const_8412,])
output2 = relay.Tuple([uop_8408,call_8413,const_8412,])
func_8417 = relay.Function([var_8407,], output)
mod['func_8417'] = func_8417
mod = relay.transform.InferType()(mod)
mutated_mod['func_8417'] = func_8417
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8418 = relay.var("var_8418", dtype = "float32", shape = (14, 7, 16))#candidate|8418|(14, 7, 16)|var|float32
func_8417_call = mutated_mod.get_global_var('func_8417')
call_8419 = func_8417_call(var_8418)
output = call_8419
func_8420 = relay.Function([var_8418], output)
mutated_mod['func_8420'] = func_8420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4448_call = mod.get_global_var('func_4448')
func_4449_call = mutated_mod.get_global_var('func_4449')
call_8445 = relay.TupleGetItem(func_4448_call(), 1)
call_8446 = relay.TupleGetItem(func_4449_call(), 1)
output = call_8445
output2 = call_8446
func_8449 = relay.Function([], output)
mod['func_8449'] = func_8449
mod = relay.transform.InferType()(mod)
mutated_mod['func_8449'] = func_8449
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8449_call = mutated_mod.get_global_var('func_8449')
call_8450 = func_8449_call()
output = call_8450
func_8451 = relay.Function([], output)
mutated_mod['func_8451'] = func_8451
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8467 = relay.var("var_8467", dtype = "float32", shape = (4, 7, 4))#candidate|8467|(4, 7, 4)|var|float32
const_8468 = relay.const([[[4.529473,4.394857,5.053843,6.051039],[-8.024958,2.161080,-0.806848,-4.250020],[4.062748,-7.389435,-1.594188,-9.963932],[-5.698700,9.796102,2.599867,8.667898],[9.323059,4.429917,8.546770,7.433045],[-9.315445,-3.342895,-3.603174,0.477047],[9.898138,1.571516,-6.691862,2.677563]],[[-9.346492,3.706105,4.438245,-1.207506],[9.323431,-0.115060,5.830510,-3.984026],[-0.975033,-9.293841,-4.275533,-0.416158],[0.204565,9.414083,8.466937,-4.537951],[2.563361,2.374042,-3.859925,7.097320],[2.277479,-5.164871,4.865655,-8.711398],[4.937080,6.911071,-6.169098,-7.593043]],[[0.413838,3.922999,-8.097723,7.928298],[7.066287,3.059524,-0.008805,7.983146],[-9.971837,-0.556595,4.938389,4.407506],[9.041723,-3.173878,-2.150920,2.436193],[-0.491903,-8.876076,-7.204480,-7.176931],[-3.558476,-1.031841,-5.095884,-6.210945],[4.830836,-0.726979,7.055483,-1.420712]],[[-5.374721,-9.859173,3.999287,6.145576],[-2.190295,-3.822068,8.107996,-6.261715],[-1.055801,-5.098009,-9.383892,9.661048],[-5.214615,-8.991887,0.077142,-4.127618],[7.491567,-5.080560,6.335059,-5.325864],[6.469241,-2.989038,7.115625,-0.022834],[3.737871,-3.620316,8.797913,-2.912773]]], dtype = "float32")#candidate|8468|(4, 7, 4)|const|float32
bop_8469 = relay.floor_mod(var_8467.astype('float32'), relay.reshape(const_8468.astype('float32'), relay.shape_of(var_8467))) # shape=(4, 7, 4)
output = bop_8469
output2 = bop_8469
func_8487 = relay.Function([var_8467,], output)
mod['func_8487'] = func_8487
mod = relay.transform.InferType()(mod)
mutated_mod['func_8487'] = func_8487
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8488 = relay.var("var_8488", dtype = "float32", shape = (4, 7, 4))#candidate|8488|(4, 7, 4)|var|float32
func_8487_call = mutated_mod.get_global_var('func_8487')
call_8489 = func_8487_call(var_8488)
output = call_8489
func_8490 = relay.Function([var_8488], output)
mutated_mod['func_8490'] = func_8490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8449_call = mod.get_global_var('func_8449')
func_8451_call = mutated_mod.get_global_var('func_8451')
call_8588 = func_8449_call()
call_8589 = func_8449_call()
output = relay.Tuple([call_8588,])
output2 = relay.Tuple([call_8589,])
func_8594 = relay.Function([], output)
mod['func_8594'] = func_8594
mod = relay.transform.InferType()(mod)
mutated_mod['func_8594'] = func_8594
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8594_call = mutated_mod.get_global_var('func_8594')
call_8595 = func_8594_call()
output = call_8595
func_8596 = relay.Function([], output)
mutated_mod['func_8596'] = func_8596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4189_call = mod.get_global_var('func_4189')
func_4190_call = mutated_mod.get_global_var('func_4190')
call_8640 = relay.TupleGetItem(func_4189_call(), 0)
call_8641 = relay.TupleGetItem(func_4190_call(), 0)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_8670 = relay.TupleGetItem(func_2925_call(), 0)
call_8671 = relay.TupleGetItem(func_2927_call(), 0)
output = relay.Tuple([call_8640,call_8670,])
output2 = relay.Tuple([call_8641,call_8671,])
func_8673 = relay.Function([], output)
mod['func_8673'] = func_8673
mod = relay.transform.InferType()(mod)
mutated_mod['func_8673'] = func_8673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8673_call = mutated_mod.get_global_var('func_8673')
call_8674 = func_8673_call()
output = call_8674
func_8675 = relay.Function([], output)
mutated_mod['func_8675'] = func_8675
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8778 = relay.var("var_8778", dtype = "int32", shape = ())#candidate|8778|()|var|int32
var_8779 = relay.var("var_8779", dtype = "int32", shape = (7, 7, 8))#candidate|8779|(7, 7, 8)|var|int32
bop_8780 = relay.multiply(var_8778.astype('int32'), var_8779.astype('int32')) # shape=(7, 7, 8)
output = bop_8780
output2 = bop_8780
func_8791 = relay.Function([var_8778,var_8779,], output)
mod['func_8791'] = func_8791
mod = relay.transform.InferType()(mod)
var_8792 = relay.var("var_8792", dtype = "int32", shape = ())#candidate|8792|()|var|int32
var_8793 = relay.var("var_8793", dtype = "int32", shape = (7, 7, 8))#candidate|8793|(7, 7, 8)|var|int32
output = func_8791(var_8792,var_8793,)
func_8794 = relay.Function([var_8792,var_8793,], output)
mutated_mod['func_8794'] = func_8794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_8859 = relay.TupleGetItem(func_595_call(), 1)
call_8860 = relay.TupleGetItem(func_596_call(), 1)
output = call_8859
output2 = call_8860
func_8880 = relay.Function([], output)
mod['func_8880'] = func_8880
mod = relay.transform.InferType()(mod)
mutated_mod['func_8880'] = func_8880
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8880_call = mutated_mod.get_global_var('func_8880')
call_8881 = func_8880_call()
output = call_8881
func_8882 = relay.Function([], output)
mutated_mod['func_8882'] = func_8882
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9012 = relay.const([[[5.860992,-3.747924,0.673421,9.074226,5.690456,2.453783,-4.820636,-9.438946,-2.581464,6.857830,5.051411]],[[0.136026,-6.573165,-5.828066,-2.755420,9.011320,-9.638660,-0.867640,-0.721354,9.705379,5.133425,-0.793001]],[[-4.033328,8.288746,9.446697,5.429219,-5.742392,-2.670398,3.014806,-6.019216,4.652644,-3.938450,3.205302]],[[8.646542,-4.315714,-5.306243,0.628153,1.352837,7.832781,8.516682,-8.990194,-5.977861,3.734639,0.617240]],[[0.880914,6.376644,-6.557766,-8.389186,-3.161964,9.727499,5.860495,-9.305510,4.836995,-4.378367,-0.593581]],[[8.705382,-1.833003,5.030213,2.045210,-6.147660,-8.340152,5.172938,1.775775,5.338947,3.194248,-2.147171]],[[-4.419652,3.643461,3.328341,-6.282868,4.160589,-3.916705,0.203147,-2.481235,-8.968531,-8.858180,-0.259751]],[[5.323895,0.025335,7.803646,-7.191600,0.042228,0.893912,-2.424496,-4.758733,-9.791296,-1.236563,0.497624]]], dtype = "float32")#candidate|9012|(8, 1, 11)|const|float32
var_9013 = relay.var("var_9013", dtype = "float32", shape = (8, 1, 11))#candidate|9013|(8, 1, 11)|var|float32
bop_9014 = relay.greater(const_9012.astype('bool'), relay.reshape(var_9013.astype('bool'), relay.shape_of(const_9012))) # shape=(8, 1, 11)
var_9018 = relay.var("var_9018", dtype = "bool", shape = (8, 3, 11))#candidate|9018|(8, 3, 11)|var|bool
bop_9019 = relay.logical_or(bop_9014.astype('bool'), var_9018.astype('bool')) # shape=(8, 3, 11)
func_2207_call = mod.get_global_var('func_2207')
func_2208_call = mutated_mod.get_global_var('func_2208')
call_9026 = relay.TupleGetItem(func_2207_call(), 1)
call_9027 = relay.TupleGetItem(func_2208_call(), 1)
func_3953_call = mod.get_global_var('func_3953')
func_3954_call = mutated_mod.get_global_var('func_3954')
call_9034 = relay.TupleGetItem(func_3953_call(), 1)
call_9035 = relay.TupleGetItem(func_3954_call(), 1)
bop_9053 = relay.floor_mod(var_9013.astype('float32'), bop_9019.astype('float32')) # shape=(8, 3, 11)
uop_9068 = relay.tan(var_9013.astype('float64')) # shape=(8, 1, 11)
const_9074 = relay.const([[[-3.724332,9.302304,-6.437726,5.800243,0.266827,0.179615,-1.043532,4.577198,-1.363475,-2.266685,-7.849812]],[[8.092594,2.458588,0.342800,1.529598,1.265321,6.885153,-7.789862,8.455116,7.880562,-7.448701,3.435128]],[[8.230938,-4.464972,-9.287259,-8.271149,-2.017453,6.598458,6.451185,-9.915207,-9.585670,-9.092969,-0.767943]],[[7.466535,5.203870,-9.333302,1.373817,-7.674962,-3.673220,5.663052,-9.882932,-1.421681,1.033279,-4.809714]],[[-9.367196,9.015081,-3.554347,-4.357100,-5.428799,-4.160011,-9.795330,1.301436,-3.669010,-3.072966,-1.189829]],[[-7.166187,-2.983868,-0.474478,-8.682003,-4.107641,2.070612,5.914017,-6.380843,8.521850,-8.764664,-4.867739]],[[-7.394379,-7.298312,6.050685,-6.013562,-4.035169,-0.595237,4.405359,-6.906441,3.424725,-6.546213,-9.936356]],[[-8.515374,8.533748,-3.316275,7.790128,2.253035,-3.391304,4.733358,-1.472075,-9.623792,-0.418251,4.271311]]], dtype = "float64")#candidate|9074|(8, 1, 11)|const|float64
bop_9075 = relay.divide(uop_9068.astype('float32'), relay.reshape(const_9074.astype('float32'), relay.shape_of(uop_9068))) # shape=(8, 1, 11)
func_7515_call = mod.get_global_var('func_7515')
func_7516_call = mutated_mod.get_global_var('func_7516')
call_9086 = relay.TupleGetItem(func_7515_call(), 0)
call_9087 = relay.TupleGetItem(func_7516_call(), 0)
var_9094 = relay.var("var_9094", dtype = "float32", shape = (8, 7, 11))#candidate|9094|(8, 7, 11)|var|float32
bop_9095 = relay.mod(bop_9075.astype('float32'), var_9094.astype('float32')) # shape=(8, 7, 11)
func_3322_call = mod.get_global_var('func_3322')
func_3323_call = mutated_mod.get_global_var('func_3323')
call_9106 = func_3322_call()
call_9107 = func_3322_call()
func_7174_call = mod.get_global_var('func_7174')
func_7177_call = mutated_mod.get_global_var('func_7177')
var_9118 = relay.var("var_9118", dtype = "float64", shape = (176,))#candidate|9118|(176,)|var|float64
call_9117 = relay.TupleGetItem(func_7174_call(relay.reshape(var_9118.astype('float64'), [1, 11, 16])), 0)
call_9119 = relay.TupleGetItem(func_7177_call(relay.reshape(var_9118.astype('float64'), [1, 11, 16])), 0)
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_9122 = relay.TupleGetItem(func_4240_call(), 0)
call_9123 = relay.TupleGetItem(func_4241_call(), 0)
func_3641_call = mod.get_global_var('func_3641')
func_3643_call = mutated_mod.get_global_var('func_3643')
call_9130 = func_3641_call()
call_9131 = func_3641_call()
output = relay.Tuple([call_9026,call_9034,bop_9053,call_9086,bop_9095,call_9106,call_9117,var_9118,call_9122,call_9130,])
output2 = relay.Tuple([call_9027,call_9035,bop_9053,call_9087,bop_9095,call_9107,call_9119,var_9118,call_9123,call_9131,])
func_9144 = relay.Function([var_9013,var_9018,var_9094,var_9118,], output)
mod['func_9144'] = func_9144
mod = relay.transform.InferType()(mod)
mutated_mod['func_9144'] = func_9144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9144_call = mutated_mod.get_global_var('func_9144')
var_9146 = relay.var("var_9146", dtype = "float32", shape = (8, 1, 11))#candidate|9146|(8, 1, 11)|var|float32
var_9147 = relay.var("var_9147", dtype = "bool", shape = (8, 3, 11))#candidate|9147|(8, 3, 11)|var|bool
var_9148 = relay.var("var_9148", dtype = "float32", shape = (8, 7, 11))#candidate|9148|(8, 7, 11)|var|float32
var_9149 = relay.var("var_9149", dtype = "float64", shape = (176,))#candidate|9149|(176,)|var|float64
call_9145 = func_9144_call(var_9146,var_9147,var_9148,var_9149,)
output = call_9145
func_9150 = relay.Function([var_9146,var_9147,var_9148,var_9149,], output)
mutated_mod['func_9150'] = func_9150
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9162 = relay.var("var_9162", dtype = "float32", shape = (9, 3, 16))#candidate|9162|(9, 3, 16)|var|float32
uop_9163 = relay.erf(var_9162.astype('float32')) # shape=(9, 3, 16)
func_9144_call = mod.get_global_var('func_9144')
func_9150_call = mutated_mod.get_global_var('func_9150')
var_9174 = relay.var("var_9174", dtype = "float32", shape = (88,))#candidate|9174|(88,)|var|float32
const_9175 = relay.const([True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True], dtype = "bool")#candidate|9175|(264,)|const|bool
const_9176 = relay.const([[-1.230187,-7.593793],[-9.662592,8.338014],[-0.256419,-8.469216],[8.471110,-3.607258],[8.968606,-9.148145],[3.029037,8.266425],[-0.375646,-5.335513],[9.976230,3.847988],[-4.475085,3.231979],[6.620674,-8.297391],[3.140461,7.351258],[4.135956,8.032161],[0.369783,-4.211413],[6.921227,-4.850036],[-4.517923,6.148073],[-9.484259,-8.753140],[-8.166287,0.195566],[-8.273248,-9.718842],[-9.658273,-3.028016],[9.154709,-8.185583],[4.923223,4.457718],[-7.654100,-9.586861],[4.262964,5.158031],[2.462765,-5.891928],[0.989002,8.846429],[2.067462,9.862393],[6.400277,5.865604],[4.158598,8.824355],[4.730512,2.140918],[-5.302748,-1.650504],[4.686718,-0.271618],[4.160725,1.188887],[-3.291813,-3.376666],[-0.385436,-4.423935],[-3.491433,-5.971175],[5.564882,-8.765218],[-2.972903,3.553416],[-9.781682,-3.483156],[3.659371,-7.869216],[1.895937,1.530495],[-4.364645,3.086070],[7.559684,-7.910810],[-8.269087,3.955248],[8.891540,-8.345299],[0.544732,-2.578640],[0.768063,-1.276617],[4.762256,-7.861295],[-1.220997,3.899922],[4.050379,3.858242],[-8.238560,-9.557123],[-2.122080,-6.371301],[-9.362647,2.538351],[-1.503811,3.906194],[9.639665,-9.249679],[-4.915055,9.637827],[-4.954438,6.671829],[-2.750291,-2.568901],[-3.588105,0.910040],[-5.049968,-3.265351],[-1.261353,1.354076],[-5.317447,-5.681894],[-6.172141,-5.413918],[9.511330,7.529368],[-2.476262,-6.775157],[6.680389,1.060470],[3.230501,-7.508027],[1.945134,-4.789445],[-8.559281,-3.255450],[-6.352868,-6.098182],[-0.306647,2.637494],[4.294742,2.947412],[2.038274,-6.526139],[0.809827,7.495204],[-6.623123,-0.607779],[-7.409581,3.144877],[-6.096038,7.625711],[-7.853152,8.569956],[0.501789,1.746079],[2.523578,-2.795711],[-8.097093,2.636209],[4.535076,-2.738045],[-8.696430,3.966802],[-1.645579,-3.179737],[-0.483233,3.647355],[2.979479,1.426301],[-2.999774,9.540497],[-4.050835,-2.118778],[-6.257571,-4.839644],[-5.438469,0.896207],[6.408425,-1.586188],[8.550263,6.574663],[-5.347308,2.867470],[0.144595,-6.411956],[0.251652,-4.553722],[-3.864198,-4.332689],[-7.512195,-7.261246],[7.424085,-9.940224],[-9.329996,-6.883017],[9.032503,3.231956],[6.702576,8.648698],[-6.064848,-1.285991],[-0.450934,8.089312],[5.290663,7.815681],[-0.024109,8.783880],[-3.295638,-5.446301],[-2.488904,-5.091520],[-7.922518,1.862481],[-4.773462,3.850042],[9.960136,-5.400055],[-5.873656,-3.301303],[3.877060,8.784825],[8.001670,-9.547905],[-4.499596,-5.196927],[4.230927,-1.742285],[-7.301553,4.671529],[1.333257,3.479566],[-5.214107,-7.317763],[4.830915,2.641961],[-6.321739,-1.784603],[0.904987,8.905511],[-2.386676,-6.465970],[5.245000,8.007236],[-4.907101,-5.127230],[9.532481,-3.238361],[-0.282863,-0.796670],[1.335898,-9.542826],[4.066416,7.605866],[0.560061,-6.411561],[-3.842002,-2.983111],[-2.230209,-8.446831],[-3.966009,-1.253891],[-2.735499,-8.100108],[0.689258,7.192710],[-9.279554,-5.389993],[-3.615918,-9.432070],[1.925175,7.639667],[2.718130,7.612536],[-8.030062,-0.921858],[-8.817362,-1.952161],[-5.735047,2.316527],[-4.235572,-4.485729],[3.826352,-3.813529],[9.334572,1.762201],[9.979312,-5.023728],[-7.183777,-7.840308],[9.566740,-6.374153],[0.825308,3.624344],[9.400335,4.114095],[3.336377,-0.159489],[4.978554,-4.920922],[0.942362,8.063339],[4.062786,5.246632],[0.048672,-1.080791],[-5.359772,-3.443948],[0.685663,3.903805],[4.102918,-7.883814],[2.364632,4.269212],[3.177096,8.474094],[1.140310,-3.535932],[-9.743713,8.258682],[5.475983,7.620011],[-5.852284,-4.096661],[2.117751,-8.442893],[-0.117061,2.812087],[9.706394,-7.321009],[-3.051248,8.892898],[-4.357913,-4.714799],[9.524649,-8.146883],[0.366880,-8.983215],[-0.890490,-8.098498],[2.153914,-9.725388],[1.375807,9.680532],[-0.795388,-0.248619],[5.926754,-9.679722],[5.415264,-7.599642],[-4.253021,7.974491],[-4.504949,0.801829],[-2.022966,-8.656999],[-4.434863,-3.687478],[-2.932239,-5.986007],[4.007046,-1.590190],[-2.964868,7.916643],[1.958029,-6.129564],[-3.285126,-2.428223],[-0.953147,0.576349],[4.575456,-4.659095],[-8.113811,9.742859],[-7.668069,9.080630],[-7.789148,-1.400085],[4.481701,-6.643917],[5.362191,-8.912257],[1.790456,0.841469],[4.815086,-8.060988],[-7.338779,-8.167173],[3.998428,-1.953320],[-3.191968,-1.078989],[6.487139,8.075039],[-8.736702,5.079437],[7.045398,3.065867],[-9.560146,-7.621501],[-5.170543,-9.904651],[6.896068,0.458115],[1.143861,-4.601560],[-3.695002,-5.714204],[9.730708,-9.865783],[-2.344890,4.911511],[9.519689,-8.302260],[9.050232,6.101724],[2.188935,6.599498],[8.922960,-5.755288],[-2.007343,-5.890181],[0.345141,-4.618939],[-6.577337,-5.431907],[-2.029580,-8.834205],[-7.920758,-9.240211],[7.012824,0.130124],[1.804376,7.349017],[-9.512283,5.630745],[-0.052767,2.019206],[2.502113,-9.339196],[-6.557085,-5.242907],[4.890089,-9.843374],[2.400199,7.477569],[7.949631,1.073829],[6.555148,2.372334],[-9.178243,-4.205419],[-1.879321,-7.181035],[0.285386,8.581247],[0.799691,7.560264],[3.438515,1.768622],[-8.000541,2.409281],[0.578587,-9.474760],[-0.555814,-1.175892],[5.095911,8.332576],[-2.442964,0.298056],[1.627491,2.063791],[-4.785648,0.582327],[1.105854,-8.936975],[9.295258,7.969258],[-1.182503,-6.377827],[0.874870,-4.749631],[8.541541,-9.046058],[3.948727,-1.912049],[-2.274790,-8.229560],[-5.447854,-5.205908],[-1.308033,4.412201],[6.344014,-6.693354],[-7.344730,-9.290628],[-3.225026,-3.205448],[-0.617248,1.725479],[-3.539679,-9.603746],[-1.983121,0.965751],[-6.859337,-1.607110],[-5.174673,5.196778],[-0.420377,-0.412456],[-0.227076,-7.411842],[8.321722,-5.138152],[1.082996,0.220128],[5.128231,-8.648785],[-8.367739,-2.583165],[-9.049781,5.567388],[-7.519669,-1.640782],[6.384695,-1.531789],[7.439246,-4.035455],[0.748365,-3.655347],[-3.625910,0.329540],[-7.736662,8.702413],[8.139941,5.122639],[-5.541781,1.097438],[9.774147,5.474704],[-2.048425,-4.660952],[-6.334002,-4.140164],[-8.168790,-3.375660],[-0.649086,-1.247859],[-7.004012,-6.559908],[-0.780612,0.065655],[-2.243699,8.024289],[-8.324449,-5.180905],[-4.859005,-9.525337],[6.986845,5.937499],[9.745867,5.441829],[9.407833,-9.201545],[4.141659,6.990487],[4.588674,8.644917],[2.311082,7.315371],[4.607444,-6.731804],[5.752449,3.272860],[4.093926,-9.198500],[-2.281445,3.013505],[8.094080,5.847190],[-8.064301,-1.039844],[9.326925,6.018237],[6.521248,-7.641157],[4.426419,-9.311379],[8.872569,8.697857],[-9.651891,-6.106029],[4.685748,-8.452439],[9.038075,-8.068577],[1.683488,9.447307],[-2.420068,7.650995],[-3.205777,-8.138594],[3.251955,-2.835388],[-2.561851,4.555653],[1.248523,-7.081403],[0.162771,5.038506],[-9.423432,-4.509184],[9.660427,5.032437],[4.938093,2.149672]], dtype = "float32")#candidate|9176|(308, 2)|const|float32
var_9177 = relay.var("var_9177", dtype = "float64", shape = (176,))#candidate|9177|(176,)|var|float64
call_9173 = relay.TupleGetItem(func_9144_call(relay.reshape(var_9174.astype('float32'), [8, 1, 11]), relay.reshape(const_9175.astype('bool'), [8, 3, 11]), relay.reshape(const_9176.astype('float32'), [8, 7, 11]), relay.reshape(var_9177.astype('float64'), [176,]), ), 5)
call_9178 = relay.TupleGetItem(func_9150_call(relay.reshape(var_9174.astype('float32'), [8, 1, 11]), relay.reshape(const_9175.astype('bool'), [8, 3, 11]), relay.reshape(const_9176.astype('float32'), [8, 7, 11]), relay.reshape(var_9177.astype('float64'), [176,]), ), 5)
func_5292_call = mod.get_global_var('func_5292')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_9186 = func_5292_call()
call_9187 = func_5292_call()
output = relay.Tuple([uop_9163,call_9173,var_9174,const_9175,const_9176,var_9177,call_9186,])
output2 = relay.Tuple([uop_9163,call_9178,var_9174,const_9175,const_9176,var_9177,call_9187,])
func_9192 = relay.Function([var_9162,var_9174,var_9177,], output)
mod['func_9192'] = func_9192
mod = relay.transform.InferType()(mod)
mutated_mod['func_9192'] = func_9192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9192_call = mutated_mod.get_global_var('func_9192')
var_9194 = relay.var("var_9194", dtype = "float32", shape = (9, 3, 16))#candidate|9194|(9, 3, 16)|var|float32
var_9195 = relay.var("var_9195", dtype = "float32", shape = (88,))#candidate|9195|(88,)|var|float32
var_9196 = relay.var("var_9196", dtype = "float64", shape = (176,))#candidate|9196|(176,)|var|float64
call_9193 = func_9192_call(var_9194,var_9195,var_9196,)
output = call_9193
func_9197 = relay.Function([var_9194,var_9195,var_9196,], output)
mutated_mod['func_9197'] = func_9197
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9213 = relay.var("var_9213", dtype = "int8", shape = (4, 12, 6))#candidate|9213|(4, 12, 6)|var|int8
var_9214 = relay.var("var_9214", dtype = "int8", shape = (4, 12, 6))#candidate|9214|(4, 12, 6)|var|int8
bop_9215 = relay.maximum(var_9213.astype('int8'), relay.reshape(var_9214.astype('int8'), relay.shape_of(var_9213))) # shape=(4, 12, 6)
output = bop_9215
output2 = bop_9215
func_9220 = relay.Function([var_9213,var_9214,], output)
mod['func_9220'] = func_9220
mod = relay.transform.InferType()(mod)
mutated_mod['func_9220'] = func_9220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9220_call = mutated_mod.get_global_var('func_9220')
var_9222 = relay.var("var_9222", dtype = "int8", shape = (4, 12, 6))#candidate|9222|(4, 12, 6)|var|int8
var_9223 = relay.var("var_9223", dtype = "int8", shape = (4, 12, 6))#candidate|9223|(4, 12, 6)|var|int8
call_9221 = func_9220_call(var_9222,var_9223,)
output = call_9221
func_9224 = relay.Function([var_9222,var_9223,], output)
mutated_mod['func_9224'] = func_9224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4307_call = mod.get_global_var('func_4307')
func_4309_call = mutated_mod.get_global_var('func_4309')
call_9245 = func_4307_call()
call_9246 = func_4307_call()
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
const_9253 = relay.const([-0.834941,-8.636036,-6.009535,-2.945396,4.076220,2.468701,-5.127333,-3.420280,2.345780,5.875968,-5.875381,-2.945533,7.297633,9.945546,-0.408466,-1.375029,3.341133,-2.879862,3.088849,0.788134,9.192747,-8.842806,-4.651419,2.324612,3.232250,-1.157669,0.421599,4.812672,-7.788502,3.315963,-4.331142,2.486393,-9.607930,4.763297,-6.482279,-9.338057,-0.068677,1.105873,-0.360433,-7.566283,4.929112,8.548172,1.858656,3.940777,-0.417428,9.938893,5.688575,-2.008122,-7.547269,5.502629,-2.949340,-7.046567,-6.457959,-9.767955,-6.916974,7.970992,6.563597,-7.647703,1.861485,-1.989422,-8.244981,2.646079,5.237503,-6.929901,4.690531,-9.305399,6.143638,-1.414942,4.203153,-8.256421,-6.648279,2.228878,7.575695,-0.808783,-5.352117,-5.150292,-4.781459,-7.413625,1.129789,-5.144453,-2.777884,2.181195,6.322544,9.270903,-3.289135,1.643687,3.391151,-3.591745,-6.140536,-3.085146,-4.396464,-9.501614,-9.459462,-8.052037,1.233979,-0.891905,3.049875,2.070302,-2.801904,3.503654,3.743763,8.815584,-7.152154,8.955059,-2.653744,4.455576,-1.983651,-6.258314,-4.963136,-8.984952,3.782078,7.374681,-0.516440,5.427402,6.016142,6.396703,8.843235,-1.320947,8.906204,6.613865,6.284340,-7.413526,-0.897803,-2.678455,5.034098,-3.291964,1.202902,9.769964,-7.529944,-3.530108,-8.166777,-8.876959,-0.174216,2.731262,-8.029497,-1.096514,0.060516,1.004345,2.403123,-2.498537,2.295520,8.179623,-4.729754,-6.721207,5.001450,-9.666771,1.586654,-3.016152,1.550332,0.973659,-0.548791,2.769793,-8.501167,2.405479,-4.935576,-2.479102,-2.690258,9.407210,-2.862598,0.959525,-9.885668,7.739741,3.350883,-5.536850,3.572933,-5.112186,9.385041,8.336129,4.233593,7.215626,-2.492745,0.645869,3.263455,5.987787,-5.610598,8.507837,2.947407,-0.010123,-3.154012,7.414727,-4.830820,0.331162,-2.452824,3.847352,5.445455,0.530206,-9.094427,-1.045321,8.309187,-5.506583,4.669057,2.562211,-3.908605,9.397841,-9.040786,4.152445,-0.336321,-3.078679,7.331199,-4.195641,-4.710285,6.618781,-9.121456,-6.804052,2.532894,-6.611648,-2.207224,2.207991,5.444559,-6.635944,-2.835838,7.131665,-5.638925,5.416549,9.552356,5.929882,7.346483,8.160609,-5.621599,-0.220835,-6.020446,-5.686253,-1.800999,0.183394,-0.410889,5.680361,4.270243,-9.367846,-5.062178,-0.087764,6.194915,2.711741,-6.318897,6.651997,-6.105848,-2.198673,-8.650603,1.516988,0.048810,-7.311314,-3.595502,-3.902268,-9.550983,-3.609306,-9.332626,7.906082,-2.718490,-3.119094,7.678420,3.725660,9.304453,-3.987239,1.416094,-9.779120,-3.201980,-6.524314,-2.543153,6.528739,0.614702,6.216659,-8.186372,-1.444344,6.712556,3.155277,-1.928455,-1.057109,-9.957448,2.724479,8.903050,-0.514694,-3.224414,-6.467835,8.636991,-8.777930,5.102954,-5.001429,-3.995668,-7.396289,-6.116563,-2.947380,1.642805,-5.667818,9.046012,0.230562,-8.593582,-5.797385,-0.178498,5.111193,-2.883267,8.771150,-5.296538,8.595816,-2.988211,-1.878133,4.038939,5.979568,-5.283314,5.980207,4.493687,-8.419970,-0.179149,-3.158169,2.324441,4.654972,8.220154,-2.479605,-7.334878,-3.115041,2.649152,8.543263,2.827611,3.100881,1.521473,5.241227,5.368995,-0.675435,5.990426,3.649912,-0.467547,-3.974443,2.726496,3.846229,7.653057,-6.758278,8.331155,2.983797,-3.727328,-9.507119,9.200475,-1.837774,3.525466,1.801012,6.955904,3.628306,6.812911,-0.385108,-9.286509,-8.048373,9.048809,7.592561,0.575269,-4.303949,3.601718,3.704633,-5.126977,-0.943502,-7.491420,-6.445165,-9.800262,6.602586,-0.848121,-4.344486,-3.606359,-9.734911,1.100745,-7.468458,-1.887645,-9.556138,0.298245,6.932347,3.734557,6.821005,4.000779,0.870116,3.636386,8.005709,-5.318172,0.782377,-6.756080,0.271290,4.894576,-0.614570,-9.881537,1.329016,-7.678349,5.446635,-7.323776,6.880405,3.107566,0.934841,-4.424918,-9.132482,-4.851487,3.111255,5.499630,-1.749806,-1.849723,-1.388853,6.559263,-3.781370,-7.237221,7.371646,-4.121856,-0.471947,-9.116780,-3.796834,-3.473211,6.445894,-9.964277,-6.248551,6.832367,-9.376529,1.693017,-7.152114,8.046107,6.733203,1.053227,-3.981494,9.787044,2.857565,1.542347,-1.206351,-4.497558,-7.101059,-9.758794,-5.907221,-3.285894,2.419015,7.822013,-1.408317,-3.121734,2.051677,6.108091,4.036326,-2.287516,-5.765488,4.366396,-3.469802,-4.052066,-0.929385,1.559711,4.979278,-5.563979,6.034324,-4.916094,-8.979834,4.874799,-7.350804,5.049723,-6.200921,-4.377727,5.487454,6.568535,8.860319,4.486755,2.066036,-2.706800,-3.147633,8.405572,6.617423,0.275549,7.958554,5.057727,3.810574,9.062104,-8.808642,-7.994168,0.599598,3.618531,-0.109475,9.618624,6.326077,-7.731214,-4.698839,-7.535125,4.229889,0.968788,-1.090703,1.100172,4.135704,9.394181,-1.853194,-7.700061,-7.159861,7.967610,-1.678493,-5.397526,-2.359506,5.394182,-4.311326,-9.256924,3.872656,-8.991646,-1.641683,-6.566735,1.303029,-7.932895,8.747384,7.438988,-3.150949,-5.142035,4.081691,1.327136,8.767570,-8.757617,-1.810292,-4.322607,-8.671147,8.638286,-1.108834,4.711131,-3.907262,0.875055,-1.963536,0.273237,7.403293,6.659985,-4.112457,7.101812,6.639902,2.068298,-4.798402,3.213477,0.353911,-5.074589,-1.605012,6.675704,7.200588,8.676075,3.066609,-0.405239,-8.030223,-1.484864,-7.085007,4.846126,9.710400,3.921858,-9.409825,9.123436,-3.269750,9.780591,9.732676,5.422901,5.946598,-6.197822,2.851592,-8.638346,-7.316546,-8.528189,-9.588263,-3.787582,-4.023937,9.621405,-5.825715,-8.450709,-2.734158,-7.381535,-6.521932,-9.383200,-8.787934,5.407166,-9.402650,2.170672,-3.191801,2.328416,1.639002,-3.909452,-1.746752,-2.044679,-0.559571,7.122427,-8.931385,-5.420906,3.894419,8.255265,4.702251,5.576429,-5.961772,-0.854122,-1.698664,9.713310,2.141489,6.018254,3.314108,5.976368,2.732779,2.607199,-6.863651,-0.054051,-6.529765,0.071110,-6.461535,9.775362,2.998535,6.907334,-0.169193,-7.262802,9.298499,5.658373,8.206898,-9.909029,4.519842,8.678680,-1.405128,7.989011,1.945219,-7.566768,3.354086,-0.740512,-9.488908,-5.813241,-1.236669,-6.238689,-0.808842,-8.377523,-1.102021,-2.699958,-2.454999,6.860996,-7.343747,-7.608613,4.458547,7.311581,-3.724455,-1.690910,-2.842153,5.538859,7.319009,-0.713771,4.531067,9.792656,2.434718,0.966354,2.993948,-9.005949,8.078305,6.898996,-5.815322,7.689507,-4.211422,0.047212,-9.628171,2.532176,-0.979432,-4.969967,2.956830,-2.240412,4.757077,-5.060500,-9.669236,-1.606876,5.781369,6.844580,4.959854,3.766013,-6.600856,-2.506868,9.505379,-9.187549,1.108238,-4.069119,-7.815575,9.224946,-8.318921,5.661810,3.434042,5.819730,6.483117,-2.593023,4.847170,2.463086,-2.875198,8.418798,3.358765,3.854878,-2.846532,4.677552,-7.549221,-8.430864,5.760616,-7.463122,-2.805794,4.587580,-2.014082,-7.503548,0.020040,1.501114,4.932964,-4.645247,-7.827934,0.748569,2.551646,4.919930,5.050342,-3.794103,4.816653,0.984433,-1.951240,-3.195399,-1.632743,2.457546,-1.519340,2.926445,1.055920,-8.718018,-1.888337,-5.098431,4.129635,4.092670,2.882793,8.597958,-2.092810,-3.894459,1.053532,3.761439,4.105381,-6.370661,2.859825,5.616107,5.686517,-1.994850,1.691866,6.038046,9.837634,-7.759248,-2.050949,5.665984,-8.820250,-8.210643,-0.443075,-5.272502,-8.488318,9.561050,-0.039746,-6.646536,5.329708,4.067557,7.770968,3.732439,-2.393785,2.182960,7.963557,3.936418,4.877126,4.132369,-7.218956,9.627427,-1.253249,-5.985796,-4.791378,-4.375185,-0.813793,-4.623220,-4.307769,-1.262744,6.399956,-1.458161,-2.594344,7.092151,6.889719,-8.626112,-5.531393,-4.346745,-5.138353,3.612675,5.344437,-1.659418,-6.934051,1.385579,-5.495523,0.195236,3.857547,-4.411943,7.519510,5.651915,1.708819,-8.676354,-0.192021,-5.307515,-9.565567,0.017169,-7.971850,9.342872,-1.075995,0.037278,-8.366568,2.050287,-8.090296,7.626186,5.008701,-9.628364,-4.244626,-8.419309,6.387550,-4.289976,-9.365308,2.293554,1.993260,1.239887,1.508339,2.710973,1.267176,-5.812850,-0.464273,-3.500936,-5.196931,-5.290611,3.582174,3.890628,-7.508692,-1.841484,8.888036,7.206359,-5.692414,8.168849,0.540964,3.364971,5.425949,6.219393,-7.610616,9.730043,-8.655463,7.699985,-2.110912,0.135439,-2.843582,2.425960,8.110322,2.551784,-8.108292,-4.236164,5.255930,-3.087906,9.709904,-3.130907,8.354200,-7.699438,-7.369539,-9.220711,2.813461,3.246012,9.408395], dtype = "float64")#candidate|9253|(832,)|const|float64
call_9252 = relay.TupleGetItem(func_5442_call(relay.reshape(const_9253.astype('float64'), [104, 8])), 1)
call_9254 = relay.TupleGetItem(func_5444_call(relay.reshape(const_9253.astype('float64'), [104, 8])), 1)
func_4958_call = mod.get_global_var('func_4958')
func_4960_call = mutated_mod.get_global_var('func_4960')
const_9256 = relay.const([1.894188,6.750516,5.081047,-2.390031,9.531805,2.444672,8.653409,-0.682348,7.260100,-9.853639,5.521389,4.222434,-6.803662,-4.389117,-6.786363,-3.934179,2.503861,-7.175407,-0.703968,-7.081379,-6.902010,1.969664,0.417171,-5.346663,7.012657,4.036554,-5.667163,0.797459,7.986616,2.937451,9.124770,-3.443165,7.277344,-7.171217,8.797799,-1.073959,-0.851615,9.200881,3.980860,-6.883314,1.403448,4.440453,-1.881579,-2.619696,-5.780774,-7.246344,-1.993698,4.863883,8.120018,8.593496,-1.802530,-2.450048,1.705239,-6.776318,1.571606,6.169588,-8.985784,1.060957,5.481906,9.893072,3.679041,0.474415,-8.857979,7.878780,-2.241818,-1.200014,-1.026815,0.197849,2.426990,8.782596,-1.550515,7.245856,4.419807,-4.831738,-4.416313,9.680882,7.657825,4.685015,5.943918,8.207026,0.346623,-1.708009,1.422424,7.118198,1.241657,2.881824,8.027781,-2.141943,6.235519,4.832758,-9.209934,6.378760,-1.132389,5.979580,-6.359836,3.349839,8.638757,3.957173,-4.966111,9.606736,8.280407,6.819134,6.271540,-7.011571,-0.666144,-8.327921,-9.866480,-7.693608,2.298288,-0.393490,7.109063,1.266773,2.972400,1.493931,-3.553759,8.066358,0.479358,-7.415574,-3.035715,-7.552160,1.035074,-5.850192,-7.643558,-9.905598,-4.906898,4.109682,-5.572591,-2.162968,-6.781614,1.839224,-6.934063,-7.451555,-1.115646,-5.933919,7.127291,9.740196,-4.045210,-5.477281,8.623328,-1.023555,4.535182,3.592343,-5.703530,5.173649,0.353019,3.825563,1.387912,9.575245,9.326444,9.915835,-5.502349,8.215089,-7.409674,-3.259787,-0.024896,6.292412,-2.952576,9.392675,1.373552,9.342973,-9.922632,-5.888877,5.661078,7.262129,-3.893603,5.814530,3.288267,6.115953], dtype = "float32")#candidate|9256|(168,)|const|float32
call_9255 = relay.TupleGetItem(func_4958_call(relay.reshape(const_9256.astype('float32'), [84, 2])), 1)
call_9257 = relay.TupleGetItem(func_4960_call(relay.reshape(const_9256.astype('float32'), [84, 2])), 1)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_9261 = relay.TupleGetItem(func_2467_call(), 0)
call_9262 = relay.TupleGetItem(func_2468_call(), 0)
output = relay.Tuple([call_9245,call_9252,const_9253,call_9255,const_9256,call_9261,])
output2 = relay.Tuple([call_9246,call_9254,const_9253,call_9257,const_9256,call_9262,])
func_9270 = relay.Function([], output)
mod['func_9270'] = func_9270
mod = relay.transform.InferType()(mod)
mutated_mod['func_9270'] = func_9270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9270_call = mutated_mod.get_global_var('func_9270')
call_9271 = func_9270_call()
output = call_9271
func_9272 = relay.Function([], output)
mutated_mod['func_9272'] = func_9272
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1618_call = mod.get_global_var('func_1618')
func_1619_call = mutated_mod.get_global_var('func_1619')
call_9284 = func_1618_call()
call_9285 = func_1618_call()
func_4767_call = mod.get_global_var('func_4767')
func_4769_call = mutated_mod.get_global_var('func_4769')
const_9292 = relay.const([[-6.371229,2.093318,0.755476,4.661594,-6.058928,-0.746368,4.285755,8.044125,4.257267,-1.721774,6.779816,3.981628,-6.604614,-6.733206,-9.235642,0.307725,8.828504,-3.581095,0.267798,-8.038036,-2.428921,3.883972,-0.490597,6.680341,5.101769,4.548324,0.350135,-0.193909,7.328886,-4.227043,-2.861303,8.756998,2.270537,-9.648057,4.201658,-5.197924,4.076506,4.130021,-0.502478,-4.961489,0.955012,7.976801,-7.353553,-5.765669,-3.626893,5.571842,2.373235,-3.641955,-5.377234,3.806464,-2.429335,-9.726031,8.777843,2.376098,-3.984770,3.314433,0.894697,0.404611,-0.751789,-6.835054,-2.408039,7.041333,-8.922822,-7.626284,6.615614,-9.563513,-5.744986,7.600515,1.089982,1.247886,-6.014467,8.256601,5.383662,-2.306598,-4.121905,-2.945881,-2.426868,-2.983075,-3.538197,-6.295066,-0.374750,8.429393,9.921034,-8.090438,3.627947,-2.569752,8.015668,-0.993368,-8.020480,-7.664760,5.178409,-4.079012,4.980173,-1.701096,9.261114,0.946847,8.452254,-2.372802,5.016710,7.157064,7.508696,1.514521,4.623538,2.457746,-0.468916,4.770257,4.663955,1.762112,-3.729471,-2.434547,-8.803053,-0.039061,-7.518441,-7.898138,8.806041,-9.612291,-9.475193,6.044965,3.945881,6.982829,2.707542,8.942021,-8.166287,3.652567,-1.265577,1.156399,7.502256,3.067287,-2.868941,2.280185,9.243647,-5.118985,5.868165,-4.481702,1.260026,-8.181497,-8.484600,0.205784,6.918829,3.393141,-7.048582,-6.795425,-0.304907,8.567527,-8.900329,4.767997,-2.372449,6.377156,7.768823,1.352594,6.179285,8.242186,4.562382,1.999411,1.998573,9.707886,2.598257,0.694622,4.911120,-9.865568,-9.594886,7.028969,-5.392783,-3.638249,-6.809547,-3.808177,-1.408032,7.755249]], dtype = "float32")#candidate|9292|(1, 168)|const|float32
call_9291 = func_4767_call(relay.reshape(const_9292.astype('float32'), [7, 8, 3]))
call_9293 = func_4767_call(relay.reshape(const_9292.astype('float32'), [7, 8, 3]))
func_3863_call = mod.get_global_var('func_3863')
func_3865_call = mutated_mod.get_global_var('func_3865')
var_9299 = relay.var("var_9299", dtype = "int8", shape = (352,))#candidate|9299|(352,)|var|int8
call_9298 = relay.TupleGetItem(func_3863_call(relay.reshape(var_9299.astype('int8'), [352,])), 1)
call_9300 = relay.TupleGetItem(func_3865_call(relay.reshape(var_9299.astype('int8'), [352,])), 1)
func_1454_call = mod.get_global_var('func_1454')
func_1456_call = mutated_mod.get_global_var('func_1456')
call_9304 = relay.TupleGetItem(func_1454_call(), 0)
call_9305 = relay.TupleGetItem(func_1456_call(), 0)
func_8061_call = mod.get_global_var('func_8061')
func_8065_call = mutated_mod.get_global_var('func_8065')
const_9309 = relay.const([-3,-7,-9,9,-9,-1,-9,4,-2,5,8,-9,10,3,1,3,-4,5,1,9,6,-6,-4,-8,-1,-4,9,-9,9,-8,4,4,-4,-3,-6,6,4,-8,-2,-5,-1,1,2,10,-4,4,2,5,-9,-10,5,-9,-9,7,5,-2,1,-10,-3,-6,9,-4,8,-4,2,-1], dtype = "int16")#candidate|9309|(66,)|const|int16
call_9308 = func_8061_call(relay.reshape(const_9309.astype('int16'), [2, 11, 3]), relay.reshape(const_9309.astype('int16'), [2, 11, 3]), )
call_9310 = func_8061_call(relay.reshape(const_9309.astype('int16'), [2, 11, 3]), relay.reshape(const_9309.astype('int16'), [2, 11, 3]), )
output = relay.Tuple([call_9284,call_9291,const_9292,call_9298,var_9299,call_9304,call_9308,const_9309,])
output2 = relay.Tuple([call_9285,call_9293,const_9292,call_9300,var_9299,call_9305,call_9310,const_9309,])
func_9313 = relay.Function([var_9299,], output)
mod['func_9313'] = func_9313
mod = relay.transform.InferType()(mod)
var_9314 = relay.var("var_9314", dtype = "int8", shape = (352,))#candidate|9314|(352,)|var|int8
output = func_9313(var_9314)
func_9315 = relay.Function([var_9314], output)
mutated_mod['func_9315'] = func_9315
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6949_call = mod.get_global_var('func_6949')
func_6951_call = mutated_mod.get_global_var('func_6951')
call_9323 = relay.TupleGetItem(func_6949_call(), 1)
call_9324 = relay.TupleGetItem(func_6951_call(), 1)
output = relay.Tuple([call_9323,])
output2 = relay.Tuple([call_9324,])
func_9336 = relay.Function([], output)
mod['func_9336'] = func_9336
mod = relay.transform.InferType()(mod)
output = func_9336()
func_9337 = relay.Function([], output)
mutated_mod['func_9337'] = func_9337
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9336_call = mod.get_global_var('func_9336')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_9347 = relay.TupleGetItem(func_9336_call(), 0)
call_9348 = relay.TupleGetItem(func_9337_call(), 0)
func_4958_call = mod.get_global_var('func_4958')
func_4960_call = mutated_mod.get_global_var('func_4960')
const_9355 = relay.const([[-5.939121,-1.075319,-3.042916,9.356945,1.082112,-4.434468,2.221055,-2.350629,1.049065,2.413241,-0.465330,-7.649330,-8.462322,-5.380732,9.895676,-7.649209,2.254094,-2.341598,4.459454,-1.667866,-0.038423,-8.368623,-6.559633,0.301875,7.193637,-9.623596,4.397650,2.657323,8.105142,0.187995,2.129140,-6.008727,-0.008940,-5.455800,-5.990965,-8.737383,4.234014,-3.262124,3.568141,9.412842,6.865719,7.755305,5.279002,-1.415344,-5.315090,0.042310,-1.498361,-3.562429,-3.793200,-3.906206,3.237663,3.200775,-6.353680,-3.125795,0.985035,-9.131091],[-2.422374,-4.984977,-9.567071,-9.318484,-8.851277,-3.030884,8.357467,1.896824,-5.486865,-6.793048,2.477862,-0.340584,-0.214540,0.542910,0.969046,-7.209547,9.338605,0.694930,7.654548,4.075247,0.498792,-9.525970,-0.280336,2.035878,-8.553673,5.286994,5.589815,0.243665,-2.938905,-5.166928,-9.053899,7.054033,0.268685,0.253340,-9.913376,-5.431894,5.698656,-5.565611,-9.548905,-1.089183,-5.566717,-2.808886,7.924159,2.166593,5.002738,8.185578,-5.896977,0.952483,9.678634,-8.574340,4.431461,-8.606723,-1.855706,3.431389,-0.349759,8.874126],[1.303116,-7.627822,2.322188,-2.636339,3.255425,-7.727640,4.853680,4.313251,-4.678731,-0.837236,-2.914163,-4.752217,-3.320284,-0.968646,4.893826,5.502169,0.660279,-5.740546,3.978657,5.665301,-2.748758,-0.553556,-4.055474,1.116373,8.168520,-5.785676,-5.091308,-5.165318,-4.616078,3.776055,-2.745526,-8.769838,-3.623102,-0.543029,-7.867145,5.709921,8.260104,-5.127984,8.357664,3.144610,2.374733,5.235702,-1.963235,-4.412638,-7.388062,6.538116,-2.684400,-3.792775,-2.456851,-9.523490,2.651797,6.615920,6.657907,-7.769752,8.535486,-8.682003]], dtype = "float32")#candidate|9355|(3, 56)|const|float32
call_9354 = relay.TupleGetItem(func_4958_call(relay.reshape(const_9355.astype('float32'), [84, 2])), 1)
call_9356 = relay.TupleGetItem(func_4960_call(relay.reshape(const_9355.astype('float32'), [84, 2])), 1)
output = relay.Tuple([call_9347,call_9354,const_9355,])
output2 = relay.Tuple([call_9348,call_9356,const_9355,])
func_9358 = relay.Function([], output)
mod['func_9358'] = func_9358
mod = relay.transform.InferType()(mod)
mutated_mod['func_9358'] = func_9358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9358_call = mutated_mod.get_global_var('func_9358')
call_9359 = func_9358_call()
output = call_9359
func_9360 = relay.Function([], output)
mutated_mod['func_9360'] = func_9360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_9394 = relay.TupleGetItem(func_1145_call(), 0)
call_9395 = relay.TupleGetItem(func_1147_call(), 0)
func_1618_call = mod.get_global_var('func_1618')
func_1619_call = mutated_mod.get_global_var('func_1619')
call_9398 = func_1618_call()
call_9399 = func_1618_call()
func_1337_call = mod.get_global_var('func_1337')
func_1338_call = mutated_mod.get_global_var('func_1338')
call_9408 = relay.TupleGetItem(func_1337_call(), 0)
call_9409 = relay.TupleGetItem(func_1338_call(), 0)
func_4448_call = mod.get_global_var('func_4448')
func_4449_call = mutated_mod.get_global_var('func_4449')
call_9412 = relay.TupleGetItem(func_4448_call(), 1)
call_9413 = relay.TupleGetItem(func_4449_call(), 1)
output = relay.Tuple([call_9394,call_9398,call_9408,call_9412,])
output2 = relay.Tuple([call_9395,call_9399,call_9409,call_9413,])
func_9421 = relay.Function([], output)
mod['func_9421'] = func_9421
mod = relay.transform.InferType()(mod)
output = func_9421()
func_9422 = relay.Function([], output)
mutated_mod['func_9422'] = func_9422
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6806_call = mod.get_global_var('func_6806')
func_6807_call = mutated_mod.get_global_var('func_6807')
call_9494 = relay.TupleGetItem(func_6806_call(), 0)
call_9495 = relay.TupleGetItem(func_6807_call(), 0)
func_5196_call = mod.get_global_var('func_5196')
func_5197_call = mutated_mod.get_global_var('func_5197')
call_9511 = func_5196_call()
call_9512 = func_5196_call()
func_9336_call = mod.get_global_var('func_9336')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_9546 = relay.TupleGetItem(func_9336_call(), 0)
call_9547 = relay.TupleGetItem(func_9337_call(), 0)
func_7530_call = mod.get_global_var('func_7530')
func_7532_call = mutated_mod.get_global_var('func_7532')
var_9555 = relay.var("var_9555", dtype = "float64", shape = (660, 1))#candidate|9555|(660, 1)|var|float64
call_9554 = relay.TupleGetItem(func_7530_call(relay.reshape(var_9555.astype('float64'), [10, 11, 6])), 0)
call_9556 = relay.TupleGetItem(func_7532_call(relay.reshape(var_9555.astype('float64'), [10, 11, 6])), 0)
func_5747_call = mod.get_global_var('func_5747')
func_5750_call = mutated_mod.get_global_var('func_5750')
call_9577 = relay.TupleGetItem(func_5747_call(relay.reshape(call_9511.astype('float64'), [2, 12, 9])), 0)
call_9578 = relay.TupleGetItem(func_5750_call(relay.reshape(call_9511.astype('float64'), [2, 12, 9])), 0)
output = relay.Tuple([call_9494,call_9511,call_9546,call_9554,var_9555,call_9577,])
output2 = relay.Tuple([call_9495,call_9512,call_9547,call_9556,var_9555,call_9578,])
func_9585 = relay.Function([var_9555,], output)
mod['func_9585'] = func_9585
mod = relay.transform.InferType()(mod)
var_9586 = relay.var("var_9586", dtype = "float64", shape = (660, 1))#candidate|9586|(660, 1)|var|float64
output = func_9585(var_9586)
func_9587 = relay.Function([var_9586], output)
mutated_mod['func_9587'] = func_9587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4985_call = mod.get_global_var('func_4985')
func_4987_call = mutated_mod.get_global_var('func_4987')
call_9592 = func_4985_call()
call_9593 = func_4985_call()
output = call_9592
output2 = call_9593
func_9601 = relay.Function([], output)
mod['func_9601'] = func_9601
mod = relay.transform.InferType()(mod)
mutated_mod['func_9601'] = func_9601
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9601_call = mutated_mod.get_global_var('func_9601')
call_9602 = func_9601_call()
output = call_9602
func_9603 = relay.Function([], output)
mutated_mod['func_9603'] = func_9603
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_9617 = relay.TupleGetItem(func_4240_call(), 0)
call_9618 = relay.TupleGetItem(func_4241_call(), 0)
output = relay.Tuple([call_9617,])
output2 = relay.Tuple([call_9618,])
func_9641 = relay.Function([], output)
mod['func_9641'] = func_9641
mod = relay.transform.InferType()(mod)
mutated_mod['func_9641'] = func_9641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9641_call = mutated_mod.get_global_var('func_9641')
call_9642 = func_9641_call()
output = call_9642
func_9643 = relay.Function([], output)
mutated_mod['func_9643'] = func_9643
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9336_call = mod.get_global_var('func_9336')
func_9337_call = mutated_mod.get_global_var('func_9337')
call_9644 = relay.TupleGetItem(func_9336_call(), 0)
call_9645 = relay.TupleGetItem(func_9337_call(), 0)
func_3863_call = mod.get_global_var('func_3863')
func_3865_call = mutated_mod.get_global_var('func_3865')
var_9684 = relay.var("var_9684", dtype = "int8", shape = (352,))#candidate|9684|(352,)|var|int8
call_9683 = relay.TupleGetItem(func_3863_call(relay.reshape(var_9684.astype('int8'), [352,])), 0)
call_9685 = relay.TupleGetItem(func_3865_call(relay.reshape(var_9684.astype('int8'), [352,])), 0)
output = relay.Tuple([call_9644,call_9683,var_9684,])
output2 = relay.Tuple([call_9645,call_9685,var_9684,])
func_9695 = relay.Function([var_9684,], output)
mod['func_9695'] = func_9695
mod = relay.transform.InferType()(mod)
mutated_mod['func_9695'] = func_9695
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9696 = relay.var("var_9696", dtype = "int8", shape = (352,))#candidate|9696|(352,)|var|int8
func_9695_call = mutated_mod.get_global_var('func_9695')
call_9697 = func_9695_call(var_9696)
output = call_9697
func_9698 = relay.Function([var_9696], output)
mutated_mod['func_9698'] = func_9698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_762_call = mod.get_global_var('func_762')
func_764_call = mutated_mod.get_global_var('func_764')
call_9747 = relay.TupleGetItem(func_762_call(), 1)
call_9748 = relay.TupleGetItem(func_764_call(), 1)
func_6350_call = mod.get_global_var('func_6350')
func_6352_call = mutated_mod.get_global_var('func_6352')
call_9765 = func_6350_call()
call_9766 = func_6350_call()
func_6401_call = mod.get_global_var('func_6401')
func_6402_call = mutated_mod.get_global_var('func_6402')
call_9768 = relay.TupleGetItem(func_6401_call(), 0)
call_9769 = relay.TupleGetItem(func_6402_call(), 0)
output = relay.Tuple([call_9747,call_9765,call_9768,])
output2 = relay.Tuple([call_9748,call_9766,call_9769,])
func_9795 = relay.Function([], output)
mod['func_9795'] = func_9795
mod = relay.transform.InferType()(mod)
output = func_9795()
func_9796 = relay.Function([], output)
mutated_mod['func_9796'] = func_9796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8673_call = mod.get_global_var('func_8673')
func_8675_call = mutated_mod.get_global_var('func_8675')
call_9842 = relay.TupleGetItem(func_8673_call(), 0)
call_9843 = relay.TupleGetItem(func_8675_call(), 0)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_9846 = relay.TupleGetItem(func_2925_call(), 0)
call_9847 = relay.TupleGetItem(func_2927_call(), 0)
output = relay.Tuple([call_9842,call_9846,])
output2 = relay.Tuple([call_9843,call_9847,])
func_9851 = relay.Function([], output)
mod['func_9851'] = func_9851
mod = relay.transform.InferType()(mod)
output = func_9851()
func_9852 = relay.Function([], output)
mutated_mod['func_9852'] = func_9852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8594_call = mod.get_global_var('func_8594')
func_8596_call = mutated_mod.get_global_var('func_8596')
call_9907 = relay.TupleGetItem(func_8594_call(), 0)
call_9908 = relay.TupleGetItem(func_8596_call(), 0)
output = call_9907
output2 = call_9908
func_9915 = relay.Function([], output)
mod['func_9915'] = func_9915
mod = relay.transform.InferType()(mod)
mutated_mod['func_9915'] = func_9915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9915_call = mutated_mod.get_global_var('func_9915')
call_9916 = func_9915_call()
output = call_9916
func_9917 = relay.Function([], output)
mutated_mod['func_9917'] = func_9917
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9970 = relay.var("var_9970", dtype = "float32", shape = (6, 7, 6))#candidate|9970|(6, 7, 6)|var|float32
uop_9971 = relay.erf(var_9970.astype('float32')) # shape=(6, 7, 6)
uop_9978 = relay.asinh(uop_9971.astype('float64')) # shape=(6, 7, 6)
func_1322_call = mod.get_global_var('func_1322')
func_1323_call = mutated_mod.get_global_var('func_1323')
call_9986 = relay.TupleGetItem(func_1322_call(), 0)
call_9987 = relay.TupleGetItem(func_1323_call(), 0)
output = relay.Tuple([uop_9978,call_9986,])
output2 = relay.Tuple([uop_9978,call_9987,])
func_9991 = relay.Function([var_9970,], output)
mod['func_9991'] = func_9991
mod = relay.transform.InferType()(mod)
var_9992 = relay.var("var_9992", dtype = "float32", shape = (6, 7, 6))#candidate|9992|(6, 7, 6)|var|float32
output = func_9991(var_9992)
func_9993 = relay.Function([var_9992], output)
mutated_mod['func_9993'] = func_9993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5499_call = mod.get_global_var('func_5499')
func_5500_call = mutated_mod.get_global_var('func_5500')
call_10018 = relay.TupleGetItem(func_5499_call(), 0)
call_10019 = relay.TupleGetItem(func_5500_call(), 0)
func_8239_call = mod.get_global_var('func_8239')
func_8243_call = mutated_mod.get_global_var('func_8243')
const_10023 = relay.const([-7,-6,6,10,-9,-1,-2,-10,7,9,-7,-1,-9,8,-9,3,-5,-8,-10,3,3,-2,-2,5,8,-5,6,-1,-8,-7,4,-5,-1,-4,-3,8,-2,4,-5,-5,-3,-9,8,-4,-10,5,2,-5,-3,2,5,-2,4,-10,5,3,6,6,1,2], dtype = "uint64")#candidate|10023|(60,)|const|uint64
var_10024 = relay.var("var_10024", dtype = "float32", shape = (810,))#candidate|10024|(810,)|var|float32
call_10022 = relay.TupleGetItem(func_8239_call(relay.reshape(const_10023.astype('uint64'), [60,]), relay.reshape(var_10024.astype('float32'), [810,]), ), 1)
call_10025 = relay.TupleGetItem(func_8243_call(relay.reshape(const_10023.astype('uint64'), [60,]), relay.reshape(var_10024.astype('float32'), [810,]), ), 1)
func_7645_call = mod.get_global_var('func_7645')
func_7648_call = mutated_mod.get_global_var('func_7648')
const_10043 = relay.const(9.154626, dtype = "float32")#candidate|10043|()|const|float32
var_10044 = relay.var("var_10044", dtype = "float32", shape = (1, 1001))#candidate|10044|(1, 1001)|var|float32
call_10042 = relay.TupleGetItem(func_7645_call(relay.reshape(const_10043.astype('float32'), []), relay.reshape(var_10044.astype('float32'), [7, 13, 11]), ), 1)
call_10045 = relay.TupleGetItem(func_7648_call(relay.reshape(const_10043.astype('float32'), []), relay.reshape(var_10044.astype('float32'), [7, 13, 11]), ), 1)
func_2925_call = mod.get_global_var('func_2925')
func_2927_call = mutated_mod.get_global_var('func_2927')
call_10046 = relay.TupleGetItem(func_2925_call(), 1)
call_10047 = relay.TupleGetItem(func_2927_call(), 1)
func_7333_call = mod.get_global_var('func_7333')
func_7334_call = mutated_mod.get_global_var('func_7334')
call_10055 = relay.TupleGetItem(func_7333_call(), 0)
call_10056 = relay.TupleGetItem(func_7334_call(), 0)
func_5292_call = mod.get_global_var('func_5292')
func_5293_call = mutated_mod.get_global_var('func_5293')
call_10076 = func_5292_call()
call_10077 = func_5292_call()
func_4958_call = mod.get_global_var('func_4958')
func_4960_call = mutated_mod.get_global_var('func_4960')
const_10079 = relay.const([3.706473,3.910680,1.321587,9.513220,-5.014844,6.083351,9.244389,2.044744,-7.435017,4.158650,-4.932678,6.066329,-6.468951,-3.702624,1.945594,2.343700,4.291846,7.837513,-0.941567,2.025364,0.244576,1.597430,4.866516,6.223216,7.415217,7.608984,-8.031480,7.525293,-1.814265,-2.607612,-4.805376,7.833059,-1.717250,-0.764910,0.420959,2.694481,-1.523332,-7.033650,3.177803,-3.153511,-0.665353,-8.828323,-7.268309,4.230722,5.707323,-3.280860,6.843626,-7.554135,-6.764596,3.802993,-1.300611,-0.858924,6.699590,-7.262545,7.532113,2.920187,9.426333,-4.523244,-4.654369,-4.324068,8.358121,5.432615,-7.265195,-6.669885,-5.178550,4.916479,-4.322038,5.825189,-8.241445,-2.111875,-9.182024,2.268828,-9.726413,9.160143,4.799523,-3.487050,8.251193,8.644348,0.412643,-1.917925,0.960154,6.611884,-6.915588,-4.362178,-5.443416,-8.531231,-5.888875,-5.178507,2.014940,8.876680,-5.326127,0.481012,3.526428,8.955112,-9.301390,-8.761542,2.915556,5.763624,4.733711,-0.508201,-1.684016,-1.944772,-6.530231,6.980690,0.169927,-8.374188,3.409695,4.097774,0.767659,4.156969,-3.919797,4.985761,3.623921,5.477088,-8.121934,1.203917,-5.089729,-8.842903,-9.924249,-8.062676,-2.626391,6.993017,-6.045485,1.462759,-6.211756,6.805307,-8.653702,-9.508747,3.040137,-3.098346,-7.266604,3.121383,-7.325393,5.298739,2.689238,-6.432268,0.824520,6.797559,-4.537209,3.469295,-1.829665,3.871954,0.710327,-7.942853,-4.865188,4.294941,-0.073551,2.300599,-7.453758,-1.027857,4.606057,7.652379,-0.603321,-0.150737,0.841140,6.636363,9.944640,8.630851,7.459674,5.435534,-9.169053,-0.695576,5.086088,0.322332,-3.818696,-2.133149,-3.771842,-0.544229], dtype = "float32")#candidate|10079|(168,)|const|float32
call_10078 = relay.TupleGetItem(func_4958_call(relay.reshape(const_10079.astype('float32'), [84, 2])), 2)
call_10080 = relay.TupleGetItem(func_4960_call(relay.reshape(const_10079.astype('float32'), [84, 2])), 2)
func_393_call = mod.get_global_var('func_393')
func_395_call = mutated_mod.get_global_var('func_395')
call_10081 = relay.TupleGetItem(func_393_call(), 1)
call_10082 = relay.TupleGetItem(func_395_call(), 1)
func_3573_call = mod.get_global_var('func_3573')
func_3575_call = mutated_mod.get_global_var('func_3575')
call_10103 = relay.TupleGetItem(func_3573_call(), 0)
call_10104 = relay.TupleGetItem(func_3575_call(), 0)
uop_10116 = relay.atanh(call_10078.astype('float64')) # shape=(7, 8, 3)
uop_10118 = relay.atanh(call_10080.astype('float64')) # shape=(7, 8, 3)
output = relay.Tuple([call_10018,call_10022,const_10023,var_10024,call_10042,const_10043,var_10044,call_10046,call_10055,call_10076,const_10079,call_10081,call_10103,uop_10116,])
output2 = relay.Tuple([call_10019,call_10025,const_10023,var_10024,call_10045,const_10043,var_10044,call_10047,call_10056,call_10077,const_10079,call_10082,call_10104,uop_10118,])
func_10119 = relay.Function([var_10024,var_10044,], output)
mod['func_10119'] = func_10119
mod = relay.transform.InferType()(mod)
mutated_mod['func_10119'] = func_10119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10119_call = mutated_mod.get_global_var('func_10119')
var_10121 = relay.var("var_10121", dtype = "float32", shape = (810,))#candidate|10121|(810,)|var|float32
var_10122 = relay.var("var_10122", dtype = "float32", shape = (1, 1001))#candidate|10122|(1, 1001)|var|float32
call_10120 = func_10119_call(var_10121,var_10122,)
output = call_10120
func_10123 = relay.Function([var_10121,var_10122,], output)
mutated_mod['func_10123'] = func_10123
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7917_call = mod.get_global_var('func_7917')
func_7919_call = mutated_mod.get_global_var('func_7919')
call_10133 = relay.TupleGetItem(func_7917_call(), 0)
call_10134 = relay.TupleGetItem(func_7919_call(), 0)
func_7917_call = mod.get_global_var('func_7917')
func_7919_call = mutated_mod.get_global_var('func_7919')
call_10144 = relay.TupleGetItem(func_7917_call(), 0)
call_10145 = relay.TupleGetItem(func_7919_call(), 0)
output = relay.Tuple([call_10133,call_10144,])
output2 = relay.Tuple([call_10134,call_10145,])
func_10147 = relay.Function([], output)
mod['func_10147'] = func_10147
mod = relay.transform.InferType()(mod)
mutated_mod['func_10147'] = func_10147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10147_call = mutated_mod.get_global_var('func_10147')
call_10148 = func_10147_call()
output = call_10148
func_10149 = relay.Function([], output)
mutated_mod['func_10149'] = func_10149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10173 = relay.var("var_10173", dtype = "float64", shape = (1, 9, 14))#candidate|10173|(1, 9, 14)|var|float64
uop_10174 = relay.acos(var_10173.astype('float64')) # shape=(1, 9, 14)
output = uop_10174
output2 = uop_10174
func_10176 = relay.Function([var_10173,], output)
mod['func_10176'] = func_10176
mod = relay.transform.InferType()(mod)
var_10177 = relay.var("var_10177", dtype = "float64", shape = (1, 9, 14))#candidate|10177|(1, 9, 14)|var|float64
output = func_10176(var_10177)
func_10178 = relay.Function([var_10177], output)
mutated_mod['func_10178'] = func_10178
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6679_call = mod.get_global_var('func_6679')
func_6681_call = mutated_mod.get_global_var('func_6681')
call_10192 = func_6679_call()
call_10193 = func_6679_call()
output = call_10192
output2 = call_10193
func_10207 = relay.Function([], output)
mod['func_10207'] = func_10207
mod = relay.transform.InferType()(mod)
mutated_mod['func_10207'] = func_10207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10207_call = mutated_mod.get_global_var('func_10207')
call_10208 = func_10207_call()
output = call_10208
func_10209 = relay.Function([], output)
mutated_mod['func_10209'] = func_10209
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4638_call = mod.get_global_var('func_4638')
func_4640_call = mutated_mod.get_global_var('func_4640')
call_10225 = relay.TupleGetItem(func_4638_call(), 1)
call_10226 = relay.TupleGetItem(func_4640_call(), 1)
func_8035_call = mod.get_global_var('func_8035')
func_8036_call = mutated_mod.get_global_var('func_8036')
call_10256 = relay.TupleGetItem(func_8035_call(), 0)
call_10257 = relay.TupleGetItem(func_8036_call(), 0)
func_1145_call = mod.get_global_var('func_1145')
func_1147_call = mutated_mod.get_global_var('func_1147')
call_10258 = relay.TupleGetItem(func_1145_call(), 0)
call_10259 = relay.TupleGetItem(func_1147_call(), 0)
output = relay.Tuple([call_10225,call_10256,call_10258,])
output2 = relay.Tuple([call_10226,call_10257,call_10259,])
func_10270 = relay.Function([], output)
mod['func_10270'] = func_10270
mod = relay.transform.InferType()(mod)
mutated_mod['func_10270'] = func_10270
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10270_call = mutated_mod.get_global_var('func_10270')
call_10271 = func_10270_call()
output = call_10271
func_10272 = relay.Function([], output)
mutated_mod['func_10272'] = func_10272
mutated_mod = relay.transform.InferType()(mutated_mod)
const_10364 = relay.const([[[0.249867,9.972862,-8.801822,9.928249,3.024877,3.131445,-7.565561,-2.774397,0.331030,7.364623,-2.273436,-1.742767],[-9.259752,-0.296703,1.736156,6.457037,8.904179,7.844416,-7.613602,2.899304,-7.499795,-3.953003,-2.757079,-1.530485],[-8.430141,5.039986,2.966225,8.090227,-7.911029,-8.093060,1.492701,-2.487606,-2.148472,-4.577601,-0.581313,-4.457951],[2.782337,-8.675367,-3.018164,6.903738,-2.432992,8.487110,-2.358305,-7.146094,1.876750,-8.247285,-7.241456,9.787239],[2.814155,2.452703,-4.426654,-1.455602,-8.535662,0.471946,2.317960,5.301605,7.183983,1.455518,6.000190,-7.190429],[-9.540350,8.167366,-8.392641,2.453642,3.558573,7.188150,2.399182,0.883108,-9.483403,-3.294148,9.149984,-0.140500],[-1.362951,-6.147834,9.101723,-6.950568,-5.217774,-0.668951,6.856320,-3.151693,-2.978008,-4.331730,4.231913,-5.310576],[-4.613664,-5.882715,-2.769730,-6.482813,-1.600007,4.138024,8.758442,-1.078653,4.334526,-4.823072,-1.209681,8.808613],[7.141694,-7.805803,0.400951,-2.245912,8.380073,8.206371,6.051407,1.971927,5.254491,7.988454,-6.006588,-4.252812],[-5.805032,-6.963950,8.368846,-7.308896,8.771683,7.889062,5.231455,-6.401549,-2.304296,-0.082125,5.693051,-8.311906]],[[-0.300671,-4.206992,6.597529,2.236360,5.024123,-4.315812,5.642001,4.940295,-9.099539,-4.998775,5.369299,-6.700700],[-3.288145,1.667054,-4.462474,-9.175591,-1.041779,-7.946400,0.230806,2.377714,6.486479,0.764295,-8.742690,-9.760228],[-9.106855,-7.653571,8.351810,7.174255,-8.181758,-8.872112,-1.502716,7.275570,4.778349,-0.603105,7.898365,3.150928],[-0.518049,-7.789322,-8.436722,8.727594,4.316290,-6.745187,-3.285805,-2.781873,-4.076569,-8.464154,-4.914504,8.760952],[4.971103,-0.231192,-6.178342,1.990104,9.835453,7.142876,-3.164147,-3.592639,8.067674,8.236138,-6.781108,-1.027605],[-8.196751,-4.812526,-8.684509,-2.670040,6.157032,7.249047,-7.243313,-8.383201,-5.147678,9.227488,-8.201524,-2.016294],[-0.243820,-3.770628,7.220525,-0.570917,6.453182,-0.478159,-6.062588,0.410860,-8.267547,2.870207,5.200567,-3.316525],[-5.128911,8.025721,1.916026,-4.929221,1.382086,-0.537888,2.040345,-7.742711,3.961122,-7.934630,4.580831,-6.771299],[-8.001149,-3.361012,9.971674,8.669514,2.578870,8.060255,-4.890747,-6.620345,-4.254831,1.838579,2.464664,-0.508771],[-1.243150,5.299120,-4.875997,8.055597,4.730736,-2.830861,-4.485068,-1.159830,-7.690080,-4.067486,5.580120,-8.824511]],[[-4.070720,0.299956,3.936715,-0.185811,5.792789,4.671612,6.140599,-7.667413,0.418648,-2.294805,3.140816,5.150282],[-7.191520,-8.521679,-7.951719,8.425156,-7.958902,7.205098,-7.510763,-4.213430,2.786487,2.091702,-6.742848,9.053198],[-6.767290,-6.772831,5.684387,-8.457524,1.163451,9.251867,8.999522,-3.617241,-2.279051,-4.554480,-6.945004,-3.304140],[-2.973414,-3.238981,6.073606,-5.334063,6.412574,8.580909,-7.948084,-0.530473,5.617154,-8.501754,-2.635503,-3.950256],[-3.873090,6.487443,2.510952,-9.251261,6.149809,3.960813,-2.714862,0.635847,-4.296518,-4.722421,-4.727400,-4.839811],[2.564280,-9.866034,-0.214107,-8.528413,3.304987,9.914271,9.557138,2.326360,-0.181449,4.435943,-2.219142,6.492352],[-1.116784,-5.598883,-7.546296,-8.225603,4.128412,-7.650877,7.577926,-8.909458,-9.426726,-8.240922,6.299610,2.299306],[-0.723144,-0.226867,5.670119,7.234588,-8.218240,-6.808652,-6.477461,-7.477221,9.810115,9.228387,5.801411,-9.460421],[9.899029,2.967254,-5.089608,1.904491,7.146737,7.256110,2.796828,-9.911531,-7.793186,-4.367539,3.093183,-5.694734],[5.718588,-9.761125,4.096380,2.627886,6.182393,4.551848,9.411595,-4.304340,7.322991,7.210984,-2.195543,-5.451516]],[[-9.435597,8.159201,6.238633,-6.014453,-2.748593,7.629057,5.921873,-2.006222,0.830963,-3.473210,-8.143066,8.605213],[5.230894,-4.845953,3.288235,-1.819442,-0.917176,7.953153,-0.716297,-6.123741,-8.083831,-6.886089,-2.757368,-8.753100],[5.610476,-2.958953,2.925089,1.518541,-0.637097,-9.609981,-2.450388,2.897795,8.198005,-3.681275,7.038823,-1.993000],[-3.877024,9.925338,7.201372,-2.481693,3.754697,7.071427,-3.937419,5.712489,-4.132668,-3.308717,-3.804778,7.397554],[9.820162,3.212438,0.410388,-3.052899,3.916258,-5.163416,-4.078783,3.399467,-9.593542,-5.537837,4.518756,1.724172],[-2.776822,-5.373315,-2.056423,-1.948949,0.844998,-5.720977,7.613168,-1.848797,-3.299124,5.629249,1.995011,-8.544606],[2.357750,-7.663821,-9.296457,4.467537,-3.459498,-9.668686,7.973078,-8.899062,-6.716312,9.923073,0.183536,-1.388262],[1.517884,-5.405984,-3.896237,-4.367629,-7.031060,-9.402813,-6.428369,7.409905,7.127617,8.452885,-8.210801,4.747949],[-8.257653,-0.581839,-7.594218,-7.275120,-3.901193,-6.030238,1.871097,8.814009,-8.900077,8.863823,5.158120,3.167466],[-8.319608,5.041668,-0.956387,6.812494,-2.590175,-8.999809,7.947673,-6.778088,-0.544274,-3.205081,7.109947,6.017247]]], dtype = "float32")#candidate|10364|(4, 10, 12)|const|float32
uop_10365 = relay.asin(const_10364.astype('float32')) # shape=(4, 10, 12)
output = uop_10365
output2 = uop_10365
func_10390 = relay.Function([], output)
mod['func_10390'] = func_10390
mod = relay.transform.InferType()(mod)
output = func_10390()
func_10391 = relay.Function([], output)
mutated_mod['func_10391'] = func_10391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_10444 = relay.TupleGetItem(func_595_call(), 1)
call_10445 = relay.TupleGetItem(func_596_call(), 1)
output = call_10444
output2 = call_10445
func_10450 = relay.Function([], output)
mod['func_10450'] = func_10450
mod = relay.transform.InferType()(mod)
output = func_10450()
func_10451 = relay.Function([], output)
mutated_mod['func_10451'] = func_10451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2467_call = mod.get_global_var('func_2467')
func_2468_call = mutated_mod.get_global_var('func_2468')
call_10464 = relay.TupleGetItem(func_2467_call(), 0)
call_10465 = relay.TupleGetItem(func_2468_call(), 0)
func_5196_call = mod.get_global_var('func_5196')
func_5197_call = mutated_mod.get_global_var('func_5197')
call_10495 = func_5196_call()
call_10496 = func_5196_call()
output = relay.Tuple([call_10464,call_10495,])
output2 = relay.Tuple([call_10465,call_10496,])
func_10512 = relay.Function([], output)
mod['func_10512'] = func_10512
mod = relay.transform.InferType()(mod)
output = func_10512()
func_10513 = relay.Function([], output)
mutated_mod['func_10513'] = func_10513
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1993_call = mod.get_global_var('func_1993')
func_1994_call = mutated_mod.get_global_var('func_1994')
call_10514 = relay.TupleGetItem(func_1993_call(), 2)
call_10515 = relay.TupleGetItem(func_1994_call(), 2)
func_8083_call = mod.get_global_var('func_8083')
func_8085_call = mutated_mod.get_global_var('func_8085')
call_10516 = func_8083_call()
call_10517 = func_8083_call()
func_6848_call = mod.get_global_var('func_6848')
func_6850_call = mutated_mod.get_global_var('func_6850')
call_10524 = func_6848_call()
call_10525 = func_6848_call()
func_1118_call = mod.get_global_var('func_1118')
func_1122_call = mutated_mod.get_global_var('func_1122')
var_10531 = relay.var("var_10531", dtype = "float32", shape = (448,))#candidate|10531|(448,)|var|float32
const_10532 = relay.const([5,4,-7,6,-3,-9,-6,2,4,3,4,-5,4,-8,-10,-2,-2,10,7,-7,9,-1,10,-4,9,-10,-5,-2,4,6,10,10,-8,3,8,-10,-6,2,4,-10,3,8,4,-9,-1,-4,-6,-4,7,-2,5,-4,2,-9,-3,-1,-9,-6,-10,-3,1,1,4,-10,3,9,-3,-1,8,3,-8,-10,5,2,-1,8,4,7,-7,10,10,-7,2,-8,-7,2,7,-4,7,10,3,-8,-7,7,-2,3,-6,-7,-10,9,-7,-5,-4,-5,-5,7,-2,4,-9,-5,-10,5,1,-4,-8,-2,-7,-7,6,-2,-8,-10,5,2,-7,-7,7,2,-5,-1,-3,-7,-10,3,-8,-6,5,9,-1,6,-9,-4,-8,-2,-5,7,6,10,8,-1,-8,5,4,-5,-4,-5,-7,-7,9,9,4,4,8,7,7,2,-4,1,10,5,9,9,10,1,9,3,-6,5,-1,9,8,-5,10,-10,-2,-6,-4,-8,-1,4,-1,-3,-4,-10,-1,-6,10,-1,5,-1,-6,-1,2,-7,-8,-2,7,-5,-6,-9,4,5,-5,4,-10,1,2,10,-1,6,7,-10,5,-7,-10,9,-2,-8,3,-8,-9,-10,-1,6,5,-1,1,-7,7,-9,-10,1,-3,10,-10,-8,9,9,-8,2,-8,8,-6,-8,-10,-10,-7,2,-9,-7,-1,10,-5,-10,6,8,8,-3,-2,-7,-2,-3,-9,1,7,9,-5,10,9,-2,-3,-9,8,-5,-7,-3,9,-7,10,6,-8,-7,-7,-2,8,-1,6,-4,-6,-5,1,-1,3,-9,-8,2,4,-10,8,-5,-5,9,-10,6,-2,-8,-10,-3,9,-7,9,-6,1,-3,-7,7,-9,-5,-9,-5,-3,-6,-6,-7,-3,5,-6,-6,-6,-5,-9,6,9,5,2,1,-6,2,9,6,-6,5], dtype = "int8")#candidate|10532|(352,)|const|int8
call_10530 = relay.TupleGetItem(func_1118_call(relay.reshape(var_10531.astype('float32'), [8, 14, 4]), relay.reshape(var_10531.astype('float32'), [8, 14, 4]), relay.reshape(const_10532.astype('int8'), [352,]), ), 0)
call_10533 = relay.TupleGetItem(func_1122_call(relay.reshape(var_10531.astype('float32'), [8, 14, 4]), relay.reshape(var_10531.astype('float32'), [8, 14, 4]), relay.reshape(const_10532.astype('int8'), [352,]), ), 0)
uop_10534 = relay.exp(call_10530.astype('float32')) # shape=(8, 14, 4)
uop_10536 = relay.exp(call_10533.astype('float32')) # shape=(8, 14, 4)
func_452_call = mod.get_global_var('func_452')
func_455_call = mutated_mod.get_global_var('func_455')
var_10549 = relay.var("var_10549", dtype = "uint8", shape = ())#candidate|10549|()|var|uint8
const_10550 = relay.const([-8,8,10,-4,-6,1,5,-8,2,1,-9,10,9,4,-8,2,8,1,7,-4,8,-5,-1,-6,-8,-1,-5,8,2,-2,9,-6,5,-4,-7,-5,4,-7,-2,-9,1,-9,3,-2,1,7,1,-6,-3,9,9,-2,-6,9,4,-10,10,-1,7,9,-9,-8,10,-7,6,-2,3,-7,2,9,-4,1,10,-8,-7,-5,-1,-9,8,-3,-5,9,-8,-7,2,8,-6,-9,-3,3,4,-8,-4,-6,-4,-9,4,7,6,-4,-1,-4,3,3,-2,6,6,-3,-3,-5,9,-6,-1,7,-6,-6,5,-3,-7,6,5,-7,8,-3,8,9,-9,-2,-7,-10,2,-3,-9,-9,5,8,-9,-2,3,-9,-3,-10,-3,-7,-1,-7,-2,-2,-7,7,-6,3,-10,-2,10,5,10,-8,-6,-5,-1,-10,5,5,-4,-3,7,-6,10,-9,-3,-4,10,8,-8,-2,7,1,7,3,8,2,3,2,9,-6,8,5,-3,-3,-8,-7,9,7,3,7,-10,-7,-10,8,4,2,-3,1,10,6,-3,2,-4,9,-3,-9,9,7,8,-9,-9,-6,7,-10,-5,4,-1,1,-5,3,9,10,1,-5,3,1,4,4,-9,10,-1,2,-1,9,5,6,5,10,-3,5,1,-8,5,10,-6,-8,3,1,4,1,-4,-1,-3,7,10,-4,7,-7,3,8,8,-8,-5,6,-7,-9,4,-9,3,-2,7,-5,7,-1,-1,-4,5,9,-9,9,2,8,-10,-2,5,9,2,-10,-5,-3,-10,-5,-7,2,1,-5,-3,-10,1,9,8,10,9,-10,1,-1,8,-3,-2,2,-10,8,-9,-6,10,8,1,-9,10,-7,1,-1,3,6,2,-9,-5,6,3,6,-9,-5,-2,3,4,-2,-7,7,-8,-5,3,3,-1,3,2,9,-4,2,-1,-6,6,-1,3,-4,1,1,3,3,2,-8,-5,-6,3,5,-6,8,-10,-4,7,4,-7,-3,1,-6,1,-7,-5,7,4,4,6,-9,-3,1,-3,1,2,-2,-9,5,-6,-8,7,9,-9,1,-4,-2,-5,8,-10,8,2,-4,-10,-1,-3,-5,8,4,-8,-3,-5,-1,9,-6,8,-10,6,1,5,2,5,-8,5,8,-5,6,-9,-10,-8,-9,2,7,5,6,2,-8,7,-7,6,-6,10,2,-8,-10,-1,-3,10,3,-9,-7,-6,7,-1,-6,2,9,-3,-1,-5,9,10,1,3,-7,-2,3,-9,3,-5,-6,-2,-10,8,-8,-4,1,1,6,-5,-6,9,-6,2,-10,-8,-5,-3,-5,-8,-6,-10,-6,8,-4,-7,9,-10,8,-4,-10,-5,3,9,1,-3,-10,3,-3,-10,-3,7,-6,-6,-10,3,5,4,7,9,3,-6,-4,-10,9,4,-8,-3,2,9,4,-2,9,8,-1,4,9,-6,-9,10,6,-10,-6,1,6,2,1,8,3,-5,-5,8,-7,4,3,-3,-9,5,8,5,-5,4,4,5,-10,-10,7,8,6,-1,-8,-8,-9,-4,9,3,-10,-10,-10,10,3,-6,1,6,8,4,4,-4,-7,2,-10,9,-3,-4,4,-5,-5,-9,7,-4,5,-2,2,-3,-4,4,-9,6,10,5,6,-10,10,-9,-5,1,-3,-10,-9,-3,-6,-9,-7,-7,8,2,-9,-9,4,-8,-3,10,4,-10,-10,5,9,3,2,-7,-1,6,-3,-10,3,5,-9,-1,-4,-3,5,2,-6,3,4,-8,-9,4,-9,1,2,-5,3,-3,6,-1,6,6,8,-1,7,7,6,-2,-6,5,10,-1,6,10,-10,5,-6,-9,8,7,9,-5,-5,-10,-1,1,6,6,3,-6,-9,-10,-1,7,9,7,8,-5,-1,6,-1,-5,6,-1,-9,4,9,3,3,9,6,3,2,-8,2,-6,10,2,-5,9,-1,2,-8,-7,-6,4,6,7,5,10,-1,2,8,-9,8,-6,10,-6,4,-9,2,2,3,4,7,7,10,9,-3,10,-6,-8,-6,-5,10,3,-1,9,-6,-2,-9,-3,6,7,-10,-3,-5,3,9,-4,-3,-10,3,8,4,-4,-7,-2,-9,-6,-7,-5,2,-4,5,-10,6,-5,-9,8,-3,8,9,4,-10,5,9,-10,8,-4,3,-5,3,-5,3,8,8,-5,-6,5,9,-3,-1,-3,-6,-4,-2,7,-9,10,8,9,3,-2,-4,7,6,4,-3,-6,6,10,-1,3,-9,-3,10,2,-5,-4,-1,4,1,5,-7,-6,3,10,3,3,8,-1,-7,4,9,-2,-1,8,-4,-7,-5,3,9,3,9,-3,3,9,-9,5,3,8,4,5,10,9,4,-5,-7,2,8,5,1,3,-7,10,6,3,6,7,7,-3,-8,-4,9,-3,1,-8,1,4,2,9,4,7,7,5,-10,7,-9,4,-6,6,-4,4,8,5,-4,7,6,7,7,-1,4,-6,-10,-2,-7,6,5,-9,7,-2,-10,-8,-2,-2,-1,-6,3,-8,4,9,-10,-5,4,7,-7,2,-7,-4,7,8,8,-3,-9,4,-2,-7,8,9,-5,3,5,-7,-8,-3,-6,-7,6,7,-2,1,6,8,9,7,-4,-3,-8,3,-5,4,-9,8,-10,3,6,6,9,7,1,-1,4,4,-8], dtype = "uint8")#candidate|10550|(1008,)|const|uint8
call_10548 = func_452_call(relay.reshape(var_10549.astype('uint8'), []), relay.reshape(const_10550.astype('uint8'), [8, 14, 9]), )
call_10551 = func_452_call(relay.reshape(var_10549.astype('uint8'), []), relay.reshape(const_10550.astype('uint8'), [8, 14, 9]), )
bop_10564 = relay.left_shift(uop_10534.astype('int16'), relay.reshape(call_10530.astype('int16'), relay.shape_of(uop_10534))) # shape=(8, 14, 4)
bop_10567 = relay.left_shift(uop_10536.astype('int16'), relay.reshape(call_10533.astype('int16'), relay.shape_of(uop_10536))) # shape=(8, 14, 4)
output = relay.Tuple([call_10514,call_10516,call_10524,var_10531,const_10532,call_10548,var_10549,const_10550,bop_10564,])
output2 = relay.Tuple([call_10515,call_10517,call_10525,var_10531,const_10532,call_10551,var_10549,const_10550,bop_10567,])
func_10568 = relay.Function([var_10531,var_10549,], output)
mod['func_10568'] = func_10568
mod = relay.transform.InferType()(mod)
var_10569 = relay.var("var_10569", dtype = "float32", shape = (448,))#candidate|10569|(448,)|var|float32
var_10570 = relay.var("var_10570", dtype = "uint8", shape = ())#candidate|10570|()|var|uint8
output = func_10568(var_10569,var_10570,)
func_10571 = relay.Function([var_10569,var_10570,], output)
mutated_mod['func_10571'] = func_10571
mutated_mod = relay.transform.InferType()(mutated_mod)
var_10587 = relay.var("var_10587", dtype = "uint32", shape = (6, 5, 10))#candidate|10587|(6, 5, 10)|var|uint32
var_10588 = relay.var("var_10588", dtype = "uint32", shape = (6, 5, 10))#candidate|10588|(6, 5, 10)|var|uint32
bop_10589 = relay.not_equal(var_10587.astype('bool'), relay.reshape(var_10588.astype('bool'), relay.shape_of(var_10587))) # shape=(6, 5, 10)
uop_10592 = relay.tan(bop_10589.astype('float32')) # shape=(6, 5, 10)
func_2776_call = mod.get_global_var('func_2776')
func_2778_call = mutated_mod.get_global_var('func_2778')
call_10597 = relay.TupleGetItem(func_2776_call(), 0)
call_10598 = relay.TupleGetItem(func_2778_call(), 0)
output = relay.Tuple([uop_10592,call_10597,])
output2 = relay.Tuple([uop_10592,call_10598,])
func_10606 = relay.Function([var_10587,var_10588,], output)
mod['func_10606'] = func_10606
mod = relay.transform.InferType()(mod)
var_10607 = relay.var("var_10607", dtype = "uint32", shape = (6, 5, 10))#candidate|10607|(6, 5, 10)|var|uint32
var_10608 = relay.var("var_10608", dtype = "uint32", shape = (6, 5, 10))#candidate|10608|(6, 5, 10)|var|uint32
output = func_10606(var_10607,var_10608,)
func_10609 = relay.Function([var_10607,var_10608,], output)
mutated_mod['func_10609'] = func_10609
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2863_call = mod.get_global_var('func_2863')
func_2865_call = mutated_mod.get_global_var('func_2865')
call_10611 = relay.TupleGetItem(func_2863_call(), 2)
call_10612 = relay.TupleGetItem(func_2865_call(), 2)
func_7371_call = mod.get_global_var('func_7371')
func_7373_call = mutated_mod.get_global_var('func_7373')
call_10626 = func_7371_call()
call_10627 = func_7371_call()
func_3524_call = mod.get_global_var('func_3524')
func_3525_call = mutated_mod.get_global_var('func_3525')
call_10635 = relay.TupleGetItem(func_3524_call(), 0)
call_10636 = relay.TupleGetItem(func_3525_call(), 0)
output = relay.Tuple([call_10611,call_10626,call_10635,])
output2 = relay.Tuple([call_10612,call_10627,call_10636,])
func_10648 = relay.Function([], output)
mod['func_10648'] = func_10648
mod = relay.transform.InferType()(mod)
output = func_10648()
func_10649 = relay.Function([], output)
mutated_mod['func_10649'] = func_10649
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_10728 = relay.TupleGetItem(func_595_call(), 1)
call_10729 = relay.TupleGetItem(func_596_call(), 1)
output = relay.Tuple([call_10728,])
output2 = relay.Tuple([call_10729,])
func_10730 = relay.Function([], output)
mod['func_10730'] = func_10730
mod = relay.transform.InferType()(mod)
output = func_10730()
func_10731 = relay.Function([], output)
mutated_mod['func_10731'] = func_10731
mutated_mod = relay.transform.InferType()(mutated_mod)
func_595_call = mod.get_global_var('func_595')
func_596_call = mutated_mod.get_global_var('func_596')
call_10784 = relay.TupleGetItem(func_595_call(), 1)
call_10785 = relay.TupleGetItem(func_596_call(), 1)
output = call_10784
output2 = call_10785
func_10788 = relay.Function([], output)
mod['func_10788'] = func_10788
mod = relay.transform.InferType()(mod)
mutated_mod['func_10788'] = func_10788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10788_call = mutated_mod.get_global_var('func_10788')
call_10789 = func_10788_call()
output = call_10789
func_10790 = relay.Function([], output)
mutated_mod['func_10790'] = func_10790
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7371_call = mod.get_global_var('func_7371')
func_7373_call = mutated_mod.get_global_var('func_7373')
call_10825 = func_7371_call()
call_10826 = func_7371_call()
output = call_10825
output2 = call_10826
func_10847 = relay.Function([], output)
mod['func_10847'] = func_10847
mod = relay.transform.InferType()(mod)
output = func_10847()
func_10848 = relay.Function([], output)
mutated_mod['func_10848'] = func_10848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7866_call = mod.get_global_var('func_7866')
func_7868_call = mutated_mod.get_global_var('func_7868')
call_10883 = relay.TupleGetItem(func_7866_call(), 0)
call_10884 = relay.TupleGetItem(func_7868_call(), 0)
func_3961_call = mod.get_global_var('func_3961')
func_3962_call = mutated_mod.get_global_var('func_3962')
call_10886 = func_3961_call()
call_10887 = func_3961_call()
func_5165_call = mod.get_global_var('func_5165')
func_5166_call = mutated_mod.get_global_var('func_5166')
call_10888 = relay.TupleGetItem(func_5165_call(), 4)
call_10889 = relay.TupleGetItem(func_5166_call(), 4)
var_10896 = relay.var("var_10896", dtype = "uint8", shape = (12, 84))#candidate|10896|(12, 84)|var|uint8
bop_10897 = relay.maximum(call_10888.astype('int32'), relay.reshape(var_10896.astype('int32'), relay.shape_of(call_10888))) # shape=(12, 84)
bop_10900 = relay.maximum(call_10889.astype('int32'), relay.reshape(var_10896.astype('int32'), relay.shape_of(call_10889))) # shape=(12, 84)
func_5280_call = mod.get_global_var('func_5280')
func_5283_call = mutated_mod.get_global_var('func_5283')
var_10902 = relay.var("var_10902", dtype = "uint32", shape = (312,))#candidate|10902|(312,)|var|uint32
call_10901 = relay.TupleGetItem(func_5280_call(relay.reshape(var_10902.astype('uint32'), [312,])), 1)
call_10903 = relay.TupleGetItem(func_5283_call(relay.reshape(var_10902.astype('uint32'), [312,])), 1)
output = relay.Tuple([call_10883,call_10886,bop_10897,call_10901,var_10902,])
output2 = relay.Tuple([call_10884,call_10887,bop_10900,call_10903,var_10902,])
func_10907 = relay.Function([var_10896,var_10902,], output)
mod['func_10907'] = func_10907
mod = relay.transform.InferType()(mod)
mutated_mod['func_10907'] = func_10907
mutated_mod = relay.transform.InferType()(mutated_mod)
func_10907_call = mutated_mod.get_global_var('func_10907')
var_10909 = relay.var("var_10909", dtype = "uint8", shape = (12, 84))#candidate|10909|(12, 84)|var|uint8
var_10910 = relay.var("var_10910", dtype = "uint32", shape = (312,))#candidate|10910|(312,)|var|uint32
call_10908 = func_10907_call(var_10909,var_10910,)
output = call_10908
func_10911 = relay.Function([var_10909,var_10910,], output)
mutated_mod['func_10911'] = func_10911
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8594_call = mod.get_global_var('func_8594')
func_8596_call = mutated_mod.get_global_var('func_8596')
call_10960 = relay.TupleGetItem(func_8594_call(), 0)
call_10961 = relay.TupleGetItem(func_8596_call(), 0)
func_9585_call = mod.get_global_var('func_9585')
func_9587_call = mutated_mod.get_global_var('func_9587')
var_10963 = relay.var("var_10963", dtype = "float64", shape = (5, 132))#candidate|10963|(5, 132)|var|float64
call_10962 = relay.TupleGetItem(func_9585_call(relay.reshape(var_10963.astype('float64'), [660, 1])), 0)
call_10964 = relay.TupleGetItem(func_9587_call(relay.reshape(var_10963.astype('float64'), [660, 1])), 0)
uop_10968 = relay.cos(var_10963.astype('float32')) # shape=(5, 132)
func_6555_call = mod.get_global_var('func_6555')
func_6557_call = mutated_mod.get_global_var('func_6557')
var_10981 = relay.var("var_10981", dtype = "uint32", shape = (936,))#candidate|10981|(936,)|var|uint32
call_10980 = relay.TupleGetItem(func_6555_call(relay.reshape(var_10981.astype('uint32'), [936,])), 1)
call_10982 = relay.TupleGetItem(func_6557_call(relay.reshape(var_10981.astype('uint32'), [936,])), 1)
bop_10991 = relay.greater(uop_10968.astype('bool'), relay.reshape(var_10963.astype('bool'), relay.shape_of(uop_10968))) # shape=(5, 132)
func_9601_call = mod.get_global_var('func_9601')
func_9603_call = mutated_mod.get_global_var('func_9603')
call_10994 = func_9601_call()
call_10995 = func_9601_call()
func_7976_call = mod.get_global_var('func_7976')
func_7978_call = mutated_mod.get_global_var('func_7978')
call_10999 = relay.TupleGetItem(func_7976_call(), 0)
call_11000 = relay.TupleGetItem(func_7978_call(), 0)
bop_11012 = relay.bitwise_or(uop_10968.astype('int32'), relay.reshape(bop_10991.astype('int32'), relay.shape_of(uop_10968))) # shape=(5, 132)
uop_11018 = relay.cos(call_10980.astype('float32')) # shape=(13, 6, 12)
uop_11020 = relay.cos(call_10982.astype('float32')) # shape=(13, 6, 12)
output = relay.Tuple([call_10960,call_10962,var_10981,call_10994,call_10999,bop_11012,uop_11018,])
output2 = relay.Tuple([call_10961,call_10964,var_10981,call_10995,call_11000,bop_11012,uop_11020,])
func_11026 = relay.Function([var_10963,var_10981,], output)
mod['func_11026'] = func_11026
mod = relay.transform.InferType()(mod)
var_11027 = relay.var("var_11027", dtype = "float64", shape = (5, 132))#candidate|11027|(5, 132)|var|float64
var_11028 = relay.var("var_11028", dtype = "uint32", shape = (936,))#candidate|11028|(936,)|var|uint32
output = func_11026(var_11027,var_11028,)
func_11029 = relay.Function([var_11027,var_11028,], output)
mutated_mod['func_11029'] = func_11029
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4222_call = mod.get_global_var('func_4222')
func_4223_call = mutated_mod.get_global_var('func_4223')
call_11042 = relay.TupleGetItem(func_4222_call(), 0)
call_11043 = relay.TupleGetItem(func_4223_call(), 0)
output = call_11042
output2 = call_11043
func_11046 = relay.Function([], output)
mod['func_11046'] = func_11046
mod = relay.transform.InferType()(mod)
mutated_mod['func_11046'] = func_11046
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11046_call = mutated_mod.get_global_var('func_11046')
call_11047 = func_11046_call()
output = call_11047
func_11048 = relay.Function([], output)
mutated_mod['func_11048'] = func_11048
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9851_call = mod.get_global_var('func_9851')
func_9852_call = mutated_mod.get_global_var('func_9852')
call_11080 = relay.TupleGetItem(func_9851_call(), 1)
call_11081 = relay.TupleGetItem(func_9852_call(), 1)
output = call_11080
output2 = call_11081
func_11090 = relay.Function([], output)
mod['func_11090'] = func_11090
mod = relay.transform.InferType()(mod)
mutated_mod['func_11090'] = func_11090
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11090_call = mutated_mod.get_global_var('func_11090')
call_11091 = func_11090_call()
output = call_11091
func_11092 = relay.Function([], output)
mutated_mod['func_11092'] = func_11092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8035_call = mod.get_global_var('func_8035')
func_8036_call = mutated_mod.get_global_var('func_8036')
call_11108 = relay.TupleGetItem(func_8035_call(), 0)
call_11109 = relay.TupleGetItem(func_8036_call(), 0)
output = call_11108
output2 = call_11109
func_11125 = relay.Function([], output)
mod['func_11125'] = func_11125
mod = relay.transform.InferType()(mod)
output = func_11125()
func_11126 = relay.Function([], output)
mutated_mod['func_11126'] = func_11126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6806_call = mod.get_global_var('func_6806')
func_6807_call = mutated_mod.get_global_var('func_6807')
call_11182 = relay.TupleGetItem(func_6806_call(), 2)
call_11183 = relay.TupleGetItem(func_6807_call(), 2)
output = call_11182
output2 = call_11183
func_11197 = relay.Function([], output)
mod['func_11197'] = func_11197
mod = relay.transform.InferType()(mod)
mutated_mod['func_11197'] = func_11197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11197_call = mutated_mod.get_global_var('func_11197')
call_11198 = func_11197_call()
output = call_11198
func_11199 = relay.Function([], output)
mutated_mod['func_11199'] = func_11199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2207_call = mod.get_global_var('func_2207')
func_2208_call = mutated_mod.get_global_var('func_2208')
call_11231 = relay.TupleGetItem(func_2207_call(), 0)
call_11232 = relay.TupleGetItem(func_2208_call(), 0)
output = relay.Tuple([call_11231,])
output2 = relay.Tuple([call_11232,])
func_11251 = relay.Function([], output)
mod['func_11251'] = func_11251
mod = relay.transform.InferType()(mod)
output = func_11251()
func_11252 = relay.Function([], output)
mutated_mod['func_11252'] = func_11252
mutated_mod = relay.transform.InferType()(mutated_mod)
const_11263 = relay.const([[[1.740524,-7.296110,6.877798],[-6.623030,-1.040731,2.245684],[1.252212,2.586065,0.697084],[-2.017891,-0.827123,2.705424],[0.947467,-9.841498,6.611066],[9.676008,-3.379428,-2.619728],[1.382823,9.680206,6.820364],[4.266280,8.152611,-7.441035]],[[1.570621,9.766274,-3.318072],[-5.312896,-6.692086,-7.941908],[-7.258802,3.123020,-9.314542],[-8.785564,-4.876779,1.494613],[5.959913,-5.194711,9.675575],[4.988631,8.092363,-0.334141],[7.885484,6.280017,9.632833],[4.564299,5.489580,-0.663125]],[[-4.663501,9.450267,4.614203],[-5.839868,8.856073,4.300776],[-9.964416,-6.901400,2.723385],[3.146617,7.414077,-9.270183],[-9.655431,-2.354325,-5.083856],[9.625132,-9.274340,1.095250],[-6.768215,-2.038646,-4.332239],[-0.633960,-6.374418,-0.579056]]], dtype = "float64")#candidate|11263|(3, 8, 3)|const|float64
var_11264 = relay.var("var_11264", dtype = "float64", shape = (3, 8, 3))#candidate|11264|(3, 8, 3)|var|float64
bop_11265 = relay.divide(const_11263.astype('float64'), relay.reshape(var_11264.astype('float64'), relay.shape_of(const_11263))) # shape=(3, 8, 3)
output = bop_11265
output2 = bop_11265
func_11277 = relay.Function([var_11264,], output)
mod['func_11277'] = func_11277
mod = relay.transform.InferType()(mod)
mutated_mod['func_11277'] = func_11277
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11278 = relay.var("var_11278", dtype = "float64", shape = (3, 8, 3))#candidate|11278|(3, 8, 3)|var|float64
func_11277_call = mutated_mod.get_global_var('func_11277')
call_11279 = func_11277_call(var_11278)
output = call_11279
func_11280 = relay.Function([var_11278], output)
mutated_mod['func_11280'] = func_11280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9270_call = mod.get_global_var('func_9270')
func_9272_call = mutated_mod.get_global_var('func_9272')
call_11292 = relay.TupleGetItem(func_9270_call(), 2)
call_11293 = relay.TupleGetItem(func_9272_call(), 2)
var_11313 = relay.var("var_11313", dtype = "float64", shape = (832,))#candidate|11313|(832,)|var|float64
bop_11314 = relay.divide(call_11292.astype('float32'), relay.reshape(var_11313.astype('float32'), relay.shape_of(call_11292))) # shape=(832,)
bop_11317 = relay.divide(call_11293.astype('float32'), relay.reshape(var_11313.astype('float32'), relay.shape_of(call_11293))) # shape=(832,)
output = bop_11314
output2 = bop_11317
func_11333 = relay.Function([var_11313,], output)
mod['func_11333'] = func_11333
mod = relay.transform.InferType()(mod)
mutated_mod['func_11333'] = func_11333
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11334 = relay.var("var_11334", dtype = "float64", shape = (832,))#candidate|11334|(832,)|var|float64
func_11333_call = mutated_mod.get_global_var('func_11333')
call_11335 = func_11333_call(var_11334)
output = call_11335
func_11336 = relay.Function([var_11334], output)
mutated_mod['func_11336'] = func_11336
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9851_call = mod.get_global_var('func_9851')
func_9852_call = mutated_mod.get_global_var('func_9852')
call_11396 = relay.TupleGetItem(func_9851_call(), 1)
call_11397 = relay.TupleGetItem(func_9852_call(), 1)
func_2273_call = mod.get_global_var('func_2273')
func_2275_call = mutated_mod.get_global_var('func_2275')
call_11401 = func_2273_call()
call_11402 = func_2273_call()
output = relay.Tuple([call_11396,call_11401,])
output2 = relay.Tuple([call_11397,call_11402,])
func_11410 = relay.Function([], output)
mod['func_11410'] = func_11410
mod = relay.transform.InferType()(mod)
output = func_11410()
func_11411 = relay.Function([], output)
mutated_mod['func_11411'] = func_11411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11419 = relay.var("var_11419", dtype = "float32", shape = (12, 5, 16))#candidate|11419|(12, 5, 16)|var|float32
uop_11420 = relay.sin(var_11419.astype('float32')) # shape=(12, 5, 16)
func_10176_call = mod.get_global_var('func_10176')
func_10178_call = mutated_mod.get_global_var('func_10178')
var_11423 = relay.var("var_11423", dtype = "float64", shape = (126,))#candidate|11423|(126,)|var|float64
call_11422 = func_10176_call(relay.reshape(var_11423.astype('float64'), [1, 9, 14]))
call_11424 = func_10176_call(relay.reshape(var_11423.astype('float64'), [1, 9, 14]))
uop_11429 = relay.sqrt(var_11419.astype('float64')) # shape=(12, 5, 16)
func_7530_call = mod.get_global_var('func_7530')
func_7532_call = mutated_mod.get_global_var('func_7532')
var_11433 = relay.var("var_11433", dtype = "float64", shape = (660,))#candidate|11433|(660,)|var|float64
call_11432 = relay.TupleGetItem(func_7530_call(relay.reshape(var_11433.astype('float64'), [10, 11, 6])), 0)
call_11434 = relay.TupleGetItem(func_7532_call(relay.reshape(var_11433.astype('float64'), [10, 11, 6])), 0)
output = relay.Tuple([uop_11420,call_11422,var_11423,uop_11429,call_11432,var_11433,])
output2 = relay.Tuple([uop_11420,call_11424,var_11423,uop_11429,call_11434,var_11433,])
func_11435 = relay.Function([var_11419,var_11423,var_11433,], output)
mod['func_11435'] = func_11435
mod = relay.transform.InferType()(mod)
var_11436 = relay.var("var_11436", dtype = "float32", shape = (12, 5, 16))#candidate|11436|(12, 5, 16)|var|float32
var_11437 = relay.var("var_11437", dtype = "float64", shape = (126,))#candidate|11437|(126,)|var|float64
var_11438 = relay.var("var_11438", dtype = "float64", shape = (660,))#candidate|11438|(660,)|var|float64
output = func_11435(var_11436,var_11437,var_11438,)
func_11439 = relay.Function([var_11436,var_11437,var_11438,], output)
mutated_mod['func_11439'] = func_11439
mutated_mod = relay.transform.InferType()(mutated_mod)
func_11197_call = mod.get_global_var('func_11197')
func_11199_call = mutated_mod.get_global_var('func_11199')
call_11455 = func_11197_call()
call_11456 = func_11197_call()
func_5973_call = mod.get_global_var('func_5973')
func_5976_call = mutated_mod.get_global_var('func_5976')
const_11465 = relay.const([1.420694,-1.856510,4.516408,-2.738959,7.376164,2.728711,-3.833158,-2.464792,-9.103753,-2.384905,7.490636,-7.107465,-0.870164,5.884980,-3.164133,6.071956,-2.228872,-6.558701,3.274129,-6.216377,8.338635,-8.743373,-8.502188,-2.031858,0.871346,5.037482,7.224951,-0.270930,2.528080,-9.809721,2.646109,6.829485,6.671095,5.318718,-7.788689,2.870509,4.612113,8.606337,-1.894198,-3.026217,-8.888304,3.199524,6.966272,-5.886964,0.273042,-1.606320,-4.526015,-1.900049,-4.584633,4.862637,1.014242,-2.528335,-0.330616,-7.545895,3.782327,5.519040,-9.921060,4.719524,-1.320405,-6.719175,-3.553194,-6.094023,-0.940737,-5.336430,-5.254222,-6.110362,-3.138255,-4.226234,-1.216740,-1.413671,-3.597304,-1.824619,-9.540536,-4.055033,6.814574,-4.267798,-3.760499,-1.653391,3.380851,6.168097,-8.936895,7.824845,-9.046595,-1.275418,-8.719885,-2.663752,-5.313733,2.077743,-9.978651,1.287523,-6.334967,-2.790757,6.060810,3.506972,9.675495,-6.139499,-9.246904,6.880590,-2.418581,-9.906149,-7.144384,8.374396,6.159023,5.410391,-4.227524,1.184739,-5.353339,6.969415,-2.052178,-4.745577,7.172973,-9.362878,-2.280565,-5.880569,0.029493,4.467310,6.800093,-6.447487,0.370217,1.351718,-1.730280,-6.634798,-1.765273,-1.165198,-1.245398,-8.010970,-1.986376,-1.219918,-5.057077,3.204778,6.107454,4.462820,4.831838,9.497227,1.380361,-4.434015,9.941152,-6.868120,7.651309,-3.280550,1.810838,8.084608,9.599244,-4.844156,5.075944,3.331361,-6.842223,1.731614,-7.895521,-1.214739,4.060862,-6.602150,3.123588,-9.708250,2.293656,9.749641,-6.883763,-3.250889,-2.754489,8.194154,-2.542954,-5.943122,-1.524159,-7.306130,-6.951283,-0.473782,-9.533277,-9.987099,-2.570706,-0.284262,6.272732,-0.983201,-6.880608,-7.381272,-3.024311,-9.580713,-6.286414,9.493593,3.972935,-6.417201,0.793407,9.352592,3.945437,1.603654,5.367132,9.169721,1.116363,-4.926089,1.503808,-7.523836,-2.647679,-7.934825,3.962352,4.510850,-9.799066,-7.478030,7.444419,2.660323,2.980812,-0.435285,-2.181111,-6.745152,8.207916,6.827054,9.749709,-7.240200,9.515117,-0.403833,5.154102,1.531041,9.413681,7.768071,6.650112,6.821427,4.122501,5.428949,-4.431916,-4.248827,-0.605425,-4.937721,8.180312,-4.400590,3.521015,-0.131051,-8.150356,-6.165450,9.783768,-7.068894,-1.246875,-3.469247,0.899226,2.902438,8.356145,-0.652567,-2.987418,7.998716,7.217512,-9.134957,-8.317583,9.816442,-8.807405,4.197627,9.762832,-4.047478,8.840204,-9.862967,3.429494,-6.180423,8.179257,-2.946764,1.616954,1.467954,0.557896,-7.804440,-2.654989,7.228196,5.048486,4.976622,-0.820962,6.449939,-6.427617,9.328180,8.820239,-1.396994,-8.565924,-1.747520,-8.593621,-6.777637,4.385662,6.032415,5.474023,-1.017954,4.863664,4.784792,-2.273946,-6.851127,-1.446006,-0.962414,6.209558,-1.359646,5.049919,-6.369823,9.223261,-5.100915,8.486661,-1.132142,-6.284331,8.578308,-4.267828,0.260128,7.324740,7.026307,9.230478,-7.561581,-8.859995,-4.774398,3.508597,2.380299,-8.212822,-1.246944,-1.753556,-1.078406,3.300911,-3.099127,-3.364780,-8.278218,1.696550,-2.370432,2.849016,-6.335817,6.488932,-8.976594,0.969111,7.963578,9.603890,8.868563,6.514814,-8.240245,2.450772,-5.203221,-0.102154,-7.319429,5.971672,3.983456,0.434966,-5.507312,-2.914915,9.826250,6.517534,8.107896,-8.027658,-4.068710,-5.330932,0.669129,6.322249,-6.047574,-3.861909,-9.569078,8.209280,7.126035,6.949327,0.848810,-2.244812,4.033622,-6.606735,-8.662470,3.722187,-1.869357,6.907065,4.432499,4.706831,-0.119797,-4.488162,8.016459,-9.434900,-1.264842,1.431815,-4.055617,5.717611,7.735226,-4.574904,-3.518891,-6.658049,-1.076589,-3.887975,-1.410370,6.355373,-4.001823,9.488140,2.083352,-6.861678,1.415744,4.557616,5.719033,2.816555,-7.310533,-9.637106,6.345977,6.760006,-8.438759,-9.713615,-2.451743,0.871936,3.818154,-5.253976,3.349486,2.668893,-9.624815,-4.720880,7.403041,-4.217332,7.545098,-8.185122,2.037866,-8.332771,-9.697584,0.312569,-3.903600,3.846772,8.712662,-0.331788,-7.654551,-2.262983,8.065434,-6.131178,-6.148681,-9.012827,0.111706,0.730650,3.356934,-9.769570,-2.175822,-6.262259,-5.292230,-8.801549,5.979020,-8.159502,-4.269557,6.141653,9.677065,-7.554172,-7.731738,-6.571372,-7.549998,7.213591,9.478479,2.928385,4.753701,9.943639,3.063761,3.388455,-7.819080,-7.958890,-7.238936,-1.916207,8.138133,-2.102689,-5.990630,6.332776,-6.783659,-6.059175,-6.164172,4.771234,8.062507,0.457252,-0.141862,8.570057,2.637627,-8.867771,9.234246,9.198864,2.932675,9.706486,-3.160245,-7.737383,6.374948,9.754399,-5.436784,8.555880,8.037529,-1.159575,7.859936,-0.139192,2.782503,7.221851,-6.050033,4.790586,-4.763673,4.231304,6.671474,8.792629,-3.221905,-8.064773,0.594815,-2.925185,5.106974,-5.119921,-2.629982,3.190347,5.562430,1.393810,5.465286,-9.008268,8.117094,4.088236,4.822718,4.331083,2.472957,3.447295,0.127680,4.695715,-7.702791,0.540134,-0.189553,4.318711,2.499170,1.938368,7.577594,-9.160830,6.403620,-5.817874,-9.516978,-3.635528,7.010462,-4.856417,4.153304,3.680217,-7.235126,1.076485,3.811955,-0.086651,9.148336,-3.717008,6.558090,7.670453,-6.329044,-0.871876,8.391236,-8.821610,-3.807886,6.909166,-2.160612,4.734672,8.208460,3.866432,8.540827,-1.474722,-6.947979,-3.137365,0.412220,-7.085551,7.965109,1.249578,-6.754702,1.924252,-8.242964,-4.939377,-5.054971,7.451637,-0.047414,-1.846061,7.236560,-7.995333,3.816580,8.170007,-7.807900,-3.457903,-7.332365,-1.629181,4.551161,6.943967,-5.557808,-8.824895,-5.786968,1.713589,2.678269,-7.811362,-6.119223,-2.871486,1.202065,-2.976191,3.605966,9.382785,-3.514844,-5.666625,-7.587374,-2.570314,-3.426534,7.027317,-0.872695,4.374933,-8.565669,-6.558360,1.929595,5.209227,5.352501,-7.806002,-5.566882,-7.788451,-7.798800,9.213231,2.739093,3.582600,-5.054146,-5.896811,3.433911,-8.179760,8.511473,-5.674159,9.474886,-5.519539,-0.364845,-2.425325,-8.192553,3.150646,2.122330,3.442611,-4.635058,-8.595012,3.280582,-3.616784,0.579518,7.000966,1.790746,1.505162,3.702141,4.663168,-9.141360,-4.167412,2.144443,5.863553,-8.345428,7.247932,-8.351443,-3.605942,-5.316366,-3.632742,8.200171,-2.436179,-9.102434,-3.968855,3.231359,0.499714,6.288022,5.327181,2.942271,8.865820,8.873494,7.791447,0.732284,-6.531723,-0.105468,7.017108,-1.573158,-3.425263,9.021570,-8.005335,7.474379,-0.601653,6.549385,7.528513,8.343410,6.480738,1.624674,-9.921424,-6.298493,-0.211494,9.486266,-0.148504,2.721211,-9.058473,0.036060,-9.111161,-6.112476,1.283817,-3.623065,2.118500,-1.663924,-0.909225,9.406961,-0.966901,8.675830,-1.978246,-6.185637,-5.652398,4.569718,-2.456762,6.666014,5.458826,0.927966,-6.401355,0.045924,0.319119,-3.028077,0.851658,-3.991833,0.491029,-4.791878,4.493195,-2.411753,1.254555,-9.764193,7.246340,-8.637356,-3.816684,7.992032,5.122636,-0.673948,-2.934428,-5.585408,-8.778947,1.328255,6.991682,2.840456,-0.643554,-9.390129,1.853635,1.875579,0.480372,-8.929774,-3.425069,-3.357105,-8.447579,-4.531497,6.530578,1.965277,-0.425372,0.870164,-2.056254,-7.117692,-3.535534,-7.887076,3.620428,-7.225840,9.184220], dtype = "float64")#candidate|11465|(715,)|const|float64
var_11466 = relay.var("var_11466", dtype = "float32", shape = (810,))#candidate|11466|(810,)|var|float32
call_11464 = relay.TupleGetItem(func_5973_call(relay.reshape(const_11465.astype('float64'), [13, 5, 11]), relay.reshape(var_11466.astype('float32'), [81, 10]), ), 5)
call_11467 = relay.TupleGetItem(func_5976_call(relay.reshape(const_11465.astype('float64'), [13, 5, 11]), relay.reshape(var_11466.astype('float32'), [81, 10]), ), 5)
func_11090_call = mod.get_global_var('func_11090')
func_11092_call = mutated_mod.get_global_var('func_11092')
call_11477 = func_11090_call()
call_11478 = func_11090_call()
func_4240_call = mod.get_global_var('func_4240')
func_4241_call = mutated_mod.get_global_var('func_4241')
call_11482 = relay.TupleGetItem(func_4240_call(), 0)
call_11483 = relay.TupleGetItem(func_4241_call(), 0)
output = relay.Tuple([call_11455,call_11464,const_11465,var_11466,call_11477,call_11482,])
output2 = relay.Tuple([call_11456,call_11467,const_11465,var_11466,call_11478,call_11483,])
func_11489 = relay.Function([var_11466,], output)
mod['func_11489'] = func_11489
mod = relay.transform.InferType()(mod)
mutated_mod['func_11489'] = func_11489
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11490 = relay.var("var_11490", dtype = "float32", shape = (810,))#candidate|11490|(810,)|var|float32
func_11489_call = mutated_mod.get_global_var('func_11489')
call_11491 = func_11489_call(var_11490)
output = call_11491
func_11492 = relay.Function([var_11490], output)
mutated_mod['func_11492'] = func_11492
mutated_mod = relay.transform.InferType()(mutated_mod)
var_11505 = relay.var("var_11505", dtype = "float32", shape = (1, 3, 7))#candidate|11505|(1, 3, 7)|var|float32
uop_11506 = relay.asin(var_11505.astype('float32')) # shape=(1, 3, 7)
bop_11510 = relay.less_equal(uop_11506.astype('bool'), relay.reshape(var_11505.astype('bool'), relay.shape_of(uop_11506))) # shape=(1, 3, 7)
uop_11536 = relay.cos(var_11505.astype('float64')) # shape=(1, 3, 7)
output = relay.Tuple([bop_11510,uop_11536,])
output2 = relay.Tuple([bop_11510,uop_11536,])
F = relay.Function([var_11505,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_11505,], output2)
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
