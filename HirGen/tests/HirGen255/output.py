import tvm
from tvm import relay
from tvm.ir.transform import Sequential
from tvm.contrib import graph_runtime
import numpy as np
mod = tvm.IRModule()
mutated_mod = tvm.IRModule()
var_288 = relay.var("var_288", dtype = "uint8", shape = (12, 1, 14))#candidate|288|(12, 1, 14)|var|uint8
const_289 = relay.const([[[-1,6,9,6,2,7,-1,-2,-4,2,-5,-3,-5,10]],[[-4,-7,-1,-8,2,-6,-5,2,8,7,-7,5,9,-10]],[[-2,8,-1,-10,9,-3,-1,7,1,-2,-7,10,-1,-3]],[[2,-7,-6,-10,-1,9,8,10,10,7,-9,2,-9,-8]],[[-7,3,6,6,6,-9,8,-6,4,8,-3,7,4,-8]],[[2,-3,8,-2,7,-6,-8,9,-7,-2,9,4,3,-4]],[[1,-9,-1,-5,10,3,7,-8,8,-9,-10,-5,1,3]],[[-1,10,-2,-6,-1,9,-8,7,-6,8,-2,-9,8,-5]],[[1,2,6,5,-8,8,2,1,2,5,6,-1,10,3]],[[2,-6,6,7,9,10,5,-7,5,-6,9,-6,7,-3]],[[5,-7,-6,10,-1,5,-10,-7,3,1,5,7,-1,9]],[[10,4,-10,2,4,-7,2,-6,7,7,-9,-7,8,-6]]], dtype = "uint8")#candidate|289|(12, 1, 14)|const|uint8
bop_290 = relay.right_shift(var_288.astype('uint8'), relay.reshape(const_289.astype('uint8'), relay.shape_of(var_288))) # shape=(12, 1, 14)
output = relay.Tuple([bop_290,])
output2 = relay.Tuple([bop_290,])
func_295 = relay.Function([var_288,], output)
mod['func_295'] = func_295
mod = relay.transform.InferType()(mod)
mutated_mod['func_295'] = func_295
mutated_mod = relay.transform.InferType()(mutated_mod)
var_296 = relay.var("var_296", dtype = "uint8", shape = (12, 1, 14))#candidate|296|(12, 1, 14)|var|uint8
func_295_call = mutated_mod.get_global_var('func_295')
call_297 = func_295_call(var_296)
output = call_297
func_298 = relay.Function([var_296], output)
mutated_mod['func_298'] = func_298
mutated_mod = relay.transform.InferType()(mutated_mod)
var_460 = relay.var("var_460", dtype = "bool", shape = (15, 7, 5))#candidate|460|(15, 7, 5)|var|bool
var_461 = relay.var("var_461", dtype = "bool", shape = (15, 7, 5))#candidate|461|(15, 7, 5)|var|bool
bop_462 = relay.logical_or(var_460.astype('bool'), relay.reshape(var_461.astype('bool'), relay.shape_of(var_460))) # shape=(15, 7, 5)
output = bop_462
output2 = bop_462
func_465 = relay.Function([var_460,var_461,], output)
mod['func_465'] = func_465
mod = relay.transform.InferType()(mod)
mutated_mod['func_465'] = func_465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_465_call = mutated_mod.get_global_var('func_465')
var_467 = relay.var("var_467", dtype = "bool", shape = (15, 7, 5))#candidate|467|(15, 7, 5)|var|bool
var_468 = relay.var("var_468", dtype = "bool", shape = (15, 7, 5))#candidate|468|(15, 7, 5)|var|bool
call_466 = func_465_call(var_467,var_468,)
output = call_466
func_469 = relay.Function([var_467,var_468,], output)
mutated_mod['func_469'] = func_469
mutated_mod = relay.transform.InferType()(mutated_mod)
const_1036 = relay.const([[[-6.148797,-0.463083,-1.354567,-7.020569,-8.247169,0.724979,-9.124551,-4.330309,5.344305,-5.793170,7.783941,6.054635,0.164633,-6.626777,-6.048987],[6.383697,0.829121,8.986551,4.211250,-9.724200,-5.541560,-4.850036,-1.835896,-5.963485,-0.629139,4.439178,-8.819665,-1.099679,-8.919870,-1.034302],[-0.508819,4.644757,5.698360,1.223754,-4.373204,-4.722098,3.054887,7.669893,-9.576417,4.561471,-5.028433,-1.914470,1.501967,1.881340,7.643499]],[[4.536540,6.935878,3.745408,0.091272,4.459469,-0.141267,-3.952105,6.005828,8.332220,-0.484248,-0.456185,-4.180028,1.338965,6.028851,6.757370],[-6.411516,-8.398669,7.595666,0.202937,-1.220229,9.310686,-0.768652,0.332767,3.405391,4.789889,2.684822,3.543662,-6.291812,-0.709534,5.518612],[-4.338700,-1.007527,8.473074,5.984221,-5.055211,2.849958,-7.724834,-7.381006,6.158455,8.143884,8.586919,3.715655,-2.024567,7.848360,9.390909]],[[-7.392433,-9.837952,0.183939,-7.324534,-2.489404,-4.238422,-9.001749,-1.545240,-9.430591,7.492752,-2.729087,5.979810,3.600663,-2.270598,-8.318901],[3.074114,8.981430,3.237175,7.994212,7.933716,-0.066697,0.859472,8.664238,4.095973,-2.460836,9.229491,7.148482,-1.420674,-9.996136,9.242028],[-8.181476,0.989347,7.942095,-5.575406,-6.715616,-4.166985,-9.084371,-6.090935,8.991067,3.368956,-4.617636,1.724221,5.733669,-3.955452,-9.851887]],[[-7.472315,-4.402901,-5.009711,-1.087459,-1.669299,2.813976,-7.560756,-5.671251,3.784917,-6.792696,0.971834,1.048680,6.123491,-2.829671,-2.028645],[7.019631,-5.059318,-0.094364,9.161778,4.492600,9.057033,1.033846,-1.927436,-9.005971,0.737031,2.342972,4.796906,5.147388,7.174501,-9.910988],[-6.100086,8.709895,0.925901,-4.556757,-2.117200,-2.116668,-9.954106,9.003283,-5.589627,-6.777146,0.154245,-8.204681,-8.978528,4.050307,-6.734115]],[[9.226539,3.373851,2.211031,-9.428577,-7.195017,4.634201,-9.731595,-4.302599,6.717257,-3.981791,-4.910180,1.431731,-3.290022,1.473405,7.739369],[-3.672581,-6.227217,7.865120,-5.947339,2.799194,1.969359,-0.702425,-1.121969,6.403024,5.778652,5.355564,6.945886,-8.024013,-0.456221,2.634656],[1.373424,-1.285454,-7.130945,0.928181,0.273602,1.148467,-8.966541,9.247900,-7.680957,-2.176478,-2.654128,8.052073,-4.275817,9.815852,3.916036]],[[-1.485107,-2.393240,4.192106,9.631001,-0.677362,2.447393,8.806857,9.240762,4.703252,5.181556,8.152984,3.547830,-0.994341,-3.548040,5.215784],[-7.213266,6.766036,-7.034576,4.977970,4.589706,5.813258,8.675046,-1.308664,6.857397,-7.200847,4.779142,-7.900512,1.649990,-0.142729,-3.903060],[0.929710,-4.170126,-8.879319,5.645635,-4.646921,0.348230,-9.646009,-9.277314,9.444511,-2.786809,-9.000955,7.854841,-9.659730,3.198814,-4.341844]],[[-8.570499,9.528465,-1.240874,-6.981626,0.448214,5.434766,-9.858632,-3.182972,-0.072166,-0.433731,0.932194,1.320245,5.466515,3.144329,-4.342215],[-7.567507,-7.665592,0.797031,4.972346,-2.046751,-2.652148,1.169997,1.069333,5.086834,8.157210,-9.987610,3.145277,2.669173,-5.071673,8.584544],[7.549614,8.052112,2.790321,-8.281420,-5.825362,-9.440719,-9.983346,0.559584,1.593515,-3.166637,-7.316592,5.835054,-0.400100,-4.235493,-6.648982]],[[8.882918,-2.678156,2.176297,-2.583173,-8.033215,-9.732830,9.624515,6.602097,4.132262,-8.260498,7.162465,-6.188654,-2.608115,-3.797379,7.786620],[-7.906052,-0.017916,-1.166532,4.634224,4.359929,6.279439,-9.073932,5.418185,-2.846134,-0.606182,-8.701731,7.680283,-5.773537,8.976563,7.487711],[1.602041,3.693959,-6.883414,3.615289,-7.635408,5.176001,9.371292,1.471041,7.760131,8.173244,-2.976431,-7.614904,-3.502250,4.030046,7.031528]],[[6.562721,-3.263764,-9.587803,-9.270281,-1.630693,-9.144925,-9.113379,3.645232,-7.142559,9.331414,-7.868824,8.211228,-6.695507,-3.450449,2.351083],[-7.342870,-7.075842,-8.893038,4.581950,5.710024,8.649965,4.931958,7.453090,8.155072,-5.364270,2.544682,-0.063400,6.876829,-0.920049,-3.466285],[5.948669,-0.380150,-5.422245,-1.284044,1.967902,4.533486,6.389460,8.935911,-2.114951,4.650019,8.308167,3.929748,3.164041,-5.363573,-7.137677]],[[-0.857242,8.290632,-1.299177,9.670385,9.068430,-9.065880,4.182796,-3.923384,-8.448838,-2.769527,7.466386,-3.970861,8.459518,2.015613,7.306283],[8.838418,1.244136,4.336715,-6.706311,-5.395695,0.744198,-1.899287,-4.295141,3.429678,7.013174,-4.515521,-2.920844,-1.283023,0.539822,6.513001],[9.435488,-1.862344,-2.300275,-8.905299,-6.157844,-6.752494,1.557020,-8.467812,6.291950,-7.400833,2.579910,1.518605,7.323495,-4.650426,7.775405]],[[-8.763988,-4.736623,9.898423,-0.497391,1.337727,-9.577009,-1.128631,-1.694212,-5.016188,0.206621,5.735944,7.398928,-4.861982,-0.751190,8.931860],[-9.017732,-3.157977,-3.407332,4.108376,-9.306289,2.593876,5.746862,-3.639070,0.254348,4.794849,-9.049198,7.485070,-0.375565,-0.305507,-3.434229],[-5.353586,6.996147,1.245408,7.676239,-0.057761,4.935567,-0.176808,-5.677977,1.157568,3.031976,-7.732732,6.556503,-4.592929,9.780933,-7.928200]],[[-5.084239,-6.941403,5.766201,-1.611050,5.349997,-9.077482,-8.343892,4.822921,-6.524737,-0.430281,4.834334,2.052974,9.115938,-4.906395,-6.031150],[-4.494789,-9.551706,7.590807,7.199353,-2.421733,-5.842419,1.015647,2.419994,5.855493,4.078937,-3.585125,-7.835142,8.004371,1.710849,-6.354028],[-6.546457,-5.216980,-3.020799,1.695698,2.712514,-4.284741,-0.096188,8.926232,-4.946758,1.783820,-9.599298,-1.901627,1.831100,-0.264251,-2.413191]],[[0.548692,-5.070929,0.371207,6.546650,-9.454791,-6.301152,-3.944512,-7.241997,-7.439441,3.596511,9.079374,1.676515,-8.797021,6.528040,3.064142],[-9.621687,9.711275,7.677380,4.498390,4.155789,3.782414,-4.707392,-8.058594,9.989503,0.257069,9.153756,2.312868,-4.466636,2.605732,-1.777510],[6.132921,4.462950,6.189340,7.024995,9.100292,-8.800653,-0.696705,1.501144,-3.739470,-4.483431,7.984728,-6.764872,-8.848431,-7.410109,-9.399965]],[[4.841312,1.807877,-3.369934,4.695821,6.353909,-3.135914,4.926149,-9.017822,-7.214464,-0.222488,-6.813202,-6.828619,-9.590651,-6.094173,-0.592679],[2.201213,-1.759103,4.658176,-0.752352,1.729524,1.402519,7.739336,-0.481477,0.364050,-8.735887,2.665359,4.113958,6.790701,3.967784,3.050443],[8.385160,2.951026,8.748763,-0.051454,7.813825,-7.895386,-8.417868,1.147434,0.269884,4.784570,-6.987931,2.902225,-1.839926,7.337734,-1.873206]]], dtype = "float32")#candidate|1036|(14, 3, 15)|const|float32
uop_1037 = relay.asin(const_1036.astype('float32')) # shape=(14, 3, 15)
output = relay.Tuple([uop_1037,])
output2 = relay.Tuple([uop_1037,])
func_1040 = relay.Function([], output)
mod['func_1040'] = func_1040
mod = relay.transform.InferType()(mod)
mutated_mod['func_1040'] = func_1040
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mutated_mod.get_global_var('func_1040')
call_1041 = func_1040_call()
output = call_1041
func_1042 = relay.Function([], output)
mutated_mod['func_1042'] = func_1042
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1047 = relay.var("var_1047", dtype = "float32", shape = (2, 10, 14))#candidate|1047|(2, 10, 14)|var|float32
uop_1048 = relay.cos(var_1047.astype('float32')) # shape=(2, 10, 14)
uop_1050 = relay.sin(var_1047.astype('float64')) # shape=(2, 10, 14)
output = relay.Tuple([uop_1048,uop_1050,])
output2 = relay.Tuple([uop_1048,uop_1050,])
func_1056 = relay.Function([var_1047,], output)
mod['func_1056'] = func_1056
mod = relay.transform.InferType()(mod)
mutated_mod['func_1056'] = func_1056
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1057 = relay.var("var_1057", dtype = "float32", shape = (2, 10, 14))#candidate|1057|(2, 10, 14)|var|float32
func_1056_call = mutated_mod.get_global_var('func_1056')
call_1058 = func_1056_call(var_1057)
output = call_1058
func_1059 = relay.Function([var_1057], output)
mutated_mod['func_1059'] = func_1059
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1079 = relay.TupleGetItem(func_1040_call(), 0)
call_1080 = relay.TupleGetItem(func_1042_call(), 0)
output = relay.Tuple([call_1079,])
output2 = relay.Tuple([call_1080,])
func_1084 = relay.Function([], output)
mod['func_1084'] = func_1084
mod = relay.transform.InferType()(mod)
mutated_mod['func_1084'] = func_1084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mutated_mod.get_global_var('func_1084')
call_1085 = func_1084_call()
output = call_1085
func_1086 = relay.Function([], output)
mutated_mod['func_1086'] = func_1086
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1106 = relay.TupleGetItem(func_1084_call(), 0)
call_1107 = relay.TupleGetItem(func_1086_call(), 0)
uop_1109 = relay.tan(call_1106.astype('float32')) # shape=(14, 3, 15)
uop_1111 = relay.tan(call_1107.astype('float32')) # shape=(14, 3, 15)
bop_1114 = relay.not_equal(uop_1109.astype('bool'), relay.reshape(call_1106.astype('bool'), relay.shape_of(uop_1109))) # shape=(14, 3, 15)
bop_1117 = relay.not_equal(uop_1111.astype('bool'), relay.reshape(call_1107.astype('bool'), relay.shape_of(uop_1111))) # shape=(14, 3, 15)
var_1119 = relay.var("var_1119", dtype = "float32", shape = (14, 3, 15))#candidate|1119|(14, 3, 15)|var|float32
bop_1120 = relay.logical_and(uop_1109.astype('bool'), relay.reshape(var_1119.astype('bool'), relay.shape_of(uop_1109))) # shape=(14, 3, 15)
bop_1123 = relay.logical_and(uop_1111.astype('bool'), relay.reshape(var_1119.astype('bool'), relay.shape_of(uop_1111))) # shape=(14, 3, 15)
const_1128 = relay.const([[[-9.327464,9.208722,3.730449,-0.768489,9.120558,-5.518801,-1.984182,8.334159,-9.250271,7.338276,-1.331456,5.745062,-4.429457,-6.177213,1.154243],[8.810508,-6.437301,-0.874283,-4.998199,-3.569592,-3.520765,6.420657,-3.044363,1.123947,1.240028,-1.865562,2.343406,2.391648,9.224957,-5.060535],[7.808179,4.339606,5.179772,0.496448,-3.686609,7.411948,0.011457,3.680250,6.890007,-8.800477,-2.941623,9.867504,-9.915208,9.876539,-2.739433]],[[-2.429871,3.683113,5.949129,5.239566,-5.310169,5.114745,-3.988748,-5.826395,-7.273511,8.350336,6.728632,0.396567,9.731249,1.917135,-7.959899],[1.684471,5.682394,-1.528607,1.395349,7.120619,9.811666,0.240403,4.167904,1.493832,-3.354287,-6.920803,-0.880651,-6.025942,8.661441,-5.517828],[0.830365,7.285348,2.130840,-7.719826,5.845360,-1.763997,-6.353775,8.095008,-7.659281,5.456463,2.995564,-1.232071,6.216875,4.993181,-8.306928]],[[-0.585284,5.210993,-0.980849,7.883295,8.314285,-9.333927,7.784730,-3.778632,4.614687,-6.559439,7.869008,-5.557510,8.469918,-4.625188,4.106999],[9.384618,-8.974888,1.830895,6.010126,9.167996,1.405506,-4.504833,-8.085255,9.081603,3.564612,-9.033097,9.649575,-8.733606,3.997420,-9.348603],[1.604702,-3.983545,-1.370809,-4.802178,2.902621,4.309201,-7.011379,5.345666,-4.865444,-9.712804,-6.169012,-1.371185,9.237733,6.129678,5.021430]],[[3.335223,2.876184,-1.451617,7.029246,4.462636,6.702740,-4.973637,-7.231502,-8.891191,-3.858466,3.832834,-4.288887,8.439850,-6.584232,-5.841770],[-4.076411,9.901223,6.351293,4.835807,-5.386604,3.021108,0.207902,5.685362,-5.751498,-8.049744,-4.929788,2.836389,5.864642,0.660961,3.607746],[0.998517,6.155398,5.886886,0.119340,-2.083952,1.350262,6.899983,2.776712,0.554733,-4.899628,-9.301370,6.505630,8.976108,-7.145846,-3.721204]],[[-7.037944,7.034853,-4.276099,1.983024,-9.505339,-0.781082,6.018199,-4.532851,-5.717836,-3.985505,-3.518355,-6.952048,4.672981,-5.331472,-6.914446],[8.071123,7.826879,-8.804353,-1.991400,2.865701,6.655410,-8.188913,6.348943,4.782059,-2.253252,-6.982854,1.756434,-8.522971,8.156367,-6.512998],[-2.557234,-4.625023,4.169525,0.395587,-4.298806,-1.359237,-0.861023,6.699935,2.919094,-0.623777,-5.188195,-3.733969,1.755707,-2.390130,-3.140590]],[[-7.198195,4.650257,-3.094991,8.099607,-6.785529,-9.011744,-5.458494,5.877254,-1.086955,-9.014074,1.582667,4.090741,-3.475130,-6.726469,1.590291],[-3.672699,8.466901,3.739429,-8.116879,-5.408988,-9.904643,9.600013,3.537632,-4.989052,6.477211,-8.802656,-9.063325,7.748873,-6.602598,8.635476],[-6.107644,2.244264,7.401202,3.878972,-2.865532,-8.026507,-5.854823,9.036033,2.621353,2.841372,-5.176859,5.221517,6.481038,-6.540597,-3.692924]],[[-9.994867,1.663561,7.717050,-8.651787,-4.449672,-1.917239,9.374788,-4.492413,-9.273971,9.699979,-4.949237,-9.602870,-4.254156,-5.065642,3.706687],[-8.634467,6.733226,-5.667221,5.863170,8.487314,9.013465,-9.438460,-8.845542,7.026778,-8.175899,-6.615571,-7.660493,-8.098378,8.543807,9.945673],[-0.326228,-9.748948,5.033715,-2.763113,3.862500,-1.405834,2.143878,3.860344,8.418640,-1.386725,8.086701,5.175238,4.765637,-5.141940,-6.133875]],[[-2.457759,-1.412331,4.027103,9.906690,-6.035538,0.561569,4.442579,3.794281,0.228389,0.286974,7.444548,-7.438861,-3.614567,-9.964233,-8.845636],[6.772910,3.037770,6.172826,6.654513,-7.013375,4.024465,0.471274,-3.079839,-5.566771,1.334263,-1.597230,-3.482404,8.413749,-6.693105,-2.702582],[2.059887,1.000026,3.548843,7.931568,6.006546,-4.756322,8.197371,4.140308,-4.178723,6.211681,4.652264,-5.962069,3.014462,5.553023,-3.821116]],[[-9.897304,5.255750,-4.125832,2.549380,0.386924,-0.928146,0.336967,3.786102,9.186501,-7.810700,-7.678786,-9.911991,-6.328646,-1.065823,-1.866799],[8.263235,-1.471931,-0.537589,6.395304,-8.585007,1.516179,-6.455593,1.139233,6.777989,2.269880,9.550986,-7.023130,5.554326,1.186518,-1.130640],[-7.078773,5.768662,-0.660570,6.794635,8.686884,-9.489629,-7.839454,2.401880,3.651541,7.715930,9.746218,-2.168317,-2.523238,-5.017111,4.141009]],[[9.130583,-0.025758,7.727459,5.099812,-0.346310,-9.117121,5.809457,8.335856,-2.733874,2.789730,0.183347,5.282128,-5.719049,4.721124,1.960322],[6.663327,-7.140496,2.917408,-6.891084,1.619912,6.973917,-0.558483,-4.141554,-5.857824,-4.467468,-3.556504,-0.257932,0.451267,-5.192634,9.345514],[9.116793,-5.717965,-8.328144,8.461122,-5.649194,2.684552,2.489026,-7.493593,1.485658,-6.449993,3.103545,6.028265,-5.665206,-3.813590,-3.861454]],[[6.000193,9.936295,2.960986,6.054255,-1.413934,1.837539,-2.611863,4.084515,3.941313,6.204421,-0.455935,-2.988380,-0.173840,-9.591667,0.569907],[-3.578962,0.315476,2.324301,1.250503,3.368130,-0.757923,1.762045,7.643367,-0.371913,4.122403,6.339422,-4.443110,1.299102,-0.062469,8.717071],[-6.395430,-8.736691,3.678039,2.206634,0.301926,1.389342,1.715901,-8.229603,1.138404,3.491073,-5.627895,9.574196,1.460945,6.932853,-2.382036]],[[6.085556,-4.990680,-6.968717,1.970443,-8.270022,7.864484,7.728578,-6.071203,3.445699,-0.374761,-5.576672,5.473854,1.753757,-8.565726,4.727604],[0.867333,-6.079902,-4.224425,-0.967470,-1.363533,-9.288347,-2.360674,-2.083321,2.202283,-2.127704,6.598748,-6.798329,-8.882940,0.574709,-2.882633],[-6.127498,8.891545,5.161155,1.919987,-5.443256,-4.787401,7.659027,-7.783781,3.181479,-6.350584,2.158068,-0.572931,-3.031693,8.441398,-7.219225]],[[-8.837060,0.616811,2.463023,-1.726606,-9.965089,-2.827934,0.683251,7.442497,2.175783,-2.854698,9.431666,3.284739,9.612455,-0.460984,7.953613],[4.201828,0.448207,-5.786683,4.374878,-9.082262,6.169873,5.076882,-5.142640,-6.650132,2.772856,4.505245,-9.102976,4.080620,6.163595,-6.601424],[-9.615040,-9.521834,-5.337018,-3.158476,1.044930,-3.494442,9.896753,-0.837340,-2.194720,7.030251,5.633625,-6.172798,-1.105894,6.232175,-4.276986]],[[-2.617418,5.950662,-0.301806,9.968116,-6.311031,0.312581,4.790442,-9.754077,2.072400,-9.311544,-6.410388,4.841094,8.364149,-8.136478,9.870640],[-3.299618,6.834211,3.613120,-8.702306,-5.801390,2.408166,9.391645,-9.922378,-7.157689,-2.861590,5.857793,-3.351671,-4.787647,-1.691046,6.184069],[1.470714,3.365574,5.284374,-2.967750,-3.725907,-8.186450,1.044759,-5.334252,9.092150,2.679373,-8.053594,7.834647,7.434258,-6.918505,-8.865680]]], dtype = "float32")#candidate|1128|(14, 3, 15)|const|float32
bop_1129 = relay.bitwise_xor(var_1119.astype('int64'), relay.reshape(const_1128.astype('int64'), relay.shape_of(var_1119))) # shape=(14, 3, 15)
output = relay.Tuple([bop_1114,bop_1120,bop_1129,])
output2 = relay.Tuple([bop_1117,bop_1123,bop_1129,])
func_1133 = relay.Function([var_1119,], output)
mod['func_1133'] = func_1133
mod = relay.transform.InferType()(mod)
var_1134 = relay.var("var_1134", dtype = "float32", shape = (14, 3, 15))#candidate|1134|(14, 3, 15)|var|float32
output = func_1133(var_1134)
func_1135 = relay.Function([var_1134], output)
mutated_mod['func_1135'] = func_1135
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1142 = relay.var("var_1142", dtype = "bool", shape = (12, 5, 5))#candidate|1142|(12, 5, 5)|var|bool
const_1143 = relay.const([[[True,False,True,False,False],[False,False,False,False,False],[True,True,False,False,True],[False,False,False,True,False],[True,True,False,True,True]],[[True,False,True,True,True],[True,False,False,True,True],[False,True,True,False,True],[False,True,False,False,True],[False,False,True,False,True]],[[False,True,False,False,False],[True,True,True,False,False],[False,False,False,False,True],[True,True,False,True,True],[False,True,True,False,True]],[[False,False,True,False,False],[True,False,True,True,False],[False,True,True,True,True],[True,True,True,True,False],[False,True,True,True,False]],[[False,True,True,True,True],[False,False,False,True,False],[False,False,False,False,False],[False,False,True,True,True],[False,False,False,False,True]],[[False,False,False,True,True],[False,False,False,True,True],[False,True,True,False,True],[True,False,True,True,False],[True,True,False,False,False]],[[True,True,False,False,True],[False,False,True,False,False],[True,True,False,True,False],[True,True,False,True,True],[True,False,False,False,False]],[[False,False,True,True,False],[False,False,True,False,False],[False,False,True,False,True],[True,True,False,True,False],[False,False,False,False,True]],[[True,True,False,True,False],[False,False,False,True,True],[False,True,True,False,False],[False,False,False,True,False],[True,False,True,True,True]],[[False,False,True,False,False],[True,True,False,True,True],[False,True,True,False,False],[False,False,False,True,False],[False,True,True,False,False]],[[True,False,False,True,True],[True,True,True,True,True],[False,False,False,False,True],[True,False,False,False,False],[False,False,False,False,False]],[[True,False,True,False,True],[False,True,True,False,False],[False,False,True,False,True],[False,False,True,True,False],[False,False,False,False,True]]], dtype = "bool")#candidate|1143|(12, 5, 5)|const|bool
bop_1144 = relay.logical_or(var_1142.astype('bool'), relay.reshape(const_1143.astype('bool'), relay.shape_of(var_1142))) # shape=(12, 5, 5)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
const_1148 = relay.const([[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[True],[True],[False],[True],[False],[False],[True],[True],[False],[False],[True],[False],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[True],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[True],[True],[True],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[True],[False],[False],[False],[False],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[False],[True],[True],[False],[False],[False],[False],[False],[True],[True],[False],[False],[False],[False],[True],[True],[False],[True],[True],[True],[False],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[True],[True],[False],[False],[True],[False],[False],[True],[True],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[False],[False],[True],[True],[False],[False],[False],[True],[True],[True],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[False],[True],[False],[False],[True],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[True],[True],[False],[True],[True],[True],[True],[False],[True],[False],[False],[True],[False],[False],[False],[False],[True],[False],[True],[False],[False],[True],[False],[False],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[True],[True],[False],[False],[False],[True],[False],[True],[True],[False],[True],[True],[True],[True],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[True],[False],[False],[True],[True],[False],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[False],[True],[False],[True],[False],[False],[False],[True],[True],[True],[False],[True],[True],[False],[True],[False],[True],[False],[True],[True],[True],[False],[False],[False],[False],[False],[False],[False],[False],[True],[False],[False],[False],[False],[True],[True],[False],[True],[False],[True],[True],[False],[True],[False],[False],[False],[False],[True],[False]], dtype = "bool")#candidate|1148|(525, 1)|const|bool
call_1147 = func_465_call(relay.reshape(const_1148.astype('bool'), [15, 7, 5]), relay.reshape(const_1148.astype('bool'), [15, 7, 5]), )
call_1149 = func_465_call(relay.reshape(const_1148.astype('bool'), [15, 7, 5]), relay.reshape(const_1148.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([bop_1144,call_1147,const_1148,])
output2 = relay.Tuple([bop_1144,call_1149,const_1148,])
func_1152 = relay.Function([var_1142,], output)
mod['func_1152'] = func_1152
mod = relay.transform.InferType()(mod)
mutated_mod['func_1152'] = func_1152
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1153 = relay.var("var_1153", dtype = "bool", shape = (12, 5, 5))#candidate|1153|(12, 5, 5)|var|bool
func_1152_call = mutated_mod.get_global_var('func_1152')
call_1154 = func_1152_call(var_1153)
output = call_1154
func_1155 = relay.Function([var_1153], output)
mutated_mod['func_1155'] = func_1155
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1174 = relay.TupleGetItem(func_1040_call(), 0)
call_1175 = relay.TupleGetItem(func_1042_call(), 0)
func_295_call = mod.get_global_var('func_295')
func_298_call = mutated_mod.get_global_var('func_298')
var_1197 = relay.var("var_1197", dtype = "uint8", shape = (168, 1))#candidate|1197|(168, 1)|var|uint8
call_1196 = relay.TupleGetItem(func_295_call(relay.reshape(var_1197.astype('uint8'), [12, 1, 14])), 0)
call_1198 = relay.TupleGetItem(func_298_call(relay.reshape(var_1197.astype('uint8'), [12, 1, 14])), 0)
uop_1203 = relay.acos(var_1197.astype('float32')) # shape=(168, 1)
uop_1225 = relay.atan(uop_1203.astype('float64')) # shape=(168, 1)
output = relay.Tuple([call_1174,call_1196,uop_1225,])
output2 = relay.Tuple([call_1175,call_1198,uop_1225,])
func_1234 = relay.Function([var_1197,], output)
mod['func_1234'] = func_1234
mod = relay.transform.InferType()(mod)
mutated_mod['func_1234'] = func_1234
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1235 = relay.var("var_1235", dtype = "uint8", shape = (168, 1))#candidate|1235|(168, 1)|var|uint8
func_1234_call = mutated_mod.get_global_var('func_1234')
call_1236 = func_1234_call(var_1235)
output = call_1236
func_1237 = relay.Function([var_1235], output)
mutated_mod['func_1237'] = func_1237
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1269 = relay.TupleGetItem(func_1040_call(), 0)
call_1270 = relay.TupleGetItem(func_1042_call(), 0)
uop_1276 = relay.cosh(call_1269.astype('float32')) # shape=(14, 3, 15)
uop_1278 = relay.cosh(call_1270.astype('float32')) # shape=(14, 3, 15)
bop_1298 = relay.greater_equal(uop_1276.astype('bool'), relay.reshape(call_1269.astype('bool'), relay.shape_of(uop_1276))) # shape=(14, 3, 15)
bop_1301 = relay.greater_equal(uop_1278.astype('bool'), relay.reshape(call_1270.astype('bool'), relay.shape_of(uop_1278))) # shape=(14, 3, 15)
var_1307 = relay.var("var_1307", dtype = "bool", shape = (14, 3, 15))#candidate|1307|(14, 3, 15)|var|bool
bop_1308 = relay.bitwise_or(bop_1298.astype('uint64'), relay.reshape(var_1307.astype('uint64'), relay.shape_of(bop_1298))) # shape=(14, 3, 15)
bop_1311 = relay.bitwise_or(bop_1301.astype('uint64'), relay.reshape(var_1307.astype('uint64'), relay.shape_of(bop_1301))) # shape=(14, 3, 15)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
var_1317 = relay.var("var_1317", dtype = "bool", shape = (525,))#candidate|1317|(525,)|var|bool
call_1316 = func_465_call(relay.reshape(var_1317.astype('bool'), [15, 7, 5]), relay.reshape(var_1317.astype('bool'), [15, 7, 5]), )
call_1318 = func_465_call(relay.reshape(var_1317.astype('bool'), [15, 7, 5]), relay.reshape(var_1317.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([bop_1308,call_1316,var_1317,])
output2 = relay.Tuple([bop_1311,call_1318,var_1317,])
func_1322 = relay.Function([var_1307,var_1317,], output)
mod['func_1322'] = func_1322
mod = relay.transform.InferType()(mod)
mutated_mod['func_1322'] = func_1322
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1322_call = mutated_mod.get_global_var('func_1322')
var_1324 = relay.var("var_1324", dtype = "bool", shape = (14, 3, 15))#candidate|1324|(14, 3, 15)|var|bool
var_1325 = relay.var("var_1325", dtype = "bool", shape = (525,))#candidate|1325|(525,)|var|bool
call_1323 = func_1322_call(var_1324,var_1325,)
output = call_1323
func_1326 = relay.Function([var_1324,var_1325,], output)
mutated_mod['func_1326'] = func_1326
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1379 = relay.TupleGetItem(func_1084_call(), 0)
call_1380 = relay.TupleGetItem(func_1086_call(), 0)
func_1152_call = mod.get_global_var('func_1152')
func_1155_call = mutated_mod.get_global_var('func_1155')
var_1382 = relay.var("var_1382", dtype = "bool", shape = (300,))#candidate|1382|(300,)|var|bool
call_1381 = relay.TupleGetItem(func_1152_call(relay.reshape(var_1382.astype('bool'), [12, 5, 5])), 0)
call_1383 = relay.TupleGetItem(func_1155_call(relay.reshape(var_1382.astype('bool'), [12, 5, 5])), 0)
output = relay.Tuple([call_1379,call_1381,var_1382,])
output2 = relay.Tuple([call_1380,call_1383,var_1382,])
func_1404 = relay.Function([var_1382,], output)
mod['func_1404'] = func_1404
mod = relay.transform.InferType()(mod)
mutated_mod['func_1404'] = func_1404
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1405 = relay.var("var_1405", dtype = "bool", shape = (300,))#candidate|1405|(300,)|var|bool
func_1404_call = mutated_mod.get_global_var('func_1404')
call_1406 = func_1404_call(var_1405)
output = call_1406
func_1407 = relay.Function([var_1405], output)
mutated_mod['func_1407'] = func_1407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1415 = relay.TupleGetItem(func_1040_call(), 0)
call_1416 = relay.TupleGetItem(func_1042_call(), 0)
output = relay.Tuple([call_1415,])
output2 = relay.Tuple([call_1416,])
func_1430 = relay.Function([], output)
mod['func_1430'] = func_1430
mod = relay.transform.InferType()(mod)
mutated_mod['func_1430'] = func_1430
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1430_call = mutated_mod.get_global_var('func_1430')
call_1431 = func_1430_call()
output = call_1431
func_1432 = relay.Function([], output)
mutated_mod['func_1432'] = func_1432
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1453 = relay.var("var_1453", dtype = "float64", shape = (6, 11, 6))#candidate|1453|(6, 11, 6)|var|float64
uop_1454 = relay.log10(var_1453.astype('float64')) # shape=(6, 11, 6)
output = uop_1454
output2 = uop_1454
func_1463 = relay.Function([var_1453,], output)
mod['func_1463'] = func_1463
mod = relay.transform.InferType()(mod)
var_1464 = relay.var("var_1464", dtype = "float64", shape = (6, 11, 6))#candidate|1464|(6, 11, 6)|var|float64
output = func_1463(var_1464)
func_1465 = relay.Function([var_1464], output)
mutated_mod['func_1465'] = func_1465
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1482 = relay.TupleGetItem(func_1084_call(), 0)
call_1483 = relay.TupleGetItem(func_1086_call(), 0)
var_1502 = relay.var("var_1502", dtype = "float32", shape = (14, 3, 15))#candidate|1502|(14, 3, 15)|var|float32
bop_1503 = relay.divide(call_1482.astype('float32'), relay.reshape(var_1502.astype('float32'), relay.shape_of(call_1482))) # shape=(14, 3, 15)
bop_1506 = relay.divide(call_1483.astype('float32'), relay.reshape(var_1502.astype('float32'), relay.shape_of(call_1483))) # shape=(14, 3, 15)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1516 = relay.TupleGetItem(func_1084_call(), 0)
call_1517 = relay.TupleGetItem(func_1086_call(), 0)
output = relay.Tuple([bop_1503,call_1516,])
output2 = relay.Tuple([bop_1506,call_1517,])
func_1526 = relay.Function([var_1502,], output)
mod['func_1526'] = func_1526
mod = relay.transform.InferType()(mod)
var_1527 = relay.var("var_1527", dtype = "float32", shape = (14, 3, 15))#candidate|1527|(14, 3, 15)|var|float32
output = func_1526(var_1527)
func_1528 = relay.Function([var_1527], output)
mutated_mod['func_1528'] = func_1528
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_1589 = relay.TupleGetItem(func_1430_call(), 0)
call_1590 = relay.TupleGetItem(func_1432_call(), 0)
func_1152_call = mod.get_global_var('func_1152')
func_1155_call = mutated_mod.get_global_var('func_1155')
const_1595 = relay.const([[False,True,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,False,False,False,True,True,True,False,True,True,False,True],[True,False,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,True,True,True,True],[False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False],[False,False,True,False,True,False,True,False,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False],[True,True,False,False,True,True,False,True,True,False,True,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,False,False],[True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,True],[True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,True,False,False,True,False,True,False,False,False,True],[True,False,False,False,True,False,True,True,True,False,True,False,True,False,True,False,False,True,True,False,True,False,True,True,True,True,True,True,True,True],[True,True,True,True,True,False,True,False,True,False,True,False,False,False,True,True,True,True,False,False,True,True,False,False,True,False,False,False,True,True],[True,False,False,True,True,True,True,False,False,True,False,True,True,True,True,False,False,False,True,True,False,True,False,True,True,True,True,True,True,False]], dtype = "bool")#candidate|1595|(10, 30)|const|bool
call_1594 = relay.TupleGetItem(func_1152_call(relay.reshape(const_1595.astype('bool'), [12, 5, 5])), 2)
call_1596 = relay.TupleGetItem(func_1155_call(relay.reshape(const_1595.astype('bool'), [12, 5, 5])), 2)
output = relay.Tuple([call_1589,call_1594,const_1595,])
output2 = relay.Tuple([call_1590,call_1596,const_1595,])
func_1611 = relay.Function([], output)
mod['func_1611'] = func_1611
mod = relay.transform.InferType()(mod)
output = func_1611()
func_1612 = relay.Function([], output)
mutated_mod['func_1612'] = func_1612
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1616 = relay.TupleGetItem(func_1040_call(), 0)
call_1617 = relay.TupleGetItem(func_1042_call(), 0)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
var_1623 = relay.var("var_1623", dtype = "bool", shape = (525,))#candidate|1623|(525,)|var|bool
call_1622 = func_465_call(relay.reshape(var_1623.astype('bool'), [15, 7, 5]), relay.reshape(var_1623.astype('bool'), [15, 7, 5]), )
call_1624 = func_465_call(relay.reshape(var_1623.astype('bool'), [15, 7, 5]), relay.reshape(var_1623.astype('bool'), [15, 7, 5]), )
func_1463_call = mod.get_global_var('func_1463')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_1627 = relay.var("var_1627", dtype = "float64", shape = (66, 6))#candidate|1627|(66, 6)|var|float64
call_1626 = func_1463_call(relay.reshape(var_1627.astype('float64'), [6, 11, 6]))
call_1628 = func_1463_call(relay.reshape(var_1627.astype('float64'), [6, 11, 6]))
output = relay.Tuple([call_1616,call_1622,var_1623,call_1626,var_1627,])
output2 = relay.Tuple([call_1617,call_1624,var_1623,call_1628,var_1627,])
func_1637 = relay.Function([var_1623,var_1627,], output)
mod['func_1637'] = func_1637
mod = relay.transform.InferType()(mod)
mutated_mod['func_1637'] = func_1637
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1637_call = mutated_mod.get_global_var('func_1637')
var_1639 = relay.var("var_1639", dtype = "bool", shape = (525,))#candidate|1639|(525,)|var|bool
var_1640 = relay.var("var_1640", dtype = "float64", shape = (66, 6))#candidate|1640|(66, 6)|var|float64
call_1638 = func_1637_call(var_1639,var_1640,)
output = call_1638
func_1641 = relay.Function([var_1639,var_1640,], output)
mutated_mod['func_1641'] = func_1641
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_1736 = relay.TupleGetItem(func_1040_call(), 0)
call_1737 = relay.TupleGetItem(func_1042_call(), 0)
func_1463_call = mod.get_global_var('func_1463')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_1746 = relay.var("var_1746", dtype = "float64", shape = (396,))#candidate|1746|(396,)|var|float64
call_1745 = func_1463_call(relay.reshape(var_1746.astype('float64'), [6, 11, 6]))
call_1747 = func_1463_call(relay.reshape(var_1746.astype('float64'), [6, 11, 6]))
func_1404_call = mod.get_global_var('func_1404')
func_1407_call = mutated_mod.get_global_var('func_1407')
var_1771 = relay.var("var_1771", dtype = "bool", shape = (300,))#candidate|1771|(300,)|var|bool
call_1770 = relay.TupleGetItem(func_1404_call(relay.reshape(var_1771.astype('bool'), [300,])), 2)
call_1772 = relay.TupleGetItem(func_1407_call(relay.reshape(var_1771.astype('bool'), [300,])), 2)
output = relay.Tuple([call_1736,call_1745,var_1746,call_1770,var_1771,])
output2 = relay.Tuple([call_1737,call_1747,var_1746,call_1772,var_1771,])
func_1780 = relay.Function([var_1746,var_1771,], output)
mod['func_1780'] = func_1780
mod = relay.transform.InferType()(mod)
var_1781 = relay.var("var_1781", dtype = "float64", shape = (396,))#candidate|1781|(396,)|var|float64
var_1782 = relay.var("var_1782", dtype = "bool", shape = (300,))#candidate|1782|(300,)|var|bool
output = func_1780(var_1781,var_1782,)
func_1783 = relay.Function([var_1781,var_1782,], output)
mutated_mod['func_1783'] = func_1783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_1801 = relay.TupleGetItem(func_1430_call(), 0)
call_1802 = relay.TupleGetItem(func_1432_call(), 0)
output = call_1801
output2 = call_1802
func_1817 = relay.Function([], output)
mod['func_1817'] = func_1817
mod = relay.transform.InferType()(mod)
mutated_mod['func_1817'] = func_1817
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mutated_mod.get_global_var('func_1817')
call_1818 = func_1817_call()
output = call_1818
func_1819 = relay.Function([], output)
mutated_mod['func_1819'] = func_1819
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_1832 = func_1817_call()
call_1833 = func_1817_call()
func_1463_call = mod.get_global_var('func_1463')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_1841 = relay.var("var_1841", dtype = "float64", shape = (396,))#candidate|1841|(396,)|var|float64
call_1840 = func_1463_call(relay.reshape(var_1841.astype('float64'), [6, 11, 6]))
call_1842 = func_1463_call(relay.reshape(var_1841.astype('float64'), [6, 11, 6]))
output = relay.Tuple([call_1832,call_1840,var_1841,])
output2 = relay.Tuple([call_1833,call_1842,var_1841,])
func_1846 = relay.Function([var_1841,], output)
mod['func_1846'] = func_1846
mod = relay.transform.InferType()(mod)
mutated_mod['func_1846'] = func_1846
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1847 = relay.var("var_1847", dtype = "float64", shape = (396,))#candidate|1847|(396,)|var|float64
func_1846_call = mutated_mod.get_global_var('func_1846')
call_1848 = func_1846_call(var_1847)
output = call_1848
func_1849 = relay.Function([var_1847], output)
mutated_mod['func_1849'] = func_1849
mutated_mod = relay.transform.InferType()(mutated_mod)
var_1874 = relay.var("var_1874", dtype = "float32", shape = (1, 2, 5))#candidate|1874|(1, 2, 5)|var|float32
uop_1875 = relay.atan(var_1874.astype('float32')) # shape=(1, 2, 5)
func_1056_call = mod.get_global_var('func_1056')
func_1059_call = mutated_mod.get_global_var('func_1059')
var_1880 = relay.var("var_1880", dtype = "float32", shape = (280,))#candidate|1880|(280,)|var|float32
call_1879 = relay.TupleGetItem(func_1056_call(relay.reshape(var_1880.astype('float32'), [2, 10, 14])), 1)
call_1881 = relay.TupleGetItem(func_1059_call(relay.reshape(var_1880.astype('float32'), [2, 10, 14])), 1)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
var_1884 = relay.var("var_1884", dtype = "bool", shape = (525,))#candidate|1884|(525,)|var|bool
call_1883 = func_465_call(relay.reshape(var_1884.astype('bool'), [15, 7, 5]), relay.reshape(var_1884.astype('bool'), [15, 7, 5]), )
call_1885 = func_465_call(relay.reshape(var_1884.astype('bool'), [15, 7, 5]), relay.reshape(var_1884.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([uop_1875,call_1879,var_1880,call_1883,var_1884,])
output2 = relay.Tuple([uop_1875,call_1881,var_1880,call_1885,var_1884,])
func_1888 = relay.Function([var_1874,var_1880,var_1884,], output)
mod['func_1888'] = func_1888
mod = relay.transform.InferType()(mod)
mutated_mod['func_1888'] = func_1888
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1888_call = mutated_mod.get_global_var('func_1888')
var_1890 = relay.var("var_1890", dtype = "float32", shape = (1, 2, 5))#candidate|1890|(1, 2, 5)|var|float32
var_1891 = relay.var("var_1891", dtype = "float32", shape = (280,))#candidate|1891|(280,)|var|float32
var_1892 = relay.var("var_1892", dtype = "bool", shape = (525,))#candidate|1892|(525,)|var|bool
call_1889 = func_1888_call(var_1890,var_1891,var_1892,)
output = call_1889
func_1893 = relay.Function([var_1890,var_1891,var_1892,], output)
mutated_mod['func_1893'] = func_1893
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1901 = relay.TupleGetItem(func_1084_call(), 0)
call_1902 = relay.TupleGetItem(func_1086_call(), 0)
func_1846_call = mod.get_global_var('func_1846')
func_1849_call = mutated_mod.get_global_var('func_1849')
const_1917 = relay.const([5.168122,2.394415,-7.766229,8.113430,1.460483,2.542597,4.578575,-5.163089,-7.468874,-9.672260,-5.971848,7.398129,-2.316121,-5.727257,-2.615377,5.033089,0.038275,0.530128,2.184024,5.860518,-0.808039,-2.626202,5.164223,-5.481990,-9.613504,-0.779862,-1.057399,-3.353521,2.992127,-9.846340,-6.944091,4.165080,-4.472587,1.269316,7.323868,-2.619154,-7.335020,3.586268,-8.439158,2.845647,-0.166932,7.925618,3.617083,-3.154202,-6.894328,3.697454,-8.368407,-7.243663,6.991930,-6.615671,-2.256579,9.214360,-0.429518,7.752188,-1.479297,1.972227,-3.572515,3.244639,-6.149714,-5.493569,9.457366,0.492060,7.989794,-2.282021,-4.496154,9.563989,-0.142670,0.123054,-0.691435,7.065839,5.020235,7.452995,4.689736,-3.925184,-5.198593,-3.296211,-2.914438,1.003357,6.751069,-4.813800,6.429656,1.649580,-0.518689,-6.501074,1.363923,1.174866,-6.333287,-4.694802,-3.071221,3.575938,-9.786298,-1.567143,-9.535962,-8.005692,3.133302,3.021449,-8.714683,-2.089102,1.053614,1.558184,-5.241422,5.806083,-2.959841,-8.045578,-0.407039,6.667426,7.070320,3.517988,-0.755228,-2.553383,9.436996,-8.457893,-3.402246,-5.544778,1.725101,-7.900504,3.828426,-0.660449,4.282652,-2.892306,-8.236100,-5.324484,7.873190,5.315501,8.236535,1.013652,1.763976,4.865393,2.918116,4.428076,0.259371,-3.245615,-1.701850,-3.935085,-5.211569,6.895032,0.418718,-8.864982,-0.973252,-6.265690,2.998856,-8.653688,5.578898,-1.135312,5.392203,7.591294,4.692030,5.914730,-0.226947,-6.469129,-2.063381,8.771255,6.374666,-8.103411,-5.132064,-2.108528,5.968597,-5.488037,-8.565646,1.785868,0.682317,-9.437448,-4.860760,-2.537624,-5.107080,0.820557,-4.606406,-8.175584,2.178767,8.285054,9.078231,2.597505,-3.815935,0.327880,5.499892,9.271192,6.715498,8.316712,5.153861,-9.635941,-0.095132,8.859689,-8.276235,5.474857,-1.394208,2.078702,-8.115336,-6.802347,3.503517,4.003855,-3.527240,1.155134,-8.863628,-9.390390,-8.961556,7.117984,-3.897034,3.886402,-2.493682,-4.603538,-3.738562,-4.370121,1.934542,0.251403,-8.827331,2.724639,6.039410,-5.035625,6.592402,-2.403008,4.800218,3.050554,-5.289049,0.898224,9.273918,4.367322,2.648499,-5.254598,4.751947,8.070587,-4.898628,-2.473887,5.232279,6.729135,6.410300,-2.156782,-4.387751,5.633985,9.352591,2.096768,-1.949847,-3.549171,1.861436,-1.510994,-4.571114,-2.230801,-0.370335,9.755689,-4.436576,9.829815,-4.194921,-5.612338,4.800797,0.056171,-9.104323,3.070514,8.660032,0.907413,-4.509249,8.341675,0.163201,7.866944,7.449020,-4.423559,0.753407,6.324569,6.968616,-1.577690,4.010084,6.553630,5.990052,5.893606,-8.154758,7.425998,-9.614509,-3.718501,-2.013658,-6.957710,-9.276379,2.972304,-3.799472,8.693121,0.384164,-2.683265,6.082178,-0.171787,-4.262549,9.026106,-7.678487,0.250518,-9.523047,3.883235,8.751333,-5.276520,-9.553648,8.190834,-7.893443,-8.784845,2.467542,7.285120,0.953512,6.135804,2.054935,-5.929227,5.551725,-6.684273,4.274339,-4.030074,6.365509,-7.871799,1.967362,-5.333890,-6.053945,7.770740,0.139663,-8.118594,-4.398713,-3.819593,8.602484,-1.453365,-0.141177,-9.464444,-0.469682,-8.264220,4.717180,9.420459,5.761797,-4.726202,-5.707408,5.936917,-8.742237,-5.073649,7.521827,-5.953085,-7.748861,7.177307,-5.657849,-1.135533,-7.542491,-4.108711,-7.654488,-4.233721,-9.182512,9.409651,-6.897914,-3.765827,3.720699,-7.047322,-8.162792,2.986766,1.989439,9.786030,-1.364388,-4.414647,4.447875,-1.004131,-7.187867,7.515456,3.777049,3.327799,5.161048,9.720133,8.802926,1.387706,-8.909604,-6.042544,9.643633,7.147506,6.001553,-7.430067,8.319246,-4.226162,-2.002994,-7.392812,2.099527,4.507319,8.270975,3.189197,-0.137530,-9.141834,6.757207,-3.920789,6.499113,-3.170538,4.282806,1.288385,2.605712,-0.356613,7.756717,4.101978,9.576530,3.685989,1.500281,6.379360,2.149857,3.235957,-2.096212,5.301436,1.771988,-9.967987,-4.451858,6.312764,-5.348996,0.198978,-0.999149,-4.783255], dtype = "float64")#candidate|1917|(396,)|const|float64
call_1916 = relay.TupleGetItem(func_1846_call(relay.reshape(const_1917.astype('float64'), [396,])), 0)
call_1918 = relay.TupleGetItem(func_1849_call(relay.reshape(const_1917.astype('float64'), [396,])), 0)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
var_1920 = relay.var("var_1920", dtype = "bool", shape = (525,))#candidate|1920|(525,)|var|bool
call_1919 = func_465_call(relay.reshape(var_1920.astype('bool'), [15, 7, 5]), relay.reshape(var_1920.astype('bool'), [15, 7, 5]), )
call_1921 = func_465_call(relay.reshape(var_1920.astype('bool'), [15, 7, 5]), relay.reshape(var_1920.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([call_1901,call_1916,const_1917,call_1919,var_1920,])
output2 = relay.Tuple([call_1902,call_1918,const_1917,call_1921,var_1920,])
func_1939 = relay.Function([var_1920,], output)
mod['func_1939'] = func_1939
mod = relay.transform.InferType()(mod)
var_1940 = relay.var("var_1940", dtype = "bool", shape = (525,))#candidate|1940|(525,)|var|bool
output = func_1939(var_1940)
func_1941 = relay.Function([var_1940], output)
mutated_mod['func_1941'] = func_1941
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_1981 = relay.TupleGetItem(func_1084_call(), 0)
call_1982 = relay.TupleGetItem(func_1086_call(), 0)
func_1133_call = mod.get_global_var('func_1133')
func_1135_call = mutated_mod.get_global_var('func_1135')
call_1991 = relay.TupleGetItem(func_1133_call(relay.reshape(call_1981.astype('float32'), [14, 3, 15])), 2)
call_1992 = relay.TupleGetItem(func_1135_call(relay.reshape(call_1981.astype('float32'), [14, 3, 15])), 2)
func_1526_call = mod.get_global_var('func_1526')
func_1528_call = mutated_mod.get_global_var('func_1528')
call_1994 = relay.TupleGetItem(func_1526_call(relay.reshape(call_1981.astype('float32'), [14, 3, 15])), 1)
call_1995 = relay.TupleGetItem(func_1528_call(relay.reshape(call_1981.astype('float32'), [14, 3, 15])), 1)
bop_2005 = relay.subtract(call_1994.astype('uint32'), relay.reshape(call_1981.astype('uint32'), relay.shape_of(call_1994))) # shape=(14, 3, 15)
bop_2008 = relay.subtract(call_1995.astype('uint32'), relay.reshape(call_1982.astype('uint32'), relay.shape_of(call_1995))) # shape=(14, 3, 15)
output = relay.Tuple([call_1991,bop_2005,])
output2 = relay.Tuple([call_1992,bop_2008,])
func_2010 = relay.Function([], output)
mod['func_2010'] = func_2010
mod = relay.transform.InferType()(mod)
output = func_2010()
func_2011 = relay.Function([], output)
mutated_mod['func_2011'] = func_2011
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_2014 = relay.TupleGetItem(func_1430_call(), 0)
call_2015 = relay.TupleGetItem(func_1432_call(), 0)
output = call_2014
output2 = call_2015
func_2016 = relay.Function([], output)
mod['func_2016'] = func_2016
mod = relay.transform.InferType()(mod)
output = func_2016()
func_2017 = relay.Function([], output)
mutated_mod['func_2017'] = func_2017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2026 = relay.TupleGetItem(func_2010_call(), 1)
call_2027 = relay.TupleGetItem(func_2011_call(), 1)
output = call_2026
output2 = call_2027
func_2034 = relay.Function([], output)
mod['func_2034'] = func_2034
mod = relay.transform.InferType()(mod)
output = func_2034()
func_2035 = relay.Function([], output)
mutated_mod['func_2035'] = func_2035
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_2038 = relay.TupleGetItem(func_1040_call(), 0)
call_2039 = relay.TupleGetItem(func_1042_call(), 0)
output = call_2038
output2 = call_2039
func_2045 = relay.Function([], output)
mod['func_2045'] = func_2045
mod = relay.transform.InferType()(mod)
mutated_mod['func_2045'] = func_2045
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mutated_mod.get_global_var('func_2045')
call_2046 = func_2045_call()
output = call_2046
func_2047 = relay.Function([], output)
mutated_mod['func_2047'] = func_2047
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1612_call = mutated_mod.get_global_var('func_1612')
call_2065 = relay.TupleGetItem(func_1611_call(), 1)
call_2066 = relay.TupleGetItem(func_1612_call(), 1)
var_2071 = relay.var("var_2071", dtype = "bool", shape = (525, 10))#candidate|2071|(525, 10)|var|bool
bop_2072 = relay.less_equal(call_2065.astype('bool'), var_2071.astype('bool')) # shape=(525, 10)
bop_2075 = relay.less_equal(call_2066.astype('bool'), var_2071.astype('bool')) # shape=(525, 10)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
call_2090 = func_465_call(relay.reshape(call_2065.astype('bool'), [15, 7, 5]), relay.reshape(call_2065.astype('bool'), [15, 7, 5]), )
call_2091 = func_465_call(relay.reshape(call_2065.astype('bool'), [15, 7, 5]), relay.reshape(call_2065.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([bop_2072,call_2090,])
output2 = relay.Tuple([bop_2075,call_2091,])
func_2092 = relay.Function([var_2071,], output)
mod['func_2092'] = func_2092
mod = relay.transform.InferType()(mod)
mutated_mod['func_2092'] = func_2092
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2093 = relay.var("var_2093", dtype = "bool", shape = (525, 10))#candidate|2093|(525, 10)|var|bool
func_2092_call = mutated_mod.get_global_var('func_2092')
call_2094 = func_2092_call(var_2093)
output = call_2094
func_2095 = relay.Function([var_2093], output)
mutated_mod['func_2095'] = func_2095
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_2112 = func_1817_call()
call_2113 = func_1817_call()
func_1846_call = mod.get_global_var('func_1846')
func_1849_call = mutated_mod.get_global_var('func_1849')
var_2128 = relay.var("var_2128", dtype = "float64", shape = (396,))#candidate|2128|(396,)|var|float64
call_2127 = relay.TupleGetItem(func_1846_call(relay.reshape(var_2128.astype('float64'), [396,])), 2)
call_2129 = relay.TupleGetItem(func_1849_call(relay.reshape(var_2128.astype('float64'), [396,])), 2)
output = relay.Tuple([call_2112,call_2127,var_2128,])
output2 = relay.Tuple([call_2113,call_2129,var_2128,])
func_2142 = relay.Function([var_2128,], output)
mod['func_2142'] = func_2142
mod = relay.transform.InferType()(mod)
var_2143 = relay.var("var_2143", dtype = "float64", shape = (396,))#candidate|2143|(396,)|var|float64
output = func_2142(var_2143)
func_2144 = relay.Function([var_2143], output)
mutated_mod['func_2144'] = func_2144
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_2176 = func_2016_call()
call_2177 = func_2016_call()
const_2179 = relay.const([[[5.361338,1.318205,-9.221188,-0.736378,-8.940088,9.192039,-2.672161,4.566357,-9.110335,4.856723,-4.018456,1.283580,1.395464,-1.020632,3.146851],[-7.395423,-1.566620,1.599607,-9.312041,-4.224085,-4.384453,-2.373602,-7.797033,4.379173,6.420766,1.265868,-2.192264,-3.691619,-4.372095,6.437814],[-9.217637,-0.135975,4.513318,6.995560,6.061631,9.732366,-1.433222,-0.264079,0.790988,8.671008,-9.023772,7.008351,7.224268,-5.702305,-5.047665]],[[0.658256,-4.992446,1.924922,3.410864,7.271510,-9.810071,-7.443114,-3.481010,1.221451,-4.317885,-4.576358,9.467998,0.987081,5.733171,-1.506880],[7.871455,3.733056,3.330683,-9.373278,4.872000,1.457939,-0.130695,-0.426306,4.254033,-0.981133,-8.382916,-2.663527,-7.851389,-3.180664,-5.703418],[2.480176,-2.836311,6.154670,6.041608,-5.743226,1.769099,8.357115,1.993905,5.281712,9.822184,9.419020,-2.632906,-7.542062,1.150049,6.576003]],[[2.488782,-9.706869,7.672789,-4.680812,3.308181,7.631561,-0.350318,-1.499261,5.218823,-9.765897,2.530184,-7.254976,-2.271124,6.606568,-6.564485],[4.699720,3.922619,0.380704,4.710862,-3.325541,4.919906,4.999474,-1.099094,3.297797,4.523090,-6.838021,9.594587,7.194619,5.968009,-2.488473],[1.798012,-7.522442,7.407167,3.822296,9.573416,5.327420,3.217482,-1.165111,-9.906405,5.508287,-5.877876,-3.285277,3.830832,1.623581,-3.860967]],[[-3.417674,1.363588,8.723911,-3.367046,5.957918,-9.385699,-0.338256,7.114077,9.637415,9.441449,-5.797886,-6.903408,4.688547,-6.726521,7.242263],[-3.593467,-8.870689,-2.979505,-5.319621,-9.955885,-8.253059,-8.532326,-9.144643,2.460014,4.627651,3.314219,-0.274360,1.773703,7.681964,-9.796395],[-2.118633,-6.476548,-9.569018,-2.066645,8.204299,-7.586976,8.902813,3.973876,2.354727,9.267701,2.544512,-0.820232,9.439261,5.439450,0.974751]],[[7.727987,2.974284,-2.124719,-2.427157,-8.185919,9.464143,6.963727,-4.810094,-5.701154,5.577901,-3.430776,-1.876222,0.008109,-2.091802,-4.615134],[-5.549534,-5.282306,7.224908,-4.612362,2.338531,-9.659418,0.559133,-0.922872,-4.976915,3.447350,-8.994180,-4.670551,-5.403742,-4.368437,-0.693720],[-9.200261,-0.179997,-0.221476,7.753649,4.317230,-5.037477,5.058599,3.845533,5.618737,6.217274,-9.577869,-0.739418,-2.688755,-9.615917,-9.563376]],[[-8.321715,9.459858,7.494161,-6.254179,-5.066915,9.475042,7.084315,8.871337,-7.818819,-8.794069,3.106214,-9.972026,6.843825,0.631425,8.838594],[3.716779,-5.774759,6.431945,-4.910774,7.366206,2.574931,7.378100,4.590572,-3.535570,0.608213,3.472284,1.563080,6.392700,2.222345,-9.788994],[-6.534876,-7.145938,-7.636035,-2.483076,2.196569,-7.486552,-5.258019,-7.717049,-8.722699,-6.169880,8.421961,-6.347641,5.511760,-1.814789,-5.262272]],[[3.023853,-9.338233,-9.078545,7.771888,4.276044,-6.767864,-6.378385,-7.849860,-7.035819,4.165977,-4.939362,2.604478,0.993375,-7.786604,7.248177],[-3.254083,9.224632,-1.965968,0.850153,-6.090816,-5.748410,-6.983120,-3.070586,9.747248,4.164987,0.641048,-2.970050,0.416808,1.453295,1.491922],[-2.024108,9.197633,-4.098634,9.750074,-3.279341,-1.677507,-3.378430,4.900995,2.359087,-2.257448,6.555023,2.185739,-8.148302,5.185759,-0.759873]],[[-6.523535,-0.164264,9.855042,8.665767,-6.096826,-8.760314,-5.358279,-6.337252,0.717484,3.662042,-3.462733,5.880919,-2.523187,-3.061237,6.530389],[-7.355637,-8.025810,-1.786477,0.136373,-8.804419,1.335458,-0.739420,-3.337028,4.287575,9.340133,2.742392,3.055574,3.846292,-2.840620,1.752144],[-4.819772,7.267442,-8.276080,-1.469809,0.844731,9.945991,-5.664833,-6.550035,-4.579139,-3.298852,-9.115554,-8.906128,7.024039,0.303046,3.559299]],[[6.326318,-8.366216,-9.920187,-0.338340,-5.057059,-3.829763,-4.158676,-1.157986,6.814449,-1.807708,-7.584658,6.115072,-0.007254,-5.973973,-4.750497],[-2.895321,6.860370,-2.322487,1.396010,2.113809,-4.433434,-9.056107,-1.539384,7.468788,3.446434,7.967428,7.490622,-3.311533,6.908273,5.066493],[5.317539,-2.211210,1.803567,-7.978142,7.672493,-8.767603,4.988709,5.832858,2.860752,7.540139,-9.548438,-8.002753,5.562100,-2.868791,1.627541]],[[-6.790277,5.592554,-2.248448,4.158161,-8.737472,-5.270919,-6.500477,1.128020,7.966195,0.942214,4.912568,5.818833,9.052107,8.381279,-9.149046],[7.647566,5.362788,5.847277,4.546598,-1.395847,2.185682,0.184041,2.652145,3.702448,6.166589,1.991350,2.717086,9.412962,-3.840385,-7.054874],[2.893698,6.470832,-5.429573,-1.705165,-5.726530,7.607655,2.925999,0.796209,7.907119,4.898143,9.276207,-4.943344,-5.491128,7.812176,-1.865304]],[[0.303071,-1.144225,-0.803444,7.564494,-8.140123,0.054749,9.118369,-6.786038,2.889829,-1.408176,0.891169,-9.246578,-3.494224,8.582702,5.466167],[0.188849,2.136502,7.830948,-7.209303,1.451717,-3.685882,4.229680,8.608202,3.061477,7.408589,-5.685093,0.962168,-5.189083,2.663102,-6.077152],[7.354374,5.108723,0.779098,-3.432474,6.764946,-0.091488,2.991771,2.870223,-6.610676,7.140509,-7.239456,-7.533982,-0.146533,5.135108,-1.752899]],[[-3.514912,0.310147,-1.021366,8.557611,5.343733,-9.747358,-8.557129,1.592809,9.010301,-4.451587,9.588108,-9.396409,1.303393,1.742334,-7.738514],[-1.305703,5.979715,-5.571631,-6.637929,1.827403,-5.135839,8.390876,1.716886,-5.321884,-0.377334,7.586618,-3.976761,2.579328,4.143197,-6.970224],[-0.387047,-5.606289,1.264825,-5.014139,-7.943306,0.697915,1.655654,-1.655261,4.269603,9.562219,1.609243,8.000089,-1.066538,9.879656,5.098324]],[[9.910510,-9.584041,-0.575651,-9.343986,2.779786,-2.382420,4.232817,-5.395080,-7.505091,7.930766,4.037950,-2.143443,-7.820609,-6.728952,-0.903356],[1.331020,2.117167,-4.187976,1.898136,-9.016537,8.435027,2.999565,4.696734,-0.049386,5.608988,9.809198,1.955058,-4.139899,6.648617,2.435075],[-8.233120,0.731989,4.468243,4.262757,6.888118,4.238787,-8.552815,9.141509,-8.458585,5.448263,9.350098,2.447196,3.730276,-8.673206,-6.408934]],[[-1.368342,4.612764,-0.149902,8.137431,5.973287,-5.481027,-3.779728,-3.097984,-5.458143,2.920029,-3.709631,-1.827236,2.302348,1.170624,-2.890407],[-1.420814,2.399342,5.204787,-5.063156,3.879889,9.264499,-7.597773,1.266778,4.902540,-2.711141,0.714627,-4.232668,-6.955870,9.427330,8.664640],[2.496406,0.276273,4.328993,-2.206053,7.341424,-1.654112,0.058323,-2.588341,8.269680,-6.579012,0.945863,-5.612410,-7.029559,6.238707,8.015060]]], dtype = "float32")#candidate|2179|(14, 3, 15)|const|float32
bop_2180 = relay.floor_divide(call_2176.astype('float64'), relay.reshape(const_2179.astype('float64'), relay.shape_of(call_2176))) # shape=(14, 3, 15)
bop_2183 = relay.floor_divide(call_2177.astype('float64'), relay.reshape(const_2179.astype('float64'), relay.shape_of(call_2177))) # shape=(14, 3, 15)
output = relay.Tuple([bop_2180,])
output2 = relay.Tuple([bop_2183,])
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
var_2238 = relay.var("var_2238", dtype = "float32", shape = ())#candidate|2238|()|var|float32
var_2239 = relay.var("var_2239", dtype = "float32", shape = (8, 7, 11))#candidate|2239|(8, 7, 11)|var|float32
bop_2240 = relay.floor_divide(var_2238.astype('float32'), var_2239.astype('float32')) # shape=(8, 7, 11)
bop_2243 = relay.greater(var_2238.astype('bool'), bop_2240.astype('bool')) # shape=(8, 7, 11)
var_2247 = relay.var("var_2247", dtype = "bool", shape = (8, 7, 11))#candidate|2247|(8, 7, 11)|var|bool
bop_2248 = relay.equal(bop_2243.astype('bool'), relay.reshape(var_2247.astype('bool'), relay.shape_of(bop_2243))) # shape=(8, 7, 11)
bop_2251 = relay.maximum(bop_2248.astype('int64'), relay.reshape(bop_2243.astype('int64'), relay.shape_of(bop_2248))) # shape=(8, 7, 11)
func_1056_call = mod.get_global_var('func_1056')
func_1059_call = mutated_mod.get_global_var('func_1059')
const_2258 = relay.const([-7.534952,-8.695062,3.240429,-1.251725,-2.518185,-7.509220,0.736396,-4.927212,-8.102449,-0.549223,-4.802388,-8.490021,8.497126,4.464512,7.739174,-1.721632,-0.109545,-1.604676,-4.613415,1.563851,-3.118245,3.704498,-8.467538,1.900167,5.634041,-8.849655,-0.337246,8.206920,-9.973957,1.017927,-2.319632,8.615159,-7.549101,-9.967132,-5.349473,7.360960,8.130408,-9.522265,0.372926,1.539808,1.157033,-7.713787,-1.492708,0.268851,-5.213801,-2.297989,-9.717640,6.191543,-5.740520,5.127927,7.097704,2.219428,-1.297334,-6.915941,8.631911,-2.329201,-5.480189,3.225845,6.252898,2.917615,3.692977,-5.328534,0.008978,-3.769701,3.223574,3.006833,3.900898,6.554663,-6.676264,3.798844,7.161538,8.877347,-5.945235,-1.423913,9.225710,1.439773,-1.392170,6.051085,-4.982308,4.065367,6.754303,-6.720512,1.882488,-4.159580,-7.645871,8.087464,-1.529128,0.600091,1.965318,-3.674408,0.697114,9.709358,9.080685,4.784671,1.612044,9.118863,7.965115,5.941801,3.741415,4.570957,5.969245,-1.735085,7.257254,-3.993172,1.106264,1.336411,-8.900897,-7.176855,7.099643,9.946540,-4.435715,-8.691638,5.367896,-5.024092,3.552095,-9.810930,4.838691,-3.956815,-7.591802,2.949836,9.075077,-3.736814,-2.389619,5.007464,-1.476307,-5.182348,6.156047,2.352870,-4.629788,-8.013177,0.407435,-4.967472,4.475052,7.799051,2.847859,2.290850,2.990052,-5.340215,7.197002,-1.474392,7.140714,-7.796747,2.814169,6.502270,-9.217082,9.458537,-9.418056,-0.406661,1.672147,6.241229,-3.306438,2.967517,-0.767535,1.729629,-1.501888,7.170401,-4.655424,-6.381202,1.396802,9.213635,9.165037,4.627840,-8.957054,1.248509,3.560906,-0.397412,-5.810373,-9.424528,-6.907310,-1.456840,7.971999,-7.509687,1.900177,3.726992,-3.954588,-2.753792,7.633016,5.977239,9.097719,6.919026,2.637730,5.308646,-2.124612,-8.851439,6.473889,1.780640,-5.930102,8.902820,-8.840095,8.582576,9.419120,7.150093,0.137130,5.591466,8.814755,-7.764729,-8.075434,-7.403303,1.602916,2.354121,6.333383,2.355437,-6.305459,-3.991082,6.667673,5.526712,4.543847,6.087815,2.796052,-4.607281,-8.314113,4.244043,-2.956040,5.426137,-7.260506,-4.601247,8.680663,-4.148151,-1.156151,-8.728299,-6.885968,1.416515,-5.013618,-8.019308,0.752194,7.365647,8.031780,-0.169566,-6.635059,0.755383,0.835268,5.833658,6.079425,-3.721229,-4.155048,0.361091,0.635245,-9.405118,-9.227669,9.993283,2.754333,8.358751,-4.819582,-5.572801,2.799651,1.609980,-4.724901,5.409640,-2.838563,2.979006,-6.766446,2.222682,5.052548,-2.184785,2.478627,2.532849,-3.212565,5.779363,0.761336,8.407976,-0.894008,2.446854,0.569462,-3.832907,-9.006880,-9.800619,3.422678,-6.830208,-3.358725,-5.529219,3.406256,-2.537090,-6.511137,-6.958011,-5.755707,-9.176895,-0.627460,8.332974,-6.182799,-8.111817], dtype = "float32")#candidate|2258|(280,)|const|float32
call_2257 = relay.TupleGetItem(func_1056_call(relay.reshape(const_2258.astype('float32'), [2, 10, 14])), 1)
call_2259 = relay.TupleGetItem(func_1059_call(relay.reshape(const_2258.astype('float32'), [2, 10, 14])), 1)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_2273 = func_2045_call()
call_2274 = func_2045_call()
uop_2275 = relay.acos(bop_2243.astype('float32')) # shape=(8, 7, 11)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
var_2278 = relay.var("var_2278", dtype = "bool", shape = (525,))#candidate|2278|(525,)|var|bool
call_2277 = func_465_call(relay.reshape(var_2278.astype('bool'), [15, 7, 5]), relay.reshape(var_2278.astype('bool'), [15, 7, 5]), )
call_2279 = func_465_call(relay.reshape(var_2278.astype('bool'), [15, 7, 5]), relay.reshape(var_2278.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([bop_2251,call_2257,const_2258,call_2273,uop_2275,call_2277,var_2278,])
output2 = relay.Tuple([bop_2251,call_2259,const_2258,call_2274,uop_2275,call_2279,var_2278,])
func_2283 = relay.Function([var_2238,var_2239,var_2247,var_2278,], output)
mod['func_2283'] = func_2283
mod = relay.transform.InferType()(mod)
var_2284 = relay.var("var_2284", dtype = "float32", shape = ())#candidate|2284|()|var|float32
var_2285 = relay.var("var_2285", dtype = "float32", shape = (8, 7, 11))#candidate|2285|(8, 7, 11)|var|float32
var_2286 = relay.var("var_2286", dtype = "bool", shape = (8, 7, 11))#candidate|2286|(8, 7, 11)|var|bool
var_2287 = relay.var("var_2287", dtype = "bool", shape = (525,))#candidate|2287|(525,)|var|bool
output = func_2283(var_2284,var_2285,var_2286,var_2287,)
func_2288 = relay.Function([var_2284,var_2285,var_2286,var_2287,], output)
mutated_mod['func_2288'] = func_2288
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_2302 = relay.TupleGetItem(func_2198_call(), 0)
call_2303 = relay.TupleGetItem(func_2200_call(), 0)
var_2318 = relay.var("var_2318", dtype = "float64", shape = (14, 3, 15))#candidate|2318|(14, 3, 15)|var|float64
bop_2319 = relay.logical_xor(call_2302.astype('int8'), relay.reshape(var_2318.astype('int8'), relay.shape_of(call_2302))) # shape=(14, 3, 15)
bop_2322 = relay.logical_xor(call_2303.astype('int8'), relay.reshape(var_2318.astype('int8'), relay.shape_of(call_2303))) # shape=(14, 3, 15)
output = relay.Tuple([bop_2319,])
output2 = relay.Tuple([bop_2322,])
func_2326 = relay.Function([var_2318,], output)
mod['func_2326'] = func_2326
mod = relay.transform.InferType()(mod)
var_2327 = relay.var("var_2327", dtype = "float64", shape = (14, 3, 15))#candidate|2327|(14, 3, 15)|var|float64
output = func_2326(var_2327)
func_2328 = relay.Function([var_2327], output)
mutated_mod['func_2328'] = func_2328
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2343 = relay.TupleGetItem(func_2010_call(), 1)
call_2344 = relay.TupleGetItem(func_2011_call(), 1)
output = relay.Tuple([call_2343,])
output2 = relay.Tuple([call_2344,])
func_2351 = relay.Function([], output)
mod['func_2351'] = func_2351
mod = relay.transform.InferType()(mod)
output = func_2351()
func_2352 = relay.Function([], output)
mutated_mod['func_2352'] = func_2352
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_2387 = func_2034_call()
call_2388 = func_2034_call()
const_2392 = relay.const([[[-1,4,-4,2,-7,10,-2,-10,-3,5,-2,2,-2,6,-6],[-5,-6,1,-3,7,-3,3,1,6,-10,7,7,-9,4,5],[4,7,7,9,2,-8,-4,-10,6,9,8,9,-7,4,-6]],[[1,7,10,-5,-3,-7,-2,4,6,-8,10,-2,1,9,-3],[6,-5,-2,-8,3,4,4,1,-7,-10,1,-9,10,4,-7],[4,-9,-6,-5,-7,-8,8,-8,10,5,8,-1,-9,-9,10]],[[-8,-9,5,-7,2,9,-5,-1,-6,-8,-4,-5,3,8,6],[10,-4,8,-6,2,-9,9,-7,-8,-3,4,-3,4,4,8],[10,4,8,-5,-9,4,7,-5,-8,-9,-9,10,-5,-8,6]],[[1,-5,-2,-6,-9,4,-4,-1,-9,-2,-9,5,-3,-4,1],[10,-6,6,-9,-4,9,4,-3,2,3,10,5,1,-6,-10],[5,-9,-4,-10,7,-3,-2,-10,3,6,-6,-10,-4,8,8]],[[-6,-9,-5,-10,-7,-8,3,-7,-6,-5,-8,9,-1,-9,-2],[8,-9,5,-9,10,1,-4,8,9,4,6,-4,-8,-7,-1],[-1,1,5,5,-10,-8,2,7,-5,-4,10,-9,-5,9,-3]],[[3,1,-5,9,-10,6,1,-2,-8,7,-6,-9,1,-1,8],[-1,9,6,-8,-3,-3,8,6,2,-7,-5,-6,-9,10,7],[5,10,2,5,10,-10,-10,5,-8,-2,-6,9,3,8,7]],[[3,5,-5,1,7,-1,-4,-5,7,-8,8,5,-3,-3,-4],[-6,4,4,8,-1,-9,-4,-1,4,10,-6,5,6,-10,10],[-3,2,-8,9,2,-3,-10,3,-3,1,8,-4,1,-10,-10]],[[4,9,-3,2,4,-9,4,3,-3,2,-2,3,3,7,-4],[6,-2,-6,1,-4,4,2,-5,3,3,-3,-6,-2,-10,-2],[8,6,2,-5,-2,8,4,-3,-6,6,4,2,-6,10,-3]],[[-2,-10,-1,10,5,-4,-7,-4,-5,7,-8,1,-10,6,4],[-2,-10,-7,-7,6,-9,7,-7,6,-1,-5,3,-1,-4,-3],[-6,-7,9,7,10,-10,-4,-5,-7,-4,6,-9,9,2,-9]],[[-4,-1,-1,-4,8,4,3,4,10,10,2,-5,-3,-3,8],[1,6,2,2,-8,9,8,-1,-9,6,4,5,10,-4,6],[-4,-5,-9,-8,2,-3,9,3,6,8,3,-1,-1,-8,-6]],[[10,-1,10,9,-3,3,2,-9,-9,-8,6,-9,10,10,9],[-4,5,2,-7,1,-4,6,-6,2,10,6,-1,-5,-7,3],[-10,-4,4,10,9,-1,-10,2,4,3,3,-1,6,-5,10]],[[10,-7,-7,-10,-10,2,5,-2,8,-8,1,-2,-6,-8,-1],[1,10,-6,6,-8,9,2,2,1,-10,-2,-10,3,3,9],[2,7,-7,-3,-9,3,-10,1,9,-1,1,-1,-8,-9,6]],[[6,1,3,6,-2,6,-4,2,-10,7,1,-7,-1,7,-7],[-1,2,-6,-9,-1,-7,8,-7,7,3,-1,4,-7,2,-6],[-8,3,8,-6,-2,-7,6,-10,-10,-10,-5,-9,8,3,-1]],[[-10,7,-8,-3,-1,1,-3,5,-10,4,-8,-1,-7,5,9],[-10,-7,-2,-1,1,-9,-10,-1,-8,10,3,1,8,-2,-8],[1,2,7,4,9,10,10,-2,6,6,-2,-5,4,2,6]]], dtype = "uint32")#candidate|2392|(14, 3, 15)|const|uint32
bop_2393 = relay.right_shift(call_2387.astype('uint64'), relay.reshape(const_2392.astype('uint64'), relay.shape_of(call_2387))) # shape=(14, 3, 15)
bop_2396 = relay.right_shift(call_2388.astype('uint64'), relay.reshape(const_2392.astype('uint64'), relay.shape_of(call_2388))) # shape=(14, 3, 15)
func_1056_call = mod.get_global_var('func_1056')
func_1059_call = mutated_mod.get_global_var('func_1059')
var_2403 = relay.var("var_2403", dtype = "float32", shape = (280,))#candidate|2403|(280,)|var|float32
call_2402 = relay.TupleGetItem(func_1056_call(relay.reshape(var_2403.astype('float32'), [2, 10, 14])), 0)
call_2404 = relay.TupleGetItem(func_1059_call(relay.reshape(var_2403.astype('float32'), [2, 10, 14])), 0)
output = relay.Tuple([bop_2393,call_2402,var_2403,])
output2 = relay.Tuple([bop_2396,call_2404,var_2403,])
func_2405 = relay.Function([var_2403,], output)
mod['func_2405'] = func_2405
mod = relay.transform.InferType()(mod)
mutated_mod['func_2405'] = func_2405
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2406 = relay.var("var_2406", dtype = "float32", shape = (280,))#candidate|2406|(280,)|var|float32
func_2405_call = mutated_mod.get_global_var('func_2405')
call_2407 = func_2405_call(var_2406)
output = call_2407
func_2408 = relay.Function([var_2406], output)
mutated_mod['func_2408'] = func_2408
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2441 = relay.var("var_2441", dtype = "int16", shape = ())#candidate|2441|()|var|int16
var_2442 = relay.var("var_2442", dtype = "int16", shape = (11, 11, 11))#candidate|2442|(11, 11, 11)|var|int16
bop_2443 = relay.right_shift(var_2441.astype('int16'), var_2442.astype('int16')) # shape=(11, 11, 11)
bop_2447 = relay.less(bop_2443.astype('bool'), var_2441.astype('bool')) # shape=(11, 11, 11)
output = bop_2447
output2 = bop_2447
func_2452 = relay.Function([var_2441,var_2442,], output)
mod['func_2452'] = func_2452
mod = relay.transform.InferType()(mod)
var_2453 = relay.var("var_2453", dtype = "int16", shape = ())#candidate|2453|()|var|int16
var_2454 = relay.var("var_2454", dtype = "int16", shape = (11, 11, 11))#candidate|2454|(11, 11, 11)|var|int16
output = func_2452(var_2453,var_2454,)
func_2455 = relay.Function([var_2453,var_2454,], output)
mutated_mod['func_2455'] = func_2455
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_2457 = relay.TupleGetItem(func_2010_call(), 1)
call_2458 = relay.TupleGetItem(func_2011_call(), 1)
output = relay.Tuple([call_2457,])
output2 = relay.Tuple([call_2458,])
func_2459 = relay.Function([], output)
mod['func_2459'] = func_2459
mod = relay.transform.InferType()(mod)
mutated_mod['func_2459'] = func_2459
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2459_call = mutated_mod.get_global_var('func_2459')
call_2460 = func_2459_call()
output = call_2460
func_2461 = relay.Function([], output)
mutated_mod['func_2461'] = func_2461
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2464 = relay.var("var_2464", dtype = "uint8", shape = (13, 16, 3))#candidate|2464|(13, 16, 3)|var|uint8
var_2465 = relay.var("var_2465", dtype = "uint8", shape = (13, 16, 3))#candidate|2465|(13, 16, 3)|var|uint8
bop_2466 = relay.bitwise_xor(var_2464.astype('uint8'), relay.reshape(var_2465.astype('uint8'), relay.shape_of(var_2464))) # shape=(13, 16, 3)
func_2405_call = mod.get_global_var('func_2405')
func_2408_call = mutated_mod.get_global_var('func_2408')
var_2489 = relay.var("var_2489", dtype = "float32", shape = (280,))#candidate|2489|(280,)|var|float32
call_2488 = relay.TupleGetItem(func_2405_call(relay.reshape(var_2489.astype('float32'), [280,])), 2)
call_2490 = relay.TupleGetItem(func_2408_call(relay.reshape(var_2489.astype('float32'), [280,])), 2)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_2504 = func_1817_call()
call_2505 = func_1817_call()
func_2142_call = mod.get_global_var('func_2142')
func_2144_call = mutated_mod.get_global_var('func_2144')
var_2518 = relay.var("var_2518", dtype = "float64", shape = (396, 1))#candidate|2518|(396, 1)|var|float64
call_2517 = relay.TupleGetItem(func_2142_call(relay.reshape(var_2518.astype('float64'), [396,])), 1)
call_2519 = relay.TupleGetItem(func_2144_call(relay.reshape(var_2518.astype('float64'), [396,])), 1)
uop_2524 = relay.sinh(var_2518.astype('float32')) # shape=(396, 1)
func_2142_call = mod.get_global_var('func_2142')
func_2144_call = mutated_mod.get_global_var('func_2144')
call_2534 = relay.TupleGetItem(func_2142_call(relay.reshape(call_2517.astype('float64'), [396,])), 0)
call_2535 = relay.TupleGetItem(func_2144_call(relay.reshape(call_2517.astype('float64'), [396,])), 0)
func_1888_call = mod.get_global_var('func_1888')
func_1893_call = mutated_mod.get_global_var('func_1893')
const_2545 = relay.const([[-8.145116,2.962020],[0.439135,2.658720],[3.849525,-1.258283],[-6.595470,-5.034952],[-4.781395,7.024892]], dtype = "float32")#candidate|2545|(5, 2)|const|float32
const_2546 = relay.const([False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,True,True,True,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,True,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,True,False,True,False,False,True,False,True,False,True,False,False,False,False,False,False,True,True,True,True,False,False,False,True,False,False,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,True,False,True,False,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,False,True,False,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,True,False,False,True,False,True,False,False,False,True,False,True,True,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,False,True,False,True,False,False,False,False,False,True,False,True,False,False,False,True,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,True,False,True,False,True,True,False,True,True,True,False,False,False,True,True,True], dtype = "bool")#candidate|2546|(525,)|const|bool
call_2544 = relay.TupleGetItem(func_1888_call(relay.reshape(const_2545.astype('float32'), [1, 2, 5]), relay.reshape(call_2488.astype('float32'), [280,]), relay.reshape(const_2546.astype('bool'), [525,]), ), 1)
call_2547 = relay.TupleGetItem(func_1893_call(relay.reshape(const_2545.astype('float32'), [1, 2, 5]), relay.reshape(call_2488.astype('float32'), [280,]), relay.reshape(const_2546.astype('bool'), [525,]), ), 1)
uop_2566 = relay.acosh(uop_2524.astype('float32')) # shape=(396, 1)
func_1780_call = mod.get_global_var('func_1780')
func_1783_call = mutated_mod.get_global_var('func_1783')
const_2572 = relay.const([True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,True,False,False,False,False,False,True,False,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,True,False,False,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,False,False,False,True,True,True,True,True,True,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,False,False,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,False,False,True,False,True,True,True,False,False,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,True,True,True,False,True], dtype = "bool")#candidate|2572|(300,)|const|bool
call_2571 = relay.TupleGetItem(func_1780_call(relay.reshape(call_2517.astype('float64'), [396,]), relay.reshape(const_2572.astype('bool'), [300,]), ), 3)
call_2573 = relay.TupleGetItem(func_1783_call(relay.reshape(call_2517.astype('float64'), [396,]), relay.reshape(const_2572.astype('bool'), [300,]), ), 3)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_2575 = relay.TupleGetItem(func_1040_call(), 0)
call_2576 = relay.TupleGetItem(func_1042_call(), 0)
func_1322_call = mod.get_global_var('func_1322')
func_1326_call = mutated_mod.get_global_var('func_1326')
call_2579 = relay.TupleGetItem(func_1322_call(relay.reshape(call_2534.astype('bool'), [14, 3, 15]), relay.reshape(const_2546.astype('bool'), [525,]), ), 0)
call_2580 = relay.TupleGetItem(func_1326_call(relay.reshape(call_2534.astype('bool'), [14, 3, 15]), relay.reshape(const_2546.astype('bool'), [525,]), ), 0)
uop_2586 = relay.erf(uop_2524.astype('float32')) # shape=(396, 1)
output = relay.Tuple([bop_2466,call_2488,var_2489,call_2504,call_2517,call_2534,call_2544,const_2545,const_2546,uop_2566,call_2571,const_2572,call_2575,call_2579,uop_2586,])
output2 = relay.Tuple([bop_2466,call_2490,var_2489,call_2505,call_2519,call_2535,call_2547,const_2545,const_2546,uop_2566,call_2573,const_2572,call_2576,call_2580,uop_2586,])
func_2588 = relay.Function([var_2464,var_2465,var_2489,var_2518,], output)
mod['func_2588'] = func_2588
mod = relay.transform.InferType()(mod)
var_2589 = relay.var("var_2589", dtype = "uint8", shape = (13, 16, 3))#candidate|2589|(13, 16, 3)|var|uint8
var_2590 = relay.var("var_2590", dtype = "uint8", shape = (13, 16, 3))#candidate|2590|(13, 16, 3)|var|uint8
var_2591 = relay.var("var_2591", dtype = "float32", shape = (280,))#candidate|2591|(280,)|var|float32
var_2592 = relay.var("var_2592", dtype = "float64", shape = (396, 1))#candidate|2592|(396, 1)|var|float64
output = func_2588(var_2589,var_2590,var_2591,var_2592,)
func_2593 = relay.Function([var_2589,var_2590,var_2591,var_2592,], output)
mutated_mod['func_2593'] = func_2593
mutated_mod = relay.transform.InferType()(mutated_mod)
const_2613 = relay.const([[[5,4,-1,-6,2,-9,-5,-3,-1,-3,2,5,-6,-7],[-9,6,4,-10,9,-8,-9,9,9,-10,-4,9,-3,-5],[9,1,-2,-4,9,3,-1,-8,-9,-2,-8,1,7,9],[4,-10,-6,1,-10,-4,10,-6,8,1,2,8,-10,-3]],[[8,-9,-5,-5,2,9,-2,2,10,-5,1,-6,3,-4],[-2,10,-8,-2,7,-4,-5,10,3,3,9,2,6,-4],[3,-10,4,6,-10,-5,-8,-6,9,2,10,-7,-3,-1],[-10,-10,5,-1,1,-3,8,7,-4,-10,-9,-8,8,-7]],[[6,-2,7,9,-3,10,-8,2,-10,3,-2,-10,-7,-1],[4,8,8,-6,3,6,8,7,-1,-3,9,-9,-10,3],[7,-2,2,3,-9,6,8,7,9,3,6,3,3,8],[10,9,-5,-10,-1,10,6,4,-7,-10,-7,-6,-1,10]]], dtype = "int16")#candidate|2613|(3, 4, 14)|const|int16
var_2614 = relay.var("var_2614", dtype = "int16", shape = (3, 4, 14))#candidate|2614|(3, 4, 14)|var|int16
bop_2615 = relay.equal(const_2613.astype('bool'), relay.reshape(var_2614.astype('bool'), relay.shape_of(const_2613))) # shape=(3, 4, 14)
func_1780_call = mod.get_global_var('func_1780')
func_1783_call = mutated_mod.get_global_var('func_1783')
const_2619 = relay.const([-4.326563,1.468374,3.219218,-5.658038,6.874197,7.319814,3.734144,5.401771,-6.328798,-7.056957,-4.510272,-1.308420,-4.321385,-2.478158,3.306250,3.037670,-9.949468,2.779886,2.389259,4.038675,7.322810,-6.021518,0.130797,1.057279,-9.511017,-6.442385,-1.523579,9.900440,4.012956,-1.231819,-5.256834,-2.219306,-1.870515,-0.530090,5.131507,-2.287423,-1.086421,-9.265511,6.034924,5.295757,5.646225,-0.353632,8.297294,-3.944626,0.137222,0.618291,3.550731,-3.751794,9.252717,1.755030,1.067379,3.998121,-1.282976,6.130930,-4.196569,3.596793,-1.037062,1.186160,0.225315,-5.511181,-8.826616,-2.210004,8.787751,-2.029035,-2.026789,-5.856415,3.443366,6.442515,7.176778,1.932761,-1.699957,2.857858,9.421795,-6.148167,-1.569067,4.609639,-7.824002,-0.477033,6.078701,2.609773,-6.067447,1.688814,8.218704,-5.154509,6.507883,-1.861016,-1.740012,-7.548471,-7.311320,3.504450,5.212400,-5.746997,-7.383283,7.886430,6.460915,0.436561,-7.090560,1.420655,-1.431651,-9.124458,-6.975899,6.401675,-3.632901,-7.513168,-5.045968,-4.599786,-1.473979,5.547509,5.020259,-9.630305,9.649996,8.867417,-4.524980,-4.658658,-6.289509,-3.084717,0.262915,8.379798,4.247601,0.778253,2.318623,9.641264,-6.976878,1.741191,-0.377875,-1.122569,5.499957,4.350641,-7.054502,-6.208490,9.905156,5.400282,-6.858940,-5.536495,-7.423229,9.087643,6.281512,-5.138614,-2.662060,-5.527595,0.509746,-1.354858,-1.845955,8.572189,5.453025,4.279369,-2.112307,-0.539035,8.221203,3.370680,-5.541908,-5.940611,1.821584,5.314297,-2.128803,-1.204906,-1.787455,-1.535136,9.098045,8.328192,-7.562904,5.953937,-5.571200,4.444116,-7.383223,0.993663,-2.029826,4.354573,-1.698979,5.619834,-6.491792,1.262201,-7.984921,0.881602,3.927713,1.126046,9.378253,-3.604990,-7.808208,8.969224,-4.397699,2.371996,-2.885203,6.114323,6.632506,1.374929,-6.656248,-9.322346,7.481407,-2.385247,-7.877278,-7.014669,-4.641774,6.133154,-1.912890,-3.339704,-9.969519,8.261996,-5.289893,4.245856,5.483294,0.804439,0.401508,9.605991,8.779793,7.873604,3.128422,1.873316,6.701657,-3.419191,3.398378,-7.614511,-6.959163,7.829286,-3.252677,-6.833048,3.375419,-5.251019,4.268005,9.622860,5.460844,-5.468684,-6.614698,0.461941,5.673095,-7.747146,-4.597902,-7.500549,-2.010621,9.726292,-7.976759,3.279487,6.946661,5.121974,0.615682,1.510975,4.981405,9.471505,8.860485,9.404339,-7.220342,9.908493,5.650103,4.785970,6.870319,-1.609656,-6.516929,-7.879947,6.718114,-0.995573,-3.027894,-2.211927,2.359491,-6.354433,-1.915062,3.347324,0.435480,3.930989,-0.055629,-9.787654,0.570378,-9.227043,-9.951604,1.652654,-1.839249,-7.486235,5.925762,-4.020147,-8.749658,5.808015,4.513735,5.564796,4.438597,4.958239,9.941981,-9.291391,-3.925730,-0.066994,3.971409,6.270671,9.843474,-9.432617,-2.321229,-1.987691,7.145947,4.837523,-2.527527,4.414634,1.703739,-0.800172,3.918379,9.520666,7.944584,-0.224449,4.294852,-6.856022,-3.996046,0.989737,1.546262,0.331184,8.292636,7.008161,-9.038765,3.644395,3.920486,-3.597119,-8.239836,3.642121,-3.659330,-1.379962,1.260078,-1.934248,-7.937071,-5.404216,2.988676,-1.568873,-6.281517,4.658484,2.028518,-1.140170,-6.881089,0.286063,-9.272074,-6.705907,-6.134939,-8.436063,1.037478,4.196358,-4.183402,0.605030,-0.729042,-0.390123,-4.066859,0.018928,-9.968184,-1.384654,-2.424860,-1.088454,-1.252770,2.073059,8.710144,-2.000438,6.263118,-6.379080,1.545959,5.400865,-8.260158,-7.927063,2.345983,-8.704556,5.294866,-3.535882,-7.616948,-4.136103,9.783957,4.987562,8.597278,7.024548,-7.314127,-3.825486,-2.296712,0.865270,0.778785,4.906002,0.481788,0.443554,-4.689292,-3.609322,-2.576406,-9.600729,4.136721,-0.986854,6.705421,0.428473,-3.899538,-3.421348,1.151710,9.170367,4.599417,-3.317858,-0.492657,-6.005365,9.539013,5.393633,8.000716,-8.916829,6.836817,-4.335804,-9.486722,-8.328183,5.133264,6.114303,-8.854145,-3.665604,9.740462,-5.877352], dtype = "float64")#candidate|2619|(396,)|const|float64
var_2620 = relay.var("var_2620", dtype = "bool", shape = (300,))#candidate|2620|(300,)|var|bool
call_2618 = relay.TupleGetItem(func_1780_call(relay.reshape(const_2619.astype('float64'), [396,]), relay.reshape(var_2620.astype('bool'), [300,]), ), 1)
call_2621 = relay.TupleGetItem(func_1783_call(relay.reshape(const_2619.astype('float64'), [396,]), relay.reshape(var_2620.astype('bool'), [300,]), ), 1)
output = relay.Tuple([bop_2615,call_2618,const_2619,var_2620,])
output2 = relay.Tuple([bop_2615,call_2621,const_2619,var_2620,])
func_2629 = relay.Function([var_2614,var_2620,], output)
mod['func_2629'] = func_2629
mod = relay.transform.InferType()(mod)
var_2630 = relay.var("var_2630", dtype = "int16", shape = (3, 4, 14))#candidate|2630|(3, 4, 14)|var|int16
var_2631 = relay.var("var_2631", dtype = "bool", shape = (300,))#candidate|2631|(300,)|var|bool
output = func_2629(var_2630,var_2631,)
func_2632 = relay.Function([var_2630,var_2631,], output)
mutated_mod['func_2632'] = func_2632
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2787 = relay.var("var_2787", dtype = "float64", shape = (15, 15, 12))#candidate|2787|(15, 15, 12)|var|float64
uop_2788 = relay.cosh(var_2787.astype('float64')) # shape=(15, 15, 12)
output = relay.Tuple([uop_2788,])
output2 = relay.Tuple([uop_2788,])
func_2795 = relay.Function([var_2787,], output)
mod['func_2795'] = func_2795
mod = relay.transform.InferType()(mod)
mutated_mod['func_2795'] = func_2795
mutated_mod = relay.transform.InferType()(mutated_mod)
var_2796 = relay.var("var_2796", dtype = "float64", shape = (15, 15, 12))#candidate|2796|(15, 15, 12)|var|float64
func_2795_call = mutated_mod.get_global_var('func_2795')
call_2797 = func_2795_call(var_2796)
output = call_2797
func_2798 = relay.Function([var_2796], output)
mutated_mod['func_2798'] = func_2798
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_2889 = relay.TupleGetItem(func_1084_call(), 0)
call_2890 = relay.TupleGetItem(func_1086_call(), 0)
output = call_2889
output2 = call_2890
func_2894 = relay.Function([], output)
mod['func_2894'] = func_2894
mod = relay.transform.InferType()(mod)
output = func_2894()
func_2895 = relay.Function([], output)
mutated_mod['func_2895'] = func_2895
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_2902 = func_2045_call()
call_2903 = func_2045_call()
output = call_2902
output2 = call_2903
func_2910 = relay.Function([], output)
mod['func_2910'] = func_2910
mod = relay.transform.InferType()(mod)
mutated_mod['func_2910'] = func_2910
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2910_call = mutated_mod.get_global_var('func_2910')
call_2911 = func_2910_call()
output = call_2911
func_2912 = relay.Function([], output)
mutated_mod['func_2912'] = func_2912
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1612_call = mutated_mod.get_global_var('func_1612')
call_2955 = relay.TupleGetItem(func_1611_call(), 0)
call_2956 = relay.TupleGetItem(func_1612_call(), 0)
output = call_2955
output2 = call_2956
func_2965 = relay.Function([], output)
mod['func_2965'] = func_2965
mod = relay.transform.InferType()(mod)
mutated_mod['func_2965'] = func_2965
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2965_call = mutated_mod.get_global_var('func_2965')
call_2966 = func_2965_call()
output = call_2966
func_2967 = relay.Function([], output)
mutated_mod['func_2967'] = func_2967
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_2973 = relay.TupleGetItem(func_1430_call(), 0)
call_2974 = relay.TupleGetItem(func_1432_call(), 0)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_2991 = relay.TupleGetItem(func_2351_call(), 0)
call_2992 = relay.TupleGetItem(func_2352_call(), 0)
output = relay.Tuple([call_2973,call_2991,])
output2 = relay.Tuple([call_2974,call_2992,])
func_2993 = relay.Function([], output)
mod['func_2993'] = func_2993
mod = relay.transform.InferType()(mod)
mutated_mod['func_2993'] = func_2993
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mutated_mod.get_global_var('func_2993')
call_2994 = func_2993_call()
output = call_2994
func_2995 = relay.Function([], output)
mutated_mod['func_2995'] = func_2995
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_2996 = relay.TupleGetItem(func_2351_call(), 0)
call_2997 = relay.TupleGetItem(func_2352_call(), 0)
uop_2998 = relay.rsqrt(call_2996.astype('float32')) # shape=(14, 3, 15)
uop_3000 = relay.rsqrt(call_2997.astype('float32')) # shape=(14, 3, 15)
const_3018 = relay.const([[[-9.566372,6.119825,-3.290324,6.378418,3.351441,3.000237,-9.067874,-4.319119,-5.680600,6.085529,-4.800497,-0.492140,5.557303,1.542743,3.929747],[-8.606212,6.423064,-2.144849,4.711489,-7.553011,9.691948,8.219839,-9.880594,-8.057240,-9.927135,-4.852242,-9.675475,8.561419,2.445596,-3.871798],[-2.607096,6.352027,9.705592,4.830324,3.612790,1.097673,0.088404,4.909791,-6.466483,-3.846925,0.556382,0.894857,5.776935,5.975821,-2.401052]],[[9.898590,6.681018,-7.861989,3.623638,9.195005,9.795829,1.219986,0.654938,4.291543,-5.059626,-2.346244,-9.410004,3.211297,-4.990903,-3.749640],[7.127644,1.074303,-6.124246,9.407492,3.059381,7.964840,0.669805,-4.324752,5.735855,1.490364,7.356313,2.844316,2.952966,-9.668378,-2.372506],[-3.233292,-0.080369,-6.806638,2.252863,-8.499022,-0.916214,-2.800021,-5.332152,-9.269473,-6.902193,-8.490351,3.675512,9.170307,-4.527944,-5.406091]],[[-0.988118,-9.703434,3.219475,-1.376662,-8.907056,9.218826,-8.030288,8.800413,-9.341701,-4.242755,4.500653,0.509625,-9.300661,1.861722,-7.010047],[3.119613,3.722549,7.123660,-1.909950,2.475253,1.890851,2.738479,-1.288869,-4.052334,-0.025754,5.019621,4.383754,-1.027945,8.252352,1.350810],[-9.655796,4.078191,-2.167889,-7.510003,-2.113781,-0.143485,-2.412243,1.911018,-0.915522,-1.676552,-0.916824,-1.192798,-3.295340,5.700597,-4.650850]],[[2.933798,-3.750525,-9.204992,7.196112,4.520461,3.023630,4.466878,-7.675238,-6.512580,9.697882,8.569096,8.651071,4.944247,6.544735,4.567001],[2.628771,-9.062193,9.678645,8.796072,5.813134,-4.883049,-9.579888,-4.823860,-9.991672,5.267594,0.014952,1.962074,-1.194942,-9.803597,-0.950522],[6.267415,-4.338545,5.831619,0.506635,4.952658,9.417556,7.171709,5.781530,-5.071246,-2.753315,3.092019,2.403888,-7.413042,-7.573215,2.533030]],[[5.531249,-4.482000,-0.052443,0.782729,-4.788555,-9.957133,5.909387,2.263559,9.380176,-6.590401,6.624546,-3.071670,8.391932,-5.070423,2.786808],[-3.409711,1.949399,8.423287,-2.719387,4.181822,6.197550,-3.307269,9.388759,6.126301,-2.186993,-9.654782,-4.186446,-7.887471,-3.988751,4.884870],[-4.471100,-4.369895,-1.081356,0.100561,-6.828816,-7.682239,-1.700854,-6.514546,-4.759149,-0.926768,-0.432308,6.315902,9.609652,-2.710502,-1.451835]],[[-6.123254,6.154017,-2.835616,-2.272098,-3.851200,-4.819008,-5.037907,7.459374,-6.460207,-9.107205,-3.724521,-2.511107,7.273936,1.772878,1.985780],[0.691375,-1.534883,-4.056001,3.486239,-4.713483,2.974194,-1.073100,6.372595,9.963507,7.314361,7.832106,-2.437260,8.369102,9.721271,9.877968],[6.672724,-1.467602,3.035012,-1.181470,3.064890,-6.379788,-2.443461,-7.036902,-7.512014,2.419844,-4.226381,-4.687043,-1.300081,-6.995040,-4.610853]],[[-9.802612,8.750275,-0.761684,1.703948,7.612605,7.795777,-2.938872,-5.941575,-5.069337,-8.556743,-8.062468,-1.723872,3.822810,5.575837,-2.234678],[8.463571,3.714002,-8.036518,3.638733,-4.974543,-6.796344,-4.945593,6.349411,-2.882277,5.304868,-6.851136,8.685216,-9.662487,8.153211,-1.962430],[-3.128391,1.127887,-2.742363,7.164735,4.371448,-8.030790,5.606940,-2.648565,2.418037,-8.510571,5.218753,9.549872,0.087305,1.565773,9.947042]],[[2.717222,5.629475,2.726638,-0.747980,5.968284,-6.094814,1.484346,-5.753271,5.101319,-2.770790,8.369351,-5.406216,-4.687343,-9.098201,-6.722808],[-0.702866,7.590742,-2.343876,2.861761,4.494047,9.176768,6.587988,-3.715523,-0.759951,9.520615,1.892462,9.642528,9.784585,-3.389513,2.042259],[9.822019,-0.358088,-1.518535,2.696782,6.128228,-7.261856,3.812602,0.072276,-4.031353,9.044846,6.572055,-8.131722,-7.619000,-8.278049,4.877444]],[[9.927782,4.785369,-3.825087,6.033665,-7.333618,-4.599329,7.211604,-0.354628,0.168856,-8.569272,-0.485041,-8.971103,-2.851846,5.033491,0.928559],[6.946400,6.554333,-7.296474,-2.621862,-1.009608,-5.134451,6.494460,-2.474082,-0.933629,-7.276130,-4.346434,-9.716562,2.772005,5.149476,-0.988357],[-2.687312,7.177150,-4.088812,0.910679,3.063699,4.298990,-3.310838,7.232987,-3.801932,2.376820,6.228906,-9.430977,-6.459987,-1.745447,-1.738596]],[[-7.543715,-4.109877,-9.341109,4.534437,5.042378,8.515474,-6.318418,-4.806331,-4.316219,3.990631,3.985004,2.708993,1.754994,-1.340815,0.474747],[-6.737553,2.940833,-2.380374,5.913230,0.884974,-1.572813,-4.352984,-0.103693,1.100622,2.302326,-4.190611,3.560215,-3.358941,8.054507,-2.274629],[5.373927,-9.368430,-0.378156,2.346422,-3.954081,-1.592808,9.754890,2.959711,3.312489,0.029283,-5.636123,-0.090959,9.671972,-2.067930,0.694266]],[[-5.575352,6.614207,9.495263,6.047546,4.080762,4.391123,-1.326815,-0.075098,-3.183260,-5.275116,6.200087,-0.298035,-0.814935,-4.312018,-8.071367],[-0.322878,3.255122,-5.193981,3.294164,9.454891,5.310141,-4.750606,5.610871,-5.116310,1.916232,7.249728,7.597624,-8.780118,-6.471105,-7.252134],[-1.857959,5.336520,-6.403914,-3.933474,9.706644,-8.904518,-6.734753,-8.898694,-4.929617,3.895849,-5.094169,-4.597542,-9.937225,7.537441,0.342689]],[[-5.508651,-3.273081,6.109685,8.068815,-3.834949,1.401647,8.187576,-4.809850,-5.401285,-3.164004,-8.812171,-0.491324,-6.087298,3.366066,1.249923],[6.493874,-4.467416,0.797421,-4.935352,0.279051,1.081774,-8.225620,-7.294760,9.435038,2.702211,-5.789824,-3.427430,-2.569860,-5.485024,-0.839479],[-0.466294,7.379645,-9.377415,3.201356,3.466505,3.511338,2.017447,1.593854,-3.295907,-9.005914,3.178300,9.251382,-9.077165,-3.576701,6.304606]],[[-6.853427,9.846138,-5.474127,0.317298,-4.189423,-2.986844,1.523215,7.052477,5.915680,4.605785,5.110855,4.444605,-5.363478,-7.876801,-0.449218],[-8.416818,-8.231021,-4.944660,7.883833,-9.021205,-0.838920,4.054899,-4.041009,-7.445939,5.500381,-9.201759,-9.827833,0.903836,1.193161,-1.903782],[-5.124389,-4.593505,-7.773809,3.863290,-8.271133,8.738688,1.378632,3.934741,-4.698128,4.343534,1.203011,-6.290658,6.118993,5.696566,-4.759089]],[[-7.659065,-0.912593,8.266853,9.848026,-1.237248,-5.353525,-2.840613,-1.530539,6.039414,-4.102014,-2.915768,-6.358182,8.471637,8.136206,-6.177468],[-9.771213,-4.478089,-7.087978,4.201574,-7.775763,6.381308,-0.635791,-0.861868,2.929652,9.461624,0.098817,-9.299665,-8.606176,7.378952,-1.576742],[7.859838,0.611917,9.913824,8.237981,4.983088,-2.469836,-5.025882,2.260348,6.289193,7.831049,-7.539683,3.565835,-7.368721,-6.325241,6.536698]]], dtype = "float32")#candidate|3018|(14, 3, 15)|const|float32
bop_3019 = relay.add(uop_2998.astype('uint64'), relay.reshape(const_3018.astype('uint64'), relay.shape_of(uop_2998))) # shape=(14, 3, 15)
bop_3022 = relay.add(uop_3000.astype('uint64'), relay.reshape(const_3018.astype('uint64'), relay.shape_of(uop_3000))) # shape=(14, 3, 15)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_3031 = relay.TupleGetItem(func_2198_call(), 0)
call_3032 = relay.TupleGetItem(func_2200_call(), 0)
func_2588_call = mod.get_global_var('func_2588')
func_2593_call = mutated_mod.get_global_var('func_2593')
const_3045 = relay.const([-6,-3,8,-10,4,-9,-8,9,-6,7,-3,-10,4,-3,6,8,-4,7,-10,-8,-4,3,9,-7,1,10,-1,-7,10,3,7,-8,-4,-3,-3,-9,2,-10,6,-6,1,10,-4,1,8,-2,5,6,-6,-4,-1,-5,-6,4,2,10,-5,9,1,7,-4,-4,8,10,10,2,-6,-6,2,6,-1,-9,-9,8,-6,9,2,1,-3,6,5,-7,-5,-7,3,10,2,-10,8,10,1,-6,-3,6,7,1,8,-5,1,9,-5,-9,10,7,7,2,9,2,-4,-9,-8,5,8,-10,-1,-4,2,5,-1,10,2,-6,9,-4,-6,-5,3,4,-9,-2,-7,-9,8,-1,-8,6,2,-2,2,5,7,4,-10,-3,5,1,10,1,6,8,2,4,8,6,-2,-9,10,10,4,-1,9,-10,-2,8,2,1,-1,-9,-1,-10,7,1,-3,-7,6,-3,-10,5,-4,1,10,2,-7,10,-8,-10,-8,-2,1,7,9,-2,4,4,-2,-6,7,2,10,1,-10,3,-3,10,-4,3,6,-4,-5,-8,1,7,-3,3,1,-1,6,-1,-7,-3,8,6,-3,4,-9,5,8,10,-1,5,7,-4,-10,-2,-8,9,2,1,6,-3,2,4,10,-1,7,4,2,6,5,-10,-6,-10,-4,6,-8,2,-9,-10,-10,-9,-9,-10,-10,-4,6,-9,-10,-3,-10,4,-7,6,3,-6,-6,-2,9,7,-10,-4,2,-1,2,9,-2,-8,9,7,-1,-7,-8,-4,-2,-6,-10,1,6,8,-5,-10,8,-5,3,9,5,-2,6,1,5,-2,-10,10,-4,-5,-3,-3,-6,-8,-2,-4,-4,9,-10,-9,10,1,4,-9,8,-7,-1,-4,1,-6,8,10,-6,-3,1,-3,-3,2,-6,8,-5,8,9,2,1,-5,-10,2,-3,-4,5,7,4,7,-10,-5,-2,-2,-5,3,6,7,-10,-4,4,-1,-7,-8,10,10,-4,7,-10,-7,5,10,-7,-7,-8,1,-1,10,1,-7,-5,10,-4,7,6,-6,5,10,5,-8,8,-4,2,-7,1,-5,-10,8,-4,7,-9,8,-1,6,8,10,3,-7,5,9,7,-4,1,-3,9,2,5,3,-2,3,-1,8,-4,-9,8,-6,-4,-3,6,-9,-6,-4,2,-6,-6,-4,1,-3,8,5,-1,-2,5,9,1,-6,-8,-9,-6,5,-5,1,5,-2,-5,9,-2,-1,4,6,-6,4,1,-4,-8,10,-2,-1,4,-9,2,5,7,-9,-5,-10,-9,5,-8,8,-2,1,-1,10,-8,4,-5,4,-4,6,-1,-10,-1,-10,-6,6,9,1,-2,3,9,9,-6,-7,9,-8,2,-1,-5,-5,-9,8,-10,8,-9,1,-10,-2,-5,-7,-6,5,4,-2,-8,9,-10,5,-5,2,-6,2,3,-2,-4,-3,3,10,-7,-8,1,-10,4,9,-10,3,-1,-2,2,-3,1,9,-7,5,1,-6,-9,-1,4,2,2,10,4,-10,-3,3,10,-2,-10,8,8,-4,-10,10,9,-8,1,4,9,2,-6,10,6,2,6,-9,-4,1,-10,-10,7,9,7,3,-7,1,-9,-1,10,-3,3,-1,5,-1,-7,3,8,-1,-5,-2,-9,-6,-2,3,10,10], dtype = "uint8")#candidate|3045|(624,)|const|uint8
var_3046 = relay.var("var_3046", dtype = "float32", shape = (70, 4))#candidate|3046|(70, 4)|var|float32
const_3047 = relay.const([[5.936486,1.743547],[8.458480,4.043305],[-1.035872,7.672564],[2.727425,6.469052],[-0.123430,-4.960603],[-9.873513,9.104682],[7.207876,-5.883736],[-8.759093,-3.838668],[1.030874,0.443637],[-6.209883,4.221770],[2.146169,1.811024],[8.988825,6.991463],[-1.271753,-8.117335],[-7.083980,0.833864],[-8.985854,-9.786657],[6.953688,-1.499249],[-9.053904,6.349534],[-6.022984,-5.779045],[2.898408,5.337200],[-8.117962,-0.296456],[-0.331410,-2.267440],[-1.006494,-7.949985],[2.833552,8.777854],[6.447889,8.312062],[-9.974607,4.061238],[7.265686,-7.507422],[4.604521,9.745769],[-5.027510,-0.291214],[6.793556,2.717039],[-9.072564,-0.725462],[-3.256312,-7.090026],[-4.870638,-0.367217],[-3.624774,7.930158],[3.174952,-6.592832],[8.378836,-0.150818],[-3.766180,0.065935],[7.344326,9.847054],[-3.057133,6.276898],[-7.627090,8.328351],[4.369416,6.197498],[6.319381,-8.849677],[-6.067863,8.106560],[-1.436869,5.885542],[-2.646833,-7.970004],[5.338712,7.566276],[-5.780718,2.714010],[-3.272797,9.321112],[-6.779713,5.980457],[6.515425,-8.341138],[-5.040258,-5.978163],[3.733889,3.530210],[-6.431723,-8.852286],[-6.966892,4.159719],[-2.547028,1.364494],[3.231489,2.302595],[9.914497,3.416429],[-2.261864,-2.840997],[5.146304,3.201741],[-5.397286,-8.116899],[1.826085,-9.862292],[-8.540569,-6.648328],[-6.125770,5.422592],[-4.142267,6.704583],[3.469790,-5.760016],[-3.066214,3.956475],[5.417062,4.297772],[6.479142,-4.505681],[-4.609088,-3.611935],[4.631730,8.554107],[-7.158964,1.851894],[4.432462,-6.855936],[-6.737107,-7.354866],[0.318622,-9.468643],[0.747335,-3.600740],[-9.390177,4.923732],[-2.125571,1.152681],[-6.384116,2.650177],[-1.248840,3.844559],[-9.073708,-6.912721],[-7.690290,6.142126],[-1.759827,7.007185],[6.537989,8.164494],[-3.892794,-4.374665],[-1.057647,-8.975980],[1.218552,-8.150564],[8.984596,7.062288],[5.885784,-8.284127],[7.914471,-5.036080],[6.848398,5.801864],[0.617211,-4.966879],[2.440637,-3.993426],[6.127728,-5.200329],[0.229184,-6.424397],[-0.060965,-5.722482],[4.908456,2.814101],[-5.864748,2.477977],[7.809897,3.668458],[3.227859,4.073196],[-0.057592,-9.186471],[-9.439490,-1.971676],[0.222859,-5.031523],[9.159614,-6.320465],[9.124978,9.962130],[7.617302,-4.030275],[3.871880,6.241318],[2.074956,2.333756],[3.007846,5.027282],[-0.856627,8.527733],[-3.190778,2.246917],[-0.070910,6.723368],[2.795484,0.843910],[3.163172,-8.157169],[0.103641,8.160155],[-8.032454,6.770708],[-6.463133,8.734819],[-2.045427,1.962089],[9.756228,-9.313414],[-6.731658,8.274420],[-3.061471,-5.842496],[-3.977501,-4.760349],[-0.224386,9.054792],[-4.668233,-1.396489],[9.715684,2.294306],[-2.846482,4.805707],[2.489612,8.012894],[4.783765,-3.105158],[-7.674158,0.212896],[4.010038,-0.433384],[5.537947,-2.869716],[-1.083675,-0.489078],[-1.856027,-4.875620],[-0.932959,-3.380186],[0.034359,4.230049],[4.420936,5.859675],[-1.378595,-3.484021],[-7.657927,-0.617546],[-9.555331,-4.113404],[5.002137,8.326761],[-3.802833,4.960596],[4.546956,1.354142],[0.621711,7.604046],[-6.134383,-2.412666],[1.431394,-2.091066],[-2.538474,4.751063],[2.753591,1.949969],[-1.592187,-3.341678],[-8.156144,-3.366988],[-2.374829,4.562296],[-6.579871,-9.917546],[0.170339,-5.026629],[2.345521,-2.007533],[1.527786,1.796107],[2.077971,1.543598],[6.525072,1.473935],[3.725924,9.922928],[9.048481,-8.281986],[9.797535,-6.842745],[6.518023,4.121862],[1.294080,-6.518394],[2.651391,7.324749],[9.637973,-6.767914],[-4.486592,-7.124399],[0.936874,2.241618],[-9.387164,5.277490],[-0.022767,-2.774855],[-5.550454,5.251437],[-1.318092,-2.322294],[4.818590,-0.974837],[-6.414377,2.196385],[-3.305102,6.642509],[4.853763,-7.492658],[-7.469903,8.264886],[6.188185,-6.346053],[8.812984,1.557996],[-9.693132,1.054095],[5.618595,-7.800868],[-1.264753,6.493177],[9.017922,0.686986],[8.592742,1.321712],[4.023474,7.887548],[-1.425596,-0.119505],[5.557749,3.432575],[2.906449,6.563111],[2.527489,-4.775935],[3.832453,-4.941092],[-5.318281,8.923780],[-0.082452,2.115077],[5.514117,-1.670866],[1.287052,2.507539],[9.972511,-1.397733],[6.784262,6.072193],[2.862227,-6.923696],[4.025269,4.762948],[-9.963065,-0.888996],[3.379237,-1.065762],[-5.830286,9.255536],[7.481147,-4.455922],[4.784571,0.005342]], dtype = "float64")#candidate|3047|(198, 2)|const|float64
call_3044 = relay.TupleGetItem(func_2588_call(relay.reshape(const_3045.astype('uint8'), [13, 16, 3]), relay.reshape(const_3045.astype('uint8'), [13, 16, 3]), relay.reshape(var_3046.astype('float32'), [280,]), relay.reshape(const_3047.astype('float64'), [396, 1]), ), 13)
call_3048 = relay.TupleGetItem(func_2593_call(relay.reshape(const_3045.astype('uint8'), [13, 16, 3]), relay.reshape(const_3045.astype('uint8'), [13, 16, 3]), relay.reshape(var_3046.astype('float32'), [280,]), relay.reshape(const_3047.astype('float64'), [396, 1]), ), 13)
func_295_call = mod.get_global_var('func_295')
func_298_call = mutated_mod.get_global_var('func_298')
var_3050 = relay.var("var_3050", dtype = "uint8", shape = (168,))#candidate|3050|(168,)|var|uint8
call_3049 = relay.TupleGetItem(func_295_call(relay.reshape(var_3050.astype('uint8'), [12, 1, 14])), 0)
call_3051 = relay.TupleGetItem(func_298_call(relay.reshape(var_3050.astype('uint8'), [12, 1, 14])), 0)
func_2283_call = mod.get_global_var('func_2283')
func_2288_call = mutated_mod.get_global_var('func_2288')
var_3058 = relay.var("var_3058", dtype = "float32", shape = ())#candidate|3058|()|var|float32
const_3059 = relay.const([2.445911,8.386284,4.596385,-7.659523,-3.061772,-1.208685,4.148593,3.057246,4.679390,-4.496038,-8.949098,-4.944158,-9.039597,0.717379,-0.339777,6.332871,-6.350288,-1.407842,9.917297,7.629818,4.816088,-2.424865,-8.419435,-7.205688,-7.349689,6.825578,2.795951,-4.886179,-9.340992,2.035753,-6.154468,5.264765,0.903111,-5.673473,-0.707443,-2.549471,0.908395,9.027754,-4.455501,5.072189,-7.891013,-2.087016,2.201878,8.666733,-5.729472,-7.510532,2.506649,5.062013,-3.442540,-0.621048,3.332584,-2.788424,9.769630,3.874970,7.539013,-9.652488,4.815745,5.578370,-2.533262,-3.745598,7.597665,9.256198,-8.719588,1.085703,8.186860,-5.046908,3.843001,5.508848,-5.376844,-6.537793,-7.292409,2.170706,0.859848,-4.693906,5.627546,-7.854133,6.056751,5.366962,8.166762,-3.958375,-0.477159,7.586559,5.843839,-8.655866,3.076363,0.646124,-1.100291,7.992877,6.771946,3.443179,2.091527,0.508886,9.038112,-7.389477,-7.484355,5.377031,9.133143,-7.550393,-9.470589,-9.729383,3.324101,3.620395,-3.970317,-5.376868,-1.843053,-0.099072,7.738678,-9.545820,0.160755,9.656664,-2.749567,-2.440264,-7.551115,-2.134279,-9.068461,-7.084468,9.481482,9.299685,6.401690,6.663222,1.226411,0.794485,-3.320819,4.883220,-2.685047,4.734051,-8.068312,9.439509,-6.545022,8.269867,-1.877523,-1.887735,4.397995,-1.134192,3.475945,-4.899543,1.295209,-3.434387,3.671453,1.977176,-4.290479,-4.229214,9.434430,6.379338,-9.917412,-1.421675,3.693434,-0.968940,-0.827147,5.577129,-7.991433,-9.192565,7.959614,9.609506,-8.915418,-7.234437,9.474643,4.659169,-9.391117,-9.292810,4.347862,-0.710810,-1.452560,0.357519,8.657507,-4.551164,-9.752181,9.825827,0.590417,0.462707,-6.727832,7.839378,-1.627867,-2.163651,1.781434,5.923713,1.745157,5.200999,-5.632130,-5.130296,2.874600,-9.644071,8.934890,7.108187,-9.637695,-5.075476,8.501197,4.084406,0.381880,-1.906286,-3.288192,9.508600,7.621036,4.177199,-1.014744,4.563903,5.467207,8.514908,-0.619411,6.135924,2.360889,3.140178,0.019613,6.372727,-2.197586,-1.546480,3.618236,-5.760813,-4.848140,2.055368,6.926972,9.942098,-2.131616,1.794329,5.763692,5.364639,-5.725759,1.049854,2.639170,-4.497020,2.692753,6.841768,5.359537,5.288297,6.205676,-9.219708,-5.617681,2.520478,-8.257262,7.955824,-8.029976,3.398430,9.282177,-2.603913,3.060472,-7.127896,7.398852,2.443984,4.275137,0.955614,5.271307,1.329910,8.060832,-5.436120,8.453655,1.889043,7.626923,-6.188497,-0.428501,5.230553,-6.576136,-3.147905,3.714122,-6.137280,-6.569602,-7.670854,3.744144,0.553993,-1.148074,-7.011434,1.389583,7.076384,-9.929225,2.543606,0.945474,-3.599721,-5.197340,5.751356,7.748086,-2.951554,7.813318,3.248453,-2.318897,8.745056,5.885561,-0.482790,-4.272031,3.602200,-0.393674,9.333541,2.348268,0.358618,-1.164881,-6.937704,-0.480649,2.531522,9.802044,-0.303893,-3.341086,-1.503741,6.176552,-1.820046,1.974599,1.040726,7.344112,9.351139,-4.909437,-3.428721,4.676033,-3.658187,-9.968098,-7.268966,0.282449,6.520310,-6.340020,4.103739,7.448300,8.821529,8.820385,-6.696225,7.608478,1.687343,-0.429321,-5.852794,-4.936176,5.561015,7.599958,-2.212324,-3.617629,-5.853404,-4.497834,-2.883285,3.133081,-7.341378,-3.911701,5.816362,-3.593386,-2.549697,7.479014,-5.341415,7.630033,-1.935855,9.648535,7.391927,-4.248503,1.908077,8.781482,-9.458381,7.539987,9.717936,8.066833,-8.253033,-2.884630,-4.694777,6.003078,8.761783,-9.064116,6.709730,1.664243,8.305094,-6.413603,-6.289284,4.134849,6.024981,9.118978,-9.346827,9.104660,-2.692402,5.180639,8.404115,0.696545,-4.914251,-2.792954,-4.014587,-8.862025,-7.591959,-2.319451,4.741139,8.653757,-7.684023,4.895792,-5.065970,4.220204,-8.778263,9.546390,-5.319808,8.816934,3.683388,-0.490843,4.197034,2.139282,-2.127791,-4.281846,4.644225,-2.360234,-1.300893,4.669169,-9.632840,3.082914,1.186081,3.251875,8.117121,-1.854610,-8.762928,-1.050819,-8.233564,5.241488,9.322250,-3.601099,-8.506981,9.255768,-6.738019,1.374350,6.394973,-8.680187,5.652166,-5.364057,-1.239278,6.096688,-4.713229,-3.815244,-7.315422,3.873518,2.207185,-7.508927,-2.074642,-0.286863,-5.452787,1.557264,-6.903408,5.129652,7.243747,-4.118448,-9.276974,6.612619,-4.312067,2.952501,0.527921,-3.163800,-1.133840,-7.901129,-9.199453,-0.430372,-7.125243,6.513768,7.356710,6.577925,-1.920451,-2.745487,6.765544,4.268696,3.871810,-8.001680,7.835795,7.299759,-5.855981,-8.021415,-7.597180,4.361800,9.456976,1.633748,3.613765,8.077230,-1.713217,7.325011,1.244345,8.420207,0.509329,-4.462583,6.415207,2.623760,0.760072,-1.091562,-8.780350,8.143004,-2.455707,-7.225248,2.936691,-6.944835,9.492681,7.126619,-7.600861,9.647440,4.491444,9.493125,2.337780,-8.616461,-4.856355,-5.162007,-9.071050,-6.352462,-7.918343,2.017945,6.641232,5.332317,4.956868,1.015803,-1.118856,9.219646,-3.814527,-4.681045,3.350574,8.664201,0.259821,-4.052212,0.827674,5.308153,8.991837,8.840201,-0.799923,4.773518,8.244557,6.145920,8.909688,5.831025,5.560933,2.885044,-9.331017,3.974541,-4.385527,-0.392376,-7.672885,1.239535,-4.710187,-7.722769,-9.120620,-2.891024,4.704337,1.824507,-6.476473,-0.455796,-3.173094,4.393800,-1.247262,-9.255782,-0.731098,-4.049145,-3.296403,1.568021,-9.749404,5.153340,4.726580,8.248293,-6.535217,-9.268704,2.762983,-9.616661,-4.704415,9.268178,-8.630086,-8.545975,-1.099823,-1.217256,-1.474679,1.892256,7.678897,5.626399,-0.244810,4.947707,1.266177,7.601601,0.019505,-2.015344,0.004616,-9.689561,-1.424752,6.086941,-6.617568,2.275824,9.553000,1.221885,-1.462328,3.904689,0.368424,8.694612,-4.966326,-2.925129,-4.344389,-2.663634,-7.294621,-7.772698,3.924740,3.372843,5.125444,-4.571288,6.434727,0.310900,6.839526,-2.508387,-4.185395,8.923477,-2.181313,-4.492433,2.776930,8.940223,3.022520,-5.197539,5.334407,-7.695416,-8.416533,4.574696,1.723052,4.352149,0.913923,3.975987,8.720814,4.260858,-9.806675,6.588457,-7.670695,2.473444,-0.577399,-4.030246,6.182035,-7.076862,9.085121,0.003354,-2.738612,9.231567,-4.187587,9.988447,-0.057066,-0.888636,-9.681504,-3.173936,-5.392815], dtype = "float32")#candidate|3059|(616,)|const|float32
const_3060 = relay.const([True,True,True,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,False,True,True,True,False,True,False,True,False,True,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,True,True,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,False,False,False,False,True,True,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,False,True,True,True,False,True,True,False,True,False,False,True,True,True,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,True,False,False,False,True,True,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,False,True,False,True,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,False,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,False,False,True,True,False,True,True,True,False,True,True,True,True,False,True,False,False,False,False,True,True,False,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,False,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,True,False,True,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,False,True,True,False,True,True,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,True,False,False,False], dtype = "bool")#candidate|3060|(525,)|const|bool
call_3057 = relay.TupleGetItem(func_2283_call(relay.reshape(var_3058.astype('float32'), []), relay.reshape(const_3059.astype('float32'), [8, 7, 11]), relay.reshape(const_3059.astype('bool'), [8, 7, 11]), relay.reshape(const_3060.astype('bool'), [525,]), ), 0)
call_3061 = relay.TupleGetItem(func_2288_call(relay.reshape(var_3058.astype('float32'), []), relay.reshape(const_3059.astype('float32'), [8, 7, 11]), relay.reshape(const_3059.astype('bool'), [8, 7, 11]), relay.reshape(const_3060.astype('bool'), [525,]), ), 0)
uop_3062 = relay.atanh(bop_3019.astype('float64')) # shape=(14, 3, 15)
uop_3064 = relay.atanh(bop_3022.astype('float64')) # shape=(14, 3, 15)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_3069 = relay.TupleGetItem(func_1084_call(), 0)
call_3070 = relay.TupleGetItem(func_1086_call(), 0)
func_2092_call = mod.get_global_var('func_2092')
func_2095_call = mutated_mod.get_global_var('func_2095')
const_3076 = relay.const([True,False,True,False,True,True,True,False,False,False,True,True,False,False,True,True,True,True,False,False,False,False,True,False,True,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,False,True,False,False,False,True,True,False,True,True,True,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,False,True,True,True,True,True,False,False,False,False,False,True,True,False,True,True,False,False,False,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,True,True,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,False,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,True,True,True,False,False,True,True,False,True,False,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,False,False,True,True,True,False,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,True,True,True,False,False,False,True,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,False,True,True,False,False,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,False,False,True,False,False,False,True,True,False,False,True,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,False,False,False,False,False,False,False,False,False,True,False,True,False,False,False,False,False,False,True,True,False,True,True,True,False,False,False,True,True,False,False,True,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,False,False,False,False,False,True,True,False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,False,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,False,False,False,True,False,True,True,False,False,True,False,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,False,False,True,False,False,True,True,True,False,True,True,True,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,False,True,True,False,False,True,True,False,False,False,False,False,False,False,False,False,True,True,False,True,False,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,False,True,False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,True,False,True,True,False,False,False,True,True,False,False,True,True,False,True,True,True,False,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,False,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,True,False,False,True,True,True,False,False,True,True,True,True,True,True,False,False,False,False,True,True,True,False,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,True,True,True,False,False,False,False,False,False,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,False,False,False,False,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,False,True,False,True,False,False,True,True,False,False,True,False,True,True,False,True,False,False,True,True,True,False,False,True,False,True,True,True,True,False,False,True,True,False,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,True,False,False,False,True,True,True,False,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,False,True,True,True,False,True,False,True,False,True,False,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,True,False,False,False,False,True,True,False,False,True,True,False,True,False,True,True,True,False,False,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,True,True,True,True,False,False,False,True,True,False,True,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,True,True,True,True,True,True,False,True,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,True,False,False,False,False,False,True,True,False,True,True,True,True,True,False,False,True,False,False,False,True,True,True,True,False,True,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,False,True,True,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,True,False,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,True,True,False,False,False,False,True,False,False,True,True,False,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,False,False,True,True,False,False,False,False,False,True,True,False,True,True,True,False,True,True,False,True,True,True,False,False,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,False,False,True,False,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,True,False,False,True,True,False,False,True,True,False,False,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,False,False,False,True,True,True,False,False,False,True,False,True,True,True,True,False,True,False,True,True,False,True,True,False,False,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,True,True,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,True,False,False,False,False,False,False,True,False,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,True,False,False,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,False,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,False,False,False,True,False,True,True,True,True,True,True,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,False,True,False,False,False,True,False,False,False,False,True,True,False,False,True,True,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,True,False,True,False,False,True,True,True,False,False,False,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,True,False,True,True,True,False,True,False,False,False,True,False,True,True,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,True,True,True,True,True,True,True,False,False,True,False,True,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,False,True,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,True,False,True,False,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,False,True,False,False,True,True,False,True,True,False,True,True,False,True,False,True,False,False,True,False,False,True,False,True,True,True,False,True,False,False,False,False,True,False,True,True,False,True,False,True,True,False,False,False,True,False,True,True,True,False,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,True,True,False,True,True,True,True,False,True,False,False,True,False,True,True,False,False,False,True,True,True,False,True,False,False,True,True,False,True,True,False,False,False,False,True,False,True,False,False,False,True,True,True,True,False,False,True,False,False,False,False,True,False,True,False,True,False,True,True,True,False,True,True,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,True,True,False,True,True,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,False,False,False,False,False,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,False,True,True,False,True,True,True,True,False,False,True,True,False,False,False,False,False,False,True,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,False,True,False,False,False,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,False,False,True,False,False,False,True,False,False,True,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,True,True,True,True,True,False,True,True,True,False,False,True,True,False,False,False,True,False,False,True,True,False,True,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,False,False,True,False,True,False,False,False,False,False,False,False,True,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,False,False,False,False,False,False,True,False,False,False,False,False,True,True,True,False,False,False,False,False,True,False,True,False,False,True,True,False,True,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,True,False,False,True,False,False,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,False,False,True,False,True,True,False,False,False,True,False,True,True,False,True,True,True,False,True,False,True,True,False,False,True,True,True,False,True,False,False,True,False,True,True,True,True,True,False,True,False,False,False,True,True,True,True,False,False,False,False,True,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,False,True,False,True,True,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,True,True,True,False,False,True,False,False,True,True,False,False,False,False,False,False,True,False,True,True,False,False,True,True,False,True,False,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,True,False,False,True,False,False,False,False,True,True,False,False,True,True,False,False,True,True,False,False,True,False,False,True,False,True,False,False,False,True,True,True,True,True,True,True,True,True,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,False,True,True,False,True,True,True,False,False,False,False,False,True,False,True,True,False,False,False,True,False,True,True,True,False,True,True,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,True,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,True,True,True,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,True,True,True,True,True,False,False,False,False,True,False,True,True,True,True,True,False,True,True,True,True,False,False,True,False,True,True,False,False,False,False,False,True,True,True,False,True,True,False,True,True,False,False,False,False,False,True,False,True,False,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,False,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,True,False,False,False,False,True,False,True,False,True,True,True,False,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,False,False,False,True,False,True,True,True,True,False,False,False,True,False,True,True,True,True,False,False,True,True,False,True,False,True,True,True,False,True,True,False,True,True,True,True,False,False,True,True,True,True,True,False,True,False,True,False,False,False,True,True,True,True,True,False,False,False,True,False,True,False,False,False,True,False,False,True,False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,False,False,False,False,False,False,True,False,False,True,True,False,False,True,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,False,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,False,True,True,False,True,False,True,True,False,False,False,False,False,False,True,False,False,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,False,True,False,True,False,True,False,False,True,False,False,True,False,False,False,True,True,True,True,False,False,False,True,True,True,False,False,False,True,False,False,True,False,False,True,False,True,True,False,True,False,True,False,False,True,False,True,False,True,True,False,True,True,True,True,False,True,True,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,False,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,False,False,False,True,True,False,True,False,False,True,True,True,True,True,True,True,False,True,True,False,True,True,True,False,True,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,False,True,False,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,False,True,False,True,True,False,False,False,False,True,False,True,False,False,True,True,True,True,True,False,True,False,True,True,True,True,True,False,True,True,True,True,False,True,False,True,True,True,True,False,False,False,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,True,True,True,False,False,True,False,False,False,True,True,True,False,True,True,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,True,True,True,True,True,True,False,False,True,True,True,False,True,False,True,True,True,True,False,True,True,False,False,True,True,True,True,True,False,True,True,True,False,True,True,False,False,True,False,True,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,False,True,True,True,True,False,True,True,True,False,False,True,False,True,True,True,True,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,True,False,True,False,False,False,False,True,False,True,False,True,False,False,True,True,True,True,True,True,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,False,True,False,True,True,False,False,True,False,False,False,True,True,True,True,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,False,False,False,True,False,False,False,False,True,False,False,False,True,True,True,True,True,True,False,True,True,True,True,True,False,True,True,True,False,False,False,False,False,True,True,False,True,False,True,False,False,True,True,False,False,False,True,True,True,True,False,True,True,True,False,True,False,True,True,False,False,True,False,False,False,True,True,False,True,False,False,False,True,True,False,True,True,True,False,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,False,False,True,False,False,True,True,False,False,False,False,True,False,True,True,True,False,True,True,False,False,True,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,True,True,False,True,True,True,False,False,False,False,True,False,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,False,False,False,False,True,True,False,False,False,True,True,False,True,True,True,False,True,False,False,True,False,True,False,True,True,False,True,True,False,False,True,False,False,False,False,True,True,False,False,False,True,True,False,True,False,False,True,True,False,True,True,False,True,True,True,False,True,False,True,True,False,True,True,False,True,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,True,True,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,False,True,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,False,False,True,False,False,True,False,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,False,False,True,True,False,True,True,True,True,True,True,True,True,False,False,True,True,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,False,True,False,True,False,False,True,False,True,True,False,True,False,True,False,False,False,True,True,True,False,False,False,False,True,True,True,False,False,False,False,True,False,False,False,False,True,True,True,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,True,False,True,False,False,True,False,True,True,True,False,False,False,True,True,False,False,False,False,False,True,True,True,False,False,True,False,False,True,True,False,True,True,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,True,True,False,False,True,True,True,True,True,True,True,False,False,False,True,True,False,False,False,False,True,True,True,True,True,False,True,False,True,True,False,True,False,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,True,True,False,False,False,False,True,False,False,False,False,False,True,False,True,True,True,False,False,False,True,True,True,True,False,False,True,False,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,True,True,True,True,False,True,True,True,True,False,False,False,True,True,False,True,False,False,False,False,False,False,False,True,True,True,True,True,True,False,True,True,False,False,False,False,False,True,True,True,False,False,True,True,True,True,False,True,False,True,True,False,True,True,True,False,False,True,False,False,True,True,True,True,False,True,False,False,False,True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,True,False,False,False,False,True,False,False,False,False,False,False,True,True,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,True,True,False,True,True,False,False,True,False,False,True,False,False,True,True,True,False,True,False,True,False,False,False,False,False,False,False,True,True,False,True,False,True,False,True,False,False,True,False,True,True,True,True,True,False,True,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,False,False,False,True,False,False,False,False,True,True,True,True,True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,False,True,True,True,True,True,False,False,False,False,False,False,True,True,True,True,False,True,True,False,False,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,True,False,False,False,False,True,True,True,False,False,False,True,True,False,True,True,True,False,False,True,True,False,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,False,False,True,False,False,False,False,False,False,True,False,False,True,True,True,True,True,True,True,False,True,True,True,False,False,False,False,False,False,True,False,False,True,True,True,True,False,True,True,False,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,True,True,False,True,False,False,False,True,True,True,True,False,True,False,False,True,False,False,True,False,False,True,False,False,True,True,False,True,True,False,True,False,True,True,True,True,True,False,True,True,True,False,True,True,False,True,False,False,True,True,False,True,False,True,True,True,False,False,True,False,False,False,False,True,False,False,False,True,False,True,False,True,False,True,False,False,False,False,True,True,True], dtype = "bool")#candidate|3076|(5250,)|const|bool
call_3075 = relay.TupleGetItem(func_2092_call(relay.reshape(const_3076.astype('bool'), [525, 10])), 0)
call_3077 = relay.TupleGetItem(func_2095_call(relay.reshape(const_3076.astype('bool'), [525, 10])), 0)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_3085 = relay.TupleGetItem(func_1430_call(), 0)
call_3086 = relay.TupleGetItem(func_1432_call(), 0)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_3088 = relay.TupleGetItem(func_2326_call(relay.reshape(call_3069.astype('float64'), [14, 3, 15])), 0)
call_3089 = relay.TupleGetItem(func_2328_call(relay.reshape(call_3069.astype('float64'), [14, 3, 15])), 0)
uop_3104 = relay.sinh(call_2996.astype('float32')) # shape=(14, 3, 15)
uop_3106 = relay.sinh(call_2997.astype('float32')) # shape=(14, 3, 15)
func_2092_call = mod.get_global_var('func_2092')
func_2095_call = mutated_mod.get_global_var('func_2095')
call_3125 = relay.TupleGetItem(func_2092_call(relay.reshape(const_3076.astype('bool'), [525, 10])), 1)
call_3126 = relay.TupleGetItem(func_2095_call(relay.reshape(const_3076.astype('bool'), [525, 10])), 1)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_3141 = func_1817_call()
call_3142 = func_1817_call()
uop_3145 = relay.exp(uop_3062.astype('float32')) # shape=(14, 3, 15)
uop_3147 = relay.exp(uop_3064.astype('float32')) # shape=(14, 3, 15)
output = relay.Tuple([call_3031,call_3044,const_3045,var_3046,const_3047,call_3049,var_3050,call_3057,var_3058,const_3059,const_3060,call_3069,call_3075,const_3076,call_3085,call_3088,uop_3104,call_3125,call_3141,uop_3145,])
output2 = relay.Tuple([call_3032,call_3048,const_3045,var_3046,const_3047,call_3051,var_3050,call_3061,var_3058,const_3059,const_3060,call_3070,call_3077,const_3076,call_3086,call_3089,uop_3106,call_3126,call_3142,uop_3147,])
func_3149 = relay.Function([var_3046,var_3050,var_3058,], output)
mod['func_3149'] = func_3149
mod = relay.transform.InferType()(mod)
var_3150 = relay.var("var_3150", dtype = "float32", shape = (70, 4))#candidate|3150|(70, 4)|var|float32
var_3151 = relay.var("var_3151", dtype = "uint8", shape = (168,))#candidate|3151|(168,)|var|uint8
var_3152 = relay.var("var_3152", dtype = "float32", shape = ())#candidate|3152|()|var|float32
output = func_3149(var_3150,var_3151,var_3152,)
func_3153 = relay.Function([var_3150,var_3151,var_3152,], output)
mutated_mod['func_3153'] = func_3153
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_3169 = relay.TupleGetItem(func_1040_call(), 0)
call_3170 = relay.TupleGetItem(func_1042_call(), 0)
output = call_3169
output2 = call_3170
func_3172 = relay.Function([], output)
mod['func_3172'] = func_3172
mod = relay.transform.InferType()(mod)
mutated_mod['func_3172'] = func_3172
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3172_call = mutated_mod.get_global_var('func_3172')
call_3173 = func_3172_call()
output = call_3173
func_3174 = relay.Function([], output)
mutated_mod['func_3174'] = func_3174
mutated_mod = relay.transform.InferType()(mutated_mod)
const_3187 = relay.const([[[-7.610143,8.141572,-2.770255,-1.746375,6.964290,-9.229113,3.553326,-3.848401,2.992799,-5.881279,-5.018483,-6.256872,-9.158909,5.913988,6.191172,1.987055],[-9.936108,-9.912912,-9.643976,-4.315615,4.443622,4.820921,-2.152779,-7.882682,-8.318472,8.032458,-4.948220,0.923704,3.170149,6.884607,8.135279,-2.433035],[1.292447,-4.513489,6.403477,8.410732,3.052475,-7.907092,-3.406879,6.960293,8.033150,-0.377942,9.544130,9.026763,-1.731129,3.002750,3.207603,2.320775],[4.160298,1.485306,-4.911061,1.730783,3.730068,0.865772,-9.815123,1.578717,-3.916736,5.429265,6.304317,-9.565409,9.689167,4.969062,1.418055,6.580164],[-7.118025,6.195311,-1.071668,-1.643568,-0.055622,6.299574,-3.214843,7.160034,-6.448139,-8.800420,1.614856,1.513372,6.604866,8.236081,-4.865699,6.422136],[9.838025,8.332742,2.017283,-9.445600,-5.216179,-9.835540,-4.037150,9.364794,7.641801,-9.379739,-7.568403,7.249366,-3.027585,-0.205617,-2.544696,5.074565],[-5.947983,4.466525,-3.913622,-3.267784,2.635916,3.942141,-2.650909,9.900076,5.195499,-8.938427,2.032831,0.358101,-9.063837,-8.552771,1.930766,7.442942],[1.746143,2.146568,-7.592667,-8.425252,-3.406690,5.434746,-9.676818,-8.004889,-6.893592,9.836168,1.668491,4.370944,-0.329382,-7.723763,3.609058,6.159582],[-2.965146,-3.388289,-5.774327,-2.447009,-6.836685,4.738335,-6.503480,-6.402967,-0.295435,3.330335,-5.924231,-2.487687,-8.307721,-0.536672,-5.349140,-9.857862],[-7.605954,0.146689,7.391113,-5.410128,7.558834,-8.792640,8.284070,-9.249317,-3.415106,4.564729,-9.501144,5.255516,-3.084590,-6.052121,-0.440198,0.452548],[4.093071,1.524576,8.570159,-6.924027,-6.987252,-4.764224,-1.746777,6.311138,-8.963684,4.898957,-4.220302,-4.470615,7.600882,0.829236,1.124518,-6.643047],[3.436440,-5.230556,1.390923,1.929116,2.821198,-2.515907,-6.009474,8.147284,-6.233386,0.532142,1.483347,-5.434308,-3.515838,-5.336628,-9.277519,-2.917741]],[[3.848161,-5.951139,-0.525831,-6.235516,-2.439206,0.100283,-6.989272,5.667818,6.049613,-4.611287,-8.283809,7.942755,-1.252980,5.102267,6.915513,1.725472],[-4.255384,2.974837,6.142045,-9.618645,-3.618335,4.956707,-2.204221,-8.571425,8.584877,8.412432,1.849164,0.478888,-5.967497,-5.206387,-8.842224,-2.087494],[-1.967799,4.390095,0.777000,6.433644,5.394916,4.419917,2.774923,-9.248580,-1.864326,1.422093,-1.168224,5.771079,4.926902,-8.598347,0.818839,-0.519787],[1.220193,-9.138354,3.237843,-3.458601,-8.947038,8.210922,5.893313,-4.791287,3.496909,1.127642,-6.243000,-7.793548,4.118338,-4.624552,-1.382918,-0.734412],[-6.853837,-7.259205,-8.867050,9.055581,-6.674004,-3.538582,-9.478511,2.700819,-6.902979,0.849325,-4.886084,-2.682955,0.333200,-8.302177,2.711341,8.782468],[8.593434,-8.955928,-6.268433,-9.625377,-5.410116,8.543659,-7.345701,-3.763489,3.870929,1.497170,7.137554,1.368837,-8.214963,-6.883273,-8.556315,-7.060247],[-0.501870,1.225525,-1.936792,1.648736,4.267826,5.977439,-2.608300,-2.504071,7.724345,6.593727,-0.555283,1.218797,-0.377916,-0.084112,9.541302,9.694220],[8.803820,1.083837,-4.856590,-7.102222,7.839104,3.992884,1.245675,4.886272,-2.711011,-9.124034,-6.266708,8.092828,7.770057,6.791192,-9.002931,-5.596665],[-4.239560,6.605392,1.710717,-4.644536,3.038839,-6.019435,4.568334,-3.069029,-4.015053,-4.139492,-4.550734,9.403086,-6.260783,2.720233,6.620087,-2.272769],[2.451404,5.018009,-8.506012,7.499735,3.302185,-5.800519,1.635449,-9.501801,4.085009,-7.081692,7.820536,-5.162747,4.719740,-6.200085,9.750765,-1.694800],[0.243437,1.818962,2.711663,3.505454,-8.380756,5.571582,-4.635371,0.268553,6.696636,-1.144077,-2.941034,-1.323549,-2.750657,-9.260141,2.078448,-6.848367],[-8.744681,-4.086551,-2.478650,8.445129,-9.274315,-4.393901,-7.831307,-2.539408,-3.118416,-3.408182,2.376556,-4.131544,-3.413500,-2.555175,1.201310,-0.727566]],[[-7.512871,8.772803,-9.952010,-0.934295,9.605204,-2.195453,-1.671163,3.656004,6.144947,2.275986,-6.586711,-0.299728,0.682824,7.283677,4.756046,-1.258189],[-9.531021,-4.408233,-2.433128,0.639247,3.443808,-2.292017,7.636978,-2.754971,1.496888,0.212566,6.381635,-3.755874,-2.879311,3.972299,6.716704,-1.859850],[5.544074,4.778810,6.920588,-2.532998,-2.857775,-5.003575,-3.118722,-8.122202,2.023916,-4.120190,6.316553,1.096870,-4.884565,4.370520,-6.622321,0.536686],[-3.347230,-4.385992,-5.763962,-5.949175,7.481334,-0.181401,-4.169118,3.342095,-4.241717,-6.476054,2.047546,-5.886927,6.109993,5.193959,2.132329,8.269543],[1.377599,2.384225,-3.485084,-2.464676,-0.956916,-4.007650,7.194249,-4.895226,4.191523,4.927798,-9.758065,-0.846830,0.117145,-5.217913,-4.500461,-6.780526],[4.129441,1.755776,-1.484026,8.725114,-2.176386,3.873580,5.449164,-4.277302,-3.123015,0.100528,2.682859,-3.390694,-8.362343,0.091738,1.141631,-9.940192],[7.911816,-2.846931,-4.985588,-3.899603,1.907145,-9.162181,-3.328188,2.561888,4.993857,0.194356,-8.327427,6.630886,-7.611793,-3.167564,1.563383,-3.379206],[-8.195488,-8.768234,-3.611510,-7.859065,-2.887709,7.781664,8.529940,5.240685,9.022815,2.304439,2.718632,-5.205920,2.636940,1.262333,-5.074345,6.340133],[-0.958782,5.883118,-4.028206,4.903828,-0.832987,1.390099,8.658259,-9.126449,-2.735972,8.810172,6.064207,1.065319,-1.688464,6.075708,6.169936,5.365674],[-6.171119,-5.687749,-3.604142,5.635934,-9.898275,-0.290323,9.565698,1.724516,-9.168009,1.362415,-1.872098,-5.500674,9.568868,3.395844,-3.670520,6.311772],[8.339518,-1.962650,9.918089,9.360579,-0.903933,7.043864,-1.235956,6.723252,8.510872,-3.477639,-2.481309,-4.960694,-6.677444,-2.241571,3.750668,3.695578],[9.982187,-4.498372,7.561344,7.242053,-9.111545,-4.984420,9.243929,0.001234,-2.336757,-9.393472,5.957274,3.323882,9.106478,-3.373945,2.505428,4.187278]],[[0.226558,8.496994,8.486523,3.886342,5.605307,3.880408,8.575300,-1.426916,-3.510003,-7.422298,8.130547,-2.041323,4.598727,3.364342,-4.115838,-9.598958],[7.040876,1.125032,-4.503924,-3.886618,-8.300449,-6.274665,-1.901714,2.552270,2.948971,-9.725939,1.487015,9.029437,-3.039831,1.925020,-6.884593,-2.904811],[5.861248,-4.507799,-3.864476,-6.484785,-1.805094,6.057425,8.365329,-1.280829,-0.252687,0.351456,8.713408,8.210405,-8.770874,-6.221126,-9.972911,-4.056322],[-3.516770,6.004176,0.516413,8.218884,-8.777156,-3.216547,-7.209283,-2.263450,-5.566751,-9.845945,5.899353,7.282936,9.873252,-2.583940,-4.526004,1.665114],[0.469875,-6.526180,-3.926167,6.141054,-1.240229,-4.794295,-0.928874,8.014649,9.410180,-2.776307,5.282317,-0.367038,6.588036,-5.932596,9.975385,2.579361],[-4.430696,5.104193,2.948210,4.595853,-3.318057,-5.089886,0.824861,2.736684,-1.980022,3.488652,1.076102,-3.624219,-5.145508,3.587391,-9.183807,-6.491401],[-5.684849,-1.022916,-2.031946,6.658547,8.263412,7.774901,1.625277,3.097548,-1.877681,-6.303914,-6.655922,2.715905,2.824375,-8.015026,8.454127,5.208873],[-4.450413,3.507879,1.055541,-9.428405,6.120954,4.538763,-3.608452,-6.896607,7.715937,2.913368,2.887634,-1.418058,1.210334,-4.924906,-7.631131,-2.380937],[6.862549,1.563480,-3.467391,-7.224991,-6.552711,-6.505720,-9.384383,3.202387,8.046934,-6.617842,4.172805,-2.547682,0.487986,1.742119,-3.872386,2.913275],[-3.039935,-6.613210,-8.812829,-3.318859,1.402896,4.782150,0.490765,0.853795,9.690567,5.701762,6.055043,4.843623,-3.114738,-2.022899,-2.645001,8.837142],[-6.305583,3.319637,-2.249186,2.570704,6.279997,3.376241,-9.104279,8.510596,-3.224843,-2.998126,-2.112149,1.465426,0.094255,1.215386,3.441346,-5.211502],[4.936446,-7.399555,6.517498,7.506542,-3.366654,8.881917,1.377798,6.714365,8.925431,1.254461,6.109788,-8.853651,-5.818807,1.974226,-2.085174,-0.347140]],[[7.665708,5.722224,-1.571133,5.021274,-0.755136,5.278497,-0.744172,9.944194,8.904900,0.334074,5.704775,0.235374,-8.767857,8.604983,-7.321585,-2.263970],[-4.260256,-9.489930,-6.537178,-1.798355,-8.147610,-1.509825,-3.972242,-5.815915,0.588159,-0.558598,9.442980,-8.966241,-8.970229,1.832847,6.984859,2.845019],[3.443472,5.900807,8.198498,-0.576853,1.787939,-1.421802,7.633449,1.053831,0.912596,9.799103,8.202308,-3.596677,-9.120196,-2.192204,3.981914,0.955205],[6.467920,-2.175481,-9.137062,-3.208502,2.652557,6.297760,8.030387,5.814761,8.204736,-5.823549,3.685533,-4.968255,-0.194299,7.232498,-8.819437,-8.672862],[4.180303,6.398145,-1.747281,-9.538915,-0.379648,-4.801418,-4.680691,-7.572822,-4.907750,3.090664,4.436825,1.702867,-2.213293,0.552665,-6.763829,0.661878],[-5.007172,8.553527,-0.472624,5.696332,-8.894276,4.743373,6.293855,-7.971538,-1.862073,3.810522,1.884481,1.255109,-2.280551,0.311396,-3.570722,-1.029172],[5.360247,1.294602,7.240174,-0.739442,-1.266770,2.714111,-7.550009,-9.957584,9.844481,-1.402212,-4.120959,-4.440703,2.637602,5.208331,-2.015483,-0.032277],[-4.491632,-7.110417,-6.250790,2.112229,-7.172038,4.345601,-7.582821,3.415549,6.368400,-7.428587,6.086144,-5.880903,-9.902231,-6.642663,-0.856890,-9.599122],[8.576985,-2.295877,-2.520094,-1.325920,-2.640757,3.066729,4.682676,-1.657025,-5.248475,4.659874,-9.584695,-4.646237,5.529961,9.187309,-7.315213,-3.555701],[-9.070070,9.808642,-0.977896,5.391151,7.152026,7.089406,6.126180,-7.688747,0.264520,4.815570,8.836036,-5.937422,9.162742,-6.382034,-3.584980,4.448998],[-4.014067,1.515505,-7.344744,8.385475,0.136954,9.508180,3.889960,-7.964061,1.880229,-1.652507,-9.863619,9.239672,-4.648943,8.628531,1.839088,-5.037410],[0.069228,-0.170159,-8.581578,-3.063132,3.333007,2.770884,0.461106,5.144018,9.469411,7.922367,-1.280247,5.359925,3.350583,3.122621,2.395631,-4.048242]],[[2.610331,9.017934,-8.365152,2.139907,1.145872,-1.909583,6.089550,9.705667,0.002637,-5.255068,3.890339,7.070897,-3.381634,5.766839,-0.196492,-2.017086],[5.527684,4.261409,0.323160,3.821253,0.625261,8.829224,2.697126,-7.147496,-7.883028,-8.502214,-9.229709,-6.918286,9.961353,4.549851,5.908984,8.344310],[3.326449,-7.885827,-0.547578,2.705725,-0.651082,-2.884569,2.799001,-3.161368,6.512062,5.658527,-5.847351,-9.335224,-0.376228,5.045876,3.188082,-6.044808],[-4.013904,-2.399106,-2.089668,-3.279238,-2.218534,-9.968300,3.003253,5.086579,1.707004,4.631277,-8.309055,2.755434,3.043988,-7.744267,-1.805797,7.046570],[-9.869130,8.228437,4.497135,1.997178,-9.857119,7.035607,-5.434879,-6.030200,8.755067,-4.228480,7.850287,-8.581665,-7.610187,0.673008,4.371480,0.710578],[-6.199583,-8.948466,7.855920,-4.501743,1.299072,0.701513,-6.970759,-8.191818,7.870379,-7.934406,-5.146513,0.850577,3.163385,6.549949,5.134766,-5.974897],[9.711044,2.323625,-7.435454,-0.810773,5.741557,-4.366402,5.430557,-1.118828,6.648961,3.490266,0.186727,-2.243851,-8.536136,-4.458555,9.993055,8.244287],[6.370836,6.527308,-5.495555,-4.460362,7.336222,-1.906101,0.034047,-1.590593,6.504418,-8.726273,-9.353173,9.768522,4.611489,3.010666,3.337934,5.076167],[9.338883,-1.682662,0.158400,-1.017063,3.726574,0.839070,3.603349,1.327812,-2.584268,4.775719,4.816766,9.183568,-8.051202,2.422161,8.434726,8.692454],[1.260071,0.451559,-0.449581,0.531311,-9.257807,-6.809164,-6.077293,-2.451432,1.000070,-4.566084,-0.420372,2.923298,-2.204323,-8.818473,-2.710642,-0.844570],[-1.281757,-3.835405,8.757652,-6.158647,-3.233279,2.201127,1.663861,4.381625,-7.210352,6.666012,8.716646,7.279364,2.913306,-5.530469,3.471077,1.439412],[-9.082184,-1.915261,2.520703,5.464484,9.018951,7.982653,-2.229430,-8.783229,-7.677329,3.659496,-0.227788,0.230234,7.161338,1.715797,-4.114183,-9.223871]],[[-4.724938,8.962485,9.575050,-4.080629,8.720863,8.629337,-5.649685,-7.050353,1.941022,7.392628,9.601987,4.838513,-6.897058,6.836352,1.497477,3.976522],[4.350321,-7.848291,3.817926,9.729333,-5.788564,-2.978640,-5.002245,2.372866,-7.943185,-7.619856,1.656489,-0.510082,-7.325240,-0.959323,0.565520,-2.347750],[-3.933547,-1.937106,0.365846,1.655774,-5.005614,-3.692928,-8.795981,3.086059,-2.402186,-1.417463,7.147323,9.126402,4.072433,-6.816543,6.583971,9.123249],[8.415517,2.093470,2.608370,-9.454411,-9.529814,3.828465,-3.204180,-9.316148,-6.026388,-5.777847,5.280870,6.651746,7.162121,-2.146429,-4.679893,7.089203],[7.397748,-5.361030,9.397403,-4.316124,-8.062279,-4.034722,-6.777478,1.231615,-4.619076,5.240483,-4.259698,-5.596933,-2.809600,-9.925472,-0.506336,-7.638003],[9.168990,-2.447673,9.698095,-6.787010,-8.964763,-0.644342,0.969041,6.922153,8.494354,-1.851170,-6.822876,6.108255,5.618381,3.387559,2.335904,1.273219],[7.514556,4.162756,-1.336432,-2.818063,0.782748,-4.312843,-9.157799,-5.485095,-8.016291,9.478406,9.831867,2.808750,5.418524,-0.222833,-4.417126,4.644284],[9.366202,-7.089332,-4.491778,1.795040,3.496894,2.124130,9.105663,4.127647,-5.347453,-5.035399,4.197064,-8.427488,6.049038,-6.699523,-6.893290,5.924322],[-1.900652,1.438967,-8.387272,-8.576171,-4.474883,1.982952,9.241362,2.161324,-5.700947,4.287314,2.377643,-2.737097,-4.040728,-0.009074,-2.149951,2.945388],[8.303215,1.165566,8.927834,7.459869,2.975956,7.381640,2.483313,-1.769997,0.804848,-6.484716,1.331821,2.481829,6.121640,-6.202768,0.699190,-1.358042],[6.224958,-0.527318,-5.135656,-2.786375,-2.457472,-7.109710,0.440254,5.367906,9.389093,0.644707,-9.705259,-6.263330,5.057986,2.104353,-5.908500,9.736312],[-8.805279,-0.610335,-4.193411,-3.479761,8.863209,-3.322697,-8.308614,2.618738,4.894784,-6.485277,7.635733,4.187697,-7.460247,3.131521,9.008717,-8.435796]],[[-5.156142,-7.832305,5.254664,0.702496,2.514671,0.826626,-5.288005,4.861684,-4.101601,6.646021,2.474676,-4.377780,-8.148749,-2.489324,-5.473545,4.200985],[-3.706143,0.788458,-1.286620,-8.522683,1.003767,5.871101,-5.753707,3.189369,9.001208,-8.683917,-5.313061,-3.013944,-5.376695,-6.089716,0.610681,1.511036],[0.259180,5.272288,9.891978,0.440850,-1.446149,-5.684098,-8.230350,5.590679,3.585722,-5.353357,-0.196802,-6.731815,7.153466,8.464027,-1.852164,-8.100447],[-5.451901,6.279921,6.619688,-1.708510,-3.850534,-5.959653,-5.018193,-6.967218,6.312605,2.540922,7.824033,-8.030019,-1.033143,9.599507,-6.052534,-8.206033],[9.718506,0.407758,6.785938,-6.765433,-4.431890,-0.813683,-8.946774,-7.360158,2.741287,1.117396,4.395292,6.525706,-3.512312,-6.709377,0.428123,1.332238],[1.567578,1.913849,-6.337793,-8.865293,2.900837,0.096338,9.262772,5.095117,-0.532408,5.160511,1.663789,9.863453,1.770728,-7.136045,7.697624,0.064410],[-4.997772,3.747489,2.837189,-2.707587,-1.523278,-2.031528,2.731135,-3.620985,3.020008,-7.485670,-2.708666,-8.394067,2.970698,-2.388038,-7.867384,8.190836],[0.331714,0.244059,-8.715842,2.087768,4.047191,-7.349602,0.474540,-7.585635,-0.469344,1.954146,2.651382,-7.670626,3.095729,4.886216,4.075619,-1.529015],[8.260378,6.800335,0.282562,-7.119483,-2.957705,-7.916795,2.261032,-0.631696,4.726269,-5.264222,4.499400,9.634759,-1.278402,-6.049176,-6.183458,-5.989060],[-9.699292,0.743880,-2.371563,0.044815,1.537358,-6.109082,-8.508252,-1.820013,4.084130,-8.278611,-9.306364,0.049068,-9.781952,-7.335519,-8.205434,-3.989896],[-3.295027,9.253869,4.982800,9.342045,-7.734871,4.277743,4.925346,-3.801648,0.641287,6.179189,-9.358341,-5.375956,6.704317,2.111588,1.966190,-8.763431],[-3.389960,-1.066675,-3.820531,-1.882061,5.043347,-5.795352,8.730064,8.719157,7.531194,-6.318529,6.124602,0.953812,4.242815,8.443341,-4.862378,-2.080011]],[[3.785922,0.341097,1.795665,-6.214689,5.217013,4.993288,7.533892,5.801951,3.093195,-3.046707,-7.870355,9.340945,2.006498,-9.162090,0.366520,-4.665856],[2.062781,-2.571553,0.628810,-7.834728,3.590693,9.047756,-6.944746,-8.502790,1.167240,2.222918,-8.408703,0.172876,7.914924,0.235639,5.808215,0.487603],[6.047531,4.570157,-8.756211,-9.071913,8.097075,-4.717326,-6.617816,6.680215,4.700732,-5.735821,-7.890363,8.773280,2.445621,-3.891552,-1.281563,-9.649220],[4.903322,-4.550215,4.769371,-4.815164,0.003358,-3.144076,6.951203,3.703157,-3.799400,-9.183557,0.388718,-8.240845,-6.420638,4.969453,-0.305069,3.884349],[9.048189,2.542167,-6.351357,2.313778,-6.696615,0.967750,-8.537731,2.645861,-5.259327,7.497648,9.160626,2.374804,-8.730602,7.085538,-5.498618,-5.343580],[-2.809496,-9.966959,1.474666,-9.699865,6.961684,7.693195,-9.056970,8.904548,-4.344740,2.023842,-0.657264,-8.319742,5.378080,-5.837018,-7.078102,-1.836030],[-3.584110,1.017104,-0.816737,-4.995754,4.971861,8.379725,-8.088469,7.669101,4.732601,-1.592259,1.932762,-8.734939,-7.884996,-9.645865,-8.515478,-2.931030],[8.967239,-0.675733,3.785651,9.920524,9.912143,7.831152,1.860668,-7.145977,1.691065,1.951424,1.167953,1.543675,-4.970182,-3.987055,-0.485333,3.538774],[-6.165875,-5.389302,-5.676279,5.703946,-0.897110,8.792144,5.610174,8.553433,5.270559,5.715569,-0.114421,-0.221208,-6.988390,1.454551,9.134746,-1.029890],[5.174413,-6.365552,-6.507162,9.942265,-0.711861,1.628360,-9.462461,-0.209366,4.014475,3.293848,-9.260493,-4.790214,-2.522601,-1.351614,-5.098291,-1.761389],[3.053592,-9.929693,-7.702554,-9.551030,-0.589728,-3.710101,-9.607827,-3.221473,-5.812843,-2.525456,-6.060625,2.271210,-9.022532,-2.101614,-0.364990,-0.353489],[8.052541,5.225077,-6.080213,-9.682066,8.979711,-8.845670,1.346776,1.238918,-7.010517,4.237883,-1.397952,7.812981,-7.859340,-7.584570,-1.962664,-9.833969]],[[9.738831,6.688770,3.557956,-7.735907,-9.327856,4.855900,-1.706208,3.195342,-6.905227,1.037416,8.091525,8.944473,-8.134121,-1.844396,5.915119,6.469315],[0.731588,-0.620860,-7.539190,1.456013,8.581027,7.173900,-3.238472,-6.843106,5.149346,8.476412,2.738689,-4.181452,-2.178515,-1.752530,2.391357,-1.045021],[9.587048,4.502109,-5.147135,-5.045633,9.898719,7.313622,8.020411,-2.516471,3.579498,2.436555,7.683019,-2.730226,3.072030,8.791441,-8.379959,9.583588],[-1.620565,-3.305925,2.121255,0.025997,-5.343678,-3.919451,-1.175230,-8.750872,1.838835,-9.726460,7.315551,-7.228062,-5.594399,9.541901,-4.911372,-6.494386],[6.998737,2.974427,7.432287,-8.585463,8.712676,4.912853,0.494251,1.033183,-4.858092,8.085001,-5.276113,-4.749178,8.056662,-5.078799,-8.592005,3.673689],[8.401034,-9.549941,6.919739,-5.388821,-1.152154,-0.505089,0.284762,-9.974479,-5.546261,8.426601,8.469194,0.758098,9.162671,-0.636376,-6.370762,2.504186],[-0.088286,-6.443675,-4.142977,-7.619806,3.534483,3.923841,-9.524905,-6.604854,0.073348,-9.310752,2.599409,-0.316720,5.581482,-3.700551,-4.161287,7.943774],[2.822774,-8.332332,-3.373897,-2.066261,9.088754,-1.145253,7.921184,-8.864696,-1.671641,-6.454290,-0.671730,-0.522725,2.609821,9.897866,-3.078778,9.663739],[1.792789,-7.545232,-6.303630,9.598938,-4.208712,-3.333379,-0.068266,-2.268170,3.997157,-2.397787,6.851647,5.491412,9.212605,-2.503415,8.814202,0.013188],[3.866475,-1.326296,5.677991,-6.819179,3.465012,9.841929,8.658051,-8.832158,-8.721978,7.883676,0.272323,7.047723,3.748906,-2.759253,6.080314,2.935694],[8.615340,-5.318758,4.164219,-4.216586,1.424877,-7.388275,-7.979641,5.673774,7.719216,-9.978277,4.384395,1.420981,-3.858196,1.765183,-6.763775,-1.715049],[-2.514129,-7.165551,5.890758,-5.981934,-1.126649,-8.230388,3.300028,-0.069548,-4.149800,2.408760,-1.753010,-5.442639,1.514311,-5.158772,7.085546,7.663323]],[[7.456817,3.802284,8.975440,-5.575711,3.062797,-1.638442,-3.368713,3.169007,0.607728,9.608696,-2.772317,-1.236852,1.909842,4.312739,-6.082861,5.777892],[-9.446752,-2.354523,-1.150687,4.498945,3.070662,4.092979,-5.198761,-7.623791,9.162955,9.552193,-0.686109,8.191269,-4.852908,-0.564137,-1.295562,1.421450],[-6.748581,-7.163544,-2.119832,-5.830499,2.721937,5.977789,8.538781,3.411584,5.013393,-5.104767,5.317786,-7.071851,-0.986367,-4.094863,-2.705482,2.855130],[8.920812,2.919191,9.431726,-6.809573,1.359594,9.317963,6.228579,-2.995869,8.800534,-8.199586,-8.455613,9.405557,6.994100,8.028820,5.352043,7.011568],[-1.836276,-4.582521,-7.306245,-2.829984,-9.100158,-8.770813,4.360730,3.897448,2.529907,6.972535,-9.213762,-0.991766,-0.560437,8.581589,-7.236283,-4.808023],[2.925856,3.970534,1.089335,-5.874403,5.982697,-2.848001,2.020189,2.178011,8.866500,-9.966716,7.239934,-4.776962,3.474926,2.062211,-1.143596,-6.442512],[-6.095606,9.972387,-5.588488,-9.592938,1.100497,-5.629813,-5.979064,6.640100,-1.898766,6.990950,9.432239,3.066707,9.140012,-7.440322,-5.791724,0.309948],[-1.401204,3.455192,-8.739040,-3.259587,-5.327532,-3.714562,9.548456,-0.632773,-1.384778,4.691827,1.095674,-8.120664,-0.856752,-3.779461,1.084015,1.213880],[9.417505,-2.948501,-2.940355,9.235337,0.840569,8.033687,9.645911,-3.131924,0.373411,0.468138,-7.211145,0.139008,4.969172,-3.112578,-3.060615,-3.416216],[-6.060044,6.131351,-2.965992,0.660819,9.281442,-3.723281,-6.682120,-9.730923,-2.003877,2.472533,2.369898,5.454526,-4.380110,9.798141,-0.167376,-6.188066],[2.416610,8.613235,-6.768992,0.846841,-6.370203,0.145509,0.516841,-9.305010,0.719405,-6.684398,6.846824,5.033023,4.360737,-1.146841,3.053949,-0.579227],[-1.238152,-2.478724,-0.872052,-5.195757,5.790733,-1.712442,9.426303,-2.626915,-4.908041,2.082276,3.386291,2.425908,-1.905480,-7.321375,1.479047,-4.143223]]], dtype = "float32")#candidate|3187|(11, 12, 16)|const|float32
uop_3188 = relay.rsqrt(const_3187.astype('float32')) # shape=(11, 12, 16)
output = uop_3188
output2 = uop_3188
func_3198 = relay.Function([], output)
mod['func_3198'] = func_3198
mod = relay.transform.InferType()(mod)
mutated_mod['func_3198'] = func_3198
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mutated_mod.get_global_var('func_3198')
call_3199 = func_3198_call()
output = call_3199
func_3200 = relay.Function([], output)
mutated_mod['func_3200'] = func_3200
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1612_call = mutated_mod.get_global_var('func_1612')
call_3201 = relay.TupleGetItem(func_1611_call(), 1)
call_3202 = relay.TupleGetItem(func_1612_call(), 1)
uop_3206 = relay.asinh(call_3201.astype('float64')) # shape=(525, 1)
uop_3208 = relay.asinh(call_3202.astype('float64')) # shape=(525, 1)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_3214 = func_2894_call()
call_3215 = func_2894_call()
uop_3219 = relay.cosh(uop_3206.astype('float64')) # shape=(525, 1)
uop_3221 = relay.cosh(uop_3208.astype('float64')) # shape=(525, 1)
uop_3230 = relay.sqrt(uop_3219.astype('float32')) # shape=(525, 1)
uop_3232 = relay.sqrt(uop_3221.astype('float32')) # shape=(525, 1)
func_1463_call = mod.get_global_var('func_1463')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_3234 = relay.var("var_3234", dtype = "float64", shape = (66, 6))#candidate|3234|(66, 6)|var|float64
call_3233 = func_1463_call(relay.reshape(var_3234.astype('float64'), [6, 11, 6]))
call_3235 = func_1463_call(relay.reshape(var_3234.astype('float64'), [6, 11, 6]))
uop_3241 = relay.sin(uop_3230.astype('float32')) # shape=(525, 1)
uop_3243 = relay.sin(uop_3232.astype('float32')) # shape=(525, 1)
bop_3252 = relay.floor_divide(uop_3230.astype('float32'), relay.reshape(call_3201.astype('float32'), relay.shape_of(uop_3230))) # shape=(525, 1)
bop_3255 = relay.floor_divide(uop_3232.astype('float32'), relay.reshape(call_3202.astype('float32'), relay.shape_of(uop_3232))) # shape=(525, 1)
output = relay.Tuple([call_3214,call_3233,var_3234,uop_3241,bop_3252,])
output2 = relay.Tuple([call_3215,call_3235,var_3234,uop_3243,bop_3255,])
func_3260 = relay.Function([var_3234,], output)
mod['func_3260'] = func_3260
mod = relay.transform.InferType()(mod)
mutated_mod['func_3260'] = func_3260
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3261 = relay.var("var_3261", dtype = "float64", shape = (66, 6))#candidate|3261|(66, 6)|var|float64
func_3260_call = mutated_mod.get_global_var('func_3260')
call_3262 = func_3260_call(var_3261)
output = call_3262
func_3263 = relay.Function([var_3261], output)
mutated_mod['func_3263'] = func_3263
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_3306 = func_2910_call()
call_3307 = func_2910_call()
func_1133_call = mod.get_global_var('func_1133')
func_1135_call = mutated_mod.get_global_var('func_1135')
call_3330 = relay.TupleGetItem(func_1133_call(relay.reshape(call_3306.astype('float32'), [14, 3, 15])), 1)
call_3331 = relay.TupleGetItem(func_1135_call(relay.reshape(call_3306.astype('float32'), [14, 3, 15])), 1)
func_1780_call = mod.get_global_var('func_1780')
func_1783_call = mutated_mod.get_global_var('func_1783')
var_3336 = relay.var("var_3336", dtype = "float64", shape = (3, 132))#candidate|3336|(3, 132)|var|float64
const_3337 = relay.const([True,True,True,False,False,False,False,True,False,True,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,False,True,True,True,False,False,True,False,False,True,True,False,False,False,True,True,False,False,True,False,True,False,True,False,True,True,False,True,False,False,False,False,True,True,True,True,True,False,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,False,False,False,False,False,True,False,False,True,False,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,False,False,False,True,True,True,False,True,True,False,True,False,False,False,True,False,False,True,True,True,False,False,True,False,False,False,True,True,False,True,False,False,True,False,False,False,True,False,False,False,False,True,False,False,True,True,False,True,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,True,False,True,True,False,True,True,True,True,True,True,False,True,False,False,False,True,False,True,True,False,False,True,False,False,False,False,False,True,False,False,False,False,True,True,False,False,False,True,True,True,False,True,False,True,True,False,False,True,True,False,True,True,True,True,True,True,False,True,False,False,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,True,True,True,True,True,True,False,False,False,True,False,False,True,True,True,False,True,True,True,False,True,False,True,False,True,False,True,False,True,False,True,False,True,True,True,False], dtype = "bool")#candidate|3337|(300,)|const|bool
call_3335 = relay.TupleGetItem(func_1780_call(relay.reshape(var_3336.astype('float64'), [396,]), relay.reshape(const_3337.astype('bool'), [300,]), ), 0)
call_3338 = relay.TupleGetItem(func_1783_call(relay.reshape(var_3336.astype('float64'), [396,]), relay.reshape(const_3337.astype('bool'), [300,]), ), 0)
output = relay.Tuple([call_3306,call_3330,call_3335,var_3336,const_3337,])
output2 = relay.Tuple([call_3307,call_3331,call_3338,var_3336,const_3337,])
func_3339 = relay.Function([var_3336,], output)
mod['func_3339'] = func_3339
mod = relay.transform.InferType()(mod)
mutated_mod['func_3339'] = func_3339
mutated_mod = relay.transform.InferType()(mutated_mod)
var_3340 = relay.var("var_3340", dtype = "float64", shape = (3, 132))#candidate|3340|(3, 132)|var|float64
func_3339_call = mutated_mod.get_global_var('func_3339')
call_3341 = func_3339_call(var_3340)
output = call_3341
func_3342 = relay.Function([var_3340], output)
mutated_mod['func_3342'] = func_3342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3200_call = mutated_mod.get_global_var('func_3200')
call_3358 = func_3198_call()
call_3359 = func_3198_call()
var_3368 = relay.var("var_3368", dtype = "float32", shape = (11, 12, 16))#candidate|3368|(11, 12, 16)|var|float32
bop_3369 = relay.divide(call_3358.astype('float32'), relay.reshape(var_3368.astype('float32'), relay.shape_of(call_3358))) # shape=(11, 12, 16)
bop_3372 = relay.divide(call_3359.astype('float32'), relay.reshape(var_3368.astype('float32'), relay.shape_of(call_3359))) # shape=(11, 12, 16)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_3382 = func_2910_call()
call_3383 = func_2910_call()
uop_3389 = relay.sigmoid(bop_3369.astype('float64')) # shape=(11, 12, 16)
uop_3391 = relay.sigmoid(bop_3372.astype('float64')) # shape=(11, 12, 16)
func_1611_call = mod.get_global_var('func_1611')
func_1612_call = mutated_mod.get_global_var('func_1612')
call_3402 = relay.TupleGetItem(func_1611_call(), 0)
call_3403 = relay.TupleGetItem(func_1612_call(), 0)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_3404 = relay.TupleGetItem(func_1040_call(), 0)
call_3405 = relay.TupleGetItem(func_1042_call(), 0)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_3409 = func_2910_call()
call_3410 = func_2910_call()
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_3412 = relay.TupleGetItem(func_2198_call(), 0)
call_3413 = relay.TupleGetItem(func_2200_call(), 0)
output = relay.Tuple([call_3382,uop_3389,call_3402,call_3404,call_3409,call_3412,])
output2 = relay.Tuple([call_3383,uop_3391,call_3403,call_3405,call_3410,call_3413,])
func_3418 = relay.Function([var_3368,], output)
mod['func_3418'] = func_3418
mod = relay.transform.InferType()(mod)
var_3419 = relay.var("var_3419", dtype = "float32", shape = (11, 12, 16))#candidate|3419|(11, 12, 16)|var|float32
output = func_3418(var_3419)
func_3420 = relay.Function([var_3419], output)
mutated_mod['func_3420'] = func_3420
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3200_call = mutated_mod.get_global_var('func_3200')
call_3438 = func_3198_call()
call_3439 = func_3198_call()
output = call_3438
output2 = call_3439
func_3440 = relay.Function([], output)
mod['func_3440'] = func_3440
mod = relay.transform.InferType()(mod)
output = func_3440()
func_3441 = relay.Function([], output)
mutated_mod['func_3441'] = func_3441
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_3493 = relay.TupleGetItem(func_2198_call(), 0)
call_3494 = relay.TupleGetItem(func_2200_call(), 0)
func_295_call = mod.get_global_var('func_295')
func_298_call = mutated_mod.get_global_var('func_298')
const_3509 = relay.const([-6,-9,8,2,8,8,3,10,7,-8,10,-9,-4,10,-1,-3,8,3,-9,8,8,-9,-1,10,-9,-1,8,-7,2,-10,-8,9,5,6,6,-3,9,7,5,7,8,4,7,-8,3,-1,1,1,-1,3,-10,-2,-10,-10,-6,10,-5,10,8,-1,6,-3,2,-4,-8,2,5,8,3,-2,-5,5,-9,-9,2,7,2,6,4,8,-9,2,4,-9,10,-8,-4,-2,-7,-9,1,-7,-7,-8,5,3,-6,-7,-6,9,-10,10,7,6,-3,3,4,-8,4,-10,-1,4,9,-8,-8,3,-4,-1,-5,5,5,-1,-9,-7,-4,-4,1,2,1,-7,7,-6,-2,-3,7,4,-7,8,5,-1,-4,4,6,9,6,-6,-7,5,1,-6,-6,-10,-7,-1,6,9,-8,7,-9,-1,2,9,10,-1,-3,-9,9,-4], dtype = "uint8")#candidate|3509|(168,)|const|uint8
call_3508 = relay.TupleGetItem(func_295_call(relay.reshape(const_3509.astype('uint8'), [12, 1, 14])), 0)
call_3510 = relay.TupleGetItem(func_298_call(relay.reshape(const_3509.astype('uint8'), [12, 1, 14])), 0)
func_2795_call = mod.get_global_var('func_2795')
func_2798_call = mutated_mod.get_global_var('func_2798')
const_3526 = relay.const([-3.578317,1.365288,-4.259484,-1.261762,3.746489,-6.811858,-1.633874,-3.551347,-6.225383,7.346567,8.302095,-0.396957,-6.217152,-0.127712,4.733723,2.317372,9.300527,-9.877558,-5.085744,-3.812427,5.848650,3.473456,2.626825,6.895585,2.382012,-2.059488,3.367164,7.675110,0.825632,-8.212825,-5.144152,-5.637285,-3.237192,7.907740,-5.369539,-3.440837,8.196074,9.730980,5.485261,-7.267839,5.725209,4.019486,-5.015282,-9.225458,-4.073163,-0.015279,-3.076372,8.466992,0.217035,-7.945826,-8.694054,-7.803437,-3.840271,-5.388713,-1.015417,9.470241,-3.232535,-8.297168,8.773174,-7.602235,9.002971,-8.648741,1.142586,-9.461418,1.733080,-4.148244,0.245072,2.536420,-8.834797,-9.775633,-5.979900,-5.582913,-7.367879,5.384192,-7.222066,-2.232949,-1.246774,2.491959,-1.919594,5.057026,-3.407678,7.177923,-3.029508,-4.981726,-3.887006,4.621135,-3.970939,1.662988,-0.764286,-8.777773,-8.651038,2.328729,-6.521269,2.271678,-5.830417,-6.433793,-1.507454,7.940284,-0.914023,-9.417158,-0.125928,8.066688,4.008277,8.741819,-7.722150,-8.818599,-2.965218,4.790754,8.769327,8.509669,3.949933,-1.094180,7.211797,-5.315382,0.212336,2.351980,-7.802997,-3.786026,9.455987,-2.250463,-4.367745,2.533110,-8.746799,3.867582,0.490750,2.773293,-6.908508,-9.436111,7.069875,3.567873,9.159396,-3.255778,1.230865,-0.999649,7.868891,-5.990521,4.470191,-2.330673,6.272954,5.962491,4.065475,8.360867,1.154531,5.684685,4.180877,4.207497,5.041881,-4.601317,6.846053,-4.731573,7.542032,-3.419200,-1.621307,-6.950466,-7.640635,-4.661236,6.620463,4.641238,1.433876,4.485818,8.733806,-1.765808,6.900849,9.052099,4.408333,2.874165,9.385656,7.852265,-0.322342,1.582221,-5.429510,-5.897531,2.708115,-6.968978,0.123934,0.227622,-7.984164,1.981757,6.947150,-3.488419,-0.439395,0.134405,6.221047,0.990933,0.574675,-2.853591,-4.494234,0.169767,-8.584203,9.952513,2.161801,-7.016454,-5.477355,5.657345,9.599049,-3.631207,9.496465,6.098398,-3.446355,0.441727,5.808643,1.721416,-0.897034,2.071324,-8.656878,-8.421375,-3.838082,-8.655593,4.654948,-9.255009,5.841626,-4.937008,-0.939233,-2.904551,8.931450,-8.088225,5.627838,-8.622996,-0.739357,8.749676,-3.205300,7.425377,-1.454171,7.364066,3.156456,-1.358086,-4.564474,-9.421224,-6.213178,-3.271261,-3.877686,-8.977136,-8.093131,2.753759,9.468851,-9.607495,5.710057,-1.502508,1.041488,5.877032,7.231866,3.396280,-0.504123,-8.619657,-2.433627,-0.839098,-0.707177,8.323256,-5.427028,9.578809,5.537951,9.235598,7.720749,-7.618692,-3.796616,-6.630764,-7.393044,0.675471,6.373929,1.697604,-8.688448,-1.984991,6.417484,-7.424622,-3.692299,8.547119,1.598435,-8.509666,-4.352129,8.539395,-2.206690,-6.398478,5.407794,-7.679996,3.375366,3.717698,6.749102,-2.694114,9.445513,-0.816934,5.360170,5.235229,9.357334,5.907622,-1.070213,-0.824101,-5.047410,5.336909,-8.311112,-1.438817,-0.188419,-5.565860,7.439239,-8.644301,9.545331,2.523075,-8.519337,8.367005,-2.630481,1.225592,9.901688,-8.344227,-3.562409,3.170129,5.726969,-6.048190,9.070762,4.017603,-3.331620,2.986497,0.965246,-7.953828,2.177303,0.532590,-5.337168,2.385243,-3.423923,-0.243326,9.467806,7.173704,1.265408,-8.397637,-0.638057,-2.941396,1.500998,-9.709535,-5.554146,-1.977935,-1.625543,0.154330,-2.203579,-2.644409,-8.976092,3.724406,3.817362,-2.940113,7.462426,7.265458,3.133420,-8.815694,-2.917019,8.845806,4.149896,-9.314507,7.017704,-2.553494,-6.015516,-3.512475,7.662524,9.246114,-0.018125,-8.107233,-6.350441,-9.313909,8.344670,7.653731,0.230008,-6.501825,-2.201035,0.814923,-9.013379,-7.612183,-1.419763,-3.868295,-0.529901,-9.124729,9.855494,-6.192818,8.873216,4.313171,1.995316,-3.340433,1.035519,1.037201,4.302002,1.016993,1.060199,3.588769,-1.263363,6.881480,5.713382,-7.695997,-9.240307,-2.198710,5.421001,-6.812206,-9.382475,6.207667,0.297453,-5.618620,2.854330,1.228799,7.613553,1.563246,-0.058774,-3.210507,-2.805049,-5.403907,-2.050960,-1.390815,8.441163,-6.117331,9.932400,2.423410,4.539320,-1.950781,-8.602127,0.753931,-6.323448,2.071859,6.484691,-7.225160,-3.880436,5.197444,4.183489,-9.710087,-7.748113,6.148770,5.454659,6.052359,-2.316797,8.948499,5.012095,-8.617329,1.089857,-2.845391,8.195232,4.488468,7.489296,-4.474594,-1.156145,7.544314,-3.455777,1.809663,-3.500454,-7.276647,-5.561256,8.770154,-9.552453,1.137597,2.428439,-0.824663,-9.172424,9.979181,-5.829886,-2.114830,-1.492353,-9.066136,-8.293200,-0.256148,-0.090316,4.967699,9.216077,-2.059445,-1.935924,8.917733,9.277351,1.922012,1.494899,0.957323,-6.274338,3.177224,-4.843023,0.637580,5.438682,0.416979,-0.472874,-2.338657,3.210329,7.631462,-2.007765,8.548285,8.479088,3.258115,9.767495,-0.133431,-9.511210,7.410060,7.435805,-2.913633,-2.894841,-5.355131,-4.514320,-6.878346,5.398408,-9.060101,0.241399,3.327842,-7.492046,4.637782,-2.120976,4.413077,3.305066,6.847976,-5.713313,7.651575,7.045085,6.957281,-3.211265,4.073667,-9.951837,4.256108,7.844883,-4.984769,1.482597,-7.885025,6.020302,3.124225,-5.715416,-9.479963,-8.722362,8.553031,6.665943,6.014953,8.501658,-5.326136,-6.079296,5.932104,-3.745077,9.521241,1.072692,0.294786,-4.088537,-9.053076,5.543738,8.720509,-8.272155,7.280205,3.015662,-6.983907,0.300970,-2.590817,-5.639784,-3.283477,6.388245,8.046897,1.186005,-1.478111,3.394444,-1.140642,0.024646,-9.200143,-7.236477,1.137288,-3.145292,-6.814023,-3.621599,-2.062660,-4.561956,-8.103655,-2.874006,0.082730,-9.720519,2.105609,-9.405880,8.346949,9.815895,2.713833,5.266958,-0.277752,-9.706477,-2.529437,4.525321,-6.809971,2.385029,-1.791107,-1.862467,4.620062,7.111719,-3.639979,-7.916906,4.936478,4.003965,0.156271,5.184115,-6.393351,3.530807,2.998840,1.056700,-8.209592,-0.430852,5.248186,-0.545142,7.680410,8.507177,3.048602,1.622464,-8.314319,-0.212809,-9.100252,6.046911,6.276306,1.280902,0.459466,-9.335107,6.695500,-8.943840,3.661057,9.833350,-1.795385,-8.939038,-7.237319,-1.255438,-8.628140,-7.321921,4.585599,-3.284944,-4.956448,4.902719,-4.847340,-0.424388,-6.872174,-6.456717,9.614717,-3.804011,6.035083,-9.368578,1.881214,-4.242361,8.211085,-0.326419,-8.525510,2.866580,-3.959887,-2.531565,6.168967,-5.036344,-3.252212,6.543989,-4.792744,4.846674,2.318076,0.780046,7.018526,-8.343847,-0.437146,3.808631,3.924872,-9.177791,3.290973,5.159891,0.106590,-0.703840,-0.414033,6.812983,3.002224,-9.082381,-6.900518,8.423126,9.289511,-8.864129,-8.466559,-6.198720,6.409484,6.762400,-7.130985,8.876569,-1.365082,9.504387,7.084293,3.816477,0.195344,4.389526,7.051260,9.290771,6.173497,4.894875,8.911388,6.629800,-4.015979,4.119142,8.699036,-6.552947,-9.782480,1.475748,-6.932412,0.486218,-4.811858,-3.079435,4.968922,5.967150,1.412551,2.403429,-6.344538,6.226226,8.113181,1.918373,4.348088,8.604334,7.484002,-5.268816,8.187043,-0.290324,-4.168746,-1.483251,-6.182480,-4.584559,-1.358668,0.578551,8.807081,4.109181,2.437964,3.440557,-8.212659,4.530964,6.796626,8.481218,9.627238,0.786903,-6.034893,0.794619,6.070448,6.371784,9.978003,-2.696241,7.097556,-9.479529,9.305750,-7.122545,-8.908888,3.082057,5.006945,-9.073484,-5.266535,-7.341853,3.674401,-7.449876,-7.454189,-8.779612,-8.631888,-4.663091,-5.855103,-6.480754,-7.756027,1.046007,-0.347739,1.609734,-8.596122,-1.899716,9.861379,1.898958,9.311661,0.850954,3.894993,1.203470,-3.082028,-7.658530,-3.067452,-6.141847,2.218282,8.751226,5.503560,4.990431,5.207197,-3.373784,-2.568012,4.756122,2.326939,2.350519,4.307531,-7.169967,-8.569759,-6.636058,-3.657037,-3.275113,7.325889,5.523611,-8.751057,-1.851323,1.725418,-2.566677,-8.181404,0.204760,-4.946895,3.136679,7.616572,2.006701,-2.448554,6.180844,6.906504,-3.004933,7.411264,6.207153,-3.660737,0.889285,-7.949791,8.446943,-0.090391,0.793065,-0.567210,-5.963497,-7.868790,0.865231,9.124999,9.235732,-1.519342,2.713312,-1.293611,7.523411,-2.235906,-2.606596,-9.051952,-3.841976,-0.171269,2.693241,-0.454590,-8.215892,-7.149578,3.453773,-4.418532,-8.852579,-5.835025,0.858706,-1.329467,0.492603,2.584162,9.839752,8.087427,-7.194252,6.695584,-1.934657,7.765838,8.769015,8.866701,-4.635217,4.409863,-3.349717,-1.126230,-6.858923,1.771607,-3.091108,1.885438,-7.532742,3.466924,-0.781257,9.801134,-9.301466,-6.812064,-3.102478,-2.446374,8.627976,4.474412,0.368444,0.882174,-8.610227,1.867794,-5.320579,-7.336120,7.617605,0.589449,7.768492,3.050463,-9.014155,4.164427,9.211290,3.526814,5.519271,-1.008188,-6.707542,4.931328,-9.959984,9.398430,9.767349,-5.769139,9.716673,9.372556,-0.077717,-2.931837,-7.691816,9.563542,7.338659,-6.659535,2.072131,2.447839,5.010330,-4.198228,2.660037,-6.830253,4.245496,-8.698404,-4.695987,6.619819,-2.243875,7.993839,0.169327,-6.408449,0.111661,-9.232666,0.549307,3.441740,-7.392318,2.402061,3.072145,-8.202860,-9.167089,-7.350655,-5.430546,2.732835,0.417765,5.360832,6.833631,-8.611401,7.888524,8.646894,-7.103100,0.204329,-8.449539,6.002152,-5.708883,-9.222233,-1.650888,5.915293,2.300601,4.192257,-2.883848,0.366593,-5.412936,-6.641213,-7.243012,-2.781359,-5.124432,9.020346,-4.495272,2.035566,8.889903,3.321485,-6.992709,-0.300032,5.662882,-7.522239,2.994098,4.082891,4.154367,0.014167,4.202493,5.234495,1.128608,-3.693344,9.470162,-9.877805,-6.146836,-2.982133,-1.277375,-3.314579,-9.178610,7.823275,-9.442645,7.156085,6.703400,-0.598967,-1.736711,-5.689784,-2.868489,-0.398460,-0.615816,-3.430212,-7.884072,5.442993,-4.677165,1.883693,0.996189,-0.254255,7.568863,4.049256,-3.805085,-5.338382,2.186128,-4.260011,4.715236,3.981251,9.093162,-5.944534,-1.424260,-9.909428,4.898963,3.809377,7.207089,3.944391,1.101237,6.350590,-5.999805,5.054224,-0.866599,7.140763,-8.682349,-8.857114,5.525657,4.801881,-2.550492,-4.059757,5.922455,-4.364664,9.823765,-3.820109,2.892561,-7.436307,5.167057,4.206873,4.572468,4.080446,-2.972743,1.254606,0.523783,7.909434,-2.582957,8.071024,-0.776823,-8.917625,8.395041,-4.962398,-7.097471,-3.757012,-8.528121,-8.978286,8.010488,5.206395,5.974728,3.246495,-7.066435,-3.173352,-0.339618,-6.320933,-1.146386,-1.313380,4.493644,-1.230127,3.740959,1.446521,-4.793309,8.868344,-2.306990,7.322418,7.501600,-9.709961,-8.166931,-2.879785,-2.144125,9.867365,-5.941424,7.421613,-0.260790,3.020675,-2.952682,-5.177290,-3.051015,-0.665611,-4.888683,-6.896613,-3.240256,2.479642,-9.159820,9.582514,9.076252,7.892607,-9.708100,4.531157,-1.403024,-6.851610,-5.025520,2.927333,-2.277739,7.921693,-0.233518,-8.063718,-0.394664,6.500863,-9.870047,4.708330,6.261936,9.716403,4.202868,-8.869229,2.086730,7.360495,9.257394,3.114612,-9.914945,9.268716,-3.102681,-1.436944,7.934963,4.395637,-6.658477,7.271472,9.649671,-0.396235,-0.203896,-8.364998,3.849776,4.924839,7.532305,4.002970,3.403770,-2.457384,-0.065274,-6.602614,-4.405423,7.986046,-5.274919,-1.125486,8.564018,9.376475,4.444405,-9.683195,8.245918,-0.492062,-3.982979,-8.234811,-6.921645,0.527079,6.651703,-9.796742,-4.143879,3.613337,9.202208,-7.143183,-0.548530,-8.615893,-7.970719,-0.794262,-6.061131,-4.084602,-3.259289,-7.395715,3.160599,-8.785967,1.475319,-2.240183,-6.228367,-8.002482,8.415319,3.085018,-1.934708,0.420416,-2.355721,-4.875685,-2.841881,2.674114,-7.204133,3.105374,7.616063,-0.165453,1.079346,-9.859326,-4.136881,7.376124,-3.611586,1.654495,-5.406154,7.961326,1.047768,8.107529,-2.225994,-5.591572,-5.473934,-7.415136,3.470470,-6.686050,3.808877,6.598110,5.512663,6.793466,0.261224,3.663601,7.149795,-0.439167,-5.287951,4.392663,-4.547556,4.305497,4.941773,-8.454885,1.060490,8.248276,-7.386377,-0.716816,4.175387,8.415325,5.805712,-3.779191,6.827177,2.176033,-3.638939,-0.016992,-5.234548,8.185981,1.782860,7.602571,-7.640635,3.100768,3.831915,4.678455,9.215109,8.381505,7.041621,2.083374,-5.638493,-7.938668,0.852168,2.076702,3.596613,-4.906847,-5.286150,2.806308,-3.588706,1.140570,-1.473387,4.151409,4.911682,-7.370169,-2.898773,6.214957,-5.506082,-1.139185,-1.820600,-7.024330,-8.982924,-7.582891,-8.924592,-3.813574,-5.827826,-7.306241,-5.275994,-4.765770,-1.199981,-9.753567,8.652986,3.266780,9.853690,4.194772,0.129798,2.480450,-9.845846,-7.143789,7.330741,-8.601731,1.583246,8.538095,-7.001994,6.477750,-2.796865,6.718386,-6.940741,-7.066887,-8.376069,0.194260,0.598732,-0.934132,8.504655,-8.018051,8.267096,-6.794156,7.951653,-6.734924,-5.692795,-4.815174,3.916284,-8.050609,-2.862471,5.742431,-0.037659,-5.730093,-6.549560,-1.031897,6.301292,-6.789730,8.778833,4.467209,-9.492074,-5.314773,-7.881919,-7.044328,-6.190909,5.865181,9.769426,-7.051594,5.077578,2.139170,3.897281,6.551331,-7.144255,9.810384,9.408686,-5.520681,-8.456657,-2.695891,5.206860,-1.387814,8.510965,-3.091232,-0.878689,-5.553398,0.807099,8.209946,4.360796,4.514091,2.048448,1.442490,-5.129563,-1.479545,-2.231189,8.486558,4.099438,-4.838083,3.929284,1.453940,8.188814,2.089802,0.252380,2.742655,-8.275732,-2.933278,7.758945,-8.051046,4.887664,-6.536162,7.571280,3.371852,7.355340,0.075016,-7.254224,-1.323367,-8.579440,-4.897856,5.077478,9.165852,1.683600,1.362679,8.491922,-1.992869,-4.852387,8.636530,-1.189835,3.795685,-0.492441,-9.815137,8.391494,-7.944527,-9.789592,-5.092667,-7.990791,5.488962,8.044870,-5.815030,-0.436712,-1.170059,0.932889,-6.756560,-9.503503,0.774079,-3.208315,-2.208769,-6.235784,-5.049648,2.813087,-9.188239,-5.409405,4.136124,-8.883046,-9.935376,-1.527999,-5.466404,-9.028082,4.085738,-9.599416,1.061374,-2.614536,-6.295528,-7.456538,-0.504424,1.726494,3.535027,-6.121406,-9.824978,-1.957478,-7.908617,0.422476,-2.193751,4.304497,-3.390691,-0.699110,3.151256,4.087821,-9.253010,-7.427743,-4.909554,4.857625,2.087247,-0.391399,7.617767,-9.402318,-6.971872,-6.726651,-4.647260,-6.581942,2.463478,-4.644292,-8.237845,-4.590804,-0.996907,5.666125,5.037656,-9.465176,-7.265570,-5.841681,-6.056891,8.668999,-7.759969,2.965583,-1.338819,6.105965,5.940797,-3.261256,-8.948477,-1.454510,3.650954,4.279407,-8.726059,0.501605,-1.259425,-2.675809,-6.059108,8.349782,5.243368,6.798993,1.624511,8.644528,2.455712,-9.218455,6.200263,-6.482353,-6.798590,0.023965,4.711226,4.335922,-7.809067,-1.464269,-1.009576,2.857231,2.478566,9.108106,5.697112,2.649470,-5.656258,-4.545224,-0.888520,-7.230867,-2.837542,5.240710,-3.139446,-2.065912,8.560662,2.089062,-5.489055,8.871290,-6.161169,-2.349596,-7.605630,-6.310224,0.511317,-9.456891,0.217711,-7.197573,-7.746322,1.746179,5.698787,8.883006,3.137367,-5.630024,5.461453,7.576372,-8.973925,0.919358,8.171158,1.135239,6.990247,-3.363494,-1.860883,-0.503472,-4.083053,7.755627,2.705752,-4.970580,5.061289,9.075763,2.303308,-7.524520,-1.815003,-8.476027,3.433734,2.293342,1.833004,5.751817,-3.115762,-4.895804,-0.635265,-6.402753,-5.314447,-1.934676,5.324368,-8.292641,-8.923136,-5.146829,-6.272874,-0.898589,-8.587211,-8.583726,8.044607,3.349697,-9.719956,-9.892099,5.348912,-9.140591,-8.716155,-6.569812,-2.704194,-7.520350,9.737836,-1.186712,4.614760,-9.995361,-3.298590,7.687611,-2.073319,5.778785,-4.184944,2.899076,8.457181,0.720099,-9.727686,8.287099,-6.401164,1.738148,4.130946,5.723986,-6.729128,-4.906325,0.861793,-9.208541,1.727155,-7.991470,-0.543099,0.843093,6.188319,8.259011,-6.218364,4.651699,-0.965101,0.126440,-4.209355,-9.044265,-1.656071,8.297128,-7.256873,9.777349,8.996277,7.652287,-9.051515,6.787430,8.319890,5.380895,-0.646182,-3.648291,-9.688796,-4.035022,-1.991314,3.775061,1.301319,-2.582715,6.052466,2.266756,1.946299,-6.887916,-7.012448,-5.258568,-8.332436,3.902044,-7.735003,2.672797,0.276329,7.176362,-9.307159,-4.654447,7.929698,1.151495,2.602701,5.065678,6.002606,-8.664268,-7.599918,4.552111,-8.942042,6.737238,-0.803625,5.573496,-0.781374,5.519216,-8.467735,-1.002941,5.719793,-3.203380,7.166770,6.194370,1.032488,-2.075285,-2.591439,-2.381415,-5.254512,6.835984,-3.572525,9.032061,9.610022,1.872673,-4.990545,2.022721,6.465168,-2.946885,-7.334326,3.607090,2.414118,3.452589,3.459844,9.457302,4.364095,-3.345356,6.705357,-6.348786,-9.475259,-9.867444,2.381066,-0.863394,1.695224,0.604480,3.332744,5.449704,-0.698027,-5.745794,-0.433698,-7.234914,0.419117,1.322199,-8.365398,1.208016,4.590441,6.588999,-9.016283,0.911844,2.093738,8.083019,7.680536,9.440715,0.809669,4.139855,4.222374,8.819935,-0.451646,-8.020101,-7.791345,-7.232030,8.465537,-1.696456,1.443357,-3.631194,4.140855,5.977838,-3.557238,-2.859244,8.024721,-0.337506,0.059557,8.503312,-1.253661,-3.619947,0.641457,1.672257,3.264225,-0.266885,8.568489,1.225963,-3.870191,-0.392108,5.831727,-0.808304,-2.361151,-7.319830,-1.979284,-2.172399,4.157473,9.421825,6.335524,3.228307,0.699473,6.128727,-0.270758,8.038155,-0.677246,-0.009552,-6.356463,-8.229506,6.428675,6.148376,-0.123935,-9.793305,-2.132229,-3.000448,-2.028206,-8.817163,-9.270896,8.100281,-0.413543,1.976025,-9.481675,5.190992,2.954427,3.171838,-7.063341,-5.530438,-1.169520,-4.455978,2.731608,-1.463282,-2.853222,1.909884,0.743377,-8.544586,1.146987,-3.556485,6.119869,-8.888735,1.861718,2.606482,-8.973331,-3.844264,-2.095018,-9.490803,8.536939,-1.677546,4.452561,-2.206041,-3.153435,1.452337,6.219627,5.974015,8.413534,7.186893,3.092752,-7.359150,-5.494210,8.774998,3.366399,-4.981859,-7.418793,-1.559492,-9.946153,-3.547496,8.497456,-3.692062,6.125545,0.141408,-6.260721,9.397213,1.049367,7.763940,-0.967622,6.964506,-3.589929,8.877892,-0.196017,1.033595,-3.311242,5.151315,2.545001,-7.342224,1.322760,3.489159,-8.260617,7.764824,-5.424162,-1.573108,8.939617,-5.937019,4.636346,3.349435,8.904465,9.356281,-7.057340,-6.410508,-5.815960,5.938304,-2.341494,3.345100,7.072524,8.136499,-2.146578,4.017359,6.160750,8.358965,2.747816,-4.023832,8.401507,-5.302015,-8.694368,7.312472,-1.247608,-9.250941,7.282892,1.719041,-2.473857,-8.946823,-5.076861,8.301300,3.160665,1.542832,2.743467,-1.312830,9.861734,-1.275480,8.461873,-1.729993,-4.737965,-9.762879,0.678429,0.876686,-2.602471,-3.621131,6.014598,-9.941245,-8.810828,8.578994,0.973438,3.849354,-6.862254,-5.881623,6.516619,3.979579,2.096285,-6.732011,-5.396065,8.338972,9.108899,4.593251,8.479761,-1.517753,2.428290,3.821576,1.380241,7.668745,-5.216904,5.129520,1.254182,-2.625889,-7.649485,9.886223,-5.375154,-1.255149,-9.919113,-4.053481,3.999698,6.341170,-4.382757,-6.983665,3.943859,6.066488,1.590872,-5.982767,-7.129720,-4.901427,6.350143,0.695014,-2.715317,5.726318,5.507928,-2.740572,-1.036815,-5.253747,-0.386067,-5.024904,-5.470600,0.161496,-5.274228,-5.809631,-9.571072,-9.521934,-6.127701,1.078351,7.889278,6.139130,-2.742502,0.875808,-5.504513,2.022383,-6.296392,-0.177926,-2.788283,4.317932,7.616654,9.989443,-4.774791,4.893837,4.261634,9.101835,-5.724749,0.461959,-2.487514,7.607234,-7.421787,6.495133,4.172834,-1.223221,9.693738,-8.483256,5.204914,8.644185,5.027312,4.803511,8.640112,2.726604,5.102835,3.472700,-8.279768,-2.975090,5.888024,5.858949,-2.632118,-2.725512,2.660630,-0.580829,-0.630350,-1.928718,5.473105,-7.802946,-1.161734,-9.203722,0.022512,1.544700,-3.168004,-3.208879,0.835843,-5.117905,8.741185,-3.260359,-8.011674,-1.392936,-7.245434,-5.556342,-6.166307,-9.195357,6.492835,-5.442746,-1.898156,-2.257850,-7.807935,6.332454,-8.574488,8.991534,-4.439751,7.065202,-3.754781,-3.020246,-1.081681,-7.102498,0.697613,-6.458561,2.007052,7.516459,-1.388506,0.436918,0.336563,5.491113,-2.617937,5.852039,-7.527416,2.611380,-2.382562,0.257277,4.025083,3.975054,-9.647900,3.914803,7.744256,-6.614811,-9.657346,-4.320960,-1.379453,6.117085,-2.169219,1.496788,6.069912,0.554561,-2.639567,7.882567,5.879157,8.762006,-5.162505,6.670702,1.716904,7.061257,7.450761,9.526312,4.696471,7.603632,-6.652819,-6.949555,5.509471,7.744546,-4.958950,2.105608,-0.687409,-0.563234,2.824704,-3.393105,8.454597,-5.265961,7.215332,-9.959146,7.546396,-4.318336,-1.147640,8.602422,-9.558603,-6.814875,3.245595,-3.712362,-4.922688,-1.599856,2.204269,-5.042299,4.118160,3.175682,2.001801,4.366135,1.853997,-0.018608,6.891550,-9.784932,-2.162886,-1.615265,-7.275134,7.643617,6.984972,7.861492,-3.779153,6.809301,-1.866364,-4.628867,-6.875919,-2.159667,6.332214,-4.271852,2.045500,9.604462,8.685968,3.040475,-2.181873,-4.346515,4.007283,-4.552832,2.711184,6.154957,0.859602,2.272919,1.068722,3.249857,-8.069279,8.326772,-6.762459,-3.327709,9.902381,-4.719413,-1.275920,9.107076,-6.785920,-8.796653,-3.484077,4.237674,3.623162,8.706142,4.177896,-6.883964,-9.880630,2.186284,-5.154888,-8.391595,4.844053,0.415421,3.735164,2.191948,2.290448,-3.637172,2.821516,2.373417,-2.860943,-7.560851,0.294594,-1.999527,-3.487333,5.630614,2.934704,-5.409442,-0.368542,-3.458913,5.096700,9.223111,7.435428,-1.181055,2.400012,-6.178678,-0.810181,1.574420,8.397861,-6.348074,7.103698,-1.548475,0.343675,-7.061704,-5.399628,-3.496365,-0.780251,-5.870432,9.518232,4.724172,-0.032053,-4.129364,-4.489563,2.741111,1.072737,7.908101,2.114217,5.265409,4.542086,-2.613080,4.709711,6.491437,-7.203274,6.123270,-5.874435,-4.222398,-6.302702,5.638850,6.401522,-8.884660,-8.706350,5.950972,8.535121,1.417336,-0.412267,8.451370,-1.375670,-6.135131,-0.927370,-5.564099,-7.711595,-8.101914,5.061369,6.789796,-2.075380,-9.911562,8.574642,-9.086626,-0.894061,6.759950,5.811058,-2.371703,6.393189,-2.524851,6.522308,-1.747695,8.082461,-0.230707,6.828138,1.766900,-4.343445,-1.938265,-8.661466,-1.586356,-6.057568,3.721610,-5.996451,1.347929,-0.805826,-0.394283,-4.375811,0.914436,0.325179,4.838191,8.555566,-1.919730,-7.114589,-5.004384,2.918455,9.112621,-1.377967,5.782230,1.917192,0.187918,-7.839676,4.941379,-6.543326,-5.080637,-0.999765,-1.845013,6.405107,4.778889,-1.669480,-0.292726,3.435634,1.724835,-7.273152,-4.474193,-7.344501,-2.711410,5.037922,7.261040,-4.198294,4.939178,7.623821,6.467865,-0.062068,-6.244055,-6.188486,-8.952714,9.154299,9.644133,-7.710509,6.086688,2.092024,2.238260,7.079338,8.814695,8.500113,-8.451812,-1.569089,2.909134,7.635065,9.872488,-0.310660,8.573762,-6.987954,4.117741,-1.622151,1.788446,-9.869521,1.171608,5.129671,-2.992574,4.510374,-9.075870,-6.317339,3.295552,7.702081,1.135316,-6.507891,7.391873,9.411394,-7.482733,2.044296,-3.115668,-1.068128,4.526472,-0.285312,-1.474121,9.396130,6.017387,-5.791560,5.005148,-4.921636,3.282759,9.361172,6.731434,-7.899797,-7.755927,9.144288,9.507719,-5.612228,8.867999,-6.592650,2.675430,-7.048735,0.731300,0.282358,7.121524,0.639369,-9.412696,0.175382,-7.306278,1.160673,-4.994504,2.903114,9.017217,-0.022435,-8.148420,-9.940922,-6.737855,-7.063434,-0.343988,-5.386614,3.038531,-7.579858,-9.415612,7.507727,9.499392,-7.442942,8.031762,-6.912281,9.696398,-7.238227,8.721125,0.164431,3.729136,-2.950073,3.876771,7.824098,-8.948328,7.006482,-3.265118,8.915279,2.795298,6.292569,0.677708,4.040460,-6.528230,-7.223057,1.988698,-4.986422,-2.415401,-8.273781,8.711534,-0.164933,5.380771,6.198873,5.382859,-2.456030,-3.947446,2.745040,4.594568,-4.702461,-3.150944,9.227064,8.114901,8.867389,-0.329807,0.861137,7.771769,-2.101284,0.278237,-8.157562,-0.648933,-1.372971,-1.207592,8.252158,-4.248574,-2.731578,-2.403025,-1.287342,3.294195,2.934949,9.117985,0.018238,0.755855,-0.801812,1.344526,8.983073,5.994928,-4.196680,3.918952,3.899121,-9.825973,1.806367,7.299113,-5.775705,8.555617,3.762176,-9.728019,0.414091,-1.188161,7.898565,7.792722,7.589830,-1.361313,-9.389718,1.431453,1.340373,1.501345,2.407638,9.353483,0.471941,6.972353,3.132214,-8.438195,5.887848,-6.389578,-3.987950,4.394749,-0.314492,-9.591853,-0.680877,-6.345505,5.074772,-4.559546,1.999543,-7.155281,-6.723838,3.510878,2.563754,-3.431182,-6.701897,4.704562,-3.400783,-5.529895,-3.653123,-6.214953,0.179069,4.679643,-9.784078,8.052590,4.515069,8.287402,1.707848,8.962777,-3.685019,-4.582398,6.073763,0.788005,-3.157551,-1.906878,-0.907447,3.768832,-1.485970,-9.066274,-3.309451,-8.923486,4.211056,6.863692,-2.862116,-5.606559,6.643545,7.321346,-8.157001,-0.256221,-2.175627,-4.203303,6.305728,-2.119669,-7.446647,3.292869,-3.912780,-9.919250,3.223902,0.090735,-1.989461,-5.757487,-3.296691,-7.403319,-9.530287,5.841518,-3.096462,-0.937551,-4.443431,5.221322,9.487835,8.311598,-3.079941,-3.206951,-4.375809,9.168768,0.953122,-1.796506,3.191848,-9.277041,8.366066,-4.783247,8.766883,-2.956781,-5.312658,-7.324982,-5.852152,2.114621,1.378614,-0.830965,7.505387,3.616236,9.160677,-6.968644,-2.116142,-6.227550,9.024706,2.339760,1.597118,-4.575316,9.319814,-1.081024,-7.349316,-2.574488,1.132409,1.601906,-3.074788,4.166383,-7.656308,-4.039768,-4.655628,4.772211,-7.952658,1.508867,-6.795462,6.279705,-0.008317,7.261812,3.434844,2.257660,-8.182483,-1.452943,3.768491,-1.979958,5.622417,-3.621740,7.182998,5.699970,2.710146,-5.000545,-1.810447,8.913229,0.456249,-7.690400,1.668238,2.885859,-2.178646,-5.972202,2.350892,-9.826416,-6.287591,-7.059261,-1.412901,8.591067,-1.383647,9.306042,0.324933,-7.860831,9.267030,4.738537,-0.543691,-8.437209,-1.918589,-9.646927,4.895249,0.073380,0.627059,0.341718,4.177225,1.274259,-1.336596,4.349678,-0.800608,-8.465936,-5.330416,-2.709133,-1.023590,7.461157,2.160828,-3.957643,-0.721314,-6.021848,-3.075839,6.497458,-6.664073,7.034279,7.128435,-7.077348,-2.254872,0.499554,4.162923,0.271235,-9.797508,-3.615734,-6.119363,-7.742628,-5.708752,3.734154,5.632234,7.768118,1.511329,-5.849788,1.443098,-6.184319,-5.694370,-5.159681,6.409721,5.270989,-1.932432,-8.379489,4.536313,-6.435396,3.838441,-9.058223,-2.817288,4.782951,-2.264651,6.903358,-7.528292,-3.678242,9.793528,-4.737316,-3.669264,4.247617,-7.849844,-4.715335,-0.405574,9.505976,-0.753065,-2.665131,7.077050,-7.775720,-6.079189,4.256169,-8.282308,5.411961,-5.840549,-1.813389,8.700798,-4.892167,5.375075,7.313240,6.884722,-0.490893,-8.654453,-3.977081,-9.020314,-7.925019,-2.715343,8.689444,2.953216,9.354263,3.202888,-9.371439,5.756033,-4.427290,8.520477,-8.562647,-6.010686,-8.569460,-1.825761,6.686005,-9.075502,9.790978,1.040385,3.746006,1.383926,0.989016,-0.916357,5.604759,-5.934316,1.092450,-5.694430,-7.944365,-0.775952,0.710186,5.013574,7.805480,-5.493704,3.610660,1.130296,-6.452497,8.749157,5.407269,-7.748187,5.138655,-3.706982,-3.001454,-9.626891,-0.630335,-0.102859,9.959144,-3.338188,7.093294,3.424437,-1.461527,1.617245,5.759854,-2.132730,-6.960113,-3.856519,7.150725,-2.907205,2.595619,-8.594634,4.710787,1.920722,5.266045,7.115796,1.514670,0.690510,-9.188784,-9.794888,4.414386,-3.216739,1.764673,5.069801,-5.399981,0.417480,-9.001937,5.572689], dtype = "float64")#candidate|3526|(2700,)|const|float64
call_3525 = relay.TupleGetItem(func_2795_call(relay.reshape(const_3526.astype('float64'), [15, 15, 12])), 0)
call_3527 = relay.TupleGetItem(func_2798_call(relay.reshape(const_3526.astype('float64'), [15, 15, 12])), 0)
output = relay.Tuple([call_3493,call_3508,const_3509,call_3525,const_3526,])
output2 = relay.Tuple([call_3494,call_3510,const_3509,call_3527,const_3526,])
func_3545 = relay.Function([], output)
mod['func_3545'] = func_3545
mod = relay.transform.InferType()(mod)
mutated_mod['func_3545'] = func_3545
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3545_call = mutated_mod.get_global_var('func_3545')
call_3546 = func_3545_call()
output = call_3546
func_3547 = relay.Function([], output)
mutated_mod['func_3547'] = func_3547
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_3640 = func_2910_call()
call_3641 = func_2910_call()
uop_3657 = relay.asinh(call_3640.astype('float64')) # shape=(14, 3, 15)
uop_3659 = relay.asinh(call_3641.astype('float64')) # shape=(14, 3, 15)
func_1637_call = mod.get_global_var('func_1637')
func_1641_call = mutated_mod.get_global_var('func_1641')
var_3669 = relay.var("var_3669", dtype = "bool", shape = (525,))#candidate|3669|(525,)|var|bool
const_3670 = relay.const([9.277643,3.986359,-8.733459,3.671090,9.389699,-6.162890,2.353063,-2.973040,-9.085305,1.823112,2.004639,2.897400,0.091500,-6.275462,9.381843,3.996657,-2.474287,8.207799,-2.920040,-3.147963,-9.505698,-6.416581,0.981542,3.584151,1.223072,0.688310,-3.562377,-6.877459,-3.746824,-5.385798,-9.366385,-0.714670,0.577402,5.102154,8.350912,9.969952,0.983056,0.576671,-6.943477,-3.948772,7.475352,-3.375172,-0.133863,-5.362214,4.531599,0.017917,-1.854793,2.670542,3.033941,-5.686176,-9.474456,-9.421282,4.952672,-6.960068,-9.206518,8.381119,-9.313670,0.685814,-1.749955,8.103482,6.861642,3.938094,9.477665,7.161488,-2.521946,1.493531,6.060499,-1.190336,4.684504,-6.446430,8.355734,8.301899,-2.538323,3.882314,-7.035321,-7.229458,2.150645,-6.748765,-2.216194,9.997457,3.671676,1.115220,-2.970500,8.524145,-5.412969,1.007613,0.423699,-3.799259,-9.015684,-0.140579,-9.297549,-2.194900,-4.558653,-4.559449,-3.129192,5.571191,-9.561592,-4.341339,-8.935731,-7.694886,7.230143,6.547097,5.197753,-5.638918,7.068347,-2.225361,-3.774661,8.425459,8.178557,1.267856,9.027966,9.739627,-9.553894,-3.828006,8.665765,0.851169,-1.115186,6.164378,-2.031350,4.182798,-3.414941,-8.223269,-1.781494,-4.849962,0.082121,2.083413,-2.911078,5.775745,-5.685830,-1.428344,-2.786777,5.775005,-8.533212,-0.686567,-1.505792,-0.139558,-7.270540,7.615743,-5.662506,-8.241513,-3.613241,-3.844824,4.428823,4.159174,9.788547,7.052347,7.573317,-2.331548,-6.442522,0.818260,7.939061,7.875596,-4.235850,-9.179085,-7.932970,-8.859246,3.310088,-3.973962,-8.578127,-4.997957,7.059332,-8.011125,-6.940478,-3.856169,5.911023,-7.497595,7.781789,-2.568101,-4.773650,-2.945071,-8.760310,2.962162,1.797251,-2.684101,4.240994,3.441322,-7.122774,-2.805058,-5.584027,8.969087,-9.196159,-4.728575,-8.818849,3.053923,-3.596396,7.614123,-3.145953,-8.566015,-7.625114,-4.466808,6.378058,-9.736001,2.280495,7.825130,2.405942,0.291342,-0.759371,5.733517,7.445196,2.677451,-3.736056,-0.109907,-0.618256,-4.920264,8.493946,-1.685462,-4.475704,-2.022656,6.715634,-4.193800,2.005022,-5.448600,5.582756,-4.435229,-0.759453,-3.936059,-9.756609,-0.689328,6.829245,-5.549653,6.765140,-7.706757,7.378539,3.280753,-4.398012,-8.054331,3.587352,4.302483,-0.831806,6.547198,3.682456,-3.309605,-1.184423,-7.753210,4.090025,-3.637738,-4.853614,8.753676,-9.678201,-7.046304,-8.453262,-9.237957,-3.289103,-3.012294,1.194535,9.062678,-4.650281,-9.404992,-6.888100,-5.318075,5.792334,-8.865080,1.121695,-8.260947,-4.960776,-4.748755,8.772485,8.968991,-1.945934,-1.752031,0.665987,8.429547,0.497310,5.165148,-5.577849,-9.021473,-5.932891,6.672932,-0.939547,6.120074,8.456557,6.199612,-5.472304,-8.398505,-6.441676,-7.351587,-7.779431,9.324048,-0.464930,-4.548168,7.910536,-2.240788,8.140289,7.911757,8.069892,4.904152,1.065709,1.793858,2.021497,-9.855534,7.940950,1.574093,-3.536412,0.529259,8.088518,-6.569877,-1.397364,2.814570,-2.585849,1.224478,1.522293,-9.450966,3.921568,1.604715,3.751170,4.641488,-3.253585,4.009950,4.080838,7.743230,-5.750084,7.725399,6.128436,-5.952338,-6.507815,3.358268,-9.262221,-5.749597,-2.080602,-4.674240,0.242098,-2.726958,2.459286,1.775979,-1.202428,0.434082,-1.585717,-3.619948,1.486551,6.250823,-8.803704,-6.284549,2.818881,5.395198,-1.337985,0.611376,1.782720,1.448024,8.189403,2.596931,-5.687785,-3.525560,-3.989956,-5.540769,-2.283881,5.568166,-2.368043,7.432325,-0.116916,6.728340,8.075128,-0.421754,-6.798704,1.472700,-5.627437,-1.379807,9.585343,5.985094,5.026261,-8.723377,-7.760780,-5.121008,2.907373,-8.466028,-2.800758,-4.375656,-4.676586,-7.151140,-6.730765,3.271508,1.168458,5.596706,-2.401279,-0.106024,-3.272068,6.412112,-4.755209,-7.482673,-9.425881,1.454917,-3.209629,-0.656035,-9.848892,-3.318461,-0.396729,-4.091304,6.702203,-8.595093,-2.336273,7.152408,7.075735,5.912218,-6.883142,5.470067,-1.094733,-7.550332], dtype = "float64")#candidate|3670|(396,)|const|float64
call_3668 = relay.TupleGetItem(func_1637_call(relay.reshape(var_3669.astype('bool'), [525,]), relay.reshape(const_3670.astype('float64'), [66, 6]), ), 2)
call_3671 = relay.TupleGetItem(func_1641_call(relay.reshape(var_3669.astype('bool'), [525,]), relay.reshape(const_3670.astype('float64'), [66, 6]), ), 2)
uop_3674 = relay.sin(uop_3657.astype('float64')) # shape=(14, 3, 15)
uop_3676 = relay.sin(uop_3659.astype('float64')) # shape=(14, 3, 15)
func_1056_call = mod.get_global_var('func_1056')
func_1059_call = mutated_mod.get_global_var('func_1059')
const_3684 = relay.const([4.154084,9.925570,-7.171192,6.680784,-4.124136,-4.266245,-5.304626,2.218195,1.069686,1.396250,-5.563198,7.584487,4.731471,5.106788,-5.665658,3.846714,2.827667,5.414048,4.311400,8.514998,9.378525,-3.841468,8.643973,-7.852853,3.492862,-9.755713,-1.918499,-9.225179,-6.388567,-8.841003,-3.272544,-7.364313,4.563970,9.133737,-3.119720,-6.412161,-1.584159,7.453418,9.386883,-1.879290,-0.903946,-2.496014,6.084245,-8.433235,-9.076240,-0.393839,-3.235463,-1.621404,-2.674513,4.171500,-1.956931,1.908532,-1.299659,7.155443,-7.505187,-1.337597,-0.182450,1.516511,5.901600,7.700598,6.021768,-9.582711,-5.629468,6.080324,-3.421916,-3.221274,-0.145983,0.510525,-7.723736,-2.921637,7.728406,1.689152,3.062720,0.161623,-6.270104,-5.625982,-6.652088,-6.953148,-7.774303,-7.290219,-3.058953,9.205381,-4.233058,8.199232,6.899993,8.086337,-9.934982,-3.293576,0.498908,-7.751892,-1.515171,8.454612,-5.029092,-1.285194,4.991334,8.001320,4.777145,0.936958,-2.788157,-1.372653,-4.746967,-5.320737,4.672459,0.335144,-4.822284,-3.245002,-0.302108,4.491290,7.123493,0.710434,-4.421540,-3.940654,-8.348837,5.300211,-7.366847,-8.056442,7.018930,3.414738,-6.350956,-4.827413,7.034363,6.147491,-2.559210,-8.108940,-4.597254,2.129767,-9.241685,-2.344045,2.734255,4.795892,-4.750244,-5.198018,-0.096676,-7.536318,-6.903590,7.771844,2.729491,-0.043314,-6.458164,-1.974545,-2.651309,5.727732,3.129812,3.246836,-6.139241,1.066899,0.375369,-5.933314,3.053292,-9.019370,5.800561,9.375764,-6.271110,4.439465,-6.913105,-7.767639,8.335676,-5.007110,5.944346,5.911340,-7.790771,-4.615094,-6.181422,-3.048015,2.473119,-5.331963,-3.446015,-7.420766,3.663848,1.637532,0.139320,-9.954005,-9.419867,8.645536,8.910365,4.300088,8.958932,9.947888,-9.940213,-7.869630,-0.632862,8.955977,-6.093216,8.176053,5.321840,-1.840595,-5.323428,8.406200,7.444035,4.611772,7.284070,-8.455902,-8.196019,-3.376710,5.097226,0.388512,2.547921,0.156865,-3.702609,3.047149,2.772563,-5.113764,5.944522,-7.784615,-4.399901,9.556829,-5.827330,9.228380,2.676892,-2.910209,-2.571438,-4.243583,-2.999747,6.088035,-6.220397,-4.087966,-6.192118,-8.881613,-7.839318,-8.455389,-0.464958,-4.623557,-5.553952,3.724281,2.374167,-3.557857,0.786408,-3.786129,-9.998822,-1.443228,-0.512218,7.063356,2.678993,-0.091414,-7.757040,6.343854,-2.997558,-7.860886,3.630491,-5.032310,8.919246,-5.965158,1.237474,-2.203870,-4.089625,8.017162,5.665847,-8.409577,-7.927183,-6.363063,1.331346,7.836612,6.015737,-4.613724,3.060781,9.703108,-3.478699,-4.829065,-6.138276,9.346918,4.963969,-6.014551,4.681042,-0.034054,4.542600,9.581991,-2.020563,8.395243,-0.817410,-1.631307,-6.384400,-5.935978,1.394458,1.165025,2.780407,-8.204731,1.691194,0.039228,8.869086,-1.681092], dtype = "float32")#candidate|3684|(280,)|const|float32
call_3683 = relay.TupleGetItem(func_1056_call(relay.reshape(const_3684.astype('float32'), [2, 10, 14])), 0)
call_3685 = relay.TupleGetItem(func_1059_call(relay.reshape(const_3684.astype('float32'), [2, 10, 14])), 0)
func_1637_call = mod.get_global_var('func_1637')
func_1641_call = mutated_mod.get_global_var('func_1641')
call_3689 = relay.TupleGetItem(func_1637_call(relay.reshape(var_3669.astype('bool'), [525,]), relay.reshape(const_3670.astype('float64'), [66, 6]), ), 3)
call_3690 = relay.TupleGetItem(func_1641_call(relay.reshape(var_3669.astype('bool'), [525,]), relay.reshape(const_3670.astype('float64'), [66, 6]), ), 3)
var_3696 = relay.var("var_3696", dtype = "float64", shape = (14, 3, 15))#candidate|3696|(14, 3, 15)|var|float64
bop_3697 = relay.bitwise_and(uop_3674.astype('uint32'), relay.reshape(var_3696.astype('uint32'), relay.shape_of(uop_3674))) # shape=(14, 3, 15)
bop_3700 = relay.bitwise_and(uop_3676.astype('uint32'), relay.reshape(var_3696.astype('uint32'), relay.shape_of(uop_3676))) # shape=(14, 3, 15)
bop_3716 = relay.power(uop_3657.astype('float32'), relay.reshape(uop_3674.astype('float32'), relay.shape_of(uop_3657))) # shape=(14, 3, 15)
bop_3719 = relay.power(uop_3659.astype('float32'), relay.reshape(uop_3676.astype('float32'), relay.shape_of(uop_3659))) # shape=(14, 3, 15)
output = relay.Tuple([call_3668,var_3669,const_3670,call_3683,const_3684,call_3689,bop_3697,bop_3716,])
output2 = relay.Tuple([call_3671,var_3669,const_3670,call_3685,const_3684,call_3690,bop_3700,bop_3719,])
func_3754 = relay.Function([var_3669,var_3696,], output)
mod['func_3754'] = func_3754
mod = relay.transform.InferType()(mod)
mutated_mod['func_3754'] = func_3754
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3754_call = mutated_mod.get_global_var('func_3754')
var_3756 = relay.var("var_3756", dtype = "bool", shape = (525,))#candidate|3756|(525,)|var|bool
var_3757 = relay.var("var_3757", dtype = "float64", shape = (14, 3, 15))#candidate|3757|(14, 3, 15)|var|float64
call_3755 = func_3754_call(var_3756,var_3757,)
output = call_3755
func_3758 = relay.Function([var_3756,var_3757,], output)
mutated_mod['func_3758'] = func_3758
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3545_call = mod.get_global_var('func_3545')
func_3547_call = mutated_mod.get_global_var('func_3547')
call_3782 = relay.TupleGetItem(func_3545_call(), 0)
call_3783 = relay.TupleGetItem(func_3547_call(), 0)
var_3793 = relay.var("var_3793", dtype = "float64", shape = (14, 3, 15))#candidate|3793|(14, 3, 15)|var|float64
bop_3794 = relay.maximum(call_3782.astype('int16'), relay.reshape(var_3793.astype('int16'), relay.shape_of(call_3782))) # shape=(14, 3, 15)
bop_3797 = relay.maximum(call_3783.astype('int16'), relay.reshape(var_3793.astype('int16'), relay.shape_of(call_3783))) # shape=(14, 3, 15)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_3800 = func_2894_call()
call_3801 = func_2894_call()
output = relay.Tuple([bop_3794,call_3800,])
output2 = relay.Tuple([bop_3797,call_3801,])
func_3810 = relay.Function([var_3793,], output)
mod['func_3810'] = func_3810
mod = relay.transform.InferType()(mod)
var_3811 = relay.var("var_3811", dtype = "float64", shape = (14, 3, 15))#candidate|3811|(14, 3, 15)|var|float64
output = func_3810(var_3811)
func_3812 = relay.Function([var_3811], output)
mutated_mod['func_3812'] = func_3812
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_3869 = func_2910_call()
call_3870 = func_2910_call()
output = call_3869
output2 = call_3870
func_3874 = relay.Function([], output)
mod['func_3874'] = func_3874
mod = relay.transform.InferType()(mod)
output = func_3874()
func_3875 = relay.Function([], output)
mutated_mod['func_3875'] = func_3875
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_3898 = relay.TupleGetItem(func_2459_call(), 0)
call_3899 = relay.TupleGetItem(func_2461_call(), 0)
output = relay.Tuple([call_3898,])
output2 = relay.Tuple([call_3899,])
func_3920 = relay.Function([], output)
mod['func_3920'] = func_3920
mod = relay.transform.InferType()(mod)
mutated_mod['func_3920'] = func_3920
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mutated_mod.get_global_var('func_3920')
call_3921 = func_3920_call()
output = call_3921
func_3922 = relay.Function([], output)
mutated_mod['func_3922'] = func_3922
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3172_call = mod.get_global_var('func_3172')
func_3174_call = mutated_mod.get_global_var('func_3174')
call_3950 = func_3172_call()
call_3951 = func_3172_call()
output = call_3950
output2 = call_3951
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
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_3961 = relay.TupleGetItem(func_2198_call(), 0)
call_3962 = relay.TupleGetItem(func_2200_call(), 0)
func_1637_call = mod.get_global_var('func_1637')
func_1641_call = mutated_mod.get_global_var('func_1641')
var_3982 = relay.var("var_3982", dtype = "bool", shape = (525,))#candidate|3982|(525,)|var|bool
var_3983 = relay.var("var_3983", dtype = "float64", shape = (396,))#candidate|3983|(396,)|var|float64
call_3981 = relay.TupleGetItem(func_1637_call(relay.reshape(var_3982.astype('bool'), [525,]), relay.reshape(var_3983.astype('float64'), [66, 6]), ), 1)
call_3984 = relay.TupleGetItem(func_1641_call(relay.reshape(var_3982.astype('bool'), [525,]), relay.reshape(var_3983.astype('float64'), [66, 6]), ), 1)
output = relay.Tuple([call_3961,call_3981,var_3982,var_3983,])
output2 = relay.Tuple([call_3962,call_3984,var_3982,var_3983,])
func_3986 = relay.Function([var_3982,var_3983,], output)
mod['func_3986'] = func_3986
mod = relay.transform.InferType()(mod)
mutated_mod['func_3986'] = func_3986
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3986_call = mutated_mod.get_global_var('func_3986')
var_3988 = relay.var("var_3988", dtype = "bool", shape = (525,))#candidate|3988|(525,)|var|bool
var_3989 = relay.var("var_3989", dtype = "float64", shape = (396,))#candidate|3989|(396,)|var|float64
call_3987 = func_3986_call(var_3988,var_3989,)
output = call_3987
func_3990 = relay.Function([var_3988,var_3989,], output)
mutated_mod['func_3990'] = func_3990
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4086 = relay.var("var_4086", dtype = "float32", shape = (2, 6, 5))#candidate|4086|(2, 6, 5)|var|float32
uop_4087 = relay.sigmoid(var_4086.astype('float32')) # shape=(2, 6, 5)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_4093 = relay.TupleGetItem(func_3920_call(), 0)
call_4094 = relay.TupleGetItem(func_3922_call(), 0)
output = relay.Tuple([uop_4087,call_4093,])
output2 = relay.Tuple([uop_4087,call_4094,])
func_4099 = relay.Function([var_4086,], output)
mod['func_4099'] = func_4099
mod = relay.transform.InferType()(mod)
var_4100 = relay.var("var_4100", dtype = "float32", shape = (2, 6, 5))#candidate|4100|(2, 6, 5)|var|float32
output = func_4099(var_4100)
func_4101 = relay.Function([var_4100], output)
mutated_mod['func_4101'] = func_4101
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1612_call = mutated_mod.get_global_var('func_1612')
call_4111 = relay.TupleGetItem(func_1611_call(), 1)
call_4112 = relay.TupleGetItem(func_1612_call(), 1)
output = call_4111
output2 = call_4112
func_4118 = relay.Function([], output)
mod['func_4118'] = func_4118
mod = relay.transform.InferType()(mod)
mutated_mod['func_4118'] = func_4118
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mutated_mod.get_global_var('func_4118')
call_4119 = func_4118_call()
output = call_4119
func_4120 = relay.Function([], output)
mutated_mod['func_4120'] = func_4120
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_4127 = relay.TupleGetItem(func_2198_call(), 0)
call_4128 = relay.TupleGetItem(func_2200_call(), 0)
output = relay.Tuple([call_4127,])
output2 = relay.Tuple([call_4128,])
func_4129 = relay.Function([], output)
mod['func_4129'] = func_4129
mod = relay.transform.InferType()(mod)
mutated_mod['func_4129'] = func_4129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4129_call = mutated_mod.get_global_var('func_4129')
call_4130 = func_4129_call()
output = call_4130
func_4131 = relay.Function([], output)
mutated_mod['func_4131'] = func_4131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3172_call = mod.get_global_var('func_3172')
func_3174_call = mutated_mod.get_global_var('func_3174')
call_4203 = func_3172_call()
call_4204 = func_3172_call()
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_4217 = relay.TupleGetItem(func_2459_call(), 0)
call_4218 = relay.TupleGetItem(func_2461_call(), 0)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_4241 = relay.TupleGetItem(func_1430_call(), 0)
call_4242 = relay.TupleGetItem(func_1432_call(), 0)
output = relay.Tuple([call_4203,call_4217,call_4241,])
output2 = relay.Tuple([call_4204,call_4218,call_4242,])
func_4245 = relay.Function([], output)
mod['func_4245'] = func_4245
mod = relay.transform.InferType()(mod)
mutated_mod['func_4245'] = func_4245
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4245_call = mutated_mod.get_global_var('func_4245')
call_4246 = func_4245_call()
output = call_4246
func_4247 = relay.Function([], output)
mutated_mod['func_4247'] = func_4247
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_4268 = func_2045_call()
call_4269 = func_2045_call()
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
var_4275 = relay.var("var_4275", dtype = "bool", shape = (35, 15))#candidate|4275|(35, 15)|var|bool
call_4274 = func_465_call(relay.reshape(var_4275.astype('bool'), [15, 7, 5]), relay.reshape(var_4275.astype('bool'), [15, 7, 5]), )
call_4276 = func_465_call(relay.reshape(var_4275.astype('bool'), [15, 7, 5]), relay.reshape(var_4275.astype('bool'), [15, 7, 5]), )
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_4277 = relay.TupleGetItem(func_1084_call(), 0)
call_4278 = relay.TupleGetItem(func_1086_call(), 0)
uop_4281 = relay.tan(call_4274.astype('float32')) # shape=(15, 7, 5)
uop_4283 = relay.tan(call_4276.astype('float32')) # shape=(15, 7, 5)
uop_4291 = relay.sin(uop_4281.astype('float64')) # shape=(15, 7, 5)
uop_4293 = relay.sin(uop_4283.astype('float64')) # shape=(15, 7, 5)
output = relay.Tuple([call_4268,var_4275,call_4277,uop_4291,])
output2 = relay.Tuple([call_4269,var_4275,call_4278,uop_4293,])
func_4298 = relay.Function([var_4275,], output)
mod['func_4298'] = func_4298
mod = relay.transform.InferType()(mod)
mutated_mod['func_4298'] = func_4298
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4299 = relay.var("var_4299", dtype = "bool", shape = (35, 15))#candidate|4299|(35, 15)|var|bool
func_4298_call = mutated_mod.get_global_var('func_4298')
call_4300 = func_4298_call(var_4299)
output = call_4300
func_4301 = relay.Function([var_4299], output)
mutated_mod['func_4301'] = func_4301
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_4399 = relay.TupleGetItem(func_2993_call(), 1)
call_4400 = relay.TupleGetItem(func_2995_call(), 1)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_4410 = relay.TupleGetItem(func_2351_call(), 0)
call_4411 = relay.TupleGetItem(func_2352_call(), 0)
output = relay.Tuple([call_4399,call_4410,])
output2 = relay.Tuple([call_4400,call_4411,])
func_4433 = relay.Function([], output)
mod['func_4433'] = func_4433
mod = relay.transform.InferType()(mod)
mutated_mod['func_4433'] = func_4433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4433_call = mutated_mod.get_global_var('func_4433')
call_4434 = func_4433_call()
output = call_4434
func_4435 = relay.Function([], output)
mutated_mod['func_4435'] = func_4435
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_4445 = func_3958_call()
call_4446 = func_3958_call()
func_1404_call = mod.get_global_var('func_1404')
func_1407_call = mutated_mod.get_global_var('func_1407')
var_4448 = relay.var("var_4448", dtype = "bool", shape = (5, 60))#candidate|4448|(5, 60)|var|bool
call_4447 = relay.TupleGetItem(func_1404_call(relay.reshape(var_4448.astype('bool'), [300,])), 1)
call_4449 = relay.TupleGetItem(func_1407_call(relay.reshape(var_4448.astype('bool'), [300,])), 1)
func_1322_call = mod.get_global_var('func_1322')
func_1326_call = mutated_mod.get_global_var('func_1326')
const_4451 = relay.const([[False,True,True,True,True,True,True,False,False,False,True,True,True,False,False],[True,True,False,False,True,True,True,False,False,False,False,True,True,True,False],[False,True,False,False,True,True,True,False,True,True,False,False,True,False,True],[True,True,False,False,True,True,True,True,False,True,True,False,False,False,True],[True,False,True,True,False,False,False,False,False,True,True,True,True,False,True],[False,False,False,True,False,False,False,True,True,False,False,False,True,True,False],[False,False,False,True,True,True,True,True,True,False,False,False,True,True,True],[False,False,True,False,True,True,False,True,False,True,False,False,True,True,True],[True,True,True,False,True,False,True,False,True,False,False,True,False,True,True],[True,True,True,False,False,False,True,False,True,True,False,True,False,True,False],[True,True,False,True,True,True,True,False,True,True,False,False,False,False,True],[True,False,True,False,False,True,False,False,True,False,True,True,True,True,True],[False,True,False,False,False,True,True,True,True,False,False,True,False,True,True],[False,False,True,True,True,False,False,True,False,True,True,True,True,True,True],[False,True,False,False,True,False,True,False,True,False,False,False,True,True,True],[False,True,True,False,False,False,False,False,False,False,True,True,True,False,False],[False,False,True,False,False,False,False,True,False,False,True,True,False,False,False],[True,True,True,False,True,True,True,True,True,True,True,False,False,False,True],[True,True,True,False,True,False,True,False,True,True,False,True,False,False,True],[False,True,False,True,True,True,False,False,False,True,True,True,False,False,False],[True,True,True,False,True,False,False,False,False,False,False,False,True,False,False],[False,True,True,True,False,True,False,True,True,True,False,True,False,False,True],[False,True,False,True,False,True,False,False,False,False,False,False,True,True,False],[True,False,True,True,True,False,False,True,True,True,False,True,False,True,False],[True,True,True,True,True,True,True,True,False,True,True,False,True,False,False],[True,False,False,True,True,True,True,True,False,False,False,True,True,True,False],[True,False,True,True,False,False,False,True,True,False,False,True,True,True,True],[True,False,True,True,True,False,False,False,True,False,False,False,True,False,True],[True,True,True,True,False,True,True,True,False,True,True,False,False,False,True],[True,True,False,True,False,True,True,False,False,True,True,False,True,False,False],[False,False,False,True,True,False,True,False,True,True,True,True,False,True,True],[True,True,True,True,False,True,True,True,False,True,False,True,True,True,True],[False,True,True,False,True,False,False,False,True,False,True,False,True,True,False],[False,True,True,True,False,True,True,True,False,True,False,True,False,False,False],[True,False,False,True,False,True,True,False,True,False,False,False,True,True,False]], dtype = "bool")#candidate|4451|(35, 15)|const|bool
call_4450 = relay.TupleGetItem(func_1322_call(relay.reshape(call_4445.astype('bool'), [14, 3, 15]), relay.reshape(const_4451.astype('bool'), [525,]), ), 2)
call_4452 = relay.TupleGetItem(func_1326_call(relay.reshape(call_4445.astype('bool'), [14, 3, 15]), relay.reshape(const_4451.astype('bool'), [525,]), ), 2)
uop_4453 = relay.atanh(call_4447.astype('float64')) # shape=(12, 5, 5)
uop_4455 = relay.atanh(call_4449.astype('float64')) # shape=(12, 5, 5)
uop_4464 = relay.asin(var_4448.astype('float32')) # shape=(5, 60)
output = relay.Tuple([call_4445,call_4450,const_4451,uop_4453,uop_4464,])
output2 = relay.Tuple([call_4446,call_4452,const_4451,uop_4455,uop_4464,])
func_4472 = relay.Function([var_4448,], output)
mod['func_4472'] = func_4472
mod = relay.transform.InferType()(mod)
mutated_mod['func_4472'] = func_4472
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4473 = relay.var("var_4473", dtype = "bool", shape = (5, 60))#candidate|4473|(5, 60)|var|bool
func_4472_call = mutated_mod.get_global_var('func_4472')
call_4474 = func_4472_call(var_4473)
output = call_4474
func_4475 = relay.Function([var_4473], output)
mutated_mod['func_4475'] = func_4475
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4492 = relay.var("var_4492", dtype = "uint16", shape = (10, 15, 14))#candidate|4492|(10, 15, 14)|var|uint16
var_4493 = relay.var("var_4493", dtype = "uint16", shape = (10, 15, 14))#candidate|4493|(10, 15, 14)|var|uint16
bop_4494 = relay.bitwise_or(var_4492.astype('uint16'), relay.reshape(var_4493.astype('uint16'), relay.shape_of(var_4492))) # shape=(10, 15, 14)
uop_4507 = relay.log10(var_4493.astype('float32')) # shape=(10, 15, 14)
output = relay.Tuple([bop_4494,uop_4507,])
output2 = relay.Tuple([bop_4494,uop_4507,])
func_4513 = relay.Function([var_4492,var_4493,], output)
mod['func_4513'] = func_4513
mod = relay.transform.InferType()(mod)
var_4514 = relay.var("var_4514", dtype = "uint16", shape = (10, 15, 14))#candidate|4514|(10, 15, 14)|var|uint16
var_4515 = relay.var("var_4515", dtype = "uint16", shape = (10, 15, 14))#candidate|4515|(10, 15, 14)|var|uint16
output = func_4513(var_4514,var_4515,)
func_4516 = relay.Function([var_4514,var_4515,], output)
mutated_mod['func_4516'] = func_4516
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2965_call = mod.get_global_var('func_2965')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_4545 = func_2965_call()
call_4546 = func_2965_call()
func_3754_call = mod.get_global_var('func_3754')
func_3758_call = mutated_mod.get_global_var('func_3758')
const_4551 = relay.const([True,False,True,True,False,True,False,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,False,True,False,False,True,True,True,False,False,True,False,True,True,False,True,False,True,True,True,True,True,False,False,True,True,False,False,False,False,False,False,False,False,True,False,True,False,True,True,False,False,True,True,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,False,False,True,False,True,True,True,True,False,True,True,True,False,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,True,True,False,True,False,True,True,True,False,True,True,False,False,False,True,False,True,False,True,True,False,True,False,False,False,True,False,False,True,False,True,True,True,True,False,True,False,False,True,False,True,False,False,True,False,False,True,False,False,False,True,False,True,True,True,True,True,True,True,False,True,False,True,True,True,False,False,True,False,True,True,True,True,False,False,False,False,True,False,False,False,True,False,True,False,True,True,True,True,False,False,False,True,True,True,False,True,False,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,False,False,False,False,False,True,True,True,True,False,True,True,True,False,True,True,False,True,True,False,True,True,False,False,True,True,False,True,False,True,False,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,True,True,True,True,True,False,False,True,True,False,True,True,True,True,False,True,True,False,True,False,True,True,True,False,False,True,False,False,True,True,False,True,False,True,False,True,False,False,False,True,False,True,False,True,False,True,False,False,True,False,False,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,True,True,True,False,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,False,False,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,True,False,False,True,False,False,True,False,True,True,False,False,False,True,True,False,True,True,True,True,True,True,False,False,False,False,True,False,False,True,True,True,True,True,False,True,True,True,True,False,False,True,True,False,True,False,False,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,False,True,False,True,False,False,False,False,False,True,True,True,True,False,True,False,True,False,False,True,True,True,True,False,False,False,False,True,True,True,False,False,False,True,True,True,True,True,True,True,False,False,True,False,True,False,False,False,True,False,True,False,True,False,False,True,True,False,False,False,True,True,False,False,False,True,True,True,True,False,False,True,False,True], dtype = "bool")#candidate|4551|(525,)|const|bool
call_4550 = relay.TupleGetItem(func_3754_call(relay.reshape(const_4551.astype('bool'), [525,]), relay.reshape(call_4545.astype('float64'), [14, 3, 15]), ), 4)
call_4552 = relay.TupleGetItem(func_3758_call(relay.reshape(const_4551.astype('bool'), [525,]), relay.reshape(call_4545.astype('float64'), [14, 3, 15]), ), 4)
func_1040_call = mod.get_global_var('func_1040')
func_1042_call = mutated_mod.get_global_var('func_1042')
call_4557 = relay.TupleGetItem(func_1040_call(), 0)
call_4558 = relay.TupleGetItem(func_1042_call(), 0)
func_2588_call = mod.get_global_var('func_2588')
func_2593_call = mutated_mod.get_global_var('func_2593')
const_4568 = relay.const([10,9,6,-9,2,4,-6,-9,4,3,8,5,3,-5,9,-9,1,-8,-5,-4,2,3,10,6,-5,-6,-2,4,-6,-8,-1,8,8,-9,-5,-10,-8,-9,-2,-4,2,2,2,-7,7,7,-6,-9,3,7,-8,-6,-9,-9,-8,10,3,-3,-9,5,-10,3,-9,10,10,-9,4,7,8,4,8,-7,-5,-8,-5,-10,7,-2,-6,8,10,4,-1,-9,6,-9,7,-5,-8,-9,-6,-9,2,9,4,2,5,7,-7,-8,-10,-9,-3,-1,7,-6,-9,-8,-8,9,-6,-5,-6,-10,-1,-10,-5,7,-5,-1,-8,-7,-5,8,-6,5,-7,-5,-3,8,3,-2,-8,8,-9,6,-9,-6,10,8,-10,-7,1,10,9,5,-7,-2,-10,-8,1,-8,-9,-5,-8,-6,-3,-5,-7,8,4,-9,2,8,4,-3,-4,-3,5,3,-10,2,-3,6,2,9,-9,9,-10,3,4,8,7,10,-1,5,-3,-5,-6,8,6,5,6,7,10,-3,-6,-10,-4,6,3,-7,2,3,-2,5,-2,1,4,-5,8,7,-9,-10,7,-8,-9,7,6,9,-4,-6,-7,-4,7,-5,9,10,9,3,-7,-6,-6,8,-6,-10,5,7,-2,-3,2,3,-10,-1,4,4,-5,-8,5,2,4,2,-7,3,1,10,6,7,8,-4,4,-4,10,9,-9,-7,-3,4,9,9,5,-3,3,-4,2,5,-8,6,-2,-5,7,4,10,-10,-5,-9,10,-1,6,6,-5,-5,-10,3,5,3,-10,4,4,1,4,-2,-3,-9,-10,8,-6,8,-3,9,9,-2,8,-8,-9,-6,10,9,-2,-4,-3,-8,5,-8,9,6,1,8,3,6,7,-5,1,-10,-10,7,-7,6,-3,2,-2,-3,-6,4,8,-1,1,10,8,7,4,-5,1,5,-4,9,5,2,-2,1,6,3,-8,1,4,-5,-4,-1,10,10,-3,3,-10,9,1,1,4,5,8,-7,4,1,2,4,6,-9,2,6,7,3,9,-7,8,6,-8,8,-7,-1,-9,-3,8,5,-4,-1,10,10,7,-4,-9,-3,-3,10,-10,-7,5,-5,1,-6,-2,-7,2,10,5,8,-4,1,-4,5,2,-4,-3,-4,10,1,-7,-2,8,-10,-8,8,-9,-9,-10,6,8,2,10,8,-6,-2,9,-1,6,9,10,-7,-6,2,1,-1,10,10,7,-2,9,7,-5,-5,10,6,5,10,10,-9,-10,9,4,-3,-9,6,-8,6,-1,-8,-8,2,-10,5,4,8,-6,7,-6,1,-5,3,-7,-9,-3,1,1,-5,6,8,7,4,-5,-3,1,-8,10,10,-2,6,-5,-7,10,7,5,6,5,5,-10,3,-2,-8,2,-10,8,-10,-4,-3,-2,-10,8,-10,5,5,4,7,-8,-8,4,5,-3,8,3,-2,2,3,-6,-4,-8,6,-6,-8,7,-5,4,-4,-4,-6,4,3,10,9,-8,-6,-2,8,5,-2,-4,5,6,6,-4,8,-2,7,8,-9,8,5,-8,-8,1,-7,-9,-4,4,5,-4,-9,6,10,9,-4,-3,-7,-4,-7,-8,-9,-9,-10,-4,-2,-9,-5,-6,-1,-2,-3,6,9,-6,-4,-1,1,-7,-2,7,-9], dtype = "uint8")#candidate|4568|(624,)|const|uint8
const_4569 = relay.const([5.570436,8.134684,-0.078068,-2.934421,4.990329,-6.566305,-8.632418,-5.491376,8.102098,-2.679432,-3.252532,-5.104995,2.571119,3.359052,7.161017,3.276980,-2.876746,-5.799623,7.535607,-5.026057,6.065065,-3.808891,4.400343,-6.159183,-8.012940,-8.597204,4.927923,2.174591,-3.061207,1.815875,8.249209,-7.524886,-8.729699,-9.482269,-1.257557,-7.944755,-8.106623,0.194077,9.323420,-2.611845,-6.361108,-5.631671,2.918560,9.836534,-1.485009,-4.546341,2.470808,9.307084,4.568141,-8.360860,-2.759669,2.955329,0.919291,-2.424618,-2.132069,4.577411,6.998837,-4.130628,4.263642,9.974359,9.473913,-0.220198,-8.522798,-9.267469,9.563486,9.229803,5.228905,-4.401115,1.090600,7.846170,8.764634,8.081551,-0.050996,-7.813118,5.845353,3.518432,0.186224,1.178464,4.411592,7.985661,-3.402138,-7.990123,9.299901,4.956735,7.807080,4.279222,9.806179,-4.095199,-7.743826,6.320393,-2.418047,-8.214878,-2.654491,8.902369,3.596407,9.452628,-9.397594,2.944839,-1.931320,-3.316605,4.254996,2.361821,-4.496384,-2.400256,-3.030140,-1.822097,-0.922936,-2.214245,4.238097,-9.908758,-7.465837,-8.880258,1.287061,-6.110924,-5.650548,-0.315484,-2.034703,-5.026693,6.151556,-0.667795,0.078619,-6.868581,1.547997,-3.135036,-6.446140,-6.347679,-3.370609,5.826425,-3.402028,-5.871596,4.412662,0.094594,-3.458112,-7.026616,-0.950025,3.797941,-8.667133,-7.149119,-9.924585,-9.930964,7.249534,8.710599,2.086018,-8.961999,-6.410946,4.255289,2.305062,-3.662974,-8.196695,3.004127,0.339730,-1.886264,-0.580835,5.980674,-9.756727,5.451648,-0.038484,7.712579,-4.752479,-7.354937,-7.270938,-4.155546,-8.004878,2.428142,9.720026,6.979328,4.846180,-7.110156,-6.854291,-3.894328,1.158952,7.357503,-7.059526,-6.624778,-2.731108,-6.200694,-5.462491,-1.846809,2.327241,8.731397,-7.893893,2.437170,5.976638,0.718985,8.803073,-3.105102,4.583384,9.451336,-6.919059,-9.563354,-6.828320,-7.392245,1.989014,9.361851,-0.744035,-5.679620,3.996477,8.563513,6.484564,4.668153,-3.693738,-7.598570,9.549815,-2.305738,0.168277,-0.775543,3.293959,-1.507611,6.488437,6.848852,-7.462752,-6.847724,9.345472,-5.181479,-0.068767,1.356117,6.344621,-9.440805,4.147750,4.835506,-0.567065,-3.066852,-4.354296,-9.574637,-4.015963,1.257213,2.377454,8.119522,4.408298,-1.972393,3.213035,4.343932,4.357212,7.130956,-3.884995,8.536429,-9.543480,-2.558492,-6.531791,-7.542429,-4.123412,1.619631,0.329286,-3.047985,3.201960,-6.424641,-9.716685,0.960467,2.026888,9.016590,4.638449,-1.667600,-5.503723,-0.864517,-0.401281,-1.663858,0.091952,-9.969178,-3.647122,8.832922,7.699885,-7.825455,1.883445,2.008415,-3.982271,-7.650152,9.485720,1.713269,0.232165,-7.491177,-9.777253,-0.833943,9.020288,-7.983103,0.639530,5.197117,5.522802,6.100305,1.328463,1.217385,6.214515,-0.215144,3.255772,-5.640679,8.527823,-8.823269,1.647747,6.453659,5.968267,-1.570532,-9.933257,-9.683793,1.374669,-8.328316,-4.029572,-9.795970,-3.446987,2.232082,-6.535105,-5.155849,-6.848245,8.052759,-3.242242,-3.558194,-9.310033,-9.856175,-4.500040,-0.588074,-5.827244,4.168241,5.650300,-1.362148,-3.101374,0.635391,-6.188785,-9.915354,-3.782391,-0.688493,3.860677,-4.524135,-2.180756,-5.113594,1.311806,-2.792754,9.573362,3.770108,-6.666125,-0.386057,1.734381,7.767121,-9.538969,-2.703651,-9.507603,7.685501,-2.736557,2.700261,-6.580765,1.204323,7.833597,-5.943701,3.538546,5.434789,5.723021,-2.544198,9.409048,-1.143991,-3.025216,-3.964015,-9.425265,-0.984589,8.205668,0.290790,2.125303,-1.901044,-1.929068,9.343621,-8.443544,1.670674,2.668906,-9.551434,-1.329164,-4.341959,8.759592,8.549582,-1.358019,-0.285364,3.805494,2.418580,7.102214,2.235093,-1.257944,1.863873,9.501779,9.679344,7.058635,7.742106,-8.666409,-0.735349,-0.053800,4.320404,9.611980,3.526984,7.710150,0.928527,-8.702027,5.248962,1.927530,4.718518,2.427711,1.982305,-6.977273,-7.813743,-2.297164,-2.444504,-5.725192,3.438926], dtype = "float64")#candidate|4569|(396,)|const|float64
call_4567 = relay.TupleGetItem(func_2588_call(relay.reshape(const_4568.astype('uint8'), [13, 16, 3]), relay.reshape(const_4568.astype('uint8'), [13, 16, 3]), relay.reshape(call_4550.astype('float32'), [280,]), relay.reshape(const_4569.astype('float64'), [396, 1]), ), 13)
call_4570 = relay.TupleGetItem(func_2593_call(relay.reshape(const_4568.astype('uint8'), [13, 16, 3]), relay.reshape(const_4568.astype('uint8'), [13, 16, 3]), relay.reshape(call_4550.astype('float32'), [280,]), relay.reshape(const_4569.astype('float64'), [396, 1]), ), 13)
output = relay.Tuple([call_4545,call_4550,const_4551,call_4557,call_4567,const_4568,const_4569,])
output2 = relay.Tuple([call_4546,call_4552,const_4551,call_4558,call_4570,const_4568,const_4569,])
func_4571 = relay.Function([], output)
mod['func_4571'] = func_4571
mod = relay.transform.InferType()(mod)
mutated_mod['func_4571'] = func_4571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mutated_mod.get_global_var('func_4571')
call_4572 = func_4571_call()
output = call_4572
func_4573 = relay.Function([], output)
mutated_mod['func_4573'] = func_4573
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1817_call = mod.get_global_var('func_1817')
func_1819_call = mutated_mod.get_global_var('func_1819')
call_4666 = func_1817_call()
call_4667 = func_1817_call()
output = relay.Tuple([call_4666,])
output2 = relay.Tuple([call_4667,])
func_4684 = relay.Function([], output)
mod['func_4684'] = func_4684
mod = relay.transform.InferType()(mod)
mutated_mod['func_4684'] = func_4684
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4684_call = mutated_mod.get_global_var('func_4684')
call_4685 = func_4684_call()
output = call_4685
func_4686 = relay.Function([], output)
mutated_mod['func_4686'] = func_4686
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_4724 = relay.TupleGetItem(func_4571_call(), 5)
call_4725 = relay.TupleGetItem(func_4573_call(), 5)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_4726 = relay.TupleGetItem(func_3920_call(), 0)
call_4727 = relay.TupleGetItem(func_3922_call(), 0)
func_3172_call = mod.get_global_var('func_3172')
func_3174_call = mutated_mod.get_global_var('func_3174')
call_4728 = func_3172_call()
call_4729 = func_3172_call()
func_1322_call = mod.get_global_var('func_1322')
func_1326_call = mutated_mod.get_global_var('func_1326')
const_4733 = relay.const([True,False,False,True,True,False,False,False,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,False,True,False,True,True,True,True,True,True,True,True,False,True,True,False,True,False,False,True,False,True,False,False,True,False,True,False,False,True,False,False,False,True,False,True,False,False,False,True,True,False,False,True,True,True,True,False,True,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,True,False,True,False,True,True,True,True,False,True,False,True,True,False,False,False,True,False,False,False,False,True,False,False,False,False,True,False,True,False,False,False,True,True,False,False,False,False,True,False,True,True,True,False,False,False,False,True,False,False,False,False,True,False,False,False,True,True,False,False,False,True,True,True,False,True,True,True,True,True,True,False,False,True,False,False,True,False,False,True,True,False,True,False,False,True,False,True,True,True,False,True,False,True,False,False,False,True,True,False,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,False,False,True,True,True,False,True,False,False,False,False,True,True,False,False,True,False,True,True,True,True,False,True,False,False,False,False,False,False,True,True,False,False,True,True,True,True,True,False,False,True,False,True,False,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,True,False,True,False,True,False,False,False,False,False,False,True,True,False,True,False,False,False,True,True,True,False,False,False,True,False,False,False,False,False,True,True,False,False,False,False,True,False,False,True,False,False,False,True,True,False,True,True,False,True,False,True,True,False,False,False,False,False,False,False,True,False,False,True,False,False,True,True,False,False,True,False,False,True,True,True,True,False,False,False,True,False,True,False,True,True,False,True,False,True,False,True,True,False,False,True,False,False,True,False,False,False,False,False,True,True,False,True,True,False,True,True,True,False,True,False,False,False,True,False,True,True,True,False,True,True,True,True,True,False,True,True,False,True,False,False,False,False,True,False,False,False,True,True,False,False,True,False,False,True,False,True,False,True,True,False,True,True,True,False,True,True,False,False,False,False,False,True,False,True,True,False,True,False,False,True,False,True,False,True,False,False,False,True,False,False,True,True,True,False,True,False,True,True,False,False,True,False,True,True,True,False,False,False,False,False,False,False,True,False,True,False,False,False,True,False,False,False,True,True,False,True,True,False,False,False,False,False,False,True,True,False,True,True,False,True,True,False,True,True,False,True,True,True,True,False,True,True,False,True,False,False,False,True], dtype = "bool")#candidate|4733|(525,)|const|bool
call_4732 = relay.TupleGetItem(func_1322_call(relay.reshape(call_4728.astype('bool'), [14, 3, 15]), relay.reshape(const_4733.astype('bool'), [525,]), ), 1)
call_4734 = relay.TupleGetItem(func_1326_call(relay.reshape(call_4728.astype('bool'), [14, 3, 15]), relay.reshape(const_4733.astype('bool'), [525,]), ), 1)
var_4737 = relay.var("var_4737", dtype = "bool", shape = (15, 7, 5))#candidate|4737|(15, 7, 5)|var|bool
bop_4738 = relay.divide(call_4732.astype('float32'), relay.reshape(var_4737.astype('float32'), relay.shape_of(call_4732))) # shape=(15, 7, 5)
bop_4741 = relay.divide(call_4734.astype('float32'), relay.reshape(var_4737.astype('float32'), relay.shape_of(call_4734))) # shape=(15, 7, 5)
bop_4742 = relay.mod(call_4728.astype('float32'), relay.reshape(call_4726.astype('float32'), relay.shape_of(call_4728))) # shape=(14, 3, 15)
bop_4745 = relay.mod(call_4729.astype('float32'), relay.reshape(call_4727.astype('float32'), relay.shape_of(call_4729))) # shape=(14, 3, 15)
func_2045_call = mod.get_global_var('func_2045')
func_2047_call = mutated_mod.get_global_var('func_2047')
call_4747 = func_2045_call()
call_4748 = func_2045_call()
func_4245_call = mod.get_global_var('func_4245')
func_4247_call = mutated_mod.get_global_var('func_4247')
call_4749 = relay.TupleGetItem(func_4245_call(), 1)
call_4750 = relay.TupleGetItem(func_4247_call(), 1)
func_3149_call = mod.get_global_var('func_3149')
func_3153_call = mutated_mod.get_global_var('func_3153')
const_4768 = relay.const([3.853430,4.519070,3.236739,0.997939,-9.900422,0.144859,-2.757885,-4.076409,-0.796793,-6.663229,6.323949,-5.645826,-2.103886,-6.148762,4.911891,-7.091770,1.960760,-4.081601,-7.130087,-1.732192,0.898494,-8.485268,-4.570566,7.006326,7.919601,-6.294189,-2.210187,7.173158,-5.340031,-9.429380,8.064263,-4.986296,-3.737666,5.478135,-0.709831,2.661740,4.412437,-0.705196,-3.732717,1.369141,4.216277,6.630839,-1.740918,-5.489832,-0.566067,-1.146812,3.116800,2.313145,-4.870290,-8.367073,-9.375327,-2.589901,-2.489615,-7.485804,-9.467018,-4.870411,7.311904,-1.857637,4.496298,6.832532,7.574403,1.712133,-2.378188,5.950385,4.083311,-0.962228,2.915502,-1.088702,0.847033,7.687878,-9.206890,7.962349,9.605043,3.609310,1.729031,-7.076705,-1.931302,4.179845,-2.329297,8.903696,1.554405,-3.161212,2.048177,-8.427941,1.361385,-1.044538,7.533132,2.886043,7.211774,4.310466,5.831080,-8.863122,8.026544,1.567333,-3.013777,-1.596901,-5.333699,-0.958098,4.581010,-0.329077,-9.081071,-2.356538,-1.495391,-0.023893,-4.299530,-3.876573,-3.453448,8.602025,0.024099,8.833269,-1.990054,8.739515,-4.115529,-7.333238,-7.851337,-5.087694,0.383187,-1.483424,7.224287,-4.469066,5.870030,4.090061,7.798303,6.996574,8.762563,-4.657792,-7.281731,-8.240854,0.530760,-1.826529,6.081395,5.687358,7.230697,3.705387,-3.141451,-7.501958,-5.270096,6.738967,7.093254,-3.148113,-2.175206,-9.741852,-1.047088,2.806580,7.879733,9.367505,5.084333,6.329830,5.467540,8.141999,-3.115695,1.417770,7.096694,-7.078533,4.485495,-4.135752,8.355809,3.902374,2.362235,-1.936465,-0.944183,-3.575229,-1.837506,1.476995,-8.400679,0.705964,-5.016951,0.336809,-5.861223,-3.794550,1.709694,7.568919,7.985868,-1.179846,5.191891,4.000183,0.077993,0.038497,-7.618120,2.755202,0.648535,4.017760,5.941566,-5.488881,8.741006,6.834554,1.426512,7.312810,5.012704,0.856197,-7.711565,5.456145,-3.789194,5.293828,5.877153,0.905445,-7.791545,-3.992360,-3.194834,2.004340,-8.283145,-9.243126,6.076470,-9.117294,1.196956,7.676064,5.599212,3.038933,-3.868968,-2.769329,4.792596,-7.542499,-0.835619,6.559959,1.304292,-3.199220,-7.986098,4.041523,8.987549,-6.662516,-4.202125,-2.941518,-9.637935,9.407162,4.314827,-2.599390,-1.837781,-6.133674,-2.868315,3.697461,-7.041597,2.129949,-1.542684,-7.841301,-1.633582,-0.943092,-0.884575,-5.943986,7.307130,6.922360,0.192598,1.449305,0.916358,9.374719,-5.391173,7.656280,-3.474184,5.420780,-4.971882,-1.309074,-5.124679,3.587376,-2.805829,-0.161146,8.921571,-9.208564,3.233682,-7.449197,6.417774,-7.747059,-8.376939,-1.099642,-4.781460,6.821490,1.438244,-6.093635,3.085939,-2.833074,5.386771,1.563704,9.933983,-8.485691,0.858486,6.784175,-8.961537,-4.556388,9.513812,6.501578,-7.033399,-8.870750], dtype = "float32")#candidate|4768|(280,)|const|float32
const_4769 = relay.const([-2,1,1,2,-3,-10,-2,-1,-7,8,1,-1,-2,-6,-3,7,5,5,-1,9,-3,3,9,-8,-6,-6,4,5,2,-2,-10,4,-6,1,-8,-3,7,-8,-2,5,-5,-5,10,4,-3,9,-5,7,2,1,8,4,-10,4,-1,9,1,4,6,-3,6,2,-7,-5,7,-2,9,-10,8,-10,2,6,5,-5,10,10,2,-7,3,9,-7,-4,-8,-5,10,-7,5,8,-3,-1,-2,9,4,-4,-8,-6,-5,1,-9,-10,-2,-3,-10,8,-5,4,-1,1,1,-4,-10,3,-5,9,-1,-2,7,9,-10,9,-6,-3,10,-6,-9,9,5,3,6,-3,-4,-7,4,-6,-5,-8,-2,1,4,10,-10,-1,8,-4,-9,-1,-3,1,8,-2,4,5,-10,5,-4,7,3,10,3,8,-2,-4,9,4,3,-10,5,-5], dtype = "uint8")#candidate|4769|(168,)|const|uint8
var_4770 = relay.var("var_4770", dtype = "float32", shape = ())#candidate|4770|()|var|float32
call_4767 = relay.TupleGetItem(func_3149_call(relay.reshape(const_4768.astype('float32'), [70, 4]), relay.reshape(const_4769.astype('uint8'), [168,]), relay.reshape(var_4770.astype('float32'), []), ), 2)
call_4771 = relay.TupleGetItem(func_3153_call(relay.reshape(const_4768.astype('float32'), [70, 4]), relay.reshape(const_4769.astype('uint8'), [168,]), relay.reshape(var_4770.astype('float32'), []), ), 2)
output = relay.Tuple([call_4724,const_4733,bop_4738,bop_4742,call_4747,call_4749,call_4767,const_4768,const_4769,var_4770,])
output2 = relay.Tuple([call_4725,const_4733,bop_4741,bop_4745,call_4748,call_4750,call_4771,const_4768,const_4769,var_4770,])
func_4775 = relay.Function([var_4737,var_4770,], output)
mod['func_4775'] = func_4775
mod = relay.transform.InferType()(mod)
var_4776 = relay.var("var_4776", dtype = "bool", shape = (15, 7, 5))#candidate|4776|(15, 7, 5)|var|bool
var_4777 = relay.var("var_4777", dtype = "float32", shape = ())#candidate|4777|()|var|float32
output = func_4775(var_4776,var_4777,)
func_4778 = relay.Function([var_4776,var_4777,], output)
mutated_mod['func_4778'] = func_4778
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2965_call = mod.get_global_var('func_2965')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_4824 = func_2965_call()
call_4825 = func_2965_call()
output = relay.Tuple([call_4824,])
output2 = relay.Tuple([call_4825,])
func_4858 = relay.Function([], output)
mod['func_4858'] = func_4858
mod = relay.transform.InferType()(mod)
output = func_4858()
func_4859 = relay.Function([], output)
mutated_mod['func_4859'] = func_4859
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_4875 = relay.TupleGetItem(func_2459_call(), 0)
call_4876 = relay.TupleGetItem(func_2461_call(), 0)
output = call_4875
output2 = call_4876
func_4885 = relay.Function([], output)
mod['func_4885'] = func_4885
mod = relay.transform.InferType()(mod)
output = func_4885()
func_4886 = relay.Function([], output)
mutated_mod['func_4886'] = func_4886
mutated_mod = relay.transform.InferType()(mutated_mod)
var_4889 = relay.var("var_4889", dtype = "float64", shape = (9, 10, 16))#candidate|4889|(9, 10, 16)|var|float64
const_4890 = relay.const([[[9.918554,3.450358,2.859046,-8.647408,-1.953917,-4.059232,6.703049,4.857303,2.375019,0.206975,5.432536,8.037635,8.260620,-5.438901,-4.055421,-6.522533],[6.898030,-3.912136,3.191764,-5.513223,5.640242,4.543076,-6.083446,-6.307314,6.649598,0.544525,-6.907111,-7.358990,0.362397,6.709871,-8.561806,0.385449],[9.782813,4.190292,-7.635303,9.736509,-9.459298,-3.182252,9.801614,-2.189848,7.683170,4.053243,-4.478809,9.315846,-3.973669,-0.857321,-2.156104,-4.659222],[5.944545,-9.006120,7.695459,9.023115,-7.217330,-3.313995,-8.946347,-1.707355,3.277540,5.229217,1.599288,6.273353,-3.194021,5.239155,9.901790,-2.280050],[5.164675,-3.644854,-3.339907,-6.498419,8.984776,7.974095,6.115358,4.624121,8.268982,3.444272,3.979150,8.722797,-8.809209,-6.869513,-7.597154,-4.028261],[0.374640,0.592820,4.102369,-2.660973,-4.459781,-3.805945,7.091083,-9.121075,0.695208,-1.543595,-1.123879,-8.846553,-3.781114,-4.715021,2.990290,-2.294944],[2.114203,1.298893,1.040245,-0.367237,3.353002,6.059762,-3.668372,3.461243,5.742235,7.893782,3.375086,-8.075372,-3.298598,4.955720,-6.921661,2.851718],[2.919299,-8.616310,-5.245152,-9.048656,7.800988,1.039775,-6.748519,9.834338,-6.225033,7.228336,-7.260301,2.226239,8.001742,9.588841,-3.438794,1.391701],[9.895024,-2.514330,-1.181722,9.992626,-1.269750,-5.606245,2.845637,9.956071,-1.959079,-8.729241,-1.917090,1.816682,-5.427489,5.095461,2.483376,-9.687768],[-9.578192,7.210810,0.130039,0.744241,7.379307,-8.075550,2.157636,-0.729327,8.400275,2.711217,-3.599485,5.869348,1.708450,9.594288,1.108558,0.675825]],[[-5.544881,8.822688,8.695545,0.925768,-7.362090,3.233018,3.679155,9.338479,-9.071211,2.061095,0.490135,3.035329,5.877002,-7.535523,-2.508306,6.779298],[-0.371645,0.433631,1.592298,-4.319136,-9.097192,2.183915,7.915111,-6.217004,3.518919,-7.670073,-9.242311,9.556498,-1.269665,1.206890,6.052003,9.061533],[5.516244,9.578671,0.270005,-6.621280,-3.081095,-0.106778,-6.616547,4.552874,-8.201703,-7.018328,-6.115180,-9.993151,5.075241,5.834432,-2.765570,-1.912022],[3.832137,-1.218091,9.662328,7.716837,4.819235,9.685648,-5.169806,1.246468,-7.595387,-9.099100,-7.045193,6.385346,-3.878099,-3.264876,5.375273,-0.069899],[8.666249,-5.020210,6.249925,-8.700718,5.267210,-8.426448,-3.957494,-7.968389,5.468262,1.606717,4.915030,-5.812487,-8.699430,1.674149,0.724460,-8.712543],[-8.409465,-6.394703,-4.648272,-4.046757,-7.602817,-2.308188,4.817520,-8.653699,0.484527,-5.027877,-9.110710,-5.815386,3.081425,2.267875,5.171405,7.822843],[-7.866040,7.063255,-8.302262,-4.189356,-1.225704,-3.991985,7.501399,-9.651984,-4.100594,3.530294,3.223115,1.235538,6.921158,-9.592324,3.514222,4.144130],[3.264549,-9.197278,-1.431256,-4.723164,4.188570,-9.639988,7.532056,1.849645,8.827304,5.642803,-3.987174,-5.262208,6.491706,-1.823084,-2.988357,-7.448840],[-3.597970,-1.552620,8.784906,3.460331,7.985947,8.412572,0.807277,-5.494495,8.480335,1.199045,9.675347,-1.491089,-3.964181,7.669396,-3.535139,-6.766738],[-3.581018,0.648190,-9.768219,2.475086,1.444989,-6.132376,8.422716,2.109049,-8.253924,7.966520,-7.421448,-3.122801,-1.869152,-2.164542,9.378922,-4.845173]],[[5.545782,0.197285,-6.574241,4.528393,7.038824,-2.209283,-8.484093,-3.087985,9.176333,-5.745301,1.658231,-3.326044,-5.749623,-8.459788,-3.644275,-0.386069],[-3.306141,1.212534,-4.534743,-2.475735,-9.746748,-0.905573,1.843121,-2.580600,-8.644530,-1.910193,8.697222,-4.647404,1.702306,-4.717571,2.675358,0.837452],[-3.677750,-8.029299,6.754551,2.101590,-7.450152,2.933953,-6.820142,-0.381254,-3.941910,-3.327418,1.014776,-3.273968,4.882914,-8.853263,5.949843,-2.728059],[-7.783552,-0.608885,-0.650301,-8.628344,5.098173,-9.004283,6.104703,4.379341,1.146672,3.917781,-5.774884,-6.798024,-4.948252,-7.435424,-1.339066,-6.892835],[3.683359,6.162154,-5.598967,-7.142493,6.221862,5.227906,3.584589,-6.842184,-1.433124,-9.266033,4.585056,-2.180561,8.220534,3.295156,2.233916,1.335445],[-9.570218,-1.047925,-6.373353,1.229001,2.347855,-5.451570,3.908057,-8.668043,-3.027206,-8.203141,2.590308,-1.309400,7.551561,-6.761313,3.574443,0.637522],[-3.289560,-2.622938,0.180087,-0.737060,-0.415479,0.777877,-5.424695,2.296997,-7.640391,-2.794634,-4.321353,8.719349,6.862344,-8.106397,5.726543,-7.665554],[-6.856917,-8.423768,-5.847192,-8.917553,6.010485,-8.048134,8.989480,-9.874633,2.721579,1.151018,9.709950,9.937145,0.387350,6.551545,-0.270975,-6.739993],[-1.346506,-5.749048,-7.810229,2.162137,-5.312244,9.589795,8.411922,-0.132866,-0.693724,-1.910394,-9.227330,-9.843865,-7.955097,-9.484874,-2.752209,9.951394],[8.960531,3.941222,-7.297629,8.263582,1.396248,3.764546,-0.183616,5.509046,7.848246,8.351034,-4.846089,4.619303,8.234912,3.344130,6.931421,1.998859]],[[-2.039652,-8.961024,1.416005,5.521663,-0.491611,-3.293058,-4.031638,4.807203,5.499501,1.948591,8.554172,-9.042067,-2.868835,-2.384435,-8.774449,-4.802046],[-0.917661,-5.628415,-1.675826,-7.764610,-8.279214,-1.339347,8.409605,-1.532631,-1.681575,-5.715939,8.433808,-5.526058,-6.666247,4.192995,-9.779724,9.742000],[-8.972703,6.564217,6.905456,9.471164,-0.244685,9.563267,9.397298,-0.174485,8.039080,9.927763,-6.560257,5.150225,-6.876562,2.785735,-7.377382,-1.118775],[-0.045438,-4.533962,0.398468,5.623163,0.129491,6.024233,5.761009,-7.680965,-8.462580,6.846758,8.472119,5.407249,0.851619,7.532601,0.548193,-3.451813],[5.344050,-9.245034,-1.003566,-9.550215,-5.334804,-9.348032,0.402184,-9.489542,7.685551,-5.883000,-5.213758,-7.839130,9.233009,-7.064356,7.747814,-0.567294],[3.152031,-2.356644,8.718329,3.514671,-3.046436,3.505394,-9.614464,-8.377887,1.697044,-8.938437,-2.557463,6.505374,-1.913198,9.642661,-4.225390,-4.852813],[-5.160645,9.119051,7.345604,2.414340,-2.549636,-2.463805,-5.600536,-1.143730,5.764160,-0.725800,-0.748653,3.225086,3.687891,-8.709851,8.296977,1.009014],[6.550941,5.649828,4.442290,0.197207,4.902425,-3.906398,-6.780916,3.781048,0.799319,0.934468,6.455649,1.672240,9.212065,-0.298386,-9.433266,-0.975433],[-7.837710,5.110304,-3.948889,9.790080,-9.068675,-8.531627,8.032480,-6.461434,0.641846,-1.636396,5.429940,1.527658,4.586669,1.146349,3.690572,-3.087356],[5.750983,2.314962,-5.396224,0.634851,-8.610949,3.271725,8.710109,-6.797415,3.222034,2.905307,-3.219159,-7.133711,-4.078917,-0.751479,2.559732,3.382944]],[[-0.369227,2.734376,1.710487,2.556764,-9.394226,2.728821,-3.730028,-2.877136,-0.262318,-4.545690,-9.125233,2.927688,-6.776838,-5.332857,-3.445547,-1.183147],[-2.504967,2.738426,-9.417801,1.019510,8.570708,-4.134106,-5.077915,3.526116,-9.169130,-3.182023,-5.952420,4.370280,6.064025,1.848461,8.591447,-8.759685],[4.189576,-8.910231,-7.526697,-9.065017,-4.755415,1.057078,3.669657,-0.380996,2.261371,-4.236408,-6.319828,-6.870095,0.140937,0.969153,-0.080527,-0.547479],[7.978779,9.170616,-7.465139,8.927956,4.596020,8.748014,5.613764,-1.893663,-9.835318,3.642692,1.245858,-5.339216,1.451795,3.957867,4.155058,3.889034],[-2.745064,-7.543173,-8.139130,-1.964131,0.317898,-0.136148,0.607236,0.322873,9.693938,-0.763795,-3.559561,6.567298,-4.728591,8.901392,-9.065036,-6.810242],[-8.608469,8.275153,-3.270501,-5.657958,6.064115,-2.180064,5.832578,3.126637,-8.970368,8.757748,-4.968247,-7.445956,-8.606858,3.930653,-8.778960,1.158770],[-3.500960,6.183873,-9.228429,-9.922853,-0.615044,-5.910714,-3.938116,-5.392384,2.087313,-3.951226,-1.838315,-4.488970,-6.166647,5.799706,1.990868,6.945056],[7.005143,-9.575550,-9.701371,-2.703282,-7.136712,8.515228,-9.047006,0.929590,3.206115,5.656549,7.608866,-9.493609,7.088172,-4.783786,6.643476,6.789546],[1.189205,-0.255001,-7.810734,-3.345986,-9.983880,-4.387159,-7.941366,-6.686253,7.037812,2.951192,-5.652998,-7.483098,-3.254399,-3.387891,2.839163,-6.602932],[-9.362087,-1.097607,3.342921,5.773239,-4.792583,-1.116713,7.807866,0.740306,4.514331,4.677100,-0.497794,6.799896,8.698885,-4.638479,3.425877,5.372741]],[[-9.004464,0.990726,-1.110213,2.046023,-6.125927,3.995875,-8.558945,-8.442014,-5.741960,5.359095,6.245890,4.429947,7.950522,3.273131,-5.996814,-6.905278],[3.482216,5.892367,-9.826565,-8.741773,-9.598905,-6.628676,-3.564876,-6.319760,5.089684,-9.978543,4.459424,7.641962,1.128174,8.112446,7.249479,-9.373394],[4.533505,-8.166269,-9.057119,-6.264586,4.883487,-7.320712,7.050543,-5.825138,-5.887864,-0.322355,-2.528809,-3.626856,-9.753132,2.452012,5.758558,-7.344613],[7.984270,-8.395570,-4.601229,5.722064,-4.423129,9.991301,-8.346312,-5.523282,-3.725788,-4.899831,-3.482399,8.900861,7.725884,-7.171319,-9.633850,6.131979],[9.418616,-3.229716,6.631463,2.518626,2.367534,5.816449,-0.595816,-5.233583,-5.620210,0.425064,-0.053454,-7.749496,-4.223295,-3.398446,3.123260,-7.994805],[-4.339333,-2.507539,-3.365900,7.648119,8.750775,-8.491952,-9.339412,-9.659657,2.410871,1.649653,-1.774116,4.714386,-1.595770,-1.277391,-2.013339,-5.012808],[7.889611,-9.737030,5.479913,2.413445,-3.667663,-5.896673,-1.474567,-0.209135,4.685207,6.867029,4.973157,-0.641061,5.880462,4.868077,1.329623,-1.264063],[6.052353,5.382885,-3.771783,3.010894,-8.303302,0.013524,-5.317231,-3.135788,6.616006,-7.933140,5.975772,-4.482724,8.595330,-6.153265,1.891843,0.783979],[9.953180,4.473789,4.066044,-4.500956,9.676887,-9.610067,9.843898,4.582987,5.172083,7.802796,-9.616792,5.293152,-7.487603,-3.844613,-0.136833,-4.443501],[-7.868696,9.900639,-7.117160,7.303661,8.432193,4.838223,8.435664,0.069728,-3.712515,2.445202,-0.425952,-5.881217,-7.259633,-2.733921,-9.629106,-7.389946]],[[5.557055,-1.262032,0.667837,8.943068,-2.302713,-8.844175,4.581485,-3.719091,-2.023525,-7.575959,-4.657007,6.402891,8.624817,4.273333,-6.022325,1.475591],[3.558040,1.092146,8.159165,0.895017,-0.154918,1.414954,1.592295,9.756978,0.861548,-2.921064,3.291873,-1.278624,7.215626,-8.069055,2.480692,9.964474],[-4.804777,-9.500518,4.521215,7.409347,7.697817,3.683372,-7.326076,-8.744090,-9.705592,1.158900,7.997270,8.256466,9.054752,-2.743497,8.552540,9.932697],[0.935196,5.111177,9.625750,-9.584868,-3.835715,2.854854,-4.074006,-3.801801,-1.437337,-0.094635,-3.072467,-2.998015,-9.118668,-0.632245,5.174224,3.725705],[7.083067,6.226301,0.219698,1.966027,-6.192187,-8.321882,6.459264,1.574133,-8.494137,5.167986,7.557020,-2.225515,-6.853803,7.850102,-0.208788,-3.791811],[-6.533102,-4.350642,4.413411,3.789721,-2.186610,0.738687,-5.716957,6.336006,-7.638309,2.884838,-7.690951,0.875137,8.794586,-4.803585,1.278087,7.001132],[8.847469,1.257725,-0.084071,-6.101761,-2.774742,-0.790936,-2.832952,0.436815,-3.607946,7.509158,-9.857124,2.301624,6.405148,2.141080,4.507477,-7.669990],[-6.193088,1.474590,-3.439990,3.416054,9.254755,-4.135608,0.144615,2.297177,-2.862918,8.251059,4.266611,-1.431243,-4.426477,-1.750169,4.750564,-2.108015],[-5.573938,-0.740588,4.109295,-1.284456,3.081984,5.091961,-7.648415,-4.765609,7.375414,-8.774924,-5.788968,5.082514,-8.039392,-0.479895,2.451267,-9.173149],[2.076731,-1.801005,-7.662485,5.582742,6.049224,1.459040,5.544751,6.401390,8.797195,-1.736116,-3.467165,-8.202473,0.663039,-2.397054,-6.313581,-0.137464]],[[0.750971,-5.709307,8.555304,1.132073,-7.782692,9.841788,-6.812359,-4.273275,-2.023502,-4.302920,1.919270,8.202622,2.816662,2.875923,-4.529637,0.832374],[-0.898371,-5.726655,-2.933645,8.928471,-5.481364,-8.991085,6.224866,-3.969403,2.916004,-3.045677,2.404236,7.791261,-9.845832,-4.995130,3.886445,-2.581657],[-5.869229,4.672668,6.194796,0.294063,3.972634,-6.869300,7.244465,-0.788258,1.452635,8.892419,2.238629,-8.650795,8.571489,-4.357913,-7.110144,-2.618984],[6.804576,4.824741,-3.424690,-2.975295,5.195994,-0.464050,4.704585,3.522257,-8.338196,-7.525584,-1.434918,9.324055,0.952516,-3.360306,-7.478746,-2.341078],[-1.438827,-6.066521,7.483137,8.834891,-1.912389,3.786948,-5.355645,-5.807777,3.967838,-2.887005,8.997597,2.018337,-0.618160,7.887642,-7.076135,-8.376895],[7.119780,-3.012681,-2.078344,7.433438,0.788125,-3.421715,-1.528934,-3.275101,6.886287,3.799448,-0.107299,-9.916642,-9.208409,-1.710760,5.609621,2.796993],[1.313541,1.549018,4.588247,-0.854698,4.794283,2.719118,-9.335028,9.300092,-6.619375,-6.855328,2.575550,1.548779,-7.093145,6.992028,3.773655,8.843894],[-0.045636,-9.433925,9.183874,-1.579931,4.460281,-4.307840,-0.028316,-9.943667,-2.801735,1.590637,5.474208,2.885230,-1.602692,8.247597,-8.408601,6.643974],[-9.655348,-9.850407,-2.168007,-0.520393,-3.352985,1.646069,8.850989,-2.880124,4.073767,3.700506,-2.557970,-5.723332,6.598136,-9.976575,-4.382454,-6.820438],[1.242722,8.583274,-7.253864,-6.236362,-3.821001,6.675248,5.600853,-5.810099,5.231560,0.329452,-7.240825,5.174666,3.328618,5.807503,3.384767,-8.417247]],[[6.295682,-0.273080,-1.241914,-3.138753,4.279751,-1.806935,8.789505,0.464248,-6.558268,4.260871,-4.562883,9.633675,-1.862399,-1.675447,-4.613521,1.906533],[-7.835919,4.621319,-6.700534,4.721575,3.555789,-6.994815,-4.573489,-5.788696,-1.976729,-7.225005,-9.131015,-0.991701,-8.166484,-4.678846,-1.565562,-7.939866],[3.474330,7.852090,-8.582749,1.961993,-1.877144,-4.277475,7.334336,0.719438,-6.887589,9.168496,5.929397,-2.678991,-1.184445,6.557842,-6.690794,0.701025],[4.505280,2.653253,1.046130,-1.648241,-8.500962,3.356649,2.756224,0.064997,-3.122993,-0.094608,-3.053182,6.019756,1.668385,1.959576,1.661915,0.210534],[3.636923,-1.428230,-1.564278,-5.997209,8.885968,-1.558475,5.964944,8.148769,-2.842811,9.461166,-2.102385,6.942740,5.324861,5.293796,9.008025,-9.155943],[3.196257,-1.388826,0.011965,-3.859868,-3.079891,0.349760,-9.154021,4.305883,-0.772818,0.849834,3.707007,-5.371080,-1.936901,2.713110,-3.619497,-0.024913],[-6.448257,2.555281,-5.057728,8.977739,8.306454,-0.146638,6.807967,-3.866627,-1.362037,-8.574130,6.697156,3.794704,-1.050639,9.547540,-0.767777,-9.900896],[-5.939119,-1.864151,3.540979,1.707243,-6.320909,-1.321715,0.320957,0.015087,-0.307226,-6.180172,-4.263189,8.543327,-1.248616,7.798504,9.381062,-4.996419],[-3.130696,-0.722943,-3.100126,-7.415299,3.200190,-1.727375,8.597005,-5.484261,3.828782,0.174571,-3.076032,-8.932377,-7.387779,2.688347,1.503773,7.734000],[-2.045566,2.903143,-3.864260,9.321291,-8.169289,-1.518228,8.623874,9.849069,7.113920,-8.886574,-4.580474,5.636250,3.178046,-4.423408,-3.307026,-4.529380]]], dtype = "float64")#candidate|4890|(9, 10, 16)|const|float64
bop_4891 = relay.floor_divide(var_4889.astype('float64'), relay.reshape(const_4890.astype('float64'), relay.shape_of(var_4889))) # shape=(9, 10, 16)
uop_4895 = relay.atanh(const_4890.astype('float32')) # shape=(9, 10, 16)
output = relay.Tuple([bop_4891,uop_4895,])
output2 = relay.Tuple([bop_4891,uop_4895,])
func_4903 = relay.Function([var_4889,], output)
mod['func_4903'] = func_4903
mod = relay.transform.InferType()(mod)
var_4904 = relay.var("var_4904", dtype = "float64", shape = (9, 10, 16))#candidate|4904|(9, 10, 16)|var|float64
output = func_4903(var_4904)
func_4905 = relay.Function([var_4904], output)
mutated_mod['func_4905'] = func_4905
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4571_call = mod.get_global_var('func_4571')
func_4573_call = mutated_mod.get_global_var('func_4573')
call_4909 = relay.TupleGetItem(func_4571_call(), 4)
call_4910 = relay.TupleGetItem(func_4573_call(), 4)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_4919 = relay.TupleGetItem(func_2351_call(), 0)
call_4920 = relay.TupleGetItem(func_2352_call(), 0)
func_3958_call = mod.get_global_var('func_3958')
func_3960_call = mutated_mod.get_global_var('func_3960')
call_4929 = func_3958_call()
call_4930 = func_3958_call()
uop_4932 = relay.log(call_4919.astype('float64')) # shape=(14, 3, 15)
uop_4934 = relay.log(call_4920.astype('float64')) # shape=(14, 3, 15)
uop_4940 = relay.erf(uop_4932.astype('float32')) # shape=(14, 3, 15)
uop_4942 = relay.erf(uop_4934.astype('float32')) # shape=(14, 3, 15)
func_4903_call = mod.get_global_var('func_4903')
func_4905_call = mutated_mod.get_global_var('func_4905')
const_4956 = relay.const([[2.723725,7.077013],[-6.486686,1.780114],[-9.633476,-5.159828],[-0.861841,-9.268435],[-1.434446,-3.057028],[0.531584,5.248550],[0.835541,6.143652],[-7.368378,9.172665],[-5.703208,7.485308],[-3.606480,-4.893736],[8.874528,5.470628],[-5.113660,5.569159],[-0.831194,-0.025898],[-8.128285,8.517295],[4.759264,-2.570075],[-2.949897,2.046560],[-3.333512,0.187297],[0.710512,-6.660757],[8.175656,-5.049611],[2.397305,-1.016232],[4.506893,-5.132842],[-3.045327,3.108554],[-3.058955,8.186123],[7.521599,-6.565548],[-2.391600,3.317289],[5.205268,-7.387667],[9.599837,2.189887],[-8.733175,-1.865874],[-7.836396,3.834849],[-9.614573,-9.007024],[-8.868606,-5.886880],[9.724512,-7.967719],[-2.656484,4.242034],[5.385299,-0.100528],[4.001265,5.606113],[9.334807,6.244601],[-9.786425,7.818718],[-7.957316,-5.001399],[6.877060,-0.317531],[1.965723,-6.203192],[-1.382820,2.977032],[3.610798,5.538370],[7.597416,-1.235557],[-7.049718,5.101469],[7.175955,-2.926507],[-8.147717,-5.026552],[9.268629,-9.754958],[0.483547,-2.770893],[7.129309,1.302277],[-0.519328,3.621583],[-4.470278,-0.300430],[1.039604,0.097141],[-9.562422,-1.460035],[-7.768063,4.937298],[-7.354610,-4.767467],[-5.407584,0.858979],[1.073607,6.241159],[6.659350,4.383140],[-0.982962,4.822620],[6.052364,-2.238509],[-6.307482,4.148648],[-4.632022,-6.531164],[-6.514545,-0.599364],[3.384573,-7.534305],[3.145836,-1.718197],[-8.922604,-5.070119],[-1.525141,7.695094],[-3.808915,0.020832],[-5.483968,-3.113126],[4.604225,7.583049],[7.902244,5.494670],[-2.841060,4.388881],[9.183275,-4.604809],[-6.880778,-3.606789],[-8.012776,-0.982493],[-9.272978,3.925405],[-2.385267,9.327746],[-9.627769,-4.204002],[-3.254535,8.855723],[6.660279,-0.178749],[-5.797481,3.692568],[8.043734,8.494923],[2.034451,3.189734],[-0.707323,-5.450127],[-1.740005,-5.222090],[4.875580,-1.268699],[-2.385065,-9.939090],[0.279185,-2.465066],[8.621678,-0.333448],[-2.154345,1.931379],[5.037954,2.940230],[0.616158,4.607206],[2.374839,5.934170],[-6.484582,-4.404896],[7.464943,-9.686686],[-1.379823,-8.826731],[-4.590874,-2.613810],[3.661925,-2.707758],[-7.380324,-6.839386],[-3.532280,8.740302],[5.766833,-2.387185],[9.371123,2.485584],[5.352958,8.283783],[-0.704059,0.561423],[-0.444505,6.208042],[6.439241,-1.908926],[7.490115,-2.028059],[-9.939649,7.612220],[-5.973473,3.659868],[7.548569,-4.561089],[7.605533,-1.351699],[3.741818,-4.514166],[2.388441,1.184966],[-8.916844,2.869863],[-8.448125,9.072284],[6.513249,5.875820],[-2.325560,2.623958],[2.622103,-7.198846],[7.022945,-9.095015],[-2.254233,-9.194942],[3.085854,6.992253],[-7.418566,2.056436],[-2.805246,8.469271],[-7.551170,6.979955],[-9.429873,-9.824182],[-1.852603,-4.198810],[3.994106,-6.561902],[5.501764,2.499836],[4.292006,-8.944317],[9.861468,-5.528198],[-4.189188,-3.344492],[-5.017876,1.496116],[-9.945223,-2.209544],[-7.144262,5.463462],[-3.882253,-4.897291],[-9.226181,-8.105105],[-4.908785,0.037139],[-8.541147,8.281697],[-0.806392,8.663822],[8.504058,4.223383],[-8.674149,-2.564891],[-2.495173,-6.636048],[0.861012,-3.837478],[0.220656,8.133461],[-1.949187,9.977371],[9.256314,3.463189],[-4.432634,-4.121053],[-4.180373,-8.647113],[-0.030612,7.754301],[-0.143296,5.844059],[-5.911426,1.214873],[-8.628953,1.380136],[-4.398622,2.755182],[5.725264,8.654172],[-2.689117,7.956656],[8.513599,4.698255],[-1.933806,-5.606318],[2.865543,5.270667],[8.366063,8.569374],[8.003111,-5.101696],[9.576820,7.580917],[2.134118,7.795567],[0.627974,-0.742295],[-8.440277,-4.085081],[-8.098510,5.078395],[-8.279257,-9.801383],[5.924550,0.217742],[-6.182289,-1.428889],[7.021491,9.756946],[-0.445539,-7.308526],[2.347360,-0.345692],[1.808312,4.377651],[6.929238,0.417580],[4.153215,-3.111566],[4.295031,5.557121],[5.420672,5.976028],[-9.848082,8.173521],[6.647560,-1.114829],[-5.804001,-4.450829],[9.555599,-8.964179],[-5.649992,-1.316298],[3.999145,3.826989],[-6.381851,-8.483961],[-7.737720,-4.250734],[-0.738090,-4.826501],[-8.846806,5.938010],[7.944884,-4.156727],[6.632493,-3.448159],[-3.913096,6.823123],[1.013996,-9.706050],[4.032208,2.984857],[-8.842173,-7.329012],[-6.278479,2.615983],[3.818492,4.877968],[-4.034117,1.790215],[-0.096731,-7.757258],[-4.423466,-2.856389],[-1.221553,5.658112],[-7.969042,6.468976],[0.812566,2.358730],[-0.095346,-3.303004],[2.725831,3.392404],[3.786727,9.416064],[-2.930918,-4.934670],[1.642655,-1.056723],[3.414501,-2.194739],[-1.597879,-6.632823],[3.268599,9.147378],[-7.600956,-6.326614],[-9.794879,-7.405903],[-9.995831,6.267122],[3.978018,-1.848158],[3.380386,-3.457900],[-2.556190,-7.887395],[-9.607654,-6.321301],[-2.143154,-7.289925],[8.366817,5.234014],[-2.934881,2.407356],[3.024684,8.298267],[-4.337672,-7.833437],[-2.638930,-3.175898],[5.511389,4.140173],[-3.835601,3.225451],[-0.868005,8.239225],[-9.031641,9.169630],[-1.204861,-5.046939],[6.168209,-9.962277],[9.641725,8.958354],[1.394232,-6.919728],[-6.062711,6.276686],[-8.751774,-0.617798],[-6.326773,-1.851006],[-5.864991,1.871295],[5.341410,-8.729852],[1.814124,-3.635026],[1.995695,-2.760313],[-0.865730,7.165246],[-3.369433,8.373913],[-8.543492,6.966627],[8.388220,3.264540],[4.930137,5.694516],[-6.435988,-7.300987],[-7.969512,-9.391525],[-5.878778,1.537263],[-2.049635,-2.142550],[6.008131,6.344681],[1.125724,-2.079366],[-9.955332,-7.741707],[-6.363813,-2.428290],[9.909957,-7.135305],[-1.666025,-0.287242],[4.185637,4.150908],[-3.785842,-3.489025],[2.481716,9.146539],[4.966892,8.979370],[-3.186945,0.822302],[5.194480,6.940257],[-9.354037,1.351130],[8.576984,-5.470273],[0.629422,-5.090244],[8.767304,0.172130],[-2.689930,3.807389],[-9.621897,1.401470],[-0.623079,6.128922],[7.541871,-8.961768],[-7.495707,-5.652498],[8.185929,-6.629064],[-1.350921,6.191873],[7.238371,-9.481754],[9.813926,7.070839],[-4.657888,-0.141094],[-6.918618,3.271552],[4.136270,9.912551],[6.741628,6.517957],[-8.363440,7.769502],[-0.939179,-1.935188],[3.196832,5.296826],[-7.836922,-1.530839],[7.457402,5.843927],[-2.599901,0.577208],[5.300391,1.845000],[-5.570168,1.066251],[-0.797905,1.673478],[1.347140,-5.514650],[-9.141207,-6.048520],[1.034657,-6.398801],[2.218470,-4.672916],[-9.848009,4.392705],[-6.202323,-1.073441],[9.941432,-9.355484],[-3.060906,-6.999732],[0.120847,-9.504532],[-6.918041,5.203971],[5.380389,5.450305],[7.441479,-8.770166],[2.559968,5.194738],[-4.427603,1.496884],[-6.168873,6.907407],[7.568714,-0.958271],[-8.503323,8.548265],[0.760655,-6.591732],[-6.942352,-2.622790],[5.773341,9.178223],[-9.001402,4.262368],[-1.396719,9.290342],[-2.049572,1.939950],[-4.478946,-9.959537],[-9.422260,-0.384961],[-7.487555,-2.466360],[-3.717445,5.482890],[8.816131,-0.227482],[6.544233,-5.074465],[-0.145686,-5.503481],[-9.527339,4.962914],[-3.357232,0.260926],[8.485807,-4.689982],[8.141508,-0.001612],[2.514158,8.730214],[-7.079674,4.225124],[1.692882,7.266403],[4.510609,-6.272429],[7.749637,-2.377323],[-4.357873,-7.358576],[9.219394,6.138979],[6.448015,-0.500781],[9.251450,2.364834],[-7.983656,-7.161481],[-8.394884,1.835785],[5.538239,8.247238],[2.800631,-7.848337],[5.425190,0.494195],[-9.380126,9.203815],[-2.352743,-1.226926],[-2.675231,1.400786],[-5.146142,-4.753293],[7.420762,-1.053643],[-8.870325,3.659381],[-9.384672,7.410810],[-9.863184,-2.483419],[1.764345,-5.785681],[-9.715707,-3.582259],[-3.529497,7.912214],[6.748432,8.664708],[3.189950,4.595329],[0.539159,-5.601417],[3.914882,-0.398117],[-8.573563,-0.336875],[-0.286886,-1.427859],[5.526114,6.412051],[-4.705090,9.626013],[1.282587,6.375127],[-7.005428,-1.962645],[9.096235,8.328508],[-5.185281,0.523937],[0.147260,-0.595539],[-2.284021,-3.976943],[1.646890,-5.920741],[-8.418334,0.432012],[-9.172219,-9.750537],[-0.617808,8.839688],[9.492266,-8.527033],[-2.355118,2.625233],[5.828822,5.197704],[-9.967494,7.560449],[-5.891222,3.504311],[6.333131,-1.439367],[7.201723,4.285056],[0.953767,-0.205082],[8.057964,-8.666914],[-9.421083,3.853304],[9.000066,7.483794],[-0.835940,-7.405852],[-1.981915,2.063063],[-0.588720,-3.477858],[9.726886,3.032119],[-3.819455,7.368652],[-0.481661,5.492869],[8.027901,-3.884682],[7.602110,-5.578764],[0.496128,-4.616189],[3.724554,8.645539],[3.136983,4.434912],[6.355160,9.311684],[-8.267944,-4.892138],[-4.444295,3.085965],[-2.417538,6.550510],[-2.293611,-1.468131],[-2.320344,4.679304],[-2.814605,1.695273],[-8.688265,-7.546917],[-4.370897,5.542591],[5.666584,3.396049],[2.280504,3.009072],[9.929532,-7.076631],[3.985547,0.058890],[3.353566,7.184927],[1.345919,-5.269983],[6.893189,-5.909386],[-8.361096,6.331932],[8.752237,-1.730234],[7.631101,-2.437235],[-5.740073,-6.713220],[6.554588,8.016222],[3.837362,1.154505],[1.065697,-6.321074],[-2.259734,-9.824843],[8.715299,-1.191153],[0.077924,9.978607],[5.037467,7.127845],[-4.686971,7.474450],[9.168249,2.295308],[5.195910,4.621880],[-6.256032,8.936800],[-5.241735,5.707312],[9.541167,-1.345378],[-7.541175,-1.420717],[-1.946314,1.470279],[7.450824,-3.542708],[0.692360,2.203352],[-9.449504,-5.503817],[5.651034,-7.066895],[0.394622,1.241156],[3.315727,9.371110],[2.517531,0.017890],[4.727511,7.631491],[7.427994,7.563704],[8.753126,0.003797],[-4.120623,-5.293223],[-7.601667,1.309773],[-6.223585,-5.130889],[9.061580,-4.802934],[7.574010,-4.566207],[-9.092767,-7.414193],[2.729784,9.604092],[-9.015753,4.114020],[-9.208177,-9.166118],[-9.119693,-6.208365],[-1.152254,-2.491949],[6.871953,7.228719],[4.745257,0.106676],[8.193978,6.098327],[-4.945956,3.354434],[-2.654811,0.755029],[-0.061773,5.993450],[7.987664,0.255501],[-8.957653,2.562091],[-7.630647,8.710225],[-4.955693,-0.745020],[-0.996538,0.676723],[-1.778233,1.888628],[7.011823,3.254799],[5.937604,-2.517750],[-4.275689,-5.219222],[0.476576,-0.690663],[-0.761933,8.762206],[2.196216,-0.224993],[-2.454450,-6.117375],[-0.250805,1.448358],[-6.205374,7.257282],[1.425175,-3.853340],[-2.296020,-0.856406],[1.627347,1.366534],[-9.391318,-5.109759],[-4.838165,1.078019],[-6.595528,8.761889],[-4.580634,-4.914305],[2.694997,-5.945755],[1.475072,8.138473],[8.520070,-3.922261],[-4.428787,8.416966],[-3.698929,-9.406823],[-5.161895,8.217385],[6.939897,-7.286176],[7.667573,-3.978255],[-9.069971,6.660600],[-1.180464,9.847496],[8.397714,-0.282375],[-6.773796,-9.492746],[2.319742,6.288609],[3.022445,5.251145],[-6.806981,-0.096766],[-5.270888,-1.679601],[5.109621,7.366405],[-7.134828,7.667528],[-7.766039,-1.049601],[9.243855,5.672787],[3.935619,7.955455],[-1.421312,-0.068038],[-9.361635,-5.602072],[3.371711,6.291889],[6.177190,-6.455309],[-9.432246,6.925238],[0.512489,0.549345],[-3.868769,-2.734937],[8.851963,-4.585411],[-3.831331,-1.419416],[9.060687,9.838648],[-5.854513,4.955826],[8.001319,1.929887],[-3.262188,-8.332723],[-1.906194,-6.001338],[4.790973,2.044467],[-1.797663,-7.900265],[-7.856730,3.052473],[9.412205,-1.180206],[-1.411116,7.287883],[-6.079686,6.585625],[4.929161,-7.947329],[6.508064,2.361542],[0.653995,7.286683],[-6.277618,-5.468716],[8.273854,8.459483],[3.355799,-0.500622],[1.295205,4.983755],[-4.146481,-7.178245],[4.106993,-8.065067],[-6.768388,1.324586],[-5.886340,7.674336],[-0.883084,3.317769],[-7.476391,-2.506059],[-7.059809,4.685438],[7.107746,7.614161],[3.360472,4.662510],[0.539372,0.449295],[3.870110,4.565254],[8.973990,9.163766],[0.516306,0.062532],[7.061356,3.594198],[-2.368419,8.522236],[6.047869,-7.660777],[0.247877,3.862345],[6.675192,-7.850563],[9.135710,-7.551813],[-2.513804,-7.995048],[-6.132266,0.313753],[-6.575165,8.721127],[6.580850,-6.682306],[-7.522510,7.608149],[-8.740125,-6.279834],[8.850278,4.813471],[-6.472557,-9.528557],[8.115126,-7.856537],[-3.596314,0.246059],[-1.669907,-9.371239],[5.831280,7.106186],[7.125896,8.046021],[1.933799,8.540209],[-2.718440,-3.195669],[-3.820355,-7.443539],[0.995574,6.634358],[-0.489725,-4.785717],[4.900927,2.275978],[7.702470,-5.775006],[0.786149,7.626915],[2.265093,-2.838289],[8.730104,3.133487],[9.579437,1.159976],[-1.255603,-0.226747],[2.779276,-8.077797],[2.990098,0.430525],[-2.840709,9.959597],[-9.738045,-1.586469],[3.926591,7.071617],[9.386680,-4.581113],[-2.581361,-5.867630],[-4.753427,-3.765947],[8.132200,2.472384],[-2.948372,-9.954569],[-5.893864,-5.328761],[-6.173680,9.861602],[3.469160,-0.459972],[5.093834,6.077049],[-8.232577,-2.866228],[0.451592,-8.045837],[9.791582,6.768316],[-8.649712,-1.561762],[-4.200397,1.844197],[-7.263462,-7.487798],[-9.809034,-3.847742],[-0.005811,8.739651],[7.857129,2.639173],[-0.655431,-6.770444],[4.299719,2.466708],[1.821825,9.512206],[3.656419,-5.087189],[5.707577,1.379561],[4.906277,5.512129],[-3.643350,-1.680618],[-3.501898,-5.762335],[3.274219,3.064461],[-8.443066,-2.952871],[-8.685458,0.598134],[8.970413,2.483985],[6.071072,-9.390666],[0.352380,-6.648260],[-4.919922,3.637952],[-7.624474,-1.777376],[-4.825413,1.679086],[-6.225659,-6.570668],[9.679045,-6.617569],[7.617952,2.265956],[7.134970,1.889484],[8.453732,-1.191258],[-6.197140,-2.581492],[0.917127,-8.138154],[-0.693584,-6.731606],[-9.574736,-8.706994],[7.339798,-3.884383],[-9.174842,7.883399],[7.417308,-7.326038],[-9.021103,-2.713797],[8.623702,7.511739],[3.801100,-4.172290],[4.270989,0.035829],[-3.501144,9.051384],[-5.827434,-8.711190],[0.574927,-7.083293],[7.522091,1.905428],[1.630253,-5.725416],[8.356227,6.672184],[-5.372083,-5.018069],[2.295082,5.272964],[0.686049,0.391030],[-1.698948,5.257244],[2.367643,-8.708713],[-6.779051,-8.521006],[8.430239,-7.926058],[-3.879556,-5.824906],[-5.719489,9.691863],[-8.449712,2.988283],[0.693215,0.753385],[-9.464592,-6.606075],[4.206413,-7.156363],[-9.067371,1.708430],[-3.095842,-0.350872],[-6.231911,6.637752],[-0.736747,-5.541338],[8.888235,-8.778935],[-3.670633,-1.330594],[-1.233931,-2.823104],[7.350592,-7.428403],[6.542539,7.342866],[4.826036,-0.671963],[-1.590020,-1.343059],[-6.336507,0.384704],[-8.503577,6.416335],[-3.992995,-5.924017],[-5.453673,-3.549347],[1.900513,7.085176],[-0.251281,-7.413150],[3.560502,1.101569],[-0.938484,-7.897975],[-4.445098,-7.868373],[1.472476,5.269910],[3.882012,2.781124],[-5.146173,0.525423],[-3.244847,-4.321105],[-2.948654,-6.590223],[-8.741135,8.544564],[-1.831115,5.772145],[-9.717709,3.656419],[7.802468,4.167963],[-7.993694,-4.629506],[-0.446674,3.833596],[2.183541,8.912349],[-1.505654,1.938230],[-0.951587,-5.604597],[-8.314752,2.453911],[9.146924,-7.142224],[-0.007275,-0.291452],[-9.132492,2.993303],[-2.513619,2.215860],[6.308788,1.897936],[4.399170,-1.663923],[-2.267406,-6.076382],[-5.924657,4.901986],[-1.430066,9.766200],[8.394398,-2.748132],[-0.221069,-6.897542],[-0.953418,-0.237048],[-1.533601,3.346936],[-3.318249,1.414581],[-9.190598,3.030209],[-7.255935,4.942797],[3.666181,8.810123],[-0.657053,-3.327250],[1.404330,3.765662],[4.167459,5.589037],[-8.583448,4.398450],[-3.116434,6.915896],[-4.933244,-9.402932],[3.168735,6.176494],[-3.531251,8.344803],[-1.658834,2.145798],[-7.299504,8.119480],[1.680361,6.949682],[-7.312852,-6.208234],[-7.304634,6.009093],[3.097512,4.128122],[7.410227,9.040134],[2.778057,-9.009147],[-7.281189,7.796103],[8.768336,-2.421160],[-7.407852,-8.525449],[-7.576091,2.571175],[-6.309635,6.069625],[-6.966794,-0.832825],[-5.214045,4.376315],[-8.401405,4.858103],[-7.871205,8.845920],[-3.817028,-6.781749],[8.486814,8.919170],[4.560087,-1.184736],[4.849228,6.403476],[-5.176491,-1.142931],[4.097321,-7.035507],[3.465327,9.997283],[3.189772,3.226213],[-6.596606,-3.537767],[-1.834590,-1.835589]], dtype = "float64")#candidate|4956|(720, 2)|const|float64
call_4955 = relay.TupleGetItem(func_4903_call(relay.reshape(const_4956.astype('float64'), [9, 10, 16])), 1)
call_4957 = relay.TupleGetItem(func_4905_call(relay.reshape(const_4956.astype('float64'), [9, 10, 16])), 1)
output = relay.Tuple([call_4909,call_4929,uop_4940,call_4955,const_4956,])
output2 = relay.Tuple([call_4910,call_4930,uop_4942,call_4957,const_4956,])
func_4959 = relay.Function([], output)
mod['func_4959'] = func_4959
mod = relay.transform.InferType()(mod)
mutated_mod['func_4959'] = func_4959
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4959_call = mutated_mod.get_global_var('func_4959')
call_4960 = func_4959_call()
output = call_4960
func_4961 = relay.Function([], output)
mutated_mod['func_4961'] = func_4961
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5005 = relay.var("var_5005", dtype = "float64", shape = (6, 15, 15))#candidate|5005|(6, 15, 15)|var|float64
var_5006 = relay.var("var_5006", dtype = "float64", shape = (6, 15, 15))#candidate|5006|(6, 15, 15)|var|float64
bop_5007 = relay.floor_mod(var_5005.astype('float64'), relay.reshape(var_5006.astype('float64'), relay.shape_of(var_5005))) # shape=(6, 15, 15)
func_1846_call = mod.get_global_var('func_1846')
func_1849_call = mutated_mod.get_global_var('func_1849')
const_5021 = relay.const([5.778548,5.757956,7.793128,4.996416,7.857268,-7.457866,-0.151346,-4.263225,0.016815,3.056323,-6.813401,3.543818,6.123167,2.260650,1.391588,-9.114596,6.578580,-2.308811,1.526155,-6.671732,7.417010,3.261512,-1.485904,2.985405,0.107363,3.502635,1.493054,-2.807681,-3.307917,4.386691,-3.527253,-7.237200,-8.859239,-2.299701,1.438741,-3.256333,-4.131068,-6.971772,0.365791,-9.739257,-2.445075,-3.107912,4.780798,-9.576779,-1.368449,5.726880,-5.564747,-1.777434,-8.799449,-8.810474,-5.111284,1.049455,8.397963,9.565789,0.880806,1.255227,4.640664,-1.439905,-2.078280,2.018023,-8.806969,-4.142016,-8.788427,9.576592,5.235314,-4.085665,-0.677181,-6.839709,-6.499333,8.810432,-3.630846,0.921110,-6.870998,-8.391334,3.819571,-6.811927,-7.645615,-1.530147,3.613969,2.540185,8.521096,-5.911973,3.007993,9.678020,4.550789,-0.560823,4.911129,7.747010,9.646657,5.954049,4.020806,-6.307828,-9.732847,1.474782,3.809526,-0.776465,-7.967881,-2.650681,-4.749038,6.353008,-1.474904,9.223610,-9.531573,-8.645210,-8.364567,-7.474814,4.466717,6.908601,1.195483,9.084424,7.633634,3.908195,7.718372,-9.599559,-1.869657,1.862279,0.958123,-8.467585,9.276888,8.751288,-1.974271,-1.422708,-6.310423,2.907401,-8.968681,-6.737454,4.865046,5.171841,-9.107091,-5.411691,-6.226277,2.484850,-9.278566,4.049718,-9.954689,9.979363,-7.907326,-2.405972,4.021537,-9.716405,4.987498,6.312552,-2.395182,4.462632,-7.492518,7.768610,1.722852,-6.032976,2.951593,1.224687,-1.283701,-2.492713,-6.880319,-5.716961,8.160338,2.882631,9.054984,6.827697,-8.458413,-6.915321,-4.199038,9.798725,3.756734,3.164775,5.500511,-4.938983,8.038100,-3.684141,-3.318378,8.455065,6.299408,-4.581336,4.307001,-2.271746,-9.367542,1.314498,2.198161,-1.878638,-9.127106,4.822579,-9.945266,-2.645150,-2.252954,-9.331561,9.059240,-8.280015,-2.736735,6.341915,-1.649572,7.056115,0.855214,4.741939,9.103324,1.307679,8.116809,8.794383,-1.303237,7.430543,-1.986366,0.618618,3.736441,-8.951267,-9.814450,-4.419257,-1.261449,2.454393,-6.240372,-8.031273,-1.128660,4.623747,-6.157421,-7.181157,-7.471978,8.481112,6.153076,-8.553333,9.420864,-6.089821,4.204745,-2.711970,4.998431,2.644076,8.567861,3.163227,9.598285,2.333749,-7.777470,-8.778960,-8.408327,1.364717,3.013861,-9.835471,2.499600,-8.050604,5.024294,-2.520154,4.519836,-4.424878,2.683805,-1.719835,7.648429,-6.850481,8.818294,-3.031355,-9.165043,6.002745,-8.575595,-6.634766,6.993451,-9.769587,-0.095282,2.829105,-0.118498,-6.381713,3.600755,-0.112609,-2.866313,-3.837783,4.799386,3.627183,4.452430,9.090300,3.231167,5.629437,5.082920,7.679267,-9.936601,2.320175,0.519553,-4.200986,-3.157562,0.357858,8.277702,0.712462,-4.027997,-5.672944,2.878534,2.074290,-2.111647,8.282793,-3.692260,9.690235,5.789577,6.198176,-3.280360,-4.473131,-4.973714,5.686744,9.752408,3.977360,-6.754532,3.817307,7.674993,-5.620273,9.970667,1.786147,-8.350327,-0.906954,2.460108,-2.822630,2.297020,1.417350,-9.817980,0.589628,9.274850,-2.802406,4.687451,0.268218,-2.577821,-2.875632,-4.672817,-5.404022,-9.682343,-3.776651,-3.628952,4.279770,2.741548,-6.620044,2.359888,-3.503070,-1.967845,-1.939621,-6.681002,-0.328527,9.102072,9.173001,7.612795,8.412092,-5.502043,5.333147,-0.367625,6.054964,9.732123,-1.506929,0.282052,4.800715,9.221743,8.764002,-2.359163,-6.193964,-1.054906,1.766532,4.195439,6.312049,-7.029117,8.306877,9.807130,8.299060,-8.202415,-9.342669,-5.592260,5.251629,7.002466,1.542351,-8.684120,-5.465913,2.854283,-3.252673,-4.679400,1.062384,0.080650,9.646873,4.187025,6.798133,-6.752050,6.028678,-8.758959,-9.016112,-8.841999,2.286582,-7.727140,5.456595,9.695512,-2.018540,-7.675940,-1.449258,-1.055837,-7.513563,-0.731018,0.228041,5.904784,3.455017,6.632663,-5.297185,-3.587581,6.546270,9.220496,-1.448037,-5.501772,-8.505257,-7.963629,-3.328348,-0.242184,-7.794324,8.023592,-9.101556], dtype = "float64")#candidate|5021|(396,)|const|float64
call_5020 = relay.TupleGetItem(func_1846_call(relay.reshape(const_5021.astype('float64'), [396,])), 0)
call_5022 = relay.TupleGetItem(func_1849_call(relay.reshape(const_5021.astype('float64'), [396,])), 0)
bop_5027 = relay.divide(var_5005.astype('float64'), relay.reshape(var_5006.astype('float64'), relay.shape_of(var_5005))) # shape=(6, 15, 15)
func_2405_call = mod.get_global_var('func_2405')
func_2408_call = mutated_mod.get_global_var('func_2408')
const_5049 = relay.const([-9.368679,1.964017,1.437526,6.916051,-4.400323,3.760449,-5.674020,-5.012954,-4.068877,0.436890,9.737360,7.673789,-7.559357,-0.084003,3.233977,-0.138004,-8.293192,3.375198,3.307136,-6.525171,-3.629550,8.087271,-6.139699,-6.575351,-5.616652,2.825895,-9.353311,-5.263555,5.029982,-5.589494,8.999037,-9.197194,-9.641790,0.181613,-6.083368,5.391405,-3.503476,6.173108,0.218707,9.122058,2.335508,9.061087,6.255323,-2.688002,7.019987,-2.457928,-3.797537,-9.868273,-1.191295,-5.447991,2.629553,9.778508,-6.204608,2.169674,-1.732099,7.182307,3.522120,9.784081,-0.826519,1.591835,-2.620925,-7.804050,4.763230,-3.022800,9.553656,-1.530178,-8.786102,-9.010255,7.288716,-0.359903,-4.922908,9.525661,6.183120,-5.776410,9.804621,9.247831,2.881562,-8.360762,-7.602791,1.797375,3.525347,-5.054557,5.565206,-9.826191,-4.178314,8.646885,-1.248414,-1.882424,3.415110,4.283420,1.845772,3.547434,4.878096,7.658667,-5.569268,5.240109,-0.565438,0.015252,-5.843611,-0.573027,0.997682,7.210437,1.405875,4.714041,-8.740144,3.443328,2.620005,4.858696,-5.309730,-5.842087,5.099398,-7.782327,3.409758,6.100151,0.114939,2.594905,3.492395,-6.561787,-7.909721,-8.482666,-1.146801,-5.517816,-2.166760,-7.628443,-9.473869,5.888993,-2.750323,-8.520091,6.067087,7.925835,1.973863,6.969885,2.410075,2.104303,4.774671,4.244516,7.735497,1.092892,6.745589,-6.458949,-6.985483,1.364800,7.755496,5.450429,7.740794,4.787056,6.122668,-8.875293,-2.671964,-9.938771,9.390085,-2.869225,-4.679621,-1.322302,3.942637,9.793564,-8.403156,3.423963,-0.028998,-8.720056,4.637340,3.567822,7.128383,-3.244433,2.778295,8.045140,-4.758190,-8.836282,-8.049547,-0.475217,3.318240,7.253426,-2.426400,-2.568454,3.199429,-1.153367,-6.105738,8.093028,8.188890,-3.830685,3.387641,5.839775,9.628235,-3.162502,-0.197485,3.839058,-8.796524,8.644029,8.503242,-0.885466,0.124674,-4.562204,-3.685808,7.429298,9.282376,-8.448791,8.182905,-2.729448,7.817774,-3.687043,6.948079,-2.090098,0.421021,-1.819470,6.273982,5.778076,8.861104,-1.959682,-2.128853,-5.471730,8.310968,-2.299345,-8.385976,9.649614,9.148113,-5.048110,-3.364300,-1.695403,-6.913131,-4.729405,5.358941,-5.198417,8.081266,-4.288374,-0.636878,8.008219,-9.435784,7.300836,-7.104552,-1.059355,-6.474252,-7.306882,2.540855,-1.454223,9.869152,9.434727,4.002980,-8.525652,0.167891,-3.191412,2.480246,3.746277,0.961512,-0.088679,-8.277445,9.692082,5.314979,5.714577,-1.832499,1.867522,-7.243046,3.595041,-3.800004,9.843604,-6.943333,-3.189180,2.988441,8.663629,-5.942372,9.582534,7.945422,6.849152,-9.122042,5.168301,6.317034,8.386620,-1.121078,1.408070,-2.334125,-8.784634,-6.396343,-8.906125,-6.620958,-9.221649,5.584190,0.445410,-5.193144,-8.684984,9.431637,6.641314], dtype = "float32")#candidate|5049|(280,)|const|float32
call_5048 = relay.TupleGetItem(func_2405_call(relay.reshape(const_5049.astype('float32'), [280,])), 2)
call_5050 = relay.TupleGetItem(func_2408_call(relay.reshape(const_5049.astype('float32'), [280,])), 2)
output = relay.Tuple([bop_5007,call_5020,const_5021,bop_5027,call_5048,const_5049,])
output2 = relay.Tuple([bop_5007,call_5022,const_5021,bop_5027,call_5050,const_5049,])
func_5078 = relay.Function([var_5005,var_5006,], output)
mod['func_5078'] = func_5078
mod = relay.transform.InferType()(mod)
var_5079 = relay.var("var_5079", dtype = "float64", shape = (6, 15, 15))#candidate|5079|(6, 15, 15)|var|float64
var_5080 = relay.var("var_5080", dtype = "float64", shape = (6, 15, 15))#candidate|5080|(6, 15, 15)|var|float64
output = func_5078(var_5079,var_5080,)
func_5081 = relay.Function([var_5079,var_5080,], output)
mutated_mod['func_5081'] = func_5081
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5090 = relay.var("var_5090", dtype = "uint32", shape = ())#candidate|5090|()|var|uint32
var_5091 = relay.var("var_5091", dtype = "uint32", shape = (15, 4, 1))#candidate|5091|(15, 4, 1)|var|uint32
bop_5092 = relay.subtract(var_5090.astype('uint32'), var_5091.astype('uint32')) # shape=(15, 4, 1)
output = relay.Tuple([bop_5092,])
output2 = relay.Tuple([bop_5092,])
func_5125 = relay.Function([var_5090,var_5091,], output)
mod['func_5125'] = func_5125
mod = relay.transform.InferType()(mod)
var_5126 = relay.var("var_5126", dtype = "uint32", shape = ())#candidate|5126|()|var|uint32
var_5127 = relay.var("var_5127", dtype = "uint32", shape = (15, 4, 1))#candidate|5127|(15, 4, 1)|var|uint32
output = func_5125(var_5126,var_5127,)
func_5128 = relay.Function([var_5126,var_5127,], output)
mutated_mod['func_5128'] = func_5128
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_5153 = relay.TupleGetItem(func_1084_call(), 0)
call_5154 = relay.TupleGetItem(func_1086_call(), 0)
output = relay.Tuple([call_5153,])
output2 = relay.Tuple([call_5154,])
func_5158 = relay.Function([], output)
mod['func_5158'] = func_5158
mod = relay.transform.InferType()(mod)
output = func_5158()
func_5159 = relay.Function([], output)
mutated_mod['func_5159'] = func_5159
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4684_call = mod.get_global_var('func_4684')
func_4686_call = mutated_mod.get_global_var('func_4686')
call_5269 = relay.TupleGetItem(func_4684_call(), 0)
call_5270 = relay.TupleGetItem(func_4686_call(), 0)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_5276 = relay.TupleGetItem(func_2993_call(), 0)
call_5277 = relay.TupleGetItem(func_2995_call(), 0)
func_5078_call = mod.get_global_var('func_5078')
func_5081_call = mutated_mod.get_global_var('func_5081')
var_5279 = relay.var("var_5279", dtype = "float64", shape = (1, 1350))#candidate|5279|(1, 1350)|var|float64
call_5278 = relay.TupleGetItem(func_5078_call(relay.reshape(var_5279.astype('float64'), [6, 15, 15]), relay.reshape(var_5279.astype('float64'), [6, 15, 15]), ), 4)
call_5280 = relay.TupleGetItem(func_5081_call(relay.reshape(var_5279.astype('float64'), [6, 15, 15]), relay.reshape(var_5279.astype('float64'), [6, 15, 15]), ), 4)
const_5288 = relay.const([[-6.149476,-8.953819,-4.872602,2.006049,9.579126,-6.939503,7.892221,-3.437002,6.938275,7.152659,-1.355249,-3.072946,-9.197935,9.989931,6.809745,1.959168,-4.189245,-9.813759,2.439664,-2.507562,-8.204755,-9.156825,-6.107296,1.019864,-4.038716,3.376002,4.467325,1.710353,-6.372587,7.892780,0.756681,9.829501,-3.784392,-7.658504,4.166317,4.251048,0.882298,-8.108952,-0.261311,-5.139674,-3.157189,5.130219,2.934929,9.781814,2.315856,2.497191,-4.273199,-0.798593,-3.413274,-8.933542,-9.566621,-2.972988,-4.805528,0.434518,-0.766878,8.656011,1.643579,-2.320318,1.693947,-3.974707,9.673970,3.281886,5.471059,-9.095629,-1.755454,6.327190,-2.698167,2.875950,-8.185106,-5.184926,-1.489485,-0.802582,-9.584906,-6.107981,-3.068706,9.348886,-3.135717,1.464845,-4.497621,-3.492739,9.554827,1.548952,2.193176,-4.746889,0.370580,-8.074383,-6.768301,1.952076,-9.181468,2.412786,1.512903,-2.621989,3.057776,8.008842,5.324695,6.696000,0.897080,6.235841,5.694261,9.584337,-5.288716,-3.575671,-9.651351,8.660979,2.325204,5.786016,1.868877,-0.401828,-7.934684,2.603930,2.355601,-8.473086,8.643487,1.821511,6.476249,-0.976349,0.661141,-0.521298,-2.749407,-8.280546,-5.827159,-2.562491,5.523743,6.986864,-8.905687,5.180921,8.167557,2.003670,8.203428,1.168964,2.874974,-6.457319,-9.342319,-9.424572,0.167953,-6.978063,-0.314467,4.854729,5.982353,3.944341,4.118190,-8.103609,-1.950770,-6.831896,-1.756706,-5.822651,1.661410,-8.976365,-0.574202,-1.284424,4.272840,5.528708,-5.260058,7.898940,2.288444,3.227962,-8.761579,8.796030,4.647976,-6.622062,6.032220,9.756528,-1.802597,-9.544406,-2.839682,-8.221202,5.009809,-8.855633,-9.867478,-2.856818,-7.426728,1.296679,4.067550,-8.139053,-8.806237,-0.034093,4.380441,-4.290297,-9.573181,-6.541359,6.488044,-5.483927,7.854607,-5.757470,3.643079,5.974653,2.984875,-0.193643,-5.895634,2.831313,0.611753,-7.689409,-0.540701,-2.542508,-1.994696,8.357591,0.834001,-3.402755,-7.257541,8.996595,3.164870,-9.575021,2.607028,7.946683,6.165979,-7.608883,0.210392,2.319826,3.994719,-2.621679,2.600080,2.828457,8.557305,1.801323,0.993369,8.649374,4.799749,5.881237,-4.304469,-2.116409,6.710706,2.614871,-6.750729,-7.986789,-4.380945,5.645328,9.844748,0.672038,-4.179265,-1.217900,2.652199,6.897965,5.301955,8.882504,1.111245,1.883063,-0.398466,2.515064,-3.650246,-3.216692,-7.533556,-7.327566,-9.222883,4.831555,-7.348590,-7.958607,6.542055,-8.381662,-7.732024,8.792618,-7.515988,9.672766,2.179348,0.776849,-0.676694,-4.134100,2.183693,-2.446500,-6.916787,-0.573144,-8.016783,-4.055237,-8.733827,-2.549280,-3.499592,6.245282,3.188886,6.439287,1.965775,-2.350350,-3.289060,9.352448,4.764401,-3.822788,2.353611,-2.028146,3.538116,9.315783,4.004255,0.528498,1.083788,-9.556060,3.481722,8.578092,-5.515773,-2.334357,0.462344,-6.926559,-5.524284,-0.231438,-1.429082,5.616105,-4.601980,0.339944,-0.481783,4.749914,1.649076,-4.361993,-6.529009,-5.441603,3.605053,2.364433,-9.372420,9.766729,-9.352475,-0.294159,-4.540664,8.767110,-7.404852,4.391391,6.679335,3.815728,-8.408223,9.794163,7.039844,-5.804852,-7.065827,3.621242,6.169898,5.276440,2.388658,-5.086237,0.724541,-6.843667,2.570153,5.853492,-7.177381,5.787731,-4.192557,4.738317,-1.182697,6.645608,-4.528653,0.786393,8.424648,9.818031,-5.201538,1.004246,5.272249,-0.649403,7.394306,5.000190,-8.539827,-4.617260,5.590295,-3.505378,4.525350,4.081877,0.052954,-3.706624,2.245565,4.513413,1.336566,-3.504713,-2.886093,4.366835,-5.545666,7.243531,-7.636738,6.119123,-3.160507,3.721303,4.344888,6.791217,-2.843551,-3.329431,4.357623,0.496923,-9.106200,-6.177889,-4.129153,-8.649999,-0.358191,3.914592,9.415661,6.129844,4.414376,-2.925797,6.439918,8.786594,9.150343,3.044674,0.518158,3.574936,-5.777394,-5.303821,-5.335045,2.173902,-3.257651,1.943573,-5.479994,2.476280,6.438503,-5.185895,4.975097,-8.018997,8.003732,-4.116285,2.835799,-5.301228,3.059199,-7.721292,8.560465,-2.684873,7.438865,-4.114560,-8.189926,5.513521,9.429866,-7.893555,1.057113,9.787356,3.439166,4.422392,3.254121,-6.356993,-6.138471,-1.289800,0.193122,6.649188,-4.117641,-7.361803,-7.930216,3.488447,1.638741,-5.606460,-7.489724,-3.640204,6.561535,-1.371242,9.532739,2.883453,-7.358153,-5.304558,9.816730,-0.458994,4.140994,-6.988601,-4.506293,5.964941,-3.324817,-1.686337,6.988704,-8.692748,-8.960530,0.482747,6.839733,4.873160,7.228696,9.051175,6.094917,-8.644705,-0.229273,-9.335939,-0.220687,5.972305,-2.504397,-8.793828,-8.857583,-5.959716,5.292028,-2.862889,5.078427,-1.484972,3.202893,7.361685,1.941254,5.812196,-6.253565,-5.688582,5.807509,5.859358,5.211129,2.635682,-9.938520,-8.504170,-6.725070,1.732251,-8.881808,-0.536871,9.604247,1.457327,8.075108,6.056365,-2.898448,7.875275,1.805628,8.467670,-6.841811,-5.468017,2.654027,-6.274507,0.865870,3.086831,-3.994334,-0.098332,3.720563,-8.767106,-6.159197,-9.056018,-8.010365,4.314887,5.308796,-0.527296,5.759030,-8.161182,-5.901357,-9.129369,-0.003373,0.436441,9.619501,6.864847,0.760598,-5.875936,5.066230,9.243636,-8.008062,5.177412,8.725826,2.268478,-7.763995,6.703773,-4.936042,-0.895756,2.227834,5.780887,5.487110,9.429014,3.549371,7.632198,4.419644,-9.147275,4.521514,0.833275,8.082116,4.041028,-4.778267,-8.726202,9.349069,-5.674459,1.733946,6.922979,-7.418883,4.492692,-6.510590,-4.666578,6.070263,1.378182,-6.197748,-4.360320,7.742570,1.322365,-9.065836,1.971975,-3.264879,7.759740,2.700984,7.374092,5.408212,2.449473,8.240154,0.155011,-4.523429,6.811516,9.170398,8.065134,6.258940,3.628750,-8.145726,0.172561,-5.688805,-7.698613,-2.150804,5.023457,7.052883,3.017560,-0.403193,1.863653,-2.853498,7.103269,-9.885137,-1.768351,5.098322,-9.777548,-3.244564,-2.570813,-2.805623,1.692781,-7.064064,-6.676234,4.869631,-1.949943,0.073376,6.470423,-1.678102,4.218477,9.484183,7.391883,9.176947,-8.792280,6.193033,-2.766412,-6.802314,-4.616800,-4.815906,-8.873429,1.519095,9.090933,-9.741972,-1.793929,3.277027,-9.209623,4.532347,7.260990,5.551243,0.982044,8.642626,-4.633173,2.590374,-1.180927,4.474955,7.730944,-5.342781,0.535523,0.824886,6.089453,-5.280537,2.133876,6.888614,-2.191051,4.531861,-1.295369,-3.398230,-7.233455,4.054963,1.322027,4.913890,9.362686,-3.899550,-1.262107,-7.443494,-7.795457,0.597869,4.147862,2.854139,0.844186,0.574141,5.501078,-5.058997,4.068514,-3.998365,5.528265,6.559360,7.736546,8.001438,-6.769615,-6.721558,-0.422433,-6.698284,-7.595965,-9.292104,-1.942155,8.304454,9.885960,8.209092,-4.972910,1.993501,3.624807,-6.465030,-5.662439,0.271372,-5.783830,-9.489904,6.213603,-3.303431,-6.326531,-7.948924,-3.046039,-9.724723,3.608740,-0.676071,2.041967,7.424701,-6.790798,-9.098676,-7.323556,8.192456,7.076779,7.337723,0.659351,-9.468632,-6.781845,-2.006922,9.217042,-4.803124,6.927318,-6.220176,6.313611,8.402622,5.553157,-8.185605,9.254819,-4.950173,1.310283,-1.734440,4.129706,-1.951529,6.490617,-2.020893,6.815123,2.522892,3.549135,-1.201535,-2.624315,2.105944,9.484244,0.811580,9.995080,5.139021,6.047611,5.070755,-3.119213,0.301759,7.940332,-6.063711,-1.221685,7.643850,3.946902,-4.687803,4.914856,-2.642663,-9.849184,-3.522783,8.063247,-5.592051,4.598149,-2.704443,-8.898458,0.203607,3.417733,-2.846165,8.198553,-3.311294,5.935409,-6.746973,-2.862990,1.565677,-9.342316,-6.602209,9.620438,8.503423,1.775782,0.531106,0.713132,7.464669,-1.082673,-7.579915,3.831773,5.362886,-4.304795,9.531417,-2.452196,2.137618,-4.248218,-0.284570,-9.953800,-2.664690,4.984274,3.358101,-3.388011,-0.822168,1.523850,2.078731,7.768068,3.922413,-1.655913,-0.107472,-7.181716,-0.623467,6.592576,-7.735347,-2.287106,6.443733,-0.998225,-3.328573,1.266594,-5.768463,5.891570,8.840747,-0.189293,-8.989285,-3.937556,0.966610,-9.782479,2.836870,-0.134398,-5.937162,9.248392,0.317797,-6.740278,-5.488249,-9.719933,-8.986859,-4.707442,-0.790990,2.296118,-4.997744,5.227184,-9.470517,1.617565,8.729720,5.429399,-1.245739,-2.300203,2.210077,3.486043,-2.887271,-4.693577,6.605034,7.684324,4.112147,7.358317,-8.709130,4.136881,-5.077948,-3.611535,-4.921968,1.839369,-6.659360,-1.000276,2.849595,-4.992406,6.885686,-5.079132,5.576048,-3.347343,-9.435269,-2.632545,-6.845841,5.908532,-8.364415,2.200686,-8.073482,5.475046,-1.054660,-8.037766,8.386212,5.205558,1.106533,-0.270271,3.804586,7.032666,-4.104032,-3.481216,6.973284,1.911022,-4.178012,-0.629221,-7.194555,0.890019,-2.540897,-8.019593,-9.114944,-3.945356,5.323016,8.046975,-3.475413,2.698825,-7.712113,4.686785,3.853014,-4.715287,7.519603,-2.610479,-9.416794,-3.952243,5.513894,4.835493,7.136052,9.354048,-5.174846,4.555281,2.551192,8.217154,4.578110,7.421118,3.554401,-2.997719,1.651076,-7.532613,-3.771210,-6.994257,1.256772,-3.524822,5.500455,-4.865849,-9.990589,-8.942045,-0.009570,0.392801,2.267879,-5.517978,-4.705992,8.078138,-5.204626,-4.797236,7.180847,-4.202244,-6.681163,4.278647,0.818160,2.755427,5.899873,1.887373,6.133776,0.856278,-6.521214,1.751872,-1.330398,-6.718014,5.546465,-6.580792,7.436928,0.781792,4.822390,7.190207,-0.359307,-2.925544,8.618486,6.192266,-4.733641,5.367532,3.811301,-6.731355,5.094486,-1.609966,5.304893,0.111132,7.525049,-4.177457,2.801741,2.350844,-2.156790,-0.311852,-7.019574,-5.629382,-1.671169,0.554172,-2.148016,-6.310602,-6.341798,-7.931829,0.803682,-4.711098,5.448798,0.606904,-0.372690,-2.525201,-2.485111,-8.939806,5.692246,5.664671,-7.036377,4.347405,-9.317573,1.751657,-4.781662,-3.555072,7.556376,-4.979629,2.913822,-5.892571,9.971587,-1.891734,2.396070,-2.031753,9.457660,-6.543785,-5.401817,9.631768,4.142205,6.233204,-2.852465,1.420657,-7.450693,-0.829565,1.858326,6.561647,-7.416687,-9.291487,9.757012,-8.025253,5.485410,-9.367308,-8.234396,-8.865216,-4.420921,1.073786,-8.748984,6.791222,-3.233061,-8.145268,-4.816437,-9.993607,-6.141917,-5.925967,0.870609,-7.976497,0.866762,-9.658593,-5.877170,-7.382773,-0.031789,-6.554259,-7.657788,6.169951,1.762171,5.062021,-7.560659,-8.738796,-1.940357,-9.383213,8.407522,-8.660129,1.110485,-7.905345,-3.141521,2.430048,-4.302774,8.446955,1.724805,-8.911784,-3.303087,-6.115885,0.466188,2.124869,7.419513,-9.911014,4.936813,7.420604,8.588271,-4.248234,-6.614381,0.874348,2.021905,-2.487156,1.019701,-8.930190,-0.839360,-8.168445,9.024479,0.278122,8.713671,-6.746231,1.145854,-0.352928,1.472552,-8.979929,-6.561842,4.343057,-7.307069,-3.533254,-1.342936,7.745003,2.442746,-7.780411,-5.319449,3.419879,2.870393,-8.463077,3.242529,-9.661099,2.586820,8.129688,-7.814948,-4.292836,-3.813723,-1.749208,6.670124,7.847230,-0.716800,5.404299,5.282173,-5.256043,-3.299763,3.016483,7.672081,2.223044,-6.319035,-5.972686,2.623297,2.570897,9.125622,-2.575399,-3.963284,0.070282,4.510365,4.875963,8.874159,-9.012186,-6.298205,-4.094087,0.284950,-1.568495,-5.248949,-3.118797,2.021753,8.500471,7.985089,5.613773,3.576889,-3.045142,-5.515987,6.386312,-1.319703,6.394402,-2.321787,-6.694290,5.583725,0.393159,-2.891264,7.410523,-4.055390,-0.797190,-6.408854,7.065807,4.689736,1.969193,6.545876,2.737899,-8.351019,-6.796509,-1.224477,-4.027822,4.279141,4.454644,6.689731,-8.172196,7.001790,9.511858,-9.041967,5.429243,9.826828,4.493333,-9.182588,-4.508603,-2.770302,0.238079,8.391474,-1.938393,4.729223,-0.185234,0.752488,-8.813116,-2.210185,-0.740741,-7.044251,-8.502971,-0.615087,-7.217722,-1.412819,4.678353,9.200582,-4.354392,-8.722281,-4.159393,-9.178379,-9.078176,8.270981,2.343475,2.388183,-8.225556,7.666661,8.778332,5.285918,-3.470883,-2.618084,-0.292062,-3.716391,-8.358295,6.608983,4.685260,-0.823558,4.186548,-1.650815,6.264089,7.801803,-7.882809,-5.185364,-2.104909,6.715853,8.830723,5.559744,-1.921160,-4.970571,-8.015784,7.374894,-2.061526,-5.153428,8.548932,-1.230332,-4.025949,-4.819826,-5.397348,-6.709033,-0.227465,-2.710011,3.997648,5.127396,8.151661,-4.460864,-2.141022,0.637522,1.677394,-5.311489,1.782117,7.217869,-1.533053,-9.077238,-8.116296,-6.365086,-9.307092,2.814794,-5.729962,6.485773,-2.394990,7.005876,1.355447,1.784499,-3.725466,6.205858,-4.777419,9.290769,2.921468,-1.285557,-2.583867,-2.153836,0.610498,-9.064375,4.119352,8.882213,-7.681124,-2.935320,-9.156948,-5.409749,6.010872,-8.130778,6.667365,5.390761,8.699442,-7.183494,-2.555273,-2.105400,-9.874716,4.197363,9.603231,-6.000415,8.707128,4.609917,-6.505286,6.972115,-7.640278,-1.303464,6.608269,-2.260928,2.657862,3.199030,3.151052,5.137063,-1.751121,2.191480,4.962973,0.910519,-7.527387,-3.558092,2.275201,9.650499,1.573766,7.354542,8.959561,3.191274,-8.697800,-7.147648,8.730758,-9.595410,-1.008822,5.576615,2.807722,-4.498684,6.344508,-7.927360,-0.038859,-1.187201,0.126360,1.241405,6.695283,4.376906,2.728490,-8.960366,7.966948,-8.546666,-4.214214,-6.589564,8.914621,-2.553051,0.881123,4.113899,-3.137330,-9.337622,0.333511,-8.742294,-6.623057,-0.874368,8.240355,-1.623346,4.221878,-4.446065,-9.590923,9.348598,8.369989,3.909575,6.231672,1.067491,-1.129639,0.984218,0.922485,8.396869,-3.394150,9.999492,-2.606805,-1.308723,-3.985845,4.350185,8.257598,-6.423484,-8.750808,-9.450772,-4.575543,4.041455,4.097971,-4.968209,-6.826278,-8.197141,-8.334228,-3.020261,-6.217385,-8.450734,5.407662,3.815133,3.777736],[-7.771439,3.245381,0.102158,-6.648336,4.525566,1.361982,-7.360672,3.401971,-0.320787,-8.794526,-2.479931,-3.439196,8.616230,-8.753282,-3.520715,7.770130,-6.046040,5.152257,-1.405711,-8.871159,5.684454,-0.649217,-4.866979,3.952756,9.575761,1.881973,-3.861819,-9.958134,-7.607188,-9.510207,-3.473978,8.865492,9.393911,-4.977052,-1.590566,9.068541,0.237433,7.002416,3.798712,-9.941713,-5.350093,-1.890242,8.564258,-2.935556,0.637287,9.612685,-9.313120,-5.557018,0.512464,-7.630993,-0.461609,-4.468543,4.684489,1.920564,-1.834382,7.603117,2.852033,7.444078,-1.175679,-9.852791,-4.641830,-8.113527,-2.083013,-1.009878,9.875298,9.709999,-7.235996,4.455469,7.854758,-8.050021,8.822701,-4.582416,2.635723,9.911790,-4.577718,-1.801404,3.662372,4.731570,4.621115,-4.558915,-9.076580,-9.545646,0.116684,-9.421720,-9.250183,-4.179610,-7.198833,6.847642,-9.044269,-0.488751,-7.589124,2.752764,0.418404,-1.850913,2.581278,3.789353,-1.194192,-2.323557,-9.980724,2.732976,-4.719877,-5.713011,-7.749422,-5.839209,-8.913141,9.596202,8.241314,3.198169,-6.407923,-6.572593,-5.133248,4.821860,6.870368,-9.126829,1.381634,0.263139,0.644122,-4.631875,0.383359,-9.257809,5.953054,-9.579814,-4.527084,2.129177,8.966696,-7.679976,-1.326984,3.045344,-2.527240,4.528880,4.697467,7.972363,-0.304205,-3.406627,-8.437714,0.830819,9.452137,9.899478,5.596752,-9.275264,-0.633245,-9.452659,-9.528927,-3.649582,4.829563,-2.206165,-8.423038,2.964300,-9.755900,-2.811883,-8.359609,-1.277315,-1.629317,-4.081769,6.831548,-9.223467,9.417078,-9.978959,-4.673377,-1.359025,-6.772360,-9.526196,-0.745748,6.187338,-5.804433,-2.404769,2.399934,-4.499910,-8.623866,-0.206181,7.069374,4.008986,8.769039,-7.006861,-3.437304,-5.595536,-6.982773,-2.597068,-1.685527,5.400155,8.460946,-4.860555,-4.486284,-3.146632,5.717362,-4.916421,-6.345208,1.730142,1.150534,4.811425,3.277126,-1.128304,9.812929,-0.900634,-1.908060,-8.323648,1.908519,3.177992,7.972573,-1.472658,-4.928270,5.301613,-0.788514,-0.604871,-8.337996,-1.985952,6.679564,4.085404,7.030078,0.007854,0.010829,7.693413,-7.503029,1.343813,2.107568,-8.265997,-1.854888,-5.688090,-2.725496,9.843926,-3.192529,-3.440676,-6.322843,-5.703440,-1.623181,-9.155116,9.955300,-9.279960,-6.051686,8.335447,-7.608126,3.075837,3.570722,1.087818,-4.956433,9.627131,-4.983459,5.276549,2.487241,-0.723477,0.396873,-4.887393,6.999756,-1.695128,-3.593287,2.033515,4.034540,3.702996,-9.525025,-3.970253,4.660182,4.466194,-8.967823,3.992326,5.317221,6.310320,-0.346198,1.542601,-9.920602,1.657793,-2.279523,1.508807,4.199144,-7.931123,-5.979008,-9.599113,-2.217859,1.613883,-2.663864,1.128950,1.599388,-2.780595,-4.741251,5.776579,3.713979,0.711464,6.418034,6.280456,0.946980,-6.195802,5.790228,-3.669178,-4.625878,-7.293459,-0.406060,-3.308304,-8.303274,1.203647,4.239910,4.844049,1.401360,-6.437981,-6.996947,3.787309,4.810398,7.007341,-6.172064,4.853784,7.276693,-8.597487,0.557899,8.714399,0.350248,-0.231038,6.828129,-8.221505,-7.312449,4.384811,-2.482854,-1.094213,-3.362251,-6.562107,5.349018,-4.817606,7.541897,-2.704508,0.639349,-8.462727,-9.732882,1.955970,7.156784,-2.819009,-6.002628,-1.243736,-1.339800,3.009030,-1.072594,-7.266911,6.440938,-5.564423,5.101316,1.078707,7.353415,2.304277,-9.361488,4.317393,-0.663313,7.695762,-8.696236,-4.079815,-1.019948,4.599246,2.180523,9.358645,-7.319624,-0.326154,-4.366799,3.668253,9.767861,-9.640674,0.943702,3.961286,7.170601,3.375631,-7.929300,6.484821,6.195619,6.715739,-0.059482,8.042936,9.939644,-9.465922,7.673579,6.275674,-3.000243,-4.874161,2.101282,-2.649149,-6.269195,-7.775820,4.459082,7.231944,9.858374,2.099244,1.985915,-2.608075,-2.822710,4.147569,-4.327523,4.745296,-6.411282,9.453183,8.479762,-2.459174,3.966716,2.572425,-0.721276,3.537742,9.042598,5.738055,3.765047,7.623212,-7.939683,6.878487,9.495751,-7.727074,-3.956272,-8.601082,9.351219,0.905999,0.295656,5.712626,1.318404,7.939017,7.415773,-6.178061,6.605333,5.497209,-1.283328,-9.009970,7.179086,3.027460,-9.202377,7.321609,-0.276193,-5.465272,9.924353,-6.445877,-7.290055,-7.771730,-4.550664,-0.362404,-7.828030,-3.097031,-8.369660,1.074829,9.453255,4.190567,-0.245350,9.853133,7.453531,-0.868498,5.874644,-6.437666,4.480604,5.574184,7.110432,7.762306,5.265726,-2.471871,-9.899471,0.368607,-0.656420,-7.719860,-8.760671,8.264946,1.555497,-7.663404,-5.545574,1.541915,9.491087,-1.213430,-6.067742,6.848032,6.719261,-2.108936,7.574817,9.796538,-3.724522,-1.807833,4.835570,0.223495,3.420008,0.474165,-6.245750,7.063772,1.947158,-6.793471,0.043750,-1.584429,5.685691,5.581310,-6.278014,-9.216436,-3.444459,5.006827,-2.606340,-0.676102,1.584391,-3.281515,-5.000561,1.456138,8.495960,-4.032708,6.340543,9.699310,6.134311,3.855515,7.747229,-3.932190,-0.042592,2.237520,-6.348785,1.958410,2.541601,7.547378,0.635810,2.296956,-1.234484,-8.836937,-9.856826,-0.414257,-2.881226,-5.953681,9.069564,3.385086,-4.668066,8.010688,-0.573936,-0.859851,-7.154126,-3.880160,2.924797,-3.166711,5.523360,8.798390,-6.588367,5.167828,-6.153913,-1.597912,-2.428013,6.155387,-5.459988,-6.435173,8.124333,-5.691023,-4.798752,-8.345249,-9.866146,-1.306840,2.096355,-0.124472,4.202775,-8.082385,1.424661,-9.466243,-1.648729,-8.932178,-8.992087,3.239059,-6.434889,6.644511,-3.872355,-1.020974,-7.271551,-8.662052,-2.419405,7.169954,-4.798356,3.845091,-9.435349,-2.731773,-4.718943,1.437650,7.807541,-3.814021,-9.126760,-2.304789,2.033834,3.498656,1.486707,2.949677,-8.531755,-5.614982,-0.278545,-8.015742,8.937996,6.196764,-8.350826,-6.866416,-3.502036,0.682015,-8.493126,2.514245,-1.768568,3.521936,0.898351,3.951175,2.705762,-7.376490,-7.281106,-1.619154,5.883684,7.762135,-6.770079,9.419974,-6.064151,3.149324,3.358755,6.870007,9.794678,6.454976,7.778209,4.459342,-0.952912,3.212364,-2.101895,-4.410037,0.189778,8.455467,8.167346,-6.897352,6.870054,-4.233883,5.501095,-8.959752,-4.457548,9.863677,5.619623,-7.168743,-5.825855,-7.572411,2.774125,3.050771,-9.914564,-7.183557,6.489436,2.196897,-1.704719,7.754893,5.052459,5.165749,-2.735211,-4.410865,2.015369,6.865890,-7.214986,-8.285519,5.172404,-6.656670,4.936932,8.360193,-2.506015,3.949157,9.501281,-7.261056,9.481785,-0.544267,-2.804352,7.112311,-7.459003,9.698455,-8.679291,-3.987526,1.386794,9.255521,-8.015921,-6.718257,0.913301,1.657077,-9.087905,-1.759177,9.140952,3.781276,2.643245,2.625202,-6.333264,-9.997173,4.853442,-5.486160,6.066389,4.268871,-8.159635,-0.392492,7.354842,-3.779923,3.810379,1.956699,-4.650519,-6.180073,5.536393,9.969780,3.742167,-2.151534,-5.670385,0.900305,-1.457832,4.831218,-0.253613,8.195129,-2.576402,-9.693865,-5.419680,-2.887126,-7.371624,-1.403943,0.125821,0.587859,2.876594,2.801978,-7.317966,7.786133,1.236456,-1.612784,0.997405,9.581145,1.644420,8.627992,-4.182800,-7.884733,3.540719,-9.079603,-1.064088,5.896005,-2.773898,-4.779019,0.714954,0.731182,-5.249059,6.598530,9.825732,1.914281,-8.484202,-7.048319,2.775667,7.277260,4.929496,3.147868,-2.497784,3.910748,7.183048,8.294706,-1.727322,6.023832,-2.347937,-6.740890,1.930534,6.518079,-5.707826,-6.611047,-8.096981,-8.152423,-6.353703,-1.803966,-3.641651,2.036049,5.258235,7.556348,6.601199,-9.239968,3.455470,-0.866369,5.901166,-2.607297,7.569663,6.589208,-7.096789,-4.158115,7.249699,1.188003,-0.930049,8.907429,-3.367382,6.179167,3.252087,6.584167,-3.405294,8.084208,0.510413,-4.322620,5.193304,7.283537,1.365595,-4.777941,-0.406152,1.033728,-7.865069,-9.550949,2.993551,-3.250447,2.709470,6.235653,4.427520,8.246452,-2.471163,-4.476291,0.519929,0.919912,2.103495,4.037089,-8.842847,-6.134874,4.571656,8.481796,0.508603,3.523586,9.019640,-8.398317,-5.795111,-1.541261,6.127767,-0.780469,-7.356027,-5.044168,5.475845,8.947066,-4.069528,-6.788637,-9.140146,-9.000902,2.905781,-1.537139,-5.644781,-6.874040,4.868159,9.772735,7.718352,1.766729,9.287524,4.140657,-4.924191,-9.637869,-5.961778,-4.655983,-0.864928,-3.840381,6.458614,1.482003,-0.894806,-9.043834,-6.513811,-6.715616,0.364178,7.606857,2.232520,7.254502,3.663881,-3.703059,-5.452064,-6.312567,0.958907,-9.403013,9.043356,-3.274849,4.742171,9.307139,-4.568667,5.262160,-4.763006,8.109109,1.224837,1.785544,-1.328087,9.854744,-6.351270,-2.183185,-0.149247,-3.118136,-4.876394,9.480390,5.506642,6.811614,3.156402,6.134549,3.384196,0.167725,9.043373,5.910072,4.994907,-0.147291,-7.499846,9.659154,-8.485066,-6.524312,1.520305,-9.974986,0.435663,-7.387721,9.742402,-4.455274,-9.921868,6.464086,-7.288120,-1.801836,2.332366,6.397584,0.950926,6.572791,6.855177,-3.546177,6.909999,3.086665,-6.541972,0.393752,-1.260635,-5.234198,-5.844729,-5.069007,-0.439855,-0.946234,-5.688711,9.858344,-7.682630,5.969790,-0.672650,-6.811381,-2.924400,-4.895130,-4.955669,-2.328712,5.336735,7.062612,2.514779,-3.543874,-0.232958,8.094512,3.579518,-9.480120,9.435195,7.970159,3.404822,-0.254323,5.018232,-4.424735,-5.210917,-4.171949,6.048988,5.262061,-1.440737,-4.000140,-0.678115,2.094313,-0.704966,-7.061542,1.795227,-1.111144,8.796181,-3.135407,1.213629,-9.525693,-1.107476,-6.068814,2.480799,-0.263187,3.909924,-6.815928,-3.830701,9.144841,-8.259947,2.852365,1.621785,-6.009417,-1.910587,-4.646559,-5.613356,5.724279,3.595663,-4.463787,-8.288833,-7.161389,-7.592136,9.843096,-0.739169,0.836420,-1.972711,-8.419438,-5.664530,6.989799,-6.242030,5.448107,-8.432949,6.629666,-1.209403,-5.665862,-2.786540,-6.351730,-1.364422,4.149472,5.446680,4.192298,0.583804,9.626554,-5.859561,-0.119443,-7.524902,5.515669,5.860138,5.651199,6.622101,-4.474488,-9.386099,-2.242025,-0.609101,-6.519653,-2.460413,-3.072458,2.945191,-4.787894,-0.462616,-2.802998,-0.376099,0.155953,-6.629312,8.481778,7.370435,6.353194,-1.828187,-0.380042,-6.935224,-2.609371,-4.836842,-4.440692,9.388397,3.824669,-7.820000,-3.643933,-0.218664,-0.027517,-2.443553,-5.656096,0.021823,-8.916248,9.944410,-7.441534,9.692120,-2.891765,2.888639,1.962320,1.028267,-8.144684,1.824344,-0.964818,5.549780,-2.036330,-5.648464,6.196871,8.704099,-9.818755,-9.170328,-5.675293,5.457644,0.834321,7.424842,2.001692,4.341241,-6.565813,0.035622,-9.342493,4.999045,-4.551887,8.478273,1.845424,6.559072,2.670226,9.882063,5.380948,3.824936,9.212223,-0.552850,0.486745,0.773729,-8.727212,2.834925,1.501839,8.688115,-6.705486,5.937413,1.061718,7.595024,-7.341985,-3.780598,-2.220145,-6.605970,7.169900,-5.294681,-1.683056,-5.251631,-7.141875,-2.343221,6.626769,-3.964680,-9.633963,5.040145,-0.706757,2.182454,0.808895,4.503866,4.167113,-9.765802,-1.640698,6.233483,-7.305975,8.399007,9.163477,-1.695107,8.287234,0.996766,-4.832651,-3.455494,0.412981,5.515275,8.293259,-4.208145,-7.980658,5.213336,-3.187234,3.709714,9.835074,2.440195,-7.703960,7.021375,-3.718606,-4.209592,2.776011,-8.655357,-3.122709,-7.584383,-2.703461,-7.854845,5.675058,6.762873,-2.344726,-2.532762,7.775081,2.004021,1.718605,5.046185,3.638114,-2.021367,-8.212854,8.991524,-5.946905,7.388395,8.204044,5.244939,5.560223,-2.427965,6.737906,4.639489,-3.410491,6.349398,8.990277,-4.626680,-6.148866,-8.510256,8.980431,0.954215,4.096705,-1.128719,-8.611374,7.115919,-8.573363,8.048818,-4.854611,-5.610606,3.566545,-6.482526,-3.445576,9.442213,7.148784,-0.594802,-3.719956,-7.374668,-6.904360,-4.267597,-8.303021,-3.869947,4.487302,-9.884493,0.883894,-0.481455,-1.789167,7.300258,4.127802,2.072262,-9.203555,7.492877,0.297491,-9.899719,-1.432202,-0.223296,-5.418649,8.651299,9.181449,0.841971,-1.781836,6.073180,-8.330854,-3.410033,-8.046855,-5.746598,8.527135,1.252525,5.245436,-4.385603,-4.068197,-6.229831,7.972327,-8.577089,-0.123325,7.310863,8.375599,5.863142,-6.487203,-7.270529,-7.441135,0.974566,-6.888908,-3.096542,3.341797,-9.918751,-8.647658,-2.664266,-3.129634,-4.219185,3.755316,-1.347348,-2.309445,-0.798984,4.435929,1.765217,-4.613410,0.214755,9.933215,-5.783851,-6.058800,-6.130419,-1.880547,-4.399923,3.082752,2.704616,1.022620,-5.129092,6.098381,-7.997824,5.119389,-8.833680,-9.676194,-9.206171,-7.844282,-6.103659,2.863302,6.349795,-0.635091,9.017245,-7.406130,-7.857432,-3.120671,0.929926,0.168686,-9.938969,-3.810543,-9.559967,-7.442552,-1.504038,-4.295664,5.263185,-6.869158,8.195032,-4.937440,-3.057996,1.116077,-4.682832,0.142971,9.047898,6.800058,8.434331,7.607176,2.460998,2.405090,-3.456837,-9.249827,1.752744,-6.881928,6.182594,3.432880,0.862146,-7.679572,-2.322703,1.299758,8.869701,8.684915,-5.705094,-0.995440,-1.641271,-9.237415,0.818100,-4.240296,8.658974,6.416761,-3.799176,-4.616148,2.715414,6.053651,0.719604,-3.536026,-1.088793,5.186267,-5.324393,-3.879567,1.457711,4.372981,7.313382,-6.395382,-9.819548,-9.944529,-6.618186,-7.135832,8.686912,-2.881013,-3.068079,8.534608,-6.713162,-0.800069,8.620047,-6.112518,1.563000,6.574584,0.700962,1.681366,-9.042444,-1.010963,-8.272287,-7.353918,0.096541,-3.347674,6.838731,-2.080322,3.868167,-2.874255,8.745375,7.683824,-9.243668,4.347941,-4.640219,3.953179,-6.088214,-3.754167,-9.470431,2.969074,7.294479,-9.425809,8.580489,-2.026846,7.639486,2.280690,2.871326,4.636378,-2.476084,-1.486739,0.670152,2.945672,5.889620,-1.793604,-2.595898,1.774955,-4.704163,8.864074,-3.238636,-4.057245],[-2.096300,-1.329200,-2.672490,-9.964514,2.328813,-9.199758,-4.512107,-4.318768,3.887571,-8.346945,-9.201677,9.254134,1.755187,4.818468,-2.786832,2.591891,2.375124,3.627303,1.388271,-9.942716,-3.186393,9.890375,-8.551206,-8.039043,-4.517913,-5.945283,0.196917,1.538790,-1.465411,-3.797974,-6.790486,6.147295,-6.400015,-8.580045,-9.153296,-8.082252,9.280007,-7.491724,3.105547,4.131707,9.852743,8.588495,2.783927,5.539638,0.157123,-4.583693,9.357941,2.082376,-7.291077,7.976346,6.294990,9.769572,1.972199,-8.152362,9.558730,-1.150215,4.620328,1.336769,6.710108,-8.465399,-8.594713,-7.487425,0.544281,0.253543,7.776661,-4.316591,-1.189774,7.483948,6.475885,7.907170,8.045904,5.969993,4.379427,6.675845,3.783010,2.908736,6.607154,6.726318,5.796941,-7.408539,9.604496,1.406311,8.834475,7.717521,6.630155,5.197737,3.363187,7.069476,6.190594,4.538856,4.048915,-6.173005,-0.670813,0.245363,8.944241,2.291155,-7.280531,-0.987728,7.486382,4.754709,-1.390209,-9.775789,2.132644,-8.700791,-9.835838,-9.378777,-6.983413,-1.101332,-8.073636,7.884159,-7.534882,2.548468,8.600315,-1.587836,8.138813,6.096529,-4.242856,5.585786,-5.662289,-0.352319,3.689338,-3.657025,6.019663,4.488055,-4.673208,5.845280,0.398696,7.046821,9.678221,8.244223,5.143734,-4.337907,-8.358092,-6.558958,-0.959908,-5.417501,4.209833,8.360532,8.210272,-9.271230,3.290752,-3.260978,-8.277892,-6.557442,4.259032,7.719712,-9.180730,-4.359639,9.868203,2.006943,2.511047,-9.271496,-3.060135,-5.688563,-0.629389,1.839435,-5.964257,-1.444024,-9.513379,-6.048520,-9.845637,-9.940879,-0.888606,-9.649305,5.135950,2.672450,3.745423,9.953714,6.425216,8.374566,2.409991,-3.078172,6.300743,-4.824806,9.573459,2.372837,-7.129698,-9.085485,7.818647,1.685039,6.152058,7.461451,-1.977546,-8.653622,-7.394244,3.261148,4.836147,-4.400301,-0.931710,-2.833354,1.583870,3.862349,5.290409,-0.389333,-1.700024,-6.896631,-9.660576,-9.111433,-4.729920,8.738737,7.797578,-3.062593,-9.111692,1.070345,-2.309432,-0.536400,3.089145,7.918248,3.580533,8.241629,0.961161,9.345727,-0.051993,-1.806023,6.052355,9.821269,-2.128613,0.263186,-6.614062,4.181185,-4.147287,0.032694,-2.787055,-3.497423,-9.996421,9.753560,6.304826,-7.636403,8.676559,2.491166,-0.477023,9.390220,-9.629599,0.604294,7.066114,7.251685,-4.735549,5.473209,-0.233096,-9.257850,-6.393487,-1.641659,9.516078,5.106761,-6.469323,4.608728,3.166389,4.056724,6.067874,6.552195,-6.606555,-2.694469,2.611337,8.896874,6.945090,-6.591072,7.029724,-5.934508,3.042133,7.854026,-0.829237,-6.097903,0.827097,2.135763,-9.002974,0.691773,-6.612833,1.085068,-3.203185,5.169724,4.279475,0.521268,-2.170430,5.770097,6.492212,9.906730,2.272663,5.464480,-2.833693,6.099591,8.065632,8.866887,-3.429143,3.969398,4.711088,-9.191999,3.803047,5.308095,2.885522,4.006486,-1.348782,-5.897660,5.163082,-0.481978,8.572278,-0.665240,4.632421,-5.013463,7.066906,-5.995511,-8.879571,4.705036,-0.013114,2.190578,3.858961,-5.759867,-8.492677,6.363294,-1.417880,4.016309,1.026256,8.298887,4.787556,-5.627768,6.143786,1.743744,2.906356,7.228015,9.617139,-0.063435,-6.063764,-4.098801,5.254452,-5.386959,-1.937374,3.807686,6.523508,-3.815625,-4.510222,5.184240,6.818197,4.637615,3.764219,-7.033235,-2.854390,5.820886,7.314090,5.360836,6.366247,-9.526605,2.299431,3.748644,-1.288695,1.650543,-0.558757,1.054939,5.996177,2.349631,8.313902,2.386681,-0.866845,-1.907902,5.939666,-5.483880,0.052101,-1.164078,8.835871,-5.112754,0.858132,-8.662591,-5.845990,8.002599,1.149529,5.735528,-2.184208,-2.412045,4.643197,-2.795233,-7.484168,-2.683245,2.320720,-9.701370,-7.597915,6.854298,-6.185149,-3.892977,5.454867,-8.988290,-6.668018,5.913216,-4.398339,4.753946,8.737200,-9.596078,-9.291669,0.641458,2.626744,-5.235046,-9.004751,3.848087,-1.372054,-3.485239,7.853932,-5.828843,-0.250909,-9.459844,1.534931,-6.781342,7.781752,-8.164941,4.387800,-8.323130,8.748933,7.267186,-5.023942,-2.300868,-4.031379,-9.858598,5.841162,3.348092,-8.982377,-1.560887,8.780555,-7.660943,-2.328375,-5.148003,2.241172,-2.684924,-5.327593,-3.505570,6.232512,5.739818,0.662378,3.705524,-8.143929,-2.472417,7.218381,-3.131504,-2.410963,8.827653,1.823689,-7.919221,-3.873950,8.642929,-2.426300,1.037524,-9.015326,7.410675,-7.255878,-8.006466,2.206544,-5.793039,4.617792,8.921500,4.271306,-0.492790,7.099380,1.869858,-4.667163,-6.347053,2.842471,-9.747497,-1.121053,9.754196,-2.742065,5.547534,0.802202,-6.386900,-7.378470,-4.328189,2.804012,-9.208279,8.488052,-7.762608,-9.197880,1.314762,1.911475,7.443801,0.873296,-0.250786,-2.779098,-2.263895,1.901725,-8.125486,-0.976411,-7.132849,-8.239428,-8.997134,-4.674841,8.287850,8.628287,-1.486535,-1.125053,-6.961354,1.772190,4.724039,-8.841531,8.592653,3.286698,5.526842,-0.022620,7.092878,-0.446207,-0.668470,-3.185985,2.747885,-5.517842,-3.246686,0.475734,9.706338,-8.248696,-6.098840,-9.990181,-7.172614,-5.883334,7.758692,2.732417,3.128456,5.489297,3.380014,4.429731,5.253632,-5.412590,-5.215935,8.749410,-1.138183,-6.762202,-1.151015,-0.979423,-2.319353,1.061171,1.279711,-8.966272,-7.727126,7.603787,-4.958750,3.075329,-6.665077,3.229983,3.048902,-5.749170,-9.740908,5.122958,9.493308,-6.547960,-6.760115,-1.920589,-9.117976,-8.556142,-0.675271,-2.795487,-7.686445,-9.326359,-8.230444,0.118994,-5.880958,9.247291,-1.713298,-5.319184,9.076263,-8.995524,-6.258255,9.480801,9.949910,4.180152,7.251639,-3.824453,0.214183,7.263922,3.791599,-6.802923,-6.811609,-2.280981,-5.878249,6.146355,4.492357,6.072496,-5.014983,2.543268,-5.352746,7.964576,-8.386429,4.763128,-1.157418,5.527121,6.713148,-9.830392,-4.110431,-2.579768,1.512315,-0.603261,5.786973,-4.952618,-1.264682,-9.230418,-2.011241,1.862465,3.152311,6.740110,2.221686,0.268581,-8.608766,-1.462719,2.089441,0.111401,-8.114700,1.598020,5.744926,6.702069,1.943324,-5.380415,3.252735,3.292421,-9.704550,2.691991,6.253156,-6.102355,-4.661273,-9.026292,5.002153,-8.474740,6.165124,-4.386075,8.040450,6.336833,7.769608,-4.668465,0.094100,8.598146,-5.169492,3.835122,-3.333098,6.998081,-6.840680,-2.281978,6.570156,-9.127552,-5.458370,4.104307,-1.281253,9.194987,-2.545131,4.636505,2.307784,0.261023,6.931961,4.970019,-9.866764,-2.705179,9.661472,2.311250,4.766731,1.947344,-8.190836,8.382320,9.088626,-8.140883,-4.345265,1.763179,-2.005963,-5.717726,7.109079,7.804126,-6.659379,0.902352,-2.319273,2.233110,-0.129848,-0.786709,1.189775,3.398686,-4.337407,2.193412,5.813019,-4.462867,1.877311,2.683495,-3.042105,7.491653,-4.873460,-5.484625,1.977360,-0.104129,7.263394,-7.447299,-5.761745,9.766012,8.077303,-8.345185,-8.846948,-7.062069,2.723388,-5.661135,1.177810,-9.891135,-4.299566,-0.195974,-6.227889,6.024170,5.326784,3.611119,-8.307922,-0.072552,3.309532,-2.130894,7.832708,1.991579,8.913624,4.255795,1.224874,-8.413988,-8.349849,9.616143,-7.496523,-7.009045,-5.922460,9.603069,1.105530,-8.936259,-5.782683,-2.968844,-4.945341,-9.537344,0.737116,-6.986981,-2.702512,3.406340,1.320369,6.172778,3.390978,-9.028533,3.772570,-9.234459,6.975613,9.146445,-6.275287,-4.292923,-7.578459,-1.260569,-6.221316,-2.117650,0.290376,5.773073,5.734460,-9.465479,3.079803,-8.765839,3.735062,7.777117,-0.660330,-3.363463,-2.289316,1.121425,-6.213165,-7.937707,-6.717979,0.242520,-8.965359,-5.336471,1.234222,9.473400,8.405373,-1.839082,-7.715223,-3.224800,-0.488161,7.665644,6.228855,0.063555,-0.314283,-9.827053,8.021174,3.185942,-5.653042,5.940338,-3.256018,-2.776149,-3.144207,-6.546290,-4.128551,9.309128,-2.880047,4.655410,5.860485,4.336193,4.951263,-4.993448,7.150606,-8.198446,-7.591316,1.040964,-9.792419,-7.823869,-7.029110,-7.085696,8.444000,-4.829341,-4.851920,0.356466,-8.489818,-0.459042,-1.748344,-5.839119,-0.438881,-5.626221,-2.764302,8.424379,5.488962,-7.441425,8.350361,9.970720,-5.657545,-7.900435,0.057143,8.027323,-2.813459,9.227813,-1.921628,-4.800033,4.707406,3.955808,-3.978904,-5.846609,8.201630,-4.685690,8.377341,3.222485,1.798877,5.242550,-4.838089,-4.668752,-2.059522,1.040290,-4.751365,4.334800,-8.729840,9.927864,2.909247,6.502090,-2.597876,7.150092,9.836074,-6.455094,-0.746872,3.459299,-7.282252,6.730279,-3.897906,8.086827,-9.040928,-5.695745,-9.588444,-3.403857,9.597895,-6.492091,3.414000,-1.412854,-4.885879,7.490618,-9.493853,2.264511,-7.385006,5.489032,-8.822525,4.313678,7.272422,1.751370,-8.026097,7.772105,1.649046,1.808390,-8.042848,5.893119,-9.102898,9.548057,-3.087947,3.170140,-8.941354,3.833212,-4.307975,9.579614,-6.532248,6.611483,-6.083560,-2.569608,-8.120967,-5.318361,4.645018,8.897377,-8.227146,-8.179302,-9.360356,-4.857283,-8.390824,9.816508,-4.393701,-1.026567,0.762604,2.564995,8.819126,-7.357428,-6.309030,-2.128841,-1.998610,0.013305,-6.519356,6.943770,-1.020730,2.851527,4.953164,7.291531,-0.917257,-0.802390,7.870052,1.157249,-1.330543,-2.654544,1.218320,-9.058673,-7.186473,-6.071395,-2.419736,5.719360,4.465446,8.405324,6.048732,5.606481,8.438929,-8.675693,5.451185,9.362992,7.519895,-8.101468,-6.524167,-8.411968,5.207308,6.385746,4.071863,-0.759194,-7.405414,1.614587,-5.985328,1.418717,6.248455,-2.260018,2.685887,-8.714821,0.668001,2.381534,6.276640,-1.107556,3.272157,-8.020252,3.377925,8.506200,2.950157,1.745900,7.015125,7.410013,-4.679327,-2.435891,5.350846,-9.232494,8.987499,-8.839482,-3.842141,6.846030,-5.535006,-1.442679,-7.536166,8.921952,-7.571668,9.587436,9.397677,-5.817531,-6.115940,-2.960288,2.723464,-9.321989,-7.084619,-8.344790,-7.558564,-0.866819,0.200878,-6.173613,8.128730,0.252106,-0.255296,3.580643,9.704033,-3.659703,-8.247723,2.688630,2.358522,3.996781,-7.335030,-3.155914,1.660850,-9.166518,9.600198,2.925620,-6.904513,3.364786,8.903370,0.133332,-9.422172,6.175273,-8.449556,8.959122,-1.981774,0.781109,-5.175042,3.346992,2.142115,-5.231132,-0.884301,7.366709,8.193842,-7.183863,7.021694,7.844908,1.307486,9.675799,-8.020540,7.836154,8.630556,3.448208,9.874745,2.477177,-9.835807,0.453404,6.294079,-1.801915,4.220506,-2.077221,-6.326393,6.848734,-3.775389,2.001505,8.025396,2.974455,4.705190,-8.381953,-3.831777,6.826767,7.038906,3.984541,9.248556,0.235447,-0.106008,-5.286320,-6.227065,-0.830926,-6.230627,4.588679,1.616362,-1.406702,9.425006,4.355587,-7.628212,6.648955,0.428315,6.436687,-0.365057,-9.833397,-9.075492,7.574332,-3.573061,2.024300,9.334072,-0.950023,4.927852,8.705198,3.602139,-6.772883,-4.391071,7.227696,3.735007,-0.962620,-1.541898,-0.504452,0.734729,7.316180,-4.382475,-1.982333,9.720524,-7.456094,2.032205,7.137728,-5.397167,5.503426,3.385263,-1.530389,5.499141,-6.455375,1.865625,-9.788045,-1.526917,-0.280958,-5.135139,-2.657436,0.107041,-8.371271,0.632203,9.435385,-6.009596,-5.871692,-6.813976,-1.373249,8.071076,9.823734,1.881944,-5.804864,2.578025,-0.710303,1.788198,6.885232,8.660283,-5.735349,6.191508,-9.731429,-1.585159,-6.332526,-6.890595,-7.552066,1.140823,-7.961006,1.594957,1.504688,-0.489720,-1.582693,-3.073224,-3.395223,9.505264,-4.994330,1.515636,-7.102187,9.872394,-7.472986,2.133107,-7.964807,-7.880289,-5.831486,4.405714,-3.394351,6.202769,0.172985,-3.845787,-9.954461,-3.481955,-0.980115,5.242314,5.682326,4.757988,-3.278099,-4.593322,-5.274605,-6.532298,-4.460175,-5.655906,7.402934,4.767497,0.153400,-8.063617,-1.732244,2.219950,-5.567272,3.256490,6.297077,4.455324,-5.037197,-0.412820,-4.867617,1.978490,-3.670515,7.528287,2.983167,8.604596,-1.651217,-5.597480,-9.214896,-2.997850,7.420426,9.636952,-9.314849,-7.393261,-0.418498,6.987796,1.733955,-4.962284,-7.518535,0.686161,-0.493416,8.824626,3.141091,7.668832,0.508121,-2.356628,-3.327770,3.167592,1.335630,2.098096,9.383101,-3.586592,8.955775,-8.860988,5.931817,2.722984,-8.709422,-3.005346,6.184269,-6.094662,0.559339,5.132136,-9.561331,1.314099,-6.030579,0.836984,4.482989,4.904962,-2.412065,7.716405,8.949288,-5.310013,8.779478,6.154379,-7.653251,6.000944,9.227619,9.422331,5.362506,8.558411,2.105575,2.901513,-1.251134,4.306405,8.755710,-2.941795,-4.024218,-2.421433,-3.824697,-1.110064,9.504614,-0.235814,-4.391451,-1.054102,-7.077437,8.593679,3.209857,9.802403,6.165086,-6.230314,1.765528,-4.572904,3.743388,8.379142,-2.697727,1.925461,1.869905,-8.322294,6.856013,5.856021,-5.807561,-7.168989,-6.567723,-2.077030,-6.616566,-7.475918,7.058325,7.096597,9.566060,-1.016755,-6.974662,-5.769096,-0.615077,0.802578,2.651023,4.313944,-0.045609,5.266250,8.537980,-4.540442,6.739625,5.219170,8.790116,6.607849,6.494680,9.795356,6.507509,6.037809,-7.522446,-3.127091,-2.895630,-0.143494,7.612073,3.088847,5.433472,-5.191243,-9.016181,1.542175,5.159587,-0.853098,3.620878,-3.608826,8.739667,-8.483787,1.566126,-0.291073,-7.116982,-3.187582,-4.773075,2.109716,9.445318,-8.356767,1.447581,-5.863682,0.179407,-6.955389,-2.529945,1.273991,-2.067922,4.488720,-1.048081,2.999364,-7.092951,-0.132825,3.715245,-1.686933,-8.855374,-5.406855,7.187900,-3.187216,-6.176856,8.695552,3.474358,-2.772451,-2.086733,8.977811,2.685685,9.342688,-7.935354,7.731851,6.279243,9.136957,-1.683991,-1.571259,-6.447377,-8.651048,5.582801,5.333073,7.965210,-8.157476,5.312194,-6.032559,3.278302,1.321310,-4.303647,3.110939,-2.985057,3.995266],[2.519069,-6.240527,-5.623257,-4.422026,-3.589866,-2.569598,9.019831,4.011082,0.494471,-3.261017,-2.725494,-1.716789,-2.843877,-0.358923,-6.875249,8.092182,0.934417,3.965681,1.983213,7.790915,5.588504,1.483991,2.411214,-5.180275,-5.330965,4.857978,-4.305420,3.813920,5.621379,7.659533,9.135824,7.308486,3.880259,-2.735198,-9.671424,-4.511300,-4.190510,9.440942,7.798224,-5.507959,-9.382893,-4.502197,5.067379,2.639439,4.797798,2.720801,9.086426,-0.557369,2.582701,4.853544,-9.798347,-5.033950,1.110281,-6.723359,7.873252,8.997401,-2.812011,-8.499504,5.440223,4.667081,-3.414985,-1.929707,0.982266,-2.045272,6.417550,9.819807,-2.429742,-9.977666,7.275046,-6.452219,6.921305,-1.058263,8.071928,-7.050755,-1.361952,0.510777,-4.885075,-6.051501,-0.076850,-8.844639,3.564975,-1.865347,6.385073,1.812300,6.384250,4.208449,5.958691,9.401488,-0.107920,-3.740805,7.778628,-7.659162,8.141834,2.927002,3.060512,2.287880,1.614679,-0.354531,7.656689,5.399559,2.948310,2.783025,-3.175278,0.277801,-9.699012,6.973356,-0.358490,4.090473,7.744076,5.742311,8.206715,9.159968,-1.991711,9.256441,5.501159,8.559546,-4.880263,-8.345646,8.310042,0.986453,8.127699,4.833193,-0.911725,9.502882,1.947469,2.706846,2.206196,-2.546696,-8.035038,7.279861,-1.312762,7.432466,-8.149618,-6.708625,6.491204,9.920437,-9.615743,-3.655387,-4.944961,-6.997164,6.855059,-5.399002,-6.133564,-9.485484,-7.143874,9.905396,-5.625395,5.619666,-0.895881,-6.036100,-4.673746,-2.525682,-9.254945,8.099287,-0.790596,9.776007,4.409945,-6.490161,-8.728933,7.277943,1.280535,6.828854,3.168258,-4.270628,-7.434386,2.767941,-9.219081,-8.953567,4.419973,5.841197,6.966537,7.737252,-3.691367,2.375709,-7.383328,-4.595992,3.815091,-6.136565,-6.677837,-9.178628,3.090638,0.445931,3.432998,6.441842,-4.521088,-5.851159,5.108633,-5.302336,9.791497,-7.882584,-2.489731,9.485979,-9.489072,-5.164621,-7.109994,-5.369869,4.073756,-5.478332,6.714156,8.346514,-0.259463,1.633170,2.675715,-7.327696,5.437688,-6.153407,4.509456,4.218847,2.427178,-1.791128,-4.480653,-9.092551,0.972120,-0.519552,-9.189522,-9.686740,5.489391,-8.943540,8.389007,-8.080266,2.232270,9.325816,-5.040834,-1.484558,-9.557135,-1.894787,2.960517,-1.913209,8.218435,3.646733,-1.854543,-6.499784,-8.931410,-2.630380,3.326845,-5.962591,-2.093675,2.636875,9.545372,-4.981084,9.711243,-5.689495,5.748061,6.721698,-3.489391,-8.995347,-8.345795,-1.512149,4.018314,-8.170882,7.536398,9.657133,-2.325739,2.512016,4.474269,-3.071633,-1.461632,3.469663,3.497377,-2.396600,-1.419111,6.255312,3.377946,8.063839,-5.820527,-4.781949,-4.527703,1.168179,-2.113156,-3.680854,5.332730,-9.138455,-4.048341,7.465084,-2.724939,7.056494,4.802843,2.583135,-1.648418,5.586072,1.335097,1.227272,-3.117702,-3.706544,6.713423,-5.233791,0.325857,-2.562237,-6.656221,-8.521862,7.201200,3.528162,-1.872933,3.400174,1.717589,8.110216,-2.623586,2.286509,-0.196082,-1.974092,-3.862069,-9.374003,8.324914,9.525069,-8.305403,7.073318,5.350446,-4.545498,5.713927,0.017391,8.400935,9.339342,9.282964,-1.522272,0.978972,1.658137,7.236422,3.040324,-4.164834,-4.000517,-4.480151,-8.390077,3.971364,5.989752,-5.432098,5.512250,-1.584460,-3.828374,0.170309,1.801550,2.009675,6.004044,-9.015924,7.697432,7.301913,8.998716,4.295773,-5.741500,5.961762,-5.483478,-1.256267,4.727948,-2.870219,-7.211059,-5.140057,-0.183324,-1.158166,-9.949390,9.095088,6.354283,2.526968,-6.887204,-0.200332,1.947943,7.947974,5.065387,-7.147571,-0.242679,-9.573180,-6.520655,-1.354781,-9.265864,-3.958973,0.317748,3.210858,2.350785,3.033986,2.605666,-4.054979,3.298290,-7.633679,7.137456,8.481830,-1.407285,-6.685596,-3.710777,3.798417,0.480860,1.376007,8.829267,1.591344,-9.319819,9.939474,-6.645002,-5.057808,0.478428,-2.435350,6.981075,-0.718422,-9.867078,7.815148,4.935529,4.036193,-1.824921,0.944467,8.729514,-0.973654,2.331285,-2.291575,3.530048,-2.372349,9.902009,7.664010,-8.061615,-0.237728,-6.131879,-0.377432,2.222803,-3.137954,-7.769543,6.688950,-7.109415,0.795581,0.571167,9.849467,0.342111,3.584946,8.231096,2.964024,-3.226696,-9.304958,8.375067,-1.648639,-2.030942,6.547771,-0.016242,6.243393,-3.892461,5.621782,-0.590190,9.851296,-5.514006,-9.430136,4.817626,3.578477,-8.233757,0.768296,-5.044890,-7.264778,-4.688274,-2.120479,-0.536355,-5.346850,-9.180367,3.160511,-0.721381,-6.977137,4.150860,-4.583623,0.038543,4.539492,7.581545,5.012942,-6.123943,0.305344,3.242896,-7.271127,3.310054,3.426382,-6.107459,-9.933213,4.505727,4.295969,9.206917,9.749767,9.506623,-2.591410,9.833994,6.982504,1.625726,0.041624,-9.339150,7.202378,-1.662542,1.501291,8.475886,3.712108,2.070051,0.359179,4.523914,2.058421,1.374078,1.053133,2.453261,1.317868,4.632363,-9.638239,-6.000154,2.877208,-6.637624,9.506635,-6.561100,-1.150298,7.605970,5.226103,-0.641649,2.173301,-8.018103,7.121220,6.863813,4.973678,8.751712,-8.587244,1.823188,-7.080351,5.004090,2.330807,-2.753678,5.473222,0.216998,-1.270179,2.105690,-1.382838,3.144601,1.801490,-5.757161,1.507600,-4.749299,5.488768,-4.669151,5.180171,6.124835,2.139527,-2.747159,4.296795,0.148282,-6.675983,6.383373,9.350943,-4.374460,-7.476429,6.056280,-0.045706,5.979572,5.909880,0.647395,6.191755,4.157182,-4.029240,8.995443,2.884234,-8.523682,7.439765,-4.081341,-5.778968,-7.143115,3.108193,-4.620028,2.759234,6.190651,1.069881,-9.442529,4.615761,-4.964381,4.368729,1.280467,-6.167229,-8.439800,-7.001763,-9.955133,2.891364,4.861929,-2.592364,-4.067258,8.719887,-9.568774,-0.751186,-7.445234,-9.189670,-8.471027,-8.963795,8.910903,7.959403,5.113249,-4.384344,-3.531654,-6.585848,7.814634,5.044972,-3.942382,2.085341,-6.935064,8.749099,-8.080370,2.569267,-7.412170,-5.051729,-4.780013,5.772647,9.602448,-0.807223,-4.960213,4.429673,1.197587,2.486194,-0.718518,4.841908,6.260371,0.987345,-7.142255,-3.345957,-9.065291,-2.594230,-0.869078,-9.679732,-5.486922,0.059809,8.762730,-9.438152,5.277295,9.930573,-1.995973,-9.171115,2.318638,1.622882,-2.952303,-5.335230,7.540618,-6.041676,0.161109,5.698169,3.901260,-3.312958,-7.153173,3.482316,-6.117427,4.337995,8.348372,-0.418407,2.107915,4.268917,4.228806,-3.440134,-3.511680,-4.388195,-6.047872,0.871895,-9.534573,-5.087105,-6.258249,1.990785,-7.044522,-0.970382,-3.022411,5.908723,-8.179284,-6.922708,-4.661096,-2.732276,3.650530,-3.982300,2.415856,9.742240,3.507913,-1.619900,6.801177,0.524612,-3.028824,-5.046372,-8.534998,-7.108705,-6.017816,1.979909,5.779321,4.658279,-3.313402,-1.939036,-5.590462,-0.782004,-5.227962,1.142687,-1.477876,0.230540,-2.077397,2.610431,1.905871,-5.292564,-8.735586,1.938423,3.553671,-5.719347,-7.111663,9.311490,-3.455756,1.758864,-1.954883,9.025053,8.027429,4.042533,-7.776212,-3.342500,-9.844579,5.218507,-1.601456,0.667660,3.133192,-3.397994,-1.197088,-4.913447,8.259740,0.220785,8.168215,-2.583363,-2.580304,-5.995100,-5.007643,-0.517822,0.828747,-0.288365,-6.019197,-6.670070,0.158854,-2.977374,-5.553035,5.335656,-6.046948,-2.747941,6.855434,-6.132385,-7.252245,-7.950225,3.767713,-1.729423,-0.914378,2.620655,-8.576539,-5.624946,-1.397006,2.595880,-7.501838,-2.985784,-0.417678,-2.945762,5.946207,4.553997,1.329163,-1.847768,-6.942042,-6.087666,2.281524,-8.455481,4.417711,-5.748393,9.303245,-8.067540,-0.384649,-0.820197,5.000186,-6.138031,0.164508,8.059405,9.154488,9.159451,-0.187840,-2.396155,2.865043,7.559074,8.734415,-5.474266,3.818883,-8.050474,0.979887,-1.862122,5.365070,4.211992,-4.761907,-4.360252,7.894261,-0.519860,2.890607,7.305462,6.838620,8.937186,-0.181455,1.665382,-9.021200,0.139323,-0.742890,1.222735,-2.816377,-1.591297,3.025173,-7.828219,-6.686503,-8.097883,4.026934,7.466636,-8.445340,-9.775189,-9.511862,-6.485620,2.843544,1.172843,-4.892431,-3.229579,2.304585,8.048866,6.522740,2.740035,-8.826909,0.595758,-5.575129,-1.115863,6.886255,5.951600,-0.862247,-7.820067,-6.962869,3.735789,-0.070248,3.913956,-1.519226,-4.236173,8.883621,-5.013235,7.368436,4.530742,-6.889597,-6.813522,-6.687405,9.086930,-1.525526,3.052916,6.178275,7.838220,-8.016782,-1.939984,7.644600,-4.415798,-5.832978,8.135857,-2.555278,7.700806,-3.801070,-7.057443,-8.199146,-3.759774,9.966556,2.373540,-1.308419,3.981341,7.727903,-7.952629,-0.370860,1.524575,4.989468,8.328159,-9.925811,-2.673128,-7.554239,3.027245,-7.646260,0.523855,7.985402,2.747058,3.183343,-3.899212,-8.806606,-1.431404,6.381803,5.524920,-3.690168,-6.601063,-1.408844,8.181074,6.543906,7.051246,-5.663995,-6.047079,8.919533,-2.743224,-2.073934,9.582989,8.729130,6.436732,-2.688785,6.459215,1.702868,3.837281,-1.671344,2.950116,5.985321,1.918956,3.224348,-6.111379,4.313587,-5.433843,3.130841,-6.102723,4.124740,-1.540295,9.861951,-0.562803,2.426019,-1.254800,-2.608310,-4.992112,-7.460475,-2.882985,0.437852,-3.855746,3.724552,-9.913758,-8.248856,4.059041,-9.188878,5.602377,3.074351,6.777573,7.424335,-7.078601,7.620846,-1.366201,-8.516400,0.142688,6.393251,4.954325,-7.054551,5.959685,-0.151463,-1.809493,-4.742684,-7.217140,3.717434,9.774830,1.185420,2.436864,-6.792660,-4.715614,-3.875257,-7.151081,4.842721,-5.564374,9.056021,0.962387,-5.255896,-0.285968,1.543170,-6.655179,-8.786934,-2.579953,3.987013,-1.072576,0.580457,-8.082625,5.914851,8.269828,-2.910853,-7.574626,1.636196,-0.628165,-4.218109,9.178822,1.626308,-3.475552,5.663832,-6.521074,-1.401383,-0.762401,0.936980,5.447705,4.765878,-0.787979,-4.692371,6.849867,-3.461500,6.731379,-3.312100,-3.841043,-9.025685,-4.784542,5.818662,-5.535508,5.890594,7.029660,-0.027132,6.063195,3.001122,3.188730,3.972940,-8.305098,-3.163403,-7.340325,-6.255856,1.510128,8.996205,-7.349073,-6.038205,5.607284,3.248856,-9.146063,6.117951,7.091479,7.758866,6.899136,4.747643,-5.551546,3.914336,-1.788558,-5.090280,3.103875,3.770199,-4.043614,-6.519486,-4.783739,8.281119,4.086162,-7.377931,7.081131,-4.172726,-1.679912,-0.404081,4.675073,1.037634,5.630993,0.241953,-9.331125,-2.539701,-6.390338,-1.118840,-1.686513,-8.575709,-5.700738,-1.791359,-8.703671,-5.107677,-0.813671,-0.250237,9.655863,-7.474422,2.175691,4.965786,-3.740388,-5.121112,-8.573155,6.168519,-7.202932,2.880778,4.480796,5.213944,-2.806075,-9.834822,-6.514350,-9.408768,0.998949,9.062160,7.855907,-8.673003,-4.393870,-4.224325,9.250702,-6.497434,0.850606,-0.207875,5.580545,7.290116,-7.461321,6.664211,-8.402922,-3.936906,-8.439649,-7.056631,-9.984151,5.983398,0.905457,0.562219,-2.156121,0.384717,4.804322,-4.143940,3.810882,-9.989265,2.578896,-9.728764,-0.160616,9.274058,-2.360189,-2.574868,-3.820000,-5.225318,3.307434,-7.405456,4.698160,-5.425663,-3.023761,0.882867,-5.661851,6.375271,9.097335,2.547761,-2.588861,-4.491069,-3.860310,0.437335,6.217640,-1.007245,3.965738,-9.384204,-5.222189,-5.880741,8.667904,-6.965769,8.553910,7.699500,-1.747527,-0.201396,-3.060206,7.651920,6.741814,9.349251,-1.814439,-5.071583,0.990832,-5.229514,3.974177,-7.818282,6.134431,-2.762858,-1.544115,1.522574,-0.854482,3.242028,6.547215,9.575573,4.762532,1.499173,-9.390482,3.704325,-0.186990,-3.064251,-6.347245,-0.571195,3.718820,8.723118,-2.174485,-1.444750,-0.811931,7.996910,8.826481,5.102157,-6.676085,-1.745135,-8.986819,-0.284052,-8.187287,-5.591218,0.574218,-0.622373,9.531755,-1.899027,-6.063332,-4.071507,-2.956885,-3.301760,-7.231554,-4.002096,-6.607218,0.574989,-5.174887,8.683500,-7.349229,-5.823085,-5.670455,0.396069,-5.451245,-7.156865,-4.232474,2.294159,-1.608752,-5.755265,6.961574,7.749617,-1.453886,-5.474934,-7.704064,4.863211,0.787568,-5.656207,-6.056660,1.207621,9.158969,1.025888,-2.505935,-0.856384,4.746188,5.167426,4.846584,-6.684437,-6.601207,4.808105,4.214855,6.740859,-8.895588,-9.099049,5.065640,8.578549,8.553675,7.302895,5.732116,1.365542,-1.504035,-2.835384,0.576944,0.221301,1.186777,9.474995,1.374700,-1.303367,-9.923228,-6.798475,-1.092596,0.574870,5.498598,-1.377784,-0.621788,4.019203,-5.186082,0.254948,-0.128887,6.459398,4.795730,-0.350127,-5.838187,-8.774040,-1.578894,-6.047719,-7.496913,-8.295653,-0.202954,-9.264407,-8.589298,-0.273841,4.226011,2.438136,-4.454521,-1.826343,6.000975,1.424096,5.326654,-1.293413,-9.329611,-6.904844,-4.340001,-8.153318,3.814696,-6.057071,-9.565043,0.756249,-9.579026,-7.686780,6.645499,-2.118741,9.026170,-3.190774,3.388633,-4.511793,-6.017480,-9.323900,-4.642014,1.561329,4.253782,6.119858,-3.188722,-4.793189,0.373729,-6.810556,0.346104,1.147683,-0.522482,0.567285,5.167019,6.191938,-5.871725,-4.624170,2.676520,6.280743,0.406077,-3.133140,1.029129,-5.941487,6.962908,3.781947,6.157823,-4.634981,6.054478,4.420536,0.513883,-3.737163,-3.884167,-5.721836,-1.613182,2.912227,3.628160,-2.458089,-2.384657,5.697358,2.273278,-9.543073,-3.676058,-4.837964,-6.048211,-8.877367,-7.731450,8.034164,1.425724,-4.422957,5.358202,-6.651254,-8.170692,4.942801,2.852690,-4.456142,-9.722239,-8.180028,6.413497,-0.804622,-5.636234,-2.824133,3.027808,-5.132176,2.762855,-4.702435,-6.632335,8.083031,3.965372,0.736179,-0.805784,4.463250,-4.862599,5.142091,-3.991307,5.547663,-2.302270,-9.158320,2.380621,-4.671932,1.167077,-6.512683,7.085197,-0.742726,-7.900125,-4.604861,-3.218976,2.937959,6.706414,-8.319880,-8.758987,-1.356009,7.614842,-5.612453],[3.241176,-6.048222,-0.451068,-5.735810,-1.514715,-9.989446,-6.028030,6.435525,1.587863,0.872003,6.985979,-3.453017,6.256558,-8.584244,2.210438,-5.642689,-8.949136,-2.344874,2.034174,-7.272368,4.729405,-1.009686,6.978042,-1.736953,8.997038,4.413142,-6.318754,-8.248034,6.878502,-7.886345,-2.021040,3.695693,6.071479,2.726879,7.719200,1.992023,-2.409455,-9.485148,1.842441,-7.787479,5.709145,-1.522265,-2.686496,1.304438,4.444465,-1.332855,-0.652023,-1.073722,4.516513,-2.770402,-0.306499,-5.653708,-5.467371,-6.724309,8.213357,-0.197801,6.687082,-1.054503,7.730065,0.800937,-6.967591,-5.837207,4.137043,-3.170276,-2.645468,9.399036,-7.998155,-9.892411,8.305684,3.837164,1.236615,4.986354,-1.163161,-4.361583,6.990294,-7.507237,-6.706929,0.653784,-6.733655,-7.197147,-4.643728,1.498042,3.356055,0.101270,-8.152219,-5.874482,-0.019348,-4.942256,0.071914,1.337927,-8.609118,-0.749312,-2.368295,4.103836,-7.295067,-4.396971,8.588905,8.765391,1.486205,0.653484,3.392972,1.822025,3.294599,-5.272918,0.073838,-9.158022,-7.177790,-0.472523,-2.420418,4.287531,3.620095,9.723640,0.774803,-0.954953,-4.826980,-8.253307,9.091509,0.181837,-6.408206,7.466785,7.076954,6.419152,2.097641,5.295103,7.682125,-8.282661,-1.509710,-1.781796,-6.840812,-0.032379,-2.388178,5.747170,-8.226406,0.670999,-8.661007,-8.741762,-5.819487,6.934350,2.579370,3.210215,8.356802,-4.568409,1.342212,3.202255,9.509733,-0.016935,2.642141,2.199522,1.041851,-2.020763,5.262702,3.640690,-1.236259,4.522040,6.330115,5.911912,-0.977212,-3.096008,-1.454589,-8.201287,8.241007,4.324927,-3.449672,5.666558,5.068164,6.366316,-6.209447,-7.405379,-4.485778,7.118658,-5.262248,-6.607572,-9.364218,8.287880,6.273683,-8.506254,-3.903723,1.753908,-6.464912,-9.004305,-3.567670,-7.212947,5.696958,0.841406,5.204114,5.657195,1.377809,-2.597929,9.233325,-3.662043,0.041110,0.926550,0.255896,-6.466154,3.300208,1.018787,5.440636,0.156341,5.808179,-8.591795,6.025563,-8.606159,9.941101,-2.915870,-0.388854,8.435845,6.339244,-4.320232,3.518452,-7.432532,7.962418,-2.636668,4.364413,2.378018,4.951602,6.633997,-3.257295,1.009090,6.268922,-0.541429,3.142511,5.475983,-7.116943,3.701305,8.964203,4.857365,1.485807,3.097047,5.186549,3.501325,-8.471565,7.308542,6.175503,-5.898949,-3.321686,-1.064462,8.130191,-1.663157,9.897282,4.287705,8.254900,-6.008198,1.043572,0.594283,-2.157826,8.297075,-9.150175,0.302287,4.996325,-2.521157,-7.660379,7.947444,-3.542568,-9.136653,8.028717,-8.719666,-7.586534,-9.692758,-9.236334,-8.722029,-1.979947,3.921668,-4.577948,-6.314459,6.182258,5.558803,-6.402780,8.049777,-6.607154,-4.678941,6.485675,-7.762485,2.227168,1.233430,-8.538208,0.036636,4.321068,9.508786,6.608249,-1.900118,-2.151023,6.233075,-1.367559,-7.746382,-0.517313,5.523680,7.647263,9.725843,-2.354715,9.805364,-4.729401,7.815310,4.870048,6.224239,2.709061,0.579760,0.201539,-7.283156,3.192390,-9.549687,9.931059,-1.223417,2.616121,-3.500254,-2.825619,-5.523480,-4.617541,2.788257,5.424858,-3.688218,-7.107252,-3.077976,-6.118037,7.656420,8.909000,4.824354,5.018651,-1.011126,0.056283,-9.113292,-3.441807,-1.214415,4.359887,-9.789464,-3.929035,9.126227,9.623446,-8.358450,-5.166632,7.346431,3.108442,-1.010830,-3.813793,5.990308,6.294532,-1.448824,0.686990,-4.671841,-8.447723,8.889099,-4.157561,4.984389,-6.686675,3.969673,7.905388,9.842308,-0.249190,-4.348950,-7.391733,-9.785357,9.090921,4.363618,-6.829194,6.263272,-2.209203,2.057798,9.727209,-9.189199,9.129546,-9.676000,9.464964,9.824619,-9.040648,-5.391178,-5.434050,-5.746884,4.011812,-2.022523,-3.961043,-4.033233,-4.377126,1.011114,-5.601451,9.906785,6.506931,7.965298,1.834396,-9.440755,-8.725844,-3.472296,-1.309320,-0.665975,-1.663719,9.418962,6.354076,-2.995404,2.326265,2.276609,1.502303,3.630645,0.690782,9.048629,-1.011963,-7.549110,7.216243,3.144292,0.459379,3.735298,-9.660625,-2.345264,0.448793,8.600892,-6.054235,-9.391613,3.907564,0.822259,-5.840252,-8.329998,-0.901784,5.369143,4.341489,1.916435,7.646704,3.262231,7.902363,7.396824,-9.402977,-8.347063,7.181853,-5.059518,-8.140244,6.443326,6.951781,7.149269,-6.357330,7.671506,5.123197,4.939809,9.033377,-3.485925,-0.339600,4.914687,-2.167185,-7.861672,7.457444,0.305131,-3.232659,-0.128821,-4.601030,1.909879,6.920831,-4.660068,-0.012351,5.382775,-3.993610,-5.542841,3.986864,1.999435,3.978830,1.304743,3.945606,5.811054,-0.534207,0.102896,3.833644,1.638843,0.256620,-2.828228,1.434662,5.675474,0.678938,5.091718,-1.300530,1.072808,-5.523068,-8.427181,0.670805,3.850169,4.752157,-2.096224,2.896057,6.301063,4.440920,-3.642701,7.320844,4.416816,-3.376506,2.306277,3.263252,-9.808443,-5.147302,2.349916,-9.047638,5.413298,8.542260,1.616466,8.322654,7.150323,-9.246282,-8.251059,-2.930569,-3.202478,-7.069156,3.719537,-8.452955,4.642922,-9.128622,-9.798894,1.732559,-8.246187,8.482617,1.257978,2.813817,-7.969105,5.857154,8.548783,-9.522903,-1.227688,-6.246299,-9.359694,7.371851,4.658611,9.018487,5.319240,2.688761,3.921474,9.012933,9.834874,-1.777240,-0.963873,-9.812570,9.268124,1.904667,2.840464,9.642128,5.408405,8.005728,-6.013956,-4.076431,2.620783,1.186810,2.566115,-2.588554,4.488813,-7.414209,-8.024292,-2.226686,8.367561,3.937174,5.929367,-2.636744,5.518662,4.430292,-6.229895,0.692968,7.008477,6.046894,8.533598,5.814388,-6.767764,-8.517622,9.000445,-5.798186,8.252717,4.865364,-6.502900,0.286838,-7.173922,0.658883,-3.928507,-7.044844,3.369064,-4.915208,7.424886,-8.444402,1.899861,-4.402560,6.148107,5.359599,-0.724960,3.801825,0.292337,6.919111,1.990641,-2.994831,3.520871,3.699900,-7.181714,-4.721708,6.244458,4.616198,8.034207,5.339894,-7.773037,2.831305,-5.219263,7.554377,3.708121,5.961679,2.905275,8.634887,-2.391075,-0.416452,-8.993456,5.051483,6.698410,4.083434,-2.417755,0.905356,1.717964,-7.430745,8.257180,9.783999,-9.356302,6.263012,4.014414,-7.545527,0.416186,-9.619453,5.661026,7.377952,9.528043,-8.956564,-4.703826,-7.787638,-4.843451,1.943655,1.064627,7.615224,8.396657,3.149971,9.651109,-7.934823,-5.652992,-4.780086,-6.461239,-8.539340,-6.395266,-6.190458,-7.397990,6.071890,6.330604,-8.750034,5.522382,-0.135718,-5.762231,1.828594,9.885134,-3.640198,8.697427,-5.750236,2.516383,8.475183,6.371404,-8.366514,-1.109645,-9.550154,-0.631963,-2.993177,-5.960185,-2.143434,6.454844,-6.481024,9.093038,-9.774166,-0.167768,6.354430,-5.195722,5.754197,-7.230843,6.477006,9.551876,-1.195356,1.286300,-5.012270,1.951901,-7.066253,-8.043230,8.859925,-1.338429,-6.859735,-4.532611,-6.467757,-9.140630,-9.310015,8.379606,-0.309644,-3.697187,-6.143180,4.503873,6.699493,2.314717,6.649757,4.824295,5.236078,6.411397,-7.977521,3.586657,-3.876652,-5.895587,-6.503169,-0.850517,5.606781,8.566289,-6.290432,-7.026106,9.207528,-3.900451,5.233702,-1.664569,2.830154,7.948328,7.586923,-0.059746,-0.532913,7.652915,-0.810499,0.546044,-2.542610,2.984451,-5.268841,-7.634027,3.731210,-4.957718,-4.880889,1.855364,-0.119925,4.710098,-2.700671,1.334349,8.633271,5.106651,3.294191,0.213422,-2.512583,-3.605650,-1.837491,-3.615731,2.932178,-8.106141,7.082809,1.918472,-9.394122,-6.327395,-5.025871,-1.056568,-3.943186,2.622689,-4.287448,3.412456,8.476275,5.087432,-3.265906,4.336136,7.114443,-5.715440,-7.149479,-2.796596,-8.302662,1.794635,9.030098,-7.576307,9.424187,8.125773,-6.281689,-2.904232,-8.350808,5.315110,-0.036254,3.289481,7.807438,-3.964932,0.236297,-2.466993,2.589311,4.120746,1.286663,-3.452045,5.542740,7.452505,-3.074640,-2.724671,8.082368,-0.495271,-2.993553,8.710312,2.824782,4.376806,4.167292,-1.113839,7.039645,3.066284,-2.263990,-4.030693,2.741519,0.121665,5.221146,-0.413870,-3.507542,-6.660212,-5.542852,-6.496200,-7.927895,6.396843,0.955491,-6.906676,6.176062,-9.238352,-5.012354,0.862333,-5.346739,9.285034,-0.568069,-3.804531,-2.439152,-2.319264,6.089689,-3.216144,-7.393220,5.324901,-4.564241,7.953976,1.011214,0.245995,-6.992661,3.377803,3.401606,-4.504090,-2.065020,-8.203315,-7.288329,-9.436341,9.336610,4.891024,-4.874598,-6.262567,-4.673747,-3.044914,8.662728,2.330938,-1.377930,-4.066673,-9.048008,-4.724745,4.772446,8.091854,3.250695,9.516007,9.831068,-7.898191,1.583576,-3.583272,-6.107623,7.402803,-0.830023,7.915536,4.998886,-9.249247,1.282372,6.823691,-4.521107,-2.969706,-0.295566,-8.263446,-3.928110,8.028947,5.430175,7.775063,-4.026030,5.863685,-0.700487,2.930987,-3.483455,6.490413,-9.994363,7.005404,4.112491,-1.497612,4.157072,7.592189,-5.575370,-8.663503,-2.848329,4.075894,-2.807110,0.108442,-4.595546,3.896901,5.734956,-7.625411,9.670008,-8.919499,5.018415,-3.908036,1.212325,-1.490750,-0.264068,-9.148246,-5.718479,4.275950,-6.944801,8.310697,2.319438,-1.508766,1.733154,9.347301,-8.397719,-9.755854,-5.210490,-0.468311,-4.705560,5.737927,1.703077,-9.821281,-6.520849,0.538162,-1.912629,9.502250,2.721516,-0.252080,-6.294690,3.201208,3.046354,-1.144031,-9.679729,-4.443116,3.049997,8.439184,9.760995,-4.411607,3.310870,-4.933050,8.806920,8.633042,0.418507,6.781609,4.237818,-5.743524,-9.426784,1.499951,-3.062154,-6.486376,0.076526,-4.538450,5.332411,-2.022711,-7.149884,-2.266269,-0.485108,-5.700579,-9.024156,5.078360,-6.512109,-8.618752,-0.765062,4.588625,1.088685,-2.121828,2.088851,5.186258,-1.877674,4.599847,2.178766,-3.259963,-8.697416,5.271879,-2.347635,-8.367754,1.104171,-7.557862,-0.207936,-9.240917,5.971991,0.607698,3.626683,9.074680,-2.219993,4.221447,-8.553866,-6.940733,-7.207364,3.431255,-4.075127,-9.069206,1.897123,-1.813891,-6.196181,8.393431,9.478335,6.607758,-9.188663,-7.109140,5.265695,-7.425444,4.699730,-7.381424,-9.763143,1.438851,-8.996419,-3.835108,-8.385788,0.713804,2.275266,-9.675302,5.254513,-9.442255,-9.091610,2.077088,-5.520424,8.421095,-5.458939,9.651067,-2.723812,9.318324,-5.318445,-8.405998,-4.339824,-9.776989,-3.172084,5.441763,-8.474883,2.499458,-9.520447,-8.241564,-1.852207,6.914434,-3.574335,-8.918951,6.065765,8.640071,2.328910,-8.664521,9.081044,-8.853036,1.504112,-5.868869,8.201076,-3.599461,-0.265012,-5.298714,-3.773681,2.921748,-2.387860,8.289437,0.933993,-4.804489,-6.473669,6.426946,6.157767,-6.970275,1.419225,-4.612008,-5.168674,-7.790963,7.164149,-1.804031,-4.080264,-8.833973,2.082825,-5.101215,-0.623353,4.935239,1.146350,2.250213,-4.674195,6.376161,-9.230296,-1.332468,-5.391923,7.780019,1.645767,-4.639432,0.883985,8.140194,-7.615523,9.222856,-4.042402,-5.154964,4.712426,-0.282947,0.857664,1.963401,8.338439,-0.160272,6.989078,1.998585,8.879524,-9.758491,8.483295,9.000948,-4.254273,-5.641952,-8.195744,-2.174588,-1.528391,4.231354,9.130699,2.139669,9.071990,-1.897335,7.530430,6.541711,8.432753,0.666212,2.624854,8.375877,-9.975725,-7.551519,-8.309158,-4.189371,2.515994,-5.759242,2.709300,2.730276,9.964348,6.715949,-9.448088,-8.795148,-1.167527,-3.128130,-2.902328,9.834596,8.321784,4.069515,1.647185,4.940930,-3.028858,3.313799,3.590433,-8.797063,-2.604616,-3.388184,-5.305048,9.641364,-6.652053,8.684154,9.570813,3.312030,-9.066120,-5.408014,5.077808,1.520907,0.939169,9.209855,7.782527,0.625584,6.743864,-7.078059,-8.265329,-5.592450,4.412442,-1.368769,1.388067,-3.294281,-5.014611,4.009431,-8.005087,3.793872,2.626005,-3.968116,-4.672328,-8.685174,0.940637,-8.070250,-1.256785,9.578450,-2.240502,-0.394228,7.393124,5.172217,9.116295,4.171673,9.499021,5.210952,8.449246,-9.905924,-8.132799,1.141103,6.456737,6.758082,5.865981,-0.302863,-1.717564,2.737066,7.150615,-9.496898,9.214193,-4.180926,-2.322457,4.084092,5.426679,-1.128876,-3.691390,-9.906798,3.073649,-5.745561,-7.532938,-9.030069,5.837920,-2.491974,-9.755078,-9.502317,9.419790,0.152647,-2.109771,9.130763,-1.763314,9.218434,-8.725671,-9.675213,-6.668550,-3.979576,8.271010,1.008716,-0.274975,3.035120,-6.769074,-5.503784,-1.637332,-1.229698,-2.552531,0.916170,2.909455,5.678151,-3.962625,8.052938,-4.367741,9.633196,-5.758408,9.426906,-1.126862,9.010146,-2.528463,-5.083527,7.932170,4.588194,6.408305,-5.231263,-4.340798,-2.576044,-8.858450,8.605477,8.299127,-5.634850,4.569025,-9.275075,0.250868,3.175015,6.981998,-3.686261,-7.642967,-9.235096,-5.849201,-7.263154,-9.634763,9.323085,-9.425829,-3.769570,2.570569,0.923343,-0.930000,2.541213,5.779403,1.401283,-2.713145,-0.908244,4.943715,-4.949123,1.939799,-9.173561,6.009767,-9.380316,-1.579244,1.980486,-5.592711,5.058170,-1.508545,-5.633495,5.838723,-9.776824,8.949306,-5.685477,7.052306,7.733782,4.567050,8.968025,9.815902,-8.491307,-6.470648,-3.088038,-8.886783,2.241581,-7.222263,-4.229218,9.018184,2.957033,2.601761,2.891140,4.457708,-3.528322,9.519505,2.325430,0.950916,-2.526264,-3.589595,-1.451875,-4.873345,7.770733,7.276562,-5.648902,6.922946,-6.416369,0.268648,1.602021,-5.490433,0.738972,6.733650,-8.912711,-2.071914,-9.480733,8.474293,7.580845,-7.926010,-1.373341,7.012944,-2.729285,2.338862,7.248809,0.973763,5.240892,-8.347106,1.918069,8.788808,0.672766,-3.208936,-3.431244,-5.017897,-6.707120,6.464641,1.007451,7.173551,7.495878,-7.354701,-2.697092,5.523281,2.235160,-3.056465,-9.992532,-6.114878,-7.292387,4.663533,9.759513,-6.184366,0.402433,-7.814381,-7.111392,-9.681186,-8.518308,4.072137,-4.760525]], dtype = "float64")#candidate|5288|(5, 1350)|const|float64
bop_5289 = relay.not_equal(var_5279.astype('bool'), const_5288.astype('bool')) # shape=(5, 1350)
func_4513_call = mod.get_global_var('func_4513')
func_4516_call = mutated_mod.get_global_var('func_4516')
var_5294 = relay.var("var_5294", dtype = "uint16", shape = (2100,))#candidate|5294|(2100,)|var|uint16
call_5293 = relay.TupleGetItem(func_4513_call(relay.reshape(var_5294.astype('uint16'), [10, 15, 14]), relay.reshape(var_5294.astype('uint16'), [10, 15, 14]), ), 0)
call_5295 = relay.TupleGetItem(func_4516_call(relay.reshape(var_5294.astype('uint16'), [10, 15, 14]), relay.reshape(var_5294.astype('uint16'), [10, 15, 14]), ), 0)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_5310 = relay.TupleGetItem(func_2326_call(relay.reshape(call_5269.astype('float64'), [14, 3, 15])), 0)
call_5311 = relay.TupleGetItem(func_2328_call(relay.reshape(call_5269.astype('float64'), [14, 3, 15])), 0)
bop_5317 = relay.equal(const_5288.astype('bool'), var_5279.astype('bool')) # shape=(5, 1350)
bop_5321 = relay.minimum(bop_5317.astype('float32'), var_5279.astype('float32')) # shape=(5, 1350)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
call_5334 = relay.TupleGetItem(func_2326_call(relay.reshape(call_5310.astype('float64'), [14, 3, 15])), 0)
call_5335 = relay.TupleGetItem(func_2328_call(relay.reshape(call_5310.astype('float64'), [14, 3, 15])), 0)
bop_5336 = relay.divide(const_5288.astype('float32'), var_5279.astype('float32')) # shape=(5, 1350)
output = relay.Tuple([call_5269,call_5276,call_5278,bop_5289,call_5293,var_5294,call_5310,bop_5321,call_5334,bop_5336,])
output2 = relay.Tuple([call_5270,call_5277,call_5280,bop_5289,call_5295,var_5294,call_5311,bop_5321,call_5335,bop_5336,])
func_5339 = relay.Function([var_5279,var_5294,], output)
mod['func_5339'] = func_5339
mod = relay.transform.InferType()(mod)
var_5340 = relay.var("var_5340", dtype = "float64", shape = (1, 1350))#candidate|5340|(1, 1350)|var|float64
var_5341 = relay.var("var_5341", dtype = "uint16", shape = (2100,))#candidate|5341|(2100,)|var|uint16
output = func_5339(var_5340,var_5341,)
func_5342 = relay.Function([var_5340,var_5341,], output)
mutated_mod['func_5342'] = func_5342
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_5356 = relay.TupleGetItem(func_2351_call(), 0)
call_5357 = relay.TupleGetItem(func_2352_call(), 0)
func_2142_call = mod.get_global_var('func_2142')
func_2144_call = mutated_mod.get_global_var('func_2144')
var_5364 = relay.var("var_5364", dtype = "float64", shape = (396,))#candidate|5364|(396,)|var|float64
call_5363 = relay.TupleGetItem(func_2142_call(relay.reshape(var_5364.astype('float64'), [396,])), 1)
call_5365 = relay.TupleGetItem(func_2144_call(relay.reshape(var_5364.astype('float64'), [396,])), 1)
func_2588_call = mod.get_global_var('func_2588')
func_2593_call = mutated_mod.get_global_var('func_2593')
const_5379 = relay.const([-7,5,-4,-7,2,-5,-3,-7,-3,-3,-7,8,8,8,7,3,6,7,2,-9,4,-1,8,5,-1,4,7,-1,7,5,5,-9,8,2,-10,4,5,-2,3,4,-6,-3,-4,10,-4,-7,-4,1,-2,4,2,-7,3,-9,7,-2,6,7,-10,1,-3,4,-7,-1,-7,-3,3,7,-1,2,-2,4,10,7,-10,5,-9,1,3,4,-5,1,7,3,6,8,2,5,-3,3,3,7,8,-5,-9,2,-6,-3,-3,-2,2,7,4,-7,4,-2,-9,-6,-8,1,-2,1,-8,-2,1,-9,6,8,-8,8,-6,-9,-1,3,10,5,8,7,-2,-8,2,5,-5,-9,9,-7,10,-1,2,8,-9,3,1,-3,10,-8,-1,2,8,-1,1,-2,-5,-9,7,1,4,-3,-4,10,2,-6,-10,10,-10,-5,-10,-9,1,2,-9,6,-6,10,7,-4,7,3,8,5,6,-8,-10,9,-9,9,-3,1,4,-9,-1,-4,-3,-6,-10,-9,-3,-1,4,-2,1,10,6,3,-3,5,-5,2,5,7,9,10,-2,4,-10,-10,-10,7,2,-10,-2,10,-3,5,8,-3,-9,8,-5,9,9,-8,-10,6,5,-10,10,-6,10,-3,5,-7,9,8,-10,-9,8,9,-2,-1,-1,-6,9,-6,-5,-1,-4,-7,-6,9,3,4,-5,9,-7,4,1,9,-4,-3,3,-1,2,2,-4,3,-10,9,7,-5,-10,2,-1,-3,5,3,-2,7,-2,-4,-1,-4,-2,-6,-10,-3,10,-4,-6,7,5,-9,6,-10,6,-7,-9,-8,3,-1,-7,-5,-10,9,6,-7,-7,5,-4,-2,-9,9,-9,10,-3,6,5,-6,-10,3,2,-6,-8,-10,10,-3,2,-8,9,4,-8,1,-4,10,-5,-2,3,-3,3,-3,9,1,-8,-4,-6,10,-1,-9,9,8,10,-10,-10,-4,-8,5,3,-1,-4,9,-5,3,-1,10,-2,3,-2,7,-5,4,-5,5,4,8,-2,7,-7,3,5,-7,6,10,-2,2,7,-5,5,-2,-5,-7,9,-2,4,-4,3,-7,1,8,6,5,6,-10,7,3,6,8,-4,4,8,-9,9,-1,-7,6,-1,-1,-10,-1,4,-8,2,6,6,5,7,-6,-4,-7,-10,-6,-3,-7,7,9,-1,-2,4,-10,9,6,-1,-2,-3,-8,3,1,9,10,-7,-9,-7,1,8,-4,7,3,-4,7,-6,-10,6,-7,-1,-3,6,-9,3,-4,3,10,-10,10,-9,-1,9,-8,-3,2,-1,-6,-6,-10,7,2,4,10,6,-7,-6,-2,10,-1,-4,-8,-1,4,9,8,9,-6,1,-8,7,-2,4,9,3,-8,7,3,-10,5,2,5,-3,-6,-8,-1,-2,7,8,-1,-8,-9,-2,-10,1,2,-9,5,-10,6,7,-3,2,-4,-6,3,-3,8,7,8,5,1,6,8,9,4,-3,5,-6,6,-6,-5,-1,4,1,8,-1,2,7,5,-3,-1,7,4,9,-3,-8,3,1,1,-9,-10,8,-10,-1,10,-6,-2,1,4,5,4,-10,-7,4,5,-5,-4,6,-9,-10,2,-1,1,-2,3,-6,3,4,7,7,1,-6,6,-2,-2,3,-10,-10,-10,8,10], dtype = "uint8")#candidate|5379|(624,)|const|uint8
var_5380 = relay.var("var_5380", dtype = "float32", shape = (280,))#candidate|5380|(280,)|var|float32
call_5378 = relay.TupleGetItem(func_2588_call(relay.reshape(const_5379.astype('uint8'), [13, 16, 3]), relay.reshape(const_5379.astype('uint8'), [13, 16, 3]), relay.reshape(var_5380.astype('float32'), [280,]), relay.reshape(var_5364.astype('float64'), [396, 1]), ), 2)
call_5381 = relay.TupleGetItem(func_2593_call(relay.reshape(const_5379.astype('uint8'), [13, 16, 3]), relay.reshape(const_5379.astype('uint8'), [13, 16, 3]), relay.reshape(var_5380.astype('float32'), [280,]), relay.reshape(var_5364.astype('float64'), [396, 1]), ), 2)
output = relay.Tuple([call_5356,call_5363,var_5364,call_5378,const_5379,var_5380,])
output2 = relay.Tuple([call_5357,call_5365,var_5364,call_5381,const_5379,var_5380,])
func_5407 = relay.Function([var_5364,var_5380,], output)
mod['func_5407'] = func_5407
mod = relay.transform.InferType()(mod)
mutated_mod['func_5407'] = func_5407
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5407_call = mutated_mod.get_global_var('func_5407')
var_5409 = relay.var("var_5409", dtype = "float64", shape = (396,))#candidate|5409|(396,)|var|float64
var_5410 = relay.var("var_5410", dtype = "float32", shape = (280,))#candidate|5410|(280,)|var|float32
call_5408 = func_5407_call(var_5409,var_5410,)
output = call_5408
func_5411 = relay.Function([var_5409,var_5410,], output)
mutated_mod['func_5411'] = func_5411
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1611_call = mod.get_global_var('func_1611')
func_1612_call = mutated_mod.get_global_var('func_1612')
call_5460 = relay.TupleGetItem(func_1611_call(), 0)
call_5461 = relay.TupleGetItem(func_1612_call(), 0)
func_1463_call = mod.get_global_var('func_1463')
func_1465_call = mutated_mod.get_global_var('func_1465')
var_5477 = relay.var("var_5477", dtype = "float64", shape = (396,))#candidate|5477|(396,)|var|float64
call_5476 = func_1463_call(relay.reshape(var_5477.astype('float64'), [6, 11, 6]))
call_5478 = func_1463_call(relay.reshape(var_5477.astype('float64'), [6, 11, 6]))
output = relay.Tuple([call_5460,call_5476,var_5477,])
output2 = relay.Tuple([call_5461,call_5478,var_5477,])
func_5482 = relay.Function([var_5477,], output)
mod['func_5482'] = func_5482
mod = relay.transform.InferType()(mod)
var_5483 = relay.var("var_5483", dtype = "float64", shape = (396,))#candidate|5483|(396,)|var|float64
output = func_5482(var_5483)
func_5484 = relay.Function([var_5483], output)
mutated_mod['func_5484'] = func_5484
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_5496 = func_2034_call()
call_5497 = func_2034_call()
output = relay.Tuple([call_5496,])
output2 = relay.Tuple([call_5497,])
func_5507 = relay.Function([], output)
mod['func_5507'] = func_5507
mod = relay.transform.InferType()(mod)
mutated_mod['func_5507'] = func_5507
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5507_call = mutated_mod.get_global_var('func_5507')
call_5508 = func_5507_call()
output = call_5508
func_5509 = relay.Function([], output)
mutated_mod['func_5509'] = func_5509
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4858_call = mod.get_global_var('func_4858')
func_4859_call = mutated_mod.get_global_var('func_4859')
call_5523 = relay.TupleGetItem(func_4858_call(), 0)
call_5524 = relay.TupleGetItem(func_4859_call(), 0)
func_3986_call = mod.get_global_var('func_3986')
func_3990_call = mutated_mod.get_global_var('func_3990')
const_5527 = relay.const([True,False,False,False,True,True,True,False,True,True,False,True,True,True,True,False,True,True,False,False,False,True,False,True,True,False,True,False,False,True,False,True,True,False,False,True,True,True,True,False,False,True,True,True,False,True,False,False,False,False,False,True,False,False,False,True,True,True,True,True,False,True,True,True,True,True,False,True,False,True,True,False,True,True,False,True,False,False,True,False,False,True,True,False,False,True,True,True,False,False,False,False,True,True,False,True,False,False,False,False,False,True,True,True,False,True,False,False,True,False,True,True,True,False,False,True,False,True,False,False,False,True,True,True,False,True,False,True,True,False,True,True,False,False,False,False,True,True,True,False,True,False,False,False,False,False,False,False,True,False,True,True,True,False,True,False,True,True,True,False,False,False,False,False,True,False,False,False,True,True,True,False,True,True,True,False,True,True,False,False,True,True,False,True,True,True,True,False,False,False,True,False,False,True,False,True,True,True,False,True,False,True,True,False,False,False,False,True,True,False,True,True,False,True,False,True,False,True,False,True,True,True,True,True,False,False,True,True,True,True,False,True,False,False,True,False,False,True,True,False,False,False,True,False,False,True,True,False,False,True,True,True,False,True,False,False,True,True,False,False,False,False,True,False,False,True,False,True,False,True,True,False,False,False,False,False,True,False,False,True,True,False,False,False,True,False,False,False,False,False,False,False,True,True,True,True,False,True,False,True,True,True,True,True,True,False,True,False,False,True,True,True,True,True,True,False,False,False,False,False,False,False,False,True,False,True,True,False,True,True,True,False,True,True,True,False,True,False,True,True,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,True,True,True,False,False,True,True,True,False,False,False,False,True,True,True,True,False,False,True,False,False,True,False,False,True,False,False,False,False,True,False,True,False,True,False,False,False,True,False,False,True,False,False,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,True,False,False,True,True,False,False,True,False,False,True,True,False,True,False,False,True,False,False,True,True,False,True,False,False,True,True,True,True,True,False,True,False,False,False,True,True,False,True,True,False,False,False,True,False,False,True,True,False,False,False,False,False,True,False,True,False,True,False,True,True,False,False,True,False,True,False,True,True,True,False,False,False,True,True,False,True,False,True,False,False,True,False,True,False,False,False,False,False,False,True,True,False,False,False,False,True,False,False,False,False,False,False,False,True,True,False,True], dtype = "bool")#candidate|5527|(525,)|const|bool
const_5528 = relay.const([-9.845208,2.496724,6.028298,-6.088678,-6.352628,0.732825,-9.904954,-2.974694,7.553236,-7.667900,-3.813594,-9.244795,1.490582,-2.242981,-1.511003,9.716159,9.285759,0.645141,-8.268697,6.014939,-7.534066,-3.350702,3.115899,-1.035792,-6.565057,3.410732,-0.301363,-2.119967,-2.632655,-2.333690,3.489814,7.824368,-4.165823,6.480831,-5.723457,-4.108929,7.589233,4.262955,2.266916,6.289338,0.125582,2.873382,-1.574658,1.901769,-6.674470,-3.144882,-7.257853,-7.783602,-6.461352,0.109222,-9.055820,8.400294,-7.185657,3.234136,8.740384,3.656313,0.027237,-3.592655,-7.734344,-3.524811,3.316449,-9.863114,-0.725951,-3.879509,-1.504097,0.906274,8.070297,-6.548405,4.381796,-0.218114,-9.284436,4.736894,-9.129088,5.445931,-4.185472,1.060009,-2.742607,5.805624,2.336994,-9.918978,1.039112,-8.088370,-2.184117,-0.769418,-8.109541,-6.967205,-6.924087,-9.246801,5.401416,9.897310,1.679385,5.009453,-4.404963,-3.373135,3.309255,0.676932,-3.527786,2.270574,-9.585579,2.145757,-3.497142,1.626716,7.106042,6.567648,4.862772,-4.439835,-2.098637,3.842005,-0.045304,-5.561829,-2.313568,-2.606616,4.900887,7.174259,8.054968,0.490448,1.411398,-0.545518,-9.222184,4.603474,-2.848140,9.065046,-8.714361,3.057578,-4.378237,-4.486255,9.516925,-5.112376,-6.546784,-3.146147,-9.862755,-0.164437,-4.163242,-3.652349,-1.755253,1.039531,-1.125995,2.061252,9.591120,1.506758,-8.329062,-7.086225,6.435145,0.555715,-8.632266,1.780322,1.650615,-5.078789,5.341306,-0.234923,2.586680,-5.955407,-6.251690,-8.864105,6.325218,-9.470076,4.576180,8.872050,6.068399,-9.780880,8.684416,-9.194103,0.666569,-3.665228,9.307370,3.408590,-1.620614,-6.419143,2.006399,-1.779567,1.715807,0.672012,8.340506,9.978723,9.976421,8.117685,4.854708,8.399258,-8.217616,2.145480,-5.575318,-2.001529,6.508613,-2.191212,9.876327,2.684343,9.735797,4.835772,3.012852,7.353274,5.177471,5.645653,-1.507554,3.082804,8.889435,-8.014032,0.319078,-6.448338,-6.429906,-8.997510,-4.326020,-4.282761,-0.986682,-4.231741,-4.360099,-1.396161,-8.469681,-4.951532,-1.152254,-3.580603,1.373803,2.134286,9.162310,7.785542,-9.919558,-8.068691,2.526662,-0.814429,-0.677716,3.736255,-3.243635,-6.495351,-3.358313,5.263923,3.563462,-8.359704,8.577734,0.560342,4.009677,-3.027134,-7.968978,-8.976764,0.350463,5.836668,-5.357815,-4.551725,-0.044237,4.458530,8.079668,4.560302,-8.499907,5.516477,-2.828843,6.368582,9.965054,6.360192,-2.487875,1.558123,4.294359,2.586188,-8.157834,-5.765929,3.790585,3.444186,8.353641,5.188917,-5.865759,1.319873,5.821749,-3.319504,-9.424713,1.455994,-4.498877,-9.303814,2.133687,5.626465,2.500227,6.182049,5.332461,0.790381,3.745389,5.242917,-9.281097,-7.024572,7.987925,-6.109002,3.482009,-7.833248,9.546930,4.131447,-1.352230,-0.516219,-4.490061,-0.989618,-9.156928,-6.197787,-0.950567,4.108281,-5.198035,1.579752,-3.073419,5.915748,5.452917,9.222206,-8.228735,7.713562,4.631417,-0.043914,8.311134,-3.203435,5.536207,-3.486748,-2.403250,-4.261692,2.442432,-1.369933,8.767827,3.814786,8.724967,0.783829,0.683172,-6.296116,-4.737254,2.706447,-0.580980,0.841000,-9.465274,5.786550,2.896775,-1.581228,4.731448,6.566124,-9.971380,0.485447,6.594600,-2.114109,-1.642755,-3.237449,1.517502,-3.540464,2.799927,8.349819,2.200790,-1.245034,-4.419801,-3.170121,6.581146,0.375198,-8.919422,9.885163,9.592866,9.996885,-0.652573,1.354495,0.283058,4.159124,2.018668,-3.086144,-5.360146,-5.129872,8.672100,-5.273024,-0.499307,2.713633,7.399720,-3.034377,-7.824878,-0.404732,6.861114,-9.645596,0.160792,4.421474,5.628561,-7.393986,-4.073700,-9.634660,7.187752,-9.164675,-8.977127,-6.129419,-1.863639,2.671422,-5.165399,-2.346752,9.284267,-8.279832,-3.041417,6.925685,-8.155197,3.821313,-3.262813,-4.570981,3.770687,1.138128,-8.095493,1.119175,5.374555,0.943949,-0.353769,3.609262,8.324078,-9.941002,-6.267319,3.189297,3.218890,2.579946], dtype = "float64")#candidate|5528|(396,)|const|float64
call_5526 = relay.TupleGetItem(func_3986_call(relay.reshape(const_5527.astype('bool'), [525,]), relay.reshape(const_5528.astype('float64'), [396,]), ), 2)
call_5529 = relay.TupleGetItem(func_3990_call(relay.reshape(const_5527.astype('bool'), [525,]), relay.reshape(const_5528.astype('float64'), [396,]), ), 2)
func_5078_call = mod.get_global_var('func_5078')
func_5081_call = mutated_mod.get_global_var('func_5081')
var_5536 = relay.var("var_5536", dtype = "float64", shape = (27, 50))#candidate|5536|(27, 50)|var|float64
call_5535 = relay.TupleGetItem(func_5078_call(relay.reshape(var_5536.astype('float64'), [6, 15, 15]), relay.reshape(var_5536.astype('float64'), [6, 15, 15]), ), 3)
call_5537 = relay.TupleGetItem(func_5081_call(relay.reshape(var_5536.astype('float64'), [6, 15, 15]), relay.reshape(var_5536.astype('float64'), [6, 15, 15]), ), 3)
var_5543 = relay.var("var_5543", dtype = "float64", shape = (27, 50))#candidate|5543|(27, 50)|var|float64
bop_5544 = relay.bitwise_or(var_5536.astype('uint32'), relay.reshape(var_5543.astype('uint32'), relay.shape_of(var_5536))) # shape=(27, 50)
output = relay.Tuple([call_5523,call_5526,const_5527,const_5528,call_5535,bop_5544,])
output2 = relay.Tuple([call_5524,call_5529,const_5527,const_5528,call_5537,bop_5544,])
func_5547 = relay.Function([var_5536,var_5543,], output)
mod['func_5547'] = func_5547
mod = relay.transform.InferType()(mod)
var_5548 = relay.var("var_5548", dtype = "float64", shape = (27, 50))#candidate|5548|(27, 50)|var|float64
var_5549 = relay.var("var_5549", dtype = "float64", shape = (27, 50))#candidate|5549|(27, 50)|var|float64
output = func_5547(var_5548,var_5549,)
func_5550 = relay.Function([var_5548,var_5549,], output)
mutated_mod['func_5550'] = func_5550
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5158_call = mod.get_global_var('func_5158')
func_5159_call = mutated_mod.get_global_var('func_5159')
call_5560 = relay.TupleGetItem(func_5158_call(), 0)
call_5561 = relay.TupleGetItem(func_5159_call(), 0)
output = call_5560
output2 = call_5561
func_5569 = relay.Function([], output)
mod['func_5569'] = func_5569
mod = relay.transform.InferType()(mod)
mutated_mod['func_5569'] = func_5569
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5569_call = mutated_mod.get_global_var('func_5569')
call_5570 = func_5569_call()
output = call_5570
func_5571 = relay.Function([], output)
mutated_mod['func_5571'] = func_5571
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_5605 = func_2034_call()
call_5606 = func_2034_call()
output = call_5605
output2 = call_5606
func_5610 = relay.Function([], output)
mod['func_5610'] = func_5610
mod = relay.transform.InferType()(mod)
output = func_5610()
func_5611 = relay.Function([], output)
mutated_mod['func_5611'] = func_5611
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5689 = relay.var("var_5689", dtype = "float64", shape = (3, 10, 15))#candidate|5689|(3, 10, 15)|var|float64
uop_5690 = relay.cosh(var_5689.astype('float64')) # shape=(3, 10, 15)
func_3149_call = mod.get_global_var('func_3149')
func_3153_call = mutated_mod.get_global_var('func_3153')
var_5693 = relay.var("var_5693", dtype = "float32", shape = (140, 2))#candidate|5693|(140, 2)|var|float32
var_5694 = relay.var("var_5694", dtype = "uint8", shape = (168,))#candidate|5694|(168,)|var|uint8
var_5695 = relay.var("var_5695", dtype = "float32", shape = ())#candidate|5695|()|var|float32
call_5692 = relay.TupleGetItem(func_3149_call(relay.reshape(var_5693.astype('float32'), [70, 4]), relay.reshape(var_5694.astype('uint8'), [168,]), relay.reshape(var_5695.astype('float32'), []), ), 7)
call_5696 = relay.TupleGetItem(func_3153_call(relay.reshape(var_5693.astype('float32'), [70, 4]), relay.reshape(var_5694.astype('uint8'), [168,]), relay.reshape(var_5695.astype('float32'), []), ), 7)
bop_5700 = relay.logical_and(uop_5690.astype('bool'), relay.reshape(var_5689.astype('bool'), relay.shape_of(uop_5690))) # shape=(3, 10, 15)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_5706 = func_2034_call()
call_5707 = func_2034_call()
output = relay.Tuple([call_5692,var_5693,var_5694,var_5695,bop_5700,call_5706,])
output2 = relay.Tuple([call_5696,var_5693,var_5694,var_5695,bop_5700,call_5707,])
func_5709 = relay.Function([var_5689,var_5693,var_5694,var_5695,], output)
mod['func_5709'] = func_5709
mod = relay.transform.InferType()(mod)
mutated_mod['func_5709'] = func_5709
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5709_call = mutated_mod.get_global_var('func_5709')
var_5711 = relay.var("var_5711", dtype = "float64", shape = (3, 10, 15))#candidate|5711|(3, 10, 15)|var|float64
var_5712 = relay.var("var_5712", dtype = "float32", shape = (140, 2))#candidate|5712|(140, 2)|var|float32
var_5713 = relay.var("var_5713", dtype = "uint8", shape = (168,))#candidate|5713|(168,)|var|uint8
var_5714 = relay.var("var_5714", dtype = "float32", shape = ())#candidate|5714|()|var|float32
call_5710 = func_5709_call(var_5711,var_5712,var_5713,var_5714,)
output = call_5710
func_5715 = relay.Function([var_5711,var_5712,var_5713,var_5714,], output)
mutated_mod['func_5715'] = func_5715
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2965_call = mod.get_global_var('func_2965')
func_2967_call = mutated_mod.get_global_var('func_2967')
call_5730 = func_2965_call()
call_5731 = func_2965_call()
output = relay.Tuple([call_5730,])
output2 = relay.Tuple([call_5731,])
func_5744 = relay.Function([], output)
mod['func_5744'] = func_5744
mod = relay.transform.InferType()(mod)
mutated_mod['func_5744'] = func_5744
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5744_call = mutated_mod.get_global_var('func_5744')
call_5745 = func_5744_call()
output = call_5745
func_5746 = relay.Function([], output)
mutated_mod['func_5746'] = func_5746
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3440_call = mod.get_global_var('func_3440')
func_3441_call = mutated_mod.get_global_var('func_3441')
call_5758 = func_3440_call()
call_5759 = func_3440_call()
uop_5770 = relay.cosh(call_5758.astype('float32')) # shape=(11, 12, 16)
uop_5772 = relay.cosh(call_5759.astype('float32')) # shape=(11, 12, 16)
output = relay.Tuple([uop_5770,])
output2 = relay.Tuple([uop_5772,])
func_5777 = relay.Function([], output)
mod['func_5777'] = func_5777
mod = relay.transform.InferType()(mod)
mutated_mod['func_5777'] = func_5777
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5777_call = mutated_mod.get_global_var('func_5777')
call_5778 = func_5777_call()
output = call_5778
func_5779 = relay.Function([], output)
mutated_mod['func_5779'] = func_5779
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3440_call = mod.get_global_var('func_3440')
func_3441_call = mutated_mod.get_global_var('func_3441')
call_5783 = func_3440_call()
call_5784 = func_3440_call()
func_3149_call = mod.get_global_var('func_3149')
func_3153_call = mutated_mod.get_global_var('func_3153')
var_5788 = relay.var("var_5788", dtype = "float32", shape = (1, 280))#candidate|5788|(1, 280)|var|float32
var_5789 = relay.var("var_5789", dtype = "uint8", shape = (168,))#candidate|5789|(168,)|var|uint8
const_5790 = relay.const(-5.340461, dtype = "float32")#candidate|5790|()|const|float32
call_5787 = relay.TupleGetItem(func_3149_call(relay.reshape(var_5788.astype('float32'), [70, 4]), relay.reshape(var_5789.astype('uint8'), [168,]), relay.reshape(const_5790.astype('float32'), []), ), 5)
call_5791 = relay.TupleGetItem(func_3153_call(relay.reshape(var_5788.astype('float32'), [70, 4]), relay.reshape(var_5789.astype('uint8'), [168,]), relay.reshape(const_5790.astype('float32'), []), ), 5)
output = relay.Tuple([call_5783,call_5787,var_5788,var_5789,const_5790,])
output2 = relay.Tuple([call_5784,call_5791,var_5788,var_5789,const_5790,])
func_5795 = relay.Function([var_5788,var_5789,], output)
mod['func_5795'] = func_5795
mod = relay.transform.InferType()(mod)
var_5796 = relay.var("var_5796", dtype = "float32", shape = (1, 280))#candidate|5796|(1, 280)|var|float32
var_5797 = relay.var("var_5797", dtype = "uint8", shape = (168,))#candidate|5797|(168,)|var|uint8
output = func_5795(var_5796,var_5797,)
func_5798 = relay.Function([var_5796,var_5797,], output)
mutated_mod['func_5798'] = func_5798
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5808 = relay.var("var_5808", dtype = "float64", shape = ())#candidate|5808|()|var|float64
const_5809 = relay.const([[[3.678195,5.594482,0.817118,6.357030,4.273458,5.883504],[-1.627418,-2.640995,-7.513041,-4.903787,-8.614599,8.751116],[-9.052245,-9.218047,0.507090,4.791419,-8.334393,8.751443],[-2.709233,-9.834074,1.576001,0.956034,-0.568319,6.195500],[3.151550,7.720652,4.397053,-5.153786,2.718101,-2.589502],[-1.866268,3.512148,8.812184,2.285873,8.842434,8.077173],[9.494495,-0.450324,-1.639240,-3.364895,0.154183,-6.135108],[-9.803575,9.158729,1.696193,-9.713669,4.543036,-8.564873],[-6.399795,-7.393642,2.124412,0.905867,-9.572589,2.262301],[2.432350,1.833291,0.801580,0.435139,-7.321596,0.378887],[6.042487,-4.554840,9.098847,8.415789,-4.527549,6.573872],[3.036541,-6.542434,-4.741507,1.848952,-6.379000,2.291085],[-4.579197,3.996063,4.463191,-2.383915,1.344195,6.173435],[3.828730,-5.140046,3.111225,-0.233915,-4.696151,-7.980996]],[[-5.042014,8.883307,-0.578894,-9.932070,1.351738,-6.122640],[4.608831,3.573582,0.231375,1.289723,4.324102,-9.004176],[-5.719589,-1.769852,7.235476,9.330756,-3.853706,-2.741653],[2.780621,9.461346,0.337086,7.089546,-9.650914,9.905567],[-7.389191,-9.735248,-4.461649,-3.164617,1.788354,-4.179647],[8.528685,-7.873530,-9.785080,8.719440,-4.568786,-1.506630],[-1.946980,-0.331116,3.192660,-8.834801,-3.647552,4.948552],[1.809254,7.206740,-5.704231,8.724203,-5.175146,0.921566],[0.302281,-2.118174,6.291106,0.696145,4.841388,-4.636704],[0.948315,-4.801542,-8.549324,-7.482568,0.433905,-2.237073],[6.926482,4.535354,-2.018107,-7.629417,1.167701,8.124695],[-7.264222,-5.546180,-5.052684,-3.115905,1.971396,4.815498],[-6.184241,9.839353,-7.658116,-1.628356,-6.017987,7.184552],[-8.705656,-7.750238,-6.976992,4.078176,-5.565024,-4.886107]]], dtype = "float64")#candidate|5809|(2, 14, 6)|const|float64
bop_5810 = relay.power(var_5808.astype('float64'), const_5809.astype('float64')) # shape=(2, 14, 6)
output = bop_5810
output2 = bop_5810
func_5813 = relay.Function([var_5808,], output)
mod['func_5813'] = func_5813
mod = relay.transform.InferType()(mod)
mutated_mod['func_5813'] = func_5813
mutated_mod = relay.transform.InferType()(mutated_mod)
var_5814 = relay.var("var_5814", dtype = "float64", shape = ())#candidate|5814|()|var|float64
func_5813_call = mutated_mod.get_global_var('func_5813')
call_5815 = func_5813_call(var_5814)
output = call_5815
func_5816 = relay.Function([var_5814], output)
mutated_mod['func_5816'] = func_5816
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4433_call = mod.get_global_var('func_4433')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_5818 = relay.TupleGetItem(func_4433_call(), 0)
call_5819 = relay.TupleGetItem(func_4435_call(), 0)
output = call_5818
output2 = call_5819
func_5847 = relay.Function([], output)
mod['func_5847'] = func_5847
mod = relay.transform.InferType()(mod)
output = func_5847()
func_5848 = relay.Function([], output)
mutated_mod['func_5848'] = func_5848
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3200_call = mutated_mod.get_global_var('func_3200')
call_5871 = func_3198_call()
call_5872 = func_3198_call()
var_5873 = relay.var("var_5873", dtype = "float32", shape = (11, 12, 16))#candidate|5873|(11, 12, 16)|var|float32
bop_5874 = relay.equal(call_5871.astype('bool'), relay.reshape(var_5873.astype('bool'), relay.shape_of(call_5871))) # shape=(11, 12, 16)
bop_5877 = relay.equal(call_5872.astype('bool'), relay.reshape(var_5873.astype('bool'), relay.shape_of(call_5872))) # shape=(11, 12, 16)
func_4858_call = mod.get_global_var('func_4858')
func_4859_call = mutated_mod.get_global_var('func_4859')
call_5880 = relay.TupleGetItem(func_4858_call(), 0)
call_5881 = relay.TupleGetItem(func_4859_call(), 0)
output = relay.Tuple([bop_5874,call_5880,])
output2 = relay.Tuple([bop_5877,call_5881,])
func_5887 = relay.Function([var_5873,], output)
mod['func_5887'] = func_5887
mod = relay.transform.InferType()(mod)
var_5888 = relay.var("var_5888", dtype = "float32", shape = (11, 12, 16))#candidate|5888|(11, 12, 16)|var|float32
output = func_5887(var_5888)
func_5889 = relay.Function([var_5888], output)
mutated_mod['func_5889'] = func_5889
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_5919 = func_4118_call()
call_5920 = func_4118_call()
func_5610_call = mod.get_global_var('func_5610')
func_5611_call = mutated_mod.get_global_var('func_5611')
call_5921 = func_5610_call()
call_5922 = func_5610_call()
const_5925 = relay.const([[False,True,True,True,False,False,True,True,True],[True,True,True,False,True,True,False,False,True],[False,False,True,False,False,False,False,False,False],[True,True,False,True,False,True,False,True,True],[False,False,False,False,True,False,True,True,True],[False,True,True,True,True,True,True,True,False],[True,False,False,True,True,True,True,False,True],[False,True,False,True,True,True,True,True,False],[True,False,False,False,False,True,False,False,True],[True,True,False,True,False,False,True,True,True],[True,False,False,False,False,True,True,True,False],[False,False,False,False,False,False,False,False,True],[False,False,True,True,False,False,True,True,False],[False,True,True,True,False,True,True,False,True],[False,True,False,True,True,False,True,False,False],[True,False,True,False,False,True,True,True,True],[True,True,True,True,True,False,False,False,False],[True,False,False,False,False,False,False,True,True],[True,False,True,True,False,False,False,False,False],[False,False,False,True,True,True,False,True,False],[False,True,False,False,True,False,True,True,True],[True,False,False,False,True,True,False,False,True],[False,True,True,False,True,True,False,False,True],[True,True,False,True,True,True,False,False,False],[False,True,False,True,False,False,False,False,True],[True,False,True,False,False,False,True,True,True],[True,True,False,False,True,True,False,False,False],[True,False,False,False,True,True,False,False,True],[False,False,False,True,True,False,False,True,True],[True,True,False,False,False,True,False,False,False],[True,False,True,False,True,True,False,True,False],[False,True,True,True,True,True,True,False,True],[False,True,False,True,False,True,True,False,True],[False,True,True,True,False,True,False,False,True],[True,True,False,False,True,False,True,False,True],[False,False,False,True,False,True,False,True,True],[True,False,True,True,False,False,False,True,True],[False,True,True,True,True,False,True,True,True],[True,False,False,True,False,False,True,False,False],[False,False,True,True,True,True,False,False,True],[True,True,True,False,True,False,True,False,True],[False,True,False,True,True,False,True,False,True],[True,True,True,True,True,True,False,False,False],[True,False,True,True,True,False,False,True,True],[False,True,True,False,True,False,False,False,True],[True,False,True,False,True,False,True,True,True],[False,True,True,False,True,False,True,False,True],[True,False,True,False,False,False,True,False,True],[False,True,True,True,False,True,True,False,True],[True,True,False,True,True,True,False,True,False],[False,True,False,False,False,False,True,True,True],[True,False,True,False,False,False,True,False,False],[True,True,False,False,False,True,False,True,False],[True,False,False,False,False,True,False,False,True],[True,True,False,False,False,True,True,False,True],[False,False,True,False,True,False,True,True,True],[False,True,False,True,False,False,True,False,True],[False,True,True,True,False,True,False,False,True],[True,True,False,False,True,False,False,False,True],[False,True,False,True,True,True,False,False,True],[False,True,False,True,True,True,True,True,True],[False,True,True,True,False,False,True,False,False],[True,False,False,False,True,True,False,False,False],[True,False,True,True,True,False,True,False,False],[False,True,True,True,True,False,False,True,False],[False,False,False,False,False,True,False,False,False],[True,True,False,False,False,True,True,True,False],[True,False,False,True,False,False,False,True,True],[False,True,False,False,False,True,True,False,True],[False,True,True,False,False,False,False,False,True],[True,True,False,True,True,True,False,False,True],[False,True,True,True,True,False,False,False,False],[True,True,True,False,True,False,True,True,False],[False,True,True,True,True,False,True,False,True],[False,False,False,False,False,True,True,False,False],[True,False,False,False,True,True,True,True,False],[True,False,True,True,False,True,False,True,False],[True,True,False,False,True,True,False,True,True],[True,False,True,False,False,True,False,False,False],[False,True,True,False,False,False,False,True,False],[True,False,False,True,True,True,True,True,False],[False,False,False,False,True,False,True,True,False],[True,False,False,True,False,True,True,False,True],[True,False,True,True,True,True,True,False,False],[False,False,True,True,False,True,True,False,True],[True,False,False,False,True,False,False,False,False],[False,True,True,True,False,True,False,False,True],[True,True,True,True,False,True,True,True,False],[False,False,False,True,True,False,False,True,True],[False,False,False,True,False,True,False,True,False],[True,False,False,False,True,True,False,True,True],[True,False,False,True,False,False,False,False,False],[False,False,True,False,False,True,False,True,True],[True,True,True,True,True,True,True,True,False],[True,True,True,False,True,True,True,False,False],[True,False,False,True,True,False,True,True,False],[False,True,False,False,False,True,True,False,False],[False,True,False,False,False,True,False,True,False],[True,False,True,True,True,True,True,True,False],[True,False,True,False,False,False,False,False,True],[True,True,True,False,True,False,False,False,True],[True,False,False,False,True,False,True,True,True],[False,False,False,True,False,False,False,False,True],[True,False,True,False,True,True,True,True,False],[True,True,False,False,True,False,False,True,False],[False,False,True,False,False,True,False,True,True],[True,False,True,False,True,True,True,True,True],[False,False,False,True,True,False,True,False,True],[False,False,False,False,True,False,True,True,False],[False,True,False,False,False,False,True,False,True],[True,False,False,False,False,False,False,True,True],[False,True,True,True,True,False,True,True,True],[True,False,False,False,False,True,False,False,False],[False,False,False,True,True,False,True,True,True],[True,True,False,False,False,True,False,True,False],[False,True,True,True,False,True,True,False,False],[False,False,False,False,False,False,True,True,True],[True,False,False,False,True,False,True,False,False],[False,False,True,True,False,False,False,True,True],[False,False,True,False,False,False,False,True,False],[True,False,False,False,True,False,True,False,False],[True,True,False,True,True,False,False,False,False],[True,True,True,False,True,True,True,True,True],[True,True,False,False,False,False,False,True,False],[False,False,False,False,True,True,False,False,False],[False,False,True,False,True,False,True,True,True],[False,True,False,False,False,True,False,False,False],[True,False,True,True,True,True,True,True,False],[False,False,False,False,False,False,True,True,False],[True,False,True,False,True,False,False,True,True],[False,True,True,False,False,False,True,True,True],[False,False,False,False,False,False,False,True,True],[False,False,False,False,False,False,False,False,True],[False,True,False,True,True,False,True,True,False],[True,False,False,False,False,False,False,False,True],[True,False,False,False,False,False,False,True,False],[False,True,True,False,True,False,False,True,True],[False,False,False,True,True,False,True,True,False],[True,True,False,False,False,False,False,False,False],[True,False,True,True,True,False,False,True,False],[False,True,True,True,False,True,True,True,False],[True,False,True,True,True,False,True,False,True],[True,False,True,False,True,False,True,True,True],[False,True,False,False,False,True,True,True,True],[False,True,False,False,False,False,True,False,False],[True,True,False,False,True,False,False,True,False],[False,False,True,True,False,False,True,False,False],[False,True,False,False,True,True,False,True,True],[True,False,True,True,False,True,True,False,False],[True,False,True,True,False,True,False,True,False],[True,False,False,True,True,False,True,True,True],[False,True,True,False,False,True,True,True,True],[False,False,False,False,False,False,True,True,True],[True,False,False,True,True,True,True,False,False],[True,False,True,True,False,False,False,False,True],[True,False,False,True,False,True,True,True,True],[True,False,False,False,True,False,True,False,True],[False,False,False,False,True,False,True,False,False],[True,False,True,False,False,True,True,True,True],[False,False,False,True,True,True,True,False,False],[False,True,True,True,True,True,True,True,False],[True,False,True,False,True,True,True,False,True],[False,True,False,True,True,False,False,False,False],[True,True,False,True,True,True,False,True,False],[True,False,True,False,False,True,True,False,False],[False,True,False,False,True,True,False,False,False],[True,False,False,True,True,False,True,True,True],[False,True,False,False,True,True,True,True,True],[False,False,True,False,False,False,True,False,True],[False,True,True,True,False,False,True,True,True],[True,False,False,True,False,False,True,False,True],[False,True,False,True,True,False,False,True,False],[False,False,True,True,True,False,True,False,False],[True,True,True,False,True,True,True,False,True],[True,True,True,False,False,False,False,True,True],[False,False,False,False,False,True,True,False,False],[True,True,False,True,False,True,False,False,False],[True,True,False,False,False,False,True,False,False],[True,False,True,False,False,True,True,True,False],[False,False,False,False,False,True,False,True,True],[True,False,True,False,True,True,False,False,True],[False,True,False,False,True,False,False,True,True],[True,False,False,True,False,False,True,False,False],[False,False,False,True,False,False,True,False,True],[False,False,True,True,True,True,True,True,False],[False,True,True,True,True,False,True,False,False],[True,False,True,False,False,True,False,False,True],[False,True,True,True,True,False,True,False,True],[False,False,False,False,False,False,True,True,True],[True,False,True,False,True,True,True,True,False],[False,True,False,False,True,True,True,True,False],[True,False,False,False,False,False,True,False,False],[True,True,True,False,True,True,True,True,True],[True,False,False,True,False,False,True,False,True],[False,False,False,False,True,False,False,False,False],[True,True,False,True,False,False,True,False,True],[False,True,False,True,False,False,False,True,False],[False,False,True,True,False,True,False,False,False],[False,True,False,True,False,True,True,True,True],[True,False,True,False,True,True,False,False,True],[False,False,True,True,False,True,False,False,False],[True,False,False,True,False,True,False,True,True],[True,True,True,True,False,True,False,True,False],[True,True,True,True,False,True,False,True,False],[True,True,False,True,False,False,False,True,False],[True,True,False,True,True,True,False,False,True],[True,False,False,False,False,False,True,True,False],[False,True,True,False,False,False,False,False,False],[False,False,True,True,True,True,True,False,False],[False,False,False,True,False,False,False,False,False],[False,True,True,False,True,False,True,False,True],[True,False,True,True,True,True,False,False,False],[True,True,True,True,True,True,True,False,True],[False,False,True,False,False,False,False,False,False],[False,True,False,True,False,False,False,True,True],[True,False,True,False,True,False,True,True,True],[False,False,False,False,False,False,True,True,True],[False,True,True,False,True,True,False,True,True],[False,True,True,False,True,True,True,True,False],[False,False,True,True,False,False,True,False,False],[False,False,True,True,False,False,False,False,False],[True,False,True,True,False,False,False,False,True],[True,False,False,True,False,False,True,True,True],[True,True,True,True,True,True,True,False,True],[True,False,True,True,False,True,False,True,False],[True,True,False,False,False,False,True,True,False],[True,False,False,False,True,True,False,True,False],[True,False,False,True,True,False,False,True,False],[False,True,True,False,False,False,False,True,False],[True,False,False,True,True,False,True,False,False],[False,False,True,False,True,True,False,False,False],[True,True,True,True,True,True,True,True,True],[True,True,False,False,False,False,False,False,False],[False,True,False,False,False,False,True,False,True],[False,True,False,True,False,True,False,True,False],[True,False,True,True,False,False,True,False,True],[False,False,True,False,False,False,False,True,False],[False,False,True,True,True,False,True,False,False],[False,False,True,False,False,False,True,True,False],[False,False,False,True,False,False,False,False,False],[False,False,True,True,False,False,False,False,True],[False,True,True,False,False,True,True,False,True],[True,False,False,True,False,True,True,True,True],[True,True,False,False,True,False,True,False,True],[True,False,True,False,False,False,True,False,False],[True,False,True,False,True,True,True,True,True],[False,False,False,True,False,True,True,False,False],[False,True,True,True,True,True,False,True,False],[False,True,False,True,False,False,False,False,False],[True,True,True,False,True,True,False,True,True],[True,False,True,True,False,True,False,True,False],[False,True,True,False,False,False,False,True,False],[True,True,True,True,False,False,False,False,False],[True,False,True,True,True,True,False,False,False],[True,True,True,True,True,True,True,True,True],[True,True,False,False,False,True,True,True,True],[True,True,True,True,True,True,False,False,False],[False,False,False,False,False,True,True,True,False],[False,False,True,True,False,True,True,False,True],[False,True,True,True,False,False,False,False,True],[True,False,True,True,False,False,False,False,False],[True,False,True,False,False,False,True,False,False],[False,True,False,False,False,True,True,True,True],[True,False,True,True,True,False,False,True,False],[False,True,True,False,False,True,False,False,True],[False,False,True,False,False,True,False,False,True],[True,True,False,False,True,False,False,False,False],[False,False,True,False,True,False,True,True,False],[False,True,True,False,True,True,True,True,True],[False,True,False,True,False,True,False,True,False],[False,True,False,False,True,True,True,True,False],[True,True,True,False,True,True,True,True,False],[False,True,False,True,True,True,True,True,False],[True,True,True,True,True,False,False,False,True],[True,True,False,True,True,True,False,True,True],[True,False,False,False,False,True,False,True,True],[True,True,False,True,False,True,False,True,False],[False,True,False,True,False,False,False,True,True],[True,False,False,False,True,False,True,True,False],[False,True,True,True,True,False,True,False,False],[False,True,False,True,True,True,True,True,False],[True,True,True,False,False,True,False,True,True],[False,False,False,False,False,False,False,False,True],[False,True,True,True,False,False,True,True,False],[False,False,True,False,False,False,False,False,False],[True,True,True,False,True,True,True,False,False],[True,False,False,False,False,True,True,True,True],[False,False,False,False,True,True,True,True,True],[True,True,True,True,True,False,True,True,False],[False,False,False,False,True,False,False,True,False],[False,True,False,True,True,False,False,True,True],[True,False,True,False,True,False,True,False,True],[False,True,True,False,False,True,False,False,True],[False,True,False,False,True,True,False,False,False],[True,False,True,False,True,True,True,True,False],[False,True,True,True,True,False,False,True,False],[False,True,True,True,True,False,True,True,True],[True,False,True,True,True,False,True,True,True],[False,True,True,True,True,False,False,False,True],[False,True,False,True,True,True,False,False,False],[False,True,True,True,False,True,False,False,False],[False,True,False,False,True,True,True,False,False],[True,False,False,False,True,True,False,False,False],[True,False,False,True,False,False,False,True,False],[False,True,False,False,False,True,False,False,True],[True,True,True,True,False,False,False,False,True],[True,False,True,False,True,True,False,False,True],[False,False,False,True,False,True,True,True,True],[True,True,True,False,True,False,True,False,False],[True,False,False,False,False,False,True,False,True],[False,False,True,True,True,False,True,False,False],[True,True,True,False,False,True,False,False,False],[False,False,False,True,True,True,True,False,True],[False,True,True,True,False,True,True,True,False],[True,True,False,True,False,False,True,False,False],[False,False,True,False,True,True,False,False,False],[True,True,False,False,True,False,True,True,False],[True,False,True,True,True,False,False,False,False],[False,True,True,False,True,True,True,True,False],[False,False,False,True,True,False,True,False,True],[True,True,False,True,False,False,True,False,True],[True,False,False,False,False,True,True,False,True],[False,False,False,True,False,False,True,True,False],[True,True,False,True,False,True,True,False,False],[False,True,False,True,False,False,True,False,False],[True,True,False,False,False,False,False,True,True],[True,False,False,True,False,True,True,True,False],[False,False,False,False,False,True,False,False,True],[False,True,False,False,False,True,True,False,True],[True,True,False,False,False,True,True,True,True],[False,False,False,False,False,False,False,True,True],[True,True,True,True,False,False,True,False,True],[False,True,True,False,True,False,False,True,False],[True,False,True,False,True,True,False,True,False],[True,False,True,False,True,False,True,False,False],[True,True,True,False,False,False,False,False,True],[False,False,True,True,False,True,False,False,False],[False,True,False,False,False,False,True,False,True],[True,True,False,False,False,True,True,True,True],[True,True,True,True,True,False,False,False,False],[True,True,False,False,True,True,False,True,True],[False,False,True,True,True,False,True,True,True],[True,False,False,False,False,True,False,True,False],[False,True,True,False,False,False,False,False,True],[False,False,False,True,False,False,True,False,True],[True,True,True,False,False,True,False,True,True],[True,True,False,False,True,True,True,True,False],[True,True,False,False,True,True,False,True,True],[False,False,True,True,True,True,False,False,True],[False,False,False,True,False,True,False,False,False],[True,True,True,True,False,True,False,False,False],[True,False,True,False,False,True,False,True,True],[True,False,True,False,False,True,True,True,True],[False,True,True,True,True,False,False,False,False],[True,False,False,False,True,False,True,False,False],[True,False,False,False,True,False,True,True,False],[False,False,True,False,True,True,True,False,False],[False,False,False,False,False,True,True,False,False],[True,True,False,False,False,False,False,False,True],[False,True,True,False,False,True,True,False,False],[False,True,False,False,True,True,True,False,True],[False,True,True,False,False,False,True,False,True],[True,False,True,True,False,True,False,False,True],[True,False,True,False,False,False,False,True,False],[True,False,False,False,False,True,True,False,True],[False,True,False,True,True,False,False,False,True],[True,False,True,False,True,True,True,True,False],[False,False,True,False,True,True,False,False,True],[True,True,True,False,True,True,False,False,False],[True,True,False,False,False,False,True,True,True],[True,False,True,True,False,True,False,False,False],[True,False,False,False,True,False,True,False,True],[False,False,False,False,True,True,False,True,True],[False,True,False,False,False,True,True,True,True],[False,True,False,False,False,False,True,False,False],[True,True,False,False,False,False,False,False,False],[True,True,True,True,True,False,True,True,False],[False,False,True,False,False,False,False,True,False],[False,False,False,False,True,False,False,True,False],[True,False,False,True,True,True,False,False,True],[True,False,False,True,False,True,True,False,True],[True,False,False,False,True,False,False,True,True],[False,False,True,False,True,True,True,False,False],[False,False,True,True,True,True,False,True,True],[True,False,False,False,True,False,True,True,True],[True,False,True,True,False,True,False,True,False],[True,False,False,True,False,False,False,False,False],[True,False,True,True,True,True,True,True,False],[True,False,False,True,False,False,False,True,False],[True,True,True,True,False,True,True,True,False],[True,False,False,True,True,False,False,False,True],[True,True,False,False,True,True,False,False,True],[False,False,False,False,True,True,False,False,True],[True,True,False,True,False,False,True,False,False],[True,False,False,False,False,False,True,False,True],[False,False,True,True,False,True,True,False,False],[False,False,False,True,False,True,True,True,True],[False,True,True,False,False,False,False,True,False],[False,False,False,True,False,False,False,True,False],[True,False,False,True,False,True,True,True,True],[False,False,False,False,False,True,True,False,False],[True,True,True,True,True,True,True,True,True],[True,True,False,True,True,False,False,False,False],[True,False,True,False,False,True,False,False,False],[False,False,False,False,True,True,True,True,True],[False,False,False,True,False,True,True,True,False],[True,True,True,True,False,True,False,False,True],[True,True,False,True,True,False,False,True,True],[True,False,False,False,False,True,False,True,True],[False,False,False,False,True,False,True,False,False],[False,False,True,False,True,False,False,True,True],[False,True,False,True,False,False,False,True,False],[True,True,True,False,True,True,False,False,False],[False,True,False,True,False,False,False,False,True],[False,False,False,True,False,True,True,True,False],[True,True,True,True,False,False,False,False,False],[True,True,False,True,True,True,True,False,True],[True,False,True,False,False,True,True,True,True],[False,False,True,False,True,False,True,False,True],[False,False,True,False,True,False,False,False,False],[True,True,False,True,False,True,False,True,True],[False,False,True,True,False,True,False,True,True],[True,False,True,False,False,False,True,False,True],[False,False,False,False,False,True,False,True,False],[True,True,True,True,True,True,False,True,True],[True,True,False,False,False,True,False,False,True],[False,False,False,True,False,False,True,False,False],[True,False,True,True,False,True,False,True,False],[True,True,True,False,False,True,True,True,True],[False,True,False,True,True,False,True,False,False],[False,False,False,False,True,False,False,False,False],[True,False,True,True,True,False,True,True,True],[False,False,False,True,False,True,True,False,False],[True,True,False,True,True,False,True,False,True],[False,False,True,False,True,True,False,False,False],[False,True,False,True,True,False,True,True,True],[False,False,True,False,False,False,True,True,False],[True,True,False,True,True,False,False,True,True],[False,True,True,False,False,True,False,True,False],[True,True,True,False,True,False,True,False,False],[True,True,True,True,False,False,True,True,True],[True,False,True,False,False,False,False,False,False],[True,True,False,True,False,True,True,False,False],[True,True,False,True,False,True,False,False,False],[True,True,True,False,True,True,True,True,True],[False,True,False,False,False,True,False,False,True],[True,True,True,False,False,False,False,True,False],[False,True,False,False,False,False,True,True,True],[True,False,False,False,False,False,False,True,False],[True,True,False,False,True,True,True,True,True],[True,True,False,False,True,False,False,True,False],[False,True,True,True,False,False,False,False,False],[False,True,True,False,False,True,True,True,False],[False,False,True,False,False,False,False,False,False],[False,False,True,True,True,False,False,False,False],[False,False,True,True,False,False,False,True,False],[True,False,True,True,False,False,False,False,False],[True,True,False,True,True,False,False,False,True],[True,True,False,True,True,False,False,False,True],[False,True,False,True,False,False,False,False,False],[False,False,True,False,True,False,False,False,True],[True,True,False,False,False,True,False,True,False],[True,False,True,False,False,False,False,True,False],[False,False,False,False,False,True,True,True,False],[True,True,True,True,False,False,True,True,False],[False,True,True,False,False,True,True,False,False],[True,False,True,False,False,True,False,True,False],[True,False,True,False,False,False,True,True,True],[True,False,False,True,False,True,False,False,False],[False,False,False,False,True,True,True,True,True],[True,False,False,True,True,True,False,True,True],[False,False,False,True,True,False,True,False,False],[True,True,False,True,True,False,True,True,False],[False,False,True,False,True,True,False,False,True],[True,False,False,False,True,True,False,False,False],[False,False,True,False,True,False,True,False,True],[True,True,False,True,False,False,True,False,False],[False,False,False,True,False,True,False,False,False],[True,True,False,True,True,False,False,False,True],[False,True,True,True,False,True,True,False,True],[False,True,True,False,True,True,False,True,True],[True,True,False,True,False,True,False,True,False],[False,False,False,False,False,True,True,False,False],[False,True,False,True,True,True,False,True,False],[False,False,True,True,True,False,True,True,False],[False,True,False,True,True,False,True,True,False],[True,True,False,True,True,False,True,True,True],[False,True,True,False,True,True,False,True,False],[False,False,True,True,True,False,True,False,False],[True,True,True,True,False,False,False,True,False],[False,False,True,True,False,False,False,True,False],[True,True,True,False,True,True,True,False,False],[False,True,False,False,False,False,True,False,False],[False,False,False,False,False,False,True,True,True],[True,False,False,True,True,True,False,True,False],[False,True,True,False,True,False,True,True,True],[True,False,True,True,False,True,True,False,True],[False,True,False,True,True,False,True,False,False],[False,True,True,False,True,False,True,True,True],[False,False,False,True,True,True,False,True,True],[True,False,False,False,False,True,False,True,False],[True,False,True,True,False,False,False,True,True],[True,False,False,False,False,True,True,True,False],[False,True,True,True,False,False,True,False,False],[True,True,False,True,False,False,False,True,True],[False,True,False,True,False,False,False,True,True],[True,False,False,True,False,False,True,True,False],[True,True,True,True,False,False,True,True,False],[False,False,True,True,False,False,True,False,True],[True,False,False,False,True,False,True,False,False],[True,True,True,True,False,False,False,False,False],[False,True,False,False,True,False,True,False,False],[False,True,False,True,True,False,True,True,True],[True,False,False,True,True,True,False,True,False],[True,True,False,True,False,True,True,False,True],[True,False,True,False,False,True,False,True,False],[True,False,True,False,True,False,False,False,True],[False,False,False,False,True,False,False,True,False],[True,False,False,False,False,False,False,False,False],[True,False,True,True,True,True,False,False,False],[False,False,False,False,False,True,False,False,False],[False,False,True,False,False,False,True,False,False],[True,False,False,False,True,False,True,False,False],[True,True,False,True,True,False,False,True,True],[True,False,True,True,False,False,True,True,False]], dtype = "bool")#candidate|5925|(525, 9)|const|bool
bop_5926 = relay.floor_mod(call_5919.astype('float32'), const_5925.astype('float32')) # shape=(525, 9)
bop_5929 = relay.floor_mod(call_5920.astype('float32'), const_5925.astype('float32')) # shape=(525, 9)
uop_5931 = relay.acos(call_5921.astype('float32')) # shape=(14, 3, 15)
uop_5933 = relay.acos(call_5922.astype('float32')) # shape=(14, 3, 15)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_5941 = func_2910_call()
call_5942 = func_2910_call()
bop_5943 = relay.maximum(const_5925.astype('uint64'), call_5919.astype('uint64')) # shape=(525, 9)
bop_5946 = relay.maximum(const_5925.astype('uint64'), call_5920.astype('uint64')) # shape=(525, 9)
func_5744_call = mod.get_global_var('func_5744')
func_5746_call = mutated_mod.get_global_var('func_5746')
call_5963 = relay.TupleGetItem(func_5744_call(), 0)
call_5964 = relay.TupleGetItem(func_5746_call(), 0)
bop_5987 = relay.not_equal(bop_5926.astype('bool'), relay.reshape(bop_5943.astype('bool'), relay.shape_of(bop_5926))) # shape=(525, 9)
bop_5990 = relay.not_equal(bop_5929.astype('bool'), relay.reshape(bop_5946.astype('bool'), relay.shape_of(bop_5929))) # shape=(525, 9)
func_5709_call = mod.get_global_var('func_5709')
func_5715_call = mutated_mod.get_global_var('func_5715')
var_5998 = relay.var("var_5998", dtype = "float64", shape = (450,))#candidate|5998|(450,)|var|float64
const_5999 = relay.const([4.096591,4.209315,7.405711,6.441548,-9.656337,-2.985882,8.291070,-1.240716,4.541746,-2.234617,3.190639,-0.050380,-1.328599,1.873316,-2.245499,7.409234,5.543529,-9.157528,-9.518375,-5.561595,4.460795,-9.987208,-2.439934,6.302051,5.522043,9.302915,6.742599,-2.991572,1.561323,-2.329238,2.023889,3.388924,-0.102945,9.995107,-4.748433,9.173702,-1.845364,-7.135777,2.039660,3.671598,9.093752,0.109713,-9.404394,-1.055425,-8.268217,2.143712,-0.182331,-4.425981,-9.846006,-4.470405,5.829934,-6.783917,7.095295,7.468794,8.230004,9.053417,2.549140,6.657730,-0.935521,-8.153709,-8.322225,-7.907348,-3.505710,2.477890,1.934826,1.340434,-8.030340,-8.102291,3.071662,-7.044877,-2.246112,9.661178,-3.573279,-2.590947,9.572338,3.100910,-3.833970,-9.974743,-2.751409,-8.913516,5.745916,6.992305,3.613326,9.837645,9.565921,9.710516,8.072144,6.266809,-2.067216,-9.766324,-7.434232,3.422776,-1.164582,-9.654474,-2.387063,-2.486448,-2.785623,5.838227,9.486791,-7.384278,-6.519917,6.139658,6.187632,0.350957,-0.607643,0.628941,-9.881024,6.830937,-8.142391,6.880044,-8.617064,2.691846,1.116402,4.159765,7.197663,4.793846,0.410072,-2.868993,-7.504987,-6.296778,6.191124,5.638559,5.357674,-1.011643,-7.044769,-8.787241,0.908992,-7.009222,-5.798546,-2.028226,5.913208,1.881933,-4.106016,6.846639,7.914855,9.856802,5.322926,-1.782193,2.754667,7.263430,0.874436,1.582119,5.294887,8.978517,4.123345,1.000709,-6.175588,9.430906,-0.896672,8.107385,7.187568,2.813269,2.576241,4.583616,-4.523357,3.470640,-5.058357,8.329525,-3.935370,3.383929,-6.075332,-5.870831,6.985909,2.669151,9.808521,8.270650,7.675642,6.442977,5.104832,4.420116,6.272573,6.781039,4.990985,1.003457,9.859028,1.774376,-4.741294,-2.235309,-3.922551,8.321401,-1.188184,-0.806715,0.887809,1.212615,-3.806555,2.537165,0.867963,5.906484,0.508659,-8.933488,2.227514,-7.720570,4.805465,8.874268,-3.990664,3.410699,9.393754,-6.269957,-7.625592,4.713295,-8.854928,-6.884611,3.360418,6.831860,3.425614,-7.911922,9.627489,-8.899659,0.825225,-3.935025,-1.778360,3.662849,2.362755,9.183526,7.355580,-9.603529,8.367225,9.110676,-3.486337,2.290825,-8.584404,-7.102383,-3.982280,-3.069865,-6.231490,8.404506,0.504000,1.333596,-1.499651,-9.394965,8.337821,5.116567,1.375102,-0.094903,3.501658,2.397344,5.766441,-5.639870,-7.650073,7.143690,7.438008,-2.185629,9.962080,-9.776845,-4.991782,3.795107,5.967059,-5.740931,4.995519,0.860747,-2.080216,-8.155953,-8.719455,8.106980,-2.426127,-5.783652,8.225122,-7.693750,-1.536960,-4.841960,7.146053,-0.687436,-2.291850,3.666946,0.006637,9.384937,-8.874098,3.932479,-3.971953,6.320447,-6.903335,-5.035005,-0.909287,-6.179349,9.658288,5.196876,2.349372,-8.504509,-4.625368,7.631658], dtype = "float32")#candidate|5999|(280,)|const|float32
var_6000 = relay.var("var_6000", dtype = "uint8", shape = (168,))#candidate|6000|(168,)|var|uint8
const_6001 = relay.const(9.196187, dtype = "float32")#candidate|6001|()|const|float32
call_5997 = relay.TupleGetItem(func_5709_call(relay.reshape(var_5998.astype('float64'), [3, 10, 15]), relay.reshape(const_5999.astype('float32'), [140, 2]), relay.reshape(var_6000.astype('uint8'), [168,]), relay.reshape(const_6001.astype('float32'), []), ), 0)
call_6002 = relay.TupleGetItem(func_5715_call(relay.reshape(var_5998.astype('float64'), [3, 10, 15]), relay.reshape(const_5999.astype('float32'), [140, 2]), relay.reshape(var_6000.astype('uint8'), [168,]), relay.reshape(const_6001.astype('float32'), []), ), 0)
output = relay.Tuple([uop_5931,call_5941,call_5963,bop_5987,call_5997,var_5998,const_5999,var_6000,const_6001,])
output2 = relay.Tuple([uop_5933,call_5942,call_5964,bop_5990,call_6002,var_5998,const_5999,var_6000,const_6001,])
func_6023 = relay.Function([var_5998,var_6000,], output)
mod['func_6023'] = func_6023
mod = relay.transform.InferType()(mod)
var_6024 = relay.var("var_6024", dtype = "float64", shape = (450,))#candidate|6024|(450,)|var|float64
var_6025 = relay.var("var_6025", dtype = "uint8", shape = (168,))#candidate|6025|(168,)|var|uint8
output = func_6023(var_6024,var_6025,)
func_6026 = relay.Function([var_6024,var_6025,], output)
mutated_mod['func_6026'] = func_6026
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3920_call = mod.get_global_var('func_3920')
func_3922_call = mutated_mod.get_global_var('func_3922')
call_6053 = relay.TupleGetItem(func_3920_call(), 0)
call_6054 = relay.TupleGetItem(func_3922_call(), 0)
func_3260_call = mod.get_global_var('func_3260')
func_3263_call = mutated_mod.get_global_var('func_3263')
const_6056 = relay.const([4.867132,5.361755,-9.029000,-2.760557,5.561536,-9.845364,4.305539,-3.624353,7.163666,-6.338436,-6.064990,8.121440,-6.286231,6.400188,-0.701386,-2.299232,8.992431,8.632716,5.410134,1.535056,-7.420359,-0.749491,-5.916069,9.753365,-0.583204,-3.208772,-7.959613,-6.161449,-1.348899,-1.253960,-9.128179,-8.581672,-2.998397,8.018803,4.813848,5.175610,9.142041,8.265188,-9.718791,3.009136,5.367004,0.043923,6.016880,-3.267728,8.514825,-2.065152,2.220536,2.034806,-4.431088,-8.433120,-0.992429,6.088777,1.498228,8.958252,6.501998,2.133009,3.823617,-5.401881,-8.718385,-9.833640,-7.103674,7.828904,2.125717,1.829341,-0.714359,-1.357997,8.991309,-8.882266,-8.660713,-2.921505,-4.001316,-3.250024,-7.369116,-1.716289,-2.402334,-3.641692,-6.571878,-2.026507,1.296155,8.748883,2.339556,-9.071492,-3.025950,-9.890712,-4.321449,-9.431872,-8.882527,-8.064848,-6.426620,7.136996,9.810562,7.297631,3.283230,-0.643823,9.857690,-2.975661,4.981494,-2.544256,2.341501,-4.167049,6.417536,-0.378478,-3.548337,3.039024,-0.343340,1.896627,-7.682303,7.488230,-8.107338,-7.286634,0.191011,6.484132,9.827112,-0.277839,-4.288488,2.748206,-8.859336,9.628824,-4.989664,7.795916,4.581278,9.316688,9.646229,9.985112,-9.480046,9.468166,7.432068,-9.163591,-6.786208,7.734975,5.630771,8.163355,8.399903,-3.735513,6.999901,-8.137847,-2.693744,-4.250666,-1.933091,-5.241671,-1.265601,-8.935183,-1.264492,-1.326518,-1.134063,1.622994,-2.516030,6.810804,8.494138,-9.455427,4.210994,0.235357,-1.985623,2.540204,3.475349,6.649406,9.651073,5.899291,-2.841678,5.616006,-7.172106,-8.916472,5.010467,-5.464228,-0.126438,2.355319,5.237671,1.109729,-6.220397,-7.489037,-4.754731,5.147935,5.668611,4.861975,3.631242,-8.523592,1.460046,-1.790676,-9.130023,4.985534,6.343010,-9.021479,5.380422,-9.310557,-9.439104,-4.278261,-4.671363,3.211874,-1.872286,2.954278,8.008071,3.418663,7.836802,1.642432,-8.605115,-3.086783,2.286583,-4.431082,-7.830633,-0.176509,7.646531,-9.738969,8.045790,-0.708032,-9.591597,5.330922,2.086901,5.131520,-6.368053,8.652675,2.537592,7.078397,-6.470820,-5.359552,-4.800941,-3.699120,0.677338,-5.625862,-6.874958,-9.722300,-2.740546,-5.436702,6.777923,-6.937884,-8.176823,-2.588403,1.585687,-4.267672,-3.768514,6.368767,2.783952,-3.024550,-5.769318,3.567093,9.983360,4.839833,8.600358,-2.858869,5.899027,9.603272,-3.213590,-6.906147,9.959589,9.758790,3.098830,-7.400491,-6.957309,0.882544,3.787265,7.007433,-4.138483,2.940817,-9.454489,-7.507056,-2.969391,2.709733,-9.005110,4.905577,-8.454394,7.155531,3.377566,2.533423,-9.190322,-5.840292,8.407581,3.781838,-3.303075,-6.165161,-4.188671,8.901810,-6.217756,0.811475,-0.063665,-6.844028,9.940328,-5.950509,2.311206,2.725448,-8.290269,-3.694366,3.310420,8.316292,-1.964214,5.342191,7.284717,7.199047,1.280397,-8.305936,5.139394,9.144875,-4.444195,3.193262,9.879893,1.961867,-2.672530,7.956661,0.628412,-4.901529,-5.741696,-2.431982,-8.133257,1.810518,-5.929014,9.661120,-1.232813,3.765704,-0.491752,3.233511,6.250732,0.317419,-0.993042,1.904762,0.915255,2.234647,0.368409,0.528954,6.465211,-5.512400,-5.309633,-9.216546,-4.217606,0.369483,-7.851910,-3.232959,-4.436679,-9.620978,-7.644319,-9.072055,9.091316,-7.427179,-2.066265,-3.500439,-2.588771,7.462060,-6.946375,-1.116054,1.693834,0.293775,-9.329346,1.620991,3.790729,5.350872,-7.524143,6.047336,7.959177,-6.233949,-0.836057,8.768698,3.128907,4.905853,-6.011642,-1.888496,-4.310857,-0.099628,3.136306,8.971738,3.509634,2.919510,-2.456632,7.145591,-7.094520,6.294861,-9.773776,3.827680,-9.014359,7.206517,-8.468823,-0.692517,2.840458,8.278217,4.390486,0.137557,3.606828,-1.287933,0.751479,0.546068,5.268945,-4.385743,-3.941338,-7.776070,9.495882,4.515531,4.053782,-9.878636,-5.931714,-6.862339,-3.229387,-3.708965,-8.927937,2.430210,-4.466636,1.693880,-2.313359,3.594344,3.038410,3.863113], dtype = "float64")#candidate|6056|(396,)|const|float64
call_6055 = relay.TupleGetItem(func_3260_call(relay.reshape(const_6056.astype('float64'), [66, 6])), 2)
call_6057 = relay.TupleGetItem(func_3263_call(relay.reshape(const_6056.astype('float64'), [66, 6])), 2)
bop_6065 = relay.maximum(const_6056.astype('int32'), relay.reshape(call_6055.astype('int32'), relay.shape_of(const_6056))) # shape=(396,)
bop_6068 = relay.maximum(const_6056.astype('int32'), relay.reshape(call_6057.astype('int32'), relay.shape_of(const_6056))) # shape=(396,)
const_6072 = relay.const([[4.626363,-1.710734,6.394318,-8.979340,-4.845481,-5.664335],[-9.540874,-3.862885,2.483124,-2.416682,-2.126458,-6.293035],[7.251612,-6.546549,2.112816,-4.672031,1.201652,-2.644020],[-4.350420,-7.631811,7.564967,4.847248,-6.993225,1.804068],[-8.558927,1.035052,2.145144,4.713627,2.432486,-2.483654],[-3.666725,2.650895,8.700428,-5.096001,6.720619,-8.965703],[-4.940504,-6.685462,-5.412823,-3.453520,4.597150,1.452539],[7.058324,0.927457,-7.800360,9.860016,8.794342,-2.462465],[-0.094694,-8.773306,9.411584,6.413815,8.047072,3.615499],[8.971705,-0.585789,5.049257,3.193093,-6.123172,4.595508],[2.210356,0.341294,-9.562265,3.317471,8.239078,-2.363007],[7.546841,-0.924583,4.155929,-6.289935,6.949191,-6.374768],[-0.294698,5.773292,-1.443420,-8.435693,5.073145,-5.949244],[3.241161,1.692349,-7.592253,-6.029916,8.302254,-4.857487],[-0.904663,8.217771,6.733338,-1.517974,-5.965698,-5.582274],[-5.884587,-8.792304,6.686043,6.197416,-5.982145,3.329028],[-8.038868,-7.479258,-6.011233,5.555484,3.190503,-0.800279],[-9.918432,7.451134,-6.981894,2.986909,-7.911019,-7.717500],[1.063169,-0.929333,-6.706607,-2.042803,1.870844,-2.194822],[0.591823,-1.481614,2.060325,2.004556,6.332022,-3.830375],[-8.239190,7.633015,3.037453,-0.798141,7.036929,-5.321748],[-4.272242,0.540333,-3.085712,9.950442,2.923951,-2.662380],[-7.442171,-4.613736,-9.441799,6.828784,-2.143096,4.064780],[3.465238,-6.128704,5.815819,-3.755866,5.561171,3.922489],[-3.997728,5.549020,0.568401,-8.374460,8.425404,6.207069],[3.942736,9.183329,1.154433,2.976018,-8.510225,-5.548100],[-8.896065,-7.771885,-1.594983,4.791091,-6.326221,-1.644223],[3.478550,-9.890742,2.940509,-0.465011,-0.384921,-8.106089],[0.018594,-6.483669,-1.075162,4.662111,-6.481162,-3.927302],[0.775181,5.703824,4.710149,7.745688,-5.324484,5.423587],[-6.212398,-7.824463,6.125569,-5.255375,-7.263040,1.333173],[7.127321,8.755393,-6.896020,-2.152710,-9.050538,1.791660],[2.537502,-0.884297,-1.046294,3.076980,2.261332,-2.389927],[6.778638,0.257073,7.818475,-9.583194,0.238809,-0.192595],[1.644126,-4.426894,-9.761622,1.703791,-7.735235,7.032824],[-3.025263,2.060175,-1.730685,-5.220160,4.718410,6.535238],[-1.556492,9.201019,-4.078401,5.673277,0.390954,9.772778],[-0.065467,9.884416,-0.559028,6.312196,-3.443429,-0.400368],[-6.217057,-4.596194,4.935585,9.342079,0.880299,8.666628],[-1.960126,1.985747,-4.428242,-8.962801,-0.265421,-7.927067],[-9.243270,2.725282,-4.925037,-9.981358,-0.342283,-6.591894],[-5.983059,-0.660142,5.516996,4.557854,-8.423594,2.555059],[2.681313,7.246430,3.672872,-0.009545,-1.012299,-5.432243],[-8.248335,8.829374,6.504603,-6.514749,9.692101,5.633303],[-9.277840,1.796003,-4.221004,-5.148108,-4.219698,1.104664],[5.047644,8.588482,5.348691,-1.989610,-8.208504,-3.406640],[-4.513918,-4.354033,0.944841,-6.244345,-9.266837,8.106095],[-8.432963,2.831427,6.484833,-3.660968,-9.678626,-0.926448],[-7.000620,0.521597,2.130391,-3.388116,-4.704883,6.894961],[5.581948,-9.520623,4.775018,-2.028629,5.673060,-9.394488],[-9.172588,1.824374,3.514313,-3.521738,-7.696924,-6.340638],[3.330622,6.108979,8.172704,-2.838141,-3.744494,7.175021],[-4.973163,0.764799,0.701890,-6.749087,1.289657,-3.858818],[-1.097535,-5.813596,1.463773,-2.924737,6.566646,-1.816399],[-5.768965,1.351846,2.536005,1.626726,-2.112537,3.128584],[-3.820531,8.942614,2.826447,-9.652026,-9.125531,5.647419],[-2.810745,4.825914,3.424591,-2.469485,-0.715404,4.648971],[-8.414532,0.725793,6.697392,-0.514837,-5.167778,9.806389],[-7.255368,3.570792,-4.557488,-0.278613,-5.725490,6.502320],[3.623416,-3.829881,0.537506,-7.041404,-9.610731,4.900816],[-1.140743,6.712859,1.786818,0.641735,9.493035,2.033507],[0.441854,-3.927710,7.409317,4.121227,9.562728,-7.907762],[7.669702,2.910932,-1.689715,-9.990136,-5.291309,0.636366],[-1.378217,2.725942,-5.884782,-1.995542,-9.589733,1.661244],[-5.172056,0.244887,-1.069384,-4.660054,-9.832404,1.242088],[-3.418052,1.945458,-6.174353,6.823860,8.534612,-1.109667]], dtype = "float64")#candidate|6072|(66, 6)|const|float64
bop_6073 = relay.floor_mod(call_6055.astype('float32'), relay.reshape(const_6072.astype('float32'), relay.shape_of(call_6055))) # shape=(66, 6)
bop_6076 = relay.floor_mod(call_6057.astype('float32'), relay.reshape(const_6072.astype('float32'), relay.shape_of(call_6057))) # shape=(66, 6)
output = relay.Tuple([call_6053,bop_6065,bop_6073,])
output2 = relay.Tuple([call_6054,bop_6068,bop_6076,])
func_6083 = relay.Function([], output)
mod['func_6083'] = func_6083
mod = relay.transform.InferType()(mod)
output = func_6083()
func_6084 = relay.Function([], output)
mutated_mod['func_6084'] = func_6084
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5610_call = mod.get_global_var('func_5610')
func_5611_call = mutated_mod.get_global_var('func_5611')
call_6095 = func_5610_call()
call_6096 = func_5610_call()
output = relay.Tuple([call_6095,])
output2 = relay.Tuple([call_6096,])
func_6134 = relay.Function([], output)
mod['func_6134'] = func_6134
mod = relay.transform.InferType()(mod)
output = func_6134()
func_6135 = relay.Function([], output)
mutated_mod['func_6135'] = func_6135
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5847_call = mod.get_global_var('func_5847')
func_5848_call = mutated_mod.get_global_var('func_5848')
call_6308 = func_5847_call()
call_6309 = func_5847_call()
output = relay.Tuple([call_6308,])
output2 = relay.Tuple([call_6309,])
func_6317 = relay.Function([], output)
mod['func_6317'] = func_6317
mod = relay.transform.InferType()(mod)
mutated_mod['func_6317'] = func_6317
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6317_call = mutated_mod.get_global_var('func_6317')
call_6318 = func_6317_call()
output = call_6318
func_6319 = relay.Function([], output)
mutated_mod['func_6319'] = func_6319
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1084_call = mod.get_global_var('func_1084')
func_1086_call = mutated_mod.get_global_var('func_1086')
call_6329 = relay.TupleGetItem(func_1084_call(), 0)
call_6330 = relay.TupleGetItem(func_1086_call(), 0)
func_5125_call = mod.get_global_var('func_5125')
func_5128_call = mutated_mod.get_global_var('func_5128')
var_6334 = relay.var("var_6334", dtype = "uint32", shape = ())#candidate|6334|()|var|uint32
const_6335 = relay.const([3,8,2,8,-10,3,1,10,2,10,-9,1,5,-1,10,10,-2,9,-10,1,4,-6,9,-2,4,-7,8,-4,-10,7,7,-5,-6,4,-1,-4,10,-9,-7,-10,-7,-8,4,10,-7,6,-4,4,7,-4,2,3,-9,10,7,9,-6,-9,-8,-4], dtype = "uint32")#candidate|6335|(60,)|const|uint32
call_6333 = relay.TupleGetItem(func_5125_call(relay.reshape(var_6334.astype('uint32'), []), relay.reshape(const_6335.astype('uint32'), [15, 4, 1]), ), 0)
call_6336 = relay.TupleGetItem(func_5128_call(relay.reshape(var_6334.astype('uint32'), []), relay.reshape(const_6335.astype('uint32'), [15, 4, 1]), ), 0)
uop_6348 = relay.sin(call_6333.astype('float64')) # shape=(15, 4, 1)
uop_6350 = relay.sin(call_6336.astype('float64')) # shape=(15, 4, 1)
output = relay.Tuple([call_6329,var_6334,const_6335,uop_6348,])
output2 = relay.Tuple([call_6330,var_6334,const_6335,uop_6350,])
func_6351 = relay.Function([var_6334,], output)
mod['func_6351'] = func_6351
mod = relay.transform.InferType()(mod)
mutated_mod['func_6351'] = func_6351
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6352 = relay.var("var_6352", dtype = "uint32", shape = ())#candidate|6352|()|var|uint32
func_6351_call = mutated_mod.get_global_var('func_6351')
call_6353 = func_6351_call(var_6352)
output = call_6353
func_6354 = relay.Function([var_6352], output)
mutated_mod['func_6354'] = func_6354
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6083_call = mod.get_global_var('func_6083')
func_6084_call = mutated_mod.get_global_var('func_6084')
call_6453 = relay.TupleGetItem(func_6083_call(), 0)
call_6454 = relay.TupleGetItem(func_6084_call(), 0)
output = relay.Tuple([call_6453,])
output2 = relay.Tuple([call_6454,])
func_6471 = relay.Function([], output)
mod['func_6471'] = func_6471
mod = relay.transform.InferType()(mod)
mutated_mod['func_6471'] = func_6471
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6471_call = mutated_mod.get_global_var('func_6471')
call_6472 = func_6471_call()
output = call_6472
func_6473 = relay.Function([], output)
mutated_mod['func_6473'] = func_6473
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6482 = relay.var("var_6482", dtype = "float32", shape = (4, 13, 14))#candidate|6482|(4, 13, 14)|var|float32
uop_6483 = relay.cos(var_6482.astype('float32')) # shape=(4, 13, 14)
func_5777_call = mod.get_global_var('func_5777')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_6486 = relay.TupleGetItem(func_5777_call(), 0)
call_6487 = relay.TupleGetItem(func_5779_call(), 0)
uop_6490 = relay.acos(uop_6483.astype('float32')) # shape=(4, 13, 14)
bop_6498 = relay.logical_and(uop_6483.astype('bool'), relay.reshape(var_6482.astype('bool'), relay.shape_of(uop_6483))) # shape=(4, 13, 14)
output = relay.Tuple([call_6486,uop_6490,bop_6498,])
output2 = relay.Tuple([call_6487,uop_6490,bop_6498,])
func_6509 = relay.Function([var_6482,], output)
mod['func_6509'] = func_6509
mod = relay.transform.InferType()(mod)
var_6510 = relay.var("var_6510", dtype = "float32", shape = (4, 13, 14))#candidate|6510|(4, 13, 14)|var|float32
output = func_6509(var_6510)
func_6511 = relay.Function([var_6510], output)
mutated_mod['func_6511'] = func_6511
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_6545 = relay.TupleGetItem(func_2993_call(), 1)
call_6546 = relay.TupleGetItem(func_2995_call(), 1)
output = call_6545
output2 = call_6546
func_6549 = relay.Function([], output)
mod['func_6549'] = func_6549
mod = relay.transform.InferType()(mod)
mutated_mod['func_6549'] = func_6549
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6549_call = mutated_mod.get_global_var('func_6549')
call_6550 = func_6549_call()
output = call_6550
func_6551 = relay.Function([], output)
mutated_mod['func_6551'] = func_6551
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4684_call = mod.get_global_var('func_4684')
func_4686_call = mutated_mod.get_global_var('func_4686')
call_6594 = relay.TupleGetItem(func_4684_call(), 0)
call_6595 = relay.TupleGetItem(func_4686_call(), 0)
func_5795_call = mod.get_global_var('func_5795')
func_5798_call = mutated_mod.get_global_var('func_5798')
const_6620 = relay.const([-4.052370,7.877701,-9.350863,2.473054,-9.494655,-0.382237,4.590035,-2.598526,8.151144,9.026959,8.783630,-0.587285,9.315517,7.189642,7.571219,3.279258,-5.949791,7.387996,8.709246,9.794219,1.954374,-0.327844,-3.922920,-3.054412,-6.696129,5.647719,-1.921993,-3.761484,-2.547236,-7.063552,-3.305647,-5.284232,9.164645,7.139922,-0.450308,-1.139851,9.567755,-8.643167,8.018274,0.159193,-9.986100,-6.224050,4.432531,-4.857148,-2.139456,4.737680,4.399922,-0.582519,-9.589048,8.151886,-0.622881,-1.261490,-7.518352,3.883228,-6.661115,9.581742,6.861064,3.555087,-2.057294,3.041352,3.511472,4.823063,-3.607417,0.382825,-5.338429,7.351042,-2.063782,-1.575175,-7.231272,3.099469,-7.909393,-7.284073,-5.975043,-0.241036,2.585737,3.577298,9.855244,1.811155,-3.423964,-0.906739,6.401310,-1.444297,2.403349,5.541049,-5.935875,-8.601021,1.392193,7.127585,1.266163,9.369022,7.310146,7.150705,1.940529,-7.880222,9.543196,-1.612605,-6.659794,-7.275701,2.540866,3.200819,-5.400131,2.595186,-6.558767,1.473854,-7.353405,1.057754,-0.969696,-6.255897,7.365651,5.588726,2.199395,-5.228367,-1.618032,-0.432350,-9.212663,-8.963277,6.167429,-3.069416,-6.609994,6.293049,-2.353942,-0.364697,9.889298,8.238302,9.166848,3.307017,-9.250428,-6.168503,0.310941,8.690317,-4.729262,-0.517286,7.004827,-1.389497,6.261912,-0.089181,-9.735771,-7.773809,-7.159557,-9.424549,-6.176325,-1.524188,6.587021,-4.550540,3.576073,-7.355837,8.842643,-9.741165,-2.019035,-5.981088,-1.191372,0.881289,8.818860,2.952426,6.621371,1.198657,5.494817,3.945177,-3.215900,5.702903,9.835311,1.389585,8.044273,1.170652,-4.117287,5.201607,-8.980527,7.103602,-6.965804,8.122146,5.001352,3.496635,9.376196,6.652448,-8.287753,5.702775,8.426856,-3.419394,-0.419913,-2.075645,8.590607,-9.212138,-8.098453,7.465321,-6.536819,2.006869,0.119996,-9.015905,6.247503,-3.366077,0.329641,7.677722,7.105713,2.827312,4.862886,-7.495430,0.177583,-0.579193,4.867591,-4.666138,8.442812,0.080115,-4.858131,8.764489,2.533550,-1.704334,2.865713,6.725401,6.124948,1.354663,-5.292384,-9.161627,-9.818429,-1.226936,-3.166602,9.231284,-4.353226,1.853174,-2.163627,-3.530475,-2.589262,-1.476946,-2.315017,-4.196653,-1.854345,-6.396532,-5.059919,-1.262888,6.196909,-4.988569,7.643077,4.571468,-2.752639,3.734720,5.577898,-1.539944,-5.565757,-3.148889,2.831432,-3.260803,-1.054095,-4.675577,2.167444,4.393584,6.572313,3.619808,0.430677,-8.218087,2.570322,-0.970290,3.665137,-6.699052,-1.960334,-9.048181,-7.179012,6.711125,9.788899,7.580254,5.129435,-8.671335,-6.272176,4.092136,-3.852752,3.513171,4.033301,2.327919,-7.979608,-3.529395,-8.723168,-0.878882,-5.870152,4.532977,-0.887103,-0.883852,8.900356,-2.519249,-2.865517,1.145628,-1.545934,-3.095451], dtype = "float32")#candidate|6620|(280,)|const|float32
var_6621 = relay.var("var_6621", dtype = "uint8", shape = (42, 4))#candidate|6621|(42, 4)|var|uint8
call_6619 = relay.TupleGetItem(func_5795_call(relay.reshape(const_6620.astype('float32'), [1, 280]), relay.reshape(var_6621.astype('uint8'), [168,]), ), 3)
call_6622 = relay.TupleGetItem(func_5798_call(relay.reshape(const_6620.astype('float32'), [1, 280]), relay.reshape(var_6621.astype('uint8'), [168,]), ), 3)
uop_6635 = relay.sin(var_6621.astype('float32')) # shape=(42, 4)
output = relay.Tuple([call_6594,call_6619,const_6620,uop_6635,])
output2 = relay.Tuple([call_6595,call_6622,const_6620,uop_6635,])
func_6643 = relay.Function([var_6621,], output)
mod['func_6643'] = func_6643
mod = relay.transform.InferType()(mod)
var_6644 = relay.var("var_6644", dtype = "uint8", shape = (42, 4))#candidate|6644|(42, 4)|var|uint8
output = func_6643(var_6644)
func_6645 = relay.Function([var_6644], output)
mutated_mod['func_6645'] = func_6645
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2459_call = mod.get_global_var('func_2459')
func_2461_call = mutated_mod.get_global_var('func_2461')
call_6652 = relay.TupleGetItem(func_2459_call(), 0)
call_6653 = relay.TupleGetItem(func_2461_call(), 0)
func_4099_call = mod.get_global_var('func_4099')
func_4101_call = mutated_mod.get_global_var('func_4101')
var_6664 = relay.var("var_6664", dtype = "float32", shape = (60,))#candidate|6664|(60,)|var|float32
call_6663 = relay.TupleGetItem(func_4099_call(relay.reshape(var_6664.astype('float32'), [2, 6, 5])), 0)
call_6665 = relay.TupleGetItem(func_4101_call(relay.reshape(var_6664.astype('float32'), [2, 6, 5])), 0)
output = relay.Tuple([call_6652,call_6663,var_6664,])
output2 = relay.Tuple([call_6653,call_6665,var_6664,])
func_6666 = relay.Function([var_6664,], output)
mod['func_6666'] = func_6666
mod = relay.transform.InferType()(mod)
var_6667 = relay.var("var_6667", dtype = "float32", shape = (60,))#candidate|6667|(60,)|var|float32
output = func_6666(var_6667)
func_6668 = relay.Function([var_6667], output)
mutated_mod['func_6668'] = func_6668
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5569_call = mod.get_global_var('func_5569')
func_5571_call = mutated_mod.get_global_var('func_5571')
call_6724 = func_5569_call()
call_6725 = func_5569_call()
func_6471_call = mod.get_global_var('func_6471')
func_6473_call = mutated_mod.get_global_var('func_6473')
call_6759 = relay.TupleGetItem(func_6471_call(), 0)
call_6760 = relay.TupleGetItem(func_6473_call(), 0)
output = relay.Tuple([call_6724,call_6759,])
output2 = relay.Tuple([call_6725,call_6760,])
func_6783 = relay.Function([], output)
mod['func_6783'] = func_6783
mod = relay.transform.InferType()(mod)
mutated_mod['func_6783'] = func_6783
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6783_call = mutated_mod.get_global_var('func_6783')
call_6784 = func_6783_call()
output = call_6784
func_6785 = relay.Function([], output)
mutated_mod['func_6785'] = func_6785
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3200_call = mutated_mod.get_global_var('func_3200')
call_6813 = func_3198_call()
call_6814 = func_3198_call()
var_6821 = relay.var("var_6821", dtype = "float32", shape = (11, 12, 16))#candidate|6821|(11, 12, 16)|var|float32
bop_6822 = relay.greater_equal(call_6813.astype('bool'), relay.reshape(var_6821.astype('bool'), relay.shape_of(call_6813))) # shape=(11, 12, 16)
bop_6825 = relay.greater_equal(call_6814.astype('bool'), relay.reshape(var_6821.astype('bool'), relay.shape_of(call_6814))) # shape=(11, 12, 16)
output = relay.Tuple([bop_6822,])
output2 = relay.Tuple([bop_6825,])
func_6828 = relay.Function([var_6821,], output)
mod['func_6828'] = func_6828
mod = relay.transform.InferType()(mod)
mutated_mod['func_6828'] = func_6828
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6829 = relay.var("var_6829", dtype = "float32", shape = (11, 12, 16))#candidate|6829|(11, 12, 16)|var|float32
func_6828_call = mutated_mod.get_global_var('func_6828')
call_6830 = func_6828_call(var_6829)
output = call_6830
func_6831 = relay.Function([var_6829], output)
mutated_mod['func_6831'] = func_6831
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_6910 = func_2016_call()
call_6911 = func_2016_call()
output = relay.Tuple([call_6910,])
output2 = relay.Tuple([call_6911,])
func_6918 = relay.Function([], output)
mod['func_6918'] = func_6918
mod = relay.transform.InferType()(mod)
output = func_6918()
func_6919 = relay.Function([], output)
mutated_mod['func_6919'] = func_6919
mutated_mod = relay.transform.InferType()(mutated_mod)
var_6959 = relay.var("var_6959", dtype = "float64", shape = (16, 12, 10))#candidate|6959|(16, 12, 10)|var|float64
uop_6960 = relay.log2(var_6959.astype('float64')) # shape=(16, 12, 10)
func_5813_call = mod.get_global_var('func_5813')
func_5816_call = mutated_mod.get_global_var('func_5816')
var_6993 = relay.var("var_6993", dtype = "float64", shape = ())#candidate|6993|()|var|float64
call_6992 = func_5813_call(relay.reshape(var_6993.astype('float64'), []))
call_6994 = func_5813_call(relay.reshape(var_6993.astype('float64'), []))
func_2092_call = mod.get_global_var('func_2092')
func_2095_call = mutated_mod.get_global_var('func_2095')
var_7008 = relay.var("var_7008", dtype = "bool", shape = (5250,))#candidate|7008|(5250,)|var|bool
call_7007 = relay.TupleGetItem(func_2092_call(relay.reshape(var_7008.astype('bool'), [525, 10])), 1)
call_7009 = relay.TupleGetItem(func_2095_call(relay.reshape(var_7008.astype('bool'), [525, 10])), 1)
output = relay.Tuple([uop_6960,call_6992,var_6993,call_7007,var_7008,])
output2 = relay.Tuple([uop_6960,call_6994,var_6993,call_7009,var_7008,])
func_7013 = relay.Function([var_6959,var_6993,var_7008,], output)
mod['func_7013'] = func_7013
mod = relay.transform.InferType()(mod)
var_7014 = relay.var("var_7014", dtype = "float64", shape = (16, 12, 10))#candidate|7014|(16, 12, 10)|var|float64
var_7015 = relay.var("var_7015", dtype = "float64", shape = ())#candidate|7015|()|var|float64
var_7016 = relay.var("var_7016", dtype = "bool", shape = (5250,))#candidate|7016|(5250,)|var|bool
output = func_7013(var_7014,var_7015,var_7016,)
func_7017 = relay.Function([var_7014,var_7015,var_7016,], output)
mutated_mod['func_7017'] = func_7017
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_7137 = func_4118_call()
call_7138 = func_4118_call()
var_7149 = relay.var("var_7149", dtype = "bool", shape = (525, 13))#candidate|7149|(525, 13)|var|bool
bop_7150 = relay.logical_xor(call_7137.astype('uint64'), var_7149.astype('uint64')) # shape=(525, 13)
bop_7153 = relay.logical_xor(call_7138.astype('uint64'), var_7149.astype('uint64')) # shape=(525, 13)
output = relay.Tuple([bop_7150,])
output2 = relay.Tuple([bop_7153,])
func_7156 = relay.Function([var_7149,], output)
mod['func_7156'] = func_7156
mod = relay.transform.InferType()(mod)
var_7157 = relay.var("var_7157", dtype = "bool", shape = (525, 13))#candidate|7157|(525, 13)|var|bool
output = func_7156(var_7157)
func_7158 = relay.Function([var_7157], output)
mutated_mod['func_7158'] = func_7158
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_7183 = func_2910_call()
call_7184 = func_2910_call()
func_3260_call = mod.get_global_var('func_3260')
func_3263_call = mutated_mod.get_global_var('func_3263')
const_7206 = relay.const([0.923947,1.837322,-7.548953,-0.625585,3.761595,0.798096,0.076423,-8.004298,-9.745354,0.761043,-3.576446,-2.670970,8.529680,2.463551,4.808080,4.311137,8.533749,-0.022996,2.906834,-5.258409,-2.108044,-3.693091,-4.806657,9.866481,-8.015596,6.444758,3.815441,6.473335,-0.488268,6.675336,-6.693252,4.372429,8.414618,4.571376,-8.632702,8.941017,5.596925,-6.575817,-0.755814,1.557516,-3.493983,1.350921,-7.210847,-3.654299,-3.045712,-4.803020,3.026281,-2.510320,-8.944012,4.037644,0.360950,6.393589,-3.231533,-3.781691,3.655614,-5.310533,6.285324,7.781854,-0.277715,-2.284832,-3.960467,3.181641,-4.931890,-4.609652,4.204182,-7.410590,3.652337,7.355306,1.763276,-0.363067,0.722022,3.981361,3.600070,-5.055213,-0.126200,-2.715275,-9.633334,-6.190330,7.230488,7.057177,2.463820,6.742767,8.800655,-0.112317,9.446820,-8.927427,7.382442,7.322003,-1.053151,-8.203832,-0.046140,9.090795,-6.171875,-5.508282,6.823763,-1.855212,7.619679,7.991871,9.756565,9.181216,-3.109889,9.043650,2.535861,-8.862095,3.932119,7.794865,9.672299,-8.553406,-1.521558,3.718488,-9.030048,-8.682398,-7.142929,-6.970153,-8.760861,-7.742143,3.257438,-6.202430,-9.995074,9.764156,-0.675474,3.199804,8.333689,5.776023,-4.594049,8.987453,8.313628,-0.160862,6.346955,6.562719,8.881500,5.760437,6.056042,3.970382,-1.071962,5.570717,7.966651,2.613136,-0.594212,0.496199,7.796721,4.004531,-2.294852,-7.534589,8.325188,6.726250,2.112049,8.119477,2.764736,-1.565922,2.937708,-8.049614,8.204837,-3.054282,-2.552792,-9.272345,-7.288843,-8.565826,-1.977784,3.913499,-0.857218,-8.904521,0.731480,2.820023,-7.627229,-2.909589,9.263865,0.050206,-1.205871,6.099879,9.529212,2.867014,7.394017,-3.445595,-7.619069,3.566742,2.020003,0.944187,-8.840379,3.530488,-6.323345,-6.849572,-7.943013,-6.138289,5.533384,8.665717,-3.119423,7.464712,1.957545,5.293904,4.227748,-8.304476,-9.838874,5.684840,-4.893320,2.477009,-0.642445,3.142818,3.627416,-4.098549,4.857863,0.369119,-7.592985,7.403026,1.759465,5.620795,-5.264220,5.389131,6.906040,7.711005,4.232158,8.499778,-5.452675,-5.427352,-0.474272,8.595317,-2.511330,6.191659,7.253135,-9.791345,5.622033,5.400302,-7.076414,-6.735536,4.790069,6.019214,6.483379,-7.552181,5.968942,7.266650,3.212359,0.240574,-2.516834,-2.557940,-5.914988,-2.165001,6.446109,4.826625,-0.030440,6.959214,4.819462,-5.308022,3.546971,-7.200660,2.456309,9.216381,-3.226627,-9.421114,3.151721,-5.100338,-6.697265,-7.304635,-4.078614,0.041883,6.336440,-7.933632,4.205368,7.546989,-1.594515,-0.198558,-2.475412,-9.471828,-6.771658,2.611197,-1.596457,0.447316,-3.752057,-2.265933,5.270062,4.421889,-8.925169,2.309629,-5.157361,7.192176,9.156852,-1.135920,2.183722,-0.824279,2.009950,4.026003,-5.941496,-6.352588,-3.891326,6.053301,-1.934951,9.483322,9.381568,3.352655,6.652189,-8.595792,-8.580991,-6.427704,3.962184,9.719736,-4.711142,-5.274712,-2.877518,7.832883,4.504369,-1.706607,5.148684,9.492062,1.184454,-1.677685,2.216844,6.589651,1.948810,7.437866,-3.133476,-8.503408,5.252068,6.934798,8.109856,7.833380,-7.971592,4.122681,1.703925,-8.638826,6.554289,2.458493,7.496117,-3.222308,4.358249,3.028667,-4.135910,-3.860765,1.242765,0.052722,6.997502,0.643494,5.613440,3.452424,1.898827,8.190885,7.068752,5.890578,3.850255,6.654530,3.931826,-2.631074,-7.740157,-3.744709,1.288540,5.578434,-9.058483,-6.044790,2.666853,-4.648660,8.620898,6.928935,-3.800589,4.045040,-8.284857,-3.330652,3.140372,6.601757,-9.741099,5.860883,-0.905311,-1.771072,-0.765689,-6.455554,-1.219179,-0.807083,-3.892569,-8.555373,5.751656,-5.943479,6.416551,3.440807,1.144592,-4.853722,-9.982805,8.748349,-1.302364,6.000663,-8.611007,-4.705661,-2.042575,-2.725328,-5.337050,-0.300861,-2.235922,0.786405,4.205205,8.326591,-6.391191,-8.537748,1.048889,3.715704,5.777669,-6.817143,-6.236468,1.070032,-8.829654,2.736497], dtype = "float64")#candidate|7206|(396,)|const|float64
call_7205 = relay.TupleGetItem(func_3260_call(relay.reshape(const_7206.astype('float64'), [66, 6])), 1)
call_7207 = relay.TupleGetItem(func_3263_call(relay.reshape(const_7206.astype('float64'), [66, 6])), 1)
func_6509_call = mod.get_global_var('func_6509')
func_6511_call = mutated_mod.get_global_var('func_6511')
var_7209 = relay.var("var_7209", dtype = "float32", shape = (728,))#candidate|7209|(728,)|var|float32
call_7208 = relay.TupleGetItem(func_6509_call(relay.reshape(var_7209.astype('float32'), [4, 13, 14])), 1)
call_7210 = relay.TupleGetItem(func_6511_call(relay.reshape(var_7209.astype('float32'), [4, 13, 14])), 1)
func_1234_call = mod.get_global_var('func_1234')
func_1237_call = mutated_mod.get_global_var('func_1237')
const_7223 = relay.const([10,4,-5,-7,10,-4,8,2,10,9,2,4,-8,-7,5,-6,7,1,2,2,4,9,-2,7,-3,-5,-4,-4,-9,9,-6,-1,4,3,-1,-10,-5,-9,1,10,-4,-8,-5,3,5,8,-6,4,-2,-7,-4,-8,-7,-7,-2,-2,-5,5,5,1,-9,-1,7,-6,-2,2,2,-8,-6,5,3,4,-8,-7,-6,-2,9,-1,-9,-7,-10,9,-8,10,2,-10,1,-3,5,-1,-10,8,-6,-10,-6,4,-6,9,-7,-6,4,-4,-3,3,8,-9,-7,-2,7,-6,6,10,-4,-6,10,10,1,7,2,2,-6,-10,9,5,-3,9,-2,3,-10,7,-2,-1,2,7,-2,5,1,10,-9,-5,8,2,-5,-6,-4,6,-9,-9,9,-6,-6,-8,8,6,-4,8,7,2,4,8,10,-2,-2,-1,-8,1,-9,10], dtype = "uint8")#candidate|7223|(168,)|const|uint8
call_7222 = relay.TupleGetItem(func_1234_call(relay.reshape(const_7223.astype('uint8'), [168, 1])), 1)
call_7224 = relay.TupleGetItem(func_1237_call(relay.reshape(const_7223.astype('uint8'), [168, 1])), 1)
func_1234_call = mod.get_global_var('func_1234')
func_1237_call = mutated_mod.get_global_var('func_1237')
call_7226 = relay.TupleGetItem(func_1234_call(relay.reshape(call_7222.astype('uint8'), [168, 1])), 1)
call_7227 = relay.TupleGetItem(func_1237_call(relay.reshape(call_7222.astype('uint8'), [168, 1])), 1)
output = relay.Tuple([call_7183,call_7205,const_7206,call_7208,var_7209,call_7222,const_7223,call_7226,])
output2 = relay.Tuple([call_7184,call_7207,const_7206,call_7210,var_7209,call_7224,const_7223,call_7227,])
func_7228 = relay.Function([var_7209,], output)
mod['func_7228'] = func_7228
mod = relay.transform.InferType()(mod)
mutated_mod['func_7228'] = func_7228
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7229 = relay.var("var_7229", dtype = "float32", shape = (728,))#candidate|7229|(728,)|var|float32
func_7228_call = mutated_mod.get_global_var('func_7228')
call_7230 = func_7228_call(var_7229)
output = call_7230
func_7231 = relay.Function([var_7229], output)
mutated_mod['func_7231'] = func_7231
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5777_call = mod.get_global_var('func_5777')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_7274 = relay.TupleGetItem(func_5777_call(), 0)
call_7275 = relay.TupleGetItem(func_5779_call(), 0)
func_2910_call = mod.get_global_var('func_2910')
func_2912_call = mutated_mod.get_global_var('func_2912')
call_7280 = func_2910_call()
call_7281 = func_2910_call()
const_7292 = relay.const([[[6.010984,-9.099837,-4.635914,8.215689,-3.755746,2.904483,2.903434,-9.039622,9.514130,-8.247080,-6.037728,8.104619,6.411466,9.562342,-5.972783,-1.526905],[4.411979,9.048344,-4.520765,3.800733,0.277757,-3.632488,-8.553469,1.164314,-4.248151,9.385750,-7.770432,3.423587,4.508190,-8.865159,-8.826372,-4.233529],[0.870234,0.819319,-8.143290,-4.308964,1.240320,-2.657885,5.896396,2.642748,9.806395,-2.954977,9.633301,-8.567430,3.492243,-3.657459,4.952733,4.529396],[5.159070,-9.460204,-3.253482,1.035243,3.895872,5.083133,7.145843,-4.014550,-2.184820,-0.709986,6.987566,-4.266858,5.654666,-4.176592,8.050398,7.635044],[-4.263703,8.506765,1.411023,-7.837137,-2.486523,3.504252,-8.207544,4.825486,5.236816,-2.069912,-6.017736,9.938906,0.041950,-4.273651,8.563758,9.701867],[8.153181,-1.763906,5.843911,2.343234,8.483497,-3.579186,1.472843,-7.459484,3.567086,7.321931,8.533392,-9.305706,-1.615014,-9.899225,-2.926618,2.632660],[-0.485244,-0.703442,-8.925371,9.236222,4.716409,5.249649,9.952991,7.967806,-0.486102,-9.567355,2.940687,-0.977723,9.799321,4.713173,1.951214,2.454507],[6.739222,9.059062,-3.409541,0.812789,-4.013517,-7.854524,-2.592177,5.129646,-3.896991,-2.897830,-4.821552,3.378383,2.391608,1.633966,1.348555,-8.986996],[1.830725,-4.919166,8.956057,6.927206,-5.510036,3.453484,3.307188,1.782062,8.532145,9.085518,-8.610365,8.234231,7.021644,-2.953750,-4.143477,8.829508],[4.136746,3.065810,3.618063,-1.373755,-4.792107,-8.090468,-2.896529,1.490627,-2.301922,7.049197,7.481808,-9.452737,-5.740367,2.796696,-8.228557,-4.440492],[-8.680834,-8.676922,-9.728319,5.869910,-8.599659,-4.959076,6.909657,-6.435800,-5.944772,-2.517898,8.534726,-9.529275,-0.960733,-7.938751,0.285715,-3.436870],[-9.038386,3.056346,0.511472,9.583860,3.910005,9.522191,8.086867,-9.445998,8.684690,4.569764,3.891828,-7.559948,8.833633,-6.597497,8.199764,-2.847253]],[[0.030539,-0.961555,-7.601010,6.913490,9.782602,-5.524022,-4.699465,-1.758554,3.206456,-0.653745,-8.144396,-3.651602,1.810550,-1.612922,4.700229,-6.356771],[-3.416287,-6.631831,-1.417516,-1.483082,-4.011691,-1.799351,2.294038,-9.888902,-6.339645,-5.603539,-3.929385,-9.480054,8.715922,-0.926968,0.213757,-2.923709],[-3.211419,-9.281052,-8.899633,-8.360100,6.192256,9.053789,-1.152885,-8.812429,0.459431,2.833736,6.349799,9.835289,-4.878595,-7.980543,2.335731,4.277251],[2.119274,-0.591188,7.978508,-6.835397,-5.516459,8.997435,9.143989,1.038043,-4.590496,-1.942076,2.893317,5.665962,-1.922834,1.635462,-8.489462,2.781328],[7.368132,9.223609,-9.933408,8.214308,8.596758,0.933536,-0.724151,8.805497,1.821651,3.325307,-0.641348,-5.396883,-0.692902,-6.653835,9.609482,-1.043063],[4.430292,6.313833,4.405128,-1.428005,8.975061,4.055071,2.873097,1.290451,7.372520,9.701258,4.404818,-4.485774,6.992433,-1.598683,-0.088167,5.813687],[-2.613514,2.089364,-3.801601,-6.052216,-3.262271,6.027927,6.366522,-5.110750,2.339868,-8.086180,-9.995746,-3.764307,3.152277,-9.380245,6.200803,4.242825],[-8.122737,2.318759,9.825609,-1.045739,-7.209906,8.431164,-1.494393,-1.748363,8.964518,-1.186112,4.833506,9.178126,3.655290,-6.167147,-1.721632,-3.503780],[-5.241103,4.077909,-1.654101,1.941417,7.939391,-6.813686,3.480690,-3.135038,6.982283,-0.916938,8.241803,7.069588,7.524445,-4.395321,0.062025,-2.594063],[-9.968229,9.553169,9.247454,0.645109,9.448946,5.996218,-8.288366,4.543218,-5.968922,-5.139223,-0.808019,9.255180,1.801765,4.236705,-2.067025,5.116887],[4.735624,1.658166,4.383830,1.900837,-2.399984,0.793558,-3.784354,-8.166083,-5.560717,9.304765,-5.956467,-1.439151,-3.262339,5.421410,0.374356,1.647037],[5.851202,-8.811784,-7.842342,-5.084735,-2.281603,0.007048,-0.111727,5.266730,7.495091,6.102035,1.433617,3.512081,9.786701,6.160815,2.498609,4.456934]],[[9.715630,-3.480132,-0.762446,0.124557,-1.027976,1.245236,-3.664553,-8.177567,8.470218,-0.114293,9.062396,-4.335142,-9.276047,-2.658942,3.896521,-6.509715],[8.539237,-2.638182,6.961959,-7.158520,-8.642366,6.357529,-2.352626,-2.754386,7.110542,7.848392,7.584158,-7.493712,9.341813,9.088173,-0.030095,1.767878],[-7.770372,1.676025,2.984097,-8.935137,-8.418056,6.282427,0.090353,-1.584645,-9.039455,0.399653,-6.410351,7.521515,-5.788446,-5.303819,-4.413282,-6.857231],[7.199469,6.779983,4.687202,-5.682498,4.722205,8.638526,-0.877001,2.404863,2.723064,-9.152125,-0.159275,8.178850,-2.902290,-0.724891,4.418411,-2.287508],[-7.257689,-2.559725,4.215669,4.925537,-2.371771,1.139113,4.606621,5.528606,0.730384,-9.916366,0.811717,2.091149,1.485580,-6.883987,-4.723195,9.275801],[-7.928581,3.408174,-8.677325,-5.628998,4.492790,6.618695,3.206779,1.646644,-4.362047,-2.272115,2.918085,-4.626469,0.443095,0.131511,9.843028,9.860534],[-4.066900,2.250466,5.342357,5.192691,5.517377,2.718285,4.729108,8.048473,-3.589107,9.706876,9.927649,-0.817548,8.184793,9.334470,-8.292966,-9.374008],[9.549292,-1.075463,-5.272286,6.715931,-1.101054,-5.105243,3.700116,-1.654580,6.325480,5.278762,5.789999,-8.897174,7.644043,7.212969,-8.184173,7.473599],[4.378952,-2.214053,1.350546,3.675432,2.651302,-0.927177,2.998971,-4.369801,-6.939155,-8.299000,-0.068056,-4.114488,-1.245165,1.898089,-2.511808,-0.896125],[-1.354842,4.670291,-1.456227,-3.539561,-8.574753,-6.802278,3.011592,-8.852611,-0.537523,9.365931,3.953312,-7.675550,1.960756,-2.708791,-0.873636,1.011886],[-0.578667,8.252957,7.681863,-2.493777,-8.427181,1.879397,8.576733,9.759854,-9.951047,-3.108400,8.272509,0.238578,5.420762,-0.062659,-9.577978,-7.786349],[-5.960845,2.277495,3.115524,4.985871,-4.000646,6.446374,-1.628449,2.862159,8.519275,7.167349,8.138164,0.666211,-9.019080,-5.236516,6.699880,0.513298]],[[-7.363781,7.187513,-3.484639,9.691841,-4.138114,9.534972,-4.815060,5.494651,-6.955802,-5.569357,-8.247955,-3.699076,5.820701,7.871971,-5.533867,-1.905471],[-4.131521,-4.887214,-8.222822,7.393701,6.173085,0.179005,-7.701184,2.103328,4.638533,-2.145780,-5.611356,4.334543,1.791777,-3.240870,8.506038,0.829150],[3.730292,2.635799,4.051043,-3.923499,4.067525,-9.527554,-8.867821,-9.688869,5.350581,4.712380,-9.758909,0.581238,-5.884587,9.608757,-0.554761,5.941259],[-5.009836,1.664905,8.104039,-3.541247,-2.775191,-7.215396,4.426055,-7.227123,7.509604,-5.170266,-1.852467,-8.301960,4.643114,3.225153,-4.789021,9.643458],[7.834441,-4.513547,-8.064751,9.418725,-6.365898,-2.285076,-8.614244,-5.933476,-6.098155,3.842759,7.832783,7.285792,3.431562,-8.895943,6.990567,3.402148],[9.835866,-9.179266,-0.735166,-3.945140,7.839384,-5.477695,2.050734,-0.194312,7.824309,9.631688,5.776219,-5.064670,9.312375,-7.570999,-9.793793,7.495938],[9.508654,-6.177380,1.454057,-0.904209,0.850411,-6.009187,-9.988041,-4.186260,0.817183,-2.135079,0.173820,5.468253,6.115878,5.509097,5.756596,7.325658],[-8.515156,7.620631,-0.472403,4.828897,-1.850053,8.952142,-9.019959,8.045773,1.900033,-4.878498,-5.474000,4.906605,7.858230,6.036690,5.740416,8.820112],[-2.965422,4.372670,8.058430,-0.905186,-9.788631,-3.133605,-7.949802,-3.248858,2.653176,-2.298221,7.194725,7.762050,-6.431948,0.401541,-2.519610,-7.539959],[4.051565,4.860173,-0.095598,5.705890,0.168314,8.085101,0.130054,5.500197,-8.783030,-3.080383,9.035954,-7.383355,-4.860636,5.351104,-1.847167,-5.186902],[0.122352,-4.531802,0.886801,6.442963,3.217060,-2.997404,-6.966391,6.446552,6.320958,-9.403853,-3.394108,0.323002,4.836496,5.733099,-8.449919,7.542081],[5.919122,3.515376,9.798454,-0.396610,0.337255,5.821857,-3.478896,-5.477038,-0.047083,6.820723,4.211610,-9.323538,0.983840,-3.354506,1.887927,-3.925640]],[[-6.706934,9.394667,-2.675700,-7.112499,0.756421,5.345514,7.366829,8.363649,0.726152,-6.835224,6.418404,5.673840,-3.959300,-8.862580,1.001833,-0.609492],[-2.985880,-6.830347,0.491469,-3.701708,-1.382832,2.184508,0.661861,-4.420519,6.793971,1.592607,0.684835,5.043755,7.809600,8.266219,-6.858273,-4.229982],[9.477532,3.360641,3.589939,2.734443,-1.410382,0.989412,-6.450012,-1.915400,-0.748750,-9.902111,-5.944473,0.416520,-9.444366,-3.400953,6.840725,9.969306],[5.588453,1.231590,8.991435,3.467508,0.813356,9.533490,-9.039012,8.244643,-0.249589,-0.714330,-8.678159,-1.811905,-7.390738,1.553667,4.578826,-3.166906],[-2.960882,2.036147,8.561532,7.558967,-5.804324,-9.052443,-7.953460,5.214497,5.080772,6.788925,-7.764448,-0.825842,-8.159492,-9.164761,6.741294,2.223985],[-0.520042,2.450940,5.373855,7.473962,8.328754,-7.173697,6.440414,-8.970799,2.029468,-4.424733,6.315730,-0.633019,9.611080,6.438533,7.529660,-1.870219],[-3.647104,8.136723,-6.964787,0.187261,-3.878539,5.318070,0.460837,4.425577,8.201088,-6.996664,-1.452853,-2.961476,4.325936,-3.762063,-7.341714,5.844074],[-2.226016,-1.192680,1.338973,2.091669,7.145912,9.027897,-3.880864,6.345904,2.294876,4.950274,-8.389283,0.569904,1.240382,7.899865,-6.725004,-9.600040],[6.206298,9.633483,-6.558985,1.512020,3.419572,3.597957,3.875286,9.097886,-3.344275,-6.399041,-0.220784,8.717161,-6.026267,-4.143460,3.337260,9.026440],[8.747612,6.275417,8.296558,-2.746282,3.656592,2.404743,-8.865647,5.013510,2.175709,-7.719409,8.929236,2.116234,-8.940022,-9.887978,9.086343,-6.335886],[-8.254337,-7.103467,-2.465334,-8.079153,-2.205920,-9.360877,-3.043633,-0.635766,-4.487029,-4.498215,-7.847684,1.079289,7.293632,-7.274591,8.706159,6.016708],[-2.846324,-2.642446,-8.521902,-4.415195,-5.464854,-0.589864,3.965043,-6.730781,9.147700,0.836294,-6.622839,-0.631361,1.595212,-7.988224,7.411279,-7.301343]],[[-7.755451,2.673034,-2.407583,0.555942,-3.273641,7.349957,-3.071729,6.408748,-3.850524,7.304809,9.701992,-8.373773,-3.679340,-8.863632,8.501220,5.043812],[6.659870,-3.527814,2.590280,-7.229985,4.497298,1.921892,3.425432,7.465168,9.941610,-3.748163,-4.657176,8.595877,-8.423789,4.701912,4.104354,3.993185],[4.486090,-6.178595,4.100092,-1.438765,-9.871563,9.162354,1.988118,-9.703844,0.488759,0.356079,3.648105,4.813914,-1.800682,5.090294,1.008218,-8.167058],[8.864436,0.804866,9.960121,4.771797,7.376563,6.096997,-1.259224,-9.726392,2.080111,0.428245,-7.927897,-3.841391,0.985958,-7.254953,-7.464980,9.530827],[4.265043,-6.614062,0.333198,3.350281,-7.168182,0.599408,-7.039808,1.270221,5.564491,-0.015780,6.032402,0.931032,6.411154,4.222075,-8.826254,1.966953],[-3.596063,6.817154,6.663598,-6.983496,1.204597,-7.092612,4.818070,6.440632,1.990936,5.556887,-2.847268,9.820868,-5.277693,0.195467,-0.527063,9.766475],[1.593837,-6.354005,8.045997,-3.939003,-5.155541,-5.639254,-5.004416,-2.217872,0.149763,-0.418673,-4.087233,0.318929,1.408754,-9.898455,2.966127,-8.279689],[-4.962386,-9.644765,7.290926,-0.652223,6.058713,-1.984696,8.098543,5.556538,-3.990399,-1.795818,-3.963405,9.542163,5.766186,5.509750,8.290228,2.630178],[-0.503922,3.480570,-6.190152,0.946213,-0.546107,-3.549578,-0.011560,8.830978,7.919441,-1.743763,4.256175,0.198042,5.260529,-8.019583,-9.466618,-9.188352],[7.041159,7.164520,8.216735,8.115704,-1.056383,1.797576,-1.841177,0.743067,4.406957,7.401643,3.502743,0.861433,8.778491,-3.343441,8.042300,-5.475208],[-2.907441,-9.061365,-5.461074,-1.903615,4.990750,0.808908,-3.145520,-0.415065,-4.482460,-6.691561,-2.160356,-0.179737,6.048055,-8.247857,4.823127,3.673122],[-2.753921,-7.531986,-5.845026,2.874155,-6.483528,2.806564,8.362054,-1.531247,1.704015,9.365729,-1.750932,8.656714,-8.470715,-9.569318,-9.533128,-0.797380]],[[-3.179440,6.113473,3.195964,-9.054454,7.689013,-2.847171,2.126499,7.349952,9.402106,3.081895,-7.564566,-2.815144,-4.292821,9.219463,-1.527119,3.567495],[-4.719941,0.805136,6.947354,0.068801,7.201583,4.389380,9.598104,4.438944,0.279662,-6.046660,5.902395,5.428253,-4.039180,-6.288446,-4.432796,1.995118],[-4.574253,-5.893342,-3.717937,9.447159,7.324530,5.255098,7.609935,0.330409,5.659570,-0.402618,-2.904388,-5.285535,-4.021438,-1.831226,-0.014969,2.613412],[-1.982181,-2.809609,-9.051000,6.011592,-5.558131,-7.536749,6.073264,-1.283718,7.435757,-3.188689,-3.015253,-3.817386,4.959949,6.283631,-2.138954,6.291773],[-1.515659,-2.121850,5.876740,-1.530923,-2.293355,8.851041,0.111364,-0.324627,-2.467605,-1.115395,1.641802,-1.851534,1.694545,-5.975861,-9.072625,7.707116],[4.849566,2.674930,6.847085,-8.328990,-2.249817,0.467484,1.306546,5.049492,-3.764625,0.940615,-7.573967,5.495855,4.651566,-2.959233,6.339157,3.576175],[4.230300,5.980228,-6.171830,-0.845340,4.393116,-3.230403,8.657418,-9.564553,-0.612868,4.158172,5.895649,-8.409273,-8.888414,8.642318,-0.247114,-3.366387],[0.616239,-1.790264,3.760044,9.900488,8.625189,5.804236,4.634175,-2.599181,0.823264,-9.050335,-5.319090,-3.422890,6.840479,-5.908210,-8.838302,1.686384],[-5.670152,8.931784,-3.605411,-3.093855,2.355914,-0.657929,-4.165750,-7.133192,-7.774716,-1.332278,6.034643,1.570078,-9.304263,1.446723,-1.909517,3.697423],[-5.957835,-1.791301,9.980292,-2.062489,1.082319,9.092501,-7.599996,4.801426,-7.521749,0.921426,-1.696618,9.342135,8.824845,0.988949,9.021086,-4.911889],[-2.778898,5.977008,-0.001330,-8.081330,-7.697288,1.973615,2.883893,-7.156609,-2.829305,4.340706,-2.692289,-6.542774,7.066461,-6.695827,-3.651058,1.982498],[4.628451,-7.941823,-8.513972,8.432384,-5.839242,9.220984,-3.991053,8.822546,-9.653008,7.285390,5.230829,-1.263507,-6.030620,-2.298438,0.156817,4.519588]],[[-6.240006,-2.994148,-2.670905,7.341521,-7.404035,-1.116747,-8.453795,-0.520704,-3.510125,-1.099546,7.440990,0.159035,9.509703,-9.360364,9.921884,5.500877],[2.375610,-2.244211,-9.436636,-3.701506,8.511768,4.668836,-8.730615,-4.291833,6.112681,9.032029,2.950254,-8.551339,-8.431253,8.910282,-9.907935,6.994035],[3.638675,0.855970,0.526220,-2.994162,-3.409665,4.518716,4.168672,-3.457676,-0.879670,1.555874,-0.518489,-1.449416,-9.844724,-7.693090,-1.260421,-2.102262],[2.830938,6.048355,5.412542,3.402696,3.395939,2.581911,-0.994594,-4.423722,3.265329,-9.245126,5.130423,-3.799843,9.148261,9.245117,-6.418044,3.166932],[2.907305,-7.233985,-2.263962,4.793092,-1.630518,8.670250,-8.524129,3.894984,5.113028,5.377982,-8.093731,0.951299,-7.718510,-7.415523,-4.627939,-3.684697],[-0.762822,3.329449,2.947696,6.006997,8.723844,-4.854678,-0.947806,5.268634,-0.565295,-8.873282,-8.645934,-4.387902,-1.446046,4.037140,-9.407240,4.572722],[-5.110259,8.874268,2.565179,-0.394148,0.107554,-7.810423,-8.641471,-4.783391,-9.200774,-1.813005,-0.081120,7.320565,2.766172,7.834581,-9.163244,-5.073592],[5.021771,-0.910613,-1.814888,3.000615,-0.355965,4.574933,0.562134,3.581479,4.921745,-1.736393,-7.422190,-7.203551,-7.269823,9.242038,-8.129429,-4.017111],[5.543699,-9.882807,6.714451,-2.524620,2.859247,-6.557029,2.002680,-2.812473,7.253975,-0.264269,-5.240534,9.343340,-8.324005,-7.996651,6.381661,6.729966],[8.641794,-0.453370,7.860860,-3.770259,8.571423,-0.149430,-4.848402,7.195084,2.029914,2.649394,-7.220496,9.047061,4.325564,-9.407435,-8.745126,-3.773546],[6.672903,-3.091408,7.522752,-0.936520,3.390699,8.061511,2.170931,-9.873723,-8.408088,0.711957,-5.293921,2.505160,-2.373727,-9.963866,8.978329,-3.340090],[-5.882441,-3.690382,-4.038623,-6.483408,8.072174,4.875065,-8.505137,4.813092,-0.716541,9.156106,4.966252,-3.338796,-2.024001,-9.795539,5.964453,2.684762]],[[8.252432,8.685744,-4.101902,-9.683805,2.958008,-9.485793,7.923185,-9.888309,-4.982010,-6.240120,9.304145,5.752042,-4.490951,6.091672,9.301807,9.645400],[-9.704076,-3.830321,-8.020214,-3.747457,-0.579308,9.763061,4.090995,3.194531,8.293092,2.508919,9.558633,7.470282,9.414078,8.217032,6.243405,8.392701],[-1.814702,-5.240164,-0.223183,-0.401758,9.938262,-6.208640,-9.469138,3.692384,-4.164571,-8.152902,4.499583,8.738393,-4.214405,7.105820,9.647151,-9.965476],[-9.137321,-7.919982,2.539295,-5.647491,-9.684763,5.058756,-7.072073,-9.332737,-9.352649,-8.263846,-3.235528,-6.984646,5.116273,-9.246314,-8.211114,-1.785849],[7.842030,-8.761572,3.625150,-4.321424,2.856857,-5.040570,-7.775641,-2.870204,2.299908,-8.863877,-6.502264,1.627459,5.297545,-3.445943,-2.417916,-6.598162],[9.992381,-6.814075,6.938179,-4.785157,7.898867,1.142296,-3.963136,-9.481945,-9.371117,6.955791,6.853810,-5.563803,3.953040,-0.957056,1.395606,7.490474],[2.443670,-6.574001,-8.136486,-6.764950,0.067419,2.201928,7.582386,-6.902540,3.390439,0.390135,-4.566548,1.583451,-2.599590,9.339459,-8.312806,1.264543],[-3.032185,9.973674,-4.777356,-3.837731,6.049035,8.180151,1.051599,-4.228853,-2.694322,3.841440,-1.366908,-1.694585,2.848459,-3.167659,-9.670240,3.669958],[3.954308,-5.075004,-4.797557,-3.289536,-4.973290,8.076919,7.042611,-2.546293,0.460683,-7.944122,-5.121035,-7.021768,-6.475844,-5.299434,-4.725562,7.783152],[-6.025034,-2.551786,4.107700,-3.033206,-1.227033,9.730916,6.592841,9.218208,-8.275924,-0.947193,-6.522962,-1.280588,-7.050582,-9.941396,-8.383615,-1.948940],[4.119871,-1.505971,6.143883,-4.958532,-0.744895,3.747944,-9.269535,-9.635035,-5.925124,0.849910,1.453151,7.961964,-8.880206,7.741378,-7.143375,2.002418],[-4.821752,-3.071020,-5.174469,7.927687,-0.794950,2.475684,-5.055892,4.700252,-4.918820,4.109171,-5.365575,3.753389,-7.251824,-2.989711,0.489024,-8.299227]],[[2.343910,8.551802,-5.148543,-7.789050,-4.468636,6.007823,3.505092,1.693316,4.420019,0.108824,-8.129271,9.922787,3.453400,4.236919,3.304607,-0.573764],[-6.350325,2.315041,2.701960,7.041297,8.787343,-0.331015,-6.794355,-7.171859,-5.320063,7.758258,6.761351,-2.052031,-2.269696,7.165271,8.001698,-9.026048],[8.107010,-2.096168,2.491144,-1.681254,-1.626801,9.697574,5.616353,1.998287,-3.519036,-1.663568,2.132178,-5.999631,-1.489509,1.524756,-7.019591,2.037628],[6.124191,-5.334095,9.003081,9.487576,1.317570,-4.521830,9.249794,-2.548430,8.864503,4.870722,8.465327,-3.407013,6.581198,-1.470017,-5.207503,5.437789],[6.685556,-1.065659,1.788332,6.348254,2.834437,5.889991,4.916715,-9.974009,-3.280344,3.468135,8.525947,4.998885,0.175979,-6.303195,9.532387,-1.878140],[7.920966,1.365224,-8.676839,5.974594,6.164225,-7.209130,3.929287,0.095768,-8.988379,6.356862,-7.326826,-7.686466,-5.695815,4.159988,6.018631,4.442913],[6.380538,5.479638,5.750038,1.811246,7.821554,8.743463,-4.187007,-6.411543,5.754423,-9.155430,-9.589832,0.789841,-9.905416,-9.263132,-9.854225,-2.707354],[-3.699158,-3.265722,3.599644,-5.441239,2.804870,2.396835,-2.617611,2.528261,0.770574,-1.773241,-0.910923,1.864372,-3.871492,-8.114600,1.312942,-0.552573],[-3.212524,3.814475,-1.670932,-3.669042,2.527019,6.866824,9.791390,1.309173,4.059115,-3.468113,3.118561,-1.320806,9.620041,3.300448,5.226060,0.575056],[-5.244702,9.722420,-8.775674,-0.708449,6.585166,-6.811679,-9.196277,-4.781754,1.179403,-0.213151,-7.237616,-1.470164,2.071514,-5.954933,-8.705066,7.566516],[-4.062871,1.674463,-2.981440,-8.525549,-8.619710,9.707956,-7.767272,-0.582623,-4.276596,-2.230390,4.493078,0.696351,-3.461184,1.628964,4.734289,2.727899],[-0.510904,-1.458384,7.108488,-9.904097,7.918285,-4.279693,4.236722,9.115450,7.886211,-8.507855,3.246987,-6.264350,4.736019,-3.832021,-3.459049,-6.613550]],[[-4.730618,4.653667,3.594005,5.085860,4.616330,-7.433302,-6.961654,8.863621,-5.541829,-8.728115,0.795695,7.952191,4.219385,2.397832,-2.394829,-6.260316],[-5.526580,-6.822704,7.336727,7.356712,1.041347,-1.793884,0.401286,-8.454843,0.617525,9.565844,8.653799,-0.850664,-8.781453,-2.355799,1.172303,-5.754005],[-6.820394,-2.623598,-8.378644,1.176722,0.659668,-2.730261,1.685958,-4.357520,4.701795,9.799819,7.669173,3.479513,2.116812,-5.895999,-2.485058,-7.632297],[3.605801,6.024023,-4.843913,8.329436,-8.939646,8.806902,-6.147254,-3.626555,0.644197,-4.827083,6.019969,8.108803,3.727264,-9.255851,-7.897026,0.221141],[5.391713,4.958361,3.600147,8.756834,-1.217669,6.841461,1.284339,7.176673,3.380963,8.924815,3.658061,2.910047,-1.477085,1.551333,-3.925437,-2.055906],[7.003114,-2.252540,-8.145218,-2.661013,-5.132373,-6.726562,0.874041,-5.228222,5.684326,-2.149482,-7.090678,-0.244710,0.307244,6.227552,-0.776708,3.798519],[-5.206026,-1.758755,8.052664,3.483198,-5.187304,0.160905,7.858157,-2.770813,7.704964,-4.576195,-4.579859,-7.184910,-7.529813,6.215244,8.842916,-0.084389],[-4.743132,7.129013,1.335970,6.345109,-9.016715,0.818925,4.897099,-3.162934,-5.630896,-8.522665,2.514444,-6.933358,6.993744,-5.310608,-7.440426,-3.950688],[9.323409,4.098506,-0.183153,-0.403404,5.753678,4.852795,6.652459,-0.270589,-2.171537,-1.914691,0.453123,3.688582,1.255384,-7.782100,-6.343529,-4.945303],[-2.665435,-9.106887,4.398426,8.269539,-8.698232,9.326947,-5.766465,-6.315826,-5.937510,4.797881,3.432635,-3.323348,-1.621663,7.300681,1.946271,7.942594],[9.601336,2.355585,-5.810426,6.585262,8.981561,1.580976,-4.932209,-4.428039,-2.565918,7.953240,-8.282887,-5.852219,-8.976148,4.416944,-6.526847,6.561338],[-0.378079,-3.332436,0.612197,0.404156,-5.321018,-8.511815,-1.320444,3.697700,-2.196308,5.795903,5.990957,-6.559259,6.859870,7.370768,-0.401627,2.993568]]], dtype = "float32")#candidate|7292|(11, 12, 16)|const|float32
bop_7293 = relay.floor_mod(call_7274.astype('float64'), relay.reshape(const_7292.astype('float64'), relay.shape_of(call_7274))) # shape=(11, 12, 16)
bop_7296 = relay.floor_mod(call_7275.astype('float64'), relay.reshape(const_7292.astype('float64'), relay.shape_of(call_7275))) # shape=(11, 12, 16)
output = relay.Tuple([call_7280,bop_7293,])
output2 = relay.Tuple([call_7281,bop_7296,])
func_7311 = relay.Function([], output)
mod['func_7311'] = func_7311
mod = relay.transform.InferType()(mod)
output = func_7311()
func_7312 = relay.Function([], output)
mutated_mod['func_7312'] = func_7312
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4433_call = mod.get_global_var('func_4433')
func_4435_call = mutated_mod.get_global_var('func_4435')
call_7332 = relay.TupleGetItem(func_4433_call(), 0)
call_7333 = relay.TupleGetItem(func_4435_call(), 0)
output = relay.Tuple([call_7332,])
output2 = relay.Tuple([call_7333,])
func_7334 = relay.Function([], output)
mod['func_7334'] = func_7334
mod = relay.transform.InferType()(mod)
output = func_7334()
func_7335 = relay.Function([], output)
mutated_mod['func_7335'] = func_7335
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7311_call = mod.get_global_var('func_7311')
func_7312_call = mutated_mod.get_global_var('func_7312')
call_7343 = relay.TupleGetItem(func_7311_call(), 0)
call_7344 = relay.TupleGetItem(func_7312_call(), 0)
output = call_7343
output2 = call_7344
func_7365 = relay.Function([], output)
mod['func_7365'] = func_7365
mod = relay.transform.InferType()(mod)
output = func_7365()
func_7366 = relay.Function([], output)
mutated_mod['func_7366'] = func_7366
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3198_call = mod.get_global_var('func_3198')
func_3200_call = mutated_mod.get_global_var('func_3200')
call_7393 = func_3198_call()
call_7394 = func_3198_call()
uop_7398 = relay.acos(call_7393.astype('float32')) # shape=(11, 12, 16)
uop_7400 = relay.acos(call_7394.astype('float32')) # shape=(11, 12, 16)
bop_7406 = relay.right_shift(uop_7398.astype('int64'), relay.reshape(call_7393.astype('int64'), relay.shape_of(uop_7398))) # shape=(11, 12, 16)
bop_7409 = relay.right_shift(uop_7400.astype('int64'), relay.reshape(call_7394.astype('int64'), relay.shape_of(uop_7400))) # shape=(11, 12, 16)
func_2326_call = mod.get_global_var('func_2326')
func_2328_call = mutated_mod.get_global_var('func_2328')
var_7414 = relay.var("var_7414", dtype = "float64", shape = (630,))#candidate|7414|(630,)|var|float64
call_7413 = relay.TupleGetItem(func_2326_call(relay.reshape(var_7414.astype('float64'), [14, 3, 15])), 0)
call_7415 = relay.TupleGetItem(func_2328_call(relay.reshape(var_7414.astype('float64'), [14, 3, 15])), 0)
output = relay.Tuple([bop_7406,call_7413,var_7414,])
output2 = relay.Tuple([bop_7409,call_7415,var_7414,])
func_7431 = relay.Function([var_7414,], output)
mod['func_7431'] = func_7431
mod = relay.transform.InferType()(mod)
var_7432 = relay.var("var_7432", dtype = "float64", shape = (630,))#candidate|7432|(630,)|var|float64
output = func_7431(var_7432)
func_7433 = relay.Function([var_7432], output)
mutated_mod['func_7433'] = func_7433
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_7462 = relay.TupleGetItem(func_2351_call(), 0)
call_7463 = relay.TupleGetItem(func_2352_call(), 0)
output = call_7462
output2 = call_7463
func_7466 = relay.Function([], output)
mod['func_7466'] = func_7466
mod = relay.transform.InferType()(mod)
mutated_mod['func_7466'] = func_7466
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7466_call = mutated_mod.get_global_var('func_7466')
call_7467 = func_7466_call()
output = call_7467
func_7468 = relay.Function([], output)
mutated_mod['func_7468'] = func_7468
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2034_call = mod.get_global_var('func_2034')
func_2035_call = mutated_mod.get_global_var('func_2035')
call_7469 = func_2034_call()
call_7470 = func_2034_call()
func_7431_call = mod.get_global_var('func_7431')
func_7433_call = mutated_mod.get_global_var('func_7433')
call_7476 = relay.TupleGetItem(func_7431_call(relay.reshape(call_7469.astype('float64'), [630,])), 1)
call_7477 = relay.TupleGetItem(func_7433_call(relay.reshape(call_7469.astype('float64'), [630,])), 1)
func_4129_call = mod.get_global_var('func_4129')
func_4131_call = mutated_mod.get_global_var('func_4131')
call_7478 = relay.TupleGetItem(func_4129_call(), 0)
call_7479 = relay.TupleGetItem(func_4131_call(), 0)
func_7228_call = mod.get_global_var('func_7228')
func_7231_call = mutated_mod.get_global_var('func_7231')
const_7483 = relay.const([-0.267426,2.417525,2.181481,0.687196,6.645025,-7.823876,4.877881,9.754649,0.665398,1.308276,-9.350240,2.003024,3.539493,4.316050,-5.089807,4.562238,6.948774,9.908358,-8.161123,-8.137901,9.467101,-4.441836,-9.815381,7.768060,9.086882,-6.274339,-0.652415,-5.074869,2.346831,-9.989559,4.309812,-3.730112,-8.064988,9.628533,-8.418787,-4.401698,-1.579153,-0.785781,3.213798,6.096935,8.543968,-7.168074,3.146600,3.633009,-1.475478,-9.378340,9.713487,-9.896329,-7.343880,9.180642,-8.165082,6.921393,-3.600442,9.326514,3.409890,1.933131,-4.854945,-6.326794,-8.247248,-2.172903,0.196517,-7.810018,-7.536719,6.844490,-2.505056,3.531139,-9.022125,0.345444,8.274418,-6.138869,9.023943,5.954085,1.016519,2.157223,9.574157,-2.015054,9.287183,7.275974,-8.292909,-0.993281,7.736532,4.823420,-8.699689,8.421878,2.459862,-6.979481,0.610237,4.945672,5.269693,-3.531385,-9.831932,-3.811304,1.041003,5.656611,-7.565183,-9.153595,-2.715420,7.966007,-1.923252,-4.231400,5.153925,7.623612,-6.989542,9.863188,9.345736,-3.051840,2.712345,8.805902,-5.740069,-5.874896,1.710316,4.227235,-1.298083,-2.993549,0.096433,-7.788943,-1.246241,4.011537,-4.800345,-6.987738,-3.249047,-2.886485,0.770368,-0.666197,-2.189312,-9.368946,2.724556,4.756172,9.603773,-4.726336,-4.737521,8.168144,-2.048803,9.197733,8.905938,0.157405,-8.123668,5.971036,5.347288,-8.167861,-2.096782,9.580857,-4.483458,4.220762,0.967905,-1.603029,8.256027,-7.613285,-7.414895,-8.644124,1.131573,1.636162,5.182444,-6.565112,-8.847901,8.439317,7.877043,-1.256363,3.414005,3.927203,0.840167,6.189480,7.648542,0.245195,5.778817,-3.040371,6.657103,4.493667,-3.414375,8.593846,-3.427322,-8.397281,-9.450008,2.499360,-6.888156,-1.190899,-7.803459,-3.910295,7.203540,3.642776,-3.608233,4.640683,4.839623,-5.407855,-6.385028,-4.545247,-2.420540,6.318147,0.162012,8.328827,1.444464,7.112682,2.584096,-5.806947,7.473333,8.992786,2.256976,0.354389,0.624931,-9.769051,-2.522564,-8.537144,3.080411,5.566869,-3.745107,8.883866,-1.244752,6.004869,-3.538533,-4.755025,9.121373,4.459413,-9.158297,5.072671,5.753559,-0.247803,-9.069770,-8.484132,-4.986210,-4.699274,-2.363921,-2.727731,2.677299,-1.231988,7.061927,6.063965,1.729008,6.889911,-2.184007,5.606270,5.162628,1.726761,8.771420,1.294747,1.614134,-6.751474,4.023411,-8.949648,4.064158,7.281066,6.117647,7.447953,2.168691,-4.871713,-3.031594,3.555178,5.038481,9.923727,1.493345,-8.270768,5.824761,-5.577977,-4.946416,4.692455,-8.978176,-6.395485,9.239446,-7.300792,0.731285,-3.024331,-7.456196,6.530248,-5.585676,-2.121362,4.918587,-2.267819,-5.309069,-0.922086,3.303904,-4.860334,-7.910301,2.303114,-3.820929,-5.808215,3.737904,2.150954,2.892541,5.014077,-0.621732,6.483341,1.032424,-7.095438,-7.567942,-6.508708,-6.269194,6.277979,1.561328,-0.747689,-2.037473,9.328229,-7.033788,-5.392767,0.493198,5.945341,2.289680,-7.075182,8.781466,-5.589178,3.671016,0.290906,8.111466,-7.297194,-3.232301,3.204185,6.417761,-3.966904,1.746240,4.902402,-7.392502,-1.345139,9.996821,-1.261309,2.109767,3.034056,2.110825,-0.326386,8.190157,-9.194762,-9.960458,1.254165,-6.221943,9.215587,-4.315797,8.835210,1.893433,-3.228985,-0.808220,6.660339,-6.173453,-7.826342,-2.552455,-8.863710,8.739488,2.706909,-4.802867,7.067522,-9.655433,4.028868,-6.142888,9.911694,-5.646055,-1.352063,1.777086,2.693698,-4.259725,5.968772,-0.098142,6.479642,-7.162555,4.553347,1.076754,-6.122796,5.341182,-5.727326,-6.993992,-8.731851,6.327339,4.533560,-0.168125,-2.783239,-3.802846,7.356134,-1.453788,-3.414493,1.193147,1.837422,-1.129271,-0.510856,5.579335,8.602454,5.775672,4.783960,9.201922,3.394186,6.691168,-1.227860,4.365538,-7.502749,-4.036839,5.529244,1.047852,-5.636144,-0.667360,2.964789,1.287779,7.461898,-7.008223,-8.519700,8.851477,-6.357329,4.978130,-4.014953,-6.330579,-0.071784,6.279029,4.545522,9.082406,-0.953765,-5.208840,8.552461,4.881623,-1.578990,5.425560,8.382663,-8.287716,4.011316,-3.603458,5.955120,2.366801,-5.376635,2.356712,1.677580,9.612151,-7.504675,0.863123,-3.388785,-4.491044,2.228131,2.478709,-9.547200,-6.383341,7.888494,8.638035,4.983627,3.182910,3.285813,3.259269,5.291968,-9.554624,8.936046,4.964523,-7.025123,-1.497875,-2.235962,-1.877043,-8.377339,-5.127005,-5.735742,-8.983408,-8.396581,2.578897,-8.560506,-3.498654,8.235063,2.149995,5.763311,-8.675208,-2.657323,6.619610,-2.436488,4.554253,-0.524200,7.032597,6.204121,-1.352532,6.916032,3.271712,7.331820,2.375100,-9.973358,0.776902,3.452322,-4.081469,-3.674361,-2.157627,0.204879,8.333084,-4.990211,-8.174812,-4.244563,6.777790,-4.822378,8.818942,9.617250,6.957037,5.829167,5.584084,-7.982778,-4.885503,3.887880,-6.534604,-8.700818,-9.793941,-3.242094,-1.648065,3.302611,-2.966832,-9.948035,9.160929,-2.646392,-8.535700,0.134420,-6.524907,7.102211,4.264603,-5.983420,0.866525,4.400131,5.691643,9.064101,4.204791,4.608757,-3.706563,6.464260,2.937649,-2.302572,-7.567244,1.227133,-0.435682,1.742246,8.472330,7.124112,1.926110,-0.897250,-6.268789,-5.991491,5.957892,4.740992,-6.056507,6.389315,-3.481298,0.122698,-1.450291,0.733528,2.206611,-9.569203,-8.787427,3.588452,-4.063807,-8.982995,4.633946,-8.972199,0.896062,5.699175,1.485003,4.792550,-6.914930,-1.509905,-5.957954,7.180558,-9.812785,-9.367859,8.726682,-1.020648,-6.090272,-3.061191,-4.372890,-5.201271,-5.002886,6.581653,-8.361010,1.291197,1.670969,0.707463,-1.396680,4.760460,-1.936159,0.675139,8.652012,-0.784858,3.695191,-5.053068,6.155478,9.616518,-3.147701,1.179430,9.321883,9.639766,-7.062006,-9.144146,-8.708536,-3.648041,-8.976131,-9.442851,1.292454,8.766004,-3.179052,-0.894498,-8.421637,4.778877,-5.899211,9.992656,-9.919407,-5.350918,-2.231313,7.706049,-7.680848,5.247271,4.240247,2.264315,-4.304544,8.570890,-0.260420,3.997452,3.873888,3.208036,3.876697,-0.380330,7.707450,5.258870,4.449608,-5.516202,-6.502433,-9.703933,-0.552115,-3.841217,-6.434193,3.548496,-0.202931,5.829292,6.149756,7.974954,-7.095951,-2.161530,7.269739,6.359640,-4.099848,-1.218588,2.635326,0.292777,-5.439571,1.891048,5.435275,6.500364,5.133408,-3.136484,7.136783,6.162158,0.316569,-0.011160,7.612709,9.664706,9.146678,-1.907064,4.138411,-6.389395,-2.558110,-8.028233,-5.381312,4.889983,7.809614,0.305193,0.294955,-8.109699,-4.448546,0.988523,-9.110108,-9.810473,2.903704,-5.363150,-7.095463,-3.510210,-6.125398,-0.828022,3.746006,-4.854715,8.761981,3.444921,0.331320,6.710200,-4.213084,8.445524,-1.439997,1.875159,8.025166,-4.588951,-3.678677,-6.222115,8.777242,-2.091577,-0.827106,8.196126,-1.906375,-5.306300,-6.556252,2.480043,8.246880,9.644646,-4.209812,5.527407,7.546000,3.953546,-2.704276,-0.905037,1.720233,-4.309706,-0.932859,7.451943,9.511032,-4.647149,-8.820073,-2.705138,-1.330465,1.732409,-9.111965,-9.283817,-7.198725,-4.455262,7.341024,-5.012971,0.419010,-4.806860,9.710053,-5.290633,-2.466039,-4.872640,-8.383457,-9.232617,2.462714,-3.652500,-2.356081,6.281035,-8.429746,4.053813,-1.685167,-5.289184,8.449431,1.849634,0.512722,5.070750,-2.497776,-5.723656,-0.035742,-2.097050,-1.168509,-6.625203,9.084269,8.798513], dtype = "float32")#candidate|7483|(728,)|const|float32
call_7482 = relay.TupleGetItem(func_7228_call(relay.reshape(const_7483.astype('float32'), [728,])), 3)
call_7484 = relay.TupleGetItem(func_7231_call(relay.reshape(const_7483.astype('float32'), [728,])), 3)
func_3149_call = mod.get_global_var('func_3149')
func_3153_call = mutated_mod.get_global_var('func_3153')
var_7487 = relay.var("var_7487", dtype = "float32", shape = (280,))#candidate|7487|(280,)|var|float32
const_7488 = relay.const([-4,-8,5,7,4,7,-2,8,5,3,2,-7,-8,6,-7,-10,4,-1,-2,8,-8,-1,7,-2,3,-10,9,-3,-6,-1,-2,4,-1,-4,3,10,-10,-4,2,-7,3,9,-9,-9,1,-8,10,-6,6,5,-3,-3,-8,10,-2,5,6,-7,6,10,5,10,-1,-8,8,6,-10,6,5,10,-3,-5,10,-4,10,-6,3,2,-2,-10,-6,4,7,-6,6,-4,-2,7,-2,8,6,-9,-8,2,-3,-4,3,9,-10,4,2,2,-6,-3,10,2,-5,-5,-2,-7,-3,6,-9,-8,1,-4,2,4,-6,8,-10,4,-1,-10,-9,-8,6,-8,10,-5,-2,3,-4,3,7,8,2,-3,-10,-6,10,1,9,-2,-9,-1,3,-2,2,-8,7,-6,-7,-1,-4,8,-2,-9,-10,3,5,8,-9,-6,6,-2,10,-3], dtype = "uint8")#candidate|7488|(168,)|const|uint8
const_7489 = relay.const(9.227027, dtype = "float32")#candidate|7489|()|const|float32
call_7486 = relay.TupleGetItem(func_3149_call(relay.reshape(var_7487.astype('float32'), [70, 4]), relay.reshape(const_7488.astype('uint8'), [168,]), relay.reshape(const_7489.astype('float32'), []), ), 5)
call_7490 = relay.TupleGetItem(func_3153_call(relay.reshape(var_7487.astype('float32'), [70, 4]), relay.reshape(const_7488.astype('uint8'), [168,]), relay.reshape(const_7489.astype('float32'), []), ), 5)
output = relay.Tuple([call_7469,call_7476,call_7478,call_7482,const_7483,call_7486,var_7487,const_7488,const_7489,])
output2 = relay.Tuple([call_7470,call_7477,call_7479,call_7484,const_7483,call_7490,var_7487,const_7488,const_7489,])
func_7491 = relay.Function([var_7487,], output)
mod['func_7491'] = func_7491
mod = relay.transform.InferType()(mod)
var_7492 = relay.var("var_7492", dtype = "float32", shape = (280,))#candidate|7492|(280,)|var|float32
output = func_7491(var_7492)
func_7493 = relay.Function([var_7492], output)
mutated_mod['func_7493'] = func_7493
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5744_call = mod.get_global_var('func_5744')
func_5746_call = mutated_mod.get_global_var('func_5746')
call_7513 = relay.TupleGetItem(func_5744_call(), 0)
call_7514 = relay.TupleGetItem(func_5746_call(), 0)
output = relay.Tuple([call_7513,])
output2 = relay.Tuple([call_7514,])
func_7520 = relay.Function([], output)
mod['func_7520'] = func_7520
mod = relay.transform.InferType()(mod)
output = func_7520()
func_7521 = relay.Function([], output)
mutated_mod['func_7521'] = func_7521
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5569_call = mod.get_global_var('func_5569')
func_5571_call = mutated_mod.get_global_var('func_5571')
call_7522 = func_5569_call()
call_7523 = func_5569_call()
output = relay.Tuple([call_7522,])
output2 = relay.Tuple([call_7523,])
func_7534 = relay.Function([], output)
mod['func_7534'] = func_7534
mod = relay.transform.InferType()(mod)
mutated_mod['func_7534'] = func_7534
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7534_call = mutated_mod.get_global_var('func_7534')
call_7535 = func_7534_call()
output = call_7535
func_7536 = relay.Function([], output)
mutated_mod['func_7536'] = func_7536
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_7543 = func_4118_call()
call_7544 = func_4118_call()
output = call_7543
output2 = call_7544
func_7557 = relay.Function([], output)
mod['func_7557'] = func_7557
mod = relay.transform.InferType()(mod)
mutated_mod['func_7557'] = func_7557
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7557_call = mutated_mod.get_global_var('func_7557')
call_7558 = func_7557_call()
output = call_7558
func_7559 = relay.Function([], output)
mutated_mod['func_7559'] = func_7559
mutated_mod = relay.transform.InferType()(mutated_mod)
func_4118_call = mod.get_global_var('func_4118')
func_4120_call = mutated_mod.get_global_var('func_4120')
call_7577 = func_4118_call()
call_7578 = func_4118_call()
uop_7587 = relay.atan(call_7577.astype('float32')) # shape=(525, 1)
uop_7589 = relay.atan(call_7578.astype('float32')) # shape=(525, 1)
func_7534_call = mod.get_global_var('func_7534')
func_7536_call = mutated_mod.get_global_var('func_7536')
call_7599 = relay.TupleGetItem(func_7534_call(), 0)
call_7600 = relay.TupleGetItem(func_7536_call(), 0)
func_465_call = mod.get_global_var('func_465')
func_469_call = mutated_mod.get_global_var('func_469')
call_7603 = func_465_call(relay.reshape(uop_7587.astype('bool'), [15, 7, 5]), relay.reshape(uop_7587.astype('bool'), [15, 7, 5]), )
call_7604 = func_465_call(relay.reshape(uop_7587.astype('bool'), [15, 7, 5]), relay.reshape(uop_7587.astype('bool'), [15, 7, 5]), )
output = relay.Tuple([uop_7587,call_7599,call_7603,])
output2 = relay.Tuple([uop_7589,call_7600,call_7604,])
func_7609 = relay.Function([], output)
mod['func_7609'] = func_7609
mod = relay.transform.InferType()(mod)
output = func_7609()
func_7610 = relay.Function([], output)
mutated_mod['func_7610'] = func_7610
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2993_call = mod.get_global_var('func_2993')
func_2995_call = mutated_mod.get_global_var('func_2995')
call_7648 = relay.TupleGetItem(func_2993_call(), 1)
call_7649 = relay.TupleGetItem(func_2995_call(), 1)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_7674 = func_2894_call()
call_7675 = func_2894_call()
output = relay.Tuple([call_7648,call_7674,])
output2 = relay.Tuple([call_7649,call_7675,])
func_7678 = relay.Function([], output)
mod['func_7678'] = func_7678
mod = relay.transform.InferType()(mod)
output = func_7678()
func_7679 = relay.Function([], output)
mutated_mod['func_7679'] = func_7679
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_7714 = func_2894_call()
call_7715 = func_2894_call()
func_1888_call = mod.get_global_var('func_1888')
func_1893_call = mutated_mod.get_global_var('func_1893')
const_7720 = relay.const([4.705491,-4.873675,-8.887297,6.937830,-7.720057,-2.231242,-1.345852,-4.471084,3.836904,-3.262731], dtype = "float32")#candidate|7720|(10,)|const|float32
var_7721 = relay.var("var_7721", dtype = "float32", shape = (140, 2))#candidate|7721|(140, 2)|var|float32
var_7722 = relay.var("var_7722", dtype = "bool", shape = (525,))#candidate|7722|(525,)|var|bool
call_7719 = relay.TupleGetItem(func_1888_call(relay.reshape(const_7720.astype('float32'), [1, 2, 5]), relay.reshape(var_7721.astype('float32'), [280,]), relay.reshape(var_7722.astype('bool'), [525,]), ), 3)
call_7723 = relay.TupleGetItem(func_1893_call(relay.reshape(const_7720.astype('float32'), [1, 2, 5]), relay.reshape(var_7721.astype('float32'), [280,]), relay.reshape(var_7722.astype('bool'), [525,]), ), 3)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_7724 = relay.TupleGetItem(func_1430_call(), 0)
call_7725 = relay.TupleGetItem(func_1432_call(), 0)
func_6666_call = mod.get_global_var('func_6666')
func_6668_call = mutated_mod.get_global_var('func_6668')
var_7741 = relay.var("var_7741", dtype = "float32", shape = (60,))#candidate|7741|(60,)|var|float32
call_7740 = relay.TupleGetItem(func_6666_call(relay.reshape(var_7741.astype('float32'), [60,])), 1)
call_7742 = relay.TupleGetItem(func_6668_call(relay.reshape(var_7741.astype('float32'), [60,])), 1)
output = relay.Tuple([call_7714,call_7719,const_7720,var_7721,var_7722,call_7724,call_7740,var_7741,])
output2 = relay.Tuple([call_7715,call_7723,const_7720,var_7721,var_7722,call_7725,call_7742,var_7741,])
func_7743 = relay.Function([var_7721,var_7722,var_7741,], output)
mod['func_7743'] = func_7743
mod = relay.transform.InferType()(mod)
var_7744 = relay.var("var_7744", dtype = "float32", shape = (140, 2))#candidate|7744|(140, 2)|var|float32
var_7745 = relay.var("var_7745", dtype = "bool", shape = (525,))#candidate|7745|(525,)|var|bool
var_7746 = relay.var("var_7746", dtype = "float32", shape = (60,))#candidate|7746|(60,)|var|float32
output = func_7743(var_7744,var_7745,var_7746,)
func_7747 = relay.Function([var_7744,var_7745,var_7746,], output)
mutated_mod['func_7747'] = func_7747
mutated_mod = relay.transform.InferType()(mutated_mod)
var_7778 = relay.var("var_7778", dtype = "int8", shape = (6, 15, 10))#candidate|7778|(6, 15, 10)|var|int8
var_7779 = relay.var("var_7779", dtype = "int8", shape = (6, 15, 10))#candidate|7779|(6, 15, 10)|var|int8
bop_7780 = relay.multiply(var_7778.astype('int8'), relay.reshape(var_7779.astype('int8'), relay.shape_of(var_7778))) # shape=(6, 15, 10)
output = relay.Tuple([bop_7780,])
output2 = relay.Tuple([bop_7780,])
func_7792 = relay.Function([var_7778,var_7779,], output)
mod['func_7792'] = func_7792
mod = relay.transform.InferType()(mod)
mutated_mod['func_7792'] = func_7792
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7792_call = mutated_mod.get_global_var('func_7792')
var_7794 = relay.var("var_7794", dtype = "int8", shape = (6, 15, 10))#candidate|7794|(6, 15, 10)|var|int8
var_7795 = relay.var("var_7795", dtype = "int8", shape = (6, 15, 10))#candidate|7795|(6, 15, 10)|var|int8
call_7793 = func_7792_call(var_7794,var_7795,)
output = call_7793
func_7796 = relay.Function([var_7794,var_7795,], output)
mutated_mod['func_7796'] = func_7796
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2894_call = mod.get_global_var('func_2894')
func_2895_call = mutated_mod.get_global_var('func_2895')
call_7821 = func_2894_call()
call_7822 = func_2894_call()
output = relay.Tuple([call_7821,])
output2 = relay.Tuple([call_7822,])
func_7823 = relay.Function([], output)
mod['func_7823'] = func_7823
mod = relay.transform.InferType()(mod)
output = func_7823()
func_7824 = relay.Function([], output)
mutated_mod['func_7824'] = func_7824
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_7873 = func_2016_call()
call_7874 = func_2016_call()
func_2198_call = mod.get_global_var('func_2198')
func_2200_call = mutated_mod.get_global_var('func_2200')
call_7876 = relay.TupleGetItem(func_2198_call(), 0)
call_7877 = relay.TupleGetItem(func_2200_call(), 0)
output = relay.Tuple([call_7873,call_7876,])
output2 = relay.Tuple([call_7874,call_7877,])
func_7880 = relay.Function([], output)
mod['func_7880'] = func_7880
mod = relay.transform.InferType()(mod)
output = func_7880()
func_7881 = relay.Function([], output)
mutated_mod['func_7881'] = func_7881
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7520_call = mod.get_global_var('func_7520')
func_7521_call = mutated_mod.get_global_var('func_7521')
call_7892 = relay.TupleGetItem(func_7520_call(), 0)
call_7893 = relay.TupleGetItem(func_7521_call(), 0)
output = relay.Tuple([call_7892,])
output2 = relay.Tuple([call_7893,])
func_7895 = relay.Function([], output)
mod['func_7895'] = func_7895
mod = relay.transform.InferType()(mod)
output = func_7895()
func_7896 = relay.Function([], output)
mutated_mod['func_7896'] = func_7896
mutated_mod = relay.transform.InferType()(mutated_mod)
func_1430_call = mod.get_global_var('func_1430')
func_1432_call = mutated_mod.get_global_var('func_1432')
call_8040 = relay.TupleGetItem(func_1430_call(), 0)
call_8041 = relay.TupleGetItem(func_1432_call(), 0)
func_7792_call = mod.get_global_var('func_7792')
func_7796_call = mutated_mod.get_global_var('func_7796')
var_8050 = relay.var("var_8050", dtype = "int8", shape = (18, 50))#candidate|8050|(18, 50)|var|int8
call_8049 = relay.TupleGetItem(func_7792_call(relay.reshape(var_8050.astype('int8'), [6, 15, 10]), relay.reshape(var_8050.astype('int8'), [6, 15, 10]), ), 0)
call_8051 = relay.TupleGetItem(func_7796_call(relay.reshape(var_8050.astype('int8'), [6, 15, 10]), relay.reshape(var_8050.astype('int8'), [6, 15, 10]), ), 0)
func_6509_call = mod.get_global_var('func_6509')
func_6511_call = mutated_mod.get_global_var('func_6511')
var_8054 = relay.var("var_8054", dtype = "float32", shape = (1, 728))#candidate|8054|(1, 728)|var|float32
call_8053 = relay.TupleGetItem(func_6509_call(relay.reshape(var_8054.astype('float32'), [4, 13, 14])), 2)
call_8055 = relay.TupleGetItem(func_6511_call(relay.reshape(var_8054.astype('float32'), [4, 13, 14])), 2)
func_7743_call = mod.get_global_var('func_7743')
func_7747_call = mutated_mod.get_global_var('func_7747')
var_8057 = relay.var("var_8057", dtype = "float32", shape = (280,))#candidate|8057|(280,)|var|float32
var_8058 = relay.var("var_8058", dtype = "bool", shape = (525,))#candidate|8058|(525,)|var|bool
var_8059 = relay.var("var_8059", dtype = "float32", shape = (60,))#candidate|8059|(60,)|var|float32
call_8056 = relay.TupleGetItem(func_7743_call(relay.reshape(var_8057.astype('float32'), [140, 2]), relay.reshape(var_8058.astype('bool'), [525,]), relay.reshape(var_8059.astype('float32'), [60,]), ), 0)
call_8060 = relay.TupleGetItem(func_7747_call(relay.reshape(var_8057.astype('float32'), [140, 2]), relay.reshape(var_8058.astype('bool'), [525,]), relay.reshape(var_8059.astype('float32'), [60,]), ), 0)
func_5777_call = mod.get_global_var('func_5777')
func_5779_call = mutated_mod.get_global_var('func_5779')
call_8065 = relay.TupleGetItem(func_5777_call(), 0)
call_8066 = relay.TupleGetItem(func_5779_call(), 0)
output = relay.Tuple([call_8040,call_8049,var_8050,call_8053,var_8054,call_8056,var_8057,var_8058,var_8059,call_8065,])
output2 = relay.Tuple([call_8041,call_8051,var_8050,call_8055,var_8054,call_8060,var_8057,var_8058,var_8059,call_8066,])
func_8075 = relay.Function([var_8050,var_8054,var_8057,var_8058,var_8059,], output)
mod['func_8075'] = func_8075
mod = relay.transform.InferType()(mod)
mutated_mod['func_8075'] = func_8075
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8075_call = mutated_mod.get_global_var('func_8075')
var_8077 = relay.var("var_8077", dtype = "int8", shape = (18, 50))#candidate|8077|(18, 50)|var|int8
var_8078 = relay.var("var_8078", dtype = "float32", shape = (1, 728))#candidate|8078|(1, 728)|var|float32
var_8079 = relay.var("var_8079", dtype = "float32", shape = (280,))#candidate|8079|(280,)|var|float32
var_8080 = relay.var("var_8080", dtype = "bool", shape = (525,))#candidate|8080|(525,)|var|bool
var_8081 = relay.var("var_8081", dtype = "float32", shape = (60,))#candidate|8081|(60,)|var|float32
call_8076 = func_8075_call(var_8077,var_8078,var_8079,var_8080,var_8081,)
output = call_8076
func_8082 = relay.Function([var_8077,var_8078,var_8079,var_8080,var_8081,], output)
mutated_mod['func_8082'] = func_8082
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7609_call = mod.get_global_var('func_7609')
func_7610_call = mutated_mod.get_global_var('func_7610')
call_8118 = relay.TupleGetItem(func_7609_call(), 2)
call_8119 = relay.TupleGetItem(func_7610_call(), 2)
output = call_8118
output2 = call_8119
func_8129 = relay.Function([], output)
mod['func_8129'] = func_8129
mod = relay.transform.InferType()(mod)
mutated_mod['func_8129'] = func_8129
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8129_call = mutated_mod.get_global_var('func_8129')
call_8130 = func_8129_call()
output = call_8130
func_8131 = relay.Function([], output)
mutated_mod['func_8131'] = func_8131
mutated_mod = relay.transform.InferType()(mutated_mod)
func_5569_call = mod.get_global_var('func_5569')
func_5571_call = mutated_mod.get_global_var('func_5571')
call_8314 = func_5569_call()
call_8315 = func_5569_call()
func_5407_call = mod.get_global_var('func_5407')
func_5411_call = mutated_mod.get_global_var('func_5411')
var_8321 = relay.var("var_8321", dtype = "float64", shape = (198, 2))#candidate|8321|(198, 2)|var|float64
var_8322 = relay.var("var_8322", dtype = "float32", shape = (280,))#candidate|8322|(280,)|var|float32
call_8320 = relay.TupleGetItem(func_5407_call(relay.reshape(var_8321.astype('float64'), [396,]), relay.reshape(var_8322.astype('float32'), [280,]), ), 2)
call_8323 = relay.TupleGetItem(func_5411_call(relay.reshape(var_8321.astype('float64'), [396,]), relay.reshape(var_8322.astype('float32'), [280,]), ), 2)
output = relay.Tuple([call_8314,call_8320,var_8321,var_8322,])
output2 = relay.Tuple([call_8315,call_8323,var_8321,var_8322,])
func_8340 = relay.Function([var_8321,var_8322,], output)
mod['func_8340'] = func_8340
mod = relay.transform.InferType()(mod)
var_8341 = relay.var("var_8341", dtype = "float64", shape = (198, 2))#candidate|8341|(198, 2)|var|float64
var_8342 = relay.var("var_8342", dtype = "float32", shape = (280,))#candidate|8342|(280,)|var|float32
output = func_8340(var_8341,var_8342,)
func_8343 = relay.Function([var_8341,var_8342,], output)
mutated_mod['func_8343'] = func_8343
mutated_mod = relay.transform.InferType()(mutated_mod)
func_7823_call = mod.get_global_var('func_7823')
func_7824_call = mutated_mod.get_global_var('func_7824')
call_8356 = relay.TupleGetItem(func_7823_call(), 0)
call_8357 = relay.TupleGetItem(func_7824_call(), 0)
output = call_8356
output2 = call_8357
func_8358 = relay.Function([], output)
mod['func_8358'] = func_8358
mod = relay.transform.InferType()(mod)
mutated_mod['func_8358'] = func_8358
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8358_call = mutated_mod.get_global_var('func_8358')
call_8359 = func_8358_call()
output = call_8359
func_8360 = relay.Function([], output)
mutated_mod['func_8360'] = func_8360
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2351_call = mod.get_global_var('func_2351')
func_2352_call = mutated_mod.get_global_var('func_2352')
call_8409 = relay.TupleGetItem(func_2351_call(), 0)
call_8410 = relay.TupleGetItem(func_2352_call(), 0)
output = relay.Tuple([call_8409,])
output2 = relay.Tuple([call_8410,])
func_8417 = relay.Function([], output)
mod['func_8417'] = func_8417
mod = relay.transform.InferType()(mod)
mutated_mod['func_8417'] = func_8417
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8417_call = mutated_mod.get_global_var('func_8417')
call_8418 = func_8417_call()
output = call_8418
func_8419 = relay.Function([], output)
mutated_mod['func_8419'] = func_8419
mutated_mod = relay.transform.InferType()(mutated_mod)
func_2010_call = mod.get_global_var('func_2010')
func_2011_call = mutated_mod.get_global_var('func_2011')
call_8458 = relay.TupleGetItem(func_2010_call(), 1)
call_8459 = relay.TupleGetItem(func_2011_call(), 1)
output = call_8458
output2 = call_8459
func_8506 = relay.Function([], output)
mod['func_8506'] = func_8506
mod = relay.transform.InferType()(mod)
mutated_mod['func_8506'] = func_8506
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8506_call = mutated_mod.get_global_var('func_8506')
call_8507 = func_8506_call()
output = call_8507
func_8508 = relay.Function([], output)
mutated_mod['func_8508'] = func_8508
mutated_mod = relay.transform.InferType()(mutated_mod)
func_6317_call = mod.get_global_var('func_6317')
func_6319_call = mutated_mod.get_global_var('func_6319')
call_8608 = relay.TupleGetItem(func_6317_call(), 0)
call_8609 = relay.TupleGetItem(func_6319_call(), 0)
func_2016_call = mod.get_global_var('func_2016')
func_2017_call = mutated_mod.get_global_var('func_2017')
call_8632 = func_2016_call()
call_8633 = func_2016_call()
func_7334_call = mod.get_global_var('func_7334')
func_7335_call = mutated_mod.get_global_var('func_7335')
call_8646 = relay.TupleGetItem(func_7334_call(), 0)
call_8647 = relay.TupleGetItem(func_7335_call(), 0)
func_5078_call = mod.get_global_var('func_5078')
func_5081_call = mutated_mod.get_global_var('func_5081')
const_8661 = relay.const([[6.743317,9.649905],[4.114929,-4.008564],[7.332259,9.099747],[-4.818313,-0.931058],[-3.997955,1.413977],[-4.130782,0.331524],[-0.948141,7.329220],[-8.563945,-7.473846],[1.844629,6.491211],[8.407318,-1.450268],[0.671166,-3.033614],[-5.823480,-7.957729],[-2.876602,3.874854],[8.808696,-0.034648],[1.521014,-8.413687],[-3.026509,9.106510],[-8.051495,8.619989],[-1.883425,-8.422494],[1.060351,5.167357],[-9.826446,-4.629840],[9.427439,2.960501],[-0.001620,-8.354550],[5.542601,-5.438074],[0.242227,3.180029],[-8.512757,-2.526957],[8.539608,-2.748774],[6.800055,-2.073828],[1.225927,-3.908926],[-7.698543,8.255972],[-3.914730,-4.600533],[-4.784099,6.944660],[-6.763344,-1.159642],[8.218346,7.393764],[4.767532,-7.696667],[8.043703,-2.661251],[2.378859,6.264993],[-2.743894,7.535716],[-1.481545,8.342877],[-3.480673,0.765275],[4.340627,8.220142],[-4.040255,5.852691],[4.645879,-5.120994],[0.749321,7.140740],[-1.640321,-3.363986],[-3.772146,3.395127],[-5.492849,9.490545],[4.577349,0.829976],[-2.549674,-3.789796],[-7.955110,8.169948],[7.584744,-5.471083],[-3.666200,2.165245],[4.335101,-4.965282],[8.066076,-4.855635],[-3.104079,-7.555978],[-3.866079,-5.330337],[9.259662,1.474161],[4.620408,9.291326],[9.731833,8.537163],[6.861885,-5.760205],[-7.390163,-8.013439],[-5.901682,5.703850],[3.746512,-9.240894],[-0.665599,-1.426120],[3.732894,6.844573],[-7.909605,5.385955],[-6.011980,-5.621206],[-4.724349,-8.219732],[1.712655,-9.181211],[-4.335655,-6.511645],[-1.609864,7.669959],[1.427355,-4.013590],[-5.179678,0.873823],[-0.299953,-7.155262],[3.793500,-1.413327],[7.450152,9.938434],[-3.938648,-8.954478],[7.131227,-2.921718],[9.791057,-2.994268],[8.447788,-1.990491],[-4.892720,0.893957],[-2.948899,-2.771621],[-0.465815,7.756494],[5.403712,-0.018469],[6.586122,-6.170849],[0.782219,-5.227245],[3.549855,1.400783],[2.668167,-4.110059],[-1.055872,-3.514851],[8.260633,-2.627011],[3.416242,1.008633],[-0.312385,-6.345453],[-9.084510,2.668363],[0.039956,-3.399374],[-3.782863,-3.580837],[2.608819,-5.531260],[-8.744719,3.938977],[0.398029,5.404134],[7.266492,5.317077],[-1.169783,3.723428],[8.183828,-2.966264],[-9.691029,7.477432],[-8.506100,-1.413420],[-0.893016,3.762018],[8.053831,-0.100602],[0.553612,-4.513333],[-8.404513,-0.165763],[8.892353,6.592853],[-8.085853,-2.560847],[-9.393098,-7.405785],[8.124768,8.294597],[4.030203,-6.967546],[2.861872,4.415502],[-5.968005,3.092059],[3.633350,5.375405],[-9.584839,3.691219],[-8.046444,6.364738],[1.946281,9.056516],[5.457287,-2.555279],[-9.163273,6.272335],[0.198878,-0.456094],[-1.163617,-3.025920],[6.906686,1.486033],[-6.934498,2.371032],[-2.042602,-3.705114],[-5.844241,-3.260295],[-1.744787,-6.148977],[7.864239,-6.040683],[-6.845855,-8.027225],[-3.746922,-5.595139],[-2.027763,3.791474],[5.835808,9.982372],[-3.373210,8.033976],[8.685736,-2.398730],[3.765909,-5.737340],[-4.989830,9.470426],[7.441425,-1.595955],[7.724600,-4.304954],[-5.891345,-9.231811],[-2.640544,9.358658],[6.174112,8.608835],[-8.729020,-3.239334],[-3.946615,-9.950797],[1.974978,2.679858],[3.452567,8.763396],[-1.381325,-7.246247],[7.957324,-2.073556],[-9.004886,-9.400145],[3.521488,-3.672076],[4.522046,2.400143],[-0.966511,3.614005],[7.123571,-3.857265],[-4.929767,2.747603],[2.501491,2.969795],[4.367520,-4.168092],[0.971336,1.770434],[-7.338834,-8.185463],[4.508091,3.691751],[8.546609,0.144886],[6.569510,6.729347],[4.670723,5.490598],[-3.384004,-6.478997],[-6.093731,3.283129],[5.314791,-0.460151],[-8.499564,-3.496617],[-5.387611,1.864245],[-4.589959,4.815198],[1.532740,2.488290],[4.752141,5.548961],[4.042750,7.290323],[2.056688,4.326916],[-9.221472,-9.399873],[-5.096998,-3.803625],[0.925424,-8.533255],[-8.781556,3.205514],[-3.923477,3.009863],[0.022191,2.542697],[-1.799018,6.081710],[9.136263,-2.288927],[-3.616096,-3.491790],[8.904878,-2.503411],[1.224350,-3.936731],[-5.739821,1.237119],[-3.360386,-5.692024],[4.030627,-0.062964],[9.479822,7.277073],[-5.312609,-6.465754],[2.099967,9.178924],[0.104429,7.937770],[-4.914977,-0.053264],[3.921588,6.670146],[-4.183537,-6.082646],[7.448924,4.860750],[-6.842960,6.596395],[3.319105,9.241600],[8.497939,5.463407],[-5.741494,6.866746],[3.657052,7.731661],[6.974088,-9.352432],[3.751064,0.566397],[-7.918510,3.218258],[-1.122934,2.490096],[-7.331817,-6.259684],[-8.416529,-3.319925],[-6.602752,1.502683],[9.096015,-2.339066],[-3.408250,3.968777],[9.088747,-5.967694],[4.722431,-0.663910],[8.923759,2.974989],[4.871250,3.318213],[-3.043730,-7.626267],[2.579135,-5.537769],[7.308155,0.532427],[0.178894,1.878641],[8.439521,-6.319028],[1.560433,-5.476129],[5.110246,-9.493537],[3.187367,-1.999233],[2.032811,-3.219868],[-5.823545,7.117228],[-1.221305,2.254127],[6.700603,-7.758514],[3.518653,-2.479735],[-1.612584,5.498056],[-0.531734,-0.222019],[5.106007,0.288100],[4.792444,0.039324],[-1.477238,6.090603],[5.497980,4.493988],[4.820656,6.020542],[-8.101989,7.386855],[0.786070,-9.103986],[-9.994455,8.499205],[7.738882,-2.828484],[8.586427,0.778130],[7.342080,-3.892239],[4.623493,5.772828],[3.089216,0.937404],[-4.534065,-3.075289],[2.098923,-5.980383],[3.799247,9.414024],[-1.259213,-1.691513],[3.390342,-8.371661],[-1.275679,2.822172],[-0.312679,4.091554],[-7.836779,3.900643],[8.824996,-8.442831],[6.953283,5.904564],[-3.929483,9.903844],[-5.523745,-1.135899],[0.838072,-5.405268],[8.788280,-1.407422],[7.253366,-1.912918],[-6.859675,-5.180718],[2.724738,1.533486],[1.116548,-9.108050],[2.100047,4.855319],[9.536724,-2.325228],[-5.904938,-8.804618],[-3.056974,5.561067],[-1.600990,5.457187],[3.599423,2.048715],[-1.626678,7.071931],[4.231153,-7.567493],[-2.015589,-8.405236],[3.798181,-4.363000],[-2.965916,-9.621704],[6.545781,-5.384308],[1.790217,6.899363],[4.930113,6.671850],[0.252434,-2.543658],[-8.412590,6.832272],[-5.120502,-5.040885],[-1.299644,9.520453],[-3.309586,-4.662760],[0.234749,3.080011],[-8.595303,0.906533],[9.442540,-1.051794],[-0.270007,2.010656],[0.069743,9.217324],[8.237637,4.361614],[-0.633078,-9.785841],[-2.199876,9.362510],[1.219176,-0.624335],[1.532277,3.916242],[6.353712,4.933627],[-6.838748,-1.261676],[5.399447,5.085351],[-2.029274,5.278085],[6.110876,2.022785],[-7.864266,1.128425],[3.256445,5.184658],[-0.917347,-0.145752],[-2.200119,9.381438],[-4.457725,-3.940085],[2.745368,-4.896701],[8.688569,-1.529734],[3.870403,-6.616174],[-9.204119,6.997615],[-8.799951,-7.994317],[-6.082826,-5.746979],[-6.300668,8.501352],[1.022984,4.504296],[-9.755337,-5.001149],[8.025678,-4.445978],[-0.539782,-0.717432],[3.922046,3.730703],[-7.401777,-7.092592],[-9.616049,-7.585844],[-7.443484,9.131096],[2.259063,-9.473907],[9.392417,3.592214],[3.078325,0.093283],[7.307954,8.420282],[-2.787127,-1.016357],[-0.578624,8.305494],[2.558330,-6.878276],[1.027136,9.238253],[-0.299646,-2.616835],[4.748657,-6.228960],[-6.146029,-6.558961],[6.795129,-5.922640],[-1.814132,-9.861919],[2.326421,5.492109],[8.470724,-2.337488],[-2.069393,-6.117872],[5.632325,-8.239839],[-8.062679,4.234955],[-2.660216,-4.982425],[7.799718,2.928428],[4.067637,4.030562],[4.090546,1.641162],[-2.142893,-0.992815],[-5.016069,9.592103],[6.378736,-4.454484],[-3.400369,-8.164328],[1.639301,-7.458867],[5.686765,5.775720],[7.752071,4.406447],[0.201884,-9.355483],[-0.680893,-0.715602],[3.876468,-5.170343],[4.812844,-6.600341],[8.299276,3.585137],[-7.907931,4.570940],[2.488948,-8.060730],[2.199721,-5.083019],[7.739933,-3.677960],[3.202058,-9.182912],[-5.786399,8.328313],[5.895171,3.585692],[8.194093,1.319227],[-2.473712,1.959879],[7.908724,4.212353],[-5.587953,-7.248886],[-9.129649,8.161192],[9.113694,-0.896938],[5.427969,-9.141113],[0.197107,9.328163],[-2.043202,-6.354338],[3.490055,-9.578217],[-3.190186,-9.296098],[9.900488,-0.292292],[5.053101,5.735992],[5.328727,2.311754],[-4.619613,3.463010],[2.836418,-1.112847],[5.380866,2.522362],[-9.602923,-4.104173],[7.975650,0.517400],[1.326942,-3.849220],[-8.647210,1.105602],[7.032845,-0.258460],[-1.436546,0.149850],[-4.616026,1.442081],[8.480488,-0.433273],[4.204531,-1.453534],[8.315212,3.684028],[1.993718,-9.778972],[-9.810010,7.171154],[-0.569186,0.492212],[0.330804,-8.474886],[-7.572646,6.487244],[-1.306049,5.189454],[-6.078333,-3.752229],[-1.726211,-6.175717],[0.944486,2.522744],[2.126454,3.462442],[-6.558156,-6.108851],[-7.337184,3.892940],[2.789229,-9.734538],[-4.200831,4.765516],[1.076081,6.399592],[9.605039,9.006486],[-7.974840,-9.104008],[5.583385,3.133008],[-5.949060,0.704992],[-9.201023,2.486757],[8.987607,-2.775227],[-9.616874,2.594622],[0.387424,7.424094],[-8.854240,-0.041169],[6.256823,-6.641291],[-9.264160,-2.237168],[-8.350244,2.286797],[-8.334354,-8.357992],[-7.362390,0.891760],[-8.087581,-1.687119],[1.640990,-2.729770],[-7.396771,-6.192662],[-7.643862,-2.518232],[-4.406728,1.787435],[-7.797844,-2.048082],[-5.545465,9.474646],[7.146230,3.870826],[5.209044,4.234712],[5.093176,-2.941195],[-3.740115,1.126159],[-8.454819,-0.731767],[-1.360361,0.146606],[-2.957862,9.621301],[-0.123542,-2.751453],[5.335921,9.900754],[0.190788,-6.651172],[-2.365098,3.226966],[8.868773,5.059064],[-7.047779,0.144311],[-9.601942,-4.464045],[-0.611257,5.452646],[-2.346582,-1.349671],[3.839407,-4.420587],[-6.703224,0.361816],[9.932678,-2.175382],[5.345137,-0.936163],[3.983767,-4.040895],[-4.905976,-5.809331],[-1.546753,3.847438],[8.893977,-7.414130],[0.111919,-6.169732],[3.916292,4.198032],[-8.800537,-3.889427],[0.666232,7.554171],[-4.603010,-7.057479],[-4.802094,7.618327],[-7.706508,1.610628],[-6.262867,-8.341890],[-8.377766,6.344382],[-3.036319,9.807946],[-6.688221,-1.924353],[-0.147472,-1.935131],[1.000083,-4.948270],[-7.607516,-6.201865],[-1.791923,-1.205754],[-4.316702,8.867992],[8.512303,-1.353174],[1.747370,-1.307698],[1.790485,4.604956],[5.645677,-7.145937],[9.406273,-5.872750],[-1.560049,-4.613200],[0.177349,0.569368],[-6.742950,-5.417146],[-5.086735,6.756556],[-8.571983,3.585500],[7.754411,-4.715771],[2.850677,5.336108],[3.912536,-3.595134],[3.104431,-2.236101],[3.012481,-6.126905],[-1.215892,-7.864864],[9.873810,-9.731212],[2.671985,-9.384992],[0.309100,4.391630],[6.318899,0.938117],[0.988600,2.520677],[-1.667025,8.580438],[9.276003,1.981296],[-7.207150,-4.434908],[-4.153092,-6.970788],[6.295179,-3.327124],[5.066555,7.857690],[-4.578642,8.157687],[-8.763766,-3.086416],[-4.377987,-6.495362],[6.171877,-2.190913],[1.830950,-5.983911],[5.149877,-2.500264],[4.261864,6.347037],[-8.108240,3.427147],[1.932172,-5.057817],[0.576380,5.613641],[-3.541532,-3.983894],[4.339895,-6.296955],[7.470397,-9.169966],[3.871297,6.211093],[9.646737,0.559777],[2.374876,3.110941],[8.696063,-8.285659],[-6.449501,-1.925902],[-5.422793,6.435824],[9.284716,-9.900694],[-7.581440,-1.790399],[4.221543,-2.297016],[-8.938463,1.875149],[-8.104944,4.273083],[-8.970461,7.549337],[4.219146,-5.858414],[-7.754119,4.532981],[9.127229,-2.571586],[4.415533,7.150971],[0.159831,3.824050],[7.726695,4.747655],[2.655957,3.986138],[3.780451,3.534687],[-1.962964,-2.096949],[6.566023,4.641017],[9.594756,-5.502117],[-1.944171,-2.940263],[2.748617,2.962731],[-0.322198,-2.903703],[8.867089,3.490030],[-7.943181,8.006390],[-9.375934,3.722166],[-6.512572,-1.699426],[4.350348,-6.221015],[-1.592502,0.945555],[-3.250078,-5.011771],[7.373259,2.114990],[-8.764836,6.222805],[1.059926,-6.736600],[-1.575825,7.699435],[-9.067216,8.120699],[-4.567970,1.172014],[-9.781661,-2.794473],[5.040294,5.781693],[8.218948,-7.216246],[1.921306,1.720242],[-4.706272,9.990449],[8.857382,1.874288],[-0.022276,4.825472],[-5.967210,-8.399140],[6.648153,-2.277487],[5.512851,-1.052841],[-7.423394,7.921952],[-1.666892,-5.496801],[-5.998387,-1.027837],[-7.707842,7.450377],[-8.168545,7.217336],[1.632010,3.221937],[-1.525231,3.124125],[2.908958,-8.794837],[-7.184755,8.257825],[-5.825985,-3.184122],[9.722382,4.636969],[-3.676237,4.630723],[5.677956,-5.204658],[-6.743619,-3.994457],[5.416396,-7.007637],[0.620413,-8.663830],[-0.794335,-1.245383],[0.027144,7.776480],[1.576631,-1.972084],[3.454918,-0.415327],[-9.011826,1.567907],[-5.666891,5.473248],[-6.757996,-0.771490],[-2.422460,7.220610],[4.864363,-5.486519],[-0.116842,7.434571],[-6.625413,-4.100661],[2.904590,-5.260821],[4.757267,-6.139381],[6.788345,5.136712],[-3.373876,9.788188],[-2.033799,0.780316],[1.595924,-4.273324],[-3.774400,7.558297],[1.008486,-9.314850],[1.899972,-0.607876],[6.230973,-4.478021],[-3.156386,-0.643246],[-9.676711,3.944557],[-0.283974,-7.635095],[-7.602754,-8.145945],[-7.942659,9.037581],[1.955869,8.458238],[7.166316,1.136399],[-4.874668,2.012301],[9.360437,1.515744],[-5.734942,-0.548527],[-9.739891,-8.026224],[5.401261,8.550448],[-5.650088,0.046589],[-3.579355,-4.312307],[-5.777745,-6.225534],[-0.832264,8.347313],[6.252166,7.448135],[9.647553,8.820926],[-9.832017,2.851903],[-2.696229,9.677088],[8.999468,-5.867646],[4.078935,2.506143],[-3.679991,4.678173],[-9.820445,-8.247339],[4.132777,1.886737],[0.113429,-5.112706],[-7.899824,0.438944],[-0.729539,9.842458],[7.567121,-8.533862],[2.044817,-5.990750],[9.592909,-5.936479],[-6.958189,-8.590342],[-5.474194,-4.166099],[-4.762967,4.710796],[-6.058357,9.299591],[1.659311,9.223268],[-8.250656,-1.110578],[3.971253,7.722213],[-2.524717,-2.309987],[-4.538149,-2.537900],[-0.738255,-1.115274],[-0.675214,9.484475],[-5.031414,4.733829],[-6.403834,-5.948967],[-7.283978,-3.141299],[9.817046,7.676015],[8.440899,-3.977475],[-9.121552,-3.732227],[8.696137,4.424858],[-6.706500,6.143508],[6.208255,-2.024357],[3.599009,-1.829892],[9.734873,7.006659],[-4.265832,-9.353709],[9.248924,2.754761],[-9.471020,-3.681451],[-3.373053,9.769543],[9.813159,4.753814],[6.598431,-9.399807],[-9.442909,6.664264],[5.384305,-5.231364],[5.915720,0.509458],[1.863992,-2.205467],[-2.550003,5.189248],[-0.919693,2.420082],[4.693292,-8.944056],[-2.836722,9.995775],[1.680662,9.379951],[-7.437399,-6.356265],[-1.227647,-7.953588],[-2.148018,0.710207],[1.174720,7.121426],[7.741313,7.261831],[9.258064,-9.652190],[-5.407361,-8.420795],[-8.067458,-4.596353],[9.222574,-2.144132],[-1.695429,7.026275],[4.898771,0.763500],[5.134013,-3.046967],[7.273736,-9.132509],[5.531139,9.814370],[-0.065903,3.280376],[7.970713,0.884209],[-0.617688,-0.333121],[-0.617871,6.628229],[0.901873,0.792872],[0.940495,5.935078],[2.265440,9.944887],[-9.960361,8.444462],[-2.499332,5.099429],[-3.543214,-1.552531],[-6.348605,-8.116741],[-7.082002,-4.721149],[-8.860257,-9.888043]], dtype = "float64")#candidate|8661|(675, 2)|const|float64
call_8660 = relay.TupleGetItem(func_5078_call(relay.reshape(const_8661.astype('float64'), [6, 15, 15]), relay.reshape(const_8661.astype('float64'), [6, 15, 15]), ), 4)
call_8662 = relay.TupleGetItem(func_5081_call(relay.reshape(const_8661.astype('float64'), [6, 15, 15]), relay.reshape(const_8661.astype('float64'), [6, 15, 15]), ), 4)
func_7431_call = mod.get_global_var('func_7431')
func_7433_call = mutated_mod.get_global_var('func_7433')
call_8666 = relay.TupleGetItem(func_7431_call(relay.reshape(call_8646.astype('float64'), [630,])), 1)
call_8667 = relay.TupleGetItem(func_7433_call(relay.reshape(call_8646.astype('float64'), [630,])), 1)
output = relay.Tuple([call_8608,call_8632,call_8646,call_8660,const_8661,call_8666,])
output2 = relay.Tuple([call_8609,call_8633,call_8647,call_8662,const_8661,call_8667,])
func_8672 = relay.Function([], output)
mod['func_8672'] = func_8672
mod = relay.transform.InferType()(mod)
mutated_mod['func_8672'] = func_8672
mutated_mod = relay.transform.InferType()(mutated_mod)
func_8672_call = mutated_mod.get_global_var('func_8672')
call_8673 = func_8672_call()
output = call_8673
func_8674 = relay.Function([], output)
mutated_mod['func_8674'] = func_8674
mutated_mod = relay.transform.InferType()(mutated_mod)
func_3440_call = mod.get_global_var('func_3440')
func_3441_call = mutated_mod.get_global_var('func_3441')
call_8699 = func_3440_call()
call_8700 = func_3440_call()
func_5813_call = mod.get_global_var('func_5813')
func_5816_call = mutated_mod.get_global_var('func_5816')
const_8706 = relay.const(-5.809679, dtype = "float64")#candidate|8706|()|const|float64
call_8705 = func_5813_call(relay.reshape(const_8706.astype('float64'), []))
call_8707 = func_5813_call(relay.reshape(const_8706.astype('float64'), []))
const_8732 = relay.const([[[-8.301269,0.302657,2.159294,8.209394,-2.185593,-1.532686,-8.642317,-0.299486,-1.358056,-9.036478,8.419889,7.753565,-3.848347,-5.550444,8.707397,-2.752128],[-1.953385,6.344585,-9.731406,-1.649143,-5.627567,-6.523772,0.736727,-1.422317,-4.919962,-0.149100,-9.243104,-9.410443,-8.101510,7.507961,-2.246793,-8.331646],[8.739438,-8.866577,-7.052720,9.325332,6.129176,6.678600,-1.778782,0.095110,9.030692,-1.634090,2.698107,-2.881026,7.897454,4.186100,-2.584930,-9.457593],[7.893679,7.994982,-1.499696,-6.844833,-1.301195,-9.364258,3.335745,-4.319809,1.242237,0.394796,7.866176,-6.569884,4.778802,3.481611,8.698479,-0.447598],[-0.042474,0.954249,-6.796153,1.004492,6.801001,3.451014,4.677859,0.026578,3.057689,1.294461,5.274959,1.215375,4.436150,-3.291616,4.939044,7.183317],[-2.915387,-9.847080,-8.915310,-3.053161,8.562294,1.224085,3.493781,3.440878,0.710829,4.191471,-0.781221,0.598051,5.142820,2.623785,-3.592114,8.418727],[1.054554,0.210558,9.309178,0.626953,-8.958409,5.241476,-2.287009,-7.255429,9.210796,-3.785346,-5.375608,8.332077,1.965386,-8.275017,5.993430,-1.218914],[9.578198,-0.126301,6.876587,7.417269,-8.351496,9.640968,6.513016,-1.245077,-7.150544,7.014858,6.137114,-3.398355,6.102675,-1.455023,-9.696878,9.698250],[5.142487,-3.402241,0.939339,-7.408923,-1.286028,-2.991818,3.101127,-4.058530,3.224229,-8.240256,-6.130096,8.681525,-2.670296,-3.068751,6.681207,-1.138311],[-6.483668,2.715794,0.030351,9.982018,-5.748600,2.187296,1.047408,8.530103,9.376805,1.907967,-7.570050,6.724393,-1.738146,-6.717546,8.842036,-9.232198],[1.780489,-7.817228,5.120573,6.472968,1.139664,7.402308,-9.722809,-1.945595,9.763620,-9.425924,-2.343527,-3.361483,0.594365,-1.831566,5.184578,-5.704211],[3.542873,5.530535,6.418735,-0.220710,-5.519679,2.018565,-2.903697,-4.164221,4.675597,0.361374,5.009267,-8.534498,-9.327381,2.718465,-7.965468,1.676816]],[[-4.657712,-9.012275,6.413926,5.327677,3.117758,-2.202153,-7.478795,3.279607,7.205077,6.606560,-3.848258,-3.889521,9.088206,-6.085572,4.159462,7.699378],[0.612301,7.578367,-2.271540,-1.832971,2.530344,3.127465,4.001562,8.874600,9.331554,3.574178,0.310670,9.753444,-7.390235,-6.077590,4.862421,9.368479],[3.899391,9.562136,0.839881,4.366032,-5.924033,-7.020910,8.514425,0.318412,4.096048,-5.322759,-7.380105,0.021618,-7.386763,-0.013130,7.574465,-2.100747],[5.563667,-3.088679,9.459655,5.288337,-0.599435,1.050886,-0.325497,-8.508268,-6.202793,-7.194745,-4.901704,7.215375,5.315615,-4.544613,1.453319,6.115631],[-6.294874,-0.106111,-4.952462,-9.672130,1.763405,-8.794703,-4.754489,8.819953,-2.426602,8.763379,4.741167,3.266728,-7.235491,2.739342,-7.254134,-5.334585],[-1.073206,-4.905765,3.257388,2.394216,-8.404730,-4.968433,1.784266,0.127716,7.508881,-4.396547,2.281452,2.832891,-7.294371,-7.316520,3.616082,7.324251],[8.630165,-4.946884,-6.516733,5.375731,-8.508802,1.263749,-2.918124,6.609612,2.894690,-4.105923,0.569668,8.058051,2.057351,-7.856357,-5.594399,-6.700673],[9.273880,-6.370923,3.960989,-1.794270,2.807419,5.856658,6.702146,2.375072,-0.689327,0.104048,5.486510,8.375293,-1.323551,-5.945470,-5.995109,-1.054703],[8.049798,4.271734,0.602113,-2.624829,-0.117051,-9.449860,-3.703262,-3.555164,6.046800,-1.553898,-7.233124,7.895757,6.055710,-7.095418,4.925364,4.844496],[6.394045,9.632305,2.958717,-1.546588,0.056098,6.616487,-3.294994,-5.201070,5.605988,9.661604,8.149999,1.993239,-5.689501,-2.238843,-8.224412,-0.111198],[-3.519356,-5.797989,-2.371597,5.038001,9.465225,2.203812,0.212910,-6.493470,9.578274,-6.712078,-1.003822,1.671766,1.928379,-0.941558,-9.575476,-3.717145],[-7.108532,-2.133379,7.496119,-7.941076,-7.077853,-4.371480,-4.494707,-2.925046,-1.992625,-4.759133,-7.805325,8.583003,9.854767,-3.493943,2.967123,-6.819321]],[[2.250354,-2.008164,7.080812,-7.313395,-2.038157,8.353007,1.822936,-2.168112,-6.000494,-6.494105,5.001049,6.096687,-1.968732,-1.719299,-6.740996,0.340681],[1.325072,-2.815087,4.375365,-6.641867,4.702011,-0.353558,5.351000,0.807058,0.885044,6.389098,5.181358,0.724338,-7.216034,1.550298,-5.224159,-2.703146],[-7.514228,-0.497255,0.666959,-6.329706,-9.727925,2.667485,2.827372,-7.486203,4.428389,7.069368,-9.551762,-9.678070,-5.300801,7.641129,-4.127365,-2.323684],[-3.718417,-5.378124,8.556934,-2.773498,1.286097,-6.634915,-0.534771,1.303571,-8.809063,2.201097,7.937765,0.074520,2.314777,8.125594,-6.072291,0.772512],[-9.877760,6.162345,-0.628429,-5.824418,4.985808,-4.544060,0.826875,2.178313,6.267536,-4.269782,-9.615117,-5.067274,-2.918109,-2.617369,-0.063011,4.167170],[5.788402,-4.008328,-9.377781,-4.612031,3.864033,-9.445737,-4.505630,-0.844721,-7.990564,5.190303,-6.799919,-7.991508,9.142783,-9.641727,-7.081192,-5.441610],[-5.412466,3.899390,4.195728,-0.275267,7.772373,1.254769,0.073853,6.369184,-1.386141,-5.170407,-5.682385,0.331378,1.352929,2.183888,2.470260,-7.417537],[7.841415,3.495373,8.289622,1.867436,-7.212226,-4.127059,8.027252,3.696889,-6.686487,-1.338047,-0.118334,-4.562608,0.473086,-5.385063,-7.616691,-3.884527],[-1.249740,-9.684429,-6.864644,-1.281770,0.201044,-0.757142,-9.601713,-0.875519,3.301577,-2.449968,3.031274,-2.863991,-0.465062,8.074515,8.162462,-5.630699],[5.298252,0.796441,3.152877,-6.921853,-2.741279,5.462526,-8.423232,-3.654518,-3.808748,-9.864177,8.770395,0.966423,1.157966,-7.331868,-4.911748,-3.093446],[-8.738165,2.657134,-9.454677,-6.321798,-6.024678,2.542383,3.556013,8.111588,-4.237988,0.530828,-8.976831,-0.430122,-8.728509,-8.194620,5.756192,-1.340162],[-2.789582,8.421029,-5.874388,0.670897,0.873297,7.242066,-0.953564,4.198318,-8.610710,3.316097,6.545263,-6.793284,-2.575460,-4.620590,-9.457160,7.538446]],[[1.723629,1.288555,-3.356232,-2.321815,8.216500,6.715448,-8.915617,3.916062,6.128675,4.954377,-1.680972,-8.235345,-2.257331,-1.067652,-0.119179,7.503566],[6.429117,2.868802,-2.079648,9.398515,7.668143,1.394339,5.440914,3.104175,1.317126,1.266130,-4.686969,0.565973,7.598745,7.341517,3.473680,4.880119],[7.942693,9.321169,-2.973903,-7.059989,4.007916,-7.057446,-2.265620,2.390941,-3.417791,6.402538,7.173134,-6.647112,-5.507404,-9.736035,-3.969268,-6.191370],[-4.808581,6.391777,9.696344,-3.142696,-6.499052,8.693411,-5.527376,-9.346354,-0.697663,-7.885420,-8.665471,-6.472761,-0.430108,3.078875,-6.390984,7.768495],[9.859630,7.528392,-0.549329,4.840076,-0.833815,3.593435,4.217028,-3.497335,5.291475,8.435692,7.821343,-8.262040,-0.120575,-0.384220,-6.105160,9.605882],[3.002336,-0.875431,1.207140,-8.528581,-0.973602,-0.880864,1.824438,5.779309,6.164935,9.130713,-3.884122,9.807172,7.683093,8.730934,3.706449,2.538551],[-5.629383,-9.366271,5.104113,0.809597,-2.095110,6.429883,-5.420268,-1.422135,-6.890855,-2.243039,2.516586,5.911179,-7.686769,-9.184047,-3.554142,-7.114085],[0.387312,-5.460445,8.326809,8.804407,8.192046,9.171835,3.678710,-6.859388,5.046295,3.571557,-1.423754,9.606423,0.096676,-9.594092,5.663646,-6.392876],[2.412306,4.572882,2.577375,-9.309660,-5.870636,-0.955784,9.415603,5.469945,-3.867393,8.285408,5.168344,9.410140,7.820177,-6.358614,-5.318959,7.838457],[2.865309,-6.450054,8.892119,-6.075572,-0.744486,-9.298565,1.455460,9.048480,-0.074024,-1.635044,6.253100,-0.032984,8.021401,-7.288893,-0.862514,2.373576],[-7.873442,-3.874554,-0.284533,2.676202,7.223188,-9.848867,1.005034,-7.123063,-7.304663,-6.711691,-1.052789,-0.443623,6.140594,6.229428,2.687433,-6.763074],[-0.883129,5.724180,3.823906,-8.357537,-1.490006,7.061518,-1.867444,9.556128,-9.038308,-6.011787,9.358802,-6.387909,8.448682,-7.598798,-1.923331,6.324809]],[[2.076145,4.592480,2.385247,0.604010,-4.319374,-3.618633,8.253708,0.896068,4.757537,-6.571614,9.977756,4.941486,6.495026,7.056553,-7.016593,-9.323936],[4.597611,-5.978499,6.019440,0.292331,-4.528325,-5.843491,2.049303,4.603266,-7.674370,0.150950,-1.580610,-1.829509,-7.236346,0.741952,-1.231810,-1.986526],[1.481565,4.486076,6.526215,-8.632214,-5.386026,6.123522,7.358512,-0.035347,-4.105266,9.171215,-2.789983,-1.672505,7.752533,-6.725650,-2.072277,6.206679],[1.440373,-3.172295,5.232243,7.914554,-2.943701,-3.490556,8.884193,8.170199,-1.132265,3.152186,-9.543343,-9.251906,2.832700,-8.675432,2.039684,-2.654116],[-2.583606,9.867408,2.922387,4.170680,8.880306,8.142697,-3.395758,1.132426,7.916613,5.734914,-1.186811,2.524720,-0.502797,8.447301,-6.643317,9.167368],[5.400191,-7.951605,5.613527,-2.201923,2.156377,4.228052,-3.394137,2.901954,4.282825,6.301776,-7.020129,-9.918694,-0.023236,-5.538151,4.567423,6.182713],[8.786028,9.993857,0.610897,8.733353,-4.966169,-9.042609,6.615009,-8.275685,5.198078,6.538226,0.215538,-6.279439,1.721666,-5.764046,-2.476172,2.893593],[7.848369,-9.301099,-1.404556,-8.707945,6.650250,1.447994,-4.043932,4.739538,-4.609477,6.208183,-6.048140,4.804331,-6.914373,-0.207389,-5.397067,-0.657010],[4.995775,-1.683630,3.109598,-7.201151,-6.068007,0.585877,8.401702,-0.316266,7.311682,6.508761,4.072442,-9.440049,-2.463850,2.945302,-6.205239,5.347177],[-5.503275,-2.570205,-4.084915,-0.848711,-2.067181,4.370454,4.426861,6.417061,1.134655,-8.932751,-2.012279,-4.041642,-4.134049,1.127046,-1.038182,-7.308515],[-1.237137,-2.701981,2.665120,6.078636,-7.474825,8.586034,-1.860556,2.861527,-1.903595,0.791705,-0.871478,0.985703,2.804197,8.395524,5.281041,-3.711726],[-1.626818,-6.422036,-1.229143,-5.370214,-3.879879,-7.911657,-8.373055,-8.023945,0.894125,3.339130,-3.090489,-1.435357,1.521290,8.615413,2.978863,2.773275]],[[-2.099864,7.902000,8.310302,0.940393,-7.824450,9.648554,4.205191,6.491743,5.437403,-2.717121,5.243562,0.940307,8.321050,-9.129453,-7.538852,-7.443481],[9.936129,7.384906,0.676299,8.775545,-6.846175,6.675309,-8.406788,9.290560,8.425962,0.951233,-6.537254,-0.346035,4.774367,3.357501,-3.544308,-0.755203],[6.995958,-4.000671,5.343272,-3.850286,-0.709009,3.680839,-4.036720,-2.849190,2.549031,4.534968,-2.581896,6.963305,-1.181883,-9.206169,-8.976474,-6.278778],[-0.685694,7.025067,-5.760445,-6.170356,3.167843,-4.826470,-3.021514,6.404667,-5.635841,6.888887,-7.819788,2.105144,2.339379,1.357214,-1.521079,-4.184274],[9.992729,-0.747750,6.108275,-0.758573,9.935748,1.037884,-4.286115,9.327440,3.056341,1.830157,5.880794,-1.446340,-2.769418,-9.021859,3.465472,-7.174284],[-3.877566,0.959197,3.022255,-3.673660,-1.299905,-0.699671,7.231861,3.966659,-8.775781,-7.911119,3.527983,5.936555,8.797797,8.454491,-4.363359,5.302727],[-4.051853,-7.884211,-8.424461,-1.347385,-0.514065,5.799238,-7.599633,-5.277416,-2.495209,-9.802866,8.929829,8.157762,-4.884391,-0.685243,-7.030630,8.784078],[-5.668478,-4.598441,1.619241,2.604482,6.749900,0.245211,3.097062,8.752918,-9.848832,-8.929817,4.378924,-7.422406,-1.045628,-8.415824,-7.206520,7.485810],[6.115031,-9.807178,6.876643,2.344786,-6.856322,-9.525566,-8.947424,8.160965,-0.145921,7.186580,-6.591115,5.097608,-1.440156,6.307994,7.969203,7.427267],[4.961171,2.650508,6.416956,7.794094,0.768867,0.313300,3.562729,9.076389,-7.046164,3.256561,-9.661962,2.188439,-3.156284,-7.381436,-2.289009,9.743428],[4.778395,-3.110938,4.798547,-6.146778,6.981870,-9.445112,0.759932,-0.718331,-1.419444,-7.981086,-6.502309,8.612806,-4.439256,4.950966,6.843127,-6.197182],[7.831585,8.669744,2.682520,-1.271531,-4.052473,7.143389,-5.999881,8.743024,-5.578122,0.343435,-3.098106,6.567419,-9.015424,6.017113,5.099750,-1.588955]],[[-4.520367,1.090877,-9.806055,-0.874828,3.458143,-8.482666,-8.704606,-7.228577,9.954342,8.006234,7.184791,-6.236056,5.369345,1.907468,-6.646206,-2.398103],[-2.131255,-9.324392,6.514254,5.978199,-8.844959,-6.034443,2.390396,6.907725,-4.190863,-7.529233,-7.799178,-5.304978,-8.185299,-9.220570,7.333947,8.537780],[0.606288,-7.763965,0.361422,7.037280,7.118556,-9.850504,-1.948179,9.039755,-7.641115,-7.251347,0.614153,9.426463,9.118687,-4.695217,-2.120099,-5.819860],[6.368612,-1.776956,-4.038778,-8.693202,4.855280,-3.335690,6.846481,-5.270836,-4.029049,-0.926597,7.881504,3.447860,4.460741,-5.217274,-4.359234,6.817347],[7.751537,-6.885777,6.719608,-8.613330,2.226683,7.073723,-7.390923,-7.044051,-8.352002,-8.023458,-9.707636,-1.294368,0.605911,6.222256,3.095255,0.041184],[-6.073786,-3.071231,7.377224,-8.921155,-9.552115,8.281320,-2.915531,2.220508,-4.311309,-6.091829,1.801931,-1.637751,6.171960,-6.692105,7.087006,-0.759259],[2.035709,4.163125,2.127382,3.833782,5.623445,-9.745504,9.116974,4.798776,-2.214486,-8.251968,-2.456941,-7.238382,9.761204,0.552854,5.935379,-3.112612],[-4.490764,7.272686,-4.382018,7.456204,8.305746,3.478237,1.589959,-2.288382,-6.887788,-7.457171,6.536625,0.080693,2.534041,6.967801,-2.125015,-8.885727],[-8.306248,-1.772867,-1.485335,-2.151635,7.736419,-4.955885,-5.594795,-5.582064,-8.626159,-6.588504,-6.089446,-5.749921,-4.672328,-2.010880,2.324556,8.597032],[-3.785807,-8.388752,-1.650565,-5.785374,-7.270005,-0.178263,6.371870,-0.404003,7.101773,8.089449,-4.768092,-0.060576,-4.105452,5.558109,3.341178,1.725459],[-0.992869,-8.286701,-5.259137,-7.985446,-0.142187,-1.453106,-5.007395,1.973137,7.110449,0.266210,-7.853862,-5.458606,-8.707073,-9.916212,-9.320282,6.963463],[-2.814580,0.947231,-3.223714,8.965859,2.352555,-9.839872,-8.959609,0.783111,-0.900220,1.335867,-6.523244,6.275708,7.394318,-0.811319,5.087953,-1.428142]],[[-3.528712,2.019124,-8.831237,8.170938,-5.971104,9.405824,6.584833,-6.030013,4.953771,-4.633054,2.854660,-2.630022,4.102200,-0.282054,-7.096945,-6.693341],[5.638864,5.935834,5.794781,4.142620,-6.289742,-3.998491,3.153878,3.920915,7.019598,7.734267,-4.744331,4.103851,-3.235786,-2.653041,7.624667,5.866233],[-3.997860,-6.465658,0.434396,5.017096,-6.765830,8.388692,-7.931836,-3.141701,-9.936452,-9.232655,8.917023,8.885840,-6.346843,-4.164292,-7.359583,-0.646078],[-4.087984,-8.314112,-0.299279,2.184581,-2.188892,-3.367094,8.862382,-7.989554,-2.886022,-4.741060,-7.684819,-6.134167,-4.445306,-5.929415,-8.438241,8.034368],[5.243190,9.294800,-3.603147,-9.665750,0.012603,7.375951,1.625706,2.187208,1.869200,9.655322,1.440775,-7.092703,-4.903419,-9.064989,7.584399,2.765288],[-2.771052,-5.121175,1.486297,2.958268,6.088541,-5.601404,-5.462819,6.144533,3.322533,1.084899,-1.824846,-2.721959,6.762088,8.016482,6.368184,0.773574],[3.971861,-9.384429,9.733349,-8.682023,-0.124472,1.055057,-0.439672,-9.501472,-2.841276,-0.090508,0.757723,4.848821,8.178792,9.077015,-0.706486,-1.613196],[-2.461940,-3.142372,-9.405366,1.772270,3.230004,1.725197,5.437321,-9.139729,-5.599248,-3.938744,6.205664,-4.190695,-2.887542,0.659625,-9.791572,8.818590],[-7.042205,-5.029586,-1.974567,-6.755951,6.769185,2.527586,1.526563,-3.637011,-5.858844,-5.707001,-2.826107,-8.412979,-0.268642,8.377745,-7.818878,-2.715300],[2.831470,3.927469,-3.897594,6.255578,-8.405952,-3.033501,-3.965389,1.563187,9.509224,3.130019,-2.431897,-8.814061,1.488707,0.775514,-0.305160,3.988284],[7.022751,6.506120,-8.236180,2.853801,1.198251,-1.622143,-0.379983,-1.232006,8.043142,2.749401,-2.262856,4.239620,-9.877948,7.078213,-7.210280,-5.539025],[5.682509,5.445526,-0.567271,-3.080304,-3.534136,-6.546684,-8.023048,-4.761681,-9.988947,3.083401,6.846336,-3.403835,-9.558026,0.915145,-5.163398,-6.046944]],[[9.596759,3.124030,-4.218736,-7.842297,9.468100,2.728393,7.944707,6.688415,8.152544,-8.865901,5.302827,-0.969332,-0.359782,-4.619876,0.866894,9.955379],[-5.697730,0.921611,-0.627135,4.996522,-6.974000,-7.672690,-2.574792,2.450898,-4.410018,4.858187,-2.235202,9.693221,9.180695,-1.462372,-3.965274,2.399954],[-3.648413,3.087113,-8.312760,-5.089039,4.427293,1.214535,5.214732,-2.438332,-0.024238,9.206321,3.415402,-8.701831,4.603979,-0.947761,-7.666970,-7.487459],[-8.882258,1.031588,1.410421,8.244234,-2.334524,-3.571796,2.840202,-8.384569,-9.267723,-0.364360,-6.045932,-4.596571,2.449622,-9.758981,2.504903,2.368753],[-0.478697,-8.369056,-3.723710,9.848243,-2.001586,-8.996847,-1.368684,-5.446746,0.530450,-8.462464,9.832125,2.758473,7.089150,-2.838600,-1.538512,-8.008127],[-0.876961,-3.002360,-4.745439,-6.827102,-7.500147,-4.176755,9.266289,9.283168,-5.411986,-1.293600,8.160103,-9.212977,3.922302,5.304858,-5.553955,5.638327],[-6.490214,-9.754893,4.638062,-0.273398,5.630154,-0.123300,7.788606,6.858873,8.674073,2.554275,1.546961,-7.929060,-6.647170,3.179989,4.771899,4.126562],[-8.642929,5.286181,-8.990818,0.269432,-9.174528,-0.582831,-2.982186,6.534309,-5.544003,-7.859906,4.790571,-7.986651,-3.804360,-4.668956,-3.140988,2.966306],[8.175915,-0.921581,-7.321800,-0.466092,6.026441,-2.508974,-4.767071,-5.657088,-5.541932,0.321902,0.297542,4.786193,5.704684,5.278103,-5.606800,-4.742975],[9.636632,1.628827,7.495502,9.517557,0.513432,-2.001936,3.366673,-2.172001,8.332718,3.485989,5.213126,-2.450409,3.784198,2.997283,-2.741291,2.939616],[-5.184483,-6.972198,-9.147452,2.589935,3.250108,-2.673700,-5.731077,2.174914,-6.629629,-6.308725,7.102188,-6.406121,-5.050525,-7.230598,4.208874,8.086540],[1.113993,2.101551,2.311897,6.737381,-7.595461,1.008685,-3.219359,-0.571700,-5.104346,-7.694775,0.434798,-9.127795,-7.988698,5.983008,-4.078311,-9.532518]],[[-8.864845,-1.517152,-3.877515,-7.672622,1.932653,6.296704,-2.740029,-4.371700,-9.615616,8.788579,2.219631,1.970710,-7.851497,5.034019,9.177757,-7.227700],[-1.326601,1.078201,-9.739691,6.302136,-2.700919,1.081530,7.891546,3.969420,1.719102,4.433298,-1.211334,-6.766703,7.962745,4.128632,7.151057,-0.914558],[-8.827187,-0.956233,-8.196336,-8.712211,-8.166959,8.166483,7.246748,7.674904,5.433755,8.270718,-7.790863,2.452150,-6.231670,-3.749596,-6.211939,8.315714],[3.551165,-1.358737,2.905247,-1.716663,-7.169942,4.272459,-7.440017,-4.703563,-0.199870,1.153510,-0.757192,-7.838298,5.284676,-4.882640,-5.000675,2.410062],[-6.327480,7.429129,-9.273436,6.048030,9.837724,2.613218,-9.295266,-0.584373,8.966154,2.552489,-2.037665,-8.347920,-2.248609,1.471058,-0.963849,-5.543541],[-5.813134,7.115332,1.209607,-9.039402,8.065760,-4.154896,3.307542,-6.844060,-0.984825,-9.860808,-7.792745,4.054895,-9.814795,2.434316,2.161332,5.800136],[2.206106,-4.501132,0.656707,1.433015,-5.123292,-5.178002,-3.341018,8.966587,-6.243821,7.701115,-9.930004,-4.186857,-5.394624,-3.802637,1.359051,0.340011],[-3.715987,-6.746204,-8.846134,-8.970086,8.183871,0.272364,-0.983330,2.744147,-1.183720,8.338741,4.168255,9.415295,8.472009,6.638513,7.758654,8.569164],[-1.548083,-4.124282,3.976444,-3.343895,0.236226,9.303938,-7.355644,1.913111,4.861876,5.830026,-2.900234,-5.354130,-1.079379,-2.485621,9.044786,1.687790],[9.340519,-6.449309,3.307669,-7.723781,-6.980249,-8.424950,-3.749933,-1.467106,-3.536770,-6.126258,-1.362888,-4.403194,-4.906362,4.515642,-3.823166,8.285183],[-9.369265,-7.994667,-6.833568,-9.711110,-1.863149,8.530495,-3.073312,3.813867,-5.872167,2.924281,-5.912647,6.161601,1.624189,-5.548133,-3.541688,9.081407],[-4.507905,-0.517755,-4.316256,5.480910,3.307355,4.051977,-4.556732,-2.664494,-9.724727,-2.263719,6.199188,0.027459,-8.696798,-9.542926,-7.831293,8.413708]],[[5.632393,0.660898,-9.817206,3.703302,-5.670896,-8.136454,6.361223,7.733391,-4.647214,-9.481888,3.636476,-5.811753,-1.535020,-4.024208,2.584395,8.026108],[2.969527,-3.149959,5.333549,3.172724,4.990032,8.015168,-6.358015,-5.370066,-0.115277,-5.526428,2.302887,7.102809,6.001511,-4.862282,9.627232,-4.472964],[-8.399442,-2.886945,-0.505083,4.201238,8.281106,-3.088125,9.547918,8.330531,3.170460,-2.101959,-0.646510,-8.857292,0.493731,-4.543781,-8.178364,-1.401293],[-3.011576,6.357801,-3.645977,-8.619601,2.443010,-3.185097,1.754947,-3.690358,7.273406,8.896110,-3.609926,-4.569224,-6.767837,-9.795325,8.078864,-3.766824],[0.659398,-5.336144,-9.865556,-2.977809,0.477175,3.668080,-5.602607,6.859111,-6.363661,0.241666,5.611135,-7.841501,3.329559,-1.425816,1.040756,-8.132148],[-6.609493,8.210145,8.316958,-6.642014,-8.913451,6.526437,0.875448,-6.111747,-8.192361,-7.525116,3.815324,4.504289,9.362985,7.099838,-4.152451,-6.615778],[-9.963809,-3.020974,3.753936,-5.878280,-2.054824,-2.509473,2.845527,8.956417,-7.998735,9.188719,-1.281981,-6.475378,-3.679754,0.503774,7.444473,-3.215232],[5.101089,3.993067,7.700141,-6.114239,-2.747083,-6.560458,6.985934,2.449472,3.740066,-7.066987,2.444867,-1.566089,-6.780900,8.324382,6.928698,-2.847857],[-8.663485,5.997967,5.965768,6.213587,-5.267009,9.854475,6.772225,1.274217,0.101547,-0.137557,8.117073,2.300555,-9.129867,9.192301,-0.548573,-0.786363],[-5.151898,-7.172139,2.285709,7.875283,7.884274,-0.782589,0.737943,-6.851497,7.284353,5.333026,0.737902,-6.657772,8.547879,2.284887,0.793010,-9.485539],[1.124041,-3.055536,-7.600077,-8.887307,-5.827027,-7.496762,-7.142832,6.373259,-7.881952,-4.544351,5.665678,9.232927,6.952721,-0.706505,3.474682,-4.010574],[3.919005,2.204440,-9.018839,-3.800855,-7.530543,-1.269069,4.906408,-0.812404,-7.191983,0.570608,-4.493059,8.140041,5.573584,-4.504390,-0.715970,6.053705]]], dtype = "float32")#candidate|8732|(11, 12, 16)|const|float32
bop_8733 = relay.minimum(call_8699.astype('int8'), relay.reshape(const_8732.astype('int8'), relay.shape_of(call_8699))) # shape=(11, 12, 16)
bop_8736 = relay.minimum(call_8700.astype('int8'), relay.reshape(const_8732.astype('int8'), relay.shape_of(call_8700))) # shape=(11, 12, 16)
output = relay.Tuple([call_8705,const_8706,bop_8733,])
output2 = relay.Tuple([call_8707,const_8706,bop_8736,])
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
