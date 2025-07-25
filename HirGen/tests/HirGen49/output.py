import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_62 = relay.var("var_62", dtype = "float64", shape = (5, 6, 11))#candidate|62|(5, 6, 11)|var|float64
uop_63 = relay.cos(var_62.astype('float64')) # shape=(5, 6, 11)
uop_70 = relay.cosh(var_62.astype('float32')) # shape=(5, 6, 11)
uop_72 = relay.atan(uop_63.astype('float64')) # shape=(5, 6, 11)
uop_77 = relay.erf(uop_70.astype('float32')) # shape=(5, 6, 11)
output = relay.Tuple([uop_72,uop_77,])
output2 = relay.Tuple([uop_72,uop_77,])
func_80 = relay.Function([var_62,], output)
mod['func_80'] = func_80
mod = relay.transform.InferType()(mod)
mutated_mod['func_80'] = func_80
mutated_mod = relay.transform.InferType()(mutated_mod)
var_81 = relay.var("var_81", dtype = "float64", shape = (5, 6, 11))#candidate|81|(5, 6, 11)|var|float64
func_80_call = mutated_mod.get_global_var('func_80')
call_82 = func_80_call(var_81)
output = call_82
func_83 = relay.Function([var_81], output)
mutated_mod['func_83'] = func_83
mutated_mod = relay.transform.InferType()(mutated_mod)
var_110 = relay.var("var_110", dtype = "uint64", shape = (8, 4, 13))#candidate|110|(8, 4, 13)|var|uint64
var_111 = relay.var("var_111", dtype = "uint64", shape = (8, 4, 13))#candidate|111|(8, 4, 13)|var|uint64
bop_112 = relay.greater_equal(var_110.astype('bool'), relay.reshape(var_111.astype('bool'), relay.shape_of(var_110))) # shape=(8, 4, 13)
uop_122 = relay.sigmoid(var_111.astype('float64')) # shape=(8, 4, 13)
output = relay.Tuple([bop_112,uop_122,])
output2 = relay.Tuple([bop_112,uop_122,])
func_132 = relay.Function([var_110,var_111,], output)
mod['func_132'] = func_132
mod = relay.transform.InferType()(mod)
mutated_mod['func_132'] = func_132
mutated_mod = relay.transform.InferType()(mutated_mod)
func_132_call = mutated_mod.get_global_var('func_132')
var_134 = relay.var("var_134", dtype = "uint64", shape = (8, 4, 13))#candidate|134|(8, 4, 13)|var|uint64
var_135 = relay.var("var_135", dtype = "uint64", shape = (8, 4, 13))#candidate|135|(8, 4, 13)|var|uint64
call_133 = func_132_call(var_134,var_135,)
output = call_133
func_136 = relay.Function([var_134,var_135,], output)
mutated_mod['func_136'] = func_136
mutated_mod = relay.transform.InferType()(mutated_mod)
const_314 = relay.const([[[True,False,False,True,True,True,True,True,False,False,False,True,False],[True,True,True,False,True,False,False,False,True,False,True,True,False],[True,True,False,True,True,True,True,True,False,False,False,True,False],[False,False,False,True,False,True,False,True,True,False,True,True,False],[True,True,False,False,False,True,False,False,False,True,False,True,True],[False,True,True,False,True,False,False,True,True,False,False,False,True],[True,False,False,True,False,True,False,False,False,False,True,False,True]],[[True,True,True,False,False,True,False,False,True,True,False,True,True],[True,True,True,True,False,True,True,True,False,False,False,False,False],[False,True,False,False,False,True,False,True,False,False,False,False,False],[False,True,False,True,False,False,True,False,True,True,True,True,False],[True,True,True,True,True,True,False,True,False,False,True,False,True],[True,False,False,True,True,False,False,True,True,True,True,False,True],[True,False,False,False,False,True,True,True,False,False,True,True,False]],[[True,True,True,True,True,False,True,True,True,False,True,True,False],[False,False,True,True,True,False,True,True,False,True,False,True,True],[True,False,False,False,False,True,True,True,False,False,True,True,True],[False,False,False,True,False,True,False,True,False,True,False,True,True],[False,False,True,False,True,False,False,True,False,False,False,False,True],[False,False,False,False,False,False,False,False,True,False,True,True,True],[True,True,True,False,False,False,True,True,False,False,False,False,False]],[[False,False,False,False,True,True,True,True,True,True,True,True,True],[False,True,True,False,False,False,True,False,True,True,False,False,False],[False,False,False,False,False,True,False,True,True,True,False,False,False],[True,True,True,False,True,True,True,False,True,True,False,False,True],[True,True,True,True,False,True,False,False,True,False,True,True,True],[True,False,True,True,False,False,True,True,False,False,True,True,False],[False,True,False,True,False,False,False,False,True,False,True,True,True]],[[True,False,False,False,True,True,True,True,True,True,True,False,True],[False,False,False,True,False,False,False,False,True,True,False,False,True],[False,False,False,True,True,True,True,False,False,True,True,True,False],[False,False,True,False,True,True,False,True,True,False,False,True,True],[True,False,True,True,True,True,False,False,True,True,True,False,True],[True,True,True,False,True,True,True,True,False,False,False,False,False],[True,True,False,True,False,True,True,True,True,True,True,True,True]],[[False,False,False,False,False,False,False,True,False,True,False,True,False],[False,False,True,True,False,False,False,False,True,False,True,True,True],[False,False,False,True,True,False,False,True,True,False,True,True,True],[False,False,True,True,True,False,True,False,True,True,False,True,True],[False,True,True,True,False,True,True,True,True,False,True,True,True],[False,True,True,True,False,True,False,True,False,True,True,False,True],[False,True,True,True,True,True,False,False,False,True,True,True,False]],[[False,True,True,True,True,False,False,False,True,False,True,True,False],[True,False,True,True,True,False,True,True,True,False,False,False,False],[True,True,True,False,True,False,False,False,True,True,False,False,True],[False,False,False,True,False,True,False,False,True,True,False,False,False],[True,False,True,True,False,False,False,True,False,True,True,False,False],[True,True,False,True,False,False,True,False,False,False,False,False,False],[True,True,False,True,False,True,True,True,True,True,True,True,False]],[[True,True,False,False,True,True,True,True,False,False,False,True,False],[False,True,False,False,True,True,True,True,False,True,True,True,False],[False,False,True,True,True,True,False,True,True,True,False,False,True],[False,False,True,True,True,True,True,True,True,False,True,False,False],[True,False,True,True,False,True,True,False,False,False,True,True,True],[False,False,True,False,True,True,True,False,True,False,True,False,True],[False,False,False,True,False,False,True,True,True,True,False,False,True]],[[True,True,False,False,False,False,False,False,True,False,True,False,False],[False,False,False,False,True,False,True,False,True,True,False,False,True],[True,False,True,True,True,False,False,False,False,True,False,True,True],[True,True,False,True,True,True,True,True,True,True,False,False,True],[True,False,True,False,True,False,False,False,True,True,True,False,True],[True,True,False,False,False,True,True,False,True,True,True,False,False],[True,True,False,True,False,False,True,True,False,False,True,False,True]]], dtype = "bool")#candidate|314|(9, 7, 13)|const|bool
var_315 = relay.var("var_315", dtype = "bool", shape = (9, 7, 13))#candidate|315|(9, 7, 13)|var|bool
bop_316 = relay.logical_or(const_314.astype('bool'), relay.reshape(var_315.astype('bool'), relay.shape_of(const_314))) # shape=(9, 7, 13)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
var_344 = relay.var("var_344", dtype = "uint64", shape = (416,))#candidate|344|(416,)|var|uint64
call_343 = relay.TupleGetItem(func_132_call(relay.reshape(var_344.astype('uint64'), [8, 4, 13]), relay.reshape(var_344.astype('uint64'), [8, 4, 13]), ), 1)
call_345 = relay.TupleGetItem(func_136_call(relay.reshape(var_344.astype('uint64'), [8, 4, 13]), relay.reshape(var_344.astype('uint64'), [8, 4, 13]), ), 1)
func_80_call = mod.get_global_var('func_80')
func_83_call = mutated_mod.get_global_var('func_83')
const_347 = relay.const([-0.524161,4.837375,-9.481628,-3.936254,3.467134,-0.337325,8.501073,3.900570,-8.028772,-7.436499,4.208501,5.631578,-4.028702,-9.241566,7.152490,-5.695892,6.507594,-1.120279,9.977364,-4.223232,-4.703176,-8.498449,4.228224,-5.440382,2.152151,-0.521019,-5.723007,0.812994,0.291450,-8.249741,-8.358024,-8.170935,4.699301,6.663526,-1.752167,6.342038,-0.175324,-4.326585,-0.242625,6.258438,-2.840719,-7.468946,9.925025,5.588259,-9.805727,1.687728,-5.302775,-3.316497,-4.131173,-9.606544,2.445092,-2.479606,-1.905102,-4.777537,1.830577,-3.157044,0.338975,-1.566291,4.847236,8.827148,-3.855358,-2.416095,8.562794,-0.942685,-5.320710,-6.358299,-3.349052,2.149477,0.993796,2.628849,8.918436,-3.066631,4.860374,-4.127137,-2.945681,-1.841042,-4.762792,-6.586816,5.538502,-5.988398,8.817254,7.252649,3.783713,-4.801221,-5.172082,3.165730,-2.675030,-4.044464,-3.867148,-0.441708,5.091282,8.502156,4.167948,4.587084,-8.106298,-7.570689,-8.528790,-2.560604,-9.803710,-2.999105,-3.925797,-4.591471,-2.295417,-9.602788,9.841163,5.758179,1.655764,2.075957,-9.631162,8.365103,-7.549754,8.497141,-1.761796,-0.087705,-8.948700,5.766961,-7.518923,1.424969,6.838805,2.118299,-9.987273,9.199118,-1.650780,-6.443520,7.824989,9.239330,4.581634,-8.828083,-9.293633,-8.738385,2.129217,-1.413693,-8.705496,-0.147658,7.218411,-3.741996,5.262625,-6.733419,-8.933938,-8.361724,-2.958554,4.684288,-6.119871,1.026550,-9.137214,-5.978488,-8.871800,1.132030,-4.160830,-4.303245,-3.419578,-1.293459,-8.902134,3.366869,8.114262,-8.441670,9.215416,-2.882331,2.440001,5.011066,2.994067,9.926039,-7.172025,-1.972841,3.155803,-9.497701,-0.945057,9.995954,9.696407,8.391173,-7.761936,8.618823,-4.629467,-5.917948,6.847160,0.114471,7.841276,-7.791900,-0.695826,-2.393544,9.278673,4.435466,1.861453,-6.494891,1.681685,-4.521201,4.653344,0.454217,2.466316,6.368244,8.572936,8.151708,-0.033657,-1.271155,4.888894,-1.398650,-9.953563,-1.438797,-9.381535,-4.566953,-3.621652,2.393250,-2.313006,7.330716,-1.746645,8.710104,-0.809172,-1.154202,-3.041189,7.433333,-4.714261,1.031908,2.298488,-0.184418,-0.230803,5.841575,2.162842,8.072784,6.057361,7.335566,8.576180,-5.696641,-7.647282,-7.831800,7.934682,-5.898230,8.797310,-8.955544,3.678155,-9.744267,-6.399292,-3.864484,0.577721,9.370877,3.173595,-6.062149,9.530124,-2.038255,-1.354879,5.919584,-0.992576,6.639682,3.155333,-2.844823,-5.769891,-8.897571,-1.782416,3.668839,-0.551822,-3.322246,0.807058,7.207821,9.185413,-5.748472,-7.633500,-2.956016,2.586341,0.124265,3.577221,4.179504,-3.425026,-1.762165,3.765066,-3.578646,1.283576,1.178671,-7.708715,0.179313,-5.612765,9.092057,4.199767,7.976796,8.907937,7.108901,-2.240729,-3.810096,4.910975,7.450275,-5.608789,-6.406145,-5.277644,9.331996,-8.952890,5.414862,-4.680644,-2.073903,-1.698047,9.167597,-7.692557,-8.795557,6.161454,4.531019,-6.488130,2.215089,1.471144,-9.194558,3.324708,-6.630224,-4.481332,-2.638343,-9.560767,3.013034,-5.118678,-6.210968,3.380625,8.413113,4.986238,8.615507,3.371759,8.679918,4.823362,5.411511,1.590088,-4.183069,5.196668,-9.870320,1.767158,-4.338351,-6.647827,-8.926174,4.063452,4.583285,6.274521,-3.704239,9.379114,5.740265,3.755020,-2.651082,-0.156239,3.606287], dtype = "float64")#candidate|347|(330,)|const|float64
call_346 = relay.TupleGetItem(func_80_call(relay.reshape(const_347.astype('float64'), [5, 6, 11])), 1)
call_348 = relay.TupleGetItem(func_83_call(relay.reshape(const_347.astype('float64'), [5, 6, 11])), 1)
bop_350 = relay.equal(var_315.astype('bool'), relay.reshape(bop_316.astype('bool'), relay.shape_of(var_315))) # shape=(9, 7, 13)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
call_353 = relay.TupleGetItem(func_132_call(relay.reshape(call_343.astype('uint64'), [8, 4, 13]), relay.reshape(call_343.astype('uint64'), [8, 4, 13]), ), 0)
call_354 = relay.TupleGetItem(func_136_call(relay.reshape(call_343.astype('uint64'), [8, 4, 13]), relay.reshape(call_343.astype('uint64'), [8, 4, 13]), ), 0)
bop_359 = relay.add(call_353.astype('uint8'), relay.reshape(call_343.astype('uint8'), relay.shape_of(call_353))) # shape=(8, 4, 13)
bop_362 = relay.add(call_354.astype('uint8'), relay.reshape(call_345.astype('uint8'), relay.shape_of(call_354))) # shape=(8, 4, 13)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
call_369 = relay.TupleGetItem(func_132_call(relay.reshape(call_353.astype('uint64'), [8, 4, 13]), relay.reshape(call_353.astype('uint64'), [8, 4, 13]), ), 1)
call_370 = relay.TupleGetItem(func_136_call(relay.reshape(call_353.astype('uint64'), [8, 4, 13]), relay.reshape(call_353.astype('uint64'), [8, 4, 13]), ), 1)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
call_376 = relay.TupleGetItem(func_132_call(relay.reshape(call_353.astype('uint64'), [8, 4, 13]), relay.reshape(var_344.astype('uint64'), [8, 4, 13]), ), 0)
call_377 = relay.TupleGetItem(func_136_call(relay.reshape(call_353.astype('uint64'), [8, 4, 13]), relay.reshape(var_344.astype('uint64'), [8, 4, 13]), ), 0)
const_379 = relay.const([[[False,False,False,True,False,True,True,True,True,True,False,True,True],[True,False,False,True,True,False,False,False,False,False,False,True,True],[True,False,True,True,False,True,True,False,False,True,True,False,False],[True,True,False,False,False,True,True,False,False,False,False,False,True],[False,False,True,True,False,False,False,True,True,False,False,True,True],[True,False,False,True,True,True,False,True,False,False,True,True,True],[True,True,True,False,False,False,False,True,True,False,True,True,True]],[[True,False,False,False,True,True,False,True,False,True,True,False,True],[True,False,False,False,True,True,True,True,True,False,True,False,True],[False,False,True,False,False,False,False,False,False,True,True,False,False],[True,False,True,True,True,False,True,True,False,True,False,False,False],[False,False,True,False,True,True,False,False,True,False,False,True,False],[False,False,True,True,True,False,True,False,True,False,True,True,True],[True,False,True,True,False,True,True,True,True,True,False,False,True]],[[False,False,False,True,True,False,False,False,True,True,True,False,True],[False,False,False,True,True,False,True,True,True,True,False,True,False],[False,False,True,False,True,True,False,True,False,True,False,False,False],[True,True,True,False,True,True,False,True,True,False,True,False,True],[True,False,True,False,False,True,False,True,True,True,False,False,True],[True,True,True,True,True,False,True,False,False,False,False,True,True],[True,True,True,True,False,False,True,True,False,False,True,False,True]],[[False,True,False,False,False,True,False,True,False,True,False,True,False],[False,True,False,True,True,True,False,False,False,False,False,False,False],[False,False,True,False,True,True,True,True,False,False,False,False,True],[True,True,True,False,True,False,False,True,True,True,False,False,True],[True,False,True,True,False,True,True,True,True,False,True,False,False],[True,False,False,True,False,True,False,True,False,False,True,False,True],[True,True,False,True,False,True,True,True,False,False,False,True,True]],[[True,True,False,True,True,True,False,False,False,False,True,True,True],[True,True,True,True,False,False,False,False,True,False,True,False,True],[True,False,True,False,False,False,False,False,False,True,False,False,True],[False,False,True,True,True,False,False,False,False,True,False,False,True],[True,True,True,False,False,False,False,False,True,False,False,True,True],[False,False,True,False,False,True,False,True,True,False,True,True,False],[True,False,True,False,False,False,True,True,False,True,True,True,True]],[[False,True,False,True,False,False,False,True,True,False,True,True,True],[False,True,False,True,False,False,False,True,False,False,True,True,True],[False,False,False,True,False,True,False,False,False,True,False,False,False],[True,False,True,True,True,True,False,False,True,False,False,True,True],[False,True,True,True,False,True,True,False,False,True,True,False,True],[False,True,False,False,False,True,True,True,False,False,True,True,False],[False,True,False,True,True,False,False,False,True,False,True,True,False]],[[True,False,False,True,False,False,True,False,False,True,True,True,False],[False,False,True,True,False,True,False,True,False,True,True,False,True],[True,False,False,False,True,True,False,True,True,False,True,False,False],[True,True,False,True,True,False,True,True,True,True,False,True,False],[True,True,False,True,False,True,False,True,True,True,False,True,False],[True,False,True,True,False,False,False,False,True,False,False,False,True],[True,False,True,True,False,False,False,False,False,False,True,False,True]],[[False,True,False,False,True,True,False,False,True,False,False,True,True],[False,True,True,False,False,True,False,False,False,True,False,False,True],[False,False,True,False,False,True,True,False,True,False,True,True,False],[False,False,True,False,True,True,True,False,True,False,True,False,False],[True,True,False,True,False,True,False,True,True,False,True,True,False],[False,True,True,False,False,False,False,True,False,True,False,True,True],[True,True,True,True,True,False,False,False,False,True,True,False,False]],[[False,False,True,True,False,False,True,True,False,True,True,False,False],[True,True,False,True,False,True,False,True,True,False,False,True,False],[False,False,True,False,True,True,False,False,True,False,False,False,True],[False,True,True,False,True,False,True,True,True,False,False,False,True],[True,False,True,True,False,True,True,True,True,False,False,True,True],[True,True,True,True,True,False,False,False,False,True,False,False,False],[False,False,True,False,True,False,False,True,True,False,False,True,True]]], dtype = "bool")#candidate|379|(9, 7, 13)|const|bool
bop_380 = relay.not_equal(var_315.astype('bool'), relay.reshape(const_379.astype('bool'), relay.shape_of(var_315))) # shape=(9, 7, 13)
uop_384 = relay.cosh(bop_380.astype('float64')) # shape=(9, 7, 13)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
call_390 = relay.TupleGetItem(func_132_call(relay.reshape(call_376.astype('uint64'), [8, 4, 13]), relay.reshape(var_344.astype('uint64'), [8, 4, 13]), ), 1)
call_391 = relay.TupleGetItem(func_136_call(relay.reshape(call_376.astype('uint64'), [8, 4, 13]), relay.reshape(var_344.astype('uint64'), [8, 4, 13]), ), 1)
uop_397 = relay.exp(uop_384.astype('float64')) # shape=(9, 7, 13)
func_80_call = mod.get_global_var('func_80')
func_83_call = mutated_mod.get_global_var('func_83')
call_408 = relay.TupleGetItem(func_80_call(relay.reshape(call_346.astype('float64'), [5, 6, 11])), 0)
call_409 = relay.TupleGetItem(func_83_call(relay.reshape(call_346.astype('float64'), [5, 6, 11])), 0)
uop_419 = relay.tan(uop_384.astype('float64')) # shape=(9, 7, 13)
output = relay.Tuple([var_344,call_346,const_347,bop_350,bop_359,call_369,call_376,call_390,uop_397,call_408,uop_419,])
output2 = relay.Tuple([var_344,call_348,const_347,bop_350,bop_362,call_370,call_377,call_391,uop_397,call_409,uop_419,])
func_421 = relay.Function([var_315,var_344,], output)
mod['func_421'] = func_421
mod = relay.transform.InferType()(mod)
mutated_mod['func_421'] = func_421
mutated_mod = relay.transform.InferType()(mutated_mod)
func_421_call = mutated_mod.get_global_var('func_421')
var_423 = relay.var("var_423", dtype = "bool", shape = (9, 7, 13))#candidate|423|(9, 7, 13)|var|bool
var_424 = relay.var("var_424", dtype = "uint64", shape = (416,))#candidate|424|(416,)|var|uint64
call_422 = func_421_call(var_423,var_424,)
output = call_422
func_425 = relay.Function([var_423,var_424,], output)
mutated_mod['func_425'] = func_425
mutated_mod = relay.transform.InferType()(mutated_mod)
const_844 = relay.const([[[4.919782,-2.842904,-5.523079,4.398960,5.445095,0.152407,2.267931,-4.612531,-1.297215,3.593145,-9.637763,-1.107754,-0.141723,9.328866,-5.162239],[4.058450,8.015480,6.297903,-5.011502,6.322180,8.655663,8.633064,8.839282,-6.114027,-8.009123,-5.848583,9.325954,-3.720193,-1.501908,3.986160],[6.979487,-0.189987,-8.663332,-0.812780,-2.225538,8.520430,-3.078890,9.493530,-8.485919,-5.365111,1.702179,1.051855,8.963178,-9.032698,8.887687]],[[5.414704,5.607882,-9.923849,9.182628,-9.152419,-4.696464,5.760625,-1.332048,-4.823003,-8.086266,8.531865,1.407038,-8.893964,0.695973,-8.379783],[7.104904,5.428675,-9.547311,-8.911545,-7.037155,7.470153,-4.677516,-3.472153,1.083758,6.505519,8.537212,3.598180,3.213308,7.550435,5.777394],[-2.195367,0.537885,7.499643,8.094295,3.526624,-9.077287,-7.426810,8.098380,-1.989164,-2.605731,-8.530720,-6.324175,-6.732730,-0.433413,-0.100478]],[[-9.079879,-3.905674,-4.881501,8.820061,2.383202,-8.337694,7.680259,6.554650,3.105915,-3.383078,4.203229,2.701918,-6.304027,-2.430424,5.823438],[-7.436669,4.591679,-0.079955,-3.456303,8.056917,-3.906090,-9.927166,-5.598797,7.468839,5.153012,6.523933,-3.140122,-6.215014,4.974024,9.445203],[-8.803277,-5.780714,-8.754371,9.010966,-8.486141,5.503017,-2.982311,-2.396408,4.920624,-5.719989,9.456086,0.464143,-8.065350,6.731940,-0.304255]],[[1.228647,-4.613111,-6.999682,-4.229177,-4.769955,-4.024025,3.119412,7.960696,-5.843862,9.535904,1.771876,-4.228170,4.110018,-8.545685,-0.578906],[8.047582,7.125085,2.112763,3.256562,-8.627912,-2.653655,0.748529,8.571287,-2.526819,0.753183,1.784464,-4.045593,4.865705,-7.648435,-0.459635],[4.296419,-9.393122,-2.804461,-5.875853,2.889243,2.278003,-2.520294,-1.427256,5.101514,3.018862,-8.873857,1.051346,-6.569292,-1.789595,-8.091976]],[[-3.231861,9.533455,7.276876,-3.306984,0.208130,-5.627979,-2.682552,1.302067,-1.782011,6.225441,0.763775,-6.539527,-5.942677,8.551431,-4.736112],[-0.865098,0.748095,6.882757,4.965664,8.829093,-7.934081,0.639402,-1.388325,8.883528,5.737087,-1.989658,-6.975170,5.605466,3.226423,-3.118884],[-1.503811,-3.479721,-0.183327,-9.654497,-5.604188,-6.564072,0.047172,7.922897,-4.143481,1.705586,2.410206,-2.327096,-8.542804,-7.437729,-5.062362]],[[9.260000,1.952324,0.981448,-6.617675,5.522250,1.428416,8.819874,6.680055,-1.557357,4.581834,5.574146,9.203912,-2.695987,8.203701,2.036154],[3.885558,2.647178,7.762812,-6.480279,-3.356433,-3.857701,5.486496,7.904025,-0.389789,-9.011426,4.421265,-1.921501,7.972510,-9.664445,2.772126],[1.036114,6.726932,-7.892582,4.838898,-8.820522,-8.425985,2.316464,-1.993465,0.190888,-2.754879,-2.593248,4.876543,-3.711186,2.601071,-3.858420]],[[-6.237866,-9.247107,-4.672787,-0.094469,0.503342,7.192410,9.038686,-6.819509,1.340857,-4.014859,1.294966,3.816653,6.285666,-5.785751,4.735431],[-7.489285,-6.811048,9.854542,9.469211,-2.473370,-6.090633,-0.568327,-8.565789,2.068045,-1.206314,7.118955,-1.230863,9.758882,-5.912477,-0.201430],[-3.222839,7.739804,0.816253,4.593356,0.311244,-4.981000,8.134697,2.174696,3.896598,-2.476607,3.178778,4.442693,-1.604088,2.292709,-5.408269]],[[-3.779961,-5.971606,2.721550,-3.152471,-1.117793,-4.996899,3.177783,-2.447373,4.906088,6.549732,2.665652,2.203206,-7.612121,4.606669,-0.973326],[-5.094817,-9.191160,4.331215,-2.367464,-8.405067,6.923735,6.642711,1.116415,8.051877,4.783135,-9.026229,2.034848,-7.777104,0.334377,-0.163941],[0.659532,1.470687,2.141957,-6.791382,-8.294276,0.724486,2.714167,0.739250,-9.217882,-1.936344,9.955211,-8.038839,-5.278900,6.722070,3.758365]],[[-6.023978,-3.437266,-2.352654,-9.423370,1.124199,-7.847386,-6.542564,-6.114765,-6.144206,-1.848254,-1.302594,7.675329,4.885292,0.312463,0.867693],[-7.544118,-1.048498,3.351682,-2.915504,1.168781,7.835754,-2.612608,8.118643,4.522760,0.154261,-6.204716,1.626486,4.169637,-2.895672,3.676847],[9.269157,4.168889,-6.528164,-6.460383,-3.287370,1.537962,7.577453,2.051953,-6.509608,-9.894502,-6.223036,5.216940,-7.571476,-1.478242,-0.645489]],[[4.265750,7.533849,5.351874,3.209217,1.237020,6.490894,8.315229,-1.853745,4.342073,6.070975,1.468067,2.269424,-8.356409,6.934442,-9.456151],[-0.448181,3.844837,-9.857006,-9.420927,-6.835752,0.906927,-5.494238,8.000539,0.273934,7.028046,-6.519410,-6.454570,2.565478,-7.150677,-7.406810],[-0.692636,-1.059094,-1.119660,-4.888359,-6.988697,-6.381258,-3.834561,3.226089,-7.973591,5.210393,0.931075,-4.737969,7.688423,-4.891999,-5.835543]],[[-1.450541,-0.084600,-1.476369,5.882213,4.285489,3.565587,6.687925,-2.395064,9.504504,4.325737,-5.575493,2.681730,-4.871534,-4.850553,-7.375690],[6.287421,-5.297043,1.325227,6.844734,7.701841,-4.394878,-6.560730,3.318078,-7.320677,3.846195,9.477919,5.104109,-3.781185,3.605420,-3.250532],[5.117905,-6.592978,6.910984,-3.727155,-0.846864,8.193721,6.130285,-2.243648,-0.533208,3.913420,-3.388695,1.399987,5.348928,0.256666,8.000626]],[[-6.032069,-2.918882,-5.938072,-7.833099,-1.187856,-8.824429,-1.058042,0.166084,-0.120360,2.400463,-4.033462,-5.864674,0.598764,2.196358,-2.814286],[7.492282,-4.874235,2.235095,1.127307,5.695349,-8.932534,-4.532650,2.092615,8.493101,4.227257,-6.876517,-3.056530,-0.624138,-5.886665,4.832438],[-1.469810,-3.066812,-7.417280,6.877011,1.247093,0.994667,-7.563149,-9.772530,3.652810,-2.250832,3.763859,-1.687540,4.743328,2.011097,3.652867]],[[1.065733,6.831113,-6.475232,2.893860,-8.697640,-0.499290,7.148980,8.104952,5.027563,9.303975,3.810217,-2.349580,4.046528,-2.701781,4.418710],[8.293992,2.634150,-8.024681,-5.466490,9.361405,9.770088,-2.141531,8.598188,-3.980241,-6.907977,-7.687214,-9.076436,-9.928497,-8.639214,6.733511],[-6.487985,-4.205893,9.803028,0.964290,5.468366,-5.390538,-5.708382,9.475103,-5.341812,-1.076437,7.411088,3.252428,2.612236,9.373628,-9.372431]]], dtype = "float32")#candidate|844|(13, 3, 15)|const|float32
uop_845 = relay.log(const_844.astype('float32')) # shape=(13, 3, 15)
func_421_call = mod.get_global_var('func_421')
func_425_call = mutated_mod.get_global_var('func_425')
var_857 = relay.var("var_857", dtype = "bool", shape = (819,))#candidate|857|(819,)|var|bool
const_858 = relay.const([8,-5,6,-1,-6,9,8,-1,-3,-7,5,-10,-8,9,9,-10,-10,7,-2,8,9,-9,-7,10,-1,4,-10,-4,1,-4,9,-7,-9,-4,-5,9,10,-1,-8,-4,7,4,-2,6,2,-6,-4,-10,9,3,4,8,-10,10,9,7,-2,3,-9,-9,-9,-2,10,-7,3,3,-4,3,9,3,9,-5,-1,5,9,1,-9,-2,-4,-7,9,-6,2,-8,-5,2,1,7,6,-1,5,3,-4,4,2,-5,-3,7,-2,-10,-5,3,8,7,-1,8,-10,-4,6,2,-1,-2,-10,2,3,1,4,4,-3,5,7,3,-6,4,5,9,-5,-10,9,6,-6,8,2,-10,-2,10,10,-9,-10,-8,10,-9,-10,1,3,-9,-6,-6,10,-5,5,-4,-9,-1,7,-4,-9,-6,-3,8,6,-6,-8,-3,10,-3,-3,10,-1,3,-2,-6,1,2,1,-2,7,9,2,-4,-10,-7,-3,7,10,1,-8,-5,-1,4,4,8,6,7,-9,-10,7,2,-6,3,10,10,-10,-8,9,-2,-10,8,-8,-3,7,4,3,-3,6,5,-9,3,-9,2,-4,4,-5,-9,-7,-9,-8,-8,10,7,9,-9,8,-8,4,-4,-6,-4,9,3,-8,10,-7,4,-10,-1,-5,-9,-4,-10,9,-7,-2,-6,-6,9,-3,-7,-7,-6,-6,-8,-7,5,-4,-10,-9,-7,-9,4,-4,-7,-9,-5,-9,-3,-10,-5,-8,8,3,2,-6,5,-2,1,9,2,6,6,10,8,10,7,-4,-9,-5,-1,2,6,-4,-9,-7,-4,-10,-6,-10,10,-10,10,-4,-10,-10,9,8,5,4,-6,-4,-4,1,-5,-6,2,6,9,9,-8,-2,-10,-4,-4,-10,9,-3,10,-5,-6,2,7,10,-9,-5,9,-3,2,5,-6,-8,-8,-8,-6,5,-3,10,6,-8,-10,-9,-4,7,2,10,8,2,1,-6,4,1,-6,-9,-10,7,-2,8,-1,-10,8,10,9,3,4,1,9,-5,-2,9,-1,-3,-3,9,-7,-6,10,-2,-7,-3,2,-9,3,-8,-10,8,-3,6,-1,7,-5,-4,8,6,-10,-8,-10,-5,-3], dtype = "uint64")#candidate|858|(416,)|const|uint64
call_856 = relay.TupleGetItem(func_421_call(relay.reshape(var_857.astype('bool'), [9, 7, 13]), relay.reshape(const_858.astype('uint64'), [416,]), ), 3)
call_859 = relay.TupleGetItem(func_425_call(relay.reshape(var_857.astype('bool'), [9, 7, 13]), relay.reshape(const_858.astype('uint64'), [416,]), ), 3)
func_80_call = mod.get_global_var('func_80')
func_83_call = mutated_mod.get_global_var('func_83')
var_872 = relay.var("var_872", dtype = "float64", shape = (330,))#candidate|872|(330,)|var|float64
call_871 = relay.TupleGetItem(func_80_call(relay.reshape(var_872.astype('float64'), [5, 6, 11])), 0)
call_873 = relay.TupleGetItem(func_83_call(relay.reshape(var_872.astype('float64'), [5, 6, 11])), 0)
func_80_call = mod.get_global_var('func_80')
func_83_call = mutated_mod.get_global_var('func_83')
call_874 = relay.TupleGetItem(func_80_call(relay.reshape(call_871.astype('float64'), [5, 6, 11])), 0)
call_875 = relay.TupleGetItem(func_83_call(relay.reshape(call_871.astype('float64'), [5, 6, 11])), 0)
func_421_call = mod.get_global_var('func_421')
func_425_call = mutated_mod.get_global_var('func_425')
call_877 = relay.TupleGetItem(func_421_call(relay.reshape(var_857.astype('bool'), [9, 7, 13]), relay.reshape(const_858.astype('uint64'), [416,]), ), 5)
call_878 = relay.TupleGetItem(func_425_call(relay.reshape(var_857.astype('bool'), [9, 7, 13]), relay.reshape(const_858.astype('uint64'), [416,]), ), 5)
func_80_call = mod.get_global_var('func_80')
func_83_call = mutated_mod.get_global_var('func_83')
call_883 = relay.TupleGetItem(func_80_call(relay.reshape(var_872.astype('float64'), [5, 6, 11])), 0)
call_884 = relay.TupleGetItem(func_83_call(relay.reshape(var_872.astype('float64'), [5, 6, 11])), 0)
uop_891 = relay.sigmoid(uop_845.astype('float64')) # shape=(13, 3, 15)
var_896 = relay.var("var_896", dtype = "float32", shape = (13, 3, 15))#candidate|896|(13, 3, 15)|var|float32
bop_897 = relay.greater_equal(uop_845.astype('bool'), relay.reshape(var_896.astype('bool'), relay.shape_of(uop_845))) # shape=(13, 3, 15)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
call_900 = relay.TupleGetItem(func_132_call(relay.reshape(call_877.astype('uint64'), [8, 4, 13]), relay.reshape(const_858.astype('uint64'), [8, 4, 13]), ), 1)
call_901 = relay.TupleGetItem(func_136_call(relay.reshape(call_877.astype('uint64'), [8, 4, 13]), relay.reshape(const_858.astype('uint64'), [8, 4, 13]), ), 1)
var_907 = relay.var("var_907", dtype = "float32", shape = (13, 3, 15))#candidate|907|(13, 3, 15)|var|float32
bop_908 = relay.bitwise_xor(uop_845.astype('int8'), relay.reshape(var_907.astype('int8'), relay.shape_of(uop_845))) # shape=(13, 3, 15)
output = relay.Tuple([call_856,var_857,const_858,call_871,var_872,call_874,call_877,call_883,uop_891,bop_897,call_900,bop_908,])
output2 = relay.Tuple([call_859,var_857,const_858,call_873,var_872,call_875,call_878,call_884,uop_891,bop_897,call_901,bop_908,])
func_914 = relay.Function([var_857,var_872,var_896,var_907,], output)
mod['func_914'] = func_914
mod = relay.transform.InferType()(mod)
var_915 = relay.var("var_915", dtype = "bool", shape = (819,))#candidate|915|(819,)|var|bool
var_916 = relay.var("var_916", dtype = "float64", shape = (330,))#candidate|916|(330,)|var|float64
var_917 = relay.var("var_917", dtype = "float32", shape = (13, 3, 15))#candidate|917|(13, 3, 15)|var|float32
var_918 = relay.var("var_918", dtype = "float32", shape = (13, 3, 15))#candidate|918|(13, 3, 15)|var|float32
output = func_914(var_915,var_916,var_917,var_918,)
func_919 = relay.Function([var_915,var_916,var_917,var_918,], output)
mutated_mod['func_919'] = func_919
mutated_mod = relay.transform.InferType()(mutated_mod)
var_955 = relay.var("var_955", dtype = "float32", shape = (7, 7, 3))#candidate|955|(7, 7, 3)|var|float32
uop_956 = relay.log10(var_955.astype('float32')) # shape=(7, 7, 3)
output = relay.Tuple([uop_956,])
output2 = relay.Tuple([uop_956,])
func_963 = relay.Function([var_955,], output)
mod['func_963'] = func_963
mod = relay.transform.InferType()(mod)
var_964 = relay.var("var_964", dtype = "float32", shape = (7, 7, 3))#candidate|964|(7, 7, 3)|var|float32
output = func_963(var_964)
func_965 = relay.Function([var_964], output)
mutated_mod['func_965'] = func_965
mutated_mod = relay.transform.InferType()(mutated_mod)
var_974 = relay.var("var_974", dtype = "float64", shape = (7, 12, 2))#candidate|974|(7, 12, 2)|var|float64
uop_975 = relay.sinh(var_974.astype('float64')) # shape=(7, 12, 2)
uop_988 = relay.atanh(var_974.astype('float64')) # shape=(7, 12, 2)
func_421_call = mod.get_global_var('func_421')
func_425_call = mutated_mod.get_global_var('func_425')
var_993 = relay.var("var_993", dtype = "bool", shape = (819,))#candidate|993|(819,)|var|bool
const_994 = relay.const([[8,7,-7,-7,7,10,-10,-6,5,-1,8,-4,10,-2,3,1,-9,-1,9,1,-5,-9,-1,1,3,-6],[5,-9,-5,-7,-5,10,-7,10,-8,-5,9,5,-3,7,10,6,-3,-4,6,-7,-2,-6,-7,-6,-7,-7],[4,-10,2,-2,1,10,5,-2,-5,-5,-7,5,-9,-8,-9,5,-7,-2,-2,-1,-6,-9,-5,3,2,-9],[9,1,-3,6,-4,-9,6,9,-8,3,3,5,4,10,-6,-3,2,-4,-4,9,1,-10,1,-9,2,-1],[5,-5,-3,-3,3,-5,1,-2,-10,-5,-10,2,-6,10,-2,-3,8,3,2,-2,3,1,-9,-1,5,3],[-10,-9,-3,-4,-2,3,-4,1,4,4,1,1,2,10,-7,5,6,-4,2,8,-5,-4,-7,9,-8,-7],[10,-10,2,-10,-3,-6,10,1,-6,-6,8,-1,4,-4,-5,-1,3,-7,-1,3,5,-2,7,-5,-2,7],[-10,3,-8,-6,2,-8,-7,9,6,-2,9,-4,-9,1,-1,-1,7,-6,-5,-10,8,-1,4,4,9,-1],[-4,-5,5,6,6,-8,3,10,6,4,-7,-10,-2,1,2,10,-8,-1,-2,-10,6,3,-3,9,2,-3],[8,-2,-8,4,4,6,-8,6,5,10,7,3,6,-1,-7,9,-10,8,3,-7,-5,-2,1,-2,-5,8],[-6,4,-4,2,3,-9,-4,10,8,-6,-2,5,-4,10,9,-3,-10,7,-6,-7,2,-2,4,2,9,4],[-6,-5,-6,-2,-2,10,-6,7,-7,10,10,-4,4,-6,-5,6,-1,-2,3,-4,10,6,10,-5,8,6],[7,-2,-7,-8,3,4,5,1,-9,-3,-8,3,4,6,-5,-10,10,5,-4,-10,7,1,7,9,8,4],[-3,-5,-5,9,-1,2,4,-1,-2,-5,4,-10,9,-8,1,4,-9,1,10,-3,10,6,-5,-2,7,-6],[5,-1,-5,-3,9,10,-6,1,10,9,-1,6,2,-7,-7,-8,-10,9,8,-2,9,4,-1,-3,10,3],[-7,-1,8,7,-10,-10,-6,6,2,10,7,7,2,1,4,-5,-2,1,6,-5,-5,-7,-5,4,10,-1]], dtype = "uint64")#candidate|994|(16, 26)|const|uint64
call_992 = relay.TupleGetItem(func_421_call(relay.reshape(var_993.astype('bool'), [9, 7, 13]), relay.reshape(const_994.astype('uint64'), [416,]), ), 8)
call_995 = relay.TupleGetItem(func_425_call(relay.reshape(var_993.astype('bool'), [9, 7, 13]), relay.reshape(const_994.astype('uint64'), [416,]), ), 8)
output = relay.Tuple([uop_975,uop_988,call_992,var_993,const_994,])
output2 = relay.Tuple([uop_975,uop_988,call_995,var_993,const_994,])
func_1001 = relay.Function([var_974,var_993,], output)
mod['func_1001'] = func_1001
mod = relay.transform.InferType()(mod)
var_1002 = relay.var("var_1002", dtype = "float64", shape = (7, 12, 2))#candidate|1002|(7, 12, 2)|var|float64
var_1003 = relay.var("var_1003", dtype = "bool", shape = (819,))#candidate|1003|(819,)|var|bool
output = func_1001(var_1002,var_1003,)
func_1004 = relay.Function([var_1002,var_1003,], output)
mutated_mod['func_1004'] = func_1004
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1041 = relay.var("var_1041", dtype = "float32", shape = (12, 11, 2))#candidate|1041|(12, 11, 2)|var|float32
uop_1042 = relay.cos(var_1041.astype('float32')) # shape=(12, 11, 2)
output = relay.Tuple([uop_1042,])
output2 = relay.Tuple([uop_1042,])
func_1046 = relay.Function([var_1041,], output)
mod['func_1046'] = func_1046
mod = relay.transform.InferType()(mod)
var_1047 = relay.var("var_1047", dtype = "float32", shape = (12, 11, 2))#candidate|1047|(12, 11, 2)|var|float32
output = func_1046(var_1047)
func_1048 = relay.Function([var_1047], output)
mutated_mod['func_1048'] = func_1048
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1176 = relay.var("var_1176", dtype = "int32", shape = (15, 1, 6))#candidate|1176|(15, 1, 6)|var|int32
var_1177 = relay.var("var_1177", dtype = "int32", shape = (15, 8, 6))#candidate|1177|(15, 8, 6)|var|int32
bop_1178 = relay.minimum(var_1176.astype('int32'), var_1177.astype('int32')) # shape=(15, 8, 6)
bop_1181 = relay.logical_and(var_1176.astype('bool'), bop_1178.astype('bool')) # shape=(15, 8, 6)
output = relay.Tuple([bop_1181,])
output2 = relay.Tuple([bop_1181,])
func_1185 = relay.Function([var_1176,var_1177,], output)
mod['func_1185'] = func_1185
mod = relay.transform.InferType()(mod)
var_1186 = relay.var("var_1186", dtype = "int32", shape = (15, 1, 6))#candidate|1186|(15, 1, 6)|var|int32
var_1187 = relay.var("var_1187", dtype = "int32", shape = (15, 8, 6))#candidate|1187|(15, 8, 6)|var|int32
output = func_1185(var_1186,var_1187,)
func_1188 = relay.Function([var_1186,var_1187,], output)
mutated_mod['func_1188'] = func_1188
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1268 = relay.var("var_1268", dtype = "uint8", shape = ())#candidate|1268|()|var|uint8
const_1269 = relay.const([[[10,2,-5,-10,-8,-3,6,4,-3],[7,-2,8,1,-3,3,-6,-5,6],[1,8,-6,-8,-9,6,3,-9,-4],[-7,7,1,3,4,10,-1,5,2],[-4,-2,3,7,3,10,-3,2,8],[-1,-5,-2,4,-7,5,-8,10,-2],[-10,-10,4,-10,-9,-8,-10,-10,3],[-1,5,6,7,-9,-6,1,-9,-8],[-3,2,5,-10,1,1,2,-3,-1],[-7,4,7,-6,-7,3,7,-4,-9]],[[3,3,9,-9,7,8,-2,-8,10],[10,6,-10,-1,-5,8,-5,3,-4],[-3,5,-7,-9,9,-7,3,-6,3],[9,5,-2,-8,-5,-6,-5,-3,10],[-5,-1,6,-5,5,9,-9,5,-4],[6,-5,-5,1,-1,-10,4,-2,2],[-3,9,8,8,-8,-1,10,-4,-10],[8,-9,-4,2,6,3,1,5,-3],[-8,2,4,8,-3,-10,9,2,7],[-7,-4,-4,-1,4,-7,-10,-10,10]],[[-6,-9,-1,9,7,10,-7,-4,9],[1,-4,-7,4,5,8,7,6,-2],[-2,-8,4,4,4,6,7,7,-2],[2,10,9,5,-3,-1,9,-7,4],[-7,-5,-6,8,8,-5,-8,8,6],[-7,5,-1,6,-4,1,6,-6,-10],[-4,8,-2,6,-9,7,4,-6,5],[-9,-1,5,1,-9,4,1,-6,2],[1,-9,2,8,1,9,3,-6,-1],[6,2,-10,3,-4,10,8,-2,6]],[[2,-4,-9,-8,10,-9,-6,-2,-8],[-7,-6,3,-7,-9,-7,-4,8,3],[-10,-2,-6,-1,5,5,8,6,2],[-9,-10,7,3,8,1,1,-4,-4],[-5,5,8,3,9,-9,-1,-10,-7],[10,-10,3,2,5,-6,-6,-1,1],[10,-9,-7,2,9,9,-8,-7,-1],[-2,-4,-7,-3,3,4,7,-10,-3],[-7,5,6,3,4,2,2,-8,-10],[-9,8,1,10,7,8,-8,-6,2]],[[-8,-6,7,-8,4,7,3,-9,2],[4,-1,1,-1,-2,-2,7,-1,2],[2,9,10,-10,-6,3,-10,-9,5],[8,-10,1,7,4,2,8,-10,8],[4,10,-8,7,7,8,-7,6,-1],[1,-6,7,-1,-1,-3,10,8,7],[-10,-5,4,8,2,-9,4,10,-7],[9,-2,-10,1,2,7,-7,-8,5],[-6,3,1,-2,4,-5,8,8,6],[5,-7,7,8,2,-6,8,-1,3]],[[-3,-5,6,-7,-5,6,-4,-9,10],[4,9,6,2,-1,-4,-3,9,5],[1,2,8,7,1,-4,1,-10,3],[-8,-9,8,-5,-2,2,-2,9,8],[1,9,9,-4,-1,-3,-10,1,-1],[-5,-3,-3,-2,7,8,-9,9,3],[-3,-10,-1,9,3,-1,3,1,2],[-1,8,8,-1,6,-6,10,6,-4],[-3,8,-4,-8,-4,-3,2,3,-1],[-5,7,-4,10,2,4,-3,-10,-2]],[[-10,1,1,2,-7,-3,-5,1,-8],[7,-9,-4,-7,-9,-7,-1,-1,-3],[-6,6,-10,-2,-5,-7,7,1,-4],[-8,-3,6,-8,-1,9,1,-8,1],[-6,-1,7,6,-3,-10,3,6,7],[-7,10,5,-1,7,5,-7,10,-4],[7,10,6,-7,-2,-6,-8,3,3],[7,8,7,-9,-4,4,7,7,-3],[1,-3,-4,1,6,-10,-4,6,1],[5,8,1,9,-5,-7,-1,-10,-1]],[[-5,-6,6,1,3,2,-9,-3,10],[8,4,-6,-4,1,-1,-8,-5,-7],[-2,-1,-6,-10,3,1,-9,-1,-4],[6,-3,-2,9,9,6,-5,4,5],[10,-4,-1,6,-8,3,-3,-10,7],[-1,1,2,-5,6,-2,1,8,-7],[-2,7,10,-2,2,-1,1,7,1],[-9,-6,-10,-8,2,-8,-3,4,10],[3,-8,3,5,-3,-8,-2,5,-2],[8,-5,5,1,-4,1,10,-10,-8]],[[10,-9,-6,9,5,-7,8,8,6],[-7,-5,-4,8,10,-2,3,4,7],[10,-9,10,4,1,-1,7,-6,10],[-9,-3,6,-9,-9,10,4,-2,7],[-9,9,-2,9,-8,-4,-4,-7,-1],[-2,2,5,9,-4,-4,-4,9,-5],[4,2,8,10,-8,6,-10,4,-2],[-3,-2,-4,7,1,1,-9,-9,-7],[-7,-6,-4,8,3,-5,5,-9,-7],[1,-1,10,-8,7,9,4,-8,5]],[[-5,5,7,6,-2,-6,6,-2,2],[8,-8,7,6,-3,4,-10,1,6],[7,-9,-6,7,6,10,-9,8,-3],[5,8,8,6,-10,3,-6,-9,9],[-1,7,6,-3,-6,-4,-8,10,9],[-8,4,-1,-6,-7,-1,10,5,-9],[-7,-9,3,-3,4,-9,-1,-5,4],[10,-4,-7,-5,7,6,-2,8,9],[-7,-4,-6,-2,-9,2,7,-5,10],[6,-9,-7,8,-2,-3,10,3,-8]],[[7,6,1,9,-1,-8,6,-6,6],[-4,3,1,-4,5,-2,-8,7,5],[1,5,-8,-3,-5,-1,-2,-5,10],[-4,-6,-4,4,-9,6,-10,-8,1],[7,10,2,-5,6,-1,8,3,-4],[4,8,2,7,-3,6,9,-7,-7],[2,-3,-4,5,2,5,4,8,1],[8,-2,3,2,-1,-2,-7,-10,3],[9,-3,-7,-8,8,-4,8,8,-2],[5,-4,-4,7,-1,4,-9,3,3]],[[-2,2,1,-8,-10,6,-7,8,1],[6,-3,-3,2,-9,7,8,7,9],[7,-4,4,-1,-4,10,2,1,6],[2,7,-4,5,2,-1,-7,-8,9],[4,-3,-10,-2,-3,-8,7,7,-9],[-8,5,6,3,-8,8,-3,9,1],[-10,-2,7,2,-9,-10,3,5,-10],[-6,4,-3,3,-5,3,2,10,-8],[7,1,-10,6,-8,3,-2,10,5],[10,-9,-10,10,8,9,7,8,2]]], dtype = "uint8")#candidate|1269|(12, 10, 9)|const|uint8
bop_1270 = relay.maximum(var_1268.astype('uint8'), const_1269.astype('uint8')) # shape=(12, 10, 9)
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
const_1275 = relay.const([-1.355629,-3.923037,-8.152114,4.956304,9.766715,7.144169,6.807207,-1.791389,-1.462615,0.704783,-8.640387,-3.040170,4.514284,7.235819,7.371253,8.556955,-3.578667,-7.076296,-9.094605,-9.431940,-6.025636,9.134081,-0.115734,4.147943,-0.111180,5.434406,-8.565403,-8.919947,2.593586,-3.104299,6.965331,-7.239368,9.023207,-9.669547,-5.894204,-0.644694,-8.327428,-2.268537,2.182664,5.786770,3.831651,-6.044334,-0.775350,9.674342,-6.528194,4.876029,-6.226585,6.333826,-8.677315,9.240936,3.972262,8.019053,9.853643,-9.454798,-2.539058,-0.736061,9.131195,7.526864,-0.023516,1.250765,-4.161919,-3.317049,-4.076604,7.447675,1.468009,9.306895,-5.822156,-9.952790,6.668701,-6.545486,-1.509457,3.155050,9.968286,9.645808,0.783896,8.605089,1.678503,-8.292403,9.812138,-2.751622,0.618885,9.979434,3.554183,7.538343,6.276888,-6.438905,5.363237,7.882703,-3.300008,-9.711972,3.652134,5.516355,4.773302,-1.466733,7.458201,3.241657,-8.781146,-3.067241,-6.662422,-6.746846,9.607191,6.860129,-6.947231,-8.742536,6.757863,5.616982,-3.685819,-4.622493,-6.312835,-3.954249,8.787741,-7.815468,2.892190,2.992550,3.195761,5.423178,-1.169528,5.051194,1.695933,4.077169,-4.120075,7.013154,-5.062615,-1.856423,-0.309231,-1.166579,-4.057348,3.438873,-2.034390,0.483955,1.887259,-6.818939,5.311316,-6.880331,7.201804,5.948792,-5.664194,-8.826208,-3.958809,-6.862417,-2.962004,6.478436,8.900814,-0.881345,7.717606,9.928531,-7.775767], dtype = "float32")#candidate|1275|(147,)|const|float32
call_1274 = relay.TupleGetItem(func_963_call(relay.reshape(const_1275.astype('float32'), [7, 7, 3])), 0)
call_1276 = relay.TupleGetItem(func_965_call(relay.reshape(const_1275.astype('float32'), [7, 7, 3])), 0)
func_421_call = mod.get_global_var('func_421')
func_425_call = mutated_mod.get_global_var('func_425')
const_1287 = relay.const([False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,False,False,False,False,False,False,True,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,False,True,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,False,True,True], dtype = "bool")#candidate|1287|(819,)|const|bool
const_1288 = relay.const([-3,6,-10,8,-7,-2,3,2,5,4,-8,-4,4,4,7,3,10,-3,2,-4,6,-4,9,4,3,-9,-4,3,7,1,-3,-5,6,5,-3,-6,6,-5,-5,8,8,3,8,-7,-5,10,-3,-3,5,6,9,-7,4,-10,3,-9,5,3,9,-10,-10,-2,-7,3,-5,10,-3,-8,10,-7,6,-6,-9,-6,-10,-1,-9,3,-10,-8,7,8,6,8,2,1,-1,-8,-5,-9,1,3,-6,5,-5,10,2,2,4,6,-5,-3,-3,9,5,2,9,-5,-4,-9,-5,8,9,-7,-10,-8,-7,3,1,-7,1,10,5,-3,8,-5,-2,-10,3,-3,-10,1,-1,-7,-8,7,-4,-9,4,7,5,5,-4,-8,4,-3,-4,2,-9,-8,-5,-8,3,9,9,-9,5,2,1,-8,3,1,-4,-3,-6,-1,5,2,-7,3,-7,8,8,-3,10,-6,-3,-10,-2,1,3,8,3,6,-3,6,3,3,-4,10,8,-6,-5,-9,1,-6,5,-2,6,-10,7,8,-10,1,9,-9,-1,9,3,-4,1,-9,-4,5,-1,8,1,-7,-8,6,-2,-4,9,-9,-3,-9,3,-1,10,-6,10,-8,1,-3,-4,6,-5,-8,-8,-9,2,-5,5,-1,-1,6,10,-6,9,-9,10,10,-10,2,-9,-8,10,-3,1,-1,-10,6,1,10,3,7,-7,-1,-7,-4,7,-7,-5,-3,4,-9,-1,4,-8,5,4,-7,9,7,-2,-4,2,5,2,4,-1,2,-1,-7,-9,-2,-2,-3,4,7,-10,4,-2,7,-6,2,7,1,-10,-7,-9,-1,6,2,-3,-6,1,5,9,-9,-5,2,5,-10,-2,-4,-3,-3,-1,9,-7,-9,8,-6,-5,2,8,-4,1,-7,-8,-5,-8,-10,-5,-2,-7,-3,-4,2,3,-1,-1,-3,-8,5,-3,-7,-9,1,9,8,-6,-2,1,-10,-9,-5,-6,3,1,10,-8,-9,7,3,-5,3,-6,-2,9,9,-2,8,-5,2,9,-1,10,-4,-8,-2,-9,-4,7,10,-7,6,5,9,-5,7,-4,10,6,10,10,9,-6,4,9,1,-7,7,-1,4], dtype = "uint64")#candidate|1288|(416,)|const|uint64
call_1286 = relay.TupleGetItem(func_421_call(relay.reshape(const_1287.astype('bool'), [9, 7, 13]), relay.reshape(const_1288.astype('uint64'), [416,]), ), 10)
call_1289 = relay.TupleGetItem(func_425_call(relay.reshape(const_1287.astype('bool'), [9, 7, 13]), relay.reshape(const_1288.astype('uint64'), [416,]), ), 10)
output = relay.Tuple([bop_1270,call_1274,const_1275,call_1286,const_1287,const_1288,])
output2 = relay.Tuple([bop_1270,call_1276,const_1275,call_1289,const_1287,const_1288,])
func_1314 = relay.Function([var_1268,], output)
mod['func_1314'] = func_1314
mod = relay.transform.InferType()(mod)
mutated_mod['func_1314'] = func_1314
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1315 = relay.var("var_1315", dtype = "uint8", shape = ())#candidate|1315|()|var|uint8
func_1314_call = mutated_mod.get_global_var('func_1314')
call_1316 = func_1314_call(var_1315)
output = call_1316
func_1317 = relay.Function([var_1315], output)
mutated_mod['func_1317'] = func_1317
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1390 = relay.const(-1.359386, dtype = "float32")#candidate|1390|()|const|float32
var_1391 = relay.var("var_1391", dtype = "float32", shape = (4, 12, 15))#candidate|1391|(4, 12, 15)|var|float32
bop_1392 = relay.floor_mod(const_1390.astype('float32'), var_1391.astype('float32')) # shape=(4, 12, 15)
func_1046_call = mod.get_global_var('func_1046')
func_1048_call = mutated_mod.get_global_var('func_1048')
const_1428 = relay.const([6.055333,-3.425640,5.888836,-1.938200,1.969277,-1.941771,3.935269,-2.467046,4.276589,0.068622,0.154875,-4.616134,0.096211,-9.299512,0.634388,0.401087,5.266209,-0.103158,7.813434,5.636574,1.550479,-9.913488,7.285169,5.718225,-9.907415,-3.516650,8.350743,-2.591939,7.757688,6.078595,-2.048415,9.947213,-4.130069,-4.815401,-6.138503,-8.788305,7.585917,3.919218,0.016571,4.661289,3.435603,0.504327,4.208582,5.639792,-7.128131,6.084926,-4.617268,-2.315503,-1.208180,-1.737379,2.446294,7.145009,4.691604,4.681341,5.088573,-8.657870,-0.944799,-3.428802,1.656354,-5.303611,-7.335046,-4.829562,-9.870284,-7.805057,3.024324,1.807404,9.190431,3.124861,8.627602,-2.814984,-6.052877,5.840677,-8.197869,-1.784709,-6.370909,-1.175702,-6.436698,4.211356,1.069406,-3.391039,-2.881177,0.923107,-6.266171,5.729759,9.027519,-9.745477,-6.458928,-9.232915,2.315951,6.251494,6.706858,8.226923,-2.085620,-1.366362,-3.165388,7.262088,6.481048,-9.537493,0.459102,6.182832,2.334929,-1.020774,-3.434280,7.881821,1.215839,7.584828,-0.244036,4.083281,8.251717,-9.494063,-5.536784,-1.934052,3.080926,3.094101,-6.834259,8.504872,-3.928679,-1.900461,4.244888,0.348428,-2.528384,9.444145,4.583153,4.825282,6.620292,-5.521986,8.047769,2.349309,0.861312,-1.519554,4.269766,-6.523071,8.464286,-4.865025,-8.015016,-9.221593,-4.144540,4.600776,-0.274461,-8.040744,-4.780956,8.795469,-2.394393,-2.572377,3.192168,7.286339,5.622089,-1.343122,-3.571300,6.815491,-0.468909,2.687538,8.661369,-3.069258,-3.795443,7.612316,9.203186,-8.887507,8.695787,-2.448430,1.194714,-0.516351,6.588162,-8.616742,4.538131,-9.087833,9.518609,5.126249,-0.072643,-9.386921,-1.687190,1.534034,-6.960899,0.352832,0.119699,-0.763843,-0.348405,7.580688,8.877080,1.550775,6.987449,2.672317,-0.631605,8.453810,-1.522522,0.202950,-4.551329,7.320695,-3.525115,-1.518121,-4.439931,1.357697,2.215269,-0.960729,-3.336793,-8.914153,3.593225,-0.248655,-4.646278,-8.720395,8.530228,4.428231,-6.957788,-3.628603,-9.814746,-2.334600,2.674405,5.141383,-6.575328,2.504458,3.060245,-0.821082,6.847612,-5.933459,1.459451,8.341753,-4.649961,-0.337345,1.683380,-6.869737,7.379898,-9.246088,-3.502925,-0.818541,0.351774,4.647462,1.928337,6.452827,-1.601502,-5.885968,-1.033237,-7.926059,-3.248633,8.515979,9.599914,6.243857,6.332880,5.979863,0.432851,-1.139106,9.807022,-2.413527,-2.724457,-8.575379,5.962957,-5.551559,-8.419190,6.016561,5.662055,-5.393541,-3.712419,8.447506,8.068159,0.217068,-3.375645,0.508870,0.183453,-5.907860,8.683705,-2.614928,7.230996,-5.684079,2.972775,8.925082], dtype = "float32")#candidate|1428|(264,)|const|float32
call_1427 = relay.TupleGetItem(func_1046_call(relay.reshape(const_1428.astype('float32'), [12, 11, 2])), 0)
call_1429 = relay.TupleGetItem(func_1048_call(relay.reshape(const_1428.astype('float32'), [12, 11, 2])), 0)
func_1314_call = mod.get_global_var('func_1314')
func_1317_call = mutated_mod.get_global_var('func_1317')
call_1435 = relay.TupleGetItem(func_1314_call(relay.reshape(const_1390.astype('uint8'), [])), 5)
call_1436 = relay.TupleGetItem(func_1317_call(relay.reshape(const_1390.astype('uint8'), [])), 5)
output = relay.Tuple([bop_1392,call_1427,const_1428,call_1435,])
output2 = relay.Tuple([bop_1392,call_1429,const_1428,call_1436,])
func_1453 = relay.Function([var_1391,], output)
mod['func_1453'] = func_1453
mod = relay.transform.InferType()(mod)
var_1454 = relay.var("var_1454", dtype = "float32", shape = (4, 12, 15))#candidate|1454|(4, 12, 15)|var|float32
output = func_1453(var_1454)
func_1455 = relay.Function([var_1454], output)
mutated_mod['func_1455'] = func_1455
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2185 = relay.var("var_2185", dtype = "float64", shape = (10, 1, 8))#candidate|2185|(10, 1, 8)|var|float64
uop_2186 = relay.asinh(var_2185.astype('float64')) # shape=(10, 1, 8)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
const_2194 = relay.const([-2,-5,1,5,10,-7,-10,-9,6,4,4,-4,9,10,-6,-1,8,-1,4,8,-1,-10,-4,5,6,9,-3,-5,-5,-6,-7,-9,3,-7,5,-2,10,9,-5,-3,-4,-3,5,3,-4,-1,8,-10,-10,-9,-10,-3,-4,-6,7,-10,-4,-9,-4,1,1,-10,3,-9,5,-10,-10,-9,5,3,-7,-4,9,-1,6,-10,-5,-8,-10,-1,-7,-2,-4,-1,-6,-5,-9,-3,-2,9,6,9,-10,10,-3,5,-2,7,9,8,-2,8,2,10,-4,4,-8,1,-9,10,-2,4,-3,1,-10,-9,2,6,7,-7,-4,-2,5,2,6,8,6,-1,4,5,3,-8,1,8,-7,10,-8,-6,10,7,-8,2,-8,7,7,7,5,-6,9,-6,-8,10,1,-1,1,-6,4,7,3,5,7,3,-7,-8,-2,3,-3,8,-8,-6,6,2,-10,-1,4,-6,-7,-2,-7,-1,7,8,8,3,-4,8,10,9,8,4,7,-2,-8,-1,9,3,7,-7,7,2,10,1,-10,10,10,10,8,2,-10,-1,6,-4,-5,-9,-10,4,-2,10,5,10,7,-3,-5,1,9,-4,-7,-7,1,5,-8,3,-3,-10,4,4,-3,6,-5,3,10,10,-8,-2,-4,2,7,9,-8,-10,10,-6,4,-1,9,-4,3,-10,2,10,8,-7,-7,9,-7,10,5,-2,-7,8,9,9,-8,3,-1,-8,-6,6,-3,-3,-3,2,10,-5,-9,5,6,1,2,-6,10,-2,10,2,-2,-6,9,-3,3,5,2,1,-5,4,8,-10,5,-5,-9,-10,5,8,-5,-2,-8,10,1,7,-6,3,2,-4,-5,-4,7,9,-10,-7,-5,-3,10,-2,9,-6,2,-10,-3,3,-3,-6,9,-4,10,5,-10,8,-4,-10,-2,7,-6,-10,1,-10,-8,-7,-2,7,-2,-9,3,-4,-10,1,3,-5,6,9,-7,-2,-7,-4,-1,3,5,10,9,-4,-10,-10,4,-1,1,8,1,4,10,-7,1,4,1,-2,8,1,5,-3,7,7,-6,-7,-6,4,-9,5,-2,5,-5,-4,-5,4,-8,-8,1,-4,-2,-5], dtype = "uint64")#candidate|2194|(416,)|const|uint64
call_2193 = relay.TupleGetItem(func_132_call(relay.reshape(const_2194.astype('uint64'), [8, 4, 13]), relay.reshape(const_2194.astype('uint64'), [8, 4, 13]), ), 1)
call_2195 = relay.TupleGetItem(func_136_call(relay.reshape(const_2194.astype('uint64'), [8, 4, 13]), relay.reshape(const_2194.astype('uint64'), [8, 4, 13]), ), 1)
func_132_call = mod.get_global_var('func_132')
func_136_call = mutated_mod.get_global_var('func_136')
call_2199 = relay.TupleGetItem(func_132_call(relay.reshape(const_2194.astype('uint64'), [8, 4, 13]), relay.reshape(call_2193.astype('uint64'), [8, 4, 13]), ), 1)
call_2200 = relay.TupleGetItem(func_136_call(relay.reshape(const_2194.astype('uint64'), [8, 4, 13]), relay.reshape(call_2193.astype('uint64'), [8, 4, 13]), ), 1)
bop_2205 = relay.left_shift(uop_2186.astype('uint64'), relay.reshape(var_2185.astype('uint64'), relay.shape_of(uop_2186))) # shape=(10, 1, 8)
output = relay.Tuple([call_2193,const_2194,call_2199,bop_2205,])
output2 = relay.Tuple([call_2195,const_2194,call_2200,bop_2205,])
func_2220 = relay.Function([var_2185,], output)
mod['func_2220'] = func_2220
mod = relay.transform.InferType()(mod)
mutated_mod['func_2220'] = func_2220
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2221 = relay.var("var_2221", dtype = "float64", shape = (10, 1, 8))#candidate|2221|(10, 1, 8)|var|float64
func_2220_call = mutated_mod.get_global_var('func_2220')
call_2222 = func_2220_call(var_2221)
output = call_2222
func_2223 = relay.Function([var_2221], output)
mutated_mod['func_2223'] = func_2223
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2269 = relay.var("var_2269", dtype = "float64", shape = (15, 12, 2))#candidate|2269|(15, 12, 2)|var|float64
uop_2270 = relay.acos(var_2269.astype('float64')) # shape=(15, 12, 2)
var_2276 = relay.var("var_2276", dtype = "float64", shape = (15, 12, 2))#candidate|2276|(15, 12, 2)|var|float64
bop_2277 = relay.multiply(uop_2270.astype('int64'), relay.reshape(var_2276.astype('int64'), relay.shape_of(uop_2270))) # shape=(15, 12, 2)
output = relay.Tuple([bop_2277,])
output2 = relay.Tuple([bop_2277,])
func_2280 = relay.Function([var_2269,var_2276,], output)
mod['func_2280'] = func_2280
mod = relay.transform.InferType()(mod)
mutated_mod['func_2280'] = func_2280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2280_call = mutated_mod.get_global_var('func_2280')
var_2282 = relay.var("var_2282", dtype = "float64", shape = (15, 12, 2))#candidate|2282|(15, 12, 2)|var|float64
var_2283 = relay.var("var_2283", dtype = "float64", shape = (15, 12, 2))#candidate|2283|(15, 12, 2)|var|float64
call_2281 = func_2280_call(var_2282,var_2283,)
output = call_2281
func_2284 = relay.Function([var_2282,var_2283,], output)
mutated_mod['func_2284'] = func_2284
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2297 = relay.var("var_2297", dtype = "uint32", shape = ())#candidate|2297|()|var|uint32
var_2298 = relay.var("var_2298", dtype = "uint32", shape = (11, 13, 12))#candidate|2298|(11, 13, 12)|var|uint32
bop_2299 = relay.equal(var_2297.astype('bool'), var_2298.astype('bool')) # shape=(11, 13, 12)
output = bop_2299
output2 = bop_2299
func_2302 = relay.Function([var_2297,var_2298,], output)
mod['func_2302'] = func_2302
mod = relay.transform.InferType()(mod)
var_2303 = relay.var("var_2303", dtype = "uint32", shape = ())#candidate|2303|()|var|uint32
var_2304 = relay.var("var_2304", dtype = "uint32", shape = (11, 13, 12))#candidate|2304|(11, 13, 12)|var|uint32
output = func_2302(var_2303,var_2304,)
func_2305 = relay.Function([var_2303,var_2304,], output)
mutated_mod['func_2305'] = func_2305
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2633 = relay.var("var_2633", dtype = "float64", shape = (4, 1, 8))#candidate|2633|(4, 1, 8)|var|float64
uop_2634 = relay.asinh(var_2633.astype('float64')) # shape=(4, 1, 8)
func_1185_call = mod.get_global_var('func_1185')
func_1188_call = mutated_mod.get_global_var('func_1188')
const_2637 = relay.const([-2,2,-2,5,-1,-10,4,9,7,7,-5,-2,-1,4,-6,-10,6,2,-2,-6,7,-2,-6,-7,8,-6,10,-7,-5,-7,-10,9,-1,-7,-10,-4,1,-2,-6,1,-4,9,7,8,-7,-4,4,-6,-6,5,-6,-7,-6,5,7,-8,-2,-8,4,-10,-1,-9,-8,9,10,2,-5,-4,-7,5,-4,8,1,-7,-3,8,-1,-10,-4,5,-5,9,-7,2,-1,-1,-1,2,-6,-9], dtype = "int32")#candidate|2637|(90,)|const|int32
var_2638 = relay.var("var_2638", dtype = "int32", shape = (360, 2))#candidate|2638|(360, 2)|var|int32
call_2636 = relay.TupleGetItem(func_1185_call(relay.reshape(const_2637.astype('int32'), [15, 1, 6]), relay.reshape(var_2638.astype('int32'), [15, 8, 6]), ), 0)
call_2639 = relay.TupleGetItem(func_1188_call(relay.reshape(const_2637.astype('int32'), [15, 1, 6]), relay.reshape(var_2638.astype('int32'), [15, 8, 6]), ), 0)
output = relay.Tuple([uop_2634,call_2636,const_2637,var_2638,])
output2 = relay.Tuple([uop_2634,call_2639,const_2637,var_2638,])
func_2651 = relay.Function([var_2633,var_2638,], output)
mod['func_2651'] = func_2651
mod = relay.transform.InferType()(mod)
mutated_mod['func_2651'] = func_2651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2651_call = mutated_mod.get_global_var('func_2651')
var_2653 = relay.var("var_2653", dtype = "float64", shape = (4, 1, 8))#candidate|2653|(4, 1, 8)|var|float64
var_2654 = relay.var("var_2654", dtype = "int32", shape = (360, 2))#candidate|2654|(360, 2)|var|int32
call_2652 = func_2651_call(var_2653,var_2654,)
output = call_2652
func_2655 = relay.Function([var_2653,var_2654,], output)
mutated_mod['func_2655'] = func_2655
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2756 = relay.const([[[-4.025966],[8.685576],[-7.351122],[-8.636689]],[[-4.329036],[-6.638336],[4.186340],[8.333766]],[[-9.878739],[-2.079189],[2.029049],[-5.649268]],[[7.537759],[0.551727],[-5.461455],[5.356215]],[[-9.538874],[6.530706],[-8.406451],[-9.639599]],[[-7.337820],[2.454080],[-7.336688],[6.847621]],[[-3.289896],[6.029233],[-5.158664],[5.003517]],[[-1.277422],[8.703552],[-5.106974],[9.020123]],[[2.071874],[8.564977],[-8.018601],[-8.358519]],[[-9.075099],[-4.111546],[-8.696157],[-6.846952]],[[1.748086],[9.954151],[2.849356],[-4.138355]],[[7.139607],[6.139220],[-5.699375],[-0.862023]],[[5.004475],[6.023503],[0.517340],[-3.811539]],[[9.119576],[1.391443],[9.215838],[-7.318749]],[[1.551041],[-9.854430],[5.695514],[-6.996057]],[[-9.113897],[-3.548087],[0.168879],[-0.902401]]], dtype = "float64")#candidate|2756|(16, 4, 1)|const|float64
uop_2757 = relay.sin(const_2756.astype('float64')) # shape=(16, 4, 1)
output = uop_2757
output2 = uop_2757
func_2762 = relay.Function([], output)
mod['func_2762'] = func_2762
mod = relay.transform.InferType()(mod)
mutated_mod['func_2762'] = func_2762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mutated_mod.get_global_var('func_2762')
call_2763 = func_2762_call()
output = call_2763
func_2764 = relay.Function([], output)
mutated_mod['func_2764'] = func_2764
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_2765 = func_2762_call()
call_2766 = func_2762_call()
func_1314_call = mod.get_global_var('func_1314')
func_1317_call = mutated_mod.get_global_var('func_1317')
const_2771 = relay.const(-2, dtype = "uint8")#candidate|2771|()|const|uint8
call_2770 = relay.TupleGetItem(func_1314_call(relay.reshape(const_2771.astype('uint8'), [])), 0)
call_2772 = relay.TupleGetItem(func_1317_call(relay.reshape(const_2771.astype('uint8'), [])), 0)
const_2775 = relay.const([[[-6,3,-4,-7,-9,5,10,-7,9],[3,7,1,-6,-4,3,-2,2,-2],[-2,-7,-2,1,2,-8,5,9,5],[8,8,-2,-7,9,-10,6,-2,3],[7,9,5,-2,-9,2,10,-5,4],[-7,-4,10,9,-7,1,6,5,-1],[3,1,-4,-5,-5,-3,10,9,8],[7,7,8,-6,-8,-2,-1,2,-6],[-5,3,3,-8,-7,4,-6,1,-7],[-1,-5,-3,-10,1,-6,-10,-10,-10]],[[8,6,7,-9,5,6,10,4,-8],[2,3,10,2,2,-3,-7,-2,-4],[-4,-4,4,-8,9,2,1,7,-7],[5,7,3,2,8,-2,-5,-5,5],[8,4,7,5,9,-2,-9,8,-4],[5,-3,-2,-5,-1,-7,-10,10,-2],[-9,5,-1,6,3,5,5,5,-4],[2,5,2,10,7,-5,6,-6,-3],[9,-6,-1,2,-2,5,4,-7,-3],[-1,10,-4,6,10,3,8,3,4]],[[4,2,-3,-4,-8,-9,8,7,-7],[5,-3,7,8,-9,9,5,-9,1],[-7,2,4,8,1,-1,6,-4,-3],[-4,6,2,-7,1,7,2,7,-9],[3,-4,-3,-5,-3,8,1,6,7],[3,6,-2,5,7,7,-2,5,7],[1,9,-2,-9,-2,10,-3,-5,-6],[2,-2,3,8,2,-9,3,10,5],[10,-4,-7,2,-7,8,6,5,2],[-7,-3,-6,-7,-4,3,-8,-1,7]],[[-5,7,10,5,9,3,-10,-2,1],[-5,8,-5,7,8,-6,-8,-8,2],[2,1,9,-1,-8,2,-2,10,-4],[-5,-8,1,-7,-6,-3,2,-8,-5],[9,-8,2,8,6,-5,3,-3,10],[7,-2,4,-1,-9,9,10,1,-9],[-7,-6,-5,5,-1,-8,-2,-2,-8],[-8,-3,2,10,-2,-9,5,-7,10],[1,9,2,5,-2,8,3,1,-2],[10,4,-4,-4,-8,9,-3,1,-4]],[[-9,9,-8,-3,5,-9,-8,1,-2],[4,6,-6,-8,-7,1,4,-2,3],[-9,3,2,-1,10,4,-8,7,-8],[9,2,-5,-9,2,1,3,2,4],[-9,-6,-6,10,-7,-8,-10,3,4],[4,6,-7,1,-8,8,-7,-6,6],[1,8,5,-5,4,6,5,-1,7],[-9,-8,1,9,-10,3,7,-4,-4],[-10,3,-8,-1,-10,-5,8,5,-2],[-1,8,-6,-7,-5,-9,-9,1,-4]],[[-10,1,7,9,3,-3,-2,-8,6],[-1,8,-6,-6,-7,-7,-5,7,-9],[5,4,-1,3,-3,-4,-4,4,3],[-10,-2,-8,-1,8,-1,4,6,-2],[-7,2,7,-9,-1,2,2,4,10],[-5,-5,8,-1,-1,-2,-7,9,9],[5,6,2,1,1,-7,7,3,4],[-7,-6,5,-1,-7,10,-6,-7,-5],[2,10,-1,-8,9,-10,3,-10,-4],[-6,-5,-7,10,-4,-8,5,-2,7]],[[2,-2,5,1,-9,-6,6,-10,-5],[-10,10,2,-10,10,-2,7,-2,-2],[-3,6,6,5,-4,-6,9,3,-9],[-9,-2,5,8,5,-3,1,-1,-7],[9,-10,-6,1,4,9,9,-4,-7],[-4,-1,6,-5,9,4,-5,-2,7],[3,7,1,9,-2,-10,10,-5,-10],[-4,-10,3,2,8,-2,2,-2,-3],[5,-3,-4,7,5,-6,6,2,-4],[-1,-2,10,5,-1,3,2,-5,4]],[[-5,7,4,7,-3,6,-3,-6,8],[-2,10,-2,7,-2,8,-6,-6,3],[6,7,-8,-9,-10,7,-10,2,2],[6,9,-6,3,-10,-4,-10,4,2],[-2,4,-7,-1,9,1,-9,-3,-3],[3,-10,7,-7,-6,4,-2,2,-8],[6,6,-3,7,3,8,6,4,-6],[1,5,4,-9,6,2,-10,3,6],[-4,10,10,3,-1,5,5,-1,-7],[-2,3,8,1,-6,6,2,2,7]],[[-10,-1,7,-10,-3,-5,-6,-7,-6],[-4,4,3,1,-10,-9,-8,-9,-2],[4,1,1,-6,-4,5,7,-6,1],[-1,-7,7,9,-5,-4,-5,8,-6],[1,-7,-6,-4,4,-3,1,9,-6],[4,-4,6,-5,-8,6,-2,-9,-3],[-3,-7,-8,4,-8,-7,-3,-10,9],[5,-6,7,-1,2,-9,-5,1,-1],[-6,-10,10,-7,-8,8,-4,3,9],[3,-2,10,-9,4,-6,-10,-10,5]],[[8,10,10,5,-4,5,10,-1,-2],[-2,5,2,10,6,-4,9,4,8],[-9,9,1,5,1,-2,9,3,-1],[-7,-8,-1,3,-4,9,-2,-7,10],[-4,-9,-4,-7,8,-9,4,-10,-9],[5,-2,1,-1,8,4,5,-6,3],[7,3,10,4,7,8,-8,-8,-10],[-10,1,-8,-9,-5,7,-2,-7,-2],[6,3,-4,7,-6,2,5,-8,1],[1,8,2,-3,-2,9,9,1,-7]],[[5,-7,-1,8,1,2,1,-10,1],[-6,6,7,3,-1,8,-1,3,5],[-7,10,6,-9,-7,-7,3,-3,1],[-6,-5,-9,8,7,10,-7,-2,6],[-1,6,6,-6,-7,1,8,2,-8],[-6,3,-10,-5,9,-6,-7,9,-6],[-9,7,-3,3,8,7,-8,-2,8],[3,9,-1,6,5,-3,4,5,-9],[-10,2,-10,3,3,1,7,5,8],[4,-1,-1,10,-8,7,-3,-10,4]],[[-5,-9,4,2,-6,9,10,-1,-10],[7,10,-3,1,-5,-3,10,-7,8],[1,-3,6,4,-5,7,7,-5,9],[5,6,-2,10,6,-3,9,4,-4],[5,-4,-2,4,-7,8,7,-8,3],[1,-4,-1,1,2,3,6,1,-8],[3,2,-3,9,-6,-4,-7,-2,-1],[-9,-4,-10,4,-7,-5,9,7,1],[-4,9,-7,8,-7,6,-3,10,5],[-6,-5,-5,-8,-2,6,4,-4,-9]]], dtype = "uint8")#candidate|2775|(12, 10, 9)|const|uint8
bop_2776 = relay.bitwise_or(call_2770.astype('uint32'), relay.reshape(const_2775.astype('uint32'), relay.shape_of(call_2770))) # shape=(12, 10, 9)
bop_2779 = relay.bitwise_or(call_2772.astype('uint32'), relay.reshape(const_2775.astype('uint32'), relay.shape_of(call_2772))) # shape=(12, 10, 9)
output = relay.Tuple([call_2765,const_2771,bop_2776,])
output2 = relay.Tuple([call_2766,const_2771,bop_2779,])
func_2786 = relay.Function([], output)
mod['func_2786'] = func_2786
mod = relay.transform.InferType()(mod)
mutated_mod['func_2786'] = func_2786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2786_call = mutated_mod.get_global_var('func_2786')
call_2787 = func_2786_call()
output = call_2787
func_2788 = relay.Function([], output)
mutated_mod['func_2788'] = func_2788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_2803 = func_2762_call()
call_2804 = func_2762_call()
func_1001_call = mod.get_global_var('func_1001')
func_1004_call = mutated_mod.get_global_var('func_1004')
const_2815 = relay.const([8.891954,7.023247,6.271645,-5.429601,3.863280,4.793970,2.657377,-7.121377,3.834205,-2.521965,6.358597,8.250989,5.983884,9.521214,3.833914,5.739649,-2.602924,6.122557,1.255057,4.670479,-6.163311,-3.452830,-0.100267,0.798660,-0.695428,-5.137017,3.039957,8.193861,9.357315,1.707012,2.027485,-9.261761,1.534180,-3.103715,3.595997,0.943567,-4.317971,-4.789542,-3.852379,-5.264313,8.894523,9.313491,3.506690,5.296070,3.094265,1.626485,-9.983945,2.730768,-3.296704,-7.802505,1.340223,7.690243,6.878878,-8.144873,5.342901,-2.182177,-3.501117,1.511047,6.716343,-5.503071,5.679352,6.575738,0.168357,2.029036,-2.179787,-4.918571,4.884446,6.785918,0.180614,-3.995965,5.063680,9.927118,-3.609013,9.680490,9.670760,1.607502,4.404117,-7.866020,5.041658,-7.157052,8.679851,1.048721,-7.160962,-7.922119,3.490784,-5.401440,6.674028,-6.138866,-4.139269,6.856306,1.158467,-4.378599,-4.926435,-3.351791,-8.964971,2.560039,8.811621,-7.392297,-5.139218,3.220770,-3.438501,-6.951603,4.723963,6.993376,-5.642765,5.420551,3.957319,-5.110122,1.673476,4.936049,-8.073652,9.332450,-2.811020,5.982868,-7.986311,-2.233494,6.208342,4.091428,3.538724,-9.396215,8.431315,9.414673,-6.188788,-0.107654,-4.413653,6.728284,6.038974,-3.889435,0.365848,-7.222986,-2.833578,-2.893067,5.819419,-8.048114,-5.674425,-9.844927,1.189183,9.379461,3.479493,5.645662,7.293644,-0.942512,6.093645,-0.975374,6.436146,8.779637,6.242152,8.104921,9.081512,5.045201,-6.414803,2.268308,-4.357001,4.565873,3.303357,7.147060,-9.237648,0.977417,0.313037,-5.391918,-2.177159,-8.973311,4.464496,-3.443268,-5.939861,-7.684541,8.358952,-2.524947], dtype = "float64")#candidate|2815|(168,)|const|float64
var_2816 = relay.var("var_2816", dtype = "bool", shape = (819,))#candidate|2816|(819,)|var|bool
call_2814 = relay.TupleGetItem(func_1001_call(relay.reshape(const_2815.astype('float64'), [7, 12, 2]), relay.reshape(var_2816.astype('bool'), [819,]), ), 0)
call_2817 = relay.TupleGetItem(func_1004_call(relay.reshape(const_2815.astype('float64'), [7, 12, 2]), relay.reshape(var_2816.astype('bool'), [819,]), ), 0)
bop_2833 = relay.less_equal(const_2815.astype('bool'), call_2803.astype('bool')) # shape=(16, 4, 168)
bop_2836 = relay.less_equal(const_2815.astype('bool'), call_2804.astype('bool')) # shape=(16, 4, 168)
func_2651_call = mod.get_global_var('func_2651')
func_2655_call = mutated_mod.get_global_var('func_2655')
var_2839 = relay.var("var_2839", dtype = "float64", shape = (16, 2))#candidate|2839|(16, 2)|var|float64
var_2840 = relay.var("var_2840", dtype = "int32", shape = (720,))#candidate|2840|(720,)|var|int32
call_2838 = relay.TupleGetItem(func_2651_call(relay.reshape(var_2839.astype('float64'), [4, 1, 8]), relay.reshape(var_2840.astype('int32'), [360, 2]), ), 3)
call_2841 = relay.TupleGetItem(func_2655_call(relay.reshape(var_2839.astype('float64'), [4, 1, 8]), relay.reshape(var_2840.astype('int32'), [360, 2]), ), 3)
var_2843 = relay.var("var_2843", dtype = "int32", shape = (360, 2))#candidate|2843|(360, 2)|var|int32
bop_2844 = relay.minimum(call_2838.astype('float64'), relay.reshape(var_2843.astype('float64'), relay.shape_of(call_2838))) # shape=(360, 2)
bop_2847 = relay.minimum(call_2841.astype('float64'), relay.reshape(var_2843.astype('float64'), relay.shape_of(call_2841))) # shape=(360, 2)
bop_2854 = relay.bitwise_xor(const_2815.astype('uint32'), call_2803.astype('uint32')) # shape=(16, 4, 168)
bop_2857 = relay.bitwise_xor(const_2815.astype('uint32'), call_2804.astype('uint32')) # shape=(16, 4, 168)
bop_2861 = relay.right_shift(bop_2854.astype('int8'), relay.reshape(bop_2833.astype('int8'), relay.shape_of(bop_2854))) # shape=(16, 4, 168)
bop_2864 = relay.right_shift(bop_2857.astype('int8'), relay.reshape(bop_2836.astype('int8'), relay.shape_of(bop_2857))) # shape=(16, 4, 168)
output = relay.Tuple([call_2814,var_2816,var_2839,var_2840,bop_2844,bop_2861,])
output2 = relay.Tuple([call_2817,var_2816,var_2839,var_2840,bop_2847,bop_2864,])
func_2870 = relay.Function([var_2816,var_2839,var_2840,var_2843,], output)
mod['func_2870'] = func_2870
mod = relay.transform.InferType()(mod)
mutated_mod['func_2870'] = func_2870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2870_call = mutated_mod.get_global_var('func_2870')
var_2872 = relay.var("var_2872", dtype = "bool", shape = (819,))#candidate|2872|(819,)|var|bool
var_2873 = relay.var("var_2873", dtype = "float64", shape = (16, 2))#candidate|2873|(16, 2)|var|float64
var_2874 = relay.var("var_2874", dtype = "int32", shape = (720,))#candidate|2874|(720,)|var|int32
var_2875 = relay.var("var_2875", dtype = "int32", shape = (360, 2))#candidate|2875|(360, 2)|var|int32
call_2871 = func_2870_call(var_2872,var_2873,var_2874,var_2875,)
output = call_2871
func_2876 = relay.Function([var_2872,var_2873,var_2874,var_2875,], output)
mutated_mod['func_2876'] = func_2876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_2884 = func_2762_call()
call_2885 = func_2762_call()
output = call_2884
output2 = call_2885
func_2889 = relay.Function([], output)
mod['func_2889'] = func_2889
mod = relay.transform.InferType()(mod)
mutated_mod['func_2889'] = func_2889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2889_call = mutated_mod.get_global_var('func_2889')
call_2890 = func_2889_call()
output = call_2890
func_2891 = relay.Function([], output)
mutated_mod['func_2891'] = func_2891
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2930 = relay.var("var_2930", dtype = "uint64", shape = (3, 1, 13))#candidate|2930|(3, 1, 13)|var|uint64
const_2931 = relay.const([[[8,7,-1,8,10,9,5,2,-5,9,-6,1,9],[10,4,-4,-2,-6,-1,-3,10,-10,9,2,-9,-1],[1,10,2,6,2,10,-4,-6,-3,-3,10,7,5],[5,-10,10,-8,3,-10,10,2,3,8,-10,10,-3],[-1,10,-2,2,3,5,-2,-5,-1,4,5,-1,9],[-4,-7,9,-7,-3,-6,-3,7,-2,10,1,2,-5],[3,2,9,10,4,3,-8,2,-3,5,-5,-9,4],[-4,-3,7,-7,7,6,-2,-7,-4,5,-9,1,6],[-10,-8,-5,3,3,6,-9,-8,2,-5,-8,2,-3],[10,6,9,-3,10,-1,-5,-1,6,4,4,5,3],[-8,-7,-9,-6,-4,-8,-4,-2,9,1,8,9,3],[-8,-3,-4,-7,4,7,-10,5,-8,6,3,-9,5],[-2,-9,-10,-5,-9,5,-9,1,-9,5,-9,-2,-2],[8,1,-9,2,8,-7,8,-2,-2,-2,-7,4,-4]],[[6,5,2,1,1,-6,10,-6,9,-2,6,3,7],[-8,1,-5,7,7,5,3,-8,8,3,6,9,4],[-4,-3,7,3,1,-7,7,-8,-1,-8,-9,10,4],[3,-4,9,6,-10,-3,-2,-10,-3,-2,9,3,6],[-6,2,-10,1,4,3,-2,-2,5,-9,3,-10,-4],[-10,-6,9,-3,-2,-7,-9,3,-2,7,9,-8,-7],[-2,-5,7,3,4,-7,-2,9,2,-2,-2,-1,8],[2,-10,-4,7,-7,7,-2,-4,7,8,7,4,6],[-4,6,8,-6,7,9,3,2,9,-10,-3,-1,3],[-2,9,-2,6,5,-5,2,-4,8,8,7,4,-2],[-4,-5,-3,3,-4,5,4,3,2,1,-8,-1,-9],[-6,6,7,3,9,10,5,9,-5,9,-10,3,7],[10,-10,8,1,3,6,-1,-9,-6,-6,-6,6,9],[8,-9,3,-5,-8,8,7,-7,-9,-5,-1,5,-6]],[[6,-8,-9,-7,1,10,5,-7,7,-6,6,-7,6],[-1,-3,3,10,2,-8,-10,9,3,7,-8,-5,-3],[2,9,5,-10,-9,-6,6,10,7,3,9,-1,-7],[1,3,-10,-3,2,10,-4,9,-10,8,-1,10,-2],[-9,5,9,-5,-1,7,5,-10,5,6,4,1,5],[-8,7,4,-10,-1,7,3,-4,-2,2,-3,-5,-1],[4,2,5,4,9,-9,7,10,-7,-9,-3,-9,2],[2,-3,-10,-4,-6,-4,2,-8,-2,2,-6,7,1],[8,-5,-1,10,7,-1,-4,-3,-7,2,7,-8,-8],[-7,2,4,-5,10,3,2,-2,4,-1,-4,3,4],[10,6,-6,2,8,-8,3,3,-10,8,7,7,9],[6,7,-2,2,4,1,-8,2,-4,-3,-2,3,4],[4,-9,3,4,5,-7,-4,-5,-9,-5,-6,-9,-7],[4,3,-9,-9,9,-2,-2,-1,-4,-1,1,9,-2]]], dtype = "uint64")#candidate|2931|(3, 14, 13)|const|uint64
bop_2932 = relay.logical_xor(var_2930.astype('uint64'), const_2931.astype('uint64')) # shape=(3, 14, 13)
var_2948 = relay.var("var_2948", dtype = "uint64", shape = (3, 2, 13))#candidate|2948|(3, 2, 13)|var|uint64
bop_2949 = relay.add(var_2930.astype('uint16'), var_2948.astype('uint16')) # shape=(3, 2, 13)
func_421_call = mod.get_global_var('func_421')
func_425_call = mutated_mod.get_global_var('func_425')
var_2953 = relay.var("var_2953", dtype = "bool", shape = (819,))#candidate|2953|(819,)|var|bool
var_2954 = relay.var("var_2954", dtype = "uint64", shape = (8, 52))#candidate|2954|(8, 52)|var|uint64
call_2952 = relay.TupleGetItem(func_421_call(relay.reshape(var_2953.astype('bool'), [9, 7, 13]), relay.reshape(var_2954.astype('uint64'), [416,]), ), 6)
call_2955 = relay.TupleGetItem(func_425_call(relay.reshape(var_2953.astype('bool'), [9, 7, 13]), relay.reshape(var_2954.astype('uint64'), [416,]), ), 6)
output = relay.Tuple([bop_2932,bop_2949,call_2952,var_2953,var_2954,])
output2 = relay.Tuple([bop_2932,bop_2949,call_2955,var_2953,var_2954,])
func_2961 = relay.Function([var_2930,var_2948,var_2953,var_2954,], output)
mod['func_2961'] = func_2961
mod = relay.transform.InferType()(mod)
mutated_mod['func_2961'] = func_2961
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2961_call = mutated_mod.get_global_var('func_2961')
var_2963 = relay.var("var_2963", dtype = "uint64", shape = (3, 1, 13))#candidate|2963|(3, 1, 13)|var|uint64
var_2964 = relay.var("var_2964", dtype = "uint64", shape = (3, 2, 13))#candidate|2964|(3, 2, 13)|var|uint64
var_2965 = relay.var("var_2965", dtype = "bool", shape = (819,))#candidate|2965|(819,)|var|bool
var_2966 = relay.var("var_2966", dtype = "uint64", shape = (8, 52))#candidate|2966|(8, 52)|var|uint64
call_2962 = func_2961_call(var_2963,var_2964,var_2965,var_2966,)
output = call_2962
func_2967 = relay.Function([var_2963,var_2964,var_2965,var_2966,], output)
mutated_mod['func_2967'] = func_2967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_2999 = func_2762_call()
call_3000 = func_2762_call()
output = relay.Tuple([call_2999,])
output2 = relay.Tuple([call_3000,])
func_3009 = relay.Function([], output)
mod['func_3009'] = func_3009
mod = relay.transform.InferType()(mod)
output = func_3009()
func_3010 = relay.Function([], output)
mutated_mod['func_3010'] = func_3010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2889_call = mod.get_global_var('func_2889')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_3025 = func_2889_call()
call_3026 = func_2889_call()
func_3009_call = mod.get_global_var('func_3009')
func_3010_call = mutated_mod.get_global_var('func_3010')
call_3029 = relay.TupleGetItem(func_3009_call(), 0)
call_3030 = relay.TupleGetItem(func_3010_call(), 0)
func_2870_call = mod.get_global_var('func_2870')
func_2876_call = mutated_mod.get_global_var('func_2876')
const_3035 = relay.const([False,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,False,True,False,False,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,True,False,False,False,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,False,False,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False], dtype = "bool")#candidate|3035|(819,)|const|bool
const_3036 = relay.const([-7.050217,2.163172,5.045547,6.941988,-1.960512,-6.961635,6.551944,-8.040911,-2.760261,0.281775,2.979552,0.169686,7.977481,-8.394748,-4.111471,-0.626237,-1.293215,1.458974,6.131676,8.436521,-2.274853,-6.442418,2.097334,-0.501606,-3.419789,-4.179646,-3.671527,6.344722,-0.583721,-1.017342,7.212693,9.335638], dtype = "float64")#candidate|3036|(32,)|const|float64
const_3037 = relay.const([-5,3,-7,-7,9,-9,-5,3,-5,3,-7,-4,6,4,-7,3,7,2,-9,4,5,10,-4,-3,5,5,-5,-3,-3,6,5,2,7,7,2,-5,7,-10,10,2,-7,7,7,3,-8,-8,10,6,3,-3,-7,6,8,6,7,-5,-4,8,-2,-1,-10,1,10,-7,-1,10,1,-1,-9,-8,3,-3,-4,10,4,6,10,-5,-7,3,-3,5,6,4,10,-4,-3,-4,7,-3,-3,6,6,-4,-2,-10,-8,2,10,-9,-5,-7,-9,-7,3,9,9,-1,-5,-10,10,5,-5,-3,-10,-7,-7,-5,-3,3,2,-2,-7,8,8,10,-5,7,9,-7,2,6,-6,6,-3,5,-2,8,2,1,1,-7,6,8,-3,8,7,-7,-7,2,1,-7,8,2,9,-9,7,-7,-1,-10,-10,-2,-2,-1,1,1,5,-6,-1,-1,2,-3,6,-3,6,3,-2,4,3,5,1,5,1,-6,-10,7,7,-2,-9,-1,-8,1,-9,-4,-10,-6,4,-4,-5,-9,7,8,5,10,4,-7,8,-2,2,-1,6,1,1,7,6,-2,2,-1,-9,-9,6,7,5,-3,9,7,-1,5,4,9,-8,6,-10,-6,-2,4,-4,-2,-10,4,-8,5,1,-3,-4,6,-3,3,-3,-2,6,3,-7,-9,-9,-6,-5,-6,3,-1,4,-10,-4,-10,-1,-2,-8,-7,9,2,10,-4,-1,9,-2,10,2,2,-2,-2,5,-2,-10,-8,6,6,-9,8,3,-1,-10,10,4,7,-4,-1,-5,-4,1,-4,3,10,10,-10,-7,-7,-6,10,-7,-6,-6,-2,7,5,-9,4,7,-3,-3,-2,-8,7,4,-5,-6,3,-7,2,10,-3,-6,-10,2,2,10,4,-10,1,-10,-4,7,-8,-2,-8,10,9,10,-1,-5,-6,6,3,2,-2,2,9,-5,4,1,-8,-5,9,10,-8,2,10,-3,-3,-8,-9,3,10,7,3,-7,-9,2,8,7,-9,-9,6,-1,-8,6,-1,-5,4,6,10,-2,6,8,-6,-1,3,-3,3,-9,-4,10,3,8,-7,-7,-8,9,-3,-9,1,5,3,4,3,-8,-10,4,-4,-1,7,-10,-6,-8,-6,-9,8,-5,-3,6,4,-5,-2,6,-1,9,-6,2,7,-3,6,2,-8,-6,7,7,8,4,10,8,-10,3,5,7,5,7,-4,9,7,4,-9,-5,-2,-9,-2,8,-3,5,-6,9,4,7,6,-1,1,-7,8,-7,3,-5,-2,-5,5,2,4,-5,9,8,7,-10,-7,-7,1,5,8,8,-4,5,-5,-3,2,7,1,9,-7,4,-8,-8,5,-4,3,4,-7,1,10,2,3,3,7,9,3,-7,-4,-3,-8,1,10,-3,6,10,-7,6,-2,-1,3,2,-3,10,-3,4,1,-5,3,-10,1,3,-4,7,9,6,7,-1,-6,8,5,3,9,9,-7,1,10,-5,4,-10,-9,5,4,-8,7,4,-2,-10,-8,-3,7,-2,-9,-1,10,-3,10,8,-6,-8,4,6,10,7,2,-2,5,8,-2,6,-2,2,-9,-8,7,-1,-8,7,3,-6,5,6,2,5,-2,-6,9,8,6,-6,-4,4,-4,-1,-4,-3,-5,-10,-4,-8,3,3,-2,4,7,-3,-5,-2,-9,-5,10,-3,-9,-1,-5,9,5,-3,-3,6,-5,8,7,8,-4,8,-10,-8,-3,2,-10,-7,-3,1,-5,5,-8,-1,-6,9,-1,4,10,-2,3,-3,5,7,10,5,8,9,-6,9,9,-9,-8,2,7,3,8,-4,-7,4,-10,7,2,4,-4,7,2,4,1,10,-1,-7,-8,-5,-1,-4,-9,-10,5,-6,-6,4,9,2,7,-7,4,9,-4,-8,-3,-9,-1], dtype = "int32")#candidate|3037|(720,)|const|int32
call_3034 = relay.TupleGetItem(func_2870_call(relay.reshape(const_3035.astype('bool'), [819,]), relay.reshape(const_3036.astype('float64'), [16, 2]), relay.reshape(const_3037.astype('int32'), [720,]), relay.reshape(const_3037.astype('int32'), [360, 2]), ), 3)
call_3038 = relay.TupleGetItem(func_2876_call(relay.reshape(const_3035.astype('bool'), [819,]), relay.reshape(const_3036.astype('float64'), [16, 2]), relay.reshape(const_3037.astype('int32'), [720,]), relay.reshape(const_3037.astype('int32'), [360, 2]), ), 3)
uop_3058 = relay.cos(const_3035.astype('float64')) # shape=(819,)
output = relay.Tuple([call_3025,call_3029,call_3034,const_3036,const_3037,uop_3058,])
output2 = relay.Tuple([call_3026,call_3030,call_3038,const_3036,const_3037,uop_3058,])
func_3063 = relay.Function([], output)
mod['func_3063'] = func_3063
mod = relay.transform.InferType()(mod)
mutated_mod['func_3063'] = func_3063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3063_call = mutated_mod.get_global_var('func_3063')
call_3064 = func_3063_call()
output = call_3064
func_3065 = relay.Function([], output)
mutated_mod['func_3065'] = func_3065
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2889_call = mod.get_global_var('func_2889')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_3066 = func_2889_call()
call_3067 = func_2889_call()
func_1453_call = mod.get_global_var('func_1453')
func_1455_call = mutated_mod.get_global_var('func_1455')
var_3083 = relay.var("var_3083", dtype = "float32", shape = (4, 180))#candidate|3083|(4, 180)|var|float32
call_3082 = relay.TupleGetItem(func_1453_call(relay.reshape(var_3083.astype('float32'), [4, 12, 15])), 2)
call_3084 = relay.TupleGetItem(func_1455_call(relay.reshape(var_3083.astype('float32'), [4, 12, 15])), 2)
func_2870_call = mod.get_global_var('func_2870')
func_2876_call = mutated_mod.get_global_var('func_2876')
var_3088 = relay.var("var_3088", dtype = "bool", shape = (819,))#candidate|3088|(819,)|var|bool
const_3089 = relay.const([0.178683,-0.109896,-5.973517,3.562052,-7.739568,5.122237,7.667060,-9.288269,-7.633816,-2.774768,-9.116623,4.741808,-3.943082,-7.982403,5.363802,1.410563,6.395625,-2.428747,9.910733,1.926616,-8.410443,-9.126181,5.102446,-3.046536,5.891811,-7.483423,4.305037,-9.817679,-4.600306,1.005648,-8.244588,-2.412361], dtype = "float64")#candidate|3089|(32,)|const|float64
call_3087 = relay.TupleGetItem(func_2870_call(relay.reshape(var_3088.astype('bool'), [819,]), relay.reshape(const_3089.astype('float64'), [16, 2]), relay.reshape(var_3083.astype('int32'), [720,]), relay.reshape(var_3083.astype('int32'), [360, 2]), ), 3)
call_3090 = relay.TupleGetItem(func_2876_call(relay.reshape(var_3088.astype('bool'), [819,]), relay.reshape(const_3089.astype('float64'), [16, 2]), relay.reshape(var_3083.astype('int32'), [720,]), relay.reshape(var_3083.astype('int32'), [360, 2]), ), 3)
bop_3101 = relay.logical_xor(var_3083.astype('uint64'), relay.reshape(call_3087.astype('uint64'), relay.shape_of(var_3083))) # shape=(4, 180)
bop_3104 = relay.logical_xor(var_3083.astype('uint64'), relay.reshape(call_3090.astype('uint64'), relay.shape_of(var_3083))) # shape=(4, 180)
output = relay.Tuple([call_3066,call_3082,var_3088,const_3089,bop_3101,])
output2 = relay.Tuple([call_3067,call_3084,var_3088,const_3089,bop_3104,])
func_3124 = relay.Function([var_3083,var_3088,], output)
mod['func_3124'] = func_3124
mod = relay.transform.InferType()(mod)
var_3125 = relay.var("var_3125", dtype = "float32", shape = (4, 180))#candidate|3125|(4, 180)|var|float32
var_3126 = relay.var("var_3126", dtype = "bool", shape = (819,))#candidate|3126|(819,)|var|bool
output = func_3124(var_3125,var_3126,)
func_3127 = relay.Function([var_3125,var_3126,], output)
mutated_mod['func_3127'] = func_3127
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3161 = relay.const([[[4,7,-9,-9,5,1,-8,8,5,7,-6,10,8,-6,7,-4],[8,-6,6,-1,5,2,3,7,2,9,-6,9,5,7,-5,-4],[-2,2,-8,-10,9,8,-2,9,10,1,9,2,-7,-7,-9,7],[-3,-1,6,-6,3,-4,-1,-10,-2,-7,-3,6,-7,4,6,-9],[-2,10,4,-10,1,4,8,-1,7,3,6,-1,4,2,9,-7],[-2,9,-4,-2,5,-7,2,-5,-7,-10,-2,9,-6,-4,-10,6],[-9,-9,5,9,9,-5,7,1,-2,8,-2,8,6,3,-4,-10],[-3,9,2,8,-6,-4,4,-7,-8,10,2,8,-1,-7,-9,7]],[[8,3,-4,1,5,4,-3,-8,8,9,-6,-9,9,10,-3,-3],[5,-10,7,10,9,1,-7,-10,-7,-4,-7,7,-10,-5,6,-5],[2,-1,-9,10,6,-9,-2,-7,-2,-9,-5,7,3,-10,10,1],[1,10,4,-9,3,3,-10,2,3,-1,8,-6,1,-10,-9,10],[3,-9,2,-7,-7,8,-1,9,10,4,9,-8,4,-9,1,5],[1,-2,4,-6,10,-8,4,6,-7,-3,10,7,1,9,5,-5],[9,-9,-7,-4,1,-7,-9,-1,3,3,3,-7,5,-6,9,-9],[9,1,-5,2,-9,2,-3,-6,-5,8,-8,4,-3,4,-2,-10]],[[10,-8,10,-2,-8,-9,-7,7,-2,2,2,-3,-6,8,-7,10],[2,4,-7,-3,1,8,-4,2,2,8,-9,10,8,-3,6,4],[-9,-2,-3,3,-4,5,-6,8,10,1,-8,5,6,-1,-1,-2],[1,1,8,1,-3,-4,1,6,-7,-1,5,-1,7,-5,6,1],[1,3,-5,5,-1,8,10,-5,8,-2,-5,-6,-4,1,8,9],[-5,3,7,8,7,-1,-10,4,4,3,-8,10,-9,3,-2,-9],[5,6,9,3,10,1,-2,-9,10,6,10,1,8,7,6,-8],[9,6,-8,2,-1,-9,7,-9,-10,4,-10,1,10,-9,-5,1]],[[9,-2,4,-6,-6,-10,-4,9,-4,6,-9,-4,-5,9,-10,-6],[8,5,-1,-9,-7,-9,7,-5,-2,-9,-7,1,-7,-6,3,-5],[9,2,-2,-6,-1,-10,-2,1,7,4,-6,10,7,10,7,10],[-7,7,-5,-10,5,-5,6,-10,8,1,-8,9,8,-5,7,2],[-8,-5,9,9,3,2,10,4,-5,-3,-5,-8,2,-7,-9,-4],[7,1,-3,1,-2,7,4,-9,-6,2,5,-6,3,7,-2,10],[10,-7,-2,1,1,6,-1,6,9,1,-8,-2,-10,-5,-2,4],[-6,5,9,-2,3,-8,2,4,-4,5,3,4,-8,8,4,2]],[[-2,10,2,-2,7,-1,-5,-2,3,-2,-7,-2,5,-7,-3,-3],[-7,-6,4,-5,-7,-1,3,-1,1,5,-10,-6,-8,-6,-1,5],[1,-6,9,-7,10,-9,1,1,5,-1,2,2,10,10,8,-1],[7,5,1,-2,-9,-3,-5,4,2,-5,-3,-4,-6,8,10,-2],[-7,2,-10,-8,-7,9,9,2,-9,4,5,-8,-2,4,6,-8],[-6,10,7,4,2,8,9,1,-8,-1,-4,-5,-5,-10,-6,3],[-1,7,-4,-1,-4,-6,-8,10,-3,-10,-2,-3,5,-8,-2,-2],[-6,10,-8,6,2,5,-10,-8,8,10,-5,8,8,1,-9,-4]],[[10,6,-7,-1,4,-8,3,-9,-6,-2,6,10,-8,-6,4,5],[-6,-5,3,9,-4,-4,-3,-9,-4,9,-2,3,-2,10,-1,-1],[6,-7,1,-8,4,-3,5,-7,4,-8,-9,-10,-2,-8,-3,-7],[4,-10,3,-2,-10,-6,-9,-5,-3,1,3,-2,2,-5,8,6],[9,8,1,-1,-7,5,1,10,2,7,-5,-10,8,1,-1,-7],[2,2,-9,4,9,-3,1,8,7,1,-2,-8,-10,6,6,2],[3,1,9,10,-7,10,-8,-1,2,8,7,-6,-5,-6,10,-8],[4,-6,5,10,-9,-9,-9,-4,4,-8,-6,-8,9,-1,-4,3]],[[-10,-2,5,6,4,-2,6,7,8,3,-10,-6,-4,1,9,7],[-4,-2,-3,-4,-4,2,-4,1,4,7,-4,-6,-3,-8,10,-10],[6,-3,2,8,4,5,-10,-10,-2,-2,-4,-7,-5,9,-2,-2],[-1,-9,-2,9,8,-6,2,-5,-4,5,5,-7,8,-10,3,1],[6,-8,-9,-8,1,-5,9,1,9,3,7,6,6,-6,-7,4],[6,-6,1,2,-6,-6,9,2,1,-1,7,-4,5,-1,-6,10],[9,9,-7,-3,-7,2,6,1,-9,-8,4,-7,-1,-5,-5,8],[-10,5,7,-2,7,-10,6,-4,6,1,-1,10,7,8,-10,-10]],[[-5,-8,5,7,-6,6,-10,8,10,7,8,-5,5,-10,10,-7],[-5,9,7,-1,-3,-6,7,9,5,-3,5,9,1,-7,7,8],[-9,1,3,2,1,8,-3,-7,5,1,-8,-10,-10,-2,2,-1],[6,-8,6,-4,-9,-4,1,3,3,-6,6,2,4,3,5,-7],[-7,-2,9,7,10,2,-5,5,-9,-1,-8,3,6,-8,-1,1],[-3,9,9,-8,9,10,5,4,-8,-2,-7,-8,10,-5,2,7],[9,5,-1,-8,-5,6,6,7,-6,-10,-2,7,4,-3,10,-2],[-5,8,10,-8,-6,6,-6,-6,1,-5,-4,-7,6,7,-1,4]],[[3,-3,10,1,-10,8,1,-8,1,9,8,8,-7,8,3,5],[-6,1,2,3,-1,7,6,6,1,-5,-1,-10,7,6,4,5],[10,7,10,-5,3,-2,-9,8,-4,-8,-5,3,8,1,-3,-1],[4,8,-10,-6,-6,3,7,-5,4,5,-2,3,-2,-2,-3,-9],[-5,-3,-9,-9,5,2,3,4,3,-9,2,6,8,-10,-3,8],[-7,2,-7,-2,-10,8,-2,-3,4,9,-5,9,-3,6,7,3],[-6,1,-5,-8,7,-10,-10,5,6,9,9,7,-8,-1,7,-10],[-10,-8,2,-1,4,10,-4,-6,-9,4,-5,-3,3,8,7,-5]],[[-7,-1,9,-9,-5,6,2,-2,9,10,-6,-4,4,-1,10,-9],[10,-5,3,-3,1,-8,3,5,-5,-3,5,-1,1,-1,9,7],[9,10,6,-10,5,3,9,10,-10,-4,2,3,9,-4,3,10],[5,-5,5,9,7,-10,7,-10,-2,-1,2,-10,9,9,-7,-5],[-1,3,-8,-6,6,1,5,-2,6,1,-9,-8,7,10,6,-6],[6,3,-6,8,4,-5,1,-5,-1,2,9,8,-7,10,4,2],[-9,-5,-3,-5,4,-7,-7,9,-1,10,3,6,6,7,3,-1],[4,7,1,-6,2,-10,-8,-9,-2,-8,6,-6,1,-4,1,-7]],[[3,2,-6,1,-4,10,-7,-10,7,3,4,-6,3,9,5,-10],[-2,4,-3,-9,-3,-10,6,-1,-9,-6,6,-8,-2,-4,5,-5],[8,-6,-2,9,-1,-8,-8,2,5,-10,10,1,-5,8,1,-6],[3,-2,-6,-2,10,4,9,7,3,-7,7,4,-5,1,-8,-6],[8,7,9,-1,-9,6,2,-6,-3,8,10,-2,-6,2,-2,4],[4,-6,-1,1,3,-10,3,9,-8,7,-1,-5,-4,1,-3,7],[-6,-10,7,9,-9,4,6,7,10,-1,3,-2,-1,4,-9,1],[2,-4,-3,1,-1,-3,8,-10,3,1,-7,6,5,-4,-9,-10]],[[8,-1,7,4,-7,-5,-6,3,-8,9,9,-7,-3,1,-8,4],[6,-9,-9,1,10,1,4,-7,-10,10,-10,-4,-8,7,-7,-1],[10,6,-3,-5,4,10,10,10,4,7,-5,-8,-7,8,-10,7],[-1,9,-9,-8,10,10,-7,-8,-8,-8,-10,-7,-3,-1,6,-3],[8,-2,8,-9,-9,-8,9,1,3,-2,6,-9,8,4,-7,-2],[2,-3,5,-9,-3,5,3,9,5,-10,-5,-2,1,9,-6,5],[7,8,-4,-8,-2,-6,9,2,9,5,-2,-6,-4,3,6,-7],[7,-6,-2,5,7,8,9,10,-1,1,-1,-6,-2,4,-6,10]],[[6,-6,10,2,-5,3,-2,1,7,7,-6,4,4,7,-1,-5],[3,-7,3,2,10,1,10,5,3,-7,9,-9,9,2,3,7],[9,2,-3,-1,10,5,5,9,-6,-8,-8,-5,-3,7,6,-5],[-7,-6,-9,-5,10,-1,2,2,-6,2,-7,3,3,7,5,4],[-7,4,9,9,1,-4,-1,2,5,3,10,2,-7,5,-1,6],[1,-5,9,-10,5,-5,10,-4,-9,7,-5,5,7,4,6,5],[-9,-8,6,9,1,8,1,-6,-8,-10,-1,-5,-2,6,8,-7],[-6,5,4,3,-10,-7,-10,-1,-6,-3,5,-5,10,9,5,-7]],[[1,-2,8,10,-6,-8,10,7,2,2,2,6,-1,2,-3,8],[10,10,-7,7,7,-10,-7,-4,-10,6,-6,-6,9,6,4,7],[5,-6,-6,-6,10,-4,6,6,6,8,6,2,9,-9,-1,-10],[2,1,-9,-4,4,6,8,5,-3,8,6,-7,6,-9,4,7],[5,5,4,3,-9,-9,-10,-9,-7,2,-6,8,7,-3,9,9],[6,2,-5,-2,-5,-1,5,-5,8,-4,8,-8,-1,8,-9,-8],[2,8,6,-4,-1,3,7,-6,7,1,6,-4,2,-9,-10,-7],[8,4,5,2,-4,-2,4,10,-2,1,-2,-4,-9,-5,-1,-3]],[[-10,-2,6,-3,-10,-5,-6,8,-6,3,3,4,2,1,2,4],[-3,-8,-10,-1,-7,5,-1,-1,-3,7,-4,8,-8,1,6,-3],[2,10,-4,2,-7,-7,1,7,4,10,3,-6,-8,5,2,5],[-1,6,7,-9,5,5,3,2,6,-5,-9,-3,8,4,-8,-4],[5,-4,-7,9,10,10,5,-1,3,9,-1,-10,10,10,3,7],[-3,-10,-6,4,2,1,5,8,10,-9,-2,1,-5,10,-5,5],[9,-10,-4,-3,8,4,6,1,-1,-8,-1,5,-9,5,-3,4],[8,9,8,-10,3,-10,-8,-6,3,-2,-2,2,3,5,-8,7]]], dtype = "int32")#candidate|3161|(15, 8, 16)|const|int32
const_3162 = relay.const([[[7,4,9,10,10,-2,-5,6,3,-1,3,2,-7,8,-6,3],[-2,-1,-7,-5,-3,1,7,7,9,10,9,-1,-2,-8,-1,4],[-9,4,-8,-5,8,-8,-5,-5,-3,4,7,-10,6,9,-8,1],[-6,5,8,4,8,-8,-6,-5,10,-1,-9,-7,-1,-2,-7,-8],[10,8,1,-1,-5,2,-6,8,-8,-2,-2,-10,5,-1,5,-9],[1,4,-1,-3,-5,-6,3,6,5,-8,9,1,10,-8,3,1],[-5,8,-9,10,7,7,-4,-1,3,7,7,-7,1,-3,1,8],[8,-1,8,-3,9,-7,6,-1,7,-2,7,-3,-3,1,-10,-9]],[[7,-9,1,-2,-3,3,-8,8,-6,2,-10,-10,-1,6,-1,4],[-4,5,-5,6,-7,-7,7,2,8,5,-9,10,9,3,-10,10],[-10,-7,-1,2,6,-6,-9,-6,-2,-4,9,3,7,-10,5,-10],[4,-9,-4,4,4,-3,-8,-7,-2,-3,4,-9,-4,-7,6,3],[7,-6,4,-1,1,9,-2,2,-7,3,3,-2,10,3,9,7],[-7,-8,-4,-9,-10,-4,5,6,-3,5,2,2,-9,7,10,-5],[-6,9,-2,5,-7,4,-9,3,-9,7,-6,-3,-3,-4,-4,-3],[3,-2,-10,-7,-8,-8,1,-8,-2,4,-5,2,9,2,-8,-6]],[[6,-6,-7,-5,5,-1,-7,-9,-5,6,1,-7,-5,-4,5,-3],[-9,9,-3,-10,-10,-7,3,3,-10,-7,6,-9,-6,-5,4,2],[-9,9,7,-2,-2,1,4,5,-4,5,8,-2,-9,-5,-5,6],[8,-7,5,-2,-10,-4,1,-10,-2,5,-9,6,4,-10,-8,2],[-2,-3,-10,-7,9,9,-1,-5,2,-6,-8,10,4,8,8,8],[-1,-8,7,5,7,6,-3,-2,10,7,-10,8,8,-6,10,-8],[-8,-5,-4,-8,4,-10,4,1,1,2,6,-5,-7,-5,-8,9],[-1,-8,-7,-5,-2,-8,-8,10,9,-1,1,-1,9,-9,-9,3]],[[-5,5,9,2,7,-8,9,4,-10,-4,1,3,-3,6,-1,4],[-2,-7,-10,-6,9,2,4,9,-9,6,10,7,-2,-7,-4,2],[-9,10,-9,4,10,7,10,-7,9,-8,-3,-2,9,-1,-8,10],[-1,7,-7,-8,-9,-1,3,9,-1,10,-1,2,-2,5,-5,9],[7,8,9,3,2,-6,-1,-8,-1,8,-3,-3,3,-6,5,6],[1,8,-9,7,-4,-8,-7,9,5,9,-8,-2,10,-1,3,-7],[-1,-6,7,-2,10,9,-8,-5,-6,2,9,-6,2,-4,-5,3],[9,6,5,-8,-10,2,5,-3,-6,-8,-9,-3,-4,-7,-1,4]],[[-2,-5,-10,1,2,-8,-5,-10,5,5,2,4,7,4,-6,8],[-9,-4,-10,9,-10,-10,9,5,10,6,8,-10,5,-4,4,-6],[9,-4,-5,-10,1,2,-2,1,-7,-5,-1,1,-9,-7,-9,6],[5,6,2,-6,9,-10,-5,2,2,-6,-10,-10,-3,2,4,-9],[-5,-10,4,9,-6,-2,-3,-2,2,7,6,-3,-6,1,2,-8],[9,-5,6,4,-4,-2,5,-2,-3,-2,-8,-7,1,-4,-2,-1],[10,3,3,-5,-6,-6,2,-9,-10,-3,-6,-3,-2,10,-9,4],[1,5,-5,-1,-9,1,6,8,10,4,-4,3,-6,-10,5,4]],[[9,10,-2,-4,-9,-2,-6,-8,-2,2,-9,-3,-9,-2,5,2],[7,-8,4,-10,9,-5,4,1,8,-3,-10,4,9,8,1,-10],[2,7,-9,7,3,-1,7,-5,7,2,6,1,-9,1,-6,8],[6,6,-6,-1,6,6,-6,-6,8,-4,-3,2,-3,4,2,9],[-1,5,-7,4,10,7,-8,-3,-3,5,-4,-10,9,-6,7,-1],[2,4,2,-3,8,2,-4,-6,-4,5,-7,-4,-8,-7,8,5],[-2,1,9,-8,-3,4,-7,-6,-1,-6,-5,-5,1,-10,-8,10],[4,-5,5,-1,-6,-8,5,-4,3,7,10,-1,-1,-3,7,-10]],[[3,5,3,-8,9,1,-8,-4,-5,-8,-10,10,-3,-4,-6,-1],[-2,-7,-2,-3,1,-7,-9,1,-2,2,10,-5,5,-3,-6,10],[-3,-2,-3,6,-10,-2,-5,-6,-2,9,10,-6,5,-6,8,-8],[2,-5,-6,-9,-5,-5,6,5,10,1,-2,-5,-8,8,6,6],[8,4,-4,10,8,10,-9,-1,1,-8,-10,-9,-3,-6,-5,-8],[-6,6,-7,-9,-4,-8,-6,-1,-2,-9,10,-3,-5,2,3,-4],[2,1,8,6,-1,-4,-5,3,4,10,-9,6,3,-5,-10,7],[1,-3,8,-3,-4,-5,4,4,7,9,-8,10,-5,-10,-6,-6]],[[5,-5,9,-3,7,-9,3,6,-1,5,-3,3,-2,2,-9,4],[-8,-8,-9,9,8,-6,5,-2,8,-6,-6,1,-3,7,-1,-8],[10,-7,9,-4,6,-8,1,-7,-1,1,3,5,-5,8,3,-7],[1,3,-2,7,-6,-8,6,7,-10,5,2,-7,-2,5,10,10],[9,-1,2,-8,-4,-7,-4,8,-5,-7,-2,-6,-9,10,6,-3],[3,6,2,4,-2,6,5,10,-8,-9,-1,-3,-7,-2,-2,7],[-8,1,-7,-6,5,-7,-8,2,-5,-6,-7,9,-1,8,7,-9],[10,-5,-4,-8,-4,9,3,10,4,6,-7,7,7,3,5,-9]],[[1,-4,4,6,-8,-2,8,-8,-9,4,-9,-6,-10,-10,-1,8],[2,1,-3,-6,1,1,-1,2,5,-8,8,-3,-2,-3,-2,7],[4,-2,2,-9,7,2,3,9,-9,2,-10,-8,-8,5,4,7],[-9,-7,6,-6,8,-10,2,-8,-6,-2,7,-9,3,-8,6,-6],[-2,-6,1,-3,9,-1,-3,-4,1,-7,8,-3,10,9,-7,-10],[10,-9,-9,-9,6,-1,-8,9,-3,-8,-4,1,4,-9,4,10],[-9,-4,-1,-9,2,-7,-7,10,3,-10,-10,-1,2,5,-1,-2],[6,-9,9,-6,-9,3,-9,7,-2,-9,1,-9,9,-1,-1,-1]],[[8,-5,-1,8,-4,-8,-6,5,2,-2,-1,6,-7,2,-9,-6],[-6,-4,4,7,-4,2,-7,-2,10,-4,7,3,-8,-3,-10,3],[-1,-1,10,-6,-10,-8,5,8,4,-6,-5,-6,-6,9,9,9],[3,-7,-7,-9,1,-6,7,-2,7,3,-9,-4,-9,8,-6,-10],[-7,2,-1,-3,-10,9,-2,-10,10,-10,6,1,-8,5,-6,-3],[-3,-8,-7,9,9,-7,-10,9,-4,-9,2,6,-9,-4,-8,-1],[-3,7,2,-9,5,-2,-7,-7,10,9,-5,4,8,2,-6,-8],[4,10,1,-8,7,5,1,-5,7,-4,1,-10,-5,-4,5,-9]],[[7,-6,-1,7,4,-4,-6,-9,2,-9,3,-1,-10,-9,-7,6],[10,-2,-8,-8,3,-1,-10,-3,-6,-3,-10,7,-9,8,9,-10],[8,7,-3,10,9,-4,-4,9,-9,-6,9,2,-4,-6,6,1],[5,2,4,-3,-5,-2,-6,-8,-5,8,10,4,10,-6,-3,2],[4,8,-10,-1,-10,6,3,-2,8,4,8,3,-7,8,-5,-10],[6,9,8,3,-2,-3,2,-7,5,-8,9,-5,-10,8,3,6],[-7,5,4,5,-6,-5,6,-9,-1,-4,-8,-9,-1,-8,5,2],[-9,-7,-5,-3,1,-9,7,-7,-5,-3,1,-5,-8,-5,-7,7]],[[5,10,-6,-3,10,5,-10,-10,-5,-9,-4,9,7,7,2,-3],[7,7,8,-2,1,-8,2,-5,-10,5,1,5,7,-4,-5,-6],[-2,-6,2,-7,-7,-4,-2,6,-5,5,3,6,4,-1,-8,-3],[-9,-9,9,3,-2,3,-6,-7,7,9,-3,-4,-6,8,-1,4],[-10,-2,-10,4,-4,7,5,-2,-7,-4,7,-7,-4,-7,-6,8],[4,8,5,-8,-9,10,1,8,-3,6,2,-3,10,3,10,5],[-9,10,3,4,2,-7,6,-9,-8,10,-10,-6,4,-6,9,8],[2,-6,5,8,6,10,-9,-2,4,6,-5,-4,-4,-3,10,4]],[[9,-9,-2,2,4,-9,-3,-1,2,-10,-2,6,-5,-10,10,8],[-2,6,6,1,3,5,10,10,-3,-9,-7,10,3,6,4,7],[-3,-1,2,-2,-1,-9,-1,2,-3,1,-5,-1,-1,-4,-3,2],[-3,-8,4,-9,7,7,-1,3,10,-4,-5,5,-4,-2,9,4],[4,6,3,4,-7,7,-1,-2,2,-8,-10,4,2,-2,7,-3],[-9,-2,8,2,8,3,-8,10,10,-9,-1,-6,-7,3,6,9],[-7,-8,7,-2,9,-4,-10,-9,10,-5,-8,-3,-1,1,4,-3],[-2,-8,2,4,5,8,-2,-8,-4,-3,-5,-1,3,-4,-3,8]],[[9,-4,5,-2,-8,6,1,2,6,-10,-10,-9,-3,7,-1,1],[10,1,-5,-6,7,-3,-7,-4,8,5,-4,-10,7,-5,6,-8],[-3,-4,6,-1,3,9,-1,-4,-4,-9,-3,-7,8,-1,-8,-1],[-2,9,-6,-8,6,-8,8,-6,-10,3,5,4,-2,8,-5,-10],[7,-2,-2,1,-8,7,-10,10,-9,3,-5,-7,-3,-8,7,5],[9,-4,-10,1,5,-5,2,-3,8,-2,3,1,-6,6,1,7],[1,-3,8,10,-3,-6,-10,-5,-7,5,-6,-7,7,6,-7,8],[-6,-10,6,-6,6,-1,3,9,2,-1,10,5,-3,5,-5,7]],[[-5,-4,8,-7,3,3,5,7,5,10,-6,-5,5,9,5,9],[-5,-1,2,9,10,-1,-5,-4,6,8,-8,-3,2,-1,9,1],[5,-9,1,-2,2,-8,6,9,-8,6,-9,7,2,-2,-9,5],[4,1,-3,-8,10,4,-10,8,2,-3,4,4,-9,-6,-9,2],[-6,1,-10,6,7,-6,5,-4,-9,-9,7,6,2,-6,-5,-6],[-3,-2,-6,-3,-10,-1,-4,-3,-3,3,-8,8,2,-2,-2,2],[7,-8,-4,-7,1,-1,-2,5,7,-5,-8,-6,7,-9,-8,6],[-9,-8,7,-9,-3,1,-5,1,6,-8,1,5,3,8,-7,7]]], dtype = "int32")#candidate|3162|(15, 8, 16)|const|int32
bop_3163 = relay.maximum(const_3161.astype('int32'), relay.reshape(const_3162.astype('int32'), relay.shape_of(const_3161))) # shape=(15, 8, 16)
func_2651_call = mod.get_global_var('func_2651')
func_2655_call = mutated_mod.get_global_var('func_2655')
var_3167 = relay.var("var_3167", dtype = "float64", shape = (32,))#candidate|3167|(32,)|var|float64
var_3168 = relay.var("var_3168", dtype = "int32", shape = (720,))#candidate|3168|(720,)|var|int32
call_3166 = relay.TupleGetItem(func_2651_call(relay.reshape(var_3167.astype('float64'), [4, 1, 8]), relay.reshape(var_3168.astype('int32'), [360, 2]), ), 2)
call_3169 = relay.TupleGetItem(func_2655_call(relay.reshape(var_3167.astype('float64'), [4, 1, 8]), relay.reshape(var_3168.astype('int32'), [360, 2]), ), 2)
uop_3179 = relay.acosh(const_3161.astype('float64')) # shape=(15, 8, 16)
output = relay.Tuple([bop_3163,call_3166,var_3167,var_3168,uop_3179,])
output2 = relay.Tuple([bop_3163,call_3169,var_3167,var_3168,uop_3179,])
func_3181 = relay.Function([var_3167,var_3168,], output)
mod['func_3181'] = func_3181
mod = relay.transform.InferType()(mod)
var_3182 = relay.var("var_3182", dtype = "float64", shape = (32,))#candidate|3182|(32,)|var|float64
var_3183 = relay.var("var_3183", dtype = "int32", shape = (720,))#candidate|3183|(720,)|var|int32
output = func_3181(var_3182,var_3183,)
func_3184 = relay.Function([var_3182,var_3183,], output)
mutated_mod['func_3184'] = func_3184
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3192 = relay.const([[[2,10,1,2,-10,1,2,6],[-7,-6,8,5,9,-7,-2,-2],[1,4,-10,3,3,-9,-9,8],[3,-4,-3,1,7,-9,-2,-3]],[[3,-6,-8,-4,2,-7,-8,6],[1,4,-3,6,-2,-10,7,9],[3,-4,-6,-3,2,9,6,-1],[7,1,-10,-9,5,1,3,4]],[[7,8,-4,10,-2,8,-4,7],[6,-1,-8,-1,10,-4,1,-8],[4,10,8,6,10,-9,2,-6],[-3,-5,7,-1,9,9,-3,-8]],[[4,5,-9,1,-6,2,6,6],[-6,8,10,-10,7,9,-8,-7],[5,2,4,1,-6,7,2,-9],[8,-4,1,7,5,9,1,6]],[[7,-7,-3,-2,5,1,5,-8],[1,1,-7,-1,-4,-8,6,10],[1,-4,-10,-5,8,-2,8,-5],[-1,-3,7,-3,-4,-6,2,-2]],[[7,-9,-4,10,2,4,10,-1],[8,-1,7,7,-2,10,1,1],[1,5,-6,-9,6,10,-5,-9],[4,9,4,3,-3,2,-6,-3]],[[4,-4,2,-1,-7,6,-4,6],[-5,-1,2,-6,6,8,2,-1],[-9,7,8,-10,10,6,1,4],[-8,-8,9,-7,2,9,9,10]],[[-4,-9,-6,-7,7,10,5,7],[-9,6,-8,4,-8,-6,4,-5],[5,-1,5,7,1,-1,5,4],[2,3,2,-10,2,-9,1,7]],[[2,-9,7,-8,-5,-9,-6,6],[2,7,-9,-8,2,9,3,-1],[5,-1,-6,-3,9,-3,4,4],[9,3,8,-8,9,6,-5,-9]],[[7,-3,1,7,-9,-5,-10,-10],[-10,-6,2,-7,-1,-5,9,7],[3,10,7,4,-8,8,7,8],[8,-6,-7,-3,5,7,1,-2]]], dtype = "int8")#candidate|3192|(10, 4, 8)|const|int8
var_3193 = relay.var("var_3193", dtype = "int8", shape = (10, 4, 8))#candidate|3193|(10, 4, 8)|var|int8
bop_3194 = relay.bitwise_and(const_3192.astype('int8'), relay.reshape(var_3193.astype('int8'), relay.shape_of(const_3192))) # shape=(10, 4, 8)
bop_3197 = relay.less_equal(var_3193.astype('bool'), relay.reshape(bop_3194.astype('bool'), relay.shape_of(var_3193))) # shape=(10, 4, 8)
bop_3201 = relay.bitwise_or(var_3193.astype('int8'), relay.reshape(bop_3194.astype('int8'), relay.shape_of(var_3193))) # shape=(10, 4, 8)
uop_3207 = relay.erf(var_3193.astype('float64')) # shape=(10, 4, 8)
bop_3217 = relay.right_shift(bop_3201.astype('int8'), relay.reshape(uop_3207.astype('int8'), relay.shape_of(bop_3201))) # shape=(10, 4, 8)
bop_3221 = relay.equal(bop_3201.astype('bool'), relay.reshape(bop_3217.astype('bool'), relay.shape_of(bop_3201))) # shape=(10, 4, 8)
var_3231 = relay.var("var_3231", dtype = "int8", shape = (10, 4, 8))#candidate|3231|(10, 4, 8)|var|int8
bop_3232 = relay.logical_xor(bop_3217.astype('int16'), relay.reshape(var_3231.astype('int16'), relay.shape_of(bop_3217))) # shape=(10, 4, 8)
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
var_3238 = relay.var("var_3238", dtype = "float32", shape = (147,))#candidate|3238|(147,)|var|float32
call_3237 = relay.TupleGetItem(func_963_call(relay.reshape(var_3238.astype('float32'), [7, 7, 3])), 0)
call_3239 = relay.TupleGetItem(func_965_call(relay.reshape(var_3238.astype('float32'), [7, 7, 3])), 0)
output = relay.Tuple([bop_3197,bop_3221,bop_3232,call_3237,var_3238,])
output2 = relay.Tuple([bop_3197,bop_3221,bop_3232,call_3239,var_3238,])
func_3240 = relay.Function([var_3193,var_3231,var_3238,], output)
mod['func_3240'] = func_3240
mod = relay.transform.InferType()(mod)
var_3241 = relay.var("var_3241", dtype = "int8", shape = (10, 4, 8))#candidate|3241|(10, 4, 8)|var|int8
var_3242 = relay.var("var_3242", dtype = "int8", shape = (10, 4, 8))#candidate|3242|(10, 4, 8)|var|int8
var_3243 = relay.var("var_3243", dtype = "float32", shape = (147,))#candidate|3243|(147,)|var|float32
output = func_3240(var_3241,var_3242,var_3243,)
func_3244 = relay.Function([var_3241,var_3242,var_3243,], output)
mutated_mod['func_3244'] = func_3244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3009_call = mod.get_global_var('func_3009')
func_3010_call = mutated_mod.get_global_var('func_3010')
call_3246 = relay.TupleGetItem(func_3009_call(), 0)
call_3247 = relay.TupleGetItem(func_3010_call(), 0)
var_3290 = relay.var("var_3290", dtype = "float64", shape = (16, 4, 10))#candidate|3290|(16, 4, 10)|var|float64
bop_3291 = relay.equal(call_3246.astype('bool'), var_3290.astype('bool')) # shape=(16, 4, 10)
bop_3294 = relay.equal(call_3247.astype('bool'), var_3290.astype('bool')) # shape=(16, 4, 10)
func_1185_call = mod.get_global_var('func_1185')
func_1188_call = mutated_mod.get_global_var('func_1188')
const_3298 = relay.const([[-6,7],[-8,-7],[-2,3],[8,5],[7,8],[2,-5],[4,10],[5,-6],[-10,6],[4,7],[2,9],[3,3],[8,1],[-7,-10],[2,-9],[-5,5],[9,-5],[5,-8],[-3,1],[1,-7],[-7,2],[3,-7],[10,-1],[10,-2],[7,4],[1,-1],[9,2],[7,-10],[8,-8],[-3,-7],[8,10],[3,-9],[-9,-4],[-4,-7],[-6,2],[8,8],[3,-8],[-1,-1],[-10,9],[5,6],[2,6],[-5,-7],[-2,6],[1,6],[10,-4]], dtype = "int32")#candidate|3298|(45, 2)|const|int32
const_3299 = relay.const([-1,8,-4,9,-7,-8,-5,6,5,2,-7,-5,-1,-9,5,-10,-8,-8,3,10,8,-5,-2,8,-8,-9,5,10,-9,9,-8,2,-1,-8,-8,6,-6,-3,-9,-8,-1,-4,10,-2,-4,5,-4,-9,7,-9,6,3,4,4,8,2,8,-8,1,-9,3,-8,1,1,-7,-5,6,8,-5,-5,2,-2,5,-1,10,-1,6,-9,1,8,-2,2,10,-10,-2,-10,4,7,4,6,-1,-8,-10,-5,8,-8,6,-10,10,3,-7,-8,-7,-2,4,6,7,-2,2,8,1,-2,-6,3,-10,-9,1,8,4,-8,10,-4,9,-3,-5,3,-7,-3,5,10,-4,4,8,-1,4,3,-5,-2,-4,5,8,-7,3,7,-6,5,7,5,-3,-10,-8,-2,9,-9,-9,-4,4,-1,1,-5,6,-7,7,-10,8,7,2,-1,3,6,4,-8,-1,-5,6,1,8,-5,-10,7,-5,-6,-6,-6,8,-1,-1,-3,8,7,8,6,-6,2,5,5,-8,7,-1,2,-6,-2,-4,1,2,5,-8,3,3,-9,7,-10,-9,8,9,-7,-5,-4,-3,10,-5,-3,-8,-6,-6,-1,10,-7,-8,9,6,-2,9,9,-1,7,-4,8,1,-4,8,9,7,-9,2,2,-7,9,10,-8,-7,-8,7,4,9,-4,-3,5,10,5,-3,2,-1,6,10,-2,-8,7,-6,7,9,2,-6,-2,-2,-2,3,-7,-6,-4,4,3,-8,-1,-1,2,10,4,3,-4,-2,-4,-10,-9,-1,-5,1,-8,8,3,-8,1,-1,5,2,2,8,1,4,-6,-3,1,7,-10,1,-6,10,-8,-4,-6,-4,2,-4,-2,3,5,-9,9,-6,-2,-4,-7,-8,7,7,10,-4,5,-7,6,7,5,8,3,-3,-2,-5,-5,-3,7,-8,3,-3,-9,7,10,9,-9,1,2,7,3,2,-5,10,4,2,9,-8,-6,4,-1,1,-9,-2,-8,-4,8,-9,-8,8,-9,1,-8,6,6,-9,-2,-6,5,-1,-4,-4,-8,9,3,10,-10,10,8,1,6,10,10,-1,4,8,7,-2,4,-3,-1,-9,-1,-6,-4,4,6,-8,-4,3,-10,-5,2,4,-1,5,9,2,4,1,-6,8,1,-10,6,2,-4,-5,-6,-6,-7,10,6,5,1,-6,1,1,-1,-6,2,-2,-6,-5,-9,1,10,9,-5,-6,10,-5,5,4,7,-2,7,5,3,8,-9,-8,-4,6,3,8,-3,6,-1,3,-10,6,9,3,-1,5,-1,2,-10,-5,-10,8,-9,3,-3,-9,1,10,-9,3,-3,-2,1,-10,-2,-6,1,8,-8,-2,-7,-4,6,-8,7,5,-10,-6,10,-6,2,-9,-7,3,-9,-6,3,3,-4,-6,-2,2,-7,5,-6,-4,-2,-1,9,4,-6,4,-10,3,-10,4,-8,-6,-7,-4,1,-1,-10,-3,6,-9,-8,4,-2,4,3,-5,-6,-8,1,8,-2,4,1,3,5,-10,6,4,10,-9,-6,6,5,-9,-9,-8,-3,-5,2,-2,1,-1,-7,-5,3,-1,-10,2,-2,2,7,-4,-6,7,-10,-4,-2,-6,-2,-7,4,-5,-5,-10,10,-2,-5,7,7,9,6,8,10,8,-6,-8,-3,5,-10,6,-8,-6,7,4,9,3,7,-3,5,1,-6,-2,-2,6,-3,-1,-1,3,10,3,-3,7,6,-6,-3,4,8,8,-4,-9,9,9,-6,-9,2,-10,-6,4,6,5,-9,-9,-7,-6,-3,10,-6,3,3,-10,2,9,-4,-2,-3,10,-7,10,7,-7,-10,4,7,-7,9,-3,-9,1,-5,6,9,3,-8,-10,-8,7,5,5,-1,10,2,-1,8,-6,4,-5,9,-6,1,-4,-4,-9,4], dtype = "int32")#candidate|3299|(720,)|const|int32
call_3297 = relay.TupleGetItem(func_1185_call(relay.reshape(const_3298.astype('int32'), [15, 1, 6]), relay.reshape(const_3299.astype('int32'), [15, 8, 6]), ), 0)
call_3300 = relay.TupleGetItem(func_1188_call(relay.reshape(const_3298.astype('int32'), [15, 1, 6]), relay.reshape(const_3299.astype('int32'), [15, 8, 6]), ), 0)
var_3311 = relay.var("var_3311", dtype = "int32", shape = (45, 2))#candidate|3311|(45, 2)|var|int32
bop_3312 = relay.right_shift(const_3298.astype('uint64'), relay.reshape(var_3311.astype('uint64'), relay.shape_of(const_3298))) # shape=(45, 2)
bop_3315 = relay.minimum(bop_3312.astype('int16'), relay.reshape(var_3311.astype('int16'), relay.shape_of(bop_3312))) # shape=(45, 2)
func_3124_call = mod.get_global_var('func_3124')
func_3127_call = mutated_mod.get_global_var('func_3127')
const_3326 = relay.const([False,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,False,False,True,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,True,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,True,False,False,False,True,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,False,True,False,False,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,False,True], dtype = "bool")#candidate|3326|(819,)|const|bool
call_3325 = relay.TupleGetItem(func_3124_call(relay.reshape(const_3299.astype('float32'), [4, 180]), relay.reshape(const_3326.astype('bool'), [819,]), ), 2)
call_3327 = relay.TupleGetItem(func_3127_call(relay.reshape(const_3299.astype('float32'), [4, 180]), relay.reshape(const_3326.astype('bool'), [819,]), ), 2)
output = relay.Tuple([bop_3291,call_3297,const_3299,bop_3315,call_3325,const_3326,])
output2 = relay.Tuple([bop_3294,call_3300,const_3299,bop_3315,call_3327,const_3326,])
func_3355 = relay.Function([var_3290,var_3311,], output)
mod['func_3355'] = func_3355
mod = relay.transform.InferType()(mod)
mutated_mod['func_3355'] = func_3355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3355_call = mutated_mod.get_global_var('func_3355')
var_3357 = relay.var("var_3357", dtype = "float64", shape = (16, 4, 10))#candidate|3357|(16, 4, 10)|var|float64
var_3358 = relay.var("var_3358", dtype = "int32", shape = (45, 2))#candidate|3358|(45, 2)|var|int32
call_3356 = func_3355_call(var_3357,var_3358,)
output = call_3356
func_3359 = relay.Function([var_3357,var_3358,], output)
mutated_mod['func_3359'] = func_3359
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3393 = relay.var("var_3393", dtype = "float64", shape = (6, 2, 4))#candidate|3393|(6, 2, 4)|var|float64
uop_3394 = relay.rsqrt(var_3393.astype('float64')) # shape=(6, 2, 4)
uop_3400 = relay.log(var_3393.astype('float32')) # shape=(6, 2, 4)
output = relay.Tuple([uop_3394,uop_3400,])
output2 = relay.Tuple([uop_3394,uop_3400,])
func_3403 = relay.Function([var_3393,], output)
mod['func_3403'] = func_3403
mod = relay.transform.InferType()(mod)
mutated_mod['func_3403'] = func_3403
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3404 = relay.var("var_3404", dtype = "float64", shape = (6, 2, 4))#candidate|3404|(6, 2, 4)|var|float64
func_3403_call = mutated_mod.get_global_var('func_3403')
call_3405 = func_3403_call(var_3404)
output = call_3405
func_3406 = relay.Function([var_3404], output)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2786_call = mod.get_global_var('func_2786')
func_2788_call = mutated_mod.get_global_var('func_2788')
call_3463 = relay.TupleGetItem(func_2786_call(), 2)
call_3464 = relay.TupleGetItem(func_2788_call(), 2)
output = call_3463
output2 = call_3464
func_3467 = relay.Function([], output)
mod['func_3467'] = func_3467
mod = relay.transform.InferType()(mod)
output = func_3467()
func_3468 = relay.Function([], output)
mutated_mod['func_3468'] = func_3468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_3565 = func_2762_call()
call_3566 = func_2762_call()
func_80_call = mod.get_global_var('func_80')
func_83_call = mutated_mod.get_global_var('func_83')
var_3574 = relay.var("var_3574", dtype = "float64", shape = (330,))#candidate|3574|(330,)|var|float64
call_3573 = relay.TupleGetItem(func_80_call(relay.reshape(var_3574.astype('float64'), [5, 6, 11])), 0)
call_3575 = relay.TupleGetItem(func_83_call(relay.reshape(var_3574.astype('float64'), [5, 6, 11])), 0)
uop_3584 = relay.atanh(var_3574.astype('float64')) # shape=(330,)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_3591 = func_2762_call()
call_3592 = func_2762_call()
func_1453_call = mod.get_global_var('func_1453')
func_1455_call = mutated_mod.get_global_var('func_1455')
var_3612 = relay.var("var_3612", dtype = "float32", shape = (720,))#candidate|3612|(720,)|var|float32
call_3611 = relay.TupleGetItem(func_1453_call(relay.reshape(var_3612.astype('float32'), [4, 12, 15])), 1)
call_3613 = relay.TupleGetItem(func_1455_call(relay.reshape(var_3612.astype('float32'), [4, 12, 15])), 1)
output = relay.Tuple([call_3565,call_3573,uop_3584,call_3591,call_3611,var_3612,])
output2 = relay.Tuple([call_3566,call_3575,uop_3584,call_3592,call_3613,var_3612,])
func_3625 = relay.Function([var_3574,var_3612,], output)
mod['func_3625'] = func_3625
mod = relay.transform.InferType()(mod)
mutated_mod['func_3625'] = func_3625
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3625_call = mutated_mod.get_global_var('func_3625')
var_3627 = relay.var("var_3627", dtype = "float64", shape = (330,))#candidate|3627|(330,)|var|float64
var_3628 = relay.var("var_3628", dtype = "float32", shape = (720,))#candidate|3628|(720,)|var|float32
call_3626 = func_3625_call(var_3627,var_3628,)
output = call_3626
func_3629 = relay.Function([var_3627,var_3628,], output)
mutated_mod['func_3629'] = func_3629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3467_call = mod.get_global_var('func_3467')
func_3468_call = mutated_mod.get_global_var('func_3468')
call_3634 = func_3467_call()
call_3635 = func_3467_call()
output = call_3634
output2 = call_3635
func_3637 = relay.Function([], output)
mod['func_3637'] = func_3637
mod = relay.transform.InferType()(mod)
mutated_mod['func_3637'] = func_3637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3637_call = mutated_mod.get_global_var('func_3637')
call_3638 = func_3637_call()
output = call_3638
func_3639 = relay.Function([], output)
mutated_mod['func_3639'] = func_3639
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3657 = relay.var("var_3657", dtype = "float64", shape = (15, 10, 13))#candidate|3657|(15, 10, 13)|var|float64
const_3658 = relay.const([[[9.898319,-1.239337,-4.536166,-6.443047,5.524633,-2.776402,-1.267930,-4.793635,-9.983437,-8.655910,1.163930,-4.361992,-1.725607],[7.368204,3.021595,-3.718633,-4.318117,3.151734,-6.013443,-6.119308,3.598894,6.418598,6.252820,-1.664544,-4.269819,-8.778070],[-9.998637,3.849130,-7.540146,5.456104,9.115035,5.999408,2.739919,-5.909375,-8.418546,3.498242,-5.818894,-8.303089,-2.787535],[4.747865,0.638709,-6.005033,8.285886,-6.756353,5.636717,4.129243,4.165496,-1.986731,0.400347,-4.688157,-3.948605,1.244627],[2.037550,-0.323167,-0.602557,-0.905506,2.288236,-7.805608,-9.652928,1.999536,-2.158749,9.640492,2.972954,-7.814008,-2.588856],[-9.512466,5.488352,0.263594,9.057162,-5.904447,-9.131981,0.692660,-7.156202,-9.364497,-4.703111,-7.058331,-9.468165,9.747316],[6.287216,-5.906769,-3.322834,-7.610656,-8.969563,-8.198810,9.869597,-1.827660,2.299850,-0.973455,0.493819,5.683063,-1.586968],[-0.800999,5.787771,-1.703111,-1.405471,-6.864742,3.289792,-6.080413,2.987875,-9.530557,6.750258,-7.945478,-0.750554,-7.176385],[2.556229,-7.325849,2.378684,-6.191336,-8.392742,-4.402543,8.458927,1.344083,9.936843,-4.198977,1.810052,-5.795204,5.078109],[0.128125,8.701812,8.774175,0.873640,-3.377413,0.115757,0.760551,7.944016,-5.763870,2.475091,9.818711,0.821669,2.835408]],[[-2.761517,3.244966,-4.673128,-8.354951,8.670952,-1.947690,5.839750,3.098864,1.219354,-0.008803,-8.029463,3.251908,-7.228984],[9.691293,-2.310577,-0.623753,-8.918488,7.792903,7.582888,-8.259146,8.581772,6.526941,0.855430,2.732400,-7.510242,1.297695],[-0.692079,-7.317395,0.010673,-0.042983,-4.205911,6.360878,6.702190,0.908537,-0.405185,4.702999,-7.132064,-2.194014,9.831022],[-1.927557,5.531800,8.123424,-6.197709,-6.991391,1.138659,4.615141,-3.821487,-2.290849,8.662003,-3.730964,7.659716,-9.932503],[-7.858845,1.524325,-2.318848,6.461833,5.643907,-3.789602,-7.902850,4.656830,9.840362,2.693600,8.787871,7.408361,4.696862],[-4.766740,4.154807,-5.413589,8.153193,-4.755821,7.609527,5.661786,-6.081206,-6.803609,6.919066,-0.937977,0.425730,-9.682437],[1.066688,1.098115,9.404689,6.095707,-9.108226,-3.915327,1.184143,-2.869828,0.381957,4.012466,3.376001,-1.645053,5.661406],[9.099788,1.626230,-1.308771,-8.582372,4.524726,8.670258,-9.721511,9.478045,-2.757366,1.113358,5.134438,-9.973446,-6.545181],[1.377123,-7.731789,2.630607,2.169845,7.227010,3.543364,4.453142,7.946455,6.883142,4.640020,1.379853,5.509873,-6.887086],[1.851216,9.496912,-4.487197,-9.650291,-9.434019,-3.396915,-5.465810,7.423539,4.484490,7.009359,6.166706,0.884254,7.413951]],[[-4.654175,2.677683,2.424960,-7.670112,4.333544,2.314239,8.231921,2.529216,0.327283,-1.082187,-0.820785,-4.232196,-2.700412],[-1.571955,-8.690558,-1.186043,8.967269,3.381712,-3.648388,9.077343,-8.245339,-2.890270,-6.886449,8.150011,3.296752,-8.598980],[-3.146288,1.400005,4.704779,-6.063436,1.753677,-8.048147,-8.427949,-3.775795,2.282994,-9.227238,-9.994617,-1.602286,8.441252],[3.292193,9.707865,-5.548042,-6.617029,-8.383660,3.561512,1.268440,-1.900069,0.876799,5.575001,0.046962,-9.222717,-4.798153],[-1.571891,7.570781,-7.311031,3.694019,9.893316,1.539236,7.858364,5.892238,-7.641376,-1.757392,-4.922195,-5.510752,7.585482],[1.323114,7.002123,-6.873451,-5.309160,4.268901,-3.387210,-6.374673,-5.220125,0.340746,2.498861,5.109202,4.549476,-9.342889],[5.679744,7.837078,7.180025,-9.173267,-3.149115,-9.076723,1.198449,-2.151877,-7.559536,4.240631,-1.701826,2.133741,8.609955],[-7.514873,-3.757154,-0.187796,1.965985,-0.519476,-1.400449,3.525519,7.577093,7.549260,-9.553800,8.753004,-0.172797,4.711184],[5.928969,4.349841,9.974880,-3.534162,-2.289693,-3.243703,-2.559311,-5.133133,9.136844,-3.077508,-0.135145,4.877083,2.769127],[9.347084,7.696473,-5.076648,4.368927,5.424222,4.514293,-7.676551,6.888309,8.182716,3.668248,-5.881766,-8.841458,-3.040461]],[[6.356848,5.030157,-3.266412,-9.643698,4.935238,-5.659589,-9.071095,-4.331615,3.794495,-7.467315,6.244977,1.299268,1.909029],[6.568903,-9.690347,-9.924198,-3.415797,-1.870659,6.539644,-8.206721,1.524655,2.450972,6.696120,-0.418054,3.167815,2.005066],[-8.507289,0.874310,-5.131185,6.701881,-9.501547,-2.215017,0.743298,9.678133,-1.155775,-7.964434,3.395038,1.455494,5.205307],[1.498972,-9.684929,7.801992,9.712178,2.910166,8.383670,-3.186466,-4.901996,-0.754262,9.265609,-2.202262,-7.944149,-9.211496],[7.359478,-2.173905,0.635550,8.822606,-4.991856,-8.122862,1.462839,4.308969,3.017269,3.741835,4.864521,5.194635,9.440336],[-1.241387,-6.959287,9.355938,-6.849138,-9.979412,-2.267913,-5.315677,-5.268095,-8.946064,-7.603901,6.634378,-8.868279,4.147389],[-2.802306,-8.726684,1.962396,1.126268,8.346081,4.337865,-2.700909,5.776956,1.730358,0.644414,9.140830,8.692823,-0.449941],[3.394216,5.790243,-6.067975,5.755654,-6.908691,3.083276,0.262699,-3.032696,-9.982352,-4.343808,2.262441,9.778376,-1.338352],[6.012791,-1.549795,-6.984092,-9.689413,2.063620,2.187425,3.953741,8.591457,-2.929020,-2.485979,5.055494,8.045577,-3.674720],[7.915492,-4.408689,-7.412370,7.498730,4.004889,-6.387920,-3.802997,-7.909484,9.377148,1.794207,-2.260869,1.207663,-0.481704]],[[8.259565,-8.511630,7.179034,-6.118959,6.655879,3.335613,4.840306,-7.795920,-9.782085,2.401751,3.276344,-8.837023,8.586707],[-4.503376,3.453649,0.147204,-1.902393,9.300433,3.619063,4.702598,-8.461258,-1.198335,9.387799,-2.038327,9.025868,-8.975728],[-9.885996,2.531625,0.295552,-0.674600,-2.635006,-4.651545,1.723967,-1.208396,0.951825,-8.026490,-0.269284,8.314569,3.084506],[7.003059,-7.050769,3.039946,8.787380,-6.955840,-7.473339,1.693344,9.089226,-4.942320,1.991756,6.252315,-0.172491,4.679384],[-4.304255,4.500973,-9.062656,-1.200763,-3.685094,3.135890,-3.840661,1.554346,-7.491866,-7.299111,-3.024932,-4.885414,1.763155],[-1.263640,0.118501,2.713679,-6.200804,-0.884994,4.401809,6.072124,-8.289728,3.754914,1.498783,-1.189895,-1.903745,3.744282],[4.150214,-3.603763,1.946638,-6.853792,-8.001860,1.774726,-8.827404,1.793073,-9.553844,-4.955927,4.747597,-4.551535,-6.043354],[-8.359519,4.152706,0.977664,-0.779875,8.550457,-1.191817,-4.481476,9.132825,1.372042,6.507595,-8.734827,-6.374124,5.668468],[-3.067052,-0.039988,-2.716691,6.846858,-3.190683,-4.394040,5.236149,-7.536786,9.773884,-4.980242,-2.589384,5.477998,5.202317],[-4.955879,-1.382671,0.037974,0.476961,3.551638,4.496751,9.046853,0.751128,-0.197680,8.513326,-1.530254,6.162323,-0.112535]],[[-7.105470,-4.020641,1.540594,5.896036,-9.362112,-0.289662,-7.224034,5.231389,1.537585,7.308619,-2.705115,5.642821,6.660848],[-5.676083,-5.520135,-2.421333,-7.803753,-6.392798,6.628297,1.859463,2.457368,4.366985,4.241303,2.447582,7.079917,4.128019],[-6.972209,-2.724337,-4.487059,-7.287858,2.467991,-0.489851,1.442506,2.081587,-0.507957,-1.275688,-1.138971,-0.811405,-5.981424],[-1.572883,-4.883681,2.604220,-2.752569,-0.488716,2.383479,-0.431730,-7.223918,-1.395215,5.117778,-6.879769,5.853140,8.587901],[8.506668,5.706518,7.830363,6.715241,-8.678168,-0.857852,-5.339653,2.270049,-6.583058,-8.664398,-6.657012,-7.946125,-0.200971],[-6.468017,-7.277278,-5.891871,6.458843,2.978150,7.570565,-4.427104,-6.949141,5.407356,-9.117598,-2.438927,-6.323698,7.378682],[9.490840,-4.734195,-6.914152,5.543241,6.375060,-7.041381,-7.923989,5.005440,8.110181,0.702200,3.355533,-1.883894,6.893956],[-1.700718,-3.037326,6.112814,5.961079,3.284138,-3.284378,-7.705296,-1.667632,-7.794270,8.064232,4.843450,8.289746,-8.403661],[2.481725,-6.519234,2.207646,-7.182392,-0.528533,6.047080,3.961199,-6.298552,-3.838440,3.599737,8.605847,3.277441,-1.507569],[2.509445,1.154827,-5.097716,2.992093,1.744417,8.506806,-6.563562,7.726185,2.188501,-7.546590,-9.574118,4.529316,-0.998981]],[[3.275729,9.259847,-4.032886,-3.844160,-3.834758,-8.053752,8.478923,-2.851499,7.682063,2.790855,-9.368290,8.724000,-4.524479],[4.890456,-8.550105,-4.649980,6.565058,0.960973,6.060298,4.145408,-0.051090,6.854852,-6.894437,-4.346107,-3.354039,-6.591584],[-1.004445,7.962170,-8.238545,-9.772911,-8.905651,-7.839348,-4.917620,0.755961,2.178884,5.312945,-6.257265,-1.984599,-6.052050],[-2.295637,-5.727320,-1.081851,3.437310,4.709685,-0.168972,-9.219199,-8.095113,4.241904,-0.561034,-8.738608,2.809005,9.329246],[-9.264108,-7.903575,-6.569631,8.194570,-5.597707,9.020932,-5.942633,1.253463,8.881707,7.438293,-4.665829,-2.918472,-3.049984],[0.992227,1.833624,7.604653,-9.049208,-9.948795,8.040376,7.820079,9.354831,2.216604,4.606817,2.200458,-2.100671,-2.014484],[9.717641,4.306804,-0.808689,3.257409,8.524158,8.144947,7.214727,-8.746711,-5.436402,-7.084925,-1.339349,4.649336,-9.144166],[-8.815832,7.512994,4.181457,-0.506940,-8.125026,1.190882,-3.761469,7.314349,-3.257438,3.538572,3.746425,-6.773209,-9.363490],[7.912258,-7.558681,-3.050084,-0.188055,-3.133096,-7.535358,-5.328601,9.579199,-9.558772,-6.794452,2.010485,-8.130448,3.413196],[-4.778730,0.288496,-1.235523,-4.184187,-7.607021,-0.860990,6.260831,9.168494,1.835495,-6.487772,9.581175,-9.563877,-6.222048]],[[4.281784,-7.058472,-7.166628,-0.962035,7.757571,-4.208455,-9.181017,-5.179858,0.219959,2.142704,3.104154,-6.661249,5.828109],[9.020375,3.300946,9.655804,-8.275088,0.347507,9.393906,1.143694,8.030872,-4.344256,-7.320226,-7.706887,-0.991366,-5.115731],[-7.168639,-4.952863,5.577025,5.190904,4.082151,7.027312,-1.373865,4.256210,-9.733275,8.198573,-9.442334,0.423144,-8.530809],[3.265438,2.052520,9.005795,-9.254846,4.441412,2.406075,4.842365,-1.087733,-0.580349,6.365626,-6.221720,-4.524353,4.719971],[0.673754,-3.110743,-5.680432,3.889642,7.275336,5.745969,-7.100478,9.484461,7.388347,-2.419320,6.963977,0.564728,-7.733410],[0.815771,0.712120,-3.244272,6.102030,-7.225930,-1.823183,-7.061590,-7.254422,1.897573,-7.846110,-6.444370,2.070068,7.738065],[-7.172784,-3.047511,-7.196668,1.029058,-9.438224,3.364755,-2.086703,-4.253224,9.880941,6.315060,-3.075778,-4.242376,6.579391],[5.868728,0.233703,-7.610577,7.027610,9.783518,-3.610527,1.692608,-7.885340,-6.595231,-7.558562,7.637003,7.000216,-4.287832],[1.130990,8.827789,9.886961,-0.734224,4.264031,-7.857922,0.325930,8.602669,5.022147,-9.281814,8.206803,-6.198663,3.037801],[8.614539,-4.316556,5.252698,-0.103763,2.148598,3.565537,-6.868035,-5.221124,5.814152,-2.145576,4.882937,7.313302,8.201133]],[[-3.469909,-4.118465,7.476696,3.361399,8.028890,-5.460603,3.802134,-0.241849,3.606539,6.854097,8.465824,6.745752,2.850833],[6.407418,-3.095863,3.723741,3.541742,7.968914,1.683347,-3.078680,7.033281,-9.551537,-5.407390,2.907610,-6.435620,6.609264],[1.982078,7.854350,7.549090,8.340654,-6.016114,2.956454,-4.504004,-8.109383,4.238015,2.696667,9.082969,9.327766,-5.219592],[3.558312,4.375447,-7.360529,7.990719,-6.246995,4.608988,9.310317,-0.525399,0.941549,6.303874,7.051673,-2.557591,4.119178],[-6.619142,-2.756640,1.160927,4.927175,-2.197963,5.327452,-2.717837,2.903624,6.073948,7.962776,2.379034,-8.658074,-6.603274],[2.780842,-9.217471,2.273053,2.276591,9.795145,7.109590,1.631606,1.092588,-2.412199,-9.809418,2.703398,-6.384656,-1.862234],[9.296966,-5.710011,-9.317508,-3.568039,-2.390135,8.757831,5.802433,-4.885721,-9.435710,0.676152,-2.470167,0.932538,8.157525],[-5.842843,8.089306,0.054287,0.099135,-6.198089,0.597575,7.908867,-9.753020,7.055558,1.250394,8.342791,4.867464,2.468072],[-2.460187,7.621660,5.736491,1.384482,-3.106365,6.577704,-9.398329,2.053180,3.651411,4.858496,7.963405,2.791068,-8.260633],[-6.250574,2.548071,0.678351,-1.845439,4.839776,-4.601629,-4.764011,6.471750,-8.000587,-7.419985,2.866230,-0.820462,1.044774]],[[1.469278,0.968790,6.785027,-9.382312,6.633487,-7.974166,-7.734520,-2.504875,-2.906598,8.465927,-2.384010,5.944518,8.160808],[-1.509706,7.536944,6.303641,2.577312,-1.643766,4.018905,7.512427,-6.599223,-6.259865,-5.292821,1.562919,-1.180102,-1.706454],[2.004477,8.938489,4.074369,-3.820662,1.049345,1.737656,-4.997745,-9.928717,-9.780886,0.011429,2.070318,2.912894,-5.100191],[1.865819,1.588366,9.023989,8.791201,2.172447,9.521405,-7.379218,-3.304449,6.916408,0.847645,-7.990950,0.822745,8.245436],[8.899208,-8.394945,7.346303,-4.944715,-9.572937,0.580281,-0.677532,-1.849577,6.992616,0.031123,-7.592429,-0.723608,-8.349863],[-3.383650,-4.216965,-2.059119,-5.460192,8.548045,-5.122335,8.869052,-3.885500,6.888021,5.038678,-0.543322,-8.908017,-1.757732],[-2.841144,-5.090371,4.234656,-3.697440,-5.640798,-0.498174,-8.925707,9.685947,0.384428,4.979714,8.097762,5.063001,-4.196443],[2.479649,4.380324,9.568135,4.157692,-1.811988,-1.711325,-4.675595,3.055696,-4.712263,8.533382,5.125851,-0.273869,-1.141534],[4.095319,-7.357498,9.177419,-1.725017,-9.698067,-1.283655,1.398852,-5.853325,9.715977,9.777469,0.260657,-7.192879,8.955801],[-6.383547,-7.063472,2.469069,-4.313964,4.636257,-8.049880,-5.531859,-1.176245,-7.798488,7.593561,2.768350,5.140697,8.604071]],[[-8.846833,2.273950,3.017797,4.930127,-0.094238,4.023522,3.390398,-3.719099,-3.975091,-8.732210,0.718061,7.203775,3.703838],[-3.810358,4.356126,-0.575208,9.500470,1.153770,0.022367,3.649020,6.688576,-7.222954,7.220972,-9.620973,4.468832,-1.360085],[7.667097,6.267771,9.579592,-5.981835,5.662457,-9.331616,-3.675538,-0.942817,1.317061,-0.550270,-2.880996,8.153735,0.117653],[-7.844105,-1.230801,-5.773000,-9.728197,-3.763216,3.729167,-1.512506,7.514493,9.939468,-5.555101,3.334424,4.972032,-0.360522],[-6.706613,-3.344073,-2.111821,-8.287254,4.331964,-8.781329,-6.366955,5.646962,1.926752,4.844441,6.324410,7.761265,-0.093046],[5.807643,-3.737370,5.833725,3.376740,-9.453230,-1.728167,-7.051507,8.588324,0.300736,3.526296,8.269877,-4.638252,-7.334662],[-4.997292,4.108422,-1.440934,-1.930601,4.065514,-2.136162,3.682156,-0.040950,2.784898,-5.891354,7.186143,7.645029,-3.267767],[-3.892453,2.443330,-7.492744,-6.683072,-7.436216,-3.283524,8.471607,-9.761437,-8.224119,-8.427590,-3.971075,9.147674,3.891749],[-6.116544,-8.419964,0.544246,-3.910461,1.407037,-9.529823,-8.603472,-5.586275,-0.997116,-6.624862,2.632250,-2.856839,3.352773],[-4.223081,6.486596,-8.636161,-6.023251,7.165016,5.489501,-2.373401,-9.900505,-0.875557,3.102332,-6.084570,-1.337559,-5.389353]],[[1.721954,7.372960,1.479159,-0.671929,5.915330,1.826187,2.359357,-5.426550,-4.974153,2.768148,4.563037,6.206918,-5.233812],[-5.770088,4.843234,0.111583,-6.476593,4.199622,-9.994165,-2.714230,-6.665434,8.346590,-6.409331,-1.131109,-7.871094,-8.185251],[5.966383,-5.240248,0.725204,-3.114881,7.611121,4.054732,5.716645,-4.207332,-0.999170,4.312370,-4.073823,-3.066217,-7.273182],[1.921672,-5.769130,9.753342,2.768468,-7.396438,-9.699781,5.856515,-1.658756,4.182184,-4.114824,0.889080,6.088974,2.723323],[6.300450,-3.966240,5.117840,-7.176443,2.249702,1.386768,1.969523,4.072347,5.219862,9.051949,-9.587420,0.838246,-2.575040],[1.478982,2.070268,6.705068,3.421255,8.631942,0.621629,-8.565853,5.588912,-9.939721,8.365676,-2.574258,-9.853968,-9.259388],[6.366509,6.508830,-5.119911,4.570689,-4.076088,-7.546898,-4.199917,-7.540149,5.920809,7.185318,-6.615326,8.755009,0.781977],[-3.329599,-7.339715,-1.310195,-1.503094,7.701796,1.679220,5.071862,-1.005262,9.016371,0.360913,-6.818571,-0.346880,2.581963],[9.118432,3.556739,-4.781164,5.873041,-0.157517,-5.762726,7.858571,-0.292245,-8.446232,-3.864796,4.793157,-7.353068,7.111579],[-0.748784,-2.321408,4.324809,-7.357522,-5.366742,-3.009374,3.861881,-3.432205,-1.178557,-9.428504,-5.054141,-5.562262,8.863328]],[[-8.911052,-9.026448,-0.636380,3.603756,-9.409161,7.041228,3.228769,6.502749,2.421844,5.677503,0.712025,1.171338,-6.117321],[-7.395378,1.691980,-0.865262,7.762487,2.724307,4.886831,-2.672972,9.002663,1.933807,-9.185569,9.928787,4.765830,8.844382],[-4.022627,-7.065729,-9.719159,3.041375,-0.090353,9.616762,-4.323770,-4.204194,3.430542,0.620317,-3.052243,-1.263565,2.161866],[-5.688839,-9.117039,0.638357,-0.095101,4.348218,2.283856,-8.478990,-5.180855,4.119223,6.517709,9.287721,5.286511,7.404135],[3.888415,-0.213196,5.205332,5.694796,-6.314931,-6.127922,8.081694,7.227486,-8.149222,-1.125859,2.486150,4.838931,0.499365],[2.380077,8.168560,-2.754314,-3.282662,-5.611023,7.160205,9.170892,-5.040969,8.697720,1.002068,-1.333378,-6.607179,0.914688],[6.105829,-8.691831,4.632711,7.058894,8.844206,6.201300,-2.036005,1.202967,7.630971,0.991242,7.313940,2.351238,2.700489],[-2.706913,5.046700,1.734191,1.835830,7.889338,0.305702,0.336043,5.099470,3.978009,-9.348457,0.980805,1.238850,-4.317651],[0.268452,-5.337670,9.244975,6.956322,-9.804887,5.460438,-5.332515,-0.592156,8.350640,-7.137915,-7.975074,-3.879645,4.044316],[-3.703125,-3.489617,8.087792,8.988699,-8.825669,-5.071406,5.190810,-5.543632,-1.263897,6.050751,5.278465,5.345257,4.290900]],[[2.860095,-8.545677,-4.680952,4.694110,6.322395,-3.262973,-8.537965,-3.546643,-5.836919,2.278352,-0.150116,-8.557713,-0.505766],[3.253276,5.149064,5.140299,-2.496288,5.385510,2.142482,-8.286768,3.179914,2.124608,2.966571,6.647454,9.498218,0.315367],[-6.542330,3.128875,6.389234,-1.388388,-3.372756,7.728183,-6.896554,7.779481,6.526655,-3.991692,-0.957334,1.297681,5.972474],[-4.881285,5.223918,0.165208,0.167295,1.905378,0.102769,0.692501,3.384410,-9.720022,-3.487385,9.656121,2.669508,-4.859108],[3.115904,-2.621995,-3.988730,0.776046,-7.489719,-5.616730,-3.967691,-0.607956,9.125154,1.600495,-6.562227,-0.107688,5.513319],[-3.157160,-1.654386,-7.544060,-6.923186,-3.363336,6.073389,9.796587,-4.998095,4.621981,5.833738,-8.731682,-4.046142,8.388442],[-6.277587,2.191374,-8.686615,-4.107781,-1.895963,-7.938478,1.467948,-0.324198,6.185100,-5.223288,8.043518,-8.904000,3.513009],[9.572002,-7.559184,-5.400552,9.916220,-8.746224,-1.160402,-8.217992,6.122061,4.731245,9.952944,-0.665948,1.314164,0.311053],[-6.997653,5.780388,-4.396181,0.781184,-9.507025,0.799936,6.359517,6.910965,0.405523,5.439496,-9.771903,7.878916,-3.957037],[-4.375096,3.866566,-9.769391,3.892997,5.947131,-3.612752,-0.214099,4.326201,-7.793979,0.089285,-9.551211,5.319124,-5.184567]],[[-3.128495,-3.174511,0.564781,8.690774,-0.141095,-3.450523,9.640686,5.193135,9.803484,-8.596862,-2.209212,6.007843,-1.171682],[-5.483715,9.978078,-8.559295,-7.400196,-4.584534,9.373040,-5.095460,3.098623,-5.426530,1.068200,4.661134,0.950345,9.559832],[-1.176841,-1.750702,-7.755732,1.039669,9.000613,9.694307,-4.029313,7.208984,2.254434,5.234364,-3.276284,-0.188386,6.754702],[-5.225098,1.547852,-2.944024,2.286986,1.680997,1.723483,2.903270,-3.286828,6.247488,3.783333,-2.917254,-1.415584,5.997000],[5.640871,-4.158120,2.130634,-4.404957,-7.432399,5.488281,0.900868,6.435022,9.731226,8.231139,-6.785756,-8.915497,9.886594],[-1.745197,-9.493152,-8.448597,6.722379,-9.067666,-2.830777,-6.919490,-1.462827,-1.632341,-1.949154,-2.000339,-2.342181,5.185463],[-5.941356,-4.828778,-3.604965,-6.141318,8.556505,5.354093,4.247018,2.673906,-6.295167,1.156104,8.301834,-5.406407,0.666992],[5.421577,-8.814754,-7.013756,-2.619169,-2.384913,-0.474505,9.868144,6.988007,-1.697591,9.555145,-0.787844,3.106219,-1.594761],[9.325666,-1.489837,7.868629,2.368944,-3.374302,5.752212,-2.434784,-7.198920,-2.211117,-3.231822,-2.364840,-2.370870,8.814956],[5.795922,-8.204116,9.858531,-4.243953,9.726351,-7.353421,2.326364,-7.919940,4.879294,-6.026678,2.296709,-3.079779,-1.807002]]], dtype = "float64")#candidate|3658|(15, 10, 13)|const|float64
bop_3659 = relay.floor_divide(var_3657.astype('float64'), relay.reshape(const_3658.astype('float64'), relay.shape_of(var_3657))) # shape=(15, 10, 13)
func_2302_call = mod.get_global_var('func_2302')
func_2305_call = mutated_mod.get_global_var('func_2305')
const_3667 = relay.const(4, dtype = "uint32")#candidate|3667|()|const|uint32
const_3668 = relay.const([5,-9,-7,4,9,2,-2,-8,-3,-1,2,7,2,1,-9,-7,4,-3,-3,3,-4,-4,7,5,6,2,9,-9,-9,6,-9,-2,9,5,4,-7,-4,-5,4,-3,-7,10,8,-9,-2,-5,-8,-5,2,-10,-10,5,8,7,1,4,-4,-5,4,9,1,-6,-1,-7,-10,1,5,-6,-5,7,-2,5,-3,-10,8,-4,3,7,2,-1,10,4,6,-10,-10,9,6,-8,6,-10,7,-3,-4,8,-6,-8,-9,-4,2,-9,9,-4,6,5,-2,-6,9,-1,4,8,-8,-6,1,-3,-4,-5,2,7,3,-2,9,6,-9,-2,4,-1,-8,-9,-9,-2,-9,-3,8,1,-5,8,10,1,-1,-2,-3,-9,-2,-2,3,3,2,-2,-7,4,5,6,-6,-3,-8,-3,-10,3,-1,4,-8,-5,-2,-1,-2,-2,8,10,-5,-2,10,5,6,-3,-1,-10,-3,-9,3,-7,-6,-10,5,10,-3,-2,-8,4,-4,-10,5,6,-6,-6,-7,-2,9,9,1,3,-10,10,3,1,-2,-4,4,8,7,8,4,6,3,-9,-5,-10,-1,-2,-4,-2,7,-5,6,-2,5,6,10,-5,9,7,8,6,6,2,4,-6,1,-3,-5,9,-3,-1,9,7,-10,10,2,5,-8,9,4,3,7,2,1,3,-10,-8,-10,7,-1,-8,-4,2,4,4,-7,3,4,-7,1,-10,4,-8,-5,4,3,-9,-7,-9,-2,-8,3,-4,-9,4,1,-10,2,-1,4,-2,-9,4,-2,6,-9,3,-8,-10,10,-8,6,7,-6,6,4,-7,-9,-9,-3,6,-1,-3,-8,7,-7,-8,-3,-2,3,-10,-5,2,-7,6,-7,-3,1,-7,-9,6,9,8,9,2,-9,3,-9,-8,7,8,6,2,7,8,-6,-3,-8,-7,-2,-1,1,-5,-10,-9,-6,-10,-8,2,2,3,-6,-2,-7,1,10,-10,-9,-3,7,5,1,-8,10,6,3,9,-6,-2,-4,4,-9,6,1,-9,3,4,1,-3,-5,2,-8,5,-6,9,-4,-3,-9,-2,-10,7,-5,9,4,-7,-1,-4,2,5,10,7,8,8,-10,-6,-9,8,-5,-10,-9,7,-5,-10,-4,-4,-10,-8,-2,-4,5,7,-2,-10,1,7,6,-9,6,-8,4,-5,-5,-3,-1,1,4,2,2,4,-1,-3,-6,7,-4,4,-9,4,-4,-10,1,-1,-3,2,6,-1,8,3,8,6,7,10,1,-7,-1,9,2,9,-4,1,9,-8,-5,3,-3,5,-10,-5,1,5,-2,-5,6,-10,-7,2,-2,-4,-3,10,7,7,10,-10,5,4,10,2,3,6,-2,5,9,10,-6,10,-6,3,-9,9,-8,3,-2,4,8,3,-8,-3,8,1,-4,1,9,7,7,-4,-9,-3,-4,4,6,-4,-8,3,10,3,-4,5,-6,-1,-6,-8,-4,4,7,-1,-9,-7,-2,4,2,-8,-2,2,-5,3,-2,6,3,5,2,-2,3,-8,8,8,1,-10,1,3,7,-9,8,-6,-7,-10,10,-2,9,-9,5,-9,-7,1,1,4,-9,-8,8,7,-4,8,1,7,1,-7,5,-3,4,-10,8,-4,9,-4,-5,-6,-2,-3,4,2,-7,-10,-6,-7,-4,7,5,9,-3,-10,-7,-7,1,-9,9,-8,10,-1,10,-7,4,-8,-5,-2,-1,-7,1,7,-6,-6,-8,1,2,-4,-9,9,-7,4,-4,-10,-9,3,-5,-1,-7,-5,-1,4,-10,6,-1,3,-1,-10,3,2,-1,3,7,6,-1,2,-7,7,-7,7,9,-8,6,7,-9,3,-8,-7,-10,-3,-4,-5,3,10,-7,10,6,-8,7,4,-8,8,-3,3,8,8,-2,4,-7,5,-1,9,2,-4,5,-5,-6,9,7,-5,-7,-8,-6,-2,7,6,-2,-9,-4,-5,10,-10,-4,8,-8,-8,-5,-5,9,3,-7,-7,-6,5,-7,7,-2,-4,5,-10,4,-1,6,-10,-3,2,4,9,6,-9,6,-10,4,-7,-7,-5,6,-2,10,-7,8,3,1,-1,-9,9,10,-6,-7,-5,-1,-7,-6,7,-2,-3,6,-2,9,3,8,5,-3,-2,5,5,10,3,3,-6,-6,7,4,-10,-5,-2,7,2,-10,10,-4,3,7,1,-8,6,5,-10,5,3,7,4,5,-3,10,2,10,-9,-3,-8,-9,-9,-10,-5,-10,-4,8,-10,3,9,9,-7,-1,8,7,7,2,2,6,6,10,3,-9,-10,-8,-6,-4,-6,9,9,1,4,5,-5,5,-6,-1,-2,4,3,-5,-7,-3,-4,-10,-10,2,-2,4,-7,-9,6,4,2,-4,-9,3,-7,-2,9,-5,-1,-5,-5,2,-9,-7,-5,-3,-10,-2,-5,5,-3,5,7,3,9,2,-6,-6,-9,10,-5,-1,-1,1,1,-9,3,6,-6,-9,-6,8,7,-9,-8,-10,-1,5,-7,-7,2,-1,-10,6,-4,10,6,-2,-4,9,9,3,4,3,6,-8,-7,-3,5,-4,4,9,-4,3,1,9,5,1,2,9,-5,6,5,1,-1,-9,9,-3,10,-2,-1,-2,-5,-4,-6,-6,-1,4,-4,-7,10,-9,5,-5,-9,-5,-7,7,-9,-10,-5,7,1,-5,6,1,10,-8,-2,-2,-7,-1,4,-8,-10,-8,-7,2,-6,-4,-1,-2,-2,7,-3,-7,6,5,-8,2,1,5,-7,-7,-6,-7,5,9,10,-3,7,-5,10,4,5,5,10,-6,-7,-1,-4,-9,10,6,3,4,1,-4,9,6,6,10,1,2,-8,10,-1,-9,-4,2,-8,7,4,-10,-9,-7,-8,-2,2,7,-7,10,-6,1,-7,7,-7,-7,-8,-6,-3,-6,1,-2,-10,-2,7,-6,-4,3,8,-9,6,8,2,5,-8,-6,6,1,-8,4,-9,-6,-5,-6,-1,-8,10,-3,1,-8,6,7,10,10,2,-3,6,4,10,-4,7,-8,-9,1,-6,8,-1,-7,-4,-10,3,-9,-5,-10,-3,8,10,8,6,1,6,-5,8,-9,1,9,5,2,-1,6,1,-5,-7,-2,10,-4,-5,-3,-3,3,4,-9,-2,-10,5,8,-8,-7,-5,10,2,-2,-7,8,-1,-5,7,-5,-2,3,-9,-5,5,3,-1,-5,-7,10,4,-5,10,-10,-1,-7,8,-2,10,-5,9,5,1,5,-7,-3,2,5,-5,1,2,8,-8,6,-8,-3,8,-9,7,6,-8,4,4,-3,8,4,-4,9,-3,-9,5,9,9,-2,-3,-10,-9,10,6,4,-9,-4,-9,4,8,-4,-5,-8,-1,9,-3,5,-5,-5,10,7,-8,-4,-1,-10,2,-4,4,-9,6,-9,9,1,8,-5,5,-8,10,-9,-10,4,2,-7,1,3,6,-6,-5,8,-3,2,4,1,3,9,-1,-5,2,-9,-2,10,-4,4,3,3,-7,-4,-6,-7,6,-4,10,10,-5,-4,-3,4,1,7,10,-2,6,9,2,2,-1,-7,-10,-2,-7,-2,1,10,-4,7,-8,2,-4,7,-7,4,-7,-1,-7,2,9,6,9,-9,-2,10,5,3,3,5,-9,9,9,3,-3,4,10,-2,-8,4,9,-10,-6,-4,-3,10,-8,-9,1,7,-8,7,-10,7,-10,-8,2,3,-2,-8,6,8,7,4,-1,3,1,7,9,-9,-4,-7,-8,-6,-7,-7,10,-8,-3,6,-3,-3,-1,6,-6,-8,-4,7,-5,-2,7,5,5,6,-8,-1,-5,5,-9,-5,-6,5,10,-1,7,7,-3,1,8,5,2,-6,2,-3,2,6,-1,-9,-5,5,-6,-3,-5,-6,-2,10,6,-2,-9,1,-3,1,-10,-6,-3,-6,-3,7,-5,-2,3,-2,-8,-1,-9,8,9,-7,-10,-5,-2,-1,10,-5,-2,-4,9,-5,-10,3,9,3,-1,-1,3,-3,5,-2,-3,-1,-3,1,1,-8,4,-4,5,3,10,-6,-7,10,4,-10,2,-3,6,-7,-9,10,10,-6,-1,-10,10,4,8,1,9,-10,-3,-5,6,6,1,-9,-9,-6,4,3,-4,3,-2,-4,6,-3,-7,-9,-2,-8,-2,4,2,6,-5,-1,-6,3,-9,-1,2,-5,2,-2,3,-7,-7,-8,10,6,-3,-6,-9,6,-5,4,-3,-4,5,1,-8,-2,-1,5,-6,-9,-7,-7,2,-6,-2,-2,-1,2,-6,3,3,-8,-10,8,-3,-7,9,-9,-9,8,5,-6,10,-2,3,10,-5,-2,1,-10,-6,7,1,8,10,1,10,4,9,6,-3,8,3,2,-10,8,-9,1,10,-2,-7,-8,4,7,-7,-3,-9,10,-1,-6,7,6,1,-8,9,1,-4,-3,10,2,-10,10,10,-1,-4,-3,-5,7,-8,-8,6,3,8,-10,3,-8,1,-4,9,1,4,-4,-2,-6,-7,-7,4,5,-5,2,1,3,-9,-10,-2,-2,4,7,9,6,6,1,3,-1,2,-6,-3,-4,6,3,-6,4,2,-6,3,-7,3,-8,-3,-5,-4], dtype = "uint32")#candidate|3668|(1716,)|const|uint32
call_3666 = func_2302_call(relay.reshape(const_3667.astype('uint32'), []), relay.reshape(const_3668.astype('uint32'), [11, 13, 12]), )
call_3669 = func_2302_call(relay.reshape(const_3667.astype('uint32'), []), relay.reshape(const_3668.astype('uint32'), [11, 13, 12]), )
output = relay.Tuple([bop_3659,call_3666,const_3667,const_3668,])
output2 = relay.Tuple([bop_3659,call_3669,const_3667,const_3668,])
func_3672 = relay.Function([var_3657,], output)
mod['func_3672'] = func_3672
mod = relay.transform.InferType()(mod)
var_3673 = relay.var("var_3673", dtype = "float64", shape = (15, 10, 13))#candidate|3673|(15, 10, 13)|var|float64
output = func_3672(var_3673)
func_3674 = relay.Function([var_3673], output)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3063_call = mod.get_global_var('func_3063')
func_3065_call = mutated_mod.get_global_var('func_3065')
call_3696 = relay.TupleGetItem(func_3063_call(), 2)
call_3697 = relay.TupleGetItem(func_3065_call(), 2)
output = call_3696
output2 = call_3697
func_3704 = relay.Function([], output)
mod['func_3704'] = func_3704
mod = relay.transform.InferType()(mod)
mutated_mod['func_3704'] = func_3704
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3704_call = mutated_mod.get_global_var('func_3704')
call_3705 = func_3704_call()
output = call_3705
func_3706 = relay.Function([], output)
mutated_mod['func_3706'] = func_3706
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3637_call = mod.get_global_var('func_3637')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_3748 = func_3637_call()
call_3749 = func_3637_call()
uop_3754 = relay.log10(call_3748.astype('float32')) # shape=(12, 10, 9)
uop_3756 = relay.log10(call_3749.astype('float32')) # shape=(12, 10, 9)
uop_3764 = relay.sigmoid(uop_3754.astype('float64')) # shape=(12, 10, 9)
uop_3766 = relay.sigmoid(uop_3756.astype('float64')) # shape=(12, 10, 9)
bop_3767 = relay.power(uop_3754.astype('float64'), relay.reshape(call_3748.astype('float64'), relay.shape_of(uop_3754))) # shape=(12, 10, 9)
bop_3770 = relay.power(uop_3756.astype('float64'), relay.reshape(call_3749.astype('float64'), relay.shape_of(uop_3756))) # shape=(12, 10, 9)
output = relay.Tuple([uop_3764,bop_3767,])
output2 = relay.Tuple([uop_3766,bop_3770,])
func_3775 = relay.Function([], output)
mod['func_3775'] = func_3775
mod = relay.transform.InferType()(mod)
output = func_3775()
func_3776 = relay.Function([], output)
mutated_mod['func_3776'] = func_3776
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3467_call = mod.get_global_var('func_3467')
func_3468_call = mutated_mod.get_global_var('func_3468')
call_3784 = func_3467_call()
call_3785 = func_3467_call()
output = call_3784
output2 = call_3785
func_3792 = relay.Function([], output)
mod['func_3792'] = func_3792
mod = relay.transform.InferType()(mod)
output = func_3792()
func_3793 = relay.Function([], output)
mutated_mod['func_3793'] = func_3793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3467_call = mod.get_global_var('func_3467')
func_3468_call = mutated_mod.get_global_var('func_3468')
call_3834 = func_3467_call()
call_3835 = func_3467_call()
func_1046_call = mod.get_global_var('func_1046')
func_1048_call = mutated_mod.get_global_var('func_1048')
const_3840 = relay.const([-2.880928,-1.830499,-9.829951,6.282755,5.562474,-5.216362,1.896550,0.278236,-9.618893,-7.765370,1.110007,4.630981,1.851294,-8.449565,-6.130646,7.957375,-5.222955,-6.068775,-3.428437,-8.384134,-0.735549,-7.856371,0.405419,-6.808711,-2.802328,9.352403,7.349990,-4.480609,9.303102,6.228555,0.979064,-8.467880,-3.520697,-8.832427,2.102309,6.860456,2.411762,5.757662,1.665577,7.682364,-2.588733,8.776419,5.363001,-2.698725,-5.750079,-1.569132,1.787758,-6.468931,2.115197,-7.456607,2.311786,9.244873,3.087393,-5.433645,-9.855517,-9.477529,-7.707836,-2.532478,-2.342977,-1.619123,1.188831,-6.249537,-5.332311,-3.475305,9.585805,-4.431163,-2.673822,6.430014,-6.575266,-0.249872,0.703247,-1.760754,8.857414,6.398271,4.774453,-7.494929,-7.159464,3.904892,6.030519,8.116211,0.587107,-2.529728,9.251839,4.560234,2.388994,-6.558432,2.865099,-0.277061,-2.048538,-4.780630,-0.644310,-9.129914,8.465916,4.513531,6.110391,3.796889,-9.382293,2.721531,6.175389,0.853586,-9.284662,-0.659658,-1.938365,-6.426905,-9.211225,5.633101,-8.352687,-7.610446,5.447302,-3.590683,-7.560687,8.705393,2.742628,-3.553134,-4.379321,2.937879,8.247294,-5.940312,9.786900,-8.333913,9.433598,-6.885863,3.014320,9.196350,-0.364451,-9.369823,3.763974,1.066920,-9.770765,9.729085,8.229706,3.329990,-3.481935,8.979620,1.587491,-6.718636,4.463047,-0.306427,2.727757,8.714004,6.507338,-5.247986,-0.990141,-3.756195,0.187164,5.159707,-0.191712,6.618499,-6.318392,-3.063379,3.396825,-5.583559,5.576423,9.797410,-4.441284,-2.642907,-8.840182,-9.694734,-0.715467,4.842029,-3.052977,5.997230,-2.225106,-8.009095,0.413652,-8.270222,0.835331,9.282011,1.362675,8.218430,1.509442,4.754402,-9.042559,-3.045018,-1.019836,-5.840056,-8.759389,-2.346406,-2.152646,1.680913,0.155312,-9.215410,-4.239346,-5.434405,8.797647,4.038880,8.562129,-9.020965,-6.915686,5.746943,9.725052,-9.187426,2.816890,-4.621207,0.480780,1.368706,1.071648,8.042541,1.090120,7.043847,3.034988,2.588579,8.463948,-6.976383,0.700729,5.264648,0.402062,-9.513023,-2.576222,-2.691096,9.594439,-0.614998,-8.778542,-2.339247,6.464760,-6.932131,1.065070,-4.064927,8.101991,-3.969234,-1.298845,1.000177,1.113423,-3.171948,-0.873902,8.232579,-0.865553,-3.498291,0.726981,-7.456222,-0.910209,9.606604,-0.954742,0.155185,-9.832918,-4.774440,2.127776,-3.961948,-1.320922,-8.691351,-2.088956,-5.372418,0.058799,6.140914,2.113915,-8.532313,-6.445061,2.408309,5.069255,-7.700163,1.818330,-4.321724,0.190349,7.715354,3.752743,-7.748453,-0.495343,-0.587009,-5.085470,-5.180407,2.488978,8.589972,6.731400,-5.236719], dtype = "float32")#candidate|3840|(264,)|const|float32
call_3839 = relay.TupleGetItem(func_1046_call(relay.reshape(const_3840.astype('float32'), [12, 11, 2])), 0)
call_3841 = relay.TupleGetItem(func_1048_call(relay.reshape(const_3840.astype('float32'), [12, 11, 2])), 0)
uop_3847 = relay.rsqrt(call_3834.astype('float32')) # shape=(12, 10, 9)
uop_3849 = relay.rsqrt(call_3835.astype('float32')) # shape=(12, 10, 9)
func_2870_call = mod.get_global_var('func_2870')
func_2876_call = mutated_mod.get_global_var('func_2876')
const_3857 = relay.const([False,False,False,False,False,False,False,True,False,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,True,True,False,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,False,True,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,True,False,True,True,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,False,False,False,True,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False], dtype = "bool")#candidate|3857|(819,)|const|bool
var_3858 = relay.var("var_3858", dtype = "float64", shape = (16, 2))#candidate|3858|(16, 2)|var|float64
var_3859 = relay.var("var_3859", dtype = "int32", shape = (720, 1))#candidate|3859|(720, 1)|var|int32
call_3856 = relay.TupleGetItem(func_2870_call(relay.reshape(const_3857.astype('bool'), [819,]), relay.reshape(var_3858.astype('float64'), [16, 2]), relay.reshape(var_3859.astype('int32'), [720,]), relay.reshape(var_3859.astype('int32'), [360, 2]), ), 1)
call_3860 = relay.TupleGetItem(func_2876_call(relay.reshape(const_3857.astype('bool'), [819,]), relay.reshape(var_3858.astype('float64'), [16, 2]), relay.reshape(var_3859.astype('int32'), [720,]), relay.reshape(var_3859.astype('int32'), [360, 2]), ), 1)
bop_3862 = relay.add(call_3839.astype('uint64'), relay.reshape(const_3840.astype('uint64'), relay.shape_of(call_3839))) # shape=(12, 11, 2)
bop_3865 = relay.add(call_3841.astype('uint64'), relay.reshape(const_3840.astype('uint64'), relay.shape_of(call_3841))) # shape=(12, 11, 2)
bop_3873 = relay.not_equal(uop_3847.astype('bool'), relay.reshape(call_3834.astype('bool'), relay.shape_of(uop_3847))) # shape=(12, 10, 9)
bop_3876 = relay.not_equal(uop_3849.astype('bool'), relay.reshape(call_3835.astype('bool'), relay.shape_of(uop_3849))) # shape=(12, 10, 9)
func_3355_call = mod.get_global_var('func_3355')
func_3359_call = mutated_mod.get_global_var('func_3359')
var_3880 = relay.var("var_3880", dtype = "float64", shape = (640,))#candidate|3880|(640,)|var|float64
const_3881 = relay.const([-3,10,-4,-3,-2,4,3,-10,2,-6,-3,-9,-6,5,10,-8,3,-5,10,7,-8,-1,-6,-10,5,7,8,6,-2,3,-9,7,8,-10,-9,-10,8,10,4,-6,-5,-1,-10,-8,-8,-4,-3,-10,2,-9,4,10,3,-8,9,10,-7,-8,5,-9,8,-1,-4,-3,-8,-7,-6,-6,6,-7,-10,-6,5,-3,-9,-5,-8,1,-7,6,1,-10,10,-5,2,9,9,8,-1,-6], dtype = "int32")#candidate|3881|(90,)|const|int32
call_3879 = relay.TupleGetItem(func_3355_call(relay.reshape(var_3880.astype('float64'), [16, 4, 10]), relay.reshape(const_3881.astype('int32'), [45, 2]), ), 5)
call_3882 = relay.TupleGetItem(func_3359_call(relay.reshape(var_3880.astype('float64'), [16, 4, 10]), relay.reshape(const_3881.astype('int32'), [45, 2]), ), 5)
var_3893 = relay.var("var_3893", dtype = "bool", shape = (12, 10, 9))#candidate|3893|(12, 10, 9)|var|bool
bop_3894 = relay.greater_equal(bop_3873.astype('bool'), relay.reshape(var_3893.astype('bool'), relay.shape_of(bop_3873))) # shape=(12, 10, 9)
bop_3897 = relay.greater_equal(bop_3876.astype('bool'), relay.reshape(var_3893.astype('bool'), relay.shape_of(bop_3876))) # shape=(12, 10, 9)
bop_3903 = relay.less(const_3857.astype('bool'), var_3859.astype('bool')) # shape=(720, 819)
output = relay.Tuple([call_3856,var_3858,bop_3862,call_3879,var_3880,const_3881,bop_3894,bop_3903,])
output2 = relay.Tuple([call_3860,var_3858,bop_3865,call_3882,var_3880,const_3881,bop_3897,bop_3903,])
func_3909 = relay.Function([var_3858,var_3859,var_3880,var_3893,], output)
mod['func_3909'] = func_3909
mod = relay.transform.InferType()(mod)
var_3910 = relay.var("var_3910", dtype = "float64", shape = (16, 2))#candidate|3910|(16, 2)|var|float64
var_3911 = relay.var("var_3911", dtype = "int32", shape = (720, 1))#candidate|3911|(720, 1)|var|int32
var_3912 = relay.var("var_3912", dtype = "float64", shape = (640,))#candidate|3912|(640,)|var|float64
var_3913 = relay.var("var_3913", dtype = "bool", shape = (12, 10, 9))#candidate|3913|(12, 10, 9)|var|bool
output = func_3909(var_3910,var_3911,var_3912,var_3913,)
func_3914 = relay.Function([var_3910,var_3911,var_3912,var_3913,], output)
mutated_mod['func_3914'] = func_3914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3009_call = mod.get_global_var('func_3009')
func_3010_call = mutated_mod.get_global_var('func_3010')
call_3988 = relay.TupleGetItem(func_3009_call(), 0)
call_3989 = relay.TupleGetItem(func_3010_call(), 0)
var_3998 = relay.var("var_3998", dtype = "float64", shape = (16, 4, 13))#candidate|3998|(16, 4, 13)|var|float64
bop_3999 = relay.divide(call_3988.astype('float64'), var_3998.astype('float64')) # shape=(16, 4, 13)
bop_4002 = relay.divide(call_3989.astype('float64'), var_3998.astype('float64')) # shape=(16, 4, 13)
var_4004 = relay.var("var_4004", dtype = "float64", shape = (16, 4, 13))#candidate|4004|(16, 4, 13)|var|float64
bop_4005 = relay.equal(var_3998.astype('bool'), relay.reshape(var_4004.astype('bool'), relay.shape_of(var_3998))) # shape=(16, 4, 13)
output = relay.Tuple([bop_3999,bop_4005,])
output2 = relay.Tuple([bop_4002,bop_4005,])
func_4018 = relay.Function([var_3998,var_4004,], output)
mod['func_4018'] = func_4018
mod = relay.transform.InferType()(mod)
mutated_mod['func_4018'] = func_4018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4018_call = mutated_mod.get_global_var('func_4018')
var_4020 = relay.var("var_4020", dtype = "float64", shape = (16, 4, 13))#candidate|4020|(16, 4, 13)|var|float64
var_4021 = relay.var("var_4021", dtype = "float64", shape = (16, 4, 13))#candidate|4021|(16, 4, 13)|var|float64
call_4019 = func_4018_call(var_4020,var_4021,)
output = call_4019
func_4022 = relay.Function([var_4020,var_4021,], output)
mutated_mod['func_4022'] = func_4022
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2889_call = mod.get_global_var('func_2889')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_4029 = func_2889_call()
call_4030 = func_2889_call()
output = relay.Tuple([call_4029,])
output2 = relay.Tuple([call_4030,])
func_4036 = relay.Function([], output)
mod['func_4036'] = func_4036
mod = relay.transform.InferType()(mod)
output = func_4036()
func_4037 = relay.Function([], output)
mutated_mod['func_4037'] = func_4037
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mod.get_global_var('func_3775')
func_3776_call = mutated_mod.get_global_var('func_3776')
call_4065 = relay.TupleGetItem(func_3775_call(), 0)
call_4066 = relay.TupleGetItem(func_3776_call(), 0)
output = relay.Tuple([call_4065,])
output2 = relay.Tuple([call_4066,])
func_4067 = relay.Function([], output)
mod['func_4067'] = func_4067
mod = relay.transform.InferType()(mod)
output = func_4067()
func_4068 = relay.Function([], output)
mutated_mod['func_4068'] = func_4068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3467_call = mod.get_global_var('func_3467')
func_3468_call = mutated_mod.get_global_var('func_3468')
call_4085 = func_3467_call()
call_4086 = func_3467_call()
func_2651_call = mod.get_global_var('func_2651')
func_2655_call = mutated_mod.get_global_var('func_2655')
const_4095 = relay.const([9.423499,2.520485,-7.338289,8.425738,3.486489,9.454063,-9.573821,3.166191,7.058211,-5.353357,-0.716802,-2.191933,2.392636,7.033107,-2.909484,9.103663,7.680843,2.441264,3.314690,-5.710431,-8.522669,5.745864,7.313913,-8.104589,-9.654849,5.259275,4.749955,-5.524169,-5.235682,7.360316,-0.077897,-7.694518], dtype = "float64")#candidate|4095|(32,)|const|float64
const_4096 = relay.const([6,10,3,6,-10,5,6,3,3,3,-10,-3,-3,9,7,-2,8,-5,-1,-4,-8,5,1,7,5,-5,10,4,-10,-1,-8,1,4,9,-9,-4,-4,-2,9,6,-9,9,-10,5,7,-8,-8,1,5,7,2,2,2,-10,3,-5,8,2,-6,-9,-2,7,4,-1,-7,4,2,5,9,-7,1,7,-3,-9,-7,-1,3,-6,-8,-7,-5,-4,6,1,7,10,-9,1,-7,2,-9,2,2,1,4,3,-9,-8,-10,-10,8,-7,8,-8,8,-10,2,-1,9,4,-1,5,-6,5,-2,3,7,-5,-7,2,3,-10,-4,-1,2,6,-2,3,2,4,-5,3,6,-6,5,6,-2,4,7,6,-9,-5,3,-9,-8,-10,9,-4,5,7,10,7,10,-5,-7,10,-7,-6,-3,-5,7,5,-1,10,8,6,-1,-9,6,-1,9,6,-4,-6,7,-9,9,10,-2,-5,-8,-10,6,1,7,3,-1,2,3,-4,9,7,-1,7,-7,-6,5,-3,9,-5,4,-2,8,2,-2,-4,-4,-1,7,-8,2,7,-2,-10,-4,5,2,-3,-1,-4,1,-6,-8,-10,6,-9,-10,6,7,-10,9,-7,5,1,-4,1,-2,2,5,-7,8,7,-10,-1,-9,8,-8,-8,6,9,4,-7,6,-8,-3,-9,-9,-10,-1,10,2,7,4,3,3,-1,-1,-5,10,-7,6,-4,4,8,5,-5,-5,-8,-6,-8,-4,-7,-7,-5,6,10,10,9,-7,1,-4,-10,-9,-5,-1,7,9,-4,6,5,-1,-4,-8,9,9,-7,8,-1,6,-5,8,-2,-6,7,-6,-6,5,10,-4,-9,8,-7,3,-7,-3,-6,4,1,-6,4,9,9,-1,-7,7,-7,4,-5,-1,6,5,-8,-1,1,-7,9,8,-2,-6,-3,7,-10,-5,7,-7,1,-6,3,9,-5,10,2,4,6,-5,5,-10,-2,-9,-10,-2,10,-3,5,6,8,-6,5,-6,-9,9,-10,8,1,-1,-4,5,10,9,-8,5,-3,8,-10,9,3,1,7,7,7,-1,10,-8,-4,6,-2,-9,2,4,-2,-1,-3,10,2,-7,5,3,-4,6,6,1,2,4,7,-6,-3,4,7,-3,1,-1,8,4,3,-1,1,-8,1,-7,-1,9,-7,-7,9,7,-10,8,10,-9,1,5,-1,5,4,4,2,-9,-8,-5,-8,7,-1,-5,7,8,-5,10,-4,10,6,7,-7,8,3,-2,-6,-9,6,-9,-10,-2,8,3,-6,3,-8,9,7,3,-1,-10,-6,5,5,-6,1,-1,10,2,-8,-8,-5,4,-4,-3,1,-3,4,-10,2,-3,-2,1,-8,-7,-7,-3,-4,6,1,7,5,-1,-8,10,-7,-10,-9,4,-3,4,-8,6,-3,3,4,-7,8,9,-1,5,-2,-10,7,8,4,9,8,-5,-10,4,8,2,-1,3,10,3,-4,-2,-8,-8,4,-6,5,-3,2,8,1,6,-10,8,-9,-1,6,2,4,8,-9,10,10,8,3,1,-5,7,-8,-5,-6,7,-8,7,1,1,2,4,7,3,10,-1,1,-10,3,-5,2,2,-3,3,4,3,-7,7,1,-1,2,-5,2,-5,3,-3,-3,4,-3,1,-4,5,-3,5,-2,6,10,8,-9,8,-2,4,7,-3,-8,10,-1,3,-7,2,5,-3,1,1,-6,-1,-2,-6,-4,1,-7,4,-8,-6,3,4,7,-5,1,-8,6,7,-4,-9,6,-10,3,-3,-9,3,6,-4,-5,1,4,4,9,-8,-6,1,8,-5,5,9,-6,8,2,-6,10,4,7,5,-7,6,1,5,7,10,9,-8,6,8,-7,-4,2,-2,-3,-2,4,-6,-5,6,-3,6,8,9,-9], dtype = "int32")#candidate|4096|(720,)|const|int32
call_4094 = relay.TupleGetItem(func_2651_call(relay.reshape(const_4095.astype('float64'), [4, 1, 8]), relay.reshape(const_4096.astype('int32'), [360, 2]), ), 1)
call_4097 = relay.TupleGetItem(func_2655_call(relay.reshape(const_4095.astype('float64'), [4, 1, 8]), relay.reshape(const_4096.astype('int32'), [360, 2]), ), 1)
func_2302_call = mod.get_global_var('func_2302')
func_2305_call = mutated_mod.get_global_var('func_2305')
var_4105 = relay.var("var_4105", dtype = "uint32", shape = ())#candidate|4105|()|var|uint32
var_4106 = relay.var("var_4106", dtype = "uint32", shape = (1716,))#candidate|4106|(1716,)|var|uint32
call_4104 = func_2302_call(relay.reshape(var_4105.astype('uint32'), []), relay.reshape(var_4106.astype('uint32'), [11, 13, 12]), )
call_4107 = func_2302_call(relay.reshape(var_4105.astype('uint32'), []), relay.reshape(var_4106.astype('uint32'), [11, 13, 12]), )
func_2280_call = mod.get_global_var('func_2280')
func_2284_call = mutated_mod.get_global_var('func_2284')
var_4109 = relay.var("var_4109", dtype = "float64", shape = (12, 30))#candidate|4109|(12, 30)|var|float64
call_4108 = relay.TupleGetItem(func_2280_call(relay.reshape(var_4109.astype('float64'), [15, 12, 2]), relay.reshape(var_4109.astype('float64'), [15, 12, 2]), ), 0)
call_4110 = relay.TupleGetItem(func_2284_call(relay.reshape(var_4109.astype('float64'), [15, 12, 2]), relay.reshape(var_4109.astype('float64'), [15, 12, 2]), ), 0)
output = relay.Tuple([call_4085,call_4094,const_4095,const_4096,call_4104,var_4105,var_4106,call_4108,var_4109,])
output2 = relay.Tuple([call_4086,call_4097,const_4095,const_4096,call_4107,var_4105,var_4106,call_4110,var_4109,])
func_4111 = relay.Function([var_4105,var_4106,var_4109,], output)
mod['func_4111'] = func_4111
mod = relay.transform.InferType()(mod)
var_4112 = relay.var("var_4112", dtype = "uint32", shape = ())#candidate|4112|()|var|uint32
var_4113 = relay.var("var_4113", dtype = "uint32", shape = (1716,))#candidate|4113|(1716,)|var|uint32
var_4114 = relay.var("var_4114", dtype = "float64", shape = (12, 30))#candidate|4114|(12, 30)|var|float64
output = func_4111(var_4112,var_4113,var_4114,)
func_4115 = relay.Function([var_4112,var_4113,var_4114,], output)
mutated_mod['func_4115'] = func_4115
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3009_call = mod.get_global_var('func_3009')
func_3010_call = mutated_mod.get_global_var('func_3010')
call_4120 = relay.TupleGetItem(func_3009_call(), 0)
call_4121 = relay.TupleGetItem(func_3010_call(), 0)
var_4122 = relay.var("var_4122", dtype = "float64", shape = (16, 4, 12))#candidate|4122|(16, 4, 12)|var|float64
bop_4123 = relay.equal(call_4120.astype('bool'), var_4122.astype('bool')) # shape=(16, 4, 12)
bop_4126 = relay.equal(call_4121.astype('bool'), var_4122.astype('bool')) # shape=(16, 4, 12)
uop_4135 = relay.asin(var_4122.astype('float32')) # shape=(16, 4, 12)
func_3355_call = mod.get_global_var('func_3355')
func_3359_call = mutated_mod.get_global_var('func_3359')
var_4139 = relay.var("var_4139", dtype = "float64", shape = (640,))#candidate|4139|(640,)|var|float64
var_4140 = relay.var("var_4140", dtype = "int32", shape = (90,))#candidate|4140|(90,)|var|int32
call_4138 = relay.TupleGetItem(func_3355_call(relay.reshape(var_4139.astype('float64'), [16, 4, 10]), relay.reshape(var_4140.astype('int32'), [45, 2]), ), 0)
call_4141 = relay.TupleGetItem(func_3359_call(relay.reshape(var_4139.astype('float64'), [16, 4, 10]), relay.reshape(var_4140.astype('int32'), [45, 2]), ), 0)
output = relay.Tuple([bop_4123,uop_4135,call_4138,var_4139,var_4140,])
output2 = relay.Tuple([bop_4126,uop_4135,call_4141,var_4139,var_4140,])
func_4208 = relay.Function([var_4122,var_4139,var_4140,], output)
mod['func_4208'] = func_4208
mod = relay.transform.InferType()(mod)
mutated_mod['func_4208'] = func_4208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mutated_mod.get_global_var('func_4208')
var_4210 = relay.var("var_4210", dtype = "float64", shape = (16, 4, 12))#candidate|4210|(16, 4, 12)|var|float64
var_4211 = relay.var("var_4211", dtype = "float64", shape = (640,))#candidate|4211|(640,)|var|float64
var_4212 = relay.var("var_4212", dtype = "int32", shape = (90,))#candidate|4212|(90,)|var|int32
call_4209 = func_4208_call(var_4210,var_4211,var_4212,)
output = call_4209
func_4213 = relay.Function([var_4210,var_4211,var_4212,], output)
mutated_mod['func_4213'] = func_4213
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_4302 = func_2762_call()
call_4303 = func_2762_call()
const_4306 = relay.const([[[0.133180],[-4.713336],[-8.246384],[7.228573]],[[-5.216814],[-5.686627],[-0.469314],[-3.507466]],[[-3.793768],[3.927153],[6.246438],[-3.351477]],[[-8.797546],[-1.079387],[-8.353671],[3.913722]],[[6.489100],[-5.761345],[-9.053866],[-5.806351]],[[6.952463],[7.095612],[8.061498],[-0.236102]],[[9.772221],[-7.845181],[4.789322],[-8.263014]],[[-0.902164],[3.294291],[-0.321883],[0.819046]],[[-8.493533],[-2.011527],[9.383333],[-5.699981]],[[1.416387],[3.791056],[1.094054],[-5.277571]],[[0.113946],[7.290269],[-4.285715],[-0.267618]],[[8.564573],[7.187484],[-9.140463],[3.591624]],[[-0.734645],[-8.485005],[-2.577691],[-1.423045]],[[-4.695214],[-0.652505],[-9.141007],[-4.552126]],[[-1.328376],[-7.511779],[-3.435698],[0.703895]],[[-9.872586],[6.919111],[1.176458],[-4.511987]]], dtype = "float64")#candidate|4306|(16, 4, 1)|const|float64
bop_4307 = relay.bitwise_or(call_4302.astype('uint8'), relay.reshape(const_4306.astype('uint8'), relay.shape_of(call_4302))) # shape=(16, 4, 1)
bop_4310 = relay.bitwise_or(call_4303.astype('uint8'), relay.reshape(const_4306.astype('uint8'), relay.shape_of(call_4303))) # shape=(16, 4, 1)
bop_4318 = relay.greater_equal(const_4306.astype('bool'), relay.reshape(call_4302.astype('bool'), relay.shape_of(const_4306))) # shape=(16, 4, 1)
bop_4321 = relay.greater_equal(const_4306.astype('bool'), relay.reshape(call_4303.astype('bool'), relay.shape_of(const_4306))) # shape=(16, 4, 1)
output = relay.Tuple([bop_4307,bop_4318,])
output2 = relay.Tuple([bop_4310,bop_4321,])
func_4323 = relay.Function([], output)
mod['func_4323'] = func_4323
mod = relay.transform.InferType()(mod)
mutated_mod['func_4323'] = func_4323
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4323_call = mutated_mod.get_global_var('func_4323')
call_4324 = func_4323_call()
output = call_4324
func_4325 = relay.Function([], output)
mutated_mod['func_4325'] = func_4325
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4360 = relay.var("var_4360", dtype = "float32", shape = (6, 13, 15))#candidate|4360|(6, 13, 15)|var|float32
uop_4361 = relay.asinh(var_4360.astype('float32')) # shape=(6, 13, 15)
func_4323_call = mod.get_global_var('func_4323')
func_4325_call = mutated_mod.get_global_var('func_4325')
call_4366 = relay.TupleGetItem(func_4323_call(), 0)
call_4367 = relay.TupleGetItem(func_4325_call(), 0)
output = relay.Tuple([uop_4361,call_4366,])
output2 = relay.Tuple([uop_4361,call_4367,])
func_4382 = relay.Function([var_4360,], output)
mod['func_4382'] = func_4382
mod = relay.transform.InferType()(mod)
mutated_mod['func_4382'] = func_4382
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4383 = relay.var("var_4383", dtype = "float32", shape = (6, 13, 15))#candidate|4383|(6, 13, 15)|var|float32
func_4382_call = mutated_mod.get_global_var('func_4382')
call_4384 = func_4382_call(var_4383)
output = call_4384
func_4385 = relay.Function([var_4383], output)
mutated_mod['func_4385'] = func_4385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3792_call = mod.get_global_var('func_3792')
func_3793_call = mutated_mod.get_global_var('func_3793')
call_4392 = func_3792_call()
call_4393 = func_3792_call()
var_4401 = relay.var("var_4401", dtype = "uint32", shape = (12, 10, 9))#candidate|4401|(12, 10, 9)|var|uint32
bop_4402 = relay.bitwise_xor(call_4392.astype('uint8'), relay.reshape(var_4401.astype('uint8'), relay.shape_of(call_4392))) # shape=(12, 10, 9)
bop_4405 = relay.bitwise_xor(call_4393.astype('uint8'), relay.reshape(var_4401.astype('uint8'), relay.shape_of(call_4393))) # shape=(12, 10, 9)
output = bop_4402
output2 = bop_4405
func_4407 = relay.Function([var_4401,], output)
mod['func_4407'] = func_4407
mod = relay.transform.InferType()(mod)
mutated_mod['func_4407'] = func_4407
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4408 = relay.var("var_4408", dtype = "uint32", shape = (12, 10, 9))#candidate|4408|(12, 10, 9)|var|uint32
func_4407_call = mutated_mod.get_global_var('func_4407')
call_4409 = func_4407_call(var_4408)
output = call_4409
func_4410 = relay.Function([var_4408], output)
mutated_mod['func_4410'] = func_4410
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4442 = relay.var("var_4442", dtype = "float32", shape = (9, 3, 6))#candidate|4442|(9, 3, 6)|var|float32
var_4443 = relay.var("var_4443", dtype = "float32", shape = (9, 3, 6))#candidate|4443|(9, 3, 6)|var|float32
bop_4444 = relay.floor_mod(var_4442.astype('float32'), relay.reshape(var_4443.astype('float32'), relay.shape_of(var_4442))) # shape=(9, 3, 6)
bop_4447 = relay.maximum(var_4442.astype('int32'), relay.reshape(var_4443.astype('int32'), relay.shape_of(var_4442))) # shape=(9, 3, 6)
uop_4456 = relay.sin(bop_4444.astype('float32')) # shape=(9, 3, 6)
uop_4459 = relay.sigmoid(uop_4456.astype('float32')) # shape=(9, 3, 6)
func_2961_call = mod.get_global_var('func_2961')
func_2967_call = mutated_mod.get_global_var('func_2967')
var_4464 = relay.var("var_4464", dtype = "uint64", shape = (13, 3))#candidate|4464|(13, 3)|var|uint64
const_4465 = relay.const([1,-4,-2,10,8,9,-4,-9,10,4,6,4,9,-10,9,-8,-9,-5,-1,10,-4,-1,6,3,-3,-9,-4,-4,-2,-6,2,-1,6,3,-5,-9,2,7,-1,5,9,2,6,10,10,10,10,4,-9,7,10,3,5,7,2,1,-5,-7,-9,-10,3,-3,-1,-10,4,4,-3,-3,9,-6,3,2,-10,-8,6,-10,-7,-1], dtype = "uint64")#candidate|4465|(78,)|const|uint64
const_4466 = relay.const([[True,True,True,True,False,True,True,True,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,False,False,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,True,False,False,True,False,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,False,True,True,True,False,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,False,True,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,False,True,True,False,False,False,False,True,True,True,False,False,False,True,True,False,False,False,True,False,False,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,False,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,False,True,False,False,False,False,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,True,True]], dtype = "bool")#candidate|4466|(1, 819)|const|bool
var_4467 = relay.var("var_4467", dtype = "uint64", shape = (8, 52))#candidate|4467|(8, 52)|var|uint64
call_4463 = relay.TupleGetItem(func_2961_call(relay.reshape(var_4464.astype('uint64'), [3, 1, 13]), relay.reshape(const_4465.astype('uint64'), [3, 2, 13]), relay.reshape(const_4466.astype('bool'), [819,]), relay.reshape(var_4467.astype('uint64'), [8, 52]), ), 2)
call_4468 = relay.TupleGetItem(func_2967_call(relay.reshape(var_4464.astype('uint64'), [3, 1, 13]), relay.reshape(const_4465.astype('uint64'), [3, 2, 13]), relay.reshape(const_4466.astype('bool'), [819,]), relay.reshape(var_4467.astype('uint64'), [8, 52]), ), 2)
output = relay.Tuple([bop_4447,uop_4459,call_4463,var_4464,const_4465,const_4466,var_4467,])
output2 = relay.Tuple([bop_4447,uop_4459,call_4468,var_4464,const_4465,const_4466,var_4467,])
func_4473 = relay.Function([var_4442,var_4443,var_4464,var_4467,], output)
mod['func_4473'] = func_4473
mod = relay.transform.InferType()(mod)
var_4474 = relay.var("var_4474", dtype = "float32", shape = (9, 3, 6))#candidate|4474|(9, 3, 6)|var|float32
var_4475 = relay.var("var_4475", dtype = "float32", shape = (9, 3, 6))#candidate|4475|(9, 3, 6)|var|float32
var_4476 = relay.var("var_4476", dtype = "uint64", shape = (13, 3))#candidate|4476|(13, 3)|var|uint64
var_4477 = relay.var("var_4477", dtype = "uint64", shape = (8, 52))#candidate|4477|(8, 52)|var|uint64
output = func_4473(var_4474,var_4475,var_4476,var_4477,)
func_4478 = relay.Function([var_4474,var_4475,var_4476,var_4477,], output)
mutated_mod['func_4478'] = func_4478
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4590 = relay.var("var_4590", dtype = "bool", shape = (12, 6, 4))#candidate|4590|(12, 6, 4)|var|bool
const_4591 = relay.const([[[True,False,True,False],[True,True,True,True],[True,True,True,False],[True,False,False,True],[True,True,False,False],[False,False,False,True]],[[False,True,True,False],[False,True,False,True],[True,True,True,False],[True,True,False,False],[False,True,False,True],[True,False,False,False]],[[False,True,False,False],[True,False,False,False],[True,True,False,True],[False,False,True,True],[True,False,False,False],[True,False,False,True]],[[True,False,False,False],[True,True,False,True],[False,False,True,True],[False,True,True,True],[False,True,False,False],[True,True,False,True]],[[False,False,True,True],[False,False,True,True],[False,True,True,True],[False,True,False,False],[True,False,False,True],[True,True,False,False]],[[True,False,False,False],[False,False,True,False],[False,True,True,False],[True,False,True,True],[False,False,True,False],[True,True,True,False]],[[True,True,True,True],[False,True,True,True],[False,True,False,False],[False,True,False,False],[False,True,True,True],[False,False,True,False]],[[True,False,False,False],[True,True,True,True],[False,False,False,True],[False,True,False,False],[False,False,False,False],[False,False,True,False]],[[True,False,False,True],[False,True,True,True],[True,False,False,False],[True,True,True,False],[True,True,True,True],[False,True,True,True]],[[False,True,True,False],[True,False,False,True],[False,False,False,True],[True,False,False,False],[False,False,True,True],[True,False,True,True]],[[False,False,False,False],[False,False,True,False],[True,True,False,True],[True,False,False,False],[True,False,True,False],[False,True,True,False]],[[False,False,False,True],[False,True,False,False],[False,True,True,False],[True,False,False,False],[True,False,True,True],[False,True,True,True]]], dtype = "bool")#candidate|4591|(12, 6, 4)|const|bool
bop_4592 = relay.logical_and(var_4590.astype('bool'), relay.reshape(const_4591.astype('bool'), relay.shape_of(var_4590))) # shape=(12, 6, 4)
uop_4598 = relay.atanh(const_4591.astype('float64')) # shape=(12, 6, 4)
bop_4605 = relay.floor_divide(const_4591.astype('float32'), relay.reshape(bop_4592.astype('float32'), relay.shape_of(const_4591))) # shape=(12, 6, 4)
uop_4612 = relay.acosh(bop_4605.astype('float64')) # shape=(12, 6, 4)
func_2280_call = mod.get_global_var('func_2280')
func_2284_call = mutated_mod.get_global_var('func_2284')
var_4624 = relay.var("var_4624", dtype = "float64", shape = (360,))#candidate|4624|(360,)|var|float64
call_4623 = relay.TupleGetItem(func_2280_call(relay.reshape(var_4624.astype('float64'), [15, 12, 2]), relay.reshape(var_4624.astype('float64'), [15, 12, 2]), ), 0)
call_4625 = relay.TupleGetItem(func_2284_call(relay.reshape(var_4624.astype('float64'), [15, 12, 2]), relay.reshape(var_4624.astype('float64'), [15, 12, 2]), ), 0)
output = relay.Tuple([uop_4598,uop_4612,call_4623,var_4624,])
output2 = relay.Tuple([uop_4598,uop_4612,call_4625,var_4624,])
func_4628 = relay.Function([var_4590,var_4624,], output)
mod['func_4628'] = func_4628
mod = relay.transform.InferType()(mod)
var_4629 = relay.var("var_4629", dtype = "bool", shape = (12, 6, 4))#candidate|4629|(12, 6, 4)|var|bool
var_4630 = relay.var("var_4630", dtype = "float64", shape = (360,))#candidate|4630|(360,)|var|float64
output = func_4628(var_4629,var_4630,)
func_4631 = relay.Function([var_4629,var_4630,], output)
mutated_mod['func_4631'] = func_4631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mod.get_global_var('func_3775')
func_3776_call = mutated_mod.get_global_var('func_3776')
call_4654 = relay.TupleGetItem(func_3775_call(), 0)
call_4655 = relay.TupleGetItem(func_3776_call(), 0)
uop_4660 = relay.sin(call_4654.astype('float32')) # shape=(12, 10, 9)
uop_4662 = relay.sin(call_4655.astype('float32')) # shape=(12, 10, 9)
func_3672_call = mod.get_global_var('func_3672')
func_3674_call = mutated_mod.get_global_var('func_3674')
var_4668 = relay.var("var_4668", dtype = "float64", shape = (5, 390))#candidate|4668|(5, 390)|var|float64
call_4667 = relay.TupleGetItem(func_3672_call(relay.reshape(var_4668.astype('float64'), [15, 10, 13])), 3)
call_4669 = relay.TupleGetItem(func_3674_call(relay.reshape(var_4668.astype('float64'), [15, 10, 13])), 3)
func_3637_call = mod.get_global_var('func_3637')
func_3639_call = mutated_mod.get_global_var('func_3639')
call_4678 = func_3637_call()
call_4679 = func_3637_call()
output = relay.Tuple([uop_4660,call_4667,var_4668,call_4678,])
output2 = relay.Tuple([uop_4662,call_4669,var_4668,call_4679,])
func_4681 = relay.Function([var_4668,], output)
mod['func_4681'] = func_4681
mod = relay.transform.InferType()(mod)
mutated_mod['func_4681'] = func_4681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4682 = relay.var("var_4682", dtype = "float64", shape = (5, 390))#candidate|4682|(5, 390)|var|float64
func_4681_call = mutated_mod.get_global_var('func_4681')
call_4683 = func_4681_call(var_4682)
output = call_4683
func_4684 = relay.Function([var_4682], output)
mutated_mod['func_4684'] = func_4684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3009_call = mod.get_global_var('func_3009')
func_3010_call = mutated_mod.get_global_var('func_3010')
call_4712 = relay.TupleGetItem(func_3009_call(), 0)
call_4713 = relay.TupleGetItem(func_3010_call(), 0)
func_3775_call = mod.get_global_var('func_3775')
func_3776_call = mutated_mod.get_global_var('func_3776')
call_4737 = relay.TupleGetItem(func_3775_call(), 1)
call_4738 = relay.TupleGetItem(func_3776_call(), 1)
output = relay.Tuple([call_4712,call_4737,])
output2 = relay.Tuple([call_4713,call_4738,])
func_4743 = relay.Function([], output)
mod['func_4743'] = func_4743
mod = relay.transform.InferType()(mod)
mutated_mod['func_4743'] = func_4743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4743_call = mutated_mod.get_global_var('func_4743')
call_4744 = func_4743_call()
output = call_4744
func_4745 = relay.Function([], output)
mutated_mod['func_4745'] = func_4745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3775_call = mod.get_global_var('func_3775')
func_3776_call = mutated_mod.get_global_var('func_3776')
call_4759 = relay.TupleGetItem(func_3775_call(), 1)
call_4760 = relay.TupleGetItem(func_3776_call(), 1)
output = relay.Tuple([call_4759,])
output2 = relay.Tuple([call_4760,])
func_4761 = relay.Function([], output)
mod['func_4761'] = func_4761
mod = relay.transform.InferType()(mod)
output = func_4761()
func_4762 = relay.Function([], output)
mutated_mod['func_4762'] = func_4762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4067_call = mod.get_global_var('func_4067')
func_4068_call = mutated_mod.get_global_var('func_4068')
call_4768 = relay.TupleGetItem(func_4067_call(), 0)
call_4769 = relay.TupleGetItem(func_4068_call(), 0)
output = relay.Tuple([call_4768,])
output2 = relay.Tuple([call_4769,])
func_4796 = relay.Function([], output)
mod['func_4796'] = func_4796
mod = relay.transform.InferType()(mod)
output = func_4796()
func_4797 = relay.Function([], output)
mutated_mod['func_4797'] = func_4797
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4761_call = mod.get_global_var('func_4761')
func_4762_call = mutated_mod.get_global_var('func_4762')
call_4828 = relay.TupleGetItem(func_4761_call(), 0)
call_4829 = relay.TupleGetItem(func_4762_call(), 0)
uop_4840 = relay.atanh(call_4828.astype('float64')) # shape=(12, 10, 9)
uop_4842 = relay.atanh(call_4829.astype('float64')) # shape=(12, 10, 9)
output = relay.Tuple([uop_4840,])
output2 = relay.Tuple([uop_4842,])
func_4845 = relay.Function([], output)
mod['func_4845'] = func_4845
mod = relay.transform.InferType()(mod)
mutated_mod['func_4845'] = func_4845
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4845_call = mutated_mod.get_global_var('func_4845')
call_4846 = func_4845_call()
output = call_4846
func_4847 = relay.Function([], output)
mutated_mod['func_4847'] = func_4847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3009_call = mod.get_global_var('func_3009')
func_3010_call = mutated_mod.get_global_var('func_3010')
call_4877 = relay.TupleGetItem(func_3009_call(), 0)
call_4878 = relay.TupleGetItem(func_3010_call(), 0)
func_4407_call = mod.get_global_var('func_4407')
func_4410_call = mutated_mod.get_global_var('func_4410')
const_4890 = relay.const([-5,-1,-7,4,5,7,9,9,-8,-10,8,8,-10,8,-6,-6,-6,-3,-7,8,3,3,5,-9,8,-9,9,-4,4,-4,1,-5,-10,-9,5,9,3,10,-6,3,10,-10,-9,7,8,-8,-5,7,-9,-2,-4,-2,7,-4,-1,-6,-7,2,-3,-1,-2,2,-2,-5,-5,-7,10,-3,1,9,-4,-5,-1,9,7,7,-9,-9,7,-3,-2,3,-8,-10,-6,5,6,-1,8,-3,9,4,-8,-10,8,-9,-2,6,-1,-2,-7,-6,-8,2,-8,9,-4,5,8,8,9,-8,-2,-2,3,1,-1,-3,-6,5,1,-1,-8,6,4,-2,1,-5,-6,-7,2,-9,7,-2,-8,-6,2,3,-6,6,2,4,-9,8,7,-6,-5,2,8,4,-2,6,-10,3,-7,9,-6,5,-1,3,-8,6,4,5,3,-10,2,8,7,1,10,-7,2,-2,-5,-2,1,-8,8,-9,-5,-6,6,-10,-7,9,10,2,8,-4,8,-7,3,-4,-1,2,1,-2,3,-2,-4,8,6,5,-3,-8,6,-9,-1,10,5,7,-7,5,-2,2,7,-1,9,9,-6,4,2,-10,8,6,-9,1,1,-8,2,-8,-10,-4,-4,1,-1,3,10,-10,-3,-4,-9,-10,1,-3,10,4,10,-8,-2,-8,6,8,-5,2,5,10,-1,4,2,8,9,-1,1,-7,10,8,5,10,6,-7,10,-5,-2,4,6,-6,-4,-8,-8,-8,8,-4,5,4,8,2,-3,-10,6,8,5,-1,-5,-4,1,3,9,6,-3,-5,4,-10,4,3,-3,-6,-9,7,-3,6,4,-7,9,7,2,5,-7,4,-7,5,-9,8,5,9,8,-6,-9,3,4,1,2,-5,-3,2,5,-9,8,2,5,-5,-9,3,-4,7,8,6,-6,-1,-10,-10,-2,-1,8,-6,-7,6,-10,3,7,1,-7,-7,10,3,-3,-8,2,5,-3,3,-2,5,7,-5,9,10,-7,-1,5,8,7,-2,5,8,-8,7,9,-3,1,9,-6,-8,-7,9,-2,-1,10,9,1,-3,-10,1,4,4,-2,7,-5,10,-3,4,-5,-6,8,-10,5,-10,-4,6,6,5,-4,-7,-7,-1,-7,6,1,7,-9,10,10,1,-2,-4,-7,-6,3,-2,-2,1,-1,1,8,1,9,-3,1,5,-1,4,9,-10,5,3,6,-7,8,9,10,-5,-3,-7,2,-10,2,10,-3,-6,-2,-6,-10,5,4,7,-4,-2,1,-1,-3,6,4,9,-4,-8,3,-5,10,4,-6,6,3,6,7,-7,-2,-6,-8,-6,9,9,1,-6,7,-2,8,2,-6,-5,10,3,-6,-8,3,7,1,5,-1,10,-10,-1,-10,10,-3,-1,1,-3,-5,3,7,4,-5,10,10,6,-2,-8,1,-10,-7,5,9,6,1,5,-7,-7,-10,2,7,-9,6,3,9,2,-8,-5,7,2,9,9,8,2,-3,7,-4,-8,6,-10,5,-3,10,-10,7,6,-1,6,1,5,-4,-3,-1,-1,-2,-3,4,2,4,-3,-3,-1,-4,-4,-4,-10,-3,9,5,10,2,6,9,-9,7,-6,-3,-7,-3,-3,-1,-7,7,6,-3,-9,2,-2,1,-6,5,3,8,-4,-2,-9,-1,7,10,10,-2,10,-4,4,4,-4,-1,-7,-6,3,-10,-10,9,-1,-1,-4,-9,4,7,-7,-8,-9,9,-2,-9,-4,5,9,3,3,-10,6,1,1,10,8,2,-8,5,7,-3,2,8,2,-1,5,1,-1,3,-8,-3,-10,-4,-5,6,-3,-6,7,-6,5,-5,1,4,-6,-7,10,3,-4,-8,-5,4,5,3,-5,-2,-6,-3,-1,-10,-5,-3,6,7,-2,8,1,-7,1,-8,-9,-7,5,4,8,-5,1,-10,-4,7,-1,-5,-7,9,-2,-6,-5,-8,6,8,-5,9,-1,-5,5,2,6,-10,-10,3,-6,-5,-4,1,4,-4,-4,-7,1,1,3,-3,1,-4,-2,4,-7,-9,1,-1,-1,8,-9,10,6,-7,7,9,-3,10,9,-3,5,9,2,-5,-6,-8,-7,-6,-2,-3,3,6,5,3,-1,10,8,4,-9,3,-9,2,-1,-10,-1,3,-4,-4,-6,5,-5,3,-4,3,5,1,-1,1,-1,-7,3,8,9,-8,-9,2,8,7,-4,7,8,-5,-3,1,7,-8,-5,2,10,-9,-3,-3,10,-4,2,-6,-1,9,9,-10,7,-9,-6,-8,-10,-7,2,5,2,4,3,4,3,10,3,-10,-9,5,-1,4,-2,6,1,-3,5,4,-9,3,-4,-6,2,7,7,9,-7,-9,1,4,-1,4,-6,3,1,-1,-9,-9,-3,4,-2,-5,-5,-9,-4,-10,-10,10,-7,5,-8,-10,-3,8,7,5,-5,8,7,-8,-8,5,-5,6,-5,-7,-7,-10,5,-6,1,2,2,-6,7,9,2,-3,-8,-8,-2,-7,-1,-9,6,1,-5,-3,-2,7,3,-5,1,-6,9,-1,9,9,-5,-6,-4,-8,9,7,10,-1,1,2,5,10,-9,6,8,-8,6,4,3,8,-1,3,2,-4,9,-6,3,-10,-6,10,4,9,-4,-9,-4,8,3,-7,-5,-9,-9,1,-10,4,-9,-3,4,2,-2,-6,-9,4,-6,-8,-3,7,1,-6,3,8,6,-7,-3,8,-2,-4,9,-3,-8,-5,-6,-7,-4,-8,2,-9,9,-1,-4,8,3,7,9,-6,10,9,6,5,-8,-7,2,1,1,-4,10,3,5,7,1,-2,-7,-7,7,-4,-6,7,6,-9,-9,2,-6,-5,6,-4,7,5,9,10,-5,-2,7,1,7], dtype = "uint32")#candidate|4890|(1080,)|const|uint32
call_4889 = func_4407_call(relay.reshape(const_4890.astype('uint32'), [12, 10, 9]))
call_4891 = func_4407_call(relay.reshape(const_4890.astype('uint32'), [12, 10, 9]))
func_963_call = mod.get_global_var('func_963')
func_965_call = mutated_mod.get_global_var('func_965')
var_4903 = relay.var("var_4903", dtype = "float32", shape = (147,))#candidate|4903|(147,)|var|float32
call_4902 = relay.TupleGetItem(func_963_call(relay.reshape(var_4903.astype('float32'), [7, 7, 3])), 0)
call_4904 = relay.TupleGetItem(func_965_call(relay.reshape(var_4903.astype('float32'), [7, 7, 3])), 0)
func_914_call = mod.get_global_var('func_914')
func_919_call = mutated_mod.get_global_var('func_919')
var_4907 = relay.var("var_4907", dtype = "bool", shape = (273, 3))#candidate|4907|(273, 3)|var|bool
var_4908 = relay.var("var_4908", dtype = "float64", shape = (330,))#candidate|4908|(330,)|var|float64
const_4909 = relay.const([-4.603114,3.597367,5.061929,-0.800267,4.082140,-3.642564,7.573223,9.633860,8.671510,0.370673,0.385106,6.185409,6.142334,-4.031363,0.365476,-3.974868,1.998622,-5.351619,-7.676623,1.056539,2.127654,-9.081234,-5.315599,2.116431,-7.765677,0.680414,-8.492886,1.917220,9.993058,-5.726934,1.985386,-4.124956,-0.479085,5.753387,-6.252167,4.803421,2.544260,-7.291908,5.997391,6.131129,-7.759811,1.063786,6.799264,-6.788321,-0.735280,-6.306730,-1.335928,-5.232038,4.339861,5.433738,4.173097,0.385011,6.141588,-2.914901,0.599649,-5.324147,-3.581817,-8.802116,-8.114158,-7.841499,-5.371981,2.187067,-3.577231,6.279738,8.463764,6.793903,4.996895,8.102488,-7.838095,1.691417,-0.754304,8.471777,0.059363,-2.359136,-8.906059,-0.440166,4.884662,6.165449,-2.807056,-9.355239,-4.565525,-2.134604,-3.993053,-6.756789,5.625591,7.928682,7.826091,-9.068394,-1.196563,-8.740946,3.459030,7.495100,-4.008468,-1.302796,-4.912539,5.343906,-2.255197,-0.127639,8.617484,4.790175,3.759755,-6.742123,5.881959,1.556247,-9.379179,5.104038,6.650722,-5.928028,0.759253,-8.628446,6.017478,-8.780431,0.733502,4.888339,5.215542,6.416572,6.244104,6.075830,-0.329099,-4.254148,6.209103,-3.846113,3.357655,-3.485645,-8.720302,-4.447550,-5.206489,5.174513,6.160840,5.266769,-7.726605,6.687862,-2.876406,-8.980723,-8.999302,4.062416,-3.565044,-5.829584,3.707880,9.235679,7.540821,3.830035,-2.825892,3.060040,5.865090,8.266217,2.459708,6.723185,9.456766,-6.699189,6.568711,8.863094,8.252482,2.174737,3.198211,-5.086704,-5.433392,-1.513866,3.935773,-2.001591,-1.447861,-0.814585,6.439121,-6.985961,3.422195,-0.975804,-1.249710,0.227435,6.962939,-1.547370,3.365984,4.549569,3.735725,-8.736889,6.671620,1.544251,-2.756177,9.747058,-4.199204,4.096982,-5.306198,-1.591756,7.839613,-6.924999,-7.267663,8.755723,-1.219876,2.862206,4.266381,-3.333730,-0.181641,-3.338901,2.782047,-0.395718,5.167744,3.020291,3.274569,9.522860,6.329995,8.571942,-8.610895,3.781332,0.006536,-4.097181,8.005943,1.066220,9.783994,-5.501888,3.445511,-3.637592,-2.759625,-1.605933,9.781429,8.515622,-5.930870,-9.800594,3.370411,2.984615,-6.221300,0.836084,-3.827606,5.539468,6.716092,-1.249237,3.119647,1.622291,-2.204001,4.475576,4.383741,6.846110,-7.903200,2.379385,5.317475,-6.478402,-9.712871,0.617211,1.785912,-8.612276,8.691763,2.756959,7.763844,-1.603299,1.812659,0.536652,-5.656401,-4.568273,-9.318204,0.629565,-8.088272,1.157551,1.726324,3.763726,-3.816735,9.445049,-5.053290,-8.683390,-1.768536,0.431539,-1.463489,-3.842737,0.095169,9.305731,-6.605575,-3.231591,0.074151,-5.618417,-2.013670,3.621701,6.867493,-6.985091,5.686891,-5.730876,-2.216119,2.991617,-3.943727,3.528797,-9.240660,-8.226026,3.744802,7.227060,-0.770937,-9.426090,9.706436,3.887873,-8.587446,-6.336408,-7.361823,1.573086,6.330334,-6.148202,2.652778,7.440947,-0.555760,-9.233752,-9.158597,-4.279021,9.045657,-9.916165,-7.257784,-6.795644,0.399118,9.984403,7.908267,-7.366372,4.666661,-7.487998,3.795402,8.983146,3.995095,0.026692,9.491608,6.331493,-8.704402,-7.605838,4.487216,-4.137167,4.169903,5.676104,-5.326256,5.064091,-7.523796,-0.786493,-4.168343,3.088760,-8.663224,5.664355,7.312534,-2.869023,-0.303144,-1.069794,9.327189,2.839376,-1.528951,1.618189,-0.311856,5.130000,0.536342,-8.615430,1.994813,5.911595,6.887974,2.195724,2.317301,-1.617329,-8.945642,-0.844168,8.395415,9.211384,-8.405719,3.562286,7.737249,5.175495,-0.806672,-7.641953,6.870885,4.451638,2.393468,8.783678,0.590213,-6.922907,8.401977,2.760118,-1.306762,-7.595082,-1.931657,-4.798729,-9.516812,-1.301130,0.299448,-4.274996,-1.483759,8.347825,8.751488,3.636868,5.733197,-1.960780,-0.029252,6.319895,-5.846510,2.041798,3.852731,0.676362,2.437473,2.325115,-0.888356,6.071781,3.481149,-1.915724,-9.244676,9.163939,-7.916567,-7.316007,-3.775604,3.197080,7.767290,6.769403,-1.912140,5.211862,-7.110671,3.108009,-6.642748,4.111130,3.279230,-6.999650,5.574952,1.133545,-9.406212,-3.683218,-3.154939,4.855794,-2.513697,-5.448837,6.307273,-8.767262,-5.647805,4.778724,2.606803,0.655108,-9.726419,-1.527403,1.630560,9.609316,9.804422,-3.763867,-9.065723,8.419324,-1.517962,8.881292,3.374872,5.969906,9.981946,9.625203,-3.237736,-8.348106,-8.293500,-5.563640,-2.252677,4.494503,-6.380174,0.377077,-4.649669,2.373697,9.498434,-9.980544,7.232460,-1.771317,-8.270084,2.260135,-8.578251,-2.733239,-4.273595,3.624531,-6.679235,-5.260287,-4.865641,1.177954,-7.326842,-6.351471,-4.595534,8.958816,-8.497328,-2.577655,7.931626,2.561634,1.641664,-7.988761,8.206842,0.970568,7.072615,-0.070485,2.083937,-0.905218,-3.052960,3.335123,8.424127,-8.332402,2.917273,5.307387,-3.963376,-7.826658,-1.457943,3.103981,-7.609778,4.667564,-5.981922,-8.872981,-8.525774,-7.957824,4.516607,0.112119,-4.734936,-3.506991,-2.674466,-1.946781,3.507672,3.809371,7.833552,1.865514,2.501453,5.750465,-1.458322,8.959221,-6.845113,0.179998,-3.613037,0.101470,3.789512,-6.680890,1.455234,-2.463875,9.042536,-0.623322,6.483270,1.462960,-3.786147,-4.359342,-7.842137,3.479690,5.245838,-4.573383,9.874360,-6.172094,3.525787,9.424431,4.813510,5.333764,2.559058,-8.907806,2.630638,7.730440,-4.234657,-3.472271,1.172912,-1.286937,3.400472,-3.578092,-6.376243,1.652651,4.805308,-4.881065,-6.524670,-4.041165,4.906993,-4.555863,-9.144799,-4.362581,-9.801353,6.426376,8.563820,-1.542548,-0.523163,2.054893,-8.302371,-3.136819,2.387227,-9.553358,9.142306,1.042941,4.527708,5.988211,2.762141,5.947054,5.752221,-5.610284,-8.857423,9.673227,4.765291,1.930841,3.010688,-1.400146,-1.510331,-1.802129,4.517263,-5.253373,-9.080184,-7.500159,6.075052,0.873355,-7.667248,8.540308,-1.462000,7.707967,-6.744803,6.006597,-4.468813], dtype = "float32")#candidate|4909|(585,)|const|float32
call_4906 = relay.TupleGetItem(func_914_call(relay.reshape(var_4907.astype('bool'), [819,]), relay.reshape(var_4908.astype('float64'), [330,]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), ), 10)
call_4910 = relay.TupleGetItem(func_919_call(relay.reshape(var_4907.astype('bool'), [819,]), relay.reshape(var_4908.astype('float64'), [330,]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), ), 10)
func_914_call = mod.get_global_var('func_914')
func_919_call = mutated_mod.get_global_var('func_919')
call_4913 = relay.TupleGetItem(func_914_call(relay.reshape(var_4907.astype('bool'), [819,]), relay.reshape(var_4908.astype('float64'), [330,]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), ), 1)
call_4914 = relay.TupleGetItem(func_919_call(relay.reshape(var_4907.astype('bool'), [819,]), relay.reshape(var_4908.astype('float64'), [330,]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), relay.reshape(const_4909.astype('float32'), [13, 3, 15]), ), 1)
bop_4919 = relay.floor_mod(var_4907.astype('float64'), relay.reshape(call_4913.astype('float64'), relay.shape_of(var_4907))) # shape=(273, 3)
bop_4922 = relay.floor_mod(var_4907.astype('float64'), relay.reshape(call_4914.astype('float64'), relay.shape_of(var_4907))) # shape=(273, 3)
func_4018_call = mod.get_global_var('func_4018')
func_4022_call = mutated_mod.get_global_var('func_4022')
var_4928 = relay.var("var_4928", dtype = "float64", shape = (832,))#candidate|4928|(832,)|var|float64
call_4927 = relay.TupleGetItem(func_4018_call(relay.reshape(var_4928.astype('float64'), [16, 4, 13]), relay.reshape(var_4928.astype('float64'), [16, 4, 13]), ), 1)
call_4929 = relay.TupleGetItem(func_4022_call(relay.reshape(var_4928.astype('float64'), [16, 4, 13]), relay.reshape(var_4928.astype('float64'), [16, 4, 13]), ), 1)
func_1314_call = mod.get_global_var('func_1314')
func_1317_call = mutated_mod.get_global_var('func_1317')
var_4951 = relay.var("var_4951", dtype = "uint8", shape = ())#candidate|4951|()|var|uint8
call_4950 = relay.TupleGetItem(func_1314_call(relay.reshape(var_4951.astype('uint8'), [])), 3)
call_4952 = relay.TupleGetItem(func_1317_call(relay.reshape(var_4951.astype('uint8'), [])), 3)
bop_4953 = relay.add(call_4913.astype('int8'), relay.reshape(call_4950.astype('int8'), relay.shape_of(call_4913))) # shape=(819,)
bop_4956 = relay.add(call_4914.astype('int8'), relay.reshape(call_4952.astype('int8'), relay.shape_of(call_4914))) # shape=(819,)
bop_4957 = relay.bitwise_xor(var_4903.astype('uint32'), relay.reshape(call_4902.astype('uint32'), relay.shape_of(var_4903))) # shape=(147,)
bop_4960 = relay.bitwise_xor(var_4903.astype('uint32'), relay.reshape(call_4904.astype('uint32'), relay.shape_of(var_4903))) # shape=(147,)
bop_4961 = relay.add(const_4890.astype('uint16'), var_4951.astype('uint16')) # shape=(1080,)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_4965 = relay.TupleGetItem(func_4743_call(), 0)
call_4966 = relay.TupleGetItem(func_4745_call(), 0)
output = relay.Tuple([call_4877,call_4889,call_4906,var_4908,const_4909,bop_4919,call_4927,var_4928,bop_4953,bop_4957,bop_4961,call_4965,])
output2 = relay.Tuple([call_4878,call_4891,call_4910,var_4908,const_4909,bop_4922,call_4929,var_4928,bop_4956,bop_4960,bop_4961,call_4966,])
func_4968 = relay.Function([var_4903,var_4907,var_4908,var_4928,var_4951,], output)
mod['func_4968'] = func_4968
mod = relay.transform.InferType()(mod)
mutated_mod['func_4968'] = func_4968
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4968_call = mutated_mod.get_global_var('func_4968')
var_4970 = relay.var("var_4970", dtype = "float32", shape = (147,))#candidate|4970|(147,)|var|float32
var_4971 = relay.var("var_4971", dtype = "bool", shape = (273, 3))#candidate|4971|(273, 3)|var|bool
var_4972 = relay.var("var_4972", dtype = "float64", shape = (330,))#candidate|4972|(330,)|var|float64
var_4973 = relay.var("var_4973", dtype = "float64", shape = (832,))#candidate|4973|(832,)|var|float64
var_4974 = relay.var("var_4974", dtype = "uint8", shape = ())#candidate|4974|()|var|uint8
call_4969 = func_4968_call(var_4970,var_4971,var_4972,var_4973,var_4974,)
output = call_4969
func_4975 = relay.Function([var_4970,var_4971,var_4972,var_4973,var_4974,], output)
mutated_mod['func_4975'] = func_4975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3792_call = mod.get_global_var('func_3792')
func_3793_call = mutated_mod.get_global_var('func_3793')
call_4988 = func_3792_call()
call_4989 = func_3792_call()
func_4968_call = mod.get_global_var('func_4968')
func_4975_call = mutated_mod.get_global_var('func_4975')
var_4996 = relay.var("var_4996", dtype = "float32", shape = (147,))#candidate|4996|(147,)|var|float32
const_4997 = relay.const([[False,True,True],[False,True,False],[False,False,True],[True,False,True],[False,False,False],[False,False,False],[True,True,False],[True,True,True],[False,True,False],[True,True,True],[False,True,False],[False,True,True],[False,True,True],[True,False,True],[False,True,True],[False,True,False],[False,False,True],[False,False,True],[True,False,False],[True,True,True],[False,False,False],[False,False,True],[False,False,False],[True,False,True],[True,False,False],[False,True,True],[False,True,False],[False,False,False],[True,True,False],[True,True,False],[False,True,False],[False,False,False],[True,False,False],[True,True,False],[False,False,True],[False,True,False],[False,True,True],[False,True,True],[False,False,True],[False,True,False],[False,True,True],[False,True,True],[False,False,True],[True,False,True],[True,False,True],[False,True,False],[False,True,False],[False,True,True],[True,True,False],[False,True,True],[False,False,True],[False,False,False],[True,True,True],[True,False,True],[False,True,True],[True,False,False],[False,False,True],[False,False,False],[True,False,True],[True,False,True],[True,True,True],[False,True,True],[False,False,False],[True,True,False],[False,True,False],[False,True,False],[False,True,False],[False,True,True],[False,False,True],[False,False,True],[True,True,False],[False,True,True],[True,True,False],[False,True,True],[False,True,True],[False,True,False],[False,False,True],[True,False,False],[False,False,False],[True,False,False],[False,True,True],[True,True,False],[False,True,False],[False,True,True],[False,True,False],[True,False,False],[True,False,False],[False,True,False],[False,True,False],[False,False,True],[True,True,False],[False,False,False],[True,False,True],[True,True,False],[False,True,True],[False,False,True],[False,True,False],[False,True,True],[False,True,True],[True,True,True],[False,False,False],[False,True,False],[False,False,True],[True,True,False],[True,True,True],[True,True,True],[False,False,False],[False,False,True],[False,True,False],[True,False,True],[False,False,False],[True,False,True],[True,True,True],[False,False,False],[False,False,True],[True,True,False],[False,True,False],[False,False,True],[True,False,False],[True,True,False],[True,True,False],[True,False,False],[False,False,True],[True,False,False],[True,True,False],[False,False,True],[False,True,False],[True,True,False],[False,True,False],[False,False,True],[False,True,True],[False,False,True],[False,False,True],[False,True,False],[False,False,True],[False,False,True],[True,True,False],[True,False,False],[False,False,True],[False,False,True],[False,False,True],[True,False,True],[False,False,False],[False,False,True],[False,False,False],[True,False,False],[False,True,True],[True,True,True],[True,True,True],[False,True,True],[True,True,True],[False,False,True],[False,True,False],[False,True,False],[True,True,True],[True,False,True],[False,False,True],[True,True,False],[True,False,True],[False,False,False],[False,False,False],[True,False,False],[True,False,True],[True,False,False],[True,False,True],[False,True,True],[False,True,False],[True,True,True],[True,False,False],[False,False,False],[False,False,False],[False,False,True],[True,True,True],[False,False,False],[True,True,False],[False,False,True],[False,False,True],[False,True,False],[True,False,False],[True,False,False],[False,False,True],[False,True,True],[True,False,False],[True,False,False],[True,True,True],[True,False,True],[False,False,True],[True,False,False],[True,True,False],[True,True,False],[False,True,True],[True,True,False],[False,True,False],[False,False,False],[False,True,False],[True,False,False],[True,False,False],[False,False,False],[True,True,True],[True,True,False],[False,True,True],[True,False,True],[True,False,False],[True,False,False],[True,False,True],[True,True,True],[True,False,True],[True,True,True],[True,False,True],[True,True,False],[True,True,True],[True,False,True],[False,True,True],[False,False,True],[False,False,True],[True,True,False],[False,True,True],[True,False,False],[True,False,False],[False,True,True],[False,False,True],[True,True,True],[False,True,True],[True,True,True],[False,True,True],[True,False,True],[True,False,False],[False,False,False],[False,True,False],[False,True,True],[False,True,False],[True,False,True],[False,False,True],[True,True,False],[True,True,False],[False,False,False],[True,True,True],[True,False,True],[False,False,False],[False,True,True],[False,True,False],[False,False,False],[True,False,False],[False,False,True],[True,True,False],[True,True,False],[True,True,True],[False,False,True],[True,False,False],[True,True,True],[False,True,False],[False,True,False],[False,False,False],[False,True,False],[True,False,True],[True,True,True],[True,False,False],[True,True,False],[False,False,True],[False,False,False],[True,False,True],[True,True,False],[True,True,False],[False,False,True],[False,True,True],[False,True,False],[True,False,True],[True,True,False],[True,False,False],[False,False,False],[False,False,True],[True,True,False],[True,True,True]], dtype = "bool")#candidate|4997|(273, 3)|const|bool
const_4998 = relay.const([[-6.518140,-1.571967],[-8.150336,-3.347375],[-4.252421,4.478611],[-8.416351,3.504183],[6.872601,4.808589],[-0.346937,1.865601],[8.068179,-6.351737],[1.138126,-6.375123],[-9.093050,0.055942],[-8.767726,4.855957],[7.813827,8.382166],[-8.883840,9.950787],[6.081642,-5.975550],[-4.901705,8.643871],[-8.833998,5.816830],[-8.027835,2.454344],[-5.371398,4.319252],[-8.550798,-4.647134],[8.880827,-6.047980],[-4.244931,-9.979665],[-6.864265,-0.669763],[-5.054038,2.128300],[5.976413,-0.516503],[-6.077082,-3.837534],[-1.067045,9.891833],[-8.464804,8.195032],[-8.276205,-0.766641],[7.718697,-5.630198],[3.328208,-4.032462],[-7.845379,-0.382818],[-4.469394,-2.830889],[-3.852458,4.607224],[-4.840036,-0.326657],[-5.786896,3.348955],[7.161258,-9.132904],[-6.088802,-6.248657],[8.807374,3.910281],[-9.581394,9.900333],[-8.697958,0.443953],[-4.509036,2.282915],[-0.422127,-1.568460],[5.179658,3.192982],[4.654170,7.911482],[-8.462657,3.778255],[-7.470066,-3.979079],[-2.236112,4.177593],[2.051173,5.148206],[-4.895055,-3.705631],[-7.329235,9.453964],[-9.914217,-0.429430],[-0.063243,9.540258],[-5.683270,-5.019068],[7.585247,0.305837],[-7.239684,-2.483455],[-1.392686,-1.183944],[2.264913,5.597097],[0.405497,8.229588],[5.294320,9.390702],[-3.477741,-0.032033],[7.525158,5.814165],[2.478740,-4.410780],[-0.965868,1.882504],[-4.407763,9.438832],[6.995051,-4.107061],[8.349665,-2.641139],[9.621123,0.886848],[0.565979,-7.161356],[-0.588399,1.578269],[4.243388,-9.652656],[7.129434,-3.778527],[6.351585,9.291559],[-0.841252,7.587395],[9.523031,-8.571998],[5.163263,-6.499645],[9.148542,7.054772],[7.270896,-2.221052],[-3.662540,-1.891534],[-0.182414,0.947052],[-2.584210,-2.602918],[-1.598532,-9.958976],[-1.048580,9.845233],[-1.959649,-6.305582],[-7.414232,-8.879520],[-1.702451,-0.199963],[4.232446,-9.030688],[6.215870,4.242229],[-1.659001,-0.929801],[1.154576,3.993132],[5.852147,7.751618],[-2.875302,-9.153337],[4.905309,-6.156151],[2.239519,-6.180771],[0.868107,-3.166146],[-9.740136,-8.182371],[-9.621998,-5.023883],[-9.188624,0.905692],[-3.783311,4.881420],[-5.616847,4.800124],[-2.893886,5.484657],[1.264599,-8.442262],[9.718314,3.572799],[-0.696728,-4.768447],[1.302936,-4.366447],[-9.871817,9.196070],[-9.243314,-6.253581],[-1.187546,-0.068237],[3.965660,-0.466903],[4.360044,-4.613970],[-4.700923,3.649336],[1.532607,9.911462],[-9.559232,-5.824012],[6.878838,4.380356],[6.706307,-5.207553],[2.802974,-4.225281],[-8.983725,5.308653],[-6.283267,-3.233919],[-4.015476,1.165767],[-9.124352,-2.089795],[1.321804,7.065868],[-8.549000,-2.258331],[-7.568087,-7.996253],[-6.562295,1.167610],[9.818356,-0.139317],[-0.380601,-2.044523],[-3.703258,-8.202459],[-4.598752,7.474772],[-1.876628,-9.829059],[8.975791,-5.693418],[6.228474,-8.414716],[2.869298,0.058922],[-0.928724,-6.650928],[-3.751806,0.520938],[4.407270,7.549666],[-7.652860,3.833762],[-7.582125,-2.159688],[-0.037704,0.068232],[6.266000,2.741722],[8.398944,7.798857],[7.751531,-9.988959],[7.591536,-9.516593],[-6.435783,-1.020172],[9.483283,2.077833],[-1.659055,0.501438],[-1.703862,-3.694520],[-6.430671,-7.157293],[-5.360980,-1.939398],[-6.865094,-1.337618],[-8.383960,-6.855724],[-5.744830,-3.281287],[-8.963559,6.985246],[7.761552,3.864408],[-8.243001,2.935096],[-4.290732,-5.877594],[2.781913,-9.125300],[-0.219119,5.197135],[1.745636,5.281395],[5.181827,4.979482],[1.087584,-5.701174],[-3.320946,-4.350267],[2.648840,0.801390],[9.578127,0.870206],[-4.303336,-0.149517],[-8.675198,-5.522257],[2.767288,0.102449],[4.085555,-1.448256]], dtype = "float64")#candidate|4998|(165, 2)|const|float64
var_4999 = relay.var("var_4999", dtype = "float64", shape = (832,))#candidate|4999|(832,)|var|float64
const_5000 = relay.const(1, dtype = "uint8")#candidate|5000|()|const|uint8
call_4995 = relay.TupleGetItem(func_4968_call(relay.reshape(var_4996.astype('float32'), [147,]), relay.reshape(const_4997.astype('bool'), [273, 3]), relay.reshape(const_4998.astype('float64'), [330,]), relay.reshape(var_4999.astype('float64'), [832,]), relay.reshape(const_5000.astype('uint8'), []), ), 11)
call_5001 = relay.TupleGetItem(func_4975_call(relay.reshape(var_4996.astype('float32'), [147,]), relay.reshape(const_4997.astype('bool'), [273, 3]), relay.reshape(const_4998.astype('float64'), [330,]), relay.reshape(var_4999.astype('float64'), [832,]), relay.reshape(const_5000.astype('uint8'), []), ), 11)
output = relay.Tuple([call_4988,call_4995,var_4996,const_4997,const_4998,var_4999,const_5000,])
output2 = relay.Tuple([call_4989,call_5001,var_4996,const_4997,const_4998,var_4999,const_5000,])
func_5003 = relay.Function([var_4996,var_4999,], output)
mod['func_5003'] = func_5003
mod = relay.transform.InferType()(mod)
mutated_mod['func_5003'] = func_5003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5003_call = mutated_mod.get_global_var('func_5003')
var_5005 = relay.var("var_5005", dtype = "float32", shape = (147,))#candidate|5005|(147,)|var|float32
var_5006 = relay.var("var_5006", dtype = "float64", shape = (832,))#candidate|5006|(832,)|var|float64
call_5004 = func_5003_call(var_5005,var_5006,)
output = call_5004
func_5007 = relay.Function([var_5005,var_5006,], output)
mutated_mod['func_5007'] = func_5007
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4845_call = mod.get_global_var('func_4845')
func_4847_call = mutated_mod.get_global_var('func_4847')
call_5012 = relay.TupleGetItem(func_4845_call(), 0)
call_5013 = relay.TupleGetItem(func_4847_call(), 0)
func_4382_call = mod.get_global_var('func_4382')
func_4385_call = mutated_mod.get_global_var('func_4385')
const_5020 = relay.const([-2.453192,5.284243,7.586608,-0.548526,7.321293,-3.372635,-0.524800,6.495975,0.894892,9.292801,-9.005632,-0.434274,0.131860,7.663257,6.924608,1.363188,2.279913,2.025867,-6.510688,-4.686486,0.904677,0.081478,-9.864889,5.699544,7.694099,-4.002529,-6.296838,5.004508,8.743935,-9.473726,3.619300,9.475736,5.347158,-0.381652,-6.390937,8.638416,2.893195,5.626866,7.612550,-5.582408,5.872844,-5.864388,8.025811,1.608415,-9.399967,-2.078601,-1.438490,-8.437115,-6.569232,8.144593,-4.798032,-0.725085,1.010057,7.813415,-1.722822,8.641084,-3.954603,-8.669674,2.457624,-3.420676,7.429310,4.708157,-7.418890,7.928185,-8.227874,6.475321,2.115970,0.397063,3.053888,2.873556,-9.402338,-0.394918,-2.676575,-4.309164,-9.123566,0.736801,8.065706,1.664687,5.339818,-5.814422,2.700536,-9.347192,-4.435506,7.544048,-8.420169,2.317546,6.681055,5.682694,-7.303894,2.830252,-0.263874,5.245301,-3.898090,-9.939617,0.211218,0.950691,-5.460138,-5.069482,4.857579,3.033254,-8.240679,-5.521309,-6.720102,-8.194953,-1.953693,5.205589,-0.970087,-1.098032,-7.398922,-5.109705,-2.072494,-6.308607,2.434671,9.447547,4.281907,-9.192485,4.674950,2.033371,-4.026098,7.322007,-7.531054,-1.638179,4.169246,4.377531,7.834776,3.082467,2.756924,-8.495594,-5.321482,-2.478515,-2.384345,-1.475150,7.553011,0.127922,4.771927,-0.364925,-7.335842,-1.947625,-3.352467,6.940546,-8.352447,9.363350,-8.964180,-1.674099,8.817940,-6.714216,-6.151889,3.030868,7.151311,2.531504,2.731735,-1.049992,-0.473112,5.860695,-4.754059,-2.915081,-8.690382,-6.993621,-6.114393,1.049513,0.611532,1.370682,-0.841394,-4.369040,-0.316964,-6.108428,5.471974,7.947755,-7.604452,-9.024420,1.086744,4.598073,-7.367246,-0.626641,-8.070322,-6.043092,-4.563378,4.791636,3.375303,-4.252503,-1.923191,9.498075,7.657121,8.827356,-9.516370,-3.532347,9.662481,2.228804,3.219597,-3.798871,1.704473,-6.981512,-8.919461,8.800875,6.028670,1.096372,-4.799547,6.804477,1.822817,2.133982,4.185878,8.605366,4.270989,-1.789054,1.924648,1.107537,-7.990692,-7.258715,3.372906,-7.906046,3.832788,-0.837209,-9.417304,4.657764,8.230196,9.120451,-2.523320,8.572897,1.507857,-6.311997,-7.425526,-3.279261,5.635600,4.581172,-4.998427,2.910107,-2.535848,2.129962,-0.293746,-0.320877,-5.759233,-8.839843,0.661309,-3.894237,5.040021,5.125679,-6.411104,-6.591554,-0.602294,6.939195,5.540544,-1.645439,-3.188605,1.399012,-9.811632,-1.053131,6.574287,9.678439,-9.669811,-8.813649,-8.100068,4.690503,6.448808,9.301515,-5.018511,-0.334249,3.247405,5.973221,-4.773452,-0.322749,-3.500683,8.767173,1.412721,-0.598652,1.168946,-8.215959,-5.022310,-2.365056,9.569028,3.878985,-3.619249,-2.064193,-6.010190,-3.143807,-3.570777,3.151236,8.941221,-3.506390,6.561190,7.024069,1.920777,7.769446,1.530328,1.789810,8.621636,-1.401619,-2.845255,7.676378,-2.904814,-1.766789,1.406092,-4.361469,-7.884647,5.635119,9.298813,-1.143777,-7.895472,7.090483,-3.852968,9.179192,1.897668,8.134236,-4.078827,2.799278,-2.140350,9.145882,2.973088,9.430662,-8.129113,-2.386112,0.908390,1.142671,-0.972852,4.859664,4.381763,-1.421614,4.818981,9.005447,-9.777720,-3.133044,-2.970948,-5.558966,5.191273,0.851061,9.450276,-0.921887,0.161197,-9.050176,-8.382441,-0.134822,-6.274216,-4.183076,-4.960398,8.751486,-9.868217,-9.358498,3.406932,4.025556,-6.577696,6.271942,-2.155433,-9.505019,9.948203,9.888806,-4.610693,7.293663,-6.741739,-9.604412,6.557342,5.277207,-4.213494,-5.605299,1.931950,-6.744254,8.094928,9.340740,0.965528,4.811735,-2.910695,-4.795194,-7.928205,-1.303262,-5.090732,6.550594,-9.863926,0.076767,-7.775391,2.751945,9.134549,6.282097,3.757978,-9.483832,-2.879998,7.415624,-6.517033,-6.998540,7.914438,4.525183,0.825009,-7.543324,-1.679214,-1.473133,9.500355,-3.739298,-9.075831,7.958978,-6.471564,-0.903700,4.553025,0.824325,-2.939284,-7.936135,-0.616082,6.209558,8.650569,-6.652083,1.561146,-3.446015,-9.049104,-6.601583,6.712820,-3.033302,2.457574,-1.403919,-8.463446,6.113932,8.966596,-2.514480,6.921212,-9.882603,3.264864,-9.046506,3.312583,-6.218499,7.229993,-4.643961,-0.070761,-9.021079,-1.644334,5.478725,4.881383,8.585407,-6.573761,-9.769417,5.291534,-8.194127,5.213707,6.323354,-8.623892,-1.425116,-8.103630,-7.743920,5.397276,4.969376,1.460900,-8.835866,3.846387,-1.813307,-9.465056,2.388914,0.385678,-1.132029,3.872364,9.162183,6.556767,6.838350,7.920139,5.939165,6.430266,-9.806997,5.756832,8.203085,-7.525593,-7.868659,-6.645053,-8.889194,-6.852770,9.935022,-0.468784,2.133414,-9.127700,-3.028029,-6.544718,8.714995,-7.985080,-9.923047,-1.764628,-6.157185,0.697990,5.434748,-4.443326,4.273875,7.423226,-1.676450,-2.818516,8.901511,6.751082,-8.671079,9.595700,2.787588,5.285801,8.462851,6.906853,-5.893172,4.654439,-5.370326,1.243322,-8.237603,-8.369137,-7.761289,-6.213231,-4.940523,8.856573,3.665339,-8.161013,-3.926364,-8.401055,7.699392,7.839931,2.814381,-5.674820,8.996978,6.301925,-6.559933,-8.996844,-0.876110,-1.438624,-6.325112,6.634934,5.334225,-2.353269,7.764841,2.628517,-2.687545,-2.092338,0.028762,-2.666929,-9.166010,-4.484052,5.724875,-9.453094,6.634292,-2.787877,-3.078468,1.714703,5.540512,-0.210608,9.085807,-4.501055,-0.444756,3.976430,9.409728,-3.515666,5.374733,-8.887615,-5.811510,1.492376,4.005527,0.193153,8.165690,6.337735,4.548217,-0.987789,-0.919989,-9.277907,7.228330,-1.181630,3.338939,2.937961,-1.493827,-1.640840,-4.794682,-8.495498,1.260861,0.744890,9.235103,-4.130262,-5.737157,6.762683,9.808944,-6.930803,5.672882,0.729813,5.860106,2.882367,-8.419623,-0.588398,9.984979,-8.203523,2.719484,-5.922278,2.341615,5.369192,2.808919,-3.020525,-8.242230,9.386068,5.145866,9.041044,2.198700,-3.176189,-2.141972,-5.471750,-2.211501,-9.753250,0.201632,-7.206532,0.561978,-3.419990,-6.030268,6.580143,1.423998,-5.990688,8.187920,-8.386600,-1.932075,-2.173556,9.077798,7.024033,-9.231513,8.335395,-6.962780,-5.641998,1.943335,-8.725427,7.420081,3.012092,-2.908916,0.682035,8.731112,8.306759,8.770864,-9.003939,-8.886311,-2.434678,7.849517,-5.260027,7.004210,-0.494920,-7.777689,-0.218391,-0.726437,-7.995744,8.008821,5.150672,8.380445,-5.385355,-5.578409,-3.536571,-0.091012,0.115110,-2.743603,2.854689,-6.591536,5.267835,-2.530876,-0.664638,2.219488,-1.254861,1.594195,1.990334,-5.101544,8.809961,-2.794588,0.259486,-7.107309,-6.390322,4.242744,-0.585645,1.929665,-1.669658,9.661580,2.232635,6.517496,4.767455,4.977703,-2.151534,-4.367720,-7.429829,8.505376,-7.700699,0.463677,-5.776265,-7.804561,-8.103016,-0.603933,-5.112817,-5.823048,-4.810879,9.511133,-9.606935,-9.731071,-9.185804,-4.008118,1.029400,-6.561526,8.233073,1.670333,-4.598787,-8.261244,2.161704,3.911939,-2.036771,0.177916,-6.181395,-4.686229,9.028783,8.571266,8.786220,7.093982,3.703737,-2.049927,0.523480,-7.433450,-1.009724,-6.137069,-4.752023,7.432602,0.024606,4.882700,5.923993,-8.814021,8.378300,-4.847550,9.628139,9.021886,1.286329,6.932109,7.829432,4.905122,-5.443622,-5.502945,4.383767,5.719473,-2.094844,-5.026056,-6.799883,3.225630,-6.196187,1.097477,3.485299,-3.758713,-2.413560,9.367510,-3.475592,2.408435,-3.452854,7.157177,5.136796,0.383908,0.359565,1.679309,-3.538363,7.860570,-7.432312,6.274252,-6.284384,4.413206,7.109553,-9.479052,4.817783,3.858758,8.036920,5.743692,7.412051,2.996605,5.329447,5.816316,2.368729,-5.563767,3.497190,2.359837,-4.583289,-9.323912,1.913391,7.215876,2.590267,-2.898578,1.083316,2.357828,-6.749982,4.551430,-0.933858,-8.661036,-7.651464,2.018289,-9.263457,3.991990,7.072071,-8.613508,-3.131188,6.050406,-4.269409,1.481524,-8.585594,1.743881,9.864455,-1.725485,9.769085,8.860789,6.641378,1.028851,7.464139,-7.115595,-8.529939,4.367532,-6.726549,-7.276289,-4.854949,-0.402180,1.486321,-7.702624,6.206313,-2.529822,5.142693,-8.051008,-9.435810,-5.245432,-8.466613,0.898432,6.165841,8.337930,6.029139,7.824414,6.094122,-6.733313,0.021092,2.612269,0.829725,0.180780,8.100551,-9.979811,6.654269,3.872751,1.009669,-9.473285,9.843386,5.806387,-2.207330,4.669984,-7.390253,-8.701828,-0.422571,-7.467474,1.305931,-5.564414,6.235469,-3.229666,3.356508,-3.147628,-7.905329,7.287470,1.726896,1.303352,6.870099,4.384630,-4.420300,0.229683,-9.529821,8.442135,7.632484,-0.540064,-7.077665,3.896258,7.472679,-3.461491,0.963440,3.887091,-1.978834,-8.147741,8.308592,-0.393892,4.236606,-6.014119,5.668626,6.732809,8.488767,-8.980981,-7.764601,0.940571,6.809631,-1.792178,-3.698233,6.327750,-8.637217,-5.892893,-3.037729,7.011825,9.022179,3.724988,7.986555,3.357061,-8.098761,-2.022245,-6.912210,-2.468420,-8.454712,-4.683376,9.895675,5.065253,7.842555,7.809628,-0.648844,6.000004,0.542737,1.646920,7.655377,1.403773,-2.374027,-9.502527,-6.339705,-6.005948,6.765752,2.381866,1.895258,-7.024279,-2.579485,-3.979866,7.297628,-7.611847,-8.898020,3.834974,1.488047,0.272324,8.361410,-8.837631,4.849009,-2.566983,7.483940,9.728124,-7.075947,7.891968,2.411963,-3.749192,6.980745,7.647705,-9.103138,6.165517,-9.940512,9.318475,-2.897613,7.179291,-7.720099,6.431472,2.566933,-5.032193,-8.400498,-6.595498,8.836746,-3.626095,-4.635919,-3.535610,4.216705,-1.317999,1.388020,1.577793,3.073595,8.691325,-2.499186,3.858176,8.639472,8.777666,4.974682,9.324249,-2.526285,4.621353,-7.695840,1.269282,9.953040,8.854789,6.178724,-6.960155,1.916053,0.793467,-2.441707,4.276487,-7.473855,-4.767112,-1.860400,4.378036,0.471783,1.533663,-5.987019,6.106411,-6.760640,-7.567993,6.665297,-2.516301,-9.978674,-5.860914,-3.428816,-2.762082,2.170210,-7.931681,7.728180,-3.791659,-7.233137,-8.502531,9.153309,-1.530437,-0.967880,4.845932,-9.713972,-1.347477,9.002336,2.059600,-8.299278,0.009408,-7.512230,8.367708,5.657285,6.641621,-7.357038,-1.820826,1.648484,3.492194,-4.449053,-3.669613,1.522394,9.427987,3.819309,-4.936492,6.514827,7.751304,-9.958446,8.558373,3.827813,9.287938,-5.351096,9.074462,4.733158,2.623215,0.644986,-5.756433,-7.345230,-5.721626,-5.877444,0.158388,-0.712073,-3.875935,5.827214,-6.028764,-2.133327,-2.211577,8.076813,-3.110457,6.957971,-6.126575,7.645755,9.297527,8.273697,-7.615178,-3.732035,7.143708,-0.334487,6.653957,2.689496,-4.605371,-7.889825,-5.288206,-4.181230,-7.179564,-0.180802,9.081279,1.186965,0.868011,-2.580979,-0.496508,4.873647,3.195010,1.051623,9.357445,-5.755312,-7.193999,6.591185,-2.519849,-5.596382,6.506324,-0.382315,-6.502943,9.124759,-7.317356,3.111834,-1.338254,-0.960642,9.694461,4.307519,-3.385615,-1.833099,-9.694923,8.324474,-6.627535,8.238794,-4.799015,-3.499232,4.153333,-6.238533,3.544363,-8.732422,-2.662520,3.461514,6.317380,-2.003620,-7.911866,-3.518622,-1.166450,0.754326,6.639081,-0.345627,-2.707311,7.510512,-0.207983,8.191465,4.758242,-5.170406,-8.350971,9.436711,-9.355467,7.909871,2.230783,6.992456,3.965252,-6.812313,3.729502,-6.593529,2.685889,3.231660,6.304589,4.044039,-0.727208,-5.444539,9.348259,-7.673677,-6.962014,-7.417452,-5.611232,6.900707,-5.191709,-7.821496,5.237767,-1.666585,-8.854610,-6.607107,-3.467053,4.587902,4.534930,-8.597750,2.017068,-3.160315,-7.677464,9.737296,-6.156243,8.032968,-9.764819,-3.857052,-1.161720,-9.453842,-7.556185,7.238461,-6.131810,-7.135357,-6.197201,-8.779954,3.868976,5.049134,8.588975,-8.563913,-2.673483,0.557626,-8.385328,-5.801894,-4.472343,5.567570,5.205040,9.969546,4.994412,-0.400112,-0.252045,-0.091253,4.720763,-5.311754,-8.427916,6.660036,-3.204164,-0.946038,-8.776227,5.990605,3.814166,-8.096696,7.282827], dtype = "float32")#candidate|5020|(1170,)|const|float32
call_5019 = relay.TupleGetItem(func_4382_call(relay.reshape(const_5020.astype('float32'), [6, 13, 15])), 1)
call_5021 = relay.TupleGetItem(func_4385_call(relay.reshape(const_5020.astype('float32'), [6, 13, 15])), 1)
func_4407_call = mod.get_global_var('func_4407')
func_4410_call = mutated_mod.get_global_var('func_4410')
call_5023 = func_4407_call(relay.reshape(call_5012.astype('uint32'), [12, 10, 9]))
call_5024 = func_4407_call(relay.reshape(call_5012.astype('uint32'), [12, 10, 9]))
uop_5025 = relay.atanh(const_5020.astype('float32')) # shape=(1170,)
func_3909_call = mod.get_global_var('func_3909')
func_3914_call = mutated_mod.get_global_var('func_3914')
const_5034 = relay.const([-3.819869,-7.003992,3.031787,-1.719188,-3.238074,7.205265,7.609102,-6.514838,6.233363,-1.663468,-3.376792,-5.287773,-2.911813,-3.368923,5.626481,-1.435564,6.684897,9.334180,9.793123,7.165116,-8.113127,7.630300,-6.897420,0.015887,9.571913,7.990062,4.263089,7.591314,7.714311,4.075111,-6.816405,-5.325704], dtype = "float64")#candidate|5034|(32,)|const|float64
var_5035 = relay.var("var_5035", dtype = "int32", shape = (720,))#candidate|5035|(720,)|var|int32
const_5036 = relay.const([4.787700,5.983587,-0.937899,9.532629,-5.681245,5.566555,4.912763,-7.578622,-3.431747,0.944374,1.042224,2.842721,9.070455,9.695935,0.291420,5.163369,0.862908,-3.871403,8.487295,-6.461260,-2.117380,7.301835,-5.653256,-0.336305,5.282275,7.799610,4.993983,-5.798502,9.654521,0.480306,-4.752542,9.362841,4.911905,-3.150092,6.252412,0.618751,-3.405900,5.307768,-1.079074,-5.371268,-9.605512,-9.359741,-7.971502,-6.890761,8.736560,-1.105286,-2.162845,7.079506,8.721917,-5.908636,-4.684737,1.637170,-1.220859,0.157295,-7.747670,-6.893670,-6.678812,9.954401,0.032754,-1.647250,5.128410,7.470663,-8.753120,-6.059913,-6.977366,-7.189654,-5.345380,1.394738,6.661474,9.363299,-1.245846,-7.371262,-5.546439,2.555372,1.921903,-5.975849,-1.908874,6.576941,4.867569,6.823820,-8.572836,-0.493215,5.118149,-4.974256,1.555863,-7.944566,8.307247,-9.366275,-2.830123,-2.438846,2.081971,9.022793,-1.220640,-9.910278,-5.961731,2.964281,0.538175,7.674502,5.334925,5.260622,1.020663,6.751243,-3.253020,-8.549153,7.649838,5.166322,-1.651074,0.938849,4.240703,-9.784527,2.313401,-3.521514,5.794173,2.179562,8.822958,0.899740,-9.747561,-8.726939,-1.725013,-2.106630,6.673783,-4.367403,-2.372252,-0.397837,7.571206,6.427006,-7.283787,-5.182230,2.861444,-4.696045,-6.816971,4.642365,-3.565384,-5.807207,-4.964484,7.427690,-5.074591,5.351043,3.078074,-3.784989,-7.923964,5.728634,6.804755,1.195429,5.121829,-8.926671,6.863502,-9.719409,4.522095,9.957500,4.119070,1.908716,-7.085829,-3.160309,-2.777705,4.486247,-5.256404,8.201245,-2.568486,-6.966528,-5.616781,7.854730,-6.057683,-7.017658,-2.721119,-8.337034,-5.422023,2.919811,-7.197835,-7.825043,-0.882539,-3.608168,-3.713683,6.308696,-7.106879,-9.129977,-9.052607,-6.079980,5.944086,-0.269142,-4.058063,-1.907286,-9.399550,-7.689728,2.459623,5.735394,-4.742875,5.004560,4.699379,3.279284,-4.733269,-6.886062,5.080437,-6.671696,5.740244,7.434578,5.922955,-7.926052,8.674142,-9.376426,2.362678,9.807627,3.362368,-2.900065,6.703628,-1.585214,8.973943,-6.399112,-5.373363,-3.468422,3.618638,9.027178,1.431675,-4.371429,-4.512902,9.901312,-2.155183,7.451025,4.382319,-8.604695,4.451691,5.409517,0.551929,-9.902107,-6.372357,-2.338945,-7.364459,-1.604289,0.566977,-1.791256,0.467594,-8.602926,-7.335116,-3.793138,8.856314,-4.837896,7.963745,-0.569497,0.701058,-5.769632,7.094331,9.398070,9.479900,2.332662,-4.383448,-7.127532,6.836338,0.250282,2.412558,-2.656371,-0.782414,6.879096,-6.805419,2.591930,-8.595373,9.558198,-5.317733,4.910991,-1.271183,-7.959989,5.189631,-2.493193,7.544379,-8.239112,9.614470,-0.873894,-7.292291,-4.653288,6.727732,-8.013725,9.542215,5.001394,6.085621,1.193749,7.424761,-6.992344,0.021361,9.789056,6.767310,6.781810,-8.475843,-8.813501,4.424536,5.771785,-9.438686,5.292110,0.469407,0.198343,1.886069,-8.344222,3.990331,5.650532,-1.827022,3.655394,0.787523,-8.043980,-9.150178,-7.440748,1.558259,-0.619552,2.036729,-2.292858,-1.166091,5.468378,-6.430066,-0.086214,4.578883,-7.762590,1.721189,9.929595,-0.339906,-9.991871,-6.684240,5.212197,7.050878,-2.061813,2.095826,6.115388,-9.863803,7.768482,0.540267,-6.089378,-8.562825,-2.839682,9.356741,-9.951184,8.383497,-6.207803,9.486700,-9.837070,-8.495228,6.483240,1.019360,8.259164,-8.663410,-1.278478,2.983929,-2.488044,-9.624912,2.117294,-1.098152,6.257025,-0.875372,2.188299,7.206175,-6.936435,-9.917921,1.059431,6.752527,-3.239861,-3.950644,8.901314,3.473550,4.445548,-4.499295,8.402365,-2.554939,-7.020870,8.371425,-5.026950,2.360323,-1.428251,-1.590183,6.191608,-3.659410,5.238023,5.407853,-5.101988,-1.317522,-7.175534,-6.699357,8.123792,-2.959079,-4.122451,-0.836069,5.558131,9.641914,6.963145,2.669746,1.645564,-6.986677,-4.414417,4.320878,0.816157,-0.996408,-4.486928,8.903151,5.786086,-2.803425,0.143265,-3.357501,-8.004960,-2.925305,-4.479673,2.936018,-7.358730,-4.824949,5.415349,7.900042,-3.750406,-6.359937,9.147230,-5.077177,5.625383,-5.835582,1.585157,4.257802,-8.607664,-2.743079,-0.903077,4.543052,1.900011,6.444765,1.391307,2.021327,6.231040,2.277285,-4.484011,4.575499,-1.415357,-9.687717,7.480613,4.367545,-5.873473,-4.269381,3.236427,6.154274,7.808332,3.480066,9.612862,-4.412275,-1.385814,1.227702,-7.048433,8.621997,-8.204462,-7.210800,6.186172,-2.657487,2.618364,-8.007495,-5.109898,-0.721004,6.356132,-7.123816,-6.650466,0.510562,-0.687480,3.740666,1.744337,4.100841,3.540370,3.994324,-4.713807,-3.399393,-3.647555,-5.308533,-5.858580,6.437900,9.621477,-7.589267,-6.930122,-0.258102,8.401215,5.516033,-7.861232,-9.065153,0.143584,2.081219,0.710793,2.426009,-6.568308,-2.645941,-5.489155,-2.854007,-7.845221,-9.352511,-7.403287,9.162782,-7.139389,1.208854,-0.289179,-9.336906,1.448572,5.036394,9.552893,6.015077,-5.488908,-1.702392,9.573076,-0.138204,-6.759141,-5.848383,-7.229572,-4.069401,2.903233,6.820742,7.444233,3.347003,5.366531,-8.030062,2.607286,2.324812,9.818223,1.549775,-9.623470,-8.507786,-9.837592,-9.280986,7.190100,2.268291,-0.389836,-1.242945,5.099571,-1.041547,-1.324413,1.133089,-9.480023,9.668701,1.515488,-9.520953,0.326102,-7.725918,-1.259153,-6.381586,9.645697,-2.262317,-9.496930,3.944675,-2.256270,6.182540,-5.604959,-1.052868,1.485157,6.859944,-4.386278,-7.403991,-2.394229,3.858496,2.415653,-2.640222,-3.450330,-2.673268,0.096357,-9.713441,-2.225176,-1.871830,-9.284838,7.118843,0.090692,-9.233851,2.448634,8.799583,4.312110,-4.481354,-1.491005,1.808746,2.747575,4.575262,-1.337476,-9.200068,8.865500,9.494763,8.452491,1.014229,6.393602,3.199696,5.338351,6.821165,3.258809,5.176836,-0.087178,-5.604341,8.382002,9.558722,7.577661,-8.486765,-7.582121,4.527044,-0.099942,-5.067723,-1.854972,-1.024029,-6.550831,0.841404,1.485517,2.609059,7.663678,2.251733,-9.431554,-9.211782,-2.883514,-4.982455,7.732809,2.121678,8.592926,6.662614,8.806671,1.328371,6.567283,5.420180,2.080472,6.553534,2.439643,2.339048,7.225164,7.112883,-1.192307,-8.609168,8.669474,-8.760283,-1.647774,8.008845,0.800150,9.596147,9.771165,-0.956567,-2.841102,5.250990,-3.621247,7.395920,5.095702,-6.063118,-6.349591,5.379383,-2.265732,-3.619782,4.769813,-6.215364,-9.191069,-6.141648,-0.147815,7.543406,-9.494838,-9.506810,8.247168,-1.807749,4.669464,7.482616,4.622305], dtype = "float64")#candidate|5036|(640,)|const|float64
call_5033 = relay.TupleGetItem(func_3909_call(relay.reshape(const_5034.astype('float64'), [16, 2]), relay.reshape(var_5035.astype('int32'), [720, 1]), relay.reshape(const_5036.astype('float64'), [640,]), relay.reshape(call_5012.astype('bool'), [12, 10, 9]), ), 6)
call_5037 = relay.TupleGetItem(func_3914_call(relay.reshape(const_5034.astype('float64'), [16, 2]), relay.reshape(var_5035.astype('int32'), [720, 1]), relay.reshape(const_5036.astype('float64'), [640,]), relay.reshape(call_5012.astype('bool'), [12, 10, 9]), ), 6)
bop_5039 = relay.divide(var_5035.astype('float32'), call_5019.astype('float32')) # shape=(16, 4, 720)
bop_5042 = relay.divide(var_5035.astype('float32'), call_5021.astype('float32')) # shape=(16, 4, 720)
uop_5046 = relay.acos(uop_5025.astype('float32')) # shape=(1170,)
uop_5049 = relay.log10(uop_5046.astype('float32')) # shape=(1170,)
var_5053 = relay.var("var_5053", dtype = "float32", shape = (1170,))#candidate|5053|(1170,)|var|float32
bop_5054 = relay.greater_equal(uop_5049.astype('bool'), relay.reshape(var_5053.astype('bool'), relay.shape_of(uop_5049))) # shape=(1170,)
var_5058 = relay.var("var_5058", dtype = "float32", shape = (1170,))#candidate|5058|(1170,)|var|float32
bop_5059 = relay.right_shift(uop_5025.astype('int64'), relay.reshape(var_5058.astype('int64'), relay.shape_of(uop_5025))) # shape=(1170,)
func_5003_call = mod.get_global_var('func_5003')
func_5007_call = mutated_mod.get_global_var('func_5007')
var_5069 = relay.var("var_5069", dtype = "float32", shape = (147,))#candidate|5069|(147,)|var|float32
var_5070 = relay.var("var_5070", dtype = "float64", shape = (2, 416))#candidate|5070|(2, 416)|var|float64
call_5068 = relay.TupleGetItem(func_5003_call(relay.reshape(var_5069.astype('float32'), [147,]), relay.reshape(var_5070.astype('float64'), [832,]), ), 2)
call_5071 = relay.TupleGetItem(func_5007_call(relay.reshape(var_5069.astype('float32'), [147,]), relay.reshape(var_5070.astype('float64'), [832,]), ), 2)
output = relay.Tuple([call_5012,call_5023,call_5033,const_5034,const_5036,bop_5039,bop_5054,bop_5059,call_5068,var_5069,var_5070,])
output2 = relay.Tuple([call_5013,call_5024,call_5037,const_5034,const_5036,bop_5042,bop_5054,bop_5059,call_5071,var_5069,var_5070,])
func_5077 = relay.Function([var_5035,var_5053,var_5058,var_5069,var_5070,], output)
mod['func_5077'] = func_5077
mod = relay.transform.InferType()(mod)
mutated_mod['func_5077'] = func_5077
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5077_call = mutated_mod.get_global_var('func_5077')
var_5079 = relay.var("var_5079", dtype = "int32", shape = (720,))#candidate|5079|(720,)|var|int32
var_5080 = relay.var("var_5080", dtype = "float32", shape = (1170,))#candidate|5080|(1170,)|var|float32
var_5081 = relay.var("var_5081", dtype = "float32", shape = (1170,))#candidate|5081|(1170,)|var|float32
var_5082 = relay.var("var_5082", dtype = "float32", shape = (147,))#candidate|5082|(147,)|var|float32
var_5083 = relay.var("var_5083", dtype = "float64", shape = (2, 416))#candidate|5083|(2, 416)|var|float64
call_5078 = func_5077_call(var_5079,var_5080,var_5081,var_5082,var_5083,)
output = call_5078
func_5084 = relay.Function([var_5079,var_5080,var_5081,var_5082,var_5083,], output)
mutated_mod['func_5084'] = func_5084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3467_call = mod.get_global_var('func_3467')
func_3468_call = mutated_mod.get_global_var('func_3468')
call_5144 = func_3467_call()
call_5145 = func_3467_call()
uop_5148 = relay.cosh(call_5144.astype('float32')) # shape=(12, 10, 9)
uop_5150 = relay.cosh(call_5145.astype('float32')) # shape=(12, 10, 9)
output = uop_5148
output2 = uop_5150
func_5154 = relay.Function([], output)
mod['func_5154'] = func_5154
mod = relay.transform.InferType()(mod)
mutated_mod['func_5154'] = func_5154
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5154_call = mutated_mod.get_global_var('func_5154')
call_5155 = func_5154_call()
output = call_5155
func_5156 = relay.Function([], output)
mutated_mod['func_5156'] = func_5156
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_5160 = relay.TupleGetItem(func_4743_call(), 0)
call_5161 = relay.TupleGetItem(func_4745_call(), 0)
output = call_5160
output2 = call_5161
func_5162 = relay.Function([], output)
mod['func_5162'] = func_5162
mod = relay.transform.InferType()(mod)
output = func_5162()
func_5163 = relay.Function([], output)
mutated_mod['func_5163'] = func_5163
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2762_call = mod.get_global_var('func_2762')
func_2764_call = mutated_mod.get_global_var('func_2764')
call_5189 = func_2762_call()
call_5190 = func_2762_call()
func_1046_call = mod.get_global_var('func_1046')
func_1048_call = mutated_mod.get_global_var('func_1048')
const_5192 = relay.const([-2.091147,-1.514021,2.795671,5.138029,7.490257,-3.952148,-7.855000,-7.349190,-8.144549,-4.699670,2.889620,8.705648,9.707208,7.573419,1.223488,-1.521045,-4.858689,-9.358729,1.975118,-3.628387,-9.245719,-3.032855,-9.779346,-9.734489,6.819654,1.900606,7.677128,0.809190,8.546473,-7.045297,0.497674,-7.899880,6.957993,3.493560,-5.164570,6.021910,3.259221,-1.484055,-4.324144,-1.163695,3.995783,2.761130,-8.906184,2.218325,1.812993,-9.497748,6.366723,-5.357445,-4.472308,7.543517,7.735704,8.000599,-2.644052,5.555871,-9.454824,-6.642930,0.023449,3.807759,-3.120006,2.255348,-2.151693,6.816097,-5.896883,-4.048275,6.674325,7.452658,-8.025013,1.507905,-1.252037,2.994356,-1.906037,6.149692,5.341721,-2.110474,1.505459,9.686690,8.244840,4.292013,-4.840115,-9.485918,6.358373,2.038711,2.206615,2.991386,9.745332,-7.345962,-6.805667,2.829917,-7.985653,-7.322838,8.289246,4.717273,-6.165185,-8.954456,-3.560282,-3.614892,-4.668371,7.176441,7.163077,-9.574870,-1.486505,-4.709755,-4.770344,-6.895530,4.981977,-2.110255,0.019360,-6.623816,0.950429,-5.504485,6.709976,5.646493,-5.199412,3.916566,5.552633,-0.011220,2.585014,8.546858,-0.528919,-2.558830,-8.431423,-0.974077,9.029863,2.862419,0.860267,-2.271662,-9.476463,7.275780,6.617399,-9.749646,-6.191689,-5.088958,-5.466031,3.534467,1.018433,-0.377799,-6.847498,5.260547,8.008681,-5.852716,6.589209,-1.413003,9.569289,-5.017351,-9.422323,4.927258,-8.744124,-0.124682,3.067071,1.131069,-2.276533,-0.964787,7.295628,-4.573589,-9.521594,8.709882,0.146657,-0.259177,9.389407,8.278776,1.692484,-5.558513,-7.841001,-7.538279,-4.458969,9.785817,-8.835620,-6.269508,3.203022,-2.729411,8.536395,3.884068,1.297079,7.620920,3.883064,2.558850,-6.114185,-0.504454,-2.269006,-1.497584,-3.915827,7.124010,-1.509122,-4.548212,-2.387319,9.773943,9.345316,5.131770,-5.919857,5.002970,5.777310,4.025798,7.949799,9.983815,-3.085248,-0.478636,5.143022,7.178068,7.144941,4.216520,1.945237,-8.162064,-0.242501,4.955546,-1.583052,-6.902127,1.972855,1.164698,3.421366,3.728414,5.619327,-3.300788,0.976530,-4.388984,-3.644350,8.598384,-4.558885,-2.887905,5.373887,-7.082323,-6.627783,2.759695,-3.282723,-5.034958,7.988253,9.917541,-5.569267,0.186182,-1.627164,-9.403306,-9.143277,-3.367378,3.057217,3.454498,-9.371023,2.120345,-9.645429,4.198950,7.046973,-1.716851,6.180256,6.694259,5.321714,4.636488,-8.679567,-9.407107,7.715453,-3.388476,5.662741,3.381978,2.376278,5.069786,-7.258982,-4.243803,-7.011310,-0.868941,-8.469755,2.786675,4.317913,2.439126,8.898346,-5.159173,-1.568266,1.185881], dtype = "float32")#candidate|5192|(264,)|const|float32
call_5191 = relay.TupleGetItem(func_1046_call(relay.reshape(const_5192.astype('float32'), [12, 11, 2])), 0)
call_5193 = relay.TupleGetItem(func_1048_call(relay.reshape(const_5192.astype('float32'), [12, 11, 2])), 0)
output = relay.Tuple([call_5189,call_5191,const_5192,])
output2 = relay.Tuple([call_5190,call_5193,const_5192,])
func_5207 = relay.Function([], output)
mod['func_5207'] = func_5207
mod = relay.transform.InferType()(mod)
output = func_5207()
func_5208 = relay.Function([], output)
mutated_mod['func_5208'] = func_5208
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5266 = relay.var("var_5266", dtype = "float32", shape = (12, 10, 16))#candidate|5266|(12, 10, 16)|var|float32
const_5267 = relay.const([[[-2.392725,-9.639331,-5.341227,1.403046,1.056648,5.152289,5.876965,5.517094,0.185080,-9.016221,-0.725523,-3.824926,6.972280,5.846986,-9.413103,-8.069187],[2.280517,7.883085,2.426546,-3.178197,-4.167687,4.919542,-3.378736,6.407636,-6.561809,-3.464795,-5.080971,7.406858,1.460785,0.324909,1.401873,-3.147228],[7.742111,-6.320998,-3.021206,7.856755,-7.474172,9.130468,-3.513880,-7.598151,-6.481225,2.058473,3.205830,-8.847452,3.496880,-7.549030,5.571687,-0.129263],[5.968934,2.528792,1.438833,-9.600862,7.384040,6.222215,-3.796760,-4.220065,-4.459409,-3.127453,-2.478300,-1.181575,-8.625555,9.857263,8.659091,-7.204311],[-3.649364,6.575199,1.778571,-0.268749,3.144618,-7.596112,1.791142,-4.515690,-4.887322,-5.840322,7.542695,0.992204,2.766345,-5.430674,-1.600414,9.566205],[-3.927738,-2.423637,-4.772661,1.996248,-2.899435,-5.481691,-4.050845,7.483441,2.224879,-4.086228,-1.078739,-5.935422,-1.178205,0.279246,-8.815601,4.186764],[9.389880,-7.618721,-3.080125,2.500267,4.021999,5.711632,-6.273374,-7.124155,-4.009531,-0.640842,-3.441268,-2.086829,1.362814,2.646280,7.473781,1.787293],[2.085131,-0.306660,2.323549,-0.443791,7.627476,-1.375228,0.975997,3.911548,1.782689,-8.473670,8.411700,-4.482680,-8.391277,-6.552462,4.557622,-2.769137],[3.032792,-8.648705,-2.914768,1.162910,-1.959781,3.041072,-1.915910,1.102894,1.932360,-8.744813,5.050214,2.856066,-9.296486,2.438232,1.640377,-6.120037],[-0.297826,9.076883,-5.957164,0.839388,4.266729,-3.612870,4.645484,4.548442,8.816704,3.380837,1.722732,0.435446,-6.103198,2.323684,-3.114839,-0.163458]],[[-2.068259,-9.556085,-8.044577,-5.014439,-8.248542,-1.763573,-5.995178,-1.900489,1.958899,-7.571175,2.955677,-7.713617,-0.311357,8.538313,-4.341281,-2.609684],[-6.552273,9.735503,-2.439244,-8.168519,-1.581247,-9.447637,-1.550322,-8.402617,5.988410,-2.160593,-8.833839,-5.174765,-4.470857,-0.776114,-7.005995,-0.474108],[9.446067,2.629642,6.418879,-5.887542,-2.928958,-1.843984,-6.284433,-4.453079,-9.803582,-8.712702,-7.399682,6.796302,-4.700172,5.785933,-7.873546,4.525243],[1.779470,4.295642,-9.145626,-4.920954,3.881731,-7.905225,5.077453,5.630204,1.867204,1.815148,-1.600090,5.375347,-9.514640,3.544352,-0.083456,-0.239305],[-7.174994,-9.758372,6.036785,1.928091,8.219192,-3.069498,9.924915,-2.965919,3.781513,-1.095443,5.671130,0.813084,-6.460190,-0.804040,0.711266,-7.110750],[9.744007,1.566860,0.408743,5.968547,-2.518964,5.132038,5.326560,-7.525313,6.105989,-8.361059,-8.381370,-3.737015,8.686996,2.778282,1.132811,-7.875528],[-0.296291,-2.055624,-3.721692,3.508759,4.462855,-0.479539,-0.152250,-0.718790,8.400228,-1.308277,-8.045782,-5.319961,-4.698711,-8.930212,1.888169,-4.645417],[-3.005346,5.914900,-8.437446,9.661841,-1.782443,-5.138221,1.799064,-7.951018,8.027750,-4.079383,-0.708132,4.767677,4.702198,-4.931695,-6.543570,-3.421311],[0.612694,-1.436178,-9.741461,-2.879411,9.536440,-2.239567,6.637815,-8.170250,7.654612,-3.818598,1.991454,-6.372518,6.130022,-6.701868,8.438421,4.906445],[-7.366988,-9.907512,2.720709,8.330369,3.410413,1.277036,2.513218,-1.219565,7.718193,-9.886789,-2.157238,4.166673,4.560896,-3.166566,-6.668930,-6.282147]],[[0.319882,-2.310938,2.488306,6.820934,9.345938,5.260706,-6.412445,3.840498,-6.825926,5.529091,8.297414,-7.291394,-3.105498,1.047839,-5.926657,9.186452],[4.542422,7.703194,-1.676310,0.659641,9.487621,-1.960507,-5.179706,6.464309,9.017928,-9.401755,2.576621,1.727859,8.544330,5.159524,-2.857097,8.113546],[-6.275140,-1.015958,5.496191,-6.886376,-2.500097,2.608019,-1.067709,7.963506,7.328284,-6.942598,5.759459,-2.365036,1.984390,-7.915419,-3.302357,5.140237],[-4.529646,9.938110,9.591477,1.240944,-0.843159,5.739888,9.239927,-1.590480,-1.568836,-6.991533,6.566640,-0.388092,-6.514275,-4.348201,-7.168485,5.203976],[-5.379091,-3.658664,-5.173654,4.345810,-3.614405,6.442723,-9.726827,-1.967815,7.226268,-6.590278,5.353777,8.397636,7.291639,3.363810,4.998728,2.344033],[4.216849,0.306517,8.008559,6.202029,7.048144,7.845609,-5.086057,-5.914372,-3.935753,-1.749467,0.672567,9.061940,-3.643440,-1.234835,6.775562,5.352988],[-5.393707,-6.435830,5.454054,3.422101,2.468088,-1.698694,4.628704,5.980560,1.964060,5.548087,7.508218,-7.671913,0.529931,7.464768,-4.802362,-9.197264],[8.506964,-0.920675,-8.926608,-0.100678,-1.597669,7.967203,5.915887,-7.660013,6.191391,-5.563564,-7.612343,-5.191748,3.384653,2.434527,-4.694221,-0.807185],[-2.963195,-3.090262,4.959896,-4.041964,-2.382057,0.294248,-3.803739,-2.066111,4.743469,-2.127465,1.495051,-8.512560,-4.440912,-4.026786,4.922328,1.783199],[3.651881,-5.073378,-8.806648,8.400967,-4.883066,-1.602075,-8.695881,-5.441148,2.496272,9.905648,6.871573,-5.364150,1.461377,-2.374310,2.165627,2.416903]],[[-7.687793,8.890345,-9.443773,1.577798,1.456794,-7.538613,-4.546963,-8.617430,1.557938,6.852685,1.831378,4.640543,-1.406049,0.792156,1.157730,7.445595],[-8.409158,-7.761149,9.969605,8.931654,1.555938,-5.255874,3.179202,-7.339462,-7.712679,3.810783,9.074576,1.617359,1.135139,3.630190,4.757825,-8.046327],[-4.395280,-0.562742,-4.328737,-1.147755,4.314953,4.559902,7.387462,-2.609249,7.948897,1.144712,-3.456259,3.279835,5.945745,-8.846509,0.644598,-0.858654],[5.575507,5.368911,2.213042,0.624632,-8.419863,0.192332,-0.059714,0.732238,2.564168,-4.198302,9.618702,0.931699,3.672810,2.432283,-7.555390,-0.503063],[3.284761,2.065722,8.643215,7.559168,-5.371433,-4.673117,-8.040133,-6.860250,-7.914690,1.040852,-7.391630,0.538097,-6.179070,-0.118471,-4.342041,-4.672732],[-7.054151,-2.039144,3.012655,7.852576,-9.679118,-9.723897,-1.745062,9.507860,-5.721590,-8.100404,7.148560,-0.448312,8.710483,2.455356,2.386766,1.506215],[3.078718,6.002214,8.123919,-1.130341,-9.245017,7.276788,-2.369218,-6.792284,5.547208,4.655780,-7.057002,5.791843,7.922405,1.265006,-1.309409,-6.905791],[9.682220,-2.687366,2.745966,-1.796893,-4.585519,-6.967008,-6.212249,0.819181,0.358128,3.144405,-4.371373,0.957555,7.638443,-1.419399,6.314040,5.920755],[-7.491128,-3.397812,5.116365,-6.196309,-1.800720,-6.787842,3.090316,-1.256039,-1.760781,-7.877925,-7.704656,-1.867064,-1.245984,-4.835875,-9.187952,-2.959879],[6.267788,-0.019518,-4.998477,-6.435632,7.215128,3.893514,-8.766116,7.829644,0.324476,4.416006,-4.164055,5.289759,-4.302202,-2.590370,-7.555153,-9.816696]],[[8.709709,-0.153797,2.437771,-4.305569,3.669587,3.302000,-7.692771,-9.890196,-7.086765,9.881362,-1.610695,6.563140,-2.029586,5.063415,0.953327,1.144515],[-1.210495,-9.509969,-6.205979,-8.723804,-1.716686,-4.721839,-6.649295,7.546084,-7.367148,6.860629,6.535281,-4.162034,4.706190,-9.011216,0.116059,2.622402],[1.891497,7.512158,8.053232,7.026434,9.043139,-8.184001,9.302027,-7.178886,-5.210552,-6.326373,-4.117355,-5.250508,-7.722400,-6.115276,-0.775560,8.743373],[5.497762,2.247825,-7.034088,5.440913,-2.811433,6.901955,1.699942,-1.079510,-8.436164,4.367429,1.935651,-1.514675,4.254119,0.218038,-9.562016,5.908735],[0.591950,-9.880589,-3.418593,8.957385,6.719531,-9.596635,-7.996163,4.412938,0.495320,9.004864,-8.408507,-5.667098,5.259554,9.555480,-7.163938,5.711112],[6.864339,7.606112,9.656609,9.789273,7.635311,9.168729,-5.679840,-5.981066,-9.471158,-7.430369,4.468773,-6.724074,-9.159460,5.767096,-0.149870,-5.484661],[-8.394888,0.368094,-8.964212,9.588647,-6.245407,4.835000,0.161722,-4.560637,2.746176,-3.678508,3.043432,8.392653,-8.004679,-0.875348,-0.749625,-8.975708],[-7.127178,-4.009009,-6.359944,8.290634,9.332164,1.030726,-2.463165,-6.599204,-5.822476,2.576723,5.357799,0.321594,1.157346,-0.774456,-5.499388,-8.140746],[2.631686,4.488907,-6.633243,-8.075428,6.825595,-3.530099,-4.084436,-5.200028,2.963107,-5.346274,-3.908404,-2.165419,-3.342769,1.887883,-7.610813,9.286743],[2.631976,4.457304,7.048726,1.355403,-0.566738,7.850530,-1.627678,4.520047,3.193547,-4.360542,-1.158499,0.600918,8.232731,3.229557,-1.265325,7.218107]],[[-7.999259,-1.675122,9.039558,-9.709153,2.157992,-4.875444,5.242243,-8.280919,2.456369,8.622696,7.434322,-7.055873,8.421431,-9.537152,2.664238,3.163323],[2.403956,8.323633,3.060640,-9.503097,0.874928,-6.707332,-6.354657,9.584727,4.989004,1.852607,6.395116,-4.538643,-2.361468,8.387852,-8.524623,9.264650],[-0.733254,-3.161023,-8.556608,-8.508284,9.090629,2.965282,4.536843,-4.413729,8.755198,-3.028051,9.389634,7.134574,3.997543,6.351629,-2.862168,3.847266],[-5.591248,-7.916126,-1.147080,-4.701660,-7.039569,-0.106910,0.938263,-9.192675,-6.073808,3.358379,9.889785,9.890110,3.335625,9.856477,8.944883,-1.104111],[-3.490070,7.281335,-6.983802,4.983677,8.014027,-8.482140,-6.801992,8.817470,3.969522,-9.094267,4.821086,-9.884559,9.068754,-4.836264,-9.982678,-2.481849],[-6.681194,-5.526242,1.604275,0.474327,8.233665,7.243399,-0.126516,-3.619103,-8.435861,7.963655,3.296206,-7.958116,2.286145,9.032721,-9.903721,-5.849134],[6.296481,1.478041,-5.402516,9.960422,-6.105727,9.779928,5.443548,7.151154,3.382577,-2.864170,-5.948771,6.920314,4.184240,5.458092,-6.397070,-7.743226],[-1.706639,-0.130210,-3.299903,-2.444056,2.376783,-8.075360,-5.235680,-3.616490,-2.242185,-5.487408,6.537899,-7.174137,-0.763210,-5.464959,8.829176,4.527930],[-0.467884,9.439855,7.971959,-7.439591,9.347795,-3.143080,-1.816152,5.607112,4.899132,8.666125,6.030246,2.350283,5.179954,-4.810689,2.119386,3.143777],[-9.592071,-6.177797,-3.622967,-7.952318,7.994662,7.561248,5.359063,-0.989514,-4.047518,6.807662,2.459825,-4.885765,2.342409,-9.033859,-5.220901,-0.986149]],[[-6.560723,-6.777471,8.001077,-1.746204,4.618684,-1.049710,2.025015,2.463020,-0.866520,5.829338,-1.946869,3.479426,4.710150,-2.443099,5.561791,-5.229680],[0.603555,-7.887278,7.616786,-4.836999,0.780068,3.304997,4.148182,-5.104974,1.700986,-3.738021,4.506107,2.709983,4.952143,-3.495512,1.387926,-4.253946],[-7.121058,6.386372,7.207336,-4.999040,8.769015,5.284079,5.387653,-0.863851,-2.461948,-4.947627,-2.929268,-9.403817,5.245502,-4.043673,7.853182,7.291006],[-4.640431,5.643465,-3.790840,-7.405640,6.456181,3.430761,0.112388,5.858211,-9.996421,-0.018643,-0.113587,-4.876178,2.254085,-9.916541,7.771851,-1.410424],[-3.773595,1.155701,-0.271148,-9.755183,-1.588815,-3.472864,-9.329933,8.410734,7.252255,9.509757,-4.063092,8.051815,7.856821,-2.749923,2.240836,-8.997468],[-4.400216,8.315482,4.276669,-0.676580,4.895063,2.076026,-6.399182,-6.687920,-0.665802,2.598237,0.394664,6.549501,-2.609189,4.895347,-6.001316,-5.006628],[6.116815,0.085351,7.287975,-9.483162,-7.365241,-4.733943,-5.164976,-8.056196,2.605633,1.774989,-6.590419,8.270283,-8.166954,7.957623,-4.656261,6.318899],[1.561965,-0.839617,-4.670258,2.997436,-3.962509,-2.999665,-2.290328,-9.630820,-7.035865,-1.001855,-7.743826,-3.556176,-9.980619,5.814173,6.054269,-2.356501],[-2.390636,0.180389,-8.298682,6.141950,7.450393,9.608865,2.591976,0.062271,-9.838384,-9.321757,3.018579,2.179182,-8.436049,-0.691074,-2.059056,-8.991541],[2.292119,9.171952,-6.600500,-3.493353,-8.559754,8.264916,2.180451,-7.054700,-6.475367,-2.617617,7.191566,9.609803,5.794435,4.552504,3.707819,-5.348647]],[[7.910325,-5.220017,-5.973807,2.535642,-4.567632,-1.191903,9.444688,4.090673,-9.568017,1.503939,-0.788649,4.767692,-1.850378,6.389410,3.384236,-2.145143],[5.144246,-6.435654,-3.982710,2.961151,7.692000,-5.439374,-9.254620,-1.771315,-9.366681,-8.214706,5.763241,-5.815139,-8.588564,0.958814,3.014477,-2.290354],[-2.167774,-7.002737,8.750952,0.778307,-4.873643,5.201084,-3.157565,4.306078,-9.280883,0.715394,0.854668,7.598091,2.342546,0.061670,8.761353,2.379088],[0.603595,-2.973433,8.103792,1.371538,0.024057,-7.247160,-3.363138,-0.947848,2.875669,-0.907697,1.710820,-4.929828,-8.807274,2.900235,-8.432864,3.527366],[3.785492,-0.574289,-4.475624,-6.660223,-4.623292,1.955583,-8.249748,3.833216,3.522983,-1.491277,-4.670015,0.503420,4.200049,-3.654417,9.762294,2.547968],[1.552598,-6.592415,0.020241,0.292952,4.204781,-7.750335,1.440953,-2.357452,-8.658848,8.127697,4.534188,3.270549,-1.860793,-0.606775,-6.355448,-3.101450],[8.508102,7.720924,0.040491,0.079342,0.203476,-9.705860,2.252670,1.530309,3.700827,-7.998691,7.877152,8.408244,1.016588,4.757999,2.295985,9.389819],[-8.510062,0.596531,-9.641600,1.470010,7.734706,-6.849472,-5.430408,-1.818201,-2.562987,-6.304569,-2.104058,7.151023,-6.806355,9.073377,-4.931056,-0.868507],[5.715939,-7.958898,-4.849277,2.106728,1.679529,6.574867,9.029857,-8.713505,-5.598594,5.103585,-5.722702,9.236587,-2.786621,9.431673,3.459382,8.471288],[7.035544,-3.640247,5.904916,5.354247,4.381785,-5.305065,-0.706049,9.047456,-3.234129,-1.108575,9.134779,6.456356,-9.120460,8.012339,-1.786167,7.602885]],[[-9.407184,-0.258096,4.855902,5.633393,-6.200614,-4.897383,-1.479441,7.453914,-1.177238,0.175087,3.748298,8.317004,5.610685,-2.385182,-5.948121,-9.720002],[9.718702,-8.092071,-4.709234,-8.191693,-7.957989,-2.265066,-0.111756,8.451754,8.312098,-0.328428,1.508053,-8.107428,-5.461416,-7.543415,-8.867818,-0.753375],[7.471609,2.250662,-7.265234,-8.288287,-1.381046,2.756507,9.711538,4.545593,2.255487,9.870961,-9.831723,-6.691740,-8.829478,0.988366,8.447798,7.823370],[-2.453493,-4.849996,-8.937730,2.903918,7.148220,5.103025,9.474823,5.777334,-1.402145,1.243672,0.629416,-7.227674,2.110454,-8.151665,7.799567,6.310673],[-0.429203,-0.558257,7.494262,8.877113,-5.860807,3.489578,-5.374820,-9.156379,9.905948,4.459160,4.862467,9.738025,4.296759,1.006074,8.659794,-1.761069],[3.568248,-8.271653,0.218713,4.263562,-8.724163,1.074328,-9.590746,4.386421,-6.528220,-3.069251,-5.077181,-1.501294,4.509603,-9.837463,-0.067689,2.317140],[4.732391,-7.098956,1.836690,-1.029048,-1.562877,-0.184916,-9.955897,9.045638,-5.887761,-8.877022,8.640192,-6.217215,7.844608,0.767692,-1.289206,3.980778],[-4.222819,-5.148527,0.475042,7.782107,-0.417777,-9.615285,4.582061,1.833069,0.625422,6.893620,-5.748176,-2.828597,-9.274071,-3.183214,-1.739891,5.772412],[8.369996,-5.080470,-5.325881,3.445903,-8.242886,4.290445,6.821953,4.481325,7.404533,9.781313,2.611482,0.860373,1.446231,-3.393604,5.862015,-8.441665],[8.076487,2.645028,-3.098924,-4.942864,8.845991,-7.182142,9.440253,3.072617,-1.696169,-3.799927,-8.105618,-0.071364,1.363301,9.037485,-0.258739,-5.035332]],[[4.056388,2.800016,-8.891220,-1.174637,-5.619430,-6.506642,-6.273670,-3.128341,-0.910094,-7.208116,-1.647150,-4.180816,5.996633,-8.596811,4.952433,4.725016],[-9.193154,-1.608732,1.829358,-1.287771,7.191296,7.408456,9.068597,6.309037,-9.804274,-9.441300,-9.598467,1.408633,0.234949,7.922534,-8.792111,7.787511],[0.590045,5.092213,-3.699978,-8.121190,-6.340782,0.695564,9.586720,0.480961,9.254917,-7.064670,-7.711806,1.094462,6.298374,-4.728355,-1.958967,0.636985],[7.908317,-7.588189,-2.223678,9.011234,-0.557752,-2.243821,9.629750,2.995827,-3.961296,-3.543000,3.076276,-2.449751,-9.794765,-5.775165,-8.105542,3.080459],[-1.194039,1.340817,-8.224236,1.927744,0.101562,5.702503,6.961194,8.343514,-5.250407,-7.024513,-2.258933,5.223631,0.387880,1.739666,7.320792,8.395802],[-5.803558,-1.331812,-7.525019,8.832927,-5.864183,-4.764800,0.306526,6.842120,-8.978688,-9.191308,-4.980069,8.289686,5.644919,3.050086,7.302824,8.105020],[8.315183,0.113603,7.438890,1.954880,5.691031,-1.798696,-5.371687,-6.516723,4.475998,0.332045,-2.146659,-2.068114,7.958121,-6.565504,-5.872587,-4.505627],[-2.576769,8.878546,-2.684749,1.307546,0.934289,-7.039784,8.387022,-4.063887,8.742859,-5.121837,-3.932909,-1.217952,-2.601217,5.258666,-6.706657,-7.453924],[1.752421,-8.804795,-6.250675,9.789405,9.790446,5.700349,-3.583097,-8.918699,4.041458,-1.977387,0.520471,3.274008,3.075145,-6.153158,-0.654010,-7.555738],[0.834903,0.211910,-7.645331,7.901513,4.601191,-6.671359,-7.766558,8.226294,0.212385,2.055886,-0.853081,-2.493102,2.786092,9.061600,9.032027,9.771614]],[[2.158097,7.863629,4.618058,3.415398,6.959410,5.730065,-4.274194,-7.613328,-2.619974,-1.414121,-2.757888,-4.512258,-1.632332,-5.881537,-3.421852,-6.521222],[-3.389312,9.412690,-3.669363,-0.635472,9.339274,3.795468,3.573223,8.124730,1.783319,-4.993016,2.254308,-6.560409,3.727458,7.415515,-9.358605,0.771730],[4.991777,3.484266,0.615139,-3.124981,6.868366,7.597458,3.253626,-6.570277,-2.877331,-6.359427,4.491176,3.836366,6.549186,-2.973988,-0.007268,5.526746],[1.858245,8.007047,-9.371653,3.000638,0.927257,-2.224784,0.278273,-4.991067,-0.919169,5.508945,5.064219,-9.618094,-5.517748,-5.692831,-8.692083,-1.057689],[-0.790093,-7.575291,1.844451,-2.154369,-0.036383,2.222240,1.434970,-9.213790,9.333877,-0.690834,-8.205481,8.248221,3.857681,-4.521986,5.555919,7.595798],[-3.682663,8.447135,4.935463,6.168020,-2.915211,-6.747432,-9.225800,0.755704,-3.810725,-8.503489,-5.219785,1.449871,1.000880,3.833398,7.084460,4.989455],[3.500776,5.283868,-8.490103,-3.067490,-9.703731,3.127610,8.967160,-9.377479,-0.653282,8.868245,-6.735230,-2.281293,-8.416441,3.009691,8.071863,2.168028],[3.012661,5.357664,2.863165,-4.184573,-6.211303,-1.439316,1.542952,-4.946305,1.948438,-1.334928,-7.701435,-4.103056,6.618712,-6.113059,-9.554301,0.936997],[2.944207,3.648409,-7.781305,-5.549936,1.462420,3.713758,7.832833,-8.004914,0.896626,-5.577533,-9.476274,-3.885296,-4.152448,-7.600309,-6.068572,-2.875244],[-2.529733,4.385946,-5.533789,-1.539287,-3.899680,-8.919652,4.376164,1.489165,3.267750,-2.385091,-1.918708,3.658664,-1.172809,7.175741,8.274101,-0.689280]],[[4.973169,3.003032,9.538902,-6.253500,3.011264,9.600258,9.489008,3.967004,-6.868675,-5.034056,-6.708384,-1.842016,8.114133,3.011706,9.917025,7.699707],[7.279508,-9.704937,-8.890193,8.807468,0.842890,-8.993458,0.549078,-4.347575,9.957433,-9.855158,-1.539881,-8.918924,-6.090048,8.491433,1.270006,-5.174252],[9.427685,1.169424,8.929854,0.686990,9.196529,-1.584998,7.376388,2.484753,7.356544,-9.824304,-5.424655,-4.852728,-2.771826,-4.613522,-4.961173,2.885948],[-7.058342,7.553004,4.289338,-7.081064,-6.900052,7.057176,9.878887,-9.964543,-6.272454,2.506785,-1.137175,8.038927,8.070972,-9.421819,-4.354609,7.233942],[0.281313,5.004786,8.480603,2.434091,-4.641290,3.711618,8.392087,-1.059720,-2.692973,-7.882696,5.900142,9.152422,-1.318899,-1.875592,1.492641,8.413871],[-0.834821,8.104657,-4.114108,4.648787,2.796596,7.149717,5.557671,-9.046401,9.455193,-5.425174,-2.651175,3.023943,3.725879,-5.521599,7.439217,1.893335],[-4.305312,5.984726,-3.344653,2.963575,2.353473,-8.356039,-0.697196,-1.163981,-9.616027,4.086118,-1.047687,0.553742,-6.014450,3.538519,6.867594,-8.990063],[4.267737,-2.513182,-4.324967,-6.603905,-6.826588,-7.790016,0.814168,-1.638768,8.232963,1.162898,-2.025178,-0.897340,-2.259121,-3.236078,-2.089866,6.202499],[-7.642297,4.855646,0.532391,-5.995317,5.877452,-5.930026,9.468831,-9.581998,-3.147003,2.655196,-5.140957,-6.675070,8.251411,-6.123095,7.484398,9.437735],[2.055085,-0.145380,-1.631798,8.969957,-7.749811,3.262817,-0.075646,-9.637842,2.937277,-5.264363,4.722754,-9.396429,8.595234,0.352699,-7.202826,5.478230]]], dtype = "float32")#candidate|5267|(12, 10, 16)|const|float32
bop_5268 = relay.floor_mod(var_5266.astype('float32'), relay.reshape(const_5267.astype('float32'), relay.shape_of(var_5266))) # shape=(12, 10, 16)
func_5077_call = mod.get_global_var('func_5077')
func_5084_call = mutated_mod.get_global_var('func_5084')
const_5283 = relay.const([6,-1,6,7,10,-1,7,7,-5,3,7,-6,7,7,1,-8,-5,-8,-6,6,-8,-9,1,1,6,-7,-6,-7,10,-8,7,8,6,10,2,8,-5,6,-4,3,1,-4,-2,-1,-4,-5,-4,2,10,1,-9,3,7,-1,6,-10,3,5,4,10,-2,8,8,7,-3,-2,-7,-8,6,-5,3,-1,-9,4,10,-3,6,10,1,-2,6,-7,-10,-9,-4,9,2,-6,4,-8,1,-9,-3,3,-8,8,-10,9,10,6,-6,3,-5,-1,-8,-5,10,-8,-5,-7,-9,-9,2,8,-7,7,-9,1,1,3,3,-8,4,-4,-10,-5,5,-7,1,-8,10,-2,-6,-3,7,6,-5,-10,4,-9,-6,3,-8,6,-4,8,2,4,-4,-4,-2,10,-7,-6,6,-5,-10,4,7,-7,-6,8,6,-5,7,-3,2,-6,-6,9,-8,4,3,7,-10,2,1,4,-1,10,-8,7,-8,10,5,-6,6,-2,10,10,2,-5,-3,2,8,2,-7,-8,3,-7,-9,-3,4,5,-3,-3,-8,-9,7,-7,-5,3,-9,7,10,2,8,4,1,6,-6,-10,-5,-7,2,7,4,-1,2,-7,-3,-2,6,-3,-7,10,7,-8,-1,-7,1,-4,6,8,-5,-8,5,9,8,-8,-2,8,10,-4,-5,8,6,8,9,-8,2,3,8,7,-6,10,-3,7,-6,-6,1,4,-6,-7,-2,-7,3,-10,-2,6,3,-5,-4,-10,3,-1,10,10,-10,8,2,-6,5,-7,-6,4,8,-6,2,-1,3,-9,-7,-6,-6,1,-8,-4,-7,-2,3,-2,7,-1,5,-6,-6,-9,2,4,-8,7,-5,2,3,3,-10,-6,5,6,1,-6,6,4,1,-7,2,-8,8,-9,2,6,-8,-10,2,-3,-9,2,4,-3,-1,-5,-6,-1,3,-5,3,8,6,4,-6,-10,6,8,7,7,4,2,7,6,5,-6,7,-2,3,-10,5,-2,2,-2,-3,-7,-3,1,-6,1,-2,-2,10,-9,-3,4,9,-10,-7,-9,5,1,9,-9,1,-6,4,10,-5,-1,-10,-8,-10,-1,3,1,-10,-8,-4,-1,7,-8,9,-7,8,3,-2,8,-9,10,1,-2,4,9,6,-3,-9,-4,-10,3,10,6,6,3,-5,9,-4,8,-2,-6,-6,1,-1,-4,-5,-8,4,6,-2,-7,-2,4,9,6,6,10,-4,-9,-4,-7,-9,-6,1,-5,1,-9,-8,10,2,9,-9,-1,-9,-9,3,-4,3,7,1,6,-4,4,-7,-9,2,10,-8,8,3,-2,3,1,7,-9,-10,8,-1,3,-1,-10,4,-6,-3,10,2,-2,-10,-1,9,-3,7,2,-8,-10,1,1,2,-8,2,10,-1,-8,-5,8,-1,4,6,9,-3,2,1,-9,-1,-9,-6,6,3,-10,5,4,-1,-5,6,-3,-3,3,8,-8,-1,-1,-7,-4,-5,1,-2,-5,5,10,-3,2,-7,9,-9,4,5,-4,-4,-3,3,-8,-10,6,4,9,-10,-5,-8,-2,-1,-4,4,9,8,-9,-9,-4,2,6,-9,-5,-8,5,5,10,6,4,-5,7,6,-4,3,-4,9,2,7,-6,8,-8,1,-8,-3,6,-7,1,9,8,3,-6,2,-10,-7,-1,-10,-5,8,-7,-10,-10,5,8,-9,5,-8,6,-1,6,-5,-3,7,-5,5,-5,6,-10,9,7,4,-1,7,2,-4,-7,7,-3,8,-9,-1,-8,10,-1,5,8,-2,-4,4,6,-4,6,-1,-4,-6,-3,-7,-7,-10,7,-6,7,-4,6,4,-8,5,10,5,-8,-8,10,-4,4,5,9,8,1,6,-2,1,9,-5,3,-4,1,-2,7,9,-9,-3,-8,-4,-3,-6,3,2,-3], dtype = "int32")#candidate|5283|(720,)|const|int32
var_5284 = relay.var("var_5284", dtype = "float32", shape = (10, 117))#candidate|5284|(10, 117)|var|float32
const_5285 = relay.const([2.648696,-5.196752,-1.839955,-5.696197,-8.876007,-0.807490,-9.926957,1.989819,4.072585,-7.919139,-2.805833,-2.446706,8.748826,7.736374,-0.701502,2.149018,-2.338624,2.036793,-8.288185,-3.345347,8.282981,9.038047,-2.262785,-3.244186,6.835128,5.984446,0.403122,6.492001,8.275125,7.157614,6.617360,-3.621267,7.434507,-8.438426,6.149305,-6.322153,0.051843,-4.969872,-9.355116,-0.133406,4.850952,9.996251,2.255000,7.186981,-3.269292,-3.853172,-8.618554,7.515906,4.095003,8.401418,0.983974,0.188694,-6.765596,-4.558321,-1.652817,-2.726076,4.997555,-8.100091,-5.855501,5.949324,3.542083,-2.993075,-8.120544,8.138821,1.706365,-9.601006,-0.817419,7.125568,9.011211,-2.294327,-3.380071,5.605146,-2.597576,9.620612,-9.691315,9.556290,-3.434888,0.767721,-2.551330,-3.625221,8.597774,-4.615946,2.534278,-0.179080,0.900846,-6.675966,1.871594,4.890939,-9.275939,-8.447593,-3.774986,-2.895812,4.988641,0.559583,-0.600993,6.983501,8.339293,2.383943,-4.021303,7.634837,-0.616205,9.647083,-8.215350,-9.078275,2.012689,0.325015,-5.189316,6.374195,4.531850,7.925162,-6.304628,1.358030,-6.792292,-0.113656,3.944783,5.269201,-9.612713,5.963179,5.442800,0.687754,7.725974,-6.363546,-9.133213,1.872834,1.827055,6.717565,-3.055945,1.603076,4.080947,3.964635,5.444406,9.180752,6.284088,-0.721791,-7.658333,-0.975402,-9.718213,6.892729,-6.253256,-6.049410,-2.440366,0.050450,3.224414,0.916372,1.857195,3.671216,9.620523], dtype = "float32")#candidate|5285|(147,)|const|float32
var_5286 = relay.var("var_5286", dtype = "float64", shape = (832,))#candidate|5286|(832,)|var|float64
call_5282 = relay.TupleGetItem(func_5077_call(relay.reshape(const_5283.astype('int32'), [720,]), relay.reshape(var_5284.astype('float32'), [1170,]), relay.reshape(var_5284.astype('float32'), [1170,]), relay.reshape(const_5285.astype('float32'), [147,]), relay.reshape(var_5286.astype('float64'), [2, 416]), ), 4)
call_5287 = relay.TupleGetItem(func_5084_call(relay.reshape(const_5283.astype('int32'), [720,]), relay.reshape(var_5284.astype('float32'), [1170,]), relay.reshape(var_5284.astype('float32'), [1170,]), relay.reshape(const_5285.astype('float32'), [147,]), relay.reshape(var_5286.astype('float64'), [2, 416]), ), 4)
output = relay.Tuple([bop_5268,call_5282,const_5283,var_5284,const_5285,var_5286,])
output2 = relay.Tuple([bop_5268,call_5287,const_5283,var_5284,const_5285,var_5286,])
func_5288 = relay.Function([var_5266,var_5284,var_5286,], output)
mod['func_5288'] = func_5288
mod = relay.transform.InferType()(mod)
var_5289 = relay.var("var_5289", dtype = "float32", shape = (12, 10, 16))#candidate|5289|(12, 10, 16)|var|float32
var_5290 = relay.var("var_5290", dtype = "float32", shape = (10, 117))#candidate|5290|(10, 117)|var|float32
var_5291 = relay.var("var_5291", dtype = "float64", shape = (832,))#candidate|5291|(832,)|var|float64
output = func_5288(var_5289,var_5290,var_5291,)
func_5292 = relay.Function([var_5289,var_5290,var_5291,], output)
mutated_mod['func_5292'] = func_5292
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5357 = relay.var("var_5357", dtype = "float32", shape = (14, 4, 2))#candidate|5357|(14, 4, 2)|var|float32
uop_5358 = relay.tan(var_5357.astype('float32')) # shape=(14, 4, 2)
var_5382 = relay.var("var_5382", dtype = "float32", shape = (14, 4, 2))#candidate|5382|(14, 4, 2)|var|float32
bop_5383 = relay.add(uop_5358.astype('int8'), relay.reshape(var_5382.astype('int8'), relay.shape_of(uop_5358))) # shape=(14, 4, 2)
func_4067_call = mod.get_global_var('func_4067')
func_4068_call = mutated_mod.get_global_var('func_4068')
call_5388 = relay.TupleGetItem(func_4067_call(), 0)
call_5389 = relay.TupleGetItem(func_4068_call(), 0)
var_5402 = relay.var("var_5402", dtype = "float64", shape = (12, 10, 9))#candidate|5402|(12, 10, 9)|var|float64
bop_5403 = relay.bitwise_and(call_5388.astype('int64'), relay.reshape(var_5402.astype('int64'), relay.shape_of(call_5388))) # shape=(12, 10, 9)
bop_5406 = relay.bitwise_and(call_5389.astype('int64'), relay.reshape(var_5402.astype('int64'), relay.shape_of(call_5389))) # shape=(12, 10, 9)
output = relay.Tuple([bop_5383,bop_5403,])
output2 = relay.Tuple([bop_5383,bop_5406,])
func_5408 = relay.Function([var_5357,var_5382,var_5402,], output)
mod['func_5408'] = func_5408
mod = relay.transform.InferType()(mod)
var_5409 = relay.var("var_5409", dtype = "float32", shape = (14, 4, 2))#candidate|5409|(14, 4, 2)|var|float32
var_5410 = relay.var("var_5410", dtype = "float32", shape = (14, 4, 2))#candidate|5410|(14, 4, 2)|var|float32
var_5411 = relay.var("var_5411", dtype = "float64", shape = (12, 10, 9))#candidate|5411|(12, 10, 9)|var|float64
output = func_5408(var_5409,var_5410,var_5411,)
func_5412 = relay.Function([var_5409,var_5410,var_5411,], output)
mutated_mod['func_5412'] = func_5412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4743_call = mod.get_global_var('func_4743')
func_4745_call = mutated_mod.get_global_var('func_4745')
call_5478 = relay.TupleGetItem(func_4743_call(), 1)
call_5479 = relay.TupleGetItem(func_4745_call(), 1)
output = call_5478
output2 = call_5479
func_5509 = relay.Function([], output)
mod['func_5509'] = func_5509
mod = relay.transform.InferType()(mod)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5509_call = mutated_mod.get_global_var('func_5509')
call_5510 = func_5509_call()
output = call_5510
func_5511 = relay.Function([], output)
mutated_mod['func_5511'] = func_5511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4036_call = mod.get_global_var('func_4036')
func_4037_call = mutated_mod.get_global_var('func_4037')
call_5557 = relay.TupleGetItem(func_4036_call(), 0)
call_5558 = relay.TupleGetItem(func_4037_call(), 0)
const_5563 = relay.const([[[-5.744365,5.170190,-9.380602,0.612505,-8.433667,-9.705536,-0.654255,-1.633991],[-2.387386,5.931812,-3.529787,3.784120,-1.909797,-6.985738,-1.721537,-3.324422],[-2.807771,-6.678885,6.302486,-2.914916,-9.197700,5.140448,-4.339935,4.730928],[-2.087920,9.048017,-2.448536,-3.520969,9.404410,1.328076,6.265849,-8.247302]],[[2.267709,-5.486808,-2.826601,6.613915,-9.067005,-2.108209,-2.467582,1.144075],[-7.854578,1.376272,3.976361,6.106775,6.798597,3.624569,-7.935224,-3.925721],[-2.714860,-6.309623,5.733579,9.684714,-4.268086,-1.650008,2.819234,-2.091472],[9.903943,-9.088111,7.296114,2.675234,-1.624282,8.307084,-5.923485,-1.324521]],[[8.100845,-1.636473,-2.456910,-1.811517,0.539649,-1.275875,-6.854229,-6.993524],[-9.638934,-7.969404,-8.933844,-8.099638,-1.221422,3.476301,6.484304,6.573732],[-1.013981,0.422315,7.558417,0.342426,8.933001,9.978343,-4.828436,6.267813],[-6.477124,4.497376,0.611980,5.540166,5.679166,-3.943226,7.543174,7.270371]],[[4.568259,-6.278107,-5.878753,9.588665,1.804354,2.102879,-8.632486,4.078389],[6.908611,5.256563,-0.611508,-1.000181,8.350999,1.337931,9.841745,-4.718649],[1.395190,6.128578,1.190365,0.157588,-6.579776,-3.318138,0.901825,1.336264],[-7.387931,3.219324,-0.148950,2.555426,0.879459,-4.723020,5.057077,2.115748]],[[5.525545,8.877997,-1.411090,-1.945792,1.850372,6.572786,-3.611425,9.851946],[-9.534680,2.490073,0.025093,-1.148712,1.112604,8.554096,-0.737644,-0.661176],[6.781556,-2.818578,-7.600825,-5.033759,1.722104,1.583601,2.535285,4.609717],[3.486566,-0.945027,1.129195,4.375590,7.465807,7.510043,-5.440576,6.726260]],[[4.303798,0.700067,-4.971693,-3.420407,6.583457,4.709395,-0.405868,-9.830483],[-2.058660,-2.171349,-9.481903,-9.288061,-9.368280,6.664709,7.967270,0.067840],[-6.522631,7.816019,-7.492502,-3.430645,1.014959,-1.013502,-1.534804,3.705388],[4.100147,-2.896400,-9.084340,6.326190,8.964243,5.023580,-9.390274,7.510698]],[[3.351592,0.115597,-9.961955,1.580413,-6.221239,-7.075720,3.134850,9.724946],[7.920369,-0.244163,-4.227112,9.748771,-2.924704,9.984940,7.641651,2.381332],[1.584423,-3.261470,-7.529223,7.954941,-7.452455,-8.952649,3.397261,-0.774862],[5.215763,-4.355968,6.032973,1.351569,-1.318014,-5.349722,-8.296886,-6.082968]],[[-5.552313,7.396339,7.416819,6.832236,-7.203117,1.840010,0.562069,0.739796],[-1.819664,7.189878,5.393518,3.442896,7.479109,0.978603,6.815672,8.066510],[-7.679408,-5.674589,3.120674,4.050622,7.229494,4.195354,3.371101,-1.257003],[5.747150,7.558123,-9.503722,-9.024025,-2.255867,3.508486,-5.949148,5.668344]],[[-8.039903,-2.506122,-1.270813,2.618471,-5.607662,-7.816170,6.950412,2.906497],[-6.471966,7.873826,8.488323,-8.346776,7.421250,9.737118,-6.975341,2.060290],[-2.570076,-1.348305,7.364521,2.507006,9.614019,4.248159,-5.999486,7.739245],[3.670934,6.313619,-4.012877,-8.055232,-9.534807,7.327276,5.286518,8.428537]],[[-3.903583,-1.356864,6.662175,8.780914,7.781756,-0.957502,4.543960,4.473471],[-1.718163,2.740705,-3.762420,8.310016,5.925134,-1.934286,3.811603,5.440475],[7.316736,5.406401,6.575344,1.460767,-7.975303,-7.704154,3.463447,-2.606167],[-0.848386,6.980728,-5.281076,0.824584,7.503972,-6.781846,0.294832,0.205426]],[[5.650295,-1.037627,9.768888,0.602690,8.196907,-9.275801,7.699600,-2.047717],[-0.339005,5.149640,-2.090459,6.156283,-1.887344,-3.907394,6.221526,-0.372705],[8.903589,5.601110,8.983033,-2.974588,-1.403418,0.750166,5.174346,9.321627],[4.457065,-7.383771,-1.224871,-3.190189,0.233973,-6.512226,-3.706207,7.324712]],[[0.124712,-8.845692,-0.129841,9.280782,9.397823,-4.321122,8.561670,6.830004],[-6.903667,-8.794547,0.438271,0.910778,-6.757909,3.815243,8.178102,-6.055038],[7.204363,0.301145,5.455738,-3.312641,4.242577,1.801428,-9.517652,-9.462545],[6.045164,6.350277,1.812200,5.440185,6.953977,-1.387763,-1.028515,0.363334]],[[0.226204,7.429493,-7.244686,-5.630437,-0.055088,-1.951491,-1.976299,-9.341556],[7.671436,-5.271706,-7.276022,-1.907872,-3.599737,-0.318134,6.120145,-7.355007],[-9.874743,7.234323,3.145007,9.143493,-2.176872,-7.685752,-3.235634,-3.193017],[6.458300,-6.149903,-4.043710,8.913004,2.018167,6.672956,8.643111,1.780745]],[[7.062784,-5.282633,-7.806046,1.197768,7.850079,3.328649,-3.947078,-0.844165],[-3.806467,7.048216,5.597661,8.251502,3.369934,-0.468026,-3.449081,-9.782632],[-7.300294,-1.549742,-1.970013,1.935791,-2.069380,7.768013,-6.601215,-8.330520],[-2.229498,-5.561663,-8.137588,-7.251877,-2.949822,-2.319160,2.476204,2.242283]],[[-4.290828,-2.461257,0.955277,-2.206882,3.626272,-1.782820,9.807977,-0.201734],[-5.625444,-1.201215,0.211577,-4.740425,5.140393,-6.839318,-1.944373,-8.856490],[-6.203763,0.263583,7.238219,8.397257,-6.199325,-2.375471,-9.067445,3.817649],[7.714940,2.564685,0.813933,7.318490,-9.867580,7.984914,6.269218,0.872161]],[[-3.375318,1.814281,8.457394,-8.829421,-0.273211,7.517052,-0.609201,7.254440],[-8.075052,-7.633301,5.115914,-9.218988,8.445693,-0.184595,-8.355707,-0.018741],[-7.325138,-6.066854,-5.691286,6.246311,7.143769,1.035507,-9.215886,-6.040631],[9.981644,-6.626253,-3.082731,8.861156,-9.872820,-8.216398,2.367203,3.743723]]], dtype = "float64")#candidate|5563|(16, 4, 8)|const|float64
bop_5564 = relay.equal(call_5557.astype('bool'), const_5563.astype('bool')) # shape=(16, 4, 8)
bop_5567 = relay.equal(call_5558.astype('bool'), const_5563.astype('bool')) # shape=(16, 4, 8)
output = bop_5564
output2 = bop_5567
func_5572 = relay.Function([], output)
mod['func_5572'] = func_5572
mod = relay.transform.InferType()(mod)
output = func_5572()
func_5573 = relay.Function([], output)
mutated_mod['func_5573'] = func_5573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2889_call = mod.get_global_var('func_2889')
func_2891_call = mutated_mod.get_global_var('func_2891')
call_5618 = func_2889_call()
call_5619 = func_2889_call()
output = call_5618
output2 = call_5619
func_5623 = relay.Function([], output)
mod['func_5623'] = func_5623
mod = relay.transform.InferType()(mod)
output = func_5623()
func_5624 = relay.Function([], output)
mutated_mod['func_5624'] = func_5624
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5685 = relay.const([[[9.377712,-0.307871,5.637439,6.582679,9.200680,-1.233871,-4.020441],[-5.407424,1.045030,7.587623,3.607642,5.665236,7.936303,8.110564],[-2.415107,1.945481,8.384728,-1.720042,-2.530441,0.923385,-4.860440],[7.013051,-2.926911,5.322881,4.235664,9.641126,-2.578694,1.927714],[4.384406,6.133701,3.967645,-6.818785,-3.591466,-6.386846,-4.828852],[3.817841,1.377398,2.464544,-2.852360,-7.984525,2.590751,2.683533],[-0.193702,6.815134,9.144023,6.613732,0.019411,0.702449,5.599422],[4.093392,-4.160399,-9.337279,7.838072,9.386590,-8.365074,6.544425],[8.296442,7.959086,5.322827,-9.274181,9.931048,-4.171377,6.456628],[6.400411,2.331668,-5.679712,9.601367,4.551382,-1.913735,-0.106793],[-7.320375,9.681134,-4.474507,-8.657903,3.612454,-4.887392,-3.737395],[-0.926799,8.124559,-8.678734,-9.149983,-9.077678,1.553028,-3.356217],[-3.451953,-6.757699,1.987205,-0.278577,5.453657,4.370879,3.497371]],[[0.825302,-3.151234,2.646176,8.795957,-1.034069,-6.442058,4.855855],[3.838924,-6.987751,0.504956,-5.369202,-3.809934,-1.860677,9.022262],[-9.963924,-0.019247,7.516698,5.706762,-1.237171,-9.782356,-0.893014],[0.476495,6.734516,-3.577586,-2.503723,-1.068283,-0.563900,1.518505],[-4.674794,-0.990942,-9.839508,7.704620,-6.559503,-4.778084,8.503946],[8.311118,-1.942149,-9.566328,9.128688,4.471704,-6.451641,7.795857],[-9.087372,8.601578,6.537434,9.935533,-1.830955,9.765490,-1.684807],[4.117152,3.574774,3.689873,6.484809,2.138039,-2.451619,-3.907147],[-3.700927,9.627568,8.545211,-5.971490,0.761503,-3.879973,-2.194974],[-2.565053,9.497524,-5.108577,-2.123732,-5.276696,6.008341,3.285367],[-6.357367,-9.275614,1.080123,4.184371,0.851045,8.036444,-9.013413],[-2.211191,-6.186404,4.486771,0.849210,-5.424736,4.635537,6.692694],[-4.544477,2.252162,2.107764,3.194193,3.466190,2.948549,-0.626525]],[[9.545032,-2.353849,3.549916,-5.493127,-7.347074,5.912651,-7.511013],[-5.764128,6.972477,-4.597751,7.749977,0.247488,-2.415182,-7.228555],[5.160476,-0.797998,6.869590,-5.310558,6.815559,3.917800,-2.405825],[-2.204906,7.148258,8.140430,0.401001,2.000087,2.597344,-1.653054],[-4.743052,8.677029,1.919279,-0.771112,-2.278730,-3.520441,-1.039162],[7.793855,-3.156128,8.753570,-0.333638,-8.871908,-2.194870,4.897635],[-9.501179,7.910666,-2.258362,-3.706035,-9.493045,-7.310330,-6.573382],[3.404543,-6.333458,6.058072,-3.975810,-5.250053,7.268991,8.715738],[8.318234,9.033707,-5.664640,-0.967937,1.850873,-8.573476,6.667766],[-0.237182,5.849128,-5.041680,9.771162,-2.106009,-9.281498,-1.956114],[-5.286027,6.869367,-6.896578,4.217169,4.396489,6.146465,6.537032],[2.010477,-5.358413,-7.601939,6.836736,1.225054,-9.439773,-5.211054],[8.928512,1.374486,-0.622125,5.731223,2.398956,5.992902,-0.710463]],[[-7.016309,9.736068,-5.076218,8.401649,1.666802,-8.750944,4.402304],[2.092913,9.495847,1.025793,-3.713240,-3.927048,-2.280402,-4.154821],[-8.023525,0.061389,-8.872638,-4.523943,-3.019978,2.359487,-6.933083],[3.382267,9.239902,-5.452123,7.151638,1.385295,4.088681,5.752631],[4.925886,-8.175471,-3.910790,-8.194347,-2.400249,2.143816,8.635257],[-6.832220,-2.527360,8.792689,-0.625092,2.307991,9.699284,0.215872],[-2.627078,8.436935,7.989154,7.598114,6.241846,-4.492539,1.670166],[-0.499911,5.029157,-8.843840,-2.974891,0.683944,7.718483,-3.742563],[7.969245,-4.751060,-5.150404,2.516886,8.733898,5.118351,5.827699],[-9.060070,-5.077945,2.665812,0.508567,0.804070,3.395765,2.348119],[9.896934,-9.979047,1.947542,-8.474329,-1.622094,8.829379,0.573797],[-8.352121,8.450127,4.326914,8.953747,3.374237,-8.501930,6.134791],[4.122060,8.937043,-2.167971,9.428921,-4.079813,-7.559779,4.753128]],[[-6.108880,-2.601138,7.585137,9.793919,5.835846,6.793668,1.963173],[-0.787235,-3.957113,4.172571,-5.713712,5.784311,-6.634968,-8.965329],[-9.205876,-9.787445,-2.729794,5.521335,-8.292110,-1.130323,1.257164],[-8.632279,3.635546,9.694619,-8.421927,1.136862,9.129208,-3.321288],[-2.267433,-5.737708,5.687319,0.937639,1.293544,0.904332,5.183215],[-9.164022,-4.866511,-3.227136,6.231632,6.484201,-5.972396,-7.523777],[1.242322,9.958410,1.604134,-2.612171,6.786011,-2.902027,-1.679644],[-5.937207,1.893331,-6.849494,-5.395129,-6.794589,1.551192,6.510035],[-2.176591,9.366639,0.478144,-5.443263,-9.905030,1.469732,-4.272017],[-9.902527,9.165283,3.654930,9.039700,-2.831531,-1.735089,6.029216],[-0.686538,8.205544,0.935092,-8.067683,-1.946701,4.107500,2.390734],[-8.329065,9.826646,-4.469697,1.018739,2.348188,-7.666250,-0.225874],[-5.151381,-6.704496,0.287140,-9.132142,-4.733032,4.331956,3.016619]],[[5.430451,9.468825,-8.804307,-3.411480,6.441501,-2.623037,8.555720],[8.059568,5.935191,6.212157,-2.893306,-6.110222,7.036161,-3.263233],[1.939569,-5.463726,-0.732694,-1.093123,-9.825280,-9.204064,-2.745031],[-8.781451,6.606832,-2.641380,-1.721900,-9.185193,-8.739980,6.719277],[7.290947,-9.658379,5.901127,7.536735,-6.079932,-3.788739,-1.787248],[-2.136023,-0.610069,-2.832559,-5.911122,-7.776837,3.294302,-3.644529],[5.881294,6.152746,1.535722,9.857589,-5.566230,-0.978015,-4.883680],[1.265555,0.641742,-5.666509,6.856874,2.955828,9.512007,-4.372422],[-3.522511,-3.472897,-3.764313,-7.600198,3.680807,-7.657460,-6.906242],[-3.022608,4.559076,-7.253884,8.356362,-5.654330,2.221505,5.441837],[-5.108434,9.830659,-1.938277,-3.065331,-8.755272,-3.453017,7.198391],[7.360316,3.467453,-8.275155,-5.102881,-8.112415,8.119477,-5.179190],[-9.130307,4.964834,2.223741,-5.997013,-0.081371,-1.237445,9.113394]],[[-3.901899,3.654278,4.562898,2.395207,7.730628,-1.019172,-6.444257],[6.131474,-2.212621,-7.097734,-9.365181,9.616218,6.286481,6.999032],[-8.221267,-2.654658,9.151346,-6.683193,-0.987892,4.751789,0.278429],[9.942306,7.377415,-0.494164,5.509132,-1.328904,-2.126204,-7.934020],[4.636807,5.904759,-9.867161,2.336883,8.763213,-5.742099,6.414903],[-6.458670,5.530793,-7.490277,-4.795763,0.389143,4.408612,7.545622],[7.548274,4.819423,6.059462,-1.592051,-5.074809,-6.363925,2.551083],[-1.352928,-3.027315,-2.283893,-4.270213,-5.304855,0.314737,-3.324545],[1.687402,0.589297,6.583987,-2.029145,4.435715,1.423391,-1.232963],[-6.156284,-3.099164,-4.454643,0.682135,0.431303,-8.413525,-0.636678],[6.261551,-4.765132,-2.387821,2.666673,9.474368,-4.883908,-7.839074],[-2.863631,7.145146,-3.250554,5.217932,-5.253381,9.619758,0.403670],[-6.327319,-1.235085,-5.061340,-9.397886,-0.029709,0.788467,3.640712]],[[-3.224006,9.816722,-6.548424,8.036672,-7.615656,-5.508412,4.480993],[-4.716782,1.585392,-3.531512,-4.654148,-4.098689,4.917017,-0.835708],[-8.217963,1.104681,3.191357,-8.896494,4.289651,5.039557,-5.260646],[7.684897,6.675344,-7.174846,-0.236597,-6.447719,-3.827931,7.297663],[1.269268,-8.279907,-3.632386,8.774996,-9.455833,2.817603,9.652438],[3.129910,-0.324519,-9.400369,8.913036,-0.313632,2.106456,-5.597651],[-0.751910,-1.739323,-2.712604,9.032283,-3.197167,-9.231599,-7.717846],[-8.999831,-6.532938,-0.546371,-4.968299,6.043599,4.327915,8.446599],[-1.667549,-3.709158,-8.117290,5.687795,8.177147,6.974463,2.533005],[-9.999184,7.050516,6.210110,7.917201,9.719355,-7.836385,3.602805],[-3.843064,6.928620,-6.383897,6.128630,-3.131006,3.669735,-0.410859],[5.881297,5.780172,5.510311,-9.964573,-3.445655,-1.757493,-3.246092],[-4.718503,9.012728,-2.220838,-6.388239,-9.561272,4.711100,-5.296852]],[[8.933997,2.735080,-9.140704,-0.486886,-5.951324,-7.252334,-7.187293],[-6.146991,-4.324918,-1.404637,6.036110,-3.624682,-9.610386,-5.247084],[4.457216,-3.681072,6.165618,8.955050,-5.091846,9.377196,-8.740907],[-5.250864,9.498951,5.081722,6.534742,3.261445,4.127719,-7.588452],[-9.534428,3.219091,6.618408,-1.864665,-1.290360,-3.527656,-9.210979],[9.786468,-3.699265,0.115496,-9.844635,6.017208,4.038014,-5.809328],[-0.846112,-7.864003,4.400206,-6.906504,2.036837,3.617223,-9.405705],[7.077841,-8.161779,0.363676,-2.625586,-1.106572,-9.196903,-3.687476],[-5.761234,-0.786802,-1.253465,8.141983,-3.359179,-7.976140,4.523915],[0.410115,-5.796128,-8.173518,0.602444,2.054242,-6.125895,-8.180461],[4.050090,-5.001534,-5.766791,-5.789222,3.599042,-3.245195,0.671584],[-4.618541,8.882814,-3.081488,-1.982876,-8.797303,-8.041119,7.005218],[5.264428,8.084352,-2.347130,-4.538915,-2.646047,6.730421,-4.141031]],[[-9.019699,5.058438,-5.858970,-0.562949,-7.598304,9.411173,4.964203],[-0.608085,7.710075,-2.447785,-5.224717,-3.663184,3.801478,7.664805],[4.510460,2.981834,3.606432,-1.180892,3.952271,-9.094063,3.649000],[-6.997261,2.516444,9.471984,-9.400985,-9.260062,-3.862517,7.955564],[1.279793,4.417690,-9.473556,-6.839733,3.473374,-4.579280,-3.777108],[-4.243588,-3.073181,-8.370962,6.041983,-8.327266,6.445795,-2.524785],[-7.723205,-3.484026,-2.054388,-8.647214,-2.256283,-0.867199,6.738672],[-5.092016,2.556874,5.520221,1.303660,0.535909,4.470112,-8.744050],[-7.227991,-1.687038,-2.149129,2.062649,-5.848552,0.245962,-8.740714],[-0.429021,-7.634441,3.306357,0.348140,-1.195856,-3.364092,2.605148],[7.178050,3.235011,-7.018697,-5.684449,-1.015014,9.685894,7.901056],[5.986095,-6.235428,4.208314,-0.559634,-1.812311,4.883588,-5.665005],[4.215927,7.585018,0.237380,-9.474680,6.549147,-7.316145,-1.807797]],[[-7.062272,-2.691994,-3.189867,-2.174586,-9.100627,-1.737703,-0.340295],[2.893128,-0.349986,2.040066,3.935670,-9.139821,-5.836345,2.951518],[3.969564,1.676923,4.763215,9.076946,-4.372237,-9.407300,-5.285308],[-0.032902,-9.214198,7.952061,-4.884616,1.761238,3.370838,7.738233],[0.280725,-2.932151,6.545974,-6.130822,6.033377,-5.737517,7.884707],[-8.016046,1.608212,9.712724,-6.530368,-7.468902,3.438783,6.710713],[3.476822,-1.791078,6.479777,0.690898,-9.568203,9.546765,3.990096],[-6.030476,-0.065380,-7.740110,5.892156,-5.249527,-3.320500,-5.524108],[-6.285486,-2.683938,-4.573448,-1.263846,1.184423,-2.882494,7.971442],[-1.132251,8.795686,-0.313891,4.708646,-5.641550,-7.122200,4.499652],[7.713291,-4.115218,8.965336,-1.868697,1.639303,1.721476,-2.562431],[6.397045,4.842477,6.756472,-1.514981,2.413382,-9.499804,-4.484592],[-3.377859,-4.650932,1.647662,6.523548,6.710086,-9.200549,-3.860975]],[[-1.035870,-9.176769,-7.420917,7.303918,-5.434756,1.992028,5.300211],[4.955171,-8.934408,9.588974,-0.496219,6.105323,2.642389,1.636133],[-6.084473,9.226360,-9.287365,-0.723923,-5.576212,-8.756495,5.102443],[-1.153996,-0.966483,-9.548558,6.558520,3.956567,-2.722822,1.378776],[2.095605,1.091895,-7.721950,-3.936731,-4.001239,0.708776,-2.051953],[-7.638271,-5.025465,1.636082,-2.435984,2.774451,0.996956,7.197119],[-4.456475,-2.484172,0.405154,6.360793,-1.796836,3.225401,-5.504868],[3.758168,-5.452973,-2.073259,-9.904347,6.892348,2.276635,-0.795312],[1.585658,-6.396324,-2.118958,-9.351887,-8.793458,7.432772,0.347773],[-8.813155,-3.251425,9.774530,6.753475,2.993410,6.590558,-3.793453],[6.644287,6.707000,1.288156,-5.579787,-3.486741,4.334868,-5.286734],[-8.964326,3.433356,7.182821,-4.553076,2.167846,-2.534300,-1.806848],[9.441374,-5.455797,8.201067,-4.283606,2.439863,0.861619,4.394100]],[[1.817263,0.736085,6.442836,-2.666982,-7.308171,0.425687,-0.641983],[-5.962937,0.955347,0.028028,2.143023,-8.458765,2.772985,-7.795870],[5.481615,-4.327181,-6.606319,-6.677652,-6.610811,-7.683645,-2.322179],[-2.849540,-3.663702,3.530194,5.469756,1.287070,4.692857,-8.160618],[-4.448739,7.889857,-4.761463,-7.079951,-0.811534,-3.928787,6.245465],[8.958658,0.711027,-5.827178,3.598678,6.395491,-1.187109,5.352123],[-7.177664,7.070683,-4.665343,9.096220,-3.144189,2.810076,-1.421775],[5.761468,2.089864,6.183288,3.842864,-5.272055,4.639195,0.655168],[-9.038543,-9.942862,-3.410990,8.890851,-2.481125,6.881861,-4.860716],[2.369792,-5.725749,-7.202161,-2.546670,-8.073330,6.761809,-5.159184],[3.390256,6.553312,-7.093722,-5.518290,7.046714,1.863315,-6.069991],[-5.589159,-9.482122,-4.437926,-6.926220,-6.199272,-7.802182,-0.341854],[6.862110,5.007698,-6.530462,-6.647291,-6.258137,6.506720,6.512908]]], dtype = "float32")#candidate|5685|(13, 13, 7)|const|float32
uop_5686 = relay.sigmoid(const_5685.astype('float32')) # shape=(13, 13, 7)
output = uop_5686
output2 = uop_5686
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
