import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_177 = relay.var("var_177", dtype = "int32", shape = ())#candidate|177|()|var|int32
var_178 = relay.var("var_178", dtype = "int32", shape = (1, 6, 8))#candidate|178|(1, 6, 8)|var|int32
bop_179 = relay.subtract(var_177.astype('int32'), var_178.astype('int32')) # shape=(1, 6, 8)
output = relay.Tuple([bop_179,])
output2 = relay.Tuple([bop_179,])
func_182 = relay.Function([var_177,var_178,], output)
mod['func_182'] = func_182
mod = relay.transform.InferType()(mod)
mutated_mod['func_182'] = func_182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_182_call = mutated_mod.get_global_var('func_182')
var_184 = relay.var("var_184", dtype = "int32", shape = ())#candidate|184|()|var|int32
var_185 = relay.var("var_185", dtype = "int32", shape = (1, 6, 8))#candidate|185|(1, 6, 8)|var|int32
call_183 = func_182_call(var_184,var_185,)
output = call_183
func_186 = relay.Function([var_184,var_185,], output)
mutated_mod['func_186'] = func_186
mutated_mod = relay.transform.InferType()(mutated_mod)
const_345 = relay.const([[[9.976412,6.918428,-2.775988,-6.228057],[-3.036190,-1.105850,1.640127,4.713451],[-4.347701,1.062436,7.676865,0.679058],[-2.425998,3.007605,5.722672,6.729012],[-4.752713,-5.377583,-2.076305,4.026694],[-9.318005,-6.686565,4.080598,3.348950],[-6.932524,-3.257023,-0.298395,-0.408108],[-5.370231,-0.651299,8.415619,-9.444347],[-9.863343,-3.810040,4.793566,1.366474],[5.807676,-5.588783,8.489676,6.325892],[-1.272173,0.033518,3.320567,2.464649]],[[3.077380,-2.583192,-5.548627,-1.068222],[1.176775,9.790378,-3.226201,-1.154717],[-7.707788,1.715933,0.856896,1.340600],[-3.205247,-1.776729,5.296964,-0.824427],[7.004895,3.281686,6.638665,-6.269866],[-8.603097,-6.873128,-0.130675,-1.655842],[0.920858,-8.604801,-4.686472,-2.582765],[-4.829045,0.978533,-0.293228,-5.824229],[-4.821952,2.082468,3.472243,-2.756596],[-4.772127,2.788422,-5.012663,9.768639],[5.156873,-9.833204,-8.639607,-1.531619]],[[3.441999,-3.934439,6.551637,-9.287506],[-2.380279,-5.289538,4.448615,9.428567],[5.461305,9.100523,-0.827941,0.963419],[-1.023446,-5.296273,-8.730737,-7.624305],[-7.459019,7.180060,7.187006,6.938783],[-3.886979,-4.248445,-3.814534,7.589989],[-8.250275,3.728328,8.275179,-6.260425],[-0.700887,-6.835408,5.014589,7.940828],[2.253181,-0.749490,-7.160644,-7.276731],[7.023629,-4.104847,-1.314822,2.044774],[-2.767541,-1.108997,8.864138,-0.367082]],[[6.141061,-8.716733,5.224294,-8.049106],[-9.764102,1.911829,-7.484958,0.145310],[-0.462574,9.613492,0.672149,5.469108],[-3.908890,-0.458494,-1.041384,7.138311],[0.633914,3.555539,5.527663,-3.111086],[-9.954685,-7.408167,4.301718,-9.192540],[-8.565316,2.242459,-5.762730,9.037030],[-1.159940,-0.764632,-1.092849,-9.901264],[1.772807,-0.866714,0.629056,-1.015848],[4.846786,-7.053927,3.386882,-8.721309],[-6.135439,2.666091,4.431068,2.449270]],[[-1.849683,-0.203144,-0.451879,7.700430],[-6.513291,-5.445712,-6.231277,5.452067],[-2.430461,-2.699322,-6.051943,6.850938],[-9.001517,6.360139,0.814570,1.120755],[-4.266776,9.729217,-4.862217,-3.476445],[-9.537213,-6.534598,-2.046726,-9.350790],[6.592353,-4.509462,-7.182960,7.818228],[-5.796192,-5.995370,5.823101,-3.992815],[0.211903,-2.650413,-4.645355,3.933861],[-5.148338,1.063624,4.580376,6.006366],[-5.590478,7.430594,4.629468,-6.921497]]], dtype = "float32")#candidate|345|(5, 11, 4)|const|float32
uop_346 = relay.sin(const_345.astype('float32')) # shape=(5, 11, 4)
const_357 = relay.const([[[-5.516437,-6.483817,-9.790989,-6.216877],[0.260423,-1.193494,-2.541549,-8.518561],[7.664244,-3.385203,2.722560,-5.324971],[2.175564,6.714489,0.877149,-5.894824],[-8.985918,-0.907112,1.319626,4.282486],[-7.182117,-8.710540,-1.407699,-5.375305],[-4.389881,-3.955579,1.882096,7.628035],[9.590847,-1.586937,4.995094,-1.045526],[7.496860,-7.950587,3.515000,2.141350],[-8.737660,-0.476901,0.565160,-9.821106],[7.154980,0.182204,-9.338321,-7.376734]],[[-2.788647,-5.724801,5.323806,1.503275],[5.039448,8.863099,6.159432,-7.866061],[-1.843445,-3.432934,2.602723,-3.177203],[6.250846,-5.370689,-5.332096,0.240907],[7.024705,-2.162585,-6.939225,7.413330],[-3.573073,-2.339462,-0.082239,1.570751],[1.838787,-4.539484,-6.903484,-8.468909],[-6.958474,4.868130,6.448168,6.180596],[-2.464818,1.753680,9.005134,-9.038800],[-1.952153,-5.676595,-8.743664,0.466842],[9.722358,-5.795213,-1.699916,-6.156367]],[[0.360193,4.932275,-8.512885,8.050152],[3.357698,-3.828052,-4.709512,-4.741383],[2.876804,2.947248,-4.938151,-4.867694],[-1.518564,9.190428,0.419985,0.783028],[-4.853182,5.136247,-8.676448,4.517762],[7.836097,-8.590254,0.378684,-1.731558],[5.453088,-9.681471,5.285986,-2.189863],[1.066627,-2.942901,4.894169,-7.012725],[6.379855,-5.088673,-3.329008,6.053351],[8.968355,0.673813,-3.000206,-9.913483],[4.213487,8.388675,3.990951,-8.373350]],[[3.268596,8.547965,7.403222,-0.540894],[6.341587,-9.125751,3.521254,5.366489],[7.594839,3.892888,8.328509,-9.784966],[-5.799585,5.603400,7.533618,-2.251895],[-2.041823,2.595659,3.050663,-5.530002],[-4.663541,5.849078,-9.795601,1.132706],[7.742356,9.040065,-5.690006,-7.006570],[2.976274,-3.797469,3.787519,-5.954580],[-0.250718,4.348057,2.444939,-8.999620],[-9.586663,3.455540,-7.142111,7.739009],[9.330758,-4.555595,-2.672471,-5.164355]],[[-1.348543,-1.239330,-8.085168,-9.654229],[-5.549146,-2.602405,5.869257,8.309036],[-8.342430,6.579558,1.322045,7.632751],[4.099882,-6.483917,-1.421862,-8.053182],[2.110419,-2.512268,0.257199,-9.385360],[5.671732,3.714830,4.979257,-4.679188],[-5.695591,6.437157,-1.582182,-6.008377],[-9.820437,9.622370,-2.618894,-0.771939],[-3.914975,2.335210,8.965793,4.303369],[-1.904946,4.734314,-7.207300,-7.730343],[1.404846,-5.332256,-7.601352,-0.559825]]], dtype = "float32")#candidate|357|(5, 11, 4)|const|float32
bop_358 = relay.floor_mod(uop_346.astype('float32'), relay.reshape(const_357.astype('float32'), relay.shape_of(uop_346))) # shape=(5, 11, 4)
output = bop_358
output2 = bop_358
func_361 = relay.Function([], output)
mod['func_361'] = func_361
mod = relay.transform.InferType()(mod)
output = func_361()
func_362 = relay.Function([], output)
mutated_mod['func_362'] = func_362
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_368 = func_361_call()
call_369 = func_361_call()
uop_385 = relay.atan(call_368.astype('float64')) # shape=(5, 11, 4)
uop_387 = relay.atan(call_369.astype('float64')) # shape=(5, 11, 4)
uop_388 = relay.log(uop_385.astype('float64')) # shape=(5, 11, 4)
uop_390 = relay.log(uop_387.astype('float64')) # shape=(5, 11, 4)
output = uop_388
output2 = uop_390
func_397 = relay.Function([], output)
mod['func_397'] = func_397
mod = relay.transform.InferType()(mod)
output = func_397()
func_398 = relay.Function([], output)
mutated_mod['func_398'] = func_398
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_410 = func_361_call()
call_411 = func_361_call()
output = call_410
output2 = call_411
func_412 = relay.Function([], output)
mod['func_412'] = func_412
mod = relay.transform.InferType()(mod)
mutated_mod['func_412'] = func_412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_412_call = mutated_mod.get_global_var('func_412')
call_413 = func_412_call()
output = call_413
func_414 = relay.Function([], output)
mutated_mod['func_414'] = func_414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_461 = func_397_call()
call_462 = func_397_call()
uop_473 = relay.atanh(call_461.astype('float32')) # shape=(5, 11, 4)
uop_475 = relay.atanh(call_462.astype('float32')) # shape=(5, 11, 4)
output = uop_473
output2 = uop_475
func_480 = relay.Function([], output)
mod['func_480'] = func_480
mod = relay.transform.InferType()(mod)
mutated_mod['func_480'] = func_480
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mutated_mod.get_global_var('func_480')
call_481 = func_480_call()
output = call_481
func_482 = relay.Function([], output)
mutated_mod['func_482'] = func_482
mutated_mod = relay.transform.InferType()(mutated_mod)
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_523 = func_397_call()
call_524 = func_397_call()
output = call_523
output2 = call_524
func_526 = relay.Function([], output)
mod['func_526'] = func_526
mod = relay.transform.InferType()(mod)
mutated_mod['func_526'] = func_526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mutated_mod.get_global_var('func_526')
call_527 = func_526_call()
output = call_527
func_528 = relay.Function([], output)
mutated_mod['func_528'] = func_528
mutated_mod = relay.transform.InferType()(mutated_mod)
var_534 = relay.var("var_534", dtype = "float32", shape = (7, 2, 3))#candidate|534|(7, 2, 3)|var|float32
uop_535 = relay.acosh(var_534.astype('float32')) # shape=(7, 2, 3)
uop_539 = relay.sin(uop_535.astype('float64')) # shape=(7, 2, 3)
func_182_call = mod.get_global_var('func_182')
func_186_call = mutated_mod.get_global_var('func_186')
const_542 = relay.const(-5, dtype = "int32")#candidate|542|()|const|int32
var_543 = relay.var("var_543", dtype = "int32", shape = (48,))#candidate|543|(48,)|var|int32
call_541 = relay.TupleGetItem(func_182_call(relay.reshape(const_542.astype('int32'), []), relay.reshape(var_543.astype('int32'), [1, 6, 8]), ), 0)
call_544 = relay.TupleGetItem(func_186_call(relay.reshape(const_542.astype('int32'), []), relay.reshape(var_543.astype('int32'), [1, 6, 8]), ), 0)
output = relay.Tuple([uop_539,call_541,const_542,var_543,])
output2 = relay.Tuple([uop_539,call_544,const_542,var_543,])
func_545 = relay.Function([var_534,var_543,], output)
mod['func_545'] = func_545
mod = relay.transform.InferType()(mod)
var_546 = relay.var("var_546", dtype = "float32", shape = (7, 2, 3))#candidate|546|(7, 2, 3)|var|float32
var_547 = relay.var("var_547", dtype = "int32", shape = (48,))#candidate|547|(48,)|var|int32
output = func_545(var_546,var_547,)
func_548 = relay.Function([var_546,var_547,], output)
mutated_mod['func_548'] = func_548
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_555 = func_361_call()
call_556 = func_361_call()
var_557 = relay.var("var_557", dtype = "float32", shape = (5, 11, 4))#candidate|557|(5, 11, 4)|var|float32
bop_558 = relay.greater(call_555.astype('bool'), relay.reshape(var_557.astype('bool'), relay.shape_of(call_555))) # shape=(5, 11, 4)
bop_561 = relay.greater(call_556.astype('bool'), relay.reshape(var_557.astype('bool'), relay.shape_of(call_556))) # shape=(5, 11, 4)
var_562 = relay.var("var_562", dtype = "bool", shape = (5, 11, 4))#candidate|562|(5, 11, 4)|var|bool
bop_563 = relay.multiply(bop_558.astype('float64'), relay.reshape(var_562.astype('float64'), relay.shape_of(bop_558))) # shape=(5, 11, 4)
bop_566 = relay.multiply(bop_561.astype('float64'), relay.reshape(var_562.astype('float64'), relay.shape_of(bop_561))) # shape=(5, 11, 4)
output = relay.Tuple([bop_563,])
output2 = relay.Tuple([bop_566,])
func_573 = relay.Function([var_557,var_562,], output)
mod['func_573'] = func_573
mod = relay.transform.InferType()(mod)
mutated_mod['func_573'] = func_573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_573_call = mutated_mod.get_global_var('func_573')
var_575 = relay.var("var_575", dtype = "float32", shape = (5, 11, 4))#candidate|575|(5, 11, 4)|var|float32
var_576 = relay.var("var_576", dtype = "bool", shape = (5, 11, 4))#candidate|576|(5, 11, 4)|var|bool
call_574 = func_573_call(var_575,var_576,)
output = call_574
func_577 = relay.Function([var_575,var_576,], output)
mutated_mod['func_577'] = func_577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_621 = relay.var("var_621", dtype = "float32", shape = ())#candidate|621|()|var|float32
var_622 = relay.var("var_622", dtype = "float32", shape = (14, 7, 1))#candidate|622|(14, 7, 1)|var|float32
bop_623 = relay.minimum(var_621.astype('float32'), var_622.astype('float32')) # shape=(14, 7, 1)
output = relay.Tuple([bop_623,])
output2 = relay.Tuple([bop_623,])
func_629 = relay.Function([var_621,var_622,], output)
mod['func_629'] = func_629
mod = relay.transform.InferType()(mod)
mutated_mod['func_629'] = func_629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_629_call = mutated_mod.get_global_var('func_629')
var_631 = relay.var("var_631", dtype = "float32", shape = ())#candidate|631|()|var|float32
var_632 = relay.var("var_632", dtype = "float32", shape = (14, 7, 1))#candidate|632|(14, 7, 1)|var|float32
call_630 = func_629_call(var_631,var_632,)
output = call_630
func_633 = relay.Function([var_631,var_632,], output)
mutated_mod['func_633'] = func_633
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_681 = func_361_call()
call_682 = func_361_call()
output = relay.Tuple([call_681,])
output2 = relay.Tuple([call_682,])
func_684 = relay.Function([], output)
mod['func_684'] = func_684
mod = relay.transform.InferType()(mod)
mutated_mod['func_684'] = func_684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mutated_mod.get_global_var('func_684')
call_685 = func_684_call()
output = call_685
func_686 = relay.Function([], output)
mutated_mod['func_686'] = func_686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_727 = func_480_call()
call_728 = func_480_call()
func_629_call = mod.get_global_var('func_629')
func_633_call = mutated_mod.get_global_var('func_633')
var_730 = relay.var("var_730", dtype = "float32", shape = ())#candidate|730|()|var|float32
const_731 = relay.const([-6.842666,6.074048,5.786817,-4.722535,7.171881,-2.019846,-2.366216,5.619896,-2.386390,-9.950084,5.199385,-5.089941,6.308038,-6.210504,-4.091880,-7.338289,8.285790,0.849167,-3.727906,7.254260,-1.966617,9.572717,-0.760567,-3.128107,-9.839933,-3.212395,5.641954,7.746065,-1.459028,4.251552,6.208294,6.548312,2.550122,-3.756052,-8.837882,-3.285403,6.409496,6.917827,-2.008128,-4.433214,5.630098,-3.884572,4.685054,9.524148,0.583986,-9.006341,-6.763523,5.778144,4.178001,9.982731,0.272603,-0.117348,5.055014,-2.910062,-7.529080,-9.306603,-9.913250,-4.475522,-1.031926,3.959251,-8.491392,-5.003011,9.628283,-1.909764,4.818280,-6.881808,8.285253,7.077390,-6.255501,-2.636193,2.952646,-6.256398,5.785285,3.552665,-2.313129,6.470285,5.529552,0.645860,0.297358,0.185015,4.542486,5.955408,-2.342016,0.242276,2.409786,8.354367,-7.000971,-3.960520,-9.551329,9.977503,-0.033100,8.212814,5.288696,-5.616843,8.428516,1.930461,7.062491,9.859254], dtype = "float32")#candidate|731|(98,)|const|float32
call_729 = relay.TupleGetItem(func_629_call(relay.reshape(var_730.astype('float32'), []), relay.reshape(const_731.astype('float32'), [14, 7, 1]), ), 0)
call_732 = relay.TupleGetItem(func_633_call(relay.reshape(var_730.astype('float32'), []), relay.reshape(const_731.astype('float32'), [14, 7, 1]), ), 0)
uop_734 = relay.sinh(call_729.astype('float32')) # shape=(14, 7, 1)
uop_736 = relay.sinh(call_732.astype('float32')) # shape=(14, 7, 1)
bop_738 = relay.logical_and(uop_734.astype('bool'), var_730.astype('bool')) # shape=(14, 7, 1)
bop_741 = relay.logical_and(uop_736.astype('bool'), var_730.astype('bool')) # shape=(14, 7, 1)
output = relay.Tuple([call_727,const_731,bop_738,])
output2 = relay.Tuple([call_728,const_731,bop_741,])
func_749 = relay.Function([var_730,], output)
mod['func_749'] = func_749
mod = relay.transform.InferType()(mod)
mutated_mod['func_749'] = func_749
mutated_mod = relay.transform.InferType()(mutated_mod)
var_750 = relay.var("var_750", dtype = "float32", shape = ())#candidate|750|()|var|float32
func_749_call = mutated_mod.get_global_var('func_749')
call_751 = func_749_call(var_750)
output = call_751
func_752 = relay.Function([var_750], output)
mutated_mod['func_752'] = func_752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_754 = func_397_call()
call_755 = func_397_call()
var_756 = relay.var("var_756", dtype = "float64", shape = (5, 11, 4))#candidate|756|(5, 11, 4)|var|float64
bop_757 = relay.logical_xor(call_754.astype('int64'), relay.reshape(var_756.astype('int64'), relay.shape_of(call_754))) # shape=(5, 11, 4)
bop_760 = relay.logical_xor(call_755.astype('int64'), relay.reshape(var_756.astype('int64'), relay.shape_of(call_755))) # shape=(5, 11, 4)
uop_774 = relay.sqrt(bop_757.astype('float32')) # shape=(5, 11, 4)
uop_776 = relay.sqrt(bop_760.astype('float32')) # shape=(5, 11, 4)
output = uop_774
output2 = uop_776
func_791 = relay.Function([var_756,], output)
mod['func_791'] = func_791
mod = relay.transform.InferType()(mod)
var_792 = relay.var("var_792", dtype = "float64", shape = (5, 11, 4))#candidate|792|(5, 11, 4)|var|float64
output = func_791(var_792)
func_793 = relay.Function([var_792], output)
mutated_mod['func_793'] = func_793
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_812 = func_361_call()
call_813 = func_361_call()
uop_825 = relay.erf(call_812.astype('float32')) # shape=(5, 11, 4)
uop_827 = relay.erf(call_813.astype('float32')) # shape=(5, 11, 4)
output = relay.Tuple([uop_825,])
output2 = relay.Tuple([uop_827,])
func_859 = relay.Function([], output)
mod['func_859'] = func_859
mod = relay.transform.InferType()(mod)
output = func_859()
func_860 = relay.Function([], output)
mutated_mod['func_860'] = func_860
mutated_mod = relay.transform.InferType()(mutated_mod)
var_872 = relay.var("var_872", dtype = "float64", shape = (7, 4, 7))#candidate|872|(7, 4, 7)|var|float64
var_873 = relay.var("var_873", dtype = "float64", shape = (7, 4, 7))#candidate|873|(7, 4, 7)|var|float64
bop_874 = relay.power(var_872.astype('float64'), relay.reshape(var_873.astype('float64'), relay.shape_of(var_872))) # shape=(7, 4, 7)
output = bop_874
output2 = bop_874
func_884 = relay.Function([var_872,var_873,], output)
mod['func_884'] = func_884
mod = relay.transform.InferType()(mod)
var_885 = relay.var("var_885", dtype = "float64", shape = (7, 4, 7))#candidate|885|(7, 4, 7)|var|float64
var_886 = relay.var("var_886", dtype = "float64", shape = (7, 4, 7))#candidate|886|(7, 4, 7)|var|float64
output = func_884(var_885,var_886,)
func_887 = relay.Function([var_885,var_886,], output)
mutated_mod['func_887'] = func_887
mutated_mod = relay.transform.InferType()(mutated_mod)
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_921 = func_397_call()
call_922 = func_397_call()
var_925 = relay.var("var_925", dtype = "float64", shape = (5, 11, 4))#candidate|925|(5, 11, 4)|var|float64
bop_926 = relay.bitwise_and(call_921.astype('uint8'), relay.reshape(var_925.astype('uint8'), relay.shape_of(call_921))) # shape=(5, 11, 4)
bop_929 = relay.bitwise_and(call_922.astype('uint8'), relay.reshape(var_925.astype('uint8'), relay.shape_of(call_922))) # shape=(5, 11, 4)
func_412_call = mod.get_global_var('func_412')
func_414_call = mutated_mod.get_global_var('func_414')
call_930 = func_412_call()
call_931 = func_412_call()
output = relay.Tuple([bop_926,call_930,])
output2 = relay.Tuple([bop_929,call_931,])
func_941 = relay.Function([var_925,], output)
mod['func_941'] = func_941
mod = relay.transform.InferType()(mod)
var_942 = relay.var("var_942", dtype = "float64", shape = (5, 11, 4))#candidate|942|(5, 11, 4)|var|float64
output = func_941(var_942)
func_943 = relay.Function([var_942], output)
mutated_mod['func_943'] = func_943
mutated_mod = relay.transform.InferType()(mutated_mod)
var_972 = relay.var("var_972", dtype = "float32", shape = (11, 13, 15))#candidate|972|(11, 13, 15)|var|float32
var_973 = relay.var("var_973", dtype = "float32", shape = (11, 13, 15))#candidate|973|(11, 13, 15)|var|float32
bop_974 = relay.floor_divide(var_972.astype('float32'), relay.reshape(var_973.astype('float32'), relay.shape_of(var_972))) # shape=(11, 13, 15)
bop_980 = relay.floor_mod(bop_974.astype('float32'), relay.reshape(var_973.astype('float32'), relay.shape_of(bop_974))) # shape=(11, 13, 15)
bop_990 = relay.bitwise_or(var_972.astype('int16'), relay.reshape(bop_980.astype('int16'), relay.shape_of(var_972))) # shape=(11, 13, 15)
output = relay.Tuple([bop_990,])
output2 = relay.Tuple([bop_990,])
func_1001 = relay.Function([var_972,var_973,], output)
mod['func_1001'] = func_1001
mod = relay.transform.InferType()(mod)
mutated_mod['func_1001'] = func_1001
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1001_call = mutated_mod.get_global_var('func_1001')
var_1003 = relay.var("var_1003", dtype = "float32", shape = (11, 13, 15))#candidate|1003|(11, 13, 15)|var|float32
var_1004 = relay.var("var_1004", dtype = "float32", shape = (11, 13, 15))#candidate|1004|(11, 13, 15)|var|float32
call_1002 = func_1001_call(var_1003,var_1004,)
output = call_1002
func_1005 = relay.Function([var_1003,var_1004,], output)
mutated_mod['func_1005'] = func_1005
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_1017 = relay.TupleGetItem(func_859_call(), 0)
call_1018 = relay.TupleGetItem(func_860_call(), 0)
func_884_call = mod.get_global_var('func_884')
func_887_call = mutated_mod.get_global_var('func_887')
const_1022 = relay.const([-5.258164,-4.342819,3.232182,7.254939,-1.794484,2.372272,-4.348939,-1.403640,-9.019920,3.854040,-6.452090,-8.515689,-8.990441,-8.613550,-9.573365,1.800407,3.689258,-4.369388,2.629300,0.788481,-9.795262,1.626417,3.789449,-9.648920,-3.890078,8.739878,1.944358,5.423899,-4.109610,4.154666,0.689131,0.171549,9.338737,2.976069,3.796918,-7.233136,-4.179257,9.170009,5.547713,1.427636,2.697096,2.374909,-1.052975,-4.833268,-9.437938,5.847317,-1.538023,6.432237,1.640427,-7.335070,8.800181,-5.238926,-9.444366,4.646345,6.433315,8.660955,5.254676,9.609607,9.377017,4.175036,-3.970221,8.286953,4.417597,-5.072898,-6.189497,-7.090098,8.350141,1.511112,-5.514110,-1.805136,4.708344,-9.872546,-5.054412,9.449189,9.216906,0.777501,3.100237,-1.072716,8.998044,1.353068,-6.894512,5.974534,9.725292,6.914493,-4.146981,9.217854,-1.308635,-2.272646,-3.901072,-3.981729,-6.098922,4.593822,4.063077,3.274746,-0.545696,-2.738846,-6.542403,-9.785019,-4.114783,1.562820,9.285109,-4.655258,-8.670153,-5.760122,-9.605746,-0.421486,0.751917,2.367312,7.796471,2.659004,5.818394,-0.903194,-9.644228,4.733814,4.169879,5.627874,-9.679923,-1.411533,-9.309190,0.715445,5.502746,-1.365813,0.042293,9.792001,-6.746601,-3.140751,-8.588146,1.090224,8.507618,7.797240,7.169708,-2.783891,9.311707,-3.682220,9.716541,-5.194959,3.685963,0.328192,-9.635637,4.332102,-5.155069,9.872017,5.975569,2.149005,4.882637,7.519556,8.137281,-5.026562,-9.476815,-4.012320,-1.413583,-9.218145,9.293436,-4.056441,3.503226,-0.510174,5.656366,-9.859970,-6.875202,-8.665610,4.220164,-9.861494,4.286194,8.149134,0.121780,6.393074,-8.532608,7.139765,-1.716263,-8.470930,-8.175480,5.075890,-1.942252,-2.196560,9.957609,-4.499940,-2.245681,7.714916,-2.328770,1.906027,-3.159740,0.808965,-5.077739,9.596166,2.886242,-8.118176,-3.006191,5.865250,-7.910126,-7.878792,-1.600191,-4.253203,6.110855,-4.585560,-9.393487,-5.985486], dtype = "float64")#candidate|1022|(196,)|const|float64
call_1021 = func_884_call(relay.reshape(const_1022.astype('float64'), [7, 4, 7]), relay.reshape(const_1022.astype('float64'), [7, 4, 7]), )
call_1023 = func_884_call(relay.reshape(const_1022.astype('float64'), [7, 4, 7]), relay.reshape(const_1022.astype('float64'), [7, 4, 7]), )
func_573_call = mod.get_global_var('func_573')
func_577_call = mutated_mod.get_global_var('func_577')
call_1038 = relay.TupleGetItem(func_573_call(relay.reshape(call_1017.astype('float32'), [5, 11, 4]), relay.reshape(call_1017.astype('bool'), [5, 11, 4]), ), 0)
call_1039 = relay.TupleGetItem(func_577_call(relay.reshape(call_1017.astype('float32'), [5, 11, 4]), relay.reshape(call_1017.astype('bool'), [5, 11, 4]), ), 0)
output = relay.Tuple([call_1017,call_1021,const_1022,call_1038,])
output2 = relay.Tuple([call_1018,call_1023,const_1022,call_1039,])
func_1043 = relay.Function([], output)
mod['func_1043'] = func_1043
mod = relay.transform.InferType()(mod)
mutated_mod['func_1043'] = func_1043
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1043_call = mutated_mod.get_global_var('func_1043')
call_1044 = func_1043_call()
output = call_1044
func_1045 = relay.Function([], output)
mutated_mod['func_1045'] = func_1045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_412_call = mod.get_global_var('func_412')
func_414_call = mutated_mod.get_global_var('func_414')
call_1058 = func_412_call()
call_1059 = func_412_call()
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_1063 = relay.TupleGetItem(func_941_call(relay.reshape(call_1058.astype('float64'), [5, 11, 4])), 0)
call_1064 = relay.TupleGetItem(func_943_call(relay.reshape(call_1058.astype('float64'), [5, 11, 4])), 0)
bop_1066 = relay.divide(call_1063.astype('float32'), relay.reshape(call_1058.astype('float32'), relay.shape_of(call_1063))) # shape=(5, 11, 4)
bop_1069 = relay.divide(call_1064.astype('float32'), relay.reshape(call_1059.astype('float32'), relay.shape_of(call_1064))) # shape=(5, 11, 4)
output = bop_1066
output2 = bop_1069
func_1072 = relay.Function([], output)
mod['func_1072'] = func_1072
mod = relay.transform.InferType()(mod)
output = func_1072()
func_1073 = relay.Function([], output)
mutated_mod['func_1073'] = func_1073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_1082 = relay.TupleGetItem(func_684_call(), 0)
call_1083 = relay.TupleGetItem(func_686_call(), 0)
output = call_1082
output2 = call_1083
func_1091 = relay.Function([], output)
mod['func_1091'] = func_1091
mod = relay.transform.InferType()(mod)
mutated_mod['func_1091'] = func_1091
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mutated_mod.get_global_var('func_1091')
call_1092 = func_1091_call()
output = call_1092
func_1093 = relay.Function([], output)
mutated_mod['func_1093'] = func_1093
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_1145 = func_1091_call()
call_1146 = func_1091_call()
uop_1161 = relay.asin(call_1145.astype('float64')) # shape=(5, 11, 4)
uop_1163 = relay.asin(call_1146.astype('float64')) # shape=(5, 11, 4)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1173 = func_1072_call()
call_1174 = func_1072_call()
func_1043_call = mod.get_global_var('func_1043')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_1190 = relay.TupleGetItem(func_1043_call(), 0)
call_1191 = relay.TupleGetItem(func_1045_call(), 0)
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_1231 = func_397_call()
call_1232 = func_397_call()
func_182_call = mod.get_global_var('func_182')
func_186_call = mutated_mod.get_global_var('func_186')
var_1242 = relay.var("var_1242", dtype = "int32", shape = ())#candidate|1242|()|var|int32
var_1243 = relay.var("var_1243", dtype = "int32", shape = (48,))#candidate|1243|(48,)|var|int32
call_1241 = relay.TupleGetItem(func_182_call(relay.reshape(var_1242.astype('int32'), []), relay.reshape(var_1243.astype('int32'), [1, 6, 8]), ), 0)
call_1244 = relay.TupleGetItem(func_186_call(relay.reshape(var_1242.astype('int32'), []), relay.reshape(var_1243.astype('int32'), [1, 6, 8]), ), 0)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_1245 = func_1072_call()
call_1246 = func_1072_call()
uop_1249 = relay.tan(uop_1161.astype('float32')) # shape=(5, 11, 4)
uop_1251 = relay.tan(uop_1163.astype('float32')) # shape=(5, 11, 4)
output = relay.Tuple([call_1173,call_1190,call_1231,call_1241,var_1242,var_1243,call_1245,uop_1249,])
output2 = relay.Tuple([call_1174,call_1191,call_1232,call_1244,var_1242,var_1243,call_1246,uop_1251,])
func_1255 = relay.Function([var_1242,var_1243,], output)
mod['func_1255'] = func_1255
mod = relay.transform.InferType()(mod)
mutated_mod['func_1255'] = func_1255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1255_call = mutated_mod.get_global_var('func_1255')
var_1257 = relay.var("var_1257", dtype = "int32", shape = ())#candidate|1257|()|var|int32
var_1258 = relay.var("var_1258", dtype = "int32", shape = (48,))#candidate|1258|(48,)|var|int32
call_1256 = func_1255_call(var_1257,var_1258,)
output = call_1256
func_1259 = relay.Function([var_1257,var_1258,], output)
mutated_mod['func_1259'] = func_1259
mutated_mod = relay.transform.InferType()(mutated_mod)
func_412_call = mod.get_global_var('func_412')
func_414_call = mutated_mod.get_global_var('func_414')
call_1337 = func_412_call()
call_1338 = func_412_call()
func_791_call = mod.get_global_var('func_791')
func_793_call = mutated_mod.get_global_var('func_793')
call_1339 = func_791_call(relay.reshape(call_1337.astype('float64'), [5, 11, 4]))
call_1340 = func_791_call(relay.reshape(call_1337.astype('float64'), [5, 11, 4]))
output = relay.Tuple([call_1337,call_1339,])
output2 = relay.Tuple([call_1338,call_1340,])
func_1344 = relay.Function([], output)
mod['func_1344'] = func_1344
mod = relay.transform.InferType()(mod)
mutated_mod['func_1344'] = func_1344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1344_call = mutated_mod.get_global_var('func_1344')
call_1345 = func_1344_call()
output = call_1345
func_1346 = relay.Function([], output)
mutated_mod['func_1346'] = func_1346
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1365 = relay.const([[[0.579824,-8.959289,1.700698,9.370238,-8.226357,0.835431,-8.953141,0.669618,2.247291,4.764661,-3.314759,-5.804054,5.227536,-6.753321],[-6.567345,-1.285469,3.472700,-5.847971,3.323433,0.796492,2.526778,-1.639074,8.155969,-9.493834,3.108489,-6.353440,4.889805,0.689999],[0.311388,-1.186254,9.242501,9.479223,-5.246906,1.019924,8.629985,6.220478,6.180713,-6.893062,3.814021,6.574030,8.200186,3.846470],[5.620199,2.670099,-8.024625,-8.498024,-3.012635,-7.952018,8.213351,-7.208293,-2.831824,-1.304691,9.162250,4.778474,9.879445,-4.613104],[-0.473679,-9.023496,-2.542842,-6.949058,4.299685,-0.010433,-8.076955,-0.738419,2.771373,-7.094636,6.750282,3.170039,-3.092423,4.973026],[-5.635914,-6.471336,9.204445,-0.626323,-5.515550,-7.531376,0.778570,-1.343764,-8.753933,6.530060,0.432475,3.980108,-3.079041,-5.563537],[9.076459,9.401317,8.912748,2.369244,-4.036103,-8.907869,-8.037063,-9.992416,3.531372,-0.441675,-9.295079,0.790759,0.001918,-5.908537]],[[-7.952100,-2.986818,-4.367660,6.127203,8.175114,5.699053,-3.423013,1.183824,-7.877115,-6.876667,-1.060456,2.091213,-0.642357,-6.514242],[-2.535246,-7.810404,9.229040,-6.162058,-2.065437,6.524282,-2.476614,5.624518,-8.028287,-2.975138,-2.324449,3.657703,7.142201,4.994505],[8.112900,1.589446,-2.180497,-0.042286,5.142187,-5.978631,-9.044131,8.637770,-4.471014,8.609339,4.183455,6.335881,-3.071450,-5.852294],[-8.536138,-7.648380,-7.079266,7.241064,5.195885,-9.510084,-5.046039,-6.291939,9.001921,-6.711530,-9.626125,-8.791453,6.400541,3.310156],[-4.429153,1.059889,-2.087731,6.944831,7.232505,5.636596,-6.124542,1.976809,-9.394884,-3.110796,-5.602896,9.485378,-8.748424,-3.641122],[-3.356391,-9.392960,-1.182311,1.221354,0.249305,7.300279,9.264274,3.138922,-7.740691,-8.961634,-6.988006,-8.844147,0.208443,8.937982],[-8.230132,9.115890,5.444240,7.611285,3.115502,-9.559748,2.923023,-7.122040,6.486113,4.374678,-2.393422,-9.184047,-2.777016,6.029676]],[[8.233710,7.385305,2.810103,-6.101855,-2.614570,-0.935151,-5.625223,-6.067839,-6.272080,-4.411114,-9.676824,8.911135,3.228143,7.335964],[3.660659,-8.664671,4.358611,-6.143630,-9.147887,-5.614344,-2.075389,5.185226,5.134257,2.674966,-5.095250,6.131897,1.864338,3.944204],[9.876004,-7.511431,-7.583381,8.809543,-6.873946,-1.977833,-5.602536,-7.954210,0.517883,2.992940,9.442621,-9.129150,-1.020982,4.754018],[-4.664143,-9.487497,1.983169,-8.639355,5.459423,-0.139207,9.569152,3.208676,8.801965,9.351407,4.688960,1.877568,2.132820,-9.699682],[-9.942799,4.792689,-0.676398,-8.416220,-3.651413,2.601122,-2.357067,4.658247,-9.161276,8.849342,-3.255991,-3.771253,3.261939,9.123652],[8.849714,-6.805407,5.478893,9.893924,6.688233,9.871866,-4.226437,-5.038093,-2.372008,6.339858,-3.558013,-3.274944,3.280900,-5.497647],[2.542683,8.769853,4.313579,-0.660038,5.332626,-4.494049,2.354887,-2.665335,7.620310,-3.319766,-4.206936,-8.338118,-3.271080,-0.847462]],[[-2.293924,-7.861825,-8.112702,-0.209000,7.510205,-4.929988,-0.267369,9.023662,-5.677794,-3.782834,-4.836576,-8.450626,-1.674994,5.084601],[6.732251,-9.607474,-0.230272,5.969424,-3.779601,-7.690747,-9.888385,-4.615994,-3.105598,-4.179144,1.288213,-0.527178,0.974943,-2.460163],[1.465288,-0.115921,6.069173,-7.791673,2.406138,-4.243713,-7.697625,9.353255,2.071650,7.397064,-3.935860,6.737851,-9.594267,3.593208],[-8.673027,3.751825,-6.561688,-3.340426,-2.086247,0.992861,4.544261,5.370598,7.076357,-4.827702,-0.197322,-7.220424,-2.789107,-4.137042],[6.604130,-8.457184,-2.983924,7.937007,-3.232500,-5.826463,5.991609,-4.749106,-4.231453,-0.073019,6.664081,-2.738231,-3.446831,-9.644413],[-2.138394,-8.192974,-3.272825,4.458537,-0.974823,2.299846,8.096278,-1.650887,-6.552873,1.244219,-3.362779,-1.052411,-5.910279,-6.357924],[4.168029,9.315387,6.383766,2.676746,1.552345,-0.405032,6.247606,-6.153074,-2.296947,9.940041,2.335057,9.015251,-2.277494,4.735426]],[[-8.875993,-9.125145,-4.467936,-0.170799,1.922651,-6.309318,-2.352593,-6.100037,-1.389113,-0.497133,9.053736,2.034556,-1.046081,2.341476],[-8.414083,-0.512807,-7.943505,-6.782385,-9.942234,-7.537156,-0.455227,-0.945359,-3.187287,6.012963,5.735674,8.177488,6.360015,-7.625663],[8.016823,6.335654,-3.653585,-7.741579,-5.010584,-9.469579,5.883941,-8.005747,7.298934,5.550366,5.030305,-5.126353,-1.031749,-8.068842],[9.263156,-0.905889,-8.804188,-1.994534,3.264747,6.598258,-0.233281,-1.124746,-9.291972,2.417996,-0.879701,2.467565,3.903879,-3.862325],[6.028145,-4.115303,1.880533,0.921914,-5.537252,1.784197,5.476432,3.256151,-6.755375,6.637235,-7.539602,-6.373914,5.909844,-0.149304],[1.973887,6.320724,7.794776,6.706295,-5.370266,-2.848858,0.482376,-3.353712,-2.538406,-9.601286,2.489672,-0.812740,-1.740627,-0.684239],[-9.264286,1.668335,-8.011796,4.558691,-4.757974,-5.931315,0.515479,4.779180,-1.709527,2.062471,1.665570,3.202224,-6.725429,-9.029793]],[[-4.841367,-4.616815,4.352526,6.908908,-2.066055,-3.578288,1.958815,6.883770,6.669469,3.410808,-6.839702,3.711612,-8.606258,3.631053],[-4.786460,-8.256274,-7.458778,3.410120,-3.585040,7.868099,1.414594,5.525322,4.035924,-8.445677,2.564683,-0.124605,-0.280062,5.547532],[1.303159,0.943378,-2.248622,-3.374685,0.507782,-5.705791,-8.253548,-4.407207,1.010463,0.448190,7.980109,-7.216463,0.338110,-0.141366],[-7.291419,7.521100,-0.841077,3.814638,-1.384126,-9.229455,8.535489,1.712673,-2.719679,-0.541120,0.060194,-8.900531,8.563945,7.904227],[-4.015722,-4.359296,0.387939,-1.431824,6.799829,-2.784963,6.431963,9.286365,8.195053,5.741600,-1.879501,-5.935745,4.997624,-5.884431],[1.600973,4.983824,-9.583588,-3.265975,3.293022,4.666242,-5.142969,-6.698205,-6.843124,-9.249958,-6.282550,-2.522579,7.156038,-4.107822],[4.515604,5.983022,-9.128887,-1.303103,1.786513,-6.798806,8.693799,2.588120,4.851821,-1.077050,3.589362,-2.406249,-9.203809,-4.163334]],[[8.700635,-8.958677,-9.513514,3.345581,-2.662034,9.424154,-7.762350,3.657877,5.590703,5.083402,-7.545082,3.391295,-3.191263,-3.192417],[-7.429527,9.208185,4.342446,-5.409359,1.827661,7.299566,-5.731702,9.324723,-0.819626,-4.728251,2.868964,2.737052,6.289517,0.259319],[-6.070619,-2.450008,8.167894,-1.964058,9.968589,-8.909402,-4.723813,4.824452,-8.436820,3.989367,6.891206,-3.089731,0.624217,-0.915633],[-7.323917,-2.513713,3.185712,7.937889,-8.669296,-4.352371,8.649414,2.634360,-1.437438,-3.911727,6.968182,5.684291,4.971043,-9.020185],[6.151836,-1.223911,-4.045688,-1.248740,4.791751,-4.078259,4.385283,-9.654760,8.130452,-6.884200,-0.691385,-4.486761,-5.902249,-2.737149],[-3.487678,-2.534122,8.630399,0.742081,-3.598500,-7.635993,-6.372355,4.330434,1.237232,-7.604064,2.914099,-1.301092,5.108534,-0.112471],[-2.849848,7.694456,0.006090,3.692372,-6.122028,-7.577115,-9.554539,5.338688,-6.927351,7.177231,-5.884782,-0.753018,-9.903588,7.139422]],[[-2.565806,-8.085396,-7.893978,0.889130,3.632019,-8.193938,8.059543,-8.526388,4.724104,-7.922516,1.408737,3.924052,7.369375,1.404416],[-8.562814,6.331025,-1.452205,-9.761062,-9.123604,-8.194848,-8.892157,5.913033,-2.198754,4.842092,0.571004,9.946250,2.719758,-6.826916],[-3.163089,5.869078,-0.938267,6.226248,-1.381979,4.930988,5.407666,-3.806069,4.413786,-1.875780,-3.274127,9.622513,2.146049,-6.309067],[-6.972046,-9.204585,-1.127967,7.851369,-2.540355,-3.914313,-6.999043,9.554095,7.248171,2.687399,-7.595380,-3.810963,-2.297495,-6.495959],[-6.253225,-9.856561,-8.523260,-6.482997,-7.909910,0.333409,-8.429457,4.783953,-4.859347,5.700285,3.722881,-3.586038,-6.244132,-1.538963],[-2.385229,-1.984321,4.413791,5.278935,4.167101,-0.306863,-0.521688,7.658962,8.054833,7.336939,7.713068,-0.495291,-6.691214,-5.770627],[1.892983,0.892939,-2.010571,7.075835,-0.356902,7.249387,-3.556904,-2.784632,1.992120,2.007563,-8.346520,-0.920420,9.262592,-9.520508]],[[2.263861,-8.043592,9.396940,1.512078,-6.951364,1.748347,6.553380,-1.400733,7.914164,-5.155084,-4.392097,5.487635,3.752550,9.875993],[-9.009370,-9.203166,-4.900218,4.169150,-3.804573,6.303279,9.400961,6.095484,0.830291,-3.330881,-0.688948,-5.671508,-2.025385,-5.535151],[6.981246,5.610471,5.223722,-6.115559,-1.556534,-5.480884,-2.213731,5.532663,-2.997700,-3.577296,4.465259,-6.238588,-9.833652,-4.995697],[6.468414,-1.942563,-0.116227,-3.476829,2.035265,-0.325628,-3.490873,-1.607695,-6.755826,-6.627504,-2.193899,9.897961,4.760919,-7.408345],[-7.338839,7.323490,7.254078,-6.799918,0.030090,5.357466,6.626204,-4.305645,-5.887419,-8.845554,9.092968,-7.335290,-9.344081,9.286621],[5.344395,3.496688,-0.661290,1.133500,-1.108739,-7.575150,9.583683,-5.742650,7.987556,-8.062185,4.384688,-0.093555,-8.266565,-8.610953],[-9.593817,-8.227315,8.983842,9.980814,-6.337364,6.448161,0.998243,-0.222464,-4.483965,1.203854,-4.876366,2.288770,3.748350,-8.854447]],[[-3.056202,-4.789035,-3.973475,1.556282,-7.396340,9.257091,2.414225,7.224685,-9.384990,9.418637,-1.654826,-4.395999,5.136400,-2.217203],[-5.450219,-6.882218,0.758861,7.813152,9.350827,-4.987464,-9.990139,6.532650,-2.543709,-9.830623,-4.975187,0.054814,-4.135005,8.688967],[-9.539965,-4.821940,-3.886221,5.509367,3.731591,4.691803,1.533883,-6.959882,-8.788301,-4.949514,-9.994793,5.750294,-5.137128,0.500082],[0.473843,-5.536038,-4.069088,-3.190951,0.009578,0.563727,-2.459652,-9.771997,-8.975649,1.077369,-7.059628,4.168086,-6.799810,6.823404],[-8.876554,-9.121733,-0.711790,2.204982,6.221021,6.542721,9.483040,-4.531849,-8.489528,-2.170005,1.421774,5.864856,7.128649,0.556395],[4.507815,-3.918884,9.779867,7.815946,-9.798593,4.226860,-6.851604,-0.741920,7.165890,-2.216412,0.676830,-4.493030,-3.709551,-3.651831],[-6.001391,-0.996660,1.145332,3.292026,6.718051,-6.448589,3.609506,7.025196,-0.486687,-3.008921,-5.942292,8.295441,5.025154,0.557690]],[[3.393549,7.066374,8.825242,-5.291116,-2.341189,2.896638,-8.409598,2.887364,6.682868,-5.354519,7.083938,3.569679,9.787185,6.110896],[-5.241725,-9.967970,8.188960,-7.265475,8.184838,1.863363,-6.556233,0.285814,-1.359897,1.821245,-1.545554,6.835331,-6.462995,1.798361],[-9.384965,-2.070751,3.652831,-4.177407,-1.230597,4.068572,4.959226,6.783882,-7.592624,3.534154,-5.526613,-7.003208,-3.262558,-3.692249],[6.788485,-5.399505,-9.015173,-5.477329,5.517684,-8.766270,1.376690,-1.981556,-2.001388,6.264266,-6.193528,4.657336,2.085987,2.114848],[-4.687701,-6.544894,-6.137292,6.860343,8.195984,-8.613479,-5.074878,-7.130838,3.246898,9.082874,-8.012693,-7.606176,0.198615,0.246307],[3.491901,-8.714260,-4.005240,7.801149,8.614231,-0.117553,3.590082,7.539093,8.109485,3.158634,-1.873574,0.108574,9.413070,-7.014162],[3.793605,1.231638,-1.979692,-8.713291,-0.138776,7.351333,-8.138442,-7.030056,5.794699,-6.648204,6.058246,1.187194,-3.622906,1.603732]],[[-9.821914,-3.883681,7.650684,-7.692542,2.856755,9.912666,2.260404,8.593025,-6.417261,0.038747,9.306399,-7.720517,4.697152,9.904222],[-5.494016,-9.879340,-8.481562,1.276459,-6.963499,9.186110,-8.948603,-1.971822,-1.979817,-4.408411,2.424902,-6.374636,0.995029,-5.656029],[-1.677683,-2.443818,-9.098547,8.197714,6.571097,-8.331782,-9.603809,4.685477,-8.791278,-3.897901,4.909166,4.798679,-6.589712,5.799268],[8.063725,8.521219,7.193063,-6.260813,-6.411247,-9.835833,-9.652313,7.416208,9.885871,-8.976896,-3.553909,-9.147216,4.208543,9.069054],[5.827787,1.585846,-6.211234,-5.966652,-8.572452,6.990158,-1.874172,-2.690769,-6.368055,8.436813,-7.648621,-3.446813,0.281853,-6.284911],[-7.564049,-0.898497,-4.710784,-6.354947,-6.487382,8.452982,-9.496100,8.442258,-5.608591,6.904813,-6.314808,-7.903061,-6.086247,4.374793],[4.316058,-6.026403,8.655417,9.778254,-8.776183,-8.594848,-7.946794,0.784389,-3.216737,8.110367,-9.754009,-2.458486,-1.547811,5.420889]]], dtype = "float32")#candidate|1365|(12, 7, 14)|const|float32
uop_1366 = relay.rsqrt(const_1365.astype('float32')) # shape=(12, 7, 14)
output = relay.Tuple([uop_1366,])
output2 = relay.Tuple([uop_1366,])
func_1368 = relay.Function([], output)
mod['func_1368'] = func_1368
mod = relay.transform.InferType()(mod)
output = func_1368()
func_1369 = relay.Function([], output)
mutated_mod['func_1369'] = func_1369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_1373 = func_361_call()
call_1374 = func_361_call()
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_1375 = func_397_call()
call_1376 = func_397_call()
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_1384 = relay.TupleGetItem(func_684_call(), 0)
call_1385 = relay.TupleGetItem(func_686_call(), 0)
uop_1393 = relay.cos(call_1384.astype('float64')) # shape=(5, 11, 4)
uop_1395 = relay.cos(call_1385.astype('float64')) # shape=(5, 11, 4)
output = relay.Tuple([call_1373,call_1375,uop_1393,])
output2 = relay.Tuple([call_1374,call_1376,uop_1395,])
func_1398 = relay.Function([], output)
mod['func_1398'] = func_1398
mod = relay.transform.InferType()(mod)
output = func_1398()
func_1399 = relay.Function([], output)
mutated_mod['func_1399'] = func_1399
mutated_mod = relay.transform.InferType()(mutated_mod)
func_412_call = mod.get_global_var('func_412')
func_414_call = mutated_mod.get_global_var('func_414')
call_1421 = func_412_call()
call_1422 = func_412_call()
output = call_1421
output2 = call_1422
func_1425 = relay.Function([], output)
mod['func_1425'] = func_1425
mod = relay.transform.InferType()(mod)
mutated_mod['func_1425'] = func_1425
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1425_call = mutated_mod.get_global_var('func_1425')
call_1426 = func_1425_call()
output = call_1426
func_1427 = relay.Function([], output)
mutated_mod['func_1427'] = func_1427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_1552 = func_480_call()
call_1553 = func_480_call()
var_1565 = relay.var("var_1565", dtype = "float32", shape = (5, 11, 4))#candidate|1565|(5, 11, 4)|var|float32
bop_1566 = relay.logical_and(call_1552.astype('bool'), relay.reshape(var_1565.astype('bool'), relay.shape_of(call_1552))) # shape=(5, 11, 4)
bop_1569 = relay.logical_and(call_1553.astype('bool'), relay.reshape(var_1565.astype('bool'), relay.shape_of(call_1553))) # shape=(5, 11, 4)
output = bop_1566
output2 = bop_1569
func_1575 = relay.Function([var_1565,], output)
mod['func_1575'] = func_1575
mod = relay.transform.InferType()(mod)
var_1576 = relay.var("var_1576", dtype = "float32", shape = (5, 11, 4))#candidate|1576|(5, 11, 4)|var|float32
output = func_1575(var_1576)
func_1577 = relay.Function([var_1576], output)
mutated_mod['func_1577'] = func_1577
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1582 = relay.var("var_1582", dtype = "float32", shape = (7, 8, 7))#candidate|1582|(7, 8, 7)|var|float32
const_1583 = relay.const([[[6.854852,-4.995352,6.209213,-6.082715,9.946534,5.108930,7.345630],[0.109454,-1.132249,-0.284178,-7.262231,9.658923,7.882982,5.692471],[-0.035918,3.090167,-4.659749,8.271450,-2.142051,-6.175027,-8.520264],[3.310814,2.874764,4.896137,9.988392,-4.494139,2.801813,-1.725689],[-7.371504,-2.023477,-3.769524,-9.589625,4.564471,-1.045647,0.761530],[-3.937904,-6.794008,7.316892,-8.269221,-0.630347,7.272791,3.564827],[-9.803161,9.300953,8.984068,5.885466,1.437700,-5.955992,1.253512],[-1.297432,-6.731839,-2.835360,9.264224,-2.001185,-6.077678,5.577504]],[[6.001508,0.462072,-0.896849,-8.621385,-6.323333,6.782418,9.660799],[-9.176226,4.294812,0.554463,6.939210,-0.213019,-0.729737,-9.711813],[0.087347,-3.431867,4.282696,-8.938665,-1.333997,1.893546,-7.848030],[-6.729433,2.945586,7.137209,-9.669727,-3.757094,-5.866801,-0.285095],[6.960914,-1.371373,-1.081854,3.314689,-3.415933,4.782738,-7.036681],[8.267079,1.157964,-1.634002,-3.739448,3.307169,-0.573011,1.057444],[1.243522,4.863092,-4.064446,2.851316,-5.671111,-2.758157,4.024841],[1.795007,7.938398,-3.927242,3.294636,1.754872,-1.296354,-9.959908]],[[-6.634977,-1.548198,9.015282,-7.552660,4.420347,-8.790423,-3.002355],[-6.201389,-5.288985,7.035282,-6.019864,-2.448618,-7.280036,7.800132],[6.802786,0.043642,8.309300,5.970880,-9.630248,3.844549,9.078238],[3.024782,-0.007763,5.444495,-7.765906,-1.075658,6.275261,-3.185300],[-6.203832,-1.864959,0.987900,3.299391,6.920344,3.350142,-2.970621],[3.540206,-0.925578,9.466357,-7.291315,3.278180,7.451393,3.546697],[-5.620194,-1.059884,-5.225135,-4.237811,4.679092,-3.328973,-3.335663],[-0.949132,-6.708301,0.402500,-6.687082,-5.173219,8.085287,4.706832]],[[6.928404,2.864293,-7.746281,1.083301,9.855568,-2.651210,2.269529],[6.027972,-5.969346,6.022016,-3.925018,0.402789,5.776443,9.973406],[1.494978,-5.588062,-0.279216,3.548153,1.946660,9.587871,-9.809813],[4.846662,-4.903527,-3.659948,-4.898012,-4.609156,-4.096379,-6.386849],[6.001396,-1.187079,-6.913403,4.199062,7.063847,-7.596114,7.164072],[6.649373,2.894196,-0.745770,6.090804,6.883722,-9.300011,-9.972601],[3.254308,-2.598322,9.554377,-5.625852,5.926983,-4.671591,-5.720120],[-0.899302,-3.997280,5.488214,-2.221939,9.477536,-6.693263,-1.176899]],[[-5.610552,1.877809,7.786839,-4.669730,6.891888,-8.776341,5.077169],[9.454190,0.754701,5.962946,4.083869,-9.459847,-5.271269,9.708142],[-3.283674,8.726085,4.029824,-8.988187,3.130615,7.516489,8.597512],[6.631949,-6.658881,-7.219735,-1.726498,2.132207,8.410575,-0.825254],[0.740403,-4.369298,3.038672,8.831675,5.320415,0.178762,-7.771621],[6.531892,-5.412272,-2.972531,3.869865,8.560159,3.305090,1.063156],[-5.915966,-1.825167,0.129916,7.173378,8.878114,1.809309,-6.112106],[7.404160,1.012440,8.744046,3.410635,-9.329336,-0.622550,5.409678]],[[-9.341400,-5.559938,-7.819031,6.209892,-0.448005,-3.401657,0.001762],[-3.357411,-5.560791,-6.739417,-3.581100,5.210106,-1.520687,-3.188563],[5.166579,-1.148445,-9.701706,-6.847680,3.066365,-0.834736,-7.425126],[7.187256,5.758330,-0.707589,9.851081,8.118021,-7.562833,-5.125122],[1.567673,5.041224,-3.138005,-3.743805,7.357818,3.513711,-5.464270],[-2.309484,-3.937246,-6.889031,3.012089,5.115182,-0.788721,-3.773039],[9.967469,7.345094,0.172611,-4.000270,-8.506016,-4.228755,9.248322],[-4.046027,1.913582,3.501827,1.106534,7.564079,-6.779044,6.713370]],[[-5.618679,7.006043,-1.317157,-3.493396,1.627390,1.845414,1.090448],[8.808439,5.195601,0.522913,-1.193138,-7.436289,-5.648475,-5.249663],[-6.507638,8.541062,9.304007,4.368282,4.537230,6.421376,-0.839180],[-3.003762,-5.479860,-8.295427,-8.932654,5.345092,-9.888152,-9.376503],[1.445869,8.082819,-2.165242,-7.061058,7.985509,-2.850002,1.357368],[-2.632269,-0.553974,-2.579277,-4.578393,8.760503,-0.014128,-4.311113],[-6.782283,7.844093,2.357410,-6.234159,-1.814027,-4.877876,-1.589780],[-3.539650,-5.526673,0.248486,-8.192365,-8.330079,-1.687276,1.763014]]], dtype = "float32")#candidate|1583|(7, 8, 7)|const|float32
bop_1584 = relay.equal(var_1582.astype('bool'), relay.reshape(const_1583.astype('bool'), relay.shape_of(var_1582))) # shape=(7, 8, 7)
output = relay.Tuple([bop_1584,])
output2 = relay.Tuple([bop_1584,])
func_1587 = relay.Function([var_1582,], output)
mod['func_1587'] = func_1587
mod = relay.transform.InferType()(mod)
var_1588 = relay.var("var_1588", dtype = "float32", shape = (7, 8, 7))#candidate|1588|(7, 8, 7)|var|float32
output = func_1587(var_1588)
func_1589 = relay.Function([var_1588], output)
mutated_mod['func_1589'] = func_1589
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_1705 = relay.TupleGetItem(func_859_call(), 0)
call_1706 = relay.TupleGetItem(func_860_call(), 0)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_1707 = func_1091_call()
call_1708 = func_1091_call()
output = relay.Tuple([call_1705,call_1707,])
output2 = relay.Tuple([call_1706,call_1708,])
func_1719 = relay.Function([], output)
mod['func_1719'] = func_1719
mod = relay.transform.InferType()(mod)
output = func_1719()
func_1720 = relay.Function([], output)
mutated_mod['func_1720'] = func_1720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_412_call = mod.get_global_var('func_412')
func_414_call = mutated_mod.get_global_var('func_414')
call_1747 = func_412_call()
call_1748 = func_412_call()
const_1752 = relay.const([[[5.977252,-4.689062,-0.433523,6.015440],[4.927238,-2.749202,3.451124,8.918320],[5.848711,-9.550349,-2.293688,2.417904],[-6.218638,2.174983,4.405052,2.385487],[4.253012,0.637095,-5.558423,-3.382413],[-5.731900,0.066737,-1.337709,0.391714],[-0.949731,-9.994902,9.346001,-9.277113],[-7.381052,-0.574576,7.774925,8.602824],[4.996977,-6.272191,7.794105,3.355488],[9.004072,3.684527,-6.840472,1.736247],[-3.149470,0.105811,0.086164,2.566328]],[[7.025847,1.666900,-1.839760,-9.184024],[0.787963,6.205862,6.645406,-9.651708],[8.183424,3.953464,-9.473203,-1.987932],[-9.668276,4.457547,-6.523329,-3.655502],[-2.966574,-9.745309,-4.671840,-3.533253],[4.432180,-8.263771,6.938601,-8.680250],[4.927328,-5.044245,-8.620746,-1.825454],[-1.671610,0.109413,3.738149,4.209341],[1.126981,-5.187462,-0.320274,-5.867525],[-7.940911,-5.940057,1.305760,1.318180],[-7.010640,4.272146,-3.200780,-6.942907]],[[2.283434,2.056749,6.932354,-1.487818],[-3.662407,-0.341049,2.578190,4.731424],[0.748408,9.983333,-2.129070,0.665205],[-3.889088,3.379415,2.116981,-3.793707],[0.589666,6.489727,-3.881510,-9.092118],[-1.435194,5.971034,6.204481,1.614414],[-7.166219,3.236721,2.542977,-1.974659],[5.092819,4.374374,0.392941,3.534674],[1.639609,7.898161,-0.191099,3.054325],[-5.328690,2.942705,5.831743,-4.842177],[9.018410,-3.887064,7.203571,1.108126]],[[-1.570851,9.770027,-2.109696,6.981025],[5.848944,3.063309,-1.200956,-2.362673],[0.903403,-1.717198,-9.450449,-3.948128],[-8.561579,3.904651,2.353425,2.277703],[4.943405,4.664306,0.865042,1.013153],[5.979716,0.716177,8.515707,-0.041489],[3.434737,5.664479,-6.002023,4.040342],[-3.483229,-6.681323,9.684034,-5.216200],[-2.656848,-5.383880,-2.883911,-2.852945],[-8.307773,1.378454,7.749430,-3.437464],[-8.454910,-6.783957,-5.015119,1.154245]],[[-3.373412,-8.672067,3.887834,-9.121597],[2.084982,-3.039221,8.803561,3.343663],[-3.300108,4.788519,0.257127,-2.479850],[-4.762324,-8.533590,-6.739888,9.447733],[5.913695,8.447615,-9.374380,-4.867306],[-6.421590,6.204837,2.522703,-9.507027],[8.417484,9.641362,7.821876,-8.833384],[-1.211054,-4.945164,6.394078,-4.789776],[-2.525147,2.894017,5.982451,-3.247733],[-3.849447,3.184024,-9.966361,9.142567],[-6.145197,-0.064598,-3.202173,5.202192]]], dtype = "float32")#candidate|1752|(5, 11, 4)|const|float32
bop_1753 = relay.less(call_1747.astype('bool'), relay.reshape(const_1752.astype('bool'), relay.shape_of(call_1747))) # shape=(5, 11, 4)
bop_1756 = relay.less(call_1748.astype('bool'), relay.reshape(const_1752.astype('bool'), relay.shape_of(call_1748))) # shape=(5, 11, 4)
output = bop_1753
output2 = bop_1756
func_1758 = relay.Function([], output)
mod['func_1758'] = func_1758
mod = relay.transform.InferType()(mod)
output = func_1758()
func_1759 = relay.Function([], output)
mutated_mod['func_1759'] = func_1759
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1043_call = mod.get_global_var('func_1043')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_1783 = relay.TupleGetItem(func_1043_call(), 1)
call_1784 = relay.TupleGetItem(func_1045_call(), 1)
output = call_1783
output2 = call_1784
func_1794 = relay.Function([], output)
mod['func_1794'] = func_1794
mod = relay.transform.InferType()(mod)
output = func_1794()
func_1795 = relay.Function([], output)
mutated_mod['func_1795'] = func_1795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1813 = relay.var("var_1813", dtype = "uint16", shape = (11, 11, 7))#candidate|1813|(11, 11, 7)|var|uint16
var_1814 = relay.var("var_1814", dtype = "uint16", shape = (11, 11, 7))#candidate|1814|(11, 11, 7)|var|uint16
bop_1815 = relay.maximum(var_1813.astype('uint16'), relay.reshape(var_1814.astype('uint16'), relay.shape_of(var_1813))) # shape=(11, 11, 7)
func_1368_call = mod.get_global_var('func_1368')
func_1369_call = mutated_mod.get_global_var('func_1369')
call_1820 = relay.TupleGetItem(func_1368_call(), 0)
call_1821 = relay.TupleGetItem(func_1369_call(), 0)
output = relay.Tuple([bop_1815,call_1820,])
output2 = relay.Tuple([bop_1815,call_1821,])
func_1824 = relay.Function([var_1813,var_1814,], output)
mod['func_1824'] = func_1824
mod = relay.transform.InferType()(mod)
mutated_mod['func_1824'] = func_1824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1824_call = mutated_mod.get_global_var('func_1824')
var_1826 = relay.var("var_1826", dtype = "uint16", shape = (11, 11, 7))#candidate|1826|(11, 11, 7)|var|uint16
var_1827 = relay.var("var_1827", dtype = "uint16", shape = (11, 11, 7))#candidate|1827|(11, 11, 7)|var|uint16
call_1825 = func_1824_call(var_1826,var_1827,)
output = call_1825
func_1828 = relay.Function([var_1826,var_1827,], output)
mutated_mod['func_1828'] = func_1828
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1091_call = mod.get_global_var('func_1091')
func_1093_call = mutated_mod.get_global_var('func_1093')
call_1844 = func_1091_call()
call_1845 = func_1091_call()
output = relay.Tuple([call_1844,])
output2 = relay.Tuple([call_1845,])
func_1846 = relay.Function([], output)
mod['func_1846'] = func_1846
mod = relay.transform.InferType()(mod)
mutated_mod['func_1846'] = func_1846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1846_call = mutated_mod.get_global_var('func_1846')
call_1847 = func_1846_call()
output = call_1847
func_1848 = relay.Function([], output)
mutated_mod['func_1848'] = func_1848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_1868 = func_361_call()
call_1869 = func_361_call()
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_1872 = func_526_call()
call_1873 = func_526_call()
uop_1874 = relay.asinh(call_1872.astype('float32')) # shape=(5, 11, 4)
uop_1876 = relay.asinh(call_1873.astype('float32')) # shape=(5, 11, 4)
output = relay.Tuple([call_1868,uop_1874,])
output2 = relay.Tuple([call_1869,uop_1876,])
func_1883 = relay.Function([], output)
mod['func_1883'] = func_1883
mod = relay.transform.InferType()(mod)
mutated_mod['func_1883'] = func_1883
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1883_call = mutated_mod.get_global_var('func_1883')
call_1884 = func_1883_call()
output = call_1884
func_1885 = relay.Function([], output)
mutated_mod['func_1885'] = func_1885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mod.get_global_var('func_1368')
func_1369_call = mutated_mod.get_global_var('func_1369')
call_1891 = relay.TupleGetItem(func_1368_call(), 0)
call_1892 = relay.TupleGetItem(func_1369_call(), 0)
func_1398_call = mod.get_global_var('func_1398')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_1909 = relay.TupleGetItem(func_1398_call(), 0)
call_1910 = relay.TupleGetItem(func_1399_call(), 0)
const_1914 = relay.const([[[8.625845,-0.657709,5.449252,-4.541583,8.051041,5.863505,-9.587416,-7.832309,-2.611876,3.453723,8.166673,2.511053,-7.649240,-0.722870],[9.975987,9.772283,6.227355,3.180609,6.727647,6.034033,-8.912399,3.233578,8.794111,7.370894,6.506281,4.948702,-5.800279,9.000187],[-8.707599,-0.460517,3.950238,-9.608623,1.109587,-4.775456,8.131201,6.025321,-9.696832,-4.703642,-2.739337,5.483156,1.720378,6.260213],[6.125040,-4.387503,-4.396458,8.548443,8.105220,-8.693385,-3.047344,2.948626,-4.220153,3.509994,-1.045244,4.593076,-8.622192,-5.074924],[1.732883,4.623118,6.717055,-7.461568,-1.788375,5.577121,9.255480,-8.361284,-3.688120,3.700630,-1.808375,0.206385,9.605975,-8.836186],[4.587052,8.272523,-0.284825,7.358938,-2.861484,9.439978,-3.856302,-0.843752,-6.218804,1.653106,2.719739,6.592422,7.705409,-9.869786],[8.436283,-7.815490,6.051975,-1.321322,5.887161,7.130344,3.591256,-4.252565,-4.810199,-0.344404,-9.691330,9.228238,-0.380058,7.319853]],[[-7.996798,-5.907848,-1.119394,-1.295997,-7.503704,1.316007,9.112629,-7.978281,8.066323,-8.478635,0.909855,-0.198517,-4.593214,0.010213],[1.477992,-8.591551,-4.089290,8.098730,-3.421124,7.372013,-0.968247,-6.137078,8.849682,3.585678,8.272914,-4.121093,-0.716194,-6.809774],[9.793689,7.150815,3.788227,-9.535267,8.161687,-5.737352,1.272073,-3.541799,7.279083,5.713484,2.579679,4.182990,-6.021825,-3.506349],[3.690320,6.282925,-2.199355,2.953959,6.301692,-6.817842,0.099056,-2.314809,-1.684868,4.560083,4.329165,-0.451525,6.365763,8.071064],[-5.746956,-9.546631,7.662365,-9.908916,-0.800100,8.165489,4.846614,-5.481849,-9.848620,8.087128,-4.289208,-6.603844,-6.667353,-2.405574],[5.015187,4.353021,3.595866,9.420177,-5.171586,5.374731,2.328217,-5.752324,-8.551122,9.193577,9.909971,3.966620,0.887383,6.096981],[-0.949315,5.008727,5.406945,4.151614,-5.494356,9.275899,-7.088102,-1.566096,7.261308,-5.236038,0.449197,3.834062,0.573365,-7.553812]],[[-9.837257,-7.039581,-1.362579,-4.380618,-1.341792,-2.728162,-0.556385,7.775733,-9.058028,-4.712093,-3.857386,0.932438,3.832188,-8.115153],[9.301549,3.677552,-2.933866,2.089833,-5.370998,4.374728,9.966382,6.653562,8.885472,6.473590,-9.378320,-0.910596,-2.832946,2.708207],[-5.939268,-0.250705,-0.749275,0.700028,9.919364,0.527307,6.925052,0.544927,8.071731,-7.966414,6.578333,-5.696303,-9.714718,2.535487],[3.327911,-2.439415,-2.006425,3.451800,-0.900024,-6.969166,8.503038,0.710962,-0.925896,-4.519595,-9.975483,-1.461778,-0.030095,5.304442],[0.086204,2.313280,8.418148,-4.171798,2.090721,6.824898,5.123162,0.252902,1.050252,3.659133,0.049260,4.270938,-9.383281,-3.532336],[4.226201,6.479494,-5.223655,0.198579,-0.702875,7.099780,4.684847,-9.176233,-6.956328,-3.244221,-3.656572,0.602497,7.534962,5.054176],[1.297970,-4.902757,-3.529639,2.747054,-3.166110,-2.227371,4.665708,-6.197627,-4.074677,0.701767,7.453944,9.852915,6.818343,9.264950]],[[2.109585,-8.289965,-3.318242,9.641518,4.266155,4.298664,8.726561,-0.071372,-0.229478,-0.918095,5.187469,6.051176,3.054804,8.044013],[-9.458326,4.759286,3.339228,-8.787421,-6.424610,-7.465994,-9.930927,5.273228,-5.615200,-5.129852,7.339768,4.086502,-1.706846,2.780569],[5.143170,-0.911330,1.358550,-7.831902,-9.340748,9.342526,-5.861854,-3.595443,7.869764,1.931553,2.071773,-6.044572,-9.029468,-9.408210],[9.854788,-1.560019,-7.049917,-4.527195,-8.493348,-0.525091,0.827813,9.101497,-8.732619,-5.161060,7.862523,3.612715,-3.229534,6.575394],[7.408678,5.044092,3.480181,-2.384922,0.910333,-5.186644,1.342860,-3.987964,-2.452323,-7.952736,3.666250,-2.142253,-5.720647,7.744573],[-2.939913,7.855456,-8.742432,-8.515014,-7.501774,1.022249,1.249003,6.144730,7.581511,7.272714,5.514576,-1.741274,-4.966486,-2.903338],[-3.641421,8.343456,-2.267616,-3.205954,-7.131417,6.226918,3.509470,-8.095539,-8.898165,9.569088,8.950739,1.072109,4.584124,6.335749]],[[-9.238964,-5.540455,9.952563,4.721508,7.847923,4.250078,-5.471647,-2.376611,1.083287,-0.016000,7.384886,2.083273,-7.759400,5.877314],[-3.858361,-8.537762,-9.269451,9.954492,-2.017224,-6.692188,7.014203,8.643492,-5.044959,6.906932,-7.891697,7.983481,-3.743693,-9.076978],[6.929382,-6.828272,-2.001879,-1.228634,6.951380,9.137640,1.662787,5.099317,7.383468,-3.710696,2.552416,3.238858,-7.687860,6.312342],[-8.889064,4.571021,1.499685,6.403246,-2.990641,9.787637,-8.440532,-7.641876,-9.365751,-8.115811,-2.998050,4.041927,-3.974564,-4.794201],[0.094554,1.881296,2.652604,7.864285,-6.905863,4.500863,-4.029942,6.638842,4.607215,-5.828664,4.785939,4.383696,-3.744936,8.855470],[4.427278,3.053105,4.910032,-2.408560,6.815851,-4.102197,5.923630,9.830952,-2.703635,-8.818531,-7.443113,0.269942,0.346461,6.704145],[6.079094,-8.687755,-1.726976,3.316403,2.161214,0.617522,7.800862,-2.608401,3.356857,-3.185623,-7.782880,2.506633,-1.852028,1.530285]],[[4.062301,8.377094,3.025905,6.729347,9.040030,-2.331638,2.467378,3.525148,5.557684,5.407819,5.271646,-7.310713,-8.092078,-9.371737],[-3.981016,-2.495632,6.879708,-1.873303,7.509659,-1.355104,-7.271224,1.875295,-9.563243,-9.243953,6.782020,-5.205958,3.558633,-0.110026],[-8.399991,-5.155858,-1.832808,-1.024776,-1.089437,5.600109,2.434822,-5.828211,-5.693094,4.238178,8.386686,-1.795668,7.518698,4.166611],[2.143498,-8.285563,5.822855,-2.796477,0.400815,2.236761,5.716367,1.938449,-3.525101,-9.010247,-4.966351,-1.580087,2.844358,-6.844547],[6.128242,9.388544,4.972053,3.898246,7.212065,4.770276,-8.101825,-0.121811,5.623635,-8.014208,-3.171980,-0.523943,-9.669982,-3.229939],[7.369520,-5.945297,-1.170759,0.522919,9.520335,-0.294256,-6.271789,1.484731,-8.251231,-6.467960,-5.057129,-3.023563,2.750012,9.395759],[5.124181,6.563740,-9.503510,5.171485,0.963276,-7.853760,6.945861,6.253472,-6.420910,0.068753,0.954860,-7.963566,-1.473528,-6.917670]],[[7.045573,-7.492799,3.936944,8.821304,8.164161,-0.975770,8.288558,-9.954510,-1.557139,-2.491092,-9.516993,6.599993,5.810085,1.618833],[-1.383187,3.256599,9.400622,-3.498312,3.416086,-2.388731,9.477196,-5.816730,-6.025634,3.692664,-4.702250,7.919416,1.380115,-7.601377],[6.403778,8.908822,8.838573,9.696640,-7.790005,3.159354,-6.019815,-5.278527,5.086163,-6.453991,2.988024,-9.736314,-8.758688,2.853029],[-6.512955,-6.191684,9.594577,-3.573169,5.059063,-2.983328,7.071845,3.963865,9.410780,9.692130,-7.098514,-0.294392,-6.493266,-5.577682],[9.920579,-5.471139,2.166616,2.366108,-9.552069,-0.267564,0.686579,2.895571,-4.900394,-8.097766,5.841788,-7.276261,-8.130713,0.310787],[2.763849,1.279791,0.371243,2.467460,-3.078228,-2.432693,-7.197326,-2.447817,9.255224,-4.621866,1.271484,9.593674,6.454111,-1.452190],[2.106774,-3.691419,2.013861,1.083477,7.624535,-3.316258,2.075703,8.510990,0.786649,3.335824,4.576120,-1.595809,1.232918,8.871894]],[[-8.927426,-3.462943,-1.214849,-5.995301,-3.594234,-6.117644,-9.835150,5.255036,5.283583,1.194870,4.809820,8.110949,3.959143,2.998420],[-4.741186,9.234961,-3.787888,-2.357729,-4.516724,6.395515,-9.196271,-1.228809,-9.370646,-3.986752,-5.080693,-9.147323,-4.231798,5.720264],[1.500636,-3.010321,3.432767,-4.938430,9.731552,-9.533103,-2.911523,-0.395149,-8.915091,1.455006,0.737474,-1.662212,-6.968219,6.232128],[7.001740,-9.549688,7.857331,-5.303309,-6.731912,-4.583124,5.976172,6.153287,-6.004688,-4.958482,-6.327945,5.338269,8.794510,-7.339942],[-1.895545,-6.961644,-7.631378,4.449658,-5.306016,-4.599484,-8.239446,-3.853148,-0.831589,1.643759,-8.215709,0.748959,-9.667216,-6.123519],[-6.765659,7.777669,-3.708124,-0.585930,-8.718466,-6.778572,8.639634,3.770367,2.139075,4.991485,2.742375,1.260599,-1.309914,-5.248674],[4.869804,-0.937540,4.021771,8.937184,-5.371486,-9.498796,8.493445,0.433856,-9.086961,-8.613166,-6.894717,8.886412,6.113459,1.377941]],[[8.598565,-6.205609,-2.019908,-5.250171,-4.298108,8.559029,-7.955730,1.276272,-5.845926,-0.705534,0.066835,0.288334,1.279302,7.360193],[2.571105,-7.387946,-0.445143,5.902101,-8.716697,4.625323,0.167441,8.569603,-0.856830,1.761108,9.530886,4.355091,8.186931,-2.115387],[4.382413,0.714829,6.324478,7.528230,-1.760730,-3.484440,1.996820,2.483855,1.055505,-0.400136,0.340001,-2.335150,9.442870,8.578203],[-6.692916,0.615767,5.623057,-6.113382,0.381693,-7.638796,3.455109,-8.717902,-9.959109,6.746407,-4.292601,-0.652368,-3.886961,-3.968958],[-8.337943,-5.330166,3.764252,8.700974,-1.437947,1.915857,9.616944,1.661451,1.641127,1.448744,3.467715,9.862319,-4.716136,2.395169],[-2.106348,5.658281,3.916389,-7.376503,6.718059,5.232290,3.689457,0.821854,-9.408578,1.328099,-2.548154,-9.428290,-7.104690,0.338382],[5.815947,2.112253,-1.297348,-7.050064,-2.389241,2.596784,-8.638980,6.929576,8.411171,9.938801,7.008184,6.446438,5.611362,8.409341]],[[5.499093,2.494756,1.373405,9.183386,5.784405,6.540422,-6.180848,1.330170,5.970093,-6.434852,-0.986558,-8.522696,3.389766,3.070994],[0.129690,-6.528791,-8.774406,5.303668,-5.971081,4.899036,8.488693,2.555436,5.917566,-8.237102,4.565255,-9.044827,-8.445543,1.018634],[-9.587137,5.435912,1.878700,2.607248,9.177538,2.115042,9.312561,0.101426,1.226057,-7.477475,4.544762,6.613195,1.800928,-8.542399],[-9.504937,8.525211,8.167318,3.662470,-5.184843,-1.847025,5.548655,2.159887,-4.009866,7.986144,9.014200,7.953796,5.995401,6.595023],[-3.137069,-9.694679,9.285286,7.233773,-6.842997,6.619731,2.284298,-4.008058,7.941548,3.770467,-5.677071,8.894818,-0.666875,8.586753],[4.258195,7.806481,-7.076284,6.044703,2.383457,-4.293757,6.250231,2.308084,2.399154,1.848148,7.692133,6.403146,-5.945930,-6.615360],[8.040253,-7.838610,-3.440938,-7.402036,3.920449,7.045766,-1.812317,9.248923,0.107105,0.324254,-7.085752,-4.936371,7.246202,-4.999461]],[[-5.638589,2.112438,-6.458775,0.222253,9.131897,1.506277,5.348578,5.222050,8.582223,9.764775,7.712213,4.730143,4.362089,-9.243602],[9.168499,-6.613860,7.236092,7.671527,9.532102,-0.175697,-4.856878,-3.794783,-4.629182,-5.964941,-7.036905,2.317501,-5.536930,3.875576],[-1.001121,-8.422113,-7.346768,3.594125,-9.857082,0.260947,7.525673,-2.936857,-6.949821,8.182741,6.721969,-4.797853,7.354079,5.322185],[-8.248010,-4.849584,-3.988783,9.162297,9.862206,-1.995840,6.645506,-0.191678,-1.860696,9.044258,9.422045,6.573912,-1.471235,-3.105319],[5.684492,2.271568,-7.807123,-7.387210,-4.851799,-4.034398,3.527448,-9.246104,-7.222522,0.965249,6.472369,7.595633,-5.104064,9.820486],[-9.340508,-3.045344,-2.460331,-1.542395,1.016892,8.783844,-1.083568,-8.938560,1.827903,-8.327508,4.823162,-9.388648,-0.322686,4.707259],[-6.168991,4.524787,-7.340841,3.119586,1.866221,8.579803,-0.965255,1.261966,-1.827730,-5.827099,-1.794682,-0.711729,8.576363,-7.867096]],[[-4.396189,-4.201649,5.040456,-5.008354,3.737222,-9.142055,6.292843,-6.142207,-4.394844,-6.289954,4.231680,-8.326923,5.308717,1.297423],[9.408588,0.914911,3.140721,7.575243,1.155490,-2.914168,1.626622,-3.577822,-6.146312,-1.850918,-3.095470,-6.094061,-4.499552,6.233213],[1.492761,-2.898504,-6.059051,-0.772633,0.080942,-8.636448,1.664819,3.259118,1.774026,2.519663,-0.964568,2.126823,-0.071226,-8.845549],[-2.710294,0.703764,-4.422451,7.963443,1.948462,-7.796016,1.270474,9.808024,6.700275,0.137021,-9.397952,3.148305,-0.548684,1.932587],[-6.757769,6.099882,5.228217,-5.533626,-1.286366,1.839233,2.227039,-9.141200,-4.012404,-3.999044,7.833874,2.789537,-9.023711,-3.850607],[2.154461,-3.884754,-7.651920,-8.702575,-0.802138,6.984452,-2.079383,-8.127360,3.487181,-0.687005,-3.735791,3.326694,-0.912572,-3.763595],[2.237750,-5.703975,-9.714723,-1.628742,-5.880419,1.345621,5.414497,-2.142200,5.300739,-4.063003,1.999112,-1.626647,6.943569,9.080881]]], dtype = "float32")#candidate|1914|(12, 7, 14)|const|float32
bop_1915 = relay.maximum(call_1891.astype('uint8'), relay.reshape(const_1914.astype('uint8'), relay.shape_of(call_1891))) # shape=(12, 7, 14)
bop_1918 = relay.maximum(call_1892.astype('uint8'), relay.reshape(const_1914.astype('uint8'), relay.shape_of(call_1892))) # shape=(12, 7, 14)
output = relay.Tuple([call_1909,bop_1915,])
output2 = relay.Tuple([call_1910,bop_1918,])
func_1925 = relay.Function([], output)
mod['func_1925'] = func_1925
mod = relay.transform.InferType()(mod)
mutated_mod['func_1925'] = func_1925
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1925_call = mutated_mod.get_global_var('func_1925')
call_1926 = func_1925_call()
output = call_1926
func_1927 = relay.Function([], output)
mutated_mod['func_1927'] = func_1927
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1846_call = mod.get_global_var('func_1846')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_1930 = relay.TupleGetItem(func_1846_call(), 0)
call_1931 = relay.TupleGetItem(func_1848_call(), 0)
uop_1934 = relay.log2(call_1930.astype('float64')) # shape=(5, 11, 4)
uop_1936 = relay.log2(call_1931.astype('float64')) # shape=(5, 11, 4)
output = uop_1934
output2 = uop_1936
func_1955 = relay.Function([], output)
mod['func_1955'] = func_1955
mod = relay.transform.InferType()(mod)
output = func_1955()
func_1956 = relay.Function([], output)
mutated_mod['func_1956'] = func_1956
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1344_call = mod.get_global_var('func_1344')
func_1346_call = mutated_mod.get_global_var('func_1346')
call_2078 = relay.TupleGetItem(func_1344_call(), 0)
call_2079 = relay.TupleGetItem(func_1346_call(), 0)
output = relay.Tuple([call_2078,])
output2 = relay.Tuple([call_2079,])
func_2087 = relay.Function([], output)
mod['func_2087'] = func_2087
mod = relay.transform.InferType()(mod)
mutated_mod['func_2087'] = func_2087
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2087_call = mutated_mod.get_global_var('func_2087')
call_2088 = func_2087_call()
output = call_2088
func_2089 = relay.Function([], output)
mutated_mod['func_2089'] = func_2089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1719_call = mod.get_global_var('func_1719')
func_1720_call = mutated_mod.get_global_var('func_1720')
call_2157 = relay.TupleGetItem(func_1719_call(), 1)
call_2158 = relay.TupleGetItem(func_1720_call(), 1)
func_1001_call = mod.get_global_var('func_1001')
func_1005_call = mutated_mod.get_global_var('func_1005')
const_2173 = relay.const([2.249069,-2.193539,-0.421560,1.916813,-6.487741,-2.433941,9.957824,-8.107977,-3.816140,-0.628260,7.853512,2.787823,7.682015,-2.330231,-1.856098,8.940009,8.875636,-8.202735,-3.437259,-6.923453,-1.827075,8.168882,-9.371544,-3.452167,5.074082,-1.567873,-9.931084,-6.869056,8.937694,8.781173,-0.895602,0.071070,-5.281378,-0.552130,6.752421,-3.563548,6.872505,2.359447,9.000122,-9.615677,-7.609950,3.008892,7.929517,-8.348963,-0.790259,-3.562881,-4.646535,5.520502,4.869666,-9.528403,-8.929301,-9.161928,-5.879089,2.200317,8.886338,0.449027,8.382898,6.586417,-5.946449,0.029340,9.093709,2.370119,7.241120,-4.180836,-3.101612,-4.270770,5.601794,-2.457506,-8.496835,-4.766192,-9.843025,-6.389960,-6.048919,-0.516180,8.694290,-5.336631,0.098519,7.430308,-8.971588,8.372674,-2.518606,6.766748,-4.807754,1.883772,2.989686,-8.368074,3.432488,8.270380,-6.038817,-4.500371,2.268503,-8.075990,0.267558,-2.486949,-2.618221,-1.347068,1.701013,-4.668018,-6.787035,-2.203447,7.222920,7.160747,7.463212,9.852926,-7.979024,-1.071383,-1.752419,-1.723161,-4.082281,2.828226,-9.942096,5.051367,1.596003,7.478682,2.965896,6.894232,-7.777174,-0.278339,-7.689623,-6.405593,0.843601,-0.570742,9.589052,2.977410,9.158925,-0.636561,8.336224,8.070018,-0.305486,-5.642309,8.490313,-9.645267,-8.248333,6.584333,-5.135977,1.608044,-3.950386,3.509962,-1.747641,8.715863,1.135330,4.601321,4.247686,0.792552,1.094108,-2.305967,-2.522618,-9.517945,4.292290,1.968262,2.771579,7.775334,-3.615775,-4.758968,-5.346490,4.946621,9.761553,-4.877117,3.563893,-8.378443,2.340657,0.658716,-9.944300,-6.688462,-3.265833,1.016640,-7.172640,9.640312,-1.310797,2.634998,-4.980412,-5.767353,7.050916,-9.247973,2.672676,9.083184,0.738352,-7.724513,-0.990715,8.108262,-8.044853,7.027070,-4.231442,7.612491,-4.773464,2.233052,7.091492,-2.163627,-9.321616,-0.184801,-0.099084,-3.591734,-7.420008,2.520080,4.374634,7.945580,5.999546,-6.502096,-0.691656,-9.057718,-8.617246,7.012405,-6.054876,-9.512132,-8.793006,-6.131630,-4.354348,1.083648,6.789043,7.458972,8.574001,-9.217497,2.688851,-3.555948,-7.047416,-7.550355,-0.795649,5.200347,-0.836552,8.064048,-9.373744,6.958237,-2.665592,8.371941,5.052422,-1.652408,-5.498875,2.931902,7.465748,1.274094,7.759819,-9.825796,6.680705,-2.659631,7.265957,-6.240127,4.745994,-2.034586,-0.183932,1.131814,0.890760,3.506690,-9.747641,6.750614,-5.136671,5.991541,9.314837,-7.839027,2.113413,-2.788048,-0.227558,-3.556122,-7.481455,-2.658443,4.067388,-0.402711,6.060765,-4.595512,-9.651764,-9.009503,-9.323090,-3.632999,7.087905,-9.173247,9.470262,-5.630584,2.722015,9.674221,0.467621,4.948046,4.815746,3.793530,2.486866,-8.903499,-8.598800,-8.502834,3.706477,-4.238268,0.042762,9.813422,7.784194,5.205139,4.293636,-7.872614,-4.222539,9.106941,0.935458,-5.894903,-4.572157,-9.635482,2.831814,4.779159,-6.351085,-3.177340,-9.920652,-0.786244,8.758342,-2.250019,3.362746,6.125598,-3.936435,6.750674,-2.816967,-4.886163,9.532918,5.989024,-8.642451,1.214972,-2.332962,-2.385867,0.188676,-3.647111,-7.544061,0.497529,3.073196,6.407841,9.638440,0.460816,5.245315,-3.792955,-8.657135,0.386091,-6.490687,3.814615,-2.164198,9.969833,4.756666,-0.267865,9.560322,0.523097,8.656610,-4.108546,3.646597,-4.584254,-3.124107,9.474258,-8.383062,2.743896,1.583497,4.354735,-7.426317,-7.281536,-1.265064,-3.275830,-2.704763,-2.799270,-5.921740,3.388232,-6.774606,-4.206378,-0.808921,9.274385,5.325657,-9.771610,-8.126679,-2.837272,-3.675602,-7.369378,-7.678806,-0.527897,-5.352163,-2.688746,-5.599785,-7.954080,4.587033,2.702987,1.502582,-8.275350,1.159120,8.988388,-2.254263,-3.476943,-7.801398,4.340448,7.228830,-0.520060,-2.775157,6.421644,-1.646458,5.739797,-1.773787,8.682433,3.835688,-6.184052,-0.733942,-8.364607,-4.986717,-1.117444,6.049669,9.340244,8.630038,-0.286760,-1.226348,-3.210221,-1.066934,-3.672134,-1.626132,-0.713049,9.395624,-6.825451,-7.218857,-7.237947,-3.483602,-5.006165,-5.381479,-4.877178,1.467114,6.287926,-2.712262,-3.110959,2.193497,-4.906600,-4.345861,0.465656,4.069784,-4.928100,9.132388,-9.376470,9.822206,7.713448,-2.058956,6.738671,1.073150,9.996261,4.528355,-4.323869,-2.913845,-3.940865,9.643112,-1.912801,-5.469336,-4.771620,1.602436,1.985220,1.639563,-8.901615,-3.504320,1.221560,-8.052711,-8.828618,-6.910254,-1.559636,0.218897,-0.817265,1.532797,8.158979,2.410137,9.647600,1.896147,9.123521,3.851308,-2.543107,0.206430,5.612582,3.168132,0.697171,-5.137118,-7.400245,4.773030,-4.868576,-3.698581,-3.228291,-4.977576,-2.085946,-3.066323,-0.133776,-0.895533,3.379926,1.587642,8.060027,-5.335318,-1.036053,7.770171,-1.937693,0.544652,2.618935,0.185588,1.878738,5.417354,9.584955,8.135476,4.719021,-8.700588,-5.427948,-6.370014,-4.772516,-6.445453,0.362412,-3.820537,-8.883884,0.101528,5.280185,8.130281,-4.495369,-4.469205,-7.671532,7.010578,1.216153,6.339672,7.726015,-0.254740,-6.256759,6.317801,-6.853259,-5.333626,6.348290,-1.380577,-8.905165,-5.663723,-2.778926,-6.505859,-6.368467,-3.145451,7.660010,4.890460,2.127352,5.173979,5.943198,-5.575923,-4.706372,-4.675642,-4.784390,-5.081461,4.736062,1.738719,3.693445,-7.412290,8.700496,-0.555939,-4.269331,-2.498154,9.359264,-4.264385,-6.092531,-6.308702,7.933840,-6.174882,0.700248,-4.858385,8.593436,-9.916924,0.685102,2.266460,6.915613,0.250242,6.492030,-0.232206,5.665428,2.722642,5.175877,-4.146582,2.099696,-3.544316,7.772055,8.132687,-0.018505,-0.603492,-2.844926,-3.868778,6.718323,-2.481269,8.727012,1.205387,3.197941,-9.183239,-0.855709,6.209887,-7.514873,-3.575256,-8.508157,-7.542836,6.441728,-8.656302,-5.534697,4.709112,-2.933425,1.239772,-9.813783,6.351676,7.422435,-8.873242,-4.330403,2.326554,7.258435,5.468868,3.303604,-5.666632,-1.924006,9.362861,-0.117485,-0.565114,-3.666132,-3.294878,-0.153915,-8.274658,-5.179539,8.039030,-2.013062,7.148337,-5.341074,0.853768,-9.824223,-4.887094,-2.516206,-6.996410,-3.986642,6.795269,-6.807300,-4.541098,7.419346,-3.714991,5.040722,9.161624,4.827341,-5.466766,4.214638,7.391439,7.479536,-3.456164,2.501996,-9.730560,2.044814,-6.501023,-1.826595,-0.958578,9.240411,6.428438,-9.926643,-1.156535,2.471535,4.604616,-2.655032,-5.516123,-5.604395,3.500419,7.060177,8.613488,-9.519829,-5.352492,-7.374324,-9.376145,-9.219181,7.294289,-0.838169,-0.540304,-6.908157,-3.669482,-1.967800,-1.994112,5.780088,6.345854,-1.821356,8.785315,-7.252589,0.755787,-0.117085,3.961856,0.187332,8.179499,-0.960308,0.901481,9.125713,-5.813716,-3.322934,-9.918285,-8.298155,3.045071,0.216525,0.929616,-4.238144,-5.036031,7.786909,3.674780,-8.876751,-9.102986,-2.686152,1.370880,-6.620640,-2.564377,9.519754,-7.862736,-4.319452,-9.011521,3.293686,6.175210,-2.011248,-6.295104,3.749777,-9.121651,6.956201,4.517145,-7.718500,2.039186,-0.305273,4.397897,0.216763,8.318619,0.345547,2.604617,-4.101843,3.611941,-6.323022,-9.449294,9.807687,-7.911931,6.305420,8.840151,-2.908461,-9.368199,-0.296647,-6.360727,-6.217929,9.052679,2.792339,-1.765613,3.615884,-6.666967,1.594286,-2.495291,0.857505,4.366755,-9.644183,-1.534653,-6.952312,5.407823,5.529026,-9.921899,5.723172,7.026441,-4.870983,-1.001743,2.781202,3.884583,9.684694,-8.189568,-2.394136,-6.179286,-4.003688,-1.614340,1.662948,3.488214,7.806680,-8.017643,7.750174,-1.589150,3.137694,2.947149,7.805196,-9.974995,-6.775946,-2.842288,-7.241711,0.672903,8.340348,1.290041,6.660423,3.378661,-0.484884,-2.585916,-6.556168,8.956892,0.647777,-0.379929,-7.758958,-1.511231,3.118723,8.818566,9.533054,-7.639671,-9.063800,9.065389,-6.570115,1.138125,7.387889,-2.825570,-2.372912,9.645221,4.065336,-6.438047,-1.122748,-2.655238,3.115598,-6.491516,4.307961,-7.256388,-6.401924,1.853976,-9.965009,-8.273117,-8.278483,5.527549,-0.395600,2.629461,9.406927,8.464350,-7.927382,6.100728,-4.249128,-0.674344,2.322579,1.530864,-9.412115,-3.007765,2.264902,-3.851811,-7.345161,-6.706915,4.681535,-8.318116,-0.576307,-5.001140,6.815814,-1.793007,6.129147,0.516275,4.137921,3.505249,-8.627189,5.501302,-7.552892,2.294873,0.029431,2.550237,5.571110,1.310855,-6.866280,-5.202529,-1.213916,1.257526,4.170125,-8.047958,7.388595,8.657033,6.124350,-9.457506,-8.723658,-4.577314,5.939017,-0.108808,5.032204,-1.783277,-5.498284,-9.309147,-3.617284,-5.422646,-2.920999,-4.921239,-8.108405,8.613294,-0.840395,0.413138,-2.446040,7.239439,-8.793643,-9.467084,2.944619,5.224693,-7.997184,-0.840292,6.134371,-8.797328,7.188073,5.038954,-3.839788,-7.217615,-2.298041,-8.358652,5.429180,5.714619,9.719922,-9.771662,-5.202827,-9.285133,9.497970,3.547396,-8.363115,-5.519469,9.815910,8.140865,3.926386,-0.908947,-5.613689,-7.322326,-2.384544,8.519337,2.697882,8.912022,6.934658,-9.714890,-5.094194,6.072553,-6.809868,8.100235,5.336390,8.827025,-9.347800,3.211418,-5.329131,-4.206550,9.394302,2.446517,5.279761,-3.068450,-0.660520,9.835216,7.438747,2.186204,4.894548,8.441760,-2.426190,1.065384,-2.614377,1.800524,-4.200553,-0.202767,9.222782,-0.124797,-5.978059,9.749160,-8.793823,6.675978,6.788510,4.397994,5.115465,3.308157,8.133815,-3.042753,2.310480,2.521572,-0.212443,5.609234,3.267080,-6.858846,3.929046,-6.054080,9.654696,5.717327,9.886072,5.276408,1.001670,-2.055011,4.207116,-3.256762,-5.264876,-7.290707,3.632809,-0.365237,2.775941,-3.945072,-1.763929,-1.603308,1.940235,-8.943193,-6.871594,4.475902,-4.363048,2.502570,1.016496,7.355965,2.728239,-0.563009,0.853328,4.965750,4.364878,8.630191,-8.600893,5.798123,5.613595,-7.202894,7.158696,8.361983,2.514690,8.834647,8.199637,-0.702057,-0.443826,5.115873,5.926346,2.939135,0.306842,-9.029160,-0.641747,9.014140,2.235208,-6.003076,3.207122,0.466983,-3.731395,2.245329,0.939158,-2.002857,-9.653842,6.101154,-2.200297,8.151459,-1.922585,9.190838,4.847802,-5.881332,0.892146,-1.014037,4.558905,2.866304,-8.000577,1.890389,7.664484,-7.781281,9.915147,0.966091,-7.504910,8.861658,5.902788,3.671745,0.229260,0.701909,-3.430843,-5.763447,1.151670,2.481589,-1.917077,9.936193,-0.457204,-7.179939,-2.059196,1.892079,-2.767246,5.589901,-8.805010,-6.785667,-9.755071,-0.712640,9.464553,-8.867559,-8.267665,0.854311,-3.471343,-8.494166,-9.012167,3.509457,4.382772,2.143016,7.595165,1.985553,8.276358,-5.269215,4.138922,3.142895,0.742434,-7.977685,1.157771,-3.811096,-4.700707,9.755891,0.285822,1.276572,3.792474,-5.300176,0.903964,-3.397739,-6.569338,4.040475,3.608504,-9.261841,-5.118051,8.692679,-8.934813,-8.848044,-8.937641,3.002718,-0.503348,-3.586597,7.805252,-0.167023,-2.605140,-7.111193,9.579564,3.890079,-9.960678,2.313115,-6.144001,-2.579003,4.975585,5.622546,-4.493515,8.130248,-8.792832,9.650623,1.255071,-0.770572,-2.497686,-6.120506,-9.556458,8.270382,1.628417,-3.997814,7.047083,0.036563,2.830853,-8.879025,3.109699,-7.673308,-5.591702,-0.128820,2.511484,2.391392,0.909053,-3.625980,1.929117,-7.600979,-9.491325,-0.489381,7.567798,-4.092011,2.613004,5.970623,2.174607,-6.026514,7.606667,8.011255,7.277266,-5.151942,-3.178749,4.652682,-0.081868,-4.492832,-0.823534,-7.979375,-2.839763,-9.121367,-4.144546,4.394886,8.064427,1.151348,-3.944472,1.506463,1.167174,-9.258429,-7.980816,-6.721230,9.445086,-6.233493,5.488837,3.676555,9.160578,1.789655,1.012059,0.722913,-1.282001,2.870649,4.331501,3.654339,1.906634,-9.423214,9.854410,-4.053159,-8.639789,-5.858872,-5.514790,4.980354,1.501427,2.540042,0.878568,2.755168,2.432564,-2.243200,7.666226,7.191642,2.205079,8.465737,-9.481478,1.949112,-2.366421,8.195917,-3.375637,-4.870726,9.506310,-6.709765,2.450262,8.128503,3.834298,8.489060,4.771167,3.777126,8.139946,3.673503,-4.937749,-1.487912,-9.297453,4.106975,-3.134281,-8.832684,7.118764,1.055706,-3.138559,0.846332,-5.746110,-1.201461,-2.814115,7.285241,-6.894473,5.146367,8.186575,4.041882,7.015902,-8.370098,4.202764,-0.175402,-2.675590,7.732961,-6.609121,-2.808620,9.919907,-3.031409,-0.394224,8.085950,-0.381843,0.245474,-5.749415,2.157753,-3.218910,-4.595970,-1.064114,-2.488350,-0.740492,2.898333,0.971982,9.903882,-5.590295,-3.207097,5.781701,-2.554639,-4.327389,-7.384980,-2.534108,5.370725,0.296655,-3.186614,-0.420764,-6.572539,-8.703178,0.480074,7.126498,3.383137,-5.594527,-8.152845,8.580551,5.649837,4.823328,7.130183,1.665907,-0.910191,-3.151272,-3.723896,4.562719,8.072674,-6.441638,8.137970,8.539553,8.510362,-6.178952,-5.844064,-1.565796,-1.427124,2.663733,-3.738797,-0.643149,2.475796,5.562464,7.351065,8.875165,0.882231,4.743556,6.279479,4.887518,-1.349572,7.239581,5.130839,-5.932077,0.312123,1.257007,-0.144964,-6.511302,-4.614808,1.169933,-8.221757,-8.147174,-7.406898,9.073713,6.324153,-0.839859,-4.371219,-8.826091,-0.454209,9.062451,-3.045472,5.507957,-4.430298,-3.037826,6.234119,-0.389814,-7.528161,8.972020,-0.987354,4.047357,4.071136,4.495769,9.611819,-6.825729,-8.925268,2.057682,-4.987050,8.626676,-7.219137,-3.095508,7.319540,1.603037,2.149742,-9.973569,3.176253,7.558499,-6.169609,7.987715,-4.782454,2.648457,7.239733,3.006318,7.926673,3.075884,7.579699,5.288388,-5.347943,-5.737417,-9.838079,-9.725979,-7.022666,-2.721617,-4.661033,-0.986993,9.090696,-4.161974,-9.083142,2.600546,-8.377087,6.463901,-3.703606,3.184820,-7.006199,-3.625719,-5.076375,-1.769424,9.767940,6.756870,-2.724268,-4.913554,8.865088,8.265896,6.128162,0.533521,1.749966,9.944270,-2.995713,-5.978910,-0.227732,8.801829,4.325988,-4.169212,-5.248326,4.687929,7.624475,8.235631,-7.273323,1.305864,0.214087,3.541740,8.543567,-3.810045,8.054804,-4.684595,7.763152,7.790436,-7.152039,5.522401,7.772252,8.490598,5.047582,-2.568397,1.324627,7.057767,-5.366662,0.473345,0.731803,9.768111,0.604061,-6.327244,7.320500,9.634257,4.515235,2.995372,0.186135,-1.641469,9.478138,-4.558903,-7.604124,1.254437,2.413949,-9.382240,-0.502113,1.030240,-2.746214,-5.057390,5.351003,5.705959,7.709018,-1.589726,1.855810,8.189323,1.785758,-8.937077,3.775541,-4.286193,-1.501093,3.650115,5.107196,-7.363107,-2.944794,3.469310,9.165019,6.222247,8.268862,9.416558,-4.661793,9.092892,9.158354,8.339270,2.223983,9.061947,-8.038514,-0.177841,0.416533,3.373837,-8.876238,-8.904598,6.482281,-4.634312,3.343215,-1.439178,-1.725058,9.347795,9.121486,-3.939275,-1.446858,-6.433642,-4.247087,-9.087496,-0.713769,1.241096,7.517121,-9.186407,0.775642,2.312831,-2.042000,-3.551185,-7.567741,-4.769833,-2.789644,-8.913119,-0.785621,-4.093525,-7.973781,0.813600,-2.330677,8.020281,-2.118371,1.546192,-8.617964,-7.510327,-9.748173,4.477557,-9.856220,-5.981908,-7.108202,6.480086,0.695749,0.580001,8.491641,-8.704993,8.256218,7.612518,5.833612,-6.697779,0.375368,4.512979,0.331898,-4.044033,-3.793214,3.638909,-8.557443,-1.259268,-2.419366,4.195953,-3.287441,9.474989,0.684076,6.458777,4.497956,-4.032503,-3.737920,-9.084313,-5.334880,0.738450,4.307145,2.035067,1.398982,-3.929987,0.175911,2.963782,9.321704,6.927960,4.665776,-5.962204,-3.678660,-1.061096,-2.415294,1.876550,1.894885,1.404005,2.511683,-5.600407,-5.183818,-5.968254,-5.892506,6.741146,-4.786903,-8.091998,5.446029,8.528970,8.156885,-4.843638,-8.511407,-4.371166,-2.523293,2.241542,-6.282673,4.871289,-1.664817,-6.668693,8.241292,-5.356605,8.132445,-8.952881,7.747689,-6.321232,3.225060,-0.237296,-9.891309,9.509518,6.703675,-7.384285,0.253155,-7.482354,7.036459,-8.977406,7.867118,0.112703,-7.108308,6.395684,7.814252,-4.084508,9.101377,-0.181422,-6.720296,-7.458231,-9.833817,1.425607,-2.343359,8.216584,1.860738,5.213000,4.314456,5.664899,-7.799303,1.076872,-9.717714,-1.453469,7.680807,-8.826908,-5.607960,3.370378,5.889187,-8.228611,-7.772155,-6.046363,-9.888480,-8.851803,-0.941514,6.987526,2.228768,-6.668499,-8.232913,4.277832,9.137546,0.189145,-7.344970,8.133062,-0.975549,-4.036982,8.531817,-0.153853,-8.757740,5.487012,-0.710785,2.321038,-8.463726,7.325862,-5.229484,-8.302648,-0.421633,3.325529,-5.570550,6.844348,4.848056,5.471051,-4.668674,-1.811957,3.027211,9.855438,-5.427125,2.206064,-7.375829,8.622430,4.080871,-9.017733,-1.433865,-2.970047,-2.954694,1.346097,0.018284,1.150623,-4.090681,-7.357609,0.898751,2.187798,-3.786541,-2.194873,1.574876,2.082049,5.256138,8.659853,-7.448702,-1.801446,2.448342,-2.735719,5.185857,-2.501360,8.151547,6.561866,-1.052956,-3.206777,5.489259,7.485736,-3.363153,1.279747,-3.837591,4.198636,-4.479138,-7.204510,2.017244,7.301352,-1.061698,-7.219410,-6.311211,-0.807250,-2.282263,-3.813733,-5.501622,3.220168,-6.934930,-6.414420,8.952461,5.358801,-6.514669,5.743859,-4.327551,-0.727941,-7.864979,-0.802080,-0.333494,9.863707,5.528916,-1.084903,3.183575,5.594050,-7.095612,-6.323634,6.079467,0.098693,9.655060,-5.504732,8.304723,-2.180248,3.592438,2.754573,-9.478837,7.111113,-8.850203,5.943963,4.643051,0.335568,-7.874165,4.765811,-5.949661,8.227387,8.107741,4.447941,-5.363539,-5.990152,3.945617,2.773232,-6.387655,2.726616,-6.358654,-1.877978,7.976764,8.169154,5.649231,-8.036771,-6.981963,-3.662889,0.401556,-6.119588,0.556425,7.217769,-6.518958,-9.022511,1.476281,2.815472,-4.570626,3.022598,-3.967480,-1.329180,9.350793,4.834655,-7.943266,3.551980,2.601645,-3.311959,-0.629485,6.269818,-1.479642,4.693943,-5.635977,-0.451507,-6.802636,-3.580054,-2.089840,9.993233,7.143866,3.151289,-6.141712,0.289232,1.590029,-8.667854,-8.640671,-8.260027,-4.261849,-1.782712,5.141077,4.896270,6.933857,-2.861547,-9.721831,9.518400,-7.178421,-6.670514,-6.602135,-9.760355,6.026757,2.966328,0.223271,-6.342764,-3.092171,-0.575754,2.691450,0.804399,3.660571,0.286020,3.268249,-4.934098,9.528046,-3.086547,-0.690613,9.923766,-4.830426,1.507146,4.737990,6.030041,4.334701,4.620027,9.052204,2.519716,-9.101161,0.475844,8.008334,0.058305,-2.345937,-1.015613,-5.325040,-9.773546,9.027442,-3.543950,7.436228,-6.689670,9.410232,-2.878375,-9.232402,-5.083402,-2.845467,4.726137,4.434032,-8.282047,-8.295037,-3.184346,7.020095,8.552155,8.036161,6.585957,4.405677,7.606765,1.257086,-6.136733,5.730918,-0.253155,-2.420305,4.615735,-9.588795,3.375350,3.024305,6.899891,-5.690737,9.278846,4.919399,-8.936338,-2.443572,4.890484,3.594884,4.834575,-2.139012,-0.493005,3.345553,-5.709316,-9.940153,7.846646,-5.183811,-1.568056,7.305274,-2.132672,-0.296142,-8.540677,-1.758274,-2.592196,0.589692,-1.217527,3.471967,-7.793259,-0.316664,-9.301146,-2.298658,-6.723232,-4.313716,6.232008,-3.556398,-5.086728,-6.165821,7.328307,4.502591,5.100981,-4.695853,-7.322801,-7.353440,-7.141200,-4.098392,7.000565,-2.879614,6.584876,-0.443350,4.914581,-4.914678,2.559745,-9.891710,3.318065,-4.756957,-2.651417,-2.685041,-0.920597,8.765475,2.471310,9.998511,-4.369236,1.214490,3.966216,-1.771873,-0.948516,-0.674664,6.833778,0.720721,-1.283438,5.212687,-6.495609,-6.379440,9.087504,1.768975,7.429725,7.353249,5.398149,2.938999,0.169060,5.658535,-1.410824,1.139392,-8.266440,-2.023902,2.636633,2.775734,1.719280,-3.200159,5.452498,9.927630,0.252257,-0.280681,4.979737,0.002637,5.944493,7.741351,-4.477928,8.013086,8.042156,-8.716137,-6.966231,-9.711210,2.618088,-0.518300,-3.644239,2.268328,-8.068734,-9.874856,0.581017,-7.113140,-6.998538,-6.321829,0.494186,9.989969,8.620170,4.812995,1.005812,5.900633,-6.285692,1.223344,9.200599,-4.027090,-1.589343,-4.680885,-3.301236,-5.438375,-5.591574,-4.828262,3.802049,-0.688912,1.279618,-8.506627,9.982868,3.652043,6.088128,-2.201157,5.181487,-7.569758,-8.222483,6.274311,-3.651561,8.783132,-0.031285,-9.329442,-0.400190,-7.484501,-3.251606,-2.340378,-2.944421,1.754480,6.289562,-0.295133,5.764395,-1.944815,1.962650,-9.732421,-4.945057,-1.587219,6.292279,-8.446475,7.373905,0.996540,6.834356,0.505245,1.117246,0.574408,8.097512,6.317459,-5.851752,-0.085847,9.562802,6.470844,-5.628800,-5.522474,-8.353070,1.875284,6.618076,3.014085,2.848565,-4.508490,-7.627739,9.881418,-4.115853,-0.818411,-4.572581,-0.602544,4.340719,1.576234,-8.467509,-1.104982,-9.665184,-7.708092,-6.458734,-4.693705,8.526476,1.026041,-3.500989,7.584610,2.097031,-3.168682,-7.827835,-5.819757,-2.748406,2.466463,2.850150,-1.525131,-5.093991,-8.053944,-5.392801,-4.838074,6.757948,9.584736,-3.301464,-2.263258,-5.676006,9.757249,-6.164855,0.551541,-6.957173,5.399928,-0.262705,3.141171,-8.798367,2.764298,8.211656,-3.135946,9.508506,-0.253034,-0.734466,-6.787677,4.115541,1.480578,1.141421,4.928964,-5.988214,7.766650,-5.328448,2.769613,-3.884995,0.951978,-9.817660,3.125009,-8.007655,1.657894,-0.827779,8.802734,8.990054,5.523699,8.613182,-5.680870,4.529067,-1.383191,2.201064,2.613208,7.096980,9.912678,-4.587564,7.693786,-6.689027,-1.460752,-6.338954,9.965274,-2.073479,-1.755306,9.706512,7.480387,8.818640,-2.502327,5.003713,-2.293774,-8.926821,-6.505137,-8.083222,4.619079,-4.109486,-5.107339,-7.618901,1.307257,-5.279702,-3.161752,-1.475130,8.169389,-2.221025,-5.338706,5.790007,-0.488411,-7.628555,-7.426830,-9.094146,-2.900446,9.775958,-6.580582,-0.118620,3.772458,9.228103,-0.342024,3.833864,8.614101,0.648709,-5.754182,1.426500,-6.292121,4.175414,-1.353538,4.734890,3.292293,8.763639,-8.488125], dtype = "float32")#candidate|2173|(2145,)|const|float32
call_2172 = relay.TupleGetItem(func_1001_call(relay.reshape(const_2173.astype('float32'), [11, 13, 15]), relay.reshape(const_2173.astype('float32'), [11, 13, 15]), ), 0)
call_2174 = relay.TupleGetItem(func_1005_call(relay.reshape(const_2173.astype('float32'), [11, 13, 15]), relay.reshape(const_2173.astype('float32'), [11, 13, 15]), ), 0)
func_1824_call = mod.get_global_var('func_1824')
func_1828_call = mutated_mod.get_global_var('func_1828')
const_2185 = relay.const([1,-4,3,-2,-10,2,-7,-7,-2,10,-5,1,4,-7,9,2,2,-3,-4,4,10,-7,6,5,2,-7,-10,-6,10,9,-9,-1,7,-8,1,-4,-5,-7,7,-8,-7,8,7,2,-7,-7,1,9,-2,-10,8,-5,5,5,-3,-2,10,-8,6,-4,-2,-1,-9,-3,-7,5,7,10,1,5,-8,4,9,-7,-3,-7,-2,-8,-7,1,3,1,7,1,5,-3,3,5,1,-6,-2,1,-9,4,-1,-2,-2,-6,4,-8,5,4,-9,1,-2,6,8,-8,8,5,-9,-6,1,10,1,-4,9,6,8,2,2,2,7,9,3,5,-4,-3,-4,8,-2,2,10,-3,-3,8,3,9,1,-5,3,-4,-2,-2,1,10,2,-7,9,-3,-5,10,-1,7,-9,6,-4,-1,-9,-3,-2,-4,-6,-9,10,-9,-4,-2,10,-7,-4,10,-5,-6,-3,5,-3,-2,-1,-6,-4,8,6,1,1,-4,2,5,-5,2,-10,-3,-7,4,5,-8,6,5,8,-9,-7,-4,-7,8,9,-9,-6,-4,9,-10,-9,-3,6,9,5,3,-1,1,-7,9,9,-5,-2,8,6,-6,-6,-1,7,8,-2,-2,-9,10,-1,4,-8,-5,-9,-10,2,-1,4,-3,-6,1,-2,-10,9,9,-10,10,-1,6,1,-4,-3,1,8,8,-3,-1,-5,7,2,4,8,-8,10,-8,2,-3,-6,-2,-6,-10,3,-5,-4,-10,8,-6,9,-5,10,1,-5,6,-7,-8,3,4,-1,2,-3,2,10,10,-6,10,8,7,-6,-5,-3,7,-2,10,2,-1,-8,-8,4,6,3,-5,7,-4,-5,5,-3,2,5,-3,5,2,10,10,10,-4,-3,-3,1,3,-8,1,-1,9,6,3,-7,-7,-6,10,4,-8,3,9,-9,-9,3,8,-3,-9,10,-4,-8,-3,7,-10,-5,10,-10,-3,3,7,10,-9,-4,-5,4,-1,-8,9,-6,-8,9,-1,1,9,-6,10,-4,10,-9,2,4,-8,-8,10,5,-6,-10,-5,-1,-4,3,-2,3,4,-10,-7,-8,9,-1,-1,-10,3,4,-8,-4,-3,-6,-3,8,5,2,4,-9,9,3,6,-4,3,7,-4,-6,8,-3,-5,8,1,-3,3,8,-2,9,6,9,3,5,-6,6,4,-5,-10,-10,7,6,7,-2,-4,-9,6,2,-5,-9,-7,-3,4,-2,4,-7,-7,-9,-4,-3,3,1,-3,1,7,7,6,-6,1,-7,2,-4,-7,-3,-7,1,2,9,4,-1,9,6,-1,8,-10,5,-2,-1,5,2,-2,-9,-5,-10,-10,10,1,7,-6,-2,-1,-10,-9,2,7,-3,6,-3,-2,-10,4,-2,-3,6,5,10,8,-10,3,10,-7,10,9,-4,8,5,-3,-8,-7,8,4,-9,9,1,3,-5,6,-2,1,-8,-2,-3,-10,-1,-5,9,8,6,-9,-1,-8,-1,-2,-1,-10,1,2,7,5,10,-9,-1,-9,4,4,10,-2,10,5,6,-2,9,3,7,6,-9,-6,-1,9,-3,-3,-9,-6,-6,2,-10,10,-8,7,-10,1,-5,-2,-4,-2,-4,-1,-9,-1,2,8,8,1,-3,-1,9,-4,1,-3,-7,-1,1,5,1,-6,9,-4,3,3,6,-9,-8,-1,9,5,10,-8,-9,10,8,4,-9,-6,-6,8,-5,-8,2,-3,5,10,3,6,-10,4,2,7,8,4,2,-7,1,-1,7,7,-3,9,4,10,2,1,-1,3,-2,5,-1,3,10,-6,-10,-10,1,-9,-5,-6,-2,-8,5,-4,10,-3,2,4,9,-8,4,-2,-7,9,-7,-8,-4,-3,10,8,-9,-3,-4,-2,9,-4,7,-10,-4,-8,-4,1,1,-8,5,10,-6,4,2,-5,-5,-3,-4,9,-4,8,-1,7,-6,2,-1,-3,7,-9,3,-9,-2,1,7,-3,-4,8,-1,-7,2,-8,4,-1,1,2,-3,-10,-5,-2,-10,-5,5,10,-10,5,-8,6,4,-7,-9,-9,-1,-9,2,1,4,8,1,7,5,-7,3,-7,3,4,-4,-4,3,-1,3,-9,-2,-8,5,8,5,6,-9,7,-8,3,5,7,9,5,2,10,-2,-8,-4,-8,-2,-9,7,2,-8,-7,2,-10,-2,4,-2,-9,-5,-1,5,-9,6,-7,-3,-10,4,3,3,-9,-10,-10,-7,7,10,-2,9,-2,-7,-10,8,1,-9,-9,8], dtype = "uint16")#candidate|2185|(847,)|const|uint16
call_2184 = relay.TupleGetItem(func_1824_call(relay.reshape(const_2185.astype('uint16'), [11, 11, 7]), relay.reshape(const_2185.astype('uint16'), [11, 11, 7]), ), 0)
call_2186 = relay.TupleGetItem(func_1828_call(relay.reshape(const_2185.astype('uint16'), [11, 11, 7]), relay.reshape(const_2185.astype('uint16'), [11, 11, 7]), ), 0)
bop_2188 = relay.less_equal(call_2184.astype('bool'), relay.reshape(const_2185.astype('bool'), relay.shape_of(call_2184))) # shape=(11, 11, 7)
bop_2191 = relay.less_equal(call_2186.astype('bool'), relay.reshape(const_2185.astype('bool'), relay.shape_of(call_2186))) # shape=(11, 11, 7)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_2193 = relay.TupleGetItem(func_941_call(relay.reshape(call_2157.astype('float64'), [5, 11, 4])), 1)
call_2194 = relay.TupleGetItem(func_943_call(relay.reshape(call_2157.astype('float64'), [5, 11, 4])), 1)
output = relay.Tuple([call_2157,call_2172,const_2173,bop_2188,call_2193,])
output2 = relay.Tuple([call_2158,call_2174,const_2173,bop_2191,call_2194,])
func_2197 = relay.Function([], output)
mod['func_2197'] = func_2197
mod = relay.transform.InferType()(mod)
mutated_mod['func_2197'] = func_2197
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2197_call = mutated_mod.get_global_var('func_2197')
call_2198 = func_2197_call()
output = call_2198
func_2199 = relay.Function([], output)
mutated_mod['func_2199'] = func_2199
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_2266 = relay.TupleGetItem(func_1883_call(), 1)
call_2267 = relay.TupleGetItem(func_1885_call(), 1)
output = call_2266
output2 = call_2267
func_2294 = relay.Function([], output)
mod['func_2294'] = func_2294
mod = relay.transform.InferType()(mod)
output = func_2294()
func_2295 = relay.Function([], output)
mutated_mod['func_2295'] = func_2295
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_2308 = func_1425_call()
call_2309 = func_1425_call()
output = relay.Tuple([call_2308,])
output2 = relay.Tuple([call_2309,])
func_2310 = relay.Function([], output)
mod['func_2310'] = func_2310
mod = relay.transform.InferType()(mod)
mutated_mod['func_2310'] = func_2310
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2310_call = mutated_mod.get_global_var('func_2310')
call_2311 = func_2310_call()
output = call_2311
func_2312 = relay.Function([], output)
mutated_mod['func_2312'] = func_2312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2087_call = mod.get_global_var('func_2087')
func_2089_call = mutated_mod.get_global_var('func_2089')
call_2402 = relay.TupleGetItem(func_2087_call(), 0)
call_2403 = relay.TupleGetItem(func_2089_call(), 0)
output = relay.Tuple([call_2402,])
output2 = relay.Tuple([call_2403,])
func_2412 = relay.Function([], output)
mod['func_2412'] = func_2412
mod = relay.transform.InferType()(mod)
mutated_mod['func_2412'] = func_2412
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mutated_mod.get_global_var('func_2412')
call_2413 = func_2412_call()
output = call_2413
func_2414 = relay.Function([], output)
mutated_mod['func_2414'] = func_2414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_2598 = relay.TupleGetItem(func_684_call(), 0)
call_2599 = relay.TupleGetItem(func_686_call(), 0)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_2625 = func_480_call()
call_2626 = func_480_call()
func_2310_call = mod.get_global_var('func_2310')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_2639 = relay.TupleGetItem(func_2310_call(), 0)
call_2640 = relay.TupleGetItem(func_2312_call(), 0)
func_182_call = mod.get_global_var('func_182')
func_186_call = mutated_mod.get_global_var('func_186')
var_2643 = relay.var("var_2643", dtype = "int32", shape = ())#candidate|2643|()|var|int32
const_2644 = relay.const([-2,4,-6,9,8,3,3,-9,-4,-8,-4,-1,-9,-6,-5,2,8,5,5,-1,9,8,4,8,8,2,-5,2,7,-2,4,2,-10,-8,-10,7,5,-1,5,-8,7,4,4,-7,-5,-5,-3,-3], dtype = "int32")#candidate|2644|(48,)|const|int32
call_2642 = relay.TupleGetItem(func_182_call(relay.reshape(var_2643.astype('int32'), []), relay.reshape(const_2644.astype('int32'), [1, 6, 8]), ), 0)
call_2645 = relay.TupleGetItem(func_186_call(relay.reshape(var_2643.astype('int32'), []), relay.reshape(const_2644.astype('int32'), [1, 6, 8]), ), 0)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_2652 = relay.TupleGetItem(func_684_call(), 0)
call_2653 = relay.TupleGetItem(func_686_call(), 0)
func_1001_call = mod.get_global_var('func_1001')
func_1005_call = mutated_mod.get_global_var('func_1005')
var_2663 = relay.var("var_2663", dtype = "float32", shape = (2145,))#candidate|2663|(2145,)|var|float32
call_2662 = relay.TupleGetItem(func_1001_call(relay.reshape(var_2663.astype('float32'), [11, 13, 15]), relay.reshape(var_2663.astype('float32'), [11, 13, 15]), ), 0)
call_2664 = relay.TupleGetItem(func_1005_call(relay.reshape(var_2663.astype('float32'), [11, 13, 15]), relay.reshape(var_2663.astype('float32'), [11, 13, 15]), ), 0)
func_1824_call = mod.get_global_var('func_1824')
func_1828_call = mutated_mod.get_global_var('func_1828')
const_2675 = relay.const([10,8,2,-4,-5,-2,2,-9,4,7,-8,-5,3,1,7,-7,-7,-10,8,9,4,10,-7,-10,-4,3,7,1,9,10,-9,-6,3,7,-7,-5,-2,-9,-1,-9,6,-10,-1,3,-4,7,-9,4,-8,-1,7,-8,-10,-7,-5,-9,10,2,-2,-3,-7,2,5,7,-4,8,6,-2,4,9,-8,8,10,1,-6,-8,7,10,3,3,6,3,-1,10,6,5,-10,4,-7,-3,1,8,1,-10,-3,-6,-6,3,-3,5,6,3,-6,-7,-6,-6,10,-5,-9,-7,-7,5,1,-5,3,-2,-1,-5,4,8,2,6,-7,5,7,-2,5,2,-5,10,4,-7,9,-9,-5,2,2,-9,3,7,-8,-6,4,10,-2,9,2,-2,9,-3,-10,-2,-5,1,7,-9,7,-7,-3,2,7,3,7,-10,9,-1,-8,-1,-3,4,2,-4,-9,2,10,-7,-5,-8,-8,-1,2,5,-6,-7,-1,-1,-2,-4,8,5,9,-6,-4,9,3,-8,5,-8,-10,-1,6,5,-9,-1,6,2,7,2,-2,-5,2,-3,7,-9,8,9,4,-4,-7,-7,-2,-8,8,-2,2,7,-1,2,-4,4,-3,-6,8,-9,6,8,6,6,-6,6,8,-4,8,6,7,3,-4,6,-2,7,-10,5,10,1,2,4,3,-10,3,2,-5,-9,-8,10,-9,-8,-3,8,4,9,-9,9,-10,2,4,-5,-10,9,9,-8,8,9,6,-5,7,10,7,-7,-8,-2,2,1,-2,-2,10,9,-5,-1,6,-5,8,-8,-5,-3,3,-3,-5,-8,7,-7,-1,6,7,-7,3,-7,-7,7,-1,5,8,-8,4,-9,8,-7,4,-3,1,5,3,-5,8,-2,-4,2,7,-6,-8,2,-3,-4,-4,-8,-10,9,3,-4,7,10,7,3,2,4,4,-5,-7,-2,8,6,-10,-1,-10,-6,5,8,7,-3,-9,-8,-5,10,4,2,3,-7,-4,10,5,3,-3,1,10,-1,-3,4,4,9,-7,7,9,-4,6,1,1,1,-2,-4,-6,-3,-5,-6,-2,-4,-4,-10,-9,-9,10,6,1,5,-10,8,-5,-7,-10,7,8,3,-6,-6,-9,10,5,1,5,-1,-5,5,10,10,4,3,1,-5,-9,4,6,-9,1,-6,8,-3,6,4,-1,9,-2,-7,-8,-9,-3,-7,6,1,8,6,-7,-10,7,1,8,3,-2,-10,5,7,2,-9,2,8,9,7,-2,-9,2,-9,1,8,-6,-4,-10,1,5,-2,1,-8,-3,6,-3,-8,-8,3,9,-5,-2,6,-9,5,8,-10,9,-9,2,-10,4,-10,-5,2,-6,10,5,1,-4,8,6,-1,8,9,-7,7,-7,4,9,5,-2,-5,-1,-8,7,-7,8,7,-7,-7,5,8,8,3,7,-5,3,3,-10,-6,-1,-9,-10,2,-3,4,3,-2,-3,10,-3,6,-7,-9,-1,2,-10,10,7,7,-1,2,4,-6,-8,-8,1,6,-4,3,-10,9,7,-9,-1,6,1,7,1,6,-8,-10,-8,-7,1,-10,-6,-2,8,7,10,-3,-1,-8,-4,2,9,-2,-8,9,-8,4,-10,9,8,9,-1,-10,-3,-7,-5,10,10,-10,1,-10,10,5,10,10,-9,-7,1,3,10,-4,6,8,6,-6,7,7,2,7,-5,-10,-8,-3,8,5,-5,-4,3,-10,-10,-7,4,4,6,-6,10,5,6,-9,7,4,-2,-4,-10,5,1,-7,-6,9,-2,-6,4,2,-1,-6,-4,-10,-1,-1,-1,3,8,8,-10,-9,3,-9,-7,1,-2,8,-9,4,5,5,4,1,-7,-8,-6,-1,2,-8,-9,-9,-5,-8,-5,8,-8,9,8,-3,-9,-2,-10,3,-1,3,1,-2,8,5,-2,7,-4,9,-6,-9,-3,-9,-3,7,5,-7,-1,-5,9,-4,10,1,10,8,-2,1,7,10,-4,8,-4,-6,-2,-6,8,3,3,-4,4,9,10,-1,3,8,8,-5,-1,-1,-1,-5,7,8,2,5,7,-1,-7,5,6,5,1,8,10,-4,-6,-9,1,-5,1,-8,-5,7,-3,-9,-6,-3,-4,-9,-10,-5,-6,-1,2,-9,-7,3,-5,-5,-1,-7,9,-3,1,-9,-7,-9,-7,-7,10,3,-2,-1,-7,5,-1,8,-2,-4,5,6,-8,-4,-9,5,8,9,6,-8,6,-4,8,8,-3,3,-8,9,-7], dtype = "uint16")#candidate|2675|(847,)|const|uint16
call_2674 = relay.TupleGetItem(func_1824_call(relay.reshape(const_2675.astype('uint16'), [11, 11, 7]), relay.reshape(const_2675.astype('uint16'), [11, 11, 7]), ), 0)
call_2676 = relay.TupleGetItem(func_1828_call(relay.reshape(const_2675.astype('uint16'), [11, 11, 7]), relay.reshape(const_2675.astype('uint16'), [11, 11, 7]), ), 0)
func_1794_call = mod.get_global_var('func_1794')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_2677 = func_1794_call()
call_2678 = func_1794_call()
bop_2685 = relay.add(call_2625.astype('float64'), var_2643.astype('float64')) # shape=(5, 11, 4)
bop_2688 = relay.add(call_2626.astype('float64'), var_2643.astype('float64')) # shape=(5, 11, 4)
uop_2709 = relay.atanh(call_2662.astype('float64')) # shape=(11, 13, 15)
uop_2711 = relay.atanh(call_2664.astype('float64')) # shape=(11, 13, 15)
func_1925_call = mod.get_global_var('func_1925')
func_1927_call = mutated_mod.get_global_var('func_1927')
call_2717 = relay.TupleGetItem(func_1925_call(), 0)
call_2718 = relay.TupleGetItem(func_1927_call(), 0)
func_1846_call = mod.get_global_var('func_1846')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_2726 = relay.TupleGetItem(func_1846_call(), 0)
call_2727 = relay.TupleGetItem(func_1848_call(), 0)
output = relay.Tuple([call_2598,call_2639,call_2642,const_2644,call_2652,var_2663,call_2674,const_2675,call_2677,bop_2685,uop_2709,call_2717,call_2726,])
output2 = relay.Tuple([call_2599,call_2640,call_2645,const_2644,call_2653,var_2663,call_2676,const_2675,call_2678,bop_2688,uop_2711,call_2718,call_2727,])
func_2728 = relay.Function([var_2643,var_2663,], output)
mod['func_2728'] = func_2728
mod = relay.transform.InferType()(mod)
var_2729 = relay.var("var_2729", dtype = "int32", shape = ())#candidate|2729|()|var|int32
var_2730 = relay.var("var_2730", dtype = "float32", shape = (2145,))#candidate|2730|(2145,)|var|float32
output = func_2728(var_2729,var_2730,)
func_2731 = relay.Function([var_2729,var_2730,], output)
mutated_mod['func_2731'] = func_2731
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2791 = relay.var("var_2791", dtype = "float64", shape = (1, 11, 6))#candidate|2791|(1, 11, 6)|var|float64
uop_2792 = relay.cos(var_2791.astype('float64')) # shape=(1, 11, 6)
bop_2795 = relay.logical_and(uop_2792.astype('bool'), relay.reshape(var_2791.astype('bool'), relay.shape_of(uop_2792))) # shape=(1, 11, 6)
output = relay.Tuple([bop_2795,])
output2 = relay.Tuple([bop_2795,])
func_2801 = relay.Function([var_2791,], output)
mod['func_2801'] = func_2801
mod = relay.transform.InferType()(mod)
mutated_mod['func_2801'] = func_2801
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2802 = relay.var("var_2802", dtype = "float64", shape = (1, 11, 6))#candidate|2802|(1, 11, 6)|var|float64
func_2801_call = mutated_mod.get_global_var('func_2801')
call_2803 = func_2801_call(var_2802)
output = call_2803
func_2804 = relay.Function([var_2802], output)
mutated_mod['func_2804'] = func_2804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_412_call = mod.get_global_var('func_412')
func_414_call = mutated_mod.get_global_var('func_414')
call_2814 = func_412_call()
call_2815 = func_412_call()
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_2830 = relay.TupleGetItem(func_859_call(), 0)
call_2831 = relay.TupleGetItem(func_860_call(), 0)
output = relay.Tuple([call_2814,call_2830,])
output2 = relay.Tuple([call_2815,call_2831,])
func_2832 = relay.Function([], output)
mod['func_2832'] = func_2832
mod = relay.transform.InferType()(mod)
mutated_mod['func_2832'] = func_2832
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2832_call = mutated_mod.get_global_var('func_2832')
call_2833 = func_2832_call()
output = call_2833
func_2834 = relay.Function([], output)
mutated_mod['func_2834'] = func_2834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1925_call = mod.get_global_var('func_1925')
func_1927_call = mutated_mod.get_global_var('func_1927')
call_2862 = relay.TupleGetItem(func_1925_call(), 0)
call_2863 = relay.TupleGetItem(func_1927_call(), 0)
func_1955_call = mod.get_global_var('func_1955')
func_1956_call = mutated_mod.get_global_var('func_1956')
call_2868 = func_1955_call()
call_2869 = func_1955_call()
output = relay.Tuple([call_2862,call_2868,])
output2 = relay.Tuple([call_2863,call_2869,])
func_2900 = relay.Function([], output)
mod['func_2900'] = func_2900
mod = relay.transform.InferType()(mod)
mutated_mod['func_2900'] = func_2900
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mutated_mod.get_global_var('func_2900')
call_2901 = func_2900_call()
output = call_2901
func_2902 = relay.Function([], output)
mutated_mod['func_2902'] = func_2902
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1043_call = mod.get_global_var('func_1043')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_2912 = relay.TupleGetItem(func_1043_call(), 3)
call_2913 = relay.TupleGetItem(func_1045_call(), 3)
output = relay.Tuple([call_2912,])
output2 = relay.Tuple([call_2913,])
func_2936 = relay.Function([], output)
mod['func_2936'] = func_2936
mod = relay.transform.InferType()(mod)
output = func_2936()
func_2937 = relay.Function([], output)
mutated_mod['func_2937'] = func_2937
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1398_call = mod.get_global_var('func_1398')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_2999 = relay.TupleGetItem(func_1398_call(), 2)
call_3000 = relay.TupleGetItem(func_1399_call(), 2)
output = relay.Tuple([call_2999,])
output2 = relay.Tuple([call_3000,])
func_3008 = relay.Function([], output)
mod['func_3008'] = func_3008
mod = relay.transform.InferType()(mod)
output = func_3008()
func_3009 = relay.Function([], output)
mutated_mod['func_3009'] = func_3009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_3069 = func_397_call()
call_3070 = func_397_call()
output = relay.Tuple([call_3069,])
output2 = relay.Tuple([call_3070,])
func_3073 = relay.Function([], output)
mod['func_3073'] = func_3073
mod = relay.transform.InferType()(mod)
mutated_mod['func_3073'] = func_3073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3073_call = mutated_mod.get_global_var('func_3073')
call_3074 = func_3073_call()
output = call_3074
func_3075 = relay.Function([], output)
mutated_mod['func_3075'] = func_3075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_3108 = relay.TupleGetItem(func_684_call(), 0)
call_3109 = relay.TupleGetItem(func_686_call(), 0)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_3121 = relay.TupleGetItem(func_1883_call(), 1)
call_3122 = relay.TupleGetItem(func_1885_call(), 1)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_3126 = func_1425_call()
call_3127 = func_1425_call()
output = relay.Tuple([call_3108,call_3121,call_3126,])
output2 = relay.Tuple([call_3109,call_3122,call_3127,])
func_3128 = relay.Function([], output)
mod['func_3128'] = func_3128
mod = relay.transform.InferType()(mod)
output = func_3128()
func_3129 = relay.Function([], output)
mutated_mod['func_3129'] = func_3129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_3162 = func_526_call()
call_3163 = func_526_call()
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_3172 = relay.TupleGetItem(func_941_call(relay.reshape(call_3162.astype('float64'), [5, 11, 4])), 0)
call_3173 = relay.TupleGetItem(func_943_call(relay.reshape(call_3162.astype('float64'), [5, 11, 4])), 0)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_3181 = relay.TupleGetItem(func_1883_call(), 0)
call_3182 = relay.TupleGetItem(func_1885_call(), 0)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_3209 = func_361_call()
call_3210 = func_361_call()
output = relay.Tuple([call_3162,call_3172,call_3181,call_3209,])
output2 = relay.Tuple([call_3163,call_3173,call_3182,call_3210,])
func_3211 = relay.Function([], output)
mod['func_3211'] = func_3211
mod = relay.transform.InferType()(mod)
mutated_mod['func_3211'] = func_3211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3211_call = mutated_mod.get_global_var('func_3211')
call_3212 = func_3211_call()
output = call_3212
func_3213 = relay.Function([], output)
mutated_mod['func_3213'] = func_3213
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3219 = relay.var("var_3219", dtype = "uint16", shape = ())#candidate|3219|()|var|uint16
var_3220 = relay.var("var_3220", dtype = "uint16", shape = (9, 2, 13))#candidate|3220|(9, 2, 13)|var|uint16
bop_3221 = relay.logical_xor(var_3219.astype('uint16'), var_3220.astype('uint16')) # shape=(9, 2, 13)
output = bop_3221
output2 = bop_3221
func_3236 = relay.Function([var_3219,var_3220,], output)
mod['func_3236'] = func_3236
mod = relay.transform.InferType()(mod)
var_3237 = relay.var("var_3237", dtype = "uint16", shape = ())#candidate|3237|()|var|uint16
var_3238 = relay.var("var_3238", dtype = "uint16", shape = (9, 2, 13))#candidate|3238|(9, 2, 13)|var|uint16
output = func_3236(var_3237,var_3238,)
func_3239 = relay.Function([var_3237,var_3238,], output)
mutated_mod['func_3239'] = func_3239
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3271 = relay.var("var_3271", dtype = "float32", shape = (1, 6, 14))#candidate|3271|(1, 6, 14)|var|float32
uop_3272 = relay.cos(var_3271.astype('float32')) # shape=(1, 6, 14)
output = relay.Tuple([uop_3272,])
output2 = relay.Tuple([uop_3272,])
func_3296 = relay.Function([var_3271,], output)
mod['func_3296'] = func_3296
mod = relay.transform.InferType()(mod)
var_3297 = relay.var("var_3297", dtype = "float32", shape = (1, 6, 14))#candidate|3297|(1, 6, 14)|var|float32
output = func_3296(var_3297)
func_3298 = relay.Function([var_3297], output)
mutated_mod['func_3298'] = func_3298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_3337 = func_1072_call()
call_3338 = func_1072_call()
output = call_3337
output2 = call_3338
func_3340 = relay.Function([], output)
mod['func_3340'] = func_3340
mod = relay.transform.InferType()(mod)
mutated_mod['func_3340'] = func_3340
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3340_call = mutated_mod.get_global_var('func_3340')
call_3341 = func_3340_call()
output = call_3341
func_3342 = relay.Function([], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1398_call = mod.get_global_var('func_1398')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_3459 = relay.TupleGetItem(func_1398_call(), 0)
call_3460 = relay.TupleGetItem(func_1399_call(), 0)
func_629_call = mod.get_global_var('func_629')
func_633_call = mutated_mod.get_global_var('func_633')
const_3465 = relay.const(1.595811, dtype = "float32")#candidate|3465|()|const|float32
const_3466 = relay.const([-2.129573,3.175571,-2.430607,5.466258,-9.456085,1.207981,-7.611764,-4.397215,-2.663580,-1.388989,-2.240754,-6.401444,7.664735,4.744541,-6.742043,-1.136385,7.769511,4.135883,-1.722292,-5.101532,5.691951,-9.236882,-5.089963,-7.577787,2.038500,-7.617946,-0.811472,-6.467213,-5.548153,-0.997591,9.778179,9.255083,-4.003175,-5.159320,-3.736813,8.132968,6.062433,4.905570,-5.157573,-8.237095,5.277191,6.073141,-3.000955,1.342095,4.372694,5.440057,7.372569,-5.699846,6.716949,-0.405387,4.853609,4.332534,8.488483,-4.649017,-4.519477,2.123412,-8.523442,-3.649230,-8.426464,0.978450,3.961799,-9.396233,-4.228394,6.449861,-4.347470,0.918624,5.063200,-1.783721,3.105980,5.834128,6.731606,9.459241,6.084788,-9.402585,-3.323152,-7.304678,5.811931,-5.073226,7.657090,7.410616,5.580528,2.049514,-0.942815,9.822390,3.701357,8.692559,7.077424,-2.265754,-2.679009,3.740970,-2.018179,6.313690,-7.224497,5.228991,0.652475,2.085727,1.209634,6.149394], dtype = "float32")#candidate|3466|(98,)|const|float32
call_3464 = relay.TupleGetItem(func_629_call(relay.reshape(const_3465.astype('float32'), []), relay.reshape(const_3466.astype('float32'), [14, 7, 1]), ), 0)
call_3467 = relay.TupleGetItem(func_633_call(relay.reshape(const_3465.astype('float32'), []), relay.reshape(const_3466.astype('float32'), [14, 7, 1]), ), 0)
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_3468 = func_3340_call()
call_3469 = func_3340_call()
func_3008_call = mod.get_global_var('func_3008')
func_3009_call = mutated_mod.get_global_var('func_3009')
call_3477 = relay.TupleGetItem(func_3008_call(), 0)
call_3478 = relay.TupleGetItem(func_3009_call(), 0)
uop_3488 = relay.acosh(call_3464.astype('float64')) # shape=(14, 7, 1)
uop_3490 = relay.acosh(call_3467.astype('float64')) # shape=(14, 7, 1)
output = relay.Tuple([call_3459,const_3465,const_3466,call_3468,call_3477,uop_3488,])
output2 = relay.Tuple([call_3460,const_3465,const_3466,call_3469,call_3478,uop_3490,])
func_3508 = relay.Function([], output)
mod['func_3508'] = func_3508
mod = relay.transform.InferType()(mod)
mutated_mod['func_3508'] = func_3508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mutated_mod.get_global_var('func_3508')
call_3509 = func_3508_call()
output = call_3509
func_3510 = relay.Function([], output)
mutated_mod['func_3510'] = func_3510
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1794_call = mod.get_global_var('func_1794')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_3514 = func_1794_call()
call_3515 = func_1794_call()
output = relay.Tuple([call_3514,])
output2 = relay.Tuple([call_3515,])
func_3537 = relay.Function([], output)
mod['func_3537'] = func_3537
mod = relay.transform.InferType()(mod)
mutated_mod['func_3537'] = func_3537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3537_call = mutated_mod.get_global_var('func_3537')
call_3538 = func_3537_call()
output = call_3538
func_3539 = relay.Function([], output)
mutated_mod['func_3539'] = func_3539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3607 = relay.var("var_3607", dtype = "float64", shape = (1, 15, 10))#candidate|3607|(1, 15, 10)|var|float64
uop_3608 = relay.tan(var_3607.astype('float64')) # shape=(1, 15, 10)
output = relay.Tuple([uop_3608,])
output2 = relay.Tuple([uop_3608,])
func_3619 = relay.Function([var_3607,], output)
mod['func_3619'] = func_3619
mod = relay.transform.InferType()(mod)
mutated_mod['func_3619'] = func_3619
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3620 = relay.var("var_3620", dtype = "float64", shape = (1, 15, 10))#candidate|3620|(1, 15, 10)|var|float64
func_3619_call = mutated_mod.get_global_var('func_3619')
call_3621 = func_3619_call(var_3620)
output = call_3621
func_3622 = relay.Function([var_3620], output)
mutated_mod['func_3622'] = func_3622
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_3651 = relay.TupleGetItem(func_684_call(), 0)
call_3652 = relay.TupleGetItem(func_686_call(), 0)
output = call_3651
output2 = call_3652
func_3653 = relay.Function([], output)
mod['func_3653'] = func_3653
mod = relay.transform.InferType()(mod)
mutated_mod['func_3653'] = func_3653
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3653_call = mutated_mod.get_global_var('func_3653')
call_3654 = func_3653_call()
output = call_3654
func_3655 = relay.Function([], output)
mutated_mod['func_3655'] = func_3655
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_3677 = func_1425_call()
call_3678 = func_1425_call()
func_397_call = mod.get_global_var('func_397')
func_398_call = mutated_mod.get_global_var('func_398')
call_3688 = func_397_call()
call_3689 = func_397_call()
output = relay.Tuple([call_3677,call_3688,])
output2 = relay.Tuple([call_3678,call_3689,])
func_3698 = relay.Function([], output)
mod['func_3698'] = func_3698
mod = relay.transform.InferType()(mod)
mutated_mod['func_3698'] = func_3698
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3698_call = mutated_mod.get_global_var('func_3698')
call_3699 = func_3698_call()
output = call_3699
func_3700 = relay.Function([], output)
mutated_mod['func_3700'] = func_3700
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3742 = relay.const([[[-2.079925,-1.667552,4.304789,0.213963,-9.419280,-0.819801,-9.419106,1.070694,-6.296124,-3.188593,-5.795879,6.496694,1.866145,-8.795504,6.411076],[-3.528156,-2.853851,4.307545,5.298116,-6.275046,7.694729,-4.899482,-7.095111,-0.663784,6.278891,-8.444667,4.944976,7.485540,-8.340315,5.953523],[-0.460974,1.502282,-2.468052,-5.737224,4.600478,-8.888840,5.434799,2.183377,-7.533384,-0.023475,-0.777408,6.036072,9.940542,-3.980006,9.070517],[4.618379,-0.260711,-3.621820,7.617256,-2.991667,9.210125,7.827476,0.708953,-7.479946,-2.430506,0.717590,3.515553,-9.418357,3.286519,-5.759502],[-7.157345,-8.918689,4.873006,2.359402,6.123123,8.544371,-1.147470,-0.417189,7.327038,-1.415100,7.523497,7.335184,-5.923867,7.561782,-6.786189],[-6.093666,0.059432,3.081642,0.633134,5.474999,-6.163781,-4.986242,8.607902,-9.394199,7.687808,-0.065030,-4.947980,-9.899608,7.325182,5.388731],[2.815366,-3.436045,-5.901183,4.204095,0.813405,4.368064,-2.775333,-1.476460,-5.279874,-2.189616,5.002334,-2.208126,-3.765008,9.670612,0.948894],[-0.587193,-6.438271,5.343428,-6.721429,4.113219,-1.053305,-7.810856,-2.854223,-7.503542,7.477666,-4.129921,-8.933428,0.463774,3.301631,-6.746081],[7.063311,-0.005362,-0.645231,-8.619554,-6.597428,-1.687115,-4.870081,7.873572,6.408778,3.844819,5.480965,-9.522361,2.873410,-1.729240,-2.581622],[6.174910,4.283638,3.177677,2.512518,9.830793,6.318389,-4.075284,-8.314215,-3.446396,-9.101522,-5.267739,-2.211827,6.997143,-8.048566,-1.425663],[-2.070358,-9.664947,2.116221,0.423844,-2.628633,3.816120,-7.775981,8.746600,8.865252,2.218015,-2.345211,9.708757,-8.948588,-0.503020,1.252755],[2.690627,-6.813054,0.772178,6.327258,-8.495034,9.512985,-8.813170,-4.471492,-9.537334,5.494072,7.372142,-8.405605,-8.614190,8.525889,0.537424],[-4.165445,-3.996106,4.411878,-5.093485,1.685660,-0.650610,-9.812828,-9.894241,-8.094256,5.090245,-1.751839,4.275281,1.441109,3.593114,-1.648195]],[[0.328305,6.366056,3.822007,-1.467032,-3.332089,3.273405,-4.512165,4.093775,-1.330440,-0.474686,0.147278,-6.936360,4.955676,9.996602,-1.223542],[7.025176,-4.736860,5.820567,2.585451,8.845433,6.995380,-8.583461,9.368012,4.048218,-2.342007,1.999742,-5.116876,-9.372626,6.272901,2.932002],[-2.960982,-9.181551,6.759275,-9.172282,1.564365,-4.697022,-0.585439,-8.929039,-9.403320,5.552007,1.783440,1.691238,-0.187898,7.270962,3.013142],[3.582156,-2.429280,-2.931374,-0.665862,-1.613108,-9.876018,-0.210535,-6.170027,-5.207087,-9.198639,5.129067,-9.917314,-3.237889,-6.691344,0.646882],[-4.723983,5.142491,-0.455392,-9.285437,0.505837,-2.667698,-0.634930,-5.742289,1.418339,3.191133,4.383698,-6.218745,6.703778,-8.258243,-1.760751],[3.113123,4.529200,2.410707,-1.120592,-9.902728,3.716733,-6.676748,2.789620,-0.982034,7.250984,9.613210,-9.859586,6.113770,-6.099773,4.065896],[0.419943,1.541740,-5.364927,-7.058243,-1.430388,-1.328915,2.736341,9.812156,3.407118,5.068797,-5.177567,1.655203,-8.471685,-8.722591,7.082198],[-1.697132,0.046545,0.596546,-5.368581,-0.448794,-1.927154,-5.333253,7.088844,-2.102258,8.162272,-1.823503,-7.593068,-4.345743,-9.494021,5.404679],[2.972481,-2.405171,4.110339,-3.097075,3.405782,0.686424,8.642184,0.789157,8.549172,3.583096,8.458318,-6.712239,-6.608452,1.229501,-3.347586],[-0.590306,-2.605307,-1.591457,-8.313938,5.569941,4.749835,9.677744,9.504927,-8.593509,-9.873470,0.545411,2.879822,-3.658327,4.948275,-2.965065],[-7.800179,0.298305,5.812857,8.706292,-5.390598,3.893299,5.121938,-3.639224,8.238748,3.092470,-5.035910,1.856696,0.782832,7.231377,0.939415],[-4.989382,-2.879738,-1.033420,0.862992,5.495796,2.153244,0.415364,7.467401,9.386621,-6.213883,7.991349,1.612799,-3.040591,-5.426997,4.452472],[3.932778,2.770810,5.705186,4.201756,2.690582,-4.099506,6.471180,1.550125,4.153372,8.177779,-1.772960,3.090052,-5.122862,-3.480623,4.388496]],[[-5.116966,5.702882,7.641828,-3.738815,7.737708,5.192274,-7.997587,5.020234,-8.090569,-0.658778,6.421092,-8.592932,-3.456945,-2.735081,9.984269],[6.995530,7.650076,0.454213,6.329222,5.677358,-3.030678,7.341193,-7.259223,-0.855029,6.010376,-8.459601,6.966808,5.208088,6.793738,-0.356685],[-2.494928,5.325129,-4.085728,-3.271099,-2.302882,-2.666336,-3.911865,3.243413,9.049364,8.299599,-7.933123,6.977328,-9.818665,1.424858,-6.029287],[-1.144704,7.998548,-1.036895,8.274936,-2.577847,2.688636,-6.431749,-4.684877,-3.194014,5.552990,-3.213070,0.879015,-3.502706,9.905014,-0.912932],[3.334692,-1.099188,-2.865280,9.483114,7.417480,6.878757,-8.236875,-0.825906,1.007626,-7.967943,1.304148,-1.134889,-8.070128,-5.884450,-3.976488],[-5.973311,-1.161655,1.098492,2.579003,-5.740602,-8.203625,7.518533,3.004172,9.763182,-1.194431,6.508388,-6.593038,1.320839,-3.609032,-9.826619],[-1.979831,8.918276,8.978484,5.904857,1.066348,0.134207,6.382904,-2.852127,0.213174,6.750261,-5.608291,0.930346,-3.343316,1.389090,-9.022913],[0.897518,-4.215186,6.346211,9.158838,7.638153,-4.521980,-3.418724,8.770859,-2.430486,-2.278088,2.218360,0.470831,-7.982446,0.310259,-4.707257],[5.085991,-6.836986,-7.823145,-0.868741,-4.559349,-9.264188,-7.187933,-1.981890,-2.742804,-9.871267,-1.276687,7.576800,-5.260785,3.804957,0.483739],[-8.771818,4.994377,4.419655,-2.606327,-1.984578,4.983833,-2.230006,7.700698,1.807086,2.267537,8.727529,7.878096,5.268175,-1.878542,6.967526],[2.346946,-3.230415,-0.066661,-8.702846,2.137002,9.118550,-4.011634,8.815701,-4.365751,3.819955,-1.576041,3.012994,4.438583,-6.775698,6.112468],[6.148923,1.155347,-8.332061,6.481173,-9.026354,1.661087,5.287554,1.869901,2.067490,-4.964571,-8.046639,3.592209,-0.250282,-4.725421,-5.323023],[7.478146,-5.917770,-7.498215,-7.021270,-6.166644,-8.458668,7.446820,8.254013,-5.202756,-6.326423,9.661066,-9.109046,8.926682,1.248248,4.363827]],[[9.821662,9.987530,2.447678,-1.752938,-8.109594,-2.422656,-7.180161,-0.933806,1.608261,7.920319,1.818949,-1.379845,1.619973,3.107313,4.254678],[7.853546,1.493270,0.281631,-1.909121,-4.609778,-2.852758,5.304339,-0.179093,-2.362220,3.920964,-5.045557,-9.924605,-0.124096,-7.455218,-5.796222],[-0.864943,-5.656375,-6.080965,-3.240121,-8.485975,9.787896,5.318249,4.238090,5.588839,0.473727,3.774238,9.140412,-0.600943,-2.070580,3.968783],[8.898850,-5.094555,4.223037,0.107579,5.370342,9.938772,-3.549927,2.523522,-4.750816,9.669958,1.796320,5.169002,-9.186861,-0.248745,-6.074702],[2.430036,0.600460,-3.831955,-9.461693,-9.793696,8.006811,6.124034,9.854829,4.087555,2.948457,5.766018,-0.476667,6.221380,6.730910,7.061352],[-8.209547,3.587702,-3.271677,-4.372933,6.765382,-1.206706,-3.860689,-1.527083,-3.403259,-3.224483,-4.413603,8.484941,-7.215844,4.998264,-1.632947],[-1.515324,9.827623,4.721472,1.311986,-1.185578,-6.480065,4.684172,-6.299851,-0.820075,6.267898,-0.395858,1.331441,-1.914343,5.596346,2.812989],[-7.307853,-0.595747,7.110481,2.693962,2.007197,6.355469,-6.032463,3.651160,-3.477476,-4.362347,-7.222555,4.291301,-9.213726,2.291165,4.394206],[2.209800,-3.797634,5.266147,4.601593,-0.053692,-7.369387,7.561009,-5.933142,-8.618292,-9.727803,0.953526,5.536063,-5.580218,-5.324944,5.158485],[-5.197470,-3.008637,-6.779979,-6.505833,-1.863136,5.218835,-7.656931,-8.233824,8.739363,6.626087,7.385499,-7.861581,1.679103,-5.492017,-1.812243],[8.654852,-3.875339,-4.871533,6.281027,3.073854,0.822770,3.047718,4.788925,3.121762,-6.153432,-7.606854,2.677877,-8.196508,-0.009278,-4.780835],[4.196446,6.612002,7.388347,-6.352468,2.633582,1.189709,-9.966763,-3.584672,-0.576490,-0.626474,7.647049,-2.269649,5.529458,8.380576,9.377172],[4.431842,-9.501080,-4.495993,-7.059624,-2.478769,-4.707364,-9.727595,-9.203180,-1.139118,-0.034835,8.579289,-2.030977,-5.244849,0.083817,7.899826]],[[-6.050989,8.759265,4.520463,-9.936900,-5.303839,2.727509,-8.239285,-7.165196,8.473752,5.728241,9.362146,7.351297,-7.882219,-1.850577,2.358591],[-6.036737,-7.478598,-1.417427,-0.043288,4.996986,-1.332349,5.528624,-9.515105,7.007580,7.267715,-3.342636,-1.891267,-2.869173,1.555583,-1.676410],[-9.801980,-0.239842,-7.893853,-6.470100,-8.481463,5.664600,0.284908,7.381461,-9.187348,2.689497,-9.057263,3.539054,3.432253,0.333396,-5.747916],[7.533028,4.545730,4.809095,8.111577,-1.228405,9.244977,-6.902068,-3.425042,-4.350399,-7.878937,-2.055884,3.367770,1.037134,6.377575,-6.808841],[-5.528181,-5.548514,1.205784,9.749285,-6.561266,-2.481629,-2.624405,-3.119352,2.951667,6.832543,-6.954413,-7.163202,5.462088,-1.024304,-0.993024],[-4.316629,-9.484327,-5.206912,-2.611125,-9.201541,2.304140,-0.385752,4.940940,0.569257,-5.666147,8.733568,-7.401627,-3.677232,2.252642,4.135441],[5.225824,5.156262,-9.153419,-4.544086,4.298857,0.134360,6.362531,-9.706849,-7.911636,8.277834,3.419444,4.440303,-6.199620,9.568569,-5.052200],[-4.220428,3.094353,-9.534576,0.243364,-1.434804,1.761245,-4.339691,-0.599384,-4.920023,-6.739693,8.809519,-2.928333,2.232587,-2.810729,-0.069320],[5.352777,2.134079,-0.272642,4.073108,-7.093038,9.499141,0.469872,-5.583314,-0.581044,6.388188,2.640906,-9.267523,6.372137,-7.830072,0.779190],[6.492637,7.181327,9.217942,-5.533831,-1.943536,-0.763931,-3.852751,6.556942,4.064562,4.804246,-6.635361,7.589305,-6.213967,-0.385129,2.766751],[-7.748450,5.431278,6.937996,0.086721,4.523930,-9.068172,4.375936,8.963943,4.649889,3.483433,1.354642,5.851227,-1.800313,-3.227028,9.217867],[-0.651637,-0.085745,0.482448,-0.327717,3.631481,-3.606453,-4.337571,-6.450338,-7.902077,-1.417668,7.714299,0.130555,2.975063,-2.414286,8.285902],[0.695636,7.783226,7.162974,7.443446,-9.537362,6.838120,-0.871153,-0.772985,2.571982,-7.932415,-2.662046,-4.198222,1.140863,-9.982200,1.753982]]], dtype = "float64")#candidate|3742|(5, 13, 15)|const|float64
uop_3743 = relay.atanh(const_3742.astype('float64')) # shape=(5, 13, 15)
output = relay.Tuple([uop_3743,])
output2 = relay.Tuple([uop_3743,])
func_3745 = relay.Function([], output)
mod['func_3745'] = func_3745
mod = relay.transform.InferType()(mod)
mutated_mod['func_3745'] = func_3745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3745_call = mutated_mod.get_global_var('func_3745')
call_3746 = func_3745_call()
output = call_3746
func_3747 = relay.Function([], output)
mutated_mod['func_3747'] = func_3747
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3772 = relay.const([[[-0.704954],[9.921833],[-1.954639],[0.441979],[-8.612234],[2.761621],[-5.679968]],[[3.522928],[-8.756398],[-0.160423],[-4.482186],[8.807422],[3.057148],[2.205016]],[[9.293420],[6.872362],[-9.215968],[6.295173],[-3.782880],[7.326971],[6.722214]],[[3.649289],[6.675312],[-4.267084],[-0.118741],[5.130901],[1.999575],[0.006629]],[[7.322076],[4.922645],[6.384568],[-1.239303],[-4.886594],[0.355557],[-3.412739]],[[1.893439],[4.911352],[-2.158189],[9.227041],[-4.896170],[7.263160],[-4.305882]],[[-7.205970],[-9.663543],[5.726181],[-6.349266],[-2.353315],[-9.542632],[5.927851]],[[1.847056],[3.085179],[0.679501],[-7.359383],[6.396314],[-5.894360],[1.028484]],[[2.328189],[-7.332793],[6.053567],[3.185479],[-4.937643],[-8.259572],[5.851495]],[[6.294530],[-3.589961],[-6.686362],[-6.498451],[-2.183702],[9.675419],[-8.015115]],[[-6.162541],[-3.891089],[-1.160981],[2.436254],[2.703963],[-3.065321],[7.749171]],[[-2.386442],[4.916014],[6.611814],[-3.442285],[0.935310],[6.758186],[3.854482]],[[-7.012495],[-0.853793],[9.352479],[-9.375034],[7.214279],[-4.952475],[1.249117]],[[-6.871157],[1.561486],[2.204637],[9.461397],[-3.137041],[-7.068292],[-1.241884]],[[9.467244],[6.395058],[6.135845],[-4.383160],[-3.233421],[-3.552414],[3.875197]],[[-9.942222],[9.918487],[2.305121],[8.368635],[-6.775103],[3.764821],[-1.690574]]], dtype = "float32")#candidate|3772|(16, 7, 1)|const|float32
uop_3773 = relay.tan(const_3772.astype('float32')) # shape=(16, 7, 1)
bop_3778 = relay.subtract(const_3772.astype('uint64'), relay.reshape(uop_3773.astype('uint64'), relay.shape_of(const_3772))) # shape=(16, 7, 1)
output = relay.Tuple([bop_3778,])
output2 = relay.Tuple([bop_3778,])
func_3806 = relay.Function([], output)
mod['func_3806'] = func_3806
mod = relay.transform.InferType()(mod)
output = func_3806()
func_3807 = relay.Function([], output)
mutated_mod['func_3807'] = func_3807
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1925_call = mod.get_global_var('func_1925')
func_1927_call = mutated_mod.get_global_var('func_1927')
call_3837 = relay.TupleGetItem(func_1925_call(), 1)
call_3838 = relay.TupleGetItem(func_1927_call(), 1)
output = call_3837
output2 = call_3838
func_3846 = relay.Function([], output)
mod['func_3846'] = func_3846
mod = relay.transform.InferType()(mod)
output = func_3846()
func_3847 = relay.Function([], output)
mutated_mod['func_3847'] = func_3847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2197_call = mod.get_global_var('func_2197')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_3848 = relay.TupleGetItem(func_2197_call(), 0)
call_3849 = relay.TupleGetItem(func_2199_call(), 0)
output = call_3848
output2 = call_3849
func_3850 = relay.Function([], output)
mod['func_3850'] = func_3850
mod = relay.transform.InferType()(mod)
mutated_mod['func_3850'] = func_3850
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3850_call = mutated_mod.get_global_var('func_3850')
call_3851 = func_3850_call()
output = call_3851
func_3852 = relay.Function([], output)
mutated_mod['func_3852'] = func_3852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3537_call = mod.get_global_var('func_3537')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_3879 = relay.TupleGetItem(func_3537_call(), 0)
call_3880 = relay.TupleGetItem(func_3539_call(), 0)
output = relay.Tuple([call_3879,])
output2 = relay.Tuple([call_3880,])
func_3897 = relay.Function([], output)
mod['func_3897'] = func_3897
mod = relay.transform.InferType()(mod)
output = func_3897()
func_3898 = relay.Function([], output)
mutated_mod['func_3898'] = func_3898
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2902_call = mutated_mod.get_global_var('func_2902')
call_3989 = relay.TupleGetItem(func_2900_call(), 1)
call_3990 = relay.TupleGetItem(func_2902_call(), 1)
output = call_3989
output2 = call_3990
func_3993 = relay.Function([], output)
mod['func_3993'] = func_3993
mod = relay.transform.InferType()(mod)
mutated_mod['func_3993'] = func_3993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3993_call = mutated_mod.get_global_var('func_3993')
call_3994 = func_3993_call()
output = call_3994
func_3995 = relay.Function([], output)
mutated_mod['func_3995'] = func_3995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2832_call = mod.get_global_var('func_2832')
func_2834_call = mutated_mod.get_global_var('func_2834')
call_4005 = relay.TupleGetItem(func_2832_call(), 1)
call_4006 = relay.TupleGetItem(func_2834_call(), 1)
var_4009 = relay.var("var_4009", dtype = "float32", shape = (5, 11, 4))#candidate|4009|(5, 11, 4)|var|float32
bop_4010 = relay.bitwise_xor(call_4005.astype('int16'), relay.reshape(var_4009.astype('int16'), relay.shape_of(call_4005))) # shape=(5, 11, 4)
bop_4013 = relay.bitwise_xor(call_4006.astype('int16'), relay.reshape(var_4009.astype('int16'), relay.shape_of(call_4006))) # shape=(5, 11, 4)
output = relay.Tuple([bop_4010,])
output2 = relay.Tuple([bop_4013,])
func_4025 = relay.Function([var_4009,], output)
mod['func_4025'] = func_4025
mod = relay.transform.InferType()(mod)
mutated_mod['func_4025'] = func_4025
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4026 = relay.var("var_4026", dtype = "float32", shape = (5, 11, 4))#candidate|4026|(5, 11, 4)|var|float32
func_4025_call = mutated_mod.get_global_var('func_4025')
call_4027 = func_4025_call(var_4026)
output = call_4027
func_4028 = relay.Function([var_4026], output)
mutated_mod['func_4028'] = func_4028
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3653_call = mod.get_global_var('func_3653')
func_3655_call = mutated_mod.get_global_var('func_3655')
call_4043 = func_3653_call()
call_4044 = func_3653_call()
uop_4063 = relay.sinh(call_4043.astype('float64')) # shape=(5, 11, 4)
uop_4065 = relay.sinh(call_4044.astype('float64')) # shape=(5, 11, 4)
func_3745_call = mod.get_global_var('func_3745')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4077 = relay.TupleGetItem(func_3745_call(), 0)
call_4078 = relay.TupleGetItem(func_3747_call(), 0)
output = relay.Tuple([uop_4063,call_4077,])
output2 = relay.Tuple([uop_4065,call_4078,])
func_4091 = relay.Function([], output)
mod['func_4091'] = func_4091
mod = relay.transform.InferType()(mod)
output = func_4091()
func_4092 = relay.Function([], output)
mutated_mod['func_4092'] = func_4092
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1398_call = mod.get_global_var('func_1398')
func_1399_call = mutated_mod.get_global_var('func_1399')
call_4142 = relay.TupleGetItem(func_1398_call(), 1)
call_4143 = relay.TupleGetItem(func_1399_call(), 1)
output = call_4142
output2 = call_4143
func_4146 = relay.Function([], output)
mod['func_4146'] = func_4146
mod = relay.transform.InferType()(mod)
output = func_4146()
func_4147 = relay.Function([], output)
mutated_mod['func_4147'] = func_4147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3211_call = mod.get_global_var('func_3211')
func_3213_call = mutated_mod.get_global_var('func_3213')
call_4176 = relay.TupleGetItem(func_3211_call(), 1)
call_4177 = relay.TupleGetItem(func_3213_call(), 1)
uop_4191 = relay.log10(call_4176.astype('float32')) # shape=(5, 11, 4)
uop_4193 = relay.log10(call_4177.astype('float32')) # shape=(5, 11, 4)
output = relay.Tuple([uop_4191,])
output2 = relay.Tuple([uop_4193,])
func_4208 = relay.Function([], output)
mod['func_4208'] = func_4208
mod = relay.transform.InferType()(mod)
mutated_mod['func_4208'] = func_4208
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mutated_mod.get_global_var('func_4208')
call_4209 = func_4208_call()
output = call_4209
func_4210 = relay.Function([], output)
mutated_mod['func_4210'] = func_4210
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4283 = relay.var("var_4283", dtype = "float64", shape = (8, 6, 13))#candidate|4283|(8, 6, 13)|var|float64
uop_4284 = relay.sqrt(var_4283.astype('float64')) # shape=(8, 6, 13)
func_884_call = mod.get_global_var('func_884')
func_887_call = mutated_mod.get_global_var('func_887')
var_4288 = relay.var("var_4288", dtype = "float64", shape = (196,))#candidate|4288|(196,)|var|float64
call_4287 = func_884_call(relay.reshape(var_4288.astype('float64'), [7, 4, 7]), relay.reshape(var_4288.astype('float64'), [7, 4, 7]), )
call_4289 = func_884_call(relay.reshape(var_4288.astype('float64'), [7, 4, 7]), relay.reshape(var_4288.astype('float64'), [7, 4, 7]), )
var_4292 = relay.var("var_4292", dtype = "float64", shape = (7, 4, 7))#candidate|4292|(7, 4, 7)|var|float64
bop_4293 = relay.less_equal(call_4287.astype('bool'), relay.reshape(var_4292.astype('bool'), relay.shape_of(call_4287))) # shape=(7, 4, 7)
bop_4296 = relay.less_equal(call_4289.astype('bool'), relay.reshape(var_4292.astype('bool'), relay.shape_of(call_4289))) # shape=(7, 4, 7)
uop_4308 = relay.tan(var_4283.astype('float64')) # shape=(8, 6, 13)
uop_4313 = relay.atanh(call_4287.astype('float64')) # shape=(7, 4, 7)
uop_4315 = relay.atanh(call_4289.astype('float64')) # shape=(7, 4, 7)
func_791_call = mod.get_global_var('func_791')
func_793_call = mutated_mod.get_global_var('func_793')
var_4336 = relay.var("var_4336", dtype = "float64", shape = (220,))#candidate|4336|(220,)|var|float64
call_4335 = func_791_call(relay.reshape(var_4336.astype('float64'), [5, 11, 4]))
call_4337 = func_791_call(relay.reshape(var_4336.astype('float64'), [5, 11, 4]))
output = relay.Tuple([uop_4284,var_4288,bop_4293,uop_4308,uop_4313,call_4335,var_4336,])
output2 = relay.Tuple([uop_4284,var_4288,bop_4296,uop_4308,uop_4315,call_4337,var_4336,])
func_4339 = relay.Function([var_4283,var_4288,var_4292,var_4336,], output)
mod['func_4339'] = func_4339
mod = relay.transform.InferType()(mod)
var_4340 = relay.var("var_4340", dtype = "float64", shape = (8, 6, 13))#candidate|4340|(8, 6, 13)|var|float64
var_4341 = relay.var("var_4341", dtype = "float64", shape = (196,))#candidate|4341|(196,)|var|float64
var_4342 = relay.var("var_4342", dtype = "float64", shape = (7, 4, 7))#candidate|4342|(7, 4, 7)|var|float64
var_4343 = relay.var("var_4343", dtype = "float64", shape = (220,))#candidate|4343|(220,)|var|float64
output = func_4339(var_4340,var_4341,var_4342,var_4343,)
func_4344 = relay.Function([var_4340,var_4341,var_4342,var_4343,], output)
mutated_mod['func_4344'] = func_4344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1344_call = mod.get_global_var('func_1344')
func_1346_call = mutated_mod.get_global_var('func_1346')
call_4368 = relay.TupleGetItem(func_1344_call(), 0)
call_4369 = relay.TupleGetItem(func_1346_call(), 0)
func_2728_call = mod.get_global_var('func_2728')
func_2731_call = mutated_mod.get_global_var('func_2731')
const_4373 = relay.const(4, dtype = "int32")#candidate|4373|()|const|int32
const_4374 = relay.const([-6.214004,-6.729117,-9.723107,3.034095,4.925365,-6.361289,-0.481542,5.466863,-7.431604,-1.057791,-0.725925,1.490979,-4.045309,6.628132,8.051082,5.277606,3.982450,-6.011433,-4.975827,8.387314,5.692749,-5.571810,3.952346,-0.313611,-8.882208,-3.925232,-4.385580,0.368127,8.240565,-5.032782,4.789798,-0.439540,6.565846,-2.176552,2.023787,2.510002,1.028648,-9.731580,-5.994217,-6.395494,2.279058,5.455984,2.285717,5.214085,9.800235,2.205574,1.823336,1.850415,-9.464242,5.613827,-4.895984,-4.324143,-2.295362,-8.376342,0.747873,9.588741,-1.585674,-6.723296,-8.525322,-4.981254,-6.068054,-1.809458,2.686386,-6.832081,8.863702,2.842945,1.211754,2.226900,9.655359,-6.446626,0.366247,4.520839,-9.040834,8.883176,5.773863,-6.582058,3.594747,-0.231374,7.237368,1.460468,-1.732565,-3.617395,-3.777944,0.772495,2.928669,1.395862,6.097204,-0.800130,-3.451435,-3.654785,4.954656,2.766029,7.312809,-1.175882,5.570602,7.623596,-2.662156,7.916524,-8.378647,-1.026780,-2.948183,-9.910642,4.951848,9.818083,-5.300623,9.738404,-1.048442,-5.932051,-5.236487,-1.366586,-9.761203,5.235949,2.525456,-5.721800,9.983918,-6.340975,-8.031358,-2.450903,3.523596,3.911107,8.878621,-7.073795,-8.126907,-5.889668,9.528953,-9.281649,-5.003954,-3.849150,-9.570465,6.460641,-6.445593,2.652841,-5.508922,-7.512787,4.961164,8.476317,-5.785800,-7.027282,1.969798,-5.881514,-6.109791,-3.512334,-9.299555,-8.570959,8.065131,5.624043,2.254391,-1.978653,-1.790312,-6.470634,9.475718,-4.318479,5.021439,-4.909398,9.418102,8.357230,0.365408,4.113660,-5.681853,-9.603450,1.312793,1.648093,-6.282432,2.503716,-8.139123,-6.973624,6.264081,-7.214476,2.254645,5.856897,6.546440,-7.534990,9.435737,-1.418946,-3.361868,0.233271,-4.263939,-5.238999,7.774159,9.483757,9.734177,1.616575,9.906144,1.404313,-7.110090,6.315960,2.593624,-4.592955,3.894559,3.436764,6.469219,-8.778257,2.224883,-3.494418,-5.973284,5.609768,0.032159,-6.509149,-3.458012,5.979267,8.742114,-5.264363,6.342427,2.860608,0.419338,-4.024454,5.862234,9.704738,6.980056,5.414525,3.236725,-2.728953,3.464556,1.362022,-0.106004,-7.318175,-3.542908,6.050983,6.432287,-3.395490,7.357168,6.779082,8.805949,3.603101,-1.016717,-5.722313,0.307828,-3.360624,-6.771131,-9.982495,1.159150,-6.205116,5.879857,5.599516,-7.251168,-1.263753,-9.203526,-8.598281,-6.007539,-5.468761,0.461601,-0.034916,4.452308,1.652899,2.264035,2.776019,4.467987,-3.391141,4.792507,2.062214,6.857862,1.062961,-8.952566,-8.262844,1.376845,2.586341,3.231468,-3.524172,2.422492,-0.643006,3.372766,4.001960,4.927946,-4.655032,1.486369,-4.473351,0.985035,-2.050797,-3.789710,-8.676595,5.250903,-0.742398,3.918927,-3.195595,-7.735695,5.518601,-9.357598,-3.583451,-9.677833,-6.017564,9.917524,8.646175,-9.682754,-1.314875,-7.334974,-3.583485,-3.622580,-2.628013,0.327459,-9.964719,-8.518393,-2.819021,-7.411680,-1.913515,7.898374,-4.395752,-1.017181,7.394673,6.858704,6.558020,-2.628162,-7.994579,-9.367933,-3.065158,8.031403,5.418343,2.132645,-7.945431,2.862465,-3.333294,3.494475,2.023078,-8.777835,-4.736225,-5.742185,4.871212,2.074701,7.387796,0.700853,-7.119215,4.710203,-3.134877,4.048837,-0.810676,3.934890,2.025377,-3.602515,-3.495247,2.777653,-6.559928,-9.269423,-0.297952,3.297941,4.900703,5.630172,5.908090,-8.941411,3.087017,-0.984581,-5.845201,9.447596,-7.143834,-7.810835,-8.587253,1.054424,3.333373,5.824923,-0.559575,9.527362,7.309796,9.077645,1.122743,-0.117830,4.272402,2.761695,-8.929925,0.239323,-7.610396,-9.779073,9.184784,0.697082,7.353318,-6.393953,-9.920045,-0.910161,-7.660209,-1.306225,5.974323,1.521216,-7.260434,-2.567349,3.280776,5.125155,6.228123,-2.402241,-6.372775,8.621149,-7.218005,8.600182,1.932671,-7.268532,1.746387,-8.740427,3.295533,5.570770,-4.601697,3.493869,0.577899,9.218890,-2.512202,5.304944,9.198862,-7.127201,-1.933196,-5.925342,7.348611,2.047073,-6.261670,6.285037,0.144574,2.276080,-9.776186,9.822745,2.589430,-5.580937,1.076695,-2.995176,-8.303069,-2.065172,-4.574500,9.925035,-4.114555,-9.889189,-5.931642,-4.287680,-6.825798,0.273121,-2.874672,-4.535856,5.431568,7.571873,-4.705777,9.968372,1.200302,3.876209,9.027326,4.306654,-4.638687,-3.203474,-2.037968,-1.711572,-7.470577,5.887938,3.669184,-5.550109,3.514280,4.239242,-7.771938,-9.399358,-5.893884,5.146680,-6.942730,0.008036,0.068600,8.834414,7.528242,-0.269530,9.948496,-8.939071,-7.706422,7.235685,8.449393,2.349515,-1.615990,6.881666,-0.658839,-5.104671,2.464235,2.719754,9.061047,-4.206302,-2.602346,-9.122402,1.025134,-1.443463,6.810873,0.627971,-3.127672,-4.033826,-7.876126,-2.449273,5.252871,-1.793629,-0.130544,6.362105,-0.214802,-1.795887,-8.072583,7.804511,-3.078429,1.057309,2.808961,-0.689469,-3.549632,-9.481397,-7.176848,2.432616,4.587107,-6.789779,5.212323,4.240005,-3.174585,-1.758475,-4.152124,-3.352425,-5.175529,4.101898,-6.783259,0.584731,-0.283485,3.232916,-9.969897,-0.229309,-5.786522,-0.769968,-5.630758,-4.695331,7.113559,-8.328050,-1.003384,-6.773381,-7.098058,-6.954783,4.580325,1.127337,-6.267950,-9.082564,1.202180,-1.411045,-5.167028,5.667147,6.666733,8.735274,6.516973,-0.171384,-2.070841,-1.018586,-4.089402,7.186831,-9.137846,-5.186578,6.760583,-3.617067,6.908037,6.218845,0.495931,3.178727,-1.608258,3.420122,-4.809399,6.161630,4.639523,2.018863,-5.471874,3.429551,-4.217213,4.159464,4.746938,-5.200076,2.890276,-5.166644,2.937967,0.386452,-8.659474,0.413208,-7.608325,9.077190,-7.838360,-6.977576,6.832452,9.313258,1.247594,3.703387,-4.650489,0.942467,9.430363,-4.395027,5.507639,-3.002355,6.510366,-8.787013,-6.197587,5.712404,5.320547,-5.198543,9.114211,-5.130564,-1.687316,1.888115,4.605425,-4.339315,-4.448159,5.131091,-5.880710,5.297337,3.588251,-6.217815,4.726520,-2.050970,0.075564,4.342329,5.611379,2.158192,-5.720058,-5.312151,9.746290,-8.354024,-8.244727,-6.102082,-6.093828,-1.786949,5.421839,0.016654,-0.506423,7.943465,-9.227711,-0.280772,-6.417685,-4.529929,0.517198,8.991905,5.597248,-0.940087,5.050537,5.806026,2.402620,-4.454177,-3.459356,8.508725,6.102952,-8.945792,-7.237691,5.559136,-4.074085,3.663865,6.606486,-8.043094,-7.148639,-0.732836,5.056090,5.595024,7.573403,-7.678854,-2.169907,-2.650736,-0.817813,6.102616,7.961747,-7.622037,-0.533254,1.363452,-1.531116,1.228584,8.489333,-4.774509,6.982969,8.210998,6.871360,-0.916932,8.365149,-5.150260,9.529199,-4.156600,-8.979300,-4.026893,-8.339637,-8.600214,1.235403,-1.788337,0.215745,-8.707361,-5.690988,2.606753,1.001293,2.679380,-1.690706,-7.491977,-4.004701,2.440594,8.667589,9.836980,2.769953,-3.307569,9.359973,9.419065,-7.349454,9.051684,5.578576,-7.835224,-2.405365,-1.648252,1.595777,-0.448933,0.509584,3.873292,2.117374,6.686921,-8.322223,-6.221786,-5.881651,6.701460,3.721200,7.393626,5.463809,2.263630,-8.375954,6.237715,-1.351535,9.665305,9.899038,4.153804,4.394312,8.343339,-8.259406,-2.048318,-2.816587,0.632279,-4.578023,-7.425783,1.621709,-7.511999,3.919896,1.663698,2.415836,-8.304930,3.642641,-8.659100,-1.101706,0.954557,4.771322,7.157975,0.899525,0.136010,7.287168,7.708329,9.400042,-3.501166,0.559838,-9.014289,-8.165474,1.396043,-7.045956,8.737907,-0.148518,-6.301184,-9.724338,5.481725,-5.090326,0.390903,-3.841056,-0.333887,-0.299428,0.418430,0.156017,8.384418,-4.727490,9.546383,-4.336864,1.255489,4.465125,-9.280213,5.559581,1.485778,-7.615699,0.010534,-3.390741,-4.726963,1.486946,-5.464114,7.788093,-4.396896,6.484724,3.971825,-7.864473,-4.194264,-9.172796,6.484936,-8.161965,2.957087,-2.237557,1.629537,2.489237,4.466980,3.186205,1.598727,8.639224,-2.260372,3.898382,-9.892467,-3.033598,-0.594513,1.835882,-6.542961,-6.316624,-3.167472,2.959976,6.884733,3.610896,2.363017,3.173246,-0.922597,-2.447537,2.888878,-4.372157,-4.695783,-5.783784,0.536605,-7.083406,9.305897,6.525001,2.208950,7.850631,4.906912,-6.281933,-2.421131,4.106812,-2.479940,3.449745,-2.373850,-8.264052,5.801437,7.883047,-6.284150,-1.416059,-6.650342,-0.059476,-2.448797,5.026934,-3.728477,-4.476081,6.795421,9.280835,-4.148133,5.928652,-4.003141,1.699838,-2.209369,-8.165262,-4.325060,-4.857526,6.648949,4.070476,-7.860833,4.498217,-1.009322,3.881149,-9.641143,6.921921,-5.006949,4.396711,-1.017379,-6.985839,3.185534,-6.476970,6.680460,-3.366657,0.843186,0.927172,-4.715324,-9.753058,-6.908499,-6.353705,0.078749,2.133345,-0.913423,-8.084016,8.020730,9.420136,-7.260339,1.828093,-3.649149,-3.669880,9.209175,-5.401658,-0.987724,-6.389005,-8.644747,8.717187,-5.793064,0.266486,7.823536,-7.494833,-4.959893,9.226620,6.009841,7.118022,1.158348,0.873842,6.441147,-0.237887,-0.173782,-9.615677,-2.395078,-7.707517,9.477503,0.783301,-9.993161,0.302865,-5.752128,1.338804,5.652233,0.861821,-9.323281,9.669707,-2.926620,8.562618,-1.076139,-9.463416,-9.377597,-1.968075,-1.809167,-4.751957,2.003598,-1.828302,3.528552,3.497685,-5.719164,1.510403,7.756908,-0.144877,-5.540423,-6.362065,3.044182,2.679027,-2.320668,3.832763,-0.840664,4.522738,-6.608114,6.129709,4.585741,-9.855421,6.133994,-5.047057,7.569242,3.157355,-9.219341,-3.232459,-8.300111,5.193190,7.585692,6.830546,3.878211,3.860190,-9.733011,5.379342,9.049825,3.394565,5.271329,4.209910,-1.341368,-6.954168,3.098444,2.050849,7.791277,-8.315160,0.628580,-5.800879,-3.109370,-0.448120,-2.802263,-2.833905,-0.977757,-4.131828,6.017538,-0.720449,-7.004458,-3.595936,2.012935,1.238219,7.015609,-5.405283,-5.197523,4.995033,-5.373598,4.628958,3.333380,0.159277,-9.391839,4.186950,3.052289,1.620971,-1.172288,4.357658,2.195576,-4.374498,-2.575595,-8.561595,9.715300,0.599184,2.789716,-0.942325,-8.404731,-0.861334,-4.932950,-6.619758,5.833762,4.383568,-7.188484,-9.850476,-1.037388,-0.296705,1.133723,2.972436,-5.791203,-8.764650,9.477831,-0.382393,-7.337269,-2.483650,-8.642731,2.374647,9.735109,0.950859,0.760611,9.864417,3.349634,2.806986,-3.576471,8.416754,0.943882,9.621457,9.783335,7.825368,-1.890903,-8.350235,-8.405399,5.894452,-3.635944,5.875207,-0.476688,8.040395,-0.470047,-9.738237,4.773312,0.869838,9.505371,-5.363767,-0.338413,5.096505,4.617433,5.518592,5.505933,4.517101,-1.288792,1.782040,-8.887798,-7.128742,4.234291,1.400890,-0.915065,-1.824265,9.357784,-0.485836,-9.926198,2.997835,8.558529,9.750553,7.021625,2.864626,-1.821778,-8.780816,8.771675,4.668038,2.234138,-8.654434,-9.414137,2.496210,1.218849,2.242039,7.552139,4.912628,-6.294186,0.989481,-2.231721,6.195913,-5.566741,5.829024,-9.031376,-1.191077,3.570730,0.116477,7.732656,-1.610620,5.609013,-7.498509,-2.573483,2.814152,5.676153,-6.806423,2.431814,-0.100779,1.539778,-5.723958,-4.635083,1.348304,3.487701,8.062891,9.691964,2.239889,-9.792229,-8.701426,5.208094,0.662372,-6.265620,-7.991510,5.690481,8.419191,-7.717477,-4.987794,3.918445,2.639721,-0.647362,4.481104,-3.071893,-7.367407,0.262422,9.948877,5.764400,8.915638,-9.591119,8.724212,-4.447424,-1.977959,-3.925810,6.809514,-0.579914,-1.194680,-8.656552,-9.933444,-9.978433,0.070082,1.550228,8.299254,3.798590,0.070934,-4.459927,7.357315,7.887408,-3.103157,-9.246637,4.661276,-4.212237,0.444695,-6.817948,8.362339,0.494140,-2.326681,0.476336,8.089100,-7.552502,-8.312044,4.870894,6.742825,6.362137,3.192074,1.629947,-2.603515,-1.817548,-2.281216,5.657393,-3.964552,-6.499694,-3.546284,-4.808505,-2.978916,-0.648069,5.913261,-8.374544,-8.208600,-1.390720,6.447709,2.905933,4.713457,-4.308489,-9.912502,1.059342,-8.957810,7.145766,1.981355,-5.703693,-4.304606,-7.917372,-2.514594,-2.185887,-2.887826,-4.444598,-1.453998,0.150522,-9.207693,-3.275170,-8.840471,4.153499,5.447268,9.554886,-3.511469,3.608886,-4.413082,-6.992963,-3.151154,7.385158,-2.697957,6.125750,6.606800,-6.698539,-0.762901,-9.630159,3.470117,7.716981,-7.557561,9.722580,-4.033659,6.181021,5.387179,0.716614,-4.909492,-9.895762,9.913143,-9.510000,0.802509,-8.758474,2.847821,-4.278954,-8.614646,9.146436,-5.858055,8.156736,6.562935,1.862516,-2.807199,2.225621,7.922971,8.901877,8.219043,-8.908754,4.805523,-2.958378,3.438639,6.272185,-1.225341,9.361048,9.506019,2.558227,8.453405,1.089233,1.617095,8.940674,6.958672,5.917341,-8.591640,6.176741,-1.497122,-5.086695,-5.676799,9.884169,-2.760800,6.861138,1.903822,3.136038,4.417383,8.806381,8.753011,3.872010,1.414556,6.702824,-7.312390,4.593352,-4.576663,5.560420,6.535359,3.759681,4.777519,-6.423264,8.620812,6.214864,-6.774995,6.305485,6.364137,-1.723800,-5.218335,-4.729296,-4.770851,0.614747,6.180691,6.479383,-0.711241,3.864261,6.717861,-9.155346,8.120874,3.715073,-0.649375,2.020309,-5.603754,7.303383,6.995153,8.492643,2.043146,-3.165274,6.507994,-4.322420,-9.765654,1.532051,1.757371,-8.570880,-2.028264,-1.021047,-7.110172,-7.087420,-7.621393,6.113459,-8.198128,9.906993,-2.475389,-0.337096,-7.011763,8.882379,-8.905631,-7.982202,-9.598470,-2.395447,4.664810,-6.219928,-9.134817,-2.834858,-9.569183,-5.919695,-9.461442,-9.970627,4.766159,2.625050,9.894602,-6.599622,1.748359,0.194646,9.743263,-7.306677,1.695355,5.469344,-2.034784,-5.729800,3.985391,8.544288,-0.753364,-2.173413,-3.327713,5.748420,-9.137347,-9.846339,2.906139,-4.579505,1.499224,8.738889,8.502922,2.712038,-3.467452,-2.242173,-1.875492,6.870571,6.815477,2.155350,4.032498,-0.280508,-3.377304,-5.480199,-7.150612,0.502547,0.368223,-4.407259,9.151920,-5.993163,5.228837,1.989845,-5.086753,0.748974,7.696460,-0.987196,5.919624,-2.051085,2.119552,2.982591,4.815717,5.274544,2.640124,7.043154,0.029132,-8.735624,-3.224269,5.147962,8.248652,9.969860,9.103571,0.119322,-5.550879,-3.661555,-8.772192,2.477107,-4.951322,5.502825,9.089200,-8.691780,-3.837246,0.364319,2.301954,-5.723938,0.420206,4.640577,5.309667,-1.535079,-0.891149,4.088988,-8.740946,0.778780,6.668411,2.414600,2.829217,-0.848920,-7.299946,1.072397,-0.008306,-8.484345,9.139952,-6.107566,7.325096,-4.506225,3.078730,-0.212124,-5.864226,6.391660,-3.961456,-1.669745,-5.056536,-4.723087,9.275383,-6.081203,7.589995,8.112300,-7.276822,5.908155,-6.200812,-1.700728,3.664312,-0.708499,-5.479010,0.204919,-4.152833,-1.559923,-9.287442,9.620575,-8.168502,8.682496,8.096669,-0.456918,-1.158290,5.842121,0.016388,7.847543,-4.074511,5.401899,4.207735,-3.397349,-9.296209,-1.403899,0.622072,-6.891386,-3.576032,2.134382,5.114215,7.039658,6.309400,-8.098362,-9.477645,8.231312,6.677759,0.134358,1.971140,-3.920763,5.735613,1.837850,3.337089,-8.891524,8.958399,8.634147,-7.453412,1.474502,9.874126,-8.031796,0.563642,-8.093625,-1.760614,1.101962,9.548416,-2.573906,-8.844317,7.227515,7.746846,6.881408,2.904442,8.508930,-2.621376,9.816951,6.442789,8.419962,4.183186,7.266520,-7.028861,-6.114301,5.682379,-9.520334,-6.109590,0.938735,8.909159,-9.765526,8.486905,-7.588676,-7.081794,4.105469,-4.488937,-8.234196,-9.056888,8.003732,-0.763140,5.150418,-0.865497,-4.645462,5.683660,6.633972,-2.189467,-9.065209,9.390812,5.988015,-5.803772,2.088753,-0.545344,8.752022,-4.506203,0.936306,-3.957296,-2.883151,-6.514197,5.465753,-3.377690,-2.450803,-4.836457,-7.873339,-0.166393,-2.260705,-1.282442,7.793031,8.957278,8.709740,1.428583,5.735268,2.846504,1.768547,-4.203528,-6.222968,4.511617,2.127191,9.911147,1.841166,-6.421853,-3.263161,-0.343775,4.019018,-2.244341,7.180458,9.928285,3.632833,-9.223312,-7.508806,6.546603,9.979188,5.559482,5.071019,-5.957223,-6.217532,-3.062425,6.230041,-0.091448,-7.915728,2.041712,2.607132,-2.216075,-8.837381,7.487999,0.338634,6.182186,7.140782,-5.529529,3.378352,1.055068,9.644740,-3.561064,-7.824703,1.576595,-5.037011,-2.962161,7.114463,-1.745763,9.826888,-1.246861,5.239441,1.886704,-0.513087,6.415708,-5.225070,-1.242056,-0.883051,-5.929797,4.019333,4.628562,3.149809,8.982961,5.228636,-0.439238,7.594765,0.734790,-1.901421,3.332574,-0.421687,-3.992933,-3.906618,-6.864519,9.371367,9.486884,-6.403948,-4.188103,7.663465,-0.844507,-5.089730,7.570810,8.496324,-0.309420,-5.854133,6.968836,-2.486147,6.930791,-6.092120,2.345597,1.583921,-8.678699,2.292021,2.544823,7.380450,5.724767,-4.037130,4.922557,-9.469403,9.739969,-3.061245,8.469119,-5.512843,6.996926,3.394248,-8.595308,4.932716,-5.563356,-5.038294,9.551110,-6.583375,6.130840,-2.041368,-0.076612,-7.387724,7.171991,-5.075240,6.106566,7.198899,6.957049,4.367851,3.546103,2.371847,3.223938,5.935165,1.099424,-4.544926,-0.680322,1.811843,3.630371,-3.146976,-2.769205,4.466734,5.313262,-0.823827,7.623618,2.775488,9.640646,7.142942,-6.801349,6.106958,-3.512954,-5.618753,-6.657505,2.514352,0.856366,-5.634554,1.150233,9.124866,9.590023,6.784316,4.012272,2.947358,8.522835,9.418684,-0.361641,7.312009,-4.074736,1.691833,-0.023640,-5.410018,7.759357,5.940421,3.036896,9.346470,4.129200,5.271760,1.012351,1.488673,9.377494,-2.437310,2.854916,-2.045370,1.866123,3.872204,2.199040,3.657698,-7.328796,6.405873,8.388911,-8.535837,6.605818,5.776580,2.228427,-8.073896,-2.271995,-7.364197,-7.410293,8.554859,-2.995532,9.100196,1.298039,-2.232968,-6.809885,9.121369,2.356220,-3.544897,2.620462,2.691964,-5.469240,-7.301081,8.319304,-0.137291,2.412182,0.292052,-6.392672,6.024424,-0.972844,-2.998074,2.640677,-3.986698,9.644437,-8.346465,5.156652,3.208894,2.759579,-9.002476,-5.379441,-8.503202,-2.183623,-0.790484,0.573015,-4.481735,4.445120,-1.475520,-9.050495,4.000649,6.685028,3.686416,-6.087550,-6.415989,-4.497149,-7.031239,1.834403,-3.470348,-4.199428,5.508921,3.737514,5.059938,-5.713115,3.191272,4.005567,-6.118843,-0.956701,0.151457,1.318665,-5.962226,-6.342578,-0.152622,-3.700413,7.589759,9.214415,-0.103707,6.346003,-0.776420,4.954990,-9.104632,-3.812134,4.794324,-0.262659,3.013584,-4.422284,7.217297,-9.908951,-0.580045,9.370270,-0.128549,-5.776258,7.547597,-7.978671,9.796564,1.089308,-8.172971,8.931095,9.396480,-5.312379,0.873328,-5.099633,8.418200,-9.970666,9.048863,-0.486171,2.460218,-0.949337,-0.686693,-2.182157,-2.932354,9.344380,4.031321,-4.294954,6.601588,-3.692302,4.084331,5.090570,2.521607,5.728649,2.537371,-5.929946,-0.757346,7.840559,-4.449706,7.236956,-1.785616,6.875852,3.870911,-4.033381,0.755038,1.740999,2.601685,0.395311,-5.659367,-1.085933,-8.366613,-1.156238,5.961029,7.561410,1.404855,7.503854,-1.449797,-9.601963,-3.115548,-1.674613,5.948310,0.575889,-5.892003,3.293147,4.104859,0.663955,1.897978,-6.683880,8.314965,-3.367386,-0.102718,-9.151151,-0.995038,-6.724973,1.694638,-6.583490,-5.681648,-8.050872,1.177473,-0.654689,1.910431,-5.746695,1.762443,6.477425,1.944713,-4.857562,1.258980,-0.241661,8.631670,8.802014,6.995796,5.749262,4.128082,-8.225457,8.103009,9.984527,-8.884553,2.803646,-4.666430,6.449679,-6.564063,-7.500339,-8.725625,-2.389200,8.396309,9.969236,1.689848,9.011239,-9.082142,2.763528,-3.993440,-2.835757,8.660174,-1.634961,-4.069460,6.656525,9.805499,7.952648,-3.852096,2.591370,6.915823,-7.772532,2.105730,4.389736,0.119628,-5.469665,3.612564,7.386113,-2.767482,-9.390323,8.395669,-5.837182,9.807294,-3.498765,6.391910,-6.674839,-5.799230,6.615970,-8.661440,3.813709,-7.411351,9.553647,-7.513956,-5.952564,-7.540580,-7.591297,-6.624439,0.274845,-1.708717,9.805227,3.641124,-1.876776,-5.403214,-1.889355,-4.768251,-1.376110,1.188316,-2.962486,-5.285873,-2.397116,6.274335,-9.416934,4.907166,-0.312314,-6.848562,4.767518,0.890235,7.797426,-6.188869,-9.706297,-0.948330,0.106826,-9.681742,6.791975,-4.420694,8.702343,-2.997610,3.374659,2.404860,5.601016,0.076792,-8.886763,-9.499784,-2.533222,5.935594,0.354458,5.692012,1.425608,-4.118760,1.983056,-0.319615,9.120923,-2.957617,3.272088,-5.666502,8.465978,8.554735,-5.863753,-1.011531,-3.304122,1.385224,3.001796,-4.817861,-8.934858,2.964921,6.337990,-3.938181,5.520583,3.464913,8.108755,3.789745,4.693607,-7.558981,0.077512,-2.332647,-8.970069,7.008939,6.236415,-7.810803,7.581104,8.476386,6.963135,5.924702,-7.463275,8.205745,-2.539936,4.989680,-3.517034,6.697533,-5.358093,2.870407,7.313267,-9.303210,0.094625,-8.682723,-0.169796,1.547074,9.840665,-4.247148,-0.886121,1.908229,7.006295,-3.041526,-1.178729,2.537697,-9.793117,8.504988,0.503602,-0.448703,-7.909418,5.351837,-6.848737,9.458714,4.410002,5.154795,7.080305,-2.021685,0.759774,-5.372964,-7.379379,-8.715358,6.166238,-3.377970,5.037229,2.653528,3.989886,7.760765,8.669670,-8.912895,-9.825093,-7.775014,-7.554819,-2.722442,-3.242212,-6.474857,-2.816885,3.464326,-0.045765,6.645337,-3.661092,-5.225049,0.447401,5.356357,-1.321471,-4.056477,0.715573,-0.332456,5.724336,-4.702117,-4.208324,5.713790,8.376796,-5.866885,-6.663905,-0.265408,-2.321140,2.336916,-5.495610,-6.474025,-3.318188,0.186841,-6.516763,4.059523,5.753626,9.166675,-9.525059,-2.869531,8.335551,-1.673212,-8.152215,-4.403164,6.087366,3.997603,-0.738038,-0.177061,-7.829710,-7.384178,0.252741,-4.275184,1.147701,-9.808798,-7.805439,-8.749107,0.981322,-0.580688,4.774182,-5.531512,-5.565745,-7.075328,-6.498338,0.707602,-5.958555,5.776935,4.023597,-7.518101,4.707263,4.499966,-0.711745,1.561132,-5.586258,9.516087,-9.973627,-2.596176], dtype = "float32")#candidate|4374|(2145,)|const|float32
call_4372 = relay.TupleGetItem(func_2728_call(relay.reshape(const_4373.astype('int32'), []), relay.reshape(const_4374.astype('float32'), [2145,]), ), 1)
call_4375 = relay.TupleGetItem(func_2731_call(relay.reshape(const_4373.astype('int32'), []), relay.reshape(const_4374.astype('float32'), [2145,]), ), 1)
func_3993_call = mod.get_global_var('func_3993')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_4378 = func_3993_call()
call_4379 = func_3993_call()
func_1846_call = mod.get_global_var('func_1846')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_4417 = relay.TupleGetItem(func_1846_call(), 0)
call_4418 = relay.TupleGetItem(func_1848_call(), 0)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_4432 = func_1072_call()
call_4433 = func_1072_call()
output = relay.Tuple([call_4368,call_4372,const_4373,const_4374,call_4378,call_4417,call_4432,])
output2 = relay.Tuple([call_4369,call_4375,const_4373,const_4374,call_4379,call_4418,call_4433,])
func_4434 = relay.Function([], output)
mod['func_4434'] = func_4434
mod = relay.transform.InferType()(mod)
mutated_mod['func_4434'] = func_4434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4434_call = mutated_mod.get_global_var('func_4434')
call_4435 = func_4434_call()
output = call_4435
func_4436 = relay.Function([], output)
mutated_mod['func_4436'] = func_4436
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_4451 = func_2294_call()
call_4452 = func_2294_call()
func_1001_call = mod.get_global_var('func_1001')
func_1005_call = mutated_mod.get_global_var('func_1005')
const_4456 = relay.const([[-6.765658],[-2.517562],[-9.746637],[5.252055],[-3.662866],[1.923184],[-0.090557],[7.139506],[-6.950646],[-3.833464],[-2.721382],[-1.446135],[-6.924404],[0.446926],[-7.376091],[8.580923],[-6.975020],[-4.441373],[5.975324],[5.540913],[-3.055498],[1.367944],[9.308717],[-7.260327],[-8.440759],[7.772350],[-0.373328],[9.918670],[2.376212],[8.059116],[-6.529883],[5.881784],[-2.066922],[-4.385384],[4.174448],[5.572326],[-0.802874],[-7.192550],[8.007114],[1.984683],[9.761982],[-0.490593],[-9.719316],[7.214290],[-7.056931],[9.459375],[3.156286],[-4.873399],[-6.549802],[2.282143],[-9.251970],[-3.385719],[3.473348],[-9.803393],[5.401264],[-0.652801],[1.217970],[-6.279302],[-9.098211],[1.099798],[5.674098],[-5.696991],[6.110197],[-4.756043],[5.152058],[-5.117789],[3.768319],[-9.227428],[9.693177],[1.498618],[-8.046385],[-2.059956],[6.350626],[0.944268],[-9.045560],[-8.970556],[-4.064335],[-2.172375],[9.706927],[9.708996],[-6.020311],[-7.141482],[-6.039766],[-2.052856],[-4.628530],[2.898081],[5.197193],[-1.726539],[-5.012300],[3.563974],[-2.012080],[-4.239099],[-3.569707],[4.137603],[-3.306073],[-5.859053],[-5.144257],[-0.029914],[6.391634],[-8.406811],[-9.524871],[-5.651062],[0.908980],[-6.422812],[-7.455287],[-6.201646],[-5.447237],[6.393999],[9.752739],[-9.270050],[-2.262767],[-3.242847],[-7.071201],[5.832239],[8.474863],[7.209685],[4.376256],[-5.977044],[-6.714673],[1.343435],[-9.157757],[2.775467],[-0.783241],[6.633819],[7.545922],[7.555035],[-4.918840],[-7.276797],[-6.206826],[-0.171251],[-8.742303],[-8.018291],[6.187783],[-8.270080],[1.600479],[-3.172677],[-6.769942],[-7.856598],[7.483222],[-9.704401],[-5.112430],[-3.230605],[-4.276975],[5.881273],[-2.845739],[-7.331417],[9.169927],[4.018792],[8.910603],[-4.279076],[0.287771],[-2.501977],[-6.676484],[-6.042178],[-4.640971],[9.461276],[1.566607],[1.994807],[-5.416388],[-6.653650],[-6.780769],[2.318580],[1.305510],[-1.176062],[2.494800],[-6.895530],[-8.773350],[-7.210221],[5.507521],[-5.679293],[7.223328],[-6.287061],[3.816768],[-1.363962],[-5.480155],[-3.328813],[-6.868663],[-3.304194],[-1.208785],[-9.129530],[2.911196],[-7.479184],[-2.407698],[3.958885],[-6.007251],[6.340402],[5.843170],[-5.516040],[-1.193536],[-2.833619],[8.223665],[3.352111],[5.838950],[-3.146961],[4.333899],[4.403376],[7.929064],[-0.215258],[-6.173559],[1.098880],[2.056758],[-0.216920],[6.718653],[8.540137],[-7.202427],[-1.361981],[-7.917842],[2.759012],[-4.597726],[-5.574570],[-5.453224],[-7.067352],[0.171105],[8.289934],[-2.026246],[-2.706810],[-2.840777],[-9.393816],[0.850263],[8.315542],[-4.667755],[-5.807923],[2.172942],[-4.422379],[7.350046],[9.715900],[-9.641396],[4.686056],[-8.870822],[2.319239],[2.766251],[-7.854300],[-2.223198],[8.661644],[-3.623354],[1.180895],[3.231557],[-2.722570],[3.900228],[-8.808262],[0.526703],[0.064521],[3.443473],[0.231366],[0.830415],[5.809670],[4.590106],[-5.708562],[-4.003145],[1.892520],[-5.315149],[8.202969],[-6.928045],[3.979580],[-4.859860],[-5.516451],[2.880689],[7.490790],[-1.138498],[5.120601],[7.852672],[7.815117],[-3.970695],[3.006217],[7.764331],[-5.650557],[7.558723],[3.069542],[4.149188],[-9.104423],[-6.382973],[9.205969],[-4.443623],[4.558279],[6.809780],[-0.979885],[1.690657],[9.816927],[-3.635732],[-3.018126],[-2.479093],[8.887872],[1.891315],[9.883087],[4.205120],[-7.662137],[8.786531],[-1.990799],[0.958307],[-2.256357],[-8.578560],[2.117540],[-0.121268],[0.058280],[4.532720],[2.153176],[-4.446300],[-5.882860],[3.131535],[-8.839363],[0.491364],[8.701850],[-7.516067],[-0.263423],[0.918670],[7.211149],[2.860862],[3.651859],[8.944304],[-0.098682],[-9.161935],[-9.371893],[5.566364],[-2.125960],[0.545704],[8.691166],[-1.247094],[6.150670],[-5.350061],[-6.355966],[-4.055540],[3.510744],[-4.404922],[-8.460450],[-0.176242],[0.007389],[-0.666294],[6.762712],[-0.117782],[-0.171794],[6.938319],[-4.637035],[-8.498887],[-9.482047],[4.122423],[-0.496516],[-6.331072],[1.476941],[-8.565332],[7.516566],[0.949014],[-9.603597],[-0.704217],[6.425518],[4.994902],[-4.801740],[2.423695],[-1.458967],[-7.866496],[7.796159],[9.132001],[-4.548616],[3.265282],[8.377800],[0.391820],[-2.274423],[2.149116],[-0.596651],[7.958376],[-4.409681],[3.256514],[9.910274],[4.229754],[7.070827],[-0.285661],[7.467566],[-8.432700],[-4.624720],[0.056228],[-8.262864],[-0.922765],[4.530700],[2.391249],[9.773461],[1.609254],[6.393838],[0.080633],[-4.372778],[1.203359],[-1.312865],[-6.271658],[7.918581],[8.597247],[-7.939755],[0.608782],[2.719369],[-1.798188],[5.142945],[-2.907797],[-7.684961],[-3.488596],[2.389862],[-0.489334],[-2.820297],[4.449749],[3.401630],[-0.893196],[-2.305454],[-6.758267],[7.545075],[2.403722],[4.478351],[2.052049],[9.800767],[-3.951963],[-8.957336],[-2.571824],[-8.101565],[7.281658],[-0.679476],[5.834542],[-1.670161],[-3.853238],[-6.204352],[9.798696],[8.010609],[-5.172228],[-9.422285],[5.953121],[-2.290090],[1.325495],[4.799025],[-9.977003],[-5.012296],[-8.595760],[-3.734429],[0.137200],[-2.288334],[2.859577],[-3.227151],[-6.868928],[-4.253738],[9.957662],[-8.288934],[-8.473864],[-8.327494],[0.256432],[3.582604],[4.323512],[1.614523],[-3.951608],[4.545946],[-7.204265],[-3.453632],[-0.747337],[7.242459],[-9.475396],[-2.274370],[-7.805163],[-2.808709],[0.260503],[7.283057],[-4.411035],[-1.035328],[-4.496094],[-3.679445],[4.219030],[-5.374936],[2.508758],[0.924309],[-7.329410],[-5.324897],[-1.510872],[-2.780959],[5.472334],[-9.885733],[4.685767],[-7.290301],[-0.995437],[9.318583],[-1.786486],[-9.245281],[8.970467],[-0.896213],[5.114324],[6.169800],[-2.993518],[-3.374811],[-9.998654],[6.121800],[6.007125],[-8.837499],[5.898236],[2.115954],[3.625283],[9.763738],[-4.855039],[8.719427],[-7.527975],[-9.561261],[0.495097],[6.113785],[9.363016],[3.767469],[-0.693028],[3.918280],[-7.769293],[-0.665352],[-5.346258],[0.767026],[-4.471615],[-8.261566],[-9.979064],[2.692225],[3.824471],[-7.321249],[1.198708],[-8.704736],[2.793389],[-6.039801],[-0.595057],[-9.765028],[8.299618],[4.198896],[-4.001256],[9.696208],[5.697979],[3.467877],[8.765070],[-9.470622],[-8.407075],[5.134722],[0.169417],[-7.322057],[4.076064],[-2.566024],[-2.657531],[-1.343135],[-8.120543],[-8.522700],[2.876821],[1.767550],[0.352636],[-7.723559],[1.781833],[5.201742],[-0.199280],[2.775283],[-9.703386],[-0.466788],[-6.344130],[9.770963],[6.781329],[-8.476322],[8.427569],[-2.619236],[-6.030643],[0.475949],[-0.106166],[-6.179179],[5.339778],[9.132857],[6.952728],[7.263779],[-2.633909],[6.952811],[-9.087606],[-0.245196],[9.194111],[9.535883],[9.065108],[7.779446],[-4.545519],[3.066985],[-1.962598],[-0.964091],[7.002576],[9.286528],[4.878743],[-9.349474],[7.044129],[-1.052033],[-6.191114],[5.188969],[-6.221555],[8.667312],[5.006468],[2.422706],[8.173555],[-9.032324],[6.482655],[4.668624],[5.261921],[4.337827],[1.829538],[-3.369773],[5.386805],[8.114118],[9.097803],[2.849622],[8.966907],[2.404735],[4.710977],[-9.106466],[6.448976],[0.805370],[-7.952973],[8.318277],[3.443764],[-8.012925],[-7.977787],[9.992545],[0.948352],[-5.812463],[-2.697488],[-6.238259],[-8.183454],[-1.416376],[2.299053],[-6.239954],[2.997276],[0.156950],[8.560460],[9.216858],[9.959074],[9.157066],[2.514761],[5.368218],[8.790032],[9.598616],[-1.806018],[-2.915340],[-4.196862],[-8.135220],[5.383754],[-5.594811],[-3.469506],[-1.400039],[1.581996],[5.672079],[5.668030],[-0.173609],[3.621801],[-2.361195],[5.784132],[-2.586921],[8.340564],[-0.760261],[5.884195],[6.455255],[-7.529623],[-6.135414],[7.305224],[-7.039179],[-2.041873],[9.902511],[-3.562251],[-6.200436],[-6.009091],[7.792398],[5.084953],[6.054274],[-4.206512],[-1.450369],[-7.889324],[-8.764232],[7.483614],[-6.606930],[-0.846392],[2.172803],[-7.083869],[-0.245891],[8.392187],[-1.535360],[2.035706],[0.617981],[-6.294497],[-0.419152],[5.525402],[-9.310270],[-6.178111],[-6.698629],[5.100200],[1.050089],[7.633846],[8.975417],[8.630036],[-4.776201],[-7.402578],[-7.334821],[-8.632287],[-1.137548],[-4.107505],[7.990914],[8.912699],[-4.565717],[5.800323],[-7.978189],[4.872563],[-5.812902],[-8.276767],[-6.297394],[8.757714],[-6.831558],[5.863356],[-6.285472],[4.777033],[-1.718433],[0.368124],[2.342019],[-0.530827],[-2.015674],[-5.095452],[-0.436170],[-6.431196],[-0.919242],[-2.041162],[0.004228],[0.467732],[-8.953888],[-8.624198],[6.935181],[4.250281],[-9.658098],[4.922765],[-9.504812],[6.595176],[2.457148],[5.160525],[1.977044],[-5.900882],[-3.942456],[-7.323490],[0.489581],[-5.561294],[-1.764339],[-8.430812],[-8.277442],[-2.738554],[-2.072812],[-5.333857],[9.213402],[7.273507],[2.838628],[-4.686108],[2.713433],[-0.958470],[-9.869015],[5.170758],[-0.945099],[1.264734],[-6.164507],[-0.907548],[6.670718],[4.533621],[5.433495],[-0.367404],[7.468516],[8.273420],[-4.805013],[1.023642],[9.984843],[-4.229931],[-7.440124],[0.400817],[9.237969],[-7.294516],[-2.458072],[-4.420181],[4.992722],[8.241521],[9.886877],[3.697751],[3.606330],[2.170612],[-9.925039],[4.584944],[-5.839597],[3.311837],[0.121624],[4.426035],[6.923521],[3.259775],[4.194040],[-9.259179],[8.749738],[1.307555],[2.306485],[-4.772015],[3.190571],[9.716858],[-9.423285],[6.410651],[-8.578835],[-9.588862],[4.981315],[-9.785838],[3.373851],[-2.538455],[4.328180],[9.859734],[-4.500132],[8.915026],[3.371352],[2.656320],[0.409137],[-9.560677],[6.825822],[-4.259644],[7.701135],[-1.140807],[-1.014823],[4.973865],[-7.417949],[-5.591457],[-0.411391],[-2.559249],[-7.355736],[5.750690],[4.336911],[0.135531],[9.178379],[2.974022],[7.233202],[-6.439893],[-0.980216],[-0.481988],[6.873571],[-1.856061],[6.984850],[5.192282],[-7.539160],[5.716154],[3.133406],[-7.569130],[6.317601],[3.886140],[5.739035],[8.175315],[-2.044327],[6.107373],[-2.289177],[8.913334],[-5.667268],[5.857690],[1.291840],[3.163052],[3.544316],[-7.213924],[6.165685],[0.404962],[-0.693155],[0.474420],[9.198541],[8.879902],[-5.897945],[-0.545132],[-7.652098],[-2.736300],[3.766268],[-9.620828],[-8.462305],[-1.389361],[-5.535591],[-2.669880],[7.386718],[-7.992721],[-4.059348],[-4.997413],[0.488123],[0.515805],[-0.939494],[-1.230399],[-2.323263],[1.073882],[6.241014],[-0.665719],[-3.500944],[7.137853],[6.302221],[-1.264878],[5.323776],[5.513153],[6.183719],[-0.378830],[3.165515],[-3.594943],[7.117822],[-7.364107],[-5.022570],[-6.643756],[5.797420],[2.297474],[5.454563],[2.860520],[0.755008],[-5.425433],[-1.926334],[-6.962435],[0.987374],[-3.243273],[5.377410],[-5.188916],[-3.455219],[-2.489288],[8.074703],[-1.275266],[5.738326],[-9.612598],[-9.422258],[8.556845],[6.250875],[-9.961367],[5.815900],[7.572771],[2.300823],[2.643311],[9.853267],[-2.247460],[-4.488662],[-9.479710],[3.693150],[1.987095],[-9.338057],[6.525186],[8.676312],[-3.906213],[-7.747610],[-9.698843],[-1.994805],[-1.390009],[-1.624882],[-7.953036],[-9.520746],[7.574444],[6.390925],[-4.416996],[-7.575563],[6.732310],[2.341506],[7.982436],[7.982053],[6.486852],[-7.197072],[-1.365021],[-2.751371],[2.905343],[-2.199848],[-8.898630],[-0.167527],[-9.374247],[3.644109],[-2.627989],[-3.660828],[-7.669910],[-1.434214],[-0.019188],[-6.260950],[-9.823242],[3.104850],[8.857112],[6.660436],[-4.775013],[-3.054650],[-9.144786],[-5.438691],[-1.878979],[4.846532],[3.809037],[-9.243063],[6.339518],[9.132162],[-8.361476],[-5.147554],[0.625643],[6.730465],[2.984353],[4.769861],[4.457493],[-1.871954],[-1.850248],[-6.512735],[-4.301616],[0.360310],[4.791499],[7.421185],[-9.753761],[-2.122541],[-5.482402],[1.256422],[-7.253585],[-3.356445],[-2.059447],[-4.841074],[9.134468],[7.180440],[8.954217],[-9.569287],[-7.112736],[-5.069896],[8.754934],[-0.447041],[-2.699215],[1.273500],[5.292967],[-7.320309],[8.683849],[0.161842],[-4.247868],[7.176499],[-4.884701],[7.697605],[-8.922457],[3.749381],[8.890098],[-2.550767],[-8.899700],[8.899858],[7.791278],[7.049248],[2.453582],[3.601410],[3.470065],[-6.493953],[-4.695336],[7.451667],[3.123212],[-0.990285],[7.235892],[-6.402943],[9.987356],[7.255372],[5.010386],[4.912866],[5.558565],[-6.611843],[-6.450841],[-7.201032],[-0.806699],[-8.748359],[-6.532357],[-0.674352],[-5.920612],[-3.536885],[-7.071482],[2.019549],[1.165014],[2.946929],[4.222103],[-6.472814],[-9.859988],[7.411991],[-5.593901],[-8.894641],[1.510694],[9.692979],[-1.253593],[7.614490],[-7.715981],[-4.516657],[-6.325939],[8.914555],[0.354674],[-5.328514],[8.927861],[3.188594],[3.016061],[-2.973996],[-4.874560],[6.192977],[2.665646],[-9.643878],[-6.806782],[1.534802],[0.142349],[0.955157],[2.044481],[4.882588],[-2.194216],[9.365385],[-6.494294],[5.567722],[7.606404],[9.683314],[-6.873527],[0.112997],[4.433228],[0.033119],[4.966792],[1.942939],[3.062023],[-0.702653],[6.942574],[7.536265],[-3.949455],[3.412479],[9.280162],[-2.658722],[-4.011244],[1.247964],[-1.711699],[9.707645],[-0.611195],[4.200102],[2.598020],[-4.925496],[-5.406386],[7.663404],[-1.321429],[1.511527],[5.930226],[-6.507114],[4.068019],[3.617471],[-9.732026],[-1.645323],[-8.954639],[1.797986],[-1.647559],[-2.842523],[7.283897],[-0.002242],[-1.571826],[2.818647],[-4.995588],[9.034062],[2.290851],[6.810520],[-2.598931],[-8.173501],[6.667839],[-7.926217],[-0.995496],[-0.381830],[-3.367459],[-2.094389],[9.355144],[8.054405],[-2.247247],[-0.423311],[9.265207],[-5.281103],[9.731804],[7.526938],[6.527710],[9.754453],[-3.496198],[-6.005807],[8.362509],[-5.599547],[1.328530],[9.468135],[2.442178],[-6.308699],[2.987758],[6.625607],[-4.005021],[9.297367],[4.460011],[-0.529218],[-4.286950],[1.826957],[0.486161],[-1.289390],[-1.708239],[-1.202590],[9.376384],[-2.135002],[8.399286],[1.065706],[4.952493],[3.478547],[-4.015057],[-0.174764],[-4.865134],[-7.605470],[-6.746921],[6.286203],[0.157345],[-9.796091],[-1.253355],[-8.182346],[-6.064308],[2.672314],[1.943295],[-5.943819],[4.446889],[0.239832],[-5.360705],[3.511842],[-4.906469],[9.492169],[6.488758],[-2.905520],[-5.757872],[-7.821875],[0.853615],[4.353840],[6.122558],[7.674670],[1.103886],[8.330522],[-7.136500],[-6.039363],[-1.135380],[1.116096],[-1.732510],[4.717973],[1.966551],[-6.435125],[-2.892911],[3.376408],[2.695031],[1.558660],[2.313956],[-6.479507],[-0.714066],[1.151475],[-6.149325],[7.403595],[9.818793],[6.960105],[-8.541339],[4.903824],[-8.765233],[7.394059],[-4.368674],[-8.542310],[3.011319],[-3.866851],[8.273594],[8.975028],[-4.021130],[-3.920080],[6.307274],[-5.215180],[-0.173785],[-5.274544],[-6.576129],[-9.010426],[7.051765],[-3.444569],[-7.101663],[-3.024714],[-6.910478],[-4.880717],[3.217116],[-0.837693],[-7.647997],[-9.655934],[-7.886503],[-9.599832],[-0.318054],[9.788485],[-8.591094],[8.333604],[-8.362911],[4.200761],[-8.065223],[-8.139368],[-2.974442],[-3.491220],[8.797973],[-1.432601],[9.447938],[5.179592],[7.806859],[-3.246532],[-2.184887],[-9.556020],[-2.159575],[-3.493485],[9.975171],[1.388125],[8.425727],[4.028074],[2.463532],[5.248481],[-3.673150],[-1.308010],[-6.062098],[8.681570],[-3.539280],[7.386460],[-1.115954],[0.015557],[0.345558],[9.058917],[-1.167974],[0.391475],[-0.181510],[8.328821],[-5.144108],[-9.866147],[-9.608560],[0.121532],[-9.725006],[-5.985754],[-2.418143],[6.512957],[-5.524774],[7.416283],[5.763572],[-2.022206],[-1.442038],[6.986704],[-8.792148],[-2.758653],[-1.935722],[5.837905],[4.974404],[3.403343],[-4.219137],[-9.600457],[-5.132604],[5.854736],[9.915957],[-0.306631],[2.352907],[-2.995665],[-6.596406],[-7.523180],[-6.915775],[-8.962145],[-4.679130],[-6.459432],[-1.519917],[7.174821],[2.136530],[3.833934],[-4.892926],[-5.387173],[-9.829727],[-2.715283],[-4.773922],[4.245506],[-7.273571],[3.354809],[-7.328616],[8.275425],[-2.551756],[-9.023617],[-8.963040],[6.359136],[-2.455827],[2.630995],[2.125929],[-2.751909],[-5.339343],[3.202529],[6.754880],[-3.085518],[-8.716228],[-6.530750],[8.355997],[3.295726],[8.344628],[-2.888098],[-5.005788],[-5.015911],[-6.853610],[7.440547],[7.359665],[4.048355],[-3.688509],[-8.985922],[2.933679],[3.753718],[4.364281],[-0.312370],[-8.215845],[-1.407693],[-3.022893],[4.394073],[-2.937874],[1.497707],[3.242167],[-5.282624],[-6.175205],[-8.726133],[-6.733230],[-4.806393],[0.630603],[1.011910],[1.682286],[6.810678],[-5.515796],[-0.335783],[-1.507995],[5.068556],[2.280249],[-8.804314],[2.386649],[6.776560],[-0.129762],[-9.872682],[5.686502],[7.654325],[-6.836216],[3.657691],[-1.251524],[8.382967],[-4.501585],[7.626199],[4.139827],[5.048825],[1.099389],[8.063319],[-1.666374],[-3.311115],[7.091665],[4.116061],[8.586206],[2.950451],[1.337983],[-9.986834],[-2.864997],[-9.458317],[0.932009],[0.293845],[-6.291303],[4.011575],[-4.211562],[-0.848751],[4.886880],[-8.282843],[6.529583],[6.997622],[-6.560530],[4.493302],[3.974220],[0.409805],[6.133276],[-2.006487],[-4.079036],[-5.929295],[-7.595343],[-7.293945],[-9.103303],[0.405535],[-0.244889],[-9.132162],[7.986827],[-2.177333],[9.259976],[-4.848493],[8.917750],[-0.949015],[7.602518],[7.504207],[-7.085948],[6.697163],[7.989572],[-9.052641],[-6.721996],[-8.207996],[6.548494],[3.350977],[-5.747374],[-6.330618],[5.295463],[9.843772],[-7.404055],[0.947264],[-8.872841],[8.876108],[-9.937557],[-6.613791],[6.400240],[-8.628876],[-5.306509],[-2.674024],[8.159984],[5.880557],[8.947451],[7.083738],[-8.734111],[-8.968924],[-6.504068],[-4.058324],[-4.024326],[-6.622961],[-8.086752],[3.719932],[9.138103],[-6.959477],[-6.870229],[8.508702],[-4.566748],[5.075722],[-1.147578],[-8.378367],[8.650087],[1.986016],[-2.581097],[6.412669],[-3.785201],[-0.779474],[-9.532540],[-4.008639],[8.068259],[9.409620],[4.655026],[8.943906],[4.055945],[5.930359],[-0.160721],[-0.058092],[-1.373735],[1.835027],[-1.779179],[-3.359944],[-8.009469],[6.280322],[-3.787770],[-7.079134],[-9.707256],[3.602823],[-7.688574],[4.326036],[5.717035],[4.651476],[-1.807795],[-3.497779],[-5.625727],[-8.744845],[-9.140145],[5.510181],[9.616451],[1.200772],[-9.803265],[8.067282],[7.398805],[-5.587921],[8.553072],[-2.538738],[-9.852546],[-4.531073],[8.897837],[-1.786193],[3.984521],[-3.290934],[5.706500],[-9.481831],[1.881303],[-3.842489],[-1.681229],[-7.226519],[-9.513941],[5.331892],[0.336207],[-1.605133],[-6.514480],[-5.697496],[5.881837],[2.203660],[9.387909],[-0.990409],[3.140921],[4.303510],[-7.947325],[-5.815260],[6.738109],[4.888904],[6.791703],[-5.180789],[-5.359474],[-9.873162],[4.799731],[-9.463745],[5.936898],[5.858540],[-5.288210],[9.428509],[0.422263],[-9.859144],[-1.056316],[-0.819664],[9.955702],[9.305767],[-2.942303],[3.427995],[7.763834],[8.887779],[3.747484],[0.446996],[0.527256],[3.721603],[7.556913],[4.414477],[-7.154185],[-5.758052],[-5.612560],[-5.726207],[-6.521071],[-8.253408],[1.926113],[6.874308],[-5.332644],[-9.172196],[1.532782],[-9.535305],[-9.955495],[-4.492653],[1.385005],[-8.643907],[7.407781],[-2.024972],[0.843836],[8.617347],[6.026742],[5.389682],[-3.282892],[4.369565],[7.785368],[-8.890506],[9.943145],[-2.530488],[-1.112092],[3.663510],[-5.871822],[8.151308],[7.087688],[-8.503422],[4.858658],[-1.399641],[4.348405],[3.325380],[3.055229],[-7.240563],[-6.806001],[4.141348],[-3.507163],[-8.107822],[-7.796982],[-1.119633],[3.779089],[-7.219435],[8.894270],[-8.123491],[-1.908823],[3.179624],[-6.441592],[3.211967],[9.583519],[-7.558774],[-9.437946],[-7.162933],[9.979675],[-1.543336],[-2.465834],[2.351648],[-4.658923],[-5.762910],[-7.252636],[-9.695134],[-0.066431],[-0.689488],[6.032455],[-7.436478],[-8.972097],[-5.265224],[-3.229036],[7.168247],[1.051405],[1.188354],[-7.190829],[-1.572538],[-1.410274],[-6.692074],[9.284626],[0.160115],[9.098026],[-3.557050],[-6.264468],[9.952267],[5.200724],[0.073866],[-5.973553],[-0.717100],[-6.331665],[-2.299527],[-2.192176],[-6.171619],[2.671750],[3.065511],[9.460905],[-2.856336],[-6.727058],[1.193059],[0.505088],[0.178452],[7.029495],[-4.972560],[7.863359],[1.629282],[-3.738062],[-7.821242],[-0.216480],[4.866990],[-0.466930],[-2.105041],[-7.446867],[-9.724931],[4.390918],[1.258533],[-2.623932],[-6.168665],[7.799959],[-6.573920],[7.107810],[3.019795],[4.303224],[-5.684034],[-8.324155],[8.071570],[-5.115096],[-7.039966],[0.754446],[6.628958],[5.365587],[1.022629],[-4.991438],[2.159120],[3.872688],[-1.662015],[2.301780],[-3.125496],[-5.894263],[6.483020],[5.239073],[2.223738],[-5.580600],[-7.067056],[-2.964554],[8.044582],[-2.145339],[0.293257],[-5.196564],[-3.674729],[-2.858903],[-4.787411],[-9.162839],[-4.502270],[9.139853],[3.775751],[3.514919],[-6.682533],[5.414088],[0.906169],[-9.646891],[4.831691],[8.600511],[4.215452],[1.794607],[3.051240],[1.264790],[5.991416],[6.932221],[-8.769234],[0.119707],[8.350708],[-4.728606],[0.529444],[-3.525601],[0.926073],[3.411209],[6.665877],[2.511504],[-2.939292],[-9.360460],[9.993235],[0.915751],[-2.670386],[-4.006524],[4.069409],[-8.696464],[-9.710206],[-8.010671],[-8.150988],[-2.238010],[2.515037],[-1.725978],[5.906934],[-4.051256],[-9.571458],[2.335840],[-7.697564],[7.581344],[4.089244],[0.846475],[8.275536],[9.750739],[-2.024087],[0.864739],[-5.855248],[-7.799143],[8.697384],[-0.606046],[-1.568166],[-9.964406],[-2.292234],[-8.321017],[-0.984932],[9.165073],[-7.000186],[-2.351374],[-7.637351],[0.820569],[8.360405],[-4.288927],[8.018306],[-1.938070],[5.769096],[3.075866],[3.404452],[8.029801],[6.363497],[-6.462703],[9.999480],[-0.147913],[-1.547588],[1.246651],[-5.052876],[3.778416],[-6.568259],[-2.090446],[-4.788266],[-9.992501],[5.268634],[1.380195],[-2.384199],[-4.213307],[9.017517],[7.048281],[-7.925325],[-5.989074],[0.210651],[-4.304237],[-3.801947],[4.111988],[7.256895],[-4.725694],[-9.559643],[2.350282],[-6.079212],[-4.938817],[3.029744],[7.189759],[9.155534],[2.159073],[-4.529637],[-2.804382],[-0.359832],[9.759428],[-9.721382],[9.387542],[-4.118599],[6.335730],[-1.102011],[7.932128],[-4.689035],[1.303955],[-4.428945],[-4.511519],[-1.305354],[-3.299813],[4.996562],[-2.612060],[4.337797],[-2.631752],[-4.051247],[1.823177],[-6.941126],[-5.767847],[7.346626],[4.135293],[4.709703],[-9.301268],[8.990946],[-4.220048],[-7.974372],[-0.675807],[8.648396],[4.277144],[6.523834],[8.009579],[9.287021],[-1.394570],[8.662165],[5.083272],[-3.908082],[-9.967181],[1.565917],[-4.094417],[8.170464],[-4.849520],[2.567366],[9.710539],[8.320752],[3.244902],[2.524478],[5.047672],[8.978083],[-8.239646],[-7.612190],[2.088619],[-2.501883],[-6.631801],[-9.183808],[4.206053],[1.879002],[-5.491481],[-9.719681],[-5.275262],[-6.779067],[-4.660538],[-8.488449],[8.945376],[-1.498657],[-0.784795],[5.476746],[2.317467],[-0.913019],[2.752345],[-7.471584],[-0.058929],[7.166066],[-5.679512],[4.971286],[0.685265],[-5.284603],[6.912001],[6.841722],[-4.352433],[-3.170190],[-7.562050],[9.204969],[2.526960],[-6.597700],[-8.427313],[5.481405],[-8.481342],[4.401822],[3.354747],[3.480722],[3.516231],[-2.898191],[-1.331281],[1.961780],[8.082498],[-1.556828],[3.372794],[-1.467095],[0.296304],[1.527351],[7.311448],[-7.029365],[4.643261],[6.170747],[-7.679413],[-9.390244],[-0.951600],[-3.631579],[-3.770533],[-7.804561],[7.678132],[-2.635991],[-6.168726],[-0.350938],[5.308654],[8.640255],[-6.898998],[-4.529119],[-2.743168],[-0.874623],[0.828565],[-5.064220],[-0.205709],[-7.188169],[-4.044815],[-2.244517],[5.685483],[-2.670865],[3.383584],[9.365884],[-1.618651],[-6.847815],[6.662931],[2.295212],[-2.632747],[-7.511593],[-9.468967],[5.422947],[-2.500654],[3.315464],[-7.023188],[-4.364611],[-8.138612],[3.261020],[4.514640],[-4.248625],[-3.368733],[0.251988],[-1.467369],[9.786403],[-5.903103],[-3.843146],[-8.874902],[5.144754],[9.207211],[8.150437],[7.022345],[-6.617294],[-2.554862],[6.159122],[-1.706639],[0.444840],[-7.612862],[-9.792759],[5.377401],[9.345857],[-7.700721],[-5.604775],[-0.438072],[7.915529],[8.915690],[1.159938],[-7.314488],[-0.347965],[-7.828249],[6.525665],[-0.152235],[8.168944],[5.192584],[2.530788],[0.255498],[-9.649279],[-0.534483],[-1.389437],[7.946922],[-1.735633],[-8.391860],[3.710962],[4.580678],[2.637976],[1.265167],[9.400778],[9.129322],[8.469218],[-2.292601],[-3.584128],[1.589687],[5.881868],[9.351178],[-8.867225],[3.560917],[1.542381],[7.090736],[7.791347],[4.120882],[-8.350118],[0.298458],[-0.984217],[-8.618657],[7.769823],[-6.315129],[-6.824050],[-9.827853],[1.419440],[9.766960],[-3.933589],[-2.013367],[-9.611746],[-3.543842],[9.788485],[-8.605838],[9.419705],[4.977381],[-9.984462],[4.172490],[-4.068376],[2.581945],[4.871249],[6.926264],[-1.403546],[8.719339],[5.689345],[-4.403690],[5.981488],[0.042780],[-7.636754],[-6.329023],[2.456011],[8.864745],[3.553404],[3.189543],[-5.364911],[-9.095542],[1.161521],[-8.642389],[-6.977114],[-5.927765],[-5.296935],[0.237721],[-2.448370],[-6.795965],[-6.964889],[-6.775568],[-0.785583],[3.092957],[-4.629992],[4.667050],[-9.452570],[-8.578574],[8.297143],[6.486164],[-3.935048],[-5.193651],[-1.390642],[-4.387920],[-9.712977],[-4.861430],[1.256118],[3.011401],[-2.844086],[9.472232],[7.062195],[-4.195849],[-0.529140],[4.474020],[0.668583],[0.026141],[0.921176],[-7.262997],[6.182834],[-3.523434],[5.619459],[-0.125458],[4.954142],[-9.902411],[9.761386],[-6.604679],[6.463166],[-4.467944],[4.871169],[4.062537],[-0.771073],[5.035064],[-6.914332],[5.865967],[-6.496867],[-6.351570],[-7.699669],[1.102299]], dtype = "float32")#candidate|4456|(2145, 1)|const|float32
call_4455 = relay.TupleGetItem(func_1001_call(relay.reshape(const_4456.astype('float32'), [11, 13, 15]), relay.reshape(const_4456.astype('float32'), [11, 13, 15]), ), 0)
call_4457 = relay.TupleGetItem(func_1005_call(relay.reshape(const_4456.astype('float32'), [11, 13, 15]), relay.reshape(const_4456.astype('float32'), [11, 13, 15]), ), 0)
output = relay.Tuple([call_4451,call_4455,const_4456,])
output2 = relay.Tuple([call_4452,call_4457,const_4456,])
func_4458 = relay.Function([], output)
mod['func_4458'] = func_4458
mod = relay.transform.InferType()(mod)
mutated_mod['func_4458'] = func_4458
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4458_call = mutated_mod.get_global_var('func_4458')
call_4459 = func_4458_call()
output = call_4459
func_4460 = relay.Function([], output)
mutated_mod['func_4460'] = func_4460
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3008_call = mod.get_global_var('func_3008')
func_3009_call = mutated_mod.get_global_var('func_3009')
call_4511 = relay.TupleGetItem(func_3008_call(), 0)
call_4512 = relay.TupleGetItem(func_3009_call(), 0)
func_3993_call = mod.get_global_var('func_3993')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_4517 = func_3993_call()
call_4518 = func_3993_call()
func_3806_call = mod.get_global_var('func_3806')
func_3807_call = mutated_mod.get_global_var('func_3807')
call_4523 = relay.TupleGetItem(func_3806_call(), 0)
call_4524 = relay.TupleGetItem(func_3807_call(), 0)
func_1719_call = mod.get_global_var('func_1719')
func_1720_call = mutated_mod.get_global_var('func_1720')
call_4528 = relay.TupleGetItem(func_1719_call(), 1)
call_4529 = relay.TupleGetItem(func_1720_call(), 1)
output = relay.Tuple([call_4511,call_4517,call_4523,call_4528,])
output2 = relay.Tuple([call_4512,call_4518,call_4524,call_4529,])
func_4533 = relay.Function([], output)
mod['func_4533'] = func_4533
mod = relay.transform.InferType()(mod)
output = func_4533()
func_4534 = relay.Function([], output)
mutated_mod['func_4534'] = func_4534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2832_call = mod.get_global_var('func_2832')
func_2834_call = mutated_mod.get_global_var('func_2834')
call_4535 = relay.TupleGetItem(func_2832_call(), 0)
call_4536 = relay.TupleGetItem(func_2834_call(), 0)
output = relay.Tuple([call_4535,])
output2 = relay.Tuple([call_4536,])
func_4537 = relay.Function([], output)
mod['func_4537'] = func_4537
mod = relay.transform.InferType()(mod)
mutated_mod['func_4537'] = func_4537
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4537_call = mutated_mod.get_global_var('func_4537')
call_4538 = func_4537_call()
output = call_4538
func_4539 = relay.Function([], output)
mutated_mod['func_4539'] = func_4539
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4569 = relay.var("var_4569", dtype = "int8", shape = (1, 2, 14))#candidate|4569|(1, 2, 14)|var|int8
var_4570 = relay.var("var_4570", dtype = "int8", shape = (15, 2, 14))#candidate|4570|(15, 2, 14)|var|int8
bop_4571 = relay.maximum(var_4569.astype('int8'), var_4570.astype('int8')) # shape=(15, 2, 14)
output = bop_4571
output2 = bop_4571
func_4586 = relay.Function([var_4569,var_4570,], output)
mod['func_4586'] = func_4586
mod = relay.transform.InferType()(mod)
var_4587 = relay.var("var_4587", dtype = "int8", shape = (1, 2, 14))#candidate|4587|(1, 2, 14)|var|int8
var_4588 = relay.var("var_4588", dtype = "int8", shape = (15, 2, 14))#candidate|4588|(15, 2, 14)|var|int8
output = func_4586(var_4587,var_4588,)
func_4589 = relay.Function([var_4587,var_4588,], output)
mutated_mod['func_4589'] = func_4589
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4605 = relay.var("var_4605", dtype = "int64", shape = (13, 11, 5))#candidate|4605|(13, 11, 5)|var|int64
const_4606 = relay.const([[[10,5,9,4,7],[5,1,3,8,-6],[4,2,7,2,-3],[-6,-6,-8,-3,10],[-2,-3,4,7,-10],[6,9,1,-1,-8],[10,9,6,-1,-10],[10,8,6,-9,-4],[8,-10,8,-4,6],[5,-9,2,-4,4],[-5,-5,-8,-5,-6]],[[6,8,4,9,7],[2,-3,-8,6,-9],[-5,5,-9,1,-9],[-4,-2,3,10,-5],[-9,-1,-10,7,-3],[4,-5,8,-3,-10],[5,-7,6,-4,-2],[-7,6,3,-9,1],[9,7,-6,7,-3],[2,-1,-8,1,-5],[-1,-5,-2,-4,-9]],[[10,2,-9,4,8],[3,7,2,-10,7],[7,-2,6,9,3],[-7,-5,2,-7,-1],[4,-8,-7,6,3],[-7,-1,1,10,-9],[7,8,5,5,8],[9,-10,-5,-5,-6],[-4,9,1,3,9],[8,6,-7,8,2],[-9,-10,-10,-8,5]],[[5,9,3,1,5],[5,-5,7,-1,5],[-3,-8,5,-7,3],[9,1,10,-9,-9],[-3,6,-7,-2,-2],[-6,3,-7,10,-1],[5,-10,9,-10,3],[3,-6,-3,-3,-3],[-2,-9,3,-5,-7],[-7,-8,1,-7,6],[-10,5,7,1,3]],[[-5,5,1,-8,-2],[-7,-1,5,4,1],[-3,8,-1,6,-5],[7,5,3,-9,-4],[-10,-1,-8,1,10],[2,6,-3,-3,8],[7,9,7,-8,5],[-9,-3,-3,7,-2],[9,10,2,-2,-2],[6,-8,-3,-6,-3],[-3,3,-3,8,4]],[[6,-4,9,-10,4],[5,-3,-2,6,-7],[9,1,7,-10,-3],[7,-10,-6,8,1],[-9,-1,-9,-1,2],[-4,-8,-3,-9,2],[-1,-1,-9,-9,-2],[10,-9,6,-5,-3],[-6,8,-3,1,-5],[-6,-3,5,-4,8],[9,9,-8,-5,5]],[[7,-8,5,5,-5],[-10,-7,10,4,8],[-1,-1,-4,9,-1],[-9,4,-5,-9,7],[-1,7,-10,1,2],[-6,-8,-5,-6,-2],[-9,-5,-6,-5,1],[9,9,-1,4,2],[3,8,5,-4,10],[-5,-6,-3,3,7],[10,-7,5,-9,-1]],[[-2,-7,8,4,2],[-7,-2,-9,5,-4],[5,2,4,-9,-4],[-4,-7,-7,-2,8],[-4,2,9,-2,3],[-9,-10,10,10,-9],[-10,-3,3,-3,-2],[10,7,1,-5,-10],[-8,7,-2,6,-8],[8,-7,6,-10,4],[1,9,7,-4,2]],[[-1,7,-10,6,-2],[-10,-2,-1,6,9],[-5,-5,-8,4,-5],[10,-9,-5,-5,-7],[-7,7,-4,10,-10],[-10,-9,9,7,3],[-10,-9,9,1,9],[3,5,-7,-6,8],[8,-1,3,6,3],[-4,-4,3,-7,9],[2,-1,-10,5,7]],[[-4,-9,2,4,2],[9,10,8,-7,8],[10,6,9,2,-3],[-5,-6,9,8,7],[-9,-5,10,-4,10],[-2,4,-4,3,-4],[6,1,-6,9,-4],[-4,-3,-3,4,-9],[-1,-5,-9,7,4],[8,5,-2,-10,4],[7,10,-1,-2,-2]],[[9,10,-8,2,10],[-9,10,8,4,4],[3,-8,-1,7,3],[-2,3,-6,-10,-8],[-8,9,-10,9,4],[-2,5,1,8,-7],[1,5,3,7,-2],[6,-2,8,-1,-4],[2,-3,7,-3,5],[-7,-3,-10,-4,2],[2,7,-2,-3,-6]],[[7,4,-5,3,7],[-9,-4,-5,-9,-9],[-6,-8,4,10,2],[-6,-5,8,-3,-7],[-10,-3,1,7,10],[2,9,-10,9,-10],[-7,-9,-9,2,9],[-2,-8,-1,6,10],[8,-1,1,7,1],[-2,-6,-1,-9,6],[-2,4,5,2,7]],[[-7,-5,1,-10,-7],[-8,9,1,8,3],[-7,4,9,-9,1],[5,1,6,6,-2],[7,4,-3,-8,-5],[7,-7,3,10,-9],[10,-1,-1,-4,-3],[4,6,7,-4,-10],[-5,-1,8,2,-10],[9,2,2,8,-4],[2,-2,5,8,4]]], dtype = "int64")#candidate|4606|(13, 11, 5)|const|int64
bop_4607 = relay.greater_equal(var_4605.astype('bool'), relay.reshape(const_4606.astype('bool'), relay.shape_of(var_4605))) # shape=(13, 11, 5)
output = relay.Tuple([bop_4607,])
output2 = relay.Tuple([bop_4607,])
func_4616 = relay.Function([var_4605,], output)
mod['func_4616'] = func_4616
mod = relay.transform.InferType()(mod)
var_4617 = relay.var("var_4617", dtype = "int64", shape = (13, 11, 5))#candidate|4617|(13, 11, 5)|var|int64
output = func_4616(var_4617)
func_4618 = relay.Function([var_4617], output)
mutated_mod['func_4618'] = func_4618
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4684 = relay.var("var_4684", dtype = "float32", shape = (8, 9, 16))#candidate|4684|(8, 9, 16)|var|float32
var_4685 = relay.var("var_4685", dtype = "float32", shape = (8, 9, 16))#candidate|4685|(8, 9, 16)|var|float32
bop_4686 = relay.equal(var_4684.astype('bool'), relay.reshape(var_4685.astype('bool'), relay.shape_of(var_4684))) # shape=(8, 9, 16)
func_3653_call = mod.get_global_var('func_3653')
func_3655_call = mutated_mod.get_global_var('func_3655')
call_4692 = func_3653_call()
call_4693 = func_3653_call()
func_4339_call = mod.get_global_var('func_4339')
func_4344_call = mutated_mod.get_global_var('func_4344')
const_4697 = relay.const([9.157798,-1.178991,-9.904625,-4.866565,4.886351,7.381402,4.000138,-3.982955,6.865006,6.894159,2.082589,6.242751,-5.290940,-8.579846,-2.611595,-5.310010,3.622834,4.877606,-0.093353,-3.377371,-5.072950,-2.062039,5.419636,-5.346376,3.346571,1.154474,-2.095059,-7.273752,3.030728,-4.029638,-1.013744,7.716925,-4.201880,-5.209386,-3.562586,-9.218361,-6.578310,-1.879947,0.652887,-5.772167,-1.696564,2.390340,-5.195601,-1.517153,-5.305966,-0.751934,4.792499,-6.046763,-8.141462,-8.737304,-6.648921,8.257356,-0.940475,-6.047411,7.023378,-8.705359,-0.170275,-9.291515,1.628267,-7.347314,0.994800,5.175921,-9.984196,-7.131730,-7.605989,1.817962,4.043443,7.444433,0.389275,-3.000172,-6.390179,-5.801947,-2.031223,3.143574,1.767382,-6.799969,-7.979337,1.657900,4.837978,-8.612378,9.921460,-3.392631,-2.608422,-2.402000,4.958692,-1.374041,8.135191,-7.102870,5.494733,-7.043203,1.586967,-7.052294,-9.736751,-6.587794,5.308702,5.767121,7.662737,-5.782670,7.552331,0.034019,0.809365,-2.167219,-5.347119,-5.045019,-9.460132,3.463687,0.956649,-2.161783,0.538261,-0.727884,4.885859,0.277197,3.917204,-7.824483,-7.049859,-9.031199,-1.182389,6.175892,3.449451,-1.552008,-4.036934,-7.166274,0.942593,8.633597,3.999901,-3.579572,4.403866,9.944763,5.791690,4.584044,6.708055,4.475731,-6.309541,3.691474,-0.060019,3.006985,9.663230,5.464184,-0.025489,8.886147,-9.927692,-5.482284,-9.797835,-1.593175,-1.833915,5.218094,5.042623,7.148356,1.041275,-1.181242,-7.662641,-7.512883,6.719265,6.966460,-3.142799,0.115432,-4.023039,-4.161575,-3.842310,-6.973375,-6.774678,-6.866866,-6.174418,4.979291,-6.762793,1.621763,-7.515934,-8.738225,9.099479,9.072902,9.270042,-7.425879,4.303118,-3.182851,-2.488490,-1.296287,-6.504251,-2.746288,-1.165481,5.950900,5.460528,5.410016,-7.871925,9.831669,6.216712,-1.845740,-7.014170,-2.566380,2.760887,4.933239,9.112425,6.211180,-3.956419,-5.817364,9.876236,-1.686916,6.059265,-3.542780,7.369981,4.989921,9.445821,3.021404,1.693572,6.245801,-6.319441,-1.243466,-9.874949,-9.462462,5.518894,0.823364,-7.273278,-3.327707,2.775347,1.146324,-6.641723,-8.891902,-8.725600,5.617189,5.589009,4.073461,7.617675,-7.010545,6.415677,1.169826,5.605011,3.373315,-5.885758,2.058723,2.517101,-4.958432,-8.782910,6.426769,8.637467,-9.332857,3.667931,-6.941391,5.856839,-4.893000,0.593235,5.144117,-4.334350,-3.509348,-6.517071,-8.067050,7.076208,-7.066617,1.929641,-5.183540,-2.600579,-7.943363,-8.380243,6.664513,8.187534,-5.705887,5.511650,6.710183,3.102833,-5.909308,-7.137742,5.190975,7.649004,0.952300,7.905953,5.283184,-8.654479,8.209263,7.113822,-8.623176,-6.423143,2.558649,-8.832105,5.371266,8.385814,-9.332609,-2.855154,6.655774,9.949591,0.659325,-0.081459,-9.094178,-3.025206,-2.283797,-1.815360,-7.318371,6.072603,-8.424553,-3.006015,6.845073,5.925786,3.674971,9.444570,-2.966274,3.356220,9.224622,-8.988997,-6.048525,6.593028,-4.060099,6.844285,-6.510441,4.687620,3.425856,-0.409181,0.720619,-8.297767,-9.062612,1.604423,-8.046997,-0.177686,-0.743314,9.300870,1.730762,9.812118,4.590739,-3.673834,-4.098657,-6.741128,0.840597,-2.514706,3.467055,-8.879222,6.731512,-4.118438,-7.877873,0.023301,6.847758,-4.925833,-2.363669,9.167873,-8.772056,6.372115,8.324201,-7.808661,3.691669,8.629959,9.469952,-6.109961,7.467364,-8.751700,0.850723,-0.939406,3.866551,2.990156,7.091853,2.269652,-7.308074,-3.229123,-9.033807,-4.136026,9.221259,-5.206575,5.279787,5.961833,9.362772,5.213653,-5.420293,-0.374764,-8.968180,2.845792,-1.073953,6.892229,1.776935,-4.769685,1.935746,5.151441,-9.373179,8.734244,-4.583467,-3.879374,3.825286,-5.455655,4.593578,4.425958,-4.328018,4.125844,1.094242,4.415668,-1.487494,-1.750338,8.923413,7.711251,-8.106943,6.165422,5.582992,-4.027686,3.225884,-9.327439,6.408435,-9.449000,-0.392387,-2.798790,4.962275,9.409012,5.404440,7.820552,1.324151,-2.427104,0.021065,3.645165,0.074681,1.784550,-0.671401,-6.596389,7.651357,-0.838391,-9.418461,6.112821,-6.736655,-9.515844,5.052359,-5.336095,-3.924944,-8.460560,3.179849,-8.449196,6.199413,4.276269,-9.965992,-9.333186,4.742197,0.830812,3.102492,5.841553,8.209426,-5.504106,2.074212,-8.459319,7.999998,2.338840,-1.746310,-4.096605,-9.629340,0.708683,4.409391,-8.341529,-8.990457,-7.716577,8.478574,-0.756687,2.003785,8.416370,3.826737,-8.535818,-6.476650,2.852178,-7.613877,-0.972845,-3.353796,1.905239,6.283835,-5.707566,7.528241,-4.552025,-2.571469,-0.913902,5.808844,-5.441823,7.047848,3.796012,-1.688232,-3.322154,-1.974036,4.819049,-7.889062,-7.792366,1.429487,-8.269691,-2.661317,6.683321,8.828485,-2.957917,4.104391,4.604906,-2.302476,-5.071405,-2.943284,1.183264,2.837966,7.080216,8.481777,-1.554181,-1.753135,5.339275,3.339301,3.373931,-7.855523,7.869815,-4.985166,-3.425729,8.177174,2.487493,1.881026,0.855843,-2.210609,5.598430,-4.059144,-0.715769,-2.938049,2.931255,-6.812382,-4.697961,5.210752,-4.836124,-6.549652,-9.860879,1.603970,1.666262,-9.749533,1.955063,5.857012,-5.508424,-8.163365,-7.303886,-1.642287,-4.273024,-9.467623,-8.213596,-0.085485,1.301569,4.992989,1.761118,-4.177262,-3.296547,7.559916,4.840833,-4.214672,-3.911898,-2.517839,9.010957,2.564897,6.343604,-3.523700,2.498183,-6.641154,3.881991,-7.961923,-5.811335,-9.166746,2.122285,-1.925807,-6.130191,-3.135020,-5.453081,-9.580817,7.448324,4.263551,1.969187,-7.379981,8.821020,-1.227485,3.491901,3.742798,6.815660,-6.739374,4.202142,9.986465,9.923762,-6.501379,-0.068390,7.885770,-0.852769,-3.960659,-9.378105,-9.021044,9.439118,-7.342501,4.711598,-0.745821,8.295482,9.891573,3.615532,6.829489,-7.280049,-3.754454,-6.817033,2.640867,8.647085,-4.660995,-7.785676,8.313383,8.224817,-0.699146,7.185907,2.709804,0.676117,1.133377,8.590934,8.641368,-6.056003,-5.646158,0.023925,-6.025197,2.696649,-0.130726,2.446600,9.958061,-6.708491,-6.128462,-1.068058,-0.078005,-9.690588,2.608166,-6.636171,-1.628414,-2.181649,2.530318,-3.725788,-4.789139,2.400448,1.462248,-8.608822,7.805562,5.685544,-3.489874,-7.352087,5.490095,-9.578470,-5.774393,-1.970775,-9.738749,-7.912090,-8.099225,7.623391,-6.800131], dtype = "float64")#candidate|4697|(624,)|const|float64
var_4698 = relay.var("var_4698", dtype = "float64", shape = (196,))#candidate|4698|(196,)|var|float64
call_4696 = relay.TupleGetItem(func_4339_call(relay.reshape(const_4697.astype('float64'), [8, 6, 13]), relay.reshape(var_4698.astype('float64'), [196,]), relay.reshape(var_4698.astype('float64'), [7, 4, 7]), relay.reshape(call_4692.astype('float64'), [220,]), ), 6)
call_4699 = relay.TupleGetItem(func_4344_call(relay.reshape(const_4697.astype('float64'), [8, 6, 13]), relay.reshape(var_4698.astype('float64'), [196,]), relay.reshape(var_4698.astype('float64'), [7, 4, 7]), relay.reshape(call_4692.astype('float64'), [220,]), ), 6)
output = relay.Tuple([bop_4686,call_4692,call_4696,const_4697,var_4698,])
output2 = relay.Tuple([bop_4686,call_4693,call_4699,const_4697,var_4698,])
func_4703 = relay.Function([var_4684,var_4685,var_4698,], output)
mod['func_4703'] = func_4703
mod = relay.transform.InferType()(mod)
var_4704 = relay.var("var_4704", dtype = "float32", shape = (8, 9, 16))#candidate|4704|(8, 9, 16)|var|float32
var_4705 = relay.var("var_4705", dtype = "float32", shape = (8, 9, 16))#candidate|4705|(8, 9, 16)|var|float32
var_4706 = relay.var("var_4706", dtype = "float64", shape = (196,))#candidate|4706|(196,)|var|float64
output = func_4703(var_4704,var_4705,var_4706,)
func_4707 = relay.Function([var_4704,var_4705,var_4706,], output)
mutated_mod['func_4707'] = func_4707
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3745_call = mod.get_global_var('func_3745')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_4735 = relay.TupleGetItem(func_3745_call(), 0)
call_4736 = relay.TupleGetItem(func_3747_call(), 0)
output = call_4735
output2 = call_4736
func_4755 = relay.Function([], output)
mod['func_4755'] = func_4755
mod = relay.transform.InferType()(mod)
output = func_4755()
func_4756 = relay.Function([], output)
mutated_mod['func_4756'] = func_4756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3073_call = mod.get_global_var('func_3073')
func_3075_call = mutated_mod.get_global_var('func_3075')
call_4804 = relay.TupleGetItem(func_3073_call(), 0)
call_4805 = relay.TupleGetItem(func_3075_call(), 0)
func_941_call = mod.get_global_var('func_941')
func_943_call = mutated_mod.get_global_var('func_943')
call_4809 = relay.TupleGetItem(func_941_call(relay.reshape(call_4804.astype('float64'), [5, 11, 4])), 1)
call_4810 = relay.TupleGetItem(func_943_call(relay.reshape(call_4804.astype('float64'), [5, 11, 4])), 1)
func_1255_call = mod.get_global_var('func_1255')
func_1259_call = mutated_mod.get_global_var('func_1259')
var_4815 = relay.var("var_4815", dtype = "int32", shape = ())#candidate|4815|()|var|int32
var_4816 = relay.var("var_4816", dtype = "int32", shape = (48,))#candidate|4816|(48,)|var|int32
call_4814 = relay.TupleGetItem(func_1255_call(relay.reshape(var_4815.astype('int32'), []), relay.reshape(var_4816.astype('int32'), [48,]), ), 2)
call_4817 = relay.TupleGetItem(func_1259_call(relay.reshape(var_4815.astype('int32'), []), relay.reshape(var_4816.astype('int32'), [48,]), ), 2)
output = relay.Tuple([call_4804,call_4809,call_4814,var_4815,var_4816,])
output2 = relay.Tuple([call_4805,call_4810,call_4817,var_4815,var_4816,])
func_4830 = relay.Function([var_4815,var_4816,], output)
mod['func_4830'] = func_4830
mod = relay.transform.InferType()(mod)
mutated_mod['func_4830'] = func_4830
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4830_call = mutated_mod.get_global_var('func_4830')
var_4832 = relay.var("var_4832", dtype = "int32", shape = ())#candidate|4832|()|var|int32
var_4833 = relay.var("var_4833", dtype = "int32", shape = (48,))#candidate|4833|(48,)|var|int32
call_4831 = func_4830_call(var_4832,var_4833,)
output = call_4831
func_4834 = relay.Function([var_4832,var_4833,], output)
mutated_mod['func_4834'] = func_4834
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3340_call = mod.get_global_var('func_3340')
func_3342_call = mutated_mod.get_global_var('func_3342')
call_4841 = func_3340_call()
call_4842 = func_3340_call()
var_4881 = relay.var("var_4881", dtype = "float32", shape = (5, 11, 4))#candidate|4881|(5, 11, 4)|var|float32
bop_4882 = relay.left_shift(call_4841.astype('uint8'), relay.reshape(var_4881.astype('uint8'), relay.shape_of(call_4841))) # shape=(5, 11, 4)
bop_4885 = relay.left_shift(call_4842.astype('uint8'), relay.reshape(var_4881.astype('uint8'), relay.shape_of(call_4842))) # shape=(5, 11, 4)
output = bop_4882
output2 = bop_4885
func_4888 = relay.Function([var_4881,], output)
mod['func_4888'] = func_4888
mod = relay.transform.InferType()(mod)
mutated_mod['func_4888'] = func_4888
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4889 = relay.var("var_4889", dtype = "float32", shape = (5, 11, 4))#candidate|4889|(5, 11, 4)|var|float32
func_4888_call = mutated_mod.get_global_var('func_4888')
call_4890 = func_4888_call(var_4889)
output = call_4890
func_4891 = relay.Function([var_4889], output)
mutated_mod['func_4891'] = func_4891
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_4974 = func_2294_call()
call_4975 = func_2294_call()
output = call_4974
output2 = call_4975
func_5008 = relay.Function([], output)
mod['func_5008'] = func_5008
mod = relay.transform.InferType()(mod)
output = func_5008()
func_5009 = relay.Function([], output)
mutated_mod['func_5009'] = func_5009
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1925_call = mod.get_global_var('func_1925')
func_1927_call = mutated_mod.get_global_var('func_1927')
call_5062 = relay.TupleGetItem(func_1925_call(), 1)
call_5063 = relay.TupleGetItem(func_1927_call(), 1)
var_5064 = relay.var("var_5064", dtype = "uint8", shape = (12, 7, 14))#candidate|5064|(12, 7, 14)|var|uint8
bop_5065 = relay.mod(call_5062.astype('float32'), relay.reshape(var_5064.astype('float32'), relay.shape_of(call_5062))) # shape=(12, 7, 14)
bop_5068 = relay.mod(call_5063.astype('float32'), relay.reshape(var_5064.astype('float32'), relay.shape_of(call_5063))) # shape=(12, 7, 14)
output = relay.Tuple([bop_5065,])
output2 = relay.Tuple([bop_5068,])
func_5072 = relay.Function([var_5064,], output)
mod['func_5072'] = func_5072
mod = relay.transform.InferType()(mod)
var_5073 = relay.var("var_5073", dtype = "uint8", shape = (12, 7, 14))#candidate|5073|(12, 7, 14)|var|uint8
output = func_5072(var_5073)
func_5074 = relay.Function([var_5073], output)
mutated_mod['func_5074'] = func_5074
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1368_call = mod.get_global_var('func_1368')
func_1369_call = mutated_mod.get_global_var('func_1369')
call_5078 = relay.TupleGetItem(func_1368_call(), 0)
call_5079 = relay.TupleGetItem(func_1369_call(), 0)
uop_5080 = relay.acosh(call_5078.astype('float64')) # shape=(12, 7, 14)
uop_5082 = relay.acosh(call_5079.astype('float64')) # shape=(12, 7, 14)
output = relay.Tuple([uop_5080,])
output2 = relay.Tuple([uop_5082,])
func_5094 = relay.Function([], output)
mod['func_5094'] = func_5094
mod = relay.transform.InferType()(mod)
output = func_5094()
func_5095 = relay.Function([], output)
mutated_mod['func_5095'] = func_5095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1794_call = mod.get_global_var('func_1794')
func_1795_call = mutated_mod.get_global_var('func_1795')
call_5118 = func_1794_call()
call_5119 = func_1794_call()
var_5129 = relay.var("var_5129", dtype = "float64", shape = (7, 4, 7))#candidate|5129|(7, 4, 7)|var|float64
bop_5130 = relay.subtract(call_5118.astype('uint64'), relay.reshape(var_5129.astype('uint64'), relay.shape_of(call_5118))) # shape=(7, 4, 7)
bop_5133 = relay.subtract(call_5119.astype('uint64'), relay.reshape(var_5129.astype('uint64'), relay.shape_of(call_5119))) # shape=(7, 4, 7)
func_1758_call = mod.get_global_var('func_1758')
func_1759_call = mutated_mod.get_global_var('func_1759')
call_5147 = func_1758_call()
call_5148 = func_1758_call()
func_1255_call = mod.get_global_var('func_1255')
func_1259_call = mutated_mod.get_global_var('func_1259')
var_5155 = relay.var("var_5155", dtype = "int32", shape = ())#candidate|5155|()|var|int32
var_5156 = relay.var("var_5156", dtype = "int32", shape = (48,))#candidate|5156|(48,)|var|int32
call_5154 = relay.TupleGetItem(func_1255_call(relay.reshape(var_5155.astype('int32'), []), relay.reshape(var_5156.astype('int32'), [48,]), ), 5)
call_5157 = relay.TupleGetItem(func_1259_call(relay.reshape(var_5155.astype('int32'), []), relay.reshape(var_5156.astype('int32'), [48,]), ), 5)
output = relay.Tuple([bop_5130,call_5147,call_5154,var_5155,var_5156,])
output2 = relay.Tuple([bop_5133,call_5148,call_5157,var_5155,var_5156,])
func_5171 = relay.Function([var_5129,var_5155,var_5156,], output)
mod['func_5171'] = func_5171
mod = relay.transform.InferType()(mod)
var_5172 = relay.var("var_5172", dtype = "float64", shape = (7, 4, 7))#candidate|5172|(7, 4, 7)|var|float64
var_5173 = relay.var("var_5173", dtype = "int32", shape = ())#candidate|5173|()|var|int32
var_5174 = relay.var("var_5174", dtype = "int32", shape = (48,))#candidate|5174|(48,)|var|int32
output = func_5171(var_5172,var_5173,var_5174,)
func_5175 = relay.Function([var_5172,var_5173,var_5174,], output)
mutated_mod['func_5175'] = func_5175
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5193 = relay.var("var_5193", dtype = "int16", shape = (16, 12, 1))#candidate|5193|(16, 12, 1)|var|int16
var_5194 = relay.var("var_5194", dtype = "int16", shape = (16, 12, 8))#candidate|5194|(16, 12, 8)|var|int16
bop_5195 = relay.left_shift(var_5193.astype('int16'), var_5194.astype('int16')) # shape=(16, 12, 8)
bop_5210 = relay.add(var_5194.astype('float32'), var_5193.astype('float32')) # shape=(16, 12, 8)
var_5224 = relay.var("var_5224", dtype = "int16", shape = (16, 12, 3))#candidate|5224|(16, 12, 3)|var|int16
bop_5225 = relay.equal(var_5193.astype('bool'), var_5224.astype('bool')) # shape=(16, 12, 3)
output = relay.Tuple([bop_5195,bop_5210,bop_5225,])
output2 = relay.Tuple([bop_5195,bop_5210,bop_5225,])
func_5239 = relay.Function([var_5193,var_5194,var_5224,], output)
mod['func_5239'] = func_5239
mod = relay.transform.InferType()(mod)
var_5240 = relay.var("var_5240", dtype = "int16", shape = (16, 12, 1))#candidate|5240|(16, 12, 1)|var|int16
var_5241 = relay.var("var_5241", dtype = "int16", shape = (16, 12, 8))#candidate|5241|(16, 12, 8)|var|int16
var_5242 = relay.var("var_5242", dtype = "int16", shape = (16, 12, 3))#candidate|5242|(16, 12, 3)|var|int16
output = func_5239(var_5240,var_5241,var_5242,)
func_5243 = relay.Function([var_5240,var_5241,var_5242,], output)
mutated_mod['func_5243'] = func_5243
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5285 = relay.var("var_5285", dtype = "float64", shape = (6, 5, 11))#candidate|5285|(6, 5, 11)|var|float64
uop_5286 = relay.exp(var_5285.astype('float64')) # shape=(6, 5, 11)
func_5239_call = mod.get_global_var('func_5239')
func_5243_call = mutated_mod.get_global_var('func_5243')
var_5318 = relay.var("var_5318", dtype = "int16", shape = (192,))#candidate|5318|(192,)|var|int16
const_5319 = relay.const([[-10,-8,-7,-2,2,3,-4,3,-4,-9,10,-6,6,6,3,-6,10,7,-10,-10,3,-6,2,-10],[-4,5,9,-5,-5,6,6,-10,-5,8,10,-8,1,9,-3,-4,-9,3,2,-1,-10,4,9,4],[5,-1,-10,-7,3,6,4,-3,9,-1,5,-6,10,-2,-6,-5,8,3,7,9,-5,-3,5,3],[5,2,7,6,-10,8,-5,-6,-1,1,10,-5,4,-5,8,-2,-4,-3,-4,8,-5,3,-9,5],[1,-7,5,-5,2,8,10,2,-6,-4,-4,-6,7,1,10,6,-1,2,5,-4,9,-8,4,4],[-7,-10,-9,1,10,3,-5,1,2,-1,1,3,-9,-3,-2,-5,-5,9,-5,-1,-2,3,1,-5],[-7,9,4,-10,-6,-10,-9,-9,-9,-10,1,-7,6,-2,6,-2,-4,1,-5,-2,5,1,-6,10],[-9,10,-2,4,-9,-6,2,7,9,5,-8,-6,1,-9,-8,-2,9,-8,9,10,-6,2,-2,-7],[7,-6,-1,10,-10,8,-7,-6,2,-7,5,10,4,1,-3,9,-2,-4,9,-4,-2,8,5,-4],[-7,-2,10,4,-6,-2,-5,6,9,-10,-6,1,9,5,-3,-2,2,5,-6,8,3,-10,2,-6],[7,-1,-10,-1,2,-4,-7,-9,2,2,10,1,-1,-4,8,8,-3,10,-1,-2,-9,10,-3,-4],[3,-3,8,-8,5,-6,1,-8,-2,8,1,8,6,-3,-7,4,-5,-2,-10,-5,-4,8,6,-10],[6,2,7,7,-8,-2,9,6,2,-10,10,-9,-6,-2,7,-1,-1,2,4,1,10,-8,1,5],[-4,6,-8,-2,6,-9,5,5,4,4,-7,-10,2,5,4,5,-5,-3,9,-1,7,-5,-1,-8],[8,-3,-1,-1,10,4,-10,-1,-3,-9,-8,-5,-2,9,3,-8,-3,7,3,5,-7,-7,-10,-1],[-3,-5,-3,-9,-5,8,-8,-10,-9,-3,6,-6,-10,10,-3,3,3,8,2,-1,-8,4,9,-6],[-10,9,-8,-9,-9,-8,-9,-8,-3,-8,-8,2,10,-1,-10,7,6,8,-2,4,-5,4,7,6],[-2,7,-5,-3,4,6,-1,-6,9,-4,-10,-2,5,10,-2,4,-3,4,-7,-5,-3,7,-3,4],[6,3,-10,-2,5,-7,-10,-10,1,3,5,10,-8,-3,-9,-5,6,-10,4,-1,6,5,10,-1],[3,2,-3,-5,1,-3,8,-7,5,3,1,-10,4,3,3,9,-9,6,-3,-4,-1,-7,5,5],[3,-1,2,3,7,1,1,7,-9,3,-6,-10,-4,-7,-3,10,8,2,1,5,-3,-9,4,-6],[1,-9,-4,3,6,-6,-2,-4,-6,-2,4,-6,-4,1,10,-5,5,-5,10,7,-8,4,-9,-2],[-7,-5,-2,5,-3,5,4,-4,1,7,9,-9,9,9,-2,-5,3,-9,1,10,2,7,3,-4],[1,8,-5,7,2,2,-6,4,-6,-4,-9,-1,10,-7,-9,9,-2,10,-6,1,-2,2,9,7],[9,2,-6,10,-1,6,8,10,4,7,-6,8,1,-5,-7,6,4,5,1,3,-10,1,-6,-10],[-10,10,7,-5,-9,-7,-5,-2,10,-6,-1,-2,9,3,-4,-6,1,-2,8,-5,8,-5,4,1],[-5,5,-7,10,-10,-1,-5,-1,-7,-3,10,3,-1,-10,-6,-8,-7,10,2,2,-3,8,-2,-6],[-2,5,8,-10,6,3,1,4,6,6,4,-10,8,6,-7,-2,-3,10,5,-10,8,-5,-3,-10],[5,-7,-1,7,-6,-3,7,-1,10,-2,1,-8,-3,9,3,7,7,-6,-10,10,-6,-1,6,-3],[-3,-5,-5,5,-7,-6,-6,-6,-4,1,-5,-1,2,4,-4,-8,10,-3,-6,2,3,-4,8,1],[-4,9,-3,-10,2,5,-1,-5,8,-5,-8,-8,5,-9,-3,9,5,7,-8,-3,1,8,-2,-10],[-5,-7,-3,4,-8,-1,5,6,-7,8,-10,-8,10,2,3,4,-8,-10,5,-7,7,4,9,2],[5,-1,-10,5,-7,3,8,7,-10,6,-1,8,2,-7,-4,-7,8,5,9,9,-6,7,2,3],[-2,-5,10,8,7,-3,6,-1,7,4,5,-3,6,8,-5,7,-8,10,-10,-1,6,10,-5,-8],[-7,10,6,5,-5,-9,4,10,10,1,8,7,-10,-8,9,7,8,10,-3,5,9,-10,8,6],[-10,8,-1,-4,3,5,-5,8,2,-7,-4,-4,-4,6,6,2,9,4,4,-2,-9,8,9,-7],[-5,-5,5,-2,4,3,-9,6,4,9,-7,6,6,-9,-2,-4,-1,6,8,6,-5,4,5,-2],[-9,8,10,1,10,10,6,-8,5,-6,-1,5,-3,-10,8,-9,2,2,-3,-7,2,-6,-3,9],[8,1,10,-7,-4,3,-10,-10,10,-2,4,8,9,8,8,-8,-3,-8,-4,7,-4,3,-3,-6],[-2,5,-8,-3,7,-8,9,3,-4,6,-8,7,3,7,2,8,2,1,-8,-8,6,-2,-2,8],[6,4,-8,9,3,-7,9,-9,9,-2,4,2,6,6,8,1,-9,1,10,-9,6,-7,9,10],[6,5,-4,2,2,5,6,-6,-5,-2,-7,-7,7,1,-2,6,-3,-9,-7,-6,-3,-8,8,-3],[3,7,8,-4,-10,5,-4,-1,1,5,-3,8,1,-4,-2,-4,-4,-4,7,-9,2,2,-4,-4],[-2,-6,9,4,2,3,-7,-10,7,3,-3,-2,8,-1,-6,-1,6,-7,3,-7,9,10,6,-5],[5,9,-4,-3,5,-7,10,1,-7,-3,10,-5,1,-3,5,-9,9,10,-9,8,-10,-8,4,8],[-10,2,-10,-8,-2,7,-2,10,4,-7,-7,-10,-1,-9,8,8,8,-7,-7,-1,-8,6,5,-1],[8,-6,2,-3,-4,8,10,9,6,-6,3,-1,6,-10,5,-3,-1,1,-5,-6,7,-1,10,6],[-6,-10,-10,9,-8,10,-2,8,2,-5,-4,-5,7,-9,-6,4,9,-2,-4,-6,1,8,9,-5],[7,-7,4,-3,6,7,-9,3,-4,-7,-7,1,-9,9,4,8,-7,2,4,10,9,1,10,-6],[-10,-1,7,5,10,5,-10,-5,7,8,-5,3,-8,4,2,-10,-4,-9,4,7,8,8,-5,4],[-2,-5,-3,-5,-7,-6,-10,9,-1,2,-2,9,-3,7,2,3,-6,-3,9,9,-6,2,3,-9],[-10,10,-2,-2,-6,4,-2,1,5,8,-3,-9,4,-6,-5,-3,-6,8,2,4,1,-7,6,5],[-4,-7,-2,8,2,-4,9,-3,-10,6,3,3,9,-10,-8,8,8,8,6,5,-10,-6,-6,-5],[-9,2,10,-9,5,-5,4,6,-3,-3,10,8,9,-10,-2,-3,5,-7,5,7,-3,5,-8,-1],[-3,3,-2,-5,4,6,-10,10,-8,-2,1,3,2,5,-8,2,-9,-7,5,-4,7,8,10,-5],[-3,3,8,1,-5,1,-1,5,9,2,5,-6,7,2,-10,-8,-5,10,-9,5,-7,5,1,-9],[3,-6,-9,-5,-4,4,5,8,4,-3,-9,5,5,4,-2,-6,-6,7,5,-2,6,-3,-9,-1],[1,6,-4,-3,-2,5,-10,1,3,1,-8,7,10,-7,4,-4,3,2,10,6,-2,6,-4,-8],[-4,7,4,8,-5,-5,-2,-2,6,4,-1,9,-3,-7,-3,4,-8,9,-4,-5,9,-7,-6,10],[7,1,-4,3,-7,-6,9,-8,-2,6,2,-6,3,4,4,-5,-7,9,9,1,-4,6,7,-8],[-9,-5,-10,-3,-4,-2,2,9,4,-3,10,8,-2,-7,8,-8,-2,1,-5,2,-3,8,-4,7],[5,-2,5,-10,4,-8,3,-3,-10,-6,7,2,4,5,7,7,-3,6,9,-5,-5,7,-8,4],[3,10,-10,1,-4,-6,-10,2,2,-1,6,-3,-8,1,-1,3,7,-3,8,2,2,-3,-1,-6],[-3,-5,3,-1,10,-5,9,4,-1,-2,3,-1,2,-9,-8,-7,2,-3,-1,3,8,-2,-6,-2]], dtype = "int16")#candidate|5319|(64, 24)|const|int16
const_5320 = relay.const([6,-10,3,4,6,-7,-5,6,-1,4,-8,-4,9,7,6,5,-6,-2,8,10,-8,-10,5,10,-5,-2,7,5,5,-7,-10,5,-9,6,3,-3,3,3,-1,4,9,3,3,2,-8,8,-1,-5,-10,-8,-8,-3,6,9,-8,5,2,-3,-4,10,4,-3,3,-5,-10,5,4,9,3,-9,-2,2,2,6,10,9,5,9,9,-10,-7,-7,4,-2,5,-2,8,10,9,8,-5,3,1,8,8,-1,5,-7,-5,6,2,8,1,-8,5,8,-4,-1,-7,-5,7,9,5,10,4,-9,-5,-6,6,-5,-1,2,-7,8,-2,-8,-8,-2,2,-2,-2,-5,-9,-3,5,5,-2,1,10,1,4,-4,6,-5,9,-7,10,8,-2,-6,9,-5,10,8,5,3,-1,-2,-2,7,6,-10,5,10,9,6,-7,6,-7,7,-6,-1,-7,3,-10,9,-4,6,9,7,-10,-5,-6,-4,5,-4,2,-7,-8,6,-1,-6,8,-4,-8,4,-6,4,-9,-4,10,7,-3,8,-7,1,-3,-4,-1,-7,-9,-4,1,-6,6,7,8,-7,10,-2,4,-6,-2,-8,-9,9,-6,-5,-3,-7,3,-7,10,1,9,-9,-9,-10,7,4,-10,4,-8,-5,9,1,6,2,10,-7,9,4,5,10,1,-10,7,-9,2,-3,5,-5,-2,8,2,-2,5,10,-1,4,4,-3,7,-3,5,1,2,3,-3,-5,-8,8,7,5,-8,-10,-10,-3,-6,-5,-2,4,-4,-7,8,4,1,1,-9,5,-5,2,-9,-4,9,9,8,7,-8,9,-6,-6,-2,-6,5,-2,8,8,7,4,1,-1,-7,-9,1,-3,-8,8,7,-2,-7,5,-8,-5,-4,5,4,-4,-2,-6,-10,2,9,9,5,-2,-8,10,-1,3,5,3,-1,2,10,8,8,-8,-1,-5,-8,7,-6,-2,-1,4,-2,-7,4,8,-7,3,-6,2,-8,2,-4,4,5,6,-2,5,-7,-6,-2,-4,9,-4,-8,2,5,-4,4,-8,-5,-6,7,8,4,5,-8,-6,-8,-6,9,4,2,3,-7,7,-9,6,4,10,-2,5,5,9,-4,-2,2,8,-6,-2,-4,-5,-1,9,-9,-5,-3,8,-4,1,-3,2,9,-1,-1,-7,1,-7,5,2,-2,-2,7,-5,9,8,1,7,-10,-4,-1,-3,3,9,-4,1,-7,-5,2,-7,7,3,7,-7,-10,5,2,-8,-8,4,-7,1,5,-10,5,-10,-5,8,4,-9,6,8,2,4,4,-3,10,-6,-10,-4,4,-5,6,10,-9,-6,3,-3,-1,-4,-5,-5,2,4,8,5,1,-10,5,8,-1,1,10,8,2,-6,2,4,5,-4,-7,4,10,6,5,1,8,-1,-5,2,2,6,3,8,9,8,10,3,-7,-7,-3,-10,10,1,-10,-5,-3,6,3,2,5,-10,-4,-7,2,-5,2,-5,-5,-8,-1,7,5,10,9,-2,5,-9,4,2,-2,10], dtype = "int16")#candidate|5320|(576,)|const|int16
call_5317 = relay.TupleGetItem(func_5239_call(relay.reshape(var_5318.astype('int16'), [16, 12, 1]), relay.reshape(const_5319.astype('int16'), [16, 12, 8]), relay.reshape(const_5320.astype('int16'), [16, 12, 3]), ), 0)
call_5321 = relay.TupleGetItem(func_5243_call(relay.reshape(var_5318.astype('int16'), [16, 12, 1]), relay.reshape(const_5319.astype('int16'), [16, 12, 8]), relay.reshape(const_5320.astype('int16'), [16, 12, 3]), ), 0)
func_5094_call = mod.get_global_var('func_5094')
func_5095_call = mutated_mod.get_global_var('func_5095')
call_5323 = relay.TupleGetItem(func_5094_call(), 0)
call_5324 = relay.TupleGetItem(func_5095_call(), 0)
output = relay.Tuple([uop_5286,call_5317,var_5318,const_5319,const_5320,call_5323,])
output2 = relay.Tuple([uop_5286,call_5321,var_5318,const_5319,const_5320,call_5324,])
func_5369 = relay.Function([var_5285,var_5318,], output)
mod['func_5369'] = func_5369
mod = relay.transform.InferType()(mod)
mutated_mod['func_5369'] = func_5369
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5369_call = mutated_mod.get_global_var('func_5369')
var_5371 = relay.var("var_5371", dtype = "float64", shape = (6, 5, 11))#candidate|5371|(6, 5, 11)|var|float64
var_5372 = relay.var("var_5372", dtype = "int16", shape = (192,))#candidate|5372|(192,)|var|int16
call_5370 = func_5369_call(var_5371,var_5372,)
output = call_5370
func_5373 = relay.Function([var_5371,var_5372,], output)
mutated_mod['func_5373'] = func_5373
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3850_call = mod.get_global_var('func_3850')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_5435 = func_3850_call()
call_5436 = func_3850_call()
output = call_5435
output2 = call_5436
func_5442 = relay.Function([], output)
mod['func_5442'] = func_5442
mod = relay.transform.InferType()(mod)
mutated_mod['func_5442'] = func_5442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5442_call = mutated_mod.get_global_var('func_5442')
call_5443 = func_5442_call()
output = call_5443
func_5444 = relay.Function([], output)
mutated_mod['func_5444'] = func_5444
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_5447 = relay.TupleGetItem(func_1883_call(), 1)
call_5448 = relay.TupleGetItem(func_1885_call(), 1)
output = call_5447
output2 = call_5448
func_5462 = relay.Function([], output)
mod['func_5462'] = func_5462
mod = relay.transform.InferType()(mod)
output = func_5462()
func_5463 = relay.Function([], output)
mutated_mod['func_5463'] = func_5463
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4091_call = mod.get_global_var('func_4091')
func_4092_call = mutated_mod.get_global_var('func_4092')
call_5506 = relay.TupleGetItem(func_4091_call(), 1)
call_5507 = relay.TupleGetItem(func_4092_call(), 1)
var_5516 = relay.var("var_5516", dtype = "float64", shape = (5, 13, 15))#candidate|5516|(5, 13, 15)|var|float64
bop_5517 = relay.logical_and(call_5506.astype('bool'), relay.reshape(var_5516.astype('bool'), relay.shape_of(call_5506))) # shape=(5, 13, 15)
bop_5520 = relay.logical_and(call_5507.astype('bool'), relay.reshape(var_5516.astype('bool'), relay.shape_of(call_5507))) # shape=(5, 13, 15)
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_5522 = func_5442_call()
call_5523 = func_5442_call()
output = relay.Tuple([bop_5517,call_5522,])
output2 = relay.Tuple([bop_5520,call_5523,])
func_5524 = relay.Function([var_5516,], output)
mod['func_5524'] = func_5524
mod = relay.transform.InferType()(mod)
var_5525 = relay.var("var_5525", dtype = "float64", shape = (5, 13, 15))#candidate|5525|(5, 13, 15)|var|float64
output = func_5524(var_5525)
func_5526 = relay.Function([var_5525], output)
mutated_mod['func_5526'] = func_5526
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4533_call = mod.get_global_var('func_4533')
func_4534_call = mutated_mod.get_global_var('func_4534')
call_5548 = relay.TupleGetItem(func_4533_call(), 0)
call_5549 = relay.TupleGetItem(func_4534_call(), 0)
func_1043_call = mod.get_global_var('func_1043')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_5566 = relay.TupleGetItem(func_1043_call(), 1)
call_5567 = relay.TupleGetItem(func_1045_call(), 1)
output = relay.Tuple([call_5548,call_5566,])
output2 = relay.Tuple([call_5549,call_5567,])
func_5569 = relay.Function([], output)
mod['func_5569'] = func_5569
mod = relay.transform.InferType()(mod)
output = func_5569()
func_5570 = relay.Function([], output)
mutated_mod['func_5570'] = func_5570
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_5619 = relay.TupleGetItem(func_859_call(), 0)
call_5620 = relay.TupleGetItem(func_860_call(), 0)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_5621 = func_1072_call()
call_5622 = func_1072_call()
output = relay.Tuple([call_5619,call_5621,])
output2 = relay.Tuple([call_5620,call_5622,])
func_5623 = relay.Function([], output)
mod['func_5623'] = func_5623
mod = relay.transform.InferType()(mod)
output = func_5623()
func_5624 = relay.Function([], output)
mutated_mod['func_5624'] = func_5624
mutated_mod = relay.transform.InferType()(mutated_mod)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_5638 = func_480_call()
call_5639 = func_480_call()
output = relay.Tuple([call_5638,])
output2 = relay.Tuple([call_5639,])
func_5667 = relay.Function([], output)
mod['func_5667'] = func_5667
mod = relay.transform.InferType()(mod)
mutated_mod['func_5667'] = func_5667
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5667_call = mutated_mod.get_global_var('func_5667')
call_5668 = func_5667_call()
output = call_5668
func_5669 = relay.Function([], output)
mutated_mod['func_5669'] = func_5669
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_5675 = relay.TupleGetItem(func_4208_call(), 0)
call_5676 = relay.TupleGetItem(func_4210_call(), 0)
output = relay.Tuple([call_5675,])
output2 = relay.Tuple([call_5676,])
func_5693 = relay.Function([], output)
mod['func_5693'] = func_5693
mod = relay.transform.InferType()(mod)
output = func_5693()
func_5694 = relay.Function([], output)
mutated_mod['func_5694'] = func_5694
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5700 = relay.var("var_5700", dtype = "uint32", shape = (3, 8, 16))#candidate|5700|(3, 8, 16)|var|uint32
var_5701 = relay.var("var_5701", dtype = "uint32", shape = (3, 8, 16))#candidate|5701|(3, 8, 16)|var|uint32
bop_5702 = relay.logical_xor(var_5700.astype('uint32'), relay.reshape(var_5701.astype('uint32'), relay.shape_of(var_5700))) # shape=(3, 8, 16)
output = relay.Tuple([bop_5702,])
output2 = relay.Tuple([bop_5702,])
func_5706 = relay.Function([var_5700,var_5701,], output)
mod['func_5706'] = func_5706
mod = relay.transform.InferType()(mod)
var_5707 = relay.var("var_5707", dtype = "uint32", shape = (3, 8, 16))#candidate|5707|(3, 8, 16)|var|uint32
var_5708 = relay.var("var_5708", dtype = "uint32", shape = (3, 8, 16))#candidate|5708|(3, 8, 16)|var|uint32
output = func_5706(var_5707,var_5708,)
func_5709 = relay.Function([var_5707,var_5708,], output)
mutated_mod['func_5709'] = func_5709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3897_call = mod.get_global_var('func_3897')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_5715 = relay.TupleGetItem(func_3897_call(), 0)
call_5716 = relay.TupleGetItem(func_3898_call(), 0)
output = call_5715
output2 = call_5716
func_5718 = relay.Function([], output)
mod['func_5718'] = func_5718
mod = relay.transform.InferType()(mod)
output = func_5718()
func_5719 = relay.Function([], output)
mutated_mod['func_5719'] = func_5719
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4146_call = mod.get_global_var('func_4146')
func_4147_call = mutated_mod.get_global_var('func_4147')
call_5727 = func_4146_call()
call_5728 = func_4146_call()
output = call_5727
output2 = call_5728
func_5732 = relay.Function([], output)
mod['func_5732'] = func_5732
mod = relay.transform.InferType()(mod)
mutated_mod['func_5732'] = func_5732
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5732_call = mutated_mod.get_global_var('func_5732')
call_5733 = func_5732_call()
output = call_5733
func_5734 = relay.Function([], output)
mutated_mod['func_5734'] = func_5734
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5748 = relay.const([[[-7,-2,5,3,-9,-4,3,-7],[5,-6,10,-1,-10,5,-3,5],[-7,10,-7,5,-8,-10,1,5]],[[-3,1,4,-4,-7,6,-2,-9],[9,5,6,3,9,6,-3,7],[1,9,-2,-10,2,10,-8,-6]],[[-10,-5,1,2,-3,9,9,-10],[-8,6,2,10,3,-9,-10,-9],[6,-9,-4,-4,-9,-3,-2,9]],[[-1,-1,-4,-6,-10,-1,2,1],[6,2,10,6,-2,8,-1,-6],[-5,-5,6,7,8,6,-7,-7]],[[-6,-4,-6,6,1,-2,4,-7],[4,7,5,8,1,5,-3,-1],[-1,7,-7,-5,-8,1,4,-10]],[[-1,-8,2,-2,-2,-1,9,-3],[-8,10,-5,4,-2,5,4,-6],[-6,-1,-2,1,2,-6,5,3]],[[-10,-1,-8,8,9,-9,3,-5],[-2,5,-1,-8,8,6,-5,-9],[4,2,2,-3,7,3,7,-9]],[[8,5,-2,-4,8,6,-9,-10],[2,4,-6,-6,-10,3,8,-8],[-5,6,7,8,10,-1,-6,3]],[[-7,-5,-7,-3,1,-6,-7,-7],[-9,-8,5,-4,-9,-7,7,4],[-8,-4,1,1,5,-2,2,-3]],[[-4,-9,-6,-7,7,-9,-3,-6],[-1,5,-10,-3,-6,7,6,-10],[10,3,-2,2,-2,4,5,6]],[[4,9,2,1,1,-7,-8,1],[-10,-6,5,-4,3,4,-9,8],[-4,9,3,5,8,2,2,-3]],[[-8,-5,-1,1,6,-3,-8,8],[10,-9,9,-6,9,-2,3,-1],[6,-5,-4,2,4,5,-8,5]],[[2,2,9,8,-8,-8,6,2],[-5,1,-5,-1,10,-2,-1,-10],[-10,-6,-2,8,-5,-3,-8,-4]]], dtype = "int32")#candidate|5748|(13, 3, 8)|const|int32
var_5749 = relay.var("var_5749", dtype = "int32", shape = (13, 3, 8))#candidate|5749|(13, 3, 8)|var|int32
bop_5750 = relay.equal(const_5748.astype('bool'), relay.reshape(var_5749.astype('bool'), relay.shape_of(const_5748))) # shape=(13, 3, 8)
uop_5755 = relay.sqrt(var_5749.astype('float32')) # shape=(13, 3, 8)
bop_5758 = relay.greater_equal(uop_5755.astype('bool'), relay.reshape(const_5748.astype('bool'), relay.shape_of(uop_5755))) # shape=(13, 3, 8)
func_1425_call = mod.get_global_var('func_1425')
func_1427_call = mutated_mod.get_global_var('func_1427')
call_5768 = func_1425_call()
call_5769 = func_1425_call()
output = relay.Tuple([bop_5750,bop_5758,call_5768,])
output2 = relay.Tuple([bop_5750,bop_5758,call_5769,])
func_5770 = relay.Function([var_5749,], output)
mod['func_5770'] = func_5770
mod = relay.transform.InferType()(mod)
var_5771 = relay.var("var_5771", dtype = "int32", shape = (13, 3, 8))#candidate|5771|(13, 3, 8)|var|int32
output = func_5770(var_5771)
func_5772 = relay.Function([var_5771], output)
mutated_mod['func_5772'] = func_5772
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4146_call = mod.get_global_var('func_4146')
func_4147_call = mutated_mod.get_global_var('func_4147')
call_5802 = func_4146_call()
call_5803 = func_4146_call()
func_1955_call = mod.get_global_var('func_1955')
func_1956_call = mutated_mod.get_global_var('func_1956')
call_5813 = func_1955_call()
call_5814 = func_1955_call()
uop_5821 = relay.acos(call_5802.astype('float32')) # shape=(5, 11, 4)
uop_5823 = relay.acos(call_5803.astype('float32')) # shape=(5, 11, 4)
func_1587_call = mod.get_global_var('func_1587')
func_1589_call = mutated_mod.get_global_var('func_1589')
const_5835 = relay.const([-0.775608,-0.865249,-8.432470,3.581683,0.894079,5.297777,6.276511,8.928602,-1.235057,8.385449,-0.405133,9.782304,-4.112906,-0.523030,7.818616,-5.218327,5.366007,1.932178,-6.935435,0.871656,-1.690044,5.128837,4.584761,4.716657,1.053970,0.913106,7.844915,-8.019338,8.329209,7.941453,-4.970965,-9.432004,-1.447339,-1.833632,2.114971,-1.371387,-4.128101,1.692374,-6.061415,6.769784,7.641794,7.320799,-5.619097,0.643323,-1.036265,-5.974069,-1.597468,2.488332,-8.570024,5.806970,8.550559,2.434914,8.536873,-0.193511,-0.526961,9.762910,-8.330583,-5.495900,-2.275580,-5.899356,-7.939740,-0.300364,1.074168,1.242149,8.325276,3.555481,-8.700940,-3.961809,-4.009518,6.587081,7.713464,-3.294981,3.597956,-4.569071,-7.732722,-0.515604,3.546888,5.586207,-9.731250,-2.555229,7.231484,1.212580,-5.189546,-7.788080,-5.574741,3.465532,-9.685935,9.875978,-0.704013,-0.478839,-5.617790,0.368108,1.682994,-9.661684,4.693844,6.106343,8.781860,-2.007169,-2.637857,-4.779573,-7.835104,-8.086330,7.997860,-5.026057,4.407587,1.685988,-0.962871,5.135607,9.162462,1.625500,-8.043641,-2.306534,6.994197,-5.613908,2.218023,-9.491823,-4.066801,-9.393012,-5.591545,-1.786583,1.523770,7.886104,-9.675656,0.326570,1.559878,6.413221,7.775263,8.041318,-8.995304,0.116166,-9.942004,-6.216671,-6.314959,-4.572738,5.070893,5.997204,-1.767786,-1.688321,7.348956,2.103523,4.756310,1.703205,-7.770636,7.874545,-1.549857,-8.849728,7.440279,6.782120,6.680489,-7.510043,-8.283675,-1.768934,4.346116,-0.515914,-7.891018,9.117811,-8.908211,5.967832,7.835079,1.477094,6.107686,-3.142509,-3.754422,-8.887956,2.651301,7.008576,-1.933906,3.722426,-9.246598,4.127607,7.976619,-9.166478,4.773619,-9.637338,2.735923,-3.645547,4.822224,7.499073,-7.989166,0.804755,-6.569746,-1.645030,-5.730264,-1.011892,7.132558,-1.566143,-1.280716,-2.093272,-8.944666,-4.622757,-8.549740,-0.538541,2.643396,-6.282747,1.893551,-7.868437,-9.466146,0.398406,-6.970730,5.801356,6.010672,-3.418300,5.212841,9.896048,7.488461,6.893739,-9.766217,1.753335,8.191454,2.936379,1.534738,-2.357068,-2.303103,8.246648,-8.623971,-6.354522,-3.472767,4.955890,7.055091,2.501590,1.192990,5.786453,-4.696301,5.302084,-8.930372,-6.182089,-9.846197,2.131967,-4.256847,7.807167,9.508871,-4.724275,-2.061127,7.273087,-4.752721,-4.493434,7.206564,1.331137,-6.459539,1.186864,-8.897495,4.625529,2.181876,1.010642,5.063926,-3.295889,1.650431,-2.474489,-3.112025,2.106586,-9.311092,-5.175034,5.280729,2.716713,4.014460,-0.043010,-6.053972,-9.703468,-3.195054,-8.304169,9.615064,9.644925,7.122330,-6.206596,4.816922,8.230960,-2.829748,-1.110965,4.877473,1.457941,-7.631286,-8.951162,0.841470,-1.547999,9.870800,1.455659,3.408938,0.743971,-2.071639,8.298042,8.659210,3.516801,-0.474102,-2.774194,6.987078,-7.744695,3.050997,2.647761,-1.741883,0.900407,-7.989150,-2.188458,1.124968,-1.829506,3.858795,6.841962,-1.887107,-2.299448,-9.709560,8.274224,9.187093,-1.210033,-5.140771,2.055869,4.944063,-0.433870,-7.636282,-4.930667,-3.174863,9.126980,-1.644845,6.608459,-5.763603,6.022050,-5.944451,-6.937463,3.511764,-1.912477,-6.611187,-9.746416,-1.871760,2.238879,8.704413,-5.968201,7.435795,4.389731,3.002929,-7.779710,0.066047,-1.725725,-1.516082,9.780852,0.082696,-7.772727,3.847302,-0.147138,7.660536,-9.229110,1.360022,4.626054,0.466805,-3.729672,1.493675,-4.043939,-8.357781,-0.012241,9.094711,-5.096971,6.103628,2.432965,3.910786,7.315118,3.045014,6.506095,-6.128983,6.367202,-4.581013,-6.135829,6.681736,-2.718711,-4.405628,-3.353036,-1.357998,-0.033042,0.179562,-0.591310,2.037711,-9.339883,-6.175077,4.369177,-5.761487,-6.143555,-8.353704,-8.547336,2.108744,-4.798795,1.088580,8.904359,8.994384,5.795485,0.495819,-1.908879,6.920873,-1.719440,-5.090691,8.571228,-6.561419,6.839501,-9.260926,-1.938151,-5.825597,7.804729], dtype = "float32")#candidate|5835|(392,)|const|float32
call_5834 = relay.TupleGetItem(func_1587_call(relay.reshape(const_5835.astype('float32'), [7, 8, 7])), 0)
call_5836 = relay.TupleGetItem(func_1589_call(relay.reshape(const_5835.astype('float32'), [7, 8, 7])), 0)
output = relay.Tuple([call_5813,uop_5821,call_5834,const_5835,])
output2 = relay.Tuple([call_5814,uop_5823,call_5836,const_5835,])
func_5845 = relay.Function([], output)
mod['func_5845'] = func_5845
mod = relay.transform.InferType()(mod)
output = func_5845()
func_5846 = relay.Function([], output)
mutated_mod['func_5846'] = func_5846
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4533_call = mod.get_global_var('func_4533')
func_4534_call = mutated_mod.get_global_var('func_4534')
call_5850 = relay.TupleGetItem(func_4533_call(), 3)
call_5851 = relay.TupleGetItem(func_4534_call(), 3)
output = call_5850
output2 = call_5851
func_5852 = relay.Function([], output)
mod['func_5852'] = func_5852
mod = relay.transform.InferType()(mod)
mutated_mod['func_5852'] = func_5852
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mutated_mod.get_global_var('func_5852')
call_5853 = func_5852_call()
output = call_5853
func_5854 = relay.Function([], output)
mutated_mod['func_5854'] = func_5854
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2087_call = mod.get_global_var('func_2087')
func_2089_call = mutated_mod.get_global_var('func_2089')
call_5860 = relay.TupleGetItem(func_2087_call(), 0)
call_5861 = relay.TupleGetItem(func_2089_call(), 0)
func_791_call = mod.get_global_var('func_791')
func_793_call = mutated_mod.get_global_var('func_793')
call_5874 = func_791_call(relay.reshape(call_5860.astype('float64'), [5, 11, 4]))
call_5875 = func_791_call(relay.reshape(call_5860.astype('float64'), [5, 11, 4]))
output = relay.Tuple([call_5860,call_5874,])
output2 = relay.Tuple([call_5861,call_5875,])
func_5877 = relay.Function([], output)
mod['func_5877'] = func_5877
mod = relay.transform.InferType()(mod)
mutated_mod['func_5877'] = func_5877
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5877_call = mutated_mod.get_global_var('func_5877')
call_5878 = func_5877_call()
output = call_5878
func_5879 = relay.Function([], output)
mutated_mod['func_5879'] = func_5879
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_5880 = func_2294_call()
call_5881 = func_2294_call()
output = call_5880
output2 = call_5881
func_5888 = relay.Function([], output)
mod['func_5888'] = func_5888
mod = relay.transform.InferType()(mod)
output = func_5888()
func_5889 = relay.Function([], output)
mutated_mod['func_5889'] = func_5889
mutated_mod = relay.transform.InferType()(mutated_mod)
const_5903 = relay.const([[[-3,-7,-5,-4,10,-1,8,10,-6,4,-1,3,-6],[-2,-2,-8,-7,9,-2,2,-10,10,3,-7,-4,-9],[8,2,4,10,5,2,5,-6,6,-10,3,2,9],[6,-2,10,-7,-3,-8,-9,-3,5,-2,-4,10,-5],[-5,10,-10,-7,1,2,2,1,10,-3,2,-10,10],[5,7,5,-10,-6,-1,-3,-2,2,-4,-4,-6,-7],[4,3,9,-5,9,-8,7,9,9,-2,-9,-5,-1],[7,-3,-6,-2,-2,-8,-1,1,7,-5,7,10,-5],[8,-2,-8,-8,5,-9,-2,10,-1,8,10,1,-2],[9,2,1,-3,-10,-1,-1,4,-3,-2,8,-4,5],[-4,9,-7,-7,2,8,10,6,8,-8,-9,9,-6],[5,5,-5,-6,-4,5,-1,-1,4,-7,-3,-8,-9],[5,-8,-7,10,3,-1,-2,-2,-8,3,2,-1,8],[5,-8,-2,-2,-4,3,3,9,-5,-2,-7,-9,-10],[-8,1,-6,3,-1,-6,7,-4,-4,-6,-2,6,-9]],[[-4,3,-1,-6,8,-9,7,8,-4,3,-5,6,2],[4,4,10,4,-6,6,-7,6,-7,-7,6,10,-1],[8,8,-7,-7,8,3,-1,-6,10,1,-9,-1,-3],[-10,-8,-10,8,6,10,10,-1,9,1,6,9,9],[8,-6,7,-6,5,-1,1,10,-3,9,-5,-3,-2],[-8,-8,10,-7,7,-10,-8,8,-10,1,10,2,7],[8,2,10,-2,8,-6,-8,-8,-5,-3,-8,-2,3],[-4,-3,-2,2,4,7,10,-10,10,-9,-4,5,-9],[-10,-5,-5,10,9,-3,-10,-2,-3,-2,-1,10,-1],[8,4,10,-10,-9,-3,7,2,2,6,-1,-8,-3],[5,9,-10,3,-6,-9,7,3,6,-9,-9,2,-5],[-6,6,-2,-3,-1,9,8,-7,4,-5,-2,-9,9],[4,-7,4,3,-1,5,9,-10,9,6,4,-8,8],[-10,-2,9,10,-6,7,8,-8,5,-8,6,2,-1],[-1,-5,-8,-8,-4,8,-2,10,-8,1,-1,1,-1]],[[5,8,-10,-7,-10,10,7,8,7,4,3,-6,-5],[-1,4,-3,7,-9,2,2,10,3,-3,5,-3,7],[-10,-8,-10,1,-3,7,6,7,-9,-2,-10,-8,-6],[-4,3,-2,-6,8,-3,2,-3,-6,-2,-9,-3,-3],[5,-9,-6,1,6,-4,6,-10,3,5,-10,5,7],[6,4,-4,-1,-2,-5,10,-6,8,10,-3,2,7],[2,-6,5,-8,1,7,-4,-3,-2,2,9,10,-8],[10,-2,1,-10,-2,1,3,-3,-6,-9,-7,1,-9],[-9,-10,3,-8,1,-10,8,-6,-3,3,-1,-2,-9],[3,8,2,4,-6,-6,-3,-4,5,-6,-3,4,-6],[4,-9,-5,-2,-6,-2,-8,7,-3,-8,5,10,-8],[4,-8,9,6,-2,-2,-6,1,-9,6,-3,-10,9],[6,-9,-2,-8,-3,2,-7,-2,1,7,6,8,-6],[3,2,1,1,2,-5,6,7,7,4,-3,7,-4],[-10,9,5,-9,-3,-5,-2,-2,9,-7,7,2,-3]],[[-6,-7,-5,3,10,-5,-5,1,7,-8,2,-8,-6],[3,8,-3,6,5,4,7,-3,4,3,9,1,-8],[7,-2,-4,-10,-10,-7,2,10,-9,9,9,2,-9],[1,-8,-2,8,-7,10,-5,10,-1,-5,6,9,-7],[-9,2,10,7,-4,-5,5,-5,9,9,5,2,10],[3,5,10,1,-1,5,10,-7,4,-7,8,10,-5],[-7,4,-5,9,-10,-6,-2,1,7,9,-6,-9,-3],[-9,4,7,-1,9,1,-9,-6,10,-4,-7,2,-6],[-10,-9,1,5,2,-5,2,-2,-1,-2,4,6,4],[-8,1,3,8,-2,4,4,-9,10,10,-4,10,9],[1,1,-9,10,-4,9,8,3,-1,7,-4,3,8],[-7,5,-4,1,2,6,-10,-6,4,-4,-8,-4,7],[4,3,7,-2,-8,-1,-2,1,-6,10,-1,9,-3],[-10,-2,6,5,7,1,-8,-4,10,-3,-5,1,2],[4,-5,6,4,2,-3,-1,-1,-10,1,-8,-1,1]],[[8,5,-4,-1,6,4,-5,-1,-3,1,-5,1,-4],[-9,9,-4,2,7,6,4,-5,-5,-5,1,9,2],[-2,1,3,4,10,1,5,9,-7,-7,-1,5,7],[6,9,-1,4,-10,10,10,-9,-3,8,8,-4,10],[-5,3,-2,-1,10,5,-4,10,-8,-5,3,1,-9],[-7,-6,-8,3,-5,2,-7,8,6,-6,7,9,10],[9,3,2,8,-10,-9,10,7,1,-6,-7,-4,-1],[6,-2,-3,-10,8,-10,-10,-5,-1,-6,-8,-2,8],[7,4,-3,-9,7,-6,10,-10,10,-9,10,9,10],[-3,-2,-2,2,-8,-6,-10,10,-3,9,1,3,4],[1,7,3,-4,10,-5,-3,9,-9,-6,6,1,1],[5,-3,-7,-2,-8,2,-1,1,5,8,-5,5,-8],[-1,6,-1,7,-8,10,7,-7,1,1,4,8,-2],[-9,-4,-9,5,8,4,2,10,-4,-2,-7,-10,7],[-6,6,-7,8,1,8,-1,-2,4,7,-5,-2,-3]]], dtype = "int8")#candidate|5903|(5, 15, 13)|const|int8
var_5904 = relay.var("var_5904", dtype = "int8", shape = (5, 15, 13))#candidate|5904|(5, 15, 13)|var|int8
bop_5905 = relay.less_equal(const_5903.astype('bool'), relay.reshape(var_5904.astype('bool'), relay.shape_of(const_5903))) # shape=(5, 15, 13)
var_5912 = relay.var("var_5912", dtype = "int8", shape = (5, 15, 13))#candidate|5912|(5, 15, 13)|var|int8
bop_5913 = relay.bitwise_and(const_5903.astype('int32'), relay.reshape(var_5912.astype('int32'), relay.shape_of(const_5903))) # shape=(5, 15, 13)
func_2412_call = mod.get_global_var('func_2412')
func_2414_call = mutated_mod.get_global_var('func_2414')
call_5916 = relay.TupleGetItem(func_2412_call(), 0)
call_5917 = relay.TupleGetItem(func_2414_call(), 0)
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_5918 = func_5442_call()
call_5919 = func_5442_call()
output = relay.Tuple([bop_5905,bop_5913,call_5916,call_5918,])
output2 = relay.Tuple([bop_5905,bop_5913,call_5917,call_5919,])
func_5945 = relay.Function([var_5904,var_5912,], output)
mod['func_5945'] = func_5945
mod = relay.transform.InferType()(mod)
mutated_mod['func_5945'] = func_5945
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5945_call = mutated_mod.get_global_var('func_5945')
var_5947 = relay.var("var_5947", dtype = "int8", shape = (5, 15, 13))#candidate|5947|(5, 15, 13)|var|int8
var_5948 = relay.var("var_5948", dtype = "int8", shape = (5, 15, 13))#candidate|5948|(5, 15, 13)|var|int8
call_5946 = func_5945_call(var_5947,var_5948,)
output = call_5946
func_5949 = relay.Function([var_5947,var_5948,], output)
mutated_mod['func_5949'] = func_5949
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1043_call = mod.get_global_var('func_1043')
func_1045_call = mutated_mod.get_global_var('func_1045')
call_5951 = relay.TupleGetItem(func_1043_call(), 2)
call_5952 = relay.TupleGetItem(func_1045_call(), 2)
output = relay.Tuple([call_5951,])
output2 = relay.Tuple([call_5952,])
func_5953 = relay.Function([], output)
mod['func_5953'] = func_5953
mod = relay.transform.InferType()(mod)
output = func_5953()
func_5954 = relay.Function([], output)
mutated_mod['func_5954'] = func_5954
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5970 = relay.var("var_5970", dtype = "int32", shape = (12, 10, 12))#candidate|5970|(12, 10, 12)|var|int32
const_5971 = relay.const([[[5,10,10,-4,8,7,-3,-8,9,3,10,-10],[8,-9,-8,6,6,-1,-2,5,2,-3,-6,8],[-7,-7,-6,-1,-4,-1,-5,-8,-5,-1,3,-6],[-10,3,-10,-3,-3,5,-7,6,-7,6,3,4],[2,-2,1,-3,9,-9,9,5,2,1,-6,-1],[-3,-4,-2,2,-4,-10,-6,-8,-10,-3,10,-9],[10,2,-9,9,-1,-8,-3,-6,9,-2,10,8],[-8,9,1,-10,1,8,-4,-4,2,-5,-4,-2],[8,6,5,-10,-8,-10,-6,-1,2,-7,-8,1],[-2,-5,-9,9,-2,-5,-2,-9,-3,-9,-1,6]],[[-2,2,-5,-10,-1,-5,-3,-10,-1,1,2,-4],[-10,4,3,-7,-4,-5,-1,-7,-1,5,-7,8],[-9,-1,-8,4,8,-9,9,-6,-2,1,7,8],[-10,-3,-5,5,9,-3,-3,-2,6,-3,-7,7],[1,5,-5,9,3,2,-2,-1,7,5,2,2],[-1,4,-4,-9,8,5,6,-1,-6,6,2,-9],[3,10,3,5,4,6,-8,-5,9,-4,-5,-6],[7,-9,1,-9,-1,-10,-10,-2,2,-4,-3,1],[-10,10,9,6,-8,-9,4,3,-7,-2,8,3],[2,-4,-8,-10,9,8,4,4,-1,-2,10,-10]],[[10,6,-6,10,8,-6,7,9,-3,-4,10,-2],[-2,6,2,1,-8,10,7,3,-3,4,-4,-8],[7,-6,1,-8,2,4,-9,-4,3,-10,-5,8],[3,-8,4,-6,7,9,-9,10,2,7,-1,10],[-6,-6,5,-7,-7,-7,-2,-3,-6,6,3,9],[9,9,-7,-6,1,-4,-6,-7,7,-6,-9,-7],[-3,-10,-10,-6,-7,1,-5,-8,8,3,2,-1],[-3,7,5,-7,-8,7,-10,-9,7,10,8,8],[-10,4,-10,3,9,7,6,4,-5,-4,-3,1],[-4,4,8,9,-3,-2,-7,8,6,10,1,8]],[[5,10,-6,10,1,3,5,9,-7,3,-7,10],[8,5,-5,7,4,10,8,1,5,1,10,-10],[-5,10,5,5,-1,-5,3,6,1,9,-5,1],[6,10,3,2,-4,-10,-2,2,-5,-8,1,8],[-2,-3,9,9,-5,-3,8,6,8,10,-1,3],[-9,6,7,-4,-1,7,3,5,-4,8,-6,5],[10,-3,-8,-7,-9,9,-7,6,1,7,-9,4],[3,-7,-6,-2,-8,7,1,-2,-7,8,-5,-1],[10,-4,10,-2,2,1,-2,6,8,-5,-9,3],[2,-9,8,7,8,6,-9,-3,10,9,-7,-3]],[[8,5,-8,3,-10,9,4,5,-5,-2,-3,-5],[8,-8,-9,-9,-10,-4,3,-10,-4,10,-5,2],[9,-6,8,7,5,9,6,-3,-2,-7,-6,7],[-8,-10,1,-2,-3,-3,2,-6,-3,3,3,-8],[-4,-2,-1,-2,6,-1,1,7,4,6,-10,-4],[-7,4,6,-9,-6,1,-9,-6,5,2,-1,-4],[1,-4,4,5,7,-5,1,3,6,5,-9,10],[8,-1,-5,7,-7,-8,-9,6,4,10,5,3],[9,9,-10,-3,-5,9,-1,3,-5,3,-3,9],[10,3,5,9,5,-2,-6,-3,-9,-10,-7,2]],[[-5,-8,-2,8,-8,-7,8,-7,-3,7,-3,-2],[-1,7,-5,-1,-2,9,-8,5,-7,-7,10,7],[2,-5,-2,-1,9,-4,5,-5,4,2,-2,-8],[-1,5,10,5,5,10,6,2,-7,10,-2,8],[10,10,7,2,-4,9,8,-7,-5,10,-6,5],[-1,-5,9,-10,3,2,7,-10,-10,6,-5,10],[-10,9,5,1,-10,-8,2,-9,-8,-5,-4,10],[3,1,9,-8,-2,-8,3,-4,6,4,-9,-2],[-4,4,3,-2,-9,4,4,10,-9,4,8,6],[9,-3,-5,-5,-4,-6,2,3,3,-1,9,3]],[[-10,9,7,3,7,2,2,10,-8,-5,6,-4],[-7,-6,-6,6,9,5,3,2,5,10,3,5],[8,-4,10,-5,-2,-5,1,-6,7,6,9,-9],[-4,-4,-1,-8,1,-5,-9,9,-3,-2,6,-7],[-9,-4,-1,-7,-6,-1,9,7,-1,-10,3,2],[4,10,-1,-4,10,-1,2,7,8,-4,7,-9],[-4,-1,-10,4,-8,-5,-1,-1,6,-3,1,-6],[-10,-8,-10,7,5,2,4,1,-10,3,5,4],[10,-10,9,-2,6,6,-6,-1,-3,-6,7,-9],[4,-8,-7,-10,2,-8,8,10,1,-2,-10,-7]],[[8,-2,-3,-3,4,-5,4,10,9,-6,9,3],[-1,6,-1,-4,6,-3,-8,7,-6,5,-10,-7],[-2,-8,-9,2,7,1,8,-5,1,5,-4,1],[5,-1,8,3,-1,2,1,7,-9,6,-4,-4],[-10,-6,9,4,1,8,3,1,4,3,-9,-5],[-1,-8,3,1,8,8,5,1,9,-7,-3,-8],[4,-2,4,-1,-10,1,10,-9,-9,6,-10,10],[-8,-4,7,-8,5,-4,-7,5,6,3,10,-4],[10,5,-9,-1,-3,-8,7,1,-5,-3,10,2],[-4,1,6,4,-5,5,-5,-9,-1,9,4,-4]],[[-5,-3,-4,2,-9,-3,6,10,6,5,2,-10],[-4,5,-8,-9,3,-7,-9,5,2,3,-5,1],[-8,5,-2,-5,3,-4,-6,-4,-5,5,2,1],[10,-3,-7,-8,-3,-7,7,1,9,-3,-8,-5],[1,-6,2,8,3,6,-8,-7,7,-7,-3,6],[-6,8,-7,-9,-2,3,4,3,3,-7,4,-3],[9,5,10,5,-10,4,-5,8,-7,1,-2,-9],[4,9,4,-8,2,5,5,-2,5,4,8,-9],[-7,-8,-5,-6,-5,-8,7,-9,1,4,6,-1],[-1,-2,1,4,2,-8,1,9,-1,4,-4,8]],[[9,-1,10,-7,-1,8,10,9,-5,10,-1,1],[-5,9,-10,-5,10,5,10,-1,-8,-2,-2,-10],[-9,3,7,-3,9,-4,-10,-7,6,2,-1,-6],[1,-7,2,10,-8,-3,-6,-9,-10,-3,3,3],[-9,5,8,-1,3,4,7,-7,8,2,-6,-1],[6,-7,6,-10,6,7,1,5,-7,-9,4,3],[-6,7,8,6,-4,6,-4,-4,-4,-4,-10,6],[9,-4,-1,-4,4,9,-9,-7,-8,2,-9,-2],[-9,7,7,-9,-1,7,1,-9,3,6,-2,7],[-8,-2,7,-2,-10,8,-2,-2,-3,5,2,-9]],[[-3,-9,10,5,-6,6,10,-2,9,-6,8,-4],[-10,-4,-6,-9,8,3,5,7,-6,-5,-3,7],[-8,2,2,6,8,4,3,-2,3,-8,-5,10],[-7,6,-1,-9,7,-4,7,2,-9,9,2,-2],[9,3,-6,3,-9,3,-3,8,4,-10,-3,-8],[3,-6,-1,9,-10,-1,-9,-8,-5,-8,-3,-10],[-10,2,5,6,9,2,-10,-7,-7,-5,-5,3],[-5,-8,-7,7,-1,3,-9,3,-10,-8,-9,-3],[5,3,2,-10,6,7,-8,-5,5,6,-6,2],[5,-8,-4,1,10,9,-9,-1,9,-2,-4,8]],[[2,3,-3,6,4,-2,-7,-10,-6,-1,8,-4],[1,5,-3,-7,5,5,-7,-5,6,-1,-2,-2],[-10,5,-4,-6,-7,2,-6,-6,-1,10,-3,8],[4,-4,10,5,8,9,-1,9,-10,7,-2,-6],[8,-10,2,-2,-7,5,2,-7,-1,4,-3,-1],[8,8,3,-4,1,1,9,-2,-2,6,-6,-6],[-1,-1,5,-9,2,-4,3,-7,9,-10,3,-9],[-6,1,-7,-10,-1,-5,7,-1,3,-5,1,-1],[-1,-3,2,1,6,-1,-1,3,6,-8,4,-1],[5,3,9,8,-4,6,4,3,1,3,9,-6]]], dtype = "int32")#candidate|5971|(12, 10, 12)|const|int32
bop_5972 = relay.not_equal(var_5970.astype('bool'), relay.reshape(const_5971.astype('bool'), relay.shape_of(var_5970))) # shape=(12, 10, 12)
output = relay.Tuple([bop_5972,])
output2 = relay.Tuple([bop_5972,])
func_5981 = relay.Function([var_5970,], output)
mod['func_5981'] = func_5981
mod = relay.transform.InferType()(mod)
mutated_mod['func_5981'] = func_5981
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5982 = relay.var("var_5982", dtype = "int32", shape = (12, 10, 12))#candidate|5982|(12, 10, 12)|var|int32
func_5981_call = mutated_mod.get_global_var('func_5981')
call_5983 = func_5981_call(var_5982)
output = call_5983
func_5984 = relay.Function([var_5982], output)
mutated_mod['func_5984'] = func_5984
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1719_call = mod.get_global_var('func_1719')
func_1720_call = mutated_mod.get_global_var('func_1720')
call_6018 = relay.TupleGetItem(func_1719_call(), 1)
call_6019 = relay.TupleGetItem(func_1720_call(), 1)
output = relay.Tuple([call_6018,])
output2 = relay.Tuple([call_6019,])
func_6061 = relay.Function([], output)
mod['func_6061'] = func_6061
mod = relay.transform.InferType()(mod)
mutated_mod['func_6061'] = func_6061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6061_call = mutated_mod.get_global_var('func_6061')
call_6062 = func_6061_call()
output = call_6062
func_6063 = relay.Function([], output)
mutated_mod['func_6063'] = func_6063
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3073_call = mod.get_global_var('func_3073')
func_3075_call = mutated_mod.get_global_var('func_3075')
call_6214 = relay.TupleGetItem(func_3073_call(), 0)
call_6215 = relay.TupleGetItem(func_3075_call(), 0)
output = call_6214
output2 = call_6215
func_6222 = relay.Function([], output)
mod['func_6222'] = func_6222
mod = relay.transform.InferType()(mod)
mutated_mod['func_6222'] = func_6222
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6222_call = mutated_mod.get_global_var('func_6222')
call_6223 = func_6222_call()
output = call_6223
func_6224 = relay.Function([], output)
mutated_mod['func_6224'] = func_6224
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5852_call = mod.get_global_var('func_5852')
func_5854_call = mutated_mod.get_global_var('func_5854')
call_6265 = func_5852_call()
call_6266 = func_5852_call()
output = call_6265
output2 = call_6266
func_6285 = relay.Function([], output)
mod['func_6285'] = func_6285
mod = relay.transform.InferType()(mod)
mutated_mod['func_6285'] = func_6285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6285_call = mutated_mod.get_global_var('func_6285')
call_6286 = func_6285_call()
output = call_6286
func_6287 = relay.Function([], output)
mutated_mod['func_6287'] = func_6287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2936_call = mod.get_global_var('func_2936')
func_2937_call = mutated_mod.get_global_var('func_2937')
call_6340 = relay.TupleGetItem(func_2936_call(), 0)
call_6341 = relay.TupleGetItem(func_2937_call(), 0)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_6342 = relay.TupleGetItem(func_3508_call(), 3)
call_6343 = relay.TupleGetItem(func_3510_call(), 3)
bop_6348 = relay.maximum(call_6342.astype('int32'), relay.reshape(call_6340.astype('int32'), relay.shape_of(call_6342))) # shape=(5, 11, 4)
bop_6351 = relay.maximum(call_6343.astype('int32'), relay.reshape(call_6341.astype('int32'), relay.shape_of(call_6343))) # shape=(5, 11, 4)
output = relay.Tuple([bop_6348,])
output2 = relay.Tuple([bop_6351,])
func_6354 = relay.Function([], output)
mod['func_6354'] = func_6354
mod = relay.transform.InferType()(mod)
output = func_6354()
func_6355 = relay.Function([], output)
mutated_mod['func_6355'] = func_6355
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_6364 = relay.TupleGetItem(func_684_call(), 0)
call_6365 = relay.TupleGetItem(func_686_call(), 0)
func_2900_call = mod.get_global_var('func_2900')
func_2902_call = mutated_mod.get_global_var('func_2902')
call_6375 = relay.TupleGetItem(func_2900_call(), 1)
call_6376 = relay.TupleGetItem(func_2902_call(), 1)
func_5693_call = mod.get_global_var('func_5693')
func_5694_call = mutated_mod.get_global_var('func_5694')
call_6378 = relay.TupleGetItem(func_5693_call(), 0)
call_6379 = relay.TupleGetItem(func_5694_call(), 0)
output = relay.Tuple([call_6364,call_6375,call_6378,])
output2 = relay.Tuple([call_6365,call_6376,call_6379,])
func_6405 = relay.Function([], output)
mod['func_6405'] = func_6405
mod = relay.transform.InferType()(mod)
mutated_mod['func_6405'] = func_6405
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6405_call = mutated_mod.get_global_var('func_6405')
call_6406 = func_6405_call()
output = call_6406
func_6407 = relay.Function([], output)
mutated_mod['func_6407'] = func_6407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_6418 = relay.TupleGetItem(func_684_call(), 0)
call_6419 = relay.TupleGetItem(func_686_call(), 0)
output = relay.Tuple([call_6418,])
output2 = relay.Tuple([call_6419,])
func_6429 = relay.Function([], output)
mod['func_6429'] = func_6429
mod = relay.transform.InferType()(mod)
mutated_mod['func_6429'] = func_6429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mutated_mod.get_global_var('func_6429')
call_6430 = func_6429_call()
output = call_6430
func_6431 = relay.Function([], output)
mutated_mod['func_6431'] = func_6431
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5623_call = mod.get_global_var('func_5623')
func_5624_call = mutated_mod.get_global_var('func_5624')
call_6435 = relay.TupleGetItem(func_5623_call(), 1)
call_6436 = relay.TupleGetItem(func_5624_call(), 1)
func_480_call = mod.get_global_var('func_480')
func_482_call = mutated_mod.get_global_var('func_482')
call_6439 = func_480_call()
call_6440 = func_480_call()
func_5877_call = mod.get_global_var('func_5877')
func_5879_call = mutated_mod.get_global_var('func_5879')
call_6446 = relay.TupleGetItem(func_5877_call(), 0)
call_6447 = relay.TupleGetItem(func_5879_call(), 0)
output = relay.Tuple([call_6435,call_6439,call_6446,])
output2 = relay.Tuple([call_6436,call_6440,call_6447,])
func_6453 = relay.Function([], output)
mod['func_6453'] = func_6453
mod = relay.transform.InferType()(mod)
output = func_6453()
func_6454 = relay.Function([], output)
mutated_mod['func_6454'] = func_6454
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_6547 = relay.TupleGetItem(func_4208_call(), 0)
call_6548 = relay.TupleGetItem(func_4210_call(), 0)
func_182_call = mod.get_global_var('func_182')
func_186_call = mutated_mod.get_global_var('func_186')
var_6573 = relay.var("var_6573", dtype = "int32", shape = ())#candidate|6573|()|var|int32
const_6574 = relay.const([-8,5,4,-9,-7,3,-8,3,6,10,7,-3,3,-2,-5,-4,-1,-2,-9,6,-1,-1,2,1,-7,5,8,4,10,-6,5,5,-7,3,-9,5,9,-10,-2,-10,3,5,-5,-3,-7,7,9,7], dtype = "int32")#candidate|6574|(48,)|const|int32
call_6572 = relay.TupleGetItem(func_182_call(relay.reshape(var_6573.astype('int32'), []), relay.reshape(const_6574.astype('int32'), [1, 6, 8]), ), 0)
call_6575 = relay.TupleGetItem(func_186_call(relay.reshape(var_6573.astype('int32'), []), relay.reshape(const_6574.astype('int32'), [1, 6, 8]), ), 0)
uop_6580 = relay.log10(call_6572.astype('float32')) # shape=(1, 6, 8)
uop_6582 = relay.log10(call_6575.astype('float32')) # shape=(1, 6, 8)
output = relay.Tuple([call_6547,var_6573,const_6574,uop_6580,])
output2 = relay.Tuple([call_6548,var_6573,const_6574,uop_6582,])
func_6585 = relay.Function([var_6573,], output)
mod['func_6585'] = func_6585
mod = relay.transform.InferType()(mod)
var_6586 = relay.var("var_6586", dtype = "int32", shape = ())#candidate|6586|()|var|int32
output = func_6585(var_6586)
func_6587 = relay.Function([var_6586], output)
mutated_mod['func_6587'] = func_6587
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3993_call = mod.get_global_var('func_3993')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_6592 = func_3993_call()
call_6593 = func_3993_call()
output = relay.Tuple([call_6592,])
output2 = relay.Tuple([call_6593,])
func_6611 = relay.Function([], output)
mod['func_6611'] = func_6611
mod = relay.transform.InferType()(mod)
output = func_6611()
func_6612 = relay.Function([], output)
mutated_mod['func_6612'] = func_6612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3537_call = mod.get_global_var('func_3537')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_6661 = relay.TupleGetItem(func_3537_call(), 0)
call_6662 = relay.TupleGetItem(func_3539_call(), 0)
var_6672 = relay.var("var_6672", dtype = "float64", shape = (7, 4, 7))#candidate|6672|(7, 4, 7)|var|float64
bop_6673 = relay.bitwise_or(call_6661.astype('int32'), relay.reshape(var_6672.astype('int32'), relay.shape_of(call_6661))) # shape=(7, 4, 7)
bop_6676 = relay.bitwise_or(call_6662.astype('int32'), relay.reshape(var_6672.astype('int32'), relay.shape_of(call_6662))) # shape=(7, 4, 7)
output = bop_6673
output2 = bop_6676
func_6678 = relay.Function([var_6672,], output)
mod['func_6678'] = func_6678
mod = relay.transform.InferType()(mod)
mutated_mod['func_6678'] = func_6678
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6679 = relay.var("var_6679", dtype = "float64", shape = (7, 4, 7))#candidate|6679|(7, 4, 7)|var|float64
func_6678_call = mutated_mod.get_global_var('func_6678')
call_6680 = func_6678_call(var_6679)
output = call_6680
func_6681 = relay.Function([var_6679], output)
mutated_mod['func_6681'] = func_6681
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2900_call = mod.get_global_var('func_2900')
func_2902_call = mutated_mod.get_global_var('func_2902')
call_6747 = relay.TupleGetItem(func_2900_call(), 1)
call_6748 = relay.TupleGetItem(func_2902_call(), 1)
output = call_6747
output2 = call_6748
func_6759 = relay.Function([], output)
mod['func_6759'] = func_6759
mod = relay.transform.InferType()(mod)
output = func_6759()
func_6760 = relay.Function([], output)
mutated_mod['func_6760'] = func_6760
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6761 = relay.var("var_6761", dtype = "uint64", shape = (15, 4, 13))#candidate|6761|(15, 4, 13)|var|uint64
var_6762 = relay.var("var_6762", dtype = "uint64", shape = (15, 4, 13))#candidate|6762|(15, 4, 13)|var|uint64
bop_6763 = relay.maximum(var_6761.astype('uint64'), relay.reshape(var_6762.astype('uint64'), relay.shape_of(var_6761))) # shape=(15, 4, 13)
output = bop_6763
output2 = bop_6763
func_6766 = relay.Function([var_6761,var_6762,], output)
mod['func_6766'] = func_6766
mod = relay.transform.InferType()(mod)
var_6767 = relay.var("var_6767", dtype = "uint64", shape = (15, 4, 13))#candidate|6767|(15, 4, 13)|var|uint64
var_6768 = relay.var("var_6768", dtype = "uint64", shape = (15, 4, 13))#candidate|6768|(15, 4, 13)|var|uint64
output = func_6766(var_6767,var_6768,)
func_6769 = relay.Function([var_6767,var_6768,], output)
mutated_mod['func_6769'] = func_6769
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6405_call = mod.get_global_var('func_6405')
func_6407_call = mutated_mod.get_global_var('func_6407')
call_6798 = relay.TupleGetItem(func_6405_call(), 1)
call_6799 = relay.TupleGetItem(func_6407_call(), 1)
output = relay.Tuple([call_6798,])
output2 = relay.Tuple([call_6799,])
func_6802 = relay.Function([], output)
mod['func_6802'] = func_6802
mod = relay.transform.InferType()(mod)
mutated_mod['func_6802'] = func_6802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6802_call = mutated_mod.get_global_var('func_6802')
call_6803 = func_6802_call()
output = call_6803
func_6804 = relay.Function([], output)
mutated_mod['func_6804'] = func_6804
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3128_call = mod.get_global_var('func_3128')
func_3129_call = mutated_mod.get_global_var('func_3129')
call_6818 = relay.TupleGetItem(func_3128_call(), 0)
call_6819 = relay.TupleGetItem(func_3129_call(), 0)
func_1925_call = mod.get_global_var('func_1925')
func_1927_call = mutated_mod.get_global_var('func_1927')
call_6853 = relay.TupleGetItem(func_1925_call(), 0)
call_6854 = relay.TupleGetItem(func_1927_call(), 0)
output = relay.Tuple([call_6818,call_6853,])
output2 = relay.Tuple([call_6819,call_6854,])
func_6857 = relay.Function([], output)
mod['func_6857'] = func_6857
mod = relay.transform.InferType()(mod)
output = func_6857()
func_6858 = relay.Function([], output)
mutated_mod['func_6858'] = func_6858
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3846_call = mod.get_global_var('func_3846')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_6961 = func_3846_call()
call_6962 = func_3846_call()
uop_6966 = relay.cos(call_6961.astype('float32')) # shape=(12, 7, 14)
uop_6968 = relay.cos(call_6962.astype('float32')) # shape=(12, 7, 14)
bop_6972 = relay.minimum(uop_6966.astype('float32'), relay.reshape(call_6961.astype('float32'), relay.shape_of(uop_6966))) # shape=(12, 7, 14)
bop_6975 = relay.minimum(uop_6968.astype('float32'), relay.reshape(call_6962.astype('float32'), relay.shape_of(uop_6968))) # shape=(12, 7, 14)
output = relay.Tuple([bop_6972,])
output2 = relay.Tuple([bop_6975,])
func_6986 = relay.Function([], output)
mod['func_6986'] = func_6986
mod = relay.transform.InferType()(mod)
output = func_6986()
func_6987 = relay.Function([], output)
mutated_mod['func_6987'] = func_6987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4146_call = mod.get_global_var('func_4146')
func_4147_call = mutated_mod.get_global_var('func_4147')
call_7003 = func_4146_call()
call_7004 = func_4146_call()
func_1824_call = mod.get_global_var('func_1824')
func_1828_call = mutated_mod.get_global_var('func_1828')
var_7011 = relay.var("var_7011", dtype = "uint16", shape = (847,))#candidate|7011|(847,)|var|uint16
call_7010 = relay.TupleGetItem(func_1824_call(relay.reshape(var_7011.astype('uint16'), [11, 11, 7]), relay.reshape(var_7011.astype('uint16'), [11, 11, 7]), ), 1)
call_7012 = relay.TupleGetItem(func_1828_call(relay.reshape(var_7011.astype('uint16'), [11, 11, 7]), relay.reshape(var_7011.astype('uint16'), [11, 11, 7]), ), 1)
const_7020 = relay.const([6,9,-2,-5,-1,2,-6,5,-3,4,1,6,3,1,-10,-3,6,2,-1,10,6,9,6,9,-2,-3,-1,8,6,5,2,4,2,-7,-1,-4,-3,-8,8,10,-10,-4,3,-7,3,-5,-10,2,-3,2,8,-10,10,1,5,9,-6,8,-4,10,-5,-2,-4,-6,5,-2,5,-5,-1,-4,-8,4,3,-5,5,4,-10,6,1,4,9,9,1,-8,10,1,-2,-4,-6,-1,6,-2,2,-4,-9,8,-4,9,-1,-8,-8,1,-3,-4,7,10,1,-2,10,-7,-4,-7,4,-4,5,-7,10,-5,-4,3,-6,-5,-7,-1,2,-7,3,-7,-10,-1,2,7,6,8,-1,-1,4,-4,-2,-9,5,3,8,6,-10,2,-6,5,-1,4,-1,-10,1,-7,1,9,2,3,-1,-7,-5,-2,-9,3,-7,-5,1,7,-9,5,10,3,6,-1,4,-8,8,2,-7,1,-3,4,10,-8,-6,9,8,8,-2,5,-9,-7,-2,-6,5,5,-2,3,-2,2,-5,8,7,-9,6,-6,-6,-2,3,9,3,-5,-7,-8,-1,-9,-5,10,-2,2,-5,-3,-3,-1,-10,4,6,-10,-10,-4,-3,7,-1,-10,8,-2,-10,1,-7,10,5,-5,-3,-4,5,6,-2,-6,8,7,-9,8,-2,-5,-1,10,-8,7,-10,-6,10,3,-3,-6,-4,-8,1,-4,-4,4,3,3,9,-3,-2,5,1,7,-6,8,5,-5,-1,-9,-8,-2,9,10,-7,8,-4,-3,-1,-2,3,-7,7,3,10,4,-7,7,-4,-5,-2,10,7,4,4,-7,5,3,5,-1,-10,-3,3,-4,-10,8,3,9,-1,-8,-8,-2,-8,-6,-3,-1,2,-1,-5,2,3,7,-7,-5,-1,3,-9,-4,-10,-1,-9,-5,8,8,10,-1,1,8,-6,8,6,-7,-6,2,-3,-10,-7,5,-2,1,4,-6,9,3,-7,-3,2,-7,-2,8,-4,-8,-3,8,-8,9,2,7,9,7,2,-6,1,-7,-4,6,3,-1,-9,-4,-10,8,-8,1,8,-1,9,7,3,-3,-8,3,5,8,2,2,4,-2,-9,-8,-5,7,6,-6,-9,6,-7,9,-4,9,-8,8,3,2,6,-8,9,-5,-9,-4,9,6,-8,2,-1,-7,-2,-10,-6,-8,2,-1,9,-6,8,-7,-9,-5,-5,8,-7,-4,2,5,-6,-10,7,9,-9,4,-2,-2,-3,7,-3,-5,-2,9,-5,-1,5,1,-3,8,5,7,5,10,8,8,-4,10,-4,-9,-3,-1,-10,-10,3,4,2,-7,3,-6,5,-2,9,-5,1,3,6,2,-8,-10,-2,1,6,-2,-5,9,4,-9,5,9,1,2,8,3,8,-9,8,4,-5,-4,-9,-10,-6,8,-6,7,-9,-3,3,-2,-1,-1,10,4,4,-8,3,-7,-9,-10,4,-2,-6,-1,-3,10,-6,5,-6,1,-9,4,9,10,-6,2,-10,4,-1,7,-8,10,-7,9,-5,5,3,5,1,-9,8,9,-8,-7,8,5,-10,1,1,5,4,2,-9,9,-4,1,2,3,-4,8,-4,-9,9,4,-4,8,8,5,-8,-9,5,-6,9,6,8,5,-9,6,6,10,10,-10,-1,-8,-1,1,9,2,7,-1,-4,-8,-3,-2,6,-9,-3,7,-3,-3,3,2,-1,10,-4,2,-9,2,-5,-1,8,9,10,-5,2,9,2,-9,-8,1,-4,-10,5,5,6,-3,7,-8,-10,1,-3,-9,-4,9,9,-1,-7,6,-3,-2,-8,-7,-6,1,10,-10,-2,1,9,-5,-2,-1,-9,8,7,-5,4,-9,7,-10,2,3,1,10,-3,-8,5,-1,6,8,-1,8,5,10,7,-10,-2,-5,-6,-10,-1,-2,-8,9,-6,9,10,-5,-5,8,4,1,2,8,-10,-6,7,-5,3,-10,3,-6,-7,1,-7,3,8,9,1,-9,-6,-4,-5,9,-5,8,-10,-4,-7,-8,3,-6,-7,-2,-2,1,-9,10,-4,-5,10,8,10,-7,-6,-3,-6,9,-4,4,-3,4,2,8,-5,-8,6,4,-7,-5,6,1,7,-5,-2,-8,8,8,6,-7,-7,-5,-10,-9,10,1,1,7,-1,-2,-3,-7,-2,10,-9,10,-1,-8,-4,9,2,9,1,3,10,4,-6,2,-8,-10,9,-4,3,-1,-1,-2,-10,6,8,-5,5,-2,2,2,8,8,10,-8,-4], dtype = "uint16")#candidate|7020|(847,)|const|uint16
bop_7021 = relay.multiply(var_7011.astype('int16'), relay.reshape(const_7020.astype('int16'), relay.shape_of(var_7011))) # shape=(847,)
func_2294_call = mod.get_global_var('func_2294')
func_2295_call = mutated_mod.get_global_var('func_2295')
call_7033 = func_2294_call()
call_7034 = func_2294_call()
func_5369_call = mod.get_global_var('func_5369')
func_5373_call = mutated_mod.get_global_var('func_5373')
var_7059 = relay.var("var_7059", dtype = "float64", shape = (330,))#candidate|7059|(330,)|var|float64
const_7060 = relay.const([-9,8,-10,9,9,-4,-8,7,-10,2,9,6,7,-6,3,9,-6,-7,1,8,5,-4,-8,8,4,-5,3,2,-9,5,4,3,-3,10,6,2,9,6,-9,-7,-6,7,6,-1,10,8,-2,-5,3,8,5,-5,-8,-2,-5,3,3,-3,9,-7,-2,2,8,-10,5,10,-8,4,6,-6,-7,4,-6,1,1,-6,-3,-6,6,-1,1,-2,-6,6,2,-5,-10,-1,4,-4,1,7,-8,6,8,-6,-9,-10,5,-1,8,6,-2,6,10,-2,-10,7,-9,-2,10,-6,6,-8,-3,-8,2,1,-2,4,7,-2,-3,4,2,1,-6,5,-4,-5,-1,-10,-8,8,9,1,-8,-2,-4,4,-4,1,1,-4,-6,-2,3,-9,2,-2,-1,-7,-7,-1,9,10,8,5,-5,2,9,10,7,-4,9,2,-10,1,9,-10,-5,4,-2,-3,-10,-2,-1,3,-2,-7,-5,-2,-5,2,-7,4,3,-5,7,-5,3,7], dtype = "int16")#candidate|7060|(192,)|const|int16
call_7058 = relay.TupleGetItem(func_5369_call(relay.reshape(var_7059.astype('float64'), [6, 5, 11]), relay.reshape(const_7060.astype('int16'), [192,]), ), 5)
call_7061 = relay.TupleGetItem(func_5373_call(relay.reshape(var_7059.astype('float64'), [6, 5, 11]), relay.reshape(const_7060.astype('int16'), [192,]), ), 5)
output = relay.Tuple([call_7003,call_7010,bop_7021,call_7033,call_7058,var_7059,const_7060,])
output2 = relay.Tuple([call_7004,call_7012,bop_7021,call_7034,call_7061,var_7059,const_7060,])
func_7062 = relay.Function([var_7011,var_7059,], output)
mod['func_7062'] = func_7062
mod = relay.transform.InferType()(mod)
mutated_mod['func_7062'] = func_7062
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7062_call = mutated_mod.get_global_var('func_7062')
var_7064 = relay.var("var_7064", dtype = "uint16", shape = (847,))#candidate|7064|(847,)|var|uint16
var_7065 = relay.var("var_7065", dtype = "float64", shape = (330,))#candidate|7065|(330,)|var|float64
call_7063 = func_7062_call(var_7064,var_7065,)
output = call_7063
func_7066 = relay.Function([var_7064,var_7065,], output)
mutated_mod['func_7066'] = func_7066
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1072_call = mod.get_global_var('func_1072')
func_1073_call = mutated_mod.get_global_var('func_1073')
call_7078 = func_1072_call()
call_7079 = func_1072_call()
output = call_7078
output2 = call_7079
func_7098 = relay.Function([], output)
mod['func_7098'] = func_7098
mod = relay.transform.InferType()(mod)
mutated_mod['func_7098'] = func_7098
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7098_call = mutated_mod.get_global_var('func_7098')
call_7099 = func_7098_call()
output = call_7099
func_7100 = relay.Function([], output)
mutated_mod['func_7100'] = func_7100
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3508_call = mod.get_global_var('func_3508')
func_3510_call = mutated_mod.get_global_var('func_3510')
call_7101 = relay.TupleGetItem(func_3508_call(), 1)
call_7102 = relay.TupleGetItem(func_3510_call(), 1)
func_629_call = mod.get_global_var('func_629')
func_633_call = mutated_mod.get_global_var('func_633')
var_7129 = relay.var("var_7129", dtype = "float32", shape = (98,))#candidate|7129|(98,)|var|float32
call_7128 = relay.TupleGetItem(func_629_call(relay.reshape(call_7101.astype('float32'), []), relay.reshape(var_7129.astype('float32'), [14, 7, 1]), ), 0)
call_7130 = relay.TupleGetItem(func_633_call(relay.reshape(call_7101.astype('float32'), []), relay.reshape(var_7129.astype('float32'), [14, 7, 1]), ), 0)
output = relay.Tuple([call_7101,call_7128,var_7129,])
output2 = relay.Tuple([call_7102,call_7130,var_7129,])
func_7142 = relay.Function([var_7129,], output)
mod['func_7142'] = func_7142
mod = relay.transform.InferType()(mod)
var_7143 = relay.var("var_7143", dtype = "float32", shape = (98,))#candidate|7143|(98,)|var|float32
output = func_7142(var_7143)
func_7144 = relay.Function([var_7143], output)
mutated_mod['func_7144'] = func_7144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1925_call = mod.get_global_var('func_1925')
func_1927_call = mutated_mod.get_global_var('func_1927')
call_7168 = relay.TupleGetItem(func_1925_call(), 0)
call_7169 = relay.TupleGetItem(func_1927_call(), 0)
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_7176 = func_526_call()
call_7177 = func_526_call()
func_5770_call = mod.get_global_var('func_5770')
func_5772_call = mutated_mod.get_global_var('func_5772')
const_7187 = relay.const([4,-9,-10,-1,-2,3,-2,-10,-9,-5,9,5,-10,3,-1,-3,8,8,-9,-8,-3,-1,-10,-10,-10,-9,-10,9,3,10,-8,3,-6,-3,7,6,-2,5,-9,-10,3,6,-6,-3,-8,-7,7,10,10,-10,7,-8,-4,1,-1,-10,2,6,-2,-7,2,-7,-3,-4,-2,-3,-10,-6,-6,-8,9,9,-8,7,6,10,-7,8,-6,6,-7,-7,-10,3,-1,10,3,-9,-6,10,-10,9,7,-1,2,-1,6,7,-10,-9,5,10,1,-6,-6,1,7,7,-9,-9,6,1,-7,-6,-1,7,-6,-4,6,8,-8,-2,-8,1,7,-8,9,7,-10,-4,-9,6,9,6,2,9,-10,-5,10,-6,3,4,-7,-9,-5,7,3,1,5,-7,-3,7,7,-2,7,8,5,-3,2,-9,-4,-10,10,-8,3,4,-2,-7,-2,-10,10,8,-7,-8,-4,5,-3,-2,8,-10,5,-5,4,8,3,-2,3,8,2,10,-5,1,-9,1,-4,6,-4,6,5,1,-1,10,-4,5,-6,-1,9,-9,6,6,10,1,3,1,3,-7,-6,10,7,7,2,6,-9,-10,4,8,9,9,9,1,3,-8,-5,10,-6,5,4,-1,-6,-1,8,4,1,9,-3,-1,8,-7,10,3,4,-5,-9,3,-1,6,6,-7,5,-4,-8,-7,6,7,3,3,-10,-8,-9,6,7,-9,4,-9,-2,7,10,6,10,-4,-3,-10,7,2,1,6,-10,1,1,-10,3,-4,-3,-10,4,-6,5,10,6,-10,9,-4,-10,-2,-7,5,4,-4,2,2,2,-2], dtype = "int32")#candidate|7187|(312,)|const|int32
call_7186 = relay.TupleGetItem(func_5770_call(relay.reshape(const_7187.astype('int32'), [13, 3, 8])), 1)
call_7188 = relay.TupleGetItem(func_5772_call(relay.reshape(const_7187.astype('int32'), [13, 3, 8])), 1)
output = relay.Tuple([call_7168,call_7176,call_7186,const_7187,])
output2 = relay.Tuple([call_7169,call_7177,call_7188,const_7187,])
func_7191 = relay.Function([], output)
mod['func_7191'] = func_7191
mod = relay.transform.InferType()(mod)
output = func_7191()
func_7192 = relay.Function([], output)
mutated_mod['func_7192'] = func_7192
mutated_mod = relay.transform.InferType()(mutated_mod)
const_7259 = relay.const([[[5,-9,8,-6,-9,6,-10,7,-1]],[[1,-3,6,-1,-2,-10,3,7,-2]],[[3,1,2,-10,-8,-6,6,-6,8]],[[-1,-4,-10,-6,-10,4,-5,-1,-8]],[[4,7,5,-3,-3,-9,3,-1,-5]],[[-1,-5,-1,6,-7,6,8,-3,2]],[[-10,-8,3,5,-9,3,9,-4,-9]],[[-5,-5,-10,8,-1,-4,-9,-7,9]],[[-6,8,-3,1,6,-8,4,-10,6]],[[10,-9,-6,-3,9,-4,1,-5,9]]], dtype = "int16")#candidate|7259|(10, 1, 9)|const|int16
var_7260 = relay.var("var_7260", dtype = "int16", shape = (10, 1, 9))#candidate|7260|(10, 1, 9)|var|int16
bop_7261 = relay.not_equal(const_7259.astype('bool'), relay.reshape(var_7260.astype('bool'), relay.shape_of(const_7259))) # shape=(10, 1, 9)
output = bop_7261
output2 = bop_7261
func_7268 = relay.Function([var_7260,], output)
mod['func_7268'] = func_7268
mod = relay.transform.InferType()(mod)
mutated_mod['func_7268'] = func_7268
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7269 = relay.var("var_7269", dtype = "int16", shape = (10, 1, 9))#candidate|7269|(10, 1, 9)|var|int16
func_7268_call = mutated_mod.get_global_var('func_7268')
call_7270 = func_7268_call(var_7269)
output = call_7270
func_7271 = relay.Function([var_7269], output)
mutated_mod['func_7271'] = func_7271
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5667_call = mod.get_global_var('func_5667')
func_5669_call = mutated_mod.get_global_var('func_5669')
call_7292 = relay.TupleGetItem(func_5667_call(), 0)
call_7293 = relay.TupleGetItem(func_5669_call(), 0)
func_4458_call = mod.get_global_var('func_4458')
func_4460_call = mutated_mod.get_global_var('func_4460')
call_7294 = relay.TupleGetItem(func_4458_call(), 1)
call_7295 = relay.TupleGetItem(func_4460_call(), 1)
output = relay.Tuple([call_7292,call_7294,])
output2 = relay.Tuple([call_7293,call_7295,])
func_7297 = relay.Function([], output)
mod['func_7297'] = func_7297
mod = relay.transform.InferType()(mod)
output = func_7297()
func_7298 = relay.Function([], output)
mutated_mod['func_7298'] = func_7298
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5462_call = mod.get_global_var('func_5462')
func_5463_call = mutated_mod.get_global_var('func_5463')
call_7302 = func_5462_call()
call_7303 = func_5462_call()
func_5667_call = mod.get_global_var('func_5667')
func_5669_call = mutated_mod.get_global_var('func_5669')
call_7335 = relay.TupleGetItem(func_5667_call(), 0)
call_7336 = relay.TupleGetItem(func_5669_call(), 0)
func_6354_call = mod.get_global_var('func_6354')
func_6355_call = mutated_mod.get_global_var('func_6355')
call_7364 = relay.TupleGetItem(func_6354_call(), 0)
call_7365 = relay.TupleGetItem(func_6355_call(), 0)
func_3745_call = mod.get_global_var('func_3745')
func_3747_call = mutated_mod.get_global_var('func_3747')
call_7375 = relay.TupleGetItem(func_3745_call(), 0)
call_7376 = relay.TupleGetItem(func_3747_call(), 0)
output = relay.Tuple([call_7302,call_7335,call_7364,call_7375,])
output2 = relay.Tuple([call_7303,call_7336,call_7365,call_7376,])
func_7383 = relay.Function([], output)
mod['func_7383'] = func_7383
mod = relay.transform.InferType()(mod)
mutated_mod['func_7383'] = func_7383
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7383_call = mutated_mod.get_global_var('func_7383')
call_7384 = func_7383_call()
output = call_7384
func_7385 = relay.Function([], output)
mutated_mod['func_7385'] = func_7385
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3846_call = mod.get_global_var('func_3846')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_7407 = func_3846_call()
call_7408 = func_3846_call()
output = relay.Tuple([call_7407,])
output2 = relay.Tuple([call_7408,])
func_7414 = relay.Function([], output)
mod['func_7414'] = func_7414
mod = relay.transform.InferType()(mod)
mutated_mod['func_7414'] = func_7414
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7414_call = mutated_mod.get_global_var('func_7414')
call_7415 = func_7414_call()
output = call_7415
func_7416 = relay.Function([], output)
mutated_mod['func_7416'] = func_7416
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4533_call = mod.get_global_var('func_4533')
func_4534_call = mutated_mod.get_global_var('func_4534')
call_7490 = relay.TupleGetItem(func_4533_call(), 3)
call_7491 = relay.TupleGetItem(func_4534_call(), 3)
func_5732_call = mod.get_global_var('func_5732')
func_5734_call = mutated_mod.get_global_var('func_5734')
call_7503 = func_5732_call()
call_7504 = func_5732_call()
output = relay.Tuple([call_7490,call_7503,])
output2 = relay.Tuple([call_7491,call_7504,])
func_7510 = relay.Function([], output)
mod['func_7510'] = func_7510
mod = relay.transform.InferType()(mod)
output = func_7510()
func_7511 = relay.Function([], output)
mutated_mod['func_7511'] = func_7511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3846_call = mod.get_global_var('func_3846')
func_3847_call = mutated_mod.get_global_var('func_3847')
call_7566 = func_3846_call()
call_7567 = func_3846_call()
output = call_7566
output2 = call_7567
func_7581 = relay.Function([], output)
mod['func_7581'] = func_7581
mod = relay.transform.InferType()(mod)
mutated_mod['func_7581'] = func_7581
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7581_call = mutated_mod.get_global_var('func_7581')
call_7582 = func_7581_call()
output = call_7582
func_7583 = relay.Function([], output)
mutated_mod['func_7583'] = func_7583
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6453_call = mod.get_global_var('func_6453')
func_6454_call = mutated_mod.get_global_var('func_6454')
call_7602 = relay.TupleGetItem(func_6453_call(), 0)
call_7603 = relay.TupleGetItem(func_6454_call(), 0)
output = call_7602
output2 = call_7603
func_7604 = relay.Function([], output)
mod['func_7604'] = func_7604
mod = relay.transform.InferType()(mod)
output = func_7604()
func_7605 = relay.Function([], output)
mutated_mod['func_7605'] = func_7605
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_7678 = func_361_call()
call_7679 = func_361_call()
func_7098_call = mod.get_global_var('func_7098')
func_7100_call = mutated_mod.get_global_var('func_7100')
call_7680 = func_7098_call()
call_7681 = func_7098_call()
bop_7684 = relay.mod(call_7680.astype('float64'), relay.reshape(call_7678.astype('float64'), relay.shape_of(call_7680))) # shape=(5, 11, 4)
bop_7687 = relay.mod(call_7681.astype('float64'), relay.reshape(call_7679.astype('float64'), relay.shape_of(call_7681))) # shape=(5, 11, 4)
func_5693_call = mod.get_global_var('func_5693')
func_5694_call = mutated_mod.get_global_var('func_5694')
call_7697 = relay.TupleGetItem(func_5693_call(), 0)
call_7698 = relay.TupleGetItem(func_5694_call(), 0)
func_1344_call = mod.get_global_var('func_1344')
func_1346_call = mutated_mod.get_global_var('func_1346')
call_7707 = relay.TupleGetItem(func_1344_call(), 1)
call_7708 = relay.TupleGetItem(func_1346_call(), 1)
func_884_call = mod.get_global_var('func_884')
func_887_call = mutated_mod.get_global_var('func_887')
const_7711 = relay.const([2.652809,0.097976,7.794756,4.794221,8.616629,-9.916868,1.738943,6.872238,-0.620479,1.268096,4.497469,-6.666893,8.115543,7.887027,1.070434,-3.752786,-1.187743,3.831170,7.892831,7.918401,-4.520176,-2.602778,6.080078,-1.037620,7.007806,-5.447576,-8.270729,9.954209,5.898113,-9.499647,-9.703264,5.236246,7.135469,-6.306389,6.189216,5.427543,-5.833916,6.790754,5.468792,4.411877,-3.067010,-9.392276,-1.889115,-9.303728,-8.409285,-8.943326,5.458055,9.805147,-4.178499,-2.562870,-0.242749,2.595389,0.150827,-6.733201,-0.444599,-4.882490,3.465083,-0.723301,-6.920704,9.609719,8.979460,7.694902,-3.980640,5.018096,-2.355950,-6.198972,-8.733964,5.825592,5.317536,-8.126865,8.512901,-0.862118,5.577842,-6.912079,0.906672,-5.498453,2.663480,-8.176805,2.547387,2.303244,3.190395,-1.458631,8.973842,3.532023,8.223696,8.534406,-3.075598,-7.596857,-0.304528,1.326113,-2.743597,-0.918394,0.627115,7.307674,9.464421,1.457143,5.188391,-4.215165,0.150019,2.939267,5.576385,-2.875722,-5.080259,-2.058896,8.830713,-4.816503,4.325636,-6.648965,2.464743,6.175897,-7.278678,0.826423,-2.401346,-6.158976,-3.236649,6.548446,-2.351450,3.035924,-9.996581,5.754910,-4.023393,9.391981,3.861781,-8.781925,-5.499126,1.256220,-7.468908,-0.055351,-0.792031,2.146213,-6.838037,-3.327797,-9.968110,6.234823,6.871807,-3.871664,-2.088830,-1.968371,6.587110,0.737902,-4.892457,-9.943433,0.564438,-9.342781,-2.658765,-7.696385,-0.474159,8.153951,8.024165,6.884727,-8.904250,-9.995230,6.268607,-3.757214,0.472909,-3.520883,-0.957004,5.343242,9.716944,7.575352,7.502689,-9.661307,-7.032818,-9.518368,-9.713702,1.230970,5.527687,-4.711327,-0.053321,-9.259891,-2.336693,9.493953,1.792455,-1.681832,-4.803562,-0.212521,-8.635226,2.740381,8.605577,-5.875932,1.720026,-8.230641,9.741135,-8.655102,7.939669,3.893812,3.956429,-2.564528,5.757050,-3.229648,-6.559878,1.251060,8.851698,3.852683,-5.703555,4.661546], dtype = "float64")#candidate|7711|(196,)|const|float64
call_7710 = func_884_call(relay.reshape(const_7711.astype('float64'), [7, 4, 7]), relay.reshape(const_7711.astype('float64'), [7, 4, 7]), )
call_7712 = func_884_call(relay.reshape(const_7711.astype('float64'), [7, 4, 7]), relay.reshape(const_7711.astype('float64'), [7, 4, 7]), )
output = relay.Tuple([bop_7684,call_7697,call_7707,call_7710,const_7711,])
output2 = relay.Tuple([bop_7687,call_7698,call_7708,call_7712,const_7711,])
func_7725 = relay.Function([], output)
mod['func_7725'] = func_7725
mod = relay.transform.InferType()(mod)
mutated_mod['func_7725'] = func_7725
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7725_call = mutated_mod.get_global_var('func_7725')
call_7726 = func_7725_call()
output = call_7726
func_7727 = relay.Function([], output)
mutated_mod['func_7727'] = func_7727
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7740 = relay.var("var_7740", dtype = "float64", shape = (15, 14, 16))#candidate|7740|(15, 14, 16)|var|float64
const_7741 = relay.const([[[-6.230719,-9.680138,2.114975,-5.208838,-2.452357,2.297007,2.530012,-9.297188,-6.868062,9.122186,-0.948018,4.270227,8.562844,0.672176,-1.877159,-1.800798],[8.530720,3.883540,-0.153293,-3.924898,0.816896,9.896001,3.089522,1.409135,6.279318,6.058475,8.070846,2.670414,-0.146962,8.131697,5.039060,5.058899],[-1.803702,5.620839,-3.345306,-7.575372,8.912195,8.983060,9.129126,-1.515241,0.204663,-2.041867,-4.089527,2.234503,-5.291453,-7.345492,-9.609075,-0.782855],[-9.660604,8.050074,-1.319533,3.887143,-4.824319,-7.332875,6.135595,-4.686769,-2.740337,4.679480,-5.620137,3.669974,6.902486,-2.580056,-6.153255,-8.732000],[-9.277491,0.865248,5.860420,-4.606983,6.225213,-2.328530,-9.646100,7.083670,9.945152,3.927959,4.059279,1.089883,-5.323055,-1.260599,-2.017683,-4.462806],[5.080065,4.354014,-5.234472,-9.608329,7.482351,-0.285738,9.644858,-4.717492,-4.320357,9.709140,3.193667,-9.786288,-7.855248,-5.134611,6.129981,-7.880044],[-8.405686,-3.744931,9.560947,4.599452,1.650072,-6.993621,5.562029,3.884364,4.137340,-8.536643,7.480772,-5.869744,2.966245,4.497372,8.904139,1.414306],[9.590333,-1.133922,-3.780917,2.162852,7.520330,6.443629,7.012184,-3.812869,0.646828,3.574518,4.888603,-2.742980,-8.469815,-1.969388,4.157116,9.234829],[4.430928,-0.536868,2.599702,7.271788,7.750430,-3.411545,2.626609,1.709324,9.358852,-6.750188,5.580718,3.959717,-1.144447,4.802088,-7.234883,-7.056182],[1.111782,9.767593,9.561954,9.536472,6.921228,8.580720,9.643749,0.932894,5.911606,8.729385,7.015084,-1.990932,-7.600171,2.531152,-2.802783,-7.686999],[-7.258264,6.321362,-6.124640,7.444461,-4.799803,4.175177,9.806118,-5.991858,-3.123029,6.875109,-7.507712,4.387889,-9.873309,5.096443,-0.272778,-6.876054],[-3.207811,-8.571026,-0.569770,-5.616487,-7.687868,-5.633417,3.150698,-4.800272,7.158573,6.146441,9.883390,-0.057670,2.701602,0.602482,-4.485861,9.628026],[5.614079,4.054802,8.930202,-7.761370,8.773411,3.170910,4.887577,-2.234788,-2.319605,-4.505409,-6.807045,6.994741,3.077722,-3.798365,-7.035191,-9.840537],[1.398668,1.364727,2.542147,9.805042,2.579360,7.806159,-8.879732,2.069648,3.861211,8.518852,-6.491973,-3.184121,5.780429,2.839491,-4.131729,7.339039]],[[-2.924769,-9.070901,-9.449313,-3.597048,-9.030952,-4.851678,-5.622537,4.744368,3.312901,5.361293,9.927614,4.580154,-8.601116,-0.529011,-9.154593,9.395671],[3.734559,4.480648,6.689165,4.956788,1.984229,-6.519048,9.799111,-5.132575,-2.742331,-0.533966,4.136368,-7.521976,5.036174,-4.270320,-2.324209,-0.206599],[7.898568,2.976711,3.796022,-9.988800,-0.713443,-9.159782,3.793245,7.927055,4.323046,2.114135,8.703127,-9.175059,2.368957,1.120200,-2.022248,8.782761],[8.976300,-1.031042,6.998616,8.102894,-1.478809,2.401773,-8.669802,4.942921,-4.189576,-8.185833,0.648324,-3.808848,2.464481,-8.583071,7.105974,0.565373],[3.395964,-6.749277,1.610693,-3.455979,4.492289,4.393081,-0.261808,9.532520,2.001694,7.578786,0.370585,1.073017,5.644861,-8.235217,0.796535,0.813048],[-9.941882,2.256013,9.521433,1.237558,2.639865,2.333140,8.364281,6.630379,-4.458711,5.088697,-8.038763,5.564939,4.660437,2.628586,0.944521,3.850591],[-7.070709,1.905135,-8.583589,-8.752514,4.636210,-5.142780,9.021768,-2.099155,-3.385372,2.223243,-7.679574,-4.953211,-4.390422,4.924329,-1.016502,5.169326],[2.296847,-2.371094,8.795868,-4.607095,-4.971014,-2.868663,-7.478719,-3.518911,-0.144515,4.915492,-2.555329,-0.151749,6.377337,-0.168338,-6.313552,-2.096097],[5.378216,-9.369404,-1.187820,6.021409,2.409042,-6.854707,-7.790390,-7.082085,-4.173724,-0.800654,0.276988,2.129193,-6.182339,-8.803118,-6.101719,-4.580967],[0.243842,-8.099305,7.356235,6.224158,5.955094,-8.298147,-8.196996,3.573431,7.388972,6.877936,-2.623498,0.005654,-9.215550,-2.728582,8.343148,-4.312060],[2.011033,-5.599714,3.172887,4.515724,5.004076,-4.877903,-4.540694,-3.709257,0.480391,-5.608013,-2.166122,-1.649339,6.664402,8.967671,-3.961614,3.303527],[3.105323,-5.667338,5.332912,8.001687,-4.284108,-4.105406,1.374131,-8.105840,-2.489210,3.134020,-4.172868,-0.235502,-6.412193,-2.860618,7.575876,-1.503034],[5.200808,0.568207,-8.958631,6.080043,9.341376,3.252839,-0.785573,2.741843,-2.831540,-2.668438,8.035274,-3.191771,-4.001127,-0.885676,-6.468967,-6.425872],[0.817401,8.197685,7.870204,-3.564094,-8.789850,1.838218,5.553307,-7.164674,3.221029,6.136682,1.991918,-4.098617,-6.376542,5.269368,6.332188,0.468341]],[[-2.534415,-3.377423,0.785391,-5.382596,-1.334794,7.300959,-2.364176,1.269052,-4.612180,-6.378633,-1.390846,9.776505,9.645626,-2.695394,4.652860,-2.059144],[-4.426708,6.068103,1.473297,3.289070,7.551553,-5.108352,-6.201472,-4.734903,-6.712202,-3.551432,6.282625,1.295558,9.758170,-5.768923,6.566411,-5.300105],[5.009324,-5.338237,8.538670,1.221980,-9.045438,-1.743975,2.018180,4.648165,-7.181238,5.582723,7.059112,-3.861669,-9.129992,9.470777,5.599560,6.797080],[8.550959,-5.084467,1.854132,-1.628608,8.115240,3.075091,1.550369,-2.888440,-8.675219,2.222859,-7.145633,-4.112719,-2.069570,4.492007,1.503447,0.214649],[-9.043089,9.551227,1.105312,9.595428,6.175493,0.565275,7.108828,-2.035202,0.701162,9.466305,2.708217,-9.593087,-2.654638,-9.225038,-9.862880,-4.809774],[0.845472,5.989557,4.779791,4.003549,8.959749,0.688202,-6.302245,-4.893178,-6.343353,1.050087,-2.728705,7.276739,6.433078,-6.145002,0.460045,-2.213841],[6.249548,7.740160,-8.653782,5.504556,-3.232131,-4.656618,-8.331704,-3.759246,9.269481,-0.514666,-2.604666,-5.466042,9.659836,2.811917,0.546664,2.638166],[1.224098,-4.632456,5.454553,3.445571,-0.852414,-0.658557,5.056353,2.509097,5.808124,-9.096000,-8.673241,5.093225,3.013657,-5.159502,8.679493,0.520896],[7.047311,-1.109069,9.567873,-1.678516,-0.499146,-6.784826,9.835320,-6.274199,-1.127540,-8.185161,9.753175,-3.629083,6.349736,3.846368,5.618342,0.363419],[-3.523093,8.141691,-2.437310,-6.994833,4.636817,-4.283183,-0.965373,8.759738,9.829220,9.890315,4.312266,2.140930,9.239663,9.117285,-2.606193,8.875849],[2.506768,-1.146597,-3.757236,-3.632400,-9.260655,-9.503381,3.257968,8.181647,-8.690436,6.176007,-6.780273,-1.909822,1.206662,-4.887393,-7.098901,9.071219],[4.115446,1.133530,-5.523030,5.040900,-7.056482,1.693860,7.901572,-1.505597,-1.932241,0.556814,2.476730,-5.404023,-4.657913,-1.939068,-7.364588,-7.210809],[2.398312,5.816179,8.018093,-1.292831,-9.028286,0.921037,-1.777341,3.734412,5.612863,-6.006586,-4.125747,6.276759,8.050308,-9.446957,7.239162,3.536209],[-2.588174,-9.277447,0.304793,-7.303145,4.494508,5.031153,9.066050,-2.563292,-8.650872,2.203959,9.684922,4.341057,-7.530099,-9.645394,-9.133626,6.473670]],[[-6.225838,-2.539392,-0.962783,0.440918,-4.955376,-2.557681,-2.056822,-7.032498,0.307827,1.780256,-7.680987,7.511566,-2.087762,7.225818,-3.806665,-1.250947],[-2.472643,-0.777583,1.857957,-1.262580,8.757897,5.185841,1.352752,-9.473633,-0.268953,7.614583,-6.913841,4.161010,-9.298605,8.526344,0.370830,7.181243],[-5.818957,0.828721,-7.100581,0.769512,-9.704668,9.893922,-0.909964,-6.640603,9.407485,5.630289,-1.523584,4.356583,8.591255,7.706449,-0.971679,5.709605],[0.880868,-6.863020,-0.002031,0.694960,-1.413617,9.814819,-7.580338,0.994385,2.667375,0.206701,-7.020238,7.023066,3.368124,-0.692773,4.660852,-9.689926],[-8.102614,-8.245067,-8.301698,6.659511,-9.928376,5.698232,-3.046969,1.294379,6.770360,-8.402240,0.956858,-8.543012,-1.471401,-2.302730,-2.677811,-3.933565],[9.151034,9.640402,-1.867070,-5.708848,0.964762,9.739530,2.165052,-0.056109,4.674277,-5.233636,-1.482309,9.062420,5.955438,-0.932434,-6.401012,3.002940],[-4.557234,2.680879,6.556623,6.009230,5.283062,5.192955,7.794488,-3.223704,-1.729946,6.370174,7.914657,7.306822,-5.218870,-8.022679,1.725568,-9.502740],[-2.877347,-8.342205,-1.401182,1.157078,7.785161,-7.808515,-1.071408,3.026173,5.663044,9.537332,-2.770182,1.415875,-6.953568,8.249530,1.826827,4.633729],[-5.607643,-6.348222,-7.111087,-4.615799,-3.442646,-3.151023,1.542377,6.004974,1.674256,5.897116,3.183092,-1.894014,-1.997460,6.574003,-0.794511,-9.433544],[6.161535,9.620463,-7.055954,8.998176,-9.270946,8.513885,1.232280,-0.368456,1.642928,-3.569982,-4.760348,-1.032123,4.774112,0.750851,2.229984,-8.294673],[-2.266129,-9.725328,9.301951,4.221292,6.754394,-2.933274,7.206769,6.779099,-1.496800,5.828870,6.271274,-8.776255,-7.788650,-5.746586,7.326392,-7.744571],[-0.076478,-2.335843,-7.023345,4.782181,-5.952896,-9.013937,-7.910271,-8.693858,-7.702721,8.307147,5.358478,-5.240164,1.104107,5.009373,3.885349,-3.258555],[-0.510094,7.694140,-9.711815,6.305490,-6.656238,-6.618276,9.241570,-3.566409,5.601870,8.773829,0.552883,-5.082487,-5.790068,3.943975,3.928433,4.647056],[-5.020311,-8.331100,9.338102,8.047077,1.603603,-9.106706,-6.301335,-8.158462,7.582110,-3.309003,3.794422,5.812989,9.021260,4.456421,1.937103,-4.086344]],[[-4.245007,-6.629558,-1.315743,8.812811,-4.726670,1.061237,-6.999330,-3.351888,2.525002,-7.310332,4.848879,3.916980,-3.952297,3.964859,2.777105,7.696527],[-4.142512,-0.394032,2.831315,-9.606087,3.697494,-5.866454,-0.806978,3.962773,-0.125708,-2.450290,-8.320640,-6.175888,3.633967,-7.820760,0.324637,-8.302189],[3.431876,1.845927,-2.839400,-5.867841,8.049297,-8.986348,8.039965,2.277989,5.265973,6.531235,0.749427,2.976605,4.315234,-9.355282,7.504800,-2.145740],[8.130032,-0.732333,-0.411083,1.822516,5.074079,5.069903,-0.939035,-0.732038,-3.819871,9.582502,6.928638,-3.293624,-4.608536,-1.495781,4.843818,-3.239607],[-8.988884,1.864755,-7.677794,-8.599646,-0.521817,-3.417363,-8.234586,-0.427469,3.144233,4.958625,-0.162530,3.629199,-8.572775,4.845253,2.031458,-9.219817],[-7.209220,-4.454764,-1.252920,-2.056136,-9.467054,7.352378,-7.801143,2.155643,6.683676,-6.508154,9.830299,-3.651654,5.399493,9.851714,-1.527431,-2.333396],[6.642457,4.756101,0.322280,-8.672721,-4.889721,1.135467,-9.667071,-7.435774,3.175836,4.438508,0.259657,-7.024017,3.473023,8.549727,7.879721,-5.671227],[-5.696838,-5.926375,-0.989877,9.923683,3.112492,2.620448,2.758247,6.112412,-5.128836,2.733164,3.514688,7.315468,-7.778734,-7.665963,-2.600098,-5.310685],[-6.137263,0.664378,-4.999479,7.153309,7.582226,5.266615,8.512839,8.296560,1.139585,9.980298,-4.250859,-9.445507,8.709740,-2.988360,1.685747,-3.320601],[3.424212,-8.652688,-5.123373,7.074053,-5.227460,-0.445468,-4.996436,-0.967459,4.772384,-0.420647,-4.609915,-3.433976,0.729318,5.916388,3.995293,-4.594162],[3.741508,-7.722704,-4.064056,9.045520,-3.123914,-8.718545,8.974244,8.179811,-9.692422,-0.054500,-1.952958,-4.780276,9.975860,-9.103262,8.089702,-7.759847],[-3.234276,-2.838251,-1.313469,1.648774,-3.207421,3.483872,-1.437485,-1.812586,-8.792700,2.434074,1.984044,-9.613221,-2.710005,3.074684,1.552368,-2.497038],[6.049110,7.962301,1.453661,-0.916197,-4.948416,6.903591,-3.299444,-1.046768,0.611630,1.191672,6.830050,2.996292,4.207557,-0.500882,-1.854630,-9.151809],[2.367550,-4.022974,-5.035766,-9.350734,-4.663802,-0.686598,5.210909,-2.282076,-8.408951,9.657905,4.939329,0.607761,-7.678019,-2.547255,4.026561,-7.621311]],[[-7.265210,5.817808,0.272043,6.281617,8.455158,5.467132,-1.849330,3.873111,3.960810,5.964030,-2.694460,0.522271,-2.760096,8.682852,-7.502857,-5.118228],[-4.638331,-2.980675,-2.358437,-1.897985,9.545927,-6.600464,3.527026,-0.638563,3.338362,8.708637,5.116683,-1.244811,-4.491321,2.041210,1.499234,8.958187],[6.630689,1.867009,-2.738996,6.988582,4.523277,9.077721,-0.249545,-7.477354,6.918947,0.212259,-5.438879,-4.543269,7.866185,-4.658118,-8.430303,6.289824],[8.572143,7.197318,-0.769791,4.536164,-9.294128,-7.644228,-2.270086,-0.449319,-4.197512,-6.076777,5.490381,-9.299032,-7.768045,4.830135,-6.513147,-1.645524],[-7.399223,4.858469,1.700713,-0.480441,-3.721688,-8.180384,4.132537,-6.132041,-0.641282,6.732014,-7.331177,-9.624312,-4.295911,1.393106,-5.352155,-1.294786],[8.900298,7.348959,-7.254486,-6.923714,-0.081949,2.183454,-7.878975,-4.543278,7.238860,-6.329359,3.039536,-4.104760,4.880009,-0.623260,-7.768457,-8.666195],[1.756990,-3.142345,0.945852,-0.733954,8.579088,-3.483258,0.053049,-5.495209,-5.485533,-5.763694,7.058366,2.834065,-5.553072,9.084614,-9.792471,-2.855163],[6.007771,2.180089,-2.573220,4.300530,7.501532,6.936430,-5.685764,2.385958,-4.034580,-0.717388,4.871191,-0.045545,6.911432,-2.092090,9.076478,2.313849],[0.544508,-7.860254,-7.793445,4.466267,7.886589,9.724296,-2.603293,-3.217440,-9.206064,-2.065401,-2.103239,-9.496901,-7.786293,0.654173,2.590846,4.189681],[5.408248,-7.580372,4.836005,2.069440,-9.756089,-6.073542,-7.284512,-8.311272,6.279496,-4.080931,7.557700,4.264976,2.126936,-9.450051,-8.845723,9.022575],[3.867691,1.766322,9.342369,0.114012,4.821866,-7.705533,-9.071069,4.253517,9.898675,6.763895,-9.242213,7.889496,3.204947,-0.707612,7.985428,7.371418],[-8.462755,5.260679,0.128818,2.317769,-3.703111,-5.165850,-2.247033,-0.332837,8.944228,1.752327,-1.398945,1.001187,-5.263282,7.242111,9.772579,-9.996257],[-6.547141,7.421633,-9.441658,-7.099542,-2.572572,5.089209,-8.715444,6.847423,4.117745,6.710572,3.076750,8.978071,6.043038,8.064141,5.846521,-2.498413],[6.799560,2.010458,-5.231729,-0.518358,0.498088,-4.682322,9.699399,3.344930,-2.720360,-4.751240,-7.179771,8.543322,4.841930,-3.077578,-8.980937,-4.272775]],[[9.995219,9.127877,0.425117,-6.554105,8.866140,2.342868,-3.582351,5.072918,1.342279,-1.563134,3.948347,4.692425,-0.682781,9.399642,-1.635252,-2.221207],[6.509932,-8.937447,9.041752,9.335542,6.783218,0.176326,-6.242590,-6.893491,1.378624,7.522901,-9.851346,1.973989,-7.326615,7.504820,-2.383823,-0.378219],[6.438567,-3.307384,-0.897123,0.781580,-0.406473,2.422495,6.431468,7.329241,0.485245,5.288838,0.696778,-3.432745,4.445410,5.470989,-7.268003,3.155324],[-8.670303,-4.341731,-9.361456,-0.501184,4.396092,8.039422,1.376983,1.345040,0.597677,-8.289494,2.462799,-3.522093,-1.551446,-1.872738,-8.776458,-8.480348],[2.607771,2.752809,-3.441544,8.129586,7.546674,-3.211560,1.500805,7.312097,-3.137878,9.275006,4.406523,-4.170454,5.230789,-0.312260,-3.600080,-3.948597],[5.374508,6.938990,8.141763,4.688798,2.365103,0.812133,0.200279,5.889368,-6.372413,8.112862,3.279882,0.943837,-4.771148,-2.178837,-9.144903,2.931458],[-0.376089,2.216754,9.598908,-5.800606,-5.963278,4.587088,0.488401,2.252817,6.828582,4.864074,-6.580912,-6.942551,-3.980521,-6.684602,9.229810,-2.502273],[-8.105962,-9.211784,4.338719,8.677092,-3.232037,2.964157,0.066029,-1.832401,-5.075088,9.465266,-1.397646,5.879939,-5.306313,-6.925656,6.337925,1.202777],[-6.984721,1.201275,6.344264,-0.759079,4.180569,8.921371,-8.691177,-5.818765,2.727625,-1.349609,6.520513,-2.031869,6.904397,0.508457,2.162623,-9.214824],[-8.673832,0.715164,-5.168543,-6.501974,-7.433935,5.782989,1.915819,2.791675,5.040206,-9.156357,0.163390,1.822349,2.576184,-2.657572,5.267441,5.169259],[-4.785379,4.353629,-8.540185,4.165001,2.640144,7.774180,-5.676369,7.219267,-0.572984,-3.252619,-1.162334,-5.173630,-2.166949,2.865218,-5.726554,-2.221163],[3.944026,2.765290,9.493481,-4.600737,6.210671,2.935763,-7.271458,-0.897463,-4.337474,4.298435,-1.055402,3.699928,-1.255982,-3.865970,4.202872,3.105022],[9.185078,-9.628480,8.412603,9.680195,-3.989440,-6.681748,-8.025131,-8.064660,1.121678,8.648408,8.676940,4.676796,9.058321,-6.713154,-6.365078,-9.203349],[4.985677,-6.479481,2.820537,8.221997,-7.582111,9.893530,-6.946646,0.099190,1.468443,7.668272,3.873425,-3.658513,6.965174,2.098689,-1.277216,6.257578]],[[-4.156518,6.961224,7.881754,-8.583456,-1.070359,-9.595348,6.505806,9.359735,4.191335,6.473665,9.358044,9.603041,7.979089,-9.718480,-4.934930,7.015739],[5.152692,8.007937,9.673191,-2.584915,8.843311,5.136526,-5.771492,4.338105,2.925427,8.428484,-6.822639,9.654338,7.880344,1.125639,2.784498,2.517730],[1.190044,-6.432080,-6.138101,9.644343,8.290490,-0.923662,1.834354,6.278969,-8.490389,6.579783,-2.409218,-5.810529,-4.086009,2.154777,-6.097392,-1.978310],[1.450421,5.301061,2.497560,1.931336,6.865474,-0.398325,6.702815,1.793384,-6.665444,-0.441785,-8.455699,9.688448,0.075137,-1.188307,5.406345,7.228600],[4.394788,-4.274412,9.239469,-9.744457,8.379990,9.177333,-2.291328,-0.112050,8.851626,0.341899,-9.792862,-1.950180,-3.853799,6.840052,0.081390,-9.135496],[2.045760,2.525841,2.898959,8.635089,6.121099,0.938140,-1.642223,-1.269632,0.796573,4.053858,-4.989108,5.013143,-9.394515,-9.448895,2.352624,9.403675],[5.931034,-4.965582,-7.798351,5.261173,-1.957111,2.023019,2.976088,0.931776,-9.566524,-7.469755,-2.876331,4.717704,-2.069708,7.849313,-0.626579,2.633481],[5.834859,-8.321260,4.863114,6.480678,7.373276,-9.071048,8.803315,6.930292,-0.230580,-6.945294,4.761993,-3.751934,-2.827066,4.778776,-3.155142,-8.623827],[-5.709618,5.332284,1.710576,-9.593112,2.003333,9.513443,-2.383667,-2.101640,-8.788258,6.511754,-0.802662,7.094103,2.952014,-4.502550,2.890777,-4.691657],[7.090684,-4.668462,-8.944033,6.588317,8.267742,-6.173651,2.818712,0.354086,-3.342090,1.741934,-2.656734,0.403182,-1.906288,5.755570,-0.056956,9.966444],[6.531058,-3.574523,-7.589594,0.006376,-5.880779,2.711923,5.849438,2.102407,-8.165394,-8.648179,-9.672797,-9.711300,9.907274,-6.226967,4.598832,-8.828561],[3.894143,0.607228,-9.591790,-6.227274,-0.310491,2.730868,-2.413701,1.814982,6.728958,3.820752,9.095709,-5.721227,4.803928,4.334938,3.568248,7.796679],[-5.339891,-2.124775,4.947216,-9.305160,1.153980,0.514647,-8.436768,-0.552043,3.896852,6.475197,0.861272,5.031482,7.453506,-2.974490,-3.859256,4.491406],[-6.734962,-9.474994,-4.270250,6.142210,-1.454741,9.147524,-8.816844,-1.452089,5.489140,-6.840901,-2.714103,2.514395,-9.768406,-4.161863,3.872653,-7.380568]],[[5.859607,-5.878943,5.379442,5.236645,-7.991874,-4.516339,-8.350823,-6.695816,8.759255,9.626531,5.995247,1.424606,-9.156138,-5.683110,5.033510,3.411870],[0.993030,0.604715,9.940384,-1.842050,6.489410,-9.480385,-9.139065,-7.072233,-8.106543,3.915078,-6.839837,5.847759,-5.924291,1.856130,-0.075369,-7.938783],[-4.443003,-8.980783,6.795051,8.511521,-0.618324,-5.413179,8.870654,-5.327853,-8.828863,1.674329,-2.835443,9.834281,-8.267850,-7.215263,5.221386,2.216902],[-7.167109,-2.411072,-5.297643,8.529962,2.306177,8.661404,-0.551305,-0.621929,1.002711,8.350778,7.583762,-3.734282,1.081702,-8.393464,-7.099619,-3.415662],[-0.514429,-7.756173,3.685740,0.419956,4.752309,5.342880,-3.430204,4.290337,7.225609,6.973767,5.063108,-1.813784,-7.016909,-3.936707,-1.692375,-0.818456],[5.712345,-7.383089,-8.431597,1.549656,-3.695075,4.535349,3.698117,9.478946,5.805737,1.549845,-0.096663,-6.763982,-4.685193,3.505814,1.017458,3.540551],[-0.951991,3.304740,5.785417,7.879359,9.019209,-0.803030,0.114287,3.281389,-7.709180,5.044634,2.475323,-0.684553,-9.257780,-9.360425,6.966144,-8.259806],[0.984840,-5.802190,0.312674,1.449943,-8.116385,8.271377,1.244885,-9.767467,8.688878,-3.147459,5.805349,-9.078934,3.913136,-3.255967,4.763593,-0.463815],[-9.928451,0.368950,-2.127135,9.198458,8.377232,-7.675261,7.023244,-3.694096,7.949644,4.474961,1.430981,-4.689086,7.499221,2.165914,-4.964676,3.613837],[-5.636955,-7.018233,5.543653,5.859981,-3.991039,1.312282,0.739231,-6.438721,4.813953,2.116982,9.482791,7.235725,-8.828615,9.302763,-8.444496,-4.503654],[-1.471113,-2.949952,-6.955189,-8.215401,1.864399,-0.655361,1.930887,9.376448,7.096907,-9.510904,5.332696,0.507892,-4.566868,-3.919625,1.238086,-1.878226],[7.922734,-5.595028,-9.583512,-1.645009,-7.439110,-2.695486,9.337052,-8.441546,9.298134,3.855869,-7.580905,-1.111635,-1.001186,-3.514617,0.662898,0.967577],[8.916908,-9.210301,-5.411336,2.138823,-5.754915,-3.011356,-9.283459,-1.712507,5.956193,-0.393114,-2.379416,2.640739,1.991460,-7.536294,-7.796549,0.608114],[5.657450,4.792853,-5.500401,4.636233,8.597876,-6.331613,-7.575164,0.948898,-3.660185,-0.547602,-6.469138,5.130943,7.812913,6.684794,7.417704,0.173619]],[[-0.861672,-4.954283,1.880622,3.493862,-5.908797,-1.819649,-7.469514,-2.472379,7.603029,6.694294,-6.895429,7.855777,5.249640,3.676922,5.570332,9.401835],[-8.981244,-7.568342,8.457116,-4.404194,3.183539,7.171349,-9.640416,2.282919,-7.704392,1.394700,6.835763,-5.569177,1.338861,-5.525156,-7.875806,7.121121],[1.181729,-1.639566,9.692548,-0.623325,-9.634555,7.319605,-0.904764,-6.394122,7.567257,8.247496,5.536388,5.401260,-4.249787,4.262773,-8.280843,9.855643],[1.951033,-9.257089,-3.282478,7.210189,-2.615012,4.881845,7.624274,0.557961,0.593925,-5.319518,-8.700680,-3.888595,8.557157,8.476441,-6.943411,1.959400],[7.318358,-0.230339,2.050003,-2.746984,-5.481154,-7.892754,4.190001,0.144390,-6.838556,3.711285,7.075598,2.771387,-7.840391,-1.320946,7.735950,-1.062406],[-4.456107,-2.678459,-6.492636,6.684896,-8.959388,9.026887,-8.572801,7.580540,-9.247043,7.148477,-9.395772,-3.283686,-1.754917,7.645586,-0.209132,-7.805058],[-9.564312,-9.886256,9.893729,-4.922675,0.636218,0.522367,-4.550193,2.907926,-3.104082,-8.053108,3.010920,0.315794,-9.524918,-2.161884,-7.828211,4.671449],[3.498906,1.136391,0.312190,6.201535,6.445423,-3.754359,9.536652,-5.076523,6.118921,-7.414836,2.363584,-8.317382,-2.326700,2.689391,0.112174,7.328574],[-1.645819,5.860052,-1.169866,1.411581,9.894510,0.794995,2.412540,-2.803355,1.674691,4.629913,-9.347694,-1.299960,-5.647020,2.497579,-8.567026,5.593148],[-6.940014,-6.328599,8.989218,-6.290872,-1.761491,2.150996,-9.374731,-2.402323,-3.086966,-3.496198,1.956655,9.380800,-6.813388,2.037348,7.848301,-5.158646],[0.691550,5.171933,-1.664898,1.211397,3.792889,-0.064153,6.436306,9.968746,-7.430062,-3.558426,-4.413955,-1.780722,9.812133,5.440345,-5.487026,-0.814904],[5.135433,-9.864968,8.434194,-5.300355,-1.286489,-1.460347,1.245632,2.426222,-4.848998,9.668451,3.297910,8.494684,8.110036,9.260872,-6.233341,0.565492],[5.931115,2.822239,2.405407,-2.815553,-0.456655,2.067538,-9.826023,-2.546395,6.935158,-0.401610,9.945727,0.766753,-8.862959,-8.999962,-9.413697,-7.767455],[0.852481,-1.521697,4.239002,-7.982482,-0.023442,7.455771,-8.613202,6.945566,8.515254,-4.487290,0.836337,7.178044,-0.033223,5.919756,9.709561,2.305788]],[[2.990170,-7.087439,-1.179633,8.006777,-1.133996,8.416565,-4.546935,-3.119654,-9.603849,-2.827329,-9.122393,-4.617967,7.886520,9.978899,8.126607,1.931271],[6.500811,-8.363400,-2.671407,-1.442360,-5.938080,1.461971,-9.769834,1.800449,-5.358182,-1.418448,0.623286,7.356189,-8.529257,-9.178350,8.146722,1.895581],[1.261057,-5.328694,9.844238,-4.459679,5.584946,-7.284508,-2.963140,-8.732463,7.598775,1.978521,0.471569,5.503085,-8.157285,-0.525081,5.705639,-6.842251],[3.447257,-1.742375,1.529063,-0.267698,-0.014749,-2.762774,-8.132526,8.111195,2.537896,9.363888,2.221097,0.070186,-1.582840,-0.311434,2.645784,-7.683668],[6.797782,1.541066,3.493598,4.296821,-5.756974,-4.582424,5.986064,-3.453437,8.255913,0.675170,-9.845897,-1.779296,-5.099357,-0.366236,5.716855,-3.224540],[1.780727,8.768036,-8.438968,-2.722959,-3.603148,7.486504,-3.815328,-4.155985,4.043183,-1.635231,-8.579821,-3.792487,1.096876,-0.541793,1.842975,-8.096333],[-0.279080,-3.501593,-2.029643,0.880428,5.314476,-2.750126,-2.122858,4.708968,6.993109,2.104073,-4.934989,-8.488735,-0.315285,-8.539829,-9.188808,-4.160371],[-4.808911,8.284595,4.989512,7.312543,3.036178,-9.000736,5.547814,-2.436103,-2.585213,-8.313829,9.702943,-7.630108,-8.215054,-5.092270,4.683895,0.941413],[5.016236,0.266145,-0.257023,9.091629,-3.471368,6.585830,-7.367837,-7.903348,-0.467935,1.759289,-3.031467,5.964075,3.611893,2.767041,4.507269,-3.354867],[2.542315,4.375173,3.226119,3.656982,2.587956,5.934598,-2.383676,-7.012218,-7.178970,5.993261,6.141956,2.898009,-3.294205,-3.729072,-0.274208,-3.689804],[-6.893565,0.619599,-8.204151,6.794028,7.615370,1.129370,5.576627,-1.878350,-3.348970,-2.969499,2.747914,-4.909208,-0.764784,5.518002,6.917625,-6.855449],[9.646911,4.705742,-1.353945,7.963833,9.317465,-7.816533,-4.931993,2.761193,-5.866407,6.894950,9.744433,2.290744,-2.654878,-3.084365,-9.558366,8.422158],[-7.624846,6.319578,1.336469,4.485234,-4.730594,5.122554,-6.434762,2.077934,-4.121279,-0.981971,-6.159806,4.225174,-4.819683,-6.317194,-6.356011,4.149616],[9.387771,-0.843700,5.528600,1.415629,9.604012,3.196901,6.936028,-2.007529,4.622467,-4.770379,-9.509258,-1.763163,2.029970,0.144223,-2.062907,4.315993]],[[9.630972,-4.057064,3.113398,-9.662291,0.654175,-4.811652,-7.901109,-2.298412,-1.696581,3.202411,5.315339,8.113648,1.482116,-2.564028,0.126975,4.421259],[9.937085,-2.890028,9.034968,7.404775,-1.602912,-0.730733,-0.519263,-8.096563,0.317815,8.361811,3.178950,3.311135,6.747331,-3.048988,3.758619,-5.210923],[8.234510,9.165295,4.479892,8.388564,0.880867,3.078424,8.547089,-0.409888,2.461281,3.204648,-2.480480,8.270778,-1.608554,0.573919,1.949285,4.245260],[-8.802218,-2.669185,8.304207,1.001794,9.259530,0.388663,-8.145320,4.592587,0.110588,-5.331407,6.029409,-2.033222,9.566189,-2.175284,4.184502,7.266641],[-6.973442,8.324606,-1.091957,-0.318945,8.292947,-4.613997,6.803456,-8.490887,-0.114548,8.184398,-9.591336,1.769987,3.057859,6.847155,8.954942,-0.816710],[-8.140303,-8.037239,-4.426780,-0.056759,-0.603272,5.132505,-4.976993,-4.237055,-4.261761,-0.993377,9.391028,-1.333505,9.914878,1.552186,-0.537859,2.764025],[-9.858319,8.888733,-6.685757,-5.116150,-4.546883,6.802231,0.505131,0.160696,1.383298,1.001662,-3.975538,3.742738,3.146856,-3.445941,-4.492376,-8.797415],[4.990120,5.923016,3.576623,-5.958417,7.363600,-0.039046,-0.679398,-9.669280,6.748285,-7.839407,1.886362,-9.358176,2.476550,-0.843991,-3.751011,-4.497260],[8.810212,3.073231,2.038403,-6.053136,8.404541,-5.838972,8.919763,9.962702,-2.399363,-0.655160,9.934244,-2.077512,0.303888,-7.458879,3.633454,-7.009147],[-6.461609,8.679640,5.850940,-1.956855,-4.149488,-5.420468,0.304341,-6.583570,-4.566224,5.873581,5.153142,-8.599966,1.685804,-1.857324,6.841306,9.026368],[7.536935,8.233752,-6.141203,9.836403,-9.257813,-4.841793,-3.272582,2.178834,2.914719,-7.166299,-8.240799,-3.157571,-2.830769,-7.989232,2.716550,7.917594],[-8.509022,3.083068,0.123818,3.008145,2.513427,8.894851,2.187942,-5.957500,-0.838933,8.879537,6.016294,-7.893605,3.762182,3.555270,-4.102232,7.788640],[1.076652,7.299929,6.142526,0.937167,1.787031,-9.074788,2.422401,2.322485,-8.635516,5.386878,-9.676424,6.947185,-1.302479,-1.619349,1.989829,-3.465726],[7.417037,4.645920,-1.207988,2.782889,-5.604819,-6.164449,-2.856340,9.513190,7.109191,-3.178289,-7.080298,4.725378,-2.857986,2.862786,9.806553,-7.312790]],[[9.505295,4.977690,-3.394779,6.241649,2.943323,8.396637,-5.327929,-7.703829,3.356406,2.802459,-3.384108,-4.983275,6.920566,-0.516187,7.155619,2.159425],[3.459688,3.768845,5.675454,-1.534342,-0.415319,-4.606618,-3.924603,-6.601983,0.101988,9.146114,-3.743795,-9.970662,5.116832,-7.233507,6.269631,8.077015],[1.968453,4.707950,-3.026670,1.685265,1.216662,9.266638,-3.766239,5.491875,9.689280,5.708442,-7.904414,7.631705,-0.830192,1.646372,1.847487,-8.110719],[6.216951,8.345035,2.470960,-3.120810,-0.379400,-6.506338,-9.551024,-7.243815,-0.314679,7.773176,7.207806,-4.971796,0.727720,-3.681851,5.057625,8.559664],[-2.246711,-9.141350,1.782296,-5.523067,-8.387041,-5.719890,-1.731130,-6.611746,-5.404761,5.765206,6.766379,8.633009,6.433432,5.053747,8.801142,8.124210],[-8.916704,0.463514,0.466506,5.188185,2.107297,-9.941847,7.405213,-4.774833,-7.915422,4.425128,-0.807951,-9.975737,-0.882312,-5.588402,-9.622352,9.204993],[9.848009,-8.483342,-2.995607,-2.825319,1.533658,6.690553,2.350927,-1.872085,-7.624764,0.754443,3.339373,-5.085530,-4.340146,1.237223,7.773340,2.024281],[8.405448,3.730350,9.657107,2.495738,-1.423986,0.039460,5.666837,7.889943,-2.131272,-4.795221,5.840827,1.206146,8.915439,-3.377684,-9.032259,1.217530],[-3.911660,5.003380,-1.175518,-0.597543,-8.346436,-9.532906,-3.099477,4.545462,5.330461,-0.096048,-0.093552,-4.016989,-2.803632,-1.203268,-5.630073,-9.491937],[-3.259515,-7.631125,5.209026,6.521788,0.639148,5.723799,-4.018497,-8.470388,-1.771836,-3.118846,-7.067851,-9.823162,0.794780,1.439449,-6.943742,-3.363283],[-8.312972,6.948627,-6.140885,2.178325,-9.740559,0.898512,4.542681,-8.171423,-4.716433,-3.890260,8.973137,1.600388,-4.886214,-5.035308,-3.487446,5.766071],[-5.324160,-9.673269,-9.049857,-6.541410,-6.992112,1.644795,8.634259,8.420184,-6.018846,-9.149055,-2.243319,-0.700267,2.029244,8.584958,-5.330908,-7.096916],[3.872140,1.071563,-4.379678,9.277775,0.950912,-4.194758,-6.352319,-6.239042,2.693646,4.072666,-5.696519,-7.985722,-9.515054,1.107232,0.006934,1.792422],[5.712627,-8.464740,-0.447875,-1.999166,-8.111026,-4.519286,4.975775,9.471307,-8.530837,-7.111463,-5.497803,-4.538473,8.308289,5.844980,3.615087,6.608673]],[[1.092834,-5.787764,3.965015,2.817485,1.264143,9.031893,-6.003799,0.096092,0.607308,0.035121,9.803729,-2.111451,-6.701736,3.939763,9.132481,-4.056394],[-5.773927,-8.348077,7.842095,8.307416,-6.861105,5.693483,3.230052,7.661991,1.143775,-0.763587,-8.079423,2.019873,2.199906,-8.479034,5.681492,1.249130],[2.056041,-0.747171,-5.248031,7.942826,-0.489983,5.753455,2.203253,-5.917757,-5.180482,2.098729,2.279317,6.879378,1.462322,7.008825,-4.102773,-1.248266],[4.314557,-3.791051,-5.003110,-3.978187,9.034705,-8.543347,-6.036760,6.306116,-8.093978,9.317757,3.313669,-5.679071,-9.625797,5.344763,-3.494491,-0.728562],[-6.924186,8.920734,-3.443240,5.353584,-8.971011,-3.976794,-3.110920,9.503287,3.297557,0.791085,3.299515,6.848639,1.002005,-4.225930,6.908970,7.064903],[6.097038,-8.148856,-8.140343,8.648765,-6.251541,5.627685,4.361077,5.727977,2.038863,8.702485,-0.424221,-7.054025,-2.161833,7.026784,4.431489,6.277663],[-1.077640,-8.527448,-1.193219,1.890147,-8.918570,5.871317,7.162531,-8.935132,8.465836,3.994782,-2.470252,-4.094448,-6.371856,-7.028330,-4.589380,-6.820646],[-0.471206,-0.302043,9.537109,1.457189,-9.708027,9.019060,1.586988,4.046441,-0.971143,-8.503799,-4.653433,1.866520,-5.262386,0.438911,6.783145,5.158976],[-5.600428,-9.716526,9.661794,2.469367,1.502526,6.920061,-2.314900,4.267201,0.472018,-9.152782,-4.451371,-6.320095,6.285396,-8.473621,-6.222611,-5.088075],[2.686039,-0.174939,-2.746171,-2.136450,-6.252052,-8.191969,-7.586915,7.684215,9.461752,-7.898241,4.922421,0.806070,-2.350052,-4.427390,4.775272,1.450910],[2.499003,-0.897552,-1.542548,3.441662,-7.522103,7.104733,-2.739101,5.688908,-1.045425,1.822304,-5.375352,4.130661,-9.954577,3.108339,-2.089587,-6.381667],[-2.409356,-0.203316,-8.440321,-0.113981,6.460226,5.842685,-5.846867,-0.378445,-5.293403,0.413036,-0.157362,6.931299,-5.098555,-6.137612,-9.867006,-2.216984],[6.474895,9.226374,2.532550,9.324283,7.961859,-7.609868,8.171645,0.640375,-3.326782,-3.090643,7.996740,-5.965412,4.281351,-6.452969,1.918233,-4.429530],[3.735152,-1.805275,4.982235,-6.846727,1.277555,5.026992,2.106848,-1.261423,9.026696,-7.861122,9.305384,-9.349086,0.208989,-0.389205,5.862781,-2.051079]],[[-4.664899,0.981371,-1.551926,-0.765275,-8.919134,-4.752122,-3.552513,-5.164736,2.721853,-8.014110,4.424613,6.045867,-0.954224,5.796536,8.629016,-8.671925],[2.412595,4.313629,4.243578,2.360570,6.686513,9.450249,-8.241152,1.259258,-1.956737,-6.629663,-4.701379,5.817403,1.498789,0.632344,-1.238957,-7.172788],[8.223264,6.399747,-4.448226,5.900829,-5.402374,3.001871,-3.472805,-5.381669,4.513204,-5.728191,2.667478,-4.154191,-8.608197,1.482143,0.958724,-2.865914],[9.067264,-7.235429,-8.122667,-2.061365,-7.874189,-3.684783,-8.043273,-3.872005,6.136974,-8.599231,-6.219882,-9.496916,-4.025364,2.403876,0.372885,-0.112645],[9.654376,-4.024044,-4.307169,-6.245150,6.700675,3.356064,5.522432,6.122846,-7.197615,4.983170,-3.631452,-1.686608,9.670682,-4.889731,5.042928,-9.226232],[4.133402,5.935120,5.353071,7.437787,-2.815036,-5.829561,-6.626034,-1.166418,6.306607,6.950746,5.581047,-3.990399,5.212851,-5.892900,-6.464702,8.538099],[5.299363,9.578334,-6.379113,6.888001,-0.812683,-6.758037,0.286848,0.059536,6.499477,-2.479983,-7.127279,0.757780,-9.908879,4.851138,-4.706901,-5.133207],[1.714609,-5.596443,-0.808349,-6.772483,-7.076094,7.663503,3.202316,-2.719084,1.393610,-0.994362,-0.163013,5.119633,0.056555,5.361894,5.526135,4.682663],[6.422494,-6.721125,-7.537781,-6.809140,-3.866981,-5.518350,4.937621,-7.356619,-9.195797,-4.776958,-6.553341,4.855020,-6.827072,-0.735967,-2.855234,-1.169430],[4.876897,-8.409748,5.314983,-1.840327,-2.752112,-1.734414,-4.454168,1.226069,8.548630,4.202101,6.502445,3.257263,7.369869,-7.978431,9.479727,7.755653],[1.276339,-6.153440,0.447695,-1.903026,-4.791508,9.019430,8.449853,3.479768,-9.335438,1.671865,4.408617,-5.000901,-3.470916,-9.573475,9.716109,-8.370559],[2.560772,-1.786184,-7.532485,7.112584,5.690113,2.623255,6.391771,7.359724,6.471551,7.686888,3.507843,6.111894,-2.339196,0.026087,1.980347,4.085917],[1.143937,4.901084,-2.477837,-3.779323,7.972016,4.765649,-6.189604,7.803250,8.482691,-1.325730,-5.741968,-9.070381,2.328018,-9.871346,0.195605,-6.305546],[4.048337,-7.767429,-9.305144,9.541590,-8.321929,-2.248772,2.282557,-4.846071,-8.199998,5.619643,-9.128286,-5.519726,-5.122241,9.479419,-8.834120,-3.265684]]], dtype = "float64")#candidate|7741|(15, 14, 16)|const|float64
bop_7742 = relay.power(var_7740.astype('float64'), relay.reshape(const_7741.astype('float64'), relay.shape_of(var_7740))) # shape=(15, 14, 16)
output = relay.Tuple([bop_7742,])
output2 = relay.Tuple([bop_7742,])
func_7748 = relay.Function([var_7740,], output)
mod['func_7748'] = func_7748
mod = relay.transform.InferType()(mod)
mutated_mod['func_7748'] = func_7748
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7749 = relay.var("var_7749", dtype = "float64", shape = (15, 14, 16))#candidate|7749|(15, 14, 16)|var|float64
func_7748_call = mutated_mod.get_global_var('func_7748')
call_7750 = func_7748_call(var_7749)
output = call_7750
func_7751 = relay.Function([var_7749], output)
mutated_mod['func_7751'] = func_7751
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_7767 = func_5442_call()
call_7768 = func_5442_call()
output = call_7767
output2 = call_7768
func_7773 = relay.Function([], output)
mod['func_7773'] = func_7773
mod = relay.transform.InferType()(mod)
mutated_mod['func_7773'] = func_7773
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7773_call = mutated_mod.get_global_var('func_7773')
call_7774 = func_7773_call()
output = call_7774
func_7775 = relay.Function([], output)
mutated_mod['func_7775'] = func_7775
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3897_call = mod.get_global_var('func_3897')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_7807 = relay.TupleGetItem(func_3897_call(), 0)
call_7808 = relay.TupleGetItem(func_3898_call(), 0)
func_7098_call = mod.get_global_var('func_7098')
func_7100_call = mutated_mod.get_global_var('func_7100')
call_7827 = func_7098_call()
call_7828 = func_7098_call()
output = relay.Tuple([call_7807,call_7827,])
output2 = relay.Tuple([call_7808,call_7828,])
func_7837 = relay.Function([], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
mutated_mod['func_7837'] = func_7837
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7837_call = mutated_mod.get_global_var('func_7837')
call_7838 = func_7837_call()
output = call_7838
func_7839 = relay.Function([], output)
mutated_mod['func_7839'] = func_7839
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3698_call = mod.get_global_var('func_3698')
func_3700_call = mutated_mod.get_global_var('func_3700')
call_7859 = relay.TupleGetItem(func_3698_call(), 1)
call_7860 = relay.TupleGetItem(func_3700_call(), 1)
output = call_7859
output2 = call_7860
func_7869 = relay.Function([], output)
mod['func_7869'] = func_7869
mod = relay.transform.InferType()(mod)
mutated_mod['func_7869'] = func_7869
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7869_call = mutated_mod.get_global_var('func_7869')
call_7870 = func_7869_call()
output = call_7870
func_7871 = relay.Function([], output)
mutated_mod['func_7871'] = func_7871
mutated_mod = relay.transform.InferType()(mutated_mod)
func_684_call = mod.get_global_var('func_684')
func_686_call = mutated_mod.get_global_var('func_686')
call_7913 = relay.TupleGetItem(func_684_call(), 0)
call_7914 = relay.TupleGetItem(func_686_call(), 0)
output = relay.Tuple([call_7913,])
output2 = relay.Tuple([call_7914,])
func_7922 = relay.Function([], output)
mod['func_7922'] = func_7922
mod = relay.transform.InferType()(mod)
output = func_7922()
func_7923 = relay.Function([], output)
mutated_mod['func_7923'] = func_7923
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1846_call = mod.get_global_var('func_1846')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_7944 = relay.TupleGetItem(func_1846_call(), 0)
call_7945 = relay.TupleGetItem(func_1848_call(), 0)
func_6986_call = mod.get_global_var('func_6986')
func_6987_call = mutated_mod.get_global_var('func_6987')
call_7952 = relay.TupleGetItem(func_6986_call(), 0)
call_7953 = relay.TupleGetItem(func_6987_call(), 0)
func_7581_call = mod.get_global_var('func_7581')
func_7583_call = mutated_mod.get_global_var('func_7583')
call_7961 = func_7581_call()
call_7962 = func_7581_call()
output = relay.Tuple([call_7944,call_7952,call_7961,])
output2 = relay.Tuple([call_7945,call_7953,call_7962,])
func_7974 = relay.Function([], output)
mod['func_7974'] = func_7974
mod = relay.transform.InferType()(mod)
output = func_7974()
func_7975 = relay.Function([], output)
mutated_mod['func_7975'] = func_7975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5693_call = mod.get_global_var('func_5693')
func_5694_call = mutated_mod.get_global_var('func_5694')
call_8027 = relay.TupleGetItem(func_5693_call(), 0)
call_8028 = relay.TupleGetItem(func_5694_call(), 0)
output = relay.Tuple([call_8027,])
output2 = relay.Tuple([call_8028,])
func_8030 = relay.Function([], output)
mod['func_8030'] = func_8030
mod = relay.transform.InferType()(mod)
output = func_8030()
func_8031 = relay.Function([], output)
mutated_mod['func_8031'] = func_8031
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8067 = relay.var("var_8067", dtype = "float64", shape = (12, 11, 8))#candidate|8067|(12, 11, 8)|var|float64
var_8068 = relay.var("var_8068", dtype = "float64", shape = (12, 11, 8))#candidate|8068|(12, 11, 8)|var|float64
bop_8069 = relay.divide(var_8067.astype('float64'), relay.reshape(var_8068.astype('float64'), relay.shape_of(var_8067))) # shape=(12, 11, 8)
func_7098_call = mod.get_global_var('func_7098')
func_7100_call = mutated_mod.get_global_var('func_7100')
call_8082 = func_7098_call()
call_8083 = func_7098_call()
output = relay.Tuple([bop_8069,call_8082,])
output2 = relay.Tuple([bop_8069,call_8083,])
func_8085 = relay.Function([var_8067,var_8068,], output)
mod['func_8085'] = func_8085
mod = relay.transform.InferType()(mod)
var_8086 = relay.var("var_8086", dtype = "float64", shape = (12, 11, 8))#candidate|8086|(12, 11, 8)|var|float64
var_8087 = relay.var("var_8087", dtype = "float64", shape = (12, 11, 8))#candidate|8087|(12, 11, 8)|var|float64
output = func_8085(var_8086,var_8087,)
func_8088 = relay.Function([var_8086,var_8087,], output)
mutated_mod['func_8088'] = func_8088
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8140 = relay.const([[-8.169751,-3.634992,-3.225343,1.626284,-6.919427,-5.609409,-4.121334,4.693199,9.754928,-1.932746],[9.092141,9.844170,-6.989757,-3.685461,7.963015,5.693816,4.493927,8.533954,-3.648478,-7.939659],[-2.153106,4.054573,0.127236,3.051212,-3.268764,3.708173,2.596116,1.780241,-4.672798,-3.170334],[2.493831,7.732552,7.932114,-5.348807,1.852626,-4.622634,1.138407,7.065825,-8.276831,8.991389],[-4.799040,5.578571,-9.584446,-3.287771,-6.755961,-9.153442,-1.073914,-0.845355,-6.455750,1.923953]], dtype = "float64")#candidate|8140|(5, 10)|const|float64
uop_8141 = relay.asin(const_8140.astype('float64')) # shape=(5, 10)
func_7383_call = mod.get_global_var('func_7383')
func_7385_call = mutated_mod.get_global_var('func_7385')
call_8149 = relay.TupleGetItem(func_7383_call(), 2)
call_8150 = relay.TupleGetItem(func_7385_call(), 2)
func_8030_call = mod.get_global_var('func_8030')
func_8031_call = mutated_mod.get_global_var('func_8031')
call_8151 = relay.TupleGetItem(func_8030_call(), 0)
call_8152 = relay.TupleGetItem(func_8031_call(), 0)
output = relay.Tuple([uop_8141,call_8149,call_8151,])
output2 = relay.Tuple([uop_8141,call_8150,call_8152,])
func_8160 = relay.Function([], output)
mod['func_8160'] = func_8160
mod = relay.transform.InferType()(mod)
mutated_mod['func_8160'] = func_8160
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8160_call = mutated_mod.get_global_var('func_8160')
call_8161 = func_8160_call()
output = call_8161
func_8162 = relay.Function([], output)
mutated_mod['func_8162'] = func_8162
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3850_call = mod.get_global_var('func_3850')
func_3852_call = mutated_mod.get_global_var('func_3852')
call_8163 = func_3850_call()
call_8164 = func_3850_call()
output = call_8163
output2 = call_8164
func_8180 = relay.Function([], output)
mod['func_8180'] = func_8180
mod = relay.transform.InferType()(mod)
mutated_mod['func_8180'] = func_8180
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8180_call = mutated_mod.get_global_var('func_8180')
call_8181 = func_8180_call()
output = call_8181
func_8182 = relay.Function([], output)
mutated_mod['func_8182'] = func_8182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_8211 = relay.TupleGetItem(func_859_call(), 0)
call_8212 = relay.TupleGetItem(func_860_call(), 0)
func_5094_call = mod.get_global_var('func_5094')
func_5095_call = mutated_mod.get_global_var('func_5095')
call_8238 = relay.TupleGetItem(func_5094_call(), 0)
call_8239 = relay.TupleGetItem(func_5095_call(), 0)
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_8242 = func_526_call()
call_8243 = func_526_call()
const_8252 = relay.const([[[-6.835932,9.801891,-6.483035,6.877245,-2.921172,-9.756792,9.054121,-2.471686,3.017424,1.056877,-1.747065,-0.624321,5.836530,3.939720],[3.434015,8.840020,-1.105392,8.431862,7.896392,6.631209,5.117749,3.737569,-2.078972,1.746544,3.134208,-3.345571,2.386316,-7.981070],[-5.354318,4.884255,-1.635869,1.926489,3.138036,6.302768,3.737546,-1.323254,-5.491648,9.006112,9.375952,-3.158685,1.200770,-6.774199],[-9.755875,6.874245,3.856195,-2.516915,7.676872,-3.897091,-4.216777,-0.030929,-1.671885,-0.302290,-6.337676,8.380242,-5.372527,-8.652664],[-9.445486,6.649635,9.331869,8.068620,8.730781,7.778109,7.947707,2.814774,3.387590,9.084437,-1.973817,5.435032,9.163071,3.267150],[-7.076452,3.757500,-6.568819,9.686493,6.167020,-2.093049,-7.349541,-3.856853,5.170831,9.378204,7.253761,-4.603863,6.336725,-1.181212],[3.981252,-1.837385,6.624466,-5.266717,-2.698087,1.470634,5.104877,-2.806162,1.612452,9.397223,-0.428446,-6.269224,-3.533208,-9.035913]],[[-9.982488,-0.129995,-6.999797,5.571043,7.024755,7.473621,-5.790017,9.419940,3.447059,7.395419,-5.553988,3.478693,-6.582188,-8.849206],[9.120209,-4.105021,5.933964,8.275089,8.028762,3.427208,-7.180799,2.866183,-7.952900,-7.281115,-2.713788,-7.194232,3.390713,-4.060060],[1.012826,-5.099186,5.707816,-9.215977,7.066867,-3.064482,2.649596,9.428796,-1.984403,-0.445460,-5.892725,-0.447367,-9.275915,0.316329],[5.188048,0.100921,3.369574,3.310458,-0.732282,3.593437,4.523593,2.421371,-9.250940,-3.120854,5.616760,1.072721,-5.078614,-4.851335],[-1.592104,-5.097228,4.893317,1.046004,6.081877,5.440195,-1.915984,7.822168,-4.282163,-5.726962,-8.223939,-0.397210,2.289858,6.522742],[7.376147,5.769561,8.226849,5.731339,8.962315,5.980224,5.249312,2.352087,-8.655746,9.414270,9.849854,8.891916,6.584864,2.541647],[1.590397,-5.781651,-5.842119,-6.417939,9.445193,0.895471,-5.918067,7.329202,4.897745,-1.940617,0.353956,8.141578,1.907607,-3.897960]],[[-1.240698,-7.196940,-2.060534,-4.930019,-5.621847,2.646803,4.449589,-3.341007,6.466895,8.748598,-6.305154,-3.166677,-0.163481,-0.452643],[-9.507228,-4.341660,-8.747710,-7.585556,1.507884,-2.081908,-4.769126,3.294833,-2.708329,2.236785,2.923054,-1.069998,-3.861507,0.296062],[-4.522445,6.915126,1.050155,7.802909,-0.695542,-1.370456,3.356516,4.326404,-4.791915,3.496370,-7.489109,0.188851,0.443138,-1.558914],[-6.090539,-4.532451,2.366967,-7.138530,3.569497,4.420964,5.916501,3.049430,-7.272443,-4.939320,8.245628,4.385992,4.840674,3.503848],[-3.978526,-8.732988,-8.648644,-2.186629,-2.090193,-3.317184,-7.796761,6.940585,8.138222,-9.104839,2.397397,5.419230,-0.386408,5.447682],[4.374264,1.812931,-3.354875,-2.688425,-3.823703,-4.600085,2.135584,0.274616,-3.344924,-5.878005,5.774385,8.211702,2.543203,-2.294220],[6.629352,7.589209,-3.822020,0.012347,0.612320,0.911957,-5.044212,-6.432736,-3.071996,5.241255,1.509407,2.201014,4.940222,9.055381]],[[6.046926,-7.407022,4.247859,3.960457,-7.061226,-9.834792,-3.695939,-0.769421,-5.414263,7.405942,-4.948718,3.761560,-1.290199,-4.581860],[-9.930619,-0.534276,2.020422,-5.063767,6.326299,5.024526,-1.210455,7.791698,2.182948,9.124138,-1.958278,4.573191,-7.705228,-7.425756],[0.543965,-6.120649,5.225107,6.353671,1.904564,2.040636,8.455569,4.470789,2.212726,-0.889604,-0.215696,-1.929566,-5.657267,7.574099],[-0.321685,7.636044,-9.798041,1.860483,1.631230,6.037307,9.002244,0.783058,4.056919,-9.105325,1.401701,5.506926,5.884438,-3.341591],[5.539584,-4.427831,-9.472190,0.788569,0.418885,-6.864467,1.552818,9.303419,-1.850112,8.314500,1.675332,-1.493104,7.146992,-1.023038],[8.065385,-6.303113,-6.543823,3.224614,5.160770,-7.120271,6.101900,4.618299,-5.374823,2.617489,4.814307,-2.121306,5.672499,2.410155],[-6.908591,4.827257,-8.859215,6.224216,-3.417783,7.395811,6.845093,-1.996168,-9.299323,-6.665362,-9.667415,-2.154418,-3.702184,9.614383]],[[6.307811,-0.683548,-9.929512,-0.351264,-3.442446,-6.817303,-2.543650,-4.555592,4.706997,-4.290943,-9.279590,-3.125126,2.825054,-5.093204],[0.333453,7.369868,-4.750966,-7.499471,6.595663,0.788192,-8.199984,-9.901341,-2.509688,0.349250,6.576940,4.732107,-2.249396,-9.624857],[-3.253149,1.606134,-6.142795,9.591517,8.517752,-1.676142,-2.647285,-1.049712,3.519796,3.774954,5.084918,9.265496,-5.936051,-0.415483],[-2.248904,-2.066388,0.569196,-9.232115,-8.139906,-2.092757,3.753362,-6.697656,-5.115216,4.444737,3.839468,6.856126,9.880478,8.073118],[-5.231163,-1.179173,8.254728,0.474846,-7.115059,-5.695844,3.951514,-5.881667,1.882018,-4.704725,0.550755,0.937543,-0.845171,0.476801],[6.417194,-4.811039,-4.969365,-7.915322,6.155066,-9.207311,4.439830,6.547543,6.345535,-7.424865,-1.617353,8.171530,-3.950288,2.933106],[8.347109,-4.597742,7.306927,-4.590500,9.596403,9.859489,1.232991,-0.398091,2.906558,0.496695,-0.721937,3.272843,6.501440,-5.356284]],[[-1.175263,-4.095350,1.799103,-8.517082,6.375670,-2.054776,-4.221110,-3.500839,-5.596502,-6.749145,-5.659069,-5.422034,6.670853,4.663612],[-6.384018,-7.135176,8.026630,3.713447,6.273086,-1.061936,-5.327047,5.763754,-6.710572,-9.019485,6.035999,-5.633446,1.137401,-9.270523],[7.049709,1.382654,3.561417,-8.774413,-2.839393,7.953666,1.886034,3.531831,9.738166,-2.210755,-2.869956,-6.993804,-9.676917,4.760240],[9.138254,-0.103679,4.751316,3.161111,-3.403313,-6.064839,6.531137,-4.179902,2.722981,-1.004756,6.910749,-6.174624,-4.728946,9.150060],[-7.870590,-8.523090,-2.639063,-4.471106,-6.572305,-8.437288,7.527138,0.164050,3.457102,2.626942,4.366346,8.826996,6.242710,-3.313012],[-1.371430,-8.478026,-6.914134,-9.386773,5.558359,5.965651,-9.356600,-4.564327,-6.998440,-7.602873,-4.000770,-1.678325,-3.998721,-9.147887],[1.618334,9.423881,-0.312284,-4.849815,-0.036906,7.742487,3.367176,1.240399,-4.715257,8.699771,3.817637,-7.506084,-0.555469,-1.387520]],[[-1.548103,-3.164978,9.812786,2.505659,7.816361,9.059197,9.666818,3.506669,8.454938,-3.597966,8.806679,-4.200984,-3.056255,-5.656506],[4.381850,9.868570,3.553085,2.066011,6.639431,-4.699413,2.773264,-6.678101,-1.604273,8.371270,-6.659591,0.736276,-0.951223,-8.947778],[7.219024,8.949567,1.096913,-7.973898,-2.378297,-0.410519,5.396036,-4.879222,-5.030030,1.603926,-5.147039,-4.226687,-6.735800,-2.049923],[1.554837,1.809830,8.430073,3.282015,2.269894,8.551494,9.905060,9.111975,-4.735470,6.418647,-1.662489,7.607375,-6.359173,8.446139],[-2.755056,2.641499,3.787771,-6.038853,9.262074,3.807464,1.435115,-7.335336,-3.424336,4.040363,5.962519,1.274282,3.411587,-7.939057],[-2.828866,6.135602,-5.428132,-9.752055,3.753294,-0.117059,-3.946071,-9.728719,9.583176,9.930750,-1.192560,-6.790357,7.425169,-6.329629],[3.714949,-6.773446,-6.691687,-5.327483,-8.199253,-9.737919,2.944598,-2.386059,3.051479,8.328557,8.883751,-8.337059,-1.555196,5.864578]],[[6.050459,-4.104610,0.746392,-8.003955,-5.695375,-9.251565,-0.222710,4.597050,7.929069,0.652055,-1.771081,7.612384,5.644714,7.643345],[5.093540,-3.604428,-1.340419,6.162768,4.658221,-3.375526,-2.564088,4.230450,5.807426,-5.593597,-6.868915,4.449019,-8.292504,5.433822],[9.093627,2.626303,3.880219,3.253999,7.298571,6.986668,-2.374707,-5.643144,-0.108580,3.581522,-0.369787,7.088441,-7.399615,8.645746],[0.727415,-4.935294,-1.037398,6.414639,0.739908,9.924189,9.746868,-3.604695,-4.706836,-0.557644,-6.891868,3.595899,0.401783,8.480426],[2.556726,1.001347,3.508926,4.855297,6.526131,-6.249090,0.846576,9.108960,-0.719569,8.552865,0.379266,-6.381784,9.781636,-7.626323],[-1.655942,-6.696011,6.021627,-9.291136,-3.077384,-5.575154,5.518929,-1.089885,-1.426827,7.268969,4.477369,-9.100673,2.707797,-2.237861],[-1.084834,5.711140,5.199470,-5.650867,0.871816,0.974585,3.161676,-8.368109,-3.799255,7.863368,-9.457505,-3.155175,3.957717,-2.418326]],[[2.068275,-5.982049,-2.233221,-8.406856,2.183057,-8.959409,7.223228,-1.789432,7.313112,6.143752,-2.145268,-6.741876,-5.520403,-4.426460],[0.842477,-1.775698,-6.340480,-3.656932,-5.261965,-2.614698,-5.256880,2.711044,-6.172843,-5.468236,-6.574440,-5.360575,-0.993139,8.791258],[3.718822,2.926853,3.502557,3.467097,-0.636176,-6.100928,-4.954623,-6.464508,3.861912,-6.757504,-9.240712,2.861327,3.829287,0.287480],[-5.229467,-5.697634,-8.150610,5.009899,6.357971,1.066809,-4.165744,-1.171164,-2.931733,7.632417,-7.424003,-3.753364,-9.940663,0.391304],[7.990768,-8.386317,-8.675425,8.716633,-1.917110,-9.265592,4.952884,9.758639,0.860075,-8.496664,-7.157459,8.464091,6.127213,0.163435],[0.747786,5.773063,8.895531,-7.135788,-5.600459,8.733050,-3.149048,-1.234980,5.523913,-0.172499,-5.214430,8.911459,-4.603809,6.431668],[-6.868561,-3.573198,-9.649628,-8.831590,2.650799,3.966513,-1.697249,-1.360544,-6.817848,-0.587704,-6.590424,-5.099237,3.324144,2.171910]],[[-0.056652,1.326171,-4.313063,-6.264737,-8.905567,-4.452941,0.590854,1.411433,-7.290607,8.189304,3.146364,0.606929,-0.364009,-7.682458],[3.149306,9.334734,-8.461377,-4.250878,-1.883492,7.735748,9.077640,-7.649128,3.157670,-7.990783,6.462605,-3.042542,3.809738,-1.908301],[9.076275,3.990414,4.488954,-1.877166,5.587688,-3.578071,7.341776,-6.965038,9.611131,-8.821784,1.066787,0.481263,-0.821184,0.079194],[9.811001,4.773945,-4.885356,6.029241,8.967549,1.859976,-1.280040,0.127364,-0.243449,-7.483686,-8.663006,-4.644238,6.347293,4.239190],[-1.594537,3.895637,-6.380545,-5.178956,6.597121,-9.155827,-9.820107,0.825812,7.621172,-4.113686,9.523004,-8.441365,7.152781,1.479814],[-6.049714,-3.567239,6.726336,-7.990246,-3.471093,-5.115851,-0.240672,6.457991,-2.977933,5.706648,5.004064,5.501900,-4.770866,-1.330136],[2.006550,-9.882844,-3.436230,-2.855642,-2.843486,-5.573804,6.867396,-7.554027,9.955085,-1.796471,-5.689294,-1.376364,-7.089107,-5.965562]],[[2.146045,-4.044839,-1.122931,-0.253450,-0.563126,-5.184353,3.912996,1.839556,6.080747,-8.577050,6.734348,2.834398,-2.323447,5.944118],[6.421128,7.019733,4.498458,2.812163,-8.337457,-6.072040,-0.610832,2.293439,5.630462,3.675301,-8.800778,-3.112913,-4.964512,6.922338],[3.285733,2.196364,5.594611,2.091925,4.503878,-9.280785,-7.048400,-9.192969,-1.993577,-1.636423,-3.937365,-3.349865,4.938884,0.326883],[-9.922997,-2.392726,9.491159,4.595725,-1.656678,7.603166,1.005759,1.785534,5.687350,7.186623,1.907307,2.441153,1.026010,-0.678353],[-8.408846,-2.781221,-0.215126,-4.848941,7.832684,-1.830238,-9.304120,9.179204,-0.456822,7.225776,-7.964376,3.125275,-4.259890,7.577041],[-6.011860,-3.804125,6.762655,-3.358636,2.758858,-5.718771,-2.251259,-1.288711,-6.863891,-2.697376,-5.694054,-2.898826,-0.438694,-5.040831],[0.235203,-8.944513,7.056900,-1.854457,-1.108470,8.418179,-1.742217,-4.632440,-3.089558,0.178210,-3.765861,3.284731,-7.089228,8.070670]],[[6.102912,2.269705,5.652007,5.189546,4.914524,-3.716715,-6.773391,5.770699,9.449320,1.424116,1.752861,-6.799663,-6.204365,-5.381342],[-0.568587,-1.272905,-9.575379,-3.617024,1.842544,-5.683141,3.338032,-6.918649,-3.786966,-2.052316,8.741586,-8.272656,2.300205,-4.939617],[-1.848632,-9.945475,-6.204874,0.805973,-4.765098,2.543400,2.327188,-8.190952,-2.983892,-4.398323,1.074208,-8.924308,-0.145897,9.217296],[2.400609,6.110426,-7.340115,-5.397521,-9.153308,0.109057,7.658658,2.008190,7.258898,-3.783816,-1.374724,-9.930180,0.533285,2.307986],[3.497146,5.363020,-6.787810,1.467601,-5.050378,-7.428482,9.824554,-0.165993,-9.659796,7.763105,8.713911,2.361918,-2.024021,7.274294],[-0.481033,9.380073,9.984249,-7.853674,0.845643,1.123769,-2.803852,6.873142,9.509609,-8.401687,0.822762,1.693397,5.078749,-9.407159],[4.572182,-3.802300,-7.777040,1.305826,-6.712723,-6.808592,6.115989,-7.230513,9.824176,3.931965,3.569234,-0.941152,8.639987,8.726219]]], dtype = "float64")#candidate|8252|(12, 7, 14)|const|float64
bop_8253 = relay.less(call_8238.astype('bool'), relay.reshape(const_8252.astype('bool'), relay.shape_of(call_8238))) # shape=(12, 7, 14)
bop_8256 = relay.less(call_8239.astype('bool'), relay.reshape(const_8252.astype('bool'), relay.shape_of(call_8239))) # shape=(12, 7, 14)
func_6354_call = mod.get_global_var('func_6354')
func_6355_call = mutated_mod.get_global_var('func_6355')
call_8267 = relay.TupleGetItem(func_6354_call(), 0)
call_8268 = relay.TupleGetItem(func_6355_call(), 0)
output = relay.Tuple([call_8211,call_8242,bop_8253,call_8267,])
output2 = relay.Tuple([call_8212,call_8243,bop_8256,call_8268,])
func_8285 = relay.Function([], output)
mod['func_8285'] = func_8285
mod = relay.transform.InferType()(mod)
output = func_8285()
func_8286 = relay.Function([], output)
mutated_mod['func_8286'] = func_8286
mutated_mod = relay.transform.InferType()(mutated_mod)
const_8287 = relay.const([[[1.155273,8.988871,6.124148,-1.220228,-5.616870,3.394096,-6.729811,2.820621,-5.297497,4.888358,8.999991,-8.999003,-9.019794,6.104559,-2.204899],[-3.956679,2.904032,3.118302,-3.910994,-3.342211,-5.941502,5.766887,-6.993559,4.604892,5.757085,2.977868,-4.315303,3.111007,6.059244,-3.821485],[8.697689,8.056810,-7.590106,8.925298,-1.992405,1.341414,9.077003,2.662311,-3.969178,-4.558755,4.940777,-2.637766,-7.217323,-4.113547,-9.021277],[3.662929,-4.487759,-2.246783,9.682318,6.327881,8.650668,-2.882525,9.674591,1.675194,-0.141369,-6.330337,9.042313,2.614615,-4.852184,0.617778],[-3.798148,-2.661779,1.462173,7.776846,3.689147,-1.686170,1.116530,0.523712,8.193490,-8.594544,0.081637,1.647674,6.550562,-2.724938,2.234205],[-6.516399,-0.796297,-2.940014,-5.713017,-8.261679,-4.739485,-0.160673,5.677253,-9.478149,-2.129803,-3.490087,5.778400,3.140895,-0.344305,-0.924350],[3.018268,1.407251,-0.828890,-7.426402,2.392855,-0.243615,9.964348,4.053443,-4.093329,2.698102,9.981007,-9.998126,-6.834984,9.319229,9.388350],[-1.345302,4.603637,-9.067606,9.457972,-2.609154,1.082987,-7.935758,9.559096,2.467595,9.358597,3.089309,-4.981048,-4.525644,8.537123,7.748044],[1.311873,6.797888,8.378464,-6.593310,-6.049964,8.640199,6.472285,7.336612,-8.658332,1.435456,7.907078,-3.829793,-3.300400,-8.365444,-9.008726],[2.918391,5.430783,-4.165628,-9.046579,5.925919,4.828401,8.404037,-9.505708,-8.373885,6.759366,3.346653,-1.281446,4.159741,-7.689390,-0.044432],[5.160468,-8.829698,-8.467038,-3.664730,-4.473799,-7.571372,-6.384842,-3.848832,-8.005303,7.759420,-1.507237,-0.393935,-9.011831,-9.147116,-5.877059],[-7.794342,-2.929000,-3.279912,1.184777,8.509748,5.112713,-4.302774,5.545169,-8.839876,2.387446,-9.915060,-9.941183,-8.850186,-5.389636,8.799818],[4.334387,-3.929419,2.694813,-5.606041,1.952010,-9.201097,6.358147,8.295195,0.064682,-4.416659,8.183440,3.913332,-0.253163,0.558873,-8.458548],[1.411945,-7.144396,8.160116,-7.785134,-9.569174,9.005531,-4.695830,9.047673,-3.334164,-0.454866,7.435005,4.279727,4.904239,-9.002003,-6.010700],[-5.667786,-4.244081,2.038926,-6.966379,-0.198617,-6.753279,0.307308,-8.084566,-7.056708,0.570768,-4.557763,-2.469745,3.529713,6.803818,-6.091273],[-6.833042,6.616019,2.390159,-6.723802,-4.253265,9.951249,3.952823,-7.166354,0.346149,-4.763222,0.536337,-6.733148,-4.904758,8.287885,6.207095]],[[2.649535,-9.726372,4.732643,0.009254,4.230663,-7.300211,-0.504166,7.315253,5.691116,2.122641,-0.244925,-4.595741,9.078239,-8.102666,-0.259279],[-9.794625,-2.794997,-7.609719,0.827895,2.616440,-7.769276,5.338615,3.732939,8.327890,2.281278,-9.942661,5.739898,-6.519491,3.466340,4.911476],[6.267367,0.961075,3.313948,9.722851,-0.816970,4.203556,-4.801386,5.609997,-9.144190,-1.354830,-0.922256,5.706748,-5.980365,-6.699413,-7.585304],[5.357400,1.466712,1.005761,6.376254,4.843057,-6.938564,-0.708915,8.637604,-2.111485,-2.844172,-7.759473,-2.736924,-3.305703,6.995463,-7.046466],[-3.216608,4.559977,1.337099,-6.818669,1.626333,-7.778557,3.129078,-5.466693,-4.464950,-5.972368,-0.567132,5.349325,-0.551267,5.849893,-9.621884],[0.868451,1.811756,4.011447,-6.371137,7.229616,2.306945,2.416543,-9.074423,-4.898799,-2.050165,0.442627,7.926786,2.309267,-4.449465,0.432649],[1.581506,-1.275839,-3.362478,1.176636,6.737508,-9.730294,-2.562967,0.583412,-9.806814,5.500711,-0.573259,8.950913,-2.232874,2.909867,0.738549],[0.179151,-2.504744,0.568868,6.169141,4.886704,-1.587934,-0.478776,5.457724,2.338879,3.455392,-0.870079,-0.023086,0.246144,5.373197,5.736638],[3.050417,9.295048,-4.715640,-3.895540,5.836117,9.483117,-6.892526,-4.969129,0.992341,3.198870,-1.558142,0.163475,8.607457,4.256690,7.718534],[7.954594,-8.046883,-4.170703,3.036927,-8.676051,-2.577505,-8.912772,6.743836,-9.628505,4.088780,8.576502,-5.861476,-1.121129,3.968972,-7.654124],[-6.234851,-5.541464,-1.786311,-5.209427,7.119258,-5.288163,-0.198309,-9.851475,3.424441,-7.746789,-5.898003,-2.994690,-7.592403,-1.931107,9.806323],[4.577937,-5.233237,-0.237756,-8.420285,3.078506,4.720733,-8.377425,-2.673461,-0.677865,3.601081,-6.857656,-2.530659,-6.966256,5.117655,1.156037],[2.759931,7.131367,-2.133918,-0.174009,-1.357586,-2.825504,0.095429,4.347518,-9.548595,4.231934,-5.275698,1.574935,4.546739,-9.353696,8.078493],[7.135299,-4.694986,-5.472929,-5.557028,3.323703,-4.224602,-0.886313,-4.392872,-1.346491,4.080419,5.824930,8.963906,1.826523,-9.141607,-8.608599],[6.907496,1.764454,-9.128183,-5.639770,-2.504245,1.652719,2.588818,0.835911,2.588567,-0.417935,6.347612,-8.556700,9.590992,7.999725,5.837894],[1.458866,7.241770,-4.193592,-4.387828,-0.697265,0.306608,-7.701119,-5.387551,-1.074721,2.183113,-6.581724,-0.076001,2.960523,-5.361880,-2.964592]],[[-7.732653,-2.730701,-9.939901,0.762777,4.317016,0.553334,9.030830,-0.600154,7.436205,9.070316,4.346403,-6.119361,5.783349,5.393337,-1.475793],[5.713831,1.196597,6.175452,8.112031,5.246531,-2.885043,7.678368,-3.531217,8.176636,-6.315226,-6.843438,5.771846,-6.908389,-6.694966,-0.232316],[7.005229,-1.806327,-5.232129,-4.333631,-6.553792,-7.263996,-1.919213,9.192439,9.196550,9.741153,8.621238,-7.261161,-6.227496,4.140301,-5.939428],[2.665645,-4.000956,6.707355,5.706140,-7.834873,0.754093,3.814297,-8.540228,-3.002308,8.702203,1.376274,2.968502,5.499643,-9.006680,-9.515026],[0.153981,-3.374803,4.779837,-0.979600,4.492510,1.050882,9.538589,8.525534,1.986963,-0.282202,9.189782,4.515665,5.701418,-6.638360,-6.614185],[-6.674113,-1.350776,2.875190,-3.639705,4.701231,-4.135471,-5.447487,5.658591,2.612890,1.277086,2.728849,1.085565,8.241456,-6.426129,3.442466],[6.790879,-6.111225,-2.171728,5.864094,1.798965,5.095932,6.167736,5.640617,1.611034,7.661924,-8.454590,0.248149,-9.233609,-1.620957,-7.772180],[6.782233,-1.124640,6.165264,5.490700,1.432616,6.010409,-4.272372,7.852413,2.289429,-5.759859,7.572783,-5.324123,-2.201680,-0.987419,5.526034],[-2.550451,-4.253780,-1.392820,-7.295677,-8.025905,-3.731944,-9.937825,2.553945,-5.039130,-8.035780,7.862800,-2.524582,-7.213396,-3.324309,7.943087],[8.300694,-4.818458,-0.748137,9.015762,-3.764512,6.620021,-1.015481,2.957441,8.410383,-9.735399,-6.829405,9.702112,2.116927,-1.527280,-6.072946],[4.329331,2.453677,4.708611,-0.829646,-5.381190,5.293219,8.523809,6.982467,2.117825,8.267313,-1.023285,4.503742,-2.623609,4.046132,6.084691],[-2.428847,9.257533,-7.679146,-9.546111,-3.318305,-5.314861,-4.154732,2.798279,-8.956775,-8.593515,-7.344982,-3.464746,-0.662264,8.373138,8.348646],[-3.941133,2.422561,2.810536,-0.323303,3.487296,1.719714,-3.143948,1.680672,2.884052,-4.162102,5.557864,2.359312,0.910131,-3.396067,8.558640],[2.385487,-5.127681,-3.895896,-5.120524,2.800968,2.976037,0.951960,-8.136324,8.835675,1.286639,8.432162,-1.735021,-8.356684,-8.133146,-0.295699],[-3.759076,3.787263,9.234330,-4.119967,9.326728,8.559582,-9.239139,-0.074262,9.055082,0.976004,-9.032081,-4.559795,3.858442,-0.140225,1.574491],[9.737663,-9.694930,-0.470893,-4.600790,3.732011,-9.390534,-4.750810,-7.683152,7.343247,-6.450873,-1.036969,4.264982,-7.679207,3.313149,2.256527]],[[3.411909,-8.408299,0.392438,5.895931,2.554254,7.547132,5.617982,2.699116,7.228178,-9.899505,1.054383,-4.881343,5.359969,8.921127,5.797453],[2.465799,4.407716,-1.579228,1.642734,1.006200,-6.906959,-8.346603,-0.385836,2.213141,7.821072,-4.046002,-5.641275,0.629358,8.802205,-1.501837],[6.477833,8.324471,5.548578,-5.394747,-9.722197,-4.261083,-0.325158,-7.555949,-8.007765,-5.229483,1.229349,-1.830592,6.536988,2.232697,-3.180352],[4.356010,-2.700919,-1.062257,-5.790394,-6.858509,-1.997863,-4.944247,6.363837,-9.721715,-8.377212,5.092299,5.512851,-2.643435,-8.845617,4.300466],[0.987389,-1.791726,8.019658,-7.979867,8.135656,-3.077573,5.549282,1.558040,-1.077022,-3.837703,-9.368151,-5.090162,2.916055,6.776104,2.787621],[-3.887205,4.076888,-9.276000,0.847933,7.291568,1.797176,3.229549,-6.922380,3.957295,-8.337214,1.711937,-5.530371,-0.598723,-3.591959,4.886279],[-9.921942,0.477777,-9.386082,-0.226718,-1.619420,9.240334,-3.823716,-0.086877,8.959018,1.642292,2.516667,-2.765470,-7.502222,7.696281,-2.455301],[-2.735918,-6.556717,1.684427,5.861578,-2.149676,5.587182,9.002510,-3.093856,-6.755736,-6.352111,9.224286,-5.518446,9.446932,-1.838095,-4.330038],[4.560121,8.016544,-5.231487,-8.657723,6.415496,6.428362,-0.230466,-0.378162,-3.779558,-4.290956,-4.221726,-8.780567,-4.197176,8.135235,-8.337789],[2.658668,7.573584,3.869734,9.607963,4.700440,-1.548007,4.043995,-9.564113,-8.120362,-3.062682,1.659389,-1.179245,-4.481115,1.701182,-3.517494],[7.122403,5.837204,-5.231708,-7.144801,-6.613178,-5.894792,-4.277027,-6.706308,6.663378,3.719342,5.730303,-9.180776,-4.956911,-5.665579,3.028087],[4.814304,1.299554,3.254157,6.961462,7.826715,4.228109,-1.058638,-7.398623,-3.654050,5.231518,1.458264,-5.338696,8.791009,-7.320135,-4.356909],[-7.898257,-2.073306,-4.432136,0.344566,1.723989,-2.632193,7.223093,-6.794646,5.996124,5.285384,-8.940373,5.524446,6.097102,8.998461,2.174514],[4.586502,8.272844,0.724974,2.919988,0.979997,1.320362,6.876869,8.125663,-5.275833,1.732642,7.307837,4.364066,-0.752044,0.617856,-5.416126],[-2.418570,-3.810540,-1.603861,2.746121,8.301472,-9.369611,-3.789543,9.157899,-7.183044,-6.276531,0.733068,1.531689,9.560709,7.286318,-9.574778],[7.101613,5.060138,-8.545108,4.814236,6.611279,5.826380,2.415351,-7.690458,7.084468,1.699562,-3.392666,0.967597,0.355018,0.619466,-9.069384]],[[-4.044192,-5.251070,1.904550,6.887605,2.581528,6.502410,1.421940,-5.705216,1.748984,-5.435182,-7.937268,-4.845441,-9.642392,-4.642895,-9.021668],[9.183650,-6.302710,3.079639,1.101935,-0.231124,7.592048,9.346860,-0.521808,-6.149251,9.255052,-6.373601,3.301760,3.338140,-3.771052,-8.325534],[-8.237515,-9.899472,5.012167,0.488533,-9.679529,3.549094,1.727006,-3.929132,1.551405,-4.293101,9.069407,-3.989253,4.523723,8.556916,0.960765],[-4.624896,5.878808,-2.311573,-9.051884,9.334768,7.716730,5.678676,9.227724,-8.296853,-6.102050,0.874827,-6.364468,6.336389,-4.236514,3.744727],[-9.172491,7.404512,-4.071135,-6.127769,3.427456,-9.753137,0.877190,-9.311883,7.256418,9.649150,9.682077,-9.342784,-7.147450,7.182403,-2.498741],[-6.678189,-5.527187,-0.058884,1.906359,-7.116371,3.324246,7.492823,-1.744663,5.245244,-7.393599,3.457581,-6.843078,4.195963,5.031074,7.534666],[-1.735700,-4.122163,8.582784,7.407878,-4.247947,-1.825231,-5.175081,-5.930533,7.468957,8.846189,-7.104594,8.671410,-4.719352,4.240281,1.759581],[9.913687,-5.667422,-9.827246,-3.563601,-7.480216,5.946974,-3.842916,-0.421399,-2.114443,6.567630,0.201452,1.327279,-5.281552,-6.200412,1.386864],[-2.020111,2.349911,0.136690,-2.550218,4.239918,-3.058300,5.470792,7.875016,3.033802,0.807343,8.074853,-5.886606,5.045021,-7.289452,-6.447033],[0.665591,-1.837699,8.125202,1.944298,5.955282,-7.671520,8.405544,2.924038,3.518798,3.507302,9.732502,2.714560,9.534880,-3.077035,-5.456765],[4.023285,8.850162,-0.441454,8.974266,-2.785242,4.990725,-3.152115,8.353117,5.624578,-3.422544,5.164634,9.332713,5.254476,-5.717888,-7.014977],[-6.116954,-2.567478,8.646672,-8.271326,-4.635713,6.520100,4.638982,4.878382,4.386194,0.940112,5.124795,9.286585,-4.975923,3.727480,-9.507447],[3.207124,1.807748,-4.377920,7.929898,-0.757087,-2.780766,7.548172,7.883153,-1.549203,8.593134,2.430313,-4.727564,1.249871,2.878582,8.213413],[-6.534016,7.057433,3.204188,-0.540394,-2.478631,-9.021269,-5.520757,5.133263,-1.040407,7.317476,5.519785,-5.439842,9.224327,-7.658261,-3.245865],[4.582477,4.102455,5.651620,-8.413598,7.974436,-4.557794,0.398575,1.844626,-2.484728,-4.121945,8.293682,-0.120549,-5.903157,9.321947,9.924337],[-0.370111,-9.249375,2.121993,-8.148840,8.929648,-7.729984,-8.729029,-1.430148,-0.865619,1.186082,-3.012293,7.421967,9.815051,6.605809,-9.641440]],[[-7.254705,1.553116,-4.040577,-0.409810,-7.376075,-4.332187,7.542238,0.968305,-9.338185,8.746783,-5.359470,-1.754476,-6.362626,6.140939,-1.829045],[-5.711219,4.961091,3.356090,-6.828908,-6.395647,1.737823,-7.549198,4.870993,5.658036,0.632048,-5.803821,-8.941992,3.696397,-4.424543,-0.829688],[2.175932,3.486891,-1.047613,-0.020029,2.141739,-6.815726,-3.180914,5.624285,-0.136625,1.337587,5.682666,2.870761,9.759187,9.536379,-2.374774],[-6.861034,-0.188604,-5.333723,5.624520,-9.884781,6.471326,5.327367,3.277905,-2.946089,3.632008,2.767319,2.759352,0.629581,-0.133727,-3.648031],[-6.177107,-8.040888,-4.609586,-2.877968,5.346281,-8.646266,8.455962,-6.802935,5.242318,-4.055815,9.835555,2.094678,-3.655558,7.509285,4.847192],[1.584372,-1.720782,8.302749,-9.761715,-9.387135,-5.777826,5.983191,4.835437,-8.219763,-0.760579,6.780239,-7.265290,-8.620237,5.240811,4.433979],[8.166869,4.264820,-1.689737,-3.710545,-2.218978,7.948255,-0.648098,-6.652662,-5.452894,-4.030839,8.037055,-8.228305,-3.115641,-0.246123,-2.816280],[4.385075,3.069275,-7.096287,7.293141,-8.686224,6.840289,-6.764248,-5.815787,2.715952,3.773704,2.410296,-8.621196,-1.638290,-0.079490,-6.861376],[8.218305,-1.116864,-2.728024,-5.656088,-0.328530,1.347255,-8.593743,5.137954,-0.700561,-2.860694,-8.917296,-9.546432,8.990896,2.393680,-9.576490],[8.631013,4.673081,-4.484125,-5.108459,9.704050,5.005032,-2.386591,-3.476509,0.889073,3.538567,-7.586468,0.767844,-5.057992,-4.535834,7.962416],[9.166836,-2.395193,-7.562150,0.434397,6.945476,9.119443,6.824605,8.761375,1.173224,3.326221,-0.347520,-6.680207,-4.176960,-3.243546,6.159367],[0.624206,-1.362282,3.898592,-4.771384,9.837664,-1.835637,1.399082,4.314791,6.996290,2.729797,5.515510,5.104833,0.302685,-2.949089,-3.639299],[3.267172,-6.441011,8.090649,8.714358,-1.964237,8.154988,7.695025,4.790804,7.313517,-1.490120,1.940674,-4.206739,4.010767,-8.698060,-3.270191],[2.515959,9.681643,4.097909,-6.211894,-8.457569,-7.750127,9.254905,-5.526328,-8.854634,2.201092,-2.075909,-8.665395,8.389055,4.711428,7.700758],[-4.233567,7.378335,-6.545958,-4.253341,1.690071,-3.193952,8.265510,-9.334886,-5.316156,6.732720,3.211374,-7.514090,6.759937,6.355707,5.816158],[-9.646640,-8.973342,2.931044,-0.301559,3.811866,6.305208,3.732578,9.707981,-8.392398,-3.917730,6.641318,-6.842005,8.041148,-4.040815,-1.632599]],[[8.594471,4.347826,-2.258707,4.327782,7.984672,0.980344,-8.319087,7.111978,-1.120410,7.749818,3.992032,-5.939061,-6.389538,7.111548,-3.229867],[-5.127906,-2.574560,4.378190,6.633263,-7.886622,8.938321,4.424371,-6.141420,0.182279,-1.444086,-2.328398,-2.510291,3.856107,-9.308803,5.129178],[-6.087878,9.508649,6.814079,-2.906688,6.644638,3.231128,-9.081007,-6.881136,9.089545,7.806818,-9.874229,-5.287237,-7.371470,3.688397,-6.884145],[5.702463,-3.895665,-8.902524,-2.706765,-5.123008,6.018587,-6.100604,-3.538776,-3.186870,3.541851,-9.153715,8.872247,-7.439505,-5.985742,2.090296],[-8.252389,-6.329442,3.307385,-1.641194,1.694037,2.405480,5.625650,-2.089601,-2.673316,1.487709,-6.691571,6.519614,-1.597052,2.484501,6.213318],[-7.646139,3.385604,-3.484254,5.605661,-0.902766,-8.036655,8.242775,-9.950826,9.413415,-2.259156,-5.547385,-7.783115,9.338551,1.364178,-4.789815],[0.224553,-5.952636,5.349920,3.971859,9.067808,2.316983,5.817250,0.198810,-8.266142,-5.396385,-5.574794,6.910121,-3.388166,0.605682,9.794325],[-1.150926,-4.834589,3.743453,0.957315,-3.942343,3.443855,-8.438860,-6.126274,-9.854244,9.235236,-7.857894,5.386685,-2.302222,-2.639735,8.500390],[8.472562,-1.253485,-1.129784,7.703697,-5.314986,-0.707158,0.404377,-2.072603,1.650715,-3.708514,0.605802,-7.681882,-3.784535,-6.138836,-1.356619],[-1.235311,4.358976,-8.659645,1.141620,2.857281,0.354646,6.487503,0.507348,8.690593,-0.465306,7.385484,-8.213587,-9.634591,-5.550771,0.982530],[-2.869814,1.801580,-4.597534,4.901056,2.778320,4.772286,-2.020302,-5.242544,-1.256408,-0.013070,3.464525,-7.693719,0.057143,8.201641,1.859632],[9.999444,-3.478401,9.572377,-2.229848,-5.110801,8.977477,-1.738912,-0.003632,9.026658,-5.213986,7.450528,7.371136,8.200011,-1.005374,5.981122],[5.384021,3.234352,9.168325,-5.946001,7.329959,4.335567,-3.447204,8.708537,-7.989701,0.703929,-6.187076,4.033207,-4.567187,1.928441,6.581307],[-7.198941,4.408781,-0.326946,-6.767066,-6.831104,-7.767399,0.316275,2.587154,7.927852,5.521015,6.318134,-3.042664,-8.316551,0.722881,3.941227],[-7.221434,-3.187305,-9.991988,-9.872062,4.727734,-0.897315,-2.356699,3.634501,-0.016572,-7.861312,2.338330,-9.740241,-8.896885,0.834279,-8.155060],[-9.908203,-5.413638,-3.784264,7.415802,-0.679814,4.374731,-7.613275,-9.525212,6.122046,3.460269,-5.613932,9.614037,-6.218276,7.632982,-3.558497]],[[-1.488747,-7.157507,6.737902,9.103755,1.235209,8.522621,4.574629,6.596147,8.976696,-2.332049,-5.187866,-5.749331,5.252911,1.079541,-9.317490],[-2.171325,-2.817915,8.044638,3.292060,-8.437852,-7.098216,4.446790,-9.486569,8.604495,-5.616791,-7.915099,0.805419,-7.296827,7.579522,6.768048],[5.450335,-7.163884,8.219467,9.036991,9.929161,1.508675,-1.487260,5.628586,8.860123,-2.811663,-2.419271,-9.161105,2.963169,7.308434,-6.433274],[-2.457114,-5.416067,5.887418,8.285480,1.187761,1.041720,-2.611026,5.086629,-7.179902,9.752286,-4.414935,3.120344,5.287947,-2.860200,3.141518],[7.927659,-5.699585,-6.273637,1.678664,2.376737,-4.015600,-3.941340,-1.383002,-4.327481,-1.838831,1.572836,-3.864162,-1.249725,-6.914138,-5.813582],[2.485582,7.865790,9.799457,-0.162254,1.877844,0.249562,-5.429339,0.479190,-1.734627,6.086251,6.998851,6.151610,2.287109,8.649848,-0.180936],[8.301179,6.478259,-2.048605,-1.029658,-9.444091,-1.821779,-2.557443,6.668655,3.932171,7.331807,-2.205202,3.110989,-2.244866,8.155357,-2.144648],[4.520423,-7.974027,4.999281,-4.309560,9.017629,3.170679,-5.312117,-0.524181,8.597514,7.768537,-9.772282,2.402273,-5.040923,-7.629341,1.647300],[8.386053,-7.106557,-1.531056,-8.688986,2.276002,9.827145,8.270174,-1.693912,7.059812,3.440895,6.316581,-0.419234,-3.102273,-4.658742,5.483516],[7.363204,6.456569,-7.024428,3.575576,-7.583859,-6.081519,-2.634706,8.169124,6.994733,-3.487968,-2.613053,-7.280082,6.054785,0.755228,3.760196],[6.559985,5.015174,-2.220583,-5.791237,0.522198,-7.650310,-8.844216,9.920828,-9.000864,-7.681909,-6.589520,-8.926214,-4.527450,2.633722,2.383224],[-5.452524,0.754401,7.533917,1.166328,-0.490148,-1.797489,-0.780418,8.458180,7.948565,-6.041594,-6.855403,-8.146823,2.097577,-0.530477,-7.426315],[7.621134,1.874707,-8.310783,-8.086443,-7.986838,-5.891367,6.426919,-7.829417,3.490798,-2.760265,1.355046,-5.339610,3.822040,-1.204676,-0.831428],[-9.639200,8.047667,-8.067972,-6.588479,3.161601,6.636226,-6.472048,-7.055859,7.935689,-5.499611,5.463586,6.766271,4.511178,7.297780,-8.955170],[-8.454586,0.326642,-8.341658,5.342360,-9.868504,-3.540865,8.226569,5.281387,3.831695,5.041229,-3.622372,4.254949,-4.022432,7.905856,8.188889],[4.123533,-2.015683,9.440390,-4.040289,6.699472,-8.291877,3.410209,-0.306538,4.018518,0.312968,6.833784,-1.279750,4.941337,6.884845,-9.045130]],[[5.886982,-3.120798,1.560893,-1.214065,5.091477,-2.242917,0.800412,0.684265,-1.722114,6.950364,8.904476,-9.997210,-9.515196,-4.738686,-0.681715],[-9.266329,-8.642159,1.334924,-4.020776,3.150901,0.897298,7.016577,1.266838,2.641764,-2.115674,-0.164497,7.099629,4.690833,-5.014904,-3.142557],[-9.659895,-8.095288,7.761423,-6.469661,-7.254914,1.738736,-9.889206,-8.683465,0.207118,1.276888,2.251274,4.199945,-9.697264,-1.003728,-7.410796],[0.237380,7.046584,4.276224,3.984566,-3.315696,-6.374088,-2.130626,8.051307,-4.653057,-7.335187,-2.172769,0.470143,-8.401872,-4.866180,9.014610],[4.066647,7.619704,-5.417002,-9.440732,0.613378,4.035316,-8.394102,-5.766559,0.552616,5.442240,-9.321018,0.477222,0.531031,-8.062723,-7.872496],[8.310287,-9.485769,-8.882087,2.196792,8.621205,9.834643,-1.494455,-2.959043,3.987279,-7.375593,2.964255,-7.830645,-1.283975,-6.356491,5.050331],[-8.779759,2.816385,-1.623201,-9.299458,-0.109223,-0.500091,-4.767410,8.023715,2.763680,-7.223134,4.316591,-5.260696,-8.195513,-8.621629,6.964410],[4.002084,-6.396993,5.992667,-2.620011,-8.255197,4.317597,7.198253,-8.622200,-9.855863,4.443040,1.336892,-3.921807,1.212484,-4.777948,0.327014],[3.232631,-1.705652,6.598282,-8.097272,9.815899,-6.479906,3.462717,-4.800306,2.036897,7.182352,-7.362900,2.586518,8.027353,4.352942,-9.038011],[3.907531,-7.403925,4.847819,8.368146,7.367077,7.630391,1.540879,6.453296,-7.082759,-7.254530,-3.829705,-1.152109,9.670608,-5.156960,8.442936],[-9.412537,-4.437606,-6.910461,-0.270305,-7.052900,-7.199484,-6.205020,-4.537243,-8.034966,-0.178501,5.321376,8.858420,-1.522074,1.729510,4.568849],[-5.809976,3.440783,-9.872690,-1.423197,-6.376293,5.794902,-0.087956,-7.019831,3.292533,9.616400,-1.420989,-0.438130,-9.884285,-9.897345,0.537515],[5.803277,7.512379,0.483798,-6.527194,4.482106,-4.627575,-7.037995,-7.046550,1.717043,4.417828,7.690947,5.834015,6.149906,-9.237268,0.830452],[7.591835,5.010044,-2.939895,1.547179,4.834600,8.576529,9.598701,-7.368417,-0.075212,0.759190,7.933267,1.064901,9.420038,-9.860969,7.875857],[9.007173,-6.423799,6.319198,2.111272,-0.557120,8.881971,-6.661419,5.476598,-5.611489,2.641802,9.461006,-9.212073,8.882225,4.502316,-9.495504],[-9.054840,7.235136,-7.294841,1.553696,0.017184,-0.407595,2.658658,8.713412,-2.302508,-7.357981,-3.235214,-7.251755,2.931505,-7.401093,4.225390]],[[1.045012,-6.120062,1.080518,1.434268,1.658850,-8.058251,-1.414699,-0.825508,-7.606493,9.656628,-2.974717,-4.916162,7.233002,9.719865,-1.944969],[-7.783947,-6.434189,-7.843646,0.919961,-3.994505,7.025722,2.092187,-2.459865,8.241312,-8.990758,9.743019,-6.908035,8.266943,1.951941,4.333269],[5.866999,6.531582,7.660162,1.035317,-1.598127,0.614379,-0.773546,6.821946,-7.094130,8.732685,1.863991,-7.102718,-6.746134,6.161033,-3.954145],[5.313836,-3.791409,8.226381,7.685959,0.369458,-5.302328,1.609754,7.921621,8.126923,4.244899,-9.132606,9.102386,0.246994,-0.381466,-7.572219],[2.174946,-2.137705,-5.702146,0.243787,7.434824,4.211486,8.016213,-5.983077,1.729657,1.394797,4.896310,-1.374303,-6.573740,-4.155977,-9.838548],[7.157935,8.266579,-3.113659,7.412946,5.958080,-1.434140,-0.475330,3.491781,-5.843207,-5.186369,8.525068,8.805654,-2.343712,1.565061,-6.014521],[3.899686,-1.358376,0.346118,4.384487,-3.241836,6.225989,0.504239,9.600704,1.097830,-0.438764,9.017031,8.121351,2.572111,-4.551058,-1.268453],[-5.357461,-0.351711,-1.681632,2.495726,-4.360303,-6.762294,-7.618023,4.180692,-1.479885,9.217398,-3.702544,2.456461,3.663315,0.184279,1.067640],[-1.046103,-6.399430,-1.706024,0.423226,-7.379061,-0.456771,1.578538,-5.437126,-7.028543,2.673314,0.394253,-7.805327,8.478966,2.382184,2.270954],[9.397556,2.081575,-9.136505,-6.795551,7.600945,9.446583,-1.269548,8.526770,6.397312,1.346552,1.439317,-8.698875,9.682351,-4.833141,-7.242825],[-9.528144,9.481680,1.314464,0.797648,1.251603,-3.263765,-1.507270,-6.669090,-5.618259,4.700289,-6.579085,-9.595265,-5.123727,9.738943,5.728244],[-5.235655,7.978989,8.775895,6.941605,-5.347009,1.260800,0.968393,2.386307,1.130819,5.764795,-6.468468,-2.705575,-6.663333,-7.108832,3.926034],[-0.033408,3.444656,6.335850,-8.645400,-6.142127,-5.478900,-5.151233,8.797444,4.618165,5.957688,-3.976055,-0.631766,-0.604582,5.347672,-0.367093],[-2.828484,9.451638,-5.012184,-0.154319,5.385538,-5.954964,5.329248,-8.282859,-1.498723,6.530795,-6.726633,4.290109,-2.261910,-0.649471,1.382107],[-6.166447,7.080660,0.412855,9.564563,-1.361773,-5.193088,-6.537686,3.189431,4.246925,-6.020871,0.465543,-9.754846,1.755849,3.546401,-8.686415],[7.185161,-5.168744,-0.830879,-6.069967,-5.477451,9.865983,5.141117,-6.780766,-1.511689,9.772727,-6.251055,9.969788,9.447419,-4.568559,-2.828899]],[[2.420900,7.962363,-8.045426,-5.177887,7.186612,-2.937570,2.572596,-7.541937,-3.069898,9.998063,4.256514,1.559520,-8.191318,-7.441851,5.776035],[-7.266008,-5.048610,-9.395401,7.821437,2.740174,7.729135,8.141963,-6.883924,-5.627126,-5.200025,-6.093768,-1.770694,9.236763,-6.255249,1.841281],[-5.288916,7.686392,0.219191,-5.331027,-5.174097,-4.086097,7.422666,-5.079350,6.177648,-3.337679,0.430716,-3.416341,-4.945142,-3.585781,9.235676],[-4.727223,1.393006,-2.401321,-6.853931,-9.543483,-9.049551,-1.978055,-1.471010,3.074741,-4.285461,-6.124070,-8.657312,3.592858,-2.917321,-6.946112],[5.333909,1.722934,-1.272874,5.328427,-3.459741,9.292600,-5.406901,-1.888462,-6.804702,5.808983,-7.427420,-5.414708,-9.327596,1.326175,-9.781316],[-2.818769,0.602123,-2.862798,8.570892,-7.884766,8.166466,-7.527525,2.192590,9.684284,2.300017,-6.351437,-2.775943,-7.015569,-5.626677,7.780043],[5.189149,-4.933004,7.096351,-6.235864,7.365905,0.016149,-5.967090,-9.766190,-2.201925,-2.382612,-3.131119,6.959722,1.439047,2.744815,-8.455118],[-1.228259,-6.684669,-9.880385,-9.629536,-5.978048,5.772939,-1.799974,-5.048874,3.349936,-7.063115,-1.404848,7.749712,2.651621,6.235265,-5.958381],[9.824887,-2.545544,-6.063115,-5.076049,0.129302,-3.644626,-6.719504,2.240049,0.027134,7.435292,-7.553957,4.533003,-8.213265,-4.508710,6.893362],[5.007682,-8.626792,4.051379,-8.414515,7.934697,-0.542159,-0.669061,-8.499245,9.985987,-0.828376,-1.165126,-6.340686,-4.650674,-4.776283,6.046476],[-4.497613,0.199125,-0.291802,8.692697,-9.027401,-1.229906,-8.346252,9.391186,-8.709689,-5.481234,5.340807,5.487091,-7.815003,-9.980116,4.946508],[7.610296,-4.436966,-8.561489,4.262453,7.077561,-9.321212,-9.768640,-9.425760,0.475484,3.551919,-0.512985,-0.163840,-7.298792,1.532076,-1.038382],[-0.484498,-1.199798,-1.198491,3.737236,-8.418888,3.609147,6.327295,7.417414,5.687780,-4.332592,1.455657,3.108520,9.330988,-4.552114,9.196043],[2.806843,-5.825701,-8.499284,-5.641601,-9.789077,2.867214,1.180143,-7.080121,-9.763999,3.249317,-1.049349,7.007695,1.224990,1.113750,-1.089824],[-7.629078,0.572274,0.226988,0.471415,6.603601,5.220009,1.341171,0.189624,2.643308,7.423380,9.175081,6.554344,2.353271,2.986144,6.262868],[5.351277,8.770987,-6.786051,8.813606,-3.069133,-0.715378,3.689722,-6.432683,9.092630,-0.650896,-3.126664,-9.758155,7.641744,-0.994629,-6.990966]],[[-0.779991,3.584997,-1.928088,-1.736615,5.185265,6.497291,-2.264653,0.016049,7.557497,4.846826,5.024742,9.639832,9.538992,-5.737275,9.484674],[8.888294,-4.628220,5.419573,6.272204,-8.809882,-3.433895,-0.954745,-1.528060,0.215664,-5.917461,-2.585493,0.517834,0.924547,-0.370379,-1.758144],[-2.065705,3.516303,4.380345,-4.154884,-6.814919,2.074686,-1.790432,-5.081201,-8.097252,-4.768395,-1.557288,-5.860730,8.554701,-6.131869,5.022766],[1.418524,7.308064,1.287084,-4.238027,9.003326,-0.309933,9.211658,-0.669375,-2.860460,-6.673916,6.788257,7.259275,-1.766457,7.744142,-0.551563],[2.052741,-4.565365,-7.724530,3.257160,5.866315,7.948105,-7.240471,-6.000485,-8.734852,6.253814,-4.123851,9.668617,-2.898049,-2.579787,4.801031],[3.715862,-8.394511,1.184320,2.725124,4.988018,0.194268,-3.488648,-8.047307,-1.532624,3.321566,5.047810,-2.948484,8.917589,-5.673948,-0.476627],[-0.632342,-3.027353,5.633880,9.813952,8.924796,-6.712979,-5.874672,-4.252775,6.609630,4.725348,-3.429115,-4.971336,-9.764048,1.681975,7.528890],[-9.376908,0.792023,9.562687,-6.338787,4.568482,8.267310,-8.601987,8.690518,-9.664030,1.340284,4.375892,-1.821780,-7.433545,-4.739419,1.960192],[0.120897,6.253793,7.651696,8.472189,-2.591638,4.551903,-7.877756,9.841274,-7.715260,6.892137,8.962256,9.913094,-6.922512,-3.564130,2.503839],[7.030629,4.073494,-5.751072,0.555776,-6.336167,-9.350960,3.935779,4.269243,-1.168211,1.566606,9.894259,3.827415,-1.031888,-4.601786,-4.293531],[5.920940,-9.008629,-4.706779,1.974528,9.899657,1.842745,5.075177,-6.188519,1.901072,-7.419414,-1.479120,-1.224362,-3.784892,-5.594523,3.082631],[-2.580801,-6.262468,-8.427812,7.803523,-9.960231,7.133253,2.165161,-6.841728,-8.182744,-8.696527,-7.051730,-1.835690,-0.302321,-1.759068,-4.879377],[8.595255,-6.824114,4.840966,1.702665,-1.522669,3.050317,9.515888,-4.203148,4.623757,-8.573248,5.455853,-4.365316,5.061309,-4.045429,3.352743],[1.467442,6.077277,-2.204451,-7.702529,-0.218159,2.046506,0.369381,-0.076365,3.565162,-3.674064,0.401592,-1.283110,2.270503,0.099637,8.546421],[-4.121758,2.610373,-6.037893,8.372902,4.516278,7.536493,8.902417,-5.260641,-5.865702,9.016633,2.868630,-4.082785,0.473695,3.290658,1.545120],[8.254988,1.012957,-8.583181,6.357693,8.432076,6.798264,0.380582,6.606127,-1.392286,0.148383,-9.988792,-1.938085,0.783248,-4.524807,-8.668336]]], dtype = "float32")#candidate|8287|(12, 16, 15)|const|float32
uop_8288 = relay.sin(const_8287.astype('float32')) # shape=(12, 16, 15)
uop_8298 = relay.sqrt(const_8287.astype('float32')) # shape=(12, 16, 15)
output = relay.Tuple([uop_8288,uop_8298,])
output2 = relay.Tuple([uop_8288,uop_8298,])
func_8309 = relay.Function([], output)
mod['func_8309'] = func_8309
mod = relay.transform.InferType()(mod)
mutated_mod['func_8309'] = func_8309
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8309_call = mutated_mod.get_global_var('func_8309')
call_8310 = func_8309_call()
output = call_8310
func_8311 = relay.Function([], output)
mutated_mod['func_8311'] = func_8311
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_8360 = relay.TupleGetItem(func_4208_call(), 0)
call_8361 = relay.TupleGetItem(func_4210_call(), 0)
func_4830_call = mod.get_global_var('func_4830')
func_4834_call = mutated_mod.get_global_var('func_4834')
const_8365 = relay.const(-2, dtype = "int32")#candidate|8365|()|const|int32
const_8366 = relay.const([[7,-4,-9,10],[5,-4,1,-3],[6,9,-8,4],[-6,6,2,-6],[-1,-5,9,2],[7,3,5,-8],[-1,-9,-8,4],[5,-2,9,6],[-8,10,8,1],[7,3,9,5],[8,10,6,-2],[5,7,-9,6]], dtype = "int32")#candidate|8366|(12, 4)|const|int32
call_8364 = relay.TupleGetItem(func_4830_call(relay.reshape(const_8365.astype('int32'), []), relay.reshape(const_8366.astype('int32'), [48,]), ), 2)
call_8367 = relay.TupleGetItem(func_4834_call(relay.reshape(const_8365.astype('int32'), []), relay.reshape(const_8366.astype('int32'), [48,]), ), 2)
func_182_call = mod.get_global_var('func_182')
func_186_call = mutated_mod.get_global_var('func_186')
call_8371 = relay.TupleGetItem(func_182_call(relay.reshape(const_8365.astype('int32'), []), relay.reshape(const_8366.astype('int32'), [1, 6, 8]), ), 0)
call_8372 = relay.TupleGetItem(func_186_call(relay.reshape(const_8365.astype('int32'), []), relay.reshape(const_8366.astype('int32'), [1, 6, 8]), ), 0)
var_8375 = relay.var("var_8375", dtype = "int32", shape = (2, 6, 8))#candidate|8375|(2, 6, 8)|var|int32
bop_8376 = relay.logical_or(call_8371.astype('bool'), var_8375.astype('bool')) # shape=(2, 6, 8)
bop_8379 = relay.logical_or(call_8372.astype('bool'), var_8375.astype('bool')) # shape=(2, 6, 8)
bop_8385 = relay.floor_divide(const_8365.astype('float64'), var_8375.astype('float64')) # shape=(2, 6, 8)
func_8180_call = mod.get_global_var('func_8180')
func_8182_call = mutated_mod.get_global_var('func_8182')
call_8388 = func_8180_call()
call_8389 = func_8180_call()
bop_8402 = relay.bitwise_or(call_8371.astype('uint8'), bop_8385.astype('uint8')) # shape=(2, 6, 8)
bop_8405 = relay.bitwise_or(call_8372.astype('uint8'), bop_8385.astype('uint8')) # shape=(2, 6, 8)
func_7142_call = mod.get_global_var('func_7142')
func_7144_call = mutated_mod.get_global_var('func_7144')
const_8426 = relay.const([-8.389590,9.666139,-9.970703,-6.510657,-8.704953,-4.206936,7.010594,9.391890,8.294941,-6.708213,3.872479,-7.261659,-1.100051,-6.256148,-3.013931,-7.416906,-6.083815,-2.741069,4.659522,-3.743144,-0.018606,-7.174495,5.767537,7.152172,7.007709,-3.482197,-2.697923,3.923225,6.738793,-8.624272,-5.257762,-6.658925,-2.190296,1.190763,-6.975647,2.210807,-7.485444,-6.821360,9.452484,1.250423,6.849492,-5.057010,-2.471350,5.962560,0.460365,2.749519,-7.473977,-1.595831,8.995044,6.837357,8.525760,-6.459254,-7.385668,-2.702969,-3.775223,-4.955537,3.383500,8.390413,9.735607,-5.911432,0.984229,-1.945905,9.225000,-4.753764,9.876527,-4.599306,2.200808,-6.579486,4.563895,3.849053,-7.890446,-3.256768,-1.375844,2.087234,-9.872099,-7.150187,-2.024491,4.007997,2.886522,-9.214575,3.095466,-8.092207,3.059258,9.978724,1.922571,-0.290621,-8.015706,7.417274,7.796847,-3.446337,-6.730417,0.094631,-9.197757,7.543328,-4.644239,-2.518794,-1.398790,-3.206664], dtype = "float32")#candidate|8426|(98,)|const|float32
call_8425 = relay.TupleGetItem(func_7142_call(relay.reshape(const_8426.astype('float32'), [98,])), 0)
call_8427 = relay.TupleGetItem(func_7144_call(relay.reshape(const_8426.astype('float32'), [98,])), 0)
output = relay.Tuple([call_8360,call_8364,const_8366,bop_8376,call_8388,bop_8402,call_8425,const_8426,])
output2 = relay.Tuple([call_8361,call_8367,const_8366,bop_8379,call_8389,bop_8405,call_8427,const_8426,])
func_8439 = relay.Function([var_8375,], output)
mod['func_8439'] = func_8439
mod = relay.transform.InferType()(mod)
mutated_mod['func_8439'] = func_8439
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8440 = relay.var("var_8440", dtype = "int32", shape = (2, 6, 8))#candidate|8440|(2, 6, 8)|var|int32
func_8439_call = mutated_mod.get_global_var('func_8439')
call_8441 = func_8439_call(var_8440)
output = call_8441
func_8442 = relay.Function([var_8440], output)
mutated_mod['func_8442'] = func_8442
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_8462 = func_361_call()
call_8463 = func_361_call()
output = call_8462
output2 = call_8463
func_8472 = relay.Function([], output)
mod['func_8472'] = func_8472
mod = relay.transform.InferType()(mod)
mutated_mod['func_8472'] = func_8472
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8472_call = mutated_mod.get_global_var('func_8472')
call_8473 = func_8472_call()
output = call_8473
func_8474 = relay.Function([], output)
mutated_mod['func_8474'] = func_8474
mutated_mod = relay.transform.InferType()(mutated_mod)
func_361_call = mod.get_global_var('func_361')
func_362_call = mutated_mod.get_global_var('func_362')
call_8481 = func_361_call()
call_8482 = func_361_call()
output = relay.Tuple([call_8481,])
output2 = relay.Tuple([call_8482,])
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
func_5442_call = mod.get_global_var('func_5442')
func_5444_call = mutated_mod.get_global_var('func_5444')
call_8492 = func_5442_call()
call_8493 = func_5442_call()
output = call_8492
output2 = call_8493
func_8496 = relay.Function([], output)
mod['func_8496'] = func_8496
mod = relay.transform.InferType()(mod)
mutated_mod['func_8496'] = func_8496
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8496_call = mutated_mod.get_global_var('func_8496')
call_8497 = func_8496_call()
output = call_8497
func_8498 = relay.Function([], output)
mutated_mod['func_8498'] = func_8498
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3653_call = mod.get_global_var('func_3653')
func_3655_call = mutated_mod.get_global_var('func_3655')
call_8512 = func_3653_call()
call_8513 = func_3653_call()
func_2936_call = mod.get_global_var('func_2936')
func_2937_call = mutated_mod.get_global_var('func_2937')
call_8519 = relay.TupleGetItem(func_2936_call(), 0)
call_8520 = relay.TupleGetItem(func_2937_call(), 0)
output = relay.Tuple([call_8512,call_8519,])
output2 = relay.Tuple([call_8513,call_8520,])
func_8533 = relay.Function([], output)
mod['func_8533'] = func_8533
mod = relay.transform.InferType()(mod)
mutated_mod['func_8533'] = func_8533
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8533_call = mutated_mod.get_global_var('func_8533')
call_8534 = func_8533_call()
output = call_8534
func_8535 = relay.Function([], output)
mutated_mod['func_8535'] = func_8535
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_8568 = relay.TupleGetItem(func_4208_call(), 0)
call_8569 = relay.TupleGetItem(func_4210_call(), 0)
func_1368_call = mod.get_global_var('func_1368')
func_1369_call = mutated_mod.get_global_var('func_1369')
call_8572 = relay.TupleGetItem(func_1368_call(), 0)
call_8573 = relay.TupleGetItem(func_1369_call(), 0)
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_8578 = func_526_call()
call_8579 = func_526_call()
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_8580 = func_526_call()
call_8581 = func_526_call()
func_8489_call = mod.get_global_var('func_8489')
func_8491_call = mutated_mod.get_global_var('func_8491')
call_8584 = relay.TupleGetItem(func_8489_call(), 0)
call_8585 = relay.TupleGetItem(func_8491_call(), 0)
func_3698_call = mod.get_global_var('func_3698')
func_3700_call = mutated_mod.get_global_var('func_3700')
call_8593 = relay.TupleGetItem(func_3698_call(), 1)
call_8594 = relay.TupleGetItem(func_3700_call(), 1)
output = relay.Tuple([call_8568,call_8572,call_8578,call_8580,call_8584,call_8593,])
output2 = relay.Tuple([call_8569,call_8573,call_8579,call_8581,call_8585,call_8594,])
func_8608 = relay.Function([], output)
mod['func_8608'] = func_8608
mod = relay.transform.InferType()(mod)
mutated_mod['func_8608'] = func_8608
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8608_call = mutated_mod.get_global_var('func_8608')
call_8609 = func_8608_call()
output = call_8609
func_8610 = relay.Function([], output)
mutated_mod['func_8610'] = func_8610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5953_call = mod.get_global_var('func_5953')
func_5954_call = mutated_mod.get_global_var('func_5954')
call_8627 = relay.TupleGetItem(func_5953_call(), 0)
call_8628 = relay.TupleGetItem(func_5954_call(), 0)
func_7098_call = mod.get_global_var('func_7098')
func_7100_call = mutated_mod.get_global_var('func_7100')
call_8639 = func_7098_call()
call_8640 = func_7098_call()
func_3008_call = mod.get_global_var('func_3008')
func_3009_call = mutated_mod.get_global_var('func_3009')
call_8652 = relay.TupleGetItem(func_3008_call(), 0)
call_8653 = relay.TupleGetItem(func_3009_call(), 0)
output = relay.Tuple([call_8627,call_8639,call_8652,])
output2 = relay.Tuple([call_8628,call_8640,call_8653,])
func_8659 = relay.Function([], output)
mod['func_8659'] = func_8659
mod = relay.transform.InferType()(mod)
mutated_mod['func_8659'] = func_8659
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8659_call = mutated_mod.get_global_var('func_8659')
call_8660 = func_8659_call()
output = call_8660
func_8661 = relay.Function([], output)
mutated_mod['func_8661'] = func_8661
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3897_call = mod.get_global_var('func_3897')
func_3898_call = mutated_mod.get_global_var('func_3898')
call_8715 = relay.TupleGetItem(func_3897_call(), 0)
call_8716 = relay.TupleGetItem(func_3898_call(), 0)
output = call_8715
output2 = call_8716
func_8737 = relay.Function([], output)
mod['func_8737'] = func_8737
mod = relay.transform.InferType()(mod)
output = func_8737()
func_8738 = relay.Function([], output)
mutated_mod['func_8738'] = func_8738
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8030_call = mod.get_global_var('func_8030')
func_8031_call = mutated_mod.get_global_var('func_8031')
call_8745 = relay.TupleGetItem(func_8030_call(), 0)
call_8746 = relay.TupleGetItem(func_8031_call(), 0)
output = call_8745
output2 = call_8746
func_8755 = relay.Function([], output)
mod['func_8755'] = func_8755
mod = relay.transform.InferType()(mod)
mutated_mod['func_8755'] = func_8755
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8755_call = mutated_mod.get_global_var('func_8755')
call_8756 = func_8755_call()
output = call_8756
func_8757 = relay.Function([], output)
mutated_mod['func_8757'] = func_8757
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6061_call = mod.get_global_var('func_6061')
func_6063_call = mutated_mod.get_global_var('func_6063')
call_8769 = relay.TupleGetItem(func_6061_call(), 0)
call_8770 = relay.TupleGetItem(func_6063_call(), 0)
func_5239_call = mod.get_global_var('func_5239')
func_5243_call = mutated_mod.get_global_var('func_5243')
const_8773 = relay.const([[-9,-10,8,-2,-3,-9,7,10,4,10,5,-1,-10,-1,-4,-8,9,-7,7,8,-8,2,2,9,-7,-4,-8,-1,7,-7,-2,-4,-2,-7,-10,-8,-1,-4,-2,1,-1,-2,-1,1,-4,8,3,6,-3,-4,-10,-1,-3,-6,-7,4,9,1,8,9,-8,5,-1,7,-6,8,3,6,6,1,-6,-3,9,-6,-4,9,2,-5,7,-8,3,8,5,2,-8,5,7,3,-10,5,4,9,-9,10,8,-8],[3,-9,-4,10,-5,7,2,10,-9,-9,-8,-2,3,-3,-1,4,-9,-4,5,6,-8,-1,-3,4,5,-6,10,-2,-1,5,-5,7,1,10,5,5,-7,6,7,-1,-3,-7,-4,-7,-3,-8,-1,-6,-6,8,2,-5,-8,-8,-10,9,-5,-6,7,-7,-6,-3,-10,9,5,7,9,-6,-2,-5,-5,-6,3,3,-7,-4,-5,-2,-6,-9,8,-10,-10,7,-3,6,7,10,6,-1,4,-8,2,2,-10,-3]], dtype = "int16")#candidate|8773|(2, 96)|const|int16
var_8774 = relay.var("var_8774", dtype = "int16", shape = (768, 2))#candidate|8774|(768, 2)|var|int16
const_8775 = relay.const([-6,7,-7,-5,5,5,-7,2,-7,7,3,-7,-9,5,-6,7,-7,3,9,4,-5,-6,8,-6,-10,-1,1,9,-6,3,-1,8,-3,9,9,7,-2,6,-3,-7,7,6,-7,-8,-3,6,3,9,-5,9,-2,7,1,8,-8,-7,-2,-5,-1,-3,-5,-6,5,4,6,5,4,-3,-7,-1,5,-2,-2,-5,1,5,9,4,-9,-3,4,2,-9,-2,-8,-3,-10,10,-5,5,5,2,3,5,6,6,5,7,5,-4,4,-5,-6,6,-10,-7,-1,8,-7,-6,10,-3,2,-10,-3,9,4,2,9,-9,-9,5,-5,3,-5,-5,3,-9,-1,-3,5,-2,5,9,9,4,-4,7,-1,3,3,10,-7,-2,-10,-3,-4,6,-6,-5,2,-5,10,8,-6,9,9,5,8,6,-2,-7,-1,-8,-5,-4,-6,-3,-2,-10,-2,-10,-8,-8,-2,-6,-1,-3,-5,1,-7,7,5,10,1,-8,10,-3,-2,-7,-5,-3,8,-1,8,-3,9,8,9,3,-1,4,-10,-2,-10,-9,1,-3,7,-2,-10,-9,6,-2,9,-7,-8,-2,8,3,10,-4,3,4,3,-6,-2,1,4,2,-1,-4,8,9,9,-5,-3,3,-8,7,-2,6,10,1,3,9,-2,2,10,-7,3,-7,-3,-4,7,4,-6,5,-8,-2,-10,2,6,4,-7,-3,5,9,-2,10,-6,-3,3,-10,4,1,-5,-10,8,4,-4,-10,-1,-10,-3,4,-5,4,5,-8,-8,-5,-1,-1,-8,6,4,-5,-6,7,5,1,-6,-7,-8,10,-3,6,-1,-5,-4,2,-9,-10,-10,-4,-8,-5,9,5,-7,5,3,6,-2,4,-3,1,-3,-9,-10,10,-10,-2,6,-10,6,5,-9,-5,1,7,6,-6,-1,-2,9,-8,-6,8,10,7,3,7,-10,-5,2,4,9,8,6,10,-3,-2,1,-3,10,-8,1,-7,8,1,-3,1,-7,-4,9,6,-4,-3,10,7,7,5,1,-8,-5,2,-5,1,-9,3,-1,-2,-9,10,-4,-1,4,-8,7,5,-6,-1,-7,-1,9,6,2,3,-4,1,1,8,8,-10,3,-7,2,10,-2,6,6,9,2,1,8,4,4,7,-10,-8,-4,-2,3,-6,4,6,3,-9,-9,1,-2,7,8,9,10,-1,-10,-9,-6,10,8,-1,1,-8,-8,-8,-5,-6,6,1,1,-10,-6,8,5,-3,5,-6,1,9,-2,-10,9,-9,1,4,-1,-5,-5,-8,-2,-5,-2,5,4,7,-10,-2,4,5,1,-9,6,-9,8,3,-6,-9,1,6,-8,3,9,-7,9,8,3,-2,3,10,-9,-1,5,-5,-4,4,-5,9,4,-7,-10,-5,-4,4,8,-9,10,2,-10,2,10,-5,2,-9,10,1,4,-6,3,-6,-7,8,6,1,-8,1,8,5,10,8,1,-3,-3,3,-1,7,-5,3,6,9,-6,4,-6,6,2,-7,1,-7,-9,4,-1,-7,-7,-10], dtype = "int16")#candidate|8775|(576,)|const|int16
call_8772 = relay.TupleGetItem(func_5239_call(relay.reshape(const_8773.astype('int16'), [16, 12, 1]), relay.reshape(var_8774.astype('int16'), [16, 12, 8]), relay.reshape(const_8775.astype('int16'), [16, 12, 3]), ), 2)
call_8776 = relay.TupleGetItem(func_5243_call(relay.reshape(const_8773.astype('int16'), [16, 12, 1]), relay.reshape(var_8774.astype('int16'), [16, 12, 8]), relay.reshape(const_8775.astype('int16'), [16, 12, 3]), ), 2)
var_8787 = relay.var("var_8787", dtype = "int16", shape = (768, 2))#candidate|8787|(768, 2)|var|int16
bop_8788 = relay.less_equal(var_8774.astype('bool'), relay.reshape(var_8787.astype('bool'), relay.shape_of(var_8774))) # shape=(768, 2)
uop_8799 = relay.sigmoid(call_8769.astype('float64')) # shape=(5, 11, 4)
uop_8801 = relay.sigmoid(call_8770.astype('float64')) # shape=(5, 11, 4)
func_5623_call = mod.get_global_var('func_5623')
func_5624_call = mutated_mod.get_global_var('func_5624')
call_8802 = relay.TupleGetItem(func_5623_call(), 1)
call_8803 = relay.TupleGetItem(func_5624_call(), 1)
func_5718_call = mod.get_global_var('func_5718')
func_5719_call = mutated_mod.get_global_var('func_5719')
call_8814 = func_5718_call()
call_8815 = func_5718_call()
output = relay.Tuple([call_8772,const_8773,const_8775,bop_8788,uop_8799,call_8802,call_8814,])
output2 = relay.Tuple([call_8776,const_8773,const_8775,bop_8788,uop_8801,call_8803,call_8815,])
func_8816 = relay.Function([var_8774,var_8787,], output)
mod['func_8816'] = func_8816
mod = relay.transform.InferType()(mod)
var_8817 = relay.var("var_8817", dtype = "int16", shape = (768, 2))#candidate|8817|(768, 2)|var|int16
var_8818 = relay.var("var_8818", dtype = "int16", shape = (768, 2))#candidate|8818|(768, 2)|var|int16
output = func_8816(var_8817,var_8818,)
func_8819 = relay.Function([var_8817,var_8818,], output)
mutated_mod['func_8819'] = func_8819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4208_call = mod.get_global_var('func_4208')
func_4210_call = mutated_mod.get_global_var('func_4210')
call_8832 = relay.TupleGetItem(func_4208_call(), 0)
call_8833 = relay.TupleGetItem(func_4210_call(), 0)
output = call_8832
output2 = call_8833
func_8844 = relay.Function([], output)
mod['func_8844'] = func_8844
mod = relay.transform.InferType()(mod)
output = func_8844()
func_8845 = relay.Function([], output)
mutated_mod['func_8845'] = func_8845
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8846 = relay.var("var_8846", dtype = "uint8", shape = (10, 8, 14))#candidate|8846|(10, 8, 14)|var|uint8
var_8847 = relay.var("var_8847", dtype = "uint8", shape = (10, 8, 14))#candidate|8847|(10, 8, 14)|var|uint8
bop_8848 = relay.less(var_8846.astype('bool'), relay.reshape(var_8847.astype('bool'), relay.shape_of(var_8846))) # shape=(10, 8, 14)
func_7191_call = mod.get_global_var('func_7191')
func_7192_call = mutated_mod.get_global_var('func_7192')
call_8856 = relay.TupleGetItem(func_7191_call(), 1)
call_8857 = relay.TupleGetItem(func_7192_call(), 1)
bop_8862 = relay.greater(var_8846.astype('bool'), relay.reshape(var_8847.astype('bool'), relay.shape_of(var_8846))) # shape=(10, 8, 14)
output = relay.Tuple([bop_8848,call_8856,bop_8862,])
output2 = relay.Tuple([bop_8848,call_8857,bop_8862,])
func_8886 = relay.Function([var_8846,var_8847,], output)
mod['func_8886'] = func_8886
mod = relay.transform.InferType()(mod)
mutated_mod['func_8886'] = func_8886
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8886_call = mutated_mod.get_global_var('func_8886')
var_8888 = relay.var("var_8888", dtype = "uint8", shape = (10, 8, 14))#candidate|8888|(10, 8, 14)|var|uint8
var_8889 = relay.var("var_8889", dtype = "uint8", shape = (10, 8, 14))#candidate|8889|(10, 8, 14)|var|uint8
call_8887 = func_8886_call(var_8888,var_8889,)
output = call_8887
func_8890 = relay.Function([var_8888,var_8889,], output)
mutated_mod['func_8890'] = func_8890
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8755_call = mod.get_global_var('func_8755')
func_8757_call = mutated_mod.get_global_var('func_8757')
call_8896 = func_8755_call()
call_8897 = func_8755_call()
output = call_8896
output2 = call_8897
func_8904 = relay.Function([], output)
mod['func_8904'] = func_8904
mod = relay.transform.InferType()(mod)
mutated_mod['func_8904'] = func_8904
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8904_call = mutated_mod.get_global_var('func_8904')
call_8905 = func_8904_call()
output = call_8905
func_8906 = relay.Function([], output)
mutated_mod['func_8906'] = func_8906
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5623_call = mod.get_global_var('func_5623')
func_5624_call = mutated_mod.get_global_var('func_5624')
call_8937 = relay.TupleGetItem(func_5623_call(), 0)
call_8938 = relay.TupleGetItem(func_5624_call(), 0)
func_1955_call = mod.get_global_var('func_1955')
func_1956_call = mutated_mod.get_global_var('func_1956')
call_8963 = func_1955_call()
call_8964 = func_1955_call()
func_7510_call = mod.get_global_var('func_7510')
func_7511_call = mutated_mod.get_global_var('func_7511')
call_8966 = relay.TupleGetItem(func_7510_call(), 0)
call_8967 = relay.TupleGetItem(func_7511_call(), 0)
output = relay.Tuple([call_8937,call_8963,call_8966,])
output2 = relay.Tuple([call_8938,call_8964,call_8967,])
func_8975 = relay.Function([], output)
mod['func_8975'] = func_8975
mod = relay.transform.InferType()(mod)
mutated_mod['func_8975'] = func_8975
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8975_call = mutated_mod.get_global_var('func_8975')
call_8976 = func_8975_call()
output = call_8976
func_8977 = relay.Function([], output)
mutated_mod['func_8977'] = func_8977
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9036 = relay.const([[[-3,7,-6,1,-10,3,1,-9,1,-10,9,10,-2],[5,5,5,-5,-7,-5,-6,-7,7,10,-1,-3,1]],[[-4,8,-8,-6,-2,-1,7,-7,-6,7,3,-1,10],[-5,3,-7,-9,-3,-9,-7,1,-8,-8,1,2,-9]],[[-2,10,-4,-4,-3,4,-5,6,-5,5,-3,-4,-9],[-4,3,-8,4,4,2,-3,-9,6,3,6,-5,5]],[[3,6,6,-5,-3,-1,-10,3,5,7,-4,-5,-5],[6,-1,5,-4,-10,-2,9,-9,-2,-7,10,-2,3]],[[-2,-2,1,-4,-3,-10,3,-7,-6,-10,-7,3,7],[6,-2,5,9,-8,9,5,-2,-9,7,-8,4,-8]],[[-2,5,-4,-1,9,-8,-5,-9,8,-8,-8,-3,-5],[-8,1,-10,-4,-4,-7,3,-1,2,-7,2,-4,-6]],[[-7,7,-2,-3,-8,-5,9,1,4,-9,6,1,-4],[-1,-1,-3,5,-2,-5,-9,-9,7,6,3,-3,3]],[[6,5,6,10,-2,-8,1,2,-7,8,7,-4,-5],[-1,9,-8,-9,-5,-10,4,8,-8,4,-4,3,6]],[[9,-3,7,3,-9,1,7,-4,-2,8,2,8,8],[-6,-6,-2,-2,-1,8,-3,8,-6,-1,-1,-9,-1]],[[-7,-7,-1,-7,-5,5,-2,8,-2,-7,-6,-3,-3],[8,-3,5,5,4,-4,4,8,9,-6,9,10,8]],[[9,1,-6,-6,-5,9,-4,10,2,9,5,-9,7],[-9,-4,-10,-8,4,9,3,2,6,4,6,-1,-7]],[[5,5,4,8,3,-2,9,5,8,2,9,-8,5],[9,10,-2,2,8,3,7,-4,-7,4,2,1,4]],[[5,2,-7,-6,9,-2,7,-8,-6,6,-3,-6,6],[-1,-6,-6,-6,-1,-9,9,-6,10,3,-4,4,-10]],[[7,-4,-5,-2,9,-10,-6,9,9,-5,1,10,3],[2,8,-4,7,7,-2,-3,-7,-7,5,10,4,-10]]], dtype = "int16")#candidate|9036|(14, 2, 13)|const|int16
var_9037 = relay.var("var_9037", dtype = "int16", shape = (14, 2, 13))#candidate|9037|(14, 2, 13)|var|int16
bop_9038 = relay.equal(const_9036.astype('bool'), relay.reshape(var_9037.astype('bool'), relay.shape_of(const_9036))) # shape=(14, 2, 13)
uop_9054 = relay.cosh(const_9036.astype('float32')) # shape=(14, 2, 13)
output = relay.Tuple([bop_9038,uop_9054,])
output2 = relay.Tuple([bop_9038,uop_9054,])
func_9066 = relay.Function([var_9037,], output)
mod['func_9066'] = func_9066
mod = relay.transform.InferType()(mod)
var_9067 = relay.var("var_9067", dtype = "int16", shape = (14, 2, 13))#candidate|9067|(14, 2, 13)|var|int16
output = func_9066(var_9067)
func_9068 = relay.Function([var_9067], output)
mutated_mod['func_9068'] = func_9068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_859_call = mod.get_global_var('func_859')
func_860_call = mutated_mod.get_global_var('func_860')
call_9089 = relay.TupleGetItem(func_859_call(), 0)
call_9090 = relay.TupleGetItem(func_860_call(), 0)
output = relay.Tuple([call_9089,])
output2 = relay.Tuple([call_9090,])
func_9112 = relay.Function([], output)
mod['func_9112'] = func_9112
mod = relay.transform.InferType()(mod)
mutated_mod['func_9112'] = func_9112
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9112_call = mutated_mod.get_global_var('func_9112')
call_9113 = func_9112_call()
output = call_9113
func_9114 = relay.Function([], output)
mutated_mod['func_9114'] = func_9114
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8496_call = mod.get_global_var('func_8496')
func_8498_call = mutated_mod.get_global_var('func_8498')
call_9117 = func_8496_call()
call_9118 = func_8496_call()
func_526_call = mod.get_global_var('func_526')
func_528_call = mutated_mod.get_global_var('func_528')
call_9122 = func_526_call()
call_9123 = func_526_call()
output = relay.Tuple([call_9117,call_9122,])
output2 = relay.Tuple([call_9118,call_9123,])
func_9131 = relay.Function([], output)
mod['func_9131'] = func_9131
mod = relay.transform.InferType()(mod)
mutated_mod['func_9131'] = func_9131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9131_call = mutated_mod.get_global_var('func_9131')
call_9132 = func_9131_call()
output = call_9132
func_9133 = relay.Function([], output)
mutated_mod['func_9133'] = func_9133
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6429_call = mod.get_global_var('func_6429')
func_6431_call = mutated_mod.get_global_var('func_6431')
call_9137 = relay.TupleGetItem(func_6429_call(), 0)
call_9138 = relay.TupleGetItem(func_6431_call(), 0)
func_7837_call = mod.get_global_var('func_7837')
func_7839_call = mutated_mod.get_global_var('func_7839')
call_9165 = relay.TupleGetItem(func_7837_call(), 0)
call_9166 = relay.TupleGetItem(func_7839_call(), 0)
func_3073_call = mod.get_global_var('func_3073')
func_3075_call = mutated_mod.get_global_var('func_3075')
call_9179 = relay.TupleGetItem(func_3073_call(), 0)
call_9180 = relay.TupleGetItem(func_3075_call(), 0)
output = relay.Tuple([call_9137,call_9165,call_9179,])
output2 = relay.Tuple([call_9138,call_9166,call_9180,])
func_9185 = relay.Function([], output)
mod['func_9185'] = func_9185
mod = relay.transform.InferType()(mod)
output = func_9185()
func_9186 = relay.Function([], output)
mutated_mod['func_9186'] = func_9186
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7297_call = mod.get_global_var('func_7297')
func_7298_call = mutated_mod.get_global_var('func_7298')
call_9187 = relay.TupleGetItem(func_7297_call(), 1)
call_9188 = relay.TupleGetItem(func_7298_call(), 1)
output = relay.Tuple([call_9187,])
output2 = relay.Tuple([call_9188,])
func_9189 = relay.Function([], output)
mod['func_9189'] = func_9189
mod = relay.transform.InferType()(mod)
output = func_9189()
func_9190 = relay.Function([], output)
mutated_mod['func_9190'] = func_9190
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2412_call = mod.get_global_var('func_2412')
func_2414_call = mutated_mod.get_global_var('func_2414')
call_9244 = relay.TupleGetItem(func_2412_call(), 0)
call_9245 = relay.TupleGetItem(func_2414_call(), 0)
output = call_9244
output2 = call_9245
func_9254 = relay.Function([], output)
mod['func_9254'] = func_9254
mod = relay.transform.InferType()(mod)
output = func_9254()
func_9255 = relay.Function([], output)
mutated_mod['func_9255'] = func_9255
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3698_call = mod.get_global_var('func_3698')
func_3700_call = mutated_mod.get_global_var('func_3700')
call_9292 = relay.TupleGetItem(func_3698_call(), 0)
call_9293 = relay.TupleGetItem(func_3700_call(), 0)
func_7773_call = mod.get_global_var('func_7773')
func_7775_call = mutated_mod.get_global_var('func_7775')
call_9308 = func_7773_call()
call_9309 = func_7773_call()
func_5693_call = mod.get_global_var('func_5693')
func_5694_call = mutated_mod.get_global_var('func_5694')
call_9337 = relay.TupleGetItem(func_5693_call(), 0)
call_9338 = relay.TupleGetItem(func_5694_call(), 0)
output = relay.Tuple([call_9292,call_9308,call_9337,])
output2 = relay.Tuple([call_9293,call_9309,call_9338,])
func_9342 = relay.Function([], output)
mod['func_9342'] = func_9342
mod = relay.transform.InferType()(mod)
mutated_mod['func_9342'] = func_9342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9342_call = mutated_mod.get_global_var('func_9342')
call_9343 = func_9342_call()
output = call_9343
func_9344 = relay.Function([], output)
mutated_mod['func_9344'] = func_9344
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8472_call = mod.get_global_var('func_8472')
func_8474_call = mutated_mod.get_global_var('func_8474')
call_9345 = func_8472_call()
call_9346 = func_8472_call()
output = call_9345
output2 = call_9346
func_9348 = relay.Function([], output)
mod['func_9348'] = func_9348
mod = relay.transform.InferType()(mod)
mutated_mod['func_9348'] = func_9348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9348_call = mutated_mod.get_global_var('func_9348')
call_9349 = func_9348_call()
output = call_9349
func_9350 = relay.Function([], output)
mutated_mod['func_9350'] = func_9350
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1883_call = mod.get_global_var('func_1883')
func_1885_call = mutated_mod.get_global_var('func_1885')
call_9400 = relay.TupleGetItem(func_1883_call(), 0)
call_9401 = relay.TupleGetItem(func_1885_call(), 0)
output = call_9400
output2 = call_9401
func_9412 = relay.Function([], output)
mod['func_9412'] = func_9412
mod = relay.transform.InferType()(mod)
output = func_9412()
func_9413 = relay.Function([], output)
mutated_mod['func_9413'] = func_9413
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3537_call = mod.get_global_var('func_3537')
func_3539_call = mutated_mod.get_global_var('func_3539')
call_9438 = relay.TupleGetItem(func_3537_call(), 0)
call_9439 = relay.TupleGetItem(func_3539_call(), 0)
output = relay.Tuple([call_9438,])
output2 = relay.Tuple([call_9439,])
func_9466 = relay.Function([], output)
mod['func_9466'] = func_9466
mod = relay.transform.InferType()(mod)
output = func_9466()
func_9467 = relay.Function([], output)
mutated_mod['func_9467'] = func_9467
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2197_call = mod.get_global_var('func_2197')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_9471 = relay.TupleGetItem(func_2197_call(), 3)
call_9472 = relay.TupleGetItem(func_2199_call(), 3)
output = call_9471
output2 = call_9472
func_9477 = relay.Function([], output)
mod['func_9477'] = func_9477
mod = relay.transform.InferType()(mod)
output = func_9477()
func_9478 = relay.Function([], output)
mutated_mod['func_9478'] = func_9478
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4146_call = mod.get_global_var('func_4146')
func_4147_call = mutated_mod.get_global_var('func_4147')
call_9490 = func_4146_call()
call_9491 = func_4146_call()
func_2197_call = mod.get_global_var('func_2197')
func_2199_call = mutated_mod.get_global_var('func_2199')
call_9492 = relay.TupleGetItem(func_2197_call(), 0)
call_9493 = relay.TupleGetItem(func_2199_call(), 0)
output = relay.Tuple([call_9490,call_9492,])
output2 = relay.Tuple([call_9491,call_9493,])
func_9512 = relay.Function([], output)
mod['func_9512'] = func_9512
mod = relay.transform.InferType()(mod)
mutated_mod['func_9512'] = func_9512
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9512_call = mutated_mod.get_global_var('func_9512')
call_9513 = func_9512_call()
output = call_9513
func_9514 = relay.Function([], output)
mutated_mod['func_9514'] = func_9514
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8659_call = mod.get_global_var('func_8659')
func_8661_call = mutated_mod.get_global_var('func_8661')
call_9517 = relay.TupleGetItem(func_8659_call(), 0)
call_9518 = relay.TupleGetItem(func_8661_call(), 0)
output = relay.Tuple([call_9517,])
output2 = relay.Tuple([call_9518,])
func_9523 = relay.Function([], output)
mod['func_9523'] = func_9523
mod = relay.transform.InferType()(mod)
output = func_9523()
func_9524 = relay.Function([], output)
mutated_mod['func_9524'] = func_9524
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3993_call = mod.get_global_var('func_3993')
func_3995_call = mutated_mod.get_global_var('func_3995')
call_9525 = func_3993_call()
call_9526 = func_3993_call()
output = relay.Tuple([call_9525,])
output2 = relay.Tuple([call_9526,])
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
func_1846_call = mod.get_global_var('func_1846')
func_1848_call = mutated_mod.get_global_var('func_1848')
call_9556 = relay.TupleGetItem(func_1846_call(), 0)
call_9557 = relay.TupleGetItem(func_1848_call(), 0)
func_573_call = mod.get_global_var('func_573')
func_577_call = mutated_mod.get_global_var('func_577')
call_9562 = relay.TupleGetItem(func_573_call(relay.reshape(call_9556.astype('float32'), [5, 11, 4]), relay.reshape(call_9556.astype('bool'), [5, 11, 4]), ), 0)
call_9563 = relay.TupleGetItem(func_577_call(relay.reshape(call_9556.astype('float32'), [5, 11, 4]), relay.reshape(call_9556.astype('bool'), [5, 11, 4]), ), 0)
func_9477_call = mod.get_global_var('func_9477')
func_9478_call = mutated_mod.get_global_var('func_9478')
call_9583 = func_9477_call()
call_9584 = func_9477_call()
output = relay.Tuple([call_9556,call_9562,call_9583,])
output2 = relay.Tuple([call_9557,call_9563,call_9584,])
func_9618 = relay.Function([], output)
mod['func_9618'] = func_9618
mod = relay.transform.InferType()(mod)
output = func_9618()
func_9619 = relay.Function([], output)
mutated_mod['func_9619'] = func_9619
mutated_mod = relay.transform.InferType()(mutated_mod)
const_9658 = relay.const([[[-9,8,-10,1,-9],[7,2,10,6,-3],[1,-6,-5,5,-2],[-3,-3,-9,7,8],[-7,-5,-4,8,-6],[4,7,4,6,-7],[8,-1,5,5,-2],[-8,-9,-7,-2,10],[7,7,5,6,-1]],[[-2,-5,3,3,-3],[-10,-5,6,9,-6],[-5,-4,-7,-6,-4],[5,9,9,1,-7],[-6,-5,-3,2,8],[10,10,-8,6,-9],[-2,-4,-6,10,-4],[4,-3,2,2,7],[-3,7,-4,10,8]],[[10,-6,10,7,1],[-6,-3,4,4,-1],[-7,-1,-8,9,5],[-9,-9,9,-5,9],[10,-1,-6,-2,2],[-3,-6,5,-9,1],[-6,-7,5,4,2],[8,-9,-9,-5,-5],[-2,7,-5,3,-9]],[[-8,-7,9,10,-2],[7,8,-8,-2,8],[9,8,-10,-8,-6],[9,3,-8,-6,6],[-3,-7,-8,8,7],[7,-5,-9,9,10],[-8,9,3,-4,6],[-8,-10,9,-9,9],[-2,1,3,-4,9]],[[6,-1,9,-2,4],[2,6,8,-1,4],[-4,-6,8,4,10],[6,-3,2,-2,6],[2,-9,-1,8,5],[-1,2,1,-7,-2],[10,-6,8,8,2],[-7,1,7,-4,-3],[-8,-5,2,-2,4]],[[-7,-3,-9,10,-10],[-1,-9,4,6,2],[6,-2,2,-10,-2],[-8,9,1,-4,-7],[-3,3,5,-9,-5],[8,3,-4,-5,-9],[9,7,1,-7,-1],[1,-7,8,-2,-2],[-10,-8,-4,7,-9]],[[8,6,-5,5,3],[-10,-2,9,-8,-8],[7,3,-10,10,-6],[-4,6,-10,-8,-4],[-3,-5,9,4,2],[10,-8,7,-7,5],[-7,-8,10,3,-4],[-9,1,-9,-6,10],[5,-1,2,-10,6]],[[-4,6,-5,1,4],[-7,2,7,-8,6],[-2,7,-3,1,10],[9,-2,6,-1,7],[2,-8,-2,8,7],[8,-5,5,4,9],[5,5,-5,7,10],[1,10,6,2,3],[-8,-9,6,8,9]],[[-1,9,4,-1,-8],[-4,10,-8,-7,-2],[10,-1,-2,-4,-4],[-2,-9,-5,3,-3],[6,9,3,-4,-8],[3,6,-8,9,-1],[-4,2,-3,4,2],[6,5,5,3,-10],[-6,8,5,2,-5]],[[-10,5,-2,-8,2],[-6,-9,-6,-10,-4],[9,-3,3,2,-5],[8,7,7,2,8],[7,-4,4,3,-8],[-4,8,-3,-7,-4],[-5,-6,-8,4,8],[5,3,-4,-9,10],[-5,-4,2,-1,6]],[[1,-10,4,10,7],[9,5,-1,-10,7],[8,2,2,1,5],[1,-1,-3,-10,-4],[-2,10,6,10,2],[3,9,3,-1,7],[4,-2,-2,9,-9],[-10,5,-10,-9,-4],[-8,-2,4,2,-10]],[[1,-8,6,-7,3],[-7,7,-3,10,9],[-5,-10,-6,10,10],[-7,-3,-6,-7,5],[1,3,3,-6,7],[8,-2,7,-5,-6],[-9,5,-7,1,6],[-4,-8,-4,2,-4],[5,1,2,-7,-6]],[[-9,-3,-7,9,-6],[5,-9,-8,4,5],[9,9,9,-7,-8],[7,-10,-4,-5,-6],[-8,-1,-2,2,-9],[3,8,7,5,4],[-8,1,-3,6,9],[-9,1,-6,10,-8],[-6,8,-6,3,-10]],[[-7,10,-8,-4,-1],[4,-2,1,-7,-5],[-2,9,8,5,-9],[10,3,1,-1,6],[9,-5,5,6,-8],[9,5,10,-3,7],[-9,-5,5,4,2],[1,9,2,-1,-6],[-3,-9,-2,4,-5]]], dtype = "uint16")#candidate|9658|(14, 9, 5)|const|uint16
var_9659 = relay.var("var_9659", dtype = "uint16", shape = (14, 9, 5))#candidate|9659|(14, 9, 5)|var|uint16
bop_9660 = relay.add(const_9658.astype('uint16'), relay.reshape(var_9659.astype('uint16'), relay.shape_of(const_9658))) # shape=(14, 9, 5)
func_8439_call = mod.get_global_var('func_8439')
func_8442_call = mutated_mod.get_global_var('func_8442')
var_9676 = relay.var("var_9676", dtype = "int32", shape = (96,))#candidate|9676|(96,)|var|int32
call_9675 = relay.TupleGetItem(func_8439_call(relay.reshape(var_9676.astype('int32'), [2, 6, 8])), 7)
call_9677 = relay.TupleGetItem(func_8442_call(relay.reshape(var_9676.astype('int32'), [2, 6, 8])), 7)
uop_9683 = relay.asin(call_9675.astype('float32')) # shape=(98,)
uop_9685 = relay.asin(call_9677.astype('float32')) # shape=(98,)
func_4586_call = mod.get_global_var('func_4586')
func_4589_call = mutated_mod.get_global_var('func_4589')
const_9688 = relay.const([6,-2,-5,-6,1,-1,-1,10,3,-8,6,-2,-4,-3,-7,-9,-2,-1,-1,6,-2,-9,-7,10,10,10,-8,4], dtype = "int8")#candidate|9688|(28,)|const|int8
const_9689 = relay.const([5,2,10,-4,-2,7,-9,6,-1,-8,4,-10,5,7,8,-9,-7,-8,4,9,8,-8,4,-6,9,-5,-3,-9,1,-8,-5,3,-7,-2,-6,8,6,3,-2,-6,-3,5,-6,-6,2,7,10,-1,4,9,6,-3,5,-4,-5,7,-1,-5,1,-5,7,2,3,-6,9,-6,5,7,5,7,4,-7,-10,-2,-6,-4,9,2,-1,9,-6,-5,4,4,-7,-7,-7,-6,7,-8,4,-7,7,-5,8,8,-8,-8,9,2,-3,5,-3,8,8,6,5,-5,3,-1,-3,-6,4,-5,-5,8,-8,-9,3,-3,-1,-5,2,-1,9,5,-4,6,6,2,-8,9,-3,-7,6,-1,10,-5,5,7,-9,9,5,1,7,-3,4,-3,10,5,-3,-5,2,7,-6,-3,-7,10,10,-3,7,-5,8,7,-9,6,-9,-7,10,8,6,-5,-6,7,8,-4,-6,5,-7,3,-7,10,-9,4,-8,-9,4,9,1,-9,-6,4,-1,5,3,6,7,5,2,9,-4,4,4,-9,9,-4,10,-6,-6,1,-1,1,-4,5,-8,3,5,-9,1,4,5,-7,-5,-7,8,-2,6,6,-2,5,-7,9,6,-1,-5,8,-2,-6,-10,1,3,-6,9,-9,2,8,-2,9,4,-4,-4,8,9,-6,6,-8,3,6,-3,2,10,-7,6,8,-8,8,9,10,9,-9,-3,4,9,7,-6,1,8,8,-4,5,-1,5,-10,-9,3,4,5,4,-7,-7,-10,10,-6,6,-5,3,-6,7,3,5,-4,-2,6,-4,-6,7,-1,6,3,9,-2,3,1,2,-6,10,5,-10,7,-3,6,3,-4,7,2,5,-8,-2,8,3,-2,-5,-4,-7,2,-7,9,-8,-8,2,10,-4,6,7,1,-8,-2,9,2,8,9,2,5,2,-4,-3,-2,3,2,-1,-2,5,4,10,3,7,3,-9,9,2,-8,6,-2,9,10,7,1,-6,8,-2,-5,-3,10,9,-3,-1,-7,-2,-9,-3,1,3,-5,-8,8,-6,-10,-3,10,8,-4,6,-9,10,-9,8,-6,3,-1,-4,10,-2,-10,-1,-9,-6,9,4,-10,5], dtype = "int8")#candidate|9689|(420,)|const|int8
call_9687 = func_4586_call(relay.reshape(const_9688.astype('int8'), [1, 2, 14]), relay.reshape(const_9689.astype('int8'), [15, 2, 14]), )
call_9690 = func_4586_call(relay.reshape(const_9688.astype('int8'), [1, 2, 14]), relay.reshape(const_9689.astype('int8'), [15, 2, 14]), )
var_9701 = relay.var("var_9701", dtype = "int8", shape = (28,))#candidate|9701|(28,)|var|int8
bop_9702 = relay.logical_xor(const_9688.astype('uint64'), relay.reshape(var_9701.astype('uint64'), relay.shape_of(const_9688))) # shape=(28,)
output = relay.Tuple([bop_9660,var_9676,uop_9683,call_9687,const_9689,bop_9702,])
output2 = relay.Tuple([bop_9660,var_9676,uop_9685,call_9690,const_9689,bop_9702,])
func_9715 = relay.Function([var_9659,var_9676,var_9701,], output)
mod['func_9715'] = func_9715
mod = relay.transform.InferType()(mod)
mutated_mod['func_9715'] = func_9715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9715_call = mutated_mod.get_global_var('func_9715')
var_9717 = relay.var("var_9717", dtype = "uint16", shape = (14, 9, 5))#candidate|9717|(14, 9, 5)|var|uint16
var_9718 = relay.var("var_9718", dtype = "int32", shape = (96,))#candidate|9718|(96,)|var|int32
var_9719 = relay.var("var_9719", dtype = "int8", shape = (28,))#candidate|9719|(28,)|var|int8
call_9716 = func_9715_call(var_9717,var_9718,var_9719,)
output = call_9716
func_9720 = relay.Function([var_9717,var_9718,var_9719,], output)
mutated_mod['func_9720'] = func_9720
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5462_call = mod.get_global_var('func_5462')
func_5463_call = mutated_mod.get_global_var('func_5463')
call_9758 = func_5462_call()
call_9759 = func_5462_call()
output = relay.Tuple([call_9758,])
output2 = relay.Tuple([call_9759,])
func_9760 = relay.Function([], output)
mod['func_9760'] = func_9760
mod = relay.transform.InferType()(mod)
mutated_mod['func_9760'] = func_9760
mutated_mod = relay.transform.InferType()(mutated_mod)
func_9760_call = mutated_mod.get_global_var('func_9760')
call_9761 = func_9760_call()
output = call_9761
func_9762 = relay.Function([], output)
mutated_mod['func_9762'] = func_9762
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2310_call = mod.get_global_var('func_2310')
func_2312_call = mutated_mod.get_global_var('func_2312')
call_9775 = relay.TupleGetItem(func_2310_call(), 0)
call_9776 = relay.TupleGetItem(func_2312_call(), 0)
func_4703_call = mod.get_global_var('func_4703')
func_4707_call = mutated_mod.get_global_var('func_4707')
const_9783 = relay.const([[-5.387171,-0.520727,5.105189,-1.576390,-0.692431,-4.114665,-4.168596,-7.060358,3.894222,-6.900941,0.434238,5.888392,1.489256,5.626391,-2.695548,8.150230,4.285199,6.682161,-3.500688,-7.181482,7.589442,-8.635914,2.322455,9.980726,-1.948565,8.628578,-0.933287,2.011978,2.700765,-5.282989,0.995621,-2.658663,6.612768,-0.316937,1.149246,8.014585,3.489228,-6.608742,-6.360455,4.857060,-5.502999,6.489543,-9.708020,-8.303363,7.912898,5.792792,-5.949019,2.656034,6.681821,3.278930,-4.488769,5.219906,-1.885483,-6.265741,0.773143,-6.623090,-0.957231,-5.474229,-6.060063,-6.936037,6.731485,-7.240256,1.614730,-5.370886,9.052219,-4.637324,-4.940362,6.116264,5.969783,4.978690,-7.978083,-9.462729,9.242778,6.223327,-2.732101,-7.450725,0.452126,4.547297,-7.178139,8.599016,-2.822957,-2.658922,9.364470,9.468013,2.268046,6.782364,-9.885937,7.110309,-4.993770,7.736603,-9.747781,4.600232,5.752283,4.936612,-6.073738,9.366013,-5.542025,0.222830,-0.603903,-8.513309,8.130880,1.145758,-4.245892,-1.994292,5.275328,3.461882,0.317850,5.702752,9.337464,-1.808618,2.565491,-6.935528,9.395831,0.568382,5.956829,-8.121897,1.537441,-2.837500,-0.802496,-8.999180,3.451434,8.961790,-9.183549,1.246891,6.542037,7.963984,3.090102,-8.956032,1.935024,-8.632537,-4.509035,-3.361140,-1.564754,8.363633,3.129274,-0.781260,3.244639,7.247770,-4.676318,9.024290,-9.944352,-7.872514,2.995444,7.454326,-6.143527,9.642229,-8.897169,-0.249581,-7.781734,0.507880,-0.009584,-0.713192,5.791168,3.926749,-9.967761,-8.493160,-5.436977,2.692418,2.832065,-5.027983,-7.955090,-0.859487,2.516377,-4.381367,-0.045952,1.682962,7.905384,-2.298967,8.455872,9.587621,7.751146,6.715454,-0.005457,3.208229,8.015508,-0.128041,5.874120,-2.859233,8.411255,-7.033969,-6.214286,-9.846317,-5.923152,-8.784595,9.972934,6.151117,4.833272,-6.121973,6.959721,-3.962133,9.525348,6.599308,9.163362,-7.632479,-6.249544,7.797505,-9.321461,-3.233556,-5.925719,2.452372,-3.350196,-7.763558,1.233165,-9.439238,-5.747227,4.181256,8.051437,-4.098513,-7.927980,2.525477,-6.514682,3.648384,2.568044,6.412009,-6.479708,2.089410,7.901451,3.679479,-2.815980,-4.552661,-1.628263,-7.477184,-2.996166,-8.083732,7.019565,2.904939,-0.180938,9.299500,-3.757390,-7.764698,7.106211,-0.143996,2.434727,4.477234,3.990174,5.417614,4.812852,1.723827,-8.303477,-8.215177,6.952985,7.821787,-1.234026,2.789856,6.324346,4.350897,5.557866,-5.542227,0.677697,-0.171346,4.022688,-4.379044,-9.842156,-6.555594,-9.334308,-6.119739,-7.649097,8.265281,-0.577940,7.272867,-2.277232,-7.937973,-7.564357,5.164779,-7.295624,-7.548438,5.522449,-6.069733,-4.955771,-0.957097,9.720645,4.310912,4.899488,-8.824008,9.195497,2.849880,5.680729,-9.898339,-3.374142,9.699563,1.213642,-5.971950,1.181941,-3.385533,6.798805,-3.585637,-6.231458,-7.162968,-1.247467,5.712591,3.728927,-9.659744,6.071497,-7.553937,-9.410590,-3.948925,-1.791160,-8.414054,-3.448720,4.104049,0.944678,-0.498611,7.471075,5.313112,-1.979889,-3.560700,-0.036679,-8.890499,7.032425,8.107436,-5.714413,0.534986,4.948087,-6.728354,4.520604,2.503026,6.698800,-8.915116,4.391455,2.439056,-6.764843,3.048527,-0.194908,-5.301847,-5.194858,9.131108,-4.726837,2.054781,-0.837693,3.089608,-3.749411,-7.013738,-5.504523,-7.502738,3.046193,5.690710,1.000732,-7.840628,-8.530912,7.926456,-8.091168,-4.075435,-6.270883,-3.682674,4.424301,-1.538034,4.844215,-8.279775,5.000793,9.024762,-8.347127,-4.080490,1.621602,7.571414,-7.406850,-9.883477,8.283059,1.469907,4.625577,-6.361173,9.636793,-7.771376,7.425956,-3.342509,7.398407,2.132866,5.291567,-9.554847,-6.921743,-2.393300,-4.161281,-7.820424,8.436840,3.562459,8.430329,-8.623228,-2.839262,6.807700,6.995168,-9.804949,0.475596,-0.553600,-3.683066,2.865133,-0.360198,6.549540,0.607810,-7.688134,0.723613,9.502185,4.463670,9.293063,-9.708877,6.041620,-6.560277,-3.229978,-7.466639,-8.310234,8.107492,5.342319,-7.005911,7.437816,-9.410911,-6.950990,6.885299,5.998614,3.466203,7.768601,8.255287,8.103881,-9.771463,-7.824140,-9.681147,8.289181,-2.636701,5.230943,6.515224,-2.431320,-7.866590,2.567649,-3.671683,-8.608048,4.781772,7.643940,0.772288,5.721017,2.181481,-6.120407,-1.340632,5.236638,-7.516678,6.872184,3.083843,-9.773793,9.741653,-9.677895,-3.177138,6.459432,-0.410216,-0.542168,-7.113163,5.661551,6.820181,4.794966,-7.118181,3.871540,-9.931299,-5.894553,-2.014218,6.116350,8.699386,-6.281263,0.104764,0.571073,-2.380501,6.098262,8.845948,-5.960840,-5.323972,7.155426,0.220582,6.667146,1.668376,7.866218,-0.952011,4.315219,-6.072754,1.784314,-7.316730,7.499945,9.376809,3.796225,-6.426671,4.843236,4.321779,1.319869,5.161030,-7.319744,-2.461612,4.821165,3.665306,-7.925899,-4.169092,8.559580,6.161721,5.767534,4.867634,1.518217,4.686269,-2.365174,3.515885,1.659773,-0.583263,-6.322357,0.868920,-9.185018,-9.602040,9.253868,-1.924050,0.937536,8.418610,-1.564532,2.153826,-9.491902,5.061572,-7.013131,-0.969195,8.094175,5.924747,-6.000688,7.080600,6.447010,2.234486,-2.935766,8.048583,3.935220,4.884470,2.350935,-5.703165,2.055312,-4.653327,-7.485993,4.879486,-1.778311,6.241367,0.716433,3.467718,2.959947,8.086914,-0.425677,1.753427,-8.917275,-5.350070,-9.512556,1.131102,-2.987007,2.631951,4.018553,-8.286608,1.220079,-2.054387,0.313040,-4.824765,-6.398359,-2.662612,-8.350897,5.813503,-4.971583,2.283650,-9.342426,-5.801677,-9.467378,7.513392,-5.925334,3.198635,-2.696002,3.382433,2.368570,-6.930573,4.026837,1.238020,-0.491111,-9.872983,-3.884865,9.830971,3.271996,0.650140,7.357613,8.755657,-2.175934,-6.191668,-8.022819,-0.377007,5.555615,2.238415,-2.425564,-3.573342,5.650424,5.567841,-3.109405,-4.248678,5.896055,-5.461447,0.477617,-6.676013,-8.739623,-2.358360,-4.398577,4.613368,9.439793,0.011316,3.256418,-0.900650,-6.257035,-3.814572,6.438847,-7.405452,-7.893000,9.155735,-1.088064,1.708171,-1.362955,7.547802,9.735705,-7.463729,-9.045647,-1.191398,-0.830577,-7.308312,-3.804230,0.096373,-7.200584,-5.421054,-3.368537,-6.950345,-7.859425,-3.122329,9.463803,6.259241,-1.571169,3.703475,8.442915,-0.913318,-7.675533,1.489702,3.459215,-2.820398,-3.736148,-7.040940,8.014832,-8.571281,-5.905036,-8.856865,-0.782035,-1.101176,-9.380516,8.109034,3.628533,8.096100,1.096941,8.120216,4.945069,-1.157863,-3.508861,8.234392,3.164718,9.202478,-1.658704,1.301499,-5.725710,6.333972,3.965118,-9.092483,-9.758883,-4.302944,-6.576616,-6.298717,-4.660658,-1.688411,5.669064,-1.693540,8.677393,-5.100656,7.607718,-0.456564,-9.175010,-1.215074,9.967048,-4.758093,-9.325966,7.398581,-2.983859,3.930723,-7.463634,-1.079881,3.139623,-2.755882,-0.640885,-6.701488,-4.642351,3.661912,-2.418894,-5.463948,0.152305,4.882843,0.111186,-1.656285,-7.980629,-3.099159,8.070632,-0.861700,9.954012,6.725672,4.329858,-3.267345,8.056311,-1.904606,7.636238,3.271559,-1.924825,0.756076,6.966556,4.871611,4.084883,-4.000984,-9.911239,1.005271,9.996130,-6.601512,-3.298080,-0.823645,-1.610716,5.189544,2.097333,-5.670017,8.476250,4.689946,-9.487268,-4.709986,8.087895,-9.256429,1.029101,7.908731,4.130252,8.345389,-8.717216,0.636526,9.999792,0.884473,2.765126,-2.004106,8.609662,5.804431,-3.296388,6.479998,-1.747821,-6.440393,8.749247,-3.729796,7.095120,-6.472070,4.000474,-7.074709,-6.889068,2.885958,-8.812714,-5.113680,3.780895,9.073255,8.831401,4.804023,-0.076362,9.604398,-8.914990,-6.552741,4.097917,4.170080,-1.698077,9.531202,5.244150,-5.161130,-2.659716,3.177277,-8.545340,-6.073852,9.717558,7.401676,3.462954,3.885704,-6.007381,7.121885,-6.571822,-9.690329,-9.710887,4.061468,-6.224904,3.317697,-7.605650,9.072406,3.700071,-8.328553,6.340529,4.349489,-6.950165,-5.389505,-5.004913,0.373891,0.876013,-9.358403,3.902249,4.472429,9.163657,3.892530,-7.083230,8.445474,-2.867497,-2.331152,8.991271,-4.766808,0.715708,9.544466,-8.539592,-1.734922,-8.068803,3.513579,2.877955,-8.365547,-4.129363,-8.482932,-5.755287,-2.297553,-1.865593,-5.319592,-6.021090,3.530184,-1.299529,-5.166205,4.415049,-9.424812,4.853461,-6.799467,-6.579664,9.739681,-4.775550,1.404986,6.019246,6.978177,1.550354,-7.095000,-6.629389,2.330875,-4.101598,6.573109,-9.103068,2.585155,2.931451,-3.946363,-2.134285,-6.950246,-5.719943,8.191876,-7.110528,7.198672,2.109656,7.308857,2.064541,-4.980119,-0.453728,-9.654974,8.177461,-9.563924,8.297716,-6.659534,5.851145,-4.004977,6.935976,5.851451,-2.786831,7.187654,-7.566441,0.790484,5.679285,3.851944,6.265530,-3.414310,-8.404407,0.181075,-6.755954,3.191115,0.796978,7.697683,-4.022993,-5.500313,1.750992,-5.209005,-1.743078,2.834603,4.031975,-3.479280,-6.432304,6.508309,8.456099,-6.346243,-6.976304,7.682823,4.717400,-9.815205,-6.380341,-4.904453,-9.161699,9.595222,-7.518363,-4.206799,-0.605207,-6.618666,-1.814599,6.682386,8.876712,6.530490,6.533309,7.173978,9.470956,-6.880562,-5.267119,0.968050,8.100476,2.688475,0.852908,0.495959,-4.087283,8.317550,3.978526,3.911905,-2.058811,6.218012,9.332503,9.998149,-1.414381,-2.621135,-4.021887,-6.024286,0.153339,-0.912404,7.163196,-9.553990,6.518927,-5.168075,-4.484857,6.142928,-3.926899,-9.310421,9.349230,-5.293262,-0.883688,-5.130475,-4.062352,-0.511605,2.025349,8.872583,3.894302,-8.762741,9.104111,4.511140,-5.927791,-8.272033,1.536604,3.351451,-0.364694,4.247613,-8.827379,-5.977769,-9.543487,-8.519719,7.290487,-2.433574,3.918072,6.785468,-2.863569,-9.619679,-8.162078,1.364075,-0.433024,-9.831659,6.850991,6.592440,-6.082520,-5.380677,-5.610808,-0.707770,-7.768851,-7.260153,6.375356,-4.969730,6.657082,4.638562,-2.303938,0.817894,4.978117,6.004583,5.990281,-9.688976,-7.753339,-6.060484,-4.627511,-7.697375,-6.865879,-7.495925,8.809177,6.218017,-6.588201,-9.571850,1.773661,3.305095,6.836520,9.252249,5.461290,-7.858012,2.042975,-0.385026,8.493870,-0.312464,-8.510225,-5.327842,-3.041854,-4.593042,-8.512873,9.768034,-6.784102,-3.442238,4.743060,9.923569,6.810930,5.302684,-0.874932,-4.818630,-4.162443,9.120834,-2.200590,-7.294011,4.237734,6.779898,0.654595,-6.433902,2.925195,-7.947154,-9.049668,6.307844,2.138209,-4.200633,-4.482855,-7.136567,-7.208596,9.854724,2.798885,6.693495,-5.179806,-5.361239,0.513250,-6.048312,4.882649,6.241033,-0.172396,9.696368,8.446891,0.237415,2.993871,1.742310,-6.929518,-6.957226,-9.007144,-2.148767,-4.846092,1.231942,3.481733,-0.104869,-8.134260,5.805082,-9.564500,-5.891426,-0.456600,8.842900,2.435010,2.530411,-9.065542,7.619580,7.823502,2.762619,-4.441171,4.194197,-1.466561,-0.693068,-0.727346,2.701811,4.147159,-9.109537,-2.074251,8.998246,-5.062867,6.348678,-6.334280,-4.857270,-1.958669,9.160224,-7.129113,8.861341,-5.691670,5.046231,2.131621,2.466590,-5.164947,-5.614223,2.062913,9.952490,9.488147,-0.452751,2.143283,5.436444,4.206904,3.235322,-1.966984,-2.123676,-5.543675,1.789207,4.228752,-8.909560,-3.951420,-5.438697,-3.254830,-7.450918,-6.455000,2.713834,8.065923,6.699609,6.119903,-1.286067,5.487220,-5.562119,-3.086858,8.594513,-3.004155,9.082949,2.802802,8.096657,1.718848,4.119571,-1.039713,-6.906974,0.656952,-7.336418,-6.811786,-9.190979,-5.421812,0.673912,-8.917672,-5.451977,9.765416,-9.980286,6.559452,-7.925452,1.187010,-8.154478,1.965260,0.820146,-1.529444,0.888122,-2.762010,5.581647,6.297733,2.966618,1.963882,-3.645990,3.401570]], dtype = "float32")#candidate|9783|(1, 1152)|const|float32
var_9784 = relay.var("var_9784", dtype = "float64", shape = (98, 2))#candidate|9784|(98, 2)|var|float64
call_9782 = relay.TupleGetItem(func_4703_call(relay.reshape(const_9783.astype('float32'), [8, 9, 16]), relay.reshape(const_9783.astype('float32'), [8, 9, 16]), relay.reshape(var_9784.astype('float64'), [196,]), ), 0)
call_9785 = relay.TupleGetItem(func_4707_call(relay.reshape(const_9783.astype('float32'), [8, 9, 16]), relay.reshape(const_9783.astype('float32'), [8, 9, 16]), relay.reshape(var_9784.astype('float64'), [196,]), ), 0)
func_5718_call = mod.get_global_var('func_5718')
func_5719_call = mutated_mod.get_global_var('func_5719')
call_9792 = func_5718_call()
call_9793 = func_5718_call()
output = relay.Tuple([call_9775,call_9782,const_9783,var_9784,call_9792,])
output2 = relay.Tuple([call_9776,call_9785,const_9783,var_9784,call_9793,])
func_9796 = relay.Function([var_9784,], output)
mod['func_9796'] = func_9796
mod = relay.transform.InferType()(mod)
var_9797 = relay.var("var_9797", dtype = "float64", shape = (98, 2))#candidate|9797|(98, 2)|var|float64
output = func_9796(var_9797)
func_9798 = relay.Function([var_9797], output)
mutated_mod['func_9798'] = func_9798
mutated_mod = relay.transform.InferType()(mutated_mod)
var_9810 = relay.var("var_9810", dtype = "int8", shape = (16, 8, 11))#candidate|9810|(16, 8, 11)|var|int8
var_9811 = relay.var("var_9811", dtype = "int8", shape = (16, 8, 11))#candidate|9811|(16, 8, 11)|var|int8
bop_9812 = relay.minimum(var_9810.astype('int8'), relay.reshape(var_9811.astype('int8'), relay.shape_of(var_9810))) # shape=(16, 8, 11)
output = relay.Tuple([bop_9812,])
output2 = relay.Tuple([bop_9812,])
F = relay.Function([var_9810,var_9811,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_9810,var_9811,], output2)
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
