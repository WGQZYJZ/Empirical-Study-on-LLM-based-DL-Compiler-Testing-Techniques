import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
const_193 = relay.const([[[-5.580435,-8.862804],[-6.908959,5.788898],[4.568171,-7.777360],[-0.418186,4.463266],[8.780481,2.047569],[5.061431,-2.843142],[-8.518238,5.378195],[1.099240,-4.199356],[-8.943065,-6.245934],[6.489007,-9.653647]],[[-6.614088,-5.382161],[2.767617,8.739173],[-9.198288,-3.660052],[-8.127474,8.615027],[4.844419,8.324039],[2.053655,-7.540840],[-0.406001,-7.004896],[-3.293508,-9.228409],[2.242544,4.360923],[7.390798,1.415415]],[[0.545245,9.771449],[3.880199,4.273368],[9.733954,3.149842],[-3.232353,-7.174353],[-9.732677,-6.692819],[0.687549,8.259196],[5.170626,4.478286],[4.752466,-6.094807],[-0.113782,-5.234800],[-1.216373,-0.446881]],[[-2.746264,-1.872472],[8.255734,-9.892727],[-1.944619,-6.156467],[9.291339,-0.595610],[2.466878,7.512559],[8.772767,1.437839],[2.027769,1.791369],[9.445124,5.157980],[3.092920,-4.541415],[-5.925555,-1.128157]],[[7.844441,-3.854418],[9.385065,5.780848],[1.218512,8.509462],[0.684719,-9.253836],[5.723000,-8.364082],[-7.378557,-9.172834],[-0.079924,-2.558296],[2.304649,8.204008],[-8.061996,-4.123173],[-4.037525,-5.131392]],[[-2.045016,-3.811757],[-8.205811,1.828955],[-7.303553,7.820610],[8.072557,-8.568185],[-1.860475,6.600078],[-2.839788,5.385355],[-1.298673,-1.159187],[6.320135,-0.250561],[-2.608702,1.416401],[-5.564754,-8.276117]],[[1.274808,7.449838],[-8.747097,-3.991922],[-9.315758,-7.990579],[-6.138284,3.028603],[8.060375,8.639515],[-1.543645,6.350028],[6.911329,-7.976447],[8.715326,-3.120112],[-2.678971,0.616636],[-7.006344,6.845072]]], dtype = "float64")#candidate|193|(7, 10, 2)|const|float64
uop_194 = relay.sinh(const_193.astype('float64')) # shape=(7, 10, 2)
output = uop_194
output2 = uop_194
func_196 = relay.Function([], output)
mod['func_196'] = func_196
mod = relay.transform.InferType()(mod)
mutated_mod['func_196'] = func_196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mutated_mod.get_global_var('func_196')
call_197 = func_196_call()
output = call_197
func_198 = relay.Function([], output)
mutated_mod['func_198'] = func_198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_201 = func_196_call()
call_202 = func_196_call()
output = call_201
output2 = call_202
func_203 = relay.Function([], output)
mod['func_203'] = func_203
mod = relay.transform.InferType()(mod)
output = func_203()
func_204 = relay.Function([], output)
mutated_mod['func_204'] = func_204
mutated_mod = relay.transform.InferType()(mutated_mod)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_258 = func_203_call()
call_259 = func_203_call()
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_260 = func_196_call()
call_261 = func_196_call()
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_275 = func_196_call()
call_276 = func_196_call()
uop_279 = relay.sqrt(call_258.astype('float64')) # shape=(7, 10, 2)
uop_281 = relay.sqrt(call_259.astype('float64')) # shape=(7, 10, 2)
bop_282 = relay.logical_and(call_260.astype('bool'), relay.reshape(call_275.astype('bool'), relay.shape_of(call_260))) # shape=(7, 10, 2)
bop_285 = relay.logical_and(call_261.astype('bool'), relay.reshape(call_276.astype('bool'), relay.shape_of(call_261))) # shape=(7, 10, 2)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_291 = func_196_call()
call_292 = func_196_call()
output = relay.Tuple([uop_279,bop_282,call_291,])
output2 = relay.Tuple([uop_281,bop_285,call_292,])
func_299 = relay.Function([], output)
mod['func_299'] = func_299
mod = relay.transform.InferType()(mod)
output = func_299()
func_300 = relay.Function([], output)
mutated_mod['func_300'] = func_300
mutated_mod = relay.transform.InferType()(mutated_mod)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_313 = relay.TupleGetItem(func_299_call(), 2)
call_314 = relay.TupleGetItem(func_300_call(), 2)
output = call_313
output2 = call_314
func_318 = relay.Function([], output)
mod['func_318'] = func_318
mod = relay.transform.InferType()(mod)
output = func_318()
func_319 = relay.Function([], output)
mutated_mod['func_319'] = func_319
mutated_mod = relay.transform.InferType()(mutated_mod)
var_447 = relay.var("var_447", dtype = "float64", shape = (1, 4, 11))#candidate|447|(1, 4, 11)|var|float64
const_448 = relay.const([[[0.613245,-7.873391,4.240949,4.634649,-5.627620,6.899625,4.479102,-5.813623,-0.875031,-9.668805,0.778531],[-1.890728,-3.016279,-5.574148,-0.985981,-7.514029,5.680811,-5.148477,5.035055,-2.673290,1.350527,7.239156],[-1.726596,-2.975120,-9.529082,-2.600947,3.236881,-4.251000,-6.309887,8.556204,2.679391,-0.404372,8.348699],[9.653183,-5.220013,-6.628106,0.002265,-1.905873,0.131574,-2.572422,7.212004,8.447556,-1.405612,-9.438967]]], dtype = "float64")#candidate|448|(1, 4, 11)|const|float64
bop_449 = relay.floor_mod(var_447.astype('float64'), relay.reshape(const_448.astype('float64'), relay.shape_of(var_447))) # shape=(1, 4, 11)
bop_453 = relay.less_equal(bop_449.astype('bool'), relay.reshape(var_447.astype('bool'), relay.shape_of(bop_449))) # shape=(1, 4, 11)
output = bop_453
output2 = bop_453
func_459 = relay.Function([var_447,], output)
mod['func_459'] = func_459
mod = relay.transform.InferType()(mod)
var_460 = relay.var("var_460", dtype = "float64", shape = (1, 4, 11))#candidate|460|(1, 4, 11)|var|float64
output = func_459(var_460)
func_461 = relay.Function([var_460], output)
mutated_mod['func_461'] = func_461
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_500 = func_196_call()
call_501 = func_196_call()
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_515 = func_196_call()
call_516 = func_196_call()
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_518 = relay.TupleGetItem(func_299_call(), 1)
call_519 = relay.TupleGetItem(func_300_call(), 1)
uop_530 = relay.log(call_518.astype('float64')) # shape=(7, 10, 2)
uop_532 = relay.log(call_519.astype('float64')) # shape=(7, 10, 2)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_545 = relay.TupleGetItem(func_299_call(), 1)
call_546 = relay.TupleGetItem(func_300_call(), 1)
func_459_call = mod.get_global_var('func_459')
func_461_call = mutated_mod.get_global_var('func_461')
var_548 = relay.var("var_548", dtype = "float64", shape = (44,))#candidate|548|(44,)|var|float64
call_547 = func_459_call(relay.reshape(var_548.astype('float64'), [1, 4, 11]))
call_549 = func_459_call(relay.reshape(var_548.astype('float64'), [1, 4, 11]))
output = relay.Tuple([call_500,call_515,uop_530,call_545,call_547,var_548,])
output2 = relay.Tuple([call_501,call_516,uop_532,call_546,call_549,var_548,])
func_556 = relay.Function([var_548,], output)
mod['func_556'] = func_556
mod = relay.transform.InferType()(mod)
mutated_mod['func_556'] = func_556
mutated_mod = relay.transform.InferType()(mutated_mod)
var_557 = relay.var("var_557", dtype = "float64", shape = (44,))#candidate|557|(44,)|var|float64
func_556_call = mutated_mod.get_global_var('func_556')
call_558 = func_556_call(var_557)
output = call_558
func_559 = relay.Function([var_557], output)
mutated_mod['func_559'] = func_559
mutated_mod = relay.transform.InferType()(mutated_mod)
var_628 = relay.var("var_628", dtype = "int16", shape = (14, 13, 1))#candidate|628|(14, 13, 1)|var|int16
var_629 = relay.var("var_629", dtype = "int16", shape = (14, 13, 1))#candidate|629|(14, 13, 1)|var|int16
bop_630 = relay.not_equal(var_628.astype('bool'), relay.reshape(var_629.astype('bool'), relay.shape_of(var_628))) # shape=(14, 13, 1)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_639 = relay.TupleGetItem(func_299_call(), 1)
call_640 = relay.TupleGetItem(func_300_call(), 1)
uop_663 = relay.log10(var_629.astype('float32')) # shape=(14, 13, 1)
bop_668 = relay.floor_mod(uop_663.astype('float32'), relay.reshape(bop_630.astype('float32'), relay.shape_of(uop_663))) # shape=(14, 13, 1)
bop_677 = relay.right_shift(uop_663.astype('uint16'), relay.reshape(bop_668.astype('uint16'), relay.shape_of(uop_663))) # shape=(14, 13, 1)
output = relay.Tuple([call_639,bop_677,])
output2 = relay.Tuple([call_640,bop_677,])
func_688 = relay.Function([var_628,var_629,], output)
mod['func_688'] = func_688
mod = relay.transform.InferType()(mod)
mutated_mod['func_688'] = func_688
mutated_mod = relay.transform.InferType()(mutated_mod)
func_688_call = mutated_mod.get_global_var('func_688')
var_690 = relay.var("var_690", dtype = "int16", shape = (14, 13, 1))#candidate|690|(14, 13, 1)|var|int16
var_691 = relay.var("var_691", dtype = "int16", shape = (14, 13, 1))#candidate|691|(14, 13, 1)|var|int16
call_689 = func_688_call(var_690,var_691,)
output = call_689
func_692 = relay.Function([var_690,var_691,], output)
mutated_mod['func_692'] = func_692
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_319_call = mutated_mod.get_global_var('func_319')
call_694 = func_318_call()
call_695 = func_318_call()
output = relay.Tuple([call_694,])
output2 = relay.Tuple([call_695,])
func_696 = relay.Function([], output)
mod['func_696'] = func_696
mod = relay.transform.InferType()(mod)
output = func_696()
func_697 = relay.Function([], output)
mutated_mod['func_697'] = func_697
mutated_mod = relay.transform.InferType()(mutated_mod)
func_696_call = mod.get_global_var('func_696')
func_697_call = mutated_mod.get_global_var('func_697')
call_733 = relay.TupleGetItem(func_696_call(), 0)
call_734 = relay.TupleGetItem(func_697_call(), 0)
output = relay.Tuple([call_733,])
output2 = relay.Tuple([call_734,])
func_759 = relay.Function([], output)
mod['func_759'] = func_759
mod = relay.transform.InferType()(mod)
mutated_mod['func_759'] = func_759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_759_call = mutated_mod.get_global_var('func_759')
call_760 = func_759_call()
output = call_760
func_761 = relay.Function([], output)
mutated_mod['func_761'] = func_761
mutated_mod = relay.transform.InferType()(mutated_mod)
var_801 = relay.var("var_801", dtype = "uint8", shape = (5, 7))#candidate|801|(5, 7)|var|uint8
var_802 = relay.var("var_802", dtype = "uint8", shape = (5, 7))#candidate|802|(5, 7)|var|uint8
bop_803 = relay.less_equal(var_801.astype('bool'), relay.reshape(var_802.astype('bool'), relay.shape_of(var_801))) # shape=(5, 7)
func_459_call = mod.get_global_var('func_459')
func_461_call = mutated_mod.get_global_var('func_461')
var_813 = relay.var("var_813", dtype = "float64", shape = (11, 4))#candidate|813|(11, 4)|var|float64
call_812 = func_459_call(relay.reshape(var_813.astype('float64'), [1, 4, 11]))
call_814 = func_459_call(relay.reshape(var_813.astype('float64'), [1, 4, 11]))
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_822 = func_203_call()
call_823 = func_203_call()
output = relay.Tuple([bop_803,call_812,var_813,call_822,])
output2 = relay.Tuple([bop_803,call_814,var_813,call_823,])
func_828 = relay.Function([var_801,var_802,var_813,], output)
mod['func_828'] = func_828
mod = relay.transform.InferType()(mod)
var_829 = relay.var("var_829", dtype = "uint8", shape = (5, 7))#candidate|829|(5, 7)|var|uint8
var_830 = relay.var("var_830", dtype = "uint8", shape = (5, 7))#candidate|830|(5, 7)|var|uint8
var_831 = relay.var("var_831", dtype = "float64", shape = (11, 4))#candidate|831|(11, 4)|var|float64
output = func_828(var_829,var_830,var_831,)
func_832 = relay.Function([var_829,var_830,var_831,], output)
mutated_mod['func_832'] = func_832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_839 = func_203_call()
call_840 = func_203_call()
func_688_call = mod.get_global_var('func_688')
func_692_call = mutated_mod.get_global_var('func_692')
const_850 = relay.const([[-3,-9,-5,-7,9,8,-9,10,10,10,2,-9,-5,5],[-10,4,-2,-10,-1,-3,8,6,6,-3,-9,-4,4,-8],[-2,8,7,-5,6,7,-4,-8,2,2,-1,4,-7,-1],[-2,1,3,5,-3,3,8,9,-10,8,10,-2,4,-2],[-4,3,-5,7,-6,-10,-5,-2,-2,-6,-5,-6,4,-7],[4,1,-4,4,-1,-7,-5,9,1,4,-10,8,5,-4],[4,5,-3,-7,-1,8,6,-10,-4,3,-10,-1,-7,8],[4,9,5,7,-2,-7,-5,-6,10,-2,-9,-10,-1,-1],[-1,-10,-3,5,5,-6,-6,10,7,2,6,-10,10,3],[-2,-2,3,7,9,4,4,10,4,-1,8,6,9,8],[-7,-3,-5,-1,-4,-4,2,8,-9,-6,-8,2,10,1],[-6,-1,2,-4,-8,7,5,7,-1,-3,-3,3,-6,9],[-7,-7,9,-5,-3,-8,-4,-5,8,4,6,10,-6,1]], dtype = "int16")#candidate|850|(13, 14)|const|int16
call_849 = relay.TupleGetItem(func_688_call(relay.reshape(const_850.astype('int16'), [14, 13, 1]), relay.reshape(const_850.astype('int16'), [14, 13, 1]), ), 1)
call_851 = relay.TupleGetItem(func_692_call(relay.reshape(const_850.astype('int16'), [14, 13, 1]), relay.reshape(const_850.astype('int16'), [14, 13, 1]), ), 1)
output = relay.Tuple([call_839,call_849,const_850,])
output2 = relay.Tuple([call_840,call_851,const_850,])
func_861 = relay.Function([], output)
mod['func_861'] = func_861
mod = relay.transform.InferType()(mod)
mutated_mod['func_861'] = func_861
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mutated_mod.get_global_var('func_861')
call_862 = func_861_call()
output = call_862
func_863 = relay.Function([], output)
mutated_mod['func_863'] = func_863
mutated_mod = relay.transform.InferType()(mutated_mod)
const_893 = relay.const([[[-4.139669,-5.606984,-3.978881,-5.958945,-8.366446,8.861303,7.269105,7.669378,-0.241537],[7.454749,8.557018,6.556521,5.473777,-7.759086,3.106004,-1.494777,3.530277,8.060878],[-2.041771,5.559523,8.665747,-3.191720,-1.591295,5.425620,5.269627,4.271249,-4.177808],[-9.385470,4.594487,1.599240,-7.527095,6.382993,-7.154483,0.089735,-7.977579,0.004698],[1.237171,3.180303,-7.879843,0.431443,5.910769,-0.345956,0.896017,3.750791,1.552374],[5.272305,-6.240546,5.986442,7.604415,9.274930,-2.857196,0.848743,-2.144515,7.023802],[-4.679531,3.610480,2.057972,3.025788,-8.359406,6.112541,5.020112,-0.843852,4.054990],[-7.198945,-4.724659,5.418935,4.916647,2.595212,7.003196,-4.500167,3.330075,3.645100],[1.433074,9.086446,5.327906,-2.149035,-7.304489,-5.952890,-7.501464,-4.231995,-7.344129],[1.141071,6.627364,-5.680979,0.897416,-1.389640,-1.946852,7.473853,-5.728881,5.628279],[-4.592409,5.062884,-0.918800,-3.299756,-9.141757,-0.652831,-7.645295,-6.728112,-9.353911],[-6.715992,9.324269,-8.390065,-5.086430,-5.960745,-1.241812,-0.707891,8.133992,8.662895],[9.278244,-6.281967,6.368927,0.071292,0.582413,1.400047,-8.536666,1.695602,-5.846807],[9.645090,-5.893772,7.780741,8.553777,7.032052,7.404345,6.365827,-1.023700,0.598524],[-2.303692,-9.961932,-6.039650,9.021533,0.241376,8.232754,-8.053881,7.091841,-2.170322]],[[6.617716,-8.056095,-1.354139,-9.977194,2.221754,8.790884,-2.782106,6.060571,7.458710],[-5.446292,-0.364200,-7.924379,9.999312,-9.024932,9.130128,1.014278,-1.351098,7.317988],[-9.504339,-0.626689,-7.014308,-8.197879,0.117925,9.600242,0.953627,0.194337,-0.574198],[3.241644,-0.128382,-3.095197,-9.966617,8.064261,9.311625,5.819059,-8.718422,0.250413],[-0.905672,2.290389,6.169903,-4.140785,-6.750613,-3.056672,3.043666,-7.487378,8.576116],[4.254668,-5.027139,0.344377,1.300249,7.257131,-3.905365,8.607371,-7.058687,2.512652],[1.051443,4.358184,8.807730,-2.320462,4.919415,7.816147,5.483843,8.452759,5.018347],[-0.738854,5.735762,-1.107244,-2.651613,-8.136428,-7.469785,2.641704,-5.540400,9.024679],[-9.690724,-8.049141,-2.262080,4.136901,6.473756,7.512543,5.177801,4.412901,-8.536667],[-6.736407,6.806102,5.454477,-2.185255,-5.506257,2.024149,3.709778,6.667320,-7.992263],[3.735928,-4.747328,-2.936337,0.610927,0.689112,-1.650136,-2.833605,-5.645317,-3.598965],[2.184045,-6.258286,4.318226,3.011829,-1.979025,-1.464641,-7.539049,-0.490300,-8.041550],[-1.271105,-7.502428,7.689393,3.826645,7.024949,2.937392,-2.319229,3.620498,-5.030064],[-4.465451,9.935654,1.272245,3.038081,1.952667,-3.767668,-5.894245,7.037410,-5.133364],[-8.614796,-3.355493,3.635263,2.943794,-1.085702,3.831697,3.208718,-3.537530,-6.334824]],[[-5.347437,6.641176,0.495205,-2.967155,-4.637885,-4.307114,-6.012483,0.349244,-1.843168],[-1.409657,-2.720556,-7.296359,-5.936144,4.815571,-3.100641,-8.796999,-2.063395,-6.062494],[7.996242,8.089972,-4.243383,-9.483607,-2.919091,2.545199,-6.789829,-3.590927,-3.825874],[-0.409324,-0.341991,9.729608,8.891175,-7.247331,9.381241,5.415974,2.739636,5.256618],[-3.653106,-5.856077,0.405626,-2.955398,6.918895,-2.812919,8.856743,-2.875754,-4.417973],[4.881836,3.367363,8.933510,-1.239477,2.439704,-3.633657,-2.372158,-7.222070,9.011969],[-4.455149,-2.003986,4.795883,-1.925146,8.055013,-3.880155,-2.492315,-6.065230,8.451521],[7.369499,-4.365767,8.006432,4.506285,-6.676165,-2.972440,2.723619,7.449537,7.101578],[-6.276997,2.026459,-6.228650,8.047723,0.512942,9.461189,-1.279844,1.390718,1.882057],[8.627911,-2.054155,8.610221,9.586876,4.817210,-8.892501,8.674641,-9.983134,-2.269402],[7.431542,-3.790087,1.711413,4.734541,-4.780443,8.072399,-6.197201,-9.263219,-6.336924],[6.642159,-6.165154,-7.645356,8.874494,1.297532,-1.858834,8.090429,8.987568,2.789469],[0.439737,-9.657930,7.532648,2.008301,-3.620287,-6.362823,6.872930,2.967203,-1.210858],[-1.993021,5.177208,-4.275845,-5.580060,3.052960,5.219770,-8.045752,-0.937411,-9.354337],[-3.449915,2.449638,4.685490,1.200953,7.810789,-8.214608,-7.577419,-1.202412,-7.182552]],[[-7.604269,-2.228715,-1.460037,-9.558087,-9.872892,-7.815357,-2.642006,-5.865588,2.887531],[5.478120,8.581808,2.990075,-5.462646,-6.136056,-7.974357,9.024946,5.737677,-4.193106],[8.649713,8.341077,0.998074,-1.530756,-1.070705,6.071210,-2.931029,2.673809,-8.016640],[9.576390,-3.315081,1.844517,-0.212601,4.597292,-4.056501,-1.665114,-5.653267,1.956150],[3.014787,1.530404,-1.684605,3.691925,8.442225,-0.796400,-7.190564,5.689524,-1.155797],[2.542022,5.110785,-4.918331,-8.334038,-4.954009,-6.634048,7.845130,5.825686,-3.125651],[2.041661,3.424056,-6.586222,-4.763001,9.309496,1.601867,-7.882056,0.937635,-6.334391],[9.385579,-7.453121,2.637562,6.573385,-6.867850,-1.457335,5.006135,-6.494653,-3.525758],[-2.447971,8.504802,-7.405674,0.148437,1.051494,5.175776,7.558427,3.254115,-5.005876],[-6.704915,8.354787,-8.885148,6.915865,8.678518,-2.444024,-1.144270,5.895862,6.956905],[0.539893,-3.073101,8.640196,-5.577269,4.278763,-6.015258,-3.989688,7.270311,3.001715],[7.011315,3.409902,-3.693998,5.926260,6.480964,7.598123,-1.494460,5.905214,1.836975],[-3.547207,2.010469,9.733479,0.291119,6.060038,2.323555,9.816265,9.185834,-4.718853],[-6.100879,5.101414,-2.642896,-7.421692,0.112460,7.139551,-6.257452,-9.984252,9.884047],[3.503733,9.817308,-9.799236,8.427820,-7.848815,-9.188490,6.933115,-0.704731,-2.550549]]], dtype = "float32")#candidate|893|(4, 15, 9)|const|float32
uop_894 = relay.cosh(const_893.astype('float32')) # shape=(4, 15, 9)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_901 = relay.TupleGetItem(func_299_call(), 0)
call_902 = relay.TupleGetItem(func_300_call(), 0)
uop_903 = relay.log(uop_894.astype('float64')) # shape=(4, 15, 9)
output = relay.Tuple([call_901,uop_903,])
output2 = relay.Tuple([call_902,uop_903,])
func_912 = relay.Function([], output)
mod['func_912'] = func_912
mod = relay.transform.InferType()(mod)
output = func_912()
func_913 = relay.Function([], output)
mutated_mod['func_913'] = func_913
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_863_call = mutated_mod.get_global_var('func_863')
call_936 = relay.TupleGetItem(func_861_call(), 0)
call_937 = relay.TupleGetItem(func_863_call(), 0)
output = relay.Tuple([call_936,])
output2 = relay.Tuple([call_937,])
func_941 = relay.Function([], output)
mod['func_941'] = func_941
mod = relay.transform.InferType()(mod)
output = func_941()
func_942 = relay.Function([], output)
mutated_mod['func_942'] = func_942
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_960 = func_196_call()
call_961 = func_196_call()
output = call_960
output2 = call_961
func_967 = relay.Function([], output)
mod['func_967'] = func_967
mod = relay.transform.InferType()(mod)
output = func_967()
func_968 = relay.Function([], output)
mutated_mod['func_968'] = func_968
mutated_mod = relay.transform.InferType()(mutated_mod)
var_997 = relay.var("var_997", dtype = "float32", shape = (9, 12, 1))#candidate|997|(9, 12, 1)|var|float32
uop_998 = relay.atanh(var_997.astype('float32')) # shape=(9, 12, 1)
output = uop_998
output2 = uop_998
func_1001 = relay.Function([var_997,], output)
mod['func_1001'] = func_1001
mod = relay.transform.InferType()(mod)
var_1002 = relay.var("var_1002", dtype = "float32", shape = (9, 12, 1))#candidate|1002|(9, 12, 1)|var|float32
output = func_1001(var_1002)
func_1003 = relay.Function([var_1002], output)
mutated_mod['func_1003'] = func_1003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_912_call = mod.get_global_var('func_912')
func_913_call = mutated_mod.get_global_var('func_913')
call_1020 = relay.TupleGetItem(func_912_call(), 0)
call_1021 = relay.TupleGetItem(func_913_call(), 0)
uop_1035 = relay.cos(call_1020.astype('float64')) # shape=(7, 10, 2)
uop_1037 = relay.cos(call_1021.astype('float64')) # shape=(7, 10, 2)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_1046 = func_196_call()
call_1047 = func_196_call()
output = relay.Tuple([uop_1035,call_1046,])
output2 = relay.Tuple([uop_1037,call_1047,])
func_1050 = relay.Function([], output)
mod['func_1050'] = func_1050
mod = relay.transform.InferType()(mod)
output = func_1050()
func_1051 = relay.Function([], output)
mutated_mod['func_1051'] = func_1051
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1080 = relay.var("var_1080", dtype = "uint64", shape = (5, 9, 1))#candidate|1080|(5, 9, 1)|var|uint64
var_1081 = relay.var("var_1081", dtype = "uint64", shape = (5, 9, 2))#candidate|1081|(5, 9, 2)|var|uint64
bop_1082 = relay.subtract(var_1080.astype('uint64'), var_1081.astype('uint64')) # shape=(5, 9, 2)
output = relay.Tuple([bop_1082,])
output2 = relay.Tuple([bop_1082,])
func_1090 = relay.Function([var_1080,var_1081,], output)
mod['func_1090'] = func_1090
mod = relay.transform.InferType()(mod)
var_1091 = relay.var("var_1091", dtype = "uint64", shape = (5, 9, 1))#candidate|1091|(5, 9, 1)|var|uint64
var_1092 = relay.var("var_1092", dtype = "uint64", shape = (5, 9, 2))#candidate|1092|(5, 9, 2)|var|uint64
output = func_1090(var_1091,var_1092,)
func_1093 = relay.Function([var_1091,var_1092,], output)
mutated_mod['func_1093'] = func_1093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_912_call = mod.get_global_var('func_912')
func_913_call = mutated_mod.get_global_var('func_913')
call_1095 = relay.TupleGetItem(func_912_call(), 0)
call_1096 = relay.TupleGetItem(func_913_call(), 0)
func_556_call = mod.get_global_var('func_556')
func_559_call = mutated_mod.get_global_var('func_559')
var_1123 = relay.var("var_1123", dtype = "float64", shape = (44,))#candidate|1123|(44,)|var|float64
call_1122 = relay.TupleGetItem(func_556_call(relay.reshape(var_1123.astype('float64'), [44,])), 3)
call_1124 = relay.TupleGetItem(func_559_call(relay.reshape(var_1123.astype('float64'), [44,])), 3)
output = relay.Tuple([call_1095,call_1122,var_1123,])
output2 = relay.Tuple([call_1096,call_1124,var_1123,])
func_1125 = relay.Function([var_1123,], output)
mod['func_1125'] = func_1125
mod = relay.transform.InferType()(mod)
var_1126 = relay.var("var_1126", dtype = "float64", shape = (44,))#candidate|1126|(44,)|var|float64
output = func_1125(var_1126)
func_1127 = relay.Function([var_1126], output)
mutated_mod['func_1127'] = func_1127
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_863_call = mutated_mod.get_global_var('func_863')
call_1184 = relay.TupleGetItem(func_861_call(), 1)
call_1185 = relay.TupleGetItem(func_863_call(), 1)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_1186 = func_203_call()
call_1187 = func_203_call()
uop_1193 = relay.log10(call_1186.astype('float32')) # shape=(7, 10, 2)
uop_1195 = relay.log10(call_1187.astype('float32')) # shape=(7, 10, 2)
output = relay.Tuple([call_1184,uop_1193,])
output2 = relay.Tuple([call_1185,uop_1195,])
func_1196 = relay.Function([], output)
mod['func_1196'] = func_1196
mod = relay.transform.InferType()(mod)
mutated_mod['func_1196'] = func_1196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1196_call = mutated_mod.get_global_var('func_1196')
call_1197 = func_1196_call()
output = call_1197
func_1198 = relay.Function([], output)
mutated_mod['func_1198'] = func_1198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_1248 = func_196_call()
call_1249 = func_196_call()
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
const_1251 = relay.const([[-5,-3,-9,9,9],[-4,6,-6,-7,-2],[6,1,-9,6,1],[10,-1,8,-7,-9],[-8,5,-4,-6,-3],[-7,6,3,-9,9],[2,-5,-2,2,-1]], dtype = "uint8")#candidate|1251|(7, 5)|const|uint8
var_1252 = relay.var("var_1252", dtype = "float64", shape = (44,))#candidate|1252|(44,)|var|float64
call_1250 = relay.TupleGetItem(func_828_call(relay.reshape(const_1251.astype('uint8'), [5, 7]), relay.reshape(const_1251.astype('uint8'), [5, 7]), relay.reshape(var_1252.astype('float64'), [11, 4]), ), 2)
call_1253 = relay.TupleGetItem(func_832_call(relay.reshape(const_1251.astype('uint8'), [5, 7]), relay.reshape(const_1251.astype('uint8'), [5, 7]), relay.reshape(var_1252.astype('float64'), [11, 4]), ), 2)
func_318_call = mod.get_global_var('func_318')
func_319_call = mutated_mod.get_global_var('func_319')
call_1254 = func_318_call()
call_1255 = func_318_call()
uop_1257 = relay.asin(call_1254.astype('float32')) # shape=(7, 10, 2)
uop_1259 = relay.asin(call_1255.astype('float32')) # shape=(7, 10, 2)
output = relay.Tuple([call_1248,call_1250,const_1251,var_1252,uop_1257,])
output2 = relay.Tuple([call_1249,call_1253,const_1251,var_1252,uop_1259,])
func_1272 = relay.Function([var_1252,], output)
mod['func_1272'] = func_1272
mod = relay.transform.InferType()(mod)
mutated_mod['func_1272'] = func_1272
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1273 = relay.var("var_1273", dtype = "float64", shape = (44,))#candidate|1273|(44,)|var|float64
func_1272_call = mutated_mod.get_global_var('func_1272')
call_1274 = func_1272_call(var_1273)
output = call_1274
func_1275 = relay.Function([var_1273], output)
mutated_mod['func_1275'] = func_1275
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_942_call = mutated_mod.get_global_var('func_942')
call_1303 = relay.TupleGetItem(func_941_call(), 0)
call_1304 = relay.TupleGetItem(func_942_call(), 0)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_1310 = func_203_call()
call_1311 = func_203_call()
uop_1313 = relay.atanh(call_1310.astype('float32')) # shape=(7, 10, 2)
uop_1315 = relay.atanh(call_1311.astype('float32')) # shape=(7, 10, 2)
func_1125_call = mod.get_global_var('func_1125')
func_1127_call = mutated_mod.get_global_var('func_1127')
const_1319 = relay.const([7.341872,6.780966,4.250454,-9.716819,1.413974,1.705551,-7.676204,1.495715,0.050513,7.578304,3.182021,-2.615935,6.530028,-6.221825,-7.205255,-0.370962,3.036817,9.814506,-8.055600,5.076924,3.947881,9.944651,1.784057,-7.273972,7.391439,1.470355,4.811457,8.844371,-0.505563,5.996924,7.549634,-9.819690,1.201742,2.722303,1.189854,-8.332553,0.767346,-2.718491,-7.250633,1.708564,-2.706682,-9.753867,4.175826,-5.380828], dtype = "float64")#candidate|1319|(44,)|const|float64
call_1318 = relay.TupleGetItem(func_1125_call(relay.reshape(const_1319.astype('float64'), [44,])), 2)
call_1320 = relay.TupleGetItem(func_1127_call(relay.reshape(const_1319.astype('float64'), [44,])), 2)
func_1090_call = mod.get_global_var('func_1090')
func_1093_call = mutated_mod.get_global_var('func_1093')
const_1330 = relay.const([7,-10,-9,-8,8,3,1,8,-7,-9,-10,1,-7,8,-7,3,4,-4,10,7,5,5,10,-8,-4,1,-10,-10,5,2,4,8,3,-3,6,-10,10,9,-9,-8,-1,-6,5,-9,5], dtype = "uint64")#candidate|1330|(45,)|const|uint64
var_1331 = relay.var("var_1331", dtype = "uint64", shape = (45, 2))#candidate|1331|(45, 2)|var|uint64
call_1329 = relay.TupleGetItem(func_1090_call(relay.reshape(const_1330.astype('uint64'), [5, 9, 1]), relay.reshape(var_1331.astype('uint64'), [5, 9, 2]), ), 0)
call_1332 = relay.TupleGetItem(func_1093_call(relay.reshape(const_1330.astype('uint64'), [5, 9, 1]), relay.reshape(var_1331.astype('uint64'), [5, 9, 2]), ), 0)
output = relay.Tuple([call_1303,uop_1313,call_1318,const_1319,call_1329,const_1330,var_1331,])
output2 = relay.Tuple([call_1304,uop_1315,call_1320,const_1319,call_1332,const_1330,var_1331,])
func_1345 = relay.Function([var_1331,], output)
mod['func_1345'] = func_1345
mod = relay.transform.InferType()(mod)
var_1346 = relay.var("var_1346", dtype = "uint64", shape = (45, 2))#candidate|1346|(45, 2)|var|uint64
output = func_1345(var_1346)
func_1347 = relay.Function([var_1346], output)
mutated_mod['func_1347'] = func_1347
mutated_mod = relay.transform.InferType()(mutated_mod)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_1362 = relay.TupleGetItem(func_759_call(), 0)
call_1363 = relay.TupleGetItem(func_761_call(), 0)
const_1376 = relay.const([[[5.919050,-3.954433],[-2.485954,9.936906],[5.970805,4.823976],[0.825412,-1.371395],[-5.985825,-5.367080],[6.978355,0.966792],[8.847110,2.918754],[-1.581370,9.242937],[9.288827,-1.832166],[-1.764605,-6.175172]],[[0.211613,6.648734],[6.542529,2.107846],[-1.193362,6.297340],[-8.086592,6.596958],[6.891627,-1.626730],[-7.489645,-2.830364],[1.596145,6.287809],[-7.653813,8.108656],[6.434375,-4.692692],[2.964326,0.502547]],[[3.764660,7.881205],[4.276521,4.046364],[9.092931,-8.444015],[-7.185753,-8.559441],[0.395250,3.965270],[9.882048,-2.085341],[1.664625,0.436484],[-7.482815,-7.381473],[1.253920,7.644833],[-0.428129,-6.461256]],[[-8.961635,4.060001],[5.453911,9.430565],[-2.984273,-9.913281],[4.144403,-4.303171],[9.211513,6.748468],[-9.765676,2.819863],[5.499074,-2.515619],[6.054587,-1.557890],[-9.890141,-2.987819],[7.865901,-2.780313]],[[-2.200237,2.853249],[1.309888,-5.399644],[-7.314057,-7.575055],[3.455584,-8.943794],[-9.784885,1.173250],[2.027430,-2.419906],[3.608168,1.771394],[-3.458371,-2.498883],[-5.734504,-9.914262],[-4.865108,-2.561867]],[[1.541158,5.350712],[-0.513783,0.946329],[9.268040,4.748084],[-5.952403,-0.058703],[-1.684012,-9.635405],[9.374794,-3.135259],[6.166104,-5.263551],[1.505853,-8.802892],[2.986835,-8.810984],[8.039779,4.403788]],[[-2.811231,-2.371970],[-0.309215,-8.470207],[-4.507442,2.909650],[-1.039760,-6.852545],[-5.368040,4.337822],[7.278975,-8.301890],[3.945050,2.000314],[6.318484,7.800804],[1.324192,-4.580339],[-7.339776,-5.580371]]], dtype = "float64")#candidate|1376|(7, 10, 2)|const|float64
bop_1377 = relay.greater_equal(call_1362.astype('bool'), relay.reshape(const_1376.astype('bool'), relay.shape_of(call_1362))) # shape=(7, 10, 2)
bop_1380 = relay.greater_equal(call_1363.astype('bool'), relay.reshape(const_1376.astype('bool'), relay.shape_of(call_1363))) # shape=(7, 10, 2)
uop_1399 = relay.acosh(const_1376.astype('float64')) # shape=(7, 10, 2)
func_1050_call = mod.get_global_var('func_1050')
func_1051_call = mutated_mod.get_global_var('func_1051')
call_1401 = relay.TupleGetItem(func_1050_call(), 0)
call_1402 = relay.TupleGetItem(func_1051_call(), 0)
output = relay.Tuple([bop_1377,uop_1399,call_1401,])
output2 = relay.Tuple([bop_1380,uop_1399,call_1402,])
func_1409 = relay.Function([], output)
mod['func_1409'] = func_1409
mod = relay.transform.InferType()(mod)
output = func_1409()
func_1410 = relay.Function([], output)
mutated_mod['func_1410'] = func_1410
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_1414 = func_196_call()
call_1415 = func_196_call()
output = call_1414
output2 = call_1415
func_1416 = relay.Function([], output)
mod['func_1416'] = func_1416
mod = relay.transform.InferType()(mod)
output = func_1416()
func_1417 = relay.Function([], output)
mutated_mod['func_1417'] = func_1417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_1494 = func_196_call()
call_1495 = func_196_call()
output = call_1494
output2 = call_1495
func_1507 = relay.Function([], output)
mod['func_1507'] = func_1507
mod = relay.transform.InferType()(mod)
output = func_1507()
func_1508 = relay.Function([], output)
mutated_mod['func_1508'] = func_1508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1507_call = mod.get_global_var('func_1507')
func_1508_call = mutated_mod.get_global_var('func_1508')
call_1547 = func_1507_call()
call_1548 = func_1507_call()
output = relay.Tuple([call_1547,])
output2 = relay.Tuple([call_1548,])
func_1552 = relay.Function([], output)
mod['func_1552'] = func_1552
mod = relay.transform.InferType()(mod)
mutated_mod['func_1552'] = func_1552
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1552_call = mutated_mod.get_global_var('func_1552')
call_1553 = func_1552_call()
output = call_1553
func_1554 = relay.Function([], output)
mutated_mod['func_1554'] = func_1554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_967_call = mod.get_global_var('func_967')
func_968_call = mutated_mod.get_global_var('func_968')
call_1567 = func_967_call()
call_1568 = func_967_call()
func_696_call = mod.get_global_var('func_696')
func_697_call = mutated_mod.get_global_var('func_697')
call_1578 = relay.TupleGetItem(func_696_call(), 0)
call_1579 = relay.TupleGetItem(func_697_call(), 0)
output = relay.Tuple([call_1567,call_1578,])
output2 = relay.Tuple([call_1568,call_1579,])
func_1584 = relay.Function([], output)
mod['func_1584'] = func_1584
mod = relay.transform.InferType()(mod)
output = func_1584()
func_1585 = relay.Function([], output)
mutated_mod['func_1585'] = func_1585
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1552_call = mod.get_global_var('func_1552')
func_1554_call = mutated_mod.get_global_var('func_1554')
call_1626 = relay.TupleGetItem(func_1552_call(), 0)
call_1627 = relay.TupleGetItem(func_1554_call(), 0)
output = relay.Tuple([call_1626,])
output2 = relay.Tuple([call_1627,])
func_1629 = relay.Function([], output)
mod['func_1629'] = func_1629
mod = relay.transform.InferType()(mod)
mutated_mod['func_1629'] = func_1629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mutated_mod.get_global_var('func_1629')
call_1630 = func_1629_call()
output = call_1630
func_1631 = relay.Function([], output)
mutated_mod['func_1631'] = func_1631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1409_call = mod.get_global_var('func_1409')
func_1410_call = mutated_mod.get_global_var('func_1410')
call_1637 = relay.TupleGetItem(func_1409_call(), 0)
call_1638 = relay.TupleGetItem(func_1410_call(), 0)
output = relay.Tuple([call_1637,])
output2 = relay.Tuple([call_1638,])
func_1639 = relay.Function([], output)
mod['func_1639'] = func_1639
mod = relay.transform.InferType()(mod)
output = func_1639()
func_1640 = relay.Function([], output)
mutated_mod['func_1640'] = func_1640
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1050_call = mod.get_global_var('func_1050')
func_1051_call = mutated_mod.get_global_var('func_1051')
call_1641 = relay.TupleGetItem(func_1050_call(), 0)
call_1642 = relay.TupleGetItem(func_1051_call(), 0)
output = relay.Tuple([call_1641,])
output2 = relay.Tuple([call_1642,])
func_1646 = relay.Function([], output)
mod['func_1646'] = func_1646
mod = relay.transform.InferType()(mod)
output = func_1646()
func_1647 = relay.Function([], output)
mutated_mod['func_1647'] = func_1647
mutated_mod = relay.transform.InferType()(mutated_mod)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_1681 = relay.TupleGetItem(func_299_call(), 2)
call_1682 = relay.TupleGetItem(func_300_call(), 2)
output = call_1681
output2 = call_1682
func_1703 = relay.Function([], output)
mod['func_1703'] = func_1703
mod = relay.transform.InferType()(mod)
mutated_mod['func_1703'] = func_1703
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1703_call = mutated_mod.get_global_var('func_1703')
call_1704 = func_1703_call()
output = call_1704
func_1705 = relay.Function([], output)
mutated_mod['func_1705'] = func_1705
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_942_call = mutated_mod.get_global_var('func_942')
call_1847 = relay.TupleGetItem(func_941_call(), 0)
call_1848 = relay.TupleGetItem(func_942_call(), 0)
output = relay.Tuple([call_1847,])
output2 = relay.Tuple([call_1848,])
func_1850 = relay.Function([], output)
mod['func_1850'] = func_1850
mod = relay.transform.InferType()(mod)
output = func_1850()
func_1851 = relay.Function([], output)
mutated_mod['func_1851'] = func_1851
mutated_mod = relay.transform.InferType()(mutated_mod)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_1937 = relay.TupleGetItem(func_299_call(), 1)
call_1938 = relay.TupleGetItem(func_300_call(), 1)
func_1272_call = mod.get_global_var('func_1272')
func_1275_call = mutated_mod.get_global_var('func_1275')
const_1948 = relay.const([-6.643699,4.969998,-7.146673,-7.828094,-1.250045,-4.930641,-0.412020,5.773235,-4.955093,5.368306,6.056018,0.991843,6.748973,8.353383,-8.911204,-9.019012,7.306670,-8.507599,3.377547,-8.202115,3.393689,-0.321223,-8.151303,7.485455,8.356013,-7.242702,-6.689212,-5.001445,-1.029838,4.885344,1.779995,3.561057,1.765986,-6.938186,1.442941,5.918753,1.708071,-0.909968,1.098226,-8.406804,8.404862,2.931432,-7.696774,2.234473], dtype = "float64")#candidate|1948|(44,)|const|float64
call_1947 = relay.TupleGetItem(func_1272_call(relay.reshape(const_1948.astype('float64'), [44,])), 0)
call_1949 = relay.TupleGetItem(func_1275_call(relay.reshape(const_1948.astype('float64'), [44,])), 0)
uop_1957 = relay.acos(call_1937.astype('float64')) # shape=(7, 10, 2)
uop_1959 = relay.acos(call_1938.astype('float64')) # shape=(7, 10, 2)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_1971 = func_1416_call()
call_1972 = func_1416_call()
const_1978 = relay.const([[[-7.452316,-0.171825],[8.871700,6.940667],[7.548813,-5.610441],[0.823816,-0.191291],[-0.952715,-7.724724],[1.459138,-6.372934],[-7.428781,6.365120],[1.247155,3.917185],[-3.575292,-8.336583],[1.641357,8.537005]],[[6.910660,8.506458],[0.637385,1.011674],[7.836186,7.539729],[0.555174,9.935328],[-0.945323,3.359604],[-0.300354,4.397465],[-9.658724,-9.220781],[1.371086,-8.377251],[0.592096,7.300606],[1.697065,-3.558605]],[[3.354375,-1.610009],[0.559556,-4.748584],[-1.273314,-4.971479],[-0.846415,3.747350],[2.656199,4.448842],[4.970490,-3.417535],[7.612735,6.110365],[-5.297408,9.595135],[9.602812,-7.938984],[-6.211708,-4.778272]],[[-4.134631,6.819563],[-5.634541,-0.226432],[-0.535264,7.508395],[6.553916,-9.704893],[6.706422,-7.149065],[4.789510,7.610121],[9.048424,8.193772],[3.458402,-9.962415],[-9.516483,-7.421955],[-0.714522,1.596867]],[[-0.720603,-1.096416],[-2.729393,-6.986724],[-9.978584,7.539806],[6.726241,-9.755061],[2.148789,-0.266496],[-5.671693,-9.471068],[-6.878096,3.763084],[3.206042,0.781508],[0.999378,-8.066104],[-1.559527,-6.544463]],[[4.803432,-7.975503],[-2.626635,9.854857],[-9.073536,-9.510419],[-1.184417,-6.211729],[-2.857433,8.219577],[-5.596077,1.394549],[-1.051343,6.108320],[1.657216,0.958775],[6.262620,3.805807],[-9.973442,7.983110]],[[-8.298818,3.694262],[0.529980,0.088377],[-1.912560,9.801970],[5.103025,-9.249804],[-7.597429,-3.444943],[7.000751,-8.674073],[2.126292,1.095594],[-4.498965,-6.869226],[-2.573793,6.202128],[4.395003,1.228511]]], dtype = "float64")#candidate|1978|(7, 10, 2)|const|float64
bop_1979 = relay.less(uop_1957.astype('bool'), relay.reshape(const_1978.astype('bool'), relay.shape_of(uop_1957))) # shape=(7, 10, 2)
bop_1982 = relay.less(uop_1959.astype('bool'), relay.reshape(const_1978.astype('bool'), relay.shape_of(uop_1959))) # shape=(7, 10, 2)
output = relay.Tuple([call_1947,const_1948,call_1971,bop_1979,])
output2 = relay.Tuple([call_1949,const_1948,call_1972,bop_1982,])
func_1986 = relay.Function([], output)
mod['func_1986'] = func_1986
mod = relay.transform.InferType()(mod)
mutated_mod['func_1986'] = func_1986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mutated_mod.get_global_var('func_1986')
call_1987 = func_1986_call()
output = call_1987
func_1988 = relay.Function([], output)
mutated_mod['func_1988'] = func_1988
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1552_call = mod.get_global_var('func_1552')
func_1554_call = mutated_mod.get_global_var('func_1554')
call_2020 = relay.TupleGetItem(func_1552_call(), 0)
call_2021 = relay.TupleGetItem(func_1554_call(), 0)
const_2033 = relay.const([[[-2.211585,-8.839266],[-7.402562,1.185850],[-2.915340,0.849801],[-9.711205,0.724903],[4.560979,9.488711],[6.166508,7.506248],[2.859040,6.974779],[-0.660278,-8.342631],[-5.190374,8.582514],[0.075865,-6.307254]],[[-6.284709,-8.950580],[2.206266,6.805792],[2.021420,-4.174926],[2.867113,1.220623],[-5.717040,5.923339],[6.754121,-8.864620],[-3.099144,-0.720472],[-4.694762,-0.736400],[6.814197,6.114796],[-4.314176,8.108003]],[[0.655776,-1.734890],[0.346770,0.407000],[5.701372,-8.095936],[5.459488,-7.092031],[6.178411,1.821600],[3.786499,-5.437594],[5.350735,8.972851],[0.020422,1.362560],[5.808239,1.047870],[-3.940548,-8.000100]],[[4.397819,-5.787981],[1.959982,4.702218],[-9.590717,0.825193],[-5.802119,-0.381861],[9.700651,7.016419],[-6.149124,-5.153326],[0.658128,-9.705543],[-7.395157,5.013475],[-5.873713,-0.190841],[-8.257460,-6.039087]],[[4.869960,-5.156376],[0.982944,0.635813],[-8.618329,9.721465],[9.168188,-9.172606],[-0.739139,-1.881017],[-2.089837,-3.255161],[-4.240082,-6.597485],[-8.261181,4.102321],[-3.925920,8.881507],[-2.190670,0.888413]],[[-9.051127,0.009156],[-4.913355,-4.746877],[-0.632409,0.092091],[-6.894030,5.657262],[8.352630,2.391675],[-2.032877,2.382420],[-9.121110,2.234952],[1.336143,1.388045],[4.082073,4.922474],[1.505106,-3.862600]],[[5.177227,-6.806710],[-9.018708,-2.719925],[0.820557,1.449365],[-8.166037,7.144398],[-6.921855,7.701392],[3.328913,8.490800],[2.794580,-3.521828],[-9.624190,-8.077205],[-6.064386,5.313546],[1.870087,-6.173977]]], dtype = "float64")#candidate|2033|(7, 10, 2)|const|float64
bop_2034 = relay.floor_mod(call_2020.astype('float64'), relay.reshape(const_2033.astype('float64'), relay.shape_of(call_2020))) # shape=(7, 10, 2)
bop_2037 = relay.floor_mod(call_2021.astype('float64'), relay.reshape(const_2033.astype('float64'), relay.shape_of(call_2021))) # shape=(7, 10, 2)
uop_2048 = relay.sigmoid(call_2020.astype('float64')) # shape=(7, 10, 2)
uop_2050 = relay.sigmoid(call_2021.astype('float64')) # shape=(7, 10, 2)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_2056 = func_203_call()
call_2057 = func_203_call()
var_2060 = relay.var("var_2060", dtype = "float64", shape = (7, 10, 2))#candidate|2060|(7, 10, 2)|var|float64
bop_2061 = relay.logical_xor(call_2056.astype('uint16'), relay.reshape(var_2060.astype('uint16'), relay.shape_of(call_2056))) # shape=(7, 10, 2)
bop_2064 = relay.logical_xor(call_2057.astype('uint16'), relay.reshape(var_2060.astype('uint16'), relay.shape_of(call_2057))) # shape=(7, 10, 2)
output = relay.Tuple([bop_2034,uop_2048,bop_2061,])
output2 = relay.Tuple([bop_2037,uop_2050,bop_2064,])
func_2069 = relay.Function([var_2060,], output)
mod['func_2069'] = func_2069
mod = relay.transform.InferType()(mod)
var_2070 = relay.var("var_2070", dtype = "float64", shape = (7, 10, 2))#candidate|2070|(7, 10, 2)|var|float64
output = func_2069(var_2070)
func_2071 = relay.Function([var_2070], output)
mutated_mod['func_2071'] = func_2071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1584_call = mod.get_global_var('func_1584')
func_1585_call = mutated_mod.get_global_var('func_1585')
call_2092 = relay.TupleGetItem(func_1584_call(), 1)
call_2093 = relay.TupleGetItem(func_1585_call(), 1)
output = relay.Tuple([call_2092,])
output2 = relay.Tuple([call_2093,])
func_2098 = relay.Function([], output)
mod['func_2098'] = func_2098
mod = relay.transform.InferType()(mod)
output = func_2098()
func_2099 = relay.Function([], output)
mutated_mod['func_2099'] = func_2099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_696_call = mod.get_global_var('func_696')
func_697_call = mutated_mod.get_global_var('func_697')
call_2139 = relay.TupleGetItem(func_696_call(), 0)
call_2140 = relay.TupleGetItem(func_697_call(), 0)
output = call_2139
output2 = call_2140
func_2160 = relay.Function([], output)
mod['func_2160'] = func_2160
mod = relay.transform.InferType()(mod)
mutated_mod['func_2160'] = func_2160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2160_call = mutated_mod.get_global_var('func_2160')
call_2161 = func_2160_call()
output = call_2161
func_2162 = relay.Function([], output)
mutated_mod['func_2162'] = func_2162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1703_call = mod.get_global_var('func_1703')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_2187 = func_1703_call()
call_2188 = func_1703_call()
output = relay.Tuple([call_2187,])
output2 = relay.Tuple([call_2188,])
func_2198 = relay.Function([], output)
mod['func_2198'] = func_2198
mod = relay.transform.InferType()(mod)
mutated_mod['func_2198'] = func_2198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mutated_mod.get_global_var('func_2198')
call_2199 = func_2198_call()
output = call_2199
func_2200 = relay.Function([], output)
mutated_mod['func_2200'] = func_2200
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2342 = relay.var("var_2342", dtype = "float32", shape = (13, 6, 6))#candidate|2342|(13, 6, 6)|var|float32
uop_2343 = relay.sinh(var_2342.astype('float32')) # shape=(13, 6, 6)
uop_2348 = relay.asin(var_2342.astype('float64')) # shape=(13, 6, 6)
bop_2353 = relay.bitwise_xor(uop_2348.astype('int64'), relay.reshape(uop_2343.astype('int64'), relay.shape_of(uop_2348))) # shape=(13, 6, 6)
func_688_call = mod.get_global_var('func_688')
func_692_call = mutated_mod.get_global_var('func_692')
var_2364 = relay.var("var_2364", dtype = "int16", shape = (182,))#candidate|2364|(182,)|var|int16
call_2363 = relay.TupleGetItem(func_688_call(relay.reshape(var_2364.astype('int16'), [14, 13, 1]), relay.reshape(var_2364.astype('int16'), [14, 13, 1]), ), 0)
call_2365 = relay.TupleGetItem(func_692_call(relay.reshape(var_2364.astype('int16'), [14, 13, 1]), relay.reshape(var_2364.astype('int16'), [14, 13, 1]), ), 0)
output = relay.Tuple([bop_2353,call_2363,var_2364,])
output2 = relay.Tuple([bop_2353,call_2365,var_2364,])
func_2367 = relay.Function([var_2342,var_2364,], output)
mod['func_2367'] = func_2367
mod = relay.transform.InferType()(mod)
var_2368 = relay.var("var_2368", dtype = "float32", shape = (13, 6, 6))#candidate|2368|(13, 6, 6)|var|float32
var_2369 = relay.var("var_2369", dtype = "int16", shape = (182,))#candidate|2369|(182,)|var|int16
output = func_2367(var_2368,var_2369,)
func_2370 = relay.Function([var_2368,var_2369,], output)
mutated_mod['func_2370'] = func_2370
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_319_call = mutated_mod.get_global_var('func_319')
call_2379 = func_318_call()
call_2380 = func_318_call()
output = call_2379
output2 = call_2380
func_2386 = relay.Function([], output)
mod['func_2386'] = func_2386
mod = relay.transform.InferType()(mod)
output = func_2386()
func_2387 = relay.Function([], output)
mutated_mod['func_2387'] = func_2387
mutated_mod = relay.transform.InferType()(mutated_mod)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_2440 = func_203_call()
call_2441 = func_203_call()
func_1584_call = mod.get_global_var('func_1584')
func_1585_call = mutated_mod.get_global_var('func_1585')
call_2452 = relay.TupleGetItem(func_1584_call(), 1)
call_2453 = relay.TupleGetItem(func_1585_call(), 1)
output = relay.Tuple([call_2440,call_2452,])
output2 = relay.Tuple([call_2441,call_2453,])
func_2465 = relay.Function([], output)
mod['func_2465'] = func_2465
mod = relay.transform.InferType()(mod)
output = func_2465()
func_2466 = relay.Function([], output)
mutated_mod['func_2466'] = func_2466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_967_call = mod.get_global_var('func_967')
func_968_call = mutated_mod.get_global_var('func_968')
call_2488 = func_967_call()
call_2489 = func_967_call()
func_1196_call = mod.get_global_var('func_1196')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_2510 = relay.TupleGetItem(func_1196_call(), 0)
call_2511 = relay.TupleGetItem(func_1198_call(), 0)
uop_2518 = relay.cosh(call_2510.astype('float32')) # shape=(14, 13, 1)
uop_2520 = relay.cosh(call_2511.astype('float32')) # shape=(14, 13, 1)
func_459_call = mod.get_global_var('func_459')
func_461_call = mutated_mod.get_global_var('func_461')
const_2528 = relay.const([-9.825002,-5.294153,-3.020281,3.084781,-5.234034,0.649043,9.121651,7.276081,4.474335,-2.042309,-7.498783,-6.803157,6.433648,-1.542175,-8.560056,6.639308,9.240575,-8.341561,5.913591,6.825330,-0.509130,5.690649,1.185154,-2.463313,-2.731200,-9.460411,7.747353,-4.382147,-8.982606,4.621503,3.525090,2.288251,-3.289906,-3.205472,2.522628,2.553625,-4.348993,1.546669,4.508693,-3.394029,-1.995588,2.081081,5.029996,8.050784], dtype = "float64")#candidate|2528|(44,)|const|float64
call_2527 = func_459_call(relay.reshape(const_2528.astype('float64'), [1, 4, 11]))
call_2529 = func_459_call(relay.reshape(const_2528.astype('float64'), [1, 4, 11]))
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_2533 = relay.TupleGetItem(func_759_call(), 0)
call_2534 = relay.TupleGetItem(func_761_call(), 0)
func_1196_call = mod.get_global_var('func_1196')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_2535 = relay.TupleGetItem(func_1196_call(), 1)
call_2536 = relay.TupleGetItem(func_1198_call(), 1)
output = relay.Tuple([call_2488,uop_2518,call_2527,const_2528,call_2533,call_2535,])
output2 = relay.Tuple([call_2489,uop_2520,call_2529,const_2528,call_2534,call_2536,])
func_2545 = relay.Function([], output)
mod['func_2545'] = func_2545
mod = relay.transform.InferType()(mod)
output = func_2545()
func_2546 = relay.Function([], output)
mutated_mod['func_2546'] = func_2546
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2098_call = mod.get_global_var('func_2098')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_2547 = relay.TupleGetItem(func_2098_call(), 0)
call_2548 = relay.TupleGetItem(func_2099_call(), 0)
uop_2549 = relay.rsqrt(call_2547.astype('float32')) # shape=(7, 10, 2)
uop_2551 = relay.rsqrt(call_2548.astype('float32')) # shape=(7, 10, 2)
output = relay.Tuple([uop_2549,])
output2 = relay.Tuple([uop_2551,])
func_2552 = relay.Function([], output)
mod['func_2552'] = func_2552
mod = relay.transform.InferType()(mod)
output = func_2552()
func_2553 = relay.Function([], output)
mutated_mod['func_2553'] = func_2553
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2622 = relay.const([[[6.254261,5.592192,-3.390090,-4.068011,8.018275,3.352739,6.754301,9.625577,-6.372437],[2.723216,-9.088988,-3.032054,-9.060425,-4.498118,-1.468139,-5.055148,4.639615,-2.665466],[-0.236869,-1.017188,2.523616,-3.879560,-8.822191,9.034402,-1.022308,9.701388,-7.598077],[-2.955258,5.019529,-1.769011,-8.737723,3.413998,-5.958613,9.810333,6.772032,-1.784224],[-5.313786,8.978475,8.001358,5.482975,9.355022,-0.861353,-2.163393,-0.053847,9.859483],[7.101460,8.438714,-8.413577,-5.543632,-4.148814,1.075226,-0.477706,-6.303705,-0.931073],[-5.116166,8.646130,0.752920,1.695056,-3.829811,0.762949,-1.605158,8.079628,1.210635],[-6.235444,-7.515436,2.490883,3.566999,3.360326,6.806933,1.263121,8.293805,-3.891493]],[[6.115148,-1.244083,8.318721,0.577353,-3.986045,-4.728070,-1.801550,-4.363477,4.437290],[-2.193297,9.256438,-1.938224,-9.916816,7.183031,8.321334,-9.112371,8.103326,-0.150227],[-3.650593,6.259007,4.899264,-1.019167,-5.148135,-7.397287,8.900870,-6.452032,-6.656603],[1.659080,6.081023,-8.697665,-7.016330,8.536307,7.962367,5.898375,3.134170,-8.276128],[-7.446128,7.459967,3.937390,-2.316666,-2.463666,-0.336129,-2.155506,7.526047,-7.182062],[-2.193171,-4.801818,-6.230365,8.703938,8.404157,-5.359641,1.607023,4.444218,7.795238],[-1.889885,6.841459,2.705826,0.735346,3.209155,4.996493,-8.294481,1.574114,6.137132],[-2.862689,5.633960,8.523276,-3.771842,-3.266527,6.296444,-0.662517,5.236318,7.108137]],[[2.328881,-3.563990,0.734469,-4.891484,0.730069,0.434483,-2.837691,-4.888278,6.214817],[1.021002,-3.431362,9.247319,-0.111211,-6.169612,4.006439,-1.879708,-2.593958,-3.530309],[-6.774374,-6.226291,-1.663129,-2.676460,1.099711,-0.938976,-2.286317,-3.860509,8.163245],[7.652588,-8.657744,0.153752,9.381968,-4.820191,9.189560,2.174826,-5.090909,2.996349],[9.774041,8.025066,-9.352183,-9.757953,2.638398,-0.550472,-7.825181,-0.861737,2.832117],[4.020788,8.889802,-3.740508,-6.252751,-6.698418,3.248200,8.726134,3.948171,-7.646207],[-6.153694,5.249954,9.850457,-5.667966,4.058837,-2.071512,-2.133460,8.014982,-2.976713],[-2.502188,2.329170,5.481896,2.930545,-5.547984,7.122153,-9.980137,0.235847,1.174169]],[[7.542258,-7.095878,2.242121,5.225691,-5.221420,2.440730,1.168107,3.130172,2.637874],[7.239872,0.262154,8.810702,-8.255002,-0.594342,1.906989,8.411326,9.579518,6.383273],[-3.098209,8.321391,6.455944,4.165612,-4.288061,-5.670017,5.354348,-8.765887,1.086984],[2.318297,-9.499454,6.728646,-9.695838,-7.784733,-8.161082,-5.165012,5.135065,-1.436747],[-5.218552,7.192559,-9.125163,-5.910328,2.763228,3.486987,2.070559,6.863659,-5.779598],[6.491317,9.607205,2.184893,-6.338743,-1.773089,0.815576,-9.544165,7.177426,-1.719507],[2.605486,8.061992,-7.463970,8.092641,-0.478894,7.458106,0.184160,4.321495,-5.364247],[5.854352,-0.614488,-1.623079,-5.249760,6.234870,-4.832739,6.394632,3.104388,5.334884]]], dtype = "float32")#candidate|2622|(4, 8, 9)|const|float32
uop_2623 = relay.atanh(const_2622.astype('float32')) # shape=(4, 8, 9)
bop_2625 = relay.floor_mod(uop_2623.astype('float64'), relay.reshape(const_2622.astype('float64'), relay.shape_of(uop_2623))) # shape=(4, 8, 9)
output = bop_2625
output2 = bop_2625
func_2635 = relay.Function([], output)
mod['func_2635'] = func_2635
mod = relay.transform.InferType()(mod)
output = func_2635()
func_2636 = relay.Function([], output)
mutated_mod['func_2636'] = func_2636
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2647 = relay.var("var_2647", dtype = "bool", shape = (15, 6, 7))#candidate|2647|(15, 6, 7)|var|bool
var_2648 = relay.var("var_2648", dtype = "bool", shape = (15, 6, 7))#candidate|2648|(15, 6, 7)|var|bool
bop_2649 = relay.logical_or(var_2647.astype('bool'), relay.reshape(var_2648.astype('bool'), relay.shape_of(var_2647))) # shape=(15, 6, 7)
output = relay.Tuple([bop_2649,])
output2 = relay.Tuple([bop_2649,])
func_2657 = relay.Function([var_2647,var_2648,], output)
mod['func_2657'] = func_2657
mod = relay.transform.InferType()(mod)
mutated_mod['func_2657'] = func_2657
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2657_call = mutated_mod.get_global_var('func_2657')
var_2659 = relay.var("var_2659", dtype = "bool", shape = (15, 6, 7))#candidate|2659|(15, 6, 7)|var|bool
var_2660 = relay.var("var_2660", dtype = "bool", shape = (15, 6, 7))#candidate|2660|(15, 6, 7)|var|bool
call_2658 = func_2657_call(var_2659,var_2660,)
output = call_2658
func_2661 = relay.Function([var_2659,var_2660,], output)
mutated_mod['func_2661'] = func_2661
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2693 = relay.var("var_2693", dtype = "float64", shape = (13, 12, 1))#candidate|2693|(13, 12, 1)|var|float64
const_2694 = relay.const([[[-7.805720,3.325873,-1.057465],[9.199079,8.271653,-7.393053],[-8.725167,2.680269,-5.402307],[8.010950,-9.233694,-4.711264],[2.971453,2.920733,-3.782907],[-4.889992,-5.751481,2.248297],[-0.347797,6.345320,-6.237805],[5.825379,-1.872720,-3.755801],[-5.833799,-2.276565,8.557051],[-9.402141,-3.832839,2.911074],[1.596920,9.563259,-8.197502],[-6.856612,-9.410934,-7.537736]],[[2.920948,2.119986,-6.620518],[5.577879,7.220320,4.309911],[-2.690886,0.967594,1.065152],[7.283505,-5.113045,-4.754496],[-1.865377,6.287836,-9.797924],[8.031973,0.479520,2.912856],[-0.427122,-3.973096,7.509755],[-4.468328,-9.961481,-9.170734],[5.473168,-9.907743,-5.344454],[-0.079224,1.013903,7.059247],[3.012946,8.543386,0.876777],[-5.091965,2.854099,-0.299507]],[[-6.621177,-6.074146,-9.390044],[-7.930117,1.559483,-3.025412],[1.820625,-8.709132,-5.268957],[0.718523,-9.353870,8.730888],[8.272386,8.554613,-4.427695],[3.951588,-7.761965,8.224781],[-3.479198,-6.000302,-4.296855],[-5.424634,0.916235,-0.135977],[-2.304949,0.027148,5.698613],[4.005449,-4.708362,2.388288],[-2.813270,2.715329,1.828351],[3.572392,-7.195557,6.232874]],[[-0.944298,0.304341,-7.622955],[-5.263294,0.598218,2.114104],[-8.422626,4.330773,0.274092],[0.162042,-1.282421,-9.316808],[-7.208396,6.440350,-9.466861],[5.186597,-8.709540,-3.558851],[5.829699,-0.329008,6.487670],[0.815698,-7.662273,-2.878916],[4.996156,1.296171,6.013875],[5.909702,7.020210,-2.470495],[3.919596,2.725942,-3.712291],[-9.689021,-9.677002,-0.147363]],[[-7.754690,6.977152,7.007807],[-0.188303,0.680342,-8.012121],[-2.407933,-3.809758,-5.719259],[6.472918,9.971199,-0.730058],[-1.416151,8.147092,4.835579],[-1.954575,7.105688,-0.413365],[-5.870512,8.174576,-8.077112],[-5.323554,-4.661212,-0.529002],[1.156854,-6.424959,-3.449495],[6.125807,-5.988625,3.298505],[-5.202260,2.749170,0.095012],[-2.931764,8.611870,-8.167587]],[[2.542835,-1.624224,1.349910],[5.377134,-2.575231,3.652572],[-6.831167,5.744977,7.880017],[-3.663543,1.701089,7.062298],[4.084692,-8.203163,-5.909342],[-1.648840,3.969225,5.693121],[6.643691,4.471020,-9.774998],[4.719549,2.538949,4.119054],[7.947434,2.562066,-7.173355],[-0.927618,-2.112877,-3.064974],[1.243116,0.075970,1.547053],[7.656880,9.973333,-0.625221]],[[-3.556471,-4.328396,-9.741522],[-9.454476,2.466917,-0.105189],[4.196791,8.546405,5.266962],[-0.057246,-3.485623,5.465848],[-0.018648,-6.939987,-3.342345],[8.286865,-8.917640,-4.583016],[-5.614312,7.707715,-9.611407],[3.215450,-0.256431,-0.293072],[-8.902441,-9.824973,-1.255819],[-7.975070,-6.747524,-6.182940],[5.478248,2.545377,7.106738],[-4.242826,4.190969,2.546272]],[[-5.753780,3.775434,0.994784],[-7.013444,-8.996950,-5.679256],[6.986598,9.982992,9.966434],[-4.395362,3.410997,0.037960],[8.020931,-8.402573,9.323400],[7.247856,-9.417536,-9.661532],[-4.070673,3.524903,0.115348],[8.279677,-1.652932,-2.716222],[-5.353042,-3.074925,2.725705],[-8.082668,-1.094033,7.089004],[-2.384502,6.856197,7.654991],[-1.323968,-3.164287,-5.463383]],[[0.873810,-8.744424,-9.452922],[1.582111,7.252821,-2.305825],[7.229056,-4.898444,-8.138826],[3.699545,-7.439849,4.942390],[-1.694805,3.213838,-3.100659],[-3.123710,0.077228,9.705706],[-4.332352,-0.826384,7.917463],[-4.435715,0.052391,-5.148907],[-6.212636,-3.630197,-1.381390],[-0.554902,5.061450,1.151176],[2.543867,7.487685,0.888008],[-8.779471,3.658975,3.891040]],[[4.674778,-0.540229,-1.310693],[-4.189280,-3.636953,8.125425],[9.537324,-1.657001,6.609867],[-5.083490,3.324020,6.501559],[-5.116233,-8.417952,-2.973818],[-4.680536,2.964227,-2.299300],[2.602685,-7.782082,8.350976],[-1.484899,8.940340,0.193617],[4.141195,1.881831,5.088226],[7.373323,-5.497947,-2.196398],[5.853783,3.879212,6.846273],[1.889797,-8.113344,-7.829213]],[[8.389604,-9.213819,1.992196],[-9.681236,6.929681,-1.955861],[-6.286395,7.850768,0.067365],[-1.793397,-2.955713,-8.724689],[1.221230,9.319294,7.598364],[-2.126710,-5.702456,-9.177284],[-0.140138,-6.730908,-6.532465],[0.360580,-1.771605,-4.683167],[-1.216288,1.798517,-9.140731],[-2.811639,0.937878,3.942227],[2.210989,5.461181,6.106452],[-7.439319,-3.920741,0.561226]],[[8.061516,-7.233377,9.452582],[8.242563,7.669647,8.858874],[-7.400037,4.276408,3.174698],[3.073470,-2.019538,-1.010784],[-6.835920,-7.767406,-1.934030],[2.592401,-1.935004,9.086811],[-6.787301,2.699601,5.736022],[1.361311,-3.443706,5.612735],[-2.624263,-4.399821,-3.654416],[-6.130087,9.625523,0.492175],[-1.005815,2.258673,-0.568037],[4.735335,-0.189351,-1.849144]],[[3.825871,0.495814,2.895752],[4.352869,6.832973,-0.302593],[-4.384883,-0.528313,6.351752],[4.693325,6.664991,-4.994401],[-9.517795,-4.419471,-9.610583],[-1.192503,1.364810,3.290734],[2.946958,-9.111862,7.632949],[-4.808745,0.666847,4.721091],[-9.033328,-2.680387,-9.056982],[-0.114954,-3.315262,0.400982],[2.730396,-0.637875,1.403039],[0.732970,-9.805606,-7.198872]]], dtype = "float64")#candidate|2694|(13, 12, 3)|const|float64
bop_2695 = relay.less(var_2693.astype('bool'), const_2694.astype('bool')) # shape=(13, 12, 3)
output = bop_2695
output2 = bop_2695
func_2698 = relay.Function([var_2693,], output)
mod['func_2698'] = func_2698
mod = relay.transform.InferType()(mod)
mutated_mod['func_2698'] = func_2698
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2699 = relay.var("var_2699", dtype = "float64", shape = (13, 12, 1))#candidate|2699|(13, 12, 1)|var|float64
func_2698_call = mutated_mod.get_global_var('func_2698')
call_2700 = func_2698_call(var_2699)
output = call_2700
func_2701 = relay.Function([var_2699], output)
mutated_mod['func_2701'] = func_2701
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2465_call = mod.get_global_var('func_2465')
func_2466_call = mutated_mod.get_global_var('func_2466')
call_2726 = relay.TupleGetItem(func_2465_call(), 0)
call_2727 = relay.TupleGetItem(func_2466_call(), 0)
func_2635_call = mod.get_global_var('func_2635')
func_2636_call = mutated_mod.get_global_var('func_2636')
call_2731 = func_2635_call()
call_2732 = func_2635_call()
output = relay.Tuple([call_2726,call_2731,])
output2 = relay.Tuple([call_2727,call_2732,])
func_2733 = relay.Function([], output)
mod['func_2733'] = func_2733
mod = relay.transform.InferType()(mod)
mutated_mod['func_2733'] = func_2733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mutated_mod.get_global_var('func_2733')
call_2734 = func_2733_call()
output = call_2734
func_2735 = relay.Function([], output)
mutated_mod['func_2735'] = func_2735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_2834 = relay.TupleGetItem(func_1986_call(), 2)
call_2835 = relay.TupleGetItem(func_1988_call(), 2)
output = call_2834
output2 = call_2835
func_2836 = relay.Function([], output)
mod['func_2836'] = func_2836
mod = relay.transform.InferType()(mod)
mutated_mod['func_2836'] = func_2836
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mutated_mod.get_global_var('func_2836')
call_2837 = func_2836_call()
output = call_2837
func_2838 = relay.Function([], output)
mutated_mod['func_2838'] = func_2838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_318_call = mod.get_global_var('func_318')
func_319_call = mutated_mod.get_global_var('func_319')
call_2851 = func_318_call()
call_2852 = func_318_call()
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_2853 = relay.TupleGetItem(func_1629_call(), 0)
call_2854 = relay.TupleGetItem(func_1631_call(), 0)
func_2098_call = mod.get_global_var('func_2098')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_2864 = relay.TupleGetItem(func_2098_call(), 0)
call_2865 = relay.TupleGetItem(func_2099_call(), 0)
uop_2887 = relay.erf(call_2853.astype('float64')) # shape=(7, 10, 2)
uop_2889 = relay.erf(call_2854.astype('float64')) # shape=(7, 10, 2)
var_2892 = relay.var("var_2892", dtype = "float64", shape = (7, 10, 2))#candidate|2892|(7, 10, 2)|var|float64
bop_2893 = relay.less_equal(call_2853.astype('bool'), relay.reshape(var_2892.astype('bool'), relay.shape_of(call_2853))) # shape=(7, 10, 2)
bop_2896 = relay.less_equal(call_2854.astype('bool'), relay.reshape(var_2892.astype('bool'), relay.shape_of(call_2854))) # shape=(7, 10, 2)
func_2733_call = mod.get_global_var('func_2733')
func_2735_call = mutated_mod.get_global_var('func_2735')
call_2898 = relay.TupleGetItem(func_2733_call(), 0)
call_2899 = relay.TupleGetItem(func_2735_call(), 0)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_2903 = func_1416_call()
call_2904 = func_1416_call()
func_2098_call = mod.get_global_var('func_2098')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_2907 = relay.TupleGetItem(func_2098_call(), 0)
call_2908 = relay.TupleGetItem(func_2099_call(), 0)
func_1409_call = mod.get_global_var('func_1409')
func_1410_call = mutated_mod.get_global_var('func_1410')
call_2916 = relay.TupleGetItem(func_1409_call(), 2)
call_2917 = relay.TupleGetItem(func_1410_call(), 2)
func_2836_call = mod.get_global_var('func_2836')
func_2838_call = mutated_mod.get_global_var('func_2838')
call_2925 = func_2836_call()
call_2926 = func_2836_call()
output = relay.Tuple([call_2851,call_2864,uop_2887,bop_2893,call_2898,call_2903,call_2907,call_2916,call_2925,])
output2 = relay.Tuple([call_2852,call_2865,uop_2889,bop_2896,call_2899,call_2904,call_2908,call_2917,call_2926,])
func_2934 = relay.Function([var_2892,], output)
mod['func_2934'] = func_2934
mod = relay.transform.InferType()(mod)
var_2935 = relay.var("var_2935", dtype = "float64", shape = (7, 10, 2))#candidate|2935|(7, 10, 2)|var|float64
output = func_2934(var_2935)
func_2936 = relay.Function([var_2935], output)
mutated_mod['func_2936'] = func_2936
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mod.get_global_var('func_2733')
func_2735_call = mutated_mod.get_global_var('func_2735')
call_2942 = relay.TupleGetItem(func_2733_call(), 1)
call_2943 = relay.TupleGetItem(func_2735_call(), 1)
output = relay.Tuple([call_2942,])
output2 = relay.Tuple([call_2943,])
func_2959 = relay.Function([], output)
mod['func_2959'] = func_2959
mod = relay.transform.InferType()(mod)
output = func_2959()
func_2960 = relay.Function([], output)
mutated_mod['func_2960'] = func_2960
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1703_call = mod.get_global_var('func_1703')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_2990 = func_1703_call()
call_2991 = func_1703_call()
output = call_2990
output2 = call_2991
func_2995 = relay.Function([], output)
mod['func_2995'] = func_2995
mod = relay.transform.InferType()(mod)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mutated_mod.get_global_var('func_2995')
call_2996 = func_2995_call()
output = call_2996
func_2997 = relay.Function([], output)
mutated_mod['func_2997'] = func_2997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1507_call = mod.get_global_var('func_1507')
func_1508_call = mutated_mod.get_global_var('func_1508')
call_3001 = func_1507_call()
call_3002 = func_1507_call()
func_318_call = mod.get_global_var('func_318')
func_319_call = mutated_mod.get_global_var('func_319')
call_3036 = func_318_call()
call_3037 = func_318_call()
output = relay.Tuple([call_3001,call_3036,])
output2 = relay.Tuple([call_3002,call_3037,])
func_3041 = relay.Function([], output)
mod['func_3041'] = func_3041
mod = relay.transform.InferType()(mod)
output = func_3041()
func_3042 = relay.Function([], output)
mutated_mod['func_3042'] = func_3042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3051 = relay.var("var_3051", dtype = "float64", shape = (3, 12, 10))#candidate|3051|(3, 12, 10)|var|float64
uop_3052 = relay.exp(var_3051.astype('float64')) # shape=(3, 12, 10)
func_1639_call = mod.get_global_var('func_1639')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_3060 = relay.TupleGetItem(func_1639_call(), 0)
call_3061 = relay.TupleGetItem(func_1640_call(), 0)
uop_3062 = relay.erf(uop_3052.astype('float32')) # shape=(3, 12, 10)
uop_3071 = relay.asinh(uop_3052.astype('float64')) # shape=(3, 12, 10)
uop_3077 = relay.sin(uop_3071.astype('float32')) # shape=(3, 12, 10)
bop_3081 = relay.divide(var_3051.astype('float64'), relay.reshape(uop_3052.astype('float64'), relay.shape_of(var_3051))) # shape=(3, 12, 10)
output = relay.Tuple([call_3060,uop_3062,uop_3077,bop_3081,])
output2 = relay.Tuple([call_3061,uop_3062,uop_3077,bop_3081,])
func_3089 = relay.Function([var_3051,], output)
mod['func_3089'] = func_3089
mod = relay.transform.InferType()(mod)
mutated_mod['func_3089'] = func_3089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3090 = relay.var("var_3090", dtype = "float64", shape = (3, 12, 10))#candidate|3090|(3, 12, 10)|var|float64
func_3089_call = mutated_mod.get_global_var('func_3089')
call_3091 = func_3089_call(var_3090)
output = call_3091
func_3092 = relay.Function([var_3090], output)
mutated_mod['func_3092'] = func_3092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3120 = relay.var("var_3120", dtype = "float64", shape = (1, 7, 15))#candidate|3120|(1, 7, 15)|var|float64
var_3121 = relay.var("var_3121", dtype = "float64", shape = (14, 7, 15))#candidate|3121|(14, 7, 15)|var|float64
bop_3122 = relay.floor_divide(var_3120.astype('float64'), var_3121.astype('float64')) # shape=(14, 7, 15)
output = bop_3122
output2 = bop_3122
func_3139 = relay.Function([var_3120,var_3121,], output)
mod['func_3139'] = func_3139
mod = relay.transform.InferType()(mod)
var_3140 = relay.var("var_3140", dtype = "float64", shape = (1, 7, 15))#candidate|3140|(1, 7, 15)|var|float64
var_3141 = relay.var("var_3141", dtype = "float64", shape = (14, 7, 15))#candidate|3141|(14, 7, 15)|var|float64
output = func_3139(var_3140,var_3141,)
func_3142 = relay.Function([var_3140,var_3141,], output)
mutated_mod['func_3142'] = func_3142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1703_call = mod.get_global_var('func_1703')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_3155 = func_1703_call()
call_3156 = func_1703_call()
var_3159 = relay.var("var_3159", dtype = "float64", shape = (7, 10, 2))#candidate|3159|(7, 10, 2)|var|float64
bop_3160 = relay.divide(call_3155.astype('float64'), relay.reshape(var_3159.astype('float64'), relay.shape_of(call_3155))) # shape=(7, 10, 2)
bop_3163 = relay.divide(call_3156.astype('float64'), relay.reshape(var_3159.astype('float64'), relay.shape_of(call_3156))) # shape=(7, 10, 2)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_3184 = relay.TupleGetItem(func_1629_call(), 0)
call_3185 = relay.TupleGetItem(func_1631_call(), 0)
output = relay.Tuple([bop_3160,call_3184,])
output2 = relay.Tuple([bop_3163,call_3185,])
func_3198 = relay.Function([var_3159,], output)
mod['func_3198'] = func_3198
mod = relay.transform.InferType()(mod)
mutated_mod['func_3198'] = func_3198
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3199 = relay.var("var_3199", dtype = "float64", shape = (7, 10, 2))#candidate|3199|(7, 10, 2)|var|float64
func_3198_call = mutated_mod.get_global_var('func_3198')
call_3200 = func_3198_call(var_3199)
output = call_3200
func_3201 = relay.Function([var_3199], output)
mutated_mod['func_3201'] = func_3201
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1409_call = mod.get_global_var('func_1409')
func_1410_call = mutated_mod.get_global_var('func_1410')
call_3218 = relay.TupleGetItem(func_1409_call(), 0)
call_3219 = relay.TupleGetItem(func_1410_call(), 0)
output = relay.Tuple([call_3218,])
output2 = relay.Tuple([call_3219,])
func_3247 = relay.Function([], output)
mod['func_3247'] = func_3247
mod = relay.transform.InferType()(mod)
mutated_mod['func_3247'] = func_3247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3247_call = mutated_mod.get_global_var('func_3247')
call_3248 = func_3247_call()
output = call_3248
func_3249 = relay.Function([], output)
mutated_mod['func_3249'] = func_3249
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mod.get_global_var('func_2995')
func_2997_call = mutated_mod.get_global_var('func_2997')
call_3250 = func_2995_call()
call_3251 = func_2995_call()
output = relay.Tuple([call_3250,])
output2 = relay.Tuple([call_3251,])
func_3256 = relay.Function([], output)
mod['func_3256'] = func_3256
mod = relay.transform.InferType()(mod)
output = func_3256()
func_3257 = relay.Function([], output)
mutated_mod['func_3257'] = func_3257
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_3273 = relay.TupleGetItem(func_2198_call(), 0)
call_3274 = relay.TupleGetItem(func_2200_call(), 0)
uop_3277 = relay.tan(call_3273.astype('float32')) # shape=(7, 10, 2)
uop_3279 = relay.tan(call_3274.astype('float32')) # shape=(7, 10, 2)
func_2098_call = mod.get_global_var('func_2098')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_3289 = relay.TupleGetItem(func_2098_call(), 0)
call_3290 = relay.TupleGetItem(func_2099_call(), 0)
output = relay.Tuple([uop_3277,call_3289,])
output2 = relay.Tuple([uop_3279,call_3290,])
func_3291 = relay.Function([], output)
mod['func_3291'] = func_3291
mod = relay.transform.InferType()(mod)
mutated_mod['func_3291'] = func_3291
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3291_call = mutated_mod.get_global_var('func_3291')
call_3292 = func_3291_call()
output = call_3292
func_3293 = relay.Function([], output)
mutated_mod['func_3293'] = func_3293
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2465_call = mod.get_global_var('func_2465')
func_2466_call = mutated_mod.get_global_var('func_2466')
call_3320 = relay.TupleGetItem(func_2465_call(), 0)
call_3321 = relay.TupleGetItem(func_2466_call(), 0)
func_967_call = mod.get_global_var('func_967')
func_968_call = mutated_mod.get_global_var('func_968')
call_3326 = func_967_call()
call_3327 = func_967_call()
output = relay.Tuple([call_3320,call_3326,])
output2 = relay.Tuple([call_3321,call_3327,])
func_3338 = relay.Function([], output)
mod['func_3338'] = func_3338
mod = relay.transform.InferType()(mod)
mutated_mod['func_3338'] = func_3338
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3338_call = mutated_mod.get_global_var('func_3338')
call_3339 = func_3338_call()
output = call_3339
func_3340 = relay.Function([], output)
mutated_mod['func_3340'] = func_3340
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3391 = relay.var("var_3391", dtype = "int64", shape = (16, 1, 16))#candidate|3391|(16, 1, 16)|var|int64
var_3392 = relay.var("var_3392", dtype = "int64", shape = (16, 2, 16))#candidate|3392|(16, 2, 16)|var|int64
bop_3393 = relay.logical_xor(var_3391.astype('int64'), var_3392.astype('int64')) # shape=(16, 2, 16)
func_967_call = mod.get_global_var('func_967')
func_968_call = mutated_mod.get_global_var('func_968')
call_3399 = func_967_call()
call_3400 = func_967_call()
output = relay.Tuple([bop_3393,call_3399,])
output2 = relay.Tuple([bop_3393,call_3400,])
func_3405 = relay.Function([var_3391,var_3392,], output)
mod['func_3405'] = func_3405
mod = relay.transform.InferType()(mod)
var_3406 = relay.var("var_3406", dtype = "int64", shape = (16, 1, 16))#candidate|3406|(16, 1, 16)|var|int64
var_3407 = relay.var("var_3407", dtype = "int64", shape = (16, 2, 16))#candidate|3407|(16, 2, 16)|var|int64
output = func_3405(var_3406,var_3407,)
func_3408 = relay.Function([var_3406,var_3407,], output)
mutated_mod['func_3408'] = func_3408
mutated_mod = relay.transform.InferType()(mutated_mod)
func_696_call = mod.get_global_var('func_696')
func_697_call = mutated_mod.get_global_var('func_697')
call_3426 = relay.TupleGetItem(func_696_call(), 0)
call_3427 = relay.TupleGetItem(func_697_call(), 0)
func_1001_call = mod.get_global_var('func_1001')
func_1003_call = mutated_mod.get_global_var('func_1003')
var_3431 = relay.var("var_3431", dtype = "float32", shape = (108,))#candidate|3431|(108,)|var|float32
call_3430 = func_1001_call(relay.reshape(var_3431.astype('float32'), [9, 12, 1]))
call_3432 = func_1001_call(relay.reshape(var_3431.astype('float32'), [9, 12, 1]))
uop_3433 = relay.log(call_3430.astype('float32')) # shape=(9, 12, 1)
uop_3435 = relay.log(call_3432.astype('float32')) # shape=(9, 12, 1)
func_1125_call = mod.get_global_var('func_1125')
func_1127_call = mutated_mod.get_global_var('func_1127')
const_3438 = relay.const([[6.143916,-7.232444],[-4.927285,6.879620],[3.081753,8.467627],[-7.853503,-4.536380],[-4.887601,-0.560477],[-5.942699,-7.562394],[-0.320404,-5.902749],[3.799659,2.242347],[-6.038733,0.508209],[-3.407627,8.081956],[6.391536,9.440892],[5.759404,-3.217594],[8.169486,2.623006],[1.384551,8.702927],[6.154147,-1.960148],[3.105309,9.444309],[4.191217,-0.556771],[-3.101926,1.656502],[4.993796,8.219919],[2.747431,-9.518279],[-3.871489,-8.835073],[1.883221,-3.431377]], dtype = "float64")#candidate|3438|(22, 2)|const|float64
call_3437 = relay.TupleGetItem(func_1125_call(relay.reshape(const_3438.astype('float64'), [44,])), 0)
call_3439 = relay.TupleGetItem(func_1127_call(relay.reshape(const_3438.astype('float64'), [44,])), 0)
output = relay.Tuple([call_3426,var_3431,uop_3433,call_3437,const_3438,])
output2 = relay.Tuple([call_3427,var_3431,uop_3435,call_3439,const_3438,])
func_3443 = relay.Function([var_3431,], output)
mod['func_3443'] = func_3443
mod = relay.transform.InferType()(mod)
mutated_mod['func_3443'] = func_3443
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3444 = relay.var("var_3444", dtype = "float32", shape = (108,))#candidate|3444|(108,)|var|float32
func_3443_call = mutated_mod.get_global_var('func_3443')
call_3445 = func_3443_call(var_3444)
output = call_3445
func_3446 = relay.Function([var_3444], output)
mutated_mod['func_3446'] = func_3446
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2465_call = mod.get_global_var('func_2465')
func_2466_call = mutated_mod.get_global_var('func_2466')
call_3451 = relay.TupleGetItem(func_2465_call(), 1)
call_3452 = relay.TupleGetItem(func_2466_call(), 1)
const_3454 = relay.const([[[4.809749,-0.120908],[0.627039,3.514295],[-3.931658,-6.136263],[-0.854906,4.200016],[1.773058,-5.178457],[-7.671906,-5.523563],[-5.802426,7.232032],[5.306866,-5.867106],[-1.283460,-1.337063],[2.176750,-8.655098]],[[7.288661,-5.578890],[7.187752,-7.511154],[-4.483266,-5.685824],[-8.791701,4.548410],[-3.056806,7.352917],[7.598315,-2.720113],[-0.449608,4.511449],[-3.491990,4.058776],[-0.364184,1.158739],[-8.946561,-9.890251]],[[1.612705,3.318824],[2.647187,-3.113551],[4.818511,-6.797417],[1.261969,-5.980916],[2.869281,9.644309],[5.570952,-7.284030],[-2.361309,8.689634],[6.771807,2.496144],[-2.103249,-1.062398],[1.726558,5.219141]],[[9.301864,3.130818],[-4.773204,-4.286256],[7.335883,5.479206],[5.580414,2.359880],[-4.763405,-6.154547],[-1.300197,-1.416623],[-6.142174,7.118690],[5.558245,-2.407180],[-4.076687,-4.185929],[8.537169,-6.521388]],[[-6.780423,-2.163078],[0.769675,-0.078811],[-2.843573,6.661740],[-8.249311,-4.234157],[8.717963,6.737037],[-9.288441,9.882077],[7.706629,-0.622670],[-8.288404,-8.099404],[-2.500748,-2.423594],[-6.003894,2.266732]],[[5.823480,2.266650],[-3.525004,-6.494286],[4.951815,5.856049],[4.494264,-8.796917],[-1.271294,-4.618148],[-9.851252,8.920018],[3.690644,-0.533216],[-7.707769,-1.363920],[9.697117,-5.094757],[8.643216,8.249619]],[[-7.716581,9.819033],[3.881492,-1.937622],[-7.737497,-0.423311],[2.099271,4.691105],[-7.764775,-8.296922],[-3.505426,-1.444642],[5.673229,2.146401],[-2.185070,7.092868],[3.058304,-9.138791],[6.210541,-6.177166]]], dtype = "float64")#candidate|3454|(7, 10, 2)|const|float64
bop_3455 = relay.floor_divide(call_3451.astype('float64'), relay.reshape(const_3454.astype('float64'), relay.shape_of(call_3451))) # shape=(7, 10, 2)
bop_3458 = relay.floor_divide(call_3452.astype('float64'), relay.reshape(const_3454.astype('float64'), relay.shape_of(call_3452))) # shape=(7, 10, 2)
output = bop_3455
output2 = bop_3458
func_3469 = relay.Function([], output)
mod['func_3469'] = func_3469
mod = relay.transform.InferType()(mod)
output = func_3469()
func_3470 = relay.Function([], output)
mutated_mod['func_3470'] = func_3470
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_3478 = relay.TupleGetItem(func_3291_call(), 0)
call_3479 = relay.TupleGetItem(func_3293_call(), 0)
output = relay.Tuple([call_3478,])
output2 = relay.Tuple([call_3479,])
func_3488 = relay.Function([], output)
mod['func_3488'] = func_3488
mod = relay.transform.InferType()(mod)
mutated_mod['func_3488'] = func_3488
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3488_call = mutated_mod.get_global_var('func_3488')
call_3489 = func_3488_call()
output = call_3489
func_3490 = relay.Function([], output)
mutated_mod['func_3490'] = func_3490
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_942_call = mutated_mod.get_global_var('func_942')
call_3565 = relay.TupleGetItem(func_941_call(), 0)
call_3566 = relay.TupleGetItem(func_942_call(), 0)
var_3572 = relay.var("var_3572", dtype = "float64", shape = (7, 10, 2))#candidate|3572|(7, 10, 2)|var|float64
bop_3573 = relay.mod(call_3565.astype('float64'), relay.reshape(var_3572.astype('float64'), relay.shape_of(call_3565))) # shape=(7, 10, 2)
bop_3576 = relay.mod(call_3566.astype('float64'), relay.reshape(var_3572.astype('float64'), relay.shape_of(call_3566))) # shape=(7, 10, 2)
func_941_call = mod.get_global_var('func_941')
func_942_call = mutated_mod.get_global_var('func_942')
call_3598 = relay.TupleGetItem(func_941_call(), 0)
call_3599 = relay.TupleGetItem(func_942_call(), 0)
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
var_3606 = relay.var("var_3606", dtype = "uint8", shape = (35,))#candidate|3606|(35,)|var|uint8
var_3607 = relay.var("var_3607", dtype = "float64", shape = (44,))#candidate|3607|(44,)|var|float64
call_3605 = relay.TupleGetItem(func_828_call(relay.reshape(var_3606.astype('uint8'), [5, 7]), relay.reshape(var_3606.astype('uint8'), [5, 7]), relay.reshape(var_3607.astype('float64'), [11, 4]), ), 3)
call_3608 = relay.TupleGetItem(func_832_call(relay.reshape(var_3606.astype('uint8'), [5, 7]), relay.reshape(var_3606.astype('uint8'), [5, 7]), relay.reshape(var_3607.astype('float64'), [11, 4]), ), 3)
output = relay.Tuple([bop_3573,call_3598,call_3605,var_3606,var_3607,])
output2 = relay.Tuple([bop_3576,call_3599,call_3608,var_3606,var_3607,])
func_3610 = relay.Function([var_3572,var_3606,var_3607,], output)
mod['func_3610'] = func_3610
mod = relay.transform.InferType()(mod)
var_3611 = relay.var("var_3611", dtype = "float64", shape = (7, 10, 2))#candidate|3611|(7, 10, 2)|var|float64
var_3612 = relay.var("var_3612", dtype = "uint8", shape = (35,))#candidate|3612|(35,)|var|uint8
var_3613 = relay.var("var_3613", dtype = "float64", shape = (44,))#candidate|3613|(44,)|var|float64
output = func_3610(var_3611,var_3612,var_3613,)
func_3614 = relay.Function([var_3611,var_3612,var_3613,], output)
mutated_mod['func_3614'] = func_3614
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3488_call = mod.get_global_var('func_3488')
func_3490_call = mutated_mod.get_global_var('func_3490')
call_3626 = relay.TupleGetItem(func_3488_call(), 0)
call_3627 = relay.TupleGetItem(func_3490_call(), 0)
func_1639_call = mod.get_global_var('func_1639')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_3632 = relay.TupleGetItem(func_1639_call(), 0)
call_3633 = relay.TupleGetItem(func_1640_call(), 0)
func_2552_call = mod.get_global_var('func_2552')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_3636 = relay.TupleGetItem(func_2552_call(), 0)
call_3637 = relay.TupleGetItem(func_2553_call(), 0)
func_3405_call = mod.get_global_var('func_3405')
func_3408_call = mutated_mod.get_global_var('func_3408')
var_3641 = relay.var("var_3641", dtype = "int64", shape = (2, 128))#candidate|3641|(2, 128)|var|int64
var_3642 = relay.var("var_3642", dtype = "int64", shape = (512,))#candidate|3642|(512,)|var|int64
call_3640 = relay.TupleGetItem(func_3405_call(relay.reshape(var_3641.astype('int64'), [16, 1, 16]), relay.reshape(var_3642.astype('int64'), [16, 2, 16]), ), 0)
call_3643 = relay.TupleGetItem(func_3408_call(relay.reshape(var_3641.astype('int64'), [16, 1, 16]), relay.reshape(var_3642.astype('int64'), [16, 2, 16]), ), 0)
output = relay.Tuple([call_3626,call_3632,call_3636,call_3640,var_3641,var_3642,])
output2 = relay.Tuple([call_3627,call_3633,call_3637,call_3643,var_3641,var_3642,])
func_3655 = relay.Function([var_3641,var_3642,], output)
mod['func_3655'] = func_3655
mod = relay.transform.InferType()(mod)
mutated_mod['func_3655'] = func_3655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3655_call = mutated_mod.get_global_var('func_3655')
var_3657 = relay.var("var_3657", dtype = "int64", shape = (2, 128))#candidate|3657|(2, 128)|var|int64
var_3658 = relay.var("var_3658", dtype = "int64", shape = (512,))#candidate|3658|(512,)|var|int64
call_3656 = func_3655_call(var_3657,var_3658,)
output = call_3656
func_3659 = relay.Function([var_3657,var_3658,], output)
mutated_mod['func_3659'] = func_3659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mod.get_global_var('func_2733')
func_2735_call = mutated_mod.get_global_var('func_2735')
call_3669 = relay.TupleGetItem(func_2733_call(), 1)
call_3670 = relay.TupleGetItem(func_2735_call(), 1)
func_2836_call = mod.get_global_var('func_2836')
func_2838_call = mutated_mod.get_global_var('func_2838')
call_3703 = func_2836_call()
call_3704 = func_2836_call()
func_828_call = mod.get_global_var('func_828')
func_832_call = mutated_mod.get_global_var('func_832')
const_3710 = relay.const([-3,-7,4,-3,5,4,-8,7,-3,-5,-4,-2,-7,1,-4,-7,9,-5,-1,2,10,5,-8,9,1,-4,6,-2,-6,6,-3,-7,6,-5,-10], dtype = "uint8")#candidate|3710|(35,)|const|uint8
const_3711 = relay.const([5.505511,2.904655,-8.924478,-4.485143,3.169113,-1.546991,-0.209926,8.492764,7.323535,-8.275108,-2.724227,9.477856,1.884481,-3.968294,-6.801124,-7.909034,4.674099,1.301855,6.559570,1.638630,7.693185,-4.970042,-2.273508,7.105720,-5.305084,-9.637632,3.464038,-7.876837,5.948481,0.930377,6.968828,9.364266,-1.619091,-9.666202,-4.798130,-8.732530,3.538345,-7.061255,8.109799,5.732601,9.431875,-4.813292,9.777404,1.405784], dtype = "float64")#candidate|3711|(44,)|const|float64
call_3709 = relay.TupleGetItem(func_828_call(relay.reshape(const_3710.astype('uint8'), [5, 7]), relay.reshape(const_3710.astype('uint8'), [5, 7]), relay.reshape(const_3711.astype('float64'), [11, 4]), ), 1)
call_3712 = relay.TupleGetItem(func_832_call(relay.reshape(const_3710.astype('uint8'), [5, 7]), relay.reshape(const_3710.astype('uint8'), [5, 7]), relay.reshape(const_3711.astype('float64'), [11, 4]), ), 1)
func_3469_call = mod.get_global_var('func_3469')
func_3470_call = mutated_mod.get_global_var('func_3470')
call_3760 = func_3469_call()
call_3761 = func_3469_call()
output = relay.Tuple([call_3669,call_3703,call_3709,const_3710,const_3711,call_3760,])
output2 = relay.Tuple([call_3670,call_3704,call_3712,const_3710,const_3711,call_3761,])
func_3779 = relay.Function([], output)
mod['func_3779'] = func_3779
mod = relay.transform.InferType()(mod)
mutated_mod['func_3779'] = func_3779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mutated_mod.get_global_var('func_3779')
call_3780 = func_3779_call()
output = call_3780
func_3781 = relay.Function([], output)
mutated_mod['func_3781'] = func_3781
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1050_call = mod.get_global_var('func_1050')
func_1051_call = mutated_mod.get_global_var('func_1051')
call_3799 = relay.TupleGetItem(func_1050_call(), 0)
call_3800 = relay.TupleGetItem(func_1051_call(), 0)
output = call_3799
output2 = call_3800
func_3801 = relay.Function([], output)
mod['func_3801'] = func_3801
mod = relay.transform.InferType()(mod)
mutated_mod['func_3801'] = func_3801
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3801_call = mutated_mod.get_global_var('func_3801')
call_3802 = func_3801_call()
output = call_3802
func_3803 = relay.Function([], output)
mutated_mod['func_3803'] = func_3803
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2160_call = mod.get_global_var('func_2160')
func_2162_call = mutated_mod.get_global_var('func_2162')
call_3806 = func_2160_call()
call_3807 = func_2160_call()
output = relay.Tuple([call_3806,])
output2 = relay.Tuple([call_3807,])
func_3842 = relay.Function([], output)
mod['func_3842'] = func_3842
mod = relay.transform.InferType()(mod)
mutated_mod['func_3842'] = func_3842
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3842_call = mutated_mod.get_global_var('func_3842')
call_3843 = func_3842_call()
output = call_3843
func_3844 = relay.Function([], output)
mutated_mod['func_3844'] = func_3844
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_3861 = func_1416_call()
call_3862 = func_1416_call()
output = call_3861
output2 = call_3862
func_3865 = relay.Function([], output)
mod['func_3865'] = func_3865
mod = relay.transform.InferType()(mod)
mutated_mod['func_3865'] = func_3865
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3865_call = mutated_mod.get_global_var('func_3865')
call_3866 = func_3865_call()
output = call_3866
func_3867 = relay.Function([], output)
mutated_mod['func_3867'] = func_3867
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3338_call = mod.get_global_var('func_3338')
func_3340_call = mutated_mod.get_global_var('func_3340')
call_3879 = relay.TupleGetItem(func_3338_call(), 1)
call_3880 = relay.TupleGetItem(func_3340_call(), 1)
output = call_3879
output2 = call_3880
func_3894 = relay.Function([], output)
mod['func_3894'] = func_3894
mod = relay.transform.InferType()(mod)
output = func_3894()
func_3895 = relay.Function([], output)
mutated_mod['func_3895'] = func_3895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2733_call = mod.get_global_var('func_2733')
func_2735_call = mutated_mod.get_global_var('func_2735')
call_3985 = relay.TupleGetItem(func_2733_call(), 1)
call_3986 = relay.TupleGetItem(func_2735_call(), 1)
output = relay.Tuple([call_3985,])
output2 = relay.Tuple([call_3986,])
func_3992 = relay.Function([], output)
mod['func_3992'] = func_3992
mod = relay.transform.InferType()(mod)
output = func_3992()
func_3993 = relay.Function([], output)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1584_call = mod.get_global_var('func_1584')
func_1585_call = mutated_mod.get_global_var('func_1585')
call_3994 = relay.TupleGetItem(func_1584_call(), 0)
call_3995 = relay.TupleGetItem(func_1585_call(), 0)
output = call_3994
output2 = call_3995
func_4009 = relay.Function([], output)
mod['func_4009'] = func_4009
mod = relay.transform.InferType()(mod)
output = func_4009()
func_4010 = relay.Function([], output)
mutated_mod['func_4010'] = func_4010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_4079 = relay.TupleGetItem(func_3291_call(), 0)
call_4080 = relay.TupleGetItem(func_3293_call(), 0)
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
var_4084 = relay.var("var_4084", dtype = "float64", shape = (7, 15))#candidate|4084|(7, 15)|var|float64
const_4085 = relay.const([-6.501974,-8.696846,3.987388,-2.056790,-0.202162,-4.728347,1.231600,7.299247,-3.969904,1.348887,0.208684,-3.606736,6.743049,-4.001812,7.855429,-4.974682,7.581624,-3.979095,0.170327,0.536030,-6.287421,-6.519066,9.669364,-2.251946,1.384505,-2.667127,9.906325,6.567999,2.186439,-3.744688,3.412196,-7.604286,8.242606,8.166896,4.622262,-6.845719,-4.453643,-1.231667,5.937143,-8.984052,-3.841446,0.290838,6.647998,-8.357287,-2.250659,0.871612,7.039716,2.750434,-6.972342,-5.072470,8.965539,5.811446,8.042895,3.683564,8.445007,-9.256471,-3.517563,3.597407,-6.692630,-9.943943,-9.875155,-1.964990,3.800881,-9.039885,-7.998313,-5.795412,-7.571227,-0.504272,8.563055,-2.207408,2.270496,-5.239560,-1.707876,3.629291,-7.520368,2.965595,-0.450113,-1.361499,4.748336,5.746104,8.039568,0.632391,-4.135135,-2.719344,1.423563,-0.194092,5.185337,-9.796616,-3.991189,-8.120613,5.319785,-7.035468,6.630978,-2.770013,1.125444,-0.086904,3.259495,-6.488236,9.582906,2.921355,0.365926,3.357281,-4.805311,-3.155442,-1.630279,5.896002,9.475530,1.930476,2.357704,8.593477,4.410829,3.218898,-9.711382,-0.882640,-4.449817,-3.676929,9.614482,-0.122345,-9.424460,8.270788,8.229800,-6.608120,-2.672419,2.120870,5.001892,-7.844243,4.547702,4.548338,-8.862615,1.120936,4.638177,-6.694477,-9.151404,1.910816,-4.138469,3.847976,5.221914,-3.664944,7.045505,1.903341,-4.142313,9.832839,-2.451444,4.974731,7.560874,3.384063,3.694377,7.101190,2.795290,-7.253396,0.984041,2.512922,6.273525,-6.553911,-6.943099,-0.627352,-0.810129,-4.105937,-3.226939,2.629809,-7.736502,8.349264,-3.458116,4.347713,1.720460,7.276043,7.713319,1.777850,-0.290206,0.026179,-5.131163,-3.066322,-9.484750,4.664664,-0.763820,-1.262879,3.970274,-6.491638,-7.101339,8.205329,9.193300,6.052742,-1.734292,-3.794717,-7.258177,9.157005,5.725609,5.047663,-3.929755,-1.052667,9.363453,7.870040,-2.883586,3.117338,-6.167866,-2.996086,6.721956,-5.298782,2.186827,5.507119,9.774019,-8.599190,-2.685117,-5.322018,-6.274149,7.233611,3.435785,-4.943144,5.371409,-5.712194,2.024071,5.937904,-5.138922,-1.067846,-6.885567,-3.698852,-7.180876,-9.744636,-0.505527,4.594290,-1.730105,5.792627,1.585017,0.395996,7.182728,-7.144327,7.083679,1.250188,-5.526929,1.252828,1.480612,-4.783838,-5.782335,-0.431832,0.916185,4.225079,7.179405,8.654431,-7.302048,9.397866,-2.443166,-3.590331,3.642745,-3.788790,8.789443,4.239635,6.060102,-6.175695,-8.829852,-5.908096,-2.552230,4.045122,-5.169732,4.547211,-4.671514,-0.568837,-0.034955,-7.201205,6.559091,1.380599,-2.641095,1.309623,-8.662852,7.400190,1.145663,-5.903550,9.509843,7.935372,-2.163222,-5.190225,3.654444,-3.698488,-5.488374,2.235873,8.326234,-2.372785,3.125366,2.575209,-9.472229,3.532017,-5.909052,4.106887,3.224822,-6.524024,3.134555,-0.439481,6.998965,0.932118,0.432654,2.068209,3.324351,-2.827540,-2.972929,7.760543,-0.107943,-3.336679,-7.822567,-2.661443,-1.128442,-0.243019,-1.874124,-4.155431,1.700598,9.567116,-6.961269,5.309739,-5.980168,4.506326,1.447052,0.083868,7.133126,-6.795730,-4.190107,5.894346,9.621048,-6.178459,1.340444,-5.600212,-0.258603,7.671384,-3.918388,4.378382,9.591404,1.093691,9.753738,-3.288203,-3.931880,-6.269377,-8.695697,4.113214,8.106604,7.790646,-3.078391,9.911706,4.923706,-2.732986,8.634885,-6.041677,-6.729265,7.351215,6.449651,-8.198619,9.201438,-2.427486,-5.426765,2.366441,4.594639,-7.734294,-0.493319,4.128727,4.963115,-0.621403,4.858995,7.281414,-3.148439,9.257991,-0.357493,-2.649366,-9.495911,1.601299,-4.465400,8.928277,5.353045,-0.243914,9.800385,6.799262,9.543787,-6.164621,2.325208,-3.992686,-3.912686,7.730076,8.854525,-8.311315,-8.598882,-8.551654,7.009633,-6.643661,-3.260310,-0.884462,-0.160970,-0.062211,0.035660,-4.987674,-0.187517,7.795939,-3.156502,6.661160,-6.647258,-9.079413,-1.730209,2.944690,-3.127513,-7.188797,-4.353155,-0.207531,7.838231,-4.383925,5.862931,0.039888,0.677552,9.446955,8.228190,3.693116,-1.666730,-1.380353,2.695607,-0.846382,4.817442,-8.043053,-6.442776,0.727120,1.744841,-4.659572,-9.426952,-9.599586,-0.937447,-4.462099,-8.312525,6.864586,1.530593,6.218264,-1.917286,-3.620087,5.568736,6.280933,0.721166,0.200523,1.724044,-7.605023,4.452805,9.015073,-5.792634,1.076929,-1.942856,6.584950,-8.471728,-1.952533,7.720423,-1.717830,0.319042,-3.098430,-6.335748,9.896161,4.265864,-7.622901,-1.622575,0.223846,6.371729,6.674994,1.692116,3.856294,-1.829751,-7.274856,-1.166293,-7.553605,2.682742,-2.042464,-3.776712,0.298263,4.723839,-5.100050,0.166029,-3.636149,-7.709680,-8.440390,7.059897,3.865127,0.271222,0.358259,-8.667291,1.332301,-6.140025,-6.434123,5.287029,-1.128068,4.056504,-5.183096,-7.062448,6.007499,8.377843,5.204428,6.463516,-6.162805,-3.225057,-8.454947,5.075815,-3.787934,0.306630,-6.918095,-3.475917,-9.807908,7.142665,0.665270,4.276182,-3.918541,-1.890691,2.066188,-8.711283,8.574964,6.052758,5.137218,4.230029,-8.550354,-9.266786,-0.420715,-3.167085,-0.897350,4.838332,4.960130,-6.352951,2.916081,8.536439,-1.266425,-0.075335,7.343354,1.716133,-3.445633,-0.511035,-8.528732,5.247722,-7.078600,1.126307,2.131687,-8.405893,3.663537,-6.090674,0.350126,-1.621498,0.435835,3.914428,-9.852076,-9.544679,-8.339835,-8.318097,6.591612,6.227692,7.784143,3.766519,8.911250,0.282471,-0.455303,-2.778935,-9.306199,-5.896793,4.432699,-6.492840,-4.943036,8.443069,7.171041,5.846981,2.771235,-5.989568,6.187394,-7.142459,9.882538,-6.706168,4.238448,-8.732512,2.322456,-9.785810,-7.886665,-7.501408,0.221008,1.248706,6.651483,6.790679,7.658384,6.784866,5.602119,-8.633840,-2.261280,4.754807,0.597639,4.644974,-2.160780,4.090771,-6.788671,6.400225,5.589563,-0.730817,-4.279817,-3.308027,-8.203412,-3.064674,6.475736,-4.376703,2.147551,2.129039,9.790510,8.693518,-1.907659,3.282557,7.613960,-8.439335,0.837191,7.411542,3.974650,-9.234335,-2.175635,1.331957,8.254562,3.138713,3.518077,3.605712,9.955476,-3.062733,1.578830,-5.217906,2.204268,-9.048555,8.042526,-9.666319,8.490422,-9.438409,0.604046,9.184675,-7.457393,-5.462078,0.554497,-9.919589,-5.666016,9.595252,-2.532972,-5.615773,-5.313837,2.082061,5.529288,-8.909766,-1.301141,-1.481858,8.622519,-9.304022,-7.174076,1.702734,-9.984758,-4.066975,5.196704,-6.345659,3.236727,5.957672,4.664539,0.420624,-3.472467,2.680315,9.873215,-7.924090,9.869412,-5.875379,6.528465,-9.928544,9.685815,4.072373,-6.067489,7.376990,-5.321443,4.560043,0.430767,-5.403713,8.552238,-6.034620,9.470518,5.603421,7.072282,-8.757731,6.533192,-2.038669,2.147376,9.154187,4.424608,2.605681,5.030497,-8.565780,-3.476299,-3.393088,-5.729799,-9.491387,-5.198411,6.652636,8.052909,-8.678423,-9.631419,7.501500,-4.020387,7.521518,6.033943,-4.129412,6.989227,8.189966,3.891215,5.087946,-3.782333,-8.072582,2.970001,-9.874086,2.224933,-7.725952,6.799733,-6.159007,-8.958073,-7.288336,-5.878455,2.317073,7.706085,4.928297,-6.968326,-1.731237,-4.153471,6.559814,-7.784152,-2.134069,5.803379,6.939767,1.333226,-5.736140,7.654902,3.551605,2.598529,-3.513835,-0.319901,-8.082841,-4.783198,8.279419,3.615949,0.761840,3.235044,5.676198,-3.198530,0.392559,-5.945948,3.444616,-0.574673,-0.996423,1.528655,-8.071019,-7.074730,6.536690,-9.811101,-4.872026,2.491743,7.972441,3.839152,6.641101,-5.519327,4.250324,8.979542,-7.249554,-5.305052,9.832872,8.580462,5.989024,-6.505042,6.634428,3.861661,-3.799904,6.577837,4.138878,0.823758,-4.678917,-6.651378,-9.700336,-5.043268,2.710643,6.441207,7.160683,4.230636,3.819488,4.833715,-6.610643,-4.193925,5.134097,-8.061317,-4.617770,-5.431405,9.988560,3.608104,-3.453078,0.313071,-8.899610,-5.067057,6.484945,-0.702037,-9.030226,7.446010,-0.691929,9.264182,0.241548,1.969754,7.183294,-6.659571,-8.038531,8.657932,-9.964817,-0.971447,4.513546,-3.383123,-8.926884,8.318704,-2.929014,4.687943,-6.693121,-5.569758,3.336669,-0.050330,6.865475,8.770171,-3.723014,-9.440034,4.438958,9.837199,-3.890057,-1.611536,-9.077009,9.527054,-0.828948,8.525670,6.939791,2.243226,9.795090,-0.128608,-6.394928,-7.310059,-8.106007,4.699054,-0.801432,-8.045430,-7.683395,9.189870,0.217521,8.238857,-9.634824,-2.722383,4.104541,-5.703299,4.593432,3.370215,-0.818098,-2.432751,3.839952,6.367176,-0.510685,-6.944355,-6.865063,5.994323,-2.096891,0.951578,-9.659418,-5.991003,7.799034,-9.433410,7.407939,9.781675,-2.465972,-8.811586,2.842620,3.223266,-0.673034,0.682421,6.819276,-9.984387,1.602199,-0.169001,1.270517,5.901300,4.928030,-1.430182,-0.351666,5.968070,6.468935,-5.517096,8.642070,6.319352,9.380221,-0.950263,8.892596,-3.781616,-3.032336,-7.051197,6.050591,0.034308,-5.417382,-8.135839,4.382687,1.382158,3.796758,7.850005,8.061910,-8.136906,0.162178,5.174183,2.627329,-8.801393,4.417801,-5.282579,-3.953367,2.211336,3.984298,4.084884,0.951903,7.692350,-4.379766,1.040108,0.403565,-9.224359,-7.539585,-7.564910,4.691095,-1.024297,0.300251,-3.674351,-6.724070,-5.642388,3.553841,-3.831732,-7.453676,3.992513,-6.587336,-5.728162,2.263803,8.867085,7.678147,6.368069,-4.424839,8.928352,-1.139118,8.100818,6.549682,-4.500276,-5.076524,-0.683021,5.398039,6.956417,-8.357465,4.364787,2.882062,-7.213558,-7.526139,0.918718,6.997231,7.689146,-0.536965,-5.010821,-9.770259,-6.963165,7.785992,-6.600524,5.568972,-2.113853,3.635690,9.435242,-7.043178,0.254925,7.793112,1.620420,8.947795,1.812410,-1.777371,-5.559800,-5.918588,4.358858,7.152809,-9.599482,4.077118,-4.960553,0.973351,0.527858,1.993799,-4.517798,-1.754652,8.475774,-1.993743,6.785596,-8.316037,-4.127800,7.404963,-4.182812,8.343544,7.315780,-4.973166,3.768022,1.048511,6.165296,-2.753388,3.583624,-1.710246,-0.811062,0.691796,0.248079,7.439732,2.989490,4.355826,0.035541,-9.915058,2.771384,2.323216,-8.292038,-8.992280,8.078534,-0.302950,6.202037,-1.609783,9.406142,7.354582,1.444350,-1.216301,1.314150,8.439210,-6.763453,9.236138,-3.590021,4.328510,6.937825,-4.000437,-1.958701,-8.725416,2.894029,6.330288,-7.725134,7.383184,-6.161855,-8.485703,3.745172,-5.241553,-8.649207,-0.038123,-9.830518,8.117620,6.526522,6.246225,-5.296920,9.218732,-6.515539,3.361979,0.469346,-5.763798,-0.554276,-6.871847,-0.213992,-2.301549,-4.387071,1.782970,-5.996152,9.258590,1.007576,2.301849,-2.162089,0.495676,5.140759,0.471575,-6.773420,-7.705547,8.459719,-4.774434,-8.429397,-7.004413,4.890058,5.075049,-1.077430,5.744261,7.363563,-8.470088,1.122915,-7.443215,-9.531060,-1.639639,-9.050842,1.024738,9.995149,0.627116,-0.916578,-5.117043,-9.368368,0.978413,-1.374255,-6.620858,4.747021,6.564226,-3.077317,-2.414561,-8.186218,6.974476,2.584100,-2.714547,9.178167,-0.364401,2.136504,6.925584,6.127308,-9.828764,-0.885370,2.022674,7.302096,-1.661322,8.153195,-4.116237,7.024755,-0.881575,6.658464,2.095252,-5.512637,-1.511374,0.686111,1.880947,0.269122,-9.176710,-3.992922,3.214641,9.532594,-7.063012,-1.202464,-2.770732,-8.049296,3.693820,1.211367,-4.963476,-5.756021,2.873140,3.651354,-5.022693,-1.335994,-9.745679,9.647188,3.401033,1.109598,9.664230,-0.864458,-8.257902,-5.925591,-8.631437,-2.058592,5.956923,-5.552566,-6.479750,-7.603607,-3.378809,-6.962655,6.787782,-2.243551,-9.760406,-5.541089,-6.129908,2.519417,-1.940454,-0.282455,5.878435,3.705156,0.152753,6.938948,7.007316,8.076621,-1.422884,-8.494993,2.536029,-9.237282,9.989506,8.659412,-1.770343,-8.789266,-5.310943,7.901615,3.426139,-4.740459,-8.158919,1.651694,1.791615,2.022595,-3.513682,-4.119443,1.607000,9.068236,3.877199,-3.541552,1.335202,-5.355334,7.410712,1.017268,5.978931,4.853687,1.904522,5.669904,5.434341,-7.070211,7.786111,5.762351,-0.223854,5.018750,5.414367,0.745109,-4.487414,-2.612365,3.568258,-1.527293,-3.374678,6.869101,-8.110087,-3.403774,1.990688,9.508280,3.956511,4.505545,1.267534,-8.236252,-6.704929,4.971793,3.662006,-8.911967,7.877930,3.008985,3.773169,7.105915,-1.928062,6.511772,3.903929,-1.232712,-3.142789,-7.749536,-7.593484,-5.138186,-2.832347,5.771753,-7.669153,-9.907129,-2.072985,3.983107,-6.274623,-7.880609,-0.518345,4.185356,-4.949631,1.237830,7.393672,9.811635,-5.676228,5.286227,2.822095,-1.804257,-7.488681,-6.928832,1.481477,-9.876037,-8.531667,-8.015567,8.180269,-3.245301,2.252821,-6.702345,8.664809,-1.601696,2.109669,-9.536388,-3.852313,-0.393946,-9.158813,2.344302,-0.485851,6.564037,-2.579806,-4.636957,4.134474,-1.478246,-2.756411,-2.790174,-5.150123,9.191782,-4.449823,-2.756844,-6.449376,2.781067,0.220360,-8.624576,2.442015,5.133484,7.687099,0.796550,-6.592650,8.672529,-1.406046,8.934942,-6.157425,-3.793295,-5.835335,7.504349,-0.728838,1.179719,-4.030260,1.980742,-1.707314,0.434509,-7.832265,-5.309677,-7.157156,3.931319,3.546309,2.987058,7.862441,-3.625937,9.796914,9.277017,0.340656,8.870402,-5.810946,1.066600,4.066232,3.048508,6.132615,5.133431,5.062816,-0.509029,6.424839,9.438712,1.451343,-5.778472,4.715599,-6.758737,1.106737,-2.000436,5.972112,-9.384433,8.445291,-7.550595,8.997517,-9.339981,0.931525,-8.464704,1.381637,6.990273,7.239597,7.811281,7.460979,2.994334,4.165959,6.362301,1.845606,-7.445171,7.865264,2.415390,-6.977128,8.132572,-7.018410,-6.020591,9.187695,2.104131,3.457132,-6.224044,-5.108696,2.476505,0.251538,-8.701486,-6.999203,3.736961,-2.274737,5.195299,6.263616,-0.250178,-5.132631,3.922880,-2.947434,-7.038674,4.590737,4.445296,1.486861,6.192579,5.578155,6.594378,-7.198422,1.466465,-9.758195,9.029699,5.132205,7.272503,-6.675528,-0.836281,5.468758,9.194238,8.047921,8.738885,9.767943,9.329957,-3.273623,9.346003,-6.291521,7.304526,7.514706,-6.810309,-2.879727,-9.142461,-8.998180,-0.069330,1.184476,-3.515846,-9.882233,1.893982,-3.719374,-3.325205,-0.607140,-2.943991,-2.995904,5.635707,-5.781583,-7.355949,4.459834,-0.086372,8.789955,-3.536399,-7.722371,9.367532,-5.286569,-6.684931,-4.734849,0.229812,-9.471964,7.923906,-6.470067,-4.106023,-7.789838,1.333255,7.924310,8.331221,-3.236122,-8.282795,-1.815233,7.791168,-2.468534,7.554651,-7.076254,9.304037,-7.187789,6.928274,6.078614,-6.847743,7.774058,-7.947655,7.956103,1.261092,6.587848,-5.073840,-5.638955,-4.561573,4.083463,2.212041,-9.087792,9.202003,9.791511,8.412953,-5.623588,-0.040275,-2.934073,6.735809,-5.214861,6.573546,-0.490710,7.691793,-2.417349,9.316019,7.645150,5.424648,-5.507727,1.753887,-3.330805,-9.752156,-6.544778,-6.307457,3.212039,-5.629215,-6.718977,1.933109,4.659595,9.784195,-2.586977,7.751463], dtype = "float64")#candidate|4085|(1470,)|const|float64
call_4083 = func_3139_call(relay.reshape(var_4084.astype('float64'), [1, 7, 15]), relay.reshape(const_4085.astype('float64'), [14, 7, 15]), )
call_4086 = func_3139_call(relay.reshape(var_4084.astype('float64'), [1, 7, 15]), relay.reshape(const_4085.astype('float64'), [14, 7, 15]), )
uop_4089 = relay.log10(const_4085.astype('float32')) # shape=(1470,)
output = relay.Tuple([call_4079,call_4083,var_4084,uop_4089,])
output2 = relay.Tuple([call_4080,call_4086,var_4084,uop_4089,])
func_4100 = relay.Function([var_4084,], output)
mod['func_4100'] = func_4100
mod = relay.transform.InferType()(mod)
var_4101 = relay.var("var_4101", dtype = "float64", shape = (7, 15))#candidate|4101|(7, 15)|var|float64
output = func_4100(var_4101)
func_4102 = relay.Function([var_4101], output)
mutated_mod['func_4102'] = func_4102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_4104 = relay.TupleGetItem(func_2545_call(), 3)
call_4105 = relay.TupleGetItem(func_2546_call(), 3)
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_4113 = relay.TupleGetItem(func_299_call(), 2)
call_4114 = relay.TupleGetItem(func_300_call(), 2)
output = relay.Tuple([call_4104,call_4113,])
output2 = relay.Tuple([call_4105,call_4114,])
func_4120 = relay.Function([], output)
mod['func_4120'] = func_4120
mod = relay.transform.InferType()(mod)
output = func_4120()
func_4121 = relay.Function([], output)
mutated_mod['func_4121'] = func_4121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4120_call = mod.get_global_var('func_4120')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_4142 = relay.TupleGetItem(func_4120_call(), 0)
call_4143 = relay.TupleGetItem(func_4121_call(), 0)
func_2098_call = mod.get_global_var('func_2098')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_4146 = relay.TupleGetItem(func_2098_call(), 0)
call_4147 = relay.TupleGetItem(func_2099_call(), 0)
func_318_call = mod.get_global_var('func_318')
func_319_call = mutated_mod.get_global_var('func_319')
call_4148 = func_318_call()
call_4149 = func_318_call()
func_2552_call = mod.get_global_var('func_2552')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_4157 = relay.TupleGetItem(func_2552_call(), 0)
call_4158 = relay.TupleGetItem(func_2553_call(), 0)
func_2657_call = mod.get_global_var('func_2657')
func_2661_call = mutated_mod.get_global_var('func_2661')
const_4180 = relay.const([False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,False,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,False,True,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,True,False,True,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,True,False,False,True,False,True,True,True,False,True,True,True,True,True,False,False,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,True,False,False,True,True,False,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,False,False,True,True,False,True,False,True,False], dtype = "bool")#candidate|4180|(630,)|const|bool
call_4179 = relay.TupleGetItem(func_2657_call(relay.reshape(const_4180.astype('bool'), [15, 6, 7]), relay.reshape(const_4180.astype('bool'), [15, 6, 7]), ), 0)
call_4181 = relay.TupleGetItem(func_2661_call(relay.reshape(const_4180.astype('bool'), [15, 6, 7]), relay.reshape(const_4180.astype('bool'), [15, 6, 7]), ), 0)
output = relay.Tuple([call_4142,call_4146,call_4148,call_4157,call_4179,const_4180,])
output2 = relay.Tuple([call_4143,call_4147,call_4149,call_4158,call_4181,const_4180,])
func_4194 = relay.Function([], output)
mod['func_4194'] = func_4194
mod = relay.transform.InferType()(mod)
output = func_4194()
func_4195 = relay.Function([], output)
mutated_mod['func_4195'] = func_4195
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3041_call = mod.get_global_var('func_3041')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_4237 = relay.TupleGetItem(func_3041_call(), 1)
call_4238 = relay.TupleGetItem(func_3042_call(), 1)
func_3256_call = mod.get_global_var('func_3256')
func_3257_call = mutated_mod.get_global_var('func_3257')
call_4247 = relay.TupleGetItem(func_3256_call(), 0)
call_4248 = relay.TupleGetItem(func_3257_call(), 0)
func_3443_call = mod.get_global_var('func_3443')
func_3446_call = mutated_mod.get_global_var('func_3446')
var_4256 = relay.var("var_4256", dtype = "float32", shape = (108,))#candidate|4256|(108,)|var|float32
call_4255 = relay.TupleGetItem(func_3443_call(relay.reshape(var_4256.astype('float32'), [108,])), 2)
call_4257 = relay.TupleGetItem(func_3446_call(relay.reshape(var_4256.astype('float32'), [108,])), 2)
output = relay.Tuple([call_4237,call_4247,call_4255,var_4256,])
output2 = relay.Tuple([call_4238,call_4248,call_4257,var_4256,])
func_4265 = relay.Function([var_4256,], output)
mod['func_4265'] = func_4265
mod = relay.transform.InferType()(mod)
mutated_mod['func_4265'] = func_4265
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4266 = relay.var("var_4266", dtype = "float32", shape = (108,))#candidate|4266|(108,)|var|float32
func_4265_call = mutated_mod.get_global_var('func_4265')
call_4267 = func_4265_call(var_4266)
output = call_4267
func_4268 = relay.Function([var_4266], output)
mutated_mod['func_4268'] = func_4268
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mod.get_global_var('func_2386')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_4316 = func_2386_call()
call_4317 = func_2386_call()
output = call_4316
output2 = call_4317
func_4322 = relay.Function([], output)
mod['func_4322'] = func_4322
mod = relay.transform.InferType()(mod)
mutated_mod['func_4322'] = func_4322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4322_call = mutated_mod.get_global_var('func_4322')
call_4323 = func_4322_call()
output = call_4323
func_4324 = relay.Function([], output)
mutated_mod['func_4324'] = func_4324
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1646_call = mod.get_global_var('func_1646')
func_1647_call = mutated_mod.get_global_var('func_1647')
call_4325 = relay.TupleGetItem(func_1646_call(), 0)
call_4326 = relay.TupleGetItem(func_1647_call(), 0)
output = relay.Tuple([call_4325,])
output2 = relay.Tuple([call_4326,])
func_4341 = relay.Function([], output)
mod['func_4341'] = func_4341
mod = relay.transform.InferType()(mod)
output = func_4341()
func_4342 = relay.Function([], output)
mutated_mod['func_4342'] = func_4342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3781_call = mutated_mod.get_global_var('func_3781')
call_4343 = relay.TupleGetItem(func_3779_call(), 0)
call_4344 = relay.TupleGetItem(func_3781_call(), 0)
var_4345 = relay.var("var_4345", dtype = "float64", shape = (4, 8, 9))#candidate|4345|(4, 8, 9)|var|float64
bop_4346 = relay.minimum(call_4343.astype('int8'), relay.reshape(var_4345.astype('int8'), relay.shape_of(call_4343))) # shape=(4, 8, 9)
bop_4349 = relay.minimum(call_4344.astype('int8'), relay.reshape(var_4345.astype('int8'), relay.shape_of(call_4344))) # shape=(4, 8, 9)
output = relay.Tuple([bop_4346,])
output2 = relay.Tuple([bop_4349,])
func_4351 = relay.Function([var_4345,], output)
mod['func_4351'] = func_4351
mod = relay.transform.InferType()(mod)
mutated_mod['func_4351'] = func_4351
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4352 = relay.var("var_4352", dtype = "float64", shape = (4, 8, 9))#candidate|4352|(4, 8, 9)|var|float64
func_4351_call = mutated_mod.get_global_var('func_4351')
call_4353 = func_4351_call(var_4352)
output = call_4353
func_4354 = relay.Function([var_4352], output)
mutated_mod['func_4354'] = func_4354
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4391 = relay.var("var_4391", dtype = "float32", shape = (14, 3, 13))#candidate|4391|(14, 3, 13)|var|float32
uop_4392 = relay.erf(var_4391.astype('float32')) # shape=(14, 3, 13)
bop_4398 = relay.greater(var_4391.astype('bool'), relay.reshape(uop_4392.astype('bool'), relay.shape_of(var_4391))) # shape=(14, 3, 13)
func_4100_call = mod.get_global_var('func_4100')
func_4102_call = mutated_mod.get_global_var('func_4102')
var_4403 = relay.var("var_4403", dtype = "float64", shape = (105,))#candidate|4403|(105,)|var|float64
call_4402 = relay.TupleGetItem(func_4100_call(relay.reshape(var_4403.astype('float64'), [7, 15])), 1)
call_4404 = relay.TupleGetItem(func_4102_call(relay.reshape(var_4403.astype('float64'), [7, 15])), 1)
bop_4412 = relay.bitwise_and(bop_4398.astype('int8'), relay.reshape(uop_4392.astype('int8'), relay.shape_of(bop_4398))) # shape=(14, 3, 13)
output = relay.Tuple([call_4402,var_4403,bop_4412,])
output2 = relay.Tuple([call_4404,var_4403,bop_4412,])
func_4426 = relay.Function([var_4391,var_4403,], output)
mod['func_4426'] = func_4426
mod = relay.transform.InferType()(mod)
var_4427 = relay.var("var_4427", dtype = "float32", shape = (14, 3, 13))#candidate|4427|(14, 3, 13)|var|float32
var_4428 = relay.var("var_4428", dtype = "float64", shape = (105,))#candidate|4428|(105,)|var|float64
output = func_4426(var_4427,var_4428,)
func_4429 = relay.Function([var_4427,var_4428,], output)
mutated_mod['func_4429'] = func_4429
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4494 = relay.var("var_4494", dtype = "float64", shape = (11, 13, 15))#candidate|4494|(11, 13, 15)|var|float64
uop_4495 = relay.log2(var_4494.astype('float64')) # shape=(11, 13, 15)
output = uop_4495
output2 = uop_4495
func_4497 = relay.Function([var_4494,], output)
mod['func_4497'] = func_4497
mod = relay.transform.InferType()(mod)
var_4498 = relay.var("var_4498", dtype = "float64", shape = (11, 13, 15))#candidate|4498|(11, 13, 15)|var|float64
output = func_4497(var_4498)
func_4499 = relay.Function([var_4498], output)
mutated_mod['func_4499'] = func_4499
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3842_call = mod.get_global_var('func_3842')
func_3844_call = mutated_mod.get_global_var('func_3844')
call_4537 = relay.TupleGetItem(func_3842_call(), 0)
call_4538 = relay.TupleGetItem(func_3844_call(), 0)
func_4322_call = mod.get_global_var('func_4322')
func_4324_call = mutated_mod.get_global_var('func_4324')
call_4561 = func_4322_call()
call_4562 = func_4322_call()
output = relay.Tuple([call_4537,call_4561,])
output2 = relay.Tuple([call_4538,call_4562,])
func_4563 = relay.Function([], output)
mod['func_4563'] = func_4563
mod = relay.transform.InferType()(mod)
mutated_mod['func_4563'] = func_4563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4563_call = mutated_mod.get_global_var('func_4563')
call_4564 = func_4563_call()
output = call_4564
func_4565 = relay.Function([], output)
mutated_mod['func_4565'] = func_4565
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4589 = relay.var("var_4589", dtype = "bool", shape = (1, 1, 12))#candidate|4589|(1, 1, 12)|var|bool
var_4590 = relay.var("var_4590", dtype = "bool", shape = (6, 8, 12))#candidate|4590|(6, 8, 12)|var|bool
bop_4591 = relay.logical_and(var_4589.astype('bool'), var_4590.astype('bool')) # shape=(6, 8, 12)
bop_4600 = relay.bitwise_or(bop_4591.astype('int8'), relay.reshape(var_4590.astype('int8'), relay.shape_of(bop_4591))) # shape=(6, 8, 12)
func_1001_call = mod.get_global_var('func_1001')
func_1003_call = mutated_mod.get_global_var('func_1003')
const_4616 = relay.const([-9.299198,-8.979096,3.284666,0.275000,3.716509,-9.452584,1.027582,-1.506925,0.024575,-1.083189,-5.000101,-4.904619,2.725888,8.535888,-1.514574,-3.291412,2.476738,-1.883830,7.692023,-8.945377,-9.921154,2.640472,-8.387596,-6.607172,-5.329710,3.177346,2.287092,4.689529,4.216508,3.189404,4.543891,1.095247,-7.767989,9.337931,3.362569,7.476402,-4.362040,-6.316350,-6.775653,-9.378444,4.410225,9.945449,3.508019,5.802840,-5.174331,-1.157297,-4.340136,-9.287290,-1.645483,8.453965,2.874296,4.899396,1.683676,1.713762,-1.114976,-5.192323,8.347126,8.571018,-3.970281,8.341675,1.155233,-3.183876,7.182711,4.872223,7.060370,-8.755168,6.633804,-4.883207,2.845813,-1.851097,-0.687761,7.890452,-3.276543,-0.803543,-0.157109,2.095199,-0.045889,7.456718,0.570869,9.365906,9.247289,0.202496,0.991237,5.350899,0.971172,-7.894387,-8.381764,9.494351,-0.298622,7.782936,-6.528695,7.702151,6.044410,-7.679682,9.945374,2.271013,8.720123,3.373426,-6.881804,4.994158,-5.288193,1.938958,-7.403457,7.820601,9.014042,1.487832,-2.545713,-2.063649], dtype = "float32")#candidate|4616|(108,)|const|float32
call_4615 = func_1001_call(relay.reshape(const_4616.astype('float32'), [9, 12, 1]))
call_4617 = func_1001_call(relay.reshape(const_4616.astype('float32'), [9, 12, 1]))
func_299_call = mod.get_global_var('func_299')
func_300_call = mutated_mod.get_global_var('func_300')
call_4624 = relay.TupleGetItem(func_299_call(), 1)
call_4625 = relay.TupleGetItem(func_300_call(), 1)
output = relay.Tuple([bop_4600,call_4615,const_4616,call_4624,])
output2 = relay.Tuple([bop_4600,call_4617,const_4616,call_4625,])
func_4628 = relay.Function([var_4589,var_4590,], output)
mod['func_4628'] = func_4628
mod = relay.transform.InferType()(mod)
var_4629 = relay.var("var_4629", dtype = "bool", shape = (1, 1, 12))#candidate|4629|(1, 1, 12)|var|bool
var_4630 = relay.var("var_4630", dtype = "bool", shape = (6, 8, 12))#candidate|4630|(6, 8, 12)|var|bool
output = func_4628(var_4629,var_4630,)
func_4631 = relay.Function([var_4629,var_4630,], output)
mutated_mod['func_4631'] = func_4631
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1196_call = mod.get_global_var('func_1196')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_4654 = relay.TupleGetItem(func_1196_call(), 1)
call_4655 = relay.TupleGetItem(func_1198_call(), 1)
func_3894_call = mod.get_global_var('func_3894')
func_3895_call = mutated_mod.get_global_var('func_3895')
call_4661 = func_3894_call()
call_4662 = func_3894_call()
output = relay.Tuple([call_4654,call_4661,])
output2 = relay.Tuple([call_4655,call_4662,])
func_4670 = relay.Function([], output)
mod['func_4670'] = func_4670
mod = relay.transform.InferType()(mod)
output = func_4670()
func_4671 = relay.Function([], output)
mutated_mod['func_4671'] = func_4671
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4787 = relay.var("var_4787", dtype = "float64", shape = (4, 13))#candidate|4787|(4, 13)|var|float64
uop_4788 = relay.rsqrt(var_4787.astype('float64')) # shape=(4, 13)
output = relay.Tuple([uop_4788,])
output2 = relay.Tuple([uop_4788,])
func_4802 = relay.Function([var_4787,], output)
mod['func_4802'] = func_4802
mod = relay.transform.InferType()(mod)
mutated_mod['func_4802'] = func_4802
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4803 = relay.var("var_4803", dtype = "float64", shape = (4, 13))#candidate|4803|(4, 13)|var|float64
func_4802_call = mutated_mod.get_global_var('func_4802')
call_4804 = func_4802_call(var_4803)
output = call_4804
func_4805 = relay.Function([var_4803], output)
mutated_mod['func_4805'] = func_4805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1646_call = mod.get_global_var('func_1646')
func_1647_call = mutated_mod.get_global_var('func_1647')
call_4810 = relay.TupleGetItem(func_1646_call(), 0)
call_4811 = relay.TupleGetItem(func_1647_call(), 0)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_4820 = relay.TupleGetItem(func_3291_call(), 1)
call_4821 = relay.TupleGetItem(func_3293_call(), 1)
func_4563_call = mod.get_global_var('func_4563')
func_4565_call = mutated_mod.get_global_var('func_4565')
call_4824 = relay.TupleGetItem(func_4563_call(), 1)
call_4825 = relay.TupleGetItem(func_4565_call(), 1)
func_696_call = mod.get_global_var('func_696')
func_697_call = mutated_mod.get_global_var('func_697')
call_4833 = relay.TupleGetItem(func_696_call(), 0)
call_4834 = relay.TupleGetItem(func_697_call(), 0)
output = relay.Tuple([call_4810,call_4820,call_4824,call_4833,])
output2 = relay.Tuple([call_4811,call_4821,call_4825,call_4834,])
func_4854 = relay.Function([], output)
mod['func_4854'] = func_4854
mod = relay.transform.InferType()(mod)
mutated_mod['func_4854'] = func_4854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mutated_mod.get_global_var('func_4854')
call_4855 = func_4854_call()
output = call_4855
func_4856 = relay.Function([], output)
mutated_mod['func_4856'] = func_4856
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_863_call = mutated_mod.get_global_var('func_863')
call_4857 = relay.TupleGetItem(func_861_call(), 2)
call_4858 = relay.TupleGetItem(func_863_call(), 2)
func_3291_call = mod.get_global_var('func_3291')
func_3293_call = mutated_mod.get_global_var('func_3293')
call_4893 = relay.TupleGetItem(func_3291_call(), 1)
call_4894 = relay.TupleGetItem(func_3293_call(), 1)
func_3198_call = mod.get_global_var('func_3198')
func_3201_call = mutated_mod.get_global_var('func_3201')
call_4908 = relay.TupleGetItem(func_3198_call(relay.reshape(call_4893.astype('float64'), [7, 10, 2])), 0)
call_4909 = relay.TupleGetItem(func_3201_call(relay.reshape(call_4893.astype('float64'), [7, 10, 2])), 0)
func_3041_call = mod.get_global_var('func_3041')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_4920 = relay.TupleGetItem(func_3041_call(), 0)
call_4921 = relay.TupleGetItem(func_3042_call(), 0)
func_1272_call = mod.get_global_var('func_1272')
func_1275_call = mutated_mod.get_global_var('func_1275')
const_4935 = relay.const([[1.157839,6.410129,6.863775,8.549868,6.084601,7.784500,9.026689,-5.374454,-2.019697,7.203233,-7.458079,5.681071,-8.674480,-6.890362,-9.616060,4.286461,-8.314006,-7.439339,5.076022,-2.376883,-4.871250,5.790596,-3.945609,-1.856892,-0.264375,-2.103938,8.509051,-2.833899,-9.895487,7.147029,-3.207979,5.996297,3.234292,-7.297357,6.682929,1.488371,-3.871469,0.951115,-8.023209,3.438422,-1.001067,-4.361649,4.624676,2.717497]], dtype = "float64")#candidate|4935|(1, 44)|const|float64
call_4934 = relay.TupleGetItem(func_1272_call(relay.reshape(const_4935.astype('float64'), [44,])), 1)
call_4936 = relay.TupleGetItem(func_1275_call(relay.reshape(const_4935.astype('float64'), [44,])), 1)
output = relay.Tuple([call_4857,call_4893,call_4908,call_4920,call_4934,const_4935,])
output2 = relay.Tuple([call_4858,call_4894,call_4909,call_4921,call_4936,const_4935,])
func_4970 = relay.Function([], output)
mod['func_4970'] = func_4970
mod = relay.transform.InferType()(mod)
output = func_4970()
func_4971 = relay.Function([], output)
mutated_mod['func_4971'] = func_4971
mutated_mod = relay.transform.InferType()(mutated_mod)
func_912_call = mod.get_global_var('func_912')
func_913_call = mutated_mod.get_global_var('func_913')
call_4975 = relay.TupleGetItem(func_912_call(), 1)
call_4976 = relay.TupleGetItem(func_913_call(), 1)
output = relay.Tuple([call_4975,])
output2 = relay.Tuple([call_4976,])
func_4995 = relay.Function([], output)
mod['func_4995'] = func_4995
mod = relay.transform.InferType()(mod)
mutated_mod['func_4995'] = func_4995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4995_call = mutated_mod.get_global_var('func_4995')
call_4996 = func_4995_call()
output = call_4996
func_4997 = relay.Function([], output)
mutated_mod['func_4997'] = func_4997
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1416_call = mod.get_global_var('func_1416')
func_1417_call = mutated_mod.get_global_var('func_1417')
call_5017 = func_1416_call()
call_5018 = func_1416_call()
var_5019 = relay.var("var_5019", dtype = "float64", shape = (7, 10, 2))#candidate|5019|(7, 10, 2)|var|float64
bop_5020 = relay.power(call_5017.astype('float64'), relay.reshape(var_5019.astype('float64'), relay.shape_of(call_5017))) # shape=(7, 10, 2)
bop_5023 = relay.power(call_5018.astype('float64'), relay.reshape(var_5019.astype('float64'), relay.shape_of(call_5018))) # shape=(7, 10, 2)
output = bop_5020
output2 = bop_5023
func_5033 = relay.Function([var_5019,], output)
mod['func_5033'] = func_5033
mod = relay.transform.InferType()(mod)
var_5034 = relay.var("var_5034", dtype = "float64", shape = (7, 10, 2))#candidate|5034|(7, 10, 2)|var|float64
output = func_5033(var_5034)
func_5035 = relay.Function([var_5034], output)
mutated_mod['func_5035'] = func_5035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1703_call = mod.get_global_var('func_1703')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_5046 = func_1703_call()
call_5047 = func_1703_call()
func_1639_call = mod.get_global_var('func_1639')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_5048 = relay.TupleGetItem(func_1639_call(), 0)
call_5049 = relay.TupleGetItem(func_1640_call(), 0)
func_4563_call = mod.get_global_var('func_4563')
func_4565_call = mutated_mod.get_global_var('func_4565')
call_5050 = relay.TupleGetItem(func_4563_call(), 0)
call_5051 = relay.TupleGetItem(func_4565_call(), 0)
func_4563_call = mod.get_global_var('func_4563')
func_4565_call = mutated_mod.get_global_var('func_4565')
call_5065 = relay.TupleGetItem(func_4563_call(), 1)
call_5066 = relay.TupleGetItem(func_4565_call(), 1)
output = relay.Tuple([call_5046,call_5048,call_5050,call_5065,])
output2 = relay.Tuple([call_5047,call_5049,call_5051,call_5066,])
func_5087 = relay.Function([], output)
mod['func_5087'] = func_5087
mod = relay.transform.InferType()(mod)
mutated_mod['func_5087'] = func_5087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5087_call = mutated_mod.get_global_var('func_5087')
call_5088 = func_5087_call()
output = call_5088
func_5089 = relay.Function([], output)
mutated_mod['func_5089'] = func_5089
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5099 = relay.var("var_5099", dtype = "float64", shape = (2, 2, 13))#candidate|5099|(2, 2, 13)|var|float64
uop_5100 = relay.exp(var_5099.astype('float64')) # shape=(2, 2, 13)
output = uop_5100
output2 = uop_5100
func_5102 = relay.Function([var_5099,], output)
mod['func_5102'] = func_5102
mod = relay.transform.InferType()(mod)
mutated_mod['func_5102'] = func_5102
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5103 = relay.var("var_5103", dtype = "float64", shape = (2, 2, 13))#candidate|5103|(2, 2, 13)|var|float64
func_5102_call = mutated_mod.get_global_var('func_5102')
call_5104 = func_5102_call(var_5103)
output = call_5104
func_5105 = relay.Function([var_5103], output)
mutated_mod['func_5105'] = func_5105
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2160_call = mod.get_global_var('func_2160')
func_2162_call = mutated_mod.get_global_var('func_2162')
call_5149 = func_2160_call()
call_5150 = func_2160_call()
func_4100_call = mod.get_global_var('func_4100')
func_4102_call = mutated_mod.get_global_var('func_4102')
const_5166 = relay.const([3.305711,3.205133,-4.754939,3.193016,-4.811855,6.897096,-8.550121,9.636282,-6.147531,-3.314292,-1.570866,8.641174,0.725284,-6.015230,-4.586623,-7.035789,-5.518094,-0.585890,1.411981,9.609566,3.951734,3.908930,-9.442544,-6.892307,-8.723629,-7.549146,6.400272,4.451662,0.581766,-2.139917,-6.153269,5.828649,-4.477547,-3.245391,4.154075,3.000391,-2.060901,-3.324684,6.504227,-3.861891,2.863339,-5.654275,-0.597127,0.546716,9.300849,6.246766,-0.858676,-5.316241,-3.575957,-1.570455,0.771331,0.723698,-6.854719,-4.120333,-5.416090,1.618435,-7.965322,-6.475609,-4.735976,-4.078782,8.888842,3.973716,-1.452075,-3.454574,-4.346144,-8.654263,-7.851024,-8.930486,6.951460,-0.656588,6.295026,-2.546397,7.392924,-1.616884,-2.892290,0.246691,4.767167,-2.239936,2.480605,-3.617791,9.126337,4.741402,-1.720243,5.334121,-5.220034,4.021189,0.894631,6.170009,7.648391,-1.421678,-5.904927,8.801600,7.190419,6.860498,6.289102,-5.158211,-0.851605,-1.692568,6.802910,8.050418,-0.481807,0.440678,-2.020657,-3.018297,0.238820], dtype = "float64")#candidate|5166|(105,)|const|float64
call_5165 = relay.TupleGetItem(func_4100_call(relay.reshape(const_5166.astype('float64'), [7, 15])), 2)
call_5167 = relay.TupleGetItem(func_4102_call(relay.reshape(const_5166.astype('float64'), [7, 15])), 2)
func_1125_call = mod.get_global_var('func_1125')
func_1127_call = mutated_mod.get_global_var('func_1127')
const_5182 = relay.const([-6.298953,7.874419,1.163090,2.445574,-0.352905,5.158914,3.393536,-5.818470,-3.300910,7.718839,4.112965,0.308887,8.361374,3.551473,6.652445,8.606282,-3.231808,-4.187006,-2.753167,-3.706548,4.883372,-1.780676,-0.003407,-6.573668,6.350076,-1.880451,2.463533,-1.776107,-4.289063,9.842052,-9.833962,-6.091576,-1.690514,-5.648601,-5.142548,1.432888,1.289912,-2.922933,-3.351502,-8.680684,-8.048342,-1.008520,-5.905949,-7.964322], dtype = "float64")#candidate|5182|(44,)|const|float64
call_5181 = relay.TupleGetItem(func_1125_call(relay.reshape(const_5182.astype('float64'), [44,])), 0)
call_5183 = relay.TupleGetItem(func_1127_call(relay.reshape(const_5182.astype('float64'), [44,])), 0)
output = relay.Tuple([call_5149,call_5165,const_5166,call_5181,const_5182,])
output2 = relay.Tuple([call_5150,call_5167,const_5166,call_5183,const_5182,])
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
func_1196_call = mod.get_global_var('func_1196')
func_1198_call = mutated_mod.get_global_var('func_1198')
call_5242 = relay.TupleGetItem(func_1196_call(), 1)
call_5243 = relay.TupleGetItem(func_1198_call(), 1)
output = relay.Tuple([call_5242,])
output2 = relay.Tuple([call_5243,])
func_5255 = relay.Function([], output)
mod['func_5255'] = func_5255
mod = relay.transform.InferType()(mod)
output = func_5255()
func_5256 = relay.Function([], output)
mutated_mod['func_5256'] = func_5256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1646_call = mod.get_global_var('func_1646')
func_1647_call = mutated_mod.get_global_var('func_1647')
call_5257 = relay.TupleGetItem(func_1646_call(), 0)
call_5258 = relay.TupleGetItem(func_1647_call(), 0)
func_1703_call = mod.get_global_var('func_1703')
func_1705_call = mutated_mod.get_global_var('func_1705')
call_5259 = func_1703_call()
call_5260 = func_1703_call()
output = relay.Tuple([call_5257,call_5259,])
output2 = relay.Tuple([call_5258,call_5260,])
func_5261 = relay.Function([], output)
mod['func_5261'] = func_5261
mod = relay.transform.InferType()(mod)
mutated_mod['func_5261'] = func_5261
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5261_call = mutated_mod.get_global_var('func_5261')
call_5262 = func_5261_call()
output = call_5262
func_5263 = relay.Function([], output)
mutated_mod['func_5263'] = func_5263
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5296 = relay.var("var_5296", dtype = "float64", shape = (10, 12, 16))#candidate|5296|(10, 12, 16)|var|float64
uop_5297 = relay.asinh(var_5296.astype('float64')) # shape=(10, 12, 16)
output = relay.Tuple([uop_5297,])
output2 = relay.Tuple([uop_5297,])
func_5306 = relay.Function([var_5296,], output)
mod['func_5306'] = func_5306
mod = relay.transform.InferType()(mod)
var_5307 = relay.var("var_5307", dtype = "float64", shape = (10, 12, 16))#candidate|5307|(10, 12, 16)|var|float64
output = func_5306(var_5307)
func_5308 = relay.Function([var_5307], output)
mutated_mod['func_5308'] = func_5308
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2098_call = mod.get_global_var('func_2098')
func_2099_call = mutated_mod.get_global_var('func_2099')
call_5330 = relay.TupleGetItem(func_2098_call(), 0)
call_5331 = relay.TupleGetItem(func_2099_call(), 0)
func_3405_call = mod.get_global_var('func_3405')
func_3408_call = mutated_mod.get_global_var('func_3408')
const_5335 = relay.const([-7,5,-9,10,-2,5,3,-3,5,8,5,9,9,-4,-10,-8,2,-6,6,8,-8,2,-7,8,2,1,8,-7,10,5,-2,9,-8,6,3,-4,7,10,-2,-5,-4,6,-8,8,-2,-8,-6,2,-3,10,2,-5,-1,-2,5,9,-6,3,6,10,2,4,-6,-4,5,-5,7,8,6,8,7,-1,2,5,-3,6,4,5,-8,-8,-10,-2,2,-4,-9,-8,-2,9,2,10,10,3,9,3,7,-10,6,-6,1,-5,-2,7,3,-8,2,10,-5,6,-1,1,4,-4,5,-7,10,9,8,-8,1,-5,3,5,-2,-3,-3,10,-6,-6,-6,9,8,8,3,-6,-1,7,10,-3,4,3,10,3,-2,9,5,-4,6,-6,9,3,-2,-3,2,-5,3,4,-3,-1,9,3,-8,4,8,-10,1,-6,-4,7,8,-4,10,-4,6,-10,-3,-8,9,-4,-3,3,-10,9,9,-9,10,7,3,4,5,6,-8,-1,-10,1,1,-7,4,-2,4,9,-9,3,-8,-3,5,-2,-6,8,-10,-9,-5,-10,2,4,-7,1,9,-8,-5,1,10,10,6,2,-1,7,-7,6,10,7,-3,3,-4,-1,2,6,-5,10,8,-7,4,4,-10,-1,2,-8,-8,-9,2,1,1,-7,-8,10,-10,-5], dtype = "int64")#candidate|5335|(256,)|const|int64
const_5336 = relay.const([-4,-1,9,-6,-8,-10,9,6,7,1,-6,1,-5,2,-3,-10,2,-3,5,-10,6,-10,1,6,5,-1,6,-8,-3,2,-3,-3,2,-8,7,-9,-7,7,7,3,1,-5,-6,-8,5,-4,-10,5,-5,10,10,-7,10,-4,-5,9,3,-3,-8,7,-2,-6,-10,-6,-4,8,-8,3,-9,5,6,-10,-9,-5,5,-4,4,9,1,-8,-4,2,-3,1,2,6,1,6,-10,-9,-4,3,-3,2,10,10,8,5,5,-1,-2,-6,4,3,2,10,4,-5,-6,10,7,-7,10,-6,9,-5,-4,-6,-2,2,-2,1,4,5,-3,5,7,-4,-7,5,10,1,-10,4,-7,-5,9,-8,-1,4,-2,-5,2,-7,2,4,-1,-7,1,2,-8,-8,-4,-1,-9,-3,3,-9,9,-1,-9,2,10,-4,1,-1,-4,3,7,-5,8,-9,-5,-5,6,3,2,9,7,5,9,6,-6,1,4,2,-3,-2,-9,3,2,3,3,6,-5,-7,-8,6,-1,-9,-5,6,10,-8,-4,6,-7,10,3,2,-10,10,4,-1,-5,2,1,-9,6,2,10,-8,9,9,-5,-7,1,-2,-5,2,5,-1,-3,-9,-10,9,-3,7,4,-3,8,-3,-9,-6,9,-6,3,1,10,5,3,1,2,7,5,-6,-1,-2,5,7,-7,10,-10,5,3,1,-5,-3,10,4,1,6,2,-4,-7,3,-4,1,-4,-6,-8,4,-7,10,-6,-3,-8,-10,-9,7,7,-8,-3,-7,-7,5,-9,-9,-5,-4,-5,9,-7,4,-5,-2,1,5,2,2,-4,5,5,10,4,2,-2,-5,-3,-5,-9,3,8,7,-2,9,5,1,-1,1,-6,7,5,-9,10,-7,2,3,9,-9,-7,5,4,4,-7,-1,8,-5,1,-1,7,-1,9,-10,-2,-7,9,4,10,-9,3,-3,9,5,-9,10,-6,6,5,-4,-5,9,-5,-7,1,3,7,6,-4,-5,-1,1,-6,-5,-3,1,1,1,-10,-2,-6,6,3,-9,-5,9,9,-3,7,7,8,7,7,7,8,-10,-6,-6,-8,-7,-9,-1,6,-3,-4,2,-8,9,-1,-3,-6,1,-9,3,4,-4,-8,-1,-1,-9,7,-4,2,-2,-2,2,-10,-1,2,8,-6,10,7,8,8,-10,-9,-3,10,4,2,9,10,1,-4,9,1,-3,3,-8,-7,7,5,-6,5,6,-9,9,6,1,-1,9,-10,-2,-2,-5,9,4,1,-8,4,-4,-2,10,3,8,-2,5,7,-6,-8,-9,-2,-10,5,-9,-3,-1,8,-2,3,-4,-7,10,8,3,6,2,5,10,9,8], dtype = "int64")#candidate|5336|(512,)|const|int64
call_5334 = relay.TupleGetItem(func_3405_call(relay.reshape(const_5335.astype('int64'), [16, 1, 16]), relay.reshape(const_5336.astype('int64'), [16, 2, 16]), ), 1)
call_5337 = relay.TupleGetItem(func_3408_call(relay.reshape(const_5335.astype('int64'), [16, 1, 16]), relay.reshape(const_5336.astype('int64'), [16, 2, 16]), ), 1)
output = relay.Tuple([call_5330,call_5334,const_5335,const_5336,])
output2 = relay.Tuple([call_5331,call_5337,const_5335,const_5336,])
func_5339 = relay.Function([], output)
mod['func_5339'] = func_5339
mod = relay.transform.InferType()(mod)
output = func_5339()
func_5340 = relay.Function([], output)
mutated_mod['func_5340'] = func_5340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3256_call = mod.get_global_var('func_3256')
func_3257_call = mutated_mod.get_global_var('func_3257')
call_5347 = relay.TupleGetItem(func_3256_call(), 0)
call_5348 = relay.TupleGetItem(func_3257_call(), 0)
output = relay.Tuple([call_5347,])
output2 = relay.Tuple([call_5348,])
func_5351 = relay.Function([], output)
mod['func_5351'] = func_5351
mod = relay.transform.InferType()(mod)
output = func_5351()
func_5352 = relay.Function([], output)
mutated_mod['func_5352'] = func_5352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mod.get_global_var('func_4854')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_5353 = relay.TupleGetItem(func_4854_call(), 2)
call_5354 = relay.TupleGetItem(func_4856_call(), 2)
func_2552_call = mod.get_global_var('func_2552')
func_2553_call = mutated_mod.get_global_var('func_2553')
call_5369 = relay.TupleGetItem(func_2552_call(), 0)
call_5370 = relay.TupleGetItem(func_2553_call(), 0)
output = relay.Tuple([call_5353,call_5369,])
output2 = relay.Tuple([call_5354,call_5370,])
func_5377 = relay.Function([], output)
mod['func_5377'] = func_5377
mod = relay.transform.InferType()(mod)
mutated_mod['func_5377'] = func_5377
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5377_call = mutated_mod.get_global_var('func_5377')
call_5378 = func_5377_call()
output = call_5378
func_5379 = relay.Function([], output)
mutated_mod['func_5379'] = func_5379
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5428 = relay.var("var_5428", dtype = "int16", shape = (14, 1, 6))#candidate|5428|(14, 1, 6)|var|int16
var_5429 = relay.var("var_5429", dtype = "int16", shape = (14, 6, 6))#candidate|5429|(14, 6, 6)|var|int16
bop_5430 = relay.right_shift(var_5428.astype('int16'), var_5429.astype('int16')) # shape=(14, 6, 6)
output = bop_5430
output2 = bop_5430
func_5441 = relay.Function([var_5428,var_5429,], output)
mod['func_5441'] = func_5441
mod = relay.transform.InferType()(mod)
mutated_mod['func_5441'] = func_5441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5441_call = mutated_mod.get_global_var('func_5441')
var_5443 = relay.var("var_5443", dtype = "int16", shape = (14, 1, 6))#candidate|5443|(14, 1, 6)|var|int16
var_5444 = relay.var("var_5444", dtype = "int16", shape = (14, 6, 6))#candidate|5444|(14, 6, 6)|var|int16
call_5442 = func_5441_call(var_5443,var_5444,)
output = call_5442
func_5445 = relay.Function([var_5443,var_5444,], output)
mutated_mod['func_5445'] = func_5445
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5491 = relay.var("var_5491", dtype = "float64", shape = ())#candidate|5491|()|var|float64
var_5492 = relay.var("var_5492", dtype = "float64", shape = (1, 10, 6))#candidate|5492|(1, 10, 6)|var|float64
bop_5493 = relay.floor_mod(var_5491.astype('float64'), var_5492.astype('float64')) # shape=(1, 10, 6)
bop_5496 = relay.maximum(var_5491.astype('float64'), var_5492.astype('float64')) # shape=(1, 10, 6)
func_2069_call = mod.get_global_var('func_2069')
func_2071_call = mutated_mod.get_global_var('func_2071')
const_5502 = relay.const([-1.832109,-2.469638,1.221353,8.339667,-7.281959,5.693815,3.764055,0.442362,0.909830,3.020663,2.859374,-2.294075,-5.191789,-3.811379,3.170260,-0.331016,7.224402,-7.250561,-6.565154,9.001426,7.284122,3.567431,-6.146356,-3.484624,1.935972,-9.122333,-4.290205,0.493430,-2.270554,-6.722742,0.631194,9.017994,6.382669,9.356837,7.178701,-3.290969,-2.118802,1.895307,5.306102,-2.488884,-4.147674,6.635970,-5.219261,8.492119,-6.552417,-2.644150,-1.827723,5.143713,-8.468498,-1.181178,1.518725,-5.865366,-7.369759,-5.355107,6.256911,-1.806099,9.866228,-6.431346,-7.230158,4.805273,3.573387,-4.821464,5.269018,1.332895,7.830078,-2.545880,3.495340,-2.535943,-6.430961,1.084267,2.125112,7.886586,5.146818,-9.874595,3.337529,-3.940116,-1.319388,8.699843,-6.907786,8.623907,-1.902373,-7.728303,-2.610339,0.403891,2.261428,-5.812075,6.345803,-0.501999,9.345107,-4.094073,-4.344541,8.542621,-2.611579,-6.244552,4.481720,-9.560683,7.556477,8.630961,3.352673,4.587760,1.798457,2.266043,0.746387,9.652119,1.954008,-8.332419,2.486531,-5.269330,-1.142217,-5.182453,-0.534169,3.953936,-2.867261,6.451221,7.543777,-4.297053,-7.634503,9.694429,2.890957,-0.037972,2.560351,-0.430208,-7.683926,-9.800114,-3.234035,-7.134141,7.618491,-1.130712,4.208662,7.236335,-6.081286,2.106014,7.788309,2.528382,-3.469845,9.095539,-5.121508,-0.945651,-8.271713,4.766526], dtype = "float64")#candidate|5502|(140,)|const|float64
call_5501 = relay.TupleGetItem(func_2069_call(relay.reshape(const_5502.astype('float64'), [7, 10, 2])), 2)
call_5503 = relay.TupleGetItem(func_2071_call(relay.reshape(const_5502.astype('float64'), [7, 10, 2])), 2)
output = relay.Tuple([bop_5493,bop_5496,call_5501,const_5502,])
output2 = relay.Tuple([bop_5493,bop_5496,call_5503,const_5502,])
func_5504 = relay.Function([var_5491,var_5492,], output)
mod['func_5504'] = func_5504
mod = relay.transform.InferType()(mod)
mutated_mod['func_5504'] = func_5504
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5504_call = mutated_mod.get_global_var('func_5504')
var_5506 = relay.var("var_5506", dtype = "float64", shape = ())#candidate|5506|()|var|float64
var_5507 = relay.var("var_5507", dtype = "float64", shape = (1, 10, 6))#candidate|5507|(1, 10, 6)|var|float64
call_5505 = func_5504_call(var_5506,var_5507,)
output = call_5505
func_5508 = relay.Function([var_5506,var_5507,], output)
mutated_mod['func_5508'] = func_5508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mod.get_global_var('func_2386')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_5517 = func_2386_call()
call_5518 = func_2386_call()
func_3469_call = mod.get_global_var('func_3469')
func_3470_call = mutated_mod.get_global_var('func_3470')
call_5520 = func_3469_call()
call_5521 = func_3469_call()
func_2465_call = mod.get_global_var('func_2465')
func_2466_call = mutated_mod.get_global_var('func_2466')
call_5527 = relay.TupleGetItem(func_2465_call(), 1)
call_5528 = relay.TupleGetItem(func_2466_call(), 1)
output = relay.Tuple([call_5517,call_5520,call_5527,])
output2 = relay.Tuple([call_5518,call_5521,call_5528,])
func_5531 = relay.Function([], output)
mod['func_5531'] = func_5531
mod = relay.transform.InferType()(mod)
output = func_5531()
func_5532 = relay.Function([], output)
mutated_mod['func_5532'] = func_5532
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2160_call = mod.get_global_var('func_2160')
func_2162_call = mutated_mod.get_global_var('func_2162')
call_5536 = func_2160_call()
call_5537 = func_2160_call()
output = relay.Tuple([call_5536,])
output2 = relay.Tuple([call_5537,])
func_5545 = relay.Function([], output)
mod['func_5545'] = func_5545
mod = relay.transform.InferType()(mod)
mutated_mod['func_5545'] = func_5545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5545_call = mutated_mod.get_global_var('func_5545')
call_5546 = func_5545_call()
output = call_5546
func_5547 = relay.Function([], output)
mutated_mod['func_5547'] = func_5547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3992_call = mod.get_global_var('func_3992')
func_3993_call = mutated_mod.get_global_var('func_3993')
call_5555 = relay.TupleGetItem(func_3992_call(), 0)
call_5556 = relay.TupleGetItem(func_3993_call(), 0)
func_5545_call = mod.get_global_var('func_5545')
func_5547_call = mutated_mod.get_global_var('func_5547')
call_5559 = relay.TupleGetItem(func_5545_call(), 0)
call_5560 = relay.TupleGetItem(func_5547_call(), 0)
output = relay.Tuple([call_5555,call_5559,])
output2 = relay.Tuple([call_5556,call_5560,])
func_5561 = relay.Function([], output)
mod['func_5561'] = func_5561
mod = relay.transform.InferType()(mod)
mutated_mod['func_5561'] = func_5561
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5561_call = mutated_mod.get_global_var('func_5561')
call_5562 = func_5561_call()
output = call_5562
func_5563 = relay.Function([], output)
mutated_mod['func_5563'] = func_5563
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5377_call = mod.get_global_var('func_5377')
func_5379_call = mutated_mod.get_global_var('func_5379')
call_5570 = relay.TupleGetItem(func_5377_call(), 1)
call_5571 = relay.TupleGetItem(func_5379_call(), 1)
output = call_5570
output2 = call_5571
func_5577 = relay.Function([], output)
mod['func_5577'] = func_5577
mod = relay.transform.InferType()(mod)
mutated_mod['func_5577'] = func_5577
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5577_call = mutated_mod.get_global_var('func_5577')
call_5578 = func_5577_call()
output = call_5578
func_5579 = relay.Function([], output)
mutated_mod['func_5579'] = func_5579
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3992_call = mod.get_global_var('func_3992')
func_3993_call = mutated_mod.get_global_var('func_3993')
call_5671 = relay.TupleGetItem(func_3992_call(), 0)
call_5672 = relay.TupleGetItem(func_3993_call(), 0)
output = call_5671
output2 = call_5672
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
func_1507_call = mod.get_global_var('func_1507')
func_1508_call = mutated_mod.get_global_var('func_1508')
call_5696 = func_1507_call()
call_5697 = func_1507_call()
output = call_5696
output2 = call_5697
func_5706 = relay.Function([], output)
mod['func_5706'] = func_5706
mod = relay.transform.InferType()(mod)
output = func_5706()
func_5707 = relay.Function([], output)
mutated_mod['func_5707'] = func_5707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4341_call = mod.get_global_var('func_4341')
func_4342_call = mutated_mod.get_global_var('func_4342')
call_5711 = relay.TupleGetItem(func_4341_call(), 0)
call_5712 = relay.TupleGetItem(func_4342_call(), 0)
output = call_5711
output2 = call_5712
func_5722 = relay.Function([], output)
mod['func_5722'] = func_5722
mod = relay.transform.InferType()(mod)
output = func_5722()
func_5723 = relay.Function([], output)
mutated_mod['func_5723'] = func_5723
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_5726 = func_196_call()
call_5727 = func_196_call()
func_4351_call = mod.get_global_var('func_4351')
func_4354_call = mutated_mod.get_global_var('func_4354')
const_5729 = relay.const([7.695716,-8.442860,-4.096826,-7.030187,-4.696656,4.890501,-7.079017,6.469354,-1.234839,4.227001,3.595600,-1.511137,-0.792900,6.787588,5.479059,-7.691870,3.839367,5.402368,-9.486142,0.174447,-7.237379,3.874236,-6.067275,3.864901,-7.000529,8.980614,-3.403902,-9.041659,2.443604,9.893494,-7.164907,-6.529022,-6.771994,3.115772,2.726916,9.728768,2.453291,8.268042,0.723186,-8.593140,4.877459,8.353252,9.724944,-8.528557,-5.394871,5.540264,-8.751239,-8.925681,0.531961,5.910053,-6.658877,-0.648617,5.453935,7.549915,0.375838,-6.441039,2.060452,-8.820572,5.891213,-2.462628,-8.030727,-3.533931,1.027911,-2.356183,-2.604558,0.188350,-3.898666,-4.866424,2.997201,6.399440,-0.787833,-7.148239,3.492769,-7.544553,4.936375,-0.050976,0.014941,-6.144090,5.079368,3.604809,9.629511,-4.057933,9.861698,8.955144,1.583487,7.317359,1.572127,7.225381,-5.414469,9.068230,-7.670709,-6.552982,1.255887,-8.486180,6.289130,-8.925831,4.989996,-1.891705,-4.567710,9.754360,-8.518150,6.702075,-5.019409,2.251620,-6.980409,7.218124,-5.592310,-6.794145,-8.092507,9.512560,5.912824,-9.771225,-9.994105,0.971089,4.791414,-3.018842,8.651559,5.089563,3.115971,-9.382894,4.978485,-2.504908,6.171187,4.705758,-0.232292,9.416000,0.590533,-1.240353,2.645345,-8.857962,-1.916464,-2.314595,-7.699323,-3.519332,-2.653527,6.477597,-5.737102,-4.935510,2.940730,0.817441,-1.885650,6.965976,2.403993,8.819139,9.553215,7.215462,6.677403,7.457581,6.019561,4.121498,-5.420835,7.921481,-5.994639,2.494276,-5.605167,6.304362,7.518816,-4.593507,-9.428372,8.536220,7.215658,-0.894789,3.807378,-5.229196,6.629585,-4.912386,-0.977924,-6.613482,8.266950,-8.912728,-0.036153,-5.355527,-3.737454,-0.923390,1.743249,-8.573071,-4.116692,5.738480,-7.231544,-3.104874,3.144569,-1.728119,7.241819,-6.358174,-1.085623,-2.222819,4.052597,-8.790425,6.716207,-9.083211,3.006733,3.141306,8.303018,6.212497,-6.366706,1.430562,-6.385234,6.045862,-5.034087,9.136447,6.339793,-5.545529,-1.821937,-6.987477,2.990736,-8.467734,-9.317807,0.423939,-8.852850,7.651828,-7.840747,-3.928610,-4.709760,-1.764927,-6.674218,1.826886,9.393963,-2.031355,1.466668,3.786426,4.994303,8.226004,5.913931,-0.697452,0.086799,-5.760176,-2.200687,-5.620838,6.360996,-9.439142,-5.508555,9.901278,1.326736,-4.001830,-2.873549,5.463044,2.953444,3.210124,1.384366,9.111484,-6.321072,4.729374,-9.341317,4.142107,-8.734711,9.586442,-5.019724,7.417880,-6.790677,-9.600798,3.505312,3.520304,-4.086069,-4.638311,-5.680211,-0.065729,4.601968,3.615403,8.804131,0.500605,-6.859801,9.331801,8.043332,-6.083549,-3.039607,9.998593,1.796859,-9.310247,0.316594,9.550780,-1.619896,-9.434187,4.747381,-9.742775,6.072031,0.987420,-3.764178,-3.446156,0.232133,-3.082553,6.969882,8.694426,-3.665454,-0.389691,-6.258805,9.353455,6.334156,9.764288], dtype = "float64")#candidate|5729|(288,)|const|float64
call_5728 = relay.TupleGetItem(func_4351_call(relay.reshape(const_5729.astype('float64'), [4, 8, 9])), 0)
call_5730 = relay.TupleGetItem(func_4354_call(relay.reshape(const_5729.astype('float64'), [4, 8, 9])), 0)
output = relay.Tuple([call_5726,call_5728,const_5729,])
output2 = relay.Tuple([call_5727,call_5730,const_5729,])
func_5735 = relay.Function([], output)
mod['func_5735'] = func_5735
mod = relay.transform.InferType()(mod)
mutated_mod['func_5735'] = func_5735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5735_call = mutated_mod.get_global_var('func_5735')
call_5736 = func_5735_call()
output = call_5736
func_5737 = relay.Function([], output)
mutated_mod['func_5737'] = func_5737
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5339_call = mod.get_global_var('func_5339')
func_5340_call = mutated_mod.get_global_var('func_5340')
call_5768 = relay.TupleGetItem(func_5339_call(), 0)
call_5769 = relay.TupleGetItem(func_5340_call(), 0)
var_5780 = relay.var("var_5780", dtype = "float64", shape = (7, 10, 2))#candidate|5780|(7, 10, 2)|var|float64
bop_5781 = relay.logical_or(call_5768.astype('bool'), relay.reshape(var_5780.astype('bool'), relay.shape_of(call_5768))) # shape=(7, 10, 2)
bop_5784 = relay.logical_or(call_5769.astype('bool'), relay.reshape(var_5780.astype('bool'), relay.shape_of(call_5769))) # shape=(7, 10, 2)
output = bop_5781
output2 = bop_5784
func_5786 = relay.Function([var_5780,], output)
mod['func_5786'] = func_5786
mod = relay.transform.InferType()(mod)
var_5787 = relay.var("var_5787", dtype = "float64", shape = (7, 10, 2))#candidate|5787|(7, 10, 2)|var|float64
output = func_5786(var_5787)
func_5788 = relay.Function([var_5787], output)
mutated_mod['func_5788'] = func_5788
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2386_call = mod.get_global_var('func_2386')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_5816 = func_2386_call()
call_5817 = func_2386_call()
output = relay.Tuple([call_5816,])
output2 = relay.Tuple([call_5817,])
func_5818 = relay.Function([], output)
mod['func_5818'] = func_5818
mod = relay.transform.InferType()(mod)
mutated_mod['func_5818'] = func_5818
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mutated_mod.get_global_var('func_5818')
call_5819 = func_5818_call()
output = call_5819
func_5820 = relay.Function([], output)
mutated_mod['func_5820'] = func_5820
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3865_call = mod.get_global_var('func_3865')
func_3867_call = mutated_mod.get_global_var('func_3867')
call_5853 = func_3865_call()
call_5854 = func_3865_call()
output = relay.Tuple([call_5853,])
output2 = relay.Tuple([call_5854,])
func_5855 = relay.Function([], output)
mod['func_5855'] = func_5855
mod = relay.transform.InferType()(mod)
mutated_mod['func_5855'] = func_5855
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5855_call = mutated_mod.get_global_var('func_5855')
call_5856 = func_5855_call()
output = call_5856
func_5857 = relay.Function([], output)
mutated_mod['func_5857'] = func_5857
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5935 = relay.var("var_5935", dtype = "int32", shape = (2, 1, 1))#candidate|5935|(2, 1, 1)|var|int32
var_5936 = relay.var("var_5936", dtype = "int32", shape = (2, 1, 7))#candidate|5936|(2, 1, 7)|var|int32
bop_5937 = relay.subtract(var_5935.astype('int32'), var_5936.astype('int32')) # shape=(2, 1, 7)
output = relay.Tuple([bop_5937,])
output2 = relay.Tuple([bop_5937,])
func_5944 = relay.Function([var_5935,var_5936,], output)
mod['func_5944'] = func_5944
mod = relay.transform.InferType()(mod)
var_5945 = relay.var("var_5945", dtype = "int32", shape = (2, 1, 1))#candidate|5945|(2, 1, 1)|var|int32
var_5946 = relay.var("var_5946", dtype = "int32", shape = (2, 1, 7))#candidate|5946|(2, 1, 7)|var|int32
output = func_5944(var_5945,var_5946,)
func_5947 = relay.Function([var_5945,var_5946,], output)
mutated_mod['func_5947'] = func_5947
mutated_mod = relay.transform.InferType()(mutated_mod)
func_941_call = mod.get_global_var('func_941')
func_942_call = mutated_mod.get_global_var('func_942')
call_5957 = relay.TupleGetItem(func_941_call(), 0)
call_5958 = relay.TupleGetItem(func_942_call(), 0)
output = call_5957
output2 = call_5958
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
var_5973 = relay.var("var_5973", dtype = "float32", shape = (8, 15, 8))#candidate|5973|(8, 15, 8)|var|float32
var_5974 = relay.var("var_5974", dtype = "float32", shape = (8, 15, 8))#candidate|5974|(8, 15, 8)|var|float32
bop_5975 = relay.floor_mod(var_5973.astype('float32'), relay.reshape(var_5974.astype('float32'), relay.shape_of(var_5973))) # shape=(8, 15, 8)
uop_5978 = relay.atan(bop_5975.astype('float64')) # shape=(8, 15, 8)
uop_5985 = relay.log10(uop_5978.astype('float32')) # shape=(8, 15, 8)
func_4265_call = mod.get_global_var('func_4265')
func_4268_call = mutated_mod.get_global_var('func_4268')
const_5991 = relay.const([-3.535775,-3.966192,-7.635600,6.016264,8.414032,-4.402464,-0.684701,-7.369762,-8.922730,-4.230609,7.605905,-0.513944,8.590441,2.558208,-4.584395,1.188330,-2.950964,-2.746494,4.097040,9.797898,-6.824967,6.342090,-1.391078,-3.397684,-1.079340,6.746306,-8.657240,4.234779,4.995796,-2.828887,3.071838,-8.604930,-5.327240,6.584557,-3.929076,-7.444922,-8.773369,5.520539,8.766893,0.121780,-2.873420,6.919106,4.201445,4.758668,-7.172656,-1.240349,7.868894,0.760655,2.083896,8.155443,9.160137,-9.405616,-5.658057,9.625854,6.901193,6.802155,5.116024,2.397437,5.438037,0.643793,-9.479599,-1.006963,-1.913857,1.186749,-0.525464,1.330362,-6.983338,2.902380,9.594790,-4.830879,4.773352,1.300709,4.452364,8.779376,3.504478,-5.240792,-7.390380,4.503387,-8.918868,4.300862,8.216671,7.617430,-8.777865,-4.384783,4.490222,9.924420,-5.046575,3.570985,9.091412,3.247340,1.997643,-4.076553,-5.190569,-1.231712,3.809490,2.554959,-0.650651,-3.779269,7.512815,-6.803077,-3.833371,8.588311,-2.325211,-4.673303,-9.144413,-1.122020,1.208146,3.151348], dtype = "float32")#candidate|5991|(108,)|const|float32
call_5990 = relay.TupleGetItem(func_4265_call(relay.reshape(const_5991.astype('float32'), [108,])), 2)
call_5992 = relay.TupleGetItem(func_4268_call(relay.reshape(const_5991.astype('float32'), [108,])), 2)
output = relay.Tuple([uop_5985,call_5990,const_5991,])
output2 = relay.Tuple([uop_5985,call_5992,const_5991,])
func_6014 = relay.Function([var_5973,var_5974,], output)
mod['func_6014'] = func_6014
mod = relay.transform.InferType()(mod)
mutated_mod['func_6014'] = func_6014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6014_call = mutated_mod.get_global_var('func_6014')
var_6016 = relay.var("var_6016", dtype = "float32", shape = (8, 15, 8))#candidate|6016|(8, 15, 8)|var|float32
var_6017 = relay.var("var_6017", dtype = "float32", shape = (8, 15, 8))#candidate|6017|(8, 15, 8)|var|float32
call_6015 = func_6014_call(var_6016,var_6017,)
output = call_6015
func_6018 = relay.Function([var_6016,var_6017,], output)
mutated_mod['func_6018'] = func_6018
mutated_mod = relay.transform.InferType()(mutated_mod)
func_203_call = mod.get_global_var('func_203')
func_204_call = mutated_mod.get_global_var('func_204')
call_6061 = func_203_call()
call_6062 = func_203_call()
output = call_6061
output2 = call_6062
func_6063 = relay.Function([], output)
mod['func_6063'] = func_6063
mod = relay.transform.InferType()(mod)
output = func_6063()
func_6064 = relay.Function([], output)
mutated_mod['func_6064'] = func_6064
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2836_call = mod.get_global_var('func_2836')
func_2838_call = mutated_mod.get_global_var('func_2838')
call_6068 = func_2836_call()
call_6069 = func_2836_call()
uop_6085 = relay.sin(call_6068.astype('float64')) # shape=(7, 10, 2)
uop_6087 = relay.sin(call_6069.astype('float64')) # shape=(7, 10, 2)
output = uop_6085
output2 = uop_6087
func_6102 = relay.Function([], output)
mod['func_6102'] = func_6102
mod = relay.transform.InferType()(mod)
output = func_6102()
func_6103 = relay.Function([], output)
mutated_mod['func_6103'] = func_6103
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6117 = relay.var("var_6117", dtype = "float64", shape = (9, 12, 13))#candidate|6117|(9, 12, 13)|var|float64
uop_6118 = relay.rsqrt(var_6117.astype('float64')) # shape=(9, 12, 13)
uop_6125 = relay.tan(uop_6118.astype('float64')) # shape=(9, 12, 13)
bop_6127 = relay.bitwise_or(uop_6125.astype('uint16'), relay.reshape(uop_6118.astype('uint16'), relay.shape_of(uop_6125))) # shape=(9, 12, 13)
output = relay.Tuple([bop_6127,])
output2 = relay.Tuple([bop_6127,])
func_6130 = relay.Function([var_6117,], output)
mod['func_6130'] = func_6130
mod = relay.transform.InferType()(mod)
mutated_mod['func_6130'] = func_6130
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6131 = relay.var("var_6131", dtype = "float64", shape = (9, 12, 13))#candidate|6131|(9, 12, 13)|var|float64
func_6130_call = mutated_mod.get_global_var('func_6130')
call_6132 = func_6130_call(var_6131)
output = call_6132
func_6133 = relay.Function([var_6131], output)
mutated_mod['func_6133'] = func_6133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4009_call = mod.get_global_var('func_4009')
func_4010_call = mutated_mod.get_global_var('func_4010')
call_6176 = func_4009_call()
call_6177 = func_4009_call()
func_2635_call = mod.get_global_var('func_2635')
func_2636_call = mutated_mod.get_global_var('func_2636')
call_6224 = func_2635_call()
call_6225 = func_2635_call()
output = relay.Tuple([call_6176,call_6224,])
output2 = relay.Tuple([call_6177,call_6225,])
func_6243 = relay.Function([], output)
mod['func_6243'] = func_6243
mod = relay.transform.InferType()(mod)
mutated_mod['func_6243'] = func_6243
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6243_call = mutated_mod.get_global_var('func_6243')
call_6244 = func_6243_call()
output = call_6244
func_6245 = relay.Function([], output)
mutated_mod['func_6245'] = func_6245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4120_call = mod.get_global_var('func_4120')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_6282 = relay.TupleGetItem(func_4120_call(), 0)
call_6283 = relay.TupleGetItem(func_4121_call(), 0)
func_2069_call = mod.get_global_var('func_2069')
func_2071_call = mutated_mod.get_global_var('func_2071')
var_6296 = relay.var("var_6296", dtype = "float64", shape = (140,))#candidate|6296|(140,)|var|float64
call_6295 = relay.TupleGetItem(func_2069_call(relay.reshape(var_6296.astype('float64'), [7, 10, 2])), 2)
call_6297 = relay.TupleGetItem(func_2071_call(relay.reshape(var_6296.astype('float64'), [7, 10, 2])), 2)
func_5735_call = mod.get_global_var('func_5735')
func_5737_call = mutated_mod.get_global_var('func_5737')
call_6305 = relay.TupleGetItem(func_5735_call(), 2)
call_6306 = relay.TupleGetItem(func_5737_call(), 2)
output = relay.Tuple([call_6282,call_6295,var_6296,call_6305,])
output2 = relay.Tuple([call_6283,call_6297,var_6296,call_6306,])
func_6307 = relay.Function([var_6296,], output)
mod['func_6307'] = func_6307
mod = relay.transform.InferType()(mod)
mutated_mod['func_6307'] = func_6307
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6308 = relay.var("var_6308", dtype = "float64", shape = (140,))#candidate|6308|(140,)|var|float64
func_6307_call = mutated_mod.get_global_var('func_6307')
call_6309 = func_6307_call(var_6308)
output = call_6309
func_6310 = relay.Function([var_6308], output)
mutated_mod['func_6310'] = func_6310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_861_call = mod.get_global_var('func_861')
func_863_call = mutated_mod.get_global_var('func_863')
call_6329 = relay.TupleGetItem(func_861_call(), 0)
call_6330 = relay.TupleGetItem(func_863_call(), 0)
func_912_call = mod.get_global_var('func_912')
func_913_call = mutated_mod.get_global_var('func_913')
call_6362 = relay.TupleGetItem(func_912_call(), 0)
call_6363 = relay.TupleGetItem(func_913_call(), 0)
func_4120_call = mod.get_global_var('func_4120')
func_4121_call = mutated_mod.get_global_var('func_4121')
call_6369 = relay.TupleGetItem(func_4120_call(), 1)
call_6370 = relay.TupleGetItem(func_4121_call(), 1)
func_5855_call = mod.get_global_var('func_5855')
func_5857_call = mutated_mod.get_global_var('func_5857')
call_6383 = relay.TupleGetItem(func_5855_call(), 0)
call_6384 = relay.TupleGetItem(func_5857_call(), 0)
output = relay.Tuple([call_6329,call_6362,call_6369,call_6383,])
output2 = relay.Tuple([call_6330,call_6363,call_6370,call_6384,])
func_6390 = relay.Function([], output)
mod['func_6390'] = func_6390
mod = relay.transform.InferType()(mod)
output = func_6390()
func_6391 = relay.Function([], output)
mutated_mod['func_6391'] = func_6391
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mod.get_global_var('func_4854')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_6545 = relay.TupleGetItem(func_4854_call(), 2)
call_6546 = relay.TupleGetItem(func_4856_call(), 2)
output = relay.Tuple([call_6545,])
output2 = relay.Tuple([call_6546,])
func_6596 = relay.Function([], output)
mod['func_6596'] = func_6596
mod = relay.transform.InferType()(mod)
mutated_mod['func_6596'] = func_6596
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6596_call = mutated_mod.get_global_var('func_6596')
call_6597 = func_6596_call()
output = call_6597
func_6598 = relay.Function([], output)
mutated_mod['func_6598'] = func_6598
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5531_call = mod.get_global_var('func_5531')
func_5532_call = mutated_mod.get_global_var('func_5532')
call_6640 = relay.TupleGetItem(func_5531_call(), 0)
call_6641 = relay.TupleGetItem(func_5532_call(), 0)
output = relay.Tuple([call_6640,])
output2 = relay.Tuple([call_6641,])
func_6642 = relay.Function([], output)
mod['func_6642'] = func_6642
mod = relay.transform.InferType()(mod)
output = func_6642()
func_6643 = relay.Function([], output)
mutated_mod['func_6643'] = func_6643
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6652 = relay.var("var_6652", dtype = "int8", shape = (10, 1))#candidate|6652|(10, 1)|var|int8
var_6653 = relay.var("var_6653", dtype = "int8", shape = (10, 1))#candidate|6653|(10, 1)|var|int8
bop_6654 = relay.bitwise_xor(var_6652.astype('int8'), relay.reshape(var_6653.astype('int8'), relay.shape_of(var_6652))) # shape=(10, 1)
func_1125_call = mod.get_global_var('func_1125')
func_1127_call = mutated_mod.get_global_var('func_1127')
var_6676 = relay.var("var_6676", dtype = "float64", shape = (44,))#candidate|6676|(44,)|var|float64
call_6675 = relay.TupleGetItem(func_1125_call(relay.reshape(var_6676.astype('float64'), [44,])), 1)
call_6677 = relay.TupleGetItem(func_1127_call(relay.reshape(var_6676.astype('float64'), [44,])), 1)
output = relay.Tuple([bop_6654,call_6675,var_6676,])
output2 = relay.Tuple([bop_6654,call_6677,var_6676,])
func_6694 = relay.Function([var_6652,var_6653,var_6676,], output)
mod['func_6694'] = func_6694
mod = relay.transform.InferType()(mod)
mutated_mod['func_6694'] = func_6694
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6694_call = mutated_mod.get_global_var('func_6694')
var_6696 = relay.var("var_6696", dtype = "int8", shape = (10, 1))#candidate|6696|(10, 1)|var|int8
var_6697 = relay.var("var_6697", dtype = "int8", shape = (10, 1))#candidate|6697|(10, 1)|var|int8
var_6698 = relay.var("var_6698", dtype = "float64", shape = (44,))#candidate|6698|(44,)|var|float64
call_6695 = func_6694_call(var_6696,var_6697,var_6698,)
output = call_6695
func_6699 = relay.Function([var_6696,var_6697,var_6698,], output)
mutated_mod['func_6699'] = func_6699
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6714 = relay.var("var_6714", dtype = "float32", shape = (8, 7, 2))#candidate|6714|(8, 7, 2)|var|float32
var_6715 = relay.var("var_6715", dtype = "float32", shape = (8, 7, 2))#candidate|6715|(8, 7, 2)|var|float32
bop_6716 = relay.power(var_6714.astype('float32'), relay.reshape(var_6715.astype('float32'), relay.shape_of(var_6714))) # shape=(8, 7, 2)
func_3610_call = mod.get_global_var('func_3610')
func_3614_call = mutated_mod.get_global_var('func_3614')
var_6722 = relay.var("var_6722", dtype = "float64", shape = (140,))#candidate|6722|(140,)|var|float64
var_6723 = relay.var("var_6723", dtype = "uint8", shape = (35,))#candidate|6723|(35,)|var|uint8
var_6724 = relay.var("var_6724", dtype = "float64", shape = (44,))#candidate|6724|(44,)|var|float64
call_6721 = relay.TupleGetItem(func_3610_call(relay.reshape(var_6722.astype('float64'), [7, 10, 2]), relay.reshape(var_6723.astype('uint8'), [35,]), relay.reshape(var_6724.astype('float64'), [44,]), ), 4)
call_6725 = relay.TupleGetItem(func_3614_call(relay.reshape(var_6722.astype('float64'), [7, 10, 2]), relay.reshape(var_6723.astype('uint8'), [35,]), relay.reshape(var_6724.astype('float64'), [44,]), ), 4)
func_3488_call = mod.get_global_var('func_3488')
func_3490_call = mutated_mod.get_global_var('func_3490')
call_6729 = relay.TupleGetItem(func_3488_call(), 0)
call_6730 = relay.TupleGetItem(func_3490_call(), 0)
const_6731 = relay.const([[[0.498654,-7.748731],[1.826108,-1.964514],[2.444989,-8.871868],[9.174665,-4.339484],[0.074864,8.326288],[1.496602,0.031072],[-4.565831,3.509461]],[[-1.708276,7.667117],[5.566664,-4.055374],[-1.249716,7.695166],[-5.376572,6.214274],[8.993160,-6.935171],[-8.141265,5.278221],[-3.186544,-6.824655]],[[-9.953312,-9.625420],[-6.610327,9.049753],[2.218238,8.103408],[-2.409202,-5.138900],[-0.844318,-3.207688],[2.538429,-7.786187],[-3.332026,6.455923]],[[8.561095,2.411856],[4.007947,-5.292607],[0.667515,4.129130],[-4.627212,-9.248626],[-9.136650,1.333346],[-1.416887,-3.329241],[3.305650,9.371373]],[[-7.742669,-8.683431],[-5.772646,-6.596890],[9.193984,-8.858189],[-2.253546,-3.864486],[-4.811524,8.918691],[0.168621,4.366712],[-1.577658,1.286679]],[[-0.998046,3.744436],[0.229400,-8.225047],[6.143051,7.879108],[-0.483926,3.200110],[-7.959951,0.230890],[-1.149352,1.976119],[4.915515,7.260270]],[[-6.819694,9.028444],[5.606318,2.699403],[7.623051,2.503693],[-3.264889,1.362994],[-9.505442,1.601547],[-1.392332,0.996421],[4.889343,-4.213482]],[[3.196900,-6.659130],[-0.850950,-5.647303],[-7.141614,-5.764951],[-4.478939,-2.185384],[1.327348,4.505498],[-3.729664,-8.854463],[0.945274,0.443996]]], dtype = "float32")#candidate|6731|(8, 7, 2)|const|float32
bop_6732 = relay.less(var_6715.astype('bool'), relay.reshape(const_6731.astype('bool'), relay.shape_of(var_6715))) # shape=(8, 7, 2)
func_3256_call = mod.get_global_var('func_3256')
func_3257_call = mutated_mod.get_global_var('func_3257')
call_6745 = relay.TupleGetItem(func_3256_call(), 0)
call_6746 = relay.TupleGetItem(func_3257_call(), 0)
output = relay.Tuple([bop_6716,call_6721,var_6722,var_6723,var_6724,call_6729,bop_6732,call_6745,])
output2 = relay.Tuple([bop_6716,call_6725,var_6722,var_6723,var_6724,call_6730,bop_6732,call_6746,])
func_6759 = relay.Function([var_6714,var_6715,var_6722,var_6723,var_6724,], output)
mod['func_6759'] = func_6759
mod = relay.transform.InferType()(mod)
mutated_mod['func_6759'] = func_6759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6759_call = mutated_mod.get_global_var('func_6759')
var_6761 = relay.var("var_6761", dtype = "float32", shape = (8, 7, 2))#candidate|6761|(8, 7, 2)|var|float32
var_6762 = relay.var("var_6762", dtype = "float32", shape = (8, 7, 2))#candidate|6762|(8, 7, 2)|var|float32
var_6763 = relay.var("var_6763", dtype = "float64", shape = (140,))#candidate|6763|(140,)|var|float64
var_6764 = relay.var("var_6764", dtype = "uint8", shape = (35,))#candidate|6764|(35,)|var|uint8
var_6765 = relay.var("var_6765", dtype = "float64", shape = (44,))#candidate|6765|(44,)|var|float64
call_6760 = func_6759_call(var_6761,var_6762,var_6763,var_6764,var_6765,)
output = call_6760
func_6766 = relay.Function([var_6761,var_6762,var_6763,var_6764,var_6765,], output)
mutated_mod['func_6766'] = func_6766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5820_call = mutated_mod.get_global_var('func_5820')
call_6776 = relay.TupleGetItem(func_5818_call(), 0)
call_6777 = relay.TupleGetItem(func_5820_call(), 0)
output = call_6776
output2 = call_6777
func_6781 = relay.Function([], output)
mod['func_6781'] = func_6781
mod = relay.transform.InferType()(mod)
output = func_6781()
func_6782 = relay.Function([], output)
mutated_mod['func_6782'] = func_6782
mutated_mod = relay.transform.InferType()(mutated_mod)
const_6813 = relay.const([[[4.437652,7.928481,5.436623,-0.036269,7.256290,-5.424550,-6.253236,1.475637,5.942918,3.837562,1.379045,1.124850,-1.345330,-4.415277],[3.796963,9.203135,-0.679888,-3.752619,9.242802,9.264549,4.588865,0.008467,-8.584198,7.453895,-8.450593,6.966389,-4.684493,-2.947651],[9.253013,5.376946,-7.199339,3.656819,-3.302179,-0.002727,-3.345183,-1.467952,-6.907227,9.461556,5.549502,-4.693680,7.446961,2.325983],[-1.451525,-1.659882,-6.312117,4.410182,-1.722331,9.570486,-6.627067,-2.809863,-6.360028,-9.914008,-8.510008,3.453359,-2.322888,1.373975],[6.775464,-3.802777,-1.568809,1.750428,-1.504637,-6.141032,4.406091,6.572144,1.641033,-1.276775,4.308496,-4.879801,-1.487720,0.139042],[5.847943,-4.305425,9.359261,4.035490,7.915248,-9.543503,3.122983,-6.384698,-8.845824,-5.850028,5.765837,0.315150,1.490238,-0.489706],[1.950491,-4.116033,-3.169867,-4.688534,4.157885,-9.015488,-3.954443,6.601029,1.907958,6.418315,1.472903,0.064593,-3.609260,5.428708],[4.380848,-9.776551,6.093262,2.494205,3.459758,5.686675,1.155504,-2.849391,-2.681743,5.949452,0.394986,-6.804140,-3.256271,-7.645632]],[[-4.831986,-7.525143,5.318027,9.626384,-0.911594,8.327995,-7.227807,-7.925514,-8.100405,7.998778,-9.482652,-1.561818,5.594804,7.036732],[-5.377465,0.692773,8.482981,-5.518726,-9.358564,-6.132517,3.405939,-4.522787,-0.872453,3.105059,9.165182,-0.786088,-2.440750,-4.487257],[2.377463,4.818860,1.250535,-3.715322,8.835314,0.357425,-7.725968,-1.715103,5.859876,4.389614,9.019600,-1.545112,-3.503042,3.036444],[9.346557,-0.374641,8.524759,8.214676,-3.593009,9.470865,-6.334069,3.930388,-5.449497,-5.593720,8.475206,-1.259459,7.223501,0.185987],[3.089255,-1.015280,-2.303091,7.375699,-3.922530,-9.654101,-7.427430,-9.233721,3.200049,-9.062042,4.722919,6.664059,-8.372271,-0.562396],[1.692952,4.034034,-0.194373,6.531808,1.956540,-3.702806,1.892934,-1.013836,-8.315276,2.518343,1.831953,-3.732111,-1.278041,4.038409],[7.763551,-9.110065,3.204280,3.611742,8.028144,7.577766,5.713389,4.773088,-7.537777,-2.876397,-3.539556,-0.833290,1.943690,4.666895],[6.819639,7.988928,-9.774118,5.553570,8.852780,1.341489,4.557789,5.236073,-7.028042,-3.183507,0.161910,9.341417,-1.179257,1.231445]],[[-5.289693,5.596363,5.533472,-7.944487,0.806242,1.210881,-2.059447,7.585511,8.187061,-1.694829,4.975509,6.216262,-1.462261,3.150813],[-5.937588,-0.913871,8.312727,-0.027388,-7.297211,-2.806867,-7.285151,5.384251,-4.453749,0.456682,5.314013,4.278712,-2.114803,7.838816],[0.367606,3.734329,1.478856,6.981490,1.892490,6.399206,-9.624416,7.633890,-2.878681,-0.525321,-5.152273,-1.785850,3.376586,-8.651032],[-2.789516,-8.224033,-4.688460,-1.824049,-9.855641,-7.438974,8.655143,0.213086,7.494983,1.609289,0.347064,-8.913684,6.628857,-9.271248],[-3.677561,-2.533323,-0.500755,8.483956,-4.033321,4.809613,4.031996,-0.384506,9.156395,-8.777763,1.647485,-9.259857,9.334995,-1.196742],[-0.058416,-5.600967,1.125493,3.521043,8.559001,4.510107,-3.288207,-4.804472,-9.229262,3.021055,3.520541,8.583662,3.595662,6.261249],[-8.299625,3.330829,-1.265084,-2.397576,-4.756076,-0.511516,-2.824445,3.116404,-2.278741,-2.611060,-6.560021,-0.451888,5.379401,-7.821488],[-4.937591,-0.212172,0.502074,1.540092,2.996102,-5.669930,4.649006,5.571045,-2.227489,6.545861,6.416526,4.531081,9.945332,3.697963]],[[9.600984,1.672772,4.976740,2.657373,3.281153,8.175523,-2.010625,-5.743991,-6.700085,3.219289,-8.124053,9.209521,-5.525644,4.515309],[-1.259060,-5.480494,6.330379,7.359916,3.025576,6.417486,2.921821,1.211449,-3.912819,-7.953954,-3.119220,7.785198,-8.377851,-2.313910],[-4.932880,-6.766581,-4.915135,-3.061395,-7.042451,-8.640635,-2.724890,-4.115026,-8.839771,5.320667,6.425174,1.986361,8.717627,-2.325986],[4.946722,-1.945711,-8.917692,6.829095,-4.751419,-5.312638,2.892161,-7.067535,6.088354,-2.931015,8.729687,-4.207521,8.810757,-1.439213],[7.915755,-1.839771,2.981015,-9.296640,1.740626,-0.612402,2.353162,-0.627413,2.353291,9.557162,3.058999,6.434239,1.296957,7.186819],[9.066529,-4.597702,-2.544530,-8.738104,0.434142,2.292975,-3.654071,-4.532346,4.017441,-0.697030,-7.472163,4.748617,2.111753,-2.703410],[-1.875952,0.901552,6.857633,-1.364126,-5.144859,1.118293,9.691307,-4.837071,-2.098177,-5.280954,0.267461,-2.067609,-2.794740,7.373935],[-2.088540,-3.653013,8.729626,1.398054,0.679969,-3.478011,-4.524772,-8.793761,7.778952,9.606088,0.263107,7.833038,-4.794138,-9.725115]],[[2.012004,2.843340,1.996401,-5.505427,0.444117,5.219295,-6.223053,8.375077,8.217912,-2.306176,-3.072549,-7.500659,3.024866,4.918820],[-3.810609,-5.459343,7.184335,9.761929,-3.755464,-9.144877,7.871629,-7.910484,5.680531,-9.210761,2.562634,6.622024,-2.470570,-5.946356],[3.141375,-6.226894,3.187810,1.148852,-1.441361,-9.746976,6.560550,-5.872231,-6.310149,-7.051771,-5.517597,7.479723,3.078682,-9.266224],[-1.447703,-3.490833,-1.007612,6.444253,1.101698,-7.576906,-4.162787,-3.489752,0.976757,-9.006706,-2.424015,-2.853340,-3.931230,-7.905752],[-8.297777,5.907283,1.549301,1.470789,-7.781514,-0.313962,0.053052,5.763041,8.075249,4.863584,6.180552,-2.466371,-1.833821,-5.940958],[-4.773920,6.195885,9.585388,-4.779586,-8.202255,-4.374647,-3.268338,-5.098980,-8.707834,7.605612,-4.420064,-3.862164,4.879358,3.806514],[4.461098,-1.945884,-1.013170,6.407319,-7.508222,1.340986,4.314655,-4.575749,-2.733742,5.281392,-7.943122,-4.461179,-8.246630,-6.822957],[9.841187,4.356074,-8.218258,9.025954,5.784304,-8.811365,-5.220116,-0.249161,-3.121878,4.956436,-9.359037,1.129808,-3.512756,0.241449]]], dtype = "float32")#candidate|6813|(5, 8, 14)|const|float32
uop_6814 = relay.rsqrt(const_6813.astype('float32')) # shape=(5, 8, 14)
output = relay.Tuple([uop_6814,])
output2 = relay.Tuple([uop_6814,])
func_6825 = relay.Function([], output)
mod['func_6825'] = func_6825
mod = relay.transform.InferType()(mod)
output = func_6825()
func_6826 = relay.Function([], output)
mutated_mod['func_6826'] = func_6826
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6835 = relay.var("var_6835", dtype = "bool", shape = (6, 12, 6))#candidate|6835|(6, 12, 6)|var|bool
var_6836 = relay.var("var_6836", dtype = "bool", shape = (6, 12, 6))#candidate|6836|(6, 12, 6)|var|bool
bop_6837 = relay.logical_and(var_6835.astype('bool'), relay.reshape(var_6836.astype('bool'), relay.shape_of(var_6835))) # shape=(6, 12, 6)
uop_6847 = relay.rsqrt(var_6836.astype('float32')) # shape=(6, 12, 6)
output = relay.Tuple([bop_6837,uop_6847,])
output2 = relay.Tuple([bop_6837,uop_6847,])
func_6859 = relay.Function([var_6835,var_6836,], output)
mod['func_6859'] = func_6859
mod = relay.transform.InferType()(mod)
mutated_mod['func_6859'] = func_6859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6859_call = mutated_mod.get_global_var('func_6859')
var_6861 = relay.var("var_6861", dtype = "bool", shape = (6, 12, 6))#candidate|6861|(6, 12, 6)|var|bool
var_6862 = relay.var("var_6862", dtype = "bool", shape = (6, 12, 6))#candidate|6862|(6, 12, 6)|var|bool
call_6860 = func_6859_call(var_6861,var_6862,)
output = call_6860
func_6863 = relay.Function([var_6861,var_6862,], output)
mutated_mod['func_6863'] = func_6863
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4854_call = mod.get_global_var('func_4854')
func_4856_call = mutated_mod.get_global_var('func_4856')
call_6869 = relay.TupleGetItem(func_4854_call(), 3)
call_6870 = relay.TupleGetItem(func_4856_call(), 3)
func_759_call = mod.get_global_var('func_759')
func_761_call = mutated_mod.get_global_var('func_761')
call_6873 = relay.TupleGetItem(func_759_call(), 0)
call_6874 = relay.TupleGetItem(func_761_call(), 0)
output = relay.Tuple([call_6869,call_6873,])
output2 = relay.Tuple([call_6870,call_6874,])
func_6877 = relay.Function([], output)
mod['func_6877'] = func_6877
mod = relay.transform.InferType()(mod)
output = func_6877()
func_6878 = relay.Function([], output)
mutated_mod['func_6878'] = func_6878
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3041_call = mod.get_global_var('func_3041')
func_3042_call = mutated_mod.get_global_var('func_3042')
call_7060 = relay.TupleGetItem(func_3041_call(), 0)
call_7061 = relay.TupleGetItem(func_3042_call(), 0)
output = relay.Tuple([call_7060,])
output2 = relay.Tuple([call_7061,])
func_7074 = relay.Function([], output)
mod['func_7074'] = func_7074
mod = relay.transform.InferType()(mod)
output = func_7074()
func_7075 = relay.Function([], output)
mutated_mod['func_7075'] = func_7075
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7183 = relay.const([[-0.463306,-1.638982,-8.945723],[-5.427237,1.624397,9.972267],[-6.153350,1.886274,8.827360],[5.102405,-2.564906,-3.433133],[7.646323,-7.548162,6.989838],[9.717657,-1.163260,-3.274961],[-2.105269,-2.531430,-0.427006],[-9.037834,1.969489,1.312715],[3.488729,1.392981,-1.419916],[7.023621,-0.244155,-3.124401],[-0.392272,2.612614,-9.843081]], dtype = "float32")#candidate|7183|(11, 3)|const|float32
uop_7184 = relay.sin(const_7183.astype('float32')) # shape=(11, 3)
func_3610_call = mod.get_global_var('func_3610')
func_3614_call = mutated_mod.get_global_var('func_3614')
const_7189 = relay.const([[-1.097008,7.713437,-9.586732,-4.858040,8.348498,-1.000940,2.607945,5.727368,-0.918106,-2.699757,-0.375260,3.020451,-7.741527,1.908948,9.071010,8.216787,-8.670344,-7.547374,-0.084448,9.813384,0.858176,8.390334,4.574267,9.027442,-5.232196,-9.764201,3.719172,2.467692,8.395721,-2.679096,5.597202,-8.934266,-3.046599,-1.693093,-7.533128,-4.883834,2.973809,-1.343892,-8.725573,-7.661608,9.781325,-5.774398,2.115629,-6.269200,-1.789036,3.607867,-6.475362,-5.997105,-9.017349,4.820842,-7.526741,-5.536869,2.090907,5.143029,-3.325438,-2.470404,-5.222897,-8.394151,-0.365145,-7.792128,4.505940,-6.544413,-6.639441,-6.469182,0.326471,1.011914,-8.698718,0.982370,-7.983626,0.025693,1.844204,-0.691192,-3.861009,6.381584,3.548625,-4.759148,5.763683,-8.965590,6.312879,3.897850,9.869412,-0.870045,-9.054420,6.512065,-4.630201,-7.939984,1.607401,-6.856052,6.725466,-3.215975,2.700469,-3.821326,-9.493715,-9.889760,6.887964,-1.929925,-2.629943,-2.483063,8.692574,5.724299,9.127732,8.357703,-5.507942,-2.929364,5.558329,-0.042933,8.107646,3.580597,-4.004847,0.083463,6.522122,-5.737612,6.797131,3.455729,-7.328006,-9.180519,-4.038491,-7.906906,6.603026,-1.982713,-9.199010,-3.338766,3.612748,0.796383,7.636534,-0.784809,-2.691822,3.186427,0.284580,-3.597971,1.673699,6.483755,-4.725885,8.062435,7.629769,-7.153235,-2.446679,0.705397,6.563016,5.692249]], dtype = "float64")#candidate|7189|(1, 140)|const|float64
var_7190 = relay.var("var_7190", dtype = "uint8", shape = (35,))#candidate|7190|(35,)|var|uint8
var_7191 = relay.var("var_7191", dtype = "float64", shape = (1, 44))#candidate|7191|(1, 44)|var|float64
call_7188 = relay.TupleGetItem(func_3610_call(relay.reshape(const_7189.astype('float64'), [7, 10, 2]), relay.reshape(var_7190.astype('uint8'), [35,]), relay.reshape(var_7191.astype('float64'), [44,]), ), 3)
call_7192 = relay.TupleGetItem(func_3614_call(relay.reshape(const_7189.astype('float64'), [7, 10, 2]), relay.reshape(var_7190.astype('uint8'), [35,]), relay.reshape(var_7191.astype('float64'), [44,]), ), 3)
func_3198_call = mod.get_global_var('func_3198')
func_3201_call = mutated_mod.get_global_var('func_3201')
call_7196 = relay.TupleGetItem(func_3198_call(relay.reshape(const_7189.astype('float64'), [7, 10, 2])), 0)
call_7197 = relay.TupleGetItem(func_3201_call(relay.reshape(const_7189.astype('float64'), [7, 10, 2])), 0)
output = relay.Tuple([uop_7184,call_7188,const_7189,var_7190,var_7191,call_7196,])
output2 = relay.Tuple([uop_7184,call_7192,const_7189,var_7190,var_7191,call_7197,])
func_7204 = relay.Function([var_7190,var_7191,], output)
mod['func_7204'] = func_7204
mod = relay.transform.InferType()(mod)
var_7205 = relay.var("var_7205", dtype = "uint8", shape = (35,))#candidate|7205|(35,)|var|uint8
var_7206 = relay.var("var_7206", dtype = "float64", shape = (1, 44))#candidate|7206|(1, 44)|var|float64
output = func_7204(var_7205,var_7206,)
func_7207 = relay.Function([var_7205,var_7206,], output)
mutated_mod['func_7207'] = func_7207
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1629_call = mod.get_global_var('func_1629')
func_1631_call = mutated_mod.get_global_var('func_1631')
call_7238 = relay.TupleGetItem(func_1629_call(), 0)
call_7239 = relay.TupleGetItem(func_1631_call(), 0)
func_459_call = mod.get_global_var('func_459')
func_461_call = mutated_mod.get_global_var('func_461')
const_7257 = relay.const([-3.297200,8.713203,5.704347,-0.030979,-4.099928,1.660412,-3.060078,8.619881,9.094952,7.538821,-9.033848,-3.485719,6.321070,0.484124,-2.064130,5.238771,-2.852688,2.406470,7.182904,7.067547,-6.432540,-4.808709,6.894000,-5.355409,-2.179315,-3.138240,4.376410,-5.068775,3.680489,-3.397628,-7.344915,-2.085281,-1.820015,0.948543,-3.444835,9.571860,8.993709,8.913220,-7.108320,-2.904684,3.179741,8.256550,4.942144,-3.408343], dtype = "float64")#candidate|7257|(44,)|const|float64
call_7256 = func_459_call(relay.reshape(const_7257.astype('float64'), [1, 4, 11]))
call_7258 = func_459_call(relay.reshape(const_7257.astype('float64'), [1, 4, 11]))
uop_7261 = relay.acosh(const_7257.astype('float64')) # shape=(44,)
output = relay.Tuple([call_7238,call_7256,uop_7261,])
output2 = relay.Tuple([call_7239,call_7258,uop_7261,])
func_7263 = relay.Function([], output)
mod['func_7263'] = func_7263
mod = relay.transform.InferType()(mod)
mutated_mod['func_7263'] = func_7263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7263_call = mutated_mod.get_global_var('func_7263')
call_7264 = func_7263_call()
output = call_7264
func_7265 = relay.Function([], output)
mutated_mod['func_7265'] = func_7265
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1646_call = mod.get_global_var('func_1646')
func_1647_call = mutated_mod.get_global_var('func_1647')
call_7266 = relay.TupleGetItem(func_1646_call(), 0)
call_7267 = relay.TupleGetItem(func_1647_call(), 0)
func_2934_call = mod.get_global_var('func_2934')
func_2936_call = mutated_mod.get_global_var('func_2936')
call_7275 = relay.TupleGetItem(func_2934_call(relay.reshape(call_7266.astype('float64'), [7, 10, 2])), 8)
call_7276 = relay.TupleGetItem(func_2936_call(relay.reshape(call_7266.astype('float64'), [7, 10, 2])), 8)
output = relay.Tuple([call_7266,call_7275,])
output2 = relay.Tuple([call_7267,call_7276,])
func_7281 = relay.Function([], output)
mod['func_7281'] = func_7281
mod = relay.transform.InferType()(mod)
output = func_7281()
func_7282 = relay.Function([], output)
mutated_mod['func_7282'] = func_7282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5818_call = mod.get_global_var('func_5818')
func_5820_call = mutated_mod.get_global_var('func_5820')
call_7325 = relay.TupleGetItem(func_5818_call(), 0)
call_7326 = relay.TupleGetItem(func_5820_call(), 0)
output = relay.Tuple([call_7325,])
output2 = relay.Tuple([call_7326,])
func_7329 = relay.Function([], output)
mod['func_7329'] = func_7329
mod = relay.transform.InferType()(mod)
mutated_mod['func_7329'] = func_7329
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7329_call = mutated_mod.get_global_var('func_7329')
call_7330 = func_7329_call()
output = call_7330
func_7331 = relay.Function([], output)
mutated_mod['func_7331'] = func_7331
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1050_call = mod.get_global_var('func_1050')
func_1051_call = mutated_mod.get_global_var('func_1051')
call_7350 = relay.TupleGetItem(func_1050_call(), 0)
call_7351 = relay.TupleGetItem(func_1051_call(), 0)
output = call_7350
output2 = call_7351
func_7353 = relay.Function([], output)
mod['func_7353'] = func_7353
mod = relay.transform.InferType()(mod)
output = func_7353()
func_7354 = relay.Function([], output)
mutated_mod['func_7354'] = func_7354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2959_call = mod.get_global_var('func_2959')
func_2960_call = mutated_mod.get_global_var('func_2960')
call_7360 = relay.TupleGetItem(func_2959_call(), 0)
call_7361 = relay.TupleGetItem(func_2960_call(), 0)
output = relay.Tuple([call_7360,])
output2 = relay.Tuple([call_7361,])
func_7364 = relay.Function([], output)
mod['func_7364'] = func_7364
mod = relay.transform.InferType()(mod)
output = func_7364()
func_7365 = relay.Function([], output)
mutated_mod['func_7365'] = func_7365
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7263_call = mod.get_global_var('func_7263')
func_7265_call = mutated_mod.get_global_var('func_7265')
call_7381 = relay.TupleGetItem(func_7263_call(), 1)
call_7382 = relay.TupleGetItem(func_7265_call(), 1)
func_4426_call = mod.get_global_var('func_4426')
func_4429_call = mutated_mod.get_global_var('func_4429')
var_7386 = relay.var("var_7386", dtype = "float32", shape = (546,))#candidate|7386|(546,)|var|float32
const_7387 = relay.const([-5.770329,-8.119147,-5.948399,6.460886,-2.290131,-5.760431,-4.602227,4.314523,-4.763487,-3.741488,-2.244271,-7.460552,2.241189,4.829115,1.267879,-3.367859,-0.541049,1.699328,0.545733,2.567770,-7.307475,1.629041,-3.105452,-3.901785,-7.084931,6.497537,-6.391861,0.420713,5.157128,-3.602441,-6.159894,1.836144,2.000894,1.236979,3.120641,6.977342,-7.232424,-2.371500,2.393780,-4.814197,-2.517456,-4.256543,1.572823,-5.818643,-7.616979,4.418546,-6.449908,4.356753,1.041381,-7.006555,1.875275,-6.665297,-2.785366,6.400685,-8.468497,2.999711,2.182455,9.478897,-0.391013,-7.660909,-8.813388,4.281055,-5.670780,4.218391,0.398276,-3.737545,8.776401,5.496101,9.867613,8.389743,-5.635271,-0.441149,-1.537346,-5.416490,-1.000539,4.530289,-7.715399,0.630556,9.463462,-8.409917,-0.855997,-4.088175,-4.728224,0.561286,-1.832909,6.610512,-2.954775,-1.698328,6.977070,4.582610,9.755661,-0.747338,5.043983,-9.230116,-2.361691,7.986148,7.671835,-0.980588,1.526046,-2.256417,-6.618396,-2.051904,3.153142,4.063218,9.600251], dtype = "float64")#candidate|7387|(105,)|const|float64
call_7385 = relay.TupleGetItem(func_4426_call(relay.reshape(var_7386.astype('float32'), [14, 3, 13]), relay.reshape(const_7387.astype('float64'), [105,]), ), 1)
call_7388 = relay.TupleGetItem(func_4429_call(relay.reshape(var_7386.astype('float32'), [14, 3, 13]), relay.reshape(const_7387.astype('float64'), [105,]), ), 1)
func_1639_call = mod.get_global_var('func_1639')
func_1640_call = mutated_mod.get_global_var('func_1640')
call_7392 = relay.TupleGetItem(func_1639_call(), 0)
call_7393 = relay.TupleGetItem(func_1640_call(), 0)
func_5691_call = mod.get_global_var('func_5691')
func_5693_call = mutated_mod.get_global_var('func_5693')
call_7405 = func_5691_call()
call_7406 = func_5691_call()
output = relay.Tuple([call_7381,call_7385,var_7386,const_7387,call_7392,call_7405,])
output2 = relay.Tuple([call_7382,call_7388,var_7386,const_7387,call_7393,call_7406,])
func_7410 = relay.Function([var_7386,], output)
mod['func_7410'] = func_7410
mod = relay.transform.InferType()(mod)
var_7411 = relay.var("var_7411", dtype = "float32", shape = (546,))#candidate|7411|(546,)|var|float32
output = func_7410(var_7411)
func_7412 = relay.Function([var_7411], output)
mutated_mod['func_7412'] = func_7412
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7463 = relay.var("var_7463", dtype = "float32", shape = (10, 3, 2))#candidate|7463|(10, 3, 2)|var|float32
uop_7464 = relay.log2(var_7463.astype('float32')) # shape=(10, 3, 2)
func_3405_call = mod.get_global_var('func_3405')
func_3408_call = mutated_mod.get_global_var('func_3408')
const_7467 = relay.const([-5,-6,6,-5,2,4,-10,5,7,-1,-2,3,-5,-9,7,2,8,6,-6,6,-5,-10,-7,6,-10,2,-10,-6,-1,2,4,-2,2,6,-1,5,-1,10,1,-1,-2,1,-10,-7,-5,-1,-2,1,2,-1,-10,-6,1,-8,-1,3,5,-5,2,-6,-10,-6,-9,-8,6,2,6,-6,6,-9,-4,2,8,-4,9,9,-4,-2,4,4,9,-6,7,-4,-6,2,7,9,1,-6,-1,8,10,10,1,-5,-1,-7,-3,-3,-4,-8,1,4,1,10,5,-9,1,-2,-5,-3,6,-7,9,-7,-9,3,10,-9,9,3,1,-10,3,-3,9,-5,5,5,3,8,4,-9,-1,7,2,-4,4,-3,8,-5,3,-1,3,-4,-7,-6,4,-7,-6,4,6,10,4,9,9,-10,-4,-1,-6,-3,9,-3,-7,-9,5,-2,3,-1,5,-10,3,-9,10,6,-8,10,8,-10,4,-9,-3,9,5,5,-1,-8,-7,-3,-8,-5,-10,4,8,5,3,2,7,4,-5,-1,5,3,6,-9,7,-3,-10,-4,-2,2,-5,3,-10,-1,5,-3,3,2,-4,-6,-8,-7,-9,-7,-4,-6,7,-8,-6,4,-4,4,3,-7,-1,-9,5,5,8,4,-3,10,10,9,-10,-9,-1,2,-1,2,-5,8,6,-3], dtype = "int64")#candidate|7467|(256,)|const|int64
const_7468 = relay.const([[9,-8,-6,2],[8,1,5,-6],[5,3,1,4],[-10,5,-3,3],[-9,-6,9,-10],[1,-10,7,9],[3,9,-5,5],[10,-9,3,8],[-6,8,-2,4],[-10,-2,-2,2],[-4,9,-3,-3],[4,-9,8,10],[-2,9,7,-9],[-10,7,-3,7],[-7,7,3,-5],[5,-4,9,-7],[2,-7,9,-7],[9,3,10,-1],[8,-9,9,-8],[5,-5,5,7],[8,-8,2,-8],[-1,4,8,-10],[-5,-7,-10,7],[6,10,-4,3],[-3,-10,8,7],[-6,-1,-8,3],[10,8,-5,-5],[-8,4,-6,-5],[8,5,3,3],[4,-8,-7,-6],[2,-6,10,8],[8,2,-9,-2],[-4,10,8,-1],[-1,5,-9,-2],[-6,10,10,5],[-9,2,6,4],[-3,-9,10,-3],[8,-7,-8,10],[7,-1,-7,7],[-3,-6,6,-1],[4,10,-10,5],[9,-7,-2,3],[6,-8,-10,10],[7,4,-6,10],[5,-6,-3,4],[-4,10,-7,-7],[5,-7,4,8],[-5,-3,-7,5],[-5,6,-1,-1],[-9,-2,2,-1],[-7,-1,8,-10],[-2,-8,-10,-1],[-3,4,-7,-8],[3,-5,9,3],[-6,7,-4,1],[-2,6,-1,8],[6,-7,-6,-3],[4,6,-6,1],[3,-8,-9,-6],[-9,4,1,-3],[3,-4,-6,9],[-5,-5,-4,-4],[8,-6,2,-7],[-6,2,-10,-8],[6,1,-7,10],[-5,-2,5,8],[10,8,7,3],[-6,-3,-10,1],[-1,8,5,9],[-4,1,-8,3],[-4,-10,-6,-4],[-9,-9,8,-7],[-4,-6,-2,9],[9,-7,8,5],[-1,-2,-9,1],[3,-7,2,9],[-8,5,1,5],[-5,-7,2,-4],[6,-2,-2,4],[-3,-8,6,8],[-10,3,-8,-1],[3,-5,-9,-8],[5,-1,2,-4],[-6,-7,10,6],[10,-3,-8,-1],[-10,7,-5,4],[6,-9,-1,-1],[-7,-9,8,7],[5,-8,4,-5],[6,-4,7,-3],[5,1,-6,3],[5,-10,-7,10],[-7,-4,-10,7],[-1,8,-1,2],[10,-4,-8,-10],[10,5,-7,1],[5,-8,8,-2],[-6,-8,-1,7],[-4,10,9,-6],[-9,8,7,-3],[9,-9,7,-6],[4,-2,-4,8],[9,1,-9,-8],[-9,-8,8,-9],[3,5,-1,-2],[5,-2,4,-9],[2,-2,-9,9],[7,-4,-9,3],[3,1,-9,1],[-9,-2,-6,8],[3,7,8,-1],[5,9,8,-7],[10,-5,3,2],[2,4,7,4],[-2,3,10,7],[9,1,-10,8],[-6,-10,10,10],[-5,10,8,3],[8,4,-10,-5],[-8,6,-5,-9],[-9,2,10,3],[-8,-7,-8,8],[6,6,-4,-3],[-7,2,5,-5],[-10,-6,-8,-6],[-2,3,-3,8],[5,-5,4,3],[9,5,7,-10]], dtype = "int64")#candidate|7468|(128, 4)|const|int64
call_7466 = relay.TupleGetItem(func_3405_call(relay.reshape(const_7467.astype('int64'), [16, 1, 16]), relay.reshape(const_7468.astype('int64'), [16, 2, 16]), ), 1)
call_7469 = relay.TupleGetItem(func_3408_call(relay.reshape(const_7467.astype('int64'), [16, 1, 16]), relay.reshape(const_7468.astype('int64'), [16, 2, 16]), ), 1)
uop_7477 = relay.erf(uop_7464.astype('float32')) # shape=(10, 3, 2)
uop_7479 = relay.atan(uop_7477.astype('float64')) # shape=(10, 3, 2)
bop_7484 = relay.floor_mod(uop_7464.astype('float32'), relay.reshape(var_7463.astype('float32'), relay.shape_of(uop_7464))) # shape=(10, 3, 2)
var_7488 = relay.var("var_7488", dtype = "float64", shape = (10, 3, 2))#candidate|7488|(10, 3, 2)|var|float64
bop_7489 = relay.logical_and(uop_7479.astype('bool'), relay.reshape(var_7488.astype('bool'), relay.shape_of(uop_7479))) # shape=(10, 3, 2)
bop_7499 = relay.bitwise_and(uop_7464.astype('int16'), relay.reshape(bop_7484.astype('int16'), relay.shape_of(uop_7464))) # shape=(10, 3, 2)
output = relay.Tuple([call_7466,const_7467,const_7468,bop_7489,bop_7499,])
output2 = relay.Tuple([call_7469,const_7467,const_7468,bop_7489,bop_7499,])
func_7503 = relay.Function([var_7463,var_7488,], output)
mod['func_7503'] = func_7503
mod = relay.transform.InferType()(mod)
var_7504 = relay.var("var_7504", dtype = "float32", shape = (10, 3, 2))#candidate|7504|(10, 3, 2)|var|float32
var_7505 = relay.var("var_7505", dtype = "float64", shape = (10, 3, 2))#candidate|7505|(10, 3, 2)|var|float64
output = func_7503(var_7504,var_7505,)
func_7506 = relay.Function([var_7504,var_7505,], output)
mutated_mod['func_7506'] = func_7506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1646_call = mod.get_global_var('func_1646')
func_1647_call = mutated_mod.get_global_var('func_1647')
call_7537 = relay.TupleGetItem(func_1646_call(), 0)
call_7538 = relay.TupleGetItem(func_1647_call(), 0)
func_4563_call = mod.get_global_var('func_4563')
func_4565_call = mutated_mod.get_global_var('func_4565')
call_7544 = relay.TupleGetItem(func_4563_call(), 0)
call_7545 = relay.TupleGetItem(func_4565_call(), 0)
func_556_call = mod.get_global_var('func_556')
func_559_call = mutated_mod.get_global_var('func_559')
const_7547 = relay.const([9.842202,2.160207,0.095311,-9.913786,-1.415312,4.465308,-7.958666,-8.678380,7.910623,-4.650230,-7.467258,4.218674,2.372585,-1.033037,3.600821,-6.171192,-7.639310,3.634316,5.065551,-3.477486,-5.409431,-3.271512,8.937634,-1.229077,2.903500,-3.881494,4.161050,-2.906733,-9.434160,7.629806,3.123298,-2.716002,7.806559,7.144241,0.207188,-6.684131,6.169419,-8.183038,-9.338603,-3.996683,0.120809,3.694449,-0.073195,2.846848], dtype = "float64")#candidate|7547|(44,)|const|float64
call_7546 = relay.TupleGetItem(func_556_call(relay.reshape(const_7547.astype('float64'), [44,])), 4)
call_7548 = relay.TupleGetItem(func_559_call(relay.reshape(const_7547.astype('float64'), [44,])), 4)
output = relay.Tuple([call_7537,call_7544,call_7546,const_7547,])
output2 = relay.Tuple([call_7538,call_7545,call_7548,const_7547,])
func_7551 = relay.Function([], output)
mod['func_7551'] = func_7551
mod = relay.transform.InferType()(mod)
mutated_mod['func_7551'] = func_7551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7551_call = mutated_mod.get_global_var('func_7551')
call_7552 = func_7551_call()
output = call_7552
func_7553 = relay.Function([], output)
mutated_mod['func_7553'] = func_7553
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3779_call = mod.get_global_var('func_3779')
func_3781_call = mutated_mod.get_global_var('func_3781')
call_7590 = relay.TupleGetItem(func_3779_call(), 5)
call_7591 = relay.TupleGetItem(func_3781_call(), 5)
output = call_7590
output2 = call_7591
func_7602 = relay.Function([], output)
mod['func_7602'] = func_7602
mod = relay.transform.InferType()(mod)
mutated_mod['func_7602'] = func_7602
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7602_call = mutated_mod.get_global_var('func_7602')
call_7603 = func_7602_call()
output = call_7603
func_7604 = relay.Function([], output)
mutated_mod['func_7604'] = func_7604
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7608 = relay.const([[[-9.375286],[6.105267],[4.475156],[-2.704831],[-3.584619],[3.922368],[-1.718195],[-4.530680],[-1.195015],[-3.492173],[9.700314],[3.017264],[-7.259849],[-2.350965],[9.743553],[-6.325430]],[[-7.036526],[-4.604327],[9.715203],[-1.423644],[0.141516],[-1.364570],[-3.081623],[5.004969],[2.991594],[2.251111],[-9.315167],[-2.149997],[-0.362899],[-7.428526],[-9.337099],[6.928456]],[[7.347329],[-8.246306],[-6.418460],[-5.112842],[2.725527],[-4.563232],[7.866999],[-2.200028],[3.255897],[-9.766038],[4.843056],[-1.241564],[3.472626],[1.502153],[7.939537],[-8.303255]],[[-3.850363],[-0.015502],[-1.618056],[-3.227552],[4.974915],[9.723364],[-3.866911],[5.217596],[6.447756],[5.898561],[-9.648898],[-2.949883],[7.005441],[6.240761],[-0.710191],[1.107216]]], dtype = "float32")#candidate|7608|(4, 16, 1)|const|float32
uop_7609 = relay.atan(const_7608.astype('float32')) # shape=(4, 16, 1)
output = uop_7609
output2 = uop_7609
func_7616 = relay.Function([], output)
mod['func_7616'] = func_7616
mod = relay.transform.InferType()(mod)
output = func_7616()
func_7617 = relay.Function([], output)
mutated_mod['func_7617'] = func_7617
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_7628 = relay.TupleGetItem(func_2545_call(), 1)
call_7629 = relay.TupleGetItem(func_2546_call(), 1)
func_2657_call = mod.get_global_var('func_2657')
func_2661_call = mutated_mod.get_global_var('func_2661')
var_7641 = relay.var("var_7641", dtype = "bool", shape = (630,))#candidate|7641|(630,)|var|bool
call_7640 = relay.TupleGetItem(func_2657_call(relay.reshape(var_7641.astype('bool'), [15, 6, 7]), relay.reshape(var_7641.astype('bool'), [15, 6, 7]), ), 0)
call_7642 = relay.TupleGetItem(func_2661_call(relay.reshape(var_7641.astype('bool'), [15, 6, 7]), relay.reshape(var_7641.astype('bool'), [15, 6, 7]), ), 0)
func_4194_call = mod.get_global_var('func_4194')
func_4195_call = mutated_mod.get_global_var('func_4195')
call_7649 = relay.TupleGetItem(func_4194_call(), 5)
call_7650 = relay.TupleGetItem(func_4195_call(), 5)
func_3256_call = mod.get_global_var('func_3256')
func_3257_call = mutated_mod.get_global_var('func_3257')
call_7654 = relay.TupleGetItem(func_3256_call(), 0)
call_7655 = relay.TupleGetItem(func_3257_call(), 0)
uop_7656 = relay.rsqrt(call_7628.astype('float32')) # shape=(14, 13, 1)
uop_7658 = relay.rsqrt(call_7629.astype('float32')) # shape=(14, 13, 1)
func_3469_call = mod.get_global_var('func_3469')
func_3470_call = mutated_mod.get_global_var('func_3470')
call_7667 = func_3469_call()
call_7668 = func_3469_call()
bop_7672 = relay.right_shift(uop_7656.astype('int16'), var_7641.astype('int16')) # shape=(14, 13, 630)
bop_7675 = relay.right_shift(uop_7658.astype('int16'), var_7641.astype('int16')) # shape=(14, 13, 630)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_7677 = relay.TupleGetItem(func_5203_call(), 3)
call_7678 = relay.TupleGetItem(func_5205_call(), 3)
output = relay.Tuple([call_7640,call_7649,call_7654,call_7667,bop_7672,call_7677,])
output2 = relay.Tuple([call_7642,call_7650,call_7655,call_7668,bop_7675,call_7678,])
func_7679 = relay.Function([var_7641,], output)
mod['func_7679'] = func_7679
mod = relay.transform.InferType()(mod)
var_7680 = relay.var("var_7680", dtype = "bool", shape = (630,))#candidate|7680|(630,)|var|bool
output = func_7679(var_7680)
func_7681 = relay.Function([var_7680], output)
mutated_mod['func_7681'] = func_7681
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7685 = relay.var("var_7685", dtype = "float64", shape = (3, 15, 5))#candidate|7685|(3, 15, 5)|var|float64
uop_7686 = relay.acos(var_7685.astype('float64')) # shape=(3, 15, 5)
bop_7701 = relay.divide(uop_7686.astype('float64'), relay.reshape(var_7685.astype('float64'), relay.shape_of(uop_7686))) # shape=(3, 15, 5)
var_7711 = relay.var("var_7711", dtype = "float64", shape = (3, 15, 5))#candidate|7711|(3, 15, 5)|var|float64
bop_7712 = relay.maximum(uop_7686.astype('int64'), relay.reshape(var_7711.astype('int64'), relay.shape_of(uop_7686))) # shape=(3, 15, 5)
output = relay.Tuple([bop_7701,bop_7712,])
output2 = relay.Tuple([bop_7701,bop_7712,])
func_7728 = relay.Function([var_7685,var_7711,], output)
mod['func_7728'] = func_7728
mod = relay.transform.InferType()(mod)
var_7729 = relay.var("var_7729", dtype = "float64", shape = (3, 15, 5))#candidate|7729|(3, 15, 5)|var|float64
var_7730 = relay.var("var_7730", dtype = "float64", shape = (3, 15, 5))#candidate|7730|(3, 15, 5)|var|float64
output = func_7728(var_7729,var_7730,)
func_7731 = relay.Function([var_7729,var_7730,], output)
mutated_mod['func_7731'] = func_7731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7748 = relay.var("var_7748", dtype = "int16", shape = (4, 6, 3))#candidate|7748|(4, 6, 3)|var|int16
var_7749 = relay.var("var_7749", dtype = "int16", shape = (4, 6, 3))#candidate|7749|(4, 6, 3)|var|int16
bop_7750 = relay.logical_xor(var_7748.astype('int16'), relay.reshape(var_7749.astype('int16'), relay.shape_of(var_7748))) # shape=(4, 6, 3)
output = bop_7750
output2 = bop_7750
func_7753 = relay.Function([var_7748,var_7749,], output)
mod['func_7753'] = func_7753
mod = relay.transform.InferType()(mod)
var_7754 = relay.var("var_7754", dtype = "int16", shape = (4, 6, 3))#candidate|7754|(4, 6, 3)|var|int16
var_7755 = relay.var("var_7755", dtype = "int16", shape = (4, 6, 3))#candidate|7755|(4, 6, 3)|var|int16
output = func_7753(var_7754,var_7755,)
func_7756 = relay.Function([var_7754,var_7755,], output)
mutated_mod['func_7756'] = func_7756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7281_call = mod.get_global_var('func_7281')
func_7282_call = mutated_mod.get_global_var('func_7282')
call_7758 = relay.TupleGetItem(func_7281_call(), 0)
call_7759 = relay.TupleGetItem(func_7282_call(), 0)
func_5102_call = mod.get_global_var('func_5102')
func_5105_call = mutated_mod.get_global_var('func_5105')
var_7779 = relay.var("var_7779", dtype = "float64", shape = (52,))#candidate|7779|(52,)|var|float64
call_7778 = func_5102_call(relay.reshape(var_7779.astype('float64'), [2, 2, 13]))
call_7780 = func_5102_call(relay.reshape(var_7779.astype('float64'), [2, 2, 13]))
output = relay.Tuple([call_7758,call_7778,var_7779,])
output2 = relay.Tuple([call_7759,call_7780,var_7779,])
func_7783 = relay.Function([var_7779,], output)
mod['func_7783'] = func_7783
mod = relay.transform.InferType()(mod)
mutated_mod['func_7783'] = func_7783
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7784 = relay.var("var_7784", dtype = "float64", shape = (52,))#candidate|7784|(52,)|var|float64
func_7783_call = mutated_mod.get_global_var('func_7783')
call_7785 = func_7783_call(var_7784)
output = call_7785
func_7786 = relay.Function([var_7784], output)
mutated_mod['func_7786'] = func_7786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5970_call = mod.get_global_var('func_5970')
func_5972_call = mutated_mod.get_global_var('func_5972')
call_7788 = func_5970_call()
call_7789 = func_5970_call()
func_5722_call = mod.get_global_var('func_5722')
func_5723_call = mutated_mod.get_global_var('func_5723')
call_7790 = func_5722_call()
call_7791 = func_5722_call()
output = relay.Tuple([call_7788,call_7790,])
output2 = relay.Tuple([call_7789,call_7791,])
func_7800 = relay.Function([], output)
mod['func_7800'] = func_7800
mod = relay.transform.InferType()(mod)
mutated_mod['func_7800'] = func_7800
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7800_call = mutated_mod.get_global_var('func_7800')
call_7801 = func_7800_call()
output = call_7801
func_7802 = relay.Function([], output)
mutated_mod['func_7802'] = func_7802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_196_call = mod.get_global_var('func_196')
func_198_call = mutated_mod.get_global_var('func_198')
call_7819 = func_196_call()
call_7820 = func_196_call()
output = relay.Tuple([call_7819,])
output2 = relay.Tuple([call_7820,])
func_7828 = relay.Function([], output)
mod['func_7828'] = func_7828
mod = relay.transform.InferType()(mod)
output = func_7828()
func_7829 = relay.Function([], output)
mutated_mod['func_7829'] = func_7829
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3469_call = mod.get_global_var('func_3469')
func_3470_call = mutated_mod.get_global_var('func_3470')
call_7852 = func_3469_call()
call_7853 = func_3469_call()
func_4970_call = mod.get_global_var('func_4970')
func_4971_call = mutated_mod.get_global_var('func_4971')
call_7866 = relay.TupleGetItem(func_4970_call(), 0)
call_7867 = relay.TupleGetItem(func_4971_call(), 0)
output = relay.Tuple([call_7852,call_7866,])
output2 = relay.Tuple([call_7853,call_7867,])
func_7874 = relay.Function([], output)
mod['func_7874'] = func_7874
mod = relay.transform.InferType()(mod)
mutated_mod['func_7874'] = func_7874
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7874_call = mutated_mod.get_global_var('func_7874')
call_7875 = func_7874_call()
output = call_7875
func_7876 = relay.Function([], output)
mutated_mod['func_7876'] = func_7876
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7616_call = mod.get_global_var('func_7616')
func_7617_call = mutated_mod.get_global_var('func_7617')
call_7932 = func_7616_call()
call_7933 = func_7616_call()
var_7934 = relay.var("var_7934", dtype = "float32", shape = (4, 16, 1))#candidate|7934|(4, 16, 1)|var|float32
bop_7935 = relay.left_shift(call_7932.astype('int16'), relay.reshape(var_7934.astype('int16'), relay.shape_of(call_7932))) # shape=(4, 16, 1)
bop_7938 = relay.left_shift(call_7933.astype('int16'), relay.reshape(var_7934.astype('int16'), relay.shape_of(call_7933))) # shape=(4, 16, 1)
output = relay.Tuple([bop_7935,])
output2 = relay.Tuple([bop_7938,])
func_7943 = relay.Function([var_7934,], output)
mod['func_7943'] = func_7943
mod = relay.transform.InferType()(mod)
var_7944 = relay.var("var_7944", dtype = "float32", shape = (4, 16, 1))#candidate|7944|(4, 16, 1)|var|float32
output = func_7943(var_7944)
func_7945 = relay.Function([var_7944], output)
mutated_mod['func_7945'] = func_7945
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7956 = relay.var("var_7956", dtype = "uint16", shape = (5, 13, 12))#candidate|7956|(5, 13, 12)|var|uint16
var_7957 = relay.var("var_7957", dtype = "uint16", shape = (5, 13, 12))#candidate|7957|(5, 13, 12)|var|uint16
bop_7958 = relay.minimum(var_7956.astype('uint16'), relay.reshape(var_7957.astype('uint16'), relay.shape_of(var_7956))) # shape=(5, 13, 12)
output = bop_7958
output2 = bop_7958
func_7963 = relay.Function([var_7956,var_7957,], output)
mod['func_7963'] = func_7963
mod = relay.transform.InferType()(mod)
mutated_mod['func_7963'] = func_7963
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7963_call = mutated_mod.get_global_var('func_7963')
var_7965 = relay.var("var_7965", dtype = "uint16", shape = (5, 13, 12))#candidate|7965|(5, 13, 12)|var|uint16
var_7966 = relay.var("var_7966", dtype = "uint16", shape = (5, 13, 12))#candidate|7966|(5, 13, 12)|var|uint16
call_7964 = func_7963_call(var_7965,var_7966,)
output = call_7964
func_7967 = relay.Function([var_7965,var_7966,], output)
mutated_mod['func_7967'] = func_7967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6243_call = mod.get_global_var('func_6243')
func_6245_call = mutated_mod.get_global_var('func_6245')
call_7974 = relay.TupleGetItem(func_6243_call(), 1)
call_7975 = relay.TupleGetItem(func_6245_call(), 1)
func_7204_call = mod.get_global_var('func_7204')
func_7207_call = mutated_mod.get_global_var('func_7207')
const_8006 = relay.const([[-5,-10,-7,1,-7],[-8,-6,-10,8,-9],[-4,-8,4,-8,9],[-5,5,1,6,-1],[10,1,10,7,9],[-4,8,-4,4,-7],[10,-1,7,4,3]], dtype = "uint8")#candidate|8006|(7, 5)|const|uint8
var_8007 = relay.var("var_8007", dtype = "float64", shape = (44,))#candidate|8007|(44,)|var|float64
call_8005 = relay.TupleGetItem(func_7204_call(relay.reshape(const_8006.astype('uint8'), [35,]), relay.reshape(var_8007.astype('float64'), [1, 44]), ), 3)
call_8008 = relay.TupleGetItem(func_7207_call(relay.reshape(const_8006.astype('uint8'), [35,]), relay.reshape(var_8007.astype('float64'), [1, 44]), ), 3)
func_3247_call = mod.get_global_var('func_3247')
func_3249_call = mutated_mod.get_global_var('func_3249')
call_8009 = relay.TupleGetItem(func_3247_call(), 0)
call_8010 = relay.TupleGetItem(func_3249_call(), 0)
func_2995_call = mod.get_global_var('func_2995')
func_2997_call = mutated_mod.get_global_var('func_2997')
call_8011 = func_2995_call()
call_8012 = func_2995_call()
output = relay.Tuple([call_7974,call_8005,const_8006,var_8007,call_8009,call_8011,])
output2 = relay.Tuple([call_7975,call_8008,const_8006,var_8007,call_8010,call_8012,])
func_8060 = relay.Function([var_8007,], output)
mod['func_8060'] = func_8060
mod = relay.transform.InferType()(mod)
var_8061 = relay.var("var_8061", dtype = "float64", shape = (44,))#candidate|8061|(44,)|var|float64
output = func_8060(var_8061)
func_8062 = relay.Function([var_8061], output)
mutated_mod['func_8062'] = func_8062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2995_call = mod.get_global_var('func_2995')
func_2997_call = mutated_mod.get_global_var('func_2997')
call_8080 = func_2995_call()
call_8081 = func_2995_call()
output = relay.Tuple([call_8080,])
output2 = relay.Tuple([call_8081,])
func_8117 = relay.Function([], output)
mod['func_8117'] = func_8117
mod = relay.transform.InferType()(mod)
output = func_8117()
func_8118 = relay.Function([], output)
mutated_mod['func_8118'] = func_8118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5203_call = mod.get_global_var('func_5203')
func_5205_call = mutated_mod.get_global_var('func_5205')
call_8152 = relay.TupleGetItem(func_5203_call(), 2)
call_8153 = relay.TupleGetItem(func_5205_call(), 2)
output = call_8152
output2 = call_8153
func_8171 = relay.Function([], output)
mod['func_8171'] = func_8171
mod = relay.transform.InferType()(mod)
output = func_8171()
func_8172 = relay.Function([], output)
mutated_mod['func_8172'] = func_8172
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8193 = relay.var("var_8193", dtype = "float32", shape = (14, 12, 3))#candidate|8193|(14, 12, 3)|var|float32
uop_8194 = relay.asinh(var_8193.astype('float32')) # shape=(14, 12, 3)
func_2386_call = mod.get_global_var('func_2386')
func_2387_call = mutated_mod.get_global_var('func_2387')
call_8196 = func_2386_call()
call_8197 = func_2386_call()
func_5944_call = mod.get_global_var('func_5944')
func_5947_call = mutated_mod.get_global_var('func_5947')
var_8210 = relay.var("var_8210", dtype = "int32", shape = (2, 1))#candidate|8210|(2, 1)|var|int32
var_8211 = relay.var("var_8211", dtype = "int32", shape = (14,))#candidate|8211|(14,)|var|int32
call_8209 = relay.TupleGetItem(func_5944_call(relay.reshape(var_8210.astype('int32'), [2, 1, 1]), relay.reshape(var_8211.astype('int32'), [2, 1, 7]), ), 0)
call_8212 = relay.TupleGetItem(func_5947_call(relay.reshape(var_8210.astype('int32'), [2, 1, 1]), relay.reshape(var_8211.astype('int32'), [2, 1, 7]), ), 0)
output = relay.Tuple([uop_8194,call_8196,call_8209,var_8210,var_8211,])
output2 = relay.Tuple([uop_8194,call_8197,call_8212,var_8210,var_8211,])
func_8228 = relay.Function([var_8193,var_8210,var_8211,], output)
mod['func_8228'] = func_8228
mod = relay.transform.InferType()(mod)
mutated_mod['func_8228'] = func_8228
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8228_call = mutated_mod.get_global_var('func_8228')
var_8230 = relay.var("var_8230", dtype = "float32", shape = (14, 12, 3))#candidate|8230|(14, 12, 3)|var|float32
var_8231 = relay.var("var_8231", dtype = "int32", shape = (2, 1))#candidate|8231|(2, 1)|var|int32
var_8232 = relay.var("var_8232", dtype = "int32", shape = (14,))#candidate|8232|(14,)|var|int32
call_8229 = func_8228_call(var_8230,var_8231,var_8232,)
output = call_8229
func_8233 = relay.Function([var_8230,var_8231,var_8232,], output)
mutated_mod['func_8233'] = func_8233
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7800_call = mod.get_global_var('func_7800')
func_7802_call = mutated_mod.get_global_var('func_7802')
call_8240 = relay.TupleGetItem(func_7800_call(), 0)
call_8241 = relay.TupleGetItem(func_7802_call(), 0)
func_5855_call = mod.get_global_var('func_5855')
func_5857_call = mutated_mod.get_global_var('func_5857')
call_8261 = relay.TupleGetItem(func_5855_call(), 0)
call_8262 = relay.TupleGetItem(func_5857_call(), 0)
output = relay.Tuple([call_8240,call_8261,])
output2 = relay.Tuple([call_8241,call_8262,])
func_8263 = relay.Function([], output)
mod['func_8263'] = func_8263
mod = relay.transform.InferType()(mod)
output = func_8263()
func_8264 = relay.Function([], output)
mutated_mod['func_8264'] = func_8264
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_8287 = relay.TupleGetItem(func_2198_call(), 0)
call_8288 = relay.TupleGetItem(func_2200_call(), 0)
func_2545_call = mod.get_global_var('func_2545')
func_2546_call = mutated_mod.get_global_var('func_2546')
call_8304 = relay.TupleGetItem(func_2545_call(), 2)
call_8305 = relay.TupleGetItem(func_2546_call(), 2)
output = relay.Tuple([call_8287,call_8304,])
output2 = relay.Tuple([call_8288,call_8305,])
func_8314 = relay.Function([], output)
mod['func_8314'] = func_8314
mod = relay.transform.InferType()(mod)
mutated_mod['func_8314'] = func_8314
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8314_call = mutated_mod.get_global_var('func_8314')
call_8315 = func_8314_call()
output = call_8315
func_8316 = relay.Function([], output)
mutated_mod['func_8316'] = func_8316
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8366 = relay.var("var_8366", dtype = "float64", shape = (1, 5, 6))#candidate|8366|(1, 5, 6)|var|float64
uop_8367 = relay.sigmoid(var_8366.astype('float64')) # shape=(1, 5, 6)
func_5545_call = mod.get_global_var('func_5545')
func_5547_call = mutated_mod.get_global_var('func_5547')
call_8372 = relay.TupleGetItem(func_5545_call(), 0)
call_8373 = relay.TupleGetItem(func_5547_call(), 0)
bop_8384 = relay.minimum(uop_8367.astype('uint16'), relay.reshape(var_8366.astype('uint16'), relay.shape_of(uop_8367))) # shape=(1, 5, 6)
uop_8390 = relay.cosh(bop_8384.astype('float64')) # shape=(1, 5, 6)
output = relay.Tuple([call_8372,uop_8390,])
output2 = relay.Tuple([call_8373,uop_8390,])
F = relay.Function([var_8366,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8366,], output2)
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
