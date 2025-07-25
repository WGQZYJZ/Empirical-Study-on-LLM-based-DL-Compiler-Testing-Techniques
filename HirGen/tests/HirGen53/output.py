import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_115 = relay.var("var_115", dtype = "float64", shape = (3, 12, 1))#candidate|115|(3, 12, 1)|var|float64
uop_116 = relay.acosh(var_115.astype('float64')) # shape=(3, 12, 1)
bop_125 = relay.bitwise_and(var_115.astype('uint32'), relay.reshape(uop_116.astype('uint32'), relay.shape_of(var_115))) # shape=(3, 12, 1)
bop_130 = relay.not_equal(bop_125.astype('bool'), relay.reshape(var_115.astype('bool'), relay.shape_of(bop_125))) # shape=(3, 12, 1)
uop_144 = relay.asin(bop_130.astype('float32')) # shape=(3, 12, 1)
bop_151 = relay.multiply(uop_144.astype('uint64'), relay.reshape(var_115.astype('uint64'), relay.shape_of(uop_144))) # shape=(3, 12, 1)
var_175 = relay.var("var_175", dtype = "uint64", shape = (3, 12, 5))#candidate|175|(3, 12, 5)|var|uint64
bop_176 = relay.subtract(bop_151.astype('int64'), var_175.astype('int64')) # shape=(3, 12, 5)
uop_179 = relay.sigmoid(uop_116.astype('float32')) # shape=(3, 12, 1)
bop_184 = relay.logical_xor(uop_144.astype('uint16'), var_175.astype('uint16')) # shape=(3, 12, 5)
var_187 = relay.var("var_187", dtype = "uint16", shape = (3, 12, 5))#candidate|187|(3, 12, 5)|var|uint16
bop_188 = relay.not_equal(bop_184.astype('bool'), relay.reshape(var_187.astype('bool'), relay.shape_of(bop_184))) # shape=(3, 12, 5)
bop_201 = relay.logical_and(uop_144.astype('bool'), bop_176.astype('bool')) # shape=(3, 12, 5)
var_219 = relay.var("var_219", dtype = "float64", shape = (3, 12, 6))#candidate|219|(3, 12, 6)|var|float64
bop_220 = relay.mod(uop_116.astype('float32'), var_219.astype('float32')) # shape=(3, 12, 6)
output = relay.Tuple([uop_179,bop_188,bop_201,bop_220,])
output2 = relay.Tuple([uop_179,bop_188,bop_201,bop_220,])
func_225 = relay.Function([var_115,var_175,var_187,var_219,], output)
mod['func_225'] = func_225
mod = relay.transform.InferType()(mod)
var_226 = relay.var("var_226", dtype = "float64", shape = (3, 12, 1))#candidate|226|(3, 12, 1)|var|float64
var_227 = relay.var("var_227", dtype = "uint64", shape = (3, 12, 5))#candidate|227|(3, 12, 5)|var|uint64
var_228 = relay.var("var_228", dtype = "uint16", shape = (3, 12, 5))#candidate|228|(3, 12, 5)|var|uint16
var_229 = relay.var("var_229", dtype = "float64", shape = (3, 12, 6))#candidate|229|(3, 12, 6)|var|float64
output = func_225(var_226,var_227,var_228,var_229,)
func_230 = relay.Function([var_226,var_227,var_228,var_229,], output)
mutated_mod['func_230'] = func_230
mutated_mod = relay.transform.InferType()(mutated_mod)
var_354 = relay.var("var_354", dtype = "float32", shape = ())#candidate|354|()|var|float32
var_355 = relay.var("var_355", dtype = "float32", shape = (5, 7, 8))#candidate|355|(5, 7, 8)|var|float32
bop_356 = relay.floor_mod(var_354.astype('float32'), var_355.astype('float32')) # shape=(5, 7, 8)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
const_361 = relay.const([-9.139426,-3.294542,9.749554,-6.863416,3.821421,-9.620133,-4.510016,2.926784,-1.865798,-8.852022,0.321656,-5.731647,-7.046008,-6.756930,-3.366249,9.567186,2.689848,5.932185,6.594556,4.408830,-3.879782,1.265465,-1.896995,7.299557,-6.731801,-5.517531,9.229497,7.092987,4.082013,-5.564625,4.134045,3.627067,9.086458,9.805286,-7.640425,-7.880339], dtype = "float64")#candidate|361|(36,)|const|float64
var_362 = relay.var("var_362", dtype = "uint64", shape = (180,))#candidate|362|(180,)|var|uint64
var_363 = relay.var("var_363", dtype = "float64", shape = (1, 216))#candidate|363|(1, 216)|var|float64
call_360 = relay.TupleGetItem(func_225_call(relay.reshape(const_361.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(var_363.astype('float64'), [3, 12, 6]), ), 3)
call_364 = relay.TupleGetItem(func_230_call(relay.reshape(const_361.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(var_363.astype('float64'), [3, 12, 6]), ), 3)
bop_371 = relay.left_shift(bop_356.astype('uint16'), var_354.astype('uint16')) # shape=(5, 7, 8)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
call_378 = relay.TupleGetItem(func_225_call(relay.reshape(const_361.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(call_360.astype('float64'), [3, 12, 6]), ), 0)
call_379 = relay.TupleGetItem(func_230_call(relay.reshape(const_361.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(call_360.astype('float64'), [3, 12, 6]), ), 0)
bop_382 = relay.bitwise_or(var_363.astype('uint64'), var_354.astype('uint64')) # shape=(1, 216)
const_392 = relay.const([[[0.405473,1.654458,-9.375551,-2.866160,-8.083969,-4.661876,-7.620081,7.795416,-2.552622,3.507049,5.155220,-6.233168,9.960635,4.494989,8.500834,-7.447696],[-5.106059,-9.328740,5.866638,6.999931,-8.994909,4.986978,-5.543354,9.174547,7.281512,6.256543,-5.595303,-8.972951,4.357910,0.695840,-2.462902,2.228538],[9.343952,1.804832,-4.464015,2.912127,-7.474849,-6.246229,1.491448,5.958166,-3.067986,2.264428,-5.805958,-7.376914,-8.426099,-8.206629,3.223647,6.207901],[8.667753,-8.943570,9.711423,-6.521719,-9.757367,-2.105554,-0.303712,-8.322201,-1.491531,6.950787,7.376063,3.582050,2.580093,3.021292,3.933784,-0.224351],[0.467632,4.383834,-7.536130,2.285210,-9.697315,-0.127368,7.821648,6.924212,-7.605409,7.834570,-0.772361,8.882190,-4.174772,5.267843,5.084046,5.819876]],[[-6.598242,1.228380,-9.049200,1.588598,8.439403,-5.566905,-1.546060,-0.470508,-9.582653,-2.019809,-6.021491,5.383069,-7.200148,2.696226,-7.664716,3.825607],[1.562059,0.757912,7.978043,-0.259965,-9.217946,5.683349,-5.851470,8.761529,2.403820,5.684613,-9.766151,4.938635,5.341702,-7.118579,2.080319,-4.274663],[8.763468,-0.717618,-7.889342,2.113335,0.963650,9.442306,-7.639415,3.380558,6.931405,-5.729448,8.558104,-6.353111,-0.976670,-6.148209,-3.763643,-0.142611],[-1.213026,-1.553472,5.940309,5.528577,1.500204,-3.414518,6.460590,4.634493,-7.514887,-1.486686,7.592241,5.647522,-5.687017,2.285203,-7.000008,-6.958725],[1.760292,-7.246892,-8.834475,1.225709,-9.831810,2.600049,1.940693,-2.530816,-1.694399,2.404508,-5.933185,4.741621,-1.748137,6.941068,-0.118784,7.580653]],[[3.042558,-7.912949,2.592050,5.579948,7.589912,-9.363337,0.376353,3.741567,2.175874,-3.406211,0.150463,-7.536156,-4.460282,-8.148319,8.702973,-4.188217],[9.715810,-1.371159,6.385616,3.651624,0.421029,0.986775,-5.894063,-4.072363,-1.199440,7.872446,4.125383,2.483585,-2.621181,-5.088499,-0.122514,-2.596183],[-2.496745,-1.180547,-4.293232,-4.500111,3.511415,-7.970696,-8.569220,-3.303011,8.028088,-1.616863,2.893730,6.350548,-8.099289,-1.927858,-9.387231,-2.914044],[1.407441,-4.688257,-2.540656,5.875266,4.142315,-5.731373,8.342832,-9.992749,-0.167898,5.644017,-8.940714,8.922174,-5.272070,1.931158,-7.420161,4.038121],[3.711807,5.289449,1.007026,7.480708,5.921665,-9.652153,-1.660856,0.749023,-5.435275,0.448153,6.081279,2.112084,-7.274184,2.588721,-1.539748,-0.132451]],[[-4.952116,-3.349619,9.921116,-3.448983,0.620005,1.017308,8.114004,-1.023319,6.239392,6.243182,8.778339,-5.572353,1.839820,-4.171834,8.659703,4.797945],[0.414677,2.022704,-0.608741,6.836758,-4.574978,9.083860,7.094584,4.423876,8.602004,-1.576315,1.482548,-1.514004,-0.673520,6.473351,-2.683006,5.920102],[-4.884235,-2.048154,7.270306,-1.911341,-3.533377,5.506522,6.672803,-3.912905,2.544052,5.887776,2.239960,-0.250853,1.490566,5.618936,-6.684510,7.069103],[8.918124,0.466883,5.802588,6.176252,-4.902638,2.759145,7.694588,-7.320980,-6.359351,-7.483330,-0.483941,8.991784,-2.086833,8.847327,-5.177404,3.295923],[-4.560874,-0.615824,-8.882056,9.539503,-7.631523,-0.697067,-5.479411,1.278428,4.810943,-9.895870,-5.546659,5.474662,4.763689,8.250609,7.383086,3.148478]],[[-2.190918,0.699195,0.625594,7.530331,9.470146,-1.263531,-9.931030,4.934535,8.278072,7.588921,1.230803,-3.082316,4.850955,-7.737793,-5.224449,-1.979859],[8.812674,7.788936,-9.651640,4.520645,-5.562910,9.881168,0.505704,-9.065079,3.664245,-0.688913,-4.390422,9.190610,-4.926810,-4.535605,9.092102,1.439971],[-8.171718,-5.237658,4.750305,0.554400,1.988239,7.318625,4.217519,4.268409,8.578678,7.389397,-4.884010,-3.597631,4.309039,6.157094,7.141012,8.469623],[9.359275,5.671120,7.208477,-7.692228,2.117304,4.019070,-7.315557,5.757442,-2.509997,6.627007,7.039526,-4.175784,3.808313,-8.777301,-1.481073,-4.895092],[3.501162,2.973584,-4.320460,9.847971,7.118599,-9.584064,3.904640,6.343712,9.477451,-4.988283,-6.619251,9.463058,-3.024665,7.785169,9.910806,-9.100120]],[[1.542196,-2.316005,1.212250,7.005898,-6.288004,-2.840374,-3.674679,-5.560062,0.946951,-0.025294,4.347885,2.564620,4.255802,-5.229470,-7.661585,3.691685],[-6.278810,-6.639916,8.637589,-6.973166,2.951875,6.301724,3.279087,7.718888,-4.776049,-8.872370,8.297532,1.338619,-6.637090,-0.572405,-1.963291,-1.835883],[2.950626,8.195660,6.467829,-6.410992,-7.262949,-1.928888,0.024949,-8.046744,2.400066,8.573348,-1.431109,-3.589577,3.308406,-8.105928,-3.036579,-5.399859],[1.111076,2.000537,-4.065387,5.952526,3.380367,-6.629430,-0.070098,4.428753,3.011606,-3.298899,6.120929,3.942895,1.231855,9.314417,-0.384744,4.390797],[4.140154,-2.417576,2.086520,-3.685319,6.437907,4.621039,-5.417156,-0.313178,-5.017516,6.164244,7.402655,-0.844284,-5.223272,-4.502687,6.710214,-4.934544]],[[-9.344085,-7.496683,2.820326,9.173717,0.492179,-1.348811,5.462089,-8.757413,4.824799,2.840291,-8.241818,-3.153647,2.753366,9.813469,-9.239584,7.175729],[7.803811,-6.604478,9.559322,6.730988,3.374193,-7.509193,-7.549535,-5.509729,-9.394535,-2.212967,8.356628,-7.236687,-8.546068,1.829749,1.498364,0.775431],[0.406361,0.908179,8.364146,8.105213,-4.558583,6.934623,-9.774960,8.984906,-5.791691,4.873288,-7.735356,-4.308225,-7.188025,7.946206,3.871068,-3.603695],[1.667043,8.274932,-8.436019,6.332996,-3.914598,-3.897100,-7.201943,3.391137,4.223555,-0.888109,-9.242646,-5.181262,-5.552119,5.164402,5.122073,-8.195266],[8.941602,8.593444,5.930262,1.113353,-4.637475,-2.025957,1.842573,5.075662,1.626838,-3.727431,-8.106645,-5.054450,-2.662114,-9.390867,6.483981,-4.679195]],[[-2.304059,-3.941027,-6.061673,7.592162,7.510721,4.375888,-8.274168,-7.178791,-1.362899,7.902494,5.199731,-9.953341,1.108339,7.842048,0.361592,-3.501428],[-0.911108,1.029713,-3.243844,7.503728,8.612602,-7.812256,0.017183,6.577619,4.751121,-0.836498,-3.169429,-5.537812,-4.568914,-2.263567,-3.018725,8.430174],[1.056596,5.000721,-4.084304,-4.018538,-3.563764,8.416917,1.593768,4.784962,7.906351,4.812954,-8.830357,-1.092071,-2.720118,9.806293,6.483964,8.313702],[1.490902,-7.588464,0.732593,9.669414,1.775384,4.498059,0.431088,6.430636,-9.229724,-3.276992,-6.491779,9.312035,8.634932,1.962750,-1.166974,-6.109607],[-7.409548,3.138242,6.447101,9.317854,5.132275,2.937292,4.474860,3.353420,9.484453,1.282399,-2.266286,-6.756102,9.867407,-3.628044,-9.685275,6.226775]]], dtype = "float32")#candidate|392|(8, 5, 16)|const|float32
bop_393 = relay.multiply(var_354.astype('float32'), const_392.astype('float32')) # shape=(8, 5, 16)
bop_400 = relay.divide(call_378.astype('float64'), var_362.astype('float64')) # shape=(3, 12, 180)
bop_403 = relay.divide(call_379.astype('float64'), var_362.astype('float64')) # shape=(3, 12, 180)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
call_407 = relay.TupleGetItem(func_225_call(relay.reshape(call_378.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(call_360.astype('float64'), [3, 12, 6]), ), 3)
call_408 = relay.TupleGetItem(func_230_call(relay.reshape(call_378.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(call_360.astype('float64'), [3, 12, 6]), ), 3)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
call_412 = relay.TupleGetItem(func_225_call(relay.reshape(const_361.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(call_407.astype('float64'), [3, 12, 6]), ), 3)
call_413 = relay.TupleGetItem(func_230_call(relay.reshape(const_361.astype('float64'), [3, 12, 1]), relay.reshape(var_362.astype('uint64'), [3, 12, 5]), relay.reshape(var_362.astype('uint16'), [3, 12, 5]), relay.reshape(call_407.astype('float64'), [3, 12, 6]), ), 3)
uop_427 = relay.atan(call_407.astype('float32')) # shape=(3, 12, 6)
uop_429 = relay.atan(call_408.astype('float32')) # shape=(3, 12, 6)
output = relay.Tuple([call_360,const_361,bop_371,bop_382,bop_393,bop_400,call_412,uop_427,])
output2 = relay.Tuple([call_364,const_361,bop_371,bop_382,bop_393,bop_403,call_413,uop_429,])
func_430 = relay.Function([var_354,var_355,var_362,var_363,], output)
mod['func_430'] = func_430
mod = relay.transform.InferType()(mod)
mutated_mod['func_430'] = func_430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_430_call = mutated_mod.get_global_var('func_430')
var_432 = relay.var("var_432", dtype = "float32", shape = ())#candidate|432|()|var|float32
var_433 = relay.var("var_433", dtype = "float32", shape = (5, 7, 8))#candidate|433|(5, 7, 8)|var|float32
var_434 = relay.var("var_434", dtype = "uint64", shape = (180,))#candidate|434|(180,)|var|uint64
var_435 = relay.var("var_435", dtype = "float64", shape = (1, 216))#candidate|435|(1, 216)|var|float64
call_431 = func_430_call(var_432,var_433,var_434,var_435,)
output = call_431
func_436 = relay.Function([var_432,var_433,var_434,var_435,], output)
mutated_mod['func_436'] = func_436
mutated_mod = relay.transform.InferType()(mutated_mod)
const_515 = relay.const(-2.950448, dtype = "float64")#candidate|515|()|const|float64
const_516 = relay.const([[[-4.416449,4.841633,-0.265275],[-7.016025,-8.546999,-0.739426],[1.477266,9.486489,9.907563],[-5.925420,-0.337705,-2.729618],[-8.564346,-5.908581,-7.669136],[-2.348096,-2.508368,-8.899196],[4.336788,-1.320918,7.091061],[8.755053,-2.348844,-4.637872],[3.505638,4.327787,4.373514],[9.895428,-5.354069,-2.268356],[2.937107,-6.364708,-6.341146],[-8.725716,6.018832,-7.499767],[0.165435,1.657665,-8.165358],[-3.246954,-7.490056,0.413474]],[[1.256092,-2.325800,-1.506877],[5.174166,0.294232,4.904295],[-3.266662,9.458385,-9.920583],[6.375783,8.902929,-5.089585],[-8.693501,-3.123131,-9.523872],[-1.884922,-3.978654,-5.636961],[5.858083,-9.692476,6.129255],[2.806108,8.761761,3.921615],[-3.871287,2.024029,7.930216],[6.083870,-0.909279,9.279660],[0.961852,6.317574,-6.968699],[-7.655374,8.629896,-6.344835],[-5.635127,-2.276330,-2.829452],[-4.252567,-1.984145,-0.142600]]], dtype = "float64")#candidate|516|(2, 14, 3)|const|float64
bop_517 = relay.power(const_515.astype('float64'), const_516.astype('float64')) # shape=(2, 14, 3)
output = bop_517
output2 = bop_517
func_525 = relay.Function([], output)
mod['func_525'] = func_525
mod = relay.transform.InferType()(mod)
output = func_525()
func_526 = relay.Function([], output)
mutated_mod['func_526'] = func_526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_536 = func_525_call()
call_537 = func_525_call()
uop_542 = relay.sqrt(call_536.astype('float32')) # shape=(2, 14, 3)
uop_544 = relay.sqrt(call_537.astype('float32')) # shape=(2, 14, 3)
func_430_call = mod.get_global_var('func_430')
func_436_call = mutated_mod.get_global_var('func_436')
const_549 = relay.const(5.578138, dtype = "float32")#candidate|549|()|const|float32
var_550 = relay.var("var_550", dtype = "float32", shape = (280, 1))#candidate|550|(280, 1)|var|float32
const_551 = relay.const([10,10,9,-1,-7,1,-2,6,-3,3,9,-7,-6,1,9,6,1,3,-5,-1,1,-8,7,2,-1,9,7,-10,8,10,7,-9,1,-2,-6,-7,-5,3,-3,3,10,-5,-9,9,-6,5,5,4,5,10,-9,2,6,-7,10,4,-3,4,-5,9,2,-5,-9,-2,-4,-10,3,-8,-7,1,-6,-7,5,-1,6,10,-6,-6,-3,-3,-3,2,7,7,5,-1,-5,10,-4,10,2,8,4,-7,2,-4,5,3,7,5,-9,3,-7,-4,7,-10,4,1,4,5,-9,3,6,-3,-7,5,7,2,2,-4,9,-7,4,1,5,-3,6,6,3,6,-10,-10,8,10,7,10,9,-1,5,-2,7,-5,-3,-6,4,10,3,-10,1,3,-5,-6,-10,9,8,-8,-9,9,-3,2,-6,-1,2,2,-3,-1,-9,3,3,-7,-5,7,7,8,10,-9,-2,-7,-4,-8], dtype = "uint64")#candidate|551|(180,)|const|uint64
const_552 = relay.const([[-6.667819,-4.787249],[5.728123,-3.941644],[-3.460610,-5.370459],[-3.805377,-9.546560],[-0.819820,5.356671],[-4.027897,8.423207],[9.591469,4.996350],[-9.539798,8.828899],[-6.789191,-7.861656],[-4.342025,7.306129],[-1.914272,6.609877],[-7.494826,2.698102],[-8.598192,1.371931],[-2.996527,9.239626],[-9.441238,4.043123],[-0.016236,1.061626],[-5.806567,-0.969162],[-0.182775,-7.135364],[4.902532,9.912941],[8.117966,0.671605],[5.250120,-7.962865],[4.890187,3.981558],[-6.019461,-7.931468],[4.656825,-3.887757],[4.219259,-6.758124],[-8.881198,-8.576903],[-2.952823,2.812718],[-7.066595,4.727672],[-4.363928,3.024697],[-0.928254,5.916265],[-4.670511,2.237281],[8.472686,5.181508],[-8.779705,-6.494236],[-9.827069,2.976886],[-7.628150,-7.985407],[4.823113,-5.824274],[-2.777850,4.933362],[-2.196382,0.283865],[-6.757131,-3.070986],[-2.411716,-5.534401],[-4.123281,-2.572907],[-3.064880,1.275365],[-9.294929,5.054146],[-9.332204,1.019718],[-8.071895,2.882916],[1.970430,0.228634],[3.863530,3.294503],[9.032152,-7.913617],[-8.028221,6.061112],[-9.931221,2.341334],[-8.431062,-0.919826],[-0.577352,7.686460],[-0.050912,1.929729],[-0.596380,5.635744],[5.691501,1.178778],[1.694047,-0.021034],[-6.261541,-7.419469],[-0.768559,-2.408052],[-5.376990,9.328841],[-1.747158,0.707244],[1.436463,6.335618],[9.121734,3.589483],[0.511933,-6.623304],[3.422535,2.264957],[-7.484745,-4.473841],[1.415435,6.657043],[-9.210658,9.165629],[-6.525907,4.630100],[2.291654,3.824434],[-7.309474,7.279077],[4.457443,-4.120967],[-9.790420,6.416801],[3.486576,-6.286767],[-0.756958,-2.691548],[-2.044090,3.385326],[2.841431,0.845238],[6.811783,4.033108],[0.097134,-9.773158],[-6.112415,1.626288],[-8.353179,5.153005],[2.623985,-2.217818],[-9.291010,-2.006249],[-0.317245,1.901193],[-1.121304,2.196837],[6.190189,6.477860],[2.215556,7.817199],[-4.943388,4.055912],[6.664402,-3.453867],[-3.684163,-1.221632],[-3.601384,4.489173],[6.587404,-7.682266],[2.385230,1.139959],[-7.313120,-5.158638],[-3.370371,-7.029372],[-2.315136,6.053320],[-0.238140,-5.594406],[1.254358,8.774316],[1.323441,-2.582057],[0.841594,5.223138],[-1.526009,2.767011],[3.908907,9.578895],[-1.769589,5.189147],[3.837996,-6.051105],[-3.080395,-8.329753],[-0.980673,5.656768],[-5.018772,-0.122870],[-2.173995,7.025967],[-0.646980,-8.712560]], dtype = "float64")#candidate|552|(108, 2)|const|float64
call_548 = relay.TupleGetItem(func_430_call(relay.reshape(const_549.astype('float32'), []), relay.reshape(var_550.astype('float32'), [5, 7, 8]), relay.reshape(const_551.astype('uint64'), [180,]), relay.reshape(const_552.astype('float64'), [1, 216]), ), 7)
call_553 = relay.TupleGetItem(func_436_call(relay.reshape(const_549.astype('float32'), []), relay.reshape(var_550.astype('float32'), [5, 7, 8]), relay.reshape(const_551.astype('uint64'), [180,]), relay.reshape(const_552.astype('float64'), [1, 216]), ), 7)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
const_572 = relay.const([2.741361,2.043998,1.545111,7.829364,0.679486,7.500993,-7.489479,-5.738799,-7.597590,0.659008,8.884684,-2.736640,0.801282,-4.169614,3.168002,-9.011202,2.279491,2.663503,-9.610649,-4.936706,-7.103661,7.115492,7.465818,-9.071698,9.186517,0.267200,5.132377,9.551891,-9.481341,-2.976211,2.046419,-3.299184,-3.183972,0.918668,-0.296500,-1.907010], dtype = "float64")#candidate|572|(36,)|const|float64
call_571 = relay.TupleGetItem(func_225_call(relay.reshape(const_572.astype('float64'), [3, 12, 1]), relay.reshape(const_551.astype('uint64'), [3, 12, 5]), relay.reshape(const_551.astype('uint16'), [3, 12, 5]), relay.reshape(const_552.astype('float64'), [3, 12, 6]), ), 3)
call_573 = relay.TupleGetItem(func_230_call(relay.reshape(const_572.astype('float64'), [3, 12, 1]), relay.reshape(const_551.astype('uint64'), [3, 12, 5]), relay.reshape(const_551.astype('uint16'), [3, 12, 5]), relay.reshape(const_552.astype('float64'), [3, 12, 6]), ), 3)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_574 = func_525_call()
call_575 = func_525_call()
bop_577 = relay.maximum(uop_542.astype('int8'), relay.reshape(call_536.astype('int8'), relay.shape_of(uop_542))) # shape=(2, 14, 3)
bop_580 = relay.maximum(uop_544.astype('int8'), relay.reshape(call_537.astype('int8'), relay.shape_of(uop_544))) # shape=(2, 14, 3)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_581 = func_525_call()
call_582 = func_525_call()
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
call_609 = relay.TupleGetItem(func_225_call(relay.reshape(const_572.astype('float64'), [3, 12, 1]), relay.reshape(const_551.astype('uint64'), [3, 12, 5]), relay.reshape(const_551.astype('uint16'), [3, 12, 5]), relay.reshape(call_548.astype('float64'), [3, 12, 6]), ), 3)
call_610 = relay.TupleGetItem(func_230_call(relay.reshape(const_572.astype('float64'), [3, 12, 1]), relay.reshape(const_551.astype('uint64'), [3, 12, 5]), relay.reshape(const_551.astype('uint16'), [3, 12, 5]), relay.reshape(call_548.astype('float64'), [3, 12, 6]), ), 3)
bop_611 = relay.bitwise_and(uop_542.astype('uint64'), const_549.astype('uint64')) # shape=(2, 14, 3)
bop_614 = relay.bitwise_and(uop_544.astype('uint64'), const_549.astype('uint64')) # shape=(2, 14, 3)
output = relay.Tuple([call_548,var_550,const_551,const_552,call_571,const_572,call_574,bop_577,call_581,call_609,bop_611,])
output2 = relay.Tuple([call_553,var_550,const_551,const_552,call_573,const_572,call_575,bop_580,call_582,call_610,bop_614,])
func_617 = relay.Function([var_550,], output)
mod['func_617'] = func_617
mod = relay.transform.InferType()(mod)
var_618 = relay.var("var_618", dtype = "float32", shape = (280, 1))#candidate|618|(280, 1)|var|float32
output = func_617(var_618)
func_619 = relay.Function([var_618], output)
mutated_mod['func_619'] = func_619
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_653 = func_525_call()
call_654 = func_525_call()
output = relay.Tuple([call_653,])
output2 = relay.Tuple([call_654,])
func_665 = relay.Function([], output)
mod['func_665'] = func_665
mod = relay.transform.InferType()(mod)
output = func_665()
func_666 = relay.Function([], output)
mutated_mod['func_666'] = func_666
mutated_mod = relay.transform.InferType()(mutated_mod)
var_704 = relay.var("var_704", dtype = "int32", shape = (9, 7, 13))#candidate|704|(9, 7, 13)|var|int32
const_705 = relay.const([[[9,-5,6,-5,8,4,-8,-9,7,8,-2,-6,1],[4,-4,-5,-6,10,-10,-6,4,10,-9,8,-5,-2],[3,-3,-6,2,1,-2,2,1,-7,-2,-7,5,-1],[5,-9,-2,-5,-1,-2,-10,2,2,-4,-6,9,5],[2,3,-5,9,5,8,-6,2,2,3,-6,10,7],[4,-7,2,-1,5,3,-9,3,10,-6,9,6,6],[4,-5,-1,7,-8,-9,3,-4,-6,-7,-2,-10,9]],[[8,1,9,-9,8,-3,-8,-3,-1,-1,-5,10,7],[8,10,-9,5,4,7,10,3,-2,6,10,-4,-4],[5,10,6,1,5,8,-2,-4,4,-6,-9,10,6],[5,-8,-10,5,-6,5,-8,-7,-10,9,-8,10,-9],[-4,8,-6,3,-4,-8,-2,9,-2,-8,3,8,2],[4,1,2,-4,-9,-3,-6,-5,7,9,-3,-5,9],[-8,2,4,3,1,3,8,-8,2,10,-10,-5,3]],[[1,-10,7,-7,10,-7,9,2,5,-1,3,-1,-3],[9,2,-5,-1,-1,-4,9,2,-1,-6,-10,-3,6],[-8,-8,-7,-8,-1,10,-9,4,1,-9,9,-3,-1],[6,8,9,-8,-7,-5,2,10,-10,4,10,9,-10],[9,5,-10,5,4,4,-2,5,-7,-3,-10,4,1],[1,5,-8,7,-4,6,-5,-3,10,-9,3,3,-3],[-1,9,2,1,3,10,5,-5,3,-1,8,-2,-8]],[[2,-2,-6,-1,6,7,9,-7,8,-4,4,4,6],[7,-8,4,6,-5,1,-9,9,4,-8,10,-4,-10],[4,2,-5,-9,-3,2,-10,-4,-5,8,3,-4,3],[-6,8,7,-1,3,9,-10,4,-2,1,5,-10,-1],[-5,3,-1,-6,6,-1,4,4,6,4,6,-4,3],[-4,-4,-8,-2,-8,-10,1,10,5,-6,7,-3,-3],[8,-7,-9,-8,7,-4,8,3,-8,6,-6,4,-9]],[[5,-4,10,-6,-7,-7,-9,-10,5,-7,-6,3,-7],[-2,-3,1,-1,-6,9,8,-10,8,1,-4,-7,-7],[6,-6,10,-3,7,1,-1,8,1,-5,-3,10,-4],[-4,-5,-6,2,-5,8,-3,6,-2,3,6,-8,-6],[-5,-8,-3,9,-3,3,5,-8,-8,9,-9,10,2],[9,-8,-2,-3,9,3,6,-1,5,-6,2,-6,-7],[-1,-6,-2,5,-9,-10,-9,10,7,10,-6,-7,-8]],[[8,7,10,10,-10,-10,-2,-2,-3,3,5,-3,1],[1,-4,6,-4,7,2,-9,-2,9,-10,-8,4,-10],[1,-3,7,-10,-3,-4,1,3,9,-6,-1,-6,-8],[7,6,-8,-3,9,6,-10,8,-8,-5,10,10,-6],[-1,-5,-7,-10,2,-9,-10,6,10,5,-9,-6,-3],[-10,-2,-8,-9,5,-5,-8,-4,3,-5,-10,-4,4],[-9,10,7,-6,6,-6,-7,2,4,1,7,2,3]],[[-1,-8,-2,3,10,2,1,-8,-5,-5,-6,-7,9],[-3,9,4,4,-3,2,10,8,-5,-4,-5,9,5],[1,4,-9,-2,4,-6,-9,-9,-7,-2,-3,-3,2],[-5,9,8,-6,-1,-9,1,10,-4,-6,-1,-1,7],[10,2,-7,-4,-9,-6,3,7,-2,-7,-6,3,-1],[-5,7,-8,-2,-2,-7,5,7,10,9,-5,-8,5],[-1,-7,5,5,-4,3,-3,-4,9,6,-9,9,-6]],[[2,7,7,8,-2,-6,6,-2,-5,-4,-5,6,-1],[10,4,-6,-9,6,3,-9,-6,2,2,-3,-6,6],[9,5,-7,-2,10,-1,-3,4,-8,10,6,8,-5],[7,-7,5,4,-6,4,6,-7,4,2,7,10,8],[1,-6,-8,-10,-7,-8,4,4,3,-3,-6,4,4],[10,1,2,3,-10,4,-5,-2,1,-9,5,6,-2],[-6,10,8,-6,5,2,-9,-10,-10,-3,8,-10,1]],[[-8,-5,7,9,-3,-7,-7,-8,-4,-3,9,9,-8],[6,-5,5,-3,-6,-4,-10,-1,8,1,8,5,10],[-5,-6,10,-2,8,-10,2,1,-10,-4,8,-10,-8],[-4,10,-6,7,-7,-3,-1,10,10,-7,7,2,8],[-3,-10,-5,-5,10,-9,3,-1,-6,-7,-4,-8,10],[8,-7,3,-5,3,7,4,-9,-4,10,1,10,4],[-5,-6,-8,-6,-1,4,-1,-7,-5,8,5,-8,-9]]], dtype = "int32")#candidate|705|(9, 7, 13)|const|int32
bop_706 = relay.greater_equal(var_704.astype('bool'), relay.reshape(const_705.astype('bool'), relay.shape_of(var_704))) # shape=(9, 7, 13)
output = bop_706
output2 = bop_706
func_711 = relay.Function([var_704,], output)
mod['func_711'] = func_711
mod = relay.transform.InferType()(mod)
var_712 = relay.var("var_712", dtype = "int32", shape = (9, 7, 13))#candidate|712|(9, 7, 13)|var|int32
output = func_711(var_712)
func_713 = relay.Function([var_712], output)
mutated_mod['func_713'] = func_713
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_718 = relay.TupleGetItem(func_665_call(), 0)
call_719 = relay.TupleGetItem(func_666_call(), 0)
func_711_call = mod.get_global_var('func_711')
func_713_call = mutated_mod.get_global_var('func_713')
const_723 = relay.const([-3,5,-3,10,-4,5,10,9,9,-2,3,7,6,7,7,9,-3,6,7,6,-9,-7,1,2,10,-9,9,10,-8,-9,7,8,4,5,-10,-3,2,-7,-8,10,-2,-2,9,-6,-10,-5,-5,-4,5,-10,-10,3,5,-2,-8,2,5,2,-5,-2,-5,2,8,-9,-5,9,4,-7,3,-3,-4,-2,8,-3,-6,9,-10,1,9,2,-1,-9,-4,-3,6,9,-2,6,-8,-6,-4,4,-8,-3,-7,10,7,-2,-4,9,2,7,-10,5,-4,10,5,-1,1,9,8,-3,-9,-7,9,-2,-3,-6,-5,-8,-1,6,-4,-1,8,2,-9,10,-1,10,2,-2,2,7,8,-6,-4,7,7,3,-9,-1,2,-8,-10,-3,-10,-7,-3,-10,10,2,-8,1,10,-1,1,-9,7,3,6,10,-9,10,1,-4,8,4,6,1,1,5,8,-2,1,-2,1,3,-9,3,5,-9,-5,8,8,9,3,-9,10,-6,9,8,-8,-10,-3,6,-2,2,-8,3,2,-3,-8,6,6,-8,7,-4,6,1,1,-9,2,2,-2,6,-9,-6,5,-4,3,-7,10,5,-7,5,-6,3,-6,10,2,-9,-6,7,-9,2,4,2,3,10,-8,10,-1,-3,-9,-4,-8,-3,2,-6,2,-4,-9,10,6,2,7,7,4,-7,-3,-4,-6,7,-7,-8,1,5,8,2,7,9,3,-6,-6,-9,-3,-1,-10,-8,1,7,-8,4,10,-2,-9,5,-7,-8,-3,5,10,7,-6,8,-9,-3,-9,-6,2,-8,-9,2,1,10,-7,-9,10,-8,9,6,-2,8,6,10,2,-1,-10,-8,3,6,2,8,3,10,3,-1,-7,-8,-5,-2,-8,-7,-6,-3,2,10,5,7,3,10,-7,4,-4,-6,-5,-5,9,-3,-6,5,-6,-1,2,-8,9,-2,-3,-10,-9,3,3,6,9,-9,8,2,-9,-4,2,6,2,-8,4,-9,4,-6,-1,3,6,4,7,5,-8,5,-10,3,-8,-6,-9,-5,8,-2,-6,10,6,-5,1,-9,10,1,6,4,5,4,5,-8,3,-4,4,2,-10,-5,6,8,-9,-7,-2,-8,-1,10,-4,-10,8,-7,-10,4,-3,-8,4,-6,-6,-9,4,-3,10,10,2,2,-6,4,-5,3,-1,8,9,-10,4,1,-7,-2,10,2,4,3,2,-7,10,-4,2,-6,-5,-4,-8,-7,-1,-3,-3,-4,10,10,-7,-8,6,7,5,7,-10,8,-5,-2,-8,-7,1,-9,-9,2,3,-4,-3,6,-2,7,-5,-3,-4,7,1,2,-7,10,9,3,-1,2,8,1,3,4,-7,-10,-2,-2,3,5,-4,-6,-7,6,6,4,-7,3,-7,10,6,4,7,2,-9,-9,-2,-5,-2,10,10,-1,9,9,-1,-9,-8,-6,8,-4,5,-9,6,9,-4,7,3,10,-2,-7,7,1,-8,2,-4,-2,-10,5,4,6,-3,3,-3,-7,4,-7,1,-8,-4,6,7,-5,8,4,6,-9,5,6,-4,10,-8,-1,-6,7,-9,5,10,2,-4,9,8,-10,9,-10,10,3,8,4,-4,3,-5,-9,2,2,-10,5,-10,-1,-2,3,1,-7,-1,5,5,9,8,-6,1,-6,10,9,8,-6,10,-2,7,-2,-4,4,-6,-9,2,5,-3,6,-2,-1,6,-1,-9,9,-4,-4,9,8,-10,-8,-2,10,3,7,3,-6,-7,9,-3,2,1,-6,4,4,10,-10,6,-8,-6,-6,4,9,-2,7,-9,3,-7,-8,4,6,-5,-8,4,2,10,-8,2,6,-8,-9,6,-4,-2,3,-6,10,3,4,4,7,4,8,5,-9,-9,-1,-10,-7,9,6,8,9,-8,1,7,-5,5,8,-9,4,-5,4,-2,-8,2,-8,-4,4,-8,-3,2,9,-3,-9,3,-4,-10,6,1,3,-7,-6,8,2,-4,4,-3,3,-9,10,-6,2,5,8,-1,-1,-1,-1,6,6,8,-6,-2,-9,-1,-5,-5,5,-5,6,-5,4,2,7,-9,-8,5,-2,-2,10,-9,-4,-1,4,3,2,5,-6,-1,6,5,1,-9,7,-3,9,-1,8,-4,-8,2,-7,-3,-5,5,8,-9,-10,-1,2,-1,8,3,-3,-8], dtype = "int32")#candidate|723|(819,)|const|int32
call_722 = func_711_call(relay.reshape(const_723.astype('int32'), [9, 7, 13]))
call_724 = func_711_call(relay.reshape(const_723.astype('int32'), [9, 7, 13]))
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
var_728 = relay.var("var_728", dtype = "float64", shape = (36,))#candidate|728|(36,)|var|float64
var_729 = relay.var("var_729", dtype = "uint64", shape = (180,))#candidate|729|(180,)|var|uint64
const_730 = relay.const([[3.538761,4.788081,1.001755,8.877669,-5.534921,6.564614],[-4.742714,1.482907,2.106387,3.369985,-9.521717,-2.946075],[7.527929,5.650544,-9.195431,0.582787,5.070820,3.413982],[-7.122066,1.005111,-6.681123,-7.430593,-2.563766,-3.259119],[-2.413047,9.212551,-7.180594,7.516692,-7.844815,-0.034014],[-1.437496,-1.373326,-5.074764,-5.017761,5.680639,9.306423],[-3.193325,-3.074639,-6.767393,-5.434681,-4.019893,7.218403],[1.677491,-5.677927,-9.792093,2.040019,-6.087705,-3.182297],[7.351068,3.995938,5.750749,1.446451,0.359257,-0.867558],[-4.260067,-2.146964,-7.760347,9.482009,-3.472410,1.360812],[-5.424093,5.740001,8.643441,-1.469282,-5.142487,1.693858],[-1.887503,-5.671120,-8.086915,5.856537,6.499652,0.964859],[-6.073850,-4.423849,1.080822,3.698259,-7.540523,-1.441591],[-5.175264,-2.937389,4.169343,-5.898707,-4.764116,0.786737],[3.621690,0.749008,-5.660274,4.114183,-6.769871,-9.358397],[5.666192,0.620674,-9.968455,3.627770,-8.296835,-9.148276],[2.153874,-3.024300,5.335823,-4.608551,-3.724690,2.707659],[1.564244,9.670893,-3.988077,5.061420,0.903987,0.859042],[-1.959977,4.188072,0.060895,-2.822102,-0.883414,-1.573040],[-5.648139,3.898916,5.131058,-9.377038,4.448308,-9.931236],[5.498661,3.495324,-6.439911,-6.626713,-6.790884,-8.825950],[0.105672,-8.842063,4.639604,2.274416,-0.500370,-8.699807],[-4.783267,-4.673868,0.932072,5.986523,-6.780160,0.112071],[-6.622733,4.988854,9.084718,-5.785155,7.761425,0.293101],[8.762199,-8.267713,5.490963,0.139650,7.014069,3.324738],[-6.200434,4.661822,1.234702,-8.043658,0.340515,-0.809687],[3.460337,2.731208,-5.024186,2.230638,-3.966668,0.622536],[-3.341390,0.203579,-8.845416,-9.572543,8.246988,1.757564],[9.297005,-5.906265,9.595457,9.963677,9.288242,6.006298],[8.605735,-0.388083,6.485691,4.588774,-9.725157,8.239824],[3.810047,-4.313847,-1.393242,-4.467644,4.844355,-6.429008],[8.809156,6.093926,-0.743876,-1.178823,1.427089,1.922005],[-2.962505,-8.520878,1.736983,7.008523,-9.844429,-0.833233],[6.716355,-5.469814,1.010199,-2.212111,-1.480048,-1.487150],[-9.099705,3.138482,0.163135,-6.262843,3.876880,-1.553025],[2.233922,-9.662472,8.440958,-7.556298,3.758777,6.015875]], dtype = "float64")#candidate|730|(36, 6)|const|float64
call_727 = relay.TupleGetItem(func_225_call(relay.reshape(var_728.astype('float64'), [3, 12, 1]), relay.reshape(var_729.astype('uint64'), [3, 12, 5]), relay.reshape(var_729.astype('uint16'), [3, 12, 5]), relay.reshape(const_730.astype('float64'), [3, 12, 6]), ), 0)
call_731 = relay.TupleGetItem(func_230_call(relay.reshape(var_728.astype('float64'), [3, 12, 1]), relay.reshape(var_729.astype('uint64'), [3, 12, 5]), relay.reshape(var_729.astype('uint16'), [3, 12, 5]), relay.reshape(const_730.astype('float64'), [3, 12, 6]), ), 0)
uop_732 = relay.atanh(const_723.astype('float64')) # shape=(819,)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
call_738 = relay.TupleGetItem(func_225_call(relay.reshape(var_728.astype('float64'), [3, 12, 1]), relay.reshape(var_729.astype('uint64'), [3, 12, 5]), relay.reshape(var_729.astype('uint16'), [3, 12, 5]), relay.reshape(const_730.astype('float64'), [3, 12, 6]), ), 1)
call_739 = relay.TupleGetItem(func_230_call(relay.reshape(var_728.astype('float64'), [3, 12, 1]), relay.reshape(var_729.astype('uint64'), [3, 12, 5]), relay.reshape(var_729.astype('uint16'), [3, 12, 5]), relay.reshape(const_730.astype('float64'), [3, 12, 6]), ), 1)
var_741 = relay.var("var_741", dtype = "float32", shape = (3, 12, 5))#candidate|741|(3, 12, 5)|var|float32
bop_742 = relay.power(call_727.astype('float64'), var_741.astype('float64')) # shape=(3, 12, 5)
bop_745 = relay.power(call_731.astype('float64'), var_741.astype('float64')) # shape=(3, 12, 5)
uop_750 = relay.tan(const_730.astype('float64')) # shape=(36, 6)
output = relay.Tuple([call_718,call_722,var_728,var_729,uop_732,call_738,bop_742,uop_750,])
output2 = relay.Tuple([call_719,call_724,var_728,var_729,uop_732,call_739,bop_745,uop_750,])
func_761 = relay.Function([var_728,var_729,var_741,], output)
mod['func_761'] = func_761
mod = relay.transform.InferType()(mod)
mutated_mod['func_761'] = func_761
mutated_mod = relay.transform.InferType()(mutated_mod)
func_761_call = mutated_mod.get_global_var('func_761')
var_763 = relay.var("var_763", dtype = "float64", shape = (36,))#candidate|763|(36,)|var|float64
var_764 = relay.var("var_764", dtype = "uint64", shape = (180,))#candidate|764|(180,)|var|uint64
var_765 = relay.var("var_765", dtype = "float32", shape = (3, 12, 5))#candidate|765|(3, 12, 5)|var|float32
call_762 = func_761_call(var_763,var_764,var_765,)
output = call_762
func_766 = relay.Function([var_763,var_764,var_765,], output)
mutated_mod['func_766'] = func_766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_768 = relay.TupleGetItem(func_665_call(), 0)
call_769 = relay.TupleGetItem(func_666_call(), 0)
func_761_call = mod.get_global_var('func_761')
func_766_call = mutated_mod.get_global_var('func_766')
var_789 = relay.var("var_789", dtype = "float64", shape = (36,))#candidate|789|(36,)|var|float64
var_790 = relay.var("var_790", dtype = "uint64", shape = (180, 1))#candidate|790|(180, 1)|var|uint64
call_788 = relay.TupleGetItem(func_761_call(relay.reshape(var_789.astype('float64'), [36,]), relay.reshape(var_790.astype('uint64'), [180,]), relay.reshape(var_790.astype('float32'), [3, 12, 5]), ), 7)
call_791 = relay.TupleGetItem(func_766_call(relay.reshape(var_789.astype('float64'), [36,]), relay.reshape(var_790.astype('uint64'), [180,]), relay.reshape(var_790.astype('float32'), [3, 12, 5]), ), 7)
output = relay.Tuple([call_768,call_788,var_789,var_790,])
output2 = relay.Tuple([call_769,call_791,var_789,var_790,])
func_799 = relay.Function([var_789,var_790,], output)
mod['func_799'] = func_799
mod = relay.transform.InferType()(mod)
var_800 = relay.var("var_800", dtype = "float64", shape = (36,))#candidate|800|(36,)|var|float64
var_801 = relay.var("var_801", dtype = "uint64", shape = (180, 1))#candidate|801|(180, 1)|var|uint64
output = func_799(var_800,var_801,)
func_802 = relay.Function([var_800,var_801,], output)
mutated_mod['func_802'] = func_802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_886 = func_525_call()
call_887 = func_525_call()
output = relay.Tuple([call_886,])
output2 = relay.Tuple([call_887,])
func_888 = relay.Function([], output)
mod['func_888'] = func_888
mod = relay.transform.InferType()(mod)
output = func_888()
func_889 = relay.Function([], output)
mutated_mod['func_889'] = func_889
mutated_mod = relay.transform.InferType()(mutated_mod)
const_894 = relay.const([[[7,-4,-10,2,-5,-6,-3,8],[10,-10,-3,2,7,-4,7,10]],[[-5,6,-1,-1,1,7,-2,-5],[-8,7,-10,-3,-5,1,-9,5]],[[-7,-9,-9,5,2,7,-10,6],[-7,-9,4,-3,9,8,-9,1]],[[-7,-4,-5,-8,2,8,-10,-10],[-9,-4,-9,9,-5,7,3,-9]],[[2,-9,-2,-3,4,8,10,-1],[-5,2,-3,5,10,-1,-3,5]],[[2,4,1,-2,-3,-9,8,-9],[-4,-8,-2,7,6,8,8,7]],[[-5,6,10,-3,10,-3,-1,-3],[3,-3,6,-10,-10,4,-10,-8]],[[1,3,3,2,7,4,-10,-4],[-8,-10,9,-7,-8,6,1,5]],[[9,-3,5,8,1,-1,-6,-5],[-1,7,5,-10,-4,-3,2,6]],[[7,4,5,5,3,-8,-10,-3],[8,-3,-5,-7,1,5,9,5]]], dtype = "uint8")#candidate|894|(10, 2, 8)|const|uint8
const_895 = relay.const([[[8,-5,3,4,8,8,-8,-8],[2,5,-2,-8,-1,1,6,1]],[[4,-6,7,-5,-5,-8,-3,-4],[-10,3,-3,3,1,-5,9,-10]],[[3,2,-5,6,-1,-3,-3,-9],[5,3,2,-4,-1,9,-7,5]],[[-4,-2,7,1,4,-2,2,-8],[-3,6,8,-8,1,10,-8,-9]],[[-3,3,1,-6,1,-10,1,-1],[10,10,9,8,7,9,-3,8]],[[-1,6,9,7,-1,-3,8,7],[-1,-7,-8,10,2,-1,-2,-3]],[[-3,7,2,-10,-2,5,4,7],[10,-6,10,4,-7,-9,5,2]],[[-10,8,2,4,10,5,1,9],[-5,-10,1,6,-8,-7,-6,2]],[[7,-7,9,-4,-9,5,10,-1],[-9,1,-4,9,4,8,-4,-6]],[[-2,9,-2,-2,-3,-1,1,1],[5,-1,1,-3,-6,4,1,1]]], dtype = "uint8")#candidate|895|(10, 2, 8)|const|uint8
bop_896 = relay.logical_xor(const_894.astype('uint8'), relay.reshape(const_895.astype('uint8'), relay.shape_of(const_894))) # shape=(10, 2, 8)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_915 = func_525_call()
call_916 = func_525_call()
bop_924 = relay.bitwise_xor(bop_896.astype('uint8'), relay.reshape(const_895.astype('uint8'), relay.shape_of(bop_896))) # shape=(10, 2, 8)
output = relay.Tuple([call_915,bop_924,])
output2 = relay.Tuple([call_916,bop_924,])
func_929 = relay.Function([], output)
mod['func_929'] = func_929
mod = relay.transform.InferType()(mod)
mutated_mod['func_929'] = func_929
mutated_mod = relay.transform.InferType()(mutated_mod)
func_929_call = mutated_mod.get_global_var('func_929')
call_930 = func_929_call()
output = call_930
func_931 = relay.Function([], output)
mutated_mod['func_931'] = func_931
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_941 = relay.TupleGetItem(func_888_call(), 0)
call_942 = relay.TupleGetItem(func_889_call(), 0)
func_929_call = mod.get_global_var('func_929')
func_931_call = mutated_mod.get_global_var('func_931')
call_943 = relay.TupleGetItem(func_929_call(), 0)
call_944 = relay.TupleGetItem(func_931_call(), 0)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_945 = func_525_call()
call_946 = func_525_call()
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_951 = relay.TupleGetItem(func_888_call(), 0)
call_952 = relay.TupleGetItem(func_889_call(), 0)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_954 = relay.TupleGetItem(func_888_call(), 0)
call_955 = relay.TupleGetItem(func_889_call(), 0)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_958 = func_525_call()
call_959 = func_525_call()
func_929_call = mod.get_global_var('func_929')
func_931_call = mutated_mod.get_global_var('func_931')
call_961 = relay.TupleGetItem(func_929_call(), 1)
call_962 = relay.TupleGetItem(func_931_call(), 1)
bop_969 = relay.divide(call_943.astype('float64'), relay.reshape(call_945.astype('float64'), relay.shape_of(call_943))) # shape=(2, 14, 3)
bop_972 = relay.divide(call_944.astype('float64'), relay.reshape(call_946.astype('float64'), relay.shape_of(call_944))) # shape=(2, 14, 3)
bop_974 = relay.add(call_943.astype('uint64'), relay.reshape(call_954.astype('uint64'), relay.shape_of(call_943))) # shape=(2, 14, 3)
bop_977 = relay.add(call_944.astype('uint64'), relay.reshape(call_955.astype('uint64'), relay.shape_of(call_944))) # shape=(2, 14, 3)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
var_991 = relay.var("var_991", dtype = "float64", shape = (3, 12))#candidate|991|(3, 12)|var|float64
var_992 = relay.var("var_992", dtype = "uint64", shape = (90, 2))#candidate|992|(90, 2)|var|uint64
var_993 = relay.var("var_993", dtype = "float64", shape = (216,))#candidate|993|(216,)|var|float64
call_990 = relay.TupleGetItem(func_225_call(relay.reshape(var_991.astype('float64'), [3, 12, 1]), relay.reshape(var_992.astype('uint64'), [3, 12, 5]), relay.reshape(var_992.astype('uint16'), [3, 12, 5]), relay.reshape(var_993.astype('float64'), [3, 12, 6]), ), 2)
call_994 = relay.TupleGetItem(func_230_call(relay.reshape(var_991.astype('float64'), [3, 12, 1]), relay.reshape(var_992.astype('uint64'), [3, 12, 5]), relay.reshape(var_992.astype('uint16'), [3, 12, 5]), relay.reshape(var_993.astype('float64'), [3, 12, 6]), ), 2)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_1017 = func_525_call()
call_1018 = func_525_call()
output = relay.Tuple([call_941,call_951,call_958,call_961,bop_969,bop_974,call_990,var_991,var_992,var_993,call_1017,])
output2 = relay.Tuple([call_942,call_952,call_959,call_962,bop_972,bop_977,call_994,var_991,var_992,var_993,call_1018,])
func_1020 = relay.Function([var_991,var_992,var_993,], output)
mod['func_1020'] = func_1020
mod = relay.transform.InferType()(mod)
mutated_mod['func_1020'] = func_1020
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1020_call = mutated_mod.get_global_var('func_1020')
var_1022 = relay.var("var_1022", dtype = "float64", shape = (3, 12))#candidate|1022|(3, 12)|var|float64
var_1023 = relay.var("var_1023", dtype = "uint64", shape = (90, 2))#candidate|1023|(90, 2)|var|uint64
var_1024 = relay.var("var_1024", dtype = "float64", shape = (216,))#candidate|1024|(216,)|var|float64
call_1021 = func_1020_call(var_1022,var_1023,var_1024,)
output = call_1021
func_1025 = relay.Function([var_1022,var_1023,var_1024,], output)
mutated_mod['func_1025'] = func_1025
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_1047 = func_525_call()
call_1048 = func_525_call()
uop_1051 = relay.tan(call_1047.astype('float32')) # shape=(2, 14, 3)
uop_1053 = relay.tan(call_1048.astype('float32')) # shape=(2, 14, 3)
output = uop_1051
output2 = uop_1053
func_1058 = relay.Function([], output)
mod['func_1058'] = func_1058
mod = relay.transform.InferType()(mod)
mutated_mod['func_1058'] = func_1058
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1058_call = mutated_mod.get_global_var('func_1058')
call_1059 = func_1058_call()
output = call_1059
func_1060 = relay.Function([], output)
mutated_mod['func_1060'] = func_1060
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1133 = relay.var("var_1133", dtype = "float64", shape = (16, 11, 5))#candidate|1133|(16, 11, 5)|var|float64
uop_1134 = relay.asin(var_1133.astype('float64')) # shape=(16, 11, 5)
uop_1136 = relay.log2(uop_1134.astype('float64')) # shape=(16, 11, 5)
uop_1138 = relay.erf(var_1133.astype('float32')) # shape=(16, 11, 5)
output = relay.Tuple([uop_1136,uop_1138,])
output2 = relay.Tuple([uop_1136,uop_1138,])
func_1149 = relay.Function([var_1133,], output)
mod['func_1149'] = func_1149
mod = relay.transform.InferType()(mod)
mutated_mod['func_1149'] = func_1149
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1150 = relay.var("var_1150", dtype = "float64", shape = (16, 11, 5))#candidate|1150|(16, 11, 5)|var|float64
func_1149_call = mutated_mod.get_global_var('func_1149')
call_1151 = func_1149_call(var_1150)
output = call_1151
func_1152 = relay.Function([var_1150], output)
mutated_mod['func_1152'] = func_1152
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1168 = relay.var("var_1168", dtype = "float32", shape = (4, 2, 7))#candidate|1168|(4, 2, 7)|var|float32
uop_1169 = relay.atanh(var_1168.astype('float32')) # shape=(4, 2, 7)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1173 = relay.TupleGetItem(func_665_call(), 0)
call_1174 = relay.TupleGetItem(func_666_call(), 0)
var_1179 = relay.var("var_1179", dtype = "float32", shape = (4, 2, 7))#candidate|1179|(4, 2, 7)|var|float32
bop_1180 = relay.not_equal(var_1168.astype('bool'), relay.reshape(var_1179.astype('bool'), relay.shape_of(var_1168))) # shape=(4, 2, 7)
output = relay.Tuple([uop_1169,call_1173,bop_1180,])
output2 = relay.Tuple([uop_1169,call_1174,bop_1180,])
func_1194 = relay.Function([var_1168,var_1179,], output)
mod['func_1194'] = func_1194
mod = relay.transform.InferType()(mod)
mutated_mod['func_1194'] = func_1194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1194_call = mutated_mod.get_global_var('func_1194')
var_1196 = relay.var("var_1196", dtype = "float32", shape = (4, 2, 7))#candidate|1196|(4, 2, 7)|var|float32
var_1197 = relay.var("var_1197", dtype = "float32", shape = (4, 2, 7))#candidate|1197|(4, 2, 7)|var|float32
call_1195 = func_1194_call(var_1196,var_1197,)
output = call_1195
func_1198 = relay.Function([var_1196,var_1197,], output)
mutated_mod['func_1198'] = func_1198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_1219 = relay.TupleGetItem(func_888_call(), 0)
call_1220 = relay.TupleGetItem(func_889_call(), 0)
func_1149_call = mod.get_global_var('func_1149')
func_1152_call = mutated_mod.get_global_var('func_1152')
const_1234 = relay.const([-7.235895,-6.569612,-7.776306,3.964314,2.295629,-5.248791,-5.060440,8.962302,2.939320,2.454923,-5.756051,4.059617,-5.474736,-5.070493,6.733031,8.297966,2.918961,-1.033400,3.163952,7.220400,8.478857,7.678333,4.712782,-6.809178,-8.451638,-3.240594,0.680785,7.247978,-9.504390,3.644388,7.804350,-0.488659,4.269115,8.323078,-4.443970,0.940593,-4.697882,8.967816,5.625340,-1.114504,-2.474679,4.251614,-2.323657,9.600351,-1.308047,-9.201690,5.986772,-6.724116,5.905218,-3.263751,8.033949,-4.696481,-0.499427,5.797021,1.870777,-0.305426,-5.054847,1.203580,-8.641763,7.991100,2.521257,-5.895388,-4.647677,6.269259,-2.096670,6.708570,-2.637980,2.894400,-5.023021,-6.519742,-2.405468,2.167559,-0.129911,-2.073721,2.276453,4.387444,1.917557,5.169989,5.858231,-2.292955,-7.804908,1.313533,4.279353,-3.675230,6.504956,7.588738,7.813141,-5.885127,9.793490,-7.670903,-9.316588,4.870681,7.607877,-3.009173,-2.133870,7.036408,-6.148705,6.314680,9.162583,0.323947,-9.413150,1.332105,3.190146,-7.034093,-3.115309,2.678306,-8.490613,-8.032052,-8.021533,-3.167483,8.526634,2.287313,-7.565126,1.725447,-8.068696,-8.788253,2.879703,-8.414376,6.483614,0.648897,0.267667,2.967153,-2.768917,-7.152310,-9.094057,0.026978,-5.890794,6.897752,8.596782,-9.251138,-2.866594,-4.661492,-5.633163,-4.558000,0.889519,0.331785,1.889017,1.981663,2.317254,-1.463667,-2.499145,7.593759,-9.770398,-0.168819,-2.062152,-4.193972,4.720802,-7.797782,8.186668,-8.723464,6.285589,-5.354977,-7.254479,-3.697882,8.290465,3.040231,-4.091590,-4.004895,3.237990,-1.771191,7.445151,-6.410299,2.976995,5.531806,-4.518088,-8.088030,8.386576,-0.916861,-5.517002,3.212533,6.362238,5.925849,-0.564899,-7.960744,-5.323073,7.733419,5.074560,0.423124,-1.779806,-2.218286,-4.380569,-7.966708,6.450039,8.572440,3.424006,9.100331,9.637594,-2.963774,-5.428329,1.929195,4.150355,-4.099306,5.525851,-7.574295,-9.719879,-7.042545,1.161422,9.398581,1.560612,-7.789925,6.338209,0.303947,-5.318201,-8.753525,-4.411281,-4.619789,-7.842009,3.906817,-0.407520,-1.632980,-7.973756,4.058503,5.876946,-1.300079,5.543328,-4.437097,-7.426801,8.117047,7.362170,2.553088,9.038519,-5.443266,-7.429390,7.830322,5.825448,-2.252203,-8.736014,2.852426,-0.207960,-0.310226,-1.097828,-7.743037,-4.586283,3.025382,-5.259240,-2.798592,-7.444362,3.611525,-9.841442,1.104216,-9.729860,4.577233,9.635158,0.417515,-9.734427,5.059826,-6.596414,7.899882,0.384375,-6.785860,4.769368,-9.850743,7.080636,-6.268213,-3.063561,4.580604,1.038763,-0.806459,5.192667,-9.998704,9.305241,-9.492712,-4.967057,0.494320,6.857789,3.509017,-1.863760,-9.437204,9.221712,8.109521,7.459047,4.514994,7.174521,6.619516,4.232309,-3.559368,-4.248411,-2.163250,-7.372767,-8.463287,7.423216,-0.169291,1.192983,-9.936270,5.564407,1.611113,-6.020343,-0.535708,-6.375986,3.955264,0.808649,-0.921023,-0.646649,-2.904403,-2.046024,-1.020613,-7.068397,3.182744,-2.020026,6.269934,9.218966,-8.849876,1.153506,6.682215,-5.700952,1.195812,-1.081860,2.017140,-8.944580,7.277304,5.024266,-1.299280,-2.644186,5.881750,3.735716,5.512622,7.247024,5.468680,-3.461793,-7.758169,8.844149,-7.245198,-4.570814,-6.066476,-1.075248,9.122135,-8.159490,2.913713,-4.494694,8.045506,6.210207,-7.920658,-8.922840,5.984981,9.637104,1.271467,9.066676,-0.129171,-3.345280,-7.975340,7.679107,-4.785496,-8.604585,-0.906667,-7.541033,-4.400624,-1.807773,7.025965,-2.308947,1.066169,-7.198402,-7.457167,8.982993,2.105016,-2.263129,-3.379642,-6.191977,2.963512,-1.988398,0.062784,7.032384,1.581872,-4.574875,-5.115024,6.650200,-1.736294,-8.377778,-0.774622,-6.228620,5.503907,1.348912,-0.834478,-6.306188,-7.771393,1.739637,-0.239315,-9.270264,7.519177,-0.840137,8.854665,9.664344,9.512151,4.716521,5.145688,-4.788833,-1.461421,-7.369766,0.436606,-1.945582,-8.161348,7.860205,-1.933095,-9.697785,-5.347815,0.755895,-6.591295,-7.222907,-4.584152,8.607640,1.663642,8.032657,-6.861233,-6.267628,-6.917335,5.283619,-4.824576,6.081689,-5.969778,-5.395351,-5.793590,4.633073,7.379415,9.279593,5.371845,1.648238,-5.860825,-4.340054,6.138969,-7.929794,3.216981,-9.278743,-7.630192,-6.778652,4.599627,9.969514,-2.182245,-4.354299,-1.157078,8.718688,4.229398,-3.101493,9.975740,-5.998784,9.812905,1.812596,-6.896803,3.742157,5.007578,-0.106502,-8.133770,2.757520,-6.315014,-8.712903,3.241823,-1.766194,2.138112,-3.707318,0.937159,2.902125,0.691694,3.893677,-5.698494,-7.032839,-0.348533,-2.078118,-7.352062,9.204740,8.435412,-7.985455,2.679763,2.994609,3.553133,-6.695174,-2.517288,-8.115541,-9.464643,-1.008544,-4.764872,-8.397342,7.470838,4.388020,-2.879989,-2.150393,5.617331,-3.952500,1.470397,8.011680,2.961954,4.435807,3.681713,1.816399,3.576945,-4.387760,-9.298046,-1.130451,8.396006,-7.910198,-3.157750,0.056048,3.799185,-9.072234,-0.689492,1.263327,6.932450,8.746066,-1.456203,-4.409820,-8.581731,3.961856,-0.217258,-5.966983,-9.544445,5.956505,0.624804,-3.824588,7.819029,7.421163,-7.890008,0.493089,3.803640,-3.159140,-4.494693,8.008880,5.884367,7.688772,-0.222581,2.329149,-6.683626,1.332207,4.428878,-5.916770,3.841648,-4.528113,1.432656,2.047000,4.798041,-4.620971,3.145611,-6.780722,1.438425,-6.769643,-2.048376,-6.309088,-4.858735,-9.511314,3.522911,-4.824953,9.207577,-6.941191,1.813038,2.429847,0.178443,-9.280747,-4.067858,3.060129,-4.506895,4.320375,2.801545,-3.498569,-7.817598,8.912059,8.583189,-2.184460,9.277391,8.005158,-7.333845,4.450651,3.776564,-3.283462,-4.665386,2.349463,3.062972,3.963554,-0.656785,4.596703,1.951069,-7.756200,-1.181903,1.345217,1.160619,-7.409164,9.788949,7.451298,4.817101,-3.637136,8.077775,5.854604,8.370402,5.400382,-0.925248,-2.912769,1.642729,-0.907372,8.423904,6.229028,4.569182,-7.489337,4.202731,9.453025,-6.102897,0.967423,9.356344,-2.504139,0.674648,-9.431096,-6.066242,8.427705,6.194121,-0.568672,1.713133,3.323325,0.766752,-2.576126,5.132395,-5.337591,6.081057,3.423562,-5.643571,1.430991,0.596461,7.281461,-7.523295,8.624539,-6.345827,-7.100154,-2.349272,-9.942461,-2.866856,-3.497260,-8.910489,1.385735,-5.231177,-9.058332,-6.856157,8.137086,9.546017,-8.459937,9.031092,9.134938,1.481225,-7.074753,2.179540,4.271636,3.832189,9.161684,-0.273533,1.755931,4.468967,2.827974,-6.015727,2.721418,9.399280,1.130294,-7.086491,1.670153,4.955206,0.128316,-7.382959,-1.021894,-9.824243,-4.145407,-4.436294,-5.285045,6.511222,9.656348,-2.338924,-2.856098,-6.747900,-0.214177,-9.363878,-2.710009,9.974823,9.033898,1.411890,2.418749,3.069428,-7.265080,-1.283712,-4.471448,6.364152,5.966710,-7.870402,8.516258,6.340491,4.457479,6.402668,5.240121,7.013764,3.227717,-9.686322,9.412711,-1.890295,7.415477,-4.241660,-9.157558,-9.027416,0.857522,9.249284,5.858511,-8.584391,6.843522,2.362256,5.271818,2.447397,2.233474,1.947823,1.662975,-0.060878,-9.303560,-8.470035,-3.131197,-4.423003,-1.461502,0.979525,7.363641,-7.620709,4.304937,6.230730,6.871273,1.962895,0.213589,2.099080,-3.608154,9.103733,-5.397093,-6.362590,-6.966785,-2.644208,-1.753047,9.903671,0.345508,-5.477545,9.900667,9.993225,-7.996289,6.350227,-8.108519,1.953326,-9.297370,7.993454,-5.074958,-8.782055,5.343164,0.091731,-3.069961,7.626052,9.069506,-3.983109,3.286306,1.926315,1.757032,2.592382,7.548754,-5.474877,-8.450741,-1.309551,6.247504,0.808220,2.202669,8.106200,9.307985,1.955947,-5.605425,6.079120,-8.443441,-6.179220,0.293899,1.384643,-7.690322,5.774763,5.499037,9.068410,-0.925185,3.669518,-1.890821,9.893718,6.888139,-2.310085,-5.073739,-6.277073,-5.642881,-8.350572,-3.019891,-4.786201,-4.281446,4.794008,3.548181,-1.599790,-9.913416,2.080295,-5.927670,-0.391786,9.615961,-1.515555,3.254590,-4.552431,0.961029,6.430065,-5.292056,-0.448622,1.576810,1.613373,-0.035031,-3.191377,5.846366,4.352342,-8.078167,-3.078269,-9.411402,-3.370502,7.516481,6.577032,9.734567,-6.010520,-3.434510,-2.339826,6.811068,-3.495698,-9.181678,-2.547975,-8.186081,1.815413,4.670128,2.722529,-1.474757,3.925385,-8.013824,-2.181074,-0.801956,-8.108830,2.986127,-8.627671,-8.817020,4.051744,-8.363816,-3.876358,8.119867,0.441959,5.414380,1.712637,-5.866023,4.517332,9.334868,4.507094,2.976462,4.326049,-5.133069,4.901356,-7.292186,9.964511,-5.062038,-9.216355,-4.745848,-4.600536,-9.365751,7.245405,9.822377,1.092309,7.583562,-8.136412,-0.939616,1.073312,0.140884,7.658972,1.531264,-2.118676,0.692409,-0.971211,9.405764,3.907480,-5.214781,-8.570329,-8.629394,-1.535543,-6.715450,-6.301711,-3.202033,-9.748085,-7.176747,-4.042451,-6.258659,4.916806,1.542284,6.941116,-4.959970,-6.793727,-9.489456,-1.272186,-6.853738,-3.254095], dtype = "float64")#candidate|1234|(880,)|const|float64
call_1233 = relay.TupleGetItem(func_1149_call(relay.reshape(const_1234.astype('float64'), [16, 11, 5])), 0)
call_1235 = relay.TupleGetItem(func_1152_call(relay.reshape(const_1234.astype('float64'), [16, 11, 5])), 0)
uop_1239 = relay.log(const_1234.astype('float32')) # shape=(880,)
output = relay.Tuple([call_1219,call_1233,uop_1239,])
output2 = relay.Tuple([call_1220,call_1235,uop_1239,])
func_1255 = relay.Function([], output)
mod['func_1255'] = func_1255
mod = relay.transform.InferType()(mod)
output = func_1255()
func_1256 = relay.Function([], output)
mutated_mod['func_1256'] = func_1256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_929_call = mod.get_global_var('func_929')
func_931_call = mutated_mod.get_global_var('func_931')
call_1289 = relay.TupleGetItem(func_929_call(), 1)
call_1290 = relay.TupleGetItem(func_931_call(), 1)
output = relay.Tuple([call_1289,])
output2 = relay.Tuple([call_1290,])
func_1297 = relay.Function([], output)
mod['func_1297'] = func_1297
mod = relay.transform.InferType()(mod)
output = func_1297()
func_1298 = relay.Function([], output)
mutated_mod['func_1298'] = func_1298
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1310 = relay.var("var_1310", dtype = "bool", shape = (13, 7, 1))#candidate|1310|(13, 7, 1)|var|bool
var_1311 = relay.var("var_1311", dtype = "bool", shape = (13, 7, 8))#candidate|1311|(13, 7, 8)|var|bool
bop_1312 = relay.logical_and(var_1310.astype('bool'), var_1311.astype('bool')) # shape=(13, 7, 8)
output = bop_1312
output2 = bop_1312
func_1322 = relay.Function([var_1310,var_1311,], output)
mod['func_1322'] = func_1322
mod = relay.transform.InferType()(mod)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mutated_mod.get_global_var('func_1322')
var_1324 = relay.var("var_1324", dtype = "bool", shape = (13, 7, 1))#candidate|1324|(13, 7, 1)|var|bool
var_1325 = relay.var("var_1325", dtype = "bool", shape = (13, 7, 8))#candidate|1325|(13, 7, 8)|var|bool
call_1323 = func_1322_call(var_1324,var_1325,)
output = call_1323
func_1326 = relay.Function([var_1324,var_1325,], output)
mutated_mod['func_1326'] = func_1326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1328 = relay.TupleGetItem(func_665_call(), 0)
call_1329 = relay.TupleGetItem(func_666_call(), 0)
output = call_1328
output2 = call_1329
func_1330 = relay.Function([], output)
mod['func_1330'] = func_1330
mod = relay.transform.InferType()(mod)
output = func_1330()
func_1331 = relay.Function([], output)
mutated_mod['func_1331'] = func_1331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_1347 = relay.TupleGetItem(func_888_call(), 0)
call_1348 = relay.TupleGetItem(func_889_call(), 0)
uop_1357 = relay.cosh(call_1347.astype('float64')) # shape=(2, 14, 3)
uop_1359 = relay.cosh(call_1348.astype('float64')) # shape=(2, 14, 3)
output = relay.Tuple([uop_1357,])
output2 = relay.Tuple([uop_1359,])
func_1362 = relay.Function([], output)
mod['func_1362'] = func_1362
mod = relay.transform.InferType()(mod)
mutated_mod['func_1362'] = func_1362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1362_call = mutated_mod.get_global_var('func_1362')
call_1363 = func_1362_call()
output = call_1363
func_1364 = relay.Function([], output)
mutated_mod['func_1364'] = func_1364
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1476 = relay.TupleGetItem(func_665_call(), 0)
call_1477 = relay.TupleGetItem(func_666_call(), 0)
uop_1478 = relay.asinh(call_1476.astype('float64')) # shape=(2, 14, 3)
uop_1480 = relay.asinh(call_1477.astype('float64')) # shape=(2, 14, 3)
output = relay.Tuple([uop_1478,])
output2 = relay.Tuple([uop_1480,])
func_1482 = relay.Function([], output)
mod['func_1482'] = func_1482
mod = relay.transform.InferType()(mod)
mutated_mod['func_1482'] = func_1482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1482_call = mutated_mod.get_global_var('func_1482')
call_1483 = func_1482_call()
output = call_1483
func_1484 = relay.Function([], output)
mutated_mod['func_1484'] = func_1484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_1512 = relay.TupleGetItem(func_665_call(), 0)
call_1513 = relay.TupleGetItem(func_666_call(), 0)
output = relay.Tuple([call_1512,])
output2 = relay.Tuple([call_1513,])
func_1517 = relay.Function([], output)
mod['func_1517'] = func_1517
mod = relay.transform.InferType()(mod)
mutated_mod['func_1517'] = func_1517
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1517_call = mutated_mod.get_global_var('func_1517')
call_1518 = func_1517_call()
output = call_1518
func_1519 = relay.Function([], output)
mutated_mod['func_1519'] = func_1519
mutated_mod = relay.transform.InferType()(mutated_mod)
func_929_call = mod.get_global_var('func_929')
func_931_call = mutated_mod.get_global_var('func_931')
call_1542 = relay.TupleGetItem(func_929_call(), 1)
call_1543 = relay.TupleGetItem(func_931_call(), 1)
var_1544 = relay.var("var_1544", dtype = "uint8", shape = (10, 2, 8))#candidate|1544|(10, 2, 8)|var|uint8
bop_1545 = relay.greater_equal(call_1542.astype('bool'), relay.reshape(var_1544.astype('bool'), relay.shape_of(call_1542))) # shape=(10, 2, 8)
bop_1548 = relay.greater_equal(call_1543.astype('bool'), relay.reshape(var_1544.astype('bool'), relay.shape_of(call_1543))) # shape=(10, 2, 8)
func_1194_call = mod.get_global_var('func_1194')
func_1198_call = mutated_mod.get_global_var('func_1198')
var_1575 = relay.var("var_1575", dtype = "float32", shape = (56,))#candidate|1575|(56,)|var|float32
call_1574 = relay.TupleGetItem(func_1194_call(relay.reshape(var_1575.astype('float32'), [4, 2, 7]), relay.reshape(var_1575.astype('float32'), [4, 2, 7]), ), 0)
call_1576 = relay.TupleGetItem(func_1198_call(relay.reshape(var_1575.astype('float32'), [4, 2, 7]), relay.reshape(var_1575.astype('float32'), [4, 2, 7]), ), 0)
bop_1603 = relay.add(call_1574.astype('float32'), relay.reshape(var_1575.astype('float32'), relay.shape_of(call_1574))) # shape=(4, 2, 7)
bop_1606 = relay.add(call_1576.astype('float32'), relay.reshape(var_1575.astype('float32'), relay.shape_of(call_1576))) # shape=(4, 2, 7)
output = relay.Tuple([bop_1545,bop_1603,])
output2 = relay.Tuple([bop_1548,bop_1606,])
func_1608 = relay.Function([var_1544,var_1575,], output)
mod['func_1608'] = func_1608
mod = relay.transform.InferType()(mod)
mutated_mod['func_1608'] = func_1608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1608_call = mutated_mod.get_global_var('func_1608')
var_1610 = relay.var("var_1610", dtype = "uint8", shape = (10, 2, 8))#candidate|1610|(10, 2, 8)|var|uint8
var_1611 = relay.var("var_1611", dtype = "float32", shape = (56,))#candidate|1611|(56,)|var|float32
call_1609 = func_1608_call(var_1610,var_1611,)
output = call_1609
func_1612 = relay.Function([var_1610,var_1611,], output)
mutated_mod['func_1612'] = func_1612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_1685 = relay.TupleGetItem(func_1517_call(), 0)
call_1686 = relay.TupleGetItem(func_1519_call(), 0)
uop_1696 = relay.erf(call_1685.astype('float64')) # shape=(2, 14, 3)
uop_1698 = relay.erf(call_1686.astype('float64')) # shape=(2, 14, 3)
bop_1699 = relay.multiply(uop_1696.astype('uint8'), relay.reshape(call_1685.astype('uint8'), relay.shape_of(uop_1696))) # shape=(2, 14, 3)
bop_1702 = relay.multiply(uop_1698.astype('uint8'), relay.reshape(call_1686.astype('uint8'), relay.shape_of(uop_1698))) # shape=(2, 14, 3)
func_761_call = mod.get_global_var('func_761')
func_766_call = mutated_mod.get_global_var('func_766')
var_1705 = relay.var("var_1705", dtype = "float64", shape = (36,))#candidate|1705|(36,)|var|float64
const_1706 = relay.const([6,1,-10,5,2,-1,-1,-1,-6,-10,9,-10,-10,5,4,-3,1,-8,4,-5,1,-5,7,-3,-10,-7,10,5,-8,-6,-2,3,-4,6,-4,4,-7,10,-4,-10,-7,1,-6,-9,-9,-9,3,-4,-4,-5,-3,6,8,5,-8,-6,2,2,6,-6,-6,3,8,-8,-8,-1,-4,1,4,5,1,-6,-9,-2,-10,9,3,7,9,-4,-8,10,-3,-5,-8,-6,4,-3,10,7,4,-6,-7,-8,6,-5,-6,-8,7,5,-6,6,3,-2,-5,-3,-6,-7,1,1,-9,4,1,-6,9,-6,10,-4,1,8,-4,6,1,5,1,1,-2,5,9,4,1,-3,-3,-8,3,-10,-6,-9,10,-10,9,10,8,-5,-7,7,10,-10,6,-9,3,-6,-6,7,10,-8,9,-10,-1,4,-3,-7,10,6,-7,-5,-4,9,-7,-7,-6,-5,1,1,-10,2,-5,-4,8,1], dtype = "uint64")#candidate|1706|(180,)|const|uint64
call_1704 = relay.TupleGetItem(func_761_call(relay.reshape(var_1705.astype('float64'), [36,]), relay.reshape(const_1706.astype('uint64'), [180,]), relay.reshape(const_1706.astype('float32'), [3, 12, 5]), ), 5)
call_1707 = relay.TupleGetItem(func_766_call(relay.reshape(var_1705.astype('float64'), [36,]), relay.reshape(const_1706.astype('uint64'), [180,]), relay.reshape(const_1706.astype('float32'), [3, 12, 5]), ), 5)
bop_1709 = relay.logical_and(uop_1696.astype('bool'), relay.reshape(call_1685.astype('bool'), relay.shape_of(uop_1696))) # shape=(2, 14, 3)
bop_1712 = relay.logical_and(uop_1698.astype('bool'), relay.reshape(call_1686.astype('bool'), relay.shape_of(uop_1698))) # shape=(2, 14, 3)
uop_1714 = relay.rsqrt(bop_1709.astype('float32')) # shape=(2, 14, 3)
uop_1716 = relay.rsqrt(bop_1712.astype('float32')) # shape=(2, 14, 3)
uop_1718 = relay.cos(bop_1699.astype('float64')) # shape=(2, 14, 3)
uop_1720 = relay.cos(bop_1702.astype('float64')) # shape=(2, 14, 3)
bop_1723 = relay.bitwise_or(uop_1714.astype('int64'), relay.reshape(uop_1696.astype('int64'), relay.shape_of(uop_1714))) # shape=(2, 14, 3)
bop_1726 = relay.bitwise_or(uop_1716.astype('int64'), relay.reshape(uop_1698.astype('int64'), relay.shape_of(uop_1716))) # shape=(2, 14, 3)
output = relay.Tuple([call_1704,var_1705,const_1706,uop_1718,bop_1723,])
output2 = relay.Tuple([call_1707,var_1705,const_1706,uop_1720,bop_1726,])
func_1734 = relay.Function([var_1705,], output)
mod['func_1734'] = func_1734
mod = relay.transform.InferType()(mod)
var_1735 = relay.var("var_1735", dtype = "float64", shape = (36,))#candidate|1735|(36,)|var|float64
output = func_1734(var_1735)
func_1736 = relay.Function([var_1735], output)
mutated_mod['func_1736'] = func_1736
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1758 = relay.var("var_1758", dtype = "float64", shape = (14, 12, 9))#candidate|1758|(14, 12, 9)|var|float64
uop_1759 = relay.atan(var_1758.astype('float64')) # shape=(14, 12, 9)
bop_1779 = relay.subtract(var_1758.astype('uint64'), relay.reshape(uop_1759.astype('uint64'), relay.shape_of(var_1758))) # shape=(14, 12, 9)
output = bop_1779
output2 = bop_1779
func_1786 = relay.Function([var_1758,], output)
mod['func_1786'] = func_1786
mod = relay.transform.InferType()(mod)
mutated_mod['func_1786'] = func_1786
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1787 = relay.var("var_1787", dtype = "float64", shape = (14, 12, 9))#candidate|1787|(14, 12, 9)|var|float64
func_1786_call = mutated_mod.get_global_var('func_1786')
call_1788 = func_1786_call(var_1787)
output = call_1788
func_1789 = relay.Function([var_1787], output)
mutated_mod['func_1789'] = func_1789
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1058_call = mod.get_global_var('func_1058')
func_1060_call = mutated_mod.get_global_var('func_1060')
call_1839 = func_1058_call()
call_1840 = func_1058_call()
func_1786_call = mod.get_global_var('func_1786')
func_1789_call = mutated_mod.get_global_var('func_1789')
var_1878 = relay.var("var_1878", dtype = "float64", shape = (1512,))#candidate|1878|(1512,)|var|float64
call_1877 = func_1786_call(relay.reshape(var_1878.astype('float64'), [14, 12, 9]))
call_1879 = func_1786_call(relay.reshape(var_1878.astype('float64'), [14, 12, 9]))
output = relay.Tuple([call_1839,call_1877,var_1878,])
output2 = relay.Tuple([call_1840,call_1879,var_1878,])
func_1886 = relay.Function([var_1878,], output)
mod['func_1886'] = func_1886
mod = relay.transform.InferType()(mod)
var_1887 = relay.var("var_1887", dtype = "float64", shape = (1512,))#candidate|1887|(1512,)|var|float64
output = func_1886(var_1887)
func_1888 = relay.Function([var_1887], output)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_929_call = mod.get_global_var('func_929')
func_931_call = mutated_mod.get_global_var('func_931')
call_1958 = relay.TupleGetItem(func_929_call(), 0)
call_1959 = relay.TupleGetItem(func_931_call(), 0)
func_430_call = mod.get_global_var('func_430')
func_436_call = mutated_mod.get_global_var('func_436')
const_1974 = relay.const(-3.284285, dtype = "float32")#candidate|1974|()|const|float32
var_1975 = relay.var("var_1975", dtype = "float32", shape = (70, 4))#candidate|1975|(70, 4)|var|float32
const_1976 = relay.const([3,-9,-5,7,-9,-8,5,7,-6,-10,-2,-3,3,-10,-6,-5,-10,-9,1,8,2,3,7,-1,-7,-4,-3,1,-8,7,8,5,10,5,-10,5,7,1,10,-5,-2,5,7,5,9,-1,8,6,-10,1,-4,-1,-6,2,-6,-10,-7,-8,-3,4,-5,-10,3,-10,9,-10,-10,3,-5,10,4,-2,9,7,-2,-5,-8,-1,4,-3,-5,-5,7,-10,3,-4,4,-7,-7,-4,-9,-8,-3,-9,2,-10,-8,3,3,8,5,-4,-9,9,-9,-6,1,5,-5,-1,-10,-6,-7,4,4,7,-5,8,4,-1,-10,1,-3,5,3,-6,8,1,-3,-5,-6,-6,-5,-4,-2,2,-2,-5,-7,4,8,-3,4,-2,-9,-3,1,-4,4,5,-1,-9,-8,-9,-5,-9,4,1,-5,6,2,-9,-3,-9,-8,-4,-1,-5,7,8,-8,-7,8,-4,-1,-7,2,-5,-8,1], dtype = "uint64")#candidate|1976|(180,)|const|uint64
const_1977 = relay.const([2.145509,2.783517,5.698508,3.517302,1.778930,-1.153457,-0.506327,-2.023677,-9.342302,6.578811,4.915881,-3.615459,-5.586360,-9.128116,3.999346,-9.731206,9.023511,2.813178,9.244946,0.520810,-8.894129,-0.067533,1.677175,-2.990156,2.033362,-2.251038,9.154486,7.520871,0.057734,8.715165,-5.283479,2.677551,-3.676523,-1.393808,3.552448,-1.615355,5.594561,-9.193449,7.392886,2.184152,9.350929,2.732974,-5.404911,-2.345644,-3.843817,-8.637605,1.089196,-3.497722,-0.021307,2.989071,2.821997,6.360268,-1.295050,0.323447,9.429487,-4.616819,7.092660,0.871424,-1.909284,4.221704,-5.037905,4.676736,3.491412,9.713641,3.475178,6.419219,-4.341480,1.002637,1.448086,-2.568038,4.024825,8.388608,-5.957135,5.583565,-7.684219,3.341170,-4.432589,9.665854,-7.933586,-3.706461,5.320173,-5.856518,-0.866014,5.916396,4.362771,-7.405731,-0.783120,9.176312,5.781088,-3.731209,3.901611,-3.235409,-3.987891,6.778659,-3.032254,-8.685041,7.010442,6.978242,7.749298,7.185726,-2.151488,4.095140,0.272657,9.039762,0.849609,2.073118,7.748897,9.368402,4.873335,-1.713469,-6.369249,9.204927,-3.460511,7.567352,0.001540,-6.120267,8.764864,7.246102,-4.746253,6.261751,-8.663684,-3.706925,-7.351217,1.141358,-0.953648,4.753172,2.855062,-3.276201,5.004268,3.131249,8.706468,-1.829988,3.411718,3.976119,-5.821694,-3.800469,5.556288,-2.766538,-4.156984,3.298025,8.866902,8.709807,-3.727007,-2.203194,0.311488,-5.269377,4.588383,7.175410,-8.188197,-0.289673,8.149798,7.702206,8.573650,-6.128261,-3.837459,-6.117418,-5.971364,-6.074281,-9.620396,-3.369361,-4.248762,-8.388257,8.795760,-8.954341,-4.021142,-8.385622,9.512840,9.242560,9.487148,-9.422449,8.181269,-2.789951,-7.950940,-8.309408,3.750039,0.747914,-8.279915,-8.446890,4.941923,1.426119,2.460808,-8.992975,-1.966917,-3.053278,9.261518,0.978558,5.358311,1.002253,-1.568835,-2.008158,-4.483785,4.197724,6.201245,4.808998,-9.693038,8.201287,-7.922686,0.431643,9.109741,2.675869,-5.528005,2.407848,-0.654115,-4.554858,0.286321,-5.594115,-4.782392,-1.987012,8.103254,-9.629725,-0.576872,-3.930939,1.410084,6.161437,6.237188,-1.893140], dtype = "float64")#candidate|1977|(216,)|const|float64
call_1973 = relay.TupleGetItem(func_430_call(relay.reshape(const_1974.astype('float32'), []), relay.reshape(var_1975.astype('float32'), [5, 7, 8]), relay.reshape(const_1976.astype('uint64'), [180,]), relay.reshape(const_1977.astype('float64'), [1, 216]), ), 4)
call_1978 = relay.TupleGetItem(func_436_call(relay.reshape(const_1974.astype('float32'), []), relay.reshape(var_1975.astype('float32'), [5, 7, 8]), relay.reshape(const_1976.astype('uint64'), [180,]), relay.reshape(const_1977.astype('float64'), [1, 216]), ), 4)
output = relay.Tuple([call_1958,call_1973,const_1974,var_1975,const_1976,const_1977,])
output2 = relay.Tuple([call_1959,call_1978,const_1974,var_1975,const_1976,const_1977,])
func_1983 = relay.Function([var_1975,], output)
mod['func_1983'] = func_1983
mod = relay.transform.InferType()(mod)
var_1984 = relay.var("var_1984", dtype = "float32", shape = (70, 4))#candidate|1984|(70, 4)|var|float32
output = func_1983(var_1984)
func_1985 = relay.Function([var_1984], output)
mutated_mod['func_1985'] = func_1985
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2022 = relay.const([[[5],[-5],[-4],[-5],[3],[-8]],[[-7],[-10],[-2],[-6],[2],[8]],[[1],[10],[-6],[3],[10],[-2]],[[3],[7],[-1],[10],[1],[2]]], dtype = "int8")#candidate|2022|(4, 6, 1)|const|int8
const_2023 = relay.const([[[-4,6,-2,-3],[6,-5,1,-7],[10,-2,7,-4],[-5,6,-10,7],[-3,-10,-10,7],[-10,-7,8,4]],[[5,6,3,-8],[7,-6,-6,-3],[-6,4,-3,9],[5,-4,9,4],[-6,-7,-2,-7],[-9,-8,-8,6]],[[3,7,2,3],[4,-2,-7,-9],[7,-4,-1,10],[6,6,10,-7],[3,10,9,-7],[-1,6,-5,3]],[[-10,-3,-9,-10],[-2,10,-10,4],[8,1,9,10],[6,10,-10,-5],[9,3,2,5],[-10,3,-10,3]]], dtype = "int8")#candidate|2023|(4, 6, 4)|const|int8
bop_2024 = relay.minimum(const_2022.astype('int8'), const_2023.astype('int8')) # shape=(4, 6, 4)
bop_2027 = relay.less_equal(const_2022.astype('bool'), bop_2024.astype('bool')) # shape=(4, 6, 4)
output = bop_2027
output2 = bop_2027
func_2047 = relay.Function([], output)
mod['func_2047'] = func_2047
mod = relay.transform.InferType()(mod)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2047_call = mutated_mod.get_global_var('func_2047')
call_2048 = func_2047_call()
output = call_2048
func_2049 = relay.Function([], output)
mutated_mod['func_2049'] = func_2049
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1331_call = mutated_mod.get_global_var('func_1331')
call_2061 = func_1330_call()
call_2062 = func_1330_call()
const_2067 = relay.const([[[2.425263,3.445740,3.401806],[-5.389749,2.344184,-1.406034],[-4.342557,-4.907450,5.158086],[-5.663418,-5.032549,9.435220],[-3.985137,6.921085,8.033955],[2.918394,-6.239935,-1.809917],[-5.819267,3.462703,-4.970772],[-3.791878,-5.791854,-3.857184],[-9.147121,3.221118,4.036153],[-6.645931,-5.157164,-7.102851],[0.819699,-3.645686,-7.425547],[6.292127,3.431434,-0.946957],[-4.634492,-6.979545,8.199060],[-2.099666,2.102069,5.633260]],[[-8.153867,6.977653,8.085825],[2.385166,1.317126,-4.590923],[-3.835204,-1.105610,4.764785],[-2.097093,7.824710,-2.649140],[2.827262,5.464601,-2.542543],[6.693866,-8.291490,7.039741],[-2.864590,-7.716806,-1.129876],[1.655659,-2.441087,-8.572498],[-1.795723,-5.619710,-2.777318],[5.249972,2.764967,-0.212594],[2.134669,7.146348,-5.581622],[2.095510,9.200957,-8.546370],[-6.152591,-1.211415,-6.209273],[-7.049701,0.022661,-0.412418]]], dtype = "float64")#candidate|2067|(2, 14, 3)|const|float64
bop_2068 = relay.logical_xor(call_2061.astype('uint32'), relay.reshape(const_2067.astype('uint32'), relay.shape_of(call_2061))) # shape=(2, 14, 3)
bop_2071 = relay.logical_xor(call_2062.astype('uint32'), relay.reshape(const_2067.astype('uint32'), relay.shape_of(call_2062))) # shape=(2, 14, 3)
output = relay.Tuple([bop_2068,])
output2 = relay.Tuple([bop_2071,])
func_2086 = relay.Function([], output)
mod['func_2086'] = func_2086
mod = relay.transform.InferType()(mod)
mutated_mod['func_2086'] = func_2086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2086_call = mutated_mod.get_global_var('func_2086')
call_2087 = func_2086_call()
output = call_2087
func_2088 = relay.Function([], output)
mutated_mod['func_2088'] = func_2088
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_2139 = relay.TupleGetItem(func_665_call(), 0)
call_2140 = relay.TupleGetItem(func_666_call(), 0)
output = relay.Tuple([call_2139,])
output2 = relay.Tuple([call_2140,])
func_2160 = relay.Function([], output)
mod['func_2160'] = func_2160
mod = relay.transform.InferType()(mod)
output = func_2160()
func_2161 = relay.Function([], output)
mutated_mod['func_2161'] = func_2161
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_2172 = func_525_call()
call_2173 = func_525_call()
output = call_2172
output2 = call_2173
func_2174 = relay.Function([], output)
mod['func_2174'] = func_2174
mod = relay.transform.InferType()(mod)
output = func_2174()
func_2175 = relay.Function([], output)
mutated_mod['func_2175'] = func_2175
mutated_mod = relay.transform.InferType()(mutated_mod)
func_888_call = mod.get_global_var('func_888')
func_889_call = mutated_mod.get_global_var('func_889')
call_2199 = relay.TupleGetItem(func_888_call(), 0)
call_2200 = relay.TupleGetItem(func_889_call(), 0)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
var_2204 = relay.var("var_2204", dtype = "float64", shape = (1512,))#candidate|2204|(1512,)|var|float64
call_2203 = relay.TupleGetItem(func_1886_call(relay.reshape(var_2204.astype('float64'), [1512,])), 1)
call_2205 = relay.TupleGetItem(func_1888_call(relay.reshape(var_2204.astype('float64'), [1512,])), 1)
uop_2218 = relay.sinh(call_2199.astype('float32')) # shape=(2, 14, 3)
uop_2220 = relay.sinh(call_2200.astype('float32')) # shape=(2, 14, 3)
func_1149_call = mod.get_global_var('func_1149')
func_1152_call = mutated_mod.get_global_var('func_1152')
const_2224 = relay.const([[-6.055259,-4.550484,-9.690613,1.254429,-7.550898,3.651265,-2.549982,8.138739,4.465991,-2.506950,-9.052853,-3.741141,-8.429363,2.183121,3.119091,2.883031,9.961698,2.402430,9.893655,-4.824030,7.100305,-3.841062,0.964288,-0.284426,-1.353653,3.836456,6.155967,-8.957819,4.811604,-5.379739,-0.577939,-1.720442,7.612622,6.389877,-5.135569,-7.034801,4.573131,-1.019121,2.766783,-8.999972,9.204393,-2.279773,3.295323,5.540855,-2.939201,-2.595617,7.261555,0.766924,-8.442656,4.782229,-0.638282,6.682243,-1.654680,-3.593825,-9.220483,3.741547,-5.948174,-8.652644,-2.586015,-2.275577,-3.406525,-4.901480,-6.407643,-3.054439,-7.159258,3.913638,-3.461124,2.436811,-0.940349,-4.755851,-6.863913,7.171176,2.197348,-9.193447,5.802087,0.927365,6.209405,1.162382,8.204652,2.776602,-2.335900,-9.346795,9.042963,9.482916,-9.721470,-8.581239,-9.013700,5.139618,-8.357056,1.134434,0.732989,8.189289,-6.518619,-9.495079,-2.636369,-2.746805,-3.407078,9.736400,-7.101999,-0.738068,-1.160965,1.752607,-3.190957,7.796292,-4.543772,-8.813133,7.358416,8.368112,-1.331288,0.926204,5.437357,7.568460,-1.990953,8.991678,-0.358626,3.236297,-5.055248,1.385261,-3.223370,3.770971,4.940549,-5.223404,8.572045,0.740979,7.490254,1.758924,-2.567759,-8.946978,0.241780,0.480222,4.747913,4.425941,2.057793,-3.086594,6.905780,-2.871916,3.091769,1.790992,-6.414743,4.814735,0.771797,-0.457408,0.828011,-8.776459,-1.661377,-7.437875,2.560415,-1.262784,-2.202056,-7.653830,-0.939228,1.059684,6.531170,0.222378,9.084132,8.618616,9.013875,-2.582678,-2.952536,4.028351,-5.619842,2.206719,7.660604,-5.693141,-6.590307,8.251937,9.810298,5.346122,1.725061,3.568421,9.636071,8.919060,-6.731664,1.619264,3.265026,-3.061377,9.064109,1.266458,8.590957,-2.264154,-6.465936,-6.064010,-2.727219,-0.025811,-2.876262,-5.754804,-7.819488,-1.761363,8.565834,0.642371,7.086674,-8.715287,5.271567,7.063821,0.562555,6.239165,-9.574607,-3.516448,1.955557,-9.579259,-7.502522,8.930079,3.688404,3.382056,0.775832,9.671992,-9.575153,8.978672,8.347707,-3.191559,2.954280,-3.100799,-6.190464,-5.547504,7.666504,5.808903,-6.823672,-4.600359,0.462145,-3.580028],[-5.426513,3.849011,-4.137704,7.957907,6.455687,-9.424740,1.522980,-2.157050,2.505317,1.263027,-9.156444,-9.082828,7.238437,-9.800782,6.039521,2.284659,-5.143824,-5.019015,-4.828199,-6.139617,-9.949141,-2.219649,9.223627,1.675655,6.010034,5.340103,7.911681,-8.823362,-4.499477,9.157749,-8.823869,2.849233,8.652154,1.469479,0.214720,-2.055226,-8.179552,2.073457,1.403298,9.717238,7.350147,-5.358617,-3.152475,0.909288,0.911611,-9.929478,-9.772622,-9.414539,-7.752644,3.738994,0.251020,4.190184,-5.417903,6.090858,4.197831,-5.272460,7.707876,9.411122,-1.773130,-6.520012,-3.331141,7.321212,9.280868,-0.378966,7.563693,9.206830,2.159225,-7.810410,-1.693409,-4.473738,-9.885443,-8.907879,0.017231,-5.065111,4.459344,-1.019414,8.637041,-6.205036,4.806878,-1.146499,-3.005918,-9.312119,-9.286450,8.947375,-9.194348,-8.146956,-2.200499,2.056998,7.756901,7.512538,-0.576438,-3.432566,6.207950,-7.673211,4.870592,6.443810,8.185685,-1.725704,8.490440,-5.676424,8.241949,-1.630919,6.976906,4.164196,6.814253,3.861483,-8.213589,-3.248680,-3.567781,7.452329,7.375668,9.424695,-2.147768,7.070757,5.656103,7.234891,-1.806777,3.261221,4.763646,-8.996213,5.528557,3.711432,3.348872,-2.807738,-2.444347,-8.124511,-1.430537,-8.456949,9.841362,-9.893836,4.192853,9.541809,-8.116276,-2.121983,8.526679,-2.989802,-8.341783,3.939403,7.825532,-6.176843,4.785773,-5.139786,-7.444534,-8.905353,-9.837110,1.328860,-3.397129,1.812595,5.540218,1.271847,9.887410,4.222339,9.598944,5.403826,-8.326319,-7.988874,-4.959986,-6.362153,-0.270829,-6.490347,0.960674,-5.461646,-0.369537,-2.297501,0.656172,8.920488,-7.614797,1.659673,8.612143,-9.058112,-6.682401,0.152707,5.373985,7.319944,-1.024345,-4.823586,3.551271,9.716717,3.298932,8.338325,1.714275,4.881070,-2.422691,2.982752,9.077169,9.697750,1.412050,0.613900,-6.919667,-4.457024,-6.246139,1.708009,4.066476,-9.802672,-3.122266,-1.961013,-1.843715,8.093826,-4.005267,-4.486604,2.388184,9.813543,-7.296081,3.189204,5.708862,0.617111,7.429341,-8.507563,6.193590,7.432629,-8.654859,-4.109041,8.794769,2.387968,-7.762634,5.048868,-7.708971,-8.049730,3.010678,5.415754],[9.322353,5.417603,1.195922,-3.868211,-4.859106,4.718665,8.840242,8.784677,6.149599,-5.018928,-8.516469,1.457585,-5.435769,2.258194,-5.355971,-8.188139,5.681696,-2.532246,0.811654,6.459573,-2.176282,4.273082,-4.940159,-5.343040,6.682848,-2.449187,-7.986952,-0.628248,0.708471,1.591240,4.337665,-4.283385,4.915562,0.712767,2.432193,-0.859579,2.617860,7.996524,-7.756143,-8.057111,-6.250861,5.374443,-1.830389,4.022204,2.219789,8.793425,-6.558056,6.986164,-0.087394,9.546170,9.376295,0.394281,4.322362,6.212709,-8.472717,4.961921,-5.482684,-1.710932,4.590844,-4.372483,-5.235942,7.257451,7.657918,-6.698872,0.554858,3.809231,5.333663,-6.739955,2.121580,-9.627030,7.915816,-0.414480,-0.472377,-8.982609,-9.435472,-9.306593,5.397443,-1.298843,-3.249016,-9.762611,-3.989741,-3.391672,0.014097,-1.733737,-3.683177,-9.558496,-1.581679,5.603231,8.619982,-1.351409,0.958837,-3.373958,-6.263134,6.456854,6.772466,8.653617,-2.899952,3.889147,-1.777261,-6.493421,-8.557226,-0.600786,-0.672919,9.014521,5.408636,5.778684,-8.423460,8.694658,-9.653064,5.253665,8.541081,8.125100,1.482929,6.655106,-8.590617,-4.002698,-6.486370,-4.879711,1.263543,7.885900,6.792097,6.637752,-9.870585,7.559836,3.548315,0.716564,8.922345,-8.398384,1.679000,-4.067055,-4.572879,1.399507,6.313071,8.911365,1.503321,3.435938,1.785873,3.378083,-9.822883,7.438410,1.000951,-9.479917,8.780150,0.544918,-5.078721,6.621305,0.725100,2.788653,-5.385444,0.373586,5.141140,-7.588485,4.380406,7.254338,-4.971751,4.630832,7.055888,-0.848247,2.491056,3.620763,6.676524,-0.115035,1.365801,9.323618,-4.752269,-8.989620,-8.752055,-3.664237,-5.478134,5.814889,-4.885772,-7.911297,-1.604631,0.376769,8.835385,0.510028,2.768234,0.239684,2.819933,-0.336075,5.972664,-8.391245,2.409367,1.207600,-6.274416,5.020907,4.489391,-0.840722,-0.238299,7.948964,-1.385296,8.821508,-0.278149,0.533156,9.838238,1.017961,-1.225204,-3.940060,4.403937,0.771096,-1.902725,-7.415706,-6.846347,3.679583,-5.683042,-8.859693,7.143147,-5.222934,-9.424233,-7.757794,4.412716,-2.584043,4.927853,-3.435376,-2.662740,-2.103557,-8.932099,9.010690,4.389849,8.343149],[4.200410,-3.502107,5.994187,9.333660,-7.371078,-4.928804,9.425549,8.230240,2.589975,2.477694,6.804364,4.013402,2.626829,3.958117,6.206279,-9.430767,-5.295210,-4.896994,-6.995004,-4.463378,2.561664,-3.988296,5.482448,9.445447,5.998800,5.497429,-3.377171,-7.819561,2.403504,-9.189029,1.169262,7.823412,0.722227,7.114884,6.819894,0.722792,-0.277586,-1.522277,7.029659,6.527144,-0.349572,-4.481617,7.915924,-7.967718,-9.930728,3.564217,-8.197871,8.747495,-3.264401,6.109676,-8.287053,-9.961520,-6.908061,6.543678,-6.251088,5.975897,9.736439,6.221060,-2.149510,3.758363,-3.169162,-3.183616,6.302621,1.300222,6.501415,-1.158795,8.404776,-5.786280,6.549507,2.364905,-1.412839,-1.884415,-4.697411,-4.534112,-6.538219,4.411367,8.645004,8.463780,-9.758678,-9.399134,2.714063,7.968053,-4.548762,-0.156952,4.172667,6.963910,-7.415146,4.112339,-0.208385,-1.674100,5.668058,8.763222,2.230587,-6.948762,5.784691,7.256802,0.973201,3.078870,3.990093,5.972627,-1.877209,-7.018424,-8.115877,4.232387,-2.722623,2.783961,-1.413875,-2.617510,3.589913,5.921411,1.223081,1.184764,9.038721,-9.092807,4.644600,-6.317897,4.318679,-1.863723,-6.793771,-3.808621,7.587062,8.638886,-4.228504,-1.320830,-4.621666,6.023569,-6.645842,-7.514762,6.338737,-6.441144,-9.358993,-8.915653,-1.026924,8.612932,8.657985,7.262552,-0.919075,-3.390673,-9.605251,-7.090529,-2.390278,-8.306973,8.219253,-1.093371,-0.187901,2.625496,8.648046,-3.857753,-2.839247,8.728831,0.727374,9.026306,3.627668,-1.946532,-9.748809,-6.227761,-4.844504,7.796780,7.793366,8.576946,8.426118,-2.616254,-2.533984,-9.707634,-8.217724,-4.747241,-4.179892,0.129566,3.368970,4.256320,1.043836,-5.251907,-5.536232,3.921316,-3.475472,0.520499,6.941230,-2.737289,-6.018977,-7.721502,-4.561624,-2.865762,-5.615754,-9.265104,-7.640500,9.386919,2.187490,5.382287,-6.900955,5.854020,2.938979,-1.959715,-3.763854,9.145303,3.500316,-1.014808,-5.218027,-9.336166,-9.340091,3.152812,-5.884536,-3.251946,-9.314751,8.186332,-8.559072,8.133967,-3.262258,-7.824372,5.932747,9.949665,-6.631970,-3.890251,6.783247,5.824565,-2.828844,-5.647815,-8.849813,-2.293045,-7.941469,1.391661]], dtype = "float64")#candidate|2224|(4, 220)|const|float64
call_2223 = relay.TupleGetItem(func_1149_call(relay.reshape(const_2224.astype('float64'), [16, 11, 5])), 0)
call_2225 = relay.TupleGetItem(func_1152_call(relay.reshape(const_2224.astype('float64'), [16, 11, 5])), 0)
output = relay.Tuple([call_2203,var_2204,uop_2218,call_2223,const_2224,])
output2 = relay.Tuple([call_2205,var_2204,uop_2220,call_2225,const_2224,])
func_2228 = relay.Function([var_2204,], output)
mod['func_2228'] = func_2228
mod = relay.transform.InferType()(mod)
var_2229 = relay.var("var_2229", dtype = "float64", shape = (1512,))#candidate|2229|(1512,)|var|float64
output = func_2228(var_2229)
func_2230 = relay.Function([var_2229], output)
mutated_mod['func_2230'] = func_2230
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1330_call = mod.get_global_var('func_1330')
func_1331_call = mutated_mod.get_global_var('func_1331')
call_2247 = func_1330_call()
call_2248 = func_1330_call()
func_1322_call = mod.get_global_var('func_1322')
func_1326_call = mutated_mod.get_global_var('func_1326')
const_2258 = relay.const([False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False], dtype = "bool")#candidate|2258|(91,)|const|bool
const_2259 = relay.const([True,True,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,True,False,True,True,True,True,False,True,True,False,False,True,False,True,True,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,True,True,True,True,True,True,True,True,True,False,False,False,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,True,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,False,False,True,True,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,False,False], dtype = "bool")#candidate|2259|(728,)|const|bool
call_2257 = func_1322_call(relay.reshape(const_2258.astype('bool'), [13, 7, 1]), relay.reshape(const_2259.astype('bool'), [13, 7, 8]), )
call_2260 = func_1322_call(relay.reshape(const_2258.astype('bool'), [13, 7, 1]), relay.reshape(const_2259.astype('bool'), [13, 7, 8]), )
var_2261 = relay.var("var_2261", dtype = "bool", shape = (91,))#candidate|2261|(91,)|var|bool
bop_2262 = relay.logical_xor(const_2258.astype('int64'), relay.reshape(var_2261.astype('int64'), relay.shape_of(const_2258))) # shape=(91,)
uop_2270 = relay.atanh(call_2247.astype('float32')) # shape=(2, 14, 3)
uop_2272 = relay.atanh(call_2248.astype('float32')) # shape=(2, 14, 3)
output = relay.Tuple([call_2257,const_2259,bop_2262,uop_2270,])
output2 = relay.Tuple([call_2260,const_2259,bop_2262,uop_2272,])
func_2282 = relay.Function([var_2261,], output)
mod['func_2282'] = func_2282
mod = relay.transform.InferType()(mod)
mutated_mod['func_2282'] = func_2282
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2283 = relay.var("var_2283", dtype = "bool", shape = (91,))#candidate|2283|(91,)|var|bool
func_2282_call = mutated_mod.get_global_var('func_2282')
call_2284 = func_2282_call(var_2283)
output = call_2284
func_2285 = relay.Function([var_2283], output)
mutated_mod['func_2285'] = func_2285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_2337 = relay.TupleGetItem(func_665_call(), 0)
call_2338 = relay.TupleGetItem(func_666_call(), 0)
uop_2345 = relay.sin(call_2337.astype('float32')) # shape=(2, 14, 3)
uop_2347 = relay.sin(call_2338.astype('float32')) # shape=(2, 14, 3)
const_2352 = relay.const([[[-3.278181,2.247443,-3.253093],[9.732484,-5.303573,3.046541],[-7.453014,8.691139,1.177904],[3.733351,-4.920929,9.925158],[7.070189,-3.946045,5.489584],[-1.973508,-4.983326,7.961149],[-8.575529,-8.840707,-8.230028],[-9.000188,6.824520,3.347513],[9.200170,-9.198827,0.622697],[4.674168,2.346777,-3.832298],[4.672508,-2.754471,-1.509994],[-9.897497,-9.634942,6.626933],[-5.992149,2.864580,-2.818713],[-5.272692,5.204306,1.758962]],[[-1.069267,7.084527,-4.733168],[0.688909,9.805392,9.882309],[1.059042,-3.106516,6.861782],[-0.700998,5.644313,5.642553],[-1.966104,-6.331554,3.239507],[2.783966,-7.370921,4.982477],[-4.107714,-7.177953,-5.299915],[-0.560533,4.889586,-8.471452],[-8.428142,-2.925033,-8.443213],[8.884938,5.344925,3.533126],[3.654263,1.328728,2.487860],[-3.689798,2.823204,0.454969],[6.288616,2.690426,2.286877],[0.578430,9.149879,9.515624]]], dtype = "float32")#candidate|2352|(2, 14, 3)|const|float32
bop_2353 = relay.right_shift(uop_2345.astype('int16'), relay.reshape(const_2352.astype('int16'), relay.shape_of(uop_2345))) # shape=(2, 14, 3)
bop_2356 = relay.right_shift(uop_2347.astype('int16'), relay.reshape(const_2352.astype('int16'), relay.shape_of(uop_2347))) # shape=(2, 14, 3)
output = relay.Tuple([bop_2353,])
output2 = relay.Tuple([bop_2356,])
func_2357 = relay.Function([], output)
mod['func_2357'] = func_2357
mod = relay.transform.InferType()(mod)
mutated_mod['func_2357'] = func_2357
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2357_call = mutated_mod.get_global_var('func_2357')
call_2358 = func_2357_call()
output = call_2358
func_2359 = relay.Function([], output)
mutated_mod['func_2359'] = func_2359
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1482_call = mod.get_global_var('func_1482')
func_1484_call = mutated_mod.get_global_var('func_1484')
call_2373 = relay.TupleGetItem(func_1482_call(), 0)
call_2374 = relay.TupleGetItem(func_1484_call(), 0)
output = relay.Tuple([call_2373,])
output2 = relay.Tuple([call_2374,])
func_2383 = relay.Function([], output)
mod['func_2383'] = func_2383
mod = relay.transform.InferType()(mod)
output = func_2383()
func_2384 = relay.Function([], output)
mutated_mod['func_2384'] = func_2384
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1297_call = mod.get_global_var('func_1297')
func_1298_call = mutated_mod.get_global_var('func_1298')
call_2409 = relay.TupleGetItem(func_1297_call(), 0)
call_2410 = relay.TupleGetItem(func_1298_call(), 0)
output = call_2409
output2 = call_2410
func_2411 = relay.Function([], output)
mod['func_2411'] = func_2411
mod = relay.transform.InferType()(mod)
mutated_mod['func_2411'] = func_2411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2411_call = mutated_mod.get_global_var('func_2411')
call_2412 = func_2411_call()
output = call_2412
func_2413 = relay.Function([], output)
mutated_mod['func_2413'] = func_2413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1297_call = mod.get_global_var('func_1297')
func_1298_call = mutated_mod.get_global_var('func_1298')
call_2428 = relay.TupleGetItem(func_1297_call(), 0)
call_2429 = relay.TupleGetItem(func_1298_call(), 0)
uop_2445 = relay.tan(call_2428.astype('float32')) # shape=(10, 2, 8)
uop_2447 = relay.tan(call_2429.astype('float32')) # shape=(10, 2, 8)
bop_2448 = relay.maximum(uop_2445.astype('int8'), relay.reshape(call_2428.astype('int8'), relay.shape_of(uop_2445))) # shape=(10, 2, 8)
bop_2451 = relay.maximum(uop_2447.astype('int8'), relay.reshape(call_2429.astype('int8'), relay.shape_of(uop_2447))) # shape=(10, 2, 8)
output = relay.Tuple([bop_2448,])
output2 = relay.Tuple([bop_2451,])
func_2458 = relay.Function([], output)
mod['func_2458'] = func_2458
mod = relay.transform.InferType()(mod)
output = func_2458()
func_2459 = relay.Function([], output)
mutated_mod['func_2459'] = func_2459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1058_call = mod.get_global_var('func_1058')
func_1060_call = mutated_mod.get_global_var('func_1060')
call_2460 = func_1058_call()
call_2461 = func_1058_call()
const_2464 = relay.const([[[5.628416,-3.327743,-7.029493],[-2.773077,-5.508485,9.575842],[-8.864003,4.101225,-2.587811],[-9.203937,6.533216,2.991274],[4.605329,9.282239,-7.801008],[9.978923,4.393730,-6.105142],[-2.301704,-6.653269,9.131306],[3.422912,5.642017,-9.664979],[6.688372,3.528800,-0.076292],[1.314682,2.685321,-7.215213],[-8.641176,0.575026,-6.602781],[6.454183,8.393026,8.668353],[6.152258,-7.366766,8.430640],[0.434890,6.390850,-7.904453]],[[8.449388,-9.681209,-9.090719],[-5.199117,-0.290092,-2.104118],[9.506298,6.558731,0.250038],[4.251546,-5.612040,-3.436291],[6.973713,-7.668054,-1.745158],[-1.881352,-3.492921,-6.773481],[-4.479905,8.146616,3.475038],[2.010403,-2.673890,2.486187],[6.456282,-3.173226,-8.170604],[4.725389,-5.886942,-3.095254],[-4.074123,-7.956606,6.647831],[3.527012,9.125914,-6.249700],[6.978351,-6.023525,6.500763],[3.183792,-3.057572,-6.063691]]], dtype = "float32")#candidate|2464|(2, 14, 3)|const|float32
bop_2465 = relay.floor_mod(call_2460.astype('float64'), relay.reshape(const_2464.astype('float64'), relay.shape_of(call_2460))) # shape=(2, 14, 3)
bop_2468 = relay.floor_mod(call_2461.astype('float64'), relay.reshape(const_2464.astype('float64'), relay.shape_of(call_2461))) # shape=(2, 14, 3)
output = bop_2465
output2 = bop_2468
func_2470 = relay.Function([], output)
mod['func_2470'] = func_2470
mod = relay.transform.InferType()(mod)
mutated_mod['func_2470'] = func_2470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2470_call = mutated_mod.get_global_var('func_2470')
call_2471 = func_2470_call()
output = call_2471
func_2472 = relay.Function([], output)
mutated_mod['func_2472'] = func_2472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2174_call = mod.get_global_var('func_2174')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2494 = func_2174_call()
call_2495 = func_2174_call()
output = relay.Tuple([call_2494,])
output2 = relay.Tuple([call_2495,])
func_2497 = relay.Function([], output)
mod['func_2497'] = func_2497
mod = relay.transform.InferType()(mod)
mutated_mod['func_2497'] = func_2497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2497_call = mutated_mod.get_global_var('func_2497')
call_2498 = func_2497_call()
output = call_2498
func_2499 = relay.Function([], output)
mutated_mod['func_2499'] = func_2499
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2505 = relay.const([[[2.279748,1.647179,-8.127638,1.592557],[9.210910,0.316224,9.592681,-9.335537],[-2.143535,8.109441,3.391070,-7.643095],[-9.046815,1.336524,9.420724,-6.453182],[-0.930217,-9.454872,2.491741,-5.024866],[-3.219529,5.569905,0.622039,2.875897],[-5.264620,4.025865,-6.869922,0.187972],[-4.730347,4.575720,9.738074,-4.975129],[3.797061,-0.578334,7.339632,-2.407868],[-3.763147,4.192233,0.658431,8.801774],[3.265600,7.593672,0.531545,3.359714],[2.782278,9.491137,-9.283326,-4.283755]],[[-4.743282,3.669648,1.299151,7.179552],[9.913770,9.592050,6.755898,-5.254925],[8.484002,-5.364272,-7.343076,1.015106],[-7.751404,-6.125545,-4.807732,6.709319],[9.477408,-8.431009,-0.293101,5.449990],[3.245151,-8.934147,4.787442,7.094674],[-1.098038,7.706443,6.572985,-3.894250],[2.038186,0.168312,1.883826,-4.033072],[2.685134,5.078680,5.863394,8.886360],[3.601354,8.044594,-5.014430,-5.884470],[2.455545,8.907110,-8.485547,-9.185365],[-1.051162,6.633338,-2.753991,-8.249313]],[[6.882122,8.112287,-8.666269,8.302343],[-5.336736,0.146523,6.755332,9.128824],[6.911314,-0.403793,-0.662877,-4.078462],[-4.191736,-6.089158,4.731750,-1.547015],[-4.712625,0.971819,-2.293943,3.155059],[-0.772446,9.869093,-9.042333,-0.669207],[5.564298,5.988274,5.733845,-2.873968],[0.813069,7.211111,6.629686,6.558699],[2.398370,7.325315,9.347883,9.932159],[6.790804,-3.993707,8.468168,7.182919],[3.991447,1.613127,-8.997989,-9.262698],[-5.176629,0.567022,6.799301,-1.021750]],[[2.686963,-2.755986,-7.860716,-2.534201],[-5.053931,4.718817,6.709911,-3.347805],[4.643991,-0.007459,4.169246,5.557161],[-5.737606,7.400515,-1.044910,-2.319354],[2.573167,-3.434206,-6.039648,6.014971],[9.123198,1.785591,-8.520394,6.903553],[3.295492,0.008900,-6.448025,-3.721978],[3.809578,-8.944329,9.217364,-5.620106],[7.955842,-6.969301,8.070702,-0.697057],[-5.965526,-4.192724,3.942870,-2.593473],[2.592044,1.104085,9.569085,-1.760504],[-2.775315,-1.976253,2.219588,-6.868649]],[[3.526870,0.231985,0.516637,-7.381678],[3.078549,-5.186236,-5.850213,4.677371],[-0.171430,-8.245815,-4.203953,5.420168],[4.020785,9.160392,-8.404208,-9.327068],[-1.576659,-0.152849,8.321819,-1.476236],[3.429145,-3.962604,7.463525,8.654896],[-4.717900,3.213600,-0.910025,9.147474],[-6.035216,5.601267,9.058279,8.770980],[4.749782,3.070852,-4.350488,3.241022],[-7.157261,7.353324,6.951872,0.446998],[-8.258020,-0.439978,5.857708,3.695592],[-4.852761,-0.149235,-7.091849,-7.488041]],[[-6.982345,-5.705832,0.492868,-9.590195],[2.582961,5.805286,1.078795,2.229623],[-6.642847,-9.092576,5.093509,1.291511],[-0.737306,4.157507,4.325509,-0.953101],[0.126134,-9.336318,-7.160611,-8.704542],[5.447421,-9.911782,8.891605,-7.579841],[-0.236412,3.076232,-9.736565,7.527048],[4.352578,1.307744,-2.913987,-4.433157],[5.634876,-6.053992,7.421959,9.079157],[5.830172,4.851943,0.508779,-8.654933],[0.342136,-0.246226,-1.556131,-2.267849],[-4.999427,6.311697,-8.850047,3.408238]]], dtype = "float32")#candidate|2505|(6, 12, 4)|const|float32
uop_2506 = relay.log10(const_2505.astype('float32')) # shape=(6, 12, 4)
var_2511 = relay.var("var_2511", dtype = "float32", shape = (6, 12, 4))#candidate|2511|(6, 12, 4)|var|float32
bop_2512 = relay.add(uop_2506.astype('uint64'), relay.reshape(var_2511.astype('uint64'), relay.shape_of(uop_2506))) # shape=(6, 12, 4)
output = relay.Tuple([bop_2512,])
output2 = relay.Tuple([bop_2512,])
func_2519 = relay.Function([var_2511,], output)
mod['func_2519'] = func_2519
mod = relay.transform.InferType()(mod)
var_2520 = relay.var("var_2520", dtype = "float32", shape = (6, 12, 4))#candidate|2520|(6, 12, 4)|var|float32
output = func_2519(var_2520)
func_2521 = relay.Function([var_2520], output)
mutated_mod['func_2521'] = func_2521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2470_call = mod.get_global_var('func_2470')
func_2472_call = mutated_mod.get_global_var('func_2472')
call_2554 = func_2470_call()
call_2555 = func_2470_call()
func_1058_call = mod.get_global_var('func_1058')
func_1060_call = mutated_mod.get_global_var('func_1060')
call_2556 = func_1058_call()
call_2557 = func_1058_call()
func_2282_call = mod.get_global_var('func_2282')
func_2285_call = mutated_mod.get_global_var('func_2285')
var_2564 = relay.var("var_2564", dtype = "bool", shape = (91,))#candidate|2564|(91,)|var|bool
call_2563 = relay.TupleGetItem(func_2282_call(relay.reshape(var_2564.astype('bool'), [91,])), 1)
call_2565 = relay.TupleGetItem(func_2285_call(relay.reshape(var_2564.astype('bool'), [91,])), 1)
func_2357_call = mod.get_global_var('func_2357')
func_2359_call = mutated_mod.get_global_var('func_2359')
call_2566 = relay.TupleGetItem(func_2357_call(), 0)
call_2567 = relay.TupleGetItem(func_2359_call(), 0)
output = relay.Tuple([call_2554,call_2556,call_2563,var_2564,call_2566,])
output2 = relay.Tuple([call_2555,call_2557,call_2565,var_2564,call_2567,])
func_2575 = relay.Function([var_2564,], output)
mod['func_2575'] = func_2575
mod = relay.transform.InferType()(mod)
mutated_mod['func_2575'] = func_2575
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2576 = relay.var("var_2576", dtype = "bool", shape = (91,))#candidate|2576|(91,)|var|bool
func_2575_call = mutated_mod.get_global_var('func_2575')
call_2577 = func_2575_call(var_2576)
output = call_2577
func_2578 = relay.Function([var_2576], output)
mutated_mod['func_2578'] = func_2578
mutated_mod = relay.transform.InferType()(mutated_mod)
func_929_call = mod.get_global_var('func_929')
func_931_call = mutated_mod.get_global_var('func_931')
call_2584 = relay.TupleGetItem(func_929_call(), 1)
call_2585 = relay.TupleGetItem(func_931_call(), 1)
output = call_2584
output2 = call_2585
func_2593 = relay.Function([], output)
mod['func_2593'] = func_2593
mod = relay.transform.InferType()(mod)
mutated_mod['func_2593'] = func_2593
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2593_call = mutated_mod.get_global_var('func_2593')
call_2594 = func_2593_call()
output = call_2594
func_2595 = relay.Function([], output)
mutated_mod['func_2595'] = func_2595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_2602 = relay.TupleGetItem(func_1517_call(), 0)
call_2603 = relay.TupleGetItem(func_1519_call(), 0)
func_2519_call = mod.get_global_var('func_2519')
func_2521_call = mutated_mod.get_global_var('func_2521')
var_2611 = relay.var("var_2611", dtype = "float32", shape = (288,))#candidate|2611|(288,)|var|float32
call_2610 = relay.TupleGetItem(func_2519_call(relay.reshape(var_2611.astype('float32'), [6, 12, 4])), 0)
call_2612 = relay.TupleGetItem(func_2521_call(relay.reshape(var_2611.astype('float32'), [6, 12, 4])), 0)
func_1149_call = mod.get_global_var('func_1149')
func_1152_call = mutated_mod.get_global_var('func_1152')
var_2668 = relay.var("var_2668", dtype = "float64", shape = (440, 2))#candidate|2668|(440, 2)|var|float64
call_2667 = relay.TupleGetItem(func_1149_call(relay.reshape(var_2668.astype('float64'), [16, 11, 5])), 0)
call_2669 = relay.TupleGetItem(func_1152_call(relay.reshape(var_2668.astype('float64'), [16, 11, 5])), 0)
output = relay.Tuple([call_2602,call_2610,var_2611,call_2667,var_2668,])
output2 = relay.Tuple([call_2603,call_2612,var_2611,call_2669,var_2668,])
func_2673 = relay.Function([var_2611,var_2668,], output)
mod['func_2673'] = func_2673
mod = relay.transform.InferType()(mod)
mutated_mod['func_2673'] = func_2673
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2673_call = mutated_mod.get_global_var('func_2673')
var_2675 = relay.var("var_2675", dtype = "float32", shape = (288,))#candidate|2675|(288,)|var|float32
var_2676 = relay.var("var_2676", dtype = "float64", shape = (440, 2))#candidate|2676|(440, 2)|var|float64
call_2674 = func_2673_call(var_2675,var_2676,)
output = call_2674
func_2677 = relay.Function([var_2675,var_2676,], output)
mutated_mod['func_2677'] = func_2677
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_2702 = relay.TupleGetItem(func_2458_call(), 0)
call_2703 = relay.TupleGetItem(func_2459_call(), 0)
uop_2720 = relay.asinh(call_2702.astype('float64')) # shape=(10, 2, 8)
uop_2722 = relay.asinh(call_2703.astype('float64')) # shape=(10, 2, 8)
func_2593_call = mod.get_global_var('func_2593')
func_2595_call = mutated_mod.get_global_var('func_2595')
call_2724 = func_2593_call()
call_2725 = func_2593_call()
output = relay.Tuple([uop_2720,call_2724,])
output2 = relay.Tuple([uop_2722,call_2725,])
func_2730 = relay.Function([], output)
mod['func_2730'] = func_2730
mod = relay.transform.InferType()(mod)
mutated_mod['func_2730'] = func_2730
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2730_call = mutated_mod.get_global_var('func_2730')
call_2731 = func_2730_call()
output = call_2731
func_2732 = relay.Function([], output)
mutated_mod['func_2732'] = func_2732
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2761 = relay.var("var_2761", dtype = "float32", shape = (2, 15, 10))#candidate|2761|(2, 15, 10)|var|float32
var_2762 = relay.var("var_2762", dtype = "float32", shape = (2, 15, 10))#candidate|2762|(2, 15, 10)|var|float32
bop_2763 = relay.power(var_2761.astype('float32'), relay.reshape(var_2762.astype('float32'), relay.shape_of(var_2761))) # shape=(2, 15, 10)
func_2673_call = mod.get_global_var('func_2673')
func_2677_call = mutated_mod.get_global_var('func_2677')
var_2767 = relay.var("var_2767", dtype = "float32", shape = (288,))#candidate|2767|(288,)|var|float32
var_2768 = relay.var("var_2768", dtype = "float64", shape = (880,))#candidate|2768|(880,)|var|float64
call_2766 = relay.TupleGetItem(func_2673_call(relay.reshape(var_2767.astype('float32'), [288,]), relay.reshape(var_2768.astype('float64'), [440, 2]), ), 3)
call_2769 = relay.TupleGetItem(func_2677_call(relay.reshape(var_2767.astype('float32'), [288,]), relay.reshape(var_2768.astype('float64'), [440, 2]), ), 3)
func_1983_call = mod.get_global_var('func_1983')
func_1985_call = mutated_mod.get_global_var('func_1985')
var_2784 = relay.var("var_2784", dtype = "float32", shape = (280,))#candidate|2784|(280,)|var|float32
call_2783 = relay.TupleGetItem(func_1983_call(relay.reshape(var_2784.astype('float32'), [70, 4])), 2)
call_2785 = relay.TupleGetItem(func_1985_call(relay.reshape(var_2784.astype('float32'), [70, 4])), 2)
output = relay.Tuple([bop_2763,call_2766,var_2767,var_2768,call_2783,var_2784,])
output2 = relay.Tuple([bop_2763,call_2769,var_2767,var_2768,call_2785,var_2784,])
func_2788 = relay.Function([var_2761,var_2762,var_2767,var_2768,var_2784,], output)
mod['func_2788'] = func_2788
mod = relay.transform.InferType()(mod)
mutated_mod['func_2788'] = func_2788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2788_call = mutated_mod.get_global_var('func_2788')
var_2790 = relay.var("var_2790", dtype = "float32", shape = (2, 15, 10))#candidate|2790|(2, 15, 10)|var|float32
var_2791 = relay.var("var_2791", dtype = "float32", shape = (2, 15, 10))#candidate|2791|(2, 15, 10)|var|float32
var_2792 = relay.var("var_2792", dtype = "float32", shape = (288,))#candidate|2792|(288,)|var|float32
var_2793 = relay.var("var_2793", dtype = "float64", shape = (880,))#candidate|2793|(880,)|var|float64
var_2794 = relay.var("var_2794", dtype = "float32", shape = (280,))#candidate|2794|(280,)|var|float32
call_2789 = func_2788_call(var_2790,var_2791,var_2792,var_2793,var_2794,)
output = call_2789
func_2795 = relay.Function([var_2790,var_2791,var_2792,var_2793,var_2794,], output)
mutated_mod['func_2795'] = func_2795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2824 = relay.var("var_2824", dtype = "int32", shape = (8, 10, 6))#candidate|2824|(8, 10, 6)|var|int32
var_2825 = relay.var("var_2825", dtype = "int32", shape = (8, 10, 6))#candidate|2825|(8, 10, 6)|var|int32
bop_2826 = relay.greater_equal(var_2824.astype('bool'), relay.reshape(var_2825.astype('bool'), relay.shape_of(var_2824))) # shape=(8, 10, 6)
func_2575_call = mod.get_global_var('func_2575')
func_2578_call = mutated_mod.get_global_var('func_2578')
var_2837 = relay.var("var_2837", dtype = "bool", shape = (91,))#candidate|2837|(91,)|var|bool
call_2836 = relay.TupleGetItem(func_2575_call(relay.reshape(var_2837.astype('bool'), [91,])), 1)
call_2838 = relay.TupleGetItem(func_2578_call(relay.reshape(var_2837.astype('bool'), [91,])), 1)
var_2844 = relay.var("var_2844", dtype = "bool", shape = (91,))#candidate|2844|(91,)|var|bool
bop_2845 = relay.power(var_2837.astype('float32'), relay.reshape(var_2844.astype('float32'), relay.shape_of(var_2837))) # shape=(91,)
func_1020_call = mod.get_global_var('func_1020')
func_1025_call = mutated_mod.get_global_var('func_1025')
const_2853 = relay.const([[6.552549,5.596327,-0.550854,8.475217,5.815755,-7.410505,-4.403677,5.930193,-0.605485,1.651290,2.151858,6.634304],[-1.417098,3.838134,7.723807,7.736584,9.329368,-6.179037,1.784587,3.423677,0.885491,2.072277,6.393968,-1.139171],[2.273093,5.900100,-2.401774,-9.907495,1.654398,8.589243,8.419853,8.748331,9.360595,-9.431443,3.804112,3.897963]], dtype = "float64")#candidate|2853|(3, 12)|const|float64
var_2854 = relay.var("var_2854", dtype = "uint64", shape = (180,))#candidate|2854|(180,)|var|uint64
const_2855 = relay.const([2.558457,-9.678797,-7.443925,-2.122963,-3.581700,-6.949635,-5.280130,-2.464307,8.859634,-0.750268,7.965657,9.121136,-5.395786,7.949311,-0.290060,5.506048,8.296816,3.934746,-0.370736,1.116572,-3.674831,-7.306909,-7.986573,-4.222647,-1.556848,-9.451208,0.017433,1.637877,-8.651721,4.833270,5.692219,9.585749,-1.713028,-0.519082,-1.796235,-2.743128,-2.676467,-5.095515,8.647281,-3.950932,0.156367,7.074076,9.239340,6.766947,-1.626942,-2.940786,5.779521,-5.892323,1.539870,-1.734456,5.421539,-8.323942,8.399363,-1.808170,5.341892,-7.590806,3.712049,6.919934,-0.122526,9.400671,-3.085953,1.088128,6.976421,6.449335,-4.464256,-9.252993,-1.198427,9.342822,3.051071,2.910004,3.278163,-9.775217,1.524523,2.636673,-3.826805,-3.410670,-3.383966,-4.228281,-9.588639,-7.325766,6.976062,-1.019931,6.771167,0.639296,2.052220,-7.091533,2.854090,5.908006,-1.311137,-2.628857,2.823583,4.318006,-9.563955,0.514103,-3.957626,-2.856517,5.267231,1.541010,-1.773752,7.299503,9.830622,-9.409393,-6.917888,-8.498335,-9.246890,1.277014,4.169958,-2.665317,-1.647188,-3.004910,3.880738,-4.561491,5.403431,-9.947626,5.857182,4.581064,7.279175,7.386029,-3.495319,-6.083631,-2.595338,-0.321118,6.851291,-5.611121,5.690329,-9.966958,1.497831,0.888450,-5.100255,-2.741835,7.856061,5.503168,-6.268120,0.504181,-3.383730,3.277302,8.183453,-6.613010,-6.552387,7.639020,-7.334251,9.886233,-7.825233,-3.090878,-3.821560,-2.119136,1.944273,-3.174435,-1.324616,-3.481501,3.961838,-1.362107,6.166802,7.016033,4.248481,0.302677,-1.672762,5.994829,5.686391,-1.137743,-6.085928,-8.030022,-4.671551,7.218854,-5.795932,5.901193,-2.964514,-7.399446,-1.805152,9.709195,-8.820887,2.694422,1.033171,-5.269349,6.402393,-0.658013,7.913457,0.828267,9.391733,7.818285,-4.307606,-5.367377,-9.393218,-2.776917,-3.754144,-9.710597,1.511871,-4.022896,-3.963396,4.603050,9.391998,9.933298,-5.909964,-3.137929,-4.116329,5.015822,-5.420699,4.539998,7.008685,6.536417,8.055335,-1.188396,-7.383396,-3.500730,3.122784,-2.832482,5.851995,-8.226768,-8.511543,-2.795793,-6.763970,7.414135,0.541746,4.395248,-7.354491,-8.514550], dtype = "float64")#candidate|2855|(216,)|const|float64
call_2852 = relay.TupleGetItem(func_1020_call(relay.reshape(const_2853.astype('float64'), [3, 12]), relay.reshape(var_2854.astype('uint64'), [90, 2]), relay.reshape(const_2855.astype('float64'), [216,]), ), 10)
call_2856 = relay.TupleGetItem(func_1025_call(relay.reshape(const_2853.astype('float64'), [3, 12]), relay.reshape(var_2854.astype('uint64'), [90, 2]), relay.reshape(const_2855.astype('float64'), [216,]), ), 10)
var_2857 = relay.var("var_2857", dtype = "bool", shape = (91,))#candidate|2857|(91,)|var|bool
bop_2858 = relay.greater(var_2837.astype('bool'), relay.reshape(var_2857.astype('bool'), relay.shape_of(var_2837))) # shape=(91,)
func_2383_call = mod.get_global_var('func_2383')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_2861 = relay.TupleGetItem(func_2383_call(), 0)
call_2862 = relay.TupleGetItem(func_2384_call(), 0)
uop_2867 = relay.cos(var_2844.astype('float64')) # shape=(91,)
bop_2877 = relay.logical_or(uop_2867.astype('bool'), relay.reshape(bop_2845.astype('bool'), relay.shape_of(uop_2867))) # shape=(91,)
func_1297_call = mod.get_global_var('func_1297')
func_1298_call = mutated_mod.get_global_var('func_1298')
call_2883 = relay.TupleGetItem(func_1297_call(), 0)
call_2884 = relay.TupleGetItem(func_1298_call(), 0)
output = relay.Tuple([bop_2826,call_2836,call_2852,const_2853,var_2854,const_2855,bop_2858,call_2861,bop_2877,call_2883,])
output2 = relay.Tuple([bop_2826,call_2838,call_2856,const_2853,var_2854,const_2855,bop_2858,call_2862,bop_2877,call_2884,])
func_2888 = relay.Function([var_2824,var_2825,var_2837,var_2844,var_2854,var_2857,], output)
mod['func_2888'] = func_2888
mod = relay.transform.InferType()(mod)
var_2889 = relay.var("var_2889", dtype = "int32", shape = (8, 10, 6))#candidate|2889|(8, 10, 6)|var|int32
var_2890 = relay.var("var_2890", dtype = "int32", shape = (8, 10, 6))#candidate|2890|(8, 10, 6)|var|int32
var_2891 = relay.var("var_2891", dtype = "bool", shape = (91,))#candidate|2891|(91,)|var|bool
var_2892 = relay.var("var_2892", dtype = "bool", shape = (91,))#candidate|2892|(91,)|var|bool
var_2893 = relay.var("var_2893", dtype = "uint64", shape = (180,))#candidate|2893|(180,)|var|uint64
var_2894 = relay.var("var_2894", dtype = "bool", shape = (91,))#candidate|2894|(91,)|var|bool
output = func_2888(var_2889,var_2890,var_2891,var_2892,var_2893,var_2894,)
func_2895 = relay.Function([var_2889,var_2890,var_2891,var_2892,var_2893,var_2894,], output)
mutated_mod['func_2895'] = func_2895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_2900 = func_525_call()
call_2901 = func_525_call()
output = call_2900
output2 = call_2901
func_2914 = relay.Function([], output)
mod['func_2914'] = func_2914
mod = relay.transform.InferType()(mod)
output = func_2914()
func_2915 = relay.Function([], output)
mutated_mod['func_2915'] = func_2915
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2174_call = mod.get_global_var('func_2174')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2918 = func_2174_call()
call_2919 = func_2174_call()
func_2174_call = mod.get_global_var('func_2174')
func_2175_call = mutated_mod.get_global_var('func_2175')
call_2923 = func_2174_call()
call_2924 = func_2174_call()
output = relay.Tuple([call_2918,call_2923,])
output2 = relay.Tuple([call_2919,call_2924,])
func_2925 = relay.Function([], output)
mod['func_2925'] = func_2925
mod = relay.transform.InferType()(mod)
output = func_2925()
func_2926 = relay.Function([], output)
mutated_mod['func_2926'] = func_2926
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3007 = relay.var("var_3007", dtype = "float64", shape = (8, 7, 16))#candidate|3007|(8, 7, 16)|var|float64
const_3008 = relay.const([[[-8.744705,-7.773356,-4.474838,-3.352247,5.747311,6.290187,8.170204,8.691830,-8.992223,-4.325346,-4.121267,1.792233,-8.124363,-1.756666,-1.306052,-6.370614],[-4.832626,5.449748,-1.110846,-1.713143,9.129415,-2.640840,4.299969,-1.549028,7.283842,-5.261202,-3.536647,8.240268,6.411287,-6.159636,6.382189,0.267375],[-4.056882,4.222349,-6.915608,-2.041505,6.488037,-1.385985,-3.086527,-6.187077,0.289435,-6.675141,-2.034478,-1.024613,6.954409,8.045775,-9.190931,-6.823924],[-3.044361,4.639385,0.119367,-3.904832,-7.579938,8.097905,-2.897470,-4.349327,4.876964,0.169428,1.679418,7.181518,-9.321691,4.250878,7.335238,0.901015],[4.945971,-7.330118,5.213774,-8.920738,0.368388,-2.695514,4.513520,-7.240051,7.737251,1.153676,1.314301,-8.586019,5.155633,-0.559288,0.126168,-4.885165],[-0.060091,-6.367175,-4.683964,-1.176814,-8.356084,4.078195,8.997127,-3.405411,1.415010,5.101946,6.442297,-8.407598,-4.138587,8.822950,5.564739,-0.043579],[3.674578,1.305031,3.998684,1.563776,-1.972846,-7.029761,-5.665748,2.828992,-0.499668,7.115998,-2.739548,-4.918157,-7.141853,-1.832873,-0.800249,-7.370094]],[[5.873012,5.791357,9.922301,3.649112,3.895060,4.036881,-2.194270,9.943412,-7.800020,-0.253858,-2.615282,5.213202,7.570529,-9.716839,-5.298492,8.565030],[-9.451309,2.233429,7.356838,-8.897488,-8.470478,2.750373,-1.733841,7.639654,0.067030,6.309300,-3.175679,-5.194720,-7.467477,9.813315,5.245172,7.441397],[7.273823,3.234827,9.309101,0.920072,-0.208243,-3.610153,8.658044,7.165598,-1.608780,9.301115,0.522065,-2.001252,-6.577359,-8.344090,-7.970630,-8.240101],[-3.439335,-3.656924,5.336596,7.765713,-6.077308,-8.097633,7.687184,-1.955228,-5.274241,9.156002,-4.232614,0.631180,0.195418,-7.242920,1.322915,-5.387595],[9.669140,3.770942,-4.673745,-8.553521,2.439381,2.712416,-9.324346,-1.319517,7.719474,-8.271954,4.595142,-1.217270,0.311310,-3.341713,9.502926,1.150554],[3.400110,3.386182,5.384724,0.459849,-1.021028,-7.897073,-0.069578,7.147236,-1.690148,0.751863,-2.174496,-5.519754,1.177126,-6.833330,8.114470,1.129105],[2.703746,1.955951,-0.092698,5.254196,2.047796,9.041979,-9.785395,2.487173,-9.294309,-6.032878,-8.317299,-8.052086,1.240685,5.085506,-2.973797,4.734447]],[[2.021634,5.662462,2.577454,7.152481,-8.848445,2.141195,3.812383,3.605327,3.946712,-2.515132,-1.957074,8.936068,-4.999216,7.534189,1.664424,-0.050882],[9.898963,-4.410728,-8.635484,0.877454,-7.743312,0.104257,5.743779,5.422121,-6.550808,-0.861044,8.438803,-8.706082,-9.952350,-9.399933,-1.063348,6.337748],[-8.723947,3.384084,6.887612,0.931214,5.166396,9.890978,4.775453,4.318343,6.387990,3.414726,-5.120840,-9.098514,3.471028,-9.213013,4.508169,2.886494],[-4.375450,-8.126361,7.191642,9.540031,-6.553428,1.124913,-0.984285,1.923688,-2.230904,-2.127810,-1.894930,-1.708803,3.076512,4.904342,-3.147428,1.486145],[2.666435,-4.138188,3.225581,3.002237,-4.821214,-0.715423,-6.368958,-2.756490,-3.235878,7.086566,7.679727,-1.509083,-4.681454,8.035617,-7.556509,0.567726],[-9.068169,-1.109013,-1.125827,0.845699,-5.968550,8.830047,2.631622,7.540017,-9.681974,-3.827530,-4.771852,-0.941519,4.977335,3.996729,-4.645557,7.156218],[-8.056553,4.626295,-8.851226,-9.635186,-3.168412,0.884673,1.527933,5.499004,2.916057,-2.024234,-7.531834,-6.637582,-5.830519,2.333625,7.658779,-8.816754]],[[-4.800522,-5.903944,-9.226495,1.610284,-9.191520,7.055457,4.242577,7.445017,-7.979413,6.867936,-9.019789,-5.150001,5.901187,-8.371219,2.473102,2.088388],[-5.872339,-0.591214,-6.621221,2.670884,-7.088842,-4.167555,2.006745,-9.841042,1.038579,-7.137121,4.778008,1.279521,-6.867396,0.400032,-3.393180,8.850901],[-7.431704,1.738420,4.980025,0.539053,8.372034,3.502574,9.034123,2.226185,5.204611,0.225283,-8.886867,-3.872017,-7.688244,-7.258203,-6.045650,4.155451],[4.334920,1.378788,4.137338,-4.792078,-7.709823,5.233874,9.536921,9.100961,-1.964525,-5.932965,2.513246,9.997258,-7.683769,-2.139235,9.089445,-3.026818],[-9.966353,9.362522,-9.323895,8.631003,5.452826,6.939213,6.418354,-1.753601,1.738420,-4.206968,5.693921,-7.039572,-7.601929,-7.123663,-9.681880,-9.498715],[-3.806296,-3.420064,-2.048262,6.514478,-2.487872,-1.044189,3.785482,9.303574,0.228029,0.554603,8.568686,0.134296,-2.178924,3.016198,-2.598002,-4.598174],[4.427455,5.587188,-2.011778,1.013893,9.741337,-7.332035,-0.342089,9.104963,9.856847,-1.873934,-3.436211,-4.072332,6.587628,2.245559,-1.957179,-1.098575]],[[-7.383789,7.874730,4.112230,7.394617,-9.571144,6.299349,9.800198,8.106423,-1.793583,2.008102,6.884064,0.432445,1.739190,-1.497732,-9.088236,4.807785],[-0.001149,7.450485,-5.336115,3.531807,-9.175541,5.631710,8.214664,7.683985,7.414687,4.768661,-3.942661,7.402061,6.236776,5.445077,7.730358,2.217096],[9.746751,9.791409,2.962529,9.675898,1.484025,-0.840499,4.466240,-8.385058,-0.169429,7.488569,3.702066,3.200210,-0.093038,-6.361138,8.510148,3.593875],[0.338748,-3.719911,1.722298,-5.859359,0.825945,-6.145219,-6.832533,1.597395,-6.654709,-5.191407,6.890660,-5.528766,-9.811206,7.170830,-1.953515,1.137106],[8.515695,1.424574,6.967186,-8.966756,-6.115112,9.676115,1.071646,2.903627,3.918048,8.704291,0.105423,-5.429926,7.882479,-5.685534,-2.401654,0.554324],[8.798622,5.702928,-0.124280,4.306559,-4.285678,-3.924641,2.789381,1.913207,2.691134,-9.675316,-1.273959,-7.540105,-2.328102,-6.722383,-1.115036,5.583094],[-5.457203,-8.699272,-3.945709,0.282196,-7.113884,-4.295178,4.454524,-9.651928,3.777363,-6.090379,2.632785,3.141452,5.897262,7.276111,5.911961,7.592832]],[[2.625556,-9.300486,-4.262015,-7.333242,2.674706,-8.587336,-2.023463,3.617675,2.700180,6.019567,2.466379,0.463424,-0.468417,-1.679635,5.439523,6.485941],[-3.332966,-6.566528,1.326618,0.316184,7.342537,-7.553832,2.606058,0.283934,0.350558,5.288772,3.014192,1.493078,2.405920,9.212306,2.234900,3.334816],[9.566567,-6.890941,-4.641097,2.164577,-4.699159,8.173055,-2.038774,-3.755047,-2.213542,-1.277597,-9.804135,8.463470,4.849307,-3.408956,-9.756134,-1.218002],[0.943752,-1.894364,2.485220,-7.953174,2.880748,5.112945,-3.959533,1.446598,5.818224,5.088271,8.868221,-0.976089,4.194683,-1.295146,-4.171554,3.957315],[6.270383,-2.980637,-6.515679,-1.899878,-7.277457,1.867159,-2.623318,7.309061,-2.953887,2.094176,-7.815900,-8.371495,0.954492,7.712049,-7.997417,9.544297],[-9.523319,-8.103134,-5.274692,7.453556,-6.012286,-1.398833,5.775378,-2.230335,-8.626065,-2.287346,2.033600,-5.959088,7.108656,6.837385,9.731631,9.881230],[-6.183636,-0.838412,5.290111,9.784441,-0.251567,-0.561413,-0.618687,4.264780,-0.092144,3.957640,-1.869465,-0.518789,4.300625,4.516607,1.430161,-5.919911]],[[-9.993322,-8.278896,-2.362187,7.141482,0.704444,9.130159,3.877659,-5.247789,-7.966785,6.213800,-7.851426,-5.912564,7.038597,-5.773447,-7.065140,-7.096062],[3.717533,-8.449924,9.347915,-1.672497,3.284796,-9.239416,-7.967897,4.556446,-4.490228,0.943934,-5.383280,-7.376512,-8.638899,-2.380266,5.955893,7.265201],[-8.377545,6.748817,-9.721400,-0.860073,3.749019,-4.639892,-1.600635,-1.586434,-7.482008,3.833165,2.964809,8.342806,-0.313801,-9.672295,-3.260771,-4.380468],[-3.407730,-3.302567,4.793716,-0.299908,0.462585,-7.992642,-3.898370,-6.232182,-5.225509,-9.292699,8.522584,4.532340,7.422939,-2.410920,-1.451166,-8.505137],[-1.690452,8.683468,-9.166873,-1.042580,-7.192548,0.399043,3.294072,8.754449,5.014610,0.294263,6.535134,-6.665013,-4.201989,4.173294,5.847404,7.675879],[-8.163059,7.313589,6.685631,6.176511,-3.767933,-6.916195,-4.292329,2.269596,2.165170,3.931685,-4.498648,-5.242659,-7.792299,9.593668,0.609343,1.942341],[7.556134,-2.723849,-3.293670,-6.905148,-1.055200,-2.748690,-2.707221,-5.795969,-5.469812,2.113557,0.546917,2.132142,8.712411,0.556901,-6.919861,-9.551427]],[[6.491343,-0.804701,-7.717184,-4.467012,4.007604,-4.585112,0.994951,-1.515380,-4.579929,-9.252685,3.237704,4.946644,-1.241264,5.580532,7.151052,-0.905244],[4.084763,-4.058312,5.191461,-4.467870,8.439722,-3.092884,-1.036168,-9.746050,-7.163575,-1.088169,-4.531534,-7.789379,0.507260,3.569970,-8.679179,6.943609],[-5.753810,1.303438,0.402353,0.361031,-2.470009,6.672798,-1.977649,2.268815,-2.141064,-7.154181,3.943144,6.546684,-4.052845,5.246077,-6.876105,-0.607994],[-6.461231,-0.679618,-6.884855,-6.270521,3.765177,5.782732,6.607097,8.222331,-4.121623,0.987429,-0.727270,-7.925258,5.817750,9.835719,6.674534,7.273851],[-8.325751,5.019795,2.744383,2.527633,7.834722,-8.471498,-5.006006,-8.828245,5.125268,-6.871151,-9.605129,-9.850356,7.318220,9.243624,-1.235908,-9.379161],[-7.613591,9.733980,-3.108573,-1.999452,4.008951,-2.503241,-3.091139,-3.529182,-8.849701,-2.838429,-8.992176,7.443004,-2.683691,-3.435072,1.949951,3.606928],[-2.148988,0.171659,-4.811886,-3.029264,-6.160872,9.488170,8.623178,-5.892404,-6.389881,-0.085491,4.201962,-5.184876,-1.627718,-2.455812,-3.710310,0.667250]]], dtype = "float64")#candidate|3008|(8, 7, 16)|const|float64
bop_3009 = relay.maximum(var_3007.astype('float64'), relay.reshape(const_3008.astype('float64'), relay.shape_of(var_3007))) # shape=(8, 7, 16)
uop_3028 = relay.log2(bop_3009.astype('float64')) # shape=(8, 7, 16)
output = relay.Tuple([uop_3028,])
output2 = relay.Tuple([uop_3028,])
func_3033 = relay.Function([var_3007,], output)
mod['func_3033'] = func_3033
mod = relay.transform.InferType()(mod)
mutated_mod['func_3033'] = func_3033
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3034 = relay.var("var_3034", dtype = "float64", shape = (8, 7, 16))#candidate|3034|(8, 7, 16)|var|float64
func_3033_call = mutated_mod.get_global_var('func_3033')
call_3035 = func_3033_call(var_3034)
output = call_3035
func_3036 = relay.Function([var_3034], output)
mutated_mod['func_3036'] = func_3036
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_3117 = relay.TupleGetItem(func_665_call(), 0)
call_3118 = relay.TupleGetItem(func_666_call(), 0)
output = relay.Tuple([call_3117,])
output2 = relay.Tuple([call_3118,])
func_3119 = relay.Function([], output)
mod['func_3119'] = func_3119
mod = relay.transform.InferType()(mod)
mutated_mod['func_3119'] = func_3119
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3119_call = mutated_mod.get_global_var('func_3119')
call_3120 = func_3119_call()
output = call_3120
func_3121 = relay.Function([], output)
mutated_mod['func_3121'] = func_3121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2047_call = mod.get_global_var('func_2047')
func_2049_call = mutated_mod.get_global_var('func_2049')
call_3171 = func_2047_call()
call_3172 = func_2047_call()
uop_3183 = relay.asin(call_3171.astype('float32')) # shape=(4, 6, 4)
uop_3185 = relay.asin(call_3172.astype('float32')) # shape=(4, 6, 4)
output = relay.Tuple([uop_3183,])
output2 = relay.Tuple([uop_3185,])
func_3192 = relay.Function([], output)
mod['func_3192'] = func_3192
mod = relay.transform.InferType()(mod)
mutated_mod['func_3192'] = func_3192
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3192_call = mutated_mod.get_global_var('func_3192')
call_3193 = func_3192_call()
output = call_3193
func_3194 = relay.Function([], output)
mutated_mod['func_3194'] = func_3194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2593_call = mod.get_global_var('func_2593')
func_2595_call = mutated_mod.get_global_var('func_2595')
call_3224 = func_2593_call()
call_3225 = func_2593_call()
func_2357_call = mod.get_global_var('func_2357')
func_2359_call = mutated_mod.get_global_var('func_2359')
call_3259 = relay.TupleGetItem(func_2357_call(), 0)
call_3260 = relay.TupleGetItem(func_2359_call(), 0)
func_2411_call = mod.get_global_var('func_2411')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_3264 = func_2411_call()
call_3265 = func_2411_call()
var_3281 = relay.var("var_3281", dtype = "uint8", shape = (10, 2, 8))#candidate|3281|(10, 2, 8)|var|uint8
bop_3282 = relay.floor_mod(call_3264.astype('float32'), relay.reshape(var_3281.astype('float32'), relay.shape_of(call_3264))) # shape=(10, 2, 8)
bop_3285 = relay.floor_mod(call_3265.astype('float32'), relay.reshape(var_3281.astype('float32'), relay.shape_of(call_3265))) # shape=(10, 2, 8)
func_3119_call = mod.get_global_var('func_3119')
func_3121_call = mutated_mod.get_global_var('func_3121')
call_3286 = relay.TupleGetItem(func_3119_call(), 0)
call_3287 = relay.TupleGetItem(func_3121_call(), 0)
uop_3290 = relay.sigmoid(call_3264.astype('float32')) # shape=(10, 2, 8)
uop_3292 = relay.sigmoid(call_3265.astype('float32')) # shape=(10, 2, 8)
bop_3294 = relay.less_equal(uop_3290.astype('bool'), relay.reshape(bop_3282.astype('bool'), relay.shape_of(uop_3290))) # shape=(10, 2, 8)
bop_3297 = relay.less_equal(uop_3292.astype('bool'), relay.reshape(bop_3285.astype('bool'), relay.shape_of(uop_3292))) # shape=(10, 2, 8)
output = relay.Tuple([call_3224,call_3259,call_3286,bop_3294,])
output2 = relay.Tuple([call_3225,call_3260,call_3287,bop_3297,])
func_3299 = relay.Function([var_3281,], output)
mod['func_3299'] = func_3299
mod = relay.transform.InferType()(mod)
mutated_mod['func_3299'] = func_3299
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3300 = relay.var("var_3300", dtype = "uint8", shape = (10, 2, 8))#candidate|3300|(10, 2, 8)|var|uint8
func_3299_call = mutated_mod.get_global_var('func_3299')
call_3301 = func_3299_call(var_3300)
output = call_3301
func_3302 = relay.Function([var_3300], output)
mutated_mod['func_3302'] = func_3302
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2357_call = mod.get_global_var('func_2357')
func_2359_call = mutated_mod.get_global_var('func_2359')
call_3306 = relay.TupleGetItem(func_2357_call(), 0)
call_3307 = relay.TupleGetItem(func_2359_call(), 0)
output = call_3306
output2 = call_3307
func_3310 = relay.Function([], output)
mod['func_3310'] = func_3310
mod = relay.transform.InferType()(mod)
mutated_mod['func_3310'] = func_3310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3310_call = mutated_mod.get_global_var('func_3310')
call_3311 = func_3310_call()
output = call_3311
func_3312 = relay.Function([], output)
mutated_mod['func_3312'] = func_3312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_665_call = mod.get_global_var('func_665')
func_666_call = mutated_mod.get_global_var('func_666')
call_3330 = relay.TupleGetItem(func_665_call(), 0)
call_3331 = relay.TupleGetItem(func_666_call(), 0)
output = call_3330
output2 = call_3331
func_3352 = relay.Function([], output)
mod['func_3352'] = func_3352
mod = relay.transform.InferType()(mod)
output = func_3352()
func_3353 = relay.Function([], output)
mutated_mod['func_3353'] = func_3353
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_3365 = relay.TupleGetItem(func_2458_call(), 0)
call_3366 = relay.TupleGetItem(func_2459_call(), 0)
output = relay.Tuple([call_3365,])
output2 = relay.Tuple([call_3366,])
func_3375 = relay.Function([], output)
mod['func_3375'] = func_3375
mod = relay.transform.InferType()(mod)
output = func_3375()
func_3376 = relay.Function([], output)
mutated_mod['func_3376'] = func_3376
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2470_call = mod.get_global_var('func_2470')
func_2472_call = mutated_mod.get_global_var('func_2472')
call_3403 = func_2470_call()
call_3404 = func_2470_call()
output = call_3403
output2 = call_3404
func_3413 = relay.Function([], output)
mod['func_3413'] = func_3413
mod = relay.transform.InferType()(mod)
mutated_mod['func_3413'] = func_3413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3413_call = mutated_mod.get_global_var('func_3413')
call_3414 = func_3413_call()
output = call_3414
func_3415 = relay.Function([], output)
mutated_mod['func_3415'] = func_3415
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3432 = relay.const([[[3,-7,-2,5,4,9,-9,3,-1,-8,9],[9,-2,6,9,10,-9,-10,6,5,7,7],[-8,-5,3,5,-9,7,3,9,-9,1,6],[9,7,5,9,-9,-2,-5,-10,-7,5,2],[7,8,-2,4,-10,-1,10,-10,8,7,6],[5,2,-6,-5,-5,-2,8,3,2,-6,10],[-1,-4,-2,8,-1,-7,-6,10,-3,-4,7]],[[9,-4,5,7,6,8,4,-9,1,7,2],[10,5,-6,-8,-10,5,1,-6,7,-4,-1],[8,-3,1,6,-1,7,10,4,-8,-9,10],[5,6,-9,-7,-1,2,4,3,-1,6,10],[-1,8,-1,-4,-4,-9,9,3,10,-2,7],[8,-6,4,-6,10,9,9,-4,2,-2,-10],[-1,-8,4,-3,-6,1,-1,5,-9,7,2]],[[9,10,6,4,-10,9,-6,-10,6,-2,-7],[1,-2,-7,-10,6,-9,-3,-8,-10,-10,8],[6,6,3,10,-3,-4,-3,6,3,7,10],[-6,-6,7,-9,-3,5,6,7,10,9,5],[-6,-7,4,-1,-1,3,5,-5,-8,-7,6],[-1,-1,3,4,2,-10,10,-1,8,-8,-1],[-4,-7,-3,-3,10,-3,4,1,-3,-9,9]],[[9,-2,4,-10,5,1,6,6,4,5,9],[3,-9,-10,-1,10,1,-9,-2,-1,-4,-8],[-6,-10,-2,-10,-4,10,1,-2,3,4,-3],[-10,-3,1,1,6,4,2,10,-7,-4,8],[9,10,1,5,-9,9,3,-7,-9,-6,10],[-9,7,-5,-4,-8,2,-4,-2,-8,-3,-2],[9,3,-2,-1,6,-3,9,-5,2,8,1]],[[-6,3,5,3,4,-5,-9,7,-1,3,7],[-3,-5,-8,-8,4,-4,-2,-3,-4,-6,-6],[-8,-9,8,-5,4,-9,-5,-1,-6,9,-4],[-6,-5,-5,-9,-9,4,8,-2,8,10,-6],[-4,8,-3,-9,9,5,-8,-6,-1,-6,3],[-10,-6,10,4,1,-2,-8,-7,4,-4,9],[-9,-1,-9,9,2,8,6,3,3,-9,-4]],[[-10,6,8,-2,2,-3,-6,-3,-6,-4,4],[-2,1,-3,-10,7,-2,5,3,-9,1,-1],[6,-9,10,9,-5,-10,-8,-7,2,8,9],[3,1,8,-6,8,-2,8,-2,3,-10,2],[-8,6,-4,-5,8,-4,4,10,10,3,4],[-1,2,2,1,-2,4,10,-2,1,-6,6],[7,-9,-3,9,6,2,6,-10,9,-5,-9]],[[10,-1,-9,8,-7,3,-1,8,4,10,4],[1,2,-7,2,3,7,-5,-10,-4,-7,3],[-3,-10,7,-4,-7,-6,-4,7,8,10,-3],[-4,5,2,-6,1,-5,6,-2,-2,7,1],[2,-9,-9,8,3,7,-9,-1,-1,4,-5],[8,3,8,10,1,-7,-4,9,-8,-3,10],[3,9,-4,-2,7,6,-1,-10,-4,-3,-3]],[[-9,9,5,-4,6,-6,3,-9,-9,-6,4],[1,-10,-9,8,-10,-4,-4,-2,6,8,-2],[4,-8,6,9,-3,8,-7,-6,8,-2,6],[-3,-4,6,-1,-5,-10,7,8,5,-8,5],[-9,10,9,-8,-6,3,10,-4,-10,5,3],[-3,9,2,-3,5,-8,-7,-5,-1,-8,2],[6,8,-8,-5,6,-2,7,4,-1,-10,-2]],[[-5,4,9,-2,1,-1,-5,1,-8,7,-3],[3,2,6,4,-1,-6,-7,-8,-8,-1,7],[7,-6,-4,-4,7,4,-3,3,10,-6,-10],[3,-4,-8,-1,-8,2,5,7,5,-9,3],[-9,7,10,-10,-6,10,-8,-4,-1,9,-8],[-1,4,-9,5,4,8,-5,-7,-1,-10,5],[-7,-6,3,4,-10,6,-1,8,7,-9,-7]],[[3,1,-9,5,6,-4,2,8,9,-1,3],[-8,-7,6,9,-2,7,8,-4,-1,5,-3],[-3,3,2,-6,7,7,-10,9,6,4,5],[-1,-7,9,8,-8,-4,4,6,-10,-6,6],[4,7,-7,5,-5,10,9,-3,-3,9,-4],[5,4,5,-6,8,-6,-10,-10,-6,-1,8],[-8,-8,-3,-10,1,7,3,-7,-2,-7,-2]],[[1,1,-8,6,4,-4,-4,-1,-4,-10,-8],[-4,9,2,4,4,5,-5,-10,8,4,8],[8,2,2,6,6,4,6,3,1,7,3],[-8,2,8,-9,2,4,1,8,5,-7,-9],[-7,3,2,-4,2,9,-10,-10,1,-6,7],[-10,-5,9,4,-5,2,6,9,-8,-4,5],[-2,-2,-6,-8,8,-10,-1,-6,-8,-5,-8]],[[6,-3,-8,-1,-4,9,-8,6,2,5,10],[-10,2,-7,8,-2,-5,-1,3,-8,-7,-2],[-6,4,-6,-7,-7,-1,4,-8,5,9,4],[-3,-1,5,-9,-4,7,10,-7,8,-5,4],[8,2,-1,-3,10,-3,6,7,-5,2,-1],[7,-1,-1,-5,6,7,9,10,3,8,8],[-4,-3,8,-2,8,-6,-4,7,-3,5,2]],[[8,-7,-9,6,1,2,8,-9,-10,10,8],[-4,7,10,7,-7,-2,-7,9,8,-3,6],[-4,-4,4,10,-1,-8,2,-10,10,8,-2],[-2,-8,3,-3,-7,-5,-1,8,-10,-4,7],[8,6,5,-7,9,-9,2,-2,-2,3,-1],[-8,-4,8,-9,-5,-2,-3,7,5,-3,-4],[-8,-3,-7,-2,1,-7,-8,-6,-2,4,-3]],[[3,10,7,4,-10,8,-7,-10,-3,-8,-7],[-7,-5,-3,5,9,8,-9,3,-6,10,-8],[9,5,-10,-4,1,-7,2,-5,-8,6,4],[-10,-1,-3,10,-7,9,1,-4,6,6,-2],[-5,-5,3,-8,-7,5,-5,-8,-10,-4,-8],[8,-9,9,-10,-4,-10,-10,10,-8,-8,-6],[1,-6,10,10,4,-2,-4,10,2,1,-1]]], dtype = "uint8")#candidate|3432|(14, 7, 11)|const|uint8
var_3433 = relay.var("var_3433", dtype = "uint8", shape = (14, 7, 11))#candidate|3433|(14, 7, 11)|var|uint8
bop_3434 = relay.bitwise_and(const_3432.astype('uint8'), relay.reshape(var_3433.astype('uint8'), relay.shape_of(const_3432))) # shape=(14, 7, 11)
const_3441 = relay.const([[[-1,3,7,2,7,6,-4,2,-4,3,-7],[-6,-8,-5,9,10,6,1,9,9,-5,-2],[1,-4,4,-7,-6,-5,-5,3,-10,6,-6],[-7,4,3,-2,10,-10,8,-10,4,-7,10],[-9,-8,8,5,4,-9,10,6,8,5,10],[1,-8,6,3,-9,-1,-1,4,-2,-10,5],[-4,3,-6,-1,10,6,4,5,-10,-2,-3]],[[9,-1,-4,-6,2,-1,-4,-3,-5,7,-3],[3,-10,2,3,7,5,-5,-10,9,2,8],[6,1,4,-3,10,-5,-1,4,-4,-8,-10],[7,3,-3,5,1,5,-5,1,-6,-7,1],[1,2,4,-4,2,-6,9,-1,3,8,-5],[6,4,-5,6,9,-9,3,-8,2,2,8],[-7,8,1,9,10,2,-1,4,-4,5,1]],[[-1,-8,-10,8,2,7,9,-5,-5,-6,-10],[5,6,-5,3,10,-7,-4,9,-7,1,-2],[-3,1,-3,-5,5,4,-9,2,-7,7,-1],[10,-5,4,2,-8,-2,-3,5,-7,-9,-2],[10,-2,6,-10,10,-10,9,-3,-7,-6,-10],[-5,8,-9,-3,-5,5,-9,-9,-10,10,-6],[-4,-2,1,-2,-8,10,-9,10,10,-4,-7]],[[7,-3,-6,7,-2,2,3,-3,-6,4,-4],[5,-2,3,9,8,-5,3,3,-3,2,-2],[-7,-2,3,-9,8,3,6,-5,-6,-10,-5],[2,4,7,-1,3,-2,-2,-2,4,-2,1],[4,4,-10,-3,-9,4,-2,-9,8,2,-10],[6,3,3,10,-7,9,-6,-8,-5,6,2],[2,1,-5,3,5,-7,-1,8,-4,6,8]],[[2,1,-5,-1,-4,-8,5,8,-1,7,-5],[-8,-10,10,6,5,4,-9,2,-7,5,3],[-9,7,-8,-7,5,-6,10,10,-3,-5,-1],[-7,-6,-3,-10,-10,9,-10,-4,-2,4,3],[-5,9,-7,7,1,-5,10,6,6,8,5],[-4,5,-9,3,3,4,6,-8,-3,6,-4],[6,6,-7,-7,4,-1,-7,-10,-2,-10,4]],[[-10,-8,-1,-1,-1,-6,8,1,6,-9,4],[7,8,-6,-6,4,-5,8,-5,3,-5,2],[4,1,9,-7,7,9,-3,-2,9,6,-8],[-2,-3,-8,-5,4,-6,-9,6,-9,2,-6],[5,4,6,10,6,7,-6,-10,7,-8,2],[7,-3,-8,-4,-10,6,5,-5,8,-4,1],[-3,-10,-6,5,-6,-5,-9,-6,1,4,-1]],[[1,-3,-7,5,-6,10,9,4,5,6,-3],[-5,2,6,-3,-6,-6,3,-3,-3,7,6],[-1,-1,2,-8,-6,3,-9,3,-7,6,7],[7,10,-10,-5,-6,-7,-5,-6,-2,-6,-2],[6,-4,-4,8,-2,3,7,10,10,-8,-2],[-3,-6,5,-2,4,10,-2,-10,8,-7,5],[-4,6,10,-8,7,-5,8,4,4,-1,7]],[[1,-4,-1,-1,5,-3,7,4,-8,-9,-5],[-10,9,8,8,-3,-5,9,-10,-6,6,-5],[-3,-8,-4,-1,-4,-10,2,-4,5,1,-4],[10,1,-8,-3,9,6,4,-6,10,5,6],[-10,-10,-6,9,-1,6,2,10,1,-3,1],[-6,2,9,-6,7,-3,-4,-9,-1,-1,4],[-2,-1,8,-7,-1,5,9,-3,9,4,8]],[[-3,9,9,2,3,10,9,8,-6,-1,2],[-5,6,4,5,7,1,5,-8,-3,-3,7],[-2,7,3,7,9,-10,-3,4,8,-10,-7],[-7,2,-6,-3,-8,-7,3,5,3,1,9],[-8,3,-6,3,8,8,1,8,6,-9,2],[-3,1,3,1,-5,8,-7,1,-8,1,10],[10,6,-3,-1,6,-4,-1,-8,-10,1,10]],[[-2,7,1,-6,10,8,-3,10,8,9,-4],[8,3,4,7,2,-7,9,-9,-9,-10,6],[10,7,-3,-7,-7,10,6,-3,-7,4,6],[-2,-8,-5,-9,-2,-6,-4,-7,7,-7,-1],[-10,-6,9,-3,-3,9,7,10,2,3,-2],[8,-10,-1,-3,-10,7,2,-7,-9,9,2],[2,1,5,-2,3,-4,7,9,-8,-3,-6]],[[10,-1,6,7,-5,1,2,10,-2,-6,-5],[2,4,-5,-4,3,6,5,3,9,10,4],[5,8,8,-4,8,8,-5,-1,4,4,-10],[-2,-10,1,-1,4,10,5,-7,-2,6,-8],[-3,-1,7,-8,2,-9,1,4,6,1,-9],[5,-7,4,-9,4,3,8,9,-6,6,-5],[5,10,-7,-1,-9,-4,-5,8,1,5,-5]],[[6,1,-7,7,-5,-1,-8,-7,-5,-5,-1],[-9,4,10,6,4,-1,5,-3,10,-9,-4],[9,5,-6,-7,1,-5,-8,6,-2,7,9],[-1,-4,-10,-2,-9,-6,9,5,10,-9,-2],[-1,10,-1,9,9,-2,-3,-8,-9,-7,1],[8,9,-3,2,-7,6,-8,-6,-8,-9,10],[5,6,-4,10,9,3,-7,-10,4,3,9]],[[-6,10,-2,4,-8,9,-4,9,10,5,7],[2,2,7,5,-9,-2,4,-8,7,9,2],[-1,-9,-8,-8,6,-4,-5,4,-8,-10,-1],[-6,5,7,-9,7,-9,-3,-3,-1,1,9],[-8,-8,7,-9,-4,-7,8,1,4,-9,6],[-7,-5,8,-6,3,-2,-2,-1,-7,-8,4],[-10,-5,-2,-5,-8,-7,-5,-8,4,6,-4]],[[-4,1,-2,8,3,10,2,2,-2,4,-1],[6,1,-3,-7,7,-6,5,-5,3,-10,-8],[4,-4,10,6,8,-5,4,-9,-8,4,-5],[1,1,10,6,-8,9,9,-1,-3,8,9],[5,-5,-4,-7,6,-9,-2,10,8,-10,-9],[6,-5,10,-8,-7,9,-8,-1,-2,-2,7],[1,-4,5,-5,7,4,-2,-7,-3,3,-8]]], dtype = "uint8")#candidate|3441|(14, 7, 11)|const|uint8
bop_3442 = relay.greater_equal(var_3433.astype('bool'), relay.reshape(const_3441.astype('bool'), relay.shape_of(var_3433))) # shape=(14, 7, 11)
func_2593_call = mod.get_global_var('func_2593')
func_2595_call = mutated_mod.get_global_var('func_2595')
call_3451 = func_2593_call()
call_3452 = func_2593_call()
bop_3463 = relay.minimum(bop_3442.astype('int16'), relay.reshape(const_3432.astype('int16'), relay.shape_of(bop_3442))) # shape=(14, 7, 11)
output = relay.Tuple([bop_3434,call_3451,bop_3463,])
output2 = relay.Tuple([bop_3434,call_3452,bop_3463,])
func_3466 = relay.Function([var_3433,], output)
mod['func_3466'] = func_3466
mod = relay.transform.InferType()(mod)
var_3467 = relay.var("var_3467", dtype = "uint8", shape = (14, 7, 11))#candidate|3467|(14, 7, 11)|var|uint8
output = func_3466(var_3467)
func_3468 = relay.Function([var_3467], output)
mutated_mod['func_3468'] = func_3468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2411_call = mod.get_global_var('func_2411')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_3566 = func_2411_call()
call_3567 = func_2411_call()
output = relay.Tuple([call_3566,])
output2 = relay.Tuple([call_3567,])
func_3574 = relay.Function([], output)
mod['func_3574'] = func_3574
mod = relay.transform.InferType()(mod)
output = func_3574()
func_3575 = relay.Function([], output)
mutated_mod['func_3575'] = func_3575
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2383_call = mod.get_global_var('func_2383')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_3630 = relay.TupleGetItem(func_2383_call(), 0)
call_3631 = relay.TupleGetItem(func_2384_call(), 0)
output = call_3630
output2 = call_3631
func_3634 = relay.Function([], output)
mod['func_3634'] = func_3634
mod = relay.transform.InferType()(mod)
mutated_mod['func_3634'] = func_3634
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3634_call = mutated_mod.get_global_var('func_3634')
call_3635 = func_3634_call()
output = call_3635
func_3636 = relay.Function([], output)
mutated_mod['func_3636'] = func_3636
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1297_call = mod.get_global_var('func_1297')
func_1298_call = mutated_mod.get_global_var('func_1298')
call_3639 = relay.TupleGetItem(func_1297_call(), 0)
call_3640 = relay.TupleGetItem(func_1298_call(), 0)
var_3645 = relay.var("var_3645", dtype = "uint8", shape = (10, 2, 8))#candidate|3645|(10, 2, 8)|var|uint8
bop_3646 = relay.floor_divide(call_3639.astype('float32'), relay.reshape(var_3645.astype('float32'), relay.shape_of(call_3639))) # shape=(10, 2, 8)
bop_3649 = relay.floor_divide(call_3640.astype('float32'), relay.reshape(var_3645.astype('float32'), relay.shape_of(call_3640))) # shape=(10, 2, 8)
func_1734_call = mod.get_global_var('func_1734')
func_1736_call = mutated_mod.get_global_var('func_1736')
const_3662 = relay.const([-1.220128,-5.383296,-1.754286,7.359811,-7.554573,8.602981,0.920544,4.314595,-0.993695,-0.484784,9.434225,1.342394,5.827041,-6.062191,-4.555050,6.360503,3.916037,-0.505961,7.310611,-0.220168,6.294958,-5.495021,-5.571479,-7.760833,3.121251,-3.695015,0.696914,-1.434038,6.886225,6.341136,-2.701327,9.752581,-0.596159,9.675181,6.659793,9.274376], dtype = "float64")#candidate|3662|(36,)|const|float64
call_3661 = relay.TupleGetItem(func_1734_call(relay.reshape(const_3662.astype('float64'), [36,])), 3)
call_3663 = relay.TupleGetItem(func_1736_call(relay.reshape(const_3662.astype('float64'), [36,])), 3)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_3664 = func_525_call()
call_3665 = func_525_call()
output = relay.Tuple([bop_3646,call_3661,const_3662,call_3664,])
output2 = relay.Tuple([bop_3649,call_3663,const_3662,call_3665,])
func_3668 = relay.Function([var_3645,], output)
mod['func_3668'] = func_3668
mod = relay.transform.InferType()(mod)
var_3669 = relay.var("var_3669", dtype = "uint8", shape = (10, 2, 8))#candidate|3669|(10, 2, 8)|var|uint8
output = func_3668(var_3669)
func_3670 = relay.Function([var_3669], output)
mutated_mod['func_3670'] = func_3670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1362_call = mod.get_global_var('func_1362')
func_1364_call = mutated_mod.get_global_var('func_1364')
call_3675 = relay.TupleGetItem(func_1362_call(), 0)
call_3676 = relay.TupleGetItem(func_1364_call(), 0)
var_3679 = relay.var("var_3679", dtype = "float64", shape = (2, 14, 3))#candidate|3679|(2, 14, 3)|var|float64
bop_3680 = relay.not_equal(call_3675.astype('bool'), relay.reshape(var_3679.astype('bool'), relay.shape_of(call_3675))) # shape=(2, 14, 3)
bop_3683 = relay.not_equal(call_3676.astype('bool'), relay.reshape(var_3679.astype('bool'), relay.shape_of(call_3676))) # shape=(2, 14, 3)
func_1297_call = mod.get_global_var('func_1297')
func_1298_call = mutated_mod.get_global_var('func_1298')
call_3691 = relay.TupleGetItem(func_1297_call(), 0)
call_3692 = relay.TupleGetItem(func_1298_call(), 0)
func_3192_call = mod.get_global_var('func_3192')
func_3194_call = mutated_mod.get_global_var('func_3194')
call_3698 = relay.TupleGetItem(func_3192_call(), 0)
call_3699 = relay.TupleGetItem(func_3194_call(), 0)
output = relay.Tuple([bop_3680,call_3691,call_3698,])
output2 = relay.Tuple([bop_3683,call_3692,call_3699,])
func_3714 = relay.Function([var_3679,], output)
mod['func_3714'] = func_3714
mod = relay.transform.InferType()(mod)
var_3715 = relay.var("var_3715", dtype = "float64", shape = (2, 14, 3))#candidate|3715|(2, 14, 3)|var|float64
output = func_3714(var_3715)
func_3716 = relay.Function([var_3715], output)
mutated_mod['func_3716'] = func_3716
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2914_call = mod.get_global_var('func_2914')
func_2915_call = mutated_mod.get_global_var('func_2915')
call_3718 = func_2914_call()
call_3719 = func_2914_call()
func_3668_call = mod.get_global_var('func_3668')
func_3670_call = mutated_mod.get_global_var('func_3670')
const_3723 = relay.const([2,-5,-1,5,-8,5,-8,2,-3,8,4,8,-6,-5,7,-4,-6,-10,-9,4,-9,-3,-4,-8,2,4,-9,7,5,10,-2,10,5,-2,6,-4,-9,-3,-9,-7,9,8,6,-3,7,-2,8,-4,4,5,-6,-5,3,-5,3,5,5,-7,-9,3,-4,3,-9,-2,5,-2,-6,3,7,6,-1,-1,4,-9,-10,9,7,3,6,-8,-3,-1,7,2,3,-5,9,-5,6,8,-8,8,-6,1,6,-3,10,-10,10,-3,8,-9,6,1,-8,5,-5,-1,-6,3,4,1,-1,-2,-2,4,-5,-8,7,-2,-8,2,2,4,-8,9,4,9,-2,-8,8,-6,-7,3,-6,8,1,-7,5,-10,10,-6,-1,2,8,8,6,-8,-10,6,5,10,-3,-1,-10,-3,2,7,-4,7], dtype = "uint8")#candidate|3723|(160,)|const|uint8
call_3722 = relay.TupleGetItem(func_3668_call(relay.reshape(const_3723.astype('uint8'), [10, 2, 8])), 3)
call_3724 = relay.TupleGetItem(func_3670_call(relay.reshape(const_3723.astype('uint8'), [10, 2, 8])), 3)
output = relay.Tuple([call_3718,call_3722,const_3723,])
output2 = relay.Tuple([call_3719,call_3724,const_3723,])
func_3727 = relay.Function([], output)
mod['func_3727'] = func_3727
mod = relay.transform.InferType()(mod)
output = func_3727()
func_3728 = relay.Function([], output)
mutated_mod['func_3728'] = func_3728
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2160_call = mod.get_global_var('func_2160')
func_2161_call = mutated_mod.get_global_var('func_2161')
call_3751 = relay.TupleGetItem(func_2160_call(), 0)
call_3752 = relay.TupleGetItem(func_2161_call(), 0)
func_2357_call = mod.get_global_var('func_2357')
func_2359_call = mutated_mod.get_global_var('func_2359')
call_3755 = relay.TupleGetItem(func_2357_call(), 0)
call_3756 = relay.TupleGetItem(func_2359_call(), 0)
uop_3764 = relay.exp(call_3751.astype('float64')) # shape=(2, 14, 3)
uop_3766 = relay.exp(call_3752.astype('float64')) # shape=(2, 14, 3)
output = relay.Tuple([call_3755,uop_3764,])
output2 = relay.Tuple([call_3756,uop_3766,])
func_3770 = relay.Function([], output)
mod['func_3770'] = func_3770
mod = relay.transform.InferType()(mod)
mutated_mod['func_3770'] = func_3770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3770_call = mutated_mod.get_global_var('func_3770')
call_3771 = func_3770_call()
output = call_3771
func_3772 = relay.Function([], output)
mutated_mod['func_3772'] = func_3772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2925_call = mod.get_global_var('func_2925')
func_2926_call = mutated_mod.get_global_var('func_2926')
call_3773 = relay.TupleGetItem(func_2925_call(), 1)
call_3774 = relay.TupleGetItem(func_2926_call(), 1)
func_2458_call = mod.get_global_var('func_2458')
func_2459_call = mutated_mod.get_global_var('func_2459')
call_3796 = relay.TupleGetItem(func_2458_call(), 0)
call_3797 = relay.TupleGetItem(func_2459_call(), 0)
func_799_call = mod.get_global_var('func_799')
func_802_call = mutated_mod.get_global_var('func_802')
const_3815 = relay.const([-9.212083,-6.559739,1.434617,2.938707,-0.471776,-9.019493,0.038011,8.254540,-9.613305,4.200087,-0.340614,7.920730,-7.075763,9.077859,7.377651,-7.404715,2.151004,-0.254397,7.165531,6.136423,-3.948346,-5.668768,-5.850825,-7.515351,-7.053162,3.567761,5.546464,8.367771,1.758570,-2.800930,8.989796,1.022234,9.950208,-9.639198,0.584332,-8.776688], dtype = "float64")#candidate|3815|(36,)|const|float64
const_3816 = relay.const([9,-4,1,3,4,-2,-5,-2,7,4,1,10,7,6,6,-3,-1,4,-6,-9,-8,-7,-3,8,10,-8,3,7,-1,7,-8,-2,7,10,-6,4,-8,-9,-4,3,-8,7,10,1,-8,-9,-1,5,1,-3,-4,5,10,5,10,9,8,9,-9,9,1,6,-1,9,-6,-2,-9,-2,-10,4,2,8,-9,-10,-1,10,7,3,-4,-3,-5,1,-10,7,-8,10,6,4,6,8,10,-9,-1,-6,-5,7,4,7,9,-3,-5,-10,2,-8,5,8,-1,4,-9,9,1,-7,-4,-8,10,-1,-4,-8,3,5,-2,-5,9,-7,2,-6,1,-10,10,7,9,5,-1,2,-10,3,-9,5,10,10,-7,8,10,3,6,-9,10,-8,8,-4,-6,-10,-7,-7,-6,-2,-3,-1,8,2,5,-9,-7,5,-9,-6,8,-2,-1,-6,5,-2,-8,-1,10,-10,-5,10,-6,-9], dtype = "uint64")#candidate|3816|(180,)|const|uint64
call_3814 = relay.TupleGetItem(func_799_call(relay.reshape(const_3815.astype('float64'), [36,]), relay.reshape(const_3816.astype('uint64'), [180, 1]), ), 0)
call_3817 = relay.TupleGetItem(func_802_call(relay.reshape(const_3815.astype('float64'), [36,]), relay.reshape(const_3816.astype('uint64'), [180, 1]), ), 0)
output = relay.Tuple([call_3773,call_3796,call_3814,const_3815,const_3816,])
output2 = relay.Tuple([call_3774,call_3797,call_3817,const_3815,const_3816,])
func_3836 = relay.Function([], output)
mod['func_3836'] = func_3836
mod = relay.transform.InferType()(mod)
mutated_mod['func_3836'] = func_3836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3836_call = mutated_mod.get_global_var('func_3836')
call_3837 = func_3836_call()
output = call_3837
func_3838 = relay.Function([], output)
mutated_mod['func_3838'] = func_3838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2086_call = mod.get_global_var('func_2086')
func_2088_call = mutated_mod.get_global_var('func_2088')
call_3936 = relay.TupleGetItem(func_2086_call(), 0)
call_3937 = relay.TupleGetItem(func_2088_call(), 0)
output = call_3936
output2 = call_3937
func_3939 = relay.Function([], output)
mod['func_3939'] = func_3939
mod = relay.transform.InferType()(mod)
output = func_3939()
func_3940 = relay.Function([], output)
mutated_mod['func_3940'] = func_3940
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2730_call = mod.get_global_var('func_2730')
func_2732_call = mutated_mod.get_global_var('func_2732')
call_3987 = relay.TupleGetItem(func_2730_call(), 1)
call_3988 = relay.TupleGetItem(func_2732_call(), 1)
uop_3991 = relay.exp(call_3987.astype('float32')) # shape=(10, 2, 8)
uop_3993 = relay.exp(call_3988.astype('float32')) # shape=(10, 2, 8)
func_617_call = mod.get_global_var('func_617')
func_619_call = mutated_mod.get_global_var('func_619')
const_3996 = relay.const([2.167047,-6.735273,8.379141,1.693851,6.722647,-8.499764,1.575509,-0.540934,9.925110,-8.898737,9.227778,4.418625,-5.580291,-2.488495,-1.879143,2.335733,9.988958,-0.384142,-2.275963,-0.529812,-8.130668,1.173109,-5.145522,2.934874,2.224058,-2.771263,-0.953939,-8.009390,7.374732,-8.963724,-5.662296,-3.880738,9.837447,-3.164879,-0.679834,-4.663970,3.360502,-5.025981,3.160121,-0.368967,0.655056,-0.536430,-6.832812,8.284069,0.550484,-7.076881,3.667399,5.263129,3.705887,-0.879776,-8.874990,-1.862549,2.614362,-8.981139,-2.477088,1.495032,0.018448,2.097630,-8.277750,-5.805562,-6.278803,-6.856848,0.738855,5.798446,9.044107,-4.062499,-4.288075,-1.070032,9.784627,-5.153714,5.531927,9.147152,6.313909,-3.943031,1.989594,7.056042,8.969805,3.663080,-7.691530,1.323994,6.273824,5.262374,-0.949356,6.332530,-1.948718,5.416369,4.905873,8.635931,8.793815,-7.615838,-3.400285,5.171680,7.033534,-7.396357,8.587453,-2.297055,9.693919,-3.485891,4.891310,8.978521,1.175361,6.480818,9.301359,-5.113728,-2.875889,-0.478027,-1.944044,5.936856,-0.836321,4.218349,6.191611,-7.288661,-9.574401,5.306972,-0.656836,8.732671,0.142095,-9.299596,3.007232,-1.769285,-7.625932,-2.030992,-4.688272,-3.519204,5.844311,-1.783714,6.320565,3.551865,5.653216,4.145891,1.518498,7.055475,4.322090,-9.369022,-4.922536,7.399566,0.845646,-9.398398,9.201487,-8.196645,-8.113385,2.401805,-0.622866,0.722355,6.551731,4.585905,-3.690275,-8.200001,4.661442,-0.814933,3.145206,-7.505653,-7.330162,-5.277598,6.605788,-9.393186,0.767139,-0.555717,0.380072,9.461605,-9.754851,2.566712,7.219330,0.326176,-6.034333,2.325786,2.566056,-7.934439,-5.928450,1.441891,-5.019469,1.441895,7.438607,4.345593,-8.359587,-4.507314,0.189066,8.496773,6.619331,2.202891,-9.979212,8.176104,-2.894783,1.969908,-4.162984,3.685224,5.602826,-7.701875,-5.843388,9.270534,-9.288590,8.567364,3.323169,-1.336859,9.724715,3.739670,-7.247777,2.829896,-1.521034,1.355720,0.879311,3.734633,-2.595724,-5.620687,8.199076,3.809853,4.450339,-7.711808,8.586849,5.030496,-5.661814,-6.028134,6.913170,-3.711549,9.679437,-2.193450,-2.579883,2.190529,4.357711,6.640953,0.774194,-1.168237,2.451533,1.883493,5.892857,-8.100436,6.000293,8.967737,-6.288505,5.274824,6.058680,9.174849,4.116907,-3.626048,-1.314829,-2.989494,-0.450713,-2.683823,0.791805,-4.285169,-1.060314,-7.288606,-5.833838,-5.116346,5.251855,-0.483960,5.279018,-8.817785,-1.576839,1.260367,-2.460682,-6.508507,-4.661482,2.547714,-3.196232,-9.841451,-9.231577,5.742844,-6.021692,8.783915,7.694020,4.175916,9.760905,0.366908,-6.772046,-1.958487,-3.835445,-2.903839,1.614475,-1.404764,8.788669,-6.194947,-1.772404,-7.477451,1.849212,-8.069000,4.674680,2.309811,-5.537383,-3.827416], dtype = "float32")#candidate|3996|(280,)|const|float32
call_3995 = relay.TupleGetItem(func_617_call(relay.reshape(const_3996.astype('float32'), [280, 1])), 2)
call_3997 = relay.TupleGetItem(func_619_call(relay.reshape(const_3996.astype('float32'), [280, 1])), 2)
func_3310_call = mod.get_global_var('func_3310')
func_3312_call = mutated_mod.get_global_var('func_3312')
call_4002 = func_3310_call()
call_4003 = func_3310_call()
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_4007 = relay.TupleGetItem(func_1517_call(), 0)
call_4008 = relay.TupleGetItem(func_1519_call(), 0)
output = relay.Tuple([uop_3991,call_3995,const_3996,call_4002,call_4007,])
output2 = relay.Tuple([uop_3993,call_3997,const_3996,call_4003,call_4008,])
func_4009 = relay.Function([], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
output = func_4009()
func_4010 = relay.Function([], output)
mutated_mod['func_4010'] = func_4010
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4087 = relay.var("var_4087", dtype = "int64", shape = (9, 2, 11))#candidate|4087|(9, 2, 11)|var|int64
const_4088 = relay.const([[[-5,9,-7,4,4,4,4,5,-5,3,-8],[-4,6,2,-1,-9,1,4,9,-1,9,4]],[[1,1,6,1,-2,6,6,9,4,-4,8],[-5,8,-9,3,10,-3,-1,8,1,-8,-9]],[[7,-2,6,8,-3,-8,-8,8,10,-7,-1],[-2,-2,-9,1,5,-4,1,-2,-3,-9,-4]],[[9,10,9,2,8,1,6,8,-7,-5,1],[-2,-2,-8,7,-10,3,6,9,-6,-10,5]],[[-6,-3,-8,-6,2,-2,3,7,-1,6,9],[7,-10,3,9,-5,-2,6,7,-9,-9,5]],[[-10,-4,9,4,-2,6,-4,-1,6,8,6],[-8,-7,4,-9,-10,1,-7,-3,-8,1,-8]],[[-4,10,9,-10,1,10,6,-3,-2,3,6],[2,10,-6,-8,8,5,2,5,9,-1,-5]],[[2,3,3,-5,-3,-8,-1,-5,-1,10,2],[-8,-3,4,-7,-2,-1,4,8,-2,-10,-7]],[[-7,1,5,3,-1,-4,-9,10,-1,8,-7],[5,4,10,10,-5,8,-6,-7,-2,-2,-5]]], dtype = "int64")#candidate|4088|(9, 2, 11)|const|int64
bop_4089 = relay.not_equal(var_4087.astype('bool'), relay.reshape(const_4088.astype('bool'), relay.shape_of(var_4087))) # shape=(9, 2, 11)
func_1734_call = mod.get_global_var('func_1734')
func_1736_call = mutated_mod.get_global_var('func_1736')
var_4094 = relay.var("var_4094", dtype = "float64", shape = (3, 12))#candidate|4094|(3, 12)|var|float64
call_4093 = relay.TupleGetItem(func_1734_call(relay.reshape(var_4094.astype('float64'), [36,])), 1)
call_4095 = relay.TupleGetItem(func_1736_call(relay.reshape(var_4094.astype('float64'), [36,])), 1)
uop_4097 = relay.rsqrt(const_4088.astype('float32')) # shape=(9, 2, 11)
output = relay.Tuple([bop_4089,call_4093,var_4094,uop_4097,])
output2 = relay.Tuple([bop_4089,call_4095,var_4094,uop_4097,])
func_4117 = relay.Function([var_4087,var_4094,], output)
mod['func_4117'] = func_4117
mod = relay.transform.InferType()(mod)
var_4118 = relay.var("var_4118", dtype = "int64", shape = (9, 2, 11))#candidate|4118|(9, 2, 11)|var|int64
var_4119 = relay.var("var_4119", dtype = "float64", shape = (3, 12))#candidate|4119|(3, 12)|var|float64
output = func_4117(var_4118,var_4119,)
func_4120 = relay.Function([var_4118,var_4119,], output)
mutated_mod['func_4120'] = func_4120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_4133 = relay.TupleGetItem(func_1517_call(), 0)
call_4134 = relay.TupleGetItem(func_1519_call(), 0)
output = relay.Tuple([call_4133,])
output2 = relay.Tuple([call_4134,])
func_4143 = relay.Function([], output)
mod['func_4143'] = func_4143
mod = relay.transform.InferType()(mod)
mutated_mod['func_4143'] = func_4143
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4143_call = mutated_mod.get_global_var('func_4143')
call_4144 = func_4143_call()
output = call_4144
func_4145 = relay.Function([], output)
mutated_mod['func_4145'] = func_4145
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4187 = relay.var("var_4187", dtype = "float32", shape = (3, 9, 6))#candidate|4187|(3, 9, 6)|var|float32
uop_4188 = relay.exp(var_4187.astype('float32')) # shape=(3, 9, 6)
func_2086_call = mod.get_global_var('func_2086')
func_2088_call = mutated_mod.get_global_var('func_2088')
call_4192 = relay.TupleGetItem(func_2086_call(), 0)
call_4193 = relay.TupleGetItem(func_2088_call(), 0)
bop_4203 = relay.right_shift(uop_4188.astype('uint32'), relay.reshape(var_4187.astype('uint32'), relay.shape_of(uop_4188))) # shape=(3, 9, 6)
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_4206 = relay.TupleGetItem(func_1517_call(), 0)
call_4207 = relay.TupleGetItem(func_1519_call(), 0)
bop_4212 = relay.floor_mod(uop_4188.astype('float32'), relay.reshape(bop_4203.astype('float32'), relay.shape_of(uop_4188))) # shape=(3, 9, 6)
output = relay.Tuple([call_4192,call_4206,bop_4212,])
output2 = relay.Tuple([call_4193,call_4207,bop_4212,])
func_4216 = relay.Function([var_4187,], output)
mod['func_4216'] = func_4216
mod = relay.transform.InferType()(mod)
mutated_mod['func_4216'] = func_4216
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4217 = relay.var("var_4217", dtype = "float32", shape = (3, 9, 6))#candidate|4217|(3, 9, 6)|var|float32
func_4216_call = mutated_mod.get_global_var('func_4216')
call_4218 = func_4216_call(var_4217)
output = call_4218
func_4219 = relay.Function([var_4217], output)
mutated_mod['func_4219'] = func_4219
mutated_mod = relay.transform.InferType()(mutated_mod)
const_4234 = relay.const([[[10,-1,-10,-8,-5,9,-10,-7,-7,5,-5,-4]],[[-7,-3,-5,-2,-5,-1,-2,-7,9,-10,-8,-3]],[[8,-2,-1,1,9,10,9,6,-7,-8,9,7]],[[-5,6,-3,-10,-7,4,-9,7,9,2,9,1]],[[-7,4,-8,4,7,-7,-9,1,-7,5,10,-4]],[[9,-8,-5,2,-1,8,5,-1,1,3,4,5]],[[9,-7,-4,-9,-8,9,7,5,-8,-5,4,7]]], dtype = "int8")#candidate|4234|(7, 1, 12)|const|int8
const_4235 = relay.const([[[5,-4,-1,2,3,1,-9,8,-4,9,-10,2],[-10,-3,-2,-7,-8,-7,5,10,-7,9,-2,4],[-1,-5,8,8,2,4,-10,10,1,10,1,1],[3,-4,6,-10,10,10,3,-5,9,-8,8,10],[9,3,-10,-8,6,-7,-9,-1,-4,-7,7,1],[-9,7,-9,7,7,-8,8,-9,7,7,4,-4],[-9,3,-1,3,3,1,7,2,10,10,-3,2],[-6,5,-9,8,10,-7,8,-4,2,-7,-3,-2],[6,-1,-10,10,-2,-7,5,-10,-1,-7,6,1],[7,6,6,3,9,-4,6,6,10,10,9,2],[6,-8,-1,10,-9,-7,4,9,-5,4,-7,-1],[2,-4,-3,2,6,-2,10,-4,-8,-4,-1,6],[3,7,-8,9,-4,-4,9,-6,5,9,-10,2],[4,-8,8,10,6,3,10,6,5,10,-6,-9],[4,4,-1,-2,4,-9,-6,4,-8,5,-1,1]],[[3,-1,8,7,8,-8,10,5,9,-6,2,-8],[9,8,6,-5,9,-9,-6,10,10,4,-7,-3],[2,5,9,4,-9,-7,10,-6,-10,9,-3,-9],[-9,2,1,-4,7,6,-5,6,-5,-8,7,-7],[9,2,-4,-5,-3,9,-4,-8,4,-9,-6,-2],[-7,7,4,-2,7,5,4,-2,-6,-10,6,1],[2,1,-4,9,1,7,8,-8,-3,6,-2,-4],[-1,-1,4,9,4,4,-2,1,-10,1,-10,-5],[-4,10,-1,-6,-9,-9,3,-9,-9,6,7,-7],[10,7,6,2,-4,6,7,6,-3,6,-5,2],[9,5,7,-5,9,6,-5,-5,-3,4,5,5],[-7,3,-10,-5,-2,5,4,8,-3,9,7,6],[-9,1,10,-3,10,8,10,7,8,5,1,5],[8,-1,-10,-4,-5,2,-10,2,-10,8,-6,3],[-8,-5,-2,2,-6,4,9,-4,2,10,4,3]],[[-2,5,-7,-3,-9,-3,-1,-10,9,-5,-1,-3],[-9,-8,-4,-7,4,-8,10,-6,-2,-7,-8,-1],[10,-5,7,5,-2,-6,-4,5,-5,-8,4,4],[-7,-2,10,1,-1,3,8,-3,1,-7,4,-2],[4,-6,6,-8,-2,7,6,-4,-6,-5,4,-5],[9,1,-5,-2,5,-1,7,3,2,1,-7,4],[-9,10,-9,2,8,-9,8,-1,-9,-5,2,4],[-5,-1,-10,-8,6,-4,-2,10,2,2,-3,5],[5,-8,8,-2,-9,-7,-10,9,2,10,2,3],[-3,5,8,-8,2,4,2,-2,3,-1,4,-10],[7,-10,1,-2,10,10,9,-5,-6,8,-8,-10],[-10,3,-2,10,-4,8,-6,10,10,-8,-10,10],[3,-5,-10,10,-5,-6,8,8,-6,9,-7,-10],[9,-7,-10,-4,-9,-1,-3,9,-6,6,-10,-7],[-1,10,5,6,-7,-2,4,-9,-4,-9,1,-4]],[[-4,-4,5,1,-8,-3,-1,9,-3,-5,7,-7],[-4,6,6,-6,-10,-5,2,8,-8,-4,-9,-7],[6,-9,-7,3,-3,-9,-1,-1,5,-6,3,8],[-7,8,-9,-8,10,5,-6,-9,9,9,-4,1],[-6,10,-2,-9,-3,7,-6,7,4,1,2,6],[1,1,6,7,-2,-1,7,5,9,-4,-7,-10],[2,-9,-3,-6,-2,2,-3,-10,-7,-9,-1,4],[6,-6,8,-2,-7,-7,-7,5,-1,9,-5,7],[10,-6,-10,-4,8,-9,-3,-9,3,-1,8,-2],[-2,-1,2,8,-5,6,5,-4,-7,3,4,-10],[-7,-9,-6,4,-4,4,-4,-1,-9,6,4,-10],[3,-2,-5,-3,-5,7,-5,-1,5,-6,-10,-2],[3,-6,8,-9,9,-9,6,-5,4,4,3,8],[-1,-1,-3,-3,-10,3,-4,10,-4,8,-1,-2],[-6,-6,-10,-9,1,5,2,8,6,2,4,3]],[[-9,1,-5,6,-9,-10,-7,1,10,1,3,-6],[1,-1,9,6,-7,9,9,-3,6,-7,-4,-10],[-6,8,10,-8,-1,-7,-3,10,9,-1,-3,-7],[8,9,-2,-8,-9,8,2,10,5,6,2,9],[3,10,-4,4,-10,-6,3,-3,-10,-10,6,-8],[7,2,-7,-1,-1,-8,-9,-7,-7,-3,6,-3],[-6,-1,-2,7,2,-1,10,-1,4,-8,-6,-1],[-9,-5,10,-5,10,-9,4,4,-5,5,8,8],[9,-4,-10,-10,-9,6,-3,-4,-7,-9,-8,7],[9,-9,-9,-8,3,-5,-7,4,2,-5,-8,-9],[-5,6,-3,-9,6,-9,6,-5,-1,4,7,-4],[-7,-3,-2,-2,3,10,-10,10,6,-2,7,1],[-8,-6,10,-4,-10,2,1,9,-1,-2,8,8],[1,6,7,-8,2,-2,5,-1,-2,9,8,-9],[-6,1,-3,8,1,2,1,5,-3,8,-10,2]],[[-2,7,-10,-1,7,10,3,4,4,-3,7,8],[2,9,-5,-6,-4,6,-9,-10,-9,6,2,7],[9,1,-6,9,7,10,1,-8,8,10,-1,4],[3,-3,2,-1,7,-1,4,-1,-8,-10,8,5],[-4,-3,-5,4,-9,-5,6,-3,9,-8,-4,2],[1,-10,-4,8,7,-2,10,-2,-4,9,-2,-4],[8,4,10,-1,-9,-3,5,-10,3,-7,-7,-2],[-6,2,-5,7,-8,-5,-6,-3,-9,-10,8,-9],[2,-3,-6,2,8,-10,-10,-8,9,-9,2,-1],[-6,5,3,-6,1,7,-6,7,-5,-1,-5,3],[2,8,4,5,2,-6,4,-1,-3,10,9,5],[6,9,5,-3,6,3,1,-9,-5,-10,-7,4],[9,-1,-1,2,-4,-9,5,-8,-5,10,-6,-9],[-4,-2,9,-10,9,-1,-8,10,-6,-1,-2,3],[-9,-3,9,-9,-2,3,6,4,-7,-6,7,-8]],[[-4,3,9,5,-8,4,2,-2,2,-8,1,4],[6,-2,5,-6,-9,6,7,-6,8,4,-1,4],[2,-4,3,-8,7,4,9,10,10,-8,5,-4],[3,-5,-2,10,3,4,1,7,-3,-7,-10,2],[2,9,-1,-2,-8,-1,-6,-4,-4,-4,-10,2],[-1,-6,7,-5,8,-6,-6,5,5,-6,-6,7],[9,-4,4,4,6,-8,-10,2,6,8,6,10],[9,2,6,-5,3,-8,7,2,-6,6,3,5],[-8,3,-6,7,9,-3,9,2,7,-8,-3,-8],[9,4,-2,1,-4,5,-7,7,2,-1,-8,-2],[4,-9,-8,-6,9,-1,1,-2,-8,4,1,-1],[3,-5,-6,6,-7,-7,-10,-6,-4,-1,-8,-9],[3,-4,-7,9,-7,-1,-1,3,1,-5,-2,9],[7,-1,4,1,-5,2,-10,-4,-3,-1,3,2],[-3,-3,7,9,2,9,9,-1,-7,-8,2,-5]]], dtype = "int8")#candidate|4235|(7, 15, 12)|const|int8
bop_4236 = relay.add(const_4234.astype('int8'), const_4235.astype('int8')) # shape=(7, 15, 12)
output = bop_4236
output2 = bop_4236
func_4241 = relay.Function([], output)
mod['func_4241'] = func_4241
mod = relay.transform.InferType()(mod)
mutated_mod['func_4241'] = func_4241
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4241_call = mutated_mod.get_global_var('func_4241')
call_4242 = func_4241_call()
output = call_4242
func_4243 = relay.Function([], output)
mutated_mod['func_4243'] = func_4243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4360 = relay.var("var_4360", dtype = "float64", shape = (14, 6, 9))#candidate|4360|(14, 6, 9)|var|float64
uop_4361 = relay.log10(var_4360.astype('float64')) # shape=(14, 6, 9)
func_1608_call = mod.get_global_var('func_1608')
func_1612_call = mutated_mod.get_global_var('func_1612')
const_4366 = relay.const([[2,-10,4,-10,9,4,-5,-7,-9,-3,-10,-7,1,-9,3,-6,7,-9,-2,-9],[-3,4,-5,-5,3,-7,9,9,-7,-4,-2,-3,-6,9,-5,2,5,-8,-8,-5],[8,-6,-6,-1,-3,-3,-7,3,-3,5,3,8,3,8,-8,2,5,-5,5,5],[-2,3,7,3,10,-9,-5,-1,-2,2,2,-8,-4,-9,10,6,-4,-1,7,-2],[4,-10,-10,-7,-1,-2,3,-1,2,5,-6,4,-2,-3,-9,-7,-8,-1,-9,-9],[-9,5,-1,-8,-8,5,-6,4,-3,8,-3,4,2,-8,-4,-3,-7,5,-5,-3],[8,7,-8,-3,-9,3,-5,-1,-10,10,-7,-5,1,4,-2,1,4,5,10,-3],[10,2,10,-4,4,6,-5,6,2,-2,-9,-6,2,7,1,2,5,-9,-7,7]], dtype = "uint8")#candidate|4366|(8, 20)|const|uint8
const_4367 = relay.const([8.104854,0.644687,-6.413712,-4.958706,8.149881,-1.217902,-3.398395,-5.054424,3.290843,-2.201755,5.562401,-2.415669,-7.916049,-8.844690,-4.035727,-5.762597,-8.479410,3.347208,-4.684055,1.959919,0.857817,-3.025977,-4.614611,6.397403,8.554852,-1.255593,-6.577119,-6.822022,-0.647804,-0.626155,-6.126414,-3.524148,-7.158094,3.224058,5.149021,8.415256,-0.687353,4.326209,-4.137434,-2.767410,-3.733960,9.457308,-4.246788,1.930454,-8.392825,3.743615,-0.573964,-4.735662,2.571267,4.007664,-2.968074,5.745270,-5.970107,2.654184,5.071313,2.820310], dtype = "float32")#candidate|4367|(56,)|const|float32
call_4365 = relay.TupleGetItem(func_1608_call(relay.reshape(const_4366.astype('uint8'), [10, 2, 8]), relay.reshape(const_4367.astype('float32'), [56,]), ), 0)
call_4368 = relay.TupleGetItem(func_1612_call(relay.reshape(const_4366.astype('uint8'), [10, 2, 8]), relay.reshape(const_4367.astype('float32'), [56,]), ), 0)
output = relay.Tuple([uop_4361,call_4365,const_4366,const_4367,])
output2 = relay.Tuple([uop_4361,call_4368,const_4366,const_4367,])
func_4369 = relay.Function([var_4360,], output)
mod['func_4369'] = func_4369
mod = relay.transform.InferType()(mod)
mutated_mod['func_4369'] = func_4369
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4370 = relay.var("var_4370", dtype = "float64", shape = (14, 6, 9))#candidate|4370|(14, 6, 9)|var|float64
func_4369_call = mutated_mod.get_global_var('func_4369')
call_4371 = func_4369_call(var_4370)
output = call_4371
func_4372 = relay.Function([var_4370], output)
mutated_mod['func_4372'] = func_4372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3727_call = mod.get_global_var('func_3727')
func_3728_call = mutated_mod.get_global_var('func_3728')
call_4374 = relay.TupleGetItem(func_3727_call(), 0)
call_4375 = relay.TupleGetItem(func_3728_call(), 0)
output = call_4374
output2 = call_4375
func_4379 = relay.Function([], output)
mod['func_4379'] = func_4379
mod = relay.transform.InferType()(mod)
output = func_4379()
func_4380 = relay.Function([], output)
mutated_mod['func_4380'] = func_4380
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_4407 = relay.TupleGetItem(func_1517_call(), 0)
call_4408 = relay.TupleGetItem(func_1519_call(), 0)
func_2470_call = mod.get_global_var('func_2470')
func_2472_call = mutated_mod.get_global_var('func_2472')
call_4409 = func_2470_call()
call_4410 = func_2470_call()
func_1330_call = mod.get_global_var('func_1330')
func_1331_call = mutated_mod.get_global_var('func_1331')
call_4414 = func_1330_call()
call_4415 = func_1330_call()
bop_4417 = relay.bitwise_xor(call_4407.astype('int64'), relay.reshape(call_4414.astype('int64'), relay.shape_of(call_4407))) # shape=(2, 14, 3)
bop_4420 = relay.bitwise_xor(call_4408.astype('int64'), relay.reshape(call_4415.astype('int64'), relay.shape_of(call_4408))) # shape=(2, 14, 3)
func_761_call = mod.get_global_var('func_761')
func_766_call = mutated_mod.get_global_var('func_766')
const_4427 = relay.const([[4.408081,2.176597,4.253647,-2.001496,6.830944,-4.342824,-1.444855,2.261739,-9.851247,-6.352483,-0.600379,0.730034],[1.073195,0.689733,-6.406334,-6.057891,8.630735,-9.490842,5.025431,1.101780,-6.801498,-5.757065,3.179673,4.950557],[-3.795176,6.427116,-1.167889,5.167293,1.080320,8.001176,-7.944202,8.839296,3.774986,-8.234851,-3.986268,9.495920]], dtype = "float64")#candidate|4427|(3, 12)|const|float64
var_4428 = relay.var("var_4428", dtype = "uint64", shape = (180,))#candidate|4428|(180,)|var|uint64
call_4426 = relay.TupleGetItem(func_761_call(relay.reshape(const_4427.astype('float64'), [36,]), relay.reshape(var_4428.astype('uint64'), [180,]), relay.reshape(var_4428.astype('float32'), [3, 12, 5]), ), 3)
call_4429 = relay.TupleGetItem(func_766_call(relay.reshape(const_4427.astype('float64'), [36,]), relay.reshape(var_4428.astype('uint64'), [180,]), relay.reshape(var_4428.astype('float32'), [3, 12, 5]), ), 3)
func_2047_call = mod.get_global_var('func_2047')
func_2049_call = mutated_mod.get_global_var('func_2049')
call_4433 = func_2047_call()
call_4434 = func_2047_call()
output = relay.Tuple([call_4409,bop_4417,call_4426,const_4427,var_4428,call_4433,])
output2 = relay.Tuple([call_4410,bop_4420,call_4429,const_4427,var_4428,call_4434,])
func_4437 = relay.Function([var_4428,], output)
mod['func_4437'] = func_4437
mod = relay.transform.InferType()(mod)
mutated_mod['func_4437'] = func_4437
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4438 = relay.var("var_4438", dtype = "uint64", shape = (180,))#candidate|4438|(180,)|var|uint64
func_4437_call = mutated_mod.get_global_var('func_4437')
call_4439 = func_4437_call(var_4438)
output = call_4439
func_4440 = relay.Function([var_4438], output)
mutated_mod['func_4440'] = func_4440
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1255_call = mod.get_global_var('func_1255')
func_1256_call = mutated_mod.get_global_var('func_1256')
call_4495 = relay.TupleGetItem(func_1255_call(), 2)
call_4496 = relay.TupleGetItem(func_1256_call(), 2)
output = relay.Tuple([call_4495,])
output2 = relay.Tuple([call_4496,])
func_4531 = relay.Function([], output)
mod['func_4531'] = func_4531
mod = relay.transform.InferType()(mod)
output = func_4531()
func_4532 = relay.Function([], output)
mutated_mod['func_4532'] = func_4532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2497_call = mod.get_global_var('func_2497')
func_2499_call = mutated_mod.get_global_var('func_2499')
call_4540 = relay.TupleGetItem(func_2497_call(), 0)
call_4541 = relay.TupleGetItem(func_2499_call(), 0)
uop_4542 = relay.acos(call_4540.astype('float32')) # shape=(2, 14, 3)
uop_4544 = relay.acos(call_4541.astype('float32')) # shape=(2, 14, 3)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
const_4547 = relay.const([-4.283744,9.048653,6.377440,-8.630214,6.287415,7.783321,5.752654,0.664874,0.632045,7.156948,2.682987,8.545671,-0.685660,1.452040,-9.351687,6.790245,-0.867211,-0.537089,-9.909949,7.574130,-4.229795,-4.534317,-3.245537,-6.734520,-6.890313,-5.685536,1.613469,9.706258,6.302051,2.511581,3.687344,0.866230,-0.513688,7.972229,-6.013026,-4.456899,6.092745,-0.764559,5.663456,-1.106721,-0.318317,8.244050,-2.449810,-7.253075,-8.441516,2.664682,-7.245021,3.147649,5.322902,2.848137,0.060529,-1.056466,-5.662640,8.032551,2.635354,2.926842,-1.771405,8.135070,2.034215,0.853344,3.371768,5.218404,7.892548,-4.251794,2.290341,-0.441915,-6.085081,-3.994193,-5.298249,-6.067626,7.557531,7.805747,-7.111573,-2.249492,-8.847880,7.583168,-0.973804,4.686814,-5.583746,-4.989338,7.988215,-1.885926,4.294574,2.051757,-0.125987,5.933864,5.340418,-6.225504,5.046592,-9.638702,-5.486116,-2.998031,-4.577623,-9.515304,8.325476,5.082637,2.201265,-3.672189,-6.184495,-2.878269,8.565875,-6.359524,5.617884,7.217528,5.816276,-8.820120,7.729126,-5.092870,4.064289,-3.302242,-7.801772,4.085751,-4.168128,-3.253911,4.052527,2.817037,7.281428,-8.143651,-9.160827,4.185378,5.239402,4.181542,-5.400891,-2.640578,-3.982069,5.032325,-7.510905,8.759326,-1.863751,4.964023,-0.002471,5.586398,-9.571063,-7.407659,4.453324,-9.516439,-6.244438,8.070215,-3.838525,-5.757079,7.760306,9.552232,-7.506255,-1.770242,-9.456682,3.489966,-5.208333,-8.468098,-5.331102,-3.453069,7.638212,-2.399990,-8.811808,-6.589051,4.144566,-3.585383,-5.407714,5.593291,-5.339560,-7.055122,6.523295,2.555435,-6.838744,0.799802,7.426683,-0.345879,-3.603831,-9.136110,-4.027553,3.486342,3.469048,-7.202795,4.016412,-2.496513,3.225920,0.528631,-2.558683,5.210525,-3.259991,5.582712,-1.988614,-3.058351,-4.058577,0.932643,-0.735339,5.370377,-4.187485,5.326596,2.174213,6.223892,-4.543156,9.121928,-8.762731,4.361299,4.047007,-8.061596,-8.608479,1.699239,9.074155,-3.025527,5.035691,6.667660,4.165836,-2.959968,-5.422585,-0.921334,-5.596892,-2.701641,-5.274081,6.374788,-8.712425,6.788300,6.643256,-3.091596,3.273299,-9.295038,-6.227134,7.473980,-2.993891,-5.502870,6.188751,-0.860979,-1.145027,-5.521546,-7.392416,2.402819,9.734808,-1.479548,4.094921,0.610135,3.036874,1.352359,3.191495,7.243485,-7.011303,7.555235,-6.116237,3.720121,-9.899072,5.094512,-8.467071,8.932438,3.236215,-7.259061,-3.491195,-0.051727,3.896926,0.012060,-7.911053,-8.890645,-4.997962,-2.837548,5.867458,-2.778134,-3.404658,7.679884,-2.016402,-4.316503,-6.012448,-7.605198,6.817464,-8.637339,-5.526612,5.674118,-9.706961,-2.990988,7.837049,-5.506558,-4.847122,-8.941931,-2.479565,9.421573,7.760952,8.095805,-5.076175,-1.161111,-2.444749,-0.069087,1.234190,2.392193,-8.074387,-8.456410,-1.958527,-2.473452,4.109886,6.132168,-2.287969,-8.851557,3.774325,8.254279,8.223704,0.374829,-7.764965,9.890725,5.595437,-7.408311,-1.709072,-1.660014,6.412340,5.080892,2.274769,-0.014534,-8.069838,3.383807,-7.923405,5.807316,6.646042,3.261192,4.072087,6.047141,1.858993,-9.998923,-3.403174,5.217757,4.568191,2.015360,4.435159,0.643876,-4.777870,4.688514,4.155742,8.280955,9.411183,7.012081,3.586202,-1.661529,-0.072275,-6.222229,9.328527,-7.542565,-9.679258,6.156171,8.271042,1.307621,-4.985720,2.454816,-7.145601,-3.731416,8.270255,-7.747088,-5.306287,-3.729280,8.772101,2.327386,-8.681207,8.289201,1.948429,-6.146440,4.542409,2.039243,0.198032,-7.494528,6.087235,5.630102,-8.715600,2.404962,-2.277783,9.791763,-0.168723,-2.979598,-5.361731,9.312096,7.616804,-5.217619,-5.838933,-3.426255,-8.070566,3.794279,5.172087,5.796626,-3.594228,-3.150951,-1.338392,-0.961536,-3.876410,2.474296,-9.278191,8.001896,-6.878572,3.295504,2.926366,-4.645974,-9.716041,0.915376,7.949757,6.878861,9.455752,-2.240011,6.184238,-1.598026,-7.645470,-3.607560,-0.783696,-9.355620,2.594021,0.549855,7.871060,5.288470,8.313265,7.189119,3.959631,-9.620446,-9.800280,-2.308116,8.890456,6.994859,-4.699936,7.752422,7.990640,1.500979,1.202048,5.735075,6.459592,-2.995380,3.356381,6.063666,-2.807855,4.076505,-7.345460,-9.839069,-1.017022,8.715686,1.054191,-2.960103,-9.967738,8.489365,-3.578228,-3.794617,2.516562,9.806671,-9.372452,0.590300,-3.082404,5.373911,-8.075837,1.632889,-6.698084,7.821503,7.603547,-6.640543,-1.508805,7.616282,5.573200,-5.185013,-9.533428,6.531432,-0.559156,8.857493,-8.224656,1.501592,-2.483152,2.292696,-6.977742,-3.518619,-7.124491,1.582535,-2.651739,-8.774471,2.713530,7.816077,-8.664530,-0.545698,5.308828,9.544923,6.402072,3.398650,1.581339,-3.113906,9.416109,0.301118,4.697378,-9.903374,0.604601,9.423294,8.705088,-8.104126,-5.884072,-0.637316,-2.073299,1.039848,1.618438,2.819942,0.641091,-5.246740,-9.553771,2.078738,-6.919824,-6.432946,-4.005943,-9.411797,-3.082132,2.681203,-8.642823,-7.249237,2.533390,-6.410630,-9.494980,-2.588016,6.012118,8.866665,-2.586786,8.136770,-7.751588,8.397062,-3.535068,6.241088,-5.305487,7.822087,-2.652598,-6.937857,1.085455,-7.842496,-3.831168,3.399299,7.403043,-1.867185,9.267329,0.307918,5.924653,-6.738017,-3.855150,-9.992599,-6.401558,3.861360,9.060521,4.474616,-0.611482,4.095922,-3.544497,-5.284361,2.600516,0.427282,8.684982,-6.611932,4.623647,-0.205158,-4.395980,0.242431,-2.787795,-7.678499,-1.597122,-0.864923,5.290563,0.749683,-2.783634,-4.752213,-4.112019,0.179339,-0.618983,-9.160862,-4.349691,7.694636,0.426999,-7.028680,-4.938773,-5.717468,-3.052941,8.882702,-3.160183,3.932474,1.049650,-5.399915,1.858805,9.663248,1.741075,-5.797507,-6.751797,6.390815,-1.385834,6.974550,-7.806505,6.103330,-0.857552,-1.066875,3.861338,2.665175,6.052018,4.984780,2.312898,-6.550631,-5.868663,1.749133,9.709944,9.337351,-0.589098,-0.131183,-2.469303,9.591307,-7.026046,7.300003,6.344600,-8.800941,-2.687892,5.657751,-8.257290,-5.972320,-7.714691,7.644949,-7.432980,4.397048,1.461366,2.495689,8.044237,-4.227329,8.294129,-3.517573,6.437963,7.572012,-3.881463,7.677196,8.509652,1.181335,8.156096,4.511762,0.894689,-9.110096,-0.065956,-3.944766,-1.579868,9.775619,-2.283686,-9.997538,1.202755,6.904080,8.621773,-8.842142,9.684497,-1.279054,3.434775,-7.687462,4.057632,5.566014,4.095012,1.854233,1.603327,0.243357,-7.996080,5.047910,3.589512,0.245642,0.252418,3.997345,-3.559684,-2.185556,6.739168,-2.832227,6.341529,-6.969009,-5.625640,9.775311,1.580345,6.630298,-9.096405,5.286778,-1.722584,-5.022249,-4.889447,-8.730437,-3.918400,-3.442750,2.843267,-0.879974,0.313023,6.231743,-8.583730,7.224636,4.399317,-1.725731,3.482995,-2.264898,-6.733467,0.184403,-4.375479,8.135425,-4.778845,5.590780,6.015121,1.573242,-2.969883,-9.956311,3.254167,-9.632973,-1.557313,-7.428532,-3.646753,0.684457,-0.460345,-4.893849,-2.853862,7.268531,1.340138,4.372678,-2.940948,2.272168,6.548691,2.366931,7.397124,-4.093560,-2.585348,0.681296,6.884538,-3.475860,-1.720128,-5.961367,-9.351892,8.921762,-4.004221,-9.264840,6.837957,-9.248805,8.139556,4.198177,1.012442,0.537092,7.437698,9.345803,6.514158,-5.904047,-8.264851,7.085248,-2.510049,-7.556969,5.779447,4.523948,9.468021,6.134788,4.701435,2.855851,-4.374631,1.028480,-4.640366,-9.614733,-4.173438,7.586531,-6.124746,9.856636,4.217803,9.190465,8.769589,-0.818713,-0.522290,3.217249,-5.526974,5.357968,5.376331,-9.986564,2.865409,-1.522091,3.455509,-6.648920,-9.924537,-7.191479,7.934232,-5.215189,-2.720981,8.698428,-0.550566,2.000774,-2.705129,-3.500185,4.088491,2.380967,8.889128,-2.972917,3.543096,-6.240405,-7.325180,9.244334,3.314873,-2.594536,-3.839796,-3.885677,9.296234,-8.912307,-7.263791,2.107012,5.133287,-9.296345,-8.134332,-1.626227,6.663795,4.187569,8.893018,-7.565283,-9.774224,4.316160,-5.978797,-5.754333,2.990428,3.309037,2.970140,4.767983,4.897592,8.298301,-3.668062,9.974519,3.446478,0.019174,-0.674595,3.022823,3.833252,0.556134,-3.393903,7.454640,-9.685897,-7.346666,0.681179,8.570633,5.907057,7.060735,-8.748614,-7.906830,5.751662,-2.562235,1.056943,0.163977,-5.038245,-6.143970,-7.370910,-4.731919,6.254613,-6.286273,-1.287825,7.690707,-6.845939,7.025482,-7.306818,-8.536895,-0.293582,5.149366,-7.916065,-0.918935,9.534125,-9.173874,-3.693813,3.144022,6.138303,-6.697558,2.228544,8.012125,-9.052867,-5.108620,-4.224175,1.857239,1.317966,-7.622743,6.980051,2.581349,-8.792691,-6.202884,-1.254666,-7.508481,9.061238,-5.038575,-4.459769,-0.222187,-5.263391,2.885862,-3.805359,9.653668,4.288411,2.163542,-2.158623,-0.903022,-6.763619,8.446224,-6.389086,-9.217492,0.421005,-0.818075,8.782041,-6.239826,9.912357,-4.090781,-6.971527,3.215753,-5.670159,-8.908412,5.837290,9.161799,2.323697,7.732649,-0.808373,4.037857,-7.496902,3.934795,0.881332,7.607734,-4.852317,-5.953528,-3.742140,-5.985228,-2.748309,8.187206,8.443686,-6.814483,-4.021421,-6.126182,4.010140,-4.484134,2.823406,9.543133,1.635597,7.693361,1.488001,6.012495,-7.228581,-9.780067,-5.272308,-1.743008,-1.837427,7.816436,-9.284338,2.334215,4.774976,2.455697,7.969393,4.757629,-0.860942,-4.343748,-4.341824,0.508073,-8.426001,-9.347504,7.851369,-9.001763,5.106464,-7.840156,-4.519631,6.923705,0.087488,-1.451744,-7.104470,-5.788486,4.046687,-2.531610,-7.894184,-2.430180,6.346763,9.372581,2.794397,-8.717321,9.999988,2.078451,-5.932519,-3.478646,9.068287,-5.664428,-1.022092,-8.427181,-1.785314,-3.831223,-5.230634,4.440311,3.047346,7.441127,-0.566355,8.010443,-3.767612,1.010315,6.597620,5.603211,7.627852,-5.377157,-7.004054,4.987437,4.971432,7.488676,-9.741375,7.598941,3.470076,-8.791011,-4.978733,-7.634589,-0.756218,5.663778,4.326199,4.495950,8.279384,-4.328342,-6.636241,-2.945391,2.200402,-8.265642,-8.382709,6.733446,-6.643923,4.374950,8.593108,8.493991,-9.793108,-7.715031,3.977062,-9.458828,7.367017,-5.235326,-6.455403,-7.343114,-0.732505,4.315954,-9.982552,8.248982,-3.926111,-7.826709,-4.652381,-4.217383,-6.303860,-3.002988,-4.285769,-6.639873,1.598768,6.149347,7.566163,-6.324434,-1.761275,-9.408209,-7.108048,8.959802,3.458896,9.373537,-2.977124,-8.588785,-3.308170,-7.835580,2.437855,-5.631117,-7.409316,-5.252014,9.090921,2.229912,-3.460581,1.781389,2.229840,0.707717,-0.764021,-3.815948,-2.848550,0.284568,3.335548,5.916353,1.554325,-0.534285,-0.308157,3.373614,8.111717,1.917173,4.648518,-9.117801,-9.333480,7.962034,-3.402385,3.899749,-4.127689,6.260062,-3.744760,-5.212383,2.228890,8.283034,4.141706,8.781085,-6.387049,-9.319197,5.348293,-1.231075,-8.283076,-7.125208,-1.568677,-7.374482,6.293416,-1.951240,-0.547851,3.328641,9.204543,2.581851,2.619457,0.933536,-4.645530,3.314705,5.504371,0.910487,6.124633,-5.912766,7.439780,-5.334097,7.108710,-4.310975,9.868413,3.574727,7.139654,4.977170,1.804287,-2.587515,-0.388947,-8.517435,3.179479,-2.030981,3.495237,-9.602825,9.376590,9.851405,-8.838560,-5.860174,9.354538,-6.896200,5.214861,-1.123308,6.002807,-3.324697,-1.960168,8.383661,-0.573636,0.959980,-4.305741,-5.760596,-4.536776,-9.202465,5.869332,6.698123,-0.439633,8.996081,1.151457,6.393583,-4.657952,8.216683,-4.122795,6.305240,-4.183906,-6.867317,-8.522367,-2.428026,9.418371,2.031675,4.711320,5.784116,7.585656,6.774675,-3.685325,9.612594,-9.372431,-3.337461,5.014422,4.319284,-8.108738,-8.891013,-5.880142,9.012994,-3.227749,1.954150,1.136168,5.285745,8.400605,-9.666262,1.688103,2.239258,-4.047973,-8.921059,7.669036,3.685720,-0.966293,-5.822382,-8.601006,-9.003951,6.996151,-3.981044,-1.146554,4.921160,1.856739,-0.629680,7.668101,-4.345976,7.034937,4.751273,5.834810,-9.498544,-1.941719,-1.848177,-4.998429,9.605299,-2.973824,5.836906,-1.445698,0.025375,-5.091783,-0.803866,7.787930,5.491491,-0.695005,2.964988,1.350977,8.690262,-9.666497,-0.268859,-3.739366,-7.525954,1.303627,1.172050,-7.255333,5.668605,-3.034464,-0.882231,9.516297,-3.618439,-0.823019,5.196234,2.912933,-3.044248,-5.788663,5.775055,-7.879745,-3.978606,0.007762,4.167584,-3.051358,-5.543688,3.050563,-7.100426,-4.250893,-2.098695,-5.548524,-2.474198,-3.429478,9.601808,2.812195,3.148228,5.675302,3.005914,7.795515,-7.454585,-9.891116,3.194198,-9.597119,-7.088372,-8.613762,7.484304,-4.858604,2.474096,-8.628095,3.634868,1.122162,-5.494270,-5.517805,0.464808,-5.574413,7.599591,-9.172893,-4.077036,-6.133262,1.469289,1.736016,4.904149,-1.631163,-8.216138,-0.999725,-0.326473,-8.673294,-2.790256,-7.838116,6.929986,4.907504,2.288537,7.596407,-1.325146,-4.764623,-7.372397,8.422802,0.316969,-0.514869,-7.862813,-8.136887,-0.325545,4.749949,9.926094,-1.803211,1.163480,-8.795211,9.344616,-6.852208,1.121065,5.135674,5.024816,-0.482471,-6.414946,-5.177218,5.119112,7.515171,-8.835375,-1.222705,6.944618,-8.384641,-8.973611,3.152349,-1.828836,-3.169423,3.083231,2.111971,-8.477364,2.377108,9.197117,5.252033,-0.631435,-4.909189,-7.874756,6.341881,-5.594904,-7.194069,-9.879766,-5.376558,8.793154,-7.334125,7.232660,1.040600,3.493960,-0.617518,5.108999,6.574877,8.516007,-5.214990,-1.737273,3.312886,2.026724,-3.028183,7.705112,-8.558479,6.082505,1.341965,-3.641516,-7.974513,-4.861860,-7.985258,-3.205901,8.393085,-1.537582,5.065873,1.467612,2.045729,-2.179544,-3.819033,-2.031714,2.561032,-4.631645,-5.229170,6.491620,-0.133887,-6.706964,9.285444,0.721196,-4.089865,-3.640798,-2.965963,-4.809907,-9.074255,2.497427,-5.000813,2.731663,2.652201,1.652961,0.859853,-3.729982,-8.193053,-2.005926,-0.397205,-0.227224,2.722132,-6.918112,9.849582,8.677927,-8.814552,-1.807774,3.634984,-5.796927,3.074453,-0.904351,-5.594909,6.981664,6.494552,6.942513,5.112803,-7.043621,-6.401321,-1.074827,2.508625,-1.309499,4.604343,1.734767,-6.843406,5.886546,3.258647,-3.447468,9.986772,-7.849002,-6.400115,-9.055586,5.714969,-8.572302,1.249029,4.616390,3.919072,-2.203983,8.195421,3.696701,1.568237,8.291294,-4.541799,8.200197,6.218625,2.950937,7.597049,9.302473,-3.194142,-9.119689,5.807779,7.104524,2.000291,3.545456,0.500272,4.813928,1.171002,3.386281,-7.332359,3.720978,-3.338054,7.244335,-0.401096,-9.276015,0.881846,6.116338,8.108060,3.228267,-6.657590,6.038549,2.342757,9.326512,8.886430,-4.502036,9.733275,-5.538817,-4.639596,3.919475,-2.711335,-6.406818,-5.061107,-4.075844,-9.056405,2.663795,-7.335857,-1.307201,9.403507,6.276641,-7.694444,-5.130517,9.811578,9.357179,8.057321,1.730525,-8.517196,7.230027,4.951930,-7.741964,9.032169,-5.395861,-1.371419,2.784183,-8.937895,0.193337,-3.675030,-0.290751,-8.249813,-3.410521,-7.034905,2.823371,2.532220,-4.566867,1.733175,-9.806786,-3.130115,-1.765359,2.470024,-8.401768,-6.289099,-3.236568,7.337205,7.040280,-6.154237,2.977743,3.938026,2.146369,3.376861,9.323416,4.326166,8.646711,-8.623532,-0.812401,2.854250,-2.695651,-7.047148,7.086211,8.366211,5.923892,-4.921725,8.536573,-7.213196,-1.186272,-1.409776,-7.668321,9.831279,2.242602,3.026149,2.201287,-0.893266,5.669014,-9.355023,-1.853922], dtype = "float64")#candidate|4547|(1512,)|const|float64
call_4546 = relay.TupleGetItem(func_1886_call(relay.reshape(const_4547.astype('float64'), [1512,])), 0)
call_4548 = relay.TupleGetItem(func_1888_call(relay.reshape(const_4547.astype('float64'), [1512,])), 0)
bop_4549 = relay.greater(call_4546.astype('bool'), relay.reshape(call_4540.astype('bool'), relay.shape_of(call_4546))) # shape=(2, 14, 3)
bop_4552 = relay.greater(call_4548.astype('bool'), relay.reshape(call_4541.astype('bool'), relay.shape_of(call_4548))) # shape=(2, 14, 3)
uop_4556 = relay.log(uop_4542.astype('float32')) # shape=(2, 14, 3)
uop_4558 = relay.log(uop_4544.astype('float32')) # shape=(2, 14, 3)
output = relay.Tuple([const_4547,bop_4549,uop_4556,])
output2 = relay.Tuple([const_4547,bop_4552,uop_4558,])
func_4559 = relay.Function([], output)
mod['func_4559'] = func_4559
mod = relay.transform.InferType()(mod)
mutated_mod['func_4559'] = func_4559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4559_call = mutated_mod.get_global_var('func_4559')
call_4560 = func_4559_call()
output = call_4560
func_4561 = relay.Function([], output)
mutated_mod['func_4561'] = func_4561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_525_call = mod.get_global_var('func_525')
func_526_call = mutated_mod.get_global_var('func_526')
call_4581 = func_525_call()
call_4582 = func_525_call()
func_3033_call = mod.get_global_var('func_3033')
func_3036_call = mutated_mod.get_global_var('func_3036')
const_4587 = relay.const([6.191277,2.744652,-2.579281,8.910825,-5.431395,-7.862245,0.855087,7.303746,-2.693084,-7.669996,-1.086201,-9.030202,6.994206,-3.666881,-9.140778,5.545584,-7.960760,7.611721,9.389339,5.860092,4.492238,-2.730659,2.206897,6.312437,-7.770334,-6.008563,-8.522624,5.290829,6.885477,-8.178554,-4.397528,3.483427,5.330576,6.786314,1.881684,-7.492081,-4.708125,2.575466,-6.958591,0.927814,-1.211875,2.573226,1.079751,1.303112,9.775905,-7.559551,1.504701,-5.581221,-9.449643,6.438188,-2.839047,-9.293828,-9.165086,-0.293901,-6.308332,5.869928,-7.509677,-3.882820,1.304408,-5.670301,6.716347,-3.194117,-1.743281,7.982415,0.624095,-6.049254,-0.653299,-3.215535,-5.351216,7.403027,9.460305,-0.425035,-0.163476,3.881862,-5.059906,-6.296963,-8.339948,-9.972268,2.259750,0.007832,-8.592966,-1.530697,-3.363958,1.434398,-3.304641,0.937404,4.973547,4.566862,-0.085168,4.138212,-1.422691,5.429626,-4.428832,7.657861,1.326054,-3.738895,-2.349920,1.169072,-1.230677,1.629053,5.800875,-3.720520,-7.328732,-4.781590,-2.144172,3.228703,1.871505,2.830611,-5.910091,2.615551,1.532613,0.326127,6.162206,-4.191326,1.607760,-5.742437,-6.202614,4.357199,-1.846299,-3.032236,4.564017,0.864491,-7.202218,4.140934,5.025720,-8.047283,-2.721867,-8.597173,-0.885664,2.935301,-7.506751,1.150211,-5.771795,-4.836770,-3.617055,0.353561,-6.122550,0.003284,9.790650,-3.188992,7.791150,5.415950,-8.007094,5.620061,-4.211809,0.917649,-3.325679,-5.259872,5.060184,5.759813,3.152323,-3.307856,3.598851,-7.257872,-0.255858,6.850177,2.436602,2.647673,-5.124195,6.757737,-1.527148,-1.642819,2.173456,3.184529,8.488690,-5.010971,-2.003678,-4.051115,-6.241555,-3.291196,1.458896,0.015647,3.740298,3.853183,0.745866,-4.447437,4.267483,6.538473,3.031001,4.490091,0.793575,2.418700,-9.067880,-1.055384,-9.137489,9.945258,-4.557453,3.702146,-3.576486,-9.048772,0.187956,6.108037,7.107064,8.990641,3.018020,1.317874,-0.688258,-1.492760,-3.534205,-6.896555,-7.269122,3.075370,-0.210194,-3.208856,7.159930,-1.704858,0.373826,2.878623,-6.492481,-7.498598,1.753381,9.686758,-6.464667,3.474838,-3.530624,-0.393405,2.418374,9.847260,-1.332838,-5.276547,-8.440188,-4.198808,-0.829713,-0.200183,-0.904855,4.462925,-1.938235,2.020795,-8.973600,-8.324570,-9.244372,5.280331,-9.889206,8.379279,-2.763046,-8.911956,1.334875,7.054684,-2.824374,-2.507876,-0.074112,-0.821082,-4.982313,5.155924,-8.300934,3.611549,-3.793655,2.535237,-8.257733,8.746202,-8.804154,7.011654,-6.347556,-2.506733,7.019912,2.698877,-6.349814,-9.181888,-6.449258,1.068900,8.056537,3.081845,-2.638019,-1.690251,-3.177514,3.739485,2.672252,-1.607571,0.140417,-9.142031,4.266138,-1.859924,-9.020021,9.734071,1.403445,6.832806,2.607400,-0.723170,2.546707,-4.847088,9.480315,5.346761,8.925793,-5.810268,-7.826349,2.613807,0.249440,6.284864,-9.980428,-0.536696,6.771058,2.461690,-4.189769,-5.293198,-4.550460,4.899304,9.579326,6.862484,-6.645220,5.292232,-2.233927,2.349499,9.265692,9.645228,6.815751,8.247526,-4.283200,0.589156,-5.037388,-1.296916,4.037243,-8.607886,-1.932019,9.540046,-0.056670,9.306324,8.889096,-3.029794,6.603795,-0.317527,3.784984,-4.296798,-5.482747,-8.630407,7.860113,-1.458320,0.986251,8.904273,-1.981379,-3.824999,-3.853048,8.215915,-6.764505,-1.573599,-7.447068,-9.402432,-2.379470,1.014550,1.429226,7.096532,-9.385563,0.995389,6.709324,-6.897553,2.473614,-4.125160,-2.470072,5.709153,6.038211,9.157533,-2.911107,5.771968,-3.758779,-7.873609,-4.992000,-6.456174,6.634360,-9.444242,5.603983,-2.751976,-3.779995,-9.586926,-6.873002,7.843014,0.751074,9.398438,2.838009,-8.240061,5.685849,0.748389,-6.666365,2.179717,5.493579,-8.772900,-7.588383,7.361031,9.648301,5.438916,3.610844,2.117878,5.275379,-3.064414,9.748387,-3.334761,9.422657,0.766988,-0.505708,8.304699,-4.394908,-8.983838,-7.779250,6.349786,1.993783,-0.599428,-9.608947,0.297254,-6.032925,-8.932755,-9.003230,4.442172,-8.301624,9.460304,6.318281,-3.913791,7.667753,-7.117211,-3.422991,0.473022,-5.103436,-2.622387,-8.659787,0.729178,0.067439,-0.512030,-1.530126,-7.534808,-4.543530,1.837348,-8.179121,-2.520541,-2.728285,-4.084633,-2.470431,-7.911336,7.940783,2.983852,-3.009304,-9.530498,-3.494528,0.965469,-3.051241,3.977778,-2.232768,-1.015093,-3.628522,-8.579184,1.511148,7.672843,-1.661507,8.656813,-6.508813,7.734517,8.811892,6.502884,8.723122,-7.198033,-6.948676,-0.236725,9.064924,5.487502,2.511392,-4.352752,-5.242354,5.770074,-4.877830,-6.717947,2.610908,6.868373,-9.397410,6.460109,-6.903659,7.939815,9.688709,6.485140,2.378488,1.867870,-2.931763,8.610598,5.613864,5.243866,5.578748,5.414807,-4.888250,6.079371,8.747911,-2.844710,9.052114,-6.111122,1.322268,5.263208,-4.231051,-8.460568,-8.371389,-4.281766,-0.273287,8.154039,4.025867,-2.840267,-5.497333,-9.350251,-7.728482,0.944434,8.198045,6.379868,5.630408,7.339820,5.424563,-2.325813,7.889524,5.466956,-0.190529,-3.587311,5.688348,8.831631,-9.169280,8.986075,-0.362987,-0.556664,-9.235488,9.278016,-0.526650,-7.407685,-2.673803,-0.382239,2.480370,8.031027,-9.444604,8.194790,-8.691612,0.221465,8.009010,-8.369889,6.737681,6.655827,-3.102390,7.963954,5.184829,-3.106494,-1.849944,9.217907,-9.032381,-2.026361,-8.134948,5.898050,-5.612505,-2.365824,9.897439,-9.410017,5.768305,5.645201,-1.754872,9.697348,-1.901092,4.390802,-0.245831,-0.661902,2.666827,0.252611,-0.043512,-8.846919,-3.768463,-7.372621,5.511845,-5.216109,-6.840258,-4.862886,5.777593,-6.154892,6.660032,-5.090805,1.030333,7.645298,5.161900,-4.142897,3.967028,4.010403,5.636442,7.611929,-3.133938,-0.914061,8.558672,3.575286,-6.715188,-5.825112,5.119741,2.530298,2.539452,1.971781,2.584737,8.525192,-3.005557,-5.014986,-1.871225,2.093111,-4.332505,-0.964443,-7.010456,-1.283555,9.228268,2.614186,7.075269,9.344599,2.382096,-9.760525,4.920092,4.133328,-2.820922,8.667196,5.605500,0.841174,-1.813301,-2.548638,0.287159,1.037862,8.460764,1.934973,7.389296,-2.178998,3.856027,-0.502731,-5.765921,-5.172358,3.681964,8.459698,-1.429160,-4.251861,-3.470157,-2.754400,5.798806,5.586159,-9.571461,-7.241638,6.789170,-2.500235,4.168823,6.689662,-9.003703,-6.400088,-4.144124,-6.924432,-5.014011,7.912443,8.955629,-9.583006,-1.721721,-1.437285,-1.332254,-3.247428,5.625443,-1.600962,8.892000,-7.616959,6.564142,-0.344455,-1.920094,7.293971,0.390531,-0.587585,-1.537816,-4.632079,-4.804362,1.042069,4.770084,-8.206115,-3.148861,7.930411,1.082505,8.516222,-8.040881,-2.830095,-7.975513,5.677132,-9.183857,1.749500,-5.653341,5.101728,-0.917586,7.997992,9.702201,-9.243733,-1.602730,5.807350,9.375938,-7.518970,-9.319972,-3.967079,-4.550468,6.451481,9.680394,0.533034,-1.621143,-1.761106,4.184848,-8.781578,-4.825080,-9.999349,-3.819150,-8.006394,-9.061518,1.452013,0.057831,-1.007104,5.990901,-8.959182,-4.273695,-9.921909,5.711377,8.946341,-5.110925,4.345064,-4.799012,2.568360,9.209587,-1.522062,-3.263697,6.406710,6.455642,-6.222523,4.650011,-0.882172,-7.941831,-6.501902,8.111595,4.545468,3.035041,-7.246624,-8.153800,-3.146208,3.920242,-7.497513,-2.590110,2.046152,4.987607,-3.335168,6.794755,-9.224298,2.636954,6.605411,-1.914211,-8.674025,4.488264,7.031055,-8.154343,8.313618,-6.615837,1.512439,2.682412,-9.939226,-2.728095,6.050332,9.492244,-6.171362,-0.252178,-8.307935,-2.331368,-8.191570,0.397781,0.176845,0.423923,-5.927082,-7.332676,-6.256757,-8.586443,-8.945847,7.783825,-1.376094,2.052576,6.711670,-0.037684,-1.037222,-3.008886,-4.405264,-3.224043,8.467257,6.354978,7.435751,-5.677160,4.832230,6.566077,9.398502,-4.346241,6.784627,-0.413941,2.988048,-1.887788,2.716449,1.870870,1.821887,-1.718936,2.017037,-5.729605,0.090180,0.076130,3.912634,9.498709,3.368641,1.539686,5.239411,-3.986986,-8.302115,2.885979,8.287677,-1.792756,-5.821225,-6.303152,-5.545950,6.531516,6.654162,-2.475775,9.124105,4.257476,3.530559,5.519754,6.035894,-4.603390,6.349806,8.428391,-8.333198,2.552929,-7.884697,-7.175504,-5.132954,2.205603,-4.258961,-8.744833,7.629442,9.766754,-1.864891,1.817329,-1.606810,-1.034429,7.545971,-2.464272,8.458003,1.983489,3.094016,-7.132443,2.855103,8.516461,6.146464,1.929534,-7.794112,-4.733663,8.646324,-6.231240,4.363581,5.220475,-5.459179,-7.079306,8.851901,-5.867218,2.008405,-6.909257,-9.738656,6.855053,-5.491655,-0.467098,0.937341,8.503737,-0.547274,-8.023476,-7.498238,6.212228,6.002172,-0.422289,5.565378,-5.418124,3.609233,3.396053,-6.531176,-6.216673,2.616030,5.656165,4.016983,3.495503,-4.745846,5.700394,-9.502005,-1.456382,-8.813195,-7.269238,1.513344,-6.137510,-6.504065,-1.297488,-7.221417,5.848718,2.753900,-6.186414,2.803111,-1.271319,9.166372,1.895134,-8.108156,-9.217888,-3.848616,-6.881467,9.635153,5.732374,-7.952293,-1.307113,-7.243425,-1.033503,2.682829,-2.448586,7.149346], dtype = "float64")#candidate|4587|(896,)|const|float64
call_4586 = relay.TupleGetItem(func_3033_call(relay.reshape(const_4587.astype('float64'), [8, 7, 16])), 0)
call_4588 = relay.TupleGetItem(func_3036_call(relay.reshape(const_4587.astype('float64'), [8, 7, 16])), 0)
uop_4597 = relay.cos(const_4587.astype('float32')) # shape=(896,)
func_4143_call = mod.get_global_var('func_4143')
func_4145_call = mutated_mod.get_global_var('func_4145')
call_4603 = relay.TupleGetItem(func_4143_call(), 0)
call_4604 = relay.TupleGetItem(func_4145_call(), 0)
uop_4611 = relay.acosh(uop_4597.astype('float64')) # shape=(896,)
func_2411_call = mod.get_global_var('func_2411')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_4617 = func_2411_call()
call_4618 = func_2411_call()
output = relay.Tuple([call_4581,call_4586,call_4603,uop_4611,call_4617,])
output2 = relay.Tuple([call_4582,call_4588,call_4604,uop_4611,call_4618,])
func_4627 = relay.Function([], output)
mod['func_4627'] = func_4627
mod = relay.transform.InferType()(mod)
output = func_4627()
func_4628 = relay.Function([], output)
mutated_mod['func_4628'] = func_4628
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3939_call = mod.get_global_var('func_3939')
func_3940_call = mutated_mod.get_global_var('func_3940')
call_4645 = func_3939_call()
call_4646 = func_3939_call()
uop_4651 = relay.acosh(call_4645.astype('float32')) # shape=(2, 14, 3)
uop_4653 = relay.acosh(call_4646.astype('float32')) # shape=(2, 14, 3)
func_4009_call = mod.get_global_var('func_4009')
func_4010_call = mutated_mod.get_global_var('func_4010')
call_4655 = relay.TupleGetItem(func_4009_call(), 4)
call_4656 = relay.TupleGetItem(func_4010_call(), 4)
func_1983_call = mod.get_global_var('func_1983')
func_1985_call = mutated_mod.get_global_var('func_1985')
var_4665 = relay.var("var_4665", dtype = "float32", shape = (280,))#candidate|4665|(280,)|var|float32
call_4664 = relay.TupleGetItem(func_1983_call(relay.reshape(var_4665.astype('float32'), [70, 4])), 1)
call_4666 = relay.TupleGetItem(func_1985_call(relay.reshape(var_4665.astype('float32'), [70, 4])), 1)
func_225_call = mod.get_global_var('func_225')
func_230_call = mutated_mod.get_global_var('func_230')
const_4683 = relay.const([-0.947511,3.469450,-4.406990,7.936655,-5.585365,-8.577692,-8.028039,6.361361,-6.318341,-1.021324,0.552719,6.601497,1.488571,-0.646698,3.061422,-2.791534,-8.266660,9.537003,1.614961,1.375850,7.283393,-6.237413,-5.575668,-3.487608,2.641288,6.061056,2.150496,9.229418,-9.731566,3.145274,1.826600,3.777343,7.771908,-6.495342,-1.064565,-7.715178], dtype = "float64")#candidate|4683|(36,)|const|float64
const_4684 = relay.const([-6,-10,-5,9,8,-8,-3,-7,7,8,1,-3,2,9,-10,1,-3,3,4,10,1,6,2,8,3,-7,-2,3,4,-1,2,10,-6,5,-5,1,2,-2,1,6,-8,8,-5,3,5,-2,9,-4,7,3,4,-9,-1,3,-3,-6,3,-2,-5,8,10,-8,-3,1,2,1,-10,-6,-1,5,-9,-6,4,-3,-2,8,-10,-10,1,-3,7,-10,-6,10,-7,-3,5,-3,7,8,6,3,4,-10,-5,9,1,-1,-8,-2,7,3,5,10,3,-3,-8,6,-8,-9,1,8,-7,-7,-1,2,-6,-9,3,5,9,-5,-2,1,7,-6,-7,-10,-3,-1,-10,2,10,-9,3,10,-1,1,6,-7,1,3,8,-4,2,7,8,8,-3,2,-10,-9,7,-6,1,6,-7,-2,2,-9,-9,6,8,-9,2,8,-4,-5,-7,2,4,-2,6,-9,-7,-5,-7,-8,-5,-7], dtype = "uint64")#candidate|4684|(180,)|const|uint64
var_4685 = relay.var("var_4685", dtype = "float64", shape = (216,))#candidate|4685|(216,)|var|float64
call_4682 = relay.TupleGetItem(func_225_call(relay.reshape(const_4683.astype('float64'), [3, 12, 1]), relay.reshape(const_4684.astype('uint64'), [3, 12, 5]), relay.reshape(const_4684.astype('uint16'), [3, 12, 5]), relay.reshape(var_4685.astype('float64'), [3, 12, 6]), ), 1)
call_4686 = relay.TupleGetItem(func_230_call(relay.reshape(const_4683.astype('float64'), [3, 12, 1]), relay.reshape(const_4684.astype('uint64'), [3, 12, 5]), relay.reshape(const_4684.astype('uint16'), [3, 12, 5]), relay.reshape(var_4685.astype('float64'), [3, 12, 6]), ), 1)
output = relay.Tuple([uop_4651,call_4655,call_4664,var_4665,call_4682,const_4683,const_4684,var_4685,])
output2 = relay.Tuple([uop_4653,call_4656,call_4666,var_4665,call_4686,const_4683,const_4684,var_4685,])
func_4690 = relay.Function([var_4665,var_4685,], output)
mod['func_4690'] = func_4690
mod = relay.transform.InferType()(mod)
var_4691 = relay.var("var_4691", dtype = "float32", shape = (280,))#candidate|4691|(280,)|var|float32
var_4692 = relay.var("var_4692", dtype = "float64", shape = (216,))#candidate|4692|(216,)|var|float64
output = func_4690(var_4691,var_4692,)
func_4693 = relay.Function([var_4691,var_4692,], output)
mutated_mod['func_4693'] = func_4693
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3375_call = mod.get_global_var('func_3375')
func_3376_call = mutated_mod.get_global_var('func_3376')
call_4795 = relay.TupleGetItem(func_3375_call(), 0)
call_4796 = relay.TupleGetItem(func_3376_call(), 0)
func_2383_call = mod.get_global_var('func_2383')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_4809 = relay.TupleGetItem(func_2383_call(), 0)
call_4810 = relay.TupleGetItem(func_2384_call(), 0)
output = relay.Tuple([call_4795,call_4809,])
output2 = relay.Tuple([call_4796,call_4810,])
func_4829 = relay.Function([], output)
mod['func_4829'] = func_4829
mod = relay.transform.InferType()(mod)
mutated_mod['func_4829'] = func_4829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4829_call = mutated_mod.get_global_var('func_4829')
call_4830 = func_4829_call()
output = call_4830
func_4831 = relay.Function([], output)
mutated_mod['func_4831'] = func_4831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2411_call = mod.get_global_var('func_2411')
func_2413_call = mutated_mod.get_global_var('func_2413')
call_4851 = func_2411_call()
call_4852 = func_2411_call()
output = call_4851
output2 = call_4852
func_4858 = relay.Function([], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
output = func_4858()
func_4859 = relay.Function([], output)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4876 = relay.var("var_4876", dtype = "int8", shape = ())#candidate|4876|()|var|int8
var_4877 = relay.var("var_4877", dtype = "int8", shape = (14, 11, 2))#candidate|4877|(14, 11, 2)|var|int8
bop_4878 = relay.left_shift(var_4876.astype('int8'), var_4877.astype('int8')) # shape=(14, 11, 2)
output = relay.Tuple([bop_4878,])
output2 = relay.Tuple([bop_4878,])
func_4884 = relay.Function([var_4876,var_4877,], output)
mod['func_4884'] = func_4884
mod = relay.transform.InferType()(mod)
var_4885 = relay.var("var_4885", dtype = "int8", shape = ())#candidate|4885|()|var|int8
var_4886 = relay.var("var_4886", dtype = "int8", shape = (14, 11, 2))#candidate|4886|(14, 11, 2)|var|int8
output = func_4884(var_4885,var_4886,)
func_4887 = relay.Function([var_4885,var_4886,], output)
mutated_mod['func_4887'] = func_4887
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4894 = relay.var("var_4894", dtype = "int8", shape = (12, 7, 1))#candidate|4894|(12, 7, 1)|var|int8
var_4895 = relay.var("var_4895", dtype = "int8", shape = (12, 7, 8))#candidate|4895|(12, 7, 8)|var|int8
bop_4896 = relay.less_equal(var_4894.astype('bool'), var_4895.astype('bool')) # shape=(12, 7, 8)
output = bop_4896
output2 = bop_4896
func_4914 = relay.Function([var_4894,var_4895,], output)
mod['func_4914'] = func_4914
mod = relay.transform.InferType()(mod)
mutated_mod['func_4914'] = func_4914
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4914_call = mutated_mod.get_global_var('func_4914')
var_4916 = relay.var("var_4916", dtype = "int8", shape = (12, 7, 1))#candidate|4916|(12, 7, 1)|var|int8
var_4917 = relay.var("var_4917", dtype = "int8", shape = (12, 7, 8))#candidate|4917|(12, 7, 8)|var|int8
call_4915 = func_4914_call(var_4916,var_4917,)
output = call_4915
func_4918 = relay.Function([var_4916,var_4917,], output)
mutated_mod['func_4918'] = func_4918
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3939_call = mod.get_global_var('func_3939')
func_3940_call = mutated_mod.get_global_var('func_3940')
call_4958 = func_3939_call()
call_4959 = func_3939_call()
output = relay.Tuple([call_4958,])
output2 = relay.Tuple([call_4959,])
func_4967 = relay.Function([], output)
mod['func_4967'] = func_4967
mod = relay.transform.InferType()(mod)
mutated_mod['func_4967'] = func_4967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4967_call = mutated_mod.get_global_var('func_4967')
call_4968 = func_4967_call()
output = call_4968
func_4969 = relay.Function([], output)
mutated_mod['func_4969'] = func_4969
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1517_call = mod.get_global_var('func_1517')
func_1519_call = mutated_mod.get_global_var('func_1519')
call_4984 = relay.TupleGetItem(func_1517_call(), 0)
call_4985 = relay.TupleGetItem(func_1519_call(), 0)
func_2383_call = mod.get_global_var('func_2383')
func_2384_call = mutated_mod.get_global_var('func_2384')
call_4986 = relay.TupleGetItem(func_2383_call(), 0)
call_4987 = relay.TupleGetItem(func_2384_call(), 0)
bop_5003 = relay.minimum(call_4984.astype('uint16'), relay.reshape(call_4986.astype('uint16'), relay.shape_of(call_4984))) # shape=(2, 14, 3)
bop_5006 = relay.minimum(call_4985.astype('uint16'), relay.reshape(call_4987.astype('uint16'), relay.shape_of(call_4985))) # shape=(2, 14, 3)
func_1886_call = mod.get_global_var('func_1886')
func_1888_call = mutated_mod.get_global_var('func_1888')
var_5015 = relay.var("var_5015", dtype = "float64", shape = (1512,))#candidate|5015|(1512,)|var|float64
call_5014 = relay.TupleGetItem(func_1886_call(relay.reshape(var_5015.astype('float64'), [1512,])), 0)
call_5016 = relay.TupleGetItem(func_1888_call(relay.reshape(var_5015.astype('float64'), [1512,])), 0)
func_2673_call = mod.get_global_var('func_2673')
func_2677_call = mutated_mod.get_global_var('func_2677')
const_5018 = relay.const([-5.464575,8.048849,8.749099,7.992043,-1.589290,1.225153,9.293953,7.841788,-9.585453,8.622945,9.201670,5.402026,5.712493,6.292150,-4.473736,-6.595092,-5.248818,2.566401,-9.862279,0.413884,-8.979198,-3.839652,-2.383898,4.230384,8.979814,7.173808,-4.723116,9.908683,-3.693991,-1.317634,5.888820,5.421376,3.352809,-5.737794,-9.110251,-4.155343,-6.516109,-9.860747,-9.021314,4.017910,-4.201397,-1.424463,3.203432,4.667482,-3.912150,-8.552929,-7.461988,4.773439,7.278423,0.630167,-6.312287,-1.848250,-9.489097,8.193825,-9.237161,2.643025,8.106342,0.208167,0.942461,0.939031,6.865823,7.876196,7.820201,4.721032,-4.120213,-8.822120,-8.935778,-6.022175,-7.944609,-3.230971,-9.953451,1.350706,3.013892,8.977959,9.143075,0.056968,-2.145432,-6.646139,0.985706,-2.461402,0.115748,-4.083739,7.463251,-5.464823,6.275801,3.832748,-4.674448,1.601668,5.390664,-2.713840,4.187621,0.609908,0.339309,-7.959170,8.921513,-5.825654,7.434062,8.430499,8.168335,-8.563195,-8.279880,1.200499,8.330984,-7.970600,4.201076,7.210837,-6.953434,-3.388771,1.241326,8.028156,-7.164204,1.322787,-8.920046,-5.511765,-2.557726,-7.882133,-3.454856,-9.758257,1.874555,4.529679,6.202008,0.700811,9.382162,9.125820,-1.526668,-3.265163,4.417173,3.895838,-8.665368,1.224126,-2.341822,3.324113,8.400782,-2.753732,-5.711823,7.627979,8.919184,-5.967539,5.840651,3.056682,-7.060390,-3.573013,4.925416,4.220819,3.022729,-3.067772,0.502581,6.387905,3.191249,4.088747,9.033493,-3.968358,7.593276,0.991251,-1.027738,1.933208,-1.510890,-5.565444,9.012283,2.135028,4.972952,-4.105027,1.415635,1.029037,-8.454723,2.120869,-5.459431,-8.662589,-7.524514,-1.845431,-1.640211,2.990998,4.030736,-4.886193,8.343940,8.506643,9.258646,0.318387,7.074992,-1.994916,7.652743,0.002235,1.159884,-2.737125,-5.478454,-6.609552,-8.041238,6.590714,-4.528025,-1.697949,-2.718730,-0.802889,9.988477,-8.535222,-5.284059,-4.093243,-7.037230,1.434138,9.124411,7.381281,-6.469229,-7.909998,9.774151,-0.635949,9.247644,-6.970916,1.777941,-1.331740,-8.226333,9.310738,5.241075,8.548132,-1.988125,9.003304,-6.685599,0.864402,-9.684124,0.389826,6.931912,9.154508,-1.796755,-8.558041,-2.593606,-4.155704,-2.421238,-9.017562,-6.347734,4.099000,-8.083895,-0.102914,-0.194813,-2.572189,-9.891862,-3.499707,2.527620,-7.516612,9.592294,1.483003,4.023444,6.141699,-8.267163,4.256396,6.311186,8.613960,1.905297,-6.673737,8.863934,9.774466,-2.684816,6.422726,8.664052,6.519054,9.566175,4.710823,-3.763306,-3.624023,-0.039165,9.765272,-2.660180,1.298713,3.496045,8.537450,-4.089317,-7.870021,9.258160,7.232446,6.266459,3.935843,0.877771,-3.386438,8.617345,-1.139787,-3.732985,2.481925,-4.796343,3.769160,-2.376297,-6.355975,3.643332,9.998393,8.357750,9.383780,7.029172,6.043937,0.263136,7.977340,-5.373117,-3.564337], dtype = "float32")#candidate|5018|(288,)|const|float32
const_5019 = relay.const([8.349417,9.989844,-2.120924,-9.969615,-2.495202,-8.459507,-9.571117,3.931857,-9.657453,6.341526,-0.647029,5.469943,-2.004917,4.971572,4.550451,-5.532922,0.788623,2.238725,4.945116,8.702556,5.705508,4.680275,-5.028623,-5.627678,0.423004,-7.738549,-9.535575,-8.154745,-1.215533,-2.021214,0.258976,-5.565868,4.514897,-4.606516,4.769100,-0.900718,7.045153,0.972979,-0.784198,-5.721271,7.341550,9.399336,-3.426843,-1.173116,-5.813406,7.845952,3.405802,-1.966662,1.783823,-4.797311,4.883181,8.410034,-6.448411,-0.663578,-4.851080,6.622937,4.016651,9.317698,-7.317463,-7.872189,9.850588,-1.577399,7.536350,0.600092,3.407483,-0.344000,-7.371831,3.869772,-0.105457,-9.653741,6.510926,-1.875315,-6.181124,-9.662369,9.729691,2.901721,-2.736092,-9.499661,3.205689,-0.934099,1.066781,5.209338,8.271674,-5.253793,-1.455670,-1.460948,-5.157519,-0.651621,9.139579,-9.974851,-8.812156,2.618749,1.934320,-3.917275,5.148831,-7.531921,6.856695,-2.452999,-2.011550,-6.313849,1.878582,-6.632728,9.441997,0.248900,-3.483883,-5.147618,2.476418,9.481654,9.101603,3.575216,5.504770,9.620934,9.262330,7.071662,-0.903715,-9.716588,-8.623116,-3.626828,-1.823622,-9.644235,3.314512,0.520562,-6.274706,4.838396,-7.493451,-9.252106,-1.762081,1.281961,-8.478003,-1.644617,-5.400545,-7.934396,5.487273,3.149015,-9.430413,-5.060737,-9.620018,3.568893,0.892438,-0.455440,7.046264,7.798211,-2.926570,-2.379330,4.234930,3.371377,0.056561,-9.743708,-5.346553,-1.568843,-6.388350,-7.306101,-1.296793,1.586770,3.710783,-7.689109,9.388449,-1.087991,-7.531420,-4.193302,4.359228,1.829783,6.202966,-7.910377,9.221144,8.384113,1.308612,-2.251356,9.090908,7.153531,4.996700,4.075517,4.432917,-4.031767,-6.850982,6.567099,9.059749,4.660254,2.024555,-8.539433,-5.157444,-3.098559,-3.862874,-5.147932,-9.065504,-0.700725,5.417520,-0.645883,4.779374,-6.595954,0.517251,-7.250093,-5.954168,-2.810321,5.220614,4.826199,-3.135002,1.745771,-6.536060,-3.739631,-5.968608,9.520967,-4.851457,-1.555226,-6.154789,-0.406471,8.149471,-3.099345,-3.164557,8.869777,-1.190142,4.415674,-1.816091,5.176015,-7.603416,9.597997,-6.934835,-3.392179,4.801768,-6.224282,7.069605,0.178803,7.279027,4.858269,-8.625832,2.635498,4.781369,4.673261,-3.836397,-2.728236,-7.421570,0.201086,-1.102159,-3.947242,-4.939003,-7.487975,7.875425,-3.994250,3.525108,-3.963060,-3.202821,-1.121029,-4.627780,5.013304,-0.914921,-4.237358,-7.864009,4.235234,0.192516,-7.648905,4.003645,-6.988882,-2.890663,6.925738,-3.407875,-3.326666,-7.607310,-6.956030,-2.122428,7.488181,0.370054,-8.182648,8.243035,6.121048,7.294336,-8.354876,-7.418832,0.880854,-5.380992,-3.973449,-6.423007,0.658735,-5.371771,8.892196,-5.258179,4.996202,-0.829348,6.767590,-1.799897,9.491677,-3.186815,-8.018433,-9.184920,7.647773,-1.621172,9.790800,-5.763979,6.272164,-9.613509,-7.308757,9.391803,-7.191804,4.081244,5.158760,-0.297290,8.477191,5.211898,0.163494,3.458060,-3.466627,7.707500,-0.013270,-3.167885,-2.458107,-0.171345,4.685698,-9.243488,-1.620397,3.049660,6.803132,-1.642778,-5.598769,-6.779564,3.035768,8.528618,-9.189480,0.902209,-6.369838,-4.839296,-0.915316,2.551452,8.990297,8.037430,1.849647,9.537550,5.097531,6.942719,1.656371,8.415250,6.512081,-0.402957,7.731982,-9.388702,-8.083746,-8.844198,-4.614921,-2.555599,-0.952161,1.951138,2.833510,-8.935172,-4.530346,-9.109891,-4.644735,-5.908819,-4.074894,8.380007,-3.779584,-1.289769,-6.536901,4.894969,-6.076924,-9.149458,3.417357,7.754984,4.357241,0.737061,3.800209,1.617530,-2.501716,-0.188008,1.946535,-3.139879,6.799175,-8.900668,-0.721456,-2.083160,6.507218,4.206004,-0.099862,8.701107,-8.573372,3.645265,3.050420,2.701897,-5.662976,-0.065740,3.400563,6.266048,2.311400,7.076812,7.896670,3.112391,-3.465430,-3.786763,0.933615,-9.743816,-1.502689,8.825176,6.533166,3.318389,-8.931958,7.760060,6.273095,4.665245,-6.427153,-7.186678,-7.834125,-7.578648,-5.794550,-9.057962,6.059886,9.469979,-3.596585,0.592149,-0.458876,-5.223815,-8.666884,-0.400464,-9.079064,8.297116,-1.226129,3.267392,9.484068,-8.287721,-1.553371,0.070310,4.658206,1.721511,1.692852,5.346156,-4.677809,2.617744,1.773948,-3.520568,8.638997,-0.659825,0.057667,-7.706756,-6.198533,-2.510329,1.097546,-6.261278,-0.959064,4.099464,-9.343036,0.755405,-7.766921,4.268690,1.222271,0.119862,4.803799,-0.944906,2.846971,7.595880,3.619093,-1.316613,0.607935,-7.143600,4.859965,-2.905189,-3.531615,-5.410474,-7.002402,9.585249,7.085038,-9.905017,-0.594686,0.986738,2.322046,9.823758,-6.375284,-7.222431,-2.377345,2.490986,-3.666551,4.261470,-7.671256,7.646461,-3.746335,-2.830011,0.667834,-1.074978,3.864039,-0.001553,0.723638,-3.906251,8.534642,1.667617,0.533040,2.891261,-3.193978,-0.124035,-7.198028,9.385074,-8.404827,-5.904974,-5.318006,-2.218674,-9.114253,1.304905,-4.380618,1.458215,-2.272853,-4.659464,-4.392096,0.518553,-8.462074,0.439516,6.147939,5.546149,-6.074897,6.687032,9.442224,-7.881865,-2.632466,4.451926,9.776249,7.174124,1.971312,3.763279,2.220482,6.495513,3.972023,2.053976,5.219119,-1.972230,-8.548416,5.811990,1.625697,-6.931645,6.197039,3.011697,-0.677923,-3.118833,-3.062147,2.329658,-0.339464,8.956606,8.469453,-6.711650,-6.566003,-3.823665,-6.477302,-3.461372,-2.455192,-6.704415,-8.992885,-9.614152,-8.240758,-4.094532,8.637482,-6.125576,-7.473692,7.580955,-9.500071,1.624767,-8.622983,-5.948384,9.703109,5.488612,9.615298,7.468354,5.258494,-9.585836,-5.543360,-4.419071,4.520297,1.565126,-3.910712,8.541707,-5.016185,7.323538,6.170416,4.866931,-7.498628,-5.596773,-1.525283,7.394031,8.246032,0.120783,3.418880,2.843004,8.174018,-6.907220,6.401374,-0.426576,-4.025295,3.164295,7.155971,-2.141305,3.403994,4.389159,-4.808183,6.955568,9.723417,8.147221,-1.398803,0.974256,0.090403,7.873474,8.872924,-7.032236,-3.969082,6.145549,7.988798,0.008030,-4.850993,-1.122521,-6.726845,1.464178,9.694609,-9.727523,6.126068,2.414407,2.370732,-2.087903,-4.236934,9.487963,-8.170005,0.210242,-2.438557,-9.103970,2.922044,-7.599387,-7.622719,2.645535,-5.407618,1.794701,2.951235,8.120508,3.773717,-5.045414,-6.873967,-3.715203,-9.762668,-6.403608,8.408828,-3.285218,-3.635080,-2.678972,-6.178249,-3.741921,2.582076,-6.951554,-7.638847,7.400541,9.562700,9.532295,6.015795,-0.685028,6.652791,9.854612,0.718660,-8.583999,-8.309593,-5.269568,-6.490181,6.022731,-8.783089,0.659000,7.976329,1.221815,-3.521299,1.102773,-1.836385,6.228346,-6.752750,-7.995328,-8.589280,2.562407,9.443056,3.577624,-4.015777,1.584506,1.532564,7.813253,-7.589580,8.875808,-0.659668,-6.328644,1.976225,-8.790673,-7.607874,4.955069,1.212174,1.069969,4.258096,9.668406,-5.470681,-2.995610,3.992009,-0.668859,-9.526727,-5.210027,-0.175641,-0.797217,-3.112340,-5.936764,8.768946,-7.091672,-9.593834,-7.986134,-7.552358,-8.326919,-3.648258,-4.049579,-7.273567,2.854661,2.264482,1.823923,8.857419,0.571125,4.103994,-5.434511,4.802709,4.903865,0.951816,0.789648,4.227861,-6.412691,5.842690,4.204332,0.216334,-7.540115,-3.278138,3.748818,2.895821,-2.213501,-1.757440,-8.968477,4.823712,3.195861,5.156371,-9.980397,-6.883459,-5.246535,-2.243974,-5.082169,8.352454,-5.477020,-2.379529,1.616392,-4.856808,-3.482618,-9.005050,-6.371286,1.758880,-0.299592,1.488772,7.725651,9.137664,0.446397,-9.221639,-0.228686,-7.639086,5.306102,-1.866581,7.274943,-3.295692,6.397640,-6.183529,-1.012780,0.227069,-1.830835,-9.573904,3.501575,7.979851,0.926982,-1.207183,3.162672,-9.490272,4.186973,7.153526,8.277992,5.553436,7.121183,-9.080252,6.203189,-8.934765,-1.793500,0.261154,1.618503,-0.087737,-5.767750,-3.203272,-8.686138,1.951537,1.934236,-3.702755,-7.205313,4.202672,3.615804,-4.842219,7.014963,-4.521636,7.747831,3.505783,-9.649578,7.498997,-7.759663,7.767977,-3.533224,4.536491,4.651752,-7.601274,7.043469,4.025777,8.485460,0.748168,3.219650,4.300708,9.641868,2.325340,-9.712935,3.314288,-6.894164,8.121071,4.148027,-6.874860,-9.686773,-1.586876,-9.504537,-9.275436,2.054576,-0.215035,3.688779,3.461062,8.879857,0.552666,6.079604,-2.263281,6.904494,-4.157174,-0.248583,6.877680,8.155100,-4.328987,-0.427896,-8.145483,-7.156746,-6.765648,-9.850065,8.559877,-0.994747,8.769328,5.627629,5.028757,-4.500001,6.487450,-8.742254,6.983294,-6.160468,5.570568,0.552273,7.821472,-1.344113,1.579336,1.492481,-9.187178,1.647842,-8.565784,-3.281232,0.458674,4.314835,5.754903,-7.237537,-6.234921,7.653124,2.618001,4.319712,-4.614867,-0.410329,-1.164106,-1.600694,7.775758,-2.266754,-3.440339,7.706561,8.995143,-1.069739,-5.382770,-9.853721,-5.635007,-5.801867,-5.472381,-2.231535,6.366240,-5.348765,-5.618967], dtype = "float64")#candidate|5019|(880,)|const|float64
call_5017 = relay.TupleGetItem(func_2673_call(relay.reshape(const_5018.astype('float32'), [288,]), relay.reshape(const_5019.astype('float64'), [440, 2]), ), 1)
call_5020 = relay.TupleGetItem(func_2677_call(relay.reshape(const_5018.astype('float32'), [288,]), relay.reshape(const_5019.astype('float64'), [440, 2]), ), 1)
output = relay.Tuple([bop_5003,call_5014,var_5015,call_5017,const_5018,const_5019,])
output2 = relay.Tuple([bop_5006,call_5016,var_5015,call_5020,const_5018,const_5019,])
func_5028 = relay.Function([var_5015,], output)
mod['func_5028'] = func_5028
mod = relay.transform.InferType()(mod)
var_5029 = relay.var("var_5029", dtype = "float64", shape = (1512,))#candidate|5029|(1512,)|var|float64
output = func_5028(var_5029)
func_5030 = relay.Function([var_5029], output)
mutated_mod['func_5030'] = func_5030
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5043 = relay.var("var_5043", dtype = "float64", shape = (2, 8, 15))#candidate|5043|(2, 8, 15)|var|float64
uop_5044 = relay.acosh(var_5043.astype('float64')) # shape=(2, 8, 15)
output = relay.Tuple([uop_5044,])
output2 = relay.Tuple([uop_5044,])
F = relay.Function([var_5043,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_5043,], output2)
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
