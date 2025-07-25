import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_97 = relay.var("var_97", dtype = "float32", shape = (4, 6, 6))#candidate|97|(4, 6, 6)|var|float32
const_98 = relay.const([[[8.861688,-7.879188,-1.316974,-0.726662,-3.697570,2.596630],[5.371455,-1.114931,7.773410,0.034781,-7.069345,3.752077],[-9.546203,-4.694583,1.170393,6.225350,6.432720,-2.042217],[0.018784,-2.633063,4.748604,-7.800937,-3.778471,-0.743841],[7.495366,2.939233,9.493918,-4.090053,-3.726590,-7.197153],[-2.269957,-9.083802,9.347795,-9.638662,3.523006,-9.466095]],[[-2.766000,-3.540955,5.386077,-5.417621,-3.116089,-9.959718],[-8.620097,1.138822,5.500040,-3.146883,9.557677,-5.755297],[7.544857,5.157256,5.471391,-7.907454,-3.518599,-0.173022],[6.602157,3.598695,-2.788568,-8.217535,-2.324805,8.908308],[9.312353,-2.237939,-1.180153,-5.642892,0.945061,5.774923],[2.279766,-9.391527,-8.992771,-2.886099,4.174656,6.949761]],[[3.957537,0.202297,8.095957,-0.121669,-6.529981,6.082925],[5.520597,9.027187,8.378106,9.602452,-0.148897,8.158285],[2.572131,-0.741153,0.140636,-0.239006,7.498769,-9.836565],[1.081057,-6.199030,3.671409,-6.893668,1.516505,1.748666],[-5.105635,7.100138,-7.923163,2.030596,-6.356764,8.791086],[3.779211,7.692564,5.590721,5.872881,-2.852557,-2.606552]],[[6.510111,-2.331132,-4.883956,-4.329923,-2.500758,6.439260],[-6.484768,-4.667030,0.080240,-2.272330,-3.555276,9.046207],[0.837870,-9.353270,-7.359812,-9.636493,4.419519,-4.760088],[-0.449490,5.021436,5.262366,-7.959181,4.300721,-4.118843],[-9.562377,-9.160832,-9.440679,-6.870167,-5.940867,8.471605],[5.071883,2.636546,-5.135288,6.851429,-2.349228,-8.952035]]], dtype = "float32")#candidate|98|(4, 6, 6)|const|float32
bop_99 = relay.floor_mod(var_97.astype('float32'), relay.reshape(const_98.astype('float32'), relay.shape_of(var_97))) # shape=(4, 6, 6)
bop_118 = relay.not_equal(var_97.astype('bool'), relay.reshape(bop_99.astype('bool'), relay.shape_of(var_97))) # shape=(4, 6, 6)
output = bop_118
output2 = bop_118
func_122 = relay.Function([var_97,], output)
mod['func_122'] = func_122
mod = relay.transform.InferType()(mod)
var_123 = relay.var("var_123", dtype = "float32", shape = (4, 6, 6))#candidate|123|(4, 6, 6)|var|float32
output = func_122(var_123)
func_124 = relay.Function([var_123], output)
mutated_mod['func_124'] = func_124
mutated_mod = relay.transform.InferType()(mutated_mod)
var_556 = relay.var("var_556", dtype = "float32", shape = (15, 3, 3))#candidate|556|(15, 3, 3)|var|float32
uop_557 = relay.sqrt(var_556.astype('float32')) # shape=(15, 3, 3)
output = relay.Tuple([uop_557,])
output2 = relay.Tuple([uop_557,])
func_560 = relay.Function([var_556,], output)
mod['func_560'] = func_560
mod = relay.transform.InferType()(mod)
mutated_mod['func_560'] = func_560
mutated_mod = relay.transform.InferType()(mutated_mod)
var_561 = relay.var("var_561", dtype = "float32", shape = (15, 3, 3))#candidate|561|(15, 3, 3)|var|float32
func_560_call = mutated_mod.get_global_var('func_560')
call_562 = func_560_call(var_561)
output = call_562
func_563 = relay.Function([var_561], output)
mutated_mod['func_563'] = func_563
mutated_mod = relay.transform.InferType()(mutated_mod)
var_864 = relay.var("var_864", dtype = "float32", shape = (12, 12, 2))#candidate|864|(12, 12, 2)|var|float32
uop_865 = relay.cosh(var_864.astype('float32')) # shape=(12, 12, 2)
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
const_868 = relay.const([9.355011,-5.370632,8.753542,-9.484775,5.157292,-0.570867,5.483366,-1.065333,7.177846,-9.543888,-6.711441,-9.449808,5.430076,-2.576421,-2.516684,7.128203,-4.617760,3.951029,4.518077,3.981351,-5.853361,-5.610897,-2.949234,0.251568,-4.450566,2.394932,-5.729254,4.520643,-2.692327,-1.285036,-8.286918,-8.428527,2.158891,-0.981398,-0.249682,1.903672,4.623610,-4.225663,-6.501625,4.756930,9.951581,-1.420890,1.132034,1.014406,2.742328,-5.077938,-1.224645,-7.801239,-1.899049,-5.943906,4.920562,2.166519,-4.582983,-1.693951,7.104836,4.376574,-8.466937,-9.009943,7.213663,8.286646,0.195597,-0.018872,5.947596,9.113736,0.821712,-4.160727,-8.700504,3.996320,1.824973,8.650908,2.803585,9.984015,-4.871387,9.194715,-8.733761,-8.693413,5.098829,8.080790,-3.319927,-5.199300,-5.736216,-0.213873,5.181221,0.392792,1.026007,5.740742,9.963538,5.280971,2.501636,5.414804,6.268522,3.038765,-5.150169,5.522684,-7.306751,-0.110429,-4.477714,9.260959,-9.702554,-9.595815,9.766704,5.211067,9.863785,0.297453,1.907967,-2.295842,-7.936777,0.576817,-2.670623,7.834148,4.989029,4.350346,-5.543962,7.035389,-2.403293,7.995976,7.911829,-8.499559,2.565516,3.111770,6.603207,5.809801,-3.468667,-9.260170,-9.579139,9.874552,-5.595626,6.640361,9.660501,2.794052,6.938554,2.700867,1.143395,6.613126,7.221558], dtype = "float32")#candidate|868|(135,)|const|float32
call_867 = relay.TupleGetItem(func_560_call(relay.reshape(const_868.astype('float32'), [15, 3, 3])), 0)
call_869 = relay.TupleGetItem(func_563_call(relay.reshape(const_868.astype('float32'), [15, 3, 3])), 0)
output = relay.Tuple([uop_865,call_867,const_868,])
output2 = relay.Tuple([uop_865,call_869,const_868,])
func_870 = relay.Function([var_864,], output)
mod['func_870'] = func_870
mod = relay.transform.InferType()(mod)
var_871 = relay.var("var_871", dtype = "float32", shape = (12, 12, 2))#candidate|871|(12, 12, 2)|var|float32
output = func_870(var_871)
func_872 = relay.Function([var_871], output)
mutated_mod['func_872'] = func_872
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1119 = relay.const(-0.702007, dtype = "float32")#candidate|1119|()|const|float32
var_1120 = relay.var("var_1120", dtype = "float32", shape = (1, 3, 7))#candidate|1120|(1, 3, 7)|var|float32
bop_1121 = relay.divide(const_1119.astype('float32'), var_1120.astype('float32')) # shape=(1, 3, 7)
func_870_call = mod.get_global_var('func_870')
func_872_call = mutated_mod.get_global_var('func_872')
var_1132 = relay.var("var_1132", dtype = "float32", shape = (8, 36))#candidate|1132|(8, 36)|var|float32
call_1131 = relay.TupleGetItem(func_870_call(relay.reshape(var_1132.astype('float32'), [12, 12, 2])), 1)
call_1133 = relay.TupleGetItem(func_872_call(relay.reshape(var_1132.astype('float32'), [12, 12, 2])), 1)
uop_1134 = relay.exp(bop_1121.astype('float32')) # shape=(1, 3, 7)
func_870_call = mod.get_global_var('func_870')
func_872_call = mutated_mod.get_global_var('func_872')
call_1144 = relay.TupleGetItem(func_870_call(relay.reshape(var_1132.astype('float32'), [12, 12, 2])), 1)
call_1145 = relay.TupleGetItem(func_872_call(relay.reshape(var_1132.astype('float32'), [12, 12, 2])), 1)
bop_1156 = relay.maximum(uop_1134.astype('int8'), relay.reshape(var_1120.astype('int8'), relay.shape_of(uop_1134))) # shape=(1, 3, 7)
uop_1165 = relay.log(uop_1134.astype('float32')) # shape=(1, 3, 7)
func_870_call = mod.get_global_var('func_870')
func_872_call = mutated_mod.get_global_var('func_872')
call_1193 = relay.TupleGetItem(func_870_call(relay.reshape(var_1132.astype('float32'), [12, 12, 2])), 1)
call_1194 = relay.TupleGetItem(func_872_call(relay.reshape(var_1132.astype('float32'), [12, 12, 2])), 1)
func_122_call = mod.get_global_var('func_122')
func_124_call = mutated_mod.get_global_var('func_124')
const_1198 = relay.const([8.575377,-1.374749,-7.562581,-0.093938,-3.935650,-0.770782,1.322297,-6.600496,0.034736,7.565963,-8.094976,-1.684652,-9.508825,1.866419,2.380067,-5.541829,-2.362720,-6.064591,9.170192,-4.215086,-1.019257,-3.670426,-7.233648,8.775629,6.857038,3.830685,-9.668858,-5.686373,5.728900,-9.343271,7.387951,5.173993,4.672208,-4.575108,-4.562807,-6.711190,6.419180,-7.551554,7.899672,5.771586,-7.369606,8.295763,-5.101121,-2.067080,8.431839,-0.558558,4.523889,-4.780475,-6.239355,9.067906,2.197235,0.376428,-4.632674,-1.647134,8.557430,5.080364,-8.238047,-6.041930,-0.724348,-6.119546,6.241750,-3.154154,-1.216422,3.110301,-9.116004,3.991371,-6.046763,-8.000505,4.303456,7.867368,4.778816,-4.178741,6.114558,-5.964812,4.406559,1.080515,-3.300326,5.336006,-4.781497,3.597837,7.159458,-4.689577,0.245592,2.009928,6.941331,-0.032601,2.513223,-4.796452,7.517305,-7.327589,8.363205,-3.835969,2.353431,-7.561517,-2.615817,-3.674297,-9.126549,-8.263723,-5.521024,-9.368742,-8.891799,-5.763668,-7.934456,-5.252903,5.334662,-3.502580,-8.900691,-8.996308,8.584291,7.696950,-2.827672,9.347116,-2.743990,0.819020,6.962181,-3.489933,-8.380970,3.019768,4.921062,-2.475354,-1.558793,7.842287,7.550759,3.910428,-4.938285,5.350902,-3.634815,3.400111,-2.186621,6.794494,7.941294,1.379080,-0.232538,-3.286165,-4.813090,1.534588,1.864698,2.449753,-6.454287,2.070555,9.068030,-2.726684,-7.426082,-3.862891], dtype = "float32")#candidate|1198|(144,)|const|float32
call_1197 = func_122_call(relay.reshape(const_1198.astype('float32'), [4, 6, 6]))
call_1199 = func_122_call(relay.reshape(const_1198.astype('float32'), [4, 6, 6]))
output = relay.Tuple([call_1131,var_1132,call_1144,bop_1156,uop_1165,call_1193,call_1197,const_1198,])
output2 = relay.Tuple([call_1133,var_1132,call_1145,bop_1156,uop_1165,call_1194,call_1199,const_1198,])
func_1213 = relay.Function([var_1120,var_1132,], output)
mod['func_1213'] = func_1213
mod = relay.transform.InferType()(mod)
var_1214 = relay.var("var_1214", dtype = "float32", shape = (1, 3, 7))#candidate|1214|(1, 3, 7)|var|float32
var_1215 = relay.var("var_1215", dtype = "float32", shape = (8, 36))#candidate|1215|(8, 36)|var|float32
output = func_1213(var_1214,var_1215,)
func_1216 = relay.Function([var_1214,var_1215,], output)
mutated_mod['func_1216'] = func_1216
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1276 = relay.var("var_1276", dtype = "float32", shape = (5, 10, 16))#candidate|1276|(5, 10, 16)|var|float32
uop_1277 = relay.atan(var_1276.astype('float32')) # shape=(5, 10, 16)
func_870_call = mod.get_global_var('func_870')
func_872_call = mutated_mod.get_global_var('func_872')
const_1285 = relay.const([-6.359797,8.601587,-6.196134,-6.292699,-2.473283,3.759019,-4.688444,-4.609954,4.630579,9.605322,-5.877470,-5.146954,7.468388,4.339388,-7.648030,-1.636019,-5.574960,0.918227,-5.569890,-8.840589,-1.382709,-3.872630,8.854403,4.172228,1.004766,-7.949789,9.025413,8.550982,4.576622,3.970969,-8.708266,-4.693236,8.319887,2.020257,3.924219,2.361583,-2.248772,-1.624245,-1.592246,-8.133853,-0.886675,0.353670,4.463135,-9.212564,7.066085,6.681997,0.175325,-3.810600,1.119673,-0.272025,8.001966,9.194921,1.655841,-9.953031,5.551709,-4.254435,0.068708,4.101858,-8.205614,6.502806,5.888269,8.993313,-0.175177,7.810615,-8.947687,-7.478451,4.527157,4.333756,0.394434,2.354971,-5.412340,-0.162313,8.909232,2.247663,4.953499,-0.385954,5.937261,6.419809,5.033102,3.290558,0.965017,-2.056577,2.788749,7.238629,0.211939,7.329586,-5.973780,2.488200,2.739498,-2.491509,-5.459352,0.586337,-1.892005,3.424021,-3.013725,6.094073,3.188937,-8.845985,9.368401,4.188857,-2.727111,1.267785,1.118529,5.269976,6.981475,5.910576,-8.700583,3.791633,-8.307302,-3.204084,0.752659,-9.313559,9.788044,-8.120740,-2.969491,2.549207,-0.102591,-2.577214,-8.872660,8.440315,4.260346,4.835027,2.438822,-6.730155,3.987602,-7.503196,7.168632,1.359432,-6.254754,5.918053,-5.332836,9.541988,6.993797,-5.354326,7.200249,4.905155,-2.328878,-5.502367,4.472753,8.045481,-3.634496,-6.935818,-1.154685,-9.708927,3.649564,-7.747739,8.677925,-3.952437,3.038407,-6.580553,-3.136690,6.964762,-2.077987,0.702947,-5.922374,-7.773090,-7.224686,-3.081872,7.463248,5.635928,4.879020,-4.936343,-2.141447,5.831934,2.596909,-1.274226,-6.996334,-2.011703,-7.498567,-2.853379,0.702070,7.049119,6.567074,-2.404583,-1.762849,1.798500,7.786215,-2.330144,9.628613,6.175342,9.270281,-3.220111,6.479403,-7.470696,-5.109674,6.698257,-8.424496,-2.435812,-2.347892,-0.496773,-8.277837,-0.670458,6.357871,0.183131,0.230690,8.224541,6.083593,-8.011161,-1.061819,-1.870465,9.081956,-9.175492,-8.364885,-8.034866,-3.829449,7.116582,-4.104052,-0.555197,3.623111,-1.066874,4.979882,4.589754,-8.658514,9.083671,9.113232,2.517649,7.201757,-6.115995,-6.920258,8.348354,8.561446,-3.750497,-7.803922,2.031241,-3.853518,-2.087209,1.195319,-6.493733,0.930985,-1.287227,4.667179,-4.881470,-6.835533,-5.264810,7.069397,2.759011,1.984696,-4.224052,-4.670426,5.237602,-0.835939,-7.976806,3.459748,4.549956,5.679653,6.402183,3.920487,6.802305,-3.157240,5.881802,9.121361,-0.075454,-1.409306,6.519579,-8.060558,9.698741,-8.101939,-0.318278,3.649382,6.833442,-5.795538,8.829660,-0.449046,2.781207,5.354374,-4.444991,7.329015,3.045494,6.644918,-3.650418,3.809231,-9.067459,-9.206545,2.112786,-7.551093,-4.525795,-5.513358,3.025949,-0.901446,9.964914,0.908240,4.127011,1.035071,-9.830509,3.503787,-7.204605,-8.328029,-1.245925], dtype = "float32")#candidate|1285|(288,)|const|float32
call_1284 = relay.TupleGetItem(func_870_call(relay.reshape(const_1285.astype('float32'), [12, 12, 2])), 2)
call_1286 = relay.TupleGetItem(func_872_call(relay.reshape(const_1285.astype('float32'), [12, 12, 2])), 2)
func_1213_call = mod.get_global_var('func_1213')
func_1216_call = mutated_mod.get_global_var('func_1216')
var_1316 = relay.var("var_1316", dtype = "float32", shape = (21, 1))#candidate|1316|(21, 1)|var|float32
call_1315 = relay.TupleGetItem(func_1213_call(relay.reshape(var_1316.astype('float32'), [1, 3, 7]), relay.reshape(const_1285.astype('float32'), [8, 36]), ), 1)
call_1317 = relay.TupleGetItem(func_1216_call(relay.reshape(var_1316.astype('float32'), [1, 3, 7]), relay.reshape(const_1285.astype('float32'), [8, 36]), ), 1)
output = relay.Tuple([uop_1277,call_1284,const_1285,call_1315,var_1316,])
output2 = relay.Tuple([uop_1277,call_1286,const_1285,call_1317,var_1316,])
func_1326 = relay.Function([var_1276,var_1316,], output)
mod['func_1326'] = func_1326
mod = relay.transform.InferType()(mod)
var_1327 = relay.var("var_1327", dtype = "float32", shape = (5, 10, 16))#candidate|1327|(5, 10, 16)|var|float32
var_1328 = relay.var("var_1328", dtype = "float32", shape = (21, 1))#candidate|1328|(21, 1)|var|float32
output = func_1326(var_1327,var_1328,)
func_1329 = relay.Function([var_1327,var_1328,], output)
mutated_mod['func_1329'] = func_1329
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1510 = relay.var("var_1510", dtype = "int64", shape = (6, 13, 4))#candidate|1510|(6, 13, 4)|var|int64
var_1511 = relay.var("var_1511", dtype = "int64", shape = (6, 13, 4))#candidate|1511|(6, 13, 4)|var|int64
bop_1512 = relay.multiply(var_1510.astype('int64'), relay.reshape(var_1511.astype('int64'), relay.shape_of(var_1510))) # shape=(6, 13, 4)
output = relay.Tuple([bop_1512,])
output2 = relay.Tuple([bop_1512,])
func_1529 = relay.Function([var_1510,var_1511,], output)
mod['func_1529'] = func_1529
mod = relay.transform.InferType()(mod)
mutated_mod['func_1529'] = func_1529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1529_call = mutated_mod.get_global_var('func_1529')
var_1531 = relay.var("var_1531", dtype = "int64", shape = (6, 13, 4))#candidate|1531|(6, 13, 4)|var|int64
var_1532 = relay.var("var_1532", dtype = "int64", shape = (6, 13, 4))#candidate|1532|(6, 13, 4)|var|int64
call_1530 = func_1529_call(var_1531,var_1532,)
output = call_1530
func_1533 = relay.Function([var_1531,var_1532,], output)
mutated_mod['func_1533'] = func_1533
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1591 = relay.var("var_1591", dtype = "float64", shape = (13, 1, 10))#candidate|1591|(13, 1, 10)|var|float64
var_1592 = relay.var("var_1592", dtype = "float64", shape = (13, 1, 10))#candidate|1592|(13, 1, 10)|var|float64
bop_1593 = relay.divide(var_1591.astype('float64'), relay.reshape(var_1592.astype('float64'), relay.shape_of(var_1591))) # shape=(13, 1, 10)
func_1326_call = mod.get_global_var('func_1326')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_1634 = relay.var("var_1634", dtype = "float32", shape = (800, 1))#candidate|1634|(800, 1)|var|float32
var_1635 = relay.var("var_1635", dtype = "float32", shape = (21,))#candidate|1635|(21,)|var|float32
call_1633 = relay.TupleGetItem(func_1326_call(relay.reshape(var_1634.astype('float32'), [5, 10, 16]), relay.reshape(var_1635.astype('float32'), [21, 1]), ), 0)
call_1636 = relay.TupleGetItem(func_1329_call(relay.reshape(var_1634.astype('float32'), [5, 10, 16]), relay.reshape(var_1635.astype('float32'), [21, 1]), ), 0)
output = relay.Tuple([bop_1593,call_1633,var_1634,var_1635,])
output2 = relay.Tuple([bop_1593,call_1636,var_1634,var_1635,])
func_1641 = relay.Function([var_1591,var_1592,var_1634,var_1635,], output)
mod['func_1641'] = func_1641
mod = relay.transform.InferType()(mod)
var_1642 = relay.var("var_1642", dtype = "float64", shape = (13, 1, 10))#candidate|1642|(13, 1, 10)|var|float64
var_1643 = relay.var("var_1643", dtype = "float64", shape = (13, 1, 10))#candidate|1643|(13, 1, 10)|var|float64
var_1644 = relay.var("var_1644", dtype = "float32", shape = (800, 1))#candidate|1644|(800, 1)|var|float32
var_1645 = relay.var("var_1645", dtype = "float32", shape = (21,))#candidate|1645|(21,)|var|float32
output = func_1641(var_1642,var_1643,var_1644,var_1645,)
func_1646 = relay.Function([var_1642,var_1643,var_1644,var_1645,], output)
mutated_mod['func_1646'] = func_1646
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1738 = relay.var("var_1738", dtype = "bool", shape = (8, 16, 15))#candidate|1738|(8, 16, 15)|var|bool
var_1739 = relay.var("var_1739", dtype = "bool", shape = (8, 16, 15))#candidate|1739|(8, 16, 15)|var|bool
bop_1740 = relay.logical_or(var_1738.astype('bool'), relay.reshape(var_1739.astype('bool'), relay.shape_of(var_1738))) # shape=(8, 16, 15)
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
const_1748 = relay.const([3.299275,-1.172510,5.657557,-2.749481,-6.609734,-4.497417,-7.615651,-2.682612,5.465724,-2.411078,-1.287146,1.628813,2.913219,4.989671,3.941930,0.691937,1.539420,-9.918514,6.198578,5.655542,3.335767,4.687361,2.440593,9.508196,-7.338800,7.044771,-4.057477,1.954556,3.323047,-9.303373,0.702248,2.475608,-8.395386,6.785296,-1.919489,0.811841,5.349834,1.429256,-5.199318,5.453670,-8.108875,4.302353,0.657710,1.987765,-0.174273,4.193725,1.054007,-2.052632,1.446843,0.083588,-3.211820,7.373142,5.373644,5.312416,2.799862,-4.338450,4.618146,7.860938,-2.526043,1.180821,-2.460950,-5.981155,8.990390,4.240715,-6.733597,-0.630194,-9.665108,-8.280660,4.146066,2.573782,-1.647101,-6.139328,-2.622077,-5.930134,-6.510717,4.392705,7.471323,-4.489473,-8.706153,2.019563,-1.853999,5.556693,4.489354,-6.417737,0.798334,0.050416,5.061829,3.448261,1.980582,-6.688893,0.628212,0.386353,9.110832,1.214222,4.815014,7.271607,3.560645,-3.637652,-6.613629,9.760709,2.218972,-9.406687,-3.344357,-2.685911,6.586901,-3.597597,-1.424191,4.907429,1.991392,1.024321,5.900759,0.842933,5.352663,7.623809,-8.829888,-5.753053,-1.838641,7.964421,-8.394048,-4.806013,-4.696967,6.822343,-8.348221,4.282120,1.354404,0.862484,5.289312,0.117273,-0.064729,-2.818812,8.668284,-3.725197,0.159417,2.399951,5.169550], dtype = "float32")#candidate|1748|(135,)|const|float32
call_1747 = relay.TupleGetItem(func_560_call(relay.reshape(const_1748.astype('float32'), [15, 3, 3])), 0)
call_1749 = relay.TupleGetItem(func_563_call(relay.reshape(const_1748.astype('float32'), [15, 3, 3])), 0)
bop_1757 = relay.bitwise_and(bop_1740.astype('int8'), relay.reshape(var_1739.astype('int8'), relay.shape_of(bop_1740))) # shape=(8, 16, 15)
output = relay.Tuple([call_1747,const_1748,bop_1757,])
output2 = relay.Tuple([call_1749,const_1748,bop_1757,])
func_1770 = relay.Function([var_1738,var_1739,], output)
mod['func_1770'] = func_1770
mod = relay.transform.InferType()(mod)
mutated_mod['func_1770'] = func_1770
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1770_call = mutated_mod.get_global_var('func_1770')
var_1772 = relay.var("var_1772", dtype = "bool", shape = (8, 16, 15))#candidate|1772|(8, 16, 15)|var|bool
var_1773 = relay.var("var_1773", dtype = "bool", shape = (8, 16, 15))#candidate|1773|(8, 16, 15)|var|bool
call_1771 = func_1770_call(var_1772,var_1773,)
output = call_1771
func_1774 = relay.Function([var_1772,var_1773,], output)
mutated_mod['func_1774'] = func_1774
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1901 = relay.var("var_1901", dtype = "float64", shape = (15, 14, 9))#candidate|1901|(15, 14, 9)|var|float64
uop_1902 = relay.atanh(var_1901.astype('float64')) # shape=(15, 14, 9)
output = relay.Tuple([uop_1902,])
output2 = relay.Tuple([uop_1902,])
func_1904 = relay.Function([var_1901,], output)
mod['func_1904'] = func_1904
mod = relay.transform.InferType()(mod)
var_1905 = relay.var("var_1905", dtype = "float64", shape = (15, 14, 9))#candidate|1905|(15, 14, 9)|var|float64
output = func_1904(var_1905)
func_1906 = relay.Function([var_1905], output)
mutated_mod['func_1906'] = func_1906
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1926 = relay.const([[[-5,-7,6,10,1],[6,2,3,4,4],[7,8,9,-10,-4],[-8,-5,2,4,-7],[-1,1,10,7,-9],[7,6,-5,5,-3],[-6,8,7,-3,3],[-4,-4,-10,-10,-10]],[[8,5,5,1,7],[8,7,9,5,-5],[-1,-3,-3,-9,1],[-3,7,7,2,-1],[-3,6,-5,4,-4],[-10,-7,10,-7,-6],[-6,-1,9,-4,-5],[-1,4,-8,2,-10]],[[-2,-3,-5,-10,4],[3,5,5,-2,-6],[-4,3,6,-8,5],[7,10,8,-7,-8],[-4,-10,-6,2,4],[3,5,-7,-1,-1],[6,-6,10,-2,4],[-5,-2,5,8,6]],[[-7,1,8,5,4],[8,4,6,9,2],[-7,-10,-1,-7,-6],[2,-3,-7,2,10],[8,8,1,-9,-2],[-4,7,8,-2,-7],[-9,2,-4,2,-1],[-4,2,2,-7,-4]],[[1,8,3,-5,10],[-1,-3,-2,2,-4],[8,-1,-1,-4,7],[7,-9,5,10,6],[2,-2,2,1,-8],[6,-5,6,3,6],[1,5,10,-1,10],[4,-9,-4,-8,7]],[[-1,2,2,-4,2],[-3,5,3,10,10],[5,1,-8,-5,1],[4,4,10,8,1],[5,-10,-3,-10,1],[4,-1,8,-9,10],[4,4,2,4,-9],[7,-8,-6,4,-8]]], dtype = "int64")#candidate|1926|(6, 8, 5)|const|int64
var_1927 = relay.var("var_1927", dtype = "int64", shape = (6, 8, 5))#candidate|1927|(6, 8, 5)|var|int64
bop_1928 = relay.left_shift(const_1926.astype('int64'), relay.reshape(var_1927.astype('int64'), relay.shape_of(const_1926))) # shape=(6, 8, 5)
output = relay.Tuple([bop_1928,])
output2 = relay.Tuple([bop_1928,])
func_1931 = relay.Function([var_1927,], output)
mod['func_1931'] = func_1931
mod = relay.transform.InferType()(mod)
mutated_mod['func_1931'] = func_1931
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1932 = relay.var("var_1932", dtype = "int64", shape = (6, 8, 5))#candidate|1932|(6, 8, 5)|var|int64
func_1931_call = mutated_mod.get_global_var('func_1931')
call_1933 = func_1931_call(var_1932)
output = call_1933
func_1934 = relay.Function([var_1932], output)
mutated_mod['func_1934'] = func_1934
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1974 = relay.const([[[7.887655,8.919044,-9.932474]],[[5.544967,3.409749,-2.637725]],[[-7.053339,-4.495317,9.900152]],[[6.916555,-7.568130,8.457487]],[[4.396270,7.427722,-3.497213]],[[8.690645,6.398283,2.096378]]], dtype = "float64")#candidate|1974|(6, 1, 3)|const|float64
const_1975 = relay.const([[[-3.806512,0.879406,-5.239639],[1.797027,7.131105,-1.289851],[4.970722,-2.320864,-0.672301],[8.243509,-3.166688,-2.279179],[4.342298,0.954347,-6.099429],[-0.868927,-7.173433,0.468056],[7.999902,6.022576,-8.116110],[-8.039018,5.823622,-8.279705],[-0.588660,1.535058,5.894483]],[[9.212011,5.396131,2.168980],[9.978902,-8.363970,2.386354],[-1.871398,6.131918,-8.833207],[3.634031,2.835088,1.156741],[-3.662253,5.875766,1.491541],[0.615700,-3.833268,3.059298],[-5.735547,5.367689,3.376139],[-7.828664,4.223094,3.200027],[1.280032,8.926401,2.901554]],[[2.353014,-5.006251,6.795233],[1.186796,-3.767350,4.443589],[3.513729,-8.903550,2.289795],[-3.526814,8.921483,6.010234],[6.673217,5.131024,6.745698],[9.141022,-9.282456,7.695216],[6.567369,-0.278996,-4.359493],[-0.861301,4.708937,-3.300983],[-8.951663,2.764436,0.865199]],[[-0.331289,8.626435,0.262306],[-8.376443,2.861450,-2.352044],[1.472294,4.744707,-1.563920],[0.428749,-8.834592,4.966251],[7.943256,4.214445,-2.221847],[5.674852,6.351470,-4.765197],[4.495291,7.445489,-5.145948],[-9.246940,-1.663044,1.089858],[3.747452,9.856260,-8.760681]],[[1.755474,-3.281074,-1.208519],[0.663989,6.707073,-0.268554],[4.600550,-3.708691,4.935779],[-8.162749,-0.941039,1.153660],[0.508793,9.308960,-9.621420],[-8.410195,1.318613,-5.933515],[7.134843,-3.888280,-6.228348],[-2.964988,-7.907012,2.236902],[4.980474,9.641277,-4.848084]],[[-5.552291,-2.087316,-8.986038],[7.529888,-8.193479,9.871165],[-5.010953,-6.369083,9.275789],[6.629180,-1.982202,-7.776150],[3.872941,4.835154,-6.169783],[-1.059536,-0.837405,-4.933397],[3.860105,9.040531,-4.564437],[5.302086,1.739974,8.198799],[-4.267095,-5.440568,1.145642]]], dtype = "float64")#candidate|1975|(6, 9, 3)|const|float64
bop_1976 = relay.floor_divide(const_1974.astype('float64'), const_1975.astype('float64')) # shape=(6, 9, 3)
func_870_call = mod.get_global_var('func_870')
func_872_call = mutated_mod.get_global_var('func_872')
const_1984 = relay.const([6.713487,7.023971,3.055403,9.457033,5.587194,-3.782052,0.318097,-3.328294,-2.761751,-1.076261,-5.398196,-4.491985,2.524737,3.249385,-4.019808,-5.292642,-1.837400,-0.210650,-9.699094,-1.011611,-2.323749,6.202513,1.955024,-8.641001,-5.597004,-2.268075,7.129062,-3.857460,-5.145579,7.683695,8.174075,-5.166143,1.060909,-2.211334,2.337066,3.889337,8.634397,5.371735,7.052095,-1.394724,-4.396945,-3.631809,6.701782,-1.370876,1.700958,-3.521529,-8.296033,-7.136442,-6.321277,4.234163,-9.399578,8.895798,2.573598,-3.003570,-5.146413,9.344155,3.942053,1.653793,-0.399712,-7.647712,9.498646,4.191282,9.807281,-4.339705,-7.240927,7.370935,-3.031910,-5.021022,8.828139,-0.840594,2.501391,2.032304,-4.564339,0.866127,-8.359995,-8.868001,9.325461,4.815286,4.374229,-0.603333,0.545187,-0.330207,-8.084773,-4.478507,1.256622,2.634091,-6.236097,6.348170,2.747771,0.926679,-3.024549,-3.972888,5.271821,0.957880,7.356404,-8.263788,0.515493,-9.305839,7.837805,-9.117290,-4.295501,2.137920,-7.199308,0.592306,-2.955727,0.850909,-6.850781,-3.764893,-0.324778,-0.564607,5.212339,-3.743233,-3.230413,-7.920024,2.163473,-2.144935,-6.908259,-3.522268,7.283527,1.969654,8.556192,-6.041033,-3.935375,8.091023,-1.845933,-8.086163,5.171352,9.054972,0.983159,2.458215,-5.115198,-1.264347,-8.745220,2.235181,-2.133002,2.868151,9.048068,8.028944,-0.135151,-9.368525,6.936849,-7.808777,-5.764258,-4.688993,6.419073,-5.807766,0.766777,-8.381933,-8.441299,7.684245,-6.914201,-5.303993,0.725349,5.230681,-7.961260,-0.228389,-9.375923,-7.313266,-0.720178,4.242266,9.854598,3.728877,-7.839501,-7.733414,7.836843,-9.580065,-9.000853,-2.494044,-0.841588,1.141758,7.091823,-3.213728,-1.059174,-3.439656,6.137542,-8.606378,-9.585697,-4.880657,7.312662,6.913811,-9.014466,8.279978,-5.378730,-7.589492,8.030644,0.492894,-8.088569,8.118083,8.461024,3.786596,2.854437,1.141564,-6.114319,-6.055533,-8.070529,-2.867428,5.831402,2.737002,4.225993,0.729653,8.194368,-7.764625,-4.780253,-5.907069,2.472329,3.637955,6.343417,-0.743601,-7.292432,2.544163,-1.947629,9.176560,1.318631,1.744275,3.010396,-9.078782,-2.866388,-4.800932,-5.050502,-0.526209,-5.531336,-7.956463,-2.457860,8.522996,5.305488,5.976025,2.231657,-0.622044,6.425945,2.887234,-4.731715,8.585148,-1.935124,6.143632,-2.969753,6.326608,5.245489,-6.371294,-0.940275,-4.120159,-0.151149,-9.877032,6.397173,5.566048,-3.339528,0.674982,-7.546580,2.550792,-6.655598,4.641310,-9.405418,4.618672,-3.085622,9.449683,-7.167888,-9.787536,2.117071,-6.911337,2.045800,6.306732,-1.890434,-3.580355,0.461343,-7.365322,3.466986,-5.716815,-5.576067,6.266839,1.567219,7.481167,2.107099,3.767815,-7.118789,7.357672,1.470440,-0.011748,5.261497,-2.338528,-7.631110,-3.955607,-0.239368,-7.559528,-4.143972,0.650226,-2.211188,6.903914,-1.198625,7.906660], dtype = "float32")#candidate|1984|(288,)|const|float32
call_1983 = relay.TupleGetItem(func_870_call(relay.reshape(const_1984.astype('float32'), [12, 12, 2])), 2)
call_1985 = relay.TupleGetItem(func_872_call(relay.reshape(const_1984.astype('float32'), [12, 12, 2])), 2)
output = relay.Tuple([bop_1976,call_1983,const_1984,])
output2 = relay.Tuple([bop_1976,call_1985,const_1984,])
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
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_1997 = relay.TupleGetItem(func_1986_call(), 0)
call_1998 = relay.TupleGetItem(func_1988_call(), 0)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_1999 = relay.TupleGetItem(func_1986_call(), 0)
call_2000 = relay.TupleGetItem(func_1988_call(), 0)
uop_2003 = relay.sinh(call_1999.astype('float64')) # shape=(6, 9, 3)
uop_2005 = relay.sinh(call_2000.astype('float64')) # shape=(6, 9, 3)
output = relay.Tuple([call_1997,uop_2003,])
output2 = relay.Tuple([call_1998,uop_2005,])
func_2017 = relay.Function([], output)
mod['func_2017'] = func_2017
mod = relay.transform.InferType()(mod)
mutated_mod['func_2017'] = func_2017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mutated_mod.get_global_var('func_2017')
call_2018 = func_2017_call()
output = call_2018
func_2019 = relay.Function([], output)
mutated_mod['func_2019'] = func_2019
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2046 = relay.TupleGetItem(func_2017_call(), 0)
call_2047 = relay.TupleGetItem(func_2019_call(), 0)
func_1904_call = mod.get_global_var('func_1904')
func_1906_call = mutated_mod.get_global_var('func_1906')
var_2054 = relay.var("var_2054", dtype = "float64", shape = (1890,))#candidate|2054|(1890,)|var|float64
call_2053 = relay.TupleGetItem(func_1904_call(relay.reshape(var_2054.astype('float64'), [15, 14, 9])), 0)
call_2055 = relay.TupleGetItem(func_1906_call(relay.reshape(var_2054.astype('float64'), [15, 14, 9])), 0)
func_1904_call = mod.get_global_var('func_1904')
func_1906_call = mutated_mod.get_global_var('func_1906')
call_2061 = relay.TupleGetItem(func_1904_call(relay.reshape(call_2053.astype('float64'), [15, 14, 9])), 0)
call_2062 = relay.TupleGetItem(func_1906_call(relay.reshape(call_2053.astype('float64'), [15, 14, 9])), 0)
output = relay.Tuple([call_2046,call_2053,var_2054,call_2061,])
output2 = relay.Tuple([call_2047,call_2055,var_2054,call_2062,])
func_2075 = relay.Function([var_2054,], output)
mod['func_2075'] = func_2075
mod = relay.transform.InferType()(mod)
mutated_mod['func_2075'] = func_2075
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2076 = relay.var("var_2076", dtype = "float64", shape = (1890,))#candidate|2076|(1890,)|var|float64
func_2075_call = mutated_mod.get_global_var('func_2075')
call_2077 = func_2075_call(var_2076)
output = call_2077
func_2078 = relay.Function([var_2076], output)
mutated_mod['func_2078'] = func_2078
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2080 = relay.TupleGetItem(func_2017_call(), 0)
call_2081 = relay.TupleGetItem(func_2019_call(), 0)
output = relay.Tuple([call_2080,])
output2 = relay.Tuple([call_2081,])
func_2089 = relay.Function([], output)
mod['func_2089'] = func_2089
mod = relay.transform.InferType()(mod)
mutated_mod['func_2089'] = func_2089
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mutated_mod.get_global_var('func_2089')
call_2090 = func_2089_call()
output = call_2090
func_2091 = relay.Function([], output)
mutated_mod['func_2091'] = func_2091
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2109 = relay.var("var_2109", dtype = "float64", shape = (2, 11, 6))#candidate|2109|(2, 11, 6)|var|float64
uop_2110 = relay.asin(var_2109.astype('float64')) # shape=(2, 11, 6)
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
var_2132 = relay.var("var_2132", dtype = "float32", shape = (135,))#candidate|2132|(135,)|var|float32
call_2131 = relay.TupleGetItem(func_560_call(relay.reshape(var_2132.astype('float32'), [15, 3, 3])), 0)
call_2133 = relay.TupleGetItem(func_563_call(relay.reshape(var_2132.astype('float32'), [15, 3, 3])), 0)
uop_2146 = relay.cos(var_2109.astype('float64')) # shape=(2, 11, 6)
output = relay.Tuple([uop_2110,call_2131,var_2132,uop_2146,])
output2 = relay.Tuple([uop_2110,call_2133,var_2132,uop_2146,])
func_2148 = relay.Function([var_2109,var_2132,], output)
mod['func_2148'] = func_2148
mod = relay.transform.InferType()(mod)
var_2149 = relay.var("var_2149", dtype = "float64", shape = (2, 11, 6))#candidate|2149|(2, 11, 6)|var|float64
var_2150 = relay.var("var_2150", dtype = "float32", shape = (135,))#candidate|2150|(135,)|var|float32
output = func_2148(var_2149,var_2150,)
func_2151 = relay.Function([var_2149,var_2150,], output)
mutated_mod['func_2151'] = func_2151
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_2159 = relay.TupleGetItem(func_2089_call(), 0)
call_2160 = relay.TupleGetItem(func_2091_call(), 0)
uop_2161 = relay.acosh(call_2159.astype('float64')) # shape=(6, 9, 3)
uop_2163 = relay.acosh(call_2160.astype('float64')) # shape=(6, 9, 3)
output = uop_2161
output2 = uop_2163
func_2171 = relay.Function([], output)
mod['func_2171'] = func_2171
mod = relay.transform.InferType()(mod)
output = func_2171()
func_2172 = relay.Function([], output)
mutated_mod['func_2172'] = func_2172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_2196 = relay.TupleGetItem(func_1986_call(), 0)
call_2197 = relay.TupleGetItem(func_1988_call(), 0)
func_2075_call = mod.get_global_var('func_2075')
func_2078_call = mutated_mod.get_global_var('func_2078')
var_2206 = relay.var("var_2206", dtype = "float64", shape = (1890,))#candidate|2206|(1890,)|var|float64
call_2205 = relay.TupleGetItem(func_2075_call(relay.reshape(var_2206.astype('float64'), [1890,])), 0)
call_2207 = relay.TupleGetItem(func_2078_call(relay.reshape(var_2206.astype('float64'), [1890,])), 0)
uop_2226 = relay.atan(var_2206.astype('float32')) # shape=(1890,)
var_2235 = relay.var("var_2235", dtype = "float64", shape = (6, 9, 3))#candidate|2235|(6, 9, 3)|var|float64
bop_2236 = relay.maximum(call_2196.astype('float64'), relay.reshape(var_2235.astype('float64'), relay.shape_of(call_2196))) # shape=(6, 9, 3)
bop_2239 = relay.maximum(call_2197.astype('float64'), relay.reshape(var_2235.astype('float64'), relay.shape_of(call_2197))) # shape=(6, 9, 3)
output = relay.Tuple([call_2205,uop_2226,bop_2236,])
output2 = relay.Tuple([call_2207,uop_2226,bop_2239,])
func_2242 = relay.Function([var_2206,var_2235,], output)
mod['func_2242'] = func_2242
mod = relay.transform.InferType()(mod)
var_2243 = relay.var("var_2243", dtype = "float64", shape = (1890,))#candidate|2243|(1890,)|var|float64
var_2244 = relay.var("var_2244", dtype = "float64", shape = (6, 9, 3))#candidate|2244|(6, 9, 3)|var|float64
output = func_2242(var_2243,var_2244,)
func_2245 = relay.Function([var_2243,var_2244,], output)
mutated_mod['func_2245'] = func_2245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2172_call = mutated_mod.get_global_var('func_2172')
call_2278 = func_2171_call()
call_2279 = func_2171_call()
output = call_2278
output2 = call_2279
func_2281 = relay.Function([], output)
mod['func_2281'] = func_2281
mod = relay.transform.InferType()(mod)
mutated_mod['func_2281'] = func_2281
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mutated_mod.get_global_var('func_2281')
call_2282 = func_2281_call()
output = call_2282
func_2283 = relay.Function([], output)
mutated_mod['func_2283'] = func_2283
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2172_call = mutated_mod.get_global_var('func_2172')
call_2298 = func_2171_call()
call_2299 = func_2171_call()
func_1641_call = mod.get_global_var('func_1641')
func_1646_call = mutated_mod.get_global_var('func_1646')
var_2307 = relay.var("var_2307", dtype = "float64", shape = (13, 10))#candidate|2307|(13, 10)|var|float64
var_2308 = relay.var("var_2308", dtype = "float32", shape = (200, 4))#candidate|2308|(200, 4)|var|float32
var_2309 = relay.var("var_2309", dtype = "float32", shape = (1, 21))#candidate|2309|(1, 21)|var|float32
call_2306 = relay.TupleGetItem(func_1641_call(relay.reshape(var_2307.astype('float64'), [13, 1, 10]), relay.reshape(var_2307.astype('float64'), [13, 1, 10]), relay.reshape(var_2308.astype('float32'), [800, 1]), relay.reshape(var_2309.astype('float32'), [21,]), ), 2)
call_2310 = relay.TupleGetItem(func_1646_call(relay.reshape(var_2307.astype('float64'), [13, 1, 10]), relay.reshape(var_2307.astype('float64'), [13, 1, 10]), relay.reshape(var_2308.astype('float32'), [800, 1]), relay.reshape(var_2309.astype('float32'), [21,]), ), 2)
output = relay.Tuple([call_2298,call_2306,var_2307,var_2308,var_2309,])
output2 = relay.Tuple([call_2299,call_2310,var_2307,var_2308,var_2309,])
func_2322 = relay.Function([var_2307,var_2308,var_2309,], output)
mod['func_2322'] = func_2322
mod = relay.transform.InferType()(mod)
mutated_mod['func_2322'] = func_2322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2322_call = mutated_mod.get_global_var('func_2322')
var_2324 = relay.var("var_2324", dtype = "float64", shape = (13, 10))#candidate|2324|(13, 10)|var|float64
var_2325 = relay.var("var_2325", dtype = "float32", shape = (200, 4))#candidate|2325|(200, 4)|var|float32
var_2326 = relay.var("var_2326", dtype = "float32", shape = (1, 21))#candidate|2326|(1, 21)|var|float32
call_2323 = func_2322_call(var_2324,var_2325,var_2326,)
output = call_2323
func_2327 = relay.Function([var_2324,var_2325,var_2326,], output)
mutated_mod['func_2327'] = func_2327
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_2356 = relay.TupleGetItem(func_2089_call(), 0)
call_2357 = relay.TupleGetItem(func_2091_call(), 0)
const_2366 = relay.const([[[-6.488535,5.339362,-3.784556],[3.905427,-1.883979,7.796835],[-2.534788,-0.429197,-8.990923],[-7.497370,-4.731453,-1.921744],[-3.291404,-1.926120,1.031056],[-9.330560,5.315235,-4.301425],[5.685619,-7.234300,-4.146090],[6.820461,9.024309,-2.835856],[8.024449,8.273052,-1.948520]],[[-4.791356,2.412196,-0.577290],[-9.814277,-1.494158,0.323659],[-0.134251,7.464857,-9.105714],[-1.112926,-5.308073,9.035456],[9.684865,8.608377,2.946404],[-9.042525,9.046519,-5.838164],[8.833518,-9.948194,-9.243503],[-0.709847,-2.608294,-4.519465],[4.001364,5.511812,-3.891490]],[[-5.714854,7.688938,3.255462],[1.393164,-0.759347,4.340193],[2.130244,9.342271,7.989307],[9.676430,-0.727428,4.789725],[-4.503022,-8.775447,-7.199376],[-4.292217,-8.654216,-2.997964],[-6.696160,-0.686590,-8.220992],[-4.258616,-5.826624,-7.091312],[9.663028,0.332618,9.941611]],[[-7.535340,3.331282,5.623995],[-8.183928,-2.482216,9.078674],[-0.235772,9.229356,-8.897736],[-2.632181,7.309496,9.054513],[-8.780837,6.131698,-7.129593],[-6.088453,-3.549798,4.117124],[0.655220,2.663712,7.468035],[0.166338,0.615490,-9.093581],[-3.746725,-7.475322,1.705899]],[[1.806164,-4.239922,9.422688],[-3.751806,-8.270534,1.596913],[-4.590573,1.534440,-5.605734],[0.453736,-0.556301,-6.902927],[-5.393406,3.015496,-5.978501],[-6.448586,7.443569,-8.397409],[-8.068786,-3.905795,4.635895],[-9.574472,4.060881,-1.311304],[-7.959481,3.375024,-4.405593]],[[6.409827,-2.803870,8.016655],[6.012534,4.537408,-5.587822],[6.597241,-1.944738,1.305374],[6.231268,3.039649,0.560460],[3.670395,9.785438,-2.007432],[-9.845689,4.815381,8.072737],[-9.365346,-3.403406,2.296426],[6.020657,4.631953,-5.251333],[-1.561618,9.890260,-8.813647]]], dtype = "float64")#candidate|2366|(6, 9, 3)|const|float64
bop_2367 = relay.minimum(call_2356.astype('int32'), relay.reshape(const_2366.astype('int32'), relay.shape_of(call_2356))) # shape=(6, 9, 3)
bop_2370 = relay.minimum(call_2357.astype('int32'), relay.reshape(const_2366.astype('int32'), relay.shape_of(call_2357))) # shape=(6, 9, 3)
bop_2374 = relay.bitwise_and(const_2366.astype('uint16'), relay.reshape(call_2356.astype('uint16'), relay.shape_of(const_2366))) # shape=(6, 9, 3)
bop_2377 = relay.bitwise_and(const_2366.astype('uint16'), relay.reshape(call_2357.astype('uint16'), relay.shape_of(const_2366))) # shape=(6, 9, 3)
func_1931_call = mod.get_global_var('func_1931')
func_1934_call = mutated_mod.get_global_var('func_1934')
var_2379 = relay.var("var_2379", dtype = "int64", shape = (240,))#candidate|2379|(240,)|var|int64
call_2378 = relay.TupleGetItem(func_1931_call(relay.reshape(var_2379.astype('int64'), [6, 8, 5])), 0)
call_2380 = relay.TupleGetItem(func_1934_call(relay.reshape(var_2379.astype('int64'), [6, 8, 5])), 0)
func_1641_call = mod.get_global_var('func_1641')
func_1646_call = mutated_mod.get_global_var('func_1646')
const_2383 = relay.const([-4.123928,-2.015166,-0.927717,4.750256,3.377968,-1.197042,-6.068638,-0.854322,6.507498,1.051909,6.053572,8.024765,4.237375,-5.797903,9.259903,-9.371921,9.619970,9.317133,1.077077,1.003843,-1.386636,-4.921504,-5.361292,6.959147,-8.552011,7.703275,-2.034752,1.896059,-3.112000,-7.218447,3.775854,-1.601765,3.377683,8.247886,-3.052342,-6.820928,-7.231340,7.483425,9.443581,-1.266912,0.449452,-4.629288,-0.873224,6.354050,9.476283,-4.731630,3.416719,9.361428,-2.378745,8.578023,8.209967,-7.105143,-6.152510,8.220325,-9.629910,-7.458697,4.865695,1.162604,-0.367061,-2.852330,8.945715,4.597612,6.621700,5.495998,7.184211,-5.864580,-1.591251,-2.896233,-3.935133,3.240070,5.779183,-9.020104,-9.091449,-7.627096,9.363458,-2.639450,4.779874,0.866741,5.512374,7.659415,0.070066,8.936631,-4.184477,3.245856,5.426900,6.592774,-9.837761,6.373939,4.622112,4.448531,8.632513,3.168883,6.491997,3.476705,-8.197597,6.851757,8.322655,0.750817,-1.267153,-3.263752,4.965691,-4.283657,-5.493474,-3.447001,5.201364,-6.719599,-5.110400,-0.252187,-5.877645,-5.479220,-2.611905,-3.672145,-4.503397,7.709350,-4.415402,2.073534,9.841828,2.192803,2.715935,3.481950,-4.331590,4.977700,-1.847611,-2.991513,-3.543565,0.001479,4.006031,-9.245226,0.389089,-8.035864], dtype = "float64")#candidate|2383|(130,)|const|float64
var_2384 = relay.var("var_2384", dtype = "float32", shape = (8, 100))#candidate|2384|(8, 100)|var|float32
const_2385 = relay.const([5.528085,-1.112857,0.945913,-1.130521,3.425155,-4.054547,-9.570946,1.196366,-2.079526,6.877676,9.302052,-2.874663,-4.632491,7.577304,3.320740,6.974359,-8.081768,-4.072559,-7.095355,5.899257,-2.420316], dtype = "float32")#candidate|2385|(21,)|const|float32
call_2382 = relay.TupleGetItem(func_1641_call(relay.reshape(const_2383.astype('float64'), [13, 1, 10]), relay.reshape(const_2383.astype('float64'), [13, 1, 10]), relay.reshape(var_2384.astype('float32'), [800, 1]), relay.reshape(const_2385.astype('float32'), [21,]), ), 3)
call_2386 = relay.TupleGetItem(func_1646_call(relay.reshape(const_2383.astype('float64'), [13, 1, 10]), relay.reshape(const_2383.astype('float64'), [13, 1, 10]), relay.reshape(var_2384.astype('float32'), [800, 1]), relay.reshape(const_2385.astype('float32'), [21,]), ), 3)
const_2402 = relay.const([[-1.053122,0.599053,-6.047875,0.554457,5.839491,5.238866,-7.625087,-7.771576,5.063463,1.926785,-9.361647,-5.948623,-1.373210,-7.157062,9.389837,9.237037,0.361670,-7.038188,1.339644,-3.323252,4.732305,6.736571,-9.004821,-7.193625,6.086671,9.844041,4.863576,2.609991,-9.943613,-3.361155,8.312410,-0.428052,-7.852402,5.087651,-4.570811,6.528738,8.521270,2.882106,-0.572188,5.326777,3.071117,0.244380,-6.183448,1.461487,-6.767513,-3.965348,7.227626,-6.401850,-2.403232,-1.668537,1.818353,-4.550571,-1.966372,8.471288,5.579383,-5.382770,2.207186,9.009499,-3.844399,-0.621277,-8.613635,4.273961,3.746246,-9.083573,6.587905,7.057249,-0.912483,0.086217,4.287255,6.659535,0.173091,-7.996795,9.426399,-8.376392,-4.098612,-8.214892,3.290008,-4.959498,-9.954978,-0.788715,5.733914,-4.599145,0.735857,3.482519,-9.472841,-2.344896,-4.703672,-7.727428,-3.199602,-0.278505,-5.783541,-1.268380,-8.098541,-1.968317,6.888172,-0.344003,-3.775455,-7.662227,-5.594059,6.291054],[-7.677760,-3.934158,-4.143360,-7.366998,2.408162,8.980104,6.263760,7.243101,-5.873361,-7.549262,7.916253,1.340140,-0.012463,8.143922,2.319911,7.360392,-5.108276,-1.423113,4.238966,-2.782454,2.191580,-6.618356,0.594916,-4.221041,5.142812,2.705173,8.896882,6.884894,-4.636640,-9.013462,9.422012,4.492950,4.221902,-6.063389,-8.903903,2.021813,-0.997893,-1.955878,-2.786781,1.581116,-1.320713,-6.563061,7.822587,6.077692,-7.686411,9.211279,9.213565,-8.013038,3.910077,7.261692,3.444141,5.846725,-5.533738,2.392964,9.474292,3.549653,0.854947,6.097746,7.528348,-8.157780,6.696504,4.877415,-2.535158,6.699703,-7.957848,0.742381,-3.452953,1.845023,-5.524482,8.496694,8.917978,4.923243,-6.211752,-1.919107,8.983687,6.379821,-4.799778,-6.885308,-0.019741,-1.782502,-6.726715,-3.074692,4.689592,-6.713606,-8.722062,8.845876,-3.869454,-9.318474,7.025827,-6.744296,5.592096,3.719179,-7.536980,-5.414990,-3.766015,5.517922,-9.898015,4.517282,5.391054,-4.066430],[6.366493,7.783783,-2.289357,-8.781926,-1.147268,9.877298,-8.454995,-5.357670,-7.142773,-8.006353,1.136862,0.857166,9.379724,2.474992,-8.254402,7.517257,1.412392,6.956078,-6.747391,-3.025581,-7.679197,1.198733,-4.403687,7.078961,-6.877628,6.869951,7.994189,-1.441335,5.360546,9.194114,8.493610,0.779511,-7.766460,-9.194345,-7.496184,5.523479,-9.805310,-6.790598,-9.416749,8.277224,9.690784,6.785436,-8.132276,1.871514,6.650429,0.624760,2.062336,-4.366046,-1.570537,8.989216,9.323729,9.473330,5.688291,-5.702114,-9.752231,-2.272992,5.130931,-7.537854,3.953289,8.514831,9.138356,3.066969,-0.078634,-4.531153,7.379764,2.161158,-3.776594,-8.975588,-2.224392,-9.957707,7.668359,-2.274651,-8.940133,-7.117945,5.148872,-1.476538,-4.271144,1.790784,3.045533,1.266871,1.905657,9.538556,-2.536908,3.439201,0.039065,5.832231,6.343852,0.979190,-2.162323,3.703825,1.646067,-1.518094,-7.689096,-1.534234,4.086108,-4.516918,9.849401,0.150634,6.640878,-7.822234],[-9.026114,7.732845,-7.683597,7.587525,-9.353717,-3.936366,-9.676715,-6.552708,-6.007946,0.047973,-3.076300,9.910618,7.490434,4.046871,2.600178,0.752939,8.362157,0.180320,3.171792,5.349834,-4.950333,-3.710647,-4.287034,8.186850,9.638609,2.611482,-1.199717,9.518964,7.502205,-9.122942,2.190475,-8.843743,3.655096,-2.242653,-5.063457,-2.303122,3.672546,2.433829,1.142447,-8.916388,2.754932,5.192325,-1.649401,-9.582524,3.421109,2.330295,-3.248640,-4.835942,2.783129,5.831077,-9.573910,-5.272485,-1.502255,5.926445,-0.486412,-9.090804,6.873791,1.402225,8.610929,6.712234,9.399602,3.490530,-2.223671,9.649848,-9.495792,6.213202,-4.924586,-0.165977,-4.494698,2.304704,9.099834,-3.223262,1.984759,0.164258,0.731349,1.905616,3.135446,2.349547,-2.174203,1.460248,0.912620,2.651101,9.711146,-4.823315,-2.801930,-5.688487,8.107725,-4.947035,0.758442,7.938290,6.811794,0.081122,4.283182,-3.775493,1.746363,-7.231442,4.662797,-3.362669,9.218888,-1.609458],[-5.733380,-9.927807,2.125372,-6.838806,-2.854433,-0.227306,9.755259,-6.152425,-7.993969,-3.636744,-1.086577,-7.363483,5.570245,-0.439048,3.802080,-3.695441,-0.453951,5.685915,7.513240,-0.282243,-1.886313,3.147447,-7.854591,-9.368996,3.211498,-5.867682,-3.390510,5.703015,8.181574,-9.526757,-3.324958,2.692490,0.622215,-9.695301,-4.731986,-9.287367,7.885833,-5.524662,3.749174,-8.828396,-2.653404,0.911769,4.683603,-2.308384,-9.969908,6.952339,5.467931,0.231469,-0.522956,3.339102,-3.368151,6.257049,-5.044614,2.154400,-9.815109,-8.053316,-2.064471,4.486426,-4.533102,3.622235,0.275553,3.579137,6.344091,1.590538,-7.056316,-9.813322,2.867783,2.043360,-1.915062,5.940157,-3.424121,8.950908,3.509392,3.559192,-0.811615,0.228529,3.019240,-4.544165,8.581924,-5.940717,-9.051627,2.232626,-8.813325,2.312426,6.464127,-8.813252,-7.722609,0.581056,-7.202667,2.495558,8.260652,-5.177113,3.292310,3.882119,3.783990,6.176298,-3.328069,9.169940,9.216944,3.773896],[8.931936,-9.527027,5.278899,-8.672120,-9.944477,-8.714374,-1.119864,1.550560,6.238824,-4.213490,-3.612901,6.009120,-4.771804,-7.745993,4.218870,0.549826,2.252602,5.235357,1.236883,-2.876443,8.952777,9.755324,-3.892307,-0.962708,3.919598,-5.151151,-8.091579,-2.590026,-4.313732,-3.730067,0.096321,-1.231162,5.747659,9.393962,5.656149,3.014590,8.436353,-1.273669,2.331756,6.853551,-1.670044,-9.159935,7.449087,4.035961,2.282871,-6.735206,7.142266,9.725808,-9.031202,5.770542,3.470237,-3.956764,6.372322,-4.678336,3.708295,3.566530,1.480929,-7.144414,5.675354,-6.924468,2.650171,9.904156,4.688380,-2.082775,6.458780,-6.963293,-3.058716,3.734417,8.855485,-6.491828,-1.445096,-5.570574,1.702184,-3.900391,7.892764,-4.024687,1.760565,8.970716,-7.036270,-2.108469,-5.826334,-5.371784,-8.771212,-1.174627,5.391661,-5.240549,5.400819,8.027946,-3.311660,5.206150,-4.961841,-2.078625,9.203555,0.138130,6.820258,2.545119,-9.879527,-3.961364,-3.898593,-5.109357],[1.250294,1.536381,-5.074941,-9.670285,-4.275543,-4.823981,9.531162,4.054398,-7.463311,-7.948549,-9.616608,3.084501,-7.870223,7.171194,8.445324,-6.787123,1.585065,0.870133,6.728267,-4.449931,0.965594,-8.995008,7.574089,7.934937,-1.187078,-9.873614,1.622541,7.105285,8.724680,-5.916678,3.111503,-5.938454,-2.060103,-5.322622,6.585363,-4.631053,1.824980,2.145442,-3.534826,-8.556261,-3.263735,7.304877,6.014471,9.105701,-5.299269,5.334416,1.751836,-8.208125,6.170988,7.545247,9.005655,6.780539,-3.633326,6.811557,7.464850,-9.753870,-1.109635,4.647406,-7.483391,8.549031,7.724892,-5.784803,-9.342506,-2.563154,0.304332,-0.719557,2.816845,5.258436,-0.208414,-4.674057,5.129209,7.507635,4.079250,1.913580,-5.432907,-6.470824,9.804299,-2.426688,4.047834,4.129168,-3.471370,3.742188,7.854281,8.951042,1.269742,0.812274,-8.268247,7.455977,4.413682,-1.578798,1.963474,5.913147,0.192746,-9.330311,2.843491,-2.130375,8.598651,7.450204,-2.735488,-1.817544],[2.077765,-0.767421,-5.976620,4.027409,-9.530699,8.332173,-3.945126,-0.862685,-8.431242,-0.722658,-1.967472,5.612186,-0.503205,-2.674245,-9.507788,-7.453504,-2.783006,5.444223,-6.213430,3.532863,-8.122996,-8.264846,8.209792,0.315555,1.907324,3.030283,-6.543282,5.474571,-4.424888,1.055980,-1.050067,-4.241774,2.776102,-8.192013,-4.863212,-5.376352,-2.665565,0.154523,-4.908048,-1.648057,-9.244391,4.526849,-7.026202,2.497745,3.718900,5.499492,-8.490844,-9.653310,-6.925723,-3.380555,-4.464563,2.702016,6.297977,8.951757,0.172252,-2.323950,8.868390,-0.136007,-3.972637,-3.784302,6.672876,-7.965273,4.580775,8.560620,9.790213,-7.977351,-1.260707,-2.430311,-0.904513,1.450433,3.916748,3.956237,-4.892653,8.616247,4.056335,-1.208952,1.012484,0.314242,0.850456,-1.506711,-1.471756,3.695290,0.463030,-9.859017,9.518182,2.815811,6.104269,0.533344,7.153509,6.024286,3.892080,8.305168,-8.228537,4.846181,7.833324,-6.749118,9.298136,-6.493661,8.116810,-1.962182]], dtype = "float32")#candidate|2402|(8, 100)|const|float32
bop_2403 = relay.less(var_2384.astype('bool'), relay.reshape(const_2402.astype('bool'), relay.shape_of(var_2384))) # shape=(8, 100)
output = relay.Tuple([bop_2367,bop_2374,call_2378,var_2379,call_2382,const_2383,const_2385,bop_2403,])
output2 = relay.Tuple([bop_2370,bop_2377,call_2380,var_2379,call_2386,const_2383,const_2385,bop_2403,])
func_2426 = relay.Function([var_2379,var_2384,], output)
mod['func_2426'] = func_2426
mod = relay.transform.InferType()(mod)
mutated_mod['func_2426'] = func_2426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2426_call = mutated_mod.get_global_var('func_2426')
var_2428 = relay.var("var_2428", dtype = "int64", shape = (240,))#candidate|2428|(240,)|var|int64
var_2429 = relay.var("var_2429", dtype = "float32", shape = (8, 100))#candidate|2429|(8, 100)|var|float32
call_2427 = func_2426_call(var_2428,var_2429,)
output = call_2427
func_2430 = relay.Function([var_2428,var_2429,], output)
mutated_mod['func_2430'] = func_2430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2456 = relay.TupleGetItem(func_2017_call(), 0)
call_2457 = relay.TupleGetItem(func_2019_call(), 0)
func_122_call = mod.get_global_var('func_122')
func_124_call = mutated_mod.get_global_var('func_124')
var_2461 = relay.var("var_2461", dtype = "float32", shape = (144,))#candidate|2461|(144,)|var|float32
call_2460 = func_122_call(relay.reshape(var_2461.astype('float32'), [4, 6, 6]))
call_2462 = func_122_call(relay.reshape(var_2461.astype('float32'), [4, 6, 6]))
func_1213_call = mod.get_global_var('func_1213')
func_1216_call = mutated_mod.get_global_var('func_1216')
const_2480 = relay.const([[-1.822445,0.218633,3.137650,-4.005987,-3.725316,-1.018962,-8.332017,9.111603,3.158254,8.858183,6.208103,-9.789708,1.845105,-7.392363,2.362684,-2.682714,6.965391,-1.213482,1.270203,6.718848,-8.384401]], dtype = "float32")#candidate|2480|(1, 21)|const|float32
const_2481 = relay.const([[2.309690,3.508355,1.923813,-1.021462,2.053745,-0.900954,-1.081512,-0.570343,-7.047957,-9.780655,-2.407515,9.708344,8.313879,2.532528,3.109573,2.453984,6.789965,3.946489,-8.636667,1.411464,-8.792210,0.554433,3.130065,-0.483873,-2.022728,0.562285,0.457530,-0.920419,4.638803,-1.027777,1.298227,4.272938,-8.009052,7.943242,-4.938324,-4.624585],[-7.213857,5.451442,4.712736,0.458596,-8.988191,-1.097314,0.314085,-3.007463,5.936915,8.576396,-6.080320,1.934631,-1.121229,2.519266,-3.032140,0.647927,5.430488,-9.719201,9.754463,1.163301,-6.810558,7.510339,-5.635233,-9.511678,-5.601121,-1.296448,-5.371390,0.935560,-8.858560,2.720817,-4.140366,6.485068,0.755018,-7.611616,6.536934,-0.231235],[-4.609794,0.335263,4.706860,-8.395161,4.152569,-9.669710,-6.525117,-1.269173,-6.886630,4.483069,8.725054,3.167224,-5.210108,2.268573,3.383491,5.210237,5.562041,-8.692922,-8.267433,-0.944052,7.886316,6.103834,-3.461577,-5.451724,2.350684,7.242620,-2.808061,6.988751,-8.285914,-5.100098,-5.145232,7.934536,-0.744969,-6.977331,-0.696593,-4.198202],[4.823618,-6.149475,-9.643072,1.178232,-0.884714,-1.501241,4.389465,-8.801886,-4.454179,5.157001,-5.001537,-4.303668,-4.683350,-9.393223,1.925662,-9.164040,-7.343489,-7.738469,8.204583,5.130850,-5.637714,-7.694694,1.178856,6.248039,1.162743,2.691785,-6.222162,-0.032416,-0.578077,0.351710,8.053000,0.680801,-5.370090,-9.477495,0.964862,-6.706878],[8.519878,1.801599,7.403952,-5.275686,1.563316,-8.868445,8.801742,-6.066594,3.611641,2.045758,2.955771,3.611065,-4.121200,0.824536,2.283311,9.068631,-0.455691,4.132490,-2.943178,-2.321428,6.719461,0.885178,1.092967,4.936951,5.959598,2.701557,3.745796,0.618601,3.149997,7.713093,-6.323580,0.211133,1.014399,-9.007949,3.997460,1.112423],[0.536775,5.295375,-9.587163,-9.940490,-4.485718,-8.587762,-7.150595,6.572245,-6.463522,-3.584634,-3.265454,2.859034,-8.741632,4.898512,-4.485667,2.273928,3.171492,-8.668951,9.037428,2.247747,-9.999454,8.998573,7.351986,-4.466011,4.995414,-9.327272,9.872079,1.397285,9.399480,6.065458,4.146742,-2.270781,6.303953,-3.623026,1.786952,-0.526504],[8.825755,-5.261711,0.677033,-9.330972,8.039226,-1.565786,-3.300663,-4.907576,-9.348553,8.352279,-7.417993,-4.344252,-9.618090,-1.295709,-3.726179,7.927675,-1.087537,7.227715,3.097550,-4.642812,-6.049807,9.268794,-7.507320,8.138354,2.901673,-7.278615,-5.703292,1.473119,4.495534,-0.414517,6.374042,9.986261,3.345043,0.231037,-2.014867,1.303523],[-9.698349,0.489230,-7.001245,5.319942,0.688512,-9.736193,-8.006747,-9.828439,0.557309,9.579927,8.187205,3.252415,3.245447,2.863498,-9.539639,4.566382,9.994473,-8.479389,0.785139,8.560764,9.857018,-4.391004,4.597093,-7.510514,3.083249,5.266283,-6.798529,2.669456,6.253163,-0.546577,3.958967,-9.656077,-6.703784,-7.398224,-4.283062,4.328415]], dtype = "float32")#candidate|2481|(8, 36)|const|float32
call_2479 = relay.TupleGetItem(func_1213_call(relay.reshape(const_2480.astype('float32'), [1, 3, 7]), relay.reshape(const_2481.astype('float32'), [8, 36]), ), 3)
call_2482 = relay.TupleGetItem(func_1216_call(relay.reshape(const_2480.astype('float32'), [1, 3, 7]), relay.reshape(const_2481.astype('float32'), [8, 36]), ), 3)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_2486 = func_2281_call()
call_2487 = func_2281_call()
func_2075_call = mod.get_global_var('func_2075')
func_2078_call = mutated_mod.get_global_var('func_2078')
const_2489 = relay.const([6.726271,5.387791,5.322454,2.299883,-0.075824,-8.071265,6.820470,7.058237,-5.575281,4.532918,8.447357,-3.547304,2.406532,3.825193,6.152936,-0.047383,-4.083627,8.962924,5.343304,-0.515081,-5.269708,-6.850469,1.178884,-0.129034,1.403109,7.117020,6.171779,8.275768,9.941958,1.401602,-9.756299,-3.756588,-0.969888,0.597051,-1.108272,3.282939,-1.660457,8.552174,8.228803,1.839338,7.782397,0.776375,-9.447134,3.685926,-0.927362,8.508072,3.545479,0.306696,8.981478,1.903408,-2.207578,-3.509227,-7.201502,6.877924,2.933929,1.269832,4.425618,-8.907048,2.739725,3.773438,-9.109974,6.754364,-7.814967,7.701327,1.064120,-0.934686,7.010955,-8.805493,-0.054277,-4.673696,6.167429,-5.131584,-4.836825,-6.247334,-1.180616,1.917729,-4.610706,-7.613409,-3.249263,-1.667589,9.538829,8.764528,-5.844417,-1.321887,4.111717,-6.412403,-1.155473,4.982972,8.085526,2.599847,-0.230675,7.831354,8.229034,7.896896,0.221164,9.945457,-8.499843,-8.238059,-0.663605,1.327620,1.202158,-3.544586,-3.930115,-1.216804,-7.705948,-5.779260,9.699434,3.578293,8.827186,-6.434238,5.682690,7.394484,-4.172719,-5.659316,8.211852,8.953100,5.111332,-3.128305,4.478027,-2.793256,-5.852648,-3.725538,-1.653684,-2.677230,8.186772,-4.160146,-4.404634,-8.670137,9.369282,-5.155124,8.339080,2.140486,1.905745,-3.240477,0.484117,-9.686629,6.583875,4.718844,1.548866,-8.665304,-2.619421,3.900582,-4.062151,9.727793,-5.350574,-5.608225,7.170936,-1.946576,-5.262887,-8.809058,8.301773,9.300915,9.433320,-0.329726,7.121583,4.551263,-0.061088,-0.418032,7.254559,-0.655754,0.036379,6.196655,1.965990,-6.062621,-0.544723,0.526100,0.829530,0.365150,4.228225,7.696637,-8.645399,-6.838969,4.653341,0.415160,-1.909120,-2.030897,9.951840,0.194419,-4.408736,-9.544300,-2.685338,-9.784962,-9.192247,-6.478615,-1.918716,-1.271510,2.889637,3.567347,-2.164445,9.372872,-5.882787,-0.505782,8.656051,-1.967871,1.830308,-9.365463,-5.194632,-5.830885,-3.607918,-4.233067,-1.940766,9.597259,9.456688,6.055323,-4.704099,5.115165,-5.770737,-3.953594,4.973321,1.847340,5.776423,-8.411992,8.098847,-7.138369,4.787955,-8.178738,-2.318613,1.005735,-7.048922,5.694503,0.957070,0.557177,-4.911782,4.882870,4.838049,2.729154,0.668847,-0.405059,-4.226018,-9.891296,-6.686504,7.040667,0.209136,-3.796577,8.832230,-0.041202,-9.486842,7.769656,1.158828,-2.576645,3.447434,1.780669,0.517496,1.886331,-9.621601,-5.614838,-9.945168,1.456675,-7.954605,7.434509,8.833306,8.891167,-7.278913,2.051979,9.884591,-3.164213,6.405168,5.964809,4.636329,-5.657118,2.923282,-2.630072,-8.128962,7.828569,-2.370196,6.599844,-3.023803,6.953237,1.627090,-4.574535,2.414092,0.188501,-6.098351,6.522969,-5.369413,5.940953,-8.466128,3.569115,-2.622713,-8.244332,-9.845990,-0.420798,-5.088188,2.374987,-5.295432,-7.863290,-6.102959,-9.167966,5.716248,-0.877485,5.918328,5.506501,-6.003307,6.048529,9.447208,8.123178,6.060126,-2.434783,3.833206,9.487153,4.460987,6.606159,6.272092,-6.809302,-6.320455,-8.395347,-2.688067,8.651797,5.857340,9.318521,-7.854275,-4.715288,4.153815,0.404307,-3.866206,-0.129651,0.904489,5.937438,-0.866616,8.323148,-9.319613,-1.744737,5.744400,4.944006,-2.570280,1.496209,7.972172,-1.667629,-5.933484,-8.630273,-6.669851,-3.294989,-4.367015,6.672132,3.724214,7.103961,-0.287828,-1.394651,-3.445551,-1.827901,5.441930,8.684687,6.735330,3.274544,-4.287402,-6.444880,-2.700507,-5.597085,-0.436996,3.529199,-6.462466,-9.427874,6.450236,-6.900454,-3.784750,-9.052751,-3.922310,0.531695,-6.771432,4.940468,-8.692147,9.882619,-3.015610,1.080942,6.786811,-8.590502,-0.397398,3.997233,8.087998,0.311765,-2.796887,6.556208,3.774646,4.316718,2.318297,-5.757429,-0.851148,6.937231,7.638809,-6.493512,7.260060,-9.714548,9.706980,0.111208,7.835128,-8.836073,4.899990,-2.152413,-6.019102,-7.931721,-9.688734,9.013158,-5.899312,0.227917,-1.027780,1.486010,-7.509737,9.336397,2.889623,2.378822,0.451240,-4.986748,7.038082,6.380675,-6.550107,-2.237285,8.083148,-8.615448,-1.473581,9.364624,1.851446,-0.766277,2.882213,0.780077,6.991344,5.181620,-6.837814,8.443211,8.717307,-6.182678,-0.336775,-0.766587,-4.845978,9.662278,5.981086,3.797342,0.026924,-8.398802,7.652638,4.215085,-0.802682,5.675972,5.165807,8.969465,-9.172722,-8.524222,-8.154322,-4.030968,0.571032,2.699264,-6.999778,7.697913,-2.983272,-9.285975,6.001388,-8.884639,3.425739,4.664147,-0.487475,7.774237,-5.006205,7.212499,-5.134780,8.394384,-5.138716,-0.406779,-6.090191,-5.232656,-0.799279,-1.641199,0.468472,7.505072,9.924831,1.641933,6.159864,-8.532090,-8.991725,-1.098594,1.073170,3.124930,-2.419707,-4.147736,7.204694,-3.203643,-7.488264,-8.985568,7.517080,-2.509842,-0.067001,8.628023,-8.428182,2.057792,4.914962,6.891990,6.441875,-4.068202,9.203356,-0.734122,-0.309852,-1.410371,-5.768248,-5.602819,-1.469652,-9.232879,-6.840994,8.144223,9.040853,2.788122,-3.470807,0.238538,8.182246,-7.177027,-9.272146,-1.410344,6.805064,9.803226,4.780245,2.483370,-8.630318,-2.603573,4.866911,4.335715,-7.215797,-8.602981,-3.614036,-9.771603,9.904619,-6.298405,-9.394556,-6.370491,7.889555,0.332178,5.180801,-7.796120,-1.653420,-7.931468,-0.478344,-1.677651,1.392717,-2.131726,-9.498403,9.049152,5.232188,3.816235,-4.325422,0.068130,-7.707174,-0.359103,7.099732,3.408432,6.611280,-1.000271,-1.112785,-4.149002,9.837595,9.277475,-2.201009,5.671580,-4.669781,0.902423,1.108273,-0.782555,0.297288,4.574184,6.571801,-0.403395,0.679438,8.159575,0.358657,4.509059,-1.676025,-6.238956,1.392547,-5.113043,-7.418155,4.656448,-3.624110,1.284395,-6.122306,-9.203770,-0.982193,7.387754,6.188316,6.008936,-7.192642,3.500810,2.656556,6.836504,-3.515439,-2.961364,0.165689,-9.301180,6.693136,1.267502,-9.422189,8.574554,-1.553204,-2.251565,5.824481,-4.563169,-2.548430,-6.783937,7.405758,4.958426,4.785077,7.932917,0.534807,-4.639658,5.571455,-2.682547,-1.735038,-0.679937,-9.120386,-5.813925,-5.165441,-2.901246,3.323278,-9.331990,-8.503883,-8.162059,6.974507,3.631450,1.517634,6.765414,9.880301,-4.593396,-8.791262,6.685560,-3.415816,-1.500922,-7.879824,6.055866,-7.076972,4.503715,1.628248,-5.655130,9.883725,1.645657,-9.994128,8.536838,3.097502,8.192730,6.736451,-3.447873,-9.705971,-3.686188,9.554112,-2.865152,-5.206131,7.023332,3.816273,-8.754453,7.218562,7.144004,4.848622,2.688932,7.322680,-5.173385,0.118079,-9.207320,0.418953,8.027370,-7.838937,-9.329539,6.531721,8.131270,-2.578369,1.591126,6.233006,1.813614,2.949009,2.815023,4.005505,2.818778,0.733700,-7.516800,2.559250,9.879463,-5.812551,-2.333622,9.544285,-7.499901,3.924204,4.764733,2.178175,8.914713,-3.609522,4.727510,-8.824860,-6.378296,-4.047273,5.037308,-1.667546,1.071823,-6.965539,-1.948498,0.784673,8.292771,-1.911249,-8.867455,6.243940,1.035548,-9.661822,3.319484,1.766083,-5.733384,6.844134,7.833829,0.597434,-2.946946,-4.733912,4.243934,9.902481,7.317413,-1.692631,4.408247,6.243568,8.724896,0.251361,4.242426,-8.392800,-4.741212,9.403392,-9.219895,7.276090,-7.412323,1.946365,7.864208,2.094055,9.767606,-2.311245,2.402632,6.952949,-2.897721,-1.487333,0.457246,1.262724,-6.969384,-5.495001,6.256285,4.896510,9.496881,-7.302852,3.565417,3.828156,1.494683,-3.398867,-5.259259,1.525340,-7.883977,-0.762532,-2.004828,-8.464556,-7.200850,3.607987,-6.933140,2.192733,-3.617426,-5.165766,6.579067,-4.134494,-2.146375,-6.330892,-5.259320,6.657948,8.162458,-0.014639,9.921544,-6.988804,8.085894,-4.101917,-7.399819,-7.268768,7.979620,-6.523014,-8.363850,7.242304,3.126421,3.331438,4.012012,1.548826,-5.650786,-8.373170,-1.146491,4.798163,4.785035,5.208753,-1.425259,-4.698038,-0.590324,-6.670985,7.289315,5.542204,9.249874,-3.278236,5.337843,9.917505,3.263376,-5.800053,-2.962130,-1.703076,9.672421,9.514095,2.388732,5.149131,6.527283,-2.146429,3.313377,7.763928,5.862843,2.251636,3.759055,-9.442162,-3.309137,-2.192779,3.064394,-5.050036,-5.356812,-6.197844,4.348587,-6.412564,9.141441,8.450562,-5.569076,-3.313636,-4.704392,1.720430,-6.002669,5.630390,-0.873265,-6.595082,-2.222660,-4.935281,-6.559197,-7.762481,-4.952470,-4.290778,9.097017,-9.101578,0.729242,8.807999,-8.816569,0.285822,8.809476,4.660869,2.392270,5.997176,4.441489,-9.051651,-6.692440,7.625684,3.820623,-9.482917,-5.045578,1.228443,0.622508,8.496281,7.186340,8.873450,0.909375,-1.094249,-7.063717,-4.671197,5.792632,6.515885,8.202379,-9.340987,5.779063,-3.214317,7.559692,6.498478,-1.252501,-7.565075,9.413769,-9.261086,-3.855735,8.544627,-1.632657,-8.032000,2.288810,6.219074,4.035489,0.131130,7.977846,-9.254736,6.215764,7.430404,-7.698247,5.341224,0.788174,1.475231,-7.423030,-8.610362,-4.828727,-2.745877,4.164748,1.858374,0.119571,8.158941,-6.556689,3.584112,7.023400,5.876374,-3.739770,9.744878,4.045170,-3.426646,-0.475685,-9.308558,5.394356,-6.346407,5.131354,5.663250,-8.911118,3.253984,-1.591074,3.074272,9.640135,-7.502905,3.659120,-3.683201,-6.616109,7.044734,4.651099,8.652167,-4.220740,2.782132,8.115373,3.880295,6.255163,-6.736756,2.665489,8.871044,0.138883,0.514041,-6.117564,9.663959,-1.952779,7.527899,-8.201121,-4.844429,-4.448350,-8.501195,8.059007,5.415860,-1.963959,-3.285968,3.242172,4.123548,4.497636,-9.399350,-7.478981,-9.401536,-4.081663,-7.088512,4.455508,8.553080,5.496820,0.494175,6.576023,8.506096,7.235318,-1.215680,-6.233524,5.749618,-9.105093,2.864869,2.757012,8.460355,3.474394,-0.831156,-3.202488,-1.234659,-5.375107,-0.768734,-2.654864,3.588175,-3.666020,5.531425,3.533261,-6.125124,-5.453926,-1.442770,-3.989038,0.395503,-9.409096,-2.291165,8.386270,-2.656920,-5.868766,-5.785441,-8.741055,-1.864748,6.106847,3.260107,-8.792199,-0.791484,0.006287,-5.522115,-2.723397,7.044895,-2.098947,8.826910,-7.286064,4.693535,9.284861,-5.230615,6.639134,-6.011452,-8.101000,-6.499745,6.771896,6.354232,0.202831,-6.199457,8.652067,-7.252459,7.547627,2.127435,7.709279,4.060301,-9.114567,6.845490,-0.641018,-8.958843,2.959900,-3.713215,0.689185,-9.848509,1.123186,-9.607241,-9.466103,-7.590601,2.661883,-3.988403,-2.898094,3.143852,0.833343,9.683278,-0.067665,-5.308854,-2.366774,-7.255185,-6.210322,-5.401925,-9.788373,-0.933034,-4.949027,-4.835784,-6.243694,-3.198555,-7.007786,-3.951251,-7.483781,-6.119075,6.062529,5.544139,8.398601,-3.458931,-8.556512,2.081708,9.079405,8.157156,9.754500,1.811324,-0.350330,-5.339463,7.215009,-9.231866,-6.868314,-6.572209,5.533612,7.268343,-0.540701,-7.938611,1.020103,0.187099,3.466128,-2.894813,-3.737685,1.695407,8.406987,-5.755227,-4.036944,3.776895,7.794936,-3.751643,6.298888,6.176858,1.925747,-4.335876,6.395758,-3.510491,-2.102357,3.242328,-0.490746,-1.816158,9.837310,5.498764,9.788405,-6.190305,-8.730109,-8.788984,2.420657,3.017051,5.297571,0.164905,2.184520,-0.344710,-8.683355,3.035688,-2.763385,-1.455161,-5.379305,7.381113,-5.290238,-2.020769,-3.284404,-5.593676,-2.432837,2.804407,0.517078,-8.720735,-0.883447,5.434437,5.237532,8.170780,-1.153041,9.195074,2.829213,-6.075049,-1.527579,4.002875,7.782217,-2.886369,4.818671,-8.605091,-4.566644,-5.839772,3.136577,9.657249,-0.042229,-6.687002,7.924045,3.495786,-8.252073,-2.726725,-7.314615,4.290711,-9.010112,9.037831,6.133716,-1.917248,-1.631734,-8.575412,-9.537814,-3.209445,1.886164,8.765191,-8.853183,6.984976,2.709982,-7.191134,9.893132,1.107092,9.551152,-4.148039,-8.730415,2.088142,6.645266,-8.324970,2.811207,-8.510931,0.534997,4.102386,-7.953858,-9.397257,5.693960,3.929681,2.002239,-0.757769,6.540788,3.763184,3.415526,-1.493176,6.792193,1.567322,-4.198073,8.622691,1.287104,0.681456,2.042978,3.012297,-7.842777,-5.386407,-5.256134,6.811878,7.053203,6.929333,8.927052,9.117443,4.799887,8.733142,-4.437905,3.377320,-9.223156,8.153650,9.050285,-5.636640,4.371007,2.240992,8.498571,3.318556,6.804227,9.614517,-8.540299,8.774394,0.222014,8.937657,4.473885,-0.687657,-3.300630,-2.374142,-8.359209,4.940996,1.536409,1.698173,7.249168,5.020017,-5.160150,4.407524,7.451778,-1.531312,-5.427595,-1.245239,-1.422172,9.377436,-9.674184,-7.587936,-2.851922,-3.596256,-8.480238,-8.483649,-1.602091,8.014560,-7.956784,7.896505,0.277218,5.818533,-2.847060,-7.938430,-8.174867,1.780712,3.254778,7.743281,5.549435,3.884522,-5.293110,-0.277380,1.488267,1.791871,-9.355829,0.943320,-9.252841,2.678821,-1.517948,4.545706,8.521643,9.254529,4.709255,-0.431085,-8.957552,-8.076202,9.125491,3.334501,-7.966729,9.586835,6.313082,3.203569,6.669947,-6.065218,-0.983004,-7.907483,-1.800363,-9.266877,-0.259569,4.811304,-3.724735,1.042960,-4.699727,-2.016211,2.764745,7.150232,-5.455957,-1.134660,-4.757398,5.873880,9.810496,-4.885175,8.887754,2.252050,-3.354701,-9.447914,-4.793448,-0.943980,-9.423557,-2.779079,-5.947336,-9.118998,-3.361913,-8.841810,-1.955619,3.441789,8.986420,4.087071,-0.078337,8.887906,3.976103,4.233671,0.759872,-8.356601,-5.426738,-1.570838,5.366034,9.652726,5.380019,-5.035563,6.877887,9.130085,1.108406,3.092266,2.873635,-8.636819,-8.328121,3.981350,-0.827342,4.417459,-2.274936,4.139295,-3.065427,9.205082,3.971048,1.562082,9.503695,5.772758,-3.312947,-9.025076,7.602310,-7.744240,-4.638256,-1.316036,-7.534631,2.816774,4.321111,-0.203905,3.010910,0.011645,2.860034,1.030395,-2.238157,0.150414,0.948820,-8.283793,8.604634,-8.506741,-1.614910,-2.406097,-8.826292,5.366643,-6.231861,8.795317,4.094214,-9.918022,-5.583770,8.294185,2.023714,8.170608,-4.945999,4.687866,-3.695304,2.850705,-9.561326,8.923936,5.065014,-3.824231,-4.959803,7.615594,6.628796,-9.907149,3.411616,-5.542502,4.721484,6.184069,3.032950,8.767527,-8.539747,8.920961,-0.387326,6.170695,1.762094,9.676099,-8.075108,-4.940729,2.892989,9.821539,-2.026326,9.169835,9.318316,-9.225597,5.730355,-1.355853,-1.854991,4.938206,6.022963,0.030801,-8.222148,-5.416004,1.027832,-5.078120,-1.968677,-5.107597,6.618834,-3.253599,-2.742808,-3.454940,-1.870455,-0.236590,-8.448325,2.032508,-9.948702,-7.158569,8.822872,5.428896,3.958186,2.385108,9.367426,6.067814,1.956331,6.401003,-3.922375,-9.842954,4.677212,9.633013,-6.807854,2.296836,4.407449,7.581330,-4.320170,-6.433805,1.700476,6.359538,8.620186,8.198503,-2.191004,-5.607168,-0.947448,7.554036,5.451083,5.943487,6.610726,5.366929,6.746022,-0.269613,8.434631,7.162675,-1.403252,-2.813324,8.437435,4.450922,-9.349198,-5.301840,-7.516137,-1.294558,4.083005,9.004600,-7.457964,8.012712,4.331261,-1.490545,-1.515131,8.626363,-4.913908,-9.766740,-6.111336,-0.727258,-8.412597,6.718131,-1.063552,-4.318985,-3.201962,3.451316,-1.351316,-5.084495,-4.162068,1.601691,-0.917508,0.446834,-0.342966,1.268834,5.464552,4.655326,-9.778413,-7.917371,1.373339,-2.127345,-7.056157,-8.152627,4.230142,5.506792,1.202473,-2.025944,1.750743,4.016340,-1.126179,-9.910834,-7.865879,5.402331,5.981387,4.435100,-0.434519,-4.397156,8.906151,-7.539745,9.147428,-5.992360,-8.132235,-6.370260,8.899979,0.283155,-0.110507,6.444304,4.290342,-1.906673,5.352058,6.804917,1.723692,-9.532153,7.772877,7.845455,-3.168245,2.276304,6.866733,6.485617,0.237521,-8.321913,-5.333709,-5.575454,-3.513848,-1.311664,2.210518,6.097539,3.165152,1.399327,-2.498857,0.184437,2.583141,8.656820,0.639145,9.920528,3.307736,-2.334565,6.263252,-1.305528,7.907875,4.280878,-3.022620,-1.035963,9.441511,-9.645901,-4.023268,-2.650633,8.407394,-7.904683,-6.972703,4.906246,1.620951,-1.841321,9.830692,-8.159525,7.432246,2.747733,4.647322,-6.737738,4.374561,-0.333083,-3.531096,8.664749,2.920424,-4.070563,6.998489,3.679278,-5.948049,-0.655541,-0.756898,-0.701296,-2.769300,-6.437916,9.623359,-7.147329,0.326473,7.266045,-3.185409,6.357470,-6.534934,0.405518,-0.125165,6.820682,-7.488553,-7.224846,-0.504082,4.945880,-5.437497,-6.443835,-0.632591,-7.809863,-3.219838,4.806114,2.604119,-8.627657,0.585373,4.435618,-4.258829,-6.782353,-7.773816,-6.524538,3.133674,-6.005147,4.344368,-8.354363,4.335018,6.039916,-9.127089,-7.887518,-5.524882,1.520460,3.188093,5.865141,7.766625,-3.770622,-1.198473,7.371047,-0.188677,3.605669,-0.453765,8.260269,-3.172355,4.069251,-1.126589,-7.658294,-6.573465,-5.537502,5.651627,-0.239202,4.403078,-1.600650,9.631897,6.335926,5.634684,5.554861,-4.147659,-5.067931,2.357495,8.398322,6.172815,-7.697989,-1.518693,1.275838,-2.462377,-1.186334,9.196018,9.741587,-6.327664,-8.706358,3.845593,-0.631673,0.422092,6.935248,-4.982208,-8.206289,-2.580413,-3.994026,1.104735,-8.948332,3.830142,8.639390,-1.198317,2.473658,9.748816,-1.940179,4.820730,8.677039,7.762752,5.317551,6.292494,-7.899301,4.099917,-1.294509,-4.020491,-9.497008,-6.239530,-5.110520,9.170610,4.665650,-0.004188,0.614906,-8.824068,-7.194180,8.848657,-1.337863,2.825459,1.933748,0.687099,3.818716,-6.342517,8.489167,5.935524,9.174657,0.993621,9.177703,5.050592,6.230880,6.643672,1.480743,3.858821,-7.478695,-8.073598,0.905719,6.993618,-4.700123,5.213704,-1.354279,3.283985,3.371053,6.532530,-0.149708,9.732603,-3.731577,5.504937,-4.823517,2.331265,4.681183,-4.526947,0.483467,3.636634,4.811873,2.519571,7.496268,-7.711364,1.276948,-5.630838,-1.903484,2.878659,-2.648296,-3.329245,-6.930286,3.610192,-3.374516,-0.139476,-3.604750,9.584037,-1.083629,4.601824,7.763730,-3.920153,1.266228,4.961132,6.241738,7.646636,7.082524,-7.030114,3.422209,-9.995119,1.602083,-5.912959,-6.575277,3.729812,-2.694808,1.318848,-2.057410,7.000871,-2.692086,4.601609,4.299475,1.876659,0.570433,-8.420990,-6.763576,-4.309092,-8.638567,4.013151,-5.510973,8.751387,2.226514,-5.728613,7.481094,-2.229571,-0.986837,5.175221,-3.816852,3.591466,-3.984866,-3.304837,-7.470461,-4.486003,8.065916,7.576991,-8.876701,5.652898,3.429740,-8.057393,0.703714,-5.116273,-9.916567,0.891061,3.871852,-5.301104,7.998109,-8.395315,7.238048,-7.000054,-5.201504,-7.368254,-0.021489,-7.467851,-0.002164,-2.387820,2.501725,7.662389,-7.845501,-4.167464,8.522662,5.435640,-9.642515,-2.013004,-8.305162,-2.534594,0.270696,-5.174514,-7.226573,3.057568,8.987097,-5.939736,3.674400,-8.985278,8.855297,5.871907,-9.565460,6.611469,-2.924241,-8.156619,-0.036324,8.657011,-1.851580,3.318818,-7.922540,6.067646,6.567199,9.313345,9.748656,-5.106554,-3.194414,-1.790907,7.249760,3.879610,4.924635,-6.383663,0.804732,8.484330,8.154891,-5.373319,-8.035478,7.992301,-5.241472,-3.151858,4.827538,-4.755499,-9.204675,-3.501862,-2.398543,1.795341,9.234203,9.349726,1.291733,-7.127732,3.832603,-0.005587,-8.704526,0.161408,-0.284297,5.465800,9.167825,-1.519439,-0.673981,4.502566,-9.583579,-8.692412,-4.890782,-5.798598,4.397853,1.345313], dtype = "float64")#candidate|2489|(1890,)|const|float64
call_2488 = relay.TupleGetItem(func_2075_call(relay.reshape(const_2489.astype('float64'), [1890,])), 0)
call_2490 = relay.TupleGetItem(func_2078_call(relay.reshape(const_2489.astype('float64'), [1890,])), 0)
func_1770_call = mod.get_global_var('func_1770')
func_1774_call = mutated_mod.get_global_var('func_1774')
const_2495 = relay.const([[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[True],[False],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True]], dtype = "bool")#candidate|2495|(1920, 1)|const|bool
call_2494 = relay.TupleGetItem(func_1770_call(relay.reshape(const_2495.astype('bool'), [8, 16, 15]), relay.reshape(const_2495.astype('bool'), [8, 16, 15]), ), 2)
call_2496 = relay.TupleGetItem(func_1774_call(relay.reshape(const_2495.astype('bool'), [8, 16, 15]), relay.reshape(const_2495.astype('bool'), [8, 16, 15]), ), 2)
bop_2505 = relay.logical_xor(call_2479.astype('uint64'), relay.reshape(const_2480.astype('uint64'), relay.shape_of(call_2479))) # shape=(1, 3, 7)
bop_2508 = relay.logical_xor(call_2482.astype('uint64'), relay.reshape(const_2480.astype('uint64'), relay.shape_of(call_2482))) # shape=(1, 3, 7)
var_2509 = relay.var("var_2509", dtype = "float32", shape = (8, 36))#candidate|2509|(8, 36)|var|float32
bop_2510 = relay.left_shift(const_2481.astype('int32'), relay.reshape(var_2509.astype('int32'), relay.shape_of(const_2481))) # shape=(8, 36)
func_1213_call = mod.get_global_var('func_1213')
func_1216_call = mutated_mod.get_global_var('func_1216')
call_2515 = relay.TupleGetItem(func_1213_call(relay.reshape(const_2480.astype('float32'), [1, 3, 7]), relay.reshape(bop_2510.astype('float32'), [8, 36]), ), 6)
call_2516 = relay.TupleGetItem(func_1216_call(relay.reshape(const_2480.astype('float32'), [1, 3, 7]), relay.reshape(bop_2510.astype('float32'), [8, 36]), ), 6)
uop_2518 = relay.sigmoid(call_2456.astype('float64')) # shape=(6, 9, 3)
uop_2520 = relay.sigmoid(call_2457.astype('float64')) # shape=(6, 9, 3)
output = relay.Tuple([call_2460,var_2461,call_2486,call_2488,const_2489,call_2494,const_2495,bop_2505,bop_2510,call_2515,uop_2518,])
output2 = relay.Tuple([call_2462,var_2461,call_2487,call_2490,const_2489,call_2496,const_2495,bop_2508,bop_2510,call_2516,uop_2520,])
func_2526 = relay.Function([var_2461,var_2509,], output)
mod['func_2526'] = func_2526
mod = relay.transform.InferType()(mod)
var_2527 = relay.var("var_2527", dtype = "float32", shape = (144,))#candidate|2527|(144,)|var|float32
var_2528 = relay.var("var_2528", dtype = "float32", shape = (8, 36))#candidate|2528|(8, 36)|var|float32
output = func_2526(var_2527,var_2528,)
func_2529 = relay.Function([var_2527,var_2528,], output)
mutated_mod['func_2529'] = func_2529
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_2559 = func_2281_call()
call_2560 = func_2281_call()
output = relay.Tuple([call_2559,])
output2 = relay.Tuple([call_2560,])
func_2564 = relay.Function([], output)
mod['func_2564'] = func_2564
mod = relay.transform.InferType()(mod)
mutated_mod['func_2564'] = func_2564
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2564_call = mutated_mod.get_global_var('func_2564')
call_2565 = func_2564_call()
output = call_2565
func_2566 = relay.Function([], output)
mutated_mod['func_2566'] = func_2566
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2573 = relay.var("var_2573", dtype = "uint8", shape = (12, 15, 9))#candidate|2573|(12, 15, 9)|var|uint8
const_2574 = relay.const([[[3,6,-1,2,5,-6,-7,2,5],[7,8,-10,10,-9,-10,-6,-9,10],[-5,1,-6,-5,-8,-9,8,8,-9],[-2,-10,3,8,-5,-4,-6,7,-9],[6,8,-2,10,-4,5,7,-10,6],[9,5,-2,-8,7,6,10,1,-10],[6,-2,8,-4,5,-2,-9,7,-2],[10,7,-7,5,-7,-7,9,6,-4],[1,7,-3,-8,-9,-4,-6,-3,6],[-8,-9,-7,-3,-2,10,-5,-5,8],[3,-8,-3,-3,1,-3,-10,-7,-7],[7,-1,-9,6,-3,-6,7,-6,-2],[-9,9,-5,-6,5,-3,-8,-2,-9],[1,7,-6,-4,4,8,-1,3,7],[-4,10,-8,4,3,-4,-1,10,10]],[[2,-9,-6,-2,-3,6,-10,7,-2],[5,1,-3,4,2,1,10,-8,10],[5,8,7,-10,-4,9,1,1,-3],[7,-6,1,-10,9,-7,1,-10,-10],[3,-4,-6,-3,8,-9,6,-8,2],[10,-8,2,-7,-9,-4,-4,8,5],[4,3,2,2,-5,-10,10,2,10],[-5,-1,-6,3,3,9,-9,6,4],[3,7,6,8,-9,4,-6,-6,3],[-1,1,10,-2,4,1,9,4,4],[3,-4,2,-4,4,5,-2,-6,2],[5,-4,-3,7,-9,-8,-8,4,-5],[-7,3,9,-1,-6,-3,2,2,5],[3,9,-10,6,10,-10,-6,-4,-8],[-9,-3,7,-5,4,-9,5,10,5]],[[-1,-9,-2,-5,-6,7,3,7,3],[4,5,5,6,5,6,-9,2,9],[9,-10,5,2,-5,8,3,6,-9],[-9,1,-4,-3,-5,2,-8,-7,7],[8,-2,8,-9,-3,8,-5,8,10],[-4,-6,9,10,1,6,1,-7,4],[-4,-8,-9,-10,3,10,-1,-8,1],[5,5,-1,3,-2,5,-8,9,8],[2,2,-6,-1,-7,4,-8,-1,6],[-3,-6,-9,-1,1,-1,-7,7,-10],[-2,-9,-4,8,3,-5,3,-8,-3],[1,-2,-3,1,7,1,-10,10,1],[4,6,-1,8,10,-5,1,-8,-6],[9,3,7,7,7,7,-1,-9,10],[-9,4,-4,-4,-2,-1,7,10,-10]],[[-6,-2,-2,2,2,10,1,-4,-1],[-5,5,-1,-10,8,8,4,-3,-6],[-7,-10,-2,-5,-2,-10,-5,-9,-4],[9,-7,-1,7,9,-4,-6,-5,-2],[-7,-10,3,-1,6,-1,2,-4,8],[-6,-3,-4,-9,-7,-7,1,-3,-4],[-4,-5,6,-1,-7,-7,-2,-2,7],[-1,-8,-5,5,-10,9,-3,8,-5],[5,3,3,-8,3,10,-8,10,-7],[-1,-1,1,5,-4,3,5,5,9],[-8,-3,-9,-2,-3,-2,-5,3,6],[-5,9,1,-9,9,6,2,-6,-6],[-7,3,3,10,-10,4,-8,-6,10],[-8,-8,3,-6,-10,7,9,-6,-3],[10,7,-8,-6,1,3,3,-2,-8]],[[-5,-7,9,2,-7,-2,5,6,2],[4,10,1,-9,-5,-5,6,-7,4],[-7,4,5,6,8,4,8,7,5],[3,4,5,-1,7,3,6,8,-6],[7,-4,6,6,-6,-1,-1,-5,2],[-4,2,-5,-5,-7,-4,-7,-6,8],[9,-5,-7,7,3,-4,-3,-2,-10],[-2,-9,-7,3,-3,-6,-1,5,9],[-4,-9,-8,4,1,-10,2,-5,2],[-1,9,6,-7,8,2,-3,6,5],[-6,9,2,10,1,4,-9,-10,1],[2,10,-1,9,-1,7,-3,5,-2],[-9,-3,-6,-6,4,-3,-10,4,-7],[4,-8,-3,3,7,7,-6,-10,1],[-8,2,10,8,10,-2,6,3,3]],[[8,-3,3,-6,10,-8,3,5,5],[-3,-7,-6,10,-5,7,-10,-3,1],[4,-2,3,-3,-5,4,-4,-4,9],[-10,-1,1,-10,-2,5,8,3,4],[-2,-4,5,-9,-4,2,3,10,4],[2,4,8,9,9,-7,-8,7,-6],[-10,3,-7,5,6,4,1,-5,-1],[-4,-10,2,3,-6,2,7,6,5],[-5,-3,-10,-1,4,5,1,-6,10],[8,-8,8,-6,-3,4,-6,-2,10],[-6,2,8,-5,-7,-2,7,-2,4],[-6,-4,-5,-8,-7,-9,-4,-1,7],[4,-10,3,7,4,6,1,2,-10],[6,-7,-10,-2,-5,1,-2,-6,-5],[8,8,3,-2,3,-10,1,2,-8]],[[6,7,5,-5,-10,-1,9,-6,3],[-10,-4,9,7,1,-9,2,-1,9],[6,2,5,10,5,1,-7,-3,6],[-8,-5,4,10,-9,6,6,4,-7],[-3,4,-5,8,-8,5,-4,-8,-4],[2,10,-4,1,-8,7,-5,2,-10],[6,9,10,9,8,2,-10,5,-6],[-6,-8,4,-10,8,10,-9,8,10],[3,-2,7,-3,6,6,-7,-1,-9],[-10,7,10,-8,2,6,-3,-3,10],[-9,-4,-2,-9,7,4,8,-4,4],[10,3,-9,6,-8,9,9,-2,2],[-5,3,-2,7,-10,5,-7,7,9],[-10,8,-5,5,-4,7,1,9,-4],[-10,1,4,-4,-10,-10,7,-3,-8]],[[-1,-10,-2,-2,-9,-6,2,-5,-5],[-8,7,-2,-9,7,-3,10,-9,-10],[9,5,-3,-2,8,9,-6,2,6],[-2,-2,-7,-5,-8,9,-9,-10,-8],[-5,9,10,7,-6,1,5,-9,2],[2,4,4,-8,4,7,-2,-6,8],[-8,4,-5,9,8,-7,-3,10,6],[3,-6,3,-10,-6,5,-4,10,-8],[3,-5,5,-1,-10,8,-4,-2,-9],[-4,10,-7,7,-8,7,1,3,-1],[7,-9,-5,-7,-7,1,-3,-6,6],[-6,5,9,-1,-4,-4,5,8,-2],[-10,-2,-5,-2,8,3,-1,7,4],[8,4,-10,-8,4,10,7,-3,6],[1,-8,7,-3,10,-6,5,10,7]],[[-10,6,9,7,5,-6,-10,10,-4],[-9,7,6,-6,7,-10,9,-7,3],[-10,-3,-10,5,-4,8,-3,-6,10],[2,-2,-5,3,-4,6,8,10,2],[-10,2,3,-3,-8,-5,-2,-6,7],[-9,-5,1,-2,9,10,-4,8,6],[5,-8,-10,-3,9,7,3,6,-10],[-1,-8,4,2,10,-3,3,-6,3],[3,8,-7,10,10,-8,-5,-3,-9],[-10,-7,3,7,-10,-9,10,-8,8],[3,5,-5,4,-2,-2,-5,2,-7],[6,4,-8,8,7,-6,3,-4,-3],[-3,-1,-3,6,9,2,4,9,-3],[-9,7,-10,2,4,-4,-6,-3,2],[2,-4,5,-7,5,4,-7,10,10]],[[8,-5,-1,1,-6,6,10,5,1],[1,8,5,3,-7,-7,3,3,10],[-7,-1,7,2,-5,1,-8,5,-8],[7,4,4,-3,9,-7,9,-1,-8],[8,-6,-8,1,1,1,10,-1,-4],[-8,-4,-4,-7,6,3,-8,5,-4],[-3,8,-4,-3,8,9,-9,-10,3],[5,-7,9,6,-9,-3,5,-1,-8],[-3,-7,5,5,-2,-6,-1,6,1],[-5,3,9,8,-2,6,-4,-10,-1],[7,-8,5,6,6,-1,9,5,2],[10,7,-9,-1,-1,-5,6,10,-3],[-10,10,-2,5,9,-5,-4,-2,-4],[-4,-5,-6,9,2,-7,-4,-5,3],[7,1,7,-8,-9,-4,3,-10,4]],[[9,-9,3,-8,-1,3,-2,-1,8],[-9,3,-9,2,8,10,-9,3,2],[2,-3,2,-10,-6,-7,10,-1,3],[3,-1,9,-1,2,6,2,-3,4],[2,-10,-4,-3,3,9,-3,5,-3],[7,5,-10,3,-1,-8,2,9,-10],[-8,-9,-8,-9,3,7,8,-2,3],[-4,-5,-3,-1,4,-4,5,7,3],[4,-8,-5,5,-9,6,8,-8,-8],[7,-3,-1,5,-1,2,10,5,5],[5,5,6,5,3,8,-2,1,5],[-4,-8,7,-8,-5,6,-5,9,-2],[1,-8,1,-4,-2,8,-6,10,-5],[3,-5,-8,-8,10,1,2,-1,6],[10,-7,-4,-2,7,-6,10,-8,8]],[[3,-7,5,9,9,2,4,-5,4],[5,-2,9,-7,-7,-1,-10,-5,1],[4,9,-2,3,3,-6,-9,-3,5],[1,9,6,-5,8,1,9,-1,-3],[9,10,3,-7,9,7,1,6,8],[-2,6,4,-1,-7,3,-5,7,2],[-3,4,10,6,1,-1,-3,3,-5],[9,10,-8,7,5,1,3,10,-6],[1,4,-5,1,10,-9,1,-10,-3],[5,-4,-3,-10,10,6,-10,9,8],[-9,-4,-3,5,-1,4,-5,-6,-9],[-5,7,-7,-1,-1,3,6,8,-10],[-5,2,1,-3,-5,7,-10,-3,10],[-2,-8,-3,10,-2,1,9,8,3],[-9,8,-5,-8,-1,-4,2,4,-6]]], dtype = "uint8")#candidate|2574|(12, 15, 9)|const|uint8
bop_2575 = relay.logical_xor(var_2573.astype('uint8'), relay.reshape(const_2574.astype('uint8'), relay.shape_of(var_2573))) # shape=(12, 15, 9)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2580 = relay.TupleGetItem(func_2017_call(), 0)
call_2581 = relay.TupleGetItem(func_2019_call(), 0)
const_2601 = relay.const([[[10,3,-10,3,9,-6,-8,5,-5],[-5,2,-3,7,-5,-3,-10,-3,-9],[1,-6,3,-1,8,4,7,-4,-7],[9,9,2,-4,-7,7,-2,5,9],[2,8,-8,-3,4,-5,6,-6,7],[-9,2,10,1,6,-1,-3,-6,5],[7,-8,-7,3,-6,-2,-7,-6,6],[-6,7,4,-10,-3,10,-8,-5,-10],[-9,8,2,-10,3,-7,1,8,7],[8,-9,-4,10,-7,-10,9,-2,7],[-7,2,-1,10,10,2,8,-7,-2],[7,4,-6,3,-6,-2,-6,7,8],[-6,-2,6,6,-3,-2,-5,-4,5],[5,-3,2,1,-4,-7,-10,3,-9],[-5,3,-1,2,6,-5,6,-10,1]],[[4,-3,4,-3,2,6,6,-10,1],[6,5,9,-4,2,-6,7,6,-10],[-9,-5,-10,-4,-4,7,-4,-9,6],[3,-5,-5,7,-10,-1,3,5,1],[-9,-4,-9,-8,-4,4,-7,2,-3],[4,1,2,6,2,-3,7,-7,-3],[-1,-1,-10,-9,-3,10,9,5,7],[10,3,5,4,-8,-4,-7,-1,-2],[-5,-9,-1,2,2,8,5,5,1],[-5,-3,-5,-3,-1,-3,7,-1,4],[-3,10,6,-7,7,10,-3,2,-8],[-2,-3,5,-6,-4,9,9,-6,9],[8,-4,9,4,1,-7,-4,9,-2],[3,-7,6,-5,-1,-5,-5,-8,7],[-5,1,-8,-4,-7,-10,-5,8,-10]],[[-1,-9,-7,5,-7,-3,10,7,3],[-10,-8,9,-10,8,10,4,2,4],[-8,-3,1,1,-5,5,-6,4,3],[-1,-10,1,-9,-1,-8,2,3,-3],[1,-6,-6,4,-5,5,4,9,7],[3,-4,-6,-1,-8,-4,-9,-7,-3],[5,5,8,9,6,-7,9,8,8],[6,2,2,-7,3,5,8,-3,-3],[3,-4,-10,-1,-5,-2,2,-10,2],[-2,-4,-4,3,2,-5,9,-5,-6],[-8,-5,7,-5,3,-5,9,3,-6],[-4,-7,7,1,9,-10,2,3,10],[3,10,3,1,5,-5,1,8,-8],[-1,2,5,-4,-2,4,-8,9,5],[5,4,-3,9,-10,3,3,-5,3]],[[-8,8,-7,-4,-1,5,7,-5,-8],[-9,2,5,7,1,-4,3,3,-4],[6,-7,2,-7,2,9,-10,-10,-10],[-10,-4,1,5,-1,-7,-1,4,-2],[-2,5,-2,-5,-3,-7,-9,-9,9],[-10,-6,-5,6,6,5,-6,10,10],[-6,-6,-9,3,1,-10,4,7,3],[-2,9,10,-9,-1,-8,1,-6,-6],[-10,-3,-2,1,7,7,1,10,9],[-6,-6,5,5,-9,-3,-6,-5,3],[-3,5,-4,9,-2,-9,-9,-9,-9],[-9,2,-7,-5,5,-3,-9,-5,-8],[7,-6,8,-9,-8,10,-5,-6,-8],[-2,-8,-3,7,9,6,-9,-7,-3],[-10,-2,3,10,2,6,8,3,5]],[[5,7,2,-1,8,7,3,-8,-10],[8,10,3,-1,2,-7,9,-8,7],[-4,2,8,-5,-1,-7,-3,-8,-4],[7,-3,9,-5,-3,-7,-5,-1,-2],[10,-10,-10,1,-2,6,-3,-1,-3],[8,9,3,4,-6,6,-5,-5,5],[-2,1,-7,-7,-10,-7,-1,1,8],[7,-3,-10,10,3,-8,3,7,3],[-10,6,-1,3,8,3,1,2,2],[10,7,1,4,-7,-9,8,-1,1],[5,-3,9,3,-5,-3,6,10,7],[-1,5,-5,-6,-4,-5,-6,-9,5],[6,-10,-4,-7,4,-4,-7,3,2],[-6,1,3,3,6,2,-1,-9,7],[-4,4,2,-1,4,10,-4,-2,4]],[[-10,-7,-10,6,-7,-4,10,9,-6],[-3,-9,-4,1,-3,4,-10,-6,-1],[-8,-8,5,9,10,9,-10,-6,7],[6,-2,3,-8,-2,-2,1,-1,-2],[2,2,-9,1,-3,-8,9,-10,-5],[-8,-6,7,5,-5,-8,-5,-8,4],[7,-9,-2,-1,-1,3,2,8,2],[-7,5,5,10,-6,6,8,-7,4],[-3,4,3,-9,7,-4,-5,7,-2],[-5,-2,-3,-5,10,9,5,6,-6],[-5,6,4,-4,-3,-1,3,9,1],[2,4,-1,-7,-7,-4,-3,-9,4],[1,4,-10,8,5,9,-1,3,4],[-10,-10,5,1,-6,7,4,7,1],[-5,1,8,5,2,7,-3,8,-6]],[[-7,8,-7,-3,-4,-1,8,-6,5],[10,5,9,9,-9,-5,-9,-1,-8],[-6,9,1,-5,-5,1,-4,1,2],[-9,4,-9,4,5,-7,-6,-2,-10],[-7,6,-5,2,-8,7,5,-3,8],[1,-10,-1,-7,-9,-2,-6,4,-10],[8,8,-7,8,-3,-4,-10,4,9],[-6,-2,9,-4,2,-8,-6,-4,-4],[1,2,10,-6,-1,10,-6,10,1],[-10,4,-2,-4,-9,-5,9,5,-10],[9,7,6,2,6,-10,1,10,3],[8,-10,-6,-1,1,-8,3,6,-7],[-9,-4,1,10,3,-7,-1,4,3],[-6,-6,-2,-7,4,-7,8,2,-9],[-6,-6,8,-5,-10,10,-10,-10,5]],[[-3,-7,8,7,-7,7,-3,6,2],[-3,-5,-10,6,3,-8,-8,-1,-7],[-8,-4,-3,-5,-6,6,-7,6,1],[8,8,5,-10,-9,7,-1,-10,2],[-7,-2,7,10,-6,-5,4,8,3],[-2,-6,5,8,-8,10,-4,6,8],[3,-5,-4,-9,4,-4,1,-1,6],[-10,-9,-3,-8,-5,-4,-8,-1,-9],[5,-7,5,5,7,3,-1,8,-1],[10,9,-6,8,-1,8,8,-7,-2],[4,8,-5,-5,-4,-6,-5,6,2],[8,-7,1,-8,-1,-3,9,2,9],[10,2,8,-9,-4,6,7,8,-2],[9,9,6,5,-9,3,-2,3,-7],[4,3,-10,-6,2,3,4,-3,4]],[[-4,5,3,3,-10,-3,-9,-2,-7],[-1,1,10,7,-6,8,10,-6,-5],[-10,6,5,7,-6,-6,3,-7,-3],[6,10,10,9,-10,-4,6,5,6],[-3,6,3,-4,1,1,-8,-6,7],[8,8,5,-3,8,4,10,8,-1],[-7,-9,6,-4,5,7,-10,1,1],[1,-8,-5,-2,2,-8,3,7,6],[2,-2,-4,2,-1,3,9,-9,-1],[-9,-7,5,5,-5,-1,-8,2,1],[-6,-1,6,-1,6,-1,-4,1,3],[-9,5,-1,-4,9,-8,4,-3,-2],[-9,-5,-3,-5,9,8,-4,-2,-10],[5,-3,-2,7,4,-10,-1,1,7],[2,-3,-8,5,-10,10,10,-6,2]],[[-4,1,-10,-6,4,-7,-3,3,-2],[-7,-10,5,-8,5,-10,9,5,1],[5,-6,-7,9,4,4,-10,6,-9],[-10,-6,1,2,-9,2,-2,-1,5],[3,-6,8,4,2,-10,1,-9,6],[4,-2,7,-4,2,-9,-3,-2,9],[8,8,3,4,7,-2,5,-3,10],[-2,8,2,-2,-2,-4,6,6,6],[1,5,3,-3,3,5,3,-10,3],[10,6,2,3,-4,2,-8,7,-1],[1,7,7,9,-1,-2,-10,-10,6],[-6,9,-10,7,-4,-3,5,8,-10],[-7,-6,10,3,-2,-8,-6,-9,-4],[6,7,8,-4,6,6,-6,6,1],[1,6,8,4,-8,-1,-10,-6,4]],[[8,6,9,-9,6,8,-1,-3,2],[3,-7,9,-3,-2,9,-2,3,9],[1,6,3,-7,3,-3,1,-1,7],[4,-2,-1,-2,5,5,9,6,-5],[9,5,-10,-7,4,-9,9,-5,10],[1,10,-9,-4,1,2,-8,8,3],[4,10,7,1,1,-8,-3,-2,6],[10,-10,9,8,4,-1,-5,6,-4],[-5,10,2,-8,6,-10,3,-2,2],[4,-9,8,-5,6,2,-6,-5,-4],[4,-2,4,-5,-3,-10,8,-6,4],[8,9,-1,-2,-8,3,5,-6,10],[-10,-6,3,9,2,10,-1,5,2],[1,-5,2,2,5,-4,-9,1,-9],[-3,-6,4,-1,4,-5,2,-2,-6]],[[4,2,8,-6,2,2,2,10,10],[-3,8,-5,-6,10,5,-2,6,2],[-4,2,-8,9,-10,5,4,-1,5],[-5,6,-9,-1,-3,9,-4,-4,10],[1,-1,8,-2,-5,-5,10,3,7],[-6,5,9,5,-8,8,-2,-7,1],[-8,-10,-8,3,-8,4,8,-6,-9],[8,6,2,4,-2,-6,8,8,7],[4,-3,-8,-6,7,1,6,-10,5],[-6,-6,10,3,-6,-6,6,2,-2],[6,-7,1,1,-7,-10,2,3,-6],[2,3,-2,-10,10,-10,2,-10,1],[9,9,-2,10,6,-6,8,-2,5],[-1,2,6,-4,2,-9,7,6,4],[6,-3,-7,5,-6,-6,10,-7,1]]], dtype = "uint8")#candidate|2601|(12, 15, 9)|const|uint8
bop_2602 = relay.multiply(bop_2575.astype('float32'), relay.reshape(const_2601.astype('float32'), relay.shape_of(bop_2575))) # shape=(12, 15, 9)
uop_2617 = relay.log10(call_2580.astype('float64')) # shape=(6, 9, 3)
uop_2619 = relay.log10(call_2581.astype('float64')) # shape=(6, 9, 3)
output = relay.Tuple([bop_2602,uop_2617,])
output2 = relay.Tuple([bop_2602,uop_2619,])
func_2627 = relay.Function([var_2573,], output)
mod['func_2627'] = func_2627
mod = relay.transform.InferType()(mod)
var_2628 = relay.var("var_2628", dtype = "uint8", shape = (12, 15, 9))#candidate|2628|(12, 15, 9)|var|uint8
output = func_2627(var_2628)
func_2629 = relay.Function([var_2628], output)
mutated_mod['func_2629'] = func_2629
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2631 = relay.TupleGetItem(func_2017_call(), 0)
call_2632 = relay.TupleGetItem(func_2019_call(), 0)
uop_2637 = relay.sin(call_2631.astype('float32')) # shape=(6, 9, 3)
uop_2639 = relay.sin(call_2632.astype('float32')) # shape=(6, 9, 3)
output = uop_2637
output2 = uop_2639
func_2645 = relay.Function([], output)
mod['func_2645'] = func_2645
mod = relay.transform.InferType()(mod)
mutated_mod['func_2645'] = func_2645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mutated_mod.get_global_var('func_2645')
call_2646 = func_2645_call()
output = call_2646
func_2647 = relay.Function([], output)
mutated_mod['func_2647'] = func_2647
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2650 = relay.var("var_2650", dtype = "float32", shape = (9, 14, 14))#candidate|2650|(9, 14, 14)|var|float32
uop_2651 = relay.erf(var_2650.astype('float32')) # shape=(9, 14, 14)
output = relay.Tuple([uop_2651,])
output2 = relay.Tuple([uop_2651,])
func_2655 = relay.Function([var_2650,], output)
mod['func_2655'] = func_2655
mod = relay.transform.InferType()(mod)
var_2656 = relay.var("var_2656", dtype = "float32", shape = (9, 14, 14))#candidate|2656|(9, 14, 14)|var|float32
output = func_2655(var_2656)
func_2657 = relay.Function([var_2656], output)
mutated_mod['func_2657'] = func_2657
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2692 = relay.var("var_2692", dtype = "float64", shape = (13, 14, 7))#candidate|2692|(13, 14, 7)|var|float64
uop_2693 = relay.cosh(var_2692.astype('float64')) # shape=(13, 14, 7)
bop_2703 = relay.logical_and(var_2692.astype('bool'), relay.reshape(uop_2693.astype('bool'), relay.shape_of(var_2692))) # shape=(13, 14, 7)
func_1931_call = mod.get_global_var('func_1931')
func_1934_call = mutated_mod.get_global_var('func_1934')
var_2717 = relay.var("var_2717", dtype = "int64", shape = (24, 10))#candidate|2717|(24, 10)|var|int64
call_2716 = relay.TupleGetItem(func_1931_call(relay.reshape(var_2717.astype('int64'), [6, 8, 5])), 0)
call_2718 = relay.TupleGetItem(func_1934_call(relay.reshape(var_2717.astype('int64'), [6, 8, 5])), 0)
output = relay.Tuple([bop_2703,call_2716,var_2717,])
output2 = relay.Tuple([bop_2703,call_2718,var_2717,])
func_2720 = relay.Function([var_2692,var_2717,], output)
mod['func_2720'] = func_2720
mod = relay.transform.InferType()(mod)
var_2721 = relay.var("var_2721", dtype = "float64", shape = (13, 14, 7))#candidate|2721|(13, 14, 7)|var|float64
var_2722 = relay.var("var_2722", dtype = "int64", shape = (24, 10))#candidate|2722|(24, 10)|var|int64
output = func_2720(var_2721,var_2722,)
func_2723 = relay.Function([var_2721,var_2722,], output)
mutated_mod['func_2723'] = func_2723
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2773 = relay.const([[[1,9,-2,6,-9,1,1,8,5,-5,8,-9,-6]],[[6,-8,-5,-9,-10,7,6,-9,10,1,9,-7,-9]],[[8,6,10,9,-4,-10,9,3,-8,-3,-6,-4,2]],[[6,-8,6,4,8,-3,3,-1,2,3,-7,-6,5]],[[-3,10,-2,7,-3,4,5,1,-10,7,9,3,-7]],[[-2,-1,7,-6,1,5,-8,1,6,-5,-3,-3,-10]],[[2,-4,-4,-3,3,-8,9,7,-7,4,8,-1,-9]],[[1,7,-6,-5,-9,7,5,-4,-9,4,6,-4,9]],[[-10,-6,-7,3,-6,-6,-9,9,8,6,-9,-2,-4]],[[4,9,-7,-4,-8,-9,8,1,-8,8,8,3,10]],[[10,5,-10,-1,10,10,2,6,10,-9,-7,-1,6]],[[1,-3,3,2,-9,-7,-5,-8,-3,-2,4,-5,1]],[[1,7,3,-9,10,4,-2,-8,3,7,6,-4,3]],[[8,-10,-9,5,8,-3,-8,3,-7,-5,5,6,-9]],[[-6,-1,-8,6,-2,-9,-3,6,-8,-1,4,-7,10]],[[-7,5,-1,9,-9,-4,7,4,-2,-6,2,-3,-6]]], dtype = "int32")#candidate|2773|(16, 1, 13)|const|int32
var_2774 = relay.var("var_2774", dtype = "int32", shape = (16, 14, 13))#candidate|2774|(16, 14, 13)|var|int32
bop_2775 = relay.multiply(const_2773.astype('int32'), var_2774.astype('int32')) # shape=(16, 14, 13)
uop_2789 = relay.erf(bop_2775.astype('float32')) # shape=(16, 14, 13)
output = uop_2789
output2 = uop_2789
func_2792 = relay.Function([var_2774,], output)
mod['func_2792'] = func_2792
mod = relay.transform.InferType()(mod)
var_2793 = relay.var("var_2793", dtype = "int32", shape = (16, 14, 13))#candidate|2793|(16, 14, 13)|var|int32
output = func_2792(var_2793)
func_2794 = relay.Function([var_2793], output)
mutated_mod['func_2794'] = func_2794
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2172_call = mutated_mod.get_global_var('func_2172')
call_2811 = func_2171_call()
call_2812 = func_2171_call()
output = call_2811
output2 = call_2812
func_2814 = relay.Function([], output)
mod['func_2814'] = func_2814
mod = relay.transform.InferType()(mod)
mutated_mod['func_2814'] = func_2814
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mutated_mod.get_global_var('func_2814')
call_2815 = func_2814_call()
output = call_2815
func_2816 = relay.Function([], output)
mutated_mod['func_2816'] = func_2816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_2848 = relay.TupleGetItem(func_2089_call(), 0)
call_2849 = relay.TupleGetItem(func_2091_call(), 0)
var_2855 = relay.var("var_2855", dtype = "float64", shape = (6, 9, 3))#candidate|2855|(6, 9, 3)|var|float64
bop_2856 = relay.equal(call_2848.astype('bool'), relay.reshape(var_2855.astype('bool'), relay.shape_of(call_2848))) # shape=(6, 9, 3)
bop_2859 = relay.equal(call_2849.astype('bool'), relay.reshape(var_2855.astype('bool'), relay.shape_of(call_2849))) # shape=(6, 9, 3)
output = relay.Tuple([bop_2856,])
output2 = relay.Tuple([bop_2859,])
func_2883 = relay.Function([var_2855,], output)
mod['func_2883'] = func_2883
mod = relay.transform.InferType()(mod)
var_2884 = relay.var("var_2884", dtype = "float64", shape = (6, 9, 3))#candidate|2884|(6, 9, 3)|var|float64
output = func_2883(var_2884)
func_2885 = relay.Function([var_2884], output)
mutated_mod['func_2885'] = func_2885
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mod.get_global_var('func_2645')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_2974 = func_2645_call()
call_2975 = func_2645_call()
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_2978 = relay.TupleGetItem(func_2017_call(), 1)
call_2979 = relay.TupleGetItem(func_2019_call(), 1)
bop_2994 = relay.logical_or(call_2974.astype('bool'), relay.reshape(call_2978.astype('bool'), relay.shape_of(call_2974))) # shape=(6, 9, 3)
bop_2997 = relay.logical_or(call_2975.astype('bool'), relay.reshape(call_2979.astype('bool'), relay.shape_of(call_2975))) # shape=(6, 9, 3)
output = bop_2994
output2 = bop_2997
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
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_3055 = func_2281_call()
call_3056 = func_2281_call()
output = relay.Tuple([call_3055,])
output2 = relay.Tuple([call_3056,])
func_3068 = relay.Function([], output)
mod['func_3068'] = func_3068
mod = relay.transform.InferType()(mod)
mutated_mod['func_3068'] = func_3068
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3068_call = mutated_mod.get_global_var('func_3068')
call_3069 = func_3068_call()
output = call_3069
func_3070 = relay.Function([], output)
mutated_mod['func_3070'] = func_3070
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3121 = relay.var("var_3121", dtype = "float32", shape = (3, 14, 11))#candidate|3121|(3, 14, 11)|var|float32
uop_3122 = relay.asinh(var_3121.astype('float32')) # shape=(3, 14, 11)
bop_3128 = relay.less(uop_3122.astype('bool'), relay.reshape(var_3121.astype('bool'), relay.shape_of(uop_3122))) # shape=(3, 14, 11)
output = relay.Tuple([bop_3128,])
output2 = relay.Tuple([bop_3128,])
func_3139 = relay.Function([var_3121,], output)
mod['func_3139'] = func_3139
mod = relay.transform.InferType()(mod)
mutated_mod['func_3139'] = func_3139
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3140 = relay.var("var_3140", dtype = "float32", shape = (3, 14, 11))#candidate|3140|(3, 14, 11)|var|float32
func_3139_call = mutated_mod.get_global_var('func_3139')
call_3141 = func_3139_call(var_3140)
output = call_3141
func_3142 = relay.Function([var_3140], output)
mutated_mod['func_3142'] = func_3142
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_3161 = relay.TupleGetItem(func_2089_call(), 0)
call_3162 = relay.TupleGetItem(func_2091_call(), 0)
uop_3182 = relay.exp(call_3161.astype('float64')) # shape=(6, 9, 3)
uop_3184 = relay.exp(call_3162.astype('float64')) # shape=(6, 9, 3)
output = relay.Tuple([uop_3182,])
output2 = relay.Tuple([uop_3184,])
func_3192 = relay.Function([], output)
mod['func_3192'] = func_3192
mod = relay.transform.InferType()(mod)
output = func_3192()
func_3193 = relay.Function([], output)
mutated_mod['func_3193'] = func_3193
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2645_call = mod.get_global_var('func_2645')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_3206 = func_2645_call()
call_3207 = func_2645_call()
output = call_3206
output2 = call_3207
func_3210 = relay.Function([], output)
mod['func_3210'] = func_3210
mod = relay.transform.InferType()(mod)
output = func_3210()
func_3211 = relay.Function([], output)
mutated_mod['func_3211'] = func_3211
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2172_call = mutated_mod.get_global_var('func_2172')
call_3228 = func_2171_call()
call_3229 = func_2171_call()
output = relay.Tuple([call_3228,])
output2 = relay.Tuple([call_3229,])
func_3244 = relay.Function([], output)
mod['func_3244'] = func_3244
mod = relay.transform.InferType()(mod)
mutated_mod['func_3244'] = func_3244
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mutated_mod.get_global_var('func_3244')
call_3245 = func_3244_call()
output = call_3245
func_3246 = relay.Function([], output)
mutated_mod['func_3246'] = func_3246
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_3247 = relay.TupleGetItem(func_2089_call(), 0)
call_3248 = relay.TupleGetItem(func_2091_call(), 0)
uop_3251 = relay.tan(call_3247.astype('float32')) # shape=(6, 9, 3)
uop_3253 = relay.tan(call_3248.astype('float32')) # shape=(6, 9, 3)
output = relay.Tuple([uop_3251,])
output2 = relay.Tuple([uop_3253,])
func_3255 = relay.Function([], output)
mod['func_3255'] = func_3255
mod = relay.transform.InferType()(mod)
output = func_3255()
func_3256 = relay.Function([], output)
mutated_mod['func_3256'] = func_3256
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_3273 = relay.TupleGetItem(func_3244_call(), 0)
call_3274 = relay.TupleGetItem(func_3246_call(), 0)
func_3255_call = mod.get_global_var('func_3255')
func_3256_call = mutated_mod.get_global_var('func_3256')
call_3281 = relay.TupleGetItem(func_3255_call(), 0)
call_3282 = relay.TupleGetItem(func_3256_call(), 0)
output = relay.Tuple([call_3273,call_3281,])
output2 = relay.Tuple([call_3274,call_3282,])
func_3287 = relay.Function([], output)
mod['func_3287'] = func_3287
mod = relay.transform.InferType()(mod)
output = func_3287()
func_3288 = relay.Function([], output)
mutated_mod['func_3288'] = func_3288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3210_call = mod.get_global_var('func_3210')
func_3211_call = mutated_mod.get_global_var('func_3211')
call_3295 = func_3210_call()
call_3296 = func_3210_call()
uop_3302 = relay.atan(call_3295.astype('float64')) # shape=(6, 9, 3)
uop_3304 = relay.atan(call_3296.astype('float64')) # shape=(6, 9, 3)
func_1931_call = mod.get_global_var('func_1931')
func_1934_call = mutated_mod.get_global_var('func_1934')
var_3308 = relay.var("var_3308", dtype = "int64", shape = (240,))#candidate|3308|(240,)|var|int64
call_3307 = relay.TupleGetItem(func_1931_call(relay.reshape(var_3308.astype('int64'), [6, 8, 5])), 0)
call_3309 = relay.TupleGetItem(func_1934_call(relay.reshape(var_3308.astype('int64'), [6, 8, 5])), 0)
func_2627_call = mod.get_global_var('func_2627')
func_2629_call = mutated_mod.get_global_var('func_2629')
var_3311 = relay.var("var_3311", dtype = "uint8", shape = (1620,))#candidate|3311|(1620,)|var|uint8
call_3310 = relay.TupleGetItem(func_2627_call(relay.reshape(var_3311.astype('uint8'), [12, 15, 9])), 0)
call_3312 = relay.TupleGetItem(func_2629_call(relay.reshape(var_3311.astype('uint8'), [12, 15, 9])), 0)
output = relay.Tuple([uop_3302,call_3307,var_3308,call_3310,var_3311,])
output2 = relay.Tuple([uop_3304,call_3309,var_3308,call_3312,var_3311,])
func_3314 = relay.Function([var_3308,var_3311,], output)
mod['func_3314'] = func_3314
mod = relay.transform.InferType()(mod)
var_3315 = relay.var("var_3315", dtype = "int64", shape = (240,))#candidate|3315|(240,)|var|int64
var_3316 = relay.var("var_3316", dtype = "uint8", shape = (1620,))#candidate|3316|(1620,)|var|uint8
output = func_3314(var_3315,var_3316,)
func_3317 = relay.Function([var_3315,var_3316,], output)
mutated_mod['func_3317'] = func_3317
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3371 = relay.var("var_3371", dtype = "float32", shape = (8, 14, 1))#candidate|3371|(8, 14, 1)|var|float32
uop_3372 = relay.sqrt(var_3371.astype('float32')) # shape=(8, 14, 1)
bop_3374 = relay.multiply(uop_3372.astype('int64'), relay.reshape(var_3371.astype('int64'), relay.shape_of(uop_3372))) # shape=(8, 14, 1)
bop_3377 = relay.mod(uop_3372.astype('float64'), relay.reshape(var_3371.astype('float64'), relay.shape_of(uop_3372))) # shape=(8, 14, 1)
func_2322_call = mod.get_global_var('func_2322')
func_2327_call = mutated_mod.get_global_var('func_2327')
var_3383 = relay.var("var_3383", dtype = "float64", shape = (26, 5))#candidate|3383|(26, 5)|var|float64
var_3384 = relay.var("var_3384", dtype = "float32", shape = (800,))#candidate|3384|(800,)|var|float32
const_3385 = relay.const([-7.076789,-5.903307,9.081320,-3.238615,9.783664,2.954755,0.482360,1.560980,4.133221,-3.877031,-8.760704,-2.968018,2.521561,-9.565953,1.323544,-1.199701,-0.282436,-4.754458,-7.918368,8.895044,2.412203], dtype = "float32")#candidate|3385|(21,)|const|float32
call_3382 = relay.TupleGetItem(func_2322_call(relay.reshape(var_3383.astype('float64'), [13, 10]), relay.reshape(var_3384.astype('float32'), [200, 4]), relay.reshape(const_3385.astype('float32'), [1, 21]), ), 0)
call_3386 = relay.TupleGetItem(func_2327_call(relay.reshape(var_3383.astype('float64'), [13, 10]), relay.reshape(var_3384.astype('float32'), [200, 4]), relay.reshape(const_3385.astype('float32'), [1, 21]), ), 0)
uop_3394 = relay.atanh(bop_3377.astype('float64')) # shape=(8, 14, 1)
output = relay.Tuple([bop_3374,call_3382,var_3383,var_3384,const_3385,uop_3394,])
output2 = relay.Tuple([bop_3374,call_3386,var_3383,var_3384,const_3385,uop_3394,])
func_3406 = relay.Function([var_3371,var_3383,var_3384,], output)
mod['func_3406'] = func_3406
mod = relay.transform.InferType()(mod)
mutated_mod['func_3406'] = func_3406
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3406_call = mutated_mod.get_global_var('func_3406')
var_3408 = relay.var("var_3408", dtype = "float32", shape = (8, 14, 1))#candidate|3408|(8, 14, 1)|var|float32
var_3409 = relay.var("var_3409", dtype = "float64", shape = (26, 5))#candidate|3409|(26, 5)|var|float64
var_3410 = relay.var("var_3410", dtype = "float32", shape = (800,))#candidate|3410|(800,)|var|float32
call_3407 = func_3406_call(var_3408,var_3409,var_3410,)
output = call_3407
func_3411 = relay.Function([var_3408,var_3409,var_3410,], output)
mutated_mod['func_3411'] = func_3411
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3413 = relay.var("var_3413", dtype = "bool", shape = (13, 10, 6))#candidate|3413|(13, 10, 6)|var|bool
var_3414 = relay.var("var_3414", dtype = "bool", shape = (13, 10, 6))#candidate|3414|(13, 10, 6)|var|bool
bop_3415 = relay.logical_and(var_3413.astype('bool'), relay.reshape(var_3414.astype('bool'), relay.shape_of(var_3413))) # shape=(13, 10, 6)
output = bop_3415
output2 = bop_3415
func_3426 = relay.Function([var_3413,var_3414,], output)
mod['func_3426'] = func_3426
mod = relay.transform.InferType()(mod)
mutated_mod['func_3426'] = func_3426
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3426_call = mutated_mod.get_global_var('func_3426')
var_3428 = relay.var("var_3428", dtype = "bool", shape = (13, 10, 6))#candidate|3428|(13, 10, 6)|var|bool
var_3429 = relay.var("var_3429", dtype = "bool", shape = (13, 10, 6))#candidate|3429|(13, 10, 6)|var|bool
call_3427 = func_3426_call(var_3428,var_3429,)
output = call_3427
func_3430 = relay.Function([var_3428,var_3429,], output)
mutated_mod['func_3430'] = func_3430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_3449 = relay.TupleGetItem(func_2017_call(), 0)
call_3450 = relay.TupleGetItem(func_2019_call(), 0)
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
const_3458 = relay.const([-3.202898,2.085387,6.788721,8.584372,-1.447810,9.800095,-1.431339,1.804856,-3.716537,-5.177699,5.446378,-7.063262,6.210549,1.026392,1.886899,4.731912,3.069552,2.752585,-2.447111,5.517070,1.442302,-6.993254,2.664218,6.998970,-2.173871,8.489973,-0.959569,-8.185486,-4.360580,-3.830578,9.064786,5.905809,7.421591,-1.040848,7.197478,-3.236173,-8.213118,-5.246742,0.506954,8.702572,-9.970209,2.181300,-2.670339,-5.421315,-8.449059,-7.985646,-9.427768,-4.425371,7.014288,4.799226,-1.167826,4.998776,-7.911053,-4.217999,3.419991,-6.182796,-3.185659,-0.928215,3.161344,9.902913,-6.649171,9.303857,1.504579,-7.194864,-8.973397,2.601673,9.879598,8.353990,0.585553,3.039586,-6.155417,-8.910714,-1.734068,2.597591,0.347627,6.947947,1.440078,-6.866134,-0.388551,6.804713,8.887616,6.571438,4.116457,-4.077652,-5.042640,4.341381,5.065405,-5.280815,9.588218,9.748575,-3.018531,-6.191105,-4.749160,4.619925,1.509139,2.168872,3.258346,5.751565,-5.052619,7.004643,-2.837802,1.302036,-9.123272,9.460433,0.390793,-3.434380,2.262607,5.482449,-4.760705,-2.548611,8.254617,-9.972129,-3.716382,3.866051,8.066666,5.554978,-4.195336,-1.599322,-9.530909,-6.140803,-5.619954,-3.777571,6.137361,6.067096,-4.179498,7.424737,-3.581217,-8.064391,1.094835,8.410303,0.029683,-6.788987,1.100629,-2.824472,-8.282629,5.733002,-9.566568,-4.516827,-4.271494,7.636746,6.348080,-7.667423,-6.774214,-9.396512,6.609715,-9.104300,5.400343,-9.001586,8.873373,-0.194997,7.854978,7.476520,0.919412,8.126212,9.062816,-4.410246,5.501042,-4.264948,-5.261512,0.097977,-9.663692,-6.522048,3.832131,-3.450780,2.226513,-6.876949,5.546553,-1.322499,-9.646280,-2.166183,-8.756498,-1.928653,6.250506,7.162505,-1.522269,5.801196,6.027370,-9.243271,-7.165178,9.419742,2.431491,-8.690231,9.419721,-0.453398,-9.868676,-5.110005,9.342983,-7.335030,7.282060,-6.480058,7.666235,6.689115,6.882934,3.631812,-3.016999,-6.086245,-7.777479,-4.614419,9.442632,6.776482,2.840076,5.923443,8.758969,-2.430339,7.722543,-4.512799,-4.944230,7.740269,2.372095,-3.295718,-1.955613,2.395053,5.274402,-7.949455,-5.294793,4.702670,6.748611,7.881246,-3.866565,-8.697688,-8.844524,-6.741399,-1.727550,3.232916,-0.834203,1.059266,-6.386282,-4.000392,4.056371,-4.808935,-2.651452,4.367284,-0.303293,-1.190581,-3.044131,8.771248,1.651829,-5.346080,9.705797,3.474660,7.064801,-4.337357,-3.481275,0.493012,-1.286786,6.088858,1.799913,-4.951764,6.792670,4.532428,5.503114,7.497736,-8.071995,-4.177824,4.893074,-3.295887,8.184176,-2.540084,3.818162,4.341826,3.243371,-7.460207,8.804223,9.120483,-6.663509,2.085126,4.586985,-2.218067,-1.505314,9.882657,1.708837,-6.638845,5.175889,-9.559483,-5.045135,-8.143447,-1.073870,8.849831,2.968735,2.076326,6.660720,-4.897114,3.769205,-7.441574,4.502614,2.610493,3.616761,2.709527,-5.208939,0.377812,4.019543,-7.363260,1.484435,-7.668925,-7.489277,-3.694604,-8.889286,-5.052572,0.235212,3.292709,8.176167,8.641338,-7.869188,1.159467,-9.996694,9.539504,-5.659510,-4.271603,6.563583,-5.544616,-6.196237,6.042236,2.015371,-6.121730,7.430016,-5.857882,-0.037272,3.023228,-1.195828,2.647793,-8.546799,6.368460,-8.296350,-1.186705,-0.749354,-3.520449,9.385103,7.021959,8.514878,2.025456,8.147203,4.154643,-9.721647,-7.430052,0.231727,3.330136,-7.744473,-4.581593,-5.647090,6.709985,-5.319238,9.283778,7.590808,-1.100664,-6.383445,4.878789,4.870625,7.011210,-8.802142,9.556019,5.666809,9.222651,8.474572,2.168813,-5.734658,-6.653219,-3.812184,-3.161917,-7.255967,-5.608050,-3.549490,-0.209080,3.205379,1.895042,8.499657,4.942791,-5.041215,-2.998323,9.506159,5.226576,-7.775542,-1.438723,-7.696009,6.750433,2.131480,9.216621,6.670054,-8.150808,-6.736244,-1.188506,-1.048948,-1.102240,-3.819699,-4.867147,-9.291220,0.078790,3.797673,6.029546,-8.421562,-8.371836,9.476164,-9.286045,5.505783,2.584485,-4.174739,7.798142,5.686871,8.131531,-4.918426,5.518514,-0.341207,-5.163723,-0.208997,2.750696,-2.210058,8.696343,0.834608,-1.780275,-8.469488,-0.270406,-4.507751,0.987795,-9.469083,4.358692,-4.598116,1.216447,-3.274141,-7.354982,-6.994356,5.229726,4.414470,-0.709856,-5.701947,2.126959,-5.144978,-6.729480,8.698287,-2.388364,-5.181656,-3.007164,3.352019,8.289672,1.464474,-6.425024,7.334310,-5.970265,-1.147845,-5.816650,-5.684127,2.820415,4.573881,8.605398,7.514613,-8.608578,4.896652,-7.584657,5.339895,-7.584784,6.389239,-4.312701,6.490801,0.711448,7.825134,-1.993855,1.636308,-6.151099,2.853223,2.965526,5.025030,1.634006,4.362995,7.260597], dtype = "float32")#candidate|3458|(462,)|const|float32
call_3457 = relay.TupleGetItem(func_3139_call(relay.reshape(const_3458.astype('float32'), [3, 14, 11])), 0)
call_3459 = relay.TupleGetItem(func_3142_call(relay.reshape(const_3458.astype('float32'), [3, 14, 11])), 0)
func_2075_call = mod.get_global_var('func_2075')
func_2078_call = mutated_mod.get_global_var('func_2078')
const_3474 = relay.const([1.786174,-8.094162,7.343020,8.813557,6.443444,-6.369312,-4.274917,-8.422545,-6.049753,3.289604,4.872506,2.221240,9.339674,4.249093,2.896035,5.337125,-2.380465,8.309735,6.733660,6.501075,5.407842,9.624955,-0.826966,3.045521,8.924999,2.260299,7.927576,-5.212316,-0.888590,-4.618361,8.168695,-8.338148,3.638822,7.532449,0.627913,9.879965,-3.282939,-4.432376,-4.167872,1.651321,4.805031,-5.599216,1.046775,6.934535,-3.800588,9.220921,8.010051,5.308528,-3.430450,-1.881342,6.345280,-3.016410,-2.949528,-0.350714,-5.982059,6.343345,-1.695040,6.396405,-4.586230,-6.984651,-4.509202,-2.576620,0.906323,-8.625080,-2.238218,2.544843,-1.203071,-4.557190,0.719684,2.995385,-1.947840,5.931510,-3.210086,4.224587,7.611496,5.555579,2.080763,4.587761,9.471953,-2.991107,-5.001691,0.817280,7.989407,-9.871613,-4.481448,9.608087,-7.101363,-6.052683,7.902030,3.291124,5.639422,-4.650405,-5.327701,1.759750,8.841619,7.491815,-8.553899,-2.293764,-4.212672,-2.491971,-3.405694,-4.376720,-3.848726,5.118304,-1.451709,-0.052345,1.750614,-4.813022,-2.069967,3.754370,-9.279510,-3.557096,0.340407,-4.937959,4.242277,-7.973634,-6.994014,-0.759334,9.523094,-8.164080,-1.314126,8.188299,3.552646,5.656544,-3.649231,2.915567,0.064722,1.911040,-6.341816,6.166282,-4.707347,8.596864,-6.176209,0.898852,5.874406,7.869276,-9.056588,0.709427,-4.536350,3.464206,5.351019,6.905313,-2.642769,4.187941,4.761562,-9.558533,6.552301,-0.665740,4.115443,7.493413,-1.365928,-7.017553,-1.779681,-5.472183,-2.482167,1.528322,2.609706,1.624347,9.395509,-5.970446,8.136626,-0.879981,2.224263,-3.479307,-1.757660,7.354543,-0.924253,3.580912,-4.827129,0.287863,6.801053,-4.367371,-3.738558,6.875201,6.225087,-2.733411,-8.116697,9.843819,7.613779,4.495618,8.687225,-4.947290,-9.713944,-9.719590,-9.263896,-4.224362,-9.231729,-6.558061,-0.114815,-3.625142,0.998636,-3.663858,2.830740,3.822841,7.223666,-6.774204,-3.658039,-8.275664,-0.246273,8.193977,-9.543544,6.062990,-0.686901,3.412927,4.244598,-9.386601,-0.965095,-6.623759,-1.939496,7.681856,-1.436297,6.533376,-5.313515,-0.901537,-2.580811,7.441764,8.210796,-6.175471,-2.553480,-8.842468,4.769260,6.218435,7.885305,-5.559705,7.151894,2.017590,1.769454,-5.411520,-4.452849,9.061486,-5.160788,7.507694,1.168372,-7.212129,-0.813352,9.258126,3.153988,4.379003,-8.003459,6.598639,2.168780,-7.225564,3.900915,5.458843,0.498558,-1.637411,6.432835,1.948361,4.401745,8.387937,-1.756989,-2.310910,2.527592,-9.980449,8.812450,9.025770,-5.825928,9.766042,0.531487,5.983413,9.884023,-2.199284,7.164262,7.637662,8.739815,-4.217727,9.493599,-7.456220,7.343111,9.777132,-2.503950,1.005962,-2.912336,-9.740020,6.147876,-2.328185,4.726448,-1.872090,-8.994407,-3.077566,-5.955516,1.039301,2.311452,-2.091572,-0.853782,8.196263,-4.385974,7.850011,8.424110,-8.010829,7.868372,-0.169149,-8.496658,5.947619,-9.800009,-0.228778,2.700027,1.347945,1.306766,2.716819,1.032334,-8.704021,3.883775,-0.443028,0.670646,-3.902066,1.222189,-8.520957,8.198663,-7.742011,0.838521,-1.964508,-3.364992,8.167918,5.263953,2.588853,0.673206,-2.064888,0.060006,0.830793,-5.796926,4.631826,-2.375078,8.405136,9.722860,-6.196096,-0.308540,4.642136,-3.851245,1.050746,7.913240,-8.253241,-2.365579,-7.802918,6.299232,1.180049,3.129481,0.535334,-7.146934,7.018629,-1.151494,-9.527544,-1.876447,5.828950,-1.542169,-5.535980,5.576712,-8.661297,1.197720,0.637557,-7.085995,-8.001271,7.610595,-8.458180,-2.553802,1.000406,7.294153,-1.319660,-6.802672,-4.364182,-9.231871,-6.002420,3.705315,5.589818,6.298195,3.889321,6.821781,0.840142,9.375427,-7.407916,6.678054,-0.189076,9.122077,-8.954138,-2.217600,-1.437835,0.086283,-0.394770,2.770051,-6.788719,-6.425558,2.624570,9.397219,-8.302254,-8.064778,8.384283,-2.919859,-5.578858,-5.803020,8.508153,2.522438,1.809636,3.442838,7.043537,5.642572,6.982511,1.094528,-7.318066,-5.073829,0.760670,6.000825,-9.168460,-7.583013,-8.319430,-1.892822,6.587429,2.998882,-7.035665,-8.364057,-1.438663,1.317245,1.873455,-7.445198,-9.120713,-8.860457,9.133789,-1.658289,1.593881,-1.647206,5.442671,-9.629599,-4.778822,5.272807,-4.964690,-9.985415,8.943081,-3.610651,-2.608515,-7.081637,0.059462,-2.643984,2.723902,4.924788,1.190987,-8.514359,-0.743257,2.346836,-1.460035,5.700843,-1.255494,3.022825,-9.653252,-5.303436,-5.564673,4.214103,4.371665,-0.528738,-1.137979,6.832962,4.199558,-3.602407,-7.943232,-0.767573,-1.188277,3.292583,4.148700,-1.461677,5.018626,-3.174908,-3.525564,2.070859,1.060178,-0.724362,2.260180,6.712713,9.276267,-0.997338,2.723431,-2.136406,1.105390,-1.907913,4.357567,-2.310874,3.356009,-5.541743,-6.585373,4.055122,-6.960601,5.454529,-9.523655,-3.979204,-3.052598,2.322663,-0.939591,6.750493,-6.162642,-7.569216,-8.164290,-6.154745,-3.461663,3.137227,-4.841316,-1.485532,-0.355646,3.464395,5.388060,-4.148636,-4.609484,1.207839,-6.880470,-4.441034,8.096157,-6.704577,2.463026,7.302694,3.136251,-3.883724,-0.940201,-8.468570,-0.706450,1.713883,-0.415315,8.355271,8.468485,3.834853,6.922057,-5.874149,-9.329464,9.087106,1.945100,3.892346,7.958621,3.035837,9.871489,6.626740,0.161081,0.228249,-9.684594,-3.239971,2.013046,7.065773,-6.230659,9.298298,-6.404889,-8.601045,-8.337251,9.326861,-7.737198,9.712071,-7.844889,6.498502,7.716107,7.221502,-2.805382,3.058470,3.929149,-7.206020,1.800912,0.385249,-7.707206,8.631364,4.255549,4.932259,7.470208,2.924769,7.991315,8.732480,8.047575,-5.054321,3.605994,-8.743301,9.124916,-1.010678,-9.172262,-8.174823,5.757661,0.611500,-1.067777,-8.283467,0.481147,-2.143927,6.807662,0.608249,-6.636064,-8.659164,-0.715379,0.527805,5.707866,-7.422559,8.406083,8.676764,-5.639775,6.821434,0.640373,9.228386,-9.210235,6.116845,6.979769,-9.869800,-8.225792,6.697586,2.967699,-0.298437,-9.076398,8.272284,-9.581327,2.063421,3.410422,0.916663,-1.996240,-6.443171,-2.691474,-3.276605,-2.750345,-1.150015,7.674315,7.537516,-6.363989,-7.289418,-9.946320,-8.628870,-8.410599,-2.139347,-2.923910,-1.707465,-4.974465,2.317537,-2.169033,-1.671795,8.141046,8.534769,1.432735,8.706817,4.420638,-6.521547,0.557159,-4.498569,-5.221765,-3.058990,-9.574239,-2.916740,0.797138,-3.704545,2.107947,-6.287067,9.622340,-8.821115,1.293570,-1.210954,3.974297,-0.467476,5.942518,-8.498690,1.780254,-4.579170,3.113211,-5.641493,6.556062,-9.772992,-4.025813,5.678837,-7.969651,-4.802460,7.137042,-2.272384,7.654293,-2.321746,9.000297,5.879354,5.291165,6.576893,-0.607096,6.364454,-9.065085,-8.221118,-8.702114,-9.227565,0.583181,-2.903996,9.614875,0.376794,-4.667401,2.449412,-4.675175,-2.004613,-5.607004,-0.854850,-5.948346,-3.654354,1.140732,7.151684,-4.016821,6.250699,-8.496092,3.823369,-5.125733,-0.583800,-6.078722,9.849258,-9.207499,-4.831790,3.131803,3.437159,-4.064778,-1.142319,6.141764,4.698450,3.187576,3.257977,2.411141,4.454389,-0.118977,-0.968272,1.405602,0.513652,3.517886,-2.963056,6.217579,-1.664489,-6.864614,3.752990,-9.323218,3.714811,3.917241,4.099406,6.008114,4.213198,9.081896,-4.869961,2.647561,-3.732370,1.158742,0.739649,0.403474,-6.524419,-5.691014,5.099756,3.463619,-8.447253,5.595964,0.620245,-9.255652,-6.362037,-1.155521,-9.093021,8.052266,-2.198091,0.824275,3.676193,-0.119194,-0.958608,1.797974,5.767614,7.809225,-1.711536,-4.289949,7.197906,-1.868950,-3.419619,4.776798,-4.772448,3.998760,7.933695,-8.539817,9.650578,1.659922,8.553265,2.556450,9.015716,-9.049355,-7.146776,1.945766,3.027301,0.957838,-0.422436,-5.503217,0.732473,2.047389,-9.705471,0.617668,-9.659501,-8.689058,-6.681326,4.400044,-4.316250,5.918780,-8.500386,-2.839929,-4.651000,4.267303,-6.369072,1.066262,8.884304,4.768212,-7.007392,-6.542898,6.193031,-9.888609,-0.641325,5.396568,4.702256,4.951805,5.026652,5.025438,-5.178835,-0.400008,-4.761862,-5.730018,-3.199130,5.440632,2.833991,-5.881012,-3.360676,-5.426299,-8.022434,8.392708,-4.012558,4.934994,9.151378,8.254295,3.182224,-2.395575,3.969053,8.824622,-7.420794,-6.445254,-9.708735,-1.398043,9.040983,-9.634466,-0.064199,4.235363,-2.850863,-8.052695,4.192146,4.695328,2.928300,-4.593297,3.776254,0.158050,-1.544540,8.146218,-9.076554,-9.412712,-8.839481,3.359128,-2.013839,8.272588,2.795087,-3.837975,4.703074,2.741670,-2.462874,4.455726,2.919619,4.278451,-6.010670,9.431443,8.744831,-5.880000,-9.854768,-9.341283,-5.024231,9.336944,-8.811225,-7.948739,-7.956859,-5.001485,3.749532,-7.361402,-8.770653,-1.151983,-4.783666,3.414343,4.332868,5.262452,9.487476,9.653335,9.857415,7.708363,-6.681049,8.913348,8.818015,3.917557,1.850663,-5.240029,-5.417552,-6.921284,-0.365618,-5.708242,8.494685,1.935390,2.830227,-6.180007,9.415246,-0.980888,7.531406,-4.239477,-9.366458,5.298384,0.280543,9.949336,-3.036089,-3.545499,-8.874709,3.340757,-5.817419,-9.673764,0.086749,-1.053684,5.877654,-0.035269,-2.815754,9.271512,2.673510,-8.241224,-6.143157,-0.351566,2.416367,2.909182,3.186754,5.239254,5.216379,5.905256,-3.261945,-5.995789,9.568374,-8.835801,6.094566,-8.207605,-6.028396,-7.720159,-1.106190,-0.174216,2.212807,5.413514,-3.883878,4.999372,1.025643,-9.312506,-3.130829,3.439237,7.599133,-9.309033,2.778991,7.594247,6.005724,4.688905,-9.430181,-2.839475,5.762477,-8.258367,-4.371832,-2.017000,2.688236,-3.726365,5.023439,7.080741,3.963415,2.821579,-7.857739,5.832294,-0.285793,5.138582,-7.561429,5.725318,-9.477887,9.841282,4.758582,-7.206197,-5.011439,-2.063542,-4.679697,-9.115242,4.893449,-6.515413,2.057142,-4.864056,-3.822691,-3.810383,4.232448,4.137352,-2.238040,-1.617949,-4.999950,-4.604494,7.456880,-8.201411,-3.617402,-5.828742,-2.725593,5.304519,-8.442013,-0.008106,6.019398,7.642241,-5.070937,-4.442595,7.027184,-2.408277,4.881179,-0.074396,9.258129,-8.115634,0.718628,-3.836597,-7.040959,1.748139,7.304432,4.788677,5.628931,6.251552,4.917152,-2.303427,-4.902183,-9.084184,1.280190,4.757318,1.535137,-0.189824,-9.034409,8.228384,-0.824440,5.843861,-0.989054,-3.526457,2.805802,3.792721,-0.085066,2.223727,-2.026846,-8.497500,-9.471419,-5.598740,-7.070771,-7.090947,8.149865,3.073390,0.180882,2.994447,9.127410,9.724926,0.639544,-0.006078,-5.545028,9.169189,1.358740,-2.485040,6.314654,-3.424552,6.027576,-7.893582,-9.652832,-9.293272,-4.198654,1.584492,6.665736,-6.285365,9.121218,-9.482657,-6.171090,-5.800727,-0.388075,0.560807,6.188089,0.245741,-9.207751,-4.017686,9.765049,-5.052202,-3.728613,2.304817,-7.279268,0.222534,-0.267663,9.718187,7.498516,1.329879,-6.077761,7.305403,-3.487525,-7.271648,-0.841578,6.063404,4.891232,0.031018,5.834692,-5.547611,-0.668320,1.496506,2.910078,9.289241,-9.142260,-4.772659,2.840411,-1.464928,-4.071810,-6.227185,1.415619,-9.465552,-6.031772,1.402039,4.576691,8.840622,8.493904,-4.273896,-6.602703,9.710359,-7.403242,3.179148,7.750899,0.955041,4.369778,-3.981476,1.999774,5.459309,-6.709779,9.624968,-6.024654,2.349226,7.616217,9.334978,8.253283,-2.793378,-4.062042,7.357244,-3.342125,-3.859976,-6.555502,-8.016699,0.802938,3.464296,-4.826519,9.840648,-1.113537,-6.608055,7.407976,5.094541,-8.157586,-5.014040,5.463145,-6.735692,2.018177,9.509405,4.613325,0.309529,-4.141363,-1.141338,-0.240866,6.688991,-3.200762,-3.277408,5.692032,-6.352760,-1.379253,7.146698,-8.241579,1.083928,-4.049360,-3.361645,-2.663482,-1.549948,-2.975433,-1.388313,6.905924,8.308248,3.714150,1.305362,8.780369,5.867741,-9.857312,-1.448559,-6.162227,-5.190055,-2.759120,1.500548,5.374228,0.685115,-7.512207,-0.153106,-6.618417,-5.022501,6.670711,-9.300117,6.518261,-7.065472,-7.890544,0.490432,-2.151297,7.856277,-5.495983,-2.673696,4.333647,8.525111,3.138723,8.981071,-0.922083,9.020933,4.338201,-2.748184,6.115777,-4.806280,3.402840,0.680990,-8.080809,5.362050,2.035704,-9.097774,0.384625,-8.030689,5.463529,-0.744292,1.054053,7.566890,-8.797888,-9.271210,5.717359,6.672791,-1.649736,-6.367538,-2.496877,9.302198,3.618363,-5.838531,9.841791,7.461076,-1.950264,-7.138364,-7.104623,-8.440202,-3.483983,-1.098830,9.309605,-9.619867,-9.996988,-5.241732,-4.231693,-5.441917,4.136905,5.837287,-6.993184,2.938435,-5.993298,-1.443925,-0.468985,9.564853,0.254959,-6.434238,-7.330354,-4.864162,4.957250,8.976943,-5.290256,-3.661889,-5.098998,3.096745,-0.467100,9.293071,-1.318564,0.213336,-3.955962,9.846060,0.104789,-8.828857,4.673056,-0.265104,-8.958589,-0.453033,-5.960141,-0.177473,-2.269282,8.193366,8.782033,-6.840276,-8.252340,-4.623684,-5.702378,5.425725,3.449030,6.331709,-4.397922,9.940174,7.546802,-0.631582,-8.010379,-4.278663,-7.016603,-1.780704,-0.364352,2.538461,-6.690221,7.038914,-5.388360,-8.730057,2.973968,-2.798102,-2.303429,-9.838102,3.904157,2.067882,9.800251,2.605109,1.872161,1.347063,-0.452433,-7.054529,-2.837174,3.128436,-9.145956,-9.721945,-5.430578,-8.541772,8.652850,-1.533626,4.485713,-5.162169,-3.902595,-6.388908,1.644382,5.715137,-4.638131,6.320931,-8.028702,1.550197,-4.011976,-8.182209,-0.085049,1.737807,1.991757,7.127116,3.445135,0.573836,0.607750,8.426188,-1.414002,-7.884161,2.479512,6.891372,-5.746908,-1.618081,4.276960,8.296585,8.637963,7.274493,1.850036,1.864307,-6.831630,-7.952116,-2.007478,3.535747,-8.116547,-4.534149,2.418279,3.490230,-5.152465,-0.120035,-6.161321,-9.650832,4.900980,-7.803311,-4.971495,6.677640,0.723316,-3.003354,-7.661951,-1.030844,5.254286,-3.762900,-7.359200,-3.589746,3.435895,-9.725171,1.881754,-6.105975,-8.070548,0.740225,-4.791092,-8.150316,-7.699148,-2.179133,-9.735641,5.314834,6.603158,-5.136702,-5.427856,-8.076871,3.989936,8.201752,9.529447,6.968775,3.803796,-5.325532,-3.574487,2.642619,4.954025,4.730308,-4.453489,6.425797,-0.422390,1.096032,3.965538,-2.085681,9.989605,5.811989,6.131645,-3.354563,7.101227,1.995146,7.852161,-2.327191,-3.413548,-0.548947,-5.201366,-0.298228,4.344351,4.384675,1.344206,-8.946349,-5.761923,-9.247319,-8.384670,-0.186722,8.405090,4.535185,-2.794288,-1.890151,2.575291,5.275176,-6.622036,-8.770458,1.110821,-9.915728,-9.628014,0.893412,-0.206593,-6.160841,5.583525,-3.540310,-2.910021,1.308407,6.373324,7.636302,1.874789,4.301088,-7.237932,6.816756,3.744422,4.732423,-0.817991,-5.835486,-0.593241,-5.431312,6.777520,-0.722081,-4.117147,-4.049345,3.369571,7.744756,-1.586068,1.809023,-2.001086,8.619839,-9.965958,2.021227,9.262595,-3.127599,0.961488,1.234152,7.387658,-3.200689,-7.840775,-2.351397,5.614867,-4.985937,-6.336040,-4.519627,-6.291392,-4.459530,-8.043133,-2.788259,-6.263232,7.172843,0.524643,-8.806877,6.349383,-8.209082,-0.887195,4.271531,-3.659652,5.327468,1.530228,-5.095051,5.319873,6.246501,-4.113577,-9.475461,-9.458287,-8.246671,-9.302470,-9.243847,-7.916651,2.123057,1.987868,-7.108543,-6.042183,-2.613695,3.989065,-4.539029,-0.452845,4.024081,9.165625,8.298814,8.025047,4.375294,-4.958073,8.712240,-8.431847,7.993311,-2.344511,-6.092734,-8.122100,-5.471746,3.716393,-0.040281,-8.099650,-2.213449,1.288908,9.239507,-3.644487,8.113919,4.665840,9.158976,2.171082,3.572956,-4.889626,9.757122,5.738084,-5.447168,-5.351435,-4.151224,-9.155270,-1.342687,-5.626156,6.221339,-4.456031,0.709792,3.787513,5.042873,-7.199384,-8.287804,-6.020398,9.445722,-5.700182,-0.379331,-1.874207,3.908230,-3.577195,6.541171,-8.415566,4.053202,0.068818,-7.558696,9.380064,5.311530,-0.304825,-2.105042,3.350430,-3.638734,2.848353,-4.639890,3.801462,3.968465,5.186271,-8.961580,3.884199,-8.537968,2.537129,7.392879,0.490723,-0.757765,5.357102,-0.567645,-0.316614,-7.525620,-2.572537,0.700951,-7.861936,8.067320,7.547232,0.152517,4.643875,0.694783,-0.099801,5.863571,-4.525281,-2.626680,-3.151017,-8.530514,6.916366,-3.748731,-0.144113,-1.799418,-8.923024,-1.045795,8.100953,-8.051858,-0.282531,5.849754,3.283611,-3.157140,-6.501183,8.362387,1.834867,6.160292,-1.057424,-8.120420,-8.882465,7.543130,-1.466547,-5.315809,-1.136546,-5.027704,1.610454,3.755495,-5.003484,-6.746377,-5.076797,3.427524,7.843214,4.869666,6.885119,-4.367939,-6.572611,-4.361593,-3.404173,-4.514650,-2.231462,7.879051,8.603814,-3.380069,-9.944951,-5.061364,-5.366489,-7.786455,8.295912,2.555252,-2.835530,-8.858761,5.400545,8.480312,5.239796,-2.500974,7.351111,4.984974,4.162469,-7.675838,-8.722028,-0.014554,6.133161,6.009040,-9.613668,6.532320,-2.401096,5.738515,-2.223954,1.766403,3.859629,1.740052,8.758588,6.202529,-4.733947,-5.249446,-9.565162,3.682153,-3.219669,-9.162074,9.888739,3.319591,0.459303,-3.748796,9.766960,-1.284707,6.332529,2.658967,-6.430885,2.876099,9.609700,-4.735125,3.958023,0.754911,-6.061978,-2.253648,2.857315,3.906710,3.018962,-6.254616,-3.832161,4.999321,2.289137,-6.943662,3.465585,-3.974182,-5.675166,-4.306551,3.738721,7.908935,-9.284503,5.998339,0.027537,-6.342559,-7.682899,9.341066,8.873462,6.611124,-6.168216,3.814235,0.415121,-2.592957,-1.091743,6.540520,-4.239109,9.495256,7.024538,-5.008094,0.812319,8.681430,6.364011,-7.117090,7.673284,0.149094,-9.662125,0.533785,6.378912,1.894415,-3.367387,5.135719,5.634504,4.185802,4.539668,6.065325,4.855383,1.411345,9.613911,1.615805,4.829607,-6.741610,6.756091,8.622146,1.090265,-5.039170,-2.436007,-5.406068,-7.176585,-8.453495,9.914211,8.698985,-1.479290,-8.512531,-6.068550,-8.572746,-5.663897,4.865425,-2.762298,-0.937542,5.815939,8.032495,-0.344879,9.628286,-6.328060,6.068231,4.876064,-5.549110,5.070652,-7.461810,-6.842881,9.893535,1.893647,2.399014,0.263937,-3.099266,-8.181212,-1.933176,5.543053,-0.693723,5.727979,-0.300015,-9.962859,-7.264743,7.964972,3.888955,2.274668,-4.521797,-6.528903,-3.276880,-9.273947,-3.741206,3.115807,1.230980,0.618580,-4.565737,3.851256,6.626058,4.995527,8.461393,-9.354622,-8.304611,4.691587,3.163934,-2.666026,-7.995105,-6.413184,-5.115826,5.809441,-9.848589,3.236944,-3.735999,0.512827,-2.143225,2.216718,4.956687,-2.781976,-3.084780,8.177097,0.453885,9.109499,-7.466353,9.924206,7.887625,-7.244870,9.182977,-7.542644,3.626717,4.325714,-6.153251,2.861425,6.229942,-5.134393,-1.116317,0.834445,3.048546,4.172338,-8.855254,-9.449058,9.146371,7.478003,-8.596903,-5.394214,-8.009309,5.318736,8.962611,-6.978004,7.285594,-3.587018,-5.270711,0.976974,-4.045736,0.455739,2.027968,9.275336,4.341294,7.649043,-5.164850,5.336603,-0.191314,-1.561993,4.661994,-9.862840,9.233962,-3.943017,-4.501991,0.838265,-6.742332,3.505877,2.647256,4.892464,7.136349,-2.421863,-0.212499,-5.156802,1.899328,-3.132809,-2.838908,9.045087,5.709940,7.771937,7.362141,8.390785,-4.695897,-0.744471,0.533012,-0.708065,-4.882666,-7.798823,-8.742130,4.555829,7.782294,-5.392409,-9.359929,6.549437,-2.632445], dtype = "float64")#candidate|3474|(1890,)|const|float64
call_3473 = relay.TupleGetItem(func_2075_call(relay.reshape(const_3474.astype('float64'), [1890,])), 3)
call_3475 = relay.TupleGetItem(func_2078_call(relay.reshape(const_3474.astype('float64'), [1890,])), 3)
bop_3489 = relay.maximum(const_3474.astype('int8'), relay.reshape(call_3473.astype('int8'), relay.shape_of(const_3474))) # shape=(1890,)
bop_3492 = relay.maximum(const_3474.astype('int8'), relay.reshape(call_3475.astype('int8'), relay.shape_of(const_3474))) # shape=(1890,)
output = relay.Tuple([call_3449,call_3457,const_3458,bop_3489,])
output2 = relay.Tuple([call_3450,call_3459,const_3458,bop_3492,])
func_3501 = relay.Function([], output)
mod['func_3501'] = func_3501
mod = relay.transform.InferType()(mod)
output = func_3501()
func_3502 = relay.Function([], output)
mutated_mod['func_3502'] = func_3502
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3508 = relay.var("var_3508", dtype = "bool", shape = (7, 14, 4))#candidate|3508|(7, 14, 4)|var|bool
const_3509 = relay.const([[[True,False,True,False],[True,False,True,True],[False,True,True,False],[True,True,False,False],[True,True,False,False],[True,True,True,True],[True,False,False,False],[True,True,False,True],[True,False,True,False],[False,True,True,False],[False,True,True,True],[False,True,True,False],[True,True,False,False],[False,True,True,True]],[[False,True,True,True],[True,False,False,False],[False,False,True,False],[True,False,True,True],[True,False,False,False],[True,True,False,False],[False,False,False,True],[False,False,False,False],[True,False,True,False],[False,False,True,False],[False,False,False,True],[False,True,False,False],[True,False,False,True],[True,False,True,True]],[[False,False,False,False],[False,True,False,True],[True,False,False,True],[False,True,True,False],[True,True,True,True],[True,True,True,False],[True,True,True,False],[True,True,True,False],[True,False,False,True],[True,True,False,False],[True,False,True,True],[True,False,True,False],[True,False,False,False],[True,True,True,False]],[[True,False,False,False],[True,True,False,False],[True,True,True,False],[False,False,False,True],[False,True,False,False],[True,True,False,True],[True,False,True,False],[False,False,False,True],[True,False,True,False],[True,False,True,True],[True,False,True,True],[False,False,False,True],[True,False,True,True],[True,True,False,False]],[[False,True,False,False],[False,False,True,True],[False,False,True,True],[False,False,False,True],[True,False,False,True],[False,False,False,True],[False,True,False,True],[True,False,True,True],[False,True,True,False],[True,False,True,True],[False,False,True,True],[True,True,False,False],[True,True,True,True],[True,False,True,False]],[[True,True,True,False],[False,True,True,False],[False,False,False,False],[False,True,True,True],[True,False,False,False],[False,False,False,True],[True,False,True,True],[False,False,True,True],[True,False,False,True],[True,True,True,False],[False,True,False,False],[False,True,True,False],[False,True,False,False],[False,True,True,True]],[[True,False,False,True],[False,True,False,False],[False,False,True,True],[False,True,True,False],[False,True,False,True],[True,False,True,True],[True,True,True,True],[False,False,True,True],[True,True,False,True],[True,True,True,True],[True,True,False,True],[False,False,True,False],[True,False,True,False],[False,False,True,True]]], dtype = "bool")#candidate|3509|(7, 14, 4)|const|bool
bop_3510 = relay.logical_or(var_3508.astype('bool'), relay.reshape(const_3509.astype('bool'), relay.shape_of(var_3508))) # shape=(7, 14, 4)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_3523 = relay.TupleGetItem(func_2089_call(), 0)
call_3524 = relay.TupleGetItem(func_2091_call(), 0)
func_1326_call = mod.get_global_var('func_1326')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_3533 = relay.var("var_3533", dtype = "float32", shape = (800,))#candidate|3533|(800,)|var|float32
const_3534 = relay.const([2.790931,-8.479271,6.095933,-0.889959,0.437309,3.423392,7.681428,6.731873,2.717520,-1.704688,-7.006245,-5.073001,9.967198,3.911602,-7.466958,-4.549629,6.920786,5.342343,-0.292359,-9.499230,-2.893193], dtype = "float32")#candidate|3534|(21,)|const|float32
call_3532 = relay.TupleGetItem(func_1326_call(relay.reshape(var_3533.astype('float32'), [5, 10, 16]), relay.reshape(const_3534.astype('float32'), [21, 1]), ), 1)
call_3535 = relay.TupleGetItem(func_1329_call(relay.reshape(var_3533.astype('float32'), [5, 10, 16]), relay.reshape(const_3534.astype('float32'), [21, 1]), ), 1)
func_2627_call = mod.get_global_var('func_2627')
func_2629_call = mutated_mod.get_global_var('func_2629')
const_3554 = relay.const([[-6,-6,3,-10,9,-10,-5,-7,2,7,9,-9,5,-5,-1,3,-6,-4,6,5,-7,8,-1,-4,10,-10,-9,6,-7,7,4,7,8,-2,-5,-10,1,6,-4,-3,-10,-5,-2,-4,-2,8,10,-9,-5,5,-7,4,-2,7,1,-2,5,-1,-8,5,-8,7,6,-8,-8,-3,-5,-10,5,7,-9,6,-4,-10,-4,2,8,9,7,7,8,10,-6,4,-10,-9,8,3,-4,6,-8,9,-10,-9,6,4,-7,1,5,-7,4,3,1,6,9,-1,-2,4,-9,-9,-1,10,7,1,5,-6,4,-3,-5,8,2,-2,2,-6,-1,5,-8,-7,-6,-9,-8,2,-6,5,-7,-7,4,3,7,6,-4,9,-8,1,7,-7,-4,-5,7,2,-4,-2,10,6,-7,-7,-5,-7,3,9,5,-4,-8,-1,-10,-8,4,7,-7,3,-5,-7,7,7,1,9,-3,-6,4,5,-10,10,-5,8,-10,-8,-3,9,-10,-9,2,4,1,-8,7,10,-6,-3,-7,-5,-4,-4,-7,-7,9,5,-4,-7,-2,1,-8,-9,3,-5,3,-7,-2,-3,6,-5,6,4,-2,-6,-8,4,-9,-2,4,-3,7,3,-3,-10,6,3,9,3,-2,6,9,-6,4,1,5,-7,5,4,8,-8,1,-8,1,-4,2,1,-1,-10,-6,2,-6,-6,1,-1,-5,-5,10,-9,-5,-4],[-2,-8,5,-7,-8,2,10,-5,7,-9,-4,-1,10,-7,-2,3,9,6,-9,3,-1,-1,3,1,-9,2,-7,-10,-2,3,2,-9,-7,-3,7,-4,-2,-9,-9,7,-1,3,-4,6,-2,2,-4,4,-4,-8,4,-9,-4,-3,7,3,9,-9,-1,-8,5,-8,9,-2,9,-5,-1,1,-1,10,-4,-9,1,5,2,-6,3,7,7,8,7,-9,8,-6,4,-8,-1,1,-4,5,-2,-4,-8,-9,-10,9,10,8,9,8,1,4,-4,5,3,-7,-4,10,-4,5,7,1,-3,5,4,7,-9,7,-6,-1,-4,-4,1,-10,-4,-7,8,-6,9,-7,5,8,7,-7,-2,3,-9,6,-10,3,9,3,-1,2,-10,-3,-5,9,10,4,-4,-10,4,3,2,6,-7,3,-7,8,-4,-4,-5,10,9,-9,-2,8,-7,-10,6,-2,-6,-10,10,4,-10,4,3,1,1,-7,-1,1,-5,-6,-10,5,-3,-2,-3,-6,5,10,-5,10,-3,1,3,1,-6,8,-3,-3,-7,9,9,5,-7,-4,6,-10,-2,-2,-2,2,7,-3,2,-9,9,1,3,-4,2,3,-1,-6,2,9,-10,4,-10,10,-5,2,-4,3,-2,-6,-6,-4,-9,-1,10,-9,-10,8,1,3,4,9,-10,-3,-3,9,-9,-6,3,1,9,4,2,9,-9,-1,-8,10,5,2],[-4,7,2,-4,-3,10,5,-3,-5,4,5,-6,-6,-2,-10,8,3,-9,-9,4,8,-5,-8,-3,3,9,-3,-10,1,-9,-6,9,4,-6,1,-6,4,3,2,-6,-3,2,2,-4,-5,8,-2,1,-4,-1,-7,-3,10,2,10,-8,7,-9,-1,-3,-6,6,-7,7,3,6,5,-10,5,-1,-4,-10,-7,9,1,-6,5,8,8,5,1,3,1,5,7,-1,-2,-9,9,9,-2,-1,-7,-10,4,10,9,3,7,5,3,5,8,-6,-6,1,2,-6,10,-7,3,10,-1,3,-3,3,8,-3,4,5,6,7,-7,10,10,10,5,7,-4,-5,1,-3,8,5,-5,1,8,1,2,3,-9,7,-4,1,7,5,3,-4,1,-2,-2,10,-2,7,4,-8,-4,8,-9,6,-4,3,8,-10,-9,-7,-5,2,2,3,-7,1,-4,-9,-8,1,5,-1,9,2,-2,-10,-8,8,10,-5,10,10,3,-1,4,4,3,-2,5,-2,-3,-7,5,-8,-7,-3,9,3,1,-4,5,6,-3,2,-10,-4,7,3,-7,6,-6,-10,-2,-8,8,-10,1,-1,-2,-10,-7,7,-6,-7,-5,-6,4,7,-9,-9,-8,10,-4,-2,1,-3,8,2,2,8,2,8,10,-2,-10,-3,-1,-6,3,-5,3,3,-8,7,6,-7,9,-6,1,-7,-8,-7,-5,-6],[-4,3,7,-9,4,-6,3,-1,-1,3,-5,-10,3,4,2,-6,-10,-4,-8,-3,10,3,5,8,-2,-9,-1,2,8,-4,7,-9,-1,-4,-5,-9,8,-8,7,10,-7,8,8,6,7,8,-9,9,-9,9,1,9,-4,-2,-3,10,-1,-1,-10,7,-4,1,4,-5,4,7,6,5,-2,-8,-1,-8,9,-3,4,-6,7,-6,-7,3,7,-7,5,2,8,6,-2,-2,-2,10,7,8,3,-4,-5,4,-7,8,4,1,9,1,-10,2,8,-9,10,-8,9,5,-8,-9,-3,-7,6,9,3,-9,-5,-6,5,-7,-1,9,-8,8,-5,-3,6,5,9,-9,6,-7,9,3,9,10,-8,3,-5,-5,10,1,9,-7,-4,1,4,-10,-9,8,6,9,-9,1,1,-4,-4,-8,3,-9,4,6,8,-1,-2,7,9,1,6,1,9,-2,-2,-6,-6,1,-7,-7,2,3,9,1,6,5,7,-1,1,9,-4,8,10,-1,4,-1,8,-2,4,4,-7,-1,-4,9,6,9,-3,-1,4,-1,1,-7,-7,-3,-4,10,7,6,-4,7,4,-1,2,-3,5,7,7,-3,4,-7,5,10,9,-3,10,4,-5,3,8,-6,-10,-6,-8,3,-7,10,6,-3,-5,-9,-6,3,7,-1,-1,-5,-1,-8,-2,-4,-1,-8,-6,3,7,8,-4,-5,6,5],[2,-8,3,-5,-9,1,-3,7,1,-3,-4,2,-2,9,2,5,4,-8,-9,1,3,-8,-2,-6,-6,1,-9,-6,-9,-9,8,4,7,-10,-6,4,4,6,6,-1,2,-2,7,4,-2,-7,-8,2,-5,-10,5,10,6,5,9,-4,-8,-4,4,-2,-2,9,-10,-3,-5,-7,9,-8,-5,-6,-1,-9,-7,-5,-2,9,4,4,-9,10,-2,-4,6,5,-7,8,-1,6,-10,9,5,-6,6,-4,6,8,-3,-8,-4,-2,4,-6,7,-3,10,8,9,-4,-5,9,6,-9,8,8,10,3,-10,-7,1,-5,-1,6,-9,7,3,-5,-1,-8,2,1,7,-6,-2,-5,4,-4,3,6,-4,-7,-9,6,7,-9,1,10,5,-7,10,2,2,-8,-7,10,-9,2,7,6,-3,2,-8,-2,-10,-1,-2,2,-8,2,9,1,-9,4,1,2,8,8,8,-8,-10,9,-2,6,5,5,10,-10,9,4,5,-1,-2,8,8,10,-6,10,10,-8,-5,-9,-1,5,2,-7,7,-1,-9,-9,-8,7,-8,2,6,-4,-2,-8,-9,-2,-4,1,9,10,-4,6,-10,6,9,-5,-7,-8,2,-4,10,-4,-5,6,1,-3,-7,-7,-2,-4,-10,-8,9,-5,-1,-2,5,3,-2,-5,7,8,-6,10,7,-9,-4,-3,2,-2,9,1,-1,-5,7,6,7,-9],[-8,-9,2,9,4,9,-1,8,-6,-3,5,-9,-7,6,10,5,4,-2,-1,-4,-6,2,5,-7,-8,7,-10,8,5,1,9,5,1,4,2,-10,3,4,-1,9,5,5,-6,5,6,7,4,-3,-1,9,-4,-10,9,7,6,1,3,7,8,-1,7,-2,-9,-8,-1,-4,3,4,-9,-6,-6,-8,-1,-8,-6,3,-6,6,1,8,10,9,-5,9,-1,-8,-10,-7,1,1,-4,-5,-3,-8,7,-8,-7,2,9,5,-6,8,9,-8,1,-2,-6,-7,-9,3,2,-5,-8,8,-8,-9,6,-10,-3,9,-10,10,7,-4,4,-4,-9,-5,6,4,6,10,-1,9,1,-7,-9,6,6,-4,-9,9,9,-5,-7,1,-4,-7,3,8,-4,-6,4,10,-4,-2,-3,1,5,7,6,-5,-8,3,6,7,8,4,-5,-2,7,2,-5,3,8,1,-7,4,7,-9,1,-7,-7,-1,-5,3,-6,-3,-7,-2,6,1,-2,-9,4,-3,3,-2,-3,5,5,-10,-3,6,1,9,3,-1,4,-3,-9,3,-10,-2,-7,1,-5,5,-5,-9,8,2,-9,8,2,-2,-10,2,-10,-3,1,1,4,-3,-6,3,-2,7,9,-5,-7,-1,1,-8,-8,-10,-6,3,8,9,10,-9,-9,2,-2,-1,3,7,-5,-7,-8,2,-1,-6,-2,-2,-8,-5,-7,-7]], dtype = "uint8")#candidate|3554|(6, 270)|const|uint8
call_3553 = relay.TupleGetItem(func_2627_call(relay.reshape(const_3554.astype('uint8'), [12, 15, 9])), 1)
call_3555 = relay.TupleGetItem(func_2629_call(relay.reshape(const_3554.astype('uint8'), [12, 15, 9])), 1)
func_2883_call = mod.get_global_var('func_2883')
func_2885_call = mutated_mod.get_global_var('func_2885')
call_3564 = relay.TupleGetItem(func_2883_call(relay.reshape(call_3523.astype('float64'), [6, 9, 3])), 0)
call_3565 = relay.TupleGetItem(func_2885_call(relay.reshape(call_3523.astype('float64'), [6, 9, 3])), 0)
var_3570 = relay.var("var_3570", dtype = "bool", shape = (6, 9, 3))#candidate|3570|(6, 9, 3)|var|bool
bop_3571 = relay.power(call_3564.astype('float32'), relay.reshape(var_3570.astype('float32'), relay.shape_of(call_3564))) # shape=(6, 9, 3)
bop_3574 = relay.power(call_3565.astype('float32'), relay.reshape(var_3570.astype('float32'), relay.shape_of(call_3565))) # shape=(6, 9, 3)
output = relay.Tuple([bop_3510,call_3523,call_3532,var_3533,const_3534,call_3553,const_3554,bop_3571,])
output2 = relay.Tuple([bop_3510,call_3524,call_3535,var_3533,const_3534,call_3555,const_3554,bop_3574,])
func_3576 = relay.Function([var_3508,var_3533,var_3570,], output)
mod['func_3576'] = func_3576
mod = relay.transform.InferType()(mod)
var_3577 = relay.var("var_3577", dtype = "bool", shape = (7, 14, 4))#candidate|3577|(7, 14, 4)|var|bool
var_3578 = relay.var("var_3578", dtype = "float32", shape = (800,))#candidate|3578|(800,)|var|float32
var_3579 = relay.var("var_3579", dtype = "bool", shape = (6, 9, 3))#candidate|3579|(6, 9, 3)|var|bool
output = func_3576(var_3577,var_3578,var_3579,)
func_3580 = relay.Function([var_3577,var_3578,var_3579,], output)
mutated_mod['func_3580'] = func_3580
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_3600 = func_3004_call()
call_3601 = func_3004_call()
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
const_3628 = relay.const([6.096848,-2.804446,-5.365562,4.027321,1.348507,3.506130,-1.204007,-5.131286,-1.607601,2.894930,-1.294326,4.897805,-0.169414,-4.658902,-6.528954,-1.431655,-4.249464,-2.370654,4.515238,6.272792,-2.693071,4.563871,-2.080885,1.111156,-3.145271,2.491799,5.436268,5.624296,1.053183,2.284713,-0.763148,4.677617,-7.143129,7.114696,5.300995,6.415111,0.677155,-5.420020,-6.392977,-0.212687,-2.679691,2.411955,-2.042546,-8.985455,-2.747584,8.701161,5.945745,-6.292961,-5.216735,-2.813563,-1.459018,7.543835,-3.830921,3.824412,8.174581,7.114335,2.798458,-1.764016,-6.636617,-2.382119,-7.013982,4.840283,-8.607918,-7.665992,0.331968,0.493494,-3.718232,8.786555,-9.717691,9.951632,-6.548054,-9.196308,-6.713479,-1.144053,0.877577,9.359415,-5.045453,9.883529,-1.563108,-0.855186,-1.628207,0.481476,-9.142405,-8.808684,-7.644499,5.317839,-9.690641,-6.602456,-6.970038,9.607352,4.252924,2.574088,0.505557,2.717029,-3.282942,7.824014,9.173513,4.367185,0.250454,-9.297187,-3.494315,1.253850,6.379175,8.285272,-7.233103,8.406863,0.606612,7.927917,-5.715689,9.022852,-0.176861,9.508022,0.216090,-5.035519,-9.351615,-9.261251,-6.529478,-6.516302,-9.539140,3.079825,-9.618899,-0.709546,7.232445,9.238271,-8.041492,8.323002,0.187911,-4.830141,3.265076,-3.614683,-6.498148,-4.098582,-1.355251,-1.262691,-1.015949,2.944776,9.856224,2.765319,2.402128,-9.832669,9.202037,2.973428,-7.324054,3.678318,-3.910322,-0.360639,8.627190,2.668858,3.805855,-3.548463,9.519164,-1.451743,7.175522,1.157527,-1.381662,6.628862,6.721909,7.957357,-1.083743,-3.547450,-7.913545,6.970915,9.209999,5.992948,6.966943,5.149470,0.231543,9.467081,8.605614,0.345239,-9.820173,5.080351,8.777635,0.106772,9.114607,-0.725325,-5.428809,4.501357,-9.809375,-6.838451,-7.554766,-2.209313,-4.511483,5.306821,2.925490,9.529606,1.158878,1.261412,9.948001,-1.481139,-7.615439,-9.077748,9.150477,2.976035,-3.538407,0.918091,5.501453,-7.941315,4.651847,0.281133,1.224996,-8.889830,7.319342,1.071188,-3.622483,5.402488,4.603085,-7.417264,-2.272296,-2.567933,5.335242,9.437163,-6.311820,-2.780746,3.895226,-2.356894,2.353531,0.663471,-5.958240,8.150101,3.487287,-0.174646,6.389920,8.049794,-8.311722,-8.919529,7.749100,-3.813293,-3.226876,0.703699,-2.258916,-2.458771,-4.125494,-0.471229,-3.800623,3.482005,-1.653799,-9.798328,-4.390888,4.128504,-3.154615,7.835055,-5.945420,2.595240,-0.956208,-0.283421,-6.775445,-3.000654,9.948499,5.525540,5.185624,8.211898,-4.501672,2.617114,8.901604,8.518882,-4.858610,6.728527,-4.042838,0.061767,4.813803,9.120781,-6.440588,-4.383784,-7.755034,-5.782279,-1.701946,-2.364103,5.711229,-3.479997,-9.353711,-7.697477,-8.299701,1.725459,-9.521848,5.179803,0.433327,1.946777,2.291297,0.280018,-6.082066,4.533205,1.662253,0.324320,1.895481,9.994276,-3.834436,-0.499140,6.909827,0.056741,5.866515,3.001869,-5.510596,-1.340434,-4.933577,2.820294,2.938019,2.421299,-8.268356,-1.385263,-2.884163,-3.802444,6.885847,1.626923,-4.637232,6.817288,-3.407322,-4.949927,8.853442,-6.056860,-2.990265,-0.061217,-9.251226,-8.048766,4.779410,-1.802099,-4.186944,-0.593447,5.832112,-3.391386,-4.157421,1.965635,-0.403014,2.352146,1.054811,5.465457,-3.822608,6.783418,-6.519811,0.007394,-2.912203,3.492792,-3.576385,2.478599,-0.846793,-2.838994,4.623774,7.782492,7.669445,4.779553,-3.134532,5.823569,7.416590,1.338035,-1.279207,3.045783,-1.620935,-5.236964,-6.237571,-0.625785,0.390748,9.522124,4.856404,8.108466,-9.738590,5.189753,0.160550,8.404360,8.485383,-6.401985,6.489705,5.776257,0.271577,0.218563,4.823353,-1.851389,-1.354660,3.064465,-7.081330,-0.247167,3.647301,5.261356,-1.982185,3.254348,3.997560,-4.060307,5.295124,-7.485757,8.092637,-5.945367,5.795992,5.100326,9.795215,6.581050,7.041528,-6.039151,9.221467,-3.428265,-5.508158,-2.008459,0.998826,-6.672847,-6.996310,6.360961,-0.638875,-8.269302,-1.049008,4.507926,-4.329946,3.462455,1.406112,-1.321348,0.662657,-9.889128,8.812296,3.951189,6.136849,0.382101,-1.370004,1.634938,2.269749,7.200444,-0.609056,8.159257,3.931741,-9.730029,-9.618633,-2.994278,3.081755,2.175632,2.629187,-1.423289,-5.890436,-7.001034,-4.667986,-2.461899,4.734145,-6.637282,-4.072945,-9.780200,-3.467812,-1.740718,7.901577,2.098461,-5.683692,6.011838,2.874733,-2.059843,-0.475663,9.660215,3.998484,-8.519251,9.539470,-5.577171,-2.322235,2.108629,2.546361,6.311063,-1.244372,-9.831632,4.046360,-2.142219,8.721800,-4.048374,5.740493,-8.613089,1.566197,9.793661,8.473280,8.818524,-0.106549,0.939299], dtype = "float32")#candidate|3628|(462,)|const|float32
call_3627 = relay.TupleGetItem(func_3139_call(relay.reshape(const_3628.astype('float32'), [3, 14, 11])), 0)
call_3629 = relay.TupleGetItem(func_3142_call(relay.reshape(const_3628.astype('float32'), [3, 14, 11])), 0)
func_1641_call = mod.get_global_var('func_1641')
func_1646_call = mutated_mod.get_global_var('func_1646')
var_3639 = relay.var("var_3639", dtype = "float64", shape = (13, 10))#candidate|3639|(13, 10)|var|float64
const_3640 = relay.const([8.042480,9.267559,-9.183614,-7.485429,4.641229,-0.736000,-6.632191,0.561827,8.770799,3.693122,-3.305397,8.984316,7.197705,8.456244,9.660467,-9.325017,-9.349700,-7.614855,-0.373723,-3.502850,-0.250251,3.517522,3.218113,-6.032481,-5.347696,-4.599311,7.362094,6.631116,2.606101,7.192947,4.408086,-4.738946,4.236158,-3.020364,6.339427,6.428122,5.253726,-1.732116,4.482443,3.398564,-8.642869,5.183602,7.993700,-6.514047,8.078184,3.395853,-6.683986,-7.202768,-2.535785,6.558736,3.530608,4.011152,2.437998,-5.536812,-0.019431,-7.807620,5.648025,-3.994382,-5.872558,-1.128584,-6.412390,-4.871431,7.090676,-8.526417,1.822609,0.115590,-8.331705,3.287812,-7.608410,7.043731,4.313006,2.362883,9.909896,-6.853539,2.151170,3.031303,-5.521865,-1.676873,-5.177370,-3.535135,-7.110269,-2.626896,-2.475944,-1.978722,8.374095,-8.595877,-8.043197,-6.998837,1.245685,1.910613,0.838701,0.085499,7.145206,4.096512,-6.067710,1.056975,3.981217,-4.204751,-0.306723,-9.418723,-9.060791,-3.242404,-5.471607,-5.786905,4.910018,-6.384588,-9.051376,3.506209,4.774487,3.743257,-5.752016,-7.886317,-7.697425,4.630625,-1.263532,8.909224,-3.840352,6.834692,-0.390953,7.251562,3.210403,-3.083483,6.317332,6.403674,-7.903026,-1.525475,-2.304281,-5.199318,7.727103,9.134786,6.095481,-2.733544,-5.654658,-7.463961,3.872281,4.896651,-1.114465,-9.902600,7.738997,-9.269126,-2.128678,-5.587974,-1.158969,-3.862895,-8.828348,0.323726,-6.969526,-9.981615,1.414422,2.838558,-8.395857,2.206005,-2.162938,-2.931002,-0.580453,2.772194,3.675347,7.078965,-1.006640,-1.967414,5.323052,-9.604063,7.988639,-2.822786,8.119496,-0.197536,-4.149351,-1.867703,2.561393,-5.278865,-2.956873,8.876402,1.394353,5.694919,-9.301608,3.900214,5.681833,9.892442,-7.545895,5.385694,7.900909,3.920782,7.769701,-2.105315,-8.105758,-3.643407,-9.916764,-6.423876,-8.054125,1.833650,7.310984,-4.797327,-9.264253,-2.997095,-2.782055,-8.135164,3.604588,6.651793,-3.144383,1.878024,2.773547,9.354694,5.179689,0.329380,7.691140,-1.023190,5.563575,6.516744,-7.889658,-0.165072,3.272988,-4.810917,-5.078383,8.331078,5.847972,3.075930,3.293943,-1.624672,6.930984,-5.462555,-0.233627,7.615009,-1.670522,4.792193,-9.109761,6.278363,4.215511,-4.785743,6.952342,-4.508689,5.721446,3.525722,-3.486079,7.228978,-0.630681,-5.159948,9.796441,-8.628242,-1.812737,-2.167194,-0.089976,-9.152319,-0.596867,9.338842,-3.863473,-9.348512,-6.671181,-0.570616,-1.367559,-5.446264,-1.076030,2.013212,-6.143060,5.526309,-7.010313,-7.963064,3.704458,-3.777034,2.237898,1.424901,6.662115,5.870653,-7.469690,-1.861653,-5.340489,7.279683,7.927239,-7.474216,-2.017975,-4.305910,3.629759,7.087346,5.086652,-2.451221,-7.046070,-6.409553,-2.261060,9.968170,-0.889509,8.278628,-9.412640,9.941897,1.552076,6.280912,4.436652,-6.543232,-8.258351,3.175509,4.488986,4.481203,3.938003,9.472124,8.156112,-9.480812,-6.800078,-0.161936,-4.281207,-1.644389,9.243917,-5.988753,3.668815,-8.333286,-7.011387,8.909002,3.398515,1.422274,3.076611,-9.185614,0.180007,-4.318133,-9.882331,-3.125085,-0.992604,3.944283,6.973529,-3.816406,-0.824967,-5.499261,-8.609414,2.131438,-9.916278,-2.900396,3.028367,0.851766,-4.785280,2.611823,-4.920710,1.316874,-1.675010,1.822257,-2.465795,7.173331,-1.279944,-3.530831,8.231411,-2.935096,-0.225252,5.268347,-9.557165,1.742251,-4.246134,8.849313,-3.323374,1.853642,5.841528,-8.646288,-6.057562,0.076219,-0.841105,3.417372,8.033051,7.664676,1.960225,2.018036,3.695600,-7.329856,5.176232,3.839509,-5.941451,0.251946,1.216340,-8.493728,2.187114,-6.174926,2.276797,7.495381,3.714299,-1.938848,-5.603812,-9.117848,-8.736058,2.266563,7.352205,-0.516171,-7.266358,1.364724,5.792959,3.641375,1.825218,-3.202808,-6.991286,8.901173,4.875702,-6.915916,-6.395590,8.044370,1.622109,-4.325469,0.944668,-2.442649,-8.821632,5.997610,9.254550,-3.432989,-5.441332,8.262085,0.444505,1.649108,0.026890,-4.025569,-2.441654,-2.336442,-6.280256,-9.977138,1.715342,4.593362,3.094428,-7.891583,-6.094577,9.201707,7.779704,0.150066,-6.086050,1.603429,-0.845819,6.708305,-1.716147,-1.913795,-2.630155,-7.114126,5.960709,-9.590509,0.808518,-6.696092,8.017512,-6.386036,-0.514495,7.660734,-1.588277,-5.619481,-0.770466,-6.244147,-5.952647,-3.418733,9.831890,-1.784321,-7.152090,6.892356,4.154137,8.677336,-6.000957,-6.550154,0.461507,1.886198,-9.795498,-8.967331,2.114468,5.141269,5.880976,-6.499619,0.691447,-8.473322,3.276849,3.943456,6.737443,-8.423256,-8.851762,-9.996845,-9.564532,-8.508133,-3.331723,-0.935782,5.373156,1.243813,4.416201,0.392299,-9.188425,-7.394378,-6.398832,6.802296,4.736390,9.378557,-5.113099,9.532338,8.841403,9.953323,7.261429,0.739856,-0.443621,6.066367,-9.005481,-5.443078,-3.983890,9.266657,-4.119006,-9.501136,-3.410392,3.200640,-7.269005,4.875952,-4.406180,9.720691,-8.226819,-3.594184,9.024814,-0.443355,0.519516,-2.763709,-3.282031,-6.819763,-2.843812,-8.190252,-8.227448,1.261396,-4.395063,-1.381577,-9.866245,-2.755114,-7.476408,7.324129,0.869632,9.755245,-9.301176,-9.030248,3.125878,0.834909,-3.648896,-9.662136,3.273367,2.498572,4.209562,9.007247,7.170808,-7.723355,-2.839698,7.595024,-8.065090,-4.980314,-3.129973,8.461207,3.119283,-1.296530,-1.701832,-3.264353,-5.777766,5.816580,0.702996,8.016381,9.809976,-6.956226,6.671568,5.134719,0.169493,-6.975277,-3.697803,2.440641,-1.603508,9.693510,0.699172,0.202496,3.903632,8.235278,1.214880,4.081108,-6.172154,-9.698862,4.154371,1.483559,-3.666915,7.299533,0.539718,-2.195644,-1.895286,-3.857674,-1.375835,6.659611,9.420747,-0.961598,-4.700894,5.541851,-3.480927,-9.055631,6.453043,-9.502677,-9.106802,-9.693439,-4.604306,9.613906,1.489291,-8.738467,7.338598,4.498420,-0.557282,6.392722,-7.859982,-4.595452,3.827268,-2.792643,-9.697677,-7.762010,-9.057459,9.641748,8.913522,9.401539,-4.645777,-0.138770,-7.335211,-1.209009,-7.471119,0.050495,-5.604288,8.941302,-2.903321,-8.814372,-6.406599,4.777156,-5.217577,5.296147,-0.770428,-6.314357,2.489325,-7.044699,-7.137965,-6.455932,1.254035,5.378699,8.964278,6.453799,0.459107,3.897170,-3.699636,-3.886427,7.111485,-9.126478,2.432031,-3.088920,-2.377809,-4.099792,-8.102011,5.400892,-4.442339,8.633894,3.222053,7.073476,2.050156,-3.166426,-3.066728,-3.389045,-2.858017,4.345499,5.086744,-9.533850,-8.435054,-7.087046,-6.804035,-2.091671,2.877629,-0.342982,-3.573251,3.394299,-5.026597,8.681053,-1.864060,-3.058636,4.785893,-8.728437,-0.661775,-1.462756,5.361045,3.394034,-7.901644,-8.703945,8.180977,-2.584695,7.609940,0.105694,7.514166,-3.374799,-0.912083,-4.076694,-7.061575,-0.196511,-5.525069,8.615589,-9.324798,3.485892,8.068914,-8.031543,-5.251436,-5.302247,-3.565407,-5.803575,6.600300,9.529280,8.002750,5.593013,4.063931,-7.287180,-2.799595,2.970012,-1.148848,8.715296,9.278905,6.554185,-1.373681,6.182937,7.418831,-4.501499,-4.719711,4.718605,4.785595,9.699041,-1.779417,-2.000024,2.267970,6.254919,-7.913607,5.114684,-4.345523,-7.605561,0.078746,8.983793,2.880479,1.531502,-0.347573,7.130412,7.425923,-4.253177,4.397965,-2.467194,-0.425048,-3.698753,-7.045973,-4.234275,-3.648027,0.711846,-5.937078,2.399010,-6.656036,8.962229,7.833502,-1.494077,5.974636,-4.637684,-5.793037,-7.315520,1.137234,7.726245,-9.772023,-1.565862,-2.022388,-8.409624,6.249893,-1.037624,-4.273035,-1.581678,7.403139,-9.049774,4.501667,2.414081,4.394033,-1.000981,-5.536305,-6.933637,-1.645041,-1.290722,-1.486906,3.858070,-5.469038,8.115032,-7.275195,-7.266707,3.918982,-5.317450,9.777547,-4.438794,7.280369,7.416671,-6.700061,4.708494,1.955192,-4.250445,-1.134799,6.517287,4.664132,-1.706217,-1.307571,5.979564,4.714742,-4.692336,8.966606,-6.008280,8.839062,1.839032,6.594234,-9.106679,-0.802313,7.917253,8.624962,1.736598,0.097705,-8.119567,-4.833958,4.445361,0.839701,-4.997599,-9.067269,-3.345356,2.772331,-6.445829], dtype = "float32")#candidate|3640|(800,)|const|float32
var_3641 = relay.var("var_3641", dtype = "float32", shape = (21,))#candidate|3641|(21,)|var|float32
call_3638 = relay.TupleGetItem(func_1641_call(relay.reshape(var_3639.astype('float64'), [13, 1, 10]), relay.reshape(var_3639.astype('float64'), [13, 1, 10]), relay.reshape(const_3640.astype('float32'), [800, 1]), relay.reshape(var_3641.astype('float32'), [21,]), ), 2)
call_3642 = relay.TupleGetItem(func_1646_call(relay.reshape(var_3639.astype('float64'), [13, 1, 10]), relay.reshape(var_3639.astype('float64'), [13, 1, 10]), relay.reshape(const_3640.astype('float32'), [800, 1]), relay.reshape(var_3641.astype('float32'), [21,]), ), 2)
output = relay.Tuple([call_3600,call_3627,const_3628,call_3638,var_3639,const_3640,var_3641,])
output2 = relay.Tuple([call_3601,call_3629,const_3628,call_3642,var_3639,const_3640,var_3641,])
func_3648 = relay.Function([var_3639,var_3641,], output)
mod['func_3648'] = func_3648
mod = relay.transform.InferType()(mod)
var_3649 = relay.var("var_3649", dtype = "float64", shape = (13, 10))#candidate|3649|(13, 10)|var|float64
var_3650 = relay.var("var_3650", dtype = "float32", shape = (21,))#candidate|3650|(21,)|var|float32
output = func_3648(var_3649,var_3650,)
func_3651 = relay.Function([var_3649,var_3650,], output)
mutated_mod['func_3651'] = func_3651
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2814_call = mod.get_global_var('func_2814')
func_2816_call = mutated_mod.get_global_var('func_2816')
call_3653 = func_2814_call()
call_3654 = func_2814_call()
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
var_3656 = relay.var("var_3656", dtype = "float32", shape = (15, 9))#candidate|3656|(15, 9)|var|float32
call_3655 = relay.TupleGetItem(func_560_call(relay.reshape(var_3656.astype('float32'), [15, 3, 3])), 0)
call_3657 = relay.TupleGetItem(func_563_call(relay.reshape(var_3656.astype('float32'), [15, 3, 3])), 0)
const_3658 = relay.const([[[3.094589,-5.815430,1.306312],[4.062936,1.202334,8.553664],[-5.282212,1.083545,2.966820]],[[8.462966,-1.799965,8.309402],[1.733244,-2.600854,-6.437060],[8.884021,7.647615,-2.993922]],[[-3.526748,7.683077,-1.113305],[5.477373,-8.369654,-8.391583],[-0.814319,0.195486,-5.242174]],[[0.928207,-4.240654,0.179336],[2.043802,7.119815,0.317868],[4.408320,6.410809,9.193640]],[[5.379473,-5.244579,8.083290],[-4.763181,-8.530949,6.303724],[-8.765994,1.239309,-6.814089]],[[-3.772491,9.081993,-1.049773],[9.775190,-6.143901,-6.483811],[-4.780182,-5.389082,3.571136]],[[6.788373,2.653951,9.817753],[-9.419445,1.523175,2.660596],[1.373674,9.493881,5.664268]],[[2.812481,3.518679,5.298224],[6.865291,1.045523,-2.029210],[-5.469875,-9.537467,-8.537013]],[[-7.889877,-2.188941,-0.754309],[8.300769,2.977252,-5.315531],[8.850480,7.996601,1.019601]],[[-0.202694,-6.115673,-7.890833],[1.184508,4.285437,-5.830406],[7.141407,-2.272798,-9.431442]],[[1.835175,-3.019218,-5.612210],[2.307926,-5.852041,-4.835647],[8.183376,4.707708,-2.582827]],[[5.976642,-1.836709,-3.844612],[-1.528423,2.473002,2.148347],[7.504015,6.560519,3.630558]],[[-8.939947,9.969289,0.024677],[-4.748164,0.799403,-5.259099],[8.476056,4.239178,-3.025638]],[[-7.045671,3.032824,-3.489684],[7.438217,-1.820056,6.584878],[-2.842931,-2.502285,1.072772]],[[8.240804,8.277154,9.795752],[-5.803956,2.088443,-7.940208],[7.448323,-2.445125,-5.719875]]], dtype = "float32")#candidate|3658|(15, 3, 3)|const|float32
bop_3659 = relay.less(call_3655.astype('bool'), relay.reshape(const_3658.astype('bool'), relay.shape_of(call_3655))) # shape=(15, 3, 3)
bop_3662 = relay.less(call_3657.astype('bool'), relay.reshape(const_3658.astype('bool'), relay.shape_of(call_3657))) # shape=(15, 3, 3)
var_3666 = relay.var("var_3666", dtype = "float64", shape = (6, 9, 3))#candidate|3666|(6, 9, 3)|var|float64
bop_3667 = relay.floor_mod(call_3653.astype('float32'), relay.reshape(var_3666.astype('float32'), relay.shape_of(call_3653))) # shape=(6, 9, 3)
bop_3670 = relay.floor_mod(call_3654.astype('float32'), relay.reshape(var_3666.astype('float32'), relay.shape_of(call_3654))) # shape=(6, 9, 3)
output = relay.Tuple([var_3656,bop_3659,bop_3667,])
output2 = relay.Tuple([var_3656,bop_3662,bop_3670,])
func_3671 = relay.Function([var_3656,var_3666,], output)
mod['func_3671'] = func_3671
mod = relay.transform.InferType()(mod)
var_3672 = relay.var("var_3672", dtype = "float32", shape = (15, 9))#candidate|3672|(15, 9)|var|float32
var_3673 = relay.var("var_3673", dtype = "float64", shape = (6, 9, 3))#candidate|3673|(6, 9, 3)|var|float64
output = func_3671(var_3672,var_3673,)
func_3674 = relay.Function([var_3672,var_3673,], output)
mutated_mod['func_3674'] = func_3674
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3676 = relay.var("var_3676", dtype = "float32", shape = (8, 1, 13))#candidate|3676|(8, 1, 13)|var|float32
uop_3677 = relay.exp(var_3676.astype('float32')) # shape=(8, 1, 13)
output = relay.Tuple([uop_3677,])
output2 = relay.Tuple([uop_3677,])
func_3681 = relay.Function([var_3676,], output)
mod['func_3681'] = func_3681
mod = relay.transform.InferType()(mod)
var_3682 = relay.var("var_3682", dtype = "float32", shape = (8, 1, 13))#candidate|3682|(8, 1, 13)|var|float32
output = func_3681(var_3682)
func_3683 = relay.Function([var_3682], output)
mutated_mod['func_3683'] = func_3683
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3687 = relay.const([[[-5,-7,9,-2,-2,-10,7,10,7,2,6,-10,-2,9],[-5,3,1,-2,-9,7,-1,-6,2,-6,4,5,-7,-4]],[[-5,-2,3,10,-5,-4,-9,8,9,-10,1,-4,-3,-4],[5,9,10,-10,-9,7,-5,2,4,-5,3,-6,3,-9]],[[8,-7,3,2,-1,8,-5,6,8,5,8,-6,5,-7],[-3,-5,4,-3,1,-2,-2,-2,7,-6,-8,10,-10,8]],[[10,6,-4,2,4,-4,-5,-7,7,1,-9,-3,-7,-4],[-9,2,10,1,-8,3,-10,-9,3,1,7,-6,-10,-3]],[[1,-2,2,8,-2,7,3,2,-6,10,8,9,-5,10],[-5,-10,2,7,-8,7,5,9,-5,3,3,9,5,5]],[[-5,5,9,4,-1,-7,-7,8,10,2,-10,5,10,-5],[1,7,6,-6,1,-6,3,1,8,6,9,-3,4,-2]],[[-1,-9,6,10,8,-7,-6,-1,-6,2,2,-4,-5,9],[3,4,-10,-8,-9,-10,-4,5,-10,2,-9,-2,2,3]],[[10,-9,-5,1,-5,2,9,10,9,-5,2,-6,2,3],[3,3,9,-10,-2,10,10,-1,5,2,7,-4,-7,-9]],[[8,4,9,5,-7,4,6,9,9,-4,-9,8,-6,-4],[-3,-3,-8,-10,-4,7,-2,5,5,5,-1,-8,-5,-8]],[[-9,3,7,2,-3,-2,-9,-10,-10,-10,-6,10,-4,-2],[7,10,-4,9,-7,9,-3,-8,-2,5,3,8,10,9]],[[-6,-3,-2,-10,-5,10,-10,-3,9,-7,-10,-2,10,2],[-8,6,-3,9,-3,2,8,2,-8,-2,8,10,2,1]],[[-2,1,-6,-5,7,4,3,-10,7,-8,8,-4,9,-2],[-7,-4,8,10,4,2,-9,3,-4,2,4,-6,10,-7]],[[-5,-2,4,3,3,3,-9,9,5,10,5,-9,-2,3],[5,4,1,-2,4,-4,-9,4,-5,-7,-7,8,-9,-2]],[[3,4,5,10,4,10,7,4,-4,5,-9,10,9,9],[6,-8,7,7,-10,10,8,1,-6,5,-1,-9,-3,8]]], dtype = "int16")#candidate|3687|(14, 2, 14)|const|int16
var_3688 = relay.var("var_3688", dtype = "int16", shape = (14, 2, 14))#candidate|3688|(14, 2, 14)|var|int16
bop_3689 = relay.equal(const_3687.astype('bool'), relay.reshape(var_3688.astype('bool'), relay.shape_of(const_3687))) # shape=(14, 2, 14)
func_3192_call = mod.get_global_var('func_3192')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_3694 = relay.TupleGetItem(func_3192_call(), 0)
call_3695 = relay.TupleGetItem(func_3193_call(), 0)
func_3210_call = mod.get_global_var('func_3210')
func_3211_call = mutated_mod.get_global_var('func_3211')
call_3698 = func_3210_call()
call_3699 = func_3210_call()
func_2426_call = mod.get_global_var('func_2426')
func_2430_call = mutated_mod.get_global_var('func_2430')
const_3701 = relay.const([[-7,-5,4,-7,-9,-8,6,-7,4,-2,2,-9,9,-2,5,-7,6,-1,6,-9,4,5,-5,-10,2,-8,-4,-3,-9,2],[-2,-6,2,3,7,5,1,-5,6,-7,-9,-3,4,-6,2,6,-6,4,-2,-6,-9,2,4,-10,3,7,4,5,-7,-10],[-6,4,-1,-9,-7,3,9,10,3,4,-5,9,2,-7,4,1,-6,-3,-5,-1,1,-10,9,6,10,-1,-2,6,4,-4],[-3,-2,9,-5,10,-9,-9,-1,-9,-4,6,5,6,3,-3,2,-3,-6,-10,9,8,-10,6,-9,10,-5,-9,-6,10,-6],[-6,10,3,-2,-8,2,8,2,7,1,5,4,6,10,9,10,4,-7,-5,-1,-1,-8,-7,2,-2,-9,-9,-10,5,1],[-5,1,1,8,8,-1,-2,-7,9,-1,2,-5,-5,8,-4,5,-1,9,-6,-10,-6,-3,-7,-5,10,7,-6,-5,-9,2],[-3,3,5,6,8,-6,-4,-3,9,-1,-4,1,3,10,10,-7,8,8,1,5,-9,-4,-9,-8,-6,7,7,9,-3,-4],[-2,-7,9,4,-9,-9,-9,1,-1,8,6,-7,-3,-5,-7,9,-7,10,2,-6,-2,-7,-10,-10,-7,-2,4,-8,-8,-3]], dtype = "int64")#candidate|3701|(8, 30)|const|int64
const_3702 = relay.const([-9.432225,4.505399,3.363095,6.244458,-7.114153,-4.881259,7.574366,4.645315,3.921825,-7.327839,-4.575393,-5.967266,0.552967,0.749462,9.074809,9.541080,5.659464,3.379326,-9.004852,-1.800415,0.479823,0.635251,-6.745828,-5.705763,-1.457876,4.231007,8.574312,5.056115,4.434840,9.859576,-9.525201,-9.127459,6.663955,-0.383376,1.710324,-8.973017,6.995832,5.826941,-6.497770,0.539607,4.674997,-7.845154,-8.183892,0.785553,-0.183685,-2.908416,9.746118,-2.319005,9.928526,-7.113529,-9.325911,3.390462,-9.555056,9.720070,-8.919476,-3.128234,-2.908582,-9.245036,-6.455948,-9.458139,-4.320837,1.157623,0.616617,-7.879464,-6.897531,7.444874,-0.875190,-5.183308,-2.502519,6.674575,-4.263144,-3.713435,-9.871030,-0.164811,-7.252682,-7.146255,9.798996,2.908553,3.057993,3.537577,-9.593327,-3.217278,0.782411,-1.611868,2.288541,-3.191408,1.105928,-0.389404,9.095790,-2.084109,8.243246,-0.557927,-8.378076,9.934767,-7.414091,9.853477,-0.677165,6.670683,-8.664565,2.244929,2.211730,7.189772,-0.178839,6.802505,-5.258856,7.980522,-5.392820,5.808294,0.934350,-7.708343,7.008668,3.439962,-2.574115,-3.780870,-3.368907,-8.090567,4.891691,-9.293773,9.958782,-9.718715,0.392129,9.247314,2.850156,-9.343545,6.528949,-2.721377,-5.575960,-0.077821,-2.012457,1.019931,-4.237392,6.429859,1.268874,6.888836,4.206214,5.409664,-4.306535,-5.413499,2.311023,-0.123131,0.845366,0.163552,-8.794316,-1.489900,-7.957675,3.854903,5.975828,8.023827,-7.525775,4.146378,-3.400036,-2.305307,6.485004,-7.968265,6.852475,-0.813961,-0.368228,-2.097518,7.965982,2.447025,-5.292635,7.879707,9.138689,6.611394,5.005409,4.289174,6.406551,-5.207866,-5.966832,5.972212,-2.925335,2.452023,7.442114,2.724036,-9.832434,0.817031,-7.726683,8.599621,1.312037,1.826285,1.484616,-9.039126,8.065232,-8.224563,9.693396,7.075053,2.929712,-2.374123,7.709097,7.435580,8.686049,-3.632707,2.901523,7.444250,-5.120906,-9.659382,-1.668258,-6.632125,4.786336,5.001996,-8.687591,-7.000050,4.791580,1.177977,2.015020,1.679460,6.492050,-0.774709,8.812201,9.227683,-4.111865,4.224768,-3.109301,-1.796375,-9.713245,-9.433589,6.656176,-1.642016,-5.866777,8.751904,5.783116,-3.727635,-3.241806,1.938458,-1.904685,-9.235125,-1.694236,7.177321,8.360766,1.406232,-0.215331,3.032313,-8.650802,-6.541679,8.670577,-3.374382,-8.571887,3.354381,3.677916,-5.154359,0.359960,8.971828,5.005005,-9.260251,-2.625953,-2.904702,5.222030,-3.477928,-5.446746,-6.272425,-2.715954,-9.652563,0.621049,-2.105125,-5.141221,1.010010,9.967243,-0.395654,9.575268,8.062200,-0.303754,-4.459003,1.651095,1.074124,-7.097001,5.333785,8.984053,6.947569,9.014827,8.774872,5.442993,8.294919,8.518078,0.347069,-4.308073,6.269571,-2.894186,7.872594,-9.373250,6.990342,-3.179342,-5.059549,-6.862742,3.492910,1.786757,-2.213382,0.439881,1.250198,7.769414,7.622946,1.361443,-8.397244,0.630293,-1.690989,-4.800240,-6.008358,-4.560391,-7.197557,-5.896007,5.197030,2.127316,-5.084306,4.672007,6.408228,-9.019559,6.369167,6.934223,-0.691342,3.120090,3.648854,-8.547229,-6.814618,-0.583596,-4.368764,-5.519067,-0.149910,5.148978,-0.025972,-4.635699,3.100490,7.523867,-5.557290,-5.175223,7.362592,8.523264,4.798027,-4.077369,7.130283,1.904271,9.620664,9.148655,8.627594,3.747728,8.311746,1.959319,-8.104321,9.965856,-3.353602,7.819377,3.940964,-1.328873,8.618250,5.743913,7.915479,-8.676116,-7.853172,-7.479097,-0.057883,-1.170978,9.322109,-1.571036,-4.860587,-8.981503,4.606663,-4.935026,4.487517,5.943299,3.408128,2.166042,4.752170,5.365310,2.659418,4.657629,7.257207,7.228620,-1.259451,9.254926,-6.096082,5.472893,4.183815,-9.958569,-2.464880,8.233601,-6.368234,-6.462890,-2.500175,-8.411284,8.719569,9.197645,0.734308,2.308951,-4.271585,-9.858889,-1.103090,-2.229472,5.920849,-3.647886,9.874901,7.542346,-0.899424,6.587641,8.070400,-0.246660,-3.505333,-2.400649,7.603879,9.849845,-1.300024,-2.192061,7.686766,-3.281754,8.097043,-1.458144,0.776394,5.604169,9.800589,-1.698341,-5.478823,5.663686,5.915844,-7.261511,1.376165,-9.525674,0.303083,-2.095884,-9.313744,8.628414,-3.657684,-1.150413,5.131404,5.070366,-7.217882,5.228598,8.248834,5.257642,-5.693184,1.285714,8.211364,9.574980,-3.605242,3.961483,7.662391,-1.632751,-9.252936,1.792815,-7.703623,-7.510813,-8.080412,9.669868,-1.469760,-1.900452,-5.961536,-5.592933,-3.444722,-4.642090,-3.987957,1.831343,-5.531560,4.911502,-6.995297,-4.007914,7.645516,1.526028,4.477245,4.498919,-1.129020,-1.095127,3.977279,-8.794694,0.005974,-7.641598,6.745429,6.527426,-9.801276,-7.594244,7.933294,3.113659,-3.881633,-4.897491,-6.439891,7.828234,-4.179637,8.594742,9.250054,8.034683,0.309000,-8.414893,8.525084,-7.869192,-2.452170,-4.782944,-2.420492,-6.478852,-0.758940,-4.229457,1.980168,3.124566,0.559802,2.638059,0.062358,9.950592,4.078182,1.594910,1.021489,-4.224977,-9.592763,6.059554,-3.314138,9.168809,6.298877,0.927858,-5.857529,-2.056324,-4.058699,-8.791631,-3.029894,-5.507009,2.862879,-8.713317,2.350002,-0.802514,5.661413,-7.729760,8.515490,-8.014772,5.981781,5.528401,7.349193,-1.654612,-5.853208,7.853664,-5.550176,-7.050251,3.456046,1.478679,4.925422,-6.338027,8.720900,-7.057020,9.501831,8.356750,6.431392,-3.039384,-4.084032,-1.899638,0.502213,6.657001,3.725468,4.779969,-4.732242,6.981406,-1.995761,-2.593705,5.826629,-5.130842,-8.354985,3.561678,3.432079,-8.786453,-0.576064,-2.715505,-4.248933,-8.794595,7.428540,-1.880194,-5.669894,0.533396,5.585096,-6.349026,-4.737118,7.561586,9.925119,-8.852479,-8.565529,-0.245431,8.139534,-0.485926,9.314958,6.360401,-0.405664,-1.584750,-2.381238,4.818225,-8.120812,-1.073957,4.784417,2.431251,-7.689116,8.162356,-9.234872,-0.271325,-9.134343,9.919431,7.370799,-8.916550,-0.804820,-5.880339,-0.571469,-7.557005,3.306545,7.832148,2.894366,1.911758,6.957524,-5.114856,8.889399,0.278367,-4.958287,0.128840,-7.968084,2.883523,-5.452183,7.580290,-1.722922,3.004228,-8.838599,-6.401946,6.004962,2.774999,-8.359209,-3.433479,-2.549787,4.018816,-3.635195,-1.752923,-7.330091,5.516704,2.053144,0.661413,6.896888,-1.538837,4.863639,6.457636,-3.830078,9.921076,-4.226059,-8.829773,-8.622372,4.100910,-3.043128,4.844140,-9.473596,-0.562252,6.350041,0.698385,-1.547010,-4.993418,-5.312451,9.297427,-1.510941,0.169415,-8.985652,-1.486741,5.110574,-1.356088,8.342272,-7.727993,-7.086646,-0.033289,-8.867333,-3.629119,0.413198,-7.116116,-8.204884,-2.827913,1.117348,-9.524089,-1.595300,-6.288589,-5.054520,6.020703,-0.372230,2.076978,-6.144046,-3.975081,1.990892,-4.783860,1.256042,-8.960777,-6.186401,-9.175772,-4.172197,7.346291,4.724379,-1.158272,-2.966906,-9.558575,1.399084,-9.850802,1.194989,-5.390286,7.058431,6.004022,-5.834841,9.043732,-8.937705,-1.318399,-0.142277,7.594963,9.896882,2.581306,-4.222217,-0.815815,-6.564627,1.195505,4.120433,-4.784232,-9.500085,7.154192,-7.626111,3.955124,-6.695677,4.983235,-3.468856,6.701822,2.459255,8.725487,-0.447236,3.949928,-9.294525,-7.829851,6.675855,4.387057,-4.267737,-6.519991,6.992051,3.425279,6.256972,-8.444214,-8.120841,0.931937,-9.568891,8.365640,-6.784885,7.135957,7.244921,-6.207668,3.832256,4.422406,-5.457759,-1.447894,4.372562,5.931540,-3.222368,-1.956822,4.866527,-4.100161,6.256077,-3.133275,9.707443,-8.652641,5.181967,4.741427,-8.447992,-4.345913,-2.724092,-7.357860,2.559255,-7.940477,4.166355,-0.023133,-1.509014,7.846963,-2.437509,8.443569,0.564239,-3.478415,-7.237133,4.715989,-7.218491,0.006708,-7.615893,0.691536,0.993923,-3.801380,-9.825780,-7.778878,6.965171,-1.008773,8.205275,6.909826,-2.484498,-7.719941,5.088420,5.063667,9.661101,-2.087592,9.862603,5.320002,2.557288,8.632118,-4.036093,-3.309410,0.041916,5.096087,-5.077572,-3.219902,5.299165,9.600182,-5.659812,-5.506948,7.214601,-0.517915,-7.796183,-3.774148,7.301375,-9.332094,7.960896,2.694666,1.962532], dtype = "float32")#candidate|3702|(800,)|const|float32
call_3700 = relay.TupleGetItem(func_2426_call(relay.reshape(const_3701.astype('int64'), [240,]), relay.reshape(const_3702.astype('float32'), [8, 100]), ), 1)
call_3703 = relay.TupleGetItem(func_2430_call(relay.reshape(const_3701.astype('int64'), [240,]), relay.reshape(const_3702.astype('float32'), [8, 100]), ), 1)
output = relay.Tuple([bop_3689,call_3694,call_3698,call_3700,const_3701,const_3702,])
output2 = relay.Tuple([bop_3689,call_3695,call_3699,call_3703,const_3701,const_3702,])
func_3709 = relay.Function([var_3688,], output)
mod['func_3709'] = func_3709
mod = relay.transform.InferType()(mod)
mutated_mod['func_3709'] = func_3709
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3710 = relay.var("var_3710", dtype = "int16", shape = (14, 2, 14))#candidate|3710|(14, 2, 14)|var|int16
func_3709_call = mutated_mod.get_global_var('func_3709')
call_3711 = func_3709_call(var_3710)
output = call_3711
func_3712 = relay.Function([var_3710], output)
mutated_mod['func_3712'] = func_3712
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2172_call = mutated_mod.get_global_var('func_2172')
call_3744 = func_2171_call()
call_3745 = func_2171_call()
func_2883_call = mod.get_global_var('func_2883')
func_2885_call = mutated_mod.get_global_var('func_2885')
call_3750 = relay.TupleGetItem(func_2883_call(relay.reshape(call_3744.astype('float64'), [6, 9, 3])), 0)
call_3751 = relay.TupleGetItem(func_2885_call(relay.reshape(call_3744.astype('float64'), [6, 9, 3])), 0)
output = relay.Tuple([call_3744,call_3750,])
output2 = relay.Tuple([call_3745,call_3751,])
func_3752 = relay.Function([], output)
mod['func_3752'] = func_3752
mod = relay.transform.InferType()(mod)
mutated_mod['func_3752'] = func_3752
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3752_call = mutated_mod.get_global_var('func_3752')
call_3753 = func_3752_call()
output = call_3753
func_3754 = relay.Function([], output)
mutated_mod['func_3754'] = func_3754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_3788 = relay.TupleGetItem(func_2089_call(), 0)
call_3789 = relay.TupleGetItem(func_2091_call(), 0)
func_1641_call = mod.get_global_var('func_1641')
func_1646_call = mutated_mod.get_global_var('func_1646')
var_3793 = relay.var("var_3793", dtype = "float64", shape = (1, 130))#candidate|3793|(1, 130)|var|float64
const_3794 = relay.const([7.584573,-0.435931,-1.251470,4.422545,8.142716,9.611814,6.597965,6.136741,0.420609,4.611267,4.667511,6.338992,-3.494255,3.962380,6.428738,-1.773052,-2.396317,6.090380,9.346293,4.575305,-4.008662,-4.775433,-6.631520,-2.644761,2.594233,-3.683476,1.579647,2.246466,-1.874278,-0.426783,4.408724,-2.475388,2.147677,-9.821587,3.618414,1.040631,-8.946400,8.072663,2.567733,-4.175803,3.017915,1.830445,-1.635510,0.193512,6.238350,-3.134350,-4.300408,-2.634517,0.977776,-1.362476,-9.235522,-6.225582,7.782005,-6.131238,9.293595,3.555271,5.237724,-4.470926,7.296749,-9.848007,2.673471,8.039481,-5.261905,7.689673,-4.945581,-9.781039,1.353101,3.746116,-4.331174,7.859965,2.653432,-7.942895,7.347096,-6.685635,-9.654991,1.507515,-6.374658,-0.537031,1.689501,-9.701119,1.639377,-6.815263,8.778638,-6.036210,8.398641,2.050811,-0.254997,8.141130,-4.594115,0.017417,0.053554,-1.118232,5.441932,-1.985493,-3.604154,5.313783,0.974126,-9.480089,4.175373,-0.173961,-9.237134,3.054815,7.430869,-5.309346,2.162125,4.877995,8.229212,-8.090745,-9.570777,2.116048,5.033955,-3.410079,-2.757566,5.661542,4.150164,2.427669,6.177923,7.973996,7.544375,8.679035,4.160591,5.021320,-8.328022,4.620566,-6.705724,-5.783569,3.350554,-8.067447,0.805713,-7.811092,7.652825,3.671465,-8.911469,-9.885286,-6.738480,-5.456631,-6.730191,-5.926053,5.785728,0.406805,-9.505195,0.919340,-0.495296,-7.240247,6.536444,0.842853,-6.558559,-4.087770,3.238767,-7.131996,-8.895230,7.120557,8.752122,2.189328,0.800548,-5.049717,-9.666930,-8.990099,-9.647900,9.449892,2.953653,-9.075661,9.992527,-2.006945,9.212872,-9.898143,-4.967530,-3.906299,-4.711880,-7.387920,-9.911952,7.869913,2.173098,-9.225780,-8.460111,6.918192,-3.519166,4.496063,-2.613300,-5.971347,9.224929,7.746670,-8.068335,2.674216,-4.910318,-3.480262,-3.441210,0.377566,6.609312,5.200558,9.986208,0.906511,8.146459,1.024678,9.658206,2.584040,6.538882,-8.781012,2.472811,-5.473967,6.263615,-9.161234,-2.794880,8.449431,0.033225,-1.233339,-7.549441,-3.304212,-6.546975,0.866838,5.969765,-5.441768,-1.952361,-0.688811,-8.804807,4.808372,-4.305219,-5.609640,5.450149,-2.067249,-6.510961,-3.041481,4.337895,-3.583078,-1.207484,6.922654,4.478766,-6.664543,-7.574859,2.266666,1.900375,-1.407277,-1.974411,8.191078,8.099480,8.700736,-9.569079,-3.187981,-3.371298,8.172356,-9.444289,0.188422,7.171807,8.826016,-6.071542,-7.863133,5.308973,8.521757,4.333861,-4.654078,8.741844,2.580541,2.126763,9.874992,-4.209388,-2.712038,5.645856,-7.977252,-1.983631,-4.048871,-2.353323,-5.253361,5.151246,-9.050072,-0.886709,6.020668,-3.012281,2.937899,-1.593237,9.934058,-3.484662,-6.993548,9.451226,-3.509592,-5.926913,5.766082,3.213650,3.977764,4.232422,-8.954323,-5.678244,8.046400,-0.764973,-8.422871,5.283254,5.446227,0.433375,1.308095,0.385920,-8.413791,-0.028595,-0.250234,-5.963807,9.790117,8.492703,1.438637,4.589665,-9.084487,-3.792333,8.118000,9.746358,7.290597,-9.916149,0.873465,-4.766857,2.958876,3.403979,-2.114553,8.717520,-9.826717,3.483301,-1.821043,-8.874459,-1.644817,9.621203,8.287844,1.540865,-1.942803,9.369885,6.537732,9.958843,0.274850,-3.649528,-1.992651,0.908704,3.948220,4.669607,2.994187,-9.250494,-0.164984,4.276494,-0.477486,-5.033761,-8.799714,2.966415,1.041359,5.456281,4.119170,-9.198495,5.630304,-0.919037,8.456944,3.115055,-4.355044,-5.004165,5.233031,-3.287773,-5.096911,-0.120810,-1.695319,-7.350721,3.434909,-0.237317,-5.011477,-3.163518,-1.362294,-7.984557,-8.939755,1.404111,4.939459,3.774768,3.447213,2.008077,-8.471852,3.105728,3.651388,-2.265627,1.433529,4.492748,-5.973424,5.938682,9.527952,-9.596758,4.767510,-4.975881,7.056756,-8.866825,3.646030,6.315459,8.034156,-2.545474,-9.516594,0.755370,-6.365515,2.456329,1.232258,0.422078,-9.510661,-6.959294,5.027610,1.519443,6.257958,-1.326977,0.984259,-7.651237,-5.866868,3.086064,-1.299978,-7.675984,8.171886,9.081776,-0.320306,8.814180,-5.292407,7.184756,-3.332008,-4.218698,-2.852152,-4.812667,-6.251038,-7.682334,-7.860116,-4.803056,6.098385,7.471912,-2.740255,5.357879,2.046003,-9.038071,-7.699884,-7.402002,-1.378997,-9.359303,6.231041,-5.875063,-4.084010,-6.045516,-3.693793,0.165516,5.607802,-2.901686,6.419577,-9.741428,1.682568,-2.043598,-8.565585,-5.809553,3.232048,6.349645,-3.808977,7.958432,7.974306,9.491037,-5.908267,2.105664,7.395156,3.408906,1.961365,4.712504,-5.620069,-8.640636,-6.597786,4.836104,-7.662436,-4.398048,-8.373721,6.317545,6.887810,4.074064,9.299351,3.504899,2.029689,0.984853,6.077084,9.026847,-6.048369,-8.728566,-9.686338,-1.527417,9.875443,4.274160,-5.263653,2.872620,0.169858,2.153904,0.940019,4.098945,-4.864541,4.960630,-4.421024,5.042309,-7.882537,1.289260,-8.702550,6.111467,0.495470,6.767088,6.690798,3.893999,-8.120410,7.376528,-8.950718,-7.952093,6.688362,-0.994727,-7.610194,-0.560067,2.868736,2.749078,-1.348012,4.676523,-4.631697,8.871472,4.460420,-8.358518,-9.567093,1.310568,2.183527,1.382072,7.595908,-4.124681,4.313930,5.115940,-7.281670,-2.334238,0.202338,-7.410905,8.042010,-3.343357,9.897807,-4.718670,-7.397837,-1.583672,1.650292,8.255411,8.793850,-7.075087,-4.591403,0.453170,-6.770857,6.482735,-8.821475,1.873213,-3.976846,-0.303040,3.845624,7.285157,5.185022,2.879094,6.213472,6.808115,-8.926923,1.772770,0.682524,2.057072,8.483926,-3.558872,3.399391,4.972857,9.142160,8.347922,-2.220051,-9.472120,-6.108796,-2.802381,-5.610562,-0.579283,0.102430,-9.655558,-8.098824,-2.042783,-8.413955,9.768688,8.612854,2.671445,0.566580,1.523927,4.633596,6.598655,5.056411,5.955360,9.770671,-4.552976,-0.074856,-4.071118,-3.101615,-9.663233,6.839759,-6.273406,-6.928170,7.092759,-6.863832,2.347449,-6.109262,9.844919,-5.659558,-7.062686,-4.318370,-9.349363,9.598449,-5.252993,9.945139,-7.552398,-3.987773,7.013221,0.399668,-7.934889,1.624428,3.653670,-5.075203,0.878667,-7.272972,9.924169,-6.818942,2.818236,-5.551383,-6.529703,-5.890469,-9.783177,6.612784,9.322738,-4.952900,1.293975,7.430357,0.115465,4.764291,-0.041582,-1.030511,8.600420,9.817745,-6.914089,-0.046211,5.707041,-1.321945,5.232504,-6.005813,-1.009929,9.246274,-8.950080,-3.274435,-9.522418,8.178763,0.860654,-1.939103,-2.322170,9.013123,3.939829,4.681303,-6.236806,-0.843879,-1.931548,-6.910519,7.084608,-4.982542,-9.409688,-5.014373,-1.998891,5.886720,0.644084,-9.721421,1.449106,3.260844,4.534367,-3.675666,-5.189699,-8.052003,3.217082,6.879966,-0.566224,-4.087398,-6.351375,5.641740,-0.372320,2.416997,8.408584,-8.441832,4.091633,4.748865,-9.638481,3.777250,9.495127,0.448463,-3.836936,5.480310,-0.852846,-4.384862,-7.649347,-9.713233,-2.277008,9.272848,5.795441,1.154099,8.890383,-1.486235,-2.985466,-8.761092,3.480864,-5.033678,-9.510887,-0.015674,7.653397,1.241561,-8.234162,8.587843,1.193810,-7.696278,-8.451588,-8.782289,6.707030,6.407173,-9.616714,4.107839,-3.876391,1.994880,8.494764,5.192336,-4.883109,4.208191,-7.567967,-7.208249,2.895603,0.466908,-9.992590,8.162006,-2.053984,9.205648,-6.589417,-7.901207,-0.695054,3.956805,4.789237,-2.042557,5.037631,-9.783850,-6.113115,-2.134661,-6.501844,5.398515,1.688702,-3.660902,-5.782953,-9.343574,-3.213668,1.391318,-6.912683,-2.123934,8.860786,-3.574590,-8.781663,9.309576,5.667057,-7.782674,6.780878,-3.345399,-5.957591,-8.724544,-0.661012,3.285998,3.285774,8.217657,3.223798,0.806257,-6.988955,-7.379974,-9.600207,-1.990069,0.338902,1.307827,-3.376558,1.626072,-6.676789,3.387576,-1.448147,1.523282,7.611880,3.127333,1.198863,-3.533480,-8.920032,-3.920977,-1.733070,-2.159574,-9.395375,-0.707510,1.605707,9.847920,5.361605,-8.889428,-8.701769,1.857792,-6.000293,-9.747674,8.010642,-4.076779,0.073548,-0.364673,5.840759,9.701751,1.874976,-2.222751,4.098269,-3.633540,0.838310,-6.781056,1.356529,8.606649,9.360452,6.035223,-3.029673,-4.875380], dtype = "float32")#candidate|3794|(800,)|const|float32
var_3795 = relay.var("var_3795", dtype = "float32", shape = (21,))#candidate|3795|(21,)|var|float32
call_3792 = relay.TupleGetItem(func_1641_call(relay.reshape(var_3793.astype('float64'), [13, 1, 10]), relay.reshape(var_3793.astype('float64'), [13, 1, 10]), relay.reshape(const_3794.astype('float32'), [800, 1]), relay.reshape(var_3795.astype('float32'), [21,]), ), 1)
call_3796 = relay.TupleGetItem(func_1646_call(relay.reshape(var_3793.astype('float64'), [13, 1, 10]), relay.reshape(var_3793.astype('float64'), [13, 1, 10]), relay.reshape(const_3794.astype('float32'), [800, 1]), relay.reshape(var_3795.astype('float32'), [21,]), ), 1)
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
var_3799 = relay.var("var_3799", dtype = "float32", shape = (462,))#candidate|3799|(462,)|var|float32
call_3798 = relay.TupleGetItem(func_3139_call(relay.reshape(var_3799.astype('float32'), [3, 14, 11])), 0)
call_3800 = relay.TupleGetItem(func_3142_call(relay.reshape(var_3799.astype('float32'), [3, 14, 11])), 0)
output = relay.Tuple([call_3788,call_3792,var_3793,const_3794,var_3795,call_3798,var_3799,])
output2 = relay.Tuple([call_3789,call_3796,var_3793,const_3794,var_3795,call_3800,var_3799,])
func_3801 = relay.Function([var_3793,var_3795,var_3799,], output)
mod['func_3801'] = func_3801
mod = relay.transform.InferType()(mod)
var_3802 = relay.var("var_3802", dtype = "float64", shape = (1, 130))#candidate|3802|(1, 130)|var|float64
var_3803 = relay.var("var_3803", dtype = "float32", shape = (21,))#candidate|3803|(21,)|var|float32
var_3804 = relay.var("var_3804", dtype = "float32", shape = (462,))#candidate|3804|(462,)|var|float32
output = func_3801(var_3802,var_3803,var_3804,)
func_3805 = relay.Function([var_3802,var_3803,var_3804,], output)
mutated_mod['func_3805'] = func_3805
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3255_call = mod.get_global_var('func_3255')
func_3256_call = mutated_mod.get_global_var('func_3256')
call_3901 = relay.TupleGetItem(func_3255_call(), 0)
call_3902 = relay.TupleGetItem(func_3256_call(), 0)
var_3913 = relay.var("var_3913", dtype = "float32", shape = (6, 9, 3))#candidate|3913|(6, 9, 3)|var|float32
bop_3914 = relay.mod(call_3901.astype('float32'), relay.reshape(var_3913.astype('float32'), relay.shape_of(call_3901))) # shape=(6, 9, 3)
bop_3917 = relay.mod(call_3902.astype('float32'), relay.reshape(var_3913.astype('float32'), relay.shape_of(call_3902))) # shape=(6, 9, 3)
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
const_3921 = relay.const([4.354926,4.178440,-9.930628,5.674651,9.155994,5.204173,-1.235320,7.642525,-0.451985,4.405490,-0.714726,8.598196,-4.569124,-0.357657,-0.521037,-1.963108,1.644994,0.838327,9.482124,6.247193,9.702607,0.592090,-8.516195,-6.401235,0.947104,7.585362,-1.738038,-9.660484,-0.646932,-7.860642,4.899611,-2.917753,5.849389,-8.614448,-5.020904,6.156313,-3.948069,3.551573,1.485128,1.856942,2.365576,8.601833,3.143786,-7.101097,-2.363514,8.286266,-4.317849,-8.458758,7.823276,-7.636001,-2.942419,6.508003,-3.743682,9.780468,3.064491,6.140827,-8.860051,-4.271972,-8.040969,6.883991,6.748028,-5.948270,-5.024967,2.355676,-6.036703,5.468935,3.188143,4.367764,-4.947479,-5.776060,-4.121772,-6.704942,-2.980034,-0.740365,-6.159190,7.828756,-1.845493,4.472838,-8.211882,9.448699,-0.523951,-7.768849,4.999134,7.076808,-2.684526,4.639109,5.631523,7.351478,-3.891956,5.284371,8.281835,0.242835,-4.389630,-1.530720,5.782628,2.461725,1.423888,-3.541796,-7.240550,-7.594784,7.452403,0.377724,0.274660,-0.856271,-9.668785,-4.768297,-7.266879,-6.112940,-7.591553,9.833359,-1.948768,2.619235,-6.735919,-5.018215,-6.806742,-7.108163,5.283885,-9.429373,-9.126468,-9.948665,-1.614503,9.107117,-7.377536,-8.746473,-8.661529,8.401311,-7.581925,-5.437230,-6.439769,2.045202,2.742762,-7.102573,7.870861,-4.725669,8.299947], dtype = "float32")#candidate|3921|(135,)|const|float32
call_3920 = relay.TupleGetItem(func_560_call(relay.reshape(const_3921.astype('float32'), [15, 3, 3])), 0)
call_3922 = relay.TupleGetItem(func_563_call(relay.reshape(const_3921.astype('float32'), [15, 3, 3])), 0)
func_1770_call = mod.get_global_var('func_1770')
func_1774_call = mutated_mod.get_global_var('func_1774')
var_3934 = relay.var("var_3934", dtype = "bool", shape = (24, 80))#candidate|3934|(24, 80)|var|bool
call_3933 = relay.TupleGetItem(func_1770_call(relay.reshape(var_3934.astype('bool'), [8, 16, 15]), relay.reshape(var_3934.astype('bool'), [8, 16, 15]), ), 2)
call_3935 = relay.TupleGetItem(func_1774_call(relay.reshape(var_3934.astype('bool'), [8, 16, 15]), relay.reshape(var_3934.astype('bool'), [8, 16, 15]), ), 2)
func_2645_call = mod.get_global_var('func_2645')
func_2647_call = mutated_mod.get_global_var('func_2647')
call_3936 = func_2645_call()
call_3937 = func_2645_call()
func_3671_call = mod.get_global_var('func_3671')
func_3674_call = mutated_mod.get_global_var('func_3674')
call_3949 = relay.TupleGetItem(func_3671_call(relay.reshape(const_3921.astype('float32'), [15, 9]), relay.reshape(bop_3914.astype('float64'), [6, 9, 3]), ), 0)
call_3950 = relay.TupleGetItem(func_3674_call(relay.reshape(const_3921.astype('float32'), [15, 9]), relay.reshape(bop_3914.astype('float64'), [6, 9, 3]), ), 0)
func_3314_call = mod.get_global_var('func_3314')
func_3317_call = mutated_mod.get_global_var('func_3317')
const_3961 = relay.const([[-3,-3,-5,-5,-9,-3,9,-7,9,7],[5,6,6,10,-3,10,-1,-8,9,-9],[6,-7,1,9,5,-5,6,2,-3,5],[-5,4,5,-2,5,-5,3,-5,7,-8],[2,5,-3,1,-9,3,-1,-10,9,5],[3,-5,1,5,-6,2,-4,-7,4,-6],[6,7,-6,-6,-8,1,10,-2,-7,-10],[-7,2,-9,-10,-9,-8,-6,2,1,-1],[8,4,7,10,-10,1,-5,1,-4,-9],[-7,-9,1,9,9,2,-1,7,2,-3],[2,-10,-9,-10,-1,-7,5,5,7,-7],[5,4,-8,5,-2,2,4,-10,-2,5],[9,-6,-10,-10,7,1,-9,-8,-10,8],[-1,4,2,-8,4,2,7,-10,10,-2],[-7,9,-2,6,-1,-1,-3,-8,9,-1],[-1,-8,10,-5,-8,-7,4,5,-6,7],[3,8,5,5,3,-8,-9,-3,4,9],[-5,-9,4,-4,-4,8,8,-5,3,8],[-6,-8,-5,-3,-9,3,1,-4,5,-7],[-8,6,10,-1,-1,-9,-7,1,-10,-1],[9,4,5,6,5,-8,-8,-10,-6,-3],[2,-6,-1,-1,3,9,-7,1,10,-3],[-1,-7,-7,-9,-10,2,6,-10,-4,7],[4,-9,-10,6,-8,-6,-4,-9,-10,6]], dtype = "int64")#candidate|3961|(24, 10)|const|int64
const_3962 = relay.const([-1,-5,-2,-4,8,9,-3,-10,1,-8,6,-10,2,3,1,5,9,-6,1,-1,10,-8,1,1,-5,-10,2,-6,-1,2,1,7,7,2,-3,-9,-5,5,-5,9,-5,1,-1,2,7,6,-1,-9,-6,10,-4,-4,8,-4,-8,-2,-3,2,1,-8,8,-8,8,-1,8,6,10,10,1,-10,-8,2,9,-7,-8,1,-8,-6,6,-3,-9,-4,-10,7,-10,-10,3,-10,-6,3,2,9,-2,-6,-4,-1,-7,2,-1,9,-7,-10,9,-3,8,8,-9,-10,3,7,7,10,5,1,2,7,-7,2,-8,-4,10,-8,10,-9,-6,-10,-6,-6,4,-7,7,10,5,-3,-8,1,8,8,-7,-1,-5,5,1,10,-9,6,5,2,-7,-2,4,4,3,10,-10,3,9,-7,-1,10,6,-8,9,10,8,2,7,2,9,-2,-10,-4,-4,3,-10,5,-6,-8,4,-10,1,-4,7,10,7,-5,-6,-10,-10,4,-4,7,-4,3,-2,-2,-5,1,2,8,-3,8,9,-8,1,-10,-2,2,-9,-8,10,-6,-8,-6,10,2,4,1,-10,-6,-2,3,-3,-4,2,5,-3,8,8,2,10,1,5,-9,10,5,2,-8,7,-7,-3,2,1,-7,-5,-9,4,1,2,6,7,-6,3,4,-5,8,3,-5,-3,-5,1,5,4,7,-8,-7,-6,4,6,-7,8,10,9,-8,-8,-1,9,-6,-2,6,-6,6,6,9,-7,5,-4,-9,-10,5,1,9,-2,2,8,5,-3,-7,-1,2,-5,-7,2,3,-4,10,-4,7,5,-1,9,10,9,2,-6,-9,-1,-1,4,-5,-4,-8,-5,6,4,5,-5,7,10,3,-6,-6,-3,-8,-5,-9,-9,7,2,3,1,1,-3,-10,-2,1,-9,4,6,-1,6,-9,-7,-6,10,-4,9,6,8,7,3,7,-4,4,-3,-2,4,-2,6,9,1,-6,1,-2,-10,-10,-6,-4,7,10,-4,-9,-2,1,-2,5,-6,-4,4,7,-7,-8,-3,1,4,-10,-4,9,1,-7,2,4,4,6,-6,-4,3,3,-8,-8,8,1,6,-1,3,9,9,-5,3,-2,8,1,-10,7,-1,-10,-2,2,-4,6,10,-3,9,3,-3,3,3,-3,8,-2,-5,-9,-5,5,-5,-5,8,-7,9,-1,7,2,-7,2,4,-6,6,4,-8,9,3,10,3,8,-7,4,2,3,-2,-5,-9,-3,-8,-4,-9,-2,8,-4,9,-3,-1,-10,5,-2,-6,-1,-8,10,5,-4,9,-9,-8,-8,-4,-3,1,8,7,-1,7,-8,10,4,-3,10,-4,9,-1,-9,9,10,7,6,-9,7,-10,-4,-4,-6,5,-9,4,-3,6,-1,-5,-6,2,4,-8,-9,7,-9,-2,-10,-10,7,6,10,-1,-8,4,9,-4,9,-6,-10,-4,8,3,-4,-6,6,3,5,-9,-2,-4,2,6,10,10,6,1,1,-1,-7,-7,8,-1,4,5,6,7,-7,-7,-6,9,4,-8,-3,1,-6,5,8,9,7,-8,-1,-10,9,-5,8,-6,5,-7,-3,-10,-7,-4,-2,-7,-7,3,1,8,3,-2,9,-3,-4,-5,-1,9,-2,2,-8,-5,5,4,-3,3,-8,-9,7,-3,4,-1,3,-2,-4,8,-3,-6,-1,4,5,-2,-4,-1,-4,-5,10,-5,5,7,4,-1,6,-5,10,-3,-7,-7,7,-6,-10,-1,-5,5,-6,9,-6,6,8,1,3,2,-8,-2,6,-7,-9,9,5,-5,-6,10,7,-8,-9,2,4,1,2,8,-3,4,-1,7,-1,-8,9,1,-6,-10,9,-5,5,-4,1,-4,-6,8,5,7,6,-3,5,-10,4,-6,-1,5,-8,2,4,6,6,9,-7,-7,2,-9,-5,-8,8,-1,6,4,8,3,-2,2,-3,1,-7,-5,8,8,3,-2,9,-2,3,8,2,3,-10,-3,-6,-3,5,-2,3,6,-3,9,-6,-8,6,10,9,3,-8,4,-3,5,-6,10,-4,-7,7,-2,6,-1,5,-2,5,-4,4,-5,7,-4,6,2,10,-8,5,1,-9,6,4,-10,5,-1,4,-3,-5,-3,1,-10,7,10,-5,7,-5,-10,3,7,-4,5,4,8,-7,10,-8,-8,6,9,1,7,-9,5,7,-9,2,-8,4,-6,8,-6,8,-1,6,-8,-6,-4,-4,-8,-3,-1,-1,-1,-6,5,-5,-10,6,7,-3,-2,-4,5,-7,8,-10,-5,9,-5,5,8,-10,4,10,-2,8,4,-10,9,-2,5,9,2,-6,-4,-6,2,1,-3,-9,7,-7,-1,-10,2,9,-3,-9,-8,-1,-7,-5,2,-7,10,-10,-3,-6,3,7,7,7,6,-4,-1,5,9,-9,7,-5,-1,-3,-1,-9,6,-2,-3,2,4,-2,-10,-5,10,-1,-1,3,1,-6,-7,-9,-2,6,3,-5,-6,4,-7,-7,4,-3,4,8,-3,2,-3,3,-5,3,6,2,6,-8,-6,9,2,-6,-9,4,1,4,-8,-1,5,-8,1,-3,-8,1,5,-6,1,3,-8,-4,2,3,2,-2,10,-7,2,8,-4,-5,-9,6,-3,-2,8,10,-3,-2,8,3,4,9,-4,5,7,7,-9,8,3,-2,7,3,-4,-8,-6,10,-2,3,7,-4,-8,-10,3,8,9,7,2,9,-2,2,-7,10,-3,-7,-3,-5,-1,7,-5,10,-6,2,-6,8,8,-9,-2,6,2,-6,-2,5,7,7,-8,8,3,-6,10,8,3,5,-6,3,-2,-2,-1,8,-8,10,2,-2,7,-6,1,7,3,1,10,-5,2,-9,-4,-1,-3,-8,10,-10,9,5,1,-6,-3,2,-1,-8,-6,-8,-3,3,-3,-1,-3,9,8,-2,6,-1,-4,-4,2,10,8,-8,-8,-7,4,-3,10,8,7,-4,7,6,10,8,2,2,7,-1,1,-7,7,-9,-5,-4,7,7,-7,9,3,-1,-7,-4,-3,1,-4,-8,-10,1,-5,8,-5,10,-10,-1,-6,7,-7,8,-8,5,-9,7,1,-7,-3,2,1,-1,-1,-5,7,2,3,-6,-1,4,-6,-3,7,7,4,9,3,8,4,-3,-7,7,-5,10,-5,-7,-3,10,-10,-1,8,2,10,5,5,-5,1,2,-6,-3,9,4,10,-4,-2,-5,-5,-2,-8,8,-5,6,6,1,2,-5,-5,3,-2,6,-3,6,9,-2,-3,2,5,3,8,3,9,1,6,9,-2,-4,7,3,-8,-3,-5,-10,-3,-4,-8,-10,-5,-2,6,1,-6,1,6,1,8,6,9,6,10,4,6,-6,-7,-4,-10,9,1,-1,-5,-5,-6,-6,9,-10,3,9,-10,-10,5,-9,10,-5,1,10,-10,-9,-7,3,9,5,9,-1,10,5,-5,4,-6,6,7,-3,2,3,-7,5,2,-9,-5,10,-10,-3,-1,10,-6,-7,4,-9,-10,-6,-1,-4,-3,3,-3,-5,8,-8,7,-8,-6,-5,5,-9,-8,-5,-7,1,-1,-10,-5,-7,-3,4,5,-2,-9,1,2,-10,-6,7,-3,3,-3,10,8,-3,-2,-10,10,-10,-10,2,3,-2,6,-2,8,-3,-8,10,-10,-6,7,1,-7,-6,-4,-9,-10,-5,10,5,3,-10,-3,-7,-3,-5,-9,8,9,-3,2,-1,-2,-1,4,-2,-4,-7,5,9,-7,6,3,1,10,7,7,6,-2,2,3,-10,8,-5,1,9,-8,-1,-3,-3,8,8,-5,5,-3,3,4,-4,-3,5,1,-2,-3,10,-9,10,10,-3,2,4,6,1,5,2,4,-3,-5,6,10,-5,-6,6,-3,-2,-8,2,6,-6,1,-8,-7,-10,6,10,1,-4,-10,-4,9,10,4,1,-5,10,5,1,-9,-6,-8,-10,2,5,-4,5,-6,-1,6,2,-9,9,10,-9,10,1,-2,6,-5,-7,1,2,-8,-10,5,6,-4,-1,5,-3,-5,-5,-7,2,4,-1,-1,4,6,-4,6,6,-4,-6,6,6,-6,-8,-3,-7,10,-4,10,8,2,8,1,9,10,-8,7,-8,6,5,8,6,9,7,-8,9,9,1,1,7,7,10,9,6,7,5,-3,-3,3,-6,-7,2,-2,7,-4,7,-2,-7,6,-8,-5,8,6,-4,1,1,-3,-5,-7,-10,-1,-4,3,-5,5,4,8,9,3,-2,-1,4,5,3,-6,-3,-8,-9,8,-2,7,2,7,-7,3,5,-2,2,-10,9,5,-2], dtype = "uint8")#candidate|3962|(1620,)|const|uint8
call_3960 = relay.TupleGetItem(func_3314_call(relay.reshape(const_3961.astype('int64'), [240,]), relay.reshape(const_3962.astype('uint8'), [1620,]), ), 1)
call_3963 = relay.TupleGetItem(func_3317_call(relay.reshape(const_3961.astype('int64'), [240,]), relay.reshape(const_3962.astype('uint8'), [1620,]), ), 1)
func_2655_call = mod.get_global_var('func_2655')
func_2657_call = mutated_mod.get_global_var('func_2657')
const_3969 = relay.const([5.406956,-3.144023,-6.269383,-0.833577,-6.935463,-3.901634,1.709931,-4.973266,-3.572343,8.554899,9.498252,-3.691549,7.268874,3.479729,4.611383,3.405535,2.046000,0.753146,-8.054252,6.575874,-8.147073,6.448019,0.797313,-7.493842,-7.940252,-3.055507,7.015984,-2.529099,7.715058,4.702601,0.909285,-3.666512,-9.499849,-1.414436,8.802075,-5.820068,2.764400,4.035238,2.054684,1.981878,5.706828,9.079115,-0.617795,3.240646,2.202298,-3.991076,-2.783724,5.813292,-7.794997,2.155848,5.717341,0.050473,9.590429,5.007761,3.159704,-5.447009,6.042341,3.454194,4.112125,0.787588,-3.164136,8.333842,-4.816401,2.370197,-3.091972,-9.436409,-1.123464,4.963994,1.216241,-1.682662,0.482034,0.709911,-0.723655,-8.771769,-6.270947,-7.965548,7.687929,9.234642,-7.623632,-4.026890,9.345618,7.320610,7.085976,4.889866,2.472519,9.066633,-5.065559,4.663759,8.257924,-0.124726,-2.827548,-9.555027,1.707168,6.392671,5.130043,-2.018035,6.228894,-2.417324,-7.346170,6.581245,-3.853048,-6.635644,1.458857,0.152221,0.424948,-2.653194,6.084396,2.185588,-0.771878,-4.843869,1.262227,-5.163882,-0.042133,1.513898,-7.068391,9.796201,5.201047,7.140745,6.572988,1.784613,9.714925,-2.406269,1.056815,1.324671,1.456713,9.683173,-0.506486,8.078424,-9.974404,-2.697969,7.691667,6.952806,8.243018,5.273518,-3.330037,-9.356071,9.935684,-7.162584,-9.322946,-9.683286,7.739213,-7.295297,-7.193086,9.048449,-2.816971,5.825102,3.550858,-2.679676,-2.987872,9.997705,7.054088,-2.814277,3.688640,2.656809,-0.923479,6.925803,0.913327,4.850976,6.554665,-3.862913,-9.210811,9.761091,2.230241,2.718347,1.029388,-8.262095,-6.606914,8.994046,2.210587,5.551250,7.779921,3.031779,0.294872,-1.974672,0.771679,-4.041393,-0.637259,8.510044,-6.394478,5.946142,-6.233328,-2.920402,-9.997594,-7.173768,-7.471480,5.952496,-3.114453,-6.587942,-2.947489,-4.206484,6.230910,7.480471,-5.376763,0.079266,9.762950,-7.435882,-0.933965,-5.277115,4.407808,-2.498687,3.280017,8.390590,8.633531,4.663515,-1.410697,2.825333,-7.401852,1.547239,-0.323568,4.811354,-5.925236,6.150466,-5.723981,7.522723,-5.726895,9.190993,-8.836831,3.769871,-4.926918,7.347403,-8.702560,1.417379,6.595088,7.068042,8.288060,-7.342801,-4.377194,3.456576,3.161175,-8.561820,-6.278962,6.417320,-4.569402,-9.333028,9.677873,5.310302,0.938639,1.726566,-6.086558,-8.761724,1.459200,8.443893,-6.662962,8.412310,5.902025,2.791270,8.128147,-9.428961,3.405440,2.192432,-1.449453,-3.453939,8.024333,6.208263,-4.557881,2.239431,-8.978472,0.223709,8.585983,-7.874149,2.638775,4.910123,0.141488,-2.555127,-2.972786,6.108520,3.260427,-8.871904,3.077593,-5.750497,9.012567,-5.133268,-2.397431,-7.563762,-8.259642,-9.600549,-4.193837,-4.560608,-0.668018,-1.880830,-3.997155,5.259973,8.761091,-5.643298,6.838974,-8.923122,9.278118,-3.933220,0.127243,1.935751,-2.876993,5.748686,5.067591,-5.020516,-2.667110,1.721854,-6.824764,-7.491249,-9.982496,9.088948,1.627394,4.375797,-6.611077,-7.398675,-4.354384,2.217871,-6.369376,-2.623881,-4.372525,2.578830,3.428753,-6.726827,5.548002,-3.124241,8.002188,-9.719962,5.754826,1.375111,6.595366,1.277303,-8.262873,-7.579702,7.928158,-5.168547,3.303615,1.049841,-5.828776,0.136736,-8.227653,-8.659512,0.291729,4.886943,-7.751983,-7.508755,-9.298224,2.173930,-2.529358,4.885939,-1.841740,8.794710,4.744074,4.121389,-4.117694,-4.851540,-2.163815,4.842703,5.194278,-0.723238,8.585191,4.456624,4.800687,-5.430025,8.597681,6.362890,-0.342501,5.526846,5.071680,3.662640,2.279623,0.704709,-8.778611,9.997387,7.501570,4.202692,-7.718595,-2.802965,-5.580768,4.535588,6.219762,5.511837,-3.306330,1.086608,2.477817,9.367910,-1.460663,-9.868695,6.868555,-4.018482,-3.654827,-4.030975,9.957548,-4.117657,6.113754,7.917403,-2.145303,-1.948770,2.472296,5.761335,3.628962,-9.820410,7.521903,-7.165354,-5.559824,1.120339,1.122715,-9.015975,-4.038281,-8.133268,-0.432323,-2.440271,-1.489441,6.547666,5.191678,6.820836,-9.240975,-1.645688,-9.230940,-3.657239,-1.481914,6.380250,2.744269,-1.035069,-5.930954,-7.166835,-8.252777,-1.272519,2.709670,-9.053591,-7.589589,9.887796,6.020404,-1.318647,8.912193,6.915078,-1.976994,9.737020,-7.121266,7.236070,-9.747215,4.643802,1.998867,6.013951,-3.500018,9.455019,3.368171,1.955429,-6.694923,5.403718,-7.630263,2.584479,6.443365,5.897800,-7.317919,4.645746,-6.362897,8.500376,-1.064348,-8.156406,4.710295,8.852665,6.244705,7.454467,-4.441436,3.895591,8.713055,0.071079,2.298086,-7.146672,5.763006,-8.750806,1.291461,8.451859,-9.178857,-4.163152,8.989199,4.941815,-4.863668,1.674791,3.364512,1.222984,1.488326,2.712418,2.364967,5.316952,0.054243,-5.256690,5.856547,-3.637676,-0.423019,3.455569,-6.512317,-1.725024,-9.454099,8.856007,-8.386100,-8.989786,9.810550,-1.240630,-7.544218,-9.485602,6.423187,-7.902615,-2.357592,-7.164962,7.604903,7.825240,-3.205905,-0.834337,8.275520,-6.580035,-0.588063,3.551613,9.169110,5.468724,5.586682,3.163920,-7.331284,-0.040743,4.481665,4.708126,-0.060606,-7.366513,-6.733280,7.884695,3.823142,8.364178,2.396360,6.826920,-8.708703,-8.513107,-3.981037,-7.305657,7.652055,-2.033795,-7.865658,3.576793,-3.813657,2.449816,-6.012064,-9.533156,8.687091,7.477585,-3.883192,8.461029,6.756039,3.293245,0.010808,6.207606,-3.007142,2.576259,5.592914,3.785827,0.136053,9.262570,-8.574164,6.602444,9.500338,-5.433168,1.764146,4.691991,9.265529,9.483317,-5.322007,6.931369,-7.925361,3.766542,3.927462,0.449203,-0.415245,-1.281706,-1.343268,-3.121216,-3.809888,7.105281,-9.827793,5.441974,5.660444,-7.039129,0.706935,-8.197732,5.398737,1.355220,0.877049,7.803807,9.226334,-0.218944,1.084840,-8.156177,2.425234,4.540204,-0.586542,3.478620,3.183051,6.536396,4.181099,-4.463918,-9.688634,2.600823,-5.171373,4.393174,-8.912329,0.563094,-4.084184,6.786434,-9.391044,5.376441,7.528224,-0.611759,-2.943268,8.299475,-4.034151,-1.812605,-6.135689,-3.956447,-4.211842,-9.637528,5.502579,-4.167626,3.432884,7.324145,5.939815,-3.052366,2.658043,4.146449,0.554926,9.086007,0.734660,-7.138166,7.317425,-1.308089,-1.995599,-4.637864,4.173204,5.417069,-8.928295,-8.647229,1.029927,8.525387,7.069854,-0.011722,3.009722,-7.013879,-7.455073,-8.751126,9.315281,5.337559,-4.164028,9.850124,2.665545,-7.375584,9.608786,5.977740,-8.263596,6.866642,4.318966,-4.119028,6.989311,8.543831,6.559024,9.151290,4.543548,-2.593792,-0.509706,0.039593,-0.168318,-3.512462,-9.503390,-7.949863,-3.594535,-5.121483,4.692833,-7.435480,-1.220554,-5.713965,-4.847527,-8.637359,5.254301,4.571042,7.323143,9.640558,-8.255581,1.563360,8.234911,6.127632,-4.242802,8.929214,-5.758148,-7.270845,-2.183781,-3.938165,5.686962,-8.934496,3.796660,-1.890706,-6.629759,-9.543861,2.688334,1.156958,9.428586,-8.994273,-5.659982,-3.502598,-3.545119,1.336357,1.394809,2.013457,4.668316,1.845015,1.353766,8.401575,0.169453,-4.147348,6.058500,5.696126,4.948458,-0.543503,-5.845417,-2.238770,-9.477273,7.268078,-5.358525,-0.442533,-6.108034,-8.065122,5.872362,7.884192,-8.736158,-6.855389,6.232971,-0.015143,3.299068,-8.514857,1.431614,-6.704950,3.112033,-6.799988,-3.866700,9.366579,-3.847310,-4.490460,1.575477,0.089052,-4.027885,5.213540,2.988531,-5.582079,4.871419,-4.438569,7.707157,-0.826418,-6.265146,-6.780205,1.662821,9.731978,-6.856444,1.069669,2.450107,7.407218,-8.557320,2.058439,-1.563825,8.779847,1.333469,2.623487,-7.474095,4.682495,-6.656235,-5.243358,2.077737,6.687677,7.270750,1.555617,3.970427,-1.898396,2.082156,-2.219460,0.704430,4.889408,9.277235,-5.368050,-6.285527,6.470367,1.909013,-5.136092,2.996620,-1.030113,1.006495,-3.527604,-1.611758,-9.305904,-0.644091,-3.119441,-1.920712,-5.474867,-2.721366,-7.958749,-2.941811,5.891067,2.007595,-6.730993,7.595544,7.567596,-4.733379,-3.292050,9.772410,9.165612,4.535776,0.923499,5.590184,6.303537,-0.461436,3.316841,9.779574,0.166523,-6.604425,-0.498257,-0.507626,-1.520425,8.684694,-9.708373,-9.614244,-4.944185,0.847585,4.883737,-9.815305,-9.609488,-4.866734,1.351372,-4.557017,-0.937010,6.107676,-3.059859,9.459097,-1.844955,4.646697,4.695785,-2.486890,3.500289,2.834761,4.988918,-3.904336,3.905362,2.002775,-1.794401,4.278409,-4.790200,9.768348,-9.042092,-8.134558,9.094640,2.139333,2.405414,2.773564,8.291770,0.106210,-0.156804,-0.685919,8.279195,-1.130980,9.344905,-6.278127,-4.941189,0.405233,-8.456669,-8.316574,2.411051,-8.367729,5.330282,-6.451374,9.427135,0.183541,1.883959,7.098751,0.399225,-3.873962,4.606193,4.943421,9.465021,-3.254881,-3.600508,4.473184,9.067915,-5.349485,6.894955,0.719083,-3.257363,-3.953514,7.095795,-0.144628,-7.928036,7.808393,-5.805538,3.801091,6.903076,4.656730,-1.393346,-5.583480,7.878780,4.602851,1.077341,7.462652,9.719754,6.219209,7.339862,-0.789363,-5.250805,3.307946,-9.361377,-7.960676,-9.869706,5.941124,9.291377,-3.346540,-1.776179,8.769291,0.642045,0.834249,7.950501,3.871754,0.612079,-8.940046,0.553940,-6.748733,-5.215221,-9.565736,-2.752885,-4.346196,9.512301,-3.594934,-6.316634,1.981987,-6.255340,-2.889931,6.996804,-1.879599,6.549334,-4.766756,-0.154158,-0.341688,-4.520848,-9.711640,-9.059318,-2.768771,9.326027,6.215961,-2.550277,2.991464,-6.387864,-6.047975,8.082671,-1.843302,3.773614,-9.777378,9.692442,6.284998,2.813295,-9.332941,-9.451679,4.486486,-5.331463,3.144820,2.213718,0.411605,-6.690554,2.576534,8.967551,7.402189,-0.096215,-8.654277,-9.353332,2.173825,6.665662,-4.317306,-1.462609,-2.716472,-1.461219,-0.339676,-0.648457,8.810132,2.708436,8.842804,-3.554510,-9.895098,-1.420095,-5.391199,-5.782032,-6.080709,-0.706020,1.323457,-6.166688,8.276653,9.400147,-8.423597,8.102108,-6.414387,-7.532405,2.896038,-5.702373,2.859567,5.887447,-2.016417,-1.104453,0.155241,4.065778,7.164553,-7.884843,-6.460484,-0.252262,-3.239021,6.766614,4.565601,-9.923141,-2.073343,-2.567690,5.908024,-2.468639,2.476891,-6.212428,6.939542,6.670695,9.580543,5.208327,4.907222,-4.596778,5.599413,-7.346601,4.870938,-6.322196,-1.158169,5.106768,-5.201428,6.233320,-7.245179,-1.557207,3.967371,9.794998,-8.423861,-2.527336,-4.129776,7.113110,-2.444587,-8.628842,-8.161867,-2.677773,8.704898,-8.458439,8.964959,9.801052,7.361777,2.937414,9.459578,4.958060,8.600336,5.143403,-2.586644,2.350010,6.120854,-1.657773,-2.810963,-4.164089,-2.954461,2.290854,-4.228188,-5.933843,5.223441,-1.648027,-7.728319,-9.472867,2.264685,9.361334,-0.141997,1.998797,4.792364,1.771191,-3.062539,2.497190,-1.854531,-5.936260,-3.180268,-3.632227,-0.544435,-9.569536,-1.076597,-5.541018,9.598809,3.541582,-0.328228,3.917405,-5.354028,-5.550996,-2.050849,1.959236,-9.343400,5.203835,-6.975939,-3.938072,-8.596391,1.223795,0.030020,-0.619339,-4.961258,-7.110687,-1.057178,-8.922199,-4.415336,3.114200,-8.778246,8.704485,-1.058849,1.799832,-9.889131,6.421264,8.893218,0.240413,-0.003161,8.873387,0.965024,-4.916645,6.925798,-4.728768,7.718651,-2.086140,3.144808,-1.252467,-0.453043,-3.361351,-1.921028,4.618538,7.298973,-7.353420,-1.064075,-9.904999,-4.280875,-4.286568,7.367262,2.097570,-4.706835,-6.035354,-5.371521,-7.159062,5.247436,4.492946,-2.501763,0.174340,-1.585845,-8.025059,5.230190,-2.242533,9.391896,9.681717,-4.162179,7.795811,-4.537412,-8.782228,-1.381719,9.385030,6.033176,5.072352,1.323589,6.152973,9.987265,-0.973621,-4.812628,-6.324608,7.525621,-5.713827,-8.085637,2.904692,-3.854391,9.471112,-5.514629,-2.053226,-5.507726,5.391438,-6.145346,1.067041,-5.448660,-4.630880,-8.873997,-0.722553,-1.692903,1.757065,-5.281932,9.947571,-2.757190,-8.753503,6.290655,7.031487,-2.273315,9.784987,7.585533,-7.843699,-5.566159,2.654330,4.856538,0.817474,-0.460236,4.793950,5.020486,5.791593,3.843122,-6.412884,-1.437737,-6.924612,-0.258021,7.504347,-6.359560,-5.207554,-1.914516,-8.760026,2.004350,6.114733,-0.434778,8.728490,7.783053,-6.171516,-2.100436,0.654588,-8.941264,7.872933,2.969652,-3.558586,6.965986,7.500164,-4.235711,9.689594,6.127427,-0.140719,9.489983,9.426886,-6.645671,-5.891068,-9.663625,-3.695334,2.674570,3.865699,-0.259420,8.401251,-2.716366,-5.840044,-2.978307,2.402895,-5.640859,4.021613,7.143439,2.850451,-8.368325,-8.248930,3.575896,1.493454,-3.623381,-4.629221,7.922133,-8.986369,-3.705046,-2.828849,9.910082,-7.770483,1.672460,8.163825,-2.904782,1.641028,-4.679410,8.154501,-4.098092,7.769302,4.224063,1.844329,3.002914,0.311841,-2.066303,-3.519696,2.676756,-5.304437,-1.366257,7.693600,-2.868775,-1.918637,-2.803920,-6.502837,-4.591698,9.043874,1.382362,-8.801416,8.835995,-4.879657,-9.975454,8.147853,8.179176,-5.623693,5.708793,-5.813562,-0.172992,7.382438,-8.834568,4.454814,8.758767,3.602658,-2.308140,0.035468,9.592446,0.580450,-3.086098,7.118473,-7.221104,3.885816,5.358458,8.553023,-2.768239,-8.996672,4.236122,-5.320774,-8.771145,2.623615,2.102699,-1.076408,8.810280,-4.430232,-5.251389,7.492120,-0.679467,1.378281,5.413779,0.578551,0.038321,-0.813248,-7.932277,2.625839,-2.885853,2.174093,0.552305,-1.409607,0.206959,-0.930206,-0.185087,8.956726,-8.516139,-1.670098,1.067120,-2.855561,6.495346,3.326691,4.622619,1.850884,-3.006363,7.011032,-4.481887,-1.787211,6.520612,-4.744056,-0.687984,-6.370718,-6.470074,-7.638525,-7.539824,-9.616042,-1.036871,8.666608,-8.988392,3.803545,2.545377,-3.226984,1.025458,-2.681024,2.026319,-7.478523,-2.369639,-4.749116,-6.309851,-3.137837,4.975890,-3.781819,5.649081,4.963452,-3.604661,-7.066314,-3.843901,-7.706341,8.999012,-9.196363,0.903153,-7.589979,9.612418,-3.459958,-9.440399,-2.212329,5.539959,9.677933,6.910594,-2.147516,6.102236,5.135759,9.862766,7.940527,-3.807544,6.364039,6.277259,0.944052,-2.168179,-4.096184,4.118941,8.774366,5.787635,0.453374,2.459138,4.557077,-5.476800,-9.985822,-1.486377,-2.734173,4.261678,-2.659375,7.514086,3.960294,8.587917,-6.445911,2.762495,1.294740,-1.093798,8.537136,-9.126562,7.812204,3.120462,-3.246862,2.606835,0.027317,-1.527664,2.611380,9.007654,0.439627,-8.119425,7.951347,5.828612,8.004503,8.955509,-1.623263,0.452000,-6.634631,9.858104,-0.361737,7.415177,-1.841960,8.935242,-0.747971,-4.947157,2.693128,1.955196,-0.791108,4.082276,9.909994,-3.952457,-7.163051,2.927536,6.742476,0.071690,0.860745,4.919428,-4.574798,-4.248908,4.937306,-7.557061,8.552548,-5.855512,2.651749,5.448770,-2.677540,-0.427215,9.223710,-3.870458,-4.843573,-7.089300,-8.517994,2.705124,-4.287197,9.011039,6.568187,-0.692294,-8.450049,-6.301982,-8.154581,-4.290281,-5.761352,8.227111,-4.193165,-7.921974,1.100764,-4.253272,-5.489021,-0.053638,4.853647,-7.526812,-8.284070,-7.650911,4.256062,-9.018167,-1.258902,1.261483,7.512135,5.566422,-3.031175,-7.014837,-7.417958,6.048618,9.548418,-0.182798,-0.640145,1.169449,0.659029,5.389758,-0.660735,6.784203,-4.711308,6.109845,6.598739,8.238206,-1.748879,-7.617101,-5.368801,8.789783,5.833306,3.897223,1.483218,-0.889631,-1.518448,1.002608,3.557748,0.148148,0.250217,0.681411,3.077391,-9.785405,5.908160,5.037421,4.971764,1.697795,-6.975992,-5.590009,1.435911,-8.363213,-1.943599,-3.345831,-1.030386,3.658695,4.884759,7.736045,4.780915,-1.739626,-8.209889,-7.035679,6.716537,-8.686334,-1.062180,1.268703,-2.051910,1.880960,8.863031,-5.613390,-8.469547,-1.023967,2.167660,-4.019664,5.729878,7.368814,-9.812036,0.296851,1.086554,9.672546,-3.266176,0.132690,9.084305,7.381990,-2.458911,-7.506109,7.869237,-6.740864,-4.451425,0.488774,-2.656405,4.394862,4.756980,-3.599573,7.727509,-1.693847,-4.649045,-8.588065,0.054212,-2.997650,5.295906,-0.323744,8.076626,2.467348,0.120703,-4.709538,5.328372,9.151348,-8.939033,4.852301,0.290026,-1.338967,3.184718,9.099013,-8.959457,2.942981,3.192758,3.482960,-0.030239,-0.845779,2.759087,3.185048,4.440707,4.488139,-9.866059,2.818964,5.803033,6.998382,-4.521515,6.705669,9.292676,-0.063599,-4.329142,7.523431,5.016920,-2.175604,-6.499958,8.445686,-9.705604,-0.045906,-5.126835,3.030927,3.421946,-4.898731,1.494854,-5.865021,-0.274976,2.236854,-1.629561,-2.643109,7.537175,8.950015,-0.703716,9.934437,1.217886,-3.817023,1.887794,8.532998,-3.034023,-5.803347,7.816366,-6.782513,3.236917,-5.989403,6.716085,0.757797,-0.219107,-3.842478,-8.841897,4.077071,7.853815,3.790929,7.826007,9.695326,-8.364047,-3.790468,9.691333,-0.044993,-0.981761,-5.638388,9.120095,-3.860507,-0.330117,-9.961493,-1.244210,2.362241,1.616529,-9.920841,8.578475,8.598721,1.216886,-8.783033,-2.270141,-8.426521,4.351719,-9.534735,-2.079781,-6.189430,-1.643113,4.688532,8.732723,-7.741814,5.859196,0.127458,2.969170,0.289941,-8.955051,7.916617,-5.769798,-5.490247,-0.781713,-3.046347,4.721112,-2.163374,8.188936,3.102430,-2.113815,-3.647266,-4.842404,-4.745300,-3.289989,5.032384,2.066708,8.654289,-6.098108,-5.040703,9.591121,7.424871,6.340080,-9.994662,-1.123552,2.551822,6.276310,-2.469324,-6.725410,4.280917,-7.742916,5.449349,5.245489,1.381923,-8.665693,4.216138,-7.267417,9.486873,-2.496039,8.719574,9.999713,6.749877,-2.547585,-0.515279,-8.064610,6.506383,-5.393149,9.987685,6.204323,2.077042,-8.706259,7.994345,-4.723920,-4.250312,-6.081609,3.973833,5.222033,2.408554,-5.664590,-2.614521,5.073296,-6.942221,-2.940821,-1.716454,-3.038785,-9.096279,-4.031602,-7.086142,-6.148976,1.961497,-6.325246,-3.813203,8.362578,1.629658,3.356529,-2.574003,4.217690,6.460453,-4.690018,6.650273,5.328332], dtype = "float32")#candidate|3969|(1764,)|const|float32
call_3968 = relay.TupleGetItem(func_2655_call(relay.reshape(const_3969.astype('float32'), [9, 14, 14])), 0)
call_3970 = relay.TupleGetItem(func_2657_call(relay.reshape(const_3969.astype('float32'), [9, 14, 14])), 0)
func_2883_call = mod.get_global_var('func_2883')
func_2885_call = mutated_mod.get_global_var('func_2885')
call_3988 = relay.TupleGetItem(func_2883_call(relay.reshape(var_3913.astype('float64'), [6, 9, 3])), 0)
call_3989 = relay.TupleGetItem(func_2885_call(relay.reshape(var_3913.astype('float64'), [6, 9, 3])), 0)
output = relay.Tuple([bop_3914,call_3920,const_3921,call_3933,var_3934,call_3936,call_3949,call_3960,const_3961,const_3962,call_3968,const_3969,call_3988,])
output2 = relay.Tuple([bop_3917,call_3922,const_3921,call_3935,var_3934,call_3937,call_3950,call_3963,const_3961,const_3962,call_3970,const_3969,call_3989,])
func_3997 = relay.Function([var_3913,var_3934,], output)
mod['func_3997'] = func_3997
mod = relay.transform.InferType()(mod)
var_3998 = relay.var("var_3998", dtype = "float32", shape = (6, 9, 3))#candidate|3998|(6, 9, 3)|var|float32
var_3999 = relay.var("var_3999", dtype = "bool", shape = (24, 80))#candidate|3999|(24, 80)|var|bool
output = func_3997(var_3998,var_3999,)
func_4000 = relay.Function([var_3998,var_3999,], output)
mutated_mod['func_4000'] = func_4000
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4016 = relay.var("var_4016", dtype = "float64", shape = (6, 10, 10))#candidate|4016|(6, 10, 10)|var|float64
uop_4017 = relay.log10(var_4016.astype('float64')) # shape=(6, 10, 10)
var_4025 = relay.var("var_4025", dtype = "float64", shape = (6, 10, 10))#candidate|4025|(6, 10, 10)|var|float64
bop_4026 = relay.bitwise_xor(uop_4017.astype('int32'), relay.reshape(var_4025.astype('int32'), relay.shape_of(uop_4017))) # shape=(6, 10, 10)
func_3426_call = mod.get_global_var('func_3426')
func_3430_call = mutated_mod.get_global_var('func_3430')
const_4030 = relay.const([False,False,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,False,True,False,False,True,False,True,True,False,True,True,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,False,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,True,True,False,False,True,True,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,True,False,False,True,True,False,False,True,False,False,False,False,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,False,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,False,True,True,False,False,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,True], dtype = "bool")#candidate|4030|(780,)|const|bool
call_4029 = func_3426_call(relay.reshape(const_4030.astype('bool'), [13, 10, 6]), relay.reshape(const_4030.astype('bool'), [13, 10, 6]), )
call_4031 = func_3426_call(relay.reshape(const_4030.astype('bool'), [13, 10, 6]), relay.reshape(const_4030.astype('bool'), [13, 10, 6]), )
output = relay.Tuple([bop_4026,call_4029,const_4030,])
output2 = relay.Tuple([bop_4026,call_4031,const_4030,])
func_4039 = relay.Function([var_4016,var_4025,], output)
mod['func_4039'] = func_4039
mod = relay.transform.InferType()(mod)
var_4040 = relay.var("var_4040", dtype = "float64", shape = (6, 10, 10))#candidate|4040|(6, 10, 10)|var|float64
var_4041 = relay.var("var_4041", dtype = "float64", shape = (6, 10, 10))#candidate|4041|(6, 10, 10)|var|float64
output = func_4039(var_4040,var_4041,)
func_4042 = relay.Function([var_4040,var_4041,], output)
mutated_mod['func_4042'] = func_4042
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_4068 = relay.TupleGetItem(func_1986_call(), 0)
call_4069 = relay.TupleGetItem(func_1988_call(), 0)
uop_4072 = relay.cos(call_4068.astype('float32')) # shape=(6, 9, 3)
uop_4074 = relay.cos(call_4069.astype('float32')) # shape=(6, 9, 3)
func_2426_call = mod.get_global_var('func_2426')
func_2430_call = mutated_mod.get_global_var('func_2430')
var_4088 = relay.var("var_4088", dtype = "int64", shape = (240,))#candidate|4088|(240,)|var|int64
var_4089 = relay.var("var_4089", dtype = "float32", shape = (800,))#candidate|4089|(800,)|var|float32
call_4087 = relay.TupleGetItem(func_2426_call(relay.reshape(var_4088.astype('int64'), [240,]), relay.reshape(var_4089.astype('float32'), [8, 100]), ), 4)
call_4090 = relay.TupleGetItem(func_2430_call(relay.reshape(var_4088.astype('int64'), [240,]), relay.reshape(var_4089.astype('float32'), [8, 100]), ), 4)
output = relay.Tuple([uop_4072,call_4087,var_4088,var_4089,])
output2 = relay.Tuple([uop_4074,call_4090,var_4088,var_4089,])
func_4099 = relay.Function([var_4088,var_4089,], output)
mod['func_4099'] = func_4099
mod = relay.transform.InferType()(mod)
var_4100 = relay.var("var_4100", dtype = "int64", shape = (240,))#candidate|4100|(240,)|var|int64
var_4101 = relay.var("var_4101", dtype = "float32", shape = (800,))#candidate|4101|(800,)|var|float32
output = func_4099(var_4100,var_4101,)
func_4102 = relay.Function([var_4100,var_4101,], output)
mutated_mod['func_4102'] = func_4102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3287_call = mod.get_global_var('func_3287')
func_3288_call = mutated_mod.get_global_var('func_3288')
call_4127 = relay.TupleGetItem(func_3287_call(), 1)
call_4128 = relay.TupleGetItem(func_3288_call(), 1)
output = call_4127
output2 = call_4128
func_4139 = relay.Function([], output)
mod['func_4139'] = func_4139
mod = relay.transform.InferType()(mod)
mutated_mod['func_4139'] = func_4139
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4139_call = mutated_mod.get_global_var('func_4139')
call_4140 = func_4139_call()
output = call_4140
func_4141 = relay.Function([], output)
mutated_mod['func_4141'] = func_4141
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_4142 = func_3004_call()
call_4143 = func_3004_call()
output = relay.Tuple([call_4142,])
output2 = relay.Tuple([call_4143,])
func_4151 = relay.Function([], output)
mod['func_4151'] = func_4151
mod = relay.transform.InferType()(mod)
output = func_4151()
func_4152 = relay.Function([], output)
mutated_mod['func_4152'] = func_4152
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_4221 = func_3004_call()
call_4222 = func_3004_call()
func_3192_call = mod.get_global_var('func_3192')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_4230 = relay.TupleGetItem(func_3192_call(), 0)
call_4231 = relay.TupleGetItem(func_3193_call(), 0)
func_1213_call = mod.get_global_var('func_1213')
func_1216_call = mutated_mod.get_global_var('func_1216')
const_4258 = relay.const([4.463696,-1.834195,9.259594,-2.747911,-3.298780,-6.328932,7.771902,-9.713740,8.487932,9.113099,-3.897109,8.524238,2.056783,-4.150169,-7.938738,5.691842,9.339096,-9.403774,9.175758,-9.489010,1.784210], dtype = "float32")#candidate|4258|(21,)|const|float32
var_4259 = relay.var("var_4259", dtype = "float32", shape = (288,))#candidate|4259|(288,)|var|float32
call_4257 = relay.TupleGetItem(func_1213_call(relay.reshape(const_4258.astype('float32'), [1, 3, 7]), relay.reshape(var_4259.astype('float32'), [8, 36]), ), 2)
call_4260 = relay.TupleGetItem(func_1216_call(relay.reshape(const_4258.astype('float32'), [1, 3, 7]), relay.reshape(var_4259.astype('float32'), [8, 36]), ), 2)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_4267 = relay.TupleGetItem(func_2017_call(), 0)
call_4268 = relay.TupleGetItem(func_2019_call(), 0)
uop_4289 = relay.atanh(call_4230.astype('float32')) # shape=(6, 9, 3)
uop_4291 = relay.atanh(call_4231.astype('float32')) # shape=(6, 9, 3)
output = relay.Tuple([call_4221,call_4257,const_4258,var_4259,call_4267,uop_4289,])
output2 = relay.Tuple([call_4222,call_4260,const_4258,var_4259,call_4268,uop_4291,])
func_4297 = relay.Function([var_4259,], output)
mod['func_4297'] = func_4297
mod = relay.transform.InferType()(mod)
var_4298 = relay.var("var_4298", dtype = "float32", shape = (288,))#candidate|4298|(288,)|var|float32
output = func_4297(var_4298)
func_4299 = relay.Function([var_4298], output)
mutated_mod['func_4299'] = func_4299
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_4324 = relay.TupleGetItem(func_1986_call(), 0)
call_4325 = relay.TupleGetItem(func_1988_call(), 0)
output = call_4324
output2 = call_4325
func_4331 = relay.Function([], output)
mod['func_4331'] = func_4331
mod = relay.transform.InferType()(mod)
output = func_4331()
func_4332 = relay.Function([], output)
mutated_mod['func_4332'] = func_4332
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_4395 = relay.TupleGetItem(func_2017_call(), 0)
call_4396 = relay.TupleGetItem(func_2019_call(), 0)
func_2242_call = mod.get_global_var('func_2242')
func_2245_call = mutated_mod.get_global_var('func_2245')
var_4398 = relay.var("var_4398", dtype = "float64", shape = (1890,))#candidate|4398|(1890,)|var|float64
call_4397 = relay.TupleGetItem(func_2242_call(relay.reshape(var_4398.astype('float64'), [1890,]), relay.reshape(call_4395.astype('float64'), [6, 9, 3]), ), 2)
call_4399 = relay.TupleGetItem(func_2245_call(relay.reshape(var_4398.astype('float64'), [1890,]), relay.reshape(call_4395.astype('float64'), [6, 9, 3]), ), 2)
func_2526_call = mod.get_global_var('func_2526')
func_2529_call = mutated_mod.get_global_var('func_2529')
const_4405 = relay.const([[9.933854],[1.056617],[8.175217],[-7.537812],[8.051625],[1.458749],[7.378669],[2.130755],[-6.738990],[-5.339264],[0.581441],[-5.282004],[-9.108580],[-5.722006],[-8.720553],[8.389244],[-8.285545],[7.918451],[-5.392277],[-8.615296],[-1.715702],[-5.579440],[-1.429278],[-7.278663],[4.000056],[-0.941732],[-5.073685],[4.856634],[6.934964],[-4.714087],[5.007907],[8.923283],[-2.879718],[-5.018312],[-4.315120],[5.462373],[-9.757400],[-2.567267],[1.834718],[8.947578],[5.692920],[3.071336],[7.160666],[-9.602323],[8.663040],[-1.769470],[-9.189394],[-2.610658],[-9.744516],[5.402413],[7.463585],[-6.425481],[2.381209],[-0.224470],[8.760108],[0.129536],[1.945933],[-9.293855],[0.771810],[5.996525],[7.084695],[7.809483],[5.783340],[7.510382],[-6.672786],[0.183697],[2.258769],[9.602032],[-6.124374],[4.747239],[-0.307591],[7.169283],[-9.166627],[-1.447812],[-8.611159],[-9.160286],[3.146528],[-9.297900],[4.560181],[8.808005],[-4.230104],[4.350810],[-0.982708],[-6.939751],[-9.975743],[-9.385815],[-2.205582],[-4.027939],[9.369987],[-2.360308],[1.870458],[-9.530954],[9.961140],[5.036270],[-4.360395],[-9.927515],[8.063151],[-6.633268],[4.287408],[6.121269],[-2.363452],[-2.359811],[7.647732],[0.270035],[6.911019],[-8.118466],[-7.772256],[5.302500],[8.803339],[-6.768213],[3.948037],[9.134359],[-6.688506],[-4.593547],[-1.382470],[4.032202],[9.053596],[-1.103386],[8.441782],[-9.123813],[7.205735],[2.634567],[0.497526],[9.272894],[2.304619],[-2.423853],[9.891336],[-2.354651],[1.098449],[2.349674],[-3.647842],[-9.666625],[-4.898391],[-7.771953],[7.152476],[-3.934615],[1.174959],[-3.675200],[-0.834195],[-9.930116],[-0.982407],[6.649459],[-4.392041],[0.175992]], dtype = "float32")#candidate|4405|(144, 1)|const|float32
var_4406 = relay.var("var_4406", dtype = "float32", shape = (288,))#candidate|4406|(288,)|var|float32
call_4404 = relay.TupleGetItem(func_2526_call(relay.reshape(const_4405.astype('float32'), [144,]), relay.reshape(var_4406.astype('float32'), [8, 36]), ), 5)
call_4407 = relay.TupleGetItem(func_2529_call(relay.reshape(const_4405.astype('float32'), [144,]), relay.reshape(var_4406.astype('float32'), [8, 36]), ), 5)
var_4417 = relay.var("var_4417", dtype = "float64", shape = (6, 9, 3))#candidate|4417|(6, 9, 3)|var|float64
bop_4418 = relay.less(call_4397.astype('bool'), relay.reshape(var_4417.astype('bool'), relay.shape_of(call_4397))) # shape=(6, 9, 3)
bop_4421 = relay.less(call_4399.astype('bool'), relay.reshape(var_4417.astype('bool'), relay.shape_of(call_4399))) # shape=(6, 9, 3)
output = relay.Tuple([call_4395,var_4398,call_4404,const_4405,var_4406,bop_4418,])
output2 = relay.Tuple([call_4396,var_4398,call_4407,const_4405,var_4406,bop_4421,])
func_4429 = relay.Function([var_4398,var_4406,var_4417,], output)
mod['func_4429'] = func_4429
mod = relay.transform.InferType()(mod)
mutated_mod['func_4429'] = func_4429
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4429_call = mutated_mod.get_global_var('func_4429')
var_4431 = relay.var("var_4431", dtype = "float64", shape = (1890,))#candidate|4431|(1890,)|var|float64
var_4432 = relay.var("var_4432", dtype = "float32", shape = (288,))#candidate|4432|(288,)|var|float32
var_4433 = relay.var("var_4433", dtype = "float64", shape = (6, 9, 3))#candidate|4433|(6, 9, 3)|var|float64
call_4430 = func_4429_call(var_4431,var_4432,var_4433,)
output = call_4430
func_4434 = relay.Function([var_4431,var_4432,var_4433,], output)
mutated_mod['func_4434'] = func_4434
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3192_call = mod.get_global_var('func_3192')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_4436 = relay.TupleGetItem(func_3192_call(), 0)
call_4437 = relay.TupleGetItem(func_3193_call(), 0)
func_1641_call = mod.get_global_var('func_1641')
func_1646_call = mutated_mod.get_global_var('func_1646')
var_4442 = relay.var("var_4442", dtype = "float64", shape = (26, 5))#candidate|4442|(26, 5)|var|float64
var_4443 = relay.var("var_4443", dtype = "float32", shape = (800,))#candidate|4443|(800,)|var|float32
const_4444 = relay.const([1.640508,-1.711592,-2.192398,-9.821047,5.164619,-6.879285,-5.045325,-4.605238,-8.060457,-1.913204,6.760634,-9.652508,8.282630,-5.992857,-3.271025,2.171366,-9.194754,3.685258,9.899838,7.707514,9.560546], dtype = "float32")#candidate|4444|(21,)|const|float32
call_4441 = relay.TupleGetItem(func_1641_call(relay.reshape(var_4442.astype('float64'), [13, 1, 10]), relay.reshape(var_4442.astype('float64'), [13, 1, 10]), relay.reshape(var_4443.astype('float32'), [800, 1]), relay.reshape(const_4444.astype('float32'), [21,]), ), 0)
call_4445 = relay.TupleGetItem(func_1646_call(relay.reshape(var_4442.astype('float64'), [13, 1, 10]), relay.reshape(var_4442.astype('float64'), [13, 1, 10]), relay.reshape(var_4443.astype('float32'), [800, 1]), relay.reshape(const_4444.astype('float32'), [21,]), ), 0)
output = relay.Tuple([call_4436,call_4441,var_4442,var_4443,const_4444,])
output2 = relay.Tuple([call_4437,call_4445,var_4442,var_4443,const_4444,])
func_4447 = relay.Function([var_4442,var_4443,], output)
mod['func_4447'] = func_4447
mod = relay.transform.InferType()(mod)
mutated_mod['func_4447'] = func_4447
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4447_call = mutated_mod.get_global_var('func_4447')
var_4449 = relay.var("var_4449", dtype = "float64", shape = (26, 5))#candidate|4449|(26, 5)|var|float64
var_4450 = relay.var("var_4450", dtype = "float32", shape = (800,))#candidate|4450|(800,)|var|float32
call_4448 = func_4447_call(var_4449,var_4450,)
output = call_4448
func_4451 = relay.Function([var_4449,var_4450,], output)
mutated_mod['func_4451'] = func_4451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_4458 = func_3004_call()
call_4459 = func_3004_call()
output = call_4458
output2 = call_4459
func_4464 = relay.Function([], output)
mod['func_4464'] = func_4464
mod = relay.transform.InferType()(mod)
mutated_mod['func_4464'] = func_4464
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4464_call = mutated_mod.get_global_var('func_4464')
call_4465 = func_4464_call()
output = call_4465
func_4466 = relay.Function([], output)
mutated_mod['func_4466'] = func_4466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3752_call = mod.get_global_var('func_3752')
func_3754_call = mutated_mod.get_global_var('func_3754')
call_4479 = relay.TupleGetItem(func_3752_call(), 1)
call_4480 = relay.TupleGetItem(func_3754_call(), 1)
output = relay.Tuple([call_4479,])
output2 = relay.Tuple([call_4480,])
func_4485 = relay.Function([], output)
mod['func_4485'] = func_4485
mod = relay.transform.InferType()(mod)
output = func_4485()
func_4486 = relay.Function([], output)
mutated_mod['func_4486'] = func_4486
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3210_call = mod.get_global_var('func_3210')
func_3211_call = mutated_mod.get_global_var('func_3211')
call_4539 = func_3210_call()
call_4540 = func_3210_call()
output = call_4539
output2 = call_4540
func_4554 = relay.Function([], output)
mod['func_4554'] = func_4554
mod = relay.transform.InferType()(mod)
output = func_4554()
func_4555 = relay.Function([], output)
mutated_mod['func_4555'] = func_4555
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3192_call = mod.get_global_var('func_3192')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_4648 = relay.TupleGetItem(func_3192_call(), 0)
call_4649 = relay.TupleGetItem(func_3193_call(), 0)
var_4652 = relay.var("var_4652", dtype = "float64", shape = (6, 9, 3))#candidate|4652|(6, 9, 3)|var|float64
bop_4653 = relay.divide(call_4648.astype('float64'), relay.reshape(var_4652.astype('float64'), relay.shape_of(call_4648))) # shape=(6, 9, 3)
bop_4656 = relay.divide(call_4649.astype('float64'), relay.reshape(var_4652.astype('float64'), relay.shape_of(call_4649))) # shape=(6, 9, 3)
output = relay.Tuple([bop_4653,])
output2 = relay.Tuple([bop_4656,])
func_4668 = relay.Function([var_4652,], output)
mod['func_4668'] = func_4668
mod = relay.transform.InferType()(mod)
var_4669 = relay.var("var_4669", dtype = "float64", shape = (6, 9, 3))#candidate|4669|(6, 9, 3)|var|float64
output = func_4668(var_4669)
func_4670 = relay.Function([var_4669], output)
mutated_mod['func_4670'] = func_4670
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_4700 = relay.TupleGetItem(func_2564_call(), 0)
call_4701 = relay.TupleGetItem(func_2566_call(), 0)
output = call_4700
output2 = call_4701
func_4707 = relay.Function([], output)
mod['func_4707'] = func_4707
mod = relay.transform.InferType()(mod)
output = func_4707()
func_4708 = relay.Function([], output)
mutated_mod['func_4708'] = func_4708
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_4714 = func_3004_call()
call_4715 = func_3004_call()
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_4722 = relay.TupleGetItem(func_2017_call(), 1)
call_4723 = relay.TupleGetItem(func_2019_call(), 1)
func_1326_call = mod.get_global_var('func_1326')
func_1329_call = mutated_mod.get_global_var('func_1329')
const_4729 = relay.const([8.207279,-5.734451,1.994650,8.857852,-3.380024,-4.057690,-7.819008,-1.636987,5.840721,3.271335,-7.241351,-8.596328,2.043502,2.761728,-4.271074,-3.832127,-8.441859,2.953730,4.051137,-4.959958,-2.831076,-7.182943,-9.928875,-3.138932,9.803218,6.130692,-2.338724,4.307706,2.559146,-3.617633,-4.736417,-3.746663,7.310895,1.948020,-1.753154,-2.406895,-7.043080,-3.944072,-8.504531,-6.379530,-0.480343,4.612804,8.538509,-3.958284,4.463177,5.285448,-0.503379,-3.524805,5.759500,-8.720811,5.901824,-9.952134,-7.190052,-1.572448,4.751431,-7.339484,7.971740,8.729396,5.574070,3.193926,-2.420448,-3.856118,-2.310215,7.871731,-0.670836,-9.797289,-3.895187,6.744778,2.921917,9.880915,-1.972789,-3.018354,1.366606,2.803585,-7.590417,-8.680811,4.037858,9.210246,4.651733,5.141276,-6.523859,-7.544519,-3.394737,8.181184,7.550193,-0.357703,4.855442,8.583798,-6.366822,5.994997,-0.025414,-1.086059,-9.330148,9.108354,-1.090566,-5.017818,-8.491564,0.315756,-7.430166,-3.710066,-1.782801,-1.438267,-2.042768,-1.637187,-1.101132,6.111955,2.811119,-8.207525,9.299052,-9.544335,-2.286083,-2.617575,3.548366,9.137637,1.105285,4.967587,-7.199860,1.327631,-9.647590,-1.951633,2.195971,5.507932,5.012498,-2.757955,0.532953,-4.740341,7.745990,6.461503,-4.076366,7.894422,-0.904608,2.863560,-6.311514,1.077633,5.036275,3.454583,4.192580,0.100460,-4.209265,5.607972,-8.891917,1.601199,1.241629,-3.993706,8.433809,4.518607,2.128751,-9.903585,3.419611,-8.460850,8.946338,4.707975,-6.165334,6.568644,-9.240512,-5.841659,-7.208863,4.025714,-9.361049,-9.843152,9.697850,-9.389838,-2.105696,-2.111249,-5.038029,-4.526352,-4.251629,2.942991,2.424457,5.170187,2.978219,-8.016051,1.379632,9.918267,-0.815036,6.821101,4.610851,-2.378327,-2.289814,7.573208,7.624198,4.315932,3.522175,-3.085874,5.730898,4.787161,9.852100,1.644531,7.253612,1.029389,-6.660239,6.404999,-6.097459,7.051315,-1.448044,4.249471,7.422255,5.253152,9.488380,2.396496,1.159079,-8.698158,-8.087375,4.254004,-2.348457,8.340073,1.764832,9.309924,-2.701401,-1.430817,1.481356,-4.072685,-8.275886,-6.740908,4.392101,0.513782,-6.667461,-4.092904,4.700596,-6.197109,-2.451939,-5.735831,-6.728457,9.228921,-7.909759,9.500922,8.480388,-6.529356,2.468507,-0.874314,-4.794256,4.591131,8.492457,-2.984939,7.807017,-5.182325,-9.733717,0.408595,-7.937089,-5.360538,-0.387464,2.618275,6.261561,-2.853430,-2.840543,-6.033399,-2.002378,0.867310,4.405711,-1.536432,-1.361185,-2.353723,8.473835,1.410814,-0.697640,-8.412116,5.098114,-0.308458,-7.563526,9.914273,7.232597,5.802059,8.379562,8.057433,-9.258259,0.736367,6.444187,-6.162292,4.319896,-6.723583,6.796710,-4.372364,-8.121204,7.685048,2.240401,4.883579,-8.439965,-4.939275,4.583206,-4.803649,1.376407,-0.661381,6.630613,3.131953,-5.785437,-8.067101,6.449623,-6.480971,-6.628319,-7.107920,-1.775981,-6.307281,-6.829515,-1.986483,9.722509,-4.917146,-1.775514,5.772723,9.392923,-5.153839,-0.246024,7.754991,-9.546527,-8.654432,0.915458,-9.774178,-6.973646,4.836386,-4.791602,0.359388,-8.171178,-8.787167,-3.893828,7.494052,5.083564,-8.769151,-3.303910,4.035018,0.081641,6.750824,-8.667686,5.388397,4.914204,0.586897,-6.108273,1.655867,-8.007241,-3.000857,8.000740,-7.193733,1.082104,-0.011278,-1.581092,-0.274036,4.056089,8.500626,-9.255727,7.001342,3.547325,0.874379,8.285744,-3.928957,-3.943078,-7.503059,-1.490197,-8.702235,3.441213,-8.330397,-7.143835,-6.298807,-4.204589,3.473574,-3.837651,-9.370388,-1.372036,5.128272,-2.743161,7.636422,-5.664471,-9.329875,3.466962,2.423607,-0.304014,-0.605064,-6.076452,-5.224690,-1.262112,4.820325,-5.393368,-7.113763,0.768718,-7.794507,-6.931381,9.118487,-3.603104,4.749182,-7.393726,-2.818968,-3.780534,-4.922125,2.479113,-9.576773,-7.293285,-6.241247,8.108650,5.790552,7.459840,7.532528,-5.441464,-2.574327,-4.330098,-9.683457,-3.772245,3.844649,8.168972,-4.440015,6.843316,5.837171,-7.903445,-9.325119,-8.084978,4.764967,-3.443595,0.597782,8.889465,9.568221,-4.120866,-4.825615,-5.131093,0.837386,6.750130,5.984128,-2.237736,7.903218,-7.212046,2.188828,0.928309,-6.472619,7.728395,-7.252257,-2.275884,-7.550708,2.005978,4.313620,8.104562,-6.048637,-2.151911,3.816603,-0.705309,-8.686646,-7.328363,1.397645,-8.203103,0.707777,-5.465559,-4.169098,6.599581,3.348736,8.030840,4.766963,8.380740,-4.173636,1.278522,4.344698,-7.838946,-3.811136,2.957994,-2.642210,-2.283067,3.212626,-0.003673,9.753814,-3.919915,-1.902550,3.460410,-5.100309,3.809564,9.088892,-6.017055,-5.550392,-6.888380,-4.308314,3.966069,9.783806,-5.464937,-7.400209,-4.810576,0.209082,-7.533223,-4.717647,6.062937,-6.419586,4.393639,9.945719,-7.701955,-6.393845,-1.981159,-2.511543,-9.542878,8.394012,-3.812344,1.093567,5.096327,-7.745858,-8.334511,-9.660949,4.595547,5.371189,-8.498974,3.635870,-2.373322,9.945236,-5.517144,-1.596750,6.553055,1.356301,2.390304,-0.942090,9.856442,-4.914351,0.425365,1.481928,-8.389675,-6.755136,0.529674,3.841328,1.288614,3.232449,3.074027,-2.918309,3.488284,-5.353367,-6.272274,-8.367180,9.627841,-6.975389,4.327481,-3.200166,-7.891275,-5.896577,-9.293403,2.337384,-0.312320,8.462656,8.990750,-9.791711,6.983625,7.252628,3.814566,-5.523897,8.684909,6.117651,-4.683517,-4.762518,-6.073754,2.310681,-0.484058,3.496172,6.090847,-0.751598,-4.085003,7.788371,-1.609451,-3.903791,-2.188250,-0.195009,4.859782,-2.646879,4.778163,-8.857923,3.724249,-5.078078,-9.860548,-5.181851,-8.717350,-5.298019,9.937344,8.244897,5.645787,8.293935,-6.585570,2.263180,-1.340244,9.598426,-9.244385,1.130461,7.767459,7.193761,2.584008,5.221696,8.075678,0.361201,-1.420530,-0.793699,-7.307354,5.527804,0.795886,-2.673660,3.607129,-6.999910,7.819849,7.005865,1.761704,-0.856650,2.854893,3.477297,-8.892450,6.596513,9.323366,-6.350117,-2.555611,-4.710524,-7.283331,9.774415,-3.613623,1.851066,4.479168,1.837046,5.328725,-2.961778,2.596718,8.374898,-2.102580,-0.948934,-4.238762,6.145139,8.440838,1.876837,-3.266349,7.550885,-7.224192,-3.714713,4.551300,-5.873002,6.877761,5.890444,-4.271335,-1.725729,-3.495224,-2.166248,0.998520,8.200988,2.154386,-6.895233,4.930394,3.550051,-7.476450,9.322913,3.032957,6.900379,-3.852478,2.954112,3.029472,6.182767,8.147669,5.216435,7.140618,2.052235,4.769176,-4.795573,7.575232,-6.780665,7.576607,4.566770,7.281561,-5.694390,-8.549756,5.141624,4.165840,6.793330,-2.632794,-0.361524,2.400373,2.449324,2.491895,2.258260,8.702315,3.780159,1.959689,4.695457,4.199196,7.198471,6.519860,1.648413,4.403423,2.529061,6.365945,-6.101619,7.305357,1.471715,5.491899,2.800158,-4.828640,-1.696512,-4.273860,9.612737,5.933396,5.541578,8.192961,3.924743,9.836394,-6.017937,-2.780271,2.293474,-3.887980,3.334723,4.611425,-9.596229,8.552606,2.098206,-6.607805,5.367203,3.580562,8.290080,6.503311,-8.135402,0.445828,-5.777321,6.965421,-6.184324,-3.757607,5.548492,-7.397859,-1.000234,-9.238128,7.378525,-1.132354,-7.044352,5.851201,-6.557388,2.296966,7.381161,2.718969,-8.883512,9.643397,4.804345,-9.437773,0.255326,-9.088850,-0.368639,-5.090902,-7.795605,-1.092397,-6.975113,-6.570612,4.163720,0.058854,-8.413058,-2.614808,1.751066,9.406078,2.815572,-9.356953,6.826877,-8.409639,2.373839,6.954453,3.835903,7.730863,-9.915851,-8.729437,6.877292,-9.457127,7.463280,-1.884684,6.891829,7.528277,-8.569779,7.566415,-1.265279,4.968252,-2.593755,4.436618,1.634620,-7.457797,-5.294629,0.194863,-5.443550,-6.133173,-5.050572,8.669793,-2.396862,-3.916285,-3.458099,-5.468562,-4.522952,-7.001203,7.819705,-6.682671,-8.457289,-7.506376,-5.938043,-1.974716,9.034695,-0.451165,-6.697541,1.597496,-0.520094,4.427430,-9.043304,7.413262,8.345651,6.696237,-8.889931,4.711279,-7.166071,6.237372,9.514778,-9.983278,-1.392090,-5.105080,-7.507211,-0.738540,-5.880128,3.519526,6.459396,3.235624,-0.618358,1.266278,-4.848432], dtype = "float32")#candidate|4729|(800,)|const|float32
var_4730 = relay.var("var_4730", dtype = "float32", shape = (21, 1))#candidate|4730|(21, 1)|var|float32
call_4728 = relay.TupleGetItem(func_1326_call(relay.reshape(const_4729.astype('float32'), [5, 10, 16]), relay.reshape(var_4730.astype('float32'), [21, 1]), ), 0)
call_4731 = relay.TupleGetItem(func_1329_call(relay.reshape(const_4729.astype('float32'), [5, 10, 16]), relay.reshape(var_4730.astype('float32'), [21, 1]), ), 0)
bop_4747 = relay.add(var_4730.astype('int32'), const_4729.astype('int32')) # shape=(21, 800)
uop_4755 = relay.cos(var_4730.astype('float32')) # shape=(21, 1)
uop_4757 = relay.sqrt(uop_4755.astype('float64')) # shape=(21, 1)
func_4151_call = mod.get_global_var('func_4151')
func_4152_call = mutated_mod.get_global_var('func_4152')
call_4764 = relay.TupleGetItem(func_4151_call(), 0)
call_4765 = relay.TupleGetItem(func_4152_call(), 0)
output = relay.Tuple([call_4714,call_4722,call_4728,bop_4747,uop_4757,call_4764,])
output2 = relay.Tuple([call_4715,call_4723,call_4731,bop_4747,uop_4757,call_4765,])
func_4766 = relay.Function([var_4730,], output)
mod['func_4766'] = func_4766
mod = relay.transform.InferType()(mod)
var_4767 = relay.var("var_4767", dtype = "float32", shape = (21, 1))#candidate|4767|(21, 1)|var|float32
output = func_4766(var_4767)
func_4768 = relay.Function([var_4767], output)
mutated_mod['func_4768'] = func_4768
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_4842 = relay.TupleGetItem(func_3244_call(), 0)
call_4843 = relay.TupleGetItem(func_3246_call(), 0)
output = call_4842
output2 = call_4843
func_4846 = relay.Function([], output)
mod['func_4846'] = func_4846
mod = relay.transform.InferType()(mod)
output = func_4846()
func_4847 = relay.Function([], output)
mutated_mod['func_4847'] = func_4847
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3752_call = mod.get_global_var('func_3752')
func_3754_call = mutated_mod.get_global_var('func_3754')
call_4858 = relay.TupleGetItem(func_3752_call(), 1)
call_4859 = relay.TupleGetItem(func_3754_call(), 1)
output = call_4858
output2 = call_4859
func_4861 = relay.Function([], output)
mod['func_4861'] = func_4861
mod = relay.transform.InferType()(mod)
output = func_4861()
func_4862 = relay.Function([], output)
mutated_mod['func_4862'] = func_4862
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_4899 = relay.TupleGetItem(func_2564_call(), 0)
call_4900 = relay.TupleGetItem(func_2566_call(), 0)
output = call_4899
output2 = call_4900
func_4907 = relay.Function([], output)
mod['func_4907'] = func_4907
mod = relay.transform.InferType()(mod)
output = func_4907()
func_4908 = relay.Function([], output)
mutated_mod['func_4908'] = func_4908
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4331_call = mod.get_global_var('func_4331')
func_4332_call = mutated_mod.get_global_var('func_4332')
call_4916 = func_4331_call()
call_4917 = func_4331_call()
uop_4928 = relay.rsqrt(call_4916.astype('float32')) # shape=(6, 9, 3)
uop_4930 = relay.rsqrt(call_4917.astype('float32')) # shape=(6, 9, 3)
output = relay.Tuple([uop_4928,])
output2 = relay.Tuple([uop_4930,])
func_4933 = relay.Function([], output)
mod['func_4933'] = func_4933
mod = relay.transform.InferType()(mod)
output = func_4933()
func_4934 = relay.Function([], output)
mutated_mod['func_4934'] = func_4934
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4942 = relay.var("var_4942", dtype = "int64", shape = (1, 16, 7))#candidate|4942|(1, 16, 7)|var|int64
var_4943 = relay.var("var_4943", dtype = "int64", shape = (9, 16, 7))#candidate|4943|(9, 16, 7)|var|int64
bop_4944 = relay.greater_equal(var_4942.astype('bool'), var_4943.astype('bool')) # shape=(9, 16, 7)
output = bop_4944
output2 = bop_4944
func_4952 = relay.Function([var_4942,var_4943,], output)
mod['func_4952'] = func_4952
mod = relay.transform.InferType()(mod)
var_4953 = relay.var("var_4953", dtype = "int64", shape = (1, 16, 7))#candidate|4953|(1, 16, 7)|var|int64
var_4954 = relay.var("var_4954", dtype = "int64", shape = (9, 16, 7))#candidate|4954|(9, 16, 7)|var|int64
output = func_4952(var_4953,var_4954,)
func_4955 = relay.Function([var_4953,var_4954,], output)
mutated_mod['func_4955'] = func_4955
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mod.get_global_var('func_4861')
func_4862_call = mutated_mod.get_global_var('func_4862')
call_4965 = func_4861_call()
call_4966 = func_4861_call()
func_4429_call = mod.get_global_var('func_4429')
func_4434_call = mutated_mod.get_global_var('func_4434')
var_4972 = relay.var("var_4972", dtype = "float64", shape = (945, 2))#candidate|4972|(945, 2)|var|float64
var_4973 = relay.var("var_4973", dtype = "float32", shape = (288,))#candidate|4973|(288,)|var|float32
call_4971 = relay.TupleGetItem(func_4429_call(relay.reshape(var_4972.astype('float64'), [1890,]), relay.reshape(var_4973.astype('float32'), [288,]), relay.reshape(call_4965.astype('float64'), [6, 9, 3]), ), 3)
call_4974 = relay.TupleGetItem(func_4434_call(relay.reshape(var_4972.astype('float64'), [1890,]), relay.reshape(var_4973.astype('float32'), [288,]), relay.reshape(call_4965.astype('float64'), [6, 9, 3]), ), 3)
var_4978 = relay.var("var_4978", dtype = "float32", shape = (288,))#candidate|4978|(288,)|var|float32
bop_4979 = relay.maximum(var_4973.astype('int8'), relay.reshape(var_4978.astype('int8'), relay.shape_of(var_4973))) # shape=(288,)
output = relay.Tuple([call_4965,call_4971,var_4972,bop_4979,])
output2 = relay.Tuple([call_4966,call_4974,var_4972,bop_4979,])
func_4982 = relay.Function([var_4972,var_4973,var_4978,], output)
mod['func_4982'] = func_4982
mod = relay.transform.InferType()(mod)
mutated_mod['func_4982'] = func_4982
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4982_call = mutated_mod.get_global_var('func_4982')
var_4984 = relay.var("var_4984", dtype = "float64", shape = (945, 2))#candidate|4984|(945, 2)|var|float64
var_4985 = relay.var("var_4985", dtype = "float32", shape = (288,))#candidate|4985|(288,)|var|float32
var_4986 = relay.var("var_4986", dtype = "float32", shape = (288,))#candidate|4986|(288,)|var|float32
call_4983 = func_4982_call(var_4984,var_4985,var_4986,)
output = call_4983
func_4987 = relay.Function([var_4984,var_4985,var_4986,], output)
mutated_mod['func_4987'] = func_4987
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_5026 = func_4907_call()
call_5027 = func_4907_call()
uop_5034 = relay.erf(call_5026.astype('float64')) # shape=(6, 9, 3)
uop_5036 = relay.erf(call_5027.astype('float64')) # shape=(6, 9, 3)
func_3287_call = mod.get_global_var('func_3287')
func_3288_call = mutated_mod.get_global_var('func_3288')
call_5049 = relay.TupleGetItem(func_3287_call(), 0)
call_5050 = relay.TupleGetItem(func_3288_call(), 0)
output = relay.Tuple([uop_5034,call_5049,])
output2 = relay.Tuple([uop_5036,call_5050,])
func_5055 = relay.Function([], output)
mod['func_5055'] = func_5055
mod = relay.transform.InferType()(mod)
output = func_5055()
func_5056 = relay.Function([], output)
mutated_mod['func_5056'] = func_5056
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3192_call = mod.get_global_var('func_3192')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_5082 = relay.TupleGetItem(func_3192_call(), 0)
call_5083 = relay.TupleGetItem(func_3193_call(), 0)
func_3406_call = mod.get_global_var('func_3406')
func_3411_call = mutated_mod.get_global_var('func_3411')
var_5094 = relay.var("var_5094", dtype = "float32", shape = (112,))#candidate|5094|(112,)|var|float32
var_5095 = relay.var("var_5095", dtype = "float64", shape = (1, 130))#candidate|5095|(1, 130)|var|float64
const_5096 = relay.const([-2.203492,4.114641,9.144688,5.103814,7.521272,-9.810614,-7.234776,-0.810725,-5.819337,2.671671,8.426409,-6.626608,-6.822731,-2.506974,6.794556,9.015593,-8.398211,5.370726,8.358377,-3.640443,-0.837401,-3.250205,-6.825390,-2.715245,2.911706,-5.875601,9.535352,-8.955796,-7.709187,3.150341,0.626121,6.516244,2.653680,8.281354,7.738630,6.671306,-6.145194,5.417507,8.598314,-0.857111,6.955960,1.177646,5.791635,-8.086189,6.450224,6.958844,-7.026687,-0.497989,6.653311,-8.887086,2.627056,-3.537570,2.207149,2.443114,3.260600,7.773237,-9.942100,1.064397,-6.788467,-2.861424,7.727457,-0.657998,-4.567986,-4.377428,5.065182,2.279156,-4.100476,-6.979929,0.498469,-5.886265,1.237545,2.603323,8.727798,6.619333,-9.542142,7.043306,5.538190,1.214094,-3.534130,-1.442479,6.336355,2.106251,6.720827,8.211354,5.552671,-0.089903,-5.818910,-6.253191,-9.155562,1.881908,6.226353,3.526873,2.991082,6.846397,-8.156456,8.319746,0.727551,1.805597,-3.672912,5.087443,9.663333,9.681398,4.139662,1.915564,8.896644,-9.402348,4.171271,-9.125371,-3.848656,-3.252670,2.976670,-2.808279,-2.134700,6.390682,5.123923,-6.493701,-9.835044,-7.199196,-9.271048,-9.673923,-7.115278,-3.193496,-4.989578,-8.819770,-6.739840,9.744584,-5.049747,-9.451325,3.855646,-7.711956,-6.373756,4.331558,-3.953431,-2.552807,1.637449,-0.111718,4.195757,6.708841,6.785659,2.434538,9.910033,6.395139,-5.204711,-7.733710,-6.475403,-8.357337,-2.570580,1.572640,5.708116,4.936383,-8.473006,0.612675,-2.237167,7.923555,-7.308052,-9.797439,1.820559,-2.861531,6.958133,-7.572181,5.178049,1.385076,-2.764739,-8.899379,-9.358507,4.737332,9.932704,8.976835,9.817841,-2.382899,7.152202,7.336634,-3.693011,-9.732986,2.553704,4.344292,-8.127811,-5.158021,-7.852336,-9.756953,-6.334351,0.765789,-6.532570,5.072068,-4.272653,-4.901672,-7.140936,-8.315238,6.939430,5.634149,9.791280,4.490057,9.958750,1.897334,-3.865496,-6.166045,7.592917,-3.746846,-3.361834,2.439273,7.448816,-4.041342,-5.371711,1.741994,-6.069914,-6.009665,2.435145,8.600273,7.270336,-6.000350,-8.732665,-2.320770,2.018760,-2.517083,-3.596277,-4.232960,7.043774,-1.006754,1.327430,6.393293,-0.021743,-5.986432,4.450886,-5.717920,-0.759121,-1.970891,4.026152,-5.336661,3.156287,3.768031,-0.655901,-7.711467,-2.711190,2.311153,-4.073434,8.008537,-4.823368,-6.032481,3.214715,-7.004361,-8.234892,1.559815,6.072065,-1.396158,-3.699657,2.130511,4.804980,-3.626676,-9.504529,9.106822,-2.473438,1.192256,-0.656802,-5.899889,-8.909010,6.020003,2.811996,-9.194430,-9.559260,8.087886,-4.990333,-7.425797,-3.113527,-2.021831,-9.976674,8.707596,-6.324463,-2.766408,6.692345,9.845870,4.638942,-5.165682,4.340756,-9.229055,6.589914,-8.111389,-7.273415,2.476518,9.085477,7.595515,2.196694,-7.846593,6.289277,5.703224,3.472377,-8.193638,0.266533,7.265443,4.167332,3.382932,5.018487,6.638172,-3.767199,6.174438,-5.482324,4.000715,3.886738,8.559989,-4.701468,7.563263,8.023202,0.385217,-2.319623,0.764713,-2.975289,-6.761814,-9.741724,3.384771,-2.610397,-7.347514,5.944280,6.876006,2.487315,7.328020,7.246084,4.227648,-0.885733,8.069023,5.483314,-9.060930,9.403011,-2.720551,-7.248809,-8.219829,-2.009215,3.792009,3.707066,-3.070722,-6.978426,-1.845518,9.740201,-6.693455,-3.945604,-2.576361,6.038008,3.301867,-7.254924,-1.613054,8.758514,8.907498,-9.152303,9.524615,8.284329,-6.185320,3.720733,1.950049,4.262290,-4.544460,-7.179187,6.714365,-6.233271,-8.108617,-3.531814,6.300419,-7.205467,8.373764,-5.547606,-7.882130,5.520846,5.406779,0.210158,4.954913,-4.611467,2.280503,-0.303580,-1.431936,4.496744,4.835190,-7.172168,-7.023928,-9.693477,9.760233,-4.408427,-7.660840,-7.070120,7.562307,4.954905,-8.421069,-5.021754,-9.119665,5.911229,8.391360,7.056089,-1.903155,-1.696279,-7.780944,4.304992,5.144138,6.877961,3.672241,1.135098,-8.536262,1.478609,-5.712831,-8.703554,-9.235945,-0.207973,-9.439436,5.314705,7.219085,5.168873,-5.300571,7.790007,4.123126,3.654940,-2.335684,0.408076,4.016333,-9.766493,-1.755014,-2.061473,-7.556406,0.489060,0.112457,2.787814,-6.940845,-9.842230,6.119986,-7.940338,0.041916,3.829688,-1.659665,-8.869093,6.044470,8.425470,2.207302,4.715742,-2.867006,-9.250167,1.476318,-6.042468,7.817235,-2.010119,-2.463032,3.449730,-9.301283,-9.979398,6.456469,9.005658,1.284191,-8.524422,-0.303223,-4.383267,-3.473202,-4.377688,-8.286327,2.252151,-8.610856,6.433138,-3.356317,-2.941772,4.650213,0.374338,2.769305,-4.082107,-6.310634,9.721535,-5.238106,2.497910,-7.877341,-6.808274,5.095117,-0.066904,6.533226,-7.683313,-0.772710,-9.884244,6.659266,-5.704836,-2.312078,8.885075,-8.931429,-9.277969,-1.759960,5.185605,1.143647,-3.899797,-8.396486,-8.282929,-2.363638,4.411493,7.963315,-5.946132,-4.770225,7.866111,2.527364,8.446473,7.161063,-7.732542,9.560598,8.445253,4.434880,2.689385,-5.503583,3.614501,3.034855,-6.987158,7.300095,8.591086,0.109378,-0.796146,-7.671002,-3.245293,2.647120,5.584363,5.523626,-3.909345,-2.318033,-9.821641,4.381108,1.683968,-7.297382,-6.171172,1.150389,3.873622,-9.028153,0.848836,5.642024,2.585014,1.169783,-2.826718,9.356386,7.419252,-9.164023,-6.864041,-8.975983,-1.071747,4.698931,-1.995279,6.082451,-9.780544,3.168791,-3.910885,5.163083,-6.605013,-6.244864,2.024533,5.722689,-0.181982,-7.841832,0.257410,-0.315522,-0.776754,-9.896471,-8.551605,-6.893407,-5.481236,0.769462,2.169316,-4.822074,2.363172,-6.218844,-3.871948,5.149972,8.159968,3.487492,-3.079610,5.126475,-0.386699,6.941180,4.276736,0.531182,-1.898587,-2.176719,4.047136,5.210911,6.665569,-5.867571,0.322365,-3.349321,7.991061,5.311036,-5.328185,-2.477972,6.452356,6.555798,-7.036947,-7.822267,8.735507,-5.160137,2.323135,7.270543,9.478272,-7.611410,-5.526123,4.556006,-3.484323,7.214846,2.532615,8.761840,-1.698371,0.862593,4.404988,1.566187,-5.456496,-7.170196,2.875954,4.110174,6.495524,6.529459,-9.085723,8.632750,1.365663,7.147975,6.744297,5.727206,-9.513313,-6.807942,-8.935158,-0.994983,3.823919,-4.245871,3.974203,2.973119,2.852214,-5.202119,0.707020,3.980107,-3.760642,-9.522334,9.791181,8.107947,-5.242236,-1.242264,2.594241,-3.976998,3.768398,1.285852,-6.383092,1.436603,1.515635,1.769994,7.469940,-0.406037,-7.545605,4.015477,-8.246688,0.770934,-6.687265,-8.475962,-3.259987,-8.544654,6.233186,-7.296083,-2.021665,-9.648275,4.592599,9.048625,-7.500634,3.778655,-8.183621,-6.504563,7.864530,3.244308,1.698663,-3.235473,-4.297569,5.252453,-2.230997,7.775154,9.158048,5.529522,-4.459158,-8.759975,-4.711639,8.350965,-9.962169,5.279528,1.980952,-6.969269,-3.728566,-6.025127,4.201129,8.815290,-2.207388,9.321396,-5.016269,-8.425040,6.981597,3.667495,-6.320932,-8.422923,-1.558591,5.843424,-2.603828,2.364082,-1.840599,-4.571545,1.838526,9.171277,-3.837775,-1.524482,6.434378,5.935050,1.899526,-1.492358,9.489435,-8.599824,4.739119,4.108989,2.959278,-7.596866,5.789202,-5.866511,-8.197361,-2.343494,-7.235158,4.426799,8.965578,-4.115430,5.329563,7.565433,4.200696,0.939285,2.584451,-7.151929,1.710676,-0.685314,3.753110,2.297216,-4.973587,0.997894,-5.971405,5.051344,4.869383,-1.202858,-3.843508,-4.853646,-3.391416,-4.490234,-8.297167,-6.356102,-1.723714,-9.060263,8.020054,0.539812,5.284230,-3.339424,-8.155357,-3.456904,7.247888,-5.711556,-0.157434,4.573444,-8.527513,-3.102462,2.149090,-1.560959,0.850174,3.864695,5.345932,-1.981776,7.674844,-4.066966,-5.033025,-0.450834,-6.346940,-7.659650,0.828366,5.184863,0.366667,-3.825604,-2.412511,-6.696007,-6.737197,4.952324,6.170608,-9.189019,-6.235442,-3.826789,1.002646,6.439713,1.247008,-6.858907,3.403735,2.404421,7.587796,8.153340,-2.791752,0.454158,-2.356704,-6.245799,6.624177,-9.766238,-7.717802,-6.967996,9.099568,5.841622,6.628574,9.122914,4.233433,-5.393619,1.023089,-5.671505,1.140875,-5.805793,-5.656822,0.735706,9.299844,-9.757052], dtype = "float32")#candidate|5096|(800,)|const|float32
call_5093 = relay.TupleGetItem(func_3406_call(relay.reshape(var_5094.astype('float32'), [8, 14, 1]), relay.reshape(var_5095.astype('float64'), [26, 5]), relay.reshape(const_5096.astype('float32'), [800,]), ), 0)
call_5097 = relay.TupleGetItem(func_3411_call(relay.reshape(var_5094.astype('float32'), [8, 14, 1]), relay.reshape(var_5095.astype('float64'), [26, 5]), relay.reshape(const_5096.astype('float32'), [800,]), ), 0)
uop_5102 = relay.atanh(var_5095.astype('float32')) # shape=(1, 130)
func_3576_call = mod.get_global_var('func_3576')
func_3580_call = mutated_mod.get_global_var('func_3580')
const_5105 = relay.const([[True,False,True,False],[True,True,False,False],[True,True,False,False],[True,True,True,False],[False,True,True,True],[True,True,False,True],[True,False,True,False],[False,False,False,True],[False,True,True,True],[False,False,True,True],[True,False,True,False],[True,True,True,True],[False,False,False,False],[True,True,True,True],[True,False,True,True],[False,True,True,False],[False,False,True,False],[False,True,True,False],[True,True,False,False],[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,False,False,True],[True,True,True,False],[True,True,False,False],[False,False,False,True],[True,False,True,True],[False,True,True,False],[False,False,True,True],[False,False,False,False],[False,False,True,True],[True,True,True,False],[False,False,False,False],[False,False,True,True],[True,False,False,True],[False,True,True,False],[True,False,True,True],[False,True,False,False],[True,True,False,False],[False,True,True,False],[True,True,False,True],[False,True,False,True],[False,False,False,False],[False,True,False,True],[True,True,True,False],[True,True,False,False],[False,False,True,True],[False,False,True,True],[True,False,True,True],[True,True,False,True],[False,False,True,False],[True,True,True,True],[True,False,True,False],[True,True,False,False],[False,True,True,False],[True,False,True,True],[False,False,False,False],[False,True,True,False],[True,True,False,True],[False,True,False,True],[False,True,True,True],[False,False,True,False],[True,False,False,True],[True,False,False,True],[False,False,True,False],[True,True,False,True],[False,False,False,False],[False,False,False,False],[True,True,True,True],[True,True,False,True],[True,False,False,False],[False,False,False,True],[False,True,True,False],[False,False,True,False],[False,True,True,False],[True,True,False,False],[False,False,True,False],[True,True,True,False],[False,True,True,False],[True,True,True,True],[False,True,True,True],[True,False,True,True],[True,False,False,False],[True,False,False,False],[False,False,False,True],[True,True,False,True],[False,True,False,True],[False,True,False,False],[False,False,True,True],[False,True,True,False],[True,True,False,True],[True,True,True,False],[True,True,True,False],[False,True,False,False],[False,False,True,False],[True,True,True,False],[True,False,True,False],[True,False,False,True]], dtype = "bool")#candidate|5105|(98, 4)|const|bool
call_5104 = relay.TupleGetItem(func_3576_call(relay.reshape(const_5105.astype('bool'), [7, 14, 4]), relay.reshape(const_5096.astype('float32'), [800,]), relay.reshape(call_5082.astype('bool'), [6, 9, 3]), ), 5)
call_5106 = relay.TupleGetItem(func_3580_call(relay.reshape(const_5105.astype('bool'), [7, 14, 4]), relay.reshape(const_5096.astype('float32'), [800,]), relay.reshape(call_5082.astype('bool'), [6, 9, 3]), ), 5)
func_122_call = mod.get_global_var('func_122')
func_124_call = mutated_mod.get_global_var('func_124')
var_5110 = relay.var("var_5110", dtype = "float32", shape = (144,))#candidate|5110|(144,)|var|float32
call_5109 = func_122_call(relay.reshape(var_5110.astype('float32'), [4, 6, 6]))
call_5111 = func_122_call(relay.reshape(var_5110.astype('float32'), [4, 6, 6]))
func_4464_call = mod.get_global_var('func_4464')
func_4466_call = mutated_mod.get_global_var('func_4466')
call_5118 = func_4464_call()
call_5119 = func_4464_call()
output = relay.Tuple([call_5082,call_5093,var_5094,const_5096,uop_5102,call_5104,const_5105,call_5109,var_5110,call_5118,])
output2 = relay.Tuple([call_5083,call_5097,var_5094,const_5096,uop_5102,call_5106,const_5105,call_5111,var_5110,call_5119,])
func_5121 = relay.Function([var_5094,var_5095,var_5110,], output)
mod['func_5121'] = func_5121
mod = relay.transform.InferType()(mod)
mutated_mod['func_5121'] = func_5121
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5121_call = mutated_mod.get_global_var('func_5121')
var_5123 = relay.var("var_5123", dtype = "float32", shape = (112,))#candidate|5123|(112,)|var|float32
var_5124 = relay.var("var_5124", dtype = "float64", shape = (1, 130))#candidate|5124|(1, 130)|var|float64
var_5125 = relay.var("var_5125", dtype = "float32", shape = (144,))#candidate|5125|(144,)|var|float32
call_5122 = func_5121_call(var_5123,var_5124,var_5125,)
output = call_5122
func_5126 = relay.Function([var_5123,var_5124,var_5125,], output)
mutated_mod['func_5126'] = func_5126
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3244_call = mod.get_global_var('func_3244')
func_3246_call = mutated_mod.get_global_var('func_3246')
call_5133 = relay.TupleGetItem(func_3244_call(), 0)
call_5134 = relay.TupleGetItem(func_3246_call(), 0)
output = call_5133
output2 = call_5134
func_5136 = relay.Function([], output)
mod['func_5136'] = func_5136
mod = relay.transform.InferType()(mod)
output = func_5136()
func_5137 = relay.Function([], output)
mutated_mod['func_5137'] = func_5137
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2171_call = mod.get_global_var('func_2171')
func_2172_call = mutated_mod.get_global_var('func_2172')
call_5167 = func_2171_call()
call_5168 = func_2171_call()
output = relay.Tuple([call_5167,])
output2 = relay.Tuple([call_5168,])
func_5182 = relay.Function([], output)
mod['func_5182'] = func_5182
mod = relay.transform.InferType()(mod)
mutated_mod['func_5182'] = func_5182
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5182_call = mutated_mod.get_global_var('func_5182')
call_5183 = func_5182_call()
output = call_5183
func_5184 = relay.Function([], output)
mutated_mod['func_5184'] = func_5184
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mod.get_global_var('func_4861')
func_4862_call = mutated_mod.get_global_var('func_4862')
call_5213 = func_4861_call()
call_5214 = func_4861_call()
output = relay.Tuple([call_5213,])
output2 = relay.Tuple([call_5214,])
func_5219 = relay.Function([], output)
mod['func_5219'] = func_5219
mod = relay.transform.InferType()(mod)
output = func_5219()
func_5220 = relay.Function([], output)
mutated_mod['func_5220'] = func_5220
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_5228 = func_3004_call()
call_5229 = func_3004_call()
var_5236 = relay.var("var_5236", dtype = "bool", shape = (6, 9, 3))#candidate|5236|(6, 9, 3)|var|bool
bop_5237 = relay.bitwise_or(call_5228.astype('uint8'), relay.reshape(var_5236.astype('uint8'), relay.shape_of(call_5228))) # shape=(6, 9, 3)
bop_5240 = relay.bitwise_or(call_5229.astype('uint8'), relay.reshape(var_5236.astype('uint8'), relay.shape_of(call_5229))) # shape=(6, 9, 3)
func_3801_call = mod.get_global_var('func_3801')
func_3805_call = mutated_mod.get_global_var('func_3805')
const_5259 = relay.const([4.315898,-8.042829,-6.964385,3.971687,4.250846,-6.037951,-6.789734,4.178223,-8.658191,4.194365,1.430247,4.999616,-1.879302,-2.803755,3.599644,6.112595,-7.314871,-7.487473,0.273247,3.902121,9.953715,-6.274170,-0.564532,6.329595,-8.575635,-0.196456,-0.319937,5.925796,-0.198562,-2.410949,-5.522344,-2.761094,-0.563494,5.540463,-3.418085,-6.909737,-0.885957,-6.882859,7.638029,4.847532,-1.335017,5.035974,-2.012641,6.542947,-5.445226,-2.503146,3.709608,3.907088,9.816771,-9.632016,-2.352035,2.267073,6.319330,5.587512,-4.202875,-1.310431,-5.656093,6.609846,9.506862,0.642334,2.206355,-3.975159,-8.875833,-4.001392,-6.469010,-8.421548,9.536275,4.052366,6.424537,7.354630,-6.648042,-5.577502,1.923968,9.352284,-8.106504,8.341508,-8.900319,-4.504378,7.792510,-2.757352,4.797573,-7.319658,-3.140579,-1.966243,-4.557902,1.536129,7.944737,7.832883,-3.496473,5.821789,3.985052,-6.842147,-9.713192,1.324101,1.694317,7.000103,-3.873453,1.115115,-3.841058,-9.378076,-4.204861,9.484416,6.975536,-4.876150,4.367401,-5.541960,-3.281241,-6.757504,8.873614,0.230097,8.618534,-6.117167,-5.844946,-9.163166,3.755038,-6.415736,8.555484,6.704372,-5.551967,-0.331962,-1.119709,8.959481,9.741098,6.153532,2.735789,1.587481,-3.824689,-0.476036,9.325415,1.978109], dtype = "float64")#candidate|5259|(130,)|const|float64
const_5260 = relay.const([1.035703,8.892066,-3.717464,7.166744,-4.471447,1.044128,-0.446241,-7.060463,4.840143,-6.965570,4.491026,9.388984,4.407299,3.083744,-2.607991,9.792221,-7.448082,4.401185,-4.369532,2.310050,6.244572], dtype = "float32")#candidate|5260|(21,)|const|float32
var_5261 = relay.var("var_5261", dtype = "float32", shape = (462,))#candidate|5261|(462,)|var|float32
call_5258 = relay.TupleGetItem(func_3801_call(relay.reshape(const_5259.astype('float64'), [1, 130]), relay.reshape(const_5260.astype('float32'), [21,]), relay.reshape(var_5261.astype('float32'), [462,]), ), 6)
call_5262 = relay.TupleGetItem(func_3805_call(relay.reshape(const_5259.astype('float64'), [1, 130]), relay.reshape(const_5260.astype('float32'), [21,]), relay.reshape(var_5261.astype('float32'), [462,]), ), 6)
output = relay.Tuple([bop_5237,call_5258,const_5259,const_5260,var_5261,])
output2 = relay.Tuple([bop_5240,call_5262,const_5259,const_5260,var_5261,])
func_5263 = relay.Function([var_5236,var_5261,], output)
mod['func_5263'] = func_5263
mod = relay.transform.InferType()(mod)
var_5264 = relay.var("var_5264", dtype = "bool", shape = (6, 9, 3))#candidate|5264|(6, 9, 3)|var|bool
var_5265 = relay.var("var_5265", dtype = "float32", shape = (462,))#candidate|5265|(462,)|var|float32
output = func_5263(var_5264,var_5265,)
func_5266 = relay.Function([var_5264,var_5265,], output)
mutated_mod['func_5266'] = func_5266
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3210_call = mod.get_global_var('func_3210')
func_3211_call = mutated_mod.get_global_var('func_3211')
call_5279 = func_3210_call()
call_5280 = func_3210_call()
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
var_5289 = relay.var("var_5289", dtype = "float32", shape = (135,))#candidate|5289|(135,)|var|float32
call_5288 = relay.TupleGetItem(func_560_call(relay.reshape(var_5289.astype('float32'), [15, 3, 3])), 0)
call_5290 = relay.TupleGetItem(func_563_call(relay.reshape(var_5289.astype('float32'), [15, 3, 3])), 0)
output = relay.Tuple([call_5279,call_5288,var_5289,])
output2 = relay.Tuple([call_5280,call_5290,var_5289,])
func_5298 = relay.Function([var_5289,], output)
mod['func_5298'] = func_5298
mod = relay.transform.InferType()(mod)
var_5299 = relay.var("var_5299", dtype = "float32", shape = (135,))#candidate|5299|(135,)|var|float32
output = func_5298(var_5299)
func_5300 = relay.Function([var_5299], output)
mutated_mod['func_5300'] = func_5300
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5353 = relay.var("var_5353", dtype = "bool", shape = (8, 16, 11))#candidate|5353|(8, 16, 11)|var|bool
var_5354 = relay.var("var_5354", dtype = "bool", shape = (8, 16, 11))#candidate|5354|(8, 16, 11)|var|bool
bop_5355 = relay.logical_and(var_5353.astype('bool'), relay.reshape(var_5354.astype('bool'), relay.shape_of(var_5353))) # shape=(8, 16, 11)
func_3576_call = mod.get_global_var('func_3576')
func_3580_call = mutated_mod.get_global_var('func_3580')
var_5361 = relay.var("var_5361", dtype = "bool", shape = (392,))#candidate|5361|(392,)|var|bool
var_5362 = relay.var("var_5362", dtype = "float32", shape = (8, 100))#candidate|5362|(8, 100)|var|float32
var_5363 = relay.var("var_5363", dtype = "bool", shape = (162,))#candidate|5363|(162,)|var|bool
call_5360 = relay.TupleGetItem(func_3576_call(relay.reshape(var_5361.astype('bool'), [7, 14, 4]), relay.reshape(var_5362.astype('float32'), [800,]), relay.reshape(var_5363.astype('bool'), [6, 9, 3]), ), 5)
call_5364 = relay.TupleGetItem(func_3580_call(relay.reshape(var_5361.astype('bool'), [7, 14, 4]), relay.reshape(var_5362.astype('float32'), [800,]), relay.reshape(var_5363.astype('bool'), [6, 9, 3]), ), 5)
func_3426_call = mod.get_global_var('func_3426')
func_3430_call = mutated_mod.get_global_var('func_3430')
const_5367 = relay.const([True,False,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,False,True,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,False,True,False,True,True,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,False,False,True,True,False,True,False,False,True,True,True,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,False,False,False,False,False,True,True,True,False,True,True,True,True,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,True,True,True,False,False,True,True,False,False,True,False,False,True,True,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,True,True,False,False,False,True,False,True,True,True,False,False,False,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,True,False], dtype = "bool")#candidate|5367|(780,)|const|bool
call_5366 = func_3426_call(relay.reshape(const_5367.astype('bool'), [13, 10, 6]), relay.reshape(const_5367.astype('bool'), [13, 10, 6]), )
call_5368 = func_3426_call(relay.reshape(const_5367.astype('bool'), [13, 10, 6]), relay.reshape(const_5367.astype('bool'), [13, 10, 6]), )
output = relay.Tuple([bop_5355,call_5360,var_5361,var_5362,var_5363,call_5366,const_5367,])
output2 = relay.Tuple([bop_5355,call_5364,var_5361,var_5362,var_5363,call_5368,const_5367,])
func_5369 = relay.Function([var_5353,var_5354,var_5361,var_5362,var_5363,], output)
mod['func_5369'] = func_5369
mod = relay.transform.InferType()(mod)
var_5370 = relay.var("var_5370", dtype = "bool", shape = (8, 16, 11))#candidate|5370|(8, 16, 11)|var|bool
var_5371 = relay.var("var_5371", dtype = "bool", shape = (8, 16, 11))#candidate|5371|(8, 16, 11)|var|bool
var_5372 = relay.var("var_5372", dtype = "bool", shape = (392,))#candidate|5372|(392,)|var|bool
var_5373 = relay.var("var_5373", dtype = "float32", shape = (8, 100))#candidate|5373|(8, 100)|var|float32
var_5374 = relay.var("var_5374", dtype = "bool", shape = (162,))#candidate|5374|(162,)|var|bool
output = func_5369(var_5370,var_5371,var_5372,var_5373,var_5374,)
func_5375 = relay.Function([var_5370,var_5371,var_5372,var_5373,var_5374,], output)
mutated_mod['func_5375'] = func_5375
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5408 = relay.var("var_5408", dtype = "float32", shape = (4, 6, 2))#candidate|5408|(4, 6, 2)|var|float32
uop_5409 = relay.log10(var_5408.astype('float32')) # shape=(4, 6, 2)
bop_5426 = relay.bitwise_or(uop_5409.astype('uint16'), relay.reshape(var_5408.astype('uint16'), relay.shape_of(uop_5409))) # shape=(4, 6, 2)
func_5369_call = mod.get_global_var('func_5369')
func_5375_call = mutated_mod.get_global_var('func_5375')
const_5434 = relay.const([True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,True,False,True,False,False,False,False,True,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,True,False,True,False,True,False,True,True,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,True,False,True,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,True,True,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,False,False,False,False,False,True,False,False,False,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,False,False,False,True,False,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,True,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,True,True,False,False,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,False,False,False,True,False,True,True,False,False,True,True,False,False,False,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,True,False,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,True,True,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,True,True,False,True,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,False,False,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True], dtype = "bool")#candidate|5434|(1408,)|const|bool
const_5435 = relay.const([True,False,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,True,False,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,False,True,False,False,True,True,False,False,True,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,True,True,True,True,False,True,True,True,True,True,True,False,False,False,True,False,True,False,True,True,True,False,False,False,True,False,True,False,False,True,True,True,False,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,False,True,False,True,True,False,False,False,True,True,False,False,False,True,False,True], dtype = "bool")#candidate|5435|(392,)|const|bool
const_5436 = relay.const([-1.894751,-9.078798,-1.455559,5.980496,-0.154712,-2.082633,-5.426619,2.157874,-3.289722,1.954470,-3.922394,-1.974291,4.719039,-1.268757,8.705025,2.623395,5.350190,5.476500,1.603153,-9.712926,4.965673,-5.017397,2.700644,0.110960,-4.986033,6.501212,1.592261,-1.118496,-9.500526,9.149568,-2.869887,-2.022828,-0.928780,9.671415,-0.240969,-6.699861,-2.636253,8.647573,-2.560716,4.889174,5.701261,-4.753107,-4.053568,2.263078,4.085736,1.112028,5.709025,-5.972913,4.166841,1.063085,8.220341,8.473740,4.234440,9.823652,-3.772830,-3.800477,9.950237,-6.322377,-6.803622,8.176252,-4.139751,3.162004,-2.221873,-1.800335,7.200332,1.272453,5.544440,4.071400,3.351433,-8.205964,2.015364,4.609062,2.068154,0.063551,-5.173078,-9.070890,2.615477,-9.543960,0.660010,6.829917,6.910503,4.980503,3.134849,8.613776,0.145510,-4.210286,-5.889255,0.835562,6.006889,9.699577,1.403708,8.688883,4.450693,-5.747341,-9.687994,-6.576662,-3.293678,-5.135273,-3.874517,-4.982745,2.684468,-3.062639,6.577747,-8.524809,-0.678828,-5.827564,2.167870,-0.712174,5.476788,0.820344,-0.057497,6.083859,9.728211,7.512960,0.875048,9.382045,-5.918301,0.707205,5.833378,4.062504,7.947297,-8.770936,9.769713,-1.630115,6.919947,-5.354569,8.587928,7.620421,2.844639,-2.310997,-6.954478,4.424438,3.240064,-4.608817,-9.370987,3.594093,0.021678,-5.447649,-7.324446,-0.646239,-5.269654,-6.919219,-6.608823,-2.802123,-6.715774,0.263468,-8.681457,3.701845,9.644978,9.135635,3.654612,9.417125,-0.216168,9.884425,-8.890189,-4.227312,-1.894425,-6.234524,-3.302190,-7.117967,0.697846,-6.760233,0.971074,-3.447217,7.232997,-8.260625,-8.636547,-1.139318,-7.851660,2.050140,4.882833,5.722053,-8.269442,-3.013112,7.766261,0.159624,-3.137067,-3.478035,-3.298577,-7.911013,-2.216555,-6.612288,4.665769,2.868146,9.421646,-9.122118,5.567968,-9.411178,-1.396953,-2.737767,-0.056932,-4.227582,1.211535,-4.633473,4.569618,-7.849858,4.160832,-7.841908,3.616237,-0.061326,9.206872,5.643393,9.215027,-9.505882,-5.734059,7.156880,3.369960,-6.010202,-6.954859,-4.306847,9.127593,-3.084652,9.873051,9.397178,-3.141881,0.885222,7.960262,-3.145113,0.859733,-7.707487,-3.705950,-7.847133,0.349614,-9.295069,7.377932,-6.160633,1.480132,9.999518,6.684316,5.163834,3.251326,4.060902,5.546471,6.031231,2.076351,9.426542,8.728779,3.081651,-6.723964,-3.848229,-6.858056,-4.162887,7.428854,-5.836063,6.000222,9.323765,3.621095,8.970663,-0.697166,7.488991,-4.154829,3.742194,-4.328390,-1.518411,6.177654,-6.159133,8.683906,1.708935,-2.087845,-0.794145,-6.823232,-1.566827,-3.708347,-8.204970,-8.098993,-3.217920,-7.918288,-0.779583,-5.245864,9.224156,-1.706452,4.382978,0.092961,-0.623182,8.262972,5.246588,-9.012178,6.111833,4.323303,-3.529484,9.750390,-3.019253,-5.170458,-0.084826,8.425955,-9.949055,4.223885,-0.816664,0.216850,-5.222619,7.073456,-5.775533,-8.920359,-6.206178,8.040558,9.056009,-7.272859,9.795152,6.889158,8.978202,0.844560,-9.582216,-0.034686,5.419592,2.788576,-8.066360,0.694556,4.380087,-8.020064,9.033779,-8.403042,-3.546205,-0.530517,9.739803,4.680521,6.501526,7.100660,2.898641,-6.148693,7.828859,-1.379236,-1.246714,-3.873018,9.502310,4.167127,-2.449455,-8.425840,-3.086425,-6.775669,-8.648928,9.495618,9.378980,8.247196,-3.914785,3.970289,3.416879,3.277266,-3.031173,9.068550,-3.769198,-2.533182,-7.033937,1.015420,-7.326147,5.636041,6.084362,-7.445519,6.942388,7.099998,8.830566,3.218481,-9.026514,-6.708425,-9.780970,9.299979,-8.482474,1.894988,-0.887978,-9.220108,8.393388,7.651187,-0.603464,2.611609,9.120233,4.807778,3.105337,3.991983,6.532588,-4.216941,-4.758577,-6.133108,-8.253061,4.889310,-5.402894,3.759181,6.567518,-4.342715,-4.855470,2.619509,-0.459368,-7.395128,1.401228,2.175874,3.789457,-9.033578,6.560222,-8.314337,1.660670,-6.893790,8.284814,9.160788,-0.548524,-3.018886,2.981725,-6.561558,-9.649096,7.547945,6.584495,-8.519034,0.382113,-4.769511,8.315077,-4.448997,-7.330766,-0.434520,-9.506333,4.138647,1.194684,9.630021,8.369046,-9.052721,-0.980792,-7.503617,1.871492,-2.329034,1.982812,5.343036,9.678189,0.432931,9.669641,-7.141309,4.392004,-3.508592,3.147574,1.168936,-5.977036,2.146265,-2.973260,-6.517325,-4.158356,-1.781045,5.384408,2.624401,0.002364,-8.736154,-2.662418,-8.473490,-9.021970,6.621838,-0.758009,3.966664,-9.904651,0.397223,-3.387546,-4.667767,-2.822335,-2.267826,6.435349,-0.604427,6.525400,5.370371,7.877208,8.205085,-8.381013,-7.322066,-0.576202,9.776961,-3.464201,1.752666,-8.949284,4.562708,-3.503513,-3.325405,2.913125,-4.717774,-6.996944,4.371038,0.395764,0.486948,3.816174,-2.960312,6.750712,-0.263399,-4.685923,-2.869579,-0.645679,9.158709,-0.601466,-6.232930,-1.604032,-0.601792,-5.837327,1.798094,-4.788610,3.682339,-4.889706,8.091484,-5.475374,8.023307,0.447723,7.295547,4.846460,-7.891597,9.494425,-0.737312,9.870277,-8.236077,-8.183148,4.123485,-4.320895,-8.129872,-6.968829,7.717526,9.212120,0.152255,-9.063278,-3.631509,0.255057,1.190912,1.255656,7.393520,-8.220030,-7.306218,8.979805,-4.276137,2.206492,-8.096378,-7.656107,-9.012705,-5.698839,3.780393,-5.656501,-4.458419,-7.195435,-8.022159,6.699032,3.938526,9.677053,-6.322118,3.758370,2.497103,8.369659,8.453643,0.337263,-8.433420,4.927674,-8.387988,8.568916,-0.502615,5.482204,-9.272999,-6.009534,-8.303992,2.313629,-6.637316,2.235262,2.958908,1.592499,2.875545,-8.349061,-1.059852,1.103929,-8.806364,2.348762,-7.697828,4.152305,-8.933777,-3.300719,-8.672976,5.643616,0.990086,-8.813038,-5.809140,6.421333,-3.682866,7.481612,6.211897,8.903593,4.199773,-6.318881,2.199167,-5.356934,3.688173,2.082656,0.327774,-7.201961,2.164951,0.860416,-1.664139,0.084859,3.550648,6.781765,3.742438,-2.758998,-0.982072,0.633994,-6.586458,4.312945,-8.293943,8.733814,7.979262,-5.201240,-0.255494,-6.948024,-7.000186,5.706653,-1.927465,9.934861,-8.402386,8.303988,-5.350775,-3.107836,-2.931763,1.214683,-3.680305,-2.074497,-4.016137,1.080875,6.893401,-5.157764,1.591362,6.701922,-8.552470,-8.780196,-7.598170,4.614227,-6.434500,3.317020,8.586848,7.407170,-0.209595,-7.762483,2.956426,4.060767,5.772468,-0.012081,-6.480062,7.924693,-6.787375,2.178093,6.154981,-9.199145,-8.884589,-7.599505,-0.330665,-6.131843,-6.154899,3.770268,-1.893119,-9.002729,-6.559106,-3.700658,-2.323963,-0.273603,9.633903,4.309928,-0.255055,-2.914269,7.514808,5.932835,4.544007,-0.681401,-1.109068,4.185411,1.510393,-2.698423,-2.459834,-8.352459,-6.924802,-4.829153,-5.128317,-5.213269,2.697413,8.632236,-0.952424,-6.119744,-6.132224,9.924494,-2.057584,4.200670,-1.438170,-8.217236,2.406707,7.031553,1.175230,6.705686,6.178022,-0.523448,2.463074,8.698336,-5.557753,3.133554,5.831674,6.957537,6.778081,8.417749,5.885533,-0.157373,-3.960787,-0.739582,3.758397,9.375532,-0.348830,6.481985,3.870443,3.925078,-0.571824,8.002855,5.771035,-1.338319,3.645182,-0.662439,6.275345,2.858450,-0.337852,6.405300,-3.378277,-4.431597,-5.220484,-3.704475,-4.431856,-7.903813,-5.142997,-5.950668,-9.101230,-0.883104,-5.275541,-6.543483,9.769010,4.125154,-8.498013,-6.598778,6.721149,7.261064,-2.920463,-0.434782,3.836305,-2.724717,-0.716020,1.358488,3.016886,-1.342416,-0.026034,4.495483,9.601473,0.397186,5.035508,-8.262583,-5.963037,-0.011192,9.437365,4.117065,0.180236,-0.309878,7.143088,1.853140,8.458429,-6.689315,-3.282714,8.894462,0.555172,4.079072,-1.887900,2.077533,7.980202,-7.759726,-5.633080,8.204672,7.988064,6.486877,4.632146,2.340337,7.177435,-5.635569,4.379257,5.559720,-3.507395,1.593404,-0.660823,8.656277,-6.252472,-1.435505,-0.294274,1.952797,9.015692,-6.304383,7.903724,5.098536,0.720142,-4.069768,7.700744,1.187488,4.365057,4.755565,-7.651298,9.852806,-4.874457,3.713565,-4.959067,-2.175110,-2.384341,-9.650591,-9.095600,-7.578419,-8.954737,-7.258880,-9.194193,4.248750,-7.565813,5.586993], dtype = "float32")#candidate|5436|(800,)|const|float32
var_5437 = relay.var("var_5437", dtype = "bool", shape = (162,))#candidate|5437|(162,)|var|bool
call_5433 = relay.TupleGetItem(func_5369_call(relay.reshape(const_5434.astype('bool'), [8, 16, 11]), relay.reshape(const_5434.astype('bool'), [8, 16, 11]), relay.reshape(const_5435.astype('bool'), [392,]), relay.reshape(const_5436.astype('float32'), [8, 100]), relay.reshape(var_5437.astype('bool'), [162,]), ), 6)
call_5438 = relay.TupleGetItem(func_5375_call(relay.reshape(const_5434.astype('bool'), [8, 16, 11]), relay.reshape(const_5434.astype('bool'), [8, 16, 11]), relay.reshape(const_5435.astype('bool'), [392,]), relay.reshape(const_5436.astype('float32'), [8, 100]), relay.reshape(var_5437.astype('bool'), [162,]), ), 6)
func_1529_call = mod.get_global_var('func_1529')
func_1533_call = mutated_mod.get_global_var('func_1533')
var_5453 = relay.var("var_5453", dtype = "int64", shape = (78, 4))#candidate|5453|(78, 4)|var|int64
call_5452 = relay.TupleGetItem(func_1529_call(relay.reshape(var_5453.astype('int64'), [6, 13, 4]), relay.reshape(var_5453.astype('int64'), [6, 13, 4]), ), 0)
call_5454 = relay.TupleGetItem(func_1533_call(relay.reshape(var_5453.astype('int64'), [6, 13, 4]), relay.reshape(var_5453.astype('int64'), [6, 13, 4]), ), 0)
func_1326_call = mod.get_global_var('func_1326')
func_1329_call = mutated_mod.get_global_var('func_1329')
var_5476 = relay.var("var_5476", dtype = "float32", shape = (21,))#candidate|5476|(21,)|var|float32
call_5475 = relay.TupleGetItem(func_1326_call(relay.reshape(const_5436.astype('float32'), [5, 10, 16]), relay.reshape(var_5476.astype('float32'), [21, 1]), ), 1)
call_5477 = relay.TupleGetItem(func_1329_call(relay.reshape(const_5436.astype('float32'), [5, 10, 16]), relay.reshape(var_5476.astype('float32'), [21, 1]), ), 1)
output = relay.Tuple([bop_5426,call_5433,const_5434,const_5435,const_5436,var_5437,call_5452,var_5453,call_5475,var_5476,])
output2 = relay.Tuple([bop_5426,call_5438,const_5434,const_5435,const_5436,var_5437,call_5454,var_5453,call_5477,var_5476,])
func_5491 = relay.Function([var_5408,var_5437,var_5453,var_5476,], output)
mod['func_5491'] = func_5491
mod = relay.transform.InferType()(mod)
mutated_mod['func_5491'] = func_5491
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5491_call = mutated_mod.get_global_var('func_5491')
var_5493 = relay.var("var_5493", dtype = "float32", shape = (4, 6, 2))#candidate|5493|(4, 6, 2)|var|float32
var_5494 = relay.var("var_5494", dtype = "bool", shape = (162,))#candidate|5494|(162,)|var|bool
var_5495 = relay.var("var_5495", dtype = "int64", shape = (78, 4))#candidate|5495|(78, 4)|var|int64
var_5496 = relay.var("var_5496", dtype = "float32", shape = (21,))#candidate|5496|(21,)|var|float32
call_5492 = func_5491_call(var_5493,var_5494,var_5495,var_5496,)
output = call_5492
func_5497 = relay.Function([var_5493,var_5494,var_5495,var_5496,], output)
mutated_mod['func_5497'] = func_5497
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_5537 = func_4907_call()
call_5538 = func_4907_call()
output = call_5537
output2 = call_5538
func_5553 = relay.Function([], output)
mod['func_5553'] = func_5553
mod = relay.transform.InferType()(mod)
output = func_5553()
func_5554 = relay.Function([], output)
mutated_mod['func_5554'] = func_5554
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3004_call = mod.get_global_var('func_3004')
func_3006_call = mutated_mod.get_global_var('func_3006')
call_5568 = func_3004_call()
call_5569 = func_3004_call()
output = relay.Tuple([call_5568,])
output2 = relay.Tuple([call_5569,])
func_5587 = relay.Function([], output)
mod['func_5587'] = func_5587
mod = relay.transform.InferType()(mod)
output = func_5587()
func_5588 = relay.Function([], output)
mutated_mod['func_5588'] = func_5588
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_5686 = func_4907_call()
call_5687 = func_4907_call()
output = call_5686
output2 = call_5687
func_5700 = relay.Function([], output)
mod['func_5700'] = func_5700
mod = relay.transform.InferType()(mod)
mutated_mod['func_5700'] = func_5700
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5700_call = mutated_mod.get_global_var('func_5700')
call_5701 = func_5700_call()
output = call_5701
func_5702 = relay.Function([], output)
mutated_mod['func_5702'] = func_5702
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3210_call = mod.get_global_var('func_3210')
func_3211_call = mutated_mod.get_global_var('func_3211')
call_5727 = func_3210_call()
call_5728 = func_3210_call()
output = call_5727
output2 = call_5728
func_5733 = relay.Function([], output)
mod['func_5733'] = func_5733
mod = relay.transform.InferType()(mod)
mutated_mod['func_5733'] = func_5733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5733_call = mutated_mod.get_global_var('func_5733')
call_5734 = func_5733_call()
output = call_5734
func_5735 = relay.Function([], output)
mutated_mod['func_5735'] = func_5735
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4846_call = mod.get_global_var('func_4846')
func_4847_call = mutated_mod.get_global_var('func_4847')
call_5743 = func_4846_call()
call_5744 = func_4846_call()
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_5749 = relay.TupleGetItem(func_2089_call(), 0)
call_5750 = relay.TupleGetItem(func_2091_call(), 0)
output = relay.Tuple([call_5743,call_5749,])
output2 = relay.Tuple([call_5744,call_5750,])
func_5785 = relay.Function([], output)
mod['func_5785'] = func_5785
mod = relay.transform.InferType()(mod)
output = func_5785()
func_5786 = relay.Function([], output)
mutated_mod['func_5786'] = func_5786
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4464_call = mod.get_global_var('func_4464')
func_4466_call = mutated_mod.get_global_var('func_4466')
call_5787 = func_4464_call()
call_5788 = func_4464_call()
output = relay.Tuple([call_5787,])
output2 = relay.Tuple([call_5788,])
func_5801 = relay.Function([], output)
mod['func_5801'] = func_5801
mod = relay.transform.InferType()(mod)
output = func_5801()
func_5802 = relay.Function([], output)
mutated_mod['func_5802'] = func_5802
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3255_call = mod.get_global_var('func_3255')
func_3256_call = mutated_mod.get_global_var('func_3256')
call_5839 = relay.TupleGetItem(func_3255_call(), 0)
call_5840 = relay.TupleGetItem(func_3256_call(), 0)
output = relay.Tuple([call_5839,])
output2 = relay.Tuple([call_5840,])
func_5841 = relay.Function([], output)
mod['func_5841'] = func_5841
mod = relay.transform.InferType()(mod)
mutated_mod['func_5841'] = func_5841
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mutated_mod.get_global_var('func_5841')
call_5842 = func_5841_call()
output = call_5842
func_5843 = relay.Function([], output)
mutated_mod['func_5843'] = func_5843
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4933_call = mod.get_global_var('func_4933')
func_4934_call = mutated_mod.get_global_var('func_4934')
call_5873 = relay.TupleGetItem(func_4933_call(), 0)
call_5874 = relay.TupleGetItem(func_4934_call(), 0)
func_5121_call = mod.get_global_var('func_5121')
func_5126_call = mutated_mod.get_global_var('func_5126')
const_5879 = relay.const([-0.918294,1.265697,-5.670046,3.692488,6.354382,2.863602,-0.864516,-1.735094,-7.567438,2.934593,-8.266247,5.854948,-1.256264,3.464721,-4.880415,-6.975753,9.753464,5.827324,0.500080,4.944918,9.178472,8.083843,-0.819146,9.382718,-8.436146,-8.418250,-5.096504,-4.155456,-4.310422,0.914529,-1.771245,-5.178869,9.521743,6.475908,-3.156804,8.486287,-6.671309,-6.405173,-5.887496,6.775862,-1.786378,6.101803,3.163771,4.387031,6.763618,-8.420133,-4.107574,1.045903,9.428112,1.773497,-7.746865,1.145585,1.523634,2.719458,7.410876,-7.996804,8.873136,7.178294,8.105582,-3.914510,1.560819,3.098187,1.197925,1.885629,8.479705,7.408307,8.950782,-7.000713,-2.972828,-8.353136,-2.181706,2.675091,-2.513803,-2.193588,4.105321,8.688849,-3.679229,5.704804,9.313788,-7.435313,2.951427,-0.008730,-0.785464,8.621725,4.934301,2.022708,-3.329528,7.544463,5.677256,1.174726,-0.736406,3.786281,5.246513,9.678884,0.751026,6.942273,8.690423,1.801692,2.031114,-1.687968,-4.248052,-1.196958,-3.394228,6.403495,-0.610941,-7.781576,0.874994,4.290584,-0.854332,-9.482726,-8.042586,-1.680483], dtype = "float32")#candidate|5879|(112,)|const|float32
const_5880 = relay.const([-4.682086,7.718376,8.980307,-1.645026,5.467408,2.326085,-6.215574,1.187162,4.163273,-1.496420,3.091701,3.974897,-9.880866,0.633499,1.854301,-3.323952,-8.990490,-8.308916,-4.291963,0.184487,3.964533,1.784739,-1.813449,4.476973,8.173215,-1.513989,-2.379298,-8.742539,2.259150,4.267082,-9.941449,3.824862,3.193375,1.396861,-2.322151,-4.120478,3.641320,7.109028,-2.352721,-7.276357,-6.024695,-4.303722,-8.183774,2.048561,-5.788108,2.603171,5.965523,4.016180,-5.822701,-5.211134,2.869369,-9.410686,-4.195216,-3.126455,2.737667,-3.281422,3.472613,-0.229993,6.294138,-3.394835,-3.618757,-2.088634,-4.703778,1.182234,-7.962827,7.432886,-8.903609,7.598126,1.129296,2.469548,-8.879604,-1.873375,-0.077779,3.123424,-8.143547,8.429016,6.152053,-3.262004,8.748764,3.905910,0.580584,5.960861,-1.377459,-2.162295,-7.182011,-0.466691,2.801421,4.924906,-6.073268,0.946634,-5.490849,9.928090,1.050330,0.109164,9.417209,-6.650744,5.843912,-0.777009,-5.102605,9.833480,-8.140637,5.975611,-6.580373,9.935702,-0.120414,2.893310,4.986336,-6.181001,2.983235,3.026540,-1.305841,7.651493,9.111867,-5.320149,3.965875,2.938109,5.386977,9.665278,3.058605,-6.669941,-7.289933,-1.743960,5.958983,-0.712546,-1.388004,4.247254,0.186071,-2.268846,6.547423,2.931760], dtype = "float64")#candidate|5880|(130,)|const|float64
var_5881 = relay.var("var_5881", dtype = "float32", shape = (144,))#candidate|5881|(144,)|var|float32
call_5878 = relay.TupleGetItem(func_5121_call(relay.reshape(const_5879.astype('float32'), [112,]), relay.reshape(const_5880.astype('float64'), [1, 130]), relay.reshape(var_5881.astype('float32'), [144,]), ), 6)
call_5882 = relay.TupleGetItem(func_5126_call(relay.reshape(const_5879.astype('float32'), [112,]), relay.reshape(const_5880.astype('float64'), [1, 130]), relay.reshape(var_5881.astype('float32'), [144,]), ), 6)
uop_5886 = relay.rsqrt(call_5878.astype('float32')) # shape=(98, 4)
uop_5888 = relay.rsqrt(call_5882.astype('float32')) # shape=(98, 4)
func_1986_call = mod.get_global_var('func_1986')
func_1988_call = mutated_mod.get_global_var('func_1988')
call_5899 = relay.TupleGetItem(func_1986_call(), 1)
call_5900 = relay.TupleGetItem(func_1988_call(), 1)
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
var_5907 = relay.var("var_5907", dtype = "float32", shape = (77, 6))#candidate|5907|(77, 6)|var|float32
call_5906 = relay.TupleGetItem(func_3139_call(relay.reshape(var_5907.astype('float32'), [3, 14, 11])), 0)
call_5908 = relay.TupleGetItem(func_3142_call(relay.reshape(var_5907.astype('float32'), [3, 14, 11])), 0)
var_5919 = relay.var("var_5919", dtype = "float32", shape = (98, 4))#candidate|5919|(98, 4)|var|float32
bop_5920 = relay.floor_mod(uop_5886.astype('float64'), relay.reshape(var_5919.astype('float64'), relay.shape_of(uop_5886))) # shape=(98, 4)
bop_5923 = relay.floor_mod(uop_5888.astype('float64'), relay.reshape(var_5919.astype('float64'), relay.shape_of(uop_5888))) # shape=(98, 4)
func_1931_call = mod.get_global_var('func_1931')
func_1934_call = mutated_mod.get_global_var('func_1934')
const_5925 = relay.const([8,-10,-8,-4,-2,-10,9,-1,-4,5,-8,-8,-10,-8,1,-4,1,-7,-5,-10,6,-7,3,-5,-2,9,-7,-5,-7,2,8,6,-2,-10,3,-5,8,-6,-10,2,-3,-4,-7,9,-1,1,-7,-9,-1,7,7,-3,-1,-7,-1,-5,-7,9,5,7,7,5,6,-4,-3,1,2,-6,-4,-6,-2,-1,9,5,8,-1,-2,10,10,-5,8,6,9,-4,5,-9,-10,-5,2,2,2,4,10,1,1,-7,-3,8,-5,6,2,-6,-8,3,3,-10,1,-10,-10,-2,-9,10,2,-6,8,-8,7,-5,6,-7,-3,7,-2,4,-8,-5,-5,-8,2,-5,-6,-3,6,-10,-5,-5,-5,-4,-7,-9,5,1,8,9,3,-10,-7,-2,10,7,-2,-6,3,3,8,-7,5,-5,5,-3,-9,7,-6,9,2,1,-8,-10,7,-3,7,-8,-7,-7,8,-1,3,-1,7,-6,7,5,-6,-6,-10,10,10,10,-2,10,-7,6,-10,-2,8,8,-7,1,-1,6,8,9,-5,-7,-5,6,-9,5,-1,6,5,5,8,5,2,1,9,-10,-8,-9,6,-9,10,-4,-1,8,-4,-7,-8,-4,-4,-10,4,7,-9,-8,-4,9,1,2], dtype = "int64")#candidate|5925|(240,)|const|int64
call_5924 = relay.TupleGetItem(func_1931_call(relay.reshape(const_5925.astype('int64'), [6, 8, 5])), 0)
call_5926 = relay.TupleGetItem(func_1934_call(relay.reshape(const_5925.astype('int64'), [6, 8, 5])), 0)
func_5121_call = mod.get_global_var('func_5121')
func_5126_call = mutated_mod.get_global_var('func_5126')
call_5956 = relay.TupleGetItem(func_5121_call(relay.reshape(const_5879.astype('float32'), [112,]), relay.reshape(const_5880.astype('float64'), [1, 130]), relay.reshape(var_5881.astype('float32'), [144,]), ), 5)
call_5957 = relay.TupleGetItem(func_5126_call(relay.reshape(const_5879.astype('float32'), [112,]), relay.reshape(const_5880.astype('float64'), [1, 130]), relay.reshape(var_5881.astype('float32'), [144,]), ), 5)
uop_5961 = relay.sqrt(uop_5886.astype('float32')) # shape=(98, 4)
uop_5963 = relay.sqrt(uop_5888.astype('float32')) # shape=(98, 4)
var_5967 = relay.var("var_5967", dtype = "float32", shape = (98, 4))#candidate|5967|(98, 4)|var|float32
bop_5968 = relay.equal(uop_5886.astype('bool'), relay.reshape(var_5967.astype('bool'), relay.shape_of(uop_5886))) # shape=(98, 4)
bop_5971 = relay.equal(uop_5888.astype('bool'), relay.reshape(var_5967.astype('bool'), relay.shape_of(uop_5888))) # shape=(98, 4)
output = relay.Tuple([call_5873,const_5879,const_5880,var_5881,call_5899,call_5906,var_5907,bop_5920,call_5924,const_5925,call_5956,uop_5961,bop_5968,])
output2 = relay.Tuple([call_5874,const_5879,const_5880,var_5881,call_5900,call_5908,var_5907,bop_5923,call_5926,const_5925,call_5957,uop_5963,bop_5971,])
func_5973 = relay.Function([var_5881,var_5907,var_5919,var_5967,], output)
mod['func_5973'] = func_5973
mod = relay.transform.InferType()(mod)
var_5974 = relay.var("var_5974", dtype = "float32", shape = (144,))#candidate|5974|(144,)|var|float32
var_5975 = relay.var("var_5975", dtype = "float32", shape = (77, 6))#candidate|5975|(77, 6)|var|float32
var_5976 = relay.var("var_5976", dtype = "float32", shape = (98, 4))#candidate|5976|(98, 4)|var|float32
var_5977 = relay.var("var_5977", dtype = "float32", shape = (98, 4))#candidate|5977|(98, 4)|var|float32
output = func_5973(var_5974,var_5975,var_5976,var_5977,)
func_5978 = relay.Function([var_5974,var_5975,var_5976,var_5977,], output)
mutated_mod['func_5978'] = func_5978
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5841_call = mod.get_global_var('func_5841')
func_5843_call = mutated_mod.get_global_var('func_5843')
call_6008 = relay.TupleGetItem(func_5841_call(), 0)
call_6009 = relay.TupleGetItem(func_5843_call(), 0)
func_4331_call = mod.get_global_var('func_4331')
func_4332_call = mutated_mod.get_global_var('func_4332')
call_6025 = func_4331_call()
call_6026 = func_4331_call()
func_5182_call = mod.get_global_var('func_5182')
func_5184_call = mutated_mod.get_global_var('func_5184')
call_6065 = relay.TupleGetItem(func_5182_call(), 0)
call_6066 = relay.TupleGetItem(func_5184_call(), 0)
output = relay.Tuple([call_6008,call_6025,call_6065,])
output2 = relay.Tuple([call_6009,call_6026,call_6066,])
func_6071 = relay.Function([], output)
mod['func_6071'] = func_6071
mod = relay.transform.InferType()(mod)
mutated_mod['func_6071'] = func_6071
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6071_call = mutated_mod.get_global_var('func_6071')
call_6072 = func_6071_call()
output = call_6072
func_6073 = relay.Function([], output)
mutated_mod['func_6073'] = func_6073
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4554_call = mod.get_global_var('func_4554')
func_4555_call = mutated_mod.get_global_var('func_4555')
call_6097 = func_4554_call()
call_6098 = func_4554_call()
output = relay.Tuple([call_6097,])
output2 = relay.Tuple([call_6098,])
func_6099 = relay.Function([], output)
mod['func_6099'] = func_6099
mod = relay.transform.InferType()(mod)
mutated_mod['func_6099'] = func_6099
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6099_call = mutated_mod.get_global_var('func_6099')
call_6100 = func_6099_call()
output = call_6100
func_6101 = relay.Function([], output)
mutated_mod['func_6101'] = func_6101
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6113 = relay.var("var_6113", dtype = "bool", shape = (9, 11, 8))#candidate|6113|(9, 11, 8)|var|bool
var_6114 = relay.var("var_6114", dtype = "bool", shape = (9, 11, 8))#candidate|6114|(9, 11, 8)|var|bool
bop_6115 = relay.logical_or(var_6113.astype('bool'), relay.reshape(var_6114.astype('bool'), relay.shape_of(var_6113))) # shape=(9, 11, 8)
output = relay.Tuple([bop_6115,])
output2 = relay.Tuple([bop_6115,])
func_6118 = relay.Function([var_6113,var_6114,], output)
mod['func_6118'] = func_6118
mod = relay.transform.InferType()(mod)
mutated_mod['func_6118'] = func_6118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6118_call = mutated_mod.get_global_var('func_6118')
var_6120 = relay.var("var_6120", dtype = "bool", shape = (9, 11, 8))#candidate|6120|(9, 11, 8)|var|bool
var_6121 = relay.var("var_6121", dtype = "bool", shape = (9, 11, 8))#candidate|6121|(9, 11, 8)|var|bool
call_6119 = func_6118_call(var_6120,var_6121,)
output = call_6119
func_6122 = relay.Function([var_6120,var_6121,], output)
mutated_mod['func_6122'] = func_6122
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5733_call = mod.get_global_var('func_5733')
func_5735_call = mutated_mod.get_global_var('func_5735')
call_6350 = func_5733_call()
call_6351 = func_5733_call()
func_2242_call = mod.get_global_var('func_2242')
func_2245_call = mutated_mod.get_global_var('func_2245')
const_6355 = relay.const([2.264648,1.396508,5.331095,2.353343,-8.634690,3.918724,-1.847305,3.876573,-5.054143,3.043695,2.310422,-4.862161,5.932237,2.933324,-2.161363,-8.453569,1.197098,5.576949,-4.301873,0.857847,8.674392,7.423384,1.075252,-2.833316,-7.560693,6.517211,3.433696,3.800790,5.127527,1.137732,2.763638,4.157704,4.589803,9.018749,0.772613,5.326248,0.464390,1.390628,7.392540,8.902305,2.810939,8.395624,-7.518140,6.969740,-3.736861,-6.976213,-9.245651,-8.613683,-9.909990,8.319062,4.401006,-2.494752,0.586812,9.358758,1.797811,-2.624563,1.241097,5.644068,-9.714680,-8.806939,0.822800,-2.664064,-0.019205,7.044582,8.051298,6.222812,4.286179,9.362005,1.544095,8.595869,9.346510,0.921822,-8.006172,8.945887,0.702349,4.447601,-4.583535,2.511216,-8.583493,6.070007,0.611213,-2.079813,-2.355783,-2.036962,0.521797,-6.970430,7.822381,1.978711,-9.954675,7.378939,-4.483091,-6.570759,-2.074009,-5.072355,-7.068422,-4.351914,-1.907836,3.135186,3.126589,-7.261711,6.191500,2.064974,-4.385700,-1.842424,7.609079,-4.470257,-0.495048,-1.110127,-5.917110,-9.735488,-4.026504,9.873346,4.334048,6.204538,-0.464431,9.096612,-1.294763,-4.002438,-6.612227,6.603477,-6.498140,8.107648,-3.346485,-3.734709,-1.695430,-1.259621,1.907197,0.429196,-7.445114,6.176948,-1.997256,-7.889892,-2.632533,8.946860,-6.613156,-5.639716,7.514854,3.441675,-3.608110,-3.723699,-6.966210,5.090236,-9.208102,3.430466,-2.433668,6.224447,5.196668,1.240153,7.334953,-4.758367,-5.309658,-5.961652,0.106372,5.297193,1.368292,-0.348813,-6.878327,-3.288250,6.346004,9.468162,-9.972610,-8.334483,9.586275,8.457257,8.918082,-0.952541,5.307532,9.926945,-3.890450,-9.750752,-9.785199,-5.987221,-6.860276,-9.994217,-3.137384,5.670480,-8.535313,-9.778853,-8.311141,-6.586874,-2.785292,0.486252,-7.551809,-2.749103,8.048769,-9.355469,7.737798,1.188426,0.072212,6.150501,4.697005,0.868622,8.947123,4.729868,1.571661,5.627970,-5.706905,1.144825,9.421689,-9.351660,-1.762996,-3.381464,1.694737,-7.697103,7.612495,-0.942627,-6.410738,4.128351,9.116089,5.283243,-2.435438,-3.356319,8.657081,7.329985,4.380778,-6.691196,9.526170,-3.750149,-9.928646,3.665423,-7.940093,-6.915122,5.338577,-5.157965,1.086905,-0.212896,-7.693772,-1.950908,-2.722969,-3.809015,9.876156,-7.205969,-7.081850,2.665699,1.620328,-5.647240,-6.945945,-1.516502,-4.128778,6.866609,6.865124,-2.555567,-0.954859,5.560861,-3.380526,1.431698,-7.140843,-1.222098,-9.648691,5.786462,3.749278,9.414533,0.558372,8.753256,5.161374,3.972944,-3.734517,-8.444487,-6.238219,-2.849670,-7.709122,7.088230,7.145155,1.026681,5.289807,5.478519,-7.424830,0.269170,-2.617622,-1.771895,3.290549,-1.673122,2.501991,-1.719118,4.211974,-5.154435,-6.746135,-4.560578,-7.521263,7.649469,9.503028,-4.430994,-3.062074,9.951350,-5.332843,-0.859178,5.464342,-6.477758,0.284467,-9.586742,8.801627,-3.279272,-5.163442,2.869885,-6.583409,9.769066,3.975119,-6.384873,5.897469,-1.112847,7.841760,9.116276,-4.206355,9.740824,-2.568568,-4.151738,-6.149764,-5.725351,0.413799,4.201878,-2.645783,2.484022,-7.599629,4.570495,3.781101,-1.761748,-0.688214,9.460997,1.214668,8.031252,5.091875,7.412310,-1.053784,-8.350469,5.657831,-2.780746,-2.635352,3.821230,7.483181,-4.711212,-0.804236,9.662529,-9.466490,4.738169,7.881349,-3.183915,-2.484627,-2.552876,6.467094,2.532960,2.611884,-3.644806,9.462053,-0.901827,3.629539,-6.905527,2.686220,-7.004406,-3.847303,9.681262,-7.682584,-5.966697,2.876625,-5.208680,-8.720811,4.906519,4.152643,3.219289,3.127488,3.076207,0.453850,0.506805,8.074110,-5.659487,4.749082,6.294128,5.486762,5.983624,-2.337932,7.726856,1.499507,-2.884119,5.756999,9.957573,-4.075926,3.950639,-5.202459,-2.086616,-7.372504,-0.386880,5.175032,-9.464619,9.250704,6.473516,8.650620,-6.009987,-5.223381,9.307452,2.787746,-1.743119,5.383819,2.521505,-2.127034,6.606583,-9.971675,0.146765,7.626726,3.003074,8.348891,-7.892024,1.889614,1.422334,-0.178060,3.997370,4.096780,0.551180,2.989822,9.808795,-9.702748,9.666508,-5.236149,-0.747841,-6.399428,-5.916490,3.995670,-8.362850,-6.921750,-4.850233,-5.946407,-0.777790,8.526978,-0.124784,-3.985280,4.160739,-8.991286,7.377781,8.353486,-4.425946,3.038266,3.873842,0.012920,-8.132816,1.446701,-2.139711,-6.146249,9.441378,-2.505552,9.067792,4.731053,-0.538544,0.048700,-3.516863,1.487651,-2.023157,-1.035801,2.433975,3.775401,7.771281,-3.353864,-2.452532,-6.866265,3.820768,0.436672,5.574595,0.382692,-7.111182,1.173472,2.912450,0.150814,-3.999353,5.472040,7.403926,9.717472,7.815192,1.287880,-8.618797,8.993848,-2.442031,-4.033181,-5.716779,3.249354,-9.956160,5.196246,-1.561774,4.816499,-8.963810,-7.358397,1.905683,-7.825961,-1.807345,-7.975559,7.512125,-9.108798,-8.906990,7.775763,-1.285364,4.371309,-1.551280,-5.742543,8.572565,8.261497,-0.169975,-9.437256,7.720505,-0.500226,-5.236459,-7.352565,-0.481023,8.183487,-5.440904,5.535367,-3.111570,3.338127,-3.022233,6.538317,-2.460691,5.431674,-1.327678,-0.054408,2.454554,0.506530,-1.917691,2.069113,-4.219990,4.262990,-1.877595,4.483779,-7.418897,8.823407,-4.518040,-3.850080,1.529856,4.822130,7.621516,3.942475,-0.237789,-3.545990,-5.518969,-9.585993,1.993187,1.305189,-5.809176,-8.486205,-2.978277,2.225953,-0.403457,3.708713,-1.344613,8.106156,-4.324093,-4.606018,-9.742786,5.648281,-6.836370,1.529039,-4.160276,5.297893,-5.167914,3.441184,7.563016,5.643043,-8.478250,7.880023,-3.232150,5.967131,7.085387,7.700945,-0.183634,8.048135,-5.019145,-9.086753,5.172798,-1.268909,5.443789,-7.013113,-7.582370,-3.397371,-2.532303,8.117106,0.355466,-1.426779,-8.580263,-8.385366,-0.718132,-1.229253,-4.083544,8.681344,-8.458273,6.394957,1.192014,9.017463,-9.957217,1.901809,1.894478,4.321445,2.795985,-3.322688,6.428219,-2.700769,-4.164068,2.835387,-1.708011,-6.431199,-6.837111,-5.229286,-7.421585,4.016119,-2.163865,9.426545,-7.890891,-9.557282,-3.939051,7.622957,7.741817,-8.594647,-2.113913,-2.313707,-7.166072,-7.137806,5.229050,8.172945,-5.192357,-1.811005,6.439125,-1.859950,-8.170829,8.771234,7.994637,-1.690502,-6.864834,-1.049125,-0.031583,9.064442,-4.112145,9.405164,0.610489,5.306660,-9.973403,-2.866907,3.512566,2.401658,3.566106,4.795492,8.799585,9.104510,-9.383552,9.304656,-2.253289,2.881398,-6.974895,-0.906602,9.488191,8.473329,9.157276,4.448960,-4.623222,-9.327186,7.013524,9.367151,-1.060124,7.433512,-0.407498,0.362193,3.454968,9.136618,-6.183361,3.082502,8.089773,7.921242,-7.765003,-7.430847,8.945057,-9.273551,-5.901667,2.111752,-5.487965,5.848204,7.882377,-7.888985,9.349139,-7.422592,4.892417,-5.954923,-9.764896,-3.610456,-4.196148,-2.298303,6.467466,3.688863,-7.592027,-2.973789,6.230237,3.115714,0.459178,3.793276,-9.907428,-5.628927,-1.052392,-0.879739,-5.375920,7.584341,6.578179,-3.030906,4.015593,-3.274222,-6.021657,-2.919485,-6.355473,5.745216,6.357247,6.693042,-3.542206,-3.778496,-9.997930,-6.479787,3.655834,2.899729,4.880090,3.277440,9.608569,-2.791422,0.114729,0.382289,-9.250785,3.109500,-1.184357,6.384895,-2.219784,2.906483,8.003305,7.676318,9.316012,0.810844,-3.360460,2.991575,3.736241,4.663788,5.979606,-9.311340,3.628000,8.463516,-0.725594,7.590023,-3.053667,3.569409,-5.661632,-7.013377,-0.813190,-5.272592,7.280063,-6.118571,9.688060,0.792642,3.362996,-3.610136,9.605894,-2.278598,0.464062,-5.420082,-8.665098,2.701196,-0.308747,-4.043593,5.501777,3.233261,6.740560,4.863164,0.510527,4.169180,9.880036,-7.125440,8.452089,-9.044854,-5.318301,9.333230,5.856622,1.022499,-7.171375,-0.206344,-3.449382,-5.647118,4.299896,-1.969828,-3.273804,5.859942,3.847360,-9.312146,-9.163584,9.246974,1.337139,6.877031,4.702407,-5.118694,4.538774,-3.950157,-4.995650,2.703309,-2.540411,6.632172,6.974087,-0.643304,-3.708720,8.109300,-1.867046,6.367097,8.701484,-9.657167,7.954916,4.391613,0.620421,-9.031984,-5.975000,3.074112,1.640455,-5.995806,-2.484522,5.921462,7.312498,4.102890,-3.030709,-1.702265,-0.135084,-4.322085,2.654417,-6.168425,7.720099,3.012895,-3.849989,3.251254,8.477136,-8.572286,-4.465109,-7.105088,-2.311234,2.602157,-1.187638,2.352898,-0.593409,-9.554748,1.763224,-7.846694,2.985312,-9.182463,3.640837,5.467355,9.634987,-3.066595,5.206756,-0.674681,-4.821989,-6.609152,0.084078,8.959009,-3.046575,8.640480,-3.717318,-3.967862,1.378628,1.233393,-8.656909,0.149554,-3.206024,-9.799340,-1.192613,-8.413809,-7.208048,2.384096,-1.487860,-9.128584,-1.089176,-9.108262,3.914341,-1.070283,6.593044,4.438900,-5.110205,-0.986927,-0.144547,0.364037,9.953758,-9.806274,-8.189364,8.151934,-2.945945,6.310690,0.249079,-6.581318,7.825646,-2.124119,-5.831636,-8.244626,-5.034534,-6.074610,1.115776,-2.115487,4.521082,5.973748,-7.328604,-6.978065,-5.056983,-5.563712,3.742761,-7.331803,2.910876,8.583540,0.613377,7.461191,-3.705889,-7.206317,0.910942,-7.621920,6.692026,-5.982240,-7.640382,8.562681,9.388227,9.444305,-8.004259,3.411636,-1.041659,0.319099,-5.363389,3.885584,-2.577852,1.347367,-2.979082,-9.773381,8.116976,-3.764933,9.404295,-5.154182,1.263077,9.529627,3.360870,3.815519,-9.730776,2.086321,1.475728,6.157331,8.642013,0.790677,5.584453,1.793293,8.096520,-1.403482,2.152429,6.358507,-4.504882,-5.367281,2.329589,3.013692,9.182380,-5.382967,-4.059784,-4.780750,-9.921392,3.901471,-3.064468,-6.145488,-5.652671,-4.383966,0.654678,-7.325855,6.489992,-2.368500,8.038225,-9.873860,-5.078766,7.334391,-7.741092,-9.300027,-8.821529,-9.476810,2.919115,-6.924422,-0.634557,3.905886,-8.181837,8.194366,9.791374,-2.710032,-2.255417,0.491478,8.099235,2.087632,-9.805630,6.205245,3.440343,7.066744,-2.934405,6.590334,9.012888,5.119178,-1.157074,6.381151,-6.166679,-7.238512,-6.386392,8.176777,0.240833,2.123007,9.491763,-9.199206,6.701396,0.273203,4.663094,-9.392819,6.454327,-3.379753,-9.863291,0.750468,7.759311,0.787053,5.180068,4.255168,3.220951,9.369387,1.824599,-7.102835,1.570794,7.760538,-1.587265,4.493446,1.338415,2.702619,5.759515,-9.064650,6.863697,-5.247648,-9.164359,0.626538,1.717424,-8.481605,-4.124012,3.392085,-2.314268,-1.603736,-6.535216,5.180710,3.421164,5.289810,1.989676,5.465282,-1.771689,-5.151682,9.476954,-7.223857,-4.798914,-9.393007,9.307911,-5.814447,-2.133613,-3.236238,4.811798,-5.272688,7.968494,5.481169,3.538366,0.414351,2.840072,-3.930019,0.899674,5.544228,-3.080345,-9.022964,6.345085,9.631178,8.457154,-5.612676,2.312719,1.520982,-1.781508,-4.491737,8.877007,1.352572,1.186322,9.537408,5.451076,-1.645076,-6.456075,9.887511,8.686316,7.853810,4.060641,6.328560,-2.749840,7.942926,-7.613655,-2.584413,1.060473,-1.521532,-2.424355,8.619478,-9.439514,6.229430,-9.878505,-8.242580,8.193883,-9.308745,2.846383,-3.123429,-5.811121,-4.859764,9.593541,-8.509512,7.484578,1.090542,-8.403042,7.476952,-9.217665,-3.439238,9.479073,-4.115198,-4.335378,4.813774,7.847079,-8.129779,4.349454,-6.781223,4.807029,7.893138,5.122961,-3.819190,4.534993,-9.195790,-7.496526,-9.951321,4.919313,5.485705,8.989732,8.040708,-0.706344,-6.738931,-6.599506,-8.712951,2.019051,-0.328852,-7.291539,1.934632,-7.506712,1.121380,-6.719208,4.118320,-4.106784,0.400975,4.915039,-5.123248,-8.547320,-2.275898,4.796268,0.847205,-6.166049,2.613932,-5.865575,9.053425,-7.158336,-2.909445,-6.420017,-2.640389,-3.522662,1.632790,-7.749423,5.500200,-2.785290,-6.485538,-2.369127,4.377052,0.460712,4.584314,1.345196,1.901308,0.290642,-9.407831,1.999756,-4.043976,-1.353918,0.233484,-4.686062,-8.805008,-7.689422,-4.487800,-6.536083,-1.450835,8.247559,6.478499,-9.291637,-4.591269,-9.804350,0.915071,-4.748547,1.227770,9.113231,0.008533,9.235422,8.316608,-8.517454,-1.131102,1.071532,4.129973,-6.400456,8.822783,8.173090,-9.073032,-4.484047,2.912263,-5.235720,5.652732,7.699388,5.562431,-8.805235,3.564325,-6.231116,1.048413,-7.678511,-7.128835,-8.604847,7.250933,-8.179771,9.836178,5.187779,1.983474,-6.567657,-2.774334,1.928500,-4.011493,-6.768908,3.688080,-9.646130,-7.858734,5.521816,2.591118,-0.980636,2.947780,0.697983,4.532393,0.576629,-0.298403,3.541564,1.299571,-1.544701,3.192060,0.137392,8.525068,9.166797,-4.506494,8.723322,-2.078126,-1.932966,-5.993023,9.954200,9.323931,-2.204456,-7.533502,-0.226948,-5.931302,3.614426,7.736572,-9.788584,-6.155219,-8.766429,-0.211843,9.868224,8.777896,-9.509630,0.467575,9.898947,-6.280043,-1.562968,9.985577,7.405555,4.200965,2.441464,1.252624,5.323405,-0.723114,1.578667,7.645920,5.141764,-6.904495,-0.928267,5.078518,-1.950776,4.238250,-6.682593,1.829964,3.789005,9.398962,1.509074,-4.619810,-3.545982,-7.570981,-9.791534,-7.097043,-1.870167,3.940917,-3.068162,-5.038138,1.624752,0.441899,0.195931,0.729967,5.163778,6.855069,6.290042,-3.621857,-7.687626,6.465607,-9.687610,1.657732,9.253271,-2.292318,7.250044,-7.773833,-4.941903,1.241270,1.692884,-3.305306,2.110102,5.331267,-8.596461,-4.616003,7.693326,8.538585,-7.761653,-9.958495,4.796683,5.462578,-0.360295,6.417965,-7.222687,-7.728428,9.928730,-0.210329,-3.969577,-5.662048,5.816796,-2.527568,-2.064540,1.203046,-9.057939,-3.128342,-3.169339,-6.798111,-2.559806,7.829792,-1.704580,-5.621162,8.467304,-0.789165,-9.184589,-8.479233,-9.200950,-5.747414,-9.359070,6.735831,-9.899399,-5.408117,2.320307,4.648955,4.418577,-5.539664,-5.252900,2.191881,-8.439180,8.214571,-5.417461,-7.135812,-1.701228,-8.386033,-6.833283,5.251916,7.562818,3.050852,5.912081,-0.881755,-5.919638,-4.862569,7.566340,-1.388270,-0.437092,8.102401,8.128797,8.485531,-5.902083,-4.865476,5.827161,1.037261,6.755602,8.758749,3.143268,7.646395,4.828594,-4.213469,-0.675025,-0.535580,9.293407,5.721174,2.849392,-8.903273,-0.821505,1.093630,4.668418,6.205722,4.842603,5.496184,-9.014462,-5.382612,-1.880158,6.813098,3.066062,1.387356,1.533295,4.509574,7.840643,-5.231754,-1.808540,0.822618,8.260864,9.271827,-7.913888,0.250490,3.915846,-9.893796,4.078442,-0.089199,3.478080,2.874039,6.532844,8.264228,-9.279455,-8.989535,6.736412,-7.450507,-4.686366,-3.059456,-5.979276,-0.390256,3.180353,-7.076650,-8.078028,-7.089700,-6.636225,-8.583159,-1.212926,0.535543,1.696021,-4.772802,0.911762,2.244840,-8.114508,-7.557507,-5.613532,-7.645015,4.988830,-1.404721,-0.628754,5.060025,-4.797706,-9.096829,-3.711649,8.465653,5.625760,-6.874087,4.392086,9.093078,8.325312,-7.929660,-7.732385,-8.043783,8.846395,7.246429,4.541570,1.158320,-7.514014,-1.672762,9.528823,-4.832376,4.280447,0.398127,7.524339,-5.534675,2.684706,-5.525332,-7.217836,5.881393,2.979905,2.902694,-9.298743,-2.095279,-0.594601,0.949126,-3.389199,-4.650995,-6.092537,-7.278102,-9.593648,0.560197,-2.737471,8.912607,-6.099699,-0.500718,4.007940,-8.722118,-3.204015,-8.636957,2.420289,-9.794421,-9.332327,-1.866043,8.915343,-0.943292,7.181794,7.532995,5.748903,-7.094023,8.739885,5.807909,-6.677486,-0.426773,-8.810902,7.993590,-9.559962,7.058914,2.676357,-6.464172,9.939573,-1.867095,-3.703787,-0.593978,9.609600,5.655024,5.852138,1.512010,-8.814894,1.676853,3.517153,-0.998912,-9.211140,-9.721613,3.877578,-3.810625,4.593917,-7.531397,-4.865288,0.557342,6.257477,8.390630,1.661026,2.042747,-8.646456,-5.887960,3.628727,-0.472834,-4.089266,5.352044,4.687491,-7.761707,9.174912,-8.249690,6.622110,0.370244,-8.926970,-3.675521,6.431742,4.270874,-3.482198,6.905480,-3.265162,2.743419,-9.459653,4.534552,8.268231,-1.139923,-8.210765,-9.914956,-3.032404,-9.752205,-2.649625,-9.395713,-3.169647,-0.426760,0.918138,0.400119,9.698659,5.548909,2.685190,3.972443,-2.776271,2.272116,-7.025287,5.247353,7.517799,5.191462,-5.866055,-8.835115,8.070293,7.606245,-6.231181,-6.197968,4.155716,-9.052050,-9.150377,5.387425,7.199654,8.145327,7.261204,1.137916,8.412103,-0.193730,-0.238231,-9.279320,4.164605,7.679629,-9.798322,2.941194,7.430233,9.370176,6.550031,-0.480193,1.185837,-6.574636,-2.991205,-7.743045,-7.375908,5.641021,6.161744,-8.279908,2.012857,-0.602115,-5.629426,-3.818711,6.328816,4.027227,-2.584660,-4.403668,-7.943628,-0.136520,-6.559276,-5.464795,-1.284892,6.085273,9.263963,-9.192929,3.208462,4.804217,5.290999,7.832310,6.771794,5.561711,1.139308,9.305657,2.128039,-8.608686,-8.507727,-8.154203,5.172771,-2.311544,-0.012205,7.868860,-4.977252,6.594978,-5.567177,-6.080094,6.607035,-8.277534,3.510150,-7.610743,9.569391,-5.898719,7.947586,-3.355146,8.039808,-4.430509,-4.881984,6.345191,-3.536006,-5.240287,-0.211490,-2.505092,-3.295017,-2.436317,-1.039969,-1.763436,7.463977,-5.498191,-5.416494,6.128860,1.620959,6.531068,-1.507049,-2.498490,4.885558,3.449546,-5.473322,5.146079,-0.675186,-5.975165,8.684151,9.637907,-2.639994,4.621574,-0.945070,-9.426445,-1.245968,5.696163,-6.801883,9.430736,-4.496000,7.311511,-6.367781,-0.900837,-6.762396,-9.244891,4.763439,6.042176,0.694557,-9.634976,5.925186,5.809876,-0.491961,-7.211861,5.339293,-5.014523,1.657166,-3.642373,2.127136,-9.533468,5.248874,7.016116,-2.233139,-3.030541,0.998410,-7.833141,3.016761,6.340127,-7.965826,4.302320,3.632525,-5.439137,2.654625,0.983401,3.967982,9.172905,-7.536914,6.990352,4.941010,-8.174689,0.298543,9.643394,-2.761364,-9.786199,2.386063,-7.903272,-4.387788,4.491428,4.104245,-6.636100,-2.474092,-1.834219,-4.505166,-5.512834,9.017566,-1.807596,5.839243,-9.308960,-4.626043,-5.281968,-2.385921,5.666696,3.924019,-2.841355,2.394234,8.959702,-7.562630,-6.091134,-2.682516,-2.027314,6.386984,-1.398376,1.093950,-1.099952,3.919019,1.357619,-4.122761,-7.228405,9.931836,-3.686175,9.065957,-7.825162,5.000296,-8.861040,8.533094,-2.148021,-6.390846,9.846233,0.449686,0.543042,6.784211,-9.545562,4.549698,7.617307,5.215968,7.098095,-9.840066,0.334719,-5.395282,4.451957,-9.862458,-3.896039,-0.262896,-5.469394,-2.307254,-2.035666,-8.341758,3.362509,-0.165577,-9.747005,-4.198391,-8.963631,-3.111301,7.073401,-2.571678,-2.966840,-4.658394,6.051309,6.494290,-6.939201,3.210992,4.175052,5.322523,-7.369002,6.733574,9.150025,-4.021765,-2.103035,6.743399,-3.041849,-6.921828,3.774991,7.127274,3.268878,-5.246490,-0.111580,4.327267,-8.701260,-8.698188,-6.363572,2.973180,-8.885277,6.203749,-0.341488,-3.937794,-7.494403,-2.444671,6.291735,-5.345600,-0.941183,-7.367477,0.711232,-6.938021,-1.764796,-9.676619,-2.648584,-3.158491,6.684841,-1.106191,8.527524,-5.042146,9.926224,2.413851,3.657650,-4.918581,-3.888126,-7.872777,-5.268725,2.208782,-9.488298,6.791205,-0.904518,2.182780,6.965960,0.373876,-1.991344,9.005091,-9.611278,-8.615845,-0.369552,1.357170,3.714453,-4.563422,-6.244293,-9.832240,4.140015,-9.746793,7.392450,-5.631616,8.448814,1.843692,3.353696,9.736410], dtype = "float64")#candidate|6355|(1890,)|const|float64
call_6354 = relay.TupleGetItem(func_2242_call(relay.reshape(const_6355.astype('float64'), [1890,]), relay.reshape(call_6350.astype('float64'), [6, 9, 3]), ), 0)
call_6356 = relay.TupleGetItem(func_2245_call(relay.reshape(const_6355.astype('float64'), [1890,]), relay.reshape(call_6350.astype('float64'), [6, 9, 3]), ), 0)
func_6118_call = mod.get_global_var('func_6118')
func_6122_call = mutated_mod.get_global_var('func_6122')
const_6358 = relay.const([False,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,False,False,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,True,True,True,False,True,True,False,False,False,True,True,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,True,False,False,True,True,False,False,False,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,False,True,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,True,True,False,True,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,True,False,False,True,True,False,True,True,False,False,True,True,True,True,False,False,False,True,True,False,False,True,False,False,False,True,False,False,True,True,False,True,True,False,False,True,True,True,False,True,True,True,True,True,True,True,True,True,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,True,False,True,False,True,True,True,False,False,False,False,True,True,True,True,True,True,True,False,False,False,True,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,False,False,True,True,False,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,False,True,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,False,True,True,True,True,False,True,False,True,False,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,False,False,False,False,False,False,True,False,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,False,True,True,False,True,False,True,True,False,True,False,True,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,False,True,False,False,False,True,True,True,True], dtype = "bool")#candidate|6358|(792,)|const|bool
call_6357 = relay.TupleGetItem(func_6118_call(relay.reshape(const_6358.astype('bool'), [9, 11, 8]), relay.reshape(const_6358.astype('bool'), [9, 11, 8]), ), 0)
call_6359 = relay.TupleGetItem(func_6122_call(relay.reshape(const_6358.astype('bool'), [9, 11, 8]), relay.reshape(const_6358.astype('bool'), [9, 11, 8]), ), 0)
output = relay.Tuple([call_6350,call_6354,const_6355,call_6357,const_6358,])
output2 = relay.Tuple([call_6351,call_6356,const_6355,call_6359,const_6358,])
func_6371 = relay.Function([], output)
mod['func_6371'] = func_6371
mod = relay.transform.InferType()(mod)
output = func_6371()
func_6372 = relay.Function([], output)
mutated_mod['func_6372'] = func_6372
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6099_call = mod.get_global_var('func_6099')
func_6101_call = mutated_mod.get_global_var('func_6101')
call_6386 = relay.TupleGetItem(func_6099_call(), 0)
call_6387 = relay.TupleGetItem(func_6101_call(), 0)
func_3801_call = mod.get_global_var('func_3801')
func_3805_call = mutated_mod.get_global_var('func_3805')
const_6406 = relay.const([[9.950315,-2.227401,0.140568,-5.866227,-0.990594,-0.398735,4.142766,-9.209495,-7.001587,7.808160],[9.972902,8.571350,-5.262656,4.951433,-4.847961,2.708957,9.829319,-2.385893,2.363520,-6.256778],[0.714695,4.118528,8.300329,0.128638,8.892914,-3.428038,-5.184060,-7.749345,-4.480358,-9.356268],[-9.842045,-3.803309,1.518633,-5.050832,-4.685942,-2.282794,-8.922343,-5.113706,0.388916,7.952382],[-9.747382,1.850389,6.189350,4.793012,1.222519,-8.487964,5.511811,9.443466,-3.692931,4.201322],[6.181028,-9.177281,2.933457,8.253250,-6.567149,1.455471,-0.265362,-1.856135,4.043793,-6.055789],[2.274186,-5.008376,8.162543,4.453822,0.310262,-1.343667,-0.832129,-4.709587,8.358910,-5.317926],[-7.091485,-9.164767,-8.591232,0.433464,-3.564890,-5.442409,-5.407226,-9.194782,-2.972381,2.922685],[-8.648766,-8.787273,9.906311,2.069927,-0.237154,-1.240715,8.834239,-3.487282,2.801923,3.330094],[8.443721,4.482652,-5.156946,2.242839,3.917540,5.527125,5.083243,-9.889815,-6.705624,9.354574],[8.332229,-3.927025,5.426849,-9.682012,-9.013823,-1.169464,4.161589,0.205569,-2.543008,0.359018],[-6.527785,8.084180,-3.655298,-3.936309,2.081402,-0.939106,2.470390,-0.862224,9.459874,-6.793426],[-4.032549,3.938812,-5.945160,-0.210096,5.140869,4.354807,-0.066104,1.889978,-5.796191,2.638180]], dtype = "float64")#candidate|6406|(13, 10)|const|float64
var_6407 = relay.var("var_6407", dtype = "float32", shape = (21,))#candidate|6407|(21,)|var|float32
var_6408 = relay.var("var_6408", dtype = "float32", shape = (77, 6))#candidate|6408|(77, 6)|var|float32
call_6405 = relay.TupleGetItem(func_3801_call(relay.reshape(const_6406.astype('float64'), [1, 130]), relay.reshape(var_6407.astype('float32'), [21,]), relay.reshape(var_6408.astype('float32'), [462,]), ), 2)
call_6409 = relay.TupleGetItem(func_3805_call(relay.reshape(const_6406.astype('float64'), [1, 130]), relay.reshape(var_6407.astype('float32'), [21,]), relay.reshape(var_6408.astype('float32'), [462,]), ), 2)
output = relay.Tuple([call_6386,call_6405,const_6406,var_6407,var_6408,])
output2 = relay.Tuple([call_6387,call_6409,const_6406,var_6407,var_6408,])
func_6424 = relay.Function([var_6407,var_6408,], output)
mod['func_6424'] = func_6424
mod = relay.transform.InferType()(mod)
var_6425 = relay.var("var_6425", dtype = "float32", shape = (21,))#candidate|6425|(21,)|var|float32
var_6426 = relay.var("var_6426", dtype = "float32", shape = (77, 6))#candidate|6426|(77, 6)|var|float32
output = func_6424(var_6425,var_6426,)
func_6427 = relay.Function([var_6425,var_6426,], output)
mutated_mod['func_6427'] = func_6427
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3192_call = mod.get_global_var('func_3192')
func_3193_call = mutated_mod.get_global_var('func_3193')
call_6434 = relay.TupleGetItem(func_3192_call(), 0)
call_6435 = relay.TupleGetItem(func_3193_call(), 0)
output = call_6434
output2 = call_6435
func_6450 = relay.Function([], output)
mod['func_6450'] = func_6450
mod = relay.transform.InferType()(mod)
output = func_6450()
func_6451 = relay.Function([], output)
mutated_mod['func_6451'] = func_6451
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5587_call = mod.get_global_var('func_5587')
func_5588_call = mutated_mod.get_global_var('func_5588')
call_6480 = relay.TupleGetItem(func_5587_call(), 0)
call_6481 = relay.TupleGetItem(func_5588_call(), 0)
func_5553_call = mod.get_global_var('func_5553')
func_5554_call = mutated_mod.get_global_var('func_5554')
call_6515 = func_5553_call()
call_6516 = func_5553_call()
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_6517 = relay.TupleGetItem(func_2089_call(), 0)
call_6518 = relay.TupleGetItem(func_2091_call(), 0)
output = relay.Tuple([call_6480,call_6515,call_6517,])
output2 = relay.Tuple([call_6481,call_6516,call_6518,])
func_6521 = relay.Function([], output)
mod['func_6521'] = func_6521
mod = relay.transform.InferType()(mod)
output = func_6521()
func_6522 = relay.Function([], output)
mutated_mod['func_6522'] = func_6522
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4907_call = mod.get_global_var('func_4907')
func_4908_call = mutated_mod.get_global_var('func_4908')
call_6577 = func_4907_call()
call_6578 = func_4907_call()
output = call_6577
output2 = call_6578
func_6594 = relay.Function([], output)
mod['func_6594'] = func_6594
mod = relay.transform.InferType()(mod)
output = func_6594()
func_6595 = relay.Function([], output)
mutated_mod['func_6595'] = func_6595
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6521_call = mod.get_global_var('func_6521')
func_6522_call = mutated_mod.get_global_var('func_6522')
call_6658 = relay.TupleGetItem(func_6521_call(), 0)
call_6659 = relay.TupleGetItem(func_6522_call(), 0)
func_2792_call = mod.get_global_var('func_2792')
func_2794_call = mutated_mod.get_global_var('func_2794')
var_6684 = relay.var("var_6684", dtype = "int32", shape = (2912,))#candidate|6684|(2912,)|var|int32
call_6683 = func_2792_call(relay.reshape(var_6684.astype('int32'), [16, 14, 13]))
call_6685 = func_2792_call(relay.reshape(var_6684.astype('int32'), [16, 14, 13]))
bop_6690 = relay.floor_mod(call_6683.astype('float64'), relay.reshape(var_6684.astype('float64'), relay.shape_of(call_6683))) # shape=(16, 14, 13)
bop_6693 = relay.floor_mod(call_6685.astype('float64'), relay.reshape(var_6684.astype('float64'), relay.shape_of(call_6685))) # shape=(16, 14, 13)
func_6118_call = mod.get_global_var('func_6118')
func_6122_call = mutated_mod.get_global_var('func_6122')
var_6709 = relay.var("var_6709", dtype = "bool", shape = (792,))#candidate|6709|(792,)|var|bool
call_6708 = relay.TupleGetItem(func_6118_call(relay.reshape(var_6709.astype('bool'), [9, 11, 8]), relay.reshape(var_6709.astype('bool'), [9, 11, 8]), ), 0)
call_6710 = relay.TupleGetItem(func_6122_call(relay.reshape(var_6709.astype('bool'), [9, 11, 8]), relay.reshape(var_6709.astype('bool'), [9, 11, 8]), ), 0)
output = relay.Tuple([call_6658,bop_6690,call_6708,var_6709,])
output2 = relay.Tuple([call_6659,bop_6693,call_6710,var_6709,])
func_6711 = relay.Function([var_6684,var_6709,], output)
mod['func_6711'] = func_6711
mod = relay.transform.InferType()(mod)
mutated_mod['func_6711'] = func_6711
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6711_call = mutated_mod.get_global_var('func_6711')
var_6713 = relay.var("var_6713", dtype = "int32", shape = (2912,))#candidate|6713|(2912,)|var|int32
var_6714 = relay.var("var_6714", dtype = "bool", shape = (792,))#candidate|6714|(792,)|var|bool
call_6712 = func_6711_call(var_6713,var_6714,)
output = call_6712
func_6715 = relay.Function([var_6713,var_6714,], output)
mutated_mod['func_6715'] = func_6715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3255_call = mod.get_global_var('func_3255')
func_3256_call = mutated_mod.get_global_var('func_3256')
call_6728 = relay.TupleGetItem(func_3255_call(), 0)
call_6729 = relay.TupleGetItem(func_3256_call(), 0)
func_4464_call = mod.get_global_var('func_4464')
func_4466_call = mutated_mod.get_global_var('func_4466')
call_6740 = func_4464_call()
call_6741 = func_4464_call()
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_6742 = relay.TupleGetItem(func_2564_call(), 0)
call_6743 = relay.TupleGetItem(func_2566_call(), 0)
bop_6748 = relay.greater(call_6742.astype('bool'), relay.reshape(call_6728.astype('bool'), relay.shape_of(call_6742))) # shape=(6, 9, 3)
bop_6751 = relay.greater(call_6743.astype('bool'), relay.reshape(call_6729.astype('bool'), relay.shape_of(call_6743))) # shape=(6, 9, 3)
output = relay.Tuple([call_6740,bop_6748,])
output2 = relay.Tuple([call_6741,bop_6751,])
func_6755 = relay.Function([], output)
mod['func_6755'] = func_6755
mod = relay.transform.InferType()(mod)
output = func_6755()
func_6756 = relay.Function([], output)
mutated_mod['func_6756'] = func_6756
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4933_call = mod.get_global_var('func_4933')
func_4934_call = mutated_mod.get_global_var('func_4934')
call_6782 = relay.TupleGetItem(func_4933_call(), 0)
call_6783 = relay.TupleGetItem(func_4934_call(), 0)
func_3068_call = mod.get_global_var('func_3068')
func_3070_call = mutated_mod.get_global_var('func_3070')
call_6802 = relay.TupleGetItem(func_3068_call(), 0)
call_6803 = relay.TupleGetItem(func_3070_call(), 0)
func_560_call = mod.get_global_var('func_560')
func_563_call = mutated_mod.get_global_var('func_563')
var_6806 = relay.var("var_6806", dtype = "float32", shape = (135,))#candidate|6806|(135,)|var|float32
call_6805 = relay.TupleGetItem(func_560_call(relay.reshape(var_6806.astype('float32'), [15, 3, 3])), 0)
call_6807 = relay.TupleGetItem(func_563_call(relay.reshape(var_6806.astype('float32'), [15, 3, 3])), 0)
output = relay.Tuple([call_6782,call_6802,call_6805,var_6806,])
output2 = relay.Tuple([call_6783,call_6803,call_6807,var_6806,])
func_6808 = relay.Function([var_6806,], output)
mod['func_6808'] = func_6808
mod = relay.transform.InferType()(mod)
mutated_mod['func_6808'] = func_6808
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6809 = relay.var("var_6809", dtype = "float32", shape = (135,))#candidate|6809|(135,)|var|float32
func_6808_call = mutated_mod.get_global_var('func_6808')
call_6810 = func_6808_call(var_6809)
output = call_6810
func_6811 = relay.Function([var_6809], output)
mutated_mod['func_6811'] = func_6811
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6822 = relay.var("var_6822", dtype = "float64", shape = (9, 2, 7))#candidate|6822|(9, 2, 7)|var|float64
uop_6823 = relay.acos(var_6822.astype('float64')) # shape=(9, 2, 7)
uop_6839 = relay.rsqrt(uop_6823.astype('float32')) # shape=(9, 2, 7)
func_5298_call = mod.get_global_var('func_5298')
func_5300_call = mutated_mod.get_global_var('func_5300')
const_6848 = relay.const([2.253530,3.409651,-4.804466,8.899186,6.799802,9.777499,0.804352,7.386356,5.681005,-2.477836,4.836622,-2.811219,-3.621625,-7.213428,-8.283677,4.758380,5.498105,4.284297,-5.019919,-3.328065,6.963234,-6.896009,0.012165,6.103281,8.952877,2.282187,-1.410542,-9.175362,9.132654,-3.884543,-0.269477,3.183197,-9.975275,5.617762,-1.080866,-3.596934,-9.287903,-2.174782,9.262352,-2.781479,4.925044,9.012995,-7.467498,-1.105659,3.588190,5.219592,-6.453289,7.010488,8.962143,2.873217,-5.953089,-0.638555,6.852742,-1.458954,-3.917219,2.295254,-9.711263,6.116120,8.122316,-6.869650,-5.442651,-0.003820,7.935683,7.262784,7.323092,-7.430818,9.830000,-5.331606,1.489239,6.227934,6.625803,0.404385,5.784526,-9.756104,-0.135791,8.565634,0.955565,7.217919,-5.705321,2.510315,-8.968261,7.933959,-5.968120,-9.657879,9.452296,-6.967996,-1.095626,-3.525668,-3.347756,-8.237701,-3.080722,-7.823773,-3.954942,-8.737170,-9.373096,-9.540239,2.083031,-2.430439,4.060527,4.571926,-5.587393,9.408684,8.675341,0.069395,8.898579,-3.044739,8.291904,2.915883,-3.323852,-3.698155,1.952406,7.583511,0.957779,5.322953,-9.600307,7.930742,-3.405349,-2.925799,-0.156090,8.392082,1.408247,3.764478,-7.769019,-0.187320,-1.453083,-3.782473,2.364517,-5.080119,1.220554,6.616444,-3.262456,1.916376,-7.180292,-5.306883,0.258733], dtype = "float32")#candidate|6848|(135,)|const|float32
call_6847 = relay.TupleGetItem(func_5298_call(relay.reshape(const_6848.astype('float32'), [135,])), 0)
call_6849 = relay.TupleGetItem(func_5300_call(relay.reshape(const_6848.astype('float32'), [135,])), 0)
const_6855 = relay.const([[[3.191733,4.294029,-0.601643,2.024039,7.915894,4.381097,3.008367],[1.422088,-2.974976,5.551329,4.864895,8.829227,-0.274021,4.199803]],[[9.927602,-9.502792,5.477948,1.208649,2.131184,9.345023,-1.650835],[-4.026310,7.640932,6.275021,8.304769,-1.363546,-1.761839,7.403607]],[[8.023969,-5.856711,6.164945,-1.842149,-6.468402,-2.314085,-8.607452],[-8.563359,-0.364387,-5.015168,9.981895,8.404346,1.648965,7.042663]],[[0.558166,-0.073172,-8.752227,5.011468,3.540336,-6.000635,-4.982987],[8.302354,-2.920523,9.444061,-2.924686,-9.380955,0.788143,3.641902]],[[-6.119175,6.946212,0.694134,-7.045625,-5.472988,1.497054,5.702747],[-9.912153,-8.359674,-0.269628,4.694529,3.614680,-8.955337,5.426903]],[[5.244254,-8.204646,-0.015162,2.753497,5.870800,3.270482,-1.198333],[0.241932,-3.386690,9.201701,2.284014,-6.075392,7.266957,-9.819857]],[[3.808053,-7.382473,-1.682145,-1.305031,-0.872299,-8.880030,-5.819117],[5.058707,-8.777584,-0.137564,-6.367551,1.430414,-7.417244,7.185956]],[[2.539688,5.019962,4.049206,5.625895,-5.693368,-3.597828,-7.897785],[-4.372475,-1.007694,8.806310,-4.049284,-0.333645,2.975747,-7.222184]],[[3.022213,3.423677,8.214802,0.194911,-1.926439,3.743053,3.770822],[3.283235,-2.328639,-0.123772,-4.635768,-7.393078,4.848297,7.126240]]], dtype = "float32")#candidate|6855|(9, 2, 7)|const|float32
bop_6856 = relay.equal(uop_6839.astype('bool'), relay.reshape(const_6855.astype('bool'), relay.shape_of(uop_6839))) # shape=(9, 2, 7)
output = relay.Tuple([call_6847,const_6848,bop_6856,])
output2 = relay.Tuple([call_6849,const_6848,bop_6856,])
func_6868 = relay.Function([var_6822,], output)
mod['func_6868'] = func_6868
mod = relay.transform.InferType()(mod)
var_6869 = relay.var("var_6869", dtype = "float64", shape = (9, 2, 7))#candidate|6869|(9, 2, 7)|var|float64
output = func_6868(var_6869)
func_6870 = relay.Function([var_6869], output)
mutated_mod['func_6870'] = func_6870
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6099_call = mod.get_global_var('func_6099')
func_6101_call = mutated_mod.get_global_var('func_6101')
call_6892 = relay.TupleGetItem(func_6099_call(), 0)
call_6893 = relay.TupleGetItem(func_6101_call(), 0)
output = call_6892
output2 = call_6893
func_6896 = relay.Function([], output)
mod['func_6896'] = func_6896
mod = relay.transform.InferType()(mod)
output = func_6896()
func_6897 = relay.Function([], output)
mutated_mod['func_6897'] = func_6897
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6099_call = mod.get_global_var('func_6099')
func_6101_call = mutated_mod.get_global_var('func_6101')
call_6917 = relay.TupleGetItem(func_6099_call(), 0)
call_6918 = relay.TupleGetItem(func_6101_call(), 0)
output = relay.Tuple([call_6917,])
output2 = relay.Tuple([call_6918,])
func_6919 = relay.Function([], output)
mod['func_6919'] = func_6919
mod = relay.transform.InferType()(mod)
mutated_mod['func_6919'] = func_6919
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6919_call = mutated_mod.get_global_var('func_6919')
call_6920 = func_6919_call()
output = call_6920
func_6921 = relay.Function([], output)
mutated_mod['func_6921'] = func_6921
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6949 = relay.var("var_6949", dtype = "bool", shape = ())#candidate|6949|()|var|bool
var_6950 = relay.var("var_6950", dtype = "bool", shape = (2, 14, 8))#candidate|6950|(2, 14, 8)|var|bool
bop_6951 = relay.logical_and(var_6949.astype('bool'), var_6950.astype('bool')) # shape=(2, 14, 8)
uop_6965 = relay.acosh(bop_6951.astype('float32')) # shape=(2, 14, 8)
func_2627_call = mod.get_global_var('func_2627')
func_2629_call = mutated_mod.get_global_var('func_2629')
const_6976 = relay.const([[-3,10,-2,9,4,-6],[5,10,-3,3,-5,10],[-2,-5,-8,5,-4,7],[-7,-1,2,-4,9,-7],[2,-6,10,-10,-10,-5],[-6,2,-5,-5,5,-3],[-5,-6,-2,-7,-2,3],[9,-4,2,7,-2,-9],[10,-7,-10,-4,9,1],[10,6,-3,3,4,-10],[9,-4,6,5,-7,-3],[-5,4,-6,5,-3,9],[2,7,-9,4,-4,-8],[2,-8,-8,-8,5,-6],[8,-6,-4,6,-7,4],[10,4,6,4,-7,-1],[-3,-7,2,9,5,-1],[-2,-7,-10,7,-8,-3],[4,4,-2,-6,3,-5],[-7,7,2,2,-4,7],[7,7,-6,10,10,3],[9,10,3,7,10,3],[-1,-7,2,-3,9,-6],[10,7,10,-5,1,10],[-1,-5,2,-2,-1,-10],[-5,3,10,-1,5,-4],[9,-3,5,6,2,-4],[7,7,-6,-2,9,7],[5,2,7,7,5,8],[-5,3,-6,-4,-4,-3],[-8,-3,10,-8,9,7],[6,-6,5,-1,10,10],[3,-3,4,7,-10,-1],[-4,7,9,-1,-7,-7],[1,-5,-4,-9,10,1],[-7,-6,-1,-9,-5,8],[10,8,6,-2,-5,-10],[-3,-5,-10,-6,7,3],[-10,2,-9,-9,2,8],[5,9,-8,-1,7,-3],[10,-3,3,4,-8,-9],[1,-6,7,4,-6,4],[-1,5,8,-4,-7,-7],[5,-6,-2,-2,4,5],[-3,-3,-10,-1,9,9],[-3,-10,-4,-3,-10,3],[-5,-4,-4,8,8,6],[-8,8,-2,7,-4,10],[-5,6,-3,7,4,6],[-10,5,6,5,8,-3],[4,8,8,5,-10,-9],[10,10,9,1,-2,7],[-6,4,-8,6,9,-10],[-1,-8,-6,5,-5,9],[3,-3,-6,5,-3,-6],[7,2,6,-1,-7,-10],[-10,-6,-10,-6,4,-7],[10,-2,10,3,-2,1],[7,6,5,-4,9,-9],[-6,1,4,10,-10,6],[-4,9,-4,-3,4,-4],[5,3,9,-2,-9,-6],[-3,-9,-1,-6,4,1],[6,2,5,-1,5,4],[-8,-10,3,9,2,-10],[-3,-10,-2,8,6,9],[5,2,6,3,-4,2],[-8,-3,1,5,-2,2],[5,3,9,5,-4,3],[2,-5,-8,4,-9,6],[2,3,-6,7,4,-5],[4,6,-6,9,6,6],[2,-2,7,-1,9,3],[1,-9,2,8,5,-5],[5,-10,-9,-5,-8,-5],[4,6,-2,-1,10,7],[-5,9,1,10,9,4],[-8,-2,5,3,-3,-3],[9,7,-5,1,-9,9],[-6,3,10,-7,8,7],[7,3,1,7,1,7],[-6,5,1,-5,-10,6],[10,10,-5,1,7,3],[9,7,-4,5,5,7],[-1,-6,-3,-3,-8,-10],[10,-6,-5,-4,-1,-6],[7,4,1,-9,4,-5],[8,1,-3,-10,2,9],[-8,-4,3,-3,1,-2],[7,-5,7,-9,2,-2],[10,-5,1,-10,6,-6],[-3,-1,6,-7,7,5],[5,-10,5,9,7,8],[9,-4,3,8,-9,-10],[-2,-10,-2,2,1,2],[7,1,-9,-9,8,-5],[-3,7,-2,1,-8,3],[-5,5,1,2,-3,10],[-4,2,2,3,2,1],[6,8,-10,4,-7,3],[-10,-6,10,5,-4,-5],[6,-6,-7,2,7,-9],[-2,4,2,7,-4,5],[8,-9,-8,-1,-4,5],[-1,7,9,-7,-9,-10],[10,-2,-10,-10,8,-1],[4,5,6,-1,8,-9],[2,-8,8,-1,-5,5],[-2,4,-4,8,-4,8],[-2,-10,-7,-7,-4,-9],[5,5,6,7,-6,-10],[3,-10,3,-8,-9,5],[-7,6,-9,6,-6,8],[-10,10,4,-8,-7,6],[8,-5,4,4,4,5],[-4,1,-1,-2,2,10],[-3,6,7,-10,-8,4],[6,-5,8,8,-10,-4],[6,5,1,7,-4,-3],[-7,-5,-9,8,9,-8],[3,2,4,8,3,9],[9,-7,-9,3,5,-10],[1,10,1,-8,5,-10],[6,-9,1,7,4,-2],[-4,10,5,4,9,-5],[-3,5,-2,6,-10,1],[5,-1,1,3,-2,-5],[-4,-4,-4,-3,3,6],[2,-5,9,6,-3,-2],[-2,-10,-9,-3,7,-7],[-4,9,-8,-5,8,-5],[-8,-10,9,7,-8,-8],[-3,1,-6,-10,-7,-10],[-3,7,4,10,-2,3],[6,-5,-7,3,-1,2],[3,10,3,6,4,9],[5,2,-4,9,4,-2],[6,-5,-10,-6,8,-2],[7,-9,1,-1,-9,-6],[-7,-1,-8,4,-10,2],[-3,-4,6,6,-6,-4],[-2,5,-7,4,-5,-5],[-2,6,-5,4,9,-2],[4,6,-10,-6,7,-6],[2,8,-9,-10,-9,2],[9,3,2,10,-3,5],[-1,8,4,-2,-5,6],[1,-4,-6,-6,10,10],[-5,9,9,1,-7,-7],[4,1,-10,-5,5,-3],[4,6,9,8,-6,-1],[-3,4,1,2,1,-7],[10,-3,-1,-6,6,-1],[-7,8,-5,10,-1,-7],[8,-8,-5,-9,6,2],[8,2,-9,10,1,-1],[9,4,10,2,3,6],[-4,-2,8,-8,1,2],[-3,10,-2,-10,-6,9],[-10,-1,-1,-10,3,7],[-8,-8,5,3,-4,-3],[5,7,2,5,-9,4],[3,-6,7,-8,8,-6],[-7,2,1,8,-3,-5],[-3,4,7,1,-1,6],[10,-3,-9,-1,9,8],[1,5,-10,-8,3,4],[-9,9,4,7,1,-2],[10,-7,-9,8,10,3],[-4,-3,-2,-6,-6,10],[-2,3,9,-4,-9,8],[5,-9,9,-4,-2,9],[-6,6,10,1,4,-7],[-9,4,1,7,7,-10],[-7,-9,-1,-6,1,-8],[-9,7,3,8,5,4],[-3,-4,9,7,6,7],[-4,4,-7,10,-1,1],[1,10,1,-3,-6,-5],[1,-1,9,4,-2,-9],[-3,5,6,-10,5,-10],[-5,-1,10,-6,-9,7],[8,1,4,-9,9,-10],[1,-9,-3,5,3,-9],[-3,3,-5,-1,-6,2],[-2,-4,6,5,8,-6],[-4,9,6,-10,6,-2],[-6,1,-5,1,-4,8],[2,7,-7,1,3,-9],[-9,-9,-4,3,8,-3],[8,10,-10,-4,-2,-2],[-6,-2,-2,-10,-2,5],[2,8,-3,2,-7,-5],[-1,-9,2,3,2,-6],[6,7,-5,-4,10,6],[2,-9,2,-6,-5,-7],[-4,-2,8,3,2,-4],[2,-3,-9,-8,-8,-10],[10,-5,-10,-1,-5,-3],[1,-8,7,1,9,2],[4,1,-4,4,8,1],[4,-4,-5,1,-4,10],[-3,9,-4,10,-8,9],[3,-9,5,-10,-10,-5],[1,10,8,-5,10,1],[-4,9,5,7,3,10],[6,4,-4,2,8,-9],[1,-5,9,-4,-10,-4],[-2,10,6,5,10,5],[-10,-9,8,-3,3,1],[-6,4,7,9,-8,-7],[1,-4,1,4,8,-8],[-1,-7,-10,6,-3,-2],[-8,-10,-1,1,-8,2],[-6,-9,-10,-1,1,-5],[6,9,-2,2,1,6],[-8,4,2,5,2,2],[-4,-3,1,-8,-9,-8],[7,1,-1,-9,-6,7],[1,-7,10,5,2,-9],[-5,-2,3,5,10,-7],[7,-2,-3,2,-2,6],[-10,-6,-10,5,-3,10],[-7,-5,3,9,-1,2],[1,7,4,-7,-6,-7],[9,4,9,9,10,-2],[-7,-2,2,-10,9,6],[3,-8,-6,7,-6,-9],[-6,-8,2,9,1,-8],[5,-5,7,8,3,-9],[10,6,9,-1,-4,3],[-1,5,-4,-6,-1,1],[-2,-8,-4,6,6,-2],[-9,-2,-3,7,7,-7],[-5,10,-6,5,-10,5],[-3,2,4,6,8,-4],[-5,7,5,5,-7,-7],[5,-10,-9,1,-5,1],[8,5,-5,6,-2,-2],[-7,8,-1,8,6,-1],[3,7,4,9,5,-7],[-3,-10,6,-3,-8,-8],[3,-5,1,6,-5,-4],[-10,10,-7,4,9,-6],[-8,7,-9,7,8,2],[5,5,-10,-2,4,-6],[10,-2,5,-4,-8,-1],[6,8,7,7,-10,5],[-3,-2,8,7,-1,-6],[8,9,1,-4,7,4],[4,7,4,-7,8,2],[-9,-3,10,7,9,6],[8,-10,-4,1,6,5],[2,6,1,-8,-9,-9],[2,8,1,-5,4,6],[-10,7,4,5,-3,-8],[9,3,8,-6,7,4],[-8,9,-4,3,9,-1],[1,1,-9,8,-4,7],[-2,-2,8,7,5,-9],[10,-5,3,3,4,-10],[2,10,-7,-10,1,-8],[-10,-5,10,5,8,-8],[-8,5,-5,-4,10,-7],[-2,-6,10,1,8,6],[10,9,-3,-8,-9,2],[7,3,1,-6,6,5],[-5,-6,10,2,-3,-7],[7,-5,8,10,-5,-3],[-10,7,-1,2,7,-1]], dtype = "uint8")#candidate|6976|(270, 6)|const|uint8
call_6975 = relay.TupleGetItem(func_2627_call(relay.reshape(const_6976.astype('uint8'), [12, 15, 9])), 0)
call_6977 = relay.TupleGetItem(func_2629_call(relay.reshape(const_6976.astype('uint8'), [12, 15, 9])), 0)
func_4447_call = mod.get_global_var('func_4447')
func_4451_call = mutated_mod.get_global_var('func_4451')
var_6981 = relay.var("var_6981", dtype = "float64", shape = (1, 130))#candidate|6981|(1, 130)|var|float64
const_6982 = relay.const([2.708264,-5.000998,-7.575734,-8.929015,2.914852,-3.975207,-9.476443,-6.943356,-4.366168,3.083949,9.631351,-1.783332,-1.843943,7.472788,8.994453,-3.912389,-9.023618,-3.716693,1.733129,-5.434682,-9.564270,-1.214020,0.972187,5.339365,-9.203214,-5.076029,-7.478195,5.362119,-2.860883,-1.872070,2.245837,-4.162539,5.733107,-0.466583,1.998945,-8.382322,0.577319,7.287013,8.569967,-6.470083,5.743957,2.388145,6.882299,-1.794387,5.655622,6.113553,-1.196820,5.579311,2.140725,-3.463606,-6.096276,-4.170746,0.617025,-0.431974,-5.528692,-2.868770,3.858859,8.760434,-1.769477,4.161845,-0.483572,-9.204298,-3.233316,-2.288062,6.500129,1.255819,5.738633,-5.896442,9.348962,0.836642,0.875713,4.712575,6.724620,-4.386617,9.097195,-5.646034,-2.240390,-6.710379,-7.626484,-2.187249,3.470156,0.180869,8.918846,-5.390733,1.729448,-8.575817,4.295069,3.735008,-6.957375,3.114427,4.776761,7.260569,-4.056180,6.317256,9.046209,2.723393,3.467049,8.061548,-7.235776,5.799022,-7.408158,-7.779958,5.953652,-2.489364,2.941495,2.193137,6.859022,7.946381,-8.557429,-7.475133,-2.126362,5.073787,2.996213,1.079415,-1.152367,0.839619,-3.833139,-1.644607,7.871145,-4.538403,-8.833506,-2.925218,-9.851474,-1.136689,-0.812537,-7.400597,-4.889843,-7.368382,3.015797,6.373332,-4.459517,-0.546675,-7.386150,-1.822209,2.787078,3.010140,3.708772,-9.574589,7.984562,-0.955029,6.925228,-8.469226,-7.752477,9.086533,-1.150996,5.839522,4.624138,-1.611080,3.712358,-5.559144,7.182414,-0.160706,6.730405,-3.235552,0.314799,-7.740406,-8.545428,-2.888978,3.351671,-8.067936,-2.234743,-5.061308,8.967172,-9.263567,4.710958,4.387165,-4.530662,5.721901,-1.718274,-0.599586,7.709876,4.311077,0.461645,-8.176216,3.636942,7.491241,2.957945,-6.306583,-2.168162,2.112633,6.325931,-2.183792,-0.054684,1.242641,8.899754,2.960474,-2.405706,-4.018443,-2.056660,-0.880675,6.262261,-0.237044,9.587591,9.506699,1.605810,4.574271,-4.268854,-5.595215,-6.469558,7.439630,9.290893,-9.107107,8.231698,9.095758,5.100978,-7.729863,3.700244,6.987959,1.534961,-2.913941,4.088321,8.234826,6.913089,2.797596,3.419327,-6.431382,5.674636,-2.976386,2.652729,-6.812190,2.259646,-4.926874,9.135929,9.233885,-6.365733,3.116664,4.848602,0.278870,-7.218545,-2.713166,-0.515125,-8.535481,7.035550,-1.072695,7.048914,-7.391543,3.027800,3.686916,-1.849229,3.767219,1.506585,6.549828,9.210248,0.293373,6.993203,2.585341,-4.954283,4.483854,-1.754929,6.844121,-4.687990,-0.543152,-1.890616,1.984843,-7.742161,4.955647,5.131953,0.942109,-2.172546,4.318421,-2.299944,0.512728,-9.272974,5.286527,-0.277133,-6.881821,-3.958252,5.479572,2.464905,4.947974,8.493874,8.064142,1.637738,-5.769869,3.765937,0.259723,-7.041311,6.110862,4.043658,-7.276129,1.246452,8.064751,5.472862,-8.423642,0.298419,8.965002,-4.428973,4.890692,8.657774,3.664027,9.128179,-3.414555,1.896177,9.794466,-8.142495,9.607545,-8.632090,6.121730,9.836905,-3.389871,-4.258847,0.769466,-7.713989,-4.613405,-7.970120,4.865477,4.973134,-5.110297,2.053394,0.712475,2.709094,7.031289,7.130765,5.925458,-6.339966,2.279042,9.008775,7.067289,-9.009273,1.004084,-9.252211,-9.855790,4.402266,-5.687529,-4.728941,-8.329513,-4.057779,-9.316189,3.090669,-6.033211,2.919517,-6.043988,5.309255,8.713561,1.537055,-6.604527,4.084239,5.860634,4.368305,8.905431,-4.113886,1.046732,4.284231,-5.430292,-1.867261,-2.417556,4.042635,-0.901970,-4.049261,-8.436463,6.971766,7.997747,2.312362,9.239094,2.750762,3.661101,-5.435561,-4.969434,-5.668104,-2.835070,-5.330672,-8.758104,4.748525,-3.267897,-5.370106,-9.908748,5.757467,-2.140565,-4.024069,-5.329772,-0.207246,4.106852,-9.903903,-9.933882,5.454332,3.127582,7.815024,1.404953,1.583281,9.958913,-5.285018,8.157790,7.613144,-1.686424,1.987052,6.594802,-7.847597,-9.614010,0.863499,8.143682,-0.752932,-6.815193,9.721640,-6.128529,4.211574,-5.174809,8.062556,9.663436,-2.930742,7.547598,-7.755554,0.134303,2.658848,-4.296480,5.973964,9.161834,-8.357310,0.799082,5.718325,-5.194202,9.055713,-0.666352,-3.326597,-7.695278,-2.495586,-4.704257,-5.985608,8.160950,-8.210418,-5.764463,-6.880000,7.672434,0.014772,-3.136208,-9.428067,9.751273,5.868519,6.693662,-2.520022,-8.863834,6.951409,8.007903,5.987548,6.231800,-3.443101,2.420098,-2.756051,-3.990644,5.249000,-4.684907,8.370696,-9.439086,-8.807952,8.891479,5.205285,9.532657,-8.861736,-3.929380,8.471696,5.486155,-3.935961,-4.085002,6.701291,-0.197544,6.810512,6.848350,4.023162,-2.485143,1.346072,-5.226294,4.522452,3.791711,-6.144622,2.655995,7.977130,-1.403816,8.299512,-8.760611,1.163408,-7.135529,-0.058202,5.723587,9.061020,5.163946,4.123203,8.360464,7.844126,5.540777,-1.916152,5.667511,6.670457,5.709214,3.441258,-8.801784,1.212914,0.020068,-5.119072,8.399798,-4.229759,-6.359633,-8.017741,2.726905,-6.158119,8.589040,7.399322,-2.720744,-8.552254,-8.398307,-9.656760,-4.474141,9.926361,7.369630,0.775921,5.744498,0.540173,3.940010,0.069172,8.905413,7.216141,-2.700482,9.770092,-1.637074,6.486776,6.562461,1.409559,8.887200,-0.397232,-3.879690,6.836542,2.050542,2.220120,-2.360274,8.387847,-8.273432,-8.536299,-2.593141,4.308048,-3.921998,8.215824,-5.486776,3.306244,4.838760,-7.190247,4.373004,0.806692,-4.747872,-9.722178,2.510652,-1.609599,-7.186057,-1.550770,6.605734,2.077930,-6.273774,7.299235,2.049290,-2.613164,-6.217630,-0.934748,-7.012246,8.976916,-5.738725,3.462391,9.111417,6.040883,9.162125,-8.826543,-1.388050,-2.784397,-7.311428,0.074408,-8.147568,-8.720924,4.350368,5.422124,-0.997265,-2.067405,-8.544410,-2.147689,-3.264923,4.354625,-4.557735,-1.231488,-7.752251,2.972396,-3.231790,-4.878418,6.947225,-7.480521,-1.162409,-3.797802,-0.861432,9.935531,7.759873,-9.486769,-5.871970,4.039049,-6.083332,9.729689,-7.468286,7.034095,0.145319,5.975950,8.176056,3.644994,5.251684,-8.333323,4.684067,-2.063669,-3.751308,-6.582981,6.879910,4.706743,3.326445,-6.752836,6.443041,-7.675047,6.928571,1.613220,3.267546,-6.840885,4.589031,-5.035608,3.234003,6.898254,-4.727730,-0.959790,2.483760,6.551552,-6.548670,-1.349060,4.201026,-4.732357,-6.294070,9.756125,0.307573,2.095843,4.508738,4.951671,-2.523271,-4.147183,-9.215855,-2.425046,-4.576105,-2.283891,1.974339,-5.530227,0.587992,-2.055844,1.909570,-6.294537,4.040294,4.343669,3.529537,1.135309,8.322901,-7.063666,-6.648586,8.046512,-9.532671,0.310870,-2.740040,1.008537,4.245085,6.136356,9.047076,3.659596,5.937706,1.106753,8.257733,4.704982,-6.724736,-9.722190,-4.454453,6.564123,1.548494,5.098632,3.623048,4.446095,-1.126152,6.672072,-0.304221,-4.453633,6.442666,5.224511,3.850597,3.526019,-9.854855,-0.484365,0.954308,-1.862792,7.539492,-4.247049,-8.560214,9.324555,-0.721783,-1.695609,2.221550,8.623804,8.044246,7.715278,6.489473,-2.180995,-5.242881,-6.627342,5.565865,-4.865238,-9.477439,6.713885,-1.093090,4.680329,1.254506,-7.185001,4.402010,3.768308,-0.304663,6.552902,8.379649,1.236976,-2.805123,4.466103,-2.617383,-7.938225,-5.588441,2.998995,-5.386195,9.042281,3.087222,-9.218818,1.065985,2.606899,-5.537579,7.803613,-9.338981,3.560830,4.122414,-9.158664,-7.284507,-2.384268,-1.643355,-8.702818,9.511548,-7.679958,0.168299,9.884242,-1.166072,-4.736548,6.354757,-7.213234,-5.931160,-8.861805,-9.670002,-8.964675,-2.508627,5.781364,-6.941880,8.204657,-0.311007,-2.858041,7.337271,-7.937659,-2.716460,-6.620807,2.505670,-0.674896,5.099816,8.937970,1.842225,-9.491954,-3.393992,7.447536,6.629821,-7.217640,-5.334480,1.919848,-4.478816,-9.464064,-7.002214,-9.936388,8.439777,-8.446597,-9.020653,7.755395,3.154939,8.370502,7.927316,-3.910303,6.305759,-2.556136,-7.669002,1.744309,-9.387063,9.787882,2.969553,-0.939018,-9.652775,6.975670,-3.701559,2.879569,-3.490619,6.893727,7.513678,0.001354,8.332628,-7.770740,4.467450,-1.250592,3.954100,4.368146,-1.075394], dtype = "float32")#candidate|6982|(800,)|const|float32
call_6980 = relay.TupleGetItem(func_4447_call(relay.reshape(var_6981.astype('float64'), [26, 5]), relay.reshape(const_6982.astype('float32'), [800,]), ), 2)
call_6983 = relay.TupleGetItem(func_4451_call(relay.reshape(var_6981.astype('float64'), [26, 5]), relay.reshape(const_6982.astype('float32'), [800,]), ), 2)
uop_6984 = relay.erf(const_6976.astype('float32')) # shape=(270, 6)
func_2627_call = mod.get_global_var('func_2627')
func_2629_call = mutated_mod.get_global_var('func_2629')
call_6988 = relay.TupleGetItem(func_2627_call(relay.reshape(const_6976.astype('uint8'), [12, 15, 9])), 1)
call_6989 = relay.TupleGetItem(func_2629_call(relay.reshape(const_6976.astype('uint8'), [12, 15, 9])), 1)
uop_6999 = relay.asinh(call_6980.astype('float32')) # shape=(26, 5)
uop_7001 = relay.asinh(call_6983.astype('float32')) # shape=(26, 5)
output = relay.Tuple([uop_6965,call_6975,var_6981,const_6982,uop_6984,call_6988,uop_6999,])
output2 = relay.Tuple([uop_6965,call_6977,var_6981,const_6982,uop_6984,call_6989,uop_7001,])
func_7003 = relay.Function([var_6949,var_6950,var_6981,], output)
mod['func_7003'] = func_7003
mod = relay.transform.InferType()(mod)
mutated_mod['func_7003'] = func_7003
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7003_call = mutated_mod.get_global_var('func_7003')
var_7005 = relay.var("var_7005", dtype = "bool", shape = ())#candidate|7005|()|var|bool
var_7006 = relay.var("var_7006", dtype = "bool", shape = (2, 14, 8))#candidate|7006|(2, 14, 8)|var|bool
var_7007 = relay.var("var_7007", dtype = "float64", shape = (1, 130))#candidate|7007|(1, 130)|var|float64
call_7004 = func_7003_call(var_7005,var_7006,var_7007,)
output = call_7004
func_7008 = relay.Function([var_7005,var_7006,var_7007,], output)
mutated_mod['func_7008'] = func_7008
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6594_call = mod.get_global_var('func_6594')
func_6595_call = mutated_mod.get_global_var('func_6595')
call_7095 = func_6594_call()
call_7096 = func_6594_call()
output = call_7095
output2 = call_7096
func_7101 = relay.Function([], output)
mod['func_7101'] = func_7101
mod = relay.transform.InferType()(mod)
output = func_7101()
func_7102 = relay.Function([], output)
mutated_mod['func_7102'] = func_7102
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5801_call = mod.get_global_var('func_5801')
func_5802_call = mutated_mod.get_global_var('func_5802')
call_7154 = relay.TupleGetItem(func_5801_call(), 0)
call_7155 = relay.TupleGetItem(func_5802_call(), 0)
func_6118_call = mod.get_global_var('func_6118')
func_6122_call = mutated_mod.get_global_var('func_6122')
const_7158 = relay.const([[True],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[False],[False],[False],[True],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[False],[False],[False],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[False],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[True],[True],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[False],[False],[True],[True],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[True],[True],[False],[False],[False]], dtype = "bool")#candidate|7158|(792, 1)|const|bool
call_7157 = relay.TupleGetItem(func_6118_call(relay.reshape(const_7158.astype('bool'), [9, 11, 8]), relay.reshape(const_7158.astype('bool'), [9, 11, 8]), ), 0)
call_7159 = relay.TupleGetItem(func_6122_call(relay.reshape(const_7158.astype('bool'), [9, 11, 8]), relay.reshape(const_7158.astype('bool'), [9, 11, 8]), ), 0)
const_7183 = relay.const([[True,True,True,True,True,False,True,True,False,True,True],[False,True,True,False,False,False,True,False,True,False,False],[True,False,False,False,False,False,True,False,False,False,True],[True,False,False,False,True,True,False,False,False,False,True],[True,False,False,False,True,False,True,True,False,False,True],[False,False,True,True,False,False,True,False,True,True,False],[False,True,True,True,True,False,False,True,True,True,True],[True,True,False,True,True,False,True,True,True,False,False],[True,True,False,True,False,False,False,True,True,False,False],[False,False,True,False,False,False,False,True,True,True,True],[False,True,False,False,False,True,True,False,True,False,True],[True,True,False,False,False,True,True,False,False,True,False],[True,False,False,False,False,False,True,True,True,True,False],[True,True,True,False,True,True,False,True,True,True,True],[True,True,True,False,False,True,False,False,False,False,False],[False,False,False,False,True,True,True,True,False,False,False],[True,True,True,False,True,True,True,False,False,False,False],[True,True,False,False,True,False,False,True,False,True,True],[False,True,True,False,True,False,False,True,False,True,False],[False,True,True,True,True,False,True,True,False,False,False],[False,False,False,True,True,True,True,False,True,False,True],[False,False,False,False,False,False,False,True,False,False,False],[False,True,True,False,False,True,False,False,True,False,True],[True,True,False,True,True,False,False,True,True,False,True],[False,False,True,False,False,False,False,True,False,False,False],[False,False,True,True,False,True,False,True,False,False,False],[False,True,True,False,True,False,False,True,True,False,True],[False,False,True,False,False,False,True,True,True,True,True],[False,False,False,True,False,True,False,False,True,False,True],[True,True,False,True,True,True,True,True,False,True,True],[False,False,True,False,True,False,True,False,False,True,False],[False,True,False,True,True,True,False,True,False,True,False],[True,True,True,False,False,False,True,True,True,True,True],[True,True,False,True,True,False,True,False,False,True,True],[True,False,False,False,True,False,False,False,False,True,True],[False,False,True,False,True,True,False,False,False,True,True],[True,False,False,True,False,True,False,True,False,True,False],[True,True,True,True,True,True,True,True,True,True,True],[False,False,False,True,False,False,False,True,True,True,True],[False,False,True,True,False,True,True,True,True,False,False],[False,True,False,True,True,True,False,False,False,True,False],[False,False,False,False,False,True,True,True,True,True,False],[False,False,False,True,False,False,False,False,False,False,False],[False,False,True,True,False,True,True,True,False,True,False],[False,True,False,False,True,False,True,False,False,True,True],[False,True,True,False,True,True,True,False,True,True,False],[False,True,False,False,False,False,False,False,False,False,True],[False,False,False,False,True,True,False,True,False,True,False],[True,True,True,False,False,True,False,False,True,False,True],[False,False,True,False,False,True,False,True,True,False,True],[True,True,True,False,True,False,False,False,False,True,False],[True,False,False,True,False,False,False,False,True,False,True],[True,False,True,False,False,False,True,True,False,True,False],[True,True,True,True,False,False,True,True,False,False,True],[False,True,True,True,False,False,False,False,True,True,True],[False,False,True,True,True,False,True,False,False,False,False],[False,True,False,False,False,True,False,False,True,False,False],[False,True,False,False,False,False,True,True,True,False,True],[True,True,True,True,False,True,False,False,True,False,True],[True,False,True,True,False,True,False,False,True,False,False],[True,True,False,False,False,True,True,False,True,False,True],[False,False,True,True,False,True,True,False,False,False,False],[True,True,False,True,True,False,False,False,False,False,True],[False,False,True,False,True,False,True,False,True,True,False],[True,False,False,False,True,False,True,False,False,False,True],[False,True,True,False,False,True,True,False,False,True,False],[True,True,True,True,False,True,True,True,True,False,False],[True,False,True,True,True,True,True,False,True,True,True],[False,False,True,True,True,True,True,False,True,False,False],[True,False,False,False,True,False,False,True,False,True,True],[True,True,True,True,False,True,False,False,False,False,False],[False,True,True,True,False,True,True,False,True,False,False],[False,False,True,False,False,False,False,False,False,True,True],[True,False,True,False,False,True,False,False,True,False,True],[False,False,True,False,True,False,True,True,False,True,True],[False,True,False,False,True,False,False,True,True,True,True],[False,True,False,False,False,False,True,False,False,False,False],[True,False,True,True,True,False,False,True,False,False,False],[False,False,False,False,True,True,True,False,False,True,False],[False,True,False,True,True,False,True,True,True,False,True],[False,False,False,True,False,True,True,False,False,True,False],[False,True,True,True,False,False,True,True,False,False,True],[False,True,False,False,False,True,True,False,False,False,False],[False,True,False,False,False,False,False,True,True,False,False],[False,True,False,False,False,True,False,False,False,False,True],[False,True,True,True,False,False,True,False,False,False,True],[True,False,True,True,False,False,False,False,False,True,True],[False,True,True,False,False,False,False,False,True,True,True],[True,False,False,True,False,False,True,False,False,False,False],[True,False,False,False,False,False,False,True,True,True,True],[False,True,True,False,True,True,False,False,True,True,True],[True,False,True,True,True,True,True,False,True,True,False],[True,True,False,True,True,False,False,False,True,False,True],[False,True,True,True,True,True,False,False,False,True,False],[True,True,True,False,False,True,True,True,True,False,False],[False,True,False,False,True,False,True,False,False,True,True],[True,False,False,False,True,False,True,False,False,False,True],[True,True,False,True,False,True,False,True,False,False,False],[False,False,False,False,True,False,False,False,True,True,True],[True,False,False,True,True,False,True,True,False,False,False],[False,True,True,True,False,False,True,False,False,True,True],[False,False,False,False,False,True,True,False,False,False,False],[False,True,True,False,False,False,False,True,True,False,False],[False,False,False,False,True,True,False,True,False,True,True],[False,True,True,True,True,True,True,True,True,True,True],[False,False,True,True,False,False,False,True,True,False,True],[True,False,False,False,False,True,False,True,False,True,True],[False,False,False,True,False,True,True,True,False,True,True],[False,False,False,False,False,True,True,False,False,True,False],[False,True,True,False,False,False,False,True,True,False,True],[True,False,True,True,True,True,True,False,False,True,True],[False,False,True,True,True,False,True,False,False,False,False],[True,False,False,False,False,True,True,True,False,True,True],[False,False,False,True,True,False,True,True,True,False,True],[True,True,False,True,True,True,True,True,True,True,True],[True,True,True,False,False,False,False,True,True,False,True],[True,True,True,False,True,False,True,True,True,False,False],[True,True,True,False,True,False,True,False,True,False,True],[True,False,True,True,True,True,True,True,False,False,True],[True,False,False,True,False,True,False,False,True,False,False],[True,False,True,True,False,True,True,False,False,False,True],[True,True,False,False,False,True,True,True,False,False,True],[False,False,True,True,False,False,True,False,False,False,True],[True,True,True,False,False,True,False,False,False,True,False],[False,False,False,False,True,True,False,True,True,True,True],[False,False,False,False,True,False,False,True,True,True,True],[False,True,True,False,True,False,False,True,False,True,True],[False,True,False,False,True,True,True,False,True,True,True],[True,False,False,True,False,False,True,False,True,True,True],[False,True,True,False,False,False,False,True,True,True,False],[True,True,True,False,False,False,True,True,True,False,True],[True,False,False,True,True,False,False,False,True,True,False],[False,True,False,False,False,True,True,True,True,False,False],[False,True,False,False,False,True,True,True,True,True,True],[True,False,False,True,True,False,False,False,False,True,True],[False,True,True,True,True,False,False,True,False,True,False],[False,True,True,False,True,False,True,False,True,False,False],[True,True,True,True,True,True,False,False,True,False,False],[False,False,True,True,False,False,True,True,True,False,True],[False,False,False,False,True,False,True,True,False,False,False],[False,True,True,True,True,False,False,False,False,True,False],[True,False,False,True,True,False,False,True,True,False,True],[True,False,False,True,True,True,True,True,True,True,True],[True,True,False,True,True,False,True,False,False,False,False],[True,True,False,True,False,True,False,False,True,True,True],[True,False,False,True,True,False,False,True,True,True,False],[True,False,True,False,True,False,False,True,False,True,True],[False,False,True,False,False,True,True,True,False,False,True],[True,True,True,True,False,False,False,True,False,True,False],[True,True,True,True,False,True,False,True,False,False,False],[True,False,False,False,True,False,True,False,True,False,True],[False,True,True,False,True,True,False,False,True,False,False],[False,True,False,True,True,True,True,False,True,False,False],[False,True,False,False,False,False,True,False,True,False,True],[True,False,False,False,True,False,True,True,False,True,False],[False,True,False,False,False,False,True,True,False,True,False],[False,True,False,False,True,False,False,True,True,True,True],[True,True,False,True,False,True,False,True,False,False,False],[False,False,True,False,False,False,False,True,False,True,True],[False,True,False,False,True,True,True,False,False,False,True],[True,True,True,False,True,True,False,False,True,False,False],[False,False,False,False,True,False,False,False,True,False,True],[True,False,True,False,True,True,False,True,True,True,True],[False,False,False,True,False,False,True,True,True,True,True],[True,False,False,True,False,False,False,True,False,True,True],[True,True,True,False,False,False,True,True,True,False,True],[False,True,False,False,False,True,True,False,False,True,False],[True,False,False,True,True,True,True,False,True,False,False],[False,True,False,False,False,True,False,False,True,False,False],[True,False,False,False,False,False,False,True,False,True,True],[True,True,False,False,False,True,True,True,True,True,False],[True,False,False,False,False,True,True,False,True,False,False],[True,False,False,False,True,True,False,False,True,True,True],[True,False,False,False,True,True,True,True,True,False,True],[True,True,True,False,False,True,True,True,True,True,True],[False,True,False,True,True,True,False,True,False,False,True],[False,False,False,True,False,True,False,False,False,False,True],[True,False,False,False,False,True,False,True,False,False,False],[True,True,True,False,False,False,False,False,True,True,False],[False,False,False,True,True,True,False,True,False,True,True],[False,False,True,True,False,False,False,False,False,True,True],[False,True,True,False,True,True,False,False,False,False,True],[False,True,False,True,True,True,False,True,False,False,True],[False,False,True,False,False,True,True,True,False,True,False],[False,True,True,True,True,False,True,True,True,False,True],[True,True,False,False,True,True,False,False,False,False,False],[True,True,False,False,False,True,True,True,True,True,False],[False,False,False,False,False,True,True,False,False,False,True],[True,False,True,False,True,True,True,True,True,False,False],[True,True,False,False,False,True,True,True,False,True,True],[False,False,True,True,True,True,False,False,True,True,False],[False,True,True,True,False,True,False,True,True,True,False],[False,True,False,True,False,True,True,True,False,True,True],[False,True,True,True,True,True,False,False,True,False,True],[True,True,False,False,True,True,True,False,True,True,True],[True,True,True,False,False,True,False,False,False,False,True],[True,False,False,False,False,False,False,True,True,True,False],[True,True,False,False,False,False,True,False,False,False,True],[True,False,True,False,True,True,True,True,False,False,True],[False,True,False,False,True,True,False,False,True,True,True],[True,False,True,False,True,True,False,False,False,True,False],[False,False,True,True,True,True,False,True,False,False,False],[False,True,True,True,True,True,True,False,False,False,False],[False,False,False,True,False,False,False,False,False,False,False],[False,True,True,True,True,False,True,False,True,False,True],[False,True,False,False,False,False,False,True,True,False,True],[True,False,False,True,False,False,True,False,False,True,True],[True,False,True,True,False,True,False,False,False,True,True],[False,True,False,False,True,True,True,False,False,False,False],[False,True,False,False,True,False,False,False,True,True,True],[False,True,True,True,True,True,True,False,False,True,True],[False,False,True,True,True,True,False,False,True,False,True],[True,True,False,True,True,True,False,True,False,True,False],[True,False,True,False,False,False,False,True,True,True,True],[False,False,True,True,False,True,False,True,False,True,False],[True,False,True,False,True,False,False,False,False,True,False],[False,True,False,False,True,False,True,False,True,False,True],[False,True,True,True,False,False,False,True,False,True,False],[False,True,True,False,True,True,True,False,True,True,True],[False,True,False,False,False,True,True,False,False,False,False],[True,True,False,False,True,True,False,False,True,False,True],[False,True,False,True,False,False,True,True,True,True,False],[False,True,False,True,False,True,True,False,True,False,False],[True,False,True,False,True,False,False,True,True,False,False],[False,False,False,False,True,True,False,False,True,False,True],[False,True,True,True,False,False,False,False,False,True,True],[True,True,False,True,True,True,True,False,False,True,False],[False,True,True,False,True,True,True,True,False,True,False],[True,False,False,True,False,True,True,True,False,True,True],[False,False,False,True,True,False,True,False,False,False,False],[True,False,True,False,True,True,False,True,True,False,True],[False,True,False,True,True,True,True,False,False,True,False],[True,False,False,True,False,False,False,False,False,True,False],[False,False,True,True,False,False,False,False,False,False,False],[False,True,True,True,False,True,False,True,True,True,False],[True,False,False,False,False,False,False,False,False,False,False],[True,True,False,False,False,True,False,False,True,False,False],[False,True,False,True,True,False,False,False,False,False,True],[False,False,True,False,False,True,False,True,True,True,False],[False,True,False,True,True,True,False,True,True,False,True],[True,True,False,True,True,True,True,True,False,True,True],[True,True,False,True,True,True,False,True,True,False,False],[False,True,False,True,True,True,False,True,False,True,False],[True,True,False,False,False,True,False,False,True,True,True],[True,False,True,False,True,False,True,True,False,True,True],[False,False,False,False,False,False,False,False,False,True,True],[False,True,True,False,True,True,True,True,True,False,True],[False,False,False,False,True,False,False,True,True,True,True],[True,True,False,True,True,False,False,True,True,False,False],[False,False,False,False,True,True,True,True,False,True,True],[True,True,True,True,True,False,False,False,True,True,True],[True,True,True,True,True,False,False,True,False,True,False],[False,True,True,True,False,True,False,True,False,True,False],[True,False,True,True,False,False,True,True,True,False,False],[False,False,True,False,False,True,True,True,True,True,False],[False,True,False,True,True,True,False,False,True,True,False],[True,True,False,True,False,True,False,False,False,True,False],[True,True,True,False,False,False,True,False,True,False,True],[True,True,False,True,True,False,False,True,False,True,False],[False,False,False,True,True,False,True,False,True,True,True],[False,True,False,False,True,False,True,True,True,True,False],[True,False,False,True,False,True,True,False,True,True,False],[True,False,True,True,False,True,False,True,True,False,False],[True,True,True,True,False,False,False,True,True,True,True],[True,False,False,False,True,False,True,False,False,False,False],[False,True,False,True,False,True,False,False,False,True,True],[True,False,False,False,False,True,True,True,True,False,True],[True,False,False,True,True,False,True,True,True,True,False],[True,True,False,True,True,True,True,True,False,False,True],[False,False,False,False,True,True,True,True,True,False,True],[True,True,False,False,False,True,True,False,False,False,True],[False,True,False,True,False,True,False,True,True,False,True],[True,False,True,False,True,False,True,True,False,True,False],[False,True,True,False,False,True,False,False,False,False,False],[False,False,False,False,False,True,True,False,True,False,True],[False,False,False,False,False,False,False,True,False,True,False],[True,True,False,False,True,False,False,True,False,True,True],[True,True,True,False,False,False,True,False,True,True,False],[True,False,False,True,False,True,False,True,True,True,False],[True,False,True,False,False,True,False,True,False,True,False],[False,False,False,False,True,False,True,True,True,False,True],[True,False,True,True,False,True,False,True,True,False,True],[True,False,False,False,False,True,False,False,False,False,False],[False,False,True,True,True,False,False,False,True,True,False],[True,False,False,False,True,True,True,True,True,False,True],[True,False,True,False,True,True,False,True,True,True,False],[True,False,True,True,False,True,True,True,True,False,False],[True,False,True,True,True,False,False,False,True,True,False],[False,True,True,False,False,True,True,True,True,False,True],[False,False,True,False,True,False,True,True,False,True,True],[True,False,False,True,False,False,False,True,True,True,False],[False,True,False,True,False,True,False,True,False,True,True],[True,True,False,False,False,True,False,True,False,False,True],[False,True,True,True,False,False,False,True,True,False,False],[True,False,False,True,False,True,True,True,False,True,False],[False,True,True,True,True,False,True,True,False,False,True],[True,True,True,False,True,False,True,True,False,False,True],[False,True,False,False,True,True,False,False,False,True,True],[True,False,False,True,False,False,True,False,True,True,True],[False,True,False,False,False,True,False,False,True,False,False],[True,False,True,False,True,True,False,False,False,True,False],[False,True,False,False,False,False,True,True,True,True,False],[True,True,False,True,True,True,False,False,True,True,False],[False,True,True,True,False,True,True,True,False,True,False],[False,False,True,True,True,False,False,True,True,False,False],[True,True,False,False,True,False,True,False,False,True,True],[False,False,True,True,True,True,True,True,True,False,True],[False,True,False,True,True,True,False,True,False,True,False],[False,False,True,False,True,True,False,True,True,False,True],[False,False,True,True,True,False,True,True,True,True,False],[True,False,False,True,False,True,True,False,False,True,False],[True,True,True,True,True,False,False,False,False,False,False],[True,False,True,True,True,True,False,False,True,True,True],[True,False,True,True,True,True,True,False,True,False,True],[True,True,True,True,True,True,True,False,True,False,False],[False,True,True,True,True,True,True,True,False,False,True],[False,True,True,True,False,True,True,True,True,False,False],[False,True,False,True,True,False,False,True,False,False,True],[True,False,False,False,True,True,True,True,True,True,True],[False,False,True,True,True,False,False,True,True,False,True],[True,True,False,True,True,True,True,False,False,False,False],[True,False,True,False,True,False,True,False,True,True,True],[True,True,False,True,True,False,False,False,True,True,True],[True,False,True,False,True,True,True,True,True,False,False],[False,False,True,False,False,False,False,True,True,True,False],[True,False,False,True,True,False,False,False,True,True,True],[False,False,False,True,True,False,False,True,False,False,True],[True,True,True,True,True,True,False,False,True,False,False],[True,True,True,True,False,False,True,True,True,True,True],[True,True,False,True,True,True,True,False,True,True,True],[False,False,False,True,True,False,True,True,False,False,False],[False,False,False,False,True,False,True,False,True,False,True],[False,False,True,True,True,True,False,False,False,True,True],[False,False,False,False,True,True,False,False,True,False,False],[False,False,True,False,True,True,True,False,True,True,False],[False,True,True,True,True,False,True,False,True,True,True],[True,True,False,False,True,False,True,False,False,True,False],[True,True,False,True,True,False,False,False,False,False,True],[True,True,True,True,False,True,False,True,False,True,False],[True,True,True,True,True,True,False,False,False,True,False],[False,False,True,False,False,True,False,False,True,True,True],[False,True,True,True,True,False,False,True,False,True,False],[False,False,True,True,False,False,True,False,False,True,False],[True,True,True,False,True,True,True,True,True,True,False],[False,True,True,True,True,False,True,False,True,True,False],[False,True,True,False,False,True,False,False,True,True,True],[False,False,True,False,True,False,True,True,False,True,False],[True,False,True,False,False,True,True,True,True,True,False],[False,False,True,True,False,True,True,False,False,True,False],[True,True,True,True,False,False,True,False,False,True,False],[True,True,False,False,False,False,False,True,False,False,True],[True,False,False,False,True,False,True,False,False,False,False],[True,False,False,False,True,False,False,False,True,False,True],[True,False,True,True,False,True,False,True,False,True,True],[False,False,False,False,True,False,False,True,False,False,True],[True,False,True,True,False,True,False,False,True,False,True],[False,True,True,True,True,False,False,True,True,False,True],[True,True,False,False,True,True,False,True,True,True,True],[False,True,False,True,True,False,False,True,True,True,True],[True,False,False,True,False,True,True,True,False,False,False],[False,False,True,False,True,True,True,False,False,True,True],[False,False,True,True,True,False,False,False,True,True,False],[False,True,True,True,False,False,False,False,False,False,True],[True,False,False,False,True,False,True,False,False,True,True],[True,False,False,True,True,False,True,False,False,True,True],[True,False,True,True,False,False,True,True,True,True,True],[True,True,True,True,False,True,True,False,False,False,False],[False,False,True,False,True,False,True,False,True,False,False],[True,False,True,True,True,False,False,False,True,True,False],[False,False,False,False,False,False,False,False,True,True,False],[False,True,True,False,False,True,False,True,False,True,True],[True,False,False,True,False,True,False,True,True,True,True],[True,True,True,False,True,False,True,False,False,True,False],[False,False,False,True,False,True,True,True,False,False,True],[True,True,True,False,False,False,True,True,True,False,False],[True,False,True,True,True,False,True,True,False,True,True],[False,True,True,False,False,False,False,True,True,True,False],[False,True,False,False,False,True,True,True,True,False,True],[True,True,True,True,True,False,True,False,True,True,True],[False,True,False,False,False,True,True,True,True,True,True],[False,True,True,True,False,False,True,True,False,False,False],[True,True,True,True,False,False,False,True,True,False,True],[True,False,True,False,True,False,False,False,True,False,True],[True,True,True,True,False,False,True,False,True,False,True],[False,True,True,False,True,True,False,True,False,True,True],[True,False,False,True,False,False,True,False,True,False,True],[True,True,False,True,True,False,False,True,False,True,True],[True,True,False,False,True,False,False,True,True,True,True],[False,True,True,False,False,True,False,False,False,True,True],[False,False,False,True,True,False,True,False,True,False,True],[True,True,True,True,True,False,True,True,True,True,False],[False,True,False,True,True,False,True,False,True,False,True],[False,True,False,False,False,False,True,False,True,False,True],[False,False,True,False,True,False,True,False,False,True,True],[False,False,True,False,False,True,True,False,False,True,True],[False,True,True,False,False,True,False,True,True,False,True],[False,True,False,False,False,False,False,False,True,False,False],[False,False,False,False,True,False,False,True,True,True,False],[False,True,True,False,True,False,True,False,True,True,True],[True,True,True,True,True,True,False,True,False,True,True],[False,True,False,True,True,True,False,False,False,True,False],[True,True,True,True,False,True,False,True,False,True,False],[False,False,True,True,False,False,True,True,True,False,False],[True,True,False,True,True,False,True,False,False,False,True],[False,True,True,True,True,False,False,False,False,False,False],[True,True,False,True,True,False,False,True,False,False,False],[False,True,True,True,False,False,True,False,True,True,True],[True,True,False,True,True,False,False,True,False,True,False],[False,True,True,False,True,False,True,True,False,True,False],[False,False,False,False,False,False,True,True,True,False,False],[True,False,True,True,False,False,True,True,True,False,False],[False,False,False,True,True,True,True,True,False,True,True],[False,True,True,True,True,True,False,True,True,False,True],[True,True,True,True,True,True,False,True,True,True,True],[True,False,True,True,True,False,True,True,True,True,False],[True,False,True,False,True,True,True,True,False,False,False],[False,False,True,True,False,False,False,True,False,False,True],[True,True,True,True,False,False,False,True,False,True,False],[False,True,True,True,True,False,True,True,False,True,True],[False,False,False,False,True,True,False,True,True,True,False],[False,False,False,False,True,True,False,False,True,False,False],[False,True,True,False,True,False,True,False,False,True,True],[False,True,False,True,False,True,False,True,True,False,False],[True,False,True,False,True,True,False,True,True,False,True],[False,True,False,True,False,False,True,True,True,True,False],[True,False,False,False,True,False,True,True,False,False,False],[True,True,True,False,True,False,False,True,True,False,False],[True,True,False,False,False,True,True,True,False,True,False],[False,True,True,False,True,False,False,True,False,True,False],[True,False,True,False,False,True,True,False,True,True,False],[False,True,False,True,False,False,True,True,False,False,True],[True,False,False,True,True,True,False,False,False,True,False],[True,True,False,False,True,True,False,False,True,False,True],[True,True,True,True,True,True,True,True,False,False,True],[False,False,False,True,False,True,True,True,True,True,True],[False,True,False,True,True,False,False,True,True,True,True],[False,True,False,True,False,True,True,True,False,True,True],[True,True,True,False,False,False,True,True,True,True,True],[True,False,False,True,False,False,False,False,True,True,True],[True,False,True,False,False,False,False,True,True,True,False],[False,True,True,True,True,False,False,False,True,False,True],[False,True,True,False,False,True,True,True,False,False,True],[False,False,True,False,False,True,False,False,True,False,True],[False,True,False,True,False,True,False,False,False,False,True],[True,False,True,True,True,False,True,True,False,True,True],[True,False,False,False,False,False,False,False,True,False,False],[False,True,False,True,False,False,True,False,True,False,True],[True,True,False,True,True,False,True,False,True,True,False],[True,True,False,True,True,True,True,False,True,True,True],[True,False,True,True,True,False,False,True,True,True,True],[True,True,False,True,False,False,True,True,True,False,True],[True,False,False,False,True,False,True,False,False,False,False],[True,True,True,True,False,False,False,True,True,False,False],[True,True,True,False,False,False,True,True,True,False,True],[False,True,False,False,False,False,False,True,False,False,False],[True,True,False,True,False,False,True,False,False,False,True],[True,False,False,False,True,True,True,False,False,True,True],[False,False,True,False,False,False,False,False,True,True,False],[True,False,False,True,True,False,False,False,True,True,False],[True,True,False,False,True,False,False,False,True,False,False],[False,False,True,True,False,True,False,True,True,True,False],[True,True,True,True,True,True,True,False,False,False,False],[False,True,True,False,True,True,True,False,False,True,False],[True,False,True,False,False,False,False,False,False,True,True],[False,True,False,True,False,False,True,False,False,True,True],[True,True,True,True,False,True,True,False,True,False,False],[False,False,True,True,False,True,True,False,False,True,True],[False,True,True,False,False,True,True,False,True,False,True],[False,True,False,True,False,False,False,False,False,True,True],[True,False,True,False,True,True,False,True,False,False,False],[True,True,False,True,False,False,False,False,False,False,False],[False,True,False,False,True,True,False,False,False,False,False],[True,False,False,True,True,True,True,True,True,True,False],[True,False,False,False,False,True,False,False,True,False,True],[True,False,False,False,False,True,False,False,True,False,True],[True,True,False,False,False,True,True,True,False,True,True],[False,True,True,True,True,True,False,True,False,False,True],[True,False,True,False,True,False,True,True,True,True,False],[True,True,False,False,True,False,False,False,True,True,True],[True,False,False,False,True,True,True,True,False,False,True],[True,False,False,True,True,True,False,False,True,True,False],[False,False,True,False,False,True,True,True,False,False,False],[False,True,True,True,False,False,True,False,True,False,False],[False,False,True,True,False,False,True,False,False,True,False],[True,True,False,False,False,False,False,True,False,False,False],[True,True,False,True,False,False,False,False,False,False,False],[True,False,True,True,True,True,True,False,True,False,True],[True,False,True,True,False,False,True,False,False,False,True],[False,True,True,False,False,False,False,False,False,False,False],[True,True,True,False,True,True,True,True,False,True,False],[False,False,False,False,False,True,True,False,False,True,False],[False,False,False,False,False,False,False,False,True,False,False],[False,False,True,False,False,False,False,True,False,False,True],[True,True,True,False,False,False,False,True,False,False,True],[False,False,False,False,True,False,True,True,False,False,True],[True,False,True,False,False,False,False,True,False,True,False],[True,True,False,True,False,True,True,False,True,True,True],[True,False,False,True,True,True,False,True,False,True,True],[False,True,False,False,False,True,False,True,True,False,True],[True,True,True,False,True,True,True,False,False,False,False],[False,False,False,True,False,True,False,True,True,False,True],[True,False,True,False,True,False,True,True,True,False,False],[False,False,True,False,False,False,False,False,False,True,False],[False,False,False,False,False,False,True,False,True,False,True],[False,False,False,False,True,True,False,True,True,False,True],[True,False,True,True,True,False,True,False,False,False,False],[True,False,True,True,True,True,False,True,False,False,True],[False,False,False,True,False,True,True,True,False,False,True],[False,True,False,False,False,False,False,False,True,True,False],[False,False,True,True,False,False,False,False,True,False,True],[True,False,True,False,True,False,True,True,False,True,False],[False,True,False,True,True,True,False,True,True,False,True],[True,True,False,True,True,False,True,False,True,False,False],[True,True,True,True,False,False,True,True,False,False,False],[False,True,True,True,True,False,True,True,False,False,False],[False,True,False,False,False,False,False,True,False,True,False],[True,False,False,True,False,True,True,False,True,True,True],[False,True,False,True,False,True,True,False,True,True,True],[True,True,False,True,True,True,True,False,True,False,True],[True,True,True,False,False,True,True,False,False,True,True],[False,False,True,True,True,True,False,False,False,False,False],[False,True,True,True,True,False,False,True,True,True,True],[False,True,True,True,False,True,True,False,False,True,False],[True,False,False,False,False,False,True,False,False,True,False],[False,True,True,False,True,False,True,True,True,True,False],[True,False,True,False,True,True,True,False,True,False,False],[True,True,False,False,False,True,False,True,True,False,False],[False,False,False,False,True,True,False,False,True,True,False],[False,True,True,True,False,True,True,True,True,False,False],[False,False,False,True,True,True,False,True,False,False,False],[False,False,True,True,False,False,False,True,False,True,True],[False,False,True,True,True,False,True,False,False,True,False],[False,False,True,False,False,True,False,False,True,False,False],[False,True,True,False,True,False,True,False,True,True,True],[True,False,False,True,True,False,False,False,True,False,False],[False,False,False,True,False,False,False,False,True,True,True],[False,True,True,False,False,True,False,True,False,True,False],[True,False,True,True,False,False,False,True,False,True,True],[True,False,False,True,True,False,False,False,False,False,True],[True,True,False,False,True,True,True,False,True,False,False],[True,True,True,True,False,False,True,True,True,False,True],[True,False,False,False,False,False,False,True,False,True,False],[False,True,True,True,False,True,True,False,True,False,False],[False,True,False,False,False,True,False,True,False,True,True],[True,True,True,True,True,False,True,False,False,True,False],[True,True,False,False,False,True,False,False,True,False,True],[True,True,True,False,True,False,False,False,True,True,False],[True,True,True,True,False,False,False,False,False,True,True],[False,False,True,True,False,True,False,False,False,True,True],[True,True,False,False,False,True,True,True,True,False,False],[False,False,True,False,False,True,False,True,False,True,True],[True,False,True,False,True,False,False,False,True,True,False],[False,True,False,True,True,True,False,True,False,False,True],[True,True,True,False,True,True,False,False,False,True,True],[False,True,False,False,True,False,True,False,False,True,False],[False,False,True,False,False,False,False,True,False,True,False],[True,True,True,False,True,False,True,False,True,True,True],[True,True,False,True,False,False,False,False,False,False,False],[True,False,True,False,False,False,False,True,False,True,False],[True,False,True,True,True,True,False,False,False,True,True],[False,True,True,True,True,True,True,True,False,True,False],[True,True,False,True,True,False,True,False,False,False,False],[False,False,True,True,False,True,False,False,False,False,True],[False,True,False,True,True,True,True,False,True,False,True],[False,True,False,False,False,False,False,True,True,False,True],[False,False,True,False,False,True,False,False,False,False,False],[False,False,True,False,True,True,True,False,False,True,True],[False,True,False,False,False,True,True,False,False,False,False],[True,False,False,True,False,True,True,True,True,False,True],[False,False,False,True,True,False,True,True,False,True,False],[False,True,False,True,True,True,True,True,True,False,True],[False,True,True,True,True,False,False,True,True,False,True],[False,True,False,False,False,True,False,True,False,False,False],[False,True,True,True,False,False,True,True,True,True,False],[True,False,True,True,False,False,True,False,True,True,True],[False,True,True,True,False,False,True,False,False,False,False],[False,True,False,False,False,True,False,True,False,True,True],[True,False,True,False,True,True,True,False,False,True,False],[True,True,False,True,False,False,False,False,False,False,False],[True,False,False,False,False,False,False,True,True,False,False],[True,False,True,False,True,False,True,True,False,False,False],[False,False,False,False,False,True,True,False,True,False,False],[True,False,True,True,True,False,True,True,False,False,True],[False,False,False,False,True,True,False,False,True,False,False],[False,False,False,True,True,False,False,True,False,True,False],[True,True,True,False,False,False,False,False,True,False,False],[True,False,False,True,False,False,False,False,False,False,True],[False,True,False,False,True,False,False,True,False,False,False],[True,False,False,True,False,False,False,True,False,True,True],[False,False,False,False,True,False,False,True,True,False,True],[False,False,False,False,True,True,False,True,True,True,True],[True,False,True,True,False,False,False,True,False,False,False],[False,True,True,False,True,False,False,False,True,False,False],[False,False,True,True,False,False,True,True,True,False,True],[True,False,True,True,False,False,True,False,False,True,True],[True,False,True,False,False,True,True,False,True,True,False],[True,True,False,True,False,True,True,False,False,False,False],[True,True,False,True,True,True,False,False,False,True,False],[True,True,False,False,True,False,False,False,False,True,True],[False,False,True,True,True,False,True,True,False,False,True],[True,False,False,False,False,False,False,True,True,False,True],[True,False,False,False,False,False,False,True,False,True,False],[True,False,True,True,False,True,False,False,False,True,False],[False,True,False,False,True,False,True,True,True,True,False],[True,True,False,True,True,False,True,False,False,True,True],[True,False,True,False,False,True,False,True,False,False,False],[False,True,False,False,False,True,True,True,True,False,False],[False,False,False,False,True,False,False,False,True,True,True],[False,False,True,False,False,True,False,True,True,False,False],[True,True,False,True,False,False,False,True,False,False,True],[False,False,False,True,False,True,False,False,False,True,False],[True,True,False,False,True,True,False,True,True,True,False],[False,False,True,False,True,False,False,True,True,True,False],[True,False,False,False,False,False,False,True,False,False,False],[True,False,True,False,False,True,False,False,True,False,False],[False,False,True,False,False,True,True,True,True,True,True],[True,True,False,False,False,True,False,False,False,True,False],[True,False,True,False,False,True,False,False,True,False,False],[True,True,False,False,False,False,True,True,True,False,True],[True,False,True,True,True,True,True,False,True,False,False],[False,True,False,True,True,False,True,True,False,False,False],[True,False,True,True,True,False,False,True,True,False,False],[False,True,True,True,False,True,True,False,False,True,True],[False,True,False,True,False,False,True,False,False,False,False],[True,True,True,False,False,False,True,False,False,False,True],[True,True,True,True,False,True,True,False,True,True,True],[True,False,True,True,False,True,False,False,True,True,False],[False,True,False,False,True,False,True,True,True,False,False],[False,True,True,True,False,True,False,False,False,False,False],[True,True,False,False,True,True,True,True,True,True,False],[True,True,True,True,False,False,False,True,True,False,False],[False,True,True,True,False,True,True,False,True,False,True],[False,False,True,True,True,False,False,False,False,True,True],[False,False,False,False,False,True,True,False,True,True,True],[False,False,True,True,True,True,True,True,True,True,True],[False,False,False,False,False,False,False,True,False,False,True],[False,True,True,True,False,True,False,False,False,True,False],[False,False,False,True,True,True,False,False,True,False,False],[True,False,False,False,True,True,False,True,False,False,False],[True,True,True,False,True,True,True,False,True,True,True],[True,False,False,True,True,True,False,True,True,True,False],[False,True,True,True,True,False,False,True,True,True,False],[False,False,False,True,True,False,False,False,True,False,False],[False,True,True,True,True,True,False,False,True,False,False],[False,False,True,False,False,True,True,True,True,True,True],[True,False,False,False,True,False,True,True,True,True,False],[False,False,True,True,True,True,False,True,True,False,True],[True,True,True,False,False,True,True,False,False,True,False],[True,True,True,True,False,False,False,False,False,True,False],[True,False,True,True,True,True,False,True,False,True,False],[False,True,True,True,True,True,True,False,True,False,True],[True,False,True,True,False,True,False,True,False,True,False],[True,False,True,False,True,False,True,False,True,True,False],[False,False,True,True,True,True,False,False,False,True,False],[True,True,False,True,True,False,True,False,False,False,True],[True,True,False,True,False,False,False,True,False,False,True],[True,True,False,False,False,False,False,True,False,False,False],[True,True,True,True,False,False,True,False,True,False,True],[True,True,True,True,False,False,False,False,True,True,False],[False,False,False,False,False,True,True,False,False,False,True],[True,True,True,True,False,False,False,False,True,True,True],[True,True,True,True,True,False,True,False,False,True,False],[False,True,True,True,False,True,True,False,True,True,True],[False,False,True,False,True,True,False,False,True,True,True],[False,False,False,False,True,True,False,False,True,False,False],[False,False,False,False,True,True,True,False,False,True,True],[False,False,False,True,False,False,False,True,False,True,True],[False,True,True,True,False,True,True,False,True,True,False],[False,True,False,True,False,False,True,False,True,True,False],[True,True,False,False,True,True,False,False,False,False,False],[True,False,False,True,True,False,False,False,True,False,False],[True,True,False,True,True,False,True,False,False,False,True],[False,False,True,True,False,True,False,True,True,True,True],[True,False,False,False,True,False,True,True,False,False,True],[True,True,False,True,False,False,False,True,False,False,True],[True,False,False,False,False,True,False,True,False,True,False],[False,True,True,False,False,False,True,False,True,False,False],[True,True,False,False,True,True,False,False,True,True,False],[True,True,False,False,True,True,False,True,True,False,False],[False,False,True,True,True,True,False,True,True,False,True],[False,False,False,True,False,False,False,True,False,True,False],[False,True,False,False,True,True,True,True,True,False,False],[False,True,True,False,True,True,True,True,False,True,True],[False,True,True,True,True,False,True,True,True,False,False],[True,False,False,False,True,True,True,True,True,False,False],[True,False,False,False,True,True,False,True,True,False,False],[False,True,True,True,True,False,False,True,True,True,True],[True,True,False,False,False,False,False,False,False,True,False],[False,True,False,False,True,True,True,True,True,True,True],[False,False,False,True,False,True,False,True,False,True,False],[False,True,True,False,True,True,True,False,False,True,True],[False,True,False,True,False,False,False,False,True,False,False],[True,True,True,False,True,False,False,False,True,False,False],[False,True,True,True,False,False,True,True,True,True,True],[False,False,True,False,False,True,True,True,False,False,False],[True,False,False,True,False,False,False,False,False,False,True],[False,False,True,False,True,True,True,True,False,True,True],[True,True,False,True,False,True,True,False,True,False,False],[True,True,False,False,False,True,False,False,False,False,False],[False,False,False,True,False,True,True,True,False,False,True],[False,True,True,True,False,False,True,False,False,False,False],[True,False,False,False,True,False,False,True,True,False,False],[True,True,False,False,False,True,False,True,False,True,False],[False,False,True,False,True,True,False,False,True,True,False],[True,True,True,False,False,True,True,False,True,False,False],[True,False,False,False,False,True,True,True,False,True,False],[True,True,True,False,True,True,False,True,False,True,False],[True,True,False,False,False,True,True,False,True,False,False],[True,True,True,True,False,False,True,True,False,False,False],[False,False,True,True,False,False,True,False,True,True,True],[True,True,False,False,True,False,True,True,True,True,False],[False,False,False,False,True,True,True,True,True,True,True],[True,False,False,True,False,False,False,True,True,False,False],[True,False,True,False,False,True,True,True,True,True,True],[False,True,False,True,False,True,True,True,False,False,False],[False,True,False,False,False,True,False,False,True,True,False],[True,True,False,False,False,True,True,True,False,True,True],[False,True,True,True,False,True,False,False,True,False,True],[True,True,True,False,True,True,True,False,False,False,False],[False,False,False,False,False,False,False,True,True,True,False],[False,False,False,True,False,False,False,True,False,True,False],[True,True,True,True,True,True,True,True,True,True,False],[False,True,False,False,False,True,True,True,False,True,True],[False,True,False,True,True,True,True,True,True,False,False],[False,True,True,True,False,True,True,False,True,True,True],[True,True,True,False,False,False,False,True,False,True,False],[False,False,False,True,True,True,False,True,True,False,True],[True,True,True,False,False,True,True,True,True,False,False],[False,False,False,True,True,False,True,False,False,True,False],[False,False,True,True,False,False,True,False,True,False,True],[True,False,False,False,True,True,True,True,False,False,True],[False,True,False,False,False,False,True,True,False,True,True],[True,True,True,False,False,True,True,False,False,False,False],[False,True,True,False,False,False,False,False,True,False,True],[False,True,True,False,False,False,True,True,True,False,False],[False,False,False,True,False,False,False,False,False,False,True],[True,False,False,True,False,False,True,True,False,True,False],[True,True,False,False,False,True,True,True,False,False,True],[False,True,True,True,True,False,True,False,True,True,False],[True,False,True,False,True,False,False,False,False,True,False],[False,True,False,True,True,True,True,True,True,False,False],[False,True,False,False,False,False,False,True,False,True,False],[True,True,True,True,True,False,True,True,False,True,False],[False,True,True,False,False,False,True,False,True,True,True],[True,False,False,True,False,True,True,True,True,True,True],[True,False,False,True,False,True,True,True,False,True,False],[True,True,True,False,False,True,True,False,True,False,False],[True,True,False,False,False,True,False,True,False,True,False],[True,False,False,False,True,True,False,False,False,False,False],[True,False,False,False,True,False,True,True,False,False,False],[False,True,False,False,True,False,False,False,False,True,False],[False,False,True,True,False,True,True,False,True,False,False],[False,True,True,False,False,False,True,True,False,True,False],[True,True,True,True,False,True,True,True,True,True,True],[False,False,False,True,False,False,True,False,True,True,True],[False,True,False,True,False,True,True,False,True,False,True],[False,True,True,True,False,True,False,True,False,False,False],[False,True,False,True,False,False,False,True,False,False,True],[False,True,True,True,True,True,False,True,True,False,True],[False,True,True,True,True,True,False,True,True,False,False],[True,True,True,True,True,False,True,False,True,True,True],[True,False,False,False,False,False,True,False,True,False,True],[False,True,False,True,True,True,False,False,False,True,True],[True,True,True,True,False,True,True,False,False,False,False],[True,False,True,True,False,True,False,False,True,False,True],[True,False,True,True,False,True,True,False,False,False,True],[True,True,True,False,False,True,True,False,False,False,True],[True,True,True,False,True,True,True,True,False,True,True],[True,False,False,False,True,False,True,True,True,False,False],[False,True,True,False,False,True,False,False,False,True,True],[True,True,False,False,True,True,True,False,True,False,False],[True,True,True,True,False,False,False,False,False,False,True],[True,False,True,True,False,True,True,True,False,True,True],[False,True,False,False,False,False,True,True,False,False,False],[True,True,False,True,True,False,True,True,False,True,False],[True,False,False,True,True,False,True,False,True,False,False],[True,False,False,True,True,True,True,True,True,False,False],[True,True,True,False,False,False,False,True,False,True,True],[True,False,True,True,False,True,False,False,True,True,False],[False,False,True,True,True,False,True,True,False,False,False],[True,False,False,True,False,False,False,False,True,True,False],[False,False,False,False,False,False,True,True,False,True,True],[True,True,False,True,False,True,True,False,True,False,True],[True,False,True,True,False,True,True,True,False,True,True],[False,True,True,True,True,False,True,False,True,True,True],[True,False,True,False,False,False,True,False,True,False,False],[False,False,False,False,True,True,False,False,False,False,False],[True,True,True,True,True,True,False,False,True,True,False],[False,True,False,False,False,True,True,True,True,False,True],[False,False,False,True,False,False,False,False,False,True,False],[True,True,True,True,True,True,False,True,True,False,False],[False,True,True,True,False,False,False,False,True,False,False]], dtype = "bool")#candidate|7183|(792, 11)|const|bool
bop_7184 = relay.bitwise_xor(const_7158.astype('uint16'), const_7183.astype('uint16')) # shape=(792, 11)
output = relay.Tuple([call_7154,call_7157,bop_7184,])
output2 = relay.Tuple([call_7155,call_7159,bop_7184,])
func_7194 = relay.Function([], output)
mod['func_7194'] = func_7194
mod = relay.transform.InferType()(mod)
mutated_mod['func_7194'] = func_7194
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7194_call = mutated_mod.get_global_var('func_7194')
call_7195 = func_7194_call()
output = call_7195
func_7196 = relay.Function([], output)
mutated_mod['func_7196'] = func_7196
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4861_call = mod.get_global_var('func_4861')
func_4862_call = mutated_mod.get_global_var('func_4862')
call_7264 = func_4861_call()
call_7265 = func_4861_call()
func_6896_call = mod.get_global_var('func_6896')
func_6897_call = mutated_mod.get_global_var('func_6897')
call_7272 = func_6896_call()
call_7273 = func_6896_call()
output = relay.Tuple([call_7264,call_7272,])
output2 = relay.Tuple([call_7265,call_7273,])
func_7280 = relay.Function([], output)
mod['func_7280'] = func_7280
mod = relay.transform.InferType()(mod)
mutated_mod['func_7280'] = func_7280
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7280_call = mutated_mod.get_global_var('func_7280')
call_7281 = func_7280_call()
output = call_7281
func_7282 = relay.Function([], output)
mutated_mod['func_7282'] = func_7282
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2017_call = mod.get_global_var('func_2017')
func_2019_call = mutated_mod.get_global_var('func_2019')
call_7306 = relay.TupleGetItem(func_2017_call(), 0)
call_7307 = relay.TupleGetItem(func_2019_call(), 0)
func_5491_call = mod.get_global_var('func_5491')
func_5497_call = mutated_mod.get_global_var('func_5497')
var_7312 = relay.var("var_7312", dtype = "float32", shape = (24, 2))#candidate|7312|(24, 2)|var|float32
var_7313 = relay.var("var_7313", dtype = "int64", shape = (312,))#candidate|7313|(312,)|var|int64
const_7314 = relay.const([[8.831153],[4.136284],[-6.427034],[6.934375],[0.514889],[9.104759],[-9.750402],[-0.699948],[-0.457976],[-6.743447],[1.756695],[-9.508070],[0.657674],[6.393430],[8.603805],[3.445171],[-7.460722],[-3.503775],[-3.543645],[-1.252179],[7.691339]], dtype = "float32")#candidate|7314|(21, 1)|const|float32
call_7311 = relay.TupleGetItem(func_5491_call(relay.reshape(var_7312.astype('float32'), [4, 6, 2]), relay.reshape(call_7306.astype('bool'), [162,]), relay.reshape(var_7313.astype('int64'), [78, 4]), relay.reshape(const_7314.astype('float32'), [21,]), ), 0)
call_7315 = relay.TupleGetItem(func_5497_call(relay.reshape(var_7312.astype('float32'), [4, 6, 2]), relay.reshape(call_7306.astype('bool'), [162,]), relay.reshape(var_7313.astype('int64'), [78, 4]), relay.reshape(const_7314.astype('float32'), [21,]), ), 0)
output = relay.Tuple([call_7306,call_7311,var_7312,var_7313,const_7314,])
output2 = relay.Tuple([call_7307,call_7315,var_7312,var_7313,const_7314,])
func_7327 = relay.Function([var_7312,var_7313,], output)
mod['func_7327'] = func_7327
mod = relay.transform.InferType()(mod)
var_7328 = relay.var("var_7328", dtype = "float32", shape = (24, 2))#candidate|7328|(24, 2)|var|float32
var_7329 = relay.var("var_7329", dtype = "int64", shape = (312,))#candidate|7329|(312,)|var|int64
output = func_7327(var_7328,var_7329,)
func_7330 = relay.Function([var_7328,var_7329,], output)
mutated_mod['func_7330'] = func_7330
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6099_call = mod.get_global_var('func_6099')
func_6101_call = mutated_mod.get_global_var('func_6101')
call_7336 = relay.TupleGetItem(func_6099_call(), 0)
call_7337 = relay.TupleGetItem(func_6101_call(), 0)
output = call_7336
output2 = call_7337
func_7347 = relay.Function([], output)
mod['func_7347'] = func_7347
mod = relay.transform.InferType()(mod)
output = func_7347()
func_7348 = relay.Function([], output)
mutated_mod['func_7348'] = func_7348
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4485_call = mod.get_global_var('func_4485')
func_4486_call = mutated_mod.get_global_var('func_4486')
call_7357 = relay.TupleGetItem(func_4485_call(), 0)
call_7358 = relay.TupleGetItem(func_4486_call(), 0)
func_2526_call = mod.get_global_var('func_2526')
func_2529_call = mutated_mod.get_global_var('func_2529')
const_7385 = relay.const([-2.718029,8.013428,5.518368,-1.888622,-9.826853,8.574469,-7.813622,3.149372,2.226228,6.198879,2.626403,4.508341,2.007147,9.196822,-3.579344,2.043701,-8.614358,-4.392597,-3.245522,7.024763,-4.003380,2.158736,0.984606,3.473190,-0.819821,-5.686936,1.400365,-2.843480,-1.595646,3.578077,7.985359,9.711528,-3.039150,9.382745,0.431348,7.743784,8.164804,-8.139088,-1.414459,3.997222,-2.225835,-5.644440,9.329610,-2.629561,-7.167262,-4.470777,-7.380575,6.594542,-0.860428,6.127109,-7.860187,0.771015,-9.905824,-3.404343,-4.037848,2.027782,6.477616,-0.393250,-3.268019,4.800759,1.121174,3.746070,0.659467,-8.526597,0.940314,0.535011,-9.996103,-0.143769,-7.429035,7.441258,-8.089270,4.056230,0.864082,5.171366,-8.715224,-4.804208,-3.295303,9.188715,6.280808,9.122964,-7.284331,-0.796784,-7.552205,3.161100,4.925456,5.483969,3.001550,4.094885,-6.263809,-4.353234,8.337760,-9.544905,-6.550466,-2.044771,7.886019,6.417386,-6.590593,5.498538,-4.138865,-7.697413,5.338591,3.816760,-6.819486,3.915814,4.287129,-7.480676,0.638828,9.391927,-1.544251,6.115911,2.674693,1.359986,-4.071850,-2.059171,4.762382,-4.906589,-7.092954,1.049302,-5.640125,-2.109076,6.797710,6.908182,9.335312,-0.477151,-4.264817,-1.403213,-8.349726,0.478068,-8.892160,5.244751,-1.276962,-3.023682,-5.950418,-7.759899,5.651894,-9.459411,1.675757,3.421316,-0.527811,-5.624510,7.431934,3.294902,6.285477,-9.288783], dtype = "float32")#candidate|7385|(144,)|const|float32
var_7386 = relay.var("var_7386", dtype = "float32", shape = (288,))#candidate|7386|(288,)|var|float32
call_7384 = relay.TupleGetItem(func_2526_call(relay.reshape(const_7385.astype('float32'), [144,]), relay.reshape(var_7386.astype('float32'), [8, 36]), ), 8)
call_7387 = relay.TupleGetItem(func_2529_call(relay.reshape(const_7385.astype('float32'), [144,]), relay.reshape(var_7386.astype('float32'), [8, 36]), ), 8)
uop_7389 = relay.sigmoid(call_7384.astype('float64')) # shape=(8, 36)
uop_7391 = relay.sigmoid(call_7387.astype('float64')) # shape=(8, 36)
uop_7397 = relay.cos(uop_7389.astype('float64')) # shape=(8, 36)
uop_7399 = relay.cos(uop_7391.astype('float64')) # shape=(8, 36)
func_3139_call = mod.get_global_var('func_3139')
func_3142_call = mutated_mod.get_global_var('func_3142')
const_7401 = relay.const([6.228581,-0.039165,-6.726637,-9.205244,-2.851317,-0.603755,-3.307403,5.727642,-3.314502,3.417584,-1.154612,4.292006,3.197841,9.051874,-9.729401,-9.003824,-8.265320,0.445120,2.524387,6.695672,7.641595,-7.087611,1.284781,9.282938,2.862430,2.480236,6.370121,1.608818,-0.892158,8.858341,-6.383169,-9.977020,-7.525499,-8.213351,3.124935,1.267311,3.846650,-4.899511,1.650745,5.569452,-7.760914,-6.680347,3.875131,-2.673950,8.064243,2.760088,7.212021,-3.551335,3.889229,0.355910,-6.089051,0.551645,3.175667,0.882834,7.011289,8.802833,2.113538,9.046963,2.716316,-1.304797,5.926582,8.577045,2.466261,9.838628,-3.724628,5.952543,9.413321,-1.099167,3.770793,-2.107443,-8.405392,-2.828771,6.907921,1.543188,-8.118597,9.430807,3.108319,-7.267562,-1.408315,3.703544,7.893722,-9.645645,7.933531,9.950962,-7.670930,2.105109,4.398849,-3.092638,-3.390344,-4.497032,-5.961455,-5.602729,-6.402533,-5.996988,-8.315764,9.540380,1.564662,0.884498,-6.299455,2.611987,-1.407129,-9.807077,-6.397159,-3.680316,-3.318786,9.533883,0.351167,-9.288102,3.884533,-0.652335,-0.663105,2.947304,5.008985,-9.194136,4.963449,-5.918743,-8.189981,1.791167,-3.610224,9.695141,-0.996653,3.015436,9.570241,8.501864,-6.413681,-9.135273,9.314248,-7.686402,-5.173563,4.386204,-9.543052,1.223655,-5.268737,-7.037106,3.803465,4.903020,-8.008296,2.085669,-7.294485,-0.950741,-4.059152,8.416745,-6.590020,4.700368,-5.104526,-7.186091,-5.313720,7.592878,5.182335,5.221731,-1.420566,-8.503411,7.749353,-1.997835,1.276307,5.045106,9.176847,7.585246,-4.700134,6.477000,9.668571,-5.151699,5.516091,-5.891997,7.224270,1.476579,-8.264368,-8.867232,2.976785,7.215778,-9.506617,4.993712,2.980782,9.402932,2.512826,-1.873958,2.032979,-0.307567,8.428474,2.459463,1.094007,-6.870607,-7.002462,9.283069,2.501077,-3.246265,0.658031,5.625277,2.613606,0.055913,9.019274,4.807716,-9.141093,-4.529816,7.311899,-0.296833,-7.416693,-1.159074,6.359065,8.444419,1.059083,-2.808310,2.202201,3.360267,5.533477,7.456446,8.421039,0.272048,-4.322250,6.577295,9.996032,-5.306903,-9.808749,-0.178836,2.417524,-0.969902,-1.164560,3.245578,-7.806854,-2.421507,4.718677,8.689260,-9.290046,-0.729912,-9.275236,-2.322888,6.945028,0.494768,-6.941155,-7.062144,3.841793,-3.608185,1.382340,2.013069,-8.956040,6.004712,9.450497,-1.986345,5.699606,5.432444,-2.682706,0.925012,-7.269283,3.890334,4.825872,-0.616910,-3.651509,-3.293864,9.964815,-4.775718,0.207584,9.432832,-3.913845,-9.892724,6.697201,6.002744,-4.997059,0.054441,9.153732,9.584155,-6.021380,-4.631370,-3.767333,6.141758,-1.024916,4.576863,6.263926,7.188648,8.469020,-7.582672,5.252345,-9.165436,-6.328192,-8.136610,1.520464,-5.504570,-8.679712,-2.981836,6.448481,-3.786711,5.202664,1.957329,-1.058363,-8.031643,0.547476,-9.485297,-1.517584,-2.373131,5.601494,6.713594,-2.470171,-2.427669,-1.482694,8.324999,-5.256202,8.810263,7.211311,1.333032,4.818992,5.419770,-8.293008,2.949370,1.668017,4.774931,2.517899,4.170373,1.573128,-9.874292,-4.107586,1.517427,4.250918,6.083707,-7.851462,-2.565187,-2.230678,-6.286931,-9.053893,-6.736597,5.821309,-3.852466,-6.461191,-2.068138,0.140320,8.493904,-0.556615,9.802906,0.899408,-2.428470,5.809850,-3.160925,8.486653,-6.771278,-8.752374,8.727273,-0.279333,-9.540210,2.177172,-6.811785,3.894519,-8.012321,3.606405,1.664497,-5.735689,-3.360819,4.885199,-9.944086,1.920191,-6.546793,3.845845,4.008781,1.856072,-3.319961,-8.232180,2.564732,-7.088443,5.293383,8.516358,-7.720072,-8.480726,1.250276,3.679070,-5.428219,-6.634169,9.031835,-5.274191,-7.963358,-3.105083,-2.555497,5.884654,0.435482,-6.332369,8.671722,7.604000,7.260200,-0.413526,5.279236,-7.851684,-4.264337,-5.555801,-3.157268,-7.150226,-6.021841,3.419298,6.508785,1.971691,-8.866831,5.877760,7.210239,-0.803671,8.982327,-4.090822,-6.758362,-3.508714,5.170894,-5.586495,-7.438174,-6.066985,-1.354362,3.042483,2.000478,-6.100643,-5.238097,0.209417,-5.497170,4.731835,0.885187,1.898357,-9.064872,-0.020271,-1.603927,-3.348956,-7.625164,-1.689069,-9.649468,-9.627982,-0.708285,-8.023119,9.964054,-2.653393,9.493313,2.578326,6.156950,-7.325490,-1.501607,-4.489400,-5.891728,5.810358,8.457101,2.046012,-2.831247,0.035822,-3.658364,5.514461,-8.674723,2.164000,2.734396,-3.579167,7.933673,7.875722,8.626250,9.514655,-6.922841,-2.396956,-0.984158,2.215854,-8.521401,6.995956,-6.701584,-8.656685,-6.479732,-6.523087,-3.649034,7.338351,-2.303992,9.853581,-3.767438,1.329996,-4.309189,-2.929225,0.837120,9.528548,9.398738], dtype = "float32")#candidate|7401|(462,)|const|float32
call_7400 = relay.TupleGetItem(func_3139_call(relay.reshape(const_7401.astype('float32'), [3, 14, 11])), 0)
call_7402 = relay.TupleGetItem(func_3142_call(relay.reshape(const_7401.astype('float32'), [3, 14, 11])), 0)
bop_7405 = relay.multiply(uop_7397.astype('uint32'), relay.reshape(uop_7389.astype('uint32'), relay.shape_of(uop_7397))) # shape=(8, 36)
bop_7408 = relay.multiply(uop_7399.astype('uint32'), relay.reshape(uop_7391.astype('uint32'), relay.shape_of(uop_7399))) # shape=(8, 36)
func_2426_call = mod.get_global_var('func_2426')
func_2430_call = mutated_mod.get_global_var('func_2430')
var_7432 = relay.var("var_7432", dtype = "int64", shape = (2, 120))#candidate|7432|(2, 120)|var|int64
var_7433 = relay.var("var_7433", dtype = "float32", shape = (400, 2))#candidate|7433|(400, 2)|var|float32
call_7431 = relay.TupleGetItem(func_2426_call(relay.reshape(var_7432.astype('int64'), [240,]), relay.reshape(var_7433.astype('float32'), [8, 100]), ), 5)
call_7434 = relay.TupleGetItem(func_2430_call(relay.reshape(var_7432.astype('int64'), [240,]), relay.reshape(var_7433.astype('float32'), [8, 100]), ), 5)
const_7435 = relay.const([[-0.309727,7.203113,-4.701573,-9.626879,-4.491001,9.399056,3.341374,4.247129,-4.652905,3.208118,6.880436,3.394615,5.772685,0.713775,-1.600826,-9.584604,4.672893,-5.715822,2.230709,-1.357950,7.370959,-4.021934,2.722734,8.893867,0.281139,8.085895,3.350015,-6.216579,-2.020325,-5.835068,-1.364793,2.840976,1.854464,9.331209,-2.807951,-6.114127],[1.490344,1.080347,-7.849667,-9.954919,1.095184,-6.395135,-5.373479,5.356853,-8.459102,8.228470,-5.319321,7.919377,5.311471,-3.977098,-0.036965,0.650498,3.733967,-3.748406,8.357222,-3.396551,1.238996,-5.912368,4.179734,-1.739821,8.391974,-4.627153,8.937867,1.352523,-0.526872,-3.893184,8.946633,-1.091212,-4.260806,-4.833451,-9.001125,-5.231519],[-5.326195,1.239952,1.758094,2.383596,-4.675693,-4.869694,5.613796,-2.959080,-5.456270,2.643575,-2.267085,-4.924782,-4.008820,9.620137,4.019368,-0.390332,-1.987684,5.172129,-4.412322,-7.499644,-2.356013,-2.189985,8.119338,1.033450,8.949786,1.701508,6.302915,7.752609,-7.111520,-2.970176,-0.433243,4.522529,-5.416597,-5.651942,-4.540059,6.980826],[-6.345350,-4.160942,-5.282440,7.019232,-9.060475,-8.083784,-8.063132,-3.353671,-3.752495,9.577302,0.336463,6.168096,4.713233,-1.697033,-5.149868,0.704549,6.653120,-4.934158,6.020384,-8.516128,-8.202641,4.949091,-7.401737,-0.396140,-6.953190,7.145661,-6.676417,-4.762724,7.677222,1.628173,-8.324322,-9.799374,9.791277,-2.943844,-4.384715,-0.596429],[8.872101,4.703683,5.369815,-4.596206,6.526436,-1.604341,-1.782487,-5.905526,6.549513,9.836577,-8.171773,-2.029028,4.722274,-4.862182,1.396590,-8.608702,8.732921,-0.531981,3.282106,-7.687801,-0.099788,8.132510,0.269780,-2.936757,2.931772,4.932217,6.179257,6.911176,-5.458046,-9.480618,2.705487,-4.177271,1.612740,5.156753,2.964982,0.348260],[-4.920869,-1.420402,-7.303923,4.172485,-0.338725,9.362070,-7.101223,-7.621901,3.224834,-2.890889,-3.707329,7.783092,0.217201,-2.026299,-8.089827,-2.866221,-0.511331,4.594022,-7.156573,4.682285,2.154678,-8.850601,2.160660,-4.996042,-8.345819,2.308038,2.343825,-0.457749,-1.692530,7.888926,-6.125231,1.952193,-0.003318,-9.180467,8.703664,8.404677],[-8.903786,-7.244514,1.234876,-1.690939,6.025672,-2.311386,-1.035271,4.715183,2.639002,-5.359299,0.427174,8.290159,-0.071929,-1.378131,6.625764,-8.055047,2.474695,2.992312,7.550684,-5.778284,-3.081630,0.798048,5.766190,5.549455,9.642481,3.945764,7.548654,-3.101861,-7.426496,-3.908705,-5.987169,4.547902,2.155762,-7.409315,6.212860,-8.350505],[4.274834,-7.068568,-6.233229,-5.497255,8.921914,-0.570042,-5.452603,-7.591642,3.715452,-5.135458,4.683657,-2.611148,-7.125454,9.841053,6.608793,8.048185,6.623724,-0.525394,8.815135,1.976754,-1.241576,-6.844579,-1.386586,6.985362,0.912673,-6.206443,7.486426,8.706629,3.331300,8.505659,-3.398778,-2.555067,6.502458,-1.647603,5.361641,1.601524]], dtype = "float64")#candidate|7435|(8, 36)|const|float64
bop_7436 = relay.logical_and(uop_7389.astype('bool'), relay.reshape(const_7435.astype('bool'), relay.shape_of(uop_7389))) # shape=(8, 36)
bop_7439 = relay.logical_and(uop_7391.astype('bool'), relay.reshape(const_7435.astype('bool'), relay.shape_of(uop_7391))) # shape=(8, 36)
uop_7447 = relay.log(bop_7405.astype('float64')) # shape=(8, 36)
uop_7449 = relay.log(bop_7408.astype('float64')) # shape=(8, 36)
bop_7455 = relay.floor_divide(bop_7405.astype('float32'), relay.reshape(bop_7436.astype('float32'), relay.shape_of(bop_7405))) # shape=(8, 36)
bop_7458 = relay.floor_divide(bop_7408.astype('float32'), relay.reshape(bop_7439.astype('float32'), relay.shape_of(bop_7408))) # shape=(8, 36)
uop_7459 = relay.sqrt(uop_7447.astype('float64')) # shape=(8, 36)
uop_7461 = relay.sqrt(uop_7449.astype('float64')) # shape=(8, 36)
func_2089_call = mod.get_global_var('func_2089')
func_2091_call = mutated_mod.get_global_var('func_2091')
call_7462 = relay.TupleGetItem(func_2089_call(), 0)
call_7463 = relay.TupleGetItem(func_2091_call(), 0)
func_2281_call = mod.get_global_var('func_2281')
func_2283_call = mutated_mod.get_global_var('func_2283')
call_7475 = func_2281_call()
call_7476 = func_2281_call()
output = relay.Tuple([call_7357,const_7385,var_7386,call_7400,const_7401,call_7431,var_7432,var_7433,bop_7455,uop_7459,call_7462,call_7475,])
output2 = relay.Tuple([call_7358,const_7385,var_7386,call_7402,const_7401,call_7434,var_7432,var_7433,bop_7458,uop_7461,call_7463,call_7476,])
func_7485 = relay.Function([var_7386,var_7432,var_7433,], output)
mod['func_7485'] = func_7485
mod = relay.transform.InferType()(mod)
var_7486 = relay.var("var_7486", dtype = "float32", shape = (288,))#candidate|7486|(288,)|var|float32
var_7487 = relay.var("var_7487", dtype = "int64", shape = (2, 120))#candidate|7487|(2, 120)|var|int64
var_7488 = relay.var("var_7488", dtype = "float32", shape = (400, 2))#candidate|7488|(400, 2)|var|float32
output = func_7485(var_7486,var_7487,var_7488,)
func_7489 = relay.Function([var_7486,var_7487,var_7488,], output)
mutated_mod['func_7489'] = func_7489
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6919_call = mod.get_global_var('func_6919')
func_6921_call = mutated_mod.get_global_var('func_6921')
call_7517 = relay.TupleGetItem(func_6919_call(), 0)
call_7518 = relay.TupleGetItem(func_6921_call(), 0)
func_5182_call = mod.get_global_var('func_5182')
func_5184_call = mutated_mod.get_global_var('func_5184')
call_7519 = relay.TupleGetItem(func_5182_call(), 0)
call_7520 = relay.TupleGetItem(func_5184_call(), 0)
output = relay.Tuple([call_7517,call_7519,])
output2 = relay.Tuple([call_7518,call_7520,])
func_7523 = relay.Function([], output)
mod['func_7523'] = func_7523
mod = relay.transform.InferType()(mod)
mutated_mod['func_7523'] = func_7523
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mutated_mod.get_global_var('func_7523')
call_7524 = func_7523_call()
output = call_7524
func_7525 = relay.Function([], output)
mutated_mod['func_7525'] = func_7525
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7280_call = mod.get_global_var('func_7280')
func_7282_call = mutated_mod.get_global_var('func_7282')
call_7683 = relay.TupleGetItem(func_7280_call(), 1)
call_7684 = relay.TupleGetItem(func_7282_call(), 1)
output = relay.Tuple([call_7683,])
output2 = relay.Tuple([call_7684,])
func_7732 = relay.Function([], output)
mod['func_7732'] = func_7732
mod = relay.transform.InferType()(mod)
output = func_7732()
func_7733 = relay.Function([], output)
mutated_mod['func_7733'] = func_7733
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4151_call = mod.get_global_var('func_4151')
func_4152_call = mutated_mod.get_global_var('func_4152')
call_7736 = relay.TupleGetItem(func_4151_call(), 0)
call_7737 = relay.TupleGetItem(func_4152_call(), 0)
func_2564_call = mod.get_global_var('func_2564')
func_2566_call = mutated_mod.get_global_var('func_2566')
call_7741 = relay.TupleGetItem(func_2564_call(), 0)
call_7742 = relay.TupleGetItem(func_2566_call(), 0)
output = relay.Tuple([call_7736,call_7741,])
output2 = relay.Tuple([call_7737,call_7742,])
func_7743 = relay.Function([], output)
mod['func_7743'] = func_7743
mod = relay.transform.InferType()(mod)
mutated_mod['func_7743'] = func_7743
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7743_call = mutated_mod.get_global_var('func_7743')
call_7744 = func_7743_call()
output = call_7744
func_7745 = relay.Function([], output)
mutated_mod['func_7745'] = func_7745
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6594_call = mod.get_global_var('func_6594')
func_6595_call = mutated_mod.get_global_var('func_6595')
call_7758 = func_6594_call()
call_7759 = func_6594_call()
output = relay.Tuple([call_7758,])
output2 = relay.Tuple([call_7759,])
func_7765 = relay.Function([], output)
mod['func_7765'] = func_7765
mod = relay.transform.InferType()(mod)
output = func_7765()
func_7766 = relay.Function([], output)
mutated_mod['func_7766'] = func_7766
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6919_call = mod.get_global_var('func_6919')
func_6921_call = mutated_mod.get_global_var('func_6921')
call_7813 = relay.TupleGetItem(func_6919_call(), 0)
call_7814 = relay.TupleGetItem(func_6921_call(), 0)
output = call_7813
output2 = call_7814
func_7821 = relay.Function([], output)
mod['func_7821'] = func_7821
mod = relay.transform.InferType()(mod)
output = func_7821()
func_7822 = relay.Function([], output)
mutated_mod['func_7822'] = func_7822
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7523_call = mod.get_global_var('func_7523')
func_7525_call = mutated_mod.get_global_var('func_7525')
call_7835 = relay.TupleGetItem(func_7523_call(), 0)
call_7836 = relay.TupleGetItem(func_7525_call(), 0)
output = relay.Tuple([call_7835,])
output2 = relay.Tuple([call_7836,])
func_7837 = relay.Function([], output)
mod['func_7837'] = func_7837
mod = relay.transform.InferType()(mod)
output = func_7837()
func_7838 = relay.Function([], output)
mutated_mod['func_7838'] = func_7838
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4485_call = mod.get_global_var('func_4485')
func_4486_call = mutated_mod.get_global_var('func_4486')
call_7842 = relay.TupleGetItem(func_4485_call(), 0)
call_7843 = relay.TupleGetItem(func_4486_call(), 0)
output = relay.Tuple([call_7842,])
output2 = relay.Tuple([call_7843,])
func_7865 = relay.Function([], output)
mod['func_7865'] = func_7865
mod = relay.transform.InferType()(mod)
output = func_7865()
func_7866 = relay.Function([], output)
mutated_mod['func_7866'] = func_7866
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4485_call = mod.get_global_var('func_4485')
func_4486_call = mutated_mod.get_global_var('func_4486')
call_7872 = relay.TupleGetItem(func_4485_call(), 0)
call_7873 = relay.TupleGetItem(func_4486_call(), 0)
output = relay.Tuple([call_7872,])
output2 = relay.Tuple([call_7873,])
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
func_5219_call = mod.get_global_var('func_5219')
func_5220_call = mutated_mod.get_global_var('func_5220')
call_7889 = relay.TupleGetItem(func_5219_call(), 0)
call_7890 = relay.TupleGetItem(func_5220_call(), 0)
output = relay.Tuple([call_7889,])
output2 = relay.Tuple([call_7890,])
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
func_5055_call = mod.get_global_var('func_5055')
func_5056_call = mutated_mod.get_global_var('func_5056')
call_7958 = relay.TupleGetItem(func_5055_call(), 0)
call_7959 = relay.TupleGetItem(func_5056_call(), 0)
func_3709_call = mod.get_global_var('func_3709')
func_3712_call = mutated_mod.get_global_var('func_3712')
var_7969 = relay.var("var_7969", dtype = "int16", shape = (392,))#candidate|7969|(392,)|var|int16
call_7968 = relay.TupleGetItem(func_3709_call(relay.reshape(var_7969.astype('int16'), [14, 2, 14])), 5)
call_7970 = relay.TupleGetItem(func_3712_call(relay.reshape(var_7969.astype('int16'), [14, 2, 14])), 5)
func_870_call = mod.get_global_var('func_870')
func_872_call = mutated_mod.get_global_var('func_872')
const_7979 = relay.const([5.724422,-7.578711,-5.554992,6.103967,0.470720,7.097043,9.716804,-6.299226,-6.524415,2.017961,-7.903718,6.677474,-1.817315,2.508370,-2.981801,-2.328257,-5.244649,9.874374,5.548591,3.868112,-8.431885,9.780697,1.599345,-8.905885,-8.062914,2.359215,9.412870,-7.485858,6.082713,0.662264,0.205914,1.186653,-6.828833,-1.868389,2.075630,5.273676,-8.440162,7.182620,-9.858205,-2.023299,-1.589491,5.832947,-8.471816,6.313074,2.832561,4.404056,-0.928032,8.673049,-0.501335,-1.509307,9.533685,1.668298,-9.389323,5.778591,4.949680,4.465298,4.883329,6.998703,-8.387930,9.654423,1.036220,4.770707,-8.028374,-5.745235,-7.219104,-1.006826,-9.546876,-7.155927,6.098194,-0.456903,2.713057,-0.667706,-2.213500,-5.584342,-7.834473,2.502477,-0.578036,4.189115,8.771627,6.020070,-2.488342,8.242261,-9.361001,8.267432,9.441199,-7.613674,-9.912259,1.131379,-4.166649,2.734105,-4.832590,-1.431071,1.384946,1.690978,5.302127,5.535444,-9.517246,9.333240,-9.262027,-8.716520,-0.617458,-2.859743,3.313935,6.124542,4.412045,-7.210037,9.354976,-0.936624,-4.589750,2.364476,2.215206,1.230430,8.049005,-4.673100,-4.543653,2.517242,7.232759,4.400039,-3.571506,-6.673368,8.188610,7.400537,7.195381,-2.302663,1.181176,2.925201,-4.599778,-9.438779,0.752399,9.928552,-6.821734,-4.184994,-1.789751,-3.231260,6.198592,-7.079004,-4.235803,8.872393,6.214879,1.271521,-0.038478,6.168552,-5.388003,-0.930878,-3.467748,8.034012,6.829761,-9.235468,5.482249,-7.786293,0.781881,5.530463,-2.167909,7.885923,-8.098235,-2.489560,-6.716516,5.147661,2.045182,-2.986020,1.883133,-2.825689,-2.820099,-5.892648,-2.514448,-6.457664,9.721454,7.434491,-9.762909,-7.082720,3.219648,5.122855,-4.227657,-2.004841,5.617540,-3.209755,-3.194413,7.173208,7.520111,-6.887289,-0.913570,-6.872574,1.763456,9.537917,-9.885275,-6.204558,-5.968007,7.704678,4.099074,-4.222812,2.672928,3.363118,-3.237031,-0.339730,9.164136,0.397666,6.540464,5.381686,2.458248,-0.460206,-3.439934,6.567802,6.957219,-3.874543,2.060319,5.366306,8.487044,-4.055785,1.777776,6.525995,-0.122048,-7.660306,-2.093497,-9.095874,-1.694103,-3.595961,3.010329,4.403566,-3.531845,9.518706,-0.367597,-9.450144,-0.448023,2.519095,9.054330,-2.793211,8.060082,5.962241,-6.578528,4.672028,8.261427,-4.027763,-7.732436,9.334142,7.333473,-8.242063,9.085602,0.700979,2.008054,8.444776,4.237441,-6.389803,-7.618780,3.844946,5.882853,8.293352,-2.045032,-1.105513,3.092378,7.302612,-7.480972,-1.136062,9.553760,3.738360,1.868342,7.741707,-1.096262,9.985013,-4.755369,-1.450269,-5.339407,-2.250245,1.387491,5.605543,-8.728382,1.726131,-6.444221,-5.953957,7.662721,-1.445043,-4.631935,9.544846,-5.908902,7.218000,2.211116,-8.072136,5.683468,-4.212973,7.122665,1.702106,8.721074,5.875058,-3.165399,1.275193,9.253779,-1.082295,6.949357,6.900074], dtype = "float32")#candidate|7979|(288,)|const|float32
call_7978 = relay.TupleGetItem(func_870_call(relay.reshape(const_7979.astype('float32'), [12, 12, 2])), 2)
call_7980 = relay.TupleGetItem(func_872_call(relay.reshape(const_7979.astype('float32'), [12, 12, 2])), 2)
func_4297_call = mod.get_global_var('func_4297')
func_4299_call = mutated_mod.get_global_var('func_4299')
call_7981 = relay.TupleGetItem(func_4297_call(relay.reshape(const_7979.astype('float32'), [288,])), 5)
call_7982 = relay.TupleGetItem(func_4299_call(relay.reshape(const_7979.astype('float32'), [288,])), 5)
func_1931_call = mod.get_global_var('func_1931')
func_1934_call = mutated_mod.get_global_var('func_1934')
var_7990 = relay.var("var_7990", dtype = "int64", shape = (240,))#candidate|7990|(240,)|var|int64
call_7989 = relay.TupleGetItem(func_1931_call(relay.reshape(var_7990.astype('int64'), [6, 8, 5])), 0)
call_7991 = relay.TupleGetItem(func_1934_call(relay.reshape(var_7990.astype('int64'), [6, 8, 5])), 0)
output = relay.Tuple([call_7958,call_7968,var_7969,call_7978,const_7979,call_7981,call_7989,var_7990,])
output2 = relay.Tuple([call_7959,call_7970,var_7969,call_7980,const_7979,call_7982,call_7991,var_7990,])
func_8010 = relay.Function([var_7969,var_7990,], output)
mod['func_8010'] = func_8010
mod = relay.transform.InferType()(mod)
mutated_mod['func_8010'] = func_8010
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8010_call = mutated_mod.get_global_var('func_8010')
var_8012 = relay.var("var_8012", dtype = "int16", shape = (392,))#candidate|8012|(392,)|var|int16
var_8013 = relay.var("var_8013", dtype = "int64", shape = (240,))#candidate|8013|(240,)|var|int64
call_8011 = func_8010_call(var_8012,var_8013,)
output = call_8011
func_8014 = relay.Function([var_8012,var_8013,], output)
mutated_mod['func_8014'] = func_8014
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7280_call = mod.get_global_var('func_7280')
func_7282_call = mutated_mod.get_global_var('func_7282')
call_8055 = relay.TupleGetItem(func_7280_call(), 1)
call_8056 = relay.TupleGetItem(func_7282_call(), 1)
output = call_8055
output2 = call_8056
func_8060 = relay.Function([], output)
mod['func_8060'] = func_8060
mod = relay.transform.InferType()(mod)
output = func_8060()
func_8061 = relay.Function([], output)
mutated_mod['func_8061'] = func_8061
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7280_call = mod.get_global_var('func_7280')
func_7282_call = mutated_mod.get_global_var('func_7282')
call_8098 = relay.TupleGetItem(func_7280_call(), 0)
call_8099 = relay.TupleGetItem(func_7282_call(), 0)
output = relay.Tuple([call_8098,])
output2 = relay.Tuple([call_8099,])
func_8116 = relay.Function([], output)
mod['func_8116'] = func_8116
mod = relay.transform.InferType()(mod)
mutated_mod['func_8116'] = func_8116
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8116_call = mutated_mod.get_global_var('func_8116')
call_8117 = func_8116_call()
output = call_8117
func_8118 = relay.Function([], output)
mutated_mod['func_8118'] = func_8118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7732_call = mod.get_global_var('func_7732')
func_7733_call = mutated_mod.get_global_var('func_7733')
call_8142 = relay.TupleGetItem(func_7732_call(), 0)
call_8143 = relay.TupleGetItem(func_7733_call(), 0)
output = relay.Tuple([call_8142,])
output2 = relay.Tuple([call_8143,])
func_8145 = relay.Function([], output)
mod['func_8145'] = func_8145
mod = relay.transform.InferType()(mod)
mutated_mod['func_8145'] = func_8145
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8145_call = mutated_mod.get_global_var('func_8145')
call_8146 = func_8145_call()
output = call_8146
func_8147 = relay.Function([], output)
mutated_mod['func_8147'] = func_8147
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5733_call = mod.get_global_var('func_5733')
func_5735_call = mutated_mod.get_global_var('func_5735')
call_8276 = func_5733_call()
call_8277 = func_5733_call()
output = relay.Tuple([call_8276,])
output2 = relay.Tuple([call_8277,])
func_8285 = relay.Function([], output)
mod['func_8285'] = func_8285
mod = relay.transform.InferType()(mod)
mutated_mod['func_8285'] = func_8285
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8285_call = mutated_mod.get_global_var('func_8285')
call_8286 = func_8285_call()
output = call_8286
func_8287 = relay.Function([], output)
mutated_mod['func_8287'] = func_8287
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7765_call = mod.get_global_var('func_7765')
func_7766_call = mutated_mod.get_global_var('func_7766')
call_8303 = relay.TupleGetItem(func_7765_call(), 0)
call_8304 = relay.TupleGetItem(func_7766_call(), 0)
output = relay.Tuple([call_8303,])
output2 = relay.Tuple([call_8304,])
func_8326 = relay.Function([], output)
mod['func_8326'] = func_8326
mod = relay.transform.InferType()(mod)
mutated_mod['func_8326'] = func_8326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8326_call = mutated_mod.get_global_var('func_8326')
call_8327 = func_8326_call()
output = call_8327
func_8328 = relay.Function([], output)
mutated_mod['func_8328'] = func_8328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7865_call = mod.get_global_var('func_7865')
func_7866_call = mutated_mod.get_global_var('func_7866')
call_8338 = relay.TupleGetItem(func_7865_call(), 0)
call_8339 = relay.TupleGetItem(func_7866_call(), 0)
func_4151_call = mod.get_global_var('func_4151')
func_4152_call = mutated_mod.get_global_var('func_4152')
call_8406 = relay.TupleGetItem(func_4151_call(), 0)
call_8407 = relay.TupleGetItem(func_4152_call(), 0)
func_4952_call = mod.get_global_var('func_4952')
func_4955_call = mutated_mod.get_global_var('func_4955')
const_8410 = relay.const([-3,9,-2,-8,8,-1,-2,4,-8,-6,3,-7,-2,-5,9,-4,-10,-6,9,7,6,6,8,9,7,9,3,-5,7,2,9,-8,-8,1,2,7,-6,6,-2,-2,-10,-9,8,-6,5,1,-5,-2,5,2,-1,-5,-3,3,-6,2,-7,-9,-6,-2,-4,-4,-3,-3,2,-6,-6,2,-2,5,-1,3,10,4,8,7,-8,2,9,-10,1,-8,8,8,-6,-7,-10,4,4,-5,4,4,-3,3,-10,-7,-8,-9,4,6,10,6,8,9,-7,-4,-6,-5,3,-3,9,-7], dtype = "int64")#candidate|8410|(112,)|const|int64
var_8411 = relay.var("var_8411", dtype = "int64", shape = (1008,))#candidate|8411|(1008,)|var|int64
call_8409 = func_4952_call(relay.reshape(const_8410.astype('int64'), [1, 16, 7]), relay.reshape(var_8411.astype('int64'), [9, 16, 7]), )
call_8412 = func_4952_call(relay.reshape(const_8410.astype('int64'), [1, 16, 7]), relay.reshape(var_8411.astype('int64'), [9, 16, 7]), )
output = relay.Tuple([call_8338,call_8406,call_8409,const_8410,var_8411,])
output2 = relay.Tuple([call_8339,call_8407,call_8412,const_8410,var_8411,])
func_8422 = relay.Function([var_8411,], output)
mod['func_8422'] = func_8422
mod = relay.transform.InferType()(mod)
var_8423 = relay.var("var_8423", dtype = "int64", shape = (1008,))#candidate|8423|(1008,)|var|int64
output = func_8422(var_8423)
func_8424 = relay.Function([var_8423], output)
mutated_mod['func_8424'] = func_8424
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8437 = relay.var("var_8437", dtype = "float64", shape = (11, 13, 15))#candidate|8437|(11, 13, 15)|var|float64
var_8438 = relay.var("var_8438", dtype = "float64", shape = (11, 13, 15))#candidate|8438|(11, 13, 15)|var|float64
bop_8439 = relay.divide(var_8437.astype('float64'), relay.reshape(var_8438.astype('float64'), relay.shape_of(var_8437))) # shape=(11, 13, 15)
func_3501_call = mod.get_global_var('func_3501')
func_3502_call = mutated_mod.get_global_var('func_3502')
call_8445 = relay.TupleGetItem(func_3501_call(), 3)
call_8446 = relay.TupleGetItem(func_3502_call(), 3)
output = relay.Tuple([bop_8439,call_8445,])
output2 = relay.Tuple([bop_8439,call_8446,])
func_8453 = relay.Function([var_8437,var_8438,], output)
mod['func_8453'] = func_8453
mod = relay.transform.InferType()(mod)
var_8454 = relay.var("var_8454", dtype = "float64", shape = (11, 13, 15))#candidate|8454|(11, 13, 15)|var|float64
var_8455 = relay.var("var_8455", dtype = "float64", shape = (11, 13, 15))#candidate|8455|(11, 13, 15)|var|float64
output = func_8453(var_8454,var_8455,)
func_8456 = relay.Function([var_8454,var_8455,], output)
mutated_mod['func_8456'] = func_8456
mutated_mod = relay.transform.InferType()(mutated_mod)
var_8486 = relay.var("var_8486", dtype = "float32", shape = (6, 6, 12))#candidate|8486|(6, 6, 12)|var|float32
const_8487 = relay.const([[[2.020651,-9.940054,-9.247439,6.648877,0.574981,7.711685,4.307755,-8.126213,3.744049,-3.232609,7.124831,0.467586],[3.290393,4.753253,9.383004,5.848028,3.220223,6.144375,-3.964296,4.467313,8.092302,9.832745,-9.273623,8.774690],[-5.711892,-6.724272,0.414673,6.784824,4.600090,-9.644504,-6.592113,-4.935207,6.126524,8.104022,-3.920523,-5.363558],[3.857823,-8.309327,1.023570,-0.459696,2.972744,1.045570,-4.613523,-6.816068,-5.507197,-3.114432,-1.637108,-9.349221],[3.090785,-5.315458,-5.538890,9.689547,-7.830210,-9.812809,3.536723,1.930822,4.918036,1.796777,2.065438,4.304801],[9.655045,-9.542227,-3.506850,5.589347,-9.227462,5.315451,-3.511742,8.844402,6.031563,0.050288,-7.261820,4.189241]],[[5.863961,0.098852,-2.596391,-7.029368,8.414053,-8.873039,-9.257342,7.354872,1.437504,7.490212,7.350449,-0.349810],[-1.702222,2.828144,-7.936576,-4.051715,-6.591683,-2.798851,0.846520,-3.509338,-8.518333,-4.556773,-1.522766,5.024645],[7.292886,-8.992498,3.283390,1.742816,-7.896527,-5.347760,5.033470,-5.052044,2.132854,5.274123,-6.256542,0.521433],[-4.452671,1.021840,7.987968,-4.865208,6.078317,0.457435,0.289110,3.458326,0.241241,-2.940675,-9.329580,-2.043969],[2.556496,-2.780143,7.606193,-7.174736,-3.613384,9.320814,9.115431,-8.869584,-0.549302,5.872150,-5.748443,8.392702],[9.679684,-8.459764,-5.587031,0.495157,-7.690525,7.464743,7.475753,6.649772,5.850055,4.524724,-8.252058,-8.510755]],[[6.228769,-1.275463,-0.347914,1.060662,0.565599,9.995891,3.627692,-4.868030,3.952238,5.203767,7.848092,-7.112328],[5.858930,9.746550,6.927920,-4.094799,-2.574233,-8.704094,-3.420516,-1.516058,1.038838,-4.907194,-6.730955,4.287371],[-4.584549,-7.552678,4.646152,2.436268,-4.167492,9.558289,-7.405947,-1.707862,-9.997030,1.848424,-1.354330,4.579903],[3.883326,-7.665272,-6.496849,0.124041,0.842011,-3.605674,-3.568898,9.781140,9.331162,-0.981506,8.716126,-2.791455],[8.887835,-9.125436,9.173417,-0.047604,6.472105,-0.035881,-9.047691,5.486925,9.030553,-0.187248,7.217146,-5.620889],[-4.583516,-2.137834,7.431320,-4.460348,-9.356812,-9.372255,-8.842494,-1.085857,-2.406211,7.417964,2.422621,-7.092702]],[[-3.501496,-3.661419,-6.829571,-9.703051,-8.306963,-2.522189,3.464784,-7.735386,-9.281111,6.980845,7.105224,-0.338258],[-1.137448,-2.043542,-8.711902,-8.968633,-4.037021,-3.043914,5.266640,6.147072,4.917569,2.179890,-9.076264,-2.244166],[2.693316,0.814224,-7.193956,-8.865026,5.882026,-1.785387,5.005379,3.910675,0.568337,-2.671397,-8.690545,-6.773516],[-8.018114,5.408923,-6.395248,8.478402,6.107087,-6.558699,-9.694886,7.420787,-6.454632,-0.462423,-5.415885,9.635037],[0.334037,1.298876,5.178287,-2.311980,4.209302,1.365020,7.861381,5.829404,3.234141,-8.564018,-6.832025,-7.138999],[1.839217,-7.594592,-5.918730,-5.660066,-3.928621,3.072389,0.343345,5.176979,9.535838,-4.305932,0.156237,-3.660872]],[[-3.310223,-8.528574,-3.289730,4.703687,7.392673,7.604333,6.221894,-7.159274,4.352928,1.262050,3.865165,-2.103336],[7.159196,6.847305,-6.825126,-1.703863,9.144265,-7.255770,8.614428,0.393427,4.766794,-1.034754,-3.403819,-1.027141],[-4.360121,7.323888,-2.392581,5.310229,-7.652510,-5.614935,-6.736386,3.610853,-3.803525,4.093811,5.858300,-1.414480],[0.537405,0.598438,2.165000,-9.016839,-4.179012,8.254961,7.198291,-0.276275,-8.264282,-6.540897,1.174714,-8.241602],[2.196300,2.788386,-5.620804,-6.400929,-8.472168,-6.162183,7.756787,-4.519170,-3.030468,4.503732,-6.918668,9.241315],[-0.645397,7.470150,-9.088075,1.999129,7.617555,-5.500496,3.342190,8.252618,7.489227,5.804437,-3.397675,-5.571470]],[[-3.641362,-4.833577,7.189119,4.372447,-5.154123,-6.405495,-0.548927,-6.444748,-5.708106,6.668198,3.719516,-3.699212],[-6.551648,-3.108724,1.436617,4.137747,-6.391852,-8.003961,-5.162396,4.446442,-2.635581,3.919701,-2.004915,-0.624157],[-0.578663,-2.737871,-0.519927,-0.146439,-7.683283,-1.025467,3.399944,0.077124,9.940296,-1.456702,1.605553,-0.355595],[5.222727,-0.266084,-2.614600,-6.656999,7.427762,-4.753901,9.837805,-1.468334,4.187265,1.506421,5.935155,-4.758726],[-7.565807,-5.060506,2.391415,0.885074,-7.406174,-8.600982,-3.616595,8.543707,2.217391,-6.952026,5.122553,-4.464725],[6.146975,1.037013,7.872417,4.999278,-6.535923,1.308196,5.492136,-1.127694,0.483478,-4.511326,-0.074966,8.424905]]], dtype = "float32")#candidate|8487|(6, 6, 12)|const|float32
bop_8488 = relay.divide(var_8486.astype('float32'), relay.reshape(const_8487.astype('float32'), relay.shape_of(var_8486))) # shape=(6, 6, 12)
func_5136_call = mod.get_global_var('func_5136')
func_5137_call = mutated_mod.get_global_var('func_5137')
call_8491 = func_5136_call()
call_8492 = func_5136_call()
func_3501_call = mod.get_global_var('func_3501')
func_3502_call = mutated_mod.get_global_var('func_3502')
call_8496 = relay.TupleGetItem(func_3501_call(), 1)
call_8497 = relay.TupleGetItem(func_3502_call(), 1)
uop_8504 = relay.sinh(bop_8488.astype('float64')) # shape=(6, 6, 12)
output = relay.Tuple([call_8491,call_8496,uop_8504,])
output2 = relay.Tuple([call_8492,call_8497,uop_8504,])
F = relay.Function([var_8486,], output)
mod['main'] = F
mod = relay.transform.InferType()(mod)
print('==========mod==========')
print(mod.astext(show_meta_data=False))
print('===================================')
F = relay.Function([var_8486,], output2)
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
